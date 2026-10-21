# analysis lofo ablation

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lofo-ablation_20260515T075519_result.json`
- **Structured JSON:** [`8b64186758d9699d56eb.json`](../../sessions/8b/8b64186758d9699d56eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both tasks complete. Results saved to server.

---

## Task 1: LOFO Ablation Results

Full baseline (sanity check): **0.7904**

| Dropped feature | LOGO F1 | Δ vs Full (0.789) |
|---|---|---|
| hapax_ratio | 0.7848 | -0.0042 |
| ttr | 0.7835 | -0.0055 |
| entropy_mean | 0.7827 | -0.0063 |
| entropy_std | 0.7861 | -0.0029 |
| entropy_min | 0.7891 | +0.0001 |
| **entropy_max** | **0.7740** | **-0.0150** |
| tail_decay | 0.7857 | -0.0033 |

**Key findings:**
- **entropy_max** is the most important feature (Δ = -0.015, biggest drop)
- **entropy_min** is essentially redundant (Δ ≈ 0, removing it doesn't hurt)
- Importance ranking: entropy_max > entropy_mean > ttr > hapax_ratio > tail_decay > entropy_std > entropy_min

Results saved to `/root/gen-depth-fingerprint/results/lofo_ablation_results.json`

---

## Task 2: Multi-seed Stability Results

| Seed | LOGO F1 |
|---|---|
| 42 | 0.7904 |
| 123 | 0.7892 |
| 456 | 0.7876 |
| 789 | 0.7890 |
| 1024 | 0.7887 |

**Mean: 0.7890 ± 0.0009** (range: 0.7876–0.7904)

Extremely stable — std of 0.0009 confirms results are seed-independent.

Results saved to `/root/gen-depth-fingerprint/results/multi_seed_stability.json`

---
