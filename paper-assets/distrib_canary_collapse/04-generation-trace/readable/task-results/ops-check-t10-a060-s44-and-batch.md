# ops check t10 a060 s44 and batch

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-t10-a060-s44-and-batch_20260523T204414_result.json`
- **Structured JSON:** [`ee32a0e6aa116dcdbbc5.json`](../../sessions/ee/ee32a0e6aa116dcdbbc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果汇总：**

**scale_14b_t10_a060_s44_fp32** — 已完成 (gen_0–gen_10)
- distinct_3: 0.819 → 0.598, ppl: 19.83 → 63.79
- D102 (distinct_3): 2/2 robust pairs, PermG fwd 2/2, rev 0/2
  - token_entropy→d3: 3/5 [diff, perm, ty]
  - ece→d3: 4/5 [naive, diff, perm, ty]
- Registry 已更新 DONE(success) + metrics

**仍在运行 (5个)：**
- westd-17855: t15_a045_s43 (15h48m), t10_a050_s44 (11h37m), t10_a045_s44 (8h11m)
- westd-19828: t15_a075_s43 (14h03m), t10_a075_s44 (11h43m)

---
