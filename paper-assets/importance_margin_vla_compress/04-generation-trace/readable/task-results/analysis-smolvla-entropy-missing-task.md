# analysis smolvla entropy missing task

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_smolvla_entropy_missing_task_20260518T071144_result.json`
- **Structured JSON:** [`d64e51722eb855776c07.json`](../../sessions/d6/d64e51722eb855776c07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

问题比预期更严重。实际采样的 9 个 task 是 **LIBERO-90 的 task 0-8**，不是 LIBERO-Object。

根本原因：脚本按文件顺序（file-000, file-001, ...）读取，256 帧在前 10 个文件就采满了，而 LIBERO-Object 是 task_index 20-29，数据在更靠后的文件中，完全没被采到。

LIBERO-Object 10 个 task（全部缺失）：
| idx | task |
|-----|------|
| 20 | pick up the orange juice |
| 21 | pick up the ketchup |
| 22 | pick up the cream cheese |
| 23 | pick up the bbq sauce |
| 24 | pick up the alphabet soup |
| 25 | pick up the milk |
| 26 | pick up the salad dressing |
| 27 | pick up the butter |
| 28 | pick up the tomato sauce |
| 29 | pick up the chocolate pudding |

**修复方案**：在采样循环中加 `task_idx in range(20, 30)` 过滤，只采 LIBERO-Object 的帧。需要我修改脚本并在 cqa1 GPU 1 上补跑吗？

---
