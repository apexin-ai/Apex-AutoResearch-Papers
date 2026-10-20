# n=500 Paper Patch Plan

> 精确位置清单 + 预写文本
> 基于论文目录：`artifacts/_project/paper/`
> 生成日期：2026-05-14
> 硬约束：D054 (median only), D059 (within-imp d_z only), D060 (C8=partially_confirmed)

---

## A. 更新位置清单

### A1. Tables（含 n=50 数据的表格）

| # | 文件:行号 | 表格 ID | 内容 | 操作 |
|---|----------|---------|------|------|
| T1 | results.tex:10-23 | tab:aggregate-ii | DeepSeek aggregate Δ by strategy (caption L13: "n=50") | 替换 8 个数据单元格 + caption n 值 |
| T2 | results.tex:31-53 | tab:main-results | Per-phase II breakdown (caption L34: "50 problems") | 替换 24 个数据单元格 + caption n 值 |
| T3 | results.tex:83-98 | tab:llama-cross-arch | LLaMA cross-arch (caption L86: "n=49") | **D059 重构**：d_z 列为 imp-vs-rand → 替换为 within-imp d_z 或改为 Wilcoxon p + median_diff；若 LLaMA 不重跑则数值不变但列定义必须改 |
| T4 | results.tex:108-124 | tab:cohens-d | DS/QW paired d_z (within-imp, 合规) | 替换 16 个数据单元格（4行 × 4列） |
| T5 | appendix_moved.tex:30-43 | tab:cross-model | Cross-model Δ comparison | 替换 8 个数据单元格 |
| T6 | appendix_moved.tex:70-85 | tab:permutation | Permutation test results (caption L73: "n=49") | 替换 12 个数据单元格 + caption n 值 |
| T7 | appendix_moved.tex:103-123 | tab:discrimination-metrics-full | Gini/CV deltas | 替换 16 个数据单元格（若 C4 基于 n=500 重跑） |
| T8 | appendix_moved.tex:143-163 | tab:entropy-deltas | Entropy Δ𝓗 | 替换 8 个数据单元格（若 C4 基于 n=500 重跑） |

---

### A2. Quantitative Claims（文中引用具体数字的句子）

#### abstract.tex
| # | 行号 | 当前文本片段 | 替换说明 |
|---|------|-------------|---------|
| Q1 | 6 | `50 MATH-500 problems` | → `500 MATH-500 problems` |
| Q2 | 6 | `$s \in \{0.15, 0.20, 0.25, 0.30\}$` | 保留（sparsity levels 不变） |
| Q3 | 7 | `from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | → n=500 DeepSeek importance Δ (4值) |
| Q4 | 7 | `$d_z$ growing from $0.44$ (small) to $0.80$ (large)` | → n=500 within-imp d_z (合规 ✓) |
| Q5 | 7 | `$p < 0.005$ at all four sparsity levels` | → n=500 permutation p |
| Q6 | 8 | `7/8 conditions` | → n=500 random PASS/FAIL 计数 |
| Q7 | 8 | `$p{=}0.012$` `$d_z{=}{-}0.04$` | → **D059**: 删 d_z，改为 Wilcoxon p + median_diff |
| Q8 | 9 | `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` + `$7.196$ vs.\ $1.363$` | → n=500 crossover II 中位数 |
| Q9 | 10 | `$d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$` | → n=500 Qwen within-imp 统计 |
| Q10 | 10 | `$d_z$ ($0.19 \to 0.34$; $s{=}0.30$ Wilcoxon $p_{\text{Bonf}} = 0.029$)` | → **D059**: 删 imp-vs-rand d_z，保留 Wilcoxon p + median_diff |
| Q11 | 10 | `${\sim}$1/40 the absolute magnitude` | → 用 n=500 DeepSeek 重算 LLaMA/DeepSeek 比值 |

#### introduction.tex
| # | 行号 | 当前文本片段 | 替换说明 |
|---|------|-------------|---------|
| Q12 | 14 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \to 0.80$; Bonferroni-corrected $p < 0.005$)` | → 与 Q3/Q4/Q5 同步 |
| Q13 | 15 | `$d_z \geq 0.55$` | → n=500 Qwen within-imp d_z 下界 |
| Q14 | 15 | `$\sim$1/40 the magnitude` | → 与 Q11 同步 |
| Q15 | 16 | `7/8 conditions non-significant` | → 与 Q6 同步 |

