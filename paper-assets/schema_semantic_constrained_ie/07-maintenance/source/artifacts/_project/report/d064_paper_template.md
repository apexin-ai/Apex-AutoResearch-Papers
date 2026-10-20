# d064 入稿模板：Beam Search 50-doc → 998-doc 全量更新

## 1. 完整更新位置清单

### appendix_beam_search.tex（主战场）

| 行号 | 当前内容（摘要） | 需更新为 |
|------|----------------|---------|
| L23 | "DocRED evaluated on matched 50-document subsets (same documents for greedy and beam)." | "DocRED evaluated on the full 998-document dev set." |
| L34 | `Qwen3-8B / DocRED (50)` | `Qwen3-8B / DocRED (998)` |
| L35 | Greedy: `8.69 & 2.08 & 59.08 & 8.33` | 替换为 998-doc greedy 数据 |
| L36 | Beam: `0 & 0 & 0.55 & 58.64 & 9.37` | 替换为 998-doc beam 数据 |
| L42 | `Llama-3.1-8B / DocRED (50)` | `Llama-3.1-8B / DocRED (998)` |
| L43 | Greedy: `1.58 & 6.85 & 55.35 & 6.12` | 替换为 998-doc greedy 数据 |
| L44 | Beam: `0 & 0 & 0.94 & 55.62 & 9.47` | 替换为 998-doc beam 数据 |
| L50 | `Mistral-7B / DocRED (50)` | `Mistral-7B / DocRED (998)` |
| L51 | Greedy: `28.37 & 0.34 & 51.60 & 4.19` | 替换为 998-doc greedy 数据 |
| L52 | Beam: `21.37 & 0.19 & 51.78 & 5.70` | 替换为 998-doc beam 数据 |
| L58 | "DocRED with 96 relation types, 50 documents" | "DocRED with 96 relation types, 998 documents" |
| L60 | "On DocRED (matched 50-document subsets), beam search eliminates DR for both Qwen (8.69%→0%) and Llama (1.58%→0%), with CF reductions of 74% and 86% respectively." | 替换为 998-doc 数据和 reduction 百分比 |
| L61 | "Llama DocRED shows the largest R-F1 gain (+3.4 pp)" | 根据新数据重算 R-F1 差值 |
| L66 | "On DocRED (96 relation types), beam search reduces DR by 25% relative (28.4%→21.4%)" | 替换为 998-doc Mistral 数据 |
| L100 | "Beam search on DocRED introduces a modest increase in parse failures (3/50, 6%)" | 替换为 998-doc parse failure 数据 (X/998, Y%) |
| L101 | "With DR=0 in 50 DocRED documents for both calibrated models, the Clopper-Pearson 95% CI upper bound is 5.8%, so the zero-DR result is statistically meaningful despite the limited sample." | 998-doc 不再需要 CI 辩护，可简化或更新 CI |
| L129 | "551 SciERC documents and 50 DocRED documents" | "551 SciERC documents and 998 DocRED documents" |

### section5_runtime.tex

| 行号 | 当前内容 | 需更新为 |
|------|---------|---------|
| L13 | "a DocRED 50-document subset" | "the full DocRED 998-document dev set" |
| L13 | 整句需更新 Mistral 数据 "DR 7.99%, CF 1.27%" — 注意：当前值与 appendix 表格不完全匹配（表格 Mistral SciERC: DR 13.79%，DocRED: DR 21.37%），入稿时需统一 | 用 998-doc 数据统一 |

### main.tex

| 行号 | 当前内容 | 需更新为 |
|------|---------|---------|
| L82 | "a DocRED subset across three models" | "the full DocRED dev set (998 documents) across three models" |

### appendix_tcr.tex

| 行号 | 当前内容 | 需更新为 |
|------|---------|---------|
| L82 | "SciERC and DocRED 50-doc subset: DR→0% for calibrated models" | "SciERC and DocRED (998 docs): DR→0% for calibrated models" |

### 不需要更新的文件（仅引用 SciERC beam 或一般性描述）

- `abstract.tex` L5 — 仅提 SciERC zero violations
- `section1_introduction_draft.tex` L22, L29 — 仅提 SciERC
- `section7_conclusion_compressed.tex` L4 — 仅提 SciERC
- `section3_violation_landscape.tex` L9 — 一般性描述
- `section3_method_draft.tex` L15 — 一般性引用
- `section5_scierc_draft.tex` L110 — 仅提 SciERC beam
- `appendix_related_work.tex` — 引用他人工作，与我们的数据无关

---

## 2. Beam Appendix 表格 LaTeX 模板（带数据槽位）

