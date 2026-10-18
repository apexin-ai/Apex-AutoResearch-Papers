# paper appendix forward refs and tables

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix-forward-refs-and-tables_20260524T051427_result.json`
- **Structured JSON:** [`5efea3d6c4bb28aa31d1.json`](../../sessions/5e/5efea3d6c4bb28aa31d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits look correct. Here's the summary:

---

## 产出汇总

### Part A: Forward references (6 个)

| # | Label | 文件:行 | 插入内容 |
|---|-------|---------|----------|
| 1 | `app:stance` | experiments.tex:10 | `stance detection (Appendix~\ref{app:stance})` 加入 robustness validation 列表 |
| 2 | `app:semireal` | experiments.tex:11 | `Appendix~\ref{app:semireal}` 加在 16 model-dataset combinations 后 |
| 3 | `app:roc` | experiments.tex:72 | `Figure~\ref{fig:roc} in Appendix~\ref{app:roc}` 替换原来只引 Figure |
| 4 | `app:realcm_bias` | experiments.tex:77 | `Appendix~\ref{app:realcm_bias}` 加在 $R^2=0.975$ 后 |
| 5 | `app:robustness` | experiments.tex:83 | 新增句子 "EC-HTE is robust to noisy subgroup labels ($p_{\text{flip}} \leq 0.50$; Appendix~\ref{app:robustness})." |
| 6 | `app:mcmc` | method.tex:16 | `full MCMC specification in Appendix~\ref{app:mcmc}` 加在 convergence diagnostics 引用前 |

### Part B: 表格迁移

**表 1 (γ_T sweep)**:  未创建新表——数据与现有 `tab:treatment_dep`（appendix.tex L1298-1311）完全一致。在 theory.tex:98 添加了 forward ref `(full sensitivity in Table~\ref{tab:treatment_dep}, Appendix~\ref{app:treatment_dep})`。`results/` 下无 CSV 文件，无 Global 值数据源。

**表 2 (hyperprior sweep)**: 在 appendix.tex 的 MCMC 节新建 `\subsection{Hyperprior Sensitivity}` (`app:hyperprior`)，含 `tab:hyperprior_sweep` 摘要表（6 行，registry 数据）。在 method.tex:12 添加 forward ref `Table~\ref{tab:hyperprior_sweep}, Appendix~\ref{app:hyperprior}`。无 `exp001_hyperprior_sensitivity.csv`，无法建完整 (a₀, b₀) 网格表，用摘要表替代。

### 编译结果
- 32 页（+1 页来自新表），主文 ≤ 8 页
- 0 个新 error（3 个预存 `\makecell` undefined 来自 appendix_stance.tex）
- 0 个 undefined reference（第二遍编译后全部解析）

---
