# GitHub Issue Draft — Human-AI Handoff Copilot

Do not submit this issue until DD explicitly approves.

## Project

Human-AI Handoff Copilot

## Summary

A Copilot-style workflow for moving support operations between AI agents and humans without losing evidence, cost guardrails, approval decisions, or handoff context.

## Current Artifacts

- `prototype/handoff-copilot-architecture.html`
- `media/handoff-copilot-architecture-full.png`
- `../shared-agentops-engine/adapters/microsoft/copilot_architecture.md`

## Evidence Events

- `evt-0020` Support manager requested an agent that answers customer questions and escalates uncertain cases.
- `evt-0021` Agent created a workflow plan using retrieval, MCP tools, cost guardrails, and human escalation.
- `evt-0022` MCP retrieval returned the current refund policy and source URL for citation.
- `evt-0023` Agent drafted a customer answer grounded in the retrieved refund policy.
- `evt-0024` Cost guardrail warned that the high-quality model should be reserved for escalations.
- `evt-0025` Human approved the workflow with a rule that expensive model calls are escalation-only.
- `evt-0026` Closed cloud-agent workflow case with source citations, cost guardrail, and human approval captured.

## Boundary

This is an architecture/local prototype package. Do not claim a live Copilot Studio or GitHub-submitted entry until verified.
