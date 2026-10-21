# diagnose fmvd phase1 results urgent

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_fmvd-phase1-results-urgent_20260519T194723_result.json`
- **Structured JSON:** [`aa14dd8adb8ed193bfec.json`](../../sessions/aa/aa14dd8adb8ed193bfec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## FMVD Phase 1 结果

### Overall Statistics

| 指标 | 值 |
|------|-----|
| **spearman_rho** | **0.0825** |
| **spearman_p** | **2.33e-23** |
| fmvd_mean | 0.0549 |
| fmvd_std | 0.0403 |
| fmvd P25/P50/P75/P90 | 0.028 / 0.047 / 0.071 / 0.094 |
| k10_variance_mean | 0.0049 |
| n_steps | 14,512 (10 tasks × 5 episodes) |

### Per-Task Breakdown

| Task | Steps | Success | FMVD mean | ρ | p |
|------|-------|---------|-----------|------|------|
| alphabet_soup | 1500 | 0/5 | 0.0588 | **0.1044** | 5.1e-5 |
| bbq_sauce | 1500 | 0/5 | 0.0455 | 0.0264 | 0.307 |
| butter | 1500 | 0/5 | 0.0796 | **0.0846** | 1.0e-3 |
| chocolate_pudding | 1355 | 1/5 | 0.0672 | -0.0518 | 0.057 |
| cream_cheese | 1500 | 0/5 | 0.0464 | **0.1274** | 7.4e-7 |
| ketchup | 1500 | 0/5 | 0.0609 | -0.0362 | 0.162 |
| milk | 1500 | 0/5 | 0.0587 | **-0.2840** | 3.1e-29 |
| orange_juice | 1500 | 0/5 | 0.0414 | **0.2465** | 3.3e-22 |
| salad_dressing | 1337 | 1/5 | 0.0459 | **0.1489** | 4.5e-8 |
| tomato_sauce | 1320 | 1/5 | 0.0430 | 0.0474 | 0.085 |

### Go/No-Go 判断

**NO-GO.** Overall ρ = 0.0825，远低于 0.3 阈值。

关键问题：
- **相关性极弱**：FMVD 与 k10_variance 之间几乎没有单调关系。整体 ρ 虽然统计显著（p ≈ 0），但这只是因为 n=14512 样本量大，实际效应量可忽略。
- **方向不一致**：milk 任务 ρ = -0.284（显著负相关），与假设方向相反。
- **最佳单任务也不够**：orange_juice 的 ρ = 0.247 是最高的，仍未过 0.3。
- **成功率极低**：10 个任务中只有 3 个有 1/5 成功，整体 3/50 = 6%。

---
