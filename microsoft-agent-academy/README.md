# Microsoft Agent Academy Lane

This folder contains the Microsoft-focused implementation for **Human-AI Handoff Copilot**.

## One Sentence

A Copilot-style handoff agent that preserves evidence, approvals, cost guardrails, blocked actions, and resume instructions when work moves from AI to a human manager or another AI.

## Current Status

Deep local package. Final GitHub issue submission is blocked until the official Microsoft product-use checkbox can be satisfied honestly.

Verified:

- local handoff agent runs
- required handoff fields are present
- customer-facing send stays blocked until approval
- next actor can resume from the packet
- Microsoft Graph public service-root contract is checked live
- Copilot Studio-ready instructions/actions/card exist
- natural English demo video is generated

Public demo video:

- https://www.youtube.com/watch?v=asbgvArrqXU

Not claimed:

- live Copilot Studio execution
- confirmed use of Copilot Studio, Microsoft 365 Copilot, or Copilot Cowork inside a live Microsoft environment
- authenticated tenant/user data access
- final GitHub issue submission

## Run

From the repo root:

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

## Core Artifacts

- `scripts/run_handoff_copilot.py` - local handoff agent runner
- `scripts/check_microsoft_graph_contract.py` - live Microsoft Graph public service-root check
- `scripts/build_handoff_copilot_architecture.py` - builds the architecture demo and GitHub issue draft
- `scripts/build_demo_video.sh` - builds the narrated demo video
- `case_data/support_escalation_case.json` - support case
- `case_data/policy_source.md` - approved policy source
- `case_data/agent_worklog.jsonl` - evidence worklog
- `reports/handoff-packet.json` - generated handoff packet
- `reports/resume-proof.json` - resumability proof
- `reports/microsoft-graph-contract.json` - Microsoft Graph contract report
- `copilot_studio/agent-instructions.md` - Copilot Studio-ready instructions
- `copilot_studio/actions.json` - action contracts
- `copilot_studio/adaptive-card-handoff.json` - manager approval card

## Product Flow

1. Customer asks for a refund exception.
2. Agent retrieves approved policy evidence.
3. Agent drafts a careful response.
4. Agent detects that the next action is customer-facing and financial.
5. Agent blocks `send_customer_reply`.
6. Agent creates a required-field handoff packet.
7. Manager or future AI resumes from the packet instead of the raw chat.

## Microsoft Mapping

- **Copilot Studio:** instructions, actions, and Adaptive Card approval shape.
- **Microsoft Graph:** live service-root contract verifies Teams, chats, Planner, drives, and sites are available as integration surfaces.
- **Teams:** target channel for manager approval.
- **Planner:** target for resume task creation.
- **Drive / SharePoint:** target storage for policy evidence and handoff packets.

## Submission Routes Observed

- Event page: `https://microsoft.github.io/agent-academy/events/hackathon/`
- Register route: `https://aka.ms/agent-academy-live/register`
- Reactor event route: `https://developer.microsoft.com/en-us/reactor/events/27042/`
- Submit route: `https://aka.ms/agent-academy-hack/submit`
- Final GitHub issue route: `https://github.com/microsoft/agent-academy/issues/new?template=hack-submission.yml`

Do not execute the final GitHub issue submission until the finished artifact is approved.

The final issue template requires a checkbox confirming that the agent uses
Copilot Studio, Microsoft 365 Copilot, or Copilot Cowork. This repo currently
contains Copilot Studio-ready assets and a Microsoft Graph contract check, but
does not claim live product execution.

## Why This Matters

Human-AI work will not be a single actor doing everything. Real operations will involve agents drafting, humans approving, future agents resuming, and teams auditing what happened. This project makes that handoff explicit, verifiable, and reusable.
