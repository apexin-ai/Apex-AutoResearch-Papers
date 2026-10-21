# submit 1 7b dual card

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_1_7b-dual-card_20260516T194234_result.json`
- **Structured JSON:** [`e6b6f3220ffc79619d55.json`](../../sessions/e6/e6b6f3220ffc79619d55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功启动并开始训练。

**汇报：**

| 实验 | tmux session | PID | GPU | 显存占用 |
|------|-------------|-----|-----|---------|
| w2-qwen3-1.7b-random-b01 | random_1_7b | 921646 | GPU-0 (bee2603b) | 39588 MiB |
| w2-qwen3-1.7b-isr-b03 | isr_1_7b | 921785 | GPU-1 (ea63b76b) | 39588 MiB |

**初始 log 确认：**
- random: step 1 reward=0.5196, prove_rate=0.500, ~8.56s/it → 预计 ~71 min 完成
- isr: step 1 reward=0.6200, prove_rate=0.500, ~8.58s/it → 预计 ~71 min 完成

两个实验各自独占一张 GPU，无交叉占用。

---
