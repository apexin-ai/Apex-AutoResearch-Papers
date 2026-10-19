# eval 28034 fill gpu023

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_28034-fill-gpu023_20260523T035234_result.json`
- **Structured JSON:** [`08d156682f063c662ab9.json`](../../sessions/08/08d156682f063c662ab9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU0 和 GPU3 eval 正常运行中。

**当前 28034 GPU 状态：**
| GPU | Memory | 任务 |
|-----|--------|------|
| 0 | 16.8 GB | reduced-lora ckpt-5500 eval (PID 162944) |
| 1 | 21.8 GB | reduced-lora 训练（不碰） |
| 2 | 空闲 | — |
| 3 | 16.8 GB | gs8 ckpt-1500 eval (PID 163483) |

**GPU2 问题：ACT s2 ckpt-2500 不存在。**
- 29046 上 `exp-004-act-baseline-s2/` 只有 checkpoint-2000
- 训练 log 到 step 2500，但训练进程已不在运行（29046 两个 GPU 分别在跑 `gs8_r3only` 和 `len512_r3only`）
- ACT s2 ckpt-2000 的 eval 已在 28034 上完成过

GPU2 可以做什么？几个选项：
1. reduced-lora ckpt-2500 或 ckpt-3000（填 eval 曲线空缺，当前已有 500/1000/1500/2000/3500/4000/4500/5000）
2. 其他你想 eval 的 checkpoint
3. 空着等

你选哪个？

---
