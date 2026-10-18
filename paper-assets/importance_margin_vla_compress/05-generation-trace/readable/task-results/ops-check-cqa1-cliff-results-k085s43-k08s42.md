# ops check cqa1 cliff results k085s43 k08s42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cqa1-cliff-results-k085s43-k08s42_20260520T221123_result.json`
- **Structured JSON:** [`f496283fad46779a44e5.json`](../../sessions/f4/f496283fad46779a44e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验 registry 已更新。

## 结果汇总

| 实验 | Keep Ratio | Tokens | Success Rate | Wilson CI 95% |
|------|-----------|--------|-------------|---------------|
| eval_xvla_prune_k08_seed42 | 0.80 | 40/50 | **88.8%** | [85.7%, 91.3%] |
| eval_xvla_prune_k085_seed43 | 0.85 | 42/50 | **67.6%** | [63.4%, 71.6%] |

**关键发现**：k=0.8 (88.8%) 远高于 k=0.85 (67.6%)，这与预期的单调递减趋势矛盾。k=0.85 seed43 的低分主要来自 task 6 (butter, 0%) 和 task 4 (ketchup, 28%)、task 8 (chocolate pudding, 34%)，而 k=0.8 seed42 这些任务分别为 56%、80%、88%。这更可能是 seed 差异而非 keep_ratio 效应。

## GPU 状态

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 0% | 1 MiB / 24GB | **空闲** |
| 1 | 56% | 4.5 GB / 24GB | 运行中: k08_seed44 |
| 2 | 1% | 4.5 GB / 24GB | 运行中: k085_seed44 |
| 3 | 0% | 1 MiB / 24GB | **空闲** |

## 当前运行进程
- `eval_xvla_k08_seed44` — GPU 1, keep_ratio=0.8, seed=44
- `eval_xvla_k085_seed44` — GPU 2, keep_ratio=0.85, seed=44

GPU 0 和 GPU 3 空闲可用。

---
