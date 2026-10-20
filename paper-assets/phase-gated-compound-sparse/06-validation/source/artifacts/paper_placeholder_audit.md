# Paper Placeholder & Hardcoded Value Audit

> 审计日期: 2026-05-15
> 论文路径: `artifacts/_project/paper/`
> 对照文档: `artifacts/n500_paper_update_checklist.md`

---

## 一、\placeholder{} 汇总 (48 处，10 个唯一数据源)

### A. 命名 placeholder（6 处，4 个数据源）

| # | 文件:行 | 内容 | 上下文 | 数据来源 |
|---|---------|------|--------|----------|
| 1 | results.tex:71 | `\placeholder{NULL_PCT}` | Qwen mid-phase null rate，~X% of problems yield near-zero II | n=500 Qwen profiling数据 |
| 2 | results.tex:86 | `\placeholder{N_LLAMA}` | LLaMA cross-arch table caption: "$n{=}\placeholder{N\_LLAMA}$ paired problems" | c3_llama 实验（不变，但从未填入） |
| 3 | appendix_moved.tex:30 | `\placeholder{NULL_PCT}` | 同 #1 重复引用: "null rate (\placeholder{NULL\_PCT}\%)" | 同 #1 |
| 4 | appendix_moved.tex:35 | `\placeholder{N_QW}` | Qwen effective-n table caption: "$n_{\text{total}} = \placeholder{N\_QW}$" | n=500 Qwen 有效样本量 |
| 5 | discussion.tex:10 | `\placeholder{ORACLE_PCT}` | C5b pilot: "oracle recovery reached \placeholder{ORACLE\_PCT}\%" | C5b 实验数据 |
| 6 | discussion.tex:10 | `\placeholder{ORACLE_P}` | C5b pilot: "Wilcoxon $p = \placeholder{ORACLE\_P}$" | C5b 实验数据 |
| 7 | discussion.tex:10 | `\placeholder{HEUR_PCT}` | C5b pilot: "heuristic variant achieved \placeholder{HEUR\_PCT}\% recovery" | C5b 实验数据 |
| 8 | discussion.tex:10 | `\placeholder{HEUR_P}` | C5b pilot: "$p = \placeholder{HEUR\_P}$" | C5b 实验数据 |

### B. 匿名 placeholder — QW rand s030 Δ̃（5 处，1 个数据源）

| # | 文件:行 | 上下文 |
|---|---------|--------|
| 9 | abstract.tex:8 | "negligible median difference ($\widetilde{\Delta} = \placeholder{}$)" |
| 10 | appendix_moved.tex:76 | "negligible median difference ($\widetilde{\Delta} = \placeholder{}$, CI spans zero)" |
| 11 | appendix_results.tex:10 | "negligible median difference ($\widetilde{\Delta} = \placeholder{}$, CI spans zero)" |
| 12 | appendix_disc_analysis.tex:14 | "negligible effect size ($\widetilde{\Delta} = \placeholder{}$)" |
| 13 | appendix_disc_analysis.tex:49 | "negligible effect size ($\widetilde{\Delta} = \placeholder{}$, bootstrap CI spanning zero)" |

数据来源: experiment_summary_table.json → QW rand s030 median_diff

### C. 匿名 placeholder — LLaMA random Wilcoxon p（2 处，1 个数据源）

| # | 文件:行 | 上下文 |
|---|---------|--------|
| 14 | results.tex:81 | "Wilcoxon $p < \placeholder{}$ at $s{=}0.30$" |
| 15 | discussion.tex:15 | "random pruning also exhibits a non-trivial phase gradient (Wilcoxon $p < \placeholder{}$)" |

数据来源: c3_llama 实验（LLaMA 不重跑，数据已有但未填入）

### D. 匿名 placeholder — Per-problem concordance ρ, p（4 处，1 个数据源）

| # | 文件:行 | 上下文 |
|---|---------|--------|
| 16 | appendix_moved.tex:73 | "median $\rho = \placeholder{}$, $p = \placeholder{}$" |
| 17 | appendix_results.tex:7 | "median $\rho = \placeholder{}$, $p = \placeholder{}$" |

