# investigate c2 qwq layer check

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_c2_qwq_layer_check_20260517T012949_result.json`
- **Structured JSON:** [`dbf3b2572953e1aeef92.json`](../../sessions/db/dbf3b2572953e1aeef92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
QwQ layer used: 1
Is corrected layer 2: NO
Evidence: selectivity_results.json 中 qwq_32b.layer_absolute = 1，selectivity = 0.1889 (18.9pp)。使用的是 layer 1，不是 M001 修正后的 layer 2。
```

需要在 corrected layer 2 上重跑 QwQ-32B 的 control task selectivity。

---
