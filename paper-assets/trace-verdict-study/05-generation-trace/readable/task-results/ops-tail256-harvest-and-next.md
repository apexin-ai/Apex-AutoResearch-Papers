# ops tail256 harvest and next

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_tail256_harvest_and_next_20260517T200614_result.json`
- **Structured JSON:** [`ebb8611f94d1b23d9e6d.json`](../../sessions/eb/ebb8611f94d1b23d9e6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Tail-256 — **已完成** (训练 + eval 均已完成)

| 指标 | Tail-256 | Tail-512 | Tail-2048 |
|------|----------|----------|-----------|
| **Accuracy** | **78.9%** [76.5%, 81.3%] | 93.61% | 97.31% |
| **Pass F1** | 0.845 | — | — |
| **Fail F1** | 0.671 | — | — |
| **Lift over majority** | +7.4pp | — | — |

GPU 1 已空闲（0 MiB，0% util）。

趋势清晰：truncation 长度与性能强相关，256 token 严重不足，accuracy 从 97.3% → 93.6% → 78.9%。

### 2. DeepSeek head-2048 — **进行中** (95%)

- 当前进度：**421/444 steps**，预计 ~6 分钟后完成
- GPU 0：100% util, 73°C, 524W, 71.6 GiB VRAM
- PID 371047，无 tmux session（nohup 后台运行）
- 训练完成后还需手动跑 eval

---
