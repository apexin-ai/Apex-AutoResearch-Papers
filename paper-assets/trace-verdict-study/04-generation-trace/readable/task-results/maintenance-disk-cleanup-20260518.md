# maintenance disk cleanup 20260518

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_maintenance_disk_cleanup_20260518_20260518T185534_result.json`
- **Structured JSON:** [`67ab0a9ab5b0dcd47387.json`](../../sessions/67/67ab0a9ab5b0dcd47387.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
BEFORE:  248G/250G (100%)
CLEANED: ~100G total (216 intermediate checkpoint dirs + 1 failed experiment)
AFTER:   148G/250G (60%)
```

释放约 100G，无遗留中间 checkpoint，所有 final/ 目录完好。

---
