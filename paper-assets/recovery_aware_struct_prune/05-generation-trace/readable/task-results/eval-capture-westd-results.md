# eval capture westd results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_capture-westd-results_20260515T150433_result.json`
- **Structured JSON:** [`ca6cdc4a1b452dbe3fc6.json`](../../sessions/ca/ca6cdc4a1b452dbe3fc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验都还在运行，无需更新 registry。状态汇总：

### 1. α=1.0 eval (PID 42535) — GPU 1
- **进度**: 33/100 samples (33%)
- **速度**: ~4-5s/sample（当前加速中，前几个 sample 因 warmup 较慢）
- **预计剩余**: ~5-6 分钟
- 结果文件尚未生成

### 2. α=2.0 SFT (PID 43065) — GPU 1
- **进度**: 237/1870 steps (12.7%), epoch 0.25
- **速度**: ~1.7s/step
- **Loss**: 1.901 → 0.87 (持续下降)
- **Token accuracy**: 0.653 → 0.78 (持续上升)
- **最新 log**: `loss=0.903, grad_norm=4.47, token_acc=0.777`
- **预计剩余**: ~46 分钟

### 3. GraSP eval (PID 38120) — GPU 0
- **进度**: 48/100 samples (48%)
- **速度**: ~52s/sample（比上次 105s/sample 快了）
- **预计剩余**: ~45 分钟

### 4. GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 13.1 / 97.9 GB | 90% |
| 1 | 80.6 / 97.9 GB | 97% |

α=1.0 eval 最快完成，约 5-6 分钟后可以再查一次捕获结果。

---
