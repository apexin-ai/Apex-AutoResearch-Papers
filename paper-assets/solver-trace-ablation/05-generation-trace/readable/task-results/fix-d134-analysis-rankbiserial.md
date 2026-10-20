# fix d134 analysis rankbiserial

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d134-analysis-rankbiserial_20260518T150748_result.json`
- **Structured JSON:** [`0aca2f89a112fe0f1c80.json`](../../sessions/0a/0aca2f89a112fe0f1c80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复验证通过。Mann-Whitney U 部分关键输出：

```
  3. H7 Rate Mann-Whitney U Test
     ISR median:    85.7%
     RANDOM median: 0.0%
     U = 10.0, p = 0.0393
     Rank-biserial r = 1.0000
```

**r = +1.0000**，符合预期（ISR H7% 完全高于 Random H7%）。之前错误公式输出 r = -1.0，现在已修正为 `2U/(n1*n2) - 1`。

---