```latex
\begin{table}[h]
\centering
\small
\caption{Beam search ($k{=}4$) vs.\ greedy decoding under full S1 constraints.
SciERC evaluated on full test set (551 documents); DocRED evaluated on the full 998-document dev set.
ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
\label{tab:beam-search}
\begin{tabular}{@{}llcccccc@{}}
\toprule
\textbf{Model / Dataset} & \textbf{Decoding} & ET & RV & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ \\
\midrule
\multirow{2}{*}{Qwen3-8B / SciERC (551)}
  & Greedy      & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.53} & 32.00 & 8.56 \\
\midrule
\multirow{2}{*}{Qwen3-8B / DocRED (998)}
  & Greedy      & 0 & 0 & \TBD{DR} & \TBD{CF} & \TBD{E-F1} & \TBD{R-F1} \\
  & Beam ($k{=}4$) & 0 & 0 & \TBD{DR} & \TBD{CF} & \TBD{E-F1} & \TBD{R-F1} \\
\midrule
\multirow{2}{*}{Llama-3.1-8B / SciERC (551)}
  & Greedy      & 0 & 0 & 0.08 & 6.56 & 23.49 & 2.54 \\
  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.93} & 25.04 & 3.33 \\
\midrule
\multirow{2}{*}{Llama-3.1-8B / DocRED (998)}
  & Greedy      & 0 & 0 & \TBD{DR} & \TBD{CF} & \TBD{E-F1} & \TBD{R-F1} \\
  & Beam ($k{=}4$) & 0 & 0 & \TBD{DR} & \TBD{CF} & \TBD{E-F1} & \TBD{R-F1} \\
\midrule
\multirow{2}{*}{Mistral-7B / SciERC (551)}
  & Greedy      & 0 & 0 & 13.40 & 1.27 & 27.46 & 3.67 \\
  & Beam ($k{=}4$) & 0 & 0 & 13.79 & \textbf{0.57} & 26.66 & 4.37 \\
\midrule
\multirow{2}{*}{Mistral-7B / DocRED (998)}
  & Greedy      & 0 & 0 & \TBD{DR} & \TBD{CF} & \TBD{E-F1} & \TBD{R-F1} \\
  & Beam ($k{=}4$) & 0 & 0 & \TBD{DR} & \TBD{CF} & \TBD{E-F1} & \TBD{R-F1} \\
\bottomrule
\end{tabular}
\end{table}
```

**注意事项：**
- `\TBD{...}` 需定义为 `\newcommand{\TBD}[1]{\textcolor{red}{#1}}` 或直接替换为实际数字
- SciERC 行数据不变（已有 551-doc 全量）
- DocRED greedy 数据也需更新：50-doc 的 greedy baseline 要换成 998-doc matched greedy
- ET 和 RV 列预期仍为 0（constraint 保证）

---

## 3. §5 beam 段落替换框架（section5_runtime.tex L11-14）

### 当前文本（L11-14）

```
Under greedy S1, the grammar-first fallback resolves DR↔CF conflicts one token at a time;
beam search (k=4) explores paths that satisfy both layers jointly and reduces DR and CF simultaneously.
With LoRA, beam S1 eliminates all four violation types on SciERC (551 docs) for both Qwen and Llama
(R-F1 44.23, 46.11; Table~\ref{tab:beam-search}).
Under zero-shot, beam reduces DR to 0% for calibrated models on SciERC (551 docs) and a DocRED
50-document subset, and CF substantially (9.90%→0.53% Qwen; 6.56%→0.93% Llama on SciERC);
Mistral remains a boundary condition (DR 7.99%, CF 1.27%) due to high baseline violations
(Appendix~\ref{app:beam-search}).
Total latency overhead is 1.54× (beam 1.32× + constraint 1.17×; Table~\ref{tab:beam-latency}).
```

### 替换框架

```latex
Under greedy S1, the grammar-first fallback resolves DR$\leftrightarrow$CF conflicts one token at a time; beam search ($k{=}4$) explores paths that satisfy both layers jointly and reduces DR and CF simultaneously.
With LoRA, beam S1 eliminates all four violation types on SciERC (551 docs) for both Qwen and Llama (R-F1 44.23, 46.11; Table~\ref{tab:beam-search}).
Under zero-shot, beam reduces DR to 0\% for calibrated models on both SciERC (551 docs) and the full DocRED dev set (998 docs), and CF substantially (9.90\%\,$\to$\,0.53\% Qwen; 6.56\%\,$\to$\,0.93\% Llama on SciERC; [DR_Q_G]→[DR_Q_B] Qwen, [DR_L_G]→[DR_L_B] Llama on DocRED); Mistral remains a boundary condition (DR [DR_M_B]\%, CF [CF_M_B]\%) due to high baseline violations (Appendix~\ref{app:beam-search}).
Total latency overhead is 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
```

