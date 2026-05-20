# GitHub Issue Draft — Human-AI Handoff Copilot

Do not submit this issue until DD explicitly approves.

## Project

Human-AI Handoff Copilot

## Summary

A Copilot-style workflow for moving support operations between AI agents and humans without losing evidence, cost guardrails, approval decisions, or handoff context.

## Current Artifacts

- Live demo: `https://daideguchi.github.io/human-ai-handoff-copilot/`
- YouTube demo: `https://www.youtube.com/watch?v=asbgvArrqXU`
- Repository: `https://github.com/daideguchi/human-ai-handoff-copilot`
- `prototype/handoff-copilot-architecture.html`
- `prototype/terminal-session.html`
- `reports/handoff-packet.json`
- `reports/resume-proof.json`
- `reports/handoff-quality-report.md`
- `reports/microsoft-graph-contract.json`
- `media/handoff-copilot-architecture-full.png`
- `media/handoff-terminal-session-full.png`
- `media/human-ai-handoff-copilot-demo.mp4`
- `copilot_studio/agent-instructions.md`
- `copilot_studio/actions.json`
- `copilot_studio/adaptive-card-handoff.json`
- `../shared-agentops-engine/adapters/microsoft/copilot_architecture.md`

## Verification

```bash
bash microsoft-agent-academy/scripts/run_microsoft_local_checks.sh
```

Expected proof:

```text
microsoft_local_checks_ok
handoff_completeness=1.0
resumable_by_next_actor=True
microsoft_graph_contract=ok
claim_boundary=verified_local_handoff_agent_no_live_copilot_studio_execution_claim
```

## Evidence Events

- `evt-0020` Support manager requested an agent that answers customer questions and escalates uncertain cases.
- `evt-0021` Agent created a workflow plan using retrieval, MCP tools, cost guardrails, and human escalation.
- `evt-0022` MCP retrieval returned the current refund policy and source URL for citation.
- `evt-0023` Agent drafted a customer answer grounded in the retrieved refund policy.
- `evt-0024` Cost guardrail warned that the high-quality model should be reserved for escalations.
- `evt-0025` Human approved the workflow with a rule that expensive model calls are escalation-only.
- `evt-0026` Closed cloud-agent workflow case with source citations, cost guardrail, and human approval captured.

## Boundary

This is a verified local handoff-agent package with Copilot Studio-ready assets and a live Microsoft Graph service-root contract check. The official final issue template requires confirming use of Copilot Studio, Microsoft 365 Copilot, or Copilot Cowork, so do not submit or claim eligibility until one of those product paths is actually verified.
