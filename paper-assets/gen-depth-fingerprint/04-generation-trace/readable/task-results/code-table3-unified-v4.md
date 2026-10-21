# code table3 unified v4

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_table3-unified-v4_20260516T184144_result.json`
- **Structured JSON:** [`bb36ecf4e1ca5b192ffa.json`](../../sessions/bb/bb36ecf4e1ca5b192ffa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

| Method | F1 | 95% CI |
|--------|------|--------|
| ld_score | 0.4909 | [0.4852, 0.4973] |
| entropy_mean | 0.6680 | [0.6620, 0.6742] |
| 4det_surface | 0.6857 | [0.6798, 0.6918] |
| 7feature | 0.6911 | [0.6853, 0.6972] |

7feature F1=0.6911，与 canonical 0.694 偏差 0.003，在容差范围内。N=26,168（排除 depth=0 后的 binary 样本），8 generators 全部参与。输出已保存到 `/root/gen-depth-fingerprint/results/8gen_table3_unified.json`。

---
