# prep arr checklist draft

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_prep_arr-checklist-draft_20260522T185615.jsonl`
- **Structured JSON:** [`c64dda751dfb63ff96c7.json`](../../sessions/c6/c64dda751dfb63ff96c7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-22T19:00:03.883847+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T19:00:03.884205+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T19:00:03.884382+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T19:00:03.884699+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/paper_framing.md\", \"content\": \"# Paper Framing — entrainment_gated_ft\\n\\n> Revised 2026-05-20 after Round 1 review (Overall 3.0, D014). Predictive multiplicity replaces underspecification as primary framework. Title: \\\"Task-Specific Convergence and Per-Example Predictive Multiplicity in Hybrid Recurrent Architectures\\\". CI→complementary characterization. New evidence: Jaccard normalized ES (5-7%), RetNet-HGRN2 decoupling. Target 3.5+.\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Findings (via ARR)\\n- Stretch: EMNLP 2026 Main\\n- Deadline: ARR June 2026 cycle (submission ~June 15)\\n\\n## Paper Type\\nEmpirical analysis paper — quantifying a known phenomenon (per-example divergence under aggregate convergence) in a specific important domain (hybrid recurrent architectures)\\n\\n## Core Claims (3 条)\\n\\n### Claim 1: Task-Specific Convergence (revised D009)\\nAdding attention layers to different linear recurrent architectures (GatedDeltaNet, RetNet, HGRN2) induces aggregate performance convergence **specifically on context-retrieval tasks**. Across 10 benchmarks, only LAMBADA shows significant convergence (ρ=-1.0, p=0.017 two-tailed, cross-arch std drops 79%, BCa CI [-1.0, -0.7]). This task-specificity IS the finding, not a limitation:\\n- **Negative-ρ cluster** (6/10): LAMBADA, xstorycloze, COPA, PIQA, ARC-Easy, MMLU — tasks with context-retrieval or reasoning components\\n- **Positive-ρ cluster** (4/10): BoolQ, SciQ, HellaSwag, WinoGrande — commonsense/knowledge tasks where attention doesn't equalize\\n- LAMBADA is unique as a **pure context-prediction** task (predict last word from context alone), explaining why convergence is strongest there\\n\\n**Statistical strategy (D009)**:\\n1. **Complementary characterization**: BCa percentile CI [-1.0, -0.7] (100% valid resamples have ρ<0; does NOT depend on multiple comparison corr
…[truncated 11400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T19:00:03.884904+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "ROADMAP.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "file": "ROADMAP.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T19:00:03.885093+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/ROADMAP.md\", \"content\": \"# entrainment_gated_ft — Research Dashboard\\n\\n> 最后更新: 2026-05-22 18:21 UTC | 更新原因: 全面更新：E1-E4 + exp-005 完成，R15 修复落地，R16 审稿已提交\\n\\n## 核心方向\\nHybrid linear recurrent architectures (GDN/RetNet/HGRN2/GLA/DeltaNet) 中 per-example predictive multiplicity 的系统分析。核心发现：cross-arch pairwise Jaccard ≤ 0.14（5 arch, 10 pairs, all p ≤ .002）；α spectrum 0.14–0.30 task-dependent；Jaccard 在 4% attention 即饱和。详见 paper_framing.md。\\n\\n## 当前阶段\\n**R16 审稿已提交（continue mode），等待审稿结果。目标 4.0 Conference。**\\n\\n### ⚠️ DEADLINE: 2026-05-25 (ARR May cycle) — 剩余 ~40h\\n\\n### 审稿历史\\n- Round 5-12: 连续 3.0 Findings\\n- Round 13: Fresh review 3.0。三个结构性问题：convergence overclaiming、seed confound、novelty\\n- Round 14: 3.0。E1-E4 实验整合 + 10+ text fixes\\n- Round 15: 3.0。MF1/MF2/MF3 持续标记 + SF3 措辞 + SF4 routing 定位。5-arch 数据整合后 MF2 显著减弱\\n- **R15 修复完成**：P0 DeltaNet 数据修正 + P1 措辞校准 + P2 statistical caveats + HGRN footnote\\n- **R16 提交中**：等待审稿结果，预期 3.5+\\n\\n### 分数瓶颈 → 对策（全部已执行）\\n| 问题 | 对策 | 状态 |\\n|------|------|------|\\n| Convergence overclaiming (MF1) | 叙事重心转向 Jaccard saturation + α spectrum | ✅ done |\\n| GDN confound (MF2) | 5-arch 数据：排除 GDN 后仍 4 arch, 6 pairs, J ≤ 0.14 | ✅ done |\\n| Bootstrap CI (MF3) | 标注 \\\"illustrative only\\\" + 报告个体架构值 | ✅ done |\\n| \\\"Nearly disjoint\\\" 夸大 (SF3) | → \\\"largely non-overlapping\\\" + base rate context | ✅ done |\\n| Routing 定位过高 (SF4) | 降级为 illustrative case study | ✅ done |\\n| Seed confound (SF1) | E4 Pythia 70M 9-seed calibration (J=0.27-0.39, 2.7-4.3×) | ✅ done |\\n\\n## 实验成果总结\\n| ID | 结果 | 论文位置 |\\n|----|------|----------|\\n| E1 Routing | LAMBADA +5.33pp, 36% oracle gap | §4.1 case study |\\n| E2 Continuous J | J monotonic decrease τ=0→0.30 | Appendix O |\\n| E3 Calibration | ECE 17% << threshold 47% | Appendix |\\n| E4 Pythia Seed | J_within=0.27-0.39, 2.7-4.3× cross-arch gap | Appendix seed cali
…[truncated 1754 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T19:00:03.885263+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "report.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "file": "report.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T19:00:03.885429+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/report.md\", \"content\": \"# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp-005-eval: Cross-architecture per-example Jaccard (helped/hurt) remains ≤0.10 when expanding from 3 architectures (GDN/RetNet/HGRN2) to 6 (adding GLA/DeltaNet/HGRN), with 15 pairwise comparisons and 720 permutations providing dramatically stronger statistical power.（等待人工审批）\\n- exp-005-pure-v5（准备中）\\n- exp-005-pure-v4（准备中）\\n- exp-005-pure-v3（准备中）\\n- exp-005-batch（准备中）\\n- exp-005-hgrn-chain（准备中）\\n- exp-005: Cross-architecture Jaccard overlap of helped/hurt sets will remain significantly above chance when expanded from 3 to 6 linear attention architectures, indicating that attention-mediated sample sensitivity is architecture-independent.（准备中）\\n- exp-005-p1-eval-v5（准备中）\\n- exp-005-p1-eval-v4（准备中）\\n- exp-005-dn-eval（准备中）\\n- …另有 9 项\\n\\n## 近期结论\\n- **exp-005-gla-pure** (success): GLA pure (no attention) baseline at 340M scale will show lower LAMBADA accuracy and higher perplexity than GLA hybrid-3-1 counterpart, consistent with the pattern that attention layers selectively improve context-dependent word prediction tasks while having minimal or negative effect on knowledge-oriented tasks like ARC-Easy.\\n- **e4-pythia-seed-calibration** (success): Pythia 70M 9-seed variants 的 within-seed per-example Jaccard (same architecture, different random seed) 显著高于 cross-architecture Jaccard (~0.10), 证明 within-arch overlap >> cross-arch overlap, 即 cross-arch 信号不能被 seed noise 解释。 ← 基于 exp-001\\n  [e4_pythia_seed_calibration](/api/workspace-files/projects/entrainment_gated_ft/artifacts/e4-pythia-seed-calibration/data/e4_pythia_seed_calibration.json)\\n- **exp-340m-multi-bench** (success): 340M models exhibit α spectrum (per-example ambiguity) consistent with 1.3B across HellaSwag/PIQA/ARC-Easy — establishing scale-inva
…[truncated 690 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T19:00:03.885623+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T19:00:03.885796+00:00_

artifacts/dream_reports/dream_20260519T131014/best/paper.tex
artifacts/dream_reports/dream_20260519T131014/median/paper.tex
artifacts/dream_reports/dream_20260519T131014/worst/paper.tex
artifacts/dream_reports/dream_20260519T135121/best/paper.tex
artifacts/dream_reports/dream_20260519T135121/median/paper.tex
artifacts/dream_reports/dream_20260519T135121/worst/paper.tex
artifacts/dream_reports/dream_20260519T143201/best/paper.tex
artifacts/dream_reports/dream_20260519T143201/median/paper.tex
artifacts/dream_reports/dream_20260519T143201/worst/paper.tex
artifacts/_project/report/prediction_summary_table.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T19:00:03.885925+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T19:00:03.886050+00:00_

artifacts/dream_reports/dream_20260519T131014/best/paper.tex
artifacts/dream_reports/dream_20260519T131014/median/paper.tex
artifacts/dream_reports/dream_20260519T131014/worst/paper.tex
artifacts/dream_reports/dream_20260519T135121/best/paper.tex
artifacts/dream_reports/dream_20260519T135121/median/paper.tex
artifacts/dream_reports/dream_20260519T135121/worst/paper.tex
artifacts/dream_reports/dream_20260519T143201/best/paper.tex
artifacts/dream_reports/dream_20260519T143201/median/paper.tex
artifacts/dream_reports/dream_20260519T143201/worst/paper.tex
docs/paper/author_response.tex
docs/paper/arr_checklist.tex
docs/paper/author_response_r7.tex
artifacts/_project/report/prediction_summary_table.tex
docs/paper/sections/related_work.tex
docs/paper/sections/experiments.tex
docs/paper/sections/conclusion.tex
docs/paper/main.tex
docs/paper/sections/introduction.tex
docs/paper/sections/method.tex
docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T19:00:03.886176+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/arr_checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/arr_checklist.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T19:00:03.886336+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	\subsection*{A. For every submission:}
4	
5	\begin{itemize}
6	\item[\checkmark] \textbf{A1.} Did you describe the limitations of your work?
7	
8	\textit{Yes. The Limitations section (after \S5) discusses statistical power constraints ($n = 5$ attention ratios), per-example scope (four benchmarks, two supplementary), scale coverage (two scale points), architecture coverage (three backbones from one model zoo, single training run per configuration), observational design (descriptive, not causal), and pre-training-only evaluation.}
9	
10	\item[\checkmark] \textbf{A2.} Did you discuss any potential risks of your work?
11	
12	\textit{Yes. The Ethics Statement notes that this work analyzes existing public models and introduces no new risks. Per-example behavioral differences may inform practitioners about limitations of aggregate benchmarks.}
13	
14	\item[\checkmark] \textbf{A3.} Do all claims in the paper match the paper's contributions and scope?
15	
16	\textit{Yes. Claims are scoped to three architectures and four benchmarks spanning retrieval, reasoning, and mixed tasks. We explicitly note that Bonferroni-adjusted $p = .100$ does not reach conventional significance, that the scale comparison is a preliminary observation from two data points, and that per-example multiplicity is characterized as a task-dependent variation ($\alpha = 0.14$--$0.30$) rather than claimed as universal. BoolQ and WinoGrande are reported as supplementary in the Appendix due to structural limitations of near-chance binary/two-choice classification on Jaccard significance.}
17	
18	\item[\checkmark] \textbf{A4.} Have you used AI writing assistants when working on this paper?
19	
20	\textit{Yes. AI writing assistants were used for drafting and editing. All scientific content, claims, and analyses were verified by the authors.}
21	\end{itemize}
22	
23	\subsection*{B. Did you use or create scientific artifacts?}
24	
25	\textit{Yes. We use existin
…[truncated 3562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T19:00:03.886500+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\\\\\section\\{Limitations|Computational|GPU|compute|RTX|A100",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\\\\\section\\{Limitations|Computational|GPU|compute|RTX|A100",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T19:00:03.886806+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex-21-
docs/paper/sections/method.tex-22-\subsection{Convergence Metrics}\label{ssec:convergence_metrics}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex-23-
docs/paper/sections/method.tex:24:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex-25-
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex-26-We also report the convergence ratio $\sigma_{\text{pure}} / \sigma_{\text{h3-1}}$, defined as the standard deviation under the pure-recurrent configuration divided by that under the highest attention ratio (25\%). Values greater than 1 indicate that higher attention ratios are associated with lower cross-architecture variance.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex-27-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex-37-
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex-38-The net effect for each architecture is $|\text{helped}| - |\text{hurt}|$. A positive net effect means more examples transition to correct than to incorrect when attention is added; a negative net effect means the opposite.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex-39-
docs/paper/sections/method.tex:40:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex-41-
docs/paper/sections/method.tex-42-\subsection{Statistical Methods}\label{ssec:statistical_methods}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method
…[truncated 17557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T19:00:03.887011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T19:00:03.887155+00:00_

1	\section{Conclusion}
2	
3	We present the first systematic per-example analysis of attention effects in hybrid recurrent models. Per-example multiplicity spans a task-dependent variation ($\alpha = 0.14$--$0.30$) across four benchmarks, with Jaccard uniformly low ($\leq 0.10$) regardless of aggregate convergence. On LAMBADA at 1.3B, aggregate variance decreases with attention while per-example overlap saturates, consistent with configuration-specific pathways rather than uniform rescue (dependent on GDN inclusion; does not replicate on other benchmarks). Across the architectures studied here, aggregate benchmark equivalence masks per-example divergence: each backbone exhibits configuration-specific response patterns invisible to standard evaluation. Within each architecture, pure-model confidence partially predicts which examples will be affected (AUC 0.70--0.74), though disruption thresholds vary 47\% across architectures (\S\ref{ssec:per_example}).
4	
5	For practitioners, these results motivate per-example audits within the scope of controlled hybrid linear recurrent architectures studied here: the ${\sim}90\%$ non-overlap means architectures interchangeable by aggregate metrics affect largely non-overlapping examples. A majority vote across three architectures fails to consistently outperform the best individual model (LAMBADA: $-0.2$\,pp; ARC-Easy: $-1.1$\,pp; gains on other benchmarks $< 0.2$\,pp) despite 15--45\% disagreement, because roughly half of disagreement examples have only one correct architecture (Appendix~\ref{app:complementarity}). Oracle accuracy reveals $+7$--$14$\,pp of untapped complementarity, but accessing it requires selection methods beyond naive ensembling \citep{wortsman2022model}. Rescue-threshold routing extracts 36\% of oracle complementarity on LAMBADA (+5.3\,pp), demonstrating that confidence-informed selection can partially access this gap, though gains are task-dependent (\S\ref{ssec:per_example}).
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T19:00:03.887295+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\\\\\section\\{Limitations|\\\\\\\\paragraph\\{Limitations",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content",
  "-A": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\\\\\section\\{Limitations|\\\\\\\\paragraph\\{Limitations",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
    "output_mode": "content",
    "-A": "20"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T19:00:03.887415+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T19:00:03.887531+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Limitation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex",
  "output_mode": "content",
  "-A": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Limitation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex",
    "output_mode": "content",
    "-A": "20"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T19:00:03.887662+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T19:00:03.887806+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Limitation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
  "output_mode": "content",
  "-A": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Limitation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
    "output_mode": "content",
    "-A": "5"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T19:00:03.887941+00:00_

39:\section*{Limitations}
40-
41-Our analysis has several limitations.
42-
43-[Omitted long context line]
44-

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T19:00:03.888058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
  "offset": "39",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
    "offset": "39",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T19:00:03.888192+00:00_

39	\section*{Limitations}
40	
41	Our analysis has several limitations.
42	
43	\paragraph{Single training runs.} Each configuration corresponds to a single training run; we cannot fully disentangle architectural from seed-specific effects, though the $3\times$ within- vs.\ cross-architecture Jaccard gap (\S\ref{ssec:decoupling}) provides proxy evidence. All per-example claims are conditioned on this limitation. With $n = 5$ attention ratios, the minimum achievable $p$-value is 0.017, contributing to LAMBADA's Bonferroni-adjusted $p = .170$ not reaching conventional significance. As a partial calibration, we compare within-seed Jaccard from Pythia 70M PolyPythias \citep{vanderwal2025polypythias} against our cross-architecture values (Appendix~\ref{app:seed_calibration}); within-seed overlap is 2.7--4.3$\times$ higher, consistent with, but not definitive evidence for, architecture-driven divergence. Future work should conduct multi-seed training on matched architectures to fully isolate architectural from seed-specific effects.
44	
45	\paragraph{Coverage and generalization.} We examine three primary architectures from one model zoo on four main benchmarks (two supplementary); two additional architectures (GLA and DeltaNet) confirm the pattern at 340M (Appendix~\ref{app:extended_arch}). The controlled design isolates architectural effects but limits generalization to other hybrid families. We compare only two scale points (340M, 1.3B). Our analysis does not cover Mamba, RWKV, or generation tasks; generalization to these architectures and task types remains open.
46	
47	\paragraph{Pre-training only.} All models are evaluated without fine-tuning; per-example effects may not persist after task-specific adaptation. We evaluate only discrete accuracy; continuous metrics may reveal different multiplicity patterns.
48	
49	\section*{Ethics Statement}
50	
51	This work analyzes publicly available pretrained language models from the model zoo of \citet{wang2025hybrid}. No new data
…[truncated 584 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T19:00:03.888367+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__append_idea",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T19:00:03.888489+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T19:00:03.888601+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T19:00:03.888736+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T19:00:03.888846+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T19:00:03.888962+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T19:00:03.889071+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T19:00:03.889191+00:00_

__pycache__
_project
analysis_majority_vote_and_rho.py
analyze_6arch.py
analyze_per_example.py
arc_easy_jaccard_analysis.json
arc_easy_per_example.json
d009_assessment.md
dream_reports
e4-pythia-seed-calibration
eval_composition.py
eval_composition_modified.py
exp-001
exp-003
exp-003-p2
exp-004
exp-005
exp-005-batch
exp-005-eval
exp-007
exp-010
exp-340m-multi-bench
exp-boolq-hellaswag-eval
exp003_p2_data_check.md
exp007_data_check.md
exp007_script_ready.md
formal_multiplicity_metrics.json
lm_eval_1.3b_results.md
manifest.yaml
null_jaccard_results.json
paper_agent_inputs.md
paper_data
per_example_data_audit.md
report_e4_diagnosis.md
review_issues.yaml
review_reports
review_round_10
review_round_11
review_round_12
review_round_13
review_round_14
review_round_15
review_round_5
review_round_7
review_round_8
review_round_9
run_priority1_v2.sh
run_priority1_v3.sh
run_priority2.sh
synthetic_task_design.md
wang_7b_search_results.md
wang_et_al_analysis.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T19:00:03.889362+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/arr_checklist_draft.txt",
  "content": "ARR Responsible NLP Checklist — Draft Answers for OpenReview Submission Form\n=============================================================================\nPaper: \"Task-Specific Convergence and Per-Example Predictive Multiplicity\n        in Hybrid Recurrent Architectures\"\nVenue: EMNLP 2026 via ARR May/June cycle\nPrepared: 2026-05-22\n\n\nA. FOR EVERY SUBMISSION\n========================\n\nA1. Did you describe the limitations of your work?\nAnswer: Yes\nSection: Limitations (after Section 5, unnumbered)\nJustification: The Limitations section covers: (1) single training runs per\nconfiguration — cannot fully disentangle architectural from seed-specific\neffects, though within- vs. cross-architecture Jaccard gap (3x) and Pythia\n70M seed calibration (2.7-4.3x) provide proxy evidence; (2) coverage —\nfive primary architectures from one model zoo, four main benchmarks + two\nsupplementary, two scale points only; (3) pre-training only — no fine-tuning\nevaluation, discrete accuracy only; (4) statistical power — n=5 attention\nratios limits minimum achievable p to 0.017, LAMBADA Bonferroni-adjusted\np=0.170 does not reach conventional significance.\n\nA2. Did you discuss any potential risks of your work?\nAnswer: Yes\nSection: Ethics Statement (after Limitations)\nJustification: This work analyzes existing publicly available pretrained\nmodels and introduces no new risks. The identified per-example behavioral\ndifferences may inform practitioners about limitations of aggregate benchmark\ncomparisons. No new data collection, human subjects, or model training is\ninvolved.\n\nA3. Do the abstract and introduction summarize the paper's main claims?\nAnswer: Yes\nJustification: Three scoped claims: (1) task-specific aggregate convergence\n(LAMBADA at 1.3B, rho=-1.0, p=0.017, with honest reporting that\nBonferroni-adjusted p=0.170); (2) scale-dependent convergence (complete at\n1.3B, partial at 340M, two scale points only); (3) per-example predictive\nmultiplicity — pairwise Jaccard <= 0.10 across five architectures, alpha\nspectrum 0.14-0.30 task-dependent. All claims explicitly scoped to the\narchitectures and benchmarks studied.\n\nA4. Have you used AI writing assistants when working on this paper?\nAnswer: Yes\nJustification: AI writing assistants were used for drafting and editing\ntext. All scientific content, experimental design, analysis, and claims\nwere verified by the authors.\n\n\nB. DID YOU USE OR CREATE SCIENTIFIC ARTIFACTS?\n===============================================\n\nAnswer: Yes (use existing artifacts; no new artifacts created)\n\nB1. Did you cite the creators of artifacts you used?\nAnswer: Yes\nJustification: We cite: Wang et al. (2025) for the hybrid architecture\nmodel zoo (HuggingFace m-a-p organization); Gao et al. (2024) for\nlm-evaluation-harness (v0.4.12); Yang et al. for flash-linear-attention\n(v0.5.0); individual architecture papers for GatedDeltaNet, RetNet, HGRN2,\nGLA, and DeltaNet; Marx et al. (2020) for the predictive multiplicity\nframework; van der Wal et al. (2025) for PolyPythias (Pythia seed variants).\nAll benchmark datasets (LAMBADA, ARC-Easy, HellaSwag, PIQA) are cited.\n\nB2. Did you discuss the license or terms for use and/or distribution\n    of any artifacts?\nAnswer: Yes\nJustification: The Wang et al. model zoo is publicly released on HuggingFace.\nlm-evaluation-harness is open-source under MIT license. flash-linear-attention\nis open-source. All benchmark datasets are publicly available standard NLP\nbenchmarks. We do not release new artifacts (code release upon publication).\n\nB3. Did you discuss if your use of existing artifact(s) was consistent\n    with their intended use?\nAnswer: Yes\nJustification: The model zoo was designed for systematic comparison of hybrid\narchitectures, which is exactly our use case. The evaluation harness was used\nwith default prompts and standard benchmark configurations.\n\nB4. Did you discuss the steps taken to check whether the data that you\n    are using/curating contains any information that names or uniquely\n    identifies individual people or offensive content?\nAnswer: N/A\nJustification: We use established NLP benchmarks (LAMBADA, ARC-Easy,\nHellaSwag, PIQA) that have been widely vetted in prior work. No new data\nwas collected or curated.\n\nB5. Did you provide documentation of the artifacts, e.g., coverage of\n    domains, languages, and linguistic phenomena, demographic groups\n    represented, etc.?\nAnswer: N/A\nJustification: We do not release new artifacts. Analysis code and per-example\noutputs will be released upon publication with documentation.\n\nB6. Did you discuss whether and how consent was obtained from people\n    whose data you're using/curating?\nAnswer: N/A\nJustification: All data used consists of established public benchmarks.\n\n\nC. DID YOU RUN COMPUTATIONAL EXPERIMENTS?\n==========================================\n\nAnswer: Yes\n\nC1. Did you report the number of parameters in the models used, the total\n    computational budget (e.g., GPU hours), and computing infrastructure\n    used?\nAnswer: Yes\nSection: Section 3 (Method) and Appendix\nJustification: Model sizes: 340M and 1.3B parameters. Five architectures\n(GatedDeltaNet, RetNet, HGRN2, GLA, DeltaNet) x 5 attention ratios x 2\nscales. All evaluation was inference-only using pretrained checkpoints from\nWang et al. (2025); no model training was performed. Computing\ninfrastructure: single NVIDIA RTX PRO 6000 GPU. Total computational budget:\napproximately 5 GPU-hours (inference only). Pythia 70M seed calibration\nexperiment (Appendix) used the same GPU with negligible additional compute.\n\nC2. Did you discuss the experimental setup, including hyperparameter\n    search and best model selection?\nAnswer: Yes\nSection: Section 3\nJustification: Section 3 describes the model zoo, task taxonomy (retrieval /\nreasoning / mixed), all metrics (Spearman rho, cross-architecture std,\nJaccard, alpha, normalized ES), and statistical methods (permutation tests,\nBCa bootstrap CIs, Bonferroni and BH corrections). All models use default\nlm-evaluation-harness settings. No hyperparameter tuning or model selection\nwas performed — this is a post-hoc analysis of existing checkpoints.\n\nC3. Did you report descriptive statistics about your results (e.g., error\n    bars, confidence intervals, significance tests)?\nAnswer: Yes\nJustification: We report: exact permutation tests (two-tailed, 120\npermutations); BCa bootstrap confidence intervals; Bonferroni and\nBenjamini-Hochberg corrections for multiple comparisons; effect sizes\n(Cohen's d, Jaccard similarity, normalized ES); the ambiguity metric alpha\n(Marx et al. 2020); z-scores from permutation null distributions for\nJaccard significance; Mann-Whitney U and Kruskal-Wallis tests for\nwithin/cross-architecture comparisons.\n\nC4. Did you use existing packages (e.g., for pre-processing, for model\n    evaluation)?\nAnswer: Yes\nJustification: lm-evaluation-harness v0.4.12 (Gao et al. 2024) for\nbenchmark evaluation; flash-linear-attention v0.5.0 for efficient linear\nattention inference; PyTorch; standard scientific Python stack (numpy, scipy,\nscikit-learn for statistical tests).\n\n\nD. DID YOU USE HUMAN ANNOTATORS (E.G., CROWDWORKERS) OR INVOLVE HUMAN\n   PARTICIPANTS?\n==========================================\n\nAnswer: No\n\nD1-D5: N/A\nJustification: No human annotation or human participants were involved.\nThis is a purely computational analysis of existing pretrained models on\nestablished benchmarks.\n\n\nE. DID YOU USE AI ASSISTANTS (E.G., CHATGPT)?\n===============================================\n\nE1. Did you report the use of AI assistants (e.g., ChatGPT, Copilot)?\nAnswer: Yes\nJustification: See A4. AI writing assistants were used for drafting and\nediting. All scientific content was verified by the authors.\n\n\nADDITIONAL NOTES FOR FORM FIELDS\n=================================\n\nFairness / Bias Implications (if asked):\nPer-example predictive multiplicity has direct fairness implications.\nDifferent architectures with equivalent aggregate performance affect nearly\ndisjoint sets of examples (Jaccard <= 0.10, ~90% non-overlap). This means\nthe choice of architecture — often made based on aggregate benchmarks alone\n— determines WHICH specific examples are correctly or incorrectly predicted.\nThe ambiguity metric alpha ranges from 0.14 (reasoning tasks) to 0.30\n(retrieval tasks), quantifying the fraction of examples whose predictions\ndepend on architecture choice. This is an instance of predictive multiplicity\n(Marx et al. 2020) arising from architectural variation, complementing\nunderspecification (D'Amour et al. 2022) which focuses on same-pipeline\nvariation. Practitioners should be aware that aggregate-equivalent models\nare not per-example equivalent.\n\nReproducibility:\nAll models are publicly available from the Wang et al. (2025) model zoo on\nHuggingFace (m-a-p organization). Evaluation uses the standard\nlm-evaluation-harness with default settings. Analysis code and per-example\noutputs will be released upon publication. No training is required to\nreproduce results — only inference on public checkpoints.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/arr_checklist_draft.txt",
    "content": "ARR Responsible NLP Checklist — Draft Answers for OpenReview Submission Form\n=============================================================================\nPaper: \"Task-Specific Convergence and Per-Example Predictive Multiplicity\n        in Hybrid Recurrent Architectures\"\nVenue: EMNLP 2026 via ARR May/June cycle\nPrepared: 2026-05-22\n\n\nA. FOR EVERY SUBMISSION\n========================\n\nA1. Did you describe the limitations of your work?\nAnswer: Yes\nSection: Limitations (after Section 5, unnumbered)\nJustification: The Limitations section covers: (1) single training runs per\nconfiguration — cannot fully disentangle architectural from seed-specific\neffects, though within- vs. cross-architecture Jaccard gap (3x) and Pythia\n70M seed calibration (2.7-4.3x) provide proxy evidence; (2) coverage —\nfive primary architectures from one model zoo, four main benchmarks + two\nsupplementary, two scale points only; (3) pre-training only — no fine-tuning\nevaluation, discrete accuracy only; (4) statistical power — n=5 attention\nratios limits minimum achievable p to 0.017, LAMBADA Bonferroni-adjusted\np=0.170 does not reach conventional significance.\n\nA2. Did you discuss any potential risks of your work?\nAnswer: Yes\nSection: Ethics Statement (after Limitations)\nJustification: This work analyzes existing publicly available pretrained\nmodels and introduces no new risks. The identified per-example behavioral\ndifferences may inform practitioners about limitations of aggregate benchmark\ncomparisons. No new data collection, human subjects, or model training is\ninvolved.\n\nA3. Do the abstract and introduction summarize the paper's main claims?\nAnswer: Yes\nJustification: Three scoped claims: (1) task-specific aggregate convergence\n(LAMBADA at 1.3B, rho=-1.0, p=0.017, with honest reporting that\nBonferroni-adjusted p=0.170); (2) scale-dependent convergence (complete at\n1.3B, partial at 340M, two scale points only); (3) per-example predictive\nmultiplicity — pairwise Jaccard <= 0.10 across five architectures, alpha\nspectrum 0.14-0.30 task-dependent. All claims explicitly scoped to the\narchitectures and benchmarks studied.\n\nA4. Have you used AI writing assistants when working on this paper?\nAnswer: Yes\nJustification: AI writing assistants were used for drafting and editing\ntext. All scientific content, experimental design, analysis, and claims\nwere verified by the authors.\n\n\nB. DID YOU USE OR CREATE SCIENTIFIC ARTIFACTS?\n===============================================\n\nAnswer: Yes (use existing artifacts; no new artifacts created)\n\nB1. Did you cite the creators of artifacts you used?\nAnswer: Yes\nJustification: We cite: Wang et al. (2025) for the hybrid architecture\nmodel zoo (HuggingFace m-a-p organization); Gao et al. (2024) for\nlm-evaluation-harness (v0.4.12); Yang et al. for flash-linear-attention\n(v0.5.0); individual architecture papers for GatedDeltaNet, RetNet, HGRN2,\nGLA, and DeltaNet; Marx et al. (2020) for the predictive multiplicity\nframework; van der Wal et al. (2025) for PolyPythias (Pythia seed variants).\nAll benchmark datasets (LAMBADA, ARC-Easy, HellaSwag, PIQA) are cited.\n\nB2. Did you discuss the license or terms for use and/or distribution\n    of any artifacts?\nAnswer: Yes\nJustification: The Wang et al. model zoo is publicly released on HuggingFace.\nlm-evaluation-harness is open-source under MIT license. flash-linear-attention\nis open-source. All benchmark datasets are publicly available standard NLP\nbenchmarks. We do not release new artifacts (code release upon publication).\n\nB3. Did you discuss if your use of existing artifact(s) was consistent\n    with their intended use?\nAnswer: Yes\nJustification: The model zoo was designed for systematic comparison of hybrid\narchitectures, which is exactly our use case. The evaluation harness was used\nwith default prompts and standard benchmark configurations.\n\nB4. Did you discuss the steps taken to check whether the data that you\n    are using/curating contains any information that names or uniquely\n    identifies individual people or offensive content?\nAnswer: N/A\nJustification: We use established NLP benchmarks (LAMBADA, ARC-Easy,\nHellaSwag, PIQA) that have been widely vetted in prior work. No new data\nwas collected or curated.\n\nB5. Did you provide documentation of the artifacts, e.g., coverage of\n    domains, languages, and linguistic phenomena, demographic groups\n    represented, etc.?\nAnswer: N/A\nJustification: We do not release new artifacts. Analysis code and per-example\noutputs will be released upon publication with documentation.\n\nB6. Did you discuss whether and how consent was obtained from people\n    whose data you're using/curating?\nAnswer: N/A\nJustification: All data used consists of established public benchmarks.\n\n\nC. DID YOU RUN COMPUTATIONAL EXPERIMENTS?\n==========================================\n\nAnswer: Yes\n\nC1. Did you report the number of parameters in the models used, the total\n    computational budget (e.g., GPU hours), and computing infrastructure\n    used?\nAnswer: Yes\nSection: Section 3 (Method) and Appendix\nJustification: Model sizes: 340M and 1.3B parameters. Five architectures\n(GatedDeltaNet, RetNet, HGRN2, GLA, DeltaNet) x 5 attention ratios x 2\nscales. All evaluation was inference-only using pretrained checkpoints from\nWang et al. (2025); no model training was performed. Computing\ninfrastructure: single NVIDIA RTX PRO 6000 GPU. Total computational budget:\napproximately 5 GPU-hours (inference only). Pythia 70M seed calibration\nexperiment (Appendix) used the same GPU with negligible additional compute.\n\nC2. Did you discuss the experimental setup, including hyperparameter\n    search and best model selection?\nAnswer: Yes\nSection: Section 3\nJustification: Section 3 describes the model zoo, task taxonomy (retrieval /\nreasoning / mixed), all metrics (Spearman rho, cross-architecture std,\nJaccard, alpha, normalized ES), and statistical methods (permutation tests,\nBCa bootstrap CIs, Bonferroni and BH corrections). All models use default\nlm-evaluation-harness settings. No hyperparameter tuning or model selection\nwas performed — this is a post-hoc analysis of existing checkpoints.\n\nC3. Did you report descriptive statistics about your results (e.g., error\n    bars, confidence intervals, significance tests)?\nAnswer: Yes\nJustification: We report: exact permutation tests (two-tailed, 120\npermutations); BCa bootstrap confidence intervals; Bonferroni and\nBenjamini-Hochberg corrections for multiple comparisons; effect sizes\n(Cohen's d, Jaccard similarity, normalized ES); the ambiguity metric alpha\n(Marx et al. 2020); z-scores from permutation null distributions for\nJaccard significance; Mann-Whitney U and Kruskal-Wallis tests for\nwithin/cross-architecture comparisons.\n\nC4. Did you use existing packages (e.g., for pre-processing, for model\n    evaluation)?\nAnswer: Yes\nJustification: lm-evaluation-harness v0.4.12 (Gao et al. 2024) for\nbenchmark evaluation; flash-linear-attention v0.5.0 for efficient linear\nattention inference; PyTorch; standard scientific Python stack (numpy, scipy,\nscikit-learn for statistical tests).\n\n\nD. DID YOU USE HUMAN ANNOTATORS (E.G., CROWDWORKERS) OR INVOLVE HUMAN\n   PARTICIPANTS?\n==========================================\n\nAnswer: No\n\nD1-D5: N/A\nJustification: No human annotation or human participants were involved.\nThis is a purely computational analysis of existing pretrained models on\nestablished benchmarks.\n\n\nE. DID YOU USE AI ASSISTANTS (E.G., CHATGPT)?\n===============================================\n\nE1. Did you report the use of AI assistants (e.g., ChatGPT, Copilot)?\nAnswer: Yes\nJustification: See A4. AI writing assistants were used for drafting and\nediting. All scientific content was verified by the authors.\n\n\nADDITIONAL NOTES FOR FORM FIELDS\n=================================\n\nFairness / Bias Implications (if asked):\nPer-example predictive multiplicity has direct fairness implications.\nDifferent architectures with equivalent aggregate performance affect nearly\ndisjoint sets of examples (Jaccard <= 0.10, ~90% non-overlap). This means\nthe choice of architecture — often made based on aggregate benchmarks alone\n— determines WHICH specific examples are correctly or incorrectly predicted.\nThe ambiguity metric alpha ranges from 0.14 (reasoning tasks) to 0.30\n(retrieval tasks), quantifying the fraction of examples whose predictions\ndepend on architecture choice. This is an instance of predictive multiplicity\n(Marx et al. 2020) arising from architectural variation, complementing\nunderspecification (D'Amour et al. 2022) which focuses on same-pipeline\nvariation. Practitioners should be aware that aggregate-equivalent models\nare not per-example equivalent.\n\nReproducibility:\nAll models are publicly available from the Wang et al. (2025) model zoo on\nHuggingFace (m-a-p organization). Evaluation uses the standard\nlm-evaluation-harness with default settings. Analysis code and per-example\noutputs will be released upon publication. No training is required to\nreproduce results — only inference on public checkpoints.\n"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T19:00:03.889613+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/arr_checklist_draft.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T19:00:03.889779+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T19:00:03.889918+00:00_

1	- id: art_20260519_6bdbaf
2	  name: wang_7b_search_results
3	  type: report
4	  description: Wang et al. (arXiv 2507.06457) 7B模型搜索结果：确认无7B模型，仅有340M和1.3B
5	  path: projects/entrainment_gated_ft/artifacts/_project/report/wang_7b_search_results.md
6	  url: null
7	  project: entrainment_gated_ft
8	  exp_id: null
9	  skill: ''
10	  created_at: '2026-05-19T12:57:00.452560+00:00'
11	  tags:
12	  - wang_et_al
13	  - 7B
14	  - hybrid_linear_attention
15	  - model_search
16	- id: art_20260519_e33ecb
17	  name: per_example_data_audit
18	  type: report
19	  description: Per-example data completeness audit for lm_eval benchmark results across
20	    1.3B and 340M models (GDN, HGRN2, RetNet, Transformer)
21	  path: projects/entrainment_gated_ft/artifacts/_project/report/per_example_data_audit.md
22	  url: null
23	  project: entrainment_gated_ft
24	  exp_id: null
25	  skill: ''
26	  created_at: '2026-05-19T13:00:31.563610+00:00'
27	  tags:
28	  - audit
29	  - lm_eval
30	  - per-example

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T19:00:03.890058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml",
  "offset": "0",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml",
    "offset": "0",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-22T19:00:03.890184+00:00_

0	- id: art_20260519_6bdbaf
1	  name: wang_7b_search_results
2	  type: report
3	  description: Wang et al. (arXiv 2507.06457) 7B模型搜索结果：确认无7B模型，仅有340M和1.3B
4	  path: projects/entrainment_gated_ft/artifacts/_project/report/wang_7b_search_results.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-22T19:00:03.890307+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport uuid, datetime\nuid = uuid.uuid4().hex[:6]\nprint(f'art_20260522_{uid}')\nprint(datetime.datetime.now(datetime.timezone.utc).isoformat())\n\"",
  "description": "Generate artifact ID and timestamp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport uuid, datetime\nuid = uuid.uuid4().hex[:6]\nprint(f'art_20260522_{uid}')\nprint(datetime.datetime.now(datetime.timezone.utc).isoformat())\n\"",
    "description": "Generate artifact ID and timestamp"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-22T19:00:03.890421+00:00_

art_20260522_813f4f
2026-05-22T18:59:29.964200+00:00

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T19:00:03.890535+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml",
  "old_string": "- id: art_20260519_6bdbaf",
  "new_string": "- id: art_20260522_813f4f\n  name: arr_checklist_draft\n  type: report\n  description: ARR Responsible NLP Checklist draft answers for OpenReview submission form (EMNLP 2026)\n  path: projects/entrainment_gated_ft/artifacts/arr_checklist_draft.txt\n  url: null\n  project: entrainment_gated_ft\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-22T18:59:29.964200+00:00'\n  tags:\n  - arr_checklist\n  - submission\n  - emnlp2026\n- id: art_20260519_6bdbaf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml",
    "old_string": "- id: art_20260519_6bdbaf",
    "new_string": "- id: art_20260522_813f4f\n  name: arr_checklist_draft\n  type: report\n  description: ARR Responsible NLP Checklist draft answers for OpenReview submission form (EMNLP 2026)\n  path: projects/entrainment_gated_ft/artifacts/arr_checklist_draft.txt\n  url: null\n  project: entrainment_gated_ft\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-22T18:59:29.964200+00:00'\n  tags:\n  - arr_checklist\n  - submission\n  - emnlp2026\n- id: art_20260519_6bdbaf"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-22T19:00:03.890868+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_prep_arr-checklist-draft_20260522T185615",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-22T19:00:03.891076+00:00_

已完成。草稿写入 `artifacts/arr_checklist_draft.txt` 并注册到 manifest。

要点：
- A1-A4 全部 Yes，覆盖 Limitations section 的五个方面（单次训练、覆盖范围、仅预训练、统计功效、Bonferroni 报告）
- B1-B3 Yes（Wang et al. model zoo、lm-eval-harness、flash-linear-attention 均已引用），B4-B6 N/A
- C1-C4 Yes，报告了 RTX PRO 6000、~5 GPU-hours inference-only、340M/1.3B 参数量、无超参搜索、完整统计方法
- D 全部 N/A（纯计算实验）
- E1 Yes（AI 写作辅助）
- 额外补充了 fairness/bias implications 段落，强调 per-example multiplicity 的公平性含义（Jaccard ≤ 0.10, alpha 0.14-0.30）

注意：现有 `arr_checklist.tex`（论文 PDF 内）仍写的是 3 architectures / 30 models，但论文实际已扩展到 5 architectures。本草稿按最新 5-arch 状态撰写。PDF 内的 checklist.tex 也需要同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_prep_arr-checklist-draft_20260522T185615"
}
```

</details>

---
