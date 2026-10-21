# paper integrate ty fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_paper_integrate_ty_fix_20260516T002030.jsonl`
- **Structured JSON:** [`29142e210893489bf7b3.json`](../../sessions/29/29142e210893489bf7b3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-16T00:26:16.513305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/window_sensitivity_t11/window_sensitivity_fixed.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/window_sensitivity_t11/window_sensitivity_fixed.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T00:26:16.513620+00:00_

1	# Window Sensitivity Analysis — Bugfix Report (D044-A)
2	
3	## Pythia-410M, α=1.0, 4 seeds (42–45), T∈{5,6,7,8,9,10}
4	
5	Two bugs in `window_sensitivity.py` caused incorrect TY column values in the original D044-A report. The 4/5-method consensus conclusions (NX/DX/TH/PG) were unaffected because TY is not required for 4/5 majority.
6	
7	---
8	
9	## Bugs Fixed
10	
11	### Bug #1: Off-by-one in data slicing (line 193)
12	```python
13	# Before (wrong):  T=10 → 10 points (gen_0 to gen_9)
14	metrics = all_data[seed][:T]
15	
16	# After (correct): T=10 → 11 points (gen_0 to gen_10)
17	metrics = all_data[seed][:T+1]
18	```
19	Paper convention: "T=10 generations" = gen_0 through gen_10 = 11 data points.
20	
21	### Bug #2: Divergent TY implementation
22	`window_sensitivity.py` used a local `toda_yamamoto_v2` (hardcoded d=1, AIC-selected p, VAR `test_causality` chi²) which differed from the canonical `method_ablation.py` implementation (ADF-tested d_max, fixed p=1, manual OLS F-test). The local version returned `p=nan` at most window lengths due to VAR `test_causality` failing silently on short series.
23	
24	**Fix**: Imported `toda_yamamoto` from `method_ablation.py`, deleted local TY functions.
25	
26	---
27	
28	## Table 1: TY Consensus Before vs After (pairs with ≥3/4 seed sig)
29	
30	| T | Points (old→new) | TY sig old | TY sig new | NX/DX/TH/PG (unchanged) |
31	|---|---|---|---|---|
32	| 5 | 5→6 | 0/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |
33	| 6 | 6→7 | 0/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |
34	| 7 | 7→8 | 0/6 | 6/6 | 6/6, 6/6, 6/6, 6/6 |
35	| 8 | 8→9 | 3/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |
36	| 9 | 9→10 | 0/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |
37	| 10 | 10→11 | **0/6** | **4/6** | 6/6, 6/6, 6/6, 6/6 |
38	
39	**Root cause of old TY=0/6**: The buggy `toda_yamamoto_v2` returned `p=nan` for almost all seeds/windows because `VAR.test_causality()` silently fails when residual df is too low. The `nan` was then compared `< 0.05`, yielding False.
40	
41	---
42	
43	## Table 2: Full Consensus Summary (Fix
…[truncated 3368 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T00:26:16.513806+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T00:26:16.513942+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T00:26:16.514060+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T00:26:16.514175+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T00:26:16.514329+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T00:26:16.514463+00:00_

artifacts/dream_reports/dream_20260514T184925/best/paper.tex
artifacts/dream_reports/dream_20260514T184925/median/paper.tex
artifacts/dream_reports/dream_20260514T184925/worst/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/background.tex
docs/paper/background.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion_365dc4.tex
artifacts/_project/paper/abstract_8c6c62.tex
docs/paper/conclusion.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
artifacts/_project/paper/related_work.tex
docs/paper/related_work.tex
artifacts/_project/paper/discussion.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T00:26:16.514583+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper*/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper*/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T00:26:16.514703+00:00_

artifacts/_project/paper/experiments.tex
artifacts/_project/paper/background.tex
docs/paper/background.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion_365dc4.tex
artifacts/_project/paper/abstract_8c6c62.tex
docs/paper/conclusion.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
artifacts/_project/paper/related_work.tex
docs/paper/related_work.tex
artifacts/_project/paper/discussion.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T00:26:16.514835+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T00:26:16.515101+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper_framing.md\", \"content\": \"# Paper Framing — distrib_canary_collapse\\n\\n## Target Venue\\n- Primary: **EMNLP 2026 Main Track** (D043, 用户指定)\\n- ARR cycle: June 2026 (deadline ~June 15, 待确认具体日期)\\n- 格式: ACL 系列模板 (acl.sty), 8 页正文 + unlimited appendix\\n- Note: ARR May cycle 已过；June cycle 对齐 EMNLP 2026 commitment deadline\\n\\n## Narrative Structure (D027: Option B reframe)\\n\\n**主线**：方法论陷阱 + 多方法共识框架。Canary prediction 为系统性 case study。\\n**Claim 呈现顺序**：论文中 Claim 3 领衔 → Claim 2 (regime map) → Claim 1 (case study)。\\n**内部编号保持不变**（避免引用混乱），论文呈现时重排。\\n\\n## Core Claims (3 条，内部编号不变)\\n\\n1. **Canary→Diversity Granger-Causal Precedence (论文中作为 Case Study Finding)**: token_entropy 对 diversity 退化（distinct_1/2）具有 Granger-causal precedence——领先 1-2 代，差分后仍显著，证据来自多方法一致性：cross-correlation（lag=-1, std=0.0, |r|>0.99, p<0.004, 4/4 seed）、差分交叉相关（显著）、threshold onset（canary gen 1-2, diversity gen 3-4）、**permutation Granger（差分后仍 4/4 seed 显著，F=612-2615）**。论文可用措辞 (D037 更新)：*\\\"We demonstrate Granger-causal precedence of canary metrics at α≥0.75: α=1.0 achieves 24/24 FDR-sig (4 seeds), α=0.75 achieves 3/4 FDR-sig with the fourth borderline (p_fdr=0.054; single seed, pending multi-seed confirmation C001). Consistent temporal precedence (cross-correlation lag=+1, r=0.80–0.94) is observed across all contamination levels, though formal Granger tests at α≤0.50 do not reach FDR-corrected significance at T=11 (power analysis: §X).\\\"*升级上限：Granger ≠ true causality（Granger 1969），Discussion 一句话声明；双变量模型无法排除未观测混淆因子（详见 Reviewer Concerns 表）。ECE 在 cross-correlation 和 permutation Granger 下同样领先（差分后 4/4 SIG），但跨方法一致性弱于 token_entropy，地位为 conditional secondary canary 待 plan_006 确认（详见约束 #9）。注意：TY Granger 在 N=11 下不可用于区分真/伪关联（见 Claim 3），核心证据链基于多方法一致性而非单一 TY 背书。\\n2. **Regime-Dependent Predictability**: 可预测性取决于 collapse 维度和 contamination regime——canary→diversity 在差分后仍 robust（
…[truncated 15756 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T00:26:16.515315+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T00:26:16.515479+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Granger precedence is not causation.}
4	Granger causality tests whether past values of one series improve prediction of another beyond its own history; it does not establish true causation~\cite{granger1969investigating,shojaie2022granger}.
5	Bivariate Granger tests cannot exclude confounders: an unobserved process---such as a latent distributional shift in the training data---could independently drive both token entropy and diversity metrics, producing spurious lead-lag associations even when no direct relationship exists.
6	Our multi-method consensus framework inherits this limitation in full.
7	Throughout this paper, ``Granger precedence'' denotes predictive improvement in a time-series forecasting sense, not a causal mechanism.
8	This distinction is why we scope our central claim to ``token entropy Granger-precedes diversity collapse'' rather than asserting that token entropy \emph{causes} diversity collapse.
9	
10	\paragraph{Calibration scope and generalization.}
11	All FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\alpha \in \{0.0, 0.25, 0.50, 0.75, 1.0\}$).
12	Generalization to other model architectures, datasets, or training protocols requires independent validation.
13	The consensus framework's structure---multi-method agreement combined with multi-seed replication---is intended to be applicable beyond this specific setting, but the operating thresholds ($K{\geq}4/5$ methods, $S{\geq}3/4$ seeds) are empirically calibrated and may require re-tuning under different conditions.
14	For instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.
15	Our ongoing GPT-2-medium experiments represent a first step toward cross-ar
…[truncated 4560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T00:26:16.515615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T00:26:16.515818+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter autoregressive language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
10	
11	Our protocol follows the full-replacement paradigm of \citet{shumailov2024curse}.
12	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data; (2)~generate 5{,}000 synthetic samples from the fine-tuned model; (3)~fully replace the synthetic pool.
13	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.25, 0.50, 0.75, 1.00\}$.
14	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; other conditions use seed~42, with multi-seed replication in progress.
15	
16	We track two \emph{canary metrics}---cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}---and three \emph{downstream metrics}.
17	Canary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).
18	Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}) and perplexity.
19	We additionally evaluate effective rank and Self-BLEU as candidate canaries (\S\ref{sec:case_study}).
20	Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
21	
22	All hypothesis tests apply Benjamini--Hochberg (BH
…[truncated 15022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T00:26:16.515971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T00:26:16.516141+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	The experiments in \S\ref{sec:method_sensitivity}--\ref{sec:consensus_validation} reveal that lead-lag conclusions in iterative training collapse are fragile along multiple axes.
5	This section distills three methodological pitfalls (\S\ref{sec:pitfalls}), proposes a multi-method consensus framework to address them (\S\ref{sec:consensus}), and calibrates the framework's error rates using built-in experimental controls (\S\ref{sec:calibration}).
6	
7	
8	\subsection{Methodological Pitfalls in Lead-Lag Analysis}
9	\label{sec:pitfalls}
10	
11	We identify three pitfalls that, individually or in combination, can produce incorrect conclusions about temporal precedence in iterative training systems.
12	Each is documented below with representative data from our experiments; full results appear in \S\ref{sec:experiments}.
13	
14	\paragraph{Pitfall 1: Method sensitivity.}
15	Applied to the same data ($\alpha{=}1.0$, 4~seeds, 16 canary$\to$downstream pairs), five lead-lag detection methods yield FDR significance rates ranging from 100\% (naive cross-correlation) to 25\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\kappa{=}0.185$---poor agreement (\S\ref{sec:method_sensitivity}).
16	The spurious-signal rate---the fraction of pairs flagged by the most liberal method but not confirmed by the most conservative---is 75\% across all five methods and 62.5\% when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate.
17	This pitfall is dangerous because method choice alone can determine whether a lead-lag relationship is deemed present or absent.
18	In a literature where single-method analyses are the norm, the implicit assumption that method choice does not matter is demonstrably false.
19	
20	\paragraph{Pitfall 2: Spurious regression under shared trends.}
21	A single preprocessing decision---first-differencing to remove shared non-stationary trends---can eliminate an entire ana
…[truncated 8739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T00:26:16.516316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T00:26:16.516445+00:00_

1	\begin{abstract}
2	We demonstrate that lead-lag conclusions in iterative model collapse are determined more by method choice than by the data: naive cross-correlation yields 100\% significance (16/16 metric pairs), while Toda--Yamamoto Granger causality retains only 25\% (4/16), with inter-method agreement of $\kappa = 0.185$. We identify three methodological pitfalls---shared-trend confounding, short-series power loss, and threshold arbitrariness---that together inflate spurious-signal rates to 75\%. To replace single-method reporting, we introduce a multi-method consensus framework requiring agreement across ${\geq}4$ of 5 statistical tests with FDR correction, achieving 0\% false-positive and 0\% false-negative rates on reference extreme regimes. Applied to Pythia-410M across 4 seeds, 5 synthetic-data mixing ratios ($\alpha$), and 10 iterative training generations on WikiText-103, the framework reveals a sharp regime boundary: significant lead-lag relationships emerge at $\alpha{=}1.0$ (with preliminary single-seed evidence at $\alpha{=}0.75$), where token entropy Granger-causes diversity collapse with a one-generation lead ($|r| > 0.99$, 24/24 pairs significant, 0/24 in the reverse direction). Differencing eliminates all perplexity leads ($8/8 \to 0/8$) but preserves all diversity leads (24/24), confirming token entropy as a robust early-warning canary metric.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T00:26:16.516564+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T00:26:16.516717+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training language models on their own output across successive generations leads to progressive distribution degradation, a phenomenon variously termed model collapse~\cite{shumailov2024curse} or Model Autophagy Disorder~\cite{alemohammad2024mad}.
5	Tail modes vanish, lexical diversity narrows, and calibration deteriorates as each generation's output becomes the next generation's training data.
6	As large language models become ubiquitous content generators, the fraction of machine-generated text on the web grows steadily, making iterative training collapse---where models are unwittingly trained on the output of earlier model generations---a practical concern for the long-term stability of language model ecosystems.
7	
8	A natural follow-up question is whether cheap-to-compute statistics---\emph{canary metrics}---can provide early warning of impending collapse, analogous to early-warning signals for critical transitions in ecological and climate systems~\cite{scheffer2009early,scheffer2012anticipating}.
9	Several recent studies have pursued this direction: \citet{du2026geometric} informally observe that expected calibration error rises before accuracy degrades; SIGMA~\cite{sigma2026spectral} proposes spectral indicators of distributional shift; and DCES~\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.
10	Yet the statistical methodology underlying these lead-lag claims---whether a canary metric genuinely \emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends---has received little scrutiny.
11	
12	We identify four methodological deficiencies that pervade existing lead-lag analyses of iterative training collapse:
13	(1)~no differencing tests to rule out spurious regression arising from shared non-stationary trends---a well-known hazard when correlating co-trending time series;
14	(2)~no multi-method cross-validation---conclusions rest
…[truncated 6321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T00:26:16.516850+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T00:26:16.516973+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Lead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.
5	We demonstrated three pitfalls that undermine standard approaches: method choice alone swings FDR significance from 100\% to 25\% ($\kappa{=}0.185$), first-differencing exposes canary$\to$perplexity associations as entirely spurious ($F{\approx}0$, $p{=}0.99$), and regime dependence causes the same Granger test to shift from 24/24 to 0/8 significant pairs across contamination levels.
6	These findings establish that single-method, single-regime analyses---the current default---cannot reliably distinguish genuine temporal precedence from statistical artifacts.
7	
8	Our multi-method consensus framework addresses this fragility by requiring convergent evidence across ${\geq}4/5$ independent methods and ${\geq}3/4$ random seeds.
9	Calibrated on built-in experimental controls, the framework achieves 0\% false positive rate at the null control ($\alpha{=}0.0$) and 0\% false negative rate against ground-truth pairs at full contamination ($\alpha{=}1.0$), with four tiers of practical guidance scaling from exploratory screening to publication-grade claims.
10	
11	Applying the framework yields a concrete finding: token entropy serves as a one-generation-ahead canary for diversity collapse at $\alpha{=}1.0$ (with preliminary single-seed evidence at $\alpha{=}0.75$), with $|r|{>}0.99$ and complete directional asymmetry (0/24 reverse-direction FDR-significant pairs).
12	This result is deliberately scoped to lexical diversity, not model collapse broadly, since the perplexity channel proved entirely spurious under differencing.
13	
14	The methodological pitfalls we expose are not specific to our experimental setting---they arise from generic properties of short, non-stationary time series---and the consensus framework transfers directly to any domain where multiple detection methods can be applied in parallel.
15	Limitation
…[truncated 65 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T00:26:16.517097+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "window.sensitivity|FNR|33\\.3|25%.*Toda|underpowered|0/6|nan|false.negative",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Grep",
  "tool_args": {
    "pattern": "window.sensitivity|FNR|33\\.3|25%.*Toda|underpowered|0/6|nan|false.negative",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T00:26:16.517266+00:00_

artifacts/_project/paper/related_work.tex:32:(iv)~we treat method-selection sensitivity itself as a primary finding, showing that it is the dominant source of variation in existing lead-lag conclusions.
artifacts/_project/paper/experiments.tex:60:For canary$\to$diversity pairs at $\alpha{=}1.0$, both undifferenced and differenced permutation Granger tests yield unanimous FDR significance, with $F$-statistics \emph{increasing} after differencing---confirming genuine temporal precedence rather than shared-trend confounding.
artifacts/_project/paper/experiments.tex:74:At $\alpha{=}0.50$, correlation-based methods (naive, differenced, threshold) unanimously find significance while causal methods unanimously find non-significance (Figure~\ref{fig:consensus_heatmap}), the most extreme method$\times$regime divergence in our experiments.
artifacts/_project/paper/experiments.tex:120:Correlation-based methods unanimously find significance (Table~\ref{tab:method_comparison}) while causal methods unanimously find non-significance.
artifacts/_project/paper/experiments.tex:168:The consensus framework at $K{\geq}4/5$ achieves \textbf{FPR${=}$0\%}, matching the best individual methods while providing robustness against miscalibration of any single method (Table~\ref{tab:fpr_fnr}).
artifacts/_project/paper/experiments.tex:170:\paragraph{False negative rate.}
artifacts/_project/paper/experiments.tex:172:The consensus framework ($K{\geq}4/5$, $S{\geq}3/4$) recovers all~6 (\textbf{FNR${=}$0\%}).
artifacts/_project/paper/experiments.tex:173:Toda--Yamamoto alone yields FNR${=}$25\%, missing ECE$\to$distinct-2 and ECE$\to$distinct-3 due to Type~II errors at $T{=}10$.
artifacts/_project/paper/experiments.tex:174:We note a design asymmetry: FPR is validated on method-only data (single seed at $\alpha{=}0.0$), while FNR uses method$\times$seed joint data (4~seeds at $\alpha{=}1.0$).
artifacts/_project/paper/experiments.tex:176:Table~\ref{tab:fpr_fnr} reports the calibration results.
artifact
…[truncated 5574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T00:26:16.517500+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "window|appendix|sensitivity.*T=|robustness.*window",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Grep",
  "tool_args": {
    "pattern": "window|appendix|sensitivity.*T=|robustness.*window",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T00:26:16.517630+00:00_

artifacts/_project/paper/experiments.tex:20:Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
artifacts/_project/paper/experiments.tex:136:Permutation Granger tests (first-differenced) confirm all canary$\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\ref{app:distinct3}).
artifacts/_project/paper/experiments.tex:155:Of 16 canary$\to$downstream pairs tested at $\alpha{=}1.0$ (4 candidate canaries $\times$ 4 downstream metrics), \textbf{6 survive} the full consensus pipeline ($K{\geq}4/5$ methods, $S{\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\ref{app:distinct3} bring the total to~6).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T00:26:16.517745+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Toda.*Yamamoto|TY|toda.yamamoto",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "glob": "**/paper/**/*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Toda.*Yamamoto|TY|toda.yamamoto",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "glob": "**/paper/**/*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T00:26:16.517927+00:00_

artifacts/_project/paper/related_work.tex:48:The Toda--Yamamoto procedure addresses this by augmenting the VAR lag order by the integration order and testing only the original lags, yielding valid asymptotic inference regardless of cointegration structure.
artifacts/_project/paper/related_work.tex:51:Our framework applies five complementary methods---naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality, and Toda--Yamamoto Granger causality---and requires multi-method consensus before classifying a lead-lag relationship as robust, directly addressing the method-sensitivity problem that arises when any single test is taken in isolation.
artifacts/_project/paper/experiments.tex:54:The fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \textbf{16/16} (100\%), differenced cross-correlation \textbf{14/16} (87.5\%), threshold onset detection \textbf{9/16} (56.3\%), permutation Granger causality \textbf{6/16} (37.5\%), and Toda--Yamamoto Granger \textbf{4/16} (25.0\%).
artifacts/_project/paper/experiments.tex:56:The spurious-signal rate---the fraction of pairs detected by the most liberal method but not confirmed by the most conservative---is \textbf{75\%} across all five methods and \textbf{62.5\%} when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate (\S\ref{sec:consensus_validation}).
artifacts/_project/paper/experiments.tex:65:Toda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\max}$ (Figure~\ref{fig:differencing_dmax}b).
artifacts/_project/paper/experiments.tex:73:Permutation Granger and Toda--Yamamoto correctly find 0\%.
artifacts/_project/paper/experiments.tex:94:Toda--Yamamoto  & 0     & 37.5 & 0    & ---  & 59.4  & 0    \\
artifacts/_project/paper/experiments.tex:147:Its classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootst
…[truncated 9051 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T00:26:16.518059+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**/appendix*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**/appendix*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T00:26:16.518170+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T00:26:16.518359+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T00:26:16.518517+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Granger precedence is not causation.}
4	Granger causality tests whether past values of one series improve prediction of another beyond its own history; it does not establish true causation~\cite{granger1969investigating,shojaie2022granger}.
5	Bivariate Granger tests cannot exclude confounders: an unobserved process---such as a latent distributional shift in the training data---could independently drive both token entropy and diversity metrics, producing spurious lead-lag associations even when no direct relationship exists.
6	Our multi-method consensus framework inherits this limitation in full.
7	Throughout this paper, ``Granger precedence'' denotes predictive improvement in a time-series forecasting sense, not a causal mechanism.
8	This distinction is why we scope our central claim to ``token entropy Granger-precedes diversity collapse'' rather than asserting that token entropy \emph{causes} diversity collapse.
9	
10	\paragraph{Calibration scope and generalization.}
11	All FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\alpha \in \{0.0, 0.25, 0.50, 0.75, 1.0\}$).
12	Generalization to other model architectures, datasets, or training protocols requires independent validation.
13	The consensus framework's structure---multi-method agreement combined with multi-seed replication---is intended to be applicable beyond this specific setting, but the operating thresholds ($K{\geq}4/5$ methods, $S{\geq}3/4$ seeds) are empirically calibrated and may require re-tuning under different conditions.
14	For instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.
15	Our ongoing GPT-2-medium experiments represent a first step toward cross-ar
…[truncated 5874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T00:26:16.518660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T00:26:16.518887+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter autoregressive language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
10	
11	Our protocol follows the full-replacement paradigm of \citet{shumailov2024curse}.
12	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data; (2)~generate 5{,}000 synthetic samples from the fine-tuned model; (3)~fully replace the synthetic pool.
13	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.25, 0.50, 0.75, 1.00\}$.
14	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; other conditions use seed~42, with multi-seed replication in progress.
15	
16	We track two \emph{canary metrics}---cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}---and three \emph{downstream metrics}.
17	Canary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).
18	Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}) and perplexity.
19	We additionally evaluate effective rank and Self-BLEU as candidate canaries (\S\ref{sec:case_study}).
20	Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
21	
22	All hypothesis tests apply Benjamini--Hochberg (BH
…[truncated 17032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T00:26:16.519049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T00:26:16.519227+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	The experiments in \S\ref{sec:method_sensitivity}--\ref{sec:consensus_validation} reveal that lead-lag conclusions in iterative training collapse are fragile along multiple axes.
5	This section distills three methodological pitfalls (\S\ref{sec:pitfalls}), proposes a multi-method consensus framework to address them (\S\ref{sec:consensus}), and calibrates the framework's error rates using built-in experimental controls (\S\ref{sec:calibration}).
6	
7	
8	\subsection{Methodological Pitfalls in Lead-Lag Analysis}
9	\label{sec:pitfalls}
10	
11	We identify three pitfalls that, individually or in combination, can produce incorrect conclusions about temporal precedence in iterative training systems.
12	Each is documented below with representative data from our experiments; full results appear in \S\ref{sec:experiments}.
13	
14	\paragraph{Pitfall 1: Method sensitivity.}
15	Applied to the same data ($\alpha{=}1.0$, 4~seeds, 16 canary$\to$downstream pairs---4 candidate canaries $\times$ 4 downstream metrics, including candidates later excluded per \S\ref{sec:case_study}), five lead-lag detection methods yield FDR significance rates ranging from 100\% (naive cross-correlation) to 25\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\kappa{=}0.185$---poor agreement (\S\ref{sec:method_sensitivity}).
16	The spurious-signal rate---the fraction of pairs flagged by the most liberal method but not confirmed by the most conservative---is 75\% across all five methods and 62.5\% when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate.
17	This pitfall is dangerous because method choice alone can determine whether a lead-lag relationship is deemed present or absent.
18	In a literature where single-method analyses are the norm, the implicit assumption that method choice does not matter is demonstrably false.
19	
20	\paragraph{Pitfall 2: Spurious regression under shared trends.}
21	A si
…[truncated 9799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T00:26:16.519486+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex",
  "old_string": "The Toda--Yamamoto procedure returns \\texttt{insufficient\\_df} for all pairs at $T{\\leq}7$, confirming that its elevated FNR is a VAR parameter-overhead issue rather than a signal-strength problem.",
  "new_string": "The Toda--Yamamoto procedure produces valid test statistics at all window lengths ($T \\in \\{5, \\ldots, 10\\}$), but with unstable sensitivity---3/6 to 6/6 pairs reach significance depending on window length---confirming that its elevated FNR reflects limited residual degrees of freedom rather than absence of signal."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex",
    "old_string": "The Toda--Yamamoto procedure returns \\texttt{insufficient\\_df} for all pairs at $T{\\leq}7$, confirming that its elevated FNR is a VAR parameter-overhead issue rather than a signal-strength problem.",
    "new_string": "The Toda--Yamamoto procedure produces valid test statistics at all window lengths ($T \\in \\{5, \\ldots, 10\\}$), but with unstable sensitivity---3/6 to 6/6 pairs reach significance depending on window length---confirming that its elevated FNR reflects limited residual degrees of freedom rather than absence of signal."
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T00:26:16.519647+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T00:26:16.519778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex",
  "offset": "24",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex",
    "offset": "24",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T00:26:16.519903+00:00_

24	\paragraph{Short time-series constraint.}
25	With $T{=}10$ generation cycles (11 data points per series), our time-series analyses operate near the lower bound of what standard methods require.
26	This series length is typical for iterative training studies, where each generation involves a complete training run, but it severely limits statistical power.
27	The Toda--Yamamoto procedure's elevated FNR (33.3\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.
28	This finding aligns with \citet{boettiger2012limits}, who demonstrated that early-warning signals have limited detection power in short time series.
29	Longer generation chains would improve power for all methods but impose substantial computational cost; this trade-off between statistical power and compute budget is inherent to iterative training research and cannot be resolved by methodological improvements alone.
30	However, observation window sensitivity analysis provides reassurance: the $4/5$ consensus classification stabilizes at $T{\geq}5$, well below our observation window of $T{=}10$, with identical results from $T{=}5$ through $T{=}10$.
31	The Toda--Yamamoto procedure produces valid test statistics at all window lengths ($T \in \{5, \ldots, 10\}$), but with unstable sensitivity---3/6 to 6/6 pairs reach significance depending on window length---confirming that its elevated FNR reflects limited residual degrees of freedom rather than absence of signal.
32	
33	\paragraph{Diversity--calibration dissociation.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_integrate_ty_fix_20260516T002030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-16T00:26:16.520072+00:00_

Edit confirmed. Now let me verify consistency with paper_framing.md constraints.

## Summary of analysis

**Modified files:**
- `docs/paper/discussion.tex` line 31 — Replaced incorrect claim that TY returns `insufficient_df` for all pairs at T≤7 with the corrected window sensitivity results (TY produces valid statistics at all T∈{5,...,10}, 3/6 to 6/6 pairs significant).

**No changes needed in the following (verified):**

| Item | Location | Why unchanged |
|------|----------|--------------|
| TY 4/16 (25%) | experiments.tex:54, method.tex:15, intro:24 | From method_ablation.py (canonical impl), not window_sensitivity |
| TY 59.4% at α=1.0 | experiments.tex:97 (method_comparison table) | Same — canonical impl |
| TY FNR 33.3% (2/6) | experiments.tex:178, method.tex:103, discussion.tex:27 | Still correct: ECE→d2 and ECE→d3 still miss at 3/4 seed threshold (2/4 seeds) even with the fix |
| TY FNR 25% in FPR/FNR table | experiments.tex:196 | Correct (33.3%) |
| Tier 4 FNR 50% | method.tex:67,81 | Still correct: ECE→d1 at 3/4 seeds still fails 4/4 |
| 4/5 consensus = 6/6 robust | discussion.tex:30, experiments passim | Confirmed unchanged: fix report Table 2 shows 6/6 robust at every T∈{5,...,10} |
| Spurious-signal rate 75%/62.5% | experiments.tex:56, method.tex:16 | Unaffected — based on pair-level method_ablation results |
| ECE "conditional secondary" | experiments.tex:150-153 | Still correct: TY Type II errors still drive the "secondary" label |

**Consistency with paper_framing.md:**
- Constraint #15 (TY 降级为辅助指标): ✓ No claim strength change
- Constraint #8 (TY 在 N=11 下不可靠): ✓ Narrative preserved — "limited residual degrees of freedom"
- Constraint #11 (统计效力须显式论证): ✓ The updated line still explicitly acknowledges TY's power limitation

**Pre-existing issue flagged (not related to this fix):** `artifacts/_project/paper/experiments.tex:173,191` reports TY FNR as 25% instead of 33.3% (inconsistent with its own discussion.tex:27 and with the `docs/paper/` version). This predates the window_sensitivity fix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_integrate_ty_fix_20260516T002030"
}
```

</details>

---
