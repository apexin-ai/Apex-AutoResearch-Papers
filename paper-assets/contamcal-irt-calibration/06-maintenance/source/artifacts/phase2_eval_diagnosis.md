# Phase 2 Eval Status Report

**Server:** westd-29999  
**Checked at:** 2026-05-19 ~19:31 CST (11:31 UTC)  
**Started:** 2026-05-19 18:42 CST  

## TL;DR

**Processes are STILL RUNNING.** No crash. 11/25 complete, 4 in progress, 10 pending. All 4 GPUs active at 89-99% utilization.

---

## GPU Status

| GPU | Assignment | Completed | In Progress | Pending | GPU Util |
|-----|-----------|-----------|-------------|---------|----------|
| 0 | Phi-4 (5) | 2 | 1 (phi4_d025 - ARC phase) | 2 | 99% |
| 1 | Qwen2.5-14B (5) | 2 | 1 (qwen14b_d025) | 2 | 94% |
| 2 | Qwen2.5-7B (5) + Gemma2 d000 (1) | 5 | 1 (gemma2_d000 - just started) | 0 | 89% |
| 3 | Gemma2 d005-d100 (4) + OLMo2 (5) | 2 | 1 (gemma2_d050) | 6 | 94% |

---

## Completed Results (11/25)

| Model | Dosage | MMLU Acc | ARC Acc | Completed At |
|-------|--------|----------|---------|-------------|
| Qwen2.5-7B | d000 | 0.6611 | 0.8788 | 18:52 |
| Qwen2.5-7B | d005 | 0.6474 | 0.8609 | 19:01 |
| Qwen2.5-7B | d025 | 0.6298 | 0.8404 | 19:10 |
| Qwen2.5-7B | d050 | 0.6307 | 0.8456 | 19:20 |
| Qwen2.5-7B | d100 | 0.6433 | 0.8498 | 19:29 |
| Qwen2.5-14B | d000 | 0.6944 | 0.9104 | 19:01 |
| Qwen2.5-14B | d005 | 0.6901 | 0.9036 | 19:19 |
| Phi-4 | d000 | 0.7644 | 0.9206 | 18:58 |
| Phi-4 | d005 | 0.7636 | 0.9181 | 19:15 |
| Gemma-2-9B | d005 | 0.6342 | 0.7782 | 19:01 |
| Gemma-2-9B | d025 | 0.6456 | 0.8737 | 19:19 |

### Phi-4 d025 (MMLU only so far)
- MMLU: 0.7698 (completed 19:28, ARC in progress)

---

## In Progress (4)

| PID | GPU | Model | Started | Status |
|-----|-----|-------|---------|--------|
| 154162 | 0 | phi4_d025 | 19:15 | MMLU done (0.7698), ARC running |
| 154838 | 1 | qwen14b_d025 | 19:19 | Running |
| 157509 | 2 | gemma2_d000 | 19:29 | Just started loading |
| 154997 | 3 | gemma2_d050 | 19:19 | Running |

---

## Pending (10)

| GPU | Models |
|-----|--------|
| 0 | phi4_d050, phi4_d100 |
| 1 | qwen14b_d050, qwen14b_d100 |
| 2 | (none - will finish after gemma2_d000) |
| 3 | gemma2_d100, olmo2_d000, olmo2_d005, olmo2_d025, olmo2_d050, olmo2_d100 |

---

## Estimated Completion

- Per model: ~9-10 min (7B), ~15-20 min (9B/14B), ~17 min (Phi-4)
- GPU 0: 2 remaining = ~34 min -> ~20:05
- GPU 1: 2 remaining = ~40 min -> ~20:10
- GPU 2: 1 remaining (gemma2_d000) = ~20 min -> ~19:50
- GPU 3: 6 remaining = ~120 min -> ~21:30 (bottleneck)

**Overall ETA: ~21:30 CST (13:30 UTC)**

GPU 3 is the bottleneck with 9 total evals (most loaded).

---

## Observations

1. All completed results include `.done` sentinel, `eval_results.json`, `correctness_matrix.json`, `item_responses.json`, `mmlu_results.json`, `arc_challenge_results.json`
2. Qwen2.5-7B shows expected contamination pattern: MMLU drops with dosage (0.661 -> 0.630), slight recovery at d100 (0.643)
3. ARC pattern for Qwen2.5-7B similar: 0.879 -> 0.840 -> 0.846 -> 0.850
4. Gemma-2-9B d005 ARC (0.778) much lower than d025 ARC (0.874) - notable jump worth investigating
5. Phi-4 shows minimal MMLU change across dosages (0.764 -> 0.764 -> 0.770)
