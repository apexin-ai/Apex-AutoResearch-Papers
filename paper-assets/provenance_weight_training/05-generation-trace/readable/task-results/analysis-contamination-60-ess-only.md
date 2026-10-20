# analysis contamination 60 ess only

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_contamination_60_ess_only_20260516T032558_result.json`
- **Structured JSON:** [`61ff084cd203180da41f.json`](../../sessions/61/61ff084cd203180da41f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`contamination_60_ess_only_seed42` 已更新为 DONE(success)。

**结果汇总：**

| 指标 | 值 |
|------|-----|
| eval_ppl_holdout | **17.77** |
| eval_loss_holdout | 2.8775 |
| train_loss | 9.842 |
| total_steps | 6103 |
| train_runtime | 13152s (~3.65h) |

**对比：**
| 实验 | PPL |
|------|-----|
| uniform (baseline) | 17.694 |
| ρ=0.4 ess_only seed42 | 17.73 |
| **ρ=0.6 ess_only seed42** | **17.77** |

符合预期：ρ 越高（污染越严重），ESS-only 的 PPL 越差。ρ=0.6 时 PPL 比 uniform 高 0.076，比 ρ=0.4 高 0.04。

---
