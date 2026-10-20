# n=500 论文更新最终执行计划

> **目标**：n=500 实验数据就绪后，系统性更新论文所有数值、图表、措辞，同时修复 W1-W5 + s015 升级 + D059 违规。
> **论文目录**：`artifacts/_project/paper/`
> **硬约束**：D054 (median only), D059 (within-imp d_z only), D060 (C8=partially_confirmed), B=10,000 统一, onset threshold = s≥0.15
> **禁止修改**：paper_framing.md
> **生成日期**：2026-05-14

---

## Phase 0: Sync

```bash
# 本地 → 远程同步（硬前置，不可跳过）
cd artifacts/_project && bash sync_paper_to_remote.sh
# 或手动：
git add -A && git commit -m "pre-n500 sync" && git push
# 远程：cd /root/autodl-tmp/pacs && git pull
```

**验证**：远程 `git log -1` 与本地一致。

---

## Phase 1: 分析 Pipeline

### 1.1 执行统一分析脚本

```bash
# 在服务器上执行
cd /root/autodl-tmp/pacs
python analyze_n500_unified.py --model all --latex --csv --bootstrap 10000
```

**脚本已就绪**：`analyze_n500_unified.py` 在 `/root/autodl-tmp/pacs/` 下，dry-run 通过。

### 1.2 预期输出

| 输出文件 | 内容 |
|----------|------|
| `analysis_output/n500_unified.json` | 所有 condition 的 median_diff, CI, d_z, G, p-values |
| `analysis_output/n500_unified.csv` | 同上 CSV 格式 |
| `analysis_output/n500_latex_rows.tex` | 可直接粘贴的 LaTeX 表格行 |
| `analysis_output/n500_permutation.json` | 配对置换检验结果 (B=10,000) |
| `analysis_output/n500_cohens_d.json` | Within-importance paired d_z + CI |

### 1.3 关键验证

```python
# 确认所有数值为 median（D054）
# 确认 B=10,000（W4）
# 确认 d_z 仅报 within-importance（D059）
# 确认 Qwen s015 CI 不跨零（s015 升级前提）
```

---

## Phase 2: 论文 Patch（按优先级）

### ═══════════════════════════════════════
### 2a. 数据替换（Priority 1 — 最大工作量）
### ═══════════════════════════════════════

#### Table 1: tab:aggregate-ii
**文件**: `results.tex:10-23`

```latex
% 替换 Line 13 caption:
\caption{... ($n{=}\placeholder{N\_DS}$ MATH-500 problems).}
% 替换 Line 19-20 数据行:
Importance & \placeholder{DS_IMP_S015} & \placeholder{DS_IMP_S020} & \placeholder{DS_IMP_S025} & \placeholder{DS_IMP_S030} \\
Random     & \placeholder{DS_RAND_S015} & \placeholder{DS_RAND_S020} & \placeholder{DS_RAND_S025} & \placeholder{DS_RAND_S030} \\
```

#### Table 2: tab:main-results
**文件**: `results.tex:31-53`

```latex
% 替换 Line 34 caption:
\caption{... medians across \placeholder{N\_DS} problems. ...}
% 替换 Lines 40-50: 全部 8 行数据（每行 5 个数值 + G）
% 格式: s & Strategy & II_high & II_mid & II_low & Δ & G
0.15 & Importance & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} & $\mathbf{\placeholder{}}$ \\
0.15 & Random     & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
% ... 同样替换 s=0.20, 0.25, 0.30
```

#### Table 4: tab:cohens-d
**文件**: `results.tex:108-124`

```latex
% 替换 Lines 117-120: 4 行 × 4 列数据
% DS d_z, DS Δ̃[CI], QW d_z, QW Δ̃[CI]
0.15 & \placeholder{DS_DZ_015} & \placeholder{DS_DELTA_015}\; $[\placeholder{},\placeholder{}]$ & \placeholder{QW_DZ_015} & \placeholder{QW_DELTA_015}\; $[\placeholder{},\placeholder{}]$ \\
% ... 同样替换 s=0.20, 0.25, 0.30
% Line 122 脚注：若 Qwen s015 CI 不跨零，删除 \textsuperscript{ns} 标记
```

**s015 升级关键**：若 n=500 Qwen s015 CI 不跨零（memory.md 已确认 p<0.0001），则：
- 删除 Line 122 的 `\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \geq 0.20$.`
- 替换为：`All effect sizes significant after Bonferroni correction.` 或直接删除脚注

