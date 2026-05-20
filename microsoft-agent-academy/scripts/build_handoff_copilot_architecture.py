#!/usr/bin/env python3
"""Build the Microsoft Agent Academy handoff architecture artifact."""

from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SHARED_ROOT = ROOT.parent / "shared-agentops-engine"
WORKFLOW_FILE = SHARED_ROOT / "adapters" / "google" / "gemini_mcp_workflow.json"
ARCH_SOURCE = SHARED_ROOT / "adapters" / "microsoft" / "copilot_architecture.md"
OUT_FILE = ROOT / "prototype" / "handoff-copilot-architecture.html"
ISSUE_DRAFT = ROOT / "reports" / "github-issue-draft.md"


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def build_flow_cards(events: list[dict[str, Any]]) -> str:
    cards: list[str] = []
    for index, event in enumerate(events, start=1):
        cards.append(
            f"""
            <article class="flow-card">
              <span class="step">{index:02d}</span>
              <h3>{esc(event["phase"].replace("_", " ").title())}</h3>
              <p>{esc(event["summary"])}</p>
              <span class="event-id">{esc(event["event_id"])}</span>
            </article>
            """
        )
    return "\n".join(cards)


def build_html(workflow: dict[str, Any]) -> str:
    events = workflow["events"]
    flow_cards = build_flow_cards(events)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Human-AI Handoff Copilot — Microsoft Agent Academy Demo</title>
  <style>
    :root {{
      --bg: #f5f7fb;
      --surface: #fff;
      --ink: #1f2937;
      --muted: #667085;
      --line: #d8e0ea;
      --blue: #2563eb;
      --blue-soft: #eaf0ff;
      --purple: #6941c6;
      --purple-soft: #f1ecff;
      --green: #0b8043;
      --green-soft: #e8f5ec;
      --shadow: 0 16px 36px rgba(31, 41, 55, 0.08);
    }}

    * {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.5;
    }}

    main {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 28px 18px 48px;
    }}

    .locator {{
      color: var(--muted);
      font-size: 13px;
      margin-bottom: 12px;
    }}

    .hero {{
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 28px;
      box-shadow: var(--shadow);
      display: grid;
      grid-template-columns: minmax(0, 1.25fr) minmax(280px, 0.75fr);
      gap: 24px;
      align-items: start;
    }}

    h1 {{
      margin: 0;
      font-size: 34px;
      line-height: 1.12;
      letter-spacing: 0;
    }}

    h2 {{
      margin: 0 0 12px;
      font-size: 20px;
      letter-spacing: 0;
    }}

    h3 {{
      margin: 10px 0 6px;
      font-size: 16px;
      letter-spacing: 0;
    }}

    p {{ margin: 0; }}

    .hero-copy {{
      margin-top: 14px;
      color: var(--muted);
      font-size: 16px;
      max-width: 760px;
    }}

    .handoff-card {{
      background: var(--blue-soft);
      border: 1px solid #bfd0ff;
      border-radius: 8px;
      padding: 16px;
    }}

    .handoff-card strong {{
      color: #174ea6;
      display: block;
      margin-bottom: 8px;
    }}

    .metrics {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
      margin-top: 22px;
    }}

    .metric,
    .section,
    .flow-card {{
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: 0 8px 24px rgba(31, 41, 55, 0.04);
    }}

    .metric {{
      padding: 16px;
      min-height: 108px;
    }}

    .metric strong {{
      display: block;
      font-size: 28px;
      line-height: 1;
      margin-bottom: 8px;
    }}

    .metric span {{
      color: var(--muted);
      font-size: 13px;
    }}

    .section {{
      margin-top: 22px;
      padding: 20px;
    }}

    .component-grid {{
      display: grid;
      grid-template-columns: repeat(5, minmax(0, 1fr));
      gap: 10px;
    }}

    .component {{
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
      background: #fff;
      min-height: 116px;
    }}

    .component strong {{
      display: block;
      margin-bottom: 6px;
    }}

    .component span {{
      color: var(--muted);
      font-size: 13px;
    }}

    .flow-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 12px;
    }}

    .flow-card {{
      padding: 16px;
      min-height: 184px;
    }}

    .step,
    .event-id {{
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
      color: var(--blue);
      font-size: 12px;
      font-weight: 800;
      white-space: nowrap;
    }}

    .decision {{
      background: var(--green-soft);
      border: 1px solid #a7ddbd;
      border-radius: 8px;
      padding: 16px;
      color: #0b3d24;
    }}

    @media (max-width: 920px) {{
      .hero,
      .metrics,
      .component-grid,
      .flow-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    @media (max-width: 620px) {{
      main {{ padding: 16px 12px 32px; }}
      h1 {{ font-size: 27px; }}
    }}
  </style>
</head>
<body>
  <main>
    <div class="locator">Microsoft Agent Academy · Human-AI Handoff Copilot · Demo Artifact</div>

    <section class="hero">
      <div>
        <h1>Agents should know when to hand off, what to preserve, and how humans can resume.</h1>
        <p class="hero-copy">
          Human-AI Handoff Copilot packages a support workflow into a Copilot-style architecture:
          retrieve evidence, draft carefully, evaluate cost/risk, ask for approval, then preserve the handoff trail.
        </p>
      </div>
      <aside class="handoff-card">
        <strong>Final submission boundary</strong>
        <p>The GitHub issue submission route exists, but final submission must remain blocked until DD approves the finished artifact.</p>
      </aside>
    </section>

    <section class="metrics">
      <div class="metric"><strong>{len(events)}</strong><span>handoff events</span></div>
      <div class="metric"><strong>1</strong><span>human approval checkpoint</span></div>
      <div class="metric"><strong>Graph</strong><span>Microsoft product contract checked live</span></div>
      <div class="metric"><strong>0</strong><span>final submission actions executed</span></div>
    </section>

    <section class="section">
      <h2>Copilot Architecture Components</h2>
      <div class="component-grid">
        <article class="component"><strong>Conversational intake</strong><span>Support manager asks for help with a customer issue.</span></article>
        <article class="component"><strong>Policy retrieval</strong><span>Approved source material is fetched before drafting.</span></article>
        <article class="component"><strong>Drafting agent</strong><span>The answer cites the retrieved policy evidence.</span></article>
        <article class="component"><strong>Approval card</strong><span>Human approves escalation-only model usage.</span></article>
        <article class="component"><strong>Microsoft Graph contract</strong><span>Teams, chats, Planner, drives, and sites are validated against the public Graph service root.</span></article>
      </div>
    </section>

    <section class="section">
      <h2>Handoff Flow</h2>
      <div class="flow-grid">{flow_cards}</div>
    </section>

    <section class="section">
      <h2>Human Approval Decision</h2>
      <div class="decision">
        <strong>evt-0025 · support-manager approved escalation-only model usage</strong>
        <p>Costly model calls are not automatic. They become a policy-controlled escalation path.</p>
      </div>
    </section>
  </main>
</body>
</html>
"""


def write_issue_draft(workflow: dict[str, Any]) -> None:
    lines = [
        "# GitHub Issue Draft — Human-AI Handoff Copilot",
        "",
        "Do not submit this issue until DD explicitly approves.",
        "",
        "## Project",
        "",
        "Human-AI Handoff Copilot",
        "",
        "## Summary",
        "",
        "A Copilot-style workflow for moving support operations between AI agents and humans without losing evidence, cost guardrails, approval decisions, or handoff context.",
        "",
        "## Current Artifacts",
        "",
        "- Live demo: `https://daideguchi.github.io/human-ai-handoff-copilot/`",
        "- YouTube demo: `https://www.youtube.com/watch?v=asbgvArrqXU`",
        "- Repository: `https://github.com/daideguchi/human-ai-handoff-copilot`",
        "- `prototype/handoff-copilot-architecture.html`",
        "- `prototype/terminal-session.html`",
        "- `reports/handoff-packet.json`",
        "- `reports/resume-proof.json`",
        "- `reports/handoff-quality-report.md`",
        "- `reports/microsoft-graph-contract.json`",
        "- `media/handoff-copilot-architecture-full.png`",
        "- `media/handoff-terminal-session-full.png`",
        "- `media/human-ai-handoff-copilot-demo.mp4`",
        "- `copilot_studio/agent-instructions.md`",
        "- `copilot_studio/actions.json`",
        "- `copilot_studio/adaptive-card-handoff.json`",
        "- `../shared-agentops-engine/adapters/microsoft/copilot_architecture.md`",
        "",
        "## Verification",
        "",
        "```bash",
        "bash microsoft-agent-academy/scripts/run_microsoft_local_checks.sh",
        "```",
        "",
        "Expected proof:",
        "",
        "```text",
        "microsoft_local_checks_ok",
        "handoff_completeness=1.0",
        "resumable_by_next_actor=True",
        "microsoft_graph_contract=ok",
        "claim_boundary=verified_local_handoff_agent_no_live_copilot_studio_execution_claim",
        "```",
        "",
        "## Evidence Events",
        "",
    ]
    for event in workflow["events"]:
        lines.append(f"- `{event['event_id']}` {event['summary']}")
    lines.extend(
        [
            "",
        "## Boundary",
        "",
        "This is a verified local handoff-agent package with Copilot Studio-ready assets and a live Microsoft Graph service-root contract check. The official final issue template requires confirming use of Copilot Studio, Microsoft 365 Copilot, or Copilot Cowork, so do not submit or claim eligibility until one of those product paths is actually verified.",
        ]
    )
    ISSUE_DRAFT.parent.mkdir(parents=True, exist_ok=True)
    ISSUE_DRAFT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    workflow = json.loads(WORKFLOW_FILE.read_text(encoding="utf-8"))
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(build_html(workflow), encoding="utf-8")
    write_issue_draft(workflow)
    print(
        json.dumps(
            {
                "status": "ok",
                "source": str(ARCH_SOURCE.relative_to(ROOT.parent)),
                "output": str(OUT_FILE.relative_to(ROOT)),
                "issue_draft": str(ISSUE_DRAFT.relative_to(ROOT)),
                "event_count": len(workflow["events"]),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
