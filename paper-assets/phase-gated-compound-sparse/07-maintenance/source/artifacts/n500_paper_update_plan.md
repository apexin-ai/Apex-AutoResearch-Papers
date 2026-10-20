# n=500 论文更新计划

> 基于 n=50 bf16 论文全面扫描。截稿 2026-05-25。
> 分类：**[确定]** = n=500 数据到手后确定要改；**[视结果]** = 需看 n=500 分析结果决定。

---

## 文件级清单

### abstract.tex

- **L6** `using 50 MATH-500 problems` → **[确定]** 改为 `500 MATH-500 problems`
- **L7** `the median Interaction Index difference ... increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large)` → **[确定]** 全部数值替换为 n=500 median + d_z
- **L8** `$\widetilde{\Delta} = \placeholder{}$` → **[确定]** 填入 n=500 Qwen random s030 的 median diff
- **L9** `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` 及 `$\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$` → **[确定]** 替换为 n=500 crossover 数值
- **L10** `$\widetilde{\Delta}$: $0.020 \to 0.356$; $s{=}0.30$ Wilcoxon $p_{\text{Bonf}}{=}0.029$` → **[确定]** 替换为 n=500 LLaMA 数值
- **L10** `at ${\sim}$1/40 the absolute magnitude` → **[视结果]** n=500 后 magnitude ratio 可能变化

### introduction.tex

- **L14** `the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels)` → **[确定]** 替换全部数值
- **L15** `($d_z \geq 0.55$)` → **[确定]** 替换为 n=500 Qwen d_z 下界
- **L15** `at $\sim$1/40 the magnitude` → **[视结果]** 同 abstract L10

### methodology.tex

- **L10** `We use 50 problems stratified from MATH-500` → **[确定]** 改为 `500 problems`
- **L22** `$p_{\text{Bonf}} < 0.005$ at every sparsity level` → **[视结果]** p 值可能更小，但若仍 <0.005 文字可保留

### results.tex

#### Tab 1 (aggregate-ii, L10–23)
- **L13** caption: `$n{=}50$ MATH-500 problems` → **[确定]** 改为 `$n{=}500$`
- **L19** `0.39 & 1.48 & 7.16 & 14.59` → **[确定]** 替换为 n=500 importance median_diff
- **L20** `0.01 & $-$0.02 & 0.54 & 1.54` → **[确定]** 替换为 n=500 random median_diff

#### 正文引用 Tab 1 (L8)
- **L8** `$\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification ... $-0.02$ to $1.54$` → **[确定]** 替换所有数值及倍数

#### Tab 2 (main-results, L31–53)
- **L34** caption: `medians across 50 problems` → **[确定]** 改为 `500 problems`
- **L40** `0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$` → **[确定]** 整行替换
- **L41** `0.093 & 0.097 & 0.103 & 0.01 & 1.1` → **[确定]** 整行替换
- **L43** `0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$` → **[确定]** 整行替换
- **L44** `0.292 & 0.350 & 0.276 & $-$0.02 & 0.9` → **[确定]** 整行替换
- **L46** `0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$` → **[确定]** 整行替换
- **L47** `0.818 & 0.932 & 1.363 & 0.54 & 1.7` → **[确定]** 整行替换
- **L49** `0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$` → **[确定]** 整行替换
- **L50** `2.503 & 2.592 & 4.041 & 1.54 & 1.6` → **[确定]** 整行替换

#### 正文引用 Tab 2 (L29)
- **L29** `$G$ increases from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$ ... $\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$ ... $G \approx 0.9$--$1.7{\times}$` → **[确定]** 替换所有 G 值和 II_high 值

#### Fig 1 caption (L58)
- **L58** `from $69{\times}$ to $274{\times}$` → **[确定]** 替换 G 值范围

#### Crossover (L66)
- **L66** `$0.032$ vs.\ $0.818$ ... $7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal` → **[确定]** 替换 crossover 数值

#### Cross-Model (L71)
- **L71** `$\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\sim}1/5$ the magnitude` → **[确定]** 替换 Qwen Δ 数值和倍数比
- **L71** `The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \geq 0.20$ ($d_z \geq 0.55$)` → **[确定]** 替换 d_z 值；**删除 "marginal at s=0.15"**（n=500 CI 预期不跨零）
- **L71** `\placeholder{NULL\_PCT}` → **[确定]** 填入 n=500 Qwen mid-phase null rate %

