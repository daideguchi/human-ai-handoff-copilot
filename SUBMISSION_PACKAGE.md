# Submission Package - Human-AI Handoff Copilot

## Project Title

Human-AI Handoff Copilot

## Short Description

A Copilot-style handoff agent that preserves evidence, approvals, cost guardrails, and resume instructions when work moves from AI to a human manager or another AI.

## Repository

https://github.com/daideguchi/human-ai-handoff-copilot

## Live Demo

https://daideguchi.github.io/human-ai-handoff-copilot/

## Demo Video

YouTube:

- https://www.youtube.com/watch?v=asbgvArrqXU

Local video file:

- `microsoft-agent-academy/media/human-ai-handoff-copilot-demo.mp4`

The video is generated from the current repo artifacts with natural English narration.

Regenerate:

```bash
bash microsoft-agent-academy/scripts/build_demo_video.sh
```

## Try It Out

Open:

- `index.html`
- `microsoft-agent-academy/prototype/handoff-copilot-architecture.html`
- `microsoft-agent-academy/prototype/terminal-session.html`
- `shared-agentops-engine/web/index.html`

## Screenshots

- `microsoft-agent-academy/media/handoff-copilot-architecture-full.png`
- `microsoft-agent-academy/media/handoff-terminal-session-full.png`
- `shared-agentops-engine/media/shared-dashboard-full.png`

## Inspiration

I do not think the future is just "AI replaces humans." The more realistic future is that humans and AI keep passing work to each other.

That is powerful, but only if the handoff is trustworthy. If the AI did useful work but the next person cannot see the evidence, approval status, cost risk, and exact next step, the team has to start over.

Human-AI Handoff Copilot was built around that idea: the best agents are not the ones that pretend to finish everything alone. The best agents know when to pause and preserve enough context for the next human or AI to continue.

## What It Does

The prototype runs a support escalation case:

1. A customer asks for a renewal refund exception.
2. The agent retrieves the policy and worklog evidence.
3. The agent drafts a careful response.
4. The agent sees that the next action is customer-facing and financial.
5. The send action is blocked.
6. A required-field handoff packet is generated.
7. A resume proof confirms that the next actor can continue safely.
8. Microsoft Graph contract validation confirms the integration surface for Teams, chats, Planner, drives, and sites.

## How We Built It

- Python local handoff agent.
- JSON/JSONL case data and worklog evidence.
- HTML public demo and terminal proof page.
- Copilot Studio-ready agent instructions.
- Copilot Studio-style action contracts.
- Adaptive Card manager approval shape.
- Microsoft Graph public service-root contract check.
- Shared AgentOps timeline reused from the portfolio engine.

## Built With

- Python
- HTML/CSS
- JSON / JSONL
- Microsoft Graph public service root
- Copilot Studio-ready instructions/actions/card
- ffmpeg
- Edge TTS neural narration

## Working Proof

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

## Verification Command

```bash
bash microsoft-agent-academy/scripts/run_microsoft_local_checks.sh
```

## What Makes It Different

Many agent demos focus on full autonomy. This project focuses on continuity.

The product is useful precisely when the agent should not act alone: the case is risky, the cost is higher, the answer is customer-facing, or a human manager must approve. Instead of hiding that pause, the system makes it structured, auditable, and resumable.

## Microsoft Product Fit

The repo includes:

- Copilot Studio-ready agent instructions.
- Copilot Studio-style action contracts.
- An Adaptive Card approval payload.
- A live Microsoft Graph service-root contract check for Teams, chats, Planner, drives, and sites.

This keeps the submission honest while still proving the Microsoft integration path.

Important final-submit note:

The official GitHub issue form requires the submitter to confirm that the agent uses Copilot Studio, Microsoft 365 Copilot, or Copilot Cowork. This package is ready for review as a local handoff-agent prototype, but final contest submission should wait until one of those product paths is actually verified.

## Challenges

The hardest part was avoiding the false claim that a local prototype had already run inside a live Copilot Studio tenant.

The solution was to separate:

- what is verified locally,
- what is packaged for Copilot Studio,
- what Microsoft Graph contract is checked live,
- and what is not claimed yet.

## Accomplishments

- Built a working local handoff agent.
- Produced a required-field handoff packet.
- Confirmed handoff completeness at `1.0`.
- Blocked customer-facing send until approval.
- Added Microsoft Graph service-root verification.
- Added Copilot Studio-ready assets.
- Generated a natural-English demo video from current artifacts.

## What's Next

- Import the instructions/actions/card into a real Copilot Studio environment.
- Route manager approval to Teams.
- Save handoff packets into Dataverse or a Microsoft 365-backed record store.
- Create Planner tasks for resume instructions.

## Claim Boundary

Safe claim:

- Verified local handoff agent.
- Public demo and natural-English video.
- Copilot Studio-ready assets.
- Live Microsoft Graph public service-root contract check.

Not claimed:

- Live Copilot Studio execution.
- Confirmed use of Copilot Studio, Microsoft 365 Copilot, or Copilot Cowork inside a live Microsoft environment.
- Authenticated Microsoft tenant or customer data access.
- Final GitHub issue submission.
- Customer-facing send without approval.
