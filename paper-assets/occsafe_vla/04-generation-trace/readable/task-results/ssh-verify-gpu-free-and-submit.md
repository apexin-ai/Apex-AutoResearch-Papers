# ssh verify gpu free and submit

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-gpu-free-and-submit_20260528T230733_result.json`
- **Structured JSON:** [`9b0982d1d5f608bc9790.json`](../../sessions/9b/9b0982d1d5f608bc9790.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

tmux 被 read_only 拦截，但其余信息足够判断。

## 状态报告

### westd-34685
| 检查项 | 结果 |
|--------|------|
| GPU 进程 | **无** (nvidia-smi 返回空) |
| 旧进程 19300, 28639 | **已死** (ps 未找到) |
| tmux sessions | 无法通过 read_only 检查 (被拦截) |
| GPU 内存 | GPU 0: **0 MiB / 97887 MiB** (完全空闲) |

### westd-10894
| 检查项 | 结果 |
|--------|------|
| GPU 进程 | **无** (nvidia-smi 返回空) |
| 旧进程 33388, 47954 | **已死** (ps 未找到) |
| tmux sessions | 无法通过 read_only 检查 (被拦截) |
| GPU 内存 | GPU 0: **0 MiB / 97887 MiB** (完全空闲) |

**结论：两台服务器 GPU 完全空闲，所有旧进程均已终止。** 每台各显示 1 块 GPU (~96GB)，0 MiB 占用。tmux 检查因 read_only 限制无法执行，但 GPU 无进程 + 旧 PID 已死，可确认无残留占用。

---