**槽位说明：**
- `[DR_Q_G]` / `[DR_Q_B]` = Qwen DocRED 998 greedy/beam DR%
- `[DR_L_G]` / `[DR_L_B]` = Llama DocRED 998 greedy/beam DR%
- `[DR_M_B]` = Mistral DocRED 998 beam DR%
- `[CF_M_B]` = Mistral DocRED 998 beam CF%
- 如果 998-doc 结果仍然是 DR→0% for Qwen/Llama，叙事结构不变，只是统计力度从 50-doc 升级到 998-doc

---

## 4. Appendix Discussion 段落替换框架（appendix_beam_search.tex L57-67）

### 替换框架

```latex
\paragraph{Discussion.}
For calibrated models (Qwen3-8B, Llama-3.1-8B), beam search achieves DR=0\% across all four model-dataset combinations (both SciERC with 7 entity types, 551 documents, and DocRED with 96 relation types, 998 documents), regardless of schema complexity.
On SciERC, beam search eliminates DR for both Qwen (0.93\%\,$\to$\,0\%) and Llama (0.08\%\,$\to$\,0\%), and substantially reduces CF (Qwen: 9.90\%\,$\to$\,0.53\%; Llama: 6.56\%\,$\to$\,0.93\%).
On DocRED (998 documents), beam search eliminates DR for both Qwen ([DR_Q_G]\%\,$\to$\,[DR_Q_B]\%) and Llama ([DR_L_G]\%\,$\to$\,[DR_L_B]\%), with CF reductions of [CF_Q_reduction]\% and [CF_L_reduction]\% respectively.
[更新 R-F1 gain 描述，用 998-doc 数据]
The CF reduction is an indirect effect: beam search reduces constraint-fallback frequency by exploring alternative token sequences that satisfy both grammar and semantic masks simultaneously, avoiding the fallback-to-grammar path that produces cross-field inconsistencies under greedy decoding.

Mistral-7B-v0.3 constitutes a boundary condition on both datasets.
On SciERC (7 entity types), beam search does not reduce DR (13.4\%\,$\to$\,13.8\%), though CF drops by 55\% relative (1.27\%\,$\to$\,0.57\%) and R-F1 improves by $+$0.7\,pp; the unchanged DR confirms that all residual violations stem from entity type misclassification, not constraint-search failure.
On DocRED (96 relation types), beam search reduces DR by [M_DR_reduction]\% relative ([DR_M_G]\%\,$\to$\,[DR_M_B]\%): the more complex schema introduces constraint-search failures that beam exploration resolves, but the entity misclassification component remains.
This contrast reveals that beam search resolves constraint-search failure (where greedy decoding encounters $G(t) \cap S(t) = \emptyset$ conflicts) but cannot overcome fundamental model calibration limitations in entity typing.
```

---

## 5. Appendix 统计段落（L100-102）替换框架

```latex
Beam search on DocRED introduces [parse_fail_desc] (parse failure rate: [PF_beam]/998, [PF_beam_pct]\%) compared to greedy ([PF_greedy_pct]\%).
% 如果 DR 仍为 0：
With DR=0\% across 998 DocRED documents for both calibrated models, the result is now evaluated on the full dev set, eliminating the sample-size limitation of the prior 50-document evaluation.
% 如果 DR 不为 0：
% 需要根据实际数据重写
Combined with the sampling robustness results (Appendix~\ref{app:sampling}), these findings confirm that OntoCoDec's constraint enforcement is compatible with greedy, sampling, and beam search decoding without modification to the core constraint logic.
```

**关键决策点：**
- 如果 998-doc DR 仍然 =0%（Qwen/Llama），L101 的 Clopper-Pearson CI 辩护可以删除，改为更强的声明
- 如果 998-doc DR >0%（即 50-doc 的 0% 是小样本假象），需要重新定调整段叙事——从 "eliminates DR" 变为 "substantially reduces DR"，并波及 §5 和 abstract 中的 claim

---

## 6. 数据到手后执行 checklist

1. **提取指标**：从实验结果中提取 6 个 DocRED 998 数据点（3 models × {greedy, beam} × {DR, CF, E-F1, R-F1}）
2. **判断叙事**：Qwen/Llama DR 是否仍 =0%？
   - 是 → 叙事不变，只换数字和样本量
   - 否 → 需调整 abstract/intro/conclusion 中 "eliminates" 的 claim
3. **填充表格**：替换 appendix_beam_search.tex Table 1 的 6 行 DocRED 数据
4. **更新 caption**：L23 "50-document subsets" → "998-document dev set"
5. **更新 discussion**：L58-67 的百分比和 relative reduction
6. **更新 parse failure**：L100-101 的数据
7. **更新 §5**：section5_runtime.tex L13
8. **更新 limitations**：main.tex L82
9. **更新 TCR ref**：appendix_tcr.tex L82
10. **更新 beam latency paragraph**：appendix_beam_search.tex L129
11. **全文 grep "50.doc\|50-doc\|50 doc"** 确认无遗漏
12. **编译 LaTeX** 确认无错误
