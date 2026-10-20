# Bootstrap CI 引用审计报告

> 审计日期: 2026-05-18
> 背景: Bootstrap resampling 打破 GroupKFold 结构，导致数据泄漏（+6.4pp inflation on 1v2 AUC）。需确认论文正文中所有 bootstrap CI 引用已替换为 fold-based CI。

## 结论

**论文 .tex 源文件中仍有 13 处残留 bootstrap 引用描述我们自己的方法，全部需要修改为 fold-based CI。**

---

## 一、需要修改的位置（描述我们自己的方法）

### 1. docs/paper/method.tex — 第 25 行（核心方法论描述，最高优先级）

**当前文本:**
```
Bootstrap 95\% confidence intervals (CIs; 1{,}000 resamples\footnote{Boundary-pair results in Table~\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
```

**建议替换为:**
```
We quantify uncertainty via fold-based 95\% confidence intervals (CIs) derived from the five GroupKFold splits: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
```
> 说明: 删除 footnote（resamples 数量不再适用），改为描述 fold-based CI 方法。

---

### 2. docs/paper/method.tex — 第 43 行

**当前文本:**
```
...bootstrap CIs in Table~\ref{tab:selfbleu_ablation}...
```

**建议替换为:**
```
...fold-based CIs in Table~\ref{tab:selfbleu_ablation}...
```

---

### 3. docs/paper/experiments_c1.tex — 第 15 行（主结果表 caption）

**当前文本:**
```
Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
```

**建议替换为:**
```
Pairwise $\auc$ for adjacent depth pairs with fold-based 95\% CIs and permutation $p$-values for boundary rows.
```

---

### 4. docs/paper/experiments_c1.tex — 第 83 行

**当前文本:**
```
Bootstrap CIs (10{,}000 resamples) confirm $\Kempirical{=}3$ for Qwen-1.5B (CI lower $= 0.617$) and LLaMA-8B (CI lower $= 0.605$); for Mistral-7B (CI: $[0.593, 0.622]$) and Qwen-7B (CI: $[0.584, 0.613]$), the CI straddles $\theta$; their $\Kempirical{=}3$ assignment is sensitive to resampling variance (Table~\ref{tab:arxiv_crossscorer_ci}).
```

**建议替换为:**
```
Fold-based CIs confirm $\Kempirical{=}3$ for Qwen-1.5B (CI lower $= 0.617$) and LLaMA-8B (CI lower $= 0.605$); for Mistral-7B (CI: $[0.593, 0.622]$) and Qwen-7B (CI: $[0.584, 0.613]$), the CI straddles $\theta$; their $\Kempirical{=}3$ assignment is sensitive to fold variance (Table~\ref{tab:arxiv_crossscorer_ci}).
```
> 注意: CI 数值需要用新的 fold-based 计算结果替换（此处仅标记文本层面修改，数值替换需另行确认）。

---

### 5. docs/paper/appendix.tex — 第 14 行（Figure S1 caption）

**当前文本:**
```
Pairwise $\auc$ decay curves for five model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples.
```

**建议替换为:**
```
Pairwise $\auc$ decay curves for five model-mode configurations with fold-based 95\% confidence intervals. Error bars computed from five GroupKFold splits.
```

---

### 6. docs/paper/appendix.tex — 第 65 行（Table S2 caption, decoding ablation）

**当前文本:**
```
Pairwise AUC with bootstrap 95\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples).
```

**建议替换为:**
```
Pairwise AUC with fold-based 95\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode).
```

---

### 7. docs/paper/appendix.tex — 第 97 行（Table S3 caption, extended 9-config）

**当前文本:**
```
Extended pairwise $\auc$ with bootstrap 95\% CIs for all 9 model configurations.
```

**建议替换为:**
```
Extended pairwise $\auc$ with fold-based 95\% CIs for all 9 model configurations.
```

---

### 8. docs/paper/appendix.tex — 第 377 行（Table S10 caption, Pythia decoding）

