# analysis null t15 6pair recheck

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_null_t15_6pair_recheck_20260524T095105_result.json`
- **Structured JSON:** [`87ec7858726959ce2122.json`](../../sessions/87/87ec7858726959ce2122.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

```
null_t15_s42: 6-pair PermG fwd 0/6, rev 0/6, K≥3 0/6
null_t15_s43: 6-pair PermG fwd 0/6, rev 0/6, K≥3 1/6
```

s43 的 K≥3 FP pair 是 **ece→distinct_1**（naive+diff+threshold 三票），不涉及 mauve——从 8-pair 的 1/8 变成 6-pair 的 1/6，该 FP 保留。

---