数据来源: cross_model_analysis.json (注释中已有: mean_rho=-0.107, p=0.926，但正文未填入)

### E. 匿名 placeholder — LLaMA cross-arch table（16 处）

| # | 文件:行 | 内容 |
|---|---------|------|
| 18-21 | results.tex:92 | s=0.15: Δ̃, CI_lo, CI_hi, p_Bonf |
| 22-25 | results.tex:93 | s=0.20: Δ̃, CI_lo, CI_hi, p_Bonf |
| 26-29 | results.tex:94 | s=0.25: Δ̃, CI_lo, CI_hi, p_Bonf |
| 30-33 | results.tex:95 | s=0.30: Δ̃, CI_lo, CI_hi, p_Bonf |

数据来源: c3_llama 实验（LLaMA 不重跑，数据已有但未填入）

### F. 匿名 placeholder — Qwen effective-n table（12 处）

| # | 文件:行 | 内容 |
|---|---------|------|
| 34-37 | appendix_moved.tex:41 | High phase: s=0.15, 0.20, 0.25, 0.30 |
| 38-41 | appendix_moved.tex:42 | Mid phase: s=0.15, 0.20, 0.25, 0.30 |
| 42-45 | appendix_moved.tex:43 | Low phase: s=0.15, 0.20, 0.25, 0.30 |

数据来源: n=500 Qwen profiling（需从 n=500 数据计算 |II| > 0.001 的问题数）

### Placeholder 汇总

| 数据源 | 处数 | n=500 后需更新? |
|--------|------|-----------------|
| QW rand s030 Δ̃ | 5 | 是（n=500 重跑） |
| NULL_PCT (Qwen null rate) | 2 | 是（n=500 重算） |
| N_QW (Qwen total n) | 1 | 是 |
| N_LLAMA (LLaMA n) | 1 | 否（LLaMA 不重跑，但需填入已有数据） |
| LLaMA table 16 cells | 16 | 否（数据已有，需填入） |
| LLaMA random Wilcoxon p | 2 | 否（数据已有，需填入） |
| Per-problem concordance ρ, p | 4 | 是（n=500 重算） |
| Qwen effective-n table 12 cells | 12 | 是（n=500 重算） |
| C5b pilot (ORACLE/HEUR) | 4 | 独立于 n=500，取决于 C5b 实验 |
| **合计** | **48** | |

---

## 二、硬编码数值汇总（~120 处）

### 样本量文本 "50"→"500"（8 处）

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 1 | abstract.tex:6 | `50 MATH-500 problems` | 是→500 |
| 2 | methodology.tex:10 | `50 problems stratified from MATH-500` | 是→500 |
| 3 | results.tex:13 | `$n{=}50$ MATH-500 problems` (Table 1 caption) | 是→500 |
| 4 | results.tex:34 | `medians across 50 problems` (Table 2 caption) | 是→500 |
| 5 | appendix_moved.tex:26 | `Four of the 50 problems are excluded` | 是→新排除数/总数 |
| 6 | appendix_moved.tex:26 | `$n{=}46$ valid problems for Qwen (vs.\ $n{=}49$ for DeepSeek)` | 是→新有效n |
| 7 | appendix_moved.tex:93 (tab:permutation caption) | `$n{=}49$, $10{,}000$ permutations` | 是→新n |
| 8 | appendix_disc_analysis.tex:45 | `$n{=}49$...and $n{=}46$ for Qwen (4 excluded)` | 是→新n |

### Table 1: Aggregate II (results.tex:10-23) — 10 处

| # | 文件:行 | 当前值 | 数据来源 | 需要更新? |
|---|---------|--------|----------|-----------|
| 9 | results.tex:19 | `0.39 & 1.48 & 7.16 & 14.59` | DS imp median_diff | 是 |
| 10 | results.tex:20 | `0.01 & $-$0.02 & 0.54 & 1.54` | DS rand median_diff | 是 |
| 11 | results.tex:8 | `$0.39$...$14.59$...37×` | 同上 + 比率重算 | 是 |
| 12 | results.tex:8 | `$-0.02$ to $1.54$` | DS rand range | 是 |

