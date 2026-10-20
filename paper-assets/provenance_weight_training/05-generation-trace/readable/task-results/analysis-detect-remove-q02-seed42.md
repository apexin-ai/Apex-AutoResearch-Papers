# analysis detect remove q02 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_detect_remove_q02_seed42_20260518T232524_result.json`
- **Structured JSON:** [`42d878442a32814eecc5.json`](../../sessions/42/42d878442a32814eecc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。总结：

**detect_remove_q02_seed42 结果**
| 指标 | 值 |
|---|---|
| eval_ppl_holdout | **17.27** |
| eval_loss_holdout | 2.8491 |
| train_loss | 11.348 |
| train_steps | 6103 |
| data_count | 91,654 samples |
| checkpoint | `/root/autodl-tmp/output/models/detect_remove_q02_seed42/final` |

**U-curve 完整数据点：**
| threshold | data retained | eval_ppl |
|---|---|---|
| q01 | ~9% | 17.40 |
| **q02** | **~23%** | **17.27** |
| q03 | ~36% | 17.25 |
| q04 | ~49% | 17.26 |
| q05 | ~61% | 17.28 |
| q06 | ~72% | 17.30 |
| q07 | ~81% | 17.32 |
| q09 | ~95% | 17.42 |

**结论**：q02=17.27 非常接近 q03=17.25（仅差 0.02），远低于 q01=17.40（差 0.13）。左侧陡升仅在极端过滤（q01, 仅保留 9% 数据）时发生，q02-q04 区间基本平坦。U-curve 最低点在 q03-q04 附近，曲线整体呈不对称形状：左侧 q01→q02 有一个陡降，然后 q02-q04 几乎平坦，右侧从 q05 开始缓慢上升。

---
