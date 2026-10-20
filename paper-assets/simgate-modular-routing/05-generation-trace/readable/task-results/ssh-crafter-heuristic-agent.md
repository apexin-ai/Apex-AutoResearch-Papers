# ssh crafter heuristic agent

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_crafter-heuristic-agent_20260518T041020_result.json`
- **Structured JSON:** [`4ec323410342f968da1a.json`](../../sessions/4e/4ec323410342f968da1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Server westb-14838 has been unreachable for an extended period. Here's the current status:

**Progress:**
- v8 agent tested: 5/5 deaths, avg 353 steps (up from 215 in v7). Best episode reached 811 steps.
- v9 agent code is ready locally at `crafter_pilot/heuristic_agent.py` with three key fixes:
  1. Flee ALL monsters within 4 tiles (prevents zombie swarm formation that killed in eps 1-3)
  2. Sleep safety radius 12 with NO forced sleep at energy=0 (eliminates 7-damage sleep kills)
  3. Water-biased flee + wider food search (addresses starvation in ep 0)

**Critical Crafter mechanics discovered:**
- Sleep duration = (9-energy) * 11 steps. Energy=0 sleep = 99 steps = certain death if any zombie within ~50 tiles
- food=0 or drink=0 causes health decay (-1 hp every 15 steps)
- Health regen requires food>0 AND drink>0 AND (energy>0 OR sleeping)

**Pending when server returns:**
1. Deploy v9 to server
2. Run 5-episode test
3. Iterate if needed (may need to experiment with never-sleep strategy, water-barrier positioning, or plant farming)
4. Run random agent comparison (10 episodes)
5. Produce final report + sync artifact

---
