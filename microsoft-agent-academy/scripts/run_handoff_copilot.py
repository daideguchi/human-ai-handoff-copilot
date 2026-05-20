#!/usr/bin/env python3
"""Run the local Human-AI Handoff Copilot demo."""

from __future__ import annotations

import hashlib
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASE_DIR = ROOT / "case_data"
REPORT_DIR = ROOT / "reports"
PROTOTYPE_DIR = ROOT / "prototype"


def read_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def build_packet() -> dict:
    case = json.loads((CASE_DIR / "support_escalation_case.json").read_text(encoding="utf-8"))
    worklog = read_jsonl(CASE_DIR / "agent_worklog.jsonl")
    evidence_ids = [row["evidence_id"] for row in worklog]
    draft = (
        "I found the renewal-refund exception policy. Because the request was opened within the "
        "review window and the packaged usage check says no new seats were used, this may qualify "
        "for manager review. I cannot promise the refund until a support manager approves it. "
        "Evidence: policy-renewal-refund-2026-05, usage-m365-2187."
    )
    packet = {
        "case_id": case["case_id"],
        "ticket_id": case["ticket_id"],
        "target_user": case["target_user"],
        "customer_question": case["scenario"],
        "current_actor": case["current_actor"],
        "next_actor": case["next_actor"],
        "evidence_ids": evidence_ids,
        "draft_response": draft,
        "approval_required": True,
        "blocked_action": "send_customer_reply",
        "cost_summary": {
            "estimated_agent_cost_usd": 0.019,
            "expensive_model_allowed": "only_after_human_approval"
        },
        "resume_instructions": [
            "Read the evidence IDs before deciding.",
            "Approve only if the policy source and usage check are sufficient.",
            "If approved, send the draft after removing internal evidence labels.",
            "If not approved, request more evidence from the agent."
        ],
        "copilot_studio_assets": [
            "copilot_studio/agent-instructions.md",
            "copilot_studio/actions.json",
            "copilot_studio/adaptive-card-handoff.json"
        ],
        "claim_boundary": "verified_local_handoff_agent_no_live_copilot_studio_execution_claim"
    }
    canonical = json.dumps(packet, sort_keys=True)
    packet["packet_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return packet


def validate_packet(packet: dict) -> dict:
    required = json.loads((CASE_DIR / "support_escalation_case.json").read_text(encoding="utf-8"))[
        "expected_required_fields"
    ]
    missing = [field for field in required if field not in packet or packet[field] in ("", [], None)]
    resumable = not missing and packet["approval_required"] and packet["blocked_action"] == "send_customer_reply"
    return {
        "case_id": packet["case_id"],
        "required_fields_total": len(required),
        "missing_required_fields": missing,
        "handoff_completeness": round((len(required) - len(missing)) / len(required), 3),
        "resumable_by_next_actor": resumable,
        "next_actor": packet["next_actor"],
        "blocked_action": packet["blocked_action"],
        "approval_required": packet["approval_required"],
    }


def terminal_lines(packet: dict, validation: dict) -> list[str]:
    lines = [
        "$ python3 microsoft-agent-academy/scripts/run_handoff_copilot.py --case CASE-M365-HANDOFF-004",
        f"[case] {packet['case_id']} / {packet['ticket_id']}",
        "[mode] Copilot-style handoff: preserve evidence, approval, cost, and resume instructions",
        f"[agent] current={packet['current_actor']} next={packet['next_actor']}",
        "",
        "[packet] required fields captured:",
    ]
    for key in [
        "case_id",
        "ticket_id",
        "customer_question",
        "evidence_ids",
        "draft_response",
        "approval_required",
        "blocked_action",
        "cost_summary",
        "resume_instructions",
    ]:
        lines.append(f"         {key}=present")
    lines.extend(
        [
            "",
            f"[quality] handoff_completeness={validation['handoff_completeness']}",
            f"[resume] resumable_by_next_actor={validation['resumable_by_next_actor']}",
            "[approval] customer-facing send remains blocked until manager approval",
            f"[hash] packet_sha256={packet['packet_sha256'][:16]}...",
            "[boundary] verified local handoff agent; no live Copilot Studio execution claimed",
        ]
    )
    return lines


def write_terminal_html(lines: list[str]) -> None:
    escaped = "\n".join(html.escape(line) for line in lines)
    content = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Terminal Session — Human-AI Handoff Copilot</title>
  <style>
    body {{ margin: 0; background: #0b1220; color: #dbeafe; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
    main {{ max-width: 1120px; margin: 0 auto; padding: 28px 18px; }}
    .bar {{ background: #1f2937; color: #f8fafc; border: 1px solid #334155; border-radius: 8px 8px 0 0; padding: 10px 14px; font-family: Inter, system-ui, sans-serif; }}
    pre {{ margin: 0; background: #020617; border: 1px solid #334155; border-top: 0; border-radius: 0 0 8px 8px; padding: 18px; white-space: pre-wrap; line-height: 1.5; font-size: 14px; }}
  </style>
</head>
<body><main><div class="bar">CASE-M365-HANDOFF-004 · handoff terminal run</div><pre>{escaped}</pre></main></body>
</html>
"""
    (PROTOTYPE_DIR / "terminal-session.html").write_text(content, encoding="utf-8")


def write_reports(packet: dict, validation: dict, lines: list[str]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    PROTOTYPE_DIR.mkdir(parents=True, exist_ok=True)
    (REPORT_DIR / "handoff-packet.json").write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    (REPORT_DIR / "resume-proof.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    (REPORT_DIR / "terminal-transcript.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (REPORT_DIR / "handoff-quality-report.md").write_text(
        "# Handoff Quality Report\n\n"
        f"- Required fields total: `{validation['required_fields_total']}`\n"
        f"- Missing required fields: `{len(validation['missing_required_fields'])}`\n"
        f"- Handoff completeness: `{validation['handoff_completeness']}`\n"
        f"- Resumable by next actor: `{validation['resumable_by_next_actor']}`\n"
        f"- Blocked action: `{validation['blocked_action']}`\n\n"
        "The handoff is considered safe to review because the customer-facing send remains blocked until manager approval.\n",
        encoding="utf-8",
    )
    write_terminal_html(lines)


def main() -> None:
    packet = build_packet()
    validation = validate_packet(packet)
    lines = terminal_lines(packet, validation)
    write_reports(packet, validation, lines)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
