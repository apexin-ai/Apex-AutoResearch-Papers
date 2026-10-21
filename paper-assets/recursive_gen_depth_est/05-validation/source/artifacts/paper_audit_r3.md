## Paper Audit — 2026-05-15

Source: `docs/paper/` (main.tex + 9 section files + references.bib)

---

### ✅ 已完成

- **XX.X% / TODO / FIXME placeholders**: 所有 tex 文件中未发现任何 `XX.X`、`TODO`、`FIXME`、`placeholder` 占位符。所有数值均已填充。

- **Experiment ID 暴露**: 正文和 Table caption 中未发现任何实验 tracking ID（如 `_001`、`_002` 等模式）。

- **旧表述残留**: `geometry-level shift` 和 `genuine structural` 在所有 tex 文件中均未出现。D028 推翻的旧表述已清除。

- **Ethics Statement**: 已添加，位于 `conclusion.tex:41-46`。内容涵盖公开模型使用、无人类受试者、数据来源、潜在误用风险声明。

- **EDD 公式 (Eq.1)**: 已改为连续版本。`method.tex:91` 中公式为：
  `EDD_T = max { d*+1 : ∀ d' ≤ d*, AUC(d', d'+1) ≥ T }`
  包含 universal quantifier，与要求一致。

- **SHAP 内容 (§5.4)**: `generalization.tex:118-119` 中 §5.4 (End-to-End Learning) 已使用 SHAP TreeExplainer 分析，报告 perplexity/surprisal features 占 RF 贡献的 88.8%，三种 importance 方法 concordance (Kendall's W=0.896)。已替代 attention-importance。

- **DeBERTa/RoBERTa dual backbone (§5.4)**: `generalization.tex:96` 已纳入两个 backbone 结果——DeBERTa-v3-base (58.3%±4.7%) 和 RoBERTa-base (59.5%±3.2%)，1.2pp gap 排除 architecture bias。Table 8 (tab:e2e_detail) 展示 per-class F1。

- **XGBoost/LightGBM**: 已加入 Table 5 (`tab:baselines`, `generalization.tex:14-28`)。三个 atlas cell 上 RF/XGB/LGBM 对比，per-cell spread ≤0.4pp。注：原任务提及 "Table 2"，但当前编号为 Table 5（Table 2 是 atlas accuracy matrix）。

- **Feature ablation / '19-dimensional' 表述**: `19-dimensional` 已不出现。当前表述为 "19 candidate features"（`method.tex:45`, `abstract.tex:4`），并强调 top-5 achieve 97.6% of full-set performance，VIF 分析显示 effective dimensionality ≈4-5（`atlas.tex:57`）。已从维度数转为贡献度框架。

- **3-class accuracy 并列报告**: Abstract (`abstract.tex:5`) 并列报告 "70--85% four-class accuracy (chance = 25%; 58.8--82.6% when excluding the near-perfectly separable d0 class)"。Table 2 (`tab:main_matrix`, `atlas.tex:22`) caption 明确标注 "with d1--d3 three-class accuracy in parentheses (chance = 25% / 33%)"，每个 cell 均含/不含 d0 两组数值。

- **Universal scope 界定**: 
  - `introduction.tex:14`: "consistent across the three model families and three decoding strategies **studied**"（bounded by "studied"）
  - `method.tex:26`: "Our findings on feature importance and discriminability are **limited to this grid**; transfer to untested models, scales, or strategies is **not established**."
  - §4.2 subsection 已从 "Feature Universality" 改名为 "Feature Consistency Across the Grid"（`atlas.tex:44`；旧标题仅残留在 stale `.aux` 文件中）

---

### ❌ 未完成

- **Discussion 长度不足**: `discussion.tex` 主体仅 ~159 词（要求 ≥300 词）。当前 section 标题为 "Discussion and Conclusion"，将讨论和结论合并为一个简短段落。虽然 appendix 中有 Extended Discussion（`section_appendix.tex:139-154`，约 200 词），但主体 Discussion section 远低于 300 词阈值。
  - **需要修改**: 扩展 `discussion.tex`，至少增加以下内容到 ≥300 词：(a) 对 depth-graduated curation 的展开讨论（目前仅一句话）；(b) 与 binary detection 的互补关系；(c) 对 provenance toolkit 愿景的讨论。可考虑将 appendix Extended Discussion 的核心内容上移至主体。

- **Orphan bib entries**: `references.bib` 中 4 个条目未在任何 tex 文件中被 `\cite` 引用（也无 `\nocite`）：
  1. `bevendorff2025_two_paradigms` — Bevendorff et al., "The Two Paradigms of LLM Detection" (ACL 2025)
  2. `shi2025_closer_look` — Shi et al., "A Closer Look at Model Collapse" (NeurIPS 2025 Spotlight)
  3. `wu2025_detection_survey` — Wu et al., "A Survey on LLM-Generated Text Detection" (CL 2025)
  4. `yi2026_escaping_collapse` — Yi et al., "Escaping Model Collapse via Synthetic Data Verification" (ICLR 2026 Workshop)
  - **需要修改**: 要么在 Related Work 中引用这些条目（如 `wu2025_detection_survey` 适合 Detection 段、`shi2025_closer_look` 适合 Model Collapse 段），要么从 `references.bib` 中移除。

---

### ⚠️ 需确认

- **Stale .aux file**: `main.aux:494` 仍显示 §4.2 标题为 "Feature Universality"，但 `atlas.tex:44` 源码已改为 "Feature Consistency Across the Grid"。需重新编译 LaTeX 以更新 aux/toc。这不影响 PDF 内容（只要重新编译），但如果之前分发的 PDF 未重编译则仍显示旧标题。

- **Table 编号位移**: 任务中提及 "Table 2" 应含 XGBoost/LightGBM，但当前 Table 2 是 atlas accuracy matrix（`tab:main_matrix`），XGB/LGBM 在 Table 5（`tab:baselines`）。如果 R3 reviewer 的原始评论指的是特定 Table 编号，需确认当前编号是否与 response letter 中的引用一致。

- **Artifacts 旧目录**: 任务提及 `artifacts/_project/paper/section_*.tex` 为 RR3-W1 报告的不一致源，但该目录当前不含任何 .tex 文件（仅存 `references.bib`）。旧 section tex 文件已清除，但 `artifacts/_project/paper/references.bib` 仍存在且与 `docs/paper/references.bib` 内容相同（未产生不一致风险，但冗余）。

---

### 审计摘要

| # | 检查项 | 状态 |
|---|--------|------|
| 1 | XX.X% / TODO / FIXME placeholder | ✅ 无 |
| 2 | Experiment ID 暴露 | ✅ 无 |
| 3 | 旧表述残留 (geometry-level shift 等) | ✅ 已清除 |
| 4 | Orphan bib entries | ❌ 4 条 |
| 5 | Ethics Statement | ✅ 已添加 |
| 6 | Discussion ≥300 词 | ❌ ~159 词 |
| 7 | EDD 公式连续版本 | ✅ 已改 |
| 8 | SHAP 替代 attention-importance | ✅ 已替代 |
| 9 | DeBERTa/RoBERTa dual backbone | ✅ 已纳入 |
| 10 | XGBoost/LightGBM | ✅ 在 Table 5 |
| 11 | Feature ablation 表述调整 | ✅ 已调整 |
| 12 | 3-class accuracy 并列报告 | ✅ 已并列 |
| 13 | Universal scope 界定 | ✅ 已界定 |
