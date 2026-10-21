# fix bjb2 28827 disk cleanup

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bjb2-28827-disk-cleanup_20260526T022412_result.json`
- **Structured JSON:** [`0a3554068a0055d5f32b.json`](../../sessions/0a/0a3554068a0055d5f32b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 可用空间 | 4.3G | **11G** |
| 使用率 | ~86% | **66%** |

释放约 **6.7G**，来源：`/tmp/pip-*`、`/tmp/torch_*`、`/root/.cache/pip`、2天前的旧日志。根分区已恢复安全水位，无需进一步清理。

---
