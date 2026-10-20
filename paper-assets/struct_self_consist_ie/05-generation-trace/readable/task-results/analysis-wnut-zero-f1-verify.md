# analysis wnut zero f1 verify

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wnut_zero_f1_verify_20260515T042552_result.json`
- **Structured JSON:** [`ea513f625edb9cb6b777.json`](../../sessions/ea/ea513f625edb9cb6b777.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
WNUT-17 Zero F1 核实：
- 原始实例数: 1287
- Gold-nonempty: 689
- Gold-empty: 598
- Greedy F1 = 0: 355 (51.5%)
- Greedy F1 > 0: 334 (48.5%)
- 论文 "54%" 是否正确: NO，正确值为 51.5%
```

**Reviewer 是对的。** 355/689 = 51.5%，论文写的 "54%" 不准确，需要修正为 51.5%（或 "approximately 52%"）。

结果已保存到 `/root/autodl-tmp/struct_self_consist_ie/output/review_round2/wnut_zero_f1_verify.json`。

---
