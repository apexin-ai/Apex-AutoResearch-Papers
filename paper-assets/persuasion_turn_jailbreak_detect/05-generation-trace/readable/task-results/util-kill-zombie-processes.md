# util kill zombie processes

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_util_kill-zombie-processes_20260519T092902_result.json`
- **Structured JSON:** [`9b2ca4db29a71df700f2.json`](../../sessions/9b/9b2ca4db29a71df700f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

| PID | 进程 | kill 结果 |
|-----|------|-----------|
| 27231 | `python -c ...` (DeBERTaTopic 模型加载) | `kill` 正常终止 |
| 27437 | `python -u src/binary_perturbed_eval.py` | `kill` 正常终止 |

nvidia-smi 最终状态：cuda:0~3 全部 0 MiB 占用、0% 利用率，4 张卡完全释放。

---
