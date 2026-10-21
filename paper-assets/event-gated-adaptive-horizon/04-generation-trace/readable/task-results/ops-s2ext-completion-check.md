# ops s2ext completion check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s2ext-completion-check_20260519T150203_result.json`
- **Structured JSON:** [`a36ef2cc9c91f880188c.json`](../../sessions/a3/a36ef2cc9c91f880188c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

## s2_ext 状态：仍在跑，当前 444K / 505K（~88%）

| 指标 | 值 |
|------|-----|
| 最新 eval (442K) | 928.5 |
| peak eval | **960.8** @ 302K |
| latest checkpoint | `latest.pt` (更新于 22:55) |

### 尾部 ve_ratio（420K+）

| step | eval_return | value_mean | ve_ratio |
|------|------------|------------|----------|
| 422K | 933.3 | 664.3 | 0.7118 |
| 432K | 949.1 | 666.2 | 0.7019 |
| 442K | 928.5 | 666.5 | 0.7178 |

ve_ratio 稳定在 ~0.71，value_mean 平台在 ~666，eval_return 在 928-949 之间波动，无上升趋势。Peak 出现在 302K，之后 eval 一直在 880-960 区间震荡。

## s3_ext / s4_ext 进度

- **s3_ext**: 332K 步，train_return 935-987
- **s4_ext**: 288K 步，train_return 939-975

---
