# eval gs8 ckpt500 status urgent

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_gs8-ckpt500-status-urgent_20260522T205146_result.json`
- **Structured JSON:** [`9ccd6502bac4dd56e07e.json`](../../sessions/9c/9ccd6502bac4dd56e07e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

- **gs8 ckpt-500 SCP 状态**: **DONE** — checkpoint 完整（adapter_model.safetensors 235M + 全部配套文件，03:54 完成）
- **gs8 ckpt-500 eval 状态**: **NOT_STARTED** — eval 结果文件不存在，无相关 eval 进程在运行
- **cuda:2 进程**: **空闲** — 2MiB 显存，0% 利用率，无计算进程

GPU 占用情况：
| GPU | 占用 | 进程 |
|-----|------|------|
| 0 | 16.7G/32.6G | PID 958710 — 未知训练（有 torch inductor compile workers） |
| 1 | 21.8G/32.6G | PID 30011 — exp-004-reduced-lora.py（00:40 启动，已运行 ~4h） |
| 2 | **空闲** | — |
| 3 | **空闲** | — |

cuda:2 和 cuda:3 均空闲，可以直接启动 gs8 ckpt-500 eval。需要我启动吗？

---
