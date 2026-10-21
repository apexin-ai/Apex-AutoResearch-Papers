# fix cqa1 gpu3 duplicate check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1_gpu3_duplicate_check_20260528T004612_result.json`
- **Structured JSON:** [`9178dfdada12c5d21ab5.json`](../../sessions/91/9178dfdada12c5d21ab5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 3 无问题，无需清理。

**GPU 3 进程情况：**
- 仅 PID 894077 占用 GPU 3（UUID `a2a15ad4`），10500 MiB，61% 利用率
- 无多余进程抢资源

**其他 GPU：**
| GPU | PID | 显存 | 利用率 |
|-----|-----|------|--------|
| 0 | 765078 | 10420 MiB | 21% |
| 1 | 797637 | 9818 MiB | 0% |
| 2 | — | 1 MiB | 0% |
| 3 | 894077 | 10500 MiB | 61% |

**v2 进度：** 已正常运行，08:43 UTC 完成 T0（60%），之前的"慢"只是模型加载耗时（08:35→08:38 加载模型，08:38→08:43 完成首个 task 的 10 episodes）。

---