### Table 2: Per-phase II (results.tex:31-53) — 40 处 (8行×5列)

| # | 文件:行 | 行标签 | 当前值 (II_high, II_mid, II_low, Δ, G) | 需要更新? |
|---|---------|--------|----------------------------------------|-----------|
| 13 | results.tex:40 | 0.15 Imp | 0.006, 0.081, 0.398, 0.39, 69 | 是 |
| 14 | results.tex:41 | 0.15 Rand | 0.093, 0.097, 0.103, 0.01, 1.1 | 是 |
| 15 | results.tex:43 | 0.20 Imp | 0.015, 0.203, 1.496, 1.48, 103 | 是 |
| 16 | results.tex:44 | 0.20 Rand | 0.292, 0.350, 0.276, −0.02, 0.9 | 是 |
| 17 | results.tex:46 | 0.25 Imp | 0.032, 1.118, 7.196, 7.16, 222 | 是 |
| 18 | results.tex:47 | 0.25 Rand | 0.818, 0.932, 1.363, 0.54, 1.7 | 是 |
| 19 | results.tex:49 | 0.30 Imp | 0.053, 2.283, 14.639, 14.59, 274 | 是 |
| 20 | results.tex:50 | 0.30 Rand | 2.503, 2.592, 4.041, 1.54, 1.6 | 是 |

### Table 3: Cohen's d (results.tex:108-124) — 16 处

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 21 | results.tex:117 | DS: 0.44, 0.32 [0.20, 0.47]; QW: 0.28, 0.05 [−0.01, 0.11]^ns | 是 |
| 22 | results.tex:118 | DS: 0.52, 1.15 [0.66, 1.26]; QW: 0.55, 0.21 [0.07, 0.40] | 是 |
| 23 | results.tex:119 | DS: 0.68, 3.97 [2.83, 5.29]; QW: 0.89, 1.11 [0.61, 1.47] | 是 |
| 24 | results.tex:120 | DS: 0.80, 9.94 [8.39, 16.65]; QW: 1.02, 2.62 [1.72, 3.65] | 是 |

### Table: Cross-model (appendix_moved.tex:50-63) — 8 处

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 25 | appendix_moved.tex:59 | DS: 0.39, 1.48, 7.16, 14.59 | 是 |
| 26 | appendix_moved.tex:60 | QW: 0.04, 0.23, 1.27, 2.94 | 是 |

### Table: Permutation test (appendix_moved.tex:90-105) — 12 处

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 27 | appendix_moved.tex:99 | s015: 0.37, [0.19, 0.62], 0.0032 | 是 |
| 28 | appendix_moved.tex:100 | s020: 0.97, [0.69, 1.49], <0.001 | 是 |
| 29 | appendix_moved.tex:101 | s025: 3.34, [1.66, 6.64], <0.001 | 是 |
| 30 | appendix_moved.tex:102 | s030: 9.85, [6.70, 16.29], <0.001 | 是 |

### Table: Discrimination metrics (appendix_moved.tex:123-143) — 16 处

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 31 | appendix_moved.tex:132 | DS 0.15: −0.030, −0.56 | 是 |
| 32 | appendix_moved.tex:133 | DS 0.20: −0.040, −0.77 | 是 |
| 33 | appendix_moved.tex:134 | DS 0.25: −0.065, −1.29 | 是 |
| 34 | appendix_moved.tex:135 | DS 0.30: −0.081, −1.66 | 是 |
| 35 | appendix_moved.tex:137 | QW 0.15: −0.010, −0.05 | 是 |
| 36 | appendix_moved.tex:138 | QW 0.20: −0.012, −0.21 | 是 |
| 37 | appendix_moved.tex:139 | QW 0.25: −0.010, −1.49 | 是 |
| 38 | appendix_moved.tex:140 | QW 0.30: −0.020, −1.14 | 是 |

