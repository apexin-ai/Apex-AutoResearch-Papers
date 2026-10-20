# ssh crafter env setup pilot

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_crafter-env-setup-pilot_20260519T122024_result.json`
- **Structured JSON:** [`8fc26a5b0bee7579bd76.json`](../../sessions/8f/8fc26a5b0bee7579bd76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== CRAFTER PILOT RESULTS ===

Random baseline (5 eps):
  DR: 100%, Avg steps: 155.2, Avg reward: 0.90, Avg achievements: 1.8
  Per-episode: [(DIED,179), (DIED,198), (DIED,151), (DIED,55), (DIED,193)]

Deterministic (10 eps):
  DR: 100%, Avg steps: 170.9, Avg reward: 3.10, Avg achievements: 4.0
  Per-episode: [(DIED,223), (DIED,192), (DIED,108), (DIED,172), (DIED,149), (DIED,175), (DIED,169), (DIED,212), (DIED,44), (DIED,265)]

LLM/Internal (10 eps):
  DR: 100%, Avg steps: 180.3, Avg reward: -0.90, Avg achievements: 0.0
  Per-episode: [(DIED,163), (DIED,160), (DIED,191), (DIED,155), (DIED,190), (DIED,229), (DIED,189), (DIED,167), (DIED,194), (DIED,165)]

Decision:
  Int DR: 100%
  Det DR: 100%
  Δ DR: 0pp
  Verdict: NOT FEASIBLE (Δ DR = 0, both agents always die)

Infrastructure:
  Text obs method: BALROG-adapted standalone wrapper (semantic grid → text)
  LLM parse success rate: 100%
  vLLM latency: 58ms/call
  Death detection: health=0 confirmed YES (all deaths = hp=0)

Key observations:
  - Crafter 300-step episodes are universally lethal: random/det/LLM all 100% DR
  - Det agent outperforms random on achievements (4.0 vs 1.8) and reward (3.10 vs 0.90)
  - LLM agent WORSE than random (0 achievements, -0.90 reward): it only outputs movement actions, never uses "do" to interact with objects (collect wood, drink water, eat)
  - LLM survives slightly longer (180.3 steps) likely because it moves away from threats, but starves to death without ever gathering resources
  - Crafter's death rate is too high across all agent types at 300 steps to produce useful Δ DR signal
```

**Files deployed to** `/root/autodl-tmp/simgate-modular-routing/scripts/crafter/`:
- `crafter_text_wrapper.py`
- `crafter_det_agent.py`
- `crafter_runner.py`

**Results saved to** `/root/autodl-tmp/simgate-modular-routing/results/crafter_pilot_{random,det,llm}.jsonl`

---
