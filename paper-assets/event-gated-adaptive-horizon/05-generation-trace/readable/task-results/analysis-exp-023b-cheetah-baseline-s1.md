# analysis exp 023b cheetah baseline s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_023b_cheetah_baseline_s1_20260517T192705_result.json`
- **Structured JSON:** [`4dfe2f1252ca76f6b9c1.json`](../../sessions/4d/4dfe2f1252ca76f6b9c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果摘要

**exp_023b_cheetah_baseline_s1** 正常完成，无异常。

| 指标 | 值 |
|------|-----|
| 最终 eval_return (205k) | 520.3 |
| 峰值 eval_return (195k) | 572.9 |
| 末5次 eval 均值 | **542.2** |
| 总步数 | 212,000 env steps |
| 训练时长 | ~5h 24m |
| 退出码 | 0 |

**收敛判断**: 曲线在 125k 步后进入 500-573 区间震荡，无 collapse/NaN/divergence。存在 eval noise（dips at 55k/85k/145k），属正常（10 episode eval）。

**NVE 基准**: seed=1 推荐用 last-5 eval mean = 542.2。待 exp_023a (seed=0) 完成后取双 seed 均值作为最终 Cheetah Run baseline。

**Checkpoint**: `~/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023b_cheetah_baseline_s1/latest.pt`

**注意**: 此实验未接入 W&B，数据仅在本地日志和 tensorboard events 中。

---