#### Table 5: tab:cross-model
**文件**: `appendix_moved.tex:30-43`

```latex
% 替换 Lines 39-40:
DeepSeek-R1-Distill-Qwen-7B & \placeholder{DS_015} & \placeholder{DS_020} & \placeholder{DS_025} & \placeholder{DS_030} \\
Qwen2.5-7B-Instruct         & \placeholder{QW_015} & \placeholder{QW_020} & \placeholder{QW_025} & \placeholder{QW_030} \\
```

#### Table 6: tab:permutation
**文件**: `appendix_moved.tex:70-85`

```latex
% 替换 Line 73 caption: n=\placeholder{N_DS}
% 替换 Lines 79-82: 4 行 (observed Δ̃, 95% CI, p_Bonf)
0.15 & \placeholder{PERM_015} & $[\placeholder{},\; \placeholder{}]$ & \placeholder{P_015} \\
0.20 & \placeholder{PERM_020} & $[\placeholder{},\; \placeholder{}]$ & \placeholder{P_020} \\
0.25 & \placeholder{PERM_025} & $[\placeholder{},\; \placeholder{}]$ & \placeholder{P_025} \\
0.30 & \placeholder{PERM_030} & $[\placeholder{},\; \placeholder{}]$ & \placeholder{P_030} \\
```

#### Table 7: tab:discrimination-metrics-full（条件性）
**文件**: `appendix_moved.tex:103-123`
**条件**：仅当 C4 entropy 分析基于 n=500 重跑时更新 16 个单元格。若 C4 保持 n=50 数据，需在 caption 标注 "based on n=50 subset"。

#### Table 8: tab:entropy-deltas（条件性）
**文件**: `appendix_moved.tex:143-163`
**条件**：同 Table 7。

---

#### 定量声明替换（77 处）

以下按文件分组，每处给出精确行号、当前文本、替换模板。

##### abstract.tex

| ID | 行 | 当前文本 | 替换 |
|----|---|---------|------|
| Q1 | 6 | `50 MATH-500 problems` | `\placeholder{N} MATH-500 problems` |
| Q3 | 7 | `from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | `from $\placeholder{}$ at $s{=}0.15$ to $\placeholder{}$ at $s{=}0.30$` |
| Q4 | 7 | `$d_z$ growing from $0.44$ (small) to $0.80$ (large)` | `$d_z$ growing from $\placeholder{}$ to $\placeholder{}$` |
| Q5 | 7 | `$p < 0.005$ at all four sparsity levels` | 用 n=500 p 值更新 |
| Q6 | 8 | `7/8 conditions` | `\placeholder{X}/8 conditions` |
| Q7 | 8 | `$p{=}0.012$` `$d_z{=}{-}0.04$` | **D059 修复**→见 §2e |
| Q8 | 9 | `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` + `$7.196$ vs.\ $1.363$` | 用 n=500 crossover 值 |
| Q9 | 10 | `$d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$` | 用 n=500 Qwen 统计 |
| Q10 | 10 | `$d_z$ ($0.19 \to 0.34$; $s{=}0.30$ Wilcoxon $p_{\text{Bonf}} = 0.029$)` | **D059 修复**→见 §2e |
| Q11 | 10 | `${\sim}$1/40 the absolute magnitude` | 用 n=500 DS/QW 重算 LLaMA 比值 |

##### introduction.tex

| ID | 行 | 当前文本 | 替换 |
|----|---|---------|------|
| Q12 | 14 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \to 0.80$; Bonferroni-corrected $p < 0.005$)` | 与 Q3/Q4/Q5 同步 |
| Q13 | 15 | `$d_z \geq 0.55$` | n=500 Qwen d_z 下界 |
| Q14 | 15 | `$\sim$1/40 the magnitude` | 与 Q11 同步 |
| Q15 | 16 | `7/8 conditions non-significant` | 与 Q6 同步 |

##### methodology.tex

| ID | 行 | 当前文本 | 替换 |
|----|---|---------|------|
| Q16 | 10 | `50 problems stratified from MATH-500` | `500 problems from MATH-500`（去 "stratified"，500≈全集） |
| Q17 | 18 | `mean/median ratios up to 43:1` | n=500 mean/median ratio |
| Q18 | 22 | `All tests yield $p_{\text{Bonf}} < 0.005$ at every sparsity level.` | n=500 p 值 |

