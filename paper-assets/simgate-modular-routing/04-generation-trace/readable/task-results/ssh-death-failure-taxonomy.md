# ssh death failure taxonomy

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_death-failure-taxonomy_20260518T053046_result.json`
- **Structured JSON:** [`8b0408ff87c67c989640.json`](../../sessions/8b/8b0408ff87c67c989640.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No register_artifact tool available. The report is at `artifacts/death_failure_taxonomy.md` (373 lines).

---

## Summary of findings

**73 death episodes out of 241 total (30.3%)** across 7 ScienceWorld tasks. The analysis reveals a strikingly uniform failure mechanism:

### Universal death trigger
ALL 73 deaths (100%) are caused by `focus on [wrong object]`. In ScienceWorld, `focus on` is the answer-submission action. The LLM agent misuses it as a generic interaction command, targeting irrelevant objects (rooms, doors, inventory, wires). The deterministic agent survives 91.8% of these episodes simply by never issuing `focus on`.

### Failure mode taxonomy

| Category | Count | % |
|---|---|---|
| A. No task awareness (never reads task, pure connect-spam) | 16 | 21.9% |
| B. Task awareness without action capability (reads task, still connect-spam) | 51 | 69.9% |
| D. Genuine task attempt, execution failure (gained score before death) | 2 | 2.7% |
| E. Initial credit squandered (started with score, gained nothing) | 4 | 5.5% |

### Key insight for the paper
The death asymmetry is NOT because the internal agent faces more danger. It's because it systematically self-destructs through incorrect answer submission (`focus on`), while the deterministic agent, equally unable to solve the tasks (79.5% also score 0), avoids the death trigger. This is an **action-space grounding failure**: the agent can READ the task (78.1% do) but cannot GROUND it into correct ScienceWorld primitives. Only 2 of 73 death episodes show any genuine score progress before dying.

---
