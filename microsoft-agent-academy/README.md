# Human-AI Handoff Copilot

Target: Microsoft Agent Academy Hackathon

URL: https://microsoft.github.io/agent-academy/events/hackathon/

Status: registration route checked. Not a standard Devpost join flow. Final GitHub issue submission is blocked until build and DD approval.

Current local proof:

- Handoff architecture demo: `prototype/handoff-copilot-architecture.html`
- Demo screenshot: `media/handoff-copilot-architecture-full.png`
- GitHub issue draft: `reports/github-issue-draft.md`
- Builder: `scripts/build_handoff_copilot_architecture.py`

![Human-AI Handoff Copilot architecture](media/handoff-copilot-architecture-full.png)

## Position

P3 opportunistic lane.

Deadline is early, so this should only proceed if Microsoft platform access is already available or fast.

## Product Thesis

The strongest enterprise agents are not the ones that do everything alone.

They are the ones that know when to hand off to a human, what context to preserve, and how to resume safely.

Human-AI Handoff Copilot helps teams move work between AI agents and humans without losing context, approvals, or evidence.

## MVP

- Copilot-style workflow
- task card
- approval handoff
- evidence summary
- architecture diagram
- short demo

## Shared Engine Use

Reuse:

- handoff events
- approval gates
- evidence summary
- session timeline

Adapt:

- Microsoft Copilot Studio / M365 Copilot format if access is available

Current generated artifacts:

- Shared engine: `../shared-agentops-engine/`
- Canonical events: `../shared-agentops-engine/data/agentops_events.jsonl`
- Copilot architecture: `../shared-agentops-engine/adapters/microsoft/copilot_architecture.md`
- Google/Microsoft shared cloud-agent case: `CASE-CLOUD-003`

Build the Microsoft-focused local demo:

```bash
cd /Users/dd/000_AI組織/__hackason/microsoft-agent-academy
python3 scripts/build_handoff_copilot_architecture.py
```

Expected proof:

- builder returns `status: ok`
- `prototype/handoff-copilot-architecture.html` exists
- `reports/github-issue-draft.md` exists
- screenshot exists at `media/handoff-copilot-architecture-full.png`

Registration/submission routes observed:

- `Register Now` route: `https://aka.ms/agent-academy-live/register`
- Reactor event route: `https://developer.microsoft.com/en-us/reactor/events/27042/`
- `Submit Your Entry` route: `https://aka.ms/agent-academy-hack/submit`
- Final submission route redirects to GitHub issue creation: `https://github.com/microsoft/agent-academy/issues/new?template=hack-submission.yml`

Do not execute the final GitHub issue submission until DD approves the finished artifact.

## Immediate Next Steps

1. Confirm Microsoft product access.
2. If access is hard, keep this as a pitch/architecture lane only.
3. Build from the generated Copilot architecture doc if the lane remains active.

Current boundary:

- Safe claim: a Copilot-style handoff architecture and GitHub issue draft are generated locally.
- Do not execute the GitHub issue submission or claim live Copilot Studio implementation until DD approves and the platform is verified.
