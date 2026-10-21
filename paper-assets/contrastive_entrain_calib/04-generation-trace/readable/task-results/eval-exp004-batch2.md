# eval exp004 batch2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp004-batch2_20260520T144350_result.json`
- **Structured JSON:** [`5223fd4fd80410258605.json`](../../sessions/52/5223fd4fd80410258605.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张 GPU 全部满载运行。

---

### 产出汇总

**1. GPU 当前状态（westd-28034）**

| GPU | 显存 | 任务 |
|-----|------|------|
| 0 | 16884 MiB, 49% | exp-003 ckpt-4000 eval（仍在运行） |
| 1 | 14944 MiB, 11% | **exp-004 ckpt-7000**（刚启动） |
| 2 | 17660 MiB, 42% | **exp-004 ckpt-3000**（运行中） |
| 3 | 17660 MiB, 43% | **exp-004 ckpt-5000**（运行中） |

**2. 已完成结果**

**exp-004 ckpt-1000**（刚完成）：
- ToF = 0.116, NoF = 0.8729, **SYCONScore = 0.2048**
- 362 samples, 耗时 1689s

**exp-003 ckpt-4000**：仍在运行，结果未就绪。

**3. Batch 2 已提交 eval**

| eval | GPU | tmux session | PID |
|------|-----|-------------|-----|
| ckpt-3000 | 2 | exp-004-eval-ckpt3000 | 595107 |
| ckpt-5000 | 3 | exp-004-eval-ckpt5000 | 595243 |
| ckpt-7000 | 1 | exp-004-eval-ckpt7000 | 596096 |

**4. 剩余待 eval checkpoint（7 个）**

优先级排序：1500, 2500, 3500, 4500, 5500, 6500, 7500

当 GPU 0 上的 exp-003 ckpt-4000 完成后，以及当前 batch 的 3 个 eval 陆续完成时，可以继续提交这些。

---