#### Cross-Architecture (L77–81)
- **L77** `$n{=}49$ paired problems` → **[确定]** 替换为 n=500 LLaMA valid sample size
- **L79** 全段 LLaMA 描述文字（CI 数值、p 值、$\widetilde{\Delta}$: $0.020 \to 0.356$ 等） → **[确定]** 全部替换为 n=500 数值
- **L81** `${\sim}40{\times}$ smaller ... ${\sim}7{\times}$ smaller` → **[视结果]** magnitude ratios 可能变化
- **L81** `Wilcoxon $p < \placeholder{}$` → **[确定]** 填入 LLaMA random p 值

#### Tab 3 (llama-cross-arch, L83–98)
- **L86** caption: `$n{=}\placeholder{N\_LLAMA}$` → **[确定]** 填入 n=500 LLaMA sample size
- **L92–95** 全部 `\placeholder{}` → **[确定]** 填入 n=500 LLaMA 每个 sparsity level 的 Δ, CI, p

#### Statistical Validation (L104)
- **L104** `from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` → **[确定]** 替换 permutation test median diffs

#### Tab 4 (cohens-d, L108–124)
- **L117** DS d_z: `0.44`, Δ: `0.32\; $[0.20, 0.47]$`, QW d_z: `0.28`, Δ: `0.05\; $[-0.01, 0.11]$\textsuperscript{ns}` → **[确定]** 全部替换；**删除 `\textsuperscript{ns}`**（n=500 预期显著）
- **L118** DS d_z: `0.52`, Δ: `1.15\; $[0.66, 1.26]$`, QW d_z: `0.55`, Δ: `0.21\; $[0.07, 0.40]$` → **[确定]** 替换
- **L119** DS d_z: `0.68`, Δ: `3.97\; $[2.83, 5.29]$`, QW d_z: `0.89`, Δ: `1.11\; $[0.61, 1.47]$` → **[确定]** 替换
- **L120** DS d_z: `0.80`, Δ: `9.94\; $[8.39, 16.65]$`, QW d_z: `1.02`, Δ: `2.62\; $[1.72, 3.65]$` → **[确定]** 替换
- **L122** `\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \geq 0.20$.` → **[确定]** **删除整行脚注**（n=500 Qwen s015 CI 不跨零）

#### 正文引用 Tab 4 (L106)
- **L106** `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large) ... marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \geq 0.20$ ($d_z \geq 0.55$) ... $d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$` → **[确定]** 全部替换；**删除 "marginal at s=0.15" 语句**

### analysis.tex

- **L4** `Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)` → **[确定]** 替换 Gini delta 范围
- **L6** `$\Delta\mathcal{H} \in [-0.047, -0.040]$` → **[确定]** 替换 DeepSeek entropy delta 范围
- **L6** `$\Delta\mathcal{H} = +0.045$` → **[确定]** 替换 Qwen s025 entropy delta

### discussion.tex

- **L5** `$69$--$274{\times}$` → **[确定]** 替换 G 范围
- **L5** `$0.032$ vs.\ $0.818$ ... $7.196$ vs.\ $1.363$` → **[确定]** 替换 crossover 数值
- **L10** `\placeholder{ORACLE\_PCT}`, `\placeholder{ORACLE\_P}`, `\placeholder{HEUR\_PCT}`, `\placeholder{HEUR\_P}` → **[确定]** 填入 n=500 oracle/heuristic 结果
- **L10** `95\% CIs for both conditions span zero` → **[视结果]** n=500 后 CI 是否仍跨零
- **L15** `$d_z \geq 1.0$` → **[确定]** 替换 LLaMA within-importance d_z
- **L15** `${\sim}40{\times}$ smaller ... ${\sim}7{\times}$ smaller` → **[视结果]** magnitude ratios
- **L15** `Wilcoxon $p < \placeholder{}$` → **[确定]** 填入 LLaMA random p 值

### conclusion.tex

- **L4** `$69{\times}$ to $274{\times}$ ... ($d_z$: $0.44 \to 0.80$)` → **[确定]** 替换
- **L4** `($d_z \geq 0.55$)` → **[确定]** 替换 Qwen d_z 下界
- **L4** `at $\sim$1/40 the magnitude` → **[视结果]**

### limitations.tex

- **L1** `$d_z \sim 1.0$` → **[确定]** 替换 LLaMA d_z
- **L1** `$\sim$1/40 of DeepSeek` → **[视结果]**
- **L1** `$s{=}0.30$ significant after Bonferroni correction` → **[视结果]** n=500 可能更多 level 显著
- **L45** `$n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded)` → **[确定]** 替换 sample sizes
- **L46** `mean/median ratio ${\sim}1.6{:}1$` → **[确定]** 替换 skewness ratio
- **L46** `mean_diff=22.94, median_diff=14.59` (注释) → **[确定]** 替换注释中数值
- **L47** `CI lower bounds increasing from $0.19$ to $6.70$` → **[确定]** 替换 permutation CI bounds
- **L47** `$[6.70,\; 16.29]$` → **[确定]** 替换 s030 CI
- **L49** `$\widetilde{\Delta} = \placeholder{}$` → **[确定]** 填入

