# verify cka only step50 log vs wandb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_cka_only_step50_log_vs_wandb_20260518T024508_result.json`
- **Structured JSON:** [`8b76312ad423fed24a05.json`](../../sessions/8b/8b76312ad423fed24a05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。以下是完整分析结果。

---

## 核实结论

### 完整训练日志 reward 数据（每 10 步记录一次）

| Optimizer Step | Log `reward` | W&B `train/reward` | W&B `_step` |
|:-:|:-:|:-:|:-:|
| 10 | 0.2531 | 0.253125 | 280 |
| 20 | 0.2181 | 0.218125 | 562 |
| 30 | 0.25 | 0.25 | 844 |
| 40 | 0.2344 | 0.234375 | 1126 |
| **50** | **0.3544** | **0.354375** | **1408** |
| 60 | 0.2994 | 0.299375 | 1690 |
| 70 | 0.3075 | 0.3075 | 1972 |
| 80 | 0.3419 | 0.341875 | 2254 |
| 90 | 0.2419 | 0.241875 | 2536 |
| 100 | 0.3444 | 0.344375 | 2818 |

### 核心结论

```
Log step 50 reward:       0.3544 (from 'reward' key in log dict)
W&B step 50 reward:       0.354375 (from 'train/reward' key, W&B _step=1408)
W&B sub-step data near 50: 无。仅 10 个数据点，每 10 optimizer step 记录一次，无 sub-step 粒度。

Root cause of discrepancy: 不存在差异。W&B 和 log 在 step 50 完全一致（0.3544）。
  - Reviewer 报告的 0.264 在整个训练日志中不存在，任何 step 都没有这个值。
  - W&B `_step`（280, 562, ...2818）是内部计数器（≈ num_tokens / batch 相关），不是 optimizer step。
    W&B 图表 x 轴如果显示 _step，"step 50" 对应的是训练最初期（< optimizer step 10），
    此时可能尚无 reward 数据点。Reviewer 可能在 W&B UI 上误读了 x 轴。

Recommendation for paper: 使用 0.3544（log 和 W&B 一致）。
```

**W&B metric key 说明**: 训练框架 (TRL) 以 `train/reward` 为 key 写入 W&B，而 log 打印时用 `reward`。两者数值完全相同。Reviewer 报告的 0.264 可能来自对不同 run 或不同 step 的误读。

---
