# ssh qwen startup verify

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_qwen-startup-verify_20260520T014856_result.json`
- **Structured JSON:** [`af8b87b09dc226e6b327.json`](../../sessions/af/af8b87b09dc226e6b327.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练都成功启动，正在正常跑。

## GPU 状态总览

| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0 | 99% | 21.2/31.8 GB | **s123 训练正常** (PID 886278) |
| 1 | 100% | 0/31.8 GB | **hung** — 跟之前一样，100% util 但 0 VRAM |
| 2 | 87% | 16.3/31.8 GB | 已有进程 (PID 885624, 运行 22min) |
| 3 | 91% | 31.3/31.8 GB | **s456 训练正常** (PID 886352) |

## 训练进度

- **s123** (GPU 0): step 66/6633, ~12s/it, 开始于 09:36:11, ETA ~22h
- **s456** (GPU 3): step 67/6633, ~11.6s/it, 开始于 09:36:22, ETA ~21h

两个 wrapper PID (886273, 886347) 仍存活，RSS ~3.5MB（正常，实际训练是子进程 886278/886352）。

**GPU 3 没有 hung**，训练正常运行，VRAM 占满 31.3GB。GPU 1 确认 hung。

---