### appendix.tex

- **L38** `($G_{\times} = 58$--$241{\times}$)` → **[确定]** 替换 multiplicative null G 范围

### appendix_moved.tex

#### Crossover Details (L11)
- **L11** `$0.032$ vs.\ $0.818$ ... $7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal ... $3.9{\times}$ ... $5.4{\times}$ ... $5.3{\times}$ ... $3.6{\times}$` → **[确定]** 替换全部 crossover 数值

#### Cross-Model Details (L26)
- **L26** `Four of the 50 problems are excluded` → **[确定]** 替换排除数和总数
- **L26** `$n{=}46$ valid problems for Qwen (vs.\ $n{=}49$ for DeepSeek)` → **[确定]** 替换 sample sizes

#### Qwen Effective N (L30–46)
- **L30** `\placeholder{NULL\_PCT}` → **[确定]** 填入 null rate %
- **L35** `$n_{\text{total}} = \placeholder{N\_QW}$` → **[确定]** 填入 Qwen total n
- **L41–43** 12 个 `\placeholder{}` → **[确定]** 填入每 phase × sparsity 的 effective n

#### Cross-Model Table (L59)
- **L59** `0.39 & 1.48 & 7.16 & 14.59` → **[确定]** DeepSeek Δ values
- **L60** `0.04 & 0.23 & 1.27 & 2.94` → **[确定]** Qwen Δ values

#### Per-problem concordance (L73)
- **L73** `median $\rho = \placeholder{}$, $p = \placeholder{}$` → **[确定]** 填入（注释已有值 mean_rho=-0.107, p=0.926 但需 n=500 值）

#### Random eviction control (L76)
- **L76** `$\widetilde{\Delta} = \placeholder{}$` → **[确定]** 填入 Qwen random s030 median diff

#### Permutation Details (L84)
- **L84** `$1.2{\times}$ ($s{=}0.15$) to $1.6{\times}$ ($s{=}0.30$) ... $1.1{\times}$ to $1.4{\times}$` → **[确定]** 替换 skewness ratios

#### Permutation Table (L88, L99–102)
- **L88** `from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$ ... $0.19 \to 0.69 \to 1.66 \to 6.70$` → **[确定]** 替换
- **L93** caption: `$n{=}49$` → **[确定]** 替换
- **L99** `0.37 & $[0.19,\; 0.62]$ & 0.0032` → **[确定]** 替换
- **L100** `0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$` → **[确定]** 替换
- **L101** `3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$` → **[确定]** 替换
- **L102** `9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$` → **[确定]** 替换

#### Discrimination Metrics Table (L123–143)
- **L132–135** DeepSeek ΔGini: `-0.030, -0.040, -0.065, -0.081` 和 ΔCV: `-0.56, -0.77, -1.29, -1.66` → **[确定]** 替换
- **L137–140** Qwen ΔGini: `-0.010, -0.012, -0.010, -0.020` 和 ΔCV: `-0.05, -0.21, -1.49, -1.14` → **[确定]** 替换

#### Entropy Deltas Table (L163–183)
- **L171–174** DeepSeek ΔH: `-0.040, -0.047, -0.045, -0.044` → **[确定]** 替换
- **L177–180** Qwen ΔH: `-0.073, -0.076, +0.045, -0.007` → **[确定]** 替换

### appendix_results.tex

- **L7** `median $\rho = \placeholder{}$, $p = \placeholder{}$` → **[确定]** 填入（与 appendix_moved.tex L73 重复内容）
- **L10** `$\widetilde{\Delta} = \placeholder{}$` → **[确定]** 填入（与 appendix_moved.tex L76 重复内容）

### appendix_disc_analysis.tex

