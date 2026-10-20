## R20 修复报告

### MF1: (A2) 对称假设讨论

**Point A — method.tex Section 4.1**
- 新增位置：method.tex:11
- 新增内容：`The model estimates the full $J \times J$ confusion matrix per subgroup and does not require symmetric error rates~(A2); (A2) simplifies only the diagnostic (Proposition~\ref{prop:debiasing_hurts}).`
- 删减位置：method.tex:14 (原文)
- 删减内容：James-Stein 长解释 `---James-Stein shrinkage, a standard technique in small-area estimation applied here to per-subgroup confusion matrix estimation for causal inference---borrows strength across subgroups from limited expert labels,` → 简化为 `borrows strength across subgroups,`

**Point B — experiments.tex Section 5.4**
- 新增位置：experiments.tex:81-85
- 新增内容：新段落 `\paragraph{Assumption~(A2) in practice.}` 包含：(1) EC-HTE 不依赖 A2，(2) 诊断在 FPR≠FNR 下 AUC 从 0.86 降至 0.66，(3) 建议配合 R² 验证 (R²=0.991, coverage≥93.5%)
- 配套删减：experiments.tex 原 L73-74（AUC 解释 + K=2 限制细节）简化为 1 句

### MF2: Abstract AUC 报告顺序

- 修改位置：abstract.tex:6
- 原文：`(AUC $= 1.0$ on subgroups with non-zero $\Delta\tau$; $0.86$ across all synthetic subgroups; $0.63$ on real LLM error profiles)`
- 改为：`(AUC $= 0.86$ across all synthetic subgroups, reaching $1.0$ when $\Delta\tau > 0$; $0.63$ on real LLM error profiles)`
- Abstract 字数：~170 words (≤200 限制)

### SF3: 补 4 篇遗漏引用

- 新增位置：related_work.tex:24, 34-35
- 新增引用：
  1. `\citet{gligoric2025unconfident}` — NAACL 2025, confidence-driven data fusion for LLM annotations (L24)
  2. `\citet{ura2018heterogeneous}` — QE 2018, HTE with mismeasured endogenous treatment via IV (L34, 更新自 ura2015)
  3. `\citet{knox2022testing}` — ARPS 2022, ML proxy variables bias in causal estimation (L35)
  4. `\citet{knox2020administrative}` — APSR 2020, racial misclassification in administrative records (L35)
- bib 更新：references.bib — 更新 ura2015→ura2018（含卷期页码），新增 gligoric2025unconfident, knox2022testing, knox2020administrative
- 配套删减：related_work.tex 原 L37（验证方法论声明）删除

### SF1: Table 22 筛选结果

- 新增位置：experiments.tex:78
- 新增内容：`Under strict screening, no real LLM--dataset pair passes all conditions simultaneously (Table~\ref{tab:screening}); under relaxed screening (dropping the FNR$<$0.50 requirement), 79\% of configurations show RMSE improvement over global correction, with all 16 combinations maintaining coverage $\geq$93\% (Appendix~\ref{app:screening}).`

### SF4: PPCI 组合充分条件

- 新增位置：method.tex:56
- 新增内容：`Composition is valid when covariate and outcome error sources are independent---a sufficient condition satisfied in our DGP (Appendix~\ref{sec:ppci}); verification under correlated error sources remains for future work.`
- 配套删减：method.tex 原 PPCI 段落从 6 行压缩到 3 行

### SF5: Eq.6 独立性假设

- 新增位置：method.tex:44 (Eq.6 后)
- 新增内容：`This plug-in SE assumes independence between CausalForest estimation error and CM estimation error.` + 脚注讨论 expert label 与训练数据重叠影响

### SF6: (A3) P(Z=1)=0.5 退化

- 新增位置：experiments.tex:85
- 新增内容：`Under class imbalance ($P(Z{=}1) = 0.1$), the bias identity retains $R^2 \geq 0.976$ but EC-HTE's RMSE ratio relative to global correction increases to 1.06--1.68 (Appendix~\ref{app:classimbalance}).`

### Figure 2 引用格式

- 修改位置：experiments.tex:18, theory.tex:119
- 改动：`Figure~\ref{fig:heatmap}` → `Figure~\ref{fig:heatmap} (Appendix~\ref{app:dgp})`（fig:heatmap 在附录中）

### 删减汇总

| 文件 | 删减内容 | 节省行数 |
|------|---------|---------|
| method.tex L14 | James-Stein 长解释 | ~1.5 |
| method.tex L19-21 | 阈值细节 + 收敛 + 敏感性重复 | ~3 |
| method.tex L35-37 | Global vs stratified 对比段 | ~2 |
| method.tex L55-61 | PPCI 段落 6→3 行 | ~3 |
| theory.tex L50-54 | F-L 标量衰减详细讨论 | ~2 |
| experiments.tex L73-74 | AUC 解释 + K=2 限制 | ~1.5 |
| experiments.tex L79 | Hate speech 冗余 | ~0.5 |
| related_work.tex L37 | 验证方法论声明 | ~2 |
| **合计** | | **~15.5** |

### 编译验证

- 页数：8 页主文 + limitations（第 8 页开始），第 9 页起为 references + appendix。总 32 页。
- Errors：0
- Undefined refs：0（bibtex + 2 次 pdflatex 后全部解析）
- Abstract words：~170（≤200 限制）
