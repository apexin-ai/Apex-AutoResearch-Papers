# code prep dr filtered data 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_dr_filtered_data_30476_20260518T142259_result.json`
- **Structured JSON:** [`09298b8e323cf2ca32f2.json`](../../sessions/09/09298b8e323cf2ca32f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有文件已就绪，数据格式正确。汇总：

```
源数据: scored_data.jsonl — 371,499 samples

q01: 55,799 samples (q_score <= 0.1) [已有]
q03: 116,935 samples (q_score <= 0.3) [已有]
q05: 153,725 samples (q_score <= 0.5) [已有]
q07: 184,908 samples (q_score <= 0.7) [已有]
q09: 228,743 samples (q_score <= 0.9) [已有]
```

每个文件包含 `text`, `depth`, `source`, `q_score` 四个字段。无需新建任何文件。

---
