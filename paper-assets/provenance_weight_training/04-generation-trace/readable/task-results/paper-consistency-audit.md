# paper consistency audit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_consistency-audit_20260516T005941_result.json`
- **Structured JSON:** [`9788bec5979e26623bf4.json`](../../sessions/97/9788bec5979e26623bf4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查报告已写入 `artifacts/_project/paper/consistency_audit.md`。

核心发现：

**最高优先级（CRITICAL x5）**：
1. **table1_main_results.tex 与 results 正文冲突**：table1 用 n_min=3 作为主结果（PPL 17.639，标粗），但正文全部用 n_min=2（PPL 17.651）。整篇论文的 narrative 取决于选哪个——需要立刻决定。
2. **intro (c6a67f) adaptive PPL 写成 17.650，实际是 17.651**
3. **intro (base) ESS-only PPL 写成 17.722，实际是 17.723**
4. **两代文件的 citation key 完全不兼容**（`shumailov2024model` vs `shumailov_2024_model_collapse`），混用会导致 [?]
5. **table label 冲突**：`tab:main` vs `tab:main-results`

**WARNING x7**：macro/notation 不统一、"dual-constrained" vs "dual-constraint" 混用、contribution 3 overclaim（声称 comparable to neural detectors 但没做对比实验）、method.tex 51,913 micro-batches 与 experiments 描述的 24,412 不符、n_min=3 在 table1 是主结果但在 sensitivity table 标注为"not an independent ablation"。

---
