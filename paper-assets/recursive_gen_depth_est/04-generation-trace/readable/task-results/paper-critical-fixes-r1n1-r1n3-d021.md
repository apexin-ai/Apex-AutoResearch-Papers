# paper critical fixes r1n1 r1n3 d021

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_critical-fixes-r1n1-r1n3-d021_20260515T133738_result.json`
- **Structured JSON:** [`18a99618178d0218d0ad.json`](../../sessions/18/18a99618178d0218d0ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有改动已验证正确。

### 修改汇总

**atlas.tex** — Issue 1 (R1-N1 EDD 正式定义)
- `sec:atlas:edd` 子节：原来一句话引用 method section，改为完整的 EDD 定义段落
- 添加了正式数学公式 `EDD_T = max{d*+1 : AUC(d*, d*+1) ≥ T}`
- 说明了 AUC(d, d+1) 是 binary pairwise classifier 的 ROC AUC
- 说明了 T=0.75 默认阈值及其选择理由
- 添加了直觉含义：超过此深度后相邻深度变得统计不可区分

**generalization.tex** — Issue 2 (R1-N3 end-to-end baseline 对比表)
- `sec:gen:dcol` 子节：添加了 `tab:e2e_baselines` 表格（RF 78.2% / RoBERTa 59.5±3.2% / DeBERTa 58.3±4.7% / DeepSeek 40.0% / Chance 25.0%，含 Δ vs RF 列）
- 说明 MLM vs disentangled attention 两种架构一致结论（1.2pp gap），排除 architecture bias
- 新增 "Feature overlap analysis" 段落：Spearman ρ=-0.484 (p=0.036)，PLM 擅长 TTR (R²=0.85) 但 var_surprisal/p90_ppl R² 为负，结论：hand-crafted features 捕获 PLM 无法学到的深度信号

**generalization.tex** — Issue 3 (D021 z-score claim 修正)
- z-score 段落：删除 "substantially improves...for nucleus and top-k holdouts" 的 recovery 措辞
- 改为：overall LR accuracy 25%→61%，但 temp d1v2 AUC 恶化（GPT-2 XL 0.50→0.24, OLMo 0.50→0.19）
- 结论改为 "genuine geometry-level shift in feature space rather than a correctable scale difference"

**introduction.tex** — Issue 3 (D021 z-score claim 修正)
- 贡献列表第 3 条：删除 "recovers logistic regression performance for non-temperature holdouts"
- 改为：overall LR accuracy 25%→61% + 不恢复 temperature d1v2 inversion + 确认 geometry-level shift

---
