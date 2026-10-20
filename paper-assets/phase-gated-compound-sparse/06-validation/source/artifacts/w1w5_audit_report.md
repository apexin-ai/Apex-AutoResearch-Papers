# W1-W5 Reviewer Warning Audit Report

**Date**: 2026-05-14
**Remote tex path**: `/root/autodl-tmp/pacs/paper/`
**Status**: Read-only audit — no files modified

---

## W1: 本地→远程 tex 同步

**状态: PASS — 远程 tex 已包含 S5.5 LLaMA 内容，无需同步**

远程 results.tex L71-98 包含完整的 `\subsection{Cross-Architecture Validation}`，含 Table `tab:llama-cross-arch`（4 个 sparsity level 的 d_z、CI、p_Bonf）。以下文件均已引用 LLaMA 结果：

| 文件 | 行号 | 内容摘要 |
|------|------|---------|
| abstract.tex | L10 | "on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing d_z..." |
| conclusion.tex | L4 | "partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B" |
| discussion.tex | L10-11 | "Architecture-dependent magnitude" paragraph |
| limitations.tex | L2 | "Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B... partially extends..." |
| appendix_disc_analysis.tex | L33 | "Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B... provides partial support" |

**依赖 n=500**: 否

---

## W2: S5.5 LLaMA selective reporting

**文件**: `results.tex`
**行号**: L74 (S5.5 Cross-Architecture Validation prose)
**严重性**: Medium — table data is complete, but prose cherry-picks favorable evidence

### 当前文本 (L74)

```latex
At $s{=}0.15$, paired Cohen's $d_z{=}0.19$ with bootstrap 95\% CI $[0.002, 0.043]$
excluding zero, indicating a small but detectable strategy contrast even at the
lowest sparsity. The effect size increases monotonically across sparsity levels
($d_z$: $0.19 \to 0.26 \to 0.29 \to 0.34$), with the largest effect at
$s{=}0.30$ ($d_z{=}0.34$, $\widetilde{\Delta}{=}0.356$, CI $[-0.069, 0.544]$).
```

### 问题分析

| s | CI | CI含零? | p_Bonf | 显著? | 正文叙述问题 |
|---|----|---------|----|-------|---------|
| 0.15 | [0.002, 0.043] | 不含 | 0.219 | NO | 称"excluding zero"暗示显著，**未提 p=0.219** |
| 0.20 | [-0.090, 0.187] | 含零 | 0.253 | NO | 未单独讨论 |
| 0.25 | [-0.004, 0.303] | 含零 | 0.083 | NO | 未单独讨论 |
| 0.30 | [-0.069, 0.544] | 含零 | **0.029** | YES | 提了 CI 但**未注明含零**，**未提 p 显著** |

abstract.tex L10 也 cherry-pick 了 s=0.30 的 p_Bonf=0.029 作为 LLaMA 证据。

### 建议修复文本

**替换 results.tex L74** (从 "At $s{=}0.15$" 到 "CI $[-0.069, 0.544]$).")：

```latex
Table~\ref{tab:llama-cross-arch} reports the full results. The evidence for a
strategy contrast on LLaMA is mixed: at $s{=}0.15$, the bootstrap CI excludes
zero ($[0.002, 0.043]$) but the Bonferroni-corrected Wilcoxon test is
non-significant ($p_{\text{Bonf}}{=}0.219$); conversely, at $s{=}0.30$ the CI
spans zero ($[-0.069, 0.544]$) while the Wilcoxon test reaches significance
($p_{\text{Bonf}}{=}0.029$). At intermediate levels ($s \in \{0.20, 0.25\}$),
neither CI nor Wilcoxon reaches significance. The effect size increases
monotonically ($d_z$: $0.19 \to 0.34$), consistent with a genuine but weak
trend---partially confirming the cross-architecture hypothesis while
underscoring the substantially weaker interaction on LlamaForCausalLM.
```

**替换 abstract.tex L10** (cherry-picked p=0.029 部分)：

```latex
and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically
increasing $d_z$ ($0.19 \to 0.34$) provides mixed but directionally consistent
evidence for cross-architecture generalization, though at ${\sim}$1/40 the
absolute magnitude and with substantially weaker interaction than in Qwen2-based
architectures.
```

**依赖 n=500**: 否 (LLaMA data from c3_llama, unaffected by n=500)

---

## W3: [CRITICAL] LLaMA 跨架构 framing 矛盾