- **L11** `$\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ ... $0.006, 0.015, 0.032, 0.053$ ... $0.105$` → **[确定]** 替换 high-phase II medians
- **L14** `$\widetilde{\Delta} = \placeholder{}$` → **[确定]** 填入
- **L45** `$n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded)` → **[确定]** 替换
- **L46** `mean/median ratio ${\sim}1.6{:}1$` → **[确定]** 替换
- **L46** `mean_diff=22.94, median_diff=14.59` (注释) → **[确定]** 替换
- **L47** permutation CIs: `$[0.19,0.62]$, $[0.69,1.49]$, $[1.66,6.64]$, $[6.70,16.29]$` → **[确定]** 替换
- **L49** `$\widetilde{\Delta} = \placeholder{}$` → **[确定]** 填入
- **L57** `$\Delta$ growth rate $3.8{\times} \to 4.8{\times} \to 2.0{\times}$` (注释) → **[确定]** 替换

---

## 全局替换：样本量声明

| 文件 | 行号 | 当前文本 | 更新 |
|------|------|----------|------|
| abstract.tex | 6 | `using 50 MATH-500 problems` | → `500 MATH-500 problems` |
| methodology.tex | 10 | `We use 50 problems stratified from MATH-500` | → `500 problems` |
| results.tex | 13 | `$n{=}50$ MATH-500 problems` | → `$n{=}500$` |
| results.tex | 34 | `medians across 50 problems` | → `500 problems` |
| appendix_moved.tex | 26 | `Four of the 50 problems` | → 更新排除数和总数 |
| appendix_moved.tex | 26 | `$n{=}46$ ... $n{=}49$` | → n=500 valid counts |
| appendix_disc_analysis.tex | 45 | `$n{=}49$ ... $n{=}46$` | → 同上 |
| appendix_moved.tex | 93 | `$n{=}49$` | → n=500 permutation n |

---

## 全局替换："marginal at s=0.15" 删除

硬约束：n=500 Qwen s015 CI 不跨零，删除所有 "marginal" 限定语。

| 文件 | 行号 | 当前文本 | 操作 |
|------|------|----------|------|
| results.tex | 71 | `The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \geq 0.20$ ($d_z \geq 0.55$)` | 改写为在所有 sparsity level 均 reliable |
| results.tex | 106 | `the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \geq 0.20$ ($d_z \geq 0.55$)` | 同上 |
| results.tex | 117 | `\textsuperscript{ns}` 标注 | 删除 |
| results.tex | 122 | `\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \geq 0.20$.` | 删除整行脚注 |

---

## Placeholder 汇总

所有 `\placeholder{}` 在 n=500 数据到手后必须填入：

| 文件 | 行号 | Placeholder | 数据来源 |
|------|------|-------------|----------|
| abstract.tex | 8 | `\placeholder{}` (Qwen rand s030 Δ) | experiment_summary_table.json |
| results.tex | 71 | `\placeholder{NULL\_PCT}` | Qwen mid-phase null rate analysis |
| results.tex | 86 | `\placeholder{N\_LLAMA}` | LLaMA valid sample count |
| results.tex | 92–95 | 12× `\placeholder{}` (LLaMA table) | c3_llama n=500 |
| discussion.tex | 10 | `\placeholder{ORACLE\_PCT}`, `\placeholder{ORACLE\_P}` | oracle experiment |
| discussion.tex | 10 | `\placeholder{HEUR\_PCT}`, `\placeholder{HEUR\_P}` | heuristic experiment |
| discussion.tex | 15 | `\placeholder{}` (LLaMA random p) | c3_llama |
| appendix_moved.tex | 30 | `\placeholder{NULL\_PCT}` | Qwen null rate |
| appendix_moved.tex | 35 | `\placeholder{N\_QW}` | Qwen total valid n |
| appendix_moved.tex | 41–43 | 12× `\placeholder{}` | Qwen effective n per phase×sparsity |
| appendix_moved.tex | 73 | 2× `\placeholder{}` (ρ, p) | cross_model_analysis.json |
| appendix_moved.tex | 76 | `\placeholder{}` (Qwen rand Δ) | experiment_summary_table.json |
| appendix_results.tex | 7 | 2× `\placeholder{}` (ρ, p) | 同 appendix_moved L73 |
| appendix_results.tex | 10 | `\placeholder{}` (Qwen rand Δ) | 同 appendix_moved L76 |
| appendix_disc_analysis.tex | 14 | `\placeholder{}` (Qwen rand Δ) | 同上 |
| appendix_disc_analysis.tex | 49 | `\placeholder{}` (Qwen rand Δ) | 同上 |

---

## 图表更新

| 文件 | 行号 | 图表文件 | 操作 |
|------|------|----------|------|
| results.tex | 57 | `fig1_dose_response.pdf` | **[确定]** 用 n=500 数据重新生成 |
| appendix_moved.tex | 15 | `fig3_crossover.pdf` | **[确定]** 用 n=500 数据重新生成 |
| appendix_moved.tex | 67 | `fig5_crossmodel.pdf` | **[确定]** 用 n=500 数据重新生成 |
| appendix_moved.tex | 109 | `fig4_bootstrap.pdf` | **[确定]** 用 n=500 数据重新生成 |

