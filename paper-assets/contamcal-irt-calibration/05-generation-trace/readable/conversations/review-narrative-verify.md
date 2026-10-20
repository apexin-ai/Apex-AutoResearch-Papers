# review narrative verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/chats/worker_review_narrative-verify_20260517T213921.jsonl`
- **Structured JSON:** [`6dfac2db8406fdf34a30.json`](../../sessions/6d/6dfac2db8406fdf34a30.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

5 recorded events

### Tool call

_source line 1 · 2026-05-17T21:39:54.978832+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_narrative-verify_20260517T213921",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T21:39:54.979276+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection, resource allocation, and research priorities for large language models, yet training data contamination undermines the validity of these scores in ways that current evaluation cannot quantify \citep{hendrycks2021mmlu,chang2025benchmarking}. When models encounter test items during training, observed accuracy conflates genuine capability with memorization, and practitioners have no principled way to determine how much of a reported score reflects real understanding. The problem is compounded by the scale of modern training corpora: trillion-token web crawls make contamination pervasive and instance-level measurement infeasible \citep{oren2024proving}. Post-hoc calibration that quantifies contamination effects despite imperfect detection is therefore essential for trustworthy evaluation.
4	
5	Two developments make this gap urgent. First, \citet{sun2025emperor} systematically evaluate twenty contamination mitigation strategies (rephrasing, option shuffling, dynamic benchmark regeneration, and others) and demonstrate that none restores clean performance after contamination has occurred. This result forecloses the ``prevent contamination'' approach for models already trained on unrestricted web data. Second, contamination-free benchmarks \citep{white2024livebench} offer a partial solution but sacrifice the comparability and institutional knowledge accumulated around established benchmarks. Dynamic regeneration of test items may also be contaminated within weeks as web crawlers index benchmark repositories \citep{dong_2024_cdd}. The field therefore needs post-hoc statistical tools that can separate genuine ability from contamination artifacts on existing benchmarks.
6	
7	Detection methods such as Min-K\%++ \citep{zhang_2024_minkpp}, ConStat \citep{dekoninck2024constat}, and Kernel Divergence Signatures \citep{choi_2025_kds} can flag contaminated items but stop at detection. They d
…[truncated 3725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_narrative-verify_20260517T213921",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T21:39:54.979541+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_narrative-verify_20260517T213921",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T21:39:54.979816+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Calibration Quality}
5	\label{sec:calibration_results}
6	
7	\paragraph{Item filtering improves calibration.}
8	RRF-guided item filtering substantially improves IRT calibration quality over random item subsets. On a random 2000-item MMLU subset (same $J=13$ model set), vanilla 2PL achieves $\tau = 0.460$; on the 300-item RRF-selected subset, $\tau = 0.73$ ($\Delta\tau = 0.27$, controlled for model composition). Signal-guided filtering concentrates items where contamination effects are detectable, enabling sharper ability-dosage separation. Exclusion sensitivity analysis (removing 0--50\% of top-exposure items from random 2000-item subsets, $J=13$) yields $\tau$ ranging from 0.46 to 0.60 with no monotonic trend, and $\gamma$ remains non-significant at all exclusion rates. The $\tau$ improvement is not driven by item discrimination: mean $a_i$ does not differ between RRF-selected and random subsets (Cohen's $d = 0.098$, $p > 0.05$; $r_{\text{exposure}, a_i} = -0.013$).
9	
10	\paragraph{RRF vs.\ single-signal ablation.}
11	Replacing RRF with S1-only exposure for item selection and IRT fitting causes convergence failure: MMLU S1-only yields $\hat{R} = 1.53$ (ESS$=$7), while ARC S1-only converges to a degenerate solution ($\gamma = 6.84$, PPP$=$0.000). The root cause is exposure variance compression: S1-only top-300 items concentrate in a narrow score band ($[0.749, 0.867]$), creating collinearity between $\gamma \cdot e_{ij}$ and difficulty parameters. Multi-signal RRF fusion preserves broader exposure distributions that enable $\gamma$ identification. RRF's value is therefore not only signal quality aggregation but exposure variance for IRT parameter separability.
12	
13	\paragraph{Aggregate contamination effects are negligible.}
14	Table~\ref{tab:baselines} compares calibration on 300 RRF-filtered items ($J=16$). Raw accuracy achieves the lowest MAE (MMLU 0.006, ARC 0.007), outperforming all correction methods 
…[truncated 14347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_narrative-verify_20260517T213921",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-17T21:39:54.980252+00:00_

## 验证结果

### 1. Introduction C2 contribution — **存在 ✓**

第14行，contribution 列表第2条：

> "Single-signal item selection causes IRT convergence failure due to exposure variance compression, establishing multi-signal fusion as a necessary condition for $\gamma$ identifiability."

语义完全覆盖：(a) single-signal 选择 → (b) IRT convergence failure → (c) 原因是 exposure variance compression。措辞直接，无破折号滥用，无 -ing 结尾短语。"establishing" 在此处是分词做结果状语，属于学术论文常见句式，不属于 AI 风格的 -ing 结尾问题（后者指 "..., demonstrating the effectiveness of..." 这类空洞总结）。

### 2. Results pooled-vs-SocSci 显式对比 — **存在 ✓**

第66行，§5.4 Exploratory Domain Analysis 段落内：

> "In contrast to the pooled analysis where $\hat{\gamma}$ varies 2.6$\times$ across prior specifications (prior-dominated), Social Sciences $\hat{\gamma}$ varies only 1.2$\times$ ($-$0.43 to $-$0.51), confirming that the directional signal is data-dominated at this domain granularity."

语义完全覆盖：pooled γ 对 prior 敏感（2.6×，prior-dominated），Social Sciences γ 稳健（1.2×，data-dominated），有具体倍数和数值范围。

### 措辞质量评估

两处均自然流畅：
- 无解释性破折号（em-dash / en-dash）
- 无 -ing 短语结尾滥用
- 无 "Furthermore/Moreover/Additionally" 连续堆叠
- 无用词黑名单词汇
- 句式符合学术论文规范

无改进建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_review_narrative-verify_20260517T213921"
}
```

</details>

---