**当前文本:**
```
Pairwise $\auc$ with bootstrap 95\% CIs across depth pairs for Pythia-1.4B under four decoding configurations (Exp-020; 10{,}000 bootstrap resamples).
```

**建议替换为:**
```
Pairwise $\auc$ with fold-based 95\% CIs across depth pairs for Pythia-1.4B under four decoding configurations (Exp-020).
```

---

### 9. docs/paper/appendix.tex — 第 399 行（Table S11 caption, length ablation）

**当前文本:**
```
...the 1v2 bootstrap CI lower bound falls marginally below $\theta$.
```

**建议替换为:**
```
...the 1v2 fold-based CI lower bound falls marginally below $\theta$.
```

---

### 10. docs/paper/appendix_extended.tex — 第 44 行（retrain-chain table caption）

**当前文本:**
```
Retrain-chain pairwise $\auc$ with bootstrap 95\% CIs (Pythia-1.4B LoRA, 5 generations).
```

**建议替换为:**
```
Retrain-chain pairwise $\auc$ with fold-based 95\% CIs (Pythia-1.4B LoRA, 5 generations).
```

---

### 11. docs/paper/appendix_extended.tex — 第 198 行（self-BLEU ablation caption）

**当前文本:**
```
15D vs.\ 14D (self\_BLEU removed) 1v2 $\auc$ with bootstrap 95\% CIs. Removing self\_BLEU does not change $\Kempirical$ for any configuration. Maximum $|\Delta\auc| = 0.0031$, within bootstrap CI width (${\sim}0.018$).
```

**建议替换为:**
```
15D vs.\ 14D (self\_BLEU removed) 1v2 $\auc$ with fold-based 95\% CIs. Removing self\_BLEU does not change $\Kempirical$ for any configuration. Maximum $|\Delta\auc| = 0.0031$, within fold-based CI width (${\sim}0.018$).
```

---

### 12. docs/paper/appendix_extended.tex — 第 253 行（section title）

**当前文本:**
```
\subsection{ArXiv Cross-Scorer Bootstrap CIs}
```

**建议替换为:**
```
\subsection{ArXiv Cross-Scorer Fold-Based CIs}
```

---

### 13. docs/paper/appendix_extended.tex — 第 259 行（arXiv cross-scorer CI table caption）

**当前文本:**
```
Bootstrap 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.
```

**建议替换为:**
```
Fold-based 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\auc$. Point estimates classify 3/4 generators as $\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.
```

---

## 二、无需修改的位置（引用他人方法）

| 文件 | 行号 | 内容 | 理由 |
|------|------|------|------|
| `docs/paper/related_work.tex` | 20 | "importance resampling" (Drayson et al., DSIR) | 描述他人方法 |
| `docs/paper/references.bib` | 87 | DSIR 论文标题含 "Importance Resampling" | 文献标题 |
| `docs/paper/main.bbl` | 297 | 编译后书目，同上 | 自动生成 |

---

## 三、自动生成文件（无需手动修改）

`docs/paper/main.aux` 中有约 15 处 bootstrap 引用，均为 LaTeX 编译自动生成。修改上述 .tex 源文件后重新编译即可消除。

---

## 四、补充提醒

1. **CI 数值**: 上述建议仅覆盖文本层面的 "bootstrap" → "fold-based" 替换。表格中的 CI 数值区间需确认已使用 fold-based 方法重新计算。若数值未更新，表格数据也需同步替换。
2. **Figure S1 (fig_s1_auc_decay_ci.pdf)**: 如果该图的 error bars 仍基于 bootstrap resamples 绘制，需要用 fold-based CI 重新生成图片。
3. **artifacts/ 下的旧报告**: `exp_008_retrain_chain_v2/bootstrap_ci_results.md`、`exp_019_mistral7b_depth/report/exp019_bootstrap_ci.md`、`exp_14b_c4_bootstrap_ci/results_summary.md` 等为历史实验记录，不在论文中引用，无需修改但建议标记为 DEPRECATED。