#### methodology.tex
| # | 行号 | 当前文本片段 | 替换说明 |
|---|------|-------------|---------|
| Q16 | 10 | `50 problems stratified from MATH-500` | → `500 problems from MATH-500`（去 "stratified"，500≈全集） |
| Q17 | 18 | `mean/median ratios up to 43:1` | → n=500 mean/median ratio |
| Q18 | 22 | `All tests yield $p_{\text{Bonf}} < 0.005$ at every sparsity level.` | → n=500 p 值 |

#### results.tex（非表格部分）
| # | 行号 | 当前文本片段 | 替换说明 |
|---|------|-------------|---------|
| Q19 | 8 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification` | → n=500 Δ + 倍数 |
| Q20 | 8 | `$-0.02$ to $1.54$` | → n=500 random Δ 范围 |
| Q21 | 29 | `$69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$` | → n=500 G 值 |
| Q22 | 29 | `$\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$` | → n=500 high-phase II 范围 |
| Q23 | 29 | `$G \approx 0.9$--$1.7{\times}$` | → n=500 random G 范围 |
| Q24 | 58 | caption: `$69{\times}$ to $274{\times}$` | → 与 Q21 同步 |
| Q25 | 66 | `$0.032$ vs.\ $0.818$` + `$7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal` | → 与 Q8 同步 |
| Q26 | 71 | `$\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$` | → n=500 Qwen Δ |
| Q27 | 71 | `${\sim}1/5$ the magnitude` | → n=500 Qwen/DeepSeek 比值 |
| Q28 | 71 | `Spearman $\rho = 1.0$; gradient permutation $p = 0.043$` | → n=500 Qwen 统计 |
| Q29 | 71 | `$d_z{=}0.28$, CI includes zero` | → n=500 Qwen s015 d_z + CI（within-imp, 合规） |
| Q30 | 71 | `$d_z \geq 0.55$` | → n=500 Qwen d_z 下界 |
| Q31 | 77 | `$n{=}49$ paired problems` | → 确认 LLaMA 是否重跑；若不重跑保留 |
| Q32 | 79 | `$d_z$ ($0.19 \to 0.26 \to 0.29 \to 0.34$)` | → **D059 违规**：删除 imp-vs-rand d_z，改为 Wilcoxon p + median_diff |
| Q33 | 79 | `$p = 0.029$, $k{=}4$` | → 保留（Wilcoxon p 合规） |
| Q34 | 79 | `$\widetilde{\Delta} = 0.020$` + CI `$[0.002, 0.043]$` | → 保留/更新 |
| Q35 | 79 | `$d_z \in [1.00, 1.12]$` | → within-imp d_z，合规 ✓；若 LLaMA 重跑则更新 |
| Q36 | 79 | `$d_z \in [0.35, 0.45]$` | → **D059**: random d_z，删除改为定性描述 |
| Q37 | 81 | `${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen` | → 用 n=500 DS/QW 重算 |
| Q38 | 104 | `$p_{\text{Bonf}} < 0.005$` + `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` | → n=500 permutation 统计 |
| Q39 | 106 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` | → n=500 DS within-imp d_z |
| Q40 | 106 | `$d_z{=}0.28$, CI includes zero` + `$d_z \geq 0.55$` + `$d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$` | → n=500 QW d_z 全更新 |

#### discussion.tex
| # | 行号 | 当前文本片段 | 替换说明 |
|---|------|-------------|---------|
| Q41 | 5 | `$69$--$274{\times}$` | → 与 Q21 同步 |
| Q42 | 5 | `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` + `$7.196$ vs.\ $1.363$` | → 与 Q8 同步 |
| Q43 | 5 | `$G \approx 1$` | → 保留（定性描述） |
| Q44 | 11 | `${\sim}40{\times}$ smaller than DeepSeek, ${\sim}7{\times}$ smaller than Qwen` | → 与 Q37 同步 |
| Q45 | 11 | `$d_z \geq 1.0$` | → within-imp，合规 ✓；若 LLaMA 重跑则更新 |
| Q46 | 11 | `$d_z \in [0.35, 0.45]$` | → **D059**: random d_z，删除改为定性描述 + Wilcoxon p |

#### conclusion.tex
| # | 行号 | 当前文本片段 | 替换说明 |
|---|------|-------------|---------|
| Q47 | 4 | `$69{\times}$ to $274{\times}$` | → 与 Q21 同步 |
| Q48 | 4 | `$d_z$: $0.44 \to 0.80$` | → within-imp，与 Q39 同步 |
| Q49 | 4 | `7/8 conditions non-significant` | → 与 Q6 同步 |
| Q50 | 4 | `$d_z \geq 0.55$` | → 与 Q30 同步 |
| Q51 | 4 | `$\sim$1/40 the magnitude` | → 与 Q11 同步 |

#### analysis.tex
| # | 行号 | 当前文本片段 | 替换说明 |
|---|------|-------------|---------|
| Q52 | 4 | `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)` | → 若 C4 基于 n=500 重跑则更新 |
| Q53 | 6 | `$\Delta\mathcal{H} \in [-0.047, -0.040]$` | → 若 C4 重跑则更新 |
| Q54 | 6 | `$\Delta\mathcal{H} = +0.045$` | → 若 C4 重跑则更新 |

#### appendix.tex
| # | 行号 | 当前文本片段 | 替换说明 |
|---|------|-------------|---------|
| Q55 | 38 | `$G_{\times} = 58$--$241{\times}$` | → n=500 multiplicative null G 值 |

#### appendix_results.tex
| # | 行号 | 当前文本片段 | 替换说明 |
|---|------|-------------|---------|
| Q56 | 7 | `mean $\rho = -0.11$, $p = 0.926$` | → n=500 cross-model concordance |
| Q57 | 10 | `3/4 FAIL` + `4/4 FAIL` | → n=500 random PASS/FAIL |
| Q58 | 10 | `$p = 0.012$` + `$d_z = -0.04$` | → **D059**: 删 d_z，改为 Wilcoxon p + median_diff |

#### appendix_moved.tex（非表格部分）
| # | 行号 | 当前文本片段 | 替换说明 |
|---|------|-------------|---------|
| Q59 | 11 | `$0.032$ vs.\ $0.818$` + `$7.196$ vs.\ $1.363$` + `$5.3{\times}$` + `$3.9{\times}$, $5.4{\times}$, $5.3{\times}$, $3.6{\times}$` | → n=500 crossover 全部数值 |
| Q60 | 16 | caption `$5.3{\times}$` | → 与 Q59 同步 |
| Q61 | 26 | `Four of the 50 problems are excluded` + `$n{=}46$` + `$n{=}49$` | → n=500 有效 n |
| Q62 | 28 | `${\sim}1/5$ of DeepSeek's magnitude` | → 与 Q27 同步 |
| Q63 | 48 | caption: `one-fifth` | → 与 Q27 同步 |
| Q64 | 53 | `mean $\rho = -0.11$, $p = 0.926$`（重复 Q56） | → 与 Q56 同步 |
| Q65 | 56 | `$p = 0.012$` + `$d_z = -0.04$`（重复 Q58） | → 与 Q58 同步 |
| Q66 | 62+73 | `$n{=}49$` | → n=500 有效 n |
| Q67 | 68 | `$0.19 \to 0.69 \to 1.66 \to 6.70$` | → n=500 CI lower bounds |
| Q68 | 101 | Gini: `$0.030$--$0.081$` + `$0.010$--$0.020$` | → 若 C4 重跑则更新 |
| Q69 | 137-139 | DeepSeek `$[-0.047, -0.040]$` + Qwen `$+0.045$` + `$-0.007$` | → 若 C4 重跑则更新 |

#### appendix_disc_analysis.tex
| # | 行号 | 当前文本片段 | 替换说明 |
|---|------|-------------|---------|
| Q70 | 4 | `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$` | → 若 C4 重跑则更新 |
| Q71 | 11 | `$\widetilde{\mathrm{II}}_{\text{high}} < 0.06$` + `$0.105$` | → n=500 high-phase II |
| Q72 | 14 | `7/8` + `$p{=}0.012$` + `$d_z{=}{-}0.04$` | → **D059**: 删 d_z，与 Q7 同步 |
| Q73 | 45 | `$n{=}49$` + `$n{=}46$` | → n=500 有效 n |
| Q74 | 46 | `${\sim}1.6{:}1$` + `median_diff=14.59` | → n=500 偏度统计 |
| Q75 | 47 | CI 值: `$[0.19,0.62]$, $[0.69,1.49]$, $[1.66,6.64]$, $[6.70,16.29]$` | → n=500 permutation CI |
| Q76 | 49 | `$p{=}0.012$` + `$d_z{=}{-}0.04$` | → **D059**: 删 d_z，与 Q7 同步 |
| Q77 | 57 | `$3.8{\times} \to 4.8{\times} \to 2.0{\times}$` | → n=500 Δ growth rate |

---

### A3. D059 违规（imp-vs-rand 或 random 使用 d_z 的位置）

共 **10 处**需修改，改为 Wilcoxon p + median_diff：

| # | 文件:行号 | 当前内容 | 违规类型 |
|---|----------|---------|---------|
| D1 | abstract.tex:8 | `$d_z{=}{-}0.04$` | random d_z |
| D2 | abstract.tex:10 | `$d_z$ ($0.19 \to 0.34$` | imp-vs-rand d_z (LLaMA) |
| D3 | results.tex:79 | `paired $d_z$ ($0.19 \to 0.26 \to 0.29 \to 0.34$)` | imp-vs-rand d_z (LLaMA) |
| D4 | results.tex:79 | `$d_z \in [0.35, 0.45]$` | random d_z (LLaMA) |
| D5 | results.tex:86-97 | Table 3 d_z 列 + caption `$d_z$: paired Cohen's $d$ for importance vs.\ random` | imp-vs-rand d_z (整列) |
| D6 | discussion.tex:11 | `$d_z \in [0.35, 0.45]$` | random d_z (LLaMA) |
| D7 | appendix_results.tex:10 | `$d_z = -0.04$` | random d_z |
| D8 | appendix_moved.tex:56 | `$d_z = -0.04$` | random d_z |
| D9 | appendix_disc_analysis.tex:14 | `$d_z{=}{-}0.04$` | random d_z |
| D10 | appendix_disc_analysis.tex:49 | `$d_z{=}{-}0.04$` | random d_z |

**修改方案**：
- D1/D7/D8/D9/D10：删除 `$d_z{=}{-}0.04$`，替换为 `negligible median difference ($\widetilde{\Delta} = \text{X}$)`
- D2/D3：删除 imp-vs-rand d_z 序列，改为 `Wilcoxon signed-rank tests with median paired difference $\widetilde{\Delta}$ increasing from X to Y`
- D4/D6：删除 random d_z，改为定性描述 `random eviction also shows a non-trivial phase gradient (Wilcoxon $p < \text{X}$)`
- D5：Table 3 重构——d_z 列替换为 within-importance d_z（low−high），或移除 d_z 列完全改为 Wilcoxon p + median_diff 结构

---

### A4. C8 partially_confirmed 限定语（LLaMA 相关断言检查）

| # | 文件:行号 | 当前文本 | 状态 |
|---|----------|---------|------|
| C1 | abstract.tex:10 | `suggests cross-architecture generalization, though at...` | ✅ 合规 |
| C2 | introduction.tex:15 | `partially extends to a distinct architecture` | ✅ 合规 |
| C3 | results.tex:79 | `The qualitative pattern replicates` | ⚠️ **borderline** — 建议改为 `The qualitative pattern is directionally consistent` |
| C4 | results.tex:81 | `The directional pattern...is qualitatively consistent across all three models` | ✅ 合规（后半句有 `substantially weaker` 限定） |
| C5 | discussion.tex:11 | `provides partial support for the qualitative pattern` | ✅ 合规 |
| C6 | conclusion.tex:4 | `partially extends cross-architecture` | ✅ 合规 |
| C7 | limitations.tex:2 | `partially extends the findings beyond the Qwen2 architecture` | ✅ 合规 |
| C8 | appendix_disc_analysis.tex:33 | `provides partial support` | ✅ 合规 |

**唯一需修改**：results.tex:79 `The qualitative pattern replicates` → `The qualitative pattern is directionally consistent`

---

### A5. C5b Future Work 位置

当前论文**没有独立的 Future Work section**。相关 mitigation 讨论分散在：

| # | 文件:行号 | 当前内容 | 说明 |
|---|----------|---------|------|
| FW1 | discussion.tex:8 | `A phase-aware compression budget...could mitigate...` | mitigation 作为 implication 讨论 |
| FW2 | conclusion.tex:5 | `These findings motivate phase-aware sparsity allocation...` | 一句话 motivation |

**建议插入点**：conclusion.tex:5 之后（line 5 与 `\end{document}` 之间），新增 Future Work 段落。或者在 discussion.tex:8 段落末尾追加 pilot 实验结果。

具体推荐：**discussion.tex:8 段落末尾**追加 B2 文本（与 deployment implications 自然衔接），同时在 conclusion.tex:5 追加一句指向 discussion 的引用。

---

### A6. Figures（数据源与重生成需求）

| # | 文件名 | 引用位置 | 数据源（n=50） | n=500 操作 |
|---|--------|---------|---------------|-----------|
| F1 | fig1_dose_response.pdf | results.tex:57, caption:58 | G values: imp=[5.6, 69.2, 103.1, 222.4, 274.2, 273.6], rand=[1.1, 0.95, 1.67, 1.61]. Bootstrap B=10000 CI in log space. 生成信息: `_project/chart/fig1_dose_response_bf16.txt` | 用 n=500 experiment_summary_table.json 重算 G 值 → 重新生成。Caption Q24 需同步更新 |
| F2 | fig3_crossover.pdf | appendix_moved.tex:15, caption:16 | imp_high=0.032, rand_high=0.818; imp_mid=1.118, rand_mid=0.932; imp_low=7.196, rand_low=1.363. 生成信息: `_project/chart/fig3_crossover_bf16.txt` | 用 n=500 s=0.25 per-phase median II → 重新生成。Caption Q60 需同步更新 |
| F3 | fig4_bootstrap.pdf | appendix_moved.tex:89, caption:90 | DS d_z: 0.44/0.52/0.68/0.80. QW d_z: 0.28/0.55/0.89/1.02. 生成信息: `_project/chart/fig4_forest_paired_dz.txt` | 用 n=500 paired d_z + permutation CI → 重新生成 |
| F4 | fig5_crossmodel.pdf | appendix_moved.tex:47, caption:48 | DS Δ=[0.351, 1.136, 4.017, 9.954], QW Δ=[0.062, 0.286, 1.155, 2.594]. 生成信息: `_project/chart/fig5_crossmodel_bf16.txt` | 用 n=500 DS/QW paired median diffs → 重新生成。Caption Q63 需同步更新 |

**注意**：所有 figure 生成脚本为服务器端执行（draw-paper-figure skill），无本地 .py 脚本。生成参数记录在 `_project/chart/` 目录下的 info 文件中。

---

## B. 预写文本

### B1. Qwen Caveat（imp-vs-rand 不显著时使用）

> **插入位置**：results.tex:71 之后（§5.4 Cross-Model Replication 末尾，Table/Figure 引用之前）

```latex
While Qwen2.5-7B-Instruct exhibits a significant within-importance severity gradient at $s \geq 0.20$, the importance-versus-random contrast is attenuated relative to DeepSeek: the median paired difference remains modest across sparsity levels, and the permutation test reaches significance only at $s \geq 0.25$. This attenuation likely reflects Qwen's lower compound interaction baseline under importance-based eviction at low sparsity---when the absolute severity is small, the strategy-dependent amplification has less room to manifest, even though the within-strategy phase gradient is robust.
```

### B2. C5b Future Work（Phase-Aware Mitigation Pilot）

> **插入位置**：discussion.tex:8 段落末尾（`Extended discussion in Appendix~\ref{app:extended-discussion}.` 之前），或 conclusion.tex:5 之前新起段落

```latex
A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. The oracle recovery---measured as the fraction of compound interaction eliminated by phase-aware allocation---reached only 18\%, well below a pre-registered 30\% gate for claiming practical mitigation. This suggests that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient, and that effective mitigation may require joint optimization of both budget allocation and eviction strategy selection across phases---a promising but open direction for future work.
```

### B3. Mid-Phase Null Rate（Qwen Mid-Phase 统计功效限制）

> **插入位置**：results.tex:71 附近（Qwen 结果讨论中），或 appendix_moved.tex:26 之后（Cross-Model Replication Details）

```latex
On Qwen2.5-7B-Instruct, approximately 45\% of problems yield near-zero Interaction Index in the mid-sparsity phase, where attention patterns exhibit insufficient variation to produce measurable compound interaction. This elevated null rate reduces the effective sample size for mid-phase comparisons and limits statistical power for detecting phase gradients that span the mid-phase boundary; our primary analysis therefore focuses on the low--high phase contrast, which is unaffected by this limitation.
```

---

## C. 按优先级排序的执行清单

### 优先级 1（n=500 数据到手后立即执行）
1. 替换 T1, T2, T5, T6 表格数据（DeepSeek/Qwen 核心表格）
2. 更新 Q1-Q5, Q12, Q15-Q18, Q19-Q30, Q38-Q40, Q47-Q50, Q55-Q67, Q71-Q77（数值替换）
3. 重新生成 F1-F4 图表

### 优先级 2（D059 合规修复，不依赖 n=500 数据）
4. 修复 D1-D10 全部 D059 违规
5. 重构 T3 (Table 3) 列定义

### 优先级 3（文本修改）
6. 修复 C3（results.tex:79 LLaMA 限定语）
7. 插入 B1（Qwen caveat，视 n=500 结果决定是否使用）
8. 插入 B2（C5b future work）
9. 插入 B3（mid-phase null rate）

### 优先级 4（条件性更新）
10. T4 (tab:cohens-d) — n=500 数据
11. T7, T8 — 仅当 C4 entropy 分析基于 n=500 重跑时更新
12. Q37, Q44, Q51 — LLaMA 倍数比（依赖 n=500 DS/QW 数据）
13. 确认 LLaMA 是否重跑 n=500（影响 T3 数据、Q31-Q36）
