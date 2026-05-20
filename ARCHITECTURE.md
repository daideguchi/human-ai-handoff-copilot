# Architecture — Human-AI Handoff Copilot

## One Sentence

Human-AI Handoff Copilot is a Copilot Studio-ready handoff agent pattern that
preserves context, evidence, approvals, cost, and resume instructions when work
moves from an AI agent to a human manager.

## Data Flow

```text
Support escalation case
  policy source
  agent worklog
  Copilot Studio instructions
        |
        v
Local handoff agent
        |
        +--> build handoff packet
        +--> validate required fields
        +--> block customer-facing send
        +--> check Microsoft Graph public service root
        +--> produce manager approval card
        |
        v
Outputs
  terminal transcript
  handoff packet
  resume proof
  quality report
  Microsoft Graph contract report
  GitHub issue draft
  demo page
```

## Copilot Studio Mapping

- `copilot_studio/agent-instructions.md` - agent behavior and boundaries.
- `copilot_studio/actions.json` - action contracts for creating handoff packets,
  requesting approval, and sending only after approval.
- `copilot_studio/adaptive-card-handoff.json` - manager approval card shape.

## Microsoft Graph Mapping

`scripts/check_microsoft_graph_contract.py` reads the public Microsoft Graph
v1.0 service root and verifies that the required entity sets exist for the
intended implementation path:

- Teams / chats for manager approval and status updates.
- Planner for resume tasks.
- Drives / sites for policy and handoff packet storage.

The check does not read authenticated tenant or user data.

## Human-AI Boundary

The agent can retrieve evidence, draft a reply, and package the handoff. It
cannot send a customer-facing financial message until a human manager approves
the handoff card.

## Submission Boundary

This repository claims a verified local handoff agent and Copilot Studio-ready
assets plus a live Microsoft Graph public service-root contract check. It does
not claim live Copilot Studio execution or final GitHub issue submission until
those paths are separately verified.
