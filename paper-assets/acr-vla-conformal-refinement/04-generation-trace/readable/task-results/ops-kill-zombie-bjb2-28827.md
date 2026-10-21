# ops kill zombie bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-zombie-bjb2-28827_20260518T151906_result.json`
- **Structured JSON:** [`530ba257c93a3592d705.json`](../../sessions/53/530ba257c93a3592d705.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**PID 497445 (eval-obs-only-norm01-s42)**：已经自行退出，无需 kill。

**cuda:1 状态**：现在只有 PID 578945 一个进程，显存占用 5182MiB / 24564MiB，冲突已解除。

**cuda:5 状态**：PID 594156 在运行，显存 5645MiB，正常工作。（注意 PID 是 594156 而非你预期的 594147，可能是 wrapper/子进程关系）

**各 GPU 汇总**：
| GPU | PID | 显存 |
|-----|-----|------|
| 0 | 492545 | 1887MiB |
| 1 | 578945 | 5182MiB |
| 2 | 575343 | 4717MiB |
| 3 | 579221 | 5182MiB |
| 4 | 514350 | 1887MiB |
| 5 | 594156 | 5645MiB |

6 张卡各一个进程，无冲突。

---
