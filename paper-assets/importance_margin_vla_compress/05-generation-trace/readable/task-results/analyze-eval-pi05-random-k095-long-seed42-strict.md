# analyze eval pi05 random k095 long seed42 strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k095_long_seed42_strict_20260527T102022_result.json`
- **Structured JSON:** [`ac1bcb1a64c6e21829ec.json`](../../sessions/ac/ac1bcb1a64c6e21829ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。完整 metrics 汇总：

## π0.5 Random k=0.95 Long (strict) — 结果

**Overall SR: 60.6%** (303/500)，与 D257 记录一致。Strict vs Lenient Δ=-2.6pp（60.6% vs 63.2%），偏差在合理范围内，conclusion=success。

### Per-task breakdown

| Task | Description | SR |
|------|------------|-----|
| T0 | put both the alphabet soup and the tomato... | 70% |
| T1 | put both the cream cheese box and the butter... | **94%** |
| T2 | turn on the stove and put the moka pot on... | 70% |
| T3 | put the black bowl in the bottom drawer | 80% |
| T4 | put the white mug on the left plate and... | 52% |
| T5 | pick up the book and place it in the back... | **86%** |
| T6 | put the white mug on the plate and put the... | **0%** |
| T7 | put both the alphabet soup and the cream... | 58% |
| T8 | put both moka pots on the stove | 12% |
| T9 | put the yellow and white mug in the microwave | **84%** |

- 运行时间: 161.2 min (~2.7h)，GPU hours: 2.83h
- EXIT_CODE=0，无异常/warning（仅 robosuite 常规提示）
- T6 完全失败（0%）和 T8 极低（12%）是主要拖累项

---
