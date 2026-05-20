# Microsoft Agent Academy Submit Manual

Use this only after DD approves final submission.

## Final Links

- Project title: Human-AI Handoff Copilot
- Repository: https://github.com/daideguchi/human-ai-handoff-copilot
- Live demo: https://daideguchi.github.io/human-ai-handoff-copilot/
- YouTube demo: https://www.youtube.com/watch?v=asbgvArrqXU
- Demo video file in repo: `microsoft-agent-academy/media/human-ai-handoff-copilot-demo.mp4`
- Main README: https://github.com/daideguchi/human-ai-handoff-copilot#readme

## Copy Summary

Human-AI Handoff Copilot is a Copilot-style handoff agent that preserves evidence, approvals, cost guardrails, blocked actions, and resume instructions when work moves from AI to a human manager or another AI.

The local agent runs a support escalation case, retrieves evidence, creates a draft response, blocks the risky customer-facing send, generates a required-field handoff packet, and proves that the next actor can safely resume.

## What To Emphasize

- This is not another full-autonomy demo.
- The product solves the moment where AI must pause and hand work to a human.
- The handoff packet is machine-readable and auditable.
- The repo includes Copilot Studio-ready instructions, actions, and an Adaptive Card.
- Microsoft Graph public service-root contract is checked live.
- Risky customer-facing action remains blocked until approval.

## Verification Proof To Paste

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

## Claim Boundary

Safe:

- verified local handoff agent
- Copilot Studio-ready assets
- live Microsoft Graph public service-root contract check
- public GitHub Pages demo
- natural-English demo video

Do not claim:

- live Copilot Studio execution
- authenticated Microsoft tenant data access
- final issue submission before this manual is completed
- customer-facing send without approval

## Final Submission Route

Observed submit route:

```text
https://aka.ms/agent-academy-hack/submit
```

Observed GitHub issue template route:

```text
https://github.com/microsoft/agent-academy/issues/new?template=hack-submission.yml
```

Before clicking submit, rerun:

```bash
bash microsoft-agent-academy/scripts/run_microsoft_local_checks.sh
```
