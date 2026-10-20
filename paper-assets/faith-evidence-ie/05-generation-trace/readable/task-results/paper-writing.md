# paper writing

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_20260517T174249_result.json`
- **Structured JSON:** [`fdc1464c5e02ffa14e83.json`](../../sessions/fd/fdc1464c5e02ffa14e83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `appendix.tex`，包含四个 section：

1. **Training Hyperparameters** (`tab:hyperparams`): 全参数对比表，`table*` 双栏宽度
2. **Full Ablation Results** (`tab:ablation_full`): CED/flat-NLI/top-k 完整消融，含全部 seed
3. **Scaling Details** (`tab:cross_detail`): 补充 Rel-F1/Evi-F1 per scale
4. **Additional Figures**: `fig:edcr_relations` 和 `fig:grpo_dynamics` 占位文本

所有表格使用 booktabs，小数精度统一（Ign-F1 xx.xx, Rel-F1 0.xxxx, Evi-F1 xx.xx, EDCR 0.xxxx），TBD 用 `\texttt{TBD}`，无 em-dash/en-dash。

---
