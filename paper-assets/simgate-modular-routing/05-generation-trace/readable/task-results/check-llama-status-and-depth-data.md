# check llama status and depth data

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_llama-status-and-depth-data_20260516T124201_result.json`
- **Structured JSON:** [`752fdcb687a29109550b.json`](../../sessions/75/752fdcb687a29109550b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full report.

---

## Part 1: Llama cross-model-v2 — COMPLETED

No tmux session, GPUs idle (2x RTX 5090, 0 MiB used). All 7 tasks finished, 10 episodes each (70 total).

| Task | det-pref | int-pref | no-pref | Internal Deaths | Det Deaths | Both Dead | Avg Gap |
|------|----------|----------|---------|-----------------|------------|-----------|---------|
| chemistry-mix | 2 | 0 | 8 | 2 | 0 | 4 | 100.0 |
| freeze | 3 | 0 | 7 | 3 | 0 | 3 | 125.7 |
| grow-fruit | 5 | 0 | 5 | 5 | 0 | 0 | 100.0 |
| identify-life-stages-1 | 2 | 0 | 8 | 2 | 0 | 4 | 112.5 |
| inclined-plane-determine-angle | 6 | 0 | 4 | 6 | 0 | 0 | 102.5 |
| lifespan-longest-lived | 4 | 0 | 6 | 4 | 0 | 2 | 112.5 |
| measure-melting-point-unknown-substance | 2 | 0 | 8 | 2 | 0 | 4 | 100.0 |
| **TOTAL** | **24** | **0** | **46** | **24** | **0** | **13** | — |

**Key findings:**
- **int-pref = 0 across ALL 7 tasks** — Llama's internal reasoning never beats deterministic
- det-pref: 24/70 (34.3%), no-pref: 46/70 (65.7%)
- Internal death rate: 24/70 (34.3%), det death rate: 0/70 (0%)
- Both-dead: 13/70 (18.6%)
- Deterministic never dies; internal dies frequently — Llama clearly struggles with internal reasoning on these tasks

---

## Part 2: Reasoning Depth Ablation (plan-006)

**Only `deep-internal` condition found on this server.** No `fast-internal` or `deterministic` directories exist anywhere under `simgate-modular-routing`.

### plan-006-deep-internal

Mode: `deep-internal-only`, seed=42, 6 tasks × 20 episodes = **120 episodes total**

| Task | Episodes |
|------|----------|
| chemistry-mix | 20 |
| find-non-living-thing | 20 |
| identify-life-stages-1 | 20 |
| inclined-plane-determine-angle | 20 |
| lifespan-longest-lived | 20 |
| lifespan-longest-lived-then-shortest-lived | 20 |

The other conditions (`fast-internal`, `deterministic`) are **not present** on this server — they either haven't been run yet or were collected elsewhere.

---
