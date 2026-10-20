# analysis mbr selection

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mbr_selection_20260518T162305_result.json`
- **Structured JSON:** [`a2f3d863c360bd075cdc.json`](../../sessions/a2/a2f3d863c360bd075cdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已写入 `artifacts/mbr_selection/mbr_selection_results.md`，脚本在 `code/analysis_mbr_selection.py`。

**核心发现：MBR selection 在 NER 上全面失败。**

| Dataset | Greedy | LP Sel | **MBR Sel** | Oracle |
|---------|--------|--------|-------------|--------|
| SciERC  | 0.6439 | 0.6501 | **0.6449**  | 0.7758 |
| CoNLL   | 0.9087 | 0.8985 | **0.9045**  | 0.9520 |
| FewNERD | 0.7713 | 0.7800 | **0.7511**  | 0.8831 |

MBR 仅在 SciERC 上微超 Greedy (+0.001)，在 FewNERD 上大幅落后 (-0.020 vs Greedy, -0.029 vs LP)。

原因：MBR 选"最接近中心"的 sample，在 NER 中这倾向于选只预测"简单共识 entity"的 sample（高 precision、低 recall），遗漏了部分 sample 正确识别的难 entity。NER 的离散集合结构与 NMT 的连续相似性结构不同，pairwise consensus 不是 quality 的好 proxy。

---
