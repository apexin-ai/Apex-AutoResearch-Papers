# infra diagnose westd 10894 gpu state

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_diagnose-westd-10894-gpu-state_20260521T061819_result.json`
- **Structured JSON:** [`5c517572e2c5784ff972.json`](../../sessions/5c/5c517572e2c5784ff972.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部恢复。汇总：

## GPU 诊断报告 — westd-10894

| GPU | 诊断前状态 | 诊断后状态 |
|-----|-----------|-----------|
| 0 | **stuck** (100% util, 0 MiB, 无进程) | **idle** (0%, P8, 35W) |
| 1 | **stuck** (100% util, 0 MiB, 无进程) | **idle** (0%, P8, 36W) |
| 2 | **stuck** (100% util, 0 MiB, 无进程) | **idle** (0%, P8, 37W) |
| 3 | idle (0%, P8, 34W) | **idle** (0%, P8, 33W) |

- **残留进程**: 无（仅系统服务 + tmux 空 session）
- **`nvidia-smi --gpu-reset`**: 被 AutoDL 容器禁用（"not supported"）
- **CUDA 软 reset**: 成功 — 通过 `torch.cuda.empty_cache()` + 小张量分配/释放，3 张 stuck GPU 全部恢复正常
- **无需重启实例**，4× GPU 全部可用

---