### Table: Entropy deltas (appendix_moved.tex:163-183) — 8 处

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 39 | appendix_moved.tex:171 | DS 0.15: −0.040 | 是 |
| 40 | appendix_moved.tex:172 | DS 0.20: −0.047 | 是 |
| 41 | appendix_moved.tex:173 | DS 0.25: −0.045 | 是 |
| 42 | appendix_moved.tex:174 | DS 0.30: −0.044 | 是 |
| 43 | appendix_moved.tex:177 | QW 0.15: −0.073 | 是 |
| 44 | appendix_moved.tex:178 | QW 0.20: −0.076 | 是 |
| 45 | appendix_moved.tex:179 | QW 0.25: +0.045 | 是 |
| 46 | appendix_moved.tex:180 | QW 0.30: −0.007 | 是 |

### 内联统计声明 — abstract.tex（~12 处）

| # | 文件:行 | 当前值 | 数据来源 | 需要更新? |
|---|---------|--------|----------|-----------|
| 47 | abstract.tex:7 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | DS imp median_diff | 是 |
| 48 | abstract.tex:7 | `$d_z$ growing from $0.44$ (small) to $0.80$ (large)` | cohens_d_bf16.json | 是 |
| 49 | abstract.tex:7 | `$p < 0.005$` | permutation_test_results.json | 是（验证阈值） |
| 50 | abstract.tex:8 | `7/8 conditions` | 重统计 random PASS/FAIL | 是（可能→8/8） |
| 51 | abstract.tex:8 | `$p{=}0.012$` | QW rand s030 | 是 |
| 52 | abstract.tex:9 | `$0.032$ vs.\ $0.818$` | DS s025 high-phase | 是 |
| 53 | abstract.tex:9 | `$7.196$ vs.\ $1.363$` | DS s025 low-phase | 是 |
| 54 | abstract.tex:10 | `$d_z \geq 0.55$` | QW s020 d_z | 是 |
| 55 | abstract.tex:10 | `Spearman $\rho = 1.0$` | cross_model_analysis.json | 是（验证） |
| 56 | abstract.tex:10 | `$p = 0.043$` | cross_model_analysis.json | 是 |
| 57 | abstract.tex:10 | `${\sim}$1/40 the absolute magnitude` | **间接**：DS Δ̃变→比率重算 | 是 |
| 58 | abstract.tex:10 | `$0.020 \to 0.356$` | c3_llama（不变） | 否 |

### 内联统计声明 — introduction.tex（~5 处）

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 59 | introduction.tex:14 | `$0.39$...$14.59$` | 是 |
| 60 | introduction.tex:14 | `$d_z$: $0.44 \to 0.80$` | 是 |
| 61 | introduction.tex:14 | `$p < 0.005$` | 是（验证） |
| 62 | introduction.tex:15 | `$d_z \geq 0.55$` | 是 |
| 63 | introduction.tex:15 | `$\sim$1/40 the magnitude` | 是（间接） |
| 64 | introduction.tex:16 | `7/8 conditions non-significant` | 是（可能→8/8） |

### 内联统计声明 — methodology.tex（2 处）

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 65 | methodology.tex:18 | `mean/median ratios up to 43:1` | 是 |
| 66 | methodology.tex:22 | `$p_{\text{Bonf}} < 0.005$` | 是（验证） |

