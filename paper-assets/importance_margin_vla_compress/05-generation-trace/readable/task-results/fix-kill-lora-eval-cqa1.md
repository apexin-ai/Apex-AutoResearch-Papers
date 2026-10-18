# fix kill lora eval cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill_lora_eval_cqa1_20260516T215439_result.json`
- **Structured JSON:** [`bccd6c55d53cf0d8fb0a.json`](../../sessions/bc/bccd6c55d53cf0d8fb0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 1 已经是空闲状态** — 仅 1 MiB 显存占用，利用率 0%。

没有 LoRA eval 进程在 GPU 1 上运行。当前各 GPU 状态：

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 5909 MiB | 15% (full_ft eval, PID 73186 + PID 45551) |
| 1 | **1 MiB** | **0%** ✓ 已空闲 |
| 2 | 2107 MiB | 29% |
| 3 | 2749 MiB | 44% |

LoRA 100K eval 进程可能已经自行结束或之前已被 kill。GPU 1 无需额外操作。

---
