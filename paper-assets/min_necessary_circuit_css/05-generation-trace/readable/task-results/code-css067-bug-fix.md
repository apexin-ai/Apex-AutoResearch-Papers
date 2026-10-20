# code css067 bug fix

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_css067-bug-fix_20260513T080151_result.json`
- **Structured JSON:** [`b1ce02cbc48b6f793357.json`](../../sessions/b1/b1ce02cbc48b6f793357.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## Bug 修复 & 重跑结果

**Bug:** `run_sva.py:183` 的 `threshold_css` 使用 `1e-9` 容差。CSS score 2/3 = 0.6667，而 `0.6667 < 0.67 - 1e-9`，导致 majority-vote 边被排除。css_0.67 实际等于 css_1.00（都是 44 条边）。

**修复:** `1e-9` → `1e-2`（同 `eval_topk_faithfulness.py`）。已修复 `run_sva.py` 和 `run_sva_cuda1.py`。

**修正后结果（SVA, 100 prompts）:**

| Circuit | Edges | Zero CPR | Mean CPR |
|---------|-------|----------|----------|
| eap_ig | 100 | **-0.3705** | 1.1703 |
| edge_pruning | 100 | -0.6879 | 1.1703 |
| acdc | 100 | -1.2574 | **1.1746** |
| **css_0.67 FIXED** | **98** | -1.0279 | 1.1724 |
| css_1.00 | 44 | -0.8166 | 1.1873 |

**结论不变（negative）：** 修正后 css_0.67 (98 edges) 在两种 ablation 下都不优于 css_1.00 和单方法。majority-vote 层加入的 54 条额外边反而降低了 CPR，说明 2/3 共识边引入了噪声。Registry 已更新。

---