文件名无需改变，直接覆盖即可。图表数据源需指向 n=500 experiment JSON。

---

## C8 限定语：LLaMA qualitative framing（D060）

n=500 后 LLaMA 仍仅做 qualitative 描述。以下位置需检查 framing 是否需调整：

| 文件 | 行号 | 内容 | 操作 |
|------|------|------|------|
| abstract.tex | 10 | LLaMA `mixed but directionally consistent evidence` | **[视结果]** n=500 后 evidence 可能更强，调整措辞 |
| introduction.tex | 15 | `partially extends ... qualitatively consistent but substantially weaker` | **[视结果]** 同上 |
| results.tex | 79 | `The evidence ... is mixed` | **[视结果]** n=500 后可能不再 "mixed" |
| results.tex | 81 | `${\sim}40{\times}$ smaller` 等 magnitude 比较 | **[视结果]** |
| discussion.tex | 15 | `partial support ... substantially weaker` | **[视结果]** |
| conclusion.tex | 4 | `partially extends ... substantially weaker trend at $\sim$1/40` | **[视结果]** |
| limitations.tex | 1–3 | LLaMA partial confirmation 措辞 | **[视结果]** |
| appendix_disc_analysis.tex | 33 | `partial confirmation` | **[视结果]** |

---

## C5b: §8 Mitigation / Future Work

| 文件 | 行号 | 内容 | 操作 |
|------|------|------|------|
| discussion.tex | 10 | Oracle/heuristic pilot 整段（placeholder 填入后） | **[确定]** 填入 n=500 oracle 结果，根据是否过 30% gate 调整措辞 |
| discussion.tex | 10 | `below the pre-registered 30\% gate` | **[视结果]** n=500 是否过 gate |
| discussion.tex | 10 | `95\% CIs for both conditions span zero` | **[视结果]** |

---

## Qwen Caveat: mid-phase null rate

| 文件 | 行号 | 内容 | 操作 |
|------|------|------|------|
| results.tex | 71 | `approximately \placeholder{NULL\_PCT}\% of problems yield near-zero II in mid-sparsity phase` | **[确定]** 填入 n=500 null rate；若 null rate 显著下降可能需要重写此段 |
| appendix_moved.tex | 30 | `\placeholder{NULL\_PCT}\%` | **[确定]** 同上 |
| appendix_moved.tex | 35 | `$n_{\text{total}} = \placeholder{N\_QW}$` | **[确定]** |

---

## 重复内容注意

以下文件包含重复段落，修改时必须同步：

1. **appendix_results.tex L7–10** 与 **appendix_moved.tex L73, L76** — per-problem concordance + random eviction control（完全相同的文字）
2. **appendix_disc_analysis.tex L14** 与 **abstract.tex L8** — Qwen random s030 Δ placeholder

---

## 注意事项

1. **onset threshold s≥0.15**：论文已统一使用 $s \in \{0.15, 0.20, 0.25, 0.30\}$，无需额外修改。但 n=500 后所有 s=0.15 的结论需验证——如果 n=500 在 s=0.15 效应更强，需删除 n=50 时的保守措辞。

2. **median only**：论文已全面使用 median。n=500 替换时继续使用 median，不要引入 mean。

3. **d_z within-importance only**：Tab 4 (cohens-d) 报告的 d_z 是 within-importance 的 low−high 配对效应。n=500 替换时保持此定义不变。

4. **注释中的 exp_id / source**：每个数值旁有 `% exp_id:` 注释标注数据来源。n=500 替换时需同步更新注释中的 exp_id 引用。

5. **数值精度**：当前论文中 II 值保留 3 位小数（如 0.006），d_z 保留 2 位（如 0.44），p 值用 < 0.005 或具体值。n=500 替换时保持同样精度。

6. **Bonferroni k=4**：permutation test 和 Wilcoxon test 的 Bonferroni correction 因子 k=4（4 个 sparsity level）。n=500 如果测试 level 数不变则无需改。

7. **文件同步方式**：tex 文件同步用 rsync，不是 git。修改后需 rsync 到服务器编译。

8. **appendix_results.tex 与 appendix_moved.tex 有重复段落**，必须确保一致性。建议后续检查是否可合并为一个文件。

9. **总计需替换的独立数值约 150+ 个**（含表格单元格）。建议按文件顺序逐文件执行，每改一个文件就编译一次检查排版。
