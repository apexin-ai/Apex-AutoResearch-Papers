# code oom verify urgent

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_oom-verify-urgent_20260515T124708_result.json`
- **Structured JSON:** [`81aa2607da80fcc6f6dc.json`](../../sessions/81/81aa2607da80fcc6f6dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终状态

PID 518416 已不存在（之前 kill 操作已清理或自行退出）。

**当前 GPU 进程（全部为 v6，状态正常）：**

| GPU | PID | 进程 | VRAM |
|-----|-----|------|------|
| 0 | 519843 | RASP v6 (`grpo_stage2_rasp_20_v6`) 主进程 | 12,488 MiB |
| 0 | 520997 | RASP v6 (`grpo_stage2_rasp_20_v6`) worker (`--seed 42`) | 12,488 MiB |
| 1 | 519929 | Standard v6 (`grpo_stage2_standard_20_v6`) 主进程 | 12,488 MiB |
| 1 | 521089 | Standard v6 (`grpo_stage2_standard_20_v6`) worker (`--seed 42`) | 12,488 MiB |

**VRAM：** GPU 0 = 25GB/98GB, GPU 1 = 25GB/98GB — 从之前的 94GB OOM 边缘恢复正常。

注意：实际 PID 与预期略有偏差（预期 520992/521084，实际 519843+520997 / 519929+521089），但每个实验都是主进程+worker 两个 python 进程的正常模式。无异常进程，无需额外清理。

---
