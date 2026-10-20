# paper fix eq1 ci definition

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-eq1-ci-definition_20260519T062703_result.json`
- **Structured JSON:** [`70a2c78c833d3634f0f9.json`](../../sessions/70/70a2c78c833d3634f0f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

0 errors, 28 pages, two passes clean.

修改总结：

1. **method.tex Eq.1**：将 `\auc_{k-1,k} > \theta` 改为 `\mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k}) > \theta`，定义说明从 "point-estimate pairwise AUC" 改为 "lower bound of a 95% bootstrap confidence interval over the pairwise AUC"。新增一句说明该准则确保 K* 反映统计上稳健的可区分性。非边界对的 CI upper bound 验证保留为独立检查。

2. **experiments_c1.tex Table 1 caption**：将 "requires 1v2 AUC > θ" 改为 "requires 1v2 CI lower bound > θ"，并引用 Eq.1。

3. **appendix_extended.tex code domain table footnote**：同步修改 K* 定义为 CI lower bound 形式，引用 Eq.1。

---
