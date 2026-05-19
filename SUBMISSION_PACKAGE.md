# Submission Package — Human-AI Handoff Copilot

## Project Title

Human-AI Handoff Copilot

## Short Description

A Copilot-style workflow for handing work between humans and AI agents without losing context, evidence, approvals, or cost guardrails.

## Repository

https://github.com/daideguchi/human-ai-handoff-copilot

## Try It Out

Open these local demo files after cloning the repository:

- `microsoft-agent-academy/prototype/handoff-copilot-architecture.html`
- `shared-agentops-engine/web/index.html`

## Screenshots

- `microsoft-agent-academy/media/handoff-copilot-architecture-full.png`
- `shared-agentops-engine/media/shared-dashboard-full.png`

## Demo Video

Draft silent video:

- `microsoft-agent-academy/media/human-ai-handoff-copilot-demo-draft.mp4`

Regenerate:

```bash
cd microsoft-agent-academy
bash scripts/build_demo_video.sh
```

## Inspiration

The strongest agents are not the ones that pretend to finish everything alone.

They are the ones that know when to hand off, what context to preserve, and how humans can resume safely.

## What It Does

Human-AI Handoff Copilot shows a support-operations workflow where:

- an AI agent plans the task
- policy and evidence are retrieved
- cost guardrails are logged
- human approval is required before escalation
- the handoff preserves context and evidence
- another human or AI can resume from the record

## How We Built It

- Shared AgentOps event stream
- Copilot-style architecture document
- Local HTML architecture demo
- GitHub issue submission draft
- Evidence and approval timeline

## Built With

- Python
- HTML/CSS
- JSON / JSONL
- Microsoft Copilot-style architecture model
- GitHub issue submission draft

## What Is Working

```text
verify_ok
status: ok
event_count=7
```

## Verification Commands

```bash
cd shared-agentops-engine
python3 scripts/generate_portfolio_artifacts.py
python3 scripts/verify_artifacts.py
```

```bash
cd ../microsoft-agent-academy
python3 scripts/build_handoff_copilot_architecture.py
bash scripts/build_demo_video.sh
```

## Demo Script Summary

1. Show the handoff architecture.
2. Show the AI plan and retrieved evidence.
3. Show the cost guardrail and approval point.
4. Show the handoff summary.
5. Explain why resumability matters for human-AI work.

## What Makes It Different

This project treats handoff as a first-class agent capability.

The goal is not full autonomy. The goal is safe continuity between AI work and human judgment.

## Challenges

The main challenge was packaging a Microsoft Agent Academy idea without claiming a live Copilot Studio implementation before it is verified.

## Accomplishments

- Built a local handoff architecture demo
- Generated a GitHub issue draft
- Preserved evidence, cost, and approval events
- Published a clean public repository

## What We Learned

Human-AI collaboration is strongest when work can move between people and agents without losing the reasoning trail.

## What's Next

Map the workflow into Copilot Studio or the accepted Microsoft Agent Academy submission format after platform access and submission approval are confirmed.

## Claim Boundary

This is a local verified architecture prototype.

It does not claim live Copilot Studio execution or a final submitted GitHub issue yet.
