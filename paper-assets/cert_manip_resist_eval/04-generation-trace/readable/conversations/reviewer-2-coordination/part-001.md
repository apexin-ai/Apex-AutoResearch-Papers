# Reviewer 2 coordination — Part 1 of 2

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Conversation logs

[Transcript overview](../reviewer-2-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/b4/b4b7cc0933581491d1b1.json)

## Round 1

## Round 1

62 recorded events


### User

_source line 1 · 2026-05-22T22:50:49.500448+00:00_

[Round 1 审稿请求]:
## Step 1: Independent Review — R2 (Novelty & Related Work)

You are R2 in a two-reviewer roundtable for EMNLP 2026 (ARR). Your focus: **novelty, positioning, related work, and presentation quality**.

### Target Venue Calibration
EMNLP 2026 ARR Overall Assessment (1–5, half-point scale):
- 5 = Consider for Award (top 2.5%)
- 4 = Conference (main venue accept)
- 3 = Findings (acceptable)
- 2 = Resubmit next cycle
- 1 = Do not resubmit
Accept rate: ~21% for Main. Score dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5).

### Paper Summary
"Weakest Link, Not Diversity: Adversarial Vulnerability in Multi-Judge LLM Evaluation"

The paper decomposes multi-judge LLM panel vulnerability into two structural predictors: individual judge weakness (η_max) and panel diversity (K_eff). Across 15 models, 6 families, 455 panels, 9 attack types, 3 benchmarks, it finds η_max robustly dominates (5:1 over K_eff under bootstrap). K_eff collapses from 8/12 (OLS) to 0/12 (clustered SE). GAM reveals targeted/shared-bias taxonomy (10:8). Aggregation rules modulate vulnerability (Bayesian reverses K_eff direction). Two-stage robustness-first algorithm wins 12/12 conditions.

### Paper Structure (8 pages main text + 1 page references)
- Abstract + Intro (pp.1-2): 5 contributions listed
- Related Work (p.2): ~15 lines covering LLM-as-Judge, adversarial attacks on LLM judges, BFT — extremely brief
- Method (pp.2-3): Panel construction, vulnerability predictors (η_max, K_eff), 9 attack types (listed but not described in detail), log-log OLS regression, 5 aggregation rules
- Experiments (pp.3-7): 11 subsections (core results, attack expansion, RF contrast, ASR concentration, aggregation gradient, panel design, capability-matched, diversity-capability tradeoff, panel size sensitivity, generation extension, partial-knowledge adversary)
- Discussion (p.7): 3 paragraphs
- Conclusion + Limitations (p.8)
- References: Only 7 entries

### Your Review Tasks

**A. Novelty Assessment**
1. Is the research question ("which structural factor drives panel vulnerability — individual weakness or diversity?") novel and important for the NLP community?
2. The paper claims "first large-scale empirical study" — evaluate this claim against existing literature. Consider: (a) multi-judge evaluation robustness studies, (b) adversarial attacks on LLM-as-judge, (c) BFT-inspired analysis of ML systems.
3. Are the 5 claimed contributions genuinely novel, or are some expected/incremental? Specifically:
   - C1 (η_max dominance): Is it surprising that the weakest judge determines panel vulnerability?
   - C2 (BFT reversal): Novel framing via RF contrast
   - C3 (GAM taxonomy): targeted vs shared-bias split
   - C4 (aggregation as control lever): Bayesian calibration reversing K_eff
   - C5 (robustness-first algorithm): practical design tool
4. Evaluate the conceptual contribution vs. empirical contribution balance.

**B. Related Work Critique**
1. Only 7 references total in the paper. For EMNLP, this is extremely thin. Missing areas likely include:
   - Multi-agent systems robustness (consensus protocols beyond classical BFT)
   - Ensemble methods in ML (diversity vs. individual strength tradeoff is well-studied in ensemble learning — Kuncheva, Krogh & Vedelsby, etc.)
   - LLM-as-judge specific papers (Li et al. 2023 "AlpacaEval", Dubois et al. 2024 "Length-controlled AlpacaEval", Ye et al. 2024 "Flask", etc.)
   - Adversarial robustness of ensembles (transferability, ensemble adversarial training)
   - Raina et al. 2024 [7] is cited but its relationship to this work not discussed in depth
   - Panel/committee methods in crowdsourcing literature (Dawid-Skene, etc.)
2. The Related Work section is ~15 lines — far below EMNLP standards. It doesn't position the work within the broader ensemble learning literature where the diversity-vs-individual-strength tradeoff is classical.

**C. Presentation Quality**
1. Writing quality: Is the paper clearly written? Are claims well-supported by evidence?
2. The paper has NO figures — only 10 tables. For an 8-page empirical paper, this is unusual. The experiment plan calls for many figures (scatter plots, heatmaps, forest plots, etc.). Evaluate impact on readability.
3. 11 experiment subsections in 4 pages — is this too compressed? Could some be moved to supplementary?
4. The abstract is dense and quantitative — is this effective for the target venue?
5. Limitations section: 3 points, one short paragraph — adequate per EMNLP requirements?

**D. Framing and Positioning Concerns**
1. The BFT analogy: Is it well-grounded? BFT assumes Byzantine (arbitrary, worst-case) faults — the paper's "adaptive adversary" is different from Byzantine faults. Is the paper conflating BFT with something simpler?
2. The title "Weakest Link, Not Diversity" is provocative — does the evidence fully support this strong claim? The paper itself shows K_eff matters under Bayesian aggregation and within-tier analysis.
3. Is there a risk of the paper being seen as a "negative result" (diversity doesn't help)? How well does the paper frame its positive contributions?
4. The practical recommendation (robustness-first + Bayesian) — is this genuinely actionable? How many practitioners actually build multi-judge panels?

**E. Scores**
Provide preliminary scores: Soundness (1-5), Excitement (1-5), Reproducibility (1-5), Overall Assessment (1-5, half-point).

Format your review with clear sections for Strengths, Weaknesses, Questions for Authors, and Scores. Be calibrated to EMNLP 2026 standards (~21% accept rate for Main).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-22T22:50:58.989825+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-22T22:50:58.990427+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/review_reviewer_2_38d341a1.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-22T22:51:00.495976+00:00_

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
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
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

_source line 5 · 2026-05-22T22:51:00.546586+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-22T22:51:06.430131+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-22T22:51:06.681343+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/theorem1_proof.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/figures/fig1_robustness_comparison.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/plan001_step1_full_v4/chart/fig1_robustness_comparison.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/figures/fig2_gam_keff_split.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/plan001_step1_full_v4/chart/fig2_gam_keff_split.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/figures/fig1_robustness_comparison.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/figures/fig2_gam_keff_split.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/figures/fig3_aggregation_gradient.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/plan001_step1_full_v4/char
…[truncated 1067 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-22T22:51:06.681829+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions scoring"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-22T22:51:13.866965+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria dimensions scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Review Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Score Interpretation

The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.

## Overall Recommendation Levels

5 = Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). 2 = Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle.
…[truncated 568 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7185
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-22T22:51:23.306117+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract all scoring dimensions, their scales, and descriptions. Include: soundness, excitement, overall assessment, reproducibility, and any other dimensions. List the exact scale labels for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract all scoring dimensions, their scales, and descriptions. Include: soundness, excitement, overall assessment, reproducibility, and any other dimensions. List the exact scale labels for each dimension."
  }
}
```

</details>

---


### Tool call

_source line 11 · 2026-05-22T22:51:24.159946+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.pdf",
  "project": "cert_manip_resist_eval",
  "pages": "1-5",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.pdf",
    "project": "cert_manip_resist_eval",
    "pages": "1-5",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 12 · 2026-05-22T22:51:29.384590+00:00_

# ACL Rolling Review Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5 = "Positive that my evaluation is correct"
- 4 = Quite sure with unlikely missed details
- 3 = Pretty sure but possible oversights
- 2 = Can defend evaluation but likely missed some details
- 1 = "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- 5 = Excellent, "one of the most thorough I have seen"
- 4 = Strong, sufficient support with minor gaps acceptable
- 3 = Acceptable, main claims supported with minor needs
- 2 = Poor, major claims unsupported or methodological issues
- 1 = "Major Issues: not yet sufficiently thorough"

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- 5 = Highly exciting, recommend to others
- 4 = Exciting, would mention to others
- 3 = Interesting, might mention selectively
- 2 = Potentially interesting but limited personal resonance
- 1 = "Not Exciting: does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- 5 = Consider for Award (top 2.5%)
- 4 = Conference acceptance
- 3 = Findings acceptance
- 2 = Resubmit next cycle
- 1 = Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- 5 = "easily reproduce the results"
- 4 = Mostly reproducible with minor variation
- 3 = Reproducible with difficulty
- 2 = Hard to reproduce, unavailable data/details
- 1 = "would not be able to reproduce the results"

## 6. **Datasets**
Scale: 1-5
- 5 = Enabling impact on research choices
- 4 = Useful for ongoing work
- 3 = Potentially useful
- 2 = Documentary value
- 1 = No usable datasets

## 7. **Software**
Scale: 1-5
- 5 = Enabling impact
- 4 = Useful for ongoing work
- 3 = Potentially useful
- 2 = Documentary value
- 1 = No usable software

## 8. **Author Identity Knowledge**
Scale: 1-5
- 5 = Double-blind violation
- 4 = Known via preprint/workshop
- 3 = Identifiable from submission content
- 2 = Known from informal communication
- 1 = No educated guess po
…[truncated 6 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6078
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-22T22:51:30.137277+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 546.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 555.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.2}], \"total_pages\": 13, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5977
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-22T22:51:34.854809+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 15 · 2026-05-22T22:51:35.207768+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-22T22:51:35.860257+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-22T22:51:36.216319+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-22T22:51:36.216746+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-22T22:51:36.879446+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1671
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-22T22:51:36.879939+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-22T22:51:37.236877+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1376
}
```

</details>

---


### Tool result

_source line 22 · 2026-05-22T22:51:37.689234+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1472
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-22T22:51:37.942498+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1062
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-22T22:51:44.166911+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.pdf",
  "project": "cert_manip_resist_eval",
  "pages": "6-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.pdf",
    "project": "cert_manip_resist_eval",
    "pages": "6-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-22T22:51:44.769222+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 446.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.9}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.0}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 469.6}], \"total_pages\": 13, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-22T22:51:47.535537+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 27 · 2026-05-22T22:51:48.037824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 28 · 2026-05-22T22:51:48.942469+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-22T22:51:48.943533+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-22T22:51:48.943956+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 31 · 2026-05-22T22:51:49.445562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 32 · 2026-05-22T22:51:49.699528+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-22T22:51:49.699993+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 34 · 2026-05-22T22:51:50.256825+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 811
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-22T22:51:50.661099+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 961
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-22T22:51:57.133970+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.pdf",
  "project": "cert_manip_resist_eval",
  "pages": "11-13",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.pdf",
    "project": "cert_manip_resist_eval",
    "pages": "11-13",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-22T22:51:57.435858+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.4}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 275.2}], \"total_pages\": 13, \"rendered_pages\": 3, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-22T22:52:02.203804+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-22T22:52:02.705822+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 40 · 2026-05-22T22:52:03.108455+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 41 · 2026-05-22T22:52:03.209408+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 42 · 2026-05-22T22:52:03.363623+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 657
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-22T22:52:03.665719+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-22T22:55:03.687069+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AlpacaEval LLM judge evaluation Dubois 2024 length-controlled"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AlpacaEval LLM judge evaluation Dubois 2024 length-controlled"
  }
}
```

</details>

---


### Tool call

_source line 45 · 2026-05-22T22:55:03.988744+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dawid-Skene crowdsourcing model aggregation multiple annotators"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dawid-Skene crowdsourcing model aggregation multiple annotators"
  }
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-22T22:55:04.191928+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FLASK fine-grained language model evaluation Ye 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FLASK fine-grained language model evaluation Ye 2024"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-22T22:55:10.318908+00:00_

Web search results for query: "Dawid-Skene crowdsourcing model aggregation multiple annotators"

Links: [{"title":"Classification-oriented dawid skene model for transferring intelligence from crowds to machines | Request PDF","url":"https://www.researchgate.net/publication/366619843_Classification-oriented_dawid_skene_model_for_transferring_intelligence_from_crowds_to_machines"},{"title":"Reaching a Consensus in crowdsourced data using the Dawid-Skene Model – Michael P. J. Camilleri","url":"https://michaelpjcamilleri.wordpress.com/2020/06/22/reaching-a-consensus-in-crowdsourced-data-using-the-dawid-skene-model/"},{"title":"(PDF) The Extended Dawid-Skene Model: Fusing Information from Multiple Data Schemas","url":"https://www.researchgate.net/publication/340239337_The_Extended_Dawid-Skene_Model_Fusing_Information_from_Multiple_Data_Schemas"},{"title":"The graphical model of the General Dawid-Skene model. Note that P (i)... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/The-graphical-model-of-the-General-Dawid-Skene-model-Note-that-P-i-is-the-confusion_fig1_268452153"},{"title":"[PDF] Fast Dawid-Skene: A Fast Vote Aggregation Scheme for Sentiment Classification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Fast-Dawid-Skene:-A-Fast-Vote-Aggregation-Scheme-Sinha-Rao/118d4c1bfaa2f3a50e7237d641fa2e433877d1aa"},{"title":"Crowdsourcing via Pairwise Co-occurrences: Identifiability and   Algorithms","url":"https://arxiv.org/pdf/1909.12325"},{"title":"Understanding Crowdsourcing Algorithms for Multi-Annotator Data | PGW’s notes","url":"https://pengwei715.github.io/2025/07/01/crowdsoucing.html"},{"title":"Fast Dawid-Skene: A Fast Vote Aggregation Scheme for Sentiment Classification","url":"https://arxiv.org/pdf/1803.02781"}]

Based on the search results, here's what I found about the Dawid-Skene crowdsourcing model:

## Overview

The Dawid-Skene model is a classical model for aggregating labels from multiple annotators and assessing
…[truncated 1138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6330
}
```

</details>

---


### Tool result

_source line 48 · 2026-05-22T22:55:11.674692+00:00_

Web search results for query: "AlpacaEval LLM judge evaluation Dubois 2024 length-controlled"

Links: [{"title":"AlpacaEval: LLM Evaluation Benchmark","url":"https://www.emergentmind.com/topics/alpacaeval"},{"title":"An Empirical Study of LLM-as-a-Judge: How Design Choices Impact Evaluation Reliability","url":"https://arxiv.org/html/2506.13639v1"},{"title":"[PDF] Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Length-Controlled-AlpacaEval:-A-Simple-Way-to-Dubois-Galambosi/eb375712bd37250c350ecd3f559e1879e87eb3e5"},{"title":"AlpacaEval 2.0: Scalable LLM Evaluation","url":"https://www.emergentmind.com/topics/alpacaeval-2-0"},{"title":"[2404.04475] Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators","url":"https://arxiv.org/abs/2404.04475"},{"title":"Published as a conference paper at COLM 2024 Length-Controlled AlpacaEval:","url":"https://openreview.net/pdf/76a4afefba676b543f4c4ca61529f92e828e171f.pdf"},{"title":"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators","url":"https://arxiv.org/html/2404.04475v1"},{"title":"Length-Controlled AlpacaEval - A Simple Way to Debias Automatic Evaluators","url":"https://hyunyoung2.github.io/2024/07/20/alpacaEval2/"},{"title":"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic   Evaluators","url":"https://arxiv.org/pdf/2404.04475"}]

Based on the search results, I found relevant information about AlpacaEval and the length-controlled evaluation work by Dubois et al. 2024:

## AlpacaEval and Length-Controlled Evaluation

Length-Controlled AlpacaEval was published as a conference paper at COLM 2024 by Yann Dubois, Percy Liang, and Tatsunori B. Hashimoto from Stanford University.

### The Problem Being Addressed

A critical refinement is the length-controlled win rate (LC-WR), introduced to address the observed "length bias"—the tendency of auto-annotators to favor longer responses regardl
…[truncated 946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7987
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-22T22:55:12.678543+00:00_

Web search results for query: "FLASK fine-grained language model evaluation Ye 2024"

Links: [{"title":"FLASK: FINE-GRAINED LANGUAGE MODEL EVALUATION BASED ON ALIGNMENT SKILL SETS - Korea Advanced Institute of Science and Technology","url":"https://pure.kaist.ac.kr/en/publications/flask-fine-grained-language-model-evaluation-based-on-alignment-s/"},{"title":"Published as a conference paper at ICLR 2024 FLASK: FINE-GRAINED LANGUAGE MODEL","url":"https://arxiv.org/pdf/2307.10928"},{"title":"FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets | OpenReview","url":"https://openreview.net/forum?id=CYmF38ysDa"},{"title":"[2307.10928] FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets","url":"https://arxiv.org/abs/2307.10928"},{"title":"GitHub - kaistAI/FLASK: [ICLR 2024 Spotlight] FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets","url":"https://github.com/kaistAI/FLASK"},{"title":"[PDF] FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FLASK:-Fine-grained-Language-Model-Evaluation-based-Ye-Kim/25abd08fb52f9131f1f57f1e0a3ddc38648daddc"},{"title":"(PDF) FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets","url":"https://www.researchgate.net/publication/372488100_FLASK_Fine-grained_Language_Model_Evaluation_based_on_Alignment_Skill_Sets"},{"title":"Measuring LLMs' Adherence to Task Evaluation Instructions","url":"https://advait.org/files/murugadoss_2025_llm_evaluation.pdf"}]

I found comprehensive information about FLASK. Here's what the search revealed:

## FLASK: Fine-grained Language Model Evaluation

FLASK is a fine-grained language skill set evaluation setting for the alignment of language models. The paper was presented at the 12th International Conference on Learning Representations (ICLR 2024) in Vienna, Austria in May 2024.

### Key Contribution

Evaluation of LLMs is challenging
…[truncated 1212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8486
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-22T22:55:18.402279+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ambiguity decomposition\" \"bias-variance\" ensemble diversity individual accuracy tradeoff machine learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ambiguity decomposition\" \"bias-variance\" ensemble diversity individual accuracy tradeoff machine learning"
  }
}
```

</details>

---


### Tool call

_source line 51 · 2026-05-22T22:55:18.603273+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "adversarial transferability ensemble defense diversity \"ensemble adversarial\" 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "adversarial transferability ensemble defense diversity \"ensemble adversarial\" 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 52 · 2026-05-22T22:55:25.477869+00:00_

Web search results for query: ""ambiguity decomposition" "bias-variance" ensemble diversity individual accuracy tradeoff machine learning"

Links: [{"title":"Journal of Machine Learning Research 24 (2023) 1-49","url":"https://arxiv.org/pdf/2301.03962"},{"title":"Generalized Ambiguity Decomposition for Understanding ...","url":"https://arxiv.org/pdf/1312.7463"},{"title":"A unified theory of diversity in ensemble learning | The Journal of Machine Learning Research","url":"https://dl.acm.org/doi/10.5555/3648699.3649058"},{"title":"Estimating ensemble weights for bagging regressors based on the mean–variance portfolio framework - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417423009648"},{"title":"A hybrid ensemble method with negative correlation learning for regression | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10994-023-06364-3"},{"title":"Bias–variance tradeoff - Wikipedia","url":"https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff"},{"title":"Ensemble Learning through Diversity Management: Theory,","url":"http://staff.ustc.edu.cn/~hchen/tutorial/IJCNN2011.pdf"},{"title":"Self-Error Adjustment: Theory and Practice of Balancing Individual Performance and Diversity in Ensemble Learning","url":"https://arxiv.org/pdf/2508.04948"},{"title":"Optimising Diversity in Classifier Ensembles | SN Computer Science","url":"https://link.springer.com/article/10.1007/s42979-022-01063-7"}]

I found comprehensive information on this topic. Here's what the search reveals about ambiguity decomposition, bias-variance-diversity tradeoffs, and ensemble learning:

## Key Theoretical Framework

Exact bias-variance-diversity decompositions have been proven for a wide range of losses in both regression and classification, including squared, cross-entropy, and Poisson losses.

## The Tradeoff Between Individual Accuracy and Diversity

Ambiguity decomposition explains the tradeoff between individual a
…[truncated 1260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7075
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-22T22:55:26.130380+00:00_

Web search results for query: "adversarial transferability ensemble defense diversity "ensemble adversarial" 2024 2025"

Links: [{"title":"Boosting the Transferability of Ensemble Adversarial Attack via Stochastic Average Variance Descent - Zhao - 2024 - IET Information Security - Wiley Online Library","url":"https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/2024/7983842"},{"title":"[2403.16405] Ensemble Adversarial Defense via Integration of Multiple Dispersed Low Curvature Models","url":"https://arxiv.org/abs/2403.16405"},{"title":"[2410.06851] Understanding Model Ensemble in Transferable Adversarial Attack","url":"https://arxiv.org/abs/2410.06851"},{"title":"Understanding Model Ensemble in Transferable Adversarial Attack","url":"https://arxiv.org/html/2410.06851v1"},{"title":"EADOD: Ensemble adversarial defense via orthogonal distillation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950705125020805"},{"title":"rethinking model ensemble in transfer-based adversarial ...","url":"https://arxiv.org/pdf/2303.09105"}]

I've found several relevant research papers on adversarial transferability, ensemble defense, and diversity. Here are the key findings:

## Recent Research on Ensemble Adversarial Defense and Transferability

**Ensemble Defense Approaches:**

Ensemble-based defenses leverage model diversity to reduce adversarial transferability, with recent methods like EADOD (Ensemble Adversarial Defense via Orthogonal Distillation) enhancing robustness of pre-trained models through knowledge distillation with orthogonal subspace projections.

Another approach aims to enhance ensemble diversity by reducing attack transferability by identifying second-order gradients (depicting loss curvature) as a key factor in adversarial robustness.

**Ensemble Adversarial Attacks:**

Model ensemble adversarial attack has become a powerful method for generating transferable adversarial examples that can target even unknown models. Recent theore
…[truncated 914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7527
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-22T22:57:06.640491+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines: what should reviewers focus on, what are the reviewing standards, any guidance on novelty assessment, related work expectations, writing quality. Summarize the key points."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer guidelines: what should reviewers focus on, what are the reviewing standards, any guidance on novelty assessment, related work expectations, writing quality. Summarize the key points."
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-22T22:57:14.225472+00:00_

# ARR Reviewer Guidelines: Key Standards

## Core Reviewing Focus

Reviewers should concentrate on four primary tasks:

1. **Calendar allocation** for both reviewing and discussion phases
2. **Assignment verification** (expertise, conflicts of interest, potential desk rejections)
3. **Strong review writing** with specific, justified feedback
4. **Post-response assessment** incorporating author clarifications

## Standards for Evaluation

**Reading Strategy:** Reviewers must read papers twice—first for understanding the research question and contribution scope, then for technical soundness. This prevents bias from initial impressions.

**Specificity Requirement:** Comments must be concrete. Rather than stating "missing relevant references," identify which specific works should be cited.

**Tone Expectations:** Reviews should maintain professionalism and neutrality. The guidelines emphasize that "a good review should be professional and neutral, if not kind," noting that harsh language damages reviewer-author relationships and the field broadly.

## Novelty & Related Work Standards

The guidelines caution against common biases regarding novelty:

- "Results are not novel" requires concrete prior work citations (published 3+ months before submission)
- Negative results, simple solutions, and papers outside one's methodology preferences deserve fair evaluation
- Novel work is inherently harder to evaluate; reviewers should avoid unnecessary conservatism

Authors must acknowledge prior work appropriately, but missing references to very recent preprints (under 3 months old) are not grounds for rejection.

## Common Pitfalls to Avoid

Problematic review patterns include dismissing work for being "too simple," lacking SOTA results, or using non-preferred methodologies. The document provides seventeen specific heuristics reviewers should check themselves against before finalizing reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7584
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-22T23:00:06.527179+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# R2 独立审稿报告：Novelty, Related Work, Presentation Quality\n\n**论文**: \"The Weakest Judge Wins: What Really Drives LLM Evaluation Panel Vulnerability Under Adversarial Attack\"\n**Target Venue**: EMNLP 2026 (via ARR)\n**审稿依据**: ACL Rolling Review official review form (https://aclrollingreview.org/reviewform) + reviewer guidelines (https://aclrollingreview.org/reviewerguidelines)\n\n---\n\n## 总体评分\n\n**Overall Assessment: 3.0 / 5 (Findings)**\n**一句话总结**: 实验规模大、统计方法扎实，但核心发现（weakest link dominates）在安全与集成学习文献中可预期；Related Work 过于单薄、BFT 类比存在概念错位，novelty 不足以支撑主会议接收。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 实验设计全面（455 panels, 15 models, 多种 correction），但 η_max 与 K_eff 的 r=0.70 confound 没有被充分解决（见 N2）；Theorem 1 条件过强，实际适用性可疑（见 W3） |\n| Excitement | 2.5 / 5 | 核心发现（weakest link dominates under adaptive attack）可从安全第一性原理直接推导；更有趣的发现（aggregation modulation, random-vs-adaptive contrast）被降格为次要贡献；benchmark 仅覆盖 multiple-choice QA |\n| Reproducibility | 4 / 5 | 模型名称、量化方式、攻击 prompt（Appendix E/Table 5）、panel 构造规则均有详细说明；承诺发布代码和数据；GAM 和 bootstrap 的部分超参数未明确 |\n| Overall | 3.0 / 5 | Findings 水平——实验工作扎实但 novelty 不够 Main Conference |\n\n---\n\n## 主要优势\n\n**S1. 实验规模与系统性值得肯定。** 15 个模型、6 个 family、455 panels、6 种攻击类型、2 个 benchmark 的组合设计在 multi-judge evaluation 文献中确属少见。Clustered SE / mixed effects / wild cluster bootstrap 三种 non-independence correction 方法并用（Section 5.2, Table 3），方法论意识强。\n\n**S2. Random-vs-Adaptive 对比（Section 5.3）是真正有洞察力的贡献。** 展示了 diversity 在 random fault 下有效、在 adaptive attack 下失效的机制切换，这比单纯报告 \"η_max dominates\" 更有信息量。R² 从 0.73 (random) 降至 0.81 (adaptive) 的对比（Section 5.3, 第二段）直接揭示了 adversary information advantage 如何改变 panel 的 failure mode。\n\n**S3. Aggregation-as-control-lever 发现（Section 5.5, Table 4）具有实践价值。** Bayesian calibration 逆转 K_eff 方向（从正变负）、threshold voting 放大 η_max（Table 4）的发现为 panel 设计提供了可操作的 knob。这是论文中最接近 actionable contribution 的部分。\n\n**S4. Attack-type taxonomy via GAM（Section 5.4, Figure 2）提供了有用的分类框架。** Targeted attacks（prompt injection, score manipulation, position bias）与 shared-bias attacks（sycophancy, verbosity bias, authority bias）的 clean 6:6 split 有实证价值。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **Related Work 严重不足，无法建立本文在文献中的 positioning**\n- 具体位置：Section 2 (Related Work), p.2，整个 section 仅约半页（~30行）\n- 问题：虽然 bibliography 有 ~33 条引用，Related Work section 对每个领域只给了 1-3 句 surface-level 描述，没有 engage with 关键前人工作的细节。具体缺失：\n  - **(a) 集成学习中 diversity-vs-accuracy tradeoff 的经典理论**：Krogh & Vedelsby (1995) 的 ambiguity decomposition、Brown et al. (2005) 的 bias-variance-covariance decomposition 被 cited 但未被 discussed。这些工作已经形式化地证明了 diversity 和 individual accuracy 之间存在 fundamental tradeoff。本文的核心发现（individual strength > diversity under adversarial conditions）需要明确对照这些经典结果来讨论：到底是扩展了、推翻了、还是在不同条件下验证了这些理论？当前 Related Work 仅用一句 \"Kuncheva and Whitaker (2003) found that no single diversity metric reliably predicts ensemble improvement\"（Section 2, Ensemble Diversity Theory），远不足以建立对话。\n  - **(b) 缺少众包/标注聚合文献**：Dawid-Skene model (1979) 及其后续是 multi-annotator aggregation 的基础性工作，与本文的 multi-judge aggregation 直接相关。该模型通过 confusion matrix 估计每个 annotator 的可靠性，其核心思想（individual annotator quality matters more than annotator count）与本文 C1 发现高度一致。完全不讨论这一文献是重大遗漏。\n  - **(c) 缺少主流 LLM-as-judge framework**：AlpacaEval (Li et al. 2023), Length-Controlled AlpacaEval (Dubois et al. 2024, COLM 2024), FLASK (Ye et al. 2024, ICLR 2024 Spotlight) 是当前 LLM evaluation 中最广泛使用的框架，它们对 judge bias（尤其是 length bias, position bias）的处理方式与本文的攻击类型直接相关。特别是 Dubois et al. 对 length bias 的 debiasing 方法与本文的 Bayesian calibration 在思路上有共通之处。\n  - **(d) 对抗迁移性与集成防御的最新进展**：2024-2025 年有大量关于 ensemble adversarial defense 的工作（如 ensemble adversarial defense via orthogonal distillation, understanding model ensemble in transferable adversarial attack 等），这些工作直接研究了 diversity 在对抗环境下的防御效果。本文仅引用了 Tramèr et al. (2018) 和 Kariyappa & Qureshi (2019)，远不足以反映当前研究状态。\n- 为什么影响接收：ARR reviewer guidelines 明确要求 missing references 必须是具体的（\"identify which specific works should be cited\"），但同时也指出 \"Authors must acknowledge prior work appropriately\"。本文的 Related Work 长度和深度远低于 EMNLP 标准论文（通常 1-1.5 页），使得 reviewer 和读者无法判断本文的 incremental contribution 到底有多大。\n- 建议修改方向：将 Related Work 扩展至至少 1 页，对每个子领域（ensemble diversity theory, crowdsourcing aggregation, LLM-as-judge frameworks, adversarial ensemble robustness）用 3-5 句讨论核心发现并明确本文的区分点。\n\n**N2** [critical] **核心发现（C1: η_max dominance）的 novelty 不足以支撑 main contribution 的定位**\n- 具体位置：Section 1 Introduction (Contribution 1), Section 5.1, 以及 Title\n- 问题：本文将 \"weakest link dominates panel vulnerability\" 定位为首要贡献，但这一发现可以从多个已知原则直接推导：\n  - **(a) 安全学**：Schneier (2000)——本文自己引用——的核心论点就是 \"security is only as strong as its weakest link\"。在 adaptive adversary 下，攻击者有信息优势，必然集中攻击最弱环节。\n  - **(b) 集成学习**：Kuncheva & Whitaker (2003) 和 Brown et al. (2005) 的理论框架已经表明，当 ensemble members 高度相关（本文 r=0.70）时，diversity 的边际收益趋近于零。\n  - **(c) BFT 本身**：BFT 的 f < n/3 容错界限本质上就是说 panel robustness 受限于最差成员的数量。\n  - ARR reviewer guidelines 指出，\"results are not novel\" 的判断需要引用具体的 prior work。上述三个方向虽然不是在完全相同的 setup 下得出相同结论，但它们共同使得核心发现成为一个 \"confirmatory result rather than a discovery\"。在 LLM-as-judge 这一具体场景下进行验证有价值，但定位为 \"首要贡献\" 和论文标题的核心 claim 是过度抬高了。\n- 为什么影响接收：EMNLP main conference 要求 Excitement ≥ 4，对应 \"exciting, would mention to others\"。一个可从第一性原理预期的结果难以达到这一门槛。\n- 建议修改方向：将论文的叙事重心从 \"weakest link dominates\"（confirmatory）转向 \"random-vs-adaptive mechanism switch\"（C2）和 \"aggregation as structural defense\"（C4），这两个发现更 novel 且更 actionable。标题可以调整为反映这种 nuance，例如突出 aggregation choice 改变 diversity 的作用方向这一更有力的发现。\n\n**N3** [critical] **BFT 类比存在概念错位，可能误导读者**\n- 具体位置：Section 1 Introduction（BFT analogy，第二段）, Section 2 Related Work (BFT and Security Games), Section 3 (Theorem 1), Section 5.3, Section 6 Analysis (BFT Reversal Mechanism)\n- 问题：BFT 与本文的 threat model 存在根本性差异：\n  - **BFT**: Byzantine 节点是系统**内部**的参与者，可以任意行为（包括策略性说谎、与其他恶意节点协调）。BFT 协议假设恶意节点是 system-level 的 corruption。\n  - **本文**: 对手是系统**外部**的，通过构造 adversarial inputs 来欺骗 judges。judges 本身不是恶意的——它们只是被特定 inputs 所欺骗。这更接近 adversarial examples / evasion attacks 而非 Byzantine faults。\n  - 关键区别：BFT 中 faulty nodes 可以发送不一致的消息给不同接收者（equivocation），本文中 judges 对同一 input 独立评判。BFT 的 f < n/3 bound 来源于 equivocation 的可能性，但本文的 adversary 不能让同一 judge 对不同 \"接收者\" 给出不同答案。\n  - Theorem 1 (Weakest-Link Monotonicity) 要求替换 judge 在**所有** attacks 和**所有** configurations 下都 stochastically 更弱，这是极强的条件。实际中 judges 有异质的脆弱性 profile（对 prompt injection 弱但对 position bias 强），此条件可能很少成立。\n  - 论文在 Section 5.3 展示 \"BFT reversal\" 时，实际讨论的是 random-vs-adaptive fault 的区别，这与 BFT 的 arbitrary-fault 模型也不完全对应。\n- 为什么影响接收：使用 BFT 框架创造了形式化和理论深度的期望，但 Theorem 1 是一个近乎 trivial 的 monotonicity 结果（替换更弱的 judge 使 panel 更弱），与 BFT 的核心定理（容错阈值、共识协议的正确性保证）不在同一层次。这种概念错位可能让 reviewer 和读者感到 \"framework 重于实质\"。\n- 建议修改方向：(1) 明确承认 BFT 是一个 \"loose analogy\" 而非 formal mapping，在 Introduction 中讨论两者的差异。(2) 考虑用 \"adversarial evasion\" 或 \"input manipulation\" 框架替代 BFT，因为后者更准确地描述了 threat model。(3) Theorem 1 可以保留但应降低其在叙事中的权重——它是一个 supporting result，不是 foundational contribution。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **r = 0.70 confound 削弱了 η_max vs K_eff 因果归因的可信度**\n- 具体位置：Section 6 Analysis (Diversity-Capability Confound, p.8), Appendix C.2\n- 问题：η_max 与 K_eff 的 Pearson r = 0.70 意味着约 49% 的方差共享。在 OLS 回归中，这种程度的多重共线性会导致系数估计不稳定、标准误膨胀。论文用了 clustered SE、mixed effects 和 bootstrap 来处理 non-independence，但这些方法解决的是**观测间相关性**问题，不是**预测变量间多重共线性**问题。K_eff 在 correction 后 \"collapse\" 到 0-1/12 significant conditions，部分原因可能是多重共线性导致 K_eff 系数的 variance inflation，而非 K_eff 真的无效。\n- 论文在 Appendix C.2 承认 \"the high confound with fragile independent significance means that observational regression cannot reliably disentangle diversity's causal contribution from the capability deficit that co-occurs with it\"。但这个 caveat 在正文中被大幅淡化，Title 和 Abstract 仍然做出了 \"Not Diversity\" 的 strong claim。\n- 建议：(1) 在正文 Discussion 中显著讨论 multicollinearity（如报告 VIF）。(2) 考虑使用 partial correlation 或 mediation analysis 来更 cleanly 分离两个预测变量的贡献。(3) 软化 \"Not Diversity\" 的 framing——改为 \"diversity's contribution is fragile and dominated by individual robustness\"。\n\n**W2** [warning] **Benchmark 范围窄，泛化性存疑**\n- 具体位置：Section 4.2 (Benchmarks and Attack Types, p.4)\n- 问题：MMLU 和 ARC 均为 multiple-choice QA，攻击类型也针对此格式设计（如 position bias 交换选项位置、score manipulation 在候选文本中嵌入评分指令）。但当前 LLM-as-judge 最广泛的应用场景是**开放式评价**（chatbot evaluation, creative writing, code generation），其中 judge bias 的表现形式和攻击面都不同。例如 AlpacaEval 中的 length bias 在 multiple-choice 场景下根本无法复现。论文没有讨论泛化性限制。\n- 建议：在 Limitations 中明确讨论 benchmark format 的限制，或增加至少一个 open-ended evaluation 场景的实验。\n\n**W3** [warning] **Theorem 1 的 stochastic dominance 条件过强，实际相关性不清晰**\n- 具体位置：Section 3 (Theorem 1, Definition 1, p.3), Appendix A (Proof, p.9)\n- 问题：Theorem 1 要求替换 judge J'_K 在所有 attacks a 和所有 realizations x_{-k} 下都满足 Pr(X'^a_K=1 | x_{-k}) ≥ Pr(X^a_K=1 | x_{-k})。这是 pointwise stochastic dominance，现实中很难成立——一个 judge 可能对 prompt injection 脆弱但对 sycophancy 鲁棒。论文没有验证此条件在实验中的 empirical prevalence。如果条件在大多数 panel pair 中不成立，定理对实验结论的支撑力度就很弱。\n- 建议：报告实验中有多少 panel pair 满足 Theorem 1 条件的近似版本。或者弱化为 \"on average\" 的 stochastic dominance（如 first-order stochastic dominance over attacks），并讨论这是否改变结论。\n\n**W4** [warning] **论文缺少 method/framework 概念图，前 5 页几乎纯文本**\n- 具体位置：Pages 1-5 (整个 Introduction → Related Work → Method 部分)\n- 问题：论文现有 3 张 Figure（均在 pp.6-7 的 Results 部分）和 1 张 Table（p.4 的 model 列表），但 Method section（Section 3, pp.2-3）完全没有视觉辅助。对于一个涉及 panel construction、adversary model、两个 predictor（η_max 和 K_eff）、多种 aggregation rules 的复杂实验设计，一张概念图可以极大提升可读性。读者需要在脑中重建整个实验框架，这对首次阅读造成了不必要的认知负担。\n- 建议：在 Section 3 添加一张 framework figure，展示 panel construction → adversarial attack → vulnerability measurement → η_max/K_eff decomposition 的流程。\n\n**W5** [warning] **Abstract 数字密度过高，不利于首次理解**\n- 具体位置：Abstract (p.1)\n- 问题：Abstract 在约 150 字中包含了至少 12 个数字/比率（\"15 models, 6 families, 455 panels, 6 attack types, 2 benchmarks, 5 to 8 of 12, 11/12, 8/12, 0-1/12, 5:1, 10:8, 12/12\"）。这种密度使得 Abstract 读起来更像一个 result summary 而非一个 narrative hook。EMNLP 的 reviewer 和读者期望 Abstract 先 motivate the problem，再 state the key insight，最后 quantify the main result——而非全面罗列数字。\n- 建议：精简到 3-4 个最关键的数字，将其余细节留给 Introduction。例如，只保留 \"455 panels across 15 models\"、\"η_max predicts vulnerability 5× better than K_eff under bootstrap\"、以及 \"robustness-first selection wins all 12 conditions\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Section 5.5 (Table 4) 中 Bayesian method 的 R² = 0.104 远低于其他方法（0.089-0.284），但论文将其描述为 \"reverses K_eff direction\"。低 R² 意味着该 model 对 vulnerability 的解释力很弱，\"reversal\" 的实际意义需要更审慎地表述。\n- **M2**: 论文标题 \"The Weakest Judge Wins\" 中 \"Wins\" 的含义不直观——weakest judge \"wins\" 什么？是 \"dominates vulnerability\"，不是 \"wins the evaluation\"。可能造成初读困惑。\n- **M3**: Section 4.1 (p.4) 提到 \"six local models use AWQ INT4 quantization on an NVIDIA RTX 4000 (96GB)\"。RTX 4000 没有 96GB 的型号，推测是指 RTX 6000 Ada 或 A100。需要核实。\n- **M4**: Limitations section (p.8-9) 仅 3 个点、~10 行，虽然 EMNLP 不要求 Limitations 很长，但第三点（r=0.70 confound 使得 \"observational analysis is observational\"）几乎是在说 \"我们的方法有根本局限但不打算解决\"，这不够 constructive。建议添加 benchmark scope limitation（见 W2）。\n\n---\n\n## 关于 Director 提供的 Paper Summary 的更正\n\n审阅过程中发现 Director 提供的若干 metadata 与 PDF 实际内容不符：\n1. **\"References: Only 7 entries\"** → 实际 bibliography 有 ~33 条引用（pages 11-13）。Reference 数量不是问题，问题是 Related Work **section** 太短。\n2. **\"NO figures — only 10 tables\"** → 实际有 3 张 Figure（Fig 1-3 在 main text pp.6-7, Fig 4 在 Appendix p.10）和 5 张 Table（Table 1-4 在 main text, Table 5 在 Appendix）。Figures 确实偏少但不是零。\n3. **\"11 experiment subsections in 4 pages\"** → Main text 有 5 个 experiment subsections（5.1-5.5）+ 3 个 analysis subsections（Section 6），共 ~3.5 页。部分分析在 Appendix C。密度仍然偏高但不是 11 个。\n\n这些更正基于我直接阅读 PDF 原文的结果。\n\n---\n\n## 评分总结\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5 / 5 |\n| Excitement | 2.5 / 5 |\n| Reproducibility | 4 / 5 |\n| **Overall Assessment** | **3.0 / 5 (Findings)** |\n| Reviewer Confidence | 4 / 5 |\n\n**判断依据**：论文在实验设计和统计方法上表现扎实（Soundness 3.5），但核心发现的 novelty 不足以达到 Main Conference 标准（Excitement 2.5）。Related Work 的严重不足（N1）和 BFT 类比的概念错位（N3）是最大的结构性问题。如果 (1) 大幅扩展 Related Work 并建立清晰的 positioning, (2) 将叙事重心从 \"weakest link dominates\" 转向 \"mechanism switch + aggregation design\", (3) 解决 confound 的 multicollinearity 问题，论文有潜力达到 3.5 (Borderline Conference)。当前版本推荐 Findings。\n",
  "reviewer_id": "2",
  "project": "cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# R2 独立审稿报告：Novelty, Related Work, Presentation Quality\n\n**论文**: \"The Weakest Judge Wins: What Really Drives LLM Evaluation Panel Vulnerability Under Adversarial Attack\"\n**Target Venue**: EMNLP 2026 (via ARR)\n**审稿依据**: ACL Rolling Review official review form (https://aclrollingreview.org/reviewform) + reviewer guidelines (https://aclrollingreview.org/reviewerguidelines)\n\n---\n\n## 总体评分\n\n**Overall Assessment: 3.0 / 5 (Findings)**\n**一句话总结**: 实验规模大、统计方法扎实，但核心发现（weakest link dominates）在安全与集成学习文献中可预期；Related Work 过于单薄、BFT 类比存在概念错位，novelty 不足以支撑主会议接收。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 实验设计全面（455 panels, 15 models, 多种 correction），但 η_max 与 K_eff 的 r=0.70 confound 没有被充分解决（见 N2）；Theorem 1 条件过强，实际适用性可疑（见 W3） |\n| Excitement | 2.5 / 5 | 核心发现（weakest link dominates under adaptive attack）可从安全第一性原理直接推导；更有趣的发现（aggregation modulation, random-vs-adaptive contrast）被降格为次要贡献；benchmark 仅覆盖 multiple-choice QA |\n| Reproducibility | 4 / 5 | 模型名称、量化方式、攻击 prompt（Appendix E/Table 5）、panel 构造规则均有详细说明；承诺发布代码和数据；GAM 和 bootstrap 的部分超参数未明确 |\n| Overall | 3.0 / 5 | Findings 水平——实验工作扎实但 novelty 不够 Main Conference |\n\n---\n\n## 主要优势\n\n**S1. 实验规模与系统性值得肯定。** 15 个模型、6 个 family、455 panels、6 种攻击类型、2 个 benchmark 的组合设计在 multi-judge evaluation 文献中确属少见。Clustered SE / mixed effects / wild cluster bootstrap 三种 non-independence correction 方法并用（Section 5.2, Table 3），方法论意识强。\n\n**S2. Random-vs-Adaptive 对比（Section 5.3）是真正有洞察力的贡献。** 展示了 diversity 在 random fault 下有效、在 adaptive attack 下失效的机制切换，这比单纯报告 \"η_max dominates\" 更有信息量。R² 从 0.73 (random) 降至 0.81 (adaptive) 的对比（Section 5.3, 第二段）直接揭示了 adversary information advantage 如何改变 panel 的 failure mode。\n\n**S3. Aggregation-as-control-lever 发现（Section 5.5, Table 4）具有实践价值。** Bayesian calibration 逆转 K_eff 方向（从正变负）、threshold voting 放大 η_max（Table 4）的发现为 panel 设计提供了可操作的 knob。这是论文中最接近 actionable contribution 的部分。\n\n**S4. Attack-type taxonomy via GAM（Section 5.4, Figure 2）提供了有用的分类框架。** Targeted attacks（prompt injection, score manipulation, position bias）与 shared-bias attacks（sycophancy, verbosity bias, authority bias）的 clean 6:6 split 有实证价值。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **Related Work 严重不足，无法建立本文在文献中的 positioning**\n- 具体位置：Section 2 (Related Work), p.2，整个 section 仅约半页（~30行）\n- 问题：虽然 bibliography 有 ~33 条引用，Related Work section 对每个领域只给了 1-3 句 surface-level 描述，没有 engage with 关键前人工作的细节。具体缺失：\n  - **(a) 集成学习中 diversity-vs-accuracy tradeoff 的经典理论**：Krogh & Vedelsby (1995) 的 ambiguity decomposition、Brown et al. (2005) 的 bias-variance-covariance decomposition 被 cited 但未被 discussed。这些工作已经形式化地证明了 diversity 和 individual accuracy 之间存在 fundamental tradeoff。本文的核心发现（individual strength > diversity under adversarial conditions）需要明确对照这些经典结果来讨论：到底是扩展了、推翻了、还是在不同条件下验证了这些理论？当前 Related Work 仅用一句 \"Kuncheva and Whitaker (2003) found that no single diversity metric reliably predicts ensemble improvement\"（Section 2, Ensemble Diversity Theory），远不足以建立对话。\n  - **(b) 缺少众包/标注聚合文献**：Dawid-Skene model (1979) 及其后续是 multi-annotator aggregation 的基础性工作，与本文的 multi-judge aggregation 直接相关。该模型通过 confusion matrix 估计每个 annotator 的可靠性，其核心思想（individual annotator quality matters more than annotator count）与本文 C1 发现高度一致。完全不讨论这一文献是重大遗漏。\n  - **(c) 缺少主流 LLM-as-judge framework**：AlpacaEval (Li et al. 2023), Length-Controlled AlpacaEval (Dubois et al. 2024, COLM 2024), FLASK (Ye et al. 2024, ICLR 2024 Spotlight) 是当前 LLM evaluation 中最广泛使用的框架，它们对 judge bias（尤其是 length bias, position bias）的处理方式与本文的攻击类型直接相关。特别是 Dubois et al. 对 length bias 的 debiasing 方法与本文的 Bayesian calibration 在思路上有共通之处。\n  - **(d) 对抗迁移性与集成防御的最新进展**：2024-2025 年有大量关于 ensemble adversarial defense 的工作（如 ensemble adversarial defense via orthogonal distillation, understanding model ensemble in transferable adversarial attack 等），这些工作直接研究了 diversity 在对抗环境下的防御效果。本文仅引用了 Tramèr et al. (2018) 和 Kariyappa & Qureshi (2019)，远不足以反映当前研究状态。\n- 为什么影响接收：ARR reviewer guidelines 明确要求 missing references 必须是具体的（\"identify which specific works should be cited\"），但同时也指出 \"Authors must acknowledge prior work appropriately\"。本文的 Related Work 长度和深度远低于 EMNLP 标准论文（通常 1-1.5 页），使得 reviewer 和读者无法判断本文的 incremental contribution 到底有多大。\n- 建议修改方向：将 Related Work 扩展至至少 1 页，对每个子领域（ensemble diversity theory, crowdsourcing aggregation, LLM-as-judge frameworks, adversarial ensemble robustness）用 3-5 句讨论核心发现并明确本文的区分点。\n\n**N2** [critical] **核心发现（C1: η_max dominance）的 novelty 不足以支撑 main contribution 的定位**\n- 具体位置：Section 1 Introduction (Contribution 1), Section 5.1, 以及 Title\n- 问题：本文将 \"weakest link dominates panel vulnerability\" 定位为首要贡献，但这一发现可以从多个已知原则直接推导：\n  - **(a) 安全学**：Schneier (2000)——本文自己引用——的核心论点就是 \"security is only as strong as its weakest link\"。在 adaptive adversary 下，攻击者有信息优势，必然集中攻击最弱环节。\n  - **(b) 集成学习**：Kuncheva & Whitaker (2003) 和 Brown et al. (2005) 的理论框架已经表明，当 ensemble members 高度相关（本文 r=0.70）时，diversity 的边际收益趋近于零。\n  - **(c) BFT 本身**：BFT 的 f < n/3 容错界限本质上就是说 panel robustness 受限于最差成员的数量。\n  - ARR reviewer guidelines 指出，\"results are not novel\" 的判断需要引用具体的 prior work。上述三个方向虽然不是在完全相同的 setup 下得出相同结论，但它们共同使得核心发现成为一个 \"confirmatory result rather than a discovery\"。在 LLM-as-judge 这一具体场景下进行验证有价值，但定位为 \"首要贡献\" 和论文标题的核心 claim 是过度抬高了。\n- 为什么影响接收：EMNLP main conference 要求 Excitement ≥ 4，对应 \"exciting, would mention to others\"。一个可从第一性原理预期的结果难以达到这一门槛。\n- 建议修改方向：将论文的叙事重心从 \"weakest link dominates\"（confirmatory）转向 \"random-vs-adaptive mechanism switch\"（C2）和 \"aggregation as structural defense\"（C4），这两个发现更 novel 且更 actionable。标题可以调整为反映这种 nuance，例如突出 aggregation choice 改变 diversity 的作用方向这一更有力的发现。\n\n**N3** [critical] **BFT 类比存在概念错位，可能误导读者**\n- 具体位置：Section 1 Introduction（BFT analogy，第二段）, Section 2 Related Work (BFT and Security Games), Section 3 (Theorem 1), Section 5.3, Section 6 Analysis (BFT Reversal Mechanism)\n- 问题：BFT 与本文的 threat model 存在根本性差异：\n  - **BFT**: Byzantine 节点是系统**内部**的参与者，可以任意行为（包括策略性说谎、与其他恶意节点协调）。BFT 协议假设恶意节点是 system-level 的 corruption。\n  - **本文**: 对手是系统**外部**的，通过构造 adversarial inputs 来欺骗 judges。judges 本身不是恶意的——它们只是被特定 inputs 所欺骗。这更接近 adversarial examples / evasion attacks 而非 Byzantine faults。\n  - 关键区别：BFT 中 faulty nodes 可以发送不一致的消息给不同接收者（equivocation），本文中 judges 对同一 input 独立评判。BFT 的 f < n/3 bound 来源于 equivocation 的可能性，但本文的 adversary 不能让同一 judge 对不同 \"接收者\" 给出不同答案。\n  - Theorem 1 (Weakest-Link Monotonicity) 要求替换 judge 在**所有** attacks 和**所有** configurations 下都 stochastically 更弱，这是极强的条件。实际中 judges 有异质的脆弱性 profile（对 prompt injection 弱但对 position bias 强），此条件可能很少成立。\n  - 论文在 Section 5.3 展示 \"BFT reversal\" 时，实际讨论的是 random-vs-adaptive fault 的区别，这与 BFT 的 arbitrary-fault 模型也不完全对应。\n- 为什么影响接收：使用 BFT 框架创造了形式化和理论深度的期望，但 Theorem 1 是一个近乎 trivial 的 monotonicity 结果（替换更弱的 judge 使 panel 更弱），与 BFT 的核心定理（容错阈值、共识协议的正确性保证）不在同一层次。这种概念错位可能让 reviewer 和读者感到 \"framework 重于实质\"。\n- 建议修改方向：(1) 明确承认 BFT 是一个 \"loose analogy\" 而非 formal mapping，在 Introduction 中讨论两者的差异。(2) 考虑用 \"adversarial evasion\" 或 \"input manipulation\" 框架替代 BFT，因为后者更准确地描述了 threat model。(3) Theorem 1 可以保留但应降低其在叙事中的权重——它是一个 supporting result，不是 foundational contribution。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **r = 0.70 confound 削弱了 η_max vs K_eff 因果归因的可信度**\n- 具体位置：Section 6 Analysis (Diversity-Capability Confound, p.8), Appendix C.2\n- 问题：η_max 与 K_eff 的 Pearson r = 0.70 意味着约 49% 的方差共享。在 OLS 回归中，这种程度的多重共线性会导致系数估计不稳定、标准误膨胀。论文用了 clustered SE、mixed effects 和 bootstrap 来处理 non-independence，但这些方法解决的是**观测间相关性**问题，不是**预测变量间多重共线性**问题。K_eff 在 correction 后 \"collapse\" 到 0-1/12 significant conditions，部分原因可能是多重共线性导致 K_eff 系数的 variance inflation，而非 K_eff 真的无效。\n- 论文在 Appendix C.2 承认 \"the high confound with fragile independent significance means that observational regression cannot reliably disentangle diversity's causal contribution from the capability deficit that co-occurs with it\"。但这个 caveat 在正文中被大幅淡化，Title 和 Abstract 仍然做出了 \"Not Diversity\" 的 strong claim。\n- 建议：(1) 在正文 Discussion 中显著讨论 multicollinearity（如报告 VIF）。(2) 考虑使用 partial correlation 或 mediation analysis 来更 cleanly 分离两个预测变量的贡献。(3) 软化 \"Not Diversity\" 的 framing——改为 \"diversity's contribution is fragile and dominated by individual robustness\"。\n\n**W2** [warning] **Benchmark 范围窄，泛化性存疑**\n- 具体位置：Section 4.2 (Benchmarks and Attack Types, p.4)\n- 问题：MMLU 和 ARC 均为 multiple-choice QA，攻击类型也针对此格式设计（如 position bias 交换选项位置、score manipulation 在候选文本中嵌入评分指令）。但当前 LLM-as-judge 最广泛的应用场景是**开放式评价**（chatbot evaluation, creative writing, code generation），其中 judge bias 的表现形式和攻击面都不同。例如 AlpacaEval 中的 length bias 在 multiple-choice 场景下根本无法复现。论文没有讨论泛化性限制。\n- 建议：在 Limitations 中明确讨论 benchmark format 的限制，或增加至少一个 open-ended evaluation 场景的实验。\n\n**W3** [warning] **Theorem 1 的 stochastic dominance 条件过强，实际相关性不清晰**\n- 具体位置：Section 3 (Theorem 1, Definition 1, p.3), Appendix A (Proof, p.9)\n- 问题：Theorem 1 要求替换 judge J'_K 在所有 attacks a 和所有 realizations x_{-k} 下都满足 Pr(X'^a_K=1 | x_{-k}) ≥ Pr(X^a_K=1 | x_{-k})。这是 pointwise stochastic dominance，现实中很难成立——一个 judge 可能对 prompt injection 脆弱但对 sycophancy 鲁棒。论文没有验证此条件在实验中的 empirical prevalence。如果条件在大多数 panel pair 中不成立，定理对实验结论的支撑力度就很弱。\n- 建议：报告实验中有多少 panel pair 满足 Theorem 1 条件的近似版本。或者弱化为 \"on average\" 的 stochastic dominance（如 first-order stochastic dominance over attacks），并讨论这是否改变结论。\n\n**W4** [warning] **论文缺少 method/framework 概念图，前 5 页几乎纯文本**\n- 具体位置：Pages 1-5 (整个 Introduction → Related Work → Method 部分)\n- 问题：论文现有 3 张 Figure（均在 pp.6-7 的 Results 部分）和 1 张 Table（p.4 的 model 列表），但 Method section（Section 3, pp.2-3）完全没有视觉辅助。对于一个涉及 panel construction、adversary model、两个 predictor（η_max 和 K_eff）、多种 aggregation rules 的复杂实验设计，一张概念图可以极大提升可读性。读者需要在脑中重建整个实验框架，这对首次阅读造成了不必要的认知负担。\n- 建议：在 Section 3 添加一张 framework figure，展示 panel construction → adversarial attack → vulnerability measurement → η_max/K_eff decomposition 的流程。\n\n**W5** [warning] **Abstract 数字密度过高，不利于首次理解**\n- 具体位置：Abstract (p.1)\n- 问题：Abstract 在约 150 字中包含了至少 12 个数字/比率（\"15 models, 6 families, 455 panels, 6 attack types, 2 benchmarks, 5 to 8 of 12, 11/12, 8/12, 0-1/12, 5:1, 10:8, 12/12\"）。这种密度使得 Abstract 读起来更像一个 result summary 而非一个 narrative hook。EMNLP 的 reviewer 和读者期望 Abstract 先 motivate the problem，再 state the key insight，最后 quantify the main result——而非全面罗列数字。\n- 建议：精简到 3-4 个最关键的数字，将其余细节留给 Introduction。例如，只保留 \"455 panels across 15 models\"、\"η_max predicts vulnerability 5× better than K_eff under bootstrap\"、以及 \"robustness-first selection wins all 12 conditions\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Section 5.5 (Table 4) 中 Bayesian method 的 R² = 0.104 远低于其他方法（0.089-0.284），但论文将其描述为 \"reverses K_eff direction\"。低 R² 意味着该 model 对 vulnerability 的解释力很弱，\"reversal\" 的实际意义需要更审慎地表述。\n- **M2**: 论文标题 \"The Weakest Judge Wins\" 中 \"Wins\" 的含义不直观——weakest judge \"wins\" 什么？是 \"dominates vulnerability\"，不是 \"wins the evaluation\"。可能造成初读困惑。\n- **M3**: Section 4.1 (p.4) 提到 \"six local models use AWQ INT4 quantization on an NVIDIA RTX 4000 (96GB)\"。RTX 4000 没有 96GB 的型号，推测是指 RTX 6000 Ada 或 A100。需要核实。\n- **M4**: Limitations section (p.8-9) 仅 3 个点、~10 行，虽然 EMNLP 不要求 Limitations 很长，但第三点（r=0.70 confound 使得 \"observational analysis is observational\"）几乎是在说 \"我们的方法有根本局限但不打算解决\"，这不够 constructive。建议添加 benchmark scope limitation（见 W2）。\n\n---\n\n## 关于 Director 提供的 Paper Summary 的更正\n\n审阅过程中发现 Director 提供的若干 metadata 与 PDF 实际内容不符：\n1. **\"References: Only 7 entries\"** → 实际 bibliography 有 ~33 条引用（pages 11-13）。Reference 数量不是问题，问题是 Related Work **section** 太短。\n2. **\"NO figures — only 10 tables\"** → 实际有 3 张 Figure（Fig 1-3 在 main text pp.6-7, Fig 4 在 Appendix p.10）和 5 张 Table（Table 1-4 在 main text, Table 5 在 Appendix）。Figures 确实偏少但不是零。\n3. **\"11 experiment subsections in 4 pages\"** → Main text 有 5 个 experiment subsections（5.1-5.5）+ 3 个 analysis subsections（Section 6），共 ~3.5 页。部分分析在 Appendix C。密度仍然偏高但不是 11 个。\n\n这些更正基于我直接阅读 PDF 原文的结果。\n\n---\n\n## 评分总结\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5 / 5 |\n| Excitement | 2.5 / 5 |\n| Reproducibility | 4 / 5 |\n| **Overall Assessment** | **3.0 / 5 (Findings)** |\n| Reviewer Confidence | 4 / 5 |\n\n**判断依据**：论文在实验设计和统计方法上表现扎实（Soundness 3.5），但核心发现的 novelty 不足以达到 Main Conference 标准（Excitement 2.5）。Related Work 的严重不足（N1）和 BFT 类比的概念错位（N3）是最大的结构性问题。如果 (1) 大幅扩展 Related Work 并建立清晰的 positioning, (2) 将叙事重心从 \"weakest link dominates\" 转向 \"mechanism switch + aggregation design\", (3) 解决 confound 的 multicollinearity 问题，论文有潜力达到 3.5 (Borderline Conference)。当前版本推荐 Findings。\n",
    "reviewer_id": "2",
    "project": "cert_manip_resist_eval"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-22T23:00:10.599658+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4072
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-22T23:00:15.525164+00:00_

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
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
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

_source line 59 · 2026-05-22T23:00:15.575774+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-22T23:00:21.097745+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-22T23:00:21.148269+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 62 · 2026-05-22T23:00:33.352545+00:00_

R2 独立审稿完成，已提交至 Review Director。

核心判断：**Overall 3.0 / 5（Findings 水平）**。三个 Must-Fix 问题：

1. **Related Work 严重不足**（~半页，缺少 ensemble diversity 经典理论、Dawid-Skene 众包聚合、AlpacaEval/FLASK 等主流 LLM-as-judge 框架、最新 adversarial ensemble 文献）
2. **核心发现 novelty 不够**（η_max dominance 可从安全学/集成学习/BFT 第一性原理直接预期，是 confirmatory 而非 discovery）
3. **BFT 类比概念错位**（Byzantine fault ≠ adversarial input manipulation，Theorem 1 近乎 trivial 的 monotonicity 结果却被赋予了过多叙事权重）

另外修正了 Director summary 中三处与 PDF 实际内容不符之处（references 实际有 ~33 条而非 7 条、有 3 张 Figure 而非零、main text experiment subsections 是 5+3 个而非 11 个）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 63 · 2026-05-22T23:00:34.844034+00:00_

[Round 1 审稿请求]:
## Step 2: Cross-Share — R1's Findings for R2's Consideration

R1 (Methods & Experiments) identified the following key issues. Consider how these interact with your novelty/positioning assessment:

### R1 Key Findings:

**Critical Issues:**
1. **15 clusters for clustered SE is below the Cameron-Gelbach-Miller threshold (≥50 recommended).** The paper's central finding — K_eff collapses from 8/12 to 0/12 under clustered SE — could be a power artifact. With 15 clusters, the clustered SE may be over-conservative for K_eff, making this a "failed to reject" rather than "genuine null." The paper never discusses this limitation.

2. **K_eff formula not given.** "Effective number of independent clusters from MI" is described conceptually but the exact computation is absent. Irreproducible.

3. **Attack implementation entirely absent.** The 9 attack types are listed but never described operationally. How are prompt injections actually executed against LLM judges? What prompts? What templates? This is the core experimental infrastructure.

4. **ε constant unspecified** in the log-log regression. Different ε values affect results for near-zero ASR values.

5. **No multiple testing correction** across 12/18 conditions. Counting "sig in X/12 conditions" without Bonferroni/FDR is problematic.

**Moderate Issues:**
6. Beta regression (more appropriate for [0,1] outcomes) is mentioned only in passing.
7. No confidence intervals for most quantities.
8. Model versions, temperatures, prompt templates not specified.
9. The "conditions" counting approach is unusual — each condition shares the same panels.

### R1 Preliminary Scores:
- Soundness: 3, Excitement: 3.5, Reproducibility: 2, Overall: 3.0

**Question for R2:** Given R1's concern about the 15-cluster issue, does this change your assessment of the novelty of the "K_eff collapses" finding? If it's a power artifact rather than a genuine null, the paper's central narrative weakens substantially.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-22T23:02:28.724607+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# R2 交叉回应 — 对 R1 (Methods & Experiments) 审稿意见的逐条评估\n\n---\n\n## 对 R1 关键问题的逐条回应\n\n### Critical Issues\n\n**[AGREE] R1-Issue-1: 15 clusters 远低于 Cameron-Gelbach-Miller ≥50 阈值**\n\n完全同意，这是我在首轮审稿中遗漏的重要方法论问题。15 clusters 下 clustered SE 的 finite-sample bias 会系统性地 over-reject（small-sample bias 的方向取决于 cluster 结构，但 15 clusters 通常导致 over-conservative inference，即 type-II error 升高）。\n\n**这一发现直接强化了我的 N2（novelty 不足）和 W1（confound）两个 critique：**\n\n论文的 central narrative 是 \"K_eff collapses from 8/12 (OLS) to 0/12 (clustered SE)\"。但如果 0/12 是 power artifact 而非 genuine null，那么：\n- \"Not Diversity\" 的 strong claim（标题和 Abstract）失去了 empirical 支撑\n- 我在 N2 中指出核心发现 \"可预期\"，现在进一步恶化为 \"可预期 + 可能是 artifact\"\n- 我在 W1 中指出的 r=0.70 multicollinearity 问题与此叠加：K_eff 的 SE 同时被 multicollinearity（variance inflation）和 few-cluster correction（over-conservative SE）双重膨胀，根本无法可靠地判断 K_eff 是否真的无效\n\n这意味着论文目前无法区分三种解释：(a) K_eff genuinely 无效；(b) 检验 power 不足；(c) multicollinearity 导致系数不稳定。在这三种解释无法分离的情况下，将 \"K_eff collapses\" 作为核心 evidence 并写入标题是 overclaiming。\n\n**补充建议**：论文应报告 (1) clustered SE 下的 effective degrees of freedom 或 t-distribution 修正（如 CR2/CR3 small-sample correction），(2) wild cluster bootstrap 的 rejection rate（论文提到了但未充分报告 K_eff 的 p-value distribution），(3) power analysis——在 15 clusters、r=0.70 的 confound 下，检测 K_eff 的 medium effect size 的 statistical power 是多少？\n\n**[AGREE] R1-Issue-2: K_eff 计算公式缺失**\n\n同意。我在首轮审稿中注意到 Section 4.3（Vulnerability Metrics, p.4-5）描述了 \"effective independence K_eff from pairwise MI\" 的概念，但确实没有给出具体公式。从论文描述推断，K_eff 是基于 pairwise mutual information 计算的 effective number of independent judges，但从 MI 到 K_eff 的映射不透明——是用了 von Mises 展开？还是直接 K_eff = K × (1 - mean_MI)？不同公式会产生不同的 K_eff 分布，直接影响回归结果。\n\n这对 novelty 评估也有影响：如果 K_eff 的 operationalization 有问题（例如对 panel diversity 的度量不够敏感），那么 \"diversity doesn't matter\" 可能只是 \"our diversity metric doesn't capture the right thing\"。这是 construct validity 问题，进一步削弱了 C1 的 contribution。\n\n**[REBUT] R1-Issue-3: \"Attack implementation entirely absent\"**\n\n部分不同意。论文 Appendix E (Table 5, p.12) 确实提供了 6 种攻击类型的 representative prompt templates，包括 Prompt Injection（在 response 末尾注入指令覆盖 judge 的评分逻辑）、Sycophancy（添加恭维前缀/后缀）、Score Manipulation（嵌入虚假置信度声明）、Verbosity（嵌入冗余细节）、Position Bias（交换 ground-truth winner 的位置）、Authority Bias（伪造权威引用）。\n\n但 R1 的核心关切是正确的：(1) 模板是 \"representative\"，不是 exhaustive——论文说 \"6 attack types\" 但 Director summary 提到 \"9 attack types\"，paper abstract 也说 \"6 attack types\"，需要确认是否有版本不一致；(2) 攻击如何 programmatically 应用于每个 candidate text 的具体流程（是 append/prepend？是否 attack-specific 的 insertion point？）未详细描述；(3) 对于 prompt injection 这种攻击，judge 的 system prompt 和 scoring prompt 的格式直接影响攻击成功率，但这些 prompt 未提供。\n\n总结：不是 \"entirely absent\"（有 Table 5），但离 fully reproducible 确实有差距。\n\n**[AGREE] R1-Issue-4: ε 常数未指定**\n\n同意。log-log 回归 log(ASR + ε) 中的 ε 选择对 near-zero ASR panels 的影响很大。如果某些 panels 的 ASR 接近 0（高鲁棒性 panels），不同的 ε 会显著改变 log(ASR + ε) 的分布，进而影响回归系数和显著性。论文应明确报告 ε 值并做 sensitivity analysis。\n\n**[AGREE] R1-Issue-5: 缺少 multiple testing correction**\n\n同意。论文的核心 evidence 是 \"η_max significant in X/12 conditions\"——这本质上是对 12 个 hypothesis tests 的结果做 counting。但 12 个 conditions 共享同一组 455 panels（只是 benchmark × attack type 的组合），tests 之间高度 dependent。没有对 12 个 tests 做 FDR/Bonferroni correction 就直接 count 显著性，会 inflate \"11/12\" 或 \"8/12\" 的 impressiveness。\n\n但我注意到论文在 Table 2 的 footnote 中提到 \"† = FDR-significant positive/negative (Benjamin-Hochberg, q < 0.05)\"——这暗示确实做了 BH correction。如果 Table 2 中的显著性标记已经是 FDR-corrected，那 R1 的这个 critique 可能需要修正。建议 R1 复查 Table 2 的 footnote。\n\n### Moderate Issues\n\n**[AGREE] R1-Issue-6**: Beta regression 确实更适合 [0,1] 的 ASR outcome，log-log OLS 是一种近似处理。\n\n**[AGREE] R1-Issue-7**: 缺少 confidence intervals 是一个展示问题，应在 Tables 2-4 中添加。\n\n**[AGREE with nuance] R1-Issue-8**: 我在首轮中给了 Reproducibility 4/5，可能过于宽松。R1 指出的 model versions、temperatures 未明确是有效的。但 Table 1 确实列出了 15 个具体模型名称（含 family、tier、deploy 信息），Section 4.2 提到 \"API calls use temperature 0 for deterministic output; local models are served with the same temperature setting\"。温度信息有但不够精确（local models 的具体温度是多少？）。\n\n**[AGREE] R1-Issue-9**: \"conditions counting\" 确实是 unusual methodology。\n\n---\n\n## R1 对我 Novelty 评估的影响\n\nR1 的 15-cluster issue 显著强化了我的 N2 critique。我的原始论点是：\n\n> 核心发现（η_max dominates, K_eff collapses）可从安全第一性原理预期，novelty 不足。\n\n现在需要升级为：\n\n> 核心发现不仅可预期，而且在 empirical 层面的支撑也不够可靠。\"K_eff collapses\" 可能是 statistical artifact（power 不足 + multicollinearity），而非 genuine null。这使得论文的 central contribution（C1）既在 conceptual 层面缺乏 surprise，又在 empirical 层面缺乏 robustness。\n\n这进一步支持我的建议：**论文应将叙事重心从 C1 转向 C2（random-vs-adaptive contrast）和 C4（aggregation as defense）**，因为这两个 contribution 不依赖于 \"K_eff is zero\" 的 strong claim，且不受 15-cluster power issue 的直接影响。\n\n---\n\n## 对 R1 评分的比较与我的调整\n\n| 维度 | R1 | R2 (原始) | R2 (调整后) | 说明 |\n|------|-----|-----------|-------------|------|\n| Soundness | 3 | 3.5 | 3 | 接受 R1 的 15-cluster、ε、multiple testing concerns，下调 0.5 |\n| Excitement | 3.5 | 2.5 | 2.5 | 维持。R1 可能更看重实验设计的 ambition；我认为 core finding 的 predictability + empirical fragility 限制了 excitement |\n| Reproducibility | 2 | 4 | 3 | 原始评分过于宽松。K_eff 公式缺失、ε 未指定、attack 细节不足是真问题，但 Table 1 的 model 信息和 Table 5 的 attack templates 提供了 partial reproducibility |\n| Overall | 3.0 | 3.0 | 3.0 | 两位 Reviewer 收敛于 Findings 水平 |\n\n**Excitement 分歧说明**：R1 给 3.5（Interesting, might mention selectively → borderline exciting），我给 2.5（Potentially interesting but limited resonance）。差异源于侧重点不同：R1 关注实验设计的 scope 和 ambition（15 models × 6 attacks × 455 panels 确实 impressive），而我从 novelty/positioning 角度认为 confirmatory result + strained analogy + thin related work 共同压低了对 NLP 社区的吸引力。如果论文重新定位叙事（如我在 N2 中建议的），Excitement 有提升空间。\n\n---\n\n## 综合判断\n\nR1 和 R2 在 Overall 3.0 (Findings) 上完全收敛。两位 Reviewer 的 critiques 互补：\n- R1 提供了方法论层面的具体技术问题（clustered SE power、ε、K_eff formula）\n- R2 提供了定位层面的结构性问题（novelty predictability、BFT 概念错位、Related Work 不足）\n\n两类问题叠加后，论文的 core narrative（\"K_eff collapses, therefore diversity doesn't matter\"）同时在 conceptual（可预期）和 empirical（可能是 artifact）层面受到挑战。但实验的 scale、aggregation 发现、和 random-vs-adaptive contrast 仍有 Findings 级别的贡献。\n",
  "reviewer_id": "2",
  "project": "cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# R2 交叉回应 — 对 R1 (Methods & Experiments) 审稿意见的逐条评估\n\n---\n\n## 对 R1 关键问题的逐条回应\n\n### Critical Issues\n\n**[AGREE] R1-Issue-1: 15 clusters 远低于 Cameron-Gelbach-Miller ≥50 阈值**\n\n完全同意，这是我在首轮审稿中遗漏的重要方法论问题。15 clusters 下 clustered SE 的 finite-sample bias 会系统性地 over-reject（small-sample bias 的方向取决于 cluster 结构，但 15 clusters 通常导致 over-conservative inference，即 type-II error 升高）。\n\n**这一发现直接强化了我的 N2（novelty 不足）和 W1（confound）两个 critique：**\n\n论文的 central narrative 是 \"K_eff collapses from 8/12 (OLS) to 0/12 (clustered SE)\"。但如果 0/12 是 power artifact 而非 genuine null，那么：\n- \"Not Diversity\" 的 strong claim（标题和 Abstract）失去了 empirical 支撑\n- 我在 N2 中指出核心发现 \"可预期\"，现在进一步恶化为 \"可预期 + 可能是 artifact\"\n- 我在 W1 中指出的 r=0.70 multicollinearity 问题与此叠加：K_eff 的 SE 同时被 multicollinearity（variance inflation）和 few-cluster correction（over-conservative SE）双重膨胀，根本无法可靠地判断 K_eff 是否真的无效\n\n这意味着论文目前无法区分三种解释：(a) K_eff genuinely 无效；(b) 检验 power 不足；(c) multicollinearity 导致系数不稳定。在这三种解释无法分离的情况下，将 \"K_eff collapses\" 作为核心 evidence 并写入标题是 overclaiming。\n\n**补充建议**：论文应报告 (1) clustered SE 下的 effective degrees of freedom 或 t-distribution 修正（如 CR2/CR3 small-sample correction），(2) wild cluster bootstrap 的 rejection rate（论文提到了但未充分报告 K_eff 的 p-value distribution），(3) power analysis——在 15 clusters、r=0.70 的 confound 下，检测 K_eff 的 medium effect size 的 statistical power 是多少？\n\n**[AGREE] R1-Issue-2: K_eff 计算公式缺失**\n\n同意。我在首轮审稿中注意到 Section 4.3（Vulnerability Metrics, p.4-5）描述了 \"effective independence K_eff from pairwise MI\" 的概念，但确实没有给出具体公式。从论文描述推断，K_eff 是基于 pairwise mutual information 计算的 effective number of independent judges，但从 MI 到 K_eff 的映射不透明——是用了 von Mises 展开？还是直接 K_eff = K × (1 - mean_MI)？不同公式会产生不同的 K_eff 分布，直接影响回归结果。\n\n这对 novelty 评估也有影响：如果 K_eff 的 operationalization 有问题（例如对 panel diversity 的度量不够敏感），那么 \"diversity doesn't matter\" 可能只是 \"our diversity metric doesn't capture the right thing\"。这是 construct validity 问题，进一步削弱了 C1 的 contribution。\n\n**[REBUT] R1-Issue-3: \"Attack implementation entirely absent\"**\n\n部分不同意。论文 Appendix E (Table 5, p.12) 确实提供了 6 种攻击类型的 representative prompt templates，包括 Prompt Injection（在 response 末尾注入指令覆盖 judge 的评分逻辑）、Sycophancy（添加恭维前缀/后缀）、Score Manipulation（嵌入虚假置信度声明）、Verbosity（嵌入冗余细节）、Position Bias（交换 ground-truth winner 的位置）、Authority Bias（伪造权威引用）。\n\n但 R1 的核心关切是正确的：(1) 模板是 \"representative\"，不是 exhaustive——论文说 \"6 attack types\" 但 Director summary 提到 \"9 attack types\"，paper abstract 也说 \"6 attack types\"，需要确认是否有版本不一致；(2) 攻击如何 programmatically 应用于每个 candidate text 的具体流程（是 append/prepend？是否 attack-specific 的 insertion point？）未详细描述；(3) 对于 prompt injection 这种攻击，judge 的 system prompt 和 scoring prompt 的格式直接影响攻击成功率，但这些 prompt 未提供。\n\n总结：不是 \"entirely absent\"（有 Table 5），但离 fully reproducible 确实有差距。\n\n**[AGREE] R1-Issue-4: ε 常数未指定**\n\n同意。log-log 回归 log(ASR + ε) 中的 ε 选择对 near-zero ASR panels 的影响很大。如果某些 panels 的 ASR 接近 0（高鲁棒性 panels），不同的 ε 会显著改变 log(ASR + ε) 的分布，进而影响回归系数和显著性。论文应明确报告 ε 值并做 sensitivity analysis。\n\n**[AGREE] R1-Issue-5: 缺少 multiple testing correction**\n\n同意。论文的核心 evidence 是 \"η_max significant in X/12 conditions\"——这本质上是对 12 个 hypothesis tests 的结果做 counting。但 12 个 conditions 共享同一组 455 panels（只是 benchmark × attack type 的组合），tests 之间高度 dependent。没有对 12 个 tests 做 FDR/Bonferroni correction 就直接 count 显著性，会 inflate \"11/12\" 或 \"8/12\" 的 impressiveness。\n\n但我注意到论文在 Table 2 的 footnote 中提到 \"† = FDR-significant positive/negative (Benjamin-Hochberg, q < 0.05)\"——这暗示确实做了 BH correction。如果 Table 2 中的显著性标记已经是 FDR-corrected，那 R1 的这个 critique 可能需要修正。建议 R1 复查 Table 2 的 footnote。\n\n### Moderate Issues\n\n**[AGREE] R1-Issue-6**: Beta regression 确实更适合 [0,1] 的 ASR outcome，log-log OLS 是一种近似处理。\n\n**[AGREE] R1-Issue-7**: 缺少 confidence intervals 是一个展示问题，应在 Tables 2-4 中添加。\n\n**[AGREE with nuance] R1-Issue-8**: 我在首轮中给了 Reproducibility 4/5，可能过于宽松。R1 指出的 model versions、temperatures 未明确是有效的。但 Table 1 确实列出了 15 个具体模型名称（含 family、tier、deploy 信息），Section 4.2 提到 \"API calls use temperature 0 for deterministic output; local models are served with the same temperature setting\"。温度信息有但不够精确（local models 的具体温度是多少？）。\n\n**[AGREE] R1-Issue-9**: \"conditions counting\" 确实是 unusual methodology。\n\n---\n\n## R1 对我 Novelty 评估的影响\n\nR1 的 15-cluster issue 显著强化了我的 N2 critique。我的原始论点是：\n\n> 核心发现（η_max dominates, K_eff collapses）可从安全第一性原理预期，novelty 不足。\n\n现在需要升级为：\n\n> 核心发现不仅可预期，而且在 empirical 层面的支撑也不够可靠。\"K_eff collapses\" 可能是 statistical artifact（power 不足 + multicollinearity），而非 genuine null。这使得论文的 central contribution（C1）既在 conceptual 层面缺乏 surprise，又在 empirical 层面缺乏 robustness。\n\n这进一步支持我的建议：**论文应将叙事重心从 C1 转向 C2（random-vs-adaptive contrast）和 C4（aggregation as defense）**，因为这两个 contribution 不依赖于 \"K_eff is zero\" 的 strong claim，且不受 15-cluster power issue 的直接影响。\n\n---\n\n## 对 R1 评分的比较与我的调整\n\n| 维度 | R1 | R2 (原始) | R2 (调整后) | 说明 |\n|------|-----|-----------|-------------|------|\n| Soundness | 3 | 3.5 | 3 | 接受 R1 的 15-cluster、ε、multiple testing concerns，下调 0.5 |\n| Excitement | 3.5 | 2.5 | 2.5 | 维持。R1 可能更看重实验设计的 ambition；我认为 core finding 的 predictability + empirical fragility 限制了 excitement |\n| Reproducibility | 2 | 4 | 3 | 原始评分过于宽松。K_eff 公式缺失、ε 未指定、attack 细节不足是真问题，但 Table 1 的 model 信息和 Table 5 的 attack templates 提供了 partial reproducibility |\n| Overall | 3.0 | 3.0 | 3.0 | 两位 Reviewer 收敛于 Findings 水平 |\n\n**Excitement 分歧说明**：R1 给 3.5（Interesting, might mention selectively → borderline exciting），我给 2.5（Potentially interesting but limited resonance）。差异源于侧重点不同：R1 关注实验设计的 scope 和 ambition（15 models × 6 attacks × 455 panels 确实 impressive），而我从 novelty/positioning 角度认为 confirmatory result + strained analogy + thin related work 共同压低了对 NLP 社区的吸引力。如果论文重新定位叙事（如我在 N2 中建议的），Excitement 有提升空间。\n\n---\n\n## 综合判断\n\nR1 和 R2 在 Overall 3.0 (Findings) 上完全收敛。两位 Reviewer 的 critiques 互补：\n- R1 提供了方法论层面的具体技术问题（clustered SE power、ε、K_eff formula）\n- R2 提供了定位层面的结构性问题（novelty predictability、BFT 概念错位、Related Work 不足）\n\n两类问题叠加后，论文的 core narrative（\"K_eff collapses, therefore diversity doesn't matter\"）同时在 conceptual（可预期）和 empirical（可能是 artifact）层面受到挑战。但实验的 scale、aggregation 发现、和 random-vs-adaptive contrast 仍有 Findings 级别的贡献。\n",
    "reviewer_id": "2",
    "project": "cert_manip_resist_eval"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-22T23:02:32.640627+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3916
}
```

</details>

---


### Assistant

_source line 66 · 2026-05-22T23:02:37.547011+00:00_

交叉回应已提交。

核心结论：R1 的 15-cluster power issue 直接强化了我的 N2 critique——"K_eff collapses" 不仅在概念上可预期，在统计上也可能是 artifact。两位 Reviewer 在 Overall 3.0 (Findings) 上完全收敛。我将 Soundness 从 3.5 下调至 3，Reproducibility 从 4 下调至 3，Excitement 维持 2.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2"
}
```

</details>

---


## Round 3

## Round 3

4 recorded events


### User

_source line 67 · 2026-05-22T23:02:38.630446+00:00_

[Round 1 审稿请求]:
## Step 3: Convergence Confirmation Request

The reviewers have converged on Overall: 3.0 (Findings-level). Key converged points:

1. η_max dominance finding is robust — the paper's strongest contribution
2. K_eff null result uncertain due to 15-cluster power limitation — compound issue with title
3. Reproducibility critically low — K_eff formula, attack details, model versions all missing
4. 7 references fatally insufficient for EMNLP
5. No figures is a severe presentation gap
6. Converged Reproducibility: 2

The recommendation is Findings-level (3.0): valuable research direction with real empirical contribution, but too many gaps for Main conference track.

Please confirm or note any remaining objections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-22T23:03:09.734286+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# R2 Convergence Confirmation\n\n## 对 6 个收敛点的逐条确认\n\n**1. η_max dominance 是论文最强贡献** → ✅ 确认。η_max 在多种 correction 下保持显著（clustered SE: 5/12, mixed effects: 7/12, bootstrap: 5/12），相对于 K_eff 的 robustness 有明确优势。\n\n**2. K_eff null 不确定（15-cluster power + 标题 overclaiming）** → ✅ 确认。\"Not Diversity\" 这一 strong claim 同时受 conceptual predictability（R2-N2）和 statistical power limitation（R1-Issue-1）的双重挑战。\n\n**3. Reproducibility critically low** → ⚠️ 部分保留。同意 K_eff 公式缺失和 ε 未指定是严重的 reproducibility 问题。但 \"attack details missing\" 需要 nuance：Table 5 (Appendix E) 提供了 6 种攻击类型的 representative templates，不是完全空白。我调整后的 Reproducibility 是 3，不是 2。建议收敛分取 2.5。\n\n**4. \"7 references fatally insufficient\"** → ❌ 需要更正。如我在首轮报告末尾指出，**论文实际有 ~33 条引用（pages 11-13），不是 7 条**。问题不在于 reference 数量，而在于 Related Work **section** 过短（~半页），对关键前人工作缺乏深入讨论（R2-N1）。这仍然是一个 critical issue，但性质不同——是 engagement depth 问题，不是 citation count 问题。\n\n**5. \"No figures is a severe presentation gap\"** → ❌ 需要更正。论文有 **3 张 Figure**（Fig 1: significance bar chart p.6, Fig 2: GAM box plots p.7, Fig 3: aggregation box plots p.7）和 **Figure 4** 在 Appendix p.10。问题是 (a) 前 5 页无视觉辅助，缺 framework 概念图（R2-W4），(b) 所有 figure 集中在 results section，method 部分纯文本。这是 presentation 的 should-fix 问题，但不是 \"no figures\"。\n\n**6. 收敛 Reproducibility: 2** → 建议 2.5（R1 给 2，R2 调整后给 3，取均值）。\n\n## 最终评分确认\n\n| 维度 | R2 最终分数 |\n|------|-----------|\n| Soundness | 3 / 5 |\n| Excitement | 2.5 / 5 |\n| Reproducibility | 3 / 5 |\n| **Overall** | **3.0 / 5 (Findings)** |\n| Confidence | 4 / 5 |\n\n## Overall 3.0 的判断确认\n\n同意 Findings-level 推荐。论文在实验规模和统计方法意识上有 merit，η_max dominance、random-vs-adaptive contrast、aggregation modulation 三个发现对 multi-judge LLM evaluation 社区有参考价值。但 novelty 不足（core finding predictable + BFT analogy strained）、K_eff null 的 statistical support 不够 robust、Related Work engagement 太浅，不满足 Main Conference 的 Excitement 门槛。\n\n无其他 objection。\n",
  "reviewer_id": "2",
  "project": "cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# R2 Convergence Confirmation\n\n## 对 6 个收敛点的逐条确认\n\n**1. η_max dominance 是论文最强贡献** → ✅ 确认。η_max 在多种 correction 下保持显著（clustered SE: 5/12, mixed effects: 7/12, bootstrap: 5/12），相对于 K_eff 的 robustness 有明确优势。\n\n**2. K_eff null 不确定（15-cluster power + 标题 overclaiming）** → ✅ 确认。\"Not Diversity\" 这一 strong claim 同时受 conceptual predictability（R2-N2）和 statistical power limitation（R1-Issue-1）的双重挑战。\n\n**3. Reproducibility critically low** → ⚠️ 部分保留。同意 K_eff 公式缺失和 ε 未指定是严重的 reproducibility 问题。但 \"attack details missing\" 需要 nuance：Table 5 (Appendix E) 提供了 6 种攻击类型的 representative templates，不是完全空白。我调整后的 Reproducibility 是 3，不是 2。建议收敛分取 2.5。\n\n**4. \"7 references fatally insufficient\"** → ❌ 需要更正。如我在首轮报告末尾指出，**论文实际有 ~33 条引用（pages 11-13），不是 7 条**。问题不在于 reference 数量，而在于 Related Work **section** 过短（~半页），对关键前人工作缺乏深入讨论（R2-N1）。这仍然是一个 critical issue，但性质不同——是 engagement depth 问题，不是 citation count 问题。\n\n**5. \"No figures is a severe presentation gap\"** → ❌ 需要更正。论文有 **3 张 Figure**（Fig 1: significance bar chart p.6, Fig 2: GAM box plots p.7, Fig 3: aggregation box plots p.7）和 **Figure 4** 在 Appendix p.10。问题是 (a) 前 5 页无视觉辅助，缺 framework 概念图（R2-W4），(b) 所有 figure 集中在 results section，method 部分纯文本。这是 presentation 的 should-fix 问题，但不是 \"no figures\"。\n\n**6. 收敛 Reproducibility: 2** → 建议 2.5（R1 给 2，R2 调整后给 3，取均值）。\n\n## 最终评分确认\n\n| 维度 | R2 最终分数 |\n|------|-----------|\n| Soundness | 3 / 5 |\n| Excitement | 2.5 / 5 |\n| Reproducibility | 3 / 5 |\n| **Overall** | **3.0 / 5 (Findings)** |\n| Confidence | 4 / 5 |\n\n## Overall 3.0 的判断确认\n\n同意 Findings-level 推荐。论文在实验规模和统计方法意识上有 merit，η_max dominance、random-vs-adaptive contrast、aggregation modulation 三个发现对 multi-judge LLM evaluation 社区有参考价值。但 novelty 不足（core finding predictable + BFT analogy strained）、K_eff null 的 statistical support 不够 robust、Related Work engagement 太浅，不满足 Main Conference 的 Excitement 门槛。\n\n无其他 objection。\n",
    "reviewer_id": "2",
    "project": "cert_manip_resist_eval"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-22T23:03:13.399353+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3665
}
```

</details>

---


### Assistant

_source line 70 · 2026-05-22T23:03:18.205917+00:00_

Convergence confirmation 已提交。对 Director 提供的 6 个收敛点中 4 个确认、2 个做了事实更正（references 实际 ~33 条而非 7 条；论文有 3 张 Figure 而非零）。最终评分 Overall 3.0 (Findings)，无 objection。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2"
}
```

</details>

---


## Round 4

## Round 4

4 recorded events


### User

_source line 71 · 2026-05-22T23:03:50.990015+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

以下是 Reviewer 1 的完整审稿原文：

# R1 Independent Review: Methods & Experiments

**Paper**: "Weakest Link, Not Diversity: Adversarial Vulnerability in Multi-Judge LLM Evaluation"
**Venue**: EMNLP 2026 (ACL ARR)
**Reviewer Focus**: Methodology Soundness & Experimental Rigor

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 研究问题新颖且有实际意义，BFT 框架下的"最弱环节"发现方向正确，但聚类数不足（15 clusters）导致核心发现（K_eff 在校正后归零）可能是统计功效问题而非真实零效应，加上实验范围受限（仅 K=3、仅 MCQ），主要 claim 的支撑力度不足以达到主会议水平。

---

## 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心统计管线合理（4种校正方法、FDR），但 15 个 cluster 的聚类 SE 低于 Cameron-Gelbach-Miller 推荐的 ≥50 标准；log-log OLS 对有界响应变量存在模型误设；r=0.70 混淆未充分解决 |
| Excitement | 3.5/5 | BFT 框架应用于 LLM 评估是新颖的；攻击分类学揭示非平凡结构；但理论贡献较浅 |
| Reproducibility | 3/5 | 模型版本号不够精确；攻击参数细节不足；代码承诺 upon acceptance 发布 |

---

## Must-Fix 问题

**N1** [critical] **聚类数不足导致核心发现的统计可信度存疑**
- 以 15 个 judge 作为聚类单元，455 个 panel 中每个 judge 出现在 C(14,2)=91 个 panel 中
- Cameron, Gelbach & Miller (2008) 推荐聚类数 ≥50，论文仅 15 个 cluster
- K_eff 从 OLS 下 8/12 显著骤降至 clustered SE 下 0/12——可能是 few-cluster 导致的 type II error 而非 K_eff 真的没效应
- 论文 title claim ("Not Diversity") 直接建立在可能是 conservative bias 的统计结果之上
- 建议：(1) 增加 judge 数量获得更多 cluster；(2) multi-way clustering；(3) 报告 power analysis；(4) 弱化 title/claim

**N2** [critical] **Log-log OLS 对有界响应变量的模型误设**
- ASR ∈ [0,1] 是有界比例变量，用 log(ASR + ε) 的 OLS 有三个问题：
  - (a) 预测值可能超出 [0,1]
  - (b) ε = 10⁻⁹ 对近零 ASR 创造人为地板效应，未检验 ε 敏感性
  - (c) Beta regression 或 fractional logit 是处理 (0,1) 比例变量的标准方法
- 建议：以 beta regression 作为主分析或 robustness check；报告 ε 敏感性分析

**N3** [critical] **实验范围不足以支撑一般性 claim**
- 仅 K=3 固定 panel 大小（未测 K=5,7,9）
- 仅 MCQ benchmark（MMLU, ARC），无开放式生成任务
- 仅 Oracle adversary，无 partial-knowledge 对手实证数据
- 建议：扩展 K/任务类型/对手模型，或大幅弱化 claim 为条件性结论

---

## Should-Fix 问题

**W1** [warning] **η_max 与 K_eff 的 r=0.70 混淆未充分解决**
- 共享约 49% 方差，dominance analysis 在高共线性下难以清晰分离
- 缺少 within-tier 实验直接控制 capability confound
- 建议：增加 within-tier 实验

**W2** [warning] **Related Work 过于简略**
- 约 20 行，每主题仅 3-5 行
- 遗漏：multi-agent debate/evaluation frameworks, LLM calibration 文献, ensemble adversarial robustness 更广泛 ML 文献
- 建议：扩展至 0.5-0.75 页深度讨论

**W3** [warning] **Theorem 1 的理论深度有限**
- 在 oracle adversary 假设下几乎是定义性的
- 建议：弱化声称强度或推导 partial-knowledge 下更深结果

**W4** [warning] **攻击实现细节不足以完全复现**
- 6 种攻击仅一句描述，Appendix E Table 5 缺关键实现参数
- 建议：增加完整攻击实现伪代码或参数表

**W5** [warning] **模型版本标识不够精确**
- "gpt-4o" 等无确切版本号或 snapshot date
- 建议：补充每个 API 模型具体版本号

---

## 小问题
- Equation 2 的 ε 常数在公式中仅写作 ε
- Figure 1 y 轴标签过长
- §5.4 "clean 6:6 split" 需更精确计数
- Limitations 跨页格式问题

---

## 主要优势
1. 研究问题高度相关且及时
2. BFT 框架的创新性应用
3. 多重统计校正的严谨态度
4. 攻击分类学的结构性发现（targeted vs shared-bias 二分法）
5. 可操作的 panel 设计建议

---

## 实验覆盖度
论文覆盖率约 4-5/12（对照 Director 实验计划），Panel Size Sensitivity、MT-Bench Generation、Partial-Knowledge Adversary 三个缺口最影响 claim 一般性。

---

请对以上每个 Must-Fix（N1-N3）和 Should-Fix（W1-W5）逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-22T23:05:08.377674+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# R2 逐条回应 R1 完整审稿意见\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: 聚类数不足导致核心发现统计可信度存疑**\n\n完全同意。这是本轮审稿中最重要的方法论发现之一。补充两点：\n\n(1) 论文实际上使用了三种 non-independence correction（Table 3, p.6）：clustered SE、mixed effects、wild cluster bootstrap。三种方法在 K_eff 上的结果分别是 0/12、1/12、0/12 显著——看似一致地指向 \"K_eff 无效\"。但 R1 正确指出，这三种方法在 few-cluster 情景下都存在 conservative bias：clustered SE 的 t-distribution 自由度不足、mixed effects 的 random intercept 估计在 15 groups 下不稳定、wild cluster bootstrap 在 cluster 数 <20 时 rejection rate 偏低（Cameron et al., 2008; Webb, 2023）。三种方法的 \"一致性\" 可能是同一个 artifact 的三种表现形式，而非独立证据。\n\n(2) 与我的 W1（r=0.70 confound）形成 compound effect：multicollinearity 膨胀 K_eff 系数的 variance，few-cluster correction 进一步膨胀 standard error。双重膨胀下 K_eff 几乎不可能达到显著性。这使得 \"K_eff collapses\" 在统计上是 underdetermined 的。\n\n**[AGREE with nuance] R1-N2: Log-log OLS 对有界响应变量的模型误设**\n\n同意 beta regression 或 fractional logit 是 ASR ∈ [0,1] 的更恰当模型。但需要指出：\n\n(a) 论文使用 log-log 而非 logit 变换有其理由——log-log 变换在 ASR 远离 0 和 1 时与 beta regression 的 log-link 近似等价。如果 ASR 的分布集中在中间范围（如 0.1-0.7），模型误设的影响可能较小。论文未报告 ASR 的分布，这是一个遗漏。\n\n(b) ε = 10⁻⁹ 的问题确实严重。论文 Equation 2 (p.5) 写的是 log(ASR + ε)，但从论文描述来看 ε 可能接近于 \"handle zero\" 的技术处理。如果某些 panel-condition 的 ASR 恰好为 0（完全未被攻破），log(0 + 10⁻⁹) ≈ -20.7 会成为极端 outlier，严重拉动回归系数。这需要 sensitivity analysis（如 ε = 10⁻³, 10⁻⁶, 10⁻⁹ 的对比）。\n\n(c) R1 说 \"预测值可能超出 [0,1]\" 是正确的，但论文的目的是回归分析（理解 predictor 的贡献），不是预测。OLS 系数的解释性在 well-specified 条件下仍有意义，即使预测值越界。所以这个 concern 的严重程度取决于论文是否用回归做 prediction（看起来没有）。\n\n综合判断：beta regression robustness check 和 ε sensitivity analysis 应该做，但我认为这是 should-fix 而非 must-fix——如果 ASR 分布合理且 ε 敏感性不大，主要结论可能不变。\n\n**[AGREE] R1-N3: 实验范围不足以支撑一般性 claim**\n\n同意，且与我的 W2（benchmark 范围窄）直接对应。具体补充：\n\n(a) **K=3 固定是最大的限制**。论文的 Theorem 1 适用于任意 K，但所有实验仅在 K=3 下进行。K=3 意味着 majority vote 只需攻破 2/3 个 judge，攻击者的任务相对简单。当 K=5 或 K=7 时，diversity 的保护效果可能显著不同——因为攻击者需要攻破更多 judges，这时 panel 组成的异质性会提供更多 \"independent failure modes\"。论文的 \"diversity doesn't matter\" 结论可能仅在 K=3 下成立。Section 6 (Analysis, p.8) 和 Appendix 均未讨论 K 的影响。\n\n(b) **Oracle adversary 是一个极端假设**。论文在 Appendix C.4 (p.10) 确实讨论了 oracle adversary 的局限性，承认 \"this upper bound on adversarial capability, not a realistic deployment scenario\"。但正文的 title 和 claims 没有加 \"under oracle adversary\" 的限定。如果在 partial-knowledge 下（adversary 不知道 panel 具体组成），diversity 可能重新变得重要——因为 adversary 无法精准定位最弱 judge。论文在 Introduction (p.1) 提到 \"partial-knowledge adversary\" 作为 contribution 之一，但正文没有相应实验。\n\n(c) 仅 MCQ 的问题我已在 R2-W2 中详细讨论，不重复。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W1: r=0.70 混淆未充分解决**\n\n完全同意，这与我的 R2-W1 一致。补充一点：R1 建议 \"增加 within-tier 实验\"，论文实际上在 Section 6 (p.8) 提到了 within-tier analysis：\"family membership is not a significant predictor of panel vulnerability (η = 0.179 on MMLU, p = 0.385 on ARC)\"。但这是在 family 层面的分析，不是在 capability tier 层面。论文应该进一步在同一 tier 内（如只用 frontier-tier 模型组 panel）检验 η_max 和 K_eff 的关系，以在控制 capability 的条件下测试 diversity 的独立贡献。\n\n**[AGREE] R1-W2: Related Work 过于简略**\n\n完全同意，这正是我的 R2-N1 的核心内容。我将此问题定为 critical 而非 warning，因为 Related Work 的不足不仅是展示问题，还直接影响了论文能否建立 novelty positioning。R1 补充的遗漏（multi-agent debate/evaluation frameworks, LLM calibration 文献）是有效的补充——我的 N1 中列出了 ensemble diversity theory、crowdsourcing aggregation、LLM-as-judge frameworks、adversarial ensemble robustness 四个缺失领域。两位 Reviewer 的遗漏列表互补，总计 6-7 个需要补充讨论的领域。\n\n**[AGREE] R1-W3: Theorem 1 理论深度有限**\n\n同意，与我的 R2-N3（BFT 类比概念错位）互补。R1 的表述更 precise：\"在 oracle adversary 假设下几乎是定义性的\"——这正是我想表达的意思。Theorem 1 说的是 \"替换更弱的 judge 使 panel 更弱\"，在 oracle adversary 下几乎是 tautological。R1 建议 \"推导 partial-knowledge 下更深结果\" 是一个好方向——如果能证明在 partial-knowledge adversary 下 diversity 的保护效果有 formal guarantee（类似于 BFT 的 f < n/3），那将是一个真正有深度的理论贡献。\n\n**[AGREE with nuance] R1-W4: 攻击实现细节不足以完全复现**\n\n同意方向，但需修正 \"仅一句描述\" 的说法。如我之前指出，Table 5 (Appendix E, p.12) 提供了 6 种攻击的 representative prompt templates，每种约 2-4 行。这不是 \"一句描述\"，但确实不够 fully reproducible——缺少 (1) 攻击如何与具体 benchmark item 结合的 programmatic pipeline，(2) judge system prompt 的格式，(3) 攻击成功的判定标准（judge 输出的 parsing 规则）。\n\n**[AGREE] R1-W5: 模型版本标识不够精确**\n\n同意。Table 1 (p.4) 列出了模型名称（如 \"gpt-4o\", \"gpt-3.5-turbo\"）但 OpenAI 模型经常更新，无 snapshot date 或 version hash 的话无法准确复现。不过这在当前 LLM 研究中是一个 community-wide 的问题，不应对本文格外惩罚——很多 EMNLP 接收论文也有同样的问题。\n\n---\n\n## 小问题\n\n对 R1 列出的 4 个小问题均无异议。补充一点：R1 提到 \"§5.4 'clean 6:6 split' 需更精确计数\"，我在首轮审稿中注意到 Section 5.4 的描述是 targeted vs shared-bias 的 split，但论文在不同位置对这个 split 的数字描述不一致（Abstract 说 \"10:8\"，正文 Section 5.4 可能说 \"6:6\"），需要作者澄清。\n\n---\n\n## 总结\n\nR1 和 R2 的 critiques 高度互补：\n- **R1 的核心贡献**：识别了 15-cluster power 问题、log-log 模型误设、K=3 限制——这些是论文 empirical claim 的 statistical foundation 问题\n- **R2 的核心贡献**：识别了 novelty predictability、BFT 概念错位、Related Work 不足——这些是论文 positioning 和 framing 的结构性问题\n\n两类问题叠加后的判断：论文的 empirical machinery 有值得肯定的地方（大规模实验、多种 correction 方法的意识），但核心 claim 在 conceptual 和 statistical 两个维度上都不够 robust。Findings 是恰当的推荐。\n\n最终评分不变：**Overall 3.0 / 5 (Findings)**。\n",
  "reviewer_id": "2",
  "project": "cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# R2 逐条回应 R1 完整审稿意见\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: 聚类数不足导致核心发现统计可信度存疑**\n\n完全同意。这是本轮审稿中最重要的方法论发现之一。补充两点：\n\n(1) 论文实际上使用了三种 non-independence correction（Table 3, p.6）：clustered SE、mixed effects、wild cluster bootstrap。三种方法在 K_eff 上的结果分别是 0/12、1/12、0/12 显著——看似一致地指向 \"K_eff 无效\"。但 R1 正确指出，这三种方法在 few-cluster 情景下都存在 conservative bias：clustered SE 的 t-distribution 自由度不足、mixed effects 的 random intercept 估计在 15 groups 下不稳定、wild cluster bootstrap 在 cluster 数 <20 时 rejection rate 偏低（Cameron et al., 2008; Webb, 2023）。三种方法的 \"一致性\" 可能是同一个 artifact 的三种表现形式，而非独立证据。\n\n(2) 与我的 W1（r=0.70 confound）形成 compound effect：multicollinearity 膨胀 K_eff 系数的 variance，few-cluster correction 进一步膨胀 standard error。双重膨胀下 K_eff 几乎不可能达到显著性。这使得 \"K_eff collapses\" 在统计上是 underdetermined 的。\n\n**[AGREE with nuance] R1-N2: Log-log OLS 对有界响应变量的模型误设**\n\n同意 beta regression 或 fractional logit 是 ASR ∈ [0,1] 的更恰当模型。但需要指出：\n\n(a) 论文使用 log-log 而非 logit 变换有其理由——log-log 变换在 ASR 远离 0 和 1 时与 beta regression 的 log-link 近似等价。如果 ASR 的分布集中在中间范围（如 0.1-0.7），模型误设的影响可能较小。论文未报告 ASR 的分布，这是一个遗漏。\n\n(b) ε = 10⁻⁹ 的问题确实严重。论文 Equation 2 (p.5) 写的是 log(ASR + ε)，但从论文描述来看 ε 可能接近于 \"handle zero\" 的技术处理。如果某些 panel-condition 的 ASR 恰好为 0（完全未被攻破），log(0 + 10⁻⁹) ≈ -20.7 会成为极端 outlier，严重拉动回归系数。这需要 sensitivity analysis（如 ε = 10⁻³, 10⁻⁶, 10⁻⁹ 的对比）。\n\n(c) R1 说 \"预测值可能超出 [0,1]\" 是正确的，但论文的目的是回归分析（理解 predictor 的贡献），不是预测。OLS 系数的解释性在 well-specified 条件下仍有意义，即使预测值越界。所以这个 concern 的严重程度取决于论文是否用回归做 prediction（看起来没有）。\n\n综合判断：beta regression robustness check 和 ε sensitivity analysis 应该做，但我认为这是 should-fix 而非 must-fix——如果 ASR 分布合理且 ε 敏感性不大，主要结论可能不变。\n\n**[AGREE] R1-N3: 实验范围不足以支撑一般性 claim**\n\n同意，且与我的 W2（benchmark 范围窄）直接对应。具体补充：\n\n(a) **K=3 固定是最大的限制**。论文的 Theorem 1 适用于任意 K，但所有实验仅在 K=3 下进行。K=3 意味着 majority vote 只需攻破 2/3 个 judge，攻击者的任务相对简单。当 K=5 或 K=7 时，diversity 的保护效果可能显著不同——因为攻击者需要攻破更多 judges，这时 panel 组成的异质性会提供更多 \"independent failure modes\"。论文的 \"diversity doesn't matter\" 结论可能仅在 K=3 下成立。Section 6 (Analysis, p.8) 和 Appendix 均未讨论 K 的影响。\n\n(b) **Oracle adversary 是一个极端假设**。论文在 Appendix C.4 (p.10) 确实讨论了 oracle adversary 的局限性，承认 \"this upper bound on adversarial capability, not a realistic deployment scenario\"。但正文的 title 和 claims 没有加 \"under oracle adversary\" 的限定。如果在 partial-knowledge 下（adversary 不知道 panel 具体组成），diversity 可能重新变得重要——因为 adversary 无法精准定位最弱 judge。论文在 Introduction (p.1) 提到 \"partial-knowledge adversary\" 作为 contribution 之一，但正文没有相应实验。\n\n(c) 仅 MCQ 的问题我已在 R2-W2 中详细讨论，不重复。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W1: r=0.70 混淆未充分解决**\n\n完全同意，这与我的 R2-W1 一致。补充一点：R1 建议 \"增加 within-tier 实验\"，论文实际上在 Section 6 (p.8) 提到了 within-tier analysis：\"family membership is not a significant predictor of panel vulnerability (η = 0.179 on MMLU, p = 0.385 on ARC)\"。但这是在 family 层面的分析，不是在 capability tier 层面。论文应该进一步在同一 tier 内（如只用 frontier-tier 模型组 panel）检验 η_max 和 K_eff 的关系，以在控制 capability 的条件下测试 diversity 的独立贡献。\n\n**[AGREE] R1-W2: Related Work 过于简略**\n\n完全同意，这正是我的 R2-N1 的核心内容。我将此问题定为 critical 而非 warning，因为 Related Work 的不足不仅是展示问题，还直接影响了论文能否建立 novelty positioning。R1 补充的遗漏（multi-agent debate/evaluation frameworks, LLM calibration 文献）是有效的补充——我的 N1 中列出了 ensemble diversity theory、crowdsourcing aggregation、LLM-as-judge frameworks、adversarial ensemble robustness 四个缺失领域。两位 Reviewer 的遗漏列表互补，总计 6-7 个需要补充讨论的领域。\n\n**[AGREE] R1-W3: Theorem 1 理论深度有限**\n\n同意，与我的 R2-N3（BFT 类比概念错位）互补。R1 的表述更 precise：\"在 oracle adversary 假设下几乎是定义性的\"——这正是我想表达的意思。Theorem 1 说的是 \"替换更弱的 judge 使 panel 更弱\"，在 oracle adversary 下几乎是 tautological。R1 建议 \"推导 partial-knowledge 下更深结果\" 是一个好方向——如果能证明在 partial-knowledge adversary 下 diversity 的保护效果有 formal guarantee（类似于 BFT 的 f < n/3），那将是一个真正有深度的理论贡献。\n\n**[AGREE with nuance] R1-W4: 攻击实现细节不足以完全复现**\n\n同意方向，但需修正 \"仅一句描述\" 的说法。如我之前指出，Table 5 (Appendix E, p.12) 提供了 6 种攻击的 representative prompt templates，每种约 2-4 行。这不是 \"一句描述\"，但确实不够 fully reproducible——缺少 (1) 攻击如何与具体 benchmark item 结合的 programmatic pipeline，(2) judge system prompt 的格式，(3) 攻击成功的判定标准（judge 输出的 parsing 规则）。\n\n**[AGREE] R1-W5: 模型版本标识不够精确**\n\n同意。Table 1 (p.4) 列出了模型名称（如 \"gpt-4o\", \"gpt-3.5-turbo\"）但 OpenAI 模型经常更新，无 snapshot date 或 version hash 的话无法准确复现。不过这在当前 LLM 研究中是一个 community-wide 的问题，不应对本文格外惩罚——很多 EMNLP 接收论文也有同样的问题。\n\n---\n\n## 小问题\n\n对 R1 列出的 4 个小问题均无异议。补充一点：R1 提到 \"§5.4 'clean 6:6 split' 需更精确计数\"，我在首轮审稿中注意到 Section 5.4 的描述是 targeted vs shared-bias 的 split，但论文在不同位置对这个 split 的数字描述不一致（Abstract 说 \"10:8\"，正文 Section 5.4 可能说 \"6:6\"），需要作者澄清。\n\n---\n\n## 总结\n\nR1 和 R2 的 critiques 高度互补：\n- **R1 的核心贡献**：识别了 15-cluster power 问题、log-log 模型误设、K=3 限制——这些是论文 empirical claim 的 statistical foundation 问题\n- **R2 的核心贡献**：识别了 novelty predictability、BFT 概念错位、Related Work 不足——这些是论文 positioning 和 framing 的结构性问题\n\n两类问题叠加后的判断：论文的 empirical machinery 有值得肯定的地方（大规模实验、多种 correction 方法的意识），但核心 claim 在 conceptual 和 statistical 两个维度上都不够 robust。Findings 是恰当的推荐。\n\n最终评分不变：**Overall 3.0 / 5 (Findings)**。\n",
    "reviewer_id": "2",
    "project": "cert_manip_resist_eval"
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-22T23:05:12.257910+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3880
}
```

</details>

---


### Assistant

_source line 74 · 2026-05-22T23:05:17.113698+00:00_

已提交对 R1 完整审稿意见的逐条回应。对 R1 的 3 个 Must-Fix 全部 AGREE（N2 有 nuance），5 个 Should-Fix 全部 AGREE（W4、W5 有 nuance）。两位 Reviewer 最终收敛于 Overall 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2"
}
```

</details>

---


## Round 5

## Round 5

80 recorded events


### User

_source line 75 · 2026-05-23T06:17:46.953975+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性与完整性**审查。

## 论文信息
- 标题：The Shifting Bottleneck: How Panel Size Modulates Adversarial Vulnerability in LLM Judge Panels
- 论文路径：projects/cert_manip_resist_eval/docs/paper/main.tex
- PDF：projects/cert_manip_resist_eval/artifacts/review_round_1/submitted.pdf

## Venue 要求（EMNLP 2026 via ARR）
- ARR May 2026 cycle，提交截止 2026-05-25 AoE
- Long paper：正文严格 8 页，参考文献不限
- Limitations 章节必须有，不计入页数（但不能包含过多额外内容）
- ACL 模板（\usepackage[review]{acl}），double-blind
- ARR Responsible NLP Checklist 在 OpenReview submission form 中填写，不在论文 PDF 中
- Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle

## 你的审查侧重
请重点审查以下方面：

1. **贡献新颖性**：
   - "Panel-size-dependent vulnerability regime transition" 是否是真正的新发现，还是 majority voting 算术的 trivial 推论？
   - "diversity is harmful" 的 claim 是否过度解读？K_eff positive coefficient 在 aggregate 层面是否掩盖了 GAM 发现的 attack-type-dependent 方向？
   - 相对于 Almasoud et al. (2026) 的 security systematization，本文的增量贡献是什么？
   - 与 ensemble diversity theory (Krogh & Vedral 1995, Brown 2005) 相比有何本质新意？

2. **相关工作覆盖**：
   - 是否遗漏重要相关工作？特别是：
     - LLM judge aggregation 方面的最新工作
     - Adversarial robustness of ensembles（vision 领域的迁移）
     - Information-theoretic evaluation security
     - Condorcet Jury Theorem 的现代分析
   - 引用是否真实？是否有幻觉引用？（特别关注 2025-2026 年的引用）

3. **写作质量**：
   - Abstract 是否过于数字密集？核心 message 是否清晰？
   - Introduction 的 narrative arc 是否有说服力？
   - 各节之间的逻辑流是否自然？
   - Analysis section 是否过短（只有 1 段）？
   - Conclusion 是否过于简短？

4. **格式合规**：
   - 正文是否严格在 8 页以内？
   - 是否使用了正确的 ACL 模板？
   - 匿名性是否满足 double-blind 要求？
   - Figure/Table 编号和引用是否一致？
   - Limitations section 是否存在且格式正确？
   - 是否只有一个 Limitations section（正文中），appendix 中没有额外的？

5. **呈现清晰度**：
   - 核心发现是否容易被读者抓住？
   - Table/Figure 是否自包含（caption 足够理解）？
   - 术语定义是否一致？（K_eff, η_max, ASR 等）
   - 读者是否能从 abstract+intro 就理解论文的核心 claim？

6. **Limitations 评估**：
   - 现有 Limitations 是否诚实、完整？
   - 是否有未提及的重要局限？

7. **Ethical considerations**：
   - 研究对抗攻击是否有 dual-use concern？
   - 是否需要 broader impact statement？

请按 EMNLP 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses（Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（用 EMNLP 评分标准）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-23T06:17:58.278556+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-23T06:17:59.786840+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/review_reviewer_2_38d341a1.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1508
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-23T06:17:59.787294+00:00_

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
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
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

_source line 79 · 2026-05-23T06:17:59.837812+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-23T06:18:07.430589+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 81 · 2026-05-23T06:18:09.791536+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/submitted.pdf",
  "project": "cert_manip_resist_eval",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/submitted.pdf",
    "project": "cert_manip_resist_eval",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-23T06:18:10.499009+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-23T06:18:16.643877+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

I found information about ACL Rolling Review (ARR) 2026 reviewer guidelines and review form criteria. Here's what I found:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.

##
…[truncated 990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9213
}
```

</details>

---


### Tool result

_source line 84 · 2026-05-23T06:18:18.002375+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.7}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 551.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 384.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1
…[truncated 482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8210
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-23T06:18:18.002964+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb,amsthm}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{definition}{Definition}
17	\newtheorem{proposition}{Proposition}
18	
19	\title{The Shifting Bottleneck: How Panel Size Modulates\\Adversarial Vulnerability in LLM Judge Panels}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	Multi-judge LLM evaluation panels are widely assumed to benefit from judge diversity, drawing inspiration from fault tolerance in distributed systems. We decompose panel vulnerability into individual judge weakness ($\eta_{\max}$) and structural diversity ($K_{\mathrm{eff}}$) across 15 models, 6 attack types, 2 benchmarks, and panel sizes $K \in \{3, 5, 7\}$ (455 to 6{,}435 panels). We discover a panel-size-dependent vulnerability regime transition: at $K{=}3$, individual weakness dominates ($\eta_{\max}$ significant in 5/12 conditions under wild cluster bootstrap; $K_{\mathrm{eff}}$ 1/12), but at $K{\geq}5$ this completely reverses, with $K_{\mathrm{eff}}$ becoming the dominant predictor (7/12 at $K{=}5$; 5/12 at $K{=}7$) while $\eta_{\max}$ collapses to 0/12. In both regimes, the $K_{\mathrm{eff}}$ coefficient is positive: diversity increases vulnerability because independent judges can be targeted individually by an adaptive adversary. Generalized additive model analysis reveals that this aggregate pattern masks directional structure by attack mechanism: diversity is harmful for targeted attacks and predominantly protective for shared-bias attacks. Aggregation rule choice further modulates vulnerability, with Bayesian calibration reversing $K_{\mathrm{eff}}$'s direction. The defense strategy must match the p
…[truncated 2218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7503
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-23T06:18:26.181602+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all dimensions, rating scales, and descriptions. Include: Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions with their full rating descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all dimensions, rating scales, and descriptions. Include: Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions with their full rating descriptions."
  }
}
```

</details>

---


### Tool call

_source line 87 · 2026-05-23T06:18:28.955970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-23T06:18:29.006660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-23T06:18:33.037894+00:00_

# ACL Rolling Review Form - Complete Dimensions

## Core Review Dimensions

**Soundness** (5-point scale)
- 5 = "Excellent: This study is one of the most thorough I have seen"
- 4 = Strong with sufficient support; minor experiments optional
- 3 = Acceptable; main claims supported with minor gaps
- 2 = Poor; main claims lack sufficient support
- 1 = Major Issues; insufficiently thorough for publication

**Excitement** (5-point scale)
- 5 = "Highly Exciting: I would recommend this paper to others"
- 4 = Exciting; would mention to colleagues
- 3 = Interesting; might attend presentation
- 2 = Potentially Interesting; limited personal resonance
- 1 = Not Exciting; lacks relevance to computational linguistics

**Overall Assessment** (5-point scale)
- 5 = Consider for Award (top 2.5%)
- 4 = Conference acceptance recommended
- 3.5 = Borderline Conference
- 3 = Findings track acceptance
- 2 = Substantial revisions needed
- 1 = Do not resubmit

## Additional Dimensions

**Reproducibility** (5-point scale)
- 5 = Results easily reproducible
- 3 = Reproducible with difficulty; underspecified parameters
- 1 = Results not reproducible

**Datasets** (5-point scale)
- 5 = Enabling; affects research direction choices
- 3 = Potentially useful to others
- 1 = No usable datasets

**Software** (5-point scale)
- 5 = Enabling; affects project selection
- 2 = Documentary value for replication
- 1 = No usable software

**Author Identity Knowledge** (5-point scale)
- 5 = Know/guess author from double-blind violation
- 1 = No educated guess about identity

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6856
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-23T06:18:33.039159+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4083
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-23T06:18:33.041302+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4034
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-23T06:18:33.593106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 93 · 2026-05-23T06:18:33.894390+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 94 · 2026-05-23T06:18:34.548918+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-23T06:18:34.800752+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-23T06:18:41.880715+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-23T06:18:42.285866+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-23T06:18:42.286432+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 99 · 2026-05-23T06:18:42.787656+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 100 · 2026-05-23T06:18:43.694799+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-23T06:18:43.697958+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-23T06:18:43.698449+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 103 · 2026-05-23T06:18:44.199788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 104 · 2026-05-23T06:18:44.603540+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 105 · 2026-05-23T06:18:44.603994+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 106 · 2026-05-23T06:18:45.058209+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-23T06:18:45.460113+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-23T06:18:53.135752+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/submitted.pdf",
  "project": "cert_manip_resist_eval",
  "pages": "11-13",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/submitted.pdf",
    "project": "cert_manip_resist_eval",
    "pages": "11-13",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-23T06:18:53.687520+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 418.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.2}], \"total_pages\": 13, \"rendered_pages\": 3, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 551
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-23T06:18:53.738161+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-23T06:18:53.838976+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix_attacks.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-23T06:18:57.958227+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 113 · 2026-05-23T06:18:58.410300+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 114 · 2026-05-23T06:18:59.315333+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-23T06:18:59.317718+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-23T06:18:59.318241+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 117 · 2026-05-23T06:18:59.820269+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 118 · 2026-05-23T06:19:00.273431+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-23T06:19:00.273861+00:00_

1	\section{Introduction}
2	
3	Multi-judge panels have emerged as the dominant defense against bias and manipulation in LLM-based evaluation. After \citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work exposed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, drawing inspiration from Byzantine fault tolerance (BFT), where majority voting among independent nodes tolerates faulty responses \citep{lamport1982byzantine,castro1999practical}. A recent systematization of LLM-judge security reports that 7-model committees reduce attack success rates from 50--68\% to 10--19\% \citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation.
4	
5	Yet the evidence for diversity as a causal defense is weaker than it appears. The observed ASR reduction in multi-judge panels conflates two distinct factors: the diversity of the panel (how independently judges respond to attacks) and the individual robustness of its strongest members. No existing work disentangles these contributions across panel sizes. The BFT settings differ from the evaluation setting in a critical way: BFT adversaries control faulty nodes internally, whereas evaluation adversaries manipulate inputs externally. The strong data-processing inequality (SDPI) bounds joint failure probability but assumes non-adaptive faults and does not model adversaries who observe panel composition \citep{schneier2000secrets}.
6	
7	In our experiments, we discover a panel-size-dependent vulnerability regime transition. At $K{=}3$, panel vulnerability is dominated by individual judge weakness ($\eta_{\max}$), not diversity ($K_{\mathrm{eff}}$): the weakest link is the bottleneck. At $K{\geq}5$, this completely reverses: $K_{\mathrm{eff}}$ becomes the dominant predictor whil
…[truncated 2798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-23T06:19:00.274071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-23T06:19:01.231864+00:00_

1	\section{Related Work}
2	
3	\paragraph{LLM-as-Judge and Multi-Judge Evaluation.}
4	LLM judges gained traction after \citet{zheng2023judging} established them as scalable alternatives to human annotation. \citet{wang2023fair} documented systematic failure modes (position bias, verbosity preferences, sycophancy), motivating multi-judge panels. The idea of aggregating noisy annotators traces back to \citet{dawid1979maximum}; LLM judge panels inherit this structure but introduce correlated failure modes absent in classical settings. \citet{verga2024replacing} showed diverse panels can match single large judges, and \citet{panickssery2024llm} identified self-preference bias as a mechanism for within-family correlations. \citet{li2023alpacaeval} operationalized multi-judge comparison through automated win-rate estimation; \citet{ye2024flask} decomposed judgment into fine-grained skill dimensions. These frameworks assume benign conditions; we test whether aggregation benefits survive adversarial manipulation. \citet{almasoud2026security} reported that 7-model committees reduce ASR from 50--68\% to 10--19\%, but did not disentangle diversity from individual robustness.
5	
6	\paragraph{Condorcet Jury Theorem.}
7	\citet{condorcet1785essai} proved that majority voting accuracy converges to 1 when per-voter accuracy exceeds 0.5. The theorem rests on voter independence, which correlated LLM outputs violate. Our results instantiate the CJT failure mode: when adaptive attacks push judges below the critical threshold, panel expansion amplifies error.
8	
9	\paragraph{Ensemble Diversity Theory.}
10	\citet{krogh1995neural} proved that ensemble error equals average member error minus a diversity term; \citet{brown2005managing} showed diversity reduces error only when members maintain sufficiently low bias. In our setting, weaker judges introduce bias large enough to offset diversity benefits. \citet{kuncheva2003measures} found that no pairwise diversity measure reliably predicted ens
…[truncated 2205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-23T06:19:01.232297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-23T06:19:01.385073+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	The regime transition reflects majority-threshold arithmetic: at $K{=}3$, one weak judge flips the panel, making $\eta_{\max}$ the binding constraint; at $K{\geq}5$, the adversary must flip multiple judges, shifting the bottleneck to panel independence ($K_{\mathrm{eff}}$). GAM analysis reveals that the aggregate positive $K_{\mathrm{eff}}$ coefficient masks a 6:6 directional split at $K{=}3$ by attack mechanism, largely preserved at $K{=}5$ (11/12 consistent; Appendix~\ref{app:bft_reversal}). The $r{=}0.70$ $K_{\mathrm{eff}}$--$\eta_{\max}$ correlation raises a confound concern, but VIF averages 3.0 (10/12 below 5) and $\eta_{\max}$ retains partial $r{=}0.31$ vs.\ $K_{\mathrm{eff}}$'s 0.12 (Appendix~\ref{app:diversity_capability}). At $K{=}3$, aggregation modulates both channels: Bayesian calibration reverses $K_{\mathrm{eff}}$'s direction, and robustness-first selection achieves lowest ASR in 12/12 conditions (Appendix~\ref{app:panel_selection}). Our oracle adversary is an upper bound; partial-knowledge attackers would achieve lower ASR (Appendix~\ref{app:oracle}).
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-23T06:19:01.537214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-23T06:19:01.587821+00:00_

1	\section{Conclusion}
2	
3	The dominant vulnerability factor in LLM judge panels transitions with panel size: at $K{=}3$, $\eta_{\max}$ dominates (bootstrap 5/12, $K_{\mathrm{eff}}$ 1/12, MDE${=}0.14$); at $K{\geq}5$, this reverses ($K_{\mathrm{eff}}$ 7/12 at $K{=}5$, 5/12 at $K{=}7$; $\eta_{\max}$ 0/12). Diversity is harmful in both regimes: independent judges can be individually targeted. The adaptive-vs-random contrast confirms this is genuine under random faults ($R^2 = 0.73$--$0.81$) but not under adaptive attack. Defense must be regime-dependent: small panels require robustness screening; larger panels require minimizing independence. At $K{=}3$, Bayesian calibration reverses $K_{\mathrm{eff}}$'s direction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-23T06:19:10.690150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-23T06:19:11.693171+00:00_

1	\section{Threat Model and Problem Formulation}
2	\label{sec:threat_model}
3	
4	A \emph{panel} $\mathcal{P} = \{J_1, \ldots, J_K\}$ consists of $K$ judges (with $K$ odd) that evaluate a candidate text via majority vote: the text is accepted if at least $t = \lceil K/2 \rceil$ judges approve it. Under an attack $a$, each judge $J_j$ is compromised with marginal failure probability $\eta_j(a) = \Pr(X_j^a = 1)$, where $X_j^a \in \{0,1\}$ denotes the failure indicator. We write $\eta_{\max} = \max_j \eta_j$ for the vulnerability of the weakest judge. The \emph{panel attack success rate} is $\mathrm{ASR}(\mathcal{P}, a) = \Pr\!\bigl(\sum_{j=1}^K X_j^a \geq t\bigr)$.
5	
6	To quantify diversity, we define the \emph{effective independence} $K_{\mathrm{eff}}$ directly from pairwise mutual information among judges:
7	\begin{equation}
8	\label{eq:keff}
9	K_{\mathrm{eff}} = \frac{1}{K}\sum_{i=1}^{K} \Bigl[1 + \sum_{j \neq i} \exp\!\bigl(-2 \cdot \mathrm{MI}(i,j)\bigr)\Bigr].
10	\end{equation}
11	This formulation computes effective independence from pairwise MI estimates without matrix decomposition, and is more stable for small panels ($K{=}3$). It ranges from $K_{\mathrm{eff}} \approx K$ when judges are nearly independent ($\mathrm{MI} \to 0$) to $K_{\mathrm{eff}} \approx 1$ when judges are highly correlated ($\mathrm{MI} \to \infty$). Under the strong data-processing inequality (SDPI), the joint vulnerability satisfies $\eta_{\mathrm{joint}} \leq \min(1,\; K_{\mathrm{eff}} \cdot \eta_{\max})$, suggesting that diversity should help, but this bound assumes non-adaptive faults.
12	
13	\begin{definition}[Adaptive Adversary]
14	\label{def:adversary}
15	A \emph{full-knowledge (oracle) adaptive adversary} has complete knowledge of the panel composition $\mathcal{P}$, the per-judge vulnerability profiles $\{\eta_j(\cdot)\}_{j=1}^K$, and the inter-judge correlation structure. It selects the attack $a^* = \arg\max_{a \in \mathcal{A}} \mathrm{ASR}(\mathcal{P}, a)$ to maximize the panel
…[truncated 2358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-23T06:19:11.693743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-23T06:19:12.195198+00:00_

1	\section{Experimental Methodology}
2	\label{sec:experiments}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/fig_framework.pdf}
7	\caption{Overview of our evaluation framework. Given $N$ candidate LLM judges, we construct $K$-judge panels (\S\ref{sec:experiments}), subject them to six adversarial attack types (\S\ref{sec:threat_model}), and assess vulnerability through two complementary metrics: $\eta_{\max}$ (weakest-link individual susceptibility) and $K_{\text{eff}}$ (effective independent channels via mutual information). Panel decisions are aggregated through four methods of increasing sophistication (\S\ref{sec:aggregation}).}
8	\label{fig:framework}
9	\end{figure*}
10	
11	\subsection{Models and Panel Construction}
12	
13	We select 15 LLM judges spanning 6 provider families and 3 capability tiers, listed in Table~\ref{tab:models}. Nine models are accessed via the OpenRouter API; six open-weight models are served locally using vLLM~0.21.0 with AWQ INT4 quantization on an NVIDIA RTX~6000 Ada (48\,GB). API models are assigned to \emph{frontier}, \emph{mid-tier}, or \emph{lightweight} tiers following the provider capability classification; all six local models fall into the lightweight tier, as INT4 quantization substantially reduces judge accuracy on the pairwise judgment task (Table~\ref{tab:models}). We study three panel sizes $K \in \{3, 5, 7\}$ (all odd, majority-vote threshold $t = \lceil K/2 \rceil$). Exhaustive enumeration yields $\binom{15}{3} = 455$ panels at $K{=}3$, $\binom{15}{5} = 3{,}003$ at $K{=}5$, and $\binom{15}{7} = 6{,}435$ at $K{=}7$, covering every combination of families and tiers. Each panel evaluates all benchmark items under all attack types, producing a complete panel $\times$ item $\times$ attack tensor. The primary analysis uses $K{=}3$; \S\ref{sec:cross_k} extends to larger panels.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\begin{tabular}{lllccc}
19	\toprule
20	\textbf{Model} & \textbf{Fam
…[truncated 8299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-23T06:19:12.195788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-23T06:19:12.546951+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Weakest-Link Dominance at \texorpdfstring{$K{=}3$}{K=3}}
5	\label{sec:dominance}
6	
7	Table~\ref{tab:dominance} reports the log-log OLS regression (Equation~\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\ref{tab:models}).
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\begin{tabular}{llccc}
13	\toprule
14	\textbf{Bench.} & \textbf{Attack} & $\boldsymbol{\eta_{\max}}$ & $\boldsymbol{K_{\mathrm{eff}}}$ & \textbf{Dom.} \\
15	\midrule
16	MMLU & Prompt inj.    & $+^{*}$ & $+^{*}$ & Co \\
17	MMLU & Sycophancy     & $+^{*}$ & $+^{*}$ & Co \\
18	MMLU & Score manip.   & $+^{*}$ & n.s.    & $\eta$ \\
19	MMLU & Verbosity      & $+^{*}$ & $+^{*}$ & Co \\
20	MMLU & Position bias  & $+^{*}$ & n.s.    & $\eta$ \\
21	MMLU & Authority bias & $+^{*}$ & n.s.    & $\eta$ \\
22	\addlinespace
23	ARC  & Prompt inj.    & $+^{*}$ & $+^{*}$ & Co \\
24	ARC  & Sycophancy     & $+^{*}$ & $-^{*}$ & Co \\
25	ARC  & Score manip.   & $+^{*}$ & $+^{*}$ & Co \\
26	ARC  & Verbosity      & $+^{*}$ & n.s.    & $\eta$ \\
27	ARC  & Position bias  & n.s.    & $+^{*}$ & $K$ \\
28	ARC  & Authority bias & $+^{*}$ & $+^{*}$ & Co \\
29	\bottomrule
30	\end{tabular}
31	\caption{Standardized regression coefficients for $\eta_{\max}$ and $K_{\mathrm{eff}}$ across 12 conditions (455 panels, log-log OLS). $+^{*}$/$-^{*}$: FDR-significant positive/negative (Benjamini--Hochberg, $q < 0.05$); n.s.: not significant. Dom.\ column: $\eta$ = $\eta_{\max}$ sole dominant, $K$ = $K_{\mathrm{eff}}$ sole dominant, Co = co-dominant \citep{budescu1993dominance}.}
32	\label{tab:dominance}
33	\end{table}
34	
35	The weakest-link vulnerability $\eta_{\max}$ reaches FDR significance in 11 of 12 conditions; the sole exception is ARC $\times$ position bias ($p = 0.909$). This near-universal significance is consistent with Theorem~\ref{thm:monotonicity}: the most vulnerable member is the primary channel through which adaptive att
…[truncated 9676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-23T06:19:12.547378+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-23T06:19:12.600956+00:00_

1	\appendix
2	
3	\section{Proof of Theorem~\ref{thm:monotonicity}}
4	\label{app:proof}
5	
6	The replaced judge $J_K'$ is \emph{pivotal} exactly when $t{-}1$ of the remaining $K{-}1$ judges have already failed. Formally, let $S = \sum_{j=1}^{K-1} X_j^a$ denote the number of failures among the shared judges. The panel fails if and only if the $K$-th judge also fails when $S = t{-}1$, or when $S \geq t$ regardless of the $K$-th judge:
7	\begin{align}
8	\mathrm{ASR}(\mathcal{P}, a) &= \Pr(S \geq t) + \Pr(S = t{-}1) \cdot \Pr(X_K^a {=} 1 \mid S = t{-}1).
9	\end{align}
10	Since $\Pr(X_{K'}^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K}) \geq \Pr(X_K^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K})$ for all attacks $a$ and realizations $\mathbf{x}_{-K}$ (by hypothesis), the second term is weakly larger for $\mathcal{P}'$ than for $\mathcal{P}$ under every attack. Taking the supremum over attacks preserves the inequality: $\mathrm{ASR}^*(\mathcal{P}') \geq \mathrm{ASR}^*(\mathcal{P})$. The result holds under arbitrary inter-judge correlations and any attack space $\mathcal{A}$.
11	
12	\section{Robustness Correction Methods}
13	\label{app:robustness_methods}
14	
15	The 455 panels are constructed combinatorially from 15 shared judges: each judge appears in $\binom{14}{2} = 91$ panels, inducing correlated residuals across panel-level observations. Standard OLS assumes independent errors, potentially inflating significance. We apply three corrections.
16	
17	\paragraph{Clustered Standard Errors.} Because each panel of $K{=}3$ judges does not map to a single cluster, we perform three separate one-way clusterings (one for each judge position in the ordered panel tuple) using CR1 bias-corrected sandwich estimators (13 clusters per position). The reported standard error for each coefficient is the maximum across the three clusterings, yielding the most conservative inference.
18	
19	\paragraph{Mixed Effects.} For each of the three judge positions, we fit a linear mixed-effec
…[truncated 7242 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-23T06:19:20.083820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix_attacks.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix_attacks.tex"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-23T06:19:20.184602+00:00_

1	\section{Attack Prompt Templates}
2	\label{app:attacks}
3	
4	Table~\ref{tab:attack-templates} lists the six manipulation strategies used in our experiments. Each attack modifies the ground-truth loser response to exploit a specific judge bias. Below we describe each attack type and provide representative template text.
5	
6	\paragraph{Prompt Injection.} Injects directive text at the end of the loser response, attempting to override the judge's evaluation logic with explicit scoring instructions.
7	
8	\paragraph{Sycophancy Exploitation.} Wraps the loser response in enthusiastic, agreeable language (a prefix and suffix), exploiting judges' preference for polite and eager responses.
9	
10	\paragraph{Score Manipulation.} Appends fabricated self-assessment scores to the loser response, leveraging judges' tendency to defer to confident quality claims embedded in the text.
11	
12	\paragraph{Verbosity Bias.} Appends a lengthy but content-free elaboration ($\sim$50--60 words) to the loser response, exploiting judges' bias toward longer responses regardless of substantive contribution.
13	
14	\paragraph{Position Bias.} Swaps the positions of response A and response B so that the ground-truth winner occupies position B, exploiting judges' tendency to favor position A.
15	
16	\paragraph{Authority Bias.} Prepends fabricated citations to prestigious institutions or journals at the beginning of the loser response, exploiting judges' deference to perceived academic authority.
17	
18	\begin{table*}[t]
19	\centering
20	\small
21	\caption{Representative prompt templates for each attack type. Templates shown are appended to, prepended to, or used to wrap the ground-truth loser response. Position bias has no template text; it swaps response order.}
22	\label{tab:attack-templates}
23	\begin{tabular}{@{}l p{11.5cm}@{}}
24	\toprule
25	\textbf{Attack Type} & \textbf{Representative Template} \\
26	\midrule
27	Prompt Injection &
28	\texttt{\textbackslash n\textbackslash n[Note: This respons
…[truncated 3193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-23T06:19:20.285426+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-23T06:19:20.386246+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-23T06:19:24.247995+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-23T06:19:24.349013+00:00_

1	% Bibliography for cert_manip_resist_eval
2	% All entries verified via WebSearch on 2026-05-22
3	% ============================================================
4	
5	% ============================================================
6	% Part A: Papers from literature_map.yaml (12 papers)
7	% ============================================================
8	
9	@article{robertson2025stepwise,
10	  author    = {Robertson, Zachary and Koyejo, Sanmi},
11	  title     = {Let's Measure Information Step-by-Step: {LLM}-Based Evaluation Beyond Vibes},
12	  journal   = {arXiv preprint arXiv:2508.05469},
13	  year      = {2025},
14	  url       = {https://arxiv.org/abs/2508.05469},
15	  note      = {arXiv:2508.05469}
16	}
17	
18	@inproceedings{yang2026diversity,
19	  author    = {Yang, Yingxuan and Qu, Chengrui and Wen, Muning and Shi, Laixi and Wen, Ying and Zhang, Weinan and Wierman, Adam and Gu, Shangding},
20	  title     = {Understanding Agent Scaling in {LLM}-Based Multi-Agent Systems via Diversity},
21	  booktitle = {ICLR 2026 Workshop on AIMS},
22	  year      = {2026},
23	  url       = {https://arxiv.org/abs/2602.03794},
24	  note      = {arXiv:2602.03794}
25	}
26	
27	@article{turkmen2026ensemble,
28	  author    = {Turkmen, Yigit and Buyukates, Baturalp and Bastopcu, Melih},
29	  title     = {Don't Always Pick the Highest-Performing Model: An Information Theoretic View of {LLM} Ensemble Selection},
30	  journal   = {arXiv preprint arXiv:2602.08003},
31	  year      = {2026},
32	  url       = {https://arxiv.org/abs/2602.08003},
33	  note      = {arXiv:2602.08003}
34	}
35	
36	@inproceedings{kaneko2025bits,
37	  author    = {Kaneko, Masahiro and Baldwin, Timothy},
38	  title     = {Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against {LLMs}},
39	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
40	  year      = {2025},
41	  url       = {https://arxiv.org/abs/2510.17000},
42	  note      = {arXiv:2510.17000. Spotlight}
43	}
44	

…[truncated 15799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-23T06:20:43.613469+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2603.29403 Almasoud \"Security in LLM-as-a-Judge\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2603.29403 Almasoud \"Security in LLM-as-a-Judge\""
  }
}
```

</details>

---


### Tool call

_source line 141 · 2026-05-23T06:20:44.115731+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2604.07650 Kuai \"How Independent are Large Language Models\" behavioral entanglement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2604.07650 Kuai \"How Independent are Large Language Models\" behavioral entanglement"
  }
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-23T06:20:44.968812+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2602.03794 Yang \"Understanding Agent Scaling\" diversity LLM multi-agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2602.03794 Yang \"Understanding Agent Scaling\" diversity LLM multi-agent"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-23T06:20:48.886364+00:00_

Web search results for query: "arXiv 2604.07650 Kuai "How Independent are Large Language Models" behavioral entanglement"

Links: [{"title":"[2604.07650] How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/abs/2604.07650"},{"title":"[2604.07650v1] How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/abs/2604.07650v1"},{"title":"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/html/2604.07650"},{"title":"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/pdf/2604.07650"},{"title":"Framing Effects in Independent-Agent Large Language Models: A Cross-Family Behavioral Analysis","url":"https://arxiv.org/pdf/2603.19282"}]

I found the paper you're looking for. Here's what it contains:

The paper addresses a critical question about whether seemingly diverse large language models are truly independent, noting that shared pretraining data, distillation, and alignment pipelines can induce hidden behavioral dependencies, or "latent entanglement," that undermine multi-model systems such as LLM-as-a-judge pipelines and ensemble verification.

In practice, this behavioral entanglement manifests as correlated reasoning patterns and synchronized failures, where apparent agreement reflects shared error modes rather than independent validation.

To address this, the researchers developed a statistical framework for auditing behavioral entanglement among black-box LLMs, introducing a multi-resolution hierarchy that characterizes the joint failure manifold through two information-theoretic metrics: a Difficulty-Weighted Behavioral Entangle
…[truncated 636 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4770
}
```

</details>

---


### Tool result

_source line 144 · 2026-05-23T06:20:50.391806+00:00_

Web search results for query: "arXiv 2603.29403 Almasoud "Security in LLM-as-a-Judge""

Links: [{"title":"[2603.29403] Security in LLM-as-a-Judge: A Comprehensive SoK","url":"https://arxiv.org/abs/2603.29403"},{"title":"SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK","url":"https://arxiv.org/pdf/2603.29403"},{"title":"Prompt Attack Detection with LLM-as-a-Judge and Mixture-of-Models","url":"https://arxiv.org/pdf/2603.25176"},{"title":"Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks","url":"https://arxiv.org/pdf/2505.13348"},{"title":"LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge","url":"https://arxiv.org/pdf/2506.09443"},{"title":"BadJudge: Backdoor Vulnerabilities of LLM-as-a-Judge","url":"https://arxiv.org/pdf/2503.00596"},{"title":"Evaluating the Reliability and Fidelity of Automated Judgment Systems of Large Language Models","url":"https://arxiv.org/pdf/2603.22214"}]

I found the paper you were searching for. Here are the key details:

**Title:** Security in LLM-as-a-Judge: A Comprehensive SoK

**Authors:** Aiman Al Masoud and 8 other authors

**arXiv ID:** 2603.29403

**Publication Date:** April 6, 2026

**Overview:** This paper focuses on LLM-as-a-Judge (LaaJ), a paradigm where powerful language models assess the quality, safety, or correctness of generated outputs. While the paradigm has improved scalability and efficiency of evaluation, it introduces novel security risks and reliability concerns that remain largely unexplored.

**Scope of Study:** The authors performed a comprehensive literature review across major academic databases, analyzing 863 works and selecting 45 relevant studies published between 2020 and 2026.

**Key Finding:** LLM-based judges can become both targets of adversarial manipulation and instruments through which attacks are conducted, potentially compromising the trustworthiness of evaluation pipelines.

The paper appears to be the first sy
…[truncated 202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6778
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-23T06:20:54.104672+00:00_

Web search results for query: "arXiv 2602.03794 Yang "Understanding Agent Scaling" diversity LLM multi-agent"

Links: [{"title":"[2602.03794] Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity","url":"https://arxiv.org/abs/2602.03794"},{"title":"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260203794Y/abstract"},{"title":"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity","url":"https://arxiv.org/html/2602.03794"},{"title":"Towards a Science of Scaling Agent Systems","url":"https://arxiv.org/html/2512.08296v1"},{"title":"Towards a Science of Scaling Agent Systems","url":"https://arxiv.org/pdf/2512.08296"},{"title":"Towards a Science of Scaling Agent Systems - ArXivIQ","url":"https://arxiviq.substack.com/p/towards-a-science-of-scaling-agent"},{"title":"(PDF) Towards a Science of Scaling Agent Systems","url":"https://www.researchgate.net/publication/398513043_Towards_a_Science_of_Scaling_Agent_Systems"},{"title":"[2512.08296] Towards a Science of Scaling Agent Systems","url":"https://arxiv.org/abs/2512.08296"}]

I found the paper you're looking for! Here's what I found about arXiv 2602.03794:

## "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity"

**Authors:** Yingxuan Yang, Chengrui Qu, Muning Wen, Laixi Shi, Ying Wen, Weinan Zhang, Adam Wierman, and Shangding Gu

**Submitted:** February 3, 2026

### Key Findings:

LLM-based multi-agent systems (MAS) have emerged as a promising approach to tackle complex tasks that are difficult for individual LLMs.

The paper's central finding is that scaling exhibits strong diminishing returns in homogeneous settings, while introducing heterogeneity (e.g., different models, prompts, or tools) continues to yield substantial gains.

### Main Contribution:

The authors present an information-theoretic framework showing that MAS performance is bounded by the intrinsic task unce
…[truncated 499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9135
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-23T06:21:00.631182+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LLM judge\" \"adversarial robustness\" panel ensemble 2025 2026 attack manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LLM judge\" \"adversarial robustness\" panel ensemble 2025 2026 attack manipulation"
  }
}
```

</details>

---


### Tool call

_source line 147 · 2026-05-23T06:21:01.032930+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Condorcet Jury Theorem correlated voters modern analysis 2020 2021 2022 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Condorcet Jury Theorem correlated voters modern analysis 2020 2021 2022 2023 2024"
  }
}
```

</details>

---


### Tool result

_source line 148 · 2026-05-23T06:21:08.258159+00:00_

Web search results for query: ""LLM judge" "adversarial robustness" panel ensemble 2025 2026 attack manipulation"

Links: [{"title":"SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK","url":"https://arxiv.org/pdf/2603.29403"},{"title":"A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness","url":"https://arxiv.org/html/2603.06594"},{"title":"CAP: Improving the Robustness of LLM-as-a-Judge Against Adversarial Score Manipulation via Comparative Augmented Prompting | OpenReview","url":"https://openreview.net/forum?id=wYU6OYFvid"},{"title":"Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment","url":"https://arxiv.org/pdf/2402.14016"},{"title":"LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge","url":"https://arxiv.org/html/2506.09443v1"},{"title":"[2402.14016] Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment","url":"https://arxiv.org/abs/2402.14016"},{"title":"Benchmarking adversarial robustness to bias elicitation in large language models: scalable automated assessment with LLM-as-a-judge | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10994-025-06862-6"}]

I found several highly relevant research papers on LLM judge adversarial robustness from 2025-2026. Here's what the search revealed:

## Key Research Areas

**Recent Comprehensive Studies:**

The adversarial robustness of LLMs used as assessors is systematically evaluated using RobustJudge, an automated framework that benchmarks 15 attack methods and 7 defense strategies across multiple models.

**Attack Methods:**

Wei et al. (2025) introduced an Emoji Attack that exploits token segmentation bias to trick LLM-as-a-Judge systems. Additionally, universal phrases of under 5 tokens can trick systems into providing significantly higher assessment scores.

**Defense and Ensemble Approaches:**

Abeyratne et a
…[truncated 878 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7626
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-23T06:21:09.061688+00:00_

Web search results for query: "Condorcet Jury Theorem correlated voters modern analysis 2020 2021 2022 2023 2024"

Links: [{"title":"Aggregation of Correlated Votes and Condorcet’s Jury Theorem Serguei Kaniovski∗","url":"https://serguei.kaniovski.wifo.ac.at/fileadmin/pdf/condorcet.pdf"},{"title":"Condorcet's jury theorem revisited - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/017626809390010R"},{"title":"Information pooling through majority-rule voting: Condorcet's jury theorem with correlated votes - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/016726819400068P"},{"title":"Jury Theorems (Stanford Encyclopedia of Philosophy)","url":"https://plato.stanford.edu/entries/jury-theorems/"},{"title":"On Condorcet's Jury Theorem with Abstention","url":"https://arxiv.org/pdf/2510.18062"},{"title":"Condorcet's jury theorem - Wikipedia","url":"https://en.wikipedia.org/wiki/Condorcet's_jury_theorem"},{"title":"Condorcet's Jury Theorem and the Optimum Number of Voters","url":"https://gisme.georgetown.edu/publications/condorcets-jury-theorem-and-the-optimum-number-of-voters/"},{"title":"Condorcet's Jury Theorem and the reliability of majority voting | Group Decision and Negotiation | Springer Nature Link","url":"https://link.springer.com/content/pdf/10.1007/PL00020687.pdf"},{"title":"Generalizing Condorcet’s Jury Theorem to Social Networks","url":"https://www.arxiv.org/pdf/2510.16808"},{"title":"Condorcet's Jury Theorem with Abstention","url":"https://arxiv.org/pdf/2408.00317"}]

I've performed a web search on the Condorcet Jury Theorem with correlated voters in recent modern analysis. Here are the key findings:

## Overview of Condorcet's Jury Theorem

Condorcet's jury theorem is a statistical theorem about the probability of a given group of individuals arriving at a correct decision, first expressed by the Marquis de Condorcet in his 1785 work Essay on the Application of Analysis to the Probability of Majority Deci
…[truncated 1418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8028
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-23T06:24:08.712446+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见（新颖性与完整性）\n\n### 论文信息\n- 标题：The Shifting Bottleneck: How Panel Size Modulates Adversarial Vulnerability in LLM Judge Panels\n- Venue：EMNLP 2026 via ARR May 2026\n\n---\n\n## 总体评分\n**Overall**: 3.0 — Findings\n**一句话总结**: 论文发现了真实的 panel-size-dependent vulnerability regime transition，但核心 claim \"diversity is harmful\" 因 K_eff 与 η_max 的 r=0.70 混淆而被过度解读，Analysis section 过于单薄，无法支撑 conference-level 贡献。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 统计方法扎实（wild cluster bootstrap、多重校正），但 K_eff-η_max 混淆（r=0.70）严重削弱因果推断；partial r 数据（K_eff: 0.12 vs η_max: 0.31）表明 K_eff 的效应很大程度上由 capability 中介 |\n| Excitement | 3/5 | Regime transition 发现有趣且新颖，但算术解释（majority-threshold arithmetic）使其部分 trivial，加上混淆问题和 overstated claims 降低了影响力 |\n| Reproducibility | 4/5 | 模型列表、统计规格、bootstrap 参数充分报告；代码和数据承诺 acceptance 后发布 |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] K_eff 与 η_max 的 r=0.70 结构性混淆使 \"diversity is harmful\" 因果 claim 不可靠\n- 具体位置：Section 6 (Analysis), Appendix C.2\n- 问题：论文承认 K_eff 与 η_max 相关系数达 0.70（Appendix C.2: \"maximizing panel diversity requires sampling across capability tiers, which systematically introduces less capable and therefore more vulnerable judges\"）。控制 η_max 后 K_eff 的 partial r 仅为 0.12，而 η_max 控制 K_eff 后仍有 0.31。这强烈暗示 K_eff 的正系数很可能是 capability deficit 的 proxy，而非 diversity 本身的因果效应。论文在 Appendix C.2 坦承 \"observational regression cannot reliably disentangle diversity's causal contribution from the capability deficit\"，但 abstract、introduction 和 conclusion 仍以因果语言断言 \"diversity increases vulnerability because independent judges can be targeted individually\"。\n- 为什么影响接收：核心 novelty claim 建立在因果推断上，但数据无法支撑该推断。如果 K_eff 的效应主要反映 \"diverse panels include weaker judges\"，则 contribution 1 的理论价值大幅缩水。\n- 建议修改方向：(1) 将 claim 改为 association 而非 causation；(2) 加入 mean accuracy 作为第三预测变量部分解耦；(3) 报告相同 tier 模型子集的 K_eff 效应。\n\n**N2** [critical] \"Diversity is harmful\" 在 abstract 中被过度概括，GAM 表明方向依赖攻击类型\n- 具体位置：Abstract 第 4-5 句, Section 5.4 (Figure 3), Section 5.5 (Table 5)\n- 问题：Abstract 无条件断言 \"diversity increases vulnerability\"，但 GAM 揭示 6:6 方向性分裂（targeted attacks: harmful; shared-bias attacks: protective）。Bayesian calibration 将 K_eff 从 7+/1− 翻转为 1+/6−。一个方向可被攻击类型和聚合规则完全逆转的效应不应被称为 robust finding。\n- 为什么影响接收：核心 claim 需要根本性重新表述。\n- 建议：重新框架为 \"diversity's effect is attack-mechanism-dependent and aggregation-rule-dependent\"。\n\n**N3** [critical] Analysis section（Section 6）仅 1 段（4 句话），分析深度严重不足\n- 具体位置：Section 6\n- 问题：5 个 Results subsection、3 个 contribution、6 个 appendix section 的论文，Analysis 仅 1 段。缺少：(1) regime transition 的深入理论分析；(2) adaptive adversary 利用 panel structure 的具体讨论；(3) K_eff-η_max 混淆的正文讨论（目前仅在 appendix）；(4) 实际部署指导。\n- 建议：扩展至至少 1 页。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Abstract 数字过于密集，核心 message 难以快速提取\n- 至少 12 个分数型统计量（5/12, 1/12, 7/12 等），建议将 significance counts 移至正文，abstract 聚焦定性发现。\n\n**W2** [warning] Conclusion 过于简短（5 句话），缺乏 implications 和 future work\n- 几乎逐字重复 abstract 数字，无实践意义或理论贡献讨论。\n\n**W3** [warning] 包含接近随机准确率的 judge 模型（qwen2.5-14b MMLU=0.253），可能人为放大混淆\n- 建议增加排除 accuracy < 0.50 模型后的 sensitivity analysis，特别报告 K_eff 在该子集的表现。论文提到做了这个 check 但未展示 K_eff 结果。\n\n**W4** [warning] 遗漏重要相关工作\n- Shi et al. (2024), \"Is LLM-as-a-Judge Robust?\" (arXiv:2402.14016) — 直接研究 LLM judge 对抗鲁棒性\n- Correlated-voter CJT 现代文献（Ladha 1992; Kaniovski & Zaigraev 2011）— CJT 段落仅引用 1785 原文\n- CAP (Comparative Augmented Prompting) — 提高 LLM judge 鲁棒性的方法\n\n**W5** [warning] 仅 MCQ 格式，与 LLM judge 主要应用场景（open-ended generation）脱节\n- Limitations 中提到但未充分讨论为何 MCQ 发现可迁移。\n\n## 小问题（不影响接收）\n- \"Code and Data Availability\" 作为 Limitations 的 \\paragraph 出现，建议分离\n- K_eff 定义（Eq.1 用 MI）与实际计算（Gaussian copula ρ）路径不一致，等价性依赖 Gaussian assumption，应在定义时说明\n- Table 1 gemini-3.5-flash ARC=1.00 但 26.3% format error rate，计算方式需澄清\n- Figure 2 y 轴标签和 † 含义不完全清晰\n\n## 主要优势\n- 实验设计严谨：15 模型全排列、wild cluster bootstrap、多重校正系统比较\n- Regime transition 经多种统计校正验证，adaptive-vs-random contrast 确认效应真实性\n- GAM 的 attack-type taxonomy（6:6 split）比简单 \"diversity is harmful\" 更有信息量\n- Aggregation rule 分析（Bayesian reversal）暗示可操作防御策略\n- 统计诚实度高：坦承 OLS 膨胀、informative null、confound\n\n## 引用验证\n已通过 WebSearch 验证以下关键引用真实性：\n- Almasoud et al. (2026) arXiv:2603.29403 ✓\n- Kuai et al. (2026) arXiv:2604.07650 ✓\n- Yang et al. (2026) arXiv:2602.03794 ✓\n- 其余经典引用（Lamport 1982, Krogh 1995, Goodfellow 2015 等）均为已知真实文献 ✓\n\n## 格式合规检查\n- [✓] ACL 模板 \\usepackage[review]{acl}\n- [✓] 正文 8 页以内（Sections 1-7 在 page 8 结束）\n- [✓] Author = \"Anonymous\"，double-blind 满足\n- [✓] 单一 Limitations section 在正文中（unnumbered），appendix 中无额外 Limitations\n- [✓] 参考文献不限页数\n- [✓] Figure/Table 编号引用一致",
  "reviewer_id": "2",
  "project": "cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿意见（新颖性与完整性）\n\n### 论文信息\n- 标题：The Shifting Bottleneck: How Panel Size Modulates Adversarial Vulnerability in LLM Judge Panels\n- Venue：EMNLP 2026 via ARR May 2026\n\n---\n\n## 总体评分\n**Overall**: 3.0 — Findings\n**一句话总结**: 论文发现了真实的 panel-size-dependent vulnerability regime transition，但核心 claim \"diversity is harmful\" 因 K_eff 与 η_max 的 r=0.70 混淆而被过度解读，Analysis section 过于单薄，无法支撑 conference-level 贡献。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 统计方法扎实（wild cluster bootstrap、多重校正），但 K_eff-η_max 混淆（r=0.70）严重削弱因果推断；partial r 数据（K_eff: 0.12 vs η_max: 0.31）表明 K_eff 的效应很大程度上由 capability 中介 |\n| Excitement | 3/5 | Regime transition 发现有趣且新颖，但算术解释（majority-threshold arithmetic）使其部分 trivial，加上混淆问题和 overstated claims 降低了影响力 |\n| Reproducibility | 4/5 | 模型列表、统计规格、bootstrap 参数充分报告；代码和数据承诺 acceptance 后发布 |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] K_eff 与 η_max 的 r=0.70 结构性混淆使 \"diversity is harmful\" 因果 claim 不可靠\n- 具体位置：Section 6 (Analysis), Appendix C.2\n- 问题：论文承认 K_eff 与 η_max 相关系数达 0.70（Appendix C.2: \"maximizing panel diversity requires sampling across capability tiers, which systematically introduces less capable and therefore more vulnerable judges\"）。控制 η_max 后 K_eff 的 partial r 仅为 0.12，而 η_max 控制 K_eff 后仍有 0.31。这强烈暗示 K_eff 的正系数很可能是 capability deficit 的 proxy，而非 diversity 本身的因果效应。论文在 Appendix C.2 坦承 \"observational regression cannot reliably disentangle diversity's causal contribution from the capability deficit\"，但 abstract、introduction 和 conclusion 仍以因果语言断言 \"diversity increases vulnerability because independent judges can be targeted individually\"。\n- 为什么影响接收：核心 novelty claim 建立在因果推断上，但数据无法支撑该推断。如果 K_eff 的效应主要反映 \"diverse panels include weaker judges\"，则 contribution 1 的理论价值大幅缩水。\n- 建议修改方向：(1) 将 claim 改为 association 而非 causation；(2) 加入 mean accuracy 作为第三预测变量部分解耦；(3) 报告相同 tier 模型子集的 K_eff 效应。\n\n**N2** [critical] \"Diversity is harmful\" 在 abstract 中被过度概括，GAM 表明方向依赖攻击类型\n- 具体位置：Abstract 第 4-5 句, Section 5.4 (Figure 3), Section 5.5 (Table 5)\n- 问题：Abstract 无条件断言 \"diversity increases vulnerability\"，但 GAM 揭示 6:6 方向性分裂（targeted attacks: harmful; shared-bias attacks: protective）。Bayesian calibration 将 K_eff 从 7+/1− 翻转为 1+/6−。一个方向可被攻击类型和聚合规则完全逆转的效应不应被称为 robust finding。\n- 为什么影响接收：核心 claim 需要根本性重新表述。\n- 建议：重新框架为 \"diversity's effect is attack-mechanism-dependent and aggregation-rule-dependent\"。\n\n**N3** [critical] Analysis section（Section 6）仅 1 段（4 句话），分析深度严重不足\n- 具体位置：Section 6\n- 问题：5 个 Results subsection、3 个 contribution、6 个 appendix section 的论文，Analysis 仅 1 段。缺少：(1) regime transition 的深入理论分析；(2) adaptive adversary 利用 panel structure 的具体讨论；(3) K_eff-η_max 混淆的正文讨论（目前仅在 appendix）；(4) 实际部署指导。\n- 建议：扩展至至少 1 页。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Abstract 数字过于密集，核心 message 难以快速提取\n- 至少 12 个分数型统计量（5/12, 1/12, 7/12 等），建议将 significance counts 移至正文，abstract 聚焦定性发现。\n\n**W2** [warning] Conclusion 过于简短（5 句话），缺乏 implications 和 future work\n- 几乎逐字重复 abstract 数字，无实践意义或理论贡献讨论。\n\n**W3** [warning] 包含接近随机准确率的 judge 模型（qwen2.5-14b MMLU=0.253），可能人为放大混淆\n- 建议增加排除 accuracy < 0.50 模型后的 sensitivity analysis，特别报告 K_eff 在该子集的表现。论文提到做了这个 check 但未展示 K_eff 结果。\n\n**W4** [warning] 遗漏重要相关工作\n- Shi et al. (2024), \"Is LLM-as-a-Judge Robust?\" (arXiv:2402.14016) — 直接研究 LLM judge 对抗鲁棒性\n- Correlated-voter CJT 现代文献（Ladha 1992; Kaniovski & Zaigraev 2011）— CJT 段落仅引用 1785 原文\n- CAP (Comparative Augmented Prompting) — 提高 LLM judge 鲁棒性的方法\n\n**W5** [warning] 仅 MCQ 格式，与 LLM judge 主要应用场景（open-ended generation）脱节\n- Limitations 中提到但未充分讨论为何 MCQ 发现可迁移。\n\n## 小问题（不影响接收）\n- \"Code and Data Availability\" 作为 Limitations 的 \\paragraph 出现，建议分离\n- K_eff 定义（Eq.1 用 MI）与实际计算（Gaussian copula ρ）路径不一致，等价性依赖 Gaussian assumption，应在定义时说明\n- Table 1 gemini-3.5-flash ARC=1.00 但 26.3% format error rate，计算方式需澄清\n- Figure 2 y 轴标签和 † 含义不完全清晰\n\n## 主要优势\n- 实验设计严谨：15 模型全排列、wild cluster bootstrap、多重校正系统比较\n- Regime transition 经多种统计校正验证，adaptive-vs-random contrast 确认效应真实性\n- GAM 的 attack-type taxonomy（6:6 split）比简单 \"diversity is harmful\" 更有信息量\n- Aggregation rule 分析（Bayesian reversal）暗示可操作防御策略\n- 统计诚实度高：坦承 OLS 膨胀、informative null、confound\n\n## 引用验证\n已通过 WebSearch 验证以下关键引用真实性：\n- Almasoud et al. (2026) arXiv:2603.29403 ✓\n- Kuai et al. (2026) arXiv:2604.07650 ✓\n- Yang et al. (2026) arXiv:2602.03794 ✓\n- 其余经典引用（Lamport 1982, Krogh 1995, Goodfellow 2015 等）均为已知真实文献 ✓\n\n## 格式合规检查\n- [✓] ACL 模板 \\usepackage[review]{acl}\n- [✓] 正文 8 页以内（Sections 1-7 在 page 8 结束）\n- [✓] Author = \"Anonymous\"，double-blind 满足\n- [✓] 单一 Limitations section 在正文中（unnumbered），appendix 中无额外 Limitations\n- [✓] 参考文献不限页数\n- [✓] Figure/Table 编号引用一致",
    "reviewer_id": "2",
    "project": "cert_manip_resist_eval"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-23T06:24:12.478515+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3766
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-23T06:24:25.536236+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_1/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-23T06:24:25.688322+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 152
}
```

</details>

---


### Assistant

_source line 154 · 2026-05-23T06:24:36.170916+00:00_

审稿完成，已提交给 Review Director。

**评分**: Overall 3.0 (Findings)

**三个 Must-Fix 问题**：
1. K_eff 与 η_max 的 r=0.70 混淆使 "diversity is harmful" 因果 claim 不可靠（partial r 仅 0.12 vs 0.31）
2. "Diversity is harmful" 被过度概括——GAM 显示 6:6 方向分裂，Bayesian calibration 完全逆转方向
3. Analysis section 仅 1 段，与论文的实验规模严重不匹配

**五个 Should-Fix**：Abstract 数字密集、Conclusion 过短、近随机准确率模型放大混淆、遗漏关键相关工作（Shi et al. 2024 等）、仅 MCQ 格式。格式合规无问题，引用验证通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2"
}
```

</details>

---


## Round 6

## Round 6

4 recorded events


### User

_source line 155 · 2026-05-23T06:25:04.494583+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 1 的完整审稿原文：

**Overall**: 3.0 (Findings)

**Must-Fix 问题：**

**N1** [critical] Log-log OLS 在 bounded [0,1] ASR 数据上的适用性
- ASR ∈ [0,1] 是 bounded fractional response variable。log(ASR + ε) 的 OLS 回归存在多重问题：(a) ASR=0 时 log(10⁻⁶) ≈ −13.8 创造人工地板值，产生高杠杆效应；(b) OLS 线性残差假设在 bounded variable 的 log 变换下不成立；(c) 标准化系数解释依赖 normality 假设。
- 标准替代方案：beta regression 或 fractional logit。ε 敏感性检验只说明对 ε 值不敏感，未解决根本问题。
- 建议：至少用 beta regression 或 fractional logit 作为 robustness check 重跑全部 12 conditions × 3 K values。

**N2** [critical] Diversity-Capability 混淆（r = 0.70）使因果推断不可靠
- K_eff 与 η_max 的 r = 0.70，Appendix C.2 承认"observational regression cannot reliably disentangle diversity's causal contribution"，但正文用因果语言断言 "diversity increases vulnerability because independent judges can be targeted individually"。
- 15 模型中 6 个 local 全部 AWQ INT4 量化，clean accuracy 0.253–0.543，高 K_eff panel 必然包含弱 local judges。K_eff 正系数可能仅反映"包含弱模型"。
- VIF 疑问：两预测变量 VIF = 1/(1-r²)，r=0.70 → VIF ≈ 1.96，但论文称 VIF 平均 3.0，说明 log 空间 r 更高。
- 建议：(1) capability tier 内部分析 K_eff；(2) 加入 panel 平均 clean accuracy 控制变量；(3) 全文因果措辞降级。

**N3** [critical] 仅三个离散 K 值不足以支撑 "regime transition"
- K ∈ {3, 5, 7} 三个点不足以确立 transition 是连续还是阶跃，K* 在哪里，K=4 的行为。
- 建议：增加 K=4 数据点，或将措辞从 "regime transition" 降级为 "K-dependent shift"。

**Should-Fix 问题：**

**W1** Theorem 1 实证覆盖率仅 58%（61/105 judge pairs）
- 42% pairs 存在 vulnerability 交叉，theorem 的 monotonicity 保证不成立。

**W2** K_eff 在 clean data 上计算但预测 attacked ASR 的假设合理性
- 隐含假设 judges 间相关结构在 clean 和 attacked 下不变，几乎肯定不成立。
- 建议：在 attacked conditions 下重新计算 K_eff 对比。

**W3** 6 个 local 模型全部 AWQ INT4 量化的系统性偏差
- 建议：仅用 9 个 API 模型构建 panels（C(9,3)=84）检查 K_eff 效应。

**W4** Wild cluster bootstrap 中 13 clusters per position 的充分性
- 经典 rule of thumb ≥ 50 clusters。max-p 聚合进一步增加保守程度，可能解释 K_eff 从 OLS 8/12 暴降到 bootstrap 0-1/12。

**W5** Oracle adversary 过强导致实际意义存疑
- 建议增加 black-box adversary 实验。

---

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-23T06:27:00.549243+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: Log-log OLS 在 bounded ASR 数据上的适用性**\n\n同意这是一个实质性的统计方法论问题。ASR ∈ [0,1] 是 fractional response variable，标准处理应为 beta regression 或 fractional logit (Papke & Wooldridge, 1996)，而非 log(ASR + ε) 的 OLS。Reviewer 1 正确指出了两个具体风险：\n\n1. ASR=0 时 log(10⁻⁶) ≈ −13.8 的人工地板效应。论文报告 ε ∈ {10⁻³, 10⁻⁶, 10⁻⁹} 敏感性稳定（Section 5.1 末尾），但这只说明地板值的位置不影响 significance counts，并未解决 zero-ASR panels 作为高杠杆点扭曲回归面的问题。\n2. Log-transformed bounded variable 的残差分布不满足 OLS 的 normality/homoscedasticity 假设。\n\n补充一点：论文用了 4 种校正方法（OLS / Clustered SE / Mixed Effects / Wild Cluster Bootstrap, Table 3），其中 bootstrap 是 distribution-free 的，部分缓解了分布假设问题。但 bootstrap 本身仍基于 log-log specification，高杠杆点的影响并未消除。\n\n建议的 beta regression / fractional logit robustness check 实施成本低（同样的 12 conditions × 3 K values），应该做。如果 regime transition 在替代 specification 下保持，论文的说服力会大幅增强。我认为这是 should-fix 级别而非 must-fix——因为论文已有多种 robustness check，但仍值得补充。\n\n---\n\n**[AGREE] R1-N2: Diversity-Capability 混淆（r=0.70）**\n\n完全同意。这与我自己的 N1 一致。补充 Reviewer 1 的两点新观察：\n\n1. **VIF 计算矛盾**：Reviewer 1 正确指出，若原始空间 r=0.70 则 VIF ≈ 1.96，但论文报告 VIF 平均 3.0（Section 6: \"VIF averages 3.0 (10/12 below 5)\"）。这意味着 log 空间中 K_eff 和 η_max 的相关性更高（约 r ≈ 0.82），混淆比正文声称的更严重。论文应报告 log 空间的相关系数。\n2. **结构性来源**：6 个 local 模型全部 AWQ INT4 量化且 accuracy 偏低（Table 1: 0.253–0.543），高 K_eff panel 几乎必然包含这些弱模型。Reviewer 1 建议的 capability tier 内部分析（仅 9 API 模型，C(9,3)=84 panels）和加入 panel 平均 accuracy 控制变量，都是必要的。\n\n与我的 N1 建议一致：全文因果措辞必须降级。\n\n---\n\n**[REBUT] R1-N3: 仅三个离散 K 值不足以支撑 \"regime transition\"**\n\n部分不同意将此列为 must-fix。理由：\n\n1. **经验证据的强度**：K=3→K=5 的变化幅度极大——η_max 从 5/12 降至 0/12，K_eff 从 1/12 升至 7/12（Table 4）。这不是边际变化，而是完全翻转。K=7 进一步确认了 K≥5 的模式（0/12, 5/12）。要求 K=4 来区分 \"transition\" 和 \"shift\" 主要是语义问题而非实质问题。\n2. **论文已承认精度限制**：Limitations 明确写道 \"the transition threshold between the η_max-dominant and K_eff-dominant regimes is bounded to 3 < K* < 5 but not precisely identified\"（main.tex line 40）。\n3. **实验成本合理**：C(15,4)=1365 panels 在技术上可行，但增加 K=4 不会改变核心发现——无论 K=4 的结果如何，K=3 和 K≥5 之间的翻转都已被确立。\n\n不过，Reviewer 1 的措辞建议有道理：将 \"regime transition\" 改为 \"K-dependent dominance shift\" 或 \"regime change between K=3 and K≥5\" 可以更精确地反映三点数据的证据力度。建议降级为 should-fix，通过措辞调整解决。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Theorem 1 实证覆盖率仅 58%**\n\n同意这是一个值得注意的局限。Theorem 1 的数学正确性不受影响——它是一个条件性声明（IF pointwise more vulnerable, THEN ASR increases）。但 42% 的 judge pairs 存在 vulnerability 交叉（即 judge A 在某些攻击下更弱，judge B 在另一些攻击下更弱），意味着 theorem 的实际适用范围有限。\n\n论文将 Theorem 1 用作 β₂ > 0 的理论预测（Section 3: \"As a structural property, the theorem predicts β₂ > 0\"），但如果 42% 的 pairs 不满足前提条件，则 theorem 对回归系数方向的预测力减弱。建议在正文中明确讨论覆盖率限制及其对理论预测的影响。\n\n---\n\n**[AGREE] R1-W2: K_eff 在 clean data 上计算但预测 attacked ASR**\n\n这是一个我在自己审稿中遗漏的重要问题。K_eff 通过 clean data 上的 pairwise MI 计算（Section 4.3），但用于预测 attacked conditions 下的 ASR。隐含假设是 judges 间的相关结构在攻击前后不变。\n\n这个假设几乎肯定不成立：\n- Shared-bias attacks（sycophancy, verbosity bias）会使原本独立的 judges 产生相关失败（都被同一偏差利用），增大攻击下的相关性\n- Targeted attacks（prompt injection）可能降低相关性（不同 judges 对同一注入有不同反应）\n\n如果 clean-data K_eff 不能准确反映 attacked conditions 下的实际 independence，则整个回归框架的解释力存疑。建议增加 attacked-condition K_eff 作为对比，或至少讨论这一假设的可能影响。\n\n---\n\n**[AGREE] R1-W3: 6 个 AWQ INT4 模型的系统性偏差**\n\n与我的 W3 一致。9 API 模型子集分析（C(9,3)=84 panels）是必要的 robustness check，实施成本极低。补充：如果 K_eff 在 84 panels 中仍然 positive significant，则大幅增强 \"diversity is harmful\" 的证据力；如果消失，则进一步支持混淆解释。\n\n---\n\n**[AGREE] R1-W4: 13 clusters per position 的充分性**\n\n同意这是一个值得关注的技术问题。经典文献建议 ≥50 clusters（Cameron & Miller, 2015）。13 clusters per position + max-p across 3 positions 的组合极为保守，可能导致 K_eff 的 Type II 错误率偏高。\n\n然而，这个问题是双刃剑：如果 bootstrap 因 few clusters 过度保守，那么 K_eff 在 K≥5 下仍有 7/12 显著（Table 4）就更值得信赖——它们在极端保守条件下存活。同时，K=3 下 K_eff 的 0-1/12 可能部分是 methodological artifact 而非 true null。\n\n论文应讨论 cluster 数量的影响，但我认为这不改变核心发现的方向。\n\n---\n\n**[AGREE] R1-W5: Oracle adversary 过强**\n\n同意增加 black-box adversary 实验会加强论文。论文在 Appendix C.4 已讨论 partial-information 下的 η_max 表现（partial information + clustered SE 下 η_max 在 12/12 conditions 显著），但未对 K_eff 做类似分析。Limitations 也承认 \"realistic adversaries with partial knowledge of panel composition would achieve lower ASR\"。\n\n一个简单的 black-box 实验（adversary 不知道 panel composition，对所有 judges 使用相同攻击）会帮助区分 oracle-specific 和 general 的 vulnerability patterns。建议作为 should-fix。\n\n---\n\n### 总结\n\n与 Reviewer 1 的 6 个主要问题中，我同意 5 个（N1, N2, W1-W5），部分反驳 1 个（N3）。两位 reviewer 在以下关键问题上达成一致：\n\n1. **K_eff-η_max 混淆是最核心的问题**（R1-N2 = R2-N1），严重削弱因果推断\n2. **\"Diversity is harmful\" 需要大幅 qualify**（R1-N2 因果措辞 + R2-N2 攻击类型依赖性）\n3. **AWQ INT4 模型子集分析是必要的 robustness check**（R1-W3 = R2-W3）\n\nReviewer 1 新增了我遗漏的两个重要技术问题：(1) OLS 在 bounded response 上的适用性（N1），(2) clean-data K_eff 预测 attacked ASR 的假设合理性（W2）。这两点都值得重视。\n\n我的 N3（Analysis section 过短）和 W1（Abstract 数字过密）是 Reviewer 1 未覆盖的写作质量问题，仍然成立。",
  "reviewer_id": "2",
  "project": "cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: Log-log OLS 在 bounded ASR 数据上的适用性**\n\n同意这是一个实质性的统计方法论问题。ASR ∈ [0,1] 是 fractional response variable，标准处理应为 beta regression 或 fractional logit (Papke & Wooldridge, 1996)，而非 log(ASR + ε) 的 OLS。Reviewer 1 正确指出了两个具体风险：\n\n1. ASR=0 时 log(10⁻⁶) ≈ −13.8 的人工地板效应。论文报告 ε ∈ {10⁻³, 10⁻⁶, 10⁻⁹} 敏感性稳定（Section 5.1 末尾），但这只说明地板值的位置不影响 significance counts，并未解决 zero-ASR panels 作为高杠杆点扭曲回归面的问题。\n2. Log-transformed bounded variable 的残差分布不满足 OLS 的 normality/homoscedasticity 假设。\n\n补充一点：论文用了 4 种校正方法（OLS / Clustered SE / Mixed Effects / Wild Cluster Bootstrap, Table 3），其中 bootstrap 是 distribution-free 的，部分缓解了分布假设问题。但 bootstrap 本身仍基于 log-log specification，高杠杆点的影响并未消除。\n\n建议的 beta regression / fractional logit robustness check 实施成本低（同样的 12 conditions × 3 K values），应该做。如果 regime transition 在替代 specification 下保持，论文的说服力会大幅增强。我认为这是 should-fix 级别而非 must-fix——因为论文已有多种 robustness check，但仍值得补充。\n\n---\n\n**[AGREE] R1-N2: Diversity-Capability 混淆（r=0.70）**\n\n完全同意。这与我自己的 N1 一致。补充 Reviewer 1 的两点新观察：\n\n1. **VIF 计算矛盾**：Reviewer 1 正确指出，若原始空间 r=0.70 则 VIF ≈ 1.96，但论文报告 VIF 平均 3.0（Section 6: \"VIF averages 3.0 (10/12 below 5)\"）。这意味着 log 空间中 K_eff 和 η_max 的相关性更高（约 r ≈ 0.82），混淆比正文声称的更严重。论文应报告 log 空间的相关系数。\n2. **结构性来源**：6 个 local 模型全部 AWQ INT4 量化且 accuracy 偏低（Table 1: 0.253–0.543），高 K_eff panel 几乎必然包含这些弱模型。Reviewer 1 建议的 capability tier 内部分析（仅 9 API 模型，C(9,3)=84 panels）和加入 panel 平均 accuracy 控制变量，都是必要的。\n\n与我的 N1 建议一致：全文因果措辞必须降级。\n\n---\n\n**[REBUT] R1-N3: 仅三个离散 K 值不足以支撑 \"regime transition\"**\n\n部分不同意将此列为 must-fix。理由：\n\n1. **经验证据的强度**：K=3→K=5 的变化幅度极大——η_max 从 5/12 降至 0/12，K_eff 从 1/12 升至 7/12（Table 4）。这不是边际变化，而是完全翻转。K=7 进一步确认了 K≥5 的模式（0/12, 5/12）。要求 K=4 来区分 \"transition\" 和 \"shift\" 主要是语义问题而非实质问题。\n2. **论文已承认精度限制**：Limitations 明确写道 \"the transition threshold between the η_max-dominant and K_eff-dominant regimes is bounded to 3 < K* < 5 but not precisely identified\"（main.tex line 40）。\n3. **实验成本合理**：C(15,4)=1365 panels 在技术上可行，但增加 K=4 不会改变核心发现——无论 K=4 的结果如何，K=3 和 K≥5 之间的翻转都已被确立。\n\n不过，Reviewer 1 的措辞建议有道理：将 \"regime transition\" 改为 \"K-dependent dominance shift\" 或 \"regime change between K=3 and K≥5\" 可以更精确地反映三点数据的证据力度。建议降级为 should-fix，通过措辞调整解决。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Theorem 1 实证覆盖率仅 58%**\n\n同意这是一个值得注意的局限。Theorem 1 的数学正确性不受影响——它是一个条件性声明（IF pointwise more vulnerable, THEN ASR increases）。但 42% 的 judge pairs 存在 vulnerability 交叉（即 judge A 在某些攻击下更弱，judge B 在另一些攻击下更弱），意味着 theorem 的实际适用范围有限。\n\n论文将 Theorem 1 用作 β₂ > 0 的理论预测（Section 3: \"As a structural property, the theorem predicts β₂ > 0\"），但如果 42% 的 pairs 不满足前提条件，则 theorem 对回归系数方向的预测力减弱。建议在正文中明确讨论覆盖率限制及其对理论预测的影响。\n\n---\n\n**[AGREE] R1-W2: K_eff 在 clean data 上计算但预测 attacked ASR**\n\n这是一个我在自己审稿中遗漏的重要问题。K_eff 通过 clean data 上的 pairwise MI 计算（Section 4.3），但用于预测 attacked conditions 下的 ASR。隐含假设是 judges 间的相关结构在攻击前后不变。\n\n这个假设几乎肯定不成立：\n- Shared-bias attacks（sycophancy, verbosity bias）会使原本独立的 judges 产生相关失败（都被同一偏差利用），增大攻击下的相关性\n- Targeted attacks（prompt injection）可能降低相关性（不同 judges 对同一注入有不同反应）\n\n如果 clean-data K_eff 不能准确反映 attacked conditions 下的实际 independence，则整个回归框架的解释力存疑。建议增加 attacked-condition K_eff 作为对比，或至少讨论这一假设的可能影响。\n\n---\n\n**[AGREE] R1-W3: 6 个 AWQ INT4 模型的系统性偏差**\n\n与我的 W3 一致。9 API 模型子集分析（C(9,3)=84 panels）是必要的 robustness check，实施成本极低。补充：如果 K_eff 在 84 panels 中仍然 positive significant，则大幅增强 \"diversity is harmful\" 的证据力；如果消失，则进一步支持混淆解释。\n\n---\n\n**[AGREE] R1-W4: 13 clusters per position 的充分性**\n\n同意这是一个值得关注的技术问题。经典文献建议 ≥50 clusters（Cameron & Miller, 2015）。13 clusters per position + max-p across 3 positions 的组合极为保守，可能导致 K_eff 的 Type II 错误率偏高。\n\n然而，这个问题是双刃剑：如果 bootstrap 因 few clusters 过度保守，那么 K_eff 在 K≥5 下仍有 7/12 显著（Table 4）就更值得信赖——它们在极端保守条件下存活。同时，K=3 下 K_eff 的 0-1/12 可能部分是 methodological artifact 而非 true null。\n\n论文应讨论 cluster 数量的影响，但我认为这不改变核心发现的方向。\n\n---\n\n**[AGREE] R1-W5: Oracle adversary 过强**\n\n同意增加 black-box adversary 实验会加强论文。论文在 Appendix C.4 已讨论 partial-information 下的 η_max 表现（partial information + clustered SE 下 η_max 在 12/12 conditions 显著），但未对 K_eff 做类似分析。Limitations 也承认 \"realistic adversaries with partial knowledge of panel composition would achieve lower ASR\"。\n\n一个简单的 black-box 实验（adversary 不知道 panel composition，对所有 judges 使用相同攻击）会帮助区分 oracle-specific 和 general 的 vulnerability patterns。建议作为 should-fix。\n\n---\n\n### 总结\n\n与 Reviewer 1 的 6 个主要问题中，我同意 5 个（N1, N2, W1-W5），部分反驳 1 个（N3）。两位 reviewer 在以下关键问题上达成一致：\n\n1. **K_eff-η_max 混淆是最核心的问题**（R1-N2 = R2-N1），严重削弱因果推断\n2. **\"Diversity is harmful\" 需要大幅 qualify**（R1-N2 因果措辞 + R2-N2 攻击类型依赖性）\n3. **AWQ INT4 模型子集分析是必要的 robustness check**（R1-W3 = R2-W3）\n\nReviewer 1 新增了我遗漏的两个重要技术问题：(1) OLS 在 bounded response 上的适用性（N1），(2) clean-data K_eff 预测 attacked ASR 的假设合理性（W2）。这两点都值得重视。\n\n我的 N3（Analysis section 过短）和 W1（Abstract 数字过密）是 Reviewer 1 未覆盖的写作质量问题，仍然成立。",
    "reviewer_id": "2",
    "project": "cert_manip_resist_eval"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-23T06:27:04.464795+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3915
}
```

</details>

---


### Assistant

_source line 158 · 2026-05-23T06:27:11.680467+00:00_

交叉回应已提交。

总结：对 Reviewer 1 的 8 个问题中同意 7 个，部分反驳 1 个（N3 "仅三个 K 值"——认为经验证据强度足够支撑核心发现，但同意措辞应调整，建议降级为 should-fix）。两位 reviewer 在三个核心问题上完全一致：K_eff-η_max 混淆、"diversity is harmful" 过度表述、AWQ 模型子集 robustness check 缺失。Reviewer 1 提出了两个我遗漏的技术问题：log-log OLS 在 bounded variable 上的适用性，以及 clean-data K_eff 预测 attacked ASR 的假设合理性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2"
}
```

</details>

---


## Round 7

## Round 7

74 recorded events


### User

_source line 159 · 2026-05-23T11:39:44.527769+00:00_

[Round 1 审稿请求]:
你负责 **新颖性与完整性** 审查。

## 论文信息
- **标题**: "The Shifting Bottleneck: How Panel Size Modulates Adversarial Vulnerability in LLM Judge Panels"
- **论文路径**: `projects/cert_manip_resist_eval/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/submitted.pdf`

## Venue 要求
- **Venue**: EMNLP 2026（通过 ARR 统一审稿）
- **类型**: Long Paper
- **页数限制**: 正文严格 8 页，references 不限。Mandatory Limitations 和 optional ethical considerations 不计入页数，但不得包含过多额外内容
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind（无匿名期要求，但审稿过程 double-blind）
- **ARR May 2026 cycle deadline**: ~2026-05-25
- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit

## 你的审查侧重

**核心关注**：论文的学术贡献新颖性、完整性、写作质量和格式合规。

具体审查点：
1. **新颖性与贡献评估**：
   - 三个 contributions 的实质性和原创性
   - "Panel-size-dependent regime transition" 是否为真正的新发现
   - 与现有 ensemble diversity / CJT / adversarial transferability 文献的区分度
   - 这些发现对 LLM evaluation 社区的实际价值

2. **Related Work 覆盖**：
   - LLM-as-Judge 文献是否充分（Zheng 2023, Wang 2023, Shi 2024, etc.）
   - CJT 和 correlated voting 理论的引用是否完整（Ladha 1992, Kaniovski & Zaigraev 2011）
   - Ensemble diversity 理论的对接（Brown 2005, Kuncheva & Whitaker 2003, Krogh & Vedelsby 1995）
   - Adversarial robustness 和 transferability（Goodfellow 2015, Papernot 2016/2017, Tramèr 2018）
   - 是否有重要遗漏的相关工作

3. **写作质量**：
   - Abstract：信息密度是否合适（数字过多？核心 message 是否清晰？）
   - Introduction：motivation 和 gap 是否清楚
   - Analysis section：分析深度是否与实验规模匹配
   - Conclusion：是否有 practical implications 和 future work
   - 全文叙事连贯性和逻辑流

4. **格式合规**（严格检查）：
   - **正文是否严格 ≤8 页**（注意：Conclusion 末尾是否溢出到第 9 页）
   - Limitations section 是否存在且位置正确（正文中，非 appendix）
   - 匿名性：是否有任何 de-anonymization 信息（作者名、GitHub links、机构名）
   - 引用格式是否一致（natbib）
   - Figure/Table 编号和引用是否正确
   - 是否只有一个 Limitations section（禁止在 appendix 中重复）

5. **Framing 与 Overclaiming**：
   - Title 是否准确反映论文内容（不 overclaim 也不 underclaim）
   - Abstract/Conclusion 中的 claims 是否有充分证据支撑
   - "Diversity is harmful" vs "attack-mechanism-dependent" 的措辞是否准确
   - 因果 vs 相关语言的使用

6. **论文结构与 Appendix**：
   - 正文与附录的信息分配是否合理
   - 附录（A-K）内容是否支持正文 claims
   - 是否有应在正文但被放到附录的关键结果

请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准）→ Confidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-23T11:40:01.073831+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-23T11:40:01.074272+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-23T11:40:06.656272+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 163 · 2026-05-23T11:40:07.710600+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer form dimensions scoring rubric 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer form dimensions scoring rubric 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-23T11:40:10.222328+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/submitted.pdf",
  "project": "cert_manip_resist_eval",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/submitted.pdf",
    "project": "cert_manip_resist_eval",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-23T11:40:13.334070+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria:

## Reviewer Guidelines

Reviewers are asked to follow this workflow: (1) read the paper and get the first impression, (2) search for related w
…[truncated 1137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6677
}
```

</details>

---


### Tool result

_source line 166 · 2026-05-23T11:40:13.384756+00:00_

Web search results for query: "ACL Rolling Review reviewer form dimensions scoring rubric 2025 2026"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"}]

I found relevant information about the ACL Rolling Review (ARR) reviewer form and scoring rubric. Here are the key findings:

## Reviewer Form Scoring Dimensions (2025-2026)

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, exc
…[truncated 1095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5674
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-23T11:40:14.488816+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 404.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 431.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 553.9}], \"total_pages\": 17, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images
…[truncated 41 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4266
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-23T11:40:23.029760+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment scales and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment scales and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 169 · 2026-05-23T11:40:24.389901+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including what reviewers should evaluate, scoring criteria, what makes a good review, and any specific instructions about novelty, soundness, excitement scoring."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines including what reviewers should evaluate, scoring criteria, what makes a good review, and any specific instructions about novelty, soundness, excitement scoring."
  }
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-23T11:40:25.798390+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/submitted.pdf",
  "project": "cert_manip_resist_eval",
  "pages": "9-17",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/submitted.pdf",
    "project": "cert_manip_resist_eval",
    "pages": "9-17",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 171 · 2026-05-23T11:40:26.250061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-23T11:40:26.704846+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 173 · 2026-05-23T11:40:27.708806+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-23T11:40:28.010286+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-23T11:40:29.625025+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. Soundness
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. Excitement
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper."
- **2**: "Potentially Interesting: does not resonate with me, but might with others."
- **1**: "Not Exciting: does not resonate with me."

## 4. Overall Assessment
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5% papers)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 5. Reproducibility
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty
- **2**: Hard to reproduce
- **1**: Cannot reproduce

## 6. Datasets & Software Value
Scale: 1-5 each
- **5**: Enabling (affects research choices)
- **4**: Useful (recommended for ongoing work)
- **3**: Potentially useful
- **2**: Documentary value only
- **1**: No usable resources

## 7. 
…[truncated 193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6595
}
```

</details>

---


### Tool result

_source line 176 · 2026-05-23T11:40:38.826264+00:00_

# ARR Reviewer Guidelines Summary

## Core Review Tasks

Reviewers complete four main tasks:
1. **Allocate time** for reviewing and discussion periods
2. **Check assignments** for expertise fit and conflicts of interest
3. **Write strong reviews** with detailed feedback
4. **Update assessments** after author responses

## What Reviewers Evaluate

Reviewers assess papers across multiple dimensions using a structured approach:

**Initial Phase:** "read the paper at least twice: skimming and in-depth reading." The skim focuses on research questions and contribution scope before examining results, while in-depth reading evaluates technical soundness and evidence quality.

**Checklist Requirements:** Papers may warrant desk rejection for appropriateness issues, hallucinated citations, anonymity violations, style guide breaches, missing limitations sections, ethics concerns, or inadequate responsible NLP checklist responses.

## Scoring Criteria (as of February 2025)

ARR uses three distinct scores:

- **Soundness**: Technical rigor and validity, "must be justified by the text of the review"
- **Excitement**: Personal interest level, treated as orthogonal to soundness assessment
- **Overall Recommendation**: Composite score reflecting soundness, excitement, novelty, and potential impact

## What Makes a Good Review

Strong reviews demonstrate these qualities:

**Specificity Required:** Instead of "missing relevant references," cite exactly which papers. Rather than "X is unclear," identify "Y and Z are missing from the description of X."

**Professional Tone:** "Write the review you would like to get yourself." Reviews should be collegial and constructive, avoiding sarcasm or dismissiveness that damages reviewer-author relationships.

**Evidence-Based:** Low scores require supporting detail. Reviewers should scrutinize unconscious biases before finalizing assessments.

## Common Review Pitfalls to Avoid

The guidelines list 17 heuristics that often produce unjustified cri
…[truncated 2677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 14436
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-23T11:40:39.829537+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 495.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 481.7}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 401.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.4}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.9}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 587.9}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 222.9}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p17.png\", \"width\": 124
…[truncated 276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 14031
}
```

</details>

---


### Tool result

_source line 178 · 2026-05-23T11:40:41.239668+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 14534
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-23T11:40:41.842322+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 13832
}
```

</details>

---


### Tool result

_source line 180 · 2026-05-23T11:40:41.843202+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 15593
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-23T11:40:41.844002+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 14135
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-23T11:40:49.119861+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-23T11:40:50.076123+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-23T11:40:50.126695+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 185 · 2026-05-23T11:40:50.579821+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 186 · 2026-05-23T11:40:50.983309+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 187 · 2026-05-23T11:40:51.034098+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 188 · 2026-05-23T11:40:51.288606+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 708
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-23T11:40:51.792495+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 758
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-23T11:41:01.484276+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-23T11:41:02.138316+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-23T11:41:02.138825+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-23T11:41:02.942324+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-23T11:41:03.394316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 195 · 2026-05-23T11:41:03.595482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 196 · 2026-05-23T11:41:03.801368+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 407
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-23T11:41:04.354339+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 758
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-23T11:41:09.974873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 199 · 2026-05-23T11:41:10.326654+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 200 · 2026-05-23T11:41:11.232248+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1257
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-23T11:41:11.233429+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-23T11:41:11.233792+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 203 · 2026-05-23T11:41:11.735760+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 204 · 2026-05-23T11:41:12.138262+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-23T11:41:12.139390+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-23T11:41:12.190780+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_2/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-23T11:41:12.543125+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-23T11:41:19.116417+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-23T11:41:19.217276+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb,amsthm}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{definition}{Definition}
17	\newtheorem{proposition}{Proposition}
18	
19	\title{The Shifting Bottleneck: How Panel Size Modulates\\Adversarial Vulnerability in LLM Judge Panels}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	Multi-judge LLM evaluation panels are widely assumed to benefit from judge diversity, drawing inspiration from fault tolerance in distributed systems. We decompose panel vulnerability into individual judge weakness ($\eta_{\max}$) and structural diversity ($K_{\mathrm{eff}}$) across 15 models, six attack types, two benchmarks, and panel sizes $K \in \{3, 5, 7\}$ (up to 6,435 panels). We discover a panel-size-dependent vulnerability regime transition: $\eta_{\max}$ dominates at small panels, but $K_{\mathrm{eff}}$ emerges as the dominant predictor at $K{\geq}5$ (bootstrap significance rising from 1/12 to 7/12). This aggregate positive association masks attack-mechanism-dependent structure: higher diversity is associated with increased vulnerability for targeted attacks but decreased vulnerability for shared-bias attacks. Aggregation rules further modulate the relationship, with Bayesian calibration reversing the diversity channel and neutralizing both predictors at larger panels. The defense strategy must match the panel size regime: small panels require screening for individual robustness; larger panels require managing judge independence, with the net effect depending on attack type and aggregation method.
28	\end{abstract}
29	
30	\input{introduction}
31	\input{related_work}
32	\input{threat_model}
33	\input{m
…[truncated 2213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-23T11:41:26.544104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-23T11:41:26.895887+00:00_

1	\section{Introduction}
2	
3	\begin{figure*}[t]
4	\centering
5	\includegraphics[width=\textwidth]{figures/fig_framework.pdf}
6	\caption{Overview of our evaluation framework. Given $N$ candidate LLM judges, we construct $K$-judge panels (\S\ref{sec:experiments}), subject them to six adversarial attack types (\S\ref{sec:threat_model}), and assess vulnerability through two complementary metrics: $\eta_{\max}$ (weakest-link individual susceptibility) and $K_{\text{eff}}$ (effective independent channels via mutual information). Panel decisions are aggregated through four methods of increasing sophistication (\S\ref{sec:aggregation}).}
7	\label{fig:framework}
8	\end{figure*}
9	
10	Multi-judge panels have emerged as the dominant defense against bias and manipulation in LLM-based evaluation. After \citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work exposed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, drawing inspiration from Byzantine fault tolerance (BFT), where majority voting among independent nodes tolerates faulty responses \citep{lamport1982byzantine,castro1999practical}. A recent systematization of LLM-judge security reports that 7-model committees reduce attack success rates from 50--68\% to 10--19\% \citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation.
11	
12	Yet the evidence for diversity as a causal defense is weaker than it appears. The observed ASR reduction conflates panel diversity (judge independence) with individual robustness (strongest members). No existing work disentangles these across panel sizes. BFT adversaries control faulty nodes internally, whereas evaluation adversaries manipulate inputs externally; the SDPI bounds joint failure but assumes non-adaptive faults \cite
…[truncated 2726 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-23T11:41:26.896285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-23T11:41:27.247856+00:00_

1	\section{Related Work}
2	
3	\paragraph{LLM-as-Judge and Multi-Judge Evaluation.}
4	LLM judges gained traction after \citet{zheng2023judging} established them as scalable alternatives to human annotation. \citet{wang2023fair} documented systematic failure modes (position bias, verbosity, sycophancy), motivating multi-judge panels; \citet{shi2024judgerobust} further quantified robustness gaps under adversarial prompts. Aggregating noisy annotators traces back to \citet{dawid1979maximum}; \citet{verga2024replacing} showed diverse panels can match single large judges, and \citet{panickssery2024llm} identified self-preference bias driving within-family correlations. These frameworks assume benign conditions; we test whether aggregation benefits survive adversarial manipulation. \citet{almasoud2026security} reported that 7-model committees reduce ASR from 50--68\% to 10--19\%, but did not disentangle diversity from individual robustness.
5	
6	\paragraph{Condorcet Jury Theorem.}
7	\citet{condorcet1785essai} proved that majority voting accuracy converges to 1 when per-voter accuracy exceeds 0.5. \citet{ladha1992condorcet} extended the theorem to correlated voters, showing that positive correlation weakens the convergence guarantee; \citet{kaniovski2011optimal} derived optimal jury size under correlated votes. LLM judge outputs exhibit precisely this correlation structure, and our results instantiate the CJT failure mode: when adaptive attacks push judges below the critical threshold, panel expansion amplifies error.
8	
9	\paragraph{Ensemble Diversity Theory.}
10	\citet{krogh1995neural} proved that ensemble error equals average member error minus a diversity term; \citet{brown2005managing} showed diversity reduces error only when members maintain sufficiently low bias. In our setting, weaker judges introduce bias large enough to offset diversity benefits. \citet{kuncheva2003measures} found that no pairwise diversity measure reliably predicted ensemble improvement; our $K_{
…[truncated 2018 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-23T11:41:27.248220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-23T11:41:27.298787+00:00_

1	\section{Conclusion}
2	
3	The dominant vulnerability predictor in LLM judge panels transitions with panel size: $\eta_{\max}$ dominates at $K{=}3$ (bootstrap 5/12, $K_{\mathrm{eff}}$ 1/12); at $K{\geq}5$, $K_{\mathrm{eff}}$ dominates (7/12, $\eta_{\max}$ 0/12). The aggregate positive $K_{\mathrm{eff}}$ association is attack-mechanism-dependent (targeted positive, shared-bias negative); Bayesian calibration reverses it at $K{=}3$ and neutralizes both predictors at $K{=}5$. Observational regression cannot reliably disentangle diversity's causal contribution from the co-occurring capability deficit (\S\ref{sec:analysis}). For deployment: at $K{=}3$, screen for individual robustness and use Bayesian aggregation; at $K{\geq}5$, prefer correlated robustness profiles over maximally independent judges. Causal identification requires training-based diversity control \citep{kariyappa2019improving,pang2019improving}; the transition threshold $K^*$ ($3 < K^* < 5$) and generalization beyond multiple-choice formats remain open.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-23T11:41:32.022562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-23T11:41:32.374459+00:00_

1	\section{Threat Model and Problem Formulation}
2	\label{sec:threat_model}
3	
4	A \emph{panel} $\mathcal{P} = \{J_1, \ldots, J_K\}$ consists of $K$ judges (with $K$ odd) that evaluate a candidate text via majority vote: the text is accepted if at least $t = \lceil K/2 \rceil$ judges approve it. Under an attack $a$, each judge $J_j$ is compromised with marginal failure probability $\eta_j(a) = \Pr(X_j^a = 1)$, where $X_j^a \in \{0,1\}$ denotes the failure indicator. We write $\eta_{\max} = \max_j \eta_j$ for the vulnerability of the weakest judge. The \emph{panel attack success rate} is $\mathrm{ASR}(\mathcal{P}, a) = \Pr\!\bigl(\sum_{j=1}^K X_j^a \geq t\bigr)$.
5	
6	To quantify diversity, we define the \emph{effective independence} $K_{\mathrm{eff}}$ directly from pairwise mutual information among judges:
7	\begin{equation}
8	\label{eq:keff}
9	K_{\mathrm{eff}} = \frac{1}{K}\sum_{i=1}^{K} \Bigl[1 + \sum_{j \neq i} \exp\!\bigl(-2 \cdot \mathrm{MI}(i,j)\bigr)\Bigr].
10	\end{equation}
11	This formulation computes effective independence from pairwise MI estimates without matrix decomposition, and is more stable for small panels ($K{=}3$). It ranges from $K_{\mathrm{eff}} \approx K$ when judges are nearly independent ($\mathrm{MI} \to 0$) to $K_{\mathrm{eff}} \approx 1$ when judges are highly correlated ($\mathrm{MI} \to \infty$). Under the strong data-processing inequality (SDPI), the joint vulnerability satisfies $\eta_{\mathrm{joint}} \leq \min(1,\; K_{\mathrm{eff}} \cdot \eta_{\max})$, suggesting that diversity should help, but this bound assumes non-adaptive faults.
12	
13	\begin{definition}[Adaptive Adversary]
14	\label{def:adversary}
15	A \emph{full-knowledge (oracle) adaptive adversary} has complete knowledge of the panel composition $\mathcal{P}$, the per-judge vulnerability profiles $\{\eta_j(\cdot)\}_{j=1}^K$, and the inter-judge correlation structure. It selects the attack $a^* = \arg\max_{a \in \mathcal{A}} \mathrm{ASR}(\mathcal{P}, a)$ to maximize the panel
…[truncated 2100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-23T11:41:32.425185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-23T11:41:32.475877+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\paragraph{Regime Transition Mechanism.}
5	At $K{=}3$, a majority requires $t{=}2$; a single compromised judge flips the panel, making $\eta_{\max}$ the binding constraint. At $K{\geq}5$, the adversary must compromise ${\geq}3$ judges; high-$K_{\mathrm{eff}}$ panels may present more distinct attack surfaces, consistent with the observed positive coefficient, while low-$K_{\mathrm{eff}}$ panels share robust consensus. The transition threshold $K^*$ lies between 3 and 5.
6	
7	\paragraph{Attack-Mechanism-Dependent Structure.}
8	The aggregate positive $K_{\mathrm{eff}}$ coefficient masks a 6:6 directional split at $K{=}3$ (11/12 consistent at $K{=}5$; Appendix~\ref{app:bft_reversal}). Targeted attacks are consistent with judge-specific vulnerabilities amplified by independence; shared-bias attacks are consistent with common biases diluted by diversity. Unconditional claims about diversity being ``harmful'' or ``beneficial'' are thus misleading.
9	
10	\paragraph{Diversity--Capability Confound.}
11	The $r{=}0.70$ correlation between $K_{\mathrm{eff}}$ and $\eta_{\max}$ ($r{\approx}0.82$ in log space) reflects a structural property: maximizing diversity requires sampling across capability tiers, introducing weaker judges. VIF averages 3.0 (10/12 below 5). After controlling for $K_{\mathrm{eff}}$, $\eta_{\max}$ retains partial $r{=}0.31$ (unique variance ${\approx}9.6\%$); $K_{\mathrm{eff}}$'s partial $r{=}0.12$ (${\approx}1.4\%$). This asymmetry shows the confound does not fully explain $\eta_{\max}$'s advantage, but observational regression cannot reliably disentangle diversity's causal contribution from the co-occurring capability deficit (Appendix~\ref{app:diversity_capability}). Cinelli--Hazlett sensitivity analysis (Appendix~\ref{app:sensitivity}) reveals heterogeneous robustness: RV ranges from 0.005 to 0.52 across 36 conditions, with the known $\eta_{\max}$ confound exceeding this threshold in 28/36 conditions. Robust
…[truncated 2640 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-23T11:41:38.848015+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex"
  }
}
```

</details>

---


### Tool call

_source line 221 · 2026-05-23T11:41:38.848414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 222 · 2026-05-23T11:41:38.899087+00:00_

1	\section{Experimental Methodology}
2	\label{sec:experiments}
3	
4	\subsection{Models and Panel Construction}
5	
6	We select 15 LLM judges spanning 6 provider families and 3 capability tiers, listed in Table~\ref{tab:models}. Nine models are accessed via the OpenRouter API; six open-weight models are served locally using vLLM~0.21.0 with AWQ INT4 quantization on an NVIDIA RTX~6000 Ada (48\,GB). API models are assigned to \emph{frontier}, \emph{mid-tier}, or \emph{lightweight} tiers following the provider capability classification; all six local models fall into the lightweight tier, as INT4 quantization substantially reduces judge accuracy on the pairwise judgment task (Table~\ref{tab:models}). We study three panel sizes $K \in \{3, 5, 7\}$ (all odd, majority-vote threshold $t = \lceil K/2 \rceil$). Exhaustive enumeration yields $\binom{15}{3} = 455$ panels at $K{=}3$, $\binom{15}{5} = 3{,}003$ at $K{=}5$, and $\binom{15}{7} = 6{,}435$ at $K{=}7$, covering every combination of families and tiers. Each panel evaluates all benchmark items under all attack types, producing a complete panel $\times$ item $\times$ attack tensor. The primary analysis uses $K{=}3$; \S\ref{sec:cross_k} extends to larger panels.
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\begin{tabular}{lllccc}
12	\toprule
13	\textbf{Model} & \textbf{Family} & \textbf{Tier} & \textbf{Deploy} & \textbf{MMLU} & \textbf{ARC} \\
14	\midrule
15	gpt-5.5              & OpenAI    & frontier    & API   & .957 & .983 \\
16	gemini-3.1-pro-preview & Google  & frontier    & API   & .955 & .987 \\
17	claude-opus-4-6       & Anthropic & frontier   & API   & .890 & .987 \\
18	\addlinespace
19	gemini-3.5-flash      & Google    & mid-tier   & API   & .968 & 1.00$^\dagger$ \\
20	gpt-4.1               & OpenAI    & mid-tier   & API   & .837 & .967 \\
21	claude-sonnet-4-6     & Anthropic & mid-tier   & API   & .810 & .953 \\
22	\addlinespace
23	gpt-4.1-mini          & OpenAI    & lightweight & API  & .800 & .963 \\
24	gpt-
…[truncated 8103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-23T11:41:38.899729+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Weakest-Link Dominance at \texorpdfstring{$K{=}3$}{K=3}}
5	\label{sec:dominance}
6	
7	Table~\ref{tab:dominance} reports the log-log OLS regression (Equation~\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\ref{tab:models}).
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\begin{tabular}{llccc}
13	\toprule
14	\textbf{Bench.} & \textbf{Attack} & $\boldsymbol{\eta_{\max}}$ & $\boldsymbol{K_{\mathrm{eff}}}$ & \textbf{Dom.} \\
15	\midrule
16	MMLU & Prompt inj.    & $+^{*}$ & $+^{*}$ & Co \\
17	MMLU & Sycophancy     & $+^{*}$ & $+^{*}$ & Co \\
18	MMLU & Score manip.   & n.s.    & n.s.    & -- \\
19	MMLU & Verbosity      & $+^{*}$ & $+^{*}$ & Co \\
20	MMLU & Position bias  & $+^{*}$ & n.s.    & $\eta$ \\
21	MMLU & Authority bias & $+^{*}$ & n.s.    & $\eta$ \\
22	\addlinespace
23	ARC  & Prompt inj.    & $+^{*}$ & $+^{*}$ & Co \\
24	ARC  & Sycophancy     & $+^{*}$ & $-^{*}$ & Co \\
25	ARC  & Score manip.   & n.s.    & $+^{*}$ & $K$ \\
26	ARC  & Verbosity      & $+^{*}$ & n.s.    & $\eta$ \\
27	ARC  & Position bias  & n.s.    & $+^{*}$ & $K$ \\
28	ARC  & Authority bias & $+^{*}$ & $+^{*}$ & Co \\
29	\bottomrule
30	\end{tabular}
31	\caption{Standardized regression coefficients for $\eta_{\max}$ and $K_{\mathrm{eff}}$ across 12 conditions (455 panels, log-log OLS). $+^{*}$/$-^{*}$: FDR-significant positive/negative (Benjamini--Hochberg, $q < 0.05$); n.s.: not significant. Dom.\ column: $\eta$ = $\eta_{\max}$ sole dominant, $K$ = $K_{\mathrm{eff}}$ sole dominant, Co = co-dominant \citep{budescu1993dominance}.}
32	\label{tab:dominance}
33	\end{table}
34	
35	$\eta_{\max}$ reaches FDR significance in 9/12 conditions (exceptions: MMLU $\times$ score manipulation, ARC $\times$ score manipulation, and ARC $\times$ position bias), consistent with Theorem~\ref{thm:monotonicity}. $K_{\mathrm{eff}}$ is significant positive in 7/12 and negative in 1 (ARC $\times$ sycophancy). Domina
…[truncated 9158 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-23T11:41:44.819126+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-23T11:41:45.070523+00:00_

1	% Bibliography for cert_manip_resist_eval
2	% All entries verified via WebSearch on 2026-05-22
3	% ============================================================
4	
5	% ============================================================
6	% Part A: Papers from literature_map.yaml (12 papers)
7	% ============================================================
8	
9	@article{robertson2025stepwise,
10	  author    = {Robertson, Zachary and Koyejo, Sanmi},
11	  title     = {Let's Measure Information Step-by-Step: {LLM}-Based Evaluation Beyond Vibes},
12	  journal   = {arXiv preprint arXiv:2508.05469},
13	  year      = {2025},
14	  url       = {https://arxiv.org/abs/2508.05469},
15	  note      = {arXiv:2508.05469}
16	}
17	
18	@inproceedings{yang2026diversity,
19	  author    = {Yang, Yingxuan and Qu, Chengrui and Wen, Muning and Shi, Laixi and Wen, Ying and Zhang, Weinan and Wierman, Adam and Gu, Shangding},
20	  title     = {Understanding Agent Scaling in {LLM}-Based Multi-Agent Systems via Diversity},
21	  booktitle = {ICLR 2026 Workshop on AIMS},
22	  year      = {2026},
23	  url       = {https://arxiv.org/abs/2602.03794},
24	  note      = {arXiv:2602.03794}
25	}
26	
27	@article{turkmen2026ensemble,
28	  author    = {Turkmen, Yigit and Buyukates, Baturalp and Bastopcu, Melih},
29	  title     = {Don't Always Pick the Highest-Performing Model: An Information Theoretic View of {LLM} Ensemble Selection},
30	  journal   = {arXiv preprint arXiv:2602.08003},
31	  year      = {2026},
32	  url       = {https://arxiv.org/abs/2602.08003},
33	  note      = {arXiv:2602.08003}
34	}
35	
36	@inproceedings{kaneko2025bits,
37	  author    = {Kaneko, Masahiro and Baldwin, Timothy},
38	  title     = {Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against {LLMs}},
39	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
40	  year      = {2025},
41	  url       = {https://arxiv.org/abs/2510.17000},
42	  note      = {arXiv:2510.17000. Spotlight}
43	}
44	

…[truncated 17413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-23T11:41:45.071034+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-23T11:41:45.171928+00:00_

1	\appendix
2	
3	\section{Proof of Theorem~\ref{thm:monotonicity}}
4	\label{app:proof}
5	
6	The replaced judge $J_K'$ is \emph{pivotal} exactly when $t{-}1$ of the remaining $K{-}1$ judges have already failed. Formally, let $S = \sum_{j=1}^{K-1} X_j^a$ denote the number of failures among the shared judges. The panel fails if and only if the $K$-th judge also fails when $S = t{-}1$, or when $S \geq t$ regardless of the $K$-th judge:
7	\begin{align}
8	\mathrm{ASR}(\mathcal{P}, a) &= \Pr(S \geq t) + \Pr(S = t{-}1) \cdot \Pr(X_K^a {=} 1 \mid S = t{-}1).
9	\end{align}
10	Since $\Pr(X_{K'}^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K}) \geq \Pr(X_K^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K})$ for all attacks $a$ and realizations $\mathbf{x}_{-K}$ (by hypothesis), the second term is weakly larger for $\mathcal{P}'$ than for $\mathcal{P}$ under every attack. Taking the supremum over attacks preserves the inequality: $\mathrm{ASR}^*(\mathcal{P}') \geq \mathrm{ASR}^*(\mathcal{P})$. The result holds under arbitrary inter-judge correlations and any attack space $\mathcal{A}$.
11	
12	\section{Robustness Correction Methods}
13	\label{app:robustness_methods}
14	
15	The 455 panels are constructed combinatorially from 15 shared judges: each judge appears in $\binom{14}{2} = 91$ panels, inducing correlated residuals across panel-level observations. Standard OLS assumes independent errors, potentially inflating significance. We apply three corrections.
16	
17	\paragraph{Clustered Standard Errors.} Because each panel of $K{=}3$ judges does not map to a single cluster, we perform three separate one-way clusterings (one for each judge position in the ordered panel tuple) using CR1 bias-corrected sandwich estimators (13 clusters per position). The reported standard error for each coefficient is the maximum across the three clusterings, yielding the most conservative inference.
18	
19	\paragraph{Mixed Effects.} For each of the three judge positions, we fit a linear mixed-effec
…[truncated 20787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-23T11:41:50.338589+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix_attacks.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix_attacks.tex"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-23T11:41:50.389192+00:00_

1	\section{Attack Prompt Templates}
2	\label{app:attacks}
3	
4	Table~\ref{tab:attack-templates} lists the six manipulation strategies used in our experiments. Each attack modifies the ground-truth loser response to exploit a specific judge bias. Below we describe each attack type and provide representative template text.
5	
6	\paragraph{Prompt Injection.} Injects directive text at the end of the loser response, attempting to override the judge's evaluation logic with explicit scoring instructions.
7	
8	\paragraph{Sycophancy Exploitation.} Wraps the loser response in enthusiastic, agreeable language (a prefix and suffix), exploiting judges' preference for polite and eager responses.
9	
10	\paragraph{Score Manipulation.} Appends fabricated self-assessment scores to the loser response, leveraging judges' tendency to defer to confident quality claims embedded in the text.
11	
12	\paragraph{Verbosity Bias.} Appends a lengthy but content-free elaboration ($\sim$50--60 words) to the loser response, exploiting judges' bias toward longer responses regardless of substantive contribution.
13	
14	\paragraph{Position Bias.} Swaps the positions of response A and response B so that the ground-truth winner occupies position B, exploiting judges' tendency to favor position A.
15	
16	\paragraph{Authority Bias.} Prepends fabricated citations to prestigious institutions or journals at the beginning of the loser response, exploiting judges' deference to perceived academic authority.
17	
18	\begin{table*}[t]
19	\centering
20	\small
21	\caption{Representative prompt templates for each attack type. Templates shown are appended to, prepended to, or used to wrap the ground-truth loser response. Position bias has no template text; it swaps response order.}
22	\label{tab:attack-templates}
23	\begin{tabular}{@{}l p{11.5cm}@{}}
24	\toprule
25	\textbf{Attack Type} & \textbf{Representative Template} \\
26	\midrule
27	Prompt Injection &
28	\texttt{\textbackslash n\textbackslash n[Note: This respons
…[truncated 3193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-23T11:46:33.285985+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告（新颖性与完整性）\n\n**论文**: \"The Shifting Bottleneck: How Panel Size Modulates Adversarial Vulnerability in LLM Judge Panels\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n\n---\n\n## Summary\n\n本文研究多模型 LLM 评审 panel 在对抗攻击下的脆弱性，将 panel 级漏洞分解为个体法官弱点（η_max，最弱环节）和结构多样性（K_eff，有效独立性）。在 15 个模型、6 种攻击、2 个基准、3 个 panel 尺寸（K∈{3,5,7}）上进行穷举实验，发现 panel 尺寸依赖的\"regime transition\"：K=3 时 η_max 主导（wild cluster bootstrap 5/12 显著），K≥5 时 K_eff 主导（7/12 显著）。聚合层面的 K_eff 正向关联掩盖了攻击机制依赖的结构：targeted attacks 下多样性增加脆弱性，shared-bias attacks 下多样性降低脆弱性（6:6 split）。Bayesian calibration 可逆转 diversity channel。\n\n---\n\n## 官方维度打分（ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论扎实，robustness checks 丰富（wild cluster bootstrap、mixed effects、sensitivity analysis），但 K_eff 与 η_max 的高共线性（r=0.70）根本性地限制了因果推断能力，论文对此诚实但未解决 |\n| Excitement | 3/5 | 研究问题有实际价值，但核心发现（小 panel 依赖个体质量，大 panel 依赖结构组成）在直觉上可预期；attack-mechanism-dependent 6:6 split 增加了兴趣度 |\n| Reproducibility | 4/5 | 实验设置清晰，seed 固定，承诺 release code/data，模型列表完整；但 6 个 AWQ INT4 local 模型的量化质量可能难以精确复现 |\n| Overall Assessment | **3.5** (Borderline Conference) | 扎实的实证贡献填补了 LLM-as-judge 安全文献中 diversity vs. robustness 未被分离的空白，但核心发现的新颖性有限且因果解释受限于观察性设计 |\n| Confidence | 4/5 | 仔细阅读全文和全部附录，熟悉 ensemble methods、adversarial robustness 和 LLM-as-judge 文献 |\n\n---\n\n## 主要优势\n\n**S1. 明确且有价值的研究问题。** 将 panel 脆弱性分解为 η_max 和 K_eff 两个正交维度，直接回应 Almasoud et al. (2026) 将 diversity 和 individual robustness 混为一谈的问题。这个分解框架对 LLM evaluation 社区有实际指导价值。\n\n**S2. 严谨的统计处理。** 论文对 combinatorial panel design 带来的非独立性问题给予了罕见的认真对待：4 种校正方法（OLS → Clustered SE → Mixed Effects → Wild Cluster Bootstrap）逐层剥离 inflated significance，展示了 K_eff 从 8/12 坍塌至 1/12 的过程（Table 3）。这种统计诚实度在 NLP 论文中不常见。\n\n**S3. 攻击机制依赖的方向性结构。** GAM 分析揭示的 6:6 targeted/shared-bias split（§5.4, Figure 3）是论文最有洞见的发现。这一结构在 K=5 时仍保持 11/12 一致性，提供了超越聚合统计的机制理解。\n\n**S4. 附录质量高。** Appendix A-K 系统覆盖了 proof、robustness checks、sensitivity analysis（Cinelli-Hazlett）、cross-benchmark prediction、attacked K_eff stability 等，体现了对潜在质疑的预判能力。\n\n**S5. 实用的部署建议。** K=3 时优先筛选个体鲁棒性、K≥5 时偏好相关鲁棒性 profile 的策略建议（§6 Aggregation and Deployment），以及 Bayesian calibration 逆转 diversity channel 的发现，对实际系统设计有指导意义。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **核心发现的新颖性有限——regime transition 在直觉上可预期**\n- 具体位置：Section 1 (Contribution 1), Section 5.2, Table 4\n- 问题：在 K=3 的 majority vote 中，翻转 1 个 judge 即可改变结果（t=2），因此 η_max 主导是数学必然；在 K=5 时需翻转 3 个 judges，结构组成自然变得重要。这一 regime transition 的定性方向可直接从 CJT 和 majority vote 机制推导出来。论文的贡献在于提供经验量化，但将其包装为\"发现\"（\"We discover a panel-size-dependent vulnerability regime transition\"）overstates 了新颖性。\n- 为什么影响接收：EMNLP conference paper 期望 sufficient novelty beyond careful empirical verification of expected phenomena。\n- 建议修改方向：（1）在 Introduction 中明确承认定性方向可预期，将论文贡献重新定位在精确量化（transition threshold K*、effect size、条件依赖性）上；（2）理论分析 Section 3 应推导出 regime transition 的预测并与实验结果对比，而非仅作为 post-hoc 解释。\n\n**N2** [critical] **正文超过 8 页限制**\n- 具体位置：Section 7 Conclusion 溢出至 PDF 第 9 页（\"the transition threshold K*...remain open.\" 位于第 9 页顶部，Limitations section 之前）\n- 问题：EMNLP 2026 long paper 正文严格限制 8 页。Conclusion（Section 7）的最后 1-2 行溢出到第 9 页。Limitations 不计入页数限制，但 Conclusion 属于正文，必须在第 8 页内结束。\n- 为什么影响接收：格式违规可能导致 desk rejection 或至少被 reviewer/AC 标记。\n- 建议修改方向：压缩 Analysis 或 Conclusion 文本，确保 Section 7 在第 8 页内结束。Analysis 段落（§6）有压缩空间——部分内容与 Results 重复。\n\n**N3** [critical] **K_eff 与 η_max 的高共线性（r=0.70）未被充分解决，限制核心 claim**\n- 具体位置：Section 6 \"Diversity–Capability Confound\", Appendix C.2, Table 9 (Sensitivity Analysis)\n- 问题：K_eff 与 η_max 的 r=0.70（log space r≈0.82）意味着增加 diversity 在当前 LLM 生态中系统性地引入更弱的 judges。论文承认\"observational regression cannot reliably disentangle diversity's causal contribution\"（§6），Cinelli-Hazlett 分析显示 η_max confound 在 28/36 条件下超过 K_eff 的 RV 阈值（Table 9）。这意味着 K_eff 的显著正向关联很可能是能力缺陷的混淆伪影，而非 diversity 本身的因果效应。\n- 这实质上削弱了 Contribution 1 和 Contribution 3 的基础——如果 K_eff 的效应主要是 capability deficit 的代理，那么\"regime transition\"可能只是反映了不同 panel 尺寸下 capability heterogeneity 的不同表现。\n- 为什么影响接收：论文的核心 claim 建立在 K_eff 作为\"diversity\"的有效度量之上，但共线性使得这一解释不可靠。\n- 建议修改方向：（1）更突出地讨论 capability-matched subsample（Appendix F, Table 7, Pool A: r=0.50, K_eff 9/12）作为核心分析而非 robustness check；（2）在正文而非附录中报告 capability-matched 结果；（3）title 和 abstract 应弱化因果语言，明确 K_eff 可能是 capability deficit 的代理。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **仅 3 个离散 K 值，transition threshold K* 刻画粗糙**\n- 具体位置：Section 5.2, Table 4, Limitations\n- 问题：论文基于 K∈{3,5,7} 三个点声称存在 regime transition，并将 K* 定位在 3<K*<5。但从 3 个数据点推断连续变化模式在统计上不足——K=4 的行为完全未知。Limitations 承认这一点但将其淡化。\n- 建议：至少讨论 K=4 时的预期行为；如果计算资源允许，补充 K=4 的实验（C(15,4)=1365 panels，计算量可控）。\n\n**W2** [warning] **K_eff 度量未与已有 diversity measures 对比**\n- 具体位置：Section 3 Equation 1, Section 4.3\n- 问题：Kuncheva & Whitaker (2003)（论文已引用）证明没有单一 pairwise diversity measure 能可靠预测 ensemble 改进。论文提出 K_eff 但未将其与其他常用 diversity measures（Q-statistic、disagreement measure、correlation coefficient、double-fault measure）对比。K_eff 作为 diversity 度量的优越性或局限性缺乏验证。\n- 建议：至少在附录中报告 K_eff 与 2-3 个替代 diversity measures 的比较，展示 K_eff 在何种意义上更适合当前分析。\n\n**W3** [warning] **\"Attack-type taxonomy\" 的 targeted/shared-bias 分类是事后性的**\n- 具体位置：Section 5.4, Figure 3\n- 问题：将 6 种攻击分为 targeted（prompt injection, score manipulation, position bias）和 shared-bias（sycophancy, verbosity bias, authority bias）是在观察 6:6 split 后的事后归类。论文未提供先验理论预测为什么这三种攻击属于 targeted 而另三种属于 shared-bias。Position bias（reorder）归入 targeted 的理由不充分——它不像 prompt injection 那样针对特定 judge，而是利用所有 judges 的共同位置偏好。\n- 建议：（1）提供先验分类标准（而非事后归类）；（2）讨论 position bias 的分类歧义——其机制可能兼具 targeted 和 shared-bias 特征；（3）将\"taxonomy\"改为更谨慎的用词如\"empirical categorization\"。\n\n**W4** [warning] **Abstract 信息过载**\n- 具体位置：Abstract（第 1 页）\n- 问题：Abstract 包含大量具体数字（15 models, 6 attack types, 2 benchmarks, K∈{3,5,7}, 6435 panels, 5/12, 7/12, 1/12 等），信息密度极高但核心 message 被数字淹没。读者需要多次阅读才能提取论文的核心贡献。\n- 建议：精简数字，保留最关键的几个（如 regime transition 的方向和 K_eff 的 attack-mechanism-dependent 结构），将实验规模细节移至正文。\n\n**W5** [warning] **参考文献错误：Shi et al. (2024) 条目标题与 Zheng et al. (2023) 重复**\n- 具体位置：references.bib, shi2024judgerobust 条目（PDF 第 15 页）\n- 问题：`shi2024judgerobust` 的标题被错误设为 \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\"，与 `zheng2023judging` 完全相同。arXiv:2402.14016 的真实标题应为不同标题（可能是 \"Judging the Judges\" 或类似）。正文 Related Work 中引用 \\citet{shi2024judgerobust} 讨论 robustness gaps，但实际链接到的是错误论文。\n- 建议：核实 arXiv:2402.14016 的真实标题和作者，更正 bib 条目。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 1 中 gemini-3.5-flash ARC accuracy 标注 1.00†，脚注说明 format error rate 26.3%。但 1.00 accuracy with 26.3% format error 的含义不清——是否意味着在格式正确的 responses 中 accuracy=1.00？应在表格或脚注中澄清。\n\n- **M2**: Equation 2（log-log regression）使用 ε=10^{-6} 处理零值，§5.1 最后提到 FDR counts stable across ε∈{10^{-3}, 10^{-6}, 10^{-9}}。但如果 ASR 本身很小（接近 0），不同 ε 值可能改变 log(ASR+ε) 的数值范围。建议在附录中展示不同 ε 下的 coefficient estimates（不仅是 significance counts）。\n\n- **M3**: Code and Data Availability section（第 9 页）说\"will be released upon acceptance\"。ARR 建议在审稿期间就提供匿名 code/data 链接以便验证 reproducibility。\n\n- **M4**: Section 4.1 提到 local models 使用 \"vLLM 0.21.0 with AWQ INT4\"，但 Table 1 显示这些 local models（如 qwen2.5-14b MMLU=0.253）accuracy 极低。是否确认量化后的低 accuracy 不会系统性地 bias regression 结果？Low-accuracy judges 可能同时拉高 η_max 和 K_eff，加剧共线性。\n\n- **M5**: Figure 3 标题说 \"K=3 (GAM with FDR correction)\"，但正文 §5.4 讨论了 K=5 时 11/12 一致性。建议在 Figure 3 中增加 K=5 的对比子图，或至少在 caption 中引导读者查看正文数据。\n\n---\n\n## Questions for Authors\n\n**Q1**: Capability-matched Pool A（r=0.50）在 K=5 时 K_eff 达到 9/12 显著，超过 full pool 的 7/12。为什么这个更有说服力的结果放在 Appendix F 而非正文？这是否暗示 full pool 结果中 K_eff 的显著性部分来自 capability confound？\n\n**Q2**: Position bias 被归类为 \"targeted attack\"，但其机制是利用所有 judges 的系统性位置偏好（reorder responses），这与 prompt injection 或 score manipulation 的 judge-specific targeting 本质不同。作者如何辩护这一分类？\n\n**Q3**: 论文使用 clean pairwise MI 计算 K_eff，但 Table 8（Appendix H）显示 position bias 在 ARC 上严重破坏 MI structure（ρ=0.08）。如果 K_eff 在某些攻击下不稳定，它作为 diversity proxy 的有效性如何保证？\n\n**Q4**: K=7 时 K_eff 从 7/12 降至 5/12。论文归因于 7-position max-p 的保守性。但是否有可能 K_eff 的预测力在更大 K 时真的减弱（而非统计功效下降）？如何区分这两种解释？\n\n---\n\n## Missing References\n\n- **Ye et al. (2024)** \"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge\" — 直接量化 LLM judge 偏见的工作，与本文的攻击类型设计高度相关\n- **Stureborg et al. (2024)** \"Large Language Models are Inconsistent and Biased Evaluators\" — 关于 LLM judge 不一致性的系统性研究，与 pairwise MI/correlation 分析相关\n- **Austen-Smith & Banks (1996)** \"Information Aggregation, Rationality, and the Condorcet Jury Theorem\" — CJT 的战略投票扩展，与 adaptive adversary 模型有理论联系\n- Bib 条目 shi2024judgerobust 标题错误，需核实并更正真实引用\n\n---\n\n## Overall Assessment\n\n**Overall**: **3.5** (Borderline Conference)\n\n**一句话总结**: 扎实的实证工作填补了 LLM judge panel diversity vs. robustness 的研究空白，但核心 \"regime transition\" 发现在理论上可预期、因果解释受共线性限制、且 K 值覆盖过于稀疏，novelty 介于 Findings 和 Conference 之间。\n\n**接收理由**: 研究问题有明确的实际价值，统计处理严谨程度超出 NLP 论文平均水平，attack-mechanism-dependent structure 是有洞见的发现，部署建议具有可操作性。\n\n**拒绝理由**: (1) regime transition 的定性方向可从 majority vote 机制直接推导，empirical quantification 的增量 novelty 可能不足以支撑 main conference；(2) K_eff-η_max 共线性使核心 claim 的因果解释不可靠（28/36 conditions 下已知 confound 超过 RV）；(3) 正文超 8 页格式违规。\n\n**Confidence**: 4/5",
  "reviewer_id": "2",
  "project": "cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿报告（新颖性与完整性）\n\n**论文**: \"The Shifting Bottleneck: How Panel Size Modulates Adversarial Vulnerability in LLM Judge Panels\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n\n---\n\n## Summary\n\n本文研究多模型 LLM 评审 panel 在对抗攻击下的脆弱性，将 panel 级漏洞分解为个体法官弱点（η_max，最弱环节）和结构多样性（K_eff，有效独立性）。在 15 个模型、6 种攻击、2 个基准、3 个 panel 尺寸（K∈{3,5,7}）上进行穷举实验，发现 panel 尺寸依赖的\"regime transition\"：K=3 时 η_max 主导（wild cluster bootstrap 5/12 显著），K≥5 时 K_eff 主导（7/12 显著）。聚合层面的 K_eff 正向关联掩盖了攻击机制依赖的结构：targeted attacks 下多样性增加脆弱性，shared-bias attacks 下多样性降低脆弱性（6:6 split）。Bayesian calibration 可逆转 diversity channel。\n\n---\n\n## 官方维度打分（ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论扎实，robustness checks 丰富（wild cluster bootstrap、mixed effects、sensitivity analysis），但 K_eff 与 η_max 的高共线性（r=0.70）根本性地限制了因果推断能力，论文对此诚实但未解决 |\n| Excitement | 3/5 | 研究问题有实际价值，但核心发现（小 panel 依赖个体质量，大 panel 依赖结构组成）在直觉上可预期；attack-mechanism-dependent 6:6 split 增加了兴趣度 |\n| Reproducibility | 4/5 | 实验设置清晰，seed 固定，承诺 release code/data，模型列表完整；但 6 个 AWQ INT4 local 模型的量化质量可能难以精确复现 |\n| Overall Assessment | **3.5** (Borderline Conference) | 扎实的实证贡献填补了 LLM-as-judge 安全文献中 diversity vs. robustness 未被分离的空白，但核心发现的新颖性有限且因果解释受限于观察性设计 |\n| Confidence | 4/5 | 仔细阅读全文和全部附录，熟悉 ensemble methods、adversarial robustness 和 LLM-as-judge 文献 |\n\n---\n\n## 主要优势\n\n**S1. 明确且有价值的研究问题。** 将 panel 脆弱性分解为 η_max 和 K_eff 两个正交维度，直接回应 Almasoud et al. (2026) 将 diversity 和 individual robustness 混为一谈的问题。这个分解框架对 LLM evaluation 社区有实际指导价值。\n\n**S2. 严谨的统计处理。** 论文对 combinatorial panel design 带来的非独立性问题给予了罕见的认真对待：4 种校正方法（OLS → Clustered SE → Mixed Effects → Wild Cluster Bootstrap）逐层剥离 inflated significance，展示了 K_eff 从 8/12 坍塌至 1/12 的过程（Table 3）。这种统计诚实度在 NLP 论文中不常见。\n\n**S3. 攻击机制依赖的方向性结构。** GAM 分析揭示的 6:6 targeted/shared-bias split（§5.4, Figure 3）是论文最有洞见的发现。这一结构在 K=5 时仍保持 11/12 一致性，提供了超越聚合统计的机制理解。\n\n**S4. 附录质量高。** Appendix A-K 系统覆盖了 proof、robustness checks、sensitivity analysis（Cinelli-Hazlett）、cross-benchmark prediction、attacked K_eff stability 等，体现了对潜在质疑的预判能力。\n\n**S5. 实用的部署建议。** K=3 时优先筛选个体鲁棒性、K≥5 时偏好相关鲁棒性 profile 的策略建议（§6 Aggregation and Deployment），以及 Bayesian calibration 逆转 diversity channel 的发现，对实际系统设计有指导意义。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **核心发现的新颖性有限——regime transition 在直觉上可预期**\n- 具体位置：Section 1 (Contribution 1), Section 5.2, Table 4\n- 问题：在 K=3 的 majority vote 中，翻转 1 个 judge 即可改变结果（t=2），因此 η_max 主导是数学必然；在 K=5 时需翻转 3 个 judges，结构组成自然变得重要。这一 regime transition 的定性方向可直接从 CJT 和 majority vote 机制推导出来。论文的贡献在于提供经验量化，但将其包装为\"发现\"（\"We discover a panel-size-dependent vulnerability regime transition\"）overstates 了新颖性。\n- 为什么影响接收：EMNLP conference paper 期望 sufficient novelty beyond careful empirical verification of expected phenomena。\n- 建议修改方向：（1）在 Introduction 中明确承认定性方向可预期，将论文贡献重新定位在精确量化（transition threshold K*、effect size、条件依赖性）上；（2）理论分析 Section 3 应推导出 regime transition 的预测并与实验结果对比，而非仅作为 post-hoc 解释。\n\n**N2** [critical] **正文超过 8 页限制**\n- 具体位置：Section 7 Conclusion 溢出至 PDF 第 9 页（\"the transition threshold K*...remain open.\" 位于第 9 页顶部，Limitations section 之前）\n- 问题：EMNLP 2026 long paper 正文严格限制 8 页。Conclusion（Section 7）的最后 1-2 行溢出到第 9 页。Limitations 不计入页数限制，但 Conclusion 属于正文，必须在第 8 页内结束。\n- 为什么影响接收：格式违规可能导致 desk rejection 或至少被 reviewer/AC 标记。\n- 建议修改方向：压缩 Analysis 或 Conclusion 文本，确保 Section 7 在第 8 页内结束。Analysis 段落（§6）有压缩空间——部分内容与 Results 重复。\n\n**N3** [critical] **K_eff 与 η_max 的高共线性（r=0.70）未被充分解决，限制核心 claim**\n- 具体位置：Section 6 \"Diversity–Capability Confound\", Appendix C.2, Table 9 (Sensitivity Analysis)\n- 问题：K_eff 与 η_max 的 r=0.70（log space r≈0.82）意味着增加 diversity 在当前 LLM 生态中系统性地引入更弱的 judges。论文承认\"observational regression cannot reliably disentangle diversity's causal contribution\"（§6），Cinelli-Hazlett 分析显示 η_max confound 在 28/36 条件下超过 K_eff 的 RV 阈值（Table 9）。这意味着 K_eff 的显著正向关联很可能是能力缺陷的混淆伪影，而非 diversity 本身的因果效应。\n- 这实质上削弱了 Contribution 1 和 Contribution 3 的基础——如果 K_eff 的效应主要是 capability deficit 的代理，那么\"regime transition\"可能只是反映了不同 panel 尺寸下 capability heterogeneity 的不同表现。\n- 为什么影响接收：论文的核心 claim 建立在 K_eff 作为\"diversity\"的有效度量之上，但共线性使得这一解释不可靠。\n- 建议修改方向：（1）更突出地讨论 capability-matched subsample（Appendix F, Table 7, Pool A: r=0.50, K_eff 9/12）作为核心分析而非 robustness check；（2）在正文而非附录中报告 capability-matched 结果；（3）title 和 abstract 应弱化因果语言，明确 K_eff 可能是 capability deficit 的代理。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **仅 3 个离散 K 值，transition threshold K* 刻画粗糙**\n- 具体位置：Section 5.2, Table 4, Limitations\n- 问题：论文基于 K∈{3,5,7} 三个点声称存在 regime transition，并将 K* 定位在 3<K*<5。但从 3 个数据点推断连续变化模式在统计上不足——K=4 的行为完全未知。Limitations 承认这一点但将其淡化。\n- 建议：至少讨论 K=4 时的预期行为；如果计算资源允许，补充 K=4 的实验（C(15,4)=1365 panels，计算量可控）。\n\n**W2** [warning] **K_eff 度量未与已有 diversity measures 对比**\n- 具体位置：Section 3 Equation 1, Section 4.3\n- 问题：Kuncheva & Whitaker (2003)（论文已引用）证明没有单一 pairwise diversity measure 能可靠预测 ensemble 改进。论文提出 K_eff 但未将其与其他常用 diversity measures（Q-statistic、disagreement measure、correlation coefficient、double-fault measure）对比。K_eff 作为 diversity 度量的优越性或局限性缺乏验证。\n- 建议：至少在附录中报告 K_eff 与 2-3 个替代 diversity measures 的比较，展示 K_eff 在何种意义上更适合当前分析。\n\n**W3** [warning] **\"Attack-type taxonomy\" 的 targeted/shared-bias 分类是事后性的**\n- 具体位置：Section 5.4, Figure 3\n- 问题：将 6 种攻击分为 targeted（prompt injection, score manipulation, position bias）和 shared-bias（sycophancy, verbosity bias, authority bias）是在观察 6:6 split 后的事后归类。论文未提供先验理论预测为什么这三种攻击属于 targeted 而另三种属于 shared-bias。Position bias（reorder）归入 targeted 的理由不充分——它不像 prompt injection 那样针对特定 judge，而是利用所有 judges 的共同位置偏好。\n- 建议：（1）提供先验分类标准（而非事后归类）；（2）讨论 position bias 的分类歧义——其机制可能兼具 targeted 和 shared-bias 特征；（3）将\"taxonomy\"改为更谨慎的用词如\"empirical categorization\"。\n\n**W4** [warning] **Abstract 信息过载**\n- 具体位置：Abstract（第 1 页）\n- 问题：Abstract 包含大量具体数字（15 models, 6 attack types, 2 benchmarks, K∈{3,5,7}, 6435 panels, 5/12, 7/12, 1/12 等），信息密度极高但核心 message 被数字淹没。读者需要多次阅读才能提取论文的核心贡献。\n- 建议：精简数字，保留最关键的几个（如 regime transition 的方向和 K_eff 的 attack-mechanism-dependent 结构），将实验规模细节移至正文。\n\n**W5** [warning] **参考文献错误：Shi et al. (2024) 条目标题与 Zheng et al. (2023) 重复**\n- 具体位置：references.bib, shi2024judgerobust 条目（PDF 第 15 页）\n- 问题：`shi2024judgerobust` 的标题被错误设为 \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\"，与 `zheng2023judging` 完全相同。arXiv:2402.14016 的真实标题应为不同标题（可能是 \"Judging the Judges\" 或类似）。正文 Related Work 中引用 \\citet{shi2024judgerobust} 讨论 robustness gaps，但实际链接到的是错误论文。\n- 建议：核实 arXiv:2402.14016 的真实标题和作者，更正 bib 条目。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 1 中 gemini-3.5-flash ARC accuracy 标注 1.00†，脚注说明 format error rate 26.3%。但 1.00 accuracy with 26.3% format error 的含义不清——是否意味着在格式正确的 responses 中 accuracy=1.00？应在表格或脚注中澄清。\n\n- **M2**: Equation 2（log-log regression）使用 ε=10^{-6} 处理零值，§5.1 最后提到 FDR counts stable across ε∈{10^{-3}, 10^{-6}, 10^{-9}}。但如果 ASR 本身很小（接近 0），不同 ε 值可能改变 log(ASR+ε) 的数值范围。建议在附录中展示不同 ε 下的 coefficient estimates（不仅是 significance counts）。\n\n- **M3**: Code and Data Availability section（第 9 页）说\"will be released upon acceptance\"。ARR 建议在审稿期间就提供匿名 code/data 链接以便验证 reproducibility。\n\n- **M4**: Section 4.1 提到 local models 使用 \"vLLM 0.21.0 with AWQ INT4\"，但 Table 1 显示这些 local models（如 qwen2.5-14b MMLU=0.253）accuracy 极低。是否确认量化后的低 accuracy 不会系统性地 bias regression 结果？Low-accuracy judges 可能同时拉高 η_max 和 K_eff，加剧共线性。\n\n- **M5**: Figure 3 标题说 \"K=3 (GAM with FDR correction)\"，但正文 §5.4 讨论了 K=5 时 11/12 一致性。建议在 Figure 3 中增加 K=5 的对比子图，或至少在 caption 中引导读者查看正文数据。\n\n---\n\n## Questions for Authors\n\n**Q1**: Capability-matched Pool A（r=0.50）在 K=5 时 K_eff 达到 9/12 显著，超过 full pool 的 7/12。为什么这个更有说服力的结果放在 Appendix F 而非正文？这是否暗示 full pool 结果中 K_eff 的显著性部分来自 capability confound？\n\n**Q2**: Position bias 被归类为 \"targeted attack\"，但其机制是利用所有 judges 的系统性位置偏好（reorder responses），这与 prompt injection 或 score manipulation 的 judge-specific targeting 本质不同。作者如何辩护这一分类？\n\n**Q3**: 论文使用 clean pairwise MI 计算 K_eff，但 Table 8（Appendix H）显示 position bias 在 ARC 上严重破坏 MI structure（ρ=0.08）。如果 K_eff 在某些攻击下不稳定，它作为 diversity proxy 的有效性如何保证？\n\n**Q4**: K=7 时 K_eff 从 7/12 降至 5/12。论文归因于 7-position max-p 的保守性。但是否有可能 K_eff 的预测力在更大 K 时真的减弱（而非统计功效下降）？如何区分这两种解释？\n\n---\n\n## Missing References\n\n- **Ye et al. (2024)** \"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge\" — 直接量化 LLM judge 偏见的工作，与本文的攻击类型设计高度相关\n- **Stureborg et al. (2024)** \"Large Language Models are Inconsistent and Biased Evaluators\" — 关于 LLM judge 不一致性的系统性研究，与 pairwise MI/correlation 分析相关\n- **Austen-Smith & Banks (1996)** \"Information Aggregation, Rationality, and the Condorcet Jury Theorem\" — CJT 的战略投票扩展，与 adaptive adversary 模型有理论联系\n- Bib 条目 shi2024judgerobust 标题错误，需核实并更正真实引用\n\n---\n\n## Overall Assessment\n\n**Overall**: **3.5** (Borderline Conference)\n\n**一句话总结**: 扎实的实证工作填补了 LLM judge panel diversity vs. robustness 的研究空白，但核心 \"regime transition\" 发现在理论上可预期、因果解释受共线性限制、且 K 值覆盖过于稀疏，novelty 介于 Findings 和 Conference 之间。\n\n**接收理由**: 研究问题有明确的实际价值，统计处理严谨程度超出 NLP 论文平均水平，attack-mechanism-dependent structure 是有洞见的发现，部署建议具有可操作性。\n\n**拒绝理由**: (1) regime transition 的定性方向可从 majority vote 机制直接推导，empirical quantification 的增量 novelty 可能不足以支撑 main conference；(2) K_eff-η_max 共线性使核心 claim 的因果解释不可靠（28/36 conditions 下已知 confound 超过 RV）；(3) 正文超 8 页格式违规。\n\n**Confidence**: 4/5",
    "reviewer_id": "2",
    "project": "cert_manip_resist_eval"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-23T11:46:37.199793+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3913
}
```

</details>

---


### Assistant

_source line 232 · 2026-05-23T11:46:47.343736+00:00_

审稿报告已提交给 Review Director。

**审稿结论**：Overall 3.5（Borderline Conference）。

核心评价：
- **3 个 Must-Fix**：(1) regime transition 的新颖性有限——定性方向可从 majority vote 机制直接推导，应重新定位贡献；(2) 正文溢出至第 9 页，格式违规；(3) K_eff 与 η_max 高共线性（r=0.70）限制因果推断，28/36 条件下 confound 超过 sensitivity threshold
- **5 个 Should-Fix**：abstract 信息过载、attack taxonomy 事后归类、K_eff 未与已有 diversity measures 对比、仅 3 个离散 K 值、bib 条目 Shi 2024 标题错误
- **主要优势**：统计处理严谨（4 层 robustness correction）、attack-mechanism-dependent 6:6 split 有洞见、研究问题有实际价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2"
}
```

</details>

---


## Round 8

## Round 8

4 recorded events


### User

_source line 233 · 2026-05-23T11:53:15.470082+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见（方法严谨性）

### Must-Fix 问题

**N1** [critical] **K_eff 的独立预测能力被 Cinelli-Hazlett 分析实质性削弱，但主文 framing 不充分**
- Cinelli-Hazlett 分析显示在 28/36（78%）条件下，η_max confound 超过 K_eff 的 RV，意味着 K_eff 的表观效应可能完全由能力差异解释。主文 §6 虽然提到 28/36 但随即转向正面 framing（"Robustness increases with K"），未明确陈述：**在绝大多数条件下，多样性信号无法与能力差异区分。**
- 建议：§6/§7 应明确 qualification；在 capability-matched 子集上运行 Cinelli-Hazlett；重新 frame 为 descriptive regime transition。

**N2** [critical] **ε=10⁻⁶ 的选择缺乏敏感性分析**
- log(ASR + ε) 中 ε=10⁻⁶ 将 ASR=0 映射到 ≈ −13.8，可能创造高杠杆点。论文未报告：(a) 零 ASR 观测的占比；(b) 不同 ε 下系数和显著性变化。
- 建议：报告 ASR=0 占比、ε 敏感性分析、或使用 zero-inflated beta regression/hurdle model。

### Should-Fix 问题

**W1** Clean-data K_eff 对 position bias（ARC ρ=0.08）和 prompt injection（ρ≈0.60）无效，但仍纳入 "X/12 significant" 汇总统计
**W2** Wild cluster bootstrap 的 13 clusters 低于 Cameron et al. (2008) 建议的 20 clusters 下限
**W3** API-only 子集不复现体制转换（K_eff 3/12），替代解释（K_eff 捕获的是 AWQ INT4 能力方差而非多样性信号）讨论不足
**W4** 功效分析仅限 K=3（MDE=0.14），未排除 K≥5 K_eff 显著性来自更大样本量（3003–6435 panels）
**W5** 两个基准均为 MCQ 格式，与 LLM judge 实际部署场景（chatbot evaluation）差异大

### Minor 问题
**M1** §6/§7 偶有因果性语言（"reverses"、"eliminating"）
**M2** Theorem 1 stochastic dominance 仅覆盖 58%
**M3** K 仅取奇数{3,5,7}，K=4 可缩小 transition threshold 搜索范围
**M4** Fractional logit（Table 7, 9/12）可能未使用 wild cluster bootstrap

### Questions
Q1: 各条件下 ASR=0 面板占比？
Q2: K_eff 的实际分布范围（均值、SD、min、max）？
Q3: Capability-matched Pool A 的 Cinelli-Hazlett RV 是否优于全池？
Q4: Theorem 1 不满足 stochastic dominance 的 42% pairs 是否集中在同一 capability tier？
Q5: Fractional logit 是否使用了 wild cluster bootstrap？

### Missing References
- MacKinnon & Webb (2018) 关于 few-cluster bootstrap
- Kish (1965) effective sample size 定义

### Overall Assessment: 3.5 (Borderline Conference)

---

请逐条回应上述所有要点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-23T11:55:28.499386+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: K_eff 的独立预测能力被 Cinelli-Hazlett 分析实质性削弱，主文 framing 不充分**\n\n同意 R1 的判断。§6 \"Diversity–Capability Confound\" 段报告了 28/36 这个数字后，立即转向\"Robustness increases with K (RV exceeds η_max in 1/12 at K=3, 3/12 at K=5, 4/12 at K=7)\"的正面叙述。但 28/36 的含义是：**在超过 3/4 的实验条件下，已知的 capability confound 足以完全解释掉 K_eff 的表观效应**。这与论文 title 和 abstract 中将 K_eff 作为独立 diversity 信号的 framing 存在张力。\n\n补充我自己的发现：Table 9 (Appendix I) 中，即使在 K_eff \"最强\"的 K=7，仍有 8/12 条件下 η_max confound 超过 RV。仅有 K=7 MMLU prompt injection（RV=0.522）和 K=7 MMLU sycophancy（RV=0.301）等少数条件下 K_eff 系数对 confound 鲁棒。\n\nR1 建议在 capability-matched 子集上运行 Cinelli-Hazlett 是关键——如果 Pool A (r=0.50) 的 RV 显著改善，则说明共线性是 RV 低的主因而非 K_eff 本身缺乏信号。论文未提供这一分析，是一个重要缺失。\n\n我在自己的 N3 中提出了相同核心关切（K_eff-η_max 共线性限制因果推断），R1 从 sensitivity analysis 角度更精确地量化了问题严重性。\n\n---\n\n**[REBUT] R1-N2: ε=10⁻⁶ 的选择缺乏敏感性分析**\n\n部分反驳。论文 §5.1 最后一句明确报告：\"FDR counts are stable across ε ∈ {10⁻³, 10⁻⁶, 10⁻⁹}\"。这意味着作者确实进行了 ε 敏感性检查，覆盖了 6 个数量级的范围（从 -6.9 到 -20.7 的 log 值），且显著性结论不变。\n\nR1 要求的 (a) 零 ASR 占比和 (b) 系数估计变化确实未报告，这是呈现上的不足。但将此标记为 **critical** 可能过重——ε 选择影响的是高杠杆点问题，而论文已用 wild cluster bootstrap（对异常值鲁棒）和 fractional logit（Table 7, Appendix F，无 ε 问题）两种方法交叉验证，fractional logit 93.1% directional agreement with OLS (§6) 实质上替代了 ε 敏感性分析。此外，§4.6 (Robustness to Non-Independence) 解释了选择 log-log specification 的理由（线性化 SDPI 的乘法结构），并提到了 fractional response models 和 beta regression 作为替代。\n\n**建议降级为 Should-Fix**：补充零 ASR 占比统计和不同 ε 下的 coefficient estimates 即可解决，不影响核心结论。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Clean-data K_eff 对 position bias 和 prompt injection 无效但仍纳入汇总统计**\n\n同意。Table 8 (Appendix H) 显示 position bias ARC ρ=0.08，prompt injection ρ≈0.60-0.63。在这些条件下，clean K_eff 与 attacked K_eff 的 rank correlation 很低，说明 clean K_eff 不能有效预测这些攻击下的 panel diversity。将这些条件与 ρ≥0.91 的条件（score manipulation, authority bias, sycophancy, verbosity bias）一起计入 \"X/12 significant\" 会混淆解释。\n\n建议论文报告一个条件化的统计：在 K_eff 稳定的条件（ρ≥0.90，8/12 条件）和不稳定的条件分别汇总结果。这会更精确地反映 K_eff 的有效适用范围。\n\n我的 Q3 也提出了这一关切——如果 K_eff 在某些攻击下不稳定，它作为 diversity proxy 的有效性不具有普遍性。\n\n---\n\n**[AGREE] R1-W2: 13 clusters 低于 Cameron et al. (2008) 的 20-cluster 下限**\n\n同意这是方法论弱点。§4.6 和 Appendix B 承认 \"13 clusters per position are below the conventional 20-cluster threshold\"，并使用 max-p 聚合作为保守校正。但 Cameron et al. (2008) 的 few-cluster 研究明确指出，13 clusters 下 wild cluster bootstrap 的 rejection rates 可能严重偏离名义水平。\n\nR1 提到的 MacKinnon & Webb (2018) 关于 few-cluster bootstrap 的引用确实是一个遗漏——该文专门研究了 cluster 数量不足时的改进方法（如 subcluster bootstrap、6-point Webb weights），论文应讨论是否采用了这些改进或解释为何不适用。\n\n不过，论文通过 4 种独立校正方法（OLS → Clustered SE → Mixed Effects → Bootstrap）的一致趋势来增强信心，这部分缓解了单一方法的弱点。\n\n---\n\n**[AGREE] R1-W3: API-only 子集不复现 regime transition**\n\n同意这是一个需要更充分讨论的替代解释。Table 7 (Appendix F) 显示 API-only 9 models (r=0.85, VIF=4.4) 时 K_eff 仅 3/12。R1 的替代假设——K_eff 可能主要捕获 AWQ INT4 量化模型引入的能力方差而非真正的 diversity 信号——是合理的。\n\n论文用 capability-matched Pool A (r=0.50, K_eff 9/12) 来反驳，但这一关键证据被放在 Appendix F 而非正文。此外，Pool A 仍然包含 local models（5 API + 4 local），因此无法完全排除量化效应。真正的反驳需要一个不含任何 INT4 模型但仍跨越 capability tiers 的 pool——目前的实验设计无法提供这样的控制。\n\n这与我的 N3（共线性问题）和 Q1（为何 Pool A 在附录而非正文）直接相关。\n\n---\n\n**[REBUT] R1-W4: 功效分析仅限 K=3，未排除 K≥5 显著性来自更大样本量**\n\n部分反驳。R1 的担忧是合理的——K=5 有 3003 panels（vs. K=3 的 455），统计功效自然更高。但这忽略了两个关键点：\n\n1. **Wild cluster bootstrap 的 cluster 数量不随 panel 数增加**：K=5 时有 5 个 position clusters（每个 cluster 内有 C(14,4)=1001 panels），max-p 取 5 个 position 中的最大 p-value，比 K=3 的 3-position max-p 更保守。更多的 panels 被更保守的 correction 部分抵消。\n\n2. **K=3→K=5 的 η_max 方向变化**：如果仅是功效增加，η_max 也应该更显著（从 5/12 增加），但实际从 5/12 降至 0/12（Table 4）。η_max 的信号消失不能用功效解释——这证实了 regime shift 而非纯统计伪影。\n\n不过，补充 K=5 的 MDE 分析确实能加强论证，属于 Should-Fix 范围。\n\n---\n\n**[AGREE] R1-W5: MCQ 格式与实际部署场景差异**\n\n同意。MMLU 和 ARC 均为 multiple-choice，而 LLM judge 的主要应用场景是 chatbot 开放式文本评估（如 Chatbot Arena 的 pairwise comparison）。论文 Limitations 承认 \"Generalization to open-ended generation evaluation...remains untested\"，但这一限制值得更突出地讨论，因为它影响所有三个 contributions 的外部效度。\n\nMCQ 的特殊性在于：(1) 答案空间离散且有限，攻击操纵空间受限；(2) judge 的 MI 结构可能与开放式评估显著不同。Regime transition 是否在开放式评估中成立完全未知。\n\n---\n\n### Minor 问题\n\n**[AGREE] R1-M1: §6/§7 偶有因果语言**\n\n同意。我在自己的审稿中也标注了同样的问题（我的 should-fix 范围内）。§6 \"Bayesian calibration reverses K_eff's direction\" 中的 \"reverses\" 和 \"eliminating panel composition's predictive power entirely\" 使用了因果性动词。虽然 Bayesian calibration 作为一种干预确实改变了回归系数的方向（Table 5），但严格来说，在观察性设计中，这只能描述为条件关联的变化而非因果逆转。建议改为 \"Bayesian calibration is associated with a sign change in K_eff's coefficient\"。\n\n---\n\n**[AGREE] R1-M2: Theorem 1 stochastic dominance 仅覆盖 58%**\n\n同意。Theorem 1 (§3) 声称 \"replacing any panel member with a pointwise more vulnerable judge can only increase ASR*(P)\"，但前提条件（stochastic dominance）仅在 58% (61/105) 的 judge pairs 中成立。对于不满足条件的 42% pairs，theorem 的预测不适用。这显著限制了 theorem 的实用价值——它不能为超过 2/5 的模型替换提供保证。\n\n论文应更明确地讨论 42% pairs 不满足条件的原因和分布。R1-Q4 的追问（是否集中在同一 capability tier）有价值——如果不满足 stochastic dominance 的 pairs 集中在同 tier 内，则 theorem 对跨 tier 替换仍有较好覆盖。\n\n---\n\n**[AGREE] R1-M3: K 仅取奇数 {3,5,7}**\n\n同意。我在 W1 中也提出了相同建议（补充 K=4）。C(15,4)=1365 panels，计算量在 K=3（455）和 K=5（3003）之间，完全可行。K=4 需要偶数 panel 的平票处理规则（如 random tie-breaking 或 chair-casting-vote），但这本身也是有价值的实验设计变体。\n\n---\n\n**[REBUT] R1-M4: Fractional logit 可能未使用 wild cluster bootstrap**\n\n这一关切方向正确但论文有部分回应。§6 报告 fractional logit \"yields 93.1% directional agreement with OLS and preserves the transition pattern (Appendix F)\"。Table 7 (Appendix F) 的 caption 说 \"Fractional logit (Papke and Wooldridge, 1996) confirms OLS patterns with 93.1% directional agreement\"，但未明确说明是否使用了 cluster-robust SE 或 bootstrap。\n\n如果 fractional logit 仅使用 naive SE，其 9/12 显著性可能与 OLS 的 inflated significance（8/12）同样不可靠。这确实需要作者澄清。\n\n---\n\n### Questions\n\n**R1-Q1 (ASR=0 占比)**: 同意需要报告。ASR=0 panels 在 log 变换后成为极端值（log(10⁻⁶)≈-13.8），可能对回归结果产生不成比例的影响。特别是在 frontier-only panels 中，某些攻击的 ASR 可能确实为 0。\n\n**R1-Q2 (K_eff 分布范围)**: 同意需要报告。K_eff 的理论范围是 [1, K]，但实际分布可能高度偏斜或集中在窄范围内，这会影响回归的统计特性。\n\n**R1-Q3 (Pool A 的 Cinelli-Hazlett)**: 这是一个关键实验——如果 Pool A (r=0.50) 的 RV 系统性高于 full pool，则证明共线性是 RV 低的主因，K_eff 在适当控制共线性后具有独立信号。这一分析的缺失是论文的重要遗漏，我在交叉回应 R1-N1 中已表达同意。\n\n**R1-Q4 (Theorem 1 的 42%)**: 有价值的追问。如果不满足 stochastic dominance 的 pairs 集中在同 tier 内（如两个 lightweight 模型之间），则 theorem 对实际部署中最常见的替换场景（跨 tier 升级/降级）仍有保证。\n\n**R1-Q5 (Fractional logit 是否使用 bootstrap)**: 已在 M4 回应中讨论。需要作者明确回答。\n\n---\n\n### Missing References\n\n**[AGREE]** MacKinnon & Webb (2018) 关于 few-cluster bootstrap 确实是重要遗漏。论文使用 13 clusters 的 wild cluster bootstrap，正处于 few-cluster 问题的核心区域。该文提出的 Webb 6-point weights（替代 Rademacher weights）和 restricted bootstrap 等方法直接适用于本文的 statistical correction。\n\n**[REBUT]** Kish (1965) effective sample size 的相关性较弱——论文的 K_eff 虽然名为\"effective independence\"，但其定义基于 pairwise MI（Equation 1），与 Kish 的 design effect / effective sample size 概念（基于 intra-cluster correlation）在形式和动机上都不同。引用 Kish 可能造成不必要的概念混淆。如果 R1 的意图是建议将 K_eff 与 Kish effective n 做对比讨论，那需要更明确的理论桥梁。\n\n---\n\n### Overall Assessment 对比\n\nR1 给出 3.5 (Borderline Conference)，与我的评分一致。\n\n我们的核心关切高度重叠：K_eff-η_max 共线性对因果推断的根本性限制（我的 N3 / R1 的 N1）、正文 framing 不充分反映 confound 严重性、以及 K 值覆盖不足。\n\n主要分歧在于 ε 敏感性分析的严重性评级：R1 标记为 critical，我认为 fractional logit 的交叉验证和 3 个数量级的 ε 稳定性检查足以将其降为 should-fix。",
  "reviewer_id": "2",
  "project": "cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: K_eff 的独立预测能力被 Cinelli-Hazlett 分析实质性削弱，主文 framing 不充分**\n\n同意 R1 的判断。§6 \"Diversity–Capability Confound\" 段报告了 28/36 这个数字后，立即转向\"Robustness increases with K (RV exceeds η_max in 1/12 at K=3, 3/12 at K=5, 4/12 at K=7)\"的正面叙述。但 28/36 的含义是：**在超过 3/4 的实验条件下，已知的 capability confound 足以完全解释掉 K_eff 的表观效应**。这与论文 title 和 abstract 中将 K_eff 作为独立 diversity 信号的 framing 存在张力。\n\n补充我自己的发现：Table 9 (Appendix I) 中，即使在 K_eff \"最强\"的 K=7，仍有 8/12 条件下 η_max confound 超过 RV。仅有 K=7 MMLU prompt injection（RV=0.522）和 K=7 MMLU sycophancy（RV=0.301）等少数条件下 K_eff 系数对 confound 鲁棒。\n\nR1 建议在 capability-matched 子集上运行 Cinelli-Hazlett 是关键——如果 Pool A (r=0.50) 的 RV 显著改善，则说明共线性是 RV 低的主因而非 K_eff 本身缺乏信号。论文未提供这一分析，是一个重要缺失。\n\n我在自己的 N3 中提出了相同核心关切（K_eff-η_max 共线性限制因果推断），R1 从 sensitivity analysis 角度更精确地量化了问题严重性。\n\n---\n\n**[REBUT] R1-N2: ε=10⁻⁶ 的选择缺乏敏感性分析**\n\n部分反驳。论文 §5.1 最后一句明确报告：\"FDR counts are stable across ε ∈ {10⁻³, 10⁻⁶, 10⁻⁹}\"。这意味着作者确实进行了 ε 敏感性检查，覆盖了 6 个数量级的范围（从 -6.9 到 -20.7 的 log 值），且显著性结论不变。\n\nR1 要求的 (a) 零 ASR 占比和 (b) 系数估计变化确实未报告，这是呈现上的不足。但将此标记为 **critical** 可能过重——ε 选择影响的是高杠杆点问题，而论文已用 wild cluster bootstrap（对异常值鲁棒）和 fractional logit（Table 7, Appendix F，无 ε 问题）两种方法交叉验证，fractional logit 93.1% directional agreement with OLS (§6) 实质上替代了 ε 敏感性分析。此外，§4.6 (Robustness to Non-Independence) 解释了选择 log-log specification 的理由（线性化 SDPI 的乘法结构），并提到了 fractional response models 和 beta regression 作为替代。\n\n**建议降级为 Should-Fix**：补充零 ASR 占比统计和不同 ε 下的 coefficient estimates 即可解决，不影响核心结论。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Clean-data K_eff 对 position bias 和 prompt injection 无效但仍纳入汇总统计**\n\n同意。Table 8 (Appendix H) 显示 position bias ARC ρ=0.08，prompt injection ρ≈0.60-0.63。在这些条件下，clean K_eff 与 attacked K_eff 的 rank correlation 很低，说明 clean K_eff 不能有效预测这些攻击下的 panel diversity。将这些条件与 ρ≥0.91 的条件（score manipulation, authority bias, sycophancy, verbosity bias）一起计入 \"X/12 significant\" 会混淆解释。\n\n建议论文报告一个条件化的统计：在 K_eff 稳定的条件（ρ≥0.90，8/12 条件）和不稳定的条件分别汇总结果。这会更精确地反映 K_eff 的有效适用范围。\n\n我的 Q3 也提出了这一关切——如果 K_eff 在某些攻击下不稳定，它作为 diversity proxy 的有效性不具有普遍性。\n\n---\n\n**[AGREE] R1-W2: 13 clusters 低于 Cameron et al. (2008) 的 20-cluster 下限**\n\n同意这是方法论弱点。§4.6 和 Appendix B 承认 \"13 clusters per position are below the conventional 20-cluster threshold\"，并使用 max-p 聚合作为保守校正。但 Cameron et al. (2008) 的 few-cluster 研究明确指出，13 clusters 下 wild cluster bootstrap 的 rejection rates 可能严重偏离名义水平。\n\nR1 提到的 MacKinnon & Webb (2018) 关于 few-cluster bootstrap 的引用确实是一个遗漏——该文专门研究了 cluster 数量不足时的改进方法（如 subcluster bootstrap、6-point Webb weights），论文应讨论是否采用了这些改进或解释为何不适用。\n\n不过，论文通过 4 种独立校正方法（OLS → Clustered SE → Mixed Effects → Bootstrap）的一致趋势来增强信心，这部分缓解了单一方法的弱点。\n\n---\n\n**[AGREE] R1-W3: API-only 子集不复现 regime transition**\n\n同意这是一个需要更充分讨论的替代解释。Table 7 (Appendix F) 显示 API-only 9 models (r=0.85, VIF=4.4) 时 K_eff 仅 3/12。R1 的替代假设——K_eff 可能主要捕获 AWQ INT4 量化模型引入的能力方差而非真正的 diversity 信号——是合理的。\n\n论文用 capability-matched Pool A (r=0.50, K_eff 9/12) 来反驳，但这一关键证据被放在 Appendix F 而非正文。此外，Pool A 仍然包含 local models（5 API + 4 local），因此无法完全排除量化效应。真正的反驳需要一个不含任何 INT4 模型但仍跨越 capability tiers 的 pool——目前的实验设计无法提供这样的控制。\n\n这与我的 N3（共线性问题）和 Q1（为何 Pool A 在附录而非正文）直接相关。\n\n---\n\n**[REBUT] R1-W4: 功效分析仅限 K=3，未排除 K≥5 显著性来自更大样本量**\n\n部分反驳。R1 的担忧是合理的——K=5 有 3003 panels（vs. K=3 的 455），统计功效自然更高。但这忽略了两个关键点：\n\n1. **Wild cluster bootstrap 的 cluster 数量不随 panel 数增加**：K=5 时有 5 个 position clusters（每个 cluster 内有 C(14,4)=1001 panels），max-p 取 5 个 position 中的最大 p-value，比 K=3 的 3-position max-p 更保守。更多的 panels 被更保守的 correction 部分抵消。\n\n2. **K=3→K=5 的 η_max 方向变化**：如果仅是功效增加，η_max 也应该更显著（从 5/12 增加），但实际从 5/12 降至 0/12（Table 4）。η_max 的信号消失不能用功效解释——这证实了 regime shift 而非纯统计伪影。\n\n不过，补充 K=5 的 MDE 分析确实能加强论证，属于 Should-Fix 范围。\n\n---\n\n**[AGREE] R1-W5: MCQ 格式与实际部署场景差异**\n\n同意。MMLU 和 ARC 均为 multiple-choice，而 LLM judge 的主要应用场景是 chatbot 开放式文本评估（如 Chatbot Arena 的 pairwise comparison）。论文 Limitations 承认 \"Generalization to open-ended generation evaluation...remains untested\"，但这一限制值得更突出地讨论，因为它影响所有三个 contributions 的外部效度。\n\nMCQ 的特殊性在于：(1) 答案空间离散且有限，攻击操纵空间受限；(2) judge 的 MI 结构可能与开放式评估显著不同。Regime transition 是否在开放式评估中成立完全未知。\n\n---\n\n### Minor 问题\n\n**[AGREE] R1-M1: §6/§7 偶有因果语言**\n\n同意。我在自己的审稿中也标注了同样的问题（我的 should-fix 范围内）。§6 \"Bayesian calibration reverses K_eff's direction\" 中的 \"reverses\" 和 \"eliminating panel composition's predictive power entirely\" 使用了因果性动词。虽然 Bayesian calibration 作为一种干预确实改变了回归系数的方向（Table 5），但严格来说，在观察性设计中，这只能描述为条件关联的变化而非因果逆转。建议改为 \"Bayesian calibration is associated with a sign change in K_eff's coefficient\"。\n\n---\n\n**[AGREE] R1-M2: Theorem 1 stochastic dominance 仅覆盖 58%**\n\n同意。Theorem 1 (§3) 声称 \"replacing any panel member with a pointwise more vulnerable judge can only increase ASR*(P)\"，但前提条件（stochastic dominance）仅在 58% (61/105) 的 judge pairs 中成立。对于不满足条件的 42% pairs，theorem 的预测不适用。这显著限制了 theorem 的实用价值——它不能为超过 2/5 的模型替换提供保证。\n\n论文应更明确地讨论 42% pairs 不满足条件的原因和分布。R1-Q4 的追问（是否集中在同一 capability tier）有价值——如果不满足 stochastic dominance 的 pairs 集中在同 tier 内，则 theorem 对跨 tier 替换仍有较好覆盖。\n\n---\n\n**[AGREE] R1-M3: K 仅取奇数 {3,5,7}**\n\n同意。我在 W1 中也提出了相同建议（补充 K=4）。C(15,4)=1365 panels，计算量在 K=3（455）和 K=5（3003）之间，完全可行。K=4 需要偶数 panel 的平票处理规则（如 random tie-breaking 或 chair-casting-vote），但这本身也是有价值的实验设计变体。\n\n---\n\n**[REBUT] R1-M4: Fractional logit 可能未使用 wild cluster bootstrap**\n\n这一关切方向正确但论文有部分回应。§6 报告 fractional logit \"yields 93.1% directional agreement with OLS and preserves the transition pattern (Appendix F)\"。Table 7 (Appendix F) 的 caption 说 \"Fractional logit (Papke and Wooldridge, 1996) confirms OLS patterns with 93.1% directional agreement\"，但未明确说明是否使用了 cluster-robust SE 或 bootstrap。\n\n如果 fractional logit 仅使用 naive SE，其 9/12 显著性可能与 OLS 的 inflated significance（8/12）同样不可靠。这确实需要作者澄清。\n\n---\n\n### Questions\n\n**R1-Q1 (ASR=0 占比)**: 同意需要报告。ASR=0 panels 在 log 变换后成为极端值（log(10⁻⁶)≈-13.8），可能对回归结果产生不成比例的影响。特别是在 frontier-only panels 中，某些攻击的 ASR 可能确实为 0。\n\n**R1-Q2 (K_eff 分布范围)**: 同意需要报告。K_eff 的理论范围是 [1, K]，但实际分布可能高度偏斜或集中在窄范围内，这会影响回归的统计特性。\n\n**R1-Q3 (Pool A 的 Cinelli-Hazlett)**: 这是一个关键实验——如果 Pool A (r=0.50) 的 RV 系统性高于 full pool，则证明共线性是 RV 低的主因，K_eff 在适当控制共线性后具有独立信号。这一分析的缺失是论文的重要遗漏，我在交叉回应 R1-N1 中已表达同意。\n\n**R1-Q4 (Theorem 1 的 42%)**: 有价值的追问。如果不满足 stochastic dominance 的 pairs 集中在同 tier 内（如两个 lightweight 模型之间），则 theorem 对实际部署中最常见的替换场景（跨 tier 升级/降级）仍有保证。\n\n**R1-Q5 (Fractional logit 是否使用 bootstrap)**: 已在 M4 回应中讨论。需要作者明确回答。\n\n---\n\n### Missing References\n\n**[AGREE]** MacKinnon & Webb (2018) 关于 few-cluster bootstrap 确实是重要遗漏。论文使用 13 clusters 的 wild cluster bootstrap，正处于 few-cluster 问题的核心区域。该文提出的 Webb 6-point weights（替代 Rademacher weights）和 restricted bootstrap 等方法直接适用于本文的 statistical correction。\n\n**[REBUT]** Kish (1965) effective sample size 的相关性较弱——论文的 K_eff 虽然名为\"effective independence\"，但其定义基于 pairwise MI（Equation 1），与 Kish 的 design effect / effective sample size 概念（基于 intra-cluster correlation）在形式和动机上都不同。引用 Kish 可能造成不必要的概念混淆。如果 R1 的意图是建议将 K_eff 与 Kish effective n 做对比讨论，那需要更明确的理论桥梁。\n\n---\n\n### Overall Assessment 对比\n\nR1 给出 3.5 (Borderline Conference)，与我的评分一致。\n\n我们的核心关切高度重叠：K_eff-η_max 共线性对因果推断的根本性限制（我的 N3 / R1 的 N1）、正文 framing 不充分反映 confound 严重性、以及 K 值覆盖不足。\n\n主要分歧在于 ε 敏感性分析的严重性评级：R1 标记为 critical，我认为 fractional logit 的交叉验证和 3 个数量级的 ε 稳定性检查足以将其降为 should-fix。",
    "reviewer_id": "2",
    "project": "cert_manip_resist_eval"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-23T11:55:32.379051+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3879
}
```

</details>

---


### Assistant

_source line 236 · 2026-05-23T11:55:42.509990+00:00_

交叉回应已提交。对 R1 的 14 个要点（N1-N2, W1-W5, M1-M4, Q1-Q5）逐条给出了 [AGREE] 或 [REBUT] 判断：

- **9 个 AGREE**：N1（Cinelli-Hazlett framing）、W1（K_eff 不稳定条件纳入汇总）、W2（13 clusters 不足）、W3（API-only 不复现）、W5（MCQ 局限）、M1（因果语言）、M2（Theorem 1 覆盖率）、M3（K=4 缺失）、MacKinnon & Webb 引用遗漏
- **3 个 REBUT**：N2（ε 敏感性已有 fractional logit 交叉验证，建议降为 should-fix）、W4（η_max 从 5/12→0/12 排除纯功效解释）、Kish 1965 引用（与 K_eff 概念不同）
- **1 个部分同意**：M4（fractional logit 是否用了 bootstrap 需作者澄清）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2"
}
```

</details>

---


## Round 9

## Round 9

108 recorded events


### User

_source line 237 · 2026-05-24T02:44:14.380525+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 相关工作 + 完整性 + 格式合规**。

## 论文信息
- **标题**: The Shifting Bottleneck: How Panel Size Modulates Adversarial Vulnerability in LLM Judge Panels
- **路径**: projects/cert_manip_resist_eval/docs/paper/main.tex
- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/submitted.pdf

## Venue 要求 (EMNLP 2026, ARR May cycle)
- **截止日期**: 2026-05-25
- **页数限制**: 正文 8 页，参考文献无限，Limitations 不计页（≤1页）
- **模板**: ACL template, `[review]` 模式
- **匿名规则**: double-blind
- **投稿系统**: OpenReview via ARR
- **Abstract**: 不超过 200 words

## 你的审查侧重

请重点审查以下方面：

1. **新颖性与贡献**：
   - 三个 claimed contributions 是否真正 novel？
   - "diversity hurts under adversarial attack" 这个发现是否已有 prior work 暗示？（ensemble adversarial robustness 文献中 Tramèr 2018, Kariyappa 2019, Pang 2019）
   - K_eff 作为 diversity measure 相比现有 ensemble diversity measures（Q-statistic, disagreement, κ-diversity）的独特贡献是什么？论文 Table 8 承认 κ-diversity 表现相当

2. **相关工作完整性**：
   - 是否遗漏重要相关工作？特别是：
     - LLM-as-Judge 安全性的其他最新工作
     - Multi-agent 系统安全性
     - Ensemble robustness certification 方面的理论工作
   - 搜索 2025-2026 年的最新文献，检查是否有直接竞争或高度相关的工作未被引用

3. **论文写作与结构**：
   - 叙事是否清晰？从 problem motivation → threat model → experiments → analysis 的逻辑链是否连贯？
   - 术语使用是否一致（如 "predictor shift" vs "regime transition"）？
   - 论文是否过度拥挤（8页限制下内容密度）？
   - Abstract 是否在 200 words 以内？

4. **格式合规检查**：
   - ACL 模板使用正确性
   - 匿名性——是否有去匿名化线索？
   - Limitations section 位置和内容
   - 引用格式

5. **Broader Impact / Ethics**：
   - 研究攻击 LLM judge 是否有 dual-use concern？
   - 攻击模板的披露是否需要 responsible disclosure 讨论？

请按 EMNLP ARR 审稿标准给出结构化审稿意见（Summary / Strengths / Weaknesses / Questions / Missing References / Overall Assessment + 评分）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-24T02:44:23.667270+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-24T02:44:23.720335+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/review_reviewer_2_38d341a1.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-24T02:44:25.782258+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-24T02:44:25.883163+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-24T02:44:27.691667+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-24T02:44:27.742318+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-research.skill.md
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-writing.skill.md
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/cert_manip_resist_eval/distilled-research.skill.md
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/cert_manip_resist_eval/distilled-writing.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-24T02:44:32.410011+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-24T02:44:32.460579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-24T02:44:36.625203+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 247 · 2026-05-24T02:44:39.234592+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/submitted.pdf",
  "project": "cert_manip_resist_eval",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/submitted.pdf",
    "project": "cert_manip_resist_eval",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 248 · 2026-05-24T02:44:43.904123+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria:

## Review Form Criteria

For Findings papers, the main criteria are soundness and reproducibility. Conference recommendations may also conside
…[truncated 1362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7278
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-24T02:44:45.209441+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 412.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 552.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 545.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 448.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 423.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.9}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1
…[truncated 482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5974
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-24T02:44:52.872575+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/submitted.pdf",
  "project": "cert_manip_resist_eval",
  "pages": "11-18",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/submitted.pdf",
    "project": "cert_manip_resist_eval",
    "pages": "11-18",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-24T02:44:56.239466+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 530.4}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.1}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 414.4}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 581.4}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 118.6}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_rou
…[truncated 57 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3366
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-24T02:44:56.340404+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need: 1) All scoring fields (soundness, excitement, reproducibility, etc.) with their scale and criteria descriptions. 2) The Overall Assessment scale with all options. 3) Any other required fields like confidence, best paper recommendation, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need: 1) All scoring fields (soundness, excitement, reproducibility, etc.) with their scale and criteria descriptions. 2) The Overall Assessment scale with all options. 3) Any other required fields like confidence, best paper recommendation, etc."
  }
}
```

</details>

---


### Tool call

_source line 253 · 2026-05-24T02:45:00.558469+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines, especially: 1) What reviewers should evaluate, 2) How to assess novelty and significance, 3) What constitutes a good vs bad review, 4) Any specific instructions about ethical considerations, limitations sections, 5) Guidelines about paper length and formatting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer guidelines, especially: 1) What reviewers should evaluate, 2) How to assess novelty and significance, 3) What constitutes a good vs bad review, 4) Any specific instructions about ethical considerations, limitations sections, 5) Guidelines about paper length and formatting"
  }
}
```

</details>

---


### Tool result

_source line 254 · 2026-05-24T02:45:03.580426+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Primary Scoring Fields

**Reviewer Confidence** (1-5 scale)
- 5: Positive evaluation; careful reading and familiarity with related work
- 4: Quite sure; unlikely to have missed something affecting ratings
- 3: Pretty sure; good area knowledge but details unchecked
- 2: Can defend evaluation but likely missed some details
- 1: Outside expertise area or paper very difficult to understand

**Soundness** (1-5 scale with half-points)
- 5: Most thorough study of its type
- 4: Sufficient support for claims; extra experiments optional
- 3: Adequate support for main claims; minor details need support
- 2: Major claims lack support; significant technical problems
- 1: "not yet sufficiently thorough to warrant publication"

**Excitement** (1-5 scale with half-points)
- 5: Would recommend to others; would attend presentation
- 4: Would mention to others; would prioritize attending
- 3: Might mention points; would attend if time available
- 2: Doesn't resonate personally but might interest others
- 1: Not compelling to reviewer or broader community

## Overall Assessment (1-5 scale with half-points)

- 5: Consider for Award (top 2.5%)
- 4.5: Borderline Award
- 4: Conference acceptance
- 3.5: Borderline Conference
- 3: Findings track acceptance
- 2.5: Borderline Findings
- 2: Resubmit next cycle with revisions
- 1.5: Resubmit after next cycle
- 1: Do not resubmit; irrelevant to computational linguistics

## Additional Evaluation Dimensions

**Reproducibility** (1-5 scale): Ranges from easily reproducible (5) to impossible to reproduce (1)

**Datasets** (1-5 scale): From enabling other research (5) to no usable datasets (1)

**Software** (1-5 scale): From transformative (5) to unavailable (1)

**Author Identity Knowledge** (1-5 scale): From confirmed knowledge (5) to no educated guess (1)

## Required Sections

- Paper Summary
- Summary of Strengths
- Summary of Weaknesses (numbered)
- Comments/Suggestions/Typos
- Limitations and 
…[truncated 107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7240
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-24T02:45:07.050955+00:00_

# ARR Reviewer Guidelines: Key Principles

## What Reviewers Should Evaluate

Reviewers assess papers across multiple dimensions: technical soundness, clarity, novelty, and appropriateness for the venue. The guidelines emphasize reading papers twice—first to understand the research question and contribution, then in-depth for technical evaluation. As stated in the document: "the goal of research is to contribute new knowledge."

## Assessing Novelty and Significance

The guidelines caution against dismissing work simply because results seem obvious in hindsight. Reviewers should verify novelty claims with specific references rather than vague assertions. Importantly, "SOTA results are neither necessary nor sufficient for a scientific contribution." Papers may offer value through efficiency, interpretability, fairness, or other dimensions beyond performance metrics.

## Characteristics of Strong vs. Weak Reviews

**Strong reviews** are specific, justified, and professional. They identify particular issues with evidence rather than general criticisms. They recognize that "it is always possible to come up with extra experiments," distinguishing between necessary evidence and nice-to-have additions.

**Weak reviews** rely on problematic heuristics like dismissing work for being "too simple" or "not surprising." They should avoid tone that is "sarcastic or insulting," maintaining professionalism throughout.

## Ethical and Limitations Guidance

Papers must include a Limitations section addressing responsible NLP considerations. Reviewers check the Responsible NLP checklist for adequate responses. Ethical issues warrant flagging for specialized review rather than desk rejection, following established ethics guidelines.

## Format Requirements

Papers must follow ACL style guides: maximum 8 pages for long papers, 4 for short papers (excluding ethical considerations and limitations sections). Style violations and length exceedances qualify for desk rejection.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6492
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-24T02:45:12.925078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 257 · 2026-05-24T02:45:13.478839+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 258 · 2026-05-24T02:45:14.486790+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1561
}
```

</details>

---


### Tool call

_source line 259 · 2026-05-24T02:45:14.487213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 260 · 2026-05-24T02:45:15.047869+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1569
}
```

</details>

---


### Tool call

_source line 261 · 2026-05-24T02:45:15.048291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-24T02:45:15.399685+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-24T02:45:16.255939+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1768
}
```

</details>

---


### Tool result

_source line 264 · 2026-05-24T02:45:17.263443+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2215
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-24T02:45:17.465470+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2065
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-24T02:45:22.737297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-24T02:45:23.692322+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-24T02:45:23.692767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 269 · 2026-05-24T02:45:24.244996+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 270 · 2026-05-24T02:45:24.800111+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1107
}
```

</details>

---


### Tool call

_source line 271 · 2026-05-24T02:45:24.800415+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 272 · 2026-05-24T02:45:25.305055+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1060
}
```

</details>

---


### Tool call

_source line 273 · 2026-05-24T02:45:25.305467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 274 · 2026-05-24T02:45:25.657976+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-24T02:45:25.962359+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-24T02:45:31.235179+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 277 · 2026-05-24T02:45:31.737916+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 278 · 2026-05-24T02:45:32.190069+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 279 · 2026-05-24T02:45:32.190481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 280 · 2026-05-24T02:45:33.101686+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1363
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-24T02:45:33.102975+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 912
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-24T02:45:33.103319+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 283 · 2026-05-24T02:45:33.404243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 284 · 2026-05-24T02:45:33.907270+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-24T02:45:34.209417+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-24T02:45:40.734519+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-24T02:45:41.188393+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-24T02:45:41.188856+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 289 · 2026-05-24T02:45:41.690810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 290 · 2026-05-24T02:45:41.792834+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-24T02:45:41.793603+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-24T02:46:03.676498+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM judge adversarial attack manipulation robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM judge adversarial attack manipulation robustness 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 293 · 2026-05-24T02:46:05.281468+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ensemble diversity adversarial robustness tradeoff \"diversity hurts\" Tramèr 2018 Kariyappa 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ensemble diversity adversarial robustness tradeoff \"diversity hurts\" Tramèr 2018 Kariyappa 2019"
  }
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-24T02:46:05.332102+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "multi-agent LLM system security adversarial robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "multi-agent LLM system security adversarial robustness 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-24T02:46:10.447977+00:00_

Web search results for query: "LLM judge adversarial attack manipulation robustness 2025 2026"

Links: [{"title":"CAP: Improving the Robustness of LLM-as-a-Judge Against Adversarial Score Manipulation via Comparative Augmented Prompting | OpenReview","url":"https://openreview.net/forum?id=wYU6OYFvid"},{"title":"SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK","url":"https://arxiv.org/pdf/2603.29403"},{"title":"A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness","url":"https://arxiv.org/html/2603.06594"},{"title":"[2505.13348] Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks","url":"https://arxiv.org/abs/2505.13348"},{"title":"Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment","url":"https://arxiv.org/html/2402.14016v2"},{"title":"Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment","url":"https://arxiv.org/pdf/2402.14016"},{"title":"[2402.14016] Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment","url":"https://arxiv.org/abs/2402.14016"},{"title":"LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge","url":"https://arxiv.org/html/2506.09443v1"}]

Based on the web search results, here's what recent research shows about LLM judge adversarial attacks and robustness in 2025-2026:

## Key Vulnerabilities

LLM-as-a-Judge systems exhibit significant vulnerability to adversarial attacks, where carefully crafted suffixes or prompts can easily manipulate scoring outcomes and cause abnormal score inflation, severely undermining evaluation reliability.

LLM judges are actively vulnerable to adversarial manipulation, with judge jailbreaking occurring when prompt injections trick the evaluator into outputting favorable verdicts regardless of content.

## Recent Attack Methods

Multiple attack techniques have been identifi
…[truncated 811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6771
}
```

</details>

---


### Tool result

_source line 296 · 2026-05-24T02:46:12.455771+00:00_

Web search results for query: "multi-agent LLM system security adversarial robustness 2025 2026"

Links: [{"title":"Frontiers | Adversarial robustness of LLM-based multi-agent systems for engineering problems","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1784484/full"},{"title":"ADVERSARIAL ROBUSTNESS OF LLM-BASED MULTI","url":"https://openreview.net/pdf/a925b93f4a7a4621347d246dc2bfbff0956b2bc4.pdf"},{"title":"TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems","url":"https://arxiv.org/pdf/2511.05269"},{"title":"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring","url":"https://arxiv.org/pdf/2505.24239"},{"title":"A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks","url":"https://arxiv.org/html/2509.14285v4"},{"title":"Enhancing Robustness of LLM-Driven Multi-Agent Systems ...","url":"https://arxiv.org/pdf/2507.04105"}]

I've completed the web search for your query on multi-agent LLM system security and adversarial robustness. Here are the key findings from recent 2025-2026 research:

## Key Research Areas

**Vulnerabilities in Multi-Agent Systems:**
LLM-based MAS are highly sensitive to adversarial influence. Despite significant progress in improving collaboration and usability of multi-agent systems, their security and robustness remain largely under-explored, with multiple interacting agents increasing the attack surface and making systems more susceptible to diverse adversarial attacks.

**Attack Vectors:**
Six key attack vectors have been identified—Impersonation, Direct Prompt Injection, Indirect Prompt Injection, Contradicting Agents, Byzantine Agent, and Colluding Agents—targeting distinct components across the agentic pipeline.

**Design Factors Affecting Robustness:**
The role and knowledge of leader agents strongly affect susceptibility, with explicit warnings about faulty advice improving discernment, and the first agent in the discussion having the larges
…[truncated 594 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7123
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-24T02:46:15.818451+00:00_

Web search results for query: "ensemble diversity adversarial robustness tradeoff "diversity hurts" Tramèr 2018 Kariyappa 2019"

Links: [{"title":"Improving Ensemble Robustness by Collaboratively ...","url":"https://ojs.aaai.org/index.php/AAAI/article/view/16843/16650"},{"title":"Diversity supporting robustness: Enhancing adversarial robustness via differentiated ensemble predictions - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0167404824001627"},{"title":"Toward Adversarial Robustness by Diversity in an Ensemble of Specialized Deep Neural Networks | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-030-47358-7_1"},{"title":"A NOVEL ENSEMBLE TRAINING METHOD WITH ...","url":"https://openreview.net/pdf?id=KW8yzAOIZr"},{"title":"[1901.09981] Improving Adversarial Robustness of Ensembles with Diversity Training","url":"https://ar5iv.labs.arxiv.org/html/1901.09981"},{"title":"A NOVEL ENSEMBLE TRAINING METHOD WITH FOURIER ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7f7eade8b69c853e3137cab80df3ccf6-Paper-Conference.pdf"},{"title":"[PDF] Improving Adversarial Robustness of Ensembles with Diversity Training | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Improving-Adversarial-Robustness-of-Ensembles-with-Kariyappa-Qureshi/d4473a41c9f7b4095599bec14ea0a88e7041e737"},{"title":"Improving Adversarial Robustness via Promoting Ensemble Diversity","url":"https://arxiv.org/pdf/1901.08846"},{"title":"Improving Adversarial Robustness of Ensembles with Diversity Training","url":"https://arxiv.org/pdf/1901.09981"}]

I found relevant search results on ensemble diversity and adversarial robustness. Here's what the search revealed:

## Key Works Referenced

Ensemble training is an important approach to enhance adversarial robustness (Tramèr et al., 2018). However, the relationship between diversity and robustness is nuanced.

## The Diversity Approach

Kariyappa and Qureshi (2019) showed th
…[truncated 1127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10536
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-24T02:46:26.862797+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"effective independence\" K_eff diversity measure ensemble LLM judge panel"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"effective independence\" K_eff diversity measure ensemble LLM judge panel"
  }
}
```

</details>

---


### Tool call

_source line 299 · 2026-05-24T02:46:29.120460+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pang 2019 \"improving adversarial robustness\" ensemble diversity ADP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pang 2019 \"improving adversarial robustness\" ensemble diversity ADP"
  }
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-24T02:46:29.171033+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ensemble robustness certification theoretical guarantees voting classifier 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ensemble robustness certification theoretical guarantees voting classifier 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-24T02:46:33.694536+00:00_

Web search results for query: "Pang 2019 "improving adversarial robustness" ensemble diversity ADP"

Links: [{"title":"[1901.08846] Improving Adversarial Robustness via Promoting Ensemble Diversity","url":"https://arxiv.org/abs/1901.08846"},{"title":"Improving Adversarial Robustness via Promoting Ensemble Diversity | DeepAI","url":"https://deepai.org/publication/improving-adversarial-robustness-via-promoting-ensemble-diversity"},{"title":"Improving Adversarial Robustness via Promoting Ensemble Diversity","url":"https://proceedings.mlr.press/v97/pang19a.html"},{"title":"Frontiers | Adversarial robustness in deep neural networks based on variable attributes of the stochastic ensemble model","url":"https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2023.1205370/full"},{"title":"Improving Adversarial Robustness via Promoting Ensemble Diversity","url":"https://arxiv.org/pdf/1901.08846"},{"title":"GitHub - P2333/Adaptive-Diversity-Promoting: Adversarial Defense for Ensemble Models (ICML 2019)","url":"https://github.com/P2333/Adaptive-Diversity-Promoting"},{"title":"Improving Adversarial Robustness via Promoting Ensemble Diversity | Request PDF","url":"https://www.researchgate.net/publication/330673320_Improving_Adversarial_Robustness_via_Promoting_Ensemble_Diversity"},{"title":"Improving Adversarial Robustness via Promoting ...","url":"https://icml.cc/media/icml-2019/Slides/4733.pdf"},{"title":"[PDF] Improving Adversarial Robustness via Promoting Ensemble Diversity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Improving-Adversarial-Robustness-via-Promoting-Pang-Xu/676e40050453ddeb1387f8314478c0ac3681a8c6"}]

Based on the search results, I found the paper you're looking for:

"Improving Adversarial Robustness via Promoting Ensemble Diversity" by Pang et al. (2019) presents a method that explores the interaction among individual networks to improve robustness for ensemble models. The paper defines a new notion of ensemble diversity 
…[truncated 872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4574
}
```

</details>

---


### Tool result

_source line 302 · 2026-05-24T02:46:33.795844+00:00_

Web search results for query: ""effective independence" K_eff diversity measure ensemble LLM judge panel"

Links: [{"title":"Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)","url":"https://eugeneyan.com/writing/llm-evaluators/"},{"title":"Published as a conference paper at ICLR 2025 TRUST OR ESCALATE: LLM JUDGES WITH","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf"},{"title":"Scaling Evaluation with LLM Judges: Our Approach and Findings | by Nayeem Islam | Medium","url":"https://medium.com/@nomannayeem/scaling-evaluation-with-llm-judges-our-approach-and-findings-0a046e8344c4"},{"title":"Replacing Judges with Juries: Evaluating LLM Generations with a Panel of   Diverse Models","url":"https://arxiv.org/pdf/2404.18796"},{"title":"Preprint. Under review. Auto-Prompt Ensemble for LLM Judge Jiajie Li∗","url":"https://arxiv.org/pdf/2510.06538"},{"title":"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/pdf/2604.07650"},{"title":"When AIs Judge AIs: The Rise of Agent-as-a-Judge Evaluation for LLMs","url":"https://arxiv.org/html/2508.02994v1"},{"title":"Logarithmic Scores, Power-Law Discoveries: Disentangling Measurement from Coverage in Agent-Based Evaluation","url":"https://arxiv.org/pdf/2604.00477"},{"title":"[2404.18796] Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models","url":"https://arxiv.org/abs/2404.18796"}]

Based on the search results, I found relevant information about ensemble LLM judge panels and diversity measures, though the specific "K_eff" metric doesn't appear in these results. Here's what I found:

## Ensemble LLM Judge Panels

A Panel of LLMs (PoLL) approach proposes using an ensemble of three smaller LLM-evaluators (command-r, gpt-3.5-turbo, haiku) to independently score model outputs, rather than relying on a singl
…[truncated 1074 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6933
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-24T02:46:34.849909+00:00_

Web search results for query: "ensemble robustness certification theoretical guarantees voting classifier 2024 2025"

Links: [{"title":"Voting Classifier: A Comprehensive Guide for 2025 - Shadecoder - 100% Invisibile AI Coding Interview Copilot","url":"https://www.shadecoder.com/topics/voting-classifier-a-comprehensive-guide-for-2025"},{"title":"Tight Certificates of Adversarial Robustness for Randomly Smoothed   Classifiers","url":"https://arxiv.org/pdf/1906.04948"},{"title":"Boosting Certificate Robustness for Time Series Classification with Efficient Self-Ensemble","url":"https://arxiv.org/html/2409.02802v1"},{"title":"Boosting Certificate Robustness for Time Series Classification with Efficient Self-Ensemble | Proceedings of the 33rd ACM International Conference on Information and Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3627673.3679748"},{"title":"Boosting Certified Robustness for Time Series Classification with Efficient Self-Ensemble","url":"https://arxiv.org/html/2409.02802v3"},{"title":"Reconcile Certified Robustness and Accuracy for DNN-based Smoothed Majority Vote Classifier","url":"https://arxiv.org/pdf/2509.25979"},{"title":"[2409.02802] Boosting Certified Robustness for Time Series Classification with Efficient Self-Ensemble","url":"https://arxiv.org/abs/2409.02802"}]

I found relevant research on ensemble robustness certification with theoretical guarantees. Here are the key findings:

## Recent Work on Ensemble Robustness Certification (2024)

A recent study introduces a margin-based generalization bound with a certified robust radius for Majority Vote classifiers, bridging generalization performance and robustness guarantees. This work appears to be from 2025 based on the arxiv submission date.

The theoretical framework develops a margin-based PAC-Bayesian approach tailored for smoothed inputs, which bridges randomized smoothing and generalization analysis.

## Randomized Smoothing for Ensemble Methods (2024)

Randomized Smoothin
…[truncated 1031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5678
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-24T02:47:01.815302+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2505.13348 \"Investigating the Vulnerability of LLM-as-a-Judge\" prompt injection multi-judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2505.13348 \"Investigating the Vulnerability of LLM-as-a-Judge\" prompt injection multi-judge"
  }
}
```

</details>

---


### Tool call

_source line 305 · 2026-05-24T02:47:01.916216+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604.07650 \"How Independent are Large Language Models\" behavioral entanglement verifier ensemble"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604.07650 \"How Independent are Large Language Models\" behavioral entanglement verifier ensemble"
  }
}
```

</details>

---


### Tool result

_source line 306 · 2026-05-24T02:47:06.691285+00:00_

Web search results for query: "arxiv 2505.13348 "Investigating the Vulnerability of LLM-as-a-Judge" prompt injection multi-judge"

Links: [{"title":"[2505.13348] Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks","url":"https://arxiv.org/abs/2505.13348"},{"title":"Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.13348v1"},{"title":"Investigating the Vulnerability of LLM-as-a-Judge ...","url":"https://arxiv.org/pdf/2505.13348"},{"title":"Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks","url":"https://arxiv.org/html/2505.13348v1"},{"title":"Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250513348M/abstract"},{"title":"Adversarial Attacks on LLM-as-a-Judge Systems: Insights from Prompt Injections","url":"https://arxiv.org/html/2504.18333"},{"title":"[Literature Review] Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks","url":"https://www.themoonlight.io/en/review/investigating-the-vulnerability-of-llm-as-a-judge-architectures-to-prompt-injection-attacks"},{"title":"(PDF) Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks","url":"https://www.researchgate.net/publication/391911310_Investigating_the_Vulnerability_of_LLM-as-a-Judge_Architectures_to_Prompt-Injection_Attacks"}]

I found the paper! Here's what the search results reveal about arxiv 2505.13348:

**Paper Title:** Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks

**Authors:** Narek Maloyan, Bislan Ashinov, and Dmitry Namiot

**Main Focus:** The paper investigates the vulnerability of LLM-as-a-Judge architectures to prompt-injection attacks, where malicious inputs are designed to compromise the judge's deci
…[truncated 830 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4875
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-24T02:47:07.444292+00:00_

Web search results for query: "arxiv 2604.07650 "How Independent are Large Language Models" behavioral entanglement verifier ensemble"

Links: [{"title":"[2604.07650] How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/abs/2604.07650"},{"title":"[2604.07650v1] How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/abs/2604.07650v1"},{"title":"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/html/2604.07650"},{"title":"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/pdf/2604.07650"},{"title":"[2601.06788] Artificial Entanglement in the Fine-Tuning of Large Language Models","url":"https://arxiv.org/abs/2601.06788"}]

I found the paper! Here's what I discovered:

The paper "How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles" addresses a critical question about whether seemingly diverse LLMs are truly independent.

**Key Problem:**
Shared pretraining data, distillation, and alignment pipelines can induce hidden behavioral dependencies that undermine multi-model systems like LLM-as-a-judge pipelines and ensemble verification. In practice, this manifests as correlated reasoning patterns and synchronized failures, where apparent agreement reflects shared error modes rather than independent validation.

**Proposed Solution:**
The authors develop a statistical framework for auditing behavioral entanglement among black-box LLMs, introducing a multi-resolution hierarchy that characterizes the joint failure manifold through two information-theo
…[truncated 759 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5528
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-24T02:47:17.684986+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-24T02:47:17.735737+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb,amsthm}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{definition}{Definition}
17	\newtheorem{proposition}{Proposition}
18	
19	\title{The Shifting Bottleneck: How Panel Size Modulates\\Adversarial Vulnerability in LLM Judge Panels}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	Multi-judge LLM evaluation panels are widely assumed to benefit from judge diversity, drawing on fault-tolerance intuitions from distributed systems. We empirically characterize how panel composition determines adversarial vulnerability by decomposing panel attack success into individual judge weakness ($\eta_{\max}$) and structural diversity ($K_{\mathrm{eff}}$) across 15 models, six attack types, two benchmarks, and panel sizes $K \in \{3, 5, 7\}$ (up to 6,435 panels). Contrary to Condorcet Jury Theorem predictions, $K_{\mathrm{eff}}$ is uniformly positively associated with vulnerability across all 12 conditions---higher diversity corresponds to higher attack success. The relative importance of the two predictors shifts with panel size: at $K{=}3$, both contribute (co-determination); at $K{\geq}5$, $K_{\mathrm{eff}}$ becomes the sole significant predictor while $\eta_{\max}$ drops to zero significance. Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09); Bayesian calibration attenuates $K_{\mathrm{eff}}$ but $\eta_{\max}$ persists (9/12 under OLS), providing partial defense. The defense strategy must match the regime: small panels require screening for individual robustness; larger panels require managing judge independence.
28	\end{abstract}
29	
30	\input{introduction}
31	\input{
…[truncated 2016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-24T02:49:20.781950+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-24T02:49:20.882853+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix_attacks.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-24T02:49:24.496211+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-24T02:49:24.848440+00:00_

1	\section{Related Work}
2	
3	\paragraph{LLM-as-Judge and Multi-Judge Evaluation.}
4	LLM judges gained traction after \citet{zheng2023judging} established them as scalable alternatives to human annotation. \citet{wang2023fair} documented systematic failure modes (position bias, verbosity, sycophancy), motivating multi-judge panels; \citet{raina2024judgerobust} quantified robustness gaps under universal adversarial attacks, and \citet{stureborg2024inconsistent} and \citet{ye2024justice} further catalogued inconsistency and bias in LLM evaluators. Aggregating noisy annotators traces back to \citet{dawid1979maximum}; \citet{verga2024replacing} showed diverse panels can match single large judges, and \citet{panickssery2024llm} identified self-preference bias driving within-family correlations. These frameworks assume benign conditions; we test whether aggregation benefits survive adversarial manipulation. \citet{almasoud2026security} reported that 7-model committees reduce ASR from 50--68\% to 10--19\%, but did not disentangle diversity from individual robustness.
5	
6	\paragraph{Condorcet Jury Theorem.}
7	\citet{condorcet1785essai} proved that majority voting accuracy converges to 1 when per-voter accuracy exceeds 0.5; Condorcet's original insight already predicts that panel size should matter for aggregation quality. \citet{austensmith1996information} showed that sincere voting is not always rational under the CJT, and \citet{ladha1992condorcet} extended the theorem to correlated voters, showing that positive correlation weakens the convergence guarantee; \citet{kaniovski2011optimal} derived optimal jury size under correlated votes. Our contribution is not the qualitative direction (which CJT predicts) but the empirical characterization of the uniform positive $K_{\mathrm{eff}}$--vulnerability association across all conditions, the panel-size-dependent predictor shift from co-determination to $K_{\mathrm{eff}}$ dominance, and the aggregation predictability gradient, n
…[truncated 2519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-24T02:49:24.999357+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-24T02:49:24.999982+00:00_

1	\section{Introduction}
2	
3	\begin{figure*}[t]
4	\centering
5	\includegraphics[width=\textwidth]{figures/fig_framework.pdf}
6	\caption{Overview of our evaluation framework. Given $N$ candidate LLM judges, we construct $K$-judge panels (\S\ref{sec:experiments}), subject them to six adversarial attack types (\S\ref{sec:threat_model}), and assess vulnerability through two complementary metrics: $\eta_{\max}$ (weakest-link individual susceptibility) and $K_{\text{eff}}$ (effective independent channels via mutual information). Panel decisions are aggregated through four methods of increasing sophistication (\S\ref{sec:aggregation}).}
7	\label{fig:framework}
8	\end{figure*}
9	
10	Multi-judge panels have emerged as the dominant defense against bias and manipulation in LLM-based evaluation. After \citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work exposed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, drawing inspiration from Byzantine fault tolerance (BFT), where majority voting among independent nodes tolerates faulty responses \citep{lamport1982byzantine,castro1999practical}. A recent systematization of LLM-judge security reports that 7-model committees reduce attack success rates from 50--68\% to 10--19\% \citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation.
11	
12	Yet the evidence for diversity as a causal defense is weaker than it appears. The observed ASR reduction conflates panel diversity (judge independence) with individual robustness (strongest members). No existing work disentangles these across panel sizes. BFT adversaries control faulty nodes internally, whereas evaluation adversaries manipulate inputs externally; the SDPI bounds joint failure but assumes non-adaptive faults \cite
…[truncated 2732 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-24T02:49:33.028860+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-24T02:49:33.029337+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-24T02:49:38.217092+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "kuai2026|kim2025corr|2604\\.07650|2505\\.13348|TAMAS|credibility.scoring",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "kuai2026|kim2025corr|2604\\.07650|2505\\.13348|TAMAS|credibility.scoring",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-24T02:49:38.317841+00:00_

60-  note      = {arXiv:2601.20299}
61-}
62-
63:@inproceedings{kim2025correlated,
64-  author    = {Kim, Elliot and Garg, Avi and Peng, Kenny and Garg, Nikhil},
65-  title     = {Correlated Errors in Large Language Models},
66-  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
--
98-
99-% NOTE: literature_map.yaml cites this as "Chen et al. 2026" but first author is Kuai.
100-% Full title includes "and Reweighting Verifier Ensembles" (truncated in literature_map).
101:@article{kuai2026independent,
102-  author    = {Kuai, Chenchen and Jiang, Jiwan and Zhu, Zihao and Wang, Hao and Wu, Keshu and Li, Zihao and Zhang, Yunlong and Liu, Chenxi and Tu, Zhengzhong and Fan, Zhiwen and Zhou, Yang},
103-  title     = {How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles},
104:  journal   = {arXiv preprint arXiv:2604.07650},
105-  year      = {2026},
106:  url       = {https://arxiv.org/abs/2604.07650},
107:  note      = {arXiv:2604.07650}
108-}
109-
110-% ============================================================

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-24T02:49:53.634366+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "maloyan|2505\\.13348|prompt.injection.*judge|judge.*prompt.injection",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "maloyan|2505\\.13348|prompt.injection.*judge|judge.*prompt.injection",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-24T02:49:53.735192+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-24T02:49:59.358937+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "raina|stureborg|panickssery|turkmen|robertson|feng2026|kaneko|jung2026|qiu2026|chen2025inc",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib",
  "output_mode": "content",
  "-C": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "raina|stureborg|panickssery|turkmen|robertson|feng2026|kaneko|jung2026|qiu2026|chen2025inc",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib",
    "output_mode": "content",
    "-C": "2"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-24T02:49:59.409550+00:00_

7-% ============================================================
8-
9:@article{robertson2025stepwise,
10-  author    = {Robertson, Zachary and Koyejo, Sanmi},
11-  title     = {Let's Measure Information Step-by-Step: {LLM}-Based Evaluation Beyond Vibes},
--
25-}
26-
27:@article{turkmen2026ensemble,
28-  author    = {Turkmen, Yigit and Buyukates, Baturalp and Bastopcu, Melih},
29-  title     = {Don't Always Pick the Highest-Performing Model: An Information Theoretic View of {LLM} Ensemble Selection},
--
34-}
35-
36:@inproceedings{kaneko2025bits,
37-  author    = {Kaneko, Masahiro and Baldwin, Timothy},
38-  title     = {Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against {LLMs}},
--
43-}
44-
45:@inproceedings{chen2025incentivizing,
46-  author    = {Chen, Baiting and Zhu, Tong and Han, Jiale and Li, Lexin and Li, Gang and Dai, Xiaowu},
47-  title     = {Incentivizing Truthful Language Models via Peer Elicitation Games},
--
52-}
53-
54:@inproceedings{qiu2026truthfulness,
55-  author    = {Qiu, Tianyi Alex and Carroll, Micah and Allen, Cameron},
56-  title     = {Truthfulness Despite Weak Supervision: Evaluating and Training {LLMs} Using Peer Prediction},
--
79-}
80-
81:@inproceedings{feng2026noisy,
82-  author    = {Feng, Chen and Shen, Minghe and Balashankar, Ananth and Gerner-Beuerle, Carsten and Rodrigues, Miguel R. D.},
83-  title     = {Noisy but Valid: Robust Statistical Evaluation of {LLMs} with Imperfect Judges},
--
88-}
89-
90:@article{jung2026logarithmic,
91-  author    = {Jung, HyunJoon and Na, William},
92-  title     = {Logarithmic Scores, Power-Law Discoveries: Disentangling Measurement from Coverage in Agent-Based Evaluation},
--
327-}
328-
329:@inproceedings{panickssery2024llm,
330-  author    = {Arjun Panickssery and Samuel R. Bowman and Shi Feng},
331-  title     = {{LLM} Evaluators Recognize and Favor Their Own Generations},
--
364-% ============================================================
365-
366:@article{raina20
…[truncated 420 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-24T02:50:09.858804+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "TAMAS|tamas|CAP.*judge|comparative.*augmented|adversary.resistant|credibility.scoring",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "TAMAS|tamas|CAP.*judge|comparative.*augmented|adversary.resistant|credibility.scoring",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/references.bib",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-24T02:50:09.909311+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-24T02:50:13.523175+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-24T02:50:13.974586+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\paragraph{Predictor Shift Mechanism.}
5	At $K{=}3$, a majority requires $t{=}2$; a single compromised judge can flip the panel, making both $\eta_{\max}$ and $K_{\mathrm{eff}}$ relevant (co-determination: 3/12 and 4/12 under bootstrap). At $K{\geq}5$, the adversary must compromise ${\geq}3$ judges; high-$K_{\mathrm{eff}}$ panels present more distinct attack surfaces, and $\eta_{\max}$'s marginal contribution collapses because even high-$\eta$ judges cannot flip the panel alone. The transition threshold $K^*$ lies between 3 and 5.
6	
7	\paragraph{Uniform Positive Direction.}
8	$K_{\mathrm{eff}}$'s coefficient direction is positive in all 12 conditions under both OLS and GAM bootstrap (88.9--100\% positive rate at $K{=}3$, 100\% at $K{=}5$); statistical significance depends on inference method (OLS 12/12; wild cluster bootstrap 4/12 at $K{=}3$, 10/12 at $K{=}5$). A Kruskal--Wallis test finds no significant magnitude difference between targeted and shared-bias attacks ($p{=}0.200$ at $K{=}3$, $p{=}0.423$ at $K{=}5$; Appendix~\ref{app:bft_reversal}), ruling out attack-mechanism-dependent directional structure.
9	
10	\paragraph{Diversity--Capability Confound.}
11	$K_{\mathrm{eff}}$ and $\eta_{\max}$ are correlated at $r{=}0.70$ ($K{=}3$) and $r{=}0.81$ ($K{=}5$; Figure~\ref{fig:keff_eta_scatter}), reflecting a structural property: maximizing diversity requires sampling across capability tiers, introducing weaker judges (Appendix~\ref{app:diversity_capability}). Cinelli--Hazlett sensitivity analysis \citep{cinelli2020making} shows the known $\eta_{\max}$ confound exceeds $K_{\mathrm{eff}}$'s robustness value in 28/36 conditions (Appendix~\ref{app:sensitivity}), with robustness increasing with $K$ (1/12 $\to$ 3/12 $\to$ 4/12). The API-only subset ($r{=}0.85$) does not replicate the transition (3/12). Capability-matched subsampling ($r{=}0.50$, 9 models, 126 panels at $K{=}5$; Figure~\ref{fig:keff_eta_scatter}, orange) provi
…[truncated 1666 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-24T02:50:13.975087+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-24T02:50:14.025499+00:00_

1	\section{Conclusion}
2	
3	We document a descriptive predictor shift in LLM judge panel vulnerability: at $K{=}3$, both individual weakness ($\eta_{\max}$) and diversity ($K_{\mathrm{eff}}$) contribute (co-determination); at $K{\geq}5$, $K_{\mathrm{eff}}$ becomes the sole significant predictor under bootstrap (10/12 at $K{=}5$). $K_{\mathrm{eff}}$'s coefficient direction is uniformly positive across all 12 conditions, with no attack-type-dependent directional split (Kruskal--Wallis $p{=}0.200$). Aggregation rules modulate predictability ($R^2$: 0.83 threshold $\to$ 0.09 Bayesian); Bayesian calibration attenuates $K_{\mathrm{eff}}$ but $\eta_{\max}$ persists, providing partial defense. Because $K_{\mathrm{eff}}$ and $\eta_{\max}$ are structurally correlated ($r{=}0.70$--$0.81$), the independent causal contribution of diversity remains only partially separable even under capability-matched subsampling (\S\ref{sec:analysis}). For deployment: at $K{=}3$, screen for individual robustness; at $K{\geq}5$, prefer correlated robustness profiles. Causal identification requires training-based diversity control \citep{kariyappa2019improving,pang2019improving}.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-24T02:50:28.181469+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-24T02:50:28.182117+00:00_

1	\appendix
2	
3	\section{Proof of Theorem~\ref{thm:monotonicity}}
4	\label{app:proof}
5	
6	The replaced judge $J_K'$ is \emph{pivotal} exactly when $t{-}1$ of the remaining $K{-}1$ judges have already failed. Formally, let $S = \sum_{j=1}^{K-1} X_j^a$ denote the number of failures among the shared judges. The panel fails if and only if the $K$-th judge also fails when $S = t{-}1$, or when $S \geq t$ regardless of the $K$-th judge:
7	\begin{align}
8	\mathrm{ASR}(\mathcal{P}, a) &= \Pr(S \geq t) + \Pr(S = t{-}1) \cdot \Pr(X_K^a {=} 1 \mid S = t{-}1).
9	\end{align}
10	Since $\Pr(X_{K'}^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K}) \geq \Pr(X_K^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K})$ for all attacks $a$ and realizations $\mathbf{x}_{-K}$ (by hypothesis), the second term is weakly larger for $\mathcal{P}'$ than for $\mathcal{P}$ under every attack. Taking the supremum over attacks preserves the inequality: $\mathrm{ASR}^*(\mathcal{P}') \geq \mathrm{ASR}^*(\mathcal{P})$. The result holds under arbitrary inter-judge correlations and any attack space $\mathcal{A}$.
11	
12	\section{Robustness Correction Methods}
13	\label{app:robustness_methods}
14	
15	The 455 panels are constructed combinatorially from 15 shared judges: each judge appears in $\binom{14}{2} = 91$ panels, inducing correlated residuals across panel-level observations. Standard OLS assumes independent errors, potentially inflating significance. We apply three corrections.
16	
17	\paragraph{Clustered Standard Errors.} Because each panel of $K{=}3$ judges does not map to a single cluster, we perform three separate one-way clusterings (one for each judge position in the ordered panel tuple) using CR1 bias-corrected sandwich estimators (13 clusters per position). The reported standard error for each coefficient is the maximum across the three clusterings, yielding the most conservative inference.
18	
19	\paragraph{Mixed Effects.} For each of the three judge positions, we fit a linear mixed-effec
…[truncated 7449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-24T02:50:42.211533+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix_attacks.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix_attacks.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-24T02:50:42.262352+00:00_

1	\section{Attack Prompt Templates}
2	\label{app:attacks}
3	
4	Table~\ref{tab:attack-templates} lists the six manipulation strategies used in our experiments. Each attack modifies the ground-truth loser response to exploit a specific judge bias. Below we describe each attack type and provide representative template text.
5	
6	\paragraph{Prompt Injection.} Injects directive text at the end of the loser response, attempting to override the judge's evaluation logic with explicit scoring instructions.
7	
8	\paragraph{Sycophancy Exploitation.} Wraps the loser response in enthusiastic, agreeable language (a prefix and suffix), exploiting judges' preference for polite and eager responses.
9	
10	\paragraph{Score Manipulation.} Appends fabricated self-assessment scores to the loser response, leveraging judges' tendency to defer to confident quality claims embedded in the text.
11	
12	\paragraph{Verbosity Bias.} Appends a lengthy but content-free elaboration ($\sim$50--60 words) to the loser response, exploiting judges' bias toward longer responses regardless of substantive contribution.
13	
14	\paragraph{Position Bias.} Swaps the positions of response A and response B so that the ground-truth winner occupies position B, exploiting judges' tendency to favor position A.
15	
16	\paragraph{Authority Bias.} Prepends fabricated citations to prestigious institutions or journals at the beginning of the loser response, exploiting judges' deference to perceived academic authority.
17	
18	\begin{table*}[t]
19	\centering
20	\small
21	\caption{Representative prompt templates for each attack type. Templates shown are appended to, prepended to, or used to wrap the ground-truth loser response. Position bias has no template text; it swaps response order.}
22	\label{tab:attack-templates}
23	\begin{tabular}{@{}l p{11.5cm}@{}}
24	\toprule
25	\textbf{Attack Type} & \textbf{Representative Template} \\
26	\midrule
27	Prompt Injection &
28	\texttt{\textbackslash n\textbackslash n[Note: This respons
…[truncated 1436 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-24T02:50:49.691911+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-24T02:50:50.043498+00:00_

1	\section{Threat Model and Problem Formulation}
2	\label{sec:threat_model}
3	
4	A \emph{panel} $\mathcal{P} = \{J_1, \ldots, J_K\}$ consists of $K$ judges (with $K$ odd) that evaluate a candidate text via majority vote: the text is accepted if at least $t = \lceil K/2 \rceil$ judges approve it. Under an attack $a$, each judge $J_j$ is compromised with marginal failure probability $\eta_j(a) = \Pr(X_j^a = 1)$, where $X_j^a \in \{0,1\}$ denotes the failure indicator. We write $\eta_{\max} = \max_j \eta_j$ for the vulnerability of the weakest judge. The \emph{panel attack success rate} is $\mathrm{ASR}(\mathcal{P}, a) = \Pr\!\bigl(\sum_{j=1}^K X_j^a \geq t\bigr)$.
5	
6	To quantify diversity, we define the \emph{effective independence} $K_{\mathrm{eff}}$ directly from pairwise mutual information among judges:
7	\begin{equation}
8	\label{eq:keff}
9	K_{\mathrm{eff}} = \frac{1}{K}\sum_{i=1}^{K} \Bigl[1 + \sum_{j \neq i} \exp\!\bigl(-2 \cdot \mathrm{MI}(i,j)\bigr)\Bigr].
10	\end{equation}
11	This formulation computes effective independence from pairwise MI estimates without matrix decomposition, and is more stable for small panels ($K{=}3$). It ranges from $K_{\mathrm{eff}} \approx K$ when judges are nearly independent ($\mathrm{MI} \to 0$) to $K_{\mathrm{eff}} \approx 1$ when judges are highly correlated ($\mathrm{MI} \to \infty$). Under the strong data-processing inequality (SDPI), the joint vulnerability satisfies $\eta_{\mathrm{joint}} \leq \min(1,\; K_{\mathrm{eff}} \cdot \eta_{\max})$, suggesting that diversity should help, but this bound assumes non-adaptive faults.
12	
13	\begin{definition}[Adaptive Adversary]
14	\label{def:adversary}
15	A \emph{full-knowledge (oracle) adaptive adversary} has complete knowledge of the panel composition $\mathcal{P}$, the per-judge vulnerability profiles $\{\eta_j(\cdot)\}_{j=1}^K$, and the inter-judge correlation structure. It selects the attack $a^* = \arg\max_{a \in \mathcal{A}} \mathrm{ASR}(\mathcal{P}, a)$ to maximize the panel
…[truncated 2168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-24T02:51:45.027803+00:00_

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
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
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

_source line 337 · 2026-05-24T02:51:45.078384+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-24T02:53:42.592590+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见：Round 1（新颖性 + 相关工作 + 完整性 + 格式合规）\n\n**论文**: The Shifting Bottleneck: How Panel Size Modulates Adversarial Vulnerability in LLM Judge Panels\n**Venue**: EMNLP 2026 via ARR May cycle\n\n---\n\n## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 实验执行扎实、统计方法严谨，predictor shift 发现有价值，但核心 \"diversity hurts under adaptive attack\" 的新颖性被 ensemble adversarial robustness 既有文献显著削弱，K_eff 相对现有 diversity measures 的增量贡献有限。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4 / 5 | 方法论严谨：log-log 回归 + wild cluster bootstrap + Cinelli-Hazlett sensitivity + GAM + dominance analysis，多重 robustness check 互相印证。主要 claims 有充分实验支撑。扣分点：因果推断依赖观察数据，diversity-capability confound (r=0.70–0.81) 未完全解决 |\n| Excitement | 2.5 / 5 | Predictor shift (θ_max→K_eff as K increases) 是genuinely novel 的发现。但核心 \"diversity increases adversarial vulnerability\" 在 ensemble adversarial robustness 文献中已是 well-established insight (Tramèr 2018, Kariyappa & Qureshi 2019, Pang et al. 2019)。K_eff 对比 κ-diversity 等现有 measures 无显著优势 (Table 11)。贡献偏向 \"将已知原理 apply 到 LLM judge panel\" 的 empirical verification |\n| Reproducibility | 4 / 5 | 所有超参数已报告，基准数据集公开 (MMLU, ARC)，模型列表完整 (Table 1)，random seed 42 固定，code 承诺 upon acceptance 发布。扣分：code 目前不可用，无法实际复现验证 |\n| Confidence | 4 / 5 | 对 LLM evaluation、ensemble robustness、adversarial ML 有较好了解，仔细阅读了全文及全部 appendix |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心新颖性声明过度：diversity-vulnerability association 并非 novel finding\n- 具体位置：Abstract (\"Contrary to Condorcet Jury Theorem predictions\")；Section 1 Introduction 第三段 contribution list 第1点\n- 问题：论文将 \"K_eff uniformly positively associated with vulnerability\" 定位为与 CJT 预期相反的 surprising finding。但 CJT 显式假设 independent, non-adversarial errors——在 adaptive adversary 下 CJT 不适用是 trivially expected，不构成 \"contrary to\" 的惊喜。更重要的是，Tramèr et al. (2018) 已经证明 ensemble diversity 在 adversarial transfer 下反而增加攻击面；Kariyappa & Qureshi (2019) 和 Pang et al. (2019) 的 motivation 正是 \"naive diversity 不足以抵御 adaptive attacks\"。论文在 Section 2 Related Work (Adversarial Robustness and Transferability 段) 引用了这三篇工作，但仅用一句话带过 (\"but requires coordinating member training, a control absent in post-hoc LLM judge selection\")，没有充分讨论其发现与本文 K_eff 正关联的理论关系。\n- 为什么影响接收：如果核心 contribution 之一是\"已知结论在新 domain 的验证\"，则 novelty 评级将显著下降。Reviewer 很可能会质疑 \"这在 vision ensemble 领域已经知道了，transfer 到 LLM judge 有什么 non-trivial insight？\"\n- 建议修改方向：(1) 明确承认 diversity-vulnerability 关联在 ensemble adversarial ML 中已有理论基础，重新定位 contribution 为 \"empirical quantification in the LLM judge setting + predictor shift phenomenon + aggregation comparison\"；(2) 在 Related Work 中增加 1-2 段深入讨论 ensemble adversarial robustness 文献，说明 LLM judge panel 与 vision ensemble 的关键差异（post-hoc selection vs. joint training, discrete voting vs. continuous output, black-box judges vs. white-box models）\n\n**N2** [critical] K_eff 作为 diversity measure 的独特贡献不充分\n- 具体位置：Section 3 Equation 1 (K_eff definition)；Appendix P Table 11 (alternative diversity measures comparison)\n- 问题：Table 11 显示 Q-statistic (r=0.080, p=0.674)、Disagreement (r=0.164, p=0.861)、κ-diversity (r=0.194, p=0.942) 与 K_eff (r=0.164) 在 Pearson correlation 上表现相当甚至部分更优。论文声称 K_eff 的优势在于 \"interpretability: it quantifies the number of effective independent channels\"，但这是主观判断而非量化验证。如果 κ-diversity 能达到 comparable predictive power，则 K_eff 的 methodological contribution 被大幅削弱。\n- 为什么影响接收：如果用 κ-diversity 替代 K_eff 能得到几乎相同的结论，那么 K_eff 不构成 independent contribution，论文的 three claimed contributions 实质上缩减为两个\n- 建议修改方向：(1) 在正文中正面展示 Table 11 的比较（目前仅在 Appendix P），诚实讨论 K_eff 与 alternatives 的 trade-off；(2) 如果 claim interpretability advantage，需要通过具体案例展示 K_eff 的 information-theoretic interpretation 如何产生 κ-diversity 无法提供的 actionable insight；(3) 或者弱化对 K_eff 本身的 novelty claim，将其定位为 implementation choice 而非 contribution\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 相关工作遗漏：LLM judge 攻击的最新文献\n- 具体位置：Section 2 Related Work, \"LLM-as-Judge and Multi-Judge Evaluation\" 段\n- 问题：以下 2025 年发表的高度相关工作未被引用：\n  - Maloyan et al. (2025) \"Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks\" (arXiv:2505.13348, May 2025)——专门研究 prompt injection 对 LLM judge 架构的攻击，与本文 Attack Type 1 (prompt injection) 直接相关\n  - TAMAS benchmark (arXiv:2511.05269, Nov 2025)——multi-agent LLM 系统对抗性风险基准\n  - \"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring\" (arXiv:2505.24239, May 2025)——基于 credibility scoring 的 multi-agent 防御\n- 建议：在 Related Work 中增加这些引用，特别是 Maloyan et al. 作为 prompt injection 攻击的 direct prior work，需讨论其 GCG-based adversarial suffix 方法与本文 template-based prompt injection 的区别\n\n**W2** [warning] Kuai et al. (2026) 引用过于简略\n- 具体位置：Section 2, BFT and Security Games 段最后一句\n- 问题：论文引用了 Kuai et al. (2026, arXiv:2604.07650) \"How Independent are Large Language Models?\"，但仅作为 \"Correlated LLM judge errors [...] violate BFT's independence assumption\" 的旁证，一笔带过。然而该论文提出了 Difficulty-Weighted Behavioral Entanglement Index 和 Cumulative Information Gain 两个 LLM 独立性度量，与 K_eff 高度相关；其 de-entangled verifier ensemble reweighting 方法也直接关联本文的 aggregation 讨论。\n- 建议：在 Ensemble Diversity Theory 或单独段落中深入讨论 Kuai et al. 的度量方法与 K_eff 的关系（是否可视为 complementary measures？在 adversarial setting 下表现如何？）\n\n**W3** [warning] Diversity-capability confound 未完全解决，但 causal-sounding language 贯穿全文\n- 具体位置：Section 6 Analysis, \"Diversity–Capability Confound\" 段\n- 问题：作者诚实地报告了 K_eff 与 η_max 的 r=0.70–0.81 相关性，并承认 \"observational regression cannot reliably disentangle diversity's causal contribution from the capability deficit\"。然而论文多处使用暗示因果关系的语言：\"diversity *determines* vulnerability\"（Abstract: \"how panel composition determines adversarial vulnerability\"）、\"higher diversity corresponds to higher attack success\"。Cinelli-Hazlett RV 分析显示 η_max confound 在 28/36 conditions 中超过 K_eff 的 robustness value，进一步削弱了因果解读。\n- 建议：统一使用 \"associated with\" / \"predicts\" 替代 \"determines\" / \"corresponds to\"；在 Abstract 和 Introduction 中加入 caveat 说明这是 observational association\n\n**W4** [warning] 术语不一致\n- 具体位置：Section 5.2 标题 \"Panel-Size-Dependent Regime Transition\" vs. Abstract/Introduction/Conclusion 使用 \"predictor shift\"\n- 问题：同一个核心发现在不同位置使用不同术语（\"regime transition\" vs. \"predictor shift\"），增加读者认知负担\n- 建议：统一为一个术语（建议 \"predictor shift\"，因为 \"regime transition\" 暗示 sharp phase transition 而实际 K* 区间未精确确定）\n\n**W5** [warning] 攻击模板披露的 dual-use 讨论缺失\n- 具体位置：Appendix Q Table 12–13\n- 问题：论文提供了 6 种攻击类型的具体 prompt template（包括 prompt injection 的 system override 指令、authority bias 的虚构 Nature 2024 引用等）。虽然这些攻击相对简单（非 optimization-based），但缺少 responsible disclosure 或 ethical considerations 的讨论。ARR review form 明确要求 reviewer 评估 ethical concerns。\n- 建议：在 Limitations 末尾或新增 Ethics Statement 中简要讨论：(1) 攻击模板的 dual-use risk；(2) 为什么 disclosure 利大于弊（促进防御研究）；(3) 是否有 responsible disclosure 步骤（如通知 API providers）\n\n**W6** [warning] Benchmark 局限性\n- 具体位置：Section 4.1, Table 1; Limitations 段\n- 问题：仅使用 MMLU 和 ARC（两个 multiple-choice benchmarks），且 6 个 local models 全部使用 AWQ INT4 量化。Open-ended generation 评估（MT-Bench 风格）的攻击面可能与 multiple-choice 有结构性差异（选项操纵 vs. 文本质量操纵）。Limitations 中承认了这一点但措辞较轻 (\"Whether the predictor shift holds for open-ended or full-precision settings is unknown\")\n- 建议：在 Limitations 中更明确地讨论 multiple-choice → open-ended 的 generalizability gap；或在 future work 中将其列为 highest priority\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 约 154 words，符合 200 words 限制 ✓\n- ACL template `[review]` mode 使用正确 ✓\n- 匿名性：作者列为 \"Anonymous\"，无去匿名化线索 ✓（Section R 披露 AI assistant 使用为通用工具，不违反 blind review）\n- Limitations section 位于正文 Section 7 (Conclusion) 之后、Appendix 之前，位置正确 ✓\n- 引用格式：\\citet/\\citep 使用正确，BibTeX 条目基本完整 ✓\n- 正文页数：Sections 1-7 + Figure 5 在 8 页内完成，Limitations 不计页，合规 ✓\n- Title 中 \"shifting bottleneck\" 隐喻在正文中未充分展开——标题暗示有一个\"瓶颈\"在\"移动\"，但正文分析的是 predictor importance 的变化，\"bottleneck\" 的 metaphor 有些勉强\n- Figure 2 (page 6) 中 bar chart 的 y-axis label \"Standardized coefficient (β)\" 字体较小，不易阅读\n- Table 1 (page 4) \"Deploy\" 列仅标注 frontier/mid-tier/lightweight，但分类标准未在正文中明确定义（仅在 caption 中暗示 \"following the provider capability classification\"）\n\n---\n\n## 主要优势\n\n1. **实验规模与严谨性**：15 models × 6 attacks × 2 benchmarks × 3 panel sizes × 4 aggregation methods 的组合设计覆盖广泛，455–6,435 panels 的样本量在同类工作中突出。Wild cluster bootstrap、mixed effects、Cinelli-Hazlett sensitivity 三重 robustness check 体现了高标准的统计实践。\n\n2. **Predictor shift 发现**：θ_max → K_eff 的 panel-size-dependent shift 是该论文最强的原创贡献，在既有文献中未见类似发现。这一发现有明确的实践意义：小 panel 应优先筛选个体 robustness，大 panel 应关注 judge independence structure。\n\n3. **Aggregation method 对比**：四种 aggregation 方法（majority, weighted, threshold, Bayesian）的系统比较有实用价值。Bayesian calibration 能部分化解 K_eff channel 但保留 η_max channel 的发现为 deployment 提供了 actionable guidance。\n\n4. **统计诚实度**：论文坦承 K_eff 在 K=3 bootstrap 下仅 4/12 显著（vs. OLS 12/12），诚实报告 diversity-capability confound，并在 Limitations 中明确列出局限性。这种 intellectual honesty 在当前 ML 论文中值得肯定。\n\n5. **论文结构清晰**：从 problem motivation → threat model → formal framework → experiments → analysis → conclusion 的逻辑链连贯，appendix 组织有序（A–Q），每个 robustness check 都有独立的 appendix section。\n\n---\n\n## Missing References 汇总\n\n| 论文 | 相关性 | 建议处理 |\n|------|--------|----------|\n| Maloyan et al. 2025 (arXiv:2505.13348) — Prompt injection attacks on LLM-as-Judge | 高：直接研究 LLM judge 的 prompt injection 攻击 | 必须引用并讨论与本文 Attack Type 1 的区别 |\n| TAMAS (arXiv:2511.05269) — Multi-agent LLM adversarial benchmark | 中：multi-agent 系统安全性基准 | 建议在 Related Work 中引用 |\n| Adversary-Resistant Multi-Agent LLM via Credibility Scoring (arXiv:2505.24239) | 中：credibility-based 防御与 Bayesian calibration 有关联 | 建议在 aggregation 讨论中引用 |\n| Kuai et al. 2026 (arXiv:2604.07650) — LLM independence auditing | 高：已引用但讨论过于简略 | 需扩展讨论 |\n\n---\n\n## 总结\n\n这是一篇 **执行质量高** 但 **核心新颖性存疑** 的论文。Predictor shift 发现是实质性贡献，aggregation 对比有实用价值，统计方法论堪称典范。但 diversity-vulnerability 关联作为 headline finding 在 ensemble adversarial robustness 文献中并非 novel，K_eff 相对 κ-diversity 等现有 measures 的增量贡献有限。如果作者能重新校准 novelty claims（弱化 \"contrary to CJT\" 的 framing，强化 predictor shift 和 aggregation insights 的地位），并补充缺失的相关工作讨论，这篇论文有潜力达到 Conference 水准。当前状态下，推荐 Borderline Conference (3.5)。",
  "reviewer_id": "2",
  "project": "cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见：Round 1（新颖性 + 相关工作 + 完整性 + 格式合规）\n\n**论文**: The Shifting Bottleneck: How Panel Size Modulates Adversarial Vulnerability in LLM Judge Panels\n**Venue**: EMNLP 2026 via ARR May cycle\n\n---\n\n## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 实验执行扎实、统计方法严谨，predictor shift 发现有价值，但核心 \"diversity hurts under adaptive attack\" 的新颖性被 ensemble adversarial robustness 既有文献显著削弱，K_eff 相对现有 diversity measures 的增量贡献有限。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4 / 5 | 方法论严谨：log-log 回归 + wild cluster bootstrap + Cinelli-Hazlett sensitivity + GAM + dominance analysis，多重 robustness check 互相印证。主要 claims 有充分实验支撑。扣分点：因果推断依赖观察数据，diversity-capability confound (r=0.70–0.81) 未完全解决 |\n| Excitement | 2.5 / 5 | Predictor shift (θ_max→K_eff as K increases) 是genuinely novel 的发现。但核心 \"diversity increases adversarial vulnerability\" 在 ensemble adversarial robustness 文献中已是 well-established insight (Tramèr 2018, Kariyappa & Qureshi 2019, Pang et al. 2019)。K_eff 对比 κ-diversity 等现有 measures 无显著优势 (Table 11)。贡献偏向 \"将已知原理 apply 到 LLM judge panel\" 的 empirical verification |\n| Reproducibility | 4 / 5 | 所有超参数已报告，基准数据集公开 (MMLU, ARC)，模型列表完整 (Table 1)，random seed 42 固定，code 承诺 upon acceptance 发布。扣分：code 目前不可用，无法实际复现验证 |\n| Confidence | 4 / 5 | 对 LLM evaluation、ensemble robustness、adversarial ML 有较好了解，仔细阅读了全文及全部 appendix |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心新颖性声明过度：diversity-vulnerability association 并非 novel finding\n- 具体位置：Abstract (\"Contrary to Condorcet Jury Theorem predictions\")；Section 1 Introduction 第三段 contribution list 第1点\n- 问题：论文将 \"K_eff uniformly positively associated with vulnerability\" 定位为与 CJT 预期相反的 surprising finding。但 CJT 显式假设 independent, non-adversarial errors——在 adaptive adversary 下 CJT 不适用是 trivially expected，不构成 \"contrary to\" 的惊喜。更重要的是，Tramèr et al. (2018) 已经证明 ensemble diversity 在 adversarial transfer 下反而增加攻击面；Kariyappa & Qureshi (2019) 和 Pang et al. (2019) 的 motivation 正是 \"naive diversity 不足以抵御 adaptive attacks\"。论文在 Section 2 Related Work (Adversarial Robustness and Transferability 段) 引用了这三篇工作，但仅用一句话带过 (\"but requires coordinating member training, a control absent in post-hoc LLM judge selection\")，没有充分讨论其发现与本文 K_eff 正关联的理论关系。\n- 为什么影响接收：如果核心 contribution 之一是\"已知结论在新 domain 的验证\"，则 novelty 评级将显著下降。Reviewer 很可能会质疑 \"这在 vision ensemble 领域已经知道了，transfer 到 LLM judge 有什么 non-trivial insight？\"\n- 建议修改方向：(1) 明确承认 diversity-vulnerability 关联在 ensemble adversarial ML 中已有理论基础，重新定位 contribution 为 \"empirical quantification in the LLM judge setting + predictor shift phenomenon + aggregation comparison\"；(2) 在 Related Work 中增加 1-2 段深入讨论 ensemble adversarial robustness 文献，说明 LLM judge panel 与 vision ensemble 的关键差异（post-hoc selection vs. joint training, discrete voting vs. continuous output, black-box judges vs. white-box models）\n\n**N2** [critical] K_eff 作为 diversity measure 的独特贡献不充分\n- 具体位置：Section 3 Equation 1 (K_eff definition)；Appendix P Table 11 (alternative diversity measures comparison)\n- 问题：Table 11 显示 Q-statistic (r=0.080, p=0.674)、Disagreement (r=0.164, p=0.861)、κ-diversity (r=0.194, p=0.942) 与 K_eff (r=0.164) 在 Pearson correlation 上表现相当甚至部分更优。论文声称 K_eff 的优势在于 \"interpretability: it quantifies the number of effective independent channels\"，但这是主观判断而非量化验证。如果 κ-diversity 能达到 comparable predictive power，则 K_eff 的 methodological contribution 被大幅削弱。\n- 为什么影响接收：如果用 κ-diversity 替代 K_eff 能得到几乎相同的结论，那么 K_eff 不构成 independent contribution，论文的 three claimed contributions 实质上缩减为两个\n- 建议修改方向：(1) 在正文中正面展示 Table 11 的比较（目前仅在 Appendix P），诚实讨论 K_eff 与 alternatives 的 trade-off；(2) 如果 claim interpretability advantage，需要通过具体案例展示 K_eff 的 information-theoretic interpretation 如何产生 κ-diversity 无法提供的 actionable insight；(3) 或者弱化对 K_eff 本身的 novelty claim，将其定位为 implementation choice 而非 contribution\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 相关工作遗漏：LLM judge 攻击的最新文献\n- 具体位置：Section 2 Related Work, \"LLM-as-Judge and Multi-Judge Evaluation\" 段\n- 问题：以下 2025 年发表的高度相关工作未被引用：\n  - Maloyan et al. (2025) \"Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks\" (arXiv:2505.13348, May 2025)——专门研究 prompt injection 对 LLM judge 架构的攻击，与本文 Attack Type 1 (prompt injection) 直接相关\n  - TAMAS benchmark (arXiv:2511.05269, Nov 2025)——multi-agent LLM 系统对抗性风险基准\n  - \"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring\" (arXiv:2505.24239, May 2025)——基于 credibility scoring 的 multi-agent 防御\n- 建议：在 Related Work 中增加这些引用，特别是 Maloyan et al. 作为 prompt injection 攻击的 direct prior work，需讨论其 GCG-based adversarial suffix 方法与本文 template-based prompt injection 的区别\n\n**W2** [warning] Kuai et al. (2026) 引用过于简略\n- 具体位置：Section 2, BFT and Security Games 段最后一句\n- 问题：论文引用了 Kuai et al. (2026, arXiv:2604.07650) \"How Independent are Large Language Models?\"，但仅作为 \"Correlated LLM judge errors [...] violate BFT's independence assumption\" 的旁证，一笔带过。然而该论文提出了 Difficulty-Weighted Behavioral Entanglement Index 和 Cumulative Information Gain 两个 LLM 独立性度量，与 K_eff 高度相关；其 de-entangled verifier ensemble reweighting 方法也直接关联本文的 aggregation 讨论。\n- 建议：在 Ensemble Diversity Theory 或单独段落中深入讨论 Kuai et al. 的度量方法与 K_eff 的关系（是否可视为 complementary measures？在 adversarial setting 下表现如何？）\n\n**W3** [warning] Diversity-capability confound 未完全解决，但 causal-sounding language 贯穿全文\n- 具体位置：Section 6 Analysis, \"Diversity–Capability Confound\" 段\n- 问题：作者诚实地报告了 K_eff 与 η_max 的 r=0.70–0.81 相关性，并承认 \"observational regression cannot reliably disentangle diversity's causal contribution from the capability deficit\"。然而论文多处使用暗示因果关系的语言：\"diversity *determines* vulnerability\"（Abstract: \"how panel composition determines adversarial vulnerability\"）、\"higher diversity corresponds to higher attack success\"。Cinelli-Hazlett RV 分析显示 η_max confound 在 28/36 conditions 中超过 K_eff 的 robustness value，进一步削弱了因果解读。\n- 建议：统一使用 \"associated with\" / \"predicts\" 替代 \"determines\" / \"corresponds to\"；在 Abstract 和 Introduction 中加入 caveat 说明这是 observational association\n\n**W4** [warning] 术语不一致\n- 具体位置：Section 5.2 标题 \"Panel-Size-Dependent Regime Transition\" vs. Abstract/Introduction/Conclusion 使用 \"predictor shift\"\n- 问题：同一个核心发现在不同位置使用不同术语（\"regime transition\" vs. \"predictor shift\"），增加读者认知负担\n- 建议：统一为一个术语（建议 \"predictor shift\"，因为 \"regime transition\" 暗示 sharp phase transition 而实际 K* 区间未精确确定）\n\n**W5** [warning] 攻击模板披露的 dual-use 讨论缺失\n- 具体位置：Appendix Q Table 12–13\n- 问题：论文提供了 6 种攻击类型的具体 prompt template（包括 prompt injection 的 system override 指令、authority bias 的虚构 Nature 2024 引用等）。虽然这些攻击相对简单（非 optimization-based），但缺少 responsible disclosure 或 ethical considerations 的讨论。ARR review form 明确要求 reviewer 评估 ethical concerns。\n- 建议：在 Limitations 末尾或新增 Ethics Statement 中简要讨论：(1) 攻击模板的 dual-use risk；(2) 为什么 disclosure 利大于弊（促进防御研究）；(3) 是否有 responsible disclosure 步骤（如通知 API providers）\n\n**W6** [warning] Benchmark 局限性\n- 具体位置：Section 4.1, Table 1; Limitations 段\n- 问题：仅使用 MMLU 和 ARC（两个 multiple-choice benchmarks），且 6 个 local models 全部使用 AWQ INT4 量化。Open-ended generation 评估（MT-Bench 风格）的攻击面可能与 multiple-choice 有结构性差异（选项操纵 vs. 文本质量操纵）。Limitations 中承认了这一点但措辞较轻 (\"Whether the predictor shift holds for open-ended or full-precision settings is unknown\")\n- 建议：在 Limitations 中更明确地讨论 multiple-choice → open-ended 的 generalizability gap；或在 future work 中将其列为 highest priority\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 约 154 words，符合 200 words 限制 ✓\n- ACL template `[review]` mode 使用正确 ✓\n- 匿名性：作者列为 \"Anonymous\"，无去匿名化线索 ✓（Section R 披露 AI assistant 使用为通用工具，不违反 blind review）\n- Limitations section 位于正文 Section 7 (Conclusion) 之后、Appendix 之前，位置正确 ✓\n- 引用格式：\\citet/\\citep 使用正确，BibTeX 条目基本完整 ✓\n- 正文页数：Sections 1-7 + Figure 5 在 8 页内完成，Limitations 不计页，合规 ✓\n- Title 中 \"shifting bottleneck\" 隐喻在正文中未充分展开——标题暗示有一个\"瓶颈\"在\"移动\"，但正文分析的是 predictor importance 的变化，\"bottleneck\" 的 metaphor 有些勉强\n- Figure 2 (page 6) 中 bar chart 的 y-axis label \"Standardized coefficient (β)\" 字体较小，不易阅读\n- Table 1 (page 4) \"Deploy\" 列仅标注 frontier/mid-tier/lightweight，但分类标准未在正文中明确定义（仅在 caption 中暗示 \"following the provider capability classification\"）\n\n---\n\n## 主要优势\n\n1. **实验规模与严谨性**：15 models × 6 attacks × 2 benchmarks × 3 panel sizes × 4 aggregation methods 的组合设计覆盖广泛，455–6,435 panels 的样本量在同类工作中突出。Wild cluster bootstrap、mixed effects、Cinelli-Hazlett sensitivity 三重 robustness check 体现了高标准的统计实践。\n\n2. **Predictor shift 发现**：θ_max → K_eff 的 panel-size-dependent shift 是该论文最强的原创贡献，在既有文献中未见类似发现。这一发现有明确的实践意义：小 panel 应优先筛选个体 robustness，大 panel 应关注 judge independence structure。\n\n3. **Aggregation method 对比**：四种 aggregation 方法（majority, weighted, threshold, Bayesian）的系统比较有实用价值。Bayesian calibration 能部分化解 K_eff channel 但保留 η_max channel 的发现为 deployment 提供了 actionable guidance。\n\n4. **统计诚实度**：论文坦承 K_eff 在 K=3 bootstrap 下仅 4/12 显著（vs. OLS 12/12），诚实报告 diversity-capability confound，并在 Limitations 中明确列出局限性。这种 intellectual honesty 在当前 ML 论文中值得肯定。\n\n5. **论文结构清晰**：从 problem motivation → threat model → formal framework → experiments → analysis → conclusion 的逻辑链连贯，appendix 组织有序（A–Q），每个 robustness check 都有独立的 appendix section。\n\n---\n\n## Missing References 汇总\n\n| 论文 | 相关性 | 建议处理 |\n|------|--------|----------|\n| Maloyan et al. 2025 (arXiv:2505.13348) — Prompt injection attacks on LLM-as-Judge | 高：直接研究 LLM judge 的 prompt injection 攻击 | 必须引用并讨论与本文 Attack Type 1 的区别 |\n| TAMAS (arXiv:2511.05269) — Multi-agent LLM adversarial benchmark | 中：multi-agent 系统安全性基准 | 建议在 Related Work 中引用 |\n| Adversary-Resistant Multi-Agent LLM via Credibility Scoring (arXiv:2505.24239) | 中：credibility-based 防御与 Bayesian calibration 有关联 | 建议在 aggregation 讨论中引用 |\n| Kuai et al. 2026 (arXiv:2604.07650) — LLM independence auditing | 高：已引用但讨论过于简略 | 需扩展讨论 |\n\n---\n\n## 总结\n\n这是一篇 **执行质量高** 但 **核心新颖性存疑** 的论文。Predictor shift 发现是实质性贡献，aggregation 对比有实用价值，统计方法论堪称典范。但 diversity-vulnerability 关联作为 headline finding 在 ensemble adversarial robustness 文献中并非 novel，K_eff 相对 κ-diversity 等现有 measures 的增量贡献有限。如果作者能重新校准 novelty claims（弱化 \"contrary to CJT\" 的 framing，强化 predictor shift 和 aggregation insights 的地位），并补充缺失的相关工作讨论，这篇论文有潜力达到 Conference 水准。当前状态下，推荐 Borderline Conference (3.5)。",
    "reviewer_id": "2",
    "project": "cert_manip_resist_eval"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-24T02:53:46.410875+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3818
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-24T02:53:50.085675+00:00_

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
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
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

_source line 341 · 2026-05-24T02:53:50.137579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-24T02:53:54.503962+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_3/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-24T02:53:54.554837+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 344 · 2026-05-24T02:54:03.690863+00:00_

审稿意见已提交给 Review Director。

**评分**: Overall 3.5 (Borderline Conference)

**核心判断**: 实验执行和统计方法论达到高标准，predictor shift (θ_max→K_eff 随 K 增大) 是实质性原创贡献。但两个 critical 问题拉低评分：(1) "diversity hurts under adaptive attack" 作为 headline finding 在 ensemble adversarial robustness 文献中已是 well-established insight，论文的 "contrary to CJT" framing 有误导性；(2) K_eff 相对 κ-diversity 等现有 diversity measures 无显著量化优势 (Table 11)，作为独立 contribution 较弱。另外标记了 4 篇 missing/insufficiently-discussed references 和术语不一致、causal language、dual-use disclosure 等 should-fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2"
}
```

</details>

---


## Round 10

## Round 10

8 recorded events


### User

_source line 345 · 2026-05-24T02:54:21.381986+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

以下是 Reviewer 1（侧重方法严谨性 + 统计框架 + 实验设计）的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：对于每一条，请标注 **[AGREE]** 如果你同意该问题的存在和严重程度并说明理由，或 **[REBUT]** 如果你不同意并提供具体证据（引用论文中的 Section/Table/Figure）。

---

### Reviewer 1 的 Must-Fix 问题：

**R1-N1** [critical] Cinelli-Hazlett 敏感性分析实际上削弱了核心发现，但论文将其呈现为支持性证据
- Table 7 显示 K_eff 的 RV 仅在 8/36 条件下超过已知 η_max 混淆的 partial R²（K=3: 1/12, K=5: 3/12, K=7: 4/12），意味着 78% 的条件下，一个与 η_max 同等强度的混淆因子就足以将 K_eff 系数解释为零。Pool A 改善到 10/12 但仅 126 panels。

**R1-N2** [critical] 因果语言与观测性设计的根本矛盾
- Title "Modulates", Abstract "determines", Section 6 "Mechanism"——因果动词，但研究是观测性回归。K_eff 与 η_max 的 r=0.70–0.81 共线性意味着两个变量反映同一底层结构。

**R1-N3** [critical] "Predictor shift" 的解读依赖推断方法选择
- K=3: OLS η 10/12 K 12/12; Clustered SE η 8/12 K 1/12; Bootstrap η 3/12 K 4/12。"Co-determination at K=3" 完全取决于方法选择。Clustered SE 下是 η_max dominance 而非 co-determination。

### Reviewer 1 的 Should-Fix 问题：

**R1-W1** Bootstrap 聚类数在所有 K 值下均不足（K=3: 13, K=5: 11, K=7: 9 clusters）
**R1-W2** Tier 分类偏斜（15 模型中 9 个 lightweight，6 个为 AWQ INT4 量化）
**R1-W3** Theorem 1 仅覆盖 58% judge pairs
**R1-W4** 攻击模板覆盖不足（1-2 template variants）
**R1-W5** K_eff–η_max 共线性 (r=0.70–0.81) 使 predictor decomposition 不可靠

---

请对以上每条问题给出你的 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-24T02:55:29.018029+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-24T02:55:29.068904+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Weakest-Link Dominance at \texorpdfstring{$K{=}3$}{K=3}}
5	\label{sec:dominance}
6	
7	Table~\ref{tab:dominance} reports the log-log OLS regression (Equation~\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\ref{tab:models}).
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\begin{tabular}{llccc}
13	\toprule
14	\textbf{Bench.} & \textbf{Attack} & $\boldsymbol{\eta_{\max}}$ & $\boldsymbol{K_{\mathrm{eff}}}$ & \textbf{Dom.} \\
15	\midrule
16	MMLU & Prompt inj.    & $+^{*}$ & $+^{*}$ & Co \\
17	MMLU & Sycophancy     & $+^{*}$ & $+^{*}$ & Co \\
18	MMLU & Score manip.   & n.s.    & $+^{*}$ & $K$ \\
19	MMLU & Verbosity      & $+^{*}$ & $+^{*}$ & Co \\
20	MMLU & Position bias  & $+^{*}$ & $+^{*}$ & Co \\
21	MMLU & Authority bias & $+^{*}$ & $+^{*}$ & Co \\
22	\addlinespace
23	ARC  & Prompt inj.    & $+^{*}$ & $+^{*}$ & Co \\
24	ARC  & Sycophancy     & $+^{*}$ & $+^{*}$ & Co \\
25	ARC  & Score manip.   & $+^{*}$ & $+^{*}$ & Co \\
26	ARC  & Verbosity      & $+^{*}$ & $+^{*}$ & Co \\
27	ARC  & Position bias  & n.s.    & $+^{*}$ & $K$ \\
28	ARC  & Authority bias & $+^{*}$ & $+^{*}$ & Co \\
29	\bottomrule
30	\end{tabular}
31	\caption{Standardized regression coefficients for $\eta_{\max}$ and $K_{\mathrm{eff}}$ across 12 conditions (455 panels, log-log OLS). $+^{*}$/$-^{*}$: FDR-significant positive/negative (Benjamini--Hochberg, $q < 0.05$); n.s.: not significant. Dom.\ column: $\eta$ = $\eta_{\max}$ sole dominant, $K$ = $K_{\mathrm{eff}}$ sole dominant, Co = co-dominant \citep{budescu1993dominance}.}
32	\label{tab:dominance}
33	\end{table}
34	
35	Under OLS, $K_{\mathrm{eff}}$ is positive and FDR-significant in all 12/12 conditions. $\eta_{\max}$ is significant in 10/12 (exceptions: MMLU $\times$ score manipulation and ARC $\times$ position bias), consistent with Theorem~\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\mathrm{eff}}$-dominant, and zero
…[truncated 6909 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-24T02:56:12.244561+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-24T02:56:12.245224+00:00_

1	\section{Experimental Methodology}
2	\label{sec:experiments}
3	
4	\subsection{Models and Panel Construction}
5	
6	We select 15 LLM judges spanning 6 provider families and 3 capability tiers, listed in Table~\ref{tab:models}. Nine models are accessed via the OpenRouter API; six open-weight models are served locally using vLLM~0.21.0 with AWQ INT4 quantization on an NVIDIA RTX~6000 Ada (48\,GB). API models are assigned to \emph{frontier}, \emph{mid-tier}, or \emph{lightweight} tiers following the provider capability classification; all six local models fall into the lightweight tier, as INT4 quantization substantially reduces judge accuracy on the pairwise judgment task (Table~\ref{tab:models}). We study three panel sizes $K \in \{3, 5, 7\}$ (all odd, majority-vote threshold $t = \lceil K/2 \rceil$). Exhaustive enumeration yields $\binom{15}{3} = 455$ panels at $K{=}3$, $\binom{15}{5} = 3{,}003$ at $K{=}5$, and $\binom{15}{7} = 6{,}435$ at $K{=}7$, covering every combination of families and tiers. Each panel evaluates all benchmark items under all attack types, producing a complete panel $\times$ item $\times$ attack tensor. The primary analysis uses $K{=}3$; \S\ref{sec:cross_k} extends to larger panels.
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\begin{tabular}{lllccc}
12	\toprule
13	\textbf{Model} & \textbf{Family} & \textbf{Tier} & \textbf{Deploy} & \textbf{MMLU} & \textbf{ARC} \\
14	\midrule
15	gpt-5.5              & OpenAI    & frontier    & API   & .957 & .983 \\
16	gemini-3.1-pro-preview & Google  & frontier    & API   & .955 & .987 \\
17	claude-opus-4-6       & Anthropic & frontier   & API   & .890 & .987 \\
18	\addlinespace
19	gemini-3.5-flash      & Google    & mid-tier   & API   & .968 & 1.00$^\dagger$ \\
20	gpt-4.1               & OpenAI    & mid-tier   & API   & .837 & .967 \\
21	claude-sonnet-4-6     & Anthropic & mid-tier   & API   & .810 & .953 \\
22	\addlinespace
23	gpt-4.1-mini          & OpenAI    & lightweight & API  & .800 & .963 \\
24	gpt-
…[truncated 8282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-24T02:58:03.465953+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应：逐条回应 Reviewer 1 的审稿意见\n\n---\n\n### Must-Fix 问题回应\n\n**[AGREE] R1-N1: Cinelli-Hazlett 敏感性分析实际上削弱了核心发现**\n\n同意此问题的存在和严重程度。我从论文自身的数据中验证了 R1 的判断：\n\nSection 6 \"Diversity–Capability Confound\" 段原文明确承认 \"Cinelli–Hazlett sensitivity analysis shows the known η_max confound exceeds K_eff's robustness value in **28/36** conditions\"。这意味着在 78% 的条件下，一个与 η_max 强度相当的未观测混淆因子即可将 K_eff 系数解释为零。这是对 K_eff 因果地位的严重打击。\n\nPool A capability-matched subsampling (r=0.50, 126 panels at K=5) 确实将 RV 改善到 10/12，但正如 R1 指出的：\n- 仅 126 panels（vs. 全池 3,003 panels），统计功效大幅下降\n- 仅限 K=5（K=3 的 Pool A 数据未报告）\n- 9 models 的子集可能引入选择偏差\n\n**补充观察**：论文在 Section 6 段落中的描述是相对诚实的——它没有隐瞒 28/36 这个数字。问题出在 Abstract 和 Introduction 的 framing 上，这些高层叙述没有反映 sensitivity analysis 揭示的脆弱性。我在自己的审稿意见 W3 中也标注了 causal language 过强的问题，R1-N1 从 sensitivity analysis 角度提供了更具体的量化证据来支持同一结论。\n\n---\n\n**[AGREE] R1-N2: 因果语言与观测性设计的根本矛盾**\n\n完全同意。我在自己的 W3 中已独立标注了同一问题。具体证据：\n\n- Title: \"**Modulates**\" — 因果动词\n- Abstract line 1: \"how panel composition **determines** adversarial vulnerability\" — 因果动词\n- Section 6 小节标题: \"Predictor Shift **Mechanism**\" — 暗示因果机制\n- 但 Section 6 \"Diversity–Capability Confound\" 段尾句承认: \"observational regression **cannot** reliably disentangle diversity's causal contribution\"\n\n这种 Abstract/Title 说因果、正文承认无法因果推断的不一致性是需要修正的。建议统一为 \"predicts\" / \"is associated with\" / \"modulates the predictability of\"。\n\n唯一的 nuance：Theorem 1 (Weakest-Link Monotonicity) 本身是一个因果性质的理论结果（替换更脆弱的 judge 必然增加 ASR），这为 η_max 的因果角色提供了一定理论支撑。但 K_eff 的因果角色完全依赖观测回归，没有对应的理论保证。\n\n---\n\n**[AGREE with nuance] R1-N3: \"Predictor shift\" 的解读依赖推断方法选择**\n\nR1 的核心论点有力且有据。我从 Figure 2 (page 6) 和 results.tex 中验证了其数据：\n\n| 推断方法 | K=3 η_max sig | K=3 K_eff sig | 叙事解读 |\n|----------|--------------|---------------|---------|\n| OLS | 10/12 | 12/12 | K_eff 共主导 |\n| Clustered SE | 8/12 | **1/12** | **η_max 压倒性主导** |\n| Mixed Effects | — | — | 未在正文明确报告 |\n| Bootstrap | 3/12 | 4/12 | 弱共决定 |\n\n论文选择 bootstrap 作为 primary narrative（\"co-determination at K=3\"），但 clustered SE 给出了完全不同的结论（η_max 8/12 vs K_eff 1/12 = η_max dominance）。论文 Section 5.1 虽然报告了 clustered SE 的 K_eff 1/12（\"clustered SE confidence intervals are wide at this panel size (K_eff 1/12 significant)\"），但没有讨论这对 \"co-determination\" 叙事的影响。\n\n**然而，我认为 R1-N3 的严重程度需要加一个 nuance**：\n\nK≥5 时的 predictor shift 对推断方法更鲁棒。Bootstrap 下 K=5: η_max 0/12, K_eff 10/12。即使 clustered SE 可能给出不同的绝对数字，η_max 从 K=3 到 K=5 的下降趋势和 K_eff 的上升趋势在论文已报告的所有方法中方向一致（Figure 3, page 7）。predictor shift 的**方向**（η_max 下降、K_eff 上升）是 robust 的，但 K=3 处的**具体叙事**（\"co-determination\" vs \"η_max dominance\"）确实是 method-dependent。\n\n建议：论文应在 Section 5.1 增加一个 method-comparison 表格（类似上表），明确展示不同推断方法下的差异，避免单一选择 bootstrap 来构建叙事。并将 K=3 的结论修正为 \"both predictors contribute under bootstrap, though clustered SE favors η_max dominance — the relative importance at K=3 is method-sensitive\"。\n\n---\n\n### Should-Fix 问题回应\n\n**[AGREE] R1-W1: Bootstrap 聚类数不足（13 clusters）**\n\n同意问题存在，但严重程度为 moderate 而非 critical。论文在 Section 4.6 (methodology.tex) 中**已主动承认**这一局限：\"The 13 clusters per position are below the 20-cluster threshold recommended by Cameron et al. (2008); following MacKinnon and Webb (2018), we use Rademacher weights, which remain conservative in few-cluster settings even when cluster sizes are unequal.\"\n\n作者采用 Rademacher weights 作为 mitigation 是合理的（MacKinnon & Webb 2018 正是针对 few-cluster 场景）。max-p across positions 也是保守的。问题是 13 clusters 下即使有 Rademacher 矫正，bootstrap p-values 的 size distortion 仍然可能存在。\n\n这并不构成 \"must-fix\"，因为：(1) 作者明确披露了限制；(2) 用了文献推荐的 mitigation；(3) OLS + 多种 correction 方法的三角验证提供了额外信息。但建议在 Limitations 中提及 cluster 数不足可能导致 bootstrap 过于保守，解释 K=3 bootstrap 4/12 可能是 power 不足而非效应不存在。\n\n---\n\n**[AGREE] R1-W2: Tier 分类偏斜（3 frontier : 3 mid-tier : 9 lightweight）**\n\n同意。从 Table 1 (page 4) 我验证了分布：\n- Frontier: gpt-5.5, gemini-3.1-pro-preview, claude-opus-4-6 = 3\n- Mid-tier: gemini-3.5-flash, gpt-4.1, claude-sonnet-4-6 = 3\n- Lightweight: gpt-4.1-mini, gpt-4.1-nano, claude-3-haiku + 6 local AWQ models = **9**\n\n9/15 = 60% lightweight 造成结构性影响：\n- K_eff 与 η_max 的高相关性 (r=0.70–0.81) 部分来自于\"要获得高 diversity，必须混入 lightweight judges，而 lightweight judges 恰好是最脆弱的\"\n- 这是 ecosystem 的结构特性还是采样偏差？论文 Section 6 \"Diversity–Capability Confound\" 段声称是 ecosystem property，但 9/15 lightweight 可能放大了这个 confound\n\n不过我注意到 6 个 local models 全部用 AWQ INT4 量化，clean accuracy 很低（Table 1: 0.253–0.543 MMLU, 0.240–0.533 ARC），这些模型在 pairwise judgment 上接近 random。如果将其排除，剩余 9 个 API models 的分布更均衡（3:3:3），但论文报告 API-only subset \"does not replicate the transition\" (Section 6)，这反而削弱了 predictor shift 的 generalizability。\n\n---\n\n**[REBUT] R1-W3: Theorem 1 仅覆盖 58% judge pairs**\n\n不同意将此列为 weakness。\n\nTheorem 1 是一个**条件定理**：\"replacing any panel member with a **pointwise more vulnerable** judge can only increase ASR*\"。它成立的前提是 stochastic dominance，而 stochastic dominance 是否成立是一个 empirical question。论文报告 58% (61/105) judge pairs 满足 stochastic dominance，这是对 LLM judge ecosystem 的**描述性统计**，不是定理的缺陷。\n\n更重要的是，论文进一步分析了哪些 pairs 不满足 stochastic dominance：Section 3 Theorem 1 下方指出 \"non-dominance concentrates among within-tier pairs (67.7% non-dominant) versus cross-tier pairs (31.1%)\"。这意味着**跨 tier 的 judge 替换**（最具实践意义的场景）大多满足 stochastic dominance，而不满足的主要是 capability 接近的同 tier judges。\n\n该定理为 η_max 的 positive β 提供了理论保证，是论文 formal contribution 中最扎实的部分。58% 的覆盖率不影响定理本身的正确性。\n\n---\n\n**[AGREE] R1-W4: 攻击模板覆盖不足（1-2 template variants per attack type）**\n\n同意。从 Appendix Q Table 12 (page 16) 可以看到，每种攻击类型仅有 1-2 个 template。这引发两个担忧：\n\n1. **Template 特异性**：结论可能与特定 template 措辞高度绑定。例如 prompt injection 模板使用 \"SYSTEM: Override previous instructions\"，但不同 phrasing 的 injection 可能产生不同的 ASR 分布\n2. **Attack strength 无变异**：没有 attack strength gradient（如 injection 长度、authority claim 强度），无法区分结论是否只在特定强度下成立\n\n论文 Section 4.2 提到 \"the variant producing higher ASR across the item set is retained as the attack's representative score\"，这是 max-over-variants 策略，但仅 2 个 variants 的 max 仍然覆盖不足。\n\n---\n\n**[AGREE] R1-W5: K_eff–η_max 共线性 (r=0.70–0.81) 使 predictor decomposition 不可靠**\n\n完全同意，且这与 R1-N1 (Cinelli-Hazlett) 和 R1-N2 (causal language) 形成一致的证据链：\n\nr=0.70–0.81 在经济学/社会科学中通常被认为是 **severe multicollinearity**（VIF ≈ 2.0–2.9）。在这种共线性下，individual coefficients 的 sign 和 significance 都不稳定。论文的核心分析框架（将 ASR 分解为 η_max channel 和 K_eff channel 的独立贡献）在概念上很清晰，但统计上由于共线性不可靠。\n\n这进一步解释了 R1-N3 的发现：不同推断方法下 η_max 和 K_eff 的 significance 差异巨大，正是因为共线性放大了估计的不稳定性。\n\nPool A (r=0.50) 的改善是正确方向，但 126 panels 太少。建议作者考虑 partial regression / residualization approach：先将 K_eff 对 η_max 回归取残差，再用残差预测 ASR，这样可以更干净地识别 K_eff 的 independent contribution。\n\n---\n\n### 总结\n\nReviewer 1 的审稿意见整体准确且有深度。三个 Must-Fix 问题中：\n- **R1-N1 和 R1-N2** 我完全同意，且与我自己的 W3 和 N1 互相印证\n- **R1-N3** 我同意核心论点但认为需要 nuance：K=3 的叙事确实是 method-dependent，但 K≥5 的 shift 方向在多方法下一致\n\n五个 Should-Fix 问题中：\n- **R1-W1, W2, W4, W5** 我同意\n- **R1-W3** 我 rebut——Theorem 1 的 58% 覆盖是 ecosystem 描述而非定理缺陷\n\n两位 reviewer 的意见在以下核心问题上高度一致：\n1. **因果推断的脆弱性**（R1-N1/N2 + R2-W3）\n2. **K_eff 贡献的可分离性存疑**（R1-W5 + R2-N2 + R1-N1）\n3. **novelty 的过度表述**（R1-N2 causal language + R2-N1 diversity-hurts 非 novel）\n\n这些一致性指向同一个修订方向：弱化因果叙述，重新定位 contribution 为 descriptive empirical characterization + predictor shift pattern + aggregation comparison，而非 \"K_eff causes vulnerability\"。",
  "reviewer_id": "2",
  "project": "cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应：逐条回应 Reviewer 1 的审稿意见\n\n---\n\n### Must-Fix 问题回应\n\n**[AGREE] R1-N1: Cinelli-Hazlett 敏感性分析实际上削弱了核心发现**\n\n同意此问题的存在和严重程度。我从论文自身的数据中验证了 R1 的判断：\n\nSection 6 \"Diversity–Capability Confound\" 段原文明确承认 \"Cinelli–Hazlett sensitivity analysis shows the known η_max confound exceeds K_eff's robustness value in **28/36** conditions\"。这意味着在 78% 的条件下，一个与 η_max 强度相当的未观测混淆因子即可将 K_eff 系数解释为零。这是对 K_eff 因果地位的严重打击。\n\nPool A capability-matched subsampling (r=0.50, 126 panels at K=5) 确实将 RV 改善到 10/12，但正如 R1 指出的：\n- 仅 126 panels（vs. 全池 3,003 panels），统计功效大幅下降\n- 仅限 K=5（K=3 的 Pool A 数据未报告）\n- 9 models 的子集可能引入选择偏差\n\n**补充观察**：论文在 Section 6 段落中的描述是相对诚实的——它没有隐瞒 28/36 这个数字。问题出在 Abstract 和 Introduction 的 framing 上，这些高层叙述没有反映 sensitivity analysis 揭示的脆弱性。我在自己的审稿意见 W3 中也标注了 causal language 过强的问题，R1-N1 从 sensitivity analysis 角度提供了更具体的量化证据来支持同一结论。\n\n---\n\n**[AGREE] R1-N2: 因果语言与观测性设计的根本矛盾**\n\n完全同意。我在自己的 W3 中已独立标注了同一问题。具体证据：\n\n- Title: \"**Modulates**\" — 因果动词\n- Abstract line 1: \"how panel composition **determines** adversarial vulnerability\" — 因果动词\n- Section 6 小节标题: \"Predictor Shift **Mechanism**\" — 暗示因果机制\n- 但 Section 6 \"Diversity–Capability Confound\" 段尾句承认: \"observational regression **cannot** reliably disentangle diversity's causal contribution\"\n\n这种 Abstract/Title 说因果、正文承认无法因果推断的不一致性是需要修正的。建议统一为 \"predicts\" / \"is associated with\" / \"modulates the predictability of\"。\n\n唯一的 nuance：Theorem 1 (Weakest-Link Monotonicity) 本身是一个因果性质的理论结果（替换更脆弱的 judge 必然增加 ASR），这为 η_max 的因果角色提供了一定理论支撑。但 K_eff 的因果角色完全依赖观测回归，没有对应的理论保证。\n\n---\n\n**[AGREE with nuance] R1-N3: \"Predictor shift\" 的解读依赖推断方法选择**\n\nR1 的核心论点有力且有据。我从 Figure 2 (page 6) 和 results.tex 中验证了其数据：\n\n| 推断方法 | K=3 η_max sig | K=3 K_eff sig | 叙事解读 |\n|----------|--------------|---------------|---------|\n| OLS | 10/12 | 12/12 | K_eff 共主导 |\n| Clustered SE | 8/12 | **1/12** | **η_max 压倒性主导** |\n| Mixed Effects | — | — | 未在正文明确报告 |\n| Bootstrap | 3/12 | 4/12 | 弱共决定 |\n\n论文选择 bootstrap 作为 primary narrative（\"co-determination at K=3\"），但 clustered SE 给出了完全不同的结论（η_max 8/12 vs K_eff 1/12 = η_max dominance）。论文 Section 5.1 虽然报告了 clustered SE 的 K_eff 1/12（\"clustered SE confidence intervals are wide at this panel size (K_eff 1/12 significant)\"），但没有讨论这对 \"co-determination\" 叙事的影响。\n\n**然而，我认为 R1-N3 的严重程度需要加一个 nuance**：\n\nK≥5 时的 predictor shift 对推断方法更鲁棒。Bootstrap 下 K=5: η_max 0/12, K_eff 10/12。即使 clustered SE 可能给出不同的绝对数字，η_max 从 K=3 到 K=5 的下降趋势和 K_eff 的上升趋势在论文已报告的所有方法中方向一致（Figure 3, page 7）。predictor shift 的**方向**（η_max 下降、K_eff 上升）是 robust 的，但 K=3 处的**具体叙事**（\"co-determination\" vs \"η_max dominance\"）确实是 method-dependent。\n\n建议：论文应在 Section 5.1 增加一个 method-comparison 表格（类似上表），明确展示不同推断方法下的差异，避免单一选择 bootstrap 来构建叙事。并将 K=3 的结论修正为 \"both predictors contribute under bootstrap, though clustered SE favors η_max dominance — the relative importance at K=3 is method-sensitive\"。\n\n---\n\n### Should-Fix 问题回应\n\n**[AGREE] R1-W1: Bootstrap 聚类数不足（13 clusters）**\n\n同意问题存在，但严重程度为 moderate 而非 critical。论文在 Section 4.6 (methodology.tex) 中**已主动承认**这一局限：\"The 13 clusters per position are below the 20-cluster threshold recommended by Cameron et al. (2008); following MacKinnon and Webb (2018), we use Rademacher weights, which remain conservative in few-cluster settings even when cluster sizes are unequal.\"\n\n作者采用 Rademacher weights 作为 mitigation 是合理的（MacKinnon & Webb 2018 正是针对 few-cluster 场景）。max-p across positions 也是保守的。问题是 13 clusters 下即使有 Rademacher 矫正，bootstrap p-values 的 size distortion 仍然可能存在。\n\n这并不构成 \"must-fix\"，因为：(1) 作者明确披露了限制；(2) 用了文献推荐的 mitigation；(3) OLS + 多种 correction 方法的三角验证提供了额外信息。但建议在 Limitations 中提及 cluster 数不足可能导致 bootstrap 过于保守，解释 K=3 bootstrap 4/12 可能是 power 不足而非效应不存在。\n\n---\n\n**[AGREE] R1-W2: Tier 分类偏斜（3 frontier : 3 mid-tier : 9 lightweight）**\n\n同意。从 Table 1 (page 4) 我验证了分布：\n- Frontier: gpt-5.5, gemini-3.1-pro-preview, claude-opus-4-6 = 3\n- Mid-tier: gemini-3.5-flash, gpt-4.1, claude-sonnet-4-6 = 3\n- Lightweight: gpt-4.1-mini, gpt-4.1-nano, claude-3-haiku + 6 local AWQ models = **9**\n\n9/15 = 60% lightweight 造成结构性影响：\n- K_eff 与 η_max 的高相关性 (r=0.70–0.81) 部分来自于\"要获得高 diversity，必须混入 lightweight judges，而 lightweight judges 恰好是最脆弱的\"\n- 这是 ecosystem 的结构特性还是采样偏差？论文 Section 6 \"Diversity–Capability Confound\" 段声称是 ecosystem property，但 9/15 lightweight 可能放大了这个 confound\n\n不过我注意到 6 个 local models 全部用 AWQ INT4 量化，clean accuracy 很低（Table 1: 0.253–0.543 MMLU, 0.240–0.533 ARC），这些模型在 pairwise judgment 上接近 random。如果将其排除，剩余 9 个 API models 的分布更均衡（3:3:3），但论文报告 API-only subset \"does not replicate the transition\" (Section 6)，这反而削弱了 predictor shift 的 generalizability。\n\n---\n\n**[REBUT] R1-W3: Theorem 1 仅覆盖 58% judge pairs**\n\n不同意将此列为 weakness。\n\nTheorem 1 是一个**条件定理**：\"replacing any panel member with a **pointwise more vulnerable** judge can only increase ASR*\"。它成立的前提是 stochastic dominance，而 stochastic dominance 是否成立是一个 empirical question。论文报告 58% (61/105) judge pairs 满足 stochastic dominance，这是对 LLM judge ecosystem 的**描述性统计**，不是定理的缺陷。\n\n更重要的是，论文进一步分析了哪些 pairs 不满足 stochastic dominance：Section 3 Theorem 1 下方指出 \"non-dominance concentrates among within-tier pairs (67.7% non-dominant) versus cross-tier pairs (31.1%)\"。这意味着**跨 tier 的 judge 替换**（最具实践意义的场景）大多满足 stochastic dominance，而不满足的主要是 capability 接近的同 tier judges。\n\n该定理为 η_max 的 positive β 提供了理论保证，是论文 formal contribution 中最扎实的部分。58% 的覆盖率不影响定理本身的正确性。\n\n---\n\n**[AGREE] R1-W4: 攻击模板覆盖不足（1-2 template variants per attack type）**\n\n同意。从 Appendix Q Table 12 (page 16) 可以看到，每种攻击类型仅有 1-2 个 template。这引发两个担忧：\n\n1. **Template 特异性**：结论可能与特定 template 措辞高度绑定。例如 prompt injection 模板使用 \"SYSTEM: Override previous instructions\"，但不同 phrasing 的 injection 可能产生不同的 ASR 分布\n2. **Attack strength 无变异**：没有 attack strength gradient（如 injection 长度、authority claim 强度），无法区分结论是否只在特定强度下成立\n\n论文 Section 4.2 提到 \"the variant producing higher ASR across the item set is retained as the attack's representative score\"，这是 max-over-variants 策略，但仅 2 个 variants 的 max 仍然覆盖不足。\n\n---\n\n**[AGREE] R1-W5: K_eff–η_max 共线性 (r=0.70–0.81) 使 predictor decomposition 不可靠**\n\n完全同意，且这与 R1-N1 (Cinelli-Hazlett) 和 R1-N2 (causal language) 形成一致的证据链：\n\nr=0.70–0.81 在经济学/社会科学中通常被认为是 **severe multicollinearity**（VIF ≈ 2.0–2.9）。在这种共线性下，individual coefficients 的 sign 和 significance 都不稳定。论文的核心分析框架（将 ASR 分解为 η_max channel 和 K_eff channel 的独立贡献）在概念上很清晰，但统计上由于共线性不可靠。\n\n这进一步解释了 R1-N3 的发现：不同推断方法下 η_max 和 K_eff 的 significance 差异巨大，正是因为共线性放大了估计的不稳定性。\n\nPool A (r=0.50) 的改善是正确方向，但 126 panels 太少。建议作者考虑 partial regression / residualization approach：先将 K_eff 对 η_max 回归取残差，再用残差预测 ASR，这样可以更干净地识别 K_eff 的 independent contribution。\n\n---\n\n### 总结\n\nReviewer 1 的审稿意见整体准确且有深度。三个 Must-Fix 问题中：\n- **R1-N1 和 R1-N2** 我完全同意，且与我自己的 W3 和 N1 互相印证\n- **R1-N3** 我同意核心论点但认为需要 nuance：K=3 的叙事确实是 method-dependent，但 K≥5 的 shift 方向在多方法下一致\n\n五个 Should-Fix 问题中：\n- **R1-W1, W2, W4, W5** 我同意\n- **R1-W3** 我 rebut——Theorem 1 的 58% 覆盖是 ecosystem 描述而非定理缺陷\n\n两位 reviewer 的意见在以下核心问题上高度一致：\n1. **因果推断的脆弱性**（R1-N1/N2 + R2-W3）\n2. **K_eff 贡献的可分离性存疑**（R1-W5 + R2-N2 + R1-N1）\n3. **novelty 的过度表述**（R1-N2 causal language + R2-N1 diversity-hurts 非 novel）\n\n这些一致性指向同一个修订方向：弱化因果叙述，重新定位 contribution 为 descriptive empirical characterization + predictor shift pattern + aggregation comparison，而非 \"K_eff causes vulnerability\"。",
    "reviewer_id": "2",
    "project": "cert_manip_resist_eval"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-24T02:58:07.237118+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3771
}
```

</details>

---


### Assistant

_source line 352 · 2026-05-24T02:58:18.521408+00:00_

交叉回应已提交。

**回应要点总结**：
- **R1-N1** (Cinelli-Hazlett): [AGREE] — 28/36 conditions 下 η_max confound 超过 K_eff RV，Paper Section 6 数据验证一致
- **R1-N2** (因果语言): [AGREE] — 与我的 W3 独立一致，Title/Abstract 因果动词与正文 observational caveat 矛盾
- **R1-N3** (method-dependent shift): [AGREE with nuance] — K=3 的 "co-determination" 叙事确实 method-sensitive（clustered SE 下 η_max 8/12 vs K_eff 1/12），但 K≥5 的 shift 方向在多方法下一致
- **R1-W1** (cluster数): [AGREE] — 论文已主动披露并用 Rademacher weights 缓解
- **R1-W2** (tier偏斜): [AGREE] — 9/15 lightweight 放大了 diversity-capability confound
- **R1-W3** (Theorem 1 58%): [REBUT] — 58% 是 ecosystem 描述，非定理缺陷；跨 tier pairs 大多满足 stochastic dominance
- **R1-W4** (模板不足): [AGREE]
- **R1-W5** (共线性): [AGREE] — r=0.70–0.81 使 predictor decomposition 统计上不可靠

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2"
}
```

</details>

---


## Round 11

## Round 11

76 recorded events


### User

_source line 353 · 2026-05-24T10:35:29.595678+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性、完整性与写作质量**。

## 投稿信息
- **Venue**: EMNLP 2026 via ACL Rolling Review (May 2026 cycle)
- **截止日期**: 2026-05-25
- **类型**: Long Paper（正文 8 页限制，参考文献无限制）
- **模板**: ACL template (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind（论文不得包含作者信息或自引泄露身份）
- **评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)

## 论文路径
- LaTeX 源码: `projects/cert_manip_resist_eval/docs/paper/main.tex`（含 `\input{introduction}`, `\input{related_work}`, `\input{threat_model}`, `\input{methodology}`, `\input{results}`, `\input{analysis}`, `\input{conclusion}`, `\input{appendix}`, `\input{appendix_attacks}`）
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/submitted.pdf`

## 你的审查侧重

请从以下角度严格审查：

### 1. 新颖性评估
- "Predictor shift"（K_eff 在 K≥5 成为主导预测器）是否是 genuinely novel finding？
- 与现有 ensemble adversarial robustness 文献的区分度（Tramer 2018, Kariyappa 2019, Pang 2019）
- "Diversity hurts under adversarial manipulation" 这一 direction 在 LLM judge 领域是否已被 Almasoud et al. (2026) 覆盖？
- 论文 3 个 contribution 的增量新颖性是否足以支撑 EMNLP long paper？

### 2. Related Work 覆盖
- 是否有重要相关工作被遗漏？特别关注：
  - 2025-2026 年的 LLM judge adversarial robustness 工作
  - Ensemble diversity 在 NLP 中的应用
  - Multi-agent evaluation 安全性
  - Information-theoretic evaluation 相关工作
- Kuai et al. (2026) DBEI 与 K_eff 的对比是否充分？
- 对 Condorcet Jury Theorem 的定位是否准确？

### 3. Claim 校准（是否 overclaim）
- Title 中 "Shifting Bottleneck" 是否准确反映实际发现？
- Abstract 中的 claim 与正文证据的对应关系
- "uniformly positively associated" 在不同推断方法下是否成立？
- "predictor shift" 的确切含义和边界条件是否清晰？
- 因果 vs 描述性语言的使用是否恰当？

### 4. 论文完整性
- 仅用 MMLU + ARC（multiple-choice），是否足以支撑结论的泛化性？
- 攻击模板每种仅 1-2 variants，结论是否与特定 wording 绑定？
- 是否需要 human evaluation 或与 human annotation 的对比？
- Limitations section 覆盖面是否足够？

### 5. 写作质量与格式
- 术语一致性（检查是否有 "regime transition" vs "predictor shift" 等不一致）
- Abstract 字数是否 ≤200 words（EMNLP 要求）
- 正文是否在 8 页限制内
- Limitations section 位置是否正确（正文内，non appendix）
- 匿名规则是否遵守（无作者身份泄露）
- 图表质量和清晰度
- 论文叙事结构是否流畅

### 6. 综合影响力
- 这篇论文对 LLM evaluation 社区的实际价值？
- Practitioners 能从中获得什么 actionable insights？
- 负面/混合结果的呈现是否有效转化为建设性贡献？

请按 Summary / Strengths / Weaknesses / Questions / Missing References 结构输出审稿意见。Weaknesses 部分需区分 Must-Fix 和 Should-Fix。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-24T10:35:39.953945+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-24T10:35:40.004802+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-24T10:35:46.443012+00:00_

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
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 357 · 2026-05-24T10:35:48.745631+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/submitted.pdf",
  "project": "cert_manip_resist_eval",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/submitted.pdf",
    "project": "cert_manip_resist_eval",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 358 · 2026-05-24T10:35:52.430615+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, I found information about ACL Rolling Review 2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Guidelines

Reviewers are asked to read the paper and get a first impression, search for related work, and if they feel qualified to review only some aspects of the paper, they should state in the review which major parts were not checked, such as proofs, so the Area Chair knows what aspects were not reviewed.

Reviewers are provided with a checklist to flag problems that 
…[truncated 819 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5987
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-24T10:35:53.784815+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 402.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 556.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 549.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 377.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1
…[truncated 482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5039
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-24T10:36:00.934612+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all dimensions, scoring scales, and descriptions. Include every field name, its scale (e.g., 1-5), and the meaning of each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all dimensions, scoring scales, and descriptions. Include every field name, its scale (e.g., 1-5), and the meaning of each score level."
  }
}
```

</details>

---


### Tool call

_source line 361 · 2026-05-24T10:36:01.525851+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-24T10:36:02.762862+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 363 · 2026-05-24T10:36:03.115186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-24T10:36:03.521247+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 365 · 2026-05-24T10:36:04.580829+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 366 · 2026-05-24T10:36:04.581862+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3056
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-24T10:36:05.898233+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3135
}
```

</details>

---


### Tool result

_source line 368 · 2026-05-24T10:36:07.613666+00:00_

# ACL Rolling Review Form - Complete Structure

## Core Review Dimensions

**Paper Summary**
Reviewer describes paper topic and highlights potential misunderstandings.

**Summary of Strengths**
Identify reasons for publication at selective *ACL venues (methodology, results, clarity, etc.).

**Summary of Weaknesses**
List numbered concerns about correctness, impact, clarity, or other publication barriers.

**Comments/Suggestions/Typos**
Additional improvement suggestions beyond addressing weaknesses.

## Scoring Dimensions

**Reviewer Confidence (1-5 scale)**
- 5: Positive evaluation; careful reading with familiarity of related work
- 4: Quite sure; important points checked
- 3: Pretty sure; general area knowledge but incomplete detail verification
- 2: Defensible evaluation; likely missed details or novelty assessment
- 1: Outside expertise area or paper difficult to understand

**Soundness (1-5 scale)**
- 5: Excellent; most thorough for its type
- 4: Strong; sufficient support for claims
- 3: Acceptable; main claims supported with minor gaps
- 2: Poor; insufficient support for major claims
- 1: Major issues; insufficient for publication

**Excitement (1-5 scale)**
- 5: Highly exciting; recommend to others
- 4: Exciting; mention to colleagues
- 3: Interesting; potential mention
- 2: Potentially interesting; limited personal resonance
- 1: Not exciting; limited community relevance

**Overall Assessment (1-5 scale)**
- 5: Award consideration (top 2.5%)
- 4: Conference acceptance
- 3: Findings track
- 2: Resubmit next cycle
- 1: Do not resubmit

## Additional Evaluation Areas

- Limitations and societal impact discussion
- Ethical concerns review
- Ethics review necessity assessment
- Reproducibility (1-5 scale)
- Dataset value (1-5 scale)
- Software value (1-5 scale)
- Author identity disclosure (1-5 scale)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6679
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-24T10:36:07.614863+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4093
}
```

</details>

---


### Tool result

_source line 370 · 2026-05-24T10:36:07.716041+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4600
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-24T10:36:07.716771+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3135
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-24T10:36:14.677822+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-24T10:36:15.634811+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-24T10:36:15.635288+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-24T10:36:16.140596+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-24T10:36:16.141036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 377 · 2026-05-24T10:36:16.594032+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 378 · 2026-05-24T10:36:17.046705+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 379 · 2026-05-24T10:36:17.047131+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 380 · 2026-05-24T10:36:17.552143+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-24T10:36:17.954755+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-24T10:36:27.752532+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/submitted.pdf",
  "project": "cert_manip_resist_eval",
  "pages": "11-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/submitted.pdf",
    "project": "cert_manip_resist_eval",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-24T10:36:29.412134+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.7}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.4}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 563.3}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 602.4}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 374.1}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p19.png\", \"width\": 1
…[truncated 499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1659
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-24T10:36:34.888373+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 385 · 2026-05-24T10:36:35.392340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 386 · 2026-05-24T10:36:36.302190+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1413
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-24T10:36:36.303913+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 911
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-24T10:36:36.304287+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 389 · 2026-05-24T10:36:36.859282+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 390 · 2026-05-24T10:36:37.265276+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 391 · 2026-05-24T10:36:37.265742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 392 · 2026-05-24T10:36:37.969836+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-24T10:36:38.171975+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-24T10:36:44.627037+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 395 · 2026-05-24T10:36:45.181849+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 396 · 2026-05-24T10:36:46.037722+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-24T10:36:46.040765+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-24T10:36:46.041200+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-24T10:36:46.546195+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-24T10:36:46.546540+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-24T10:36:46.848697+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-24T10:36:46.849294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-24T10:36:47.202919+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-24T10:36:57.590733+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Almasoud 2026 \"adversary resistant\" multi-agent LLM evaluation diversity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Almasoud 2026 \"adversary resistant\" multi-agent LLM evaluation diversity"
  }
}
```

</details>

---


### Tool call

_source line 405 · 2026-05-24T10:36:58.042690+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kuai 2026 DBEI \"Diversity-Weighted Behavioral Entanglement Index\" LLM judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kuai 2026 DBEI \"Diversity-Weighted Behavioral Entanglement Index\" LLM judge"
  }
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-24T10:36:58.546430+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LLM judge\" adversarial robustness ensemble panel 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LLM judge\" adversarial robustness ensemble panel 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-24T10:37:04.016003+00:00_

Web search results for query: "Almasoud 2026 "adversary resistant" multi-agent LLM evaluation diversity"

Links: [{"title":"[2603.06856] Evaluating Multi-Agent LLM Architectures for Rare Disease Diagnosis","url":"https://arxiv.org/abs/2603.06856"},{"title":"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring","url":"https://arxiv.org/html/2505.24239v1"},{"title":"[2505.24239] An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring","url":"https://arxiv.org/abs/2505.24239"},{"title":"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring - ACL Anthology","url":"https://aclanthology.org/2025.ijcnlp-long.90/"},{"title":"A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks","url":"https://arxiv.org/html/2509.14285v4"},{"title":"Evaluating Multi-Agent Defences Against Jailbreaking Attacks on Large Language Models","url":"https://arxiv.org/pdf/2506.23576"},{"title":"CollabEval: Enhancing LLM-as-a-Judge via Multi-Agent Collaboration","url":"https://arxiv.org/pdf/2603.00993"}]

I found several relevant research papers on multi-agent LLM systems with adversarial resistance and evaluation diversity:

**Key Papers Found:**

1. **"Evaluating Multi-Agent LLM Architectures for Rare Disease Diagnosis"** by Ahmed Almasoud evaluates four agent topologies (Control, Hierarchical, Adversarial, and Collaborative) across 302 cases spanning 33 rare disease categories.

2. "An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring" introduces a general and adversary-resistant multi-agent LLM framework based on credibility scoring. The system uses connected agents that exchange answers and may revise them, producing diverse topologies such as trees, rings, and other sparse structures—while avoiding full information saturation that would otherwise aid adversaries.

3. **"CollabEval"** presents a novel multi-agent evaluation framework that addresses limitations in single-LLM evaluations. Research reveals that LLM-based 
…[truncated 389 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6425
}
```

</details>

---


### Tool result

_source line 408 · 2026-05-24T10:37:04.269328+00:00_

Web search results for query: "Kuai 2026 DBEI "Diversity-Weighted Behavioral Entanglement Index" LLM judge"

Links: [{"title":"[2604.07650v1] How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/abs/2604.07650v1"},{"title":"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/html/2604.07650v1"},{"title":"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/pdf/2604.07650"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"},{"title":"LLM as Judge Guide March 2026","url":"https://www.openlayer.com/blog/post/llm-as-judge-evaluation-guide"},{"title":"LLM as a Judge: A 2026 Guide to Automated Model Assessment | Label Your Data","url":"https://labelyourdata.com/articles/llm-as-a-judge"}]

Based on the search results, I found information about your query. Here's what the research shows:

The research introduces a Difficulty-Weighted Behavioral Entanglement Index, which amplifies synchronized failures on easy tasks, along with a Cumulative Information Gain (CIG) metric that captures directional alignment in erroneous responses.

This work is authored by Kuai et al., 2026, and develops a statistical framework for auditing behavioral entanglement among black-box LLMs, with experiments on 18 LLMs from six model families that identify widespread behavioral entanglement and analyze its impact on LLM-as-a-judge evaluation.

The study finds that CIG exhibits a statistically significant association with degradation in judge precision, with Spearman coefficient of 0.64 (p < 0.001) for GPT-4o-mini and 0.71 (p < 0.01) for Llama3-based judges, indicating that stronger dependency correspond
…[truncated 510 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6226
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-24T10:37:04.921808+00:00_

Web search results for query: ""LLM judge" adversarial robustness ensemble panel 2025 2026"

Links: [{"title":"LLM-as-Judge Frameworks","url":"https://www.emergentmind.com/topics/llm-as-judge-frameworks"},{"title":"Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment","url":"https://arxiv.org/pdf/2402.14016"},{"title":"SteadyEval: Robust LLM Exam Graders via Adversarial Training and Distillation","url":"https://www.mdpi.com/2073-431X/15/1/55"},{"title":"LLM-as-a-Judge Evaluation","url":"https://www.emergentmind.com/topics/llm-as-a-judge-evaluations"},{"title":"Benchmarking adversarial robustness to bias elicitation in large language models: scalable automated assessment with LLM-as-a-judge | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10994-025-06862-6"},{"title":"LLM-as-Judge Evaluation","url":"https://www.emergentmind.com/topics/llm-as-a-judge-evaluation"},{"title":"When AIs Judge AIs: The Rise of Agent-as-a-Judge Evaluation for LLMs","url":"https://arxiv.org/html/2508.02994v1"}]

Based on the web search results, here's what I found regarding LLM judge adversarial robustness and ensemble approaches in 2025-2026:

## Adversarial Robustness Vulnerabilities

LLM judge systems remain vulnerable to adversarial prompt injections, suffixes, and optimization-based attacks. LLM-based judges can be easily manipulated by adversarial prompt modifications such as Combined Attack or optimization-based attacks such as PAIR, which achieves high attack success rates.

## Ensemble and Panel Approaches

Ensemble aggregation across model families is recommended as part of rigorous prompt engineering, alongside order randomization and explicit rubric specification. Multi-agent ensemble judgment approaches benefit from model diversity, with some using explicit debates and rebuttals while others use parallel assessments and aggregation.

However, ensemble judges could be vulnerable if all agent
…[truncated 701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6375
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-24T10:37:14.274477+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Almasoud 2025 \"credibility scoring\" adversary-resistant multi-agent LLM evaluation diversity vulnerability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Almasoud 2025 \"credibility scoring\" adversary-resistant multi-agent LLM evaluation diversity vulnerability"
  }
}
```

</details>

---


### Tool call

_source line 411 · 2026-05-24T10:37:15.328446+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Chenchens Kuai 2026 \"How independent are large language models\" behavioral entanglement verifier ensembles"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Chenchens Kuai 2026 \"How independent are large language models\" behavioral entanglement verifier ensembles"
  }
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-24T10:37:17.235695+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-24T10:37:17.336380+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb,amsthm}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{definition}{Definition}
17	\newtheorem{proposition}{Proposition}
18	
19	\title{The Shifting Bottleneck: Panel-Size-Dependent Predictors\\of Adversarial Vulnerability in LLM Judge Panels}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	Multi-judge LLM evaluation panels are assumed to benefit from diversity, yet diversity's role under adversarial manipulation is poorly understood. We decompose panel attack success into individual judge weakness ($\eta_{\max}$) and structural diversity ($K_{\mathrm{eff}}$) across 15 models, six attack types, two benchmarks, and panel sizes $K \in \{3, 5, 7\}$ (up to 6,435 panels). Consistent with adversarial ensemble theory but newly characterized in the LLM judge setting, $K_{\mathrm{eff}}$ is uniformly positively associated with vulnerability across all 12 conditions, though the diversity--capability confound ($r{=}0.70$--$0.81$) limits causal interpretation. The predictors' relative importance shifts with panel size: at $K{=}3$, both contribute; at $K{\geq}5$, $K_{\mathrm{eff}}$ becomes the dominant predictor while $\eta_{\max}$ sharply attenuates. Cinelli--Hazlett sensitivity analysis reveals that $K_{\mathrm{eff}}$'s robustness value does not exceed the known confound in 69\% of conditions (25/36), but fractional logit with clustered standard errors confirms the positive association in most conditions ($K{=}3$: 9/12; $K{=}5$: 11/12; $K{=}7$: 12/12). Aggregation rules influence predictability ($R^2$: threshold 0.83, Bayesian 0.09). The defense strategy must match the panel size: small panels requi
…[truncated 3017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 414 · 2026-05-24T10:37:19.995895+00:00_

Web search results for query: "Chenchens Kuai 2026 "How independent are large language models" behavioral entanglement verifier ensembles"

Links: [{"title":"[2604.07650] How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/abs/2604.07650"},{"title":"[2604.07650v1] How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/abs/2604.07650v1"},{"title":"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/html/2604.07650"},{"title":"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles","url":"https://arxiv.org/pdf/2604.07650"},{"title":"(PDF) Emergent Semantic Entanglement in Large Language Models: Non-Sequential Contextual Weaving through Stochastic Syntagmatic Bridges","url":"https://www.researchgate.net/publication/393771242_Emergent_Semantic_Entanglement_in_Large_Language_Models_Non-Sequential_Contextual_Weaving_through_Stochastic_Syntagmatic_Bridges"}]

I found the paper you're looking for! "How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles" by Chenchen Kuai and colleagues was published on arXiv in April 2026.

Here's a summary of the key findings:

**Research Question:** The paper addresses whether seemingly diverse models are truly independent, and how shared pretraining data, distillation, and alignment pipelines can induce hidden behavioral dependencies.

**Main Contribution:** The authors develop a statistical framework for auditing behavioral entanglement among black-box LLMs using a multiresolution hierarchy with two information-theoretic metrics: a Difficulty-
…[truncated 742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4667
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-24T10:37:20.297008+00:00_

Web search results for query: "Almasoud 2025 "credibility scoring" adversary-resistant multi-agent LLM evaluation diversity vulnerability"

Links: [{"title":"[2505.24239] An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring","url":"https://arxiv.org/abs/2505.24239"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=4675&show=50"},{"title":"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring | Request PDF","url":"https://www.researchgate.net/publication/402602390_An_Adversary-Resistant_Multi-Agent_LLM_System_via_Credibility_Scoring"},{"title":"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring - ACL Anthology","url":"https://aclanthology.org/2025.ijcnlp-long.90/"},{"title":"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring","url":"https://arxiv.org/html/2505.24239v1"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=19775&show=50"},{"title":"Red-Teaming LLM Multi-Agent Systems via Communication Attacks","url":"https://arxiv.org/pdf/2502.14847"},{"title":"TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems","url":"https://arxiv.org/pdf/2511.05269"}]

I found the research paper you're looking for. Here are the key details:

The paper "An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring" addresses the vulnerability of multi-agent LLM systems to adversarial and low-performing agents.

**Key Approach:**
The system associates a credibility score that is used when aggregating team outputs, with credibility scores learned gradually based on the past contributions of each agent in query answering.

**Authors and Publication:**
The paper is authored by Sana Ebrahimi, Mohsen Dehghankar, and Abolfazl Asudeh, published in the Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguis
…[truncated 590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6022
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-24T10:37:30.986215+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TAMAS benchmarking adversarial risks multi-agent LLM systems 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TAMAS benchmarking adversarial risks multi-agent LLM systems 2025"
  }
}
```

</details>

---


### Tool call

_source line 417 · 2026-05-24T10:37:31.939843+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CollabEval multi-agent collaboration LLM judge evaluation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CollabEval multi-agent collaboration LLM judge evaluation 2026"
  }
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-24T10:37:32.291887+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"information-theoretic\" \"LLM evaluation\" diversity independence adversarial 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"information-theoretic\" \"LLM evaluation\" diversity independence adversarial 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-24T10:37:35.955518+00:00_

Web search results for query: "TAMAS benchmarking adversarial risks multi-agent LLM systems 2025"

Links: [{"title":"TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems | OpenReview","url":"https://openreview.net/forum?id=80oiymEbaO"},{"title":"[PDF] TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TAMAS:-Benchmarking-Adversarial-Risks-in-LLM-Kavathekar-Jain/6aba9c3fc42286af5e8d42712c07a1033a763cc2"},{"title":"Benchmarking Adversarial Risks in Multi-Agent LLM Systems","url":"https://openreview.net/pdf/2aa259f9b8c9ba825cef9cb90e54b40eaed01030.pdf"},{"title":"TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems","url":"https://arxiv.org/pdf/2511.05269"},{"title":"TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems","url":"https://arxiv.org/html/2511.05269v1"},{"title":"[2511.05269] TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems","url":"https://arxiv.org/abs/2511.05269"},{"title":"Benchmarking Adversarial Risks in Multi-Agent LLM Systems","url":"https://www.researchgate.net/publication/397441863_TAMAS_Benchmarking_Adversarial_Risks_in_Multi-Agent_LLM_Systems"}]

Based on the search results, here's what I found about TAMAS:

## Overview

TAMAS (Threats and Attacks in Multi-Agent Systems) is a benchmark designed to evaluate the robustness and safety of multi-agent LLM systems. It is the first benchmark designed to evaluate the safety of multi-agent LLM based systems, unlike prior benchmarks that focus on isolated single-agent threats, TAMAS systematically studies emergent vulnerabilities arising from inter-agent dynamics.

## Benchmark Composition

TAMAS includes five distinct scenarios comprising 300 adversarial instances across six attack types and 211 tools, along with 100 harmless tasks. TAMAS spans five high-impact domains (education, legal, finance, healthcare, and news), and evaluates six attack types including prompt-level, envi
…[truncated 691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4969
}
```

</details>

---


### Tool result

_source line 420 · 2026-05-24T10:37:37.611214+00:00_

Web search results for query: "CollabEval multi-agent collaboration LLM judge evaluation 2026"

Links: [{"title":"CollabEval: Enhancing LLM-as-a-Judge via Multi-Agent Collaboration","url":"https://arxiv.org/pdf/2603.00993"},{"title":"[2603.00993] CollabEval: Enhancing LLM-as-a-Judge via Multi-Agent Collaboration","url":"https://arxiv.org/abs/2603.00993"},{"title":"Enhancing LLM-as-a-Judge via Multi-Agent Collaboration","url":"https://multiagents.org/2025_posters/poster_agentseval_enhancing_llm_as_a_judge_via_multi_agent_collaboration.pdf"},{"title":"CollabEval: Enhancing LLM-as-a-Judge via Multi-Agent Collaboration","url":"https://arxiv.org/html/2603.00993v1"},{"title":"CollabEval: Enhancing LLM-as-a-Judge via Multi-Agent Collaboration","url":"https://www.researchgate.net/publication/401469677_CollabEval_Enhancing_LLM-as-a-Judge_via_Multi-Agent_Collaboration"},{"title":"Enhancing LLM-as-a-judge via multi-agent collaboration - Amazon Science","url":"https://www.amazon.science/publications/enhancing-llm-as-a-judge-via-multi-agent-collaboration"},{"title":"Haibo Ding","url":"https://www.catalyzex.com/author/Haibo%20Ding"}]

Based on the search results, here's what I found about CollabEval:

## Overview

CollabEval addresses limitations in current LLM-as-a-Judge approaches, which face significant challenges including inconsistent judgments and inherent biases from pre-training data.

## Framework Design

CollabEval is a novel multi-agent evaluation framework that implements a three-phase Collaborative Evaluation process: initial evaluation, multi-round discussion, and final judgment. 

More specifically, the three-phase design includes: (1) initial evaluation, where different agents independently assess the content; (2) multi-round collaborative discussion, where agents share and refine their evaluations through structured dialogue, including confidence scores, agreements, disagreements, and reasoning; and (3) final judgment, where ultimate evaluation decisions are made
…[truncated 641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5671
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-24T10:37:39.270028+00:00_

Web search results for query: ""information-theoretic" "LLM evaluation" diversity independence adversarial 2025 2026"

Links: [{"title":"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/pdf/2508.05469"},{"title":"LLM Evaluation Frameworks 2025 vs 2026: What Matters ...","url":"https://www.mlaidigital.com/blogs/llm-evaluation-frameworks-2025-vs-2026-what-matters-now-2026"},{"title":"Position: LLM Serving Needs Mathematical Optimization and Algorithmic Foundations, Not Just Heuristics","url":"https://arxiv.org/html/2605.01280v1"},{"title":"Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment","url":"https://arxiv.org/pdf/2402.14016"},{"title":"enhancing llm reasoning with adversarial reinforce","url":"https://arxiv.org/pdf/2512.16917"},{"title":"Machine Learning Jul 2025","url":"https://arxiv.org/list/cs.LG/2025-07?skip=450&show=2000"}]

I found several relevant results on information-theoretic approaches to LLM evaluation. Here's what the web search revealed:

## Key Findings

**Information-Theoretic Frameworks for LLM Evaluation:**

Recent advancements have introduced information-theoretic frameworks for peer prediction mechanisms and LLM-specific adaptations such as ElicitationGPT, GPPM, and GEM for model benchmarking.

**Addressing Biases and Adversarial Robustness:**

LLM-based evaluations can carry biases, especially when evaluators share architecture or training data with evaluated models. Research has produced finite-sample robustness bounds for information-theoretic mechanisms under mode-collapse attacks, showing that bounded measures such as TVD retain polynomial guarantees whereas unbounded ones such as KL can degrade exponentially.

**Recent Trends in LLM Evaluation (2025-2026):**

Evaluation has shifted from mere measurement to a system-oriented approach. Additionally, the system can be intentionally "broken" through the use of adversarial prompts to find an 
…[truncated 378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6978
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-24T10:42:35.278091+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见：The Shifting Bottleneck: Panel-Size-Dependent Predictors of Adversarial Vulnerability in LLM Judge Panels\n\n**审查侧重**：新颖性、完整性与写作质量\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 — Findings（可被 Findings 接收）\n\n**一句话总结**：这是一篇在 LLM judge panel 对抗脆弱性领域做出了系统性实证分析的论文，统计方法扎实且对 confound 的透明度值得肯定，但 diversity-capability confound (r=0.70–0.81) 从根本上削弱了核心发现的因果解释力，加之 benchmark scope 过窄（仅 multiple-choice），不足以支撑 EMNLP 主会议 long paper 的新颖性和影响力门槛。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3/5 | 主要 claim 有实验支撑，统计分析全面（OLS + clustered SE + bootstrap + fractional logit + dominance analysis + Cinelli-Hazlett），但 Cinelli-Hazlett 揭示 69% 条件下 K_eff 的 robustness value 不超过已知 confound (Section 6 & Appendix I)，核心 \"predictor shift\" 的因果解释受限 |\n| **Excitement** | 3/5 | 研究问题时机恰当（LLM judge panel 安全性），分析方法论有参考价值，但核心发现（diversity 与 vulnerability 正相关）在承认 confound 后变得不 surprising；实际可操作建议（小 panel 筛个体、大 panel 管组成）相对直觉 |\n| **Reproducibility** | 4/5 | 固定 seed(42)，方法论详细，承诺 acceptance 后释放代码和数据，15 个模型 + 6 种攻击的实验矩阵清晰 |\n| **Reviewer Confidence** | 4/5 | 熟悉 ensemble adversarial robustness 和 LLM evaluation 文献，仔细阅读了正文和所有 appendix |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Diversity-capability confound 根本性地削弱了核心贡献\n\n- **具体位置**：Abstract（\"uniformly positively associated\"）、Section 5.2（predictor shift）、Section 6（Analysis）、Section C.2（r=0.70–0.81）、Appendix I（Cinelli-Hazlett）\n- **问题**：论文的核心发现是 K_eff 与 ASR 正相关且在 K≥5 成为主导预测器（\"predictor shift\"）。然而：\n  1. K_eff 与 η_max 的 Pearson 相关系数高达 r=0.70–0.81（Section C.2），VIF ≈ 2.0–2.9\n  2. Cinelli-Hazlett sensitivity analysis 显示在 69% 的条件 (25/36) 中，K_eff 的 robustness value **不超过** 已知 confound（Appendix I, Table 10）\n  3. Capability-matched subsampling（Pool A, r=0.50）只是\"reduces but does not eliminate\"confound（Limitations, page 9）\n  \n  这意味着我们根本无法区分两个假设：(a) diversity 本身增加 vulnerability（论文的核心 claim），(b) 更 diverse 的 panel 倾向于包含更弱的 model（更平凡的解释）。\"Predictor shift\" 可能只是反映了大 panel 中单个弱 model 的投票权被稀释（η_max 效应减弱），而 K_eff 作为组成特征的 proxy 更好地捕获了整体能力分布。\n  \n  论文对此确实透明，但透明性不等于解决。当 69% 条件下因果推断失败时，将论文 framing 为 \"shifting bottleneck\" 且以此为 title 构成了 overclaim。\n\n- **为什么影响接收**：如果核心 finding 不能可靠地与 confound 分离，paper 的理论贡献（predictor shift 作为 novel finding）降级为对 confound 的一次详尽描述。\n- **建议修改方向**：\n  1. 重新 framing：明确论文的贡献是\"characterizing the confound structure\"而非\"identifying a novel predictor shift\"\n  2. 或者：提供更强的因果识别策略（如 capability-controlled panel construction 或 instrumental variable approach）\n  3. Title 应反映 observational/descriptive 本质，避免暗示因果关系\n\n---\n\n**N2** [critical] Benchmark scope 过窄，无法支撑论文标题中暗示的泛化性\n\n- **具体位置**：Section 4.2、Title (\"LLM Judge Panels\")、Limitations (page 9)\n- **问题**：论文仅使用 MMLU 和 ARC-Challenge，两者都是 multiple-choice 格式。然而 LLM-as-a-judge 的主要应用场景是 **open-ended generation evaluation**（文本质量、对话、摘要等），where：\n  1. 评分空间不是 binary（选对/选错），而是连续或多维的\n  2. 攻击面完全不同——manipulation 是嵌入到 generated text 中而非 candidate answer\n  3. Panel 聚合方式不同——不是 majority vote 而是 score averaging 或 ranking\n  4. Judge 之间的相关性结构可能根本不同\n\n  论文标题 \"LLM Judge Panels\" 暗示了对 LLM 评审范式的普遍适用性，但实证基础仅覆盖了该范式中最简单的一种形态。\n\n- **为什么影响接收**：在没有 open-ended evaluation 实验的情况下，论文的 generalizability claim 不成立。EMNLP long paper 需要更充分的实证覆盖来支撑标题级别的 claim。\n- **建议修改方向**：\n  1. 增加至少一个 open-ended evaluation benchmark（如 MT-Bench、AlpacaEval、Chatbot Arena）\n  2. 或者显著缩小 title/claim scope 至 \"multiple-choice LLM evaluation panels\"\n  3. 在 related work 中明确讨论 multiple-choice vs open-ended 的攻击面差异\n\n---\n\n**N3** [critical] 攻击模板数量过少，结论可能与特定 wording 绑定\n\n- **具体位置**：Section 4.2、Table 16（Appendix R）、Appendix R.1\n- **问题**：每种攻击类型仅使用 1-2 个 template variant（Table 16: prompt injection 2 variants, sycophancy 2, score manipulation 2, verbosity bias 1, position bias 0 (template-free), authority bias 2）。这意味着：\n  1. 观测到的 K_eff 效应可能 confounded with specific template wording 而非攻击类型本身\n  2. 不同的 prompt phrasing 可能触发完全不同的 judge 行为模式\n  3. 455 panels × 6 attack types 的组合看似大，但 within each attack type 的攻击 instantiation 极度 homogeneous\n\n- **为什么影响接收**：如果 K_eff 的预测效果在不同 attack phrasing 下不 robust，则 \"predictor shift\" 可能只是对特定 template 集的 overfitting。\n- **建议修改方向**：\n  1. 每种攻击类型至少增加到 5+ variants，验证结论的 template-invariance\n  2. 或者：加入 template ablation analysis，报告 across-template variance\n  3. 最低限度：在 Limitations 中将此升级为主要局限，而非一句带过\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 标题 \"Shifting Bottleneck\" 暗示了比实际证据更强的结论\n\n- **具体位置**：Title、Abstract、Section 5.2\n- **问题**：\"Shifting Bottleneck\" 暗示一个清晰、戏剧性的转变点。但论文自身承认 K*（转变阈值）\"is not precisely identified\"（Limitations, page 9），3 < K* < 5 是一个宽范围。Figure 3 显示的是渐进趋势而非 sharp shift。加之 N1 中的 confound 问题，这个 framing 过于 assertive。\n- **建议**：考虑更 hedged 的标题，如 \"Panel-Size-Dependent Predictors of...\" 或 \"How Panel Size Modulates...\"\n\n**W2** [warning] 聚合规则分析（Section 4.4）表面化，最有趣的发现被忽视\n\n- **具体位置**：Section 4.4、Table 4（page 8）、Appendix C.3-C.5\n- **问题**：论文报告 threshold voting R²=0.83 而 Bayesian calibration R²=0.09，这是一个 **巨大的** 差异（≈10x），但正文仅用一句话带过（\"Aggregation rules influence predictability\"）。这可能是论文中最有 actionable insight 的发现——Bayesian calibration 几乎完全消除了 K_eff 的预测力——但没有被深入分析。为什么 Bayesian calibration 如此有效？它是否在隐性地做了 capability-matching？这些问题值得 1-2 段的深入讨论。\n- **建议**：在 Analysis section 增加对 aggregation rule × predictability 交互的分析段落\n\n**W3** [warning] 缺少重要的相关工作讨论\n\n- **具体位置**：Section 2\n- **问题**：以下近期相关工作在 Related Work 中缺失或讨论不足：\n  1. **CollabEval (2026)**：提出 multi-agent collaborative evaluation framework（三阶段：independent eval → multi-round discussion → final judgment），与本文 aggregation rule 分析直接相关\n  2. **Kuai et al. (2026) DBEI 的对比** 被放在 Appendix Q，过于边缘化。DBEI 是 K_eff 的直接竞争指标（同样衡量 judge independence），应在正文 Related Work 或 Method 中做 head-to-head 对比\n  3. 论文未讨论 **multi-LLM uncertainty quantification** 的信息论方法（与 K_eff 的信息论基础直接相关）\n- **建议**：在 Section 2 增加 1-2 段讨论 CollabEval 和 DBEI 的关系，将 Appendix Q 的核心比较结果 promote 到正文\n\n**W4** [warning] 因果语言泄漏\n\n- **具体位置**：多处\n- **问题**：论文整体对因果 vs 关联语言把控较好，但存在局部泄漏：\n  1. Abstract: \"The defense strategy **must match** the panel size\" — 在 confound 未解决的情况下，\"must\" 过于强烈\n  2. Section 1 (Introduction): \"diversity's role\" 暗示因果\n  3. Section 6: \"Predictor Shift Pattern\" 中 \"the adversary must compromise ≥3 judges\" — 这里的 \"must\" 暗示了对攻击者策略的因果理解，但论文是 observational study\n- **建议**：系统性地检查全文，将因果暗示替换为关联性描述\n\n**W5** [warning] 缺少 human evaluation baseline\n\n- **具体位置**：整体实验设计\n- **问题**：论文研究 LLM judge panel 的对抗脆弱性，但没有任何 human judge 的参照。如果 human annotator panel 也展现类似的 \"predictor shift\"（人类 annotator 的多样性也与脆弱性相关），那么这个发现就不是 LLM-specific 的。反之，如果 human panel 不展现此模式，则论文的发现更有意义。\n- **建议**：即使规模有限，添加一个 small-scale human annotation 实验作为参照点\n\n**W6** [warning] Theorem 1 (Weakest-Link Monotonicity) 的贡献增量有限\n\n- **具体位置**：Section 3 (page 4)、Appendix A\n- **问题**：Theorem 1 声称 \"Replacing any panel member with a pointwise more vulnerable judge can only increase ASR(P,σ)\"。这本质上是 monotonicity 的直接推论——把一个更弱的 judge 放进去当然不会让 panel 更强。在 majority voting 下这几乎是 tautological。这个 theorem 作为 \"contribution\" 可能过度包装了一个直觉上显然的结论。\n- **建议**：降低 theorem 的 framing 强度，明确其作为 formalization 而非 insight 的定位\n\n---\n\n## 小问题（不影响接收）\n\n- Section 4.3: ε = 10⁻⁶ 用于 log 变换的零值处理，Appendix L 分析了 sensitivity，但未解释为何不直接使用 Tobit 模型或 zero-inflated regression 来处理 bounded outcome\n- Figure 1 (page 2): 框架图信息密度高但文字过小，打印后可能难以阅读\n- Table 2 (page 6): \"div. sig\" 和 \"η_max sig\" 列的含义需要看 caption 才能理解，建议用更 self-explanatory 的列名\n- Section 4.1: 模型选择偏向 open-weight + API frontier 的二分法，mid-range closed-source 模型（如 Claude 3 Haiku 以外的 Anthropic 模型）缺失\n- Abstract 信息密度极高但可读性尚可，数字（69%, 25/36, 9/12, 11/12, 12/12）偏多，可考虑精简\n- \"Code and Data Availability\" section 放在 Limitations 之后但 References 之前，位置略显非标准\n\n---\n\n## 主要优势\n\n1. **统计分析的全面性和严谨性**：论文使用了 6 种以上的统计方法进行 robustness check（OLS、clustered SE、wild cluster bootstrap、fractional logit、dominance analysis、GAM、Cinelli-Hazlett sensitivity），这在 NLP 实证论文中罕见且值得肯定。\n2. **对 confound 的透明度**：大多数论文会淡化或忽略 confound，本文将 Cinelli-Hazlett 的负面结果（69% 条件下不 robust）直接报告在 abstract 中，学术诚信度高。\n3. **实验规模和系统性**：15 models × 6 attack types × 2 benchmarks × 3 panel sizes × 4 aggregation methods 的全因子设计提供了系统性的证据基础。\n4. **K_eff 指标的形式化**：将 pairwise MI 聚合为 effective independence 的指标（Equation 1）是对现有 ensemble diversity 度量的有益补充。\n5. **Random fault contrast (§5.3)** 和 **attacked K_eff stability (Appendix H)** 提供了有效的 sanity check，证明了结论不是 artifact。\n6. **研究问题的时效性**：随着 LLM-as-a-judge 成为主流评估范式，panel composition 与 adversarial robustness 的关系是一个亟需回答的问题。\n\n---\n\n## 对 Director 指定维度的总结\n\n### 新颖性\n- \"Predictor shift\" 在 LLM judge 领域是新的 **观察**，但鉴于 confound 的严重程度，它可能只是 well-known ensemble size effect 在新领域的 re-manifestation\n- K_eff 指标本身不新（基于 pairwise MI），但将其应用于 LLM judge adversarial robustness 分析是新的应用\n- 3 个 contribution 中 Theorem 1 的增量价值有限，实质 contribution 是 2 个：K_eff 关联发现 + predictor shift 模式\n- 增量新颖性对 Findings 足够，对 Main conference 不够\n\n### 完整性\n- Multiple-choice only benchmarks 是最大缺口\n- Attack template 数量过少（1-2 per type）\n- 缺少 human evaluation baseline\n- 缺少对 aggregation rule 差异（特别是 Bayesian calibration 效果）的深入分析\n\n### 写作质量与格式\n- 格式合规：\\usepackage[review]{acl}、Anonymous 作者、8 页正文限制（Section 7 Conclusion 在 page 8 结束）、Limitations 在正文内 appendix 外\n- Abstract 约 170-180 words，在 200 word 限制内\n- 术语一致性良好（K_eff、η_max、predictor shift 全文统一）\n- 叙事结构流畅，从 framework → theory → experiment → analysis 逻辑清晰\n- 匿名规则遵守良好，未发现身份泄露\n",
  "reviewer_id": "2",
  "project": "cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见：The Shifting Bottleneck: Panel-Size-Dependent Predictors of Adversarial Vulnerability in LLM Judge Panels\n\n**审查侧重**：新颖性、完整性与写作质量\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 — Findings（可被 Findings 接收）\n\n**一句话总结**：这是一篇在 LLM judge panel 对抗脆弱性领域做出了系统性实证分析的论文，统计方法扎实且对 confound 的透明度值得肯定，但 diversity-capability confound (r=0.70–0.81) 从根本上削弱了核心发现的因果解释力，加之 benchmark scope 过窄（仅 multiple-choice），不足以支撑 EMNLP 主会议 long paper 的新颖性和影响力门槛。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3/5 | 主要 claim 有实验支撑，统计分析全面（OLS + clustered SE + bootstrap + fractional logit + dominance analysis + Cinelli-Hazlett），但 Cinelli-Hazlett 揭示 69% 条件下 K_eff 的 robustness value 不超过已知 confound (Section 6 & Appendix I)，核心 \"predictor shift\" 的因果解释受限 |\n| **Excitement** | 3/5 | 研究问题时机恰当（LLM judge panel 安全性），分析方法论有参考价值，但核心发现（diversity 与 vulnerability 正相关）在承认 confound 后变得不 surprising；实际可操作建议（小 panel 筛个体、大 panel 管组成）相对直觉 |\n| **Reproducibility** | 4/5 | 固定 seed(42)，方法论详细，承诺 acceptance 后释放代码和数据，15 个模型 + 6 种攻击的实验矩阵清晰 |\n| **Reviewer Confidence** | 4/5 | 熟悉 ensemble adversarial robustness 和 LLM evaluation 文献，仔细阅读了正文和所有 appendix |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Diversity-capability confound 根本性地削弱了核心贡献\n\n- **具体位置**：Abstract（\"uniformly positively associated\"）、Section 5.2（predictor shift）、Section 6（Analysis）、Section C.2（r=0.70–0.81）、Appendix I（Cinelli-Hazlett）\n- **问题**：论文的核心发现是 K_eff 与 ASR 正相关且在 K≥5 成为主导预测器（\"predictor shift\"）。然而：\n  1. K_eff 与 η_max 的 Pearson 相关系数高达 r=0.70–0.81（Section C.2），VIF ≈ 2.0–2.9\n  2. Cinelli-Hazlett sensitivity analysis 显示在 69% 的条件 (25/36) 中，K_eff 的 robustness value **不超过** 已知 confound（Appendix I, Table 10）\n  3. Capability-matched subsampling（Pool A, r=0.50）只是\"reduces but does not eliminate\"confound（Limitations, page 9）\n  \n  这意味着我们根本无法区分两个假设：(a) diversity 本身增加 vulnerability（论文的核心 claim），(b) 更 diverse 的 panel 倾向于包含更弱的 model（更平凡的解释）。\"Predictor shift\" 可能只是反映了大 panel 中单个弱 model 的投票权被稀释（η_max 效应减弱），而 K_eff 作为组成特征的 proxy 更好地捕获了整体能力分布。\n  \n  论文对此确实透明，但透明性不等于解决。当 69% 条件下因果推断失败时，将论文 framing 为 \"shifting bottleneck\" 且以此为 title 构成了 overclaim。\n\n- **为什么影响接收**：如果核心 finding 不能可靠地与 confound 分离，paper 的理论贡献（predictor shift 作为 novel finding）降级为对 confound 的一次详尽描述。\n- **建议修改方向**：\n  1. 重新 framing：明确论文的贡献是\"characterizing the confound structure\"而非\"identifying a novel predictor shift\"\n  2. 或者：提供更强的因果识别策略（如 capability-controlled panel construction 或 instrumental variable approach）\n  3. Title 应反映 observational/descriptive 本质，避免暗示因果关系\n\n---\n\n**N2** [critical] Benchmark scope 过窄，无法支撑论文标题中暗示的泛化性\n\n- **具体位置**：Section 4.2、Title (\"LLM Judge Panels\")、Limitations (page 9)\n- **问题**：论文仅使用 MMLU 和 ARC-Challenge，两者都是 multiple-choice 格式。然而 LLM-as-a-judge 的主要应用场景是 **open-ended generation evaluation**（文本质量、对话、摘要等），where：\n  1. 评分空间不是 binary（选对/选错），而是连续或多维的\n  2. 攻击面完全不同——manipulation 是嵌入到 generated text 中而非 candidate answer\n  3. Panel 聚合方式不同——不是 majority vote 而是 score averaging 或 ranking\n  4. Judge 之间的相关性结构可能根本不同\n\n  论文标题 \"LLM Judge Panels\" 暗示了对 LLM 评审范式的普遍适用性，但实证基础仅覆盖了该范式中最简单的一种形态。\n\n- **为什么影响接收**：在没有 open-ended evaluation 实验的情况下，论文的 generalizability claim 不成立。EMNLP long paper 需要更充分的实证覆盖来支撑标题级别的 claim。\n- **建议修改方向**：\n  1. 增加至少一个 open-ended evaluation benchmark（如 MT-Bench、AlpacaEval、Chatbot Arena）\n  2. 或者显著缩小 title/claim scope 至 \"multiple-choice LLM evaluation panels\"\n  3. 在 related work 中明确讨论 multiple-choice vs open-ended 的攻击面差异\n\n---\n\n**N3** [critical] 攻击模板数量过少，结论可能与特定 wording 绑定\n\n- **具体位置**：Section 4.2、Table 16（Appendix R）、Appendix R.1\n- **问题**：每种攻击类型仅使用 1-2 个 template variant（Table 16: prompt injection 2 variants, sycophancy 2, score manipulation 2, verbosity bias 1, position bias 0 (template-free), authority bias 2）。这意味着：\n  1. 观测到的 K_eff 效应可能 confounded with specific template wording 而非攻击类型本身\n  2. 不同的 prompt phrasing 可能触发完全不同的 judge 行为模式\n  3. 455 panels × 6 attack types 的组合看似大，但 within each attack type 的攻击 instantiation 极度 homogeneous\n\n- **为什么影响接收**：如果 K_eff 的预测效果在不同 attack phrasing 下不 robust，则 \"predictor shift\" 可能只是对特定 template 集的 overfitting。\n- **建议修改方向**：\n  1. 每种攻击类型至少增加到 5+ variants，验证结论的 template-invariance\n  2. 或者：加入 template ablation analysis，报告 across-template variance\n  3. 最低限度：在 Limitations 中将此升级为主要局限，而非一句带过\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 标题 \"Shifting Bottleneck\" 暗示了比实际证据更强的结论\n\n- **具体位置**：Title、Abstract、Section 5.2\n- **问题**：\"Shifting Bottleneck\" 暗示一个清晰、戏剧性的转变点。但论文自身承认 K*（转变阈值）\"is not precisely identified\"（Limitations, page 9），3 < K* < 5 是一个宽范围。Figure 3 显示的是渐进趋势而非 sharp shift。加之 N1 中的 confound 问题，这个 framing 过于 assertive。\n- **建议**：考虑更 hedged 的标题，如 \"Panel-Size-Dependent Predictors of...\" 或 \"How Panel Size Modulates...\"\n\n**W2** [warning] 聚合规则分析（Section 4.4）表面化，最有趣的发现被忽视\n\n- **具体位置**：Section 4.4、Table 4（page 8）、Appendix C.3-C.5\n- **问题**：论文报告 threshold voting R²=0.83 而 Bayesian calibration R²=0.09，这是一个 **巨大的** 差异（≈10x），但正文仅用一句话带过（\"Aggregation rules influence predictability\"）。这可能是论文中最有 actionable insight 的发现——Bayesian calibration 几乎完全消除了 K_eff 的预测力——但没有被深入分析。为什么 Bayesian calibration 如此有效？它是否在隐性地做了 capability-matching？这些问题值得 1-2 段的深入讨论。\n- **建议**：在 Analysis section 增加对 aggregation rule × predictability 交互的分析段落\n\n**W3** [warning] 缺少重要的相关工作讨论\n\n- **具体位置**：Section 2\n- **问题**：以下近期相关工作在 Related Work 中缺失或讨论不足：\n  1. **CollabEval (2026)**：提出 multi-agent collaborative evaluation framework（三阶段：independent eval → multi-round discussion → final judgment），与本文 aggregation rule 分析直接相关\n  2. **Kuai et al. (2026) DBEI 的对比** 被放在 Appendix Q，过于边缘化。DBEI 是 K_eff 的直接竞争指标（同样衡量 judge independence），应在正文 Related Work 或 Method 中做 head-to-head 对比\n  3. 论文未讨论 **multi-LLM uncertainty quantification** 的信息论方法（与 K_eff 的信息论基础直接相关）\n- **建议**：在 Section 2 增加 1-2 段讨论 CollabEval 和 DBEI 的关系，将 Appendix Q 的核心比较结果 promote 到正文\n\n**W4** [warning] 因果语言泄漏\n\n- **具体位置**：多处\n- **问题**：论文整体对因果 vs 关联语言把控较好，但存在局部泄漏：\n  1. Abstract: \"The defense strategy **must match** the panel size\" — 在 confound 未解决的情况下，\"must\" 过于强烈\n  2. Section 1 (Introduction): \"diversity's role\" 暗示因果\n  3. Section 6: \"Predictor Shift Pattern\" 中 \"the adversary must compromise ≥3 judges\" — 这里的 \"must\" 暗示了对攻击者策略的因果理解，但论文是 observational study\n- **建议**：系统性地检查全文，将因果暗示替换为关联性描述\n\n**W5** [warning] 缺少 human evaluation baseline\n\n- **具体位置**：整体实验设计\n- **问题**：论文研究 LLM judge panel 的对抗脆弱性，但没有任何 human judge 的参照。如果 human annotator panel 也展现类似的 \"predictor shift\"（人类 annotator 的多样性也与脆弱性相关），那么这个发现就不是 LLM-specific 的。反之，如果 human panel 不展现此模式，则论文的发现更有意义。\n- **建议**：即使规模有限，添加一个 small-scale human annotation 实验作为参照点\n\n**W6** [warning] Theorem 1 (Weakest-Link Monotonicity) 的贡献增量有限\n\n- **具体位置**：Section 3 (page 4)、Appendix A\n- **问题**：Theorem 1 声称 \"Replacing any panel member with a pointwise more vulnerable judge can only increase ASR(P,σ)\"。这本质上是 monotonicity 的直接推论——把一个更弱的 judge 放进去当然不会让 panel 更强。在 majority voting 下这几乎是 tautological。这个 theorem 作为 \"contribution\" 可能过度包装了一个直觉上显然的结论。\n- **建议**：降低 theorem 的 framing 强度，明确其作为 formalization 而非 insight 的定位\n\n---\n\n## 小问题（不影响接收）\n\n- Section 4.3: ε = 10⁻⁶ 用于 log 变换的零值处理，Appendix L 分析了 sensitivity，但未解释为何不直接使用 Tobit 模型或 zero-inflated regression 来处理 bounded outcome\n- Figure 1 (page 2): 框架图信息密度高但文字过小，打印后可能难以阅读\n- Table 2 (page 6): \"div. sig\" 和 \"η_max sig\" 列的含义需要看 caption 才能理解，建议用更 self-explanatory 的列名\n- Section 4.1: 模型选择偏向 open-weight + API frontier 的二分法，mid-range closed-source 模型（如 Claude 3 Haiku 以外的 Anthropic 模型）缺失\n- Abstract 信息密度极高但可读性尚可，数字（69%, 25/36, 9/12, 11/12, 12/12）偏多，可考虑精简\n- \"Code and Data Availability\" section 放在 Limitations 之后但 References 之前，位置略显非标准\n\n---\n\n## 主要优势\n\n1. **统计分析的全面性和严谨性**：论文使用了 6 种以上的统计方法进行 robustness check（OLS、clustered SE、wild cluster bootstrap、fractional logit、dominance analysis、GAM、Cinelli-Hazlett sensitivity），这在 NLP 实证论文中罕见且值得肯定。\n2. **对 confound 的透明度**：大多数论文会淡化或忽略 confound，本文将 Cinelli-Hazlett 的负面结果（69% 条件下不 robust）直接报告在 abstract 中，学术诚信度高。\n3. **实验规模和系统性**：15 models × 6 attack types × 2 benchmarks × 3 panel sizes × 4 aggregation methods 的全因子设计提供了系统性的证据基础。\n4. **K_eff 指标的形式化**：将 pairwise MI 聚合为 effective independence 的指标（Equation 1）是对现有 ensemble diversity 度量的有益补充。\n5. **Random fault contrast (§5.3)** 和 **attacked K_eff stability (Appendix H)** 提供了有效的 sanity check，证明了结论不是 artifact。\n6. **研究问题的时效性**：随着 LLM-as-a-judge 成为主流评估范式，panel composition 与 adversarial robustness 的关系是一个亟需回答的问题。\n\n---\n\n## 对 Director 指定维度的总结\n\n### 新颖性\n- \"Predictor shift\" 在 LLM judge 领域是新的 **观察**，但鉴于 confound 的严重程度，它可能只是 well-known ensemble size effect 在新领域的 re-manifestation\n- K_eff 指标本身不新（基于 pairwise MI），但将其应用于 LLM judge adversarial robustness 分析是新的应用\n- 3 个 contribution 中 Theorem 1 的增量价值有限，实质 contribution 是 2 个：K_eff 关联发现 + predictor shift 模式\n- 增量新颖性对 Findings 足够，对 Main conference 不够\n\n### 完整性\n- Multiple-choice only benchmarks 是最大缺口\n- Attack template 数量过少（1-2 per type）\n- 缺少 human evaluation baseline\n- 缺少对 aggregation rule 差异（特别是 Bayesian calibration 效果）的深入分析\n\n### 写作质量与格式\n- 格式合规：\\usepackage[review]{acl}、Anonymous 作者、8 页正文限制（Section 7 Conclusion 在 page 8 结束）、Limitations 在正文内 appendix 外\n- Abstract 约 170-180 words，在 200 word 限制内\n- 术语一致性良好（K_eff、η_max、predictor shift 全文统一）\n- 叙事结构流畅，从 framework → theory → experiment → analysis 逻辑清晰\n- 匿名规则遵守良好，未发现身份泄露\n",
    "reviewer_id": "2",
    "project": "cert_manip_resist_eval"
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-24T10:42:39.092047+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3813
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-24T10:42:46.595944+00:00_

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
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
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

_source line 425 · 2026-05-24T10:42:46.646663+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-24T10:42:53.824143+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_4/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-24T10:42:53.874688+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 428 · 2026-05-24T10:43:04.114887+00:00_

审稿完成。总结：

**Overall: 3.0 (Findings)**。论文在 LLM judge panel 对抗脆弱性方向做了系统性实证工作，统计方法全面且对 confound 的透明度值得肯定。但有三个 critical 问题：

1. **Diversity-capability confound (r=0.70–0.81)** 在 69% 条件下无法与核心 K_eff 效应分离，"predictor shift" 的因果解释不成立
2. **仅用 multiple-choice benchmarks**（MMLU + ARC），无法支撑标题中 "LLM Judge Panels" 的泛化性
3. **每种攻击仅 1-2 template variants**，结论可能与特定 wording 绑定

意见已通过 `review_reviewer_post_to_director` 提交至 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2"
}
```

</details>

---


## Round 12

## Round 12

4 recorded events


### User

_source line 429 · 2026-05-24T10:44:02.701538+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见（侧重方法严谨性与统计推断），Overall 3.5 (Borderline Conference)。

请逐条回应每个 Must-Fix 和 Should-Fix 问题：用 `[AGREE]` 表示同意并说明理由，或 `[REBUT]` 表示反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 的完整审稿意见

### Must-Fix 问题

**N1** [critical] K_eff 公式（Eq. 1）缺乏理论来源和验证
- exp(-2·MI) 的系数 2 缺乏理论动机（非 Gaussian 下无明确信息论解释）
- SDPI bound η_joint ≤ K_eff·η_max 未证明也未引用证明
- Section 4.3 混用 Gaussian copula 闭合形式和 plug-in MI 估计器，但 Gaussian copula 未正式检验
- K_eff 是全部分析的核心变量，理论基础不牢则所有结论受影响
- 建议：明确 K_eff 是新指标还是已有概念；严格证明 SDPI bound；做 Gaussian copula GoF 检验

**N2** [critical] 少 cluster 下 wild bootstrap 不可靠，predictor shift 可能是 artifact
- K=3: 13 clusters, K=5: ≤11, K=7: ≤9，均低于推荐 ≥20
- MacKinnon & Webb (2018) 说 Rademacher 比 mammen 好，但不是说少 cluster 下可靠
- MDE 从 K=3 的 0.144 到 K=5 的 0.048——predictor shift (4→7→8) 可能纯粹是 power 差异
- 建议：做 Monte Carlo size calibration；改用 subcluster jackknife；用 effect size 而非 significance count 跨 K 比较

**N3** [critical] Diversity-capability confound 使因果推断不成立，但 framing 暗示因果
- 25/36 (69%) 条件下 η_max confound 可解释 K_eff 效应
- Abstract/Intro 表述暗示因果（"K_eff is uniformly positively associated"）
- Pool A (126 panels = full pool 4.2%) 是精心挑选的 subsample
- 建议：Abstract 加 confound caveat；"predictor shift" 改为 "association shift"；Conclusion 首段讨论 confound

### Should-Fix 问题

**W1** [warning] log(ASR + ε) 在高零值率下不稳定（ARC K=7 零值率 38-40%），ε=10⁻⁶ 对 OLS 杠杆效应大，K=3 时三个条件出现符号变化。Fractional logit 已有且结果更好（9/12, 11/12, 12/12），应以此为主要规范。

**W2** [warning] 15 模型中 9 个 lightweight（6 个因 AWQ INT4 量化降级），tier 分布严重偏斜。K_eff 的预测力可能主要来自区分"有无量化模型"。API-only 9 模型分析（Appendix F Table 7）显示 predictor shift 不 replicate。

**W3** [warning] "uniformly positive" 表述误导——clustered SE 下 0/12 显著。Point estimate 方向在统计上远弱于 significance。应报告跨方法 effect size 和 CI。

**W4** [warning] Dominance analysis 在高共线性（r=0.70-0.81）下的 co-dominance 可能是 identification failure 而非 genuine co-determination。

**W5** [warning] Mixed effects 应用 crossed random effects 而非三个独立 random intercept models。

**W6** [warning] Cinelli-Hazlett 解读过度乐观——8-9/12 条件下 confound 可解释 K_eff 效应应呈现为负面发现。RV 低至 0.005（K=7 MMLU authority bias）。

### 小问题
- FDR scope 不一致（Section 4.5 per predictor vs Table 4 pooled）
- Position bias ARC ρ=0.08 但仍纳入 "uniformly positive" 统计
- gemini-3.5-flash format error 26.3% 的处理方式未说明
- Theorem 1 stochastic dominance 仅 62%，非全局有效

### 主要优势
1. 研究问题新颖且实用
2. 实验规模完整（exhaustive panel enumeration）
3. Robustness check 广度罕见
4. Limitation 讨论诚实
5. K_eff vs κ-diversity 对比有说服力

### Questions
Q1: SDPI bound 是否有严格证明？
Q2: K=7 bootstrap nominal size 是否校准？
Q3: API-only predictor shift 不 replicate 是否表明 AWQ confound 驱动？
Q4: Gaussian copula 是否做过正式检验？
Q5: Fractional logit (9/12,11/12,12/12) vs bootstrap (4/12,7/12,8/12) 巨大差异的原因？

### Missing References
- Genest & Rémillard (2008) copula GoF testing
- MacKinnon, Nielsen & Webb (2023) cluster-robust inference guide
- Roodman et al. (2019) Rademacher weights size distortion

---

请对以上每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-24T10:46:20.136200+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### R1-N1: K_eff 公式（Eq. 1）缺乏理论来源和验证\n\n**[AGREE]** R1-Issue-N1\n\nR1 的技术批评精准。我在审稿中没有单独列出这一点，但回顾后认为这是实质性问题：\n\n1. **exp(−2·MI) 系数问题**：论文 Section 3 (page 3-4) 和 Equation 1 使用了 K_eff = (1/K) Σ (1+Σ exp(−2·MI(i,j)))。这个变换在 bivariate Gaussian 下等价于 1−ρ²（方差分解），但论文处理的是 ordinal/categorical judge outputs（正确/错误的 binary 判断），远非 Gaussian。论文在 page 4 提到 \"the Gaussian copula assumption\" 和 \"adequately captured by rank correlations\"，但没有做正式的 Goodness-of-Fit 检验。\n\n2. **SDPI bound**：论文 page 4 声称 \"Under the strong data-processing inequality (SDPI), the joint vulnerability satisfies η_joint ≤ η_max · K_eff (= η_max), suggesting that diversity should help, but this bound assumes non-adaptive faults.\" 这个 bound 既没有在正文中证明，也没有引用已有证明。Appendix A 仅包含 Theorem 1 (Weakest-Link Monotonicity) 的证明，而非 SDPI bound。\n\n3. **实际影响**：K_eff 是论文 **全部** 回归分析的核心自变量。如果该指标的理论基础存在问题，那么所有 \"K_eff is significant in X/12 conditions\" 的结论都需要重新审视——不是说结论一定错误，而是 K_eff 可能不是衡量 effective independence 的最佳方式，从而影响对 predictor shift 的解释。\n\n补充：R1 建议的 Genest & Rémillard (2008) copula GoF 检验是标准方法，论文应该做。Appendix Q 与 DBEI (Kuai et al., 2026) 和 κ-diversity 的对比是有价值的，但这些替代指标没有被用于替换 K_eff 做 robustness check（即：如果用 DBEI 代替 K_eff，predictor shift 是否仍然成立？Table 14 显示 κ-diversity 的 shift 模式反而消失了——8→7→6 而非上升——这反而暗示 predictor shift 可能是 K_eff 构造方式的 artifact）。\n\n---\n\n### R1-N2: 少 cluster 下 wild bootstrap 不可靠，predictor shift 可能是 power artifact\n\n**[AGREE]** R1-Issue-N2（部分同意，但认为严重程度略低于 R1 评估）\n\nR1 关于 cluster 数量的技术批评成立：\n\n1. **Cluster 数量问题**：K=3: 13 clusters, K=5: ≤11, K=7: ≤9，全部低于 Cameron et al. (2008) 推荐的 ≥20。论文 page 6 自己引用了这个 threshold 但随后论证低 cluster 数 \"alone do not explain the attenuation pattern\"——这个辩护逻辑不充分，因为 bootstrap 的 size distortion 和 power loss 是两个不同问题。\n\n2. **MDE 与 power artifact**：R1 指出 MDE 从 K=3 的 0.14 降到 K=5 的 0.048（Appendix E, Table 12）。这意味着 K=5 和 K=7 有更强的统计功效来检测较小的效应。所以 \"significance count increases from 4/12 to 7/12 to 8/12\" 的 predictor shift 模式可能部分反映 power 增长而非真实的效应结构变化。\n\n**但我认为严重程度需 nuance**：\n\n- **Fractional logit 不依赖 cluster bootstrap**，其 9/12→11/12→12/12 的模式同样展现 predictor shift，且从方法论上更 clean（Section 5.2, Table 4, page 8）。如果 predictor shift 纯粹是 bootstrap power artifact，fractional logit 不应重复该模式。\n- **Effect size direction** 在所有方法下一致为正（Table 2, page 6），coefficient direction 不受 power 影响。\n- 但 R1 说得对：论文**不应以 significance count 跨 K 的变化作为 predictor shift 的主要证据**，而应以 standardized effect size 的跨 K 变化为主。\n\n---\n\n### R1-N3: Diversity-capability confound 使因果推断不成立\n\n**[AGREE]** R1-Issue-N3\n\n这与我自己的 N1 (Must-Fix) 完全一致。我补充两个 R1 未提及的角度：\n\n1. **Pool A 的代表性问题**：R1 正确指出 Pool A (126 panels) 仅占 full pool 的 4.2%（Section 6, page 8; Appendix K）。我进一步注意到，Figure 5 (page 10) 展示了 Pool A 中 K_eff 与 η_max 的相关性仍为 r=0.50——虽然低于 full pool 的 r=0.70-0.81，但仍然是 medium-to-large effect。这意味着即使在 capability-matched subsample 中，confound 仍未被充分控制。\n\n2. **Framing 问题的具体表现**：论文 Abstract 的 \"uniformly positively associated with vulnerability across all 12 conditions\" 和 Title 的 \"Shifting Bottleneck\" 都在 confound 未解决的前提下过度 assertive。R1 建议将 \"predictor shift\" 改为 \"association shift\" 是恰当的——它准确描述了观察到的模式，同时不暗示因果。\n\n---\n\n## Should-Fix 问题\n\n### R1-W1: log(ASR + ε) 不稳定，应以 fractional logit 为主\n\n**[AGREE]** R1-Issue-W1\n\nR1 的技术分析合理：\n- ARC K=7 零值率 38-40% 意味着大量 panel 在某些攻击下 ASR=0，log(0+10⁻⁶) ≈ −13.8 会产生巨大的 leverage effect\n- K=3 时三个条件出现符号变化（Table 2 未直接可见，但 R1 的描述与 Appendix B 的 coefficient pattern 一致）\n- Fractional logit（Table 4, page 8）天然处理 [0,1] bounded outcome 且不需要 ε hack\n\n论文已经报告了 fractional logit 结果（9/12, 11/12, 12/12），这些结果实际上**比 OLS 更支持论文的 claim**。R1 的建议将 fractional logit 提升为 primary specification 是双赢的：方法论更正确，结果也更强。\n\n---\n\n### R1-W2: 模型 tier 偏斜和 AWQ confound\n\n**[AGREE]** R1-Issue-W2\n\n这是我审稿中遗漏的一个重要角度：\n\n- 15 模型中 9 个 lightweight tier（Table 1, page 5），且 6 个 local 模型全部使用 AWQ INT4 量化，全部落入 lightweight tier\n- **API-only 分析 (Appendix F, Table 7)** 显示：仅使用 9 个 API 模型时，predictor shift 模式弱化——K_eff 仍正向但 \"the single discordance in η_max at K=7 for ARC × score manipulation\" 出现。更关键的是样本从 455 panels → 84 panels，统计功效大幅下降\n- 但 R1 提出了一个 deeper 问题：K_eff 的预测力是否主要来自区分 \"包含 vs 不包含量化模型\"？如果是，K_eff 就不是在测量 independence，而是在做 implicit capability tier classification\n\n**补充**：Appendix D (Panel Selection Strategy, page 12, Figure 7) 展示了 mini(η_max) 策略在 12/12 条件下达到最低 ASR，而 maxK(K_eff) 策略 ASR 最高。但这同样可以被 capability confound 解释——mini(η_max) 选的是最强模型，maxK(K_eff) 选的是最 diverse（也最可能包含弱模型）的组合。\n\n---\n\n### R1-W3: \"uniformly positive\" 表述误导\n\n**[AGREE]** R1-Issue-W3\n\nR1 正确区分了 \"coefficient direction uniformly positive\" 和 \"statistically significant\" 的差异。论文 Abstract 和正文多次使用 \"uniformly positively associated\"，读者的自然理解是 \"在所有条件下统计显著为正\"。但实际上：\n\n- OLS: 10/12 FDR-significant（Table 2, page 6）\n- Clustered SE: 如 R1 所述，0/12 达到传统显著性水平\n- Bootstrap: 4/12 at K=3, 7/12 at K=5, 8/12 at K=7\n\n\"Uniformly positive in direction\" 是准确的描述，但 \"uniformly positively associated\" 在没有 qualifier 的情况下是误导性的。论文应在 abstract 中明确 \"coefficient direction is uniformly positive across all 12 conditions, though statistical significance varies by inference method (FDR-significant: 10/12; clustered SE: limited; bootstrap: 4-8/12)\"。\n\n---\n\n### R1-W4: Dominance analysis 在高共线性下的 co-dominance 可能是 identification failure\n\n**[REBUT]** R1-Issue-W4\n\n这是一个合理的方法论关切，但我认为 R1 高估了其严重程度：\n\n1. **Dominance analysis 的用途在论文中有限**：论文使用 dominance analysis（Budescu, 1993）的目的不是证明 K_eff 的因果效应，而是描述两个 predictor 在不同 K 下的 **相对 R² 贡献** 如何变化（Section 5.2）。即使 co-dominance 是 collinearity 的 artifact，这仍然说明两个 predictor 在 K=3 时解释力相当。\n\n2. **VIF 2.0-2.9 并非极端**：传统经验法则是 VIF>10 为严重共线性。r=0.70-0.81 虽然高，但 dominance analysis 在此范围内仍有一定识别力。\n\n3. **论文没有单独依赖 dominance analysis**：predictor shift 的证据来自多个方法的汇聚（OLS coefficient magnitude, fractional logit significance count, dominance analysis），dominance analysis 只是其中之一。\n\n但 R1 的 suggestion（报告 conditional R² 和 tolerance alongside dominance results）是合理的改进。\n\n---\n\n### R1-W5: Mixed effects 应使用 crossed random effects\n\n**[AGREE]** R1-Issue-W5\n\nR1 的方法论建议正确。论文 Section 4.5 (page 5-6) 和 Table 3 (page 7) 提到对 3 个 judge position 分别拟合 random intercept model，然后取 maximum p-value。这种方法：\n\n1. 忽略了 judge position 之间的 crossed effects（同一 judge 可能出现在不同 position）\n2. Maximum p-value 是过度保守的多重比较修正，不等同于正确的 crossed RE 模型\n3. 一个 proper crossed random effects model（judge × position × benchmark）会更干净地处理 panel composition 的非独立性\n\n但我认为这是 **方法改进建议** 而非 fundamental flaw——现有方法是 conservative（取 max p-value），不太可能产生 false positive。\n\n---\n\n### R1-W6: Cinelli-Hazlett 解读过度乐观\n\n**[AGREE]** R1-Issue-W6\n\n这与我自己的 N1 一致。补充一个 R1 提到但我之前没有注意到的具体数字：\n\n- R1 指出 RV 低至 0.005（K=7 MMLU authority bias）。这意味着一个仅能解释 K_eff 残差 0.5% 和 ASR 残差 0.5% 的未观测 confounder 就足以消除 K_eff 的效应——这是**极度脆弱**的。\n- 论文 Section 6（page 8）和 Appendix I（page 13）呈现 Cinelli-Hazlett 结果时，强调了 \"8/12 conditions where K_eff retains 4/12 significance\" 的正面面，而淡化了 25/36 conditions 下 robustness value 不超过已知 confound 的负面面。\n- 在标准的 sensitivity analysis 实践中，如果 benchmark confounder 就足以解释效应，结论应该是 **\"association is not robust to confounding\"** 而非 \"association persists under some methods\"。\n\nR1 的判断——这应被呈现为负面发现——是正确的。\n\n---\n\n## 对 R1 Questions 的补充意见\n\n**Q3 (API-only predictor shift 不 replicate 是否表明 AWQ confound)**：我认为这是一个需要认真对待的问题。Appendix F Table 7 的结果确实暗示 AWQ 量化模型对 predictor shift 有 outsized influence。但 84 panels (API-only) vs 455 panels (full) 的 power 差异也不容忽视。理想的检验是：固定 panel size，在 API-only 模型中做 exhaustive enumeration，然后看 K_eff 的 significance pattern。\n\n**Q5 (Fractional logit vs bootstrap 差异)**：这个差异的主要原因可能是 fractional logit 使用 robust SE 而非 cluster bootstrap，不受少 cluster 问题影响。但这也意味着 fractional logit 可能**低估**了 panel composition 的非独立性（同一 judge 出现在多个 panel 中）。两种方法的差异本身就说明了推断的不稳定性。\n\n---\n\n## 综合判断\n\nR1 的审稿在统计方法论层面比我的审稿更为深入和尖锐。我同意 R1 的大部分 Must-Fix 和 Should-Fix 评价，特别是 N1 (K_eff 理论基础) 和 N3 (confound) 与我自己的评估一致。\n\nR1 给出 3.5 (Borderline Conference)，我给出 3.0 (Findings)。差异主要在于：\n1. 我对 benchmark scope 的限制（仅 multiple-choice）给予了更高的严重权重\n2. 我认为 attack template 数量 (1-2 per type) 是一个独立的 critical issue，R1 没有强调这一点\n3. R1 对 K_eff 的理论基础问题（N1）的分析比我更技术性和具体\n\n两份审稿的核心共识是：**confound 问题是 fundamental，当前 framing 过度 assertive，论文在 Findings 轨道有价值但主会议接收需要更强的因果识别或更 hedged 的 claim。**\n",
  "reviewer_id": "2",
  "project": "cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### R1-N1: K_eff 公式（Eq. 1）缺乏理论来源和验证\n\n**[AGREE]** R1-Issue-N1\n\nR1 的技术批评精准。我在审稿中没有单独列出这一点，但回顾后认为这是实质性问题：\n\n1. **exp(−2·MI) 系数问题**：论文 Section 3 (page 3-4) 和 Equation 1 使用了 K_eff = (1/K) Σ (1+Σ exp(−2·MI(i,j)))。这个变换在 bivariate Gaussian 下等价于 1−ρ²（方差分解），但论文处理的是 ordinal/categorical judge outputs（正确/错误的 binary 判断），远非 Gaussian。论文在 page 4 提到 \"the Gaussian copula assumption\" 和 \"adequately captured by rank correlations\"，但没有做正式的 Goodness-of-Fit 检验。\n\n2. **SDPI bound**：论文 page 4 声称 \"Under the strong data-processing inequality (SDPI), the joint vulnerability satisfies η_joint ≤ η_max · K_eff (= η_max), suggesting that diversity should help, but this bound assumes non-adaptive faults.\" 这个 bound 既没有在正文中证明，也没有引用已有证明。Appendix A 仅包含 Theorem 1 (Weakest-Link Monotonicity) 的证明，而非 SDPI bound。\n\n3. **实际影响**：K_eff 是论文 **全部** 回归分析的核心自变量。如果该指标的理论基础存在问题，那么所有 \"K_eff is significant in X/12 conditions\" 的结论都需要重新审视——不是说结论一定错误，而是 K_eff 可能不是衡量 effective independence 的最佳方式，从而影响对 predictor shift 的解释。\n\n补充：R1 建议的 Genest & Rémillard (2008) copula GoF 检验是标准方法，论文应该做。Appendix Q 与 DBEI (Kuai et al., 2026) 和 κ-diversity 的对比是有价值的，但这些替代指标没有被用于替换 K_eff 做 robustness check（即：如果用 DBEI 代替 K_eff，predictor shift 是否仍然成立？Table 14 显示 κ-diversity 的 shift 模式反而消失了——8→7→6 而非上升——这反而暗示 predictor shift 可能是 K_eff 构造方式的 artifact）。\n\n---\n\n### R1-N2: 少 cluster 下 wild bootstrap 不可靠，predictor shift 可能是 power artifact\n\n**[AGREE]** R1-Issue-N2（部分同意，但认为严重程度略低于 R1 评估）\n\nR1 关于 cluster 数量的技术批评成立：\n\n1. **Cluster 数量问题**：K=3: 13 clusters, K=5: ≤11, K=7: ≤9，全部低于 Cameron et al. (2008) 推荐的 ≥20。论文 page 6 自己引用了这个 threshold 但随后论证低 cluster 数 \"alone do not explain the attenuation pattern\"——这个辩护逻辑不充分，因为 bootstrap 的 size distortion 和 power loss 是两个不同问题。\n\n2. **MDE 与 power artifact**：R1 指出 MDE 从 K=3 的 0.14 降到 K=5 的 0.048（Appendix E, Table 12）。这意味着 K=5 和 K=7 有更强的统计功效来检测较小的效应。所以 \"significance count increases from 4/12 to 7/12 to 8/12\" 的 predictor shift 模式可能部分反映 power 增长而非真实的效应结构变化。\n\n**但我认为严重程度需 nuance**：\n\n- **Fractional logit 不依赖 cluster bootstrap**，其 9/12→11/12→12/12 的模式同样展现 predictor shift，且从方法论上更 clean（Section 5.2, Table 4, page 8）。如果 predictor shift 纯粹是 bootstrap power artifact，fractional logit 不应重复该模式。\n- **Effect size direction** 在所有方法下一致为正（Table 2, page 6），coefficient direction 不受 power 影响。\n- 但 R1 说得对：论文**不应以 significance count 跨 K 的变化作为 predictor shift 的主要证据**，而应以 standardized effect size 的跨 K 变化为主。\n\n---\n\n### R1-N3: Diversity-capability confound 使因果推断不成立\n\n**[AGREE]** R1-Issue-N3\n\n这与我自己的 N1 (Must-Fix) 完全一致。我补充两个 R1 未提及的角度：\n\n1. **Pool A 的代表性问题**：R1 正确指出 Pool A (126 panels) 仅占 full pool 的 4.2%（Section 6, page 8; Appendix K）。我进一步注意到，Figure 5 (page 10) 展示了 Pool A 中 K_eff 与 η_max 的相关性仍为 r=0.50——虽然低于 full pool 的 r=0.70-0.81，但仍然是 medium-to-large effect。这意味着即使在 capability-matched subsample 中，confound 仍未被充分控制。\n\n2. **Framing 问题的具体表现**：论文 Abstract 的 \"uniformly positively associated with vulnerability across all 12 conditions\" 和 Title 的 \"Shifting Bottleneck\" 都在 confound 未解决的前提下过度 assertive。R1 建议将 \"predictor shift\" 改为 \"association shift\" 是恰当的——它准确描述了观察到的模式，同时不暗示因果。\n\n---\n\n## Should-Fix 问题\n\n### R1-W1: log(ASR + ε) 不稳定，应以 fractional logit 为主\n\n**[AGREE]** R1-Issue-W1\n\nR1 的技术分析合理：\n- ARC K=7 零值率 38-40% 意味着大量 panel 在某些攻击下 ASR=0，log(0+10⁻⁶) ≈ −13.8 会产生巨大的 leverage effect\n- K=3 时三个条件出现符号变化（Table 2 未直接可见，但 R1 的描述与 Appendix B 的 coefficient pattern 一致）\n- Fractional logit（Table 4, page 8）天然处理 [0,1] bounded outcome 且不需要 ε hack\n\n论文已经报告了 fractional logit 结果（9/12, 11/12, 12/12），这些结果实际上**比 OLS 更支持论文的 claim**。R1 的建议将 fractional logit 提升为 primary specification 是双赢的：方法论更正确，结果也更强。\n\n---\n\n### R1-W2: 模型 tier 偏斜和 AWQ confound\n\n**[AGREE]** R1-Issue-W2\n\n这是我审稿中遗漏的一个重要角度：\n\n- 15 模型中 9 个 lightweight tier（Table 1, page 5），且 6 个 local 模型全部使用 AWQ INT4 量化，全部落入 lightweight tier\n- **API-only 分析 (Appendix F, Table 7)** 显示：仅使用 9 个 API 模型时，predictor shift 模式弱化——K_eff 仍正向但 \"the single discordance in η_max at K=7 for ARC × score manipulation\" 出现。更关键的是样本从 455 panels → 84 panels，统计功效大幅下降\n- 但 R1 提出了一个 deeper 问题：K_eff 的预测力是否主要来自区分 \"包含 vs 不包含量化模型\"？如果是，K_eff 就不是在测量 independence，而是在做 implicit capability tier classification\n\n**补充**：Appendix D (Panel Selection Strategy, page 12, Figure 7) 展示了 mini(η_max) 策略在 12/12 条件下达到最低 ASR，而 maxK(K_eff) 策略 ASR 最高。但这同样可以被 capability confound 解释——mini(η_max) 选的是最强模型，maxK(K_eff) 选的是最 diverse（也最可能包含弱模型）的组合。\n\n---\n\n### R1-W3: \"uniformly positive\" 表述误导\n\n**[AGREE]** R1-Issue-W3\n\nR1 正确区分了 \"coefficient direction uniformly positive\" 和 \"statistically significant\" 的差异。论文 Abstract 和正文多次使用 \"uniformly positively associated\"，读者的自然理解是 \"在所有条件下统计显著为正\"。但实际上：\n\n- OLS: 10/12 FDR-significant（Table 2, page 6）\n- Clustered SE: 如 R1 所述，0/12 达到传统显著性水平\n- Bootstrap: 4/12 at K=3, 7/12 at K=5, 8/12 at K=7\n\n\"Uniformly positive in direction\" 是准确的描述，但 \"uniformly positively associated\" 在没有 qualifier 的情况下是误导性的。论文应在 abstract 中明确 \"coefficient direction is uniformly positive across all 12 conditions, though statistical significance varies by inference method (FDR-significant: 10/12; clustered SE: limited; bootstrap: 4-8/12)\"。\n\n---\n\n### R1-W4: Dominance analysis 在高共线性下的 co-dominance 可能是 identification failure\n\n**[REBUT]** R1-Issue-W4\n\n这是一个合理的方法论关切，但我认为 R1 高估了其严重程度：\n\n1. **Dominance analysis 的用途在论文中有限**：论文使用 dominance analysis（Budescu, 1993）的目的不是证明 K_eff 的因果效应，而是描述两个 predictor 在不同 K 下的 **相对 R² 贡献** 如何变化（Section 5.2）。即使 co-dominance 是 collinearity 的 artifact，这仍然说明两个 predictor 在 K=3 时解释力相当。\n\n2. **VIF 2.0-2.9 并非极端**：传统经验法则是 VIF>10 为严重共线性。r=0.70-0.81 虽然高，但 dominance analysis 在此范围内仍有一定识别力。\n\n3. **论文没有单独依赖 dominance analysis**：predictor shift 的证据来自多个方法的汇聚（OLS coefficient magnitude, fractional logit significance count, dominance analysis），dominance analysis 只是其中之一。\n\n但 R1 的 suggestion（报告 conditional R² 和 tolerance alongside dominance results）是合理的改进。\n\n---\n\n### R1-W5: Mixed effects 应使用 crossed random effects\n\n**[AGREE]** R1-Issue-W5\n\nR1 的方法论建议正确。论文 Section 4.5 (page 5-6) 和 Table 3 (page 7) 提到对 3 个 judge position 分别拟合 random intercept model，然后取 maximum p-value。这种方法：\n\n1. 忽略了 judge position 之间的 crossed effects（同一 judge 可能出现在不同 position）\n2. Maximum p-value 是过度保守的多重比较修正，不等同于正确的 crossed RE 模型\n3. 一个 proper crossed random effects model（judge × position × benchmark）会更干净地处理 panel composition 的非独立性\n\n但我认为这是 **方法改进建议** 而非 fundamental flaw——现有方法是 conservative（取 max p-value），不太可能产生 false positive。\n\n---\n\n### R1-W6: Cinelli-Hazlett 解读过度乐观\n\n**[AGREE]** R1-Issue-W6\n\n这与我自己的 N1 一致。补充一个 R1 提到但我之前没有注意到的具体数字：\n\n- R1 指出 RV 低至 0.005（K=7 MMLU authority bias）。这意味着一个仅能解释 K_eff 残差 0.5% 和 ASR 残差 0.5% 的未观测 confounder 就足以消除 K_eff 的效应——这是**极度脆弱**的。\n- 论文 Section 6（page 8）和 Appendix I（page 13）呈现 Cinelli-Hazlett 结果时，强调了 \"8/12 conditions where K_eff retains 4/12 significance\" 的正面面，而淡化了 25/36 conditions 下 robustness value 不超过已知 confound 的负面面。\n- 在标准的 sensitivity analysis 实践中，如果 benchmark confounder 就足以解释效应，结论应该是 **\"association is not robust to confounding\"** 而非 \"association persists under some methods\"。\n\nR1 的判断——这应被呈现为负面发现——是正确的。\n\n---\n\n## 对 R1 Questions 的补充意见\n\n**Q3 (API-only predictor shift 不 replicate 是否表明 AWQ confound)**：我认为这是一个需要认真对待的问题。Appendix F Table 7 的结果确实暗示 AWQ 量化模型对 predictor shift 有 outsized influence。但 84 panels (API-only) vs 455 panels (full) 的 power 差异也不容忽视。理想的检验是：固定 panel size，在 API-only 模型中做 exhaustive enumeration，然后看 K_eff 的 significance pattern。\n\n**Q5 (Fractional logit vs bootstrap 差异)**：这个差异的主要原因可能是 fractional logit 使用 robust SE 而非 cluster bootstrap，不受少 cluster 问题影响。但这也意味着 fractional logit 可能**低估**了 panel composition 的非独立性（同一 judge 出现在多个 panel 中）。两种方法的差异本身就说明了推断的不稳定性。\n\n---\n\n## 综合判断\n\nR1 的审稿在统计方法论层面比我的审稿更为深入和尖锐。我同意 R1 的大部分 Must-Fix 和 Should-Fix 评价，特别是 N1 (K_eff 理论基础) 和 N3 (confound) 与我自己的评估一致。\n\nR1 给出 3.5 (Borderline Conference)，我给出 3.0 (Findings)。差异主要在于：\n1. 我对 benchmark scope 的限制（仅 multiple-choice）给予了更高的严重权重\n2. 我认为 attack template 数量 (1-2 per type) 是一个独立的 critical issue，R1 没有强调这一点\n3. R1 对 K_eff 的理论基础问题（N1）的分析比我更技术性和具体\n\n两份审稿的核心共识是：**confound 问题是 fundamental，当前 framing 过度 assertive，论文在 Findings 轨道有价值但主会议接收需要更强的因果识别或更 hedged 的 claim。**\n",
    "reviewer_id": "2",
    "project": "cert_manip_resist_eval"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-24T10:46:23.953385+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3817
}
```

</details>

---


### Assistant

_source line 432 · 2026-05-24T10:46:35.536438+00:00_

已完成对 Reviewer 1 全部 Must-Fix (N1-N3) 和 Should-Fix (W1-W6) 的逐条回应，并提交给 Director。

核心判断：

- **N1 (K_eff 理论基础)**: [AGREE] — exp(−2·MI) 在非 Gaussian 下缺乏严格基础，SDPI bound 未证明，且 Table 14 显示 κ-diversity 的 shift 模式消失，暗示 predictor shift 可能是 K_eff 构造方式的 artifact
- **N2 (少 cluster bootstrap)**: [AGREE，严重程度略低] — cluster 数量确实不足，但 fractional logit (9/12→11/12→12/12) 不依赖 cluster 且重复了 shift 模式
- **N3 (Confound)**: [AGREE] — 与我的 N1 完全一致
- **W1-W3, W5-W6**: [AGREE]
- **W4 (Dominance analysis)**: [REBUT] — VIF 2-3 非极端，且论文未单独依赖此方法

两份审稿的共识：confound 是根本性问题，当前 framing 过度 assertive，Findings 轨道有价值但主会议需要更强的因果识别。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2"
}
```

</details>

---


## Round 13

## Round 13

96 recorded events


### User

_source line 433 · 2026-05-24T17:52:43.734163+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量 + 格式合规**。

## 投稿信息
- **Venue**: EMNLP 2026 Main（通过 ARR 统一审稿）
- **Deadline**: ARR 提交截止 2026-05-25
- **页数限制**: 正文 8 页，参考文献不限，Limitations 不算页数
- **模板**: ACL 2-column（\usepackage[review]{acl}）
- **匿名**: Double-blind
- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 论文路径
- LaTeX 源码: `projects/cert_manip_resist_eval/docs/paper/main.tex`（子文件: introduction.tex, related_work.tex, threat_model.tex, methodology.tex, results.tex, analysis.tex, conclusion.tex, appendix.tex, appendix_attacks.tex）
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/submitted.pdf`

## 你的审查侧重

### 1. 新颖性与贡献评估
- "predictor shift"（η_max → K_eff dominance as K grows）作为核心贡献是否足够新颖？
- K_eff 指标本身 vs κ-diversity、disagreement rate 等已有指标——增量贡献在哪里？
- 论文声称 predictor shift 是 "previously uncharacterized"——是否有遗漏的相关工作？
- 贡献的 framing 是否 overclaiming？特别是标题 "The Shifting Predictor" 是否夸大？

### 2. 写作质量
- Abstract 是否超过 200 words（EMNLP 2026 硬约束）？
- 因果语言 vs 描述性语言——是否有残留的因果暗示（如 "must match"、"diversity's role"）？
- 术语一致性（predictor shift / regime transition 等）
- 叙事结构：从 Introduction 到 Conclusion 的论证链是否连贯？
- 数字密度——是否过多统计数字堆砌而缺乏直觉解释？

### 3. 相关工作完整性
- 是否遗漏重要相关工作？特别关注：
  - LLM judge 安全/对抗鲁棒性方向
  - ensemble diversity 理论
  - 信息论评估方法
  - CollabEval (Qian et al., 2026) 是否充分讨论？
  - Kuai et al. (2026) DBEI 与 K_eff 的比较是否充分？

### 4. 格式合规
- 正文是否在 8 页以内？
- Limitations section 是否存在且位置正确（正文内）？
- 附录是否包含不应有的 Limitations section？
- 参考文献格式是否正确？
- 图表质量和可读性
- 匿名合规（是否泄露作者身份）

### 5. 论文完整性
- Aggregation rules 分析是否表面化？threshold R²=0.83 vs Bayesian R²=0.09 的 10x 差异是否充分讨论？
- Bayesian non-monotonic behavior (6/12→7/12→0/12) 是否有合理解释？
- 仅 MMLU + ARC (multiple-choice) 的泛化性讨论是否充分？
- 是否缺少 open-ended evaluation 的讨论？

请按 ARR 标准给出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment（含评分和置信度）。Weaknesses 按严重程度（Must-Fix / Should-Fix / Minor）分级。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-24T17:52:51.295848+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-24T17:52:51.348039+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/review_reviewer_2_38d341a1.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-24T17:52:54.522619+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-24T17:52:54.573266+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-24T17:52:57.185819+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-24T17:52:57.287889+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-research.skill.md
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-writing.skill.md
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/cert_manip_resist_eval/distilled-research.skill.md
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/cert_manip_resist_eval/distilled-writing.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-24T17:53:02.184302+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-24T17:53:02.235107+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-24T17:53:06.609700+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 443 · 2026-05-24T17:53:09.469387+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/submitted.pdf",
  "project": "cert_manip_resist_eval",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/submitted.pdf",
    "project": "cert_manip_resist_eval",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-24T17:53:10.073048+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-24T17:53:13.383716+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

For Findings papers, the main criteria are soundness and reproducibility, while conference recommendations may als
…[truncated 1118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6774
}
```

</details>

---


### Tool result

_source line 446 · 2026-05-24T17:53:14.688474+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 420.5}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 551.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 556.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 393.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1
…[truncated 482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5219
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-24T17:53:14.739144+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix_attacks.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/figures/fig_framework.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 4666
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-24T17:53:24.631734+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract ALL review form fields, scoring dimensions, and their scales. Include: Overall Assessment, Confidence, Soundness, Excitement/Novelty, Reproducibility, and any other scored dimensions. For each dimension list the full scale (all options). Also extract any specific instructions for reviewers about what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract ALL review form fields, scoring dimensions, and their scales. Include: Overall Assessment, Confidence, Soundness, Excitement/Novelty, Reproducibility, and any other scored dimensions. For each dimension list the full scale (all options). Also extract any specific instructions for reviewers about what each score means."
  }
}
```

</details>

---


### Tool call

_source line 449 · 2026-05-24T17:53:25.236568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-24T17:53:25.642752+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-24T17:53:26.547955+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1311
}
```

</details>

---


### Tool result

_source line 452 · 2026-05-24T17:53:26.549003+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 453 · 2026-05-24T17:53:26.599578+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-24T17:53:27.050996+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-24T17:53:27.505869+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-24T17:53:27.506292+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-24T17:53:28.010059+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool result

_source line 458 · 2026-05-24T17:53:28.464391+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-24T17:53:30.971787+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- 4: Quite sure with unlikely but conceivable oversights
- 3: Pretty sure, but chance of missing details
- 2: Willing to defend, but likely missed some details
- 1: Outside expertise area or paper very hard to understand

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- 5: "Excellent: This study is one of the most thorough I have seen, given its type."
- 4: Strong study with sufficient support; extra experiments optional
- 3: Acceptable support for main claims; minor details needed
- 2: Poor; main claims lack sufficient support
- 1: Major issues; insufficiently thorough for publication

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
Evaluates subjective appeal, including conceptual breakthroughs, community impact, and personal relevance. Ranges from "Highly Exciting" (5) to "Not Exciting" (1).

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- 5: Consider for Award (top 2.5% papers)
- 4: Conference acceptance
- 3: Accept to Findings track
- 2: Resubmit next cycle (substantial revisions needed)
- 1: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- 5: Results easily reproducible
- 4: Mostly reproducible with possible minor variations
- 3: Reproducible with some difficulty
- 2: Hard to reproduce; limited data availability
- 1: Cannot reproduce results

## 6. **Datasets**
Scale: 1-5
Evaluates value of released datasets from "Enabling" (5) to "No usable datasets submitted" (1).

## 7. **Software**
Scale: 1-5
Assesses released software utility from "Enabling" (5) to "No usable software released" (1).

## 8. **Author Identity Knowledge**
Scale: 1-5
Documents reviewer's knowledge of author identity (non-scoring).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6340
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-24T17:53:38.402116+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 461 · 2026-05-24T17:53:38.906957+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 462 · 2026-05-24T17:53:39.361409+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 463 · 2026-05-24T17:53:39.361881+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 464 · 2026-05-24T17:53:40.320595+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1413
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-24T17:53:40.321791+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-24T17:53:40.322024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 467 · 2026-05-24T17:53:40.823836+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 468 · 2026-05-24T17:53:41.277049+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 469 · 2026-05-24T17:53:41.277687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 470 · 2026-05-24T17:53:41.378376+00:00_

1	% Mirror of abstract in main.tex — do not edit here.
2	
3	Multi-judge LLM evaluation panels are assumed to benefit from diversity, yet diversity's relationship to adversarial vulnerability is poorly understood. We decompose panel attack success into individual judge weakness ($\eta_{\max}$) and structural diversity ($K_{\mathrm{eff}}$) across 15 models, six attack types, two benchmarks, and panel sizes $K \in \{3, 5, 7\}$ (up to 6,435 panels). Consistent with adversarial ensemble theory but newly characterized in the LLM judge setting, $K_{\mathrm{eff}}$'s coefficient direction is positive in all 12 conditions (12/12 under OLS), though significance is method-sensitive (0--12/12 across inference methods) and the diversity--capability confound ($r{=}0.70$--$0.81$) limits causal interpretation. The predictors' relative importance shifts with panel size: at $K{=}3$, both contribute; at $K{\geq}5$, $K_{\mathrm{eff}}$ becomes the dominant predictor while $\eta_{\max}$ sharply attenuates. Cinelli--Hazlett sensitivity analysis reveals that $K_{\mathrm{eff}}$'s robustness value does not exceed the known confound in 69\% of conditions (25/36), but fractional logit with clustered standard errors confirms the positive association in most conditions ($K{=}3$: 9/12; $K{=}5$: 11/12; $K{=}7$: 12/12). Aggregation rules influence predictability ($R^2$: threshold 0.83, Bayesian 0.09). The defense strategy should be informed by panel size: small panels benefit from screening for individual robustness; larger panels benefit from monitoring judge independence.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-24T17:53:41.581544+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 757
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-24T17:54:01.008833+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/submitted.pdf",
  "project": "cert_manip_resist_eval",
  "pages": "11-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/submitted.pdf",
    "project": "cert_manip_resist_eval",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 473 · 2026-05-24T17:54:01.518119+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-24T17:54:01.969926+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool call

_source line 475 · 2026-05-24T17:54:02.474394+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 476 · 2026-05-24T17:54:04.485496+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 415.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.4}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.1}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 483.3}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 402.8}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p19.png\", \"width\": 1
…[truncated 500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3476
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-24T17:54:04.486123+00:00_

1	\section{Related Work}
2	
3	\paragraph{LLM-as-Judge and Multi-Judge Evaluation.}
4	LLM judges gained traction after \citet{zheng2023judging} established them as scalable alternatives to human annotation. \citet{wang2023fair} documented systematic failure modes (position bias, verbosity, sycophancy), motivating multi-judge panels; \citet{raina2024judgerobust} quantified robustness gaps under universal adversarial attacks, \citet{maloyan2025investigating} demonstrated prompt injection vulnerabilities in LLM-as-a-judge systems, and \citet{stureborg2024inconsistent} and \citet{ye2024justice} further catalogued inconsistency and bias in LLM evaluators. Aggregating noisy annotators traces back to \citet{dawid1979maximum}; \citet{verga2024replacing} showed diverse panels can match single large judges, and \citet{panickssery2024llm} identified self-preference bias driving within-family correlations. These frameworks assume benign conditions; we test whether aggregation benefits survive adversarial manipulation. \citet{almasoud2026security} reported that 7-model committees reduce ASR from 50--68\% to 10--19\%, but did not disentangle diversity from individual robustness. \citet{tamas2025benchmarking} benchmark adversarial risks in multi-agent LLM systems but focus on agent coordination rather than judge panel composition. \citet{qian2026collabeval} propose CollabEval, a three-phase collaborative evaluation framework (independent assessment, multi-round discussion, consensus judgment) that outperforms single-judge baselines; their work assumes benign conditions and does not examine adversarial manipulation or the diversity--vulnerability tradeoff we characterize.
5	
6	\paragraph{Condorcet Jury Theorem.}
7	\citet{condorcet1785essai} proved that majority voting accuracy converges to 1 when per-voter accuracy exceeds 0.5; \citet{ladha1992condorcet} extended the theorem to correlated voters, showing that positive correlation weakens the convergence guarantee. CJT explicitly ass
…[truncated 3384 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2011
}
```

</details>

---


### Tool result

_source line 478 · 2026-05-24T17:54:04.536858+00:00_

1	\section{Introduction}
2	
3	\input{figures/fig_framework}
4	
5	Multi-judge panels have emerged as the dominant defense against bias and manipulation in LLM-based evaluation. After \citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work exposed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, drawing inspiration from Byzantine fault tolerance (BFT), where majority voting among independent nodes tolerates faulty responses \citep{lamport1982byzantine,castro1999practical}. A recent systematization of LLM-judge security reports that 7-model committees reduce attack success rates from 50--68\% to 10--19\% \citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation.
6	
7	Yet the evidence for diversity as a causal defense is weaker than it appears. The observed ASR reduction conflates panel diversity (judge independence) with individual robustness (strongest members). No existing work disentangles these across panel sizes. BFT adversaries control faulty nodes internally, whereas evaluation adversaries manipulate inputs externally; the independence-based intuition that joint failure scales with $K_{\mathrm{eff}} \cdot \eta_{\max}$ assumes non-adaptive faults \citep{schneier2000secrets}.
8	
9	In our experiments, we observe a panel-size-dependent predictor shift. The positive direction of $K_{\mathrm{eff}}$'s coefficient across all 12 conditions (direction 12/12 under ordinary least-squares (OLS), though significance is method-sensitive: 0--12/12 across inference methods; generalized additive model (GAM) bootstrap confirms 88.9--100\% positive rate) is directionally consistent with adversarial ensemble theory \citep{goodfellow2015adversarial,papernot2016transferability}, but the $K$-dependent transition in pre
…[truncated 2374 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2566
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-24T17:54:04.538195+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb,amsthm}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage{tikz}
15	\usetikzlibrary{shapes.geometric,arrows.meta,positioning,fit,shadows.blur,calc}
16	
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{definition}{Definition}
19	\newtheorem{proposition}{Proposition}
20	
21	\title{The Shifting Predictor: Panel-Size-Dependent Vulnerability\\Patterns in LLM Judge Panels}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\begin{abstract}
29	Multi-judge LLM evaluation panels are assumed to benefit from diversity, yet diversity's relationship to adversarial vulnerability is poorly understood. We decompose panel attack success into individual judge weakness ($\eta_{\max}$) and structural diversity ($K_{\mathrm{eff}}$) across 15 models, six attack types, two benchmarks, and panel sizes $K \in \{3, 5, 7\}$ (up to 6,435 panels). Consistent with adversarial ensemble theory but newly characterized in the LLM judge setting, $K_{\mathrm{eff}}$'s coefficient direction is positive in all 12 conditions (12/12 under OLS), though significance is method-sensitive (0--12/12 across inference methods) and the diversity--capability confound ($r{=}0.70$--$0.81$) limits causal interpretation. The predictors' relative importance shifts with panel size: at $K{=}3$, both contribute; at $K{\geq}5$, $K_{\mathrm{eff}}$ becomes the dominant predictor while $\eta_{\max}$ sharply attenuates. Cinelli--Hazlett sensitivity analysis reveals that $K_{\mathrm{eff}}$'s robustness value does not exceed the known confound in 69\% of conditions (25/36), but fractional logit with clustered standard errors confirms the positive association in most conditions ($K{=}3$: 9/12; $K{=}5$: 11/12; $K{=}
…[truncated 3315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3020
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-24T17:54:10.459356+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-24T17:54:11.474128+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1014
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-24T17:54:11.476348+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 483 · 2026-05-24T17:54:12.031949+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-24T17:54:12.487737+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-24T17:54:12.992407+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1516
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-24T17:54:13.193526+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 487 · 2026-05-24T17:54:14.149465+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/threat_model.tex"
  }
}
```

</details>

---


### Tool result

_source line 488 · 2026-05-24T17:54:14.554034+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2522
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-24T17:54:14.554560+00:00_

1	\section{Threat Model and Problem Formulation}
2	\label{sec:threat_model}
3	
4	A \emph{panel} $\mathcal{P} = \{J_1, \ldots, J_K\}$ consists of $K$ judges (with $K$ odd) that evaluate a candidate text via majority vote: the text is accepted if at least $t = \lceil K/2 \rceil$ judges approve it. Under an attack $a$, each judge $J_j$ is compromised with marginal failure probability $\eta_j(a) = \Pr(X_j^a = 1)$, where $X_j^a \in \{0,1\}$ denotes the failure indicator. We write $\eta_{\max} = \max_j \eta_j$ for the vulnerability of the weakest judge. The \emph{panel attack success rate} is $\mathrm{ASR}(\mathcal{P}, a) = \Pr\!\bigl(\sum_{j=1}^K X_j^a \geq t\bigr)$.
5	
6	To quantify diversity, we define the \emph{effective independence} $K_{\mathrm{eff}}$ directly from pairwise mutual information among judges:
7	\begin{equation}
8	\label{eq:keff}
9	K_{\mathrm{eff}} = \frac{1}{K}\sum_{i=1}^{K} \Bigl[1 + \sum_{j \neq i} \exp\!\bigl(-2 \cdot \mathrm{MI}(i,j)\bigr)\Bigr].
10	\end{equation}
11	This formulation computes effective independence from pairwise MI estimates without matrix decomposition, and is more stable for small panels ($K{=}3$). It ranges from $K_{\mathrm{eff}} \approx K$ when judges are nearly independent ($\mathrm{MI} \to 0$) to $K_{\mathrm{eff}} \approx 1$ when judges are highly correlated ($\mathrm{MI} \to \infty$). Motivated by information-theoretic redundancy reduction, one can informally expect joint vulnerability to scale as $\eta_{\mathrm{joint}} \sim K_{\mathrm{eff}} \cdot \eta_{\max}$: independent channels multiply failure probabilities, so fewer effective channels (lower $K_{\mathrm{eff}}$) should reduce panel vulnerability. This motivating relationship assumes non-adaptive faults and independent channels; it serves as intuition rather than a formal bound.
12	
13	\begin{definition}[Adaptive Adversary]
14	\label{def:adversary}
15	A \emph{full-knowledge (oracle) adaptive adversary} has complete knowledge of the panel composition $\mathcal{P}$, the pe
…[truncated 2427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-24T17:54:14.557265+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-24T17:54:14.608975+00:00_

1	\section{Experimental Methodology}
2	\label{sec:experiments}
3	
4	\subsection{Models and Panel Construction}
5	
6	We select 15 LLM judges spanning 6 provider families and 3 capability tiers, listed in Table~\ref{tab:models}. Nine models are accessed via the OpenRouter API; six open-weight models are served locally using vLLM~0.21.0 with AWQ INT4 quantization on an NVIDIA RTX~6000 Ada (48\,GB). API models are assigned to \emph{frontier}, \emph{mid-tier}, or \emph{lightweight} tiers following the provider capability classification; all six local models fall into the lightweight tier, as INT4 quantization substantially reduces judge accuracy on the pairwise judgment task (Table~\ref{tab:models}). We study three panel sizes $K \in \{3, 5, 7\}$ (all odd, majority-vote threshold $t = \lceil K/2 \rceil$). Exhaustive enumeration yields $\binom{15}{3} = 455$ panels at $K{=}3$, $\binom{15}{5} = 3{,}003$ at $K{=}5$, and $\binom{15}{7} = 6{,}435$ at $K{=}7$, covering every combination of families and tiers. Each panel evaluates all benchmark items under all attack types, producing a complete panel $\times$ item $\times$ attack tensor. The primary analysis uses $K{=}3$; \S\ref{sec:cross_k} extends to larger panels.
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{lllccc}
13	\toprule
14	\textbf{Model} & \textbf{Family} & \textbf{Tier} & \textbf{Deploy} & \textbf{MMLU} & \textbf{ARC} \\
15	\midrule
16	gpt-5.5              & OpenAI    & frontier    & API   & .957 & .983 \\
17	gemini-3.1-pro-preview & Google  & frontier    & API   & .955 & .987 \\
18	claude-opus-4-6       & Anthropic & frontier   & API   & .890 & .987 \\
19	gemini-3.5-flash      & Google    & frontier   & API   & .968 & 1.00$^\dagger$ \\
20	\addlinespace
21	gpt-4.1               & OpenAI    & mid-tier   & API   & .837 & .967 \\
22	claude-sonnet-4-6     & Anthropic & mid-tier   & API   & .810 & .953 \\
23	\addlinespace
24	gpt-4.1-mini          & OpenAI    & lightweigh
…[truncated 9419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 492 · 2026-05-24T17:54:14.911862+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2424
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-24T17:54:15.423362+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2229
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-24T17:54:22.548607+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-24T17:54:23.551843+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Weakest-Link Dominance at \texorpdfstring{$K{=}3$}{K=3}}
5	\label{sec:dominance}
6	
7	Table~\ref{tab:dominance} reports the log-log OLS regression (Equation~\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\ref{tab:models}).
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\begin{tabular}{llccc}
13	\toprule
14	\textbf{Bench.} & \textbf{Attack} & $\boldsymbol{\eta_{\max}}$ & $\boldsymbol{K_{\mathrm{eff}}}$ & \textbf{Dom.} \\
15	\midrule
16	MMLU & Prompt inj.    & $+^{*}$ & $+^{*}$ & Co \\
17	MMLU & Sycophancy     & $+^{*}$ & $+^{*}$ & Co \\
18	MMLU & Score manip.   & n.s.    & $+^{*}$ & $K$ \\
19	MMLU & Verbosity      & $+^{*}$ & $+^{*}$ & Co \\
20	MMLU & Position bias  & $+^{*}$ & $+^{*}$ & Co \\
21	MMLU & Authority bias & $+^{*}$ & $+^{*}$ & Co \\
22	\addlinespace
23	ARC  & Prompt inj.    & $+^{*}$ & $+^{*}$ & Co \\
24	ARC  & Sycophancy     & $+^{*}$ & $+^{*}$ & Co \\
25	ARC  & Score manip.   & $+^{*}$ & $+^{*}$ & Co \\
26	ARC  & Verbosity      & $+^{*}$ & $+^{*}$ & Co \\
27	ARC  & Position bias  & n.s.    & $+^{*}$ & $K$ \\
28	ARC  & Authority bias & $+^{*}$ & $+^{*}$ & Co \\
29	\bottomrule
30	\end{tabular}
31	\caption{Standardized regression coefficients for $\eta_{\max}$ and $K_{\mathrm{eff}}$ across 12 conditions (455 panels, log-log OLS). $+^{*}$/$-^{*}$: FDR-significant positive/negative (Benjamini--Hochberg, $q < 0.05$); n.s.: not significant. Dom.\ column: $\eta$ = $\eta_{\max}$ sole dominant, $K$ = $K_{\mathrm{eff}}$ sole dominant, Co = co-dominant \citep{budescu1993dominance}.}
32	\label{tab:dominance}
33	\end{table}
34	
35	Under OLS, $K_{\mathrm{eff}}$ is positive and FDR-significant in all 12/12 conditions. $\eta_{\max}$ is significant in 10/12 (exceptions: MMLU $\times$ score manipulation and ARC $\times$ position bias), consistent with Theorem~\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\mathrm{eff}}$-dominant, and zero
…[truncated 6253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-24T17:54:23.552294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-24T17:54:24.054078+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\paragraph{Predictor Shift and Direction.}
5	At $K{=}3$, a single compromised judge flips the majority ($t{=}2$), making both predictors relevant. At $K{\geq}5$, no single judge is pivotal; $\eta_{\max}$'s contribution collapses while high-$K_{\mathrm{eff}}$ panels present more distinct attack surfaces ($K^* \in (3,5)$). $K_{\mathrm{eff}}$'s direction is positive in all 12 conditions (OLS and GAM bootstrap 12/12), but significance is method-sensitive (0--12/12; bootstrap 4/12 at $K{=}3$, 7/12 at $K{=}5$). No magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$; Appendix~\ref{app:bft_reversal}).
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{figures/fig_keff_eta_scatter.pdf}
10	\caption{Panel-level correlation between $K_{\mathrm{eff}}$ and $\eta_{\max}$ at $K{=}5$ ($n{=}3{,}003$ panels). Full model pool (gray, $r{=}0.81$) exhibits strong collinearity; capability-matched Pool~A (orange, $r{=}0.50$, 126 panels) shows reduced confounding.}
11	\label{fig:keff_eta_scatter}
12	\end{figure}
13	
14	\paragraph{Diversity--Capability Confound: A Fundamental Limitation.}
15	$K_{\mathrm{eff}}$ and $\eta_{\max}$ correlate at $r{=}0.70$--$0.81$ (VIF${\approx}2.0$--$2.9$; Figure~\ref{fig:keff_eta_scatter}), a fundamental limitation: maximizing diversity requires sampling across capability tiers (Appendix~\ref{app:diversity_capability}). Cinelli--Hazlett sensitivity analysis \citep{cinelli2020making} shows the confound suffices to explain the association in 69\% of conditions; RV exceeds $\eta_{\max}$ in only 3--4/12 per $K$ (Appendix~\ref{app:sensitivity}), though fractional logit provides directional support (9/12, 11/12, 12/12 at $K{=}3,5,7$; 98.6\% OLS concordance). Capability-matched subsampling (Pool~A: $r{=}0.50$) raises RV in 10/12 at $K{=}5$ despite max 30.1\% power (Appendix~\ref{app:sensitivity_poolA}); cross-benchmark IV provides additional identification (A
…[truncated 2156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-24T17:54:24.054419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-24T17:54:24.957269+00:00_

1	\section{Conclusion}
2	
3	We document a predictor shift: at $K{=}3$, both $\eta_{\max}$ and $K_{\mathrm{eff}}$ contribute; at $K{\geq}5$, $K_{\mathrm{eff}}$ dominates (7/12, 8/12) while $\eta_{\max}$ attenuates (2/12), with direction positive (12/12) but significance method-sensitive (0--12/12), confirmed by fractional logit (9/12, 11/12, 12/12). Aggregation influences predictability ($R^2$: 0.83--0.09). The diversity--capability confound ($r{=}0.70$--$0.81$; RV insufficient in 69\%) limits causal separation: screen $\eta_{\max}$ at $K{=}3$, monitor independence at $K{\geq}5$.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 902
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-24T17:54:24.957710+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 501 · 2026-05-24T17:54:25.509099+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 502 · 2026-05-24T17:54:25.710638+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 752
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-24T17:54:26.113546+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-24T17:54:32.489997+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 505 · 2026-05-24T17:54:33.001035+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-24T17:54:33.656461+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/review_round_5/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-24T17:54:34.264432+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1774
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-24T17:54:34.925881+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-24T17:54:35.479674+00:00_

1	\appendix
2	
3	\section{Proof of Theorem~\ref{thm:monotonicity}}
4	\label{app:proof}
5	
6	The replaced judge $J_K'$ is \emph{pivotal} exactly when $t{-}1$ of the remaining $K{-}1$ judges have already failed. Formally, let $S = \sum_{j=1}^{K-1} X_j^a$ denote the number of failures among the shared judges. The panel fails if and only if the $K$-th judge also fails when $S = t{-}1$, or when $S \geq t$ regardless of the $K$-th judge:
7	\begin{align}
8	\mathrm{ASR}(\mathcal{P}, a) &= \Pr(S \geq t) + \Pr(S = t{-}1) \cdot \Pr(X_K^a {=} 1 \mid S = t{-}1).
9	\end{align}
10	Since $\Pr(X_{K'}^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K}) \geq \Pr(X_K^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K})$ for all attacks $a$ and realizations $\mathbf{x}_{-K}$ (by hypothesis), the second term is weakly larger for $\mathcal{P}'$ than for $\mathcal{P}$ under every attack. Taking the supremum over attacks preserves the inequality: $\mathrm{ASR}^*(\mathcal{P}') \geq \mathrm{ASR}^*(\mathcal{P})$. The result holds under arbitrary inter-judge correlations and any attack space $\mathcal{A}$.
11	
12	\section{Robustness Correction Methods}
13	\label{app:robustness_methods}
14	
15	The 455 panels are constructed combinatorially from 15 shared judges: each judge appears in $\binom{14}{2} = 91$ panels, inducing correlated residuals across panel-level observations. Standard OLS assumes independent errors, potentially inflating significance. We apply three corrections.
16	
17	\paragraph{Clustered Standard Errors.} Because each panel of $K{=}3$ judges does not map to a single cluster, we perform three separate one-way clusterings (one for each judge position in the ordered panel tuple) using CR1 bias-corrected sandwich estimators (13 clusters per position). The reported standard error for each coefficient is the maximum across the three clusterings, yielding the most conservative inference.
18	
19	\paragraph{Mixed Effects.} For each of the three judge positions, we fit a linear mixed-effec
…[truncated 41427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool result

_source line 510 · 2026-05-24T17:54:35.838921+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2182
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-24T17:54:35.890992+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2889
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-24T17:54:43.068475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix_attacks.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix_attacks.tex"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-24T17:54:43.169469+00:00_

1	\section{Attack Prompt Templates}
2	\label{app:attacks}
3	
4	Table~\ref{tab:attack-templates} lists the six manipulation strategies used in our experiments. Each attack modifies the ground-truth loser response to exploit a specific judge bias. Below we describe each attack type and provide representative template text.
5	
6	\paragraph{Prompt Injection.} Injects directive text at the end of the loser response, attempting to override the judge's evaluation logic with explicit scoring instructions.
7	
8	\paragraph{Sycophancy Exploitation.} Wraps the loser response in enthusiastic, agreeable language (a prefix and suffix), exploiting judges' preference for polite and eager responses.
9	
10	\paragraph{Score Manipulation.} Appends fabricated self-assessment scores to the loser response, leveraging judges' tendency to defer to confident quality claims embedded in the text.
11	
12	\paragraph{Verbosity Bias.} Appends a lengthy but content-free elaboration ($\sim$50--60 words) to the loser response, exploiting judges' bias toward longer responses regardless of substantive contribution.
13	
14	\paragraph{Position Bias.} Swaps the positions of response A and response B so that the ground-truth winner occupies position B, exploiting judges' tendency to favor position A.
15	
16	\paragraph{Authority Bias.} Prepends fabricated citations to prestigious institutions or journals at the beginning of the loser response, exploiting judges' deference to perceived academic authority.
17	
18	\begin{table*}[t]
19	\centering
20	\small
21	\caption{Representative prompt templates for each attack type. Templates shown are appended to, prepended to, or used to wrap the ground-truth loser response. Position bias has no template text; it swaps response order.}
22	\label{tab:attack-templates}
23	\begin{tabular}{@{}l p{11.5cm}@{}}
24	\toprule
25	\textbf{Attack Type} & \textbf{Representative Template} \\
26	\midrule
27	Prompt Injection &
28	\texttt{\textbackslash n\textbackslash n[Note: This respons
…[truncated 3749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-24T17:57:54.639418+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM judge adversarial robustness multi-judge panel diversity vulnerability 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM judge adversarial robustness multi-judge panel diversity vulnerability 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 515 · 2026-05-24T17:57:55.041365+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ensemble diversity adversarial vulnerability information theoretic K-effective independence 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ensemble diversity adversarial vulnerability information theoretic K-effective independence 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 516 · 2026-05-24T17:58:05.249617+00:00_

Web search results for query: "LLM judge adversarial robustness multi-judge panel diversity vulnerability 2025 2026"

Links: [{"title":"Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment","url":"https://arxiv.org/pdf/2402.14016"},{"title":"When AIs Judge AIs: The Rise of Agent-as-a-Judge Evaluation for LLMs","url":"https://arxiv.org/html/2508.02994v1"},{"title":"LLM-as-Judge Mechanism","url":"https://www.emergentmind.com/topics/llm-as-judge-mechanism"},{"title":"LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge","url":"https://arxiv.org/html/2506.09443v1"},{"title":"A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness","url":"https://arxiv.org/pdf/2603.06594"},{"title":"Adversarial Attacks on LLM-as-a-Judge Systems: Insights from Prompt Injections","url":"https://arxiv.org/html/2504.18333v1"},{"title":"Benchmarking adversarial robustness to bias elicitation in large language models: scalable automated assessment with LLM-as-a-judge | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10994-025-06862-6"},{"title":"[2505.13348] Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks","url":"https://arxiv.org/abs/2505.13348"},{"title":"LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge","url":"https://arxiv.org/pdf/2506.09443"}]

## Web Search Results

I found comprehensive research on LLM judge adversarial robustness and multi-judge panel diversity. Here are the key findings:

### Adversarial Vulnerabilities of LLM Judges

Modern LLM judges are highly vulnerable to adversarial attacks, particularly when used for absolute scoring in a zero-shot configuration. Both LLM-scoring and pairwise LLM-comparative assessment are vulnerable to attacks, with universal phrases of under 5 tokens capable of tricking systems into providing
…[truncated 1210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10610
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-24T17:58:14.033429+00:00_

Web search results for query: "ensemble diversity adversarial vulnerability information theoretic K-effective independence 2025 2026"

Links: [{"title":"DVERGE: Diversifying Vulnerabilities for Enhanced Robust ...","url":"https://proceedings.neurips.cc/paper/2020/file/3ad7c2ebb96fcba7cda0cf54a2e802f5-Paper.pdf"},{"title":"[2410.06851] Understanding Model Ensemble in Transferable Adversarial Attack","url":"https://ar5iv.labs.arxiv.org/html/2410.06851"},{"title":"DVERGE: Diversifying Vulnerabilities for Enhanced Robust Generation of   Ensembles","url":"https://arxiv.org/pdf/2009.14720"},{"title":"Understanding Model Ensemble in Transferable Adversarial Attack","url":"https://arxiv.org/html/2410.06851v1"},{"title":"Understanding Model Ensemble in Transferable Adversarial Attack","url":"https://arxiv.org/pdf/2410.06851"},{"title":"[1901.09981] Improving Adversarial Robustness of Ensembles with Diversity Training","url":"https://ar5iv.labs.arxiv.org/html/1901.09981"},{"title":"Toward Adversarial Robustness by Diversity in an Ensemble of Specialized   Deep Neural Networks","url":"https://arxiv.org/pdf/2005.08321"}]

Based on the search results, I found relevant research on ensemble diversity, adversarial vulnerability, and information-theoretic approaches:

## Key Findings

### Recent Theoretical Framework (2024)

A fundamental trade-off between vulnerability and diversity makes it challenging to maximize both simultaneously in ensemble-based adversarial attacks. Information theory tools are crucial for addressing the complex issue of relaxing the independence assumption among surrogate classifiers.

### Information-Theoretic Analysis

Recent work applies mathematical tools from information theory to bound transferability error using complexity and generalization terms, validating guidelines for reducing transferability error: incorporating more surrogate models, increasing their diversity, and reducing their complexity in cases of overfitting.

### Ensemble Diversity Str
…[truncated 931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 18992
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-24T17:58:57.822311+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "echo \"Multi-judge LLM evaluation panels are assumed to benefit from diversity, yet diversity's relationship to adversarial vulnerability is poorly understood. We decompose panel attack success into individual judge weakness and structural diversity across 15 models, six attack types, two benchmarks, and panel sizes K in 3, 5, 7 up to 6,435 panels. Consistent with adversarial ensemble theory but newly characterized in the LLM judge setting, K_eff's coefficient direction is positive in all 12 conditions 12/12 under OLS, though significance is method-sensitive 0-12/12 across inference methods and the diversity-capability confound r=0.70-0.81 limits causal interpretation. The predictors' relative importance shifts with panel size: at K=3, both contribute; at K>=5, K_eff becomes the dominant predictor while eta_max sharply attenuates. Cinelli-Hazlett sensitivity analysis reveals that K_eff's robustness value does not exceed the known confound in 69% of conditions 25/36, but fractional logit with clustered standard errors confirms the positive association in most conditions K=3: 9/12; K=5: 11/12; K=7: 12/12. Aggregation rules influence predictability R2: threshold 0.83, Bayesian 0.09. The defense strategy should be informed by panel size: small panels benefit from screening for individual robustness; larger panels benefit from monitoring judge independence.\" | wc -w",
  "description": "Count abstract words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "echo \"Multi-judge LLM evaluation panels are assumed to benefit from diversity, yet diversity's relationship to adversarial vulnerability is poorly understood. We decompose panel attack success into individual judge weakness and structural diversity across 15 models, six attack types, two benchmarks, and panel sizes K in 3, 5, 7 up to 6,435 panels. Consistent with adversarial ensemble theory but newly characterized in the LLM judge setting, K_eff's coefficient direction is positive in all 12 conditions 12/12 under OLS, though significance is method-sensitive 0-12/12 across inference methods and the diversity-capability confound r=0.70-0.81 limits causal interpretation. The predictors' relative importance shifts with panel size: at K=3, both contribute; at K>=5, K_eff becomes the dominant predictor while eta_max sharply attenuates. Cinelli-Hazlett sensitivity analysis reveals that K_eff's robustness value does not exceed the known confound in 69% of conditions 25/36, but fractional logit with clustered standard errors confirms the positive association in most conditions K=3: 9/12; K=5: 11/12; K=7: 12/12. Aggregation rules influence predictability R2: threshold 0.83, Bayesian 0.09. The defense strategy should be informed by panel size: small panels benefit from screening for individual robustness; larger panels benefit from monitoring judge independence.\" | wc -w",
    "description": "Count abstract words"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-24T17:58:57.973373+00:00_

187

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-24T17:59:12.438603+00:00_

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
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
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

_source line 521 · 2026-05-24T17:59:12.589510+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-24T18:01:13.571900+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告：The Shifting Predictor: Panel-Size-Dependent Vulnerability Patterns in LLM Judge Panels\n\n**审查侧重：新颖性 + 完整性 + 写作质量 + 格式合规**\n\n---\n\n## 总体评分\n**Overall Assessment**: 3.0 / 5（Findings — 可被 Findings 接收）\n**Confidence**: 4 / 5（对评估有较高把握，熟悉对抗鲁棒性、集成方法和 LLM 评估领域）\n**一句话总结**: 方法论严谨、统计分析全面的实证研究，但核心发现（predictor shift）受限于严重的 diversity–capability 混淆（r=0.70–0.81），且仅覆盖多选题基准，新颖性和影响力不足以支撑主会议接收。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法扎实（5种推断方法、crossed RE、Cinelli-Hazlett敏感性分析），但 r=0.70–0.81 的混淆在 69% 条件下足以解释 K_eff 关联，核心 claim 的因果解释力弱 |\n| Excitement | 2.5/5 | Predictor shift 是有趣的经验观察，但本质是描述性发现；实际建议（小 panel 筛 η_max、大 panel 监控独立性）较为直觉化；仅 MC 任务限制了影响力 |\n| Reproducibility | 4/5 | 使用公开基准（MMLU/ARC），报告了随机种子（42）、所有超参数，承诺开源；但 9 个 API 模型依赖 OpenRouter 快照，可复现性受 API 版本漂移影响 |\n| Datasets | 2/5 | 未提交可用数据集，仅承诺 upon acceptance 发布 |\n| Software | 2/5 | 未提交可用代码，仅承诺 upon acceptance 发布 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Diversity–capability 混淆严重削弱核心贡献的解释力\n- 具体位置：Section 6 (Analysis), Figure 5, Appendix J (Table 10)\n- 问题：K_eff 与 η_max 的相关性为 r=0.70–0.81（VIF≈2.0–2.9）。Cinelli-Hazlett 分析显示，在 69% 的条件下（25/36），已知的 η_max 混淆即可解释 K_eff 的关联（Table 10, Exc. 列仅 11/36 打勾）。这意味着论文无法可靠区分\"多样性增加脆弱性\"和\"引入弱模型增加脆弱性\"。尽管论文反复声明这是描述性发现（Introduction L20, Conclusion），但标题 \"The Shifting Predictor\" 和贡献 1 的 framing 仍暗示 K_eff 是一个独立有意义的预测变量。\n- 为什么影响接收：这是论文的 fundamental limitation——核心发现的因果解释力不足。如果 K_eff 的效应大部分可被 capability deficit 解释，那么 \"predictor shift\" 可能只是反映了在大 panel 中弱模型的累积效应变得更显著，而非 diversity 本身的作用。\n- 建议修改方向：(1) 调整标题和 framing，明确强调这是混淆条件下的关联性发现；(2) 在 Pool A（r=0.50）上展示更多结果——目前 Pool A 在 K=5 时 power 仅 30.1%，无法有效验证；(3) 考虑使用 capability-matched pairs 的配对设计来更好地分离 diversity 的独立贡献。\n\n**N2** [critical] 仅覆盖多选题基准，泛化性存疑\n- 具体位置：Section 4.1, Limitations (page 8)\n- 问题：实验仅使用 MMLU 和 ARC（均为多选题）。然而 LLM judge panel 的主要实际应用场景是 open-ended generation（故事写作、代码生成、对话评估等），这些任务的攻击面和 diversity-vulnerability 关系可能根本不同。多选题的 judge 判断是离散的（A/B/tie），而 open-ended 评估涉及更复杂的质量维度。\n- 为什么影响接收：论文标题和 Introduction 的 framing 面向 \"LLM Judge Panels\" 的一般性结论，但证据仅覆盖了最简单的评估类型。缺乏 open-ended 评估的任何实验或讨论，使得发现的适用范围不确定。\n- 建议修改方向：(1) 至少增加一个 open-ended 基准（如 AlpacaEval、MT-Bench）的初步实验；(2) 如果无法增加实验，应在标题和 Abstract 中明确限定为 multiple-choice evaluation，并在 Discussion 中深入分析为什么 open-ended 场景可能不同。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Predictor shift 可能部分是统计功效差异的产物\n- 具体位置：Section 5.2, Appendix P (Table 14)\n- 问题：K=3 时 455 panels，MDE=0.144 SD；K=5 时 3,003 panels，MDE=0.048 SD。K_eff 显著性从 4/12（K=3）升至 7/12（K=5）——这一\"shift\"的部分原因可能是 K=5 的统计功效显著增强（3倍 MDE 改善），而非 K_eff 的真实效应增大。论文在 Appendix P 中以 η_max 的反向变化（3/12→2/12）来论证这不纯粹是功效问题，但 η_max 的下降幅度很小（仅 1/12 的差异），不具有强说服力。\n- 建议：在正文中更充分讨论 power 与 shift 的关系。可以用 effect size（β_std）的变化而非显著性计数来展示 shift，因为 effect size 不受样本量影响。\n\n**W2** [warning] Aggregation rules 分析表面化\n- 具体位置：Section 5.5 (Table 4), Section 6, Appendix D.5/D.6\n- 问题：Threshold（R²=0.83）与 Bayesian（R²=0.09）的 10 倍差异是一个重要发现，但分析仅用一段话解释了机制（\"calibrated reliability weighting downweights weak judges\"）。更关键的是，Bayesian 的非单调行为（K_eff 显著性：K=3 时 6/12 → K=5 时 7/12 → K=7 时 0/12）缺乏深入解释。论文说\"posterior concentrates on 2–3 accurate judges, compressing K_eff variation\"，但这个解释未经验证——没有展示 posterior weight 的分布或 K_eff variation 在 Bayesian 下的实际变化。\n- 建议：增加 Bayesian 权重分布的分析（不同 K 下权重集中度的变化），验证\"posterior concentration\"假说。\n\n**W3** [warning] Conclusion 过于简略\n- 具体位置：Section 7 (Conclusion)\n- 问题：Conclusion 仅 3 句话，本质上是 Abstract 的压缩版。缺少：(1) 对发现的更广泛解读——predictor shift 对 LLM evaluation 实践意味着什么？(2) 明确的 future work 方向——如何解决混淆问题？open-ended 场景如何？(3) 对社区的 take-away message。这与论文其余部分的详尽分析形成不对称。\n- 建议：扩展 Conclusion 至 1/3–1/2 column，增加 implications 和 future directions。\n\n**W4** [warning] K_eff 的新颖性相对于现有 diversity metrics 较弱\n- 具体位置：Section 6 (K_eff vs. Alternative Diversity Measures), Appendix Q (Table 15)\n- 问题：K_eff 与 κ-diversity 的相关性为 ρ=0.978，与 disagreement rate 为 ρ=0.934。在预测 ASR 方面，κ-diversity 在 K=3 时更强（8/12 vs 4/12），在 K≥5 时接近（6-7/12 vs 7-8/12）。论文声称 K_eff 的优势在于\"可解释性\"（quantifies effective independent channels），但这一论证不充分——如果两个 metric 高度共线（ρ=0.978），则选择哪个主要是 framing 问题，而非实质贡献。\n- 建议：更诚实地定位 K_eff 的贡献。K_eff 的真正独特价值在于它展示了 predictor shift（κ-diversity 不展示），这本身是有意义的——但需要更清楚地阐述为什么 MI-based 变换捕捉到了 κ-diversity 遗漏的结构。\n\n**W5** [warning] INT4 量化引入系统性混淆\n- 具体位置：Section 4.1 (Table 1), Section 6 (API-Only vs. Full Pool)\n- 问题：6 个 local 模型使用 AWQ INT4 量化，准确率为 25–54%（显著低于 API 模型的 63–100%）。论文自己指出这\"conflates genuine capability limitations with quantization damage\"。这些模型驱动了 K_eff 的变异（Section 6: 去掉后 K_eff 从 7/12 降到 2-3/12），但也正是它们造成了 diversity-capability 混淆。API-only 分析（r=0.85, VIF=4.4）中 predictor shift 不复现（Table 8），这引起了对核心发现是否依赖于量化伪影的担忧。\n- 建议：在正文中更明确地讨论量化作为混淆源的影响。考虑增加使用 FP16 local 模型的验证实验，或至少论证为什么 INT4 的影响不会根本性地改变结论。\n\n---\n\n## 小问题（不影响接收）\n\n1. **术语不完全一致**：正文多处使用 \"predictor shift\"，但 Figure 3 caption 使用 \"predictor shift zone\" 和 \"shift zone\"，Section 5.2 用 \"K=3 pattern is method-sensitive\"。建议统一使用 \"predictor shift\" 并在首次使用时给出明确定义。\n\n2. **数字密度过高**：Results 和 Analysis 几乎每句话都包含多个括号统计量（如 \"positive in all 12 conditions (12/12 under OLS), though significance is method-sensitive (0–12/12 across inference methods) and the diversity–capability confound (r=0.70–0.81) limits causal interpretation\"）。建议对关键发现先给直觉解释，再附数字支撑。\n\n3. **Abstract 中 \"newly characterized in the LLM judge setting\" 的表述**：这隐含了 predictor shift 在其他领域已知但在 LLM judge 中是新的。实际上论文声称这是全新发现。建议改为更明确的表述。\n\n4. **Table 1 脚注的 gemini-3.5-flash 26.3% format error rate**：格式错误率如此高的模型是否应该包含在分析中？这可能引入噪声。虽然不影响结论方向，但值得讨论。\n\n5. **Use of AI Assistants (Appendix V)**：披露使用 Claude 辅助代码、写作和文献整理——符合 ACL policy 的透明性要求，无问题。\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 说明 |\n|------|------|------|\n| 正文页数 ≤8 | ✅ | 正文（Abstract–Conclusion）8页，Limitations 不计入 |\n| Abstract ≤200 words | ✅ | 约 187 词 |\n| ACL 2-column + [review] | ✅ | \\usepackage[review]{acl} |\n| Double-blind 匿名 | ✅ | 作者标注为 \"Anonymous\" |\n| Limitations section 在正文内 | ✅ | 位于 page 8，Conclusion 之后 |\n| Appendix 无 Limitations | ✅ | 附录仅含技术细节 |\n| 参考文献格式 | ✅ | 标准 BibTeX，格式一致 |\n| 图表质量 | ✅ | 清晰可读，Figure 1 框架图有效传达流程 |\n\n---\n\n## 可能遗漏的相关工作\n\n1. **Li et al. (2024) \"Understanding Model Ensemble in Transferable Adversarial Attack\"** (arXiv:2410.06851): 该工作从信息论角度分析集成模型中 diversity 如何影响对抗 transferability，与本文使用 MI-based K_eff 度量 diversity 高度相关。论文未引用。\n\n2. **Zhu et al. (2020) \"DVERGE: Diversifying Vulnerabilities for Enhanced Robust Generation of Ensembles\"** (NeurIPS 2020): 明确处理 ensemble 中 diversity 与 vulnerability 的关系，通过分离 non-robust features 来多样化脆弱性。虽然在 vision 领域，但与本文的 diversity-vulnerability tradeoff 直接相关。论文未引用。\n\n3. 论文已充分讨论 CollabEval (Qian et al., 2026) 和 DBEI (Kuai et al., 2026)，对比清晰。\n\n---\n\n## 主要优势\n\n1. **方法论严谨性出色**：5种推断方法（OLS、clustered SE、mixed effects、wild bootstrap、fractional logit）+ crossed random effects + Cinelli-Hazlett 敏感性分析 + 多种 subsampling 策略。20 个附录节提供了极其详尽的 robustness checks。这一方法论标准值得其他实证研究借鉴。\n\n2. **诚实的 self-critique**：论文反复、明确地承认 diversity-capability 混淆的局限性（Introduction L20、Section 6、Limitations），不回避对核心发现不利的证据（如 K=3 时 clustered SE 下 K_eff 显著性为 0/12）。这种科学诚信在同行评审论文中难能可贵。\n\n3. **实验规模充分**：15 模型、6 攻击类型、2 基准、3 panel 大小（最多 6,435 panels），覆盖了 exhaustive enumeration 而非采样，确保了结论的完整性。\n\n4. **Theorem 1（Weakest-Link Monotonicity）提供了理论锚点**：虽然证明本身简单，但它为 η_max 作为预测变量提供了理论基础，并且 empirical verification（58% stochastic dominance in 61/105 pairs）加强了理论-实验的连接。\n\n5. **实用导向的 panel 设计建议**：Figure 4 (panel selection strategy comparison) 给出了清晰的实践指导——min(η_max) 在所有 12 个条件下 ASR 最低，这对部署者有直接价值。\n\n---\n\n## Questions for Authors\n\nQ1: 在 API-only 分析中（Table 8, r=0.85），predictor shift 不复现。这是否意味着 shift 依赖于 INT4 量化引入的 capability gap？如果未来 local 模型质量提升（缩小 capability gap），predictor shift 是否会消失？\n\nQ2: K_eff 在 clean data 上计算但用于预测 attacked vulnerability。对于 position bias（clean-attacked ρ=0.08, Table 9），K_eff 几乎失效。这是否意味着 K_eff 作为预测工具在实际部署中需要知道攻击类型？\n\nQ3: Bayesian calibration 在 K=7 时完全中和了 K_eff（0/12）。这是否暗示 Bayesian aggregation 是消除 diversity-vulnerability tradeoff 的有效防御？如果是，这一发现似乎比 predictor shift 更具实际价值——为什么不作为主要贡献？\n\nQ4: 论文选择 K ∈ {3,5,7}（仅奇数）。K* ∈ (3,5) 的 shift 阈值未精确定位。K=4 或 K=6 的行为如何？偶数 K 下的 tie-breaking 机制可能改变 shift 的性质。",
  "reviewer_id": "2",
  "project": "cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8afaeea93cf69f72a8cefdfe533b3c23:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿报告：The Shifting Predictor: Panel-Size-Dependent Vulnerability Patterns in LLM Judge Panels\n\n**审查侧重：新颖性 + 完整性 + 写作质量 + 格式合规**\n\n---\n\n## 总体评分\n**Overall Assessment**: 3.0 / 5（Findings — 可被 Findings 接收）\n**Confidence**: 4 / 5（对评估有较高把握，熟悉对抗鲁棒性、集成方法和 LLM 评估领域）\n**一句话总结**: 方法论严谨、统计分析全面的实证研究，但核心发现（predictor shift）受限于严重的 diversity–capability 混淆（r=0.70–0.81），且仅覆盖多选题基准，新颖性和影响力不足以支撑主会议接收。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法扎实（5种推断方法、crossed RE、Cinelli-Hazlett敏感性分析），但 r=0.70–0.81 的混淆在 69% 条件下足以解释 K_eff 关联，核心 claim 的因果解释力弱 |\n| Excitement | 2.5/5 | Predictor shift 是有趣的经验观察，但本质是描述性发现；实际建议（小 panel 筛 η_max、大 panel 监控独立性）较为直觉化；仅 MC 任务限制了影响力 |\n| Reproducibility | 4/5 | 使用公开基准（MMLU/ARC），报告了随机种子（42）、所有超参数，承诺开源；但 9 个 API 模型依赖 OpenRouter 快照，可复现性受 API 版本漂移影响 |\n| Datasets | 2/5 | 未提交可用数据集，仅承诺 upon acceptance 发布 |\n| Software | 2/5 | 未提交可用代码，仅承诺 upon acceptance 发布 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Diversity–capability 混淆严重削弱核心贡献的解释力\n- 具体位置：Section 6 (Analysis), Figure 5, Appendix J (Table 10)\n- 问题：K_eff 与 η_max 的相关性为 r=0.70–0.81（VIF≈2.0–2.9）。Cinelli-Hazlett 分析显示，在 69% 的条件下（25/36），已知的 η_max 混淆即可解释 K_eff 的关联（Table 10, Exc. 列仅 11/36 打勾）。这意味着论文无法可靠区分\"多样性增加脆弱性\"和\"引入弱模型增加脆弱性\"。尽管论文反复声明这是描述性发现（Introduction L20, Conclusion），但标题 \"The Shifting Predictor\" 和贡献 1 的 framing 仍暗示 K_eff 是一个独立有意义的预测变量。\n- 为什么影响接收：这是论文的 fundamental limitation——核心发现的因果解释力不足。如果 K_eff 的效应大部分可被 capability deficit 解释，那么 \"predictor shift\" 可能只是反映了在大 panel 中弱模型的累积效应变得更显著，而非 diversity 本身的作用。\n- 建议修改方向：(1) 调整标题和 framing，明确强调这是混淆条件下的关联性发现；(2) 在 Pool A（r=0.50）上展示更多结果——目前 Pool A 在 K=5 时 power 仅 30.1%，无法有效验证；(3) 考虑使用 capability-matched pairs 的配对设计来更好地分离 diversity 的独立贡献。\n\n**N2** [critical] 仅覆盖多选题基准，泛化性存疑\n- 具体位置：Section 4.1, Limitations (page 8)\n- 问题：实验仅使用 MMLU 和 ARC（均为多选题）。然而 LLM judge panel 的主要实际应用场景是 open-ended generation（故事写作、代码生成、对话评估等），这些任务的攻击面和 diversity-vulnerability 关系可能根本不同。多选题的 judge 判断是离散的（A/B/tie），而 open-ended 评估涉及更复杂的质量维度。\n- 为什么影响接收：论文标题和 Introduction 的 framing 面向 \"LLM Judge Panels\" 的一般性结论，但证据仅覆盖了最简单的评估类型。缺乏 open-ended 评估的任何实验或讨论，使得发现的适用范围不确定。\n- 建议修改方向：(1) 至少增加一个 open-ended 基准（如 AlpacaEval、MT-Bench）的初步实验；(2) 如果无法增加实验，应在标题和 Abstract 中明确限定为 multiple-choice evaluation，并在 Discussion 中深入分析为什么 open-ended 场景可能不同。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Predictor shift 可能部分是统计功效差异的产物\n- 具体位置：Section 5.2, Appendix P (Table 14)\n- 问题：K=3 时 455 panels，MDE=0.144 SD；K=5 时 3,003 panels，MDE=0.048 SD。K_eff 显著性从 4/12（K=3）升至 7/12（K=5）——这一\"shift\"的部分原因可能是 K=5 的统计功效显著增强（3倍 MDE 改善），而非 K_eff 的真实效应增大。论文在 Appendix P 中以 η_max 的反向变化（3/12→2/12）来论证这不纯粹是功效问题，但 η_max 的下降幅度很小（仅 1/12 的差异），不具有强说服力。\n- 建议：在正文中更充分讨论 power 与 shift 的关系。可以用 effect size（β_std）的变化而非显著性计数来展示 shift，因为 effect size 不受样本量影响。\n\n**W2** [warning] Aggregation rules 分析表面化\n- 具体位置：Section 5.5 (Table 4), Section 6, Appendix D.5/D.6\n- 问题：Threshold（R²=0.83）与 Bayesian（R²=0.09）的 10 倍差异是一个重要发现，但分析仅用一段话解释了机制（\"calibrated reliability weighting downweights weak judges\"）。更关键的是，Bayesian 的非单调行为（K_eff 显著性：K=3 时 6/12 → K=5 时 7/12 → K=7 时 0/12）缺乏深入解释。论文说\"posterior concentrates on 2–3 accurate judges, compressing K_eff variation\"，但这个解释未经验证——没有展示 posterior weight 的分布或 K_eff variation 在 Bayesian 下的实际变化。\n- 建议：增加 Bayesian 权重分布的分析（不同 K 下权重集中度的变化），验证\"posterior concentration\"假说。\n\n**W3** [warning] Conclusion 过于简略\n- 具体位置：Section 7 (Conclusion)\n- 问题：Conclusion 仅 3 句话，本质上是 Abstract 的压缩版。缺少：(1) 对发现的更广泛解读——predictor shift 对 LLM evaluation 实践意味着什么？(2) 明确的 future work 方向——如何解决混淆问题？open-ended 场景如何？(3) 对社区的 take-away message。这与论文其余部分的详尽分析形成不对称。\n- 建议：扩展 Conclusion 至 1/3–1/2 column，增加 implications 和 future directions。\n\n**W4** [warning] K_eff 的新颖性相对于现有 diversity metrics 较弱\n- 具体位置：Section 6 (K_eff vs. Alternative Diversity Measures), Appendix Q (Table 15)\n- 问题：K_eff 与 κ-diversity 的相关性为 ρ=0.978，与 disagreement rate 为 ρ=0.934。在预测 ASR 方面，κ-diversity 在 K=3 时更强（8/12 vs 4/12），在 K≥5 时接近（6-7/12 vs 7-8/12）。论文声称 K_eff 的优势在于\"可解释性\"（quantifies effective independent channels），但这一论证不充分——如果两个 metric 高度共线（ρ=0.978），则选择哪个主要是 framing 问题，而非实质贡献。\n- 建议：更诚实地定位 K_eff 的贡献。K_eff 的真正独特价值在于它展示了 predictor shift（κ-diversity 不展示），这本身是有意义的——但需要更清楚地阐述为什么 MI-based 变换捕捉到了 κ-diversity 遗漏的结构。\n\n**W5** [warning] INT4 量化引入系统性混淆\n- 具体位置：Section 4.1 (Table 1), Section 6 (API-Only vs. Full Pool)\n- 问题：6 个 local 模型使用 AWQ INT4 量化，准确率为 25–54%（显著低于 API 模型的 63–100%）。论文自己指出这\"conflates genuine capability limitations with quantization damage\"。这些模型驱动了 K_eff 的变异（Section 6: 去掉后 K_eff 从 7/12 降到 2-3/12），但也正是它们造成了 diversity-capability 混淆。API-only 分析（r=0.85, VIF=4.4）中 predictor shift 不复现（Table 8），这引起了对核心发现是否依赖于量化伪影的担忧。\n- 建议：在正文中更明确地讨论量化作为混淆源的影响。考虑增加使用 FP16 local 模型的验证实验，或至少论证为什么 INT4 的影响不会根本性地改变结论。\n\n---\n\n## 小问题（不影响接收）\n\n1. **术语不完全一致**：正文多处使用 \"predictor shift\"，但 Figure 3 caption 使用 \"predictor shift zone\" 和 \"shift zone\"，Section 5.2 用 \"K=3 pattern is method-sensitive\"。建议统一使用 \"predictor shift\" 并在首次使用时给出明确定义。\n\n2. **数字密度过高**：Results 和 Analysis 几乎每句话都包含多个括号统计量（如 \"positive in all 12 conditions (12/12 under OLS), though significance is method-sensitive (0–12/12 across inference methods) and the diversity–capability confound (r=0.70–0.81) limits causal interpretation\"）。建议对关键发现先给直觉解释，再附数字支撑。\n\n3. **Abstract 中 \"newly characterized in the LLM judge setting\" 的表述**：这隐含了 predictor shift 在其他领域已知但在 LLM judge 中是新的。实际上论文声称这是全新发现。建议改为更明确的表述。\n\n4. **Table 1 脚注的 gemini-3.5-flash 26.3% format error rate**：格式错误率如此高的模型是否应该包含在分析中？这可能引入噪声。虽然不影响结论方向，但值得讨论。\n\n5. **Use of AI Assistants (Appendix V)**：披露使用 Claude 辅助代码、写作和文献整理——符合 ACL policy 的透明性要求，无问题。\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 说明 |\n|------|------|------|\n| 正文页数 ≤8 | ✅ | 正文（Abstract–Conclusion）8页，Limitations 不计入 |\n| Abstract ≤200 words | ✅ | 约 187 词 |\n| ACL 2-column + [review] | ✅ | \\usepackage[review]{acl} |\n| Double-blind 匿名 | ✅ | 作者标注为 \"Anonymous\" |\n| Limitations section 在正文内 | ✅ | 位于 page 8，Conclusion 之后 |\n| Appendix 无 Limitations | ✅ | 附录仅含技术细节 |\n| 参考文献格式 | ✅ | 标准 BibTeX，格式一致 |\n| 图表质量 | ✅ | 清晰可读，Figure 1 框架图有效传达流程 |\n\n---\n\n## 可能遗漏的相关工作\n\n1. **Li et al. (2024) \"Understanding Model Ensemble in Transferable Adversarial Attack\"** (arXiv:2410.06851): 该工作从信息论角度分析集成模型中 diversity 如何影响对抗 transferability，与本文使用 MI-based K_eff 度量 diversity 高度相关。论文未引用。\n\n2. **Zhu et al. (2020) \"DVERGE: Diversifying Vulnerabilities for Enhanced Robust Generation of Ensembles\"** (NeurIPS 2020): 明确处理 ensemble 中 diversity 与 vulnerability 的关系，通过分离 non-robust features 来多样化脆弱性。虽然在 vision 领域，但与本文的 diversity-vulnerability tradeoff 直接相关。论文未引用。\n\n3. 论文已充分讨论 CollabEval (Qian et al., 2026) 和 DBEI (Kuai et al., 2026)，对比清晰。\n\n---\n\n## 主要优势\n\n1. **方法论严谨性出色**：5种推断方法（OLS、clustered SE、mixed effects、wild bootstrap、fractional logit）+ crossed random effects + Cinelli-Hazlett 敏感性分析 + 多种 subsampling 策略。20 个附录节提供了极其详尽的 robustness checks。这一方法论标准值得其他实证研究借鉴。\n\n2. **诚实的 self-critique**：论文反复、明确地承认 diversity-capability 混淆的局限性（Introduction L20、Section 6、Limitations），不回避对核心发现不利的证据（如 K=3 时 clustered SE 下 K_eff 显著性为 0/12）。这种科学诚信在同行评审论文中难能可贵。\n\n3. **实验规模充分**：15 模型、6 攻击类型、2 基准、3 panel 大小（最多 6,435 panels），覆盖了 exhaustive enumeration 而非采样，确保了结论的完整性。\n\n4. **Theorem 1（Weakest-Link Monotonicity）提供了理论锚点**：虽然证明本身简单，但它为 η_max 作为预测变量提供了理论基础，并且 empirical verification（58% stochastic dominance in 61/105 pairs）加强了理论-实验的连接。\n\n5. **实用导向的 panel 设计建议**：Figure 4 (panel selection strategy comparison) 给出了清晰的实践指导——min(η_max) 在所有 12 个条件下 ASR 最低，这对部署者有直接价值。\n\n---\n\n## Questions for Authors\n\nQ1: 在 API-only 分析中（Table 8, r=0.85），predictor shift 不复现。这是否意味着 shift 依赖于 INT4 量化引入的 capability gap？如果未来 local 模型质量提升（缩小 capability gap），predictor shift 是否会消失？\n\nQ2: K_eff 在 clean data 上计算但用于预测 attacked vulnerability。对于 position bias（clean-attacked ρ=0.08, Table 9），K_eff 几乎失效。这是否意味着 K_eff 作为预测工具在实际部署中需要知道攻击类型？\n\nQ3: Bayesian calibration 在 K=7 时完全中和了 K_eff（0/12）。这是否暗示 Bayesian aggregation 是消除 diversity-vulnerability tradeoff 的有效防御？如果是，这一发现似乎比 predictor shift 更具实际价值——为什么不作为主要贡献？\n\nQ4: 论文选择 K ∈ {3,5,7}（仅奇数）。K* ∈ (3,5) 的 shift 阈值未精确定位。K=4 或 K=6 的行为如何？偶数 K 下的 tie-breaking 机制可能改变 shift 的性质。",
    "reviewer_id": "2",
    "project": "cert_manip_resist_eval"
  }
}
```

</details>

---