##### results.tex（非表格部分）

| ID | 行 | 当前文本 | 替换 |
|----|---|---------|------|
| Q19 | 8 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification` | n=500 Δ + 倍数 |
| Q20 | 8 | `$-0.02$ to $1.54$` | n=500 random Δ 范围 |
| Q21 | 29 | `$69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$` | n=500 G 值 |
| Q22 | 29 | `$\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$` | n=500 high-phase II 范围 |
| Q23 | 29 | `$G \approx 0.9$--$1.7{\times}$` | n=500 random G 范围 |
| Q24 | 58 | caption: `$69{\times}$ to $274{\times}$` | 与 Q21 同步 |
| Q25 | 66 | `$0.032$ vs.\ $0.818$` + `$7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal` | n=500 crossover |
| Q26 | 71 | `$\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$` | n=500 Qwen Δ |
| Q27 | 71 | `${\sim}1/5$ the magnitude` | n=500 Qwen/DeepSeek 比值 |
| Q28 | 71 | `Spearman $\rho = 1.0$; gradient permutation $p = 0.043$` | n=500 Qwen 统计 |
| Q29 | 71 | `$d_z{=}0.28$, CI includes zero` | **s015 升级**→见 §2d |
| Q30 | 71 | `$d_z \geq 0.55$` | n=500 Qwen d_z 下界（s015 升级后可能变为 `$d_z \geq \placeholder{}$ at all sparsity levels`） |
| Q31 | 77 | `$n{=}49$ paired problems` | 确认 LLaMA 是否重跑 n=500 |
| Q32 | 79 | `$d_z$ ($0.19 \to 0.26 \to 0.29 \to 0.34$)` | **D059 修复**→见 §2e |
| Q33 | 79 | `$p = 0.029$, $k{=}4$` | 保留（Wilcoxon p 合规） |
| Q34 | 79 | `$\widetilde{\Delta} = 0.020$` + CI `$[0.002, 0.043]$` | 保留/更新（若 LLaMA 重跑） |
| Q35 | 79 | `$d_z \in [1.00, 1.12]$` | within-imp d_z，合规；若 LLaMA 重跑则更新 |
| Q36 | 79 | `$d_z \in [0.35, 0.45]$` | **D059 修复**→见 §2e |
| Q37 | 81 | `${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen` | 用 n=500 DS/QW 重算 |
| Q38 | 104 | `$p_{\text{Bonf}} < 0.005$` + `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` | n=500 permutation |
| Q39 | 106 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` | n=500 DS within-imp d_z |
| Q40 | 106 | `$d_z{=}0.28$, CI includes zero` + `$d_z \geq 0.55$` + `$d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$` | **s015 升级** + n=500 QW d_z |

##### discussion.tex

| ID | 行 | 当前文本 | 替换 |
|----|---|---------|------|
| Q41 | 5 | `$69$--$274{\times}$` | 与 Q21 同步 |
| Q42 | 5 | `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` + `$7.196$ vs.\ $1.363$` | 与 Q8 同步 |
| Q44 | 11 | `${\sim}40{\times}$ smaller than DeepSeek, ${\sim}7{\times}$ smaller than Qwen` | 与 Q37 同步 |
| Q45 | 11 | `$d_z \geq 1.0$` | within-imp 合规；若 LLaMA 重跑则更新 |
| Q46 | 11 | `$d_z \in [0.35, 0.45]$` | **D059 修复**→见 §2e |

##### conclusion.tex

| ID | 行 | 当前文本 | 替换 |
|----|---|---------|------|
| Q47 | 4 | `$69{\times}$ to $274{\times}$` | 与 Q21 同步 |
| Q48 | 4 | `$d_z$: $0.44 \to 0.80$` | 与 Q39 同步 |
| Q49 | 4 | `7/8 conditions non-significant` | 与 Q6 同步 |
| Q50 | 4 | `$d_z \geq 0.55$` | 与 Q30 同步 |
| Q51 | 4 | `$\sim$1/40 the magnitude` | 与 Q11 同步 |

##### analysis.tex

| ID | 行 | 当前文本 | 替换 | 条件 |
|----|---|---------|------|------|
| Q52 | 4 | `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)` | n=500 Gini Δ | 仅当 C4 重跑 |
| Q53 | 6 | `$\Delta\mathcal{H} \in [-0.047, -0.040]$` | n=500 entropy Δ | 仅当 C4 重跑 |
| Q54 | 6 | `$\Delta\mathcal{H} = +0.045$` | n=500 Qwen s025 | 仅当 C4 重跑 |

##### appendix.tex

| ID | 行 | 当前文本 | 替换 |
|----|---|---------|------|
| Q55 | 38 | `$G_{\times} = 58$--$241{\times}$` | n=500 multiplicative null G |

##### appendix_results.tex

| ID | 行 | 当前文本 | 替换 |
|----|---|---------|------|
| Q56 | 7 | `mean $\rho = -0.11$, $p = 0.926$` | **NEW-3**: 改为 `median $\rho$` 或 `$\bar{\rho}$` 标记（D054 边界） + n=500 值 |
| Q57 | 10 | `3/4 FAIL` + `4/4 FAIL` | n=500 random PASS/FAIL |
| Q58 | 10 | `$p = 0.012$` + `$d_z = -0.04$` | **D059 修复**→见 §2e |

##### appendix_moved.tex（非表格部分）

| ID | 行 | 当前文本 | 替换 |
|----|---|---------|------|
| Q59 | 11 | `$0.032$ vs.\ $0.818$` + `$7.196$ vs.\ $1.363$` + `$5.3{\times}$` + `$3.9{\times}$, $5.4{\times}$, $5.3{\times}$, $3.6{\times}$` | n=500 crossover 全部 |
| Q60 | 16 | caption `$5.3{\times}$` | 与 Q59 同步 |
| Q61 | 26 | `Four of the 50 problems are excluded` + `$n{=}46$` + `$n{=}49$` | n=500 有效 n |
| Q62 | 28 | `${\sim}1/5$ of DeepSeek's magnitude` | 与 Q27 同步 |
| Q63 | 48 | caption: `one-fifth` | 与 Q27 同步 |
| Q64 | 53 | `mean $\rho = -0.11$, $p = 0.926$` | **NEW-3** + 与 Q56 同步 |
| Q65 | 56 | `$p = 0.012$` + `$d_z = -0.04$` | **D059 修复**→见 §2e |
| Q66 | 62+73 | `$n{=}49$` | n=500 有效 n |
| Q67 | 68 | `$0.19 \to 0.69 \to 1.66 \to 6.70$` | n=500 CI lower bounds |
| Q68 | 101 | Gini: `$0.030$--$0.081$` + `$0.010$--$0.020$` | 仅当 C4 重跑 |
| Q69 | 137-139 | DeepSeek `$[-0.047, -0.040]$` + Qwen `$+0.045$` + `$-0.007$` | 仅当 C4 重跑 |

##### appendix_disc_analysis.tex

| ID | 行 | 当前文本 | 替换 |
|----|---|---------|------|
| Q70 | 4 | `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$` | 仅当 C4 重跑 |
| Q71 | 11 | `$\widetilde{\mathrm{II}}_{\text{high}} < 0.06$` + `$0.105$` | n=500 high-phase II |
| Q72 | 14 | `7/8` + `$p{=}0.012$` + `$d_z{=}{-}0.04$` | **D059 修复** + 与 Q6/Q7 同步 |
| Q73 | 45 | `$n{=}49$` + `$n{=}46$` | n=500 有效 n |
| Q74 | 46 | `${\sim}1.6{:}1$` + `median_diff=14.59` | n=500 偏度统计 |
| Q75 | 47 | CI: `$[0.19,0.62]$, $[0.69,1.49]$, $[1.66,6.64]$, $[6.70,16.29]$` | n=500 permutation CI |
| Q76 | 49 | `$p{=}0.012$` + `$d_z{=}{-}0.04$` | **D059 修复**→见 §2e |
| Q77 | 57 | `$3.8{\times} \to 4.8{\times} \to 2.0{\times}$` | n=500 Δ growth rate |

---

### ═══════════════════════════════════════
### 2b. W2: §5.5 Selective Reporting 修复（Priority 2）
### ═══════════════════════════════════════

**问题**：LLaMA §5.5 当前只报 s030 的 Wilcoxon p，不报其他 3 个 sparsity level 的 CI + Bonferroni Wilcoxon，构成 selective reporting。

**位置**：`results.tex:79`（§5.5 Cross-Architecture 第二段）

**当前文本**（Line 79）：
```
The qualitative pattern replicates: importance-based eviction produces systematically larger 
phase-dependent severity than random eviction, with monotonically increasing paired $d_z$ 
($0.19 \to 0.26 \to 0.29 \to 0.34$). At $s{=}0.30$, the Wilcoxon test reaches significance 
after Bonferroni correction ($p = 0.029$, $k{=}4$). At $s{=}0.15$, the median difference 
CI $[0.002, 0.043]$ excludes zero despite the small absolute magnitude 
($\widetilde{\Delta} = 0.020$).
```

**替换为**（预写 LaTeX，D059 合规 + W2 修复）：

```latex
The directional pattern is consistent: importance-based eviction produces systematically larger phase-dependent severity than random eviction at all four sparsity levels. Table~\ref{tab:llama-cross-arch} reports the Wilcoxon signed-rank test with Bonferroni correction ($k{=}4$) and median paired differences with bootstrap 95\% CIs ($B{=}10{,}000$) for each level. At $s{=}0.30$, the test reaches significance ($p_{\text{Bonf}} = \placeholder{LLAMA\_P030}$, $\widetilde{\Delta} = \placeholder{LLAMA\_DELTA030}$\; $[\placeholder{CI}]$); at $s{=}0.15$, the median difference is small but the CI excludes zero ($\widetilde{\Delta} = \placeholder{LLAMA\_DELTA015}$\; $[\placeholder{CI}]$, $p_{\text{Bonf}} = \placeholder{LLAMA\_P015}$). The remaining levels ($s \in \{0.20, 0.25\}$) show intermediate effects ($p_{\text{Bonf}} = \placeholder{}, \placeholder{}$).
```

**Table 3 重构**（`results.tex:83-98`）：

当前 Table 3 caption (Line 86) 包含 `$d_z$: paired Cohen's $d$ for importance vs.\ random severity`——这是 D059 违规（imp-vs-rand d_z）。

**替换 caption**：
```latex
\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\widetilde{\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}\placeholder{N\_LLAMA}$ paired problems.}
```

**替换表头 + 数据**（删除 d_z 列，改为 Wilcoxon p + median_diff 结构）：
```latex
\begin{tabular}{@{}lcc@{}}
\toprule
$s$ & $\widetilde{\Delta}$\; [95\% CI] & $p_{\text{Bonf}}$ \\
\midrule
0.15 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & \placeholder{} \\
0.20 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & \placeholder{} \\
0.25 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & \placeholder{} \\
0.30 & \placeholder{}\; $[\placeholder{}, \placeholder{}]$ & $\mathbf{\placeholder{}}$ \\
\bottomrule
\end{tabular}
```

---

### ═══════════════════════════════════════
### 2c. W5: Qwen Null Rate 披露（Priority 2）
### ═══════════════════════════════════════

**问题**：Qwen mid-phase 45.2% null rate（II=0）未在论文中披露。

#### 2c-i. 主文 Caveat

**插入位置**：`results.tex:71` 末尾（`Full cross-model tables...` 句之前）

**预写 LaTeX**：
```latex
A caveat applies to mid-phase comparisons: on Qwen2.5-7B-Instruct, approximately \placeholder{NULL\_PCT}\% of problems yield near-zero Interaction Index in the mid-sparsity phase, where attention patterns exhibit insufficient variation to produce measurable compound interaction. This elevated null rate reduces the effective sample size for mid-phase comparisons; our primary cross-model analysis therefore focuses on the low--high phase contrast ($\Delta$), which is unaffected by this limitation. Per-phase effective sample sizes are reported in Appendix~\ref{app:qwen-null-rate}.
```

#### 2c-ii. Appendix Per-Phase Effective n 表

**插入位置**：`appendix_moved.tex:26` 之后（Cross-Model Replication Details, Qwen exclusion 段后）

**预写 LaTeX**：
```latex
\paragraph{Per-phase effective sample size.}
\label{app:qwen-null-rate}
Table~\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\placeholder{NULL\_PCT}\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\Delta$) used in the primary analysis.

\begin{table}[t]
\centering
\small
\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\text{total}} = \placeholder{N\_QW}$).}
\label{tab:qwen-effective-n}
\begin{tabular}{@{}lcccc@{}}
\toprule
Phase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
\midrule
High & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
Mid  & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
Low  & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
\bottomrule
\end{tabular}
\end{table}
```

---

### ═══════════════════════════════════════
### 2d. s015 升级：删除 "marginal" 限定语（Priority 2）
### ═══════════════════════════════════════

**背景**：n=500 Qwen s015 CI [0.0492, 0.0925] 不跨零，p<0.0001 → onset threshold 统一为 s≥0.15。删除所有 "marginal at s=0.15" / "borderline" / "at the boundary" 限定语。

**搜索目标**：所有 .tex 中与 s015 "marginal" / "ns" / "CI includes zero" 相关的措辞。

| # | 文件:行 | 当前文本 | 替换 |
|---|--------|---------|------|
| S1 | results.tex:71 | `The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \geq 0.20$ ($d_z \geq 0.55$).` | `The effect is significant at all sparsity levels, with $d_z$ increasing from $\placeholder{QW\_DZ\_015}$ at $s{=}0.15$ to $\placeholder{QW\_DZ\_030}$ at $s{=}0.30$.` |
| S2 | results.tex:106 | `For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \geq 0.20$ ($d_z \geq 0.55$).` | `For Qwen, effect sizes are significant at all four sparsity levels ($d_z$: $\placeholder{QW\_DZ\_015} \to \placeholder{QW\_DZ\_030}$).` |
| S3 | results.tex:117 | `\textsuperscript{ns}` 标记 | 删除 |
| S4 | results.tex:122 | `\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \geq 0.20$.` | 删除整行脚注（或改为 `All levels significant after Bonferroni correction.`） |
| S5 | abstract.tex:10 | `at $s \geq 0.20$ ($d_z \geq 0.55$` | `at all sparsity levels ($d_z \geq \placeholder{QW\_DZ\_015}$` |
| S6 | introduction.tex:15 | `($d_z \geq 0.55$)` | `($d_z \geq \placeholder{QW\_DZ\_015}$)` |
| S7 | conclusion.tex:4 | `at $s \geq 0.20$ ($d_z \geq 0.55$)` | `at all sparsity levels ($d_z \geq \placeholder{QW\_DZ\_015}$)` |

---

### ═══════════════════════════════════════
### 2e. D059 违规清理（Priority 2）
### ═══════════════════════════════════════

**规则**：d_z 仅报 within-importance (low−high)。所有 imp-vs-rand d_z 和 random d_z 必须删除，替换为 Wilcoxon p + median_diff。

共 **10 处**：

| # | 文件:行 | 当前 | 类型 | 替换 |
|---|--------|------|------|------|
| D1 | abstract.tex:8 | `$d_z{=}{-}0.04$` | random d_z | `negligible median difference ($\widetilde{\Delta} = \placeholder{}$)` |
| D2 | abstract.tex:10 | `$d_z$ ($0.19 \to 0.34$` | imp-vs-rand d_z (LLaMA) | `median paired differences increasing from $\widetilde{\Delta}{=}\placeholder{}$ to $\placeholder{}$ ($s{=}0.30$ Wilcoxon $p_{\text{Bonf}} = \placeholder{}$)` |
| D3 | results.tex:79 | `paired $d_z$ ($0.19 \to 0.26 \to 0.29 \to 0.34$)` | imp-vs-rand d_z (LLaMA) | 已在 §2b 中完整替换 |
| D4 | results.tex:79 | `$d_z \in [0.35, 0.45]$` | random d_z (LLaMA) | `random eviction also shows a non-trivial phase gradient (Wilcoxon $p < \placeholder{}$ at $s{=}0.30$)` |
| D5 | results.tex:83-97 | Table 3 d_z 列 + caption | imp-vs-rand d_z (整列) | 已在 §2b 中完整重构 |
| D6 | discussion.tex:11 | `$d_z \in [0.35, 0.45]$` | random d_z (LLaMA) | `random pruning also exhibits a non-trivial phase gradient on LLaMA (Wilcoxon $p < \placeholder{}$), reducing the contrast between strategies` |
| D7 | appendix_results.tex:10 | `$d_z = -0.04$` | random d_z | `negligible median difference ($\widetilde{\Delta} = \placeholder{}$)` |
| D8 | appendix_moved.tex:56 | `$d_z = -0.04$` | random d_z | `negligible median difference ($\widetilde{\Delta} = \placeholder{}$)` |
| D9 | appendix_disc_analysis.tex:14 | `$d_z{=}{-}0.04$` | random d_z | `negligible effect size ($\widetilde{\Delta} = \placeholder{}$)` |
| D10 | appendix_disc_analysis.tex:49 | `$d_z{=}{-}0.04$` | random d_z | `negligible effect size ($\widetilde{\Delta} = \placeholder{}$, bootstrap CI spanning zero)` |

---

### ═══════════════════════════════════════
### 2f. C8 措辞修复（Priority 3）
### ═══════════════════════════════════════

**位置**：`results.tex:79`（第一句）

**当前**：`The qualitative pattern replicates:`
**替换**：`The directional pattern is consistent:`

（D060 要求 LLaMA 用 "suggests"/"partial support"；"replicates" 过强。已在 §2b 预写文本中使用 "The directional pattern is consistent"。）

---

### ═══════════════════════════════════════
### 2g. NEW-3: mean ρ → median ρ（Priority 3）
### ═══════════════════════════════════════

**位置 1**：`appendix_results.tex:7`
**位置 2**：`appendix_moved.tex:53`

**当前**：`mean $\rho = -0.11$, $p = 0.926$`
**替换**：`$\bar{\rho} = \placeholder{}$, $p = \placeholder{}$`（明确用 $\bar{\rho}$ 表示 Spearman ρ 的均值，而非 II 的 mean；或改为 median ρ）

---

### ═══════════════════════════════════════
### 2h. C5b Future Work 段落插入（Priority 3）
### ═══════════════════════════════════════

**插入位置**：`discussion.tex:8`（"Extended discussion in Appendix~\ref{app:extended-discussion}." 句**之前**）

**预写 LaTeX**：
```latex
A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached \placeholder{ORACLE\_PCT}\% (Wilcoxon $p = \placeholder{ORACLE\_P}$), below the pre-registered 30\% gate for claiming practical mitigation. A heuristic variant achieved \placeholder{HEUR\_PCT}\% recovery ($p = \placeholder{HEUR\_P}$), but 95\% CIs for both conditions span zero. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases---a promising direction for future work.
```

---

### ═══════════════════════════════════════
### 2i. Qwen Mid-Phase Caveat（Priority 3）
### ═══════════════════════════════════════

已在 §2c 中完整定义。预写文本包含主文 caveat + appendix 表格。

---

## Phase 3: Figure 重生成

使用 `draw-paper-figure` skill 在服务器端执行。每张图的参数来源于 `_project/chart/` info 文件。

| # | 文件名 | 数据源 | 引用位置 | 生成参数参考 |
|---|--------|--------|----------|-------------|
| F1 | `fig1_dose_response.pdf` | n=500 DS imp+rand G vs s | results.tex:57, caption:58 | `fig1_dose_response_bf16.txt` — G values 需替换为 n=500 值，B=10,000 CI |
| F2 | `fig3_crossover.pdf` | n=500 DS s=0.25 crossover | appendix_moved.tex:15, caption:16 | `fig3_crossover_bf16.txt` — II per-phase median 需替换 |
| F3 | `fig4_bootstrap.pdf` | n=500 paired d_z + permutation CI | appendix_moved.tex:89 | `fig4_forest_paired_dz.txt` — DS/QW d_z 需替换 |
| F4 | `fig5_crossmodel.pdf` | n=500 DS+QW Δ comparison | appendix_moved.tex:47, caption:48 | `fig5_crossmodel_bf16.txt` — DS/QW Δ 需替换 |

**生成流程**：
```bash
# 服务器端
cd /root/autodl-tmp/pacs
# 对每张图：用 n=500 数据调用绘图脚本
# 具体命令由 draw-paper-figure skill 生成
```

**Caption 同步**：
- F1 caption (results.tex:58): Q24 — G 值范围
- F2 caption (appendix_moved.tex:16): Q60 — crossover 倍数
- F3 caption (appendix_moved.tex:90): 无数值需替换
- F4 caption (appendix_moved.tex:48): Q63 — 比例描述

---

## Phase 4: 编译 + 校验

### 4.1 编译
```bash
cd /root/autodl-tmp/pacs/artifacts/_project/paper
latexmk -pdf main.tex
```

### 4.2 校验清单

- [ ] 无 undefined citation / reference warning
- [ ] 页数 ≤ EMNLP 限制（8 页正文 + unlimited appendix）
- [ ] 所有 `\placeholder{}` 已替换为实际数值
- [ ] D054: 全文搜索 `\mean` / `average` — 确认无 mean II 残留（Spearman ρ 的 $\bar{\rho}$ 除外）
- [ ] D059: 全文搜索 `imp.*rand.*d_z` / `random.*d_z` — 确认无违规
- [ ] D060: 搜索 `replicates` — 确认 LLaMA 相关语境已改为 `consistent` / `suggests`
- [ ] B=10,000: 搜索 `B{=}` — 确认所有 bootstrap 声明为 10,000
- [ ] s015: 搜索 `marginal` / `borderline` / `ns` / `non-significant` + s015 — 确认已清除
- [ ] Qwen null rate caveat 已在 §5.4 出现
- [ ] C5b pilot 已在 Discussion 出现
- [ ] W2: LLaMA §5.5 同时报所有 4 个 sparsity level 的 CI + p

### 4.3 一致性交叉验证

以下数值必须在所有出现位置一致：

| 数值类别 | 出现位置 | 验证方法 |
|---------|---------|---------|
| DS G 范围 | Q21, Q24, Q41, Q47 | grep `{\times}` |
| DS Δ s015→s030 | Q3, Q12, Q19, Tab1 | grep `s{=}0.15` |
| DS d_z s015→s030 | Q4, Q39, Q48, Tab4 | grep `d_z{=}` |
| Random PASS/FAIL | Q6, Q15, Q49, Q57 | grep `conditions` |
| Crossover 数值 | Q8, Q25, Q42, Q59 | grep `0.032` → 旧值 |
| Qwen d_z 下界 | Q9, Q13, Q30, Q50 | grep `d_z \geq` |
| LLaMA 倍数 | Q11, Q14, Q37, Q44, Q51 | grep `{\times}.*smaller` |
| Qwen/DS 比值 | Q27, Q62, Q63 | grep `one-fifth` / `1/5` |
| Permutation CI | Q67, Q75, Tab6 | grep CI bounds |

---

## Phase 5: Group C Review 提交

1. 编译通过后，从服务器拉回 PDF：`scp connect.westd.seetacloud.com:/root/autodl-tmp/pacs/artifacts/_project/paper/main.pdf ./`
2. 更新 chart info 文件（`_project/chart/fig*_n500.txt`）记录新数据源
3. Git commit: `n=500 paper update: all tables/figures/claims updated, D059/W2/W5/s015 fixes`
4. 提交 Group C review

---

## 风险监控

| 风险 | 触发条件 | 影响 | 应对 |
|------|---------|------|------|
| RISK-1: Qwen s015 仍 ns | n=500 CI 跨零 | 保留 marginal 叙事 | memory.md 已确认显著，低风险 |
| RISK-2: Random PASS/FAIL 变化 | n=500 检测到更多显著 | "X/8 non-significant" 数字变化 | 如实报告，必要时调整叙事 |
| RISK-3: LLaMA 不重跑 | LLaMA 保持 n=49 | 倍数比分母变化 | 用 n=500 DS/QW 重算比值，LLaMA 数据标注 "n=49" |
| RISK-4: Table 3 重构破坏叙事 | 删除 d_z 列后 §5.5 逻辑断裂 | 需重写 §5.5 段落 | §2b 已提供完整预写文本 |
| RISK-5: Crossover 不稳定 | n=500 crossover 倍数大幅变化 | 影响 key finding 叙事 | 如实报告新倍数，保留定性描述 |
| RISK-6: C4 entropy 不重跑 | C4 保持 n=50 | Tables 7-8 标注 "n=50 subset" | 在 caption 标注，不影响主要结论 |

---

## 执行时间估计

| Phase | 预估时间 | 说明 |
|-------|---------|------|
| Phase 0: Sync | 5 min | |
| Phase 1: Pipeline | 30-60 min | B=10,000 计算密集 |
| Phase 2a: 数据替换 | 60-90 min | 8 表 + 77 处声明 |
| Phase 2b: W2 修复 | 15 min | 预写文本就绪 |
| Phase 2c: W5 修复 | 15 min | 预写文本就绪 |
| Phase 2d: s015 升级 | 10 min | 7 处替换 |
| Phase 2e: D059 清理 | 20 min | 10 处替换 |
| Phase 2f-2i: 其他 | 15 min | |
| Phase 3: Figures | 30-45 min | 4 张图 |
| Phase 4: 编译校验 | 20 min | |
| **Total** | **~3.5-5 hr** | |