### 内联统计声明 — results.tex 正文（~20 处）

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 67 | results.tex:29 | `$69{\times}$...$274{\times}$` | 是 |
| 68 | results.tex:29 | `$0.006$ to $0.053$` | 是 |
| 69 | results.tex:29 | `$G \approx 0.9$--$1.7{\times}$` | 是 |
| 70 | results.tex:58 | `$69{\times}$ to $274{\times}$` (fig caption) | 是 |
| 71 | results.tex:66 | `$0.032$ vs.\ $0.818$` | 是 |
| 72 | results.tex:66 | `$7.196$ vs.\ $1.363$---a $5.3{\times}$` | 是 |
| 73 | results.tex:71 | `$0.04$...$2.94$...${\sim}1/5$` | 是 |
| 74 | results.tex:71 | `$d_z \geq 0.55$; Spearman $\rho = 1.0$; $p = 0.043$` | 是 |
| 75 | results.tex:71 | `$d_z{=}0.28$, CI includes zero` | 是 |
| 76 | results.tex:77 | `$0.37$...$9.85$` | 是 |
| 77 | results.tex:81 | `${\sim}40{\times}$ smaller...and ${\sim}7{\times}$ smaller` | 是（间接） |
| 78 | results.tex:106 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` | 是 |
| 79 | results.tex:106 | `$d_z{=}0.28$...CI includes zero...$d_z \geq 0.55$` | 是 |
| 80 | results.tex:106 | `$d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$` | 是 |

### 内联统计声明 — analysis.tex（~5 处）

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 81 | analysis.tex:4 | `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)` | 是 |
| 82 | analysis.tex:4 | `16 conditions` | 是（验证） |
| 83 | analysis.tex:6 | `$\Delta\mathcal{H} \in [-0.047, -0.040]$` | 是 |
| 84 | analysis.tex:6 | `$\Delta\mathcal{H} = +0.045$` | 是 |
| 85 | analysis.tex:6 | `22 of 30 problems` | 是 |

### 内联统计声明 — discussion.tex（~7 处）

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 86 | discussion.tex:5 | `$69$--$274{\times}$` | 是 |
| 87 | discussion.tex:5 | `$0.032$ vs.\ $0.818$` | 是 |
| 88 | discussion.tex:5 | `$7.196$ vs.\ $1.363$` | 是 |
| 89 | discussion.tex:5 | `$G \approx 1$` | 是（验证） |
| 90 | discussion.tex:15 | `${\sim}40{\times}$...${\sim}7{\times}$` | 是（间接） |
| 91 | discussion.tex:15 | `$d_z \geq 1.0$` | 否（LLaMA 不变） |

### 内联统计声明 — conclusion.tex（~5 处）

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 92 | conclusion.tex:4 | `$69{\times}$ to $274{\times}$` | 是 |
| 93 | conclusion.tex:4 | `$d_z$: $0.44 \to 0.80$` | 是 |
| 94 | conclusion.tex:4 | `7/8 conditions non-significant` | 是（可能→8/8） |
| 95 | conclusion.tex:4 | `$d_z \geq 0.55$` | 是 |
| 96 | conclusion.tex:4 | `$\sim$1/40 the magnitude` | 是（间接） |

### 内联统计声明 — appendix.tex（1 处）

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 97 | appendix.tex:38 | `$G_{\times} = 58$--$241{\times}$` | 是 |

### 内联统计声明 — appendix_moved.tex 正文（~12 处）

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 98 | appendix_moved.tex:11 | `$0.032$ vs.\ $0.818$`...`$7.196$ vs.\ $1.363$---a $5.3{\times}$` | 是 |
| 99 | appendix_moved.tex:11 | `$3.9{\times}$...$5.4{\times}$...$5.3{\times}$...$3.6{\times}$` | 是 |
| 100 | appendix_moved.tex:16 | `$5.3{\times}$` (fig caption) | 是 |
| 101 | appendix_moved.tex:26 | `Four of the 50 problems` | 是 |
| 102 | appendix_moved.tex:48 | `${\sim}1/5$` (fig caption) | 是 |
| 103 | appendix_moved.tex:68 | `one-fifth` | 是 |
| 104 | appendix_moved.tex:84 | `mean/median ratios...$1.2{\times}$...$1.6{\times}$` DS | 是 |
| 105 | appendix_moved.tex:84 | `$1.1{\times}$ to $1.4{\times}$` QW | 是 |
| 106 | appendix_moved.tex:86 | `$99.92$th percentile...$p_{\text{Bonf}} = 0.0032$` | 是 |
| 107 | appendix_moved.tex:88 | `$0.37$...$9.85$...CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$)` | 是 |
| 108 | appendix_moved.tex:53 (comment) | `mean $\rho = -0.11$, $p = 0.926$` | 已在 placeholder 中 |

### 内联统计声明 — appendix_disc_analysis.tex（~10 处）

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 109 | appendix_disc_analysis.tex:4 | `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$` | 是 |
| 110 | appendix_disc_analysis.tex:11 | `$\widetilde{\mathrm{II}}_{\text{high}} < 0.06$` | 是 |
| 111 | appendix_disc_analysis.tex:11 | `$s = 0.35$, high-phase II rises to $0.105$` | 否（s035 补充实验不重跑） |
| 112 | appendix_disc_analysis.tex:14 | `7/8...Qwen $s{=}0.30$, $p{=}0.012$...$d_z{=}{-}0.04$` | 是 |
| 113 | appendix_disc_analysis.tex:45 | `$n{=}49$...$n{=}46$` | 是（同 #8） |
| 114 | appendix_disc_analysis.tex:46 | `mean/median ratio ${\sim}1.6{:}1$...mean_diff=22.94, median_diff=14.59` | 是 |
| 115 | appendix_disc_analysis.tex:47 | CIs: `[0.19, 0.62]...[0.69, 1.49]...[1.66, 6.64]...[6.70, 16.29]` | 是 |
| 116 | appendix_disc_analysis.tex:49 | `$p{=}0.012$...$d_z{=}{-}0.04$...d=-0.035` | 是 |
| 117 | appendix_disc_analysis.tex:57 | `$\Delta$ growth rate $3.8{\times} \to 4.8{\times} \to 2.0{\times}$` (comment) | 是（注释中的数据） |

### 内联统计声明 — limitations.tex（1 处，新发现）

| # | 文件:行 | 当前值 | 需要更新? |
|---|---------|--------|-----------|
| 118 | limitations.tex:2 | `$\sim$1/40 of DeepSeek` | 是（间接：DS Δ̃变→比率重算） |

---

## 三、不需更新的值

| 文件:行 | 当前值 | 原因 |
|---------|--------|------|
| results.tex:77 | `$n{=}49$ paired problems` | LLaMA 实验不重跑 |
| results.tex:79 | `$[0.002, 0.043]$`, `$p_{\text{Bonf}}{=}0.219$` 等 LLaMA 统计量 | LLaMA 数据不变 |
| results.tex:79 | `$0.020 \to 0.356$` LLaMA Δ̃ | LLaMA 数据不变 |
| abstract.tex:10 | `$0.020 \to 0.356$` LLaMA Δ̃ | LLaMA 数据不变 |
| abstract.tex:10 | `$p_{\text{Bonf}}{=}0.029$` LLaMA s030 | LLaMA 数据不变 |
| discussion.tex:15 | `$d_z \geq 1.0$` LLaMA within-importance d_z | LLaMA 数据不变 |
| appendix_disc_analysis.tex:11 | `$s = 0.35$, high-phase II rises to $0.105$` | s035 补充实验不重跑 |
| related_work.tex | 全文 | 无实验数据 |
| background.tex | 全文 | 公式定义，无实验数据 |
| limitations.tex (大部分) | 描述性限定语 | 无具体数值（除比率声明外） |
| 所有 `\cite{}` 引用 | — | 无变化 |

**注意：LLaMA 绝对值不变，但 LLaMA 与 DS/QW 的比率声明需要重算（见间接影响）。**

---

## 四、间接影响：LLaMA 比率声明（4+1 处）

LLaMA 数据不变（Δ̃_s030 = 0.356），但 DS/QW 的 Δ̃ 变化导致比率需重算：

| # | 文件:行 | 当前声明 | 计算方法 |
|---|---------|---------|----------|
| 1 | abstract.tex:10 | `${\sim}$1/40` | 新 DS s030 Δ̃ / 0.356 |
| 2 | results.tex:81 | `${\sim}40{\times}$ smaller...and ${\sim}7{\times}$ smaller` | 新 DS/QW s030 Δ̃ / 0.356 |
| 3 | discussion.tex:15 | `${\sim}40{\times}$...${\sim}7{\times}$` | 同上 |
| 4 | conclusion.tex:4 | `$\sim$1/40` | 同上 |
| 5 | **limitations.tex:2** | `$\sim$1/40 of DeepSeek` | 同上（**新发现，不在已有清单中**） |

---

## 五、条件性叙事更新

### Qwen s015 决策点

n=500 后 QW s015 Cohen's d CI 是否仍含零决定叙事方案：

| 情况 | 影响位置数 | 操作 |
|------|-----------|------|
| CI 仍跨零 | 6 处 | 仅更新数值，保留 "marginal at s015 / reliable at s≥0.20" |
| CI > 0 | 6 处 | 升级为 "all four sparsity levels"，删除 ^ns |

影响文件: abstract.tex:10, introduction.tex:15, results.tex:71, results.tex:117, results.tex:122 (脚注), conclusion.tex:4

### Random 7/8 vs 8/8 决策点

n=500 后 QW rand s030 的 borderline PASS (p=0.012) 可能翻转为 FAIL：

| 情况 | 影响位置数 | 操作 |
|------|-----------|------|
| 仍 PASS | 5 处 | 仅更新 p 值和 Δ̃ |
| 翻转 FAIL | 5 处 | "7/8"→"8/8", "3/4"→"4/4", 删除 exception 叙事 |

影响文件: abstract.tex:8, introduction.tex:16, conclusion.tex:4, appendix_disc_analysis.tex:14, appendix_results.tex:10

---

## 六、与已有规划文档的差异

对照 `n500_paper_update_checklist.md`：

### 已有清单覆盖的内容
- §1 样本量文本替换: ✓ 完全覆盖
- §2 Tables: ✓ 完全覆盖
- §3 Figures: ✓ 完全覆盖（本审计不重复）
- §4 内联统计声明: ✓ 基本覆盖
- §5 Qwen s015 决策点: ✓ 完全覆盖
- §6 附属统计量: ✓ 完全覆盖
- §7 数据管道: ✓ 完全覆盖
- §8 不需更新部分: ✓ 基本正确
- §10 LLaMA 间接比率: ✓ 覆盖 4 处

### **新发现（不在已有清单中）**

| # | 发现 | 位置 | 说明 |
|---|------|------|------|
| **NEW-1** | **limitations.tex:2 的 LLaMA 比率声明** | `$\sim$1/40 of DeepSeek` | 已有清单 §10 遗漏了 limitations.tex，仅列出 abstract/results/discussion/conclusion |
| **NEW-2** | **C5b pilot placeholders 未纳入** | discussion.tex:10 的 4 个 `\placeholder{ORACLE_*/HEUR_*}` | 已有清单 §11 仅确认 "无需改"，但这 4 个 placeholder 确实存在且需要填入 C5b 实验数据 |
| **NEW-3** | **appendix_moved.tex:16 fig caption** | `$5.3{\times}$` crossover 倍数 | 已有清单中 crossover 倍数仅列 L11，遗漏了 fig3 caption L16 |
| **NEW-4** | **appendix_moved.tex:48/68 "one-fifth" 比率** | fig5 caption + 正文 | 已有清单提到了 fig5 caption 中的 "one-fifth" 但内联引用位置不完整 |

### 已有清单的数量统计 vs 实际

| 类别 | 清单统计 | 实际统计 |
|------|---------|---------|
| 样本量文本 | 8 处 | 8 处 ✓ |
| 表格单元格 | ~80 | ~110（含 placeholder 表格 28 cells） |
| 图表 PDF | 5 | 5 ✓ |
| 内联统计数值 | ~60 | ~72 处 |
| Qwen s015 叙事 | 6 处 | 6 处 ✓ |
| 7/8 vs 8/8 叙事 | 5 处 | 5 处 ✓ |
| LLaMA 间接比率 | 4 处 | **5 处**（+limitations.tex） |
| Placeholder 总数 | 未统计 | **48 处** |

---

## 七、全量统计

| 类别 | 数量 |
|------|------|
| `\placeholder{}` 实例 | 48 |
| 其中 n=500 后需更新 | 24 |
| 其中 LLaMA 数据（已有未填） | 19 |
| 其中 C5b 独立实验 | 4 |
| 其中 per-problem concordance（注释有数据未填） | 4（注释中有 ρ=-0.107, p=0.926） |
| 硬编码数值需更新 | ~118 |
| 间接比率重算 | 5 |
| 条件性叙事更新 | 11（两个决策点） |
| 图表重新生成 | 5 PDF |
| **总替换位置** | **~170+** |
