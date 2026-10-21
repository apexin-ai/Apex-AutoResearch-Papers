# analysis output mbr selection

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_output_mbr_selection_20260518T162549_result.json`
- **Structured JSON:** [`0f0051679c15e09228a6.json`](../../sessions/0f/0f0051679c15e09228a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结论：

**MBR selection（entity-set Jaccard over (text,type)）对 NER 无效。**

| Dataset | Greedy | LP Sel | **MBR Sel** | Oracle | MBR-Grd | MBR-LP |
|---------|--------|--------|-------------|--------|---------|--------|
| SciERC  | 0.6439 | 0.6501 | **0.6444**  | 0.7758 | +0.0005 | -0.0057 |
| CoNLL   | 0.9087 | 0.8985 | **0.9043**  | 0.9520 | -0.0043 | +0.0059 |
| FewNERD | 0.7478 | 0.7610 | **0.7208**  | 0.8686 | -0.0269 | -0.0402 |

- MBR 在 2/3 数据集上低于 Greedy，2/3 数据集上低于 LP
- FewNERD 上 MBR 显著差于两个 baseline（-2.7% vs Greedy，-4.0% vs LP）
- Degeneracy 分析：MBR 仅在 SciERC 高多样性 instances 上有微弱优势（+1.8%），其余全部为负

失败原因：MBR 倾向选出只包含"easy"共识实体的 sample，遗漏少数 samples 正确检测到的难实体。LP selection 仍是更强的 single-sample selection baseline。

产出：
- 脚本：`code/analysis_mbr_selection.py`（服务器 + 本地）
- 结果 JSON：服务器 `output/analysis_mbr_selection.json`
- 报告：`artifacts/mbr_selection/mbr_selection_results.md`

---
