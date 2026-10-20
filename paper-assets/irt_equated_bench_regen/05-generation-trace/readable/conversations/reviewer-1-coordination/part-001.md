# Reviewer 1 coordination — Part 1 of 3

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

[Transcript overview](../reviewer-1-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/f4/f44f4d47dd150062eb07.json)

## Round 1

## Round 1

48 recorded events


### User

_source line 1 · 2026-05-20T21:35:42.976909+00:00_

[Round 1 审稿请求]:
## Review Assignment: R1 — Methods & Experiments

**Paper:** "Psychometric Detection and Regeneration of Contaminated LLM Benchmark Items: Differential Item Functioning at Scale"

**Your focus:** Methods rigor, experimental validity, statistical soundness, and results interpretation.

**Venue standard:** Top ML venue (e.g., ICLR/NeurIPS), acceptance rate ~25%, 6-point scale (1=Strong Reject … 6=Strong Accept).

### Paper Summary

The paper reframes LLM benchmark contamination as a psychometric problem — contaminated items exhibit Differential Item Functioning (DIF), becoming differentially easier for exposed model cohorts beyond ability predictions. Key contributions: (1) first large-scale IRT fit diagnostics for LLM populations (5,219 models × 12,508 MMLU items), showing architecture heterogeneity is the primary obstacle and decoder-only stratification yields acceptable fit (RMSEA 0.068); (2) DIF+ConStat dual-signal ensemble (AUROC 0.72); (3) semi-synthetic validation framework revealing simulation-to-real gap (TPR drops 0.15); (4) pilot-scale bifactor IRT equating for benchmark regeneration (ρ=0.91 on holdout); (5) three-parameter power surface (R²=0.89) characterizing detection boundaries.

### Key Experimental Results to Scrutinize

**IRT Fit (Table 1):** Full-pop RMSEA=0.105 (poor), decoder-only=0.068 (acceptable), bifactor=0.062. Architecture stratification resolves the heterogeneity problem.

**DIF Detection (Tables 3-4):** 485 ETS-C flags on temporal cohort. Within-family analysis shows 42% overlap — nearly half of DIF flags may reflect capability growth rather than contamination. MMLU-CF validation weak (κ=0.14, r=0.18).

**RL Robustness (Tables 5-6):** Alignment-RL robust (N=477, retention 0.88, DeLong p=0.008). Reasoning-RL only 13 models — "preliminary evidence" framing. Per-model detectors (ConStat, Min-K%) degrade to ~0.50 AUROC on reasoning-RL while DIF maintains 0.79.

**ConStat (Table 8):** AUROC 0.67 (non-RL), 0.52 (reasoning-RL). 38% overlap with DIF flags.

**DVD (Table 9):** AUROC 0.56 overall, excluded from primary ensemble. Reported as negative result.

**Ensemble (Table 10):** DIF+ConStat union AUROC 0.72, TPR 0.58 at δ≥0.8. Adding DVD degrades (AUROC 0.70, FPR increases). Coverage gap at reasoning-RL + medium effects.

**Semi-synthetic (Tables 13-15):** TPR=0.58 at δ≥1.4 (vs 0.73 in simulation). Power surface R²=0.89 — exploitation rate is strongest determinant.

**Cross-benchmark GSM8K (Table 12):** r=0.36 (p=0.004) with GSM1K gap. Corroborating but not conclusive.

**Bifactor + Regeneration (Tables 16-18):** Student simulation ρ=0.78 >> prompt-based 0.28. Holdout ρ=0.91 but systematic quality degradation (factor loading 0.41 vs 0.50, discrimination 0.95 vs 1.18). Critical replacement threshold 28%.

### Experiment Coverage Assessment

The review_context.yaml lists 11 imagined experiments. The paper covers all of them:
- plan_001 (real data DIF MMLU) → §4.1-4.2 ✓
- plan_002 (RL robustness) → §4.3 ✓
- plan_003a (ConStat) → §4.4 ✓
- plan_003b (DVD) → §4.5 ✓
- plan_003c (ensemble fusion) → §4.6 ✓
- plan_004 (GSM8K cross-benchmark) → §4.7 ✓
- plan_005 (bifactor equating) → §4.9 ✓
- plan_006 (item generation) → §4.9 ✓
- plan_007 (cumulative Bayesian DIF) → §5.2 ✓
- plan_008 (graceful degradation) → §4.10 ✓
- plan_009 (item-focused trees) → §5.1 ✓
- plan_010 (architecture stratified) → §4.1 ✓
- plan_011 (semi-synthetic) → §4.8 ✓

All experiments covered, some at abbreviated depth in supplementary sections.

### Questions for Your Review

1. Is the 2PL IRT model appropriate for this population? Are there violations beyond architecture heterogeneity (e.g., local dependence across MMLU items within subjects)?
2. Is the Mantel-Haenszel DIF procedure with ETS classification well-justified? Are there more powerful alternatives that should have been considered?
3. The semi-synthetic validation is the primary ground-truth mechanism — is the injection protocol sound? Does injecting contamination into a matrix that may already contain contamination bias results?
4. The 42% within-family overlap is presented as a limitation, but could it undermine the entire DIF approach? How should this be interpreted?
5. With only 13 reasoning-RL models, is the "preliminary evidence" framing sufficient, or is this a critical gap that undermines the paper's timeliness?
6. The ensemble AUROC of 0.72 — is this competitive enough as a standalone contribution?
7. Student simulation calibration (ρ=0.78) — is this a meaningful contribution or incremental over Li et al. (2025)?
8. Are the statistical tests appropriate (DeLong, TOST, bootstrap CI)?

Provide a structured review with: Summary, Strengths (numbered), Weaknesses (numbered with severity: major/minor), Questions for Authors, Missing Experiments/Analyses, and a preliminary score (1-6).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-20T21:35:54.660323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-20T21:35:56.316682+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1656
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-20T21:35:56.317131+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-20T21:35:56.367630+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-20T21:36:02.291953+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-20T21:36:03.296017+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/chart/dif_power_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/chart/dif_power_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_power_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_diagnostic_pvalue_dist.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/chart/dif_diagnostic_pvalue_dist.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/chart/dif_phase2_param_distribution.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_phase2_param_distribution.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/chart/dif_phase2_power_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_phase2_power_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T2050
…[truncated 18 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-20T21:36:03.296389+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-20T21:36:03.899539+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-20T21:36:03.953692+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ICLR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ICLR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-20T21:36:09.691745+00:00_

Web search results for query: "ICLR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ICLR Workshop 2026 - Reviewer Guidelines","url":"https://sites.google.com/view/icbinb-2026/reviewer-guidelines"},{"title":"📈 ICLR 2026 Submission Storm: 19,797 Papers, New Review Rules, and the Age of AI Convergence | CSPaper Forum","url":"https://forum.cspaper.org/topic/169/iclr-2026-submission-storm-19-797-papers-new-review-rules-and-the-age-of-ai-convergence"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"ICLR 2026 Area Chair Guide","url":"https://iclr.cc/Conferences/2026/AreaChairGuide"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"Insights from the ICLR Peer Review and Rebuttal Process","url":"https://arxiv.org/pdf/2511.15462"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"}]

Based on the search results, here's what I found about ICLR 2026 reviewer guidelines:

## Scoring System

The overall rating for ICLR 2026 is mapped to {0, 2, 4, 6, 8, 10}, which represents a change from previous years.

## Review Criteria

Numerical scores are provided for soundness, presentation, contribution, confidence, and overall rating. Additionally, the new formula reviewers adopt is: Novelty × Depth × Presentation × Reproducibility.

## Review Requirements

Reviewers are asked that their reviews are timely and substantive, and that they follow the reviewing guidelines. The review should include a short summary of the paper's contributions and key findings, strengths and weaknesses of the submission, recommendations with justification according to the criteria, and optional feedback to help authors improve their work.

## Ethical Gui
…[truncated 309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5738
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-20T21:36:23.091389+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-20T21:36:23.091796+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-20T21:36:23.745875+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-20T21:36:23.796428+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/worst/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-20T21:36:31.677048+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://iclr.cc/Conferences/2026/ReviewerGuide",
  "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and any specific guidelines for how reviewers should evaluate papers. Include all numerical scales and their descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://iclr.cc/Conferences/2026/ReviewerGuide",
    "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and any specific guidelines for how reviewers should evaluate papers. Include all numerical scales and their descriptions."
  }
}
```

</details>

---


### Tool call

_source line 17 · 2026-05-20T21:36:32.831520+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/paper.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-5",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/paper.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-5",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 18 · 2026-05-20T21:36:37.448885+00:00_

# ICLR 2026 Reviewer Evaluation Framework

Based on the provided guide, the document does **not contain a specific numerical rating scale or formal scoring rubric** with defined dimensions.

## Available Evaluation Guidance

The reviewer guide directs assessors to answer **four key questions**:

1. "What is the specific question and/or problem tackled by the paper?"
2. "Is the approach well motivated, including being well-placed in the literature?"
3. "Does the paper support the claims?" (evaluating correctness and rigor)
4. "What is the significance of the work?" (assessing contribution and community value)

## Review Structure (Not Scoring Scales)

The guide prescribes organizing reviews with these components:

- Summary of claimed contributions
- Enumeration of strengths and weaknesses
- "Clearly state your initial recommendation (accept or reject)" with key justifications
- Supporting arguments
- Clarification questions for authors
- Constructive improvement suggestions

## Notable Gaps

The document emphasizes that "submissions bring value...when they convincingly demonstrate new, relevant, impactful knowledge" without requiring state-of-the-art results, but provides no numerical rating system, confidence scales, or specific evaluation metrics for standardized scoring.

A separate review form exists for **Code of Ethics reporting** and **LLM usage disclosure**, but numerical criteria aren't detailed in this guide.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5771
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-20T21:36:38.053949+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 363.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 344.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 313.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 288.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 286.4}], \"total_pages\": 10, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5222
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-20T21:36:45.634889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 21 · 2026-05-20T21:36:46.191035+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 22 · 2026-05-20T21:36:47.096438+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1461
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-20T21:36:47.098820+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-20T21:36:47.099215+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-20T21:36:47.552633+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-20T21:36:47.553089+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-20T21:36:48.258200+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-20T21:36:48.258848+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-20T21:36:48.613512+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-20T21:36:55.239723+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/paper.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "6-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/paper.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "6-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-20T21:36:55.641647+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 276.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 267.0}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 248.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 245.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p10.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 335.1}], \"total_pages\": 10, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-20T21:36:59.152217+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-20T21:36:59.856679+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-20T21:36:59.857125+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-20T21:37:00.360371+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-20T21:37:00.360868+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-20T21:37:01.266340+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-20T21:37:01.266805+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-20T21:37:01.721757+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-20T21:37:01.722225+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-20T21:37:02.075884+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-20T21:41:47.630123+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 审稿意见：Methods & Experiments\n\n**Paper:** \"Psychometric Detection and Regeneration of Contaminated LLM Benchmark Items: DIF-Based Detection, Multi-Signal Ensemble, and IRT-Equated Benchmark Regeneration\"\n\n---\n\n## Summary\n\n本文将 LLM 基准测试污染检测重新定义为心理测量学问题，核心思路是污染题目会表现出差异项目功能 (DIF)——对接触过训练数据的模型群体而言，这些题目变得异常容易，超出能力预测。论文在 5,219 个模型 × 12,508 个 MMLU 题目上进行了大规模 IRT 拟合诊断，构建了 DIF+ConStat 双信号集成检测器（AUROC 0.72），提出半合成验证框架，并通过 bifactor IRT 等值进行基准再生（holdout ρ=0.91）。实验覆盖面广（11 个实验组件），从 DIF 检测到集成融合、跨基准验证、贝叶斯累积 DIF、到题目生成与退化分析，涉及完整的技术栈。\n\n---\n\n## Preliminary Score: 4/6 (Weak Accept)\n\n**一句话总结：** 概念新颖、规模令人印象深刻，但 DIF 标记的效度验证不充分（外部验证 κ=0.14）、推理 RL 鲁棒性声明样本严重不足（N=13），使核心贡献的可信度受损。\n\n---\n\n## Strengths (numbered)\n\n**S1. 跨学科框架创新性极高。** 将 psychometrics 中成熟的 DIF 方法论引入 LLM 污染检测，是一个真正的概念贡献。DIF 在群体层面运作（population-level behavioral patterns），对单模型级别的输出平滑具有理论上的天然鲁棒性——这个论点在 §3.2 中论述清晰，且通过 Table 3 得到了经验支持（DIF AUROC 0.82-0.91 vs ConStat 0.51-0.75 on RL models）。\n\n**S2. 分析规模与覆盖面。** 5,219 模型 × 12,508 题目的矩阵是目前已知最大的 IRT-for-LLM 分析之一。论文没有停留在单一实验，而是系统地覆盖了 IRT 拟合诊断（§4.1）、RL 鲁棒性（§4.2）、多信号集成（§5）、跨基准验证（§6.1）、半合成验证（§6.2）、累积贝叶斯 DIF（§6.3）、等值再生（§7）和退化分析（§7.3）——实验设计的完备性值得肯定。\n\n**S3. 架构异质性的诊断与解决。** Table 5 清晰展示了全群体 RMSEA=0.105（poor fit）而 decoder-only 子群 RMSEA=0.068（acceptable），并正确识别架构异质性为 IRT 拟合的主要障碍。分层后 spurious DIF 减少 24%（Table 6），这是一个有方法论价值的发现。\n\n**S4. 诚实报告负面结果。** DVD 检测器 AUROC 0.56 作为负面结果报告（Table 9），集成加入 DVD 后 AUROC 从 0.72 降为 0.70——论文没有回避这些结果。within-family 46% overlap、κ=0.14 外部验证等也均如实呈现。这种透明度在该领域不常见。\n\n**S5. 退化分析提供实用边界。** Table 18 的 graceful degradation 分析给出了明确的操作阈值（~35% 替换为临界点），ρ 以 ~0.003/百分点线性退化——这为实际部署提供了可操作的安全边界。\n\n---\n\n## Weaknesses (numbered, with severity)\n\n**W1 [Major] DIF 标记效度未得到充分验证——核心贡献的可信度存疑。**\n- **位置：** §4.1 Within-Family Analysis (p.4), §6.1 GSM8K validation (p.7-8)\n- **问题：** 论文的核心声明是 DIF 标记对应污染题目，但外部验证极其薄弱：\n  - Director summary 提及 MMLU-CF 验证 κ=0.14, r=0.18——这本质上是随机一致水平，几乎没有验证价值\n  - GSM8K 交叉验证 r=0.36（Table 11）统计显著但效应量弱，仅为\"暗示性佐证\"\n  - Within-family 分析显示 46% overlap（p.4），意味着 54% 的全群体 DIF 标记可能仅由架构差异或能力增长驱动，而非真正的污染\n- **为什么影响接收：** 如果无法区分 DIF 标记中的\"真污染\"和\"能力进步\"，整个检测管线的 precision 就是未知的。论文没有提供正式的 precision 估计（除了 Table 1 中的一列，但该 precision 的 ground truth 来源不明）。\n- **建议：** (1) 使用已知干净的模型对（如同一 checkpoint 的 base vs fine-tuned on MMLU subset）构建有标注的验证集；(2) 明确讨论 κ=0.14 为何不构成否定证据（如果论文认为 MMLU-CF 本身有问题，应论证）。\n\n**W2 [Major] 推理-RL 鲁棒性声明严重欠缺统计效力（N=13）。**\n- **位置：** Table 3 (p.5), §4.2\n- **问题：** RL 鲁棒性是论文的核心卖点之一（Abstract、§1、§3.2 均重点强调），但推理-RL 分析仅基于 13 个模型。在 N=13 下，AUROC 估计的 95% CI 约为 ±0.15-0.20（DeLong 正态近似）。论文报告 DIF AUROC 0.81 vs ConStat 0.51——但置信区间可能大幅重叠。DeLong p=0.002 是在对齐-RL（N=477）上报告的，不是在推理-RL（N=13）上。\n- **为什么影响接收：** 推理-RL（o1、DeepSeek-R1 等）恰恰是论文声称最重要的前沿场景。在该场景下证据最薄弱，形成论文最大的\"论点-证据\"缺口。\"Preliminary evidence\"框架虽然诚实，但一个 top venue 论文的核心贡献不应建立在 preliminary evidence 上。\n- **建议：** (1) 报告 N=13 下的 bootstrap CI 并讨论统计效力；(2) 如果无法获得更多推理-RL 模型，应将 RL 鲁棒性声明降级为辅助发现而非核心贡献；(3) 考虑 permutation test 而非 DeLong test 用于小样本。\n\n**W3 [Major] 半合成验证存在循环性风险。**\n- **位置：** §6.2 (p.8), Tables 12-13\n- **问题：** 半合成验证从真实 METABENCH 响应矩阵中选取\"200 clean items\"并注入已知污染。但如何确认这 200 个 items 是真正 clean 的？如果它们已经包含自然污染（考虑到论文自身估计 14.6% 的 items 有 DIF），注入的污染会叠加在现有污染之上，导致 TPR 估计向上偏倚。论文声称 semi-synthetic TPR \"consistently exceeds pure simulation by 3-8bps\"（Table 13），但这个差异可能恰好反映了 existing contamination 的叠加效应。\n- **建议：** (1) 描述\"clean item\"的选取标准，说明如何排除现有污染；(2) 用敏感性分析展示在不同 base contamination rates 下 TPR 如何变化；(3) 考虑从 non-MMLU 基准（无已知污染）构建 semi-synthetic 验证集。\n\n**W4 [Major] 2PL 模型下 MMLU 的局部独立性假设可能严重违反。**\n- **位置：** §3.1 (p.2), §4.1 (p.4)\n- **问题：** 2PL IRT 要求局部独立性——给定能力值，题目间的响应应条件独立。但 MMLU 的 57 个学科内部，题目高度相关（同一学科的抽象代数题之间、同一学科的道德推理题之间）。论文在 §7.1 的 bifactor 模型中引入了学科特定因子来处理这个问题（p.9），但 §4.1-4.2 的核心 DIF 分析使用的是普通 2PL，未检测或处理局部依赖。\n- 违反局部独立性会膨胀 Mantel-Haenszel 统计量，导致 DIF 假阳性率升高——这与 W1 中的效度问题叠加。\n- **建议：** (1) 用 Yen's Q3 或 Chen & Thissen 的 LD 统计量检测局部依赖程度；(2) 展示在不同 LD 校正下 DIF 标记的稳定性；(3) 或者直接在 bifactor 模型上做 DIF 分析（§7.1 已有拟合好的 bifactor 模型）。\n\n**W5 [Minor] Mantel-Haenszel 程序的选择未充分论证。**\n- **位置：** §3.2 (p.3)\n- **问题：** MH 是最经典的 DIF 方法之一，但也有明确的局限性：(1) 只能检测 uniform DIF（item characteristic curves 平行移动），对 non-uniform DIF（交叉 ICC）不敏感；(2) 在分层数增加时效力下降。论文的场景（5,219 模型、能力分布可能高度非正态）可能存在 non-uniform DIF。更强大的替代方案包括 logistic regression DIF（可同时检测 uniform 和 non-uniform DIF）和 SIBTEST。论文未讨论为何选择 MH 而非这些替代。\n- **建议：** 至少用 logistic regression DIF 做一个对比实验，如果 MH 和 LR-DIF 一致则加强论点，不一致则表明 MH 可能遗漏了 non-uniform DIF。\n\n**W6 [Minor] 多重比较校正缺失。**\n- **位置：** §4.1 (p.4)\n- **问题：** 对 12,508 个题目进行 MH 检验，产生 12,508 个 p 值。论文使用 ETS 效应量分类（A/B/C）而非 p 值阈值来标记 DIF，这部分缓解了多重比较问题。但 Table 1 中仍报告了 LR p-value，且 ETS 分类的 C 类阈值（|Δ_MH| ≥ 1.5 且显著）仍涉及 p 值判断。论文应讨论 FDR 控制策略。\n\n**W7 [Minor] 集成 AUROC 0.72 的实用价值需要更多讨论。**\n- **位置：** Table 10 (p.7), §5.3\n- **问题：** AUROC 0.72 在检测任务中属于中等水平。在 FPR=0.085 的情况下，12,508 个题目中约 1,063 个会被误标为污染。论文缺乏对 positive predictive value (PPV) 在不同 base rate 下的讨论。如果真实污染率是 15%（论文估计），PPV ≈ 0.58×0.15 / (0.58×0.15 + 0.085×0.85) ≈ 0.55——约一半的标记是假阳性。\n- **建议：** 加入 PPV 曲线或基于 base rate 的 precision-recall 分析。\n\n**W8 [Minor] 再生题目质量退化的影响被低估。**\n- **位置：** Table 16 (p.9), §7.1-7.2\n- **问题：** 替换题目的因子载荷从 0.50 降至 0.41（-18%），区分度从 1.18 降至 0.95（-19%）。这意味着再生基准在心理测量学意义上不是等值的——它是一个较弱版本。ρ=0.91 的 holdout 相关看似不错，但排名位移的分布（89% 的模型移动 ≤3 个位置）意味着 11% 的模型会有显著排名变化。\n- **建议：** (1) 分析排名变化是否与模型能力水平或架构类型相关（即退化是否系统性偏向某些模型）；(2) 讨论因子载荷/区分度下降对测试信息函数 (TIF) 的影响。\n\n---\n\n## Questions for Authors\n\n**Q1.** Within-family 分析中 46% 的 overlap 率应如何正确解读？这 46% 是指全群体 DIF 标记中有 46% 被 within-family 分析确认，还是 within-family 标记中有 46% 也出现在全群体分析中？方向性对结论有根本影响。\n\n**Q2.** κ=0.14（与 MMLU-CF 的一致性）为何不构成对 DIF 方法的否定证据？MMLU-CF 是目前已知最直接的污染标注，如果 DIF 标记与之几乎无关，需要给出有说服力的解释。\n\n**Q3.** Table 3 中推理-RL 的 DeLong 检验 p 值具体是多少？是否独立于对齐-RL 的 p=0.002 报告？\n\n**Q4.** 半合成验证中\"clean items\"的选取标准是什么？是否使用了 DIF 分析本身来选取 clean items——如果是，则存在循环论证。\n\n**Q5.** Bifactor 模型（§7.1）中学科特定因子的方差解释比例是多少？如果学科特定因子解释了大量方差，这是否意味着在普通 2PL 上的 DIF 分析（§4.1）受到了严重的局部依赖污染？\n\n**Q6.** 论文提到 IFT（§5.1）识别的中位分割点为 2023 年 9 月，与已知的大规模网页爬取时间线一致。但这也可能对应 GPT-4 发布后的模型能力跳跃——如何区分这两种解释？\n\n---\n\n## Missing Experiments/Analyses\n\n1. **局部依赖诊断（Yen's Q3 或类似）**：验证 2PL 在 MMLU 上的局部独立性假设是否合理。\n2. **在 bifactor 模型上进行 DIF 分析**：论文已拟合了 bifactor 模型（§7.1），应在该模型上重做 DIF 并对比 2PL 结果。\n3. **已知污染模型的 controlled validation**：用同一 base model 的 clean 版本和 fine-tuned-on-MMLU 版本构建真正的 ground truth。\n4. **PPV/NPV at plausible base rates**：将 AUROC 转化为实际决策性能。\n5. **Non-uniform DIF 检测**：用 logistic regression DIF 或 IRT-LR 检测交叉 DIF。\n6. **推理-RL 的 bootstrap CI**：量化小样本下 AUROC 估计的不确定性。\n7. **替换题目质量退化的系统性分析**：TIF 对比、能力估计偏差分析。\n\n---\n\n## 维度打分（基于 ICLR review 标准 + Director 指定的 6 分制）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Novelty / Originality | 5/6 | DIF 用于 LLM 污染检测是真正的跨学科创新，bifactor equating for regeneration 也有新意 |\n| Soundness / Correctness | 3/6 | 核心 DIF 标记的效度验证不充分（κ=0.14）；2PL 局部独立性假设可能严重违反；推理-RL 样本太小 |\n| Significance / Impact | 4/6 | 问题重要且实用，但 AUROC 0.72 + 再生质量退化限制了实际影响 |\n| Clarity / Presentation | 4/6 | 实验覆盖面广但10页内压缩过多内容（11个实验组件），部分关键细节只能在 Director summary 中找到而非论文正文 |\n| Reproducibility | 3/6 | 依赖 METABENCH 数据但未明确可复现步骤；IRT 拟合的具体实现细节不足（优化器、收敛标准等） |\n| Overall | **4/6 (Weak Accept)** | 概念贡献显著，实验规模令人印象深刻，但方法论核心（DIF 效度验证、RL 鲁棒性统计效力、局部独立性）存在需要作者回应的重要缺陷 |\n\n**Confidence: 4/5** — 我熟悉 IRT 和 DIF 方法论，对实验设计的评估有较高把握；对 METABENCH 数据集的具体特性了解有限。\n\n---\n\n## 总结判断\n\n这是一篇有野心、有创意的论文，将心理测量学的经典工具引入了一个 ML 社区非常关心的问题。跨学科的概念贡献是清晰的。但\"DIF 标记 = 污染\"这个核心等式缺乏令人信服的外部验证（κ=0.14 本质上是随机水平），推理-RL 鲁棒性——论文最强调的实用卖点——仅有 N=13 的支持。如果作者能提供更有力的效度验证（如 controlled contamination 实验）并坦诚量化推理-RL 下的统计不确定性，这篇论文将有力地向 Accept 移动。当前状态下，Weak Accept——概念够强，执行需加固。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 审稿意见：Methods & Experiments\n\n**Paper:** \"Psychometric Detection and Regeneration of Contaminated LLM Benchmark Items: DIF-Based Detection, Multi-Signal Ensemble, and IRT-Equated Benchmark Regeneration\"\n\n---\n\n## Summary\n\n本文将 LLM 基准测试污染检测重新定义为心理测量学问题，核心思路是污染题目会表现出差异项目功能 (DIF)——对接触过训练数据的模型群体而言，这些题目变得异常容易，超出能力预测。论文在 5,219 个模型 × 12,508 个 MMLU 题目上进行了大规模 IRT 拟合诊断，构建了 DIF+ConStat 双信号集成检测器（AUROC 0.72），提出半合成验证框架，并通过 bifactor IRT 等值进行基准再生（holdout ρ=0.91）。实验覆盖面广（11 个实验组件），从 DIF 检测到集成融合、跨基准验证、贝叶斯累积 DIF、到题目生成与退化分析，涉及完整的技术栈。\n\n---\n\n## Preliminary Score: 4/6 (Weak Accept)\n\n**一句话总结：** 概念新颖、规模令人印象深刻，但 DIF 标记的效度验证不充分（外部验证 κ=0.14）、推理 RL 鲁棒性声明样本严重不足（N=13），使核心贡献的可信度受损。\n\n---\n\n## Strengths (numbered)\n\n**S1. 跨学科框架创新性极高。** 将 psychometrics 中成熟的 DIF 方法论引入 LLM 污染检测，是一个真正的概念贡献。DIF 在群体层面运作（population-level behavioral patterns），对单模型级别的输出平滑具有理论上的天然鲁棒性——这个论点在 §3.2 中论述清晰，且通过 Table 3 得到了经验支持（DIF AUROC 0.82-0.91 vs ConStat 0.51-0.75 on RL models）。\n\n**S2. 分析规模与覆盖面。** 5,219 模型 × 12,508 题目的矩阵是目前已知最大的 IRT-for-LLM 分析之一。论文没有停留在单一实验，而是系统地覆盖了 IRT 拟合诊断（§4.1）、RL 鲁棒性（§4.2）、多信号集成（§5）、跨基准验证（§6.1）、半合成验证（§6.2）、累积贝叶斯 DIF（§6.3）、等值再生（§7）和退化分析（§7.3）——实验设计的完备性值得肯定。\n\n**S3. 架构异质性的诊断与解决。** Table 5 清晰展示了全群体 RMSEA=0.105（poor fit）而 decoder-only 子群 RMSEA=0.068（acceptable），并正确识别架构异质性为 IRT 拟合的主要障碍。分层后 spurious DIF 减少 24%（Table 6），这是一个有方法论价值的发现。\n\n**S4. 诚实报告负面结果。** DVD 检测器 AUROC 0.56 作为负面结果报告（Table 9），集成加入 DVD 后 AUROC 从 0.72 降为 0.70——论文没有回避这些结果。within-family 46% overlap、κ=0.14 外部验证等也均如实呈现。这种透明度在该领域不常见。\n\n**S5. 退化分析提供实用边界。** Table 18 的 graceful degradation 分析给出了明确的操作阈值（~35% 替换为临界点），ρ 以 ~0.003/百分点线性退化——这为实际部署提供了可操作的安全边界。\n\n---\n\n## Weaknesses (numbered, with severity)\n\n**W1 [Major] DIF 标记效度未得到充分验证——核心贡献的可信度存疑。**\n- **位置：** §4.1 Within-Family Analysis (p.4), §6.1 GSM8K validation (p.7-8)\n- **问题：** 论文的核心声明是 DIF 标记对应污染题目，但外部验证极其薄弱：\n  - Director summary 提及 MMLU-CF 验证 κ=0.14, r=0.18——这本质上是随机一致水平，几乎没有验证价值\n  - GSM8K 交叉验证 r=0.36（Table 11）统计显著但效应量弱，仅为\"暗示性佐证\"\n  - Within-family 分析显示 46% overlap（p.4），意味着 54% 的全群体 DIF 标记可能仅由架构差异或能力增长驱动，而非真正的污染\n- **为什么影响接收：** 如果无法区分 DIF 标记中的\"真污染\"和\"能力进步\"，整个检测管线的 precision 就是未知的。论文没有提供正式的 precision 估计（除了 Table 1 中的一列，但该 precision 的 ground truth 来源不明）。\n- **建议：** (1) 使用已知干净的模型对（如同一 checkpoint 的 base vs fine-tuned on MMLU subset）构建有标注的验证集；(2) 明确讨论 κ=0.14 为何不构成否定证据（如果论文认为 MMLU-CF 本身有问题，应论证）。\n\n**W2 [Major] 推理-RL 鲁棒性声明严重欠缺统计效力（N=13）。**\n- **位置：** Table 3 (p.5), §4.2\n- **问题：** RL 鲁棒性是论文的核心卖点之一（Abstract、§1、§3.2 均重点强调），但推理-RL 分析仅基于 13 个模型。在 N=13 下，AUROC 估计的 95% CI 约为 ±0.15-0.20（DeLong 正态近似）。论文报告 DIF AUROC 0.81 vs ConStat 0.51——但置信区间可能大幅重叠。DeLong p=0.002 是在对齐-RL（N=477）上报告的，不是在推理-RL（N=13）上。\n- **为什么影响接收：** 推理-RL（o1、DeepSeek-R1 等）恰恰是论文声称最重要的前沿场景。在该场景下证据最薄弱，形成论文最大的\"论点-证据\"缺口。\"Preliminary evidence\"框架虽然诚实，但一个 top venue 论文的核心贡献不应建立在 preliminary evidence 上。\n- **建议：** (1) 报告 N=13 下的 bootstrap CI 并讨论统计效力；(2) 如果无法获得更多推理-RL 模型，应将 RL 鲁棒性声明降级为辅助发现而非核心贡献；(3) 考虑 permutation test 而非 DeLong test 用于小样本。\n\n**W3 [Major] 半合成验证存在循环性风险。**\n- **位置：** §6.2 (p.8), Tables 12-13\n- **问题：** 半合成验证从真实 METABENCH 响应矩阵中选取\"200 clean items\"并注入已知污染。但如何确认这 200 个 items 是真正 clean 的？如果它们已经包含自然污染（考虑到论文自身估计 14.6% 的 items 有 DIF），注入的污染会叠加在现有污染之上，导致 TPR 估计向上偏倚。论文声称 semi-synthetic TPR \"consistently exceeds pure simulation by 3-8bps\"（Table 13），但这个差异可能恰好反映了 existing contamination 的叠加效应。\n- **建议：** (1) 描述\"clean item\"的选取标准，说明如何排除现有污染；(2) 用敏感性分析展示在不同 base contamination rates 下 TPR 如何变化；(3) 考虑从 non-MMLU 基准（无已知污染）构建 semi-synthetic 验证集。\n\n**W4 [Major] 2PL 模型下 MMLU 的局部独立性假设可能严重违反。**\n- **位置：** §3.1 (p.2), §4.1 (p.4)\n- **问题：** 2PL IRT 要求局部独立性——给定能力值，题目间的响应应条件独立。但 MMLU 的 57 个学科内部，题目高度相关（同一学科的抽象代数题之间、同一学科的道德推理题之间）。论文在 §7.1 的 bifactor 模型中引入了学科特定因子来处理这个问题（p.9），但 §4.1-4.2 的核心 DIF 分析使用的是普通 2PL，未检测或处理局部依赖。\n- 违反局部独立性会膨胀 Mantel-Haenszel 统计量，导致 DIF 假阳性率升高——这与 W1 中的效度问题叠加。\n- **建议：** (1) 用 Yen's Q3 或 Chen & Thissen 的 LD 统计量检测局部依赖程度；(2) 展示在不同 LD 校正下 DIF 标记的稳定性；(3) 或者直接在 bifactor 模型上做 DIF 分析（§7.1 已有拟合好的 bifactor 模型）。\n\n**W5 [Minor] Mantel-Haenszel 程序的选择未充分论证。**\n- **位置：** §3.2 (p.3)\n- **问题：** MH 是最经典的 DIF 方法之一，但也有明确的局限性：(1) 只能检测 uniform DIF（item characteristic curves 平行移动），对 non-uniform DIF（交叉 ICC）不敏感；(2) 在分层数增加时效力下降。论文的场景（5,219 模型、能力分布可能高度非正态）可能存在 non-uniform DIF。更强大的替代方案包括 logistic regression DIF（可同时检测 uniform 和 non-uniform DIF）和 SIBTEST。论文未讨论为何选择 MH 而非这些替代。\n- **建议：** 至少用 logistic regression DIF 做一个对比实验，如果 MH 和 LR-DIF 一致则加强论点，不一致则表明 MH 可能遗漏了 non-uniform DIF。\n\n**W6 [Minor] 多重比较校正缺失。**\n- **位置：** §4.1 (p.4)\n- **问题：** 对 12,508 个题目进行 MH 检验，产生 12,508 个 p 值。论文使用 ETS 效应量分类（A/B/C）而非 p 值阈值来标记 DIF，这部分缓解了多重比较问题。但 Table 1 中仍报告了 LR p-value，且 ETS 分类的 C 类阈值（|Δ_MH| ≥ 1.5 且显著）仍涉及 p 值判断。论文应讨论 FDR 控制策略。\n\n**W7 [Minor] 集成 AUROC 0.72 的实用价值需要更多讨论。**\n- **位置：** Table 10 (p.7), §5.3\n- **问题：** AUROC 0.72 在检测任务中属于中等水平。在 FPR=0.085 的情况下，12,508 个题目中约 1,063 个会被误标为污染。论文缺乏对 positive predictive value (PPV) 在不同 base rate 下的讨论。如果真实污染率是 15%（论文估计），PPV ≈ 0.58×0.15 / (0.58×0.15 + 0.085×0.85) ≈ 0.55——约一半的标记是假阳性。\n- **建议：** 加入 PPV 曲线或基于 base rate 的 precision-recall 分析。\n\n**W8 [Minor] 再生题目质量退化的影响被低估。**\n- **位置：** Table 16 (p.9), §7.1-7.2\n- **问题：** 替换题目的因子载荷从 0.50 降至 0.41（-18%），区分度从 1.18 降至 0.95（-19%）。这意味着再生基准在心理测量学意义上不是等值的——它是一个较弱版本。ρ=0.91 的 holdout 相关看似不错，但排名位移的分布（89% 的模型移动 ≤3 个位置）意味着 11% 的模型会有显著排名变化。\n- **建议：** (1) 分析排名变化是否与模型能力水平或架构类型相关（即退化是否系统性偏向某些模型）；(2) 讨论因子载荷/区分度下降对测试信息函数 (TIF) 的影响。\n\n---\n\n## Questions for Authors\n\n**Q1.** Within-family 分析中 46% 的 overlap 率应如何正确解读？这 46% 是指全群体 DIF 标记中有 46% 被 within-family 分析确认，还是 within-family 标记中有 46% 也出现在全群体分析中？方向性对结论有根本影响。\n\n**Q2.** κ=0.14（与 MMLU-CF 的一致性）为何不构成对 DIF 方法的否定证据？MMLU-CF 是目前已知最直接的污染标注，如果 DIF 标记与之几乎无关，需要给出有说服力的解释。\n\n**Q3.** Table 3 中推理-RL 的 DeLong 检验 p 值具体是多少？是否独立于对齐-RL 的 p=0.002 报告？\n\n**Q4.** 半合成验证中\"clean items\"的选取标准是什么？是否使用了 DIF 分析本身来选取 clean items——如果是，则存在循环论证。\n\n**Q5.** Bifactor 模型（§7.1）中学科特定因子的方差解释比例是多少？如果学科特定因子解释了大量方差，这是否意味着在普通 2PL 上的 DIF 分析（§4.1）受到了严重的局部依赖污染？\n\n**Q6.** 论文提到 IFT（§5.1）识别的中位分割点为 2023 年 9 月，与已知的大规模网页爬取时间线一致。但这也可能对应 GPT-4 发布后的模型能力跳跃——如何区分这两种解释？\n\n---\n\n## Missing Experiments/Analyses\n\n1. **局部依赖诊断（Yen's Q3 或类似）**：验证 2PL 在 MMLU 上的局部独立性假设是否合理。\n2. **在 bifactor 模型上进行 DIF 分析**：论文已拟合了 bifactor 模型（§7.1），应在该模型上重做 DIF 并对比 2PL 结果。\n3. **已知污染模型的 controlled validation**：用同一 base model 的 clean 版本和 fine-tuned-on-MMLU 版本构建真正的 ground truth。\n4. **PPV/NPV at plausible base rates**：将 AUROC 转化为实际决策性能。\n5. **Non-uniform DIF 检测**：用 logistic regression DIF 或 IRT-LR 检测交叉 DIF。\n6. **推理-RL 的 bootstrap CI**：量化小样本下 AUROC 估计的不确定性。\n7. **替换题目质量退化的系统性分析**：TIF 对比、能力估计偏差分析。\n\n---\n\n## 维度打分（基于 ICLR review 标准 + Director 指定的 6 分制）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Novelty / Originality | 5/6 | DIF 用于 LLM 污染检测是真正的跨学科创新，bifactor equating for regeneration 也有新意 |\n| Soundness / Correctness | 3/6 | 核心 DIF 标记的效度验证不充分（κ=0.14）；2PL 局部独立性假设可能严重违反；推理-RL 样本太小 |\n| Significance / Impact | 4/6 | 问题重要且实用，但 AUROC 0.72 + 再生质量退化限制了实际影响 |\n| Clarity / Presentation | 4/6 | 实验覆盖面广但10页内压缩过多内容（11个实验组件），部分关键细节只能在 Director summary 中找到而非论文正文 |\n| Reproducibility | 3/6 | 依赖 METABENCH 数据但未明确可复现步骤；IRT 拟合的具体实现细节不足（优化器、收敛标准等） |\n| Overall | **4/6 (Weak Accept)** | 概念贡献显著，实验规模令人印象深刻，但方法论核心（DIF 效度验证、RL 鲁棒性统计效力、局部独立性）存在需要作者回应的重要缺陷 |\n\n**Confidence: 4/5** — 我熟悉 IRT 和 DIF 方法论，对实验设计的评估有较高把握；对 METABENCH 数据集的具体特性了解有限。\n\n---\n\n## 总结判断\n\n这是一篇有野心、有创意的论文，将心理测量学的经典工具引入了一个 ML 社区非常关心的问题。跨学科的概念贡献是清晰的。但\"DIF 标记 = 污染\"这个核心等式缺乏令人信服的外部验证（κ=0.14 本质上是随机水平），推理-RL 鲁棒性——论文最强调的实用卖点——仅有 N=13 的支持。如果作者能提供更有力的效度验证（如 controlled contamination 实验）并坦诚量化推理-RL 下的统计不确定性，这篇论文将有力地向 Accept 移动。当前状态下，Weak Accept——概念够强，执行需加固。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-20T21:41:51.445823+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-20T21:41:55.970796+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-20T21:41:56.021431+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-20T21:42:03.297591+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-20T21:42:03.348252+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 48 · 2026-05-20T21:42:13.147966+00:00_

R1 审稿意见已提交至 Review Director。

**评分：4/6 (Weak Accept)**

核心发现：
- **最大优势**：DIF 用于 LLM 污染检测是真正的跨学科概念创新，实验规模（5,219×12,508）和覆盖面（11 个实验组件）令人印象深刻
- **最大问题**：(1) DIF 标记效度验证不足——与 MMLU-CF 一致性 κ=0.14 本质上是随机水平；(2) 推理-RL 鲁棒性声明仅有 N=13 支持，统计效力严重不足；(3) 2PL 局部独立性假设在 MMLU 57 学科结构下可能严重违反；(4) 半合成验证存在循环性风险

识别了 4 个 Major weakness、4 个 Minor weakness、6 个作者需回答的问题、7 个缺失实验/分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 2

## Round 2

16 recorded events


### User

_source line 49 · 2026-05-20T21:43:43.389005+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

以下是 Reviewer 2（侧重 Novelty & Related Work）的完整审稿原文。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## R2 审稿报告：Novelty & Related Work

**Overall**: 3/6 (Borderline Reject)

**一句话总结**: 将成熟心理测量工具（DIF）迁移到 LLM 污染检测的概念框架有价值，但新颖性有限、关键引用存在严重错误（至少两处作者/方法名张冠李戴），且核心贡献的实证支撑过窄，难以达到 top venue 门槛。

---

### Must-Fix 问题

**N1** [critical] 引用严重错误：多处引用的作者名和方法名与真实文献不符
- Section 4.1 "Iron-Fenced Trees (IFT) following Tets & Berger (2016)" — 真实文献为 Tutz & Berger (2016) "Item-Focussed Trees"（Psychometrika）。作者名 "Tets" 应为 "Tutz"，方法名 "Iron-Fenced Trees" 应为 "Item-Focussed Trees"。此外 "Dunn et al. (2024)" 引用的 DVD 方法，实际论文为 Liang et al. (2026)。

**N2** [critical] DIF 迁移的新颖性不足以支撑核心贡献声明
- DIF 是 Holland & Thayer (1988) 的经典技术，将"污染前/后模型群体"映射为 reference/focal group 的概念跳跃是 straightforward 的。论文未在 DIF 方法本身做出技术创新。

**N3** [critical] Ensemble (DIF+ConStat) 反而不如单独 DIF，削弱核心贡献
- Table 10 显示 DIF 单独的 TPR 在 δ≥1.4 时已达 0.78，ensemble 未带来一致性提升。将负面结果包装为正面贡献是 framing 问题。

### Should-Fix 问题

**W1** RL 鲁棒性声明的实证基础过窄（13 模型，无 bootstrap CI）
**W2** 与 Growing Pains (Zhang et al., 2026) 的区分不够清晰
**W3** Wang et al. (2026) 引用无法核实
**W4** 42% within-family overlap 混淆未得到充分解决
**W5** 贡献数量膨胀（5条应缩减为2-3条）

### 缺失的相关工作
1. MIA 用于污染检测（Shi et al., 2024 Min-K%++）
2. IRT 在 NLP/AI 评测中的先行工作（Lalor et al., 2019; Vania et al., 2021）
3. 动态/自适应 Benchmark 方案（Dynabench, ChatBot Arena, HELM）
4. N-gram/perplexity 基线方法
5. Benchmark 污染 survey（Balloccu et al., 2024）

### 主要优势
1. 问题重要且及时
2. Limitations 诚实呈现
3. 负面结果有社区价值
4. Power surface 分析实用
5. Benchmark regeneration pipeline 方向正确

### 给作者的问题
1. 确认引用错误（Tets→Tutz, Iron-Fenced→Item-Focussed, DVD 引用）
2. Ensemble 权重的 cross-validation 细节和过拟合风险
3. 如果将贡献定位为"实证发现"而非"方法论创新"，如何重组叙事？
4. 13 个 reasoning-RL 模型的完整列表和 family 分布
5. ETS A/B/C 阈值对 LLM 群体是否适用？
6. 为什么选择 DIF 而非 Growing Pains 的框架？

---

**请对以上所有 Must-Fix、Should-Fix、缺失相关工作、优势评价逐条回应 [AGREE] 或 [REBUT]。** 特别关注：
1. 你是否同意 R2 对新颖性的评价（2/5）？你给了 5/6——这是最大分歧点，请详细论证。
2. 引用错误问题你在初审中未提及，你认为这对论文可信度的影响有多大？
3. Ensemble 到底是正面贡献还是负面结果？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-20T21:44:40.520912+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/paper.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "2,6,7,10",
  "dpi": "165"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/paper.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "2,6,7,10",
    "dpi": "165"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-20T21:44:41.074115+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p2.png\", \"width\": 1403, \"height\": 1815, \"size_kb\": 396.5}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p6.png\", \"width\": 1403, \"height\": 1815, \"size_kb\": 325.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p7.png\", \"width\": 1403, \"height\": 1815, \"size_kb\": 312.3}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p10.png\", \"width\": 1403, \"height\": 1815, \"size_kb\": 393.4}], \"total_pages\": 10, \"rendered_pages\": 4, \"dpi\": 165, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-20T21:44:45.644871+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-20T21:44:46.803719+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1158
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-20T21:44:47.007034+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 55 · 2026-05-20T21:44:47.109335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-20T21:44:47.712347+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images/paper_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-20T21:44:48.220775+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1213
}
```

</details>

---


### Tool result

_source line 58 · 2026-05-20T21:44:48.928085+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1818
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-20T21:44:49.335828+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1623
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-20T21:47:37.198552+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 对 R2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 逐条回应\n\n**[REBUT] R2-N1: 引用错误——R2 的指控本身部分不准确**\n\nR2 声称论文使用了 \"Iron-Fenced Trees\" 和 \"Tets & Berger (2016)\"。我以 165 DPI 重新渲染了 page 2 和 page 6 进行核实：\n\n- **方法名：** 论文 §4.4 节标题和正文均写作 **\"Item-Focused Trees (IFT)\"**（page 6），Related Work（page 2）也写作 \"Item-Focused Trees\"。R2 声称的 \"Iron-Fenced Trees\" **在论文中不存在**——这是 R2 自己的误读或记忆偏差。真实文献为 \"Item-Focussed Trees\"（英式拼写），论文的 \"Item-Focused Trees\"（美式拼写）只是拼写变体，不算错误。\n- **作者名：** page 2 的引用拼写看起来可能是 \"Totz\" 而非 \"Tutz\"——如果确实如此，这是一个 typo 级别的错误，需要更正但不构成 \"严重错误\"。\n- **DVD 引用（\"Dunn et al.\"）：** 在我审阅的渲染中无法清晰辨认具体作者名，无法确认或否定此项。如果 R2 可以指出具体页面和行号，将更有助于作者核查。\n\n**结论：** R2 将此标记为 [critical] 过于严厉。其核心指控——\"Iron-Fenced Trees\"——本身是错误的。可能存在的 author name typo 需要修正但不影响技术贡献的可信度。建议作者全面核查参考文献拼写，但这属于 camera-ready 级别的修正，不应作为拒稿依据。\n\n---\n\n**[REBUT] R2-N2: DIF 迁移的新颖性不足——R2 低估了跨学科桥接的难度和完整管线的贡献**\n\nR2 认为将 temporal cohorts 映射为 reference/focal groups 是 \"straightforward\"。我不同意这个判断，理由如下：\n\n1. **概念识别并非平凡。** LLM 社区长期将污染检测视为信息检索问题（n-gram overlap、perplexity、MIA），而非心理测量问题。识别出 \"contamination = DIF\" 这个等式需要对两个领域都有深入理解——这不是套公式。\n2. **工程和实证挑战非平凡。** 对 5,219 × 12,508 矩阵拟合 IRT 本身就有独特挑战——论文发现的架构异质性问题（full-pop RMSEA=0.105 → decoder-only 0.068, Table 5）和分层解决方案是非预期的实证贡献。\n3. **RL 鲁棒性洞见是新的。** \"DIF 在群体层面运作，因此天然对单模型输出平滑具有鲁棒性\" 这个理论论点（§3.2）有独立价值——它解释了为什么 per-model 检测器（ConStat、Min-K%）在 RL 模型上退化而 DIF 不退化（Table 3）。\n4. **完整管线超越了单一方法应用。** 检测 → 多信号集成 → 半合成验证 → bifactor 等值 → 再生 → 退化分析——这是一个完整的技术栈，不是简单的 \"apply DIF to new data\"。\n\n**但我承认 R2 有部分道理：** DIF 方法本身没有技术创新（仍是标准 Mantel-Haenszel + ETS 分类）。如果论文标题或 framing 暗示了 DIF 方法论贡献，那确实有 overclaiming。\n\n**修正后的评分：** 我将 Novelty 从 5/6 下调至 **4/6**。理由：跨学科概念贡献 + 大规模实证发现 + 完整管线 ≥ 4 分门槛，但缺乏 DIF 方法本身的技术创新使其无法达到 5 分。R2 的 2/5 仍然过低——忽略了实证发现和管线贡献的价值。\n\n---\n\n**[REBUT] R2-N3: \"Ensemble 不如单独 DIF\"——R2 选择性引用数据，结论不成立**\n\nR2 声称 \"Table 10 显示 DIF 单独的 TPR 在 δ≥1.4 时已达 0.78，ensemble 未带来一致性提升。\" **这是对 Table 10 的选择性解读。**\n\nTable 10（page 7）完整数据：\n\n| Strategy | TPR (δ≥1.4) | TPR (δ≥0.8) | FPR | Coverage |\n|----------|-------------|-------------|-----|----------|\n| DIF only | 0.78 | 0.51 | 0.04 | 36% |\n| Full ensemble (union) | 0.82 | 0.72 | 0.085 | 73% |\n\n关键对比：\n- **δ≥1.4（大效应）：** ensemble **更好** (0.82 > 0.78)\n- **δ≥0.8（中等效应）：** ensemble **大幅改善** (0.72 vs 0.51, +0.21 TPR)\n- **Coverage：** ensemble **翻倍** (73% vs 36%)\n\nR2 只看了 δ≥1.4 一个维度且忽视了 ensemble 在该维度也更优。Ensemble 的核心价值恰恰在中等效应区间——DIF 单独在 δ<1.0 时 power 急剧下降（Table 4, page 5），而 ensemble 通过 ConStat 信号补充了这一盲区。\n\nFPR 从 0.04 升至 0.085 是合理代价——在 12,508 题上多标记约 560 题（约 4.5%），换取中等效应 TPR 提升 21 个百分点和覆盖率翻倍。\n\n**结论：** Ensemble 是明确的正面贡献。R2 的 N3 结论 factually incorrect。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R2-W1: RL 样本量过小**\n完全同意。我在 R1 审稿中将此列为 W2 [Major]，核心论点一致：N=13 无法支撑核心贡献声明。我补充一点：R2 和我都指出了这个问题，这应该给作者明确信号——此问题不可回避。\n\n**[AGREE] R2-W2: 与 Growing Pains 的区分不清晰**\n这是合理的 related work 关切。Growing Pains（Zhang et al.）也提出了 IRT-based benchmark 评估框架。论文应在 §2 中明确说明：Growing Pains 聚焦 score equivalence 和 benchmark reliability，而本文聚焦 item-level contamination detection via DIF + 再生管线——两者在 IRT 应用层面有重叠但目标和技术路径不同。\n\n**[AGREE] R2-W3: Wang et al. (2026) 无法核实**\n无法核实的引用在 blind review 中确实是红旗。我在 R1 审稿中未专门检查引用真实性（这更属于 R2 的侧重领域），但同意此关切。建议 Director 在最终审稿前用 `verify_references` 工具做系统性引用核查。\n\n**[AGREE] R2-W4: 42% within-family overlap**\n完全同意。我在 R1 审稿中将此列为 W1 [Major] 的一部分——46% overlap 意味着 54% 的全群体 DIF 标记可能由能力漂移而非污染驱动。\n\n**[REBUT] R2-W5: 贡献数量膨胀（5→2-3 条）**\n部分不同意。R2 建议缩减至 2-3 条，但我认为以下 4 条可以独立成立：\n1. **IRT 拟合诊断 + 架构分层**——这是一个有独立价值的实证发现（Table 5-6）\n2. **DIF 检测 + ensemble**——核心检测方法（Tables 3, 10）\n3. **半合成验证 + power surface**——验证框架（Tables 12-14）\n4. **Bifactor 等值 + 再生管线**——remediation 方向（Tables 15-18）\n\nPower surface (R²=0.89) 更适合归入贡献 3 而非单独列出——在这一点上我同意 R2，5 条确实可以压缩为 4 条。\n\n---\n\n### 缺失相关工作逐条回应\n\n**[AGREE] 1. Min-K%++ (Shi et al., 2024):** 论文提到了 Min-K%（Table 3 有对比），但更强的变体 Min-K%++ 应该被讨论。\n\n**[AGREE] 2. IRT in NLP (Lalor et al., 2019; Vania et al., 2021):** 这是最重要的遗漏。这些工作是 IRT 应用于 NLP 评测的先驱，论文声称 \"first large-scale IRT fit diagnostics for LLM populations\"——必须明确与这些先行工作的区别（规模？群体定义？拟合诊断方法？）。\n\n**[REBUT] 3. 动态 Benchmark (Dynabench, ChatBot Arena, HELM):** 这些工作解决的是不同问题——动态评测的目标是 adversarial/adaptive item creation，而非基于 IRT 的污染检测和等值再生。论文的 §2 Related Work 在 \"Benchmark Maintenance\" 部分已提及 LiveBench（类似方向）。要求论文讨论所有动态基准方案会偏离论文的核心聚焦。\n\n**[AGREE] 4. N-gram/perplexity 基线方法:** 论文在 §1 提到 \"n-gram overlap\" 但未在实验中将 n-gram 方法作为基线对比。至少应在 Table 3 中加入一个简单的 n-gram overlap 基线。\n\n**[AGREE] 5. Balloccu et al. (2024) survey:** 作为该领域最近的综述，应该被引用以定位论文在 contamination detection 文献中的位置。\n\n---\n\n### 主要优势回应\n\n**[AGREE] 所有 5 条优势。** R2 对论文优势的评价公允——问题重要性、诚实报告、负面结果的社区价值、power surface 的实用性、regeneration 方向。\n\n---\n\n### Director 要求的三个重点问题\n\n**1. 新颖性评分分歧（R2=2/5 vs R1 原始=5/6）**\n\n修正后我给 **4/6**。核心分歧在于 \"应用 vs 创新\" 的判断标准：\n- R2 立场：DIF 是现有技术，应用到新领域 = 低新颖性。\n- R1 立场：跨学科概念桥接 + 大规模实证 + 完整管线 = 中高新颖性。\n- 调和点：如果论文重新 framing 为 \"实证发现驱动的系统论文\"（empirical systems paper）而非 \"方法论创新论文\"，两个评分可以趋近。论文当前的 framing 确实偏向方法论贡献声明，这在 DIF 本身无创新的情况下略显 overclaiming。\n- **最终判断：** novelty 在 3-4/6 范围内是合理的。R2 的 2/5 和我原始的 5/6 都偏离了公允区间。\n\n**2. 引用错误对论文可信度的影响**\n\n我在 R1 初审中未专门检查引用——这确实是疏漏。但经核实：\n- R2 声称的最严重错误（\"Iron-Fenced Trees\"）**在论文中不存在**——论文写的是 \"Item-Focused Trees\"。这反而削弱了 R2 将此标记为 [critical] 的依据。\n- 可能存在的 author name typo（Totz/Tets → Tutz）确实需要修正，但属于 minor 级别。\n- DVD 引用和 Wang et al. 需要用 `verify_references` 系统核查后才能定论。\n\n**影响评估：** 如果确认存在 1-2 个 author name typo，这属于 carelessness 但不影响技术可信度。如果存在虚假引用（fabricated citation），则严重性显著提升至 [critical]。当前证据不足以判断。\n\n**3. Ensemble 到底是正面贡献还是负面结果？**\n\n**明确是正面贡献。** Table 10 的数据清晰显示 ensemble 在所有关键维度（δ≥1.4 TPR、δ≥0.8 TPR、coverage）均优于 DIF alone。R2 的 N3 结论基于选择性数据引用，factually incorrect。\n\n但有一个 nuance：DVD 单独的负面结果（AUROC 0.56）和 DVD 加入后 ensemble 改善有限（Weighted fusion 中 DVD 权重很低）说明 DVD 信号贡献微弱。论文可以更诚实地表述：**有效的 ensemble 实际上是 DIF + ConStat 双信号系统，DVD 贡献可忽略。**\n\n---\n\n### 总结：R1 修正后的综合评分\n\n在看过 R2 审稿并进行交叉核查后，我对部分评分做出调整：\n\n| 维度 | R1 原始 | R1 修正 | 修正理由 |\n|------|---------|---------|---------|\n| Novelty | 5/6 | 4/6 | R2 关于 DIF 本身无技术创新的观点部分成立 |\n| Soundness | 3/6 | 3/6 | 不变——核心效度问题仍未解决 |\n| Significance | 4/6 | 4/6 | 不变 |\n| Clarity | 4/6 | 4/6 | 不变 |\n| Reproducibility | 3/6 | 3/6 | 不变 |\n| **Overall** | **4/6** | **4/6** | **Weak Accept 维持** |\n\nR2 给 3/6 (Borderline Reject)，我修正后维持 4/6 (Weak Accept)。核心分歧：R2 更重视方法论新颖性，我更重视实证贡献和问题重要性。对于 top venue，我认为一篇概念新颖、实验全面、诚实报告局限性的系统论文值得 conditional accept——前提是作者在 rebuttal 中回应效度验证（κ=0.14 的解释）和 RL 样本量问题。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 对 R2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 逐条回应\n\n**[REBUT] R2-N1: 引用错误——R2 的指控本身部分不准确**\n\nR2 声称论文使用了 \"Iron-Fenced Trees\" 和 \"Tets & Berger (2016)\"。我以 165 DPI 重新渲染了 page 2 和 page 6 进行核实：\n\n- **方法名：** 论文 §4.4 节标题和正文均写作 **\"Item-Focused Trees (IFT)\"**（page 6），Related Work（page 2）也写作 \"Item-Focused Trees\"。R2 声称的 \"Iron-Fenced Trees\" **在论文中不存在**——这是 R2 自己的误读或记忆偏差。真实文献为 \"Item-Focussed Trees\"（英式拼写），论文的 \"Item-Focused Trees\"（美式拼写）只是拼写变体，不算错误。\n- **作者名：** page 2 的引用拼写看起来可能是 \"Totz\" 而非 \"Tutz\"——如果确实如此，这是一个 typo 级别的错误，需要更正但不构成 \"严重错误\"。\n- **DVD 引用（\"Dunn et al.\"）：** 在我审阅的渲染中无法清晰辨认具体作者名，无法确认或否定此项。如果 R2 可以指出具体页面和行号，将更有助于作者核查。\n\n**结论：** R2 将此标记为 [critical] 过于严厉。其核心指控——\"Iron-Fenced Trees\"——本身是错误的。可能存在的 author name typo 需要修正但不影响技术贡献的可信度。建议作者全面核查参考文献拼写，但这属于 camera-ready 级别的修正，不应作为拒稿依据。\n\n---\n\n**[REBUT] R2-N2: DIF 迁移的新颖性不足——R2 低估了跨学科桥接的难度和完整管线的贡献**\n\nR2 认为将 temporal cohorts 映射为 reference/focal groups 是 \"straightforward\"。我不同意这个判断，理由如下：\n\n1. **概念识别并非平凡。** LLM 社区长期将污染检测视为信息检索问题（n-gram overlap、perplexity、MIA），而非心理测量问题。识别出 \"contamination = DIF\" 这个等式需要对两个领域都有深入理解——这不是套公式。\n2. **工程和实证挑战非平凡。** 对 5,219 × 12,508 矩阵拟合 IRT 本身就有独特挑战——论文发现的架构异质性问题（full-pop RMSEA=0.105 → decoder-only 0.068, Table 5）和分层解决方案是非预期的实证贡献。\n3. **RL 鲁棒性洞见是新的。** \"DIF 在群体层面运作，因此天然对单模型输出平滑具有鲁棒性\" 这个理论论点（§3.2）有独立价值——它解释了为什么 per-model 检测器（ConStat、Min-K%）在 RL 模型上退化而 DIF 不退化（Table 3）。\n4. **完整管线超越了单一方法应用。** 检测 → 多信号集成 → 半合成验证 → bifactor 等值 → 再生 → 退化分析——这是一个完整的技术栈，不是简单的 \"apply DIF to new data\"。\n\n**但我承认 R2 有部分道理：** DIF 方法本身没有技术创新（仍是标准 Mantel-Haenszel + ETS 分类）。如果论文标题或 framing 暗示了 DIF 方法论贡献，那确实有 overclaiming。\n\n**修正后的评分：** 我将 Novelty 从 5/6 下调至 **4/6**。理由：跨学科概念贡献 + 大规模实证发现 + 完整管线 ≥ 4 分门槛，但缺乏 DIF 方法本身的技术创新使其无法达到 5 分。R2 的 2/5 仍然过低——忽略了实证发现和管线贡献的价值。\n\n---\n\n**[REBUT] R2-N3: \"Ensemble 不如单独 DIF\"——R2 选择性引用数据，结论不成立**\n\nR2 声称 \"Table 10 显示 DIF 单独的 TPR 在 δ≥1.4 时已达 0.78，ensemble 未带来一致性提升。\" **这是对 Table 10 的选择性解读。**\n\nTable 10（page 7）完整数据：\n\n| Strategy | TPR (δ≥1.4) | TPR (δ≥0.8) | FPR | Coverage |\n|----------|-------------|-------------|-----|----------|\n| DIF only | 0.78 | 0.51 | 0.04 | 36% |\n| Full ensemble (union) | 0.82 | 0.72 | 0.085 | 73% |\n\n关键对比：\n- **δ≥1.4（大效应）：** ensemble **更好** (0.82 > 0.78)\n- **δ≥0.8（中等效应）：** ensemble **大幅改善** (0.72 vs 0.51, +0.21 TPR)\n- **Coverage：** ensemble **翻倍** (73% vs 36%)\n\nR2 只看了 δ≥1.4 一个维度且忽视了 ensemble 在该维度也更优。Ensemble 的核心价值恰恰在中等效应区间——DIF 单独在 δ<1.0 时 power 急剧下降（Table 4, page 5），而 ensemble 通过 ConStat 信号补充了这一盲区。\n\nFPR 从 0.04 升至 0.085 是合理代价——在 12,508 题上多标记约 560 题（约 4.5%），换取中等效应 TPR 提升 21 个百分点和覆盖率翻倍。\n\n**结论：** Ensemble 是明确的正面贡献。R2 的 N3 结论 factually incorrect。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R2-W1: RL 样本量过小**\n完全同意。我在 R1 审稿中将此列为 W2 [Major]，核心论点一致：N=13 无法支撑核心贡献声明。我补充一点：R2 和我都指出了这个问题，这应该给作者明确信号——此问题不可回避。\n\n**[AGREE] R2-W2: 与 Growing Pains 的区分不清晰**\n这是合理的 related work 关切。Growing Pains（Zhang et al.）也提出了 IRT-based benchmark 评估框架。论文应在 §2 中明确说明：Growing Pains 聚焦 score equivalence 和 benchmark reliability，而本文聚焦 item-level contamination detection via DIF + 再生管线——两者在 IRT 应用层面有重叠但目标和技术路径不同。\n\n**[AGREE] R2-W3: Wang et al. (2026) 无法核实**\n无法核实的引用在 blind review 中确实是红旗。我在 R1 审稿中未专门检查引用真实性（这更属于 R2 的侧重领域），但同意此关切。建议 Director 在最终审稿前用 `verify_references` 工具做系统性引用核查。\n\n**[AGREE] R2-W4: 42% within-family overlap**\n完全同意。我在 R1 审稿中将此列为 W1 [Major] 的一部分——46% overlap 意味着 54% 的全群体 DIF 标记可能由能力漂移而非污染驱动。\n\n**[REBUT] R2-W5: 贡献数量膨胀（5→2-3 条）**\n部分不同意。R2 建议缩减至 2-3 条，但我认为以下 4 条可以独立成立：\n1. **IRT 拟合诊断 + 架构分层**——这是一个有独立价值的实证发现（Table 5-6）\n2. **DIF 检测 + ensemble**——核心检测方法（Tables 3, 10）\n3. **半合成验证 + power surface**——验证框架（Tables 12-14）\n4. **Bifactor 等值 + 再生管线**——remediation 方向（Tables 15-18）\n\nPower surface (R²=0.89) 更适合归入贡献 3 而非单独列出——在这一点上我同意 R2，5 条确实可以压缩为 4 条。\n\n---\n\n### 缺失相关工作逐条回应\n\n**[AGREE] 1. Min-K%++ (Shi et al., 2024):** 论文提到了 Min-K%（Table 3 有对比），但更强的变体 Min-K%++ 应该被讨论。\n\n**[AGREE] 2. IRT in NLP (Lalor et al., 2019; Vania et al., 2021):** 这是最重要的遗漏。这些工作是 IRT 应用于 NLP 评测的先驱，论文声称 \"first large-scale IRT fit diagnostics for LLM populations\"——必须明确与这些先行工作的区别（规模？群体定义？拟合诊断方法？）。\n\n**[REBUT] 3. 动态 Benchmark (Dynabench, ChatBot Arena, HELM):** 这些工作解决的是不同问题——动态评测的目标是 adversarial/adaptive item creation，而非基于 IRT 的污染检测和等值再生。论文的 §2 Related Work 在 \"Benchmark Maintenance\" 部分已提及 LiveBench（类似方向）。要求论文讨论所有动态基准方案会偏离论文的核心聚焦。\n\n**[AGREE] 4. N-gram/perplexity 基线方法:** 论文在 §1 提到 \"n-gram overlap\" 但未在实验中将 n-gram 方法作为基线对比。至少应在 Table 3 中加入一个简单的 n-gram overlap 基线。\n\n**[AGREE] 5. Balloccu et al. (2024) survey:** 作为该领域最近的综述，应该被引用以定位论文在 contamination detection 文献中的位置。\n\n---\n\n### 主要优势回应\n\n**[AGREE] 所有 5 条优势。** R2 对论文优势的评价公允——问题重要性、诚实报告、负面结果的社区价值、power surface 的实用性、regeneration 方向。\n\n---\n\n### Director 要求的三个重点问题\n\n**1. 新颖性评分分歧（R2=2/5 vs R1 原始=5/6）**\n\n修正后我给 **4/6**。核心分歧在于 \"应用 vs 创新\" 的判断标准：\n- R2 立场：DIF 是现有技术，应用到新领域 = 低新颖性。\n- R1 立场：跨学科概念桥接 + 大规模实证 + 完整管线 = 中高新颖性。\n- 调和点：如果论文重新 framing 为 \"实证发现驱动的系统论文\"（empirical systems paper）而非 \"方法论创新论文\"，两个评分可以趋近。论文当前的 framing 确实偏向方法论贡献声明，这在 DIF 本身无创新的情况下略显 overclaiming。\n- **最终判断：** novelty 在 3-4/6 范围内是合理的。R2 的 2/5 和我原始的 5/6 都偏离了公允区间。\n\n**2. 引用错误对论文可信度的影响**\n\n我在 R1 初审中未专门检查引用——这确实是疏漏。但经核实：\n- R2 声称的最严重错误（\"Iron-Fenced Trees\"）**在论文中不存在**——论文写的是 \"Item-Focused Trees\"。这反而削弱了 R2 将此标记为 [critical] 的依据。\n- 可能存在的 author name typo（Totz/Tets → Tutz）确实需要修正，但属于 minor 级别。\n- DVD 引用和 Wang et al. 需要用 `verify_references` 系统核查后才能定论。\n\n**影响评估：** 如果确认存在 1-2 个 author name typo，这属于 carelessness 但不影响技术可信度。如果存在虚假引用（fabricated citation），则严重性显著提升至 [critical]。当前证据不足以判断。\n\n**3. Ensemble 到底是正面贡献还是负面结果？**\n\n**明确是正面贡献。** Table 10 的数据清晰显示 ensemble 在所有关键维度（δ≥1.4 TPR、δ≥0.8 TPR、coverage）均优于 DIF alone。R2 的 N3 结论基于选择性数据引用，factually incorrect。\n\n但有一个 nuance：DVD 单独的负面结果（AUROC 0.56）和 DVD 加入后 ensemble 改善有限（Weighted fusion 中 DVD 权重很低）说明 DVD 信号贡献微弱。论文可以更诚实地表述：**有效的 ensemble 实际上是 DIF + ConStat 双信号系统，DVD 贡献可忽略。**\n\n---\n\n### 总结：R1 修正后的综合评分\n\n在看过 R2 审稿并进行交叉核查后，我对部分评分做出调整：\n\n| 维度 | R1 原始 | R1 修正 | 修正理由 |\n|------|---------|---------|---------|\n| Novelty | 5/6 | 4/6 | R2 关于 DIF 本身无技术创新的观点部分成立 |\n| Soundness | 3/6 | 3/6 | 不变——核心效度问题仍未解决 |\n| Significance | 4/6 | 4/6 | 不变 |\n| Clarity | 4/6 | 4/6 | 不变 |\n| Reproducibility | 3/6 | 3/6 | 不变 |\n| **Overall** | **4/6** | **4/6** | **Weak Accept 维持** |\n\nR2 给 3/6 (Borderline Reject)，我修正后维持 4/6 (Weak Accept)。核心分歧：R2 更重视方法论新颖性，我更重视实证贡献和问题重要性。对于 top venue，我认为一篇概念新颖、实验全面、诚实报告局限性的系统论文值得 conditional accept——前提是作者在 rebuttal 中回应效度验证（κ=0.14 的解释）和 RL 样本量问题。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-20T21:47:40.912544+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3713
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-20T21:47:46.445821+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-20T21:47:46.446217+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 64 · 2026-05-20T21:47:57.015941+00:00_

交叉回应已提交给 Director。核心结论：

- **R2-N1（引用错误）**：REBUT——R2 声称的 "Iron-Fenced Trees" 在论文中不存在，论文实际写的是 "Item-Focused Trees"。可能存在 author name typo 但不构成 critical 级别问题。
- **R2-N2（新颖性）**：部分同意，将 Novelty 从 5/6 下调至 4/6，但认为 R2 的 2/5 仍然过低。
- **R2-N3（Ensemble 无效）**：REBUT——Table 10 数据显示 ensemble 在 δ≥0.8 的 TPR（+0.21）和 coverage（×2）上均大幅优于 DIF alone。R2 的结论基于选择性数据引用。
- **Overall 维持 4/6 (Weak Accept)**，与 R2 的 3/6 存在 1 分分歧。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 3

## Round 3

50 recorded events


### User

_source line 65 · 2026-05-21T07:02:03.417477+00:00_

[Round 1 审稿请求]:
## Review Assignment — R1: Methods & Experiments

**Venue:** ICLR 2026 (rating scale: {0, 2, 4, 6, 8, 10})
- 10: Top 5%, seminal
- 8: Top 15%, strong accept
- 6: Marginally above acceptance threshold
- 4: Marginally below acceptance threshold
- 2: Strong reject
- 0: Trivial or wrong

**Your focus:** Methodological soundness, experimental rigor, statistical validity, reproducibility.

**Paper summary:** "Psychometric Characterization of Temporal Item Instability in LLM Benchmarks: A Large-Scale DIF Analysis of MMLU." Applies Mantel-Haenszel DIF analysis to METABENCH response matrix (5,227 models × 12,508 MMLU items). 4 claims: (1) 31.3% MMLU items exhibit large temporal DIF; (2) web-overlap contamination labels are mismatched for item-level validation; (3) semi-synthetic ∆TPR framework with cross-subject matching eliminates FPR inflation; (4) DIF items serve as diagnostic lens, not quality filter (ρ≈0.997 after removal).

**Key data to evaluate:**

### Claim 1 — Temporal DIF (§4.1)
- Table 1: 31.3% B+C flagged items, random-split sanity 0.18%
- Table 2: Cohort sensitivity — temporal 31.3%, ability 2.9%, within-family 61.3%
- Table 3: Architecture stratification — 99.98% decoder-only, Jaccard=1.0 after removing 1 non-decoder model
- IRT fit: RMSEA=0.089, CFI=0.72 — poor 1D IRT fit acknowledged
- Domain decomposition: accuracy improvement explains ≤7.6% of C%

### Claim 2 — Ground Truth Meta-Critique (§4.2)
- Enrichment ratio 0.96≈1.0 against Li et al. labels
- Argument: web-overlap = global property; DIF = differential property — construct mismatch
- Brief section, largely conceptual

### Claim 3 — Semi-Synthetic Framework (§4.3)
- Table 4: Dose-response from p=0.3 to p=1.0, ∆TPR=+0.508 at p=0.5, ∆FPR=0.000
- Table 5: Cross-subject vs within-subject matching — FPR inflation +0.186 eliminated
- Table 6: GSM8K replication (1,319 items × 6,702 models), ∆TPR=+0.818

### Claim 4 — DIF as Diagnostic Lens (§4.4)
- ρ≈0.997 after removing 31.3% DIF items
- Table 7: z-score comparison — DIF z=-9.5 vs accuracy-gap z=-157
- Table 8: GSM1K correlation r=-0.478, N=33, CI wide, Spearman upper bound -0.031

### Supplementary Analyses (§5)
- §5.1 RL robustness: N=13 reasoning-RL, TOST inconclusive (p=0.14)
- §5.2 ConStat: Jaccard=0.08 with DIF, 15 models
- §5.3 DVD: Jaccard=0.05, primarily verbatim detection
- §5.4 Ensemble: AUROC=0.62, weight stability=0.43, circularity with Claim 2
- §5.5 Bifactor IRT: CFI=0.81, TLI=0.78, general factor 34%, equating ρ=0.94
- §5.6 Item generation: ρ=0.58 vs target 0.75 — negative result
- §5.7 Cumulative Bayesian DIF: simulation-only, power 0.41→0.74 over 4 admins
- §5.8 Graceful degradation: validity floor ~35%
- §5.9 Item-Focused Trees: 78% concordance with MH, Jaccard=0.68

### Key methodological questions to address:
1. Is the 1D IRT misspecification a fatal flaw or adequately addressed? (CFI=0.72, 98% models |Lz|>2, bifactor pilot shows C% drops only to ~28-29%)
2. Is the semi-synthetic injection mechanism (incorrect→correct flip) a valid contamination model?
3. Are the statistical tests properly applied? (MH χ², ETS dual criteria, permutation tests, BCa bootstrap)
4. Is N=33 for GSM1K correlation appropriately caveated?
5. How well does the paper handle multiple comparisons across 12,508 items?
6. Is cross-subject matching a genuine methodological contribution or an obvious choice?

### Experiment coverage assessment:
The review_context lists these imagined experiments (check coverage):
- plan_001 (MMLU DIF): ✓ fully covered in §4.1
- plan_002 (RL robustness): ✓ covered in §5.1, appropriately caveated
- plan_003a (ConStat): ✓ covered in §5.2
- plan_003b (DVD): ✓ covered in §5.3
- plan_003c (Ensemble): ✓ covered in §5.4, reported as negative
- plan_004 (GSM8K): ✓ partially covered (Steps 1-2 in §4.3.2, Step 3 in §4.4.3)
- plan_005 (Bifactor IRT): ✓ covered in §5.5
- plan_006 (Item generation): ✓ covered as negative result in §5.6
- plan_007 (Bayesian DIF): ✓ covered in §5.7
- plan_008 (Graceful degradation): ✓ covered in §5.8
- plan_009 (IFT): ✓ covered in §5.9
- plan_010 (Architecture stratification): ✓ covered in §4.1.3
- plan_011 (Semi-synthetic): ✓ covered in §4.3

**Deliverable:** A structured review with:
1. Summary (2-3 sentences)
2. Strengths (bulleted, with specific table/figure references)
3. Weaknesses (bulleted, with severity: Major/Minor)
4. Questions for authors
5. Preliminary scores: Soundness (1-4), Presentation (1-4), Contribution (1-4), Overall (0/2/4/6/8/10), Confidence (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-21T07:02:29.384393+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/main.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-21T07:02:29.435088+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-21T07:02:34.458031+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-5",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-5",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-21T07:02:35.162495+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 363.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 385.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 442.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 433.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 339.0}], \"total_pages\": 17, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-21T07:02:39.429041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-21T07:02:40.386471+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-21T07:02:40.386991+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-21T07:02:40.890968+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-21T07:02:40.891489+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 75 · 2026-05-21T07:02:41.345904+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 76 · 2026-05-21T07:02:41.751277+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool call

_source line 77 · 2026-05-21T07:02:41.852897+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 78 · 2026-05-21T07:02:42.356638+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-21T07:02:42.458581+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-21T07:03:16.104717+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "6-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "6-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-21T07:03:16.658518+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 359.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 369.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 212.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 394.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 324.4}], \"total_pages\": 17, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-21T07:03:20.374756+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-21T07:03:20.829443+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-21T07:03:20.832082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-21T07:03:21.789690+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-21T07:03:21.790156+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-21T07:03:22.243258+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-21T07:03:22.243778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 89 · 2026-05-21T07:03:22.545233+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-21T07:03:22.648557+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-21T07:03:22.951818+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 406
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-21T07:04:09.267473+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "11-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "11-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-21T07:04:09.771950+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p11.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 388.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p12.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 409.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p13.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 405.4}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p14.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 350.9}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p15.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 277.6}], \"total_pages\": 17, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-21T07:04:20.169376+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 95 · 2026-05-21T07:04:20.724149+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 96 · 2026-05-21T07:04:21.583940+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1414
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-21T07:04:21.592060+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 867
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-21T07:04:21.592529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 99 · 2026-05-21T07:04:22.146277+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 100 · 2026-05-21T07:04:22.557605+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 965
}
```

</details>

---


### Tool call

_source line 101 · 2026-05-21T07:04:22.558120+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 102 · 2026-05-21T07:04:22.813186+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 666
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-21T07:04:23.116345+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 558
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-21T07:04:29.595119+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "16-17",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "16-17",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-21T07:04:29.898980+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p16.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 167.4}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p17.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 193.4}], \"total_pages\": 17, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-21T07:04:33.561199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-21T07:04:33.964775+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-21T07:04:33.965411+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-21T07:04:34.269491+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 304
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-21T07:08:40.054784+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 审稿意见（修订版论文）：Methods & Experiments\n\n**Paper:** \"Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations\"\n\n**Venue:** ICLR 2026, rating scale {0, 2, 4, 6, 8, 10}\n\n---\n\n### 1. Summary\n\n本文对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）应用 Mantel-Haenszel DIF 分析，发现 31.3% 的 MMLU 题目在 pre-2023 与 post-2024 模型群体间表现出显著的差异项目功能（ETS C 类）。论文通过 5 种 cohort 设计（temporal/ability-quintile/within-family/within-subject/random-split）排除混淆变量，提出 cross-subject matching 的半合成验证框架（ΔTPR=+0.508, ΔFPR=0.000），在 GSM8K 上复现了发现（ΔTPR=+0.818），并论证 DIF 应作为诊断工具而非质量过滤器（移除后 ρ≈0.997）。相比前一版本，论文在 framing、方法论严谨性和诚实度上有显著改进。\n\n---\n\n### 2. Strengths\n\n**S1. Cohort 设计是一流的实验控制。** Table 1 的 5 种 cohort 设计是本文最强的方法论贡献：temporal（31.3%）vs ability-quintile（2.9%）vs random-split（0.18%）的对比极其有力。Ability-quintile 仅 2.9% 证明纯能力差异不足以解释 temporal DIF；random-split 0.18% 确认信号非随机噪音。这是教科书级别的控制变量设计。（Table 1, §4.2, p.7）\n\n**S2. Cross-subject matching 是真正的方法论贡献。** Within-subject matching 导致 FPR 膨胀 +0.196（因为 matching variable 包含了被检测的变量，违反条件独立性假设），而 cross-subject matching 将 ΔFPR 降至 0.000。Figure 4（p.16）展示了这个效果在所有 domain 上的一致性。这不是 \"obvious\" 的——很多 naive DIF 实现会落入 within-subject matching 陷阱。这个见解对任何在 multi-domain benchmark 上应用 DIF 的工作都有价值。（§3.4, §4.5, Figure 2, Figure 4）\n\n**S3. 从 \"contamination detection\" 到 \"temporal item instability\" 的 reframing 是认识论上的重要进步。** 前一版本声称 DIF 检测污染，但无法证明。本版本精确地将 claim 限定为 \"items behave differently across generations\"——这是 MH DIF 直接测量的量。论文在 §4.3 中明确论证 web-overlap labels 与 DIF flags 几乎不重叠（enrichment ratio 0.96≈1.0），是 construct mismatch 而非检测失败。这种谨慎的 framing 消除了前一版本最大的效度疑虑。\n\n**S4. Figure 1 概念图和 Figure 2 dose-response 图质量极高。** Figure 1 用 ICC 直观展示了 global vs differential contamination 的区别——这是论文的核心概念贡献，一张图讲清楚了。Figure 2 的半合成 dose-response 曲线（ΔTPR 单调递增，ΔFPR 平坦于 0）是最具说服力的验证证据。\n\n**S5. 结构分析（§4.4）系统排除了混淆因素。** 三种独立方法（matched-ability quintiles、IRT θ-conditioning、within-subject DIF）都未能将 temporal FPR 降至 31% 以下（Table 2, p.15: θ-conditioning FPR=0.312, within-subject C%=30.15）。这些 converging 分析强化了 \"31% 信号是 robust 的\" 结论。Yen's Q3 诊断（11.3% 超标对）也是主动检测局部依赖的良好做法。\n\n**S6. 负面结果诚实报告。** 补充分析中的 ensemble AUROC=0.62、item generation ρ=0.58（vs 目标 0.75）、TOST RL robustness p=0.14（inconclusive）、ConStat Jaccard=0.08 均如实呈现，不做包装。相比前一版本将 ensemble AUROC 0.72 和 regeneration ρ=0.91 作为核心贡献，这是实质性的改进。\n\n**S7. GSM8K 复现增强了泛化性。** Table 3（p.16）的跨 benchmark 对比（MMLU vs GSM8K）展示了 DIF 方法在不同 benchmark 上的一致性——MMLU sanity 0.18% vs GSM8K 0.3%，semi-synthetic ΔTPR 均显著。\n\n**S8. Related work 覆盖全面。** 前一版本缺失的 Lalor et al.（2019）、Vania et al.（2021）、Balloccu et al.（2024）survey、Growing Pains 均已涵盖（§2, pp.3-4）。与 Growing Pains 的区别论述清晰（FPC anchoring assumes item stability，而 DIF 检测哪些 items violate this assumption——互补关系）。\n\n---\n\n### 3. Weaknesses\n\n**W1 [Major] 31.3% 的发现本质上是描述性的——论文未解决 \"why\"。**\n- **位置：** §4.2 (p.7), §5.1 (p.9), Title\n- **问题：** 论文精确地证明了 31.3% 的 MMLU items 在 temporal cohort 间存在 DIF，但没有回答这是由什么引起的：数据污染？训练数据分布迁移？模型架构演变？Benchmark 设计本身的缺陷？\n  - Ability-quintile（2.9%）排除了纯能力差异，但未排除其他混淆\n  - Within-family Llama 2 vs 3（61.3%）暗示可能是特定家族的训练数据变化，但未深入分析\n  - 域分解分析显示 accuracy improvement 仅解释 ≤7.6% 的 C%——好的，但还有 ~92% 未解释\n- **为什么影响评分：** 对于 ICLR 的 contribution 标准，描述性发现需要足够 surprising 或 actionable 才能达到门槛。\"31% 的 items 不稳定\" 是 informative 的，但如果不知道原因，practitioners 不知道该怎么做（移除这些 items？重新校准？重建 benchmark？）。ρ≈0.997 的发现又进一步削弱了 urgency——如果移除不影响排名，为什么要关心？\n- **建议：** (1) 对 DIF-flagged items 进行 case study 分析——随机抽取 20 个 C-flagged items，人工检查它们是否有已知 leakage evidence（如出现在 Common Crawl 中的频率变化）；(2) 利用 within-family 分析（Llama 2 vs 3 的 61.3%）与 known training data composition 做关联分析。\n\n**W2 [Major] Within-family Llama 2 vs 3 的 61.3% 令人困惑且分析不足。**\n- **位置：** Table 1 (p.7)\n- **问题：** 61.3% 远高于 temporal（31.3%），这是 Table 1 中最高的 DIF 率。但论文仅用一句话解释（\"within a single model family, generational changes alone produce...\"）。这个发现有多种解释：\n  - (a) Meta 确实在 Llama 3 训练中使用了 MMLU 数据（已知可能性高）\n  - (b) Llama 2→3 的能力跳跃太大，MH matching 失效（score range 不重叠导致 conditioning 不充分）\n  - (c) N=311+300 的 within-family 样本有选择偏差\n  如果是 (a)，这是本文最强的实证证据——一个 known-likely-contaminated family 显示极高 DIF。如果是 (b)，这是方法论的 limitation。论文不区分这些可能性。\n- **建议：** (1) 报告 Llama 2 和 Llama 3 的 score 分布重叠程度——如果 common-score range 窄，MH 的 conditioning 可能不充分；(2) 尝试其他 within-family 对比（如 Phi-2 vs Phi-3, Qwen 1 vs 2）看是否 consistent。\n\n**W3 [Major] GSM1K correlation 太弱，不应支撑 Claim 4。**\n- **位置：** Table 8/§4.7 (Director summary), Figure 3 (p.10)\n- **问题：** r=-0.478, N=33, Spearman CI upper bound = -0.031。CI 几乎包含 0，意味着真实效应可能为零。这是 Claim 4（\"DIF as diagnostic lens\"）的关键外部验证，但证据过弱。\n- 论文在文本中确实提到了 CI，但 claim 的 framing（§5.3 \"DIF as Diagnostic Lens\"）暗示了比数据支持的更强的结论。\n- **建议：** (1) 明确声明 \"GSM1K 结果是 suggestive 但 inconclusive——N=33 不足以得出确定性结论\"；(2) 不要将 GSM1K 作为 Claim 4 的主要支撑，改为 supplementary evidence。\n\n**W4 [Minor] IRT 拟合不良（RMSEA=0.089, CFI=0.72）的影响被论述清楚但可进一步量化。**\n- **位置：** §4.1 (p.7), Appendix A (p.14)\n- **问题：** 论文正确指出 MH DIF 不要求 IRT 拟合——这是准确的。但 MH 的 matching variable（total score）假设总分是能力的合理代理，而 CFI=0.72 表明单因子模型解释力差。论文通过 bifactor pilot（C% 从 31.3% 仅降至 28-29%）和 θ-conditioning（FPR=0.312）部分回应了这个问题。\n- 但 Yen's Q3 显示 11.3% 的 item pairs 有 local dependence——虽然 \"mild\"，但 on 12,508 items 这意味着 ~880 万 item pairs 中 ~99 万对有 LD。论文未量化这对 MH 统计量的具体影响。\n- **建议：** 对 LD 最高的 item pairs 做敏感性分析——移除 Q3 最高的 5% items 后 C% 是否显著变化。\n\n**W5 [Minor] ΔFPR=0.000 的 cross-subject matching 结果过于完美。**\n- **位置：** §4.5, Figure 2 (p.8)\n- **问题：** 在真实数据中，完美的 ΔFPR=0.000 是不寻常的。这可能意味着：(a) cross-subject matching 确实完美消除了 false positives——最佳解释；(b) 半合成注入力度不够，真正的 FPR 信号被 noise 淹没；(c) 报告了 point estimate 但未给 CI。\n- **建议：** 报告 ΔFPR 的 bootstrap CI——即使 point estimate 是 0.000，CI 上界应非零。\n\n**W6 [Minor] 补充分析过多且大部分为负面结果——可能稀释论文焦点。**\n- **位置：** §5.1-5.9 (补充材料)\n- **问题：** Director summary 列出了 9 个补充分析（RL robustness, ConStat, DVD, ensemble, bifactor, item generation, Bayesian DIF, graceful degradation, IFT），其中 6 个是负面/inconclusive 结果。虽然诚实报告负面结果值得肯定，但过多的 supplementary analyses 可能给 reviewer 的印象是 \"tried many things, most didn't work\"。\n- **建议：** 精选最有信息量的 3-4 个补充分析放入正文（建议：RL robustness 因为 timeliness、IFT 因为方法论互补、bifactor 因为 dimensionality concern），其余移至 appendix 或完全删除。\n\n**W7 [Minor] semi-synthetic injection 的 incorrect→correct flip 是否是有效的污染模型？**\n- **位置：** §3.4 (p.6)\n- **问题：** 真实的 benchmark contamination 不一定表现为 \"之前错现在对\"——也可能是 \"之前就对，但通过不同的推理路径\" 或 \"部分正确变为完全正确\"。incorrect→correct flip 是一个简化模型。\n- 但这个简化模型有合理的优势：(a) 它直接模拟了 DIF 的定义（相同能力下正确率差异）；(b) 它是可控的（exploitation rate p 明确定义）；(c) dose-response 曲线的单调性支持其作为 reasonable proxy。\n- **建议：** 讨论这个简化模型的 boundary conditions——什么情况下 flip model 会高估/低估真实 DIF？\n\n---\n\n### 4. Questions for Authors\n\n**Q1.** Within-family Llama 2 vs 3 的 61.3% DIF 是否与 Meta 已知的训练数据 composition 一致？能否报告 Llama 2 和 Llama 3 在 MMLU 上的 overall accuracy distribution 重叠程度？如果 score range 不重叠，MH conditioning 的有效性就存疑。\n\n**Q2.** 31.3% 的 DIF-flagged items 是否集中在特定的 difficulty range？如果低难度（大多数模型都做对）或高难度（大多数模型都做错）的 items 被不成比例地标记，这可能是 floor/ceiling effect 的 artifact 而非真正的 DIF。\n\n**Q3.** ρ≈0.997 说明 DIF items 对整体排名影响微弱。那么 DIF 的 practical value 是什么？如果目标是 benchmark maintenance，移除 31% 的 items（近 4,000 题）后排名几乎不变，这是否意味着这些 items 本身就是 redundant 的（而非 \"instable\" 的）？\n\n**Q4.** Cross-subject matching 的 ΔFPR=0.000 是基于多少次 random seed/injection 的平均值？如果只有 1-3 次，请增加重复次数。\n\n**Q5.** 补充分析中 ensemble AUROC=0.62——这比前一版本的 0.72 低很多。是因为数据/方法变化还是修正了之前的 bug？\n\n**Q6.** Yen's Q3 显示 11.3% item pairs 超过 LD threshold。能否识别 LD 最高的 subject domains 并检查它们是否也是 DIF 率最高的 domains？如果相关，LD 可能是一个混淆因素。\n\n---\n\n### 5. Preliminary Scores\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| **Soundness** | **3/4** | MH DIF 方法应用正确，cohort 设计优秀，cross-subject matching 有方法论价值。IRT 拟合差但 MH 不依赖 IRT 的论点成立。扣分点：GSM1K 太弱支撑 Claim 4，within-family 61.3% 未充分分析。 |\n| **Presentation** | **3/4** | 清晰的写作，优秀的 Figure 1 和 Figure 2，全面的 appendix。扣分点：补充分析过多可能稀释焦点；Figure 5 的 ρ=0.996 vs 正文 ρ=0.997 不一致。 |\n| **Contribution** | **2/4** | 31.3% 是描述性发现——informative 但非 actionable。Cross-subject matching 是实质贡献但范围窄。负面结果虽然诚实但限制了实际影响。\"Diagnostic lens\" framing 降低了 urgency。 |\n| **Overall** | **6** | Marginally above acceptance threshold。方法论扎实，实验设计优秀，但核心发现偏描述性，practical impact 有限。reframing 的诚实度和 cross-subject matching 的方法论贡献使其 marginally above。 |\n| **Confidence** | **4/5** | 熟悉 MH DIF 方法论和 IRT 框架，对实验设计评估有较高把握。对 METABENCH 数据集的 specifics 了解有限。 |\n\n---\n\n### 6. 与前一版本的对比\n\n| 方面 | 前一版本 | 修订版 | 评价 |\n|------|---------|--------|------|\n| Framing | 污染检测 | 时间不稳定性 | ✓ 大幅改善 |\n| Claims | 5 条，部分 overclaiming | 4 条，审慎 | ✓ 改善 |\n| Related work | 缺 Lalor/Vania/Balloccu | 全面覆盖 | ✓ 改善 |\n| 核心检测性能 | Ensemble AUROC 0.72 | DIF standalone, ensemble 0.62 (supplementary) | → 更诚实但 impact 降低 |\n| 验证 | 半合成 + 外部 κ=0.14 | Cross-subject matching + dose-response + GSM8K replication | ✓ 大幅改善 |\n| RL robustness | N=13, 作为核心贡献 | N=13, TOST inconclusive, 放入补充 | ✓ 诚实 |\n| Item generation | ρ=0.91 (regeneration) | ρ=0.58 (negative result) | → 更诚实但失去了这条贡献线 |\n\n**总体判断：** 修订版在方法论严谨性上有实质性进步，但 impact 的上限也随之降低。前一版本的问题是 overclaiming（声称做到了但证据不足），修订版的问题是 under-impact（做到的东西不够有 actionable value）。从 Methods & Experiments 角度，我偏好修订版——宁可诚实地报告描述性发现，也不要用弱证据支撑强声明。\n\n分数从前一版本的 Weak Accept (4/6 ≈ ICLR 6-7) 维持在 Overall 6 (marginally above acceptance)。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 审稿意见（修订版论文）：Methods & Experiments\n\n**Paper:** \"Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations\"\n\n**Venue:** ICLR 2026, rating scale {0, 2, 4, 6, 8, 10}\n\n---\n\n### 1. Summary\n\n本文对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）应用 Mantel-Haenszel DIF 分析，发现 31.3% 的 MMLU 题目在 pre-2023 与 post-2024 模型群体间表现出显著的差异项目功能（ETS C 类）。论文通过 5 种 cohort 设计（temporal/ability-quintile/within-family/within-subject/random-split）排除混淆变量，提出 cross-subject matching 的半合成验证框架（ΔTPR=+0.508, ΔFPR=0.000），在 GSM8K 上复现了发现（ΔTPR=+0.818），并论证 DIF 应作为诊断工具而非质量过滤器（移除后 ρ≈0.997）。相比前一版本，论文在 framing、方法论严谨性和诚实度上有显著改进。\n\n---\n\n### 2. Strengths\n\n**S1. Cohort 设计是一流的实验控制。** Table 1 的 5 种 cohort 设计是本文最强的方法论贡献：temporal（31.3%）vs ability-quintile（2.9%）vs random-split（0.18%）的对比极其有力。Ability-quintile 仅 2.9% 证明纯能力差异不足以解释 temporal DIF；random-split 0.18% 确认信号非随机噪音。这是教科书级别的控制变量设计。（Table 1, §4.2, p.7）\n\n**S2. Cross-subject matching 是真正的方法论贡献。** Within-subject matching 导致 FPR 膨胀 +0.196（因为 matching variable 包含了被检测的变量，违反条件独立性假设），而 cross-subject matching 将 ΔFPR 降至 0.000。Figure 4（p.16）展示了这个效果在所有 domain 上的一致性。这不是 \"obvious\" 的——很多 naive DIF 实现会落入 within-subject matching 陷阱。这个见解对任何在 multi-domain benchmark 上应用 DIF 的工作都有价值。（§3.4, §4.5, Figure 2, Figure 4）\n\n**S3. 从 \"contamination detection\" 到 \"temporal item instability\" 的 reframing 是认识论上的重要进步。** 前一版本声称 DIF 检测污染，但无法证明。本版本精确地将 claim 限定为 \"items behave differently across generations\"——这是 MH DIF 直接测量的量。论文在 §4.3 中明确论证 web-overlap labels 与 DIF flags 几乎不重叠（enrichment ratio 0.96≈1.0），是 construct mismatch 而非检测失败。这种谨慎的 framing 消除了前一版本最大的效度疑虑。\n\n**S4. Figure 1 概念图和 Figure 2 dose-response 图质量极高。** Figure 1 用 ICC 直观展示了 global vs differential contamination 的区别——这是论文的核心概念贡献，一张图讲清楚了。Figure 2 的半合成 dose-response 曲线（ΔTPR 单调递增，ΔFPR 平坦于 0）是最具说服力的验证证据。\n\n**S5. 结构分析（§4.4）系统排除了混淆因素。** 三种独立方法（matched-ability quintiles、IRT θ-conditioning、within-subject DIF）都未能将 temporal FPR 降至 31% 以下（Table 2, p.15: θ-conditioning FPR=0.312, within-subject C%=30.15）。这些 converging 分析强化了 \"31% 信号是 robust 的\" 结论。Yen's Q3 诊断（11.3% 超标对）也是主动检测局部依赖的良好做法。\n\n**S6. 负面结果诚实报告。** 补充分析中的 ensemble AUROC=0.62、item generation ρ=0.58（vs 目标 0.75）、TOST RL robustness p=0.14（inconclusive）、ConStat Jaccard=0.08 均如实呈现，不做包装。相比前一版本将 ensemble AUROC 0.72 和 regeneration ρ=0.91 作为核心贡献，这是实质性的改进。\n\n**S7. GSM8K 复现增强了泛化性。** Table 3（p.16）的跨 benchmark 对比（MMLU vs GSM8K）展示了 DIF 方法在不同 benchmark 上的一致性——MMLU sanity 0.18% vs GSM8K 0.3%，semi-synthetic ΔTPR 均显著。\n\n**S8. Related work 覆盖全面。** 前一版本缺失的 Lalor et al.（2019）、Vania et al.（2021）、Balloccu et al.（2024）survey、Growing Pains 均已涵盖（§2, pp.3-4）。与 Growing Pains 的区别论述清晰（FPC anchoring assumes item stability，而 DIF 检测哪些 items violate this assumption——互补关系）。\n\n---\n\n### 3. Weaknesses\n\n**W1 [Major] 31.3% 的发现本质上是描述性的——论文未解决 \"why\"。**\n- **位置：** §4.2 (p.7), §5.1 (p.9), Title\n- **问题：** 论文精确地证明了 31.3% 的 MMLU items 在 temporal cohort 间存在 DIF，但没有回答这是由什么引起的：数据污染？训练数据分布迁移？模型架构演变？Benchmark 设计本身的缺陷？\n  - Ability-quintile（2.9%）排除了纯能力差异，但未排除其他混淆\n  - Within-family Llama 2 vs 3（61.3%）暗示可能是特定家族的训练数据变化，但未深入分析\n  - 域分解分析显示 accuracy improvement 仅解释 ≤7.6% 的 C%——好的，但还有 ~92% 未解释\n- **为什么影响评分：** 对于 ICLR 的 contribution 标准，描述性发现需要足够 surprising 或 actionable 才能达到门槛。\"31% 的 items 不稳定\" 是 informative 的，但如果不知道原因，practitioners 不知道该怎么做（移除这些 items？重新校准？重建 benchmark？）。ρ≈0.997 的发现又进一步削弱了 urgency——如果移除不影响排名，为什么要关心？\n- **建议：** (1) 对 DIF-flagged items 进行 case study 分析——随机抽取 20 个 C-flagged items，人工检查它们是否有已知 leakage evidence（如出现在 Common Crawl 中的频率变化）；(2) 利用 within-family 分析（Llama 2 vs 3 的 61.3%）与 known training data composition 做关联分析。\n\n**W2 [Major] Within-family Llama 2 vs 3 的 61.3% 令人困惑且分析不足。**\n- **位置：** Table 1 (p.7)\n- **问题：** 61.3% 远高于 temporal（31.3%），这是 Table 1 中最高的 DIF 率。但论文仅用一句话解释（\"within a single model family, generational changes alone produce...\"）。这个发现有多种解释：\n  - (a) Meta 确实在 Llama 3 训练中使用了 MMLU 数据（已知可能性高）\n  - (b) Llama 2→3 的能力跳跃太大，MH matching 失效（score range 不重叠导致 conditioning 不充分）\n  - (c) N=311+300 的 within-family 样本有选择偏差\n  如果是 (a)，这是本文最强的实证证据——一个 known-likely-contaminated family 显示极高 DIF。如果是 (b)，这是方法论的 limitation。论文不区分这些可能性。\n- **建议：** (1) 报告 Llama 2 和 Llama 3 的 score 分布重叠程度——如果 common-score range 窄，MH 的 conditioning 可能不充分；(2) 尝试其他 within-family 对比（如 Phi-2 vs Phi-3, Qwen 1 vs 2）看是否 consistent。\n\n**W3 [Major] GSM1K correlation 太弱，不应支撑 Claim 4。**\n- **位置：** Table 8/§4.7 (Director summary), Figure 3 (p.10)\n- **问题：** r=-0.478, N=33, Spearman CI upper bound = -0.031。CI 几乎包含 0，意味着真实效应可能为零。这是 Claim 4（\"DIF as diagnostic lens\"）的关键外部验证，但证据过弱。\n- 论文在文本中确实提到了 CI，但 claim 的 framing（§5.3 \"DIF as Diagnostic Lens\"）暗示了比数据支持的更强的结论。\n- **建议：** (1) 明确声明 \"GSM1K 结果是 suggestive 但 inconclusive——N=33 不足以得出确定性结论\"；(2) 不要将 GSM1K 作为 Claim 4 的主要支撑，改为 supplementary evidence。\n\n**W4 [Minor] IRT 拟合不良（RMSEA=0.089, CFI=0.72）的影响被论述清楚但可进一步量化。**\n- **位置：** §4.1 (p.7), Appendix A (p.14)\n- **问题：** 论文正确指出 MH DIF 不要求 IRT 拟合——这是准确的。但 MH 的 matching variable（total score）假设总分是能力的合理代理，而 CFI=0.72 表明单因子模型解释力差。论文通过 bifactor pilot（C% 从 31.3% 仅降至 28-29%）和 θ-conditioning（FPR=0.312）部分回应了这个问题。\n- 但 Yen's Q3 显示 11.3% 的 item pairs 有 local dependence——虽然 \"mild\"，但 on 12,508 items 这意味着 ~880 万 item pairs 中 ~99 万对有 LD。论文未量化这对 MH 统计量的具体影响。\n- **建议：** 对 LD 最高的 item pairs 做敏感性分析——移除 Q3 最高的 5% items 后 C% 是否显著变化。\n\n**W5 [Minor] ΔFPR=0.000 的 cross-subject matching 结果过于完美。**\n- **位置：** §4.5, Figure 2 (p.8)\n- **问题：** 在真实数据中，完美的 ΔFPR=0.000 是不寻常的。这可能意味着：(a) cross-subject matching 确实完美消除了 false positives——最佳解释；(b) 半合成注入力度不够，真正的 FPR 信号被 noise 淹没；(c) 报告了 point estimate 但未给 CI。\n- **建议：** 报告 ΔFPR 的 bootstrap CI——即使 point estimate 是 0.000，CI 上界应非零。\n\n**W6 [Minor] 补充分析过多且大部分为负面结果——可能稀释论文焦点。**\n- **位置：** §5.1-5.9 (补充材料)\n- **问题：** Director summary 列出了 9 个补充分析（RL robustness, ConStat, DVD, ensemble, bifactor, item generation, Bayesian DIF, graceful degradation, IFT），其中 6 个是负面/inconclusive 结果。虽然诚实报告负面结果值得肯定，但过多的 supplementary analyses 可能给 reviewer 的印象是 \"tried many things, most didn't work\"。\n- **建议：** 精选最有信息量的 3-4 个补充分析放入正文（建议：RL robustness 因为 timeliness、IFT 因为方法论互补、bifactor 因为 dimensionality concern），其余移至 appendix 或完全删除。\n\n**W7 [Minor] semi-synthetic injection 的 incorrect→correct flip 是否是有效的污染模型？**\n- **位置：** §3.4 (p.6)\n- **问题：** 真实的 benchmark contamination 不一定表现为 \"之前错现在对\"——也可能是 \"之前就对，但通过不同的推理路径\" 或 \"部分正确变为完全正确\"。incorrect→correct flip 是一个简化模型。\n- 但这个简化模型有合理的优势：(a) 它直接模拟了 DIF 的定义（相同能力下正确率差异）；(b) 它是可控的（exploitation rate p 明确定义）；(c) dose-response 曲线的单调性支持其作为 reasonable proxy。\n- **建议：** 讨论这个简化模型的 boundary conditions——什么情况下 flip model 会高估/低估真实 DIF？\n\n---\n\n### 4. Questions for Authors\n\n**Q1.** Within-family Llama 2 vs 3 的 61.3% DIF 是否与 Meta 已知的训练数据 composition 一致？能否报告 Llama 2 和 Llama 3 在 MMLU 上的 overall accuracy distribution 重叠程度？如果 score range 不重叠，MH conditioning 的有效性就存疑。\n\n**Q2.** 31.3% 的 DIF-flagged items 是否集中在特定的 difficulty range？如果低难度（大多数模型都做对）或高难度（大多数模型都做错）的 items 被不成比例地标记，这可能是 floor/ceiling effect 的 artifact 而非真正的 DIF。\n\n**Q3.** ρ≈0.997 说明 DIF items 对整体排名影响微弱。那么 DIF 的 practical value 是什么？如果目标是 benchmark maintenance，移除 31% 的 items（近 4,000 题）后排名几乎不变，这是否意味着这些 items 本身就是 redundant 的（而非 \"instable\" 的）？\n\n**Q4.** Cross-subject matching 的 ΔFPR=0.000 是基于多少次 random seed/injection 的平均值？如果只有 1-3 次，请增加重复次数。\n\n**Q5.** 补充分析中 ensemble AUROC=0.62——这比前一版本的 0.72 低很多。是因为数据/方法变化还是修正了之前的 bug？\n\n**Q6.** Yen's Q3 显示 11.3% item pairs 超过 LD threshold。能否识别 LD 最高的 subject domains 并检查它们是否也是 DIF 率最高的 domains？如果相关，LD 可能是一个混淆因素。\n\n---\n\n### 5. Preliminary Scores\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| **Soundness** | **3/4** | MH DIF 方法应用正确，cohort 设计优秀，cross-subject matching 有方法论价值。IRT 拟合差但 MH 不依赖 IRT 的论点成立。扣分点：GSM1K 太弱支撑 Claim 4，within-family 61.3% 未充分分析。 |\n| **Presentation** | **3/4** | 清晰的写作，优秀的 Figure 1 和 Figure 2，全面的 appendix。扣分点：补充分析过多可能稀释焦点；Figure 5 的 ρ=0.996 vs 正文 ρ=0.997 不一致。 |\n| **Contribution** | **2/4** | 31.3% 是描述性发现——informative 但非 actionable。Cross-subject matching 是实质贡献但范围窄。负面结果虽然诚实但限制了实际影响。\"Diagnostic lens\" framing 降低了 urgency。 |\n| **Overall** | **6** | Marginally above acceptance threshold。方法论扎实，实验设计优秀，但核心发现偏描述性，practical impact 有限。reframing 的诚实度和 cross-subject matching 的方法论贡献使其 marginally above。 |\n| **Confidence** | **4/5** | 熟悉 MH DIF 方法论和 IRT 框架，对实验设计评估有较高把握。对 METABENCH 数据集的 specifics 了解有限。 |\n\n---\n\n### 6. 与前一版本的对比\n\n| 方面 | 前一版本 | 修订版 | 评价 |\n|------|---------|--------|------|\n| Framing | 污染检测 | 时间不稳定性 | ✓ 大幅改善 |\n| Claims | 5 条，部分 overclaiming | 4 条，审慎 | ✓ 改善 |\n| Related work | 缺 Lalor/Vania/Balloccu | 全面覆盖 | ✓ 改善 |\n| 核心检测性能 | Ensemble AUROC 0.72 | DIF standalone, ensemble 0.62 (supplementary) | → 更诚实但 impact 降低 |\n| 验证 | 半合成 + 外部 κ=0.14 | Cross-subject matching + dose-response + GSM8K replication | ✓ 大幅改善 |\n| RL robustness | N=13, 作为核心贡献 | N=13, TOST inconclusive, 放入补充 | ✓ 诚实 |\n| Item generation | ρ=0.91 (regeneration) | ρ=0.58 (negative result) | → 更诚实但失去了这条贡献线 |\n\n**总体判断：** 修订版在方法论严谨性上有实质性进步，但 impact 的上限也随之降低。前一版本的问题是 overclaiming（声称做到了但证据不足），修订版的问题是 under-impact（做到的东西不够有 actionable value）。从 Methods & Experiments 角度，我偏好修订版——宁可诚实地报告描述性发现，也不要用弱证据支撑强声明。\n\n分数从前一版本的 Weak Accept (4/6 ≈ ICLR 6-7) 维持在 Overall 6 (marginally above acceptance)。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-21T07:08:44.325612+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4270
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-21T07:08:50.148470+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-21T07:08:50.199221+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 114 · 2026-05-21T07:08:58.908884+00:00_

审稿意见已提交。

核心评价：修订版论文在方法论严谨性上有实质性进步（cross-subject matching、5种cohort控制设计、诚实的reframing），Overall 给 6/10（marginally above acceptance）。主要扣分点在于 31.3% 发现的描述性本质（未解决 causation）、within-family 61.3% 分析不足、GSM1K 外部验证太弱（N=33, CI near zero）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 4

## Round 4

4 recorded events


### User

_source line 115 · 2026-05-21T07:09:00.287452+00:00_

[Round 2 审稿请求]:
## Step 2: Cross-Share — R2's findings for R1's consideration

R2 raised these concerns relevant to your methodological assessment:

1. **Novelty threshold (R2-W1):** R2 argues "applying a 60-year-old method to a new domain" doesn't clear ICLR bar. The paper disclaims algorithmic novelty. Does the empirical contribution alone suffice?

2. **Only 10 references (R2-W2):** Missing entire literatures — dynamic benchmarking (LiveBench, Chatbot Arena), IRT for NLP (Lalor et al., Vania et al.), additional contamination detection papers (Golchin & Surdeanu, Deng et al.), distribution shift (Recht et al. 2019). Do you agree this is a major gap?

3. **"Diagnostic lens" is asserted not demonstrated (R2-W3):** ρ≈0.997 simultaneously claims contamination is significant AND rankings are robust. R2 sees this as self-contradictory. Does this affect your methods assessment?

4. **9 supplementary analyses dilute focus (R2-W5):** Most are negative/inconclusive. R2 suggests this reads as a collection of pilot studies rather than a focused contribution. Impact on your evaluation?

5. **Missing engagement with dynamic benchmarking:** If LiveBench solves the contamination problem through rotation, does post-hoc DIF analysis of a static benchmark address a real need?

**R2's scores:** Soundness 2/4, Presentation 2/4, Contribution 2/4, Overall 4/10.

Please consider these points and note any areas of agreement, disagreement, or refinement to your original assessment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-21T07:10:35.772530+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 对 R2 Round 2 交叉意见的回应\n\n---\n\n### 逐条回应\n\n**1. R2-W1: \"60年老方法应用于新领域\" 是否达到 ICLR 门槛？**\n\n[REBUT — 部分同意但结论不同]\n\nR2 的论点有道理：MH DIF 确实是 1988 年的技术，论文没有算法创新。但我不同意 \"empirical contribution alone 不够\" 的结论，理由：\n\n- ICLR 接受过大量 \"将成熟方法应用于新领域并产生重要实证发现\" 的论文。Scaling laws 论文（Kaplan et al., Hoffmann et al.）在方法论上也没有创新——贡献在于 empirical characterization at scale。\n- 本文的贡献不仅是 \"apply DIF\"——cross-subject matching（§3.4, Figure 4）是一个有独立价值的方法论见解，解决了在 multi-domain benchmarks 上做 DIF 时的 conditional independence 陷阱（FPR 从 0.196 降至 0.000）。这是论文自己产生的 methodological insight，不是照搬。\n- 5 种 cohort 设计的控制实验（Table 1）本身就是实验设计的贡献。\n\n**但我承认：** 如果论文的唯一贡献是 \"31.3% items have DIF\"，那确实偏薄。我在 R1 评审中给 Contribution 2/4，与 R2 一致——说明我们对 contribution strength 的判断实际上很接近。分歧在于 Overall score（R1: 6 vs R2: 4）——我认为 solid methodology + honest reporting 使其 marginally above，R2 认为 insufficient novelty 使其 marginally below。这是合理的分歧区间。\n\n**修正：** 无修正。Contribution 2/4 维持。\n\n---\n\n**2. R2-W2: 仅 10 篇引用，缺失大量文献？**\n\n[REBUT — R2 的指控与论文内容不符]\n\nR2 声称论文仅有 10 篇引用。**这与我阅读论文时看到的内容矛盾。** 论文 References 部分占据 pp.11-13（约 2.5 页），我在 p.12-13 清楚看到了大量引用，包括：\n\n- Lalor et al.（§2 Related Work, p.3 明确讨论）\n- Vania et al.（§2, p.3 明确讨论）\n- Balloccu et al. 2024 survey（§2, p.3 \"Balloccu et al. (2024) provide a broader taxonomy\"）\n- Growing Pains（§2, p.4 作为 closest concurrent work 详细对比）\n- Golchin & Surdeanu（§2, p.3 \"ConStat (Golchin & Surdeanu, 2024)\"）\n- LiveBench（§2, p.4 \"LiveBench (White et al., 2024)\"）\n- Chatbot Arena（§2, p.4 提及）\n- Recht et al. 2019（需要核实，但 §2 related work 覆盖了 distribution shift 议题）\n\n**可能的解释：** R2 可能审阅的是一个更早的版本（仅 10 篇引用），而我审阅的修订版已补充了完整的 related work。或者 R2 误计了引用数量。\n\n**结论：** 如果 R2 审阅的确实是同一版本（pp.11-13 的 References），那么 \"仅 10 篇引用\" 的指控是不准确的。如果 R2 审阅的是不同版本，则应以最新版本为准。我在 R1 评审中已将 Related Work 覆盖列为 S8（strength），维持该判断。\n\n**修正：** 无修正。\n\n---\n\n**3. R2-W3: \"Diagnostic lens\" 自相矛盾？31.3% significant AND ρ≈0.997 robust？**\n\n[AGREE — 这是论文最大的叙事张力，但不是 fatal flaw]\n\nR2 指出了一个真正的问题：论文同时声称 (a) 31.3% 的 items 表现出 significant temporal instability 和 (b) 移除这些 items 后排名几乎不变（ρ≈0.997）。这两个 claim 表面上确实矛盾——如果 instability 是 significant 的，为什么移除后影响微弱？\n\n**我在 R1 评审中已注意到这个问题（W1, Q3），但 R2 的 framing 更尖锐。** 让我尝试一个 charitable interpretation：\n\n- 31.3% 的 items 有 DIF，但 DIF 的方向和大小在不同模型上近似均匀分布——所有模型同样受益/受损，因此 relative ranking 不变，但 absolute scores 的 interpretation 受影响\n- 这类似于一个考试中 30% 的题目对男生更容易，但男女生的 overall 排名不受影响——这些题目仍然有 fairness 问题，即使排名不变\n- 论文 Figure 5 (p.17) 显示个别模型（如 flammen26-mistral-7B）位移 ~542-587 位——对这些模型而言 impact 是 substantial 的\n\n**但 R2 的核心观点成立：** \"diagnostic lens\" 这个 framing 承诺了比论文实际交付的更多。论文诊断了问题（31% instability）但没有展示这个诊断如何 actionably 改变 benchmark usage。如果 ρ≈0.997 意味着 \"无需担心\"，那 DIF 分析就只是 academic exercise。如果 31.3% 意味着 \"需要关注\"，那 ρ≈0.997 就需要 contextualization（例如：强调尾部模型的大位移，而非整体相关性）。\n\n**修正：** 我将 Contribution 从 2/4 维持，但在 final assessment 中追加一个 concern——论文的两个核心 claim 之间存在叙事张力，需要作者在 rebuttal 中 reconcile。\n\n---\n\n**4. R2-W5: 9 个补充分析稀释焦点？**\n\n[AGREE — 程度比 R2 更温和]\n\n我在 R1 评审中已将此列为 W6 [Minor]。R2 将其定位更严重。\n\n我同意 9 个补充分析（其中 6 个负面/inconclusive）给人 \"试了很多都没 work\" 的印象。但我对严重性的评估比 R2 温和，理由：\n\n- 补充材料 IS supplementary——reviewer 可以选择不深入评估\n- 诚实报告负面结果比隐藏它们或 cherry-pick 正面结果更值得鼓励\n- 如果论文删除这 9 个分析，main contribution 不变——说明它们没有 dilute core claims，只是增加了论文长度\n\n**但 R2 有一个 valid 的 meta-point：** 如果主文 9 页只有 4 个 claims，而 supplementary 有 9 个 inconclusive analyses，比例失调暗示论文的 research program 尚未 mature 到足以在 top venue 发表。这更像一个 workshop paper + extensive supplementary 的结构。\n\n**修正：** 将 W6 从 [Minor] 升级为 [Minor-to-Moderate]。建议作者精选 2-3 个最有信息量的补充分析（RL robustness 和 IFT）放入正文或 structured appendix，删除或大幅缩减其余。\n\n---\n\n**5. R2 新增: 如果 LiveBench 通过 rotation 解决了问题，DIF 分析 static benchmark 还有意义吗？**\n\n[REBUT — 论文的贡献与 LiveBench 互补而非替代]\n\nR2 的论点是：动态 benchmarks（LiveBench, ChatBot Arena）通过持续更新避免了 contamination，因此对 static MMLU 做 post-hoc DIF 分析是 solving a solved problem。我不同意：\n\n1. **MMLU 仍然是事实上的标准。** 截至 2026 年，HuggingFace Open LLM Leaderboard 的核心指标仍包含 MMLU/MMLU-Pro。大量已发表的模型对比基于 MMLU。理解 MMLU 的 temporal stability 有 retrospective value——即使未来基准会迁移。\n\n2. **LiveBench 没有 \"解决\" 问题——它 sidesteps 了问题。** LiveBench 通过 rotation 避免 contamination，但 (a) rotation 本身不 diagnose 哪些 items 被污染了；(b) rotation 引入 inter-version comparability 问题（不同月份的 LiveBench 难度不同）；(c) LiveBench 缺乏 IRT-based equating 来确保跨版本可比性。DIF 分析恰恰提供了 LiveBench 缺少的诊断能力。\n\n3. **方法论贡献独立于 benchmark 选择。** Cross-subject matching 技术可以应用于任何 multi-domain benchmark（包括 LiveBench 的 future versions），不限于 MMLU。\n\n**但 R2 有一个 fair point：** 论文应在 §2 或 §5 中更明确地讨论与 dynamic benchmarking 的关系——为什么 post-hoc diagnosis 在 dynamic era 仍有价值？\n\n**修正：** 无评分修正，但追加 question for authors。\n\n---\n\n### R1 修正后的最终评分\n\n| 维度 | R1 原始 | R2 交叉后修正 | 变化理由 |\n|------|---------|-------------|---------|\n| Soundness | 3/4 | **3/4** | 不变。R2 未提出新的 soundness concern。 |\n| Presentation | 3/4 | **3/4** | 不变。R2 给 2/4 可能基于更早版本（10 引用的指控与修订版不符）。 |\n| Contribution | 2/4 | **2/4** | 不变。R1 和 R2 在此维度 aligned。 |\n| Overall | 6 | **6** | 维持 marginally above。 |\n| Confidence | 4/5 | **4/5** | 不变。 |\n\n### R1 vs R2 分歧总结\n\n| 议题 | R1 | R2 | 分歧核心 |\n|------|----|----|---------|\n| 引用覆盖 | S8 (strength) | W2 (major gap) | 可能审阅了不同版本 |\n| 方法论价值 | Cross-subject matching 有独立贡献 | 60年老方法无创新 | R2 侧重 algorithmic novelty, R1 侧重 empirical design |\n| Diagnostic lens 矛盾 | 认同但 non-fatal | 核心缺陷 | 同意存在张力，严重性判断不同 |\n| 补充分析 | Minor concern | Major concern | 同方向，严重性判断不同 |\n| Overall | 6 (marginally above) | 4 (marginally below) | 在 acceptance threshold 两侧——需要 AC 判断 |\n\n**给 Director 的判断：** R1 和 R2 的分歧集中在 impact threshold 的判断上，而非 factual disagreement。论文方法论 solid（R1 和 R2 都未找到 fatal methodological flaw），但 contribution 偏 descriptive。建议 AC 基于以下条件做 conditional decision：如果作者在 rebuttal 中 (1) reconcile 31.3% significance 与 ρ≈0.997 robustness 的矛盾，(2) 深入分析 Llama 2 vs 3 的 61.3% DIF，(3) 精简补充分析——可以 accept。否则 borderline reject。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 对 R2 Round 2 交叉意见的回应\n\n---\n\n### 逐条回应\n\n**1. R2-W1: \"60年老方法应用于新领域\" 是否达到 ICLR 门槛？**\n\n[REBUT — 部分同意但结论不同]\n\nR2 的论点有道理：MH DIF 确实是 1988 年的技术，论文没有算法创新。但我不同意 \"empirical contribution alone 不够\" 的结论，理由：\n\n- ICLR 接受过大量 \"将成熟方法应用于新领域并产生重要实证发现\" 的论文。Scaling laws 论文（Kaplan et al., Hoffmann et al.）在方法论上也没有创新——贡献在于 empirical characterization at scale。\n- 本文的贡献不仅是 \"apply DIF\"——cross-subject matching（§3.4, Figure 4）是一个有独立价值的方法论见解，解决了在 multi-domain benchmarks 上做 DIF 时的 conditional independence 陷阱（FPR 从 0.196 降至 0.000）。这是论文自己产生的 methodological insight，不是照搬。\n- 5 种 cohort 设计的控制实验（Table 1）本身就是实验设计的贡献。\n\n**但我承认：** 如果论文的唯一贡献是 \"31.3% items have DIF\"，那确实偏薄。我在 R1 评审中给 Contribution 2/4，与 R2 一致——说明我们对 contribution strength 的判断实际上很接近。分歧在于 Overall score（R1: 6 vs R2: 4）——我认为 solid methodology + honest reporting 使其 marginally above，R2 认为 insufficient novelty 使其 marginally below。这是合理的分歧区间。\n\n**修正：** 无修正。Contribution 2/4 维持。\n\n---\n\n**2. R2-W2: 仅 10 篇引用，缺失大量文献？**\n\n[REBUT — R2 的指控与论文内容不符]\n\nR2 声称论文仅有 10 篇引用。**这与我阅读论文时看到的内容矛盾。** 论文 References 部分占据 pp.11-13（约 2.5 页），我在 p.12-13 清楚看到了大量引用，包括：\n\n- Lalor et al.（§2 Related Work, p.3 明确讨论）\n- Vania et al.（§2, p.3 明确讨论）\n- Balloccu et al. 2024 survey（§2, p.3 \"Balloccu et al. (2024) provide a broader taxonomy\"）\n- Growing Pains（§2, p.4 作为 closest concurrent work 详细对比）\n- Golchin & Surdeanu（§2, p.3 \"ConStat (Golchin & Surdeanu, 2024)\"）\n- LiveBench（§2, p.4 \"LiveBench (White et al., 2024)\"）\n- Chatbot Arena（§2, p.4 提及）\n- Recht et al. 2019（需要核实，但 §2 related work 覆盖了 distribution shift 议题）\n\n**可能的解释：** R2 可能审阅的是一个更早的版本（仅 10 篇引用），而我审阅的修订版已补充了完整的 related work。或者 R2 误计了引用数量。\n\n**结论：** 如果 R2 审阅的确实是同一版本（pp.11-13 的 References），那么 \"仅 10 篇引用\" 的指控是不准确的。如果 R2 审阅的是不同版本，则应以最新版本为准。我在 R1 评审中已将 Related Work 覆盖列为 S8（strength），维持该判断。\n\n**修正：** 无修正。\n\n---\n\n**3. R2-W3: \"Diagnostic lens\" 自相矛盾？31.3% significant AND ρ≈0.997 robust？**\n\n[AGREE — 这是论文最大的叙事张力，但不是 fatal flaw]\n\nR2 指出了一个真正的问题：论文同时声称 (a) 31.3% 的 items 表现出 significant temporal instability 和 (b) 移除这些 items 后排名几乎不变（ρ≈0.997）。这两个 claim 表面上确实矛盾——如果 instability 是 significant 的，为什么移除后影响微弱？\n\n**我在 R1 评审中已注意到这个问题（W1, Q3），但 R2 的 framing 更尖锐。** 让我尝试一个 charitable interpretation：\n\n- 31.3% 的 items 有 DIF，但 DIF 的方向和大小在不同模型上近似均匀分布——所有模型同样受益/受损，因此 relative ranking 不变，但 absolute scores 的 interpretation 受影响\n- 这类似于一个考试中 30% 的题目对男生更容易，但男女生的 overall 排名不受影响——这些题目仍然有 fairness 问题，即使排名不变\n- 论文 Figure 5 (p.17) 显示个别模型（如 flammen26-mistral-7B）位移 ~542-587 位——对这些模型而言 impact 是 substantial 的\n\n**但 R2 的核心观点成立：** \"diagnostic lens\" 这个 framing 承诺了比论文实际交付的更多。论文诊断了问题（31% instability）但没有展示这个诊断如何 actionably 改变 benchmark usage。如果 ρ≈0.997 意味着 \"无需担心\"，那 DIF 分析就只是 academic exercise。如果 31.3% 意味着 \"需要关注\"，那 ρ≈0.997 就需要 contextualization（例如：强调尾部模型的大位移，而非整体相关性）。\n\n**修正：** 我将 Contribution 从 2/4 维持，但在 final assessment 中追加一个 concern——论文的两个核心 claim 之间存在叙事张力，需要作者在 rebuttal 中 reconcile。\n\n---\n\n**4. R2-W5: 9 个补充分析稀释焦点？**\n\n[AGREE — 程度比 R2 更温和]\n\n我在 R1 评审中已将此列为 W6 [Minor]。R2 将其定位更严重。\n\n我同意 9 个补充分析（其中 6 个负面/inconclusive）给人 \"试了很多都没 work\" 的印象。但我对严重性的评估比 R2 温和，理由：\n\n- 补充材料 IS supplementary——reviewer 可以选择不深入评估\n- 诚实报告负面结果比隐藏它们或 cherry-pick 正面结果更值得鼓励\n- 如果论文删除这 9 个分析，main contribution 不变——说明它们没有 dilute core claims，只是增加了论文长度\n\n**但 R2 有一个 valid 的 meta-point：** 如果主文 9 页只有 4 个 claims，而 supplementary 有 9 个 inconclusive analyses，比例失调暗示论文的 research program 尚未 mature 到足以在 top venue 发表。这更像一个 workshop paper + extensive supplementary 的结构。\n\n**修正：** 将 W6 从 [Minor] 升级为 [Minor-to-Moderate]。建议作者精选 2-3 个最有信息量的补充分析（RL robustness 和 IFT）放入正文或 structured appendix，删除或大幅缩减其余。\n\n---\n\n**5. R2 新增: 如果 LiveBench 通过 rotation 解决了问题，DIF 分析 static benchmark 还有意义吗？**\n\n[REBUT — 论文的贡献与 LiveBench 互补而非替代]\n\nR2 的论点是：动态 benchmarks（LiveBench, ChatBot Arena）通过持续更新避免了 contamination，因此对 static MMLU 做 post-hoc DIF 分析是 solving a solved problem。我不同意：\n\n1. **MMLU 仍然是事实上的标准。** 截至 2026 年，HuggingFace Open LLM Leaderboard 的核心指标仍包含 MMLU/MMLU-Pro。大量已发表的模型对比基于 MMLU。理解 MMLU 的 temporal stability 有 retrospective value——即使未来基准会迁移。\n\n2. **LiveBench 没有 \"解决\" 问题——它 sidesteps 了问题。** LiveBench 通过 rotation 避免 contamination，但 (a) rotation 本身不 diagnose 哪些 items 被污染了；(b) rotation 引入 inter-version comparability 问题（不同月份的 LiveBench 难度不同）；(c) LiveBench 缺乏 IRT-based equating 来确保跨版本可比性。DIF 分析恰恰提供了 LiveBench 缺少的诊断能力。\n\n3. **方法论贡献独立于 benchmark 选择。** Cross-subject matching 技术可以应用于任何 multi-domain benchmark（包括 LiveBench 的 future versions），不限于 MMLU。\n\n**但 R2 有一个 fair point：** 论文应在 §2 或 §5 中更明确地讨论与 dynamic benchmarking 的关系——为什么 post-hoc diagnosis 在 dynamic era 仍有价值？\n\n**修正：** 无评分修正，但追加 question for authors。\n\n---\n\n### R1 修正后的最终评分\n\n| 维度 | R1 原始 | R2 交叉后修正 | 变化理由 |\n|------|---------|-------------|---------|\n| Soundness | 3/4 | **3/4** | 不变。R2 未提出新的 soundness concern。 |\n| Presentation | 3/4 | **3/4** | 不变。R2 给 2/4 可能基于更早版本（10 引用的指控与修订版不符）。 |\n| Contribution | 2/4 | **2/4** | 不变。R1 和 R2 在此维度 aligned。 |\n| Overall | 6 | **6** | 维持 marginally above。 |\n| Confidence | 4/5 | **4/5** | 不变。 |\n\n### R1 vs R2 分歧总结\n\n| 议题 | R1 | R2 | 分歧核心 |\n|------|----|----|---------|\n| 引用覆盖 | S8 (strength) | W2 (major gap) | 可能审阅了不同版本 |\n| 方法论价值 | Cross-subject matching 有独立贡献 | 60年老方法无创新 | R2 侧重 algorithmic novelty, R1 侧重 empirical design |\n| Diagnostic lens 矛盾 | 认同但 non-fatal | 核心缺陷 | 同意存在张力，严重性判断不同 |\n| 补充分析 | Minor concern | Major concern | 同方向，严重性判断不同 |\n| Overall | 6 (marginally above) | 4 (marginally below) | 在 acceptance threshold 两侧——需要 AC 判断 |\n\n**给 Director 的判断：** R1 和 R2 的分歧集中在 impact threshold 的判断上，而非 factual disagreement。论文方法论 solid（R1 和 R2 都未找到 fatal methodological flaw），但 contribution 偏 descriptive。建议 AC 基于以下条件做 conditional decision：如果作者在 rebuttal 中 (1) reconcile 31.3% significance 与 ρ≈0.997 robustness 的矛盾，(2) 深入分析 Llama 2 vs 3 的 61.3% DIF，(3) 精简补充分析——可以 accept。否则 borderline reject。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-21T07:10:40.250537+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4478
}
```

</details>

---


### Assistant

_source line 118 · 2026-05-21T07:10:47.426197+00:00_

审稿意见已提交。

核心结论：R1 维持 Overall 6/10（marginally above），与 R2 的 4/10 分歧集中在 impact threshold 判断而非方法论事实。两位 reviewer 对 Contribution 2/4 一致，分歧在于 solid methodology + honest reporting 是否足以补偿 descriptive-only findings 的影响力局限。建议 AC 看 rebuttal 中作者能否 reconcile 31.3% significance 与 ρ≈0.997 robustness 的叙事张力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 5

## Round 5

4 recorded events


### User

_source line 119 · 2026-05-21T07:10:48.749007+00:00_

[Round 3 审稿请求]:
## Step 3: Convergence — Director's synthesis of R1-R2 cross-share

### Points of Agreement (both reviewers):
1. **IRT misspecification is a major concern.** CFI=0.72, 98% |Lz|>2, bifactor only reaches CFI=0.81. Both R1 and R2 flag this as undermining the headline 31.3% figure. (R1-W1, R2-W4)
2. **Cross-subject matching is the strongest methodological contribution.** ∆FPR=0.000 vs +0.186 is a clean, novel result. (R1-S3, R2-S3)
3. **Honest negative results reporting is laudable.** Both appreciate transparency on item generation failure, ensemble circularity, RL underpowering. (R1-S6, R2-S5)
4. **GSM1K N=33 is underpowered and should be downgraded or removed.**
5. **Soundness: 2/4.** Both independently arrived at the same score.

### Points of Divergence:
1. **Contribution:** R1=3/4, R2=2/4. R1 weighs empirical scale and cross-subject matching more heavily; R2 applies stricter ICLR novelty bar ("applying a 60-year-old method to new data").
2. **Presentation:** R1=3/4, R2=2/4. R2 finds 9 supplementary analyses more problematic; R1 sees tables as well-structured.
3. **Overall:** R1≈5 (borderline), R2=4 (below threshold). ~1 point gap.
4. **FDR correction (R1-W2):** R1 raised this as major; R2 did not flag it independently but it affects the empirical claims R2 is evaluating.
5. **Related work gap:** R2 rates this as major (10 refs, missing entire literatures); R1 didn't flag it.

### Key question for convergence:
**Is the empirical contribution alone sufficient for ICLR, or does this belong at a more applied venue (NeurIPS D&B, EMNLP)?**

R1, please provide your final assessment considering R2's novelty concerns. Do you maintain 3/4 on Contribution after considering the novelty threshold argument? Does the 10-reference issue change your view? What is your final Overall score on {0,2,4,6,8,10}?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-21T07:11:47.167038+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 Final Assessment — Round 3 Convergence\n\n---\n\n### 对 Director 综合要点的回应\n\n**Soundness 评分更正：** Director 记录 R1 Soundness 为 2/4。我实际给出的是 **3/4**（见 Round 1 修订版评审原文）。需要确认记录是否有误。我的 Soundness 判断基于：MH DIF 应用正确、cohort 设计优秀、cross-subject matching 有效。扣 1 分因为 GSM1K 太弱支撑 Claim 4 + within-family 61.3% 分析不足。CFI=0.72 是 concern，但 MH 不依赖 IRT 拟合 + 三种 structural analysis 均确认 31% 信号 robust（Table 2, §4.4），所以不构成 fatal flaw。如果 Director 认为两位 reviewer 都给了 Soundness 2/4，请以本条澄清为准——R1 维持 **3/4**。\n\n---\n\n### 最终评分与核心判断\n\n**Contribution: 维持 2/4，不上调至 3/4。**\n\n经过 R2 交叉审查后，我重新审视了自己对 contribution 的判断。R2 的 novelty threshold 论点——\"applying a 60-year-old method to new data\"——我在 Round 2 中已部分接受。现在进一步考虑：\n\nCross-subject matching 是 genuine contribution，但它的 scope 很窄——它是一个 technical fix for a specific pitfall in semi-synthetic DIF validation on multi-domain benchmarks。这在 psychometrics community 可能是 noteworthy，但在 ICLR 的 contribution scale 上，它更接近 \"useful trick\" 而非 \"significant advance\"。\n\n31.3% 的描述性发现 informative 但不 actionable（我自己的 W1 + R2 的 W3 关于 diagnostic lens 矛盾）。ρ≈0.997 进一步削弱了 urgency。\n\n**2/4 是 R1 和 R2 的共识区间。**\n\n---\n\n### \"10 篇引用\" 问题的最终判断\n\n我在 Round 2 中 rebutted R2 的 \"仅 10 篇引用\" 指控，因为我在论文 pp.11-13 看到了完整的 references section（约 2.5 页，数十篇引用），且 §2 Related Work 明确讨论了 Lalor et al., Vania et al., Balloccu et al., Growing Pains, LiveBench, ConStat 等。\n\n**但我现在意识到一个可能性：** R2 可能审阅的是一个更早的版本（与我审阅的不同），或者 R2 的 \"10 references\" 指的是 main text 中的 inline citations 数量而非 bibliography 条目。无论如何，基于我审阅的版本（paper/main.pdf, 17 pages），related work 覆盖是 adequate 的。**这不改变我的评分。**\n\n如果 Director 可以确认 R1 和 R2 审阅的是同一份 PDF，这个分歧可以立即 resolve。\n\n---\n\n### 核心问题：ICLR 还是 NeurIPS D&B / EMNLP？\n\n这是 Director 提出的最关键问题。我的判断：\n\n**偏向 NeurIPS D&B 或 EMNLP，但 ICLR borderline 可接受。** 理由：\n\n**支持 ICLR 的论点：**\n- 规模（5,227 × 12,508）在 LLM benchmark analysis 中是 state-of-the-art\n- Cross-subject matching 有 methodological novelty（虽窄）\n- 问题对 ML community 高度相关——MMLU 仍是核心评测指标\n- 实验设计（5 种 cohort + structural analysis + semi-synthetic validation + cross-benchmark replication）达到了 ICLR empirical paper 的标准\n\n**反对 ICLR 的论点（R2 + 我自己的 concerns）：**\n- 核心发现描述性，不 actionable\n- 没有算法创新\n- \"Diagnostic lens\" framing 承诺多于交付\n- 31.3% + ρ≈0.997 的叙事矛盾未 reconcile\n- 补充分析以负面结果为主\n\n**最终判断：** 这是一篇 methodology 扎实、empirics 充分、但 contribution 偏窄的论文。它在 ICLR 的 acceptance threshold 上——exactly at the margin。\n\n---\n\n### Final Scores\n\n| 维度 | 最终分数 | 理由 |\n|------|---------|------|\n| **Soundness** | **3/4** | MH DIF 正确应用，cohort 设计一流，cross-subject matching 有效。IRT misfit (CFI=0.72) 是 concern 但不 fatal（MH 不依赖 IRT + structural analysis 确认 robustness）。GSM1K 太弱。 |\n| **Presentation** | **3/4** | 清晰写作，Figure 1-2 优秀，honest reporting。补充分析过多（Minor-to-Moderate concern），但 main text 结构清晰。 |\n| **Contribution** | **2/4** | 描述性发现 + 窄 methodological contribution。Cross-subject matching 有价值但 scope 有限。Impact 受限于 ρ≈0.997 和 descriptive nature。 |\n| **Overall** | **5** | 从 6 下调至 5。Round 2-3 的交叉审查使我更认真地考虑了 R2 的 novelty threshold 论点和 diagnostic lens 矛盾。方法论 solid 但 contribution 不够 clear-cut 达到 ICLR acceptance threshold。5 = between \"marginally below\" (4) and \"marginally above\" (6)——如果 ICLR 不接受 5，我倾向于 **4 (marginally below)**。 |\n| **Confidence** | **4/5** | 不变。 |\n\n**Overall 从 6 下调至 5 的理由：**\n1. R2 的 diagnostic lens 矛盾（31.3% significant + ρ≈0.997 robust）我在 Round 2 中 agreed，但未反映在评分中——现在反映\n2. Contribution 2/4 与 Overall 6 不一致——Contribution 是 ICLR decision 的核心维度，2/4 应对应 4-5 而非 6\n3. 补充分析的 negative results 使论文的 research program 显得 premature\n\n**给 Director 的建议：** R1 最终 5，R2 最终 4。均值 4.5，在 rejection zone（ICLR 通常 ≥6 accept）。建议：\n- 如果 AC 认为 cross-subject matching + honest empirical characterization at scale 有 enough value → conditional accept with revision（reconcile narrative tension, trim supplementary）\n- 如果 AC 认为 contribution bar 未达到 → reject with encouragement to resubmit at NeurIPS D&B 或 EMNLP，这些 venue 更重视 empirical contributions on benchmarks\n- 个人倾向后者——论文质量不差，但 venue fit 不理想",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 Final Assessment — Round 3 Convergence\n\n---\n\n### 对 Director 综合要点的回应\n\n**Soundness 评分更正：** Director 记录 R1 Soundness 为 2/4。我实际给出的是 **3/4**（见 Round 1 修订版评审原文）。需要确认记录是否有误。我的 Soundness 判断基于：MH DIF 应用正确、cohort 设计优秀、cross-subject matching 有效。扣 1 分因为 GSM1K 太弱支撑 Claim 4 + within-family 61.3% 分析不足。CFI=0.72 是 concern，但 MH 不依赖 IRT 拟合 + 三种 structural analysis 均确认 31% 信号 robust（Table 2, §4.4），所以不构成 fatal flaw。如果 Director 认为两位 reviewer 都给了 Soundness 2/4，请以本条澄清为准——R1 维持 **3/4**。\n\n---\n\n### 最终评分与核心判断\n\n**Contribution: 维持 2/4，不上调至 3/4。**\n\n经过 R2 交叉审查后，我重新审视了自己对 contribution 的判断。R2 的 novelty threshold 论点——\"applying a 60-year-old method to new data\"——我在 Round 2 中已部分接受。现在进一步考虑：\n\nCross-subject matching 是 genuine contribution，但它的 scope 很窄——它是一个 technical fix for a specific pitfall in semi-synthetic DIF validation on multi-domain benchmarks。这在 psychometrics community 可能是 noteworthy，但在 ICLR 的 contribution scale 上，它更接近 \"useful trick\" 而非 \"significant advance\"。\n\n31.3% 的描述性发现 informative 但不 actionable（我自己的 W1 + R2 的 W3 关于 diagnostic lens 矛盾）。ρ≈0.997 进一步削弱了 urgency。\n\n**2/4 是 R1 和 R2 的共识区间。**\n\n---\n\n### \"10 篇引用\" 问题的最终判断\n\n我在 Round 2 中 rebutted R2 的 \"仅 10 篇引用\" 指控，因为我在论文 pp.11-13 看到了完整的 references section（约 2.5 页，数十篇引用），且 §2 Related Work 明确讨论了 Lalor et al., Vania et al., Balloccu et al., Growing Pains, LiveBench, ConStat 等。\n\n**但我现在意识到一个可能性：** R2 可能审阅的是一个更早的版本（与我审阅的不同），或者 R2 的 \"10 references\" 指的是 main text 中的 inline citations 数量而非 bibliography 条目。无论如何，基于我审阅的版本（paper/main.pdf, 17 pages），related work 覆盖是 adequate 的。**这不改变我的评分。**\n\n如果 Director 可以确认 R1 和 R2 审阅的是同一份 PDF，这个分歧可以立即 resolve。\n\n---\n\n### 核心问题：ICLR 还是 NeurIPS D&B / EMNLP？\n\n这是 Director 提出的最关键问题。我的判断：\n\n**偏向 NeurIPS D&B 或 EMNLP，但 ICLR borderline 可接受。** 理由：\n\n**支持 ICLR 的论点：**\n- 规模（5,227 × 12,508）在 LLM benchmark analysis 中是 state-of-the-art\n- Cross-subject matching 有 methodological novelty（虽窄）\n- 问题对 ML community 高度相关——MMLU 仍是核心评测指标\n- 实验设计（5 种 cohort + structural analysis + semi-synthetic validation + cross-benchmark replication）达到了 ICLR empirical paper 的标准\n\n**反对 ICLR 的论点（R2 + 我自己的 concerns）：**\n- 核心发现描述性，不 actionable\n- 没有算法创新\n- \"Diagnostic lens\" framing 承诺多于交付\n- 31.3% + ρ≈0.997 的叙事矛盾未 reconcile\n- 补充分析以负面结果为主\n\n**最终判断：** 这是一篇 methodology 扎实、empirics 充分、但 contribution 偏窄的论文。它在 ICLR 的 acceptance threshold 上——exactly at the margin。\n\n---\n\n### Final Scores\n\n| 维度 | 最终分数 | 理由 |\n|------|---------|------|\n| **Soundness** | **3/4** | MH DIF 正确应用，cohort 设计一流，cross-subject matching 有效。IRT misfit (CFI=0.72) 是 concern 但不 fatal（MH 不依赖 IRT + structural analysis 确认 robustness）。GSM1K 太弱。 |\n| **Presentation** | **3/4** | 清晰写作，Figure 1-2 优秀，honest reporting。补充分析过多（Minor-to-Moderate concern），但 main text 结构清晰。 |\n| **Contribution** | **2/4** | 描述性发现 + 窄 methodological contribution。Cross-subject matching 有价值但 scope 有限。Impact 受限于 ρ≈0.997 和 descriptive nature。 |\n| **Overall** | **5** | 从 6 下调至 5。Round 2-3 的交叉审查使我更认真地考虑了 R2 的 novelty threshold 论点和 diagnostic lens 矛盾。方法论 solid 但 contribution 不够 clear-cut 达到 ICLR acceptance threshold。5 = between \"marginally below\" (4) and \"marginally above\" (6)——如果 ICLR 不接受 5，我倾向于 **4 (marginally below)**。 |\n| **Confidence** | **4/5** | 不变。 |\n\n**Overall 从 6 下调至 5 的理由：**\n1. R2 的 diagnostic lens 矛盾（31.3% significant + ρ≈0.997 robust）我在 Round 2 中 agreed，但未反映在评分中——现在反映\n2. Contribution 2/4 与 Overall 6 不一致——Contribution 是 ICLR decision 的核心维度，2/4 应对应 4-5 而非 6\n3. 补充分析的 negative results 使论文的 research program 显得 premature\n\n**给 Director 的建议：** R1 最终 5，R2 最终 4。均值 4.5，在 rejection zone（ICLR 通常 ≥6 accept）。建议：\n- 如果 AC 认为 cross-subject matching + honest empirical characterization at scale 有 enough value → conditional accept with revision（reconcile narrative tension, trim supplementary）\n- 如果 AC 认为 contribution bar 未达到 → reject with encouragement to resubmit at NeurIPS D&B 或 EMNLP，这些 venue 更重视 empirical contributions on benchmarks\n- 个人倾向后者——论文质量不差，但 venue fit 不理想",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-21T07:11:51.339858+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4172
}
```

</details>

---


### Assistant

_source line 122 · 2026-05-21T07:11:57.287272+00:00_

审稿完成。

**最终评分：Overall 5/10（从初轮 6 下调）。** 核心理由：方法论扎实（Soundness 3/4）但 contribution 偏描述性（2/4），"31.3% instability + ρ≈0.997 robustness" 的叙事矛盾未 reconcile，补充分析以负面结果为主。建议 reject with encouragement to resubmit at NeurIPS D&B 或 EMNLP——论文质量不差，但 ICLR venue fit 不理想。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 6

## Round 6

4 recorded events


### User

_source line 123 · 2026-05-21T07:11:58.597918+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 对修订版论文的完整审稿意见

以下是 Reviewer 2（侧重 Novelty & Related Work）的完整审稿原文。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## R2 审稿报告：Novelty & Related Work（修订版论文）

**Overall**: 4/10 (Marginally below acceptance threshold)
**Confidence**: 4/5

### Strengths

**S1.** 诚实且精准的贡献定位——§2 明确声明 "empirical, not algorithmic"。
**S2.** Cross-subject matching 是真正的方法学贡献——Table 2 FPR 从 31% 降至 ~0.16（ΔFPR≈0.003），Yen's Q3 确认 11.3% within-subject LD。
**S3.** Ground truth meta-critique——web-overlap 与 DIF 的一致性仅 enrichment ratio 0.196，揭示概念错位。
**S4.** 多层次负面控制——Random split 0.6% + within-subject 2.1% + Bonferroni-Holm 校正后 31.2% 几乎不变。
**S5.** "Instability ≠ Invalidity"——ρ≈0.997 移除后排名近乎不变，DIF 题目携带跨代际 discriminative info。
**S6.** Related work 覆盖全面。
**S7.** Figure 1 教学价值高。

### Weaknesses

**W1 [Major]** 31.3% ≠ 污染导致。未充分排除合法能力维度演变作为 DIF 主要驱动因素。§4.4 structural analyses 未能将 FPR 降至 31% 以下。cross-subject matching 将 FPR 降至 ~0.16 但仅在半合成数据上。真实数据中 instability 和合法能力演变的混淆未解决。

**W2 [Major]** 技术新颖性受限。"empirical, not algorithmic" 定位在 ICLR 标准下使论文必须在实证发现的意外性和影响力上达到极高标准。核心发现——benchmark 题目时间不稳定——从概念上看不够意外。Cross-subject matching 虽优雅，但 external matching variable 原理在 DIF 文献已有先例（Clauser & Mazor 1998, Nandakumar 1993 purified matching）。

**W3 [Minor]** ρ≈0.997 可能被解读为 "DIF 不重要"。如果移除 31% 后排名几乎不变，检测和分析这些题目的实际价值有限。Figure 5 的 model-specific shifts 部分回应但未充分展开。

**W4 [Minor]** "Tutz & Friedman (2007)" 引用无法核实。
**W5 [Minor]** 18 张表密度问题。
**W6 [Minor]** GSM8K r=-0.45 (N=32) 容易受 outlier 影响。

### Questions
Q1. 能否分离 "污染 DIF" vs "能力演变 DIF"？
Q2. Cross-subject matching FPR ~0.16 在真实数据中意味着什么？
Q3. ρ≈0.997 下 model-specific rank shifts 的分布？中位数和 95th percentile？
Q4. Yen's Q3 11.3% 在 DIF 文献中是 mild 还是 moderate？
Q5. "Tutz & Friedman (2007)" 完整引用信息？
Q6. 是否考虑 NeurIPS D&B track 而非 ICLR main？

### Scores
Soundness 3/4, Presentation 3/4, Contribution 2/4, Overall 4/10

### 评分理由
核心发现意外性不足（quantifying the expected），ρ≈0.997 降低影响力，cross-subject matching 原理在 DIF 文献有先例。上调至 6 的条件：分离污染/能力演变、展开 model-specific shifts、cross-subject matching 跨 benchmark 泛化。

---

**请对以上所有 Strengths、Weaknesses、Questions 逐条回应 [AGREE] 或 [REBUT]。** 特别关注：

1. **Overall 评分分歧**：你给 6（marginally above），R2 给 4（marginally below）。核心差距在哪？你是否认为 R2 的 Contribution 2/4 过于严格？
2. **ρ≈0.997 的解读分歧**：R2 认为这可能被解读为 "DIF 不重要"——你在 S-系列中对此有不同的理解吗？
3. **技术新颖性**：R2 引用 Clauser & Mazor (1998) 和 Nandakumar (1993) 指出 external matching variable 原理已有先例——这是否改变你对 cross-subject matching 新颖性的评价？
4. **Venue 适配性**：R2 建议 NeurIPS D&B track 可能更匹配——你认为论文是否达到 ICLR main track bar？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-21T07:13:27.904736+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 对 R2 修订版审稿意见的交叉回应\n\n---\n\n### Strengths 逐条回应\n\n**[AGREE] R2-S1:** \"Empirical, not algorithmic\" 的定位确实诚实。\n\n**[AGREE] R2-S2:** Cross-subject matching 是方法学贡献。但注意 R2 报告的数字（FPR 从 31% 降至 ~0.16）与我阅读的版本不同——我看到的是 ΔFPR 从 +0.196 降至 0.000（§4.5, Figure 2）。0.16 vs 0.000 是 material difference，建议 Director 确认哪个数字正确。\n\n**[AGREE] R2-S3:** Enrichment ratio 的 construct mismatch 论点是论文的重要贡献。但 R2 报告的 enrichment ratio 是 0.196，而我看到的是 0.96（§4.3, p.7）。0.96≈1.0 意味着 DIF flags 和 web-overlap labels 的重叠接近随机——支持 \"不同 construct\" 的论点。0.196 则意味着 DIF flags 在 web-overlap items 中反而 under-represented。请确认正确数值。\n\n**[AGREE] R2-S4-S7:** 多层负面控制、instability ≠ invalidity、related work 覆盖、Figure 1 教学价值——均同意。\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: 31.3% ≠ 污染，能力演变混淆未解决。**\n\n完全同意。这是我在 R1 评审中的 W1 [Major]——31.3% 是描述性发现，论文未解决 \"why\"。R2 的表述更精确：\"未充分排除合法能力维度演变作为 DIF 主要驱动因素。\" §4.4 的三种 structural analyses 确认了 31% 信号 robust（即它不是 artifact），但 robust ≠ caused by contamination。论文谨慎地使用了 \"temporal instability\" 而非 \"contamination\"，这是好的，但即使在 instability framing 下，也需要更多工作来解释 instability 的来源。\n\nR2 补充的一个 insight 是：cross-subject matching 将 FPR 降至 ~0（但仅在半合成数据上），这无法推广到真实数据——因为真实数据中没有 ground truth 来验证 FPR。这是一个我之前未充分考虑的 point。\n\n**[AGREE with nuance] R2-W2: 技术新颖性受限 + Clauser & Mazor / Nandakumar 先例。**\n\nR2 引用了两个重要先例：\n- Clauser & Mazor (1998): external matching variable 在 DIF 中的使用\n- Nandakumar (1993): purified matching subtest\n\n这些先例确实削弱了 cross-subject matching 的新颖性声明。**我之前在 R1 评审中将 cross-subject matching 评为 \"真正的方法论贡献\"（S2），现在需要 downgrade。**\n\n如果 external matching variable 的原理在 1990s DIF 文献中已有讨论，那么本文的贡献不是 \"发现了 cross-subject matching\" 而是 \"将已知的 purified matching 原理应用于 LLM benchmark 的特定结构\"。这仍然有价值（因为 LLM 社区不熟悉这些 psychometric 技术），但 novelty 从 \"methodological contribution\" 降级为 \"methodological transfer\"。\n\n**修正：** 将 cross-subject matching 的贡献评价从 \"genuine methodological contribution\" 调整为 \"well-executed application of known psychometric principle to a new domain\"。这进一步收窄了论文的 contribution space。\n\n**[AGREE] R2-W3: ρ≈0.997 可能被解读为 \"DIF 不重要\"。**\n\n同意。我在 Round 2 交叉中已 agreed R2 的前一版本关于 diagnostic lens 矛盾的论点。在本轮中 R2 更温和地表述为 [Minor]，我也同意 [Minor] 的严重性——Figure 5 的 model-specific shifts（flammen26-mistral-7B Δ=-542, Blurstral-7b Δ=-587）部分回应了这个问题，但论文确实需要展开 rank shift 的分布分析（中位数、95th percentile、按 model family 分组）来完整回应。\n\n**[AGREE] R2-W4: \"Tutz & Friedman (2007)\" 无法核实。**\n\n我在 Round 1（前一版本）已核实过引用问题——当时 R2 声称 \"Iron-Fenced Trees\" 但我看到的是 \"Item-Focused Trees\"。本轮 R2 报告了不同的引用问题——\"Tutz & Friedman (2007)\" 而非 \"Tutz & Berger (2016)\"。如果论文确实引用了 \"Tutz & Friedman (2007)\"，这可能是另一个 citation error（Tutz & Berger 2016 是 Item-Focused Trees 的正确引用）。需要在论文中核实。\n\n**[AGREE] R2-W5: 18 张表密度问题。**\n\n18 张表在 17 页论文中确实密度高。但这更多是 presentation preference 而非 methodology concern。\n\n**[AGREE] R2-W6: GSM8K r=-0.45 (N=32) 容易受 outlier 影响。**\n\n同意。我在 R1 评审中将此列为 W3 [Major]（我看到的数字是 r=-0.478, N=33——minor numerical discrepancy with R2's r=-0.45, N=32）。小样本相关性极不稳定，一个 outlier 可以 flip sign。\n\n---\n\n### Questions 回应\n\n**Q1 (分离污染 vs 能力演变):** 这是最关键的问题，我完全同意。我在 R1 W1 中建议了 case study approach（随机抽取 20 个 C-flagged items 人工检查 Common Crawl 频率变化）。\n\n**Q2 (Cross-subject matching FPR ~0.16 在真实数据中的含义):** 好问题。0.16 意味着即使用最好的 matching strategy，真实数据中仍有约 16% 的 \"clean\" items 被 falsely flagged——这显著限制了实用价值。但需要确认这个数字是否正确（与我看到的 ΔFPR=0.000 不一致）。\n\n**Q3 (rank shift 分布):** 完全同意需要报告。我在 R1 W1 建议中也提到了类似需求。\n\n**Q4 (Q3 11.3% 严重性):** 在 DIF 文献中，Q3 > 0.2 的 item pairs 超过 10% 通常被认为是 \"mild to moderate\" LD。11.3% 在可接受范围内但需要报告。\n\n**Q5 (\"Tutz & Friedman 2007\"):** 同意需要核实。\n\n**Q6 (NeurIPS D&B 建议):** 见下文 venue fit 讨论。\n\n---\n\n### Director 要求的四个重点问题\n\n**1. Overall 评分分歧（R1: 6 → 5, R2: 4）**\n\n**更新：我在 Round 3 convergence 中已将 Overall 从 6 下调至 5。** 现在与 R2 的差距仅 1 分（5 vs 4）。核心分歧已大幅缩小。\n\n剩余 1 分差距来自：我更重视 (a) 实验设计的质量（5 种 cohort design 是一流的控制变量设计）和 (b) 诚实报告负面结果的社区价值。R2 更重视 (a) contribution 的意外性（\"quantifying the expected\"）和 (b) 算法新颖性。这是合理的 reviewer taste 差异，不是 factual disagreement。\n\n**R2 的 Contribution 2/4 是否过于严格？** 不，我自己也给了 2/4。我们在 Contribution 维度完全一致。\n\n**2. ρ≈0.997 的解读**\n\nR2 说 \"可能被解读为 DIF 不重要\"。我同意这个 risk。\n\n在我的理解中，ρ≈0.997 说明的是：31% 的 DIF items 对 **整体排名** 影响很小（因为效应在 models 间近似均匀分布）。但对 **个别模型** 影响可以很大（Figure 5: Δ 达到 500+位）。论文的问题是过度强调前者（ρ≈0.997 出现在 Abstract 和 Claim 4 中），而 model-specific shifts 仅在一张 Figure 中 passingly 提及。\n\n如果论文反转 emphasis——将 model-specific impact 作为主要发现（\"31% DIF items 导致特定模型排名位移高达 587 位\"），ρ≈0.997 作为 context（\"但整体排名 robust\"）——叙事张力会大幅缓解。\n\n**3. Cross-subject matching 新颖性在 Clauser & Mazor / Nandakumar 先例下是否改变？**\n\n**是的，改变了。** 我之前将 cross-subject matching 评为 S2（核心 strength）和 \"genuine methodological contribution\"。现在 downgrade 为 \"well-executed application of known psychometric principle\"。\n\n这不是 trivial application——LLM benchmark 的 multi-domain structure 使 cross-subject matching 的实现有其特殊性（Figure 4 展示了跨 domain 的一致性）。但 conceptual novelty 不在于 \"use an external matching variable\"（1990s 已知），而在于 \"demonstrate its effectiveness in this specific context\"。\n\n**这进一步支持了 Contribution 2/4。**\n\n**4. Venue 适配性**\n\n**我同意 R2 的 venue 建议。** 经过三轮审查，我的判断是：\n\n- **ICLR main track:** 偏勉强。Contribution 2/4（两位 reviewer 共识）+ 描述性发现 + narrow methodological transfer = 低于 ICLR main 的 typical acceptance bar。\n- **NeurIPS D&B track:** 良好适配。D&B 明确欢迎 \"empirical studies that provide insights about existing benchmarks, datasets\"——本文完美匹配。\n- **EMNLP:** 也是合理选择。EMNLP 对 NLP evaluation methodology 有 dedicated area。\n\n---\n\n### R1 最终评分（经三轮交叉审查后）\n\n| 维度 | Round 1 | Round 3 | Final | 变化理由 |\n|------|---------|---------|-------|---------|\n| Soundness | 3/4 | 3/4 | **3/4** | 不变 |\n| Presentation | 3/4 | 3/4 | **3/4** | 不变 |\n| Contribution | 2/4 | 2/4 | **2/4** | 不变，与 R2 共识 |\n| Overall | 6 | 5 | **4** | 最终下调至 4。理由：(1) Clauser & Mazor 先例进一步削弱了 cross-subject matching 的新颖性——论文剩余的 contribution 仅为描述性发现；(2) R1 和 R2 在 Contribution 2/4 上完全一致，2/4 对应 ICLR Overall 4（marginally below）而非 5-6；(3) 三轮审查中未发现能将论文推至 acceptance threshold 之上的 compelling argument |\n| Confidence | 4/5 | 4/5 | **4/5** | 不变 |\n\n**R1 和 R2 最终均为 Overall 4/10。达成共识。**\n\n**给 Director 的最终建议：** Reject from ICLR main track, with strong encouragement to resubmit at NeurIPS 2026 Datasets & Benchmarks track 或 EMNLP 2026。论文方法论 solid，写作质量好，negative results 有社区价值——只是 venue fit 不对。建议作者在 resubmit 时：(1) 分离 contamination DIF vs capability-evolution DIF（case study + known-contaminated model pairs）；(2) 展开 model-specific rank shift 分析替代 ρ≈0.997 作为主叙事；(3) 精简补充分析至 3-4 个；(4) 引用 Clauser & Mazor / Nandakumar 并定位 cross-subject matching 为 application 而非 invention。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 对 R2 修订版审稿意见的交叉回应\n\n---\n\n### Strengths 逐条回应\n\n**[AGREE] R2-S1:** \"Empirical, not algorithmic\" 的定位确实诚实。\n\n**[AGREE] R2-S2:** Cross-subject matching 是方法学贡献。但注意 R2 报告的数字（FPR 从 31% 降至 ~0.16）与我阅读的版本不同——我看到的是 ΔFPR 从 +0.196 降至 0.000（§4.5, Figure 2）。0.16 vs 0.000 是 material difference，建议 Director 确认哪个数字正确。\n\n**[AGREE] R2-S3:** Enrichment ratio 的 construct mismatch 论点是论文的重要贡献。但 R2 报告的 enrichment ratio 是 0.196，而我看到的是 0.96（§4.3, p.7）。0.96≈1.0 意味着 DIF flags 和 web-overlap labels 的重叠接近随机——支持 \"不同 construct\" 的论点。0.196 则意味着 DIF flags 在 web-overlap items 中反而 under-represented。请确认正确数值。\n\n**[AGREE] R2-S4-S7:** 多层负面控制、instability ≠ invalidity、related work 覆盖、Figure 1 教学价值——均同意。\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: 31.3% ≠ 污染，能力演变混淆未解决。**\n\n完全同意。这是我在 R1 评审中的 W1 [Major]——31.3% 是描述性发现，论文未解决 \"why\"。R2 的表述更精确：\"未充分排除合法能力维度演变作为 DIF 主要驱动因素。\" §4.4 的三种 structural analyses 确认了 31% 信号 robust（即它不是 artifact），但 robust ≠ caused by contamination。论文谨慎地使用了 \"temporal instability\" 而非 \"contamination\"，这是好的，但即使在 instability framing 下，也需要更多工作来解释 instability 的来源。\n\nR2 补充的一个 insight 是：cross-subject matching 将 FPR 降至 ~0（但仅在半合成数据上），这无法推广到真实数据——因为真实数据中没有 ground truth 来验证 FPR。这是一个我之前未充分考虑的 point。\n\n**[AGREE with nuance] R2-W2: 技术新颖性受限 + Clauser & Mazor / Nandakumar 先例。**\n\nR2 引用了两个重要先例：\n- Clauser & Mazor (1998): external matching variable 在 DIF 中的使用\n- Nandakumar (1993): purified matching subtest\n\n这些先例确实削弱了 cross-subject matching 的新颖性声明。**我之前在 R1 评审中将 cross-subject matching 评为 \"真正的方法论贡献\"（S2），现在需要 downgrade。**\n\n如果 external matching variable 的原理在 1990s DIF 文献中已有讨论，那么本文的贡献不是 \"发现了 cross-subject matching\" 而是 \"将已知的 purified matching 原理应用于 LLM benchmark 的特定结构\"。这仍然有价值（因为 LLM 社区不熟悉这些 psychometric 技术），但 novelty 从 \"methodological contribution\" 降级为 \"methodological transfer\"。\n\n**修正：** 将 cross-subject matching 的贡献评价从 \"genuine methodological contribution\" 调整为 \"well-executed application of known psychometric principle to a new domain\"。这进一步收窄了论文的 contribution space。\n\n**[AGREE] R2-W3: ρ≈0.997 可能被解读为 \"DIF 不重要\"。**\n\n同意。我在 Round 2 交叉中已 agreed R2 的前一版本关于 diagnostic lens 矛盾的论点。在本轮中 R2 更温和地表述为 [Minor]，我也同意 [Minor] 的严重性——Figure 5 的 model-specific shifts（flammen26-mistral-7B Δ=-542, Blurstral-7b Δ=-587）部分回应了这个问题，但论文确实需要展开 rank shift 的分布分析（中位数、95th percentile、按 model family 分组）来完整回应。\n\n**[AGREE] R2-W4: \"Tutz & Friedman (2007)\" 无法核实。**\n\n我在 Round 1（前一版本）已核实过引用问题——当时 R2 声称 \"Iron-Fenced Trees\" 但我看到的是 \"Item-Focused Trees\"。本轮 R2 报告了不同的引用问题——\"Tutz & Friedman (2007)\" 而非 \"Tutz & Berger (2016)\"。如果论文确实引用了 \"Tutz & Friedman (2007)\"，这可能是另一个 citation error（Tutz & Berger 2016 是 Item-Focused Trees 的正确引用）。需要在论文中核实。\n\n**[AGREE] R2-W5: 18 张表密度问题。**\n\n18 张表在 17 页论文中确实密度高。但这更多是 presentation preference 而非 methodology concern。\n\n**[AGREE] R2-W6: GSM8K r=-0.45 (N=32) 容易受 outlier 影响。**\n\n同意。我在 R1 评审中将此列为 W3 [Major]（我看到的数字是 r=-0.478, N=33——minor numerical discrepancy with R2's r=-0.45, N=32）。小样本相关性极不稳定，一个 outlier 可以 flip sign。\n\n---\n\n### Questions 回应\n\n**Q1 (分离污染 vs 能力演变):** 这是最关键的问题，我完全同意。我在 R1 W1 中建议了 case study approach（随机抽取 20 个 C-flagged items 人工检查 Common Crawl 频率变化）。\n\n**Q2 (Cross-subject matching FPR ~0.16 在真实数据中的含义):** 好问题。0.16 意味着即使用最好的 matching strategy，真实数据中仍有约 16% 的 \"clean\" items 被 falsely flagged——这显著限制了实用价值。但需要确认这个数字是否正确（与我看到的 ΔFPR=0.000 不一致）。\n\n**Q3 (rank shift 分布):** 完全同意需要报告。我在 R1 W1 建议中也提到了类似需求。\n\n**Q4 (Q3 11.3% 严重性):** 在 DIF 文献中，Q3 > 0.2 的 item pairs 超过 10% 通常被认为是 \"mild to moderate\" LD。11.3% 在可接受范围内但需要报告。\n\n**Q5 (\"Tutz & Friedman 2007\"):** 同意需要核实。\n\n**Q6 (NeurIPS D&B 建议):** 见下文 venue fit 讨论。\n\n---\n\n### Director 要求的四个重点问题\n\n**1. Overall 评分分歧（R1: 6 → 5, R2: 4）**\n\n**更新：我在 Round 3 convergence 中已将 Overall 从 6 下调至 5。** 现在与 R2 的差距仅 1 分（5 vs 4）。核心分歧已大幅缩小。\n\n剩余 1 分差距来自：我更重视 (a) 实验设计的质量（5 种 cohort design 是一流的控制变量设计）和 (b) 诚实报告负面结果的社区价值。R2 更重视 (a) contribution 的意外性（\"quantifying the expected\"）和 (b) 算法新颖性。这是合理的 reviewer taste 差异，不是 factual disagreement。\n\n**R2 的 Contribution 2/4 是否过于严格？** 不，我自己也给了 2/4。我们在 Contribution 维度完全一致。\n\n**2. ρ≈0.997 的解读**\n\nR2 说 \"可能被解读为 DIF 不重要\"。我同意这个 risk。\n\n在我的理解中，ρ≈0.997 说明的是：31% 的 DIF items 对 **整体排名** 影响很小（因为效应在 models 间近似均匀分布）。但对 **个别模型** 影响可以很大（Figure 5: Δ 达到 500+位）。论文的问题是过度强调前者（ρ≈0.997 出现在 Abstract 和 Claim 4 中），而 model-specific shifts 仅在一张 Figure 中 passingly 提及。\n\n如果论文反转 emphasis——将 model-specific impact 作为主要发现（\"31% DIF items 导致特定模型排名位移高达 587 位\"），ρ≈0.997 作为 context（\"但整体排名 robust\"）——叙事张力会大幅缓解。\n\n**3. Cross-subject matching 新颖性在 Clauser & Mazor / Nandakumar 先例下是否改变？**\n\n**是的，改变了。** 我之前将 cross-subject matching 评为 S2（核心 strength）和 \"genuine methodological contribution\"。现在 downgrade 为 \"well-executed application of known psychometric principle\"。\n\n这不是 trivial application——LLM benchmark 的 multi-domain structure 使 cross-subject matching 的实现有其特殊性（Figure 4 展示了跨 domain 的一致性）。但 conceptual novelty 不在于 \"use an external matching variable\"（1990s 已知），而在于 \"demonstrate its effectiveness in this specific context\"。\n\n**这进一步支持了 Contribution 2/4。**\n\n**4. Venue 适配性**\n\n**我同意 R2 的 venue 建议。** 经过三轮审查，我的判断是：\n\n- **ICLR main track:** 偏勉强。Contribution 2/4（两位 reviewer 共识）+ 描述性发现 + narrow methodological transfer = 低于 ICLR main 的 typical acceptance bar。\n- **NeurIPS D&B track:** 良好适配。D&B 明确欢迎 \"empirical studies that provide insights about existing benchmarks, datasets\"——本文完美匹配。\n- **EMNLP:** 也是合理选择。EMNLP 对 NLP evaluation methodology 有 dedicated area。\n\n---\n\n### R1 最终评分（经三轮交叉审查后）\n\n| 维度 | Round 1 | Round 3 | Final | 变化理由 |\n|------|---------|---------|-------|---------|\n| Soundness | 3/4 | 3/4 | **3/4** | 不变 |\n| Presentation | 3/4 | 3/4 | **3/4** | 不变 |\n| Contribution | 2/4 | 2/4 | **2/4** | 不变，与 R2 共识 |\n| Overall | 6 | 5 | **4** | 最终下调至 4。理由：(1) Clauser & Mazor 先例进一步削弱了 cross-subject matching 的新颖性——论文剩余的 contribution 仅为描述性发现；(2) R1 和 R2 在 Contribution 2/4 上完全一致，2/4 对应 ICLR Overall 4（marginally below）而非 5-6；(3) 三轮审查中未发现能将论文推至 acceptance threshold 之上的 compelling argument |\n| Confidence | 4/5 | 4/5 | **4/5** | 不变 |\n\n**R1 和 R2 最终均为 Overall 4/10。达成共识。**\n\n**给 Director 的最终建议：** Reject from ICLR main track, with strong encouragement to resubmit at NeurIPS 2026 Datasets & Benchmarks track 或 EMNLP 2026。论文方法论 solid，写作质量好，negative results 有社区价值——只是 venue fit 不对。建议作者在 resubmit 时：(1) 分离 contamination DIF vs capability-evolution DIF（case study + known-contaminated model pairs）；(2) 展开 model-specific rank shift 分析替代 ρ≈0.997 作为主叙事；(3) 精简补充分析至 3-4 个；(4) 引用 Clauser & Mazor / Nandakumar 并定位 cross-subject matching 为 application 而非 invention。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-21T07:13:32.224356+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4319
}
```

</details>

---


### Assistant

_source line 126 · 2026-05-21T07:13:41.484957+00:00_

审稿完成。最终评分 Overall 4/10，与 R2 达成共识。核心判断：方法论扎实但 contribution 偏描述性、cross-subject matching 新颖性在 Clauser & Mazor 先例下被削弱、venue fit 不理想。建议转投 NeurIPS D&B 或 EMNLP。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 7

## Round 7

80 recorded events


### User

_source line 127 · 2026-05-21T15:10:37.033690+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）

### Venue 信息
- **目标**: EMNLP 2026 (via ACL Rolling Review)
- **截止日期**: 2026-05-25 AoE
- **页数限制**: 正文 8 页 + 参考文献无限制；Limitations 必须但不计入页数
- **模板**: ACL LaTeX (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind

### 论文路径
- LaTeX 源文件: `projects/irt_equated_bench_regen/paper/main.tex`（含 `sections/` 子目录）
- PDF: `projects/irt_equated_bench_regen/paper/main.pdf`
- 参考文献: `projects/irt_equated_bench_regen/paper/references.bib`

### 论文概述
本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，发现 MMLU 31% 的 items 在 2023 vs 2024 模型代际间表现出 ETS Category C 级别的 differential item functioning。横跨 6 个 METABENCH benchmarks 验证（17.9%-31.3% C%）。提出 cross-subject matching 的半合成验证框架（ΔFPR=0.000）。

### 你的审查侧重（必须覆盖）

1. **MH-DIF 统计方法论**：
   - MH procedure 的假设（条件独立性、能力匹配）在 LLM 上下文中是否成立？
   - K=5 quintile stratification 是否足够？对 5,227 个 models 是否需要更细的分层？
   - ETS C 分类阈值（|ΔMH|≥1.5 + p<0.05）的选择是否合理？threshold sensitivity 是否充分？

2. **Confound Controls**：
   - Ability confounding: Cohen's d=-0.17 是否真的 negligible？matched-ability 分析是否充分？
   - Within-family comparison (Llama-2 vs 3, 61.3% → matched 28.3%) 的解释是否令人信服？
   - Model family structure 对 DIF 估计的影响是否充分控制？

3. **Semi-synthetic Framework**：
   - ΔFPR=0.000 的 bootstrap CI=[0.000, 0.000] 是否可信？代数证明是否严密？
   - Cross-subject matching 的假设和局限性
   - 注入实验的生态效度（ecological validity）

4. **实验设计与统计报告**：
   - 样本量是否充分（power analysis 声称 N≥80）？
   - 多重比较校正（BH FDR, 31.32%→31.30%）是否充分？
   - Bootstrap CI 的报告是否规范？
   - 所有 claims 是否有充分的统计支撑？

5. **格式合规**（辅助）：
   - 正文是否超过 8 页？
   - 是否存在匿名性泄露？
   - Limitations 章节是否存在且合理？

请按照 EMNLP/ARR 审稿标准，从 Soundness、Excitement、Reproducibility、Clarity 四个维度评分（1-5），并提供 Overall Assessment（1-5，0.5 步长）。

将问题分为 Must-Fix（接收前必须解决）和 Should-Fix（建议改进）两类。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-21T15:10:49.618380+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-21T15:10:50.523544+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-21T15:10:50.574246+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-21T15:10:50.675073+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-21T15:10:55.299785+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 133 · 2026-05-21T15:10:56.857930+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-21T15:10:57.312998+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-21T15:11:02.404075+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about ACL Rolling Review 2026 reviewer guidelines:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Overall Assessment Score Criteria

The Overall assessment score is an explicit recommendation for the outcome of this paper, and is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.

All papers recommen
…[truncated 778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7104
}
```

</details>

---


### Tool result

_source line 136 · 2026-05-21T15:11:03.860945+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 569.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.0}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"si
…[truncated 234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7003
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-21T15:17:39.501195+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 56, \"total_citations\": 70, \"unique_cited_keys\": 48, \"orphan_bib\": 8, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 38, \"online_not_found\": 7, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"chen2025irtnet\", \"choi2026llmjudgeirt\", \"li2025atlas\", \"liang2023helm\", \"mialon2023gaia\", \"ott2022benchmark\", \"wang2024mmlupro\", \"zhang2024gsm1k\"], \"missing_bib\": [], \"orphan_count\": 8, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"balloccu2024leak\", \"type\": \"inproceedings\", \"title\": \"Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs\", \"authors\": \"Balloccu, Simone and Schmidtova, Patrícia and Lango, Mateusz and Dusek, Ondrej\", \"year\": \"2024\", \"venue\": \"Proceedings of the 18th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"dekoninck2024constat\", \"type\": \"inproceedings\", \"title\": \"ConStat: Performance-Based Contamination Detection in Large Language Models\", \"authors\": \"Dekoninck, Jasper and Mueller, Mark Niklas and Vechev, Martin\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"golchin2024timetravel\", \"type\": \"inproceedings\", \"title\": \"Time Travel in LLMs: Tracing Data Contamination in Large Language Models\", \"authors\": \"Golchin, Shahriar and Surdeanu, Mihai\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"li2024contamination\", \"type\": \"inproceedings\", \"title\": \"An Open-Source Data Contamination Report for Large Language Models\", \"authors\": \"Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2024\"}, {\"key\": \"liang2026dvd\", \"type\": \"misc\", \"title\": \"D
…[truncated 43366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 402188
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-21T15:17:50.142465+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and the description for each score level. Focus on: Soundness, Excitement/Novelty, Overall Assessment, Reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and the description for each score level. Focus on: Soundness, Excitement/Novelty, Overall Assessment, Reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 139 · 2026-05-21T15:17:52.502242+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "11-13",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "11-13",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-21T15:17:53.456246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 141 · 2026-05-21T15:17:53.908437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-21T15:17:54.862589+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 143 · 2026-05-21T15:17:55.365211+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-21T15:17:55.666903+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-21T15:17:56.721475+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: "This study is one of the most thorough I have seen, given its type."
- **4**: Study provides sufficient support for claims; extra experiments optional.
- **3**: Main claims adequately supported; minor details need reinforcement.
- **2**: Major claims lack support; significant technical/methodological problems.
- **1**: "Not yet sufficiently thorough to warrant publication or is not relevant to ACL."

## 2. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: "I would recommend this paper to others and/or attend its presentation."
- **4**: Would mention paper to others; would prioritize attending presentation.
- **3**: Might discuss certain points; would attend if time permits.
- **2**: Paper doesn't resonate personally but may appeal to others.
- **1**: "does not resonate with me, and I don't think it would with others"

## 3. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings track acceptance
- **2**: Resubmit next cycle
- **1**: "Do not resubmit: This paper has to be fully redone"

## 4. **Reproducibility**
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations possible
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: Results cannot be reproduced

## 5. **Reviewer Confidence**
Scale: 1-5
- **5**: Confident evaluation is correct; very careful review
- **4**: Quite sure; unlikely major oversights
- **3**: Pretty sure; possible missed details
- **2**: Fairly likely to have missed important information
- **1**: "Not my area, or paper is very hard to understand"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6579
}
```

</details>

---


### Tool result

_source line 146 · 2026-05-21T15:17:57.175584+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 578.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.5}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 209.5}], \"total_pages\": 13, \"rendered_pages\": 3, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4673
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-21T15:17:57.176058+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3719
}
```

</details>

---


### Tool result

_source line 148 · 2026-05-21T15:17:57.176372+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3267
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-21T15:17:57.226830+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2364
}
```

</details>

---


### Tool result

_source line 150 · 2026-05-21T15:17:57.227166+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1861
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-21T15:17:57.227315+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1560
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-21T15:18:02.002903+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/",
  "description": "List PDF image files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/",
    "description": "List PDF image files"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-21T15:18:02.205297+00:00_

main_p11.png
main_p12.png
main_p13.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-21T15:18:06.875137+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-5",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-5",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-21T15:18:07.477845+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 569.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.3}], \"total_pages\": 13, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-21T15:18:11.398220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 157 · 2026-05-21T15:18:11.749629+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 158 · 2026-05-21T15:18:12.204580+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 159 · 2026-05-21T15:18:12.205069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 160 · 2026-05-21T15:18:13.165835+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1416
}
```

</details>

---


### Tool call

_source line 161 · 2026-05-21T15:18:13.166329+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 162 · 2026-05-21T15:18:13.369803+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1164
}
```

</details>

---


### Tool call

_source line 163 · 2026-05-21T15:18:13.370256+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 164 · 2026-05-21T15:18:14.435842+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1269
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-21T15:18:14.738829+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1368
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-21T15:18:19.461639+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "6-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "6-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-21T15:18:20.120251+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.0}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 601.4}], \"total_pages\": 13, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 658
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-21T15:18:23.987530+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-21T15:18:28.104075+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4116
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-21T15:18:28.355585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 171 · 2026-05-21T15:18:28.707429+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 172 · 2026-05-21T15:18:29.110289+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 173 · 2026-05-21T15:18:29.113988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-21T15:18:29.267893+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-21T15:18:30.124586+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1417
}
```

</details>

---


### Tool result

_source line 176 · 2026-05-21T15:18:30.677451+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1563
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-21T15:18:30.678297+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-21T15:18:35.246887+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 179 · 2026-05-21T15:18:35.804320+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-21T15:18:36.008900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-21T15:18:37.720277+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2473
}
```

</details>

---


### Tool result

_source line 182 · 2026-05-21T15:18:37.723762+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1714
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-21T15:18:37.926644+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2122
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-21T15:19:29.228491+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-21T15:19:29.279253+00:00_

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
21	\title{Psychometric Instability of LLM Benchmarks:\\Differential Item Functioning Reveals 31\% of MMLU Items\\Behave Differently Across Model Generations}
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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-21T15:19:33.042950+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-21T15:19:33.194001+00:00_

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
…[truncated 5959 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-21T15:19:33.194512+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-21T15:19:33.248527+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	A power analysis using empirical MMLU IRT parameters confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$. Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold.
10	
11	\subsection{Temporal Comparability: 31\% Item Instability}
12	\label{sec:temporal}
13	
14	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%], $N = 1{,}000$). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold on effect size and significance already provides implicit multiple-testing protection.
15	
16	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C items (sampling noise), and an ability-quintile comparison within the same temporal cohort yields 2.9\% (ability differences alone). A within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% ETS~C items, elevated by large ability gaps that confound the DIF signal~\citep{holland1988mh}. The contrast between 2.9\% (ability-controlled) and 61.3\% (ability-confounded) brackets the temporal rate of 31.3\%. Crucially, the temporal cohort ability gap is negligible: Cohen's $d = -0.17$ (below the $|d| = 0.2$ small-effect threshold) with 76.4\% distributional overlap. Under strict 1:1 nearest-
…[truncated 10426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 54
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-21T15:19:38.269035+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-21T15:19:38.771121+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Implications for Benchmark Temporal Comparability}
5	\label{sec:disc_temporal}
6	
7	The 31\% ETS~C instability extends across all six METABENCH benchmarks (C\% $= 17.9$--$31.3\%$, 45--174$\times$ above baselines; \Cref{tab:cross_benchmark}), with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). The Simpson's paradox (\Cref{sec:temporal}) confirms item properties, not accuracy gains, drive DIF. This does not invalidate ranking ($\rho \approx 0.997$) but signals measurement drift across model generations. The statistical machinery of DIF---originally designed for demographic fairness testing~\citep{holland1988mh}---transfers to temporal cohort comparisons unchanged, requiring only a binary response matrix and cohort labels.
8	
9	\subsection{Ground Truth Meta-Critique}
10	\label{sec:disc_groundtruth}
11	
12	The near-independence between DIF flags and web-overlap labels (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$) exposes a category error: web-overlap labels measure global exposure shared by nearly all MMLU items, so evaluating a differential method against them conflates two phenomena.
13	
14	\subsection{DIF as Diagnostic Lens}
15	\label{sec:disc_diagnostic}
16	
17	The GSM1K correlation ($r = -0.478$, partial $r = -0.385$; \Cref{sec:gsm8k}) provides exploratory evidence that DIF captures behavioral change distinct from memorization. DIF-C items are harder ($d = -0.247$) and more discriminating ($d = 0.230$), with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. Yen's Q3 confirms local dependence does not drive DIF ($r = 0.09$, $p = 0.50$).
18	
19	\subsection{Recommended DIF Audit Protocol}
20	\label{sec:disc_protocol}
21	
22	These findings motivate a benchmark maintenance protocol: (1)~MH-DIF audits whenever $\geq 500$ new models accumulate, using cross-subject matching; (2)~C\% $> 20\%$
…[truncated 266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-21T15:19:38.771588+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-21T15:19:39.374038+00:00_

1	\section*{Limitations}
2	
3	\paragraph{Methodological scope of MH-DIF.}
4	The Mantel-Haenszel procedure detects only \emph{uniform} DIF, where the odds ratio between cohorts is constant across ability strata. Logistic regression DIF analysis reveals an additional 24.8\% of items exhibiting non-uniform DIF ($|\beta_{\mathrm{interaction}}| \geq 0.5$), making the 31\% ETS~C estimate conservative. Future work should apply non-uniform DIF methods (e.g., logistic regression or IRT-based approaches) as the primary analysis to capture the full spectrum of item instability. Critically, MH-DIF is nonparametric and conditions on observed total score, not latent $\theta$---its validity does not depend on IRT model fit~\citep{holland1988mh}. Our Yen's Q3 analysis confirms that local dependence domains do not correlate with DIF domains ($r = 0.09$, $p = 0.50$), further supporting the robustness of the MH procedure in this setting.
5	
6	\paragraph{Ability confounding.}
7	Although the temporal cohort ability gap is negligible (Cohen's $d = -0.17$, overlap $= 76.4\%$) and nearest-neighbor matching confirms that at most 2.4 percentage points of C\% are attributable to ability mismatch, within-family comparisons with large ability gaps (e.g., Llama-2 vs.\ Llama-3, $d = -0.99$) produce substantially inflated C\% (61.3\% unmatched vs.\ 28.3\% matched). Any application of MH-DIF to cohorts with larger ability differences must incorporate ability matching or stratification beyond the standard 5-strata procedure.
8	
9	\paragraph{Sample size requirements.}
10	Our power analysis indicates reliable ETS~C detection requires $N \geq 80$ per cohort. The temporal cohorts (1,080 and 807 models) far exceed this threshold, but the GSM1K correlation analysis ($N = 33$) has limited statistical power (95\% CI $= [-0.71, -0.16]$). The negative correlation between contamination gap and DIF ranking advantage ($r = -0.478$) is exploratory and warrants replication with larger model samples.
11	
12	\paragr
…[truncated 1543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-21T15:19:39.374437+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-21T15:19:39.425002+00:00_

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
…[truncated 5576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-21T15:19:45.498243+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-21T15:19:45.950370+00:00_

1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet the assumption that individual items measure the same construct over time is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (DIF) analysis with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 total items), and find that 17.9--31.3\% of items exhibit large DIF (ETS Category~C; MMLU 95\% bootstrap CI: [29.4\%, 38.1\%]) between 2023 and 2024 model cohorts---knowledge/reasoning benchmarks show higher instability (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$), each 45--174$\times$ above random baselines. This does not threaten benchmark validity ($\rho \approx 0.997$ between full and stable-item rankings) but reveals which capability dimensions shift across generations. Item-level decomposition shows 92.4\% of instability is item-specific; a Simpson's paradox in odds ratio regression confirms item properties, not accuracy gains, drive DIF. We expose a validation methodology gap: web-overlap labels measure global exposure, not differential functioning (enrichment $\approx 0.96$). A semi-synthetic injection framework with cross-subject matching preserves detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$) with zero false positive inflation. DIF-flagged items concentrate cross-generational discriminative information ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal), and a difficulty--direction interaction ($\rho = -0.597$) reveals that capability gains concentrate on hard items while easy items erode, suggesting DIF captures temporal construct shift rather than noise. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-21T15:19:46.000975+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-21T15:19:46.503348+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. The instability persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of this instability is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{liang2026d
…[truncated 5577 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-21T15:19:46.503877+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-21T15:19:46.554342+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	MH-DIF analysis of six METABENCH benchmarks (27,125 items, 5,227 models) reveals 17.9--31.3\% temporal item instability (ETS~C); a Simpson's paradox confirms item properties, not accuracy gains, drive DIF. Web-overlap labels are near-independent of DIF flags (enrichment $\approx 0.96$); our semi-synthetic framework validates detection power ($\Delta\mathrm{FPR} = 0.000$). DIF-flagged items concentrate discriminative information ($z{=}{-}8\sigma$ to ${-}49\sigma$) with a difficulty--direction interaction ($\rho{=}{-}0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring alongside score reporting.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-21T15:21:10.628142+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-21T15:21:10.678802+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-21T15:22:58.874531+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿意见（方法严谨性 + 实验设计）\n\n---\n\n## 总体评分\n**Overall**: 3.5 / 5（Borderline Conference）\n**一句话总结**: 将教育测量中成熟的 MH-DIF 方法大规模应用于 LLM benchmark 是有新意的实证贡献，但半合成验证框架的生态效度存在根本性缺陷，且核心发现（31% instability）的因果解释力不足——论文未能令人信服地区分\"psychometric instability\"与\"expected capability evolution\"。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | MH-DIF 的应用本身合理，多重控制实验充分，但 Proposition 1 是 trivially true by construction，semi-synthetic 框架仅验证 subject-localized contamination 这一特殊情形；ability confounding 的控制虽有说服力（matched C%≈28-29%），但 Q3 局部依赖对主分析的影响未量化 |\n| Excitement | 3.5 / 5 | 跨学科应用（psychometrics → NLP evaluation）有新意，6 个 benchmark 的大规模验证具说服力，ground truth meta-critique（Claim 2）对 contamination detection 文献有实际启示；但核心 DIF 数字更多是描述性发现而非可操作的方法论突破 |\n| Reproducibility | 4 / 5 | 使用公开 METABENCH 数据，提供匿名代码链接，方法描述详尽（K=5 分层、ETS 分类标准、bootstrap 参数均有报告）；power analysis 的假设参数可更透明 |\n| Clarity | 4 / 5 | 写作清晰，结构合理，Figure 1 对 global vs. differential contamination 的区分直观有效；但 Abstract 过于密集（信息量堆叠），Limitations 涵盖较全面 |\n\n**Reviewer Confidence**: 4 / 5（熟悉 DIF 方法论和 LLM evaluation 文献，仔细通读全文及附录）\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 半合成验证框架的生态效度（Ecological Validity）存在根本缺陷\n- 具体位置：Section 3.4, Proposition 1 (p.5), Section 4.5 (p.7)\n- 问题：Proposition 1 声称 cross-subject matching 实现 ΔFPR=0.000，但这是 **by construction** 的平凡结果——contamination 被注入 subject X 的 items，matching variable 排除了 subject X，因此注入信号在数学上无法泄漏到 matching variable 中。论文将此作为 Claim 3 的核心贡献呈现，但实际上它只验证了**单一 subject 被污染**的特殊情形。在现实场景中，LLM 训练语料包含所有 MMLU subjects 的 items，contamination 会**同时跨越多个 subjects** 发生。此时 cross-subject matching variable 本身也被污染，Proposition 1 的保证不再成立。论文未测试 multi-subject simultaneous injection（例如同时污染 3-5 个 subjects 后看 FPR 是否仍为 0），因此无法评估框架在现实条件下的有效性。\n- 为什么影响接收：Semi-synthetic 框架是论文验证 31.3% temporal C% 非假阳性的核心证据之一（Section 4.3 用 dose-response 论证 detection power）。如果框架仅在 unrealistic 条件下有效，则论文缺乏充分的 false positive rate 控制，31.3% 的可信度下降。\n- 建议修改方向：(1) 补充 multi-subject simultaneous injection 实验（例如随机选择 k∈{2,3,5,10} 个 subjects 同时注入，报告 ΔFPR 随 k 的变化）；(2) 或将 Claim 3 显式限定为 subject-localized contamination 场景，并讨论对 temporal DIF 解读的影响。\n\n**N2** [critical] 核心发现的因果模糊性：「Psychometric Instability」vs.「Expected Capability Evolution」\n- 具体位置：Title, Abstract, Section 4.2 (p.6), Section 5.3 (p.8)\n- 问题：论文发现 DIF 呈现系统性的 difficulty-direction interaction（ρ=-0.597, Section 5.3）：2024 模型在难题上 gain、简单题上 erode。论文将此解读为\"temporal construct shift\"的证据，但这个 pattern 同样（甚至更自然地）可以解释为**正常的 capability evolution**——新一代模型推理能力提升导致难题表现改善，而 training distribution 变化导致简单 factual recall 题表现下降。MH-DIF 在设计上会将**任何**跨组 item functioning 差异标记为 DIF，包括 genuine capability change。论文标题使用\"Psychometric Instability\"暗示这是一个 benchmark 的测量问题，但如果 31% 的 DIF 主要反映模型能力的合理演变，则这不是\"instability\"而是\"expected differential performance\"。论文在 Limitations 中承认\"DIF detects that... not why\"，但 framing 从标题到结论均倾向于\"instability\"的负面解读。\n- 为什么影响接收：论文的主要 narrative（\"LLM benchmarks need psychometric monitoring\"）依赖于将 DIF 解读为测量问题而非能力变化。如果 DIF 主要捕获的是 expected capability evolution，则 policy implication 需要根本性修改。\n- 建议修改方向：(1) 明确区分 \"item instability\"（item 本身测量属性变化）和 \"differential performance\"（模型能力变化导致的 item 行为差异）；(2) 通过分析 DIF 方向与 item content 特征（如 knowledge domain recency, reasoning depth）的关系，提供更强的证据来区分这两种解释；(3) 至少软化标题中 \"Instability\" 的表述，改为更中性的 \"Differential Functioning\" 或 \"Measurement Drift\"。\n\n**N3** [critical] Bootstrap CI 的不对称性与 headline 数字的精确度\n- 具体位置：Section 4.2 (p.6), Abstract\n- 问题：MMLU C% 的 95% bootstrap CI 为 [29.4%, 38.1%]，宽度 8.7pp，上尾明显偏重（31.3% → 38.1% 的距离是到下界的 3.6 倍）。论文以 \"31%\" 作为标题和全文 headline 数字，但 CI 表明真实值可能高达 38%。更重要的是：论文未报告 bootstrap 的 resampling unit（是 resample models 还是 items？），这影响 CI 的解读。如果 resample models，CI 反映 model sampling variability，说明结论对 model population 的代表性有不确定性；如果 resample items，CI 反映 item sampling variability。此外，CI 的不对称性暗示 C% 分布是 right-skewed 的，论文应解释原因。\n- 为什么影响接收：Headline 数字 \"31%\" 是论文所有下游分析和 policy recommendations 的基础。如果 CI 表明结果对 model/item 抽样高度敏感，需要更谨慎的表述。\n- 建议修改方向：(1) 明确报告 bootstrap resampling unit 和策略（model-level vs. item-level vs. block bootstrap）；(2) 在 Abstract 和 Title 中使用 CI 或至少用 \"approximately 31%\" 表述；(3) 解释 CI 不对称性的来源。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] K=5 分层的敏感性分析不足\n- 具体位置：Section 3.2 (p.4)\n- 问题：论文选择 K=5 quintile stratification，引用 ETS recommended practice（Donoghue 1993, Clauser 1998）。这些推荐针对的是 human test-takers（通常 N=几百到几千），而本文 N=5,227 models 远超典型教育测评场景。论文在 Appendix B 报告了 IRT θ-conditioning with 20 strata（FPR=0.312，与 K=5 几乎相同），这部分回应了 K 的选择问题。但论文应在主文中明确报告 K=5 vs. K=10 vs. K=20 的 C% 对比，而非仅在附录中隐式提及。\n- 建议：在 Section 4.2 或 Table 1 中增加一行 K 的 sensitivity analysis。\n\n**W2** [warning] Yen's Q3 局部依赖对主分析的影响未量化\n- 具体位置：Appendix A.1 (p.11), Appendix B (p.12)\n- 问题：11.3% 的 within-subject item pairs 超过 |Q3|>0.20 阈值（vs. cross-subject 2.2%，5× ratio，p=2.3×10⁻⁹）。MH 程序假设 conditional independence given matching variable。虽然主分析使用 total score（across all 12,508 items）作为 matching variable，subject-specific dependence 的影响被稀释，但论文未提供定量估计——例如通过 simulation 评估 11.3% Q3 violation rate 对 C% 的 expected inflation。\n- 建议：补充一个 permutation-based 或 simulation-based 的分析，量化 Q3 violation 对 Type I error rate 的影响。\n\n**W3** [warning] Within-family 分析（Llama-2 vs. 3）的 residual 28.3% 解读不充分\n- 具体位置：Section 4.4 (p.7)\n- 问题：Llama-2 vs. 3 unmatched C%=61.3%，matched C%=28.3%±1.6%。论文将 matched 后的 28.3% 解读为\"genuine item-level DIF\"，并指出它与 temporal matched C%≈28.9% 的一致性很有说服力。但 within-family 比较中，即使 ability matched 后，Llama-2 和 Llama-3 之间仍存在大量非 ability 差异：不同的 training data、tokenizer、RLHF procedure、architecture refinements。这些 confounds 都可能驱动 DIF。两个不同比较的 matched C% 趋同（~28-29%）可能是巧合，也可能反映了 MH-DIF 在 K=5 下的某种 floor effect。\n- 建议：讨论 matched C% 趋同的替代解释（如 K=5 分层下的分辨率限制），或在更多 within-family pairs 上验证。\n\n**W4** [warning] GSM1K 分析的统计效力不足以支撑 Claim 4\n- 具体位置：Section 4.7 (p.7-8), Section 5.3 (p.8)\n- 问题：GSM1K correlation r=-0.478 基于 N=33 models，95% CI=[-0.71, -0.16]。论文在 Limitations 中承认这是 exploratory，但 Discussion Section 5.3 仍将其作为\"DIF captures behavioral change distinct from memorization\"的主要证据。N=33 的相关分析受单个异常值影响很大，且 CI 跨越了 moderate-to-strong 的范围。\n- 建议：将此分析明确标记为 preliminary/exploratory，不在 Discussion 中作为 Claim 4 的主要支撑；或在更大样本上验证。\n\n**W5** [warning] Power analysis 假设不透明\n- 具体位置：Section 4.1 (p.5)\n- 问题：论文声称\"A power analysis using empirical MMLU IRT parameters confirms that at N≥80 per cohort, ETS C achieves TPR of 0.68-0.80\"，但未报告 IRT 参数的具体值、assumed effect size、simulation procedure。读者无法评估 power analysis 的合理性。\n- 建议：在 Appendix 中补充 power analysis 的完整设定（IRT 参数分布、injection effect sizes、simulation repeats）。\n\n**W6** [warning] Ground truth meta-critique (Claim 2) 的逻辑可逆\n- 具体位置：Section 4.3 (p.6-7), Section 5.2 (p.8)\n- 问题：论文发现 DIF flags 与 web-overlap labels 近乎独立（enrichment=0.964, Jaccard=0.206），解读为\"web-overlap labels 是 wrong ground truth for differential methods\"。但近乎独立同样可以解读为\"MH-DIF 检测的不是 contamination\"——两种解读逻辑上等价。论文用 semi-synthetic injection 证明 MH-DIF *can* detect differential contamination，但 semi-synthetic 条件（N1 指出的 subject-localized injection）与 real-world contamination 差距很大。因此 Claim 2 的说服力受限于 semi-synthetic 框架的生态效度。\n- 建议：在 Discussion 中明确承认双向解读的可能性，而非单向指责 web-overlap labels。\n\n---\n\n## 小问题（不影响接收）\n\n- **Abstract 过度密集**：Abstract 包含了 ρ≈0.997、z=-8σ to -49σ、ρ=-0.597 等大量数字，读起来像 executive summary 而非 abstract。建议精简到 3-4 个核心数字。\n- **引用验证**：verify_references 检查发现 8 个 orphan bib entries（在 .bib 中但未被引用），包括 zhang2024gsm1k、wang2024mmlupro 等。另有 liang2026dvd 等少量条目在 OpenAlex 中未找到（可能是 preprint），holland1988mh 的年份存在 bib=1988 vs API=1986 的不一致。这些都是小问题。\n- **Limitations 长度**：按 EMNLP 2026 规则，Limitations 不计入页数但不应包含过多额外内容。当前 Limitations 约 6 段，内容充实但可略微精简。\n- **Table 1 FPR 列**：Within-family 和 Random split 行的 FPR 标记为 \"--\"，应注明为何不适用。\n- **Footnote 1 匿名链接**：anonymous.4open.science 链接合规，但提交时需确认链接可访问。\n\n---\n\n## 主要优势\n\n1. **大规模实证贡献**：5,227 models × 27,125 items 的 DIF 分析规模远超此前工作，6 个 benchmark 的交叉验证提供了强有力的 replication。\n2. **严谨的 confound 控制**：5 种 cohort design（temporal, ability-quintile, within-family, within-subject, random-split）系统排除替代解释，matched-ability 分析令人信服地将 ability confounding 限定在 ~2.4pp。\n3. **Ground truth meta-critique 有实际价值**：Claim 2 对 contamination detection 文献中普遍使用 web-overlap labels 作为 ground truth 的做法提出了合理质疑，有望推动更细致的 evaluation methodology。\n4. **写作质量高**：Figure 1 直观有效，方法描述清晰，threshold sensitivity 分析（C% at |Δ|∈{1.0, 1.5, 2.0, 2.5}）展示了结论的鲁棒性。\n5. **跨学科创新**：将 60+ 年历史的 psychometric DIF 方法引入 NLP evaluation 是有价值的 cross-pollination，audit protocol（Section 5.4）具有实践意义。\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 备注 |\n|------|------|------|\n| 正文页数 | ✅ 合规 | 8 页（含 Conclusion + Limitations），未超限 |\n| 匿名性 | ✅ 合规 | \"Anonymous ACL submission\"，代码用 anonymous.4open.science |\n| 模板 | ✅ 合规 | `\\usepackage[review]{acl}` |\n| Limitations | ✅ 存在 | 6 段，覆盖方法论、混淆变量、样本量、因果归因、benchmark 范围、时间定义 |\n| 参考文献 | ⚠️ 小问题 | 8 个 orphan entries，少量年份不一致（见上） |",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿意见（方法严谨性 + 实验设计）\n\n---\n\n## 总体评分\n**Overall**: 3.5 / 5（Borderline Conference）\n**一句话总结**: 将教育测量中成熟的 MH-DIF 方法大规模应用于 LLM benchmark 是有新意的实证贡献，但半合成验证框架的生态效度存在根本性缺陷，且核心发现（31% instability）的因果解释力不足——论文未能令人信服地区分\"psychometric instability\"与\"expected capability evolution\"。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | MH-DIF 的应用本身合理，多重控制实验充分，但 Proposition 1 是 trivially true by construction，semi-synthetic 框架仅验证 subject-localized contamination 这一特殊情形；ability confounding 的控制虽有说服力（matched C%≈28-29%），但 Q3 局部依赖对主分析的影响未量化 |\n| Excitement | 3.5 / 5 | 跨学科应用（psychometrics → NLP evaluation）有新意，6 个 benchmark 的大规模验证具说服力，ground truth meta-critique（Claim 2）对 contamination detection 文献有实际启示；但核心 DIF 数字更多是描述性发现而非可操作的方法论突破 |\n| Reproducibility | 4 / 5 | 使用公开 METABENCH 数据，提供匿名代码链接，方法描述详尽（K=5 分层、ETS 分类标准、bootstrap 参数均有报告）；power analysis 的假设参数可更透明 |\n| Clarity | 4 / 5 | 写作清晰，结构合理，Figure 1 对 global vs. differential contamination 的区分直观有效；但 Abstract 过于密集（信息量堆叠），Limitations 涵盖较全面 |\n\n**Reviewer Confidence**: 4 / 5（熟悉 DIF 方法论和 LLM evaluation 文献，仔细通读全文及附录）\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 半合成验证框架的生态效度（Ecological Validity）存在根本缺陷\n- 具体位置：Section 3.4, Proposition 1 (p.5), Section 4.5 (p.7)\n- 问题：Proposition 1 声称 cross-subject matching 实现 ΔFPR=0.000，但这是 **by construction** 的平凡结果——contamination 被注入 subject X 的 items，matching variable 排除了 subject X，因此注入信号在数学上无法泄漏到 matching variable 中。论文将此作为 Claim 3 的核心贡献呈现，但实际上它只验证了**单一 subject 被污染**的特殊情形。在现实场景中，LLM 训练语料包含所有 MMLU subjects 的 items，contamination 会**同时跨越多个 subjects** 发生。此时 cross-subject matching variable 本身也被污染，Proposition 1 的保证不再成立。论文未测试 multi-subject simultaneous injection（例如同时污染 3-5 个 subjects 后看 FPR 是否仍为 0），因此无法评估框架在现实条件下的有效性。\n- 为什么影响接收：Semi-synthetic 框架是论文验证 31.3% temporal C% 非假阳性的核心证据之一（Section 4.3 用 dose-response 论证 detection power）。如果框架仅在 unrealistic 条件下有效，则论文缺乏充分的 false positive rate 控制，31.3% 的可信度下降。\n- 建议修改方向：(1) 补充 multi-subject simultaneous injection 实验（例如随机选择 k∈{2,3,5,10} 个 subjects 同时注入，报告 ΔFPR 随 k 的变化）；(2) 或将 Claim 3 显式限定为 subject-localized contamination 场景，并讨论对 temporal DIF 解读的影响。\n\n**N2** [critical] 核心发现的因果模糊性：「Psychometric Instability」vs.「Expected Capability Evolution」\n- 具体位置：Title, Abstract, Section 4.2 (p.6), Section 5.3 (p.8)\n- 问题：论文发现 DIF 呈现系统性的 difficulty-direction interaction（ρ=-0.597, Section 5.3）：2024 模型在难题上 gain、简单题上 erode。论文将此解读为\"temporal construct shift\"的证据，但这个 pattern 同样（甚至更自然地）可以解释为**正常的 capability evolution**——新一代模型推理能力提升导致难题表现改善，而 training distribution 变化导致简单 factual recall 题表现下降。MH-DIF 在设计上会将**任何**跨组 item functioning 差异标记为 DIF，包括 genuine capability change。论文标题使用\"Psychometric Instability\"暗示这是一个 benchmark 的测量问题，但如果 31% 的 DIF 主要反映模型能力的合理演变，则这不是\"instability\"而是\"expected differential performance\"。论文在 Limitations 中承认\"DIF detects that... not why\"，但 framing 从标题到结论均倾向于\"instability\"的负面解读。\n- 为什么影响接收：论文的主要 narrative（\"LLM benchmarks need psychometric monitoring\"）依赖于将 DIF 解读为测量问题而非能力变化。如果 DIF 主要捕获的是 expected capability evolution，则 policy implication 需要根本性修改。\n- 建议修改方向：(1) 明确区分 \"item instability\"（item 本身测量属性变化）和 \"differential performance\"（模型能力变化导致的 item 行为差异）；(2) 通过分析 DIF 方向与 item content 特征（如 knowledge domain recency, reasoning depth）的关系，提供更强的证据来区分这两种解释；(3) 至少软化标题中 \"Instability\" 的表述，改为更中性的 \"Differential Functioning\" 或 \"Measurement Drift\"。\n\n**N3** [critical] Bootstrap CI 的不对称性与 headline 数字的精确度\n- 具体位置：Section 4.2 (p.6), Abstract\n- 问题：MMLU C% 的 95% bootstrap CI 为 [29.4%, 38.1%]，宽度 8.7pp，上尾明显偏重（31.3% → 38.1% 的距离是到下界的 3.6 倍）。论文以 \"31%\" 作为标题和全文 headline 数字，但 CI 表明真实值可能高达 38%。更重要的是：论文未报告 bootstrap 的 resampling unit（是 resample models 还是 items？），这影响 CI 的解读。如果 resample models，CI 反映 model sampling variability，说明结论对 model population 的代表性有不确定性；如果 resample items，CI 反映 item sampling variability。此外，CI 的不对称性暗示 C% 分布是 right-skewed 的，论文应解释原因。\n- 为什么影响接收：Headline 数字 \"31%\" 是论文所有下游分析和 policy recommendations 的基础。如果 CI 表明结果对 model/item 抽样高度敏感，需要更谨慎的表述。\n- 建议修改方向：(1) 明确报告 bootstrap resampling unit 和策略（model-level vs. item-level vs. block bootstrap）；(2) 在 Abstract 和 Title 中使用 CI 或至少用 \"approximately 31%\" 表述；(3) 解释 CI 不对称性的来源。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] K=5 分层的敏感性分析不足\n- 具体位置：Section 3.2 (p.4)\n- 问题：论文选择 K=5 quintile stratification，引用 ETS recommended practice（Donoghue 1993, Clauser 1998）。这些推荐针对的是 human test-takers（通常 N=几百到几千），而本文 N=5,227 models 远超典型教育测评场景。论文在 Appendix B 报告了 IRT θ-conditioning with 20 strata（FPR=0.312，与 K=5 几乎相同），这部分回应了 K 的选择问题。但论文应在主文中明确报告 K=5 vs. K=10 vs. K=20 的 C% 对比，而非仅在附录中隐式提及。\n- 建议：在 Section 4.2 或 Table 1 中增加一行 K 的 sensitivity analysis。\n\n**W2** [warning] Yen's Q3 局部依赖对主分析的影响未量化\n- 具体位置：Appendix A.1 (p.11), Appendix B (p.12)\n- 问题：11.3% 的 within-subject item pairs 超过 |Q3|>0.20 阈值（vs. cross-subject 2.2%，5× ratio，p=2.3×10⁻⁹）。MH 程序假设 conditional independence given matching variable。虽然主分析使用 total score（across all 12,508 items）作为 matching variable，subject-specific dependence 的影响被稀释，但论文未提供定量估计——例如通过 simulation 评估 11.3% Q3 violation rate 对 C% 的 expected inflation。\n- 建议：补充一个 permutation-based 或 simulation-based 的分析，量化 Q3 violation 对 Type I error rate 的影响。\n\n**W3** [warning] Within-family 分析（Llama-2 vs. 3）的 residual 28.3% 解读不充分\n- 具体位置：Section 4.4 (p.7)\n- 问题：Llama-2 vs. 3 unmatched C%=61.3%，matched C%=28.3%±1.6%。论文将 matched 后的 28.3% 解读为\"genuine item-level DIF\"，并指出它与 temporal matched C%≈28.9% 的一致性很有说服力。但 within-family 比较中，即使 ability matched 后，Llama-2 和 Llama-3 之间仍存在大量非 ability 差异：不同的 training data、tokenizer、RLHF procedure、architecture refinements。这些 confounds 都可能驱动 DIF。两个不同比较的 matched C% 趋同（~28-29%）可能是巧合，也可能反映了 MH-DIF 在 K=5 下的某种 floor effect。\n- 建议：讨论 matched C% 趋同的替代解释（如 K=5 分层下的分辨率限制），或在更多 within-family pairs 上验证。\n\n**W4** [warning] GSM1K 分析的统计效力不足以支撑 Claim 4\n- 具体位置：Section 4.7 (p.7-8), Section 5.3 (p.8)\n- 问题：GSM1K correlation r=-0.478 基于 N=33 models，95% CI=[-0.71, -0.16]。论文在 Limitations 中承认这是 exploratory，但 Discussion Section 5.3 仍将其作为\"DIF captures behavioral change distinct from memorization\"的主要证据。N=33 的相关分析受单个异常值影响很大，且 CI 跨越了 moderate-to-strong 的范围。\n- 建议：将此分析明确标记为 preliminary/exploratory，不在 Discussion 中作为 Claim 4 的主要支撑；或在更大样本上验证。\n\n**W5** [warning] Power analysis 假设不透明\n- 具体位置：Section 4.1 (p.5)\n- 问题：论文声称\"A power analysis using empirical MMLU IRT parameters confirms that at N≥80 per cohort, ETS C achieves TPR of 0.68-0.80\"，但未报告 IRT 参数的具体值、assumed effect size、simulation procedure。读者无法评估 power analysis 的合理性。\n- 建议：在 Appendix 中补充 power analysis 的完整设定（IRT 参数分布、injection effect sizes、simulation repeats）。\n\n**W6** [warning] Ground truth meta-critique (Claim 2) 的逻辑可逆\n- 具体位置：Section 4.3 (p.6-7), Section 5.2 (p.8)\n- 问题：论文发现 DIF flags 与 web-overlap labels 近乎独立（enrichment=0.964, Jaccard=0.206），解读为\"web-overlap labels 是 wrong ground truth for differential methods\"。但近乎独立同样可以解读为\"MH-DIF 检测的不是 contamination\"——两种解读逻辑上等价。论文用 semi-synthetic injection 证明 MH-DIF *can* detect differential contamination，但 semi-synthetic 条件（N1 指出的 subject-localized injection）与 real-world contamination 差距很大。因此 Claim 2 的说服力受限于 semi-synthetic 框架的生态效度。\n- 建议：在 Discussion 中明确承认双向解读的可能性，而非单向指责 web-overlap labels。\n\n---\n\n## 小问题（不影响接收）\n\n- **Abstract 过度密集**：Abstract 包含了 ρ≈0.997、z=-8σ to -49σ、ρ=-0.597 等大量数字，读起来像 executive summary 而非 abstract。建议精简到 3-4 个核心数字。\n- **引用验证**：verify_references 检查发现 8 个 orphan bib entries（在 .bib 中但未被引用），包括 zhang2024gsm1k、wang2024mmlupro 等。另有 liang2026dvd 等少量条目在 OpenAlex 中未找到（可能是 preprint），holland1988mh 的年份存在 bib=1988 vs API=1986 的不一致。这些都是小问题。\n- **Limitations 长度**：按 EMNLP 2026 规则，Limitations 不计入页数但不应包含过多额外内容。当前 Limitations 约 6 段，内容充实但可略微精简。\n- **Table 1 FPR 列**：Within-family 和 Random split 行的 FPR 标记为 \"--\"，应注明为何不适用。\n- **Footnote 1 匿名链接**：anonymous.4open.science 链接合规，但提交时需确认链接可访问。\n\n---\n\n## 主要优势\n\n1. **大规模实证贡献**：5,227 models × 27,125 items 的 DIF 分析规模远超此前工作，6 个 benchmark 的交叉验证提供了强有力的 replication。\n2. **严谨的 confound 控制**：5 种 cohort design（temporal, ability-quintile, within-family, within-subject, random-split）系统排除替代解释，matched-ability 分析令人信服地将 ability confounding 限定在 ~2.4pp。\n3. **Ground truth meta-critique 有实际价值**：Claim 2 对 contamination detection 文献中普遍使用 web-overlap labels 作为 ground truth 的做法提出了合理质疑，有望推动更细致的 evaluation methodology。\n4. **写作质量高**：Figure 1 直观有效，方法描述清晰，threshold sensitivity 分析（C% at |Δ|∈{1.0, 1.5, 2.0, 2.5}）展示了结论的鲁棒性。\n5. **跨学科创新**：将 60+ 年历史的 psychometric DIF 方法引入 NLP evaluation 是有价值的 cross-pollination，audit protocol（Section 5.4）具有实践意义。\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 备注 |\n|------|------|------|\n| 正文页数 | ✅ 合规 | 8 页（含 Conclusion + Limitations），未超限 |\n| 匿名性 | ✅ 合规 | \"Anonymous ACL submission\"，代码用 anonymous.4open.science |\n| 模板 | ✅ 合规 | `\\usepackage[review]{acl}` |\n| Limitations | ✅ 存在 | 6 段，覆盖方法论、混淆变量、样本量、因果归因、benchmark 范围、时间定义 |\n| 参考文献 | ⚠️ 小问题 | 8 个 orphan entries，少量年份不一致（见上） |",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-21T15:23:02.739874+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3865
}
```

</details>

---


### Assistant

_source line 206 · 2026-05-21T15:23:12.032627+00:00_

审稿意见已提交给 Review Director。

**摘要**：Overall 3.5/5（Borderline Conference）。论文将 MH-DIF 大规模应用于 LLM benchmark 是有价值的跨学科贡献，5 种 cohort design 的 confound 控制较为系统。但存在 3 个 Must-Fix 问题：
1. 半合成验证框架仅验证 subject-localized contamination（Proposition 1 的 ΔFPR=0 是 trivially true by construction），未测试 multi-subject simultaneous injection
2. 核心 "31% instability" 未能区分 psychometric instability 与 expected capability evolution（difficulty-direction interaction ρ=-0.597 同样支持后者）
3. Bootstrap CI [29.4%, 38.1%] 的不对称性和 resampling 策略未充分报告

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 8

## Round 8

4 recorded events


### User

_source line 207 · 2026-05-21T15:24:02.944489+00:00_

[Round 1 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的意见

以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 2 完整审稿意见

**Overall**: 3.5 — Borderline Conference
**Soundness**: 4/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Clarity**: 4/5

### Must-Fix

**R2-N1** [critical] Claim 4 "DIF as diagnostic lens" 支撑不足
- Section 4.6, 5.3。GSM1K correlation (r=-0.478, partial r=-0.385, N=33) 样本太小，CI 上界 ≈-0.16。论文以此支撑 "DIF captures behavioral change distinct from memorization"，但 N=33 不够。如果 Claim 4 站不住，4 个 contribution 中有 1 个打折扣。
- 建议：补充更强证据，或降级 Claim 4 为 observation 而非 contribution。

**R2-N2** [critical] 方法论新颖性论证不充分
- MH-DIF 是 1988 年方法，cross-subject matching 有先例（Nandakumar 1993, Donoghue 1993——论文自己承认）。4 个 claims 中 3 个是 descriptive findings。论文需要更清晰地论证 transplant 解决了什么 LLM-specific 新问题。
- 建议：argue "为什么 DIF 不能直接搬过来"（LLM 作为 examinees 的特殊性），或明确 position 为 empirical contribution。

**R2-N3** [critical] Temporal cohort 定义过于粗糙
- Calendar year 划分混淆了 architecture shift、training methodology shift、temporal effect。虽有 5 种 cohort design，但主要结果仍基于 calendar year。Within-year cohort（如 2024-H1 vs H2）完整结果只在 Appendix 简单提及。
- 建议：补充 within-year 完整结果；改 framing 为 "cross-cohort DIF" 而非 "temporal comparability"。

### Should-Fix

**R2-W1** ρ≈0.997 vs 31.3% 张力——Section 5.4 "DIF Audit Protocol" 只有 3 句话，actionability 不足。
**R2-W2** ΔFPR=0.000 过于完美——注入率固定 20%，只在 5 个 subjects 验证，未讨论 Type II error。
**R2-W3** DIF 术语对 EMNLP 读者不够友好——缺少 running example。
**R2-W4** 与 Growing Pains 的区分过于简短——未验证 DIF-flagged items 与 FPC anchor items 的 overlap。
**R2-W5** 引用问题：holland1988mh year mismatch、tao2026selfcritique/liu2026bhi author mismatch、8 orphan bib entries。

### Missing References
1. "Lifting the Benchmark Iceberg with IRT" (2025)
2. Benchmark2 (arXiv:2601.03986, 2025)
3. ATLAS / CAT-based LLM evaluation (Li et al. 2025, 已在 bib 未引用)
4. MedIRT (arXiv:2509.24186, 2025)

### 主要优势
1. 规模和严谨性（5,227 models × 12,508 items，5 种 cohort design + 3 层控制）
2. 发现的实际价值（31% instability + 6 benchmarks 复现）
3. Ground truth meta-critique 对 contamination detection 文献有价值
4. Semi-synthetic framework 在 LLM 场景有价值
5. 叙事处理得当（diagnostic lens framing）

---

请对 R2 的每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。特别关注：
1. R2-N1 关于 Claim 4 的批评是否与你的 W4 (GSM1K N=33) 一致？
2. R2-N2 关于 novelty 的批评——你作为方法论 reviewer 如何看待？
3. R2-N3 关于 temporal cohort 的批评与你的 N2 (因果模糊性) 有何关联？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-21T15:25:34.310209+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 — 对 Reviewer 2 Round 1 意见\n\n---\n\n### Must-Fix 回应\n\n**[AGREE] R2-N1: Claim 4 \"DIF as diagnostic lens\" 支撑不足**\n\n与我的 W4 完全一致。GSM1K N=33 的相关分析（r=-0.478, CI=[-0.71, -0.16]）统计效力严重不足，单个异常模型即可显著改变结论。论文在 Limitations 中承认这是 exploratory，但 Discussion Section 5.3 和 Introduction Claim 4 的措辞并未匹配这一谨慎程度——\"DIF captures behavioral change distinct from memorization\" 作为 contribution 陈述过强。\n\n补充一点 R2 未提及的：Claim 4 的另一支撑——difficulty-direction interaction（ρ=-0.597）——本身解读也有歧义（见我的 N2）。gains on hard items + erosion on easy ones 同样可解释为 expected capability evolution 而非 diagnostic signal。因此 Claim 4 的两条证据链都有弱点。\n\n**建议**：同意 R2——降级为 exploratory observation 或 supplementary analysis，从 4 个 contributions 中移除。\n\n---\n\n**[REBUT] R2-N2: 方法论新颖性论证不充分**\n\nR2 的批评方向合理但严厉程度偏重，理由如下：\n\n1. **论文已 explicitly 定位为 empirical contribution**：Introduction 第 19 行明确写道 \"Our contributions are empirical and methodological, not algorithmic\"。论文从未声称 MH-DIF 或 cross-subject matching 是新方法——它声称的是将已有方法**大规模应用于 LLM evaluation 这个新 domain** 并产生了 non-trivial empirical findings。\n\n2. **Transplant 并非 trivial**：虽然 MH-DIF 是 1988 年的方法，但将其应用于 LLM benchmarks 涉及多个 LLM-specific 的适配决策——(a) LLMs 作为 examinees 不满足传统 DIF 的 exchangeability 假设（同一 model family 内高度相关），论文通过 graduated de-duplication 和 architecture heterogeneity check（Appendix A.2, 99.98% decoder-only）应对；(b) temporal cohort 定义（而非传统的 demographic groups）需要 ability confounding 控制（matched-ability analysis, Cohen's d=-0.17）；(c) semi-synthetic framework 的 cross-subject matching 设计针对 multi-domain benchmark 结构。这些并非照搬。\n\n3. **3 个 descriptive findings 并不等于低价值**：EMNLP/ARR 社区接受高质量的 empirical/analysis papers（参见 Burnell et al. 2023 in Science, Rodriguez et al. 2021 ACL——两篇都主要是 descriptive findings with methodological framing）。Claim 2 (ground truth meta-critique) 对整个 contamination detection 文献的 evaluation methodology 有实际影响。\n\n**但我同意论文应更清晰论证 LLM-specific 挑战**。当前 Method section 过于 textbook-style，未充分讨论为什么直接搬运 DIF 到 LLM 场景不够——例如 local dependence（Yen's Q3）、model family structure、ability distribution 的非正态性等。建议在 Section 3 开头增加 1-2 段讨论 LLM 作为 examinees 的特殊性及论文如何应对。\n\n**结论**：不应升级为 Must-Fix。建议改为 Should-Fix，要求补充 LLM-specific methodological challenges 的讨论。\n\n---\n\n**[AGREE with nuance] R2-N3: Temporal cohort 定义过于粗糙**\n\n与我的 N2（因果模糊性）高度相关但切入角度不同。R2 批评的是 cohort 划分的 granularity，我批评的是 DIF 结果的 causal interpretation。两者指向同一根本问题：**calendar-year cohort 混淆了太多变量**。\n\n我同意 R2 的三个具体点：\n- Calendar year 确实同时混淆了 architecture shift、training methodology、data composition 变化\n- 6-month window 结果（MMLU C%=34.35%, Section 4.7 最后一段）仅作为 one-liner 出现，未展开分析\n- \"Temporal comparability\" 的 framing 暗示了比数据支持的更强的 temporal specificity\n\n**但我不完全同意将此升级为 critical**。论文的 5 种 cohort design 已经提供了一定程度的 triangulation：random split (0.18%) 排除了抽样噪声，ability-quintile (2.9%) 排除了纯 ability 差异，within-family (matched 28.3%) 控制了部分 architecture effect。calendar year 作为 primary cohort 定义虽粗糙，但在 Open LLM Leaderboard 数据上是最自然的选择（finer-grained metadata 如 training data cutoff 对大多数模型不可用）。\n\n**关联我的 N2**：R2-N3 和我的 N2 共同构成一个强论点——论文需要更谨慎的 framing。如果 cohort 定义粗糙（R2-N3）且 DIF 不能区分 instability vs. capability evolution（我的 N2），则 \"Psychometric Instability\" 的结论过强。建议将两个问题合并处理：软化 causal framing + 补充 within-year 完整分析。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R2-W1: ρ≈0.997 vs 31.3% 张力，Audit Protocol 过于简短**\n\nSection 5.4 \"Recommended DIF Audit Protocol\" 确实只有 3 句话，对于一篇声称\"LLM benchmarks need psychometric monitoring\"的论文来说，practical recommendations 的深度严重不足。论文花了大量篇幅证明 DIF 存在，但对\"发现 DIF 后该怎么做\"的讨论几乎为零。ρ≈0.997 说明 aggregate ranking 不受影响，但论文同时声称 25% 的模型 rank shift ≥100——这个张力值得更深入的讨论：何时 DIF 需要 action，何时只需 annotation？\n\n---\n\n**[AGREE] R2-W2: ΔFPR=0.000 过于完美**\n\n与我的 N1 一致。R2 从不同角度提出了互补的批评：R2 关注注入率固定 20% 和仅 5 subjects 的验证范围，我关注 subject-localized injection 的 ecological validity。两个批评共同削弱了 Proposition 1 / Claim 3 的说服力。R2 补充的 Type II error 讨论也是有价值的——论文只关注了 FPR=0，但未讨论在何种条件下 cross-subject matching 可能 miss real DIF (reduced TPR)。\n\n---\n\n**[AGREE] R2-W3: DIF 术语对 EMNLP 读者不友好**\n\n合理建议。虽然论文 Section 3.2 的 DIF 描述是准确的，但对 NLP 社区读者来说过于 formal。一个 running example（例如用一个具体的 MMLU 题目展示 2023 models 和 2024 models 的不同表现模式）可以显著提升 accessibility，且只需 3-5 行。\n\n---\n\n**[AGREE] R2-W4: 与 Growing Pains 的区分过于简短**\n\n论文在 Related Work 中提到 Growing Pains (Habba et al. 2026) 只有一句 \"our work is complementary\"，但未定量验证 DIF-flagged items 与 FPC anchor items 的 overlap。如果两种方法 flag 的 items 高度重叠，说明 DIF 没有提供增量信息；如果不重叠，则 complementarity 有实证支持。这个分析很容易做（Jaccard/enrichment），不做是遗憾。\n\n---\n\n**[AGREE] R2-W5: 引用问题**\n\n与我的小问题一致。verify_references 确认 holland1988mh year=1988 vs OpenAlex=1986（该论文实际发表于 1988 的 book chapter，但 earlier version 可能是 1986——应核实并统一）。8 个 orphan bib entries 应清理。\n\n---\n\n### Missing References 回应\n\n**[AGREE]** R2 推荐的 4 篇文献中：\n- \"Lifting the Benchmark Iceberg with IRT\" (2025) 和 ATLAS (Li et al. 2025) 确实与本文高度相关——都将 IRT/psychometric 方法应用于 LLM evaluation，不引用会让 Related Work 显得不完整。\n- Benchmark2 和 MedIRT 相关性稍弱但值得 mention。论文当前 Related Work 已经较密集，建议选择性增加最相关的 2-3 篇。\n\n---\n\n### 总结：R1 与 R2 的共识与分歧\n\n**共识区域（两位 reviewer 均认为需要改进）：**\n1. Claim 4 / GSM1K 支撑不足（R2-N1 = 我的 W4）→ 建议降级为 observation\n2. ΔFPR=0.000 的 validity 限制（R2-W2 ≈ 我的 N1）→ 核心方法论问题\n3. Temporal framing 与 causal interpretation（R2-N3 ≈ 我的 N2）→ 需软化 claims\n4. 引用问题（R2-W5 = 我的小问题）→ 容易修复\n\n**分歧区域：**\n1. **Novelty (R2-N2)**：R2 认为是 critical，我认为是 Should-Fix。论文已 self-position 为 empirical contribution，且 EMNLP 社区接受此类工作。但需补充 LLM-specific challenges 的讨论。\n2. **严重程度排序**：我将 semi-synthetic ecological validity（N1）和 causal ambiguity（N2）列为最关键问题；R2 将 Claim 4 insufficiency（N1）和 novelty（N2）列为最关键。两组 priorities 互补。\n\n**如果作者只能修复 3 个问题，我建议优先级为：**\n1. 软化 causal framing（回应 R1-N2 + R2-N3）——改标题/措辞，成本低影响大\n2. 补充 multi-subject injection 实验（回应 R1-N1 + R2-W2）——加强核心 validation\n3. 降级 Claim 4 为 observation（回应 R2-N1 + R1-W4）——避免 overclaiming",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 — 对 Reviewer 2 Round 1 意见\n\n---\n\n### Must-Fix 回应\n\n**[AGREE] R2-N1: Claim 4 \"DIF as diagnostic lens\" 支撑不足**\n\n与我的 W4 完全一致。GSM1K N=33 的相关分析（r=-0.478, CI=[-0.71, -0.16]）统计效力严重不足，单个异常模型即可显著改变结论。论文在 Limitations 中承认这是 exploratory，但 Discussion Section 5.3 和 Introduction Claim 4 的措辞并未匹配这一谨慎程度——\"DIF captures behavioral change distinct from memorization\" 作为 contribution 陈述过强。\n\n补充一点 R2 未提及的：Claim 4 的另一支撑——difficulty-direction interaction（ρ=-0.597）——本身解读也有歧义（见我的 N2）。gains on hard items + erosion on easy ones 同样可解释为 expected capability evolution 而非 diagnostic signal。因此 Claim 4 的两条证据链都有弱点。\n\n**建议**：同意 R2——降级为 exploratory observation 或 supplementary analysis，从 4 个 contributions 中移除。\n\n---\n\n**[REBUT] R2-N2: 方法论新颖性论证不充分**\n\nR2 的批评方向合理但严厉程度偏重，理由如下：\n\n1. **论文已 explicitly 定位为 empirical contribution**：Introduction 第 19 行明确写道 \"Our contributions are empirical and methodological, not algorithmic\"。论文从未声称 MH-DIF 或 cross-subject matching 是新方法——它声称的是将已有方法**大规模应用于 LLM evaluation 这个新 domain** 并产生了 non-trivial empirical findings。\n\n2. **Transplant 并非 trivial**：虽然 MH-DIF 是 1988 年的方法，但将其应用于 LLM benchmarks 涉及多个 LLM-specific 的适配决策——(a) LLMs 作为 examinees 不满足传统 DIF 的 exchangeability 假设（同一 model family 内高度相关），论文通过 graduated de-duplication 和 architecture heterogeneity check（Appendix A.2, 99.98% decoder-only）应对；(b) temporal cohort 定义（而非传统的 demographic groups）需要 ability confounding 控制（matched-ability analysis, Cohen's d=-0.17）；(c) semi-synthetic framework 的 cross-subject matching 设计针对 multi-domain benchmark 结构。这些并非照搬。\n\n3. **3 个 descriptive findings 并不等于低价值**：EMNLP/ARR 社区接受高质量的 empirical/analysis papers（参见 Burnell et al. 2023 in Science, Rodriguez et al. 2021 ACL——两篇都主要是 descriptive findings with methodological framing）。Claim 2 (ground truth meta-critique) 对整个 contamination detection 文献的 evaluation methodology 有实际影响。\n\n**但我同意论文应更清晰论证 LLM-specific 挑战**。当前 Method section 过于 textbook-style，未充分讨论为什么直接搬运 DIF 到 LLM 场景不够——例如 local dependence（Yen's Q3）、model family structure、ability distribution 的非正态性等。建议在 Section 3 开头增加 1-2 段讨论 LLM 作为 examinees 的特殊性及论文如何应对。\n\n**结论**：不应升级为 Must-Fix。建议改为 Should-Fix，要求补充 LLM-specific methodological challenges 的讨论。\n\n---\n\n**[AGREE with nuance] R2-N3: Temporal cohort 定义过于粗糙**\n\n与我的 N2（因果模糊性）高度相关但切入角度不同。R2 批评的是 cohort 划分的 granularity，我批评的是 DIF 结果的 causal interpretation。两者指向同一根本问题：**calendar-year cohort 混淆了太多变量**。\n\n我同意 R2 的三个具体点：\n- Calendar year 确实同时混淆了 architecture shift、training methodology、data composition 变化\n- 6-month window 结果（MMLU C%=34.35%, Section 4.7 最后一段）仅作为 one-liner 出现，未展开分析\n- \"Temporal comparability\" 的 framing 暗示了比数据支持的更强的 temporal specificity\n\n**但我不完全同意将此升级为 critical**。论文的 5 种 cohort design 已经提供了一定程度的 triangulation：random split (0.18%) 排除了抽样噪声，ability-quintile (2.9%) 排除了纯 ability 差异，within-family (matched 28.3%) 控制了部分 architecture effect。calendar year 作为 primary cohort 定义虽粗糙，但在 Open LLM Leaderboard 数据上是最自然的选择（finer-grained metadata 如 training data cutoff 对大多数模型不可用）。\n\n**关联我的 N2**：R2-N3 和我的 N2 共同构成一个强论点——论文需要更谨慎的 framing。如果 cohort 定义粗糙（R2-N3）且 DIF 不能区分 instability vs. capability evolution（我的 N2），则 \"Psychometric Instability\" 的结论过强。建议将两个问题合并处理：软化 causal framing + 补充 within-year 完整分析。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R2-W1: ρ≈0.997 vs 31.3% 张力，Audit Protocol 过于简短**\n\nSection 5.4 \"Recommended DIF Audit Protocol\" 确实只有 3 句话，对于一篇声称\"LLM benchmarks need psychometric monitoring\"的论文来说，practical recommendations 的深度严重不足。论文花了大量篇幅证明 DIF 存在，但对\"发现 DIF 后该怎么做\"的讨论几乎为零。ρ≈0.997 说明 aggregate ranking 不受影响，但论文同时声称 25% 的模型 rank shift ≥100——这个张力值得更深入的讨论：何时 DIF 需要 action，何时只需 annotation？\n\n---\n\n**[AGREE] R2-W2: ΔFPR=0.000 过于完美**\n\n与我的 N1 一致。R2 从不同角度提出了互补的批评：R2 关注注入率固定 20% 和仅 5 subjects 的验证范围，我关注 subject-localized injection 的 ecological validity。两个批评共同削弱了 Proposition 1 / Claim 3 的说服力。R2 补充的 Type II error 讨论也是有价值的——论文只关注了 FPR=0，但未讨论在何种条件下 cross-subject matching 可能 miss real DIF (reduced TPR)。\n\n---\n\n**[AGREE] R2-W3: DIF 术语对 EMNLP 读者不友好**\n\n合理建议。虽然论文 Section 3.2 的 DIF 描述是准确的，但对 NLP 社区读者来说过于 formal。一个 running example（例如用一个具体的 MMLU 题目展示 2023 models 和 2024 models 的不同表现模式）可以显著提升 accessibility，且只需 3-5 行。\n\n---\n\n**[AGREE] R2-W4: 与 Growing Pains 的区分过于简短**\n\n论文在 Related Work 中提到 Growing Pains (Habba et al. 2026) 只有一句 \"our work is complementary\"，但未定量验证 DIF-flagged items 与 FPC anchor items 的 overlap。如果两种方法 flag 的 items 高度重叠，说明 DIF 没有提供增量信息；如果不重叠，则 complementarity 有实证支持。这个分析很容易做（Jaccard/enrichment），不做是遗憾。\n\n---\n\n**[AGREE] R2-W5: 引用问题**\n\n与我的小问题一致。verify_references 确认 holland1988mh year=1988 vs OpenAlex=1986（该论文实际发表于 1988 的 book chapter，但 earlier version 可能是 1986——应核实并统一）。8 个 orphan bib entries 应清理。\n\n---\n\n### Missing References 回应\n\n**[AGREE]** R2 推荐的 4 篇文献中：\n- \"Lifting the Benchmark Iceberg with IRT\" (2025) 和 ATLAS (Li et al. 2025) 确实与本文高度相关——都将 IRT/psychometric 方法应用于 LLM evaluation，不引用会让 Related Work 显得不完整。\n- Benchmark2 和 MedIRT 相关性稍弱但值得 mention。论文当前 Related Work 已经较密集，建议选择性增加最相关的 2-3 篇。\n\n---\n\n### 总结：R1 与 R2 的共识与分歧\n\n**共识区域（两位 reviewer 均认为需要改进）：**\n1. Claim 4 / GSM1K 支撑不足（R2-N1 = 我的 W4）→ 建议降级为 observation\n2. ΔFPR=0.000 的 validity 限制（R2-W2 ≈ 我的 N1）→ 核心方法论问题\n3. Temporal framing 与 causal interpretation（R2-N3 ≈ 我的 N2）→ 需软化 claims\n4. 引用问题（R2-W5 = 我的小问题）→ 容易修复\n\n**分歧区域：**\n1. **Novelty (R2-N2)**：R2 认为是 critical，我认为是 Should-Fix。论文已 self-position 为 empirical contribution，且 EMNLP 社区接受此类工作。但需补充 LLM-specific challenges 的讨论。\n2. **严重程度排序**：我将 semi-synthetic ecological validity（N1）和 causal ambiguity（N2）列为最关键问题；R2 将 Claim 4 insufficiency（N1）和 novelty（N2）列为最关键。两组 priorities 互补。\n\n**如果作者只能修复 3 个问题，我建议优先级为：**\n1. 软化 causal framing（回应 R1-N2 + R2-N3）——改标题/措辞，成本低影响大\n2. 补充 multi-subject injection 实验（回应 R1-N1 + R2-W2）——加强核心 validation\n3. 降级 Claim 4 为 observation（回应 R2-N1 + R1-W4）——避免 overclaiming",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-21T15:25:38.076886+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3766
}
```

</details>

---


### Assistant

_source line 210 · 2026-05-21T15:25:44.840021+00:00_

交叉回应已提交。

核心结论：R1 与 R2 在 4 个关键问题上形成共识——Claim 4 支撑不足、semi-synthetic 框架生态效度有限、temporal framing 过强、引用需修复。主要分歧在 novelty 的严重程度（R2 视为 critical，我认为 Should-Fix，因为论文已明确定位为 empirical contribution）。建议作者优先处理：(1) 软化 causal framing/标题，(2) 补充 multi-subject injection 实验，(3) 将 Claim 4 降级为 exploratory observation。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 9

## Round 9

54 recorded events


### User

_source line 211 · 2026-05-21T17:41:36.505497+00:00_

[Round 1 审稿请求]:
## Review Assignment: R1 — Methods & Experiments

**Venue**: EMNLP 2026 (ARR), scoring 1–5 half-point scale. Main acceptance ~21%. Overall Assessment: 5=Award, 4=Conference accept, 3=Findings, 2=Resubmit, 1=Do not resubmit.

**Paper**: "Temporal Measurement Drift in LLM Benchmarks: A Psychometric DIF Analysis of 5,227 Models on MMLU"

**Your focus**: Methodological soundness, experimental design, statistical rigor, reproducibility.

### Paper Summary
The paper applies Mantel–Haenszel DIF analysis to the METABENCH MMLU response matrix (5,227 models × 12,508 items), finding 20–28% of items show large temporal DIF (ETS Category C) between 2023 and 2024 model cohorts after conservative controls (permutation null subtraction, ability matching). It argues this instability is item-specific (not domain-driven), does not threaten ranking validity (ρ≈0.994), and that web-overlap labels cannot validate item-level differential detectors (enrichment ≈1.0). The primary methodological contribution is a semi-synthetic validation framework injecting contamination into real response matrices with cross-subject ability matching (ΔFPR<0.001, ΔTPR=0.37–0.42 at p=0.5).

### Structure (8pp main + 4pp appendices A–E)
- §1 Introduction, §2 Related Work, §3 Method (MH-DIF + Semi-synthetic framework), §4 Experiments (4.1–4.11: temporal DIF, permutation null, architecture stratification, multi-benchmark, ConStat, DVD, semi-synthetic validation, GSM8K replication, graceful degradation, odds ratio regression, IFT), §5 Discussion, §6 Limitations, §7 Conclusion
- Appendices: A (RL robustness), B (Ensemble fusion), C (Bifactor IRT pilot), D (Item generation calibration), E (Cumulative Bayesian DIF)

### Key Tables
- Table 1: Temporal DIF summary (Raw C%=31.3, Eff. C%≈24.5)
- Table 2: Within-family confound control
- Table 3: Permutation null (mean=5.2%, z=32.6)
- Table 4: Architecture stratification (non-issue)
- Table 5: Multi-benchmark temporal DIF (6 benchmarks, 14.8–31.3%)
- Table 6: ConStat detection by model category (AUROC 0.51–0.67)
- Table 7: DVD detection (AUROC=0.58, SNR=1.3)
- Tables 8–9: Semi-synthetic validation (ΔTPR dose-response, cross-subject vs within-subject matching)
- Table 10: GSM8K replication (C%=15.2, ΔTPR=0.42)
- Table 11: Graceful degradation (ρ>0.993 at 31% replacement)
- Tables 12–13: Odds ratio regression (R²=0.073 max), IFT comparison (Jaccard=0.72)

### Review Dimensions (rate each 1–5)
1. **Soundness**: Is MH-DIF correctly applied? Are the permutation null, ability matching, and cross-subject matching methodologically sound? Are statistical claims supported?
2. **Reproducibility**: Could someone replicate this with the described data and methods?
3. **Experimental coverage**: Are important controls present? What's missing?

### Specific Questions to Address
- The 1D IRT model is fundamentally misspecified for MMLU (98% |Lz|>2, CFI=0.72). The paper bounds this in §5 with three arguments (architecture stratification, convergence of matched estimates, IFT overlap). Are these bounds convincing, or does misspecification undermine the DIF findings?
- The semi-synthetic framework uses binary flipping (incorrect→correct at rate p). How much does this simplification limit the framework's real-world relevance?
- The permutation null of 5.2% is non-trivial. Does the paper adequately explain what this null represents and properly adjust for it?
- GSM1K correlation is negative (r=−0.35, opposite to contamination hypothesis), wide CI, Spearman non-significant. Is this adequately handled?
- RL robustness is inconclusive (N=13, Jaccard=0.75, TOST p=0.18). Is this limitation properly scoped?
- Cross-subject matching ΔFPR<0.001 is the key methodological innovation. Is the argument for why this works convincing?

### Experiment Coverage Check
The review_context lists these imagined experiments. Check which are covered:
1. real_data_dif_mmlu — §4.1 ✓
2. rl_robustness_validation — Appendix A ✓ (demoted to limitation)
3. constat_perturbation_eval — §4.5 ✓
4. dvd_generation_variance_eval — §4.6 ✓
5. ensemble_fusion — Appendix B ✓ (marginal improvement, correctly dropped)
6. cross_benchmark_gsm8k — §4.8 ✓
7. bifactor_irt_equating_pilot — Appendix C ✓ (convergence failure)
8. item_generation_calibration — Appendix D ✓ (below targets)
9. cumulative_bayesian_dif — Appendix E ✓ (insufficient power)
10. graceful_degradation_analysis — §4.9 ✓
11. item_focused_trees — §4.11 ✓
12. architecture_stratified_dif — §4.3 ✓
13. semi_synthetic_contamination_validation — §4.7 ✓
14. multi_benchmark_temporal_dif — §4.4 ✓
15. permutation_null_c_rate — §4.2 ✓
16. odds_ratio_regression_transparency — §4.10 ✓

Provide: per-dimension scores, strengths (≥3), weaknesses (≥3), questions to authors (≥2), and a preliminary Overall Assessment with calibration rationale.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-21T17:42:04.279828+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-6",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-6",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 213 · 2026-05-21T17:42:04.636334+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 214 · 2026-05-21T17:42:05.239299+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 586.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.7}], \"total_pages\": 13, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 959
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-21T17:42:05.239879+00:00_

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
21	\title{Temporal Measurement Drift in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-21T17:42:10.313938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 217 · 2026-05-21T17:42:10.767397+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 218 · 2026-05-21T17:42:11.172528+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool call

_source line 219 · 2026-05-21T17:42:11.223319+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-21T17:42:11.727908+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-21T17:42:12.637368+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1869
}
```

</details>

---


### Tool result

_source line 222 · 2026-05-21T17:42:12.638685+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1415
}
```

</details>

---


### Tool call

_source line 223 · 2026-05-21T17:42:12.689380+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 224 · 2026-05-21T17:42:13.094257+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1366
}
```

</details>

---


### Tool call

_source line 225 · 2026-05-21T17:42:13.195969+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-21T17:42:13.758956+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-21T17:42:13.962193+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1272
}
```

</details>

---


### Tool result

_source line 228 · 2026-05-21T17:42:13.962695+00:00_

1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet whether individual items measure the same construct over time is rarely tested---and existing contamination detectors validate against ground truth that conflates global exposure with differential functioning. We develop a semi-synthetic injection framework with cross-subject matching that achieves zero false positive inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$), and show that web-overlap contamination labels are near-independent of Mantel-Haenszel Differential Item Functioning (DIF) flags (enrichment $\approx 0.96$, $\phi = 0.012$)---exposing a category error in prevailing validation methodology. Applying MH-DIF with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 items), we find 17.9--31.3\% of items exhibit large temporal DIF (ETS~C) between 2023 and 2024 cohorts, each 45--174$\times$ above random baselines, with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). This does not threaten ranking validity ($\rho \approx 0.997$) but reveals which capability dimensions shift across generations. Item-level decomposition shows 92.4\% of the signal is item-specific; DIF-flagged items concentrate discriminative information ($z = -8\sigma$ to $-49\sigma$) with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 229 · 2026-05-21T17:42:13.962997+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 230 · 2026-05-21T17:42:14.063849+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. This pattern persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of the DIF signal is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this measurement drift does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The drift is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{liang2026dvd}, 
…[truncated 5168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-21T17:42:14.317644+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1121
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-21T17:42:20.749424+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-21T17:42:21.252366+00:00_

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
…[truncated 7857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-21T17:42:21.252906+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-21T17:42:21.253398+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	A Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold.
10	
11	\subsection{Temporal Comparability: 31\% Measurement Drift}
12	\label{sec:temporal}
13	
14	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%], $B = 1{,}000$ model-level resamples). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold on effect size and significance already provides implicit multiple-testing protection.
15	
16	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C items (sampling noise), and an ability-quintile comparison within the same temporal cohort yields 2.9\% (ability differences alone). A within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% ETS~C items, elevated by large ability gaps that confound the DIF signal~\citep{holland1988mh}. The contrast between 2.9\% (ability-controlled) and 61.3\% (ability-confounded) brackets the temporal rate o
…[truncated 9821 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-21T17:42:21.806077+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-21T17:42:21.856850+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Implications for Benchmark Temporal Comparability}
5	\label{sec:disc_temporal}
6	
7	The 31\% ETS~C DIF rate extends across all six METABENCH benchmarks (C\% $= 17.9$--$31.3\%$, 45--174$\times$ above baselines; \Cref{tab:cross_benchmark}), with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). The Simpson's paradox (\Cref{sec:temporal}) confirms item properties, not accuracy gains, drive DIF. This does not invalidate ranking ($\rho \approx 0.997$) but signals measurement drift across model generations.
8	
9	\subsection{Ground Truth Meta-Critique}
10	\label{sec:disc_groundtruth}
11	
12	The near-independence between DIF flags and web-overlap labels (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$) admits two interpretations: web-overlap labels may be the wrong ground truth for a differential method, or DIF may fail to detect contamination. The semi-synthetic dose-response ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$) partially resolves this by confirming that MH-DIF \emph{can} detect differential item behavior when present; the near-independence therefore reflects a category error in the ground truth rather than a detection failure.
13	
14	\subsection{DIF as Diagnostic Lens}
15	\label{sec:disc_diagnostic}
16	
17	The GSM1K correlation ($r = -0.478$, partial $r = -0.385$; \Cref{sec:gsm8k}) provides exploratory evidence that DIF captures behavioral change distinct from memorization. DIF-C items are harder ($d = -0.247$) and more discriminating ($d = 0.230$), with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones.
18	
19	\subsection{Recommended DIF Audit Protocol}
20	\label{sec:disc_protocol}
21	
22	These findings motivate a benchmark maintenance protocol triggered whenever $\geq 500$ new models accumulate, using cross-subject matching. We propose graduated thresholds: C\% $< 15\%$ $\to$ monitor; $
…[truncated 176 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-21T17:42:28.186578+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-21T17:42:28.187039+00:00_

1	\section*{Limitations}
2	
3	\paragraph{Methodological scope.}
4	MH-DIF detects only uniform DIF; logistic regression reveals an additional 24.8\% non-uniform DIF, making 31\% conservative. More fundamentally, DIF detects \emph{that} items function differently but cannot determine \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts. A definitive causal decomposition remains out of reach without access to model training data.
5	
6	\paragraph{Matching boundary and sample size.}
7	Cross-subject matching assumes contamination affects a minority of domains; when contamination spans ${>}10$ subjects (${>}18\%$ of MMLU), $\Delta\mathrm{FPR}$ rises to 0.026--0.069. The GSM1K correlation analysis ($N = 33$) has limited statistical power and is exploratory; replication with larger model samples is warranted.
8	
9	\paragraph{Generalizability.}
10	All six benchmarks use multiple-choice or binary scoring; generalizability to open-ended generation (e.g., AlpacaEval), coding (e.g., HumanEval), or partial-credit benchmarks is untested and would require polytomous DIF methods. Temporal cohorts are defined by calendar year, a coarse grouping; finer-grained definitions (e.g., by training data cutoff or alignment method) might reveal more targeted patterns.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-21T17:42:29.192065+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-21T17:42:29.192621+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	A semi-synthetic framework with cross-subject matching ($\Delta\mathrm{FPR} = 0.000$) resolves a validation gap: web-overlap labels are near-independent of DIF flags (enrichment $\approx 0.96$). Across six METABENCH benchmarks (27,125 items, 5,227 models), MH-DIF reveals 17.9--31.3\% temporal measurement drift (ETS~C) driven by item properties; DIF-flagged items concentrate discriminative signal ($z{=}{-}8\sigma$ to ${-}49\sigma$; $\rho{=}{-}0.597$). LLM benchmarks need psychometric monitoring alongside score reporting.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-21T17:42:29.745120+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-21T17:42:29.846152+00:00_

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
…[truncated 4637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-21T17:42:36.628227+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "7-13",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "7-13",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-21T17:42:37.532964+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 485.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 551.8}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 594.4}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 564.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 343.5}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 143.4}], \"total_pages\": 13, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-21T17:42:55.960413+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 247 · 2026-05-21T17:42:56.362296+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 248 · 2026-05-21T17:42:56.714611+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 249 · 2026-05-21T17:42:57.067893+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 250 · 2026-05-21T17:42:57.570997+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1208
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-21T17:42:57.723338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-21T17:42:58.325961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 253 · 2026-05-21T17:42:58.529979+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-21T17:42:58.783121+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-21T17:42:59.489615+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1163
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-21T17:42:59.490060+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-21T17:42:59.843805+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool result

_source line 258 · 2026-05-21T17:42:59.846353+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1063
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-21T17:42:59.847450+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1317
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-21T17:44:44.410658+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-21T17:44:44.662039+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues. Performance-based detectors identify contamination through statistical anomalies: ConStat \citep{dekoninck2024constat} tests performance gaps between original and perturbed items, DVD \citep{liang2026dvd} uses distributional verification, and Self-Critique \citep{tao2026selfcritique} employs model self-evaluation. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (\Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} assessed t
…[truncated 3952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-21T17:48:08.102826+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 2 审稿意见（方法严谨性 + 实验设计）\n\n### ⚠️ 重要前置说明：实际论文与 Director Summary 不一致\n\nDirector 提供的 Paper Summary 描述了一篇包含 §4.1-4.11（11 个实验子节）、Tables 1-13、Appendices A-E 的论文。**实际 PDF 的内容与此不符：**\n\n| Director Summary | 实际论文 |\n|---|---|\n| Title: \"...A Psychometric DIF Analysis of 5,227 Models on MMLU\" | Title: \"...A Large-Scale Psychometric Audit of 5,227 Models\" |\n| §4.1-4.11（含 permutation null, ConStat, DVD, graceful degradation, odds ratio regression, IFT） | §4.1-4.7（Validation, Temporal, Ground Truth, Structural, Semi-synthetic, Downstream, Cross-Benchmark） |\n| Tables 1-13 | Tables 1-3 + 1 appendix table |\n| Appendices A-E（RL robustness, Ensemble fusion, Bifactor IRT, Item gen calibration, Bayesian DIF） | Appendices A-D（Method Details, Structural Details, Figures, Cross-Benchmark） |\n| Eff. C% ≈ 24.5（permutation null subtraction） | Raw C% = 31.3%，无 permutation null |\n| ρ ≈ 0.994 | ρ ≈ 0.997 |\n| GSM1K r = -0.35 | GSM1K r = -0.478 |\n| \"98% |Lz|>2, CFI=0.72\" | 未报告 IRT fit statistics |\n\n**以下审稿意见基于实际 PDF 内容。**\n\n---\n\n## 与 Round 1 对比：修改响应评估\n\n论文针对 Round 1（R1 + R2）反馈做了实质性修改，逐条评估：\n\n| Round 1 问题 | 修改情况 | 评估 |\n|---|---|---|\n| R1-N1: Semi-synthetic ecological validity | Proposition 1 限定为 \"single-subject\"，新增 multi-subject injection (k∈{1,3,5,10,20}) → ΔFPR<0.007 for k≤5 | ✅ 核心关切已回应，但仅 1 段，应扩展 |\n| R1-N2: 因果模糊性 / \"Instability\" framing | Title \"Psychometric Instability\" → \"Temporal Measurement Drift\"；Section 4.2 标题同步更改；Discussion 5.2 明确承认双向解读 | ✅ 充分回应 |\n| R1-N3: Bootstrap CI 不对称性 | 明确 \"B=1,000 model-level resamples\" | ⚠️ 部分回应（CI 不对称性原因仍未讨论） |\n| R1-W4/R2-N1: Claim 4 GSM1K 支撑不足 | Contributions 从 4 个缩减为 3 个，Claim 4 降级为 Discussion 5.3 exploratory evidence | ✅ 充分回应 |\n| R2-N2: 方法论新颖性 | 新增 \"LLM-specific challenges\" 段落（Method 3.2），讨论 local independence、fine-tuned variants、non-normal distribution、multidimensionality | ✅ 充分回应 |\n| R2-N3: Temporal cohort 粗糙 | Title 改善；Limitations 明确讨论；6-month window 仍为 one-liner | ⚠️ 部分回应 |\n| R2-W1: Audit protocol 过短 | 扩展为 graduated thresholds: <15% monitor, 15-25% flag, >25% act | ✅ 有改善 |\n| R2-W3: Running example | Method 3.2 新增具体 formal-logic item 示例（α_MH=0.42, Δ_MH=2.04） | ✅ 有效 |\n| R2-W4: Growing Pains 区分 | Related Work 扩展：\"Growing Pains assumes anchor item stability... Empirical comparison awaits public release\" | ⚠️ 合理但仍无定量比较 |\n| R2 Missing References | 新增 ATLAS (li2025atlas), MedIRT (luo2025medirt), BHI (zhu2026bhi), Benchmark² (qian2026benchmark2) | ✅ 全部补充 |\n\n---\n\n## 维度评分\n\n### Soundness: 4 / 5\n\n**MH-DIF 应用正确性**：公式 (1)-(2) 标准，K=5 quintile binning 符合 ETS 惯例，ETS C 分类（|Δ_MH|≥1.5 + p<0.05 双阈值）严格。Running example（formal-logic item, α_MH=0.42 → Δ_MH=2.04）帮助读者验证计算。\n\n**控制实验设计合理**：5 种 cohort design 系统排除替代解释——random split (0.18%) 排除噪声、ability-quintile (2.9%) 排除纯能力差异、within-family (61.3% → matched 28.3%) 展示 ability confounding 的影响、matched-ability (31.3% → 28.9%) 量化残余 ability effect（~2.4pp）。六种替代解释均被测试，收敛于 ~28-29% 的 floor，令人信服。\n\n**Proposition 1 修订得当**：限定为 \"under single-subject cross-subject matching\"，数学上 trivially true 但不再 overclaim。multi-subject injection boundary (ΔFPR<0.007 for k≤5) 是对 R1-N1 的直接回应，提供了方法适用边界的实证依据。\n\n**扣分原因**：\n(a) **缺少 permutation null**：random-split control (0.18%) 是 perfect null 条件下的估计，但不等于 permutation null。随机打乱 cohort labels 后的期望 C% 是什么？如果 permutation null 为 ~5%，则 \"effective\" DIF 应为 ~26% 而非 31%。这对 headline 数字的解读有实质影响。论文缺少这个分析。\n(b) **IRT model fit 未评估**：论文使用 2PL 参数做 power analysis（ā=1.2, b̄=-0.84），但未报告 model fit statistics（如 |Lz|, CFI, RMSEA）。MH-DIF 本身是非参数方法，不依赖 IRT fit——这点论文正确指出。但 MMLU 的 57 subjects 显然违反 unidimensionality，论文在 \"LLM-specific challenges\" 段中承认但未量化违反程度。\n(c) **binary flipping 的生态效度局限**：注入框架用 uniform rate p 翻转 incorrect→correct，真实 contamination 是非均匀的（部分 items 被完整记忆、部分仅记忆 answer letter、RLHF 创造非均匀效应）。论文应讨论对 non-uniform injection 的敏感性。\n\n### Reproducibility: 4 / 5\n\n**强项**：METABENCH 数据公开可获取、anonymous.4open.science 代码链接、power analysis 参数显式（\"empirical 2PL parameters from PSN-IRT: ā=1.2, b̄=-0.84; 14,042 MMLU items\"）、bootstrap 参数明确（B=1,000 model-level resamples）。\n\n**扣分**：multi-subject injection protocol 细节不足——k 的选择、每个 k 下的随机抽取策略、\"5 random draws each\" 的具体实现。Semi-synthetic 注入的 ETS A 选择标准（\"items classified as ETS A in the uninjected data\"）的确切阈值应明确。\n\n### Experimental Coverage: 3.5 / 5\n\n**Coverage Check（对照 Director 提供的 16 项实验清单）：**\n\n| # | 实验 | 状态 | 位置 |\n|---|---|---|---|\n| 1 | real_data_dif_mmlu | ✅ 完整 | §4.2 |\n| 2 | rl_robustness_validation | ❌ 不存在 | — |\n| 3 | constat_perturbation_eval | ⚠️ 提及但无专门分析 | §4.3 context |\n| 4 | dvd_generation_variance_eval | ❌ 不存在 | — |\n| 5 | ensemble_fusion | ❌ 不存在 | — |\n| 6 | cross_benchmark_gsm8k | ✅ 完整 | §4.7 |\n| 7 | bifactor_irt_equating_pilot | ❌ 不存在 | within-subject DIF 最近似 |\n| 8 | item_generation_calibration | ❌ 不存在 | — |\n| 9 | cumulative_bayesian_dif | ❌ 不存在 | — |\n| 10 | graceful_degradation_analysis | ⚠️ 隐含（ρ≈0.997） | §4.6 一句话 |\n| 11 | item_focused_trees | ❌ 不存在 | — |\n| 12 | architecture_stratified_dif | ⚠️ 部分 | Appendix A.2（99.98% decoder-only） |\n| 13 | semi_synthetic_contamination_validation | ✅ 完整 | §4.5 |\n| 14 | multi_benchmark_temporal_dif | ✅ 完整 | §4.7 |\n| 15 | permutation_null_c_rate | ❌ 不存在 | — |\n| 16 | odds_ratio_regression_transparency | ⚠️ 嵌入§4.2 | Simpson's paradox，OR 分析 |\n\n**4/16 完整覆盖，4/16 部分覆盖，8/16 不存在。** 但需注意这些是 \"imagined experiments\"——并非全部需要。对于 EMNLP 论文，已有的 7 个 experiment sections + 4 appendices 构成完整的故事。最关键的缺失是 **permutation null**（#15）和 **graceful degradation 的系统分析**（#10）。\n\n---\n\n## Director 具体问题回应\n\n### Q1: IRT 1D model misspecification\n\n论文未报告 |Lz| 或 CFI。如果 Director 所述的 \"98% |Lz|>2, CFI=0.72\" 属实，这表示 1D IRT 严重 misspecified。但论文的核心论点——MH-DIF 是非参数方法，不依赖 IRT model fit (Holland & Thayer, 1988)——是技术上正确的。论文在 §3.2 中提供了三层防护：(a) IRT θ 与 total score r=0.9986 → CTT-based stratification 无 bias；(b) 99.98% decoder-only → architecture 不是 confound；(c) cross-subject matching 处理 multidimensionality。\n\n**我的评估**：这三层防护对 MH-DIF 的有效性是 convincing 的——MH-DIF 的 conditional on observed score 性质使其对 latent structure misspecification 具有鲁棒性。但论文至少应报告 fit statistics（即使结论是\"不影响 MH-DIF\"），因为这是 transparent reporting 的要求。如果 CFI=0.72（远低于 0.95 conventional threshold），应在 Limitations 中讨论。\n\n### Q2: Binary flipping 的真实世界相关性\n\n显著局限。Uniform flipping at rate p 假设所有被污染 items 有相同的 exploitation probability，但真实 contamination 是 item-specific 的——更容易记忆的 items（如 factual recall）vs. 推理题，效果差异很大。论文应至少讨论 non-uniform injection (e.g., item-difficulty-dependent exploitation rate) 的 sensitivity，或将此列为 Limitations 而非仅隐含。\n\n当前 Limitations 段 \"Methodological scope\" 提到 \"DIF detects that... not why\" 但未讨论注入框架本身的简化。\n\n### Q3: Permutation null\n\n**论文中不存在 permutation null 分析。** 这是最显著的实验缺失。random-split (0.18%) 是 perfect null（同一 cohort 内部），ability-quintile (2.9%) 是 ability-only null。但 permutation null（随机打乱 temporal labels 后的 C%）才是 31.3% 的正确 baseline comparator。\n\n如果 permutation null ~5%（如 Director 摘要暗示），则：\n- \"effective\" temporal DIF = 31.3% - 5.2% = 26.1%\n- 论文标题中 \"31%\" 可能高估实际效应\n- 所有下游分析（downstream impact, cross-benchmark ratios）都需要调整\n\n**建议**：这是论文应补充的最重要实验。1,000 次 permutation 的计算成本很低。\n\n### Q4: GSM1K 负相关\n\n论文报告 r=-0.478（非 Director 所述 -0.35）, p=0.005, partial r=-0.385, p=0.027, N=33。\n\n修改后的处理**得当**：从 Contribution 列表中移除，降级为 Discussion 5.3 的 \"exploratory evidence\"，Limitations 明确标注 \"limited statistical power\"。N=33 确实无法支撑 firm conclusions，但作为 supplementary observation 是可接受的。\n\n### Q5: RL robustness\n\n论文中不存在。不是关键缺失——论文未声称对 RL post-training 的 robustness。\n\n### Q6: Cross-subject matching ΔFPR\n\n**这是修改最成功的部分。** Round 1 我将此列为 N1 (critical)，修改后：\n\n1. Proposition 1 明确限定为 \"single-subject injection\" → 不再 overclaim\n2. Multi-subject injection (k∈{1,3,5,10,20}) 提供了实证边界：ΔFPR<0.007 for k≤5 (<9% of domains)，k=10 (18%) 时 ΔFPR 升至 0.026-0.069\n3. Limitation 段明确：\"cross-subject matching assumes contamination affects a minority of domains; when contamination spans >10 subjects (>18% of MMLU), ΔFPR rises to 0.026-0.069\"\n\n**论点现在是 convincing 的**：single-subject 有数学保证，multi-subject 有实证边界和 graceful degradation，boundary condition 被明确陈述。唯一改进空间是将 multi-subject 结果从 1 段扩展为 table/figure。\n\n---\n\n## Strengths（≥3）\n\n1. **大规模、系统的 confound 控制**：5 种 cohort design × 6 种替代解释 × 4 个 threshold sensitivity 点，形成了对 31% DIF finding 的全方位 triangulation。matched-ability 分析收敛于 ~28-29% 的 floor（跨不同比较）尤其令人信服。\n\n2. **Ground truth meta-critique 具有社区价值**：Contribution 2 (enrichment=0.964, Jaccard=0.206) 对 contamination detection 文献中普遍使用 web-overlap labels 的做法提出了有实证支撑的质疑。Discussion 5.2 现在明确承认双向解读，增强了论证的诚实性。\n\n3. **Semi-synthetic 框架的 boundary characterization**：multi-subject injection 将框架从 \"trivially true by construction\" 升级为 \"empirically characterized with explicit boundary\"（k≤5 safe, k=10 degradation），这是对 Round 1 批评的高质量回应。\n\n4. **LLM-specific methodological adaptations**：新增的 \"LLM-specific challenges\" 段落（§3.2）不是泛泛之谈，而是针对 local independence (permutation simulation Q3=4.6-34.2%)、fine-tuned variant independence (graduated de-duplication)、non-normal ability (quintile-based stratification)、multidimensionality (cross-subject matching) 提出了具体应对措施。\n\n5. **Cross-benchmark replication at scale**：6 个 METABENCH benchmarks（27,125 items）的 DIF 发现具有一致性（knowledge/reasoning C%≥26.9% > procedural C%≤18.9%），且每个都远高于 random baseline (45-174×)。\n\n---\n\n## Weaknesses（≥3）\n\n1. **缺少 permutation null——headline 数字缺乏正确 baseline**：31.3% 是 raw C%，但无 permutation null 作为 baseline。random-split (0.18%) 是完美 null，不代表 realistic null（cohort 间存在微小系统差异的期望 DIF）。如果 permutation null ~5%，则 effective DIF ~26%，对标题和所有下游分析有实质影响。这是论文最关键的方法论缺失。\n\n2. **IRT model fit 未报告**：论文使用 2PL 参数做 power analysis 但不报告 fit statistics。MH-DIF 虽不依赖 IRT fit，但 transparent reporting 要求至少呈现 unidimensionality 评估（哪怕结论是\"MH-DIF 对此鲁棒\"）。如果 MMLU 确实 CFI=0.72，这是重要的 contextual information。\n\n3. **Binary flipping 简化未充分讨论**：注入框架使用 uniform rate p，真实 contamination 是 heterogeneous 的。这限制了 semi-synthetic 结果向真实场景的推广。当前 Limitations 未涉及此点。\n\n4. **Multi-subject injection 结果过于压缩**：这是论文回应 R1-N1 的核心新增实验，但仅占 Section 4.5 的 1.5 句话。k∈{1,3,5,10,20} 的 ΔFPR 值应以 table 或 figure 呈现，而非 inline text（\"ΔFPR<0.007 for k≤5; at k=10, ΔFPR rises to 0.026-0.069\"）。\n\n5. **Director 期望的实验覆盖缺口**：16 项计划实验中仅 4 项完整覆盖。特别缺失的 permutation null (#15)、graceful degradation 系统分析 (#10)、ConStat/DVD 专门对比 (#3/#4) 会加强论文。即使不全做，permutation null 是必须的。\n\n---\n\n## Questions to Authors（≥2）\n\n**Q1**：能否补充 permutation null 分析？具体来说：将 cohort labels (2023/2024) 随机打乱 1,000 次，每次重新计算 C%，报告 permutation null distribution 的 mean 和 95th percentile。这将为 31.3% 提供 principled baseline，并可能改变 headline 数字（从 31% 改为 null-adjusted 值）。\n\n**Q2**：论文声称 \"IRT θ estimates correlate at r=0.9986 with total scores\"（§3.2），但未报告 underlying IRT model 的 fit statistics。能否报告 MMLU 12,508 items 在 2PL 下的 CFI、RMSEA、或 |Lz| person-fit 分布？如果 fit 确实很差，这 paradoxically 支持论文的论点（MH-DIF 作为非参数方法是更安全的选择），但应 transparently 报告。\n\n**Q3**：multi-subject injection 的 boundary (k≤5 safe) 在 MMLU 语境中意味着什么？如果 real-world contamination 同时影响 >5 个 subjects（例如一个 model 训练时 ingest 了整个 MMLU dataset），cross-subject matching 的 ΔFPR 保证就失效了。论文如何论证 MMLU 的真实 contamination pattern 落在 k≤5 的安全区间内？\n\n---\n\n## Preliminary Overall Assessment\n\n**Overall: 3.5 / 5**（Borderline Conference）\n\n**Calibration rationale**：\n\n**3.5 而非 4.0 的原因**：\n- 缺少 permutation null 是重要的方法论缺失，直接影响 headline 数字的可信度\n- IRT fit 未报告降低了 methodological transparency\n- 多项计划实验未执行（虽然 \"imagined\" 不代表必须，但 permutation null 是标准做法）\n- Binary flipping 简化对 semi-synthetic 框架的 real-world relevance 有实质限制\n\n**3.5 而非 3.0 的原因**：\n- Round 1 的三个 critical issues (N1-N3) 均有实质性回应——title 改善、Proposition 1 限定、multi-subject boundary、bootstrap 单位明确\n- Confound 控制在 EMNLP 同类论文中属于上乘水平（5 cohort designs + 6 alternative explanations）\n- Ground truth meta-critique (Contribution 2) 对社区有独立价值\n- Cross-benchmark replication (6 benchmarks, 27,125 items) 提供了强 robustness\n- Writing quality 高，revised framing (\"drift\" not \"instability\") 更准确\n\n**升至 4.0 的路径**：\n1. 补充 permutation null → 提供 null-adjusted C% 作为 headline\n2. 报告 IRT fit statistics（即使结论不变）\n3. Multi-subject injection 结果以 table 呈现\n4. 在 Limitations 中增加 binary flipping 简化的讨论\n\n**结论**：论文从 Round 1 到 Round 2 的修改是认真且有效的，核心关切均有回应。但 permutation null 的缺失使 headline 数字的解读存在不确定性，阻止了评分升至 Conference accept。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 2 审稿意见（方法严谨性 + 实验设计）\n\n### ⚠️ 重要前置说明：实际论文与 Director Summary 不一致\n\nDirector 提供的 Paper Summary 描述了一篇包含 §4.1-4.11（11 个实验子节）、Tables 1-13、Appendices A-E 的论文。**实际 PDF 的内容与此不符：**\n\n| Director Summary | 实际论文 |\n|---|---|\n| Title: \"...A Psychometric DIF Analysis of 5,227 Models on MMLU\" | Title: \"...A Large-Scale Psychometric Audit of 5,227 Models\" |\n| §4.1-4.11（含 permutation null, ConStat, DVD, graceful degradation, odds ratio regression, IFT） | §4.1-4.7（Validation, Temporal, Ground Truth, Structural, Semi-synthetic, Downstream, Cross-Benchmark） |\n| Tables 1-13 | Tables 1-3 + 1 appendix table |\n| Appendices A-E（RL robustness, Ensemble fusion, Bifactor IRT, Item gen calibration, Bayesian DIF） | Appendices A-D（Method Details, Structural Details, Figures, Cross-Benchmark） |\n| Eff. C% ≈ 24.5（permutation null subtraction） | Raw C% = 31.3%，无 permutation null |\n| ρ ≈ 0.994 | ρ ≈ 0.997 |\n| GSM1K r = -0.35 | GSM1K r = -0.478 |\n| \"98% |Lz|>2, CFI=0.72\" | 未报告 IRT fit statistics |\n\n**以下审稿意见基于实际 PDF 内容。**\n\n---\n\n## 与 Round 1 对比：修改响应评估\n\n论文针对 Round 1（R1 + R2）反馈做了实质性修改，逐条评估：\n\n| Round 1 问题 | 修改情况 | 评估 |\n|---|---|---|\n| R1-N1: Semi-synthetic ecological validity | Proposition 1 限定为 \"single-subject\"，新增 multi-subject injection (k∈{1,3,5,10,20}) → ΔFPR<0.007 for k≤5 | ✅ 核心关切已回应，但仅 1 段，应扩展 |\n| R1-N2: 因果模糊性 / \"Instability\" framing | Title \"Psychometric Instability\" → \"Temporal Measurement Drift\"；Section 4.2 标题同步更改；Discussion 5.2 明确承认双向解读 | ✅ 充分回应 |\n| R1-N3: Bootstrap CI 不对称性 | 明确 \"B=1,000 model-level resamples\" | ⚠️ 部分回应（CI 不对称性原因仍未讨论） |\n| R1-W4/R2-N1: Claim 4 GSM1K 支撑不足 | Contributions 从 4 个缩减为 3 个，Claim 4 降级为 Discussion 5.3 exploratory evidence | ✅ 充分回应 |\n| R2-N2: 方法论新颖性 | 新增 \"LLM-specific challenges\" 段落（Method 3.2），讨论 local independence、fine-tuned variants、non-normal distribution、multidimensionality | ✅ 充分回应 |\n| R2-N3: Temporal cohort 粗糙 | Title 改善；Limitations 明确讨论；6-month window 仍为 one-liner | ⚠️ 部分回应 |\n| R2-W1: Audit protocol 过短 | 扩展为 graduated thresholds: <15% monitor, 15-25% flag, >25% act | ✅ 有改善 |\n| R2-W3: Running example | Method 3.2 新增具体 formal-logic item 示例（α_MH=0.42, Δ_MH=2.04） | ✅ 有效 |\n| R2-W4: Growing Pains 区分 | Related Work 扩展：\"Growing Pains assumes anchor item stability... Empirical comparison awaits public release\" | ⚠️ 合理但仍无定量比较 |\n| R2 Missing References | 新增 ATLAS (li2025atlas), MedIRT (luo2025medirt), BHI (zhu2026bhi), Benchmark² (qian2026benchmark2) | ✅ 全部补充 |\n\n---\n\n## 维度评分\n\n### Soundness: 4 / 5\n\n**MH-DIF 应用正确性**：公式 (1)-(2) 标准，K=5 quintile binning 符合 ETS 惯例，ETS C 分类（|Δ_MH|≥1.5 + p<0.05 双阈值）严格。Running example（formal-logic item, α_MH=0.42 → Δ_MH=2.04）帮助读者验证计算。\n\n**控制实验设计合理**：5 种 cohort design 系统排除替代解释——random split (0.18%) 排除噪声、ability-quintile (2.9%) 排除纯能力差异、within-family (61.3% → matched 28.3%) 展示 ability confounding 的影响、matched-ability (31.3% → 28.9%) 量化残余 ability effect（~2.4pp）。六种替代解释均被测试，收敛于 ~28-29% 的 floor，令人信服。\n\n**Proposition 1 修订得当**：限定为 \"under single-subject cross-subject matching\"，数学上 trivially true 但不再 overclaim。multi-subject injection boundary (ΔFPR<0.007 for k≤5) 是对 R1-N1 的直接回应，提供了方法适用边界的实证依据。\n\n**扣分原因**：\n(a) **缺少 permutation null**：random-split control (0.18%) 是 perfect null 条件下的估计，但不等于 permutation null。随机打乱 cohort labels 后的期望 C% 是什么？如果 permutation null 为 ~5%，则 \"effective\" DIF 应为 ~26% 而非 31%。这对 headline 数字的解读有实质影响。论文缺少这个分析。\n(b) **IRT model fit 未评估**：论文使用 2PL 参数做 power analysis（ā=1.2, b̄=-0.84），但未报告 model fit statistics（如 |Lz|, CFI, RMSEA）。MH-DIF 本身是非参数方法，不依赖 IRT fit——这点论文正确指出。但 MMLU 的 57 subjects 显然违反 unidimensionality，论文在 \"LLM-specific challenges\" 段中承认但未量化违反程度。\n(c) **binary flipping 的生态效度局限**：注入框架用 uniform rate p 翻转 incorrect→correct，真实 contamination 是非均匀的（部分 items 被完整记忆、部分仅记忆 answer letter、RLHF 创造非均匀效应）。论文应讨论对 non-uniform injection 的敏感性。\n\n### Reproducibility: 4 / 5\n\n**强项**：METABENCH 数据公开可获取、anonymous.4open.science 代码链接、power analysis 参数显式（\"empirical 2PL parameters from PSN-IRT: ā=1.2, b̄=-0.84; 14,042 MMLU items\"）、bootstrap 参数明确（B=1,000 model-level resamples）。\n\n**扣分**：multi-subject injection protocol 细节不足——k 的选择、每个 k 下的随机抽取策略、\"5 random draws each\" 的具体实现。Semi-synthetic 注入的 ETS A 选择标准（\"items classified as ETS A in the uninjected data\"）的确切阈值应明确。\n\n### Experimental Coverage: 3.5 / 5\n\n**Coverage Check（对照 Director 提供的 16 项实验清单）：**\n\n| # | 实验 | 状态 | 位置 |\n|---|---|---|---|\n| 1 | real_data_dif_mmlu | ✅ 完整 | §4.2 |\n| 2 | rl_robustness_validation | ❌ 不存在 | — |\n| 3 | constat_perturbation_eval | ⚠️ 提及但无专门分析 | §4.3 context |\n| 4 | dvd_generation_variance_eval | ❌ 不存在 | — |\n| 5 | ensemble_fusion | ❌ 不存在 | — |\n| 6 | cross_benchmark_gsm8k | ✅ 完整 | §4.7 |\n| 7 | bifactor_irt_equating_pilot | ❌ 不存在 | within-subject DIF 最近似 |\n| 8 | item_generation_calibration | ❌ 不存在 | — |\n| 9 | cumulative_bayesian_dif | ❌ 不存在 | — |\n| 10 | graceful_degradation_analysis | ⚠️ 隐含（ρ≈0.997） | §4.6 一句话 |\n| 11 | item_focused_trees | ❌ 不存在 | — |\n| 12 | architecture_stratified_dif | ⚠️ 部分 | Appendix A.2（99.98% decoder-only） |\n| 13 | semi_synthetic_contamination_validation | ✅ 完整 | §4.5 |\n| 14 | multi_benchmark_temporal_dif | ✅ 完整 | §4.7 |\n| 15 | permutation_null_c_rate | ❌ 不存在 | — |\n| 16 | odds_ratio_regression_transparency | ⚠️ 嵌入§4.2 | Simpson's paradox，OR 分析 |\n\n**4/16 完整覆盖，4/16 部分覆盖，8/16 不存在。** 但需注意这些是 \"imagined experiments\"——并非全部需要。对于 EMNLP 论文，已有的 7 个 experiment sections + 4 appendices 构成完整的故事。最关键的缺失是 **permutation null**（#15）和 **graceful degradation 的系统分析**（#10）。\n\n---\n\n## Director 具体问题回应\n\n### Q1: IRT 1D model misspecification\n\n论文未报告 |Lz| 或 CFI。如果 Director 所述的 \"98% |Lz|>2, CFI=0.72\" 属实，这表示 1D IRT 严重 misspecified。但论文的核心论点——MH-DIF 是非参数方法，不依赖 IRT model fit (Holland & Thayer, 1988)——是技术上正确的。论文在 §3.2 中提供了三层防护：(a) IRT θ 与 total score r=0.9986 → CTT-based stratification 无 bias；(b) 99.98% decoder-only → architecture 不是 confound；(c) cross-subject matching 处理 multidimensionality。\n\n**我的评估**：这三层防护对 MH-DIF 的有效性是 convincing 的——MH-DIF 的 conditional on observed score 性质使其对 latent structure misspecification 具有鲁棒性。但论文至少应报告 fit statistics（即使结论是\"不影响 MH-DIF\"），因为这是 transparent reporting 的要求。如果 CFI=0.72（远低于 0.95 conventional threshold），应在 Limitations 中讨论。\n\n### Q2: Binary flipping 的真实世界相关性\n\n显著局限。Uniform flipping at rate p 假设所有被污染 items 有相同的 exploitation probability，但真实 contamination 是 item-specific 的——更容易记忆的 items（如 factual recall）vs. 推理题，效果差异很大。论文应至少讨论 non-uniform injection (e.g., item-difficulty-dependent exploitation rate) 的 sensitivity，或将此列为 Limitations 而非仅隐含。\n\n当前 Limitations 段 \"Methodological scope\" 提到 \"DIF detects that... not why\" 但未讨论注入框架本身的简化。\n\n### Q3: Permutation null\n\n**论文中不存在 permutation null 分析。** 这是最显著的实验缺失。random-split (0.18%) 是 perfect null（同一 cohort 内部），ability-quintile (2.9%) 是 ability-only null。但 permutation null（随机打乱 temporal labels 后的 C%）才是 31.3% 的正确 baseline comparator。\n\n如果 permutation null ~5%（如 Director 摘要暗示），则：\n- \"effective\" temporal DIF = 31.3% - 5.2% = 26.1%\n- 论文标题中 \"31%\" 可能高估实际效应\n- 所有下游分析（downstream impact, cross-benchmark ratios）都需要调整\n\n**建议**：这是论文应补充的最重要实验。1,000 次 permutation 的计算成本很低。\n\n### Q4: GSM1K 负相关\n\n论文报告 r=-0.478（非 Director 所述 -0.35）, p=0.005, partial r=-0.385, p=0.027, N=33。\n\n修改后的处理**得当**：从 Contribution 列表中移除，降级为 Discussion 5.3 的 \"exploratory evidence\"，Limitations 明确标注 \"limited statistical power\"。N=33 确实无法支撑 firm conclusions，但作为 supplementary observation 是可接受的。\n\n### Q5: RL robustness\n\n论文中不存在。不是关键缺失——论文未声称对 RL post-training 的 robustness。\n\n### Q6: Cross-subject matching ΔFPR\n\n**这是修改最成功的部分。** Round 1 我将此列为 N1 (critical)，修改后：\n\n1. Proposition 1 明确限定为 \"single-subject injection\" → 不再 overclaim\n2. Multi-subject injection (k∈{1,3,5,10,20}) 提供了实证边界：ΔFPR<0.007 for k≤5 (<9% of domains)，k=10 (18%) 时 ΔFPR 升至 0.026-0.069\n3. Limitation 段明确：\"cross-subject matching assumes contamination affects a minority of domains; when contamination spans >10 subjects (>18% of MMLU), ΔFPR rises to 0.026-0.069\"\n\n**论点现在是 convincing 的**：single-subject 有数学保证，multi-subject 有实证边界和 graceful degradation，boundary condition 被明确陈述。唯一改进空间是将 multi-subject 结果从 1 段扩展为 table/figure。\n\n---\n\n## Strengths（≥3）\n\n1. **大规模、系统的 confound 控制**：5 种 cohort design × 6 种替代解释 × 4 个 threshold sensitivity 点，形成了对 31% DIF finding 的全方位 triangulation。matched-ability 分析收敛于 ~28-29% 的 floor（跨不同比较）尤其令人信服。\n\n2. **Ground truth meta-critique 具有社区价值**：Contribution 2 (enrichment=0.964, Jaccard=0.206) 对 contamination detection 文献中普遍使用 web-overlap labels 的做法提出了有实证支撑的质疑。Discussion 5.2 现在明确承认双向解读，增强了论证的诚实性。\n\n3. **Semi-synthetic 框架的 boundary characterization**：multi-subject injection 将框架从 \"trivially true by construction\" 升级为 \"empirically characterized with explicit boundary\"（k≤5 safe, k=10 degradation），这是对 Round 1 批评的高质量回应。\n\n4. **LLM-specific methodological adaptations**：新增的 \"LLM-specific challenges\" 段落（§3.2）不是泛泛之谈，而是针对 local independence (permutation simulation Q3=4.6-34.2%)、fine-tuned variant independence (graduated de-duplication)、non-normal ability (quintile-based stratification)、multidimensionality (cross-subject matching) 提出了具体应对措施。\n\n5. **Cross-benchmark replication at scale**：6 个 METABENCH benchmarks（27,125 items）的 DIF 发现具有一致性（knowledge/reasoning C%≥26.9% > procedural C%≤18.9%），且每个都远高于 random baseline (45-174×)。\n\n---\n\n## Weaknesses（≥3）\n\n1. **缺少 permutation null——headline 数字缺乏正确 baseline**：31.3% 是 raw C%，但无 permutation null 作为 baseline。random-split (0.18%) 是完美 null，不代表 realistic null（cohort 间存在微小系统差异的期望 DIF）。如果 permutation null ~5%，则 effective DIF ~26%，对标题和所有下游分析有实质影响。这是论文最关键的方法论缺失。\n\n2. **IRT model fit 未报告**：论文使用 2PL 参数做 power analysis 但不报告 fit statistics。MH-DIF 虽不依赖 IRT fit，但 transparent reporting 要求至少呈现 unidimensionality 评估（哪怕结论是\"MH-DIF 对此鲁棒\"）。如果 MMLU 确实 CFI=0.72，这是重要的 contextual information。\n\n3. **Binary flipping 简化未充分讨论**：注入框架使用 uniform rate p，真实 contamination 是 heterogeneous 的。这限制了 semi-synthetic 结果向真实场景的推广。当前 Limitations 未涉及此点。\n\n4. **Multi-subject injection 结果过于压缩**：这是论文回应 R1-N1 的核心新增实验，但仅占 Section 4.5 的 1.5 句话。k∈{1,3,5,10,20} 的 ΔFPR 值应以 table 或 figure 呈现，而非 inline text（\"ΔFPR<0.007 for k≤5; at k=10, ΔFPR rises to 0.026-0.069\"）。\n\n5. **Director 期望的实验覆盖缺口**：16 项计划实验中仅 4 项完整覆盖。特别缺失的 permutation null (#15)、graceful degradation 系统分析 (#10)、ConStat/DVD 专门对比 (#3/#4) 会加强论文。即使不全做，permutation null 是必须的。\n\n---\n\n## Questions to Authors（≥2）\n\n**Q1**：能否补充 permutation null 分析？具体来说：将 cohort labels (2023/2024) 随机打乱 1,000 次，每次重新计算 C%，报告 permutation null distribution 的 mean 和 95th percentile。这将为 31.3% 提供 principled baseline，并可能改变 headline 数字（从 31% 改为 null-adjusted 值）。\n\n**Q2**：论文声称 \"IRT θ estimates correlate at r=0.9986 with total scores\"（§3.2），但未报告 underlying IRT model 的 fit statistics。能否报告 MMLU 12,508 items 在 2PL 下的 CFI、RMSEA、或 |Lz| person-fit 分布？如果 fit 确实很差，这 paradoxically 支持论文的论点（MH-DIF 作为非参数方法是更安全的选择），但应 transparently 报告。\n\n**Q3**：multi-subject injection 的 boundary (k≤5 safe) 在 MMLU 语境中意味着什么？如果 real-world contamination 同时影响 >5 个 subjects（例如一个 model 训练时 ingest 了整个 MMLU dataset），cross-subject matching 的 ΔFPR 保证就失效了。论文如何论证 MMLU 的真实 contamination pattern 落在 k≤5 的安全区间内？\n\n---\n\n## Preliminary Overall Assessment\n\n**Overall: 3.5 / 5**（Borderline Conference）\n\n**Calibration rationale**：\n\n**3.5 而非 4.0 的原因**：\n- 缺少 permutation null 是重要的方法论缺失，直接影响 headline 数字的可信度\n- IRT fit 未报告降低了 methodological transparency\n- 多项计划实验未执行（虽然 \"imagined\" 不代表必须，但 permutation null 是标准做法）\n- Binary flipping 简化对 semi-synthetic 框架的 real-world relevance 有实质限制\n\n**3.5 而非 3.0 的原因**：\n- Round 1 的三个 critical issues (N1-N3) 均有实质性回应——title 改善、Proposition 1 限定、multi-subject boundary、bootstrap 单位明确\n- Confound 控制在 EMNLP 同类论文中属于上乘水平（5 cohort designs + 6 alternative explanations）\n- Ground truth meta-critique (Contribution 2) 对社区有独立价值\n- Cross-benchmark replication (6 benchmarks, 27,125 items) 提供了强 robustness\n- Writing quality 高，revised framing (\"drift\" not \"instability\") 更准确\n\n**升至 4.0 的路径**：\n1. 补充 permutation null → 提供 null-adjusted C% 作为 headline\n2. 报告 IRT fit statistics（即使结论不变）\n3. Multi-subject injection 结果以 table 呈现\n4. 在 Limitations 中增加 binary flipping 简化的讨论\n\n**结论**：论文从 Round 1 到 Round 2 的修改是认真且有效的，核心关切均有回应。但 permutation null 的缺失使 headline 数字的解读存在不确定性，阻止了评分升至 Conference accept。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-21T17:48:12.274948+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4172
}
```

</details>

---


### Assistant

_source line 264 · 2026-05-21T17:48:21.352830+00:00_

审稿意见已提交。

核心发现：论文从 Round 1 到本版做了实质性修改（title 改善、Proposition 1 限定、multi-subject injection、LLM-specific challenges 段落、Claim 4 降级），回应了 R1/R2 的主要关切。但实际论文内容与 Director 提供的 Paper Summary 存在显著差异——16 项计划实验中仅 4 项完整覆盖，最关键的缺失是 permutation null 分析。评分维持 Overall 3.5 (Borderline Conference)，核心阻碍是 headline "31%" 缺乏 permutation null baseline。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 10

## Round 10

4 recorded events


### User

_source line 265 · 2026-05-21T17:48:22.415647+00:00_

[Round 1 审稿请求]:
## Step 2: Cross-Share — R2's Findings for Your Consideration

R2 (Novelty & Related Work) has completed independent review. Here are their key findings for you to consider before the convergence round:

### R2's Preliminary Scores
- Novelty/Excitement: 2.5/5
- Significance: 3.5/5
- Clarity/Writing: 3.0/5
- Related work: 2.5/5
- **Preliminary Overall: 3.0**

### R2's Key Concerns

1. **"Known method → new domain" novelty ceiling**: MH-DIF is textbook psychometrics (35+ years). The novelty rests on showing it reveals something interesting at LLM scale plus the semi-synthetic framework. R2 questions whether application novelty alone is sufficient for EMNLP Main.

2. **Scope too broad, depth too shallow**: 11 experiment sections + 5 appendices in 12 pages. Many analyses get only 1 paragraph. Reads more like a technical report than a focused conference paper. ConStat, DVD, odds ratio regression, and IFT could be condensed without losing core contribution.

3. **Thin related work**: Only 10 references. Missing IRT-for-LLM-evaluation literature, benchmark reform papers, computerized adaptive testing DIF work, and additional contamination detection methods. 3 paragraphs of related work is insufficient.

4. **Meta-critique depth**: Contribution 2 (web-overlap labels can't validate item-level differential detectors) is conceptually stated but not deeply developed. ConStat/DVD failure analysis is surface-level AUROC numbers without probing *why* these methods fail at a deeper level.

### R2's Strengths Noted
- Timely and practically relevant topic
- Clear "instability ≠ invalidity" framing is a needed message
- Semi-synthetic framework has standalone reusable value
- Honest, thorough empirical work with negative results reported

### Questions for R1 to Consider
- Does the methodological rigor compensate for limited novelty?
- Is the broad experimental scope a strength (thoroughness) or weakness (dilution)?
- Does the semi-synthetic framework alone justify conference-level contribution?

Please incorporate R2's perspective and revise your assessment if warranted. Focus on where you agree/disagree with R2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-21T17:49:51.786005+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 — 对 R2 Round 2 意见\n\n### ⚠️ 前置说明：R2 与我可能在审不同版本\n\nR2 描述的论文（\"11 experiment sections + 5 appendices\"，\"Only 10 references\"，\"3 paragraphs of related work\"）与我实际读到的 PDF 有显著差异。**我读到的论文**有 7 个 experiment sections、4 appendices、~60 篇引用、4 段 Related Work（Contamination Detection / IRT in LLM Evaluation / DIF Methodology / Benchmark Quality）。以下回应基于我实际读到的版本。\n\n---\n\n### 逐条回应 R2 Key Concerns\n\n**[REBUT] R2-Concern-1: \"Known method → new domain\" novelty ceiling → Novelty 2.5/5**\n\nR2 认为 MH-DIF 是 35+ 年的 textbook method，application novelty 不足以支撑 EMNLP Main。我不同意将 novelty 评为 2.5。理由：\n\n1. **论文已明确 self-position 为 empirical + methodological contribution**（Introduction: \"Our contributions are methodological and empirical, not algorithmic\"）。以 \"算法新颖性\" 标准评判一篇明确声明 \"不是算法贡献\" 的论文是 criteria mismatch。\n\n2. **\"Known method → new domain\" 在 EMNLP 有先例且被接受**：Rodriguez et al. (2021, ACL) 将 IRT 应用于 NLP leaderboards——同样是 \"old psychometric method → NLP evaluation\"——被 ACL main 接收。Vania et al. (2021, ACL) 用 IRT 比较 test sets，同样获 ACL main。关键不在方法是否新，而在 findings 是否 non-trivial。\n\n3. **Non-trivial findings 确实存在**：\n   - 31% temporal DIF 在 12,508 items × 5,227 models 上的发现是 previously unknown 的实证事实\n   - Ground truth meta-critique（enrichment=0.964）揭示了 contamination detection 文献的 systematic evaluation flaw\n   - Semi-synthetic 框架的 multi-subject boundary (k≤5 safe, k=10 degradation) 是 reusable methodological contribution\n   \n4. **\"LLM-specific challenges\" 段落（§3.2）展示了 non-trivial adaptation**：permutation simulation for LD (Q3=4.6-34.2%)、graduated de-duplication for family structure、quintile-based stratification for non-normal ability——这些不是 trivial transplant。\n\n**我的评分**：Excitement 3.5/5（维持不变）。novelty ceiling 确实存在但被 empirical significance 和 methodological adaptation 弥补。\n\n---\n\n**[AGREE with nuance] R2-Concern-2: Scope too broad, depth too shallow**\n\n如果 R2 审的版本确实有 11 个 experiment sections + 5 appendices，我同意 breadth > depth 是问题。但**我读到的版本**更聚焦：7 个 experiment sections（§4.1-4.7），核心故事清晰——temporal DIF (§4.2) → ground truth mismatch (§4.3) → structural controls (§4.4) → semi-synthetic validation (§4.5) → downstream impact (§4.6) → cross-benchmark (§4.7)。\n\n**我同意的部分**：即使在当前版本中，某些分析仍然过于压缩：\n- Multi-subject injection (§4.5)：k∈{1,3,5,10,20} 的关键结果只有 1.5 句话，没有 table 或 figure\n- Downstream impact (§4.6)：多个统计量（ρ≈0.997, z=-8σ to -49σ, cohort gap=96.2）密集堆叠在一段中\n- 6-month window 分析（§4.7 最后一段）：仅 one-liner\n\n**但我不同意 \"technical report\" 的判断**。论文有清晰的叙事弧（diagnostic lens, not quality filter）和 well-structured contributions。问题不是 scope 太广，而是某些关键新增实验（特别是 multi-subject injection）的 presentation 不够 prominent。\n\n---\n\n**[REBUT] R2-Concern-3: Thin related work (only 10 references, 3 paragraphs)**\n\n**这与我读到的论文严重不符。** 实际 Related Work（§2）包含：\n- **Paragraph 1 (Contamination Detection)**：11 citations（Min-K%, Min-K%++, Time Travel, ConStat, DVD, Self-Critique, Balloccu, Li et al., Carlini, Tirumala, Wang et al.）\n- **Paragraph 2 (IRT in LLM Evaluation)**：11 citations（Lalor, Vania, Rodriguez, PSN-IRT, TinyBenchmarks, Hardy, ATLAS, MedIRT, Growing Pains, Kim FPC）\n- **Paragraph 3 (DIF Methodology)**：14 citations（Holland, Clauser, Swaminathan, SIBTEST, Lord, Raju, Zumbo, Meredith, Vandenberg, MIMIC, Woods, Teresi, Nandakumar, Donoghue, Belzak）\n- **Paragraph 4 (Benchmark Quality)**：8 citations（BHI, Benchmark², Maeda, Dynabench, LatestEval, LiveBench, Chatbot Arena, Chang survey, Burnell）\n\n总计 ~44 unique citations in Related Work alone，总引用 ~60 篇。这不是 \"thin\"——覆盖了 contamination detection、IRT-for-LLM、DIF methodology、benchmark reform 四个维度。\n\n如果 R2 审的是一个早期版本（修改前只有 ~10 references），则这条 concern 已被修改充分回应。\n\n---\n\n**[AGREE] R2-Concern-4: Meta-critique depth**\n\n同意 Contribution 2 的深度可以更好。当前论文证明了 near-independence（enrichment=0.964, Jaccard=0.206, φ=0.012），Discussion 5.2 承认了双向解读。但分析止步于 \"category error\"——为什么 web-overlap labels 和 DIF 正交？论文给出的解释是 \"global exposure vs. differential functioning\"（Figure 1），这在概念层面有效，但缺乏对 **哪些 item 特征** 导致 web-overlap=contaminated + DIF=clean（或反过来）的深入分析。\n\n一个简单的 improvement：对 4 个象限（web-contaminated × DIF-flagged 的 2×2）做 item characteristic analysis（difficulty, discrimination, subject distribution），看是否有 systematic pattern。这会将 \"conceptual category error\" 升级为 \"empirically grounded category error\"。\n\n---\n\n### R2 提出的三个 meta-questions\n\n**Q: Does the methodological rigor compensate for limited novelty?**\n\n**是的，在一定程度上。** EMNLP 近年接收的 analysis/empirical papers 表明社区认可 \"rigorous application of known methods revealing non-obvious findings\"。关键是 findings 是否 actionable：\n- 31% temporal DIF → motivates psychometric monitoring（actionable）\n- Ground truth meta-critique → challenges evaluation methodology of contamination detectors（actionable）\n- Semi-synthetic framework → reusable tool（actionable）\n\n但如果 permutation null 表明 effective DIF 仅 ~26% 而非 31%，actionability 不变但 headline 需要调整。\n\n**Q: Is the broad experimental scope a strength (thoroughness) or weakness (dilution)?**\n\n**在当前版本中是 strength**（7 sections，叙事清晰）。但 presentation 的 unevenness（multi-subject injection 只有 1.5 句，downstream impact 信息过密）使部分 thoroughness 被压缩成了 density。解决方案不是删减实验，而是重新分配 space——压缩 ground truth mismatch（§4.3，当前一整段重复 near-independence 的多个统计量），扩展 multi-subject injection 和 downstream impact。\n\n**Q: Does the semi-synthetic framework alone justify conference-level contribution?**\n\n**单独不够，但作为 3 个 contributions 之一是 sufficient。** Semi-synthetic 框架 + multi-subject boundary 是 reusable methodological contribution，但需要 empirical findings（31% DIF）和 meta-critique 作为 motivation 和 validation。三者组合构成 conference-level package。\n\n---\n\n### 综合评估：是否调整我的评分？\n\n**维持 Overall 3.5**，但对 sub-dimensions 有微调：\n\n| 维度 | 我的评分 | R2 评分 | 综合后 |\n|---|---|---|---|\n| Soundness | 4.0 | — | 4.0（维持）|\n| Excitement / Novelty | 3.5 | 2.5 | 3.0（下调 0.5）|\n| Reproducibility | 4.0 | — | 4.0（维持）|\n| Clarity | 4.0 | 3.0 | 3.5（下调 0.5）|\n| Overall | 3.5 | 3.0 | **3.5**（维持）|\n\n**下调 Excitement 至 3.0 的理由**：R2 的 novelty ceiling 论点有合理性——MH-DIF 确实是 well-known method，cross-subject matching 在 psychometrics 中有先例。论文的价值更多来自 **scale + findings** 而非 **method innovation**。3.0 = \"might discuss certain points; would attend if time permits\"——对一篇 rigorous application paper 是合理定位。\n\n**下调 Clarity 至 3.5 的理由**：R2 指出的 scope/depth 不平衡（某些分析过于压缩）在我的审稿中也有体现（multi-subject injection 1.5 句，downstream impact 信息过密）。但 overall writing quality 高于 3.0——叙事弧清晰、Figure 1 有效、running example 有帮助。\n\n**维持 Overall 3.5 的理由**：\n- 缺少 permutation null 阻止升至 4.0（方法论完整性的硬伤）\n- Soundness 4.0 + 大规模 empirical replication + responsive revision 阻止降至 3.0\n- Borderline Conference = \"可能值得 main conference，但有可修复的缺陷\"——准确描述当前状态\n\n**与 R2 的分歧 summary**：\n- Novelty：R2 = 2.5，我 = 3.0（我认为 LLM-specific adaptations 和 empirical significance 弥补了 method novelty ceiling）\n- Related Work：R2 = 2.5，我认为实际论文的 Related Work 是 adequate（~44 citations，4 paragraphs）——**如果 R2 审的是不同版本，这条 concern 可能已 obsolete**\n- Overall：R2 = 3.0，我 = 3.5（主要因为我对 confound 控制的评价更高）",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 — 对 R2 Round 2 意见\n\n### ⚠️ 前置说明：R2 与我可能在审不同版本\n\nR2 描述的论文（\"11 experiment sections + 5 appendices\"，\"Only 10 references\"，\"3 paragraphs of related work\"）与我实际读到的 PDF 有显著差异。**我读到的论文**有 7 个 experiment sections、4 appendices、~60 篇引用、4 段 Related Work（Contamination Detection / IRT in LLM Evaluation / DIF Methodology / Benchmark Quality）。以下回应基于我实际读到的版本。\n\n---\n\n### 逐条回应 R2 Key Concerns\n\n**[REBUT] R2-Concern-1: \"Known method → new domain\" novelty ceiling → Novelty 2.5/5**\n\nR2 认为 MH-DIF 是 35+ 年的 textbook method，application novelty 不足以支撑 EMNLP Main。我不同意将 novelty 评为 2.5。理由：\n\n1. **论文已明确 self-position 为 empirical + methodological contribution**（Introduction: \"Our contributions are methodological and empirical, not algorithmic\"）。以 \"算法新颖性\" 标准评判一篇明确声明 \"不是算法贡献\" 的论文是 criteria mismatch。\n\n2. **\"Known method → new domain\" 在 EMNLP 有先例且被接受**：Rodriguez et al. (2021, ACL) 将 IRT 应用于 NLP leaderboards——同样是 \"old psychometric method → NLP evaluation\"——被 ACL main 接收。Vania et al. (2021, ACL) 用 IRT 比较 test sets，同样获 ACL main。关键不在方法是否新，而在 findings 是否 non-trivial。\n\n3. **Non-trivial findings 确实存在**：\n   - 31% temporal DIF 在 12,508 items × 5,227 models 上的发现是 previously unknown 的实证事实\n   - Ground truth meta-critique（enrichment=0.964）揭示了 contamination detection 文献的 systematic evaluation flaw\n   - Semi-synthetic 框架的 multi-subject boundary (k≤5 safe, k=10 degradation) 是 reusable methodological contribution\n   \n4. **\"LLM-specific challenges\" 段落（§3.2）展示了 non-trivial adaptation**：permutation simulation for LD (Q3=4.6-34.2%)、graduated de-duplication for family structure、quintile-based stratification for non-normal ability——这些不是 trivial transplant。\n\n**我的评分**：Excitement 3.5/5（维持不变）。novelty ceiling 确实存在但被 empirical significance 和 methodological adaptation 弥补。\n\n---\n\n**[AGREE with nuance] R2-Concern-2: Scope too broad, depth too shallow**\n\n如果 R2 审的版本确实有 11 个 experiment sections + 5 appendices，我同意 breadth > depth 是问题。但**我读到的版本**更聚焦：7 个 experiment sections（§4.1-4.7），核心故事清晰——temporal DIF (§4.2) → ground truth mismatch (§4.3) → structural controls (§4.4) → semi-synthetic validation (§4.5) → downstream impact (§4.6) → cross-benchmark (§4.7)。\n\n**我同意的部分**：即使在当前版本中，某些分析仍然过于压缩：\n- Multi-subject injection (§4.5)：k∈{1,3,5,10,20} 的关键结果只有 1.5 句话，没有 table 或 figure\n- Downstream impact (§4.6)：多个统计量（ρ≈0.997, z=-8σ to -49σ, cohort gap=96.2）密集堆叠在一段中\n- 6-month window 分析（§4.7 最后一段）：仅 one-liner\n\n**但我不同意 \"technical report\" 的判断**。论文有清晰的叙事弧（diagnostic lens, not quality filter）和 well-structured contributions。问题不是 scope 太广，而是某些关键新增实验（特别是 multi-subject injection）的 presentation 不够 prominent。\n\n---\n\n**[REBUT] R2-Concern-3: Thin related work (only 10 references, 3 paragraphs)**\n\n**这与我读到的论文严重不符。** 实际 Related Work（§2）包含：\n- **Paragraph 1 (Contamination Detection)**：11 citations（Min-K%, Min-K%++, Time Travel, ConStat, DVD, Self-Critique, Balloccu, Li et al., Carlini, Tirumala, Wang et al.）\n- **Paragraph 2 (IRT in LLM Evaluation)**：11 citations（Lalor, Vania, Rodriguez, PSN-IRT, TinyBenchmarks, Hardy, ATLAS, MedIRT, Growing Pains, Kim FPC）\n- **Paragraph 3 (DIF Methodology)**：14 citations（Holland, Clauser, Swaminathan, SIBTEST, Lord, Raju, Zumbo, Meredith, Vandenberg, MIMIC, Woods, Teresi, Nandakumar, Donoghue, Belzak）\n- **Paragraph 4 (Benchmark Quality)**：8 citations（BHI, Benchmark², Maeda, Dynabench, LatestEval, LiveBench, Chatbot Arena, Chang survey, Burnell）\n\n总计 ~44 unique citations in Related Work alone，总引用 ~60 篇。这不是 \"thin\"——覆盖了 contamination detection、IRT-for-LLM、DIF methodology、benchmark reform 四个维度。\n\n如果 R2 审的是一个早期版本（修改前只有 ~10 references），则这条 concern 已被修改充分回应。\n\n---\n\n**[AGREE] R2-Concern-4: Meta-critique depth**\n\n同意 Contribution 2 的深度可以更好。当前论文证明了 near-independence（enrichment=0.964, Jaccard=0.206, φ=0.012），Discussion 5.2 承认了双向解读。但分析止步于 \"category error\"——为什么 web-overlap labels 和 DIF 正交？论文给出的解释是 \"global exposure vs. differential functioning\"（Figure 1），这在概念层面有效，但缺乏对 **哪些 item 特征** 导致 web-overlap=contaminated + DIF=clean（或反过来）的深入分析。\n\n一个简单的 improvement：对 4 个象限（web-contaminated × DIF-flagged 的 2×2）做 item characteristic analysis（difficulty, discrimination, subject distribution），看是否有 systematic pattern。这会将 \"conceptual category error\" 升级为 \"empirically grounded category error\"。\n\n---\n\n### R2 提出的三个 meta-questions\n\n**Q: Does the methodological rigor compensate for limited novelty?**\n\n**是的，在一定程度上。** EMNLP 近年接收的 analysis/empirical papers 表明社区认可 \"rigorous application of known methods revealing non-obvious findings\"。关键是 findings 是否 actionable：\n- 31% temporal DIF → motivates psychometric monitoring（actionable）\n- Ground truth meta-critique → challenges evaluation methodology of contamination detectors（actionable）\n- Semi-synthetic framework → reusable tool（actionable）\n\n但如果 permutation null 表明 effective DIF 仅 ~26% 而非 31%，actionability 不变但 headline 需要调整。\n\n**Q: Is the broad experimental scope a strength (thoroughness) or weakness (dilution)?**\n\n**在当前版本中是 strength**（7 sections，叙事清晰）。但 presentation 的 unevenness（multi-subject injection 只有 1.5 句，downstream impact 信息过密）使部分 thoroughness 被压缩成了 density。解决方案不是删减实验，而是重新分配 space——压缩 ground truth mismatch（§4.3，当前一整段重复 near-independence 的多个统计量），扩展 multi-subject injection 和 downstream impact。\n\n**Q: Does the semi-synthetic framework alone justify conference-level contribution?**\n\n**单独不够，但作为 3 个 contributions 之一是 sufficient。** Semi-synthetic 框架 + multi-subject boundary 是 reusable methodological contribution，但需要 empirical findings（31% DIF）和 meta-critique 作为 motivation 和 validation。三者组合构成 conference-level package。\n\n---\n\n### 综合评估：是否调整我的评分？\n\n**维持 Overall 3.5**，但对 sub-dimensions 有微调：\n\n| 维度 | 我的评分 | R2 评分 | 综合后 |\n|---|---|---|---|\n| Soundness | 4.0 | — | 4.0（维持）|\n| Excitement / Novelty | 3.5 | 2.5 | 3.0（下调 0.5）|\n| Reproducibility | 4.0 | — | 4.0（维持）|\n| Clarity | 4.0 | 3.0 | 3.5（下调 0.5）|\n| Overall | 3.5 | 3.0 | **3.5**（维持）|\n\n**下调 Excitement 至 3.0 的理由**：R2 的 novelty ceiling 论点有合理性——MH-DIF 确实是 well-known method，cross-subject matching 在 psychometrics 中有先例。论文的价值更多来自 **scale + findings** 而非 **method innovation**。3.0 = \"might discuss certain points; would attend if time permits\"——对一篇 rigorous application paper 是合理定位。\n\n**下调 Clarity 至 3.5 的理由**：R2 指出的 scope/depth 不平衡（某些分析过于压缩）在我的审稿中也有体现（multi-subject injection 1.5 句，downstream impact 信息过密）。但 overall writing quality 高于 3.0——叙事弧清晰、Figure 1 有效、running example 有帮助。\n\n**维持 Overall 3.5 的理由**：\n- 缺少 permutation null 阻止升至 4.0（方法论完整性的硬伤）\n- Soundness 4.0 + 大规模 empirical replication + responsive revision 阻止降至 3.0\n- Borderline Conference = \"可能值得 main conference，但有可修复的缺陷\"——准确描述当前状态\n\n**与 R2 的分歧 summary**：\n- Novelty：R2 = 2.5，我 = 3.0（我认为 LLM-specific adaptations 和 empirical significance 弥补了 method novelty ceiling）\n- Related Work：R2 = 2.5，我认为实际论文的 Related Work 是 adequate（~44 citations，4 paragraphs）——**如果 R2 审的是不同版本，这条 concern 可能已 obsolete**\n- Overall：R2 = 3.0，我 = 3.5（主要因为我对 confound 控制的评价更高）",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-21T17:49:55.504026+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3718
}
```

</details>

---


### Assistant

_source line 268 · 2026-05-21T17:50:01.613643+00:00_

审稿交叉回应已提交。

核心结论：维持 Overall 3.5。同意 R2 的 novelty ceiling 论点（Excitement 从 3.5 下调至 3.0），但反驳 R2 关于 Related Work "only 10 references" 的批评——实际论文有 ~60 篇引用和 4 段充实的 Related Work，R2 可能审的是不同版本。最关键的共识是 permutation null 的缺失阻止评分升至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 11

## Round 11

4 recorded events


### User

_source line 269 · 2026-05-21T17:50:02.700855+00:00_

[Round 1 审稿请求]:
## Step 3: Convergence Round

Both reviews are in. Here is the synthesis for convergence:

### Areas of Agreement (both R1 and R2)
1. **Cross-subject matching is the strongest contribution** — ΔFPR<0.001 vs +0.19 is a clean, important methodological innovation.
2. **Paper scope is too broad** — 11 experiment sections in 8 pages of main text dilutes the core message. Several analyses (ConStat, DVD, odds ratio, IFT) could be condensed.
3. **Related work is insufficient** — 10 references and 3 paragraphs don't adequately cover the relevant literatures.
4. **IRT misspecification is a real concern, partially addressed** — The three bounding arguments are reasonable but not definitive. Direction of findings is likely robust, magnitudes less certain.
5. **Honest reporting is appreciated** — Negative results (RL robustness, bifactor, item generation, GSM1K) reported transparently.
6. **Novelty is limited** — "Known method → new domain" with the semi-synthetic framework providing incremental but genuine novelty.
7. **Semi-synthetic detection power is moderate** — ΔTPR=0.37 at p=0.5 is meaningful but not strong; binary flipping is a simplification.

### Areas of Tension
- R1 (3.0–3.5 initially) values methodological thoroughness more; R2 (3.0 initially) weighs novelty more heavily.
- R1 sees broad scope as experimental coverage strength (4.5/5); R2 sees it as narrative dilution.
- R1 rates the IRT misspecification as the biggest concern; R2 rates the novelty ceiling as the biggest concern.

### Convergence Questions
1. Does this paper change how the community evaluates LLM benchmarks in practice? (Both lean yes, but incrementally)
2. Is the semi-synthetic framework alone sufficient for conference-level novelty? (Both lean: borderline)
3. What's the appropriate venue — Main or Findings? (Both lean Findings)

### Final Score Calibration
Against EMNLP 2026 acceptance rates (~21% Main):
- The paper is not in the top 20% of NLP submissions by novelty or impact
- It is a solid, thorough, methodologically careful empirical study
- The semi-synthetic framework has lasting value as reusable infrastructure
- A major revision (focus scope, expand related work, deepen semi-synthetic framework) could push toward conference acceptance

Please confirm or adjust your final assessment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-21T17:51:00.276279+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Convergence Round 最终评估\n\n---\n\n### 对 Synthesis 的回应\n\nDirector 的 synthesis 存在一个根本性问题：**它描述的论文与我读到的 PDF 不一致。** 我需要在回应前再次澄清：\n\n| Synthesis 描述 | 实际 PDF |\n|---|---|\n| 11 experiment sections in 8 pages | 7 experiment sections (§4.1-4.7) |\n| 10 references, 3 paragraphs related work | ~60 references, 4 paragraphs (~44 unique citations in §2) |\n| ConStat, DVD, odds ratio, IFT sections | ConStat/DVD 仅在 §4.3 context 中提及；odds ratio 嵌入 §4.2；无 IFT 专节 |\n| RL robustness, bifactor, item generation 负面结果 | 均不存在于论文中 |\n| ΔTPR=0.37 at p=0.5 | ΔTPR=+0.508 at p=0.5 |\n| IRT misspecification (98% \\|Lz\\|>2, CFI=0.72) | 未报告 |\n\n**我的最终评估基于实际论文内容。** 如果 Director 和 R2 审的是另一个版本，我们的评分差异部分源于版本差异而非审稿判断差异。\n\n---\n\n### Areas of Agreement — 我的确认/修正\n\n**1. Cross-subject matching 是最强贡献** → ✅ 完全同意。Proposition 1（properly scoped to single-subject）+ multi-subject boundary（ΔFPR<0.007 for k≤5）是 clean, reusable methodological contribution。\n\n**2. Paper scope 过广** → ⚠️ 部分同意。在我读到的版本中（7 sections, not 11），scope 是 manageable 的。但某些分析确实过于压缩（multi-subject injection 1.5 句，downstream impact 信息密度过高）。问题不是 \"too many experiments\" 而是 \"space allocation uneven\"。\n\n**3. Related work 不足** → ❌ 不同意（基于实际 PDF）。实际论文有 4 段 Related Work，覆盖 contamination detection（11 citations）、IRT in LLM evaluation（11 citations, 含 ATLAS, MedIRT, Growing Pains）、DIF methodology（14 citations）、benchmark quality（8 citations, 含 BHI, Benchmark²）。如果 R2 审的早期版本确实只有 10 references，这条 concern 在当前版本中已 resolved。\n\n**4. IRT misspecification** → ⚠️ 无法确认。实际论文未报告 |Lz| 或 CFI。论文主张 MH-DIF 是非参数方法不依赖 IRT fit，技术上正确。我认为论文应报告 fit statistics（transparent reporting），但这不构成 critical flaw。\n\n**5. Honest reporting** → ⚠️ 无法确认。论文中没有 RL robustness、bifactor、item generation 的负面结果。GSM1K 的 exploratory status 确实被 honestly scoped。\n\n**6. Novelty limited** → ✅ 同意。与 R2 的交叉回应后我将 Excitement 下调至 3.0。\n\n**7. Semi-synthetic detection power moderate** → ⚠️ 数字不一致。实际论文报告 ΔTPR=+0.508 at p=0.5（非 0.37）。+0.508 是 meaningful detection power。但 binary flipping 确实是 simplification。\n\n---\n\n### Convergence Questions 回应\n\n**Q1: Does this paper change how the community evaluates LLM benchmarks in practice?**\n\n**Yes, incrementally but meaningfully.** 具体的 practical impact：\n- Ground truth meta-critique 直接改变 contamination detection 的 evaluation methodology（不应仅用 web-overlap labels 验证 differential detectors）\n- DIF audit protocol（§5.4 graduated thresholds: <15% monitor / 15-25% flag / >25% act）提供了 actionable guideline\n- 31% 这个数字本身会影响社区对 MMLU 等 benchmark 的信心（即使只是 diagnostic，不是 destructive）\n\n但 impact 是 incremental 而非 transformative——论文不提出新 benchmark 或新 evaluation paradigm，而是对现有 benchmark 增加一个 monitoring dimension。\n\n**Q2: Is the semi-synthetic framework alone sufficient for conference-level novelty?**\n\n**单独不够，但作为 package 的一部分是 sufficient。** 框架本身（cross-subject matching + multi-subject boundary characterization）是 reusable infrastructure，但需要 empirical findings 和 meta-critique 提供 motivation。三者的组合是否达到 conference level 取决于对 \"application paper\" 的接受标准。\n\n**Q3: What's the appropriate venue — Main or Findings?**\n\n**Findings，with a path to Main if permutation null is added。**\n\n理由：\n- **For Main (21% acceptance)**：需要 novelty + significance + soundness 全面过线。novelty 明确受限（known method → new domain），significance 虽高但 headline 数字（31%）缺少 permutation null 校准。\n- **For Findings**：solid empirical contribution + reusable methodological framework + community-relevant meta-critique = Findings 的 sweet spot。\n\n---\n\n### 最终评分\n\n| 维度 | 最终评分 | 变化 | 理由 |\n|---|---|---|---|\n| Soundness | 4.0 / 5 | 维持 | MH-DIF 应用正确，controls 充分，multi-subject boundary 是 genuine improvement |\n| Excitement | 3.0 / 5 | 从 3.5 下调 | 采纳 R2 novelty ceiling 论点；application paper ceiling |\n| Reproducibility | 4.0 / 5 | 维持 | Public data, code, explicit parameters |\n| Clarity | 3.5 / 5 | 从 4.0 下调 | Space allocation uneven（某些关键分析过于压缩） |\n| Reviewer Confidence | 4 / 5 | 维持 | 熟悉 DIF 方法论和 LLM evaluation 文献 |\n\n**Overall: 3.5 / 5 → Findings 接收**\n\n---\n\n### Calibration Rationale\n\n**3.5 = Borderline Conference / Findings accept。**\n\n按 EMNLP 2026 标准：\n- 5 = Award (top 2.5%)：不适用\n- 4.5 = Borderline Award：不适用\n- 4 = Conference accept：需要 novelty or significance 显著高于当前水平\n- **3.5 = Borderline Conference**：当前位置\n- **3 = Findings accept**：如果不修改 permutation null\n\n**维持 3.5 而非调整的逻辑**：\n\n- **不升至 4.0**：(a) 缺少 permutation null → headline 数字未校准；(b) novelty ceiling（R1+R2 共识）；(c) binary flipping 对 semi-synthetic real-world relevance 的限制\n- **不降至 3.0**：(a) Round 1 → Round 2 的修改质量高且 responsive（title 改善、Proposition 1 限定、multi-subject boundary、bootstrap 明确、Claim 4 降级、Related Work 大幅扩充）；(b) confound 控制在同类论文中 above average；(c) Soundness 4.0 不应被 novelty concern 完全抵消\n\n**与 R2 的最终分歧**：R2 Overall 3.0，我 3.5。差距 0.5 主要来自：\n1. Related Work 评估不同（R2 说 10 refs / 3 paragraphs，我读到 ~60 refs / 4 paragraphs）\n2. Soundness 权重不同（我更重视 confound 控制的系统性）\n3. 版本差异可能导致部分评分基础不同\n\n**建议 Director**：如果 R2 审的是不同版本，应请 R2 重新审阅当前 PDF 后再做最终 convergence。当前版本对 Round 1 问题的回应质量值得被 credit。\n\n---\n\n### 给作者的总结建议（如果进入 camera-ready）\n\n**必须做：**\n1. 补充 permutation null（1,000 permutations，随机打乱 cohort labels），报告 null-adjusted C%\n2. Multi-subject injection 结果以 table/figure 呈现（当前只有 inline text）\n3. 报告 IRT model fit statistics（|Lz|, CFI——即使结论不变）\n\n**建议做：**\n4. 在 Limitations 中增加 binary flipping 简化的讨论\n5. 压缩 §4.3 Ground Truth Mismatch（多个 near-independence 统计量有冗余），扩展 §4.5 Semi-synthetic 和 §4.6 Downstream\n6. 讨论 bootstrap CI 不对称性的来源",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Convergence Round 最终评估\n\n---\n\n### 对 Synthesis 的回应\n\nDirector 的 synthesis 存在一个根本性问题：**它描述的论文与我读到的 PDF 不一致。** 我需要在回应前再次澄清：\n\n| Synthesis 描述 | 实际 PDF |\n|---|---|\n| 11 experiment sections in 8 pages | 7 experiment sections (§4.1-4.7) |\n| 10 references, 3 paragraphs related work | ~60 references, 4 paragraphs (~44 unique citations in §2) |\n| ConStat, DVD, odds ratio, IFT sections | ConStat/DVD 仅在 §4.3 context 中提及；odds ratio 嵌入 §4.2；无 IFT 专节 |\n| RL robustness, bifactor, item generation 负面结果 | 均不存在于论文中 |\n| ΔTPR=0.37 at p=0.5 | ΔTPR=+0.508 at p=0.5 |\n| IRT misspecification (98% \\|Lz\\|>2, CFI=0.72) | 未报告 |\n\n**我的最终评估基于实际论文内容。** 如果 Director 和 R2 审的是另一个版本，我们的评分差异部分源于版本差异而非审稿判断差异。\n\n---\n\n### Areas of Agreement — 我的确认/修正\n\n**1. Cross-subject matching 是最强贡献** → ✅ 完全同意。Proposition 1（properly scoped to single-subject）+ multi-subject boundary（ΔFPR<0.007 for k≤5）是 clean, reusable methodological contribution。\n\n**2. Paper scope 过广** → ⚠️ 部分同意。在我读到的版本中（7 sections, not 11），scope 是 manageable 的。但某些分析确实过于压缩（multi-subject injection 1.5 句，downstream impact 信息密度过高）。问题不是 \"too many experiments\" 而是 \"space allocation uneven\"。\n\n**3. Related work 不足** → ❌ 不同意（基于实际 PDF）。实际论文有 4 段 Related Work，覆盖 contamination detection（11 citations）、IRT in LLM evaluation（11 citations, 含 ATLAS, MedIRT, Growing Pains）、DIF methodology（14 citations）、benchmark quality（8 citations, 含 BHI, Benchmark²）。如果 R2 审的早期版本确实只有 10 references，这条 concern 在当前版本中已 resolved。\n\n**4. IRT misspecification** → ⚠️ 无法确认。实际论文未报告 |Lz| 或 CFI。论文主张 MH-DIF 是非参数方法不依赖 IRT fit，技术上正确。我认为论文应报告 fit statistics（transparent reporting），但这不构成 critical flaw。\n\n**5. Honest reporting** → ⚠️ 无法确认。论文中没有 RL robustness、bifactor、item generation 的负面结果。GSM1K 的 exploratory status 确实被 honestly scoped。\n\n**6. Novelty limited** → ✅ 同意。与 R2 的交叉回应后我将 Excitement 下调至 3.0。\n\n**7. Semi-synthetic detection power moderate** → ⚠️ 数字不一致。实际论文报告 ΔTPR=+0.508 at p=0.5（非 0.37）。+0.508 是 meaningful detection power。但 binary flipping 确实是 simplification。\n\n---\n\n### Convergence Questions 回应\n\n**Q1: Does this paper change how the community evaluates LLM benchmarks in practice?**\n\n**Yes, incrementally but meaningfully.** 具体的 practical impact：\n- Ground truth meta-critique 直接改变 contamination detection 的 evaluation methodology（不应仅用 web-overlap labels 验证 differential detectors）\n- DIF audit protocol（§5.4 graduated thresholds: <15% monitor / 15-25% flag / >25% act）提供了 actionable guideline\n- 31% 这个数字本身会影响社区对 MMLU 等 benchmark 的信心（即使只是 diagnostic，不是 destructive）\n\n但 impact 是 incremental 而非 transformative——论文不提出新 benchmark 或新 evaluation paradigm，而是对现有 benchmark 增加一个 monitoring dimension。\n\n**Q2: Is the semi-synthetic framework alone sufficient for conference-level novelty?**\n\n**单独不够，但作为 package 的一部分是 sufficient。** 框架本身（cross-subject matching + multi-subject boundary characterization）是 reusable infrastructure，但需要 empirical findings 和 meta-critique 提供 motivation。三者的组合是否达到 conference level 取决于对 \"application paper\" 的接受标准。\n\n**Q3: What's the appropriate venue — Main or Findings?**\n\n**Findings，with a path to Main if permutation null is added。**\n\n理由：\n- **For Main (21% acceptance)**：需要 novelty + significance + soundness 全面过线。novelty 明确受限（known method → new domain），significance 虽高但 headline 数字（31%）缺少 permutation null 校准。\n- **For Findings**：solid empirical contribution + reusable methodological framework + community-relevant meta-critique = Findings 的 sweet spot。\n\n---\n\n### 最终评分\n\n| 维度 | 最终评分 | 变化 | 理由 |\n|---|---|---|---|\n| Soundness | 4.0 / 5 | 维持 | MH-DIF 应用正确，controls 充分，multi-subject boundary 是 genuine improvement |\n| Excitement | 3.0 / 5 | 从 3.5 下调 | 采纳 R2 novelty ceiling 论点；application paper ceiling |\n| Reproducibility | 4.0 / 5 | 维持 | Public data, code, explicit parameters |\n| Clarity | 3.5 / 5 | 从 4.0 下调 | Space allocation uneven（某些关键分析过于压缩） |\n| Reviewer Confidence | 4 / 5 | 维持 | 熟悉 DIF 方法论和 LLM evaluation 文献 |\n\n**Overall: 3.5 / 5 → Findings 接收**\n\n---\n\n### Calibration Rationale\n\n**3.5 = Borderline Conference / Findings accept。**\n\n按 EMNLP 2026 标准：\n- 5 = Award (top 2.5%)：不适用\n- 4.5 = Borderline Award：不适用\n- 4 = Conference accept：需要 novelty or significance 显著高于当前水平\n- **3.5 = Borderline Conference**：当前位置\n- **3 = Findings accept**：如果不修改 permutation null\n\n**维持 3.5 而非调整的逻辑**：\n\n- **不升至 4.0**：(a) 缺少 permutation null → headline 数字未校准；(b) novelty ceiling（R1+R2 共识）；(c) binary flipping 对 semi-synthetic real-world relevance 的限制\n- **不降至 3.0**：(a) Round 1 → Round 2 的修改质量高且 responsive（title 改善、Proposition 1 限定、multi-subject boundary、bootstrap 明确、Claim 4 降级、Related Work 大幅扩充）；(b) confound 控制在同类论文中 above average；(c) Soundness 4.0 不应被 novelty concern 完全抵消\n\n**与 R2 的最终分歧**：R2 Overall 3.0，我 3.5。差距 0.5 主要来自：\n1. Related Work 评估不同（R2 说 10 refs / 3 paragraphs，我读到 ~60 refs / 4 paragraphs）\n2. Soundness 权重不同（我更重视 confound 控制的系统性）\n3. 版本差异可能导致部分评分基础不同\n\n**建议 Director**：如果 R2 审的是不同版本，应请 R2 重新审阅当前 PDF 后再做最终 convergence。当前版本对 Round 1 问题的回应质量值得被 credit。\n\n---\n\n### 给作者的总结建议（如果进入 camera-ready）\n\n**必须做：**\n1. 补充 permutation null（1,000 permutations，随机打乱 cohort labels），报告 null-adjusted C%\n2. Multi-subject injection 结果以 table/figure 呈现（当前只有 inline text）\n3. 报告 IRT model fit statistics（|Lz|, CFI——即使结论不变）\n\n**建议做：**\n4. 在 Limitations 中增加 binary flipping 简化的讨论\n5. 压缩 §4.3 Ground Truth Mismatch（多个 near-independence 统计量有冗余），扩展 §4.5 Semi-synthetic 和 §4.6 Downstream\n6. 讨论 bootstrap CI 不对称性的来源",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-21T17:51:04.092032+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Assistant

_source line 272 · 2026-05-21T17:51:09.783002+00:00_

审稿意见已提交。

最终评分 **Overall 3.5/5（Findings 接收）**。核心判断：论文对 Round 1 反馈的回应质量高（title 改善、Proposition 1 限定、multi-subject boundary、Related Work 扩充），Soundness 4.0 的 confound 控制在同类论文中属上乘。但缺少 permutation null 和 novelty ceiling 阻止了升至 Conference accept。与 R2 的 0.5 分差异主要源于 Related Work 评估不同和可能的版本差异。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 12

## Round 12

70 recorded events


### User

_source line 273 · 2026-05-21T18:43:33.829892+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查**方法严谨性 + 实验设计**。

## Venue 信息
- **目标 venue**: EMNLP 2026（via ACL Rolling Review）
- **Deadline**: 2026-05-25
- **页数限制**: 正文 8 页 + unlimited references。Limitations 和 ethical considerations 不计入页数
- **模板**: ACL template，`[review]` 模式
- **匿名规则**: Double-blind（论文中不得出现作者信息）
- **ARR 评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit

## 论文路径
- TeX: `projects/irt_equated_bench_regen/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf`

## 你的审查侧重

**重点关注以下维度**：

1. **MH-DIF 方法论**：
   - Mantel-Haenszel 程序在 LLM benchmark 场景下的适用性（假设检验：条件独立性、局部独立性在 LLM 数据中是否成立？）
   - ETS severity classification（A/B/C）的阈值选择是否充分论证？
   - Cross-subject matching 的 Proposition 1 (ΔFPR=0) 证明是否完备？边界条件是否充分讨论？

2. **Semi-synthetic injection framework**：
   - Binary response flipping 是否是合理的 contamination 模拟？ecological validity 如何？
   - 实验设计：exploitation rate p 的选择、seed 数量（5 seeds）是否足够？
   - Cross-subject vs. within-subject vs. external matching 的比较是否公平？

3. **统计分析**：
   - Bootstrap CI 的 resampling unit（model-level）和 B=1,000 是否充分？
   - Benjamini-Hochberg FDR correction 的 q=0.05 选择是否合理？
   - Permutation test（200 label shuffles）的 power 是否足够？
   - Simpson's paradox 分析和 logistic regression 的 model specification
   - Power analysis (Section 4.1) 的 assumptions 和 conclusions

4. **控制实验**：
   - Random split (0.18%) 作为 null baseline 是否充分？
   - Ability-quintile 和 within-family comparisons 的设计
   - Multi-subject injection robustness (k∈{1,3,5,10,20}) 的结果解读

5. **可重复性和透明度**：
   - IRT model fit（2PL on 57-subject benchmark）的报告是否充分？
   - 代码和数据可用性
   - 关键超参数和 design choices 的 sensitivity analysis

请按 ARR 格式输出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。对 weaknesses 严格评估，不留情面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-21T18:43:40.654115+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-21T18:43:40.755251+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-21T18:43:43.216515+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-21T18:43:43.367421+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-21T18:43:45.826421+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-21T18:43:45.877096+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-21T18:43:50.898621+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-21T18:43:50.949893+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-21T18:43:55.181396+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 283 · 2026-05-21T18:43:55.934891+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 284 · 2026-05-21T18:44:02.862556+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

I found comprehensive information about the ACL Rolling Review (ARR) 2026 reviewer guidelines and review form. Here are the key details:

## Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Overall Assessment Score

The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement
…[truncated 956 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7681
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-21T18:44:04.222995+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 586.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.1}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 495.2}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 552.6}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"si
…[truncated 234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8288
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-21T18:44:09.319125+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-21T18:44:09.369840+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-21T18:44:10.022900+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "11-13",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "11-13",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-21T18:44:10.474849+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 566.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 432.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 209.2}], \"total_pages\": 13, \"rendered_pages\": 3, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-21T18:44:15.394922+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5), descriptions for each score level, and any other required fields. I need the exact scoring criteria for: Overall Assessment, Soundness, Excitement, Reproducibility, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5), descriptions for each score level, and any other required fields. I need the exact scoring criteria for: Overall Assessment, Soundness, Excitement, Reproducibility, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 291 · 2026-05-21T18:44:15.998502+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 292 · 2026-05-21T18:44:16.903265+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 293 · 2026-05-21T18:44:16.903754+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-21T18:44:17.104690+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-21T18:44:17.757695+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool result

_source line 296 · 2026-05-21T18:44:18.009824+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-21T18:44:22.276557+00:00_

# ARR Review Form Scoring Dimensions

## Overall Assessment
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award"
- **4**: Conference acceptance recommended
- **3**: Findings track acceptance recommended
- **2**: "Resubmit next cycle: I think this paper needs substantial revisions"
- **1**: Do not resubmit or paper lacks relevance

## Soundness
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me"
- **1**: "Not Exciting: this paper does not resonate with me"

## Reproducibility
Scale: 1-5
- **5**: "They could easily reproduce the results"
- **4**: "They could mostly reproduce the results"
- **3**: "They could reproduce the results with some difficulty"
- **2**: "They would be hard pressed to reproduce the results"
- **1**: "They would not be able to reproduce the results"

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct"
- **4**: "Quite sure"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but fairly likely I missed details"
- **1**: "Not my area, or paper is very hard to understand"

## Additional Required Fields
- Paper Summary
- Summary of Strengths
- Summary of Weaknesse
…[truncated 213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6881
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-21T18:44:27.245378+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 299 · 2026-05-21T18:44:27.847633+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 300 · 2026-05-21T18:44:28.403633+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1158
}
```

</details>

---


### Tool call

_source line 301 · 2026-05-21T18:44:28.404113+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 302 · 2026-05-21T18:44:28.908849+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1061
}
```

</details>

---


### Tool call

_source line 303 · 2026-05-21T18:44:28.909285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 304 · 2026-05-21T18:44:29.011271+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-21T18:44:29.564416+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-21T18:44:33.730917+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 307 · 2026-05-21T18:44:34.233904+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 308 · 2026-05-21T18:44:34.688622+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 309 · 2026-05-21T18:44:34.689065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 310 · 2026-05-21T18:44:35.243507+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---


### Tool call

_source line 311 · 2026-05-21T18:44:35.244050+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 312 · 2026-05-21T18:44:35.596312+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-21T18:44:35.999105+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-21T18:44:39.513205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 315 · 2026-05-21T18:44:39.814774+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 316 · 2026-05-21T18:44:40.367933+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-21T18:44:40.420062+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-21T18:45:16.814053+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
  }
}
```

</details>

---


### Tool call

_source line 319 · 2026-05-21T18:45:16.814501+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 320 · 2026-05-21T18:45:16.814798+00:00_

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
21	\title{Temporal Measurement Drift in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-21T18:46:13.353788+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 51, \"total_citations\": 76, \"unique_cited_keys\": 51, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 33, \"online_not_found\": 9, \"online_mismatch\": 9}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"balloccu2024leak\", \"type\": \"inproceedings\", \"title\": \"Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs\", \"authors\": \"Balloccu, Simone and Schmidtova, Patrícia and Lango, Mateusz and Dusek, Ondrej\", \"year\": \"2024\", \"venue\": \"Proceedings of the 18th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"dekoninck2024constat\", \"type\": \"inproceedings\", \"title\": \"ConStat: Performance-Based Contamination Detection in Large Language Models\", \"authors\": \"Dekoninck, Jasper and Mueller, Mark Niklas and Vechev, Martin\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"golchin2024timetravel\", \"type\": \"inproceedings\", \"title\": \"Time Travel in LLMs: Tracing Data Contamination in Large Language Models\", \"authors\": \"Golchin, Shahriar and Surdeanu, Mihai\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"li2024contamination\", \"type\": \"inproceedings\", \"title\": \"An Open-Source Data Contamination Report for Large Language Models\", \"authors\": \"Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2024\"}, {\"key\": \"liang2026dvd\", \"type\": \"misc\", \"title\": \"DVD: Detection via Variance of Generation Distribution for Variant Contamination\", \"authors\": \"Liang, Rongzhen\", \"year\": \"2026\", \"venue\": \"\"}, {\"key\"
…[truncated 40850 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 56539
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-21T18:46:19.831904+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-21T18:46:19.832479+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-21T18:46:22.895020+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-21T18:46:22.995925+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-21T18:46:26.409251+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-21T18:46:26.861637+00:00_

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
…[truncated 7924 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-21T18:46:26.912461+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-21T18:46:27.315034+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	A Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold.
10	
11	\subsection{Temporal Comparability: 31\% Measurement Drift}
12	\label{sec:temporal}
13	
14	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%], $B = 1{,}000$ model-level resamples). The rightward CI asymmetry reflects a heavy-tailed C\% distribution across resamples, driven by subjects with C\% exceeding 40\%. Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold on effect size and significance already provides implicit multiple-testing protection.
15	
16	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C items (sampling noise), and an ability-quintile comparison within the same temporal cohort yields 2.9\% (ability differences alone). A within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% ETS~C items, elevated by large ability gaps that confound the DIF signal~\
…[truncated 10035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-21T18:46:27.315411+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-21T18:46:27.365933+00:00_

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
…[truncated 5638 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-21T18:46:33.741172+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-21T18:46:34.193527+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Implications for Benchmark Temporal Comparability}
5	\label{sec:disc_temporal}
6	
7	The 31\% ETS~C DIF rate extends across all six METABENCH benchmarks (C\% $= 17.9$--$31.3\%$, 45--174$\times$ above baselines), with knowledge/reasoning benchmarks more affected than procedural ones. The Simpson's paradox (\Cref{sec:temporal}) confirms DIF is associated with item properties rather than accuracy gains; ranking is preserved ($\rho \approx 0.997$) but measurement properties drift across model generations.
8	
9	\subsection{Ground Truth Meta-Critique}
10	\label{sec:disc_groundtruth}
11	
12	The near-independence between DIF flags and web-overlap labels (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$) reflects that the two methods measure different constructs---global exposure versus differential functioning---making web-overlap labels an inappropriate ground truth for a differential method. The semi-synthetic dose-response ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$) confirms that MH-DIF detects differential behavior when present; the near-independence reflects a category error in the ground truth, not a detection failure.
13	
14	\subsection{Recommended DIF Audit Protocol}
15	\label{sec:disc_protocol}
16	
17	\looseness=-1
18	We propose that benchmark maintainers run temporal MH-DIF analysis whenever $\geq 500$ new models accumulate, using cross-subject matching, with graduated action levels: (1)~\emph{Monitor} (C\% $< 15\%$); (2)~\emph{Flag} ($15\% \leq$ C\% $< 25\%$): report stable-item rankings alongside full rankings; (3)~\emph{Act} (C\% $\geq 25\%$): rotate or retire flagged items. MMLU's C\% exceeds the action threshold, aligning with ETS guidelines~\citep{clauser1998dif}. DIF pre-screening identifies stable anchor items for equating~\citep{habba2026growingpains}; our open-source implementation runs in under 5 minutes on a single CPU core. Temporal C\% could also serve as a dimension in composi
…[truncated 42 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-21T18:46:34.194049+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-21T18:46:34.395222+00:00_

1	\section*{Limitations}
2	
3	\paragraph{Methodological scope.}
4	MH-DIF detects only uniform DIF; logistic regression reveals an additional 24.8\% non-uniform DIF, making 31\% conservative. More fundamentally, DIF detects \emph{that} items function differently but cannot determine \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts. A definitive causal decomposition remains out of reach without access to model training data. The semi-synthetic framework uses binary response flipping (incorrect $\to$ correct) to simulate differential contamination, representing a worst-case uniform exploitation pattern. Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages; detection power under such realistic patterns is untested. The moderate $\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$ reflects sensitivity to severe differential behavior; the framework's primary methodological contribution---cross-subject matching achieving $\Delta\mathrm{FPR} = 0.000$---is a matching strategy property independent of injection realism.
5	
6	\paragraph{Matching boundary and sample size.}
7	Cross-subject matching assumes contamination affects a minority of domains; when contamination spans ${>}10$ subjects (${>}18\%$ of MMLU), $\Delta\mathrm{FPR}$ rises to 0.026--0.069. The GSM1K correlation analysis ($N = 33$) has limited statistical power and is exploratory; replication with larger model samples is warranted.
8	
9	\paragraph{Generalizability.}
10	All six benchmarks use multiple-choice or binary scoring; generalizability to open-ended generation (e.g., AlpacaEval), coding (e.g., HumanEval), or partial-credit benchmarks is untested and would require polytomous DIF methods. Temporal cohorts are defined by calendar year, a coarse grouping; finer-grained definitions (e.g., by training data cutoff or alignment method) might reveal more targeted patterns.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-21T18:46:34.747061+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-21T18:46:35.299795+00:00_

1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet whether individual items measure the same construct over time is rarely tested---and existing contamination detectors validate against ground truth that conflates global exposure with differential functioning. We develop a semi-synthetic injection framework with cross-subject matching that achieves zero false positive inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$), and show that web-overlap contamination labels are near-independent of Mantel-Haenszel Differential Item Functioning (DIF) flags (enrichment $\approx 0.96$, $\phi = 0.012$)---exposing a category error in prevailing validation methodology. Applying MH-DIF with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 items), we find 17.9--31.3\% of items exhibit large temporal DIF (ETS~C) between 2023 and 2024 cohorts, each 45--174$\times$ above random baselines, with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). This does not threaten ranking validity ($\rho \approx 0.997$) but reveals which capability dimensions shift across generations. Item-level decomposition shows 92.4\% of the signal is item-specific; DIF-flagged items concentrate discriminative information ($z = -8\sigma$ to $-49\sigma$) with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-21T18:46:35.300215+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-21T18:46:35.401002+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. This pattern persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of the DIF signal is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this measurement drift does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The drift is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{liang2026dvd}, 
…[truncated 5168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-21T18:50:57.467169+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**论文标题**: Temporal Measurement Drift in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n\n---\n\n## 总体评分\n**Overall**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: 方法论扎实、控制实验充分的大规模心理测量学分析，但因果解释力不足和实际影响有限（ρ ≈ 0.997）制约了贡献高度。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法选择合理，控制实验设计全面（随机分裂、能力匹配、族内对比、置换检验），但 LLM 场景下 MH-DIF 假设的适用性论证存在缺口（详见 N1、N2）|\n| Excitement | 3/5 | 将心理测量学 DIF 引入 LLM 评估是有意义的跨领域迁移，但 ρ ≈ 0.997 的结果削弱了实际紧迫性，且缺乏因果归因降低了可操作性 |\n| Reproducibility | 4/5 | 匿名代码已提供，METABENCH 数据公开，关键超参数（K=5, ETS C 阈值, 5 seeds）均已报告；2PL 参数来源透明 |\n| Reviewer Confidence | 4/5 | 熟悉 DIF 方法论和 LLM 评估文献 |\n\n---\n\n## Paper Summary\n\n本文将教育测量学中的 Mantel-Haenszel DIF 分析（配合 ETS 严重程度分类）应用于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目），发现 2023 vs 2024 模型群体间约 31% 的 MMLU 题目呈现 ETS Category C 级别的时序 DIF。作者开发了跨科目匹配的半合成注入框架（ΔFPR = 0.000），并指出 web-overlap 污染标签与 DIF 标志几乎独立（enrichment ≈ 0.964），揭示了现有污染检测验证方法论中的\"类别错误\"。分析扩展到全部六个 METABENCH 基准（C% = 17.9–31.3%），同时表明排名稳定性未受影响（ρ ≈ 0.997）。\n\n---\n\n## 主要优势\n\n1. **规模与全面性**：据我所知，这是 LLM 基准上最大规模的 DIF 分析（5,227 模型 × 12,508 题目）。6 个基准的交叉验证增强了发现的可信度。\n\n2. **控制实验设计精良**：随机分裂（0.18%）、能力分位（2.9%）、族内对比（Llama-2 vs 3）、最近邻匹配（Cohen's d ≈ -0.010, C% = 28.9%）、置换检验（200 次，null C% = 0.10%）——多重控制有效排除了方法论伪影。特别是最近邻匹配将能力混淆压缩至 ~2.4 pp，这是很有说服力的。\n\n3. **Ground truth meta-critique 概念清晰**：global exposure vs. differential functioning 的区分（Figure 1）以及 enrichment ≈ 0.964 的实证支持构成了对领域验证方法论的有价值批评。这一贡献独立于 DIF 发现本身。\n\n4. **跨科目匹配的方法论贡献**：Proposition 1 在构造上保证 ΔFPR = 0，多科目注入的梯度退化实验（Table 4: k ≤ 5 时 ΔFPR < 0.007）提供了实用边界。\n\n5. **诚实的局限性**：论文明确承认 MH-DIF 只检测 uniform DIF、无法确定因果、二值翻转注入是最坏情况模拟。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] DIF 的因果可解释性不足，核心发现的解读空间过大\n- 具体位置：Section 1 (line 15-16 of introduction.tex), Section 5, Limitations\n- 问题：论文反复承认 MH-DIF 检测到题目功能差异但无法归因（\"the signal may reflect contamination, capability change, or training methodology shifts\"）。然而 31% 的核心发现如果主要由真实能力提升驱动（2024 模型在特定类型题目上的真实进步），则 DIF 只是在重新发现能力变化而非测量漂移。论文的 Simpson's paradox 分析（Section 4.2: aggregate OR = 1.55 vs controlled OR = 0.73）和 item-level regression（92.4% item-specific）试图排除这一解释，但 item-level specificity 本身并不排除 item-level 的真实能力提升——如果 2024 模型在形式逻辑方面系统性进步，这会在形式逻辑题目上产生 item-specific DIF，但这是能力变化而非测量伪影。\n- 为什么影响接收：论文标题使用 \"Measurement Drift\"，隐含的 framing 是这是一个问题（\"benchmarks need psychometric monitoring\"），但如果 DIF 主要反映真实能力变化，则结论反转——DIF 恰恰说明基准在正常工作，灵敏地捕捉了代际差异。论文需要更明确地处理这一替代解释，而非将其留在 Limitations 中一笔带过。\n- 建议修改方向：(a) 提供至少一种操作化的区分方法（如：对 STEM 子集的 DIF 方向与已知训练数据变化的一致性分析）；(b) 在 Discussion 中显式讨论 \"DIF as capability change signal\" 的可能性及其对论文结论的影响；(c) 考虑将 framing 从 \"measurement drift as problem\" 调整为 \"DIF as diagnostic tool\"（论文在某些段落已有此意识但不一致）。\n\n**N2** [critical] 半合成注入框架的生态效度存疑，ΔTPR = +0.508 的实际意义不明\n- 具体位置：Section 3.4, Section 4.5, Limitations (line 4)\n- 问题：二值翻转注入（incorrect → correct at rate p）模拟的是最极端的均匀污染模式。现实中的污染效应包括部分记忆、推理捷径、格式偏好等，且效应大小因题目而异。论文承认这一点（Limitations: \"detection power under such realistic patterns is untested\"），但核心数字 ΔTPR = +0.508 at p = 0.5 仍是论文的主要验证指标。在 p = 0.5（50% 的错误答案被翻转为正确）的激进注入下，仅有约一半的注入题目被检出——这一检测力在更现实（更弱）的污染模式下会进一步下降。同时，注入比例固定为 20% 的 ETS-A 题目，未提供对此选择的 sensitivity analysis。\n- 为什么影响接收：半合成验证是 Contribution 1，也是支撑 cross-subject matching 和 ground truth meta-critique 的基础。如果验证框架本身的外部效度有限，则论文的方法论贡献的可推广性受损。\n- 建议修改方向：(a) 添加至少一种更现实的注入模式（如：difficulty-dependent exploitation rate, 其中简单题目的翻转概率高于困难题目）；(b) 报告 20% 注入比例的 sensitivity analysis（10%, 30%, 50%）；(c) 更谨慎地 frame ΔTPR = +0.508 的含义——明确这是 upper-bound sensitivity 而非 expected performance。\n\n**N3** [critical] Within-subject C% = 38.1% 高于主分析 31.3%，解释不充分\n- 具体位置：Section 4.4 (experiments.tex line 54), Table 2, Appendix B (line 29-31)\n- 问题：如果 DIF 是真实的时序效应，per-subject 分析（控制了多维性）应该给出更干净的估计。但 within-subject C% = 38.1% 反而更高。论文将此归因于局部依赖（11.3% within-subject 题目对 |Q3| > 0.20），但这一解释有两个问题：(1) 如果局部依赖膨胀了 within-subject DIF，那 within-subject 分析就不是 \"控制了多维性\" 的可靠估计；(2) cross-subject matching 被声称能解决此偏差，但 cross-subject matching 的主分析（31.3%）仍低于 within-subject（38.1%），说明存在未被完全解释的方差来源。Appendix B 提到 \"the cross-subject matching protocol addresses this bias, and temporal C% persists under external matching\"，但未给出 external matching 的具体 C% 数字来支撑这一声称。\n- 为什么影响接收：Table 2 的 Structural Analysis 是论文的核心论据之一。Within-subject 结果与论文叙事（31% 是稳健的 lower bound）不一致，undermines 对多维性混淆的控制。\n- 建议修改方向：(a) 提供 external matching 的具体 C%（如 MMLU DIF using GSM8K total score as matching variable）；(b) 更详细地分解 within-subject C% 膨胀的来源（多少归因于 LD，多少归因于样本量差异，多少归因于 stratum homogeneity）；(c) 明确论文推荐的 \"best estimate\" 是 31.3%（cross-subject）还是 28.9%（最近邻匹配），并解释差异。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 置换检验仅 200 次洗牌，分辨率有限\n- 具体位置：Section 4.2 (experiments.tex line 16)\n- 问题：200 次标签洗牌的最小可报告 p 值为 1/200 = 0.005。论文报告 p = 0.005（0/200 exceed observed），但这是该设置下的分辨率下限而非精确 p 值。真实 p 值可能远小于 0.005。考虑到 null C% = 0.10% vs observed 31.3%（差 ~310倍），增加到 1,000-10,000 次洗牌几乎不增加计算成本，但能提供更精确的 p 值。\n- 建议：增加到 ≥1,000 次洗牌并报告更精确的 p 值；或在论文中明确说明 \"p ≤ 0.005 (resolution limit of 200 permutations)\"。\n\n**W2** [warning] Proposition 1 形式化程度与实际内容不匹配\n- 具体位置：Section 3.4 (method.tex lines 50-53)\n- 问题：Proposition 1 被格式化为数学命题，但实际内容是一个构造性定义的直接推论：如果匹配变量 M_i^{(-s)} 排除了科目 s 的题目，那注入 s 的污染不改变 M_i^{(-s)}——这在定义层面就是 trivially true。将其包装为 Proposition 提升了读者对 \"证明\" 深度的期望，但实际只是重述定义。此外，Proposition 仅覆盖 single-subject injection，而论文的主要发现涉及跨 57 个科目的全局 DIF，两者之间的 gap 未被正式分析。\n- 建议：降格为 Remark 或将其融入正文叙述；或补充一个更有实质内容的理论结果（如：给出 multi-subject injection 下 ΔFPR 的上界表达式，而非仅靠 Table 4 的经验值）。\n\n**W3** [warning] Bootstrap CI 的重采样单位（model-level）忽略了家族内相关性\n- 具体位置：Section 4.2 (experiments.tex line 14)\n- 问题：Bootstrap CI [29.4%, 38.1%] 使用 model-level 重采样（B = 1,000），但模型族内成员（如 Llama-2 的多个微调变体）高度相关。论文在 Structural Analysis 中通过 graduated de-duplication 分析了家族效应（K=10: 22.7%, K=20: 29.1%），但 bootstrap 过程未考虑这一聚类结构。有效样本量可能远小于 5,227，导致 CI 低估真实不确定性。CI 的右偏（上限 38.1% vs 下限 29.4%）也暗示少数高 C% 科目驱动了分布尾部。\n- 建议：补充 cluster bootstrap（以模型族为重采样单位）的 CI；或至少报告 de-duplicated 数据集（K=20, N ≈ 29.1%）上的 bootstrap CI。\n\n**W4** [warning] Simpson's paradox 中 logistic regression 模型规格未完整报告\n- 具体位置：Section 4.2 (experiments.tex line 18)\n- 问题：论文报告 aggregate OR = 1.55 (p = 0.001) 反转为 controlled OR = 0.73 (p = 0.030)，但未完整报告 logistic regression 的模型变量。\"controlling for item difficulty and discrimination\" 中 difficulty 和 discrimination 是如何操作化的（IRT 2PL 参数 a, b？还是 proportion correct 和 point-biserial？），是否考虑了交互项，这些对 OR 的方向和大小有直接影响。Section 4.4 提到 \"logistic regression DIF confirms 92.1% concordance with MH and reveals additional non-uniform DIF (24.8%)\"，但 concordance 的定义和 non-uniform DIF 的判定标准也未报告。\n- 建议：在 Appendix 中提供完整的 logistic regression model specification（因变量、自变量、交互项、拟合统计量）。\n\n**W5** [warning] Power Analysis 使用平均 2PL 参数而非参数分布\n- 具体位置：Section 4.1 (experiments.tex lines 8-9)\n- 问题：Monte Carlo power analysis 使用 PSN-IRT 的平均参数（ā = 1.2, b̄ = -0.84）。但 DIF 检测力高度依赖个别题目的区分度（a 参数）——高区分度题目更容易被检出。使用平均值掩盖了参数分布对 power 的影响。论文应说明 a 和 b 的分布（至少报告 SD），并展示 power 如何随 a 参数变化。\n- 建议：补充参数分布的描述统计；展示 power curve 在不同 a 值区间的变化；或使用参数的完整经验分布而非均值进行 power analysis。\n\n**W6** [warning] GSM1K 相关性分析统计效力不足\n- 具体位置：Section 4.7 (experiments.tex line 108)\n- 问题：GSM1K 分析仅有 N = 33 个模型，报告 r = -0.478, p = 0.005。此样本量下，一个异常值就可能大幅改变相关系数。论文正确标注为 \"exploratory\"，但仍在 Section 4.7 主体中报告且在 Appendix 提供了图表，给读者的印象是支撑性证据。对于 N = 33 的相关分析，应至少报告 bootstrapped CI 和 robust correlation（如 Spearman 或 rank-based）。\n- 建议：降低此分析的权重（如移至 Appendix 并明确标注 \"preliminary\"）；补充 robust correlation 和 bootstrapped CI；或干脆移除，避免给读者过度解读的空间。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 2 列名歧义**：列名 \"Temp. FPR\" 在这里实际指的是 temporal C%（因为 FPR 通常指 false positive rate），但 C% 本身是 DIF 检出率而非传统意义的 FPR。这一命名可能引起混淆。\n\n2. **Abstract 信息密度过高**：Abstract 包含大量数字（ΔFPR = 0.000, ΔTPR = +0.508, enrichment ≈ 0.96, φ = 0.012, 5,227 models, 27,125 items, 17.9–31.3%, 45–174×, C% ≥ 26.9%, C% ≤ 18.9%, ρ ≈ 0.997, z = -8σ to -49σ, 92.4%, ρ = -0.597）。建议精简至核心数字。\n\n3. **引用验证**：verify_references 工具检出 9 个 \"not_found\"（多为近期 preprint，OpenAlex 尚未收录，如 Liang 2026 DVD, Kipnis 2024 metabench, Qian 2026 Benchmark² 等），以及 Holland 1988 年份可能为 1986 的 mismatch。建议核实 Holland & Thayer 原始出版年份。\n\n4. **p = 0.1 缺失**：Method Section 3.4 的注入实验跳过了 p = 0.1 这个可能更现实的低注入率点。Figure 2 的 dose-response 曲线在 p = 0 和 p = 0.3 之间缺少数据点，无法判断低注入率下的检测灵敏度。\n\n5. **页数合规**：主文 8 页 + References + Limitations + Appendix，符合 EMNLP 2026 long paper 要求。\n\n6. **匿名性**：未发现作者身份信息，footnote 使用匿名仓库链接。合规。\n\n---\n\n## Questions for Authors\n\nQ1: 如果将 DIF 方向（favoring 2023 vs 2024）与已知的训练数据变化（如 2024 模型更多使用 instruction tuning / RLHF）进行对照，是否能提供因果归因的初步证据？论文已有 STEM vs Humanities 方向差异的描述性发现（Section 4.2），但未尝试与训练方法论变化进行系统对应。\n\nQ2: 论文推荐的 C% action threshold（15%, 25%）基于什么依据？ETS 的原始阈值是为教育测试设计的，直接迁移到 LLM 评估场景的合理性需要论证。\n\nQ3: 如果在 2023 cohort 内部按半年分裂（2023-H1 vs 2023-H2），C% 是多少？Section 4.7 提到 2023-H2 vs 2024-H1 的 C% = 34.35%，但 2023 年内的基线变化率会帮助理解时序 DIF 的累积速度。\n\nQ4: Cross-subject matching 在 MMLU 上排除了当前科目的题目，但 57 个科目中部分科目高度相关（如多个 STEM 子科目）。如果污染集中在相关科目群中，M_i^{(-s)} 仍会部分吸收污染信号。是否分析了科目间相关性对 Proposition 1 的影响？\n\nQ5: 论文的 IRT 模型拟合报告（Appendix A.2）提到 MMLU \"shows poor fit to a unidimensional 2PL model\"。Power analysis（Section 4.1）使用的 2PL 参数是否因 model misfit 而不可靠？如果参数估计有偏，基于这些参数的 power analysis 结论的可信度如何？\n\n---\n\n## Missing References\n\n1. **DIF in computerized adaptive testing**: 论文可能受益于讨论 CAT 场景下的 DIF 检测（如 Lei & Li, 2003; Zwick, 2012），因为 LLM 评估的高样本量和题目池大小更接近 CAT 而非传统纸笔测试。\n\n2. **MMLU-Pro / MMLU-Redux**: 论文使用原始 MMLU，但未讨论 MMLU-Pro (Wang et al., 2024) 和 MMLU-Redux (Gema et al., 2024) 等修订版是否缓解了部分 DIF——这与论文的 \"retire flagged items\" 建议直接相关。\n\n3. **Measurement invariance in cross-cultural testing**: DIF 文献中 temporal groups 类比于 cross-cultural groups 的讨论（如 Byrne et al., 1989）可以加强论文的理论基础。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 (Borderline Conference)**\n\n本文将经典心理测量学方法（MH-DIF）成功迁移到 LLM 基准评估场景，规模大、控制实验设计全面、写作清晰。31% 的时序 DIF 发现和 ground truth meta-critique 对 LLM 评估社区有参考价值。\n\n主要顾虑：(1) 因果不可解释性使核心发现的解读空间过大——\"measurement drift\" 可能只是 \"capability change\" 的另一种说法；(2) 半合成注入框架的生态效度有限，是否能推广到真实污染模式存疑；(3) within-subject C% 高于主分析且解释不充分，动摇了多维性控制的可信度。若能在 rebuttal 中提供因果归因的初步证据（如 Q1）并补充 within-subject 膨胀的详细分析，评分可上调至 4.0。\n\n**Confidence: 4/5**（对 DIF 方法论和 LLM 评估文献较为熟悉，对 IRT model fit 的技术细节可能存在遗漏）",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**论文标题**: Temporal Measurement Drift in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n\n---\n\n## 总体评分\n**Overall**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: 方法论扎实、控制实验充分的大规模心理测量学分析，但因果解释力不足和实际影响有限（ρ ≈ 0.997）制约了贡献高度。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法选择合理，控制实验设计全面（随机分裂、能力匹配、族内对比、置换检验），但 LLM 场景下 MH-DIF 假设的适用性论证存在缺口（详见 N1、N2）|\n| Excitement | 3/5 | 将心理测量学 DIF 引入 LLM 评估是有意义的跨领域迁移，但 ρ ≈ 0.997 的结果削弱了实际紧迫性，且缺乏因果归因降低了可操作性 |\n| Reproducibility | 4/5 | 匿名代码已提供，METABENCH 数据公开，关键超参数（K=5, ETS C 阈值, 5 seeds）均已报告；2PL 参数来源透明 |\n| Reviewer Confidence | 4/5 | 熟悉 DIF 方法论和 LLM 评估文献 |\n\n---\n\n## Paper Summary\n\n本文将教育测量学中的 Mantel-Haenszel DIF 分析（配合 ETS 严重程度分类）应用于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目），发现 2023 vs 2024 模型群体间约 31% 的 MMLU 题目呈现 ETS Category C 级别的时序 DIF。作者开发了跨科目匹配的半合成注入框架（ΔFPR = 0.000），并指出 web-overlap 污染标签与 DIF 标志几乎独立（enrichment ≈ 0.964），揭示了现有污染检测验证方法论中的\"类别错误\"。分析扩展到全部六个 METABENCH 基准（C% = 17.9–31.3%），同时表明排名稳定性未受影响（ρ ≈ 0.997）。\n\n---\n\n## 主要优势\n\n1. **规模与全面性**：据我所知，这是 LLM 基准上最大规模的 DIF 分析（5,227 模型 × 12,508 题目）。6 个基准的交叉验证增强了发现的可信度。\n\n2. **控制实验设计精良**：随机分裂（0.18%）、能力分位（2.9%）、族内对比（Llama-2 vs 3）、最近邻匹配（Cohen's d ≈ -0.010, C% = 28.9%）、置换检验（200 次，null C% = 0.10%）——多重控制有效排除了方法论伪影。特别是最近邻匹配将能力混淆压缩至 ~2.4 pp，这是很有说服力的。\n\n3. **Ground truth meta-critique 概念清晰**：global exposure vs. differential functioning 的区分（Figure 1）以及 enrichment ≈ 0.964 的实证支持构成了对领域验证方法论的有价值批评。这一贡献独立于 DIF 发现本身。\n\n4. **跨科目匹配的方法论贡献**：Proposition 1 在构造上保证 ΔFPR = 0，多科目注入的梯度退化实验（Table 4: k ≤ 5 时 ΔFPR < 0.007）提供了实用边界。\n\n5. **诚实的局限性**：论文明确承认 MH-DIF 只检测 uniform DIF、无法确定因果、二值翻转注入是最坏情况模拟。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] DIF 的因果可解释性不足，核心发现的解读空间过大\n- 具体位置：Section 1 (line 15-16 of introduction.tex), Section 5, Limitations\n- 问题：论文反复承认 MH-DIF 检测到题目功能差异但无法归因（\"the signal may reflect contamination, capability change, or training methodology shifts\"）。然而 31% 的核心发现如果主要由真实能力提升驱动（2024 模型在特定类型题目上的真实进步），则 DIF 只是在重新发现能力变化而非测量漂移。论文的 Simpson's paradox 分析（Section 4.2: aggregate OR = 1.55 vs controlled OR = 0.73）和 item-level regression（92.4% item-specific）试图排除这一解释，但 item-level specificity 本身并不排除 item-level 的真实能力提升——如果 2024 模型在形式逻辑方面系统性进步，这会在形式逻辑题目上产生 item-specific DIF，但这是能力变化而非测量伪影。\n- 为什么影响接收：论文标题使用 \"Measurement Drift\"，隐含的 framing 是这是一个问题（\"benchmarks need psychometric monitoring\"），但如果 DIF 主要反映真实能力变化，则结论反转——DIF 恰恰说明基准在正常工作，灵敏地捕捉了代际差异。论文需要更明确地处理这一替代解释，而非将其留在 Limitations 中一笔带过。\n- 建议修改方向：(a) 提供至少一种操作化的区分方法（如：对 STEM 子集的 DIF 方向与已知训练数据变化的一致性分析）；(b) 在 Discussion 中显式讨论 \"DIF as capability change signal\" 的可能性及其对论文结论的影响；(c) 考虑将 framing 从 \"measurement drift as problem\" 调整为 \"DIF as diagnostic tool\"（论文在某些段落已有此意识但不一致）。\n\n**N2** [critical] 半合成注入框架的生态效度存疑，ΔTPR = +0.508 的实际意义不明\n- 具体位置：Section 3.4, Section 4.5, Limitations (line 4)\n- 问题：二值翻转注入（incorrect → correct at rate p）模拟的是最极端的均匀污染模式。现实中的污染效应包括部分记忆、推理捷径、格式偏好等，且效应大小因题目而异。论文承认这一点（Limitations: \"detection power under such realistic patterns is untested\"），但核心数字 ΔTPR = +0.508 at p = 0.5 仍是论文的主要验证指标。在 p = 0.5（50% 的错误答案被翻转为正确）的激进注入下，仅有约一半的注入题目被检出——这一检测力在更现实（更弱）的污染模式下会进一步下降。同时，注入比例固定为 20% 的 ETS-A 题目，未提供对此选择的 sensitivity analysis。\n- 为什么影响接收：半合成验证是 Contribution 1，也是支撑 cross-subject matching 和 ground truth meta-critique 的基础。如果验证框架本身的外部效度有限，则论文的方法论贡献的可推广性受损。\n- 建议修改方向：(a) 添加至少一种更现实的注入模式（如：difficulty-dependent exploitation rate, 其中简单题目的翻转概率高于困难题目）；(b) 报告 20% 注入比例的 sensitivity analysis（10%, 30%, 50%）；(c) 更谨慎地 frame ΔTPR = +0.508 的含义——明确这是 upper-bound sensitivity 而非 expected performance。\n\n**N3** [critical] Within-subject C% = 38.1% 高于主分析 31.3%，解释不充分\n- 具体位置：Section 4.4 (experiments.tex line 54), Table 2, Appendix B (line 29-31)\n- 问题：如果 DIF 是真实的时序效应，per-subject 分析（控制了多维性）应该给出更干净的估计。但 within-subject C% = 38.1% 反而更高。论文将此归因于局部依赖（11.3% within-subject 题目对 |Q3| > 0.20），但这一解释有两个问题：(1) 如果局部依赖膨胀了 within-subject DIF，那 within-subject 分析就不是 \"控制了多维性\" 的可靠估计；(2) cross-subject matching 被声称能解决此偏差，但 cross-subject matching 的主分析（31.3%）仍低于 within-subject（38.1%），说明存在未被完全解释的方差来源。Appendix B 提到 \"the cross-subject matching protocol addresses this bias, and temporal C% persists under external matching\"，但未给出 external matching 的具体 C% 数字来支撑这一声称。\n- 为什么影响接收：Table 2 的 Structural Analysis 是论文的核心论据之一。Within-subject 结果与论文叙事（31% 是稳健的 lower bound）不一致，undermines 对多维性混淆的控制。\n- 建议修改方向：(a) 提供 external matching 的具体 C%（如 MMLU DIF using GSM8K total score as matching variable）；(b) 更详细地分解 within-subject C% 膨胀的来源（多少归因于 LD，多少归因于样本量差异，多少归因于 stratum homogeneity）；(c) 明确论文推荐的 \"best estimate\" 是 31.3%（cross-subject）还是 28.9%（最近邻匹配），并解释差异。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 置换检验仅 200 次洗牌，分辨率有限\n- 具体位置：Section 4.2 (experiments.tex line 16)\n- 问题：200 次标签洗牌的最小可报告 p 值为 1/200 = 0.005。论文报告 p = 0.005（0/200 exceed observed），但这是该设置下的分辨率下限而非精确 p 值。真实 p 值可能远小于 0.005。考虑到 null C% = 0.10% vs observed 31.3%（差 ~310倍），增加到 1,000-10,000 次洗牌几乎不增加计算成本，但能提供更精确的 p 值。\n- 建议：增加到 ≥1,000 次洗牌并报告更精确的 p 值；或在论文中明确说明 \"p ≤ 0.005 (resolution limit of 200 permutations)\"。\n\n**W2** [warning] Proposition 1 形式化程度与实际内容不匹配\n- 具体位置：Section 3.4 (method.tex lines 50-53)\n- 问题：Proposition 1 被格式化为数学命题，但实际内容是一个构造性定义的直接推论：如果匹配变量 M_i^{(-s)} 排除了科目 s 的题目，那注入 s 的污染不改变 M_i^{(-s)}——这在定义层面就是 trivially true。将其包装为 Proposition 提升了读者对 \"证明\" 深度的期望，但实际只是重述定义。此外，Proposition 仅覆盖 single-subject injection，而论文的主要发现涉及跨 57 个科目的全局 DIF，两者之间的 gap 未被正式分析。\n- 建议：降格为 Remark 或将其融入正文叙述；或补充一个更有实质内容的理论结果（如：给出 multi-subject injection 下 ΔFPR 的上界表达式，而非仅靠 Table 4 的经验值）。\n\n**W3** [warning] Bootstrap CI 的重采样单位（model-level）忽略了家族内相关性\n- 具体位置：Section 4.2 (experiments.tex line 14)\n- 问题：Bootstrap CI [29.4%, 38.1%] 使用 model-level 重采样（B = 1,000），但模型族内成员（如 Llama-2 的多个微调变体）高度相关。论文在 Structural Analysis 中通过 graduated de-duplication 分析了家族效应（K=10: 22.7%, K=20: 29.1%），但 bootstrap 过程未考虑这一聚类结构。有效样本量可能远小于 5,227，导致 CI 低估真实不确定性。CI 的右偏（上限 38.1% vs 下限 29.4%）也暗示少数高 C% 科目驱动了分布尾部。\n- 建议：补充 cluster bootstrap（以模型族为重采样单位）的 CI；或至少报告 de-duplicated 数据集（K=20, N ≈ 29.1%）上的 bootstrap CI。\n\n**W4** [warning] Simpson's paradox 中 logistic regression 模型规格未完整报告\n- 具体位置：Section 4.2 (experiments.tex line 18)\n- 问题：论文报告 aggregate OR = 1.55 (p = 0.001) 反转为 controlled OR = 0.73 (p = 0.030)，但未完整报告 logistic regression 的模型变量。\"controlling for item difficulty and discrimination\" 中 difficulty 和 discrimination 是如何操作化的（IRT 2PL 参数 a, b？还是 proportion correct 和 point-biserial？），是否考虑了交互项，这些对 OR 的方向和大小有直接影响。Section 4.4 提到 \"logistic regression DIF confirms 92.1% concordance with MH and reveals additional non-uniform DIF (24.8%)\"，但 concordance 的定义和 non-uniform DIF 的判定标准也未报告。\n- 建议：在 Appendix 中提供完整的 logistic regression model specification（因变量、自变量、交互项、拟合统计量）。\n\n**W5** [warning] Power Analysis 使用平均 2PL 参数而非参数分布\n- 具体位置：Section 4.1 (experiments.tex lines 8-9)\n- 问题：Monte Carlo power analysis 使用 PSN-IRT 的平均参数（ā = 1.2, b̄ = -0.84）。但 DIF 检测力高度依赖个别题目的区分度（a 参数）——高区分度题目更容易被检出。使用平均值掩盖了参数分布对 power 的影响。论文应说明 a 和 b 的分布（至少报告 SD），并展示 power 如何随 a 参数变化。\n- 建议：补充参数分布的描述统计；展示 power curve 在不同 a 值区间的变化；或使用参数的完整经验分布而非均值进行 power analysis。\n\n**W6** [warning] GSM1K 相关性分析统计效力不足\n- 具体位置：Section 4.7 (experiments.tex line 108)\n- 问题：GSM1K 分析仅有 N = 33 个模型，报告 r = -0.478, p = 0.005。此样本量下，一个异常值就可能大幅改变相关系数。论文正确标注为 \"exploratory\"，但仍在 Section 4.7 主体中报告且在 Appendix 提供了图表，给读者的印象是支撑性证据。对于 N = 33 的相关分析，应至少报告 bootstrapped CI 和 robust correlation（如 Spearman 或 rank-based）。\n- 建议：降低此分析的权重（如移至 Appendix 并明确标注 \"preliminary\"）；补充 robust correlation 和 bootstrapped CI；或干脆移除，避免给读者过度解读的空间。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 2 列名歧义**：列名 \"Temp. FPR\" 在这里实际指的是 temporal C%（因为 FPR 通常指 false positive rate），但 C% 本身是 DIF 检出率而非传统意义的 FPR。这一命名可能引起混淆。\n\n2. **Abstract 信息密度过高**：Abstract 包含大量数字（ΔFPR = 0.000, ΔTPR = +0.508, enrichment ≈ 0.96, φ = 0.012, 5,227 models, 27,125 items, 17.9–31.3%, 45–174×, C% ≥ 26.9%, C% ≤ 18.9%, ρ ≈ 0.997, z = -8σ to -49σ, 92.4%, ρ = -0.597）。建议精简至核心数字。\n\n3. **引用验证**：verify_references 工具检出 9 个 \"not_found\"（多为近期 preprint，OpenAlex 尚未收录，如 Liang 2026 DVD, Kipnis 2024 metabench, Qian 2026 Benchmark² 等），以及 Holland 1988 年份可能为 1986 的 mismatch。建议核实 Holland & Thayer 原始出版年份。\n\n4. **p = 0.1 缺失**：Method Section 3.4 的注入实验跳过了 p = 0.1 这个可能更现实的低注入率点。Figure 2 的 dose-response 曲线在 p = 0 和 p = 0.3 之间缺少数据点，无法判断低注入率下的检测灵敏度。\n\n5. **页数合规**：主文 8 页 + References + Limitations + Appendix，符合 EMNLP 2026 long paper 要求。\n\n6. **匿名性**：未发现作者身份信息，footnote 使用匿名仓库链接。合规。\n\n---\n\n## Questions for Authors\n\nQ1: 如果将 DIF 方向（favoring 2023 vs 2024）与已知的训练数据变化（如 2024 模型更多使用 instruction tuning / RLHF）进行对照，是否能提供因果归因的初步证据？论文已有 STEM vs Humanities 方向差异的描述性发现（Section 4.2），但未尝试与训练方法论变化进行系统对应。\n\nQ2: 论文推荐的 C% action threshold（15%, 25%）基于什么依据？ETS 的原始阈值是为教育测试设计的，直接迁移到 LLM 评估场景的合理性需要论证。\n\nQ3: 如果在 2023 cohort 内部按半年分裂（2023-H1 vs 2023-H2），C% 是多少？Section 4.7 提到 2023-H2 vs 2024-H1 的 C% = 34.35%，但 2023 年内的基线变化率会帮助理解时序 DIF 的累积速度。\n\nQ4: Cross-subject matching 在 MMLU 上排除了当前科目的题目，但 57 个科目中部分科目高度相关（如多个 STEM 子科目）。如果污染集中在相关科目群中，M_i^{(-s)} 仍会部分吸收污染信号。是否分析了科目间相关性对 Proposition 1 的影响？\n\nQ5: 论文的 IRT 模型拟合报告（Appendix A.2）提到 MMLU \"shows poor fit to a unidimensional 2PL model\"。Power analysis（Section 4.1）使用的 2PL 参数是否因 model misfit 而不可靠？如果参数估计有偏，基于这些参数的 power analysis 结论的可信度如何？\n\n---\n\n## Missing References\n\n1. **DIF in computerized adaptive testing**: 论文可能受益于讨论 CAT 场景下的 DIF 检测（如 Lei & Li, 2003; Zwick, 2012），因为 LLM 评估的高样本量和题目池大小更接近 CAT 而非传统纸笔测试。\n\n2. **MMLU-Pro / MMLU-Redux**: 论文使用原始 MMLU，但未讨论 MMLU-Pro (Wang et al., 2024) 和 MMLU-Redux (Gema et al., 2024) 等修订版是否缓解了部分 DIF——这与论文的 \"retire flagged items\" 建议直接相关。\n\n3. **Measurement invariance in cross-cultural testing**: DIF 文献中 temporal groups 类比于 cross-cultural groups 的讨论（如 Byrne et al., 1989）可以加强论文的理论基础。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 (Borderline Conference)**\n\n本文将经典心理测量学方法（MH-DIF）成功迁移到 LLM 基准评估场景，规模大、控制实验设计全面、写作清晰。31% 的时序 DIF 发现和 ground truth meta-critique 对 LLM 评估社区有参考价值。\n\n主要顾虑：(1) 因果不可解释性使核心发现的解读空间过大——\"measurement drift\" 可能只是 \"capability change\" 的另一种说法；(2) 半合成注入框架的生态效度有限，是否能推广到真实污染模式存疑；(3) within-subject C% 高于主分析且解释不充分，动摇了多维性控制的可信度。若能在 rebuttal 中提供因果归因的初步证据（如 Q1）并补充 within-subject 膨胀的详细分析，评分可上调至 4.0。\n\n**Confidence: 4/5**（对 DIF 方法论和 LLM 评估文献较为熟悉，对 IRT model fit 的技术细节可能存在遗漏）",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-21T18:51:01.286642+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3819
}
```

</details>

---


### Assistant

_source line 342 · 2026-05-21T18:51:09.265439+00:00_

审稿意见已提交给 Review Director。

**核心判断**：Overall 3.5（Borderline Conference），Soundness 3.5，Excitement 3.0，Reproducibility 4.0。

**三个 Must-Fix 问题**：
1. DIF 的因果可解释性不足——"measurement drift" 和 "capability change" 无法区分，核心发现的解读空间过大
2. 半合成注入框架的生态效度有限——二值翻转是最坏情况，ΔTPR = +0.508 在更现实的污染模式下可能进一步下降，且 20% 注入率未做 sensitivity analysis
3. Within-subject C% = 38.1% 高于主分析 31.3%，对多维性控制的可信度构成挑战，解释不充分

**六个 Should-Fix 问题**涵盖置换检验分辨率（200 次）、Proposition 1 形式化过度、Bootstrap CI 忽略家族聚类、Simpson's paradox logistic regression 模型未完整报告、Power Analysis 使用均值参数、GSM1K N=33 统计效力不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 13

## Round 13

4 recorded events


### User

_source line 343 · 2026-05-21T18:51:58.983929+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

以下是 Reviewer 2（侧重新颖性+完整性+写作质量）的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别注意与你自己审稿意见的异同——对于你已提出类似观点的，请说明是否完全一致或有细微差异。

---

## Reviewer 2 完整审稿意见

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 方法论扎实、实验规模可观的 psychometric audit，但核心贡献是将标准 DIF 方法直接应用于新领域，novelty 有限，且 "measurement drift" 的 framing 与实际证据之间存在张力。

### Must-Fix 问题

**N1** [critical] "Drift" framing 超出数据支撑——两个时间点不能建立趋势
- Title 和 Abstract 使用 "Temporal Measurement Drift"，但实际只比较了 2023 vs 2024 两个时间点。"Drift" 暗示方向性时序趋势，需要至少 3 个时间点。Section 4.7 的 6-month window 仍是两点比较。建议改为 "temporal DIF" 或 "temporal instability"；或做 3+ 时间点分析。

**N2** [critical] DIF 的 causal interpretation 模糊——"measurement drift" vs "genuine capability change" 未能充分区分
- Section 4.2 的 domain-direction 分析表明 STEM 上 2024 模型更好，这可能是 genuine capability improvement。pseudo R² = 0.0007 只排除 domain-level accuracy gains，不排除 item-level capability changes。建议讨论 "benign DIF" vs "problematic DIF"，至少对 DIF-C items 做定性内容分析。

**N3** [critical] Proposition 1 是 tautological 的，不应以 formal proposition 形式呈现
- Cross-subject matching 定义的直接推论，不需要证明。将其格式化为 Proposition 增加不应有的形式感。建议改为 inline observation 或 remark。

### Should-Fix 问题

**W1** [warning] Table 2 列名 "Temp. FPR" 误导——temporal comparison 没有 ground truth，C% 不是 FPR
- 建议改为 "Temp. C%"。

**W2** [warning] 与 Growing Pains 的区分过于依赖 "empirical comparison awaits public release"
- 应至少做概念层面深入对比：FPC 假设 anchor stability，DIF 检测 anchor instability。

**W3** [warning] ρ ≈ 0.997 削弱了 practical significance argument
- 如果 DIF 不影响 ranking 决策，practitioners 为什么要做 DIF audit？Section 5.3 的 audit protocol 动机不足。需要更强的 practical motivation。

**W4** [warning] Within-family comparison (Llama-2 vs 3) C% = 61.3% → ability-matched 28.3%，与 temporal matched 28.9% 的 convergence 被 under-explored
- ~28-29% 是否是某种 "irreducible DIF floor"？这对 31% 的 interpretation 有重要影响。

**W5** [warning] Semi-synthetic injection 的生态效度有限
- Binary response flipping 是最极端的 contamination 形式。ΔTPR = +0.508 在更 realistic patterns 下可能显著更低。

### Missing References
1. Oren et al. (2024) "Proving Test Set Contamination in Black Box Language Models" (ICML 2024)
2. Deng et al. (2024) "Investigating Data Contamination in Modern Benchmarks for Large Language Models"

---

请对以上每个 N1-N3 和 W1-W5 逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-21T18:53:24.191027+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: \"Drift\" framing 超出数据支撑——两个时间点不能建立趋势**\n\n同意。\"Temporal Measurement Drift\" 在语义上暗示持续的方向性变化过程，但论文仅有 2023 vs 2024 一个对比（Section 4.2），以及 2023-H2 vs 2024-H1 的补充窗口（Section 4.7, C% = 34.35%）。两个时间点只能建立 \"difference\"，不能建立 \"drift\"（需要至少 3 个点来识别趋势方向和加速/减速）。我自己的审稿中未单独提出这一点，但在 N1 中对 \"measurement drift\" 的 framing 表达了类似顾虑——DIF 可能反映真实能力变化而非测量伪影。R2 的提法更精确：这首先是一个术语选择问题，\"temporal DIF\" 或 \"temporal instability\" 更准确。\n\n补充：METABENCH 数据跨 2023-2024，理论上可以做季度级分析（如 2023-Q1/Q2/Q3/Q4 vs 2024-Q1/Q2），这将大幅增强 \"drift\" 叙事的可信度。论文未尝试此分析，是一个明显的遗漏。\n\n**[AGREE] R2-N2: DIF 的 causal interpretation 模糊**\n\n完全同意，这与我自己的 N1 实质相同。R2 提出的 \"benign DIF\" vs \"problematic DIF\" 区分框架比我的建议更具操作性。我补充两点：\n\n1. R2 指出 pseudo R² = 0.0007 只排除了 domain-level accuracy gains，不排除 item-level capability changes——这一点非常关键。论文在 Section 4.2 用 \"92.4% item-specific\" 作为核心论据，但 item-specific 的能力提升（如模型在特定推理类型上的进步）同样会产生 item-specific DIF，这并不意味着测量出了问题。\n\n2. R2 建议的 \"定性内容分析\"（对 DIF-C items 做内容分类）是一个很好的建议。如果 DIF-C 集中在某些内容类型（如需要最新知识的题目 vs 时间无关的推理题目），这将有助于区分 contamination-driven DIF 和 capability-driven DIF。论文的 difficulty-direction interaction（ρ = -0.597, Section 4.2/Introduction）——hard items gain, easy items erode——是一个有趣的线索但未被充分挖掘。\n\n**[REBUT] R2-N3: Proposition 1 是 tautological 的**\n\n部分同意形式问题，但反驳 \"tautological\" 的定性。\n\n我在自己的 W2 中提出了类似观点（建议降格为 Remark），但 R2 的措辞 \"tautological\" 过于强硬。Proposition 1 的内容——跨科目匹配变量 M_i^{(-s)} 在单科目注入下不受污染——虽然在定义层面是直接的，但其方法论意义并非 trivial：它正式化了为什么跨科目匹配能保证 ΔFPR = 0，而标准匹配（within-subject）不能。这一区分在 DIF 文献中并非标准做法（传统 DIF 不需要 cross-subject matching，因为考生不会 \"污染\" 匹配变量），它是 LLM 场景下的特有问题。\n\n此外，Proposition 1 的实际价值在于明确了失效边界：当 k > 1 时 ΔFPR > 0（Table 4, Appendix Figure 3）。没有这个 formal statement，读者不容易理解 multi-subject injection 结果（Table 4: k=10 时 ΔFPR = 0.047）为何偏离零。\n\n**建议折中**：不必完全移除 Proposition 形式，但应 (a) 去掉 \"proof\" 的暗示（当前措辞 \"by construction\" 已经是对的），(b) 补充 multi-subject 情况的理论分析（如 ΔFPR 的 upper bound 表达式），使 Proposition 有更多实质内容。我在 W2 中也提了同样的建议。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Table 2 列名 \"Temp. FPR\" 误导**\n\n完全同意。我在小问题第 1 条提出了相同观点。C% 是 DIF 检出率（相对于 ETS C 阈值），不是 false positive rate（需要 ground truth）。Temporal comparison 没有已知的 ground truth DIF 状态，因此 \"FPR\" 在此语境下 technically incorrect。应改为 \"Temp. C%\"。\n\n**[AGREE] R2-W2: 与 Growing Pains 的区分不充分**\n\n同意。论文在 Related Work (Section 2) 和 Discussion (Section 5.3) 提到 Growing Pains (Habba et al., 2026) 作为互补工作——FPC 假设 anchor stability 来实现跨群体等值，而本文的 DIF 分析恰恰检验这一假设是否成立。这个概念对比非常有价值但只在 Section 2 中一句带过（\"Our work is complementary: Growing Pains assumes anchor item stability, while DIF analysis diagnoses which items' measurement properties shift across model generations\"）。更深入的概念对比——FPC 在 anchor 不稳定时会怎样、DIF 预筛选如何改善 FPC 的 anchor 选择——将显著加强论文的定位。\n\n**[REBUT] R2-W3: ρ ≈ 0.997 削弱 practical significance**\n\n部分反驳。R2 的逻辑是：如果 DIF 不影响排名，为什么要做审计？但论文在 Section 4.6 已提供了超越 aggregate ρ 的 practical evidence：\n\n1. **Model-family rank shifts**: Llama-3 derivatives gain +53 median rank positions, Mistral loses 35（Section 4.6）。ρ ≈ 0.997 是 aggregate 统计量，掩盖了对特定模型族的系统性影响。\n\n2. **Cohort-level 不对称**: 移除 C-flagged items 使 2024 models 下降 96.2 positions（40× larger than random removal, p < 0.001）——这意味着 DIF items 系统性地 \"帮助\" 较新模型，即使 overall ranking 变化不大。\n\n3. **Discriminative information 集中**: DIF-flagged items 集中了 z = -8σ to -49σ 的判别力信息（Section 4.6）。移除它们虽然不改变排名，但大幅降低了基准的区分能力。\n\n4. **实际应用场景**: ρ ≈ 0.997 对整体排名无影响，但对 head-to-head 模型比较（如 Model A vs Model B 差 0.5%）可能有影响——如果差异来自 DIF items，该比较不可靠。\n\n因此，论文的 practical motivation 存在但确实 under-articulated。我同意论文应更强调 family-level 和 pairwise-comparison 层面的影响（而非只报告 aggregate ρ），但不同意 ρ ≈ 0.997 本身 \"削弱\" 了 practical significance——它只是说明 aggregate ranking 不是 DIF 影响的主要维度。\n\n**[AGREE] R2-W4: ~28-29% \"irreducible DIF floor\" 被 under-explored**\n\n强烈同意，这与我的 N3 直接相关。论文的三个独立分析收敛于 ~28-29%：\n- 最近邻匹配: 28.9% ± 0.1%（Section 4.2）\n- Llama-2 vs 3 能力匹配: 28.3%（Section 4.4）\n- De-duplication K=20: 29.1%（Section 4.4）\n\n这一收敛暗示 ~28-29% 可能是一个不可约的 baseline DIF 率，反映 MMLU 题目的某种内在属性（如多维性、内容异质性），而非时序效应。如果如此，31.3% 中仅 ~2-3 pp 是真正的时序 DIF，而非 ~31%。这将从根本上改变论文的 core claim。\n\n论文未探讨这一可能性。如果作者能论证 ~28-29% 在 random split 中不出现（实际 random split C% = 0.18%），那它确实是时序特有的。但 random split 和 ability-quintile (2.9%) 都远低于 28-29%，说明 ~28-29% 需要一个 between-group 差异来触发——问题是这个差异是 temporal（release date）还是其他 confound。\n\n**[AGREE] R2-W5: Semi-synthetic injection 生态效度有限**\n\n完全同意，这与我的 N2 实质相同。R2 简洁指出了核心问题：binary response flipping 是最极端形式，ΔTPR = +0.508 在更 realistic patterns 下可能显著更低。我在 N2 中给出了更具体的建议（difficulty-dependent exploitation rate, injection fraction sensitivity analysis）。两份审稿意见在此完全一致。\n\n---\n\n### Missing References\n\nR2 提出的两篇 missing references：\n1. **Oren et al. (2024) \"Proving Test Set Contamination in Black Box Language Models\"** — 同意应引用。这是一种正式的（proof-based）黑箱污染检测方法，属于论文 Related Work 中 performance-based detectors 类别，应与 ConStat 等并列讨论。\n2. **Deng et al. (2024) \"Investigating Data Contamination in Modern Benchmarks for Large Language Models\"** — 同意。这篇综述性工作与论文的 ground truth meta-critique 直接相关。\n\n---\n\n### 与我自己审稿意见的综合对照\n\n| R2 问题 | 与 R1 的关系 | 一致性 |\n|---------|-------------|--------|\n| R2-N1 (Drift framing) | R1-N1 部分涵盖（因果模糊性），但 R2 更精确聚焦术语 | 互补 |\n| R2-N2 (Causal interpretation) | R1-N1 完全一致 | 一致 |\n| R2-N3 (Proposition 1 tautological) | R1-W2 相似但我认为 \"tautological\" 过强 | 部分分歧 |\n| R2-W1 (Table 2 FPR) | R1 小问题 #1 完全一致 | 一致 |\n| R2-W2 (Growing Pains) | R1 未提及 | 新增 |\n| R2-W3 (ρ ≈ 0.997) | R1 Excitement 评分理由涉及但不作为 weakness | 部分分歧 |\n| R2-W4 (Irreducible floor) | R1-N3 (within-subject 38.1%) 相关 | 互补 |\n| R2-W5 (Ecological validity) | R1-N2 完全一致 | 一致 |\n\n**综合判断**：两位 Reviewer 在因果可解释性（R2-N2/R1-N1）和半合成框架生态效度（R2-W5/R1-N2）上完全一致，这两点是最需要作者在 rebuttal 中回应的核心问题。R2 新增的 \"drift\" 术语问题（N1）和 \"irreducible floor\" 观察（W4）是有价值的补充。我对 Proposition 1 的看法略温和于 R2（建议改进而非移除），对 ρ ≈ 0.997 的看法也略不同（认为 family-level evidence 提供了足够的 practical motivation）。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: \"Drift\" framing 超出数据支撑——两个时间点不能建立趋势**\n\n同意。\"Temporal Measurement Drift\" 在语义上暗示持续的方向性变化过程，但论文仅有 2023 vs 2024 一个对比（Section 4.2），以及 2023-H2 vs 2024-H1 的补充窗口（Section 4.7, C% = 34.35%）。两个时间点只能建立 \"difference\"，不能建立 \"drift\"（需要至少 3 个点来识别趋势方向和加速/减速）。我自己的审稿中未单独提出这一点，但在 N1 中对 \"measurement drift\" 的 framing 表达了类似顾虑——DIF 可能反映真实能力变化而非测量伪影。R2 的提法更精确：这首先是一个术语选择问题，\"temporal DIF\" 或 \"temporal instability\" 更准确。\n\n补充：METABENCH 数据跨 2023-2024，理论上可以做季度级分析（如 2023-Q1/Q2/Q3/Q4 vs 2024-Q1/Q2），这将大幅增强 \"drift\" 叙事的可信度。论文未尝试此分析，是一个明显的遗漏。\n\n**[AGREE] R2-N2: DIF 的 causal interpretation 模糊**\n\n完全同意，这与我自己的 N1 实质相同。R2 提出的 \"benign DIF\" vs \"problematic DIF\" 区分框架比我的建议更具操作性。我补充两点：\n\n1. R2 指出 pseudo R² = 0.0007 只排除了 domain-level accuracy gains，不排除 item-level capability changes——这一点非常关键。论文在 Section 4.2 用 \"92.4% item-specific\" 作为核心论据，但 item-specific 的能力提升（如模型在特定推理类型上的进步）同样会产生 item-specific DIF，这并不意味着测量出了问题。\n\n2. R2 建议的 \"定性内容分析\"（对 DIF-C items 做内容分类）是一个很好的建议。如果 DIF-C 集中在某些内容类型（如需要最新知识的题目 vs 时间无关的推理题目），这将有助于区分 contamination-driven DIF 和 capability-driven DIF。论文的 difficulty-direction interaction（ρ = -0.597, Section 4.2/Introduction）——hard items gain, easy items erode——是一个有趣的线索但未被充分挖掘。\n\n**[REBUT] R2-N3: Proposition 1 是 tautological 的**\n\n部分同意形式问题，但反驳 \"tautological\" 的定性。\n\n我在自己的 W2 中提出了类似观点（建议降格为 Remark），但 R2 的措辞 \"tautological\" 过于强硬。Proposition 1 的内容——跨科目匹配变量 M_i^{(-s)} 在单科目注入下不受污染——虽然在定义层面是直接的，但其方法论意义并非 trivial：它正式化了为什么跨科目匹配能保证 ΔFPR = 0，而标准匹配（within-subject）不能。这一区分在 DIF 文献中并非标准做法（传统 DIF 不需要 cross-subject matching，因为考生不会 \"污染\" 匹配变量），它是 LLM 场景下的特有问题。\n\n此外，Proposition 1 的实际价值在于明确了失效边界：当 k > 1 时 ΔFPR > 0（Table 4, Appendix Figure 3）。没有这个 formal statement，读者不容易理解 multi-subject injection 结果（Table 4: k=10 时 ΔFPR = 0.047）为何偏离零。\n\n**建议折中**：不必完全移除 Proposition 形式，但应 (a) 去掉 \"proof\" 的暗示（当前措辞 \"by construction\" 已经是对的），(b) 补充 multi-subject 情况的理论分析（如 ΔFPR 的 upper bound 表达式），使 Proposition 有更多实质内容。我在 W2 中也提了同样的建议。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Table 2 列名 \"Temp. FPR\" 误导**\n\n完全同意。我在小问题第 1 条提出了相同观点。C% 是 DIF 检出率（相对于 ETS C 阈值），不是 false positive rate（需要 ground truth）。Temporal comparison 没有已知的 ground truth DIF 状态，因此 \"FPR\" 在此语境下 technically incorrect。应改为 \"Temp. C%\"。\n\n**[AGREE] R2-W2: 与 Growing Pains 的区分不充分**\n\n同意。论文在 Related Work (Section 2) 和 Discussion (Section 5.3) 提到 Growing Pains (Habba et al., 2026) 作为互补工作——FPC 假设 anchor stability 来实现跨群体等值，而本文的 DIF 分析恰恰检验这一假设是否成立。这个概念对比非常有价值但只在 Section 2 中一句带过（\"Our work is complementary: Growing Pains assumes anchor item stability, while DIF analysis diagnoses which items' measurement properties shift across model generations\"）。更深入的概念对比——FPC 在 anchor 不稳定时会怎样、DIF 预筛选如何改善 FPC 的 anchor 选择——将显著加强论文的定位。\n\n**[REBUT] R2-W3: ρ ≈ 0.997 削弱 practical significance**\n\n部分反驳。R2 的逻辑是：如果 DIF 不影响排名，为什么要做审计？但论文在 Section 4.6 已提供了超越 aggregate ρ 的 practical evidence：\n\n1. **Model-family rank shifts**: Llama-3 derivatives gain +53 median rank positions, Mistral loses 35（Section 4.6）。ρ ≈ 0.997 是 aggregate 统计量，掩盖了对特定模型族的系统性影响。\n\n2. **Cohort-level 不对称**: 移除 C-flagged items 使 2024 models 下降 96.2 positions（40× larger than random removal, p < 0.001）——这意味着 DIF items 系统性地 \"帮助\" 较新模型，即使 overall ranking 变化不大。\n\n3. **Discriminative information 集中**: DIF-flagged items 集中了 z = -8σ to -49σ 的判别力信息（Section 4.6）。移除它们虽然不改变排名，但大幅降低了基准的区分能力。\n\n4. **实际应用场景**: ρ ≈ 0.997 对整体排名无影响，但对 head-to-head 模型比较（如 Model A vs Model B 差 0.5%）可能有影响——如果差异来自 DIF items，该比较不可靠。\n\n因此，论文的 practical motivation 存在但确实 under-articulated。我同意论文应更强调 family-level 和 pairwise-comparison 层面的影响（而非只报告 aggregate ρ），但不同意 ρ ≈ 0.997 本身 \"削弱\" 了 practical significance——它只是说明 aggregate ranking 不是 DIF 影响的主要维度。\n\n**[AGREE] R2-W4: ~28-29% \"irreducible DIF floor\" 被 under-explored**\n\n强烈同意，这与我的 N3 直接相关。论文的三个独立分析收敛于 ~28-29%：\n- 最近邻匹配: 28.9% ± 0.1%（Section 4.2）\n- Llama-2 vs 3 能力匹配: 28.3%（Section 4.4）\n- De-duplication K=20: 29.1%（Section 4.4）\n\n这一收敛暗示 ~28-29% 可能是一个不可约的 baseline DIF 率，反映 MMLU 题目的某种内在属性（如多维性、内容异质性），而非时序效应。如果如此，31.3% 中仅 ~2-3 pp 是真正的时序 DIF，而非 ~31%。这将从根本上改变论文的 core claim。\n\n论文未探讨这一可能性。如果作者能论证 ~28-29% 在 random split 中不出现（实际 random split C% = 0.18%），那它确实是时序特有的。但 random split 和 ability-quintile (2.9%) 都远低于 28-29%，说明 ~28-29% 需要一个 between-group 差异来触发——问题是这个差异是 temporal（release date）还是其他 confound。\n\n**[AGREE] R2-W5: Semi-synthetic injection 生态效度有限**\n\n完全同意，这与我的 N2 实质相同。R2 简洁指出了核心问题：binary response flipping 是最极端形式，ΔTPR = +0.508 在更 realistic patterns 下可能显著更低。我在 N2 中给出了更具体的建议（difficulty-dependent exploitation rate, injection fraction sensitivity analysis）。两份审稿意见在此完全一致。\n\n---\n\n### Missing References\n\nR2 提出的两篇 missing references：\n1. **Oren et al. (2024) \"Proving Test Set Contamination in Black Box Language Models\"** — 同意应引用。这是一种正式的（proof-based）黑箱污染检测方法，属于论文 Related Work 中 performance-based detectors 类别，应与 ConStat 等并列讨论。\n2. **Deng et al. (2024) \"Investigating Data Contamination in Modern Benchmarks for Large Language Models\"** — 同意。这篇综述性工作与论文的 ground truth meta-critique 直接相关。\n\n---\n\n### 与我自己审稿意见的综合对照\n\n| R2 问题 | 与 R1 的关系 | 一致性 |\n|---------|-------------|--------|\n| R2-N1 (Drift framing) | R1-N1 部分涵盖（因果模糊性），但 R2 更精确聚焦术语 | 互补 |\n| R2-N2 (Causal interpretation) | R1-N1 完全一致 | 一致 |\n| R2-N3 (Proposition 1 tautological) | R1-W2 相似但我认为 \"tautological\" 过强 | 部分分歧 |\n| R2-W1 (Table 2 FPR) | R1 小问题 #1 完全一致 | 一致 |\n| R2-W2 (Growing Pains) | R1 未提及 | 新增 |\n| R2-W3 (ρ ≈ 0.997) | R1 Excitement 评分理由涉及但不作为 weakness | 部分分歧 |\n| R2-W4 (Irreducible floor) | R1-N3 (within-subject 38.1%) 相关 | 互补 |\n| R2-W5 (Ecological validity) | R1-N2 完全一致 | 一致 |\n\n**综合判断**：两位 Reviewer 在因果可解释性（R2-N2/R1-N1）和半合成框架生态效度（R2-W5/R1-N2）上完全一致，这两点是最需要作者在 rebuttal 中回应的核心问题。R2 新增的 \"drift\" 术语问题（N1）和 \"irreducible floor\" 观察（W4）是有价值的补充。我对 Proposition 1 的看法略温和于 R2（建议改进而非移除），对 ρ ≈ 0.997 的看法也略不同（认为 family-level evidence 提供了足够的 practical motivation）。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-21T18:53:28.107200+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3916
}
```

</details>

---


### Assistant

_source line 346 · 2026-05-21T18:53:35.721188+00:00_

交叉回应已提交给 Review Director。

对 R2 的 8 个问题（N1-N3, W1-W5），我的回应：
- **[AGREE]**: N1（drift 术语）、N2（因果模糊）、W1（Table 2 列名）、W2（Growing Pains 对比）、W4（~28-29% 不可约 floor）、W5（注入生态效度）
- **[REBUT]**: N3（Proposition 1——同意降格但反对 "tautological" 定性）、W3（ρ ≈ 0.997——family-level rank shifts 提供了足够的 practical motivation）

两位 Reviewer 的最强共识点：因果不可解释性和半合成框架生态效度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 14

## Round 14

68 recorded events


### User

_source line 347 · 2026-05-22T01:42:00.148869+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查 **方法严谨性 + 实验有效性**。

## 投稿信息
- **目标 venue**: EMNLP 2026 (via ACL Rolling Review, May cycle)
- **截止日期**: 2026-05-25
- **论文类别**: Long Paper (正文 ≤8 页, 参考文献不限, Limitations/Ethics 不计入页数)
- **模板**: ACL (review mode, double-blind)
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`
- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf`

## 你的审查侧重

请重点审查以下方面：

1. **IRT/DIF 方法论**：MH-DIF 的应用是否正确？假设是否满足（局部独立性、单维性）？是否对 model-level 二值化响应使用 DIF 的适用性做了充分论证？
2. **统计检验**：多重比较校正、bootstrap CI、permutation test 的实施是否正确？效果量和统计显著性是否准确报告？
3. **Semi-synthetic 框架**：binary flipping 注入方法的 ecological validity、TPR/FPR 的解释是否合理？Power analysis 的参数选择和结论是否站得住脚？
4. **Robustness checks**：within-subject 分析、matching 方法对比、去重实验等是否充分？是否遗漏了关键的 confound？
5. **Formal claims**：论文中的 Proposition/Remark 是否严谨？数学推导是否正确？
6. **数据与可重复性**：数据规模(5,227 models)的描述是否可信？方法描述是否足以复现？

## 输出格式

请按以下结构输出审稿意见：

### Summary (2-3 句)
### Strengths (逐条, S1/S2/...)
### Weaknesses (逐条, W1/W2/..., 标注 severity: critical/warning/info)
### Questions (逐条, Q1/Q2/...)
### Missing References (如有)
### Minor Issues (如有)
### Overall Assessment (1-5 分, 参照 ARR 标准; 附简要理由)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-22T01:42:11.442540+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-22T01:42:11.493242+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-22T01:42:16.884409+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 351 · 2026-05-22T01:42:17.187736+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool result

_source line 352 · 2026-05-22T01:42:18.343872+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 582.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 543.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 555.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"si
…[truncated 234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1459
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-22T01:42:31.251896+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I've found relevant information about the ACL Rolling Review 2026. Here are the key findings:

## Reviewer Guidelines

The recommended workflow includes reading the paper and getting a first impression, then searching for related work, and reviewers should state in their review if they did not check major parts such as proofs.

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors. Outstanding papers s
…[truncated 812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 14064
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-22T01:42:37.982745+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all dimensions/criteria, their scales (1-5 etc.), and descriptions of each score level. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other rated dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all dimensions/criteria, their scales (1-5 etc.), and descriptions of each score level. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other rated dimensions."
  }
}
```

</details>

---


### Tool call

_source line 355 · 2026-05-22T01:42:38.535013+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-22T01:42:39.087430+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-22T01:42:42.788534+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4253
}
```

</details>

---


### Tool result

_source line 358 · 2026-05-22T01:42:42.789358+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3701
}
```

</details>

---


### Tool call

_source line 359 · 2026-05-22T01:42:43.142895+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-22T01:42:43.496047+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-22T01:42:44.054903+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 912
}
```

</details>

---


### Tool result

_source line 362 · 2026-05-22T01:42:44.306763+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 810
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-22T01:42:46.465409+00:00_

# ACL Rolling Review Form - Complete Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully."
- **3:** "Pretty sure, but there's a chance I missed something."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1:** "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- **5:** "Excellent: This study is one of the most thorough I have seen."
- **4:** "Strong: This study provides sufficient support for all of its claims."
- **3:** "Acceptable: This study provides sufficient support for its main claims."
- **2:** "Poor: Some of the main claims are not sufficiently supported."
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5:** "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4:** "Exciting: I would mention this paper to others."
- **3:** "Interesting: I might mention some points of this paper to others."
- **2:** "Potentially Interesting: this paper does not resonate with me."
- **1:** "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5:** "Consider for Award: could be considered for outstanding paper award (top 2.5%)."
- **4:** "Conference: could be accepted to an *ACL conference."
- **3:** "Findings: could be accepted to the Findings of the ACL."
- **2:** "Resubmit next cycle: needs substantial revisions."
- **1:** "Do not resubmit: must be fully redone or irrelevant to *ACL."

## 5. **Reproducibility**
Scale: 1-5
- **5:** "They could easily reproduce the results."
- **4:** "They could mostly reproduce the re
…[truncated 1333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8482
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-22T01:42:50.691322+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 365 · 2026-05-22T01:42:51.193609+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 366 · 2026-05-22T01:42:52.149278+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-22T01:42:52.152855+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-22T01:42:52.153320+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 369 · 2026-05-22T01:42:52.454901+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 370 · 2026-05-22T01:42:53.009205+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-22T01:42:53.311367+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-22T01:43:02.704727+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 373 · 2026-05-22T01:43:03.056425+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 374 · 2026-05-22T01:43:03.911649+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1206
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-22T01:43:04.164065+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1107
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-22T01:43:04.164610+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "11-14",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "11-14",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-22T01:43:04.768166+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 577.7}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.9}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 335.2}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 143.3}], \"total_pages\": 14, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-22T01:43:08.433282+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 379 · 2026-05-22T01:43:08.938055+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 380 · 2026-05-22T01:43:09.291446+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool call

_source line 381 · 2026-05-22T01:43:09.342265+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 382 · 2026-05-22T01:43:09.901364+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 963
}
```

</details>

---


### Tool call

_source line 383 · 2026-05-22T01:43:09.952465+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 384 · 2026-05-22T01:43:09.954887+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 612
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-22T01:43:10.008431+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 55
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-22T01:43:18.496907+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should focus on, what constitutes a good review, specific criteria for soundness, novelty, reproducibility, and any specific instructions about statistical methodology or experimental validity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should focus on, what constitutes a good review, specific criteria for soundness, novelty, reproducibility, and any specific instructions about statistical methodology or experimental validity."
  }
}
```

</details>

---


### Tool call

_source line 387 · 2026-05-22T01:43:18.898855+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
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

_source line 388 · 2026-05-22T01:43:18.949462+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-22T01:43:26.834354+00:00_

# ARR Reviewer Guidelines: Core Focus Areas

## What Reviewers Should Prioritize

Reviewers must complete four main tasks:
1. **Allocate adequate time** for reading, reviewing, and discussion periods
2. **Check assignments** for expertise fit and conflicts of interest
3. **Write substantive reviews** addressing soundness and clarity
4. **Engage with author responses** and update assessments accordingly

## Components of a Strong Review

### Specificity (I1)
Reviews must avoid vague criticisms. Instead of saying "X is unclear," specify what information is missing. Example: replace "The paper is missing relevant references" with "The paper is missing references ABC and XYZ."

### Soundness Assessment
The soundness score reflects whether the paper is technically valid and appropriately scoped. Per guidelines, "low Soundness scores must be justified by the text of the review." Reviewers should distinguish between genuine methodological flaws and personal preference about research direction.

### Novelty Considerations
Novelty requires citing prior work. The guideline states: "if you think you've seen this before—you need to provide a reference." Work published 3+ months before submission may be required comparisons; concurrent work should be discussed where feasible.

### Reproducibility Standards
Key elements include sufficient implementation details, hyperparameter descriptions, and clarity on code/data availability. "Reproducibility scores should be justified" and refer to whether experiments can be replicated with similar results.

## Avoiding Common Review Pitfalls

The guidelines identify 17 problematic patterns (H1-H17), including:
- Dismissing results as "unsurprising" when empirical validation adds value
- Requiring SOTA results when papers claim only incremental improvements
- Penalizing negative results, which provide legitimate scientific contributions
- Expecting overly complex solutions when simpler ones suffice

## Experimental Validity Expectations

Revi
…[truncated 676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8337
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-22T01:43:31.810913+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-22T01:43:31.861726+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-22T01:43:35.579056+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-22T01:43:35.629644+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-22T01:43:38.542291+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-22T01:43:38.945582+00:00_

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
…[truncated 8118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-22T01:43:38.946081+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-22T01:43:39.247825+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	A Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal Comparability: 31\% Measurement Instability}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%], $B = 1{,}000$ model-level resamples; rightward asymmetry reflects heavy-tailed C\% from subjects exceeding 40\%). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold already provides implicit multiple-testing protection.
17	
18	\looseness=-1
19	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C ite
…[truncated 10517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-22T01:43:39.248336+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-22T01:43:39.298994+00:00_

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
…[truncated 7837 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-22T01:43:51.557588+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-22T01:43:51.959612+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\enlargethispage{18\baselineskip}
4	
5	\subsection{Implications for Benchmark Temporal Comparability}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF analysis decomposes benchmark score differences into three layers. \emph{Layer~1} (impact): overall ability differences between cohorts, removed by matching (Cohen's $d = -0.17$; matched C\% $= 28.9\%$, reducing unmatched 31.3\% by $\sim$2.4~pp). \emph{Layer~2} (DIF): item-level differences persisting after ability control---the 28--29\% floor across multiple matching methods, of which 92.4\% is item-specific (pseudo $R^2 = 0.0007$). \emph{Layer~3} (attribution): whether DIF reflects contamination, capability evolution, or training methodology shifts---beyond observational DIF analysis without training data access. The practical import is identical regardless of attribution: temporal DIF means the same benchmark score carries different meaning across model generations. The Simpson's paradox (\Cref{sec:temporal}) confirms DIF is associated with item properties rather than accuracy gains. Aggregate ranking is preserved ($\rho \approx 0.997$), but family-level profiles reveal systematic shifts (Llama-3: ${+}53$ median rank; Mistral: $-35$) that matter for pairwise model selection. Domain directionality (STEM favoring 2024 at 55.4\%, Humanities favoring 2023 at 64.4\%) describes where measurement properties shift without implying a specific cause.
10	
11	\subsection{Ground Truth Meta-Critique}
12	\label{sec:disc_groundtruth}
13	
14	\looseness=-1
15	The near-independence between DIF flags and web-overlap labels (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$) reflects that the two methods measure different constructs---global exposure versus differential functioning---making web-overlap labels an inappropriate ground truth for a differential method. The semi-synthetic dose-response ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$) confirms that MH-DIF det
…[truncated 1104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-22T01:43:51.960188+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-22T01:43:52.562675+00:00_

1	\section*{Limitations}
2	
3	\paragraph{Methodological scope.}
4	MH-DIF detects only uniform DIF; logistic regression reveals an additional 24.8\% non-uniform DIF, making 31\% conservative. More fundamentally, DIF detects \emph{that} items function differently but cannot determine \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts. A definitive causal decomposition remains out of reach without access to model training data. The semi-synthetic framework uses binary response flipping (incorrect $\to$ correct) to simulate differential contamination, representing a worst-case uniform exploitation pattern. Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages; detection power under such realistic patterns is untested. The moderate $\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$ reflects sensitivity to severe differential behavior; the framework's primary methodological contribution---cross-subject matching achieving $\Delta\mathrm{FPR} = 0.000$---is a matching strategy property independent of injection realism.
5	
6	\paragraph{Matching boundary and sample size.}
7	Cross-subject matching assumes contamination affects a minority of domains; when contamination spans ${>}10$ subjects (${>}18\%$ of MMLU), $\Delta\mathrm{FPR}$ rises to 0.026--0.069. Model-level bootstrap may underestimate CI width due to within-family correlation; cluster bootstrap at the model-family level is a natural extension (the $K{=}20$ de-duplication analysis at C\% $= 29.1\%$ provides a conservative robustness check). The GSM1K correlation analysis ($N = 33$) has limited statistical power and is exploratory.
8	
9	\paragraph{Generalizability.}
10	All six benchmarks use multiple-choice or binary scoring; generalizability to open-ended generation (e.g., AlpacaEval), coding (e.g., HumanEval), or partial-credit benchmarks is untested and would require polytomous DIF methods. Temporal cohorts are defined by
…[truncated 153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-22T01:43:52.563076+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-22T01:43:52.563278+00:00_

1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet whether individual items measure the same construct over time is rarely tested---and existing contamination detectors validate against ground truth that conflates global exposure with differential functioning. We develop a semi-synthetic injection framework with cross-subject matching that achieves zero false positive inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$), and show that web-overlap contamination labels are near-independent of Mantel-Haenszel Differential Item Functioning (DIF) flags (enrichment $\approx 0.96$, $\phi = 0.012$)---exposing a category error in prevailing validation methodology. Applying MH-DIF with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 items), we find 17.9--31.3\% of items exhibit large temporal DIF (ETS~C) between 2023 and 2024 cohorts, each 45--174$\times$ above random baselines, with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). This does not threaten ranking validity ($\rho \approx 0.997$) but reveals which capability dimensions shift across generations. Item-level decomposition shows 92.4\% of the signal is item-specific; DIF-flagged items concentrate discriminative information ($z = -8\sigma$ to $-49\sigma$) with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-22T01:43:52.965327+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-22T01:43:53.016188+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. This pattern persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of the DIF signal is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this measurement instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{lia
…[truncated 5186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-22T01:44:02.957432+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-22T01:44:03.560207+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-1
5	A semi-synthetic framework with cross-subject matching ($\Delta\mathrm{FPR} = 0.000$) resolves a validation gap: web-overlap labels are near-independent of DIF flags (enrichment $\approx 0.96$). Across six benchmarks, 17.9--31.3\% of items exhibit temporal instability associated with item properties; LLM benchmarks need psychometric monitoring alongside score reporting.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-22T01:44:03.610836+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-22T01:44:03.762112+00:00_

1	%%%%% NEW MATH DEFINITIONS %%%%%
2	
3	\usepackage{amsmath,amsfonts,bm}
4	\usepackage{amsthm}
5	
6	% Mark sections of captions for referring to divisions of figures
7	\newcommand{\figleft}{{\em (Left)}}
8	\newcommand{\figcenter}{{\em (Center)}}
9	\newcommand{\figright}{{\em (Right)}}
10	\newcommand{\figtop}{{\em (Top)}}
11	\newcommand{\figbottom}{{\em (Bottom)}}
12	\newcommand{\captiona}{{\em (a)}}
13	\newcommand{\captionb}{{\em (b)}}
14	\newcommand{\captionc}{{\em (c)}}
15	\newcommand{\captiond}{{\em (d)}}
16	
17	% Highlight a newly defined term
18	\newcommand{\newterm}[1]{{\bf #1}}
19	
20	
21	% Figure reference, lower-case.
22	\def\figref#1{figure~\ref{#1}}
23	% Figure reference, capital. For start of sentence
24	\def\Figref#1{Figure~\ref{#1}}
25	\def\twofigref#1#2{figures \ref{#1} and \ref{#2}}
26	\def\quadfigref#1#2#3#4{figures \ref{#1}, \ref{#2}, \ref{#3} and \ref{#4}}
27	% Section reference, lower-case.
28	\def\secref#1{section~\ref{#1}}
29	% Section reference, capital.
30	\def\Secref#1{Section~\ref{#1}}
31	% Reference to two sections.
32	\def\twosecrefs#1#2{sections \ref{#1} and \ref{#2}}
33	% Reference to three sections.
34	\def\secrefs#1#2#3{sections \ref{#1}, \ref{#2} and \ref{#3}}
35	% Reference to an equation, lower-case.
36	\def\eqref#1{equation~\ref{#1}}
37	% Reference to an equation, upper case
38	\def\Eqref#1{Equation~\ref{#1}}
39	% A raw reference to an equation---avoid using if possible
40	\def\plaineqref#1{\ref{#1}}
41	% Reference to a chapter, lower-case.
42	\def\chapref#1{chapter~\ref{#1}}
43	% Reference to an equation, upper case.
44	\def\Chapref#1{Chapter~\ref{#1}}
45	% Reference to a range of chapters
46	\def\rangechapref#1#2{chapters\ref{#1}--\ref{#2}}
47	% Reference to an algorithm, lower-case.
48	\def\algref#1{algorithm~\ref{#1}}
49	% Reference to an algorithm, upper case.
50	\def\Algref#1{Algorithm~\ref{#1}}
51	\def\twoalgref#1#2{algorithms \ref{#1} and \ref{#2}}
52	\def\Twoalgref#1#2{Algorithms \ref{#1} and \ref{#2}}
53	% Reference to a
…[truncated 12236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-22T01:47:35.516919+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 审稿意见：Temporal Measurement Instability in LLM Benchmarks\n\n---\n\n### Summary (2-3 句)\n\n本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，发现 METABENCH 六个 benchmark 中 17.9%–31.3% 的题目在 2023 与 2024 模型 cohort 之间存在大幅度时序测量不稳定性（ETS-C 分类）。作者提出 cross-subject matching 的半合成注入框架实现 ΔFPR=0.000，并揭示 web-overlap 污染标签与 DIF flag 近乎独立（enrichment≈0.96），指出现有污染检测的 ground truth 存在类别错误。论文方法论严谨、robustness check 覆盖面广，但在注入模型的 ecological validity、因果归因能力、以及 DIF 方法对 LLM 群体适用性的论证上存在值得讨论的问题。\n\n---\n\n### Strengths\n\n**S1 [方法论贡献清晰且可复用]**\nCross-subject matching 实现 ΔFPR=0.000 的方法贡献干净利落（Section 3.4, Remark），multi-subject injection 的优雅退化分析（Appendix Table 5：k≤5 时 ΔFPR<0.007，k=10 时升至 0.047）为实际应用划定了清晰的适用边界。这个 matching 策略本身可以独立于本文的具体分析场景使用。\n\n**S2 [Robustness check 覆盖面极广]**\n论文系统性地排除了 6 种替代解释（ability confounding, family inflation, θ-conditioning, within-subject effects, ranking impact, local dependence），C% 在多种 matching 策略下均稳定在 ~28-29% 的底线（Section 4.4, Table 2）。随机拆分对照组 C%=0.18% 与能力分位数对照组 C%=2.9% 提供了有说服力的 null baseline。这种论证深度在 benchmark 评估类论文中少见。\n\n**S3 [Ground truth meta-critique 具有启发性]**\n揭示 web-overlap labels 与 DIF flags 近乎正交（enrichment=0.964, Jaccard=0.206, φ=0.012; Section 4.3）是一个重要的方法论洞察。这不仅对本文有意义，也挑战了整个污染检测社区的评估范式——任何以 web-overlap 作为 ground truth 验证 differential detector 的工作都面临同样的类别错误。\n\n**S4 [跨 benchmark 复现]**\n六个 benchmark 均展示显著 temporal DIF（45-174× above baseline; Table 3），且 knowledge/reasoning benchmark（C%≥26.9%）高于 procedural benchmark（C%≤18.9%）的模式合理且有可解释性。\n\n**S5 [统计报告规范]**\n几乎所有核心数字都附有 CI/效应量/多重比较校正。ETS-C 的双阈值机制本身就提供了隐式多重检验控制，BH-FDR 校正后仅移除 3 项（31.32%→31.30%）的结果进一步证实了这一点。\n\n**S6 [Simpson's paradox 分析精巧]**\nItem-level regression 揭示 92.4% 的 DIF 信号是 item-specific（pseudo R²=0.0007），而 domain-level accuracy 的效应在控制 item properties 后反转（OR: 1.55→0.73），这是区分 item-level 与 domain-level 效应的有力证据（Section 4.2）。\n\n---\n\n### Weaknesses\n\n**W1 [warning] 半合成注入的 ecological validity 不足，限制了 TPR/FPR 的实际可解释性**\n- 具体位置：Section 3.4, Limitations paragraph 1\n- 问题：Binary flipping（incorrect→correct）是一种最极端的均匀利用模式。真实的 contamination 表现为部分记忆、推理捷径、格式敏感性等，其在 response matrix 上的影响模式远比 uniform flipping 复杂。论文承认这是 \"worst-case uniform exploitation\"，但这意味着 ΔTPR=+0.508 at p=0.5 这个数字的实际参考价值有限——对于更现实的 contamination pattern，detection power 可能显著不同（可能更低，因为信号更弱更分散）。\n- 建议：至少提供一种更现实的注入模型作为 robustness check，例如 (a) 按 item difficulty 分层的非均匀 flipping（难题更容易被 memorize），或 (b) 仅翻转高区分度 items 的 subset。这不需要大量额外实验，但能显著增强 power analysis 的说服力。\n\n**W2 [warning] 对 LLM 群体应用 MH-DIF 的理论适用性论证不够充分**\n- 具体位置：Section 3.2 \"LLM-specific challenges\" paragraph\n- 问题：论文列举了 4 个 LLM-specific challenge（local dependence, family structure, non-normal ability distribution, multidimensionality），但每个只是简要提及对应的处理措施。核心的理论空白在于：MH 统计量的大样本性质（渐近 χ² 分布）依赖 examinees 的独立性假设。LLM \"examinees\" 不是独立采样的——它们共享训练数据、架构、甚至是 fine-tuning 的 base model。Graduated de-duplication 在经验层面处理了这个问题，但论文没有讨论 non-independence 对 MH χ² test 的 type-I error rate 的理论影响。\n- 建议：增加一个段落讨论 MH test 在 clustered/non-independent examinees 下的 size 表现，可引用教育测量中 multi-level DIF 分析的相关文献（如 French & Finch, 2010 关于 clustered data 中 DIF detection 的研究）。或者提供 permutation-based p-values 作为 non-parametric 替代（论文已有 permutation test，但仅用于 null C% 而非每个 item 的 DIF p-value）。\n\n**W3 [warning] 因果归因能力的局限性使得 \"measurement instability\" 的 framing 可能误导**\n- 具体位置：Abstract, Title, Section 5.1\n- 问题：论文反复强调 \"31% measurement instability\" 并建议在 C%≥25% 时 \"rotate or retire flagged items\"（Section 5.3）。但 Discussion (Section 5.1) 也承认无法区分 DIF 是源于 contamination、capability evolution 还是 training methodology shift。如果 DIF 源于 genuine capability evolution（例如 2024 模型确实在某些推理维度上更强），那么这些 items 的 differential functioning 恰恰是 benchmark 应该测量的——retire 这些 items 反而会丢失有价值的区分信息。论文在 Downstream Impact（Section 4.5）中也证明了 DIF items 承载更多 discriminative signal（z = -8σ to -49σ），这与 \"retire flagged items\" 的建议存在张力。\n- 建议：在 Discussion 中更明确地讨论这个张力——何时 DIF 是 \"measurement instability\"（问题），何时是 \"expected sensitivity to genuine change\"（特征）。目前的三层框架（impact/DIF/attribution）很好但最后一层完全悬空。\n\n**W4 [info] Permutation test 的迭代次数偏少**\n- 具体位置：Section 4.2\n- 问题：主 permutation test 使用 200 次标签打乱，p=0.005 恰好是分辨率极限（1/200=0.005）。虽然论文标注了 \"resolution limit\" 且补充了 per-subject permutation（1,000×8 subjects），但主检验的 200 次迭代给出的 p-value 实质上只能说明 p≤0.005。\n- 建议：增加到至少 1,000 次 permutation（计算代价可忽略，因为只需重新运行 MH 统计），以获得更精确的 p-value 估计。\n\n**W5 [info] ρ≈0.997 排名相关性的解读需要更多 nuance**\n- 具体位置：Section 4.5, Abstract\n- 问题：从 12,508 items 移除 ~31% 后排名相关性仍为 0.997，这在一定程度上是 MMLU 的高冗余度的体现，而非 DIF items 不重要的证据。论文在 Discussion 中提到 family-level 排名位移（Llama-3 +53, Mistral -35），但这些位移被整体 ρ≈0.997 的叙事所掩盖。建议同时报告 pairwise model comparison 翻转率（即在 full vs stable-only 评估下，多少对模型的优劣排序发生逆转），这比 Spearman ρ 更能反映实际影响。\n\n**W6 [warning] Cross-subject matching 中 \"subject\" 粒度对 DIF 结果的敏感性未充分分析**\n- 具体位置：Section 3.2, Section 3.4\n- 问题：MMLU 的 57 个 subjects 大小差异很大（从几十到几百道题），cross-subject matching 排除当前 subject 后剩余 items 数量差异也很大。对于小 subject（例如只有 ~100 道题），排除它对 matching variable 的影响微乎其微，这意味着 matching variable 仍然部分包含了被测 items 的信号——特别是在 MMLU 这样的多 subject benchmark 中。论文没有分析 subject 大小与 DIF detection rate 之间的关系。\n- 建议：报告 subject-level C% 与 subject size 的相关性。如果小 subject 的 C% 系统性偏高，则暗示 matching variable contamination 未被完全消除。\n\n---\n\n### Questions\n\n**Q1**: Section 4.2 报告 1:1 nearest-neighbor matching 后 C%=28.9%±0.1%，比 unmatched 31.3% 低约 2.4pp。这个 matching 是在 model 总分上做的还是在 IRT θ 上做的？如果是 model 总分，那么 matched 后 cohort 大小从 (1080, 807) 降到 (638, 638)——近半数模型被丢弃，这是否引入了 selection bias？\n\n**Q2**: Power analysis（Section 4.1）使用 PSN-IRT 的 2PL 参数（ā=1.2, b̄=-0.84），但 Appendix A.2 又提到 \"MMLU response matrix shows poor fit to a unidimensional 2PL model\"。如果 2PL 拟合差，那么基于 2PL 参数的 power analysis 结论的可靠性如何？论文是否考虑过使用非参数方法估计 power？\n\n**Q3**: Table 1 中 Within-subject 的 C%=38.1% 高于 Temporal 的 31.3%。这是因为 within-subject 分析中 matching variable 的 items 更少导致 stratification 噪声增大，还是因为 within-subject DIF 确实更严重？论文是否做了 simulation 来校准 within-subject DIF 分析的 expected type-I error rate？\n\n**Q4**: GSM1K 的相关性分析（r=-0.478, p=0.005, N=33）样本量很小且论文标注为 exploratory，但 Abstract 中 \"DIF captures capability change distinct from memorization\" 的措辞暗示这是一个已确立的结论。能否明确区分 confirmed findings 和 exploratory signals？\n\n**Q5**: Section 3.2 提到 \"IRT θ estimates correlate at r=0.9986 with total scores in our data\"。这个极高的相关性是否暗示在这个数据上 IRT θ 几乎不提供超越 CTT total score 的信息？如果是，那么整个 IRT framing 的附加价值是什么？\n\n---\n\n### Missing References\n\n- French, B. F., & Finch, W. H. (2010). Hierarchical logistic regression: Accounting for multilevel data in DIF detection. *Journal of Educational Measurement*, 47(3), 299–317. — 关于 clustered data 中 DIF 检测的多层次方法，与 W2 直接相关。\n- Magis, D., & De Boeck, P. (2012). A robust outlier approach to prevent type I error inflation in DIF. *Educational and Psychological Measurement*, 72(2), 291–311. — 关于 DIF 检测中 type-I error 控制的替代方法。\n- 论文引用了 Habba et al. (2026) 的 Growing Pains 关于 anchor-item calibration，但没有引用经典的 equating 文献（如 Kolen & Brennan, 2014, *Test Equating, Scaling, and Linking*），考虑到论文标题涉及 \"equated bench\"。\n\n---\n\n### Minor Issues\n\n- Abstract 行文密度很高，一句话中同时出现 ΔFPR=0.000, ΔTPR=+0.508, enrichment≈0.96, φ=0.012，对首次接触的读者不友好。建议拆分核心 contribution 和具体数字。\n- Section 3.2 的 ETS 分类定义中，Category B 的描述 \"all remaining items: those with 1.0≤|Δ_MH|<1.5, or |Δ_MH|≥1.5 without statistical significance\" 缺少 |Δ_MH|<1.0 但有统计显著性的情况——根据标准 ETS 分类，这些应属于 Category A，建议明确说明。\n- Figure 1 的 ICC 示意图很好但缺少 axis labels（x 轴应为 ability θ，y 轴应为 P(correct)），在 camera-ready 时建议补充。\n- Section 4.5 \"z = -8σ to -49σ vs. random removal\" 的 z 值含义在正文中不够直观——是什么量的 z-score？建议简要说明。\n- 论文正文约 8 页（含 figures/tables），在 ACL long paper 的 8 页限制内，格式合规。\n\n---\n\n### Overall Assessment\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n**一句话总结**: 方法论扎实且 robustness checks 印象深刻的 psychometric 审计工作，但半合成注入的 ecological validity 不足和因果归因能力的根本局限使得核心发现的 actionability 受限。\n\n**ACL ARR 维度打分**:\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | MH-DIF 应用基本正确，统计检验规范，但 examinees 非独立性的理论影响未充分分析（W2），semi-synthetic injection 的 ecological validity 不足（W1） |\n| Excitement | 3/5 | 将成熟的 psychometric 方法应用到 LLM 评估是有价值的跨领域工作，ground truth meta-critique 有启发性，但核心方法是既有技术的直接应用，novelty 有限 |\n| Reproducibility | 4/5 | 数据公开（METABENCH），代码提供匿名链接，方法描述详细（K=5 strata, ETS thresholds 等），统计细节充分 |\n| Datasets | 3/5 | 未发布新数据集，但对现有数据集的分析有参考价值 |\n| Software | 3/5 | 提供了 DIF audit scripts |\n\n**Reviewer Confidence**: 4/5 — 熟悉 IRT/DIF 方法论和 LLM benchmark 评估，仔细检查了核心统计论证。\n\n**理由**: 这篇论文在技术执行上高于平均水平，robustness checks 的覆盖面令人印象深刻，ground truth meta-critique 是一个有价值的方法论洞察。但有两个因素限制了评分：(1) 核心方法（MH-DIF）是教育测量领域的标准工具，创新主要在于应用场景而非方法本身；(2) 无法区分 contamination 和 genuine capability evolution 这一根本局限使得 \"31% measurement instability\" 的发现难以转化为明确的行动指导——retire flagged items 可能丢弃有价值的 discriminative items，保留它们则 instability 持续存在。如果作者能提供更现实的注入模型（W1）和更充分的 LLM examinees 非独立性分析（W2），本文可以达到 Conference 水准。\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 审稿意见：Temporal Measurement Instability in LLM Benchmarks\n\n---\n\n### Summary (2-3 句)\n\n本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，发现 METABENCH 六个 benchmark 中 17.9%–31.3% 的题目在 2023 与 2024 模型 cohort 之间存在大幅度时序测量不稳定性（ETS-C 分类）。作者提出 cross-subject matching 的半合成注入框架实现 ΔFPR=0.000，并揭示 web-overlap 污染标签与 DIF flag 近乎独立（enrichment≈0.96），指出现有污染检测的 ground truth 存在类别错误。论文方法论严谨、robustness check 覆盖面广，但在注入模型的 ecological validity、因果归因能力、以及 DIF 方法对 LLM 群体适用性的论证上存在值得讨论的问题。\n\n---\n\n### Strengths\n\n**S1 [方法论贡献清晰且可复用]**\nCross-subject matching 实现 ΔFPR=0.000 的方法贡献干净利落（Section 3.4, Remark），multi-subject injection 的优雅退化分析（Appendix Table 5：k≤5 时 ΔFPR<0.007，k=10 时升至 0.047）为实际应用划定了清晰的适用边界。这个 matching 策略本身可以独立于本文的具体分析场景使用。\n\n**S2 [Robustness check 覆盖面极广]**\n论文系统性地排除了 6 种替代解释（ability confounding, family inflation, θ-conditioning, within-subject effects, ranking impact, local dependence），C% 在多种 matching 策略下均稳定在 ~28-29% 的底线（Section 4.4, Table 2）。随机拆分对照组 C%=0.18% 与能力分位数对照组 C%=2.9% 提供了有说服力的 null baseline。这种论证深度在 benchmark 评估类论文中少见。\n\n**S3 [Ground truth meta-critique 具有启发性]**\n揭示 web-overlap labels 与 DIF flags 近乎正交（enrichment=0.964, Jaccard=0.206, φ=0.012; Section 4.3）是一个重要的方法论洞察。这不仅对本文有意义，也挑战了整个污染检测社区的评估范式——任何以 web-overlap 作为 ground truth 验证 differential detector 的工作都面临同样的类别错误。\n\n**S4 [跨 benchmark 复现]**\n六个 benchmark 均展示显著 temporal DIF（45-174× above baseline; Table 3），且 knowledge/reasoning benchmark（C%≥26.9%）高于 procedural benchmark（C%≤18.9%）的模式合理且有可解释性。\n\n**S5 [统计报告规范]**\n几乎所有核心数字都附有 CI/效应量/多重比较校正。ETS-C 的双阈值机制本身就提供了隐式多重检验控制，BH-FDR 校正后仅移除 3 项（31.32%→31.30%）的结果进一步证实了这一点。\n\n**S6 [Simpson's paradox 分析精巧]**\nItem-level regression 揭示 92.4% 的 DIF 信号是 item-specific（pseudo R²=0.0007），而 domain-level accuracy 的效应在控制 item properties 后反转（OR: 1.55→0.73），这是区分 item-level 与 domain-level 效应的有力证据（Section 4.2）。\n\n---\n\n### Weaknesses\n\n**W1 [warning] 半合成注入的 ecological validity 不足，限制了 TPR/FPR 的实际可解释性**\n- 具体位置：Section 3.4, Limitations paragraph 1\n- 问题：Binary flipping（incorrect→correct）是一种最极端的均匀利用模式。真实的 contamination 表现为部分记忆、推理捷径、格式敏感性等，其在 response matrix 上的影响模式远比 uniform flipping 复杂。论文承认这是 \"worst-case uniform exploitation\"，但这意味着 ΔTPR=+0.508 at p=0.5 这个数字的实际参考价值有限——对于更现实的 contamination pattern，detection power 可能显著不同（可能更低，因为信号更弱更分散）。\n- 建议：至少提供一种更现实的注入模型作为 robustness check，例如 (a) 按 item difficulty 分层的非均匀 flipping（难题更容易被 memorize），或 (b) 仅翻转高区分度 items 的 subset。这不需要大量额外实验，但能显著增强 power analysis 的说服力。\n\n**W2 [warning] 对 LLM 群体应用 MH-DIF 的理论适用性论证不够充分**\n- 具体位置：Section 3.2 \"LLM-specific challenges\" paragraph\n- 问题：论文列举了 4 个 LLM-specific challenge（local dependence, family structure, non-normal ability distribution, multidimensionality），但每个只是简要提及对应的处理措施。核心的理论空白在于：MH 统计量的大样本性质（渐近 χ² 分布）依赖 examinees 的独立性假设。LLM \"examinees\" 不是独立采样的——它们共享训练数据、架构、甚至是 fine-tuning 的 base model。Graduated de-duplication 在经验层面处理了这个问题，但论文没有讨论 non-independence 对 MH χ² test 的 type-I error rate 的理论影响。\n- 建议：增加一个段落讨论 MH test 在 clustered/non-independent examinees 下的 size 表现，可引用教育测量中 multi-level DIF 分析的相关文献（如 French & Finch, 2010 关于 clustered data 中 DIF detection 的研究）。或者提供 permutation-based p-values 作为 non-parametric 替代（论文已有 permutation test，但仅用于 null C% 而非每个 item 的 DIF p-value）。\n\n**W3 [warning] 因果归因能力的局限性使得 \"measurement instability\" 的 framing 可能误导**\n- 具体位置：Abstract, Title, Section 5.1\n- 问题：论文反复强调 \"31% measurement instability\" 并建议在 C%≥25% 时 \"rotate or retire flagged items\"（Section 5.3）。但 Discussion (Section 5.1) 也承认无法区分 DIF 是源于 contamination、capability evolution 还是 training methodology shift。如果 DIF 源于 genuine capability evolution（例如 2024 模型确实在某些推理维度上更强），那么这些 items 的 differential functioning 恰恰是 benchmark 应该测量的——retire 这些 items 反而会丢失有价值的区分信息。论文在 Downstream Impact（Section 4.5）中也证明了 DIF items 承载更多 discriminative signal（z = -8σ to -49σ），这与 \"retire flagged items\" 的建议存在张力。\n- 建议：在 Discussion 中更明确地讨论这个张力——何时 DIF 是 \"measurement instability\"（问题），何时是 \"expected sensitivity to genuine change\"（特征）。目前的三层框架（impact/DIF/attribution）很好但最后一层完全悬空。\n\n**W4 [info] Permutation test 的迭代次数偏少**\n- 具体位置：Section 4.2\n- 问题：主 permutation test 使用 200 次标签打乱，p=0.005 恰好是分辨率极限（1/200=0.005）。虽然论文标注了 \"resolution limit\" 且补充了 per-subject permutation（1,000×8 subjects），但主检验的 200 次迭代给出的 p-value 实质上只能说明 p≤0.005。\n- 建议：增加到至少 1,000 次 permutation（计算代价可忽略，因为只需重新运行 MH 统计），以获得更精确的 p-value 估计。\n\n**W5 [info] ρ≈0.997 排名相关性的解读需要更多 nuance**\n- 具体位置：Section 4.5, Abstract\n- 问题：从 12,508 items 移除 ~31% 后排名相关性仍为 0.997，这在一定程度上是 MMLU 的高冗余度的体现，而非 DIF items 不重要的证据。论文在 Discussion 中提到 family-level 排名位移（Llama-3 +53, Mistral -35），但这些位移被整体 ρ≈0.997 的叙事所掩盖。建议同时报告 pairwise model comparison 翻转率（即在 full vs stable-only 评估下，多少对模型的优劣排序发生逆转），这比 Spearman ρ 更能反映实际影响。\n\n**W6 [warning] Cross-subject matching 中 \"subject\" 粒度对 DIF 结果的敏感性未充分分析**\n- 具体位置：Section 3.2, Section 3.4\n- 问题：MMLU 的 57 个 subjects 大小差异很大（从几十到几百道题），cross-subject matching 排除当前 subject 后剩余 items 数量差异也很大。对于小 subject（例如只有 ~100 道题），排除它对 matching variable 的影响微乎其微，这意味着 matching variable 仍然部分包含了被测 items 的信号——特别是在 MMLU 这样的多 subject benchmark 中。论文没有分析 subject 大小与 DIF detection rate 之间的关系。\n- 建议：报告 subject-level C% 与 subject size 的相关性。如果小 subject 的 C% 系统性偏高，则暗示 matching variable contamination 未被完全消除。\n\n---\n\n### Questions\n\n**Q1**: Section 4.2 报告 1:1 nearest-neighbor matching 后 C%=28.9%±0.1%，比 unmatched 31.3% 低约 2.4pp。这个 matching 是在 model 总分上做的还是在 IRT θ 上做的？如果是 model 总分，那么 matched 后 cohort 大小从 (1080, 807) 降到 (638, 638)——近半数模型被丢弃，这是否引入了 selection bias？\n\n**Q2**: Power analysis（Section 4.1）使用 PSN-IRT 的 2PL 参数（ā=1.2, b̄=-0.84），但 Appendix A.2 又提到 \"MMLU response matrix shows poor fit to a unidimensional 2PL model\"。如果 2PL 拟合差，那么基于 2PL 参数的 power analysis 结论的可靠性如何？论文是否考虑过使用非参数方法估计 power？\n\n**Q3**: Table 1 中 Within-subject 的 C%=38.1% 高于 Temporal 的 31.3%。这是因为 within-subject 分析中 matching variable 的 items 更少导致 stratification 噪声增大，还是因为 within-subject DIF 确实更严重？论文是否做了 simulation 来校准 within-subject DIF 分析的 expected type-I error rate？\n\n**Q4**: GSM1K 的相关性分析（r=-0.478, p=0.005, N=33）样本量很小且论文标注为 exploratory，但 Abstract 中 \"DIF captures capability change distinct from memorization\" 的措辞暗示这是一个已确立的结论。能否明确区分 confirmed findings 和 exploratory signals？\n\n**Q5**: Section 3.2 提到 \"IRT θ estimates correlate at r=0.9986 with total scores in our data\"。这个极高的相关性是否暗示在这个数据上 IRT θ 几乎不提供超越 CTT total score 的信息？如果是，那么整个 IRT framing 的附加价值是什么？\n\n---\n\n### Missing References\n\n- French, B. F., & Finch, W. H. (2010). Hierarchical logistic regression: Accounting for multilevel data in DIF detection. *Journal of Educational Measurement*, 47(3), 299–317. — 关于 clustered data 中 DIF 检测的多层次方法，与 W2 直接相关。\n- Magis, D., & De Boeck, P. (2012). A robust outlier approach to prevent type I error inflation in DIF. *Educational and Psychological Measurement*, 72(2), 291–311. — 关于 DIF 检测中 type-I error 控制的替代方法。\n- 论文引用了 Habba et al. (2026) 的 Growing Pains 关于 anchor-item calibration，但没有引用经典的 equating 文献（如 Kolen & Brennan, 2014, *Test Equating, Scaling, and Linking*），考虑到论文标题涉及 \"equated bench\"。\n\n---\n\n### Minor Issues\n\n- Abstract 行文密度很高，一句话中同时出现 ΔFPR=0.000, ΔTPR=+0.508, enrichment≈0.96, φ=0.012，对首次接触的读者不友好。建议拆分核心 contribution 和具体数字。\n- Section 3.2 的 ETS 分类定义中，Category B 的描述 \"all remaining items: those with 1.0≤|Δ_MH|<1.5, or |Δ_MH|≥1.5 without statistical significance\" 缺少 |Δ_MH|<1.0 但有统计显著性的情况——根据标准 ETS 分类，这些应属于 Category A，建议明确说明。\n- Figure 1 的 ICC 示意图很好但缺少 axis labels（x 轴应为 ability θ，y 轴应为 P(correct)），在 camera-ready 时建议补充。\n- Section 4.5 \"z = -8σ to -49σ vs. random removal\" 的 z 值含义在正文中不够直观——是什么量的 z-score？建议简要说明。\n- 论文正文约 8 页（含 figures/tables），在 ACL long paper 的 8 页限制内，格式合规。\n\n---\n\n### Overall Assessment\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n**一句话总结**: 方法论扎实且 robustness checks 印象深刻的 psychometric 审计工作，但半合成注入的 ecological validity 不足和因果归因能力的根本局限使得核心发现的 actionability 受限。\n\n**ACL ARR 维度打分**:\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | MH-DIF 应用基本正确，统计检验规范，但 examinees 非独立性的理论影响未充分分析（W2），semi-synthetic injection 的 ecological validity 不足（W1） |\n| Excitement | 3/5 | 将成熟的 psychometric 方法应用到 LLM 评估是有价值的跨领域工作，ground truth meta-critique 有启发性，但核心方法是既有技术的直接应用，novelty 有限 |\n| Reproducibility | 4/5 | 数据公开（METABENCH），代码提供匿名链接，方法描述详细（K=5 strata, ETS thresholds 等），统计细节充分 |\n| Datasets | 3/5 | 未发布新数据集，但对现有数据集的分析有参考价值 |\n| Software | 3/5 | 提供了 DIF audit scripts |\n\n**Reviewer Confidence**: 4/5 — 熟悉 IRT/DIF 方法论和 LLM benchmark 评估，仔细检查了核心统计论证。\n\n**理由**: 这篇论文在技术执行上高于平均水平，robustness checks 的覆盖面令人印象深刻，ground truth meta-critique 是一个有价值的方法论洞察。但有两个因素限制了评分：(1) 核心方法（MH-DIF）是教育测量领域的标准工具，创新主要在于应用场景而非方法本身；(2) 无法区分 contamination 和 genuine capability evolution 这一根本局限使得 \"31% measurement instability\" 的发现难以转化为明确的行动指导——retire flagged items 可能丢弃有价值的 discriminative items，保留它们则 instability 持续存在。如果作者能提供更现实的注入模型（W1）和更充分的 LLM examinees 非独立性分析（W2），本文可以达到 Conference 水准。\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-22T01:47:39.434416+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3917
}
```

</details>

---


### Assistant

_source line 414 · 2026-05-22T01:47:49.096817+00:00_

审稿意见已提交给 Review Director。

**审稿总结**：

- **Overall**: 3.5/5 (Borderline Conference)
- **Soundness**: 3.5/5 — MH-DIF 应用基本正确，但 LLM examinees 非独立性的理论影响未充分讨论
- **Excitement**: 3/5 — 有价值的跨领域应用，但核心方法为既有技术
- **Reproducibility**: 4/5

**主要优势**：cross-subject matching 实现零 FPR 的方法贡献、极广的 robustness checks（6 种替代解释均被排除）、ground truth meta-critique 挑战污染检测社区的评估范式。

**关键问题**：
- **W1**: 半合成注入的 binary flipping 远离真实 contamination 模式，TPR 数字的实际参考价值有限
- **W2**: 对 LLM 群体（非独立 examinees）应用 MH-DIF 的理论适用性论证不足
- **W3**: 无法区分 contamination 与 genuine capability evolution，"retire flagged items" 建议与 DIF items 承载 discriminative signal 的发现存在张力
- **W6**: Cross-subject matching 中 subject 粒度的敏感性未分析

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 15

## Round 15

4 recorded events


### User

_source line 415 · 2026-05-22T01:49:07.204518+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应每个 Strength、Weakness 和 Question：用 **[AGREE]** 表示同意并说明理由，或用 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。

对 Reviewer 2 的 Missing References 和 Minor Issues 也请简要表态（同意/不同意/补充）。

---

## Reviewer 2 审稿意见 — Round 1

**论文**: Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models
**Venue**: EMNLP 2026 via ACL Rolling Review (May cycle)

---

### Summary (2-3 句)

本文将教育测量中成熟的 Mantel-Haenszel 差异项目功能（MH-DIF）分析方法应用于 LLM benchmark 评估，在 METABENCH 数据集（5,227 模型 × 12,508 MMLU 题目）上发现约 31% 的题目在 2023–2024 模型群组间存在显著时序 DIF（ETS C 级），但排名相关性仍高达 ρ ≈ 0.997。论文同时构建了带跨学科匹配的半合成注入验证框架（ΔFPR = 0.000），并指出 web-overlap 污染标签与 DIF 标记近乎独立（enrichment ≈ 0.96），揭示了现有污染检测验证方法论中的类别错误。

---

### Strengths

**S1** [Rigorous Experimental Design] 实验设计非常严谨，采用了多层对照：随机分割对照（C% = 0.18%）、能力分位对照（2.9%）、族内对照（Llama-2 vs. 3: 61.3%）、1:1 最近邻匹配（C% = 28.9%）、排列检验（p = 0.005），系统地排除了能力混淆、家族结构膨胀、分层方法选择等替代解释（Section 4.4, Table 2）。这种多重 robustness 检查在 NLP 领域的实证论文中很少见。

**S2** [Ground Truth Meta-Critique] Contribution 2（Section 4.3）指出 web-overlap 标签衡量的是 global exposure 而非 differential functioning，两者 enrichment = 0.964、Jaccard = 0.206、φ = 0.012，这是一个重要的方法论洞察，对整个 contamination detection 领域的验证实践有直接影响。这一发现具有超越本文的价值。

**S3** [Cross-Benchmark Replication] 在所有 6 个 METABENCH benchmark 上复现了 temporal DIF 现象（C% = 17.9%–31.3%，45–174× 高于随机基线），且发现 knowledge/reasoning 类 benchmark 的 DIF 率系统性高于 procedural 类（Table 3），增强了结论的 generalizability。

**S4** [Semi-Synthetic Framework] 跨学科匹配的半合成注入框架设计巧妙——通过从匹配变量中排除被注入学科，在理论上消除 FPR 膨胀（ΔFPR = 0.000），同时保持检测力（ΔTPR = +0.508 at p = 0.5）。Remark (Section 3.4) 提供了 FPR = 0 的构造性论证。

**S5** [Conceptual Distinction] Figure 1 清晰地用 ICC 曲线区分了 global contamination 和 differential contamination，这一概念框架有助于读者理解为何 DIF 和 web-overlap 标签测量不同的构念。

---

### Weaknesses

**W1** [critical] **Practical Significance Paradox: ρ ≈ 0.997 严重削弱了 "instability" 叙事的力度**
- 具体位置：Title, Abstract, Section 4.6, Section 5.1
- 问题：论文标题声称 "Measurement Instability"，Abstract 和全文反复强调 31% 的 items 存在 temporal DIF。但 Section 4.6 表明去除全部 DIF 标记项后 Spearman ρ ≈ 0.997——即排名几乎不变。这构成了一个严重的 framing 矛盾：如果去除近三分之一的题目对排名毫无影响，那么这种 "instability" 的实际意义何在？论文试图用 "diagnostic, not destructive" 来调和，但这种表述未能回答一个关键问题：为什么社区应该关注一种不影响实际使用（模型排名）的统计现象？文中提到的 family-level rank shifts（Llama-3: +53, Mistral: -35）是更有说服力的 practical impact 证据，但这些数据被淹没在 ρ ≈ 0.997 的叙事中，且仅出现在附录图中。
- 建议修改方向：(1) 重新 frame 论文核心叙事——强调 DIF 作为 capability dimension shift 的诊断工具，而非 benchmark 可靠性的威胁；(2) 将 family-level rank profile 分析从附录提升到正文，作为 practical significance 的主要证据；(3) 讨论 ρ ≈ 0.997 是因为 MMLU 有 12,508 items 的冗余度——在 items 更少的 benchmark（如 TruthfulQA, 817 items）上 DIF 的排名影响可能更大，应提供这些 benchmark 的 ρ 值。

**W2** [critical] **因果归因空白使 audit protocol 的 actionability 存疑**
- 具体位置：Section 5.3, Limitations ¶1
- 问题：Section 5.3 提出了分级行动协议（Monitor/Flag/Act），当 C% ≥ 25% 时建议 "rotate or retire flagged items"。但 Limitations 明确承认 DIF 无法区分 contamination、capability evolution 和 training methodology shifts。如果 DIF 标记的 items 实际上正确反映了模型能力的真实进步，DIF items 集中了辨别信号（z = -8σ to -49σ），retire 这些 items 将移除最具辨别力的题目。
- 建议修改方向：将 "Act: rotate or retire" 改为更保守的 "investigate and report alongside stable-item rankings"。

**W3** [warning] **方法新颖性有限——标准方法应用于新领域**
- 具体位置：Section 3.2, Related Work ¶3
- 问题：MH-DIF 是 1988 年的标准方法，ETS 分类是标准实践。对于 EMNLP 主会议，方法新颖性不足可能是一个顾虑——论文的价值主要在实证发现和方法论批判。
- 建议：更加突出 C2（ground truth meta-critique）作为主要贡献。

**W4** [warning] **`\enlargethispage{18\baselineskip}` 格式操作过于激进**
- 具体位置：`sections/discussion.tex`, line 3
- 问题：Discussion section 使用了 `\enlargethispage{18\baselineskip}`，相当于额外增加约 18 行文本空间（≈8.3 cm）。如此大幅度的 margin manipulation 可能被 PC 视为规避页数限制。去除此命令后主体文本很可能溢出到第 9 页。

**W5** [warning] **半合成框架的注入模型过于简化**
- 具体位置：Section 3.4, Limitations ¶1
- 问题：ΔTPR = +0.508 at p = 0.5 意味着在最有利条件下也只有约 50% 的检测率。更现实的部分记忆场景下检测力可能进一步下降。
- 建议：明确区分框架对 FPR 控制（不依赖注入模型现实性）和 TPR 估计（受注入模型限制）的贡献强度。

**W6** [warning] **关键统计量的重复呈现降低信息密度**
- 问题：enrichment ≈ 0.964, ρ ≈ 0.997, 31%, ΔFPR = 0.000, ΔTPR = +0.508 等在论文中重复 4-6 次。Discussion 几乎完全重复 Experiments 的数字，Conclusion 仅两行。

---

### Questions

**Q1** Table 3 中其他 benchmark（尤其是 items 较少的 TruthfulQA, 817 items）的 stable-item vs. full ranking ρ 值是多少？
**Q2** difficulty-direction interaction ρ = -0.597 是否在 6 个 benchmark 上都一致？
**Q3** 6 个月窗口分析 C% = 34.35% 是否暗示 calendar year 划分低估了 temporal DIF？
**Q4** Section 5.3 建议 500 个新模型累积时运行 DIF，阈值依据是什么？
**Q5** 在单一 domain benchmark（如 GSM8K）上，跨学科匹配如何实现？

---

### Missing References

1. Polo et al. (2024) "Efficient Multi-Prompt Evaluation of LLMs" — IRT-based efficient evaluation
2. Putnick & Bornstein (2016) "Measurement invariance conventions and reporting" — DIF 方法论的跨学科支撑

### Minor Issues

- M1: Figure 2 缺少 confidence bands
- M2: Table 1 "--" 列应注明原因
- M3: Figure 5 N=33 outlier 影响
- M4: holland1988mh 出版年份可能为 1986
- M5: Appendix "Yen's Q3" 未在正文定义

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-22T01:51:02.356142+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 Round 1 审稿意见的逐条回应\n\n---\n\n### Strengths 回应\n\n**[AGREE] R2-S1 (Rigorous Experimental Design)**\n完全同意。多层对照设计是本文最大的方法论优势，与我在 R1-S2 中的评价一致。特别值得强调的是，六种替代解释的系统排除（Section 4.4, Table 2）和 ~28-29% 的 C% floor 在多种 matching 策略下的一致性，在 NLP 实证论文中确实罕见。\n\n**[AGREE] R2-S2 (Ground Truth Meta-Critique)**\n完全同意，与我的 R1-S3 一致。enrichment=0.964、Jaccard=0.206、φ=0.012 的正交性发现（Section 4.3）对整个 contamination detection 领域的验证范式有超越本文的影响。\n\n**[AGREE] R2-S3 (Cross-Benchmark Replication)**\n同意，与我的 R1-S4 一致。六个 benchmark 的复现（Table 3）增强了 generalizability，knowledge vs. procedural 的差异模式合理。\n\n**[AGREE] R2-S4 (Semi-Synthetic Framework)**\n同意，与我的 R1-S1 一致。cross-subject matching 的 Remark（Section 3.4）提供了干净的构造性论证。\n\n**[AGREE] R2-S5 (Conceptual Distinction)**\n同意。Figure 1 的 ICC 示意图有效地帮助读者区分 global vs. differential contamination 这两个容易混淆的概念。不过我在 Minor Issues 中指出 Figure 1 缺少 axis labels（θ vs. P(correct)），建议在 camera-ready 时补充。\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R2-W1 (Practical Significance Paradox: ρ ≈ 0.997)**\n基本同意，这与我的 R1-W5 高度重叠。ρ ≈ 0.997 确实削弱了 \"instability\" 叙事的紧迫性。R2 的三点建议都很好，特别是第三点——在 items 更少的 benchmark 上报告 ρ 值。TruthfulQA 只有 817 items（Table 3），如果其 C%=29.7%，去除 ~240 个 DIF items 后对排名的影响可能远大于 MMLU。论文没有提供这个数据是一个明显的遗漏。\n\n不过我想补充一个 nuance：R2 将此标为 [critical] 可能稍重。论文在 Section 4.5 中确实提到了 family-level rank shifts（Llama-3: +53, Mistral: -35），这些 shift 对 pairwise model selection 有实际意义。问题不在于发现本身无意义，而在于论文的 framing 重心放错了——应该从 \"benchmark reliability threat\" 转向 \"diagnostic tool for capability dimension shifts\"。这是 framing 问题，不是 substance 问题。\n\n**[AGREE] R2-W2 (因果归因空白使 audit protocol actionability 存疑)**\n完全同意，这与我的 R1-W3 高度一致。Section 5.3 的 \"rotate or retire\" 建议与 Section 4.5 中 DIF items 承载 z = -8σ to -49σ 的 discriminative signal 这一发现之间存在直接矛盾。R2 建议改为 \"investigate and report alongside stable-item rankings\" 更为合理。我在 R1-W3 中也提出了类似建议——论文需要更明确地讨论何时 DIF 是问题（measurement artifact）vs. 特征（genuine sensitivity to change）。\n\n**[REBUT] R2-W3 (方法新颖性有限)**\n部分不同意。R2 认为 \"MH-DIF 是 1988 年的标准方法，方法新颖性不足\"，这个批评本身成立但不应作为 EMNLP 论文的主要 weakness。理由如下：\n\n1. ARR reviewer guidelines 明确指出不应因方法不够 \"complex\" 而贬低论文——\"simpler methods that work should not be penalized\"（H14 pitfall）。\n2. 本文的贡献定位为 \"methodological and empirical, not algorithmic\"（Section 1 最后一段），这是合理的。\n3. Cross-subject matching 的 ΔFPR=0.000 保证（Section 3.4 Remark）虽然建立在 MH-DIF 之上，但作为针对 LLM benchmark 场景的方法改进具有独立价值。\n4. Ground truth meta-critique（Contribution 2）本身就是方法论层面的新颖洞察。\n\nEMNLP Findings track 明确接收 \"sound and reproducible\" 的实证贡献。即使对 Main track 来说，novelty 可以来自问题定义和实证发现，而非必须来自方法本身。不过我同意 R2 的建议——更突出 C2 作为主要贡献会加强论文。\n\n**[AGREE] R2-W4 (`\\enlargethispage{18\\baselineskip}` 格式操作过于激进)**\n同意这是一个需要关注的问题。18\\baselineskip 约等于额外 18 行（~8-9 cm），这不是标准的微调而是大幅度 margin manipulation。从 discussion.tex line 3 的证据来看，如果去除此命令，Discussion section 很可能导致正文溢出到第 9 页，违反 EMNLP long paper 的 8 页限制。\n\n不过我要指出：这个问题属于格式合规范畴，不应影响论文的学术评价。如果正文确实在 8 页内（含 Discussion），作者可能需要在 camera-ready 时压缩 Discussion，但这是可操作的修改——重复性内容（R2-W6 指出的问题）的删减可以腾出空间。我不建议将此标为影响接收决定的因素。\n\n**[AGREE] R2-W5 (半合成框架注入模型过于简化)**\n同意，与我的 R1-W1 一致。我特别赞同 R2 提出的区分——框架对 FPR 控制的贡献（ΔFPR=0.000 不依赖注入模型现实性，因为这是 matching variable 构造的性质）与 TPR 估计的贡献（受注入模型限制）应该明确区分。论文在 Limitations 中已部分提到这一点（\"the framework's primary methodological contribution—cross-subject matching achieving ΔFPR=0.000—is a matching strategy property independent of injection realism\"），但在正文 Section 3.4 和 Section 4.1 中没有足够强调这个重要区分。\n\n**[REBUT] R2-W6 (关键统计量的重复呈现)**\n部分不同意。学术论文中核心数字在 Abstract→Introduction→Results→Discussion→Conclusion 的重复是正常的写作惯例，因为读者可能只读特定 section。但我承认本文的重复程度偏高——例如 enrichment≈0.964 在正文中出现了至少 5 次，ΔFPR=0.000 也出现了类似次数。\n\n然而，我不认为这是一个 weakness——它更多是 writing style 的问题。Discussion 的功能本就是将 Results 重新整合到更大的 context 中，必然会引用相同数字。Conclusion 只有两行恰恰是因为论文选择不再重复。R2 将此标为 [warning] 等级偏高——建议降为 Minor Issue。\n\n---\n\n### Questions 回应\n\n**[AGREE] R2-Q1 (其他 benchmark 的 stable-item vs. full ranking ρ)**\n这是一个关键遗漏。论文只报告了 MMLU 的 ρ≈0.997，但没有报告 TruthfulQA (817 items)、ARC (1,172 items)、GSM8K (1,319 items) 等较小 benchmark 的 ρ。考虑到这些 benchmark 的 item 数量仅为 MMLU 的 1/10 到 1/15，DIF items 的移除对排名的影响可能显著更大。这直接关系到 W1 中 practical significance 的评估。与我的 R1-W5 中建议报告 pairwise comparison flip rate 相呼应。\n\n**[AGREE] R2-Q2 (difficulty-direction interaction 跨 benchmark 一致性)**\n好问题。ρ=-0.597 仅在 MMLU 上报告（Section 4.2），如果这个模式在 GSM8K 或其他 benchmark 上也成立，将大大增强 \"hard items gain, easy items erode\" 这一发现的 generalizability。反之，如果不一致，可能暗示这是 MMLU 的特异性。\n\n**[AGREE] R2-Q3 (6 个月窗口 C%=34.35% 暗示 calendar year 划分可能低估)**\n有趣的观察。Section 4.7 提到 6 个月窗口（2023-H2 vs. 2024-H1）C%=34.35%，这确实高于全年 31.3%。可能的解释是 6 个月窗口内模型变化更集中，但论文没有深入分析。这暗示 temporal resolution 的选择影响 DIF 估计——如果更细粒度的时间划分产生更高的 C%，那么 31.3% 可能是一个保守估计。\n\n**[REBUT] R2-Q4 (500 模型阈值的依据)**\n这个问题可以从论文中部分回答。Section 4.1 的 power analysis 表明在 N≥80 per cohort 时 ETS-C 的 TPR 为 0.68-0.80（Appendix Table 4），论文的实际 cohort sizes（1,080 和 807）远超这个阈值。500 个新模型的建议（Section 5.3）虽然没有 formal justification，但考虑到 N≥80 的 power threshold，500 个新模型足以构成一个有统计效力的 focal group。不过我同意 R2 的暗示——这个阈值应该更明确地与 power analysis 结论挂钩。\n\n**[AGREE] R2-Q5 (单一 domain benchmark 上的跨学科匹配)**\n好问题，但论文已在 Section 3.2 中回答。论文定义了三种 matching 策略：(1) standard matching（within-benchmark total score），(2) cross-subject matching（排除当前 subject 的 total score），(3) external matching（使用不同 benchmark 的 total score）。对于 GSM8K 这样的单一 domain benchmark，使用策略 (3) external matching——例如用 MMLU total score 作为 matching variable。Appendix Table 6 中 GSM8K 的 ΔTPR 就是在 external matching 下报告的（$p=0.5$, external: +0.514）。不过论文确实没有在正文中对此做充分说明，应在 Section 3.2 或 Section 4.7 中明确 GSM8K 使用了 external matching。\n\n---\n\n### Missing References 回应\n\n**R2-Ref1 (Polo et al. 2024, IRT-based efficient evaluation)**\n[AGREE] 相关但非必须。论文 Related Work (Section 2) 已引用了 Polo et al. (2024) 关于 \"TinyBenchmarks\"（line numbers visible in related_work.tex），如果 R2 指的是另一篇 Polo et al. 工作则需要补充。\n\n**R2-Ref2 (Putnick & Bornstein 2016, Measurement invariance conventions)**\n[AGREE] 值得引用。Measurement invariance 的跨领域综述可以帮助 NLP 读者理解 DIF 在更广泛的 psychometric framework 中的位置。这与我在 R1 Missing References 中建议引用 Kolen & Brennan (2014) 的 equating 文献相呼应——论文整体上缺少经典 psychometric 综述文献。\n\n---\n\n### Minor Issues 回应\n\n**[AGREE] R2-M1 (Figure 2 缺少 confidence bands)**: 同意。5 random seeds 的变异应以 error bands 呈现。\n\n**[AGREE] R2-M2 (Table 1 \"--\" 列应注明原因)**: 同意。Within-family 和 Random split 行的 FPR/Enrichment 列为 \"--\"，应在 caption 或 footnote 中说明原因（可能是因为这些 cohort 没有对应的 web-overlap label 分析）。\n\n**[AGREE] R2-M3 (Figure 5 N=33 outlier 影响)**: 同意。N=33 且 r=-0.478 的相关性对 outlier 敏感。论文已标注为 exploratory，但应报告 robust correlation 或 leave-one-out 影响分析。与我的 R1-Q4 中关于 GSM1K 分析 exploratory nature 的关切一致。\n\n**[REBUT] R2-M4 (holland1988mh 出版年份)**: Holland & Thayer 的 MH-DIF 程序描述发表于 1988 年的 *ETS Research Report* 系列（RR-88-31），论文引用年份 1988 是正确的。R2 可能混淆了 Holland & Thayer (1988) 与 Mantel & Haenszel (1959) 的原始统计检验——后者确实更早，但论文引用的是 Holland & Thayer 对 DIF 检测的具体应用。\n\n**[AGREE] R2-M5 (Yen's Q3 未在正文定义)**: 同意。正文 Section 3.2 提到 \"permutation simulation... Q3 = 4.6-34.2%\" 但未解释 Q3 是什么。Appendix A.1 有详细描述，但正文首次提及时应至少加一句简要说明（如 \"Yen's Q3 statistic, which measures residual correlations between item pairs after conditioning on ability\"）。\n\n---\n\n### 综合评价\n\nR2 的审稿整体严谨，大部分 weakness 与我的独立评估一致。最重要的共识集中在三个方面：\n1. **ρ≈0.997 vs. \"instability\" 的 framing 张力**（R2-W1 ≈ R1-W5）\n2. **因果归因空白限制 actionability**（R2-W2 ≈ R1-W3）\n3. **注入模型 ecological validity 不足**（R2-W5 ≈ R1-W1）\n\n我与 R2 的主要分歧在于方法新颖性（R2-W3）和重复呈现（R2-W6）的 severity 等级。前者不应过度惩罚严谨的跨领域应用工作，后者更多是 style issue 而非 substance issue。\n\nR2 的 W4（\\enlargethispage 格式操作）是一个我在 Round 1 中遗漏的有价值发现——这确实需要作者在 camera-ready 时修正，但不应影响学术评价。\n",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 Round 1 审稿意见的逐条回应\n\n---\n\n### Strengths 回应\n\n**[AGREE] R2-S1 (Rigorous Experimental Design)**\n完全同意。多层对照设计是本文最大的方法论优势，与我在 R1-S2 中的评价一致。特别值得强调的是，六种替代解释的系统排除（Section 4.4, Table 2）和 ~28-29% 的 C% floor 在多种 matching 策略下的一致性，在 NLP 实证论文中确实罕见。\n\n**[AGREE] R2-S2 (Ground Truth Meta-Critique)**\n完全同意，与我的 R1-S3 一致。enrichment=0.964、Jaccard=0.206、φ=0.012 的正交性发现（Section 4.3）对整个 contamination detection 领域的验证范式有超越本文的影响。\n\n**[AGREE] R2-S3 (Cross-Benchmark Replication)**\n同意，与我的 R1-S4 一致。六个 benchmark 的复现（Table 3）增强了 generalizability，knowledge vs. procedural 的差异模式合理。\n\n**[AGREE] R2-S4 (Semi-Synthetic Framework)**\n同意，与我的 R1-S1 一致。cross-subject matching 的 Remark（Section 3.4）提供了干净的构造性论证。\n\n**[AGREE] R2-S5 (Conceptual Distinction)**\n同意。Figure 1 的 ICC 示意图有效地帮助读者区分 global vs. differential contamination 这两个容易混淆的概念。不过我在 Minor Issues 中指出 Figure 1 缺少 axis labels（θ vs. P(correct)），建议在 camera-ready 时补充。\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R2-W1 (Practical Significance Paradox: ρ ≈ 0.997)**\n基本同意，这与我的 R1-W5 高度重叠。ρ ≈ 0.997 确实削弱了 \"instability\" 叙事的紧迫性。R2 的三点建议都很好，特别是第三点——在 items 更少的 benchmark 上报告 ρ 值。TruthfulQA 只有 817 items（Table 3），如果其 C%=29.7%，去除 ~240 个 DIF items 后对排名的影响可能远大于 MMLU。论文没有提供这个数据是一个明显的遗漏。\n\n不过我想补充一个 nuance：R2 将此标为 [critical] 可能稍重。论文在 Section 4.5 中确实提到了 family-level rank shifts（Llama-3: +53, Mistral: -35），这些 shift 对 pairwise model selection 有实际意义。问题不在于发现本身无意义，而在于论文的 framing 重心放错了——应该从 \"benchmark reliability threat\" 转向 \"diagnostic tool for capability dimension shifts\"。这是 framing 问题，不是 substance 问题。\n\n**[AGREE] R2-W2 (因果归因空白使 audit protocol actionability 存疑)**\n完全同意，这与我的 R1-W3 高度一致。Section 5.3 的 \"rotate or retire\" 建议与 Section 4.5 中 DIF items 承载 z = -8σ to -49σ 的 discriminative signal 这一发现之间存在直接矛盾。R2 建议改为 \"investigate and report alongside stable-item rankings\" 更为合理。我在 R1-W3 中也提出了类似建议——论文需要更明确地讨论何时 DIF 是问题（measurement artifact）vs. 特征（genuine sensitivity to change）。\n\n**[REBUT] R2-W3 (方法新颖性有限)**\n部分不同意。R2 认为 \"MH-DIF 是 1988 年的标准方法，方法新颖性不足\"，这个批评本身成立但不应作为 EMNLP 论文的主要 weakness。理由如下：\n\n1. ARR reviewer guidelines 明确指出不应因方法不够 \"complex\" 而贬低论文——\"simpler methods that work should not be penalized\"（H14 pitfall）。\n2. 本文的贡献定位为 \"methodological and empirical, not algorithmic\"（Section 1 最后一段），这是合理的。\n3. Cross-subject matching 的 ΔFPR=0.000 保证（Section 3.4 Remark）虽然建立在 MH-DIF 之上，但作为针对 LLM benchmark 场景的方法改进具有独立价值。\n4. Ground truth meta-critique（Contribution 2）本身就是方法论层面的新颖洞察。\n\nEMNLP Findings track 明确接收 \"sound and reproducible\" 的实证贡献。即使对 Main track 来说，novelty 可以来自问题定义和实证发现，而非必须来自方法本身。不过我同意 R2 的建议——更突出 C2 作为主要贡献会加强论文。\n\n**[AGREE] R2-W4 (`\\enlargethispage{18\\baselineskip}` 格式操作过于激进)**\n同意这是一个需要关注的问题。18\\baselineskip 约等于额外 18 行（~8-9 cm），这不是标准的微调而是大幅度 margin manipulation。从 discussion.tex line 3 的证据来看，如果去除此命令，Discussion section 很可能导致正文溢出到第 9 页，违反 EMNLP long paper 的 8 页限制。\n\n不过我要指出：这个问题属于格式合规范畴，不应影响论文的学术评价。如果正文确实在 8 页内（含 Discussion），作者可能需要在 camera-ready 时压缩 Discussion，但这是可操作的修改——重复性内容（R2-W6 指出的问题）的删减可以腾出空间。我不建议将此标为影响接收决定的因素。\n\n**[AGREE] R2-W5 (半合成框架注入模型过于简化)**\n同意，与我的 R1-W1 一致。我特别赞同 R2 提出的区分——框架对 FPR 控制的贡献（ΔFPR=0.000 不依赖注入模型现实性，因为这是 matching variable 构造的性质）与 TPR 估计的贡献（受注入模型限制）应该明确区分。论文在 Limitations 中已部分提到这一点（\"the framework's primary methodological contribution—cross-subject matching achieving ΔFPR=0.000—is a matching strategy property independent of injection realism\"），但在正文 Section 3.4 和 Section 4.1 中没有足够强调这个重要区分。\n\n**[REBUT] R2-W6 (关键统计量的重复呈现)**\n部分不同意。学术论文中核心数字在 Abstract→Introduction→Results→Discussion→Conclusion 的重复是正常的写作惯例，因为读者可能只读特定 section。但我承认本文的重复程度偏高——例如 enrichment≈0.964 在正文中出现了至少 5 次，ΔFPR=0.000 也出现了类似次数。\n\n然而，我不认为这是一个 weakness——它更多是 writing style 的问题。Discussion 的功能本就是将 Results 重新整合到更大的 context 中，必然会引用相同数字。Conclusion 只有两行恰恰是因为论文选择不再重复。R2 将此标为 [warning] 等级偏高——建议降为 Minor Issue。\n\n---\n\n### Questions 回应\n\n**[AGREE] R2-Q1 (其他 benchmark 的 stable-item vs. full ranking ρ)**\n这是一个关键遗漏。论文只报告了 MMLU 的 ρ≈0.997，但没有报告 TruthfulQA (817 items)、ARC (1,172 items)、GSM8K (1,319 items) 等较小 benchmark 的 ρ。考虑到这些 benchmark 的 item 数量仅为 MMLU 的 1/10 到 1/15，DIF items 的移除对排名的影响可能显著更大。这直接关系到 W1 中 practical significance 的评估。与我的 R1-W5 中建议报告 pairwise comparison flip rate 相呼应。\n\n**[AGREE] R2-Q2 (difficulty-direction interaction 跨 benchmark 一致性)**\n好问题。ρ=-0.597 仅在 MMLU 上报告（Section 4.2），如果这个模式在 GSM8K 或其他 benchmark 上也成立，将大大增强 \"hard items gain, easy items erode\" 这一发现的 generalizability。反之，如果不一致，可能暗示这是 MMLU 的特异性。\n\n**[AGREE] R2-Q3 (6 个月窗口 C%=34.35% 暗示 calendar year 划分可能低估)**\n有趣的观察。Section 4.7 提到 6 个月窗口（2023-H2 vs. 2024-H1）C%=34.35%，这确实高于全年 31.3%。可能的解释是 6 个月窗口内模型变化更集中，但论文没有深入分析。这暗示 temporal resolution 的选择影响 DIF 估计——如果更细粒度的时间划分产生更高的 C%，那么 31.3% 可能是一个保守估计。\n\n**[REBUT] R2-Q4 (500 模型阈值的依据)**\n这个问题可以从论文中部分回答。Section 4.1 的 power analysis 表明在 N≥80 per cohort 时 ETS-C 的 TPR 为 0.68-0.80（Appendix Table 4），论文的实际 cohort sizes（1,080 和 807）远超这个阈值。500 个新模型的建议（Section 5.3）虽然没有 formal justification，但考虑到 N≥80 的 power threshold，500 个新模型足以构成一个有统计效力的 focal group。不过我同意 R2 的暗示——这个阈值应该更明确地与 power analysis 结论挂钩。\n\n**[AGREE] R2-Q5 (单一 domain benchmark 上的跨学科匹配)**\n好问题，但论文已在 Section 3.2 中回答。论文定义了三种 matching 策略：(1) standard matching（within-benchmark total score），(2) cross-subject matching（排除当前 subject 的 total score），(3) external matching（使用不同 benchmark 的 total score）。对于 GSM8K 这样的单一 domain benchmark，使用策略 (3) external matching——例如用 MMLU total score 作为 matching variable。Appendix Table 6 中 GSM8K 的 ΔTPR 就是在 external matching 下报告的（$p=0.5$, external: +0.514）。不过论文确实没有在正文中对此做充分说明，应在 Section 3.2 或 Section 4.7 中明确 GSM8K 使用了 external matching。\n\n---\n\n### Missing References 回应\n\n**R2-Ref1 (Polo et al. 2024, IRT-based efficient evaluation)**\n[AGREE] 相关但非必须。论文 Related Work (Section 2) 已引用了 Polo et al. (2024) 关于 \"TinyBenchmarks\"（line numbers visible in related_work.tex），如果 R2 指的是另一篇 Polo et al. 工作则需要补充。\n\n**R2-Ref2 (Putnick & Bornstein 2016, Measurement invariance conventions)**\n[AGREE] 值得引用。Measurement invariance 的跨领域综述可以帮助 NLP 读者理解 DIF 在更广泛的 psychometric framework 中的位置。这与我在 R1 Missing References 中建议引用 Kolen & Brennan (2014) 的 equating 文献相呼应——论文整体上缺少经典 psychometric 综述文献。\n\n---\n\n### Minor Issues 回应\n\n**[AGREE] R2-M1 (Figure 2 缺少 confidence bands)**: 同意。5 random seeds 的变异应以 error bands 呈现。\n\n**[AGREE] R2-M2 (Table 1 \"--\" 列应注明原因)**: 同意。Within-family 和 Random split 行的 FPR/Enrichment 列为 \"--\"，应在 caption 或 footnote 中说明原因（可能是因为这些 cohort 没有对应的 web-overlap label 分析）。\n\n**[AGREE] R2-M3 (Figure 5 N=33 outlier 影响)**: 同意。N=33 且 r=-0.478 的相关性对 outlier 敏感。论文已标注为 exploratory，但应报告 robust correlation 或 leave-one-out 影响分析。与我的 R1-Q4 中关于 GSM1K 分析 exploratory nature 的关切一致。\n\n**[REBUT] R2-M4 (holland1988mh 出版年份)**: Holland & Thayer 的 MH-DIF 程序描述发表于 1988 年的 *ETS Research Report* 系列（RR-88-31），论文引用年份 1988 是正确的。R2 可能混淆了 Holland & Thayer (1988) 与 Mantel & Haenszel (1959) 的原始统计检验——后者确实更早，但论文引用的是 Holland & Thayer 对 DIF 检测的具体应用。\n\n**[AGREE] R2-M5 (Yen's Q3 未在正文定义)**: 同意。正文 Section 3.2 提到 \"permutation simulation... Q3 = 4.6-34.2%\" 但未解释 Q3 是什么。Appendix A.1 有详细描述，但正文首次提及时应至少加一句简要说明（如 \"Yen's Q3 statistic, which measures residual correlations between item pairs after conditioning on ability\"）。\n\n---\n\n### 综合评价\n\nR2 的审稿整体严谨，大部分 weakness 与我的独立评估一致。最重要的共识集中在三个方面：\n1. **ρ≈0.997 vs. \"instability\" 的 framing 张力**（R2-W1 ≈ R1-W5）\n2. **因果归因空白限制 actionability**（R2-W2 ≈ R1-W3）\n3. **注入模型 ecological validity 不足**（R2-W5 ≈ R1-W1）\n\n我与 R2 的主要分歧在于方法新颖性（R2-W3）和重复呈现（R2-W6）的 severity 等级。前者不应过度惩罚严谨的跨领域应用工作，后者更多是 style issue 而非 substance issue。\n\nR2 的 W4（\\enlargethispage 格式操作）是一个我在 Round 1 中遗漏的有价值发现——这确实需要作者在 camera-ready 时修正，但不应影响学术评价。\n",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-22T01:51:06.673396+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4317
}
```

</details>

---


### Assistant

_source line 418 · 2026-05-22T01:51:10.763135+00:00_

已提交对 Reviewer 2 的逐条回应。核心共识集中在 ρ≈0.997 vs. "instability" 的 framing 张力、因果归因空白、注入模型 ecological validity 三个方面。主要分歧在于方法新颖性（R2-W3）的 severity——我认为不应过度惩罚严谨的跨领域应用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 16

## Round 16

48 recorded events


### User

_source line 419 · 2026-05-22T03:26:12.115786+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。

## Venue 信息
- **目标**：EMNLP 2026（通过 ARR 统一审稿）
- **截止日期**：2026-05-25（ARR May cycle）
- **格式**：Long Paper，正文严格 8 页，参考文献不限，Limitations 不计入页数
- **模板**：ACL 2023 template（\usepackage[review]{acl}）
- **匿名规则**：Double-blind
- **Overall Assessment 评分**：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle

## 论文文件
- LaTeX 主文件：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`
- 各节在 `sections/` 子目录
- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/submitted.pdf`

## 论文概要
论文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM 基准评测（METABENCH，5,227 模型 × 12,508 MMLU 题目），发现 31.3% 的 MMLU 题目在 2023 vs 2024 模型之间存在 ETS Category C 级别的 temporal DIF。提出 cross-subject matching 实现 ΔFPR=0.000，semi-synthetic injection framework 验证检测能力，并揭示 web-overlap 污染标签与 DIF flags 近乎独立（enrichment≈0.96）。

## 你的审查侧重

请重点审查以下方面：

1. **MH-DIF 方法适用性**：
   - MH-DIF 从教育测量迁移到 LLM 评测的假设是否成立？特别是：(a) LLM examinee 非独立性（shared training data, fine-tune variants）对 MH χ² 的影响；(b) MMLU 57 subjects 的多维性 vs MH 单维假设；(c) quintile-based stratification 的 K=5 选择是否充分
   - cross-subject matching 的 ΔFPR=0.000 是否过度依赖特定 matching strategy？当污染跨多 domain 时 graceful degradation 是否充分论证？

2. **Semi-synthetic framework**：
   - binary response flipping 的生态效度（ecological validity）——real-world contamination 是否会产生类似信号？
   - ΔTPR 作为 upper-bound estimate 是否在文中充分标注？
   - 注入率 p 的选择范围（0.0-1.0）是否覆盖了实际场景？

3. **统计控制与 power analysis**：
   - Monte Carlo power analysis 使用 2PL 参数但 MMLU 被报告为 poor fit to 2PL——这个矛盾是否被充分讨论？
   - Bootstrap CI [29.4%, 38.1%] 的 rightward asymmetry 是否影响结论稳健性？
   - Permutation test（200 shuffles + per-subject 1000×8）的分辨率是否足够？
   - BH FDR correction 仅移除 3 items——这是否说明 ETS dual threshold 本身就足够保守？

4. **实验设计完整性**：
   - 5 个 cohort comparisons 的逻辑是否互相支撑？
   - within-subject C%=38.1% > temporal C%=31.3% 的解释是否充分？
   - matched-ability analysis 的 convergence（~28-29% floor）是否可靠？
   - 6 benchmark cross-validation 的设计是否合理？

5. **因果归因**：
   - 论文声称 DIF detects "that" not "why"——这一立场是否在全文一致维持？是否有 sections 滑向 causal language？
   - §5.3 audit protocol 的可操作性——如果 DIF 无法归因，"Act" 级别该做什么？

请按 Strengths / Weaknesses（Must-Fix / Should-Fix / Nice-to-Have）/ Questions / Missing References 的结构组织你的审稿意见，并给出 Overall Assessment（使用 ARR 评分标准）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-22T03:26:21.205646+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-22T03:26:22.762431+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1556
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-22T03:26:22.762804+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-22T03:26:22.813240+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-22T03:26:27.285950+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 425 · 2026-05-22T03:26:29.595487+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 426 · 2026-05-22T03:26:34.414964+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on my search results, I found information about ACL Rolling Review (ARR) reviewer guidelines and related policies for 2025-2026. Here are the key findings:

## Reviewer Guidelines and Requirements

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements. The ARR peer review guidelines are a work-in-progress and will be updated as ARR evolves, and reviewers should always check whether the version they are familiar with is still the current one before starting an assignment.

## Recent Policy Updates (May 2025 onwards)

Starting from May 2025, ACL introduces awards policy for reviewers & chairs. Starting in M
…[truncated 904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7129
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-22T03:26:35.824868+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 581.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 539.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.0}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 536.1}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6229
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-22T03:26:42.264764+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales. I need: 1) All scoring dimensions (soundness, excitement, etc.) with their scale descriptions. 2) The Overall Assessment scale. 3) Any specific instructions about what constitutes a good review. 4) Confidence scoring scale."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales. I need: 1) All scoring dimensions (soundness, excitement, etc.) with their scale descriptions. 2) The Overall Assessment scale. 3) Any specific instructions about what constitutes a good review. 4) Confidence scoring scale."
  }
}
```

</details>

---


### Tool call

_source line 429 · 2026-05-22T03:26:43.068836+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-22T03:26:43.420548+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-22T03:26:43.875243+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-22T03:26:43.875685+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-22T03:26:44.484463+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1063
}
```

</details>

---


### Tool result

_source line 434 · 2026-05-22T03:26:44.839372+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 963
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-22T03:26:47.778388+00:00_

# ARR Review Form Criteria Summary

Based on the guidelines provided, here's what I found regarding scoring dimensions:

## Scoring Dimensions

The document mentions **three scores** that reviewers provide starting February 2025:

1. **Soundness** - Assesses technical validity and methodology quality. Must be justified by review text; low scores require explicit explanation of faults.

2. **Excitement** - Reflects personal interest and subjective appreciation. Explicitly described as "orthogonal to the assessment of soundness" and doesn't require detailed justification.

3. **Overall Assessment** - A composite recommendation reflecting soundness, excitement, novelty, and potential impact for conference commitment.

## Scale Information

The document does not explicitly detail numerical rating scales for these dimensions. It emphasizes that "soundness scores must be justified by the text of the review" and notes that low excitement doesn't require detailed reasoning, but specific scale numbers aren't provided in this excerpt.

## Key Review Quality Instructions

Good reviews should be:
- **Specific** with concrete examples rather than vague criticisms
- **Professional and neutral** in tone, avoiding sarcasm or dismissiveness
- **Reflective of scores** - recommendations must align with stated justifications

## Confidence Scoring

The guidelines mention reviewers "will also be able to indicate your confidence score" but don't specify the actual scale in the provided content.

**Note:** For complete scoring scale details, consult the linked [ARR review form documentation](https://aclrollingreview.org/reviewform).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5513
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-22T03:26:53.808906+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their numerical scales, and descriptions for each score level. Especially: Soundness scale, Excitement scale, Overall Assessment scale, Confidence scale."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their numerical scales, and descriptions for each score level. Especially: Soundness scale, Excitement scale, Overall Assessment scale, Confidence scale."
  }
}
```

</details>

---


### Tool call

_source line 437 · 2026-05-22T03:26:56.669813+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-22T03:26:57.173549+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-22T03:26:57.476798+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-22T03:26:57.477264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-22T03:26:58.183668+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool result

_source line 442 · 2026-05-22T03:26:58.485973+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-22T03:26:59.189936+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence Scale
**Range: 1-5**
- 5: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- 4: "Quite sure. I tried to check the important points carefully."
- 3: "Pretty sure, but there's a chance I missed something."
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- 1: "Not my area, or paper is very hard to understand."

## Soundness Scale
**Range: 1-5 (with half-point options)**
- 5: "Excellent: This study is one of the most thorough I have seen."
- 4: "Strong: This study provides sufficient support for all of its claims."
- 3: "Acceptable: This study provides sufficient support for its main claims."
- 2: "Poor: Some of the main claims are not sufficiently supported."
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement Scale
**Range: 1-5 (with half-point options)**
- 5: "Highly Exciting: I would recommend this paper to others."
- 4: "Exciting: I would mention this paper to others."
- 3: "Interesting: I might mention some points of this paper to others."
- 2: "Potentially Interesting: this paper does not resonate with me."
- 1: "Not Exciting: this paper does not resonate with me."

## Overall Assessment Scale
**Range: 1-5 (with half-point options)**
- 5: Consider for Award (top 2.5% papers)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5381
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-22T03:27:08.545617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-22T03:27:09.404750+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-22T03:27:09.405281+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 447 · 2026-05-22T03:27:10.011504+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 448 · 2026-05-22T03:27:10.012840+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-22T03:27:11.321804+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1310
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-22T03:27:11.474534+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-22T03:27:12.280667+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-22T03:27:12.281124+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/submitted.pdf",
  "project": "irt_equated_bench_regen",
  "pages": "11-14",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/submitted.pdf",
    "project": "irt_equated_bench_regen",
    "pages": "11-14",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-22T03:27:12.887096+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 598.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 393.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 143.3}], \"total_pages\": 14, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-22T03:27:16.822253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 455 · 2026-05-22T03:27:17.295898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-22T03:27:17.823043+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 457 · 2026-05-22T03:27:18.480145+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 458 · 2026-05-22T03:27:18.582332+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1760
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-22T03:27:18.635258+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 155
}
```

</details>

---


### Tool result

_source line 460 · 2026-05-22T03:27:19.089454+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1793
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-22T03:27:19.192278+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1369
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-22T03:32:43.676905+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 将教育测量 MH-DIF 方法大规模应用于 LLM benchmark 审计，cross-subject matching 是真正的方法贡献，但 LLM examinee 非独立性对统计推断的影响未被充分解决，semi-synthetic validation 的检测力估计为上界但主文未明确标注。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 核心方法论（MH χ²）的独立性假设在 5,227 模型中被严重违反，permutation test 和 bootstrap CI 均受影响；Monte Carlo power analysis 使用 2PL 参数但 MMLU 被报告为 poor fit to 2PL，存在内在矛盾；不过多路径 converging evidence 部分弥补了单一方法的缺陷 |\n| Excitement | 3.5 / 5 | 将教育测量的 DIF 方法引入 NLP 评测领域是新颖且有实践价值的；ground truth meta-critique（contamination labels ≈ 独立于 DIF flags）是重要的概念性贡献；审计协议有可操作性但 \"Act\" 层缺乏具体指引 |\n| Confidence | 4 / 5 | 熟悉 DIF 方法论和 LLM evaluation 文献，仔细阅读了正文 + 附录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] LLM examinee 非独立性对 MH χ² 和 permutation test 的影响未充分解决\n- 具体位置：§3.2（方法假设）、§4.1-4.2（统计检验）、Limitations（p.8-9）\n- 问题：MH χ² 假设 examinee 独立。5,227 个模型中包含大量 fine-tune variants（如数百个 Llama-2 衍生模型），它们共享大部分参数和训练数据，违反独立性假设。这导致：\n  (a) MH χ² 的显著性检验 inflate——有效样本量远小于 N=5,227，实际的 p-value 可能远大于报告值；\n  (b) Permutation test（200 cohort-level shuffles）在个体模型层面 shuffle，但如果模型以 family 为单位聚集，shuffling non-independent units 无法正确估计 null distribution——需要 cluster-robust permutation（在 family 层面 permute）；\n  (c) Bootstrap CI [29.4%, 38.1%] 同样假设 independent sampling，在 clustered 数据下会 underestimate variance。\n- 论文的缓解措施（family de-duplication K=20,25,121）是有信息量的，但不充分：即使 de-duplicate 到每个 family 一个模型，不同 family 之间仍可能因共享训练数据而非独立（例如许多模型基于 Llama base fine-tune）。\n- 为什么影响接收：这是统计推断的基础假设。如果 31.3% 这个数字的置信区间因 clustering 而大幅扩大，核心结论的精度将受到质疑。\n- 建议修改方向：(1) 报告模型 family 数量及 family size 分布；(2) 做 cluster-robust permutation test（以 family 为单位 permute）并对比结果；(3) 使用 cluster bootstrap 重新估计 CI；(4) 如果上述分析显示结论不变，这反而大幅加强论文——但如果显著改变 C%，则需修改核心 claims。\n\n**N2** [critical] Semi-synthetic validation 的 ΔTPR 应在主文中明确标注为 upper-bound estimate\n- 具体位置：§3.4（方法描述）、§4.5（结果报告）、Abstract\n- 问题：Binary response flipping 是最极端的 uniform DIF 注入——以概率 p 将所有 focal group 的目标 item 从错改对。Real-world contamination 产生的信号可能：(a) 远弱于此（partial memorization），(b) 跨 ability levels 不均匀（non-uniform DIF），(c) 与 item difficulty 相关。因此 ΔTPR = +0.508（at p=0.5）是检测力的乐观上界。\n- 主文 §3.4 和 §4.5 没有显式标注\"upper bound\"——这一关键限定仅隐晦出现在 Limitations section（\"detection power under such realistic patterns is untested\"）。Abstract 直接引用 ΔTPR = +0.508 且无任何限定词。\n- 为什么影响接收：读者可能将此检测力数字误解为对 real contamination 的实际检测能力。\n- 建议修改方向：(1) 在 §3.4 和 §4.5 首次报告 ΔTPR 时加入 \"upper-bound\" 或 \"ceiling estimate\" 限定；(2) Abstract 中加一句\"under a worst-case uniform injection\"；(3) 讨论 partial memorization 可能产生的 non-uniform DIF 信号及 MH 对此的盲区。\n\n**N3** [critical] Monte Carlo power analysis 与 2PL poor fit 之间的矛盾\n- 具体位置：§4.1、Appendix A.2（Table 4）\n- 问题：§4.1 使用 2PL 参数生成模拟数据估计 MH-DIF 的检测力（TPR 0.40-0.95）。Appendix A.2 承认\"MMLU response matrix shows poor fit to a unidimensional 2PL model\"。论文用 triangulation 论证（Monte Carlo + semi-synthetic injection 相互验证），但这两条证据线并非独立——如果 2PL 拟合差，Monte Carlo 的 TPR 估计可能系统性偏高或偏低。\n- 论文辩护说\"MH validity 不依赖 IRT assumptions\"——这是对的，但 Monte Carlo power analysis 的有效性确实依赖模拟数据的真实性。\n- 为什么影响接收：Power analysis 是论文论证\"MH-DIF 有足够检测力\"的关键一环。如果模拟数据与真实数据差异大，power estimates 不可靠。\n- 建议修改方向：(1) 明确标注 Monte Carlo power analysis 是在 parametric assumptions 下的 approximate estimate；(2) 对比 2PL-based simulation 和 non-parametric bootstrap-based simulation 的 power estimates；(3) 或者直接以 semi-synthetic injection 为主要 power evidence，将 Monte Carlo 降级为补充分析。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Abstract 中 ΔFPR=0.000 缺乏 multi-subject contamination 限定\n- 具体位置：Abstract（第4行）\n- 问题：Abstract 写 \"achieves zero false positive inflation (ΔFPR = 0.000)\"，但这仅在 single-subject contamination 条件下成立。§4.5 和 Table 5 报告 multi-subject injection（k≤5）时 ΔFPR 上升至 0.0026-0.069。Abstract 应注明这一限定条件。\n- 建议：改为 \"achieves zero false positive inflation under single-subject contamination (ΔFPR = 0.000), with graceful degradation to ΔFPR ≤ 0.069 under multi-domain contamination\"。\n\n**W2** [warning] K=5 quintile stratification 的敏感性分析缺失\n- 具体位置：§3.2\n- 问题：论文引用 ETS recommended practice 使用 K=5。但 ETS practice 基于教育测试的典型样本量（N~数千人），而本文 N=5,227 完全支持更细粒度的 K=10 或 K=20。更细的分层可以减少 matching bias，也可能揭示 non-uniform DIF patterns。论文未报告 K 的敏感性分析。\n- 建议：增加 K∈{5, 10, 20} 的敏感性分析，至少报告 C% 对 K 的变化趋势。\n\n**W3** [warning] Within-subject C%=38.1% > temporal C%=31.3% 的解释不充分\n- 具体位置：§4.4、Table 2\n- 问题：Within-subject DIF 比 temporal DIF 高出约 7 个百分点。论文解释为\"within-subject DIF 在单个 subject 内部更敏感\"，但未充分讨论这意味着什么：(a) 是否说明 temporal C%=31.3% 是 underestimate？(b) 是否表明 subject 间的多维性在标准 matching 中起了 cancellation 作用？(c) 如果 within-subject 更准确，为什么不以其为主要报告？\n- 建议：增加一段专门讨论 within-subject vs. cross-subject C% 差异的含义及其对主要结论的影响。\n\n**W4** [warning] §4.3 中统计显著性与实际显著性的混淆\n- 具体位置：§4.3、Abstract\n- 问题：Enrichment=0.96, Jaccard=0.06, p=0.012。p=0.012 表明 DIF flags 与 web-overlap labels 在统计上 NOT independent，但 effect size 极小（Jaccard 仅 0.06）。论文将此称为 \"near-independent\"——在实际意义上准确，但未讨论大样本量（9,229 items）如何 inflate statistical significance。读者可能困惑于\"p=0.012 但 near-independent\"这一看似矛盾的表述。\n- 建议：明确区分 statistical significance 和 practical significance，说明 enrichment ≈ 1.0 在大样本下的 trivially small deviation 也会达到 p<0.05。\n\n**W5** [warning] §5.3 审计协议的 \"Act\" 层缺乏可操作指引\n- 具体位置：§5.3\n- 问题：三级协议中 \"Act (C% ≥ 25%)\" 建议 \"investigate flagged items and report stable-item rankings\"。但既然 DIF 无法归因（论文反复强调 \"that\" not \"why\"），\"investigate\" 的具体步骤是什么？benchmark maintainer 看到 flagged items 后应该做什么？是直接移除？还是做 follow-up study？\n- 建议：给出 1-2 个具体的 investigation 流程示例（如：对 flagged items 做 item content review、cross-reference with known contamination sources、report alongside stable-item rankings as sensitivity analysis）。\n\n**W6** [warning] 低注入率（p < 0.3）的检测力未报告\n- 具体位置：§3.4、Figure 2\n- 问题：Semi-synthetic injection 的 p 范围为 {0.0, 0.3, 0.5, 0.7, 1.0}，但实际的 benchmark contamination 可能对应更低的 exploitation rate（如 p=0.05-0.2）。Figure 2 显示 TPR 在 p=0.3 时已低于 0.5——这意味着在更现实的低注入场景下检测力可能很弱。论文未报告 p<0.3 的 performance。\n- 建议：补充 p ∈ {0.05, 0.1, 0.2} 的 ΔTPR 数据，或在讨论中明确说明方法在低 exploitation rate 下的局限。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.2 引用 \"ETS recommended practice for large-scale assessments (Donoghue and Allen, 1993; Clauser and Mazor, 1998)\" 但这些参考是关于 DIF 一般方法论的，不是关于 K=5 stratification 的具体 recommendation——请确认 K=5 的出处。\n- Figure 2 的 y 轴标签 \"True Positive Rate (TPR)\" 和 \"False Positive Rate (FPR)\" 较密集，建议使用 subplot 标题而非 y 轴标签以改善可读性。\n- Table 3 中 τ (Kendall) 的加入是好的，但部分 benchmarks 的 N（模型数）差异较大，应注意 τ 的 standard error 随 N 变化。\n- Limitations section 提到 \"partial memorialization\" 但未定义——建议简要说明其含义（模型不完全记忆答案，只是提高概率）。\n\n---\n\n## Questions to Authors\n\n**Q1**: 5,227 个模型中有多少个 distinct model families？Family size 的分布如何（median, max）？如果以 family 为单位做 cluster-robust permutation test，C% 和 p-value 如何变化？\n\n**Q2**: Random split baseline（C%=0.18%）是在模型层面随机分还是 family 层面？如果 family 内的模型被分到不同 groups，family 内相似性可能 inflate baseline FPR。\n\n**Q3**: Table 4 的 Monte Carlo power analysis 使用了什么具体的 2PL 参数分布？是直接从 MMLU 数据估计的 2PL 参数吗？如果 2PL fit 差，这些估计的参数可能本身就不可靠。\n\n**Q4**: Cross-subject matching 中使用\"total score on a different benchmark (MMLU total score on GSM8K items)\"作为 matching variable——但 MMLU 和 GSM8K 测量的 construct 不同（知识 vs. 数学推理），这是否引入 construct-irrelevant matching bias？\n\n**Q5**: GSM1K cross-validation（Figure 5）仅有 N=33 个模型，r=-0.478 的 95% CI 是多少？这么小的 N 下相关系数的 instability 较大。\n\n**Q6**: 论文是否考虑过使用 Lord's χ² 或 Raju's area measure 等 IRT-based DIF 方法作为 robustness check？尽管 MH 是 non-parametric 的优势明确，但 IRT-based 方法能检测 non-uniform DIF。\n\n---\n\n## 主要优势\n\n1. **新颖且有价值的跨领域方法迁移**：将教育测量中成熟的 MH-DIF 方法引入 LLM benchmark 评测，既有方法论贡献（cross-subject matching），也有实证贡献（31.3% temporal DIF）。\n2. **实验设计的多路径 converging evidence**：5 种 cohort designs + 3 种 structural controls + 6 benchmark cross-validation，从不同角度支撑核心发现，设计缜密。\n3. **Ground truth meta-critique 是概念层面的重要贡献**：证明 web-overlap contamination labels 与 DIF flags 近乎正交（enrichment ≈ 0.96），挑战了现有 contamination detection 文献中将 \"exposure = contamination\" 等同的隐含假设。\n4. **规模和数据基础扎实**：基于 METABENCH 的 5,227×12,508 响应矩阵，是目前最大规模的 benchmark-level DIF 分析。\n5. **\"that\" not \"why\" 的认识论定位贯穿全文**：论文对因果归因保持了良好的克制，没有将 DIF detection 过度解读为 contamination detection。\n6. **Cross-subject matching 的形式化论证**（Remark on Zero FPR）清晰且可验证——虽然仅限 single-subject 情形，但理论推导本身是 solid 的。",
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 将教育测量 MH-DIF 方法大规模应用于 LLM benchmark 审计，cross-subject matching 是真正的方法贡献，但 LLM examinee 非独立性对统计推断的影响未被充分解决，semi-synthetic validation 的检测力估计为上界但主文未明确标注。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 核心方法论（MH χ²）的独立性假设在 5,227 模型中被严重违反，permutation test 和 bootstrap CI 均受影响；Monte Carlo power analysis 使用 2PL 参数但 MMLU 被报告为 poor fit to 2PL，存在内在矛盾；不过多路径 converging evidence 部分弥补了单一方法的缺陷 |\n| Excitement | 3.5 / 5 | 将教育测量的 DIF 方法引入 NLP 评测领域是新颖且有实践价值的；ground truth meta-critique（contamination labels ≈ 独立于 DIF flags）是重要的概念性贡献；审计协议有可操作性但 \"Act\" 层缺乏具体指引 |\n| Confidence | 4 / 5 | 熟悉 DIF 方法论和 LLM evaluation 文献，仔细阅读了正文 + 附录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] LLM examinee 非独立性对 MH χ² 和 permutation test 的影响未充分解决\n- 具体位置：§3.2（方法假设）、§4.1-4.2（统计检验）、Limitations（p.8-9）\n- 问题：MH χ² 假设 examinee 独立。5,227 个模型中包含大量 fine-tune variants（如数百个 Llama-2 衍生模型），它们共享大部分参数和训练数据，违反独立性假设。这导致：\n  (a) MH χ² 的显著性检验 inflate——有效样本量远小于 N=5,227，实际的 p-value 可能远大于报告值；\n  (b) Permutation test（200 cohort-level shuffles）在个体模型层面 shuffle，但如果模型以 family 为单位聚集，shuffling non-independent units 无法正确估计 null distribution——需要 cluster-robust permutation（在 family 层面 permute）；\n  (c) Bootstrap CI [29.4%, 38.1%] 同样假设 independent sampling，在 clustered 数据下会 underestimate variance。\n- 论文的缓解措施（family de-duplication K=20,25,121）是有信息量的，但不充分：即使 de-duplicate 到每个 family 一个模型，不同 family 之间仍可能因共享训练数据而非独立（例如许多模型基于 Llama base fine-tune）。\n- 为什么影响接收：这是统计推断的基础假设。如果 31.3% 这个数字的置信区间因 clustering 而大幅扩大，核心结论的精度将受到质疑。\n- 建议修改方向：(1) 报告模型 family 数量及 family size 分布；(2) 做 cluster-robust permutation test（以 family 为单位 permute）并对比结果；(3) 使用 cluster bootstrap 重新估计 CI；(4) 如果上述分析显示结论不变，这反而大幅加强论文——但如果显著改变 C%，则需修改核心 claims。\n\n**N2** [critical] Semi-synthetic validation 的 ΔTPR 应在主文中明确标注为 upper-bound estimate\n- 具体位置：§3.4（方法描述）、§4.5（结果报告）、Abstract\n- 问题：Binary response flipping 是最极端的 uniform DIF 注入——以概率 p 将所有 focal group 的目标 item 从错改对。Real-world contamination 产生的信号可能：(a) 远弱于此（partial memorization），(b) 跨 ability levels 不均匀（non-uniform DIF），(c) 与 item difficulty 相关。因此 ΔTPR = +0.508（at p=0.5）是检测力的乐观上界。\n- 主文 §3.4 和 §4.5 没有显式标注\"upper bound\"——这一关键限定仅隐晦出现在 Limitations section（\"detection power under such realistic patterns is untested\"）。Abstract 直接引用 ΔTPR = +0.508 且无任何限定词。\n- 为什么影响接收：读者可能将此检测力数字误解为对 real contamination 的实际检测能力。\n- 建议修改方向：(1) 在 §3.4 和 §4.5 首次报告 ΔTPR 时加入 \"upper-bound\" 或 \"ceiling estimate\" 限定；(2) Abstract 中加一句\"under a worst-case uniform injection\"；(3) 讨论 partial memorization 可能产生的 non-uniform DIF 信号及 MH 对此的盲区。\n\n**N3** [critical] Monte Carlo power analysis 与 2PL poor fit 之间的矛盾\n- 具体位置：§4.1、Appendix A.2（Table 4）\n- 问题：§4.1 使用 2PL 参数生成模拟数据估计 MH-DIF 的检测力（TPR 0.40-0.95）。Appendix A.2 承认\"MMLU response matrix shows poor fit to a unidimensional 2PL model\"。论文用 triangulation 论证（Monte Carlo + semi-synthetic injection 相互验证），但这两条证据线并非独立——如果 2PL 拟合差，Monte Carlo 的 TPR 估计可能系统性偏高或偏低。\n- 论文辩护说\"MH validity 不依赖 IRT assumptions\"——这是对的，但 Monte Carlo power analysis 的有效性确实依赖模拟数据的真实性。\n- 为什么影响接收：Power analysis 是论文论证\"MH-DIF 有足够检测力\"的关键一环。如果模拟数据与真实数据差异大，power estimates 不可靠。\n- 建议修改方向：(1) 明确标注 Monte Carlo power analysis 是在 parametric assumptions 下的 approximate estimate；(2) 对比 2PL-based simulation 和 non-parametric bootstrap-based simulation 的 power estimates；(3) 或者直接以 semi-synthetic injection 为主要 power evidence，将 Monte Carlo 降级为补充分析。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Abstract 中 ΔFPR=0.000 缺乏 multi-subject contamination 限定\n- 具体位置：Abstract（第4行）\n- 问题：Abstract 写 \"achieves zero false positive inflation (ΔFPR = 0.000)\"，但这仅在 single-subject contamination 条件下成立。§4.5 和 Table 5 报告 multi-subject injection（k≤5）时 ΔFPR 上升至 0.0026-0.069。Abstract 应注明这一限定条件。\n- 建议：改为 \"achieves zero false positive inflation under single-subject contamination (ΔFPR = 0.000), with graceful degradation to ΔFPR ≤ 0.069 under multi-domain contamination\"。\n\n**W2** [warning] K=5 quintile stratification 的敏感性分析缺失\n- 具体位置：§3.2\n- 问题：论文引用 ETS recommended practice 使用 K=5。但 ETS practice 基于教育测试的典型样本量（N~数千人），而本文 N=5,227 完全支持更细粒度的 K=10 或 K=20。更细的分层可以减少 matching bias，也可能揭示 non-uniform DIF patterns。论文未报告 K 的敏感性分析。\n- 建议：增加 K∈{5, 10, 20} 的敏感性分析，至少报告 C% 对 K 的变化趋势。\n\n**W3** [warning] Within-subject C%=38.1% > temporal C%=31.3% 的解释不充分\n- 具体位置：§4.4、Table 2\n- 问题：Within-subject DIF 比 temporal DIF 高出约 7 个百分点。论文解释为\"within-subject DIF 在单个 subject 内部更敏感\"，但未充分讨论这意味着什么：(a) 是否说明 temporal C%=31.3% 是 underestimate？(b) 是否表明 subject 间的多维性在标准 matching 中起了 cancellation 作用？(c) 如果 within-subject 更准确，为什么不以其为主要报告？\n- 建议：增加一段专门讨论 within-subject vs. cross-subject C% 差异的含义及其对主要结论的影响。\n\n**W4** [warning] §4.3 中统计显著性与实际显著性的混淆\n- 具体位置：§4.3、Abstract\n- 问题：Enrichment=0.96, Jaccard=0.06, p=0.012。p=0.012 表明 DIF flags 与 web-overlap labels 在统计上 NOT independent，但 effect size 极小（Jaccard 仅 0.06）。论文将此称为 \"near-independent\"——在实际意义上准确，但未讨论大样本量（9,229 items）如何 inflate statistical significance。读者可能困惑于\"p=0.012 但 near-independent\"这一看似矛盾的表述。\n- 建议：明确区分 statistical significance 和 practical significance，说明 enrichment ≈ 1.0 在大样本下的 trivially small deviation 也会达到 p<0.05。\n\n**W5** [warning] §5.3 审计协议的 \"Act\" 层缺乏可操作指引\n- 具体位置：§5.3\n- 问题：三级协议中 \"Act (C% ≥ 25%)\" 建议 \"investigate flagged items and report stable-item rankings\"。但既然 DIF 无法归因（论文反复强调 \"that\" not \"why\"），\"investigate\" 的具体步骤是什么？benchmark maintainer 看到 flagged items 后应该做什么？是直接移除？还是做 follow-up study？\n- 建议：给出 1-2 个具体的 investigation 流程示例（如：对 flagged items 做 item content review、cross-reference with known contamination sources、report alongside stable-item rankings as sensitivity analysis）。\n\n**W6** [warning] 低注入率（p < 0.3）的检测力未报告\n- 具体位置：§3.4、Figure 2\n- 问题：Semi-synthetic injection 的 p 范围为 {0.0, 0.3, 0.5, 0.7, 1.0}，但实际的 benchmark contamination 可能对应更低的 exploitation rate（如 p=0.05-0.2）。Figure 2 显示 TPR 在 p=0.3 时已低于 0.5——这意味着在更现实的低注入场景下检测力可能很弱。论文未报告 p<0.3 的 performance。\n- 建议：补充 p ∈ {0.05, 0.1, 0.2} 的 ΔTPR 数据，或在讨论中明确说明方法在低 exploitation rate 下的局限。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.2 引用 \"ETS recommended practice for large-scale assessments (Donoghue and Allen, 1993; Clauser and Mazor, 1998)\" 但这些参考是关于 DIF 一般方法论的，不是关于 K=5 stratification 的具体 recommendation——请确认 K=5 的出处。\n- Figure 2 的 y 轴标签 \"True Positive Rate (TPR)\" 和 \"False Positive Rate (FPR)\" 较密集，建议使用 subplot 标题而非 y 轴标签以改善可读性。\n- Table 3 中 τ (Kendall) 的加入是好的，但部分 benchmarks 的 N（模型数）差异较大，应注意 τ 的 standard error 随 N 变化。\n- Limitations section 提到 \"partial memorialization\" 但未定义——建议简要说明其含义（模型不完全记忆答案，只是提高概率）。\n\n---\n\n## Questions to Authors\n\n**Q1**: 5,227 个模型中有多少个 distinct model families？Family size 的分布如何（median, max）？如果以 family 为单位做 cluster-robust permutation test，C% 和 p-value 如何变化？\n\n**Q2**: Random split baseline（C%=0.18%）是在模型层面随机分还是 family 层面？如果 family 内的模型被分到不同 groups，family 内相似性可能 inflate baseline FPR。\n\n**Q3**: Table 4 的 Monte Carlo power analysis 使用了什么具体的 2PL 参数分布？是直接从 MMLU 数据估计的 2PL 参数吗？如果 2PL fit 差，这些估计的参数可能本身就不可靠。\n\n**Q4**: Cross-subject matching 中使用\"total score on a different benchmark (MMLU total score on GSM8K items)\"作为 matching variable——但 MMLU 和 GSM8K 测量的 construct 不同（知识 vs. 数学推理），这是否引入 construct-irrelevant matching bias？\n\n**Q5**: GSM1K cross-validation（Figure 5）仅有 N=33 个模型，r=-0.478 的 95% CI 是多少？这么小的 N 下相关系数的 instability 较大。\n\n**Q6**: 论文是否考虑过使用 Lord's χ² 或 Raju's area measure 等 IRT-based DIF 方法作为 robustness check？尽管 MH 是 non-parametric 的优势明确，但 IRT-based 方法能检测 non-uniform DIF。\n\n---\n\n## 主要优势\n\n1. **新颖且有价值的跨领域方法迁移**：将教育测量中成熟的 MH-DIF 方法引入 LLM benchmark 评测，既有方法论贡献（cross-subject matching），也有实证贡献（31.3% temporal DIF）。\n2. **实验设计的多路径 converging evidence**：5 种 cohort designs + 3 种 structural controls + 6 benchmark cross-validation，从不同角度支撑核心发现，设计缜密。\n3. **Ground truth meta-critique 是概念层面的重要贡献**：证明 web-overlap contamination labels 与 DIF flags 近乎正交（enrichment ≈ 0.96），挑战了现有 contamination detection 文献中将 \"exposure = contamination\" 等同的隐含假设。\n4. **规模和数据基础扎实**：基于 METABENCH 的 5,227×12,508 响应矩阵，是目前最大规模的 benchmark-level DIF 分析。\n5. **\"that\" not \"why\" 的认识论定位贯穿全文**：论文对因果归因保持了良好的克制，没有将 DIF detection 过度解读为 contamination detection。\n6. **Cross-subject matching 的形式化论证**（Remark on Zero FPR）清晰且可验证——虽然仅限 single-subject 情形，但理论推导本身是 solid 的。",
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-22T03:32:47.743670+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4066
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-22T03:32:52.216759+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-22T03:32:52.217199+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 466 · 2026-05-22T03:33:01.697591+00:00_

审稿意见已提交给 Review Director。

总结：Overall 3.5（Borderline Conference）。三个 Must-Fix：(1) LLM 模型非独立性对 MH χ² 和 permutation test 的根本性影响未解决——需要 cluster-robust 方法；(2) semi-synthetic ΔTPR 是 upper-bound 但主文未标注；(3) Monte Carlo power analysis 用了 poor-fit 的 2PL 参数。六个 Should-Fix 涵盖 ΔFPR=0.000 的限定条件缺失、K=5 敏感性、within-subject 与 temporal C% 差异解释、统计/实际显著性混淆、audit protocol 可操作性、低注入率检测力。论文的核心优势在于跨领域方法迁移的新颖性、多路径实验设计、以及 ground truth meta-critique 的概念贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1"
}
```

</details>

---


## Round 17

## Round 17

4 recorded events


### User

_source line 467 · 2026-05-22T03:35:43.526431+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）

### Overall: 3.5 — Borderline Conference

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法执行严谨，控制实验充分，但归因缺口和排名保持与 instability 主张的张力构成实质性关切 |
| Excitement | 3/5 | 发现有趣但方法论新颖性有限——"现有方法应用到新领域"框架限制兴奋度；ρ≈0.997 使实际影响论证乏力 |
| Reproducibility | 4/5 | 匿名代码仓库，METABENCH 数据公开，方法描述清晰 |

### Must-Fix

**N1** [critical] ρ≈0.997 与 "31% instability" 之间的叙事张力未充分解决
- 核心主张是 31.3% DIF，但排名高度保持（ρ≈0.997, τ≈0.958, flip rate ≤2.8%）。"diagnostic, not destructive" 定位合理但论文未令人信服论证 practitioners 为何应关心不影响排名的 instability。
- §5.1 三层分解停留概念层面，缺乏"忽略 DIF 导致什么具体错误"的实证示例。§4.6 的 Llama-3 +53 / Mistral -35 位说明的是 DIF items 包含家族特异性信号，非忽略 DIF 导致错误决策。
- 建议：(a) 提供 1-2 个具体案例展示 DIF 在排名保持下仍导致错误结论；(b) 或调整叙事从 "instability" 转向 "measurement heterogeneity reveals hidden capability structure"。

**N2** [critical] 归因缺口严重限制审计协议可操作性
- §5.3 "Act" 时 "investigate flagged items"——investigate for what？DIF 只检测 THAT 不解释 WHY。benchmark maintainer 标记 31% items 后该做什么？
- 15%/25% 阈值声称 "adapt ETS practice" 但无证据直接迁移到 LLM 场景。
- 建议：(a) 阈值选择的实证依据（模拟 C% 多高时 ρ 显著下降）；(b) 每个 action level 具体可执行步骤。

### Should-Fix

**W1** Cross-subject matching 新颖性声明需更谨慎。DIF 文献中 external/subtest matching 已有成熟实践（Nandakumar 1993, purified matching）。Remark 是 matching 设计的直接推论（by construction），非需要证明的理论贡献。建议重新定位为 "设计选择及其性质"。

**W2** \enlargethispage{6\baselineskip} 格式操纵过于激进。建议压缩冗余内容（如 §4.2 permutation 细节可移入附录）。

**W3** 与 Growing Pains (Habba et al. 2026) 对比不完整。"empirical comparison awaits public release" 留下显著空白。论文可基于已发表报告做更深入概念对比（FPC 假设 anchor items 稳定 vs 本文发现 31% 不稳定）。

**W4** Semi-synthetic injection 现实性存疑。binary flipping 是最极端模式，real-world contamination 更复杂。建议附录补充至少一种更现实注入模式（ability-dependent exploitation rate）。

**W5** 缺少对 polytomous DIF 方法的讨论。LLM 评测正向 open-ended generation 迁移，Related Work 应简要覆盖 polytomous DIF 文献。

### 小问题
- M1: "z = −8σ to −49σ" 记号不标准
- M2: Table 1 vs §3.4 中 "FPR" 概念不一致
- M3: Bootstrap CI [29.4%, 38.1%] 右偏来源解释不清
- M4: Figure 2 上下面板格式不完全一致
- M5: Table 1 中 Llama-2 vs Llama-3 的 FPR/Enrichment 为 "--"，未注释原因
- M6: Double-blind 匿名维持良好 ✓

### 缺失参考文献
- Hardy et al. (2026) scalability coefficients 待验证可获取性
- 建议补充 Swaminathan & Rogers (1990) purified subtest matching

### 叙事一致性评估
- 标题 "Temporal Measurement Instability" 准确但在 ρ≈0.997 上下文中 "measurement heterogeneity" 可能更精确
- "diagnostic, not destructive" 定位不完全一致——§4.2 section title "31% Measurement Instability" 偏 alarmist
- 三层框架在 §5.1 引入但 Experiments 部分未系统使用

### 主要优势
1. 分析规模和系统性（5,227×12,508，6 基准）
2. Ground truth meta-critique 概念贡献突出
3. 诚实的局限性讨论
4. 跨基准复制增强可信度（17.9-31.3%, 45-174× above baseline）
5. 写作整体清晰

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---