**严重性**: CRITICAL — 论文 limitations/appendix 措辞暗示 cross-architecture validation 尚不充分，与 c3_llama D060 partially_confirmed 结果不一致

### 审查结果

远程 tex 已**部分更新**，不再有原始的"cross-architecture validation is needed"写法。但两处措辞仍需加强对 D060 partially_confirmed 的承认。

### 位置 1: appendix_disc_analysis.tex L33

**当前文本**:
```latex
Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM,
\S\ref{sec:cross-arch}) provides partial support: the directional pattern is
qualitatively consistent but the interaction magnitude is substantially weaker than
in Qwen2-based architectures, and random pruning also exhibits a non-trivial phase
gradient on LLaMA. Further validation on more diverse architectures (e.g., Mistral,
multi-latent attention architectures) is needed to establish the generality of the
full interaction.
```

**建议修复文本**:
```latex
Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B
(LlamaForCausalLM, \S\ref{sec:cross-arch}) shows qualitatively consistent
within-importance phase gradients ($d_z \sim 1.0$) but a substantially weaker
strategy $\times$ phase interaction than in Qwen2-based architectures; random
pruning also exhibits a non-trivial phase gradient on LLaMA, reducing the
strategy contrast. This partial confirmation ($s{=}0.30$ Wilcoxon
$p_{\text{Bonf}}{=}0.029$; $s \leq 0.25$ non-significant) suggests the
qualitative pattern may generalize but quantitative impact is
architecture-dependent. Comprehensive cross-architecture validation across more
diverse designs (e.g., Mistral, multi-latent attention architectures) and scales
remains an important next step.
```

### 位置 2: limitations.tex L2

**当前文本**:
```latex
All experiments are conducted at the 7B parameter scale. Whether the phase-modulated
severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains
untested. Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B
(LlamaForCausalLM, \S\ref{sec:cross-arch}) partially extends the findings beyond the
Qwen2 architecture: the directional pattern is qualitatively consistent but the
interaction magnitude is substantially weaker and random pruning also exhibits a
non-trivial phase gradient on LLaMA. The qualitative pattern has been tested on only
two architecture families at the 7--8B scale; further validation on larger models and
more diverse architectures (e.g., Mistral, multi-latent attention) is needed.
```

**建议修复文本**:
```latex
All experiments are conducted at the 7--8B parameter scale. Whether the
phase-modulated severity patterns persist, amplify, or attenuate at larger scales
(e.g., 70B) remains untested. Preliminary cross-architecture validation on
DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially
confirms the qualitative pattern beyond the Qwen2 architecture---monotonically
increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with
substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed
statistical evidence (only $s{=}0.30$ significant after Bonferroni correction).
The pattern has been tested on two architecture families (Qwen2ForCausalLM,
LlamaForCausalLM); comprehensive validation across more diverse architectures
(e.g., Mistral, multi-latent attention) and larger scales is needed for full
generalization claims.
```

### 其他已检查位置 (无需修改)

| 文件 | 行号 | 状态 |
|------|------|------|
| conclusion.tex | L4 | OK — "partially extends cross-architecture" 措辞恰当 |
| discussion.tex | L10-11 | OK — "Architecture-dependent magnitude" 段落详细讨论 LLaMA |
| appendix_disc_analysis.tex | L17 | OK — 讨论 entropy 跨架构，属机制层面 |

**依赖 n=500**: 否

---

## W4: Bootstrap B 值声明不一致

**文件**: `methodology.tex`
**行号**: L22
**严重性**: Medium — reported numbers are correct (from B=10,000 rebootstrap), but methodology statement is misleading

### 当前文本 (methodology.tex L22)

```latex
All confidence intervals and significance tests use nonparametric bootstrap
($B{=}10{,}000$)~\cite{efron-1993}. Paired bootstrap controls for problem-level
variance. All tests yield $p_{\text{Bonf}} < 0.005$ at every sparsity level.
```

### 代码证据

| 阶段 | B 值 | 代码位置 |
|------|------|---------|
| Profiling | **1,000** | `profiling/run_profiling.py:50` → `N_BOOTSTRAP = 1000` |
| Profiling outputs | **1,000** | 40+ `profiling_output_*/profiling_results.json` → `"n_bootstrap": 1000` |
| Post-hoc analysis | **10,000** | `analyze_c3_llama.py:25` → `B_BOOTSTRAP = 10000` |
| Post-hoc analysis | **10,000** | `analysis/bootstrap_per_problem.py` → `n_bootstrap=10000` |
| Dedicated rebootstrap | **10,000** | `analysis/rebootstrap_importance_b10000.py` (filename is self-documenting) |

