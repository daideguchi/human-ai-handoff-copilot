# Human-AI Handoff Copilot

Human-AI Handoff Copilot is a Microsoft Agent Academy submission package for one practical problem:

> When an AI agent cannot safely finish a task alone, how does the next human or AI continue without losing context?

The prototype runs a support escalation case, builds a required-field handoff packet, blocks the risky customer-facing action, verifies that the next actor can resume, and packages the workflow as Copilot Studio-ready instructions, action contracts, and an Adaptive Card.

## Judge Quick Read

- **Who it helps:** support leads, operations managers, and future agent supervisors who need AI work to pause cleanly instead of disappearing into chat history.
- **Problem:** AI agents often do useful work, but the moment a human needs to approve, audit, or continue the work, evidence and context get scattered.
- **Solution:** a handoff packet that preserves the case, evidence IDs, draft response, cost guardrail, blocked action, approval requirement, resume instructions, and packet hash.
- **Microsoft fit:** Copilot Studio-ready agent instructions/actions/card plus a live Microsoft Graph public service-root contract check for Teams, chats, Planner, drives, and sites.
- **Honest boundary:** verified local handoff agent and Microsoft integration contract. The official final issue form requires confirming use of Copilot Studio, Microsoft 365 Copilot, or Copilot Cowork, so final submission should wait until that product execution/import is verified.

## Live Links

- Live demo: https://daideguchi.github.io/human-ai-handoff-copilot/
- GitHub: https://github.com/daideguchi/human-ai-handoff-copilot
- YouTube demo: https://www.youtube.com/watch?v=asbgvArrqXU
- Submission package: [SUBMISSION_PACKAGE.md](SUBMISSION_PACKAGE.md)
- Architecture: [ARCHITECTURE.md](ARCHITECTURE.md)
- Demo video file: [microsoft-agent-academy/media/human-ai-handoff-copilot-demo.mp4](microsoft-agent-academy/media/human-ai-handoff-copilot-demo.mp4)

## Demo

![Human-AI Handoff Copilot architecture](microsoft-agent-academy/media/handoff-copilot-architecture-full.png)

The demo video has natural English narration and is generated from the current verified artifacts.

```text
YouTube: https://www.youtube.com/watch?v=asbgvArrqXU
microsoft-agent-academy/media/human-ai-handoff-copilot-demo.mp4
```

## What Is Working

- A local handoff agent produces `handoff-packet.json`.
- Required handoff fields are validated at 100%.
- The customer-facing send is blocked until manager approval.
- A resume proof confirms the next actor can continue.
- Microsoft Graph service root is checked live without reading tenant/user data.
- Copilot Studio-ready instructions, action contracts, and Adaptive Card assets are included.
- The demo video, screenshots, and reports are generated from the repo.

## Verification

Run the full Microsoft lane check:

```bash
bash microsoft-agent-academy/scripts/run_microsoft_local_checks.sh
```

Expected proof:

```text
microsoft_local_checks_ok
required_fields=9
handoff_completeness=1.0
resumable_by_next_actor=True
approval_required=true
microsoft_graph_contract=ok
video_seconds=74.7
claim_boundary=verified_local_handoff_agent_no_live_copilot_studio_execution_claim
```

## Key Files

- [microsoft-agent-academy/scripts/run_handoff_copilot.py](microsoft-agent-academy/scripts/run_handoff_copilot.py) - local handoff agent runner
- [microsoft-agent-academy/scripts/check_microsoft_graph_contract.py](microsoft-agent-academy/scripts/check_microsoft_graph_contract.py) - live Microsoft Graph service-root check
- [microsoft-agent-academy/reports/handoff-packet.json](microsoft-agent-academy/reports/handoff-packet.json) - the generated handoff packet
- [microsoft-agent-academy/reports/resume-proof.json](microsoft-agent-academy/reports/resume-proof.json) - resumability proof
- [microsoft-agent-academy/reports/microsoft-graph-contract.json](microsoft-agent-academy/reports/microsoft-graph-contract.json) - Microsoft Graph contract proof
- [microsoft-agent-academy/copilot_studio/agent-instructions.md](microsoft-agent-academy/copilot_studio/agent-instructions.md) - Copilot Studio behavior draft
- [microsoft-agent-academy/copilot_studio/actions.json](microsoft-agent-academy/copilot_studio/actions.json) - action contracts
- [microsoft-agent-academy/copilot_studio/adaptive-card-handoff.json](microsoft-agent-academy/copilot_studio/adaptive-card-handoff.json) - manager approval card

## Story

Human-AI collaboration should not mean "AI does everything" or "humans restart from zero." The real future is handoff: humans and agents working in the same flow, with enough evidence and responsibility preserved that either side can continue safely.

That is why this project treats handoff as an agent capability, not a side note.

## Claim Boundary

Safe claim:

- Verified local handoff agent.
- Copilot Studio-ready implementation assets.
- Live Microsoft Graph service-root contract check.
- Natural-English demo video and public GitHub Pages demo.

Not claimed:

- Live Copilot Studio import/execution.
- Confirmed use of Copilot Studio, Microsoft 365 Copilot, or Copilot Cowork inside a live Microsoft environment.
- Authenticated Microsoft tenant data access.
- Final GitHub issue submission.
- Any customer-facing action sent without approval.
