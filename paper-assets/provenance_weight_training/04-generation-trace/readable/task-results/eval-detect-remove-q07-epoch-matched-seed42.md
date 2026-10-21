# eval detect remove q07 epoch matched seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_detect_remove_q07_epoch_matched_seed42_20260519T030324_result.json`
- **Structured JSON:** [`18b7498606040f5900a6.json`](../../sessions/18/18b7498606040f5900a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

**Eval 结果汇总：**

| Threshold | Samples | Steps | PPL |
|-----------|---------|-------|-----|
| q01 | 55,799 | 919 | 18.04 |
| q03 | 116,935 | 1,927 | 17.74 |
| q05 | 152,246 | 2,533 | 17.65 |
| **q07** | **184,908** | **3,047** | **17.62** |
| q09 | - | - | 训练中 |

q07 epoch-matched PPL = 17.62，与 q05 (17.65) 基本持平，继续缓慢下降。epoch-matched 曲线呈单调递减趋势（更多数据 = 更低 PPL），进一步支持 U-shape 是多 epoch 过拟合的假设。

---