论文报告的 CI 来自 post-hoc rebootstrap (B=10,000)，数值本身正确。但 "All confidence intervals... use B=10,000" 暗示整个流水线都用 B=10,000，而实际 profiling 用 B=1,000 后 rebootstrap 到 10,000。

### 建议修复文本

**替换 methodology.tex L22**:
```latex
All reported confidence intervals and significance tests use nonparametric
bootstrap ($B{=}10{,}000$)~\cite{efron-1993}; initial profiling uses $B{=}1{,}000$
for computational efficiency, with all reported statistics recomputed at
$B{=}10{,}000$. Paired bootstrap controls for problem-level variance. All tests
yield $p_{\text{Bonf}} < 0.005$ at every sparsity level.
```

### 补充位置: appendix_disc_analysis.tex L45

**当前文本**:
```latex
Bootstrap confidence intervals use $B{=}10{,}000$ resamples.
```

**建议修复**:
```latex
Bootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from
initial $B{=}1{,}000$ profiling runs).
```

**依赖 n=500**: 否 (but n=500 profiling should use same B strategy)

---

## W5: Qwen mid-phase null rate 未披露

**严重性**: Medium — missing per-phase effective sample sizes may mask data sparsity in mid-phase

### 当前披露

| 文件 | 行号 | 内容 |
|------|------|------|
| appendix_moved.tex | L26 | "Four of the 50 problems are excluded due to degenerate phase assignments, yielding n=46 valid problems for Qwen (vs. n=49 for DeepSeek)." |
| methodology.tex | L18 | "each sequence is segmented into three phases... with min_phase_length=10" |

### 未披露内容

- Per-phase effective sample sizes (每个 phase 有多少 problem 有有效数据)
- Mid-phase null rate (多少 problem 的 mid-phase 被判为 degenerate 或过短)
- 不同 sparsity level 下 per-phase 有效样本数是否不同

### 建议添加位置

**首选**: appendix_moved.tex L26 之后 (Cross-Model Replication Details section)

```latex
Per-phase effective sample sizes vary because the quantile-based segmentation
can produce degenerate phases (fewer than \texttt{min\_phase\_length}$=$10
tokens). Table~\ref{tab:per-phase-n} reports the effective $n$ by model, phase,
and sparsity level.

\begin{table}[t]
\centering
\small
\caption{Per-phase effective sample sizes. Columns show the number of problems
with $\geq$10 tokens in each phase.}
\label{tab:per-phase-n}
\begin{tabular}{@{}llccc@{}}
\toprule
Model & $s$ & $n_{\text{low}}$ & $n_{\text{mid}}$ & $n_{\text{high}}$ \\
\midrule
DeepSeek & all & [TBD] & [TBD] & [TBD] \\
Qwen & all & [TBD] & [TBD] & [TBD] \\
LLaMA & all & [TBD] & [TBD] & [TBD] \\
\bottomrule
\end{tabular}
\end{table}
```

[TBD] values must be extracted from profiling outputs — ideally from n=500 data once available.

**依赖 n=500**: **YES** — n=500 data will change per-phase effective sample sizes; should report final numbers

---

## 汇总

| Warning | 严重性 | 文件:行号 | 依赖 n=500 | 状态 |
|---------|--------|-----------|-----------|------|
| W1 | — | 多文件 | 否 | PASS: 远程 tex 已包含 LLaMA |
| W2 | Medium | results.tex:L74, abstract.tex:L10 | 否 | NEEDS FIX: prose cherry-picks CI/p evidence |
| W3 | **CRITICAL** | appendix_disc_analysis.tex:L33, limitations.tex:L2 | 否 | NEEDS FIX: 需加强 D060 partially_confirmed 表述 |
| W4 | Medium | methodology.tex:L22, appendix_disc_analysis.tex:L45 | 否 | NEEDS FIX: 需说明 profiling B=1000 -> rebootstrap B=10000 |
| W5 | Medium | appendix_moved.tex:L26 (新增) | **YES** | NEEDS DATA: 缺 per-phase effective sample sizes |

**建议执行顺序**: W3 (CRITICAL) -> W2 -> W4 -> W5 (等 n=500 数据)
