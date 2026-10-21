# eval 28034 rl8000 and heldout monitor

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_28034-rl8000-and-heldout-monitor_20260523T082852_result.json`
- **Structured JSON:** [`7a25de0a7dbdc02759ae.json`](../../sessions/7a/7a25de0a7dbdc02759ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都完成了。

## 汇报

### 1. rl-ckpt-8000 (reduced-lora 16/16, 28034)
| 指标 | 值 |
|------|-----|
| ToF | 0.1602 |
| NoF | 0.8066 |
| **SYCONScore** | **0.2673** |
| Samples | 362 (valid=181, invalid=181) |

### 2. heldout 训练进度 (29046)
- 当前 step: 1000/8000（已过 checkpoint-1000）
- 训练持续中，~91s/10步

### 3. heldout ckpt-1000 eval (29046 本地运行)

由于两台服务器间无法直连 SCP，改为在 29046 本地用 GPU 0 运行 eval。

| 指标 | 值 |
|------|-----|
| ToF | 0.1143 |
| NoF | 0.9429 |
| **SYCONScore** | **0.2039** |
| Samples | 70 (valid=35, invalid=35) |

**注意**: heldout eval 使用的是 `eval_held_out.jsonl` (70 pairs)，与 rl-ckpt-8000 的 `calibration_v2_1_expanded.jsonl` (362 pairs) 数据集不同，不能直接对比。

---
