# Director coordination — Part 3 of 7

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../director-coordination.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/3d/3daf92a3dbeb151a5ec1.json)

## Round 50

### Tool result

_source line 519 · 2026-05-22T05:19:33.320390+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues and \citet{oren2024proving} prove contamination through exchangeability tests. Performance-based detectors identify contamination through statistical anomalies \citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique,deng2024investigating}. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (\Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} assessed test set discriminability, and \citet{rodriguez2021evaluation} demonstrat
…[truncated 3838 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-22T05:19:33.421460+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-22T05:19:33.873932+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\enlargethispage{2\baselineskip}
4	
5	\subsection{Implications for Benchmark Temporal Comparability}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF decomposes benchmark differences into three layers: (1)~\emph{impact}---ability differences removed by matching ($\sim$2.4~pp); (2)~\emph{DIF}---item-level differences after ability control ($\sim$28--29\% floor, 92.4\% item-specific); (3)~\emph{attribution}---contamination, capability evolution, or methodology shifts, underdetermined without training data. Regardless of attribution, temporal DIF means the same score carries different meaning across model generations.
10	
11	\subsection{Ground Truth Meta-Critique}
12	\label{sec:disc_groundtruth}
13	
14	\looseness=-1
15	The near-independence between DIF flags and web-overlap labels (\Cref{sec:groundtruth}) reflects a category error: web-overlap measures global exposure, while DIF measures differential functioning, making overlap-based labels an inappropriate ground truth for a differential method. Semi-synthetic dose-response confirms detection works when present; the disconnect is in the ground truth.
16	
17	\subsection{Recommended DIF Audit Protocol}
18	\label{sec:disc_protocol}
19	
20	\looseness=-1
21	We propose running temporal MH-DIF whenever $\geq 500$ new models accumulate ($N \geq 80$ suffices per \Cref{sec:validation}; 500 ensures family diversity). Empirical $\rho$ degradation simulation---DIF-ordered versus random item removal across six benchmarks---grounds graduated thresholds:
22	(1)~\emph{Monitor} (C\% $< 15\%$): $\Delta\rho < 0.001$ vs.\ random on all benchmarks; report C\% in release notes.
23	(2)~\emph{Flag} ($15$--$25\%$): $\Delta\rho = 0.001$--$0.003$ on 4/6 benchmarks; report stable-item rankings alongside full rankings.
24	(3)~\emph{Act} (C\% $\geq 25\%$): WinoGrande drops below $\rho = 0.995$ at 25\% DIF-ordered removal; review flagged item content, cross-reference with contamination i
…[truncated 342 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-22T05:19:33.874465+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-22T05:19:34.025352+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-1
5	Cross-subject matching ($\Delta\mathrm{FPR} = 0.000$) resolves the validation gap: web-overlap labels are near-independent of DIF flags (enrichment $\approx 0.96$). Across six benchmarks, 17.9--31.3\% of items exhibit temporal instability associated with item properties; LLM benchmarks need psychometric monitoring alongside score reporting.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-22T05:19:34.126238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-22T05:19:34.177023+00:00_

1	\section*{Limitations}
2	
3	\paragraph{Methodological scope.}
4	MH-DIF detects only uniform DIF; logistic regression reveals an additional 24.8\% non-uniform DIF, making 31\% conservative. More fundamentally, DIF detects \emph{that} items function differently but cannot determine \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts. A definitive causal decomposition remains out of reach without access to model training data. The semi-synthetic framework uses binary response flipping (incorrect $\to$ correct) to simulate differential contamination, representing a worst-case uniform exploitation pattern. Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages; detection power under such realistic patterns is untested. The moderate $\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$ reflects sensitivity to severe differential behavior; the framework's primary methodological contribution---cross-subject matching achieving $\Delta\mathrm{FPR} = 0.000$---is a matching strategy property independent of injection realism.
5	
6	\paragraph{Examinee non-independence.}
7	The MH $\chi^2$ test assumes independent examinees, yet LLMs sharing base models, training data, or architectures violate this assumption. Empirical mitigations partially address this: permutation simulation bounds LD-attributable FPR inflation to ${<}0.001$~pp, and graduated de-duplication ($K{=}20$: C\% $= 29.1\%$) shows family structure does not inflate results. \citet{french2010hierarchical} show that MH maintains nominal size under moderate clustering in educational settings, consistent with our empirical findings; however, the extreme relatedness of some LLM families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in that work. Cluster bootstrap resampling at the family level (29 families with $\geq$3 members, 1{,}882 models, $B = 1{,}000$) yields a 95\% CI of $[26.7\%, 53.2\%]$, $3.1
…[truncated 1341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-22T05:19:50.492730+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-22T05:19:52.350674+00:00_

1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini
…[truncated 8202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 1857
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-22T05:19:53.053919+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper && pdfinfo ../artifacts/review_round_5/submitted.pdf 2>/dev/null | grep -i \"pages\" || echo \"NO_PDFINFO\"; wc -l sections/*.tex",
  "description": "Check PDF page count and tex file sizes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper && pdfinfo ../artifacts/review_round_5/submitted.pdf 2>/dev/null | grep -i \"pages\" || echo \"NO_PDFINFO\"; wc -l sections/*.tex",
    "description": "Check PDF page count and tex file sizes"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-22T05:19:53.154782+00:00_

Pages:           14
    3 sections/abstract.tex
  121 sections/appendix.tex
    5 sections/conclusion.tex
   25 sections/discussion.tex
  117 sections/experiments.tex
   27 sections/introduction.tex
   13 sections/limitations.tex
   58 sections/method.tex
   14 sections/related_work.tex
  383 total
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_director_870d8ac6

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-22T05:20:06.364923+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-22T05:20:06.416049+00:00_

# Review Issues Tracker — irt_equated_bench_regen
# Round 10 (Fresh review, 2026-05-22)
# R1: 3.5, R2: 3.5 → Consensus 3.5 (Borderline Conference)

# ============================================================
# CRITICAL ISSUES
# ============================================================

- id: "R1-W1"
  summary: "因果归因空白使 audit protocol 不可安全执行"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 10
  mentions:
    - round: 5
      reviewers: [1, 2]
      note: "标题 'Psychometric Instability' 过强"
    - round: 8
      reviewers: [1, 2]
      note: "问题范围扩大：31% DIF 可能主要反映 genuine capability change。"
    - round: 9
      reviewers: [1, 2]
      note: "§5.3 'rotate or retire' 与 §4.6 discriminative signal 矛盾。"
    - round: 10
      reviewers: [1, 2]
      note: "§5.3 已改为 'investigate and report'，但缺乏具体可执行步骤。15%/25% 阈值缺乏 LLM 实证依据。"
  action_items:
    - round: 10
      action: "MF2 ρ degradation simulation 为阈值提供实证依据；§5.3 每个 action level 写具体步骤"
      assigned_to: agent+paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "RD2-W3"
  summary: "ρ≈0.997 practical significance paradox——'instability' 叙事被排名保持所削弱"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 2
  last_seen_round: 10
  mentions:
    - round: 8
      reviewers: [1, 2]
      note: "需更强调 family-level 和 pairwise 层面影响。"
    - round: 9
      reviewers: [1, 2]
      note: "需 6 benchmark ρ 值 + family-level profiles + pairwise flip rate + item 冗余度讨论。"
    - round: 10
      reviewers: [1, 2]
      note: "Table 3 已增加 ρ/τ/flip rate。缺具体 worked example 论证 practitioners 为何应关心。"
  action_items:
    - round: 10
      action: "MF1 worked example 从 plan_032 数据提取 pairwise flip 案例，写入 §4.6"
      assigned_to: agent+paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

# ============================================================
# WARNING ISSUES
# ======================================
…[truncated 11156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-22T05:20:28.320841+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-22T05:20:50.187930+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21867
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-22T05:20:50.339914+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你负责审查**方法严谨性 + 实验可靠性**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ACL Rolling Review May cycle)\n- **类别**: Long Paper (正文 ≤8 页，参考文献不限)\n- **模板**: ACL style template, `[review]` 模式\n- **匿名**: Double-blind\n- **Deadline**: 2026-05-25\n- **评分标准**: Overall Assessment 1-5 分 (3.5 = Borderline Conference, 4 = Conference)\n\n## 论文路径\n- LaTeX: `projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/submitted.pdf`\n\n## 论文概要\n题目: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n\n将 MH-DIF (Mantel-Haenszel Differential Item Functioning) 应用于 METABENCH 5,227 模型 × 12,508 MMLU items 的 response matrix，发现 31% items 在 2023 vs 2024 cohorts 间存在 ETS-C 级别 DIF。提出 cross-subject matching 消除 FPR 膨胀，semi-synthetic injection 验证检测力，并在 6 个 benchmark 上复制。\n\n## 你的审查侧重\n\n1. **MH-DIF 方法适用性**：MH 假设（条件独立、单维性）在 LLM 场景是否充分处理？quintile-based stratification 是否足够？\n2. **Semi-synthetic framework 有效性**：binary flipping 作为 contamination 模拟的生态效度；ΔTPR 作为 upper-bound 的讨论是否充分？\n3. **Cross-subject matching 的 ΔFPR=0.000 声明**：是否有适当限定（single-subject vs multi-subject）？bootstrap CI 的构造是否正确？\n4. **Structural controls 的完备性**：6 种 alternative explanations 是否足够排除 confounds？matched-ability 分析、IRT θ-conditioning、within-subject DIF 三重验证是否严密？\n5. **统计推断**：样本非独立性（model family clustering）对 χ² 检验的影响；多重比较校正；置信区间宽度\n6. **Cross-benchmark replication**：6 benchmark 结果的一致性和差异是否有合理解释？\n7. **Downstream impact 分析**：ρ≈0.997 与 family-level rank shifts 的表面矛盾是否充分讨论？\n\n请按 ARR review form 结构输出：Summary → Strengths → Weaknesses (逐条编号 W1, W2, ...) → Questions → Missing References → Overall Assessment + Confidence。Weaknesses 按严重程度排序（Must-Fix → Should-Fix → Minor）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你负责审查**方法严谨性 + 实验可靠性**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ACL Rolling Review May cycle)\n- **类别**: Long Paper (正文 ≤8 页，参考文献不限)\n- **模板**: ACL style template, `[review]` 模式\n- **匿名**: Double-blind\n- **Deadline**: 2026-05-25\n- **评分标准**: Overall Assessment 1-5 分 (3.5 = Borderline Conference, 4 = Conference)\n\n## 论文路径\n- LaTeX: `projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/submitted.pdf`\n\n## 论文概要\n题目: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n\n将 MH-DIF (Mantel-Haenszel Differential Item Functioning) 应用于 METABENCH 5,227 模型 × 12,508 MMLU items 的 response matrix，发现 31% items 在 2023 vs 2024 cohorts 间存在 ETS-C 级别 DIF。提出 cross-subject matching 消除 FPR 膨胀，semi-synthetic injection 验证检测力，并在 6 个 benchmark 上复制。\n\n## 你的审查侧重\n\n1. **MH-DIF 方法适用性**：MH 假设（条件独立、单维性）在 LLM 场景是否充分处理？quintile-based stratification 是否足够？\n2. **Semi-synthetic framework 有效性**：binary flipping 作为 contamination 模拟的生态效度；ΔTPR 作为 upper-bound 的讨论是否充分？\n3. **Cross-subject matching 的 ΔFPR=0.000 声明**：是否有适当限定（single-subject vs multi-subject）？bootstrap CI 的构造是否正确？\n4. **Structural controls 的完备性**：6 种 alternative explanations 是否足够排除 confounds？matched-ability 分析、IRT θ-conditioning、within-subject DIF 三重验证是否严密？\n5. **统计推断**：样本非独立性（model family clustering）对 χ² 检验的影响；多重比较校正；置信区间宽度\n6. **Cross-benchmark replication**：6 benchmark 结果的一致性和差异是否有合理解释？\n7. **Downstream impact 分析**：ρ≈0.997 与 family-level rank shifts 的表面矛盾是否充分讨论？\n\n请按 ARR review form 结构输出：Summary → Strengths → Weaknesses (逐条编号 W1, W2, ...) → Questions → Missing References → Overall Assessment + Confidence。Weaknesses 按严重程度排序（Must-Fix → Should-Fix → Minor）。"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-22T05:21:08.402425+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18062
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-22T05:21:09.056948+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你负责审查**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ACL Rolling Review May cycle)\n- **类别**: Long Paper (正文 ≤8 页，参考文献不限)\n- **模板**: ACL style template, `[review]` 模式\n- **匿名**: Double-blind\n- **Deadline**: 2026-05-25\n- **评分标准**: Overall Assessment 1-5 分 (3.5 = Borderline Conference, 4 = Conference)\n\n## 论文路径\n- LaTeX: `projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/submitted.pdf`\n\n## 论文概要\n题目: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n\n将 MH-DIF 应用于 METABENCH 5,227 模型响应矩阵，发现 31% MMLU items 在时间 cohorts 间功能不稳定。提出 cross-subject matching + semi-synthetic injection validation，并证明 web-overlap labels 与 DIF flags 近乎独立（enrichment ≈ 0.96）。6 个 benchmark 复制结果。\n\n## 你的审查侧重\n\n1. **Novelty 评估**：\n   - MH-DIF 本身是 1988 年的方法，贡献声明是 \"methodological and empirical, not algorithmic\"——这个定位对 EMNLP 是否充分？\n   - Cross-subject matching 在 DIF 文献中有先例（purified subtest matching），LLM adaptation 的新颖性边界在哪里？\n   - 与 Growing Pains (Habba et al. 2026) 的差异化是否清晰？\n\n2. **Contribution 完整性**：\n   - Ground truth meta-critique (Contribution 1) 是否有足够实证支撑，还是只是概念区分？\n   - 三个 contributions 之间的逻辑链条是否清晰连贯？\n   - 是否有未列出但实际存在的贡献（如 audit protocol）？\n\n3. **Related Work 覆盖**：\n   - 是否遗漏重要的 measurement invariance / DIF 文献？\n   - IRT in NLP 领域是否有遗漏？\n   - 动态 benchmark、contamination detection 方向是否充分覆盖？\n\n4. **写作质量**：\n   - Narrative coherence：从 \"31% instability\" 到 \"ρ≈0.997 aggregate stability\" 的表面矛盾是否有效 resolved？\n   - Abstract 密度是否过高（信息过载）？\n   - Discussion 的 audit protocol 是否可执行？阈值是否有实证依据？\n   - 术语一致性（DIF/contamination/instability 的关系是否清晰）\n\n5. **格式合规**：\n   - 页数是否符合 8 页正文限制？\n   - 匿名是否完整（URL、致谢等）？\n   - Limitations 章节是否符合 ARR 要求（仅讨论限制，不含新实验/图表）？\n   - \\enlargethispage 使用是否过于激进？\n\n6. **缺失内容**：\n   - 是否缺 Ethics Statement？\n   - 是否需要 Reproducibility 声明？\n   - 是否有悬而未决的 claim 缺乏证据支撑？\n\n请按 ARR review form 结构输出：Summary → Strengths → Weaknesses (逐条编号 W1, W2, ...) → Questions → Missing References → Overall Assessment + Confidence。Weaknesses 按严重程度排序（Must-Fix → Should-Fix → Minor）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你负责审查**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (ACL Rolling Review May cycle)\n- **类别**: Long Paper (正文 ≤8 页，参考文献不限)\n- **模板**: ACL style template, `[review]` 模式\n- **匿名**: Double-blind\n- **Deadline**: 2026-05-25\n- **评分标准**: Overall Assessment 1-5 分 (3.5 = Borderline Conference, 4 = Conference)\n\n## 论文路径\n- LaTeX: `projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/submitted.pdf`\n\n## 论文概要\n题目: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n\n将 MH-DIF 应用于 METABENCH 5,227 模型响应矩阵，发现 31% MMLU items 在时间 cohorts 间功能不稳定。提出 cross-subject matching + semi-synthetic injection validation，并证明 web-overlap labels 与 DIF flags 近乎独立（enrichment ≈ 0.96）。6 个 benchmark 复制结果。\n\n## 你的审查侧重\n\n1. **Novelty 评估**：\n   - MH-DIF 本身是 1988 年的方法，贡献声明是 \"methodological and empirical, not algorithmic\"——这个定位对 EMNLP 是否充分？\n   - Cross-subject matching 在 DIF 文献中有先例（purified subtest matching），LLM adaptation 的新颖性边界在哪里？\n   - 与 Growing Pains (Habba et al. 2026) 的差异化是否清晰？\n\n2. **Contribution 完整性**：\n   - Ground truth meta-critique (Contribution 1) 是否有足够实证支撑，还是只是概念区分？\n   - 三个 contributions 之间的逻辑链条是否清晰连贯？\n   - 是否有未列出但实际存在的贡献（如 audit protocol）？\n\n3. **Related Work 覆盖**：\n   - 是否遗漏重要的 measurement invariance / DIF 文献？\n   - IRT in NLP 领域是否有遗漏？\n   - 动态 benchmark、contamination detection 方向是否充分覆盖？\n\n4. **写作质量**：\n   - Narrative coherence：从 \"31% instability\" 到 \"ρ≈0.997 aggregate stability\" 的表面矛盾是否有效 resolved？\n   - Abstract 密度是否过高（信息过载）？\n   - Discussion 的 audit protocol 是否可执行？阈值是否有实证依据？\n   - 术语一致性（DIF/contamination/instability 的关系是否清晰）\n\n5. **格式合规**：\n   - 页数是否符合 8 页正文限制？\n   - 匿名是否完整（URL、致谢等）？\n   - Limitations 章节是否符合 ARR 要求（仅讨论限制，不含新实验/图表）？\n   - \\enlargethispage 使用是否过于激进？\n\n6. **缺失内容**：\n   - 是否缺 Ethics Statement？\n   - 是否需要 Reproducibility 声明？\n   - 是否有悬而未决的 claim 缺乏证据支撑？\n\n请按 ARR review form 结构输出：Summary → Strengths → Weaknesses (逐条编号 W1, W2, ...) → Questions → Missing References → Overall Assessment + Confidence。Weaknesses 按严重程度排序（Must-Fix → Should-Fix → Minor）。"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-22T05:21:10.619436+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1562
}
```

</details>

---


### Assistant

_source line 538 · 2026-05-22T05:21:18.499544+00:00_

Round 1 已启动：

- 视觉审查 Agent：已派发（fire-and-forget）
- Reviewer 1（方法严谨性）：已分配
- Reviewer 2（新颖性 + 完整性）：已分配

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 51

## Round 51

2 recorded events


### User

_source line 539 · 2026-05-22T05:27:08.113882+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（Round 1 — 方法严谨性 + 实验可靠性）

---

### Paper Summary

本文将教育测量学中的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 分析应用于 LLM benchmark 的时间可比性检验。基于 METABENCH 的 5,227 模型 × 12,508 MMLU items 响应矩阵，作者发现 31.3% 的 items 在 2023 vs. 2024 cohorts 间展现 ETS Category C 级别的 DIF（|Δ_MH| ≥ 1.5, p < 0.05）。论文提出 cross-subject matching 消除 FPR 膨胀（ΔFPR = 0.000），构建 semi-synthetic injection framework 验证检测力（ΔTPR = +0.508 at p=0.5），并在 6 个 benchmark 上复制。核心洞察为：web-overlap contamination labels 与 DIF flags 近乎独立（enrichment ≈ 0.96），暴露了现有 contamination detection 验证方法论中的 category error。

---

### Summary of Strengths

**S1. 规模空前的心理测量审计**：5,227 models × 12,508 items 的 DIF 分析是目前最大规模的 LLM benchmark psychometric audit，6 个 benchmark 的 replication 增强了结论的 robustness。

**S2. Ground truth meta-critique 有独到洞察**：论文清晰区分了 global exposure（web-overlap）和 differential functioning（DIF），用 enrichment ≈ 0.96、Jaccard = 0.206、φ = 0.012 三个指标实证地证明两者近乎独立。Figure 1 的 ICC 示意图有效传达了这一概念区分。这一发现对 contamination detection 研究具有方法论意义。

**S3. Cross-subject matching 设计严谨**：cross-subject matching 排除待测 subject 的 total score 作为 matching variable，在 single-subject injection 下 ΔFPR = 0 是 constructive guarantee（Section 3.4, Remark），不依赖特定 injection 模式。这是一个 clean 的方法论贡献。

**S4. Structural controls 全面**：论文系统检验了 6 种 alternative explanations（ability mismatch、IRT θ-conditioning、within-subject DIF、family de-duplication、architecture heterogeneity、permutation test），每一种都有明确的定量结果。Table 2 的结构化呈现清晰。

**S5. 写作精炼、叙事结构合理**：论文在 8 页正文内覆盖了大量分析，写作密度高但条理清晰。"diagnostic, not destructive" 的定位避免了过度声称，对 ρ ≈ 0.997 与 family-level rank shifts 的 tension 有充分讨论。

**S6. Simpson's paradox 分析有价值**：Section 4.2 的 logistic regression 展示 domain accuracy 在 aggregate level 正向预测 DIF（OR=1.55），控制 item 属性后反转（OR=0.73），92.4% signal 为 item-specific。这一 decomposition 增强了对 DIF 信号本质的理解。

---

### Summary of Weaknesses

#### Must-Fix 问题（影响接收决定）

**W1** [critical] **Quintile stratification (K=5) 在 bimodal LLM 分布下的充分性未验证**
- 具体位置：Section 3.2（"We use K = 5 equiprobable strata (quintile-based binning)"）、Section 3.2 paragraph "LLM-specific challenges"（"the ability distribution is non-normal (bimodal from base vs. instruction-tuned models), motivating quintile-based rather than parametric stratification"）
- 问题：论文正确识别了 LLM ability 分布的 bimodality（base vs. instruction-tuned），但仅以此为由选择 quintile-based 而非 parametric stratification，而未验证 K=5 在 bimodal 分布下是否提供足够的 ability conditioning。在 bimodal 分布中，quintile bins 可能跨越两个 mode 的边界，导致 within-stratum ability variance 异常大，产生 residual confounding。以 N=1,887 models 的 temporal cohorts 为例，每个 quintile stratum 包含 ~377 models。如果 base 和 instruction-tuned models 的 total score 差异恰好落在某一 quintile 边界附近，该 stratum 内的 ability 异质性会显著削弱 conditioning 效果。
- 为什么影响接收：K 的选择直接影响 DIF 检测的 validity——如果 conditioning 不充分，ability differences 会被误判为 DIF。论文引用 ETS 推荐作为 K=5 的依据，但 ETS 的推荐基于 educational testing 中近似正态的能力分布，不适用于 bimodal 场景。
- 建议修改方向：报告 K=10 和 K=20 的 sensitivity analysis 结果（或至少 K=10）；分析 bimodal 分布下各 stratum 的 within-stratum ability SD；如果 C% 对 K 不敏感，这将大幅增强 robustness。

**W2** [critical] **ΔFPR = 0.000 在 abstract/contributions 中的限定条件不足**
- 具体位置：Abstract（"achieves zero false positive inflation under single-subject contamination (ΔFPR = 0.000; ΔFPR < 0.01 for k ≤ 5 subjects)"）、Section 1 Contribution 2（"achieves ΔFPR = 0.000"）
- 问题：Abstract 的措辞在字面上提供了 single-subject 限定，但 "zero false positive inflation" 的强调效果远大于其后的限定条件。在 Contribution 2 中仅写 "achieves ΔFPR = 0.000" 而未附加条件。Table 5（Appendix）显示 k=10 时 ΔFPR = 0.047±0.022，k=20 时 = 0.069±0.018——在 MMLU 的 57 subjects 中，真实 contamination 跨越 >5 subjects 是完全可能的（尤其是 web-crawled training data）。论文在 Section 3.4 和 Limitations 中确实讨论了 boundary，但 abstract 和 contributions 的呈现方式可能让读者获得比实际更强的保证。
- 为什么影响接收：ΔFPR = 0.000 是论文的 headline claim 之一，如果读者仅看 abstract 会高估 cross-subject matching 的 robustness。ARR 审稿标准 R4 要求 "avoiding overclaiming or misleading framing"。
- 建议修改方向：Contribution 2 应改为 "achieves ΔFPR = 0.000 under single-subject contamination and ΔFPR < 0.007 for k ≤ 5 subjects (≤9% of domains)"，并在 abstract 中注明 boundary（>10 subjects 时 ΔFPR 上升至 0.026–0.069）。

#### Should-Fix 问题（影响评分但不一票否决）

**W3** [warning] **Semi-synthetic injection 的 ecological validity 不足，ΔTPR = +0.508 的 moderate 水平值得关注**
- 具体位置：Section 3.4（"we flip incorrect responses to correct in the focal group at exploitation rate p"）、Section 4.5、Limitations
- 问题：Binary flipping（incorrect → correct）是 uniform worst-case pattern，与真实 contamination 差距较大。真实 contamination 可能表现为：(a) partial memorization（对特定 answer choice 有偏好但不一定答对）；(b) reasoning shortcuts（正确推理路径被 memorized template 替代）；(c) format-specific advantages。论文承认这是 "worst-case uniform exploitation pattern" 且 ΔTPR 是 "upper-bound estimate"——但这恰恰意味着在更 realistic 的 contamination 模式下，检测力可能显著低于 0.508。ΔTPR = 0.508 本身只是 moderate（在 injected items 中仅约一半被检测到），如果 upper-bound 就是 moderate，那 realistic 场景下的检测力如何？
- 建议：(1) 补充至少一种更 realistic 的 injection pattern（如 answer-choice bias：翻转为特定 option 而非正确答案）的 sensitivity analysis；(2) 在正文中明确讨论 detection power 的 lower-bound implications，而非仅强调 ΔFPR=0 的方法论贡献。

**W4** [warning] **Family-level cluster bootstrap CI 应在正文中更突出**
- 具体位置：Limitations（"Cluster bootstrap resampling at the family level (29 families with ≥3 members, 1,882 models, B = 1,000) yields a 95% CI of [26.7%, 53.2%], 3.1× wider than the model-level CI [29.4%, 38.1%]"）
- 问题：model-level CI [29.4%, 38.1%] 在 Section 4.2 正文中报告（"95% bootstrap CI: [29.4%, 38.1%]"），但 family-level CI [26.7%, 53.2%] 仅出现在 Limitations。鉴于 LLM families 的 extreme relatedness（论文自己描述为 "hundreds of Llama-2 fine-tunes exceeds the clustering levels studied"），family-level CI 才是更 conservative、更 appropriate 的 uncertainty estimate。3.1× 的 widening 说明 family 结构对 inference 有实质影响。
- 建议：在 Section 4.2 正文中同时报告 model-level 和 family-level CI（例如 "31.3% [model-level CI: 29.4–38.1%; family-level CI: 26.7–53.2%]"），让读者自行判断 precision。

**W5** [warning] **Table 1 中 "FPR (clean)" 的术语使用自相矛盾**
- 具体位置：Table 1 caption（"FPR is the flagging rate on web-overlap 'clean' items (Li et al., 2024b), not a traditional false positive rate"）、Section 4.3
- 问题：论文在 Section 4.3 用整节篇幅论证 web-overlap labels 是 "the wrong ground truth for a differential method"——即 DIF flags 和 web-overlap labels 衡量的是不同概念。但 Table 1 仍用 "FPR" 指代 DIF 在 web-overlap "clean" items 上的 flagging rate。如果 web-overlap "clean" 不等于 "no DIF"，那 "clean" items 上的 DIF-C flagging rate 就不是 false positive rate（即便 Table 1 caption 加了 disclaimer）。这在概念上是自相矛盾的：一面说 web-overlap 不是合适的 ground truth，一面用它定义 FPR。
- 建议：将 Table 1 的列名改为 "C% (clean)" 或 "DIF-C rate on clean items"，并删除 "FPR" 术语以避免混淆。

**W6** [warning] **Graduated de-duplication 的解读偏乐观**
- 具体位置：Section 4.4（"Graduated de-duplication (K=10: 22.7%; K=20: 29.1%) confirms family structure does not inflate C%"）
- 问题：K=10 de-duplication 将 C% 从 31.3% 降至 22.7%，降幅 8.6 pp（27% reduction）。论文将此解读为 "family structure does not inflate C%"，但 8.6 pp 的下降是非 trivial 的。更准确的表述应为 "family structure inflates C% by up to ~8 pp, but the residual 22.7% remains far above the random baseline (0.18%)"。当前措辞可能让读者低估 family clustering 的影响。
- 建议：改为更 nuanced 的表述，承认 family structure 有 moderate inflation effect 但不改变定性结论。

#### Minor 问题（不影响接收）

**M1**: Section 4.6 中 "Among the 200 most displaced models, 33.6% of pairwise rankings reverse" 存在 selection bias——选取 displacement 最大的子集天然会放大 rank reversal rate。应注明这是 conditional on selection 的数字，或补充全样本的 pairwise reversal rate（从 Table 3 推断 flip rate ≈ 2%）。

**M2**: GSM1K correlation analysis (r = -0.478, p = 0.005, N=33) 统计功效有限，论文在 Limitations 中承认了 "exploratory"，但 Section 4.7 正文中的呈现方式（作为 cross-benchmark validation 的组成部分）可能让读者高估其证据强度。建议在正文中也标注 "exploratory"。

**M3**: Section 5.3 提出的 DIF audit protocol（Monitor/Flag/Act thresholds）基于经验而非理论推导。C% = 15% 和 25% 的阈值来自 ρ degradation simulation，但未提供 formal justification（如 type I/II error control）。这不影响论文的核心贡献，但 protocol 的可操作性需要更多验证。

**M4**: 论文脚注 1 提供了 anonymous code repository URL，但论文中引用的若干工具（PSN-IRT, METABENCH response matrix）的可获取性未明确说明，可能影响 reproducibility 评分。

---

### Questions for Authors

**Q1**: K=5 quintile stratification 的 sensitivity analysis 是否已在内部测试过？如果有 K=10/20 的结果，能否在 rebuttal 中提供？

**Q2**: Cross-subject matching 在 MMLU 以外的 benchmark（如 GSM8K, 仅有 1 个 "subject"）上如何操作？Section 4.7 提到 external matching 用于 GSM8K，但 cross-subject matching 是否仅限于 multi-domain benchmarks？如果是，这是否限制了方法的 generalizability？

**Q3**: 论文报告 IRT θ-conditioning 与 total score 的 r = 0.9986，但 2PL fit 较差（Appendix A.2）。在 model fit 较差的情况下，θ estimates 本身是否可靠？r = 0.9986 是否仅反映了 total score 和 θ 在 rank-order 上的一致性而非 scale 上的一致性？

**Q4**: 论文使用 2023 vs. 2024 release date 作为 temporal cohort 划分。这是否与模型的 training data cutoff 对齐？一个 2024 年发布但 training data cutoff 在 2022 年的模型可能被错误分类。论文是否有 training data cutoff 的信息？

---

### Missing References

1. **Penfield & Camilli (2007)** "Differential Item Functioning" in *Handbook of Statistics* — 作为 DIF 方法论的现代综述，与本文方法论定位高度相关。
2. **Millsap & Everson (1993)** "Methodology of Differential Item Functioning Research" — 早期但权威的 DIF 方法论总结。
3. **Liang et al. (2023)** "Holistic Evaluation of Language Models" (HELM) — 作为 LLM evaluation 的重要 framework，值得在 Related Work 中提及。

---

### Limitations and Societal Impact

Limitations 章节覆盖了 4 个方面（methodological scope、examinee non-independence、matching boundary、generalizability），内容充实且诚实。特别值得肯定的是对 family-level cluster bootstrap CI 的报告。

建议在 generalizability 段落中补充：当前结论仅适用于 METABENCH 中 Open LLM Leaderboard 的公开模型，对 closed-source models（GPT-4、Claude 等）的 DIF behavior 无法推断，因为这些模型的 training data composition 和 release pattern 可能有系统性差异。

---

### Ethical Concerns

无显著伦理问题。论文使用公开数据集和公开模型评估结果，不涉及 human subjects。Anonymous code repository 的做法符合 double-blind 要求。

---

## 总体评分

### 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法总体 sound，structural controls 全面；但 K=5 quintile 在 bimodal 分布下的充分性未验证，semi-synthetic injection 的 ecological validity 有限，family clustering 对 CI 的影响需更突出报告 |
| Excitement | 3.5/5 | 重要问题（benchmark temporal comparability），meta-critique 有独到贡献，规模空前；但方法本身为 off-the-shelf MH-DIF 的应用，核心发现为 descriptive empirical，可操作指导有限 |
| Reproducibility | 4/5 | 提供 anonymous code，methodology 描述详尽，统计参数齐全；但若干外部资源（PSN-IRT, METABENCH matrix）的可获取性未明确 |
| Confidence | 4/5 | 对 DIF 方法论和 LLM evaluation 有较好背景，仔细阅读了全文含 appendix |

**Overall Assessment**: **3.5** (Borderline Conference)

**一句话总结**: 论文在规模和 structural controls 上表现出色，ground truth meta-critique 是 genuine contribution，但 K=5 quintile 在 bimodal LLM 分布下的 adequacy 未验证、ΔFPR=0.000 的 prominent claim 需更严格限定、semi-synthetic injection 的 ecological validity 需加强——这些方法论不确定性使论文处于 Conference 和 Findings 之间。

---

### 主要优势总结
- 5,227 models × 6 benchmarks 的规模空前，结论 robust
- Ground truth meta-critique 对 contamination detection 领域有方法论修正意义
- Cross-subject matching 的 zero-FPR guarantee（under single-subject injection）是 clean 的方法论贡献
- 6 种 alternative explanations 的 systematic exclusion 令人信服
- "Diagnostic, not destructive" 的 nuanced framing 避免了 overclaiming
- 写作密度高但清晰，8 页内完成了大量分析

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 540 · 2026-05-22T05:27:17.057336+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 52

## Round 52

2 recorded events


### User

_source line 541 · 2026-05-22T05:27:22.204176+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：以 Reviewer 1（方法严谨性 + 实验可靠性）完成了 Round 1 审稿，Overall 3.5（Borderline Conference）。

核心判断：
- **2 个 Must-Fix**：(1) K=5 quintile stratification 在 bimodal LLM 分布下的充分性未验证，需 sensitivity analysis；(2) ΔFPR=0.000 在 abstract/contributions 中缺少足够限定条件
- **4 个 Should-Fix**：semi-synthetic injection ecological validity 不足、family-level CI 应在正文更突出、Table 1 "FPR" 术语自相矛盾、de-duplication 解读偏乐观
- **4 个 Minor**：200 most displaced models 的 selection bias、GSM1K N=33 exploratory 标注、DIF audit protocol 阈值缺乏 formal justification、外部资源可获取性

主要优势为规模空前（5,227 models × 6 benchmarks）、ground truth meta-critique 有方法论修正意义、structural controls 系统全面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 542 · 2026-05-22T05:27:59.853159+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 53

## Round 53

6 recorded events


### User

_source line 543 · 2026-05-22T05:28:01.357134+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告（Round 1）

**论文**: "Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models"
**审查侧重**: 新颖性 + 完整性 + 写作质量 + 格式合规

---

## Summary

本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU items），发现约 31% 的 items 在 2023 与 2024 模型 cohort 间表现出显著的 temporal DIF（ETS Category C）。论文提出 cross-subject matching 消除 FPR inflation（ΔFPR = 0.000），并通过 semi-synthetic injection 验证检测能力。核心发现：web-overlap contamination labels 与 DIF flags 近乎独立（enrichment ≈ 0.96），挑战了当前 contamination detection 研究的 validation methodology。结果在 6 个 benchmark 上复制。

---

## Strengths

**S1. Ground truth meta-critique 是真正的方法论贡献。** 论文用严格的实证（enrichment = 0.964, φ = 0.012, χ² = 1.28, Jaccard = 0.206）证明 web-overlap labels 与 DIF flags 正交，揭示了 contamination detection 文献中一个系统性的 validation category error（Section 4.3）。这一发现对整个 contamination detection 领域有 immediate implications。

**S2. 实验控制极为周密。** 论文设计了 5 种 cohort 对比（temporal, ability-quintile, within-family, within-subject, random split），6 种 structural robustness checks（matched-ability, IRT θ-conditioning, graduated de-duplication, logistic regression DIF, Simpson's paradox analysis, external matching），以及 semi-synthetic injection 的 multi-subject 扩展（Table 5）。这种 triangulation 的 thoroughness 在 NLP 实证论文中罕见。

**S3. Cross-subject matching 有清晰的理论保证。** Section 3.4 的 Remark（zero FPR under single-subject matching）给出了 constructive proof，而非仅靠 empirical validation。multi-subject injection（Table 5）划定了方法的适用边界（k ≤ 5 subjects, ΔFPR < 0.007），展现了诚实的方法评估。

**S4. "31% instability vs. ρ ≈ 0.997" 的 paradox resolution 有深度。** Section 4.6 通过 family-level rank shifts（Llama-3 +53, Mistral -35）和 top-200 displaced models（33.6% pairwise reversals）展示了 aggregate stability 掩盖 model-level instability 的现象。这不是简单的 headline 数字，而是一个有层次的分析。

**S5. 跨 benchmark 复制增强了外部效度。** 6 个 benchmark 的 C% = 17.9–31.3%（Table 3），且 knowledge/reasoning benchmarks 系统性高于 procedural ones，这一模式有实质性的 interpretive value。

**S6. Limitations 坦诚而详尽。** 覆盖了方法论范围、examinee non-independence（含 cluster bootstrap CI）、matching boundary、generalizability 四个维度，包含了自我批评性的 quantitative bounds。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1** [critical] **Abstract 信息密度过高，损害可读性和 first impression**
- 具体位置：Abstract（第1页）
- 问题：单段 abstract 内填充了 ΔFPR = 0.000, ΔFPR < 0.01, ΔTPR = +0.508, enrichment ≈ 0.96, φ = 0.012, ETS Category C, ρ ≈ 0.997, τ ≈ 0.958, z = −8 to −49, ρ = −0.597, C% = 17.9–31.3%, 45–174× 等十余个数值。读者无法在首次阅读时提取核心 story。
- 为什么影响接收：ARR reviewer 在 abstract 阶段形成初始判断。当前 abstract 读起来像 results table 的文字版而非 narrative summary，可能导致 reviewer 低估贡献的 conceptual clarity。
- 建议修改方向：分层叙述——第一句定义问题，第二句陈述方法论贡献（ground truth meta-critique + cross-subject matching），第三句给出 headline 实证结果（31%, 6 benchmarks），第四句给 practical implication。将 ΔFPR、φ、z-score 等 secondary metrics 移入正文。

**W2** [critical] **缺少 Ethics Statement**
- 具体位置：全文（Limitations 之后，References 之前应有 Ethics Statement）
- 问题：ARR submission form 要求提供 Ethics Statement（或至少明确说明不存在伦理风险）。本文虽属 audit/analysis 性质，但完全缺失此部分。
- 为什么影响接收：这是 ARR formatting requirement。Area Chair 可能因此标记 desk-reject 风险或要求修改。
- 建议修改方向：添加简短 Ethics Statement，说明：(1) 研究仅使用公开 benchmark 数据，不涉及人类受试者；(2) DIF 分析不涉及 sensitive attributes；(3) audit protocol 旨在提高 benchmark transparency。

### Should-Fix（影响评分但不一票否决）

**W3** [warning] **新颖性定位需更 sharp 地区分 adaptation 与 application**
- 具体位置：Section 1（Introduction, contributions list）, Section 2（Related Work, DIF Methodology paragraph）
- 问题：论文声明 "contributions are methodological and empirical, not algorithmic"，但这种 framing 既是优点（诚实）也是风险。MH-DIF 是 1988 年的方法，cross-subject matching 在 DIF 文献中有先例（purified subtest matching, Swaminathan 1990; Nandakumar 1993）。论文在 Related Work 中提到了这些（"our adaptation addresses LLM-specific challenges"），但未充分展开 adaptation 的具体技术细节——面对 LLM 特有的 multi-domain local dependence、extreme model relatedness（hundreds of fine-tunes）、bimodal ability distribution 时，标准 purified subtest matching 为何不够用，cross-subject matching 做了什么额外的设计？
- 与 Growing Pains (Habba et al. 2026) 的区分：Section 2 将两者定位为 complementary（FPC vs. DIF），但未讨论在 practical workflow 中如何组合使用。Section 5.3 的 audit protocol 提到 "DIF pre-screening identifies stable anchor items for equating"，这正是与 FPC 的接口——应在 Related Work 中更明确地阐述。
- 建议：在 Section 3.2 "LLM-specific challenges" 段落后增加一段，明确列出 cross-subject matching 相对于 purified subtest matching 的 3 个 LLM-specific adaptations，使 novelty boundary 可检验。

**W4** [warning] **Discussion audit protocol 的 causal framing 与 Limitations 的 agnostic stance 矛盾**
- 具体位置：Section 5.3 vs. Limitations "Methodological scope" 段
- 问题：Limitations 明确说 "DIF detects that items function differently but cannot determine why"。但 Section 5.3 的 audit protocol Step 3 (Act) 建议 "cross-reference with contamination indicators"，这隐含了 DIF flags 可作为 contamination signal 的假设。如果 DIF 与 web-overlap 近乎独立（Section 4.3 的核心发现），那么 cross-reference 预期能找到什么？
- 建议：将 Section 5.3 的 protocol 明确定位为 "measurement property monitoring"，而非 contamination detection auxiliary。Step 3 可改为 "review flagged item content for face-validity changes"，去除 contamination 暗示。

**W5** [warning] **页数可能超限**
- 具体位置：Discussion section 使用了 `\enlargethispage{2\baselineskip}`（discussion.tex 第3行）
- 问题：Main text（Sections 1–6，不含 Limitations）占据约 8.3 页。EMNLP 2026 Long Paper 限制为正文 ≤ 8 页（Limitations 和 References 不计入）。Section 5.3 (Recommended DIF Audit Protocol) 延伸到第 9 页上部，Section 6 (Conclusion) 在第 9 页中部结束。即使 Limitations 不计入，正文明显超出 8 页。`\enlargethispage{2\baselineskip}` 的使用（在 Discussion 开头扩展页面高度 2 个基线行距）说明作者已在主动挤压空间，但仍不够。
- 为什么影响接收：页数超限是 hard constraint violation，可能被 AC 直接 desk-reject。
- 建议：将 Section 5.3 audit protocol 移至 Appendix（保留一句引用），或精简 Section 4 中的重复数字陈述，释放 0.3–0.5 页空间。

**W6** [warning] **Cohort 定义按 release date 划分，未讨论 training data cutoff 的偏差**
- 具体位置：Section 3.3 Cohort Designs
- 问题：temporal cohort 按 model release date（2023 vs 2024）定义。但 2024 年初发布的模型，其 training data cutoff 可能在 2023 年中甚至更早。Release date 与 training data exposure 的 lag 是一个 systematic confound——早期 2024 模型可能在 training data 上更接近 2023 cohort。6 个月窗口分析（Section 4.7 末尾："DIF remains substantial even within a 6-month window"）部分缓解了这一问题，但仅用一句话带过。
- 建议：将 6-month window analysis 作为 Section 4 的一个正式 subsection 或至少一个 dedicated paragraph，提供 quarterly cohort 的 C% 变化趋势。

**W7** [warning] **Multiple testing 论证不够严谨**
- 具体位置：Section 4.2, Appendix A.2
- 问题：12,508 个 items 同时检验，raw significance threshold p < 0.05 会产生 ~625 个 false positives。论文说 BH-FDR 只移除 3 个 items（31.32% → 31.30%），并声称 "dual ETS threshold already provides implicit multiple-testing protection"。这是结果正确但论证不完整——implicit protection 来自 effect size 门槛 |Δ_MH| ≥ 1.5，而非统计上的 formal correction。Random-split control（0.18%）才是真正的 empirical FPR calibration，但在论文中不够突出。
- 建议：在 Section 4.2 或 Appendix A.2 中明确量化：在 null hypothesis 下（random split），expected C% = 0.18%，远低于 observed 31.3%，effect size threshold 是主要 safeguard。

### Minor（不影响接收）

**M1.** 术语一致性：论文中 "temporal measurement instability"、"temporal DIF"、"measurement invariance" 交替使用。建议在 Section 3 开头用一段明确定义三者关系：measurement invariance 是 general framework，DIF 是 specific test，temporal instability 是本文观测到的 phenomenon。

**M2.** Table 3 的 "Ratio" 列（45×–174×）：分母（random baseline C%）在 0.18%–0.60% 间变动，使得跨 benchmark 的 ratio 比较有误导性（MMLU 的 174× 部分归因于其极低的 random baseline）。建议在 caption 中注明或改用统一的 effect size metric。

**M3.** Figure 1 的 ICC 图较小，坐标轴文字在打印版可能难以辨认。建议增大字号或使用 subcaption 并排放置时增加宽度。

**M4.** GSM1K 相关分析（r = −0.478, N = 33）统计功效有限。论文已标注为 exploratory，但 Section 4.7 中 "suggests DIF captures capability change distinct from memorization" 的措辞略强。建议弱化为 "is consistent with" 而非 "suggests"。

**M5.** Conclusion（Section 6）仅 3 行，过于简短。当前内容基本重复了 abstract 的数字而无 forward-looking discussion。建议补充 1-2 句关于 temporal DIF monitoring 的 community-level implications 或 open problems。

---

## Questions for Authors

**Q1.** Cross-subject matching 在 MMLU 57 个 subjects 的结构下有效（zero FPR），但对于 single-domain benchmark（如 GSM8K 只有数学），如何实现同等的 FPR 控制？Section 4.7 使用 external matching（MMLU total score），但这引入了跨 benchmark 的 ability proxy 假设——如何确保 MMLU score 是 GSM8K ability 的无偏代理？

**Q2.** Table 1 中 within-family comparison（Llama-2 vs. Llama-3）的 C% = 61.3%，ability-matched 后降至 28.3%。这意味着 32.9% 的 apparent DIF 实为 ability difference (impact)。Temporal comparison（31.3% → 28.9% after matching）的 impact component 仅 2.4 pp。这种差异是否意味着 temporal DIF 中 ability confound 已被充分控制，而 within-family DIF 中 ability gap 才是主因？

**Q3.** 92.4% 的 DIF signal 是 item-specific（pseudo R² = 0.0007 for domain-level accuracy change as predictor）。如何排除这不是因为 item-level predictors 被遗漏（omitted variable bias）？是否测试了其他 item-level features（e.g., item length, answer option distribution, subject-specific features）？

---

## Missing References

- **HELM**: Liang et al. (2022), "Holistic Evaluation of Language Models" — 作为主流 evaluation framework 缺失
- **Measurement invariance via CFA/SEM**: Millsap (2011), "Statistical Approaches to Measurement Invariance" — DIF 是 measurement invariance 的 specific instance，但论文仅引用 Meredith 1993 和 Vandenberg 2000，缺少现代综述
- **Penfield & Camilli (2007)**: "Differential Item Functioning" (Handbook of Statistics) — 较全面的 DIF 方法论综述，与当前引用的 Zumbo 1999 互补

（注：Related Work 整体覆盖面已经相当好，上述仅为 minor suggestions。）

---

## 官方维度打分（ACL Rolling Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4.0/5 | 实验设计严密，多种 structural controls 和 robustness checks；主要扣分点是 causal attribution gap（DIF detects "that" not "why"）和 multiple testing 论证不够 formal |
| Excitement | 3.5/5 | Ground truth meta-critique 有 genuine novelty 且对 contamination detection 社区有 immediate implications；但 MH-DIF 本身是 1988 方法的 application，methodological novelty 在 techniques 层面有限 |
| Overall Assessment | **3.5** (Borderline Conference) | 扎实的大规模实证研究，ground truth meta-critique 是 genuine contribution，cross-subject matching 有实用价值。主要顾虑：(1) 应用已有方法的 novelty ceiling；(2) ρ ≈ 0.997 部分 undermines practical urgency；(3) 页数可能超限需要压缩。如果 abstract 重写 + ethics statement 补齐 + 页数合规 + novelty positioning 更 sharp，有潜力提升至 4.0 |
| Confidence | 4/5 | 熟悉 DIF 方法论和 LLM evaluation 文献，仔细阅读了全文和 appendix |

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 一项 thorough 的大规模 psychometric audit，ground truth meta-critique 是真正的方法论贡献，但 novelty 主要在 empirical findings 而非 techniques，且格式问题（缺 Ethics Statement、页数 borderline）需要修复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-22T05:28:25.047175+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应其 Weaknesses：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 Weaknesses\n\n### Must-Fix\n\n**W1** [critical] **Abstract 信息密度过高，损害可读性和 first impression**\n- 单段 abstract 内填充了十余个数值（ΔFPR, ΔTPR, enrichment, φ, ρ, τ, z, C% 等）。读者无法在首次阅读时提取核心 story。建议分层叙述，将 secondary metrics 移入正文。\n\n**W2** [critical] **缺少 Ethics Statement**\n- ARR submission form 要求提供 Ethics Statement。本文完全缺失此部分。Area Chair 可能因此标记 desk-reject 风险。\n\n### Should-Fix\n\n**W3** [warning] **新颖性定位需更 sharp 地区分 adaptation 与 application**\n- MH-DIF 是 1988 年方法，cross-subject matching 有 DIF 文献先例（purified subtest matching）。论文未充分展开 LLM-specific adaptation 的具体技术细节。与 Growing Pains 的 practical workflow 组合也未展开。\n\n**W4** [warning] **Discussion audit protocol 的 causal framing 与 Limitations 的 agnostic stance 矛盾**\n- Limitations 说 \"DIF detects that not why\"，但 Section 5.3 Step 3 (Act) 建议 \"cross-reference with contamination indicators\"，隐含 DIF flags 可作为 contamination signal。如果 DIF 与 web-overlap 近乎独立，cross-reference 预期能找到什么？\n\n**W5** [warning] **页数可能超限**\n- Main text 约 8.3 页，`\\enlargethispage{2\\baselineskip}` 说明作者已在挤压空间。EMNLP 2026 正文 ≤ 8 页是 hard constraint。\n\n**W6** [warning] **Cohort 定义按 release date 划分，未讨论 training data cutoff 偏差**\n- Release date 与 training data exposure 的 lag 是 systematic confound。6-month window analysis 仅用一句话带过。\n\n**W7** [warning] **Multiple testing 论证不够严谨**\n- 12,508 items 同时检验，implicit protection 来自 effect size 门槛而非 formal correction。Random-split control 才是真正的 empirical FPR calibration，但不够突出。\n\n### Minor\n- M1: 术语不一致（temporal measurement instability / temporal DIF / measurement invariance 交替使用）\n- M2: Table 3 Ratio 列跨 benchmark 比较有误导性\n- M3: Figure 1 ICC 图打印版可能难辨\n- M4: GSM1K \"suggests\" 措辞略强，应弱化为 \"is consistent with\"\n- M5: Conclusion 仅 3 行，过于简短\n\n---\n\n请逐条回应（W1-W7, M1-M5）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应其 Weaknesses：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 Weaknesses\n\n### Must-Fix\n\n**W1** [critical] **Abstract 信息密度过高，损害可读性和 first impression**\n- 单段 abstract 内填充了十余个数值（ΔFPR, ΔTPR, enrichment, φ, ρ, τ, z, C% 等）。读者无法在首次阅读时提取核心 story。建议分层叙述，将 secondary metrics 移入正文。\n\n**W2** [critical] **缺少 Ethics Statement**\n- ARR submission form 要求提供 Ethics Statement。本文完全缺失此部分。Area Chair 可能因此标记 desk-reject 风险。\n\n### Should-Fix\n\n**W3** [warning] **新颖性定位需更 sharp 地区分 adaptation 与 application**\n- MH-DIF 是 1988 年方法，cross-subject matching 有 DIF 文献先例（purified subtest matching）。论文未充分展开 LLM-specific adaptation 的具体技术细节。与 Growing Pains 的 practical workflow 组合也未展开。\n\n**W4** [warning] **Discussion audit protocol 的 causal framing 与 Limitations 的 agnostic stance 矛盾**\n- Limitations 说 \"DIF detects that not why\"，但 Section 5.3 Step 3 (Act) 建议 \"cross-reference with contamination indicators\"，隐含 DIF flags 可作为 contamination signal。如果 DIF 与 web-overlap 近乎独立，cross-reference 预期能找到什么？\n\n**W5** [warning] **页数可能超限**\n- Main text 约 8.3 页，`\\enlargethispage{2\\baselineskip}` 说明作者已在挤压空间。EMNLP 2026 正文 ≤ 8 页是 hard constraint。\n\n**W6** [warning] **Cohort 定义按 release date 划分，未讨论 training data cutoff 偏差**\n- Release date 与 training data exposure 的 lag 是 systematic confound。6-month window analysis 仅用一句话带过。\n\n**W7** [warning] **Multiple testing 论证不够严谨**\n- 12,508 items 同时检验，implicit protection 来自 effect size 门槛而非 formal correction。Random-split control 才是真正的 empirical FPR calibration，但不够突出。\n\n### Minor\n- M1: 术语不一致（temporal measurement instability / temporal DIF / measurement invariance 交替使用）\n- M2: Table 3 Ratio 列跨 benchmark 比较有误导性\n- M3: Figure 1 ICC 图打印版可能难辨\n- M4: GSM1K \"suggests\" 措辞略强，应弱化为 \"is consistent with\"\n- M5: Conclusion 仅 3 行，过于简短\n\n---\n\n请逐条回应（W1-W7, M1-M5）。"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-22T05:28:44.351875+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19304
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-22T05:28:44.503090+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应其 Weaknesses：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 Weaknesses\n\n### Must-Fix\n\n**W1** [critical] **Quintile stratification (K=5) 在 bimodal LLM 分布下的充分性未验证**\n- LLM ability 分布呈 bimodal（base vs. instruction-tuned），quintile bins 可能跨越两个 mode 边界，导致 within-stratum ability variance 过大、residual confounding。ETS 推荐 K=5 基于正态分布假设。需 K=10/K=20 sensitivity analysis。\n\n**W2** [critical] **ΔFPR = 0.000 在 abstract/contributions 中的限定条件不足**\n- Abstract 字面上提供了 single-subject 限定，但 \"zero false positive inflation\" 的强调效果远大于限定。Contribution 2 仅写 \"achieves ΔFPR = 0.000\" 无附加条件。k=10 时 ΔFPR = 0.047，真实 contamination 跨 >5 subjects 完全可能。\n\n### Should-Fix\n\n**W3** [warning] **Semi-synthetic injection 的 ecological validity 不足，ΔTPR = +0.508 为 moderate**\n- Binary flipping 是 worst-case uniform pattern，真实 contamination 差距大（partial memorization, reasoning shortcuts, format-specific）。如果 upper-bound 就是 moderate，realistic 场景下检测力如何？\n\n**W4** [warning] **Family-level cluster bootstrap CI 应在正文中更突出**\n- Family-level CI [26.7%, 53.2%] 比 model-level CI [29.4%, 38.1%] 宽 3.1×，但仅在 Limitations 中报告。\n\n**W5** [warning] **Table 1 \"FPR (clean)\" 术语自相矛盾**\n- 论文论证 web-overlap labels 不是合适的 ground truth，但 Table 1 仍用 \"FPR\" 指代 DIF 在 web-overlap clean items 上的 flagging rate。概念上自相矛盾。\n\n**W6** [warning] **Graduated de-duplication 解读偏乐观**\n- K=10 将 C% 从 31.3% 降至 22.7%（降幅 8.6pp），但论文说 \"family structure does not inflate C%\"。实际有 moderate inflation。\n\n### Minor\n- M1: \"200 most displaced models\" 的 33.6% pairwise reversals 有 selection bias\n- M2: GSM1K N=33 应在正文标注 \"exploratory\"\n- M3: DIF audit protocol 阈值缺 formal justification\n- M4: 外部资源（PSN-IRT, METABENCH matrix）可获取性未明确\n\n---\n\n请逐条回应（W1-W6, M1-M4）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应其 Weaknesses：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 Weaknesses\n\n### Must-Fix\n\n**W1** [critical] **Quintile stratification (K=5) 在 bimodal LLM 分布下的充分性未验证**\n- LLM ability 分布呈 bimodal（base vs. instruction-tuned），quintile bins 可能跨越两个 mode 边界，导致 within-stratum ability variance 过大、residual confounding。ETS 推荐 K=5 基于正态分布假设。需 K=10/K=20 sensitivity analysis。\n\n**W2** [critical] **ΔFPR = 0.000 在 abstract/contributions 中的限定条件不足**\n- Abstract 字面上提供了 single-subject 限定，但 \"zero false positive inflation\" 的强调效果远大于限定。Contribution 2 仅写 \"achieves ΔFPR = 0.000\" 无附加条件。k=10 时 ΔFPR = 0.047，真实 contamination 跨 >5 subjects 完全可能。\n\n### Should-Fix\n\n**W3** [warning] **Semi-synthetic injection 的 ecological validity 不足，ΔTPR = +0.508 为 moderate**\n- Binary flipping 是 worst-case uniform pattern，真实 contamination 差距大（partial memorization, reasoning shortcuts, format-specific）。如果 upper-bound 就是 moderate，realistic 场景下检测力如何？\n\n**W4** [warning] **Family-level cluster bootstrap CI 应在正文中更突出**\n- Family-level CI [26.7%, 53.2%] 比 model-level CI [29.4%, 38.1%] 宽 3.1×，但仅在 Limitations 中报告。\n\n**W5** [warning] **Table 1 \"FPR (clean)\" 术语自相矛盾**\n- 论文论证 web-overlap labels 不是合适的 ground truth，但 Table 1 仍用 \"FPR\" 指代 DIF 在 web-overlap clean items 上的 flagging rate。概念上自相矛盾。\n\n**W6** [warning] **Graduated de-duplication 解读偏乐观**\n- K=10 将 C% 从 31.3% 降至 22.7%（降幅 8.6pp），但论文说 \"family structure does not inflate C%\"。实际有 moderate inflation。\n\n### Minor\n- M1: \"200 most displaced models\" 的 33.6% pairwise reversals 有 selection bias\n- M2: GSM1K N=33 应在正文标注 \"exploratory\"\n- M3: DIF audit protocol 阈值缺 formal justification\n- M4: 外部资源（PSN-IRT, METABENCH matrix）可获取性未明确\n\n---\n\n请逐条回应（W1-W6, M1-M4）。"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-22T05:28:46.011906+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1508
}
```

</details>

---


### Assistant

_source line 548 · 2026-05-22T05:28:53.791087+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 54

## Round 54

2 recorded events


### User

_source line 549 · 2026-05-22T05:28:56.493100+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断**：Overall 3.5（Borderline Conference）。

**关键发现**：
- **2 个 Must-Fix**：Abstract 信息过载需重写；缺少 Ethics Statement
- **5 个 Should-Fix**：novelty 定位需更 sharp（W3）、audit protocol 的 causal framing 与 Limitations 矛盾（W4）、页数可能超限约 0.3 页（W5）、cohort definition 的 training data lag 讨论不足（W6）、multiple testing 论证不严谨（W7）
- **5 个 Minor**：术语一致性、Table 3 ratio 可比性、Figure 1 可读性、GSM1K 措辞偏强、Conclusion 过短

**主要优势**：ground truth meta-critique 是 genuine contribution（S1），实验控制周密程度罕见（S2），cross-subject matching 有理论保证（S3）。如果格式问题修复 + novelty positioning 更清晰，有提升至 4.0 的潜力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 550 · 2026-05-22T05:29:01.715406+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 55

## Round 55

10 recorded events


### User

_source line 551 · 2026-05-22T05:30:57.941066+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 意见

---

### Must-Fix

**[REBUT] R1-W1: Quintile stratification (K=5) 在 bimodal 分布下的充分性**

R1 的顾虑有理论依据，但论文已通过不同路径提供了等价的 sensitivity analysis。Appendix A (Section B, structural analysis details) 报告了 IRT θ-conditioning with **20 ability strata**，结果为 C% = 0.312（vs. baseline 0.313），几乎完全一致（Table 2: θ-cond. row）。这实质上是 K=20 的 stratification sensitivity analysis，只是用 IRT θ 替代 total score 作为 matching variable（两者相关 r = 0.9986）。此外，Section 4.2 的 matched-ability quintile analysis 也提供了控制——能力匹配后 C% 从 31.3% 仅降至 28.9%。

不过 R1 的建议仍有 incremental value：直接用 K=10/K=20 **MH quintile bins**（而非 θ-conditioning）做 sensitivity analysis 会让论证更直接易懂。当前读者需要从 Table 2 的 θ-conditioning 行自行推断等价性，这对不熟悉 IRT 的 NLP 读者不够友好。建议作者在 Section 3.2 或 Appendix 中补充一句明确桥接："IRT θ-conditioning with K=20 strata serves as a sensitivity check for the K=5 quintile design; results are unchanged (Table 2)."

**结论**：问题实际上已被 addressed（θ-conditioning = K=20 equivalent），但 presentation 可以更明确。不构成 must-fix。

---

**[AGREE] R1-W2: ΔFPR = 0.000 的限定条件在 Contribution statement 中不足**

同意。Abstract 中虽有 "under single-subject contamination" 的限定（原文："achieves zero false positive inflation under single-subject contamination (ΔFPR = 0.000; ΔFPR < 0.01 for k ≤ 5 subjects)"），但 Introduction 的 Contribution 2（Section 1, contribution list item 2）仅写 "Controlled injection with cross-subject matching achieves ΔFPR = 0.000"，**完全没有 single-subject 限定**。Table 5 显示 k=10 时 ΔFPR = 0.047，k=20 时 ΔFPR = 0.069——真实场景中跨 >5 subjects 的 contamination 完全可能（如 pre-training data 覆盖多个 domain）。

这不是 factual error，但 contribution statement 的 framing 会形成读者对方法能力的 over-optimistic expectation。建议在 Contribution 2 中加入 "(under single-subject contamination; ΔFPR < 0.007 for k ≤ 5)" 的限定。

---

### Should-Fix

**[AGREE] R1-W3: Semi-synthetic injection 的 ecological validity 及 ΔTPR = +0.508 的 moderate level**

同意这是一个真实的局限，且论文已在 Limitations 中坦承："Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages; detection power under such realistic patterns is untested." 但我补充两点 nuance：

1. 论文将 ΔTPR 定位为 **upper-bound estimate**（Section 3.4: "reported ΔTPR values constitute upper-bound estimates"），这意味着 realistic 场景下 TPR 会更低，而非更高。这一定位是诚实的，但也意味着方法的实际检测力可能不够 convincing——如果 upper-bound 仅为 0.508，lower bound 可能 negligible。
2. 不过，论文的 validation framework 的**核心贡献是 ΔFPR = 0.000**（matching strategy property），而非 ΔTPR（injection model dependent）。这一区分在 Section 3.4 最后一段有明确论述。

建议作者讨论 realistic contamination patterns 下的 expected TPR degradation，至少给出 qualitative 方向。

---

**[AGREE] R1-W4: Family-level cluster bootstrap CI 应在正文中更突出**

同意。Family-level CI [26.7%, 53.2%] 提供了一个重要的 conservative bound，但仅出现在 Limitations 的 "Examinee non-independence" 段落中。Section 4.2 报告 model-level CI [29.4%, 38.1%] 时，未提及 family-level CI 作为 robustness check。一个 reviewer 如果只精读正文而略过 Limitations，会获得一个 over-precise 的不确定性估计。

建议在 Section 4.2 的 bootstrap CI 报告处添加一句："Family-level cluster bootstrap yields a wider CI of [26.7%, 53.2%] (Limitations), confirming robustness to within-family dependence."

---

**[AGREE] R1-W5: Table 1 "FPR (clean)" 术语自相矛盾**

完全同意。论文的核心论点之一（Contribution 1）是 web-overlap labels 不是 DIF 的合适 ground truth，enrichment ≈ 0.96 证明两者正交。但 Table 1 的列标题 "FPR (clean)" 仍以 web-overlap clean items 作为 "true negatives" 来定义 false positive rate——这在概念上直接与 Contribution 1 矛盾。虽然 Table 1 caption 有注释 "not a traditional false positive rate"，但列标题本身会给快速扫描的读者留下错误印象。

建议改为 "DIF-C rate (clean subset)" 或 "Flagging rate (web-clean)"，消除 "FPR" 这个有强暗示的术语。

---

**[REBUT] R1-W6: Graduated de-duplication 解读偏乐观**

R1 指出 K=10 将 C% 从 31.3% 降至 22.7%（降幅 8.6pp），认为 "family structure does not inflate C%" 的论断过于乐观。这个观察表面上成立，但需要考虑 **statistical power confound**：

1. K=10 的 aggressive de-duplication 大幅减少样本量。原始数据有 5,227 模型；K=10（每 family 最多保留 10 个）可能将样本量降至远低于原始值。MH 检验的 power 依赖样本量（Section 4.1 confirms TPR 与 N 正相关），因此 C% 下降可能部分归因于 **power reduction**，而非 family inflation 的消除。
2. K=20 时 C% = 29.1%（降幅仅 2.2pp），远小于 K=10 的降幅。如果 family inflation 是主因，K=10 到 K=20 的边际变化不应这么大（8.6pp vs 2.2pp）——这种非线性更符合 power loss 的解释（K=10 的 power loss 远大于 K=20）。
3. 即使在 K=10 下，22.7% 仍然是 random baseline 0.18% 的 **126×**，qualitative conclusion 不变。

因此，论文的 qualitative claim（family structure is not the primary driver）是合理的，但 quantitative framing ("does not inflate") 确实偏乐观。建议改为 "graduated de-duplication reduces C% moderately (22.7% at K=10) but the effect is confounded with power reduction; even the most conservative estimate remains >100× above random baseline."

---

### Minor

**[AGREE] R1-M1: "200 most displaced models" 的 selection bias**

同意存在 selection bias——按定义，选择 displacement 最大的模型子集会放大 pairwise reversal rate。但论文将此用作 **illustrative example** 说明 aggregate stability 掩盖 local instability，而非作为 population-level estimate。建议在 Section 4.6 中加一句 qualification："This subgroup was selected to illustrate maximum displacement; population-wide pairwise reversal rate is 2.0%."

**[REBUT] R1-M2: GSM1K N=33 在正文标注 "exploratory"**

论文已在正文中使用了 "exploratory" 一词。Section 4.7 原文："an **exploratory** GSM1K analysis suggests DIF captures capability change distinct from memorization"。R1 的建议已被满足。

**[AGREE] R1-M3: DIF audit protocol 阈值缺 formal justification**

同意。我在自己的审稿意见中也指出了同一问题（R2-W4 涉及 protocol 的 framing）。Section 5.3 的 15%/25% 阈值来自 "empirical ρ degradation simulation"，但具体的阈值选择逻辑（为什么是 15% 而非 12% 或 18%）未给出。建议作者在 Section 5.3 或 Appendix 中补充 ρ degradation curve，标注阈值选择的 inflection points。

**[AGREE] R1-M4: 外部资源可获取性**

同意。METABENCH (Kipnis et al. 2024) 是公开数据集，footnote 1 提供了匿名代码仓库。但 PSN-IRT (Zhou et al. 2026) 的 2PL 参数用于 Section 4.1 的 power analysis，其 availability 未明确。建议在 footnote 1 或 Appendix 中注明 "PSN-IRT parameters are available at [URL]" 或 "derived from the publicly available METABENCH matrix."

---

### 汇总

| R1 Issue | 我的判断 | 核心理由 |
|----------|---------|---------|
| W1 K=5 stratification | REBUT（部分） | θ-conditioning with K=20 strata 已等价回答，但 presentation 可更明确 |
| W2 ΔFPR qualification | AGREE | Contribution 2 确实缺少 single-subject 限定 |
| W3 Ecological validity | AGREE | 真实局限，但论文已坦承且 ΔFPR=0 是主要贡献 |
| W4 Cluster bootstrap CI | AGREE | 应在正文 Section 4.2 中提及 |
| W5 "FPR (clean)" terminology | AGREE | 与 Contribution 1 的核心论点自相矛盾 |
| W6 De-duplication interpretation | REBUT（部分） | 8.6pp 降幅受 power reduction confound，qualitative claim 合理但 quantitative framing 偏乐观 |
| M1 Selection bias | AGREE | 补充 qualification 即可 |
| M2 GSM1K "exploratory" | REBUT | 论文 Section 4.7 已标注 "exploratory" |
| M3 Protocol thresholds | AGREE | 与 R2 意见一致 |
| M4 Resource availability | AGREE | PSN-IRT availability 应明确 |

---

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 Weaknesses 的逐条回应

---

### Must-Fix

**[AGREE] R2-W1: Abstract 信息密度过高**
同意。Abstract 单段内确实堆叠了过多数值指标（ΔFPR, ΔTPR, enrichment, φ, C%, ρ, τ, z, pp 数等至少 12 个数字），损害了 first impression 的可读性。作为对比，核心 story 其实可以用三个数字讲清：(1) 31% items 有 temporal DIF；(2) ΔFPR = 0.000 under cross-subject matching；(3) enrichment ≈ 0.96 说明 DIF ≠ contamination。次要指标（φ=0.012、z=-8 to -49、τ≈0.958、具体 C% range 等）完全可以移入正文。不过这是 presentation 问题而非 methodological flaw，不应影响 soundness 评分。

**[REBUT] R2-W2: 缺少 Ethics Statement → desk-reject 风险**
R2 的担忧不成立。根据 EMNLP 2026 / ACL ARR 的提交规范，Responsible NLP Checklist 在 OpenReview submission form 中由作者手动填写，而不是作为论文 PDF 的一个 section。ARR desk-reject checklist（见 reviewer guidelines）列出的条件为：匿名违规、虚构引用、格式/页数违规、缺少 Limitations section、严重 checklist 违规。"Missing Ethics Statement section in PDF" 不在其中。本文已包含 Limitations section（页 9），符合 mandatory 要求。"Ethical Considerations" 在 PDF 中是 optional section（"optional ethical considerations do not count towards this page limit"），不构成 desk-reject 依据。R2 对 desk-reject 风险的判断有误。

---

### Should-Fix

**[AGREE] R2-W3: 新颖性定位需更清晰区分 adaptation 与 application**
部分同意。MH-DIF (Holland & Thayer, 1988) 确实是 off-the-shelf 方法，cross-subject matching 改编自 purified subtest matching (Swaminathan & Rogers, 1990)。论文在 Section 1 contributions 中明确定位为 "methodological and empirical, not algorithmic"，这一自我定位是诚实的。但 R2 的批评仍然成立：论文应更 sharp 地阐述 LLM-specific adaptations 的技术细节——比如 quintile-based stratification 对 bimodal 分布的处理（我在 W1 中也提出了此问题）、multi-domain benchmark 下 cross-subject matching 的具体操作方式、permutation simulation 处理 LD 的方法论贡献。目前这些细节分散在 Section 3.2 的多个 paragraphs 中，不够集中和突出。与 Growing Pains (Habba et al., 2026) 的 practical workflow 整合确实缺乏展开。

不过，新颖性要求需按论文自身定位评判。论文的核心贡献是 (1) ground truth meta-critique 和 (2) 大规模经验发现，而非算法创新。对 empirical contribution papers，ARR guidelines 明确指出不应因缺乏 algorithmic novelty 而降分（"Dismissing results as 'obvious in retrospect' (hindsight bias)"）。建议论文增强 LLM adaptation 的呈现密度，但不应因此一票否决。

**[AGREE] R2-W4: Discussion audit protocol 的 causal framing 与 Limitations 矛盾**
完全同意，这是一个内部一致性问题。Section 5.3 Step 3 (Act) 建议 "review flagged item content, cross-reference with contamination indicators"，但 Section 4.3 实证表明 DIF flags 和 web-overlap labels 的 enrichment ≈ 0.96（近乎独立）。如果两类 flags 测量的是不同概念（论文自己称之为 "category error"），那 cross-reference 预期能找到什么？论文需要解决这一矛盾：要么 (a) 承认 cross-reference 的目的不是验证 contamination 而是排除 non-DIF confounds（如 item quality issues）；要么 (b) 说明 DIF audit protocol 中的 "contamination indicators" 指的是不同于 web-overlap 的 indicators（如 GSM1K-style functional tests）。目前的表述隐含了 DIF → contamination 的因果推断，与 Limitations 中 "detects that not why" 的 agnostic stance 不一致。

**[AGREE] R2-W5: 页数可能超限**
同意这是需要关注的风险。从 PDF 渲染看，Section 6 (Conclusion) 起始于第 9 页顶部——即使只有 ~3 行文字，主体正文（Sections 1–6）在技术上超过了 8 页。LaTeX 源码中 `\enlargethispage{2\baselineskip}` 的存在（Section 5, discussion.tex）进一步证实作者已在挤压版面。虽然 Limitations 不计入 8 页限制，但 Conclusion 是主体正文的一部分。EMNLP 2026 的 "strict 8-page limit" 是 hard constraint，AC 完全有权因此标记 format violation。建议作者压缩 Discussion（Section 5.3 的 audit protocol 可移入 appendix）或 Conclusion 以确保合规。

**[REBUT] R2-W6: Cohort 定义按 release date 划分的 confound**
部分反驳。R2 的问题本身合理（我在 Q4 中也提出了类似问题），但论文已提供了部分 mitigation。Section 4.7 报告了 6-month window analysis（2023-H2 vs. 2024-H1: MMLU C% = 34.35%），表明即使缩小 temporal window 也无法消除 DIF。更关键的是，论文在 Limitations 中明确承认 "Temporal cohorts are defined by calendar year, a coarse grouping; finer-grained definitions (e.g., by training data cutoff or alignment method) might reveal more targeted patterns"。

但 R2 说 "仅用一句话带过" 也有道理——6-month window 结果只出现在 Section 4.7 末尾一句话中，缺乏详细分析。建议作者：(1) 将 6-month window 结果提升为一个 paragraph 并讨论 release date vs. training cutoff 的 potential bias；(2) 如果有 training data cutoff metadata，提供 sensitivity analysis。但这不构成 "must-fix"——release date 是 METABENCH 中可获得的最佳 temporal signal，且论文的核心 claim（items function differently across cohorts）不依赖于 cohort 划分的精确因果解释。

**[REBUT] R2-W7: Multiple testing 论证不够严谨**
不完全同意。论文的 multiple testing 处理有三层防线：

1. **ETS dual threshold**（effect size |Δ_MH| ≥ 1.5 AND p < 0.05）——这不是单纯的 p-value 检验，effect size 门槛本身就是 implicit control（Section 3.2）。
2. **BH FDR correction**（q = 0.05）——Section 4.2 报告 BH 仅移除 3 items（31.32% → 31.30%），说明 ETS dual threshold 已基本覆盖了 FDR control。
3. **Random-split empirical calibration**——0.18% C% 在 null 条件下（Section 4.2, Table 1），这是最强的 empirical evidence。

R2 认为 random-split control "不够突出"——这一点我同意，建议在 Section 4.2 中更明确地将 random-split 的 0.18% 作为 empirical null calibration 的核心证据呈现。但 multiple testing 的方法论本身是 adequate 的，三层防线足以支撑 31.3% 的 claim。教育测量学文献中 ETS classification 的标准做法即为 dual threshold without formal correction（Donoghue & Allen, 1993; Clauser & Maver, 1998），论文遵循了这一领域惯例。

---

### Minor

**[AGREE] R2-M1: 术语不一致**
同意。"Temporal measurement instability"（标题）、"temporal DIF"（正文多处）、"measurement invariance"（Related Work 中提及）三个术语交替使用但含义不完全相同。Measurement invariance 在 psychometrics 中有特定的 IRT-based 定义（Meredith, 1993），与 DIF 是相关但不同的概念。建议统一使用 "temporal DIF" 作为核心术语，仅在引用 psychometric 文献时提及 "measurement invariance"。

**[AGREE] R2-M2: Table 3 Ratio 列跨 benchmark 比较有误导性**
同意。MMLU 的 174× 和 ARC 的 45× 直接对比可能让读者误以为 MMLU "更不稳定"，但 ratio 的差异很大程度上取决于各 benchmark 的 random-split baseline C%（MMLU 0.18% vs. ARC 0.60%），而非 temporal DIF 本身的差异。绝对 C% 的比较（31.3% vs. 26.9%）更有意义。建议在 Table 3 caption 中注明 ratio 受 baseline 影响，或降低 ratio 列的强调程度。

**[REBUT] R2-M3: Figure 1 ICC 图打印版可能难辨**
这是一个可检验的问题。从 PDF 渲染来看（submitted_p2.png），Figure 1 使用了颜色区分两个 cohorts 的 ICC curves，并有虚实线区分。在灰度打印下可能确实不易区分。但 ARR 审稿流程为电子审阅，reviewer 和 AC 查看 PDF 而非打印版，因此灰度可读性不是 blocking issue。如果论文最终被接收进入 camera-ready，建议加粗线条或增加 marker 以改善灰度可读性。

**[AGREE] R2-M4: GSM1K "suggests" 措辞略强**
同意。Section 4.7 原文 "an exploratory GSM1K analysis suggests DIF captures capability change distinct from memorization" 中，N=33 的样本量下用 "suggests" 已经偏强。r = -0.478 虽然 p=0.005，但 bootstrap CI = [-0.71, -0.16] 较宽，且论文自己在 Limitations 中承认 "limited statistical power and is exploratory"。正文和 Limitations 的 hedging 程度不一致。建议改为 "is consistent with" 或 "provides preliminary evidence for"。

**[REBUT] R2-M5: Conclusion 仅 3 行，过于简短**
不同意这是一个缺陷。在 8 页 hard constraint 下，Conclusion 的作用是 summarize 而非 elaborate。当前 3 行 Conclusion 覆盖了三个核心点：(1) cross-subject matching 解决 validation gap；(2) 6 benchmarks 17.9–31.3% temporal instability；(3) 需要 psychometric monitoring。这恰好是论文三个 contributions 的精炼概括。考虑到论文已有完整的 Discussion section（Section 5）覆盖 implications、meta-critique、audit protocol，Conclusion 不需要重复展开。在页数紧张的情况下（R2-W5 已指出可能超限），压缩 Conclusion 是合理的 editorial decision。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-22T05:31:31.539072+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-22T05:31:31.690345+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T05:20:32.435333+00:00\", \"completed_at\": \"2026-05-22T05:22:57.110569+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-6\", \"message\": \"连续约 3.5 页纯文本/近纯文本（仅 page 4 底部有 equation (1)），Related Work + Method 段缺乏 display item 穿插。审稿人在这段可能失去视觉兴趣。建议：将 Appendix 中的某个 figure（如 Figure 3 cross-subject matching 示意）提前到 Method 段，或为 Section 3.3 cohort design 添加一个简洁的 cohort 结构示意图\"}, {\"severity\": \"warning\", \"dimension\": \"pages 6-7\", \"message\": \"Section 4 Experiments 开头（page 6）全是数字堆叠的纯文本，主要结果 Table 1 和 Figure 2 直到 page 7 才出现。审稿人翻到实验部分期待快速看到结果可视化，建议将 Figure 2（dose-response）或 Table 1 提前到 page 6 顶部\"}, {\"severity\": \"warning\", \"dimension\": \"page 14\", \"message\": \"Figures 3、4、5 全部堆积在 appendix 最后一页。Figure 3（cross-subject vs within-subject matching）和 Figure 4（downstream ranking impact）支撑论文核心 claim，考虑将至少一个提升到 main text 的 Section 4.5 或 4.6 附近\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 内部文字（axis labels、legend）字号偏小，约为正文字号的 60%。在打印或低分辨率屏幕上可能不够清晰，建议适当放大 axis label\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 和 Table 2 紧邻排列在同一页，视觉密度高。两表之间的间距足够，但审稿人可能需要反复对照——如果 Table 2 能移到 page 8 顶部会更均衡\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 的 y 轴标签 \\\"True Positive Rate\\\" 和图例文字可再大 1-2pt 以提升可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 3 最优值已加粗标注（如 MMLU 行的 temporal C% = 31.3%），格式规范。但部分行的 ρ_r 列精度不完全统一（0.958 vs 0.997），建议统一到 3 位小数\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"所有表格使用 booktabs 风格（\\\\toprule/\\\\midrule/\\\\bottomrule），无竖线，排版专业\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Equation (1) 渲染正确，2×2 contingency table 公式无错误\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Conclusion + Limitations 占约 60% 页面后转入 References，过渡自然，无异常空白\"}, {\"severity
…[truncated 305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-22T05:31:31.690756+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-22T05:31:31.741205+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-22T05:33:18.725211+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Round 11 (Fresh review, 2026-05-22)\n# R1: 3.5, R2: 3.5 → Consensus 3.5 (Borderline Conference)\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R11-W1\"\n  summary: \"页数超限——正文（Sections 1-6）超过 8 页 hard constraint\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Conclusion 起始于第 9 页顶部，\\\\enlargethispage{2\\\\baselineskip} 证实作者已在挤压。EMNLP 2026 strict 8-page limit 是 hard constraint，AC 可因此 desk-reject。\"\n  action_items:\n    - round: 11\n      action: \"压缩 Discussion §5.3 audit protocol 移入 Appendix，或精简 §4 重复数字陈述，释放 0.3-0.5 页\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"因果归因空白使 audit protocol 不可安全执行\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"§5.3 已改为 'investigate and report'，但缺乏具体可执行步骤。15%/25% 阈值缺乏 LLM 实证依据。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§5.3 Step 3 'cross-reference with contamination indicators' 与 §4.3 enrichment≈0.96 (DIF⊥web-overlap) 矛盾。Protocol 应定位为 measurement monitoring 而非 contamination detection auxiliary。阈值仍缺 formal justification。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"§5.3 去除 contamination 暗示，改为 measurement property monitoring framing；补充 ρ degradation curve 标注阈值 inflection points\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R11-W2\"\n  summary: \"ΔFPR=0.000 在 Contribution 2 中缺少 single-subject 限定\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Abstract 有限定 ('under single-subject contamination')，但 Contribution 2 (§1) 仅写 'achieves ΔFPR=0.000' 无条件。k=10 时 ΔFPR=0.047。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"Contribution 2 加入 '(under single-subject contamination; ΔFPR < 0.007 for k ≤ 5)'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Abstract 信息密度过高，12+ 个数值指标损害可读性\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"单段 abstract 堆叠 ΔFPR, ΔTPR, enrichment, φ, C%, ρ, τ, z, C% range 等数值。核心 story 可用 3 个数字讲清（31%, ΔFPR=0, enrichment≈0.96），secondary metrics 应移入正文。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"Abstract 分层重写：问题→方法贡献→headline 结果→implication；secondary metrics 移入正文\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Table 1 'FPR (clean)' 术语与 Contribution 1 (ground truth meta-critique) 自相矛盾\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"论文论证 web-overlap 不是 DIF ground truth (enrichment≈0.96)，但 Table 1 仍以 web-overlap clean items 定义 'FPR'。概念矛盾。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"Table 1 列名改为 'DIF-C rate (clean subset)' 或 'Flagging rate (web-clean)'，去除 FPR 术语\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W5\"\n  summary: \"Family-level cluster bootstrap CI [26.7%, 53.2%] 应在正文 §4.2 中报告\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Model-level CI [29.4%, 38.1%] 在 §4.2 正文，family-level CI 仅在 Limitations。3.1× 宽度差异说明 family 结构有实质影响，读者仅精读正文会获得 over-precise 估计。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"§4.2 bootstrap CI 处加一句 family-level CI 作为 conservative bound\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W6\"\n  summary: \"新颖性定位需更清晰区分 LLM adaptation vs 标准 purified subtest matching\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Cross-subject matching 有 DIF 文献先例 (Swaminathan 1990, Nandakumar 1993)。LLM-specific adaptations（bimodal distribution, multi-domain LD, extreme model relatedness）的技术细节分散在多处，不够集中突出。与 Growing Pains 的 practical workflow 整合缺乏展开。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"§3.2 增加集中段落列出 3 个 LLM-specific adaptations vs standard purified matching\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W7\"\n  summary: \"Semi-synthetic injection ecological validity 有限，ΔTPR=+0.508 为 upper-bound\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Binary flipping 是 worst-case uniform pattern，真实 contamination（partial memorization, reasoning shortcuts）检测力未知。如果 upper-bound 仅 moderate，realistic lower bound 可能 negligible。但论文核心贡献是 ΔFPR=0 (matching property)，而非 ΔTPR。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"正文讨论 realistic contamination patterns 下 expected TPR degradation 的 qualitative direction\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W8\"\n  summary: \"Graduated de-duplication 解读 quantitative framing 偏乐观\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"K=10 将 C% 从 31.3% 降至 22.7% (8.6pp)，但 'does not inflate C%' 过于绝对。R2 指出 power reduction confound（样本量减少导致 C% 下降），但即使 K=10 仍为 baseline 126×。[R1 raise, R2 partial REBUT]\"\n  action_items:\n    - round: 11\n      action: \"改为 'reduces C% moderately (confounded with power reduction); even K=10 remains >100× above baseline'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO ISSUES\n# ============================================================\n\n- id: \"R11-I1\"\n  summary: \"Cohort 按 release date 划分，training data cutoff lag 讨论不足\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"6-month window analysis 仅一句话。R1 partial rebut: release date 是 METABENCH 可获得的最佳 temporal signal，且核心 claim 不依赖精确因果解释。\"\n  action_items:\n    - round: 11\n      action: \"将 6-month window 结果提升为一个 paragraph，讨论 release date vs training cutoff bias\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-I2\"\n  summary: \"Multiple testing 论证呈现不够突出\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"三层防线 adequate (ETS dual threshold + BH FDR + random-split)，但 random-split 0.18% 作为 empirical null calibration 不够突出。R1 partial rebut: 方法论本身 adequate，遵循教育测量学领域惯例。\"\n  action_items:\n    - round: 11\n      action: \"§4.2 更明确将 random-split 0.18% 呈现为 empirical null calibration 核心证据\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-I3\"\n  summary: \"'200 most displaced models' 33.6% pairwise reversals 有 selection bias\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"按定义选 displacement 最大子集放大了 reversal rate。应注明 conditional + 全样本 flip rate 2.0%。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"§4.6 加 qualification sentence\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-I4\"\n  summary: \"GSM1K 'suggests' 措辞略强于 N=33 exploratory 应有的 hedging\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"论文 §4.7 已标注 'exploratory'，但 'suggests DIF captures...' 仍偏强。改为 'is consistent with'。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"§4.7 'suggests' → 'is consistent with'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-I5\"\n  summary: \"术语不一致：temporal measurement instability / temporal DIF / measurement invariance\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"建议 §3 开头定义三者关系，统一核心术语为 temporal DIF。[AGREE by both]\"\n\n- id: \"R11-I6\"\n  summary: \"Table 3 'Ratio' 列跨 benchmark 比较受 baseline 影响有误导性\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"174× vs 45× 差异主要来自 random baseline 不同，非 DIF 本身差异。caption 应注明。[AGREE by both]\"\n\n- id: \"R11-I7\"\n  summary: \"K=5 quintile 在 bimodal 分布下的 adequacy presentation 不够直接\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 提出 must-fix，R2 rebut: θ-conditioning K=20 (Table 2) 已等价回答 (C%=0.312)。但当前呈现需要读者自行推断等价性。[R2 partial REBUT]\"\n  action_items:\n    - round: 11\n      action: \"§3.2 或 Appendix 加一句桥接：'IRT θ-conditioning with K=20 strata serves as sensitivity check for K=5; results unchanged (Table 2)'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-I8\"\n  summary: \"PSN-IRT parameters 可获取性未明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§4.1 power analysis 用 PSN-IRT 2PL 参数，availability 未说明。[AGREE by both]\"\n\n# ============================================================\n# RESOLVED ISSUES (from prior rounds, carried forward)\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"Permutation null 已补充到 §4.2\"\n  resolution_round: 8\n\n- id: \"R8-MF2\"\n  summary: \"'Drift' framing 超出数据支撑\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Title 改为 'Temporal Measurement Instability'，全文 drift→instability。\"\n  resolution_round: 9\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%.\"\n  resolution_round: 4\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 practical significance paradox\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 11\n  resolution: \"§4.6 已有 family-level profiles (Llama-3 +53, Mistral -35) + pairwise flip rate + Table 3 跨 benchmark ρ/τ/flip。'Diagnostic not destructive' framing effective。\"\n  resolution_round: 11\n\n- id: \"R8-SF1\"\n  summary: \"Proposition 1 过度形式化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"已降格为 Remark（§3.4）。\"\n  resolution_round: 9\n\n- id: \"R9-W2\"\n  summary: \"方法新颖性有限——cross-subject matching 有 DIF 文献先例\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"§3.2 已引用 Swaminathan & Rogers (1990), Nandakumar (1993)，定位为 LLM adaptation。Round 11 要求更集中展开（R11-W6）。\"\n  resolution_round: 10\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Round 11 (Fresh review, 2026-05-22)\n# R1: 3.5, R2: 3.5 → Consensus 3.5 (Borderline Conference)\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R11-W1\"\n  summary: \"页数超限——正文（Sections 1-6）超过 8 页 hard constraint\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Conclusion 起始于第 9 页顶部，\\\\enlargethispage{2\\\\baselineskip} 证实作者已在挤压。EMNLP 2026 strict 8-page limit 是 hard constraint，AC 可因此 desk-reject。\"\n  action_items:\n    - round: 11\n      action: \"压缩 Discussion §5.3 audit protocol 移入 Appendix，或精简 §4 重复数字陈述，释放 0.3-0.5 页\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"因果归因空白使 audit protocol 不可安全执行\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"§5.3 已改为 'investigate and report'，但缺乏具体可执行步骤。15%/25% 阈值缺乏 LLM 实证依据。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§5.3 Step 3 'cross-reference with contamination indicators' 与 §4.3 enrichment≈0.96 (DIF⊥web-overlap) 矛盾。Protocol 应定位为 measurement monitoring 而非 contamination detection auxiliary。阈值仍缺 formal justification。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"§5.3 去除 contamination 暗示，改为 measurement property monitoring framing；补充 ρ degradation curve 标注阈值 inflection points\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R11-W2\"\n  summary: \"ΔFPR=0.000 在 Contribution 2 中缺少 single-subject 限定\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Abstract 有限定 ('under single-subject contamination')，但 Contribution 2 (§1) 仅写 'achieves ΔFPR=0.000' 无条件。k=10 时 ΔFPR=0.047。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"Contribution 2 加入 '(under single-subject contamination; ΔFPR < 0.007 for k ≤ 5)'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Abstract 信息密度过高，12+ 个数值指标损害可读性\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"单段 abstract 堆叠 ΔFPR, ΔTPR, enrichment, φ, C%, ρ, τ, z, C% range 等数值。核心 story 可用 3 个数字讲清（31%, ΔFPR=0, enrichment≈0.96），secondary metrics 应移入正文。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"Abstract 分层重写：问题→方法贡献→headline 结果→implication；secondary metrics 移入正文\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Table 1 'FPR (clean)' 术语与 Contribution 1 (ground truth meta-critique) 自相矛盾\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"论文论证 web-overlap 不是 DIF ground truth (enrichment≈0.96)，但 Table 1 仍以 web-overlap clean items 定义 'FPR'。概念矛盾。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"Table 1 列名改为 'DIF-C rate (clean subset)' 或 'Flagging rate (web-clean)'，去除 FPR 术语\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W5\"\n  summary: \"Family-level cluster bootstrap CI [26.7%, 53.2%] 应在正文 §4.2 中报告\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Model-level CI [29.4%, 38.1%] 在 §4.2 正文，family-level CI 仅在 Limitations。3.1× 宽度差异说明 family 结构有实质影响，读者仅精读正文会获得 over-precise 估计。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"§4.2 bootstrap CI 处加一句 family-level CI 作为 conservative bound\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W6\"\n  summary: \"新颖性定位需更清晰区分 LLM adaptation vs 标准 purified subtest matching\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Cross-subject matching 有 DIF 文献先例 (Swaminathan 1990, Nandakumar 1993)。LLM-specific adaptations（bimodal distribution, multi-domain LD, extreme model relatedness）的技术细节分散在多处，不够集中突出。与 Growing Pains 的 practical workflow 整合缺乏展开。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"§3.2 增加集中段落列出 3 个 LLM-specific adaptations vs standard purified matching\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W7\"\n  summary: \"Semi-synthetic injection ecological validity 有限，ΔTPR=+0.508 为 upper-bound\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Binary flipping 是 worst-case uniform pattern，真实 contamination（partial memorization, reasoning shortcuts）检测力未知。如果 upper-bound 仅 moderate，realistic lower bound 可能 negligible。但论文核心贡献是 ΔFPR=0 (matching property)，而非 ΔTPR。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"正文讨论 realistic contamination patterns 下 expected TPR degradation 的 qualitative direction\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W8\"\n  summary: \"Graduated de-duplication 解读 quantitative framing 偏乐观\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"K=10 将 C% 从 31.3% 降至 22.7% (8.6pp)，但 'does not inflate C%' 过于绝对。R2 指出 power reduction confound（样本量减少导致 C% 下降），但即使 K=10 仍为 baseline 126×。[R1 raise, R2 partial REBUT]\"\n  action_items:\n    - round: 11\n      action: \"改为 'reduces C% moderately (confounded with power reduction); even K=10 remains >100× above baseline'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO ISSUES\n# ============================================================\n\n- id: \"R11-I1\"\n  summary: \"Cohort 按 release date 划分，training data cutoff lag 讨论不足\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"6-month window analysis 仅一句话。R1 partial rebut: release date 是 METABENCH 可获得的最佳 temporal signal，且核心 claim 不依赖精确因果解释。\"\n  action_items:\n    - round: 11\n      action: \"将 6-month window 结果提升为一个 paragraph，讨论 release date vs training cutoff bias\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-I2\"\n  summary: \"Multiple testing 论证呈现不够突出\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"三层防线 adequate (ETS dual threshold + BH FDR + random-split)，但 random-split 0.18% 作为 empirical null calibration 不够突出。R1 partial rebut: 方法论本身 adequate，遵循教育测量学领域惯例。\"\n  action_items:\n    - round: 11\n      action: \"§4.2 更明确将 random-split 0.18% 呈现为 empirical null calibration 核心证据\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-I3\"\n  summary: \"'200 most displaced models' 33.6% pairwise reversals 有 selection bias\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"按定义选 displacement 最大子集放大了 reversal rate。应注明 conditional + 全样本 flip rate 2.0%。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"§4.6 加 qualification sentence\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-I4\"\n  summary: \"GSM1K 'suggests' 措辞略强于 N=33 exploratory 应有的 hedging\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"论文 §4.7 已标注 'exploratory'，但 'suggests DIF captures...' 仍偏强。改为 'is consistent with'。[AGREE by both]\"\n  action_items:\n    - round: 11\n      action: \"§4.7 'suggests' → 'is consistent with'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-I5\"\n  summary: \"术语不一致：temporal measurement instability / temporal DIF / measurement invariance\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"建议 §3 开头定义三者关系，统一核心术语为 temporal DIF。[AGREE by both]\"\n\n- id: \"R11-I6\"\n  summary: \"Table 3 'Ratio' 列跨 benchmark 比较受 baseline 影响有误导性\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"174× vs 45× 差异主要来自 random baseline 不同，非 DIF 本身差异。caption 应注明。[AGREE by both]\"\n\n- id: \"R11-I7\"\n  summary: \"K=5 quintile 在 bimodal 分布下的 adequacy presentation 不够直接\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 提出 must-fix，R2 rebut: θ-conditioning K=20 (Table 2) 已等价回答 (C%=0.312)。但当前呈现需要读者自行推断等价性。[R2 partial REBUT]\"\n  action_items:\n    - round: 11\n      action: \"§3.2 或 Appendix 加一句桥接：'IRT θ-conditioning with K=20 strata serves as sensitivity check for K=5; results unchanged (Table 2)'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-I8\"\n  summary: \"PSN-IRT parameters 可获取性未明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"§4.1 power analysis 用 PSN-IRT 2PL 参数，availability 未说明。[AGREE by both]\"\n\n# ============================================================\n# RESOLVED ISSUES (from prior rounds, carried forward)\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"Permutation null 已补充到 §4.2\"\n  resolution_round: 8\n\n- id: \"R8-MF2\"\n  summary: \"'Drift' framing 超出数据支撑\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Title 改为 'Temporal Measurement Instability'，全文 drift→instability。\"\n  resolution_round: 9\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%.\"\n  resolution_round: 4\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 practical significance paradox\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 11\n  resolution: \"§4.6 已有 family-level profiles (Llama-3 +53, Mistral -35) + pairwise flip rate + Table 3 跨 benchmark ρ/τ/flip。'Diagnostic not destructive' framing effective。\"\n  resolution_round: 11\n\n- id: \"R8-SF1\"\n  summary: \"Proposition 1 过度形式化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"已降格为 Remark（§3.4）。\"\n  resolution_round: 9\n\n- id: \"R9-W2\"\n  summary: \"方法新颖性有限——cross-subject matching 有 DIF 文献先例\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"§3.2 已引用 Swaminathan & Rogers (1990), Nandakumar (1993)，定位为 LLM adaptation。Round 11 要求更集中展开（R11-W6）。\"\n  resolution_round: 10\n"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-22T05:33:18.828698+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 11893}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-22T05:35:30.397050+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 11 (Fresh Review)\n\n**论文**: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**目标 Venue**: EMNLP 2026 (ARR May cycle), Long Paper\n**Reviewers**: R1 (方法严谨性 + 实验可靠性), R2 (新颖性 + 完整性 + 写作质量)\n\n---\n\n## Summary\n\n本文将教育测量学中的 Mantel-Haenszel DIF 分析应用于 METABENCH 响应矩阵（5,227 models × 12,508 MMLU items），发现约 31% 的 items 在 2023 vs 2024 模型 cohorts 间展现 ETS Category C 级别的 temporal DIF。提出 cross-subject matching 消除 FPR 膨胀（ΔFPR = 0.000 under single-subject injection），semi-synthetic injection framework 验证检测力（ΔTPR = +0.508 at p=0.5），并证明 web-overlap contamination labels 与 DIF flags 近乎独立（enrichment ≈ 0.96）。结果在 6 个 METABENCH benchmarks 上复制（C% = 17.9–31.3%）。\n\n---\n\n## Strengths\n\n**S1. 规模空前的心理测量审计**：5,227 models × 12,508 items 的 DIF 分析是目前已知最大规模的 LLM benchmark psychometric audit。6 个 benchmark 的交叉复制增强了结论的外部效度。\n\n**S2. Ground truth meta-critique 是真正的方法论贡献**：用严格实证（enrichment = 0.964, φ = 0.012, Jaccard = 0.206, χ² p = 0.258）证明 web-overlap labels 与 DIF flags 正交，揭示了 contamination detection 文献中系统性的 validation category error。Figure 1 的 ICC 示意图有效传达概念区分。对整个 contamination detection 领域有 immediate methodological implications。\n\n**S3. Cross-subject matching 有理论保证**：Section 3.4 的 Remark 给出 constructive proof（ΔFPR = 0 under single-subject injection），multi-subject injection（Table 5）诚实划定适用边界（k ≤ 5, ΔFPR < 0.007）。\n\n**S4. 实验控制极为周密**：5 种 cohort 对比 + 6 种 structural robustness checks + Simpson's paradox decomposition（92.4% item-specific signal）的 triangulation thoroughness 在 NLP 实证论文中罕见。\n\n**S5. \"Diagnostic, not destructive\" 的 nuanced framing**：ρ ≈ 0.997 aggregate stability 与 family-level rank shifts (Llama-3 +53, Mistral -35) 的 paradox resolution 有层次。避免 overclaiming。\n\n**S6. 写作密度高但条理清晰**：8 页正文内覆盖大量分析，结构合理。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1** [critical, consensus] **页数超限——正文超过 8 页 hard constraint**\n- 具体：Section 6 (Conclusion) 起始于第 9 页顶部。`\\enlargethispage{2\\baselineskip}` 证实作者已在挤压版面。EMNLP 2026 正文 ≤ 8 页是 hard constraint（Limitations 和 References 不计入）。\n- 风险：AC 可因格式违规直接 desk-reject。\n- 建议：将 §5.3 audit protocol 大部分移入 Appendix（正文保留一段 summary），或精简 §4 中的重复性数字陈述。\n- Reviewer consensus: R1 AGREE, R2 raise.\n\n**W2** [critical, consensus] **§5.3 Audit protocol 的 causal framing 与核心发现矛盾**\n- 具体：Limitations 说 \"DIF detects that not why\"，但 §5.3 Step 3 (Act) 建议 \"cross-reference with contamination indicators\"，隐含 DIF → contamination 的因果推断。然而 §4.3 实证表明 DIF flags 与 web-overlap labels enrichment ≈ 0.96（近乎独立）——如果两者正交，cross-reference 预期能找到什么？\n- 问题：Protocol 可操作性依赖于一个论文自己否定的前提。阈值（15%/25%）仅来自 empirical ρ degradation simulation，缺乏 formal justification（inflection points 未标注）。\n- 建议：将 protocol 定位为 \"measurement property monitoring\"（而非 contamination auxiliary）。Step 3 改为 \"review flagged item content for face-validity changes\"。补充 ρ degradation curve 标注阈值选择依据。\n- Reviewer consensus: R1 AGREE, R2 raise.\n\n### Should-Fix（影响评分但不一票否决）\n\n**W3** [warning, consensus] **ΔFPR = 0.000 在 Contribution 2 中缺少 single-subject 限定**\n- Abstract 有 \"under single-subject contamination\" 限定，但 §1 Contribution 2 仅写 \"achieves ΔFPR = 0.000\" 无条件。Table 5 显示 k=10 时 ΔFPR = 0.047。真实 contamination 跨 >5 subjects 完全可能。\n- 建议：Contribution 2 改为 \"achieves ΔFPR = 0.000 under single-subject contamination (ΔFPR < 0.007 for k ≤ 5 subjects)\"。\n- Reviewer consensus: R1 raise, R2 AGREE.\n\n**W4** [warning, consensus] **Abstract 信息密度过高（12+ 数值指标）**\n- 单段 abstract 堆叠 ΔFPR, ΔTPR, enrichment, φ, C%, ρ, τ, z, C% range 等。读者无法在首次阅读时提取核心 story。\n- 建议：分层叙述——问题 → 方法贡献 → headline 结果（31%, ΔFPR=0, enrichment≈0.96）→ implication。Secondary metrics 移入正文。\n- Reviewer consensus: R2 raise, R1 AGREE (presentation issue, not soundness).\n\n**W5** [warning, consensus] **Table 1 \"FPR (clean)\" 术语与 Contribution 1 自相矛盾**\n- 论文核心论点之一是 web-overlap labels 不是 DIF 的 ground truth，但 Table 1 仍以 web-overlap clean items 定义 \"FPR\"。概念上直接矛盾。\n- 建议：列名改为 \"DIF-C rate (clean subset)\" 或 \"Flagging rate (web-clean)\"。\n- Reviewer consensus: R1 raise, R2 AGREE.\n\n**W6** [warning, consensus] **Family-level cluster bootstrap CI 应在 §4.2 正文中报告**\n- Family-level CI [26.7%, 53.2%] 比 model-level CI [29.4%, 38.1%] 宽 3.1×，但仅出现在 Limitations。读者仅精读正文会获得 over-precise 不确定性估计。\n- 建议：§4.2 补充一句 \"Family-level cluster bootstrap yields a wider CI of [26.7%, 53.2%] (see Limitations), confirming robustness.\"\n- Reviewer consensus: R1 raise, R2 AGREE.\n\n**W7** [warning, consensus] **新颖性定位需更集中阐述 LLM-specific adaptations**\n- Cross-subject matching 有 DIF 文献先例（purified subtest matching, Swaminathan 1990, Nandakumar 1993）。LLM-specific adaptations（bimodal ability distribution, multi-domain local dependence, extreme model relatedness, scale）分散在多处，不够集中突出。与 Growing Pains 的 practical workflow 整合缺乏展开。\n- 建议：§3.2 增加集中段落列出 3 个 LLM-specific adaptations vs standard purified matching。\n- 注意：论文自定位为 \"methodological and empirical, not algorithmic\" 是合理的，不应因缺乏 algorithmic novelty 而降分。\n- Reviewer consensus: R2 raise, R1 AGREE.\n\n**W8** [warning, consensus] **Semi-synthetic injection ecological validity 有限**\n- Binary flipping 是 worst-case uniform pattern；真实 contamination（partial memorization, reasoning shortcuts, format-specific advantages）检测力未知。ΔTPR = +0.508 作为 upper-bound 仅 moderate，realistic lower bound 可能 negligible。\n- 缓解因素：论文已在 Limitations 中坦承，且核心贡献是 ΔFPR = 0（matching strategy property）而非 ΔTPR。\n- 建议：正文讨论 realistic contamination patterns 下 expected TPR degradation 的 qualitative direction。\n- Reviewer consensus: R1 raise, R2 AGREE.\n\n**W9** [warning, partial consensus] **Graduated de-duplication quantitative framing 偏乐观**\n- K=10 将 C% 从 31.3% 降至 22.7% (8.6pp)，论文说 \"family structure does not inflate C%\"。R2 指出 power reduction confound（样本量减少导致 C% 下降），qualitative claim 合理但 quantitative framing 过于绝对。\n- 建议：改为 \"reduces C% moderately (confounded with power reduction); even K=10 remains >100× above baseline\"。\n- Reviewer consensus: R1 raise, R2 partial REBUT (power confound).\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成完全共识 [AGREE]：\n1. ΔFPR qualification 不足 (W3)\n2. Abstract 需重构 (W4)\n3. Table 1 FPR 术语矛盾 (W5)\n4. Family-level CI 应更突出 (W6)\n5. Audit protocol causal framing 矛盾 (W2)\n6. 页数超限 (W1)\n7. Semi-synthetic ecological validity 有限 (W8)\n8. GSM1K \"suggests\" 应弱化为 \"is consistent with\"\n9. \"200 most displaced models\" 应注明 selection bias + 全样本 flip rate\n\n## Reviewer Divergence\n\n**K=5 quintile stratification adequacy**：\n- R1 认为 Must-Fix（bimodal 分布下 K=5 不充分，需 K=10/20 sensitivity）\n- R2 REBUT：IRT θ-conditioning with K=20 strata（Table 2, C% = 0.312 vs baseline 0.313）已等价回答，但 presentation 不够直接\n- **Director 判断**：R2 的 rebut 成立——θ-conditioning K=20 实质上是 sensitivity analysis，结果一致。降级为 Info（presentation improvement），不构成 Must-Fix。\n\n**Ethics Statement**：\n- R2 认为 Must-Fix（ARR 要求 Ethics Statement section）\n- R1 REBUT：ARR Responsible NLP Checklist 在 OpenReview form 中填写，非 PDF 必需 section。\"Ethical Considerations\" 在 PDF 中为 optional。\n- **Director 判断**：R1 正确。ARR desk-reject criteria 不包含 \"missing Ethics section in PDF\"。论文已有 Limitations section 满足 mandatory 要求。此问题不成立。\n\n**De-duplication interpretation**：严重程度分歧（R1: should-fix, R2: qualitative claim reasonable but framing optimistic）。双方同意 qualitative conclusion 不变。\n\n---\n\n## Questions for Authors\n\n1. Cross-subject matching 在 single-domain benchmark（如 GSM8K）上如何操作？External matching 引入跨 benchmark ability proxy 假设——如何确保 MMLU score 是 GSM8K ability 的无偏代理？\n2. 92.4% DIF signal 为 item-specific（pseudo R² = 0.0007）——是否测试了其他 item-level features（item length, answer option distribution）？omitted variable bias 如何排除？\n3. Release date 是否与 training data cutoff 对齐？2024 年发布但 training cutoff 在 2022 的模型是否存在于数据中？\n4. §5.3 audit protocol Step 3 \"cross-reference with contamination indicators\" 具体指什么 indicators？如果 web-overlap 与 DIF 正交，哪类 indicators 预期有 signal？\n\n---\n\n## Missing References\n\n- **Penfield & Camilli (2007)** \"Differential Item Functioning\" in *Handbook of Statistics* — DIF 方法论现代综述\n- **Millsap (2011)** \"Statistical Approaches to Measurement Invariance\" — measurement invariance 现代综述（补充 Meredith 1993）\n- **Liang et al. (2022/2023)** HELM: Holistic Evaluation of Language Models — 主流 LLM evaluation framework\n\n（注：Related Work 整体覆盖面已相当好，以上为 minor suggestions。）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 9 info）。主要发现：\n\n**Warnings:**\n- Pages 3–6：连续约 3.5 页纯文本（Related Work + Method），缺乏 display item 穿插。建议将 Appendix Figure 3（cross-subject matching 示意）提前到 Method 段。\n- Pages 6–7：Section 4 开头全是数字堆叠，主要结果 Table 1 和 Figure 2 直到 page 7 才出现。建议将 Figure 2 或 Table 1 提前到 page 6 顶部。\n- Page 14：Figures 3/4/5 全部堆积在 appendix 最后一页。Figure 3（cross-subject vs within-subject matching）和 Figure 4（downstream ranking impact）支撑核心 claim，考虑至少提升一个到 main text。\n\n**Info:**\n- Figure 1 内部文字字号偏小（约正文 60%）\n- Table 1 和 Table 2 紧邻排列在同一页，视觉密度高\n- Figure 2 y轴标签可再大 1-2pt\n- Table 3 精度不完全统一（建议统一 3 位小数）\n- 所有表格使用 booktabs 风格，排版专业\n- Equation (1) 渲染正确\n- 参考文献格式统一，无未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n\n**置信度**: 4/5\n\n**判断依据**：\n\n论文是一项 thorough 的大规模 psychometric audit：\n- Ground truth meta-critique（web-overlap ⊥ DIF）对 contamination detection 社区有 genuine methodological contribution\n- Cross-subject matching 的 zero-FPR guarantee 有清晰理论基础\n- 6 benchmark replication + 5 cohort comparisons + 6 structural controls 的 thoroughness 罕见\n- \"Diagnostic, not destructive\" 的 nuanced framing 避免了 overclaiming\n\n**未达 4.0 的原因**：\n1. **Hard format violation**：页数超限是 desk-reject 风险\n2. **Novelty ceiling**：核心方法为 off-the-shelf MH-DIF 的 LLM application，empirical contribution 为主\n3. **Practical significance paradox**：ρ ≈ 0.997 部分 undermines urgency——虽然论文有效 resolved 了这一 tension，但 reviewer 对 \"so what\" 的疑虑仍存\n4. **Internal consistency gap**：audit protocol 的 causal framing 与核心发现矛盾\n5. **Semi-synthetic ceiling**：upper-bound ΔTPR 仅 moderate，realistic 检测力存疑\n\n**提升至 4.0 的路径**：\n- 修复页数超限（hard requirement）\n- Abstract 重写为 narrative 而非 data dump\n- §5.3 protocol 修正 causal framing + 补充 ρ degradation justification\n- Contribution 2 加限定条件\n- §3.2 集中展示 LLM-specific adaptations\n- Family-level CI 进入正文\n\n以上均为 presentation/framing 修复，不涉及新实验或核心方法改动。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 2 \"achieves ΔFPR = 0.000\" 缺少 \"under single-subject contamination\" 限定\n- 三个 contributions 之间的逻辑链条清晰（meta-critique → validation framework → empirical finding），但 Contribution 3 的 bullet 过长（6 行），建议精简\n\n### Section 3 (Method)\n- §3.2 \"LLM-specific challenges\" 段应更集中展示 adaptations vs standard purified matching\n- §3.4 Remark 的呈现恰当（降格自 Proposition，不过度 formalize）\n- Cross-subject matching, external matching, standard matching 三种策略的适用场景可用一个小 table 总结\n\n### Section 4 (Experiments)\n- §4.2 需同时报告 model-level 和 family-level bootstrap CI\n- §4.4 de-duplication 的 quantitative claim 需 nuance\n- §4.6 \"200 most displaced models\" 需 selection bias qualification + 全样本 reference\n- §4.7 GSM1K \"suggests\" → \"is consistent with\"\n\n### Section 5 (Discussion)\n- §5.3 是页数超限的主要来源；audit protocol 的 actionable 部分可移入 appendix\n- §5.3 去除 contamination 暗示，重新定位为 measurement monitoring\n\n### Limitations\n- 内容充实且诚实，cluster bootstrap CI 的报告值得肯定\n- 建议补充：结论仅适用于 Open LLM Leaderboard 公开模型，对 closed-source models 无法推断\n\n### Format/Presentation\n- Table 1 \"FPR (clean)\" → \"DIF-C rate (clean subset)\"\n- Table 3 Ratio 列 caption 注明受 baseline 影响\n- 术语统一：以 \"temporal DIF\" 为核心术语，首次出现时定义与 measurement invariance 的关系\n",
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 11 (Fresh Review)\n\n**论文**: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**目标 Venue**: EMNLP 2026 (ARR May cycle), Long Paper\n**Reviewers**: R1 (方法严谨性 + 实验可靠性), R2 (新颖性 + 完整性 + 写作质量)\n\n---\n\n## Summary\n\n本文将教育测量学中的 Mantel-Haenszel DIF 分析应用于 METABENCH 响应矩阵（5,227 models × 12,508 MMLU items），发现约 31% 的 items 在 2023 vs 2024 模型 cohorts 间展现 ETS Category C 级别的 temporal DIF。提出 cross-subject matching 消除 FPR 膨胀（ΔFPR = 0.000 under single-subject injection），semi-synthetic injection framework 验证检测力（ΔTPR = +0.508 at p=0.5），并证明 web-overlap contamination labels 与 DIF flags 近乎独立（enrichment ≈ 0.96）。结果在 6 个 METABENCH benchmarks 上复制（C% = 17.9–31.3%）。\n\n---\n\n## Strengths\n\n**S1. 规模空前的心理测量审计**：5,227 models × 12,508 items 的 DIF 分析是目前已知最大规模的 LLM benchmark psychometric audit。6 个 benchmark 的交叉复制增强了结论的外部效度。\n\n**S2. Ground truth meta-critique 是真正的方法论贡献**：用严格实证（enrichment = 0.964, φ = 0.012, Jaccard = 0.206, χ² p = 0.258）证明 web-overlap labels 与 DIF flags 正交，揭示了 contamination detection 文献中系统性的 validation category error。Figure 1 的 ICC 示意图有效传达概念区分。对整个 contamination detection 领域有 immediate methodological implications。\n\n**S3. Cross-subject matching 有理论保证**：Section 3.4 的 Remark 给出 constructive proof（ΔFPR = 0 under single-subject injection），multi-subject injection（Table 5）诚实划定适用边界（k ≤ 5, ΔFPR < 0.007）。\n\n**S4. 实验控制极为周密**：5 种 cohort 对比 + 6 种 structural robustness checks + Simpson's paradox decomposition（92.4% item-specific signal）的 triangulation thoroughness 在 NLP 实证论文中罕见。\n\n**S5. \"Diagnostic, not destructive\" 的 nuanced framing**：ρ ≈ 0.997 aggregate stability 与 family-level rank shifts (Llama-3 +53, Mistral -35) 的 paradox resolution 有层次。避免 overclaiming。\n\n**S6. 写作密度高但条理清晰**：8 页正文内覆盖大量分析，结构合理。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1** [critical, consensus] **页数超限——正文超过 8 页 hard constraint**\n- 具体：Section 6 (Conclusion) 起始于第 9 页顶部。`\\enlargethispage{2\\baselineskip}` 证实作者已在挤压版面。EMNLP 2026 正文 ≤ 8 页是 hard constraint（Limitations 和 References 不计入）。\n- 风险：AC 可因格式违规直接 desk-reject。\n- 建议：将 §5.3 audit protocol 大部分移入 Appendix（正文保留一段 summary），或精简 §4 中的重复性数字陈述。\n- Reviewer consensus: R1 AGREE, R2 raise.\n\n**W2** [critical, consensus] **§5.3 Audit protocol 的 causal framing 与核心发现矛盾**\n- 具体：Limitations 说 \"DIF detects that not why\"，但 §5.3 Step 3 (Act) 建议 \"cross-reference with contamination indicators\"，隐含 DIF → contamination 的因果推断。然而 §4.3 实证表明 DIF flags 与 web-overlap labels enrichment ≈ 0.96（近乎独立）——如果两者正交，cross-reference 预期能找到什么？\n- 问题：Protocol 可操作性依赖于一个论文自己否定的前提。阈值（15%/25%）仅来自 empirical ρ degradation simulation，缺乏 formal justification（inflection points 未标注）。\n- 建议：将 protocol 定位为 \"measurement property monitoring\"（而非 contamination auxiliary）。Step 3 改为 \"review flagged item content for face-validity changes\"。补充 ρ degradation curve 标注阈值选择依据。\n- Reviewer consensus: R1 AGREE, R2 raise.\n\n### Should-Fix（影响评分但不一票否决）\n\n**W3** [warning, consensus] **ΔFPR = 0.000 在 Contribution 2 中缺少 single-subject 限定**\n- Abstract 有 \"under single-subject contamination\" 限定，但 §1 Contribution 2 仅写 \"achieves ΔFPR = 0.000\" 无条件。Table 5 显示 k=10 时 ΔFPR = 0.047。真实 contamination 跨 >5 subjects 完全可能。\n- 建议：Contribution 2 改为 \"achieves ΔFPR = 0.000 under single-subject contamination (ΔFPR < 0.007 for k ≤ 5 subjects)\"。\n- Reviewer consensus: R1 raise, R2 AGREE.\n\n**W4** [warning, consensus] **Abstract 信息密度过高（12+ 数值指标）**\n- 单段 abstract 堆叠 ΔFPR, ΔTPR, enrichment, φ, C%, ρ, τ, z, C% range 等。读者无法在首次阅读时提取核心 story。\n- 建议：分层叙述——问题 → 方法贡献 → headline 结果（31%, ΔFPR=0, enrichment≈0.96）→ implication。Secondary metrics 移入正文。\n- Reviewer consensus: R2 raise, R1 AGREE (presentation issue, not soundness).\n\n**W5** [warning, consensus] **Table 1 \"FPR (clean)\" 术语与 Contribution 1 自相矛盾**\n- 论文核心论点之一是 web-overlap labels 不是 DIF 的 ground truth，但 Table 1 仍以 web-overlap clean items 定义 \"FPR\"。概念上直接矛盾。\n- 建议：列名改为 \"DIF-C rate (clean subset)\" 或 \"Flagging rate (web-clean)\"。\n- Reviewer consensus: R1 raise, R2 AGREE.\n\n**W6** [warning, consensus] **Family-level cluster bootstrap CI 应在 §4.2 正文中报告**\n- Family-level CI [26.7%, 53.2%] 比 model-level CI [29.4%, 38.1%] 宽 3.1×，但仅出现在 Limitations。读者仅精读正文会获得 over-precise 不确定性估计。\n- 建议：§4.2 补充一句 \"Family-level cluster bootstrap yields a wider CI of [26.7%, 53.2%] (see Limitations), confirming robustness.\"\n- Reviewer consensus: R1 raise, R2 AGREE.\n\n**W7** [warning, consensus] **新颖性定位需更集中阐述 LLM-specific adaptations**\n- Cross-subject matching 有 DIF 文献先例（purified subtest matching, Swaminathan 1990, Nandakumar 1993）。LLM-specific adaptations（bimodal ability distribution, multi-domain local dependence, extreme model relatedness, scale）分散在多处，不够集中突出。与 Growing Pains 的 practical workflow 整合缺乏展开。\n- 建议：§3.2 增加集中段落列出 3 个 LLM-specific adaptations vs standard purified matching。\n- 注意：论文自定位为 \"methodological and empirical, not algorithmic\" 是合理的，不应因缺乏 algorithmic novelty 而降分。\n- Reviewer consensus: R2 raise, R1 AGREE.\n\n**W8** [warning, consensus] **Semi-synthetic injection ecological validity 有限**\n- Binary flipping 是 worst-case uniform pattern；真实 contamination（partial memorization, reasoning shortcuts, format-specific advantages）检测力未知。ΔTPR = +0.508 作为 upper-bound 仅 moderate，realistic lower bound 可能 negligible。\n- 缓解因素：论文已在 Limitations 中坦承，且核心贡献是 ΔFPR = 0（matching strategy property）而非 ΔTPR。\n- 建议：正文讨论 realistic contamination patterns 下 expected TPR degradation 的 qualitative direction。\n- Reviewer consensus: R1 raise, R2 AGREE.\n\n**W9** [warning, partial consensus] **Graduated de-duplication quantitative framing 偏乐观**\n- K=10 将 C% 从 31.3% 降至 22.7% (8.6pp)，论文说 \"family structure does not inflate C%\"。R2 指出 power reduction confound（样本量减少导致 C% 下降），qualitative claim 合理但 quantitative framing 过于绝对。\n- 建议：改为 \"reduces C% moderately (confounded with power reduction); even K=10 remains >100× above baseline\"。\n- Reviewer consensus: R1 raise, R2 partial REBUT (power confound).\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成完全共识 [AGREE]：\n1. ΔFPR qualification 不足 (W3)\n2. Abstract 需重构 (W4)\n3. Table 1 FPR 术语矛盾 (W5)\n4. Family-level CI 应更突出 (W6)\n5. Audit protocol causal framing 矛盾 (W2)\n6. 页数超限 (W1)\n7. Semi-synthetic ecological validity 有限 (W8)\n8. GSM1K \"suggests\" 应弱化为 \"is consistent with\"\n9. \"200 most displaced models\" 应注明 selection bias + 全样本 flip rate\n\n## Reviewer Divergence\n\n**K=5 quintile stratification adequacy**：\n- R1 认为 Must-Fix（bimodal 分布下 K=5 不充分，需 K=10/20 sensitivity）\n- R2 REBUT：IRT θ-conditioning with K=20 strata（Table 2, C% = 0.312 vs baseline 0.313）已等价回答，但 presentation 不够直接\n- **Director 判断**：R2 的 rebut 成立——θ-conditioning K=20 实质上是 sensitivity analysis，结果一致。降级为 Info（presentation improvement），不构成 Must-Fix。\n\n**Ethics Statement**：\n- R2 认为 Must-Fix（ARR 要求 Ethics Statement section）\n- R1 REBUT：ARR Responsible NLP Checklist 在 OpenReview form 中填写，非 PDF 必需 section。\"Ethical Considerations\" 在 PDF 中为 optional。\n- **Director 判断**：R1 正确。ARR desk-reject criteria 不包含 \"missing Ethics section in PDF\"。论文已有 Limitations section 满足 mandatory 要求。此问题不成立。\n\n**De-duplication interpretation**：严重程度分歧（R1: should-fix, R2: qualitative claim reasonable but framing optimistic）。双方同意 qualitative conclusion 不变。\n\n---\n\n## Questions for Authors\n\n1. Cross-subject matching 在 single-domain benchmark（如 GSM8K）上如何操作？External matching 引入跨 benchmark ability proxy 假设——如何确保 MMLU score 是 GSM8K ability 的无偏代理？\n2. 92.4% DIF signal 为 item-specific（pseudo R² = 0.0007）——是否测试了其他 item-level features（item length, answer option distribution）？omitted variable bias 如何排除？\n3. Release date 是否与 training data cutoff 对齐？2024 年发布但 training cutoff 在 2022 的模型是否存在于数据中？\n4. §5.3 audit protocol Step 3 \"cross-reference with contamination indicators\" 具体指什么 indicators？如果 web-overlap 与 DIF 正交，哪类 indicators 预期有 signal？\n\n---\n\n## Missing References\n\n- **Penfield & Camilli (2007)** \"Differential Item Functioning\" in *Handbook of Statistics* — DIF 方法论现代综述\n- **Millsap (2011)** \"Statistical Approaches to Measurement Invariance\" — measurement invariance 现代综述（补充 Meredith 1993）\n- **Liang et al. (2022/2023)** HELM: Holistic Evaluation of Language Models — 主流 LLM evaluation framework\n\n（注：Related Work 整体覆盖面已相当好，以上为 minor suggestions。）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 9 info）。主要发现：\n\n**Warnings:**\n- Pages 3–6：连续约 3.5 页纯文本（Related Work + Method），缺乏 display item 穿插。建议将 Appendix Figure 3（cross-subject matching 示意）提前到 Method 段。\n- Pages 6–7：Section 4 开头全是数字堆叠，主要结果 Table 1 和 Figure 2 直到 page 7 才出现。建议将 Figure 2 或 Table 1 提前到 page 6 顶部。\n- Page 14：Figures 3/4/5 全部堆积在 appendix 最后一页。Figure 3（cross-subject vs within-subject matching）和 Figure 4（downstream ranking impact）支撑核心 claim，考虑至少提升一个到 main text。\n\n**Info:**\n- Figure 1 内部文字字号偏小（约正文 60%）\n- Table 1 和 Table 2 紧邻排列在同一页，视觉密度高\n- Figure 2 y轴标签可再大 1-2pt\n- Table 3 精度不完全统一（建议统一 3 位小数）\n- 所有表格使用 booktabs 风格，排版专业\n- Equation (1) 渲染正确\n- 参考文献格式统一，无未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n\n**置信度**: 4/5\n\n**判断依据**：\n\n论文是一项 thorough 的大规模 psychometric audit：\n- Ground truth meta-critique（web-overlap ⊥ DIF）对 contamination detection 社区有 genuine methodological contribution\n- Cross-subject matching 的 zero-FPR guarantee 有清晰理论基础\n- 6 benchmark replication + 5 cohort comparisons + 6 structural controls 的 thoroughness 罕见\n- \"Diagnostic, not destructive\" 的 nuanced framing 避免了 overclaiming\n\n**未达 4.0 的原因**：\n1. **Hard format violation**：页数超限是 desk-reject 风险\n2. **Novelty ceiling**：核心方法为 off-the-shelf MH-DIF 的 LLM application，empirical contribution 为主\n3. **Practical significance paradox**：ρ ≈ 0.997 部分 undermines urgency——虽然论文有效 resolved 了这一 tension，但 reviewer 对 \"so what\" 的疑虑仍存\n4. **Internal consistency gap**：audit protocol 的 causal framing 与核心发现矛盾\n5. **Semi-synthetic ceiling**：upper-bound ΔTPR 仅 moderate，realistic 检测力存疑\n\n**提升至 4.0 的路径**：\n- 修复页数超限（hard requirement）\n- Abstract 重写为 narrative 而非 data dump\n- §5.3 protocol 修正 causal framing + 补充 ρ degradation justification\n- Contribution 2 加限定条件\n- §3.2 集中展示 LLM-specific adaptations\n- Family-level CI 进入正文\n\n以上均为 presentation/framing 修复，不涉及新实验或核心方法改动。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 2 \"achieves ΔFPR = 0.000\" 缺少 \"under single-subject contamination\" 限定\n- 三个 contributions 之间的逻辑链条清晰（meta-critique → validation framework → empirical finding），但 Contribution 3 的 bullet 过长（6 行），建议精简\n\n### Section 3 (Method)\n- §3.2 \"LLM-specific challenges\" 段应更集中展示 adaptations vs standard purified matching\n- §3.4 Remark 的呈现恰当（降格自 Proposition，不过度 formalize）\n- Cross-subject matching, external matching, standard matching 三种策略的适用场景可用一个小 table 总结\n\n### Section 4 (Experiments)\n- §4.2 需同时报告 model-level 和 family-level bootstrap CI\n- §4.4 de-duplication 的 quantitative claim 需 nuance\n- §4.6 \"200 most displaced models\" 需 selection bias qualification + 全样本 reference\n- §4.7 GSM1K \"suggests\" → \"is consistent with\"\n\n### Section 5 (Discussion)\n- §5.3 是页数超限的主要来源；audit protocol 的 actionable 部分可移入 appendix\n- §5.3 去除 contamination 暗示，重新定位为 measurement monitoring\n\n### Limitations\n- 内容充实且诚实，cluster bootstrap CI 的报告值得肯定\n- 建议补充：结论仅适用于 Open LLM Leaderboard 公开模型，对 closed-source models 无法推断\n\n### Format/Presentation\n- Table 1 \"FPR (clean)\" → \"DIF-C rate (clean subset)\"\n- Table 3 Ratio 列 caption 注明受 baseline 影响\n- 术语统一：以 \"temporal DIF\" 为核心术语，首次出现时定义与 measurement invariance 的关系\n",
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-22T05:35:34.814860+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4417
}
```

</details>

---


### Assistant

_source line 560 · 2026-05-22T05:35:45.932881+00:00_

审稿报告已投递。

**Round 11 审稿完成：**

- **Overall: 3.5 / 5 (Borderline Conference)**
- **2 个 Must-Fix**: 页数超限（hard constraint）、audit protocol causal framing 与核心发现矛盾
- **7 个 Should-Fix**: ΔFPR 限定不足、Abstract 信息过载、Table 1 术语矛盾、family-level CI 不突出、novelty positioning 不集中、semi-synthetic ecological validity 有限、de-duplication framing 偏乐观
- **8 个 Info**: cohort 定义讨论不足、multiple testing 呈现、selection bias、GSM1K hedging、术语不一致、Table 3 ratio 误导性、K=5 presentation、PSN-IRT availability

**提升至 4.0 路径**：所有问题均为 presentation/framing 修复，不需要新实验。修复页数超限 + Abstract 重写 + protocol 修正 causal framing + Contribution 2 加限定 + novelty positioning 集中化即可。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 56

## Round 56

2 recorded events


### User

_source line 561 · 2026-05-22T05:35:47.158255+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。汇总：

- **W1 (K=5 stratification)**: REBUT — θ-conditioning with K=20 strata（Appendix B）已提供等价 sensitivity analysis，C% 基本不变（0.312 vs 0.313），但 presentation 可以更明确地桥接
- **W2 (ΔFPR qualification)**: AGREE — Contribution 2 确实缺少 single-subject 限定条件
- **W3 (Ecological validity)**: AGREE — 真实局限，论文已坦承
- **W4 (Cluster bootstrap CI)**: AGREE — 应在正文中更突出
- **W5 ("FPR clean" terminology)**: AGREE — 与核心论点矛盾
- **W6 (De-duplication)**: 部分 REBUT — 8.6pp 降幅受 power reduction confound，但 framing 确实偏乐观
- **M2 (GSM1K exploratory)**: REBUT — 论文已在 Section 4.7 标注 "exploratory"
- **M1, M3, M4**: AGREE

---

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

逐条回应总结：
- **W1 (Abstract 密度)**: [AGREE] — presentation 问题，非方法论缺陷
- **W2 (Ethics Statement)**: [REBUT] — ARR checklist 在 OpenReview form 中填写，PDF 中无需此 section，不存在 desk-reject 风险
- **W3 (新颖性)**: [AGREE] — 但论文自我定位为 empirical contribution，不应因缺乏 algorithmic novelty 一票否决
- **W4 (Audit protocol vs. Limitations 矛盾)**: [AGREE] — 内部一致性问题，Section 5.3 的 cross-reference 建议与 Section 4.3 的 near-independence 发现矛盾
- **W5 (页数超限)**: [AGREE] — Conclusion 起始于第 9 页，技术上主体超 8 页
- **W6 (Release date vs. training cutoff)**: [REBUT] — 论文已有 6-month window 分析和 Limitations 讨论，但呈现不够充分
- **W7 (Multiple testing)**: [REBUT] — 三层防线（ETS dual threshold + BH FDR + random-split calibration）足够，符合教育测量学领域惯例

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 562 · 2026-05-22T05:35:59.006672+00:00_

审稿圆桌会议已完成。

**最终结论：3.5 / 5（Borderline Conference）**

报告已投递至 Research Director。核心判断：

**Must-Fix（2 项）：**
1. 页数超限——正文（含 Conclusion）超过 8 页 hard constraint，desk-reject 风险
2. §5.3 audit protocol 的 causal framing 与 §4.3 核心发现（DIF ⊥ web-overlap）矛盾

**Should-Fix（7 项）：**
- ΔFPR=0.000 在 Contribution 2 中缺限定条件
- Abstract 信息过载需分层重写
- Table 1 "FPR (clean)" 术语矛盾
- Family-level CI 应进入正文
- 新颖性定位需更集中展示 LLM adaptations
- Semi-synthetic ecological validity 讨论不足
- De-duplication quantitative framing 偏乐观

**提升至 4.0 的路径**：均为 presentation/framing 修复（压缩页数、重写 abstract、修正 protocol framing、加限定条件），不涉及新实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 57

## Round 57

60 recorded events


### User

_source line 563 · 2026-05-22T10:16:42.917417+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-22T10:16:49.236925+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-22T10:16:49.288103+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-22T10:16:55.461127+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-22T10:16:55.511668+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-22T10:17:04.748454+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-22T10:17:04.748974+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-22T10:17:07.510673+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-22T10:17:07.561353+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-22T10:17:11.829892+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-22T10:17:12.835995+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-22T10:17:12.836473+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 575 · 2026-05-22T10:17:15.252134+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
  "description": "Check paper file existence and size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
    "description": "Check paper file existence and size"
  }
}
```

</details>

---


### Tool result

_source line 576 · 2026-05-22T10:17:16.206516+00:00_

-rw-r--r-- 1 ubuntu ubuntu 815 May 21 19:15 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex
41 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 577 · 2026-05-22T10:17:16.711066+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check submitted PDF existence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check submitted PDF existence"
  }
}
```

</details>

---


### Tool result

_source line 578 · 2026-05-22T10:17:17.213865+00:00_

-rw-r--r-- 1 ubuntu ubuntu 624807 May 22 09:27 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 579 · 2026-05-22T10:17:17.515389+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 580 · 2026-05-22T10:17:17.566260+00:00_

# Review Issues Tracker — irt_equated_bench_regen
# Round 12 (Post-P35 + 4 additions, 2026-05-22)
# Status: All critical/warning resolved. 4 open info items retained.

# ============================================================
# RESOLVED ISSUES (Round 11 → Round 12)
# ============================================================

- id: "R11-W1"
  summary: "页数超限——正文超过 8 页 hard constraint"
  category: format
  severity: critical
  status: resolved
  first_raised_round: 11
  last_seen_round: 11
  resolution: "§5.3 压缩至 5 行 + Contribution 3 压缩。Conclusion 在 page 8 内。enlargethispage{2\\baselineskip} 合规。15 页 visual check 通过。"
  resolution_round: 12

- id: "R1-W1"
  summary: "§5.3 audit protocol causal framing 与核心发现矛盾"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 11
  resolution: "删除 'cross-reference with contamination indicators'，改为 'review flagged items for differential-performance-associated content characteristics'。新增 predictive model negative finding 句进一步强化 monitoring 定位。"
  resolution_round: 12

- id: "R11-W2"
  summary: "ΔFPR=0.000 在 Contribution 2 中缺少 single-subject 限定"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 11
  last_seen_round: 11
  resolution: "Contribution 2 加 'under single-subject contamination'"
  resolution_round: 12

- id: "R11-W3"
  summary: "Abstract 信息密度过高，12+ 个数值指标损害可读性"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 11
  last_seen_round: 11
  resolution: "删除 φ=0.012、ΔFPR<0.01 for k≤5、45-174×。保持结构不变。"
  resolution_round: 12

- id: "R11-W4"
  summary: "Table 1 'FPR (clean)' 术语与 Contribution 1 自相矛盾"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 11
  last_seen_round: 11
  resolution: "列名改为 'C% (web-clean)' + caption 说明"
  resolution_round: 12

- id: "R11-W5"
  summary: "Family-level cluster bootstrap CI 应在正文 §4.2 报告"
  category: writing
  severity: warning
  status: resolved
  first_raised
…[truncated 5365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-22T10:17:18.871891+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"}]

I've performed a web search for EMNLP 2026 call for papers with ARR submission guidelines.
…[truncated 1395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 6035
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-22T10:17:33.481823+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines page limit author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limit author instructions"
  }
}
```

</details>

---


### Tool call

_source line 583 · 2026-05-22T10:17:33.482332+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 conference dates submission deadline Budapest"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 conference dates submission deadline Budapest"
  }
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-22T10:17:35.089054+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-22T10:17:35.189988+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Measurement Instability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 586 · 2026-05-22T10:17:38.302117+00:00_

Web search results for query: "EMNLP 2026 conference dates submission deadline Budapest"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"When is EMNLP 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/emnlp"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ML-news/c/W-fucfhVto4"}]

Based on the search results, here's the information about EMNLP 2026:

**Conference Dates:**
EMNLP 2026 will be held in Budapest, Hungary from October 24th to October 29th, 2026.

**Submission Deadline:**
The paper submission deadline is May 25, 2026 at 23:59:59 (UTC-12). All submissions go through ACL Rolling Review (ARR), with the ARR submission deadline of May 25, 2026.

**Key Dates:**
Important dates include the ARR submission deadline (long & short papers) May 25, 2026 and Reviewer registration deadline for ALL aut
…[truncated 392 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 4819
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-22T10:17:40.310597+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines page limit author instructions"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on my web search, here's what I found regarding ACL Rolling Review (ARR) 2026 submission guidelines:

## Submission Requirements

The submission must adhere to the formatting in the submission templates, which is available as an Overleaf template. ARR abandoned the MS Word Template for conference submissions, and submissions based on the Wor
…[truncated 1126 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 6828
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-22T10:17:52.558436+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclrollingreview.org CFP 2026 long paper short paper page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclrollingreview.org CFP 2026 long paper short paper page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 589 · 2026-05-22T10:17:54.315919+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
  "description": "List paper section files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
    "description": "List paper section files"
  }
}
```

</details>

---


### Tool result

_source line 590 · 2026-05-22T10:17:54.366750+00:00_

abstract.tex
appendix.tex
conclusion.tex
discussion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-22T10:17:57.479405+00:00_

Web search results for query: "aclrollingreview.org CFP 2026 long paper short paper page limit format requirements"

Links: [{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results for ACL Rolling Review (ARR) CFP 2026, here are the key paper format requirements:

## Page Limits

Long papers have an 8-page limit and short papers have a 4-page limit, not including limitations and ethical considerations.

## Format Requirements

All long, short, and theme papers must follow the ACL Author Guidelines, and paper submissions must use the official ACL style template.

## Submission Format

All submissions must be in PDF format.

## Limitations Section

The limitations and ethical considerations sections do not count towards the page limit. The paper must have a section titled "Limitations" placed according to ACL formatting guidelines.

For more detailed information and to access the official ACL style templates, you can visit the ARR CFP directly at https://aclrollingreview.org/cfp.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 4920
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-22T10:18:04.257625+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-22T10:18:04.612653+00:00_

1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet whether individual items measure the same construct over time is rarely tested---and existing contamination detectors validate against ground truth that conflates global exposure with differential functioning. We develop a semi-synthetic injection framework with cross-subject matching that achieves zero false positive inflation under single-subject contamination ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power under worst-case uniform injection ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$), and show that web-overlap contamination labels are near-independent of Mantel-Haenszel Differential Item Functioning (DIF) flags (enrichment $\approx 0.96$)---exposing a category error in prevailing validation methodology. Applying MH-DIF with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 items), we find 17.9--31.3\% of items exhibit large temporal DIF (ETS~C) between 2023 and 2024 cohorts, with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). This does not threaten aggregate ranking validity ($\rho \approx 0.997$, $\tau \approx 0.958$), but specific model families show concentrated rank shifts (Llama-3: ${+}53$ median positions, Mistral: $-35$) and 2.0\% of pairwise rankings reverse. Item-level decomposition shows 92.4\% of the signal is item-specific; DIF-flagged items concentrate discriminative information ($z = -8$ to $-49$) with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 355
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-22T10:18:04.613567+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-22T10:18:05.117266+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. This pattern persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of the DIF signal is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this measurement instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference~\citep{shi2024mink} to performance-based detectors~\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}. These methods validate d
…[truncated 4871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-22T10:18:05.117741+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-22T10:18:05.469829+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues and \citet{oren2024proving} prove contamination through exchangeability tests. Performance-based detectors identify contamination through statistical anomalies \citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique,deng2024investigating}. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (\Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} assessed test set discriminability, and \citet{rodriguez2021evaluation} demonstrat
…[truncated 3887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-22T10:18:05.470229+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-22T10:18:05.520807+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees 
…[truncated 8426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-22T10:18:10.091940+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-22T10:18:10.695209+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	As approximate parametric bounds, a Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal Comparability: 31\% Measurement Instability}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%], $B = 1{,}000$ model-level resamples; rightward asymmetry reflects heavy-tailed C\% from subjects exceeding 40\%; family-level cluster bootstrap over 29 families with $\geq$3 members yields a wider CI of $[26.7\%, 53.2\%]$, $3.1\times$ the model-level width, confirming robustness under within-family dependence). Leave-one-family-out analysis confirms that no single non-dominant family drives the signal ($|
…[truncated 10847 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-22T10:18:10.695749+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-22T10:18:11.147934+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\enlargethispage{2\baselineskip}
4	
5	\subsection{Implications for Benchmark Temporal Comparability}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF decomposes benchmark differences into impact (ability differences removed by matching, $\sim$2.4~pp), DIF (item-level differences after ability control, $\sim$28--29\% floor, 92.4\% item-specific), and attribution (contamination, capability evolution, or methodology shifts---underdetermined without training data).
10	
11	\subsection{Ground Truth Meta-Critique}
12	\label{sec:disc_groundtruth}
13	
14	\looseness=-1
15	The near-independence between DIF flags and web-overlap labels (\Cref{sec:groundtruth}) reflects a category error: web-overlap measures global exposure while DIF measures differential functioning. Semi-synthetic dose-response confirms detection works when present; the disconnect is in the ground truth.
16	
17	\subsection{Recommended DIF Audit Protocol}
18	\label{sec:disc_protocol}
19	
20	\looseness=-1
21	Item-level properties do not reliably predict DIF susceptibility (AUROC $= 0.60$; \Cref{app:predictive}), confirming that post-hoc monitoring cannot be replaced by pre-screening.
22	We propose temporal MH-DIF whenever $\geq$500 models accumulate, with $\rho$-degradation-grounded action levels (\Cref{app:fig_rho_degradation}):
23	(1)~\emph{Monitor} (C\% $< 15\%$): report C\% in release notes.
24	(2)~\emph{Flag} ($15$--$25\%$): report stable-item rankings as sensitivity analysis alongside full rankings.
25	(3)~\emph{Act} (C\% $\geq 25\%$): review flagged items for differential-performance-associated content characteristics; report stable-item rankings as primary metric; use DIF pre-screening to identify stable anchors for equating~\citep{kolen2014equating,habba2026growingpains}.
26	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-22T10:18:11.148403+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-22T10:18:11.700876+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-1
5	Cross-subject matching ($\Delta\mathrm{FPR} = 0.000$) resolves the validation gap: web-overlap labels are near-independent of DIF flags (enrichment $\approx 0.96$). Across six benchmarks, 17.9--31.3\% of items exhibit temporal instability; LLM benchmarks need psychometric monitoring alongside score reporting.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-22T10:18:11.701210+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-22T10:18:11.751668+00:00_

1	\section*{Limitations}
2	
3	\paragraph{Methodological scope.}
4	MH-DIF detects only uniform DIF; logistic regression reveals an additional 24.8\% non-uniform DIF, making 31\% conservative. More fundamentally, DIF detects \emph{that} items function differently but cannot determine \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts. A definitive causal decomposition remains out of reach without access to model training data. The semi-synthetic framework uses binary response flipping (incorrect $\to$ correct) to simulate differential contamination, representing a worst-case uniform exploitation pattern. Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages; detection power under such realistic patterns is untested. The moderate $\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$ reflects sensitivity to severe differential behavior; the framework's primary methodological contribution---cross-subject matching achieving $\Delta\mathrm{FPR} = 0.000$---is a matching strategy property independent of injection realism.
5	
6	\paragraph{Examinee non-independence.}
7	The MH $\chi^2$ test assumes independent examinees, yet LLMs sharing base models, training data, or architectures violate this assumption. Empirical mitigations partially address this: permutation simulation bounds LD-attributable FPR inflation to ${<}0.001$~pp, and graduated de-duplication ($K{=}20$: C\% $= 29.1\%$) shows family structure does not inflate results. \citet{french2010hierarchical} show that MH maintains nominal size under moderate clustering in educational settings, consistent with our empirical findings; however, the extreme relatedness of some LLM families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in that work. Cluster bootstrap resampling at the family level (29 families with $\geq$3 members, 1{,}882 models, $B = 1{,}000$) yields a 95\% CI of $[26.7\%, 53.2\%]$, $3.1
…[truncated 1454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-22T10:18:16.723498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-22T10:18:16.925060+00:00_

1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini
…[truncated 10679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-22T10:18:17.076329+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-22T10:18:17.127138+00:00_

1	% ============================================================
2	% Benchmark Contamination Detection
3	% ============================================================
4	
5	@inproceedings{balloccu2024leak,
6	  title     = {Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source {LLMs}},
7	  author    = {Balloccu, Simone and Schmidtova, Patrícia and Lango, Mateusz and Dusek, Ondrej},
8	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
9	  year      = {2024},
10	  doi       = {10.18653/v1/2024.eacl-long.5},
11	  url       = {https://arxiv.org/abs/2402.03927}
12	}
13	
14	@inproceedings{dekoninck2024constat,
15	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
16	  author    = {Dekoninck, Jasper and Mueller, Mark Niklas and Vechev, Martin},
17	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
18	  year      = {2024},
19	  url       = {https://arxiv.org/abs/2405.16281}
20	}
21	
22	@inproceedings{golchin2024timetravel,
23	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
24	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
25	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
26	  year      = {2024},
27	  url       = {https://arxiv.org/abs/2308.08493}
28	}
29	
30	@inproceedings{li2024contamination,
31	  title     = {An Open-Source Data Contamination Report for Large Language Models},
32	  author    = {Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua},
33	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
34	  year      = {2024},
35	  doi       = {10.18653/v1/2024.findings-emnlp.30},
36	  url       = {https://aclanthology.org/2024.findings-emnlp.30/}
37	}
38	
39	@misc{liang2026dvd,
40	  title         = {{DVD}: A Robust Method for Detecting Variant Conta
…[truncated 8076 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-22T10:18:34.251166+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool call

_source line 613 · 2026-05-22T10:18:34.402235+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 614 · 2026-05-22T10:18:34.402842+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-22T10:18:34.403196+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-22T10:19:01.357969+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-22T10:19:29.134496+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 27776
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-22T10:19:29.336157+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ACL Rolling Review)\n- **类别**: Long Paper (8 页正文限制, unlimited refs, Limitations 不计入页数)\n- **匿名规则**: Double-blind (ACL style, \\usepackage[review]{acl})\n- **截止日期**: 2026-05-25\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/submitted.pdf`\n\n## 论文概要\n本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，使用 METABENCH 响应矩阵（5,227 models × 12,508 MMLU items）发现 ~31% 的 MMLU items 在 2023 vs 2024 模型群体间展现 large temporal DIF (ETS C)。主要方法贡献是 cross-subject matching 实现 ΔFPR=0.000，以及 semi-synthetic injection 框架验证检测能力。\n\n## 你的审查侧重\n\n**1. MH-DIF 方法论适用性**\n- MH-DIF 从教育测量迁移到 LLM 评估的假设是否成立？examinees 非独立性（model families 共享训练数据/架构）对 MH chi-squared test 的影响是否充分讨论？\n- K=5 quintile stratification 在 bimodal ability distribution (base vs instruction-tuned) 下是否适当？\n- Unidimensionality 假设在 57-subject MMLU 上是否合理？cross-subject matching 是否充分解决该问题？\n\n**2. Semi-synthetic 框架有效性**\n- Binary response flipping 是否是合理的 contamination 模拟？ecological validity 如何？\n- ΔFPR=0.000 的 \"constructive guarantee\" claim 是否过强？multi-subject injection 的 boundary (k≤5) 是否实际适用？\n- TPR 被标注为 upper-bound estimate——这个限定是否足够显著？\n\n**3. 统计推断合理性**\n- Bootstrap CI [29.4%, 38.1%] vs family-level cluster bootstrap CI [26.7%, 53.2%]——3.1x width 差异暗示什么？\n- Multiple testing: ETS dual threshold 作为 implicit multiple testing protection 的论证是否充分？BH correction 只移除 3 items 是否说明问题？\n- Permutation test 的设置是否恰当？1,000 iterations 是否足够？\n\n**4. 控制实验充分性**\n- Random split (0.18%), ability quintile (2.9%), temporal (31.3%) 的阶梯是否构成充分的 validity 论证？\n- Matched-ability analysis 将 C% 从 31.3% 降至 28.9%——2.4pp attributable to ability mismatch 的解读是否合理？\n- LOFO robustness: 移除 Mistral/Llama-3 后 C% 大幅下降是否是 concern 而非仅仅是 power reduction？\n- Within-family (Llama-2 vs Llama-3) 61.3% C% 的解读是否恰当？\n\n**5. Cross-benchmark 外推**\n- 6 个 METABENCH benchmark 的结构差异大（MMLU 12K items vs TruthfulQA 817 items），statistical power 差异是否影响 C% 的可比性？\n- GSM1K correlation (r=-0.478, N=33) 的 exploratory nature 是否充分标注？\n\n请严格评审，给出 Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、Missing References，以及 Overall Assessment。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ACL Rolling Review)\n- **类别**: Long Paper (8 页正文限制, unlimited refs, Limitations 不计入页数)\n- **匿名规则**: Double-blind (ACL style, \\usepackage[review]{acl})\n- **截止日期**: 2026-05-25\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/submitted.pdf`\n\n## 论文概要\n本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，使用 METABENCH 响应矩阵（5,227 models × 12,508 MMLU items）发现 ~31% 的 MMLU items 在 2023 vs 2024 模型群体间展现 large temporal DIF (ETS C)。主要方法贡献是 cross-subject matching 实现 ΔFPR=0.000，以及 semi-synthetic injection 框架验证检测能力。\n\n## 你的审查侧重\n\n**1. MH-DIF 方法论适用性**\n- MH-DIF 从教育测量迁移到 LLM 评估的假设是否成立？examinees 非独立性（model families 共享训练数据/架构）对 MH chi-squared test 的影响是否充分讨论？\n- K=5 quintile stratification 在 bimodal ability distribution (base vs instruction-tuned) 下是否适当？\n- Unidimensionality 假设在 57-subject MMLU 上是否合理？cross-subject matching 是否充分解决该问题？\n\n**2. Semi-synthetic 框架有效性**\n- Binary response flipping 是否是合理的 contamination 模拟？ecological validity 如何？\n- ΔFPR=0.000 的 \"constructive guarantee\" claim 是否过强？multi-subject injection 的 boundary (k≤5) 是否实际适用？\n- TPR 被标注为 upper-bound estimate——这个限定是否足够显著？\n\n**3. 统计推断合理性**\n- Bootstrap CI [29.4%, 38.1%] vs family-level cluster bootstrap CI [26.7%, 53.2%]——3.1x width 差异暗示什么？\n- Multiple testing: ETS dual threshold 作为 implicit multiple testing protection 的论证是否充分？BH correction 只移除 3 items 是否说明问题？\n- Permutation test 的设置是否恰当？1,000 iterations 是否足够？\n\n**4. 控制实验充分性**\n- Random split (0.18%), ability quintile (2.9%), temporal (31.3%) 的阶梯是否构成充分的 validity 论证？\n- Matched-ability analysis 将 C% 从 31.3% 降至 28.9%——2.4pp attributable to ability mismatch 的解读是否合理？\n- LOFO robustness: 移除 Mistral/Llama-3 后 C% 大幅下降是否是 concern 而非仅仅是 power reduction？\n- Within-family (Llama-2 vs Llama-3) 61.3% C% 的解读是否恰当？\n\n**5. Cross-benchmark 外推**\n- 6 个 METABENCH benchmark 的结构差异大（MMLU 12K items vs TruthfulQA 817 items），statistical power 差异是否影响 C% 的可比性？\n- GSM1K correlation (r=-0.478, N=33) 的 exploratory nature 是否充分标注？\n\n请严格评审，给出 Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、Missing References，以及 Overall Assessment。"
  }
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-22T10:19:52.952774+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23616
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-22T10:19:53.204210+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 写作完整性 + 格式合规**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ACL Rolling Review)\n- **类别**: Long Paper (8 页正文限制, unlimited refs, Limitations 不计入页数)\n- **匿名规则**: Double-blind (ACL style, \\usepackage[review]{acl})\n- **截止日期**: 2026-05-25\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/submitted.pdf`\n\n## 论文概要\n本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，使用 METABENCH 响应矩阵（5,227 models × 12,508 MMLU items）发现 ~31% 的 MMLU items 在 2023 vs 2024 模型群体间展现 large temporal DIF (ETS C)。论文声称三项贡献：(1) ground truth meta-critique（web-overlap labels 与 DIF flags 近独立），(2) semi-synthetic validation framework（cross-subject matching ΔFPR=0.000），(3) temporal measurement instability at scale（31% C%, replicated across 6 benchmarks）。\n\n## 你的审查侧重\n\n**1. 新颖性评估**\n- 三项贡献的 novelty 层次：MH-DIF 本身是 1988 年的方法，cross-subject matching 有 psychometric precedent (Swaminathan & Rogers 1990, Nandakumar 1993)——那么真正的 novelty 是什么？\"application context\" 是否足以构成 EMNLP venue 的贡献？\n- 与 Growing Pains (Habba et al. 2026) 的区分是否清晰？两者都在做 LLM benchmark 的 psychometric analysis——complementarity claim 是否有实质支撑？\n- Ground truth meta-critique 是否已被其他工作隐含指出？是否是 genuine contribution 还是 incremental observation？\n\n**2. Related Work 覆盖度**\n- DIF methodology 部分是否遗漏关键引用？特别是 LLM evaluation 领域的 recent work\n- 是否有未提及的 concurrent work 在做类似的 temporal analysis？\n- Measurement invariance / fairness testing 文献是否充分？\n\n**3. 叙事逻辑与写作质量**\n- \"diagnostic not destructive\" framing 是否一致贯穿全文？是否有地方暗示 DIF 是 benchmark 的 defect？\n- Abstract 信息密度：是否包含过多数值（ρ, τ, Jaccard, φ, enrichment, C%, ΔFPR, ΔTPR...）？\n- Contributions 的层次是否清晰？\"methodological and empirical, not algorithmic\" 的 self-positioning 是否准确？\n- Discussion §5.3 audit protocol 的 causal 暗示——\"review flagged items for differential-performance-associated content characteristics\" 是否与论文反复强调的 \"detects THAT not WHY\" 矛盾？\n\n**4. 格式合规（EMNLP 2026 / ARR）**\n- **页数**：正文是否在 8 页以内？检查 `\\enlargethispage` 使用是否合规\n- **匿名性**：是否有 de-anonymization 风险？检查 URL、致谢、数据引用\n- **Limitations 章节**：是否存在且适当？是否包含过多额外内容？\n- **模板**：`\\usepackage[review]{acl}` 是否正确？\n- **References 格式**：是否遵循 ACL bibliography 标准？\n\n**5. Tables & Figures**\n- 5 张 figures + 多张 tables 在 8 页内是否导致信息过载？\n- Figure/Table captions 是否 self-contained？\n- 数值精度是否一致？（例如 ρ=0.997 vs C%=31.3%）\n\n请严格评审，给出 Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、Missing References，以及 Overall Assessment。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 写作完整性 + 格式合规**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ACL Rolling Review)\n- **类别**: Long Paper (8 页正文限制, unlimited refs, Limitations 不计入页数)\n- **匿名规则**: Double-blind (ACL style, \\usepackage[review]{acl})\n- **截止日期**: 2026-05-25\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_6/submitted.pdf`\n\n## 论文概要\n本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，使用 METABENCH 响应矩阵（5,227 models × 12,508 MMLU items）发现 ~31% 的 MMLU items 在 2023 vs 2024 模型群体间展现 large temporal DIF (ETS C)。论文声称三项贡献：(1) ground truth meta-critique（web-overlap labels 与 DIF flags 近独立），(2) semi-synthetic validation framework（cross-subject matching ΔFPR=0.000），(3) temporal measurement instability at scale（31% C%, replicated across 6 benchmarks）。\n\n## 你的审查侧重\n\n**1. 新颖性评估**\n- 三项贡献的 novelty 层次：MH-DIF 本身是 1988 年的方法，cross-subject matching 有 psychometric precedent (Swaminathan & Rogers 1990, Nandakumar 1993)——那么真正的 novelty 是什么？\"application context\" 是否足以构成 EMNLP venue 的贡献？\n- 与 Growing Pains (Habba et al. 2026) 的区分是否清晰？两者都在做 LLM benchmark 的 psychometric analysis——complementarity claim 是否有实质支撑？\n- Ground truth meta-critique 是否已被其他工作隐含指出？是否是 genuine contribution 还是 incremental observation？\n\n**2. Related Work 覆盖度**\n- DIF methodology 部分是否遗漏关键引用？特别是 LLM evaluation 领域的 recent work\n- 是否有未提及的 concurrent work 在做类似的 temporal analysis？\n- Measurement invariance / fairness testing 文献是否充分？\n\n**3. 叙事逻辑与写作质量**\n- \"diagnostic not destructive\" framing 是否一致贯穿全文？是否有地方暗示 DIF 是 benchmark 的 defect？\n- Abstract 信息密度：是否包含过多数值（ρ, τ, Jaccard, φ, enrichment, C%, ΔFPR, ΔTPR...）？\n- Contributions 的层次是否清晰？\"methodological and empirical, not algorithmic\" 的 self-positioning 是否准确？\n- Discussion §5.3 audit protocol 的 causal 暗示——\"review flagged items for differential-performance-associated content characteristics\" 是否与论文反复强调的 \"detects THAT not WHY\" 矛盾？\n\n**4. 格式合规（EMNLP 2026 / ARR）**\n- **页数**：正文是否在 8 页以内？检查 `\\enlargethispage` 使用是否合规\n- **匿名性**：是否有 de-anonymization 风险？检查 URL、致谢、数据引用\n- **Limitations 章节**：是否存在且适当？是否包含过多额外内容？\n- **模板**：`\\usepackage[review]{acl}` 是否正确？\n- **References 格式**：是否遵循 ACL bibliography 标准？\n\n**5. Tables & Figures**\n- 5 张 figures + 多张 tables 在 8 页内是否导致信息过载？\n- Figure/Table captions 是否 self-contained？\n- 数值精度是否一致？（例如 ρ=0.997 vs C%=31.3%）\n\n请严格评审，给出 Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、Missing References，以及 Overall Assessment。"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-22T10:19:54.925194+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1720
}
```

</details>

---


### Assistant

_source line 622 · 2026-05-22T10:20:11.475755+00:00_

已并行派发：
- ✅ 视觉审查 Agent（fire-and-forget）
- ✅ Reviewer 1（方法严谨性 + 实验有效性）
- ✅ Reviewer 2（新颖性 + 写作完整性 + 格式合规）

等待两位 Reviewer 完成 Round 1 独立初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 58

## Round 58

2 recorded events


### User

_source line 623 · 2026-05-22T10:25:51.511461+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 1 审稿意见

**论文**: Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models
**Venue**: EMNLP 2026 (ACL Rolling Review)
**审查侧重**: 方法严谨性 + 实验有效性

---

## 总体评分

**Overall Assessment: 3.5 (Borderline Conference)**

**一句话总结**: 将教育测量 MH-DIF 方法系统迁移至 LLM benchmark 评估具有真实的方法论贡献和实践意义，控制实验层次丰富，但 LOFO 分析暴露的 family-concentration 问题以及 examinee non-independence 的影响未被充分量化，削弱了核心 claim 的确信度。

---

## 官方维度打分（ACL ARR Review Form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 核心 MH-DIF 方法论迁移合理，5 组控制实验构成有力的 validity ladder，但 LOFO 分析中 Mistral/Llama-3 移除导致 C% 大幅下降（22.5%/24.1%）未被充分解释，non-independence 对 chi-squared inflation 的定量影响不明 |
| **Excitement** | 3.5/5 | 首次大规模将 psychometric DIF 引入 LLM 评估，规模（5,227 models × 12,508 items）和跨 benchmark 复现令人印象深刻，但因果归因受限（无法区分 contamination vs. capability evolution）限制了实际可操作性 |
| **Reproducibility** | 4/5 | 代码和数据明确提到可用（脚注1），METABENCH 为公开数据，方法细节充分（K=5 stratification、ETS thresholds、bootstrap replications 均有报告） |
| **Confidence** | 4/5 | 熟悉 DIF 方法论和 LLM benchmark 评估文献，仔细检查了关键统计推断 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] LOFO family-concentration 效应被低估，power-reduction 解释不充分

- **具体位置**: Table 6 (Appendix B), Section 4.4 ("Ability-matched analysis reduces…none reduces C% below ~28%"), Limitations §9
- **问题**: 移除 Mistral（547 models, 51% ref）后 C% 从 31.3% 降至 22.5%（-8.8pp），移除 Llama-3（315 models, 39% focal）后降至 24.1%（-7.3pp）。论文将此归因于"power reduction from smaller remaining samples"，但移除 Mistral 后 N_ref 仍有 ~533，移除 Llama-3 后 N_focal 仍有 ~492——远超 Section 4.1 power analysis 中 N ≥ 80 即可达到 TPR = 0.68–0.80 的阈值。N_ref = 533 + N_focal = 807 的 total sample 仍达 1,340（原始 1,887 的 71%），仅凭 power reduction 难以解释 8.8pp 的 C% 下降。
- **更深层问题**: Section 4.4 称"six alternative combinations were tested; none reduces C% below ~28%"，但这里的"alternative combinations"指的是 matching/control 策略（Table 2 structural approaches），而非 LOFO。这种行文结构让读者误以为 ~28% 是所有稳健性检验的下界，但 LOFO 结果（22.5%, 24.1%）明确低于此。两类 robustness 结果之间的 tension 未被讨论。
- **为什么影响接收**: 如果 DIF 信号高度集中于 Mistral 和 Llama-3 家族，则"~31% of MMLU items exhibit temporal DIF"的 claim 实质上是"~31% of items exhibit Mistral/Llama-3-specific DIF"——这是完全不同的结论，大幅降低了方法的普适性。
- **建议修改方向**:
  1. 对 LOFO 进行 **expected power calibration**：使用 Section 4.1 的 Monte Carlo power analysis 框架，在 N_ref = 533, N_focal = 807 的条件下模拟 expected C%，与观测到的 22.5% 对比，量化"power reduction explains X pp of the 8.8pp drop"
  2. 将 LOFO 结果与 matching-based robustness 明确区分讨论，不要让 ~28% floor 的表述覆盖 LOFO 发现
  3. 考虑 **family-weighted C%**（按 family 加权而非按 model 加权），如果 Mistral 和 Llama-3 家族的 DIF pattern 显著不同于其他家族，这本身就是重要发现

**N2** [critical] Examinee non-independence 对 MH chi-squared 的 inflation 效应缺乏直接定量

- **具体位置**: Section 3.2 ("LLM-Specific Challenges"), Appendix A.2 (Structural Analysis), Limitations §9
- **问题**: 论文承认 LLM 共享 base models/training data 违反 local independence 假设，并提供三项间接证据：(a) permutation FPR inflation < 0.001pp; (b) graduated de-duplication K=20 → C% = 29.1%; (c) cluster bootstrap CI [26.7%, 53.2%]。但这三项均未直接量化 non-independence 对 MH chi-squared 统计量的 inflation 程度：
  - (a) Permutation test 衡量的是 label-shuffling 下的 FPR，不直接回答"correlated examinees 使多少本不显著的 items 变显著了"
  - (b) Graduated de-duplication 同时改变了 sample size 和 within-family correlation，两个效应混淆（论文自己承认"confounded with statistical power reduction"）
  - (c) Cluster bootstrap 给出了正确的 CI，但 upper bound 53.2% 意味着 point estimate 的不确定性巨大——论文以 lower bound 26.7% > random baseline (0.18%) 论证稳健性，但 26.7% 到 53.2% 这个 range 本身就说明 family-level clustering 对 point estimate 有 massive impact
- **为什么影响接收**: MH chi-squared test 的 Type I error rate 在 correlated observations 下是 inflated 的（这在教育测量文献中有广泛记录）。不量化这个 inflation，就无法确信 31.3% 的 C 类 items 中有多少是 genuine DIF vs. inflated significance。
- **建议修改方向**:
  1. 使用 **design effect (DEFF)** 或 **effective sample size** 方法：估计 intra-family correlation (ICC)，计算 DEFF = 1 + (m̄ - 1) × ICC（m̄ = average family size），调整 MH chi-squared 的自由度或临界值，重新计算 C%
  2. 或者：在 graduated de-duplication 框架中，固定 total N（通过 oversampling smaller families），仅减少 within-family correlation，分离 power 和 correlation 两个效应

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Semi-synthetic injection 的 ecological validity 有限，但 claim 表述偏强

- **具体位置**: Section 3.4 ("Semi-Synthetic Injection Framework"), Section 4.5, Limitations §9
- **问题**: Binary response flipping（将 ETS A items 的 incorrect → correct）模拟的是最极端的 uniform contamination——所有 injected items 在 focal group 中以相同概率 p 被"解决"。但现实中 contamination 的 pattern 远更复杂：
  - 不同 items 的 memorization 难度不同（long-context items vs. short factoid items）
  - Contamination 可能影响同一 subject 的部分 items 而非全部
  - Response flipping 只模拟 unidirectional DIF (focal better)，而论文发现 Humanities items 64.4% favor 2023（即反方向 DIF）
  - 论文自己报告 moderate ΔTPR = +0.508 at p = 0.5，并标注为"upper-bound estimate"，但这个 caveat 只在 Limitations 一笔带过
- **建议**: (a) 在 Section 3.4 明确列出 "worst-case uniform" 这一假设及其局限性（不仅在 Limitations）; (b) 补充一个 heterogeneous injection 实验（e.g., flipping probability 与 item difficulty 相关），即使 ΔTPR 更低也能增强 framework 的 ecological validity

**W2** [warning] Bootstrap CI 的 3.1× width 差异暗示 family-level dependence 结构性影响了 inference，但未被纳入 primary results reporting

- **具体位置**: Section 4.2 ("95% bootstrap CI [29.4%, 38.1%]…family-level cluster bootstrap CI [26.7%, 53.2%]")
- **问题**: 论文 primary result 报告的是 model-level bootstrap CI [29.4%, 38.1%]，cluster bootstrap 仅作为 robustness check。但 model-level bootstrap **假设 models are independent**——这正是论文承认被违反的假设。在该假设被违反的情况下，cluster bootstrap 是更合适的推断方法，应该作为 primary CI 报告。当 primary CI 变为 [26.7%, 53.2%] 时，结论的表述需要相应调整（e.g., "approximately 27%–53% of items" 而非 "approximately 31%"）。
- **建议**: 将 family-level cluster bootstrap CI 提升为 primary inference，或至少在 abstract/introduction/conclusion 中同时报告两个 CI

**W3** [warning] Cross-benchmark C% 可比性受 statistical power 差异影响，但未调整

- **具体位置**: Table 3 (Section 4.7), Section 5
- **问题**: 6 个 benchmark 的 item 数量差异巨大（MMLU 12,508 vs. TruthfulQA 817 vs. GSM8K 1,319）。MH-DIF 的 power 与 item-level sample size 无关，但与 **model count per stratum** 有关。不同 benchmark 的 model overlap 可能不同（GSM8K 有 6,702 models vs. MMLU 5,227），导致 per-stratum N 不同。但更关键的是：每个 benchmark 的 **item-level** C% 直接取决于 |ΔMH| effect size distribution，而不同 benchmark 的 item 构造方式完全不同（MMLU 多选知识 vs. GSM8K 数学推理 vs. HellaSwag 完形填空）。论文将"knowledge/reasoning benchmarks C% ≥ 26.9% vs. procedural benchmarks C% ≤ 18.9%"解读为 content-type 差异（Section 5, "knowledge-intensive items being more sensitive to training data composition shifts"），但这一解读缺乏 formal testing——可能仅仅是 item difficulty 分布或 discriminability 差异导致。
- **建议**: 对 cross-benchmark C% 差异做 formal decomposition（e.g., 控制 item difficulty 和 discrimination 后比较 residual C%），或明确标注当前比较为 descriptive

**W4** [warning] Within-family (Llama-2 vs. Llama-3) 61.3% C% 的解读与 temporal 31.3% 的关系不清晰

- **具体位置**: Section 4.2, Table 1
- **问题**: Llama-2 vs. Llama-3 的 61.3% C% 在 matched-ability analysis 后降至 28.3%，temporal comparison 的 31.3% 降至 28.9%。论文将两者的 matched values convergence (~28-29%) 解读为"genuine item-level DIF"的证据。但 within-family 比较中的 ability mismatch 远大于 temporal 比较（Llama-2 和 Llama-3 的能力差距 > 2023 vs 2024 cohort 平均差距），所以 matching 移除了更多"假 DIF"。两个 matched C% 收敛到相近值可能是巧合而非规律。
- **建议**: 用更多 cohort pairs（e.g., different ability gaps）检验 "matched C% converges to ~28%" 是否是 robust pattern，或加 error bars 说明 28.3% 和 28.9% 的 CI 是否 overlap

**W5** [warning] GSM1K correlation (r = -0.478, N = 33) 在 Discussion 中的使用超出 "exploratory" 标注

- **具体位置**: Section 4.7 ("an exploratory GSM1K analysis"), Section 5, Figure 5
- **问题**: 论文在 Section 4.7 将 GSM1K correlation 标注为 exploratory，但 Section 5 的 Discussion 中写到 "Both benchmarks exhibit temporal DIF…consistent with DIF capturing capability change distinct from memorization (r = -0.478, p = 0.005, Figure 5)"——这里的措辞已经从 exploratory 变为 supportive evidence。N = 33 的 correlation 极其不稳定（leave-one-out 可能大幅变化），且 GSM1K 本身作为 contamination ground truth 的质量未经验证。
- **建议**: 在 Discussion 中保持 exploratory framing，加入 caveat on small N instability（e.g., bootstrap CI for r）

---

## 小问题（不影响接收）

**M1** Multiple testing: BH-FDR 只移除 3 items（31.32% → 31.30%）被解读为"ETS dual threshold already provides implicit protection"。但这也可能意味着 BH 在此 setting 下 power 不足（12,508 tests, many true positives），而非 ETS threshold 就足够。建议加一句 caveat。

**M2** Section 4.1 Power analysis: "TPR ranges from 0.40 at a = 0.5 to 0.95 at a = 2.0"——这里的 a 是 item discrimination parameter。论文报告 MMLU 的 ā = 0.87，对应 TPR ≈ 0.68。但 MMLU 各 subject 的 discrimination 分布可能很广，低 discrimination items 的 TPR 可能只有 0.40。论文的 aggregate C% 因此可能 **underestimate** true DIF（因为低 discrimination items 的 DIF 检测不出），建议在 Discussion 中提及这一点。

**M3** Equation (1): MH odds ratio 公式中使用了 $A_k$, $B_k$, $C_k$, $D_k$ 表示 2×2 table 的 cells，但未提供 table layout 图示。对不熟悉 MH-DIF 的 NLP 读者来说，一个 2×2 contingency table 示例会大幅提高 accessibility。

**M4** Section 3.3 Cohort Designs: 5 种 cohort comparison 的 rationale 分散在不同 paragraph，建议用一个表格或列表统一呈现（目的、sample sizes、expected C%），便于读者理解 validity ladder 的逻辑。

**M5** Permutation test: 1,000 iterations 对 p < 0.01 级别的 tail estimation 精度有限（SE ≈ √(0.01×0.99/1000) ≈ 0.003）。建议增加至 5,000+ 或报告 permutation p-value 的 Monte Carlo CI。

---

## Questions to Authors

**Q1**: 能否对 LOFO 进行 power-calibrated analysis？具体来说，在 N_ref = 533, N_focal = 807 条件下，使用你们已有的 Monte Carlo 框架模拟 expected C%（假设 true C% = 31.3%），与 observed 22.5% 对比？

**Q2**: Graduated de-duplication 在 K=10 时 C% = 22.7%，K=20 时 C% = 29.1%。能否在固定 total N（e.g., 通过 upsampling small families 到 K=20 level）下重复此实验，分离 power 和 de-duplication 两个效应？

**Q3**: Section 4.3 Ground Truth Mismatch 部分的 enrichment ratio 0.964 表明 DIF flags 与 web-overlap 近乎独立。但这是否意味着 MH-DIF 检测到的 temporal instability 与 contamination 无关？如果是，那么 DIF 检测到的究竟是什么现象？论文说"underdetermined without training data"，但这是否过度回避了 causal interpretation？

**Q4**: Semi-synthetic injection 中 within-subject matching 的 FPR inflation 为 +0.186（Section 4.5）。论文推荐 cross-subject matching 作为 standard protocol，但如果 contamination 同时影响多个 subjects（k > 5），cross-subject matching 的 ΔFPR 也开始上升（Table 5: k=10 → 0.047）。在实际应用中，如何判断 contamination 是否已经扩散到 >5 subjects？

**Q5**: Cluster bootstrap 的 53.2% upper bound 意味着什么实质问题？是否暗示存在某些 family 的 DIF pattern 极端不同？能否报告 per-family C% distribution？

---

## Missing References

- **Swaminathan & Rogers (1990)**: 论文引用了 Swaminathan and Rogers (1990) 关于 logistic regression DIF，但未引用其后续重要工作 **Rogers & Swaminathan (1993)** 关于 Type I error rates under model violation，这与 LLM setting 下的 assumption violation 直接相关。
- **Penfield & Camilli (2007)**: 已引用，但建议增加 **Penfield (2001)** 关于 MH DIF under small samples 的讨论，因为 LOFO 场景涉及 reduced N。
- **DIF under non-independence**: 教育测量文献中有关于 testlet-level DIF（即 items nested within passages/testlets，产生 local dependence）的讨论，如 **Wainer et al. (2007) "Testlet Response Theory and Its Applications"**——这与 LLM families 内的 non-independence 高度类似，建议引用。

---

## 主要优势

1. **规模和系统性**: 5,227 models × 12,508 MMLU items + 6 benchmarks，这是迄今最大规模的 LLM benchmark psychometric audit，数据规模本身就构成贡献
2. **Validity ladder 设计**: Random split → ability quintile → temporal → within-family 的控制对比层次清晰，逻辑严密，说服力强（Table 1）
3. **Cross-subject matching 创新**: ΔFPR = 0.000 的 constructive guarantee（在 k ≤ 5 条件下）是 genuine 的方法论贡献，解决了 matching variable contamination 这一长期难题
4. **Transparent limitations**: 论文对 assumption violations（non-independence, multidimensionality, bimodal distribution）的讨论比同类论文更诚实和详尽
5. **Practical actionability**: Section 5.3 的 Monitor/Flag/Act protocol 提供了可直接应用的框架，Figure 6 的 ranking degradation 曲线有实际指导意义
6. **Ground truth meta-critique**: Section 4.3 和 5.2 对 web-overlap 作为 contamination ground truth 的质疑（enrichment ≈ 0.96, near independence）是独立而重要的发现

---

**总结判断**: 这是一篇方法论贡献扎实、规模令人印象深刻的论文。核心问题在于：(1) LOFO 分析暴露的 family-concentration 效应需要 power-calibrated quantification 以支撑"31% items show temporal DIF"这一 headline claim 的 generality；(2) non-independence 的定量影响需要超越间接证据。如果 N1 和 N2 能得到充分 address（尤其是 N1 的 power calibration），本文可达到 Conference 接收水平。当前状态下我的建议是 Borderline Conference (3.5)，两个 critical issues 的修改可在一个 ARR cycle 内完成。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 624 · 2026-05-22T10:26:00.929178+00:00_

Reviewer 1 审稿意见已收到。评分 3.5 (Borderline Conference)，提出 2 个 critical issues（LOFO family-concentration + examinee non-independence quantification）和 5 个 warning-level 问题。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 59

## Round 59

2 recorded events


### User

_source line 625 · 2026-05-22T10:26:03.868404+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿摘要**:
- **Overall: 3.5 (Borderline Conference)**
- **Soundness: 3.5/5 | Excitement: 3.5/5**
- **2 个 Must-Fix**: (N1) LOFO family-concentration 效应被低估——移除 Mistral/Llama-3 后 C% 降至 22-24%，power reduction 解释不充分，需要 power-calibrated quantification；(N2) examinee non-independence 对 MH chi-squared 的 inflation 缺乏直接定量（design effect / effective sample size）
- **5 个 Should-Fix**: semi-synthetic ecological validity、cluster bootstrap CI 应为 primary inference、cross-benchmark C% 可比性、within-family matched C% convergence 可能是巧合、GSM1K correlation 使用超出 exploratory 标注
- **5 个 Minor**: BH-FDR 解读、low-discrimination underdetection、MH table 图示、cohort design 呈现、permutation iterations
- **核心判断**: 方法论贡献扎实、规模令人印象深刻，但 headline claim "31% items show temporal DIF" 的 generality 需要通过 LOFO power calibration 和 non-independence quantification 来巩固。两个 critical issues 可在一个 ARR cycle 内修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 626 · 2026-05-22T10:26:08.878198+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 60

## Round 60

6 recorded events


### User

_source line 627 · 2026-05-22T10:29:35.316178+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：Temporal Measurement Instability in LLM Benchmarks

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 论文在前所未有的规模上将成熟的心理测量方法（MH-DIF）应用于 LLM benchmark 评估，产出了有价值的实证发现（31% temporal DIF、DIF 与 contamination 近正交），但方法论新颖性有限，且核心 framing 存在内部矛盾。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | MH-DIF 应用正确，semi-synthetic framework 设计严谨（ΔFPR=0 by construction），cross-benchmark replication 增强可信度；但 92.4% "unrelated to domain accuracy" 的推导不透明，§5.3 audit protocol 与方法论定位存在内部矛盾 |
| Excitement | 3/5 | 问题重要（benchmark 时序稳定性）、规模令人印象深刻（5,227 models × 12,508 items）、实用价值明确；但核心方法源自 1988 年，novelty 主要在 application context 而非方法论创新 |
| Reproducibility | 4/5 | 匿名代码链接已提供（anonymous.4open.science）、METABENCH 为公开数据、实验设置清晰；Monte Carlo power analysis 参数完整 |
| Confidence | 4/5 | 熟悉 DIF 方法论和 LLM evaluation 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Abstract 信息密度严重超载

- 具体位置：Abstract (Page 1)
- 问题：Abstract 中包含至少 15 个不同的统计量：ρ, τ, Jaccard, φ, enrichment ratio, C%, ΔFPR, ΔTPR, Q3, ETS C, 多个 p 值，以及众多具体数字（0.158, 0.134, 5,227, 12,508, 31.3%, 0.000 等）。一个段落中塞入如此多的数字严重损害可读性。例如原文连续出现："contamination labels are near independent of Mantel–Haenszel Differential Item Functioning (DIF) flags (enrichment = 0.06)—exposing a category error in prevailing validation methodology" 紧接着 "ΔTPR = +0.508 at p = 0.5" 再接 "Jaccard = 0.206, φ = 0.012"——读者无法在 abstract 阶段消化这些数字。
- 为什么影响接收：Abstract 是论文的第一印象。ARR reviewer guidelines 强调 review 应关注 "whether the paper's claims are supported"——但如果 reviewer 在 abstract 就迷失在数字海洋中，会严重影响后续阅读体验和评分。
- 建议修改方向：保留 3-5 个最核心的数字（31% C%, ΔFPR=0.000, 6 benchmarks, Jaccard≈0.2 or enrichment=0.06），其余移至正文。Abstract 应传达 **narrative**（what → so what → now what），不是 results dump。

**N2** [critical] §5.3 Audit Protocol 与论文核心方法论定位存在内在矛盾

- 具体位置：Section 5.3 (Page 8), 对比 Section 3 (Page 5) 和 Limitations (Page 9)
- 问题：论文多次强调 MH-DIF "detects *that* an item functions differentially but cannot determine *why*"（Limitations, Page 9: "More fundamentally, DIF detects that items function differently but cannot determine why"）。然而 §5.3 的 audit protocol 在 Flag 和 Act 两个层级均建议 "review flagged items for differential-performance-associated content characteristics"——这明确要求评估者调查 DIF 的原因，与 "detects THAT not WHY" 的反复声明直接矛盾。此外，"Flag/Act" 的命名暗示了纠正行动（"Act" = 采取措施），与论文标榜的 "diagnostic not destructive" framing 不一致。
- 为什么影响接收：核心方法论立场的内部矛盾会被敏锐的 reviewer 视为 intellectual incoherence。论文不能同时说 "DIF 不能告诉你为什么" 和 "请根据 DIF 结果去检查内容特征来找原因"。
- 建议修改方向：(a) 将 §5.3 中 "review flagged items for content characteristics" 改为更精确的表述，如 "prioritize flagged items for independent expert review using methods that *can* assess content characteristics"，明确 DIF 是筛选器而非诊断工具本身；(b) 将 "Flag/Act" 改为中性术语如 "Monitor/Investigate/Escalate"；(c) 增加一句过渡说明 DIF 是 screening step，后续因果分析需要不同的方法（如 Maeda 2025 的 XAI approach）。

**N3** [critical] 新颖性定位不够清晰——"application context" 的贡献边界需明确论证

- 具体位置：Section 1 (Page 2), Section 2 (Page 3)
- 问题：论文声称 "Our contributions are methodological and empirical, not algorithmic"（Page 2），但三项贡献的方法论新颖性需要更严格的论证：
  - **Contribution 1**（ground truth meta-critique）：DIF flags 与 web-overlap labels 近正交（Jaccard=0.206）是有趣的实证发现，但 "method A 和 method B 捕捉不同东西" 在概念上不令人惊讶——contamination detection（surface-level text matching）与 DIF（statistical behavioral difference）在 construct 层面本就不同。论文需要论证这为什么不是 a priori obvious。
  - **Contribution 2**（semi-synthetic framework）：Cross-subject matching 在心理测量学中有直接先驱（Swaminathan & Rogers 1990 的 purified matching, Nandakumar 1993）。论文需更明确阐述 LLM 设置中的特殊挑战使得现有方法不能直接套用，以及本文的具体改造在哪里。
  - **Contribution 3**（31% temporal instability at scale）：这是最强的贡献，但数字本身需要上下文——在教育测量中，temporal DIF 的典型率是多少？31% 是否 "高得异常" 需要与传统测试情境的 DIF rates 比较才能判断。
- 为什么影响接收：ARR reviewer guidelines 明确指出 "Results are not surprising" 不是有效批评 IF the results haven't been empirically tested。但反过来，论文有义务论证为什么这些 empirical results 是 **not obvious a priori**，尤其当方法本身不是新的时候。EMNLP 接收 application papers，但需要充分论证 application context 为什么构成独立贡献。
- 建议修改方向：(a) 在 Introduction 或 Related Work 中加入一个明确的段落，说明为什么 MH-DIF 在 LLM 评估中的应用 **不是** 简单的方法搬运——有哪些 LLM-specific 挑战需要解决？Section 3 提到的三个 challenges 是好的开始，但应更早、更突出地呈现；(b) 提供传统教育测量中 temporal DIF rates 的参考数据，帮助读者理解 31% 的意义；(c) 更精确地说明 cross-subject matching 相对于 Swaminathan & Rogers (1990) 的具体改进点。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 与 Growing Pains (Habba et al., 2026) 的区分不充分

- 具体位置：Section 2, Page 3 (最后一段)
- 问题：论文称 Growing Pains 是 "closest concurrent work" 并声称互补，但仅用一句话描述其方法（"addresses score comparability through fixed-parameter calibration"）。两篇论文都将心理测量方法应用于 LLM benchmark stability——Growing Pains 用 IRT 固定参数校准实现跨时段可比性，本文用 DIF 检测 item-level temporal instability。这种互补性需要更实质性的论证，而非一句话带过。具体来说：Growing Pains 的 anchor item 选择是否可以利用 DIF 分析来改进？本文的 DIF flagging 是否可以作为 Growing Pains 框架的 upstream quality filter？
- 建议：在 Related Work 或 Discussion 中增加 2-3 句实质性分析，说明两种方法的具体互补关系。

**W2** [warning] Discussion 过于压缩，丧失了应有的分析深度

- 具体位置：Section 5 (Page 8)
- 问题：Discussion 包含三个子节（5.1 Implications, 5.2 Ground Truth Meta-Critique, 5.3 Audit Protocol），每个子节仅 3-5 句话，外加 Conclusion 一段，全部压缩在不到半页中。这种密度导致几个重要讨论点被草草带过：
  - §5.1 没有充分讨论 "temporal DIF" 的因果模糊性——DIF 可能反映 contamination、capability evolution 或 training methodology shifts，但论文未讨论这三者的相对贡献或如何区分
  - §5.2 的 meta-critique 可以更深入：如果 web-overlap 和 DIF 是正交的，那么 benchmark 质量评估需要一个 **多维度框架**——这个 implications 值得展开
  - §5.3 的 audit protocol 作为论文的 practical contribution 之一，不应如此简略
- 建议：考虑将部分实验细节（如 Table 1 中的 Ability-variable 和 Within-family 行，这些是控制实验而非核心结果）移至 Appendix，为 Discussion 腾出空间。

**W3** [warning] 缺少相关引用："Test of Time" (arXiv 2509.00072)

- 具体位置：Section 2 Related Work
- 问题："Test of Time: Rethinking Temporal Signal of Benchmark Contamination" (2509.00072, 更新至 2026) 直接质疑了 temporal performance decay 作为 contamination signal 的有效性，发现 LLM 生成的问题可以有效移除这一 temporal signal。这与本文的核心主题（temporal measurement instability）高度相关，且支持本文 §5.2 的 meta-critique（temporal signal ≠ contamination signal）。未引用是一个明显遗漏。
- 建议：在 Related Work 的 Contamination Detection 段落中加入此引用，并讨论其发现如何与本文的 DIF-contamination orthogonality 发现呼应。

**W4** [warning] "Temporal DIF" 的因果解释不充分

- 具体位置：Section 4.2 (Page 6-7), Section 5.1 (Page 8)
- 问题：31% temporal C% 是论文的 headline finding，但其解释存在根本模糊性。论文在 §5.1 承认 DIF 信号可能来自 "contamination, capability evolution, or training methodology shifts—underdetermined without training data"。然而论文标题使用 "Measurement Instability" 这个带有负面含义的术语——如果 DIF 反映的是 genuine capability change（如 2024 模型在特定领域确实更强），那么这是 benchmark 正确地捕捉到了变化，而非 "instability"。论文在 framing 上暗示了这是 benchmark 的问题，但逻辑上 DIF 也可能是 benchmark 正常运作的证据。
- 建议：(a) 在 Discussion 中增加一段讨论 "instability" vs "sensitivity" 的区分；(b) 考虑在标题中使用更中性的术语如 "Temporal Differential Item Functioning" 而非 "Measurement Instability"。

**W5** [warning] 92.4% "unrelated to domain accuracy" 的推导过程不透明

- 具体位置：Section 4.2 (Page 6)
- 问题：论文声称 "item-level regression shows that 92.4% of the DIF signal is unrelated to aggregate domain-level accuracy gains"。但这个数字的具体推导方式不清楚——是来自 partial R² 的补数？还是 DIF-C items 中通过 logistic regression 不能被 domain accuracy 解释的比例？读者无法从正文或 Appendix A 中明确追溯这个数字的计算方式。
- 建议：明确写出 92.4% 的计算公式或推导逻辑，如 "Among items classified as ETS C, X% remain DIF-C after partialling out domain-level accuracy change (logistic regression, OR=..., p=...)."

**W6** [warning] Appendix F 的 negative finding（AUROC≈0.60）与 §5.3 audit protocol 的张力

- 具体位置：Appendix F (referenced Page 8 as "Section E"), §5.3 (Page 8)
- 问题：Appendix F 报告了使用 item features 预测 DIF susceptibility 的模型仅达到 AUROC≈0.60（接近随机），这意味着无法从 item 特征预先识别哪些 items 会展现 DIF。然而 §5.3 的 audit protocol 建议 "review flagged items for differential-performance-associated content characteristics"——如果 content characteristics 不能预测 DIF（如 Appendix F 所示），这个建议的实用价值存疑。论文在正文中仅用半句话提到这一 negative finding（"DIF susceptibility (AUROC = 0.60; Section E), confirming that post-hoc monitoring cannot be replaced by pre-screening"），没有充分讨论其对 audit protocol 的 implications。
- 建议：在 Discussion 中明确讨论 Appendix F 的 negative finding 如何约束 §5.3 audit protocol 的实际效用，以及什么类型的 "content characteristics review" 在 DIF 不可预测的情况下仍然有价值。

---

## 小问题（不影响接收）

- **M1**: Table 1 (Page 7) 中用 dashes (—) 表示 Li et al. labels 不适用的情况，但 table caption 中对此没有说明。应在 caption 中加注。
- **M2**: Figure 1 caption (Page 2) 说 "Left: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. Right: differential contamination produces DIF; the focal cohort's ICC shifts because only this cohort was disproportionately exposed during training." 但 Figure 1 是概念示意图而非来自实际数据——caption 应明确标注为 "Schematic illustration" 以避免误解。
- **M3**: Page 3 提到 "ATLAS (Li et al., 2025) for computerized adaptive testing of LLMs, and competency-focused IRT evaluation in medical domains (Luo et al., 2025)"，但 Luo et al., 2025 改为了 Zhuang et al., 2025（从 reference list 看）——请核实引用是否对应正确。
  - **更正**：我重新检查后，两个引用确实都存在。但 page 3 原文连续列出了很多引用，部分引用的描述过于笼统（"competency-focused IRT evaluation"），读者难以判断其具体相关性。
- **M4**: 数值精度不完全一致——例如 ρ=0.997（3位小数）vs C%=31.3%（1位小数）vs ΔFPR=0.000（3位小数）vs enrichment ratio=0.064（3位小数）。建议统一为 2-3 位有效数字。
- **M5**: Page 6 "TPR at mean κ = 1.2 is 0.87" 与 Table 4 (Page 13) 应交叉验证一致性。
- **M6**: Limitations 部分（Page 9）长度和覆盖面适当（methodological scope, generalizability, matching boundary），符合 EMNLP 要求。

---

## 格式合规检查（EMNLP 2026 / ARR）

| 项目 | 合规 | 备注 |
|------|------|------|
| 页数（8页正文） | ✅ | Sections 1-6 在 Pages 1-8 内完成；Limitations 从 Page 9 开始，不计入页限 |
| 匿名性 | ✅ | "Anonymous ACL submission"；代码使用 anonymous.4open.science；未发现 de-anonymization 风险 |
| Limitations 章节 | ✅ | 存在且适当，~3 个点，未包含过多额外内容 |
| 模板 | ✅ | ACL 格式正确（从 PDF 排版判断） |
| References 格式 | ✅ | 遵循 ACL bibliography 标准；arXiv preprints 标注正确 |
| 代码/数据可用性 | ✅ | 匿名代码链接已提供 |

**注意**：Pages 7-8 信息密度极高（Page 7 含 Table 1 + Figure 2 + Table 2 + 三个子节；Page 8 含 Table 3 + 五个子节 + Conclusion），暗示作者可能使用了 `\enlargethispage` 或其他空间压缩手段。虽然 PDF 页面未超出 8 页限制，但极端密度本身降低了可读性。

---

## Missing References

1. **"Test of Time: Rethinking Temporal Signal of Benchmark Contamination"** (arXiv 2509.00072, v3 2026) — 直接质疑 temporal contamination signals 的有效性，与本文 §5.2 meta-critique 高度相关。**应引用。**
2. **"DIF: A Framework for Benchmarking and Verifying Implicit Bias in LLMs"** (arXiv 2505.10013, 2025) — 使用 "DIF" 但指 Demographic Implicit Fairness，与本文的 psychometric DIF 是不同概念。可在 Related Work 中提及以消除歧义。**可选引用。**

---

## 主要优势

1. **规模与系统性**：5,227 models × 12,508 items 的分析规模在 benchmark psychometrics 领域无出其右。6 个 benchmark 的 cross-validation 显著增强了发现的 robustness。
2. **Semi-synthetic validation 设计精良**：ΔFPR=0 by construction 的证明以及参数化注入框架（varying p, κ, subjects）提供了强有力的方法论支撑，避免了 "cherry-picking threshold" 的批评。
3. **Ground truth meta-critique 的实用价值**：DIF 与 web-overlap contamination labels 近正交（enrichment=0.064, Jaccard=0.206）这一发现对 benchmark evaluation community 有直接的方法论启示——当前的 contamination detection 和 DIF 分析捕捉的是不同维度的 benchmark 质量问题。
4. **控制实验充分**：matched-ability quintiles, IRT θ-conditioning, within-subject pre-checks, random split controls, within-family comparisons——多重控制确保核心发现不是 artifact。
5. **透明度**：包含 negative finding（Appendix F, AUROC≈0.60）而非只报告正面结果，这在学术写作中值得肯定。

---

## Questions for Authors

1. 31% temporal C% 在传统教育测量的 temporal DIF 研究中处于什么水平？是否有可参考的 baseline（如 SAT、GRE 的 temporal DIF rates）来帮助读者 contextualize 这个数字？
2. 如果 Appendix F 表明 item features 无法预测 DIF susceptibility（AUROC≈0.60），§5.3 建议的 "review flagged items for content characteristics" 具体应该审查什么？能否提供成功识别 DIF 来源的案例？
3. Cohort 的 temporal split 基于 model release date 而非 training data cutoff。如果一个 2024 年发布的模型使用 2023 年的训练数据，它会被归入 2024 cohort——这种错配对 DIF 估计的影响有多大？
4. 论文标题用 "Measurement Instability"，但如果 DIF 反映的是 genuine capability change，是否应该理解为 "Measurement Sensitivity" 而非 "Instability"？这两种解释对 practical recommendations 有不同含义。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-22T10:30:11.216736+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n## 总体评分\n**Overall**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: 论文在前所未有的规模上将成熟的心理测量方法（MH-DIF）应用于 LLM benchmark 评估，产出了有价值的实证发现（31% temporal DIF、DIF 与 contamination 近正交），但方法论新颖性有限，且核心 framing 存在内部矛盾。\n\n## Must-Fix 问题\n\n**N1** [critical] Abstract 信息密度严重超载\n- Abstract 中包含至少 15 个不同的统计量，严重损害可读性。建议保留 3-5 个核心数字，其余移至正文。\n\n**N2** [critical] §5.3 Audit Protocol 与论文核心方法论定位存在内在矛盾\n- 论文反复强调 \"detects THAT not WHY\"，但 §5.3 建议 \"review flagged items for differential-performance-associated content characteristics\"——这要求调查 DIF 的原因，与方法论定位矛盾。\"Flag/Act\" 命名暗示纠正行动，与 \"diagnostic not destructive\" framing 不一致。\n\n**N3** [critical] 新颖性定位不够清晰——\"application context\" 的贡献边界需明确论证\n- Contribution 1（ground truth meta-critique）在概念上可能是 a priori obvious\n- Contribution 2（cross-subject matching）有心理测量学直接先驱\n- Contribution 3（31% temporal instability）缺少与传统教育测量 DIF rates 的对比\n\n## Should-Fix 问题\n\n**W1** 与 Growing Pains (Habba et al., 2026) 的区分不充分\n**W2** Discussion 过于压缩，丧失分析深度\n**W3** 缺少引用：\"Test of Time\" (arXiv 2509.00072)\n**W4** \"Temporal DIF\" 的因果解释不充分——\"Measurement Instability\" 标题带有负面含义，DIF 也可能是 benchmark 正常运作的证据\n**W5** 92.4% \"unrelated to domain accuracy\" 的推导过程不透明\n**W6** Appendix F 的 negative finding（AUROC≈0.60）与 §5.3 audit protocol 的张力\n\n## Minor\n- M1: Table 1 dashes 无 caption 说明\n- M2: Figure 1 应标注为 \"Schematic illustration\"\n- M3: 引用核实（Luo et al. vs Zhuang et al.）\n- M4: 数值精度不一致\n- M5: TPR at mean a=1.2 与 Table 4 交叉验证\n- M6: Limitations 长度和覆盖面适当\n\n## Missing References\n1. \"Test of Time\" (arXiv 2509.00072) — 应引用\n2. \"DIF: A Framework for Benchmarking and Verifying Implicit Bias in LLMs\" (arXiv 2505.10013) — 可选\n\n---\n\n请逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告\n\n## 总体评分\n**Overall**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: 论文在前所未有的规模上将成熟的心理测量方法（MH-DIF）应用于 LLM benchmark 评估，产出了有价值的实证发现（31% temporal DIF、DIF 与 contamination 近正交），但方法论新颖性有限，且核心 framing 存在内部矛盾。\n\n## Must-Fix 问题\n\n**N1** [critical] Abstract 信息密度严重超载\n- Abstract 中包含至少 15 个不同的统计量，严重损害可读性。建议保留 3-5 个核心数字，其余移至正文。\n\n**N2** [critical] §5.3 Audit Protocol 与论文核心方法论定位存在内在矛盾\n- 论文反复强调 \"detects THAT not WHY\"，但 §5.3 建议 \"review flagged items for differential-performance-associated content characteristics\"——这要求调查 DIF 的原因，与方法论定位矛盾。\"Flag/Act\" 命名暗示纠正行动，与 \"diagnostic not destructive\" framing 不一致。\n\n**N3** [critical] 新颖性定位不够清晰——\"application context\" 的贡献边界需明确论证\n- Contribution 1（ground truth meta-critique）在概念上可能是 a priori obvious\n- Contribution 2（cross-subject matching）有心理测量学直接先驱\n- Contribution 3（31% temporal instability）缺少与传统教育测量 DIF rates 的对比\n\n## Should-Fix 问题\n\n**W1** 与 Growing Pains (Habba et al., 2026) 的区分不充分\n**W2** Discussion 过于压缩，丧失分析深度\n**W3** 缺少引用：\"Test of Time\" (arXiv 2509.00072)\n**W4** \"Temporal DIF\" 的因果解释不充分——\"Measurement Instability\" 标题带有负面含义，DIF 也可能是 benchmark 正常运作的证据\n**W5** 92.4% \"unrelated to domain accuracy\" 的推导过程不透明\n**W6** Appendix F 的 negative finding（AUROC≈0.60）与 §5.3 audit protocol 的张力\n\n## Minor\n- M1: Table 1 dashes 无 caption 说明\n- M2: Figure 1 应标注为 \"Schematic illustration\"\n- M3: 引用核实（Luo et al. vs Zhuang et al.）\n- M4: 数值精度不一致\n- M5: TPR at mean a=1.2 与 Table 4 交叉验证\n- M6: Limitations 长度和覆盖面适当\n\n## Missing References\n1. \"Test of Time\" (arXiv 2509.00072) — 应引用\n2. \"DIF: A Framework for Benchmarking and Verifying Implicit Bias in LLMs\" (arXiv 2505.10013) — 可选\n\n---\n\n请逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-22T10:30:37.305240+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 26088
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-22T10:30:37.355963+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 将教育测量 MH-DIF 方法系统迁移至 LLM benchmark 评估具有真实的方法论贡献和实践意义，控制实验层次丰富，但 LOFO 分析暴露的 family-concentration 问题以及 examinee non-independence 的影响未被充分量化，削弱了核心 claim 的确信度。\n\n## Must-Fix 问题\n\n**N1** [critical] LOFO family-concentration 效应被低估，power-reduction 解释不充分\n- 移除 Mistral（547 models, 51% ref）后 C% 从 31.3% 降至 22.5%（-8.8pp），移除 Llama-3（315 models, 39% focal）后降至 24.1%（-7.3pp）。\n- 移除后 N_ref 仍有 ~533，N_focal 仍有 ~492——远超 power analysis 中 N≥80 的阈值，power reduction 难以解释 8.8pp 下降。\n- Section 4.4 的 \"none reduces C% below ~28%\" 指 matching/control 策略，但 LOFO 结果（22.5%, 24.1%）低于此下界，两类 robustness 结果之间的 tension 未被讨论。\n- 如果 DIF 信号高度集中于 Mistral 和 Llama-3，则 \"31% items show temporal DIF\" 实质是 \"31% items show Mistral/Llama-3-specific DIF\"。\n\n**N2** [critical] Examinee non-independence 对 MH chi-squared 的 inflation 效应缺乏直接定量\n- 三项间接证据（permutation FPR < 0.001pp、de-duplication K=20 → C%=29.1%、cluster bootstrap CI [26.7%, 53.2%]）均不直接量化 chi-squared inflation。\n- Cluster bootstrap upper bound 53.2% 暗示 family-level clustering 对 point estimate 有 massive impact。\n- 建议使用 design effect (DEFF) / effective sample size 方法定量调整。\n\n## Should-Fix 问题\n\n**W1** Semi-synthetic injection ecological validity 有限但 claim 偏强\n**W2** Bootstrap CI 3.1x width 差异暗示 family-level dependence 结构性影响，cluster bootstrap 应为 primary CI\n**W3** Cross-benchmark C% 可比性受 statistical power 差异影响，缺乏 formal decomposition\n**W4** Within-family matched C% convergence (~28-29%) 可能是巧合\n**W5** GSM1K correlation (r=-0.478, N=33) 使用超出 exploratory 标注\n\n## Minor\n- M1: BH-FDR 解读需 caveat\n- M2: Low-discrimination items 的 TPR 可能只有 0.40，aggregate C% 可能 underestimate true DIF\n- M3: Equation (1) 需 2×2 table 图示\n- M4: Cohort Designs 应统一用表格呈现\n- M5: Permutation 1,000 iterations 精度有限\n\n## Missing References\n- Rogers & Swaminathan (1993) 关于 Type I error rates under model violation\n- Penfield (2001) 关于 MH DIF under small samples\n- Wainer et al. (2007) \"Testlet Response Theory\" 关于 testlet-level local dependence\n\n---\n\n请逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 将教育测量 MH-DIF 方法系统迁移至 LLM benchmark 评估具有真实的方法论贡献和实践意义，控制实验层次丰富，但 LOFO 分析暴露的 family-concentration 问题以及 examinee non-independence 的影响未被充分量化，削弱了核心 claim 的确信度。\n\n## Must-Fix 问题\n\n**N1** [critical] LOFO family-concentration 效应被低估，power-reduction 解释不充分\n- 移除 Mistral（547 models, 51% ref）后 C% 从 31.3% 降至 22.5%（-8.8pp），移除 Llama-3（315 models, 39% focal）后降至 24.1%（-7.3pp）。\n- 移除后 N_ref 仍有 ~533，N_focal 仍有 ~492——远超 power analysis 中 N≥80 的阈值，power reduction 难以解释 8.8pp 下降。\n- Section 4.4 的 \"none reduces C% below ~28%\" 指 matching/control 策略，但 LOFO 结果（22.5%, 24.1%）低于此下界，两类 robustness 结果之间的 tension 未被讨论。\n- 如果 DIF 信号高度集中于 Mistral 和 Llama-3，则 \"31% items show temporal DIF\" 实质是 \"31% items show Mistral/Llama-3-specific DIF\"。\n\n**N2** [critical] Examinee non-independence 对 MH chi-squared 的 inflation 效应缺乏直接定量\n- 三项间接证据（permutation FPR < 0.001pp、de-duplication K=20 → C%=29.1%、cluster bootstrap CI [26.7%, 53.2%]）均不直接量化 chi-squared inflation。\n- Cluster bootstrap upper bound 53.2% 暗示 family-level clustering 对 point estimate 有 massive impact。\n- 建议使用 design effect (DEFF) / effective sample size 方法定量调整。\n\n## Should-Fix 问题\n\n**W1** Semi-synthetic injection ecological validity 有限但 claim 偏强\n**W2** Bootstrap CI 3.1x width 差异暗示 family-level dependence 结构性影响，cluster bootstrap 应为 primary CI\n**W3** Cross-benchmark C% 可比性受 statistical power 差异影响，缺乏 formal decomposition\n**W4** Within-family matched C% convergence (~28-29%) 可能是巧合\n**W5** GSM1K correlation (r=-0.478, N=33) 使用超出 exploratory 标注\n\n## Minor\n- M1: BH-FDR 解读需 caveat\n- M2: Low-discrimination items 的 TPR 可能只有 0.40，aggregate C% 可能 underestimate true DIF\n- M3: Equation (1) 需 2×2 table 图示\n- M4: Cohort Designs 应统一用表格呈现\n- M5: Permutation 1,000 iterations 精度有限\n\n## Missing References\n- Rogers & Swaminathan (1993) 关于 Type I error rates under model violation\n- Penfield (2001) 关于 MH DIF under small samples\n- Wainer et al. (2007) \"Testlet Response Theory\" 关于 testlet-level local dependence\n\n---\n\n请逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-22T10:30:38.971623+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1615
}
```

</details>

---


### Assistant

_source line 632 · 2026-05-22T10:30:41.677036+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 61

## Round 61

2 recorded events


### User

_source line 633 · 2026-05-22T10:30:44.386465+00:00_

[Reviewer 2 审稿结果]:
审稿完成。报告已通过 `review_reviewer_post_to_director` 提交。

**审稿摘要**：

- **Overall: 3.5 (Borderline Conference)**
- **Soundness 4/5 | Excitement 3/5 | Reproducibility 4/5**

**3 个 Must-Fix 问题**：
1. Abstract 信息过载（15+ 统计量），严重损害可读性
2. §5.3 audit protocol 建议 "review content characteristics" 与论文反复强调的 "detects THAT not WHY" 直接矛盾
3. 新颖性定位不清——三项贡献均基于现有方法（MH-DIF 1988, cross-subject matching 1990），需要更明确论证 "application to LLM evaluation" 为何构成独立贡献

**6 个 Should-Fix 问题**：与 Growing Pains 区分不足、Discussion 过于压缩、缺引 "Test of Time" (2509.00072)、"Measurement Instability" vs "Sensitivity" 的 framing 模糊、92.4% 推导不透明、Appendix F negative finding 与 audit protocol 的张力

**主要优势**：规模无出其右（5,227×12,508）、semi-synthetic validation 设计精良（ΔFPR=0 by construction）、DIF-contamination 正交性发现有实用价值、控制实验充分、包含 negative finding 体现透明度

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 634 · 2026-05-22T10:30:49.447587+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 62

## Round 62

10 recorded events


### User

_source line 635 · 2026-05-22T10:32:38.372581+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题

**[REBUT] R2-N1: Abstract 信息密度严重超载**

R2 称 abstract 包含 15+ 统计量损害可读性。我不同意将此列为 critical。

理由：本文是 large-scale psychometric audit，核心贡献 **就是** 一组统计发现。Abstract 的数字密度与论文性质匹配——每个数字对应一个独立的 claim（31% temporal DIF、ΔFPR=0.000 validation guarantee、92.4% item-specificity、ρ≈0.997 ranking preservation、enrichment≈0.96 contamination independence）。删减任何一组都会使读者无法从 abstract 判断论文做了什么。ARR reviewer guidelines (I1) 明确要求 specificity——"instead of 'missing relevant references,' specify which ones"，同理，abstract 的具体数字正是 specificity 的体现。

此外，ACL ARR guidelines (H13) 警告不要 "demanding extra experiments beyond what claims require"——同样适用于要求删减支撑 claim 的核心数据。这是 writing preference，不是 soundness 问题，不应归为 Must-Fix。

**建议降级为 Minor/Style suggestion。**

---

**[REBUT] R2-N2: §5.3 Audit Protocol 与 "detects THAT not WHY" 存在内在矛盾**

R2 认为 §5.3 建议"review flagged items for content characteristics"与论文的方法论定位矛盾。我不同意。

理由：论文的 claim 是 **MH-DIF 方法本身** detects THAT not WHY——这是对 statistical procedure 的准确描述。§5.3 的 audit protocol 是方法应用后的 **downstream workflow recommendation**，即：先用 MH-DIF 识别可疑 items（THAT），再人工审查这些 items 的特征（WHY）。这是标准的两阶段诊断流程，与教育测量实践完全一致——ETS 自己的 DIF protocol 就是先统计检测再人工审查（参见 Zieky, 1993; Holland & Thayer, 1988 的 original framework）。

"Flag/Act" 命名指的是 monitoring 严重程度的分级响应，不是对 DIF items 的"纠正"。具体来说（Section 5.3）：
- Monitor (C% < 15%): 仅报告 C% 在 release notes
- Flag (15–25%): 报告 stable-item rankings 作为 sensitivity analysis
- Act (C% ≥ 25%): 审查 flagged items + 将 stable-item rankings 作为 primary metric

这三级响应从未声称 MH-DIF 本身能解释原因。Act 级别的"review flagged items"是将问题移交给 domain experts，不是 MH-DIF 方法在做因果归因。

**不构成 contradiction，建议降级或移除。**

---

**[PARTIAL AGREE] R2-N3: 新颖性定位不够清晰**

R2 提出三点：(a) ground truth meta-critique 可能 a priori obvious; (b) cross-subject matching 有心理测量学先驱; (c) 31% 缺少与传统教育 DIF rates 的对比。

逐点回应：

**(a) [REBUT]** Ground truth meta-critique 并非 a priori obvious。大量 contamination detection 文献（Li et al., 2024b; Deng et al., 2024; Golchin and Banerjee, 2024——Section 2 引用）**隐式假设**web-overlap 是 contamination 的可靠 ground truth。本文 Section 4.3 的实证发现——enrichment ratio = 0.964, φ = 0.012, OR = 1.05 [0.96, 1.15]——表明 DIF flags 与 web-overlap **近乎正交**，这直接挑战了该领域的主流假设。如果这一发现是"a priori obvious"，那么上述论文不应使用 web-overlap 作为 ground truth。

**(b) [PARTIAL AGREE]** Cross-subject matching 确实有先驱（Swaminathan & Rogers, 1990 的 purified matching；论文 Section 3.2 已引用）。但适配到 multi-domain LLM benchmarks（57 subjects）并证明 constructive ΔFPR = 0.000 guarantee（Table 5, k ≤ 5）是非平凡的扩展。建议作者在 Section 3.4 更明确地 credit 先驱方法并阐明 novel adaptation 的具体贡献。

**(c) [AGREE]** 缺少与传统教育测量 DIF rates 的 quantitative 对比是一个有效的 contextualization gap。典型的 large-scale 教育测试（SAT, GRE）中 ETS C 比例通常在 5–15%（参见 Zieky, 2003; Dorans & Holland, 1993）。与 31% 对比会显著增强论文 finding 的 impact framing。

**建议作者补充教育测量 baseline DIF rates 对比（可在 1–2 句内完成），并强化 cross-subject matching 的 novelty 论证。但整体来看，N3 不构成 Must-Fix——novelty positioning 不充分是 writing/framing 问题而非 soundness 问题，建议降级为 Should-Fix。**

---

## Should-Fix 问题

**[PARTIAL AGREE] R2-W1: 与 Growing Pains (Habba et al., 2026) 的区分不充分**

Section 2 确实提到了 Growing Pains 作为 "closest concurrent work"（"addresses score comparability through fixed-parameter calibration"），但区分仅一句话。Given 该工作的 high relevance（同样关注 LLM benchmark temporal comparability），2–3 句的 explicit comparison（score-level equating vs. item-level DIF; parametric IRT vs. non-parametric MH）会增强 positioning。

**[PARTIAL AGREE] R2-W2: Discussion 过于压缩**

在 8-page limit 下 Discussion 被压缩是可以理解的。但 §5.1 (Temporal Comparability) 和 §5.2 (Ground Truth Meta-Critique) 各只有一段，确实牺牲了分析深度。特别是 §5.2 需要更深入地讨论"如果 DIF 和 web-overlap 正交，DIF 到底检测到了什么"这一核心问题。建议将部分 Appendix 内容（如 structural analysis details）进一步压缩以释放 Discussion 空间。

**[REBUT] R2-W3: 缺少引用 "Test of Time" (arXiv 2509.00072)**

我无法验证该 arXiv 论文的确切内容和发表状态。如果该论文确实讨论了 benchmark temporal stability 的相关话题，可以考虑引用。但 missing reference 通常不构成 Should-Fix——ARR guidelines (H3) 警告 "claiming lack of novelty without specific references"，同理，仅凭一篇未经验证的 arXiv preprint 不应作为 novelty concern 的依据。

**建议降级为 Minor/Optional。**

**[PARTIAL AGREE] R2-W4: "Temporal DIF" 的因果解释——DIF 可能是 benchmark 正常运作的证据**

R2 提出一个有趣的概念性问题：如果模型在某些 items 上通过真实能力提升而表现更好，这些 items 显示 DIF 是 benchmark 正常运作的证据，而非"instability"。

这是一个合理的 conceptual 观点，但论文 Section 4.2 的 matched-ability analysis 已经部分回应：在控制 overall ability 后，C% 仅从 31.3% 降至 28.9%（-2.4pp），说明绝大部分 DIF 不是 ability difference 驱动的。DIF 的定义本身就是 **controlling for ability** 后的 differential functioning——如果模型的真实能力提升被 matching 控制了，那剩余的 DIF 就不是"正常运作"，而是 item 在不同群体间 **以不同方式** 运作。

但关于标题 "Measurement Instability" 的 framing，R2 有一定道理——"instability" 确实带有负面含义。不过 Section 5.1 明确称 DIF 的归因为 "underdetermined"（contamination, capability evolution, methodology shifts 均有可能），这比标题的 framing 更 nuanced。建议作者在 Introduction 或 Discussion 中加 1–2 句缓和标题的 framing。

**[AGREE] R2-W5: 92.4% "unrelated to domain accuracy" 的推导过程不透明**

R2 指出这一数字的来源不清晰。我赞同。

从论文中看，Section 4.2 报告了两个相关但不同的统计量：
- Item-level logistic regression pseudo R² = 0.0007（"item-level regression"）
- 92.4% "item-specific"

如果 pseudo R² = 0.0007 意味着 domain-level 因素只解释 0.07% 的方差，那 item-specific 应为 ~99.9% 而非 92.4%。如果 92.4% 来自另一个分析（例如 hierarchical decomposition 将 DIF 方差分解为 domain-level vs. item-level），其推导过程在正文中不可见。这个数字在 abstract 和 introduction 中都被重复引用，是核心 claim 之一，需要清晰的推导链。

**[REBUT] R2-W6: Appendix F 的 AUROC≈0.60 与 §5.3 audit protocol 的张力**

R2 认为 item-level 预测能力弱（AUROC≈0.60）与 audit protocol 的推荐存在张力。我不同意。

论文 Discussion §5.3 明确区分了两条路径：
- **Pre-screening**（基于 item features 预测哪些 items 会 DIF）→ AUROC≈0.60 说明这条路径不可行
- **Post-hoc monitoring**（收集数据后运行 MH-DIF 检测）→ 这是 §5.3 audit protocol 推荐的方法

Appendix F 的 negative finding 恰恰 **支撑** 了 §5.3 的结论："post-hoc monitoring needed, not pre-screening"（Section 5.3 原文）。没有张力，反而是逻辑自洽的。

---

## Minor 问题

**[AGREE] R2-M1**: Table 1 的 dashes 确实缺乏 caption 说明。Caption 已说明 "Dashes indicate comparisons where Li et al. labels are not applicable"，但需要更显眼。

**[AGREE] R2-M2**: Figure 1 确实应标注为 schematic/illustrative，当前 caption 的 "illustrated via Item Characteristic Curves" 不够明确。

**[REBUT] R2-M3**: 引用核实问题需要验证具体指控的准确性。R2 提到 "Luo et al. vs Zhuang et al." 但未给出具体位置和错误内容。在没有验证之前，不做判断。

**[AGREE] R2-M4**: 数值精度不一致是一个有效的 editorial concern（部分数字报告到小数点后 3 位，部分只 1 位）。

**[AGREE] R2-M5**: TPR at mean a=1.2 与 Table 4 交叉验证是合理的 internal consistency check。

**[AGREE] R2-M6**: Limitations 长度适当，覆盖面合理。

---

## Missing References

**[PARTIAL AGREE] "Test of Time" (arXiv 2509.00072)**: 需验证相关性。如果确实讨论 benchmark temporal stability，值得引用。

**[AGREE] "DIF: A Framework for Benchmarking and Verifying Implicit Bias in LLMs" (arXiv 2505.10013)**: 如果该论文将 DIF 应用于 LLM bias 检测（不同于本文的 temporal DIF），那是直接相关的 concurrent work，应该引用并区分。

---

## 总结

R2 的审稿侧重 framing/novelty/writing quality，与我的审稿侧重（statistical methodology/experimental validity）互补。核心分歧：

1. **R2-N1 (Abstract density)**: 我认为不构成 critical issue，建议降级
2. **R2-N2 (Audit protocol contradiction)**: 我认为不存在 contradiction——THAT/WHY 是对 MH-DIF method 的描述，audit protocol 是 downstream workflow
3. **R2-N3 (Novelty)**: 部分同意（缺少教育 DIF rate baseline 对比），但 ground truth meta-critique 的非 trivial 性质不应被低估
4. **R2-W5 (92.4%)**: 完全同意，这是一个需要作者 clarify 的关键推导
5. **R2-W6 (AUROC vs audit)**: 不同意——pre-screening 和 post-hoc monitoring 是明确区分的两条路径

我与 R2 对 Overall Assessment 的判断一致（3.5, Borderline Conference），但核心 concerns 不同：R2 的 blockers 偏向 framing/novelty，我的偏向 LOFO family-concentration (我的 N1) 和 non-independence quantification (我的 N2)。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-22T10:34:27.724307+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-22T10:34:27.774977+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T10:19:05.200386+00:00\", \"completed_at\": \"2026-05-22T10:22:11.204435+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 5-6\", \"message\": \"连续 2 页纯文本无任何 display item（Section 3.3-3.4 方法后半 + Section 4.1 实验前半）。从 Figure 1（p.2）到 Table 1（p.7）跨越约 4 页近纯文字，审稿人翻页体验单调。建议将 Table 1 或 Figure 2 前移至 p.5-6 区域，或在 Section 3 中增加一个方法流程示意图/框架图打破文字墙\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"三个 display items（Table 1 + Figure 2 + Table 2）集中在同一页，与前几页的纯文本形成节奏失衡。若能将其中一个前移可改善整体视觉节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"四个 display items（Table 7 + Figures 3/4/5）集中在同一页，密度高但作为 appendix 可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"Figure 6 及 caption 仅占页面上半部约 45%，底部约 50% 为空白。可考虑缩小 figure 间距或将部分 appendix 内容上移填充\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主文 8 页共 5 个 display items（2 figures + 3 tables），对于实证为主的论文偏少（通常 5-8 个）。当前处于下限，审稿人可能感到实验展示不够直观。建议考虑在主文中增加一个关键结果的可视化（如将 appendix 的 Figure 3 或 Figure 4 提升至主文）\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-22T10:34:27.775406+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-22T10:34:27.876167+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-22T10:41:14.452349+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Round 13 (Fresh review, 2026-05-22)\n# 2 critical open, 10 warning open, 5 info open\n\n# ============================================================\n# ROUND 13 — NEW / REOPENED ISSUES\n# ============================================================\n\n- id: \"R13-MF1\"\n  summary: \"LOFO family-concentration: 移除 Mistral/Llama-3 后 C% 降至 22-24%, power-reduction 解释不充分\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"N_ref≈533, N_focal≈492 仍远超 power threshold (N≥80)，8.8pp drop 不能仅归因 power reduction。Section 4.4 ~28% floor 与 LOFO 22.5% 的 tension 未讨论。\"\n  action_items:\n    - round: 13\n      action: \"使用 Monte Carlo 框架对 LOFO 进行 expected power calibration\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF2\"\n  summary: \"Examinee non-independence 对 MH chi-squared inflation 缺乏直接定量 (R10-W1 reopened)\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"首次提出\"\n    - round: 12\n      reviewers: []\n      note: \"标记 resolved (cluster bootstrap CI + LOFO)\"\n    - round: 13\n      reviewers: [1]\n      note: \"Reopened: 三项间接证据不足。需 DEFF / effective sample size 直接量化 chi-squared inflation。\"\n  action_items:\n    - round: 13\n      action: \"使用 design effect / effective sample size 方法调整 MH chi-squared\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF1\"\n  summary: \"新颖性定位——缺少与教育测量 temporal DIF rate baseline 对比 (R9-W2 related)\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 列 Must-Fix, R1 partial agree, Director 降级 Should-Fix。缺 SAT/GRE baseline (5-15%)。\"\n  action_items:\n    - round: 13\n      action: \"补充教育测量 temporal DIF rate baseline 对比 + 强化 LLM-specific novelty 论证\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF2\"\n  summary: \"Abstract 信息密度仍偏高 (R11-W3 reopened)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"标记 resolved (删除 φ, ΔFPR<0.01 for k≤5, 45-174×)\"\n    - round: 13\n      reviewers: [2]\n      note: \"R2 认为仍 15+ 数字，R1 rebut。Director 降为 Should-Fix。\"\n  action_items:\n    - round: 13\n      action: \"进一步精简至 5-7 个核心数字\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF3\"\n  summary: \"§5.3 audit protocol 'review content characteristics' 表述张力 (R1-W1 reopened)\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"标记 resolved (改为 differential-performance-associated content characteristics)\"\n    - round: 13\n      reviewers: [2]\n      note: \"R2 认为新措辞仍有问题。R1 rebut (两阶段流程)。Director 降为 Should-Fix，建议精确化。\"\n  action_items:\n    - round: 13\n      action: \"改为 'prioritize flagged items for independent expert review'\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF4\"\n  summary: \"92.4% 'item-specific' 推导不透明 (与 pseudo R²=0.0007 关系不清)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"共识问题。推导链不可见，abstract/intro 反复引用但来源不明。\"\n  action_items:\n    - round: 13\n      action: \"明确写出 92.4% 的计算公式或推导逻辑\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF5\"\n  summary: \"Cluster bootstrap CI [26.7%, 53.2%] 应提升为 primary inference\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"Model-level CI 假设被违反。至少 abstract/conclusion 应同时报告两个 CI。\"\n  action_items:\n    - round: 13\n      action: \"Abstract/conclusion 同时报告 model-level 和 cluster bootstrap CI\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF6\"\n  summary: \"Cross-benchmark C% 可比性缺 formal 调整\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"Knowledge vs procedural 差异可能仅反映 difficulty/discriminability。\"\n  action_items:\n    - round: 13\n      action: \"Formal decomposition 或标注为 descriptive\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF7\"\n  summary: \"Discussion (§5) 过于压缩\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"三子节各 3-5 句。§5.1 因果模糊性、§5.2 implications 未充分展开。\"\n  action_items:\n    - round: 13\n      action: \"压缩 appendix 细节为 Discussion 腾空间\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF8\"\n  summary: \"'Measurement Instability' framing 偏强——DIF 也可反映 benchmark sensitivity\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 partial agree。建议 Discussion 加 instability vs sensitivity 辨析。\"\n  action_items:\n    - round: 13\n      action: \"Discussion 加 1-2 句辨析\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF9\"\n  summary: \"Semi-synthetic ecological validity——正文 claim 偏强 (R11-W7 reopened)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"标记 resolved (Limitations 覆盖)\"\n    - round: 13\n      reviewers: [1]\n      note: \"应在 Section 3.4 正文中明确 worst-case uniform 假设。\"\n  action_items:\n    - round: 13\n      action: \"Section 3.4 正文加 worst-case uniform caveat\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF10\"\n  summary: \"与 Growing Pains (Habba 2026) 区分不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"仅一句话。需增加 2-3 句实质性比较。\"\n  action_items:\n    - round: 13\n      action: \"Related Work 或 Discussion 增加实质性比较\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# OPEN INFO (carried from Round 11)\n# ============================================================\n\n- id: \"R11-I1\"\n  summary: \"Cohort 按 release date 划分，training data cutoff lag 讨论不足\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R2 Q3 再次提及。\"\n\n- id: \"R11-I2\"\n  summary: \"Multiple testing 论证呈现不够突出\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R1-M1: BH-FDR 解读需 caveat。\"\n\n- id: \"R11-I5\"\n  summary: \"术语不一致：temporal measurement instability / temporal DIF / measurement invariance\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"本轮未直接提及，R13-SF8 间接相关。\"\n\n- id: \"R11-I7\"\n  summary: \"K=5 quintile 在 bimodal 分布下的 adequacy\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R1 在方法论审查中再次关注。\"\n\n- id: \"R11-I8\"\n  summary: \"PSN-IRT parameters 可获取性未明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"本轮未提及。\"\n\n# ============================================================\n# PRIOR RESOLVED (no change)\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"Permutation null 已补充到 §4.2\"\n  resolution_round: 8\n\n- id: \"R8-MF2\"\n  summary: \"'Drift' framing 超出数据支撑\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Title 改为 'Temporal Measurement Instability'\"\n  resolution_round: 9\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%\"\n  resolution_round: 4\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 practical significance paradox\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 11\n  resolution: \"Family-level profiles + pairwise flip rate + 'diagnostic not destructive' framing\"\n  resolution_round: 11\n\n- id: \"R8-SF1\"\n  summary: \"Proposition 1 过度形式化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"降格为 Remark（§3.4）\"\n  resolution_round: 9\n\n- id: \"R9-W2\"\n  summary: \"方法新颖性有限\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"§3.2 引用先驱方法 + LLM-specific adaptation\"\n  resolution_round: 10\n\n- id: \"R10-W1\"\n  summary: \"LLM examinee 非独立性对统计推断的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Cluster bootstrap CI + LOFO Table 6\"\n  resolution_round: 12\n\n- id: \"R5-N1\"\n  summary: \"ΔTPR 应标注为 upper-bound estimate\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 11\n  resolution: \"Abstract/§3.4/§4.5 均标注 worst-case uniform injection\"\n  resolution_round: 10\n\n- id: \"R9-W3\"\n  summary: \"\\\\enlargethispage 过于激进\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"从 18→6→2\"\n  resolution_round: 12\n\n- id: \"R11-W1\"\n  summary: \"页数超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§5.3 压缩 + Conclusion 在 page 8 内\"\n  resolution_round: 12\n\n- id: \"R1-W1\"\n  summary: \"§5.3 audit protocol causal framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 11\n  resolution: \"改为 'review flagged items for differential-performance-associated content characteristics'\"\n  resolution_round: 12\n\n- id: \"R11-W2\"\n  summary: \"ΔFPR=0.000 缺 single-subject 限定\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Contribution 2 加 'under single-subject contamination'\"\n  resolution_round: 12\n\n- id: \"R11-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"删除 φ=0.012、ΔFPR<0.01 for k≤5、45-174×\"\n  resolution_round: 12\n\n- id: \"R11-W4\"\n  summary: \"Table 1 'FPR (clean)' 术语矛盾\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"列名改为 'C% (web-clean)'\"\n  resolution_round: 12\n\n- id: \"R11-W5\"\n  summary: \"Family-level cluster bootstrap CI 应在正文报告\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§4.2 加 family-level CI + LOFO\"\n  resolution_round: 12\n\n- id: \"R11-W6\"\n  summary: \"新颖性定位需区分 LLM adaptation\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§3.2 加三种 matching 策略区分\"\n  resolution_round: 12\n\n- id: \"R11-W7\"\n  summary: \"Semi-synthetic ecological validity 有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Limitations 覆盖\"\n  resolution_round: 12\n\n- id: \"R11-W8\"\n  summary: \"Graduated de-duplication 解读偏乐观\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"改为 'reduces C% moderately (confounded with power reduction)'\"\n  resolution_round: 12\n\n- id: \"R11-I3\"\n  summary: \"'200 most displaced models' selection bias\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"加 top 3.8% 和 full-sample flip rate\"\n  resolution_round: 12\n\n- id: \"R11-I4\"\n  summary: \"GSM1K 'suggests' 措辞略强\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"'suggests' → 'is consistent with'\"\n  resolution_round: 12\n\n- id: \"R11-I6\"\n  summary: \"Table 3 Ratio 列跨 benchmark 比较受 baseline 影响\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Table 3 caption 加说明\"\n  resolution_round: 12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Round 13 (Fresh review, 2026-05-22)\n# 2 critical open, 10 warning open, 5 info open\n\n# ============================================================\n# ROUND 13 — NEW / REOPENED ISSUES\n# ============================================================\n\n- id: \"R13-MF1\"\n  summary: \"LOFO family-concentration: 移除 Mistral/Llama-3 后 C% 降至 22-24%, power-reduction 解释不充分\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"N_ref≈533, N_focal≈492 仍远超 power threshold (N≥80)，8.8pp drop 不能仅归因 power reduction。Section 4.4 ~28% floor 与 LOFO 22.5% 的 tension 未讨论。\"\n  action_items:\n    - round: 13\n      action: \"使用 Monte Carlo 框架对 LOFO 进行 expected power calibration\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF2\"\n  summary: \"Examinee non-independence 对 MH chi-squared inflation 缺乏直接定量 (R10-W1 reopened)\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"首次提出\"\n    - round: 12\n      reviewers: []\n      note: \"标记 resolved (cluster bootstrap CI + LOFO)\"\n    - round: 13\n      reviewers: [1]\n      note: \"Reopened: 三项间接证据不足。需 DEFF / effective sample size 直接量化 chi-squared inflation。\"\n  action_items:\n    - round: 13\n      action: \"使用 design effect / effective sample size 方法调整 MH chi-squared\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF1\"\n  summary: \"新颖性定位——缺少与教育测量 temporal DIF rate baseline 对比 (R9-W2 related)\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 列 Must-Fix, R1 partial agree, Director 降级 Should-Fix。缺 SAT/GRE baseline (5-15%)。\"\n  action_items:\n    - round: 13\n      action: \"补充教育测量 temporal DIF rate baseline 对比 + 强化 LLM-specific novelty 论证\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF2\"\n  summary: \"Abstract 信息密度仍偏高 (R11-W3 reopened)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"标记 resolved (删除 φ, ΔFPR<0.01 for k≤5, 45-174×)\"\n    - round: 13\n      reviewers: [2]\n      note: \"R2 认为仍 15+ 数字，R1 rebut。Director 降为 Should-Fix。\"\n  action_items:\n    - round: 13\n      action: \"进一步精简至 5-7 个核心数字\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF3\"\n  summary: \"§5.3 audit protocol 'review content characteristics' 表述张力 (R1-W1 reopened)\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"标记 resolved (改为 differential-performance-associated content characteristics)\"\n    - round: 13\n      reviewers: [2]\n      note: \"R2 认为新措辞仍有问题。R1 rebut (两阶段流程)。Director 降为 Should-Fix，建议精确化。\"\n  action_items:\n    - round: 13\n      action: \"改为 'prioritize flagged items for independent expert review'\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF4\"\n  summary: \"92.4% 'item-specific' 推导不透明 (与 pseudo R²=0.0007 关系不清)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"共识问题。推导链不可见，abstract/intro 反复引用但来源不明。\"\n  action_items:\n    - round: 13\n      action: \"明确写出 92.4% 的计算公式或推导逻辑\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF5\"\n  summary: \"Cluster bootstrap CI [26.7%, 53.2%] 应提升为 primary inference\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"Model-level CI 假设被违反。至少 abstract/conclusion 应同时报告两个 CI。\"\n  action_items:\n    - round: 13\n      action: \"Abstract/conclusion 同时报告 model-level 和 cluster bootstrap CI\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF6\"\n  summary: \"Cross-benchmark C% 可比性缺 formal 调整\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"Knowledge vs procedural 差异可能仅反映 difficulty/discriminability。\"\n  action_items:\n    - round: 13\n      action: \"Formal decomposition 或标注为 descriptive\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF7\"\n  summary: \"Discussion (§5) 过于压缩\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"三子节各 3-5 句。§5.1 因果模糊性、§5.2 implications 未充分展开。\"\n  action_items:\n    - round: 13\n      action: \"压缩 appendix 细节为 Discussion 腾空间\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF8\"\n  summary: \"'Measurement Instability' framing 偏强——DIF 也可反映 benchmark sensitivity\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 partial agree。建议 Discussion 加 instability vs sensitivity 辨析。\"\n  action_items:\n    - round: 13\n      action: \"Discussion 加 1-2 句辨析\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF9\"\n  summary: \"Semi-synthetic ecological validity——正文 claim 偏强 (R11-W7 reopened)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"标记 resolved (Limitations 覆盖)\"\n    - round: 13\n      reviewers: [1]\n      note: \"应在 Section 3.4 正文中明确 worst-case uniform 假设。\"\n  action_items:\n    - round: 13\n      action: \"Section 3.4 正文加 worst-case uniform caveat\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF10\"\n  summary: \"与 Growing Pains (Habba 2026) 区分不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"仅一句话。需增加 2-3 句实质性比较。\"\n  action_items:\n    - round: 13\n      action: \"Related Work 或 Discussion 增加实质性比较\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# OPEN INFO (carried from Round 11)\n# ============================================================\n\n- id: \"R11-I1\"\n  summary: \"Cohort 按 release date 划分，training data cutoff lag 讨论不足\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R2 Q3 再次提及。\"\n\n- id: \"R11-I2\"\n  summary: \"Multiple testing 论证呈现不够突出\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R1-M1: BH-FDR 解读需 caveat。\"\n\n- id: \"R11-I5\"\n  summary: \"术语不一致：temporal measurement instability / temporal DIF / measurement invariance\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"本轮未直接提及，R13-SF8 间接相关。\"\n\n- id: \"R11-I7\"\n  summary: \"K=5 quintile 在 bimodal 分布下的 adequacy\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R1 在方法论审查中再次关注。\"\n\n- id: \"R11-I8\"\n  summary: \"PSN-IRT parameters 可获取性未明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"本轮未提及。\"\n\n# ============================================================\n# PRIOR RESOLVED (no change)\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"Permutation null 已补充到 §4.2\"\n  resolution_round: 8\n\n- id: \"R8-MF2\"\n  summary: \"'Drift' framing 超出数据支撑\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Title 改为 'Temporal Measurement Instability'\"\n  resolution_round: 9\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%\"\n  resolution_round: 4\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 practical significance paradox\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 11\n  resolution: \"Family-level profiles + pairwise flip rate + 'diagnostic not destructive' framing\"\n  resolution_round: 11\n\n- id: \"R8-SF1\"\n  summary: \"Proposition 1 过度形式化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"降格为 Remark（§3.4）\"\n  resolution_round: 9\n\n- id: \"R9-W2\"\n  summary: \"方法新颖性有限\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"§3.2 引用先驱方法 + LLM-specific adaptation\"\n  resolution_round: 10\n\n- id: \"R10-W1\"\n  summary: \"LLM examinee 非独立性对统计推断的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Cluster bootstrap CI + LOFO Table 6\"\n  resolution_round: 12\n\n- id: \"R5-N1\"\n  summary: \"ΔTPR 应标注为 upper-bound estimate\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 11\n  resolution: \"Abstract/§3.4/§4.5 均标注 worst-case uniform injection\"\n  resolution_round: 10\n\n- id: \"R9-W3\"\n  summary: \"\\\\enlargethispage 过于激进\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"从 18→6→2\"\n  resolution_round: 12\n\n- id: \"R11-W1\"\n  summary: \"页数超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§5.3 压缩 + Conclusion 在 page 8 内\"\n  resolution_round: 12\n\n- id: \"R1-W1\"\n  summary: \"§5.3 audit protocol causal framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 11\n  resolution: \"改为 'review flagged items for differential-performance-associated content characteristics'\"\n  resolution_round: 12\n\n- id: \"R11-W2\"\n  summary: \"ΔFPR=0.000 缺 single-subject 限定\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Contribution 2 加 'under single-subject contamination'\"\n  resolution_round: 12\n\n- id: \"R11-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"删除 φ=0.012、ΔFPR<0.01 for k≤5、45-174×\"\n  resolution_round: 12\n\n- id: \"R11-W4\"\n  summary: \"Table 1 'FPR (clean)' 术语矛盾\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"列名改为 'C% (web-clean)'\"\n  resolution_round: 12\n\n- id: \"R11-W5\"\n  summary: \"Family-level cluster bootstrap CI 应在正文报告\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§4.2 加 family-level CI + LOFO\"\n  resolution_round: 12\n\n- id: \"R11-W6\"\n  summary: \"新颖性定位需区分 LLM adaptation\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§3.2 加三种 matching 策略区分\"\n  resolution_round: 12\n\n- id: \"R11-W7\"\n  summary: \"Semi-synthetic ecological validity 有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Limitations 覆盖\"\n  resolution_round: 12\n\n- id: \"R11-W8\"\n  summary: \"Graduated de-duplication 解读偏乐观\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"改为 'reduces C% moderately (confounded with power reduction)'\"\n  resolution_round: 12\n\n- id: \"R11-I3\"\n  summary: \"'200 most displaced models' selection bias\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"加 top 3.8% 和 full-sample flip rate\"\n  resolution_round: 12\n\n- id: \"R11-I4\"\n  summary: \"GSM1K 'suggests' 措辞略强\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"'suggests' → 'is consistent with'\"\n  resolution_round: 12\n\n- id: \"R11-I6\"\n  summary: \"Table 3 Ratio 列跨 benchmark 比较受 baseline 影响\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Table 3 caption 加说明\"\n  resolution_round: 12"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-22T10:41:14.555038+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 13237}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-22T10:43:14.672728+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告：Temporal Measurement Instability in LLM Benchmarks\n\n**Venue**: EMNLP 2026 (ACL Rolling Review) | **类别**: Long Paper | **截止**: 2026-05-25\n**Reviewers**: R1 (方法严谨性+实验有效性) + R2 (新颖性+写作+格式)\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛判断 → 本报告\n\n---\n\n## Summary\n\n论文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，使用 METABENCH 响应矩阵（5,227 models × 12,508 MMLU items）发现 ~31% 的 items 在 2023 vs 2024 模型群体间展现 large temporal DIF (ETS C)。核心方法论贡献是 cross-subject matching 实现 ΔFPR=0.000，以及发现 DIF flags 与 web-overlap contamination labels 近乎正交（enrichment ≈ 0.96）。结果在 6 个 METABENCH benchmark 上复现（C% = 17.9–31.3%）。\n\n## Strengths\n\n1. **规模无出其右**：5,227 models × 12,508 items + 6 benchmarks 跨验证，迄今 LLM benchmark psychometric audit 中规模最大\n2. **Validity ladder 设计精良**：Random split (0.18%) → ability quintile (2.9%) → temporal (31.3%) → within-family (61.3%) 的阶梯式控制逻辑严密\n3. **Semi-synthetic framework 有方法论贡献**：ΔFPR=0 by construction（k ≤ 5），cross-subject matching 解决 matching variable contamination 问题\n4. **Ground truth meta-critique 有实用价值**：DIF-contamination 近正交（enrichment = 0.964, Jaccard = 0.206）直接挑战当前 contamination detection 验证范式\n5. **透明度**：包含 negative finding（Appendix F AUROC ≈ 0.60），cluster bootstrap CI 等保守估计，Limitations 覆盖适当\n6. **可复现性高**：匿名代码链接、公开数据（METABENCH）、实验参数完整\n\n## Weaknesses\n\n### Must-Fix（2 项，影响接收决定）\n\n**MF1. LOFO family-concentration 效应需 power-calibrated quantification** [R1-N1]\n- 移除 Mistral（547 models, 51% ref）后 C% 从 31.3% 降至 22.5%（-8.8pp），移除 Llama-3（315 models, 39% focal）后降至 24.1%（-7.3pp）\n- 论文归因 \"power reduction\"，但移除后 N_ref ≈ 533, N_focal ≈ 492，仍远超 power analysis 中 N ≥ 80 阈值\n- Section 4.4 称 \"none reduces C% below ~28%\"（指 matching/control 策略），但 LOFO 结果（22.5%, 24.1%）明确低于此下界——两类 robustness 结果的 tension 未被讨论\n- **核心风险**：若 DIF 信号高度集中于 Mistral/Llama-3，则 \"31% items show temporal DIF\" 的普适性被实质削弱\n- **修改要求**：使用 Monte Carlo 框架对 LOFO 进行 expected power calibration（N_ref=533, N_focal=807 下模拟 expected C%），量化 power drop 可解释的 C% 降幅\n\n**MF2. Examinee non-independence 对 MH chi-squared inflation 缺乏直接定量** [R1-N2]\n- 三项间接证据（permutation FPR < 0.001pp, de-duplication K=20 → C%=29.1%, cluster bootstrap CI [26.7%, 53.2%]）均未直接量化 chi-squared inflation\n- Cluster bootstrap upper bound 53.2%（3.1× model-level CI width）暗示 family-level clustering 对 point estimate 有 massive impact\n- **修改要求**：使用 design effect (DEFF) 或 effective sample size 方法估计 intra-family correlation 并调整 chi-squared 临界值，或在 graduated de-duplication 中固定 total N 以分离 power 和 correlation 效应\n\n### Should-Fix（10 项，影响评分但不一票否决）\n\n**SF1. 新颖性定位需强化** [R2-N3, R1 partial agree]\n- 缺少与传统教育测量 temporal DIF rates（SAT/GRE 典型 ETS C 5–15%）的 quantitative 对比\n- LLM-specific adaptation（57 subjects, local dependence, bimodal distribution）应更早更突出呈现\n\n**SF2. Abstract 信息密度偏高** [R2-N1 → Director 降级]\n- 15+ 统计量损害可读性，建议精简至 5–7 个核心数字\n- R1 认为与论文性质匹配，R2 列为 Must-Fix → Director 综合判定为 Should-Fix\n\n**SF3. §5.3 Audit Protocol framing 需精确化** [R2-N2 → Director 降级]\n- \"Review flagged items for content characteristics\" 与 \"detects THAT not WHY\" 存在表述张力\n- R1 指出 THAT/WHY 描述 method 本身，audit 是 downstream workflow，逻辑不矛盾但表述需精确化\n- 建议改为 \"prioritize flagged items for independent expert review\"\n\n**SF4. 92.4% \"item-specific\" 推导不透明** [R1 AGREE + R2-W5 — 共识]\n- Pseudo R² = 0.0007 与 92.4% 的关系不清晰，推导链在正文中不可见\n- 此数字在 abstract/intro 反复引用，需明确计算方式\n\n**SF5. Cluster bootstrap CI 应提升为 primary inference** [R1-W2]\n- Model-level CI [29.4%, 38.1%] 假设 models independent——已知被违反\n- 至少在 abstract/conclusion 同时报告 family-level CI [26.7%, 53.2%]\n\n**SF6. Cross-benchmark C% 可比性缺 formal 调整** [R1-W3]\n- Knowledge vs procedural C% 差异可能仅反映 difficulty/discriminability，需 formal decomposition 或标注为 descriptive\n\n**SF7. Discussion 过于压缩** [R1 partial agree + R2-W2]\n- 三子节各 3–5 句，§5.1 因果模糊性和 §5.2 meta-critique implications 未充分展开\n\n**SF8. \"Measurement Instability\" framing 偏强** [R1 partial agree + R2-W4]\n- DIF 也可能反映 genuine capability change（benchmark sensitivity 而非 instability）\n- 建议 Discussion 加 instability vs sensitivity 辨析\n\n**SF9. Semi-synthetic ecological validity 正文 claim 偏强** [R1-W1]\n- Binary response flipping 是 worst-case uniform，应在 Section 3.4 正文明确（而非仅 Limitations）\n\n**SF10. 与 Growing Pains (Habba 2026) 区分不充分** [R1 partial agree + R2-W1]\n- 仅一句话描述，需增加 2–3 句实质性比较\n\n### Minor（9 项）\n\n- m1: BH-FDR 只移除 3 items 可能反映 many-true-positives 场景下的 power 特性，需加 caveat\n- m2: Low-discrimination items TPR 仅 0.40，aggregate C% 可能 underestimate true DIF\n- m3: Equation (1) 缺 2×2 contingency table 图示\n- m4: Section 3.3 Cohort Designs 应用表格统一呈现\n- m5: Permutation 1,000 iterations 精度有限，建议增至 5,000+\n- m6: Table 1 dashes 的 caption 说明不够显眼\n- m7: Figure 1 应标注为 \"Schematic illustration\"\n- m8: 数值精度不一致（ρ 3位小数 vs C% 1位 vs ΔFPR 3位）\n- m9: Appendix F AUROC≈0.60 与 §5.3 audit protocol 关系可在 Discussion 更明确讨论\n\n## Reviewer Consensus\n\n1. **[AGREE] Overall 3.5 (Borderline Conference)**：两位 Reviewer 独立给出相同评分\n2. **[AGREE] 规模和系统性是核心优势**：5,227×12,508 + 6 benchmark 跨验证\n3. **[AGREE] Semi-synthetic ΔFPR=0 是 genuine 方法论贡献**\n4. **[AGREE] 92.4% 推导不透明需明确**（R1 AGREE R2-W5）\n5. **[AGREE] 教育测量 DIF rate baseline 对比缺失**（R1 partial agree R2-N3(c)）\n6. **[AGREE] Reproducibility 高**\n\n## Reviewer Divergence\n\n1. **Abstract 信息密度** — R2: Must-Fix ↔ R1: Minor → Director 判定 Should-Fix（信息密度确实偏高但非 soundness 问题）\n2. **§5.3 Audit Protocol** — R2: Must-Fix (矛盾) ↔ R1: REBUT (两阶段流程无矛盾) → Director 判定 Should-Fix（逻辑不矛盾但表述需精确化）\n3. **新颖性严重程度** — R2: Must-Fix ↔ R1: Should-Fix → Director 判定 Should-Fix（application paper 在 EMNLP 可接受，但需强化论证）\n\n## Questions\n\n1. 能否对 LOFO 进行 power-calibrated analysis？N_ref=533, N_focal=807 下模拟 expected C%（假设 true C%=31.3%），与 observed 22.5% 对比？\n2. 能否使用 design effect (DEFF) / effective sample size 直接量化 non-independence 对 MH chi-squared 的 inflation？\n3. 92.4% \"item-specific\" 的精确推导公式？与 pseudo R²=0.0007 的数值关系？\n4. 31% temporal DIF rate 在 SAT/GRE temporal DIF 研究中的对应 baseline？\n5. DIF 与 web-overlap 近正交——DIF 检测到的究竟是什么现象？\"underdetermined\" 是否过度回避？\n6. 实际应用中如何判断 contamination 是否已扩散到 >5 subjects（cross-subject matching boundary）？\n\n## Missing References\n\n1. **\"Test of Time\" (arXiv 2509.00072)** — 质疑 temporal contamination signals 有效性，与 §5.2 meta-critique 相关 [R2 推荐; R1 需验证]\n2. **Wainer et al. (2007) \"Testlet Response Theory\"** — testlet-level local dependence 与 LLM family non-independence 类似 [R1]\n3. **Rogers & Swaminathan (1993)** — Type I error rates under model violation [R1]\n4. **\"DIF: Implicit Bias in LLMs\" (arXiv 2505.10013)** — 术语歧义消解 [R2, 可选]\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2026-05-22 10:19–10:22 UTC）。0 critical / 1 warning / 4 info。\n\n- **[warning]** Pages 5-6 连续 2 页纯文本无 display item（Figure 1 到 Table 1 跨约 4 页），审稿人翻页体验单调\n- **[info]** Page 7 三个 display items 集中（Table 1 + Figure 2 + Table 2），与前几页节奏失衡\n- **[info]** 主文 8 页仅 5 个 display items（2 figures + 3 tables），对实证论文偏少\n- **[info]** Page 15 Figure 6 仅占上半页，底部约 50% 空白\n- 建议将 Table 1 或 Figure 2 前移至 p.5-6 区域打破文字墙\n\n## Overall Assessment\n\n**评分: 3.5 (Borderline Conference)**\n**置信度: 4/5**\n\n本文是一项规模空前的 LLM benchmark psychometric audit，将成熟的 MH-DIF 方法成功迁移至 LLM 评估场景，产出了有价值的实证发现（31% temporal DIF, DIF-contamination 正交性）和方法论贡献（cross-subject matching ΔFPR=0）。控制实验设计严密，可复现性高。\n\n两个方法论问题削弱了核心 claim 的确信度：\n\n(1) **LOFO family-concentration**：移除 Mistral/Llama-3 后 C% 降至 22–24%，power reduction 解释不充分——headline \"31%\" claim 的普适性需要 power-calibrated verification。\n(2) **Non-independence quantification**：examinee non-independence 对 MH chi-squared 的 inflation 缺乏直接定量，cluster bootstrap CI 宽度（3.1×）暗示 family-level dependence 的结构性影响。\n\n这两个问题均可在一个 ARR cycle 内解决（Monte Carlo power calibration for LOFO + design effect estimation），解决后论文可达 Conference (4.0) 水平。\n\n**维度评分综合**:\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 4.0 | 3.5 |\n| Excitement | 3.5 | 3.0 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n## Detailed Comments\n\n**Section 1 (Introduction)**: Contribution 3 最强；缺教育测量 DIF rate baseline 对比；novelty 论证应更早呈现 LLM-specific challenges\n\n**Section 3 (Method)**: §3.2 LLM-specific challenges 讨论较好但应更突出；§3.4 semi-synthetic worst-case uniform 假设应在正文明确；Equation (1) 缺 2×2 table 图示\n\n**Section 4 (Experiments)**: §4.2 validity ladder 有说服力；92.4% 推导链不清；§4.4 LOFO 结果与 ~28% floor claim 的 tension 需明确讨论；§4.7 GSM1K (N=33) 在 Discussion 中应保持 exploratory framing\n\n**Section 5 (Discussion)**: 整体过于压缩；§5.3 audit protocol 表述需精确化；缺 instability vs sensitivity 辨析；Growing Pains 比较不充分\n\n**Limitations**: 覆盖面适当，但 semi-synthetic ecological validity 可更突出\n\n**格式合规**: ✅ 8页正文 | ✅ 匿名性 | ✅ Limitations | ✅ ACL模板 | ✅ References格式",
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告：Temporal Measurement Instability in LLM Benchmarks\n\n**Venue**: EMNLP 2026 (ACL Rolling Review) | **类别**: Long Paper | **截止**: 2026-05-25\n**Reviewers**: R1 (方法严谨性+实验有效性) + R2 (新颖性+写作+格式)\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛判断 → 本报告\n\n---\n\n## Summary\n\n论文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，使用 METABENCH 响应矩阵（5,227 models × 12,508 MMLU items）发现 ~31% 的 items 在 2023 vs 2024 模型群体间展现 large temporal DIF (ETS C)。核心方法论贡献是 cross-subject matching 实现 ΔFPR=0.000，以及发现 DIF flags 与 web-overlap contamination labels 近乎正交（enrichment ≈ 0.96）。结果在 6 个 METABENCH benchmark 上复现（C% = 17.9–31.3%）。\n\n## Strengths\n\n1. **规模无出其右**：5,227 models × 12,508 items + 6 benchmarks 跨验证，迄今 LLM benchmark psychometric audit 中规模最大\n2. **Validity ladder 设计精良**：Random split (0.18%) → ability quintile (2.9%) → temporal (31.3%) → within-family (61.3%) 的阶梯式控制逻辑严密\n3. **Semi-synthetic framework 有方法论贡献**：ΔFPR=0 by construction（k ≤ 5），cross-subject matching 解决 matching variable contamination 问题\n4. **Ground truth meta-critique 有实用价值**：DIF-contamination 近正交（enrichment = 0.964, Jaccard = 0.206）直接挑战当前 contamination detection 验证范式\n5. **透明度**：包含 negative finding（Appendix F AUROC ≈ 0.60），cluster bootstrap CI 等保守估计，Limitations 覆盖适当\n6. **可复现性高**：匿名代码链接、公开数据（METABENCH）、实验参数完整\n\n## Weaknesses\n\n### Must-Fix（2 项，影响接收决定）\n\n**MF1. LOFO family-concentration 效应需 power-calibrated quantification** [R1-N1]\n- 移除 Mistral（547 models, 51% ref）后 C% 从 31.3% 降至 22.5%（-8.8pp），移除 Llama-3（315 models, 39% focal）后降至 24.1%（-7.3pp）\n- 论文归因 \"power reduction\"，但移除后 N_ref ≈ 533, N_focal ≈ 492，仍远超 power analysis 中 N ≥ 80 阈值\n- Section 4.4 称 \"none reduces C% below ~28%\"（指 matching/control 策略），但 LOFO 结果（22.5%, 24.1%）明确低于此下界——两类 robustness 结果的 tension 未被讨论\n- **核心风险**：若 DIF 信号高度集中于 Mistral/Llama-3，则 \"31% items show temporal DIF\" 的普适性被实质削弱\n- **修改要求**：使用 Monte Carlo 框架对 LOFO 进行 expected power calibration（N_ref=533, N_focal=807 下模拟 expected C%），量化 power drop 可解释的 C% 降幅\n\n**MF2. Examinee non-independence 对 MH chi-squared inflation 缺乏直接定量** [R1-N2]\n- 三项间接证据（permutation FPR < 0.001pp, de-duplication K=20 → C%=29.1%, cluster bootstrap CI [26.7%, 53.2%]）均未直接量化 chi-squared inflation\n- Cluster bootstrap upper bound 53.2%（3.1× model-level CI width）暗示 family-level clustering 对 point estimate 有 massive impact\n- **修改要求**：使用 design effect (DEFF) 或 effective sample size 方法估计 intra-family correlation 并调整 chi-squared 临界值，或在 graduated de-duplication 中固定 total N 以分离 power 和 correlation 效应\n\n### Should-Fix（10 项，影响评分但不一票否决）\n\n**SF1. 新颖性定位需强化** [R2-N3, R1 partial agree]\n- 缺少与传统教育测量 temporal DIF rates（SAT/GRE 典型 ETS C 5–15%）的 quantitative 对比\n- LLM-specific adaptation（57 subjects, local dependence, bimodal distribution）应更早更突出呈现\n\n**SF2. Abstract 信息密度偏高** [R2-N1 → Director 降级]\n- 15+ 统计量损害可读性，建议精简至 5–7 个核心数字\n- R1 认为与论文性质匹配，R2 列为 Must-Fix → Director 综合判定为 Should-Fix\n\n**SF3. §5.3 Audit Protocol framing 需精确化** [R2-N2 → Director 降级]\n- \"Review flagged items for content characteristics\" 与 \"detects THAT not WHY\" 存在表述张力\n- R1 指出 THAT/WHY 描述 method 本身，audit 是 downstream workflow，逻辑不矛盾但表述需精确化\n- 建议改为 \"prioritize flagged items for independent expert review\"\n\n**SF4. 92.4% \"item-specific\" 推导不透明** [R1 AGREE + R2-W5 — 共识]\n- Pseudo R² = 0.0007 与 92.4% 的关系不清晰，推导链在正文中不可见\n- 此数字在 abstract/intro 反复引用，需明确计算方式\n\n**SF5. Cluster bootstrap CI 应提升为 primary inference** [R1-W2]\n- Model-level CI [29.4%, 38.1%] 假设 models independent——已知被违反\n- 至少在 abstract/conclusion 同时报告 family-level CI [26.7%, 53.2%]\n\n**SF6. Cross-benchmark C% 可比性缺 formal 调整** [R1-W3]\n- Knowledge vs procedural C% 差异可能仅反映 difficulty/discriminability，需 formal decomposition 或标注为 descriptive\n\n**SF7. Discussion 过于压缩** [R1 partial agree + R2-W2]\n- 三子节各 3–5 句，§5.1 因果模糊性和 §5.2 meta-critique implications 未充分展开\n\n**SF8. \"Measurement Instability\" framing 偏强** [R1 partial agree + R2-W4]\n- DIF 也可能反映 genuine capability change（benchmark sensitivity 而非 instability）\n- 建议 Discussion 加 instability vs sensitivity 辨析\n\n**SF9. Semi-synthetic ecological validity 正文 claim 偏强** [R1-W1]\n- Binary response flipping 是 worst-case uniform，应在 Section 3.4 正文明确（而非仅 Limitations）\n\n**SF10. 与 Growing Pains (Habba 2026) 区分不充分** [R1 partial agree + R2-W1]\n- 仅一句话描述，需增加 2–3 句实质性比较\n\n### Minor（9 项）\n\n- m1: BH-FDR 只移除 3 items 可能反映 many-true-positives 场景下的 power 特性，需加 caveat\n- m2: Low-discrimination items TPR 仅 0.40，aggregate C% 可能 underestimate true DIF\n- m3: Equation (1) 缺 2×2 contingency table 图示\n- m4: Section 3.3 Cohort Designs 应用表格统一呈现\n- m5: Permutation 1,000 iterations 精度有限，建议增至 5,000+\n- m6: Table 1 dashes 的 caption 说明不够显眼\n- m7: Figure 1 应标注为 \"Schematic illustration\"\n- m8: 数值精度不一致（ρ 3位小数 vs C% 1位 vs ΔFPR 3位）\n- m9: Appendix F AUROC≈0.60 与 §5.3 audit protocol 关系可在 Discussion 更明确讨论\n\n## Reviewer Consensus\n\n1. **[AGREE] Overall 3.5 (Borderline Conference)**：两位 Reviewer 独立给出相同评分\n2. **[AGREE] 规模和系统性是核心优势**：5,227×12,508 + 6 benchmark 跨验证\n3. **[AGREE] Semi-synthetic ΔFPR=0 是 genuine 方法论贡献**\n4. **[AGREE] 92.4% 推导不透明需明确**（R1 AGREE R2-W5）\n5. **[AGREE] 教育测量 DIF rate baseline 对比缺失**（R1 partial agree R2-N3(c)）\n6. **[AGREE] Reproducibility 高**\n\n## Reviewer Divergence\n\n1. **Abstract 信息密度** — R2: Must-Fix ↔ R1: Minor → Director 判定 Should-Fix（信息密度确实偏高但非 soundness 问题）\n2. **§5.3 Audit Protocol** — R2: Must-Fix (矛盾) ↔ R1: REBUT (两阶段流程无矛盾) → Director 判定 Should-Fix（逻辑不矛盾但表述需精确化）\n3. **新颖性严重程度** — R2: Must-Fix ↔ R1: Should-Fix → Director 判定 Should-Fix（application paper 在 EMNLP 可接受，但需强化论证）\n\n## Questions\n\n1. 能否对 LOFO 进行 power-calibrated analysis？N_ref=533, N_focal=807 下模拟 expected C%（假设 true C%=31.3%），与 observed 22.5% 对比？\n2. 能否使用 design effect (DEFF) / effective sample size 直接量化 non-independence 对 MH chi-squared 的 inflation？\n3. 92.4% \"item-specific\" 的精确推导公式？与 pseudo R²=0.0007 的数值关系？\n4. 31% temporal DIF rate 在 SAT/GRE temporal DIF 研究中的对应 baseline？\n5. DIF 与 web-overlap 近正交——DIF 检测到的究竟是什么现象？\"underdetermined\" 是否过度回避？\n6. 实际应用中如何判断 contamination 是否已扩散到 >5 subjects（cross-subject matching boundary）？\n\n## Missing References\n\n1. **\"Test of Time\" (arXiv 2509.00072)** — 质疑 temporal contamination signals 有效性，与 §5.2 meta-critique 相关 [R2 推荐; R1 需验证]\n2. **Wainer et al. (2007) \"Testlet Response Theory\"** — testlet-level local dependence 与 LLM family non-independence 类似 [R1]\n3. **Rogers & Swaminathan (1993)** — Type I error rates under model violation [R1]\n4. **\"DIF: Implicit Bias in LLMs\" (arXiv 2505.10013)** — 术语歧义消解 [R2, 可选]\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2026-05-22 10:19–10:22 UTC）。0 critical / 1 warning / 4 info。\n\n- **[warning]** Pages 5-6 连续 2 页纯文本无 display item（Figure 1 到 Table 1 跨约 4 页），审稿人翻页体验单调\n- **[info]** Page 7 三个 display items 集中（Table 1 + Figure 2 + Table 2），与前几页节奏失衡\n- **[info]** 主文 8 页仅 5 个 display items（2 figures + 3 tables），对实证论文偏少\n- **[info]** Page 15 Figure 6 仅占上半页，底部约 50% 空白\n- 建议将 Table 1 或 Figure 2 前移至 p.5-6 区域打破文字墙\n\n## Overall Assessment\n\n**评分: 3.5 (Borderline Conference)**\n**置信度: 4/5**\n\n本文是一项规模空前的 LLM benchmark psychometric audit，将成熟的 MH-DIF 方法成功迁移至 LLM 评估场景，产出了有价值的实证发现（31% temporal DIF, DIF-contamination 正交性）和方法论贡献（cross-subject matching ΔFPR=0）。控制实验设计严密，可复现性高。\n\n两个方法论问题削弱了核心 claim 的确信度：\n\n(1) **LOFO family-concentration**：移除 Mistral/Llama-3 后 C% 降至 22–24%，power reduction 解释不充分——headline \"31%\" claim 的普适性需要 power-calibrated verification。\n(2) **Non-independence quantification**：examinee non-independence 对 MH chi-squared 的 inflation 缺乏直接定量，cluster bootstrap CI 宽度（3.1×）暗示 family-level dependence 的结构性影响。\n\n这两个问题均可在一个 ARR cycle 内解决（Monte Carlo power calibration for LOFO + design effect estimation），解决后论文可达 Conference (4.0) 水平。\n\n**维度评分综合**:\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 4.0 | 3.5 |\n| Excitement | 3.5 | 3.0 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n## Detailed Comments\n\n**Section 1 (Introduction)**: Contribution 3 最强；缺教育测量 DIF rate baseline 对比；novelty 论证应更早呈现 LLM-specific challenges\n\n**Section 3 (Method)**: §3.2 LLM-specific challenges 讨论较好但应更突出；§3.4 semi-synthetic worst-case uniform 假设应在正文明确；Equation (1) 缺 2×2 table 图示\n\n**Section 4 (Experiments)**: §4.2 validity ladder 有说服力；92.4% 推导链不清；§4.4 LOFO 结果与 ~28% floor claim 的 tension 需明确讨论；§4.7 GSM1K (N=33) 在 Discussion 中应保持 exploratory framing\n\n**Section 5 (Discussion)**: 整体过于压缩；§5.3 audit protocol 表述需精确化；缺 instability vs sensitivity 辨析；Growing Pains 比较不充分\n\n**Limitations**: 覆盖面适当，但 semi-synthetic ecological validity 可更突出\n\n**格式合规**: ✅ 8页正文 | ✅ 匿名性 | ✅ Limitations | ✅ ACL模板 | ✅ References格式",
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-22T10:43:18.895374+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4222
}
```

</details>

---


### Assistant

_source line 644 · 2026-05-22T10:43:32.503996+00:00_

审稿报告已投递至 Research Director。

---

**圆桌审稿完成，报告摘要：**

**Overall: 3.5 (Borderline Conference)** | Soundness 3.5 | Excitement 3.0 | Reproducibility 4.0

**2 个 Must-Fix**：
1. **LOFO family-concentration**：移除 Mistral/Llama-3 后 C% 降至 22–24%，power reduction 解释不充分，需 Monte Carlo power calibration
2. **Non-independence quantification**：需 design effect / effective sample size 直接量化 MH chi-squared inflation

**10 个 Should-Fix**（含 3 项从 R2 Must-Fix 降级）：novelty 定位、abstract 密度、§5.3 表述精确化、92.4% 推导链、cluster bootstrap 提升为 primary CI、cross-benchmark 可比性、Discussion 压缩、instability/sensitivity 辨析、semi-synthetic ecological validity、Growing Pains 区分

**核心判断**：两个方法论问题均可在一个 ARR cycle 内解决，解决后可达 Conference (4.0) 水平。Issue Tracker 已同步更新（R13: 2 critical + 10 warning + 5 info open）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 63

## Round 63

2 recorded events


### User

_source line 645 · 2026-05-22T10:43:33.991788+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条交叉回应。核心判断：

- R2 的三个 Must-Fix 中，N1（Abstract 密度）和 N2（Audit protocol 矛盾）我认为不构成 critical issues，建议降级；N3（novelty）部分同意缺少教育 DIF rate baseline 对比
- Should-Fix 中完全同意 W5（92.4% 推导不透明），反驳 W6（AUROC vs audit protocol 无张力）
- 我与 R2 的 Overall 一致（3.5），但核心 concerns 方向不同——R2 偏 framing/novelty，我偏 LOFO family-concentration 和 non-independence 定量化

---

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix 问题

### [AGREE] R1-N1: LOFO family-concentration 效应被低估

同意这是一个关键问题。我核实了 Table 6 (Appendix, Page 13)：移除 Mistral（547 models, 51% ref）后 C% 降至 22.47%，移除 Llama-3 后降至约 24%。Reviewer 1 正确指出移除后 N_ref ≈ 533, N_focal ≈ 492，远超 Table 4 (Page 13) 中 power analysis 的 N ≥ 80 阈值——单纯的 power reduction 无法解释 8.8pp 的下降。

补充观察：论文 Section 4.4 (Page 7) 声称 "none reduces C% below ~28% (Section B)"，但这仅指 structural controls（matched-ability quintiles, IRT θ-conditioning, within-subject pre-checks）。Table 6 的 LOFO 结果（22.5%, 24.1%）**低于**这个 28% 下界，两类 robustness 分析之间存在未讨论的 tension。论文需要明确回答：如果 28% 是 structural controls 的收敛下界，为什么移除单个 model family 可以突破它？这暗示部分 "temporal DIF" 实质上是 family-specific DIF。

不过我想补充一个 nuance：即使 22.5% 也仍然是 substantial temporal DIF rate。论文的核心 claim（LLM benchmarks 存在非trivial 的 temporal measurement instability）在 LOFO 后仍然成立，只是 31% 这个 headline number 的可信度受损。建议作者在正文中报告 LOFO-adjusted range（22-31%）作为更保守的估计。

### [AGREE] R1-N2: Examinee non-independence 对 MH chi-squared 的影响需直接量化

同意需要更直接的量化。Page 12 (Appendix A) 报告的 cluster bootstrap CI [26.7%, 53.2%] 的 3.1× width 确实暗示了 substantial family-level dependence。

但我想补充一个 Reviewer 1 未提到的缓解因素：ETS C 分类使用**双重阈值**——|Δ_MH| ≥ 1.5（效应量）AND p < 0.05（统计显著性）（Section 3.2, Page 4）。Chi-squared inflation 只影响 p 值，不影响效应量 Δ_MH。因此，即使 chi-squared 被 inflate，只有那些效应量本身就接近 1.5 阈值的 items 才可能被错误分类。效应量远超 1.5 的 items 不受影响。这意味着 non-independence 对 C% 的实际影响可能小于 Reviewer 1 暗示的程度。

尽管如此，我同意论文应该：(a) 使用 DEFF/effective sample size 方法提供直接量化；(b) 报告仅使用效应量阈值（不要求 significance）时的 C%，以分离 chi-squared inflation 的贡献。

---

## Should-Fix 问题

### [AGREE] R1-W1: Semi-synthetic injection 的 ecological validity

部分同意。Binary response flipping（incorrect → correct at uniform rate p）确实是简化的 worst-case 场景，Section 3.4 (Page 5) 和 Limitations (Page 9) 均有承认。

但有一个重要区分：**ΔFPR = 0 的保证是 distribution-free 的**——它 by construction 成立，不依赖于注入机制的具体形式（Page 5-6: "Therefore ΔFPR = 0 by construction"）。Ecological validity 的限制主要影响 ΔTPR 的 generalizability，而非 ΔFPR 的 validity。论文的 claim 若限定为 "cross-subject matching eliminates false positives regardless of contamination pattern"，则不受此批评影响。但如果 claim 扩展到 "the framework validates MH-DIF detection power in realistic scenarios"，则 Reviewer 1 的批评成立。

建议作者区分这两个层次的 claim。

### [AGREE] R1-W2: Cluster bootstrap 应为 primary CI

同意。3.1× 的 CI width 差异（standard bootstrap 约 8.5pp vs cluster bootstrap 26.5pp）清楚表明 family-level dependence 是实质性的，不是 negligible。在这种情况下，standard bootstrap CI 系统性低估了不确定性。学术标准要求在已知 clustering 存在时使用 cluster-adjusted inference 作为 primary。论文目前将 cluster bootstrap 放在 Appendix A 作为 robustness check，应提升为正文中的 primary CI。

### [AGREE] R1-W3: Cross-benchmark C% 可比性

同意 formal power decomposition 会加强分析。Table 3 (Page 8) 中 HellaSwag (N=10,042) 和 TruthfulQA (N=818) 的 item 数量差 12 倍，但 C% 差异相对较小（17.9% vs 26.0%）。这可能是因为 HellaSwag 的 large N 提供了更精确的估计（lower sampling variance），但也可能是因为 procedural benchmarks genuinely 有更少的 temporal DIF。

不过我认为 Reviewer 1 的建议（formal decomposition）可能在 8 页限制内难以实现。一个 pragmatic 替代方案是：在 Table 3 中增加一列报告每个 benchmark 的 effective power（如在给定 N 和 cohort sizes 下检测 medium DIF 的 power），让读者自行判断 C% 差异是否可归因于 power 差异。

### [REBUT] R1-W4: Within-family matched C% convergence (~28-29%) 可能是巧合

不同意这是"巧合"。Table 2 (Page 7) 显示三种独立的控制方法——matched-ability quintiles、IRT θ-conditioning、within-subject pre-checks——以及 Appendix B (Page 13) 的 de-duplication（K=10→29.1%, K=20→29.1%）均收敛到 ~28-29% 的下界。这些方法基于不同的假设和不同的 confound removal 机制：

1. Matched-ability quintiles 控制的是 ability-level confounding
2. IRT θ-conditioning 控制的是 latent ability 的连续分布
3. Within-subject pre-checks 控制的是 subject-level heterogeneity
4. De-duplication 控制的是 family-level non-independence

四种独立方法针对四种不同的 potential artifacts，却收敛到相同区间——这是 **triangulation** 的定义，不是巧合。如果是巧合，需要解释为什么四种不同的 bias sources 恰好都被"恰好"同等程度地去除。

Reviewer 1 需要提供一个替代解释：什么 common factor 会导致四种方法都稳定在 28-29%？如果没有这样的替代解释，收敛本身就是 robustness 的证据。

### [AGREE] R1-W5: GSM1K correlation (r=-0.478, N=33) 使用超出 exploratory

部分同意。Section 4.7/8 (Page 8) 中论文确实用了 "exploratory" 标注（"an exploratory GSM1K analysis is consistent with..."），文本措辞审慎。但 Figure 5 caption (Page 14) 使用了更强的 "indicates"（"The negative correlation... indicates that models with larger contamination gaps benefit less from DIF-flagged items"）。

N=33 的 correlation 对 outliers 高度敏感——一两个极端点可能驱动整个 correlation。建议：(a) 统一使用 "suggests" 而非 "indicates"；(b) 补充 rank-based correlation（如果还没有）和 influential point analysis（Cook's distance）；(c) 在 caption 中明确标注 N=33 和 "exploratory"。

---

## Minor 问题

### [AGREE] R1-M1: BH-FDR 解读需 caveat

技术上正确：BH-FDR 假设独立或 PRDS（positive regression dependency on a subset），同一 subject 内的 items 可能违反此假设。但 Page 7 报告 FDR 校正后 C% 仅从 31.25% 变为 31.30%（移除 3 items），说明 dual ETS threshold 已提供了隐式的 multiple testing 保护。实际影响 negligible，但一句 caveat 不费空间。

### [AGREE] R1-M2: Low-discrimination items 的 TPR 限制

同意。Table 4 (Page 13) 显示 κ=0.5 时 TPR ≈ 0.40，意味着 ~60% 的 low-discrimination DIF items 被遗漏。31% C% 可能是 **下界**而非全貌。论文应明确指出这一点——这实际上 **加强**了论文的核心 claim（真实 temporal DIF 可能比 31% 更高）。

### [AGREE] R1-M3: Equation (1) 需 2×2 table 图示

对 NLP 读者友好的改进。MH-DIF 中 A, B, C, D 的 notation 在 psychometrics 文献中是标准的，但对 EMNLP 读者需要额外的视觉辅助。

### [AGREE] R1-M4: Cohort Designs 应统一用表格呈现

Section 3.3 (Page 5) 列出 5 种 cohort designs 用文字描述，改为表格可提高可读性并节省空间。

### [AGREE] R1-M5: Permutation 1,000 iterations 精度有限

1,000 iterations 对 p ≈ 0.05 的 Monte Carlo standard error 约 ±0.014，10,000 iterations 可降至 ±0.004。这是一个 low-cost 改进。但鉴于 permutation FPR < 0.001pp（Page 6），即使精度有限，结论不太可能改变。

---

## Missing References

### [AGREE] Rogers & Swaminathan (1993)
关于 MH 在 model violation 下的 Type I error rates。与 N2 的 non-independence 讨论直接相关。

### [AGREE] Penfield (2001)
关于 small sample 下 MH DIF 的行为。与 LOFO 后 reduced sample 的讨论相关。

### [AGREE] Wainer et al. (2007) "Testlet Response Theory"
关于 testlet-level local dependence。这与 LLM family clustering 的类比很有启发性——LLM families 类似于 testlet 结构中的 local dependence units。

---

## Reviewer 2 的额外观察（补充 Reviewer 1 未涉及的问题）

以下问题在我的 Round 1 独立审稿中已提出，与 Reviewer 1 的关注点互补：

1. **§5.3 Audit Protocol 与 "detects THAT not WHY" 的内在矛盾**（我的 N2）：Reviewer 1 未涉及此问题。§5.3 建议 "review flagged items for differential-performance-associated content characteristics"，但论文反复声明 DIF 无法确定原因。这是论文最突出的 framing inconsistency。

2. **Abstract 信息过载**（我的 N1）：15+ 统计量塞入一个 abstract，远超可读性阈值。Reviewer 1 未提及此点。

3. **"Measurement Instability" 标题的 framing 问题**（我的 W4）：如果 temporal DIF 反映 genuine capability change，则 "instability" 暗示 benchmark 有缺陷，但实际上可能是 benchmark 正确捕捉了变化。

4. **Discussion 过于压缩**（我的 W2）：5.1-5.3 + Conclusion 全部压缩在不到半页，重要讨论点被草草带过。

5. **缺失引用 "Test of Time" (arXiv 2509.00072)**（我的 W3）：直接质疑 temporal contamination signal 的有效性，与本文高度相关。

---

## 综合评估

两位 Reviewer 独立给出相同的 Overall 评分（3.5 Borderline Conference），关注点互补：
- **Reviewer 1** 聚焦 statistical rigor（LOFO family concentration、non-independence、power）
- **Reviewer 2** 聚焦 novelty positioning、framing consistency、writing quality

核心共识：论文的 empirical contribution 是 solid 的（大规模 temporal DIF 分析 + cross-benchmark replication），但存在两类系统性问题需要修复：(1) statistical claims 的 robustness 需更诚实的报告（LOFO range, cluster bootstrap as primary）；(2) framing 和 writing 需要更精确和一致。若作者能在 revision 中同时解决这两类问题，论文有望提升至 Conference (4.0) 水平。


---

[Reviewer 2 审稿结果]:
交叉回应完成。总结：

- **R1 的 6 个 Must-Fix/Should-Fix 中 5 个 AGREE、1 个 REBUT**（W4 关于 28-29% 收敛是巧合——我认为四种独立方法收敛到相同区间是 triangulation 证据，不是巧合）
- **全部 5 个 Minor 和 3 个 Missing References 均 AGREE**
- 补充了 Reviewer 1 未涉及的 5 个独立发现（§5.3 framing 矛盾、Abstract 过载、标题 framing、Discussion 压缩、缺失引用 "Test of Time"）
- 两位 Reviewer 独立给出相同 Overall 3.5，关注点互补（R1 偏 statistical rigor，R2 偏 novelty/framing/writing）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 646 · 2026-05-22T10:44:10.651338+00:00_

Reviewer 2 的交叉回应已收到。两位 Reviewer 的交叉分享现已全部完成。

**交叉回应补充确认**：

R2 对 R1 的回应进一步巩固了已提交报告的共识：

| R1 议题 | R2 回应 | 影响 |
|---------|---------|------|
| N1 LOFO family-concentration | **AGREE** + 补充"22.5% 仍 substantial" | 强化 MF1 共识 |
| N2 Non-independence | **AGREE** + 补充"ETS dual threshold 部分缓解" | 强化 MF2 共识，但影响可能小于 R1 暗示 |
| W1 Semi-synthetic validity | **AGREE** + 区分 ΔFPR (不受影响) vs ΔTPR (受限) | 精确化了 SF9 |
| W2 Cluster bootstrap primary | **AGREE** | 强化 SF5 共识 |
| W3 Cross-benchmark comparability | **AGREE** | 强化 SF6 共识 |
| W4 Matched C% convergence | **REBUT** — 四种独立方法收敛是 triangulation 而非巧合 | R2 提供了有力反驳 |
| W5 GSM1K exploratory | **AGREE** | 共识 |

R2 的 REBUT 在 W4 上有力——四种方法（matched-ability/IRT θ/within-subject/de-duplication）基于不同假设却收敛到 ~28-29%，确实构成 triangulation 证据。此点已在报告的 Strengths 中通过 "validity ladder 设计精良" 隐含覆盖。

**报告无需重新提交**——R2 的交叉回应确认而非改变了已有共识，两个 Must-Fix 和整体 3.5 评分不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 64

## Round 64

46 recorded events


### User

_source line 647 · 2026-05-22T11:26:47.969488+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-22T11:26:54.205659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-22T11:26:54.256773+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-22T11:26:58.023017+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-22T11:26:58.023398+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-22T11:27:04.261887+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-22T11:27:04.716069+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-22T11:27:04.917623+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-22T11:27:05.018553+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-22T11:27:09.901505+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 657 · 2026-05-22T11:27:11.812361+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 658 · 2026-05-22T11:27:12.315015+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Measurement Instability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 659 · 2026-05-22T11:27:12.466137+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "paper_framing.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "file": "paper_framing.md",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 660 · 2026-05-22T11:27:22.213326+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here's a comprehensive overview of the EMNLP 2026 ARR submission guidelines and author instructions:

## Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existin
…[truncated 2779 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 12311
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-22T11:27:22.214100+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md\", \"content\": \"# Paper Framing — irt_equated_bench_regen\\n\\n## Target Venue\\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\\n\\n## Paper Type\\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \\\"DIF reveals benchmark structural problems,\\\" not \\\"DIF detects contamination.\\\"\\n\\n## Core Claims (4 条, 可证伪)\\n\\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), pla
…[truncated 4376 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 9747
}
```

</details>

---


### Tool call

_source line 662 · 2026-05-22T11:27:36.791007+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May submission format page limit long short paper template",
  "allowed_domains": "['aclrollingreview.org', 'aclweb.org', '2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May submission format page limit long short paper template",
    "allowed_domains": "['aclrollingreview.org', 'aclweb.org', '2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 663 · 2026-05-22T11:27:37.745667+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 664 · 2026-05-22T11:27:37.946920+00:00_

1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet whether individual items measure the same construct over time is rarely tested---and existing contamination detectors validate against ground truth that conflates global exposure with differential functioning. We develop a semi-synthetic injection framework with cross-subject matching that achieves zero false positive inflation under single-subject contamination ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power under worst-case uniform injection ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$), and show that web-overlap contamination labels are near-independent of Mantel-Haenszel Differential Item Functioning (DIF) flags (enrichment $\approx 0.96$)---exposing a category error in prevailing validation methodology. Applying MH-DIF with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 items), we find 17.9--31.3\% of items exhibit large temporal DIF (ETS~C; family-level cluster bootstrap CI $[26.7\%, 53.2\%]$) between 2023 and 2024 cohorts, with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). This does not threaten aggregate ranking validity ($\rho \approx 0.997$, $\tau \approx 0.958$), but specific model families show concentrated rank shifts (Llama-3: ${+}53$ median positions, Mistral: $-35$) and 2.0\% of pairwise rankings reverse. Item-level decomposition confirms the signal is predominantly item-specific (domain pseudo $R^2 < 0.001$), with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 665 · 2026-05-22T11:27:37.947293+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 666 · 2026-05-22T11:27:38.098219+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. This pattern persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and domain-level accuracy gains explain ${<}0.1\%$ of DIF variance (pseudo $R^2 = 0.0007$). Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this measurement instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference~\citep{shi2024mink} to performance-based detectors~\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}. These methods validate detection accuracy primari
…[truncated 4859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-22T11:27:43.119772+00:00_

Web search results for query: "ACL Rolling Review 2026 May submission format page limit long short paper template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, I found information about ACL Rolling Review submission format and page limits:

## Page Limits

Long papers follow an 8-page limit for content, while short papers follow a 4-page limit, not including limitations and ethical con
…[truncated 1181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 6328
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-22T11:27:56.675763+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-22T11:27:57.630370+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-22T11:27:57.630876+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-22T11:27:57.834097+00:00_

-rw-r--r-- 1 ubuntu ubuntu 628532 May 22 11:19 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-22T11:28:02.706245+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-22T11:28:02.756872+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-22T11:28:07.026770+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "glob": "*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
    "glob": "*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-22T11:28:07.129512+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Grep",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-22T11:28:11.056916+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "glob": "**/config*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
    "glob": "**/config*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-22T11:28:11.107664+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-22T11:28:14.627922+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "glob": "**/*.yaml",
  "output_mode": "content",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
    "glob": "**/*.yaml",
    "output_mode": "content",
    "head_limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-22T11:28:14.678738+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-22T11:28:21.515733+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-22T11:28:21.617016+00:00_

# Review Issues Tracker — irt_equated_bench_regen
# Round 13 (Fresh review, 2026-05-22)
# 2 critical open, 10 warning open, 5 info open

# ============================================================
# ROUND 13 — NEW / REOPENED ISSUES
# ============================================================

- id: "R13-MF1"
  summary: "LOFO family-concentration: 移除 Mistral/Llama-3 后 C% 降至 22-24%, power-reduction 解释不充分"
  category: experiment
  severity: critical
  status: open
  first_raised_round: 13
  last_seen_round: 13
  mentions:
    - round: 13
      reviewers: [1]
      note: "N_ref≈533, N_focal≈492 仍远超 power threshold (N≥80)，8.8pp drop 不能仅归因 power reduction。Section 4.4 ~28% floor 与 LOFO 22.5% 的 tension 未讨论。"
  action_items:
    - round: 13
      action: "使用 Monte Carlo 框架对 LOFO 进行 expected power calibration"
      assigned_to: ""
      status: pending
  resolution: ""
  resolution_round: null

- id: "R13-MF2"
  summary: "Examinee non-independence 对 MH chi-squared inflation 缺乏直接定量 (R10-W1 reopened)"
  category: method
  severity: critical
  status: open
  first_raised_round: 10
  last_seen_round: 13
  mentions:
    - round: 10
      reviewers: [1]
      note: "首次提出"
    - round: 12
      reviewers: []
      note: "标记 resolved (cluster bootstrap CI + LOFO)"
    - round: 13
      reviewers: [1]
      note: "Reopened: 三项间接证据不足。需 DEFF / effective sample size 直接量化 chi-squared inflation。"
  action_items:
    - round: 13
      action: "使用 design effect / effective sample size 方法调整 MH chi-squared"
      assigned_to: ""
      status: pending
  resolution: ""
  resolution_round: null

- id: "R13-SF1"
  summary: "新颖性定位——缺少与教育测量 temporal DIF rate baseline 对比 (R9-W2 related)"
  category: framing
  severity: warning
  status: open
  first_raised_round: 9
  last_seen_round: 13
  mentions:
    - round: 13
      reviewers: [1, 2]
      note: "R2 列 Must-Fix, R1 partial agree, Director 降级 Should-Fix。缺 SAT/GRE baseline (5-15%)。"
  action_items:
    - round: 13
      action: "补充教育测量 tempora
…[truncated 11237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-22T11:28:50.645102+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 683 · 2026-05-22T11:29:07.539916+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 16894
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-22T11:29:09.005607+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你负责审查本文的**方法严谨性、统计推断和实验设计**。\n\n## 论文信息\n- 标题: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n- 路径: projects/irt_equated_bench_regen/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026** (via ARR May cycle, deadline 2026-05-25)\n- Long paper: 8 页正文限制 + 无限参考文献\n- 模板: ACL template (double-blind)\n- Limitations section 必须存在\n- Appendix 可选，reviewers 不要求阅读\n\n## 你的审查侧重\n\n1. **统计方法论**:\n   - MH-DIF 的假设是否满足（examinee independence, unidimensionality）？论文是否充分讨论违反假设的影响？\n   - ETS C 分类阈值（|Δ_MH|≥1.5）的选择是否恰当？阈值敏感性分析是否充分？\n   - 样本量和统计功效分析是否充分？\n   - 多重检验校正方法是否恰当？\n\n2. **实验设计**:\n   - Temporal cohort 划分方式是否合理？是否存在 confound？\n   - Semi-synthetic injection framework 的生态效度如何？假设是否过强？\n   - Cross-subject matching 的 $\\Delta$FPR=0.000 是否在合理条件下成立？\n   - 控制实验（random split, matched-ability quintile, θ-conditioning）是否充分排除了替代解释？\n\n3. **Claims vs Evidence**:\n   - 每个 claim 是否有充分的统计证据支撑？\n   - 置信区间和效应量报告是否完整？\n   - Cluster bootstrap CI [26.7%, 53.2%] vs model-level CI 的 tension 如何处理？\n\n4. **格式合规**:\n   - 正文是否在 8 页以内？\n   - Limitations section 是否存在且充分？\n\n请按 Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions 格式输出审稿报告。",
  "project": "irt_equated_bench_regen",
  "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
  "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你负责审查本文的**方法严谨性、统计推断和实验设计**。\n\n## 论文信息\n- 标题: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n- 路径: projects/irt_equated_bench_regen/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026** (via ARR May cycle, deadline 2026-05-25)\n- Long paper: 8 页正文限制 + 无限参考文献\n- 模板: ACL template (double-blind)\n- Limitations section 必须存在\n- Appendix 可选，reviewers 不要求阅读\n\n## 你的审查侧重\n\n1. **统计方法论**:\n   - MH-DIF 的假设是否满足（examinee independence, unidimensionality）？论文是否充分讨论违反假设的影响？\n   - ETS C 分类阈值（|Δ_MH|≥1.5）的选择是否恰当？阈值敏感性分析是否充分？\n   - 样本量和统计功效分析是否充分？\n   - 多重检验校正方法是否恰当？\n\n2. **实验设计**:\n   - Temporal cohort 划分方式是否合理？是否存在 confound？\n   - Semi-synthetic injection framework 的生态效度如何？假设是否过强？\n   - Cross-subject matching 的 $\\Delta$FPR=0.000 是否在合理条件下成立？\n   - 控制实验（random split, matched-ability quintile, θ-conditioning）是否充分排除了替代解释？\n\n3. **Claims vs Evidence**:\n   - 每个 claim 是否有充分的统计证据支撑？\n   - 置信区间和效应量报告是否完整？\n   - Cluster bootstrap CI [26.7%, 53.2%] vs model-level CI 的 tension 如何处理？\n\n4. **格式合规**:\n   - 正文是否在 8 页以内？\n   - Limitations section 是否存在且充分？\n\n请按 Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions 格式输出审稿报告。",
    "project": "irt_equated_bench_regen",
    "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
    "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-22T11:29:22.482071+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13476
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-22T11:29:22.933878+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你负责审查本文的**新颖性/贡献定位、论文结构/可读性、以及相关工作覆盖**。\n\n## 论文信息\n- 标题: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n- 路径: projects/irt_equated_bench_regen/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026** (via ARR May cycle, deadline 2026-05-25)\n- Long paper: 8 页正文限制 + 无限参考文献\n- 模板: ACL template (double-blind)\n- Limitations section 必须存在\n- Appendix 可选，reviewers 不要求阅读\n\n## 你的审查侧重\n\n1. **新颖性与贡献**:\n   - MH-DIF 是教育测量经典方法——应用到 LLM benchmarks 的增量贡献是否足够 EMNLP？\n   - 三个 contributions (ground truth meta-critique, semi-synthetic framework, temporal instability at scale) 的新颖性如何？\n   - 与 concurrent work (Growing Pains / Habba 2026, DVD / Liang 2026, etc.) 的区分是否清晰？\n   - 发现的 novelty 还是方法论的 novelty？对 NLP community 的 actionable insight 是什么？\n\n2. **论文结构与可读性**:\n   - Abstract 信息密度是否过高？关键信息是否突出？\n   - Introduction 的叙事逻辑是否清晰？\n   - Methods/Experiments/Discussion 的篇幅分配是否合理？\n   - Discussion 是否充分展开（因果解释、implications、limitations）？\n   - 全文术语使用是否一致（temporal measurement instability / temporal DIF / measurement invariance）？\n\n3. **相关工作**:\n   - 教育测量/psychometrics 文献的覆盖是否充分？\n   - LLM contamination detection 文献是否完整？\n   - 是否有重要遗漏的 recent work？\n   - 与 benchmark design/evaluation 文献的联系是否建立？\n\n4. **格式合规**:\n   - Double-blind 匿名是否达标（无作者信息泄露）？\n   - 引用格式是否符合 ACL 标准？\n   - Figure/Table 质量和自解释性如何？\n\n请按 Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References 格式输出审稿报告。",
  "project": "irt_equated_bench_regen",
  "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
  "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你负责审查本文的**新颖性/贡献定位、论文结构/可读性、以及相关工作覆盖**。\n\n## 论文信息\n- 标题: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n- 路径: projects/irt_equated_bench_regen/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_7/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026** (via ARR May cycle, deadline 2026-05-25)\n- Long paper: 8 页正文限制 + 无限参考文献\n- 模板: ACL template (double-blind)\n- Limitations section 必须存在\n- Appendix 可选，reviewers 不要求阅读\n\n## 你的审查侧重\n\n1. **新颖性与贡献**:\n   - MH-DIF 是教育测量经典方法——应用到 LLM benchmarks 的增量贡献是否足够 EMNLP？\n   - 三个 contributions (ground truth meta-critique, semi-synthetic framework, temporal instability at scale) 的新颖性如何？\n   - 与 concurrent work (Growing Pains / Habba 2026, DVD / Liang 2026, etc.) 的区分是否清晰？\n   - 发现的 novelty 还是方法论的 novelty？对 NLP community 的 actionable insight 是什么？\n\n2. **论文结构与可读性**:\n   - Abstract 信息密度是否过高？关键信息是否突出？\n   - Introduction 的叙事逻辑是否清晰？\n   - Methods/Experiments/Discussion 的篇幅分配是否合理？\n   - Discussion 是否充分展开（因果解释、implications、limitations）？\n   - 全文术语使用是否一致（temporal measurement instability / temporal DIF / measurement invariance）？\n\n3. **相关工作**:\n   - 教育测量/psychometrics 文献的覆盖是否充分？\n   - LLM contamination detection 文献是否完整？\n   - 是否有重要遗漏的 recent work？\n   - 与 benchmark design/evaluation 文献的联系是否建立？\n\n4. **格式合规**:\n   - Double-blind 匿名是否达标（无作者信息泄露）？\n   - 引用格式是否符合 ACL 标准？\n   - Figure/Table 质量和自解释性如何？\n\n请按 Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References 格式输出审稿报告。",
    "project": "irt_equated_bench_regen",
    "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
    "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-22T11:29:24.444528+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1510
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-22T11:29:29.734883+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-22T11:29:29.786584+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-22T11:29:37.281275+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排 (2人)', 'status': 'completed', 'activeForm': '完成 Reviewer 编排决定'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '完成视觉审查派发'}, {'content': 'Step 1: Round 1 独立审稿 — 等待 Reviewer 1 & 2 返回', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 & 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见互评', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排 (2人)', 'status': 'completed', 'activeForm': '完成 Reviewer 编排决定'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '完成视觉审查派发'}, {'content': 'Step 1: Round 1 独立审稿 — 等待 Reviewer 1 & 2 返回', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 & 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见互评', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-22T11:29:37.331889+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 692 · 2026-05-22T11:29:42.494288+00:00_

已派发全部任务：
- **视觉审查 Agent**：已启动（fire-and-forget）
- **Reviewer 1**（方法严谨性 + 统计推断 + 实验设计）：已分配
- **Reviewer 2**（新颖性/贡献定位 + 论文结构/可读性 + 相关工作）：已分配

等待两位 Reviewer 完成 Round 1 独立审稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 65

## Round 65

2 recorded events


### User

_source line 693 · 2026-05-22T11:34:55.613125+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：Round 1

**论文**: "Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models"
**Venue**: EMNLP 2026 (via ARR May cycle)
**审查侧重**: 新颖性/贡献定位、论文结构/可读性、相关工作覆盖、格式合规

---

## 总体评分

**Overall**: 3.5 / 5（Borderline Conference）

**一句话总结**: 方法学扎实、规模空前的 psychometric audit，ground truth meta-critique 贡献有价值，但新颖性主要在应用层面而非方法论层面，Discussion 发展不充分限制了对 NLP 社区的 actionable impact。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | MH-DIF 方法本身成熟可靠；6 项 robustness controls 严谨；但 temporal cohort 的 binary 2023 vs 2024 划分过粗，且无法归因 DIF 的 cause |
| Excitement | 3/5 | Ground truth meta-critique 是 genuinely valuable insight；但核心方法是 1988 年的 MH procedure 直接应用，temporal instability 的发现与已有 contamination 文献方向一致，对 NLP 社区的行为改变建议不够具体 |
| Reproducibility | 4/5 | 匿名代码链接已提供，数据来自公开的 METABENCH，方法细节充分（ETS 分类标准、匹配策略、注入框架均有完整说明） |
| Datasets | 3/5 | 未发布新数据集；使用已有的 METABENCH + Li et al. web-overlap labels |
| Software | 3/5 | 承诺开源 DIF audit scripts，但尚未验证可用性 |

**Reviewer Confidence**: 4/5（对 DIF 方法论和 LLM evaluation 文献均较熟悉，仔细阅读了全文含附录）

---

## 主要优势

**S1. Ground truth meta-critique 是本文最重要的贡献。** §4.3 证明 web-overlap labels 与 DIF flags 近乎独立（enrichment = 0.964, Jaccard = 0.206, φ = 0.012），这揭示了现有 contamination detection 文献中一个系统性的 validation methodology gap。该发现对所有用 web-overlap labels 做 ground truth 的后续工作都有直接影响。

**S2. 规模和 robustness 令人信服。** 5,227 models × 12,508 items 是迄今最大规模的 LLM DIF 分析。6 种 structural controls（random split、ability-quintile、within-family、matched-ability、IRT θ-conditioning、de-duplication）系统排除了替代解释。Cross-benchmark replication 在 6 个 METABENCH benchmarks 上确认了 pattern 的普遍性。

**S3. Cross-subject matching 是对经典 DIF 方法的有价值适配。** 将 purified subtest matching 适配到 MMLU 的 57-subject 结构，理论上保证单科污染下 ΔFPR = 0（§3.4 Remark），经验验证也支持（Table 5, k ≤ 5 时 ΔFPR < 0.007）。这是方法论上的 genuine contribution。

**S4. 写作整体质量高。** 对 NLP 读者不熟悉的 psychometric 概念（DIF、ETS 分类、MH procedure）解释清晰。Figure 1 的 ICC schematic 有效帮助理解 global vs. differential contamination 的区别。

**S5. Semi-synthetic validation framework 设计合理。** Dose-response 曲线（Figure 2）清晰展示检测灵敏度，ΔFPR = 0 的 constructive guarantee 增强了方法可信度。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Discussion 对于一篇 "diagnostic" 论文而言严重不足

- 具体位置：§5（Discussion），仅占约半页，3 个小节
- 问题：论文反复强调其贡献是 "methodological and empirical, not algorithmic"（§1），是 "diagnostic lens rather than a quality filter"（§1），但 Discussion 没有充分展开诊断的含义。§5.1 仅一段话讨论 temporal comparability implications；§5.2 Ground Truth Meta-Critique 重复了 §4.3 的要点；§5.3 提出的 Monitor/Flag/Act 阈值（15%/25%）虽有 ρ-degradation grounding 但主文中没有展示这些阈值如何从 Figure 6 推导出来。
- 缺失的关键讨论：
  - **因果归因的框架性讨论**：论文说 DIF 检测 "that" not "why"，但在 Discussion 中应系统讨论可能的 cause taxonomy（contamination vs. capability evolution vs. training methodology shifts），并分析各 cause 的 testable predictions。目前唯一的 "why" 分析是 GSM1K 相关性（r = -0.478, N = 33），被标注为 "exploratory"。
  - **对 NLP 社区实践的具体影响**：benchmark maintainers 应该如何行动？leaderboard operators 应该展示什么额外信息？model developers 应该如何解读 DIF-adjusted rankings？
  - **与 benchmark reform 更广泛运动的联系**：MMLU-CF（Zhao et al., ACL 2025）已经通过重构 items 解决 contamination，dynamic benchmarks 也在兴起——temporal DIF monitoring 在这个 landscape 中的定位是什么？
- 为什么影响接收：一篇定位为 "diagnostic" 的论文如果不充分 discuss 诊断结果的 implications，其核心 value proposition 就不完整。Reviewer 会问 "so what?"
- 建议修改方向：将 Discussion 扩展至至少 1 页；增加因果假说的系统讨论；明确 Monitor/Flag/Act 阈值的 ρ-degradation 推导过程；讨论 DIF monitoring 与现有 benchmark reform 方案的互补关系。

**N2** [critical] 新颖性定位需要更清晰地与 concurrent work 区分

- 具体位置：§2 Related Work "IRT in LLM Evaluation" 段
- 问题：与 Growing Pains（Habba et al., 2026）的区分叙述为 "diagnostic foundation" vs. "prescriptive framework"，但两项工作都在做 temporal LLM benchmark comparability analysis。论文声称 "their anchor-item approach can directly consume our stable-item set as pre-screened equating anchors"——这是 integration argument 而非 differentiation argument。更关键的是，论文没有说明：如果读者只能读一篇关于 LLM benchmark temporal comparability 的论文，为什么应该读这篇而不是 Growing Pains？
- 此外，Benchmark Health Index（Zhu et al., 2026）和 Benchmark²（Qian & Huang, 2026）在 §2 最后一段仅各一句带过，没有实质性对比。
- 为什么影响接收：EMNLP reviewers 会特别关注与 concurrent work 的 incremental contribution。当 3-4 篇同期工作都在 psychometric 视角审视 LLM benchmarks 时，必须 sharply 说明本文的 unique angle。
- 建议修改方向：在 Introduction 或 Related Work 中增加一个明确的 positioning paragraph，用表格或要点列表对比本文与 Growing Pains / BHI / Benchmark² 在 scope、method、findings、actionable output 方面的差异。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 信息密度过高，关键信息被稀释

- 具体位置：Abstract（整段）
- 问题：Abstract 在一段中塞入了 3 个 contributions，每个都带具体数字（ΔFPR = 0.000、ΔTPR = +0.508、enrichment ≈ 0.96、31%、[26.7%, 53.2%]、ρ ≈ 0.997、+53 positions 等）。对不熟悉 DIF 的 NLP 读者来说，第一次阅读很难抓住核心 message。
- 建议：将 Abstract 重构为：(1) 问题陈述（1-2 句）→ (2) 核心发现（ground truth mismatch + temporal instability，各 1 句）→ (3) 关键数字（选 2-3 个最重要的）→ (4) Implication（1 句）。Semi-synthetic framework 的技术细节可以降级。

**W2** [warning] 术语使用不够一致

- 具体位置：全文
- 问题：Title 用 "temporal measurement instability"，正文交替使用 "temporal DIF"、"measurement instability"、"measurement invariance"、"differential item functioning"。虽然这些概念有关联，但 psychometric 文献中 "measurement invariance"（Meredith, 1993）是一个比 DIF 更广的概念框架，而 "temporal measurement instability" 是论文自创的术语。
- 建议：在 §1 或 §3 早期明确定义首选术语并说明与相关概念的关系，之后保持一致。建议以 "temporal DIF" 为核心技术术语，"temporal measurement instability" 仅作为面向 general audience 的 non-technical descriptor。

**W3** [warning] Temporal cohort 划分过于粗糙

- 具体位置：§3.3 Cohort Designs
- 问题：主对比为 2023 vs. 2024 calendar year，这是非常粗的时间粒度。Limitations §已承认这一点（"finer-grained definitions... might reveal more targeted patterns"），但 §4.7 显示 6-month window（2023-H2 vs. 2024-H1）的 C% = 34.35%，甚至比全年对比更高。这值得在 Discussion 中深入分析：是否意味着 DIF 主要集中在时间边界附近？是否与特定模型发布事件（如 Llama-3 发布）有关？
- 建议：增加 2-3 个更细粒度的 temporal split 分析（例如按季度），或至少在 Discussion 中系统讨论 temporal granularity 对结果的影响。

**W4** [warning] "Are We Done with MMLU?"（Gema et al., 2024）在 bib 中但未在正文讨论

- 具体位置：§2 Related Work
- 问题：Gema et al. (2024) 详细分析了 MMLU 的 ground truth errors（57% virology questions 有问题）、item quality 问题等。这与本文的 MMLU item-level analysis 高度相关。如果 MMLU items 本身有大量 ground truth errors，那么 DIF 分析中的一部分 "temporal instability" 可能反映的是 models 学会了正确答案而 MMLU 的 ground truth key 是错的。这是一个重要的 confound。
- 建议：在 Related Work 或 Limitations 中讨论 MMLU item quality issues 对 DIF 分析的潜在影响。

**W5** [warning] Item-Property Predictive Analysis（App F）的 negative finding 在主文中过于简短

- 具体位置：§5.3 仅一句 "Item-level properties do not reliably predict DIF susceptibility (AUROC = 0.60; App F)"
- 问题：AUROC ≈ 0.60 这个 near-chance 结果实际上是一个 important finding（DIF 是 emergent cohort-item interaction 而非 fixed item property），值得在主文中更充分展开。它支撑了 "post-hoc monitoring over pre-screening" 的建议，但当前的一句话处理让读者可能忽略其重要性。
- 建议：在 Discussion 中用 2-3 句话讨论这个 negative finding 的含义。

---

## 小问题（不影响接收）

- §5 Discussion 的 `\enlargethispage*{8\baselineskip}` 是激进的排版操作，额外挤入了约 8 行内容。虽然技术上合规，但 camera-ready 阶段可能被格式检查标记。
- Table 2、Table 3 使用 `\resizebox{\columnwidth}` 导致字体偏小，建议检查最终 PDF 中的可读性。
- §1 Introduction 约 1.5 页，前几段就密集引用了大量具体数字（31%、0.997、0.18%、0.206 等），建议适当推迟数字细节到 Results 部分。
- Conclusion（§6）仅 3 行，对于 8 页 paper 过于简短。虽然 EMNLP 对 Conclusion 长度无硬性要求，但建议至少增加 2-3 句讨论 future directions。
- Figure 2 caption 中 "Baseline (no injection) produces ΔTPR ≈ 0" 可改为 "= 0" 以与正文一致。
- §3.2 最后的 "LLM-specific challenges" paragraph 很长（近半页），可考虑用 itemized list 提高可读性。

---

## Questions for Authors

**Q1**: §4.2 报告 C% = 31.3%，但 cluster bootstrap CI 为 [26.7%, 53.2%]，上界远高于 point estimate。作者如何解释这种不对称性？是否意味着某些 family 的贡献可能显著提升 C%？

**Q2**: §4.7 中 6-month window（2023-H2 vs. 2024-H1）的 C% = 34.35% 高于全年对比的 31.3%。这是否表明 DIF 主要是在特定时间点突变而非渐进积累？是否有更细粒度的 temporal analysis？

**Q3**: 论文发现 knowledge/reasoning benchmarks 的 C% 显著高于 procedural ones（26.9-31.3% vs. 17.9-18.9%）。作者是否有证据区分这是因为 knowledge items 更容易被 contaminate，还是因为这些领域的 genuine capability improvement 更大？

**Q4**: Cross-subject matching 的 ΔFPR = 0 guarantee 依赖于 contamination 局限于少数 subjects（k ≤ 5）。但如果 contamination 是 systematic 的（例如整个 training data pipeline 改变），这个 guarantee 是否就失效了？

---

## Missing References

1. **Zhao et al. (ACL 2025)** "MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark" — 直接重构 MMLU 以消除 contamination artifacts，是本文 MMLU-focused analysis 的重要对照。未引用。

2. **Engels, Lüdtke, and Robitzsch (2026)** "Estimating Trends With Differential Item Functioning: A Comparison of Five IRT-Based Approaches" (Educational and Psychological Measurement) — 直接讨论在存在 DIF 的情况下如何估计纵向趋势，方法论高度相关。未引用。

3. **Gema et al. (2024)** "Are We Done with MMLU?" — 已在 bib 中（`gema2024mmlu`）但未在 Related Work 正文中讨论。该文揭示的 MMLU ground truth errors 对本文的 DIF 分析有重要 implications。

4. **Lee, Huang, Svetina Valdivia, Schwartzman (2026)** "On the Complex Sources of Differential Item Functioning" — 讨论 DIF 的复杂来源，可能对本文的 "DIF detects that not why" 讨论有参考价值。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 694 · 2026-05-22T11:35:07.845876+00:00_

Reviewer 2 已返回。评分 3.5/5（Borderline Conference），2 个 critical（Discussion 不充分、novelty 定位不清晰），5 个 warning。等待 Reviewer 1 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 66

## Round 66

2 recorded events


### User

_source line 695 · 2026-05-22T11:35:13.123587+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿完成。报告已提交给 Review Director，核心评价：

- **Overall 3.5/5（Borderline Conference）**
- **2 个 Must-Fix**：Discussion 对于 diagnostic 定位的论文发展严重不足（因果归因框架、NLP 社区实践建议、与 benchmark reform 的联系均缺失）；与 Growing Pains 等 concurrent work 的新颖性区分不够清晰
- **5 个 Should-Fix**：Abstract 信息密度过高、术语不一致、temporal cohort 划分过粗、Gema et al. 未在正文讨论、predictive analysis negative finding 处理过简
- **4 条 Missing References**：MMLU-CF (Zhao et al., ACL 2025)、Engels et al. (2026) 趋势估计方法、Gema et al. 正文讨论、Lee et al. (2026) DIF 来源分析

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 696 · 2026-05-22T11:35:18.630210+00:00_

Reviewer 2 结果已收到。等待 Reviewer 1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 67

## Round 67

8 recorded events


### User

_source line 697 · 2026-05-22T11:36:16.055278+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 将 MH-DIF 引入 LLM benchmark 评估是新颖且重要的贡献，实验规模大、控制实验多，但多维度假设违反的讨论不充分、核心数字的统计精度被高估，需要修订后才能稳进主会议。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3 / 5 | 核心方法选择合理，控制实验丰富；但 MH-DIF 的单维度假设在 57-subject MMLU 上的适用性辩护不足，cluster bootstrap CI 跨度大却被淡化 |
| Excitement | 4 / 5 | 心理测量学方法在 LLM 评估中的首次大规模应用，填补了 item-level temporal stability 的研究空白，大概率引发后续工作 |
| Reproducibility | 4 / 5 | 使用公开的 METABENCH 数据，代码承诺开放，方法描述清晰，第三方应可复现 |
| Overall | 3.5 / 5 | Borderline Conference：idea 好、规模大，但方法论上有可修复的关键问题 |
| Confidence | 4 / 5 | 本人熟悉 DIF 方法论和 LLM 评估，对主要问题判断有把握 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] MMLU 的多维度结构违反 MH-DIF 的核心匹配假设，论文辩护不充分

- 具体位置：Section 3.2（MH 方法描述）、Appendix A.1（IRT model fit）
- 问题：MH-DIF 通过 total score 分层来"控制能力差异"，隐含假设是 total score 充分捕捉了影响 item response 的潜在特质。但 MMLU 横跨 57 个 subject、5 个 domain，Appendix A.1 自己承认 "the MMLU response matrix shows poor fit to a unidimensional 2PL model"。论文随即声称 "This does not affect MH-DIF validity, which relies only on total score stratification rather than parametric IRT assumptions"——这个论断过强且缺乏支撑。

  DIF 文献中已有充分记录：当测试是多维的，且 focal/reference group 在次要维度上存在系统性差异时，total-score matching 的 MH-DIF 会将次要维度上的能力差异误判为 DIF（Ackerman 1992; Roussos & Stout 1996）。在本文场景中，2023→2024 的 temporal cohort 涉及架构升级、训练数据扩充、RLHF 方法变革等多重变化，完全可能导致跨 subject 的能力 profile 系统性偏移（例如 2024 模型在 STEM 上相对更强而 Humanities 上持平），这种 profile shift 会在 total-score matching 下被错误地标记为 item-level DIF。

  Cross-subject matching（Section 3.4）部分缓解了这个问题（匹配变量排除了 focal item 所在 subject），但匹配变量仍然是其余 56 个 subject 的混合，仍然是多维的。

- 为什么影响接收：这直接关系到 31% DIF rate 中有多少是"真实的 item 功能变化"，多少是"跨维度能力 profile shift"的假阳性。如果不量化这个混淆，核心 claim 的可信度不足。

- 建议修改方向：
  (1) 将 within-subject DIF 分析（在每个 subject 内部用 subject-specific score 做匹配）提升为主分析或共同主分析，报告 subject-level C% 分布
  (2) 明确讨论 temporal cohort 的多维能力 profile shift 威胁模型：报告 2023 vs 2024 cohort 在各 domain 上的 accuracy 差异 profile，评估其是否足以产生 spurious DIF
  (3) 考虑用 SIBTEST 或 Crossing-SIBTEST 做补充分析，这些方法专为多维 DIF 检测设计

**N2** [critical] Cluster bootstrap CI [26.7%, 53.2%] 的巨大跨度与 "robust" 定性不一致

- 具体位置：Section 4.2, page 6
- 问题：论文的 headline finding 是 "approximately 31% of MMLU items exhibit DIF"。但 family-level cluster bootstrap 给出的 95% CI 为 [26.7%, 53.2%]，上界是下界的近 2 倍。论文将此描述为 "continuing robustness under within-family dependence"。

  一个跨度达 26.5 个百分点的置信区间意味着：在考虑 model family 依赖后，真实 DIF 率可能低至 27%，也可能高达 53%。这不是 "robust"，而是 substantial uncertainty。

  Appendix C 用 DEFF = 3.87 做了另一种校正，得到 adjusted C% = 34.55%。两种校正给出的图景不完全一致（DEFF 点估计偏高，bootstrap CI 极宽）。

- 为什么影响接收：31% 这个数字贯穿全文（abstract、introduction、conclusion 均引用），如果实际不确定性如此之大，读者对这个数字的信任会打折扣。

- 建议修改方向：
  (1) 在 abstract 和正文中报告 cluster bootstrap CI，而非仅在 Section 4.2 一笔带过
  (2) 将 "~31%" 的措辞改为 "27%–53% (cluster bootstrap 95% CI, point estimate 31%)" 或类似表述
  (3) 讨论 model-level CI 与 cluster bootstrap CI 之间的 tension，以及为何两种校正方法给出不同的精度

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Semi-synthetic injection 的生态效度有限，论文讨论不足

- 具体位置：Section 3.4, Limitations (p9)
- 问题：injection 通过 uniform binary flipping（incorrect→correct at rate $p$）模拟 contamination。真实 contamination 的表现形式远更复杂：(a) partial knowledge increase（不是 0/1 翻转，而是概率提升），(b) 对特定 answer pattern 的记忆而非底层知识，(c) 不同 item 上的 exploitation rate 差异很大（高频 item 更容易被记忆）。
- 论文在 Limitations 中承认了 "worst-case uniform exploitation pattern"，但没有讨论在更现实的 contamination 模型下 sensitivity 如何变化。Figure 2 的 dose-response 曲线和 Table 4 的 power 数据都是针对这一特定 injection 模型校准的，不能直接推广。
- 建议：至少讨论 1-2 种替代 contamination 模型（如 difficulty-dependent exploitation、partial knowledge injection），分析其对 detectability 的定性影响。

**W2** [warning] 低 exploitation rate 下功效接近零，underdetection 的含义讨论不足

- 具体位置：Table 4, Section 4.1
- 问题：Table 4 显示在 exploitation rate $\alpha = 0.05$ 时 TPR = 0.03（近乎零检测力）。即使在 $\alpha = 0.5$ 时 TPR 也仅 ~0.87。这意味着 MH-DIF 对低 exploitation rate 的 item（少于 ~20% 的模型利用了 contamination）几乎完全失明。
- 这对解读 31% 有重要含义：如果许多 item 的 exploitation rate 偏低，31% 可能是显著的低估。但论文缺少这一 framing——没有将 31% 明确定位为 DIF 的下界估计。
- 建议：(1) 在 Discussion 中明确 31% 是 lower bound；(2) 考虑做 sensitivity analysis——在不同 exploitation rate 分布假设下，估计真实 DIF 率范围。

**W3** [warning] IRT θ-conditioning 作为独立控制的有效性存疑

- 具体位置：Section 4.4, Table 2, Appendix A.1
- 问题：论文报告 $r(\theta, \text{total score}) = 0.996$。如此高的相关意味着 θ-conditioning 和 total-score matching 几乎完全等价，作为"独立控制"不提供增量信息。同时 Appendix A.1 承认 2PL model fit 很差——用 poorly-fitting model 的 θ 估计做控制本身就是一个 circular 问题。
- 建议：将 θ-conditioning 降级为 "sensitivity check" 而非 "structural control"，或者使用 MIRT 模型获取更合理的 θ 估计。

**W4** [warning] GSM1K cross-validation 相关 (Section 4.7, Figure 5) 样本量过小

- 具体位置：Section 4.7, Figure 5
- 问题：$N = 33$ 个模型上的相关分析（$r = -0.478, p = 0.005$）。这个 N 对于 correlation analysis 偏小，少数 influential outlier 可能驱动整个结果。Figure 5 散点图中似乎存在右下角的 leverage point。
- 建议：报告 influence diagnostics（Cook's D），或至少注明 N=33 的 small-sample limitation。

**W5** [warning] Multi-subject injection 下 ΔFPR 升至 0.069 对真实数据解读的影响未讨论

- 具体位置：Table 5, Section 4.5
- 问题：论文重点强调 single-subject injection 下 ΔFPR = 0.000（by construction），但 Table 5 显示同时污染 ≥10 个 subject 时 ΔFPR 升至 0.060-0.069。在真实场景中 contamination 几乎必然跨越多个 subject，因此 ΔFPR = 0 的保证不适用于实际条件。
- 如果基线 FPR ~6%（random split, Table 1）加上 injection-induced ΔFPR ~6.9%，总 FPR 可达 ~13%。这对解读真实数据中的 31% DIF rate 有何含义？其中有多少可能是 multi-subject contamination 导致的 false positive？
- 建议：在 Discussion 中讨论 multi-subject FPR inflation 对核心 finding 的 quantitative impact。

---

## 小问题（不影响接收）

1. **K 值未明确指定**：Section 3.2 描述 MH 用 "K score bins" 分层，但 K 的具体值没有在正文中报告。Appendix A.1 提到 "quintile-based binning"，请在正文中明确 K = 5（如果是的话）。

2. **Abstract 中 ρ = 0.964 可能产生误导**：Abstract 报告 DIF flags 与 web-overlap labels 的 "cohort ρ = 0.964"，粗看像是高度一致。但这里 ρ 是 item-level rank correlation（rank 保序性强但 classification overlap 低），真正反映 classification agreement 的是 Jaccard = 0.206。建议在 abstract 中优先报告 Jaccard 或重新措辞避免误读。

3. **Table 2 caption 不够清晰**：Table 2 中不同 control 对应的 "baseline C%" 含义不统一，建议在 caption 或脚注中说明每行的 baseline 定义。

4. **Limitations 段落中 causal decomposition 的提法**："A definitive causal decomposition remains out of reach without access to model training data"——这一点很重要但放在 Limitations 最后容易被忽略，建议在 Discussion (Section 5.1) 中也简要提及。

---

## 主要优势

1. **新颖且重要的 framing**：首次将教育测量学中成熟的 MH-DIF 方法引入 LLM benchmark 评估，填补了 item-level temporal stability 的空白。psychometric method → NLP evaluation 的 bridge 动机清晰、立论扎实。

2. **规模令人信服**：5,227 models × 12,508 items × 6 benchmarks。这不是 toy experiment，数据规模本身就构成了贡献。

3. **控制实验全面**：Random split baseline (6%)、matched-ability quintile、IRT θ-conditioning、within-subject pre-check、cross-subject matching——5 层控制形成了 thorough falsification battery。

4. **Cross-subject matching 设计巧妙**：用 focal item 所在 subject 以外的所有 score 做匹配变量，在 single-subject contamination 下 ΔFPR = 0 by construction。这个设计在 DIF 应用文献中是一个 methodological innovation。

5. **Cross-benchmark replication**：Table 3 展示 6 个 METABENCH benchmarks 一致呈现 DIF，且 knowledge-intensive benchmarks DIF 率更高的 gradient 符合理论预期。

6. **实用性强**：Section 5.3 提出的 monitoring protocol（15% flag / 25% act thresholds）有明确的操作性，对 benchmark maintainers 有直接参考价值。

---

## Questions for Authors

Q1: 是否考虑过在每个 subject 内部独立运行 MH-DIF（用 subject-internal score 做匹配），以避免跨 subject 的多维度混淆？如果有，subject-level C% 的分布是什么样的？

Q2: Table 2 中 matched-ability quintile 未能降低 C%——是否验证了 quintile 划分后各 stratum 内 2023/2024 cohort 的 score 分布确实匹配良好？如果某些 quintile 内仍有 residual ability difference，控制效果可能不足。

Q3: Cluster bootstrap CI [26.7%, 53.2%] 与 DEFF-adjusted C% = 34.55% 之间如何调和？两种处理 family dependence 的方法给出了不同精度的图景，哪个更可信？

Q4: 在 semi-synthetic framework 中，如果 exploitation rate 按 item difficulty 变化（例如 easy items 更容易被 exploit），dose-response 曲线和 ΔTPR 会如何变化？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-22T11:36:29.619079+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排 (2人)', 'status': 'completed', 'activeForm': '完成 Reviewer 编排决定'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '完成视觉审查派发'}, {'content': 'Step 1: Round 1 独立审稿 — 等待 Reviewer 1 & 2 返回', 'status': 'completed', 'activeForm': 'Reviewer 1 & 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见互评', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排 (2人)', 'status': 'completed', 'activeForm': '完成 Reviewer 编排决定'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '完成视觉审查派发'}, {'content': 'Step 1: Round 1 独立审稿 — 等待 Reviewer 1 & 2 返回', 'status': 'completed', 'activeForm': 'Reviewer 1 & 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见互评', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-22T11:36:29.670483+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-22T11:36:59.906110+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告：Round 1\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n## Must-Fix 问题\n\n**N1** [critical] Discussion 对于一篇 \"diagnostic\" 论文而言严重不足\n- §5 仅约半页，3 个小节\n- 缺失：因果归因框架性讨论（contamination vs capability evolution vs training methodology shifts）、对 NLP 社区实践的具体影响（benchmark maintainers / leaderboard operators / model developers 该怎么做）、与 benchmark reform 更广泛运动的联系（MMLU-CF / dynamic benchmarks / temporal DIF monitoring 定位）\n- §5.3 的 Monitor/Flag/Act 阈值（15%/25%）在主文中没展示如何从 Figure 6 推导\n\n**N2** [critical] 新颖性定位需要更清晰地与 concurrent work 区分\n- 与 Growing Pains (Habba 2026) 仅一句 \"diagnostic foundation vs prescriptive framework\"，不是 differentiation 而是 integration argument\n- Benchmark Health Index (Zhu 2026) 和 Benchmark² (Qian &amp; Huang 2026) 各一句带过\n- 缺少明确的 positioning paragraph 对比 scope/method/findings/actionable output\n\n## Should-Fix 问题\n\n**W1** [warning] Abstract 信息密度过高，15+ 数字稀释关键信息\n**W2** [warning] 术语不一致（temporal measurement instability / temporal DIF / measurement invariance）\n**W3** [warning] Temporal cohort 2023 vs 2024 划分过粗，§4.7 的 6-month window C%=34.35% 更高但未充分讨论\n**W4** [warning] Gema et al. (2024) \"Are We Done with MMLU?\" 在 bib 中但未在正文讨论，ground truth errors 可能是 DIF 的 confound\n**W5** [warning] App F 的 negative finding (AUROC=0.60) 在主文仅一句，应在 Discussion 展开\n\n## Minor\n- §5 的 \\enlargethispage*{8\\baselineskip} 激进\n- Table 2/3 resizebox 字体偏小\n- Introduction 过早引入大量数字\n- Conclusion 仅 3 行过短\n- Figure 2 caption \"≈ 0\" 应改 \"= 0\"\n- §3.2 \"LLM-specific challenges\" 段过长\n\n## Missing References\n1. Zhao et al. (ACL 2025) \"MMLU-CF\" — 未引用\n2. Engels, Lüdtke, Robitzsch (2026) 趋势估计 — 未引用\n3. Lee, Huang, Svetina Valdivia, Schwartzman (2026) DIF 来源 — 未引用\n\n---\n\n请逐条回应上述所有问题。",
  "project": "irt_equated_bench_regen",
  "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
  "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告：Round 1\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n## Must-Fix 问题\n\n**N1** [critical] Discussion 对于一篇 \"diagnostic\" 论文而言严重不足\n- §5 仅约半页，3 个小节\n- 缺失：因果归因框架性讨论（contamination vs capability evolution vs training methodology shifts）、对 NLP 社区实践的具体影响（benchmark maintainers / leaderboard operators / model developers 该怎么做）、与 benchmark reform 更广泛运动的联系（MMLU-CF / dynamic benchmarks / temporal DIF monitoring 定位）\n- §5.3 的 Monitor/Flag/Act 阈值（15%/25%）在主文中没展示如何从 Figure 6 推导\n\n**N2** [critical] 新颖性定位需要更清晰地与 concurrent work 区分\n- 与 Growing Pains (Habba 2026) 仅一句 \"diagnostic foundation vs prescriptive framework\"，不是 differentiation 而是 integration argument\n- Benchmark Health Index (Zhu 2026) 和 Benchmark² (Qian &amp; Huang 2026) 各一句带过\n- 缺少明确的 positioning paragraph 对比 scope/method/findings/actionable output\n\n## Should-Fix 问题\n\n**W1** [warning] Abstract 信息密度过高，15+ 数字稀释关键信息\n**W2** [warning] 术语不一致（temporal measurement instability / temporal DIF / measurement invariance）\n**W3** [warning] Temporal cohort 2023 vs 2024 划分过粗，§4.7 的 6-month window C%=34.35% 更高但未充分讨论\n**W4** [warning] Gema et al. (2024) \"Are We Done with MMLU?\" 在 bib 中但未在正文讨论，ground truth errors 可能是 DIF 的 confound\n**W5** [warning] App F 的 negative finding (AUROC=0.60) 在主文仅一句，应在 Discussion 展开\n\n## Minor\n- §5 的 \\enlargethispage*{8\\baselineskip} 激进\n- Table 2/3 resizebox 字体偏小\n- Introduction 过早引入大量数字\n- Conclusion 仅 3 行过短\n- Figure 2 caption \"≈ 0\" 应改 \"= 0\"\n- §3.2 \"LLM-specific challenges\" 段过长\n\n## Missing References\n1. Zhao et al. (ACL 2025) \"MMLU-CF\" — 未引用\n2. Engels, Lüdtke, Robitzsch (2026) 趋势估计 — 未引用\n3. Lee, Huang, Svetina Valdivia, Schwartzman (2026) DIF 来源 — 未引用\n\n---\n\n请逐条回应上述所有问题。",
    "project": "irt_equated_bench_regen",
    "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
    "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-22T11:37:20.539078+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20632
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-22T11:37:21.143697+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告：Round 1\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n## Must-Fix 问题\n\n**N1** [critical] MMLU 的多维度结构违反 MH-DIF 的核心匹配假设，论文辩护不充分\n- MMLU 57 subjects / 5 domains，Appendix A.1 承认 \"poor fit to unidimensional 2PL model\"\n- 论文声称 \"MH-DIF relies only on total score stratification rather than parametric IRT assumptions\"——过强\n- DIF 文献 (Ackerman 1992; Roussos &amp; Stout 1996)：多维测试 + 次要维度能力差异 → total-score matching MH-DIF 产生 spurious DIF\n- Cross-subject matching 部分缓解但匹配变量仍为 56 subjects 混合，仍多维\n- 建议：within-subject DIF 分析提升为主分析 / SIBTEST 补充 / 量化 temporal cohort 多维能力 profile shift\n\n**N2** [critical] Cluster bootstrap CI [26.7%, 53.2%] 跨度 26.5pp 与 \"robust\" 定性不一致\n- 上界是下界近 2 倍\n- Appendix C 的 DEFF=3.87 给出 adjusted C%=34.55%，与 bootstrap 图景不完全一致\n- 31% 贯穿 abstract/intro/conclusion，但实际不确定性巨大\n- 建议：abstract/正文同时报告 CI，\"~31%\" 改为 \"27-53% (cluster bootstrap 95% CI, point estimate 31%)\"\n\n## Should-Fix 问题\n\n**W1** [warning] Semi-synthetic injection 生态效度有限：uniform binary flipping 不反映 partial knowledge / difficulty-dependent exploitation / answer-pattern memorization\n**W2** [warning] Low exploitation rate (α=0.05) 下 TPR=0.03，31% 可能是显著低估，需定位为 lower bound\n**W3** [warning] IRT θ-conditioning 与 total score r=0.996，作为 \"structural control\" 不提供增量信息，应降级为 sensitivity check\n**W4** [warning] GSM1K cross-validation N=33 过小，可能有 influential outlier，需 Cook's D\n**W5** [warning] Multi-subject injection ≥10 subjects 时 ΔFPR=0.060-0.069，真实 contamination 必然跨 subject，ΔFPR=0 保证不适用实际条件\n\n## Minor\n1. K 值（MH score bins）未在正文明确\n2. Abstract 中 enrichment≈0.96 粗看像高一致，但实际 Jaccard=0.206，建议优先报告 Jaccard\n3. Table 2 caption baseline C% 含义不统一\n4. Limitations 中 causal decomposition 位置过偏，应在 §5.1 也提\n\n## Questions\nQ1: 是否做过 within-subject MH-DIF（subject-internal score 匹配）？subject-level C% 分布如何？\nQ2: Matched-ability quintile 各 stratum 内 2023/2024 score 分布是否确实匹配良好？\nQ3: Cluster bootstrap CI 与 DEFF-adjusted C% 如何调和？哪个更可信？\nQ4: Difficulty-dependent exploitation rate 下 dose-response 如何变化？\n\n---\n\n请逐条回应上述所有问题。",
  "project": "irt_equated_bench_regen",
  "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
  "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告：Round 1\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n## Must-Fix 问题\n\n**N1** [critical] MMLU 的多维度结构违反 MH-DIF 的核心匹配假设，论文辩护不充分\n- MMLU 57 subjects / 5 domains，Appendix A.1 承认 \"poor fit to unidimensional 2PL model\"\n- 论文声称 \"MH-DIF relies only on total score stratification rather than parametric IRT assumptions\"——过强\n- DIF 文献 (Ackerman 1992; Roussos &amp; Stout 1996)：多维测试 + 次要维度能力差异 → total-score matching MH-DIF 产生 spurious DIF\n- Cross-subject matching 部分缓解但匹配变量仍为 56 subjects 混合，仍多维\n- 建议：within-subject DIF 分析提升为主分析 / SIBTEST 补充 / 量化 temporal cohort 多维能力 profile shift\n\n**N2** [critical] Cluster bootstrap CI [26.7%, 53.2%] 跨度 26.5pp 与 \"robust\" 定性不一致\n- 上界是下界近 2 倍\n- Appendix C 的 DEFF=3.87 给出 adjusted C%=34.55%，与 bootstrap 图景不完全一致\n- 31% 贯穿 abstract/intro/conclusion，但实际不确定性巨大\n- 建议：abstract/正文同时报告 CI，\"~31%\" 改为 \"27-53% (cluster bootstrap 95% CI, point estimate 31%)\"\n\n## Should-Fix 问题\n\n**W1** [warning] Semi-synthetic injection 生态效度有限：uniform binary flipping 不反映 partial knowledge / difficulty-dependent exploitation / answer-pattern memorization\n**W2** [warning] Low exploitation rate (α=0.05) 下 TPR=0.03，31% 可能是显著低估，需定位为 lower bound\n**W3** [warning] IRT θ-conditioning 与 total score r=0.996，作为 \"structural control\" 不提供增量信息，应降级为 sensitivity check\n**W4** [warning] GSM1K cross-validation N=33 过小，可能有 influential outlier，需 Cook's D\n**W5** [warning] Multi-subject injection ≥10 subjects 时 ΔFPR=0.060-0.069，真实 contamination 必然跨 subject，ΔFPR=0 保证不适用实际条件\n\n## Minor\n1. K 值（MH score bins）未在正文明确\n2. Abstract 中 enrichment≈0.96 粗看像高一致，但实际 Jaccard=0.206，建议优先报告 Jaccard\n3. Table 2 caption baseline C% 含义不统一\n4. Limitations 中 causal decomposition 位置过偏，应在 §5.1 也提\n\n## Questions\nQ1: 是否做过 within-subject MH-DIF（subject-internal score 匹配）？subject-level C% 分布如何？\nQ2: Matched-ability quintile 各 stratum 内 2023/2024 score 分布是否确实匹配良好？\nQ3: Cluster bootstrap CI 与 DEFF-adjusted C% 如何调和？哪个更可信？\nQ4: Difficulty-dependent exploitation rate 下 dose-response 如何变化？\n\n---\n\n请逐条回应上述所有问题。",
    "project": "irt_equated_bench_regen",
    "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
    "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-22T11:37:22.715931+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1572
}
```

</details>

---


### Assistant

_source line 704 · 2026-05-22T11:37:25.873530+00:00_

交叉分享已派发。Reviewer 1 收到 Reviewer 2 的完整审稿意见，Reviewer 2 收到 Reviewer 1 的完整审稿意见，各自逐条回应中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 68

## Round 68

2 recorded events


### User

_source line 705 · 2026-05-22T11:37:28.542521+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**总结**：Overall 3.5（Borderline Conference）。主要发现：

- **2 个 Must-Fix**：(N1) MMLU 57-subject 多维度结构违反 MH-DIF 匹配假设，论文对此辩护不足——temporal cohort 的能力 profile shift 可能产生 spurious DIF；(N2) cluster bootstrap CI [26.7%, 53.2%] 跨度极大，但论文用 "robust" 淡化处理，headline 数字 "31%" 的精度被高估。
- **5 个 Should-Fix**：semi-synthetic injection 生态效度有限；低 exploitation rate 下 power 接近零但未讨论 underdetection 含义；IRT θ-conditioning 与 total score 相关 0.996 不构成独立控制；GSM1K cross-validation N=33 过小；multi-subject injection ΔFPR 升至 0.069 对真实数据的影响未讨论。
- **主要优势**：首次大规模 psychometric audit、5 层控制实验、cross-subject matching 方法创新、6 benchmarks 交叉验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 706 · 2026-05-22T11:37:33.531247+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 69

## Round 69

2 recorded events


### User

_source line 707 · 2026-05-22T11:39:10.144643+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 Round 1 意见的逐条回应

---

### Must-Fix

**[AGREE with downgrade] R2-N1: Discussion 不足**

同意 Discussion 可以更充实，但不同意 "critical" 定级——应为 Should-Fix。理由：

1. §5.1 已经给出了因果归因的三分框架："impact (ability differences removed by matching, ~2.4 pp), DIF (item-level differences after ability control, ~38-29% floor, predominantly item-specific), and attribution (contamination, capability change, or training methodology shifts—underdetermined without training data)"（p8）。R2 说 "缺失因果归因框架" 不完全准确，§5.1 有这个骨架，但确实展开不够。

2. §5.3 的 15%/25% 阈值在 Figure 6 中有视觉推导依据——vertical dashed lines 标注了 Monitor/Flag (15%) 和 Flag/Act (25%) 位置，对应 DIF-ordered removal 开始显著加速 ranking degradation 的拐点。但同意正文应更显式地写出推导逻辑（"at 15% removal, ρ drops below X"）。

3. 对于一篇 8 页正文的实证论文，~半页 Discussion 虽然偏短但不至于 "critical"。更大的问题是 Conclusion 仅 3 行（R2 Minor 中也提到）——建议将部分 Discussion 要点移入 Conclusion 以改善收尾。

**结论**：同意需要扩展 Discussion（特别是 actionable implications 和 threshold 推导），但建议降级为 Should-Fix。

---

**[REBUT] R2-N2: 新颖性定位需要更清晰地与 concurrent work 区分**

不同意 "critical" 定级。理由：

1. 本文的方法论贡献与 R2 列举的 concurrent work 在 level 上不同。Growing Pains (Habba 2026) 是 prescriptive equating framework；Benchmark Health Index (Zhu 2026) 是 composite metric；Benchmark² (Qian & Huang 2026) 是 meta-evaluation。本文的贡献是将 **已有 50+ 年历史的标准化心理测量方法（MH-DIF + ETS classification）** 首次大规模应用于 LLM benchmarks。这不是与 concurrent work "竞争" 的关系，而是提供了一个 complementary diagnostic lens。Section 2 (Related Work) 的 "IRT in LLM Evaluation" 段落明确定位了这一点："The closest concurrent work is Growing Pains (Habba et al., 2026), which uses IRT calibration to establish anchor items for cross-temporal score equating"。

2. 方法的可区分性不需要长段落论述——MH-DIF 是一个具体的、可引用的、有 ETS 标准化分类体系的方法。读者不会混淆 "DIF analysis" 和 "benchmark health index"。

3. 更实质的区分在于 **scale**（5,227 models × 12,508 items）和 **validation methodology**（semi-synthetic injection + cross-subject matching），这些在 Section 1 的 contributions 中已经明确。

**结论**：一个简短的 positioning paragraph 可以锦上添花（Should-Fix 甚至 Minor），但不应作为 Must-Fix。论文的方法论独特性足够清晰。

---

### Should-Fix

**[AGREE] R2-W1: Abstract 信息密度过高**

同意。我在 R1 审稿中也注意到了类似问题——Abstract 中 ρ = 0.964 容易被误读为高一致性（实际 Jaccard = 0.206 才反映 classification agreement）。15+ 个数字确实稀释了关键信息。建议 Abstract 只保留 3-4 个核心数字（31% C rate, cross-benchmark range 17.9-31.3%, ΔFPR = 0.000, N = 5,227 models），其余移入 Introduction。

**[AGREE] R2-W2: 术语不一致**

同意。论文混用 "temporal measurement instability"、"temporal DIF"、"measurement invariance" 而未明确层级关系。建议在 §1 或 §3 开头建立术语层次：measurement invariance 是目标属性，DIF 是检测方法，temporal measurement instability 是本文发现的现象。

**[AGREE with nuance] R2-W3: Temporal cohort 划分过粗，6-month window C% 更高**

同意 6-month window (C% = 34.35%, Table 1) 高于年度划分 (31%) 值得更多讨论。但我认为这个发现**加强**而非削弱论文的 claim——更窄的时间窗口反而检出更高的 DIF rate，说明年度划分可能是保守估计。论文应在 §4.2 中明确讨论这个 gradient 并解释其含义（temporal proximity → stronger DIF signal，因为短期内模型训练方法变化更集中？）。

补充一点我在 R1 中提出的相关担忧：更根本的问题不是粒度，而是 temporal cohort 划分 confound 了多个变量（architecture, training data, scale, alignment methods）。粗细划分都无法解决这个 confound，只有 causal decomposition 才能。

**[AGREE] R2-W4: Gema et al. (2024) ground truth errors 作为 confound**

强烈同意。这是一个我在 R1 中遗漏的重要 confound。如果 MMLU 本身存在 ground truth errors（wrong answer keys），更强的 2024 模型可能因为"知道真正的正确答案"而选择了与 key 不同的选项，这在 MH-DIF 中会被标记为 DIF——但原因是 benchmark 质量问题而非 contamination 或 measurement instability。

论文的 bib 中有 Gema et al. (2024) 但正文未讨论这个 confound。这与我在 R1-N1 中提出的多维度问题一起，构成了对 31% DIF rate 解读的另一个替代解释。

建议：(1) 在 §4 或 §5 中讨论 ground truth error confound；(2) 如果可以获取 Gema et al. 标注的有问题 items，检查这些 items 与 DIF-flagged items 的 overlap。

**[AGREE with nuance] R2-W5: App F negative finding 讨论不足**

部分同意。AUROC = 0.60 是一个重要的 negative finding（item properties 不能 reliably predict DIF susceptibility），值得在主文中多说一两句。但考虑到 8 页限制，一句提及 + Appendix 详述是可接受的安排。建议在 §5.1 中加一句解释这个 negative finding 的含义（"DIF susceptibility is not a fixed item property but may depend on the interaction between item characteristics and training methodology shifts"）。

---

### Minor

**[AGREE] \enlargethispage hack**：§5 的 `\enlargethispage*{8\baselineskip}` 确实激进，可能导致不同编译环境下页面溢出。应通过精简文字解决而非用 LaTeX hack。

**[AGREE] Table font size**：Table 2/3 的 resizebox 字体偏小，影响可读性。建议拆分或用 landscape 排列。

**[AGREE] Introduction 数字过多**：与 W1 一致，信息前置过多。

**[AGREE] Conclusion 过短**：3 行确实不够。Conclusion 应至少 recap 核心发现、讨论 broader impact、指出 future work 方向。

**[REBUT] Figure 2 caption "≈ 0" vs "= 0"**：在 single-subject injection 下 ΔFPR = 0 是 by construction（Section 3.4 有理论证明），但 caption 中 "≈ 0" 反映的可能是 empirical measurement（受 finite sample noise 影响）。如果 bootstrap CI 是 [0.000, 0.000]，则 "= 0" 更准确；如果有任何非零 replication，"≈ 0" 更诚实。需要看具体数据决定。

**[AGREE] §3.2 段落过长**：可以拆分为 sub-points 或移部分到 Appendix。

---

### Missing References

**[AGREE] MMLU-CF (Zhao et al., ACL 2025)**：高度相关——MMLU-CF 直接处理 MMLU item 质量问题（contamination-free subset），应被引用并讨论。特别是：如果将 DIF analysis 限制在 MMLU-CF 的 clean items 上，DIF rate 是否下降？这能帮助区分 ground truth error confound。

**[NEUTRAL] Engels, Lüdtke, Robitzsch (2026) 和 Lee, Huang, Svetina Valdivia, Schwartzman (2026)**：如果这两篇确实是 DIF/measurement invariance 方法论的最新进展，引用可以加强论文的心理测量学基础。但我未看到这两篇的具体内容，无法判断是否 essential。建议 authors 评估相关性后决定。

---

### 总结性评价

R2 的审稿整体质量良好，尤其是 W4（ground truth error confound）是我在 R1 中遗漏的重要观点。但 N1 和 N2 的 "critical" 定级偏高——Discussion 篇幅和 novelty positioning 对于一篇 8 页实证论文而言是 presentation 问题而非 soundness 问题，不应阻碍接收。建议将两者降级为 Should-Fix。

R2 的审稿侧重 presentation 和 positioning，与我的 R1 审稿侧重统计方法论和实验设计形成互补。综合两份审稿，论文的主要风险是：
1. **方法论**（我的 R1-N1/N2）：multidimensionality assumption + cluster CI precision
2. **Confound**（R2-W4 + 我的补充）：ground truth errors
3. **Presentation**（R2-N1/W1/W2）：Discussion 不足 + 信息过密 + 术语不一致

如果 authors 能在 revision 中 (a) 加强多维度假设的辩护、(b) 讨论 ground truth error confound、(c) 扩展 Discussion，论文可以达到 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 708 · 2026-05-22T11:39:17.001734+00:00_

Reviewer 1 完成交叉回应。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 70

## Round 70

2 recorded events


### User

_source line 709 · 2026-05-22T11:39:19.611852+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。逐条回应了 R2 的全部 Must-Fix (2)、Should-Fix (5)、Minor (6)、Missing References (3) 共 16 个问题，每条标注了 [AGREE]、[AGREE with downgrade/nuance]、[REBUT] 或 [NEUTRAL]，均附具体 Section/Table/Figure 证据。

核心判断：
- R2-N1 (Discussion 不足) 和 R2-N2 (novelty positioning) 建议从 Must-Fix 降级为 Should-Fix——这是 presentation 问题而非 soundness 问题
- R2-W4 (ground truth error confound) 是我 R1 审稿中遗漏的重要观点，强烈同意
- 综合两份审稿，论文主要风险集中在多维度假设辩护、ground truth error confound、和 Discussion 充实度三个方面

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 710 · 2026-05-22T11:39:25.906538+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 71

## Round 71

18 recorded events


### User

_source line 711 · 2026-05-22T11:39:35.926052+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 Round 1 意见的逐条回应

---

## Must-Fix 问题

### R1-N1: MMLU 多维度结构违反 MH-DIF 匹配假设

[AGREE] 部分同意——多维度性是 MH-DIF 应用于 MMLU 的最根本方法论挑战，论文的辩护确实不够充分。

**同意的部分**：R1 引用的 Ackerman (1992) / Roussos & Stout (1996) 文献确实表明，当 focal/reference group 在 secondary dimension 上存在能力差异时，total-score matching 会产生 spurious DIF。MMLU 57 subjects 跨越 5 domains，Appendix A.1 承认 poor unidimensional 2PL fit。论文声称 "MH-DIF relies only on total score stratification rather than parametric IRT assumptions"（§3.2）确实过强——MH 不需要 parametric IRT model，但仍需要 matching variable 能有效 condition out ability differences，多维结构下 total score 无法完美做到这一点。

**论文已有但不充分的辩护**：
- Cross-subject matching（§3.2）用 56 subjects 的总分匹配，排除了 target subject，但 R1 正确指出这仍然是多维的。
- Within-subject DIF（§4.4, Table 1）给出 C% = 38.1%，*高于*而非低于 cross-subject 的 31.3%。论文将此归因于 local dependence（Q3 > 0.20 的 item pairs：within-subject 11.3% vs. cross-subject 2.2%，§4.4），认为 cross-subject 是更保守的估计。这个逻辑合理但不完整——within-subject 的高 C% 也可能反映了去除多维干扰后的真实 item-level instability。
- 论文没有量化 temporal cohort 在各维度上的能力 profile shift，这是 R1 建议中最关键的一点。

**不完全同意的部分**：R1 建议将 within-subject DIF 提升为主分析。但 within-subject DIF 本身有严重的 local dependence 问题（§4.4 已文档化），且 within-subject 的 C% 更高而非更低，意味着即使多维度是问题，它可能导致 cross-subject C% *低估*而非高估真实 DIF 率。SIBTEST 补充是好建议，但对于一篇已经 8 页的论文可能 scope 过大。

**结论**：论文应（1）明确承认多维度 matching 的局限性而非回避，（2）量化 2023/2024 cohort 在 domain-level 的能力 profile 差异（域间方差分析即可），（3）讨论如果多维度导致 spurious DIF，预期方向是高估还是低估。

---

### R1-N2: Cluster bootstrap CI [26.7%, 53.2%] 与 "robust" 定性不一致

[AGREE] 基本同意——CI 宽度应在 abstract/正文中透明报告，不能只报 point estimate。

**同意的部分**：26.5pp 的 CI 跨度确实与论文全文反复使用的 "31%" 和 "approximately 31%" 的精确感不匹配。Abstract 中 "we find 17.9–31.3% of items exhibit large temporal DIF (ETS C; family-level cluster bootstrap CI [26.7%, 53.2%])" 虽然包含了 CI，但被嵌入了一个信息过载的句子中，读者很容易只记住 "31%"。Conclusion（§6）只说 "17.9–31.3% of items exhibit temporal instability (cluster bootstrap CI [26.7%, 53.2%])"，没有足够强调不确定性。

**补充观点**：
- R1 指出 Appendix C 的 DEFF adjusted C% = 29.2%（simple mean）或 13.5%（weighted mean），与 bootstrap CI 的 lower bound 26.7% 有张力。这三个 uncertainty estimate（model-level bootstrap [29.4%, 38.1%]、family-level cluster bootstrap [26.7%, 53.2%]、DEFF [13.5%, 29.2%]）给出的 picture 不一致，论文没有系统讨论哪个最合适。
- 但 R1 的建议 "改为 27-53%" 也有问题——这个 CI 的宽度部分是因为 LLM families 是 cohort-specific（no family spans both 2023 and 2024，§Limitations），family-level resampling 同时改变了 reference/focal composition，不纯粹反映 statistical uncertainty。论文在 Limitations 中提到了这一点但过于简略。

**结论**：论文应（1）在 abstract/conclusion 中将 CI 与 point estimate 同等突出，（2）在 Discussion 或 Appendix 中系统对比三种 uncertainty quantification 的假设和适用性，（3）明确说明 cluster bootstrap CI 的 upward bias 来源。

---

## Should-Fix 问题

### R1-W1: Semi-synthetic injection 生态效度有限

[AGREE] 同意。论文 Limitations § 已承认 "Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages; detection power under such realistic patterns is untested"。Uniform binary flipping 是 worst-case pattern，不反映真实 contamination 的 graded nature（如 partial knowledge 导致的 difficulty-dependent exploitation）。§3.4 将 ΔTPR 定位为 "upper-bound estimate" 是诚实的，但论文应更明确地说明这限制了从 semi-synthetic validation 到真实场景的 generalizability。

补充：R1 提到 difficulty-dependent exploitation 是一个很有 insight 的点。§4.2 已发现 difficulty-direction interaction（ρ = -0.597：hard items gain, easy items erode），这暗示真实 contamination pattern 确实与 difficulty 相关，uniform flipping 可能高估或低估不同 difficulty 水平的检测能力。

---

### R1-W2: Low exploitation rate 下 TPR 极低，31% 可能是显著低估

[REBUT] 部分不同意——这里混淆了两个不同的 claim。

论文的 31% 是直接对 actual data 应用 MH-DIF 的 observed C%，不是基于 semi-synthetic detection rate 的估计。Semi-synthetic framework 验证的是方法的 sensitivity，不是用来估计真实 DIF 率的。即使在低 exploitation rate 下 TPR 很低，也只说明 MH-DIF 可能 miss 一些 mild DIF items，不影响已检测到的 31% 的可靠性。

但 R1 暗含的论点有道理：如果 mild DIF（|Δ_MH| < 1.5）items 大量存在，真正有某种程度 temporal instability 的 items 可能远超 31%。论文的 threshold sensitivity analysis（§4.2：|Δ_MH| ≥ 2.0 时 18.3%，≥ 2.5 时 10.2%）只报告了更严格阈值下的数字，没有报告更宽松阈值（如 |Δ_MH| ≥ 1.0，即 ETS B+C）下的 rates。补充这个数据会有助于读者理解 DIF 严重程度的完整分布。

**结论**：论文无需将 31% 改称为 "lower bound"，但应补充 ETS B+C 的总 rate 以展示完整 picture。

---

### R1-W3: IRT θ-conditioning 与 total score r=0.9986 不提供增量信息

[AGREE] 同意。§4.4 / Table 2 报告 θ-conditioning 后 C% = 0.312 vs. baseline 0.313，差异微不足道。r = 0.9986 的相关性说明两种 matching variable 几乎完全等价。将其定位为 "structural control" 确实过强——它是一个 sensitivity check，确认了 total score stratification 的有效性，但不是独立的 evidence against alternative explanations。降级表述即可。

---

### R1-W4: GSM1K N=33 过小

[AGREE] 同意。论文自己在 Limitations § 称其为 "exploratory" with "limited statistical power"（§Limitations）。r = -0.478 at N=33 的 p = 0.005 看似显著，但单个 influential outlier 就可能翻转结果。Cook's D 分析是合理要求。不过考虑到论文已将其定位为 exploratory，且放在 Appendix（Figure 5），这不应是 must-fix。

---

### R1-W5: Multi-subject injection 时 ΔFPR 保证不适用实际条件

[AGREE] 部分同意。Table 5（Appendix B）确认 k = 10 时 ΔFPR = 0.047 ± 0.022，k = 20 时 0.069 ± 0.018。如果真实 contamination 跨越大量 subjects，cross-subject matching 的 FPR 控制会退化。

但需要区分两个问题：（1）semi-synthetic framework validation 中的 FPR 控制——确实受限于 k ≤ 5 条件；（2）observed C% = 31% 的可靠性——即使 matching variable 有轻微 contamination leakage，random-split control（C% = 0.18%）仍提供了 strong baseline，31% 远远超出任何合理的 FPR inflation 范围。

**结论**：论文应更明确地讨论 ΔFPR = 0 guarantee 的 boundary conditions 在主文中（目前只在 §3.4 简短提到 k ≤ 5 条件），而非仅在 Appendix/Limitations。

---

## Minor 问题

### R1-Minor-1: K 值未在正文明确

[REBUT] 不同意。§3.2 明确写道 "We use K = 5 equiprobable strata (quintile-based binning) following ETS recommended practice"。K 值已在方法论核心段落中定义。

### R1-Minor-2: Abstract 中 enrichment ≈ 0.96 容易误导

[AGREE] 同意。Enrichment ratio ≈ 1.0 在 psychometric 语境下意味着独立性，但 NLP 读者可能直觉理解为 "96% 一致"。建议 Abstract 优先报 Jaccard = 0.206 或 φ = 0.012，这两个指标对 NLP 读者更直观。

### R1-Minor-3: Table 2 caption baseline C% 含义不统一

[AGREE] 轻微同意。Table 2 的 "Reference" 行标注 C% = 0.314±.009，其他行标注方式不同（"~0.31"、"0.312"、"38.1%"），统一为相同精度会提高可读性。

### R1-Minor-4: Causal decomposition 应在 §5.1 也提

[AGREE] 同意。这与我自己的 N1 意见（Discussion 不充分）一致。Causal decomposition 的讨论不应只出现在 Limitations，§5.1 讨论 temporal comparability implications 时就应系统展开。

---

## Questions 回应

### R1-Q1: Within-subject MH-DIF 结果

论文已做且已报告：§4.4 / Table 1 报告 within-subject 平均 C% = 38.1%。§4.2 报告 57 subjects 的 C% range = 20.7%–48.4%（mean ≈ 30%）。但 within-subject 和 cross-subject 的 subject-level C% 分布的完整对比确实缺失——如果能在 Appendix 中提供 57 subjects 的 C% scatter plot（within-subject vs. cross-subject）会更有说服力。

### R1-Q2: Matched-ability quintile 内的 score 分布匹配质量

§4.2 报告了整体 Cohen's d = -0.17（76.4% overlap）和 1:1 nearest-neighbor matching 后 C% = 28.9% ± 0.1%。但 quintile 内的分布匹配质量没有单独报告——这是合理的要求，因为 MH 的有效性依赖于 stratum 内的匹配质量。

### R1-Q3: Cluster bootstrap CI 与 DEFF-adjusted C% 如何调和

这是论文的一个真正弱点。三个 estimate 给出不同 picture：
- Model-level bootstrap: [29.4%, 38.1%]
- Family-level cluster bootstrap: [26.7%, 53.2%]
- DEFF (simple mean m̄=62.8): adjusted C% = 29.2%
- DEFF (weighted mean m̄=254.5): adjusted C% = 13.5%

论文没有系统讨论哪个最合适。我认为 DEFF weighted mean 的 m̄=254.5 过于保守（因为少数大家族主导了加权），而 cluster bootstrap 的上界 53.2% 被 cohort-specific family structure 推高（Limitations § 有提及）。最合理的 range 可能是 DEFF simple mean（29.2%）到 cluster bootstrap point estimate（31.3%），但这需要作者明确论证。

### R1-Q4: Difficulty-dependent exploitation rate 下 dose-response

论文未做此实验。这是 R1-W1（生态效度）的自然延伸。如果 exploitation rate 与 item difficulty 负相关（hard items 更容易被 exploit），dose-response curve 的形状可能显著不同。这是一个 fair question，属于 future work。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-22T11:40:05.083122+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-0.7: 资料检查 + Venue + 编排 + 视觉审查', 'status': 'completed', 'activeForm': '完成初始化'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '完成交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-0.7: 资料检查 + Venue + 编排 + 视觉审查', 'status': 'completed', 'activeForm': '完成初始化'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '完成交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-22T11:40:05.134025+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 714 · 2026-05-22T11:40:13.541386+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-22T11:40:13.593247+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T11:28:54.486478+00:00\", \"completed_at\": \"2026-05-22T11:31:25.701043+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-6\", \"message\": \"连续 4 页几乎纯文本（Related Work → Method → Experiments 开头），仅 page 4 有一个公式打断。Display items 全部集中在 page 7-8，造成前松后紧的节奏失衡。建议在 Method 部分（page 4-5）插入一个流程图或 pipeline 示意图，或将 Table 1/Table 2 提前至 Method 段以改善视觉节奏。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"单页堆叠 3 个 display items（Table 1 + Figure 2 + Table 2），视觉过于拥挤，与前 4 页的空旷形成强烈反差。审稿人会感觉结果\\\"突然涌来\\\"。建议将 Table 2 移至 page 8 或调整 float 位置分散密度。\"}, {\"severity\": \"warning\", \"dimension\": \"page 15\", \"message\": \"Figure 5 caption 与 Figure 6 之间有约 1/4 页空白，末页 Figure 6 caption 下方也有约 1/5 页空白。Appendix 末页利用率偏低，但不影响主文评价。\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"Figure 6 的 6 子面板轴标签和 tick label 字号偏小（目测 ~6pt），在正常阅读距离下辨认吃力。建议增大 axis label 至 ≥8pt 或减少子面板数量。\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"Figure 5 散点图 legend 字号偏小，模型家族名称需要仔细辨认。建议适当增大 legend 字号或将 legend 移至图外。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 作为首个 display item 出现在第 2 页，位置合理。ICC 曲线示意图有效传达了 global vs differential contamination 的核心概念，Title-Abstract-Figure 1 叙事一致。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主文 8 页包含 5 个 display items（1 figure + 4 tables），密度 0.63/页。对于方法论+实证混合型论文偏低但可接受；核心结果主要通过文字传达，审稿人可能希望看到更多可视化（如 DIF 率分布图或模型排名变化图）。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title / Author / Abstract 排版整洁专业，无拥挤感。Anonymous ACL submission 标注正确。\"}, {\"severity\": \"info\", \"dimension\": \"pages 7-8\", \"message\": \"所有表格均使用 booktabs 风格（\\\\toprule/\\\\midrule/\\\\bottomrule），无竖线，格式规范。最优值有加粗标注。小数位数一致。\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-11\", \"message\": \"参考文献格式统一，无 [?] 未解析引用，无溢出。编号连续。\"}, {\"severity\": \"info\", \"dimension\"
…[truncated 214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-22T11:40:13.645864+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-22T11:40:13.696564+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-22T11:40:44.251510+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-0.7: 资料检查 + Venue + 编排 + 视觉审查', 'status': 'completed', 'activeForm': '完成初始化'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '完成交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '完成收敛判断，无需第2轮'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'in_progress', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-0.7: 资料检查 + Venue + 编排 + 视觉审查', 'status': 'completed', 'activeForm': '完成初始化'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '完成交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '完成收敛判断，无需第2轮'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'in_progress', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-22T11:40:44.302398+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-22T11:42:49.206256+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Round 14 (Fresh review, 2026-05-22)\n# 2 critical open, 9 warning open, 5 info open\n\n# ============================================================\n# ROUND 14 — MUST-FIX (CRITICAL)\n# ============================================================\n\n- id: \"R14-MF1\"\n  summary: \"MMLU 57-subject 多维度结构违反 MH-DIF 匹配假设，辩护不充分\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 首提 Must-Fix, R2 AGREE。Ackerman 1992 / Roussos & Stout 1996: 多维测试 + secondary dimension 能力差异 → spurious DIF。论文声称 MH 不依赖 parametric IRT 过强。Cross-subject matching 仍多维（56 subjects 混合）。Within-subject C%=38.1% 高于 cross-subject 31.3%，但可能反映 local dependence 而非纯 DIF。缺少 temporal cohort domain-level ability profile shift 量化。\"\n  action_items:\n    - round: 14\n      action: \"明确承认多维度 matching 局限；量化 2023/2024 cohort domain-level 能力 profile 差异；讨论 spurious DIF 预期方向（高估 vs 低估）\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-MF2\"\n  summary: \"Cluster bootstrap CI [26.7%, 53.2%] 跨度极大但被 '~31%' 淡化，三种 uncertainty estimate 不一致\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 首提 Must-Fix, R2 AGREE。Model-level [29.4%, 38.1%] vs cluster bootstrap [26.7%, 53.2%] vs DEFF simple 29.2% vs DEFF weighted 13.5%。论文全文反复用 '31%' 但 CI 嵌入信息过载句子中，上界 53.2% 被 cohort-specific family structure 推高。\"\n  action_items:\n    - round: 14\n      action: \"Abstract/conclusion 同等突出 CI；Discussion 或 Appendix 系统对比三种 uncertainty quantification 的假设和适用性；明确说明 cluster bootstrap CI upward bias 来源\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 14 — SHOULD-FIX (WARNING)\n# ============================================================\n\n- id: \"R14-SF1\"\n  summary: \"Discussion (§5) 对 diagnostic 定位论文严重不足——缺因果归因框架、NLP 实践建议、benchmark reform 联系\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 定 Must-Fix, R1 降级 Should-Fix (presentation 非 soundness)。Director 裁定 Should-Fix。§5 仅半页 3 小节。§5.3 Monitor/Flag/Act 阈值推导不透明。Conclusion 仅 3 行。\"\n  action_items:\n    - round: 14\n      action: \"扩展 Discussion 至 ~1 页：因果假说系统讨论、Monitor/Flag/Act 阈值推导逻辑、与 benchmark reform 运动定位；扩展 Conclusion\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF2\"\n  summary: \"新颖性定位——与 Growing Pains / BHI / Benchmark² 等 concurrent work 区分不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 定 Must-Fix, R1 REBUT (方法论独特性足够)。Director 裁定 Should-Fix。§2 仅一句 'diagnostic foundation vs prescriptive framework'，BHI/Benchmark² 各一句带过。\"\n  action_items:\n    - round: 14\n      action: \"Introduction 或 Related Work 增加 positioning paragraph，对比 scope/method/findings/actionable output\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF3\"\n  summary: \"Abstract 信息密度过高，15+ 数字稀释关键信息\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"共识。建议保留 3-4 核心数字，enrichment≈0.96 改报 Jaccard=0.206。\"\n  action_items:\n    - round: 14\n      action: \"Abstract 重构：问题→核心发现→3-4 关键数字→implication；enrichment 改报 Jaccard\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF4\"\n  summary: \"术语不一致：temporal measurement instability / temporal DIF / measurement invariance 混用\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"共识。建议 §1/§3 建立术语层次：measurement invariance (目标) → DIF (检测方法) → temporal measurement instability (现象)。\"\n  action_items:\n    - round: 14\n      action: \"§1 或 §3 定义术语层次，全文统一\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF5\"\n  summary: \"Gema et al. (2024) MMLU ground truth errors 作为 DIF confound 未讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 首提, R1 强烈同意（称自己遗漏）。Bib 中有 gema2024mmlu 但正文未讨论。Wrong answer keys → 2024 models 选真正正确答案 → spurious DIF。\"\n  action_items:\n    - round: 14\n      action: \"§4 或 §5 讨论 ground truth error confound；如可行检查 Gema et al. flagged items 与 DIF items 的 overlap\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF6\"\n  summary: \"Semi-synthetic injection 生态效度有限——uniform binary flipping 不反映真实 contamination\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"共识。Limitations 已承认 worst-case uniform，但缺 difficulty-dependent / partial knowledge 替代模型讨论。§4.2 difficulty-direction interaction (ρ=-0.597) 暗示真实 contamination 与 difficulty 相关。\"\n  action_items:\n    - round: 14\n      action: \"讨论 1-2 种替代 contamination 模型（difficulty-dependent, partial knowledge）的定性影响\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF7\"\n  summary: \"IRT θ-conditioning (r=0.996 with total score) 不构成独立控制，应降级为 sensitivity check\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"共识。C%=0.312 vs 0.313，差异微不足道。称 'structural control' 过强。\"\n  action_items:\n    - round: 14\n      action: \"将 θ-conditioning 重新定位为 sensitivity check\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF8\"\n  summary: \"Multi-subject injection ΔFPR=0.060-0.069 (k≥10) 对真实数据 31% 的影响未讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 首提, R2 部分同意。ΔFPR=0 guarantee 仅限 k≤5，真实 contamination 必然跨多 subject。但 R2 指出 random-split C%=0.18% 仍提供 strong baseline。\"\n  action_items:\n    - round: 14\n      action: \"主文讨论 ΔFPR=0 保证的 boundary conditions (k≤5) 及 multi-subject FPR inflation 的 quantitative impact\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF9\"\n  summary: \"GSM1K cross-validation N=33 过小，需 influence diagnostics\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"共识。r=-0.478, p=0.005 but N=33。论文已定位 exploratory，但需 Cook's D 或注明 small-sample limitation。\"\n  action_items:\n    - round: 14\n      action: \"报告 influence diagnostics (Cook's D) 或注明 small-sample caveat\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 14 — INFO\n# ============================================================\n\n- id: \"R14-I1\"\n  summary: \"App F negative finding (AUROC=0.60) 在主文仅一句，可在 Discussion 展开\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [2]\n      note: \"R2 Should-Fix, R1 同意但认为 8 页限制下一句+Appendix 可接受。Director 降为 info。\"\n\n- id: \"R14-I2\"\n  summary: \"Temporal cohort 划分过粗 (2023 vs 2024)，6-month window C%=34.35% 更高但未充分讨论\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix, R1 同意但认为更窄窗口→更高 C% 加强而非削弱 claim。根本问题是多变量 confound 非粒度。\"\n\n- id: \"R14-I3\"\n  summary: \"Low exploitation rate (α=0.05) TPR=0.03，应补充 ETS B+C rate 展示完整分布\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix (31% 是 lower bound), R2 REBUT (31% 是 observed 非 estimated)。共识：补充 ETS B+C rate 更有价值。\"\n\n- id: \"R14-I4\"\n  summary: \"Missing references: MMLU-CF (Zhao et al. ACL 2025), Engels et al. (2026), Lee et al. (2026)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"MMLU-CF 共识必引；Engels/Lee R1 neutral，建议 authors 评估。\"\n\n- id: \"R14-I5\"\n  summary: \"排版细节：§5 enlargethispage hack、Table 2/3 字体偏小、Conclusion 仅 3 行、K=5 正文声明有争议\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"多项排版和呈现细节，见 Detailed Comments。\"\n\n# ============================================================\n# PRIOR RESOLVED (carried from Round 13, no change)\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"Permutation null 已补充到 §4.2\"\n  resolution_round: 8\n\n- id: \"R8-MF2\"\n  summary: \"'Drift' framing 超出数据支撑\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Title 改为 'Temporal Measurement Instability'\"\n  resolution_round: 9\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%\"\n  resolution_round: 4\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 practical significance paradox\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 11\n  resolution: \"Family-level profiles + pairwise flip rate + 'diagnostic not destructive' framing\"\n  resolution_round: 11\n\n- id: \"R8-SF1\"\n  summary: \"Proposition 1 过度形式化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"降格为 Remark（§3.4）\"\n  resolution_round: 9\n\n- id: \"R9-W2\"\n  summary: \"方法新颖性有限\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"§3.2 引用先驱方法 + LLM-specific adaptation\"\n  resolution_round: 10\n\n- id: \"R10-W1\"\n  summary: \"LLM examinee 非独立性对统计推断的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Cluster bootstrap CI + LOFO Table 6\"\n  resolution_round: 12\n\n- id: \"R5-N1\"\n  summary: \"ΔTPR 应标注为 upper-bound estimate\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 11\n  resolution: \"Abstract/§3.4/§4.5 均标注 worst-case uniform injection\"\n  resolution_round: 10\n\n- id: \"R9-W3\"\n  summary: \"\\\\enlargethispage 过于激进\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"从 18→6→2\"\n  resolution_round: 12\n\n- id: \"R11-W1\"\n  summary: \"页数超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§5.3 压缩 + Conclusion 在 page 8 内\"\n  resolution_round: 12\n\n- id: \"R1-W1\"\n  summary: \"§5.3 audit protocol causal framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 11\n  resolution: \"改为 'review flagged items for differential-performance-associated content characteristics'\"\n  resolution_round: 12\n\n- id: \"R11-W2\"\n  summary: \"ΔFPR=0.000 缺 single-subject 限定\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Contribution 2 加 'under single-subject contamination'\"\n  resolution_round: 12\n\n- id: \"R11-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"删除 φ=0.012、ΔFPR<0.01 for k≤5、45-174×\"\n  resolution_round: 12\n\n- id: \"R11-W4\"\n  summary: \"Table 1 'FPR (clean)' 术语矛盾\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"列名改为 'C% (web-clean)'\"\n  resolution_round: 12\n\n- id: \"R11-W5\"\n  summary: \"Family-level cluster bootstrap CI 应在正文报告\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§4.2 加 family-level CI + LOFO\"\n  resolution_round: 12\n\n- id: \"R11-W6\"\n  summary: \"新颖性定位需区分 LLM adaptation\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§3.2 加三种 matching 策略区分\"\n  resolution_round: 12\n\n- id: \"R11-W7\"\n  summary: \"Semi-synthetic ecological validity 有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Limitations 覆盖\"\n  resolution_round: 12\n\n- id: \"R11-W8\"\n  summary: \"Graduated de-duplication 解读偏乐观\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"改为 'reduces C% moderately (confounded with power reduction)'\"\n  resolution_round: 12\n\n- id: \"R11-I3\"\n  summary: \"'200 most displaced models' selection bias\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"加 top 3.8% 和 full-sample flip rate\"\n  resolution_round: 12\n\n- id: \"R11-I4\"\n  summary: \"GSM1K 'suggests' 措辞略强\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"'suggests' → 'is consistent with'\"\n  resolution_round: 12\n\n- id: \"R11-I6\"\n  summary: \"Table 3 Ratio 列跨 benchmark 比较受 baseline 影响\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Table 3 caption 加说明\"\n  resolution_round: 12\n\n# ============================================================\n# ROUND 13 OPEN ISSUES — STATUS ASSESSMENT\n# ============================================================\n\n- id: \"R13-MF1\"\n  summary: \"LOFO family-concentration: 移除 Mistral/Llama-3 后 C% 降至 22-24%, power-reduction 解释不充分\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"N_ref≈533, N_focal≈492 仍远超 power threshold (N≥80)，8.8pp drop 不能仅归因 power reduction。Section 4.4 ~28% floor 与 LOFO 22.5% 的 tension 未讨论。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未直接提及。R14-MF2 涉及相关的 uncertainty quantification 问题。\"\n  action_items:\n    - round: 13\n      action: \"使用 Monte Carlo 框架对 LOFO 进行 expected power calibration\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF2\"\n  summary: \"Examinee non-independence 对 MH chi-squared inflation 缺乏直接定量 (R10-W1 reopened)\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"首次提出\"\n    - round: 12\n      reviewers: []\n      note: \"标记 resolved (cluster bootstrap CI + LOFO)\"\n    - round: 13\n      reviewers: [1]\n      note: \"Reopened: 三项间接证据不足。需 DEFF / effective sample size 直接量化 chi-squared inflation。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未直接提及，但 R14-MF2 中 DEFF=3.87 / Appendix C 讨论间接涉及。\"\n  action_items:\n    - round: 13\n      action: \"使用 design effect / effective sample size 方法调整 MH chi-squared\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF1\"\n  summary: \"新颖性定位——缺少与教育测量 temporal DIF rate baseline 对比\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"缺 SAT/GRE baseline (5-15%)。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未直接提及，但 R14-SF2 concurrent work 讨论间接相关。\"\n  action_items:\n    - round: 13\n      action: \"补充教育测量 temporal DIF rate baseline 对比\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF4\"\n  summary: \"92.4% 'item-specific' 推导不透明\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"推导链不可见，abstract/intro 反复引用但来源不明。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮 Abstract 未再出现 92.4%（已改为 pseudo R²<0.001 framing），但正文是否修复未确认。\"\n  action_items:\n    - round: 13\n      action: \"明确写出推导逻辑或替换为 pseudo R² framing\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Round 14 (Fresh review, 2026-05-22)\n# 2 critical open, 9 warning open, 5 info open\n\n# ============================================================\n# ROUND 14 — MUST-FIX (CRITICAL)\n# ============================================================\n\n- id: \"R14-MF1\"\n  summary: \"MMLU 57-subject 多维度结构违反 MH-DIF 匹配假设，辩护不充分\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 首提 Must-Fix, R2 AGREE。Ackerman 1992 / Roussos & Stout 1996: 多维测试 + secondary dimension 能力差异 → spurious DIF。论文声称 MH 不依赖 parametric IRT 过强。Cross-subject matching 仍多维（56 subjects 混合）。Within-subject C%=38.1% 高于 cross-subject 31.3%，但可能反映 local dependence 而非纯 DIF。缺少 temporal cohort domain-level ability profile shift 量化。\"\n  action_items:\n    - round: 14\n      action: \"明确承认多维度 matching 局限；量化 2023/2024 cohort domain-level 能力 profile 差异；讨论 spurious DIF 预期方向（高估 vs 低估）\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-MF2\"\n  summary: \"Cluster bootstrap CI [26.7%, 53.2%] 跨度极大但被 '~31%' 淡化，三种 uncertainty estimate 不一致\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 首提 Must-Fix, R2 AGREE。Model-level [29.4%, 38.1%] vs cluster bootstrap [26.7%, 53.2%] vs DEFF simple 29.2% vs DEFF weighted 13.5%。论文全文反复用 '31%' 但 CI 嵌入信息过载句子中，上界 53.2% 被 cohort-specific family structure 推高。\"\n  action_items:\n    - round: 14\n      action: \"Abstract/conclusion 同等突出 CI；Discussion 或 Appendix 系统对比三种 uncertainty quantification 的假设和适用性；明确说明 cluster bootstrap CI upward bias 来源\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 14 — SHOULD-FIX (WARNING)\n# ============================================================\n\n- id: \"R14-SF1\"\n  summary: \"Discussion (§5) 对 diagnostic 定位论文严重不足——缺因果归因框架、NLP 实践建议、benchmark reform 联系\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 定 Must-Fix, R1 降级 Should-Fix (presentation 非 soundness)。Director 裁定 Should-Fix。§5 仅半页 3 小节。§5.3 Monitor/Flag/Act 阈值推导不透明。Conclusion 仅 3 行。\"\n  action_items:\n    - round: 14\n      action: \"扩展 Discussion 至 ~1 页：因果假说系统讨论、Monitor/Flag/Act 阈值推导逻辑、与 benchmark reform 运动定位；扩展 Conclusion\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF2\"\n  summary: \"新颖性定位——与 Growing Pains / BHI / Benchmark² 等 concurrent work 区分不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 定 Must-Fix, R1 REBUT (方法论独特性足够)。Director 裁定 Should-Fix。§2 仅一句 'diagnostic foundation vs prescriptive framework'，BHI/Benchmark² 各一句带过。\"\n  action_items:\n    - round: 14\n      action: \"Introduction 或 Related Work 增加 positioning paragraph，对比 scope/method/findings/actionable output\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF3\"\n  summary: \"Abstract 信息密度过高，15+ 数字稀释关键信息\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"共识。建议保留 3-4 核心数字，enrichment≈0.96 改报 Jaccard=0.206。\"\n  action_items:\n    - round: 14\n      action: \"Abstract 重构：问题→核心发现→3-4 关键数字→implication；enrichment 改报 Jaccard\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF4\"\n  summary: \"术语不一致：temporal measurement instability / temporal DIF / measurement invariance 混用\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"共识。建议 §1/§3 建立术语层次：measurement invariance (目标) → DIF (检测方法) → temporal measurement instability (现象)。\"\n  action_items:\n    - round: 14\n      action: \"§1 或 §3 定义术语层次，全文统一\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF5\"\n  summary: \"Gema et al. (2024) MMLU ground truth errors 作为 DIF confound 未讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 首提, R1 强烈同意（称自己遗漏）。Bib 中有 gema2024mmlu 但正文未讨论。Wrong answer keys → 2024 models 选真正正确答案 → spurious DIF。\"\n  action_items:\n    - round: 14\n      action: \"§4 或 §5 讨论 ground truth error confound；如可行检查 Gema et al. flagged items 与 DIF items 的 overlap\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF6\"\n  summary: \"Semi-synthetic injection 生态效度有限——uniform binary flipping 不反映真实 contamination\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"共识。Limitations 已承认 worst-case uniform，但缺 difficulty-dependent / partial knowledge 替代模型讨论。§4.2 difficulty-direction interaction (ρ=-0.597) 暗示真实 contamination 与 difficulty 相关。\"\n  action_items:\n    - round: 14\n      action: \"讨论 1-2 种替代 contamination 模型（difficulty-dependent, partial knowledge）的定性影响\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF7\"\n  summary: \"IRT θ-conditioning (r=0.996 with total score) 不构成独立控制，应降级为 sensitivity check\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"共识。C%=0.312 vs 0.313，差异微不足道。称 'structural control' 过强。\"\n  action_items:\n    - round: 14\n      action: \"将 θ-conditioning 重新定位为 sensitivity check\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF8\"\n  summary: \"Multi-subject injection ΔFPR=0.060-0.069 (k≥10) 对真实数据 31% 的影响未讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 首提, R2 部分同意。ΔFPR=0 guarantee 仅限 k≤5，真实 contamination 必然跨多 subject。但 R2 指出 random-split C%=0.18% 仍提供 strong baseline。\"\n  action_items:\n    - round: 14\n      action: \"主文讨论 ΔFPR=0 保证的 boundary conditions (k≤5) 及 multi-subject FPR inflation 的 quantitative impact\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R14-SF9\"\n  summary: \"GSM1K cross-validation N=33 过小，需 influence diagnostics\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"共识。r=-0.478, p=0.005 but N=33。论文已定位 exploratory，但需 Cook's D 或注明 small-sample limitation。\"\n  action_items:\n    - round: 14\n      action: \"报告 influence diagnostics (Cook's D) 或注明 small-sample caveat\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 14 — INFO\n# ============================================================\n\n- id: \"R14-I1\"\n  summary: \"App F negative finding (AUROC=0.60) 在主文仅一句，可在 Discussion 展开\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [2]\n      note: \"R2 Should-Fix, R1 同意但认为 8 页限制下一句+Appendix 可接受。Director 降为 info。\"\n\n- id: \"R14-I2\"\n  summary: \"Temporal cohort 划分过粗 (2023 vs 2024)，6-month window C%=34.35% 更高但未充分讨论\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 Should-Fix, R1 同意但认为更窄窗口→更高 C% 加强而非削弱 claim。根本问题是多变量 confound 非粒度。\"\n\n- id: \"R14-I3\"\n  summary: \"Low exploitation rate (α=0.05) TPR=0.03，应补充 ETS B+C rate 展示完整分布\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix (31% 是 lower bound), R2 REBUT (31% 是 observed 非 estimated)。共识：补充 ETS B+C rate 更有价值。\"\n\n- id: \"R14-I4\"\n  summary: \"Missing references: MMLU-CF (Zhao et al. ACL 2025), Engels et al. (2026), Lee et al. (2026)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"MMLU-CF 共识必引；Engels/Lee R1 neutral，建议 authors 评估。\"\n\n- id: \"R14-I5\"\n  summary: \"排版细节：§5 enlargethispage hack、Table 2/3 字体偏小、Conclusion 仅 3 行、K=5 正文声明有争议\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"多项排版和呈现细节，见 Detailed Comments。\"\n\n# ============================================================\n# PRIOR RESOLVED (carried from Round 13, no change)\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"Permutation null 已补充到 §4.2\"\n  resolution_round: 8\n\n- id: \"R8-MF2\"\n  summary: \"'Drift' framing 超出数据支撑\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Title 改为 'Temporal Measurement Instability'\"\n  resolution_round: 9\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%\"\n  resolution_round: 4\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 practical significance paradox\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 11\n  resolution: \"Family-level profiles + pairwise flip rate + 'diagnostic not destructive' framing\"\n  resolution_round: 11\n\n- id: \"R8-SF1\"\n  summary: \"Proposition 1 过度形式化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"降格为 Remark（§3.4）\"\n  resolution_round: 9\n\n- id: \"R9-W2\"\n  summary: \"方法新颖性有限\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"§3.2 引用先驱方法 + LLM-specific adaptation\"\n  resolution_round: 10\n\n- id: \"R10-W1\"\n  summary: \"LLM examinee 非独立性对统计推断的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Cluster bootstrap CI + LOFO Table 6\"\n  resolution_round: 12\n\n- id: \"R5-N1\"\n  summary: \"ΔTPR 应标注为 upper-bound estimate\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 11\n  resolution: \"Abstract/§3.4/§4.5 均标注 worst-case uniform injection\"\n  resolution_round: 10\n\n- id: \"R9-W3\"\n  summary: \"\\\\enlargethispage 过于激进\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"从 18→6→2\"\n  resolution_round: 12\n\n- id: \"R11-W1\"\n  summary: \"页数超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§5.3 压缩 + Conclusion 在 page 8 内\"\n  resolution_round: 12\n\n- id: \"R1-W1\"\n  summary: \"§5.3 audit protocol causal framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 11\n  resolution: \"改为 'review flagged items for differential-performance-associated content characteristics'\"\n  resolution_round: 12\n\n- id: \"R11-W2\"\n  summary: \"ΔFPR=0.000 缺 single-subject 限定\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Contribution 2 加 'under single-subject contamination'\"\n  resolution_round: 12\n\n- id: \"R11-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"删除 φ=0.012、ΔFPR<0.01 for k≤5、45-174×\"\n  resolution_round: 12\n\n- id: \"R11-W4\"\n  summary: \"Table 1 'FPR (clean)' 术语矛盾\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"列名改为 'C% (web-clean)'\"\n  resolution_round: 12\n\n- id: \"R11-W5\"\n  summary: \"Family-level cluster bootstrap CI 应在正文报告\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§4.2 加 family-level CI + LOFO\"\n  resolution_round: 12\n\n- id: \"R11-W6\"\n  summary: \"新颖性定位需区分 LLM adaptation\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"§3.2 加三种 matching 策略区分\"\n  resolution_round: 12\n\n- id: \"R11-W7\"\n  summary: \"Semi-synthetic ecological validity 有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Limitations 覆盖\"\n  resolution_round: 12\n\n- id: \"R11-W8\"\n  summary: \"Graduated de-duplication 解读偏乐观\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"改为 'reduces C% moderately (confounded with power reduction)'\"\n  resolution_round: 12\n\n- id: \"R11-I3\"\n  summary: \"'200 most displaced models' selection bias\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"加 top 3.8% 和 full-sample flip rate\"\n  resolution_round: 12\n\n- id: \"R11-I4\"\n  summary: \"GSM1K 'suggests' 措辞略强\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"'suggests' → 'is consistent with'\"\n  resolution_round: 12\n\n- id: \"R11-I6\"\n  summary: \"Table 3 Ratio 列跨 benchmark 比较受 baseline 影响\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Table 3 caption 加说明\"\n  resolution_round: 12\n\n# ============================================================\n# ROUND 13 OPEN ISSUES — STATUS ASSESSMENT\n# ============================================================\n\n- id: \"R13-MF1\"\n  summary: \"LOFO family-concentration: 移除 Mistral/Llama-3 后 C% 降至 22-24%, power-reduction 解释不充分\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"N_ref≈533, N_focal≈492 仍远超 power threshold (N≥80)，8.8pp drop 不能仅归因 power reduction。Section 4.4 ~28% floor 与 LOFO 22.5% 的 tension 未讨论。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未直接提及。R14-MF2 涉及相关的 uncertainty quantification 问题。\"\n  action_items:\n    - round: 13\n      action: \"使用 Monte Carlo 框架对 LOFO 进行 expected power calibration\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-MF2\"\n  summary: \"Examinee non-independence 对 MH chi-squared inflation 缺乏直接定量 (R10-W1 reopened)\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"首次提出\"\n    - round: 12\n      reviewers: []\n      note: \"标记 resolved (cluster bootstrap CI + LOFO)\"\n    - round: 13\n      reviewers: [1]\n      note: \"Reopened: 三项间接证据不足。需 DEFF / effective sample size 直接量化 chi-squared inflation。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未直接提及，但 R14-MF2 中 DEFF=3.87 / Appendix C 讨论间接涉及。\"\n  action_items:\n    - round: 13\n      action: \"使用 design effect / effective sample size 方法调整 MH chi-squared\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF1\"\n  summary: \"新颖性定位——缺少与教育测量 temporal DIF rate baseline 对比\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"缺 SAT/GRE baseline (5-15%)。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未直接提及，但 R14-SF2 concurrent work 讨论间接相关。\"\n  action_items:\n    - round: 13\n      action: \"补充教育测量 temporal DIF rate baseline 对比\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-SF4\"\n  summary: \"92.4% 'item-specific' 推导不透明\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"推导链不可见，abstract/intro 反复引用但来源不明。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮 Abstract 未再出现 92.4%（已改为 pseudo R²<0.001 framing），但正文是否修复未确认。\"\n  action_items:\n    - round: 13\n      action: \"明确写出推导逻辑或替换为 pseudo R² framing\"\n      assigned_to: \"\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-22T11:42:49.308043+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 16931}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-22T11:42:53.827858+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-22T11:42:53.878669+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-22T11:45:38.455870+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 14 (Fresh Review)\n\n**论文**: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+统计推断+实验设计；R2: 新颖性+结构+相关工作）\n**轮次**: 1 轮（交叉分享后收敛，无需第 2 轮）\n\n---\n\n## Summary\n\n本文将教育测量学中经典的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 方法首次大规模应用于 LLM benchmark 评估，对 METABENCH 数据集（5,227 models × 12,508 MMLU items）进行 temporal DIF 分析。核心发现：~31% 的 MMLU items 在 2023→2024 model cohorts 间展现 ETS Category C 级别的功能变化。论文提出 ground truth meta-critique（web-overlap labels 与 DIF flags 近乎独立）和 semi-synthetic validation framework（cross-subject matching 实现 ΔFPR=0），并在 6 个 benchmarks 上进行了交叉验证。\n\n---\n\n## Strengths\n\n**S1. 填补重要研究空白。** 首次将标准化心理测量方法（MH-DIF + ETS classification）系统应用于 LLM benchmark temporal comparability 问题。规模空前（5,227 models × 27,125 items across 6 benchmarks），不是 toy experiment。\n\n**S2. Ground truth meta-critique 是 genuinely valuable insight。** 直接实证证明 web-overlap labels 与 DIF flags 近乎独立（enrichment=0.964, Jaccard=0.206, φ=0.012），揭示了现有 contamination detection 文献的系统性 validation methodology gap。对后续所有用 web-overlap 做 ground truth 的工作有直接影响。\n\n**S3. 控制实验全面且严谨。** 6 层 structural controls（random split / ability-quintile / within-family / matched-ability / IRT θ-conditioning / de-duplication）系统排除替代解释。Random split baseline (C%=0.18%) 提供了极强的 null reference。\n\n**S4. Cross-subject matching 是方法论 innovation。** 将 purified subtest matching 适配到 MMLU 的 57-subject 结构，理论上保证单科污染下 ΔFPR=0，经验验证支持（k≤5 时 ΔFPR<0.007）。\n\n**S5. Cross-benchmark replication 增强 generalizability。** 6 个 METABENCH benchmarks 一致呈现 temporal DIF pattern（C% 17.9-31.3%），knowledge/reasoning > procedural 的 gradient 符合理论预期。\n\n**S6. 写作整体质量高。** 对 NLP 读者不熟悉的 psychometric 概念解释清晰，Figure 1 ICC schematic 有效传达核心概念。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, consensus R1+R2] **MMLU 57-subject 多维度结构违反 MH-DIF 匹配假设，辩护不充分**\n\nMH-DIF 通过 total score 分层控制能力差异，隐含假设是 total score 充分捕捉影响 item response 的潜在特质。但 MMLU 横跨 57 subjects / 5 domains，Appendix A.1 承认 \"poor fit to unidimensional 2PL model\"。论文声称 \"MH-DIF relies only on total score stratification rather than parametric IRT assumptions\"（§3.2）——此论断过强。\n\nDIF 文献 (Ackerman 1992; Roussos & Stout 1996) 已充分记录：多维测试中，focal/reference group 在 secondary dimension 存在系统性差异时，total-score matching 产生 spurious DIF。2023→2024 cohort 涉及架构升级、训练数据扩充、RLHF 变革等多重变化，完全可能导致跨 subject 能力 profile 系统性偏移，被错误标记为 item-level DIF。\n\nCross-subject matching（§3.4）部分缓解但匹配变量仍为 56 subjects 混合。Within-subject C%=38.1% 高于 cross-subject 31.3%（可能反映 local dependence 而非纯 DIF），但两者之间的 tension 讨论不充分。\n\n**修改要求**：(1) 明确承认多维度 matching 的局限性而非回避；(2) 量化 2023/2024 cohort 在 domain-level 的能力 profile 差异（域间方差分析）；(3) 讨论如果多维度导致 spurious DIF，预期方向是高估还是低估。\n\n---\n\n**MF2** [critical, consensus R1+R2] **Cluster bootstrap CI [26.7%, 53.2%] 跨度极大但被 \"~31%\" 淡化，三种 uncertainty estimate 不一致**\n\n论文 headline finding \"approximately 31% of MMLU items exhibit DIF\" 贯穿 abstract/intro/conclusion。但 family-level cluster bootstrap 给出 95% CI 为 [26.7%, 53.2%]（跨度 26.5pp，上界近下界 2 倍）。三种 uncertainty quantification 给出不一致图景：\n- Model-level bootstrap: [29.4%, 38.1%]\n- Family-level cluster bootstrap: [26.7%, 53.2%]\n- DEFF simple mean: 29.2%\n- DEFF weighted mean: 13.5%\n\n论文将 cluster bootstrap CI 描述为 \"continuing robustness under within-family dependence\"，用语与 CI 跨度不匹配。Abstract/conclusion 中 CI 被嵌入信息过载句子，读者易只记住 \"31%\"。\n\n**修改要求**：(1) Abstract/conclusion 中将 CI 与 point estimate 同等突出；(2) Discussion 或 Appendix 系统对比三种 uncertainty quantification 的假设和适用性；(3) 明确说明 cluster bootstrap CI 上界偏高的来源（cohort-specific family structure）。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, R2 提出 R1 同意降级] **Discussion (§5) 对 diagnostic 定位论文发展不充分**\n\n§5 仅约半页 3 小节。论文定位为 \"diagnostic lens\" 但 Discussion 未充分展开诊断含义：缺少因果归因系统讨论（contamination vs capability evolution vs training methodology shifts 的 testable predictions）；§5.3 Monitor/Flag/Act 阈值推导不透明；缺少与 benchmark reform 运动（MMLU-CF / dynamic benchmarks）的定位讨论；Conclusion 仅 3 行。\n\n**修改建议**：扩展 Discussion 至 ~1 页；增加因果假说系统讨论；明确阈值推导逻辑；扩展 Conclusion。\n\n---\n\n**SF2** [warning, R2 提出 R1 rebut, Director 裁定 Should-Fix] **新颖性定位——与 Growing Pains / BHI / Benchmark² 等 concurrent work 区分不足**\n\n§2 与 Growing Pains 仅一句 \"diagnostic foundation vs prescriptive framework\"（integration 而非 differentiation argument）。BHI / Benchmark² 各一句带过。当 3-4 篇同期工作都在 psychometric 视角审视 LLM benchmarks 时，必须明确本文的 unique angle。\n\n**修改建议**：增加 positioning paragraph 对比 scope / method / findings / actionable output。R1 认为方法论独特性已足够清晰（MH-DIF + ETS 是具体可引用的标准化体系），但补充对比不会增加负担。\n\n---\n\n**SF3** [warning, consensus] **Abstract 信息密度过高**\n\n15+ 个数字塞入一段（ΔFPR=0.000, ΔTPR=+0.508, enrichment≈0.96, 31%, [26.7%,53.2%], ρ≈0.997, +53 positions 等）。Enrichment≈0.96 容易被 NLP 读者误读为高一致性（实际 Jaccard=0.206 才反映 classification agreement）。\n\n**修改建议**：保留 3-4 核心数字；enrichment 改报 Jaccard；重构为问题→发现→数字→implication 的叙事流。\n\n---\n\n**SF4** [warning, consensus] **术语不一致**\n\nTitle 用 \"temporal measurement instability\"，正文混用 \"temporal DIF\" / \"measurement invariance\" / \"differential item functioning\"。\"Measurement invariance\" (Meredith 1993) 是比 DIF 更广的概念框架。\n\n**修改建议**：§1 或 §3 建立术语层次（measurement invariance 是目标属性 → DIF 是检测方法 → temporal measurement instability 是现象），之后统一使用。\n\n---\n\n**SF5** [warning, R2 提出 R1 强烈同意] **Gema et al. (2024) MMLU ground truth errors 作为 DIF confound 未讨论**\n\nbib 中有 gema2024mmlu 但正文未讨论。MMLU 存在大量 ground truth errors（57% virology questions 有问题）。如果 2024 模型\"知道真正的正确答案\"而选择了与 key 不同的选项，会被 MH-DIF 标记为 DIF——原因是 benchmark 质量而非 measurement instability。这是对 31% DIF rate 的又一替代解释。\n\n**修改建议**：§4 或 §5 讨论此 confound；如可行检查 Gema et al. flagged items 与 DIF items 的 overlap。\n\n---\n\n**SF6** [warning, consensus] **Semi-synthetic injection 生态效度有限**\n\nUniform binary flipping 不反映真实 contamination（partial knowledge / difficulty-dependent exploitation / answer-pattern memorization）。§4.2 已发现 difficulty-direction interaction (ρ=-0.597)，暗示真实 contamination 与 difficulty 相关，uniform flipping 可能系统性偏离真实 pattern。Limitations 已承认但讨论不足。\n\n**修改建议**：讨论 1-2 种替代 contamination 模型的定性影响。\n\n---\n\n**SF7** [warning, consensus] **IRT θ-conditioning 不构成独立控制**\n\nr(θ, total score) = 0.996 → C% 从 0.313 变为 0.312。两种 matching variable 几乎完全等价，称 \"structural control\" 过强。且 2PL model fit 差，用 poorly-fitting model 的 θ 做控制本身有 circularity。\n\n**修改建议**：降级为 \"sensitivity check\" 而非 \"structural control\"。\n\n---\n\n**SF8** [warning, R1 提出 R2 部分同意] **Multi-subject injection ΔFPR=0.060-0.069 (k≥10) 对真实数据影响未讨论**\n\nΔFPR=0 guarantee 仅限 k≤5。真实 contamination 几乎必然跨越多个 subjects。Table 5 显示 k=10 时 ΔFPR=0.047±0.022, k=20 时 0.069±0.018。论文主文对 boundary conditions 讨论不足（仅 §3.4 简短提到 k≤5）。R2 补充：random-split C%=0.18% 仍提供 strong baseline，31% 远超合理 FPR inflation。\n\n**修改建议**：主文讨论 ΔFPR=0 保证的 boundary conditions 及 multi-subject FPR inflation 的 quantitative impact。\n\n---\n\n**SF9** [warning, consensus] **GSM1K cross-validation N=33 过小**\n\nr=-0.478, p=0.005 but N=33。Figure 5 可能存在 influential outlier。论文已定位为 \"exploratory\"，但缺少 influence diagnostics。\n\n**修改建议**：报告 Cook's D 或注明 small-sample caveat。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n- MF1（多维度假设）和 MF2（CI 透明度）是本文最核心的方法论弱点\n- Ground truth meta-critique 是本文最重要的贡献（S2）\n- Cross-subject matching 是 genuine methodological innovation（S4）\n- Abstract 信息密度过高需重构（SF3）\n- 术语需统一（SF4）\n- Gema et al. confound 必须讨论（SF5）\n- Semi-synthetic ecological validity 有限（SF6）\n- IRT θ-conditioning 应降级（SF7）\n- 规模和控制实验全面性是主要优势（S1, S3）\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | Director 裁定 |\n|------|---------|---------|---------------|\n| R2-N1 Discussion 不足 | AGREE with downgrade → Should-Fix（presentation 非 soundness） | 维持 critical | **Should-Fix** (SF1)：8 页实证论文，Discussion 长度是呈现问题 |\n| R2-N2 Novelty positioning | REBUT → Minor/Should-Fix（方法论独特性足够） | 维持 critical | **Should-Fix** (SF2)：MH-DIF 确实唯一，但补充对比无害 |\n| R1-W2 31% 是 lower bound | 维持 Should-Fix | 部分 REBUT（31% 是 observed 非 estimated） | **Info** (I3)：R2 逻辑正确——31% 是直接观测值；但补充 ETS B+C rate 有价值 |\n\n---\n\n## Questions for Authors\n\n**Q1** [from R1, R2 补充]: 是否做过在每个 subject 内部独立运行 MH-DIF（subject-internal score 匹配）的完整分析？57 subjects 的 within-subject C% 分布（vs cross-subject C%）scatter plot 能否提供？\n\n**Q2** [from R1]: Matched-ability quintile 各 stratum 内 2023/2024 cohort 的 score 分布是否确实匹配良好？是否有 residual ability difference？\n\n**Q3** [from both]: Cluster bootstrap CI [26.7%, 53.2%] 与 DEFF-adjusted C% 如何调和？三种 uncertainty quantification 哪个最适合本场景，为什么？\n\n**Q4** [from R2]: §4.7 中 6-month window (C%=34.35%) 高于年度划分 (31.3%)——是否表明 DIF 主要在特定时间点突变而非渐进积累？\n\n**Q5** [from R1]: 如果 exploitation rate 按 item difficulty 变化（hard items 更容易被 exploit），dose-response curve 形状如何变化？\n\n**Q6** [from R2]: Cross-subject matching 的 ΔFPR=0 guarantee 在 systematic contamination（整个 training pipeline 改变）下是否失效？\n\n---\n\n## Missing References\n\n1. **Zhao et al. (ACL 2025)** \"MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark\" — 直接重构 MMLU 以消除 contamination artifacts。**必须引用**（共识）。\n2. **Engels, Lüdtke, and Robitzsch (2026)** \"Estimating Trends With Differential Item Functioning\" — 讨论存在 DIF 时如何估计纵向趋势，方法论高度相关。建议引用。\n3. **Lee, Huang, Svetina Valdivia, Schwartzman (2026)** \"On the Complex Sources of Differential Item Functioning\" — DIF 来源分析，与 \"DIF detects that not why\" 讨论相关。建议引用。\n4. **Gema et al. (2024)** \"Are We Done with MMLU?\" — bib 中有但正文未讨论。必须在正文中讨论其 implications (SF5)。\n\n---\n\n## External Review\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical / 3 warning / 8 info）。\n\n**Warnings**:\n1. Pages 3-6 连续 4 页几乎纯文本（Related Work → Method → Experiments 开头），display items 全部集中在 pages 7-8，造成前松后紧节奏失衡。建议 Method 部分插入流程图或将 Table 1/2 提前。\n2. Page 7 单页堆叠 3 个 display items（Table 1 + Figure 2 + Table 2），视觉拥挤。建议将 Table 2 移至 page 8 分散密度。\n3. Page 15 (Appendix) 有 ~1/4 页空白，末页利用率偏低（不影响主文评价）。\n\n**Info highlights**:\n- Figure 1 位置合理（page 2），ICC schematic 有效传达核心概念\n- 所有表格使用 booktabs 风格，格式规范\n- 未发现 margin overflow、公式渲染错误、section heading 孤悬\n- Figure 5/6 axis labels 偏小（~6pt），建议增大至 ≥8pt\n- 主文 8 页含 5 个 display items（1 figure + 4 tables），密度 0.63/页，偏低但可接受\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5 — Borderline Conference**\n\n**置信度: 4/5**（两位 Reviewer 均熟悉 DIF 方法论和 LLM evaluation，仔细阅读全文含附录，交叉分享后意见收敛）\n\n**评分理由**:\n\n本文在 idea（psychometric audit of LLM benchmarks）和 scale（5,227 models × 6 benchmarks）上具有明确贡献，ground truth meta-critique 填补了重要空白。但存在两个可修复的核心方法论问题：(1) 多维度假设违反的量化辩护缺失，直接关系到 31% DIF rate 中有多少是 genuine vs spurious；(2) 统计不确定性的呈现不够透明，三种 CI 方法给出不一致图景。此外，Discussion 的充实度、与 concurrent work 的定位、以及 MMLU ground truth error confound 都需要加强。\n\n**修改后预期**：如果 MF1（补充 domain-level profile analysis + 明确讨论 spurious DIF 方向）和 MF2（CI 透明呈现 + 系统对比 uncertainty methods）得到充分修复，加上 SF1-SF9 中的高优先项（Discussion 扩展、Gema confound、novelty positioning），论文可达到 Conference 水平（4.0）。核心 idea 和实验规模足够支撑主会议，瓶颈在呈现和辩护而非根本性缺陷。\n\n---\n\n## Detailed Comments（逐节）\n\n**Abstract**: 信息密度过高（15+ 数字），enrichment≈0.96 易误读。建议精简至 5 个核心数字，优先报 Jaccard。\n\n**§1 Introduction**: 叙事逻辑清晰但过早引入大量数字（31%, 0.997, 0.18%, 0.206 等），建议推迟部分至 Results。约 1.5 页稍偏长。\n\n**§2 Related Work**: 覆盖面广但 concurrent work 区分不足。MMLU-CF (Zhao et al. 2025) 未引用。Growing Pains / BHI / Benchmark² 需实质性对比。\n\n**§3 Method**: 清晰完整。§3.2 \"LLM-specific challenges\" 段过长（近半页），可 itemize。IRT θ-conditioning 应降级为 sensitivity check。K=5 已在正文明确。\n\n**§4 Experiments**: 丰富且有说服力。核心问题：多维度 confound 未量化（MF1）；CI 呈现不透明（MF2）；GSM1K N=33 需 influence diagnostics。\n\n**§5 Discussion**: 过短（~半页），Monitor/Flag/Act 阈值推导不透明，因果归因骨架有但未展开，缺 benchmark reform 定位。\n\n**§6 Conclusion**: 仅 3 行，对 8 页 paper 过短。\n\n**Limitations**: 存在且覆盖主要局限（ecological validity, causal decomposition, temporal granularity），但部分重要讨论不应仅出现在此处。\n\n**Appendix**: 详尽，DEFF analysis (App C) 和 predictive model (App F) 有价值但正文引用不足。\n\n**格式合规**: 正文 8 页 ✓; ACL template [review] ✓; Double-blind ✓; Limitations section ✓; 匿名代码链接 ✓。`\\enlargethispage*{8\\baselineskip}` 在 §5 仍然激进。",
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 14 (Fresh Review)\n\n**论文**: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+统计推断+实验设计；R2: 新颖性+结构+相关工作）\n**轮次**: 1 轮（交叉分享后收敛，无需第 2 轮）\n\n---\n\n## Summary\n\n本文将教育测量学中经典的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 方法首次大规模应用于 LLM benchmark 评估，对 METABENCH 数据集（5,227 models × 12,508 MMLU items）进行 temporal DIF 分析。核心发现：~31% 的 MMLU items 在 2023→2024 model cohorts 间展现 ETS Category C 级别的功能变化。论文提出 ground truth meta-critique（web-overlap labels 与 DIF flags 近乎独立）和 semi-synthetic validation framework（cross-subject matching 实现 ΔFPR=0），并在 6 个 benchmarks 上进行了交叉验证。\n\n---\n\n## Strengths\n\n**S1. 填补重要研究空白。** 首次将标准化心理测量方法（MH-DIF + ETS classification）系统应用于 LLM benchmark temporal comparability 问题。规模空前（5,227 models × 27,125 items across 6 benchmarks），不是 toy experiment。\n\n**S2. Ground truth meta-critique 是 genuinely valuable insight。** 直接实证证明 web-overlap labels 与 DIF flags 近乎独立（enrichment=0.964, Jaccard=0.206, φ=0.012），揭示了现有 contamination detection 文献的系统性 validation methodology gap。对后续所有用 web-overlap 做 ground truth 的工作有直接影响。\n\n**S3. 控制实验全面且严谨。** 6 层 structural controls（random split / ability-quintile / within-family / matched-ability / IRT θ-conditioning / de-duplication）系统排除替代解释。Random split baseline (C%=0.18%) 提供了极强的 null reference。\n\n**S4. Cross-subject matching 是方法论 innovation。** 将 purified subtest matching 适配到 MMLU 的 57-subject 结构，理论上保证单科污染下 ΔFPR=0，经验验证支持（k≤5 时 ΔFPR<0.007）。\n\n**S5. Cross-benchmark replication 增强 generalizability。** 6 个 METABENCH benchmarks 一致呈现 temporal DIF pattern（C% 17.9-31.3%），knowledge/reasoning > procedural 的 gradient 符合理论预期。\n\n**S6. 写作整体质量高。** 对 NLP 读者不熟悉的 psychometric 概念解释清晰，Figure 1 ICC schematic 有效传达核心概念。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, consensus R1+R2] **MMLU 57-subject 多维度结构违反 MH-DIF 匹配假设，辩护不充分**\n\nMH-DIF 通过 total score 分层控制能力差异，隐含假设是 total score 充分捕捉影响 item response 的潜在特质。但 MMLU 横跨 57 subjects / 5 domains，Appendix A.1 承认 \"poor fit to unidimensional 2PL model\"。论文声称 \"MH-DIF relies only on total score stratification rather than parametric IRT assumptions\"（§3.2）——此论断过强。\n\nDIF 文献 (Ackerman 1992; Roussos & Stout 1996) 已充分记录：多维测试中，focal/reference group 在 secondary dimension 存在系统性差异时，total-score matching 产生 spurious DIF。2023→2024 cohort 涉及架构升级、训练数据扩充、RLHF 变革等多重变化，完全可能导致跨 subject 能力 profile 系统性偏移，被错误标记为 item-level DIF。\n\nCross-subject matching（§3.4）部分缓解但匹配变量仍为 56 subjects 混合。Within-subject C%=38.1% 高于 cross-subject 31.3%（可能反映 local dependence 而非纯 DIF），但两者之间的 tension 讨论不充分。\n\n**修改要求**：(1) 明确承认多维度 matching 的局限性而非回避；(2) 量化 2023/2024 cohort 在 domain-level 的能力 profile 差异（域间方差分析）；(3) 讨论如果多维度导致 spurious DIF，预期方向是高估还是低估。\n\n---\n\n**MF2** [critical, consensus R1+R2] **Cluster bootstrap CI [26.7%, 53.2%] 跨度极大但被 \"~31%\" 淡化，三种 uncertainty estimate 不一致**\n\n论文 headline finding \"approximately 31% of MMLU items exhibit DIF\" 贯穿 abstract/intro/conclusion。但 family-level cluster bootstrap 给出 95% CI 为 [26.7%, 53.2%]（跨度 26.5pp，上界近下界 2 倍）。三种 uncertainty quantification 给出不一致图景：\n- Model-level bootstrap: [29.4%, 38.1%]\n- Family-level cluster bootstrap: [26.7%, 53.2%]\n- DEFF simple mean: 29.2%\n- DEFF weighted mean: 13.5%\n\n论文将 cluster bootstrap CI 描述为 \"continuing robustness under within-family dependence\"，用语与 CI 跨度不匹配。Abstract/conclusion 中 CI 被嵌入信息过载句子，读者易只记住 \"31%\"。\n\n**修改要求**：(1) Abstract/conclusion 中将 CI 与 point estimate 同等突出；(2) Discussion 或 Appendix 系统对比三种 uncertainty quantification 的假设和适用性；(3) 明确说明 cluster bootstrap CI 上界偏高的来源（cohort-specific family structure）。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, R2 提出 R1 同意降级] **Discussion (§5) 对 diagnostic 定位论文发展不充分**\n\n§5 仅约半页 3 小节。论文定位为 \"diagnostic lens\" 但 Discussion 未充分展开诊断含义：缺少因果归因系统讨论（contamination vs capability evolution vs training methodology shifts 的 testable predictions）；§5.3 Monitor/Flag/Act 阈值推导不透明；缺少与 benchmark reform 运动（MMLU-CF / dynamic benchmarks）的定位讨论；Conclusion 仅 3 行。\n\n**修改建议**：扩展 Discussion 至 ~1 页；增加因果假说系统讨论；明确阈值推导逻辑；扩展 Conclusion。\n\n---\n\n**SF2** [warning, R2 提出 R1 rebut, Director 裁定 Should-Fix] **新颖性定位——与 Growing Pains / BHI / Benchmark² 等 concurrent work 区分不足**\n\n§2 与 Growing Pains 仅一句 \"diagnostic foundation vs prescriptive framework\"（integration 而非 differentiation argument）。BHI / Benchmark² 各一句带过。当 3-4 篇同期工作都在 psychometric 视角审视 LLM benchmarks 时，必须明确本文的 unique angle。\n\n**修改建议**：增加 positioning paragraph 对比 scope / method / findings / actionable output。R1 认为方法论独特性已足够清晰（MH-DIF + ETS 是具体可引用的标准化体系），但补充对比不会增加负担。\n\n---\n\n**SF3** [warning, consensus] **Abstract 信息密度过高**\n\n15+ 个数字塞入一段（ΔFPR=0.000, ΔTPR=+0.508, enrichment≈0.96, 31%, [26.7%,53.2%], ρ≈0.997, +53 positions 等）。Enrichment≈0.96 容易被 NLP 读者误读为高一致性（实际 Jaccard=0.206 才反映 classification agreement）。\n\n**修改建议**：保留 3-4 核心数字；enrichment 改报 Jaccard；重构为问题→发现→数字→implication 的叙事流。\n\n---\n\n**SF4** [warning, consensus] **术语不一致**\n\nTitle 用 \"temporal measurement instability\"，正文混用 \"temporal DIF\" / \"measurement invariance\" / \"differential item functioning\"。\"Measurement invariance\" (Meredith 1993) 是比 DIF 更广的概念框架。\n\n**修改建议**：§1 或 §3 建立术语层次（measurement invariance 是目标属性 → DIF 是检测方法 → temporal measurement instability 是现象），之后统一使用。\n\n---\n\n**SF5** [warning, R2 提出 R1 强烈同意] **Gema et al. (2024) MMLU ground truth errors 作为 DIF confound 未讨论**\n\nbib 中有 gema2024mmlu 但正文未讨论。MMLU 存在大量 ground truth errors（57% virology questions 有问题）。如果 2024 模型\"知道真正的正确答案\"而选择了与 key 不同的选项，会被 MH-DIF 标记为 DIF——原因是 benchmark 质量而非 measurement instability。这是对 31% DIF rate 的又一替代解释。\n\n**修改建议**：§4 或 §5 讨论此 confound；如可行检查 Gema et al. flagged items 与 DIF items 的 overlap。\n\n---\n\n**SF6** [warning, consensus] **Semi-synthetic injection 生态效度有限**\n\nUniform binary flipping 不反映真实 contamination（partial knowledge / difficulty-dependent exploitation / answer-pattern memorization）。§4.2 已发现 difficulty-direction interaction (ρ=-0.597)，暗示真实 contamination 与 difficulty 相关，uniform flipping 可能系统性偏离真实 pattern。Limitations 已承认但讨论不足。\n\n**修改建议**：讨论 1-2 种替代 contamination 模型的定性影响。\n\n---\n\n**SF7** [warning, consensus] **IRT θ-conditioning 不构成独立控制**\n\nr(θ, total score) = 0.996 → C% 从 0.313 变为 0.312。两种 matching variable 几乎完全等价，称 \"structural control\" 过强。且 2PL model fit 差，用 poorly-fitting model 的 θ 做控制本身有 circularity。\n\n**修改建议**：降级为 \"sensitivity check\" 而非 \"structural control\"。\n\n---\n\n**SF8** [warning, R1 提出 R2 部分同意] **Multi-subject injection ΔFPR=0.060-0.069 (k≥10) 对真实数据影响未讨论**\n\nΔFPR=0 guarantee 仅限 k≤5。真实 contamination 几乎必然跨越多个 subjects。Table 5 显示 k=10 时 ΔFPR=0.047±0.022, k=20 时 0.069±0.018。论文主文对 boundary conditions 讨论不足（仅 §3.4 简短提到 k≤5）。R2 补充：random-split C%=0.18% 仍提供 strong baseline，31% 远超合理 FPR inflation。\n\n**修改建议**：主文讨论 ΔFPR=0 保证的 boundary conditions 及 multi-subject FPR inflation 的 quantitative impact。\n\n---\n\n**SF9** [warning, consensus] **GSM1K cross-validation N=33 过小**\n\nr=-0.478, p=0.005 but N=33。Figure 5 可能存在 influential outlier。论文已定位为 \"exploratory\"，但缺少 influence diagnostics。\n\n**修改建议**：报告 Cook's D 或注明 small-sample caveat。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n- MF1（多维度假设）和 MF2（CI 透明度）是本文最核心的方法论弱点\n- Ground truth meta-critique 是本文最重要的贡献（S2）\n- Cross-subject matching 是 genuine methodological innovation（S4）\n- Abstract 信息密度过高需重构（SF3）\n- 术语需统一（SF4）\n- Gema et al. confound 必须讨论（SF5）\n- Semi-synthetic ecological validity 有限（SF6）\n- IRT θ-conditioning 应降级（SF7）\n- 规模和控制实验全面性是主要优势（S1, S3）\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | Director 裁定 |\n|------|---------|---------|---------------|\n| R2-N1 Discussion 不足 | AGREE with downgrade → Should-Fix（presentation 非 soundness） | 维持 critical | **Should-Fix** (SF1)：8 页实证论文，Discussion 长度是呈现问题 |\n| R2-N2 Novelty positioning | REBUT → Minor/Should-Fix（方法论独特性足够） | 维持 critical | **Should-Fix** (SF2)：MH-DIF 确实唯一，但补充对比无害 |\n| R1-W2 31% 是 lower bound | 维持 Should-Fix | 部分 REBUT（31% 是 observed 非 estimated） | **Info** (I3)：R2 逻辑正确——31% 是直接观测值；但补充 ETS B+C rate 有价值 |\n\n---\n\n## Questions for Authors\n\n**Q1** [from R1, R2 补充]: 是否做过在每个 subject 内部独立运行 MH-DIF（subject-internal score 匹配）的完整分析？57 subjects 的 within-subject C% 分布（vs cross-subject C%）scatter plot 能否提供？\n\n**Q2** [from R1]: Matched-ability quintile 各 stratum 内 2023/2024 cohort 的 score 分布是否确实匹配良好？是否有 residual ability difference？\n\n**Q3** [from both]: Cluster bootstrap CI [26.7%, 53.2%] 与 DEFF-adjusted C% 如何调和？三种 uncertainty quantification 哪个最适合本场景，为什么？\n\n**Q4** [from R2]: §4.7 中 6-month window (C%=34.35%) 高于年度划分 (31.3%)——是否表明 DIF 主要在特定时间点突变而非渐进积累？\n\n**Q5** [from R1]: 如果 exploitation rate 按 item difficulty 变化（hard items 更容易被 exploit），dose-response curve 形状如何变化？\n\n**Q6** [from R2]: Cross-subject matching 的 ΔFPR=0 guarantee 在 systematic contamination（整个 training pipeline 改变）下是否失效？\n\n---\n\n## Missing References\n\n1. **Zhao et al. (ACL 2025)** \"MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark\" — 直接重构 MMLU 以消除 contamination artifacts。**必须引用**（共识）。\n2. **Engels, Lüdtke, and Robitzsch (2026)** \"Estimating Trends With Differential Item Functioning\" — 讨论存在 DIF 时如何估计纵向趋势，方法论高度相关。建议引用。\n3. **Lee, Huang, Svetina Valdivia, Schwartzman (2026)** \"On the Complex Sources of Differential Item Functioning\" — DIF 来源分析，与 \"DIF detects that not why\" 讨论相关。建议引用。\n4. **Gema et al. (2024)** \"Are We Done with MMLU?\" — bib 中有但正文未讨论。必须在正文中讨论其 implications (SF5)。\n\n---\n\n## External Review\n\n未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical / 3 warning / 8 info）。\n\n**Warnings**:\n1. Pages 3-6 连续 4 页几乎纯文本（Related Work → Method → Experiments 开头），display items 全部集中在 pages 7-8，造成前松后紧节奏失衡。建议 Method 部分插入流程图或将 Table 1/2 提前。\n2. Page 7 单页堆叠 3 个 display items（Table 1 + Figure 2 + Table 2），视觉拥挤。建议将 Table 2 移至 page 8 分散密度。\n3. Page 15 (Appendix) 有 ~1/4 页空白，末页利用率偏低（不影响主文评价）。\n\n**Info highlights**:\n- Figure 1 位置合理（page 2），ICC schematic 有效传达核心概念\n- 所有表格使用 booktabs 风格，格式规范\n- 未发现 margin overflow、公式渲染错误、section heading 孤悬\n- Figure 5/6 axis labels 偏小（~6pt），建议增大至 ≥8pt\n- 主文 8 页含 5 个 display items（1 figure + 4 tables），密度 0.63/页，偏低但可接受\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5 — Borderline Conference**\n\n**置信度: 4/5**（两位 Reviewer 均熟悉 DIF 方法论和 LLM evaluation，仔细阅读全文含附录，交叉分享后意见收敛）\n\n**评分理由**:\n\n本文在 idea（psychometric audit of LLM benchmarks）和 scale（5,227 models × 6 benchmarks）上具有明确贡献，ground truth meta-critique 填补了重要空白。但存在两个可修复的核心方法论问题：(1) 多维度假设违反的量化辩护缺失，直接关系到 31% DIF rate 中有多少是 genuine vs spurious；(2) 统计不确定性的呈现不够透明，三种 CI 方法给出不一致图景。此外，Discussion 的充实度、与 concurrent work 的定位、以及 MMLU ground truth error confound 都需要加强。\n\n**修改后预期**：如果 MF1（补充 domain-level profile analysis + 明确讨论 spurious DIF 方向）和 MF2（CI 透明呈现 + 系统对比 uncertainty methods）得到充分修复，加上 SF1-SF9 中的高优先项（Discussion 扩展、Gema confound、novelty positioning），论文可达到 Conference 水平（4.0）。核心 idea 和实验规模足够支撑主会议，瓶颈在呈现和辩护而非根本性缺陷。\n\n---\n\n## Detailed Comments（逐节）\n\n**Abstract**: 信息密度过高（15+ 数字），enrichment≈0.96 易误读。建议精简至 5 个核心数字，优先报 Jaccard。\n\n**§1 Introduction**: 叙事逻辑清晰但过早引入大量数字（31%, 0.997, 0.18%, 0.206 等），建议推迟部分至 Results。约 1.5 页稍偏长。\n\n**§2 Related Work**: 覆盖面广但 concurrent work 区分不足。MMLU-CF (Zhao et al. 2025) 未引用。Growing Pains / BHI / Benchmark² 需实质性对比。\n\n**§3 Method**: 清晰完整。§3.2 \"LLM-specific challenges\" 段过长（近半页），可 itemize。IRT θ-conditioning 应降级为 sensitivity check。K=5 已在正文明确。\n\n**§4 Experiments**: 丰富且有说服力。核心问题：多维度 confound 未量化（MF1）；CI 呈现不透明（MF2）；GSM1K N=33 需 influence diagnostics。\n\n**§5 Discussion**: 过短（~半页），Monitor/Flag/Act 阈值推导不透明，因果归因骨架有但未展开，缺 benchmark reform 定位。\n\n**§6 Conclusion**: 仅 3 行，对 8 页 paper 过短。\n\n**Limitations**: 存在且覆盖主要局限（ecological validity, causal decomposition, temporal granularity），但部分重要讨论不应仅出现在此处。\n\n**Appendix**: 详尽，DEFF analysis (App C) 和 predictive model (App F) 有价值但正文引用不足。\n\n**格式合规**: 正文 8 页 ✓; ACL template [review] ✓; Double-blind ✓; Limitations section ✓; 匿名代码链接 ✓。`\\enlargethispage*{8\\baselineskip}` 在 §5 仍然激进。",
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-22T11:45:43.536297+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 5080
}
```

</details>

---


### Tool call

_source line 726 · 2026-05-22T11:45:51.337933+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-0.7: 资料检查 + Venue + 编排 + 视觉审查', 'status': 'completed', 'activeForm': '完成初始化'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '完成交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '完成收敛判断'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'completed', 'activeForm': '完成报告投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-0.7: 资料检查 + Venue + 编排 + 视觉审查', 'status': 'completed', 'activeForm': '完成初始化'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '完成交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '完成收敛判断'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'completed', 'activeForm': '完成报告投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-22T11:45:51.338462+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 728 · 2026-05-22T11:46:01.363984+00:00_

**Round 14 审稿完成。**

报告已投递至 Research Director。核心结论：

**评分：3.5 / 5 — Borderline Conference**

- **2 个 Must-Fix**：(MF1) MMLU 多维度结构违反 MH-DIF 匹配假设，缺 domain-level profile shift 量化；(MF2) Cluster bootstrap CI 跨度极大但被 "~31%" 淡化，三种 uncertainty estimate 不一致
- **9 个 Should-Fix**：Discussion 不充分、concurrent work 区分不足、Abstract 过密、术语不一致、Gema et al. ground truth error confound、semi-synthetic 生态效度、θ-conditioning 降级、multi-subject ΔFPR、GSM1K 样本量
- **修改后预期**：MF1/MF2 充分修复 + 高优先 SF 处理后可达 Conference 水平（4.0）。瓶颈在呈现和辩护，非根本性缺陷。

Issue Tracker 已同步（`review_issues.yaml`：2 critical / 9 warning / 5 info open）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 72

## Round 72

2 recorded events


### User

_source line 729 · 2026-05-22T11:46:04.082005+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **R1-N1（多维度性）**：[AGREE] 部分同意，多维度确实是根本性方法论挑战，但 within-subject C% 更高（38.1% vs 31.3%）暗示多维度可能导致低估而非高估
- **R1-N2（CI 宽度）**：[AGREE] 同意应透明报告 CI，但三种 uncertainty estimate 需要系统对比
- **R1-W1–W5**：大部分同意，仅 W2（31% 是 lower bound）部分反驳——31% 是 observed rate 不是 detection-based estimate
- **R1-Minor-1（K 值）**：[REBUT] K=5 已在 §3.2 明确定义
- 其余 Minor 和 Questions 均同意或补充了具体证据

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 730 · 2026-05-22T11:46:12.587453+00:00_

审稿流程已全部完成。

**汇总**：
- 评分 **3.5/5 Borderline Conference**，1 轮收敛
- **2 个 Must-Fix**：多维度假设辩护不足 + CI 透明度
- **9 个 Should-Fix**：Discussion 扩展、concurrent work 定位、Abstract 精简、术语统一、Gema confound、semi-synthetic 生态效度、θ-conditioning 降级、multi-subject ΔFPR、GSM1K 样本量
- 审稿报告 + Issue Tracker 已同步投递给 Research Director

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 73

## Round 73

64 recorded events


### User

_source line 731 · 2026-05-22T12:14:35.599698+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 732 · 2026-05-22T12:14:41.803984+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 733 · 2026-05-22T12:14:41.804650+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 734 · 2026-05-22T12:14:48.586473+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 735 · 2026-05-22T12:14:48.586982+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 736 · 2026-05-22T12:14:51.502346+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-22T12:14:51.553034+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-22T12:14:55.979631+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 739 · 2026-05-22T12:14:57.438238+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1458
}
```

</details>

---


### Tool call

_source line 740 · 2026-05-22T12:14:57.438789+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-22T12:14:58.345337+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Measurement Instability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 742 · 2026-05-22T12:14:58.396286+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-22T12:15:04.443413+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

I found search results related to EMN
…[truncated 1457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 6047
}
```

</details>

---


### Tool call

_source line 744 · 2026-05-22T12:15:08.647329+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 745 · 2026-05-22T12:15:09.409303+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers commitment deadline ARR submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers commitment deadline ARR submission"
  }
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-22T12:15:11.327051+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
  "description": "List paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
    "description": "List paper sections"
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-22T12:15:11.579274+00:00_

abstract.tex
appendix.tex
conclusion.tex
discussion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 252
}
```

</details>

---


### Tool result

_source line 748 · 2026-05-22T12:15:15.277185+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements aclrollingreview.org"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

Based on the search results from aclrollingreview.org, here are the key submission guidelines for ACL Rolling Review 2026:

## Page Limits and Format Requirements

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). Sections on ethical considerations and limitations do not count towa
…[truncated 1093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 6629
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-22T12:15:15.378356+00:00_

Web search results for query: "EMNLP 2026 call for papers commitment deadline ARR submission"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"}]

Based on the search results, here are the key details for EMNLP 2026:

## Important Deadlines

The ARR submission deadline for long and short papers is May 25, 2026, and the EMNLP 
…[truncated 879 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 5969
}
```

</details>

---


### Tool call

_source line 750 · 2026-05-22T12:15:27.975413+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-22T12:15:28.227662+00:00_

1	\begin{abstract}
2	LLM benchmark scores are compared across model generations, yet whether individual items measure the same construct over time is rarely tested. Existing contamination detectors validate against web-overlap labels that conflate global exposure with differential functioning. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 items), validated through a semi-synthetic injection framework with cross-subject matching. Between 2023 and 2024 model cohorts, 17.9--31.3\% of items exhibit large temporal DIF (ETS~C, $|\Delta_{\mathrm{MH}}| \geq 1.5$); for MMLU, family-level cluster bootstrap yields a 95\% CI of $[26.7\%, 53.2\%]$, against a random-split baseline of 0.18\%. Web-overlap contamination labels are near-independent of DIF flags (Jaccard $= 0.206$), exposing a category error in prevailing validation methodology. This instability does not threaten aggregate rankings ($\rho \approx 0.997$) but reveals item-level temporal change: a difficulty--direction interaction ($\rho = -0.597$) shows 2024 models gaining on hard items while eroding on easy ones. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-22T12:15:28.228346+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-22T12:15:28.732217+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We use \emph{measurement invariance} to denote the property that test items function identically across groups~\citep{meredith1993invariance}, \emph{differential item functioning} (DIF) as the item-level statistical test for violations, and \emph{temporal measurement instability} as the empirical phenomenon when DIF is detected across time-defined cohorts. Applying Mantel-Haenszel DIF analysis~\citep{holland1988mh} with ETS severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$) between 2023 and 2024 model cohorts---versus 0.18\% under a random-split control. This instability does not threaten benchmark validity ($\rho \approx 0.997$ between full and stable-item rankings); it is diagnostic, revealing which capability dimensions shift across model generations.
5	
6	Contamination detectors---from membership inference~\citep{shi2024mink} to performance-based methods~\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}---validate primarily against web-overlap labels~\citep{li2024contamination} that measure \emph{global exposure}: whether an item exists in publicly accessible training corpora. Such labels do not capture \emph{differential item functioning}: whether an item behaves differently across cohorts with varying exposure or training methodology (\Cref{fig:global_vs_differential}). Direct comparison confirms n
…[truncated 2799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-22T12:15:28.732607+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-22T12:15:30.099254+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees 
…[truncated 9150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 1366
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-22T12:15:30.251578+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool call

_source line 757 · 2026-05-22T12:15:30.252039+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 758 · 2026-05-22T12:15:30.302955+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	As approximate parametric bounds, a Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal Comparability: 31\% Measurement Instability}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%]; family-level cluster bootstrap over 29 families with $\geq$3 members yields CI $[26.7\%, 53.2\%]$, confirming robustness under within-family dependence). Leave-one-family-out analysis confirms that no single non-dominant family drives the signal ($|\Delta\mathrm{C\%}| \leq 2.93$\,pp; \Cref{tab:lofo}). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the
…[truncated 11115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-22T12:15:30.303474+00:00_

Error executing tool read_project_file: 1 validation error for read_project_fileArguments
project
  Field required [type=missing, input_value={'file': 'artifacts/review_issues.yaml'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-22T12:15:37.626516+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-22T12:15:38.631625+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\enlargethispage*{8\baselineskip}
4	
5	\subsection{Implications for Benchmark Temporal Comparability}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF decomposes benchmark differences into impact (ability differences removed by matching, $\sim$2.4~pp), DIF (item-level differences after ability control, $\sim$28--29\% floor, predominantly item-specific), and attribution (underdetermined without training data). In standardized educational testing, ETS~C rates typically range from 5--15\%~\citep{clauser1998dif}; our 31\% rate is 2--6$\times$ higher.
10	
11	\looseness=-1
12	Temporal DIF detects \emph{that} items function differently, not \emph{why}. Three non-mutually-exclusive mechanisms may drive the signal: (1)~differential contamination, where asymmetric training data exposure changes item difficulty for one cohort; (2)~capability evolution, where genuine skill acquisition alters the relationship between ability and item response; (3)~training methodology shifts, where RLHF, chain-of-thought prompting, or other post-training techniques change response patterns independent of raw ability. Distinguishing these requires access to training data, which is unavailable for most models.
13	
14	\looseness=-1
15	Our diagnostic approach complements benchmark reform efforts such as MMLU-CF~\citep{zhao2025mmlucf}, which reconstructs contamination-free items, and dynamic benchmarks that generate novel items per evaluation cycle. DIF monitoring provides a low-cost alternative when reconstruction is infeasible: rather than replacing items, it identifies which existing items remain measurement-invariant.
16	
17	\looseness=-1
18	Expert-annotated ground truth errors~\citep{gema2024mmlu} (313 flagged items in MMLU-Redux, 4{,}802 matched to our item set) show no enrichment among DIF-C items (enrichment $= 0.92\times$, $\varphi = -0.01$, $p = 0.37$), confirming that temporal DIF captures dynamic measurement shifts rather than
…[truncated 1271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-22T12:15:38.632906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-22T12:15:39.135969+00:00_

1	\vspace{-4pt}
2	\section{Conclusion}
3	\label{sec:conclusion}
4	
5	\looseness=-1
6	Across six METABENCH benchmarks, 17.9--31.3\% of items exhibit temporal measurement instability between 2023 and 2024 model cohorts (family-level cluster bootstrap 95\% CI $[26.7\%, 53.2\%]$ for MMLU; random-split baseline $= 0.18\%$). Multiple independent uncertainty methods---cluster bootstrap, design-effect correction, and graduated de-duplication---converge on a robust lower bound of $\sim$27--29\% (\Cref{app:uncertainty}). Web-overlap contamination labels are near-independent of DIF flags (Jaccard $= 0.206$), confirming a category error in prevailing validation methodology that our cross-subject matching framework resolves. Aggregate rankings remain preserved ($\rho \approx 0.997$), but item-level monitoring should accompany score reporting to identify which capability dimensions shift across model generations. We recommend temporal MH-DIF audits whenever $\geq$500 models accumulate (\Cref{sec:disc_protocol}).
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-22T12:15:39.137060+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-22T12:15:39.645477+00:00_

1	\section*{Limitations}
2	
3	\paragraph{Methodological scope.}
4	MH-DIF detects only uniform DIF; logistic regression reveals an additional 24.8\% non-uniform DIF, making 31\% conservative. More fundamentally, DIF detects \emph{that} items function differently but cannot determine \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts. A definitive causal decomposition remains out of reach without access to model training data. The semi-synthetic framework uses binary response flipping (incorrect $\to$ correct) to simulate differential contamination, representing a worst-case uniform exploitation pattern. Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages; detection power under such realistic patterns is untested. The moderate $\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$ reflects sensitivity to severe differential behavior; the framework's primary methodological contribution---cross-subject matching achieving $\Delta\mathrm{FPR} = 0.000$---is a matching strategy property independent of injection realism. Our uniform injection model is difficulty-agnostic, whereas real contamination likely correlates with item difficulty. Difficulty-dependent injection would concentrate DIF on easy items, potentially increasing detection power for that subset while reducing sensitivity to hard-item DIF; the observed difficulty--direction interaction ($\rho = -0.597$) suggests that actual patterns are more complex than uniform models capture.
5	
6	\paragraph{Examinee non-independence.}
7	The MH $\chi^2$ test assumes independent examinees, yet LLMs sharing base models, training data, or architectures violate this assumption. Empirical mitigations partially address this: permutation simulation bounds LD-attributable FPR inflation to ${<}0.001$~pp, and graduated de-duplication ($K{=}20$: C\% $= 29.1\%$) shows family structure does not inflate results. \citet{french2010hierarchical} sho
…[truncated 1882 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 508
}
```

</details>

---


### Tool call

_source line 766 · 2026-05-22T12:15:39.646009+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-22T12:15:40.100684+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues and \citet{oren2024proving} prove contamination through exchangeability tests. Performance-based detectors identify contamination through statistical anomalies \citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique,deng2024investigating}. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (\Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} assessed test set discriminability, and \citet{rodriguez2021evaluation} demonstrat
…[truncated 4362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-22T12:15:40.252004+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 769 · 2026-05-22T12:15:40.302884+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-22T12:15:49.983030+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-22T12:15:50.790111+00:00_

1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini
…[truncated 14613 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-22T12:15:51.142874+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-22T12:15:51.143422+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 774 · 2026-05-22T12:15:51.246866+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 775 · 2026-05-22T12:15:51.449395+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 776 · 2026-05-22T12:15:58.002909+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 777 · 2026-05-22T12:15:58.510795+00:00_

-rw-r--r-- 1 ubuntu ubuntu 635137 May 22 12:11 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 778 · 2026-05-22T12:15:59.016291+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 779 · 2026-05-22T12:15:59.981827+00:00_

# Review Issues Tracker — irt_equated_bench_regen
# Round 14 (Fresh review, 2026-05-22)
# 2 critical in_progress, 9 warning in_progress, 5 info open

# ============================================================
# ROUND 14 — MUST-FIX (CRITICAL)
# ============================================================

- id: "R14-MF1"
  summary: "MMLU 57-subject 多维度结构违反 MH-DIF 匹配假设，辩护不充分"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 14
  last_seen_round: 14
  mentions:
    - round: 14
      reviewers: [1, 2]
      note: "R1 首提 Must-Fix, R2 AGREE。多维测试 total-score matching → spurious DIF 风险。已有反证：within-subject C%=38.1% > cross-subject 31.3%（方向证明 cross-subject 保守）。"
  action_items:
    - round: 14
      action: "补实验: domain-level Cohen's d profile analysis + cross-subject-unique C 项集中度分析"
      assigned_to: "Agent"
      status: in_progress
    - round: 14
      action: "改论文: §3.2 承认多维度限制 + §5/Appendix 辩护段（利用已有 within-subject 反证 + 新实验结果）"
      assigned_to: "Paper Agent"
      status: pending
  resolution: ""
  resolution_round: null

- id: "R14-MF2"
  summary: "Cluster bootstrap CI [26.7%, 53.2%] 跨度极大但被 '~31%' 淡化，三种 uncertainty estimate 不一致"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 14
  last_seen_round: 14
  mentions:
    - round: 14
      reviewers: [1, 2]
      note: "三种 uncertainty methods 不一致: model bootstrap [29.4%,38.1%], cluster bootstrap [26.7%,53.2%], DEFF simple 29.2%, DEFF weighted 13.5%。"
  action_items:
    - round: 14
      action: "改论文: Abstract/Conclusion CI 突出 + Appendix uncertainty 方法对比表（含 de-duplication K=20）+ CI 上界来源说明"
      assigned_to: "Paper Agent"
      status: in_progress
  resolution: ""
  resolution_round: null

# ============================================================
# ROUND 14 — SHOULD-FIX (WARNING)
# ============================================================

- id: "R14-SF1"
  summary: "Discussion (§5) 对 diagnostic 定位论文严重不足"
  category: writing
  severity: war
…[truncated 12813 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 965
}
```

</details>

---


### Tool call

_source line 780 · 2026-05-22T12:15:59.982798+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/config.yaml 2>/dev/null | head -80",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 781 · 2026-05-22T12:16:00.083502+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-22T12:16:06.570803+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-22T12:16:07.024007+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-22T12:16:07.277163+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-22T12:16:07.429153+00:00_

1	% ============================================================
2	% Benchmark Contamination Detection
3	% ============================================================
4	
5	@inproceedings{balloccu2024leak,
6	  title     = {Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source {LLMs}},
7	  author    = {Balloccu, Simone and Schmidtova, Patrícia and Lango, Mateusz and Dusek, Ondrej},
8	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
9	  year      = {2024},
10	  doi       = {10.18653/v1/2024.eacl-long.5},
11	  url       = {https://arxiv.org/abs/2402.03927}
12	}
13	
14	@inproceedings{dekoninck2024constat,
15	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
16	  author    = {Dekoninck, Jasper and Mueller, Mark Niklas and Vechev, Martin},
17	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
18	  year      = {2024},
19	  url       = {https://arxiv.org/abs/2405.16281}
20	}
21	
22	@inproceedings{golchin2024timetravel,
23	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
24	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
25	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
26	  year      = {2024},
27	  url       = {https://arxiv.org/abs/2308.08493}
28	}
29	
30	@inproceedings{li2024contamination,
31	  title     = {An Open-Source Data Contamination Report for Large Language Models},
32	  author    = {Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua},
33	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
34	  year      = {2024},
35	  doi       = {10.18653/v1/2024.findings-emnlp.30},
36	  url       = {https://aclanthology.org/2024.findings-emnlp.30/}
37	}
38	
39	@misc{liang2026dvd,
40	  title         = {{DVD}: A Robust Method for Detecting Variant Conta
…[truncated 379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-22T12:16:45.716788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf",
  "pages": "1-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf",
    "pages": "1-8"
  }
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-22T12:16:46.373432+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf (620.3KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 788 · 2026-05-22T12:17:49.662205+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你负责 **方法严谨性** 审查。\n\n## 论文信息\n- **标题**: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`（各 section 在 `sections/` 子目录）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25 (ARR May cycle)\n- **页数**: Long paper — 正文最多 8 页，参考文献不限页数\n- **Limitations**: 必写，不计入 8 页限制，且不得包含新实验/图表/分析\n- **Ethical considerations**: 可选，不计入页数\n- **模板**: ACL style template，[review] mode\n- **匿名**: Double-blind anonymous review\n- **提交平台**: OpenReview\n- **特殊规则**: EMNLP 和 AACL 共享 ARR May cycle，作者需在提交时声明目标会议（binding）\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **MH-DIF 方法论适用性**：将教育测量的 MH-DIF 应用到 LLM benchmark 评估是否合理？LLM-specific assumptions（local independence violation、examinee non-independence、non-normal ability distribution、multidimensionality）是否被充分讨论和缓解？\n\n2. **统计控制充分性**：temporal C% = 31% 的结论是否经过充分控制？Random-split sanity check、matched-ability analysis、within-family comparison、within-subject DIF、IRT θ-conditioning 等控制实验是否足以排除混淆因素？\n\n3. **Uncertainty quantification**：Model-level bootstrap CI [29.4%, 38.1%]、family-level cluster bootstrap CI [26.7%, 53.2%]、DEFF adjusted C% [13.5%, 29.2%]、graduated de-duplication (K=20: 29.1%) —— 这些 uncertainty estimates 之间的不一致性是否被正确处理和报告？是否有 cherry-picking 的嫌疑？\n\n4. **Semi-synthetic injection framework**：Cross-subject matching 的 ΔFPR=0 保证是否有效？Binary response flipping 作为注入模型的生态效度如何？Multi-subject injection 的 boundary conditions 是否充分讨论？\n\n5. **多维度问题**：MMLU 57 subjects 的多维度结构是否可能产生 spurious DIF？论文提供的三条辩护（domain-level Cohen's d profile、cross-subject vs within-subject κ=0.80、C items 不集中在能力偏移大的 subject）是否充分？\n\n6. **Cross-benchmark validation**：6 个 METABENCH benchmarks 的 replication 是否充分？GSM1K 相关分析（N=33）的统计效力和解读是否合理？\n\n请按以下格式输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条列出，标注 S1, S2, ...）\n- **Weaknesses**（逐条列出，标注 W1, W2, ...，区分 Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度，使用 ARR Overall Assessment 标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你负责 **方法严谨性** 审查。\n\n## 论文信息\n- **标题**: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`（各 section 在 `sections/` 子目录）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25 (ARR May cycle)\n- **页数**: Long paper — 正文最多 8 页，参考文献不限页数\n- **Limitations**: 必写，不计入 8 页限制，且不得包含新实验/图表/分析\n- **Ethical considerations**: 可选，不计入页数\n- **模板**: ACL style template，[review] mode\n- **匿名**: Double-blind anonymous review\n- **提交平台**: OpenReview\n- **特殊规则**: EMNLP 和 AACL 共享 ARR May cycle，作者需在提交时声明目标会议（binding）\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **MH-DIF 方法论适用性**：将教育测量的 MH-DIF 应用到 LLM benchmark 评估是否合理？LLM-specific assumptions（local independence violation、examinee non-independence、non-normal ability distribution、multidimensionality）是否被充分讨论和缓解？\n\n2. **统计控制充分性**：temporal C% = 31% 的结论是否经过充分控制？Random-split sanity check、matched-ability analysis、within-family comparison、within-subject DIF、IRT θ-conditioning 等控制实验是否足以排除混淆因素？\n\n3. **Uncertainty quantification**：Model-level bootstrap CI [29.4%, 38.1%]、family-level cluster bootstrap CI [26.7%, 53.2%]、DEFF adjusted C% [13.5%, 29.2%]、graduated de-duplication (K=20: 29.1%) —— 这些 uncertainty estimates 之间的不一致性是否被正确处理和报告？是否有 cherry-picking 的嫌疑？\n\n4. **Semi-synthetic injection framework**：Cross-subject matching 的 ΔFPR=0 保证是否有效？Binary response flipping 作为注入模型的生态效度如何？Multi-subject injection 的 boundary conditions 是否充分讨论？\n\n5. **多维度问题**：MMLU 57 subjects 的多维度结构是否可能产生 spurious DIF？论文提供的三条辩护（domain-level Cohen's d profile、cross-subject vs within-subject κ=0.80、C items 不集中在能力偏移大的 subject）是否充分？\n\n6. **Cross-benchmark validation**：6 个 METABENCH benchmarks 的 replication 是否充分？GSM1K 相关分析（N=33）的统计效力和解读是否合理？\n\n请按以下格式输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条列出，标注 S1, S2, ...）\n- **Weaknesses**（逐条列出，标注 W1, W2, ...，区分 Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度，使用 ARR Overall Assessment 标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit）"
  }
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-22T12:18:08.609237+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18947
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-22T12:18:08.810957+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你负责 **新颖性与完整性** 审查。\n\n## 论文信息\n- **标题**: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`（各 section 在 `sections/` 子目录）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25 (ARR May cycle)\n- **页数**: Long paper — 正文最多 8 页，参考文献不限页数\n- **Limitations**: 必写，不计入 8 页限制，且不得包含新实验/图表/分析\n- **Ethical considerations**: 可选，不计入页数\n- **模板**: ACL style template，[review] mode\n- **匿名**: Double-blind anonymous review\n- **提交平台**: OpenReview\n- **特殊规则**: EMNLP 和 AACL 共享 ARR May cycle，作者需在提交时声明目标会议（binding）\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **贡献新颖性**：论文声称三个贡献——ground truth meta-critique、semi-synthetic validation framework、temporal measurement instability at scale。每个贡献的新颖性如何？MH-DIF 本身是既有方法，论文声称\"our contribution is the application context\"——这对 EMNLP 2026 的接收标准是否足够？\n\n2. **与 concurrent work 的区分**：Growing Pains (Habba et al., 2026) 做 IRT anchor-item calibration，BHI (Zhu et al., 2026) 做 benchmark health index，Benchmark² (Qian & Huang, 2026) 做 meta-evaluation，MMLU-CF (Zhao et al., 2025) 做 contamination-free reconstruction。论文如何定位自己？\"diagnosis vs reconstruction vs calibration\" 的 framing 是否令人信服？\n\n3. **Related work 覆盖度**：Contamination detection、IRT in LLM evaluation、DIF methodology、benchmark quality and design 四个维度的覆盖是否全面？是否有重要遗漏？\n\n4. **写作质量与叙事**：\n   - Abstract 信息密度是否过高（数字过多）？\n   - 术语一致性：temporal measurement instability / temporal DIF / measurement invariance 的使用是否清晰区分？\n   - Introduction 的叙事流是否清晰？贡献列表是否精准？\n   - Discussion (§5) 是否充分？对一篇 diagnostic 论文来说，3 个 subsection（temporal comparability + ground truth + audit protocol）是否足够？\n\n5. **实际影响力**：\n   - ρ ≈ 0.997 说明 aggregate ranking 几乎不受影响——那么 31% DIF 的实际意义是什么？论文对 \"diagnostic lens rather than quality filter\" 的 framing 是否足以支撑 impact？\n   - 推荐的 DIF Audit Protocol（Monitor/Flag/Act）是否可行？是否有足够的 empirical grounding？\n\n6. **格式合规性**：页数（正文 ≤8）、Limitations 章节、匿名性、引用格式。\n\n请按以下格式输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条列出，标注 S1, S2, ...）\n- **Weaknesses**（逐条列出，标注 W1, W2, ...，区分 Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度，使用 ARR Overall Assessment 标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你负责 **新颖性与完整性** 审查。\n\n## 论文信息\n- **标题**: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`（各 section 在 `sections/` 子目录）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_8/submitted.pdf`\n\n## Venue 要求\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25 (ARR May cycle)\n- **页数**: Long paper — 正文最多 8 页，参考文献不限页数\n- **Limitations**: 必写，不计入 8 页限制，且不得包含新实验/图表/分析\n- **Ethical considerations**: 可选，不计入页数\n- **模板**: ACL style template，[review] mode\n- **匿名**: Double-blind anonymous review\n- **提交平台**: OpenReview\n- **特殊规则**: EMNLP 和 AACL 共享 ARR May cycle，作者需在提交时声明目标会议（binding）\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **贡献新颖性**：论文声称三个贡献——ground truth meta-critique、semi-synthetic validation framework、temporal measurement instability at scale。每个贡献的新颖性如何？MH-DIF 本身是既有方法，论文声称\"our contribution is the application context\"——这对 EMNLP 2026 的接收标准是否足够？\n\n2. **与 concurrent work 的区分**：Growing Pains (Habba et al., 2026) 做 IRT anchor-item calibration，BHI (Zhu et al., 2026) 做 benchmark health index，Benchmark² (Qian & Huang, 2026) 做 meta-evaluation，MMLU-CF (Zhao et al., 2025) 做 contamination-free reconstruction。论文如何定位自己？\"diagnosis vs reconstruction vs calibration\" 的 framing 是否令人信服？\n\n3. **Related work 覆盖度**：Contamination detection、IRT in LLM evaluation、DIF methodology、benchmark quality and design 四个维度的覆盖是否全面？是否有重要遗漏？\n\n4. **写作质量与叙事**：\n   - Abstract 信息密度是否过高（数字过多）？\n   - 术语一致性：temporal measurement instability / temporal DIF / measurement invariance 的使用是否清晰区分？\n   - Introduction 的叙事流是否清晰？贡献列表是否精准？\n   - Discussion (§5) 是否充分？对一篇 diagnostic 论文来说，3 个 subsection（temporal comparability + ground truth + audit protocol）是否足够？\n\n5. **实际影响力**：\n   - ρ ≈ 0.997 说明 aggregate ranking 几乎不受影响——那么 31% DIF 的实际意义是什么？论文对 \"diagnostic lens rather than quality filter\" 的 framing 是否足以支撑 impact？\n   - 推荐的 DIF Audit Protocol（Monitor/Flag/Act）是否可行？是否有足够的 empirical grounding？\n\n6. **格式合规性**：页数（正文 ≤8）、Limitations 章节、匿名性、引用格式。\n\n请按以下格式输出审稿意见：\n- **Summary**（2-3 句）\n- **Strengths**（逐条列出，标注 S1, S2, ...）\n- **Weaknesses**（逐条列出，标注 W1, W2, ...，区分 Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者回答的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度，使用 ARR Overall Assessment 标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit）"
  }
}
```

</details>

---


### Tool call

_source line 791 · 2026-05-22T12:18:09.976973+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 792 · 2026-05-22T12:18:10.731094+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1920
}
```

</details>

---


### Tool result

_source line 793 · 2026-05-22T12:18:12.958051+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 2981
}
```

</details>

---


### Assistant

_source line 794 · 2026-05-22T12:18:27.703596+00:00_

已全部派发完毕：

- **Reviewer 1**（方法严谨性）— 已启动 ✓
- **Reviewer 2**（新颖性/完整性）— 已启动 ✓
- **视觉审查 Agent** — 已启动 ✓

等待两位 Reviewer 返回初审意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 74

## Round 74

2 recorded events


### User

_source line 795 · 2026-05-22T12:23:45.344189+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 方法严谨性审查完成

### 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**置信度**: 4/5
**一句话总结**: 将 MH-DIF 引入 LLM 基准评估是有价值的方法论创新，但 headline claim "31% temporal DIF" 与多个 robustness 下界（DEFF-adjusted 13.5%）之间的巨大落差未被充分讨论，多维度混淆也未完全排除。

### 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | MH-DIF 框架本身合理，控制实验设计周到，但 DEFF 处理、多维度混淆、temporal vs. cohort 区分存在未完全消解的疑虑 |
| Excitement | 3.5/5 | 心理测量学方法引入 LLM benchmark 评估是新颖且及时的，但实际建议（DIF 监测、item retirement）偏增量 |
| Reproducibility | 4/5 | 代码和审计脚本公开，METABENCH 数据可获取 |

### Must-Fix 问题（3 个）

**N1** [critical] DEFF-adjusted 下界与 headline claim 的严重不一致被掩盖
- 位置：Section 4.2 headline "31% C%" vs. Appendix C Table 8（DEFF = 12.79, adjusted C% = 13.5%）
- 论文通篇以 "31%" 为核心 claim（Abstract, Section 4.2, Conclusion），但 DEFF = 12.79 意味着有效样本量仅约 155 个独立模型。DEFF-adjusted 下界 13.5% 不到 headline 的一半，被放在附录中以 "conservative" 标签处理。四种不确定性估计（model bootstrap [29.4%, 38.1%], family cluster bootstrap [26.7%, 53.2%], DEFF [13.5%, 29.2%], de-duplication K=20: 29.1%）之间缺乏明确的优先级层次。
- 建议：正文中直接报告 DEFF 范围；建立估计优先级；考虑以区间替代单点 headline。

**N2** [critical] 多维度混淆未被充分排除
- 位置：Section 3.2（total-score matching）、Section 4.1（三条辩护）、Appendix A.1
- MMLU 57 subjects 高度多维度，论文自承 poor unidimensional model fit。total-score matching 在多维度测试中当 cohort 间 domain-specific ability shift 不均匀时产生 spurious DIF（Ackerman 1992）。三条辩护各有漏洞：Cohen's d range 0.146-0.329 不算 "nearly flat"（Humanities 是 Other 的 2.25 倍）；κ=0.80 意味着 20% 不一致可能恰是多维度 artifact；C items 不集中是必要非充分条件。
- 建议：分析 κ discordant items 的 domain 分布；考虑 SIBTEST 或 logistic regression with domain covariates；量化多维度混淆的潜在幅度。

**N3** [critical] "Temporal measurement instability" 因果归因过度
- 位置：Title、Abstract、Section 5.1
- "Temporal measurement instability" 暗示 items 测量属性变化，但同样的数据可解读为不同代 LLM 在不同 items 上能力 profile 合理地不同。论文列出三种机制但无法区分相对贡献。在教育测量中 DIF items 需要 expert review 而非自动 flagging。
- 建议：弱化因果归因，讨论 DIF ≠ item defect 的可能性。

### Should-Fix 问题（4 个）

**W1** [warning] Semi-synthetic injection 的 ecological validity 有限——binary response flipping 是极端模型，real contamination 更 nuanced；ΔFPR=0 仅对特定协议有效。

**W2** [warning] GSM1K 分析 N=33, r=−0.17——效力不足，"caveat + still cite" 模式有 cherry-picking 嫌疑。

**W3** [warning] Random-split sanity check 仅在 2023 cohort 内进行，验证 null FPR 而非排除替代解释。缺少 2024 cohort 内 random split。

**W4** [warning] 24.8% non-uniform DIF 对 MH 方法的影响未讨论——MH 是 uniform DIF 方法，约 1/4 items 的 DIF 幅度可能被误估。

### 小问题
- M1: Table 5 Cohen's d 正文引用数字与表格不一致
- M2: 时间 cutoff 定义模糊
- M3: "C%" 和 "temporal C%" 术语未统一
- M4: "enrichment ratio" 首次使用缺乏直觉解释

### Questions
- Q1: DEFF-adjusted 13.5% vs headline 31%，哪个更接近真实效应？
- Q2: κ discordant 20% items 是否在高 Cohen's d domain 中 over-represented？
- Q3: Within-family C%=61.5% 远高于 overall 31%，是否暗示 family-specific 变化比 "temporal instability" 更好地解释 DIF？
- Q4: Partial improvement contamination 下 sensitivity 如何？
- Q5: 是否考虑 purified MH（当 31% items 有 DIF 时 matching variable 已被污染）？

### Missing References
- Clauser, Mazor, & Hambleton (1993) — purified subtest matching
- Penfield & Algina (2006) — multidimensional DIF 框架
- Zumbo (1999) — logistic regression DIF 方法
- Bolt & Stout (1996) — multidimensionality-based DIF 理论

### 主要优势
- S1: MH-DIF + ETS classification 引入 LLM 评估是方法论创新
- S2: 规模印象深刻（5,227 models × 12,508 items），数据公开可复现
- S3: 五层控制实验（random split、matched ability、within-family、within-subject、IRT θ）系统周到
- S4: Cross-subject matching 设计技术上巧妙
- S5: 6 benchmarks cross-validation 增强 generalizability
- S6: 写作质量高，图表信息密度好

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 796 · 2026-05-22T12:23:55.792073+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 75

## Round 75

2 recorded events


### User

_source line 797 · 2026-05-22T12:23:58.396146+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：本轮审查识别了 3 个 Must-Fix（DEFF 透明度、多维度混淆、因果归因过度）、4 个 Should-Fix（injection ecological validity、GSM1K 效力不足、random-split 对照局限、non-uniform DIF 影响）和 4 个 Minor 问题。Overall 评分 3.5/5 (Borderline Conference)——核心方法论贡献有价值，但需要在 DEFF 报告透明度和多维度控制方面做实质性修改才能达到 Conference 接收水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 798 · 2026-05-22T12:24:04.865564+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 76

## Round 76

6 recorded events


### User

_source line 799 · 2026-05-22T12:24:15.576018+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（Round 1）—— 新颖性与完整性

### 总体评分
**Overall**: 3.5 (Borderline Conference)
**Confidence**: 4/5
**一句话总结**: 对 LLM benchmark 的大规模 psychometric 审计在实证上扎实且控制充分，但方法论贡献有限（MH-DIF 为既有方法），ρ ≈ 0.997 削弱了实际影响力叙事，且 concurrent work 密集的领域中 "application context" 的新颖性对主会议接收标准来说偏弱。

### 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 方法论基础扎实；6 种 alternative explanations 系统排除；semi-synthetic framework 设计合理（ΔFPR=0 保证）；三角验证充分。主要不确定性：DEFF weighted 估计将 C% 压至 13.5% |
| Excitement | 3/5 | 重要 gap 但概念新颖性有限——标准 psychometric 工具的 application；ρ=0.997 使 practical urgency 不足；ground truth meta-critique 最有洞察力 |
| Reproducibility | 4/5 | 匿名代码仓库已提供；METABENCH 公开可用；方法描述详尽 |

### Summary
本文将 Mantel-Haenszel DIF 分析（含 ETS 严重性分类）应用于 METABENCH 的 5,227 个模型 × 6 个 benchmark 的响应矩阵，发现 17.9–31.3% 的 items 在 2023–2024 时间跨度内展现 large temporal DIF（ETS C）。论文同时指出 web-overlap contamination labels 与 DIF flags 近乎独立（Jaccard=0.206），提出 cross-subject matching 的 semi-synthetic validation framework，并建议三级 DIF Audit Protocol。实证工作广泛且控制充分，但核心方法为既有教育测量工具的直接应用，aggregate ranking 的高度鲁棒性（ρ ≈ 0.997）削弱了 impact 叙事。

### Strengths

**S1** [Major] 实证规模和控制的系统性令人印象深刻。5,227 个模型、12,508 items 的分析规模远超典型 DIF 应用；6 种 alternative explanation 逐一排除。Matched-ability 分析将 ability mismatch 的贡献量化为 ~2.4 pp（§4.2），令人信服。

**S2** [Major] Ground truth meta-critique 是最有知识贡献的部分。Global exposure vs. differential functioning 的概念区分（Figure 1）清晰有力；enrichment ratio = 0.964 + Jaccard = 0.206 为 contamination detection 领域提供了重要方法论 caveat。

**S3** [Moderate] Cross-subject matching 的 ΔFPR = 0 构造性保证简洁优雅，multi-subject injection robustness（Table 6）展示了 graceful degradation。

**S4** [Moderate] Uncertainty quantification 的透明度值得肯定（Appendix D, Table 8）：五种不同假设下的估计结果并列呈现。

**S5** [Minor] Cross-benchmark validation 跨 6 个 benchmark 的一致性（Table 3）提供了有意义的 external validity。

### Weaknesses

#### Must-Fix

**W1** [Critical] 新颖性的核心张力未得到充分解决
- §2 明确承认 "We do not modify the MH procedure; our contribution is the application context"
- 三个 contributions 实质上都是 empirical findings，而非方法论创新
- 在 Growing Pains / BHI / Benchmark² / MMLU-CF 组成的 concurrent work 密集区域中，纯 "application context" 的新颖性门槛需要额外论证
- 建议：(a) 将 LLM-specific challenges 的处理前置为方法论贡献；(b) 强调 cross-subject matching 在 multi-domain contamination 场景下的理论保证；(c) 或更坦诚地定位为 Findings-track

**W2** [Critical] ρ ≈ 0.997 与 "31% instability" 之间的张力未充分调和
- aggregate ranking 几乎不受影响 → 对主要使用场景（leaderboard comparison）影响有限
- "diagnostic lens rather than quality filter" 的 framing 实质上承认了问题的有限影响
- §5.1 列出三种可能机制但立刻放弃因果推理
- 缺少 case study 展示 item-level DIF 的实际影响
- 建议：补充 concrete case study + 量化 subject-level ranking 影响 + 深化因果推理讨论

#### Should-Fix

**W3** [Warning] DEFF-adjusted C% (13.5–29.2%) 的 wide range 在主文中被低估讨论。31% 在最保守 correction 下可能只有 13.5%，这需要在主文中更充分讨论。

**W4** [Warning] Discussion §5 depth 不足（约半页）。§5.1 放弃因果推理；§5.3 的 15%/25% 阈值仅由 Figure 6 支撑；缺少 benchmark lifecycle management 的更广阔讨论。

**W5** [Warning] Abstract 信息密度过高（9+ 个数字），建议保留 3-4 个关键数字。

**W6** [Warning] 术语一致性需改进——"temporal measurement instability" / "temporal DIF" / "measurement invariance" / "temporal comparability" 的使用层次模糊。

#### Minor
- M1: Figure 5 (GSM1K, N=33) 太小，建议压缩或移入附录
- M2: Table 1 "C% (web-clean)" 对 within-family/random split 标 "--" 但未解释原因
- M3: §3.4 Remark 格式像 proposition 但无正式证明

### Questions

**Q1**: DEFF weighted-mean 的 effective cluster size 254.5 在 LLM 语境中的合理性？
**Q2**: difficulty–direction interaction ρ=-0.597 是否更支持 capability evolution 而非 contamination？如果是，对 contamination-focused framing 有何影响？
**Q3**: 实际场景中 contamination 的 cross-subject 程度如何？Table 6 k=20 的 ΔFPR=0.069 是否被 Limitations 低估？
**Q4**: 24.8% non-uniform DIF 的 item-level pattern？

### Missing References
- MR1 [Should-cite]: Gema et al. (2024) MMLU-Redux 的 item quality errors 与 DIF 交互关系值得在 Related Work 中更显式讨论
- MR2 [Consider]: TinyBenchmarks 的 item selection 与 DIF flagging 的关系
- MR3 [Consider]: Multi-group CFA measurement invariance 文献（Cheung & Rensvold 2002）
- MR4 [Consider]: Yang et al. (2023) "Rethinking benchmark and contamination"

### Overall Assessment
Rating: 3.5 / 5 (Borderline Conference), Confidence: 4/5

高质量实证研究——规模大、控制全、透明度好。Ground truth meta-critique 提供了重要 caveat。核心弱点：方法论贡献有限，31% DIF 与 ρ=0.997 的张力削弱 impact story，Discussion 对 diagnostic 价值的阐释不够深入。建议补充 case study、深化因果推理、调整 abstract 密度。充分修改后有望达到 Conference 水平；否则更适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-22T12:25:04.094624+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 **Reviewer 1（方法严谨性）** 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — 方法严谨性审查\n\n### Overall: 3.5 / 5 (Borderline Conference), Confidence: 4/5\n\n### Must-Fix（3 个）\n\n**N1** [critical] DEFF-adjusted 下界与 headline claim 的严重不一致被掩盖\n- 论文通篇以 \"31%\" 为核心 claim（Abstract, Section 4.2, Conclusion），但 DEFF = 12.79 意味着有效样本量仅约 155 个独立模型。DEFF-adjusted 下界 13.5% 不到 headline 的一半，被放在附录中以 \"conservative\" 标签处理。四种不确定性估计（model bootstrap [29.4%, 38.1%], family cluster bootstrap [26.7%, 53.2%], DEFF [13.5%, 29.2%], de-duplication K=20: 29.1%）之间缺乏明确的优先级层次。\n\n**N2** [critical] 多维度混淆未被充分排除\n- MMLU 57 subjects 高度多维度，论文自承 poor unidimensional model fit。total-score matching 在多维度测试中当 cohort 间 domain-specific ability shift 不均匀时产生 spurious DIF（Ackerman 1992）。三条辩护各有漏洞：Cohen's d range 0.146-0.329 不算 \"nearly flat\"（Humanities 是 Other 的 2.25 倍）；κ=0.80 意味着 20% 不一致可能恰是多维度 artifact；C items 不集中是必要非充分条件。\n\n**N3** [critical] \"Temporal measurement instability\" 因果归因过度\n- \"Temporal measurement instability\" 暗示 items 测量属性变化，但同样的数据可解读为不同代 LLM 在不同 items 上能力 profile 合理地不同。论文列出三种机制但无法区分相对贡献。\n\n### Should-Fix（4 个）\n\n**W1** [warning] Semi-synthetic injection 的 ecological validity 有限——binary response flipping 是极端模型。\n\n**W2** [warning] GSM1K 分析 N=33, r=−0.17——效力不足，\"caveat + still cite\" 模式有 cherry-picking 嫌疑。\n\n**W3** [warning] Random-split sanity check 仅在 2023 cohort 内进行，缺少 2024 cohort 内 random split。\n\n**W4** [warning] 24.8% non-uniform DIF 对 MH 方法的影响未讨论。\n\n### Questions\n- Q1: DEFF-adjusted 13.5% vs headline 31%，哪个更接近真实效应？\n- Q2: κ discordant 20% items 是否在高 Cohen's d domain 中 over-represented？\n- Q3: Within-family C%=61.5% 远高于 overall 31%，是否暗示 family-specific 变化比 \"temporal instability\" 更好地解释 DIF？\n- Q4: Partial improvement contamination 下 sensitivity 如何？\n- Q5: 是否考虑 purified MH（当 31% items 有 DIF 时 matching variable 已被污染）？\n\n### Missing References\n- Clauser, Mazor, & Hambleton (1993) — purified subtest matching\n- Penfield & Algina (2006) — multidimensional DIF 框架\n- Zumbo (1999) — logistic regression DIF 方法\n- Bolt & Stout (1996) — multidimensionality-based DIF 理论\n\n---\n\n请对上述每条 Must-Fix、Should-Fix 和 Question 逐一回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 **Reviewer 1（方法严谨性）** 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — 方法严谨性审查\n\n### Overall: 3.5 / 5 (Borderline Conference), Confidence: 4/5\n\n### Must-Fix（3 个）\n\n**N1** [critical] DEFF-adjusted 下界与 headline claim 的严重不一致被掩盖\n- 论文通篇以 \"31%\" 为核心 claim（Abstract, Section 4.2, Conclusion），但 DEFF = 12.79 意味着有效样本量仅约 155 个独立模型。DEFF-adjusted 下界 13.5% 不到 headline 的一半，被放在附录中以 \"conservative\" 标签处理。四种不确定性估计（model bootstrap [29.4%, 38.1%], family cluster bootstrap [26.7%, 53.2%], DEFF [13.5%, 29.2%], de-duplication K=20: 29.1%）之间缺乏明确的优先级层次。\n\n**N2** [critical] 多维度混淆未被充分排除\n- MMLU 57 subjects 高度多维度，论文自承 poor unidimensional model fit。total-score matching 在多维度测试中当 cohort 间 domain-specific ability shift 不均匀时产生 spurious DIF（Ackerman 1992）。三条辩护各有漏洞：Cohen's d range 0.146-0.329 不算 \"nearly flat\"（Humanities 是 Other 的 2.25 倍）；κ=0.80 意味着 20% 不一致可能恰是多维度 artifact；C items 不集中是必要非充分条件。\n\n**N3** [critical] \"Temporal measurement instability\" 因果归因过度\n- \"Temporal measurement instability\" 暗示 items 测量属性变化，但同样的数据可解读为不同代 LLM 在不同 items 上能力 profile 合理地不同。论文列出三种机制但无法区分相对贡献。\n\n### Should-Fix（4 个）\n\n**W1** [warning] Semi-synthetic injection 的 ecological validity 有限——binary response flipping 是极端模型。\n\n**W2** [warning] GSM1K 分析 N=33, r=−0.17——效力不足，\"caveat + still cite\" 模式有 cherry-picking 嫌疑。\n\n**W3** [warning] Random-split sanity check 仅在 2023 cohort 内进行，缺少 2024 cohort 内 random split。\n\n**W4** [warning] 24.8% non-uniform DIF 对 MH 方法的影响未讨论。\n\n### Questions\n- Q1: DEFF-adjusted 13.5% vs headline 31%，哪个更接近真实效应？\n- Q2: κ discordant 20% items 是否在高 Cohen's d domain 中 over-represented？\n- Q3: Within-family C%=61.5% 远高于 overall 31%，是否暗示 family-specific 变化比 \"temporal instability\" 更好地解释 DIF？\n- Q4: Partial improvement contamination 下 sensitivity 如何？\n- Q5: 是否考虑 purified MH（当 31% items 有 DIF 时 matching variable 已被污染）？\n\n### Missing References\n- Clauser, Mazor, & Hambleton (1993) — purified subtest matching\n- Penfield & Algina (2006) — multidimensional DIF 框架\n- Zumbo (1999) — logistic regression DIF 方法\n- Bolt & Stout (1996) — multidimensionality-based DIF 理论\n\n---\n\n请对上述每条 Must-Fix、Should-Fix 和 Question 逐一回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 801 · 2026-05-22T12:25:16.776214+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12681
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-22T12:25:17.680345+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 **Reviewer 2（新颖性与完整性）** 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — 新颖性与完整性审查\n\n### Overall: 3.5 (Borderline Conference), Confidence: 4/5\n\n### Must-Fix（2 个）\n\n**W1** [Critical] 新颖性的核心张力未得到充分解决\n- §2 明确承认 \"We do not modify the MH procedure; our contribution is the application context\"\n- 三个 contributions 实质上都是 empirical findings，而非方法论创新\n- 在 Growing Pains / BHI / Benchmark² / MMLU-CF 组成的 concurrent work 密集区域中，纯 \"application context\" 的新颖性门槛需要额外论证\n- 建议：将 LLM-specific challenges 的处理前置为方法论贡献；强调 cross-subject matching 在 multi-domain contamination 场景下的理论保证；或更坦诚地定位为 Findings-track\n\n**W2** [Critical] ρ ≈ 0.997 与 \"31% instability\" 之间的张力未充分调和\n- aggregate ranking 几乎不受影响 → 对主要使用场景（leaderboard comparison）影响有限\n- \"diagnostic lens rather than quality filter\" 的 framing 实质上承认了问题的有限影响\n- §5.1 列出三种可能机制但立刻放弃因果推理\n- 缺少 case study 展示 item-level DIF 的实际影响\n\n### Should-Fix（4 个）\n\n**W3** [Warning] DEFF-adjusted C% (13.5–29.2%) 的 wide range 在主文中被低估讨论。\n\n**W4** [Warning] Discussion §5 depth 不足（约半页）。§5.1 放弃因果推理；§5.3 的 15%/25% 阈值仅由 Figure 6 支撑。\n\n**W5** [Warning] Abstract 信息密度过高（9+ 个数字）。\n\n**W6** [Warning] 术语一致性需改进。\n\n### Questions\n- Q1: DEFF weighted-mean 的 effective cluster size 254.5 在 LLM 语境中的合理性？\n- Q2: difficulty–direction interaction ρ=-0.597 是否更支持 capability evolution 而非 contamination？\n- Q3: 实际场景中 contamination 的 cross-subject 程度如何？Table 6 k=20 的 ΔFPR=0.069 是否被 Limitations 低估？\n- Q4: 24.8% non-uniform DIF 的 item-level pattern？\n\n### Missing References\n- MR1: Gema et al. (2024) MMLU-Redux 的 item quality errors 与 DIF 交互\n- MR2: TinyBenchmarks 的 item selection 与 DIF flagging 的关系\n- MR3: Multi-group CFA measurement invariance（Cheung & Rensvold 2002）\n- MR4: Yang et al. (2023) \"Rethinking benchmark and contamination\"\n\n---\n\n请对上述每条 Must-Fix、Should-Fix 和 Question 逐一回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 **Reviewer 2（新颖性与完整性）** 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — 新颖性与完整性审查\n\n### Overall: 3.5 (Borderline Conference), Confidence: 4/5\n\n### Must-Fix（2 个）\n\n**W1** [Critical] 新颖性的核心张力未得到充分解决\n- §2 明确承认 \"We do not modify the MH procedure; our contribution is the application context\"\n- 三个 contributions 实质上都是 empirical findings，而非方法论创新\n- 在 Growing Pains / BHI / Benchmark² / MMLU-CF 组成的 concurrent work 密集区域中，纯 \"application context\" 的新颖性门槛需要额外论证\n- 建议：将 LLM-specific challenges 的处理前置为方法论贡献；强调 cross-subject matching 在 multi-domain contamination 场景下的理论保证；或更坦诚地定位为 Findings-track\n\n**W2** [Critical] ρ ≈ 0.997 与 \"31% instability\" 之间的张力未充分调和\n- aggregate ranking 几乎不受影响 → 对主要使用场景（leaderboard comparison）影响有限\n- \"diagnostic lens rather than quality filter\" 的 framing 实质上承认了问题的有限影响\n- §5.1 列出三种可能机制但立刻放弃因果推理\n- 缺少 case study 展示 item-level DIF 的实际影响\n\n### Should-Fix（4 个）\n\n**W3** [Warning] DEFF-adjusted C% (13.5–29.2%) 的 wide range 在主文中被低估讨论。\n\n**W4** [Warning] Discussion §5 depth 不足（约半页）。§5.1 放弃因果推理；§5.3 的 15%/25% 阈值仅由 Figure 6 支撑。\n\n**W5** [Warning] Abstract 信息密度过高（9+ 个数字）。\n\n**W6** [Warning] 术语一致性需改进。\n\n### Questions\n- Q1: DEFF weighted-mean 的 effective cluster size 254.5 在 LLM 语境中的合理性？\n- Q2: difficulty–direction interaction ρ=-0.597 是否更支持 capability evolution 而非 contamination？\n- Q3: 实际场景中 contamination 的 cross-subject 程度如何？Table 6 k=20 的 ΔFPR=0.069 是否被 Limitations 低估？\n- Q4: 24.8% non-uniform DIF 的 item-level pattern？\n\n### Missing References\n- MR1: Gema et al. (2024) MMLU-Redux 的 item quality errors 与 DIF 交互\n- MR2: TinyBenchmarks 的 item selection 与 DIF flagging 的关系\n- MR3: Multi-group CFA measurement invariance（Cheung & Rensvold 2002）\n- MR4: Yang et al. (2023) \"Rethinking benchmark and contamination\"\n\n---\n\n请对上述每条 Must-Fix、Should-Fix 和 Question 逐一回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 803 · 2026-05-22T12:25:19.190941+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1510
}
```

</details>

---


### Assistant

_source line 804 · 2026-05-22T12:25:29.951641+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 77

## Round 77

2 recorded events


### User

_source line 805 · 2026-05-22T12:25:32.599875+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**3.5 (Borderline Conference)**。论文在实证层面做得扎实（规模大、控制全、transparency 好），ground truth meta-critique 有知识贡献。但两个关键弱点影响接收决定：(1) 方法论贡献有限——MH-DIF 为 1988 年的既有方法，论文自己承认 "our contribution is the application context"；(2) ρ ≈ 0.997 与 31% DIF 之间的张力削弱了 impact narrative，需要更强的实际影响论证。如果能深化 Discussion 的因果推理、补充 item-level case study、并将 DEFF 不确定性更充分地纳入主文讨论，有望提升至 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 806 · 2026-05-22T12:25:37.506350+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 78

## Round 78

2 recorded events


### User

_source line 807 · 2026-05-22T12:27:25.038530+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 对 Reviewer 2 的交叉回应

### 回应总览
R2 的 10 个审查点中，**AGREE 9 个、REBUT 1 个**（MR2 TinyBenchmarks 不构成 missing reference）。

### 核心共识（两位 Reviewer 独立收敛）

1. **DEFF / uncertainty reporting**（R1-N1 ≈ R2-W3）：headline 31% 与 DEFF-adjusted 13.5% 的落差必须在正文中透明报告
2. **ρ ≈ 0.997 vs 31% 张力**（R2-W2，R1 认同）：aggregate ranking 几乎不变→ 31% instability 的 practical impact 需要更具体的 use case 论证
3. **因果归因过度**（R1-N3 ≈ R2-W2）：observational DIF 无法支撑 "measurement instability" 的因果归因
4. **多维度混淆**（R1-N2，R2-MR3 间接触及）：CFA measurement invariance 或 SIBTEST 可加强辩护

### 关键补充
- R2-Q2 difficulty–direction ρ=−0.597 更支持 capability evolution 而非 contamination——与 R1-N3 因果归因关切一致
- R2-Q3 Table 6 k=20 ΔFPR=0.069 被 Limitations 低估——R1 同意 6.9% FPR inflation 在部署中 non-negligible
- R2-W1 novelty tension：R1 认为 cross-subject matching 是真正的方法论贡献，但需更显著前置

### 评分维持
Overall: 3.5 (Borderline Conference), Confidence: 4/5
两位 Reviewer 独立给出相同分数，核心关切高度一致。解决上述四组问题后可达 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 808 · 2026-05-22T12:27:30.574225+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 79

## Round 79

2 recorded events


### User

_source line 809 · 2026-05-22T12:27:33.215393+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。R2 的 10 个点中 AGREE 9 个、REBUT 1 个（MR2），两位 Reviewer 在 DEFF reporting、ρ vs 31% 张力、因果归因、多维度混淆四个核心问题上独立收敛。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 810 · 2026-05-22T12:27:40.871604+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 80

## Round 80

8 recorded events


### User

_source line 811 · 2026-05-22T12:28:11.353590+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应

### Must-Fix 回应

**[AGREE] R1-N1: DEFF-adjusted 下界与 headline claim 的不一致**
同意这是重要问题（我的 W3 提出了相同关切）。但 "掩盖" 一词偏强——论文在 Appendix D Table 8 展示了所有五种估计。三种独立方法（cluster bootstrap 26.7%、simple DEFF 29.2%、de-duplication K=20 29.1%）收敛于 ~27–29%，使 weighted DEFF 的 13.5% 更可能是过度保守。建议主文将 headline claim 调整为 "~27–31%" 范围。

**[REBUT] R1-N2: 多维度混淆未被充分排除**
核心论点成立但包含两个事实性错误：
1. R1 称 "Cohen's d range 0.146–0.329" 且 "Humanities 是 Other 的 2.25 倍"——实际数据（Appendix B Table 5）为 STEM=0.261, Humanities=0.159, Social Science=0.147, Other=0.146。Range=0.115，Humanities/Other=1.09（非 2.25）。所有 d 值在 small effect size 范围内（<0.3）。
2. κ=0.80 的 20% 不一致解读忽略了方向性证据：cross-subject 比 within-subject 多产生 2.7 pp C items，这是 multidimensional confound 的上界。
建议降为 Should-Fix。

**[AGREE] R1-N3: "Temporal measurement instability" 因果归因过度**
同意。补充：difficulty–direction interaction ρ=−0.597 更支持 capability evolution 假说，进一步削弱 contamination-focused 的 instability framing。

### Should-Fix 回应

**[AGREE] R1-W1**: 同意 ecological validity 有限，但 ΔFPR=0 保证独立于 injection realism。
**[REBUT] R1-W2**: R1 引用 "r=−0.17" 是事实性错误——论文报告 r=−0.478, p=0.005（§4.7 + Figure 5），且 Cook's D robustness check 系统完整。"cherry-picking" 指控基于错误数值，不成立。
**[AGREE] R1-W3**: 补充 2024 cohort random split 成本极低，建议添加。
**[AGREE] R1-W4**: 24.8% non-uniform DIF 的 pattern 分析缺失，我也提出了相同问题（我的 Q4）。

### Questions 回应
- Q1: ~27–29% 更接近真实，weighted DEFF 的 $\bar{m}$=254.5 在 LLM 语境中过于极端
- Q2: 值得检查但注意 STEM d=0.261 仍在 small effect 范围
- Q3: [REBUT] 论文 §4.4 已回答——matched-ability 将 within-family 从 61.3% 降至 28.3%，与 temporal matched value 28.9% 高度一致
- Q4: 合理，值得作为 future work
- Q5: [REBUT] 论文的 cross-subject matching 实质上就是 purified MH 的 LLM 改编（§3.2 明确引用 Swaminathan and Rogers 1990），R1 似乎忽略了

### Missing References 回应
- Zumbo 1999 已被引用（§2 Related Work），R1 遗漏检查有误
- Penfield & Algina 2006、Bolt & Stout 1996 建议补充
- Clauser et al. 1993 可考虑但非必须（同年文献 donoghue1993mh 已引用）

### R2 对 R1 总评的评估
R1 的审稿整体严谨，特别是 N1（DEFF uncertainty）和 N3（因果归因）是真正重要的问题。但 N2 的多维度论证包含事实性错误（Cohen's d 数值和比例），W2 的 GSM1K 指控基于错误的 correlation 值。建议 AC 注意这些数据不一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-22T12:28:45.601836+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-22T12:28:45.903645+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T12:18:12.154027+00:00\", \"completed_at\": \"2026-05-22T12:21:12.854066+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-5\", \"message\": \"连续 3 页纯文本，无任何 display item（figure/table/display equation）。这是 Method 章节（§2 Related Work 尾部 → §3 Method → §3.4 Semi-Synthetic Framework），虽然包含 MH-DIF 公式，但均为 inline math 而非 display equation，视觉上单调。建议：将关键公式（如 α_MH 和 Δ_MH 定义）改为 display equation 以打破纯文本节奏，或将 Table 1 从 p6 提前至 p5（§3.3 Cohort Designs 附近）\"}, {\"severity\": \"warning\", \"dimension\": \"page 16\", \"message\": \"Figure 6 上方约 1/3 页面为空白，整页内容仅占约 60%。作为论文最后一页，空间利用不充分。建议：调整 figure 尺寸或将部分附录文字内容移至此页\"}, {\"severity\": \"info\", \"dimension\": \"pages 3-5\", \"message\": \"主文 Method 段没有用到任何 display equation（所有公式均为 inline），降低了数学内容的视觉锚定效果。MH odds ratio α_MH、ETS delta Δ_MH 等核心定义适合提升为 display equation\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"三个 figure（3/4/5）纵向堆叠在一页，每个图较小。Figure 5（GSM1K scatter plot）的 axis label 和数据点标注字号接近可读下限。建议适当增大或拆分为两页\"}, {\"severity\": \"info\", \"dimension\": \"overall\", \"message\": \"主文 5 个 display items / 8 页偏少（实证型论文通常 5-8 个），而附录集中了 10 个 display items。考虑将最有 narrative 价值的 1-2 个附录图表提升至主文（如 Figure 3 cross-subject matching 或 Figure 4 downstream impact）以增强主文视觉密度\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 3 展示 6 个 benchmark 的 DIF landscape，数据丰富。最优/关键数值未用加粗标注，审稿人需自行辨识重点数据\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-22T12:30:58.125044+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Round 15 (Fresh review, 2026-05-22)\n# 3 critical open, 8 warning open, 4 info open\n\n# ============================================================\n# ROUND 15 — MUST-FIX (CRITICAL)\n# ============================================================\n\n- id: \"R15-MF1\"\n  summary: \"DEFF-adjusted 下界 (13.5%) 与 headline claim (31%) 落差在正文中未充分报告\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-MF2 首提。三种 uncertainty estimates 不一致。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-W3。[AGREE] 双方共识。R2 建议 headline 改为 ~27-31% 范围（三种独立方法收敛于此），weighted DEFF 13.5% 过于保守（effective cluster size 254.5 在 LLM 语境不合理）。需在正文中建立估计优先级层次。\"\n  action_items:\n    - round: 15\n      action: \"正文 §4.2 直接报告 DEFF 范围 [13.5%, 29.2%]；建立 uncertainty 优先级；考虑以 ~27-31% 替代单点 31%\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-MF2\"\n  summary: \"'Temporal measurement instability' 因果归因过度——observational DIF 无法支撑 item 测量属性变化的因果推理\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-N3 首提，R2 [AGREE]。DIF 检测 'that' not 'why'——同样数据可解读为不同代 LLM 能力 profile 合理不同。difficulty–direction ρ=-0.597 更支持 capability evolution 假说。§5.1 列出三种机制后立刻放弃因果推理，显得不完整。\"\n  action_items:\n    - round: 15\n      action: \"弱化因果归因措辞；§5.1 深化三种机制的相对证据讨论；考虑 title 是否需要调整\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-MF3\"\n  summary: \"ρ ≈ 0.997 与 31% DIF 的张力未充分调和——practical impact 论证不足\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-W2 首提，R1 [AGREE]。aggregate ranking 几乎不变 → leaderboard comparison 影响有限。'diagnostic lens rather than quality filter' framing 实质承认影响有限。缺少 item-level case study 和 subject-level ranking 影响量化。\"\n  action_items:\n    - round: 15\n      action: \"补充 item-level case study；量化 subject-level ranking 变化；深化 diagnostic value 论证\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 15 — SHOULD-FIX (WARNING)\n# ============================================================\n\n- id: \"R15-SF1\"\n  summary: \"多维度混淆辩护仍有漏洞——κ=0.80 的 20% discordance 来源未分析\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-MF1 首提为 critical。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-N2 判 Must-Fix，R2 [REBUT] 降为 Should-Fix（R1 引用 Cohen's d 数值有误：实际 range=0.115，非 R1 所称的 0.183；Humanities/Other=1.09 非 2.25）。核心关切成立但 R1 过度陈述。2.7pp cross-subject-unique C items 是多维度 confound 的量化上界。\"\n  action_items:\n    - round: 15\n      action: \"分析 κ discordant items 的 domain 分布；考虑 SIBTEST 或 domain-covariate logistic regression\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-SF2\"\n  summary: \"新颖性定位不足——MH-DIF 为既有方法，'application context' 对主会议门槛偏弱\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF2。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-W1 首提 Must-Fix，R1 [AGREE] 但建议将 cross-subject matching 前置为方法论贡献。在 Growing Pains / BHI / Benchmark² / MMLU-CF 密集区域中需更强区分。R1 认为 cross-subject matching 是真正的方法论贡献。\"\n  action_items:\n    - round: 15\n      action: \"将 LLM-specific adaptations (cross-subject matching, multi-domain contamination control) 前置为方法论贡献；强化 positioning paragraph\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-SF3\"\n  summary: \"Discussion §5 深度不足（~半页），因果推理框架和 benchmark lifecycle 讨论缺失\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF1。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-W4，R1 [AGREE]。§5.1 放弃因果推理；§5.3 阈值 15%/25% 仅由 Figure 6 支撑；缺 benchmark lifecycle management 讨论。\"\n  action_items:\n    - round: 15\n      action: \"扩展 §5 约 0.3-0.5 页：因果假说证据讨论 + 阈值 empirical grounding + benchmark reform 定位\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-SF4\"\n  summary: \"Abstract 信息密度过高（9+ 数字），关键信息被稀释\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF3。\"\n    - round: 15\n      reviewers: [2]\n      note: \"R2-W5。建议保留 3-4 个关键数字。\"\n  action_items:\n    - round: 15\n      action: \"精简 Abstract 至 3-4 核心数字\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-SF5\"\n  summary: \"术语不一致：temporal measurement instability / temporal DIF / measurement invariance / temporal comparability 层次模糊\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF4。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-W6，R1 [AGREE]。\"\n  action_items:\n    - round: 15\n      action: \"§1 建立术语层次定义并全文统一\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-SF6\"\n  summary: \"Semi-synthetic injection ecological validity 有限——binary flipping 不反映 realistic contamination\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF6。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W1，R2 [AGREE] 但补充 ΔFPR=0 保证独立于 injection realism。\"\n  action_items:\n    - round: 15\n      action: \"Limitations 中讨论 difficulty-dependent / partial knowledge 注入模型的定性影响\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-SF7\"\n  summary: \"缺少 2024 cohort 内 random-split sanity check\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W3，R2 [AGREE]。成本极低，应补充。\"\n  action_items:\n    - round: 15\n      action: \"补充 2024 cohort random-split sanity check\"\n      assigned_to: \"Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-SF8\"\n  summary: \"24.8% non-uniform DIF 对 MH 方法影响未讨论，item-level pattern 缺失\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2-Q4。MH 是 uniform DIF 方法，~1/4 items 的 DIF 幅度可能被误估。\"\n  action_items:\n    - round: 15\n      action: \"分析 non-uniform DIF items 的 domain/difficulty 分布；讨论对 MH 结论的影响\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 15 — INFO\n# ============================================================\n\n- id: \"R15-I1\"\n  summary: \"Table 1 within-family/random-split 的 '--' 标注缺解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"R2-M2。\"\n\n- id: \"R15-I2\"\n  summary: \"§3.4 Remark 格式介于 proposition 和 remark 之间\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"R2-M3。\"\n\n- id: \"R15-I3\"\n  summary: \"Missing references: Penfield & Algina 2006, Bolt & Stout 1996, Cheung & Rensvold 2002\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1 提 4 个（Zumbo 1999 已被引用，R2 指出 R1 检查有误）。R2 提 4 个（MR1 Gema 已在 §5.1 讨论，MR2 TinyBenchmarks 被 R1 rebut）。共识：Penfield & Algina, Bolt & Stout, Cheung & Rensvold 建议补充。\"\n\n- id: \"R15-I4\"\n  summary: \"'enrichment ratio' 首次使用缺乏直觉解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1]\n      note: \"R1-M4。\"\n\n# ============================================================\n# ROUND 14 — STATUS UPDATE\n# ============================================================\n\n- id: \"R14-SF5\"\n  summary: \"Gema et al. (2024) MMLU ground truth errors 作为 DIF confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"§5.1 现已讨论 Gema et al. (2024) MMLU-Redux 313 flagged items: enrichment=0.92×, φ=-0.01, p=0.37，确认 DIF 捕获的是 dynamic shifts 而非 static defects。\"\n  resolution_round: 15\n\n- id: \"R14-SF7\"\n  summary: \"IRT θ-conditioning 不构成独立控制，应降级为 sensitivity check\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"§4.4 和 Table 2 现已标注为 'sensitivity check'，不再列为独立 structural control。\"\n  resolution_round: 15\n\n- id: \"R14-SF9\"\n  summary: \"GSM1K cross-validation N=33 过小\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"§4.7 添加 'interpret with caution' caveat + Cook's D influence diagnostics。R2 在交叉回应中确认 R1 对 GSM1K 的 cherry-picking 指控基于错误数值 (r=-0.478 非 -0.17)，不成立。\"\n  resolution_round: 15\n\n# ============================================================\n# PRIOR RESOLVED (carried from earlier rounds)\n# ============================================================\n\n- id: \"R13-MF1\"\n  summary: \"LOFO family-concentration: power-reduction 解释不充分\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"MF1 Monte Carlo power calibration (200 reps): power <1pp, composition 95-113%. Integrated into LOFO caption.\"\n  resolution_round: 14\n\n- id: \"R13-MF2\"\n  summary: \"Examinee non-independence 对 MH chi-squared inflation 缺乏直接定量\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 14\n  resolution: \"DEFF estimation: simple DEFF=3.87, weighted=12.79, adjusted C%=[13.5%, 29.2%]. New Appendix D + §4.2 reference.\"\n  resolution_round: 14\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"Permutation null 已补充到 §4.2\"\n  resolution_round: 8\n\n- id: \"R8-MF2\"\n  summary: \"'Drift' framing 超出数据支撑\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Title 改为 'Temporal Measurement Instability'\"\n  resolution_round: 9\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%\"\n  resolution_round: 4\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 practical significance paradox\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 11\n  resolution: \"Family-level profiles + pairwise flip rate + 'diagnostic not destructive' framing\"\n  resolution_round: 11\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Round 15 (Fresh review, 2026-05-22)\n# 3 critical open, 8 warning open, 4 info open\n\n# ============================================================\n# ROUND 15 — MUST-FIX (CRITICAL)\n# ============================================================\n\n- id: \"R15-MF1\"\n  summary: \"DEFF-adjusted 下界 (13.5%) 与 headline claim (31%) 落差在正文中未充分报告\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-MF2 首提。三种 uncertainty estimates 不一致。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-W3。[AGREE] 双方共识。R2 建议 headline 改为 ~27-31% 范围（三种独立方法收敛于此），weighted DEFF 13.5% 过于保守（effective cluster size 254.5 在 LLM 语境不合理）。需在正文中建立估计优先级层次。\"\n  action_items:\n    - round: 15\n      action: \"正文 §4.2 直接报告 DEFF 范围 [13.5%, 29.2%]；建立 uncertainty 优先级；考虑以 ~27-31% 替代单点 31%\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-MF2\"\n  summary: \"'Temporal measurement instability' 因果归因过度——observational DIF 无法支撑 item 测量属性变化的因果推理\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-N3 首提，R2 [AGREE]。DIF 检测 'that' not 'why'——同样数据可解读为不同代 LLM 能力 profile 合理不同。difficulty–direction ρ=-0.597 更支持 capability evolution 假说。§5.1 列出三种机制后立刻放弃因果推理，显得不完整。\"\n  action_items:\n    - round: 15\n      action: \"弱化因果归因措辞；§5.1 深化三种机制的相对证据讨论；考虑 title 是否需要调整\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-MF3\"\n  summary: \"ρ ≈ 0.997 与 31% DIF 的张力未充分调和——practical impact 论证不足\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-W2 首提，R1 [AGREE]。aggregate ranking 几乎不变 → leaderboard comparison 影响有限。'diagnostic lens rather than quality filter' framing 实质承认影响有限。缺少 item-level case study 和 subject-level ranking 影响量化。\"\n  action_items:\n    - round: 15\n      action: \"补充 item-level case study；量化 subject-level ranking 变化；深化 diagnostic value 论证\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 15 — SHOULD-FIX (WARNING)\n# ============================================================\n\n- id: \"R15-SF1\"\n  summary: \"多维度混淆辩护仍有漏洞——κ=0.80 的 20% discordance 来源未分析\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-MF1 首提为 critical。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-N2 判 Must-Fix，R2 [REBUT] 降为 Should-Fix（R1 引用 Cohen's d 数值有误：实际 range=0.115，非 R1 所称的 0.183；Humanities/Other=1.09 非 2.25）。核心关切成立但 R1 过度陈述。2.7pp cross-subject-unique C items 是多维度 confound 的量化上界。\"\n  action_items:\n    - round: 15\n      action: \"分析 κ discordant items 的 domain 分布；考虑 SIBTEST 或 domain-covariate logistic regression\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-SF2\"\n  summary: \"新颖性定位不足——MH-DIF 为既有方法，'application context' 对主会议门槛偏弱\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF2。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-W1 首提 Must-Fix，R1 [AGREE] 但建议将 cross-subject matching 前置为方法论贡献。在 Growing Pains / BHI / Benchmark² / MMLU-CF 密集区域中需更强区分。R1 认为 cross-subject matching 是真正的方法论贡献。\"\n  action_items:\n    - round: 15\n      action: \"将 LLM-specific adaptations (cross-subject matching, multi-domain contamination control) 前置为方法论贡献；强化 positioning paragraph\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-SF3\"\n  summary: \"Discussion §5 深度不足（~半页），因果推理框架和 benchmark lifecycle 讨论缺失\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF1。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-W4，R1 [AGREE]。§5.1 放弃因果推理；§5.3 阈值 15%/25% 仅由 Figure 6 支撑；缺 benchmark lifecycle management 讨论。\"\n  action_items:\n    - round: 15\n      action: \"扩展 §5 约 0.3-0.5 页：因果假说证据讨论 + 阈值 empirical grounding + benchmark reform 定位\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-SF4\"\n  summary: \"Abstract 信息密度过高（9+ 数字），关键信息被稀释\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF3。\"\n    - round: 15\n      reviewers: [2]\n      note: \"R2-W5。建议保留 3-4 个关键数字。\"\n  action_items:\n    - round: 15\n      action: \"精简 Abstract 至 3-4 核心数字\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-SF5\"\n  summary: \"术语不一致：temporal measurement instability / temporal DIF / measurement invariance / temporal comparability 层次模糊\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF4。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-W6，R1 [AGREE]。\"\n  action_items:\n    - round: 15\n      action: \"§1 建立术语层次定义并全文统一\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-SF6\"\n  summary: \"Semi-synthetic injection ecological validity 有限——binary flipping 不反映 realistic contamination\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14-SF6。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W1，R2 [AGREE] 但补充 ΔFPR=0 保证独立于 injection realism。\"\n  action_items:\n    - round: 15\n      action: \"Limitations 中讨论 difficulty-dependent / partial knowledge 注入模型的定性影响\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-SF7\"\n  summary: \"缺少 2024 cohort 内 random-split sanity check\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W3，R2 [AGREE]。成本极低，应补充。\"\n  action_items:\n    - round: 15\n      action: \"补充 2024 cohort random-split sanity check\"\n      assigned_to: \"Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-SF8\"\n  summary: \"24.8% non-uniform DIF 对 MH 方法影响未讨论，item-level pattern 缺失\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2-Q4。MH 是 uniform DIF 方法，~1/4 items 的 DIF 幅度可能被误估。\"\n  action_items:\n    - round: 15\n      action: \"分析 non-uniform DIF items 的 domain/difficulty 分布；讨论对 MH 结论的影响\"\n      assigned_to: \"Paper Agent\"\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ROUND 15 — INFO\n# ============================================================\n\n- id: \"R15-I1\"\n  summary: \"Table 1 within-family/random-split 的 '--' 标注缺解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"R2-M2。\"\n\n- id: \"R15-I2\"\n  summary: \"§3.4 Remark 格式介于 proposition 和 remark 之间\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"R2-M3。\"\n\n- id: \"R15-I3\"\n  summary: \"Missing references: Penfield & Algina 2006, Bolt & Stout 1996, Cheung & Rensvold 2002\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1 提 4 个（Zumbo 1999 已被引用，R2 指出 R1 检查有误）。R2 提 4 个（MR1 Gema 已在 §5.1 讨论，MR2 TinyBenchmarks 被 R1 rebut）。共识：Penfield & Algina, Bolt & Stout, Cheung & Rensvold 建议补充。\"\n\n- id: \"R15-I4\"\n  summary: \"'enrichment ratio' 首次使用缺乏直觉解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1]\n      note: \"R1-M4。\"\n\n# ============================================================\n# ROUND 14 — STATUS UPDATE\n# ============================================================\n\n- id: \"R14-SF5\"\n  summary: \"Gema et al. (2024) MMLU ground truth errors 作为 DIF confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"§5.1 现已讨论 Gema et al. (2024) MMLU-Redux 313 flagged items: enrichment=0.92×, φ=-0.01, p=0.37，确认 DIF 捕获的是 dynamic shifts 而非 static defects。\"\n  resolution_round: 15\n\n- id: \"R14-SF7\"\n  summary: \"IRT θ-conditioning 不构成独立控制，应降级为 sensitivity check\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"§4.4 和 Table 2 现已标注为 'sensitivity check'，不再列为独立 structural control。\"\n  resolution_round: 15\n\n- id: \"R14-SF9\"\n  summary: \"GSM1K cross-validation N=33 过小\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"§4.7 添加 'interpret with caution' caveat + Cook's D influence diagnostics。R2 在交叉回应中确认 R1 对 GSM1K 的 cherry-picking 指控基于错误数值 (r=-0.478 非 -0.17)，不成立。\"\n  resolution_round: 15\n\n# ============================================================\n# PRIOR RESOLVED (carried from earlier rounds)\n# ============================================================\n\n- id: \"R13-MF1\"\n  summary: \"LOFO family-concentration: power-reduction 解释不充分\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"MF1 Monte Carlo power calibration (200 reps): power <1pp, composition 95-113%. Integrated into LOFO caption.\"\n  resolution_round: 14\n\n- id: \"R13-MF2\"\n  summary: \"Examinee non-independence 对 MH chi-squared inflation 缺乏直接定量\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 14\n  resolution: \"DEFF estimation: simple DEFF=3.87, weighted=12.79, adjusted C%=[13.5%, 29.2%]. New Appendix D + §4.2 reference.\"\n  resolution_round: 14\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"Permutation null 已补充到 §4.2\"\n  resolution_round: 8\n\n- id: \"R8-MF2\"\n  summary: \"'Drift' framing 超出数据支撑\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Title 改为 'Temporal Measurement Instability'\"\n  resolution_round: 9\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%\"\n  resolution_round: 4\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 practical significance paradox\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 11\n  resolution: \"Family-level profiles + pairwise flip rate + 'diagnostic not destructive' framing\"\n  resolution_round: 11\n"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-22T12:30:58.181926+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 11571}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 56
}
```

</details>

---


### Tool call

_source line 816 · 2026-05-22T12:33:07.712475+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "report": "# 审稿报告 — Round 15 (Fresh Review)\n\n**论文**: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**Venue**: EMNLP 2026 (ARR May cycle)\n**审稿人**: Reviewer 1（方法严谨性）、Reviewer 2（新颖性/完整性）\n**日期**: 2026-05-22\n\n---\n\n## Summary\n\n本文将 Mantel-Haenszel DIF 分析（含 ETS 严重性分类）应用于 METABENCH 的 5,227 模型 × 6 个 benchmark 响应矩阵，发现 17.9–31.3% 的 items 在 2023–2024 时间跨度内展现 large temporal DIF (ETS C)。论文提出 cross-subject matching 的 semi-synthetic validation framework（ΔFPR=0 构造性保证），并指出 web-overlap contamination labels 与 DIF flags 近乎独立（Jaccard=0.206），揭示了现有 contamination 验证方法论的 category error。实证规模大（5,227 models × 27,125 items）、控制系统（6 种 alternative explanations）、透明度高（代码公开、5 种 uncertainty estimates 并列），但存在三个核心问题：DEFF-adjusted 下界与 headline claim 落差在正文中被低估报告、\"instability\" 因果归因超出 observational DIF 所能支撑的范围、ρ ≈ 0.997 与 31% DIF 之间的实际影响力张力未充分调和。\n\n---\n\n## Strengths\n\n**S1** [Major] 实证规模和控制的系统性令人印象深刻。5,227 模型 × 12,508 items 远超典型 DIF 应用规模；6 种 alternative explanation 逐一排除（random split、matched ability、within-family、within-subject、IRT θ-conditioning、graduated de-duplication）。[R1, R2 共识]\n\n**S2** [Major] Ground truth meta-critique 是最有知识贡献的部分。Global exposure vs. differential functioning 的概念区分（Figure 1）清晰有力；enrichment=0.964、Jaccard=0.206 为 contamination detection 领域提供了重要方法论 caveat，揭示了普遍使用的验证标准存在 category error。[R2 首提, R1 认同]\n\n**S3** [Moderate] Cross-subject matching 的 ΔFPR=0 构造性保证简洁优雅，multi-subject injection robustness（Table 6）展示了 graceful degradation。R1 和 R2 均认为这是论文真正的方法论贡献，应更显著前置。[R1, R2 共识]\n\n**S4** [Moderate] Uncertainty quantification 的透明度值得肯定——五种不同假设下的估计结果并列呈现（Appendix D Table 8），包括最保守的 DEFF-weighted 估计。[R2 首提]\n\n**S5** [Moderate] Cross-benchmark validation 跨 6 个 METABENCH benchmark 的一致性（Table 3）提供了有意义的 external validity。Knowledge/reasoning vs. procedural benchmarks 的 C% 差异模式有解释力。[R1, R2 共识]\n\n**S6** [Minor] 写作质量整体较高，图表信息密度好，可复现性强（匿名代码仓库 + 公开数据集）。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 个）\n\n**MF1** [Critical] DEFF-adjusted 下界与 headline claim 的落差在正文中被低估报告\n- 论文通篇以 \"31%\" 为核心 claim，但 DEFF-weighted 估计将 C% 压至 13.5%（Appendix D），不到 headline 的一半\n- 四种 uncertainty estimates 缺乏明确优先级层次\n- R2 指出三种独立方法（cluster bootstrap 26.7%、simple DEFF 29.2%、de-duplication K=20 29.1%）收敛于 ~27–29%，weighted DEFF 的 effective cluster size 254.5 在 LLM 语境中过于极端\n- **建议**: 正文中直接报告 DEFF 范围；建立估计优先级；考虑以 ~27–31% 替代单点 headline\n- **共识**: [AGREE] R1-N1, R2-W3\n\n**MF2** [Critical] \"Temporal measurement instability\" 因果归因超出 observational DIF 支撑范围\n- DIF 检测 \"that items function differently\" 而非 \"why\"——同样的数据可解读为不同代 LLM 在不同 items 上能力 profile 合理地不同\n- difficulty–direction interaction ρ=−0.597 更支持 capability evolution 假说（R2 补充），进一步削弱 contamination-focused 叙事\n- §5.1 列出三种机制后立刻放弃因果推理，显得不完整\n- **建议**: 弱化因果归因措辞；§5.1 深化三种机制的相对证据讨论\n- **共识**: [AGREE] R1-N3, R2 认同\n\n**MF3** [Critical] ρ ≈ 0.997 与 \"31% instability\" 之间的 practical impact 张力未充分调和\n- Aggregate ranking 几乎不受 DIF 影响 → 对 leaderboard comparison（主要使用场景）影响有限\n- \"Diagnostic lens rather than quality filter\" 的 framing 实质上承认了影响的有限性\n- 缺少 item-level case study 展示 DIF 的实际后果\n- **建议**: 补充 concrete case study + 量化 subject-level ranking 影响 + 深化 diagnostic value 论证\n- **共识**: [AGREE] R2-W2, R1 认同\n\n### Should-Fix（8 个）\n\n**SF1** [Warning] 多维度混淆辩护仍有漏洞\n- MMLU 57-subject 高度多维度，total-score matching 可能产生 spurious DIF\n- 三条辩护有改进但 κ=0.80 的 20% discordance 来源未分析\n- 注：R1 的 Cohen's d 引用有事实性错误（实际 range=0.115，所有 d < 0.3），R2 据此建议从 Must-Fix 降为 Should-Fix。2.7pp cross-subject-unique C items 是多维度 confound 的量化上界\n- **建议**: 分析 κ discordant items 的 domain 分布\n- **分歧**: R1 判 Must-Fix，R2 [REBUT] 降为 Should-Fix。Review Director 采纳 Should-Fix（R1 数据引用错误削弱了其论证力度，但核心关切成立）\n\n**SF2** [Warning] 新颖性定位不足——MH-DIF 为 1988 年既有方法\n- §2 明确承认 \"We do not modify the MH procedure; our contribution is the application context\"\n- 三个 contributions 实质为 empirical findings\n- R1 认为 cross-subject matching 是真正的方法论贡献，应前置\n- **建议**: 将 LLM-specific adaptations 前置为方法论贡献；强化与 Growing Pains / BHI / Benchmark² 的 positioning\n\n**SF3** [Warning] Discussion §5 深度不足\n- 仅约半页；§5.1 放弃因果推理；§5.3 阈值 15%/25% 仅由 Figure 6 支撑\n- **建议**: 扩展 ~0.3–0.5 页\n\n**SF4** [Warning] Abstract 信息密度过高（9+ 数字）\n- **建议**: 精简至 3–4 核心数字\n\n**SF5** [Warning] 术语层次模糊\n- temporal measurement instability / temporal DIF / measurement invariance / temporal comparability 混用\n- **建议**: §1 建立术语层次\n\n**SF6** [Warning] Semi-synthetic injection ecological validity 有限\n- Binary flipping 不反映 realistic contamination；R2 补充 ΔFPR=0 独立于 injection realism\n- **建议**: Limitations 讨论 difficulty-dependent 注入模型\n\n**SF7** [Warning] 缺少 2024 cohort 内 random-split sanity check\n- 成本极低，应补充\n\n**SF8** [Warning] 24.8% non-uniform DIF 的 item-level pattern 缺失\n- MH 是 uniform DIF 方法，~1/4 items 可能被误估\n\n---\n\n## Reviewer Consensus\n\n以下问题双方独立收敛（交叉回应中 [AGREE]）：\n\n1. **DEFF 透明度**: headline 31% 需在正文中与 DEFF 范围并列报告，三种独立方法收敛于 ~27–29% [R1-N1 ≈ R2-W3]\n2. **因果归因**: observational DIF 不支撑 \"measurement instability\" 的因果推理 [R1-N3, R2 AGREE]\n3. **Practical impact**: ρ=0.997 削弱了 31% DIF 的实际影响力叙事 [R2-W2, R1 AGREE]\n4. **Semi-synthetic ecological validity**: 有限但 ΔFPR=0 保证独立 [R1-W1, R2 AGREE]\n5. **2024 random split**: 应补充 [R1-W3, R2 AGREE]\n6. **Non-uniform DIF**: pattern 分析缺失 [R1-W4, R2 AGREE]\n\n## Reviewer Divergence\n\n**多维度混淆严重性** — R1 判 Must-Fix，R2 [REBUT] 降为 Should-Fix\n- R2 指出 R1 的 Cohen's d 引用有事实性错误（实际 range=0.115，Humanities/Other=1.09 非 R1 所称的 2.25）\n- R2 提供方向性证据：cross-subject 比 within-subject 多 2.7pp C items，作为多维度 confound 的上界\n- **Review Director 裁定**: Should-Fix。R1 的核心关切成立（κ discordance 来源未分析），但数据引用错误削弱了将其提升至 Must-Fix 的论证。\n\n**GSM1K 分析质量** — R1-W2 \"cherry-picking\"，R2 [REBUT]\n- R1 引用 \"r=−0.17\" 是事实性错误（论文报告 r=−0.478, p=0.005）\n- R2 指出论文已添加 Cook's D influence diagnostics 和 \"interpret with caution\" caveat\n- **Review Director 裁定**: 不列为 issue。R1 指控基于错误数值，不成立。\n\n---\n\n## Questions\n\n1. DEFF weighted-mean 的 effective cluster size 254.5 在 LLM 语境中的合理性？是否有更适合 LLM 家族结构的 clustering correction？[R2-Q1]\n2. difficulty–direction interaction ρ=−0.597 的因果推理含义——更支持 capability evolution 还是 contamination？对论文整体 framing 有何影响？[R2-Q2]\n3. 实际场景中 contamination 的 cross-subject 程度如何？Table 6 k=20 ΔFPR=0.069 在部署中是否 non-negligible？[R2-Q3]\n4. 24.8% non-uniform DIF items 的 domain 和 difficulty 分布？[R1-W4, R2-Q4]\n5. Within-family C%=61.3% 经 ability-matching 降至 28.3%——是否暗示 family-specific 变化是主要驱动力？[R1-Q3, R2 已 rebut: matched values 一致]\n\n---\n\n## Missing References\n\n**共识建议引用**:\n- Penfield & Algina (2006) — multidimensional DIF 框架\n- Bolt & Stout (1996) — multidimensionality-based DIF 理论\n- Cheung & Rensvold (2002) — multi-group CFA measurement invariance\n\n**注**: R1 提出的 Zumbo (1999) 已被引用（§2 Related Work）；R2 提出的 Gema et al. (2024) 已在 §5.1 讨论；R2 提出的 TinyBenchmarks 被 R1 [REBUT] 为不构成 missing reference。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（2026-05-22 12:18 → 12:21，耗时 3 分钟）\n\n**Findings**:\n- [Warning] Pages 3–5 连续 3 页纯文本无 display item（Method 章节）。建议将 α_MH 和 Δ_MH 公式改为 display equation，或将 Table 1 提前至 p5\n- [Warning] Page 16 (appendix) 上方 ~1/3 空白，Figure 6 上方空间利用不充分\n- [Info] 主文 5 个 display items / 8 页偏少（实证论文通常 5–8 个），附录集中 10 个。考虑提升 1–2 个附录图表至主文\n- [Info] Page 15 三个 figure 纵向堆叠，Figure 5 axis label 字号接近可读下限\n- [Info] Table 3 关键数值未用加粗标注\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n**Confidence: 4 / 5**\n\n两位 Reviewer 独立给出相同评分（3.5），交叉回应后维持不变。核心判断：\n\n**达到的标准**:\n- 实证规模和控制充分性达到顶会水平\n- Ground truth meta-critique（global vs. differential）有原创知识贡献\n- Cross-subject matching 的 ΔFPR=0 保证是真正的方法论贡献\n- 透明度和可复现性优秀\n\n**未达到的标准**:\n- 方法论新颖性有限（MH-DIF 为既有方法，论文自承 \"application context\"）\n- Headline claim (31%) 与 DEFF-adjusted 下界 (13.5%) 的落差需在正文中透明处理\n- \"Temporal measurement instability\" 的因果归因超出 observational DIF 支撑范围\n- ρ ≈ 0.997 削弱了 31% DIF 的实际影响力叙事，需更强的 use-case 论证\n\n**修改路径**:\n解决 MF1（DEFF 透明度）、MF2（因果归因弱化）、MF3（practical impact case study）+ SF1–SF2（多维度辩护 + novelty 前置）后，评分可提升至 4.0 (Conference)。若仅部分修改，更适合 Findings track (3.0)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 术语层次需在首次使用时建立（measurement invariance → DIF → temporal measurement instability）\n- Contribution 2 的 \"eliminates false positive inflation\" 已标注 \"under single-subject contamination\"——但 multi-subject boundary (k>5) 的讨论应在此提及\n- 建议前置 cross-subject matching 作为方法论贡献而非仅作为 validation 工具\n\n### §3 Method\n- §3.2 的 LLM-specific challenges 段已较完善，但可增加对 multidimensionality 的正式处理\n- §3.4 Remark 格式介于 proposition 和 remark 之间——建议统一\n- Pages 3–5 视觉单调，建议将 Eq. 1–2 改为 display equation\n\n### §4 Experiments\n- §4.2 headline: 建议报告为 \"~27–31% (DEFF-adjusted range: 13.5–29.2%)\" 而非单点 31%\n- §4.4 structural analysis: within-subject C%=38.1% 的解读可更明确——这是 local dependence 的直接证据\n- §4.7 GSM1K: \"interpret with caution\" + Cook's D 已足够；R1 的 cherry-picking 指控不成立\n\n### §5 Discussion\n- §5.1: 需深化因果推理——difficulty–direction ρ=−0.597 为 capability evolution 提供证据，应正式讨论\n- §5.2: 简洁有效，无需修改\n- §5.3: 阈值推导需更多 empirical grounding；建议补充 case study\n\n### §6 Conclusion\n- 目前紧凑有效，但如果 headline claim 改为范围，Conclusion 需相应更新\n\n### Limitations\n- 已涵盖核心局限但可补充：(1) difficulty-dependent injection 模型的定性影响；(2) 2024 cohort random split 的缺失\n\n### Appendix\n- Appendix D (DEFF) 内容应在正文中更显著引用\n- Figure 6 (ρ-degradation) 对 §5.3 audit protocol 有支撑作用，但 page 16 布局需优化\n",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "report": "# 审稿报告 — Round 15 (Fresh Review)\n\n**论文**: \"Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n**Venue**: EMNLP 2026 (ARR May cycle)\n**审稿人**: Reviewer 1（方法严谨性）、Reviewer 2（新颖性/完整性）\n**日期**: 2026-05-22\n\n---\n\n## Summary\n\n本文将 Mantel-Haenszel DIF 分析（含 ETS 严重性分类）应用于 METABENCH 的 5,227 模型 × 6 个 benchmark 响应矩阵，发现 17.9–31.3% 的 items 在 2023–2024 时间跨度内展现 large temporal DIF (ETS C)。论文提出 cross-subject matching 的 semi-synthetic validation framework（ΔFPR=0 构造性保证），并指出 web-overlap contamination labels 与 DIF flags 近乎独立（Jaccard=0.206），揭示了现有 contamination 验证方法论的 category error。实证规模大（5,227 models × 27,125 items）、控制系统（6 种 alternative explanations）、透明度高（代码公开、5 种 uncertainty estimates 并列），但存在三个核心问题：DEFF-adjusted 下界与 headline claim 落差在正文中被低估报告、\"instability\" 因果归因超出 observational DIF 所能支撑的范围、ρ ≈ 0.997 与 31% DIF 之间的实际影响力张力未充分调和。\n\n---\n\n## Strengths\n\n**S1** [Major] 实证规模和控制的系统性令人印象深刻。5,227 模型 × 12,508 items 远超典型 DIF 应用规模；6 种 alternative explanation 逐一排除（random split、matched ability、within-family、within-subject、IRT θ-conditioning、graduated de-duplication）。[R1, R2 共识]\n\n**S2** [Major] Ground truth meta-critique 是最有知识贡献的部分。Global exposure vs. differential functioning 的概念区分（Figure 1）清晰有力；enrichment=0.964、Jaccard=0.206 为 contamination detection 领域提供了重要方法论 caveat，揭示了普遍使用的验证标准存在 category error。[R2 首提, R1 认同]\n\n**S3** [Moderate] Cross-subject matching 的 ΔFPR=0 构造性保证简洁优雅，multi-subject injection robustness（Table 6）展示了 graceful degradation。R1 和 R2 均认为这是论文真正的方法论贡献，应更显著前置。[R1, R2 共识]\n\n**S4** [Moderate] Uncertainty quantification 的透明度值得肯定——五种不同假设下的估计结果并列呈现（Appendix D Table 8），包括最保守的 DEFF-weighted 估计。[R2 首提]\n\n**S5** [Moderate] Cross-benchmark validation 跨 6 个 METABENCH benchmark 的一致性（Table 3）提供了有意义的 external validity。Knowledge/reasoning vs. procedural benchmarks 的 C% 差异模式有解释力。[R1, R2 共识]\n\n**S6** [Minor] 写作质量整体较高，图表信息密度好，可复现性强（匿名代码仓库 + 公开数据集）。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 个）\n\n**MF1** [Critical] DEFF-adjusted 下界与 headline claim 的落差在正文中被低估报告\n- 论文通篇以 \"31%\" 为核心 claim，但 DEFF-weighted 估计将 C% 压至 13.5%（Appendix D），不到 headline 的一半\n- 四种 uncertainty estimates 缺乏明确优先级层次\n- R2 指出三种独立方法（cluster bootstrap 26.7%、simple DEFF 29.2%、de-duplication K=20 29.1%）收敛于 ~27–29%，weighted DEFF 的 effective cluster size 254.5 在 LLM 语境中过于极端\n- **建议**: 正文中直接报告 DEFF 范围；建立估计优先级；考虑以 ~27–31% 替代单点 headline\n- **共识**: [AGREE] R1-N1, R2-W3\n\n**MF2** [Critical] \"Temporal measurement instability\" 因果归因超出 observational DIF 支撑范围\n- DIF 检测 \"that items function differently\" 而非 \"why\"——同样的数据可解读为不同代 LLM 在不同 items 上能力 profile 合理地不同\n- difficulty–direction interaction ρ=−0.597 更支持 capability evolution 假说（R2 补充），进一步削弱 contamination-focused 叙事\n- §5.1 列出三种机制后立刻放弃因果推理，显得不完整\n- **建议**: 弱化因果归因措辞；§5.1 深化三种机制的相对证据讨论\n- **共识**: [AGREE] R1-N3, R2 认同\n\n**MF3** [Critical] ρ ≈ 0.997 与 \"31% instability\" 之间的 practical impact 张力未充分调和\n- Aggregate ranking 几乎不受 DIF 影响 → 对 leaderboard comparison（主要使用场景）影响有限\n- \"Diagnostic lens rather than quality filter\" 的 framing 实质上承认了影响的有限性\n- 缺少 item-level case study 展示 DIF 的实际后果\n- **建议**: 补充 concrete case study + 量化 subject-level ranking 影响 + 深化 diagnostic value 论证\n- **共识**: [AGREE] R2-W2, R1 认同\n\n### Should-Fix（8 个）\n\n**SF1** [Warning] 多维度混淆辩护仍有漏洞\n- MMLU 57-subject 高度多维度，total-score matching 可能产生 spurious DIF\n- 三条辩护有改进但 κ=0.80 的 20% discordance 来源未分析\n- 注：R1 的 Cohen's d 引用有事实性错误（实际 range=0.115，所有 d < 0.3），R2 据此建议从 Must-Fix 降为 Should-Fix。2.7pp cross-subject-unique C items 是多维度 confound 的量化上界\n- **建议**: 分析 κ discordant items 的 domain 分布\n- **分歧**: R1 判 Must-Fix，R2 [REBUT] 降为 Should-Fix。Review Director 采纳 Should-Fix（R1 数据引用错误削弱了其论证力度，但核心关切成立）\n\n**SF2** [Warning] 新颖性定位不足——MH-DIF 为 1988 年既有方法\n- §2 明确承认 \"We do not modify the MH procedure; our contribution is the application context\"\n- 三个 contributions 实质为 empirical findings\n- R1 认为 cross-subject matching 是真正的方法论贡献，应前置\n- **建议**: 将 LLM-specific adaptations 前置为方法论贡献；强化与 Growing Pains / BHI / Benchmark² 的 positioning\n\n**SF3** [Warning] Discussion §5 深度不足\n- 仅约半页；§5.1 放弃因果推理；§5.3 阈值 15%/25% 仅由 Figure 6 支撑\n- **建议**: 扩展 ~0.3–0.5 页\n\n**SF4** [Warning] Abstract 信息密度过高（9+ 数字）\n- **建议**: 精简至 3–4 核心数字\n\n**SF5** [Warning] 术语层次模糊\n- temporal measurement instability / temporal DIF / measurement invariance / temporal comparability 混用\n- **建议**: §1 建立术语层次\n\n**SF6** [Warning] Semi-synthetic injection ecological validity 有限\n- Binary flipping 不反映 realistic contamination；R2 补充 ΔFPR=0 独立于 injection realism\n- **建议**: Limitations 讨论 difficulty-dependent 注入模型\n\n**SF7** [Warning] 缺少 2024 cohort 内 random-split sanity check\n- 成本极低，应补充\n\n**SF8** [Warning] 24.8% non-uniform DIF 的 item-level pattern 缺失\n- MH 是 uniform DIF 方法，~1/4 items 可能被误估\n\n---\n\n## Reviewer Consensus\n\n以下问题双方独立收敛（交叉回应中 [AGREE]）：\n\n1. **DEFF 透明度**: headline 31% 需在正文中与 DEFF 范围并列报告，三种独立方法收敛于 ~27–29% [R1-N1 ≈ R2-W3]\n2. **因果归因**: observational DIF 不支撑 \"measurement instability\" 的因果推理 [R1-N3, R2 AGREE]\n3. **Practical impact**: ρ=0.997 削弱了 31% DIF 的实际影响力叙事 [R2-W2, R1 AGREE]\n4. **Semi-synthetic ecological validity**: 有限但 ΔFPR=0 保证独立 [R1-W1, R2 AGREE]\n5. **2024 random split**: 应补充 [R1-W3, R2 AGREE]\n6. **Non-uniform DIF**: pattern 分析缺失 [R1-W4, R2 AGREE]\n\n## Reviewer Divergence\n\n**多维度混淆严重性** — R1 判 Must-Fix，R2 [REBUT] 降为 Should-Fix\n- R2 指出 R1 的 Cohen's d 引用有事实性错误（实际 range=0.115，Humanities/Other=1.09 非 R1 所称的 2.25）\n- R2 提供方向性证据：cross-subject 比 within-subject 多 2.7pp C items，作为多维度 confound 的上界\n- **Review Director 裁定**: Should-Fix。R1 的核心关切成立（κ discordance 来源未分析），但数据引用错误削弱了将其提升至 Must-Fix 的论证。\n\n**GSM1K 分析质量** — R1-W2 \"cherry-picking\"，R2 [REBUT]\n- R1 引用 \"r=−0.17\" 是事实性错误（论文报告 r=−0.478, p=0.005）\n- R2 指出论文已添加 Cook's D influence diagnostics 和 \"interpret with caution\" caveat\n- **Review Director 裁定**: 不列为 issue。R1 指控基于错误数值，不成立。\n\n---\n\n## Questions\n\n1. DEFF weighted-mean 的 effective cluster size 254.5 在 LLM 语境中的合理性？是否有更适合 LLM 家族结构的 clustering correction？[R2-Q1]\n2. difficulty–direction interaction ρ=−0.597 的因果推理含义——更支持 capability evolution 还是 contamination？对论文整体 framing 有何影响？[R2-Q2]\n3. 实际场景中 contamination 的 cross-subject 程度如何？Table 6 k=20 ΔFPR=0.069 在部署中是否 non-negligible？[R2-Q3]\n4. 24.8% non-uniform DIF items 的 domain 和 difficulty 分布？[R1-W4, R2-Q4]\n5. Within-family C%=61.3% 经 ability-matching 降至 28.3%——是否暗示 family-specific 变化是主要驱动力？[R1-Q3, R2 已 rebut: matched values 一致]\n\n---\n\n## Missing References\n\n**共识建议引用**:\n- Penfield & Algina (2006) — multidimensional DIF 框架\n- Bolt & Stout (1996) — multidimensionality-based DIF 理论\n- Cheung & Rensvold (2002) — multi-group CFA measurement invariance\n\n**注**: R1 提出的 Zumbo (1999) 已被引用（§2 Related Work）；R2 提出的 Gema et al. (2024) 已在 §5.1 讨论；R2 提出的 TinyBenchmarks 被 R1 [REBUT] 为不构成 missing reference。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（2026-05-22 12:18 → 12:21，耗时 3 分钟）\n\n**Findings**:\n- [Warning] Pages 3–5 连续 3 页纯文本无 display item（Method 章节）。建议将 α_MH 和 Δ_MH 公式改为 display equation，或将 Table 1 提前至 p5\n- [Warning] Page 16 (appendix) 上方 ~1/3 空白，Figure 6 上方空间利用不充分\n- [Info] 主文 5 个 display items / 8 页偏少（实证论文通常 5–8 个），附录集中 10 个。考虑提升 1–2 个附录图表至主文\n- [Info] Page 15 三个 figure 纵向堆叠，Figure 5 axis label 字号接近可读下限\n- [Info] Table 3 关键数值未用加粗标注\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n**Confidence: 4 / 5**\n\n两位 Reviewer 独立给出相同评分（3.5），交叉回应后维持不变。核心判断：\n\n**达到的标准**:\n- 实证规模和控制充分性达到顶会水平\n- Ground truth meta-critique（global vs. differential）有原创知识贡献\n- Cross-subject matching 的 ΔFPR=0 保证是真正的方法论贡献\n- 透明度和可复现性优秀\n\n**未达到的标准**:\n- 方法论新颖性有限（MH-DIF 为既有方法，论文自承 \"application context\"）\n- Headline claim (31%) 与 DEFF-adjusted 下界 (13.5%) 的落差需在正文中透明处理\n- \"Temporal measurement instability\" 的因果归因超出 observational DIF 支撑范围\n- ρ ≈ 0.997 削弱了 31% DIF 的实际影响力叙事，需更强的 use-case 论证\n\n**修改路径**:\n解决 MF1（DEFF 透明度）、MF2（因果归因弱化）、MF3（practical impact case study）+ SF1–SF2（多维度辩护 + novelty 前置）后，评分可提升至 4.0 (Conference)。若仅部分修改，更适合 Findings track (3.0)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 术语层次需在首次使用时建立（measurement invariance → DIF → temporal measurement instability）\n- Contribution 2 的 \"eliminates false positive inflation\" 已标注 \"under single-subject contamination\"——但 multi-subject boundary (k>5) 的讨论应在此提及\n- 建议前置 cross-subject matching 作为方法论贡献而非仅作为 validation 工具\n\n### §3 Method\n- §3.2 的 LLM-specific challenges 段已较完善，但可增加对 multidimensionality 的正式处理\n- §3.4 Remark 格式介于 proposition 和 remark 之间——建议统一\n- Pages 3–5 视觉单调，建议将 Eq. 1–2 改为 display equation\n\n### §4 Experiments\n- §4.2 headline: 建议报告为 \"~27–31% (DEFF-adjusted range: 13.5–29.2%)\" 而非单点 31%\n- §4.4 structural analysis: within-subject C%=38.1% 的解读可更明确——这是 local dependence 的直接证据\n- §4.7 GSM1K: \"interpret with caution\" + Cook's D 已足够；R1 的 cherry-picking 指控不成立\n\n### §5 Discussion\n- §5.1: 需深化因果推理——difficulty–direction ρ=−0.597 为 capability evolution 提供证据，应正式讨论\n- §5.2: 简洁有效，无需修改\n- §5.3: 阈值推导需更多 empirical grounding；建议补充 case study\n\n### §6 Conclusion\n- 目前紧凑有效，但如果 headline claim 改为范围，Conclusion 需相应更新\n\n### Limitations\n- 已涵盖核心局限但可补充：(1) difficulty-dependent injection 模型的定性影响；(2) 2024 cohort random split 的缺失\n\n### Appendix\n- Appendix D (DEFF) 内容应在正文中更显著引用\n- Figure 6 (ρ-degradation) 对 §5.3 audit protocol 有支撑作用，但 page 16 布局需优化\n",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.5"
  }
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-22T12:33:12.488281+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4775
}
```

</details>

---


### Assistant

_source line 818 · 2026-05-22T12:33:26.656746+00:00_

审稿报告已投递至 Research Director。

**Round 15 审稿完成**。两位 Reviewer 独立给出 **3.5 (Borderline Conference)**，交叉回应后维持。

核心发现：
- **3 个 Must-Fix**: (1) DEFF 透明度——正文需报告 ~27–31% 而非单点 31%；(2) "instability" 因果归因过度——需弱化措辞；(3) ρ≈0.997 与 31% DIF 的 practical impact 张力——需 case study
- **8 个 Should-Fix**: 多维度辩护、novelty 前置、Discussion 深度、Abstract 密度、术语一致性、injection 生态效度、2024 random split、non-uniform DIF pattern
- **修改路径**: 解决 MF1–3 + SF1–2 后可达 4.0 (Conference)；否则更适合 Findings (3.0)

交叉回应纠正了 R1 的两个事实性错误（Cohen's d 数值、GSM1K 相关系数），Review Director 据此将多维度混淆从 Must-Fix 降为 Should-Fix，并驳回了 GSM1K cherry-picking 指控。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 81

## Round 81

2 recorded events


### User

_source line 819 · 2026-05-22T12:33:29.321276+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **3 个 AGREE**：N1（DEFF 不确定性，但"掩盖"偏强）、N3（因果归因过度）、W1/W3/W4
- **2 个 REBUT**：
  - N2 的多维度论证包含两个事实性错误（Cohen's d range 和 Humanities/Other 比例均不符合论文数据），建议降为 Should-Fix
  - W2 的 GSM1K "cherry-picking" 指控基于错误的 r 值（R1 写 r=−0.17，论文实际是 r=−0.478）
- **Questions**：Q3 和 Q5 反驳（论文已回答/已采纳 purified MH），其余同意或补充

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 820 · 2026-05-22T12:33:45.581196+00:00_

审稿报告已投递至 Research Director。

**Round 15 审稿总结**：

- **评分**: 3.5 / 5 (Borderline Conference)，两位 Reviewer 独立收敛
- **3 个 Must-Fix**: DEFF 透明度（headline 31% vs 下界 13.5%）、因果归因过度、ρ≈0.997 vs 31% 实际影响力张力
- **8 个 Should-Fix**: 多维度辩护、新颖性定位、Discussion 深度、Abstract 密度、术语一致性、injection ecological validity、2024 random split、non-uniform DIF pattern
- **修改路径**: 解决 3 个 MF + 前 2 个 SF 后可提升至 4.0 (Conference)；否则更适合 Findings track

Issue tracker 已同步更新（`artifacts/review_issues.yaml`），3 个 R14 issue 标记为 resolved（Gema et al. 已讨论、IRT θ 已降级为 sensitivity check、GSM1K 已添加 Cook's D）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 82

## Round 82

54 recorded events


### User

_source line 821 · 2026-05-22T13:03:54.751069+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-22T13:04:01.491853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 823 · 2026-05-22T13:04:01.543531+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 824 · 2026-05-22T13:04:07.428647+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 825 · 2026-05-22T13:04:07.479890+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 826 · 2026-05-22T13:04:13.369905+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-22T13:04:13.420679+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-22T13:04:17.744043+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 829 · 2026-05-22T13:04:17.744830+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-22T13:04:18.148831+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 831 · 2026-05-22T13:04:18.250626+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-22T13:04:24.538239+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions",
  "allowed_domains": "['aclweb.org', 'openreview.net', '2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions",
    "allowed_domains": "['aclweb.org', 'openreview.net', '2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 833 · 2026-05-22T13:04:28.552377+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex && ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/submitted.pdf 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_YAML\"",
  "description": "Check paper files and review issues tracker existence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex && ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/submitted.pdf 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_YAML\"",
    "description": "Check paper files and review issues tracker existence"
  }
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-22T13:04:28.605291+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 835 · 2026-05-22T13:04:28.857248+00:00_

-rw-r--r-- 1 ubuntu ubuntu 815 May 21 19:15 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex
41 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex
-rw-r--r-- 1 ubuntu ubuntu 635404 May 22 13:01 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_9/submitted.pdf
---
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 304
}
```

</details>

---


### Tool result

_source line 836 · 2026-05-22T13:04:31.274098+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

Based on the search results, here's information about ACL Rolling Review (ARR) 2026 submission guidelines:

## Overview
ACL Rolling Review (ARR) invites the submission of long and short papers on substantial, original, and unpublished research in all aspects of Computational Linguistics and Natural Language Processing.

## Two-Step Review Process
The reviewing process uses a centralized rolling review system with deadlines on the 15th of each month, where an action editor handles review and revision and resubmission of papers is allowed. Publication venues (conferences or workshops) then accept a subset of submitted papers for presentation.

## Anonymity Requirements
A paper can only be (re)submitted to ARR if it has been anonymous for at least a month before the first submission, and it must remain anonymous while it is under review. Authors may allow their anonymized submission to be publicly available on OpenReview while it is under ARR review.

## Platform
ARR will u
…[truncated 316 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 6735
}
```

</details>

---
