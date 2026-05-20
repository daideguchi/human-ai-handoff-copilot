#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPO_ROOT="$(cd "$ROOT/.." && pwd)"

cd "$REPO_ROOT/shared-agentops-engine"
python3 scripts/generate_portfolio_artifacts.py >/tmp/microsoft-shared-generate.log
python3 scripts/verify_artifacts.py >/tmp/microsoft-shared-verify.log

cd "$REPO_ROOT"
python3 microsoft-agent-academy/scripts/run_handoff_copilot.py >/tmp/microsoft-terminal.log
python3 microsoft-agent-academy/scripts/check_microsoft_graph_contract.py >/tmp/microsoft-graph-contract.log
python3 microsoft-agent-academy/scripts/build_handoff_copilot_architecture.py >/tmp/microsoft-architecture.log
bash microsoft-agent-academy/scripts/build_demo_video.sh >/tmp/microsoft-video.log

python3 - <<'PY'
import json
import subprocess
from pathlib import Path

root = Path("microsoft-agent-academy")
required = [
    root / "reports" / "handoff-packet.json",
    root / "reports" / "resume-proof.json",
    root / "reports" / "handoff-quality-report.md",
    root / "reports" / "microsoft-graph-contract.json",
    root / "reports" / "terminal-transcript.txt",
    root / "reports" / "github-issue-draft.md",
    root / "prototype" / "terminal-session.html",
    root / "prototype" / "handoff-copilot-architecture.html",
    root / "media" / "human-ai-handoff-copilot-demo.mp4",
    root / "copilot_studio" / "agent-instructions.md",
    root / "copilot_studio" / "actions.json",
    root / "copilot_studio" / "adaptive-card-handoff.json",
]
missing = [str(path) for path in required if not path.exists() or path.stat().st_size == 0]
if missing:
    raise SystemExit(f"missing outputs: {missing}")

packet = json.loads((root / "reports" / "handoff-packet.json").read_text())
proof = json.loads((root / "reports" / "resume-proof.json").read_text())
graph = json.loads((root / "reports" / "microsoft-graph-contract.json").read_text())
if proof["missing_required_fields"]:
    raise SystemExit(f"handoff missing fields: {proof['missing_required_fields']}")
if proof["handoff_completeness"] != 1:
    raise SystemExit("handoff completeness is not 1")
if not proof["resumable_by_next_actor"]:
    raise SystemExit("handoff is not resumable")
if not packet["approval_required"]:
    raise SystemExit("approval gate missing")
if not graph["reachable"] or graph["uses_authenticated_tenant_data"]:
    raise SystemExit("Microsoft Graph contract check did not pass")
if graph["missing_entity_sets"]:
    raise SystemExit(f"Microsoft Graph contract missing entity sets: {graph['missing_entity_sets']}")

transcript = (root / "reports" / "terminal-transcript.txt").read_text()
for needle in [
    "handoff_completeness=1.0",
    "resumable_by_next_actor=True",
    "customer-facing send remains blocked",
    "no live Copilot Studio execution claimed",
]:
    if needle not in transcript:
        raise SystemExit(f"transcript missing: {needle}")

duration = float(subprocess.check_output([
    "ffprobe", "-v", "error", "-show_entries", "format=duration",
    "-of", "default=nw=1:nk=1", str(root / "media" / "human-ai-handoff-copilot-demo.mp4")
], text=True).strip())
if duration < 45 or duration > 300:
    raise SystemExit(f"demo video duration out of bounds: {duration}")
audio = subprocess.check_output([
    "ffprobe", "-v", "error", "-select_streams", "a",
    "-show_entries", "stream=codec_type", "-of", "csv=p=0",
    str(root / "media" / "human-ai-handoff-copilot-demo.mp4")
], text=True).strip()
if "audio" not in audio:
    raise SystemExit("demo video missing audio")

print("microsoft_local_checks_ok")
print(f"required_fields={proof['required_fields_total']}")
print(f"handoff_completeness={proof['handoff_completeness']}")
print(f"resumable_by_next_actor={proof['resumable_by_next_actor']}")
print("approval_required=true")
print("microsoft_graph_contract=ok")
print(f"video_seconds={duration:.1f}")
print("claim_boundary=verified_local_handoff_agent_no_live_copilot_studio_execution_claim")
PY
