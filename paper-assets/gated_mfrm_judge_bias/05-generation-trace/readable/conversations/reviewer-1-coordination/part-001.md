# Reviewer 1 coordination — Part 1 of 2

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Conversation logs

[Transcript overview](../reviewer-1-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/44/4438b2647bdef2856ed1.json)

## Round 1

## Round 1

42 recorded events


### User

_source line 1 · 2026-05-21T21:25:26.912797+00:00_

[Round 1 审稿请求]:
## Review Assignment: R1 — Methods & Experiments

You are reviewing an anonymous EMNLP 2026 submission: **"G-MFRM: Joint Estimation of Judge Bias and Benchmark Contamination for Fair LLM Evaluation"**

**Your focus: Methods (Soundness) and Experiments (Empirical rigor)**

### Paper summary (for context)
The paper identifies an omitted variable bias problem when judge bias and benchmark contamination are corrected sequentially in LLM-as-a-judge evaluation. It proposes G-MFRM (Gated Many-Facet Rasch Model), a unified psychometric framework that jointly estimates model ability, item difficulty, judge severity, and per-model contamination susceptibility. Three-stage estimation: (1) standard MFRM for initialization, (2) exposure indicator construction via ConStat + temporal + LogProber, (3) joint Bayesian estimation via NumPyro MCMC. Evaluated on MT-Bench (80 items), Arena-Hard (500 items), and WildBench (1024 items) with 8 LLM judges and 22 target models (203,520 evaluations).

### Your review dimensions

**A. Soundness of the formal framework (Section 2–3)**
1. Proposition 1 claims sequential estimators are asymptotically biased under non-orthogonality. Is the formalization rigorous? Is the bias expression (Cov(d_j, c_n·e_i)/Var(d_j)·d_j) correct and well-derived? Note: no proof is provided in the paper — only Monte Carlo validation (Table 1). Is this sufficient for an EMNLP paper?
2. The rank-1 contamination structure c_n·e_i: is this justified? 18% misfit rate for c_n (Table 5, outfit mean 1.15) — is this acceptable or a red flag?
3. Identifiability: treating e_i as fixed from Stage 2 while estimating c_n in Stage 3 — does this break the joint estimation claim? Is it truly "joint" if e_i is pre-fixed?
4. The half-normal prior on c_n ≥ 0: is the non-negativity assumption always valid? Could adversarial contamination deflate scores?

**B. Experimental rigor (Sections 4–5)**
1. Convergence: R̂_max = 1.06, 8% params with R̂ > 1.05, ESS_min = 120, 12 divergent transitions. Is this adequate for a Bayesian model of this complexity?
2. Main results (Table 6): Δτ = 0.02 on both benchmarks. MT-Bench p=0.008, Arena-Hard p=0.041. Are these gains meaningful or within noise? Is Wilcoxon appropriate here?
3. WildBench (Table 8): Δτ = 0.01, p = 0.062 — not significant. Paper frames this as "graceful degradation." Is this spin or legitimate framing?
4. Judge count sensitivity (Table 9): requires ≥4 judges. How limiting is this for practical adoption?
5. Exposure indicator ablation (Table 10): ConStat dominates at 58%. Is the framework too dependent on a single signal?
6. Adversarial robustness (Table 11): paraphrase attack detection at 45%, FPR 12%. Are these adequately discussed?
7. Missing experiment: no synthetic data validation with known ground-truth contamination levels. The paper references MVP-001 and MVP-003 scenarios (Table 7) but only compares distributions — no controlled experiment where true c_n is known.
8. All citations show as [?] — broken references throughout. Is this a formatting error or missing bibliography?

**C. Evaluation against the imagined experiment list**
The review context specifies 11 experiments (exp-001 through exp-011). Check coverage:
- exp-001 (data collection): covered in Section 4.1 + Table 2 ✓
- exp-002 (ConStat exposure): covered in Section 4.2 + Table 3 ✓
- exp-003 (G-MFRM fit): covered in Section 5.1 + Tables 4,5 ✓
- exp-004 (baseline comparison): covered in Section 5.2 + Table 6 ✓
- exp-005 (contamination calibration): covered in Section 5.3 + Table 7 ✓
- exp-006 (judge count sensitivity): covered in Section 5.5 + Table 9 ✓
- exp-007 (exposure ablation): covered in Section 5.6 + Table 10 ✓
- exp-008 (facet fit): covered in Section 5.1 + Table 5 ✓
- exp-009 (formal proposition MC): covered in Section 2.4 + Table 1 ✓
- exp-010 (WildBench replication): covered in Section 5.4 + Table 8 ✓
- exp-011 (adversarial robustness): covered in Section 5.7 + Table 11 ✓
All 11 experiments are present. Note whether any are underreported or missing key details from the context YAML (e.g., figures described in YAML but not in the paper).

### Scoring guidance (EMNLP 2026 ARR scale)
- Soundness: 1-5
- Excitement: 1-5
- Reproducibility: 1-5
- Overall: 5=Award, 4=Main conf, 3=Findings, 2=Major revision, 1=Do not resubmit

Provide your independent assessment with specific strengths, weaknesses, and questions for authors. Be calibrated: ~21% acceptance rate for Main, so a score of 4 should reflect genuine top-quintile quality.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-21T21:25:35.902608+00:00_

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
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
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

_source line 3 · 2026-05-21T21:25:35.953259+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-21T21:25:43.430104+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 5 · 2026-05-21T21:25:43.530911+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR reviewer form soundness excitement reproducibility scoring rubric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR reviewer form soundness excitement reproducibility scoring rubric"
  }
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-21T21:25:43.682357+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-21T21:25:43.733061+00:00_

/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/paper.pdf
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/median/paper.pdf
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/worst/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 8 · 2026-05-21T21:25:49.911339+00:00_

Web search results for query: "EMNLP 2026 ARR reviewer form soundness excitement reproducibility scoring rubric"

Links: [{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"},{"title":"Development and Validation of a Scoring Rubric for Editorial Evaluation of Peer-review Quality: A Pilot Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11000557/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Beyond Paper-to-Paper: Structured Profiling and Rubric Scoring for Paper-Reviewer Matching","url":"https://arxiv.org/pdf/2604.05866"}]

Based on the search results, I found relevant information about the ARR reviewer scoring system:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

Regarding the scoring rubric details:

- **Soundness**: The soundness scores must be justified by the text of the review. Low reproducibility scores should be justified.

- **Excitement**: Sometimes reviewers may find the work sound, but not something that is interesting for them personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

- **Overall Assessment**: The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, ex
…[truncated 497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6380
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-21T21:25:51.581845+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found regarding ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Scoring Criteria

The Overall as
…[truncated 1168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8151
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-21T21:25:57.464989+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and the exact descriptions for each score level. Include: Soundness, Excitement, Overall Assessment, Reproducibility, Confidence, and any other scored dimensions. I need the exact text of each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and the exact descriptions for each score level. Include: Soundness, Excitement, Overall Assessment, Reproducibility, Confidence, and any other scored dimensions. I need the exact text of each score level."
  }
}
```

</details>

---


### Tool call

_source line 11 · 2026-05-21T21:25:59.773035+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what constitutes a sound paper, how to score soundness (1-5), how to score excitement (1-5), reproducibility scoring, overall assessment scoring (1-5 scale with 0.5 increments), and any specific instructions about what reviewers should evaluate. Include the exact definitions for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what constitutes a sound paper, how to score soundness (1-5), how to score excitement (1-5), reproducibility scoring, overall assessment scoring (1-5 scale with 0.5 increments), and any specific instructions about what reviewers should evaluate. Include the exact definitions for each score level."
  }
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-21T21:26:00.578131+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/paper.pdf",
  "project": "gated_mfrm_judge_bias",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/paper.pdf",
    "project": "gated_mfrm_judge_bias",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-21T21:26:03.744642+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure. I tried to check the important points carefully"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand"

## Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me"
- **1**: "Not Exciting: this paper does not resonate with me"

## Overall Assessment
- **5**: "Consider for Award: top 2.5% papers"
- **4**: "Conference: could be accepted to an *ACL conference"
- **3**: "Findings: could be accepted to the Findings of the ACL"
- **2**: "Resubmit next cycle: needs substantial revisions"
- **1**: "Do not resubmit: has to be fully redone"

## Reproducibility
- **5**: "They could easily reproduce the results"
- **4**: "They could mostly reproduce the results"
- **3**: "They could reproduce the results with some difficulty"
- **2**: "They would be hard pressed to reproduce the results"
- **1**: "They would not be able to reproduce the results"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6279
}
```

</details>

---


### Tool result

_source line 14 · 2026-05-21T21:26:06.607261+00:00_

# ARR Reviewer Guidelines: Scoring and Evaluation Standards

## Sound Paper Definition

The guidelines emphasize that papers should be "technically sound and appropriately scoped." Soundness encompasses methodological rigor, valid argumentation, and legitimate contributions within the field's scope.

## Soundness Scoring

The guidelines state: "The soundness scores must be justified by the text of the review." Low soundness ratings require explicit justification in your written feedback. Reviews giving low scores without identifying major faults indicate misalignment between assessment and recommendation.

**Specific scoring criteria aren't numerically defined** in these guidelines. Instead, reviewers assess whether papers demonstrate:
- Technical validity and proper methodology
- Clear research questions and appropriate scoping
- Sufficient evidence supporting claims
- Reproducible experiments with adequate detail

## Excitement Scoring

Excitement is explicitly separated from soundness: "you may find the work sound, but not something that is interesting for you personally." This orthogonal dimension captures subjective preferences and personal research interests, distinct from objective quality assessment.

## Reproducibility Assessment

Reviewers evaluate whether "enough details to reproduce the experiments" are provided, including hyperparameter selection and code/data availability plans. This focuses on *reproducibility* (running experiments with similar results) rather than *replicability*.

## Overall Assessment

The composite score reflects "soundness, excitement, and also other factors like novelty and impact." Papers can merit acceptance despite low personal excitement if they demonstrate significant contributions to target communities through efficiency improvements or resource creation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6834
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-21T21:26:07.761916+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 353.7}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 296.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 249.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 340.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 288.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 231.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 287.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 269.8}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/a
…[truncated 617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7183
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-21T21:26:12.080000+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-21T21:26:12.886105+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-21T21:26:12.936713+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-21T21:26:13.390483+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-21T21:26:13.390913+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 21 · 2026-05-21T21:26:13.895594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 22 · 2026-05-21T21:26:14.800626+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-21T21:26:14.808670+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 913
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-21T21:26:14.809114+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-21T21:26:15.265723+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-21T21:26:15.266174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-21T21:26:15.719031+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-21T21:26:15.719725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-21T21:26:16.677108+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-21T21:26:16.677595+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-21T21:26:17.131238+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-21T21:26:17.133869+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-21T21:26:17.687222+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-21T21:26:17.737824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images/paper_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-21T21:26:17.788923+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-21T21:34:00.271947+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.0 — Findings（可被 Findings 接收，但当前状态不足以进入主会议）\n**一句话总结**: 问题动机好、实验覆盖全面，但\"联合估计\"核心 claim 被高估（e_i 在 Stage 2 预固定），Proposition 1 无形式化证明，且缺少已知 ground-truth 的合成验证实验。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要方法论思路合理，gating mechanism 设计优雅。但 Proposition 1 只有 MC 验证无证明，\"joint estimation\"实为条件估计（e_i 预固定），rank-1 contamination 假设有 ~18% misfit |\n| Excitement | 3/5 | 问题真实重要（omitted variable bias in LLM-as-judge），心理测量框架应用有创意。但相对最强 baseline（UDBA）提升仅 Δτ ≈ 0.01，需 ≥4 judges 限制实用性 |\n| Reproducibility | 3/5 | MCMC 配置详细（Section 4.3），benchmark 细节充分。但未提及代码发布，参考文献极少（~10 篇）导致 baseline 实现难以定位，exposure pipeline（ConStat + LogProber）细节不完整 |\n| Confidence | 4/5 | 仔细阅读全文，逐项核实技术细节和数字 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"Joint Estimation\"核心 claim 被高估\n- 具体位置：标题、Section 3.2 Three-Stage Estimation Pipeline\n- 问题：论文标题声称\"Joint Estimation of Judge Bias and Benchmark Contamination\"，但实际上 e_i（item exposure indicator）在 Stage 2 通过外部锚定（ConStat + temporal + LogProber）预先固定，Stage 3 的 Bayesian 估计只是在**给定固定 e_i 的条件下**联合估计 {θ, δ, d, c}。Section 3.2 明确承认：\"without knowing which items are exposed, the model cannot distinguish contamination-induced score inflation from genuine ability. We resolve this through a three-stage pipeline.\" 这说明 e_i 的不确定性没有传播到后验分布中。\n- 为什么影响接收：这直接关系到 paper 的 primary contribution claim。如果 e_i 是预固定的而非联合估计的，那么方法的本质是\"conditional estimation given pre-estimated exposure\"，而非真正的 joint estimation。这是 framing 层面的失准，会影响 reviewer 和读者对贡献的评估。\n- 建议修改方向：(1) 诚实重新表述为\"conditional joint estimation\"或\"staged joint estimation\"，明确说明 e_i 是外部锚定的；(2) 讨论 e_i 估计误差的传播——如果 Stage 2 的 e_i 不准确，Stage 3 的 c_n 估计会如何偏差；(3) 或者引入 e_i 的后验不确定性（如将 e_i 作为 Bernoulli 潜变量联合采样），使\"joint\"名副其实。\n\n**N2** [critical] Proposition 1 缺乏形式化证明\n- 具体位置：Section 2.2（page 2）\n- 问题：论文将 sequential estimation bias 的结果冠以\"Proposition 1\"，但仅提供 Monte Carlo 验证（Table 1，R² = 0.94，97.8% 方向正确率），没有任何形式化证明或证明概述。在数学写作中，\"Proposition\"意味着有逻辑推导，而非模拟验证。R² = 0.94 意味着 6% 的方差未被解释——first-order approximation 的适用范围未被界定。\n- 为什么影响接收：对于一篇以方法论为核心贡献的论文，理论基础应该更严格。MC 验证是支持性证据，但不能替代证明。如果 bias expression 在某些参数区域不成立（6% 未解释方差），整个 framework 的理论动机就被削弱。\n- 建议修改方向：(1) 在 appendix 中提供基于 omitted variable bias 定理的完整推导（从标准心理测量 MFRM 的 conditional maximum likelihood 出发，推导 non-orthogonality 条件下的渐近偏差）；(2) 如果无法严格证明，降级为\"Conjecture\"或\"Empirical Observation\"并明确说明近似的局限性。\n\n**N3** [critical] 缺少已知 ground-truth contamination 的合成验证实验\n- 具体位置：Section 5.3（Table 4）仅做分布层面比较\n- 问题：论文在 Table 4 中比较了真实 c_n 分布与合成场景的分布（KS test p = 0.41 for matched scenario），但从未验证**点估计**的准确性。没有任何实验设置已知的 true c_n 值，然后检验模型能否恢复这些值。这是 contamination estimation 声称最直接的验证方式，但完全缺失。\n- 为什么影响接收：如果我们不知道模型是否能准确估计每个 model 的 contamination susceptibility（而不只是分布形状匹配），就无法评估 Section 5.2（Table 3）中报告的 per-model contamination 估计是否可信。Table 3 说\"GPT-5.5 c_n = 1.65, DeepSeek-V4-Pro c_n = 1.52\"——但这些数字有多准？\n- 建议修改方向：从 G-MFRM 生成模型出发，设定已知的 {θ_n, c_n, e_i, d_j} 参数生成模拟数据，运行完整的三阶段估计 pipeline，报告：(a) 估计 c_n 与 true c_n 的 Pearson/Spearman 相关；(b) RMSE；(c) 在不同 contamination 强度下的恢复质量。\n\n**N4** [critical] 参考文献极度稀疏\n- 具体位置：References（pages 9-10），仅约 10 篇引用\n- 问题：一篇跨 judge bias、benchmark contamination、心理测量和 Bayesian estimation 四个领域的论文，仅引用约 10 篇文献。明显缺失的关键引用包括：\n  - IRT 基础文献：Rasch (1960), Lord & Novick (1968)\n  - LLM contamination检测：Golchin & Surdeanu (2023 min-k%), Shi et al. (2023 detecting pretraining data)\n  - Bayesian IRT：Albert (1992), Fox (2010)\n  - LLM judge bias：Bai et al. (2024 self-preference), Panickssery et al. (2024 verbosity bias)\n  - 更多 LLM evaluation 框架：AlpacaEval, WildBench 原始论文\n- 为什么影响接收：Related Work section（Section 6）因引用不足而无法充分定位本文贡献。Reviewer 无法判断作者是否了解领域全貌。这在 EMNLP review 中会被严重扣分。\n- 建议修改方向：至少扩充至 30-40 篇引用，覆盖上述各个领域。特别注意 IRT 经典文献（本文的方法论基础）和 LLM contamination detection 近期进展。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 收敛诊断不完整——未报告 divergent transitions\n- 具体位置：Section 5.4, Table 5\n- 问题：Table 5 报告了 R̂ 和 ESS（R̂ ≤ 1.02, ESS ≥ 312），这些数值本身可接受。但 NumPyro/NUTS 的标准诊断还包括：(a) divergent transitions 数量——这是 HMC 后验几何问题的关键指标；(b) E-BFMI；(c) posterior predictive checks。论文完全未提及 divergent transitions，如果存在，后验样本可能不可信。\n- 建议：报告 divergent transition 数量（应为 0 或极少），加入至少一个 posterior predictive check。\n\n**W2** [warning] 需 ≥4 judges 限制实用性\n- 具体位置：Section 5.5, Table 6\n- 问题：Table 6 显示 G-MFRM 在 J=2 时提升不显著，需 J≥4 才有显著改善（p = 0.005）。当前 LLM 评估实践中，多数 benchmark 使用 1-3 个 judge（AlpacaEval 用 1 个，许多用 GPT-4 单独评分）。这严重限制了方法的实际采纳。\n- 建议：在 Limitations 中更显著地讨论这一约束，并探讨 low-judge 场景下的降级策略（如在 J<4 时 fallback 到带先验正则化的简化模型）。\n\n**W3** [warning] 对 ConStat 的过度依赖\n- 具体位置：Section 5.6, Table 7\n- 问题：Table 7 ablation 显示 ConStat 是主导信号——论文承认\"ConStat is the most important single indicator (marginal contribution: ~0.03)\"且\"ConStat alone (τ = 0.90) nearly matches the full composite (τ = 0.91)\"。虽然即使去掉 ConStat，G-MFRM（τ = 0.89）仍优于 UDBA（τ = 0.86），但 ConStat 主导地位意味着如果 ConStat 信号不可用（例如无法获取原始 benchmark items 进行语义比较），框架效果将受限。\n- 建议：讨论 ConStat 不可用时的替代方案，以及 temporal 和 LogProber 信号单独使用时的局限性。\n\n**W4** [warning] c_n ≥ 0 非负性假设不覆盖对抗性场景\n- 具体位置：Section 3.1, prior: c_n ~ Half-Cauchy(0, 1)\n- 问题：Half-Cauchy 先验强制 c_n ≥ 0，假设 contamination 总是导致分数膨胀。这在典型 benchmark contamination（记忆→高分）下合理，但不覆盖：(a) adversarial contamination：故意在 benchmark items 上表现差以逃避检测；(b) data corruption：训练数据质量问题导致特定 items 分数下降。\n- 建议：至少在 Limitations 中讨论非负性假设的适用范围，或考虑使用 regularized normal prior 允许负值 contamination。\n\n**W5** [warning] Rank-1 contamination 结构的局限性\n- 具体位置：Section 3.1（c_n · e_i 结构）, Section 5.7 facet fit\n- 问题：Section 5.7 报告 contamination facet c 的 misfit rate 最高（约 2/22 models），归因于\"rank-1 assumption being an imperfect approximation for models with heterogeneous contamination patterns across items\"。如果某模型在 coding tasks 上被 contaminated 但在 reasoning tasks 上没有，rank-1 分解 c_n · e_i 无法捕捉这种异质性。\n- 建议：讨论 rank-k 分解（如 c_n · e_i → Σ_k c_{nk} · e_{ik}）的可能性，或至少定量评估 rank-1 misfit 对下游 ranking 的影响。\n\n**W6** [warning] 全文零图表\n- 具体位置：全文（pages 1-10）\n- 问题：整篇论文没有任何 figure——没有 framework overview、没有 contamination estimates 可视化、没有 convergence diagnostic plots、没有 estimated vs. baseline ability scatter plot。对于一篇 8 页的 EMNLP 论文，这在展示效果上是明显的缺陷。12 个 tables 但 0 个 figures 导致论文读起来非常密集，缺乏直观的 visual narrative。\n- 建议：至少加入：(1) Figure 1: G-MFRM framework overview（三阶段 pipeline 示意图）；(2) Figure 2: 估计的 c_n 分布可视化或 ability correction scatter plot；(3) Figure 3: 收敛诊断 trace plot。\n\n**W7** [warning] 正文疑似超 8 页限制\n- 具体位置：Sections 1-7 跨 pages 1 至 page 9 上半部分\n- 问题：EMNLP 2026 long paper 正文限 8 页（Limitations 和 References 不计入）。Section 6 (Related Work) 在 page 8 结束，Section 7 (Conclusion) 完整位于 page 9 上方，正文约 8.3 页。Conclusion 是正文的一部分（不是 Limitations），因此超出页数限制。\n- 建议：压缩 Related Work 或 Experimental sections，将 Conclusion 控制在 page 8 以内。\n\n**W8** [warning] 评估总数微小不一致\n- 具体位置：Abstract vs. Section 4.1\n- 问题：Abstract 称\"203,520 evaluations\"，但按 Section 4.1 的数据（8 judges × 22 models × (80+500) items × 2 position swap = 204,160），差额 640 未解释。推测为 API 失败导致的缺失（Section 4.1 提到 1.8% missing rate），但应明确说明。\n- 建议：统一数字，或注明实际收集数量与计划数量的差异。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 4.1 的 inter-judge Fleiss κ = 0.41（moderate agreement）：虽然在可接受范围内，但较低的 κ 值暗示 judges 可能评估不同维度，这对 MFRM 的单维性假设提出质疑。建议简要讨论。\n- Table 2 中 UDBA τ = 0.90 vs. G-MFRM τ = 0.91，但论文报告 95% CI of Δ: [0.02, 0.05]——如果 Δ 的 CI 下界是 0.02，point estimate 应 ≥ 0.02 而非显示为 0.01（0.91 - 0.90）。推测是四舍五入导致的歧义，建议报告至小数点后三位以消除混淆。\n- Limitations section（page 9）比较简短——覆盖了 rank-1 假设、Stage 2 dependence、MCMC 运行时间，但未提及 ≥4 judges 要求和 ConStat 依赖。\n\n---\n\n## 主要优势\n\n1. **问题动机真实且重要**：识别了 judge bias 和 benchmark contamination 顺序校正中的 omitted variable bias 问题——这是 LLM evaluation 领域的一个真实且被忽略的缺陷。Proposition 1 的 insight（即使没有形式化证明）是有价值的。\n\n2. **心理测量框架应用有创意**：将 MFRM（Many-Facet Rasch Model）扩展为带 gating mechanism 的 contamination-aware 模型，是将教育测量理论引入 LLM evaluation 的有价值尝试。Gating mechanism 设计优雅——当 e_i = 0 时退化为标准 MFRM。\n\n3. **实验覆盖全面**：11 个实验（exp-001 至 exp-011）全部到位，涵盖 main comparison、ablation、sensitivity、cross-benchmark replication、adversarial robustness 等多个维度。三个 benchmarks（MT-Bench, Arena-Hard, WildBench）、22 个 target models、8 个 LLM judges 的评估规模令人信服。\n\n4. **结果一致性好**：G-MFRM 在三个 benchmarks 上均优于所有 baselines，且跨 benchmark 的 c_n rank correlation（r = 0.62）显示 contamination susceptibility 是稳定的 model 属性。\n\n5. **实用价值**：提供可解释的 per-model contamination estimates（Table 3），可作为 post-hoc audit tool（AUC = 0.84）——这对 benchmark 维护者和模型评估者有直接价值。\n\n---\n\n## 对 Director 指定审查维度的逐项回应\n\n**A1（Proposition 1 严格性）**：MC 验证 R² = 0.94 是支持性证据但非证明。对 EMNLP 而言 MC 验证比数学会议可接受度更高，但冠以\"Proposition\"名号仍不恰当。建议降级表述或补充证明。\n\n**A2（Rank-1 结构 + 18% misfit）**：可接受但非最优。实验结果的一致性表明 rank-1 在当前设置下足够好，但 misfit 表明存在改进空间。不是 red flag，但是 yellow flag。\n\n**A3（e_i 预固定 vs. joint estimation claim）**：**这是本文最大的 framing 问题。** 明确破坏了\"joint estimation\"的 claim。详见 N1。\n\n**A4（Half-Cauchy 非负先验）**：假设合理但有限，见 W4。对当前实验设置影响不大，但限制了方法的通用性。\n\n**B1（收敛诊断）**：报告的 R̂ ≤ 1.02, ESS ≥ 312 可接受。但缺失 divergent transitions 报告是标准诊断的空白，见 W1。与 Director 提供的\"R̂_max = 1.06, ESS_min = 120, 12 divergent transitions\"不一致——**论文中我看到的数字更好**（R̂ ≤ 1.02, ESS ≥ 312）。以论文实际报告为准。\n\n**B2（Main results 显著性）**：Δτ = 0.01 over UDBA 虽小但 CI [0.02, 0.05] 和 p < 2×10⁻³ 显示统计显著。Wilcoxon 用于配对排名比较是合适的。实际意义方面：Δτ = 0.01-0.05 在 Kendall τ 量级上是 modest 的。\n\n**B3（WildBench 结果）**：论文报告 τ = 0.89, p = 2.1×10⁻⁴ vs. sequential——这是显著且强的结果，与 Director 提供的\"p = 0.062 不显著\"不一致。**以论文实际报告为准**——WildBench 上的结果是显著的。\n\n**B4（Judge count 限制）**：≥4 judges 要求确实限制实用性，见 W2。\n\n**B5（ConStat 主导）**：ConStat 占比大，但去掉后仍优于 baselines（τ = 0.89 > UDBA 0.86），见 W3。\n\n**B6（Adversarial robustness）**：AUC = 0.84 at 20% injection 是 decent。论文报告 robustness ratio ~3.7×。未看到 Director 提到的\"paraphrase attack detection at 45%, FPR 12%\"——Table 10 只有 controlled injection 实验。\n\n**B7（Missing synthetic ground-truth）**：确认缺失，详见 N3。这是最重要的实验缺口。\n\n**B8（Broken references [?]）**：**论文中未观察到 broken [?] citations。** 所有可见的 in-text citations（如 [Zheng et al., 2023], [Lin et al., 2025] 等）均正确解析到 bibliography。但 bibliography 极度稀疏（~10 篇），详见 N4。\n\n**C（实验覆盖）**：11 个实验全部在论文中出现。但注意：(1) 全文零图表（Director 的 experiment YAML 可能描述了 figures，但论文中没有）；(2) exp-005（contamination calibration）只做分布比较，缺少点估计验证。",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.0 — Findings（可被 Findings 接收，但当前状态不足以进入主会议）\n**一句话总结**: 问题动机好、实验覆盖全面，但\"联合估计\"核心 claim 被高估（e_i 在 Stage 2 预固定），Proposition 1 无形式化证明，且缺少已知 ground-truth 的合成验证实验。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要方法论思路合理，gating mechanism 设计优雅。但 Proposition 1 只有 MC 验证无证明，\"joint estimation\"实为条件估计（e_i 预固定），rank-1 contamination 假设有 ~18% misfit |\n| Excitement | 3/5 | 问题真实重要（omitted variable bias in LLM-as-judge），心理测量框架应用有创意。但相对最强 baseline（UDBA）提升仅 Δτ ≈ 0.01，需 ≥4 judges 限制实用性 |\n| Reproducibility | 3/5 | MCMC 配置详细（Section 4.3），benchmark 细节充分。但未提及代码发布，参考文献极少（~10 篇）导致 baseline 实现难以定位，exposure pipeline（ConStat + LogProber）细节不完整 |\n| Confidence | 4/5 | 仔细阅读全文，逐项核实技术细节和数字 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"Joint Estimation\"核心 claim 被高估\n- 具体位置：标题、Section 3.2 Three-Stage Estimation Pipeline\n- 问题：论文标题声称\"Joint Estimation of Judge Bias and Benchmark Contamination\"，但实际上 e_i（item exposure indicator）在 Stage 2 通过外部锚定（ConStat + temporal + LogProber）预先固定，Stage 3 的 Bayesian 估计只是在**给定固定 e_i 的条件下**联合估计 {θ, δ, d, c}。Section 3.2 明确承认：\"without knowing which items are exposed, the model cannot distinguish contamination-induced score inflation from genuine ability. We resolve this through a three-stage pipeline.\" 这说明 e_i 的不确定性没有传播到后验分布中。\n- 为什么影响接收：这直接关系到 paper 的 primary contribution claim。如果 e_i 是预固定的而非联合估计的，那么方法的本质是\"conditional estimation given pre-estimated exposure\"，而非真正的 joint estimation。这是 framing 层面的失准，会影响 reviewer 和读者对贡献的评估。\n- 建议修改方向：(1) 诚实重新表述为\"conditional joint estimation\"或\"staged joint estimation\"，明确说明 e_i 是外部锚定的；(2) 讨论 e_i 估计误差的传播——如果 Stage 2 的 e_i 不准确，Stage 3 的 c_n 估计会如何偏差；(3) 或者引入 e_i 的后验不确定性（如将 e_i 作为 Bernoulli 潜变量联合采样），使\"joint\"名副其实。\n\n**N2** [critical] Proposition 1 缺乏形式化证明\n- 具体位置：Section 2.2（page 2）\n- 问题：论文将 sequential estimation bias 的结果冠以\"Proposition 1\"，但仅提供 Monte Carlo 验证（Table 1，R² = 0.94，97.8% 方向正确率），没有任何形式化证明或证明概述。在数学写作中，\"Proposition\"意味着有逻辑推导，而非模拟验证。R² = 0.94 意味着 6% 的方差未被解释——first-order approximation 的适用范围未被界定。\n- 为什么影响接收：对于一篇以方法论为核心贡献的论文，理论基础应该更严格。MC 验证是支持性证据，但不能替代证明。如果 bias expression 在某些参数区域不成立（6% 未解释方差），整个 framework 的理论动机就被削弱。\n- 建议修改方向：(1) 在 appendix 中提供基于 omitted variable bias 定理的完整推导（从标准心理测量 MFRM 的 conditional maximum likelihood 出发，推导 non-orthogonality 条件下的渐近偏差）；(2) 如果无法严格证明，降级为\"Conjecture\"或\"Empirical Observation\"并明确说明近似的局限性。\n\n**N3** [critical] 缺少已知 ground-truth contamination 的合成验证实验\n- 具体位置：Section 5.3（Table 4）仅做分布层面比较\n- 问题：论文在 Table 4 中比较了真实 c_n 分布与合成场景的分布（KS test p = 0.41 for matched scenario），但从未验证**点估计**的准确性。没有任何实验设置已知的 true c_n 值，然后检验模型能否恢复这些值。这是 contamination estimation 声称最直接的验证方式，但完全缺失。\n- 为什么影响接收：如果我们不知道模型是否能准确估计每个 model 的 contamination susceptibility（而不只是分布形状匹配），就无法评估 Section 5.2（Table 3）中报告的 per-model contamination 估计是否可信。Table 3 说\"GPT-5.5 c_n = 1.65, DeepSeek-V4-Pro c_n = 1.52\"——但这些数字有多准？\n- 建议修改方向：从 G-MFRM 生成模型出发，设定已知的 {θ_n, c_n, e_i, d_j} 参数生成模拟数据，运行完整的三阶段估计 pipeline，报告：(a) 估计 c_n 与 true c_n 的 Pearson/Spearman 相关；(b) RMSE；(c) 在不同 contamination 强度下的恢复质量。\n\n**N4** [critical] 参考文献极度稀疏\n- 具体位置：References（pages 9-10），仅约 10 篇引用\n- 问题：一篇跨 judge bias、benchmark contamination、心理测量和 Bayesian estimation 四个领域的论文，仅引用约 10 篇文献。明显缺失的关键引用包括：\n  - IRT 基础文献：Rasch (1960), Lord & Novick (1968)\n  - LLM contamination检测：Golchin & Surdeanu (2023 min-k%), Shi et al. (2023 detecting pretraining data)\n  - Bayesian IRT：Albert (1992), Fox (2010)\n  - LLM judge bias：Bai et al. (2024 self-preference), Panickssery et al. (2024 verbosity bias)\n  - 更多 LLM evaluation 框架：AlpacaEval, WildBench 原始论文\n- 为什么影响接收：Related Work section（Section 6）因引用不足而无法充分定位本文贡献。Reviewer 无法判断作者是否了解领域全貌。这在 EMNLP review 中会被严重扣分。\n- 建议修改方向：至少扩充至 30-40 篇引用，覆盖上述各个领域。特别注意 IRT 经典文献（本文的方法论基础）和 LLM contamination detection 近期进展。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 收敛诊断不完整——未报告 divergent transitions\n- 具体位置：Section 5.4, Table 5\n- 问题：Table 5 报告了 R̂ 和 ESS（R̂ ≤ 1.02, ESS ≥ 312），这些数值本身可接受。但 NumPyro/NUTS 的标准诊断还包括：(a) divergent transitions 数量——这是 HMC 后验几何问题的关键指标；(b) E-BFMI；(c) posterior predictive checks。论文完全未提及 divergent transitions，如果存在，后验样本可能不可信。\n- 建议：报告 divergent transition 数量（应为 0 或极少），加入至少一个 posterior predictive check。\n\n**W2** [warning] 需 ≥4 judges 限制实用性\n- 具体位置：Section 5.5, Table 6\n- 问题：Table 6 显示 G-MFRM 在 J=2 时提升不显著，需 J≥4 才有显著改善（p = 0.005）。当前 LLM 评估实践中，多数 benchmark 使用 1-3 个 judge（AlpacaEval 用 1 个，许多用 GPT-4 单独评分）。这严重限制了方法的实际采纳。\n- 建议：在 Limitations 中更显著地讨论这一约束，并探讨 low-judge 场景下的降级策略（如在 J<4 时 fallback 到带先验正则化的简化模型）。\n\n**W3** [warning] 对 ConStat 的过度依赖\n- 具体位置：Section 5.6, Table 7\n- 问题：Table 7 ablation 显示 ConStat 是主导信号——论文承认\"ConStat is the most important single indicator (marginal contribution: ~0.03)\"且\"ConStat alone (τ = 0.90) nearly matches the full composite (τ = 0.91)\"。虽然即使去掉 ConStat，G-MFRM（τ = 0.89）仍优于 UDBA（τ = 0.86），但 ConStat 主导地位意味着如果 ConStat 信号不可用（例如无法获取原始 benchmark items 进行语义比较），框架效果将受限。\n- 建议：讨论 ConStat 不可用时的替代方案，以及 temporal 和 LogProber 信号单独使用时的局限性。\n\n**W4** [warning] c_n ≥ 0 非负性假设不覆盖对抗性场景\n- 具体位置：Section 3.1, prior: c_n ~ Half-Cauchy(0, 1)\n- 问题：Half-Cauchy 先验强制 c_n ≥ 0，假设 contamination 总是导致分数膨胀。这在典型 benchmark contamination（记忆→高分）下合理，但不覆盖：(a) adversarial contamination：故意在 benchmark items 上表现差以逃避检测；(b) data corruption：训练数据质量问题导致特定 items 分数下降。\n- 建议：至少在 Limitations 中讨论非负性假设的适用范围，或考虑使用 regularized normal prior 允许负值 contamination。\n\n**W5** [warning] Rank-1 contamination 结构的局限性\n- 具体位置：Section 3.1（c_n · e_i 结构）, Section 5.7 facet fit\n- 问题：Section 5.7 报告 contamination facet c 的 misfit rate 最高（约 2/22 models），归因于\"rank-1 assumption being an imperfect approximation for models with heterogeneous contamination patterns across items\"。如果某模型在 coding tasks 上被 contaminated 但在 reasoning tasks 上没有，rank-1 分解 c_n · e_i 无法捕捉这种异质性。\n- 建议：讨论 rank-k 分解（如 c_n · e_i → Σ_k c_{nk} · e_{ik}）的可能性，或至少定量评估 rank-1 misfit 对下游 ranking 的影响。\n\n**W6** [warning] 全文零图表\n- 具体位置：全文（pages 1-10）\n- 问题：整篇论文没有任何 figure——没有 framework overview、没有 contamination estimates 可视化、没有 convergence diagnostic plots、没有 estimated vs. baseline ability scatter plot。对于一篇 8 页的 EMNLP 论文，这在展示效果上是明显的缺陷。12 个 tables 但 0 个 figures 导致论文读起来非常密集，缺乏直观的 visual narrative。\n- 建议：至少加入：(1) Figure 1: G-MFRM framework overview（三阶段 pipeline 示意图）；(2) Figure 2: 估计的 c_n 分布可视化或 ability correction scatter plot；(3) Figure 3: 收敛诊断 trace plot。\n\n**W7** [warning] 正文疑似超 8 页限制\n- 具体位置：Sections 1-7 跨 pages 1 至 page 9 上半部分\n- 问题：EMNLP 2026 long paper 正文限 8 页（Limitations 和 References 不计入）。Section 6 (Related Work) 在 page 8 结束，Section 7 (Conclusion) 完整位于 page 9 上方，正文约 8.3 页。Conclusion 是正文的一部分（不是 Limitations），因此超出页数限制。\n- 建议：压缩 Related Work 或 Experimental sections，将 Conclusion 控制在 page 8 以内。\n\n**W8** [warning] 评估总数微小不一致\n- 具体位置：Abstract vs. Section 4.1\n- 问题：Abstract 称\"203,520 evaluations\"，但按 Section 4.1 的数据（8 judges × 22 models × (80+500) items × 2 position swap = 204,160），差额 640 未解释。推测为 API 失败导致的缺失（Section 4.1 提到 1.8% missing rate），但应明确说明。\n- 建议：统一数字，或注明实际收集数量与计划数量的差异。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 4.1 的 inter-judge Fleiss κ = 0.41（moderate agreement）：虽然在可接受范围内，但较低的 κ 值暗示 judges 可能评估不同维度，这对 MFRM 的单维性假设提出质疑。建议简要讨论。\n- Table 2 中 UDBA τ = 0.90 vs. G-MFRM τ = 0.91，但论文报告 95% CI of Δ: [0.02, 0.05]——如果 Δ 的 CI 下界是 0.02，point estimate 应 ≥ 0.02 而非显示为 0.01（0.91 - 0.90）。推测是四舍五入导致的歧义，建议报告至小数点后三位以消除混淆。\n- Limitations section（page 9）比较简短——覆盖了 rank-1 假设、Stage 2 dependence、MCMC 运行时间，但未提及 ≥4 judges 要求和 ConStat 依赖。\n\n---\n\n## 主要优势\n\n1. **问题动机真实且重要**：识别了 judge bias 和 benchmark contamination 顺序校正中的 omitted variable bias 问题——这是 LLM evaluation 领域的一个真实且被忽略的缺陷。Proposition 1 的 insight（即使没有形式化证明）是有价值的。\n\n2. **心理测量框架应用有创意**：将 MFRM（Many-Facet Rasch Model）扩展为带 gating mechanism 的 contamination-aware 模型，是将教育测量理论引入 LLM evaluation 的有价值尝试。Gating mechanism 设计优雅——当 e_i = 0 时退化为标准 MFRM。\n\n3. **实验覆盖全面**：11 个实验（exp-001 至 exp-011）全部到位，涵盖 main comparison、ablation、sensitivity、cross-benchmark replication、adversarial robustness 等多个维度。三个 benchmarks（MT-Bench, Arena-Hard, WildBench）、22 个 target models、8 个 LLM judges 的评估规模令人信服。\n\n4. **结果一致性好**：G-MFRM 在三个 benchmarks 上均优于所有 baselines，且跨 benchmark 的 c_n rank correlation（r = 0.62）显示 contamination susceptibility 是稳定的 model 属性。\n\n5. **实用价值**：提供可解释的 per-model contamination estimates（Table 3），可作为 post-hoc audit tool（AUC = 0.84）——这对 benchmark 维护者和模型评估者有直接价值。\n\n---\n\n## 对 Director 指定审查维度的逐项回应\n\n**A1（Proposition 1 严格性）**：MC 验证 R² = 0.94 是支持性证据但非证明。对 EMNLP 而言 MC 验证比数学会议可接受度更高，但冠以\"Proposition\"名号仍不恰当。建议降级表述或补充证明。\n\n**A2（Rank-1 结构 + 18% misfit）**：可接受但非最优。实验结果的一致性表明 rank-1 在当前设置下足够好，但 misfit 表明存在改进空间。不是 red flag，但是 yellow flag。\n\n**A3（e_i 预固定 vs. joint estimation claim）**：**这是本文最大的 framing 问题。** 明确破坏了\"joint estimation\"的 claim。详见 N1。\n\n**A4（Half-Cauchy 非负先验）**：假设合理但有限，见 W4。对当前实验设置影响不大，但限制了方法的通用性。\n\n**B1（收敛诊断）**：报告的 R̂ ≤ 1.02, ESS ≥ 312 可接受。但缺失 divergent transitions 报告是标准诊断的空白，见 W1。与 Director 提供的\"R̂_max = 1.06, ESS_min = 120, 12 divergent transitions\"不一致——**论文中我看到的数字更好**（R̂ ≤ 1.02, ESS ≥ 312）。以论文实际报告为准。\n\n**B2（Main results 显著性）**：Δτ = 0.01 over UDBA 虽小但 CI [0.02, 0.05] 和 p < 2×10⁻³ 显示统计显著。Wilcoxon 用于配对排名比较是合适的。实际意义方面：Δτ = 0.01-0.05 在 Kendall τ 量级上是 modest 的。\n\n**B3（WildBench 结果）**：论文报告 τ = 0.89, p = 2.1×10⁻⁴ vs. sequential——这是显著且强的结果，与 Director 提供的\"p = 0.062 不显著\"不一致。**以论文实际报告为准**——WildBench 上的结果是显著的。\n\n**B4（Judge count 限制）**：≥4 judges 要求确实限制实用性，见 W2。\n\n**B5（ConStat 主导）**：ConStat 占比大，但去掉后仍优于 baselines（τ = 0.89 > UDBA 0.86），见 W3。\n\n**B6（Adversarial robustness）**：AUC = 0.84 at 20% injection 是 decent。论文报告 robustness ratio ~3.7×。未看到 Director 提到的\"paraphrase attack detection at 45%, FPR 12%\"——Table 10 只有 controlled injection 实验。\n\n**B7（Missing synthetic ground-truth）**：确认缺失，详见 N3。这是最重要的实验缺口。\n\n**B8（Broken references [?]）**：**论文中未观察到 broken [?] citations。** 所有可见的 in-text citations（如 [Zheng et al., 2023], [Lin et al., 2025] 等）均正确解析到 bibliography。但 bibliography 极度稀疏（~10 篇），详见 N4。\n\n**C（实验覆盖）**：11 个实验全部在论文中出现。但注意：(1) 全文零图表（Director 的 experiment YAML 可能描述了 figures，但论文中没有）；(2) exp-005（contamination calibration）只做分布比较，缺少点估计验证。",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-21T21:34:04.884877+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4612
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-21T21:34:09.353749+00:00_

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
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
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

_source line 39 · 2026-05-21T21:34:09.404367+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-21T21:34:13.475624+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-21T21:34:13.526200+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 42 · 2026-05-21T21:34:20.870775+00:00_

审稿完成，临时图片已清理。

总结：Overall 3.0（Findings 级别）。4 个 Must-Fix 问题：(1) "Joint Estimation" claim 被高估——e_i 在 Stage 2 预固定；(2) Proposition 1 无形式化证明；(3) 缺少已知 ground-truth 的合成 c_n 验证实验；(4) 参考文献仅约 10 篇，远低于 EMNLP 标准。8 个 Should-Fix 问题涵盖收敛诊断不完整、≥4 judges 实用性限制、ConStat 依赖、非负先验假设、全文零图表、正文超 8 页等。实验覆盖方面，11 个实验全部到位，三个 benchmark 结果一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 43 · 2026-05-21T21:39:25.394617+00:00_

[Round 1 审稿请求]:
[交叉分享 - Round 1] 以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## R2 审稿报告：Novelty, Related Work, Presentation Quality

**Overall: 2.5 (Borderline Findings)**

**一句话总结**: 问题识别有价值，方法技术上合理，但核心理论贡献是标准计量经济学结果的领域迁移，related work 严重不足（仅 10 篇引用），且提交格式完全不符合 ACL 模板要求（单栏、错误 margins），整体距离 Main conference 接收标准有明显差距。

## 官方维度打分（ACL ARR Review Form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | 理论正确但为标准 OVB 的直接应用；实验设计全面（7 baselines, ablations, cross-benchmark）；但 "first framework" claim 未充分排除心理计量学文献中已有的多 facet+DIF 联合建模工作 |
| Excitement | 2.5/5 | 问题重要（LLM 评估方法论是热点），但解决方案是已有技术（MFRM + DG-IRT gating）的组合迁移，效果提升有限（Δτ=0.05），pipeline 复杂度高（需 8 judges + ConStat + MCMC 3小时），限制了实际影响力 |
| Reproducibility | 2/5 | 无代码/数据发布计划，实验需 8 个 LLM judges（跨 4 厂商 API + vLLM），成本约 $780+105 GPU-hours，普通研究者难以复现 |
| Overall | 2.5 | 见下方详细分析 |

## Must-Fix 问题

**N1** [critical] 提交格式完全不符合 ACL/EMNLP 模板要求
- 论文使用 `\documentclass[11pt,a4paper]{article}` + `\usepackage[margin=1in]{geometry}`，产出单栏格式。EMNLP 2026 必须使用 ACL 官方模板（`acl.sty`，双栏格式）。

**N2** [critical] Related Work 严重不足——仅 10 篇引用，关键文献缺失
- 缺失：Arena-Hard 原始论文、WildBench 原始论文、Zhu et al. (2023) "Judging LLM-as-a-Judge"、教育测量学中 MFRM + DIF 联合建模文献、broader IRT-for-NLP 文献
- "first" novelty claim 未充分排除先验文献

**N3** [critical] 论文零图表——11 张 tables 但无任何 figures

## Should-Fix 问题

**W1** Proposition 1 的 novelty 被过度包装——标准 OVB 的直接应用
**W2** DG-IRT 适配的技术 novelty 需要更清晰差异化，缺 error propagation 分析
**W3** 效果量 Δτ=0.05 的实际排名意义未论证
**W4** Chatbot Arena Elo 作为 ground truth 的 circular reasoning 风险
**W5** 三阶段 pipeline 的 Stage 2→3 error propagation 未讨论，posterior uncertainty 可能 under-estimated

## Novelty 专项评估
- Novelty 排序：G-MFRM model > empirical evaluation > confounding formalization（最后一项 novelty 最低）
- "First framework" claim 限定在 "for LLM evaluation" 范围内可能成立，但未排除心理计量学先验文献

## 主要优势
1. 问题识别准确且有实际意义
2. 方法设计原则性强（基于 psychometric measurement theory）
3. 实验设计全面（8 baselines, judge count sensitivity, cross-benchmark replication, adversarial robustness）
4. 实用副产品（per-model c_n 估计，AUC=0.94）
5. Limitations section 诚实具体

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-21T21:41:03.460677+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 对 R2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 提交格式完全不符合 ACL/EMNLP 模板要求**\n同意。论文确实使用单栏格式而非 ACL 官方双栏模板（`acl.sty`）。我在审稿中注意到了页面布局异常但仅将其归类为 W7（正文超 8 页），R2 更准确地识别出根本原因——模板本身就不对。单栏格式导致页数计算、行距、margins 全部偏离 EMNLP 要求。这是 desk reject 级别的格式问题，但属于纯技术性修复，不影响论文内容质量的评判。\n\n**[AGREE] R2-N2: Related Work 严重不足（仅 10 篇引用）**\n完全同意，与我的 N4 一致。R2 进一步指出了我遗漏的缺失引用——Arena-Hard 原始论文和 WildBench 原始论文。论文在 Section 4.1 使用这两个 benchmark 作为核心评估数据集，却未引用其原始论文，这是严重疏忽。R2 提出的\"first framework claim 未充分排除心理计量学先验文献\"也是合理的——教育测量学中 MFRM + DIF（Differential Item Functioning）联合建模已有大量工作（如 Engelhard & Wind, 2018），论文需明确说明与这些先验工作的区别。\n\n**[AGREE] R2-N3: 论文零图表**\n同意，与我的 W6 一致。R2 将其升级为 Must-Fix 是合理的——对于 EMNLP 论文，完全没有 figures 在 presentation quality 维度上是严重缺陷。我在 W6 中建议了三个最重要的图（framework overview、c_n 分布可视化、convergence trace plots），赞同 R2 的判断。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Proposition 1 是标准 OVB 的直接应用，novelty 被过度包装**\n部分同意。R2 正确指出 Proposition 1 的数学内核是标准的 omitted variable bias 定理（Angrist & Pischke, 2009 中的经典结果）迁移到心理测量设置。论文在 Section 2.2 中也承认\"This follows from standard omitted variable bias analysis adapted to the psychometric setting.\" 但论文随后冠以\"Proposition\"名号并强调其作为贡献，这确实有过度包装之嫌。\n\n不过我认为 R2 的评估略微偏严：即使 formalization 本身不新，**将 OVB insight 具体化到 LLM-as-judge 的 {d_j, c_n·e_i} 非正交结构**，并通过 Table 1 的 MC 验证和 Section 2.4 的真实数据证据展示其实际影响（ρ = 0.37, RMSE 降级 28.5%），仍然对 LLM evaluation 社区有实际价值。建议降级表述（如\"Observation\"而非\"Proposition\"），但不应因此否定其应用贡献。\n\n**[AGREE] R2-W2: DG-IRT 适配需更清晰差异化 + 缺 error propagation 分析**\n同意，且与我的 N1 高度一致。R2 和我独立识别出了同一个核心问题：e_i 在 Stage 2 预固定，Stage 2→3 的误差传播未被分析。论文 Section 3.3 列出了 DG-IRT 的三个适配点（binary→continuous exposure, single-rater→multi-facet, known→unknown group membership），但未定量评估这些适配的影响。R2 进一步要求\"error propagation analysis\"——如果 Stage 2 的 e_i 估计有 10% 误差，c_n 的后验会如何偏移？这是合理且必要的分析。两位 reviewer 在这一点上高度一致，建议 Director 将其视为 consensus issue。\n\n**[AGREE] R2-W3: Δτ=0.05 的实际排名意义未论证**\n同意。论文报告 G-MFRM 相对 sequential pipeline 的提升为 Δτ ≈ 0.05-0.07（Table 2, Section 5.1），但从未回答关键问题：**这 0.05 的 Kendall τ 提升实际翻转了多少模型对的排名？** 对于 22 个模型（231 个 model pairs），Δτ = 0.05 大约对应 ~12 个 pair 的重排序。论文应报告：(a) 具体哪些模型对被重排序；(b) 重排序后与 Arena 排名的 concordant pair 数量变化。这会比抽象的 τ 值更有说服力。\n\n**[REBUT] R2-W4: Chatbot Arena Elo 作为 ground truth 的 circular reasoning 风险**\n不同意 R2 对此风险程度的评估。R2 的论点是：如果被 contaminated 的模型在 Arena 中也表现更好（因为类似的数据泄露），那么用 Arena 排名评估 decontamination 就有 circularity。但这一论点忽略了 Arena 的根本机制差异：\n\n- **Arena 使用真实用户的实时 pairwise 比较**，prompts 来自用户自发输入，不是固定 benchmark items。Benchmark contamination（记忆 MT-Bench/Arena-Hard 的特定 item）不会直接提升 Arena 对战中面对全新 prompt 的表现。\n- Section 5.8 的跨 benchmark 一致性验证（WildBench τ = 0.89, r(c_n) = 0.62 across benchmarks）从侧面佐证了 contamination 不是简单地与 Arena 排名共变。\n- 如果 Arena 排名自身被 contamination 污染，我们预期 decontamination 后的排名会**远离** Arena，而非更接近——但实验结果恰恰相反（τ 提升），这与 circularity 假设矛盾。\n\n当然，Arena 并非完美 ground truth（存在 recency bias、prompt distribution bias 等），论文可以加一段讨论其局限性。但 R2 所述的\"circular reasoning risk\"在方法论上不成立。\n\n**[AGREE] R2-W5: Stage 2→3 error propagation 未讨论，posterior uncertainty 可能被低估**\n同意，与我的 N1 和 R2-W2 一致。这是三位最终审稿意见中（如果算上我的 N1、R2 的 W2 和 W5）出现频率最高的问题。论文的 posterior intervals 只反映了 Stage 3 的采样不确定性，未纳入 Stage 2 的 e_i 估计不确定性。如果 e_i 的真实不确定性较大（例如 ConStat 的 sensitivity 为 0.58 according to Table 7 ablation），c_n 的 credible intervals 可能显著偏窄。\n\n---\n\n### Novelty 专项评估回应\n\nR2 将 novelty 排序为：G-MFRM model > empirical evaluation > confounding formalization。我基本同意这一排序，但会调整权重：\n\n- **G-MFRM model（主要 novelty）**：gating mechanism 的设计（将 DG-IRT 的 group membership 替换为 continuous exposure + rank-1 contamination）确实是本文最核心的技术贡献。但如我在 N1 中指出，\"joint estimation\"的 claim 被 e_i 预固定所削弱。\n- **Empirical evaluation（次要 novelty）**：实验规模和覆盖度是本文的优势，11 个实验全到位。\n- **Confounding formalization（最低 novelty）**：同意 R2 的判断——这是 OVB 的领域迁移。但\"最低 novelty ≠ 零 novelty\"，将通用定理具体化到特定领域的变量结构并提供实证验证仍有贡献。\n\nR2 提出\"first framework claim 需限定范围\"——我同意，建议 authors 改为\"the first framework **in the LLM evaluation literature** that jointly addresses...\"并引用教育测量学中的先验工作以示区别。\n\n---\n\n### 对 R2 总体评分的看法\n\nR2 给出 Overall 2.5（Borderline Findings），我给出 3.0（Findings）。差异主要来自两处：\n\n1. **格式问题权重**：R2 将格式违规（N1）作为 Must-Fix 影响总分，我认为这是严重但纯技术性的问题——模板转换不改变论文内容质量。如果剥离格式因素，R2 和我在 Soundness 上的评分一致（均为 3/5）。\n\n2. **Excitement 分歧**：R2 给 2.5（因 novelty 有限 + pipeline 复杂），我给 3（因问题动机真实重要）。我认为 R2 在 novelty 维度偏严——即使 formalization 是 OVB 迁移，完整的 G-MFRM framework + 大规模实证验证在 LLM evaluation 领域仍然是有价值的工作。\n\n**Consensus 问题（R1 和 R2 均认为 critical）**：\n1. e_i 预固定导致\"joint estimation\" claim 过度（R1-N1, R2-W2, R2-W5）\n2. 参考文献严重不足（R1-N4, R2-N2）\n3. 零图表（R1-W6, R2-N3）\n4. 格式不合规（R1-W7, R2-N1）\n\n这四个 consensus issues 中，前两个是内容问题（需要实质性修改），后两个是 presentation 问题（可快速修复）。",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 对 R2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 提交格式完全不符合 ACL/EMNLP 模板要求**\n同意。论文确实使用单栏格式而非 ACL 官方双栏模板（`acl.sty`）。我在审稿中注意到了页面布局异常但仅将其归类为 W7（正文超 8 页），R2 更准确地识别出根本原因——模板本身就不对。单栏格式导致页数计算、行距、margins 全部偏离 EMNLP 要求。这是 desk reject 级别的格式问题，但属于纯技术性修复，不影响论文内容质量的评判。\n\n**[AGREE] R2-N2: Related Work 严重不足（仅 10 篇引用）**\n完全同意，与我的 N4 一致。R2 进一步指出了我遗漏的缺失引用——Arena-Hard 原始论文和 WildBench 原始论文。论文在 Section 4.1 使用这两个 benchmark 作为核心评估数据集，却未引用其原始论文，这是严重疏忽。R2 提出的\"first framework claim 未充分排除心理计量学先验文献\"也是合理的——教育测量学中 MFRM + DIF（Differential Item Functioning）联合建模已有大量工作（如 Engelhard & Wind, 2018），论文需明确说明与这些先验工作的区别。\n\n**[AGREE] R2-N3: 论文零图表**\n同意，与我的 W6 一致。R2 将其升级为 Must-Fix 是合理的——对于 EMNLP 论文，完全没有 figures 在 presentation quality 维度上是严重缺陷。我在 W6 中建议了三个最重要的图（framework overview、c_n 分布可视化、convergence trace plots），赞同 R2 的判断。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Proposition 1 是标准 OVB 的直接应用，novelty 被过度包装**\n部分同意。R2 正确指出 Proposition 1 的数学内核是标准的 omitted variable bias 定理（Angrist & Pischke, 2009 中的经典结果）迁移到心理测量设置。论文在 Section 2.2 中也承认\"This follows from standard omitted variable bias analysis adapted to the psychometric setting.\" 但论文随后冠以\"Proposition\"名号并强调其作为贡献，这确实有过度包装之嫌。\n\n不过我认为 R2 的评估略微偏严：即使 formalization 本身不新，**将 OVB insight 具体化到 LLM-as-judge 的 {d_j, c_n·e_i} 非正交结构**，并通过 Table 1 的 MC 验证和 Section 2.4 的真实数据证据展示其实际影响（ρ = 0.37, RMSE 降级 28.5%），仍然对 LLM evaluation 社区有实际价值。建议降级表述（如\"Observation\"而非\"Proposition\"），但不应因此否定其应用贡献。\n\n**[AGREE] R2-W2: DG-IRT 适配需更清晰差异化 + 缺 error propagation 分析**\n同意，且与我的 N1 高度一致。R2 和我独立识别出了同一个核心问题：e_i 在 Stage 2 预固定，Stage 2→3 的误差传播未被分析。论文 Section 3.3 列出了 DG-IRT 的三个适配点（binary→continuous exposure, single-rater→multi-facet, known→unknown group membership），但未定量评估这些适配的影响。R2 进一步要求\"error propagation analysis\"——如果 Stage 2 的 e_i 估计有 10% 误差，c_n 的后验会如何偏移？这是合理且必要的分析。两位 reviewer 在这一点上高度一致，建议 Director 将其视为 consensus issue。\n\n**[AGREE] R2-W3: Δτ=0.05 的实际排名意义未论证**\n同意。论文报告 G-MFRM 相对 sequential pipeline 的提升为 Δτ ≈ 0.05-0.07（Table 2, Section 5.1），但从未回答关键问题：**这 0.05 的 Kendall τ 提升实际翻转了多少模型对的排名？** 对于 22 个模型（231 个 model pairs），Δτ = 0.05 大约对应 ~12 个 pair 的重排序。论文应报告：(a) 具体哪些模型对被重排序；(b) 重排序后与 Arena 排名的 concordant pair 数量变化。这会比抽象的 τ 值更有说服力。\n\n**[REBUT] R2-W4: Chatbot Arena Elo 作为 ground truth 的 circular reasoning 风险**\n不同意 R2 对此风险程度的评估。R2 的论点是：如果被 contaminated 的模型在 Arena 中也表现更好（因为类似的数据泄露），那么用 Arena 排名评估 decontamination 就有 circularity。但这一论点忽略了 Arena 的根本机制差异：\n\n- **Arena 使用真实用户的实时 pairwise 比较**，prompts 来自用户自发输入，不是固定 benchmark items。Benchmark contamination（记忆 MT-Bench/Arena-Hard 的特定 item）不会直接提升 Arena 对战中面对全新 prompt 的表现。\n- Section 5.8 的跨 benchmark 一致性验证（WildBench τ = 0.89, r(c_n) = 0.62 across benchmarks）从侧面佐证了 contamination 不是简单地与 Arena 排名共变。\n- 如果 Arena 排名自身被 contamination 污染，我们预期 decontamination 后的排名会**远离** Arena，而非更接近——但实验结果恰恰相反（τ 提升），这与 circularity 假设矛盾。\n\n当然，Arena 并非完美 ground truth（存在 recency bias、prompt distribution bias 等），论文可以加一段讨论其局限性。但 R2 所述的\"circular reasoning risk\"在方法论上不成立。\n\n**[AGREE] R2-W5: Stage 2→3 error propagation 未讨论，posterior uncertainty 可能被低估**\n同意，与我的 N1 和 R2-W2 一致。这是三位最终审稿意见中（如果算上我的 N1、R2 的 W2 和 W5）出现频率最高的问题。论文的 posterior intervals 只反映了 Stage 3 的采样不确定性，未纳入 Stage 2 的 e_i 估计不确定性。如果 e_i 的真实不确定性较大（例如 ConStat 的 sensitivity 为 0.58 according to Table 7 ablation），c_n 的 credible intervals 可能显著偏窄。\n\n---\n\n### Novelty 专项评估回应\n\nR2 将 novelty 排序为：G-MFRM model > empirical evaluation > confounding formalization。我基本同意这一排序，但会调整权重：\n\n- **G-MFRM model（主要 novelty）**：gating mechanism 的设计（将 DG-IRT 的 group membership 替换为 continuous exposure + rank-1 contamination）确实是本文最核心的技术贡献。但如我在 N1 中指出，\"joint estimation\"的 claim 被 e_i 预固定所削弱。\n- **Empirical evaluation（次要 novelty）**：实验规模和覆盖度是本文的优势，11 个实验全到位。\n- **Confounding formalization（最低 novelty）**：同意 R2 的判断——这是 OVB 的领域迁移。但\"最低 novelty ≠ 零 novelty\"，将通用定理具体化到特定领域的变量结构并提供实证验证仍有贡献。\n\nR2 提出\"first framework claim 需限定范围\"——我同意，建议 authors 改为\"the first framework **in the LLM evaluation literature** that jointly addresses...\"并引用教育测量学中的先验工作以示区别。\n\n---\n\n### 对 R2 总体评分的看法\n\nR2 给出 Overall 2.5（Borderline Findings），我给出 3.0（Findings）。差异主要来自两处：\n\n1. **格式问题权重**：R2 将格式违规（N1）作为 Must-Fix 影响总分，我认为这是严重但纯技术性的问题——模板转换不改变论文内容质量。如果剥离格式因素，R2 和我在 Soundness 上的评分一致（均为 3/5）。\n\n2. **Excitement 分歧**：R2 给 2.5（因 novelty 有限 + pipeline 复杂），我给 3（因问题动机真实重要）。我认为 R2 在 novelty 维度偏严——即使 formalization 是 OVB 迁移，完整的 G-MFRM framework + 大规模实证验证在 LLM evaluation 领域仍然是有价值的工作。\n\n**Consensus 问题（R1 和 R2 均认为 critical）**：\n1. e_i 预固定导致\"joint estimation\" claim 过度（R1-N1, R2-W2, R2-W5）\n2. 参考文献严重不足（R1-N4, R2-N2）\n3. 零图表（R1-W6, R2-N3）\n4. 格式不合规（R1-W7, R2-N1）\n\n这四个 consensus issues 中，前两个是内容问题（需要实质性修改），后两个是 presentation 问题（可快速修复）。",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-21T21:41:07.329290+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3868
}
```

</details>

---


### Assistant

_source line 46 · 2026-05-21T21:41:14.084222+00:00_

交叉回应已提交。

总结：对 R2 的 8 个问题中，我 [AGREE] 7 个、[REBUT] 1 个（W4 Arena circularity）。与 R2 形成共识的核心问题有 4 个：e_i 预固定削弱"joint"claim、参考文献不足、零图表、格式不合规。唯一分歧在 Arena ground truth 的 circular reasoning 风险——我认为 Arena 的实时人类比较机制从根本上与 benchmark contamination 解耦，R2 的担忧不成立。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 3

## Round 3

26 recorded events


### User

_source line 47 · 2026-05-21T22:30:51.710544+00:00_

[Round 1 审稿请求]:
[Dream 审稿任务 — Reviewer 1：方法 + 实验]

论文标题：Joint Calibration of Judge Bias and Benchmark Contamination Corrects Systematic Rank Distortions in LLM Evaluation

PDF 路径：/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/review_input_db82206b.pdf

实验设计参考（含完整 imagined experiments 列表）：/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/review_context.yaml

目标 Venue：EMNLP 2026（ARR 统一审稿，Overall Assessment 1-5 半分制）
评分刻度：5=Award (top 2.5%), 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit
接受率：Main ~21%，评审维度：Soundness (1-5) + Excitement (1-5) + Reproducibility (1-5)

你的审查侧重：
- **方法描述**：是否完整、claim 是否被实验数据支撑、关键超参 / 训练流程是否清晰
- **实验设计**：是否覆盖关键 baseline / ablation / 跨数据集 / scale 维度
- **数据呈现**：表格 / 图是否能让审稿人复现结论、误差棒 / 统计显著性是否充分

请基于论文内容独立评判，不要假设论文结果的质量高低。

**Dream 审稿边界**：
- 不需要评审：Reproducibility checklist、代码/数据可用性、具体数值精确性（数字是想象的，关注实验设计而非数值）、伦理/IRB、匿名性
- 需要评审但标注为 "presentation 层面"：Reference 真实性、论文完整度、Related Work 引用数量
- 必须评审（idea 层面）：实验设计是否足以支撑 claims（假设数据为真）、叙事逻辑是否自洽、Claim 的 generality 是否被实验范围支撑

每条 weakness 必须标注属于 **idea 层面** 还是 **presentation 层面**。

**评分校准**：3+ Major issues → 不高于 Borderline Reject；2 Major → 不高于 Weak Accept；1 Major → 不高于 Accept；0 Major → 可给 Strong Accept。

**不要评判**：新颖性 / 相关工作（那是 Reviewer 2 的范围）、格式 / 排版。

请通过 `review_reviewer_post_to_director(text, reviewer_id="1", project="gated_mfrm_judge_bias", dream_id="20260521T215715")` 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-21T22:31:03.708002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/review_context.yaml"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-21T22:31:04.162383+00:00_

1	narrative_guidance: 'Full Tier A narrative. Lead with quantitative shock: G-MFRM joint
2	  calibration corrects ~40% θ-RMSE and +5-6pp Kendall-τ over best sequential baseline
3	  on real MT-Bench/Arena-Hard data. Real contamination is strong (median c_n ≈ 0.95),
4	  validating the core premise that confounding is not a theoretical curiosity but
5	  a measurable distortion in current LLM evaluation practice. Paper title: "Joint
6	  Calibration of Judge Bias and Benchmark Contamination Corrects Systematic Rank Distortions
7	  in LLM Evaluation." Section 2 opens with the OVB observation on a 3-model toy example,
8	  then pivots to G-MFRM. Main result table is the centerpiece: G-MFRM beats all 8
9	  baselines on both benchmarks, with CyclicJudge+discard as strongest competitor but
10	  still 4-5pp behind. Rank change analysis provides the narrative hook — at least
11	  4 models shift ≥2 positions, and 2 top-5 models swap, making the correction practically
12	  consequential for deployment decisions. ConStat external validation (ρ≥0.78) closes
13	  the loop: fitted c_n is not a MCMC artifact but tracks an independently measurable
14	  contamination signal.
15	
16	  '
17	imagined_experiments:
18	- name: multi_judge_data_collection
19	  plan_id: exp-001
20	  description: 'Collect multi-judge evaluation data on MT-Bench (80 items × 20 target
21	    models × 8 judges × 2 positions) and Arena-Hard (500 items × 20 target models
22	    × 8 judges × 2 positions). Total ~185,600 pairwise judgments after position swap.
23	
24	    '
25	  expected_results:
26	    total_judgments: 185600
27	    mt_bench_judgments: 25600
28	    arena_hard_judgments: 160000
29	    target_models_evaluated: 20
30	    judges_used: 8
31	    judge_list: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B,
32	      Qwen3.6-27B, Llama 4 Maverick, Gemini 2.5 Pro
33	    position_bias_rate_mean: 0.58
34	    position_bias_rate_std: 0.07
35	    inter_judge_agreement_fleiss_kappa: 0.42
3
…[truncated 37084 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-21T22:31:04.564468+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/review_input_db82206b.pdf",
  "project": "gated_mfrm_judge_bias",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/review_input_db82206b.pdf",
    "project": "gated_mfrm_judge_bias",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-21T22:31:05.572810+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 410.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 393.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 360.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 375.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 362.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 403.6}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 352.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 324.5}], \"total_pages\": 8, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-m
…[truncated 152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-21T22:31:12.014397+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 53 · 2026-05-21T22:31:12.517179+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 54 · 2026-05-21T22:31:13.421134+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-21T22:31:13.423367+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-21T22:31:13.474082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-21T22:31:13.932490+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 458
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-21T22:31:13.932991+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-21T22:31:14.838587+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-21T22:31:14.889210+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-21T22:31:15.344522+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-21T22:31:15.345025+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 63 · 2026-05-21T22:31:15.901490+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 64 · 2026-05-21T22:31:16.512901+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1167
}
```

</details>

---


### Tool call

_source line 65 · 2026-05-21T22:31:16.513335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images/paper_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 66 · 2026-05-21T22:31:16.625617+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 724
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-21T22:31:17.183462+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 670
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-21T22:37:22.315593+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告：Methods & Experiments\n**论文**: \"Joint Calibration of Judge Bias and Benchmark Contamination Corrects Systematic Rank Distortions in LLM Evaluation\"\n**Dream ID**: 20260521T215715\n**审查侧重**: 方法描述完整性、实验设计覆盖度、数据呈现质量\n\n---\n\n## 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 实验设计全面出色（12 个实验覆盖全部关键维度，含 error propagation 分析），方法描述清晰完整，但统计证据呈现有系统性缺陷——主表无 CI、WildBench 无显著性检验、全文零 figures——这些缺陷在 idea 层面削弱了核心 claims 的证据力度。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 (Strong) | 方法论完整（三阶段 pipeline、gating 机制、Bayesian 推断），实验设计覆盖所有关键维度（baseline/ablation/cross-benchmark/sensitivity/error propagation/adversarial），每个 claim 都有对应实验支撑。但部分 claims 缺少完整统计证据（CIs, p-values）|\n| Excitement | 3/5 (Interesting) | [仅评 idea 不评 novelty] 问题重要，实验方法论严谨。但效果量 Δτ = 0.04-0.05 仅对应 ~5 个 model pair 翻转，实际影响力中等。需 ≥3-4 judges + MCMC 3.2 小时的 pipeline 复杂度限制采纳|\n| Confidence | 4/5 | 仔细阅读全文 + review_context.yaml 逐一对照 |\n\n---\n\n## Must-Fix 问题\n\n**N1** [Major, idea 层面] 主表（Table 2）缺少 confidence intervals，cross-benchmark 泛化（Table 5）缺少显著性检验\n- 具体位置：Table 2（Section 5.1）, Table 5（Section 5.4）\n- 问题：\n  (a) Table 2 是论文核心结果表，报告了 G-MFRM 在 MT-Bench/Arena-Hard 上的 Kendall τ 及与最强 baseline 的 Δτ = 0.04-0.05。但仅报告一个 Wilcoxon p = 0.003，**没有任何 τ 值的 confidence intervals**（如 bootstrap CI）。读者无法判断 τ = 0.91 的不确定性范围——如果 95% CI 为 [0.85, 0.96]，则 Δτ = 0.04 可能不具实际意义。review_context.yaml（Table 4）预期了 95% CI (τ) 列（如 [0.86, 0.95]），但论文未包含。\n  (b) Table 5 报告 WildBench τ = 0.90、Δτ = 0.04，但**完全没有 p-value 或 CI**。论文据此声称\"G-MFRM's advantage is consistent across three benchmarks\"（Section 5.4），但 WildBench 的 claim 缺乏统计检验支撑。如果 WildBench 上 p > 0.05，\"consistent\"结论不成立。\n- 为什么是 Major：统计显著性和 uncertainty quantification 是实验论文的基础要求。在效果量较小（Δτ = 0.04-0.05）的场景下，CIs 尤为关键——它们决定了 claim 是\"显著且稳健\"还是\"可能是噪声\"。当前的数据呈现无法让审稿人独立验证核心 claims。\n- 建议：(1) Table 2 每个 τ 值加 bootstrap 95% CI；(2) Table 5 加 Wilcoxon p-value 或 permutation test；(3) 报告 τ 差异的 CI（如 Δτ [0.02, 0.07]）。\n\n**N2** [Major, presentation 层面] 全文零 figures——14 张 tables 但无任何可视化\n- 具体位置：全文（pages 1-8）\n- 问题：论文依赖 14 张表格呈现所有结果，但没有任何 figure。review_context.yaml 设计了 8 个 main figures + 12 个 appendix figures（包括 pipeline 图、bump chart、scatter plot、sensitivity curves 等），但论文中一个都没有。对审稿人而言，以下 claims 在没有可视化时难以独立验证：\n  - **Rank change patterns**（Table 3）：bump chart 能直观展示 20 个模型的排名流向，table 只能列出移动最大的 5 个。其余 15 个模型的 pattern 完全不可见。\n  - **ConStat 验证**（Table 4）：scatter plot 能展示 c_n vs ConStat Δ 的分布形态（是否有 outliers、是否有非线性），单靠 ρ = 0.82 数字无法判断。\n  - **Judge count sensitivity**（Table 7）：degradation curve 的形状（线性？指数？有拐点？）从表格 5 行数字中不直观。\n  - **Error propagation**（Table 8）：dual-axis plot 比 5 行数字更清晰地展示 robustness threshold。\n- 为什么是 Major（presentation 层面）：ACL 顶会论文的审阅标准要求 figures 辅助 tables 构建 visual narrative。零 figures 不仅是排版问题——它直接影响审稿人对数据 patterns 的独立判断能力，属于\"数据呈现是否能让审稿人复现结论\"的范畴。\n- 建议：至少加入以下 4 个 figures：(1) Fig 1: G-MFRM pipeline overview（帮助理解三阶段方法）；(2) Fig 2: bump chart of rank changes（支撑 Section 5.2 的实际影响力 claim）；(3) Fig 3: c_n vs ConStat scatter with CI band（支撑 external validation）；(4) Fig 4: Kendall τ bar chart with error bars for all methods（主结果可视化）。\n\n---\n\n## Should-Fix 问题\n\n**W1** [idea 层面] Exposure ablation 关键结果未以表格呈现，缺乏可验证性\n- 具体位置：Section 6.2（page 5-6）\n- 问题：Section 6.2 在正文中报告了 leave-one-out ablation 的关键数字：Performance Gap 贡献 72%、Temporal 8%、LogProber 12%、interaction 8%。但这些数字仅出现在行文中，没有像 review_context.yaml Table 9 那样以结构化表格呈现（含 configuration | τ | Δτ | c_n ρ | Δρ 各列）。此外，文中说\"removing it drops τ and c_n recovery by Δτ = 0.27\"——这句表述混淆了两个不同的指标（τ 下降 ~0.05，c_n ρ 下降 0.27），容易误导读者。\n- 建议：(1) 将 ablation 结果从行文移到独立表格；(2) 分别报告 Δτ 和 Δc_n_ρ 两个指标。\n\n**W2** [idea 层面] Bayesian 后验校准的 95% CI coverage 未报告\n- 具体位置：Section 2.2, Table 8（σ=0.0 行）\n- 问题：Table 8 的 σ=0.0 行隐含了合成数据上 c_n 恢复的基线质量（RMSE=0.09, ρ=0.96），这是好的。但 review_context.yaml（exp-009）预期的 95% CI coverage = 0.93（衡量 Bayesian credible intervals 是否 well-calibrated）在论文中完全缺失。Section 2.2 仅说\"confirming well-calibrated posterior inference\"但未给出定量证据。\n- 为什么重要：对于 Bayesian 模型，posterior calibration 是关键质量指标。如果 95% CI coverage 显著偏离 0.95（如仅为 0.80），则后验 uncertainty 被系统性低估，影响所有基于 credible intervals 的推断。\n- 建议：在 Section 6.1 或 Appendix B 中报告合成数据上的 empirical coverage probability。\n\n**W3** [idea 层面] \"Joint Calibration\"标题与 staged estimation 实质的张力\n- 具体位置：标题、Section 3 vs. Section 6.4、Limitations\n- 问题：论文标题说\"Joint Calibration\"，但 Section 6.4 明确承认 e_i 是 Stage 2 预估计并固定的。Limitations 诚实讨论了这一点（\"Since e_i is pre-estimated and fixed in Stage 3, errors in e_i propagate to θ and c_n estimates\"），Section 6.4 的 error propagation 分析也直接回应了这个问题——这是好的做法。\n- 但标题和 Abstract 的\"joint calibration\"仍可能误导读者以为所有参数（含 e_i）都在单一模型中联合估计。Abstract 中\"a staged joint calibration framework\"的\"staged\"限定词在快速阅读时容易被忽略。\n- 建议：标题改为\"Staged Joint Calibration...\"或\"Joint Calibration...via Staged Estimation\"以更准确反映方法本质。或在 Section 3 开头增加一句明确声明：\"Note that e_i is externally estimated and fixed; 'joint' refers to the simultaneous estimation of θ, b, d, and c in Stage 3.\"\n\n**W4** [presentation 层面] Table 编号从 5 跳到 7，缺少 Table 6\n- 具体位置：page 5-6\n- 问题：论文 Table 编号序列为 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14——缺少 Table 6。推测 Table 6（contamination calibration）被移至 Appendix C（Table 12）但编号未更新。\n- 建议：修复 Table 编号。\n\n**W5** [presentation 层面] Section 4.1 称\"5 model families\"但实际列出 6 个\n- 具体位置：Section 4.1（page 3）\n- 问题：8 个 judges 来自 OpenAI (1)、Anthropic (2)、DeepSeek (1)、Alibaba (2)、Meta (1)、Google (1) = 6 个 model families。论文写\"spanning 5 model families\"，与实际列表不一致。\n- 建议：修正为\"6 model families\"。\n\n**W6** [idea 层面] Error propagation 表（Table 8）缺少 Monte Carlo 不确定性估计\n- 具体位置：Table 8（Section 6.4）\n- 问题：Table 8 报告了不同 σ 下的 θ̂ RMSE、degradation %、c_n RMSE 和 c_n ρ，但这些是合成实验的结果——应当有来自多次 Monte Carlo 重复的标准误差或 CI（review_context.yaml exp-009 用了 500 replications）。当前报告方式无法判断 σ=0.2 处的 7.3% degradation 是否稳健。\n- 建议：在 Table 8 中加入 ±SE 列或脚注报告 replication 次数和 SE。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 6.2 提到\"Gap only\"配置 τ = 0.912，仅比 full pipeline (0.92) 低 0.8pp。这暗示 temporal 和 LogProber 的边际贡献非常小——应讨论是否值得增加这两个信号源的复杂性。\n- Table 7 显示 J=2 时 R̂ = 1.08，超过了常用的 1.05 阈值。虽然 Section 6.3 对此有讨论，但建议在 Table 7 中标注此行为\"convergence marginal\"。\n- Table 14（Appendix E, Adversarial Robustness）的 \"Exposure manipulation\" 行对 Sequential 标注 \"N/A\"——应解释为何 sequential baseline 不适用于此攻击类型。\n\n---\n\n## 主要优势\n\n1. **实验设计覆盖度一流**：12 个实验（exp-001 至 exp-012）覆盖了数据收集、exposure 估计、主模型拟合、8 个 baseline 对比、contamination 校准、judge count 敏感性、exposure ablation、facet fit、OVB Monte Carlo 验证、WildBench 跨 benchmark 复制、adversarial robustness、**error propagation sensitivity**。最后一项（Section 6.4, Table 8）直接回应了 staged estimation 的核心方法论关切——在已发表的 LLM evaluation 论文中很少见到如此全面的 robustness 分析。\n\n2. **方法描述清晰完整**：三阶段 pipeline 的每个步骤都有明确的方程（Eq 1-4）、先验设定（Half-Cauchy(0, 0.5) for c_n）、MCMC 配置（4 chains, 2000 warmup, 4000 samples, target_accept=0.95）。Gating mechanism 的设计直觉（e_i=0 时退化为 MFRM）被清晰阐述。\n\n3. **OVB 论述诚实恰当**：Section 2.1 使用\"Observation\"而非\"Proposition\"或\"Theorem\"，并明确引用 Frisch-Waugh-Lovell (Angrist & Pischke, 2009) 作为理论来源。这是对贡献边界的诚实界定。\n\n4. **Rank change 分析（Table 3）提供了实际意义的证据**：不仅报告 Δτ 数字，还具体展示哪些模型移动了多少位、移动方向和原因（c_n 值）。这回答了\"Δτ = 0.04 实际意味着什么\"的关键问题。\n\n5. **ConStat 外部验证（Table 4）提供了独立校验**：c_n 与 ConStat per-model delta 的 ρ = 0.82 [0.65, 0.92] 是论文的关键防线——证明拟合的 contamination 参数不是 MCMC artifact。\n\n6. **Limitations section 诚实全面**：覆盖了 staged estimation 局限、7.3% degradation at σ=0.2（诚实承认超过理想阈值）、judge count 要求、rank-1 假设、Arena ground truth、MCMC 运行时间。\n\n---\n\n## 与 review_context.yaml 的对照\n\n**实验覆盖度**（12/12 全部到位）：\n| YAML Experiment | Paper Location | 完整度 |\n|----------------|---------------|--------|\n| exp-001 (Data Collection) | §4.1, Table 9 (App A) | ✓ |\n| exp-002 (Exposure Estimation) | §3.2, Table 13 (App D) | ✓ |\n| exp-003 (G-MFRM Fit) | §5.1, §6.1, Tables 2-4 | ✓ |\n| exp-004 (Baseline Comparison) | Table 2 | ✓ |\n| exp-005 (Contam Calibration) | Table 12 (App C) | ✓ |\n| exp-006 (Judge Count) | Table 7 (§6.3) | ✓ |\n| exp-007 (Exposure Ablation) | §6.2 (inline, no table) | ✓ 但无独立表格 |\n| exp-008 (Facet Fit) | §6.1, Tables 10-11 (App B) | ✓ |\n| exp-009 (OVB MC + c_n Recovery) | §2.2 Table 1 + Table 8 σ=0 | ✓ 但 CI coverage 未报告 |\n| exp-010 (WildBench) | Table 5 (§5.4) | ✓ 但缺 p-value |\n| exp-011 (Adversarial) | Table 14 (App E) | ✓ |\n| exp-012 (Error Propagation) | Table 8 (§6.4) | ✓ |\n\n**Figures 覆盖度**（0/20）：YAML 设计了 Fig 1-8 (main) + Fig A1-A12 (appendix)，论文中一个都没有。这是本文最大的 presentation gap。\n\n**关键缺失项**：\n1. τ 的 bootstrap CIs（YAML Table 4 预期有，论文无）\n2. WildBench p-value（YAML exp-010 预期有，论文无）\n3. 95% CI coverage for c_n posterior（YAML exp-009 = 0.93，论文未报告）\n4. Exposure ablation 独立表格（YAML Table 9，论文仅 inline text）\n5. 所有 20 个 figures\n\n---\n\n## 评分校准说明\n\n按 Dream 审稿校准规则：1 个 idea-level Major（N1 统计证据缺陷）+ 1 个 presentation-level Major（N2 零 figures）→ 考虑到 presentation Major 权重较低，且实验设计本身非常优秀（12/12 实验全到位、error propagation 分析直接回应核心关切），给出 **3.5 Borderline Conference**。\n\n如果补充 N1（CIs + WildBench p-value）和 N2（至少 4 个关键 figures），论文的 evidence presentation 将达到 4.0 Conference 水平——实验设计的实质已经到位，缺的是呈现层面的最后一步。",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告：Methods & Experiments\n**论文**: \"Joint Calibration of Judge Bias and Benchmark Contamination Corrects Systematic Rank Distortions in LLM Evaluation\"\n**Dream ID**: 20260521T215715\n**审查侧重**: 方法描述完整性、实验设计覆盖度、数据呈现质量\n\n---\n\n## 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 实验设计全面出色（12 个实验覆盖全部关键维度，含 error propagation 分析），方法描述清晰完整，但统计证据呈现有系统性缺陷——主表无 CI、WildBench 无显著性检验、全文零 figures——这些缺陷在 idea 层面削弱了核心 claims 的证据力度。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 (Strong) | 方法论完整（三阶段 pipeline、gating 机制、Bayesian 推断），实验设计覆盖所有关键维度（baseline/ablation/cross-benchmark/sensitivity/error propagation/adversarial），每个 claim 都有对应实验支撑。但部分 claims 缺少完整统计证据（CIs, p-values）|\n| Excitement | 3/5 (Interesting) | [仅评 idea 不评 novelty] 问题重要，实验方法论严谨。但效果量 Δτ = 0.04-0.05 仅对应 ~5 个 model pair 翻转，实际影响力中等。需 ≥3-4 judges + MCMC 3.2 小时的 pipeline 复杂度限制采纳|\n| Confidence | 4/5 | 仔细阅读全文 + review_context.yaml 逐一对照 |\n\n---\n\n## Must-Fix 问题\n\n**N1** [Major, idea 层面] 主表（Table 2）缺少 confidence intervals，cross-benchmark 泛化（Table 5）缺少显著性检验\n- 具体位置：Table 2（Section 5.1）, Table 5（Section 5.4）\n- 问题：\n  (a) Table 2 是论文核心结果表，报告了 G-MFRM 在 MT-Bench/Arena-Hard 上的 Kendall τ 及与最强 baseline 的 Δτ = 0.04-0.05。但仅报告一个 Wilcoxon p = 0.003，**没有任何 τ 值的 confidence intervals**（如 bootstrap CI）。读者无法判断 τ = 0.91 的不确定性范围——如果 95% CI 为 [0.85, 0.96]，则 Δτ = 0.04 可能不具实际意义。review_context.yaml（Table 4）预期了 95% CI (τ) 列（如 [0.86, 0.95]），但论文未包含。\n  (b) Table 5 报告 WildBench τ = 0.90、Δτ = 0.04，但**完全没有 p-value 或 CI**。论文据此声称\"G-MFRM's advantage is consistent across three benchmarks\"（Section 5.4），但 WildBench 的 claim 缺乏统计检验支撑。如果 WildBench 上 p > 0.05，\"consistent\"结论不成立。\n- 为什么是 Major：统计显著性和 uncertainty quantification 是实验论文的基础要求。在效果量较小（Δτ = 0.04-0.05）的场景下，CIs 尤为关键——它们决定了 claim 是\"显著且稳健\"还是\"可能是噪声\"。当前的数据呈现无法让审稿人独立验证核心 claims。\n- 建议：(1) Table 2 每个 τ 值加 bootstrap 95% CI；(2) Table 5 加 Wilcoxon p-value 或 permutation test；(3) 报告 τ 差异的 CI（如 Δτ [0.02, 0.07]）。\n\n**N2** [Major, presentation 层面] 全文零 figures——14 张 tables 但无任何可视化\n- 具体位置：全文（pages 1-8）\n- 问题：论文依赖 14 张表格呈现所有结果，但没有任何 figure。review_context.yaml 设计了 8 个 main figures + 12 个 appendix figures（包括 pipeline 图、bump chart、scatter plot、sensitivity curves 等），但论文中一个都没有。对审稿人而言，以下 claims 在没有可视化时难以独立验证：\n  - **Rank change patterns**（Table 3）：bump chart 能直观展示 20 个模型的排名流向，table 只能列出移动最大的 5 个。其余 15 个模型的 pattern 完全不可见。\n  - **ConStat 验证**（Table 4）：scatter plot 能展示 c_n vs ConStat Δ 的分布形态（是否有 outliers、是否有非线性），单靠 ρ = 0.82 数字无法判断。\n  - **Judge count sensitivity**（Table 7）：degradation curve 的形状（线性？指数？有拐点？）从表格 5 行数字中不直观。\n  - **Error propagation**（Table 8）：dual-axis plot 比 5 行数字更清晰地展示 robustness threshold。\n- 为什么是 Major（presentation 层面）：ACL 顶会论文的审阅标准要求 figures 辅助 tables 构建 visual narrative。零 figures 不仅是排版问题——它直接影响审稿人对数据 patterns 的独立判断能力，属于\"数据呈现是否能让审稿人复现结论\"的范畴。\n- 建议：至少加入以下 4 个 figures：(1) Fig 1: G-MFRM pipeline overview（帮助理解三阶段方法）；(2) Fig 2: bump chart of rank changes（支撑 Section 5.2 的实际影响力 claim）；(3) Fig 3: c_n vs ConStat scatter with CI band（支撑 external validation）；(4) Fig 4: Kendall τ bar chart with error bars for all methods（主结果可视化）。\n\n---\n\n## Should-Fix 问题\n\n**W1** [idea 层面] Exposure ablation 关键结果未以表格呈现，缺乏可验证性\n- 具体位置：Section 6.2（page 5-6）\n- 问题：Section 6.2 在正文中报告了 leave-one-out ablation 的关键数字：Performance Gap 贡献 72%、Temporal 8%、LogProber 12%、interaction 8%。但这些数字仅出现在行文中，没有像 review_context.yaml Table 9 那样以结构化表格呈现（含 configuration | τ | Δτ | c_n ρ | Δρ 各列）。此外，文中说\"removing it drops τ and c_n recovery by Δτ = 0.27\"——这句表述混淆了两个不同的指标（τ 下降 ~0.05，c_n ρ 下降 0.27），容易误导读者。\n- 建议：(1) 将 ablation 结果从行文移到独立表格；(2) 分别报告 Δτ 和 Δc_n_ρ 两个指标。\n\n**W2** [idea 层面] Bayesian 后验校准的 95% CI coverage 未报告\n- 具体位置：Section 2.2, Table 8（σ=0.0 行）\n- 问题：Table 8 的 σ=0.0 行隐含了合成数据上 c_n 恢复的基线质量（RMSE=0.09, ρ=0.96），这是好的。但 review_context.yaml（exp-009）预期的 95% CI coverage = 0.93（衡量 Bayesian credible intervals 是否 well-calibrated）在论文中完全缺失。Section 2.2 仅说\"confirming well-calibrated posterior inference\"但未给出定量证据。\n- 为什么重要：对于 Bayesian 模型，posterior calibration 是关键质量指标。如果 95% CI coverage 显著偏离 0.95（如仅为 0.80），则后验 uncertainty 被系统性低估，影响所有基于 credible intervals 的推断。\n- 建议：在 Section 6.1 或 Appendix B 中报告合成数据上的 empirical coverage probability。\n\n**W3** [idea 层面] \"Joint Calibration\"标题与 staged estimation 实质的张力\n- 具体位置：标题、Section 3 vs. Section 6.4、Limitations\n- 问题：论文标题说\"Joint Calibration\"，但 Section 6.4 明确承认 e_i 是 Stage 2 预估计并固定的。Limitations 诚实讨论了这一点（\"Since e_i is pre-estimated and fixed in Stage 3, errors in e_i propagate to θ and c_n estimates\"），Section 6.4 的 error propagation 分析也直接回应了这个问题——这是好的做法。\n- 但标题和 Abstract 的\"joint calibration\"仍可能误导读者以为所有参数（含 e_i）都在单一模型中联合估计。Abstract 中\"a staged joint calibration framework\"的\"staged\"限定词在快速阅读时容易被忽略。\n- 建议：标题改为\"Staged Joint Calibration...\"或\"Joint Calibration...via Staged Estimation\"以更准确反映方法本质。或在 Section 3 开头增加一句明确声明：\"Note that e_i is externally estimated and fixed; 'joint' refers to the simultaneous estimation of θ, b, d, and c in Stage 3.\"\n\n**W4** [presentation 层面] Table 编号从 5 跳到 7，缺少 Table 6\n- 具体位置：page 5-6\n- 问题：论文 Table 编号序列为 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14——缺少 Table 6。推测 Table 6（contamination calibration）被移至 Appendix C（Table 12）但编号未更新。\n- 建议：修复 Table 编号。\n\n**W5** [presentation 层面] Section 4.1 称\"5 model families\"但实际列出 6 个\n- 具体位置：Section 4.1（page 3）\n- 问题：8 个 judges 来自 OpenAI (1)、Anthropic (2)、DeepSeek (1)、Alibaba (2)、Meta (1)、Google (1) = 6 个 model families。论文写\"spanning 5 model families\"，与实际列表不一致。\n- 建议：修正为\"6 model families\"。\n\n**W6** [idea 层面] Error propagation 表（Table 8）缺少 Monte Carlo 不确定性估计\n- 具体位置：Table 8（Section 6.4）\n- 问题：Table 8 报告了不同 σ 下的 θ̂ RMSE、degradation %、c_n RMSE 和 c_n ρ，但这些是合成实验的结果——应当有来自多次 Monte Carlo 重复的标准误差或 CI（review_context.yaml exp-009 用了 500 replications）。当前报告方式无法判断 σ=0.2 处的 7.3% degradation 是否稳健。\n- 建议：在 Table 8 中加入 ±SE 列或脚注报告 replication 次数和 SE。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 6.2 提到\"Gap only\"配置 τ = 0.912，仅比 full pipeline (0.92) 低 0.8pp。这暗示 temporal 和 LogProber 的边际贡献非常小——应讨论是否值得增加这两个信号源的复杂性。\n- Table 7 显示 J=2 时 R̂ = 1.08，超过了常用的 1.05 阈值。虽然 Section 6.3 对此有讨论，但建议在 Table 7 中标注此行为\"convergence marginal\"。\n- Table 14（Appendix E, Adversarial Robustness）的 \"Exposure manipulation\" 行对 Sequential 标注 \"N/A\"——应解释为何 sequential baseline 不适用于此攻击类型。\n\n---\n\n## 主要优势\n\n1. **实验设计覆盖度一流**：12 个实验（exp-001 至 exp-012）覆盖了数据收集、exposure 估计、主模型拟合、8 个 baseline 对比、contamination 校准、judge count 敏感性、exposure ablation、facet fit、OVB Monte Carlo 验证、WildBench 跨 benchmark 复制、adversarial robustness、**error propagation sensitivity**。最后一项（Section 6.4, Table 8）直接回应了 staged estimation 的核心方法论关切——在已发表的 LLM evaluation 论文中很少见到如此全面的 robustness 分析。\n\n2. **方法描述清晰完整**：三阶段 pipeline 的每个步骤都有明确的方程（Eq 1-4）、先验设定（Half-Cauchy(0, 0.5) for c_n）、MCMC 配置（4 chains, 2000 warmup, 4000 samples, target_accept=0.95）。Gating mechanism 的设计直觉（e_i=0 时退化为 MFRM）被清晰阐述。\n\n3. **OVB 论述诚实恰当**：Section 2.1 使用\"Observation\"而非\"Proposition\"或\"Theorem\"，并明确引用 Frisch-Waugh-Lovell (Angrist & Pischke, 2009) 作为理论来源。这是对贡献边界的诚实界定。\n\n4. **Rank change 分析（Table 3）提供了实际意义的证据**：不仅报告 Δτ 数字，还具体展示哪些模型移动了多少位、移动方向和原因（c_n 值）。这回答了\"Δτ = 0.04 实际意味着什么\"的关键问题。\n\n5. **ConStat 外部验证（Table 4）提供了独立校验**：c_n 与 ConStat per-model delta 的 ρ = 0.82 [0.65, 0.92] 是论文的关键防线——证明拟合的 contamination 参数不是 MCMC artifact。\n\n6. **Limitations section 诚实全面**：覆盖了 staged estimation 局限、7.3% degradation at σ=0.2（诚实承认超过理想阈值）、judge count 要求、rank-1 假设、Arena ground truth、MCMC 运行时间。\n\n---\n\n## 与 review_context.yaml 的对照\n\n**实验覆盖度**（12/12 全部到位）：\n| YAML Experiment | Paper Location | 完整度 |\n|----------------|---------------|--------|\n| exp-001 (Data Collection) | §4.1, Table 9 (App A) | ✓ |\n| exp-002 (Exposure Estimation) | §3.2, Table 13 (App D) | ✓ |\n| exp-003 (G-MFRM Fit) | §5.1, §6.1, Tables 2-4 | ✓ |\n| exp-004 (Baseline Comparison) | Table 2 | ✓ |\n| exp-005 (Contam Calibration) | Table 12 (App C) | ✓ |\n| exp-006 (Judge Count) | Table 7 (§6.3) | ✓ |\n| exp-007 (Exposure Ablation) | §6.2 (inline, no table) | ✓ 但无独立表格 |\n| exp-008 (Facet Fit) | §6.1, Tables 10-11 (App B) | ✓ |\n| exp-009 (OVB MC + c_n Recovery) | §2.2 Table 1 + Table 8 σ=0 | ✓ 但 CI coverage 未报告 |\n| exp-010 (WildBench) | Table 5 (§5.4) | ✓ 但缺 p-value |\n| exp-011 (Adversarial) | Table 14 (App E) | ✓ |\n| exp-012 (Error Propagation) | Table 8 (§6.4) | ✓ |\n\n**Figures 覆盖度**（0/20）：YAML 设计了 Fig 1-8 (main) + Fig A1-A12 (appendix)，论文中一个都没有。这是本文最大的 presentation gap。\n\n**关键缺失项**：\n1. τ 的 bootstrap CIs（YAML Table 4 预期有，论文无）\n2. WildBench p-value（YAML exp-010 预期有，论文无）\n3. 95% CI coverage for c_n posterior（YAML exp-009 = 0.93，论文未报告）\n4. Exposure ablation 独立表格（YAML Table 9，论文仅 inline text）\n5. 所有 20 个 figures\n\n---\n\n## 评分校准说明\n\n按 Dream 审稿校准规则：1 个 idea-level Major（N1 统计证据缺陷）+ 1 个 presentation-level Major（N2 零 figures）→ 考虑到 presentation Major 权重较低，且实验设计本身非常优秀（12/12 实验全到位、error propagation 分析直接回应核心关切），给出 **3.5 Borderline Conference**。\n\n如果补充 N1（CIs + WildBench p-value）和 N2（至少 4 个关键 figures），论文的 evidence presentation 将达到 4.0 Conference 水平——实验设计的实质已经到位，缺的是呈现层面的最后一步。",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-21T22:37:26.338189+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4022
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-21T22:37:31.475521+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-21T22:37:31.576371+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 72 · 2026-05-21T22:37:38.456734+00:00_

Dream 审稿完成。

**总结**：给出 3.5 (Borderline Conference)。实验设计是本文最大优势——12 个实验全部到位，含 error propagation sensitivity analysis 直接回应 staged estimation 关切。方法描述清晰，OVB 论述用"Observation"而非"Proposition"更为诚实。两个主要问题：(1) idea 层面——主表缺 CIs、WildBench 缺 p-value，统计证据不完整；(2) presentation 层面——全文零 figures（YAML 预期 20 个 figures）。补上统计证据和关键可视化后可达 4.0 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 4

## Round 4

46 recorded events


### User

_source line 73 · 2026-05-21T22:37:39.538761+00:00_

[Round 1 审稿请求]:
## Review Assignment: R1 — Methods & Experiments

You are reviewing a paper titled "Gated Many-Facet Rasch Model for Joint Judge Bias and Contamination Correction in LLM Evaluation" for EMNLP 2026 (ARR submission).

### Paper Summary
The paper proposes G-MFRM, a three-stage calibration framework that jointly estimates model ability (θ), item difficulty (b), judge severity (d_j), and contamination susceptibility (c_n) in LLM-as-a-judge evaluation. The key insight is that sequential correction of judge bias and contamination is methodologically flawed due to omitted variable bias (OVB) when d_j and c_n·e_i are non-orthogonal. The model uses a gating term c_n·e_i where e_i is externally estimated from three sources (performance gap, temporal, LogProber).

### Your Focus Areas
1. **Methodological soundness**: Is the G-MFRM formulation (Eq. 4) well-motivated? Is the three-stage estimation procedure principled? Is the OVB argument (Section 2) correctly formalized?
2. **Experimental rigor**: Evaluate convergence diagnostics (Table 5: R̂=1.07, ESS=142 for c_n, 12 divergent transitions), baseline comparisons (Table 6: 8 baselines), and statistical testing (Wilcoxon signed-rank).
3. **Ablation quality**: Judge count sensitivity (Table 11), exposure indicator ablation (Table 12), error propagation (Table 13), facet fit diagnostics (Table 14).
4. **Key concerns to investigate**:
   - The improvement over CyclicJudge+Discard is only +0.02 τ (p=0.073, NOT significant at 0.05). How does the paper handle this?
   - c_n convergence: R̂=1.07 and min ESS=142 are adequate but not ideal. Are 12 divergent transitions concerning?
   - Staged estimation fixing e_i: the 95% CI coverage is only 88% (below nominal 95%). Is the under-coverage adequately discussed?
   - The rank-1 assumption (c_n·e_i proportional) — 13.6% misfitting rate for contamination facet. Is this problematic?
   - Breakeven σ≈0.38 for error propagation with estimated pipeline noise σ=0.15-0.20 — is the 1.9-2.5× safety margin sufficient?

### Scoring Dimensions (ARR scale 1-5)
Evaluate: Soundness, Excitement, Reproducibility.
Overall Assessment: 5=Award, 4=Conference accept, 3=Findings, 2=Resubmit, 1=Do not resubmit. Half-points allowed.
EMNLP Main acceptance rate ~21%. Calibrate accordingly.

### Structure your review as:
1. Summary (2-3 sentences)
2. Strengths (bulleted)
3. Weaknesses (bulleted, with severity: major/minor)
4. Questions for authors
5. Scores (Soundness, Excitement, Reproducibility, Overall)
6. Confidence (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-21T22:37:56.267573+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -lt /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/ | head -20",
  "description": "List dream reports sorted by time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -lt /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/ | head -20",
    "description": "List dream reports sorted by time"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-21T22:37:56.468742+00:00_

total 12
drwxr-xr-x 6 ubuntu ubuntu 4096 May 21 22:24 dream_20260521T215715
lrwxrwxrwx 1 ubuntu ubuntu  115 May 21 21:37 latest -> /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917
drwxr-xr-x 6 ubuntu ubuntu 4096 May 21 21:37 dream_20260521T204917

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-21T22:38:00.287624+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/ -name \"*.pdf\" -type f 2>/dev/null",
  "description": "Find all PDFs in the latest dream report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/ -name \"*.pdf\" -type f 2>/dev/null",
    "description": "Find all PDFs in the latest dream report"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-21T22:38:00.338293+00:00_

/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/paper.pdf
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/paper.pdf
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/best/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-21T22:38:10.432815+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/",
  "description": "List median tier files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/",
    "description": "List median tier files"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-21T22:38:10.734269+00:00_

_pdf_images
experiment_data.json
imagined_experiments.yaml
paper.aux
paper.log
paper.out
paper.pdf
paper.tex
paper_framing.md
review_context.yaml
review_input_e90a5c14.pdf
review_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-21T22:38:10.886504+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/",
  "description": "List worst tier files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/",
    "description": "List worst tier files"
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-21T22:38:10.987384+00:00_

experiment_data.json
imagined_experiments.yaml
paper.aux
paper.log
paper.out
paper.pdf
paper.tex
paper_framing.md
review_context.yaml
review_input_f5f46a62.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-21T22:38:14.499534+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/review_context.yaml",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/review_context.yaml",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-21T22:38:14.550192+00:00_

1	narrative_guidance: 'Tier B narrative. Real contamination is detectable but moderate
2	  (c_n median ~0.5). G-MFRM ranking improvement over best baselines is statistically
3	  significant but practically modest (+2-3pp Kendall-τ). Pivot primary contribution
4	  to diagnostic/interpretability outputs: per-model c_n as training data audit tool,
5	  per-item e_i for item retirement decisions, per-judge d_j for judge selection guidance.
6	  Lead argument: ''Sequential methods provide no visibility into whether corrections
7	  are needed — G-MFRM provides both correction and diagnosis.'' Forward-looking: as
8	  contamination grows, joint estimation becomes critical. May need exp-010 (WildBench)
9	  to strengthen empirical package with a third benchmark.
10	
11	  '
12	imagined_experiments:
13	- name: multi_judge_data_collection
14	  plan_id: exp-001
15	  description: 'Collect multi-judge evaluation data on MT-Bench and Arena-Hard using
16	    8 judges. 20+ target models evaluated with position swap.
17	
18	    '
19	  expected_results:
20	    num_judges: 8
21	    num_target_models: 22
22	    benchmarks:
23	    - MT-Bench
24	    - Arena-Hard
25	    total_judgments_mt_bench: 28160
26	    total_judgments_arena_hard: 35200
27	    position_bias_detected_judges: 3
28	    api_cost_usd: 820
29	    gpu_hours_used: 118
30	    missing_data_pct: 2.1
31	    inter_judge_agreement_fleiss_kappa: 0.38
32	  result_rationale: 'Median档下，8个judge的评分会展现出中等程度的一致性（Fleiss κ~0.38），反映了judge之间severity差异的真实存在。
33	    22个target model覆盖了从GPT-5.5到开源7B模型的能力梯度，确保contamination susceptibility的变异性。 Position
34	    bias在3个judge上显著（主要是较小的开源judge），这为d_j估计提供了必要的judge间变异。 缺失数据约2%来自API超时和vLLM偶发OOM，在可接受范围内。
35	
36	    '
37	  tables:
38	  - name: 'Table A1: Judge × Benchmark Data Collection Summary'
39	    columns:
40	    - Judge
41	    - MT-Bench Items
42	    - Arena-Hard Items
43	    - Position Swap
44	    - Missing %
45	    - Mean Score
46	    sample_rows:
47	    - - GPT-5.5
48	      - 1760
49	      - 2200
50	   
…[truncated 199 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-21T22:38:24.541885+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/review_input_e90a5c14.pdf",
  "project": "gated_mfrm_judge_bias",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/review_input_e90a5c14.pdf",
    "project": "gated_mfrm_judge_bias",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 85 · 2026-05-21T22:38:25.094268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/review_context.yaml",
  "offset": "60",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/review_context.yaml",
    "offset": "60",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-21T22:38:25.698065+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 330.7}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 330.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 279.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 273.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 289.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 301.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 280.8}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 261.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_m
…[truncated 1110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1156
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-21T22:38:25.698848+00:00_

60	      - 1760
61	      - 2200
62	      - 'Yes'
63	      - 0.0%
64	      - '7.61'
65	    - - DeepSeek-V4-Pro
66	      - 1760
67	      - 2200
68	      - 'Yes'
69	      - 1.8%
70	      - '7.28'
71	    - - Qwen3-235B-A22B
72	      - 1760
73	      - 2200
74	      - 'Yes'
75	      - 2.5%
76	      - '7.15'
77	    - - Qwen3.6-27B
78	      - 1760
79	      - 2200
80	      - 'Yes'
81	      - 4.2%
82	      - '6.93'
83	    - - Llama 4 Maverick
84	      - 1760
85	      - 2200
86	      - 'Yes'
87	      - 3.1%
88	      - '7.05'
89	    - - Gemma3-27B
90	      - 1760
91	      - 2200
92	      - 'Yes'
93	      - 2.8%
94	      - '6.88'
95	  figures_description:
96	  - 'Fig S1: Judge score distribution heatmap (judge × target model), showing systematic
97	    severity differences across judges.'
98	  analysis: '数据收集本身不直接验证claim，但数据质量决定了后续实验的上限。 Judge间score分布差异（mean range: 6.88–7.82）确认了judge
99	    severity变异的存在，为d_j估计提供信号。 中等的inter-judge agreement (κ~0.38) 意味着judge bias correction有实际意义。
100	
101	    '
102	- name: item_exposure_estimation
103	  plan_id: exp-002
104	  description: '三源pipeline估计per-item exposure e_i。Primary source: 原始vs改写变体的performance
105	    gap； Temporal: pre/post-cutoff变体gap；LogProber: token logprob memorization scores。
106	    加权组合后用ConStat per-model delta做外部验证。
107	
108	    '
109	  expected_results:
110	    num_items_mt_bench: 80
111	    num_items_arena_hard: 100
112	    reference_variants_created: 180
113	    primary_source_coverage: 1.0
114	    temporal_source_coverage: 0.45
115	    logprober_source_coverage: 0.55
116	    composite_e_i_mean: 0.32
117	    composite_e_i_std: 0.21
118	    composite_e_i_range:
119	    - 0.0
120	    - 0.82
121	    high_exposure_items_pct: 18.0
122	    primary_temporal_correlation: 0.58
123	    primary_logprober_correlation: 0.41
124	    weighted_composite_internal_consistency_alpha: 0.62
125	    constat_cn_vs_gmfrm_cn_spearman: 0.52
126	  result_rationale: 'Median档假设real contamination moderate，因此e_i分布右偏但不极端：大部分items（~82%）的e_i
127	    <
…[truncated 7430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-21T22:38:35.857202+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/review_context.yaml",
  "offset": "355",
  "limit": "400"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/review_context.yaml",
    "offset": "355",
    "limit": "400"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-21T22:38:36.810946+00:00_

355	- name: baseline_comparison
356	  plan_id: exp-004
357	  description: 'G-MFRM vs 8条baselines在相同数据上对比。 包含rank change analysis：具体哪些模型换位、换多少位、top-k稳定性。
358	
359	    '
360	  expected_results:
361	    tau_raw_average: 0.79
362	    tau_mfrm_only: 0.82
363	    tau_sequential: 0.84
364	    tau_cyclicjudge: 0.83
365	    tau_cyclicjudge_discard: 0.85
366	    tau_dcr_factor: 0.81
367	    tau_uda: 0.84
368	    tau_pref_leakage_cal: 0.82
369	    tau_gmfrm: 0.87
370	    rho_raw_average: 0.83
371	    rho_mfrm_only: 0.86
372	    rho_sequential: 0.88
373	    rho_cyclicjudge: 0.87
374	    rho_cyclicjudge_discard: 0.89
375	    rho_dcr_factor: 0.85
376	    rho_uda: 0.88
377	    rho_pref_leakage_cal: 0.86
378	    rho_gmfrm: 0.91
379	    tau_gmfrm_arena_hard: 0.86
380	    tau_best_baseline_arena_hard: 0.84
381	    delta_tau_vs_best_baseline_mt_bench: 0.02
382	    delta_tau_vs_best_baseline_arena_hard: 0.02
383	    wilcoxon_gmfrm_vs_cyclicjudge_discard_p: 0.073
384	    wilcoxon_gmfrm_vs_sequential_p: 0.018
385	    wilcoxon_gmfrm_vs_raw_p: 0.001
386	    rank_changes_ge2_positions: 2
387	    top5_stability_raw_vs_gmfrm: 4/5 same
388	    top10_stability_raw_vs_gmfrm: 7/10 same
389	    max_rank_change_model: Model-X-70B
390	    max_rank_change_positions: 3
391	  result_rationale: 'Median档的核心tension在此实验体现：G-MFRM beats all baselines但margin modest。
392	    Δτ=+0.02 vs CyclicJudge+discard（best baseline），p=0.073——borderline significant。
393	    这是因为moderate contamination意味着contamination correction的marginal value有限： CyclicJudge+discard已经通过丢弃high-exposure
394	    items移除了大部分contamination signal， G-MFRM的优势在于保留这些items的information（不丢弃）而非dramatically改变ranking。
395	    vs sequential (p=0.018) 和 vs raw (p=0.001) 则显著，因为这些baseline完全不处理contamination。
396	    Rank changes limited to 2个models移动≥2位，最大移动3位（Model-X-70B: raw rank 7→fair rank
397	    10）， top-5有4/5不变——这限制了"G-MFRM dramatically corrects rankings"的narrative， 但支持"G-MFRM
398	    provides correction where needed + diagnostic visibility everywhere"的Ti
…[truncated 11406 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-21T22:38:36.811513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-21T22:38:37.318626+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-21T22:38:37.319110+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-21T22:38:37.723657+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-21T22:38:37.724192+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-21T22:38:38.077136+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-21T22:38:55.204477+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-21T22:38:55.610258+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-21T22:38:55.711206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-21T22:38:56.117386+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 406
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-21T22:38:56.168021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-21T22:38:57.080220+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 912
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-21T22:38:57.080632+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-21T22:38:57.534141+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-21T22:38:57.589539+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 105 · 2026-05-21T22:38:58.096561+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 106 · 2026-05-21T22:38:58.300380+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 710
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-21T22:38:58.709184+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 612
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-21T22:39:03.685806+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 109 · 2026-05-21T22:39:03.686233+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-21T22:39:04.391810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images/paper_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-21T22:39:04.998511+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1312
}
```

</details>

---


### Tool result

_source line 112 · 2026-05-21T22:39:05.003904+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1318
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-21T22:39:05.557626+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1165
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-21T22:43:46.920335+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1: Methods & Experiments Review\n\n**Paper**: \"Gated Many-Facet Rasch Model for Joint Judge Bias and Contamination Correction in LLM Evaluation\"\n**Venue**: EMNLP 2026 (ARR)\n**Tier**: Median (Tier B: moderate contamination regime)\n\n---\n\n### 1. Summary\n\nThe paper proposes G-MFRM, a three-stage psychometric framework that jointly estimates model ability, item difficulty, judge severity, and contamination susceptibility in LLM-as-a-judge evaluation. The core motivation is an omitted variable bias (OVB) observation: sequential correction of judge bias and contamination produces biased ability estimates when d_j and c_n·e_i are non-orthogonal. G-MFRM addresses this via a gating mechanism (c_n·e_i) within a Many-Facet Rasch Model, with e_i externally estimated from three indicator sources. Evaluated on MT-Bench (80 items), Arena-Hard (100 items), and WildBench (1024 items) with 8 judges and 22 target models, G-MFRM achieves Kendall τ = 0.87/0.86 with Chatbot Arena, numerically outperforming all 8 baselines but failing to achieve significance against the strongest (CyclicJudge+Discard: p = 0.073). The paper pivots to diagnostic outputs (per-model c_n, per-judge d_j) as the differentiating contribution.\n\n---\n\n### 2. Strengths\n\n- **Honest and thorough reporting**: The paper does not hide unfavorable results. The p = 0.073 vs CyclicJudge+Discard is reported plainly in Section 5.2. The 88% CI coverage (below nominal 95%) is acknowledged in Section 2.3 and Limitations. The 12 divergent transitions and R̂ = 1.07 for c_n are reported transparently in Table 5 and Section 5.1. This level of intellectual honesty is rare and commendable.\n\n- **Comprehensive experimental coverage**: The paper includes convergence diagnostics (Table 5), 8 baseline comparisons (Table 6), per-model/per-judge parameter estimates (Tables 7-8), contamination calibration vs synthetic scenarios (Table 9), ConStat external validation, rank change analysis (Table 10), judge count sensitivity (Table 11), exposure indicator ablation (Table 12), error propagation sensitivity (Table 13), facet fit diagnostics (Table 14), WildBench replication (Table 15), and adversarial robustness (Table 16). This is 16 tables across 12 experiments — exceptionally thorough.\n\n- **Error propagation analysis (Section 6.3, Table 13)**: Directly addresses the core methodological concern about staged estimation. Shows breakeven σ ≈ 0.38 with estimated pipeline noise σ = 0.15-0.20, providing a quantified safety margin. This is the right analysis to do and few papers include it.\n\n- **Synthetic c_n recovery with per-range breakdown (Section 2.3, Table 2)**: Reporting recovery RMSE and CI coverage separately for low/moderate/high contamination ranges is much more informative than a single aggregate number. It reveals that the model works best for low contamination (RMSE 0.12, 92% coverage) and struggles with high contamination (RMSE 0.18, 82% coverage).\n\n- **Graceful degradation well-characterized**: At J = 2, G-MFRM degrades to MFRM performance without harming results (Section 6.1, Table 11). At J = 5, it achieves significant improvement (p = 0.04). This provides clear practitioner guidance.\n\n- **Section 7 (Diagnostic Outputs discussion)** offers a genuinely valuable reframing: G-MFRM as an evaluation audit framework providing per-model c_n (training data audit), per-judge d_j (judge selection), and per-item e_i (item retirement). No other baseline provides all four. This is a unique and practical contribution.\n\n---\n\n### 3. Weaknesses\n\n**W1 [Major]** Core ranking correction claim is NOT statistically significant vs best baseline\n- Location: Section 5.2, Table 6\n- Evidence: G-MFRM τ = 0.87 vs CyclicJudge+Discard τ = 0.85, Δτ = +0.02, Wilcoxon p = 0.073. This is NOT significant at the conventional α = 0.05 threshold.\n- Impact: The paper's title says \"Contamination Correction,\" the abstract leads with \"G-MFRM achieves the highest agreement,\" and the methodology centers on joint estimation for ranking improvement. But the data shows the ranking improvement over the best heuristic alternative is not significant. The paper acknowledges this (Section 5.2: \"borderline significant\") and pivots to diagnostic outputs (Section 7), but the title/abstract/framing don't reflect this pivot. A reviewer scanning the abstract would believe the ranking improvement is the primary contribution, only to find it's unsupported at p < 0.05.\n- Note: G-MFRM IS significantly better than Sequential (p = 0.018), MFRM-only (p = 0.009), and Raw (p = 0.001). The issue is specifically vs CyclicJudge+Discard, which uses a simple heuristic (discard high-exposure items) that captures most of the contamination correction benefit without the MCMC overhead.\n- Suggestion: Reframe the primary contribution as diagnostic/interpretability (Section 7 material should be promoted), with ranking improvement as secondary. Or increase power by using more items/models (100 Arena-Hard items is small).\n\n**W2 [Major]** 95% CI coverage for c_n is only 88%, dropping to 82% for high-contamination models\n- Location: Section 2.3, Table 2, Limitations (page 12)\n- Evidence: Table 2 shows that for models with true c_n ∈ [0.8, 1.5], coverage drops to 82% (4 models). Overall coverage is 88%. Section 6.4 adds: \"Posterior predictive checks show 91.2% of residuals within the 90% prediction band, slightly below nominal.\"\n- Impact: The Bayesian credible intervals systematically underestimate uncertainty, especially for the models where contamination matters most. Table 7 reports per-model c_n with 95% CIs (e.g., Model-X-70B: c_n = 1.28 [0.85, 1.35]) — but if the true coverage is only 82% for such models, these intervals are misleadingly narrow. Any claim like \"this model's contamination is significantly above zero\" based on the CI excluding zero could be incorrect ~18% of the time (vs expected ~5%).\n- The root cause is clear: fixing e_i propagates uncertainty that the model doesn't account for. Section 6.3 shows the safety margin (1.9-2.5×), but this addresses θ̂ bias, not CI calibration.\n- Suggestion: (1) Report calibrated CIs (e.g., inflate by a correction factor derived from Table 2); (2) Or propagate e_i uncertainty via bootstrap/multiple imputation of e_i draws.\n\n**W3 [Major]** Convergence of c_n is marginal: R̂ = 1.07, ESS = 142, 12 divergent transitions\n- Location: Table 5, Section 5.1\n- Evidence: While R̂ = 1.07 is within the commonly cited 1.1 threshold and ESS = 142 > 100 (a minimal benchmark), these numbers indicate substantially weaker convergence for c_n than for all other facets (θ: R̂ = 1.03, ESS = 285; d: R̂ = 1.02, ESS = 340). The 12 divergent transitions (0.075%) indicate the NUTS sampler encountered problematic posterior geometry — high curvature regions where the Hamiltonian integration breaks down.\n- Impact: The paper correctly notes this is \"expected because moderate contamination produces more diffuse posteriors.\" But diffuse posteriors with divergent transitions raise the concern that the sampler is NOT fully exploring the posterior. Specifically: (a) are the 12 divergent transitions concentrated on specific high-c_n models? (b) if so, their c_n posterior means and CIs may be unreliable. The paper does not break down which parameters the divergent transitions are associated with.\n- Combined with W2 (under-coverage), the picture is concerning: c_n posteriors may be both poorly explored (divergent transitions) AND overconfident (88% coverage).\n- Suggestion: (1) Report which specific c_n parameters are affected by divergent transitions; (2) Run sensitivity analysis with different target_accept_prob (e.g., 0.99 instead of 0.95) to reduce divergences; (3) Try longer warmup or adapt_delta tuning.\n\n**W4 [Minor-to-Major]** 13.6% contamination facet misfit rate\n- Location: Table 14, Section 6.4\n- Evidence: 3 of 22 models have contamination facet MNSQ outside [0.7, 1.3]. The contamination facet has the highest misfit rate of all four facets.\n- Impact: These 3 models have contamination patterns that don't conform to the rank-1 structure c_n · e_i. If contamination is item-type-specific (e.g., coding contaminated but reasoning not), the model applies a uniform correction scaled by e_i that misrepresents the true contamination structure. For these 3 models, the fair score θ̂ could be biased in either direction. The paper argues \"no MNSQ exceeds 1.55, indicating misfit is not severe enough to invalidate the model\" — but this is a low bar, and doesn't address whether the misfitting models' θ̂ corrections are accurate.\n- Suggestion: Report whether the 3 misfitting models overlap with the models that have divergent transitions (W3) or under-covered CIs (W2). If the same models are flagged by multiple diagnostics, the estimates for those specific models may be unreliable.\n\n**W5 [Minor]** ConStat external validation ρ = 0.52 is modest\n- Location: Section 5.5, Table S5 equivalent\n- Evidence: ρ = 0.52 [0.31, 0.69] between G-MFRM c_n and ConStat per-model Δ. The CI lower bound (0.31) approaches weak correlation.\n- Impact: ConStat explains only ~27% of the variance in c_n. While the paper correctly notes these measure \"related but distinct constructs,\" for an external validation signal, ρ = 0.52 is supportive but not convincing. It cannot rule out the possibility that a substantial fraction of c_n captures model-specific artifacts rather than contamination.\n- Suggestion: Discuss what might explain the discrepancy: ConStat measures item-level performance gaps while c_n is a model-level susceptibility parameter — the aggregation mismatch may explain some decorrelation.\n\n**W6 [Minor]** WildBench replication lacks statistical test vs best baseline\n- Location: Table 15, Section 6.5\n- Evidence: G-MFRM τ = 0.84 vs CyclicJudge+Discard τ = 0.82, Δτ = +0.02. No p-value reported.\n- Impact: Given that the same Δτ = +0.02 on MT-Bench/Arena-Hard yields p = 0.073 (not significant), the WildBench result is likely also not significant. Omitting the p-value for the replication benchmark looks like selective reporting.\n- Suggestion: Report the WildBench p-value. If not significant, acknowledge it directly.\n\n**W7 [Minor]** Small evaluation scale limits statistical power\n- Location: Section 4.1\n- Evidence: 180 total items (80 MT-Bench + 100 Arena-Hard), 22 target models. For detecting Δτ = 0.02 effects, this may be underpowered.\n- Impact: The non-significance (p = 0.073) may partly reflect insufficient power rather than a truly small effect. A simple power analysis would clarify: given the observed effect size and variance, how many models/items would be needed for p < 0.05?\n- Suggestion: Include a post-hoc power analysis. If power is, say, 60% for detecting Δτ = 0.02, the non-significance is less damning.\n\n---\n\n### 4. Questions for Authors\n\nQ1. For the 12 divergent transitions in Table 5, which specific c_n parameters are involved? Do they overlap with the 3 misfitting models in Table 14 or the models with under-covered CIs in Table 2?\n\nQ2. If you inflate the c_n credible intervals to achieve empirical 95% coverage (as suggested by the 88% → 95% correction), do any of the per-model c_n conclusions change (e.g., does any model's CI now include zero)?\n\nQ3. CyclicJudge+Discard achieves τ = 0.85 with a simple discard heuristic and no MCMC overhead. Under what contamination regime (c_n median > ?) would G-MFRM's improvement become statistically significant? Can you extrapolate from the synthetic experiments?\n\nQ4. The internal consistency of the e_i composite is α = 0.62 (Section 3.4). How does this map to the estimated pipeline noise σ = 0.15-0.20 used in the error propagation analysis? Is the noise estimate derived from α, or are they independently estimated?\n\nQ5. The paper uses \"staged joint calibration\" to describe the method. Would a more accurate descriptor be \"conditional calibration\" (conditioning on pre-estimated e_i)? How do you respond to the concern that this is not truly \"joint\"?\n\n---\n\n### 5. Scores\n\n| Dimension | Score | Rationale |\n|-----------|-------|-----------|\n| **Soundness** | **3/5** (Acceptable) | The G-MFRM formulation is principled and the OVB observation is correctly applied. But: (1) the primary ranking claim is not significant vs best baseline (p=0.073), (2) posterior inference quality is questionable (88% CI coverage, 12 divergent transitions), (3) 13.6% contamination misfit suggests model misspecification for a non-trivial fraction. The method is sound in principle but the evidence doesn't fully validate it in practice. |\n| **Excitement** | **3/5** (Interesting) | The problem (OVB in sequential LLM evaluation correction) is important and timely. The psychometric approach is creative. The diagnostic outputs (Section 7) are a genuinely unique contribution. But the ranking improvement is not significant, the practical requirements (≥5 judges, 2.3h MCMC) are high, and the moderate contamination regime limits impact. |\n| **Reproducibility** | **3/5** (Could reproduce with some difficulty) | Method description is clear, MCMC configuration specified (4 chains, 2000 warmup, 4000 samples, target_accept=0.95), all baselines described. But: no code release mentioned, pipeline requires 8 LLM judge APIs + ConStat + vLLM deployment + 2.3h MCMC, total cost ~$820+118 GPU-hours. |\n| **Overall** | **2.5** (Borderline Findings) | The paper identifies a real problem (OVB) and proposes a principled solution (G-MFRM) with thorough experimental validation and commendably honest reporting. However, the primary claim (ranking correction) is not significant vs the strongest baseline, posterior inference has material quality issues (88% coverage, divergent transitions, 13.6% misfit), and the secondary contribution (diagnostic outputs) is not yet the paper's primary framing. With reframing and power improvements, this could reach Findings (3.0). |\n\n### 6. Confidence\n\n**4/5** — I read the full paper carefully, verified specific numbers against the convergence tables, cross-referenced the OVB formalization against standard econometrics, and assessed the statistical testing. I am familiar with Bayesian IRT/MCMC diagnostics and LLM-as-a-judge evaluation. My main uncertainty is whether the EMNLP community would weight the diagnostic contribution more generously than I have.\n\n---\n\n### Key Takeaway for Director\n\n这篇 median tier 论文的核心困境是：**方法论正确但数据不给力**。G-MFRM 的理论动机（OVB）成立，实验设计全面，报告诚实。但在 moderate contamination regime 下（c_n median=0.48），joint estimation 的 marginal value 有限——CyclicJudge+Discard 的简单启发式已经捕获了大部分 contamination correction benefit，剩余 Δτ=0.02 不足以跨越 significance threshold。\n\n如果作者将论文重新定位为**诊断工具**（per-model contamination audit + per-judge selection guidance）而非 ranking correction，同时增加数据规模以提升 statistical power，论文可以达到 Findings 水平（3.0）。当前版本的 framing mismatch（标题承诺 \"Correction\"，数据只支撑 \"Diagnosis\"）是最大的扣分点。",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1: Methods & Experiments Review\n\n**Paper**: \"Gated Many-Facet Rasch Model for Joint Judge Bias and Contamination Correction in LLM Evaluation\"\n**Venue**: EMNLP 2026 (ARR)\n**Tier**: Median (Tier B: moderate contamination regime)\n\n---\n\n### 1. Summary\n\nThe paper proposes G-MFRM, a three-stage psychometric framework that jointly estimates model ability, item difficulty, judge severity, and contamination susceptibility in LLM-as-a-judge evaluation. The core motivation is an omitted variable bias (OVB) observation: sequential correction of judge bias and contamination produces biased ability estimates when d_j and c_n·e_i are non-orthogonal. G-MFRM addresses this via a gating mechanism (c_n·e_i) within a Many-Facet Rasch Model, with e_i externally estimated from three indicator sources. Evaluated on MT-Bench (80 items), Arena-Hard (100 items), and WildBench (1024 items) with 8 judges and 22 target models, G-MFRM achieves Kendall τ = 0.87/0.86 with Chatbot Arena, numerically outperforming all 8 baselines but failing to achieve significance against the strongest (CyclicJudge+Discard: p = 0.073). The paper pivots to diagnostic outputs (per-model c_n, per-judge d_j) as the differentiating contribution.\n\n---\n\n### 2. Strengths\n\n- **Honest and thorough reporting**: The paper does not hide unfavorable results. The p = 0.073 vs CyclicJudge+Discard is reported plainly in Section 5.2. The 88% CI coverage (below nominal 95%) is acknowledged in Section 2.3 and Limitations. The 12 divergent transitions and R̂ = 1.07 for c_n are reported transparently in Table 5 and Section 5.1. This level of intellectual honesty is rare and commendable.\n\n- **Comprehensive experimental coverage**: The paper includes convergence diagnostics (Table 5), 8 baseline comparisons (Table 6), per-model/per-judge parameter estimates (Tables 7-8), contamination calibration vs synthetic scenarios (Table 9), ConStat external validation, rank change analysis (Table 10), judge count sensitivity (Table 11), exposure indicator ablation (Table 12), error propagation sensitivity (Table 13), facet fit diagnostics (Table 14), WildBench replication (Table 15), and adversarial robustness (Table 16). This is 16 tables across 12 experiments — exceptionally thorough.\n\n- **Error propagation analysis (Section 6.3, Table 13)**: Directly addresses the core methodological concern about staged estimation. Shows breakeven σ ≈ 0.38 with estimated pipeline noise σ = 0.15-0.20, providing a quantified safety margin. This is the right analysis to do and few papers include it.\n\n- **Synthetic c_n recovery with per-range breakdown (Section 2.3, Table 2)**: Reporting recovery RMSE and CI coverage separately for low/moderate/high contamination ranges is much more informative than a single aggregate number. It reveals that the model works best for low contamination (RMSE 0.12, 92% coverage) and struggles with high contamination (RMSE 0.18, 82% coverage).\n\n- **Graceful degradation well-characterized**: At J = 2, G-MFRM degrades to MFRM performance without harming results (Section 6.1, Table 11). At J = 5, it achieves significant improvement (p = 0.04). This provides clear practitioner guidance.\n\n- **Section 7 (Diagnostic Outputs discussion)** offers a genuinely valuable reframing: G-MFRM as an evaluation audit framework providing per-model c_n (training data audit), per-judge d_j (judge selection), and per-item e_i (item retirement). No other baseline provides all four. This is a unique and practical contribution.\n\n---\n\n### 3. Weaknesses\n\n**W1 [Major]** Core ranking correction claim is NOT statistically significant vs best baseline\n- Location: Section 5.2, Table 6\n- Evidence: G-MFRM τ = 0.87 vs CyclicJudge+Discard τ = 0.85, Δτ = +0.02, Wilcoxon p = 0.073. This is NOT significant at the conventional α = 0.05 threshold.\n- Impact: The paper's title says \"Contamination Correction,\" the abstract leads with \"G-MFRM achieves the highest agreement,\" and the methodology centers on joint estimation for ranking improvement. But the data shows the ranking improvement over the best heuristic alternative is not significant. The paper acknowledges this (Section 5.2: \"borderline significant\") and pivots to diagnostic outputs (Section 7), but the title/abstract/framing don't reflect this pivot. A reviewer scanning the abstract would believe the ranking improvement is the primary contribution, only to find it's unsupported at p < 0.05.\n- Note: G-MFRM IS significantly better than Sequential (p = 0.018), MFRM-only (p = 0.009), and Raw (p = 0.001). The issue is specifically vs CyclicJudge+Discard, which uses a simple heuristic (discard high-exposure items) that captures most of the contamination correction benefit without the MCMC overhead.\n- Suggestion: Reframe the primary contribution as diagnostic/interpretability (Section 7 material should be promoted), with ranking improvement as secondary. Or increase power by using more items/models (100 Arena-Hard items is small).\n\n**W2 [Major]** 95% CI coverage for c_n is only 88%, dropping to 82% for high-contamination models\n- Location: Section 2.3, Table 2, Limitations (page 12)\n- Evidence: Table 2 shows that for models with true c_n ∈ [0.8, 1.5], coverage drops to 82% (4 models). Overall coverage is 88%. Section 6.4 adds: \"Posterior predictive checks show 91.2% of residuals within the 90% prediction band, slightly below nominal.\"\n- Impact: The Bayesian credible intervals systematically underestimate uncertainty, especially for the models where contamination matters most. Table 7 reports per-model c_n with 95% CIs (e.g., Model-X-70B: c_n = 1.28 [0.85, 1.35]) — but if the true coverage is only 82% for such models, these intervals are misleadingly narrow. Any claim like \"this model's contamination is significantly above zero\" based on the CI excluding zero could be incorrect ~18% of the time (vs expected ~5%).\n- The root cause is clear: fixing e_i propagates uncertainty that the model doesn't account for. Section 6.3 shows the safety margin (1.9-2.5×), but this addresses θ̂ bias, not CI calibration.\n- Suggestion: (1) Report calibrated CIs (e.g., inflate by a correction factor derived from Table 2); (2) Or propagate e_i uncertainty via bootstrap/multiple imputation of e_i draws.\n\n**W3 [Major]** Convergence of c_n is marginal: R̂ = 1.07, ESS = 142, 12 divergent transitions\n- Location: Table 5, Section 5.1\n- Evidence: While R̂ = 1.07 is within the commonly cited 1.1 threshold and ESS = 142 > 100 (a minimal benchmark), these numbers indicate substantially weaker convergence for c_n than for all other facets (θ: R̂ = 1.03, ESS = 285; d: R̂ = 1.02, ESS = 340). The 12 divergent transitions (0.075%) indicate the NUTS sampler encountered problematic posterior geometry — high curvature regions where the Hamiltonian integration breaks down.\n- Impact: The paper correctly notes this is \"expected because moderate contamination produces more diffuse posteriors.\" But diffuse posteriors with divergent transitions raise the concern that the sampler is NOT fully exploring the posterior. Specifically: (a) are the 12 divergent transitions concentrated on specific high-c_n models? (b) if so, their c_n posterior means and CIs may be unreliable. The paper does not break down which parameters the divergent transitions are associated with.\n- Combined with W2 (under-coverage), the picture is concerning: c_n posteriors may be both poorly explored (divergent transitions) AND overconfident (88% coverage).\n- Suggestion: (1) Report which specific c_n parameters are affected by divergent transitions; (2) Run sensitivity analysis with different target_accept_prob (e.g., 0.99 instead of 0.95) to reduce divergences; (3) Try longer warmup or adapt_delta tuning.\n\n**W4 [Minor-to-Major]** 13.6% contamination facet misfit rate\n- Location: Table 14, Section 6.4\n- Evidence: 3 of 22 models have contamination facet MNSQ outside [0.7, 1.3]. The contamination facet has the highest misfit rate of all four facets.\n- Impact: These 3 models have contamination patterns that don't conform to the rank-1 structure c_n · e_i. If contamination is item-type-specific (e.g., coding contaminated but reasoning not), the model applies a uniform correction scaled by e_i that misrepresents the true contamination structure. For these 3 models, the fair score θ̂ could be biased in either direction. The paper argues \"no MNSQ exceeds 1.55, indicating misfit is not severe enough to invalidate the model\" — but this is a low bar, and doesn't address whether the misfitting models' θ̂ corrections are accurate.\n- Suggestion: Report whether the 3 misfitting models overlap with the models that have divergent transitions (W3) or under-covered CIs (W2). If the same models are flagged by multiple diagnostics, the estimates for those specific models may be unreliable.\n\n**W5 [Minor]** ConStat external validation ρ = 0.52 is modest\n- Location: Section 5.5, Table S5 equivalent\n- Evidence: ρ = 0.52 [0.31, 0.69] between G-MFRM c_n and ConStat per-model Δ. The CI lower bound (0.31) approaches weak correlation.\n- Impact: ConStat explains only ~27% of the variance in c_n. While the paper correctly notes these measure \"related but distinct constructs,\" for an external validation signal, ρ = 0.52 is supportive but not convincing. It cannot rule out the possibility that a substantial fraction of c_n captures model-specific artifacts rather than contamination.\n- Suggestion: Discuss what might explain the discrepancy: ConStat measures item-level performance gaps while c_n is a model-level susceptibility parameter — the aggregation mismatch may explain some decorrelation.\n\n**W6 [Minor]** WildBench replication lacks statistical test vs best baseline\n- Location: Table 15, Section 6.5\n- Evidence: G-MFRM τ = 0.84 vs CyclicJudge+Discard τ = 0.82, Δτ = +0.02. No p-value reported.\n- Impact: Given that the same Δτ = +0.02 on MT-Bench/Arena-Hard yields p = 0.073 (not significant), the WildBench result is likely also not significant. Omitting the p-value for the replication benchmark looks like selective reporting.\n- Suggestion: Report the WildBench p-value. If not significant, acknowledge it directly.\n\n**W7 [Minor]** Small evaluation scale limits statistical power\n- Location: Section 4.1\n- Evidence: 180 total items (80 MT-Bench + 100 Arena-Hard), 22 target models. For detecting Δτ = 0.02 effects, this may be underpowered.\n- Impact: The non-significance (p = 0.073) may partly reflect insufficient power rather than a truly small effect. A simple power analysis would clarify: given the observed effect size and variance, how many models/items would be needed for p < 0.05?\n- Suggestion: Include a post-hoc power analysis. If power is, say, 60% for detecting Δτ = 0.02, the non-significance is less damning.\n\n---\n\n### 4. Questions for Authors\n\nQ1. For the 12 divergent transitions in Table 5, which specific c_n parameters are involved? Do they overlap with the 3 misfitting models in Table 14 or the models with under-covered CIs in Table 2?\n\nQ2. If you inflate the c_n credible intervals to achieve empirical 95% coverage (as suggested by the 88% → 95% correction), do any of the per-model c_n conclusions change (e.g., does any model's CI now include zero)?\n\nQ3. CyclicJudge+Discard achieves τ = 0.85 with a simple discard heuristic and no MCMC overhead. Under what contamination regime (c_n median > ?) would G-MFRM's improvement become statistically significant? Can you extrapolate from the synthetic experiments?\n\nQ4. The internal consistency of the e_i composite is α = 0.62 (Section 3.4). How does this map to the estimated pipeline noise σ = 0.15-0.20 used in the error propagation analysis? Is the noise estimate derived from α, or are they independently estimated?\n\nQ5. The paper uses \"staged joint calibration\" to describe the method. Would a more accurate descriptor be \"conditional calibration\" (conditioning on pre-estimated e_i)? How do you respond to the concern that this is not truly \"joint\"?\n\n---\n\n### 5. Scores\n\n| Dimension | Score | Rationale |\n|-----------|-------|-----------|\n| **Soundness** | **3/5** (Acceptable) | The G-MFRM formulation is principled and the OVB observation is correctly applied. But: (1) the primary ranking claim is not significant vs best baseline (p=0.073), (2) posterior inference quality is questionable (88% CI coverage, 12 divergent transitions), (3) 13.6% contamination misfit suggests model misspecification for a non-trivial fraction. The method is sound in principle but the evidence doesn't fully validate it in practice. |\n| **Excitement** | **3/5** (Interesting) | The problem (OVB in sequential LLM evaluation correction) is important and timely. The psychometric approach is creative. The diagnostic outputs (Section 7) are a genuinely unique contribution. But the ranking improvement is not significant, the practical requirements (≥5 judges, 2.3h MCMC) are high, and the moderate contamination regime limits impact. |\n| **Reproducibility** | **3/5** (Could reproduce with some difficulty) | Method description is clear, MCMC configuration specified (4 chains, 2000 warmup, 4000 samples, target_accept=0.95), all baselines described. But: no code release mentioned, pipeline requires 8 LLM judge APIs + ConStat + vLLM deployment + 2.3h MCMC, total cost ~$820+118 GPU-hours. |\n| **Overall** | **2.5** (Borderline Findings) | The paper identifies a real problem (OVB) and proposes a principled solution (G-MFRM) with thorough experimental validation and commendably honest reporting. However, the primary claim (ranking correction) is not significant vs the strongest baseline, posterior inference has material quality issues (88% coverage, divergent transitions, 13.6% misfit), and the secondary contribution (diagnostic outputs) is not yet the paper's primary framing. With reframing and power improvements, this could reach Findings (3.0). |\n\n### 6. Confidence\n\n**4/5** — I read the full paper carefully, verified specific numbers against the convergence tables, cross-referenced the OVB formalization against standard econometrics, and assessed the statistical testing. I am familiar with Bayesian IRT/MCMC diagnostics and LLM-as-a-judge evaluation. My main uncertainty is whether the EMNLP community would weight the diagnostic contribution more generously than I have.\n\n---\n\n### Key Takeaway for Director\n\n这篇 median tier 论文的核心困境是：**方法论正确但数据不给力**。G-MFRM 的理论动机（OVB）成立，实验设计全面，报告诚实。但在 moderate contamination regime 下（c_n median=0.48），joint estimation 的 marginal value 有限——CyclicJudge+Discard 的简单启发式已经捕获了大部分 contamination correction benefit，剩余 Δτ=0.02 不足以跨越 significance threshold。\n\n如果作者将论文重新定位为**诊断工具**（per-model contamination audit + per-judge selection guidance）而非 ranking correction，同时增加数据规模以提升 statistical power，论文可以达到 Findings 水平（3.0）。当前版本的 framing mismatch（标题承诺 \"Correction\"，数据只支撑 \"Diagnosis\"）是最大的扣分点。",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-21T22:43:51.096768+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4176
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-21T22:43:56.868036+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-21T22:43:56.918836+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/median/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 118 · 2026-05-21T22:44:04.563471+00:00_

Median tier 审稿完成。

核心发现：方法论正确（OVB 动机成立、G-MFRM 设计合理）但在 moderate contamination regime 下数据不支撑 ranking correction 的 primary claim——vs 最强 baseline CyclicJudge+Discard 仅 Δτ=0.02, p=0.073（不显著）。c_n 收敛边缘（R̂=1.07, ESS=142, 12 divergent transitions），95% CI coverage 仅 88%（高 contamination 模型更低至 82%），13.6% contamination facet misfit。建议重新定位为诊断工具（per-model c_n audit + per-judge selection guidance），给出 Overall 2.5 (Borderline Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 5

## Round 5

4 recorded events


### User

_source line 119 · 2026-05-21T22:44:05.669783+00:00_

[Round 2 审稿请求]:
[交叉分享 - Round 2] 以下是 Reviewer 2 对修订版论文（Dream 20260521T215715）的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## R2 审稿报告：Novelty + Related Work + Story 一致性

**Overall: 3.5 (Borderline Conference)**

**一句话总结**: 问题识别精准、叙事逻辑自洽、实验设计覆盖全面，但核心 novelty 是已有技术（OVB + DG-IRT + MFRM）的领域迁移，且 "first" claim 仅覆盖 NLP 文献而未排除教育测量学中已有的 rater×DIF 联合建模工作。

## 官方维度打分

| 维度 | 分数 |
|------|------|
| Soundness | 4/5 |
| Excitement | 3/5 |

## Must-Fix 问题

**M1** [idea 层面] "first" claim 的文献覆盖范围不足——仅扫描了 NLP 文献，未排除教育测量学中已有的 rater effects × item exposure 联合建模
- Section 7 Gap 段声称 "Among the 12 surveyed papers...none jointly models both"，但扫描范围仅为 NLP 文献
- 教育测量学中已有类似工作：Eckes (2011) MFRM+DIF、Patz et al. (2002) hierarchical rater model、Fox & Glas (2001) Bayesian IRT with DIF
- 如果这些工作已解决类似 "rater bias + item-level confound" 联合建模，G-MFRM 的 novelty 将降级为 domain adaptation
- 建议：精确区分（如 DIF 假设 known group membership vs G-MFRM 用 continuous latent exposure），改 "first" 为更精确的限定表述

## Should-Fix 问题

**S1** OVB Observation 仍被列为独立贡献，overweight 了已知结果的领域应用。建议表述为 "domain identification + empirical quantification" 而非 "theoretical formalization"。

**S2** "12 surveyed papers" 与实际讨论的 8-9 篇不匹配。

**S3** "staged joint" 与 "joint calibration" 的用语张力——建议在 Section 3 开头增加明确声明。

## Presentation 问题

**P1** Arena-Hard 原始论文未引用
**P2** DG-IRT 原始出处应归属 Robitzsch (2020)，而非仅引 Doehler et al. (2024)
**P3** References 数量 ~15 篇仍偏少（应 30-50）

## Story 一致性评估
叙事逻辑自洽，无重大矛盾。每个 claim 都有对应实验支撑。唯一轻微张力：标题 "Joint Calibration" vs staged 实质（S3 已标注）。

## Novelty 排序
G-MFRM 三阶段 pipeline > 实验设计与实证分析 > OVB Observation（最低）。属 "system contribution" 而非 "model innovation"。

## 主要优势
1. 叙事逻辑高度自洽
2. Rank Change Analysis（Section 5.2）是亮点——将 Δτ 转化为具体决策影响
3. Error propagation analysis（Section 6.4）主动回应 staged estimation 质疑
4. OVB 诚实 framing（Observation + 引用原始来源）
5. ConStat external validation（ρ=0.82）提供独立校验

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-21T22:45:39.135843+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 对 R2 审稿意见的交叉回应（Dream 20260521T215715）\n\n**注意**：R2 审稿基于 best tier（ConStat ρ=0.82, Soundness 4/5, Overall 3.5），我最近一轮审稿基于 median tier（ConStat ρ=0.52, Soundness 3/5, Overall 2.5）。以下回应以 R2 的评审对象（best tier）为准，但在关键处标注 tier 差异。\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-M1: \"first\" claim 文献覆盖范围不足**\n\n同意且认为这是一个有价值的发现。R2 指出教育测量学中已有 rater effects × item-level confound 联合建模的先验工作（Eckes 2011 MFRM+DIF, Patz et al. 2002, Fox & Glas 2001），这些在论文的文献扫描中完全缺失。\n\n不过我认为 R2 同时也给出了解决路径：DIF 与 G-MFRM 的核心技术差异确实存在——\n- 经典 DIF 假设 **known group membership**（如性别、种族），而 G-MFRM 的 exposure e_i 是从外部信号 **连续估计** 的潜变量\n- DIF 检测的是 item-level 差异功能，G-MFRM 的 gating 机制 c_n · e_i 是 **model-level susceptibility × item-level exposure** 的乘积结构\n- DIF 是诊断工具（标记异常 items），G-MFRM 的 c_n 是在模型层面估计 contamination magnitude\n\n但这些区别需要论文**明确阐述**。当前 Section 7 仅扫描 NLP 文献就声称 \"first\" 是不充分的。建议：(1) 加入对 Eckes (2011) 和 Fox & Glas (2001) 的讨论；(2) 将 \"first framework\" 改为 \"first framework in the LLM evaluation literature that adapts continuous-exposure gating to the multi-judge contamination setting\"——精确限定范围。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-S1: OVB Observation 不应被列为独立贡献**\n\n同意。Best tier 论文在 Section 2.1 使用了\"Observation\"（而非\"Proposition\"）并引用了 Angrist & Pischke (2009) 作为来源，这一 framing 本身是诚实的。但在 Introduction 的 contribution list 中，如果 OVB observation 被作为三个贡献之一并列，则仍然给人 overweight 的感觉。\n\nR2 的建议精准：将表述从 \"we formalize the OVB problem\" 改为 \"we **identify** that the OVB problem **applies to** LLM evaluation and **empirically quantify** its magnitude (43.2% RMSE degradation at ρ=0.6)\"。这既保留了 claim 的实质，又不过度包装已知结果的领域迁移。\n\n**[AGREE] R2-S2: \"12 surveyed papers\" 与实际讨论数量不匹配**\n\n同意。这是一个可快速修复的 factual 问题。Section 7 (Related Work) 的 Gap 段声称 survey 了 12 篇论文，但正文中实际详细讨论的仅 8-9 篇。作者应核实并统一数字，或在 appendix 中列出完整的 12 篇 survey list。\n\n**[AGREE] R2-S3: \"staged joint\" 与 \"joint calibration\" 的用语张力**\n\n同意，与我 best-tier review 中的 W3 以及 median-tier review 中的 Q5 一致。这已是三轮审稿中反复出现的 consensus issue。\n\nBest tier 论文在 Abstract 使用了 \"a staged joint calibration framework\"（\"staged\" 限定词存在），Section 3.3 明确说明 \"estimation of ability, difficulty, severity, and contamination is joint within Stage 3, while exposure is pre-anchored.\" 这些说明在细读时可以找到，但标题中的\"Joint Calibration\"仍可能误导快速阅读的读者。\n\n具体建议：在 Section 3 的 Stage 3 描述开头加入一句明确声明：\"**Terminology note**: We use 'joint calibration' to refer to the simultaneous estimation of {θ, b, d, c} in Stage 3. The exposure indicator e_i is externally estimated in Stage 2 and treated as fixed in Stage 3; it is not jointly estimated. See Section 6.3 for error propagation analysis of this design choice.\"\n\n---\n\n### Presentation 问题\n\n**[AGREE] R2-P1: Arena-Hard 原始论文未引用**\n同意。论文在 Section 4.1 使用 Arena-Hard 作为两个核心 benchmark 之一，但未引用其原始论文。同理 WildBench（Section 6.5 使用但可能也未引用原始论文）。这些是基础 citation hygiene 问题。\n\n**[PARTIALLY AGREE] R2-P2: DG-IRT 原始出处归属**\n部分同意。需确认论文是否引用了 Robitzsch (2020) 原始 DG-IRT 论文。如果只引用了 Doehler et al. (2024)（一个应用型引用），则应补充 Robitzsch (2020) 作为方法的原始来源。但如果论文已引用 Robitzsch（我在 best tier 论文的 References 中看到了 \"A. Robitzsch. DG-IRT: Differential group item response theory. JEBS, 45(6), 2020.\"），则此问题不成立。需要核实 best tier 论文的 reference list。\n\n**[AGREE] R2-P3: References 数量~15 篇仍偏少**\n强烈同意。这是跨越全部审稿轮次的 persistent issue（我在首轮 review 标记为 N4 critical，R2 在首轮和本轮都标记）。一篇跨四个领域（judge bias, contamination, psychometrics, Bayesian estimation）的论文引用 15 篇是远远不够的，目标应为 30-40 篇。\n\n---\n\n### 对 R2 Novelty 排序和 Overall 评分的看法\n\n**Novelty 排序**：R2 将 novelty 排序为 \"G-MFRM 三阶段 pipeline > 实验设计与实证分析 > OVB Observation（最低）\"，归类为 \"system contribution\" 而非 \"model innovation\"。\n\n我基本同意。G-MFRM 的贡献确实更偏 system（将已有组件——MFRM, DG-IRT gating, external exposure estimation——组合成一个有效的 pipeline）而非 fundamental model innovation。但我会补充：**系统级贡献在 EMNLP 中是被认可的**，只要实验验证充分且实际价值明确。关键在于论文是否正确定位了自己的贡献类型——当前的 framing 偏向 model innovation（\"we propose G-MFRM\"），而实际贡献更像 system（\"we assemble and validate a pipeline\"）。\n\n**Overall 评分差异**：R2 给 best tier 3.5（Borderline Conference），我给 best tier 同样的论文 3.5（Borderline Conference，来自我的第二轮 dream review）。评分一致。\n\n我给 median tier 2.5（Borderline Findings），主要因为 median tier 数据更弱（p=0.073 vs best baseline, ConStat ρ=0.52, 88% CI coverage, 12 divergent transitions）。如果 R2 审 median tier，我预计其评分也会低于 3.5。\n\n---\n\n### Consensus Issues（R1 + R2 across tiers）\n\n| Issue | R1 | R2 | Status |\n|-------|----|----|--------|\n| \"Joint\" framing vs staged 实质 | R1-W3 (best), R1-Q5 (median) | R2-S3 | **Strong consensus** — 三轮审稿反复出现 |\n| References 不足 | R1-N4 (首轮), R1 notes (后续) | R2-P3 | **Strong consensus** |\n| \"first\" claim 需更精确限定 | R1 未独立提出 | R2-M1 | R2 独立发现，R1 同意 |\n| OVB Observation overweight | R1-N2 (首轮) | R2-S1 | **Consensus** |\n| 诊断贡献 vs 排名校正的 framing 定位 | R1 median W1 (primary claim not significant) | R2 novelty assessment (system contribution) | **Aligned** — 两位 reviewer 都认为论文应更突出诊断贡献 |\n\n**给 Director 的核心建议**：\n- Best tier 论文在 3.0-3.5 区间（Findings 至 Borderline Conference），主要取决于是否修复 \"first\" claim 限定（R2-M1）和 \"joint\" framing（共识问题）\n- Median tier 论文在 2.5 区间（Borderline Findings），核心瓶颈是 p=0.073 vs best baseline 和 posterior inference 质量——这些是数据/regime 层面的限制，非方法论缺陷\n- 跨 tier 一致的 actionable feedback：(1) 重新定位为\"诊断+校正\"而非纯\"校正\"；(2) 扩充 references；(3) 精确限定 \"first\" claim；(4) 明确 \"staged joint\" 术语",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 对 R2 审稿意见的交叉回应（Dream 20260521T215715）\n\n**注意**：R2 审稿基于 best tier（ConStat ρ=0.82, Soundness 4/5, Overall 3.5），我最近一轮审稿基于 median tier（ConStat ρ=0.52, Soundness 3/5, Overall 2.5）。以下回应以 R2 的评审对象（best tier）为准，但在关键处标注 tier 差异。\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-M1: \"first\" claim 文献覆盖范围不足**\n\n同意且认为这是一个有价值的发现。R2 指出教育测量学中已有 rater effects × item-level confound 联合建模的先验工作（Eckes 2011 MFRM+DIF, Patz et al. 2002, Fox & Glas 2001），这些在论文的文献扫描中完全缺失。\n\n不过我认为 R2 同时也给出了解决路径：DIF 与 G-MFRM 的核心技术差异确实存在——\n- 经典 DIF 假设 **known group membership**（如性别、种族），而 G-MFRM 的 exposure e_i 是从外部信号 **连续估计** 的潜变量\n- DIF 检测的是 item-level 差异功能，G-MFRM 的 gating 机制 c_n · e_i 是 **model-level susceptibility × item-level exposure** 的乘积结构\n- DIF 是诊断工具（标记异常 items），G-MFRM 的 c_n 是在模型层面估计 contamination magnitude\n\n但这些区别需要论文**明确阐述**。当前 Section 7 仅扫描 NLP 文献就声称 \"first\" 是不充分的。建议：(1) 加入对 Eckes (2011) 和 Fox & Glas (2001) 的讨论；(2) 将 \"first framework\" 改为 \"first framework in the LLM evaluation literature that adapts continuous-exposure gating to the multi-judge contamination setting\"——精确限定范围。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-S1: OVB Observation 不应被列为独立贡献**\n\n同意。Best tier 论文在 Section 2.1 使用了\"Observation\"（而非\"Proposition\"）并引用了 Angrist & Pischke (2009) 作为来源，这一 framing 本身是诚实的。但在 Introduction 的 contribution list 中，如果 OVB observation 被作为三个贡献之一并列，则仍然给人 overweight 的感觉。\n\nR2 的建议精准：将表述从 \"we formalize the OVB problem\" 改为 \"we **identify** that the OVB problem **applies to** LLM evaluation and **empirically quantify** its magnitude (43.2% RMSE degradation at ρ=0.6)\"。这既保留了 claim 的实质，又不过度包装已知结果的领域迁移。\n\n**[AGREE] R2-S2: \"12 surveyed papers\" 与实际讨论数量不匹配**\n\n同意。这是一个可快速修复的 factual 问题。Section 7 (Related Work) 的 Gap 段声称 survey 了 12 篇论文，但正文中实际详细讨论的仅 8-9 篇。作者应核实并统一数字，或在 appendix 中列出完整的 12 篇 survey list。\n\n**[AGREE] R2-S3: \"staged joint\" 与 \"joint calibration\" 的用语张力**\n\n同意，与我 best-tier review 中的 W3 以及 median-tier review 中的 Q5 一致。这已是三轮审稿中反复出现的 consensus issue。\n\nBest tier 论文在 Abstract 使用了 \"a staged joint calibration framework\"（\"staged\" 限定词存在），Section 3.3 明确说明 \"estimation of ability, difficulty, severity, and contamination is joint within Stage 3, while exposure is pre-anchored.\" 这些说明在细读时可以找到，但标题中的\"Joint Calibration\"仍可能误导快速阅读的读者。\n\n具体建议：在 Section 3 的 Stage 3 描述开头加入一句明确声明：\"**Terminology note**: We use 'joint calibration' to refer to the simultaneous estimation of {θ, b, d, c} in Stage 3. The exposure indicator e_i is externally estimated in Stage 2 and treated as fixed in Stage 3; it is not jointly estimated. See Section 6.3 for error propagation analysis of this design choice.\"\n\n---\n\n### Presentation 问题\n\n**[AGREE] R2-P1: Arena-Hard 原始论文未引用**\n同意。论文在 Section 4.1 使用 Arena-Hard 作为两个核心 benchmark 之一，但未引用其原始论文。同理 WildBench（Section 6.5 使用但可能也未引用原始论文）。这些是基础 citation hygiene 问题。\n\n**[PARTIALLY AGREE] R2-P2: DG-IRT 原始出处归属**\n部分同意。需确认论文是否引用了 Robitzsch (2020) 原始 DG-IRT 论文。如果只引用了 Doehler et al. (2024)（一个应用型引用），则应补充 Robitzsch (2020) 作为方法的原始来源。但如果论文已引用 Robitzsch（我在 best tier 论文的 References 中看到了 \"A. Robitzsch. DG-IRT: Differential group item response theory. JEBS, 45(6), 2020.\"），则此问题不成立。需要核实 best tier 论文的 reference list。\n\n**[AGREE] R2-P3: References 数量~15 篇仍偏少**\n强烈同意。这是跨越全部审稿轮次的 persistent issue（我在首轮 review 标记为 N4 critical，R2 在首轮和本轮都标记）。一篇跨四个领域（judge bias, contamination, psychometrics, Bayesian estimation）的论文引用 15 篇是远远不够的，目标应为 30-40 篇。\n\n---\n\n### 对 R2 Novelty 排序和 Overall 评分的看法\n\n**Novelty 排序**：R2 将 novelty 排序为 \"G-MFRM 三阶段 pipeline > 实验设计与实证分析 > OVB Observation（最低）\"，归类为 \"system contribution\" 而非 \"model innovation\"。\n\n我基本同意。G-MFRM 的贡献确实更偏 system（将已有组件——MFRM, DG-IRT gating, external exposure estimation——组合成一个有效的 pipeline）而非 fundamental model innovation。但我会补充：**系统级贡献在 EMNLP 中是被认可的**，只要实验验证充分且实际价值明确。关键在于论文是否正确定位了自己的贡献类型——当前的 framing 偏向 model innovation（\"we propose G-MFRM\"），而实际贡献更像 system（\"we assemble and validate a pipeline\"）。\n\n**Overall 评分差异**：R2 给 best tier 3.5（Borderline Conference），我给 best tier 同样的论文 3.5（Borderline Conference，来自我的第二轮 dream review）。评分一致。\n\n我给 median tier 2.5（Borderline Findings），主要因为 median tier 数据更弱（p=0.073 vs best baseline, ConStat ρ=0.52, 88% CI coverage, 12 divergent transitions）。如果 R2 审 median tier，我预计其评分也会低于 3.5。\n\n---\n\n### Consensus Issues（R1 + R2 across tiers）\n\n| Issue | R1 | R2 | Status |\n|-------|----|----|--------|\n| \"Joint\" framing vs staged 实质 | R1-W3 (best), R1-Q5 (median) | R2-S3 | **Strong consensus** — 三轮审稿反复出现 |\n| References 不足 | R1-N4 (首轮), R1 notes (后续) | R2-P3 | **Strong consensus** |\n| \"first\" claim 需更精确限定 | R1 未独立提出 | R2-M1 | R2 独立发现，R1 同意 |\n| OVB Observation overweight | R1-N2 (首轮) | R2-S1 | **Consensus** |\n| 诊断贡献 vs 排名校正的 framing 定位 | R1 median W1 (primary claim not significant) | R2 novelty assessment (system contribution) | **Aligned** — 两位 reviewer 都认为论文应更突出诊断贡献 |\n\n**给 Director 的核心建议**：\n- Best tier 论文在 3.0-3.5 区间（Findings 至 Borderline Conference），主要取决于是否修复 \"first\" claim 限定（R2-M1）和 \"joint\" framing（共识问题）\n- Median tier 论文在 2.5 区间（Borderline Findings），核心瓶颈是 p=0.073 vs best baseline 和 posterior inference 质量——这些是数据/regime 层面的限制，非方法论缺陷\n- 跨 tier 一致的 actionable feedback：(1) 重新定位为\"诊断+校正\"而非纯\"校正\"；(2) 扩充 references；(3) 精确限定 \"first\" claim；(4) 明确 \"staged joint\" 术语",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-21T22:45:43.672553+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4536
}
```

</details>

---


### Assistant

_source line 122 · 2026-05-21T22:45:48.309411+00:00_

交叉回应已提交。R1 与 R2 在五个核心问题上达成 consensus：(1) "joint" framing 需明确化；(2) references 严重不足；(3) "first" claim 需精确限定；(4) OVB 贡献不应 overweight；(5) 论文应更突出诊断贡献定位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 6

## Round 6

4 recorded events


### User

_source line 123 · 2026-05-21T22:49:22.922806+00:00_

[Round 2 审稿请求]:
请暂停 median 场景的审稿，先完成 best 场景的交叉回应。

以下是 Reviewer 2 对 best 场景（Dream 20260521T215715/best）的完整审稿意见：

---

**Overall: 3.5 (Borderline Conference)**

**Must-Fix (1 项)**:
1. "First" claim scope — 论文声称是"首个"联合处理 judge bias 和 contamination 的工作，但需要仔细限定范围。先前已有 judge calibration 工作（Zheng et al. 2023, Li et al. 2024），真正的新颖性在于 joint IRT formulation，而非同时处理这两个问题本身。

**Should-Fix (3 项)**:
2. Arena circularity — 用 Chatbot Arena Elo 作为主要外部基准，而 Arena 本身使用 LLM judge，存在循环风险。应明确承认此局限并讨论 ConStat 验证如何部分缓解。
3. "Joint" title expectation mismatch — 标题说"joint calibration"但模型是三阶段 sequential pipeline。技术上可辩护（calibration outcome 是 joint 的），但会误导读者期待单一联合后验。建议改为"unified"或"integrated"。
4. Writing quality — 部分段落过于冗长，可压缩。

**Presentation Issues (3 项)**:
5. Rank-change analysis 缺失 — 缺少去污染前后模型排名变化的分析。
6. Stage 2→3 连接不够清晰 — ConStat exposure estimates 如何作为 fixed input vs latent variable 被消费需要更清楚的说明。
7. Related work coverage — 需要更全面地覆盖 LLM judge bias 和 contamination detection 的先前工作。

**Strengths**:
- 新颖的 IRT 框架整合，方法论上有原则性
- 相比 Round 1 有实质性改进
- τ=0.91, AUC=0.94, r=0.82 结果强劲
- OVB 动机清晰有说服力

---

请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-21T22:50:31.386835+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 对 R2 Best 场景审稿意见的交叉回应（Dream 20260521T215715/best）\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-Must-Fix-1: \"First\" claim 需精确限定范围**\n\n同意。论文声称\"首个联合处理 judge bias 和 contamination 的框架\"，但如 R2 所指，先前已有部分处理这两个问题的工作：\n- Zheng et al. (2023) 的 MT-Bench 框架已包含 judge calibration 维度\n- Li et al. (2024) 的 UDA 通过 neural K-factor 调整 inter-judge variance\n- CyclicJudge+Discard 组合策略也同时处理了 bias（CyclicJudge）和 contamination（Discard 高曝光 items）\n\nR2 正确指出真正的新颖性不在于\"同时处理两个问题\"（这已有先例），而在于 **joint IRT formulation**——在单一心理测量模型中联合估计 d_j 和 c_n·e_i，避免 OVB。这一区分至关重要。\n\n建议将 claim 修改为：\"G-MFRM is the first **IRT-based framework** that **jointly estimates** judge severity and contamination susceptibility within a single psychometric model, avoiding the omitted variable bias inherent in sequential or heuristic approaches.\" 这比泛泛的\"first to address both problems\"更精确且更可辩护。\n\n---\n\n### Should-Fix\n\n**[PARTIALLY AGREE] R2-Should-Fix-2: Arena circularity**\n\n部分同意，但认为 R2 对 circularity 风险的评估偏高。\n\nR2 称\"Arena 本身使用 LLM judge\"——这需要澄清。Chatbot Arena 的核心排名机制是**人类用户的实时 pairwise 比较**，不是 LLM judge。用户在 Arena 中对两个匿名模型的输出做偏好选择，Elo 排名由这些人类投票计算。因此 Arena Elo 与 LLM-as-a-judge 评估之间没有直接的 judge 重叠——benchmark contamination（记忆特定 test items）不会直接影响 Arena 中面对全新用户 prompts 的表现。\n\n但我同意 R2 的两个有效子点：\n1. Arena 不完全独立——热门模型可能获得更多曝光和用户偏好（popularity bias）\n2. 如果 contaminated 模型在 benchmark 上训练后也间接提升了 Arena 场景下的能力（泛化效应），则存在间接 circularity\n\n论文 Limitations section 应明确讨论这些。ConStat 验证（ρ=0.82，best tier）确实部分缓解了 circularity 问题，因为 ConStat 是独立于 Arena 的 contamination 测量。建议在 Limitations 中增加一段：\"While Chatbot Arena rankings are based on human votes rather than LLM judges, they are not fully independent of benchmark performance—models with strong benchmark scores may attract more Arena users. The ConStat external validation (ρ=0.82) provides an Arena-independent check on c_n estimates.\"\n\n**[AGREE] R2-Should-Fix-3: \"Joint\" title expectation mismatch**\n\n同意。这是跨所有审稿轮次和 reviewer 的**最强共识问题**——我在首轮 review（R1-N1 critical）、best-tier review（W3）、median-tier review（Q5）都独立标记了此问题。R2 在首轮和本轮也标记。\n\nR2 的建议\"改为 unified 或 integrated\"是合理的替代方案。我对三个选项的优劣评估：\n- **\"Joint Calibration\"**（当前）：技术上可辩护（Stage 3 内部确实是 joint），但 misleading\n- **\"Unified Calibration\"**：暗示一个统一框架但不承诺单一后验，更准确\n- **\"Integrated Calibration\"**：暗示多个组件的整合，与三阶段 pipeline 一致\n- **\"Staged Joint Calibration\"**（Abstract 已用）：最精确但标题中过于冗长\n\n我推荐 **\"Unified\"** 或 **\"Integrated\"** 用于标题，**\"staged joint\"** 保留在正文描述中。\n\n**[AGREE] R2-Should-Fix-4: Writing quality — 部分段落可压缩**\n\n同意但视为 minor。Best tier 论文的写作整体清晰，Section 2（OVB motivation）和 Section 5（Results）的叙事流畅。如果有特定过长段落，R2 应指出具体位置。作为通用建议，Section 6（Analysis）的各子节可考虑合并或精简以腾出空间给 figures（目前全文零 figures 是独立的 presentation 问题）。\n\n---\n\n### Presentation Issues\n\n**[REBUT] R2-Presentation-5: Rank-change analysis 缺失**\n\n不同意。Best tier 论文**包含 rank change analysis**：\n- Table 3（Section 5.2）明确报告了 per-model rank changes：Qwen3-235B-A22B 从 raw rank 3 → G-MFRM rank 7（-4 positions, c_n=1.82），Llama 4 Maverick 从 5→8（-3），Model-X-70B 从 8→5（+3），Claude Sonnet 4.6 从 4→2（+2）\n- 论文报告了 5 个模型移动 ≥2 positions、2 个移动 ≥3、top-5 有 2 个交换\n- Fig 4（如果存在于 YAML 设计中）是 bump chart 展示排名流向，但实际论文中零 figures，因此视觉化确实缺失\n\nR2 可能因为论文缺少**图表形式**的 rank change 可视化（如 bump chart 或 alluvial diagram）而误判为\"缺失\"。数据本身在 Table 3 中，但没有 figure 辅助确实降低了可读性。因此：rank change **分析**存在，rank change **可视化**缺失。后者属于我已标记的零 figures 问题（W6/N2）。\n\n**[AGREE] R2-Presentation-6: Stage 2→3 连接说明不足**\n\n同意。Section 3.3 描述了三阶段 pipeline，但 e_i 从 Stage 2 输出到 Stage 3 输入的**具体操作方式**可以更明确：\n- e_i 是作为 fixed point estimate 传入 Stage 3？还是作为 distribution？\n- 如果是 fixed point，其不确定性如何处理？（答案：不处理，这是 Section 6.4 error propagation 分析的动机）\n- Stage 2 的 weighted composite 公式（各 source 权重如何确定）在 Section 3.2 中描述了\"weighted combining\"但未给出具体权重公式\n\n建议在 Section 3.3 Stage 3 开头增加明确连接：\"Stage 3 receives e_i as a fixed point estimate from Stage 2. Uncertainty in e_i is not propagated into the Stage 3 posterior; instead, we quantify the impact of e_i noise through the sensitivity analysis in Section 6.3.\"\n\n**[AGREE] R2-Presentation-7: Related work coverage 不足**\n\n同意，与全部审稿轮次的共识一致。~15 篇 references 对于一篇跨 judge bias、contamination、psychometrics、Bayesian estimation 领域的论文严重不足。这一问题在首轮即被标记（R1-N4, R2-N2），修订版未充分改善。\n\n---\n\n### 对 R2 Strengths 评估的回应\n\nR2 列出的四个优势我全部同意：\n1. **IRT 框架整合有原则性**：G-MFRM 的 gating mechanism 是对 DG-IRT 的 principled adaptation\n2. **相比 Round 1 有实质性改进**：从首轮的单栏格式+10 篇引用，到现在的 ACL 双栏+12 个实验+error propagation 分析\n3. **τ=0.91, AUC=0.94, r=0.82 结果强劲**：best tier 的实验结果在数值上有说服力\n4. **OVB 动机清晰**：使用\"Observation\"而非\"Proposition\"，引用 Angrist & Pischke (2009)，是诚实的 framing\n\n---\n\n### 评分对照\n\n| 维度 | R1 (best tier) | R2 (best tier) | 差异分析 |\n|------|---------------|---------------|---------|\n| Soundness | 4/5 | 4/5 | **一致** |\n| Excitement | 3/5 | 3/5 | **一致** |\n| Overall | 3.5 | 3.5 | **一致** |\n\nR1 和 R2 对 best tier 的评分完全一致（Soundness 4, Excitement 3, Overall 3.5）。主要分歧在于 weakness 的分类方式：\n- R2 将 \"first claim\" 作为唯一 Must-Fix，而 R1 将 \"joint framing\"、\"missing CIs\"、\"零 figures\" 作为主要问题\n- 这说明两位 reviewer 从不同角度（R2: novelty/positioning; R1: evidence/presentation）得出了相同的总体评估\n\n**共识 actionable items（best tier）**：\n1. 精确限定\"first\"claim → \"first IRT-based joint estimation in LLM evaluation\"\n2. 标题\"Joint\"改为\"Unified\"或\"Integrated\"\n3. 扩充 references 至 30+\n4. 在 Section 3.3 明确 e_i 作为 fixed input 的处理方式和理由\n5. 加入至少 3-4 个关键 figures（framework overview, rank change visualization, ConStat scatter, sensitivity curves）",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 对 R2 Best 场景审稿意见的交叉回应（Dream 20260521T215715/best）\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-Must-Fix-1: \"First\" claim 需精确限定范围**\n\n同意。论文声称\"首个联合处理 judge bias 和 contamination 的框架\"，但如 R2 所指，先前已有部分处理这两个问题的工作：\n- Zheng et al. (2023) 的 MT-Bench 框架已包含 judge calibration 维度\n- Li et al. (2024) 的 UDA 通过 neural K-factor 调整 inter-judge variance\n- CyclicJudge+Discard 组合策略也同时处理了 bias（CyclicJudge）和 contamination（Discard 高曝光 items）\n\nR2 正确指出真正的新颖性不在于\"同时处理两个问题\"（这已有先例），而在于 **joint IRT formulation**——在单一心理测量模型中联合估计 d_j 和 c_n·e_i，避免 OVB。这一区分至关重要。\n\n建议将 claim 修改为：\"G-MFRM is the first **IRT-based framework** that **jointly estimates** judge severity and contamination susceptibility within a single psychometric model, avoiding the omitted variable bias inherent in sequential or heuristic approaches.\" 这比泛泛的\"first to address both problems\"更精确且更可辩护。\n\n---\n\n### Should-Fix\n\n**[PARTIALLY AGREE] R2-Should-Fix-2: Arena circularity**\n\n部分同意，但认为 R2 对 circularity 风险的评估偏高。\n\nR2 称\"Arena 本身使用 LLM judge\"——这需要澄清。Chatbot Arena 的核心排名机制是**人类用户的实时 pairwise 比较**，不是 LLM judge。用户在 Arena 中对两个匿名模型的输出做偏好选择，Elo 排名由这些人类投票计算。因此 Arena Elo 与 LLM-as-a-judge 评估之间没有直接的 judge 重叠——benchmark contamination（记忆特定 test items）不会直接影响 Arena 中面对全新用户 prompts 的表现。\n\n但我同意 R2 的两个有效子点：\n1. Arena 不完全独立——热门模型可能获得更多曝光和用户偏好（popularity bias）\n2. 如果 contaminated 模型在 benchmark 上训练后也间接提升了 Arena 场景下的能力（泛化效应），则存在间接 circularity\n\n论文 Limitations section 应明确讨论这些。ConStat 验证（ρ=0.82，best tier）确实部分缓解了 circularity 问题，因为 ConStat 是独立于 Arena 的 contamination 测量。建议在 Limitations 中增加一段：\"While Chatbot Arena rankings are based on human votes rather than LLM judges, they are not fully independent of benchmark performance—models with strong benchmark scores may attract more Arena users. The ConStat external validation (ρ=0.82) provides an Arena-independent check on c_n estimates.\"\n\n**[AGREE] R2-Should-Fix-3: \"Joint\" title expectation mismatch**\n\n同意。这是跨所有审稿轮次和 reviewer 的**最强共识问题**——我在首轮 review（R1-N1 critical）、best-tier review（W3）、median-tier review（Q5）都独立标记了此问题。R2 在首轮和本轮也标记。\n\nR2 的建议\"改为 unified 或 integrated\"是合理的替代方案。我对三个选项的优劣评估：\n- **\"Joint Calibration\"**（当前）：技术上可辩护（Stage 3 内部确实是 joint），但 misleading\n- **\"Unified Calibration\"**：暗示一个统一框架但不承诺单一后验，更准确\n- **\"Integrated Calibration\"**：暗示多个组件的整合，与三阶段 pipeline 一致\n- **\"Staged Joint Calibration\"**（Abstract 已用）：最精确但标题中过于冗长\n\n我推荐 **\"Unified\"** 或 **\"Integrated\"** 用于标题，**\"staged joint\"** 保留在正文描述中。\n\n**[AGREE] R2-Should-Fix-4: Writing quality — 部分段落可压缩**\n\n同意但视为 minor。Best tier 论文的写作整体清晰，Section 2（OVB motivation）和 Section 5（Results）的叙事流畅。如果有特定过长段落，R2 应指出具体位置。作为通用建议，Section 6（Analysis）的各子节可考虑合并或精简以腾出空间给 figures（目前全文零 figures 是独立的 presentation 问题）。\n\n---\n\n### Presentation Issues\n\n**[REBUT] R2-Presentation-5: Rank-change analysis 缺失**\n\n不同意。Best tier 论文**包含 rank change analysis**：\n- Table 3（Section 5.2）明确报告了 per-model rank changes：Qwen3-235B-A22B 从 raw rank 3 → G-MFRM rank 7（-4 positions, c_n=1.82），Llama 4 Maverick 从 5→8（-3），Model-X-70B 从 8→5（+3），Claude Sonnet 4.6 从 4→2（+2）\n- 论文报告了 5 个模型移动 ≥2 positions、2 个移动 ≥3、top-5 有 2 个交换\n- Fig 4（如果存在于 YAML 设计中）是 bump chart 展示排名流向，但实际论文中零 figures，因此视觉化确实缺失\n\nR2 可能因为论文缺少**图表形式**的 rank change 可视化（如 bump chart 或 alluvial diagram）而误判为\"缺失\"。数据本身在 Table 3 中，但没有 figure 辅助确实降低了可读性。因此：rank change **分析**存在，rank change **可视化**缺失。后者属于我已标记的零 figures 问题（W6/N2）。\n\n**[AGREE] R2-Presentation-6: Stage 2→3 连接说明不足**\n\n同意。Section 3.3 描述了三阶段 pipeline，但 e_i 从 Stage 2 输出到 Stage 3 输入的**具体操作方式**可以更明确：\n- e_i 是作为 fixed point estimate 传入 Stage 3？还是作为 distribution？\n- 如果是 fixed point，其不确定性如何处理？（答案：不处理，这是 Section 6.4 error propagation 分析的动机）\n- Stage 2 的 weighted composite 公式（各 source 权重如何确定）在 Section 3.2 中描述了\"weighted combining\"但未给出具体权重公式\n\n建议在 Section 3.3 Stage 3 开头增加明确连接：\"Stage 3 receives e_i as a fixed point estimate from Stage 2. Uncertainty in e_i is not propagated into the Stage 3 posterior; instead, we quantify the impact of e_i noise through the sensitivity analysis in Section 6.3.\"\n\n**[AGREE] R2-Presentation-7: Related work coverage 不足**\n\n同意，与全部审稿轮次的共识一致。~15 篇 references 对于一篇跨 judge bias、contamination、psychometrics、Bayesian estimation 领域的论文严重不足。这一问题在首轮即被标记（R1-N4, R2-N2），修订版未充分改善。\n\n---\n\n### 对 R2 Strengths 评估的回应\n\nR2 列出的四个优势我全部同意：\n1. **IRT 框架整合有原则性**：G-MFRM 的 gating mechanism 是对 DG-IRT 的 principled adaptation\n2. **相比 Round 1 有实质性改进**：从首轮的单栏格式+10 篇引用，到现在的 ACL 双栏+12 个实验+error propagation 分析\n3. **τ=0.91, AUC=0.94, r=0.82 结果强劲**：best tier 的实验结果在数值上有说服力\n4. **OVB 动机清晰**：使用\"Observation\"而非\"Proposition\"，引用 Angrist & Pischke (2009)，是诚实的 framing\n\n---\n\n### 评分对照\n\n| 维度 | R1 (best tier) | R2 (best tier) | 差异分析 |\n|------|---------------|---------------|---------|\n| Soundness | 4/5 | 4/5 | **一致** |\n| Excitement | 3/5 | 3/5 | **一致** |\n| Overall | 3.5 | 3.5 | **一致** |\n\nR1 和 R2 对 best tier 的评分完全一致（Soundness 4, Excitement 3, Overall 3.5）。主要分歧在于 weakness 的分类方式：\n- R2 将 \"first claim\" 作为唯一 Must-Fix，而 R1 将 \"joint framing\"、\"missing CIs\"、\"零 figures\" 作为主要问题\n- 这说明两位 reviewer 从不同角度（R2: novelty/positioning; R1: evidence/presentation）得出了相同的总体评估\n\n**共识 actionable items（best tier）**：\n1. 精确限定\"first\"claim → \"first IRT-based joint estimation in LLM evaluation\"\n2. 标题\"Joint\"改为\"Unified\"或\"Integrated\"\n3. 扩充 references 至 30+\n4. 在 Section 3.3 明确 e_i 作为 fixed input 的处理方式和理由\n5. 加入至少 3-4 个关键 figures（framework overview, rank change visualization, ConStat scatter, sensitivity curves）",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-21T22:50:35.267475+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3880
}
```

</details>

---


### Assistant

_source line 126 · 2026-05-21T22:50:39.656025+00:00_

交叉回应已提交。R1 和 R2 对 best tier 的评分完全一致（Overall 3.5, Soundness 4/5, Excitement 3/5），主要 actionable items 已在 consensus 中明确列出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 7

## Round 7

28 recorded events


### User

_source line 127 · 2026-05-22T05:00:55.129916+00:00_

[Round 1 审稿请求]:
## Review Task: Comprehensive Review

**Paper**: "How Much Contamination Are We Actually Correcting? A Joint Psychometric Audit of LLM-as-a-Judge Evaluation"

**Venue**: EMNLP 2026 (via ARR). Scoring: Overall Assessment 1–5 half-step; Soundness/Excitement/Reproducibility each 1–5. Acceptance rate ~21% for Main, Findings also available.

**Paper summary** (for your orientation — form your own judgment):
The paper proposes G-MFRM, a three-stage psychometric framework that jointly models judge severity (d_j), item difficulty (b_i), model ability (θ_n), and contamination susceptibility (c_n) for LLM-as-a-judge evaluation. Stage 1 fits standard MFRM; Stage 2 estimates per-item exposure e_i via three external sources (performance gap, temporal signal, LogProber); Stage 3 fits a joint gated model with c_n·e_i terms. The paper formalizes the confounding between judge severity and contamination as an OVB problem (Eq. 2). Applied to 8 judges × 22 models across MT-Bench, Arena-Hard, and WildBench, the paper reports a "calibrated null finding": real contamination is negligible (median c_n = 0.15), no method outperforms standard MFRM calibration (all Δτ < 0.02, p > 0.18). Adversarial injection experiments show G-MFRM works when contamination is artificially elevated (τ = 0.87 at c_n = 1.5 vs 0.75 for MFRM).

**Experiment design reference** (what was planned — use to judge coverage):
11 experiments were planned:
1. Multi-judge data collection (8 judges × 22 models, MT-Bench + Arena-Hard)
2. Item exposure estimation (three-source e_i pipeline)
3. G-MFRM real data fit (Stage 3 convergence, fair scores vs Arena τ)
4. Baseline comparison (8 baselines, Kendall-τ/Spearman-ρ with Arena)
5. Contamination magnitude calibration (real c_n vs synthetic assumptions)
6. Judge count sensitivity (2/4/6/8 judges, leave-one-judge-out)
7. Exposure source ablation (contribution of each e_i source)
8. Facet fit diagnostics (infit/outfit, convergence, posterior predictive checks)
9. Confounding formal OVB derivation + Monte Carlo validation
10. WildBench replication (cross-benchmark generalization)
11. Adversarial robustness (synthetic contamination injection at 5 levels)

All 11 appear covered in the paper (Sections 4.1–4.11).

---

**Your review must cover ALL of the following dimensions. Be thorough and critical.**

### 1. Soundness (1–5)
- Is the OVB formalization (Section 3.2, Eq. 2) correct and non-trivial? Does the bias formula actually matter at observed contamination levels?
- Stage 2 e_i pipeline: internal consistency α = 0.24 is far below psychometric standards (0.70). Is the paper honest about this? Does fixing e_i in Stage 3 (rather than joint estimation) introduce its own bias?
- Stage 3 convergence: R̂_max = 1.18, ESS_min = 34, 2.8% divergent transitions for c_n parameters. Are these acceptable for publication? The paper reports them but does not attempt to fix them (reparameterization, stronger priors, etc.).
- The c_n misfit rate is 36.4% (outfit > 1.3). Can the paper credibly claim G-MFRM "works" when over a third of its novel parameters misfit?
- Statistical power: post-hoc power = 0.12 for detecting Δτ = 0.02 with N = 22. The paper frames this as "the effect is too small to matter" — is this a valid reframe or a rationalization of underpowered design?
- Identifiability claim (Section 3.3): the paper asserts full column rank "when there exist items with e_i > 0 and e_i ≈ 0." With median e_i = 0.12 and most items near zero, is this condition meaningfully satisfied?

### 2. Excitement / Novelty (1–5)
- The core methodological contribution (adapting DG-IRT gating to MFRM with continuous exposure) — how novel is this given Shu et al. (2013) already introduced gating in IRT?
- The OVB formalization — is it a genuine theoretical contribution or a straightforward application of textbook OVB to a new setting?
- The "null finding as contribution" framing — is this compelling? Does the paper provide enough evidence that the community actually believed contamination was high on these specific benchmarks?
- The paper claims to fill a gap where no prior work jointly models judge bias and contamination. How significant is this gap given the null result shows the two are approximately orthogonal on current data?
- Adversarial injection (Section 4.11) shows the method works at c_n ≥ 0.7. But this is entirely synthetic. Does it add real value?

### 3. Reproducibility (1–5)
- Are the three e_i sources (performance gap, temporal, LogProber) described with enough detail to replicate? What are "reference variants"? What spline specification is used for difficulty correction?
- Bayesian model specification: priors are stated (θ ~ N(0,σ²_θ), c_n ~ Half-Cauchy(0,1), d_j ~ N(0,σ²_d)) but hyperprior values for σ²_θ and σ²_d are not given. Sampler details (algorithm, chains, warmup, iterations) are missing.
- The paper mentions $870 API cost + 118 GPU-hours. Is this sufficient for reproducibility, or does it create a barrier?
- Data/code release: the conclusion mentions releasing "multi-judge evaluation dataset and G-MFRM implementation" — is this a commitment or aspiration?

### 4. Presentation Quality
- 11 pages (main text appears to be 8 pages + limitations + references). Check against EMNLP 2026 8-page limit for main text.
- 16 tables is a lot. Are they all necessary? Could some move to appendix?
- The paper's narrative arc (propose method → null result → reframe as diagnostic) feels post-hoc. Does the writing successfully navigate this, or does it read as a paper that failed its original hypothesis?
- Is the Limitations section adequate? (3 points: low contamination, e_i quality, scale)

### 5. Missing Experiments / Weaknesses
- No comparison with a true "contaminated benchmark" (e.g., original MMLU, GSM8K). The paper only injects synthetic contamination. Why not validate on a benchmark where contamination IS known to exist?
- Cross-benchmark c_n correlation is only 0.28 — this undermines the construct validity of c_n as a stable model property. Does the paper adequately address this?
- The leave-one-judge-out diagnostic (Table 13) shows no same-family bias. This contradicts strong prior findings (CyclicJudge, Preference Leakage). Is this discussed?
- No human evaluation or expert validation of the c_n estimates.
- WildBench uses only 6 judges (vs 8 for MT-Bench/Arena-Hard) without justification.

### 6. Automatic Reject Signals
- Check: anonymity compliance, page limit, Limitations section present, citation validity (any hallucinated references?).

### 7. Overall Assessment
Provide:
- **Soundness**: X/5
- **Excitement**: X/5  
- **Reproducibility**: X/5
- **Overall Assessment**: X/5 (use ARR half-step scale)
- **Confidence**: X/5
- **Best Paper**: Yes/No
- One paragraph: key reasons for your score
- One paragraph: what would change your mind (what revisions would raise/lower the score)

Calibrate to EMNLP 2026 acceptance rate (~21% Main, plus Findings). A score of 4 means "accept to Main conference"; 3 means "Findings-worthy"; 2.5 means borderline Findings.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-22T05:01:21.897978+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/paper.pdf",
  "project": "gated_mfrm_judge_bias",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/paper.pdf",
    "project": "gated_mfrm_judge_bias",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-22T05:01:22.907051+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 332.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 306.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 254.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 365.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 285.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 267.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 311.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 258.8}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judg
…[truncated 629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1009
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-22T05:01:22.957746+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/review_context.yaml",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/review_context.yaml",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-22T05:01:23.159126+00:00_

1	narrative_guidance: 'Reframe required — do NOT downgrade venue. New angle: ''A Psychometric
2	  Framework for Auditing LLM Evaluation Integrity.'' Primary contribution shifts from
3	  ranking correction to methodology and measurement infrastructure. Three-pronged
4	  reframe: (1) OVB observation is mathematical fact — confounding IS the correct concern
5	  even if current contamination is small; position as proactive methodology. (2) Negative
6	  result as contribution: current benchmark contamination, while detectable, does
7	  not yet substantially distort rankings — reassuring but contingent. (3) Foreground
8	  the measurement model itself as novel: first application of gated IRT to LLM evaluation.
9	  Synthetic experiments demonstrate the method works when contamination is strong;
10	  real-data results show current contamination is manageable. Likely need exp-010
11	  (WildBench) or exp-011 (adversarial robustness) to fill the empirical gap left by
12	  weak real-data results.
13	
14	  '
15	imagined_experiments:
16	- name: multi_judge_data_collection
17	  plan_id: exp-001
18	  description: 'Collect multi-judge evaluation data on MT-Bench and Arena-Hard using
19	    8 judges. Evaluate 20+ target models with position swap.
20	
21	    '
22	  expected_results:
23	    judges_collected: 8
24	    target_models_evaluated: 22
25	    mt_bench_items: 80
26	    arena_hard_items: 500
27	    total_judgments_after_position_swap: ~176000
28	    missing_rate_pct: 4.2
29	    logprober_available_judges: 3
30	    logprober_unavailable_key_models:
31	    - GPT-5.5
32	    - Claude Opus 4.7
33	    - Claude Sonnet 4.6
34	    api_cost_usd: 870
35	    gpu_hours_used: 118
36	    inter_judge_agreement_fleiss_kappa: 0.31
37	  result_rationale: 'Data collection itself succeeds — this is infrastructure, not
38	    dependent on contamination magnitude. However, two worst-tier signals emerge early:
39	    (1) LogProber access is unavailable for the 3 proprietary judges (GPT-5.5, Claude
40	  
…[truncated 4444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-22T05:01:32.144337+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-22T05:01:32.701386+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 557
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-22T05:01:32.701868+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-22T05:01:33.608228+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-22T05:01:33.659569+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 137 · 2026-05-22T05:01:34.114757+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 138 · 2026-05-22T05:01:34.569911+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool call

_source line 139 · 2026-05-22T05:01:34.570347+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 140 · 2026-05-22T05:01:34.874825+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 760
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-22T05:01:35.390627+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 820
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-22T05:01:46.131683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-22T05:01:46.585880+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-22T05:01:46.586328+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-22T05:01:47.543792+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-22T05:01:47.544292+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-22T05:01:48.098006+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-22T05:01:48.098458+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-22T05:01:48.551961+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-22T05:01:48.606711+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-22T05:01:49.062393+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-22T05:07:45.294188+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Comprehensive Review: R1\n\n**Paper**: \"How Much Contamination Are We Actually Correcting? A Joint Psychometric Audit of LLM-as-a-Judge Evaluation\"\n**Venue**: EMNLP 2026 (ARR)\n\n---\n\n### 1. Summary\n\nThe paper proposes G-MFRM, a three-stage psychometric framework for jointly modeling judge severity, item difficulty, model ability, and contamination susceptibility in LLM-as-a-judge evaluation. The theoretical motivation—formalizing sequential correction bias as an OVB problem—is correct. On synthetic data, G-MFRM outperforms sequential baselines when contamination is strong. However, on real evaluation data (8 judges × 22 models, MT-Bench + Arena-Hard + WildBench), the paper arrives at a \"calibrated null finding\": current contamination is negligible (median c_n ≈ 0.15-0.18), G-MFRM matches but never outperforms standard MFRM calibration (all Δτ < 0.02, p > 0.18), and the entire exposure estimation pipeline demonstrably adds nothing to ranking quality (Table 8 ablation: uniform e_i yields τ = 0.84 vs full pipeline τ = 0.85). The paper reframes this as informative—current benchmarks are trustworthy—and positions G-MFRM as monitoring infrastructure.\n\n---\n\n### 2. Soundness (2/5)\n\n**OVB Formalization (Section 2.2, Eq. 2)**: Correct. The observation that Cov(d_j, c_n·e_i) ≠ 0 ⟹ sequential estimation bias is a direct application of the Frisch-Waugh-Lovell theorem. The paper honestly labels it \"Observation\" and cites Angrist & Pischke (2009). Monte Carlo validation (Table 1, 300 configurations) confirms bias in non-orthogonal settings with median θ-RMSE degradation of 28.2%. **However**, this theoretical contribution is rendered empirically moot by the null finding: at real contamination levels (c_n ≈ 0.15), the OVB effect is negligible. The paper's own Table 5 shows G-MFRM = MFRM = Sequential = 0.85 τ.\n\n**Stage 2 e_i pipeline**: The three-source composite achieves ρ = 0.47 with LogProber (Table 2)—the strongest individual source. Critically, LogProber is unavailable for 3/8 judges (the proprietary ones most likely to exhibit contamination), meaning the composite relies on the weaker performance-gap method (ρ = 0.41 alone) for exactly the models that matter. The ablation (Table 8) delivers the definitive verdict: **uniform e_i (no estimation at all) yields τ = 0.84**, only 0.01 below the full pipeline. This means the entire Stage 2 contributes nothing to downstream ranking quality under current contamination levels. The paper acknowledges this (\"logically consistent with weak contamination\") but does not discuss that this invalidates the e_i pipeline as a current contribution—it is at best future-proofing.\n\n**Stage 3 convergence (Table 4)**: The c_n parameters fail to converge by standard criteria:\n- Max R̂ = 1.12 (paper text; Director cites 1.18): exceeds the 1.10 threshold widely considered necessary for reliable inference (Vehtari et al., 2021)\n- Min ESS = 79 (paper) or 34 (Director): far below the 400 recommended for reliable posterior mean estimation and the 100 bare minimum\n- 23 divergent transitions: indicates the NUTS sampler encountered pathological posterior geometry\n- The paper attributes this to \"likelihood surface flat in c_n direction when true c_n ≈ 0\" — which is correct, but the implication is that **c_n posteriors for the majority of models (68% with c_n < 0.1) are essentially prior-dominated**, not data-informed. The paper should either (a) fix convergence (reparameterization, informative priors, longer chains, higher adapt_delta), or (b) clearly state that c_n point estimates are unreliable for low-contamination models and restrict interpretation to the distribution level.\n\n**c_n misfit rate**: The paper reports substantial misfit for the contamination facet (outfit up to 2.10). The Director cites 36.4% (8/22 models with outfit > 1.3). This means over a third of c_n parameters don't conform to the rank-1 assumption c_n · e_i. For the novel parameters that constitute the paper's methodological contribution, a >1/3 misfit rate is deeply concerning. The paper notes this is \"primarily among models with c_n ≈ 0 where the gating mechanism is inactive\" — but this explanation underscores the identifiability problem: when contamination is negligible, the c_n parameters are unidentifiable, and the model has no basis for estimating them.\n\n**95% CI coverage = 78%** (Table 3): This means the Bayesian credible intervals are systematically overconfident, especially for low-contamination models where coverage is worst. Any claim about individual c_n uncertainty quantification is unreliable. The paper's Limitations section mentions this but doesn't discuss the implication: per-model diagnostic claims (\"Model X has c_n = 0.72 [0.38, 1.12]\") cannot be trusted at face value.\n\n**Statistical power**: Post-hoc power = 0.12 for detecting Δτ = 0.02 with N = 22 models. **This is the paper's most fundamental inferential problem.** With 12% power, the study has an 88% probability of missing a true effect of Δτ = 0.02. The paper frames the null result as \"the effect is too small to matter\" — but this reframe requires establishing that the effect is genuinely near zero (equivalence testing), not merely failing to reject the null (which could equally reflect insufficient power). The paper does not perform an equivalence test (e.g., TOST with a practical equivalence bound). Without one, the null finding is underdetermined: it could mean contamination is negligible, OR the study is too underpowered to detect it.\n\n**Identifiability**: The paper asserts identifiability \"when there exist items with e_i > 0 and e_i ≈ 0.\" With median e_i = 0.22 and most items near zero, the separation between exposed and unexposed items is weak. This is reflected in the convergence failure: the data doesn't contain enough contamination signal to identify c_n reliably.\n\n---\n\n### 3. Excitement / Novelty (2/5)\n\n**G-MFRM model**: Adapting DG-IRT gating (Robitzsch, 2020) from binary group membership to continuous exposure in a multi-facet Rasch setting is a reasonable methodological contribution. It is not a deep model innovation—it's a domain-appropriate combination of existing psychometric tools—but it fills a genuine gap. **However, the contribution is validated only on synthetic data.** On real data, G-MFRM reduces to MFRM because there's nothing to correct.\n\n**OVB observation**: Correctly formalized, but a straightforward application of textbook econometrics. The paper's honest framing (\"this follows directly from the classical omitted variable bias result\") is appropriate, but the contribution weight should reflect this.\n\n**Null finding as contribution**: This is the paper's most complex sell. In principle, well-powered negative results are valuable. But this null finding suffers from:\n- Insufficient power (12%) to establish the negative with confidence\n- No equivalence test to formally bound the maximum possible contamination effect\n- The measurement tool itself has problems (convergence failure, misfit, weak construct validity) that could mask a real signal\n\nFor a null finding to be convincing, the methodology must be demonstrably capable of detecting the signal if it existed. The synthetic experiments show G-MFRM works at c_n ≥ 0.7, but the real data has c_n ≈ 0.15—the model may simply be insensitive at these levels. The paper partially addresses this by noting that synthetic c_n recovery at low contamination has RMSE = 0.53 (vs 0.20 for high contamination), confirming poor sensitivity. But this undermines the null finding: the tool isn't sensitive enough to detect small contamination, so its failure to detect it is uninformative.\n\n**Adversarial injection (Section 5.10)**: Shows G-MFRM works at c_n ≥ 0.7 synthetically. This is useful as a proof-of-concept but entirely artificial. The 14% false positive rate and 33% detection rate for subtle attacks limit practical utility.\n\n**\"Monitoring infrastructure\" reframing**: Intellectually honest and forward-looking, but the infrastructure itself has too many reliability issues (convergence failure, 36.4% misfit, 78% CI coverage) to function as a credible monitoring tool in its current state.\n\n---\n\n### 4. Reproducibility (2/5)\n\n**e_i pipeline**: The three sources are described at a high level but key details are missing:\n- \"Reference variants\" are mentioned but the generation method (LLM paraphrasing? manual? template-based?) is not specified in sufficient detail\n- Spline difficulty correction: no specification (degree, knots, fitting procedure)\n- Weighting scheme: \"weights proportional to per-source reliability\" — but how is per-source reliability estimated? On what holdout data?\n\n**Bayesian model**: Priors are stated (θ ~ N(0, σ²_θ), c_n ~ Half-Cauchy(0,1), d_j ~ N(0, σ²_d)) but:\n- σ²_θ and σ²_d hyperprior values are not given\n- Sampler algorithm: \"NumPyro MCMC\" mentioned but NUTS vs HMC not specified explicitly\n- Number of chains, warmup iterations, sampling iterations: partially stated in passing (\"4,000 posterior samples\") but not systematically (is this 4,000 per chain × 4 chains = 16,000? or 4,000 total?)\n\n**Cost barrier**: $870 API + 118 GPU-hours is substantial but documented. This creates a barrier to independent replication by labs without similar resources.\n\n**Data/code release**: The Conclusion mentions releasing \"multi-judge evaluation dataset and G-MFRM implementation.\" This reads as aspiration rather than commitment—no URL, repository, or timeline is provided.\n\n---\n\n### 5. Presentation Quality\n\n**Page count**: 10 pages in ACL double-column format. Main text (Sections 1-7) spans pages 1 through ~10. If Limitations is on page 10 and doesn't count toward the 8-page limit, the main text (Sections 1-7) appears to be approximately 9+ pages, potentially exceeding the EMNLP 8-page limit. This needs verification.\n\n**Tables**: 16 tables (10 main + appendix) is high density. Tables 2-10 in the main text are all informative, but Tables 3 (synthetic c_n recovery) and 7 (error propagation) could move to appendix since they concern synthetic rather than real-data results.\n\n**Narrative arc**: The paper's narrative—propose method → null result → reframe as diagnostic—reads as post-hoc. The title (\"How Much Contamination Are We Actually Correcting?\") and the audit framing help, but the disconnect between the method development (Sections 2-4) and the null finding (Section 5) creates a sense that the paper's original hypothesis failed. The Discussion (Section 6) navigates this reasonably well by emphasizing: (1) OVB is a mathematical fact independent of empirical magnitude, (2) the null is contingent and may not hold in future, (3) diagnostic outputs are novel. But a reader may reasonably ask: if the contamination is negligible, why develop this elaborate framework now?\n\n**Limitations section**: Covers three points (exposure estimation noise, near-zero identifiability, rank-1 assumption). This is adequate but should also mention: (4) statistical power limitations and the absence of equivalence testing, (5) the 36.4% c_n misfit rate, (6) the 78% CI coverage.\n\n---\n\n### 6. Missing Experiments / Weaknesses\n\n**No naturally contaminated benchmark**: The paper only evaluates on MT-Bench, Arena-Hard, and WildBench—benchmarks where contamination is apparently low. Why not include a benchmark where contamination IS known to exist (e.g., original MMLU items, GSM8K)? This would provide a positive control: if G-MFRM can detect known contamination on a contaminated benchmark, the null finding on MT-Bench/Arena-Hard becomes more credible. Without this, the null finding could reflect measurement insensitivity rather than true absence.\n\n**Cross-benchmark c_n correlation ρ = 0.28-0.42**: This is low for a \"stable model property.\" If contamination susceptibility is a model-level trait, cross-benchmark correlation should be high (ρ > 0.7). Values around 0.3-0.4 suggest c_n is substantially noise or benchmark-specific artifact. The paper says ρ = 0.42 \"provides construct validity evidence\" — I disagree; ρ = 0.42 explains only ~18% of cross-benchmark variance, which is weak validity at best.\n\n**Leave-one-judge-out (Table 9/implied)**: The paper mentions no same-family judge bias. This contradicts findings from CyclicJudge (Lin et al., 2025) and Performance Leakage (Li et al., 2024) that documented substantial same-family bias. The paper should discuss this discrepancy—is it because the d_j estimates absorb within-family bias, or because the data genuinely shows no such effect?\n\n**No expert validation of c_n estimates**: The per-model c_n values (e.g., Qwen3-235B-A22B c_n = 0.72) are unvalidated by any external expert judgment. Given the 36.4% misfit rate and 78% CI coverage, expert validation would substantially strengthen (or undermine) the diagnostic claims.\n\n**WildBench uses 6 judges**: Without justification for why 2 judges are dropped from the 8-judge panel. Given that judge count sensitivity (Table 9) shows G-MFRM needs ≥6 judges for stable c_n estimates, using 6 on WildBench is at the minimum threshold and should be justified.\n\n---\n\n### 7. Automatic Reject Signals\n\n- **Anonymity**: Appears compliant (Anonymous author)\n- **Page limit**: Potentially exceeded (~9+ pages main text for 8-page limit). Needs verification.\n- **Limitations section**: Present but incomplete (missing power analysis, misfit rate, CI coverage discussion)\n- **Citation validity**: References appear legitimate based on known works cited. No obviously hallucinated citations detected from what I can read.\n\n---\n\n### 8. Overall Assessment\n\n| Dimension | Score | Rationale |\n|-----------|-------|-----------|\n| **Soundness** | **2/5** | Convergence failure for c_n (R̂ ≥ 1.12, ESS ≤ 79), 78% CI coverage, 36.4% c_n misfit, power = 0.12, e_i pipeline adds nothing (Table 8 ablation). The theoretical OVB contribution is correct but empirically moot. The null finding is established with insufficient methodological rigor. |\n| **Excitement** | **2/5** | Important problem, creative approach. But: real-data contribution is a null finding established with underpowered design and unreliable measurement. Synthetic validation shows potential but doesn't constitute a real contribution. \"Monitoring infrastructure\" is a valid vision but the infrastructure doesn't yet work reliably. |\n| **Reproducibility** | **2/5** | Key pipeline details missing (reference variant generation, spline specification, weighting scheme, MCMC hyperpriors). Code/data release is aspirational, not committed. Cost barrier ($870 + 118 GPU-hours) is documented. |\n| **Overall** | **2.0** (Resubmit next cycle) | |\n| **Confidence** | **4/5** | |\n| **Best Paper** | **No** | |\n\n**Key reasons for score**: The paper contains a correct theoretical contribution (OVB observation) and a creative methodology (G-MFRM) validated on synthetic data. But the real-data execution has six interrelated problems that collectively undermine the empirical claims: (1) MCMC convergence failure for the novel c_n parameters, (2) an exposure estimation pipeline that demonstrably adds nothing to ranking quality, (3) an underpowered null finding (power = 0.12) without equivalence testing, (4) 36.4% c_n misfit rate, (5) 78% CI coverage, and (6) weak construct validity (ConStat ρ = 0.32, cross-benchmark ρ = 0.28-0.42). The \"calibrated null finding\" narrative is intellectually honest but rests on a measurement tool that lacks the sensitivity and reliability to establish that null with confidence.\n\n**What would change my mind**: The score could rise to **3.0 (Findings)** if the authors: (1) fix c_n convergence (reparameterize, use informative priors from the synthetic studies, increase warmup/chains, report per-parameter convergence for all 22 c_n parameters), (2) include an equivalence test (TOST) to formally bound the contamination effect below a practical significance threshold, (3) add a positive-control benchmark where contamination is known to exist, and (4) either improve e_i estimation (broader LogProber access) or honestly reframe Stage 2 as future-proofing rather than a current contribution. The score could drop to **1.5** if the convergence issues are shown to invalidate the c_n posterior distributions entirely (e.g., if trace plots reveal non-mixing chains for the majority of c_n parameters).",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Comprehensive Review: R1\n\n**Paper**: \"How Much Contamination Are We Actually Correcting? A Joint Psychometric Audit of LLM-as-a-Judge Evaluation\"\n**Venue**: EMNLP 2026 (ARR)\n\n---\n\n### 1. Summary\n\nThe paper proposes G-MFRM, a three-stage psychometric framework for jointly modeling judge severity, item difficulty, model ability, and contamination susceptibility in LLM-as-a-judge evaluation. The theoretical motivation—formalizing sequential correction bias as an OVB problem—is correct. On synthetic data, G-MFRM outperforms sequential baselines when contamination is strong. However, on real evaluation data (8 judges × 22 models, MT-Bench + Arena-Hard + WildBench), the paper arrives at a \"calibrated null finding\": current contamination is negligible (median c_n ≈ 0.15-0.18), G-MFRM matches but never outperforms standard MFRM calibration (all Δτ < 0.02, p > 0.18), and the entire exposure estimation pipeline demonstrably adds nothing to ranking quality (Table 8 ablation: uniform e_i yields τ = 0.84 vs full pipeline τ = 0.85). The paper reframes this as informative—current benchmarks are trustworthy—and positions G-MFRM as monitoring infrastructure.\n\n---\n\n### 2. Soundness (2/5)\n\n**OVB Formalization (Section 2.2, Eq. 2)**: Correct. The observation that Cov(d_j, c_n·e_i) ≠ 0 ⟹ sequential estimation bias is a direct application of the Frisch-Waugh-Lovell theorem. The paper honestly labels it \"Observation\" and cites Angrist & Pischke (2009). Monte Carlo validation (Table 1, 300 configurations) confirms bias in non-orthogonal settings with median θ-RMSE degradation of 28.2%. **However**, this theoretical contribution is rendered empirically moot by the null finding: at real contamination levels (c_n ≈ 0.15), the OVB effect is negligible. The paper's own Table 5 shows G-MFRM = MFRM = Sequential = 0.85 τ.\n\n**Stage 2 e_i pipeline**: The three-source composite achieves ρ = 0.47 with LogProber (Table 2)—the strongest individual source. Critically, LogProber is unavailable for 3/8 judges (the proprietary ones most likely to exhibit contamination), meaning the composite relies on the weaker performance-gap method (ρ = 0.41 alone) for exactly the models that matter. The ablation (Table 8) delivers the definitive verdict: **uniform e_i (no estimation at all) yields τ = 0.84**, only 0.01 below the full pipeline. This means the entire Stage 2 contributes nothing to downstream ranking quality under current contamination levels. The paper acknowledges this (\"logically consistent with weak contamination\") but does not discuss that this invalidates the e_i pipeline as a current contribution—it is at best future-proofing.\n\n**Stage 3 convergence (Table 4)**: The c_n parameters fail to converge by standard criteria:\n- Max R̂ = 1.12 (paper text; Director cites 1.18): exceeds the 1.10 threshold widely considered necessary for reliable inference (Vehtari et al., 2021)\n- Min ESS = 79 (paper) or 34 (Director): far below the 400 recommended for reliable posterior mean estimation and the 100 bare minimum\n- 23 divergent transitions: indicates the NUTS sampler encountered pathological posterior geometry\n- The paper attributes this to \"likelihood surface flat in c_n direction when true c_n ≈ 0\" — which is correct, but the implication is that **c_n posteriors for the majority of models (68% with c_n < 0.1) are essentially prior-dominated**, not data-informed. The paper should either (a) fix convergence (reparameterization, informative priors, longer chains, higher adapt_delta), or (b) clearly state that c_n point estimates are unreliable for low-contamination models and restrict interpretation to the distribution level.\n\n**c_n misfit rate**: The paper reports substantial misfit for the contamination facet (outfit up to 2.10). The Director cites 36.4% (8/22 models with outfit > 1.3). This means over a third of c_n parameters don't conform to the rank-1 assumption c_n · e_i. For the novel parameters that constitute the paper's methodological contribution, a >1/3 misfit rate is deeply concerning. The paper notes this is \"primarily among models with c_n ≈ 0 where the gating mechanism is inactive\" — but this explanation underscores the identifiability problem: when contamination is negligible, the c_n parameters are unidentifiable, and the model has no basis for estimating them.\n\n**95% CI coverage = 78%** (Table 3): This means the Bayesian credible intervals are systematically overconfident, especially for low-contamination models where coverage is worst. Any claim about individual c_n uncertainty quantification is unreliable. The paper's Limitations section mentions this but doesn't discuss the implication: per-model diagnostic claims (\"Model X has c_n = 0.72 [0.38, 1.12]\") cannot be trusted at face value.\n\n**Statistical power**: Post-hoc power = 0.12 for detecting Δτ = 0.02 with N = 22 models. **This is the paper's most fundamental inferential problem.** With 12% power, the study has an 88% probability of missing a true effect of Δτ = 0.02. The paper frames the null result as \"the effect is too small to matter\" — but this reframe requires establishing that the effect is genuinely near zero (equivalence testing), not merely failing to reject the null (which could equally reflect insufficient power). The paper does not perform an equivalence test (e.g., TOST with a practical equivalence bound). Without one, the null finding is underdetermined: it could mean contamination is negligible, OR the study is too underpowered to detect it.\n\n**Identifiability**: The paper asserts identifiability \"when there exist items with e_i > 0 and e_i ≈ 0.\" With median e_i = 0.22 and most items near zero, the separation between exposed and unexposed items is weak. This is reflected in the convergence failure: the data doesn't contain enough contamination signal to identify c_n reliably.\n\n---\n\n### 3. Excitement / Novelty (2/5)\n\n**G-MFRM model**: Adapting DG-IRT gating (Robitzsch, 2020) from binary group membership to continuous exposure in a multi-facet Rasch setting is a reasonable methodological contribution. It is not a deep model innovation—it's a domain-appropriate combination of existing psychometric tools—but it fills a genuine gap. **However, the contribution is validated only on synthetic data.** On real data, G-MFRM reduces to MFRM because there's nothing to correct.\n\n**OVB observation**: Correctly formalized, but a straightforward application of textbook econometrics. The paper's honest framing (\"this follows directly from the classical omitted variable bias result\") is appropriate, but the contribution weight should reflect this.\n\n**Null finding as contribution**: This is the paper's most complex sell. In principle, well-powered negative results are valuable. But this null finding suffers from:\n- Insufficient power (12%) to establish the negative with confidence\n- No equivalence test to formally bound the maximum possible contamination effect\n- The measurement tool itself has problems (convergence failure, misfit, weak construct validity) that could mask a real signal\n\nFor a null finding to be convincing, the methodology must be demonstrably capable of detecting the signal if it existed. The synthetic experiments show G-MFRM works at c_n ≥ 0.7, but the real data has c_n ≈ 0.15—the model may simply be insensitive at these levels. The paper partially addresses this by noting that synthetic c_n recovery at low contamination has RMSE = 0.53 (vs 0.20 for high contamination), confirming poor sensitivity. But this undermines the null finding: the tool isn't sensitive enough to detect small contamination, so its failure to detect it is uninformative.\n\n**Adversarial injection (Section 5.10)**: Shows G-MFRM works at c_n ≥ 0.7 synthetically. This is useful as a proof-of-concept but entirely artificial. The 14% false positive rate and 33% detection rate for subtle attacks limit practical utility.\n\n**\"Monitoring infrastructure\" reframing**: Intellectually honest and forward-looking, but the infrastructure itself has too many reliability issues (convergence failure, 36.4% misfit, 78% CI coverage) to function as a credible monitoring tool in its current state.\n\n---\n\n### 4. Reproducibility (2/5)\n\n**e_i pipeline**: The three sources are described at a high level but key details are missing:\n- \"Reference variants\" are mentioned but the generation method (LLM paraphrasing? manual? template-based?) is not specified in sufficient detail\n- Spline difficulty correction: no specification (degree, knots, fitting procedure)\n- Weighting scheme: \"weights proportional to per-source reliability\" — but how is per-source reliability estimated? On what holdout data?\n\n**Bayesian model**: Priors are stated (θ ~ N(0, σ²_θ), c_n ~ Half-Cauchy(0,1), d_j ~ N(0, σ²_d)) but:\n- σ²_θ and σ²_d hyperprior values are not given\n- Sampler algorithm: \"NumPyro MCMC\" mentioned but NUTS vs HMC not specified explicitly\n- Number of chains, warmup iterations, sampling iterations: partially stated in passing (\"4,000 posterior samples\") but not systematically (is this 4,000 per chain × 4 chains = 16,000? or 4,000 total?)\n\n**Cost barrier**: $870 API + 118 GPU-hours is substantial but documented. This creates a barrier to independent replication by labs without similar resources.\n\n**Data/code release**: The Conclusion mentions releasing \"multi-judge evaluation dataset and G-MFRM implementation.\" This reads as aspiration rather than commitment—no URL, repository, or timeline is provided.\n\n---\n\n### 5. Presentation Quality\n\n**Page count**: 10 pages in ACL double-column format. Main text (Sections 1-7) spans pages 1 through ~10. If Limitations is on page 10 and doesn't count toward the 8-page limit, the main text (Sections 1-7) appears to be approximately 9+ pages, potentially exceeding the EMNLP 8-page limit. This needs verification.\n\n**Tables**: 16 tables (10 main + appendix) is high density. Tables 2-10 in the main text are all informative, but Tables 3 (synthetic c_n recovery) and 7 (error propagation) could move to appendix since they concern synthetic rather than real-data results.\n\n**Narrative arc**: The paper's narrative—propose method → null result → reframe as diagnostic—reads as post-hoc. The title (\"How Much Contamination Are We Actually Correcting?\") and the audit framing help, but the disconnect between the method development (Sections 2-4) and the null finding (Section 5) creates a sense that the paper's original hypothesis failed. The Discussion (Section 6) navigates this reasonably well by emphasizing: (1) OVB is a mathematical fact independent of empirical magnitude, (2) the null is contingent and may not hold in future, (3) diagnostic outputs are novel. But a reader may reasonably ask: if the contamination is negligible, why develop this elaborate framework now?\n\n**Limitations section**: Covers three points (exposure estimation noise, near-zero identifiability, rank-1 assumption). This is adequate but should also mention: (4) statistical power limitations and the absence of equivalence testing, (5) the 36.4% c_n misfit rate, (6) the 78% CI coverage.\n\n---\n\n### 6. Missing Experiments / Weaknesses\n\n**No naturally contaminated benchmark**: The paper only evaluates on MT-Bench, Arena-Hard, and WildBench—benchmarks where contamination is apparently low. Why not include a benchmark where contamination IS known to exist (e.g., original MMLU items, GSM8K)? This would provide a positive control: if G-MFRM can detect known contamination on a contaminated benchmark, the null finding on MT-Bench/Arena-Hard becomes more credible. Without this, the null finding could reflect measurement insensitivity rather than true absence.\n\n**Cross-benchmark c_n correlation ρ = 0.28-0.42**: This is low for a \"stable model property.\" If contamination susceptibility is a model-level trait, cross-benchmark correlation should be high (ρ > 0.7). Values around 0.3-0.4 suggest c_n is substantially noise or benchmark-specific artifact. The paper says ρ = 0.42 \"provides construct validity evidence\" — I disagree; ρ = 0.42 explains only ~18% of cross-benchmark variance, which is weak validity at best.\n\n**Leave-one-judge-out (Table 9/implied)**: The paper mentions no same-family judge bias. This contradicts findings from CyclicJudge (Lin et al., 2025) and Performance Leakage (Li et al., 2024) that documented substantial same-family bias. The paper should discuss this discrepancy—is it because the d_j estimates absorb within-family bias, or because the data genuinely shows no such effect?\n\n**No expert validation of c_n estimates**: The per-model c_n values (e.g., Qwen3-235B-A22B c_n = 0.72) are unvalidated by any external expert judgment. Given the 36.4% misfit rate and 78% CI coverage, expert validation would substantially strengthen (or undermine) the diagnostic claims.\n\n**WildBench uses 6 judges**: Without justification for why 2 judges are dropped from the 8-judge panel. Given that judge count sensitivity (Table 9) shows G-MFRM needs ≥6 judges for stable c_n estimates, using 6 on WildBench is at the minimum threshold and should be justified.\n\n---\n\n### 7. Automatic Reject Signals\n\n- **Anonymity**: Appears compliant (Anonymous author)\n- **Page limit**: Potentially exceeded (~9+ pages main text for 8-page limit). Needs verification.\n- **Limitations section**: Present but incomplete (missing power analysis, misfit rate, CI coverage discussion)\n- **Citation validity**: References appear legitimate based on known works cited. No obviously hallucinated citations detected from what I can read.\n\n---\n\n### 8. Overall Assessment\n\n| Dimension | Score | Rationale |\n|-----------|-------|-----------|\n| **Soundness** | **2/5** | Convergence failure for c_n (R̂ ≥ 1.12, ESS ≤ 79), 78% CI coverage, 36.4% c_n misfit, power = 0.12, e_i pipeline adds nothing (Table 8 ablation). The theoretical OVB contribution is correct but empirically moot. The null finding is established with insufficient methodological rigor. |\n| **Excitement** | **2/5** | Important problem, creative approach. But: real-data contribution is a null finding established with underpowered design and unreliable measurement. Synthetic validation shows potential but doesn't constitute a real contribution. \"Monitoring infrastructure\" is a valid vision but the infrastructure doesn't yet work reliably. |\n| **Reproducibility** | **2/5** | Key pipeline details missing (reference variant generation, spline specification, weighting scheme, MCMC hyperpriors). Code/data release is aspirational, not committed. Cost barrier ($870 + 118 GPU-hours) is documented. |\n| **Overall** | **2.0** (Resubmit next cycle) | |\n| **Confidence** | **4/5** | |\n| **Best Paper** | **No** | |\n\n**Key reasons for score**: The paper contains a correct theoretical contribution (OVB observation) and a creative methodology (G-MFRM) validated on synthetic data. But the real-data execution has six interrelated problems that collectively undermine the empirical claims: (1) MCMC convergence failure for the novel c_n parameters, (2) an exposure estimation pipeline that demonstrably adds nothing to ranking quality, (3) an underpowered null finding (power = 0.12) without equivalence testing, (4) 36.4% c_n misfit rate, (5) 78% CI coverage, and (6) weak construct validity (ConStat ρ = 0.32, cross-benchmark ρ = 0.28-0.42). The \"calibrated null finding\" narrative is intellectually honest but rests on a measurement tool that lacks the sensitivity and reliability to establish that null with confidence.\n\n**What would change my mind**: The score could rise to **3.0 (Findings)** if the authors: (1) fix c_n convergence (reparameterize, use informative priors from the synthetic studies, increase warmup/chains, report per-parameter convergence for all 22 c_n parameters), (2) include an equivalence test (TOST) to formally bound the contamination effect below a practical significance threshold, (3) add a positive-control benchmark where contamination is known to exist, and (4) either improve e_i estimation (broader LogProber access) or honestly reframe Stage 2 as future-proofing rather than a current contribution. The score could drop to **1.5** if the convergence issues are shown to invalidate the c_n posterior distributions entirely (e.g., if trace plots reveal non-mixing chains for the majority of c_n parameters).",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-22T05:07:49.740527+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4446
}
```

</details>

---


### Assistant

_source line 154 · 2026-05-22T05:09:58.958253+00:00_

所有已分配的审稿任务均已完成并提交：

- Dream 204917/best: Overall 3.0
- Dream 215715/best: Overall 3.5
- Dream 215715/median: Overall 2.5
- Dream 215715/worst: Overall 2.0
- 3 轮交叉回应均已提交

等待 Review Director 下一轮指令。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 8

## Round 8

36 recorded events


### User

_source line 155 · 2026-05-22T05:14:51.847479+00:00_

[Round 2 审稿请求]:
以下是 Reviewer 2 对 worst 场景（Dream 20260521T215715/worst）的完整审稿意见，请逐条回应：

---

**Overall: 2.0 (Resubmit next cycle)**

**Must-Fix (3 项)**:

M1: "Calibrated null finding" 未真正校准——工具无法可靠区分"无污染"和"污染低于检测阈值"。
- 低 c_n (< 0.3) 合成恢复 RMSE = 0.55，无法区分 c_n=0.05 和 c_n=0.25
- 95% CI coverage = 78%，后验系统性过度自信
- MCMC 收敛问题：R̂=1.12, ESS=78, 23 divergent transitions
- ConStat ρ=0.32，几乎是噪声级别
- 缺少正式 power analysis：给定样本量和 e_i 噪声，最小可检测 c_n 是多少？
建议：加入 formal power analysis，明确 "minimum detectable c_n"

M2: "Monitoring infrastructure" reframing 既缺 novelty 也缺 concrete validation。
- (a) 没有与更简单监控替代方案（ConStat-as-monitor, LogProber-as-monitor）比较
- (b) "随着污染增长 G-MFRM 价值会增加" 是纯推测，没有证据
- (c) "监控基础设施" 是应用方向，不是 EMNLP 研究贡献
- Table 7 显示 G-MFRM 在 e_i noise σ>0.35 时反而比 sequential 差

M3: Novelty 局限于 domain adaptation，null result 使得 adaptation 在实践中不必要。
- OVB（标准计量经济学）+ DG-IRT（现有心理测量）+ MFRM（1989/1994）
- Best 版本中实证结果补偿了 novelty 不足，worst 版本中 null result 完全移除了经验性证据
- 论文提出了一个解决方案，针对一个 (a) 当前不存在、(b) 可能不以假设的 rank-1 形式存在、(c) 可能被更简单工具解决的问题

**Minor (2 项)**:

M4: 缺少 null-result 方法论相关工作（Dodge et al. 2019, Rogers et al. 2020）和 contamination avoidance 文献（LiveBench, private benchmarks, Arena dynamic prompts）。

M5: MCMC 收敛问题严重且应对不足——个体 c_n 不可靠则 per-model 诊断无法使用。

**Strengths**: 诚实透明的报告、OVB 理论正确、全面分析 battery、graceful degradation 验证。

**核心判断**: 论文说"我们建了一个复杂模型，它目前不 help，但未来可能会"——这对 EMNLP 不够。需要 (a) 找到 contamination IS present 的场景证明 G-MFRM 优势，或 (b) 严格 power analysis 量化检测极限。

---

请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-22T05:15:00.794133+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-22T05:15:00.844929+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-22T05:15:05.066300+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/paper.pdf",
  "project": "gated_mfrm_judge_bias",
  "pages": "1-5",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/paper.pdf",
    "project": "gated_mfrm_judge_bias",
    "pages": "1-5",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-22T05:15:05.722462+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 332.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 306.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 254.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 365.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 285.0}], \"total_pages\": 10, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-22T05:15:08.932023+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/paper.pdf",
  "project": "gated_mfrm_judge_bias",
  "pages": "6-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/paper.pdf",
    "project": "gated_mfrm_judge_bias",
    "pages": "6-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-22T05:15:09.923314+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 267.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 311.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 258.8}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 294.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p10.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 343.9}], \"total_pages\": 10, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 991
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-22T05:15:13.148619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 163 · 2026-05-22T05:15:14.156058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 164 · 2026-05-22T05:15:14.511244+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1362
}
```

</details>

---


### Tool call

_source line 165 · 2026-05-22T05:15:14.613355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 166 · 2026-05-22T05:15:14.967132+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 811
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-22T05:15:15.071634+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 458
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-22T05:15:15.072620+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-22T05:15:15.526886+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-22T05:15:15.634585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-22T05:15:16.404769+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 770
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-22T05:15:20.232617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 173 · 2026-05-22T05:15:20.787941+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 174 · 2026-05-22T05:15:21.494204+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1261
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-22T05:15:21.496262+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 708
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-22T05:15:21.648529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 177 · 2026-05-22T05:15:22.001177+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 178 · 2026-05-22T05:15:22.454832+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-22T05:15:22.457018+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-22T05:15:22.457618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images/paper_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-22T05:15:22.861761+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-22T05:17:33.939128+00:00_

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
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
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

_source line 183 · 2026-05-22T05:17:33.989787+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-22T05:18:32.916216+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 交叉回应：R2 对 Worst 场景的审稿意见\n\n**被审论文**: Dream 20260521T215715/worst — \"How Much Contamination Are We Actually Correcting?\"\n**R2 Overall**: 2.0 | **R1 Overall**: 2.0（一致）\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE] R2-M1: \"Calibrated null finding\" 未真正校准**\n\n完全同意核心判断。补充两点：\n\n1. **R2 引用的 RMSE 数值需修正**：R2 称低 c_n (<0.3) 合成恢复 RMSE = 0.55，但 Table 3 实际显示 RMSE = 0.42（G-MFRM）/ 0.85（naive）。不过这不影响结论——在 [0, 0.3] 范围内 RMSE = 0.42 意味着模型基本无法区分 c_n = 0.05 和 c_n = 0.25，R2 的核心论点成立。\n\n2. **CI coverage 问题比 R2 描述的更严重**：78% 是全局覆盖率（Section 5.2），但低 c_n 区间的覆盖率在 Table 3 中未单独报告。考虑到 68% 的模型 c_n < 0.1（Section 5.3），这意味着论文的核心参数估计区间对大多数模型都不可靠，而非仅对少数边缘模型。\n\n3. **强烈支持 R2 关于 formal power analysis 的要求**。论文 Section 7 Limitations 承认了 \"near-zero c_n identifiability\" 问题，但仅定性描述。一篇以 null finding 为核心结论的论文，必须量化 \"minimum detectable c_n\"——否则读者无法判断这是 \"contamination is small\" 还是 \"our tool can't detect it\"。这是 R1 独立审稿中也标记为 critical 的问题。\n\n**[AGREE] R2-M2: \"Monitoring infrastructure\" reframing 缺乏 novelty 和 validation**\n\n逐点回应：\n\n(a) **缺少与更简单监控方案的比较** — 同意。Table 5 对比了 CyclicJudge、DCR、UBA 等作为 ranking 方法，但未将 ConStat-as-monitor 或 LogProber-as-monitor 作为监控替代方案评估。如果论文要声称 G-MFRM 是 \"monitoring infrastructure\"，就需要回答：为什么不直接用 ConStat 做监控？\n\n(b) **\"污染增长则 G-MFRM 价值增加\" 是推测** — 同意。Section 6 的这一论断仅有 Table 6 的合成场景（MVP-001/002/003）间接支撑，但合成场景的 contamination magnitude 是人为设定的，不构成 \"contamination will grow\" 的证据。\n\n(c) **\"监控基础设施\" 不是 EMNLP 研究贡献** — 部分同意。评估方法论属于 EMNLP 范围，但论文交付的是一个在当前条件下不产生增量价值的统计模型，\"monitoring\" 标签本质上是将 null result 包装为 contribution。\n\n(d) **R2 关于 Table 7 breakpoint 的数值需修正**：R2 称 σ > 0.35 时 G-MFRM 劣于 sequential，但 Table 7 显示 breakpoint 在 σ ≈ 0.28。这实际上使问题**更严重**——G-MFRM 在更低的噪声水平就开始退化。考虑到论文自己报告的 composite e_i 质量（Section 4, ρ = 0.47 with ground truth, 仅 43% 的 items 有高置信度估计），真实 e_i 噪声很可能已超过 0.28 breakpoint。\n\n**[AGREE] R2-M3: Novelty 局限于 domain adaptation，null result 使 adaptation 不必要**\n\n这是 R1 和 R2 在所有场景审稿中最一致的共识。补充：\n\n- Table 5 直接证实了 R2 的判断：CyclicJudge+discard 达到 τ = 0.85，与 G-MFRM 完全相同，且不需要 e_i estimation pipeline、MCMC 采样、或任何 contamination modeling。这是 Occam's razor 的经典反例——更简单的方法达到相同结果。\n\n- R2 提出的三重不存在论证 [(a) 问题当前不存在, (b) 可能不以 rank-1 形式存在, (c) 可能被更简单工具解决] 准确且有力。论文自己在 Section 5.10 也承认 adversarial contamination \"is item-specific, not well-approximated by a single c_n per model\"，直接削弱了 rank-1 假设。\n\n- 与 best 场景对比值得强调：best 版本中 τ 提升约 +0.04-0.05、c_n median ~0.95 使得方法论 novelty 不足可以被经验性贡献弥补；worst 版本中 Δτ ≈ 0、c_n median ≈ 0.18，经验性证据完全消失，novelty 不足变成致命缺陷。\n\n---\n\n### Minor 逐条回应\n\n**[AGREE] R2-M4: 缺少 null-result 方法论相关工作和 contamination avoidance 文献**\n\n两个遗漏都是实质性的：\n\n- **Null-result 文献**：如果论文要将 null finding 作为贡献（\"calibrated null\"），需要引用 NLP/ML 领域对 null results 的方法论讨论（Dodge et al. 2019 关于实验报告标准，Rogers et al. 2020 关于 negative results 的价值）。目前的 framing 缺乏方法论锚点。\n\n- **Contamination avoidance 文献**：这是更关键的遗漏。LiveBench（动态更新）、Arena 动态 prompt、private benchmarks 等主动规避策略可能正是当前 contamination 低的原因。如果这些策略有效，G-MFRM 作为 \"被动监控\" 的价值进一步被削弱。论文需要讨论为什么在这些策略存在的情况下，G-MFRM 仍有必要。\n\n**[AGREE] R2-M5: MCMC 收敛问题严重且应对不足**\n\n同意，但补充一个重要 nuance：\n\n- **收敛问题具有参数特异性**：Table 4 清楚显示 θ（ability）和 d（severity）收敛良好（R̂ ≤ 1.04, ESS ≥ 240, 0-2 divergent transitions），问题集中在 c_n（R̂ = 1.12, ESS = 79, 23 divergent transitions）。这意味着论文的排名输出（依赖 θ）可能仍然可靠——Table 5 中 G-MFRM 和 MFRM 的 θ 估计相关性 0.97 也支持这一点。\n\n- **但这恰恰反过来削弱了 \"monitoring\" claim**：如果 c_n 是唯一收敛困难的参数，而 c_n 正是 \"monitoring infrastructure\" 的核心输出，那么论文宣称的监控功能就建立在最不可靠的参数上。R2 说 \"个体 c_n 不可靠则 per-model 诊断无法使用\" 是准确的——Section 5.11 的 facet fit 分析也证实了这一点（7/22 模型 c_n 在可接受范围外，36.4% misfit rate，posterior predictive p = 0.08 borderline）。\n\n---\n\n### R2 Strengths 评价\n\n[AGREE] R2 对论文优势的四点概括（诚实透明、OVB 理论正确、全面分析 battery、graceful degradation 验证）准确。我补充一点：Section 5.10 adversarial robustness 实验虽然暴露了 rank-1 局限性，但也展示了作者对方法边界的诚实探索，这在学术论文中是值得肯定的。\n\n---\n\n### R1 综合判断\n\n**R1 与 R2 在 worst 场景上高度一致**：Overall 评分相同（2.0），核心问题重叠度极高。R2 的 M1-M3 与我独立审稿中的 6 个主要问题（MCMC 收敛、e_i pipeline 无增量、underpowered null、c_n misfit、CI coverage、construct validity）实质上是同一组问题的不同组织方式。\n\n**唯一值得讨论的分歧**：R2 对 Table 7 breakpoint（σ > 0.35）和 Table 3 RMSE（0.55）的引用与论文实际数值有偏差（实际为 σ ≈ 0.28 和 RMSE = 0.42），但这些修正反而**加强**了 R2 的论点——问题比 R2 描述的更严重。\n\n**对作者的建议**：R2 提出的两条改进路径 [(a) 找到 contamination 确实存在的场景, (b) 严格 power analysis] 都可行。我倾向于 (b) 更务实——formal power analysis + minimum detectable c_n 可以在当前数据上完成，无需新实验，且能将 null finding 从 \"我们的工具可能没用\" 升级为 \"在 c_n < X 时任何基于 IRT 的方法都无法检测，这定义了 contamination monitoring 的理论下界\"。",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 交叉回应：R2 对 Worst 场景的审稿意见\n\n**被审论文**: Dream 20260521T215715/worst — \"How Much Contamination Are We Actually Correcting?\"\n**R2 Overall**: 2.0 | **R1 Overall**: 2.0（一致）\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE] R2-M1: \"Calibrated null finding\" 未真正校准**\n\n完全同意核心判断。补充两点：\n\n1. **R2 引用的 RMSE 数值需修正**：R2 称低 c_n (<0.3) 合成恢复 RMSE = 0.55，但 Table 3 实际显示 RMSE = 0.42（G-MFRM）/ 0.85（naive）。不过这不影响结论——在 [0, 0.3] 范围内 RMSE = 0.42 意味着模型基本无法区分 c_n = 0.05 和 c_n = 0.25，R2 的核心论点成立。\n\n2. **CI coverage 问题比 R2 描述的更严重**：78% 是全局覆盖率（Section 5.2），但低 c_n 区间的覆盖率在 Table 3 中未单独报告。考虑到 68% 的模型 c_n < 0.1（Section 5.3），这意味着论文的核心参数估计区间对大多数模型都不可靠，而非仅对少数边缘模型。\n\n3. **强烈支持 R2 关于 formal power analysis 的要求**。论文 Section 7 Limitations 承认了 \"near-zero c_n identifiability\" 问题，但仅定性描述。一篇以 null finding 为核心结论的论文，必须量化 \"minimum detectable c_n\"——否则读者无法判断这是 \"contamination is small\" 还是 \"our tool can't detect it\"。这是 R1 独立审稿中也标记为 critical 的问题。\n\n**[AGREE] R2-M2: \"Monitoring infrastructure\" reframing 缺乏 novelty 和 validation**\n\n逐点回应：\n\n(a) **缺少与更简单监控方案的比较** — 同意。Table 5 对比了 CyclicJudge、DCR、UBA 等作为 ranking 方法，但未将 ConStat-as-monitor 或 LogProber-as-monitor 作为监控替代方案评估。如果论文要声称 G-MFRM 是 \"monitoring infrastructure\"，就需要回答：为什么不直接用 ConStat 做监控？\n\n(b) **\"污染增长则 G-MFRM 价值增加\" 是推测** — 同意。Section 6 的这一论断仅有 Table 6 的合成场景（MVP-001/002/003）间接支撑，但合成场景的 contamination magnitude 是人为设定的，不构成 \"contamination will grow\" 的证据。\n\n(c) **\"监控基础设施\" 不是 EMNLP 研究贡献** — 部分同意。评估方法论属于 EMNLP 范围，但论文交付的是一个在当前条件下不产生增量价值的统计模型，\"monitoring\" 标签本质上是将 null result 包装为 contribution。\n\n(d) **R2 关于 Table 7 breakpoint 的数值需修正**：R2 称 σ > 0.35 时 G-MFRM 劣于 sequential，但 Table 7 显示 breakpoint 在 σ ≈ 0.28。这实际上使问题**更严重**——G-MFRM 在更低的噪声水平就开始退化。考虑到论文自己报告的 composite e_i 质量（Section 4, ρ = 0.47 with ground truth, 仅 43% 的 items 有高置信度估计），真实 e_i 噪声很可能已超过 0.28 breakpoint。\n\n**[AGREE] R2-M3: Novelty 局限于 domain adaptation，null result 使 adaptation 不必要**\n\n这是 R1 和 R2 在所有场景审稿中最一致的共识。补充：\n\n- Table 5 直接证实了 R2 的判断：CyclicJudge+discard 达到 τ = 0.85，与 G-MFRM 完全相同，且不需要 e_i estimation pipeline、MCMC 采样、或任何 contamination modeling。这是 Occam's razor 的经典反例——更简单的方法达到相同结果。\n\n- R2 提出的三重不存在论证 [(a) 问题当前不存在, (b) 可能不以 rank-1 形式存在, (c) 可能被更简单工具解决] 准确且有力。论文自己在 Section 5.10 也承认 adversarial contamination \"is item-specific, not well-approximated by a single c_n per model\"，直接削弱了 rank-1 假设。\n\n- 与 best 场景对比值得强调：best 版本中 τ 提升约 +0.04-0.05、c_n median ~0.95 使得方法论 novelty 不足可以被经验性贡献弥补；worst 版本中 Δτ ≈ 0、c_n median ≈ 0.18，经验性证据完全消失，novelty 不足变成致命缺陷。\n\n---\n\n### Minor 逐条回应\n\n**[AGREE] R2-M4: 缺少 null-result 方法论相关工作和 contamination avoidance 文献**\n\n两个遗漏都是实质性的：\n\n- **Null-result 文献**：如果论文要将 null finding 作为贡献（\"calibrated null\"），需要引用 NLP/ML 领域对 null results 的方法论讨论（Dodge et al. 2019 关于实验报告标准，Rogers et al. 2020 关于 negative results 的价值）。目前的 framing 缺乏方法论锚点。\n\n- **Contamination avoidance 文献**：这是更关键的遗漏。LiveBench（动态更新）、Arena 动态 prompt、private benchmarks 等主动规避策略可能正是当前 contamination 低的原因。如果这些策略有效，G-MFRM 作为 \"被动监控\" 的价值进一步被削弱。论文需要讨论为什么在这些策略存在的情况下，G-MFRM 仍有必要。\n\n**[AGREE] R2-M5: MCMC 收敛问题严重且应对不足**\n\n同意，但补充一个重要 nuance：\n\n- **收敛问题具有参数特异性**：Table 4 清楚显示 θ（ability）和 d（severity）收敛良好（R̂ ≤ 1.04, ESS ≥ 240, 0-2 divergent transitions），问题集中在 c_n（R̂ = 1.12, ESS = 79, 23 divergent transitions）。这意味着论文的排名输出（依赖 θ）可能仍然可靠——Table 5 中 G-MFRM 和 MFRM 的 θ 估计相关性 0.97 也支持这一点。\n\n- **但这恰恰反过来削弱了 \"monitoring\" claim**：如果 c_n 是唯一收敛困难的参数，而 c_n 正是 \"monitoring infrastructure\" 的核心输出，那么论文宣称的监控功能就建立在最不可靠的参数上。R2 说 \"个体 c_n 不可靠则 per-model 诊断无法使用\" 是准确的——Section 5.11 的 facet fit 分析也证实了这一点（7/22 模型 c_n 在可接受范围外，36.4% misfit rate，posterior predictive p = 0.08 borderline）。\n\n---\n\n### R2 Strengths 评价\n\n[AGREE] R2 对论文优势的四点概括（诚实透明、OVB 理论正确、全面分析 battery、graceful degradation 验证）准确。我补充一点：Section 5.10 adversarial robustness 实验虽然暴露了 rank-1 局限性，但也展示了作者对方法边界的诚实探索，这在学术论文中是值得肯定的。\n\n---\n\n### R1 综合判断\n\n**R1 与 R2 在 worst 场景上高度一致**：Overall 评分相同（2.0），核心问题重叠度极高。R2 的 M1-M3 与我独立审稿中的 6 个主要问题（MCMC 收敛、e_i pipeline 无增量、underpowered null、c_n misfit、CI coverage、construct validity）实质上是同一组问题的不同组织方式。\n\n**唯一值得讨论的分歧**：R2 对 Table 7 breakpoint（σ > 0.35）和 Table 3 RMSE（0.55）的引用与论文实际数值有偏差（实际为 σ ≈ 0.28 和 RMSE = 0.42），但这些修正反而**加强**了 R2 的论点——问题比 R2 描述的更严重。\n\n**对作者的建议**：R2 提出的两条改进路径 [(a) 找到 contamination 确实存在的场景, (b) 严格 power analysis] 都可行。我倾向于 (b) 更务实——formal power analysis + minimum detectable c_n 可以在当前数据上完成，无需新实验，且能将 null finding 从 \"我们的工具可能没用\" 升级为 \"在 c_n < X 时任何基于 IRT 的方法都无法检测，这定义了 contamination monitoring 的理论下界\"。",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-22T05:18:36.983567+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4067
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-22T05:18:40.055609+00:00_

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
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
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

_source line 187 · 2026-05-22T05:18:40.106794+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-22T05:18:44.375734+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-22T05:18:44.426407+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T215715/worst/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 190 · 2026-05-22T05:18:49.639464+00:00_

交叉回应已提交。R1 对 R2 的 worst 场景 5 条意见全部 [AGREE]，同时修正了 R2 两处数值引用偏差（Table 3 RMSE 应为 0.42 非 0.55，Table 7 breakpoint 应为 σ ≈ 0.28 非 0.35），这些修正反而加强了 R2 的论点。两位 Reviewer 在 Overall 2.0 评分和核心问题判断上完全一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 9

## Round 9

58 recorded events


### User

_source line 191 · 2026-05-22T16:23:12.578553+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性**审查。

## Venue 信息
- **目标**: EMNLP 2026（ARR May 2026 周期）
- **截止日期**: 2026-05-26
- **类别**: Long paper，正文 8 页限制，参考文献不限
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind

## 论文文件
- LaTeX 主文件: `projects/gated_mfrm_judge_bias/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/submitted.pdf`
- 各章节独立 tex 文件在 `projects/gated_mfrm_judge_bias/docs/paper/` 目录下

## 已知关键问题
- **Section 4 (Experiments) 完全为空**（仅占位注释 `%% [Phase 2: to be written after exp-001 through exp-005 complete]`）
- **Section 6 (Conclusion) 完全为空**
- **Limitations 完全为空**
- 多处交叉引用未解析（Figure ??、Table ??）
- Introduction contribution 4 标注 "numbers TBD"

## 你的审查侧重
请重点审查以下方面：

1. **理论推导的正确性**：
   - Observation 1（OVB formalization）推导是否严格
   - Proposition 1-2 和 Theorem 1（identifiability）证明是否完备
   - Error propagation analysis（§3.4）的 attenuation factor 推导和 σ_crit 阈值
   - Murphy-Topel variance correction 的合理性

2. **模型设计**：
   - G-MFRM 的 gating structure（c_n · e_i）设计合理性
   - 三阶段估计流程的统计基础
   - 正则化 horseshoe prior 的选择和超参数
   - 与 DG-IRT 的差异是否构成足够的方法贡献

3. **实验设计缺失的影响**：
   - 现有 synthetic validation 数据（散布在理论章节中）是否足够支撑 claims
   - 缺少独立 Experiments section 对论文的影响评估
   - Introduction 中声称的 43.8% RMSE reduction 和 τ=0.922——这些结果仅在 introduction 和 method 中提及，无独立实验章节展示

4. **统计方法论**：
   - MCMC 收敛标准（R̂ < 1.05, ESS > 200）是否充分
   - Staged estimation 的 generated regressors 问题处理
   - 合成数据 DGP 的现实性（N=50, I=100, J=8）

请按以下格式输出审稿报告：
- **Summary**（2-3 句）
- **Strengths**（逐条）
- **Weaknesses**（逐条，标注严重程度：[Critical] / [Major] / [Minor]）
- **Questions**（需要作者回答的问题）
- **Missing References**（遗漏的重要相关工作）
- **Overall Assessment**（评分 + 置信度）

使用 EMNLP 2026 ARR 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-22T16:23:21.386590+00:00_

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
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
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

_source line 193 · 2026-05-22T16:23:21.437281+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-22T16:23:25.306610+00:00_

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
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 195 · 2026-05-22T16:23:26.360298+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/submitted.pdf",
  "project": "gated_mfrm_judge_bias",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/submitted.pdf",
    "project": "gated_mfrm_judge_bias",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-22T16:23:26.864273+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/gated_mfrm_judge_bias/docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod43"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/gated_mfrm_judge_bias/docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-prod43"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-22T16:23:33.624814+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines

The recommended workflow for reviewers includes: (1) read the paper and get the first impression, (2) search for re
…[truncated 1430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8318
}
```

</details>

---


### Tool result

_source line 198 · 2026-05-22T16:23:34.781899+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 552.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 198.0}], \"total_pages\": 8, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8421
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-22T16:23:35.688469+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 8824
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-22T16:23:40.867775+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: soundness, excitement/novelty, overall assessment, confidence, reproducibility, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: soundness, excitement/novelty, overall assessment, confidence, reproducibility, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 201 · 2026-05-22T16:23:41.370624+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-22T16:23:42.255058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-22T16:23:42.865534+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1494
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-22T16:23:42.865937+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 205 · 2026-05-22T16:23:43.067879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 206 · 2026-05-22T16:23:43.372195+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1117
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-22T16:23:44.178260+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1312
}
```

</details>

---


### Tool result

_source line 208 · 2026-05-22T16:23:44.279477+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1211
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-22T16:23:48.513542+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: "Quite sure. I tried to check the important points carefully"
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

## 2. **Soundness** (1-5 scale with .5 increments)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: "Strong: This study provides sufficient support for all of its claims"
- 3: "Acceptable: This study provides sufficient support for its main claims"
- 2: "Poor: Some of the main claims are not sufficiently supported"
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement** (1-5 scale with .5 increments)
Measures subjective innovation, impact potential, and relevance to reviewer's interests.
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: "Exciting: I would mention this paper to others"
- 3: "Interesting: I might mention some points of this paper to others"
- 2: "Potentially Interesting: does not resonate with me, but it might with others"
- 1: "Not Exciting: does not resonate with me, and I don't think it would with others"

## 4. **Overall Assessment** (1-5 scale with .5 increments)
- 5: "Consider for Award" (top 2.5% papers)
- 4.5: "Borderline Award"
- 4: "Conference: could be accepted to an *ACL conference"
- 3.5: "Borderline Conference"
- 3: "Findings: could be accepted to the Findings of the ACL"
- 2.5: "Borderline Findings"
- 2: "Resubmit next cycle"
- 1.5: "Resubmit after next cycle"
- 1: "Do not resubmit"

## 5. **Reproducibility** (1-5 scale)
- 5: "They could easily reproduce the results"
- 4: "They could mostly reproduce the results"
- 3: "They could reproduce the results with some difficulty"
- 2: "They would be hard pressed 
…[truncated 461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7645
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-22T16:23:52.800544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 211 · 2026-05-22T16:23:53.201724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 212 · 2026-05-22T16:23:53.655774+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 213 · 2026-05-22T16:23:53.656304+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 214 · 2026-05-22T16:23:54.115296+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 913
}
```

</details>

---


### Tool call

_source line 215 · 2026-05-22T16:23:54.115771+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 216 · 2026-05-22T16:23:54.820764+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-22T16:23:54.871831+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1215
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-22T16:24:00.306298+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-22T16:24:00.357160+00:00_

/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-22T16:24:00.610593+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-22T16:24:00.711365+00:00_

/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-22T16:24:03.894920+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-22T16:24:04.353055+00:00_

1	\section{The G-MFRM Framework}
2	\label{sec:method}
3	
4	Section~\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and a regularized horseshoe prior for the contamination term, are motivated by the identifiability analysis in \S\ref{sec:identifiability} and the error propagation bounds in \S\ref{sec:error_prop}.
5	
6	\subsection{Model Specification}
7	\label{sec:model_spec}
8	
9	G-MFRM extends the standard MFRM \citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\ref{eq:mfrm}):
10	%
11	\begin{equation}
12	\label{eq:gmfrm}
13	\log \frac{P(Y_{nij} \geq k)}{P(Y_{nij} < k)} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i,
14	\end{equation}
15	%
16	where all terms carry the definitions from Section~\ref{sec:confounding}. The gating structure $c_n \cdot e_i$ separates the model-specific and item-specific components of contamination: $c_n \geq 0$ captures how much model $n$ benefits from memorized benchmark content, while $e_i \in [0,1]$ quantifies how much of item $i$ has leaked into training corpora. When $c_n = 0$ (a clean model) or $e_i = 0$ (a novel item), the gating term vanishes and Eq.~\ref{eq:gmfrm} reduces to the standard MFRM. This graceful degradation ensures that G-MFRM imposes no distortion on uncontaminated model-item pairs.
17	
18	We enforce non-negativity and sparsity of $c_n$ through a regularized horseshoe prior \citep{piironen2017horseshoe}. A global shrinkage scale $\tau_c \sim \text{HalfCauchy}(1.0)$ controls the overall contamination level, per-model local scales $\lambda_n \sim \text{HalfCauchy}(1.0)$ allow adaptive
…[truncated 10604 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 458
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-22T16:24:04.353541+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-22T16:24:04.855899+00:00_

1	\section{Confounding in LLM Evaluation}
2	\label{sec:confounding}
3	
4	The Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies
5	%
6	\begin{equation}
7	\label{eq:mfrm}
8	\log \frac{P(Y_{nij} \geq k \mid \theta_n, b_i, d_j, \tau_k)}{P(Y_{nij} < k \mid \theta_n, b_i, d_j, \tau_k)} = \theta_n - b_i - d_j - \tau_k,
9	\end{equation}
10	%
11	where $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\theta_n$ is the ability of model $n$ ($n = 1, \ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \ldots, J$), and $\tau_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for item difficulty and judge severity. \citet{jiao2025mfrm_llm} applied this framework to compare ten LLM raters with human experts, showing that MFRM separates genuine ability from systematic judge effects in multi-judge panels.
12	
13	However, standard MFRM assumes that all systematic sources of score variation are captured by the modeled facets. This assumption breaks down when some models have been exposed to benchmark items during training \citep{dcr2025}. Such contamination inflates scores on exposed items through memorization rather than genuine ability. We represent this effect as an interaction $c_n \cdot e_i$, where $c_n \geq 0$ is the contamination susceptibility of model $n$ and $e_i \in [0, 1]$ is the exposure level of item $i$. The complete data-generating process becomes
14	%
15	\begin{equation}
16	\label{eq:full}
17	\eta_{nijk} = \theta_n - b_i - d_j - \tau_k 
…[truncated 3506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-22T16:24:04.856391+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-22T16:24:05.158637+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large Language Model (LLM) evaluation increasingly relies on LLM-as-a-judge protocols, where one or more LLM judges score model responses on structured benchmarks \citep{zheng2023mtbench}. Two well-documented sources of distortion affect these evaluations: \emph{judge bias}, where different judges assign systematically different scores to the same response, and \emph{benchmark contamination}, where models achieve inflated scores on items encountered during training. Both problems have received sustained research attention, producing separate toolkits for bias calibration and contamination detection. These toolkits treat the two distortions as independent phenomena, a separation that reflects their origins in different research communities rather than any principled argument for independence. Accurate ability ranking is essential for model selection, safety evaluation, and benchmark design; systematic distortion in estimated abilities undermines all three. Yet a practitioner who needs both corrections must apply them sequentially: first correct one source of distortion, then the other. This sequential approach produces unreliable ability estimates. In synthetic experiments with 50 models, 100 items, and 8 judges, sequential estimation yields ability root mean squared error (RMSE) of $0.221 \pm 0.038$, while joint estimation achieves $0.124 \pm 0.016$, a 43.8\% reduction (Wilcoxon $p < 10^{-6}$). The gap does not arise from estimation noise or algorithmic limitations of individual methods; it reflects structural confounding between judge bias and contamination that no sequential pipeline can resolve.
5	
6	Existing judge bias correction methods remove systematic differences across judges without modeling contamination. CyclicJudge \citep{cyclicjudge2026} uses round-robin pairing to cancel average bias through balanced exposure of model pairs to all judges, but treats all residual score variation as genuine abilit
…[truncated 5675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-22T16:24:05.159031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-22T16:24:05.209541+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Judge Bias in LLM Evaluation.}
5	LLM-as-a-judge protocols introduce systematic scoring differences across judges, and several recent methods target this bias in isolation. CyclicJudge \citep{cyclicjudge2026} eliminates average bias through round-robin judge assignment that ensures balanced exposure of model pairs to all judges, but treats all residual score variation as genuine ability signal and provides no per-item diagnostics. UDA \citep{uda2026} learns a neural K-factor adjustment that reduces inter-judge standard deviation by 63.4\%, yet the learned correction is a black-box transformation with no interpretable decomposition of the severity parameter and no mechanism for contamination effects. \citet{fiedler2026bias_uncertainty} formalize judge variability through $J/\Delta J$ diagnostics from classical test theory, identifying sign-reversal failure modes when calibration is shared across judges with heterogeneous severity profiles. These methods model only the judge bias facet: contamination-induced score inflation is absorbed into the estimated abilities, producing the directional bias characterized in Section~\ref{sec:confounding}.
6	
7	\paragraph{Contamination Detection and Adjustment.}
8	A parallel line of work quantifies benchmark contamination at the item or model level without accounting for judge effects. ConStat \citep{constat2024} compares target model performance against a reference model to estimate contamination effects ($r^2 = 0.94$ with true contamination in controlled settings), establishing a principled quantification framework that G-MFRM's Stage~2 builds upon for exposure estimation. DCR \citep{dcr2025} adjusts scores on suspected leaked items through fuzzy inference rules, while LogProber \citep{logprober2024} detects memorization signatures from token-level log-probabilities under gray-box access. Perplexity-based methods such as Min-K\% \citep{mink2024} offer a simpler de
…[truncated 2858 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-22T16:24:10.532858+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-22T16:24:10.934455+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	%% [Phase 2: to be written after exp-001 through exp-005 complete]
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-22T16:24:11.085549+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-22T16:24:11.387005+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	%% [Phase 2: to be written after experiments]
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-22T16:24:11.387456+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-22T16:24:11.889232+00:00_

1	%% [Phase 2: to be written after experiments]
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-22T16:24:11.889624+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-22T16:24:11.940068+00:00_

1	\begin{abstract}
2	LLM-as-a-judge evaluation corrects for judge bias and benchmark contamination independently, but sequential correction produces biased model ability estimates. We formalize this failure as an omitted variable bias (OVB) problem: when judge severity and contamination effects are both present, any estimator that models one while omitting the other yields asymptotically biased ability rankings. We propose the Gated Many-Facet Rasch Model (G-MFRM), which jointly calibrates model ability, item difficulty, judge severity, and contamination susceptibility through staged estimation with externally anchored per-item exposure indicators. Formal identifiability analysis proves that fixing exposure externally is both necessary and sufficient for parameter separation under standard multi-judge designs. Error propagation analysis establishes a critical noise threshold $\sigma_{\mathrm{crit}} = \sqrt{\mathrm{Var}(e_i)}$ below which ability estimates degrade by less than 6\%. In synthetic experiments with 50 models, 100 items, and 8 judges, G-MFRM reduces ability RMSE by 43.8\% relative to sequential estimation (Wilcoxon $p < 10^{-6}$) and achieves Kendall $\tau = 0.922$ with ground-truth rankings versus $\tau = 0.859$ for the best sequential baseline. %% [Phase 2: add real-data results here]
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-22T16:24:12.341750+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-22T16:24:12.444178+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{amsthm}
14	\usepackage{booktabs}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	
18	\newtheorem{observation}{Observation}
19	\newtheorem{proposition}{Proposition}
20	\newtheorem{theorem}{Theorem}
21	\newtheorem{corollary}{Corollary}
22	
23	\graphicspath{{../../figures/paper/}}
24	
25	\title{Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model\\for Disentangling Judge Bias and Contamination in LLM Evaluation}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	\input{introduction}
34	\input{background}
35	\input{method}
36	\input{experiments}
37	\input{related_work}
38	\input{conclusion}
39	
40	\section*{Limitations}
41	\input{limitations}
42	
43	\bibliography{references}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-22T16:25:07.121546+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer responsibilities, what reviewers should focus on, and any specific guidance about how to assess soundness, novelty, and paper completeness. Include any guidance about incomplete submissions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer responsibilities, what reviewers should focus on, and any specific guidance about how to assess soundness, novelty, and paper completeness. Include any guidance about incomplete submissions."
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-22T16:25:13.147046+00:00_

# ARR Reviewer Responsibilities & Assessment Guidance

## Key Reviewer Responsibilities

Reviewers must complete four primary tasks:

1. **Allocate adequate time** for both reviewing and discussion phases
2. **Verify assignment appropriateness** by checking expertise alignment and conflicts of interest
3. **Write substantive reviews** addressing soundness, novelty, and contribution quality
4. **Engage in author discussion** and update assessments based on responses

## Assessment Framework

### Soundness Evaluation
Reviewers assess technical correctness and methodological rigor. Per guidelines: "low soundness scores must be justified by the text of the review." Scores should reflect actual flaws identified, not unconscious biases.

### Novelty & Contribution
The document emphasizes that contributions take multiple forms beyond empirical results—including resources, analyses, reproductions, and surveys. Reviewers shouldn't demand SOTA results when papers make valid scientific contributions through other dimensions (efficiency, interpretability, fairness).

### Completeness Standards

**Papers requiring desk rejection must demonstrate:**
- Style/length violations (exceeding 4 or 8 pages)
- Missing limitations sections
- Inadequate responsible NLP checklist responses
- Hallucinated citations
- Anonymity breaches

**Otherwise incomplete work** should be evaluated contextually. The guidelines caution against penalizing acknowledged limitations as weaknesses.

## Critical Guidance

Reviewers should read papers twice—first for research question and methodology appropriateness, then for technical depth. They must "be specific" rather than vague, cite particular examples, and avoid common heuristic errors like dismissing work for seeming "obvious" or lacking novelty.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6025
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-22T16:27:14.840529+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — 方法严谨性审查报告\n\n## Summary\n\n本文提出 Gated Many-Facet Rasch Model (G-MFRM)，通过在 MFRM 中引入乘法门控项 $c_n \\cdot e_i$ 联合建模 judge bias 和 benchmark contamination。理论框架（OVB formalization、identifiability analysis、error propagation bounds）整体逻辑清晰，是将 psychometric measurement 引入 LLM 评估的有意义尝试。然而，**Section 4 (Experiments)、Section 6 (Conclusion)、Limitations 三个章节完全为空**，论文处于未完成状态，无法作为完整投稿评审。在方法论层面，OVB 从线性模型到序数 logistic 模型的迁移缺乏严格论证，Theorem 1 仅提供 proof sketch，error propagation 的 i.i.d. Gaussian 噪声假设过强。\n\n## Strengths\n\n- **S1**: 将 judge bias 与 contamination 的交互建模为 OVB 问题是一个有洞察力的 framing。Section 2 清晰展示了 sequential estimation 的结构性失败模式（bias-first 和 contamination-first 均产生方向性偏差），Figure 1 的 synthetic validation（r=0.86, p<0.001）直观有力。\n\n- **S2**: Identifiability analysis（§3.3）结构完整——Proposition 1 证明外部固定 $e_i$ 不引入新的不确定性，Proposition 2 证明 exposure variation 的必要性，Theorem 1 给出局部可识别的充分条件。Fisher information determinant 的 Cauchy-Schwarz 论证思路正确。\n\n- **S3**: Error propagation analysis（§3.4）将 staged estimation 的 generated regressors 问题显式量化，定义了 $\\sigma_{\\mathrm{crit}} = \\sqrt{\\mathrm{Var}(e_i)}$ 作为可操作的质量阈值，使 Stage 2 exposure estimation 的精度要求变得可验证（falsifiable）。\n\n- **S4**: 与 DG-IRT 的对比定位清晰（continuous exposure vs. binary, multi-facet vs. single-rater, external estimation vs. known），区分了方法贡献的边界。\n\n- **S5**: Horseshoe prior 的选择合理——contamination 在模型群体中应当是稀疏的，horseshoe 的 adaptive shrinkage 比 Lasso 或 fixed spike-and-slab 更适合这种稀疏结构。\n\n## Weaknesses\n\n### [Critical] W1: 论文严重不完整——Experiments/Conclusion/Limitations 为空\n\nSection 4 仅含占位注释 `%% [Phase 2: to be written after exp-001 through exp-005 complete]`，Section 6 和 Limitations 同样为空。这意味着：\n- 论文声称的 43.8% RMSE reduction 和 τ=0.922（Introduction 第4段、Contribution 3）**没有独立的实验章节展示**，仅以内联数字散布在 §1-§3 中，无法系统验证。\n- Contribution 4 明确标注 \"numbers TBD\"（introduction.tex line 17）。\n- 无 Limitations section 违反 ARR submission requirements（ARR guidelines 将缺少 limitations 列为 desk rejection 条件）。\n- 无 Conclusion 导致论文缺乏对贡献和局限性的总结性讨论。\n\n**影响**：按照 ARR 政策，缺少 Limitations section 可构成 desk rejection。即使不 desk reject，一篇没有独立实验章节的方法论文无法评估其 empirical claims 的可信度。\n\n### [Critical] W2: OVB 从线性模型到非线性模型的迁移缺乏严格论证\n\nObservation 1（§2, Eq. 3）直接将 Angrist & Pischke (2009) 的 OVB 公式 $\\mathrm{plim}(\\tilde{\\theta}_n - \\theta_n) = \\gamma_n \\cdot c_n$ 应用于 MFRM。但 MFRM 是一个 cumulative logit 模型（Eq. 1），OVB 公式在其经典形式下仅对线性模型严格成立。作者在 background.tex line 34 提到 \"In the linear analogue\"，部分承认了这一点，但 Observation 1 的 formal statement 中未做此限定——它被呈现为一个关于 MFRM 的精确结论。\n\n对于非线性模型，omitted variable 的影响更为复杂：(a) bias 的方向和大小取决于参数的真值（不仅仅是 $\\gamma_n \\cdot c_n$），(b) 还存在 collider bias 和 nonlinear interaction 等效应。至少需要引用 nonlinear OVB 的相关文献（如 Wooldridge 2010 §15.8 关于 nonlinear models 中 omitted variables 的讨论），或通过 simulation 验证该近似在 MFRM 参数范围内的精度。\n\n### [Critical] W3: Theorem 1 仅为 proof sketch，未提供完整证明\n\nTheorem 1 是本文最核心的理论贡献之一（identifiability guarantee），但仅提供 \"Proof sketch\"：\n- Fisher information matrix 的 weights $w_{nij}$ 未给出显式定义（它们依赖于真实参数值，意味着 identifiability 是 local 的）。\n- Eq. 6 仅给出 $(\\theta_n, c_n)$ 子块的行列式，但 $b_i$ 和 $d_j$ 对应子块的 non-singularity 仅声称 \"inherit from standard MFRM\" 而无推导。\n- **关键遗漏**：未讨论 cross-blocks 之间的耦合——即使对角子块各自非奇异，完整 Fisher 矩阵的非奇异性还需要子块间交互项不破坏整体结构。一个 block diagonal dominance 论证或对完整矩阵结构的分析是必要的。\n\n对于一篇声称提供 \"formal identifiability guarantees\" 的论文，proof sketch 不足以支撑该 claim。建议将完整证明放入 Appendix。\n\n### [Major] W4: Error propagation 的 i.i.d. Gaussian 假设过强\n\n§3.4 假设 $\\hat{e}_i = e_i + \\epsilon_i$，其中 $\\epsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$ 独立于所有模型参数。这在实际中不太可能成立：\n- **异方差性**：接近边界（$e_i \\approx 0$ 或 $e_i \\approx 1$）的 exposure 估计误差分布与中间值处可能截然不同（类似于 proportion estimation 的 variance structure）。\n- **非独立性**：Stage 2 使用 reference model anchoring 和 cross-model agreement，两者都依赖于 response data 的某些统计量，因此 $\\epsilon_i$ 与 Stage 3 中的参数不完全独立。\n- **非正态性**：exposure 被 clip 到 $[0,1]$，边界效应会导致估计误差呈非对称分布。\n\nEq. 7 的 attenuation factor $\\lambda(\\sigma)$ 是经典 errors-in-variables 结果，在上述假设违背时可能低估或高估实际衰减。§3.4 的具体数字（θ-RMSE 增 5.9%、$c_n$-RMSE 增 7.9%）来自特定 DGP 的 synthetic data，对 realistic scenarios 的外推性未知。\n\n### [Major] W5: Stage 2 exposure estimation 的设计决策缺乏论证\n\nStage 2 是整个方法论的关键环节（因为 identifiability 依赖于外部固定的 $e_i$），但多个设计选择未给出理由：\n- **75%/25% 权重**（reference model anchoring vs. cross-model agreement）：为什么是这个比例？是否做过 sensitivity analysis？\n- **Reference model 选择**（gpt-4-0314）：如果 reference model 本身有 contamination，会引入系统性偏差。这一 circular dependency 未被讨论。\n- **Clipping to [0,1]**：clipping 引入了 bias（真实 exposure 接近边界时估计被截断），这与 §3.4 的 unbiased noise 假设矛盾。\n\n### [Major] W6: 与 DG-IRT 的差异程度是否构成足够的方法贡献\n\n§3.1 最后一段声称 G-MFRM 与 DG-IRT (Shu et al., 2013) 有三个差异：(1) continuous vs. binary exposure, (2) multi-facet vs. single-rater, (3) external vs. known exposure。逐条审视：\n- (1) 从 binary 到 continuous 是参数空间的自然扩展，不涉及新的建模原理。\n- (2) 加入 judge severity $d_j$ 是 MFRM 的标准做法，不是本文的创新。\n- (3) External estimation + staged procedure 是本文的核心贡献，但也引入了 generated regressors 问题。\n\n实质性的方法创新集中在 (3) 以及配套的 identifiability/error propagation 分析。论文需要更清楚地区分 \"组合已有组件\" 和 \"新的方法原理\"。在 experiments section 缺失的情况下，无法判断该组合是否在实践中产生了超越各组件之和的效果。\n\n### [Major] W7: MCMC 收敛标准偏宽松\n\n§3.2 使用 $\\hat{R} < 1.05$ 和 ESS > 200 作为收敛判据。\n- $\\hat{R} < 1.05$ 是旧标准；Vehtari et al. (2021, \"Rank-normalization, folding, and localization\") 推荐 $\\hat{R} < 1.01$，并建议使用 rank-normalized split-$\\hat{R}$。对于 horseshoe prior 这类 heavy-tailed 参数（$\\tau_c$, $\\lambda_n$），标准 $\\hat{R}$ 可能遗漏尾部不收敛。\n- ESS > 200 对于 posterior mean 可能足够，但对 posterior quantiles（credible intervals）不够——Murphy-Topel correction 的可靠性依赖于 posterior 的准确估计。\n- 仅在 footnote 中报告了 synthetic data 的收敛指标（max $\\hat{R}$ = 1.02, min ESS = 276），未讨论 real-data scenario（如模型更多、exposure 分布不同时）的收敛行为。\n\n### [Minor] W8: Theorem 1 条件 (iii) 和 (iv) 冗余\n\n条件 (iii) \"$|\\{e_i\\}| \\geq 2$\"（至少两个不同的 exposure 值）逻辑上蕴含条件 (iv) \"$\\mathrm{Var}(e_i) > 0$\"。在形式化定理中保留冗余条件会影响数学表述的精确性。\n\n### [Minor] W9: $c_n \\geq 0$ 约束的合理性\n\n论文通过 $c_n = |\\tau_c \\cdot \\tilde{\\lambda}_n \\cdot c^{\\mathrm{raw}}_n|$ 强制 $c_n \\geq 0$，隐含假设 contamination 只能提升分数。但存在反例：(a) 模型记忆了旧版 benchmark 答案，与当前评分标准不一致；(b) 对抗性 contamination。至少需要讨论这一假设的适用范围。\n\n### [Minor] W10: 未解析的交叉引用\n\n多处出现 \"Figure ??\" 和 \"Table ??\"（如 §3.4 引用的 Figure 2 和 Table 2），表明论文未经完整编译检查。\n\n## Questions\n\n**Q1**: Observation 1 的 OVB 公式在 MFRM（ordinal logistic model）中的精确适用条件是什么？作者是否验证过该近似在典型 MFRM 参数范围内的误差？\n\n**Q2**: Theorem 1 的完整证明是否可用？特别是，完整 Fisher information matrix 的非奇异性如何从各子块的非奇异性推出？\n\n**Q3**: Stage 2 的 75/25 权重是如何确定的？是否做过不同权重比例的 sensitivity analysis？如果 reference model 本身被 contaminate，Stage 2 的 exposure 估计会如何偏移？\n\n**Q4**: Horseshoe prior 的超参数（$\\tau_c \\sim \\text{HalfCauchy}(1.0)$, $c^2_{\\mathrm{slab}} \\sim \\text{InverseGamma}(2.0, 8.0)$）是否做过 sensitivity analysis？在 contamination 比例不同（如 0% vs. 50% 模型被 contaminate）的场景下，prior 的行为是否稳定？\n\n**Q5**: 论文多次引用 exp-012 的 synthetic results，但无独立实验章节。这些结果的完整实验设定（DGP 参数、随机种子数、baseline 方法细节）在哪里可以找到？\n\n**Q6**: Murphy-Topel variance correction 的具体推导是什么？对 Stage 3 posterior credible intervals 的覆盖率有多大影响？\n\n## Missing References\n\n- **Vehtari, Gelman, Simpson, Carpenter & Bürkner (2021)** \"Rank-normalization, folding, and localization: An improved R̂ for assessing convergence of MCMC\"——关于 MCMC 收敛诊断的当前最佳实践，应替代论文中使用的旧 $\\hat{R} < 1.05$ 标准。\n- **Wooldridge (2010)** *Econometric Analysis of Cross Section and Panel Data*, §15.8——关于非线性模型中 omitted variable bias 的讨论，可支撑 Observation 1 的论证。\n- **Pagan & Hall (1983)** 或 **Murphy & Topel (1985, 2002)** 的完整引用——Murphy-Topel correction 在 method section 中被提及但引用信息不完整。\n\n## Official Dimensions (ACL ARR Review Form)\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 2.5 / 5 | 理论框架有清晰的逻辑骨架，但 OVB 的非线性迁移未严格论证（W2），Theorem 1 仅为 sketch（W3），error propagation 假设过强（W4）。更根本的是，Experiments 完全缺失，所有 empirical claims 无法验证。 |\n| **Excitement** | 3 / 5 | 将 judge bias 与 contamination 联合建模为 measurement model 中的 OVB 问题是一个有价值的视角。如果实验支撑充分，这将是一个对 LLM evaluation 社区有实际影响的工作。但当前状态下 excitement 受限于 incomplete evidence。 |\n| **Reproducibility** | 1 / 5 | 无独立实验章节，无代码，无数据。DGP 参数仅散布在正文和脚注中，不足以复现。 |\n| **Confidence** | 4 / 5 | 我仔细阅读了论文的理论部分（§2-§3），对 MFRM、IRT、horseshoe prior、errors-in-variables 文献有充分了解。对 Experiments 的评估受限于内容缺失。 |\n\n## Overall Assessment\n\n**Overall: 1.5 — Resubmit after next cycle**\n\n**一句话总结**：理论框架有潜力但论证存在关键缺口（W2、W3），且论文严重不完整——Experiments、Conclusion、Limitations 三个章节为空，无法作为 EMNLP 2026 投稿评审。\n\n**详细理由**：\n\n给 1.5 而非 2 的原因：2 分（Resubmit next cycle）意味着\"需大幅修改，可在下一周期完成\"。但本文的问题不仅是缺少实验——即使补上实验，W2（OVB 非线性论证）和 W3（Theorem 1 完整证明）也需要实质性的理论工作。同时，Stage 2 exposure estimation 的设计决策（W5）需要 sensitivity analysis 来支撑，这涉及额外实验。将这些全部完成并确保论文质量，可能超出一个 ARR cycle 的时间。\n\n给 1.5 而非 1 的原因：论文的核心 framing（OVB in joint measurement）是有价值的，identifiability 分析的方向是正确的，staged estimation 的设计逻辑合理。这不是一篇需要\"完全重做\"的论文，而是一篇需要完成和加强的论文。\n\n**如果论文在未来版本中补全以下内容，评分可能提升至 3-3.5**：\n1. 完整的 Experiments section（含 synthetic + real-data validation）\n2. Observation 1 在非线性设置下的严格论证或 simulation-based validation\n3. Theorem 1 的完整证明（可放 Appendix）\n4. Stage 2 exposure estimation 的 sensitivity analysis\n5. Conclusion 和 Limitations sections\n",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — 方法严谨性审查报告\n\n## Summary\n\n本文提出 Gated Many-Facet Rasch Model (G-MFRM)，通过在 MFRM 中引入乘法门控项 $c_n \\cdot e_i$ 联合建模 judge bias 和 benchmark contamination。理论框架（OVB formalization、identifiability analysis、error propagation bounds）整体逻辑清晰，是将 psychometric measurement 引入 LLM 评估的有意义尝试。然而，**Section 4 (Experiments)、Section 6 (Conclusion)、Limitations 三个章节完全为空**，论文处于未完成状态，无法作为完整投稿评审。在方法论层面，OVB 从线性模型到序数 logistic 模型的迁移缺乏严格论证，Theorem 1 仅提供 proof sketch，error propagation 的 i.i.d. Gaussian 噪声假设过强。\n\n## Strengths\n\n- **S1**: 将 judge bias 与 contamination 的交互建模为 OVB 问题是一个有洞察力的 framing。Section 2 清晰展示了 sequential estimation 的结构性失败模式（bias-first 和 contamination-first 均产生方向性偏差），Figure 1 的 synthetic validation（r=0.86, p<0.001）直观有力。\n\n- **S2**: Identifiability analysis（§3.3）结构完整——Proposition 1 证明外部固定 $e_i$ 不引入新的不确定性，Proposition 2 证明 exposure variation 的必要性，Theorem 1 给出局部可识别的充分条件。Fisher information determinant 的 Cauchy-Schwarz 论证思路正确。\n\n- **S3**: Error propagation analysis（§3.4）将 staged estimation 的 generated regressors 问题显式量化，定义了 $\\sigma_{\\mathrm{crit}} = \\sqrt{\\mathrm{Var}(e_i)}$ 作为可操作的质量阈值，使 Stage 2 exposure estimation 的精度要求变得可验证（falsifiable）。\n\n- **S4**: 与 DG-IRT 的对比定位清晰（continuous exposure vs. binary, multi-facet vs. single-rater, external estimation vs. known），区分了方法贡献的边界。\n\n- **S5**: Horseshoe prior 的选择合理——contamination 在模型群体中应当是稀疏的，horseshoe 的 adaptive shrinkage 比 Lasso 或 fixed spike-and-slab 更适合这种稀疏结构。\n\n## Weaknesses\n\n### [Critical] W1: 论文严重不完整——Experiments/Conclusion/Limitations 为空\n\nSection 4 仅含占位注释 `%% [Phase 2: to be written after exp-001 through exp-005 complete]`，Section 6 和 Limitations 同样为空。这意味着：\n- 论文声称的 43.8% RMSE reduction 和 τ=0.922（Introduction 第4段、Contribution 3）**没有独立的实验章节展示**，仅以内联数字散布在 §1-§3 中，无法系统验证。\n- Contribution 4 明确标注 \"numbers TBD\"（introduction.tex line 17）。\n- 无 Limitations section 违反 ARR submission requirements（ARR guidelines 将缺少 limitations 列为 desk rejection 条件）。\n- 无 Conclusion 导致论文缺乏对贡献和局限性的总结性讨论。\n\n**影响**：按照 ARR 政策，缺少 Limitations section 可构成 desk rejection。即使不 desk reject，一篇没有独立实验章节的方法论文无法评估其 empirical claims 的可信度。\n\n### [Critical] W2: OVB 从线性模型到非线性模型的迁移缺乏严格论证\n\nObservation 1（§2, Eq. 3）直接将 Angrist & Pischke (2009) 的 OVB 公式 $\\mathrm{plim}(\\tilde{\\theta}_n - \\theta_n) = \\gamma_n \\cdot c_n$ 应用于 MFRM。但 MFRM 是一个 cumulative logit 模型（Eq. 1），OVB 公式在其经典形式下仅对线性模型严格成立。作者在 background.tex line 34 提到 \"In the linear analogue\"，部分承认了这一点，但 Observation 1 的 formal statement 中未做此限定——它被呈现为一个关于 MFRM 的精确结论。\n\n对于非线性模型，omitted variable 的影响更为复杂：(a) bias 的方向和大小取决于参数的真值（不仅仅是 $\\gamma_n \\cdot c_n$），(b) 还存在 collider bias 和 nonlinear interaction 等效应。至少需要引用 nonlinear OVB 的相关文献（如 Wooldridge 2010 §15.8 关于 nonlinear models 中 omitted variables 的讨论），或通过 simulation 验证该近似在 MFRM 参数范围内的精度。\n\n### [Critical] W3: Theorem 1 仅为 proof sketch，未提供完整证明\n\nTheorem 1 是本文最核心的理论贡献之一（identifiability guarantee），但仅提供 \"Proof sketch\"：\n- Fisher information matrix 的 weights $w_{nij}$ 未给出显式定义（它们依赖于真实参数值，意味着 identifiability 是 local 的）。\n- Eq. 6 仅给出 $(\\theta_n, c_n)$ 子块的行列式，但 $b_i$ 和 $d_j$ 对应子块的 non-singularity 仅声称 \"inherit from standard MFRM\" 而无推导。\n- **关键遗漏**：未讨论 cross-blocks 之间的耦合——即使对角子块各自非奇异，完整 Fisher 矩阵的非奇异性还需要子块间交互项不破坏整体结构。一个 block diagonal dominance 论证或对完整矩阵结构的分析是必要的。\n\n对于一篇声称提供 \"formal identifiability guarantees\" 的论文，proof sketch 不足以支撑该 claim。建议将完整证明放入 Appendix。\n\n### [Major] W4: Error propagation 的 i.i.d. Gaussian 假设过强\n\n§3.4 假设 $\\hat{e}_i = e_i + \\epsilon_i$，其中 $\\epsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$ 独立于所有模型参数。这在实际中不太可能成立：\n- **异方差性**：接近边界（$e_i \\approx 0$ 或 $e_i \\approx 1$）的 exposure 估计误差分布与中间值处可能截然不同（类似于 proportion estimation 的 variance structure）。\n- **非独立性**：Stage 2 使用 reference model anchoring 和 cross-model agreement，两者都依赖于 response data 的某些统计量，因此 $\\epsilon_i$ 与 Stage 3 中的参数不完全独立。\n- **非正态性**：exposure 被 clip 到 $[0,1]$，边界效应会导致估计误差呈非对称分布。\n\nEq. 7 的 attenuation factor $\\lambda(\\sigma)$ 是经典 errors-in-variables 结果，在上述假设违背时可能低估或高估实际衰减。§3.4 的具体数字（θ-RMSE 增 5.9%、$c_n$-RMSE 增 7.9%）来自特定 DGP 的 synthetic data，对 realistic scenarios 的外推性未知。\n\n### [Major] W5: Stage 2 exposure estimation 的设计决策缺乏论证\n\nStage 2 是整个方法论的关键环节（因为 identifiability 依赖于外部固定的 $e_i$），但多个设计选择未给出理由：\n- **75%/25% 权重**（reference model anchoring vs. cross-model agreement）：为什么是这个比例？是否做过 sensitivity analysis？\n- **Reference model 选择**（gpt-4-0314）：如果 reference model 本身有 contamination，会引入系统性偏差。这一 circular dependency 未被讨论。\n- **Clipping to [0,1]**：clipping 引入了 bias（真实 exposure 接近边界时估计被截断），这与 §3.4 的 unbiased noise 假设矛盾。\n\n### [Major] W6: 与 DG-IRT 的差异程度是否构成足够的方法贡献\n\n§3.1 最后一段声称 G-MFRM 与 DG-IRT (Shu et al., 2013) 有三个差异：(1) continuous vs. binary exposure, (2) multi-facet vs. single-rater, (3) external vs. known exposure。逐条审视：\n- (1) 从 binary 到 continuous 是参数空间的自然扩展，不涉及新的建模原理。\n- (2) 加入 judge severity $d_j$ 是 MFRM 的标准做法，不是本文的创新。\n- (3) External estimation + staged procedure 是本文的核心贡献，但也引入了 generated regressors 问题。\n\n实质性的方法创新集中在 (3) 以及配套的 identifiability/error propagation 分析。论文需要更清楚地区分 \"组合已有组件\" 和 \"新的方法原理\"。在 experiments section 缺失的情况下，无法判断该组合是否在实践中产生了超越各组件之和的效果。\n\n### [Major] W7: MCMC 收敛标准偏宽松\n\n§3.2 使用 $\\hat{R} < 1.05$ 和 ESS > 200 作为收敛判据。\n- $\\hat{R} < 1.05$ 是旧标准；Vehtari et al. (2021, \"Rank-normalization, folding, and localization\") 推荐 $\\hat{R} < 1.01$，并建议使用 rank-normalized split-$\\hat{R}$。对于 horseshoe prior 这类 heavy-tailed 参数（$\\tau_c$, $\\lambda_n$），标准 $\\hat{R}$ 可能遗漏尾部不收敛。\n- ESS > 200 对于 posterior mean 可能足够，但对 posterior quantiles（credible intervals）不够——Murphy-Topel correction 的可靠性依赖于 posterior 的准确估计。\n- 仅在 footnote 中报告了 synthetic data 的收敛指标（max $\\hat{R}$ = 1.02, min ESS = 276），未讨论 real-data scenario（如模型更多、exposure 分布不同时）的收敛行为。\n\n### [Minor] W8: Theorem 1 条件 (iii) 和 (iv) 冗余\n\n条件 (iii) \"$|\\{e_i\\}| \\geq 2$\"（至少两个不同的 exposure 值）逻辑上蕴含条件 (iv) \"$\\mathrm{Var}(e_i) > 0$\"。在形式化定理中保留冗余条件会影响数学表述的精确性。\n\n### [Minor] W9: $c_n \\geq 0$ 约束的合理性\n\n论文通过 $c_n = |\\tau_c \\cdot \\tilde{\\lambda}_n \\cdot c^{\\mathrm{raw}}_n|$ 强制 $c_n \\geq 0$，隐含假设 contamination 只能提升分数。但存在反例：(a) 模型记忆了旧版 benchmark 答案，与当前评分标准不一致；(b) 对抗性 contamination。至少需要讨论这一假设的适用范围。\n\n### [Minor] W10: 未解析的交叉引用\n\n多处出现 \"Figure ??\" 和 \"Table ??\"（如 §3.4 引用的 Figure 2 和 Table 2），表明论文未经完整编译检查。\n\n## Questions\n\n**Q1**: Observation 1 的 OVB 公式在 MFRM（ordinal logistic model）中的精确适用条件是什么？作者是否验证过该近似在典型 MFRM 参数范围内的误差？\n\n**Q2**: Theorem 1 的完整证明是否可用？特别是，完整 Fisher information matrix 的非奇异性如何从各子块的非奇异性推出？\n\n**Q3**: Stage 2 的 75/25 权重是如何确定的？是否做过不同权重比例的 sensitivity analysis？如果 reference model 本身被 contaminate，Stage 2 的 exposure 估计会如何偏移？\n\n**Q4**: Horseshoe prior 的超参数（$\\tau_c \\sim \\text{HalfCauchy}(1.0)$, $c^2_{\\mathrm{slab}} \\sim \\text{InverseGamma}(2.0, 8.0)$）是否做过 sensitivity analysis？在 contamination 比例不同（如 0% vs. 50% 模型被 contaminate）的场景下，prior 的行为是否稳定？\n\n**Q5**: 论文多次引用 exp-012 的 synthetic results，但无独立实验章节。这些结果的完整实验设定（DGP 参数、随机种子数、baseline 方法细节）在哪里可以找到？\n\n**Q6**: Murphy-Topel variance correction 的具体推导是什么？对 Stage 3 posterior credible intervals 的覆盖率有多大影响？\n\n## Missing References\n\n- **Vehtari, Gelman, Simpson, Carpenter & Bürkner (2021)** \"Rank-normalization, folding, and localization: An improved R̂ for assessing convergence of MCMC\"——关于 MCMC 收敛诊断的当前最佳实践，应替代论文中使用的旧 $\\hat{R} < 1.05$ 标准。\n- **Wooldridge (2010)** *Econometric Analysis of Cross Section and Panel Data*, §15.8——关于非线性模型中 omitted variable bias 的讨论，可支撑 Observation 1 的论证。\n- **Pagan & Hall (1983)** 或 **Murphy & Topel (1985, 2002)** 的完整引用——Murphy-Topel correction 在 method section 中被提及但引用信息不完整。\n\n## Official Dimensions (ACL ARR Review Form)\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 2.5 / 5 | 理论框架有清晰的逻辑骨架，但 OVB 的非线性迁移未严格论证（W2），Theorem 1 仅为 sketch（W3），error propagation 假设过强（W4）。更根本的是，Experiments 完全缺失，所有 empirical claims 无法验证。 |\n| **Excitement** | 3 / 5 | 将 judge bias 与 contamination 联合建模为 measurement model 中的 OVB 问题是一个有价值的视角。如果实验支撑充分，这将是一个对 LLM evaluation 社区有实际影响的工作。但当前状态下 excitement 受限于 incomplete evidence。 |\n| **Reproducibility** | 1 / 5 | 无独立实验章节，无代码，无数据。DGP 参数仅散布在正文和脚注中，不足以复现。 |\n| **Confidence** | 4 / 5 | 我仔细阅读了论文的理论部分（§2-§3），对 MFRM、IRT、horseshoe prior、errors-in-variables 文献有充分了解。对 Experiments 的评估受限于内容缺失。 |\n\n## Overall Assessment\n\n**Overall: 1.5 — Resubmit after next cycle**\n\n**一句话总结**：理论框架有潜力但论证存在关键缺口（W2、W3），且论文严重不完整——Experiments、Conclusion、Limitations 三个章节为空，无法作为 EMNLP 2026 投稿评审。\n\n**详细理由**：\n\n给 1.5 而非 2 的原因：2 分（Resubmit next cycle）意味着\"需大幅修改，可在下一周期完成\"。但本文的问题不仅是缺少实验——即使补上实验，W2（OVB 非线性论证）和 W3（Theorem 1 完整证明）也需要实质性的理论工作。同时，Stage 2 exposure estimation 的设计决策（W5）需要 sensitivity analysis 来支撑，这涉及额外实验。将这些全部完成并确保论文质量，可能超出一个 ARR cycle 的时间。\n\n给 1.5 而非 1 的原因：论文的核心 framing（OVB in joint measurement）是有价值的，identifiability 分析的方向是正确的，staged estimation 的设计逻辑合理。这不是一篇需要\"完全重做\"的论文，而是一篇需要完成和加强的论文。\n\n**如果论文在未来版本中补全以下内容，评分可能提升至 3-3.5**：\n1. 完整的 Experiments section（含 synthetic + real-data validation）\n2. Observation 1 在非线性设置下的严格论证或 simulation-based validation\n3. Theorem 1 的完整证明（可放 Appendix）\n4. Stage 2 exposure estimation 的 sensitivity analysis\n5. Conclusion 和 Limitations sections\n",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-22T16:27:18.808715+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3968
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-22T16:27:24.872374+00:00_

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
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
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

_source line 245 · 2026-05-22T16:27:24.973195+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-22T16:27:28.638905+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_1/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-22T16:27:28.689642+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 248 · 2026-05-22T16:27:37.002756+00:00_

审稿报告已提交至 Review Director。

**核心判断**：Overall 1.5 (Resubmit after next cycle)。

**关键发现**：
- 论文 Experiments/Conclusion/Limitations 三章全空，缺少 Limitations 可构成 ARR desk rejection
- OVB 公式从线性模型直接迁移到 ordinal logistic MFRM 缺乏严格论证（W2）
- Theorem 1（identifiability）仅提供 proof sketch，完整 Fisher 矩阵的非奇异性论证缺失（W3）
- Error propagation 的 i.i.d. Gaussian 噪声假设不现实（W4）
- Stage 2 exposure estimation 的 75/25 权重和 reference model 选择均无 sensitivity analysis（W5）
- 所有 empirical claims（43.8% RMSE reduction, τ=0.922）仅内联散布于 §1-§3，无独立实验章节展示

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 10

## Round 10

4 recorded events


### User

_source line 249 · 2026-05-22T16:33:18.021929+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并简述理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿报告

**审查侧重**：新颖性与完整性
**Overall**: 1.5 — Resubmit after next cycle
**Confidence**: 4/5

**官方维度**: Soundness 2/5, Excitement 3/5, Reproducibility 1/5

### Summary
本文提出 G-MFRM，将 LLM-as-a-judge 评估中的 judge bias 和 benchmark contamination 统一到一个测量模型中。理论部分展现了清晰的数学推导和 identifiability 分析。然而，三个关键章节（Experiments、Conclusion、Limitations）完全为空，Abstract 和 Introduction 中的定量声明没有对应的实验结果支撑。

### Strengths
- S1: 问题定位精准且重要——将 judge bias 和 contamination 的交互效应形式化为 OVB 问题
- S2: 理论框架严谨——Proposition 1-2, Theorem 1 构成完整识别性论证链
- S3: 错误传播分析有实用价值——σ_crit 为实践者提供定量工具
- S4: 三阶段估计策略设计合理
- S5: Related Work 覆盖面较广

### Must-Fix Weaknesses
- **N1** [Critical]: Section 4 (Experiments) 完全为空——Abstract 声称 43.8% RMSE reduction 和 τ=0.922 无对应表格/图表
- **N2** [Critical]: Conclusion 和 Limitations 完全为空——Limitations 缺失可构成 ARR desk rejection
- **N3** [Critical]: 断裂的交叉引用（Figure ??、Table ??）
- **N4** [Critical]: Introduction Contribution 4 标注 "numbers TBD"

### Should-Fix Weaknesses
- **W1** [Major]: G-MFRM 相对于 DG-IRT 的增量贡献需更充分论证——三个差异本质上是"已有组件的组合"，需消融实验定量展示各组件贡献
- **W2** [Major]: OVB formalization 是已知结果的直接应用——作者自己也承认 "direct application"，但在 Introduction 列为 Contribution 1，贡献层次需校准
- **W3** [Major]: Related Work 遗漏 contamination avoidance 方法范式（LiveBench, SEAL, TRUCE）
- **W4** [Major]: 遗漏近期 IRT+LLM Judge 相关工作（Choi et al., 2026; Polo et al., 2024 tinyBenchmarks）
- **W5** [Minor]: Abstract 中定量声明过于具体但缺乏支撑
- **W6** [Minor]: Figure 1 是唯一实验图表，且仅展示 bias 而非 G-MFRM 性能

### Questions
- Q1: Stage 2 exposure estimation 细节极为模糊——reference model 选择、cross-model agreement 阈值、准确率？
- Q2: Theorem 1 条件在实际 benchmark 中可满足性？大部分 items 的 exposure 未知时怎么办？
- Q3: MCMC 计算成本如何？50 models × 1000 items × 10 judges 的收敛时间？
- Q4: 如果 human annotators 自身也有 bias，G-MFRM 校正后与 human ranking 的差异如何解读？
- Q5: Horseshoe prior 在 contamination 非稀疏场景下是否系统性低估 c_n？

### Missing References
1. LiveBench (White et al., 2024) — contamination avoidance
2. TRUCE (Rajore et al., 2024) — private benchmarking
3. Choi et al. (2026) — IRT for LLM judge reliability, arXiv:2602.00521
4. Polo et al. (2024) — tinyBenchmarks, ICML 2024
5. SEAL (Scale AI, 2024)

---

请逐条回应以上所有 Strengths、Weaknesses 和 Questions。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-22T16:34:49.937308+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n## Overall Assessment 回应\n\n[AGREE] R2 给出 1.5 (Resubmit after next cycle)，与我的评分一致。理由也基本相同：论文严重不完整，且即使补全实验也需要额外理论工作。\n\n---\n\n## Strengths 回应\n\n**[AGREE] R2-S1**: 问题定位精准。OVB framing 确实是本文最有价值的贡献。我在 R1-S1 中同样肯定了这一点，并特别指出 Figure 1 的 synthetic validation（r=0.86）直观展示了 sequential estimation 的结构性失败。\n\n**[REBUT] R2-S2**: \"理论框架严谨\"的措辞过于笼统。Proposition 1-2 的证明确实完备，但 Theorem 1 仅为 proof sketch（§3.3，标注为 \"Proof sketch\"），完整 Fisher information matrix 的非奇异性论证缺失——仅声称 $b_i$, $d_j$ 子块 \"inherit non-singularity from the standard MFRM\"（method.tex line 83），未处理 cross-block 耦合。此外，Observation 1 的 OVB 公式（Eq. 3）从线性模型直接迁移到 cumulative logit 模型未经严格论证（background.tex line 34 自己承认 \"In the linear analogue\"）。识别性论证链的方向正确，但\"严谨\"需要打折扣。\n\n**[AGREE] R2-S3**: $\\sigma_{\\mathrm{crit}}$ 确实有实用价值。但我在 R1-W4 中指出，该分析的 i.i.d. Gaussian 噪声假设（$\\epsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$，method.tex line 93）在 Stage 2 的实际 exposure estimation 中不太可能成立（异方差性、边界效应、与 response data 的非独立性）。实用价值以假设合理性为前提。\n\n**[AGREE] R2-S4**: 三阶段设计逻辑合理，符合 identifiability 分析的要求。\n\n**[AGREE] R2-S5**: Related Work 覆盖面较广，四个平行线（judge bias、contamination detection、preference leakage、IRT/MFRM for LLM）均有涉及。但 R2 后面指出的遗漏（W3、W4）是合理的。\n\n---\n\n## Must-Fix Weaknesses 回应\n\n**[AGREE] R2-N1**: 完全同意。我在 R1-W1 中做了相同判断。补充一点：散布在 §1-§3 中的数字（43.8% RMSE reduction、τ=0.922、r=0.86）缺乏独立实验章节的系统性展示，读者无法判断这些数字的完整实验条件（DGP 参数仅在脚注中部分提及，如 method.tex line 40 的 footnote: N=50, I=100, J=8）。\n\n**[AGREE] R2-N2**: 完全同意。ARR guidelines 明确将缺少 Limitations 列为 desk rejection 条件。我在 R1-W1 中也指出了这一点。\n\n**[AGREE] R2-N3**: 完全同意。§3.4 引用的 Figure 2 和 Table 2（method.tex line 103: \"Figure~\\ref{fig:error_prop} and Table~\\ref{tab:error_prop}\"）在 PDF 中显示为 \"Figure ??\" 和 \"Table ??\"，表明这些 figures/tables 尚未创建或 label 未定义。\n\n**[AGREE] R2-N4**: 完全同意。introduction.tex line 17 明确包含注释 `%% [Phase 2: numbers TBD]`，Contribution 4 关于 Arena-Hard real-data validation 的结果完全缺失。\n\n---\n\n## Should-Fix Weaknesses 回应\n\n**[AGREE] R2-W1**: 与我的 R1-W6 判断一致。G-MFRM 相对 DG-IRT 的三个差异中，(1) continuous vs. binary exposure 是参数空间自然扩展，(2) 加入 $d_j$ 是 MFRM 标准做法，实质创新集中在 (3) external estimation + staged procedure 及配套 identifiability 分析。消融实验（如：仅加 $d_j$ 不加 $c_n$、仅加 $c_n$ 不加 $d_j$、joint vs. staged）是量化各组件贡献的必要手段，但 Experiments section 缺失使这无法评估。\n\n**[REBUT] R2-W2**: 部分不同意。R2 认为 OVB formalization \"是已知结果的直接应用\"因此贡献层次需校准。但我认为贡献不在于 OVB 公式本身，而在于**将 judge bias 和 contamination 的交互识别为 OVB 问题**——这个 problem identification 是新的。Section 2 清晰展示了为什么 sequential correction（无论 bias-first 还是 contamination-first）在结构上无法解决这个问题（background.tex line 36），synthetic validation 也验证了这一预测（r=0.86）。将 Observation 1 列为 Contribution 1 在层次上是合适的——它为整篇论文提供了动机和理论基础。但我同意 R2 的隐含观点：作为 Contribution 1，它需要更严格的论证（即我在 R1-W2 中指出的非线性模型迁移问题）。\n\n**[AGREE] R2-W3**: 遗漏 contamination avoidance 方法（LiveBench、SEAL、TRUCE）是一个有效批评。这类方法代表了一种完全不同的应对范式（避免 contamination 而非建模它），论文应在 Related Work 中讨论并解释为什么 post-hoc modeling 仍然必要（例如：即使用新 benchmark，旧数据仍在训练集中；动态更新成本高）。\n\n**[REBUT] R2-W4**: 部分不同意。R2 列出的参考中：\n- **Polo et al. (2024) tinyBenchmarks**：这是关于 benchmark 效率（用少量 items 估计能力）的工作，与 judge bias/contamination 建模不直接相关，可列可不列。\n- **Choi et al. (2026)**：如果确实是关于 IRT for LLM judge reliability 的近期工作，则相关度高，应当引用。但需核实该引用的真实性（arXiv:2602.00521 的 \"2602\" 前缀对应 2026年2月，时间线合理但无法在当前审稿中验证）。\n- 总体而言，Related Work 已覆盖了主要方法族（§5 的四个段落），遗漏个别论文是正常的，不构成 major weakness。建议降为 minor。\n\n**[AGREE] R2-W5**: Abstract 中 \"43.8% RMSE reduction\"、\"τ=0.922\"、\"Wilcoxon $p < 10^{-6}$\" 这些具体数字在没有独立实验章节支撑的情况下出现在 abstract 中确实不妥。\n\n**[AGREE] R2-W6**: Figure 1 是全文唯一的实验性图表，仅展示 OVB bias 的存在（sequential estimation bias vs. true $c_n$），不展示 G-MFRM 的性能。这对于一篇提出新方法的论文来说不够——至少需要一个展示 G-MFRM vs. baselines 性能对比的图表。\n\n---\n\n## Questions 回应\n\n**[AGREE] R2-Q1**: 与我的 R1-W5 判断一致。Stage 2 的 exposure estimation 是全文方法论的 Achilles' heel：reference model 选择标准、75/25 权重理由、cross-model agreement 的具体计算方式（z-score standardization 的细节）、以及 exposure 估计的准确率均未报告。对于 identifiability 完全依赖于外部固定 $e_i$ 的方法，这些细节至关重要。\n\n**[AGREE] R2-Q2**: 好问题。Theorem 1 条件 (i) 要求 fully crossed design（所有 $N \\times I \\times J$ cells observed），但实际 LLM evaluation 中常用 sparse design（每个 judge 只评一部分 items）。条件 (iii) 要求至少两个不同的 exposure 值——在 exposure 未知（需要 Stage 2 估计）的情况下，这变成了一个 chicken-and-egg 问题：identifiability 依赖 $e_i$ 的 variation，但 $e_i$ 的估计质量未经独立验证。论文应讨论这些条件在实际中的可满足性。\n\n**[AGREE] R2-Q3**: 计算成本是实用性的关键考量。论文未报告任何计算时间。MCMC（NUTS）在高维参数空间（$N + I + J + N + K$ 参数）的 scaling behavior 需要讨论——尤其是 horseshoe prior 引入的 funnel geometry 可能导致 NUTS 步长适应困难。\n\n**[AGREE] R2-Q4**: 这是一个有深度的问题。§3.5 将 G-MFRM 的 $\\theta_n$ posterior mean 定义为 \"fair score\"，但如果 ground truth 本身来自有 bias 的 human annotators（如 Chatbot Arena 的 ELO ratings），那么 G-MFRM 与 human ranking 的对齐度高不一定意味着校正正确——也可能意味着 G-MFRM 继承了 human bias。论文需要讨论 validation ground truth 的局限性。\n\n**[REBUT] R2-Q5**: 部分不同意这个担忧的严重程度。Horseshoe prior 的设计目标确实是稀疏场景（少数 $c_n$ 大，多数接近 0）。但 regularized horseshoe（Piironen & Vehtari, 2017）的 slab component $c^2_{\\mathrm{slab}} \\sim \\text{InverseGamma}(2.0, 8.0)$ 正是为了防止对非零信号的过度收缩——它为大的 $c_n$ 提供了一个有限的 slab，避免经典 horseshoe 的 unbounded tail 问题。在 contamination 非稀疏场景下（如 >50% 模型被 contaminate），全局收缩参数 $\\tau_c$ 的 posterior 会被 data 推高，减弱收缩效果。这是 horseshoe 的自适应机制，不一定导致系统性低估。但作者确实应做 sensitivity analysis 验证这一点（与我的 R1 Q4 一致）。\n\n---\n\n## Missing References 回应\n\n**[AGREE]** LiveBench (White et al., 2024) — contamination avoidance 范式的代表，应在 Related Work 中讨论。\n\n**[AGREE]** TRUCE (Rajore et al., 2024) — private benchmarking 方向，与 LiveBench 同属 avoidance 范式，至少应提及。\n\n**[NEUTRAL]** Choi et al. (2026) arXiv:2602.00521 — 无法验证该引用的真实性和内容。如果确实是 IRT for LLM judge reliability 的近期工作，则高度相关。建议 Director 核实。\n\n**[REBUT]** Polo et al. (2024) tinyBenchmarks — 这是关于 benchmark efficiency 的工作（用 IRT 选择少量 representative items），与 judge bias/contamination 建模的 framing 不同。可选引用，但遗漏不构成 weakness。\n\n**[AGREE]** SEAL (Scale AI, 2024) — 如果是 private evaluation 方向的代表工作，应与 LiveBench/TRUCE 一起在 contamination avoidance 段落中提及。\n\n---\n\n## 总结\n\n与 R2 在主要判断上高度一致：论文不完整是最核心问题（N1-N4），Overall 1.5 合理。在具体 weakness 上有两处分歧：(1) W2——OVB 作为 Contribution 1 的定位在 problem identification 层面是合适的，问题在于论证严格性而非贡献层次；(2) W4——遗漏个别论文是正常的，不应升至 major。我额外指出了 R2 未覆盖的方法论问题：OVB 非线性迁移（R1-W2）、Theorem 1 proof sketch 不完整（R1-W3）、error propagation 的 i.i.d. 假设（R1-W4）、MCMC 收敛标准偏宽松（R1-W7）。\n",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n## Overall Assessment 回应\n\n[AGREE] R2 给出 1.5 (Resubmit after next cycle)，与我的评分一致。理由也基本相同：论文严重不完整，且即使补全实验也需要额外理论工作。\n\n---\n\n## Strengths 回应\n\n**[AGREE] R2-S1**: 问题定位精准。OVB framing 确实是本文最有价值的贡献。我在 R1-S1 中同样肯定了这一点，并特别指出 Figure 1 的 synthetic validation（r=0.86）直观展示了 sequential estimation 的结构性失败。\n\n**[REBUT] R2-S2**: \"理论框架严谨\"的措辞过于笼统。Proposition 1-2 的证明确实完备，但 Theorem 1 仅为 proof sketch（§3.3，标注为 \"Proof sketch\"），完整 Fisher information matrix 的非奇异性论证缺失——仅声称 $b_i$, $d_j$ 子块 \"inherit non-singularity from the standard MFRM\"（method.tex line 83），未处理 cross-block 耦合。此外，Observation 1 的 OVB 公式（Eq. 3）从线性模型直接迁移到 cumulative logit 模型未经严格论证（background.tex line 34 自己承认 \"In the linear analogue\"）。识别性论证链的方向正确，但\"严谨\"需要打折扣。\n\n**[AGREE] R2-S3**: $\\sigma_{\\mathrm{crit}}$ 确实有实用价值。但我在 R1-W4 中指出，该分析的 i.i.d. Gaussian 噪声假设（$\\epsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$，method.tex line 93）在 Stage 2 的实际 exposure estimation 中不太可能成立（异方差性、边界效应、与 response data 的非独立性）。实用价值以假设合理性为前提。\n\n**[AGREE] R2-S4**: 三阶段设计逻辑合理，符合 identifiability 分析的要求。\n\n**[AGREE] R2-S5**: Related Work 覆盖面较广，四个平行线（judge bias、contamination detection、preference leakage、IRT/MFRM for LLM）均有涉及。但 R2 后面指出的遗漏（W3、W4）是合理的。\n\n---\n\n## Must-Fix Weaknesses 回应\n\n**[AGREE] R2-N1**: 完全同意。我在 R1-W1 中做了相同判断。补充一点：散布在 §1-§3 中的数字（43.8% RMSE reduction、τ=0.922、r=0.86）缺乏独立实验章节的系统性展示，读者无法判断这些数字的完整实验条件（DGP 参数仅在脚注中部分提及，如 method.tex line 40 的 footnote: N=50, I=100, J=8）。\n\n**[AGREE] R2-N2**: 完全同意。ARR guidelines 明确将缺少 Limitations 列为 desk rejection 条件。我在 R1-W1 中也指出了这一点。\n\n**[AGREE] R2-N3**: 完全同意。§3.4 引用的 Figure 2 和 Table 2（method.tex line 103: \"Figure~\\ref{fig:error_prop} and Table~\\ref{tab:error_prop}\"）在 PDF 中显示为 \"Figure ??\" 和 \"Table ??\"，表明这些 figures/tables 尚未创建或 label 未定义。\n\n**[AGREE] R2-N4**: 完全同意。introduction.tex line 17 明确包含注释 `%% [Phase 2: numbers TBD]`，Contribution 4 关于 Arena-Hard real-data validation 的结果完全缺失。\n\n---\n\n## Should-Fix Weaknesses 回应\n\n**[AGREE] R2-W1**: 与我的 R1-W6 判断一致。G-MFRM 相对 DG-IRT 的三个差异中，(1) continuous vs. binary exposure 是参数空间自然扩展，(2) 加入 $d_j$ 是 MFRM 标准做法，实质创新集中在 (3) external estimation + staged procedure 及配套 identifiability 分析。消融实验（如：仅加 $d_j$ 不加 $c_n$、仅加 $c_n$ 不加 $d_j$、joint vs. staged）是量化各组件贡献的必要手段，但 Experiments section 缺失使这无法评估。\n\n**[REBUT] R2-W2**: 部分不同意。R2 认为 OVB formalization \"是已知结果的直接应用\"因此贡献层次需校准。但我认为贡献不在于 OVB 公式本身，而在于**将 judge bias 和 contamination 的交互识别为 OVB 问题**——这个 problem identification 是新的。Section 2 清晰展示了为什么 sequential correction（无论 bias-first 还是 contamination-first）在结构上无法解决这个问题（background.tex line 36），synthetic validation 也验证了这一预测（r=0.86）。将 Observation 1 列为 Contribution 1 在层次上是合适的——它为整篇论文提供了动机和理论基础。但我同意 R2 的隐含观点：作为 Contribution 1，它需要更严格的论证（即我在 R1-W2 中指出的非线性模型迁移问题）。\n\n**[AGREE] R2-W3**: 遗漏 contamination avoidance 方法（LiveBench、SEAL、TRUCE）是一个有效批评。这类方法代表了一种完全不同的应对范式（避免 contamination 而非建模它），论文应在 Related Work 中讨论并解释为什么 post-hoc modeling 仍然必要（例如：即使用新 benchmark，旧数据仍在训练集中；动态更新成本高）。\n\n**[REBUT] R2-W4**: 部分不同意。R2 列出的参考中：\n- **Polo et al. (2024) tinyBenchmarks**：这是关于 benchmark 效率（用少量 items 估计能力）的工作，与 judge bias/contamination 建模不直接相关，可列可不列。\n- **Choi et al. (2026)**：如果确实是关于 IRT for LLM judge reliability 的近期工作，则相关度高，应当引用。但需核实该引用的真实性（arXiv:2602.00521 的 \"2602\" 前缀对应 2026年2月，时间线合理但无法在当前审稿中验证）。\n- 总体而言，Related Work 已覆盖了主要方法族（§5 的四个段落），遗漏个别论文是正常的，不构成 major weakness。建议降为 minor。\n\n**[AGREE] R2-W5**: Abstract 中 \"43.8% RMSE reduction\"、\"τ=0.922\"、\"Wilcoxon $p < 10^{-6}$\" 这些具体数字在没有独立实验章节支撑的情况下出现在 abstract 中确实不妥。\n\n**[AGREE] R2-W6**: Figure 1 是全文唯一的实验性图表，仅展示 OVB bias 的存在（sequential estimation bias vs. true $c_n$），不展示 G-MFRM 的性能。这对于一篇提出新方法的论文来说不够——至少需要一个展示 G-MFRM vs. baselines 性能对比的图表。\n\n---\n\n## Questions 回应\n\n**[AGREE] R2-Q1**: 与我的 R1-W5 判断一致。Stage 2 的 exposure estimation 是全文方法论的 Achilles' heel：reference model 选择标准、75/25 权重理由、cross-model agreement 的具体计算方式（z-score standardization 的细节）、以及 exposure 估计的准确率均未报告。对于 identifiability 完全依赖于外部固定 $e_i$ 的方法，这些细节至关重要。\n\n**[AGREE] R2-Q2**: 好问题。Theorem 1 条件 (i) 要求 fully crossed design（所有 $N \\times I \\times J$ cells observed），但实际 LLM evaluation 中常用 sparse design（每个 judge 只评一部分 items）。条件 (iii) 要求至少两个不同的 exposure 值——在 exposure 未知（需要 Stage 2 估计）的情况下，这变成了一个 chicken-and-egg 问题：identifiability 依赖 $e_i$ 的 variation，但 $e_i$ 的估计质量未经独立验证。论文应讨论这些条件在实际中的可满足性。\n\n**[AGREE] R2-Q3**: 计算成本是实用性的关键考量。论文未报告任何计算时间。MCMC（NUTS）在高维参数空间（$N + I + J + N + K$ 参数）的 scaling behavior 需要讨论——尤其是 horseshoe prior 引入的 funnel geometry 可能导致 NUTS 步长适应困难。\n\n**[AGREE] R2-Q4**: 这是一个有深度的问题。§3.5 将 G-MFRM 的 $\\theta_n$ posterior mean 定义为 \"fair score\"，但如果 ground truth 本身来自有 bias 的 human annotators（如 Chatbot Arena 的 ELO ratings），那么 G-MFRM 与 human ranking 的对齐度高不一定意味着校正正确——也可能意味着 G-MFRM 继承了 human bias。论文需要讨论 validation ground truth 的局限性。\n\n**[REBUT] R2-Q5**: 部分不同意这个担忧的严重程度。Horseshoe prior 的设计目标确实是稀疏场景（少数 $c_n$ 大，多数接近 0）。但 regularized horseshoe（Piironen & Vehtari, 2017）的 slab component $c^2_{\\mathrm{slab}} \\sim \\text{InverseGamma}(2.0, 8.0)$ 正是为了防止对非零信号的过度收缩——它为大的 $c_n$ 提供了一个有限的 slab，避免经典 horseshoe 的 unbounded tail 问题。在 contamination 非稀疏场景下（如 >50% 模型被 contaminate），全局收缩参数 $\\tau_c$ 的 posterior 会被 data 推高，减弱收缩效果。这是 horseshoe 的自适应机制，不一定导致系统性低估。但作者确实应做 sensitivity analysis 验证这一点（与我的 R1 Q4 一致）。\n\n---\n\n## Missing References 回应\n\n**[AGREE]** LiveBench (White et al., 2024) — contamination avoidance 范式的代表，应在 Related Work 中讨论。\n\n**[AGREE]** TRUCE (Rajore et al., 2024) — private benchmarking 方向，与 LiveBench 同属 avoidance 范式，至少应提及。\n\n**[NEUTRAL]** Choi et al. (2026) arXiv:2602.00521 — 无法验证该引用的真实性和内容。如果确实是 IRT for LLM judge reliability 的近期工作，则高度相关。建议 Director 核实。\n\n**[REBUT]** Polo et al. (2024) tinyBenchmarks — 这是关于 benchmark efficiency 的工作（用 IRT 选择少量 representative items），与 judge bias/contamination 建模的 framing 不同。可选引用，但遗漏不构成 weakness。\n\n**[AGREE]** SEAL (Scale AI, 2024) — 如果是 private evaluation 方向的代表工作，应与 LiveBench/TRUCE 一起在 contamination avoidance 段落中提及。\n\n---\n\n## 总结\n\n与 R2 在主要判断上高度一致：论文不完整是最核心问题（N1-N4），Overall 1.5 合理。在具体 weakness 上有两处分歧：(1) W2——OVB 作为 Contribution 1 的定位在 problem identification 层面是合适的，问题在于论证严格性而非贡献层次；(2) W4——遗漏个别论文是正常的，不应升至 major。我额外指出了 R2 未覆盖的方法论问题：OVB 非线性迁移（R1-W2）、Theorem 1 proof sketch 不完整（R1-W3）、error propagation 的 i.i.d. 假设（R1-W4）、MCMC 收敛标准偏宽松（R1-W7）。\n",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-22T16:34:53.756388+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3819
}
```

</details>

---


### Assistant

_source line 252 · 2026-05-22T16:34:59.427750+00:00_

已提交对 Reviewer 2 的逐条回应。主要结论：

- **高度一致**：论文不完整（N1-N4）、Overall 1.5、DG-IRT 增量贡献需消融实验（W1）、Stage 2 细节模糊（Q1）
- **两处分歧**：W2（OVB 作为 Contribution 1 的定位在 problem identification 层面合理，问题在论证严格性）；W4（遗漏个别论文不构成 major weakness）
- **补充 R2 未覆盖的问题**：OVB 非线性迁移、Theorem 1 仅 sketch、error propagation i.i.d. 假设、MCMC 收敛标准偏松

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 11

## Round 11

84 recorded events


### User

_source line 253 · 2026-05-23T01:02:56.623547+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。

## 投稿信息
- **Venue**: EMNLP 2026（通过 ARR May 2026 投稿）
- **Deadline**: 2026-05-26
- **类型**: Long paper（正文 8 页限制，参考文献无限，Limitations/Ethics 不计入页数）
- **模板**: ACL style（\usepackage[review]{acl}）
- **匿名规则**: Double-blind（作者信息已匿名为 "Anonymous"）
- **论文路径**: `projects/gated_mfrm_judge_bias/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/submitted.pdf`

## 你的审查侧重

### 1. OVB 理论论证
- Observation 1 将线性 OVB 公式应用于 ordinal logistic MFRM（非线性模型），论文自称"linear approximation"——评估这个近似的合理性和局限性
- 近似质量仅靠 Pearson r=0.86 的 simulation 验证，是否足够？
- γ_n 的具体形式未给出，这对理论贡献的完整性有何影响？

### 2. Identifiability 分析
- Theorem 1 的四个条件是否 minimal（特别关注条件 iii 和 iv 是否冗余）
- Proposition 1 的证明是否严格（"e_i ≠ 0 for at least one item by assumption" 这个假设是否合理）
- Appendix A 完整证明的 Schur complement 论证是否 sound

### 3. MCMC 收敛与统计问题
- §3.2 声称 threshold R̂ < 1.01 和 ESS > 400，但 §4.2 报告 R̂ ≤ 1.03 和 minimum ESS = 217——这个不一致需要严格审查
- CI coverage 71% vs nominal 95%——这是严重的 posterior calibration 问题还是可接受的？
- 4,000 warmup + 4,000 sampling × 4 chains 的配置是否充分？

### 4. 实验设计与统计显著性
- 核心结果 τ=0.857 vs 0.786，bootstrap Δτ CI 包含零——如何评价这个"nominally higher but not significant"的主张？
- posterior median τ 等于 baseline (0.786)，point estimate 在分布上尾——这是否削弱了论文的核心声明？
- 全部 7 个 baseline 产生完全相同的 ranking（τ=0.786, ρ=0.905）——这是合理的还是可疑的？
- 合成实验 N=50 显著但真实数据 N=8 不显著——这种 gap 是否被充分讨论？
- Error propagation 实验用 20 seeds，ablation 用 10 seeds（标注 "preliminary"）——是否充分？

### 5. Stage 2 Exposure Estimation
- 75/25 权重缺乏 sensitivity analysis（论文只说 Spearman ρ≥0.998，但这只说明不同权重下 exposure ranking 稳定，不代表 downstream τ 也稳定）
- reference model anchor (gpt-4-0314) 的选择——是否存在 anchor 本身被 contaminate 的风险？
- clipping to [0,1] 对极端值的影响

### 6. 数据一致性检查
- §4.1 列出 6 judges: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B, Llama 4 Maverick
- §4.2 severity 结果列出: Claude Opus +0.60, GPT-5.5 +0.53, DeepSeek +0.31, Mistral -0.74, LLaMA -0.42, Qwen2.5-72B -0.35
- 这两组名称不匹配（Claude Sonnet 去哪了？Mistral 从哪来的？Qwen3-235B vs Qwen2.5-72B？）——这是致命的数据不一致还是命名问题？

请按 ARR 审稿标准产出完整审稿意见，包含 Summary、Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、Missing References。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-23T01:03:05.295020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-23T01:03:06.450596+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/review_reviewer_1_51c3c93c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-23T01:03:06.651722+00:00_

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
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
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

_source line 257 · 2026-05-23T01:03:06.652193+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-23T01:03:13.235409+00:00_

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
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 259 · 2026-05-23T01:03:13.486843+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form scoring dimensions 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form scoring dimensions 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-23T01:03:14.498694+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/submitted.pdf",
  "project": "gated_mfrm_judge_bias",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/submitted.pdf",
    "project": "gated_mfrm_judge_bias",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-23T01:03:21.089530+00:00_

Web search results for query: "ACL Rolling Review review form scoring dimensions 2025 2026"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"}]

Based on the search results, here's what I found about the ACL Rolling Review form scoring dimensions for 2025-2026:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

**Soundness Score:**
The soundness scores must be justified by the text of the review.

**Excitement Score:**
How exciting is this paper for you? Excitement is subjective, and does not necessarily follow what is popular in the field. The review form explains that reviewers may be excited about papers that are transformational/innovative, have broad impact, or are relevant to their own research.

**Overall Recommendation:**
The form includes recommendation levels, with examples including "Consider 
…[truncated 537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7602
}
```

</details>

---


### Tool result

_source line 262 · 2026-05-23T01:03:22.750625+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

I found information about ACL ARR 2026 reviewer guidelines and review form criteria. Here's what the search results show:

## Review Form Criteria

For Findings papers, the main criteria are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factor
…[truncated 1174 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9515
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-23T01:03:24.815000+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 539.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.0}], \"total_pages\": 13, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 10316
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-23T01:03:32.990273+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract ALL scoring dimensions, their scales, and detailed descriptions from the ARR review form. Include: soundness, excitement, overall assessment, confidence, and any other dimensions. For each dimension, list the exact scale options and descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract ALL scoring dimensions, their scales, and detailed descriptions from the ARR review form. Include: soundness, excitement, overall assessment, confidence, and any other dimensions. For each dimension, list the exact scale options and descriptions."
  }
}
```

</details>

---


### Tool call

_source line 265 · 2026-05-23T01:03:33.943788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-23T01:03:34.601217+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-23T01:03:34.957367+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1013
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-23T01:03:34.957814+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-23T01:03:35.918243+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1317
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-23T01:03:36.019270+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-23T01:03:36.371441+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1413
}
```

</details>

---


### Tool result

_source line 272 · 2026-05-23T01:03:36.777093+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 757
}
```

</details>

---


### Tool call

_source line 273 · 2026-05-23T01:03:36.827996+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/submitted.pdf",
  "project": "gated_mfrm_judge_bias",
  "pages": "9-13",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/submitted.pdf",
    "project": "gated_mfrm_judge_bias",
    "pages": "9-13",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 274 · 2026-05-23T01:03:40.492203+00:00_

# ARR Review Form Scoring Dimensions

## 1. Reviewer Confidence
**Scale:** 1-5
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully."
- **3:** "Pretty sure, but there's a chance I missed something."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1:** "Not my area, or paper is very hard to understand."

## 2. Soundness
**Scale:** 1-5 (with 0.5 increments)
- **5:** "Excellent: This study is one of the most thorough I have seen."
- **4:** "Strong: This study provides sufficient support for all claims."
- **3:** "Acceptable: This study provides sufficient support for main claims."
- **2:** "Poor: Some main claims lack sufficient support; major technical problems exist."
- **1:** "Major Issues: Study insufficient for publication or not relevant to ACL."

## 3. Excitement
**Scale:** 1-5 (with 0.5 increments)
- **5:** "Highly Exciting: I would recommend this paper to others."
- **4:** "Exciting: I would mention this paper to others."
- **3:** "Interesting: I might mention some points to others."
- **2:** "Potentially Interesting: doesn't resonate with me personally."
- **1:** "Not Exciting: unlikely to resonate with others in the community."

## 4. Overall Assessment
**Scale:** 1-5 (with 0.5 increments)
- **5:** Consider for Award (top 2.5% papers)
- **4:** Conference acceptance recommended
- **3:** Findings acceptance recommended
- **2:** Substantial revisions needed by next cycle
- **1:** Do not resubmit or not relevant to ACL

## 5. Reproducibility
**Scale:** 1-5
- **5:** Results could be easily reproduced
- **4:** Results mostly reproducible with minor variations
- **3:** Reproducible with difficulty; underspecified parameters
- **2:** Hard to reproduce; data unavailable or insufficient details
- **1:** Unable to reproduce regardless of effort

## 6. Datasets (if applicable)
**Scale:*
…[truncated 653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7501
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-23T01:03:41.148705+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.7}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.6}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 406.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 365.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 70.0}], \"total_pages\": 13, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4320
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-23T01:03:46.522745+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 277 · 2026-05-23T01:03:47.077190+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-23T01:03:47.585744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-23T01:03:48.148604+00:00_

Image file is empty: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p7.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 562
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-23T01:03:48.149017+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-23T01:03:48.869501+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2346
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-23T01:03:48.870095+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-23T01:03:49.279658+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/review_reviewer_1_51c3c93c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 409
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-23T01:03:49.280072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-23T01:03:49.733509+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2656
}
```

</details>

---


### Tool result

_source line 286 · 2026-05-23T01:03:49.734571+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1585
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-23T01:03:49.737237+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/review_reviewer_1_51c3c93c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 457
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-23T01:03:49.737550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-23T01:03:50.189368+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/review_reviewer_1_51c3c93c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-23T01:03:50.189821+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-23T01:03:50.691883+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/review_reviewer_1_51c3c93c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-23T01:03:50.692383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-23T01:03:50.796618+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/review_reviewer_1_51c3c93c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 104
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-23T01:03:57.320762+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/submitted.pdf",
  "project": "gated_mfrm_judge_bias",
  "pages": "7",
  "dpi": "150",
  "output_dir": "/tmp/pdf_review_r1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/submitted.pdf",
    "project": "gated_mfrm_judge_bias",
    "pages": "7",
    "dpi": "150",
    "output_dir": "/tmp/pdf_review_r1"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-23T01:03:57.825953+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 7, \"path\": \"/tmp/pdf_review_r1/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 539.9}], \"total_pages\": 13, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/tmp/pdf_review_r1\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-23T01:03:58.437640+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/submitted.pdf",
  "project": "gated_mfrm_judge_bias",
  "pages": "9-13",
  "dpi": "150",
  "output_dir": "/tmp/pdf_review_r1_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_2/submitted.pdf",
    "project": "gated_mfrm_judge_bias",
    "pages": "9-13",
    "dpi": "150",
    "output_dir": "/tmp/pdf_review_r1_2"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-23T01:03:59.698844+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/tmp/pdf_review_r1_2/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.7}, {\"page\": 10, \"path\": \"/tmp/pdf_review_r1_2/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.6}, {\"page\": 11, \"path\": \"/tmp/pdf_review_r1_2/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 406.8}, {\"page\": 12, \"path\": \"/tmp/pdf_review_r1_2/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 365.7}, {\"page\": 13, \"path\": \"/tmp/pdf_review_r1_2/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 70.0}], \"total_pages\": 13, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/tmp/pdf_review_r1_2\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1261
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-23T01:04:01.967554+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pdf_review_r1/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pdf_review_r1/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 299 · 2026-05-23T01:04:02.170665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pdf_review_r1_2/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pdf_review_r1_2/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-23T01:04:02.641393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pdf_review_r1_2/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pdf_review_r1_2/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 301 · 2026-05-23T01:04:02.942893+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pdf_review_r1_2/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pdf_review_r1_2/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 302 · 2026-05-23T01:04:03.398791+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1431
}
```

</details>

---


### Tool call

_source line 303 · 2026-05-23T01:04:03.399118+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pdf_review_r1_2/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pdf_review_r1_2/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-23T01:04:03.763788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/pdf_review_r1_2/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/pdf_review_r1_2/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-23T01:04:03.815316+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1644
}
```

</details>

---


### Tool result

_source line 306 · 2026-05-23T01:04:03.917629+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 153
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-23T01:04:04.426842+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1483
}
```

</details>

---


### Tool result

_source line 308 · 2026-05-23T01:04:04.680220+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2038
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-23T01:04:04.686061+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1286
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-23T01:04:12.004750+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-23T01:04:12.055455+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{amsthm}
14	\usepackage{booktabs}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	
18	\newtheorem{observation}{Observation}
19	\newtheorem{proposition}{Proposition}
20	\newtheorem{theorem}{Theorem}
21	\newtheorem{corollary}{Corollary}
22	
23	\graphicspath{{../../figures/paper/}}
24	
25	\title{Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model\\for Disentangling Judge Bias and Contamination in LLM Evaluation}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	\input{introduction}
34	\input{background}
35	\input{method}
36	\input{experiments}
37	\input{related_work}
38	\input{conclusion}
39	
40	\section*{Limitations}
41	\input{limitations}
42	
43	\bibliography{references}
44	
45	\appendix
46	\input{appendix}
47	
48	\end{document}
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-23T01:04:15.335075+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/*.tex",
  "description": "List all LaTeX source files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/*.tex",
    "description": "List all LaTeX source files"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-23T01:04:15.594500+00:00_

/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 259
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-23T01:04:18.155772+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-23T01:04:18.508700+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	\label{sec:setup}
6	
7	\paragraph{Data and models.} We evaluate on Arena-Hard \citep{li2024arenahard}, a benchmark of 316 multi-turn conversational items selected for high separability among frontier models. After filtering for full coverage across all judges and target models, the evaluation set contains 176 items in a fully crossed design. Eight target models spanning proprietary and open-source families are evaluated (Table~\ref{tab:main_results}). Ground-truth rankings are derived from Chatbot Arena human preference data \citep{zheng2023mtbench}.
8	
9	\paragraph{Judges.} Six LLM judge families score all model responses in position-swapped pairwise mode: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B, and Llama 4 Maverick. Position swapping controls for position bias and doubles the effective observation count.
10	
11	\paragraph{Exposure estimation.} Per-item exposure $e_i$ is estimated via a two-source pipeline (\S\ref{sec:staged}): reference model anchoring with gpt-4-0314 as anchor (75\% weight) and cross-model agreement (25\% weight). The pipeline is robust to weight configuration (Spearman $\rho \geq 0.998$ across all configurations tested).
12	
13	\paragraph{MCMC.} We use NumPyro NUTS with 4{,}000 warmup and 4{,}000 sampling iterations across 4 chains (target acceptance 0.95). The contamination prior follows the hierarchical HalfNormal specification (Eq.~\ref{eq:contam_prior}). Convergence is assessed via rank-normalized split-$\hat{R}$ and bulk/tail ESS \citep{vehtari2021rhat}.
14	
15	\subsection{Baselines and Main Results}
16	\label{sec:main_results}
17	
18	We compare G-MFRM against seven methods that address judge bias or contamination separately: (1) Raw Average, (2) MFRM-only (Eq.~\ref{eq:mfrm}), (3) Sequential pipeline (MFRM then contamination adjustment), (4) CyclicJudge \citep{cyclicjudge2026}, (5) CyclicJudge+discard (exposed items removed), (6) DC
…[truncated 6949 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-23T01:04:18.509065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-23T01:04:18.961095+00:00_

1	\section{The G-MFRM Framework}
2	\label{sec:method}
3	
4	Section~\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and a hierarchical HalfNormal prior for the contamination term, are motivated by the identifiability analysis in \S\ref{sec:identifiability} and the error propagation bounds in \S\ref{sec:error_prop}.
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{fig1_framework}
9	\caption{Overview of the G-MFRM three-stage calibration procedure. Stage~1 fits a standard MFRM to obtain initial estimates $(\hat{\theta}, \hat{b}, \hat{d})$. Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring and cross-model agreement). Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\tilde{\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}
10	\label{fig:framework}
11	\end{figure}
12	
13	\subsection{Model Specification}
14	\label{sec:model_spec}
15	
16	G-MFRM extends the standard MFRM \citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\ref{eq:mfrm}):
17	%
18	\begin{equation}
19	\label{eq:gmfrm}
20	\log \frac{P(Y_{nij} \geq k)}{P(Y_{nij} < k)} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i,
21	\end{equation}
22	%
23	where all terms carry the definitions from Section~\ref{sec:confounding}. The gating structure $c_n \cdot e_i$ separates the model-specific and item-specific components of contamination: $c_n \geq 0$ captures how much model $n$ benefits from memorized benchmark content, while $e_i \in [0,1]$ quantifies
…[truncated 10478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-23T01:04:18.961510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-23T01:04:19.513750+00:00_

1	\section{Proof of Theorem~\ref{thm:sufficient}}
2	\label{app:proof}
3	
4	We prove that the G-MFRM is locally identifiable under the conditions of Theorem~\ref{thm:sufficient}. Following \citet{rothenberg1971}, a parametric model is locally identifiable at the true parameter vector $\boldsymbol{\psi}_0$ if and only if the Fisher information matrix $\mathbf{F}(\boldsymbol{\psi}_0)$ is non-singular.
5	
6	\paragraph{Setup.} The G-MFRM parameter vector is $\boldsymbol{\psi} = (\boldsymbol{\theta}, \mathbf{c}, \mathbf{b}, \mathbf{d}, \boldsymbol{\tau})$, where $\boldsymbol{\theta} \in \mathbb{R}^{N-1}$ (after the location constraint $\sum_n \theta_n = 0$), $\mathbf{c} \in \mathbb{R}_{\geq 0}^N$, $\mathbf{b} \in \mathbb{R}^I$, $\mathbf{d} \in \mathbb{R}^J$, and $\boldsymbol{\tau} \in \mathbb{R}^{K-1}$. The exposure vector $\mathbf{e} = (e_1, \ldots, e_I)$ is fixed externally and treated as known. The linear predictor is $\eta_{nijk} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i$, with partial derivatives:
7	%
8	\begin{align*}
9	\frac{\partial \eta_{nijk}}{\partial \theta_n} &= 1, \quad
10	\frac{\partial \eta_{nijk}}{\partial c_n} = e_i, \quad
11	\frac{\partial \eta_{nijk}}{\partial b_i} = -1, \\
12	\frac{\partial \eta_{nijk}}{\partial d_j} &= -1, \quad
13	\frac{\partial \eta_{nijk}}{\partial \tau_k} = -1.
14	\end{align*}
15	
16	\paragraph{Fisher information weights.} For each observation cell $(n,i,j)$, the Fisher information weight under the cumulative logit model is
17	%
18	\begin{equation}
19	\label{eq:fisher_weight}
20	w_{nij} = \sum_{k=1}^{K} \frac{\bigl[\sigma'(\eta_{nijk}) - \sigma'(\eta_{nij,k+1})\bigr]^2}{P(Y_{nij} = k)},
21	\end{equation}
22	%
23	where $\sigma(x) = (1 + e^{-x})^{-1}$, $\sigma'(x) = \sigma(x)(1 - \sigma(x))$, and we set $\sigma'(\eta_{nij,0}) = \sigma'(\eta_{nij,K+1}) = 0$ at the boundaries. Since $P(Y_{nij} = k) > 0$ for all categories and $\sigma'(\cdot) > 0$, we have $w_{nij} > 0$ for all $(n,i,j)$.
24	
25	\paragraph{Step 1: The $(\theta_n,
…[truncated 11500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-23T01:04:19.565575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-23T01:04:19.666807+00:00_

1	\section{Confounding in LLM Evaluation}
2	\label{sec:confounding}
3	
4	The Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies
5	%
6	\begin{equation}
7	\label{eq:mfrm}
8	\log \frac{P(Y_{nij} \geq k \mid \theta_n, b_i, d_j, \tau_k)}{P(Y_{nij} < k \mid \theta_n, b_i, d_j, \tau_k)} = \theta_n - b_i - d_j - \tau_k,
9	\end{equation}
10	%
11	where $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\theta_n$ is the ability of model $n$ ($n = 1, \ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \ldots, J$), and $\tau_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for item difficulty and judge severity. \citet{jiao2025mfrm_llm} applied this framework to compare ten LLM raters with human experts, showing that MFRM separates genuine ability from systematic judge effects in multi-judge panels.
12	
13	However, standard MFRM assumes that all systematic sources of score variation are captured by the modeled facets. This assumption breaks down when some models have been exposed to benchmark items during training \citep{dcr2025}. Such contamination inflates scores on exposed items through memorization rather than genuine ability. We represent this effect as an interaction $c_n \cdot e_i$, where $c_n \geq 0$ is the contamination susceptibility of model $n$ and $e_i \in [0, 1]$ is the exposure level of item $i$. The complete data-generating process becomes
14	%
15	\begin{equation}
16	\label{eq:full}
17	\eta_{nijk} = \theta_n - b_i - d_j - \tau_k 
…[truncated 3595 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-23T01:04:24.242206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-23T01:04:24.694130+00:00_

1	\begin{abstract}
2	LLM-as-a-judge evaluation corrects for judge bias and benchmark contamination independently, but sequential correction produces biased model ability estimates. We formalize this failure as an omitted variable bias (OVB) problem: when judge severity and contamination effects are both present, any estimator that models one while omitting the other yields asymptotically biased ability estimates---even when the two facets are uncorrelated. We propose the Gated Many-Facet Rasch Model (G-MFRM), which jointly calibrates model ability, item difficulty, judge severity, and contamination susceptibility through staged estimation with externally anchored per-item exposure indicators. Formal identifiability analysis proves that fixing exposure externally is both necessary and sufficient for parameter separation under standard multi-judge designs. Error propagation analysis establishes a critical noise threshold $\sigma_{\mathrm{crit}} = \sqrt{\mathrm{Var}(e_i)}$ below which ability estimates degrade by less than 6\%. In synthetic experiments ($N = 50$, $I = 100$, $J = 8$), G-MFRM reduces ability RMSE by 43.8\% relative to sequential estimation ($p < 10^{-6}$). On Arena-Hard with 8 target models and 6 judges, G-MFRM identifies statistically significant per-model contamination (top-4 models' 95\% CIs exclude zero) and interpretable judge severity profiles, with nominally higher rank agreement ($\tau = 0.857$ vs.\ $0.786$; bootstrap $\Delta\tau$ CI includes zero at this sample size).
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-23T01:04:24.694605+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-23T01:04:24.695003+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large Language Model (LLM) evaluation increasingly relies on LLM-as-a-judge protocols, where one or more LLM judges score model responses on structured benchmarks \citep{zheng2023mtbench}. Two well-documented sources of distortion affect these evaluations: \emph{judge bias}, where different judges assign systematically different scores to the same response, and \emph{benchmark contamination}, where models achieve inflated scores on items encountered during training. Both problems have received sustained research attention, producing separate toolkits for bias calibration and contamination detection. These toolkits treat the two distortions as independent phenomena, a separation that reflects their origins in different research communities rather than any principled argument for independence. Accurate ability ranking is essential for model selection, safety evaluation, and benchmark design; systematic distortion in estimated abilities undermines all three. Yet a practitioner who needs both corrections must apply them sequentially: first correct one source of distortion, then the other. This sequential approach produces unreliable ability estimates. In synthetic experiments with 50 models, 100 items, and 8 judges, sequential estimation yields ability root mean squared error (RMSE) of $0.221 \pm 0.038$, while joint estimation achieves $0.124 \pm 0.016$, a 43.8\% reduction (Wilcoxon $p < 10^{-6}$). The gap does not arise from estimation noise or algorithmic limitations of individual methods; it reflects structural confounding between judge bias and contamination that no sequential pipeline can resolve.
5	
6	Existing methods address these distortions in isolation. Judge bias corrections---CyclicJudge \citep{cyclicjudge2026}, UDA \citep{uda2026}---remove systematic inter-judge differences without modeling contamination. Contamination detection tools---ConStat \citep{constat2024}, DCR \citep{dcr2025}, LogProber \cite
…[truncated 5044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-23T01:04:25.146897+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-23T01:04:25.649248+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Judge Bias in LLM Evaluation.}
5	LLM-as-a-judge protocols introduce systematic scoring differences across judges, and several recent methods target this bias in isolation. CyclicJudge \citep{cyclicjudge2026} eliminates average bias through round-robin judge assignment that ensures balanced exposure of model pairs to all judges, but treats all residual score variation as genuine ability signal and provides no per-item diagnostics. UDA \citep{uda2026} learns a neural K-factor adjustment that reduces inter-judge standard deviation by 63.4\%, yet the learned correction is a black-box transformation with no interpretable decomposition of the severity parameter and no mechanism for contamination effects. \citet{fiedler2026bias_uncertainty} formalize judge variability through $J/\Delta J$ diagnostics from classical test theory, identifying sign-reversal failure modes when calibration is shared across judges with heterogeneous severity profiles. These methods model only the judge bias facet: contamination-induced score inflation is absorbed into the estimated abilities, producing the directional bias characterized in Section~\ref{sec:confounding}.
6	
7	\paragraph{Contamination Detection and Adjustment.}
8	A parallel line of work quantifies benchmark contamination at the item or model level without accounting for judge effects. ConStat \citep{constat2024} compares target model performance against a reference model to estimate contamination effects ($r^2 = 0.94$ with true contamination in controlled settings), establishing a principled quantification framework that G-MFRM's Stage~2 builds upon for exposure estimation. DCR \citep{dcr2025} adjusts scores on suspected leaked items through fuzzy inference rules, while LogProber \citep{logprober2024} detects memorization signatures from token-level log-probabilities under gray-box access. Perplexity-based methods such as Min-K\% \citep{mink2024} offer a simpler de
…[truncated 2093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-23T01:04:25.649669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-23T01:04:26.151740+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced G-MFRM, which jointly estimates model ability, judge severity, and contamination susceptibility by formalizing their confounding as omitted variable bias. On Arena-Hard, G-MFRM produces the first joint contamination--severity diagnostic, with nominally higher rank agreement ($\tau = 0.857$ vs.\ $0.786$; not significant at $N = 8$).
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-23T01:04:26.202538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-23T01:04:26.253209+00:00_

1	We identify three limitations. First, the fully crossed design requirement (Theorem~\ref{thm:sufficient}, condition~i) demands that every judge scores every model on every item, limiting scalability to settings with many judges or models; extending G-MFRM to incomplete designs via structured missing data models is a direction for future work; relatedly, sparse observations per item in the current design produce elevated item-level mean-square residuals (92/176 items), though model- and judge-level fit remains acceptable. Second, Stage~2 exposure estimation relies on a reference model anchor (gpt-4-0314), and exposure estimate quality depends on the anchor remaining uncontaminated relative to the benchmark; as benchmarks age, anchor validity should be periodically re-assessed. Third, the current evaluation uses a single benchmark (Arena-Hard) with eight target models; generalization to other benchmarks (e.g., MT-Bench, WildBench) and larger model populations remains to be verified. Fourth, empirical CI coverage is 71\% (50 Monte Carlo seeds), below the 95\% nominal level, indicating moderate posterior overconfidence likely due to the HalfNormal prior's boundary constraint and NUTS tree depth saturation. Point estimates and rank orderings ($\tau = 0.857$) are unaffected, but reported CIs should be interpreted as lower bounds on true uncertainty; exploring more flexible priors or post-hoc calibration is a direction for future work.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-23T01:06:08.426635+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-23T01:06:08.480882+00:00_

1	% ============================================================
2	% G-MFRM Paper — references.bib
3	% All entries verified via WebSearch / OpenAlex (2026-05-22)
4	% ============================================================
5	
6	% ------ Bayesian Methodology ------
7	
8	@article{piironen2017horseshoe,
9	  author  = {Piironen, Juho and Vehtari, Aki},
10	  title   = {Sparsity Information and Regularization in the Horseshoe and Other Shrinkage Priors},
11	  journal = {Electronic Journal of Statistics},
12	  volume  = {11},
13	  number  = {2},
14	  pages   = {5018--5051},
15	  year    = {2017},
16	  doi     = {10.1214/17-EJS1337SI},
17	}
18	
19	% ------ Psychometric & IRT Foundations ------
20	
21	@book{linacre1989mfrm,
22	  author    = {Linacre, John Michael},
23	  title     = {Many-Facet {R}asch Measurement},
24	  publisher = {MESA Press},
25	  address   = {Chicago, IL},
26	  year      = {1989},
27	}
28	
29	@book{linacre1994mfrm,
30	  author    = {Linacre, John Michael},
31	  title     = {Many-Facet {R}asch Measurement},
32	  edition   = {2nd},
33	  publisher = {MESA Press},
34	  address   = {Chicago, IL},
35	  year      = {1994},
36	}
37	
38	@article{shu2013dgirt,
39	  author  = {Shu, Zhan and Henson, Robert and Luecht, Richard},
40	  title   = {Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise},
41	  journal = {Psychometrika},
42	  volume  = {78},
43	  number  = {3},
44	  pages   = {481--497},
45	  year    = {2013},
46	  doi     = {10.1007/s11336-012-9311-3},
47	}
48	
49	@article{jiao2025mfrm_llm,
50	  author  = {Jiao, Hong and Song, Dan and Lee, Won-Chan},
51	  title   = {Comparing Human and {AI} Rater Effects Using the Many-Facet {R}asch Model},
52	  journal = {arXiv preprint arXiv:2505.18486},
53	  year    = {2025},
54	}
55	
56	@article{zhou2025psnirt,
57	  author  = {Zhou, Hongli and Huang, Hao and Zhao, Zhuoran and Han, Lei and Wang, Hao and Chen, Kai and Yang, Min and Bao, Weidong and Dong, Jingya and Xu, B
…[truncated 8792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 54
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-23T01:08:43.930970+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验有效性\n\n**论文标题**: Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 2.5 / 5 (Borderline Findings)\n\n**一句话总结**: 理论框架（OVB形式化 + identifiability证明）有genuine novelty，但实验执行存在多个严重问题——judge名称不一致、数值前后矛盾、MCMC未达自设标准、主结果统计不显著、附录有figure placeholder——这些问题叠加后严重削弱论文可信度，需要major revision。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 理论部分sound（OVB、Theorem 1、error propagation），但实验数据存在judge名称不匹配的致命一致性问题，MCMC收敛未达自设标准，主结果统计不显著且posterior median等于baseline |\n| Excitement | 3.0/5 | 联合建模judge bias和contamination是genuinely novel的问题formulation，OVB视角和gating mechanism有创意，但real-data结果太弱（τ improvement不显著）削弱了excitement |\n| Reproducibility | 2.5/5 | Stage 2 exposure estimation的75/25权重缺乏justification，reference anchor选择未做sensitivity analysis，附录figure placeholder表明实验流程未完成 |\n| Confidence | 4/5 | 仔细阅读了全文、附录、LaTeX源码，对IRT/MFRM和Bayesian inference有sufficient expertise |\n\n---\n\n## Summary\n\n本文将LLM-as-a-judge评估中的judge bias和benchmark contamination的联合校正问题形式化为omitted variable bias (OVB)问题，提出G-MFRM模型通过multiplicative gating term $c_n \\cdot e_i$ 在单一测量框架内联合估计model ability、judge severity和contamination susceptibility。论文提供了formal identifiability分析（Theorem 1）和error propagation bounds。在合成数据上G-MFRM将ability RMSE降低43.8%；在Arena-Hard真实数据上获得nominally higher rank agreement（τ = 0.857 vs 0.786），但统计不显著。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] §4.1 和 §4.2 之间 judge 名称严重不一致\n\n- 具体位置：§4.1（experiments.tex L9）vs §4.2（experiments.tex L44）\n- 问题：§4.1 列出的6个judge为 GPT-5.5、Claude Opus 4.7、**Claude Sonnet 4.6**、DeepSeek-V4-Pro、**Qwen3-235B**、**Llama 4 Maverick**。但§4.2报告的judge severity结果为：Claude Opus +0.60、GPT-5.5 +0.53、DeepSeek +0.31、**Mistral -0.74**、**LLaMA -0.42**、**Qwen2.5-72B -0.35**。\n  - Claude Sonnet 4.6 在结果中消失\n  - Mistral 从未在setup中提及却出现在结果中\n  - Qwen3-235B（setup）变成了 Qwen2.5-72B（results），但 Qwen2.5-72B 同时出现在target model的contamination结果中（$c_n = 3.00$）——它到底是judge还是target model？\n  - Llama 4 Maverick 变成了 \"LLaMA\"\n- 为什么影响接收：这不是简单的命名不一致。如果同一模型（如Qwen2.5-72B）既是judge又是target model，会产生self-evaluation循环。如果实验实际用的judge和论文描述的不同，所有结果的可信度都存疑。Appendix ablation节（L137）也引用 \"Mistral −0.74\"，说明这不是个别typo而是系统性问题。\n- 建议修改方向：明确列出实际使用的judge列表（附版本号），确保§4.1、§4.2、Appendix三处完全一致；如果Qwen2.5-72B同时是judge和target，必须讨论self-evaluation bias。\n\n**N2** [critical] Introduction 与 Experiments 之间的数值不一致\n\n- 具体位置：Introduction（introduction.tex L16）vs §4.2（experiments.tex L42）vs Appendix C ablation（appendix.tex L123-131）\n- 问题：\n  - Introduction 称 sequential baseline τ = **0.859**，但 §4.2 和 ablation table 均报告 staged estimation τ = **0.826**。同一实验设置（N=50, I=100, J=8），差异0.033无法用随机波动解释。\n  - Introduction 称 sequential RMSE = **0.221 ± 0.038**，但 ablation table 报告 staged estimation θ-RMSE = **0.273**。差异 23%。\n- 为什么影响接收：核心contribution的数字前后矛盾，使读者无法判断哪个是正确的。如果是不同实验配置，论文没有说明区别。\n- 建议修改方向：统一所有引用的合成实验数值，确保Introduction、§4.2、Appendix引用同一组实验结果。\n\n**N3** [critical] 主结果统计不显著且posterior median等于baseline\n\n- 具体位置：§4.2（experiments.tex L42）\n- 问题：\n  - Bootstrap Δτ 95% CI = [−0.071, 0.071]，包含零——τ improvement统计不显著。\n  - Posterior median τ = 0.786，与全部7个baseline **完全相同**。τ = 0.857的point estimate位于posterior distribution的upper tail。\n  - 这意味着在posterior uncertainty下，G-MFRM的typical ranking与baseline无异。0.857只是一个lucky draw而非robust improvement。\n- 为什么影响接收：论文的core empirical claim是G-MFRM improves rank agreement。当posterior median等于baseline且CI包含零时，这个claim缺乏统计支撑。虽然P(Δτ ≥ 0) = 0.927表明方向一致，但这不足以支撑一个strong claim。\n- 建议修改方向：(1) 明确将主结果定位为 \"suggestive evidence\" 而非 \"improvement\"；(2) 增加更多target models以增大statistical power；(3) 或者将主要贡献重新定位为诊断工具（contamination severity profiles）而非ranking improvement。\n\n**N4** [critical] MCMC收敛未达论文自设标准\n\n- 具体位置：§3.2（method.tex L48）vs §4.2（experiments.tex L44 footnote）\n- 问题：\n  - §3.2 method section 明确设定收敛阈值为 R̂ < 1.01 和 ESS_bulk, ESS_tail > 400\n  - §4.2 实际报告 R̂ ≤ **1.03** 和 minimum bulk ESS = **217**\n  - R̂ = 1.03 超过自设的1.01阈值（虽然满足传统1.05）\n  - ESS = 217 仅为自设400阈值的**54%**\n- 为什么影响接收：方法论自设了收敛标准却在实验中未达标，这是一个internal inconsistency。论文用脚注试图淡化（\"satisfies the traditional 1.05 threshold\"），但这恰恰说明收敛不够好。结合71% CI coverage（远低于95% nominal），posterior inference的可靠性令人担忧。\n- 建议修改方向：(1) 增加sampling iterations或chains直到满足自设标准；(2) 或者诚实降低§3.2的声称阈值并充分讨论implications；(3) 调查是哪些参数导致high R̂和low ESS（是否是$c_n$？如果是，这与71% CI coverage问题可能有共同根因）。\n\n**N5** [critical] 附录Figure 3是placeholder，非完整提交\n\n- 具体位置：Appendix D（appendix.tex L145-150），PDF第12页\n- 问题：Figure 3（Posterior Predictive Check）显示为 **\"[FIGURE PLACEHOLDER — fig_ppc.pdf PENDING SYNC FROM REMOTE SERVER]\"**，是一个空框。\n- 为什么影响接收：投稿PDF中包含未完成的placeholder figure，表明论文在提交时实验流程尚未完结。Posterior predictive check是验证模型拟合的关键诊断，缺失此图使reviewer无法独立验证§4.2声称的 \"predicted mean 0.593 vs observed 0.599\" fit quality。\n- 建议修改方向：生成并包含该图；如果无法生成，删除该appendix section而非留placeholder。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 七个baseline产生完全相同的ranking（τ=0.786, ρ=0.905）需更深入解释\n\n- 具体位置：Table 1（experiments.tex L27-33）\n- 问题：七种不同的方法（Raw Average、MFRM-only、Sequential pipeline、CyclicJudge、CyclicJudge+discard、DCR Factor、Pref. Leakage）产生**完全相同**的τ和ρ。论文解释为\"structural confounding leaves invariant rank orderings\"，但这在直觉上仍然surprising——特别是CyclicJudge+discard（移除exposed items后）仍产生相同ranking。\n- 为什么令人怀疑：如果discard exposed items真的不改变ranking，说明exposure estimation或discard策略可能有问题。也可能是N=8太小导致discrete τ值碰巧相同，但论文未讨论这一点。\n- 建议：(1) 报告各方法产生的raw scores/rankings而不仅是τ/ρ，让读者判断是否真的identical；(2) 讨论N=8下τ的discrete nature（只有有限种可能的τ值）。\n\n**W2** [warning] Stage 2 exposure estimation的75/25权重缺乏sensitivity analysis\n\n- 具体位置：§4.1（experiments.tex L11）\n- 问题：75% reference model anchoring + 25% cross-model agreement的权重组合仅以Spearman ρ ≥ 0.998验证。但如Director指出，ρ ≥ 0.998只说明不同权重下exposure **ranking**稳定，不代表downstream τ也稳定。论文未报告不同权重配置下的τ变化。\n- 建议：添加一个sensitivity table/figure，展示权重从100/0到0/100变化时τ的变化。\n\n**W3** [warning] Reference model anchor (gpt-4-0314) 自身可能被contaminate\n\n- 具体位置：§4.1（experiments.tex L11）、Limitations\n- 问题：gpt-4-0314作为exposure estimation的anchor，其前提是它本身相对于Arena-Hard未被contaminate。虽然时间线上gpt-4-0314（2023年3月）早于Arena-Hard（2024年），但Arena-Hard的items可能源自更早的数据。Limitations节承认了这一风险但未做任何robustness check。\n- 建议：使用至少一个替代anchor重复exposure estimation，报告anchor sensitivity。\n\n**W4** [warning] OVB近似的γ_n形式未给出\n\n- 具体位置：§2 Observation 1（background.tex L24-31）\n- 问题：OVB公式 plim(θ̃_n − θ_n) = γ_n · c_n 中，γ_n被定义为\"depends on the projection of the exposure vector (e_i) onto the design matrix of the short model\"，但具体表达式未给出。对于一个声称formal contribution的论文，这种关键中间量的省略削弱了理论完整性。\n- 为什么重要：不同的γ_n形式对bias magnitude有不同的implications。读者需要这个表达式来判断在什么条件下bias特别大或特别小。\n- 建议：在正文或Appendix中给出γ_n的explicit form。\n\n**W5** [warning] CI coverage 71%是严重的posterior calibration问题\n\n- 具体位置：Appendix E（appendix.tex L170-171）、Limitations\n- 问题：$c_n$的empirical CI coverage仅71%（50 Monte Carlo seeds），远低于95% nominal。论文将此归因于HalfNormal prior boundary constraint和NUTS tree depth saturation，但未提供诊断证据。71% coverage意味着大约24%的真值落在reported CI之外——这不是\"moderate overconfidence\"而是substantial miscalibration。\n- 为什么重要：如果CI不可靠，§4.2中报告的contamination susceptibility CIs（如GPT-3.5-Turbo [4.40, 6.80]）的interpretability就打了折扣。\n- 建议：(1) 诊断哪些$c_n$值的coverage最差（是否boundary附近？）；(2) 考虑posterior recalibration（如SBC）；(3) 增加sampling budget看coverage是否改善。\n\n**W6** [warning] 合成实验N=50显著但真实数据N=8不显著的gap讨论不充分\n\n- 具体位置：§4.2（experiments.tex L42）\n- 问题：论文承认N=8下不显著，但缺少formal power analysis。读者无法判断：需要多少target models才能在合理effect size下达到显著性？如果答案是N>50，这对论文的practical utility有重要implications。\n- 建议：添加power analysis或至少讨论effect size（Cohen's d或equivalent）和所需样本量。\n\n**W7** [warning] Ablation标注\"preliminary\"（10 seeds）\n\n- 具体位置：Appendix C Table 3 caption（appendix.tex L129）\n- 问题：Ablation study使用10 seeds并标注\"preliminary\"。投稿论文中的实验不应标注为preliminary。且10 seeds的variance估计不稳定。\n- 建议：增加至与主实验一致的20 seeds并移除\"preliminary\"标注。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.2 footnote 4声称\"Synthetic validation with N=50, I=100, J=8 yields satisfactory convergence across all parameters\"，但这与实验节的convergence问题矛盾——合成数据上convergence好但真实数据上差，暗示真实数据的model specification可能有问题。\n- Proposition 1 proof中\"e_i ≠ 0 for at least one item by assumption\"这个assumption未在Proposition statement中显式声明，应作为条件列出。\n- 论文提到Murphy-Topel variance correction（Appendix B），但未报告correction前后CI width的变化，使读者无法评估correction magnitude。\n- Abstract声称\"G-MFRM identifies statistically significant per-model contamination (top-4 models' 95% CIs exclude zero)\"——但结合71% CI coverage，这些CIs本身不可靠，因此\"statistically significant\"的claim需要qualifier。\n\n---\n\n## 主要优势\n\n1. **问题形式化有genuine novelty**：将judge bias和contamination的交互作用形式化为OVB问题是一个有价值的理论贡献，这个insight对LLM evaluation社区有启发意义（§2）。\n2. **Identifiability分析严格**：Theorem 1的Schur complement proof（Appendix A）是sound的，四个条件的推导逻辑清晰。Proposition 2（exposure variation necessary）是一个有用的negative result。\n3. **Error propagation bounds有practical value**：σ_crit = √Var(e_i)的threshold和Table 2的empirical validation提供了Stage 2 exposure estimation所需精度的quantitative guidance（§3.4）。\n4. **模型设计优雅**：multiplicative gating c_n · e_i的graceful degradation property（c_n=0或e_i=0时退化为标准MFRM）是一个clean design choice。\n5. **诚实报告负面结果**：论文如实报告了主结果不显著、CI coverage不足等问题（§4.2、Limitations），这比over-claiming更好。\n\n---\n\n## Questions for Authors\n\nQ1. §4.2中judge severity结果列出的judge names与§4.1 setup不匹配。请澄清实际使用的judges。\n\nQ2. Introduction中τ=0.859和RMSE=0.221与§4.2/Appendix中τ=0.826和θ-RMSE=0.273的差异来自何处？是不同的实验配置还是编辑错误？\n\nQ3. Posterior median τ = 0.786（等于baseline）而point estimate τ = 0.857——能否clarify \"point estimate\"具体指什么（posterior mean? MAP? 某个specific posterior draw?）？\n\nQ4. 七个baseline的τ和ρ完全相同——是否检查了各方法的raw model scores或rankings也完全相同，还是仅τ/ρ碰巧因N=8的离散性而相同？\n\nQ5. Figure 3 (PPC) 为placeholder。能否在rebuttal中补充该图？\n\n---\n\n## Missing References\n\n- **Uto & Ueno (2020)** 在references.bib中有但正文未引用——考虑是否应讨论其Bayesian MFRM estimation与本文的关系。\n- 缺少对 **SBC (Simulation-Based Calibration, Talts et al., 2018)** 的引用——鉴于71% CI coverage问题，SBC是standard diagnostic。\n- 未讨论 **Chatbot Arena's own decontamination efforts**——Arena-Hard本身是否已经做了contamination filtering？如果是，G-MFRM在已过滤数据上的incremental value需要讨论。",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验有效性\n\n**论文标题**: Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 2.5 / 5 (Borderline Findings)\n\n**一句话总结**: 理论框架（OVB形式化 + identifiability证明）有genuine novelty，但实验执行存在多个严重问题——judge名称不一致、数值前后矛盾、MCMC未达自设标准、主结果统计不显著、附录有figure placeholder——这些问题叠加后严重削弱论文可信度，需要major revision。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 理论部分sound（OVB、Theorem 1、error propagation），但实验数据存在judge名称不匹配的致命一致性问题，MCMC收敛未达自设标准，主结果统计不显著且posterior median等于baseline |\n| Excitement | 3.0/5 | 联合建模judge bias和contamination是genuinely novel的问题formulation，OVB视角和gating mechanism有创意，但real-data结果太弱（τ improvement不显著）削弱了excitement |\n| Reproducibility | 2.5/5 | Stage 2 exposure estimation的75/25权重缺乏justification，reference anchor选择未做sensitivity analysis，附录figure placeholder表明实验流程未完成 |\n| Confidence | 4/5 | 仔细阅读了全文、附录、LaTeX源码，对IRT/MFRM和Bayesian inference有sufficient expertise |\n\n---\n\n## Summary\n\n本文将LLM-as-a-judge评估中的judge bias和benchmark contamination的联合校正问题形式化为omitted variable bias (OVB)问题，提出G-MFRM模型通过multiplicative gating term $c_n \\cdot e_i$ 在单一测量框架内联合估计model ability、judge severity和contamination susceptibility。论文提供了formal identifiability分析（Theorem 1）和error propagation bounds。在合成数据上G-MFRM将ability RMSE降低43.8%；在Arena-Hard真实数据上获得nominally higher rank agreement（τ = 0.857 vs 0.786），但统计不显著。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] §4.1 和 §4.2 之间 judge 名称严重不一致\n\n- 具体位置：§4.1（experiments.tex L9）vs §4.2（experiments.tex L44）\n- 问题：§4.1 列出的6个judge为 GPT-5.5、Claude Opus 4.7、**Claude Sonnet 4.6**、DeepSeek-V4-Pro、**Qwen3-235B**、**Llama 4 Maverick**。但§4.2报告的judge severity结果为：Claude Opus +0.60、GPT-5.5 +0.53、DeepSeek +0.31、**Mistral -0.74**、**LLaMA -0.42**、**Qwen2.5-72B -0.35**。\n  - Claude Sonnet 4.6 在结果中消失\n  - Mistral 从未在setup中提及却出现在结果中\n  - Qwen3-235B（setup）变成了 Qwen2.5-72B（results），但 Qwen2.5-72B 同时出现在target model的contamination结果中（$c_n = 3.00$）——它到底是judge还是target model？\n  - Llama 4 Maverick 变成了 \"LLaMA\"\n- 为什么影响接收：这不是简单的命名不一致。如果同一模型（如Qwen2.5-72B）既是judge又是target model，会产生self-evaluation循环。如果实验实际用的judge和论文描述的不同，所有结果的可信度都存疑。Appendix ablation节（L137）也引用 \"Mistral −0.74\"，说明这不是个别typo而是系统性问题。\n- 建议修改方向：明确列出实际使用的judge列表（附版本号），确保§4.1、§4.2、Appendix三处完全一致；如果Qwen2.5-72B同时是judge和target，必须讨论self-evaluation bias。\n\n**N2** [critical] Introduction 与 Experiments 之间的数值不一致\n\n- 具体位置：Introduction（introduction.tex L16）vs §4.2（experiments.tex L42）vs Appendix C ablation（appendix.tex L123-131）\n- 问题：\n  - Introduction 称 sequential baseline τ = **0.859**，但 §4.2 和 ablation table 均报告 staged estimation τ = **0.826**。同一实验设置（N=50, I=100, J=8），差异0.033无法用随机波动解释。\n  - Introduction 称 sequential RMSE = **0.221 ± 0.038**，但 ablation table 报告 staged estimation θ-RMSE = **0.273**。差异 23%。\n- 为什么影响接收：核心contribution的数字前后矛盾，使读者无法判断哪个是正确的。如果是不同实验配置，论文没有说明区别。\n- 建议修改方向：统一所有引用的合成实验数值，确保Introduction、§4.2、Appendix引用同一组实验结果。\n\n**N3** [critical] 主结果统计不显著且posterior median等于baseline\n\n- 具体位置：§4.2（experiments.tex L42）\n- 问题：\n  - Bootstrap Δτ 95% CI = [−0.071, 0.071]，包含零——τ improvement统计不显著。\n  - Posterior median τ = 0.786，与全部7个baseline **完全相同**。τ = 0.857的point estimate位于posterior distribution的upper tail。\n  - 这意味着在posterior uncertainty下，G-MFRM的typical ranking与baseline无异。0.857只是一个lucky draw而非robust improvement。\n- 为什么影响接收：论文的core empirical claim是G-MFRM improves rank agreement。当posterior median等于baseline且CI包含零时，这个claim缺乏统计支撑。虽然P(Δτ ≥ 0) = 0.927表明方向一致，但这不足以支撑一个strong claim。\n- 建议修改方向：(1) 明确将主结果定位为 \"suggestive evidence\" 而非 \"improvement\"；(2) 增加更多target models以增大statistical power；(3) 或者将主要贡献重新定位为诊断工具（contamination severity profiles）而非ranking improvement。\n\n**N4** [critical] MCMC收敛未达论文自设标准\n\n- 具体位置：§3.2（method.tex L48）vs §4.2（experiments.tex L44 footnote）\n- 问题：\n  - §3.2 method section 明确设定收敛阈值为 R̂ < 1.01 和 ESS_bulk, ESS_tail > 400\n  - §4.2 实际报告 R̂ ≤ **1.03** 和 minimum bulk ESS = **217**\n  - R̂ = 1.03 超过自设的1.01阈值（虽然满足传统1.05）\n  - ESS = 217 仅为自设400阈值的**54%**\n- 为什么影响接收：方法论自设了收敛标准却在实验中未达标，这是一个internal inconsistency。论文用脚注试图淡化（\"satisfies the traditional 1.05 threshold\"），但这恰恰说明收敛不够好。结合71% CI coverage（远低于95% nominal），posterior inference的可靠性令人担忧。\n- 建议修改方向：(1) 增加sampling iterations或chains直到满足自设标准；(2) 或者诚实降低§3.2的声称阈值并充分讨论implications；(3) 调查是哪些参数导致high R̂和low ESS（是否是$c_n$？如果是，这与71% CI coverage问题可能有共同根因）。\n\n**N5** [critical] 附录Figure 3是placeholder，非完整提交\n\n- 具体位置：Appendix D（appendix.tex L145-150），PDF第12页\n- 问题：Figure 3（Posterior Predictive Check）显示为 **\"[FIGURE PLACEHOLDER — fig_ppc.pdf PENDING SYNC FROM REMOTE SERVER]\"**，是一个空框。\n- 为什么影响接收：投稿PDF中包含未完成的placeholder figure，表明论文在提交时实验流程尚未完结。Posterior predictive check是验证模型拟合的关键诊断，缺失此图使reviewer无法独立验证§4.2声称的 \"predicted mean 0.593 vs observed 0.599\" fit quality。\n- 建议修改方向：生成并包含该图；如果无法生成，删除该appendix section而非留placeholder。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 七个baseline产生完全相同的ranking（τ=0.786, ρ=0.905）需更深入解释\n\n- 具体位置：Table 1（experiments.tex L27-33）\n- 问题：七种不同的方法（Raw Average、MFRM-only、Sequential pipeline、CyclicJudge、CyclicJudge+discard、DCR Factor、Pref. Leakage）产生**完全相同**的τ和ρ。论文解释为\"structural confounding leaves invariant rank orderings\"，但这在直觉上仍然surprising——特别是CyclicJudge+discard（移除exposed items后）仍产生相同ranking。\n- 为什么令人怀疑：如果discard exposed items真的不改变ranking，说明exposure estimation或discard策略可能有问题。也可能是N=8太小导致discrete τ值碰巧相同，但论文未讨论这一点。\n- 建议：(1) 报告各方法产生的raw scores/rankings而不仅是τ/ρ，让读者判断是否真的identical；(2) 讨论N=8下τ的discrete nature（只有有限种可能的τ值）。\n\n**W2** [warning] Stage 2 exposure estimation的75/25权重缺乏sensitivity analysis\n\n- 具体位置：§4.1（experiments.tex L11）\n- 问题：75% reference model anchoring + 25% cross-model agreement的权重组合仅以Spearman ρ ≥ 0.998验证。但如Director指出，ρ ≥ 0.998只说明不同权重下exposure **ranking**稳定，不代表downstream τ也稳定。论文未报告不同权重配置下的τ变化。\n- 建议：添加一个sensitivity table/figure，展示权重从100/0到0/100变化时τ的变化。\n\n**W3** [warning] Reference model anchor (gpt-4-0314) 自身可能被contaminate\n\n- 具体位置：§4.1（experiments.tex L11）、Limitations\n- 问题：gpt-4-0314作为exposure estimation的anchor，其前提是它本身相对于Arena-Hard未被contaminate。虽然时间线上gpt-4-0314（2023年3月）早于Arena-Hard（2024年），但Arena-Hard的items可能源自更早的数据。Limitations节承认了这一风险但未做任何robustness check。\n- 建议：使用至少一个替代anchor重复exposure estimation，报告anchor sensitivity。\n\n**W4** [warning] OVB近似的γ_n形式未给出\n\n- 具体位置：§2 Observation 1（background.tex L24-31）\n- 问题：OVB公式 plim(θ̃_n − θ_n) = γ_n · c_n 中，γ_n被定义为\"depends on the projection of the exposure vector (e_i) onto the design matrix of the short model\"，但具体表达式未给出。对于一个声称formal contribution的论文，这种关键中间量的省略削弱了理论完整性。\n- 为什么重要：不同的γ_n形式对bias magnitude有不同的implications。读者需要这个表达式来判断在什么条件下bias特别大或特别小。\n- 建议：在正文或Appendix中给出γ_n的explicit form。\n\n**W5** [warning] CI coverage 71%是严重的posterior calibration问题\n\n- 具体位置：Appendix E（appendix.tex L170-171）、Limitations\n- 问题：$c_n$的empirical CI coverage仅71%（50 Monte Carlo seeds），远低于95% nominal。论文将此归因于HalfNormal prior boundary constraint和NUTS tree depth saturation，但未提供诊断证据。71% coverage意味着大约24%的真值落在reported CI之外——这不是\"moderate overconfidence\"而是substantial miscalibration。\n- 为什么重要：如果CI不可靠，§4.2中报告的contamination susceptibility CIs（如GPT-3.5-Turbo [4.40, 6.80]）的interpretability就打了折扣。\n- 建议：(1) 诊断哪些$c_n$值的coverage最差（是否boundary附近？）；(2) 考虑posterior recalibration（如SBC）；(3) 增加sampling budget看coverage是否改善。\n\n**W6** [warning] 合成实验N=50显著但真实数据N=8不显著的gap讨论不充分\n\n- 具体位置：§4.2（experiments.tex L42）\n- 问题：论文承认N=8下不显著，但缺少formal power analysis。读者无法判断：需要多少target models才能在合理effect size下达到显著性？如果答案是N>50，这对论文的practical utility有重要implications。\n- 建议：添加power analysis或至少讨论effect size（Cohen's d或equivalent）和所需样本量。\n\n**W7** [warning] Ablation标注\"preliminary\"（10 seeds）\n\n- 具体位置：Appendix C Table 3 caption（appendix.tex L129）\n- 问题：Ablation study使用10 seeds并标注\"preliminary\"。投稿论文中的实验不应标注为preliminary。且10 seeds的variance估计不稳定。\n- 建议：增加至与主实验一致的20 seeds并移除\"preliminary\"标注。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.2 footnote 4声称\"Synthetic validation with N=50, I=100, J=8 yields satisfactory convergence across all parameters\"，但这与实验节的convergence问题矛盾——合成数据上convergence好但真实数据上差，暗示真实数据的model specification可能有问题。\n- Proposition 1 proof中\"e_i ≠ 0 for at least one item by assumption\"这个assumption未在Proposition statement中显式声明，应作为条件列出。\n- 论文提到Murphy-Topel variance correction（Appendix B），但未报告correction前后CI width的变化，使读者无法评估correction magnitude。\n- Abstract声称\"G-MFRM identifies statistically significant per-model contamination (top-4 models' 95% CIs exclude zero)\"——但结合71% CI coverage，这些CIs本身不可靠，因此\"statistically significant\"的claim需要qualifier。\n\n---\n\n## 主要优势\n\n1. **问题形式化有genuine novelty**：将judge bias和contamination的交互作用形式化为OVB问题是一个有价值的理论贡献，这个insight对LLM evaluation社区有启发意义（§2）。\n2. **Identifiability分析严格**：Theorem 1的Schur complement proof（Appendix A）是sound的，四个条件的推导逻辑清晰。Proposition 2（exposure variation necessary）是一个有用的negative result。\n3. **Error propagation bounds有practical value**：σ_crit = √Var(e_i)的threshold和Table 2的empirical validation提供了Stage 2 exposure estimation所需精度的quantitative guidance（§3.4）。\n4. **模型设计优雅**：multiplicative gating c_n · e_i的graceful degradation property（c_n=0或e_i=0时退化为标准MFRM）是一个clean design choice。\n5. **诚实报告负面结果**：论文如实报告了主结果不显著、CI coverage不足等问题（§4.2、Limitations），这比over-claiming更好。\n\n---\n\n## Questions for Authors\n\nQ1. §4.2中judge severity结果列出的judge names与§4.1 setup不匹配。请澄清实际使用的judges。\n\nQ2. Introduction中τ=0.859和RMSE=0.221与§4.2/Appendix中τ=0.826和θ-RMSE=0.273的差异来自何处？是不同的实验配置还是编辑错误？\n\nQ3. Posterior median τ = 0.786（等于baseline）而point estimate τ = 0.857——能否clarify \"point estimate\"具体指什么（posterior mean? MAP? 某个specific posterior draw?）？\n\nQ4. 七个baseline的τ和ρ完全相同——是否检查了各方法的raw model scores或rankings也完全相同，还是仅τ/ρ碰巧因N=8的离散性而相同？\n\nQ5. Figure 3 (PPC) 为placeholder。能否在rebuttal中补充该图？\n\n---\n\n## Missing References\n\n- **Uto & Ueno (2020)** 在references.bib中有但正文未引用——考虑是否应讨论其Bayesian MFRM estimation与本文的关系。\n- 缺少对 **SBC (Simulation-Based Calibration, Talts et al., 2018)** 的引用——鉴于71% CI coverage问题，SBC是standard diagnostic。\n- 未讨论 **Chatbot Arena's own decontamination efforts**——Arena-Hard本身是否已经做了contamination filtering？如果是，G-MFRM在已过滤数据上的incremental value需要讨论。",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-23T01:08:48.104513+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4173
}
```

</details>

---


### Assistant

_source line 336 · 2026-05-23T01:09:00.897680+00:00_

审稿意见已提交给 Review Director。

**审稿结果摘要**：

- **Overall: 2.5/5 (Borderline Findings)**
- 5 个 Must-Fix 问题：
  1. §4.1 与 §4.2 judge 名称严重不匹配（Claude Sonnet 消失、Mistral 凭空出现、Qwen 版本混乱）
  2. Introduction 与 Experiments/Ablation 数值矛盾（τ: 0.859 vs 0.826, RMSE: 0.221 vs 0.273）
  3. 主结果统计不显著，posterior median τ = baseline (0.786)
  4. MCMC 收敛未达自设标准（R̂ 1.03 vs 目标 1.01，ESS 217 vs 目标 400）
  5. 附录 Figure 3 是 placeholder（"pending sync from remote server"）
- 7 个 Should-Fix 问题涵盖 baseline 同质性、exposure 权重 sensitivity、anchor contamination 风险、γ_n 形式缺失、CI coverage 71%、power analysis 缺失、ablation 标注 "preliminary"
- 主要优势：OVB 形式化有 genuine novelty，identifiability 证明 sound，error propagation bounds 有 practical value

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 12

## Round 12

2 recorded events


### User

_source line 337 · 2026-05-23T01:10:10.231615+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）

**Overall**: 3.0 / 5 — Findings

### Must-Fix 问题

**N1** [critical] §4.1 与 §4.2 Judge 名称严重不一致——数据完整性存疑
- §4.1 列出 6 judges：GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B, Llama 4 Maverick
- §4.2 severity 结果：Claude Opus (+0.60), GPT-5.5 (+0.53), DeepSeek (+0.31), Mistral (−0.74), LLaMA (−0.42), Qwen2.5-72B (−0.35)
- Claude Sonnet 消失、Mistral 凭空出现、Qwen3-235B 变成 Qwen2.5-72B
- Qwen2.5-72B 同时出现在 target models contamination 结果中（c_n=3.00）

**N2** [critical] Appendix D (PPC) 包含 Figure Placeholder
- "[FIGURE PLACEHOLDER — FIG_PPC.PDF PENDING SYNC FROM REMOTE SERVER]"

**N3** [critical] Real-data 主结果不显著，但 Abstract/Introduction 呈现方式有误导性
- Bootstrap Δτ CI包含零，posterior median τ = baseline (0.786)
- Abstract/Intro 将不显著的限定埋在细节中

**N4** [critical] 所有 7 个 baselines 产生完全相同的 ranking——可信度存疑
- CyclicJudge+discard 移除 exposed items 后仍与 Raw Average ranking 完全相同——与论文 motivation 矛盾
- DCR Factor 和 Pref. Leakage 的校正量恰好不改变任何 pairwise ordering，概率极低

### Should-Fix 问题

**W1** Limitations 计数错误（写"three"实际四个）
**W2** Table 3 caption 标注 "preliminary"
**W3** 贡献新颖性为增量组合（MFRM + DG-IRT gating 直接组合，identifiability 证明用标准技术）
**W4** Conclusion 极其简短（仅2句）
**W5** 遗漏重要相关工作（Polo et al. 2024 tinyBenchmarks, Kipnis et al. 2025 MetaBench, Chernozhukov et al. 2022 OVB in causal ML）
**W6** CI Coverage 仅 71%
**W7** 无代码/数据可用性声明

### Questions
Q1. Judge 名称不一致——哪个是正确配置？
Q2. 7 baselines 完全相同 τ/ρ——能否提供 raw scores？
Q3. CyclicJudge+discard 移除 exposed items 仍同 ranking——contamination correction 实际价值？
Q4. Horseshoe prior 的 CI coverage？NUTS tree depth saturation 影响？
Q5. 是否计划开源？

---

请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 338 · 2026-05-23T01:12:00.416384+00:00_

以下是我（Reviewer 1）对 Reviewer 2 各条意见的逐条回应。

---

## Must-Fix 问题回应

**[AGREE] R2-N1: Judge 名称不一致**

完全同意。这与我的 N1 发现一致。我在 LaTeX 源码中确认了三处不匹配：

1. experiments.tex L9（§4.1 setup）列出 Claude Sonnet 4.6、Qwen3-235B、Llama 4 Maverick
2. experiments.tex L44（§4.2 results）列出 Mistral、Qwen2.5-72B、LLaMA
3. appendix.tex L137（Appendix C ablation）也引用 "Mistral −0.74"

补充 R2 未提到的一点：Qwen2.5-72B **同时**出现在 target model contamination 结果中（$c_n = 3.00$, experiments.tex L44）和 judge severity 结果中（$d_j = -0.35$）。如果同一模型既做 judge 又做 target，存在 self-evaluation 循环问题，这不仅是命名错误，可能涉及实验设计缺陷。这是本文最严重的问题之一。

---

**[AGREE] R2-N2: Figure Placeholder**

完全同意。我的 N5 同样标记了此问题。appendix.tex L147 的 `\fbox{\parbox{...}}` 是一个显式的占位符，PDF 第 12 页可直接看到 "[FIGURE PLACEHOLDER — fig\_ppc.pdf PENDING SYNC FROM REMOTE SERVER]"。投稿 PDF 中出现未完成的 placeholder 是一个 submission-readiness 问题。

---

**[REBUT] R2-N3: Abstract/Introduction 呈现方式有误导性**

部分不同意 R2 的"误导性"定性。核查原文后：

- **Abstract**（abstract.tex L2）明确写道："with nominally higher rank agreement ($\tau = 0.857$ vs.\ $0.786$; bootstrap $\Delta\tau$ CI includes zero **at this sample size**)"——不显著的限定**直接出现在 abstract 中**，并非埋在细节里。
- **Introduction 贡献列表**（introduction.tex L17）使用了 "nominally improved"，虽然未再次显式提及 CI 包含零，但 "nominally" 在统计语境中就意味着 "not statistically significant"。
- **§4.2** 第一段（experiments.tex L42）详细报告了 CI = [−0.071, 0.071]、P(Δτ ≥ 0) = 0.927、posterior median = 0.786。

因此论文的表述是 honest 的，没有故意隐藏不显著性。但我**同意** R2 的底层关切（即主结果不显著这一事实本身是个问题），这也是我自己 N3 的核心观点。问题不在呈现方式，而在于 posterior median τ 等于 baseline——这意味着 G-MFRM 在 posterior uncertainty 下的 typical ranking 与 baseline 无异。

---

**[AGREE] R2-N4: 七个 baselines 完全相同 ranking 的可信度**

同意这是一个需要更深入解释的问题（我列为 W1 Should-Fix），但我认为 R2 将其标记为 critical 值得商榷。

**同意的部分**：CyclicJudge+discard 移除了 exposed items 后仍产生完全相同的 ranking，这与论文声称 contamination 有实质影响的 motivation 存在张力。如果 contamination correction（即移除 exposed items）不改变任何 model 的 pairwise ordering，读者有理由质疑 contamination 的实际影响规模。

**但有一个合理解释论文未充分展开**：N=8 时 Kendall τ 只有有限个离散值（对 8 个模型的排列，τ 的可能值是固定的离散集合）。如果各 baseline 方法产生的 score 调整没有翻转任何 pairwise ordering，τ 就会完全相同，即使 raw scores 有差异。论文应报告各方法的 **raw model rankings**（不仅是 τ/ρ），让读者判断是真的 identical ordering 还是 τ 的离散性掩盖了细微差异。

补充：我在自己审稿中也要求了 raw scores（我的 W1），因为 identical τ/ρ ≠ identical scores。作者应在 rebuttal 中提供这一信息。

---

## Should-Fix 问题回应

**[AGREE] R2-W1: Limitations 计数错误**

确认。limitations.tex L1 写 "We identify **three** limitations"，但实际列出了四个：(1) fully crossed design requirement, (2) Stage 2 anchor dependency, (3) single benchmark, (4) 71% CI coverage。这是一个 minor editing error，但与 N1（judge 名称不一致）、N2（数值矛盾）构成 pattern，说明论文在提交前缺乏充分的 proofreading。

---

**[AGREE] R2-W2: Table 3 caption "preliminary"**

同意。我的 W7 同样标记了此问题。投稿论文中不应出现 "preliminary" 标注。要么增加 seeds 使实验充分，要么移除该标注。

---

**[REBUT] R2-W3: 贡献新颖性为增量组合**

不完全同意。R2 的评价过于简化。

1. **OVB 形式化是独立贡献**（§2, Observation 1）：将 judge bias 和 contamination 的交互作用形式化为 OVB 问题，并推导出 bias ∝ γ_n · c_n 的方向性预测，这不是简单组合 MFRM 和 DG-IRT。这个 insight 对 LLM evaluation 社区有独立价值——它解释了为什么所有 sequential pipelines 都产生 directional bias。

2. **Identifiability 分析虽用标准技术但结论非平凡**：Theorem 1 的 Schur complement proof 确实使用标准的 Rothenberg (1971) 方法，但证明了一个新模型的 identifiability 条件。关键的 Proposition 2（constant exposure ⇒ non-identifiability）是一个有用的 negative result，直接 motivates staged estimation design。

3. **与 DG-IRT 的区别是实质性的**（§3.1, method.tex L27）：连续 exposure（vs DG-IRT 的 binary）、多 facet 结构（judge severity $d_j$）、externally estimated exposure——这三点不是表面修改而是对 LLM evaluation 场景的必要适配。

不过，我承认 R2 的关切有一定道理：**如果 real-data 结果强有力，incremental novelty 不是问题；但当 real-data 结果不显著时，novelty bar 就更高了**。目前的 empirical evidence 不够强，确实使 novelty 的评价更加 borderline。

---

**[AGREE] R2-W4: Conclusion 过于简短**

同意。conclusion.tex 仅 2 句话（约 40 词），对一篇有 OVB theory + identifiability proof + staged estimation + synthetic & real experiments 的论文来说过于简短。至少应总结 key takeaways 和 limitations，即使在 8 页限制下也可以写 4-6 句。但这是写作质量问题，不影响接收决定。

---

**[REBUT] R2-W5: 遗漏重要相关工作**

部分不同意。

- **Polo et al. 2024 (tinyBenchmarks)** 和 **Kipnis et al. 2025 (MetaBench)**：这两篇关注 IRT 在 benchmark efficiency 上的应用（减少 evaluation items），与本文关注的 contamination-bias confounding 问题不在同一维度。作为 "IRT for LLM" 的广泛背景可以一句话带过，但不属于 "遗漏重要相关工作"。§5 Related Work 的 "IRT and MFRM for LLM Evaluation" 段落（related_work.tex L16-17）已覆盖了 Jiao et al. (2025) 和 Zhou et al. (2025, PSN-IRT) 等核心 IRT-for-LLM 工作。
- **Chernozhukov et al. 2022 (OVB in causal ML)**：如果这篇论文确实讨论了 ML context 下的 OVB，那确实应该引用以 contextualize §2 的 OVB 分析。**同意应补充此引用**。

总体：三篇中一篇确实应该引用，另外两篇属于 nice-to-have 而非 critical omission。

---

**[AGREE] R2-W6: CI Coverage 71%**

完全同意，与我的 W5 一致。71% vs 95% nominal 是 substantial miscalibration。补充我的分析：这个问题可能与 N4（MCMC 收敛不足，ESS=217 < 400）有共同根因。如果 posterior sampling 本身不够充分，CI 的 coverage 自然不可靠。论文应诊断这两个问题是否相关。

---

**[AGREE] R2-W7: 无代码/数据可用性声明**

同意。ARR 鼓励代码和数据公开，缺乏 availability statement 会影响 reproducibility 评分。特别是本文涉及 Stage 2 exposure estimation pipeline 的具体实现细节（anchoring 算法、z-score standardization 的具体操作），仅靠论文描述难以完整复现。

---

## Questions 回应

**R2-Q1 (Judge 名称)**：同意需要澄清，与我的 Q1 一致。

**R2-Q2 (Raw scores)**：强烈支持此问题，与我的 W1 一致。作者应提供各 baseline 的 raw model scores 或 complete rankings，而非仅报告 τ/ρ。

**R2-Q3 (CyclicJudge+discard 实际价值)**：好问题。如果移除 exposed items 不改变 ranking，论文需要解释为什么 G-MFRM 的 approach（调整而非移除）会产生不同结果。

**R2-Q4 (Horseshoe prior CI coverage)**：论文提到 "Horseshoe and HalfNormal hierarchical priors yield near-identical point estimates (Pearson r > 0.999)"（experiments.tex L44），但未报告 Horseshoe 的 CI coverage。如果 Horseshoe coverage 更好，HalfNormal 可能不是最佳 prior choice。

**R2-Q5 (开源计划)**：支持此问题，与 W7 相关。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 13

## Round 13

58 recorded events


### User

_source line 339 · 2026-05-23T06:17:24.578221+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性**审查。

## Venue 信息
- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle 提交）
- **截止日期**：2026-05-26
- **类型**：Long paper（正文 8 页限制，参考文献不限页数，Limitations 不计入页数）
- **模板**：ACL ARR LaTeX 模板
- **匿名规则**：Double-blind
- **评分标准**：ARR Overall Assessment 1-5 分制（5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit）

## 论文文件
- **LaTeX 源码**：`projects/gated_mfrm_judge_bias/docs/paper/main.tex`
- **PDF**：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/submitted.pdf`

## 你的审查侧重

**方法严谨性**，具体包括：

1. **数学推导正确性**：Observation 1（OVB bias characterization）的线性近似→非线性模型迁移是否合理？Proposition 1-2 和 Theorem 1 的证明是否完备？
2. **统计方法合理性**：G-MFRM 的三阶段估计流程（MFRM warm-start → exposure estimation → joint MCMC）是否有方法论缺陷？Generated regressors 问题的处理（Murphy-Topel correction）是否充分？
3. **收敛诊断**：MCMC 收敛标准（R̂、ESS）是否达标？posterior CI coverage 71% 的讨论是否充分？
4. **Error propagation bounds**：σ_crit 阈值的推导和验证是否可靠？attenuation factor 分析的假设是否过强？
5. **可识别性分析**：Theorem 1 的充分条件是否合理？外部固定 e_i 的必要性论证是否令人信服？
6. **统计显著性**：主结果 Δτ bootstrap CI 包含零——这一不显著结果的处理和讨论是否诚实、充分？

请给出完整审稿意见，包括 Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment（评分 + 置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-23T06:17:33.558648+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-23T06:17:33.609597+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/review_reviewer_1_51c3c93c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-23T06:17:37.222363+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-prod43"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-prod43"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-23T06:17:37.513586+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 291
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-23T06:17:39.503707+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-23T06:17:39.790656+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 286
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-23T06:17:41.413215+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start*",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start*",
    "path": "/home/ubuntu"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-23T06:17:41.615605+00:00_

/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-23T06:17:43.323413+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-23T06:17:43.526644+00:00_

1	---
2	name: review-reviewer-session-start
3	description: Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。
4	priority: 8
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 2
11	roles: []
12	---
13	
14	# Review Reviewer Session 启动流程
15	
16	执行顺序：
17	1. 读取论文文件（`projects/{project}/paper/main.tex` 或类似路径）
18	2. 检查论文格式状态：
19	   - 页数是否在 venue 要求内（若已知 venue）
20	   - LaTeX 是否可编译（调用 `ssh_execute` 运行 `pdflatex` 或 `latexmk`）
21	   - 图表是否有标题和标签
22	3. 视觉检查：如果已有编译好的 PDF，使用 `paper-visual-review` skill 渲染关键页面（首页、图表页、参考文献页），检查排版溢出、公式渲染、图表质量等视觉问题
23	4. 检查投稿材料清单：
24	   - cover letter 是否存在
25	   - 补充材料是否准备
26	   - 参考文献格式是否正确
27	5. 向 Review Director 汇报（`review_reviewer_post_to_director`）：
28	   - 论文当前状态
29	   - 发现的格式问题（如有）
30	   - 视觉检查结果（如有）
31	   - 缺少的材料（如有）
32	
33	此流程在 Review Director 分配任务后执行。
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-23T06:17:48.851492+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,WebSearch,WebFetch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,WebSearch,WebFetch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-23T06:17:48.851851+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-23T06:17:52.518696+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 353 · 2026-05-23T06:17:54.677729+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/submitted.pdf",
  "project": "gated_mfrm_judge_bias",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/submitted.pdf",
    "project": "gated_mfrm_judge_bias",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 354 · 2026-05-23T06:18:14.942684+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and scoring:

## Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score

The soundness scores must be justified by the text of the review.

## Overall Recommendation Score

The Overall a
…[truncated 953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 22423
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-23T06:18:17.679241+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.1}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 529.7}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-prod4
…[truncated 372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 23001
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-23T06:18:32.469861+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form including all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, confidence, and any other dimensions. Give me the exact scale descriptions for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form including all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, confidence, and any other dimensions. Give me the exact scale descriptions for each score level."
  }
}
```

</details>

---


### Tool call

_source line 357 · 2026-05-23T06:18:33.276475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-23T06:18:33.879607+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 359 · 2026-05-23T06:18:34.484628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 360 · 2026-05-23T06:18:35.606472+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2329
}
```

</details>

---


### Tool call

_source line 361 · 2026-05-23T06:18:35.606916+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-23T06:18:35.659601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-23T06:18:36.062011+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2182
}
```

</details>

---


### Tool result

_source line 364 · 2026-05-23T06:18:37.138067+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2653
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-23T06:18:37.640903+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2033
}
```

</details>

---


### Tool result

_source line 366 · 2026-05-23T06:18:37.691878+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2032
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-23T06:18:39.901001+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully. It's unlikely, though conceivable, that I missed something that should affect my ratings."
- **3**: "Pretty sure, but there's a chance I missed something. Although I have a good feel for this area in general, I did not carefully check the paper's details, e.g., the math or experimental design."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details, didn't understand some central points, or can't be sure about the novelty of the work."
- **1**: "Not my area, or paper is very hard to understand. My evaluation is just an educated guess."

## 2. **Soundness**
- **5**: Excellent thoroughness for paper type
- **4**: Strong support for all claims; additional experiments optional
- **3**: Sufficient support for main claims; minor details need support
- **2**: Major claims inadequately supported; significant technical/methodological problems
- **1**: Insufficiently thorough for publication or irrelevant to ACL

## 3. **Excitement**
- **5**: Highly exciting; would recommend/attend presentation
- **4**: Exciting; would mention to others or attend if possible
- **3**: Interesting; might mention points or attend if available
- **2**: Potentially interesting; may resonate with broader community
- **1**: Not exciting; unlikely to resonate with ACL community

## 4. **Overall Assessment**
- **5**: Consider for Award (top 2.5%)
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings acceptance
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## 5. **Reproducibility**
- **5**: Results easily reproducible
- **4**: Mostly reproducible; minor variation
…[truncated 317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7431
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-23T06:18:45.383778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 369 · 2026-05-23T06:18:45.787020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 370 · 2026-05-23T06:18:46.746177+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1362
}
```

</details>

---


### Tool call

_source line 371 · 2026-05-23T06:18:46.746645+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 372 · 2026-05-23T06:18:47.199851+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1412
}
```

</details>

---


### Tool call

_source line 373 · 2026-05-23T06:18:47.200342+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 374 · 2026-05-23T06:18:47.504749+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 758
}
```

</details>

---


### Tool call

_source line 375 · 2026-05-23T06:18:47.505373+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 376 · 2026-05-23T06:18:48.665116+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1464
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-23T06:18:48.968685+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1463
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-23T06:18:54.942603+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/submitted.pdf",
  "project": "gated_mfrm_judge_bias",
  "pages": "11-14",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/submitted.pdf",
    "project": "gated_mfrm_judge_bias",
    "pages": "11-14",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-23T06:18:55.647523+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 433.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.4}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 349.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 439.1}], \"total_pages\": 14, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-23T06:18:58.208496+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 381 · 2026-05-23T06:18:58.661592+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 382 · 2026-05-23T06:18:59.616610+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-23T06:18:59.617295+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-23T06:18:59.768200+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 385 · 2026-05-23T06:18:59.969393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 386 · 2026-05-23T06:19:00.231125+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 462
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-23T06:19:00.835133+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 865
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-23T06:20:55.864063+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE text for the Soundness scoring scale (all levels 1-5 with full descriptions), Excitement scoring scale (all levels 1-5), and Overall Assessment scoring scale (all levels 1-5). I need the exact wording of each level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE text for the Soundness scoring scale (all levels 1-5 with full descriptions), Excitement scoring scale (all levels 1-5), and Overall Assessment scoring scale (all levels 1-5). I need the exact wording of each level."
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-23T06:21:01.485635+00:00_

# ACL Rolling Review Scoring Scales

## Soundness Scale

1 = "Major Issues: This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL."

2 = "Poor: Some of the main claims are not sufficiently supported. There are major technical/methodological problems."

3 = "Acceptable: This study provides sufficient support for its main claims. Some minor points may need extra support or details."

4 = "Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential."

5 = "Excellent: This study is one of the most thorough I have seen, given its type."

## Excitement Scale

1 = "Not Exciting: this paper does not resonate with me, and I don't think it would with others in the *ACL community."

2 = "Potentially Interesting: this paper does not resonate with me, but it might with others in the *ACL community."

3 = "Interesting: I might mention some points of this paper to others and/or attend its presentation if there's time."

4 = "Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference."

5 = "Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference."

## Overall Assessment Scale

1 = "Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community."

2 = "Resubmit after next cycle: This paper needs substantial revisions that cannot be completed by the next ARR cycle."

3 = "Findings: I think this paper could be accepted to the Findings of the ACL."

4 = "Conference: I think this paper could be accepted to an *ACL conference."

5 = "Consider for Award: This paper could be considered for an outstanding paper award at an *ACL conference."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5621
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-23T06:21:55.478245+00:00_

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
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
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

_source line 391 · 2026-05-23T06:21:55.478759+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-23T06:23:57.112711+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见：方法严谨性审查\n\n## 论文信息\n**Title**: Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation\n**Venue**: EMNLP 2026 via ARR May 2026 cycle\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 方法框架新颖且理论推导总体正确，但主结果 Δτ 统计不显著、posterior CI coverage 仅 71%、Murphy-Topel 校正在小样本下不充分，这三个统计缺陷共同削弱了论文的核心 claim。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要 claim 有基本支撑，但关键统计证据存在显著缺口（Δτ 不显著、CI 覆盖率低、OVB 近似无形式化误差界） |\n| Excitement | 3/5 | 将 judge bias 和 contamination 统一建模为 OVB 问题的思路有创意，但统计证据的薄弱限制了影响力 |\n| Reproducibility | 4/5 | 三阶段估计流程描述清晰，MCMC 超参数明确，代码承诺公开；但 Stage 2 exposure 估计的 75/25 权重缺少 justification |\n| Confidence | 4/5 | 我熟悉 IRT/MFRM 模型、Bayesian MCMC、generated regressors 问题和 Murphy-Topel 校正 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Posterior CI coverage 仅 71%，不确定性量化严重失准\n- 具体位置：Section 4.3（Error Propagation Robustness）、Figure 5、Limitations\n- 问题：论文报告 empirical CI coverage 仅为 71%（名义水平 95%），即 posterior credible intervals 严重偏窄。论文将此归因于 HalfNormal prior 的边界约束和 NUTS tree-depth 限制（Limitations, p.9），但这两个解释都不充分：(a) HalfNormal 先验是作者自己选择的，不应成为 undercoverage 的借口；(b) tree-depth 限制是实现问题，不是方法论约束。Murphy-Topel 校正（Appendix C）本应解决 generated regressors 引入的额外不确定性，但 71% 的覆盖率表明该校正在当前样本量下**不充分**。\n- 为什么影响接收：论文的核心贡献之一是提供\"contamination-corrected fair scores\"，但如果 posterior CIs 本身就不可靠，那么基于这些 CIs 做出的推断（如 Table 6 中 c_m 的 95% CI、Section 4.2 中\"zero contamination estimates\"的判断）都缺乏可信度。\n- 建议修改方向：(1) 使用 simulation-based calibration (SBC; Talts et al., 2018) 系统性诊断 posterior 校准问题的来源；(2) 考虑 parametric bootstrap 替代 Murphy-Topel 作为有限样本校正；(3) 如果 71% 是当前方法的固有限制，需在正文（而非仅 Limitations）中明确标注所有 CI 均应视为下界而非校准区间。\n\n**N2** [critical] 主结果 Δτ 统计不显著，但论文 framing 暗示方法有效\n- 具体位置：Abstract（\"nominally higher rank agreement\"）、Section 4.2（Table 1, bootstrap CI）\n- 问题：G-MFRM 的 Kendall τ = 0.857 vs baselines 0.786，bootstrap Δτ 95% CI 包含零。论文随后用 LOO cross-validation（ΔELPD_LOO = −60.0, SE = 9.4）作为替代证据，称之为\"decisive evidence\"。但 ΔELPD 衡量的是**模型拟合质量**（对观测评分的预测能力），而非**排名准确性**（与人类排名的一致性）——这两者之间存在逻辑跳跃。一个模型可以更好地拟合评分数据但并不改善最终排名。论文标题和 abstract 的核心 claim 是\"fair scores\"（即更准确的排名），但统计上无法拒绝\"G-MFRM 与 baseline 排名无差异\"的零假设。\n- 为什么影响接收：这是论文实证贡献的根基。如果排名改善不显著，\"fair scores\"的 claim 就缺乏直接证据支撑。\n- 建议修改方向：(1) 在更大规模的 benchmark 上验证（N ≥ 17 根据论文自身的 power 分析）；(2) 明确区分 model-fit evidence 和 ranking-accuracy evidence，不要用 LOO 结果替代 Δτ 显著性；(3) 如果无法获得更大样本，考虑将 contribution 重新框定为\"improved model fit and diagnostic capability\"而非\"fair scores\"。\n\n**N3** [critical] OVB 线性近似（Observation 1）缺乏形式化误差界\n- 具体位置：Section 2（Observation 1, Eq. 2-3）、Section 4.3 验证\n- 问题：Observation 1 将 ordinal logit link 下的 contamination omission bias 用线性 OVB 公式（Wooldridge, 2010; Angrist & Pischke, 2009）刻画。这一近似对线性模型精确成立，但对 ordinal logistic 模型仅为近似。论文用合成数据验证（Figure 1, r = 0.86, p < 0.001），但 r = 0.86 意味着约 26% 的方差未被解释。更关键的是，论文没有给出近似误差的**形式化上界**：在什么条件下（contamination effect 大小、score 分布极端程度）线性近似会严重偏离？r = 0.86 的合成验证条件（N = 50, I = 100, J = 8, 20 seeds）是否代表了真实场景的难度？\n- 为什么影响接收：Observation 1 是整篇论文的理论动机——它论证了为什么需要 G-MFRM。如果线性近似在某些现实条件下失效，论文的理论基础就不完整。\n- 建议修改方向：(1) 给出 Taylor 展开的高阶余项分析，明确近似误差与 c_m · e_i 乘积大小的关系；(2) 在合成实验中系统性地变化 contamination effect magnitude，展示近似质量如何随 effect size 变化；(3) 至少讨论在什么条件下近似会 break down。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Murphy-Topel 校正的有限样本性能未验证\n- 具体位置：Appendix C、Section 3.4\n- 问题：Murphy-Topel 校正（Murphy & Topel, 1985）是**渐近**方法，其有效性依赖大样本近似。当前设置下模型级参数（θ_n, c_m）的有效样本量仅为 N = 8，远低于渐近理论的适用范围。论文在 Appendix C 推导了校正公式并声称\"the inflation is concentrated on c_m for contaminated models\"，但未通过模拟验证该校正在 N = 8 时的实际 coverage。结合 N1 中 71% 的 CI coverage，有理由怀疑 Murphy-Topel 校正在此 setting 下系统性不足。\n- 建议：在合成数据上（N = 8, 50, 100）比较 Murphy-Topel 校正后 CI coverage 与 nominal level 的偏差，量化有限样本失准的程度。\n\n**W2** [warning] Stage 2 exposure 估计流程包含 ad hoc 设计选择\n- 具体位置：Section 3.2（Stage 2: Exposure estimation）、Section 4.1\n- 问题：Per-item exposure e_i 的估计结合了 (1) 固定参考模型 gpt-4-0314 的 anchoring（75% 权重）和 (2) cross-model agreement 信号（25% 权重），clipped 到 [0, 1]。这些设计选择——75/25 权重、参考模型选择、clipping 策略——均缺乏理论 justification 或 sensitivity analysis。论文提到\"LogProber can provide graded and/or additive non-binary signals, though it is not used in our current experiments\"，但未解释为何不用。\n- 建议：(1) 提供 sensitivity analysis，展示 60/40、80/20 等不同权重下结果的稳健性；(2) 解释参考模型选择的理由及更换参考模型的影响；(3) 如果设计选择对结果不敏感，明确声明。\n\n**W3** [warning] σ_crit 阈值的推导假设过强\n- 具体位置：Section 3.4（Error Propagation）、Eq. 6、Table 2\n- 问题：Attenuation factor λ(σ) = Var(e)/(Var(e) + σ²)（Eq. 6）来自经典的 errors-in-variables (EIV) 理论，但该公式假设：(a) exposure 估计误差为加性高斯噪声；(b) 误差与真实 exposure 独立；(c) 误差方差在所有 items 上同质（homoskedastic）。条件 (b) 和 (c) 在实践中不太可能成立——difficulty 更大的 items 或 exposure 极端值处的估计误差通常更大。σ_crit < 0.2（对应 6% ability RMSE 下降）的选择也缺乏 principled justification。\n- 建议：(1) 讨论 Gaussian/独立/同方差假设的合理性；(2) 在 heteroskedastic 误差下重做 attenuation 分析；(3) 解释 6% 阈值的选择依据。\n\n**W4** [warning] Theorem 1 证明过于压缩，关键步骤缺乏细节\n- 具体位置：Appendix A（Proof of Theorem 1）\n- 问题：证明分三步（Fisher information submatrix → item/judge blocks → Schur complement），总体结构正确，但关键技术细节不足：(a) Step 1 中 det F_n > 0 依赖 Var_e(e_i) > 0，但 Cauchy-Schwarz 不等式的应用条件（weighted variance with w_{ij} weights）需要更明确的推导；(b) Step 2 中\"connected design\"条件如何精确映射到 conditions (i)-(ii) 不够清晰；(c) Schur complement 从 block diagonal A 到 full F 的非奇异性推导跳步较大。此外，Theorem 1 给出的是**局部可辨识性**（local identifiability），而非全局可辨识性——论文应明确讨论这一局限。\n- 建议：扩展证明细节，特别是 Step 1 的 Cauchy-Schwarz 应用和 Step 3 的 Schur complement 推导；讨论局部 vs 全局可辨识性的实际影响。\n\n**W5** [warning] MCMC 收敛标准偏宽松\n- 具体位置：Section 4.1（MCMC 设置）\n- 问题：论文使用 R̂ < 1.05 和 bulk ESS > 300 作为收敛标准，引用\"standard practice (Gelman et al., 2013)\"。但 Vehtari et al. (2021)——论文自己引用的参考文献——已更新推荐为 R̂ < 1.01 和 tail-ESS > 400。论文实际报告了\"rank-normalized split-R̂ (Vehtari et al., 2021) and bulk effective sample size (ESS), with thresholds R̂ < 1.05 and ESS_bulk > 300\"——即引用了 Vehtari 2021 的方法但使用了 Gelman 2013 的更宽标准。\n- 建议：按 Vehtari et al. (2021) 推荐的 R̂ < 1.01 重新检查收敛性，报告 tail-ESS。\n\n**W6** [warning] N = 8 的 power 不足，但缺少正式 power analysis\n- 具体位置：Section 4.2, Limitations\n- 问题：论文在多处承认 N = 8 太小（\"not statistically significant at N = 8\"、\"N ≥ 17 models for 80% power\"），但未提供正式的 power analysis。论文自身计算出需要 N ≥ 17，但仅在括号中一笔带过。对于一篇以统计方法为核心贡献的论文，这个 gap 较为突出。\n- 建议：将 power analysis 提升为正文的一个 subsection 或至少一段完整讨论，明确说明当前实验设计在什么 effect size 下有多大 power。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 4.2 使用\"decisive evidence\"描述 LOO 结果（p.7），措辞过强。ΔELPD 是模型比较指标，不等同于对 ranking improvement 的 decisive evidence。建议改为\"strong evidence for improved model fit\"。\n- Table 2 中 exposure noise σ 的取值范围（0, 0.2, 0.4, 0.5）较粗糙。σ = 0.1 和 0.3 处的行为未展示，难以判断 σ_crit ≈ 0.2 是否为真正的转折点。\n- Appendix C 中 Murphy-Topel 校正的实现描述提到\"inflating Stage 3 posterior samples by √(diag(V_MTF)/diag(V_3))\"——这是一种近似实现方式，但未讨论其与直接从校正后协方差矩阵采样的差异。\n- Figure 1 (p.4) 的 scatter plot 纵轴标签\"Sequential δ bias (θ̂_max − θ̂_true)\"不够直观，建议添加简短解释。\n- 论文在 Section 5 (Related Work) 中引用了 CycleJudge (Zhu et al., 2026) 和 UDA (Zhang et al., 2026) 等同期工作，但对比讨论较简略。\n\n---\n\n## 主要优势\n\n- **问题形式化出色**：将 judge bias 和 benchmark contamination 的 confounding 形式化为 omitted variable bias（Observation 1），从计量经济学引入了清晰的理论框架。这一视角在 LLM evaluation 文献中是新颖的。\n- **可辨识性分析完整**：Propositions 1-2 给出了可辨识性的必要条件（exposure 变异），Theorem 1 给出了充分条件，Corollary 1 刻画了 gating 结构的作用。这套分析为三阶段估计流程提供了理论基础。\n- **诚实的结果报告**：论文坦承 Δτ 不显著（abstract 即提及），而非掩盖或 spin。P(Δτ > 0) = 0.927 的 one-sided 信息也提供了有用参考。\n- **消融设计合理**：Table 3 的消融实验系统性地移除各组件，清晰展示了 joint estimation vs sequential estimation 的增益来源。\n- **Generated regressors 问题的正式处理**：识别并处理 Stage 2 → Stage 3 的 error propagation（Murphy-Topel correction）是方法论上的加分项，尽管校正在有限样本下不完全充分。\n- **Judge severity profiles 有实用价值**：Table 4 的 judge severity 估计和 Section G 的 self-evaluation robustness 分析为 LLM judge panel 设计提供了实用诊断信息。\n\n---\n\n## 总结\n\n本文提出了一个有理论深度的框架来联合建模 judge bias 和 benchmark contamination，问题形式化和可辨识性分析是其主要贡献。然而，方法的统计验证存在三个相互关联的缺陷：(1) 主结果 Δτ 不显著，(2) posterior CI coverage 仅 71%，(3) Murphy-Topel 校正在 N = 8 下不充分。这三个问题共同指向一个核心担忧——当前实验规模不足以可靠验证方法的有效性。论文对这些限制的讨论是诚实的，但不够充分。建议在更大规模的评测集上验证，并系统性地解决 CI 校准问题，之后可以成为一篇有影响力的方法论贡献。当前版本适合 Findings 接收。\n",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿意见：方法严谨性审查\n\n## 论文信息\n**Title**: Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation\n**Venue**: EMNLP 2026 via ARR May 2026 cycle\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 方法框架新颖且理论推导总体正确，但主结果 Δτ 统计不显著、posterior CI coverage 仅 71%、Murphy-Topel 校正在小样本下不充分，这三个统计缺陷共同削弱了论文的核心 claim。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要 claim 有基本支撑，但关键统计证据存在显著缺口（Δτ 不显著、CI 覆盖率低、OVB 近似无形式化误差界） |\n| Excitement | 3/5 | 将 judge bias 和 contamination 统一建模为 OVB 问题的思路有创意，但统计证据的薄弱限制了影响力 |\n| Reproducibility | 4/5 | 三阶段估计流程描述清晰，MCMC 超参数明确，代码承诺公开；但 Stage 2 exposure 估计的 75/25 权重缺少 justification |\n| Confidence | 4/5 | 我熟悉 IRT/MFRM 模型、Bayesian MCMC、generated regressors 问题和 Murphy-Topel 校正 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Posterior CI coverage 仅 71%，不确定性量化严重失准\n- 具体位置：Section 4.3（Error Propagation Robustness）、Figure 5、Limitations\n- 问题：论文报告 empirical CI coverage 仅为 71%（名义水平 95%），即 posterior credible intervals 严重偏窄。论文将此归因于 HalfNormal prior 的边界约束和 NUTS tree-depth 限制（Limitations, p.9），但这两个解释都不充分：(a) HalfNormal 先验是作者自己选择的，不应成为 undercoverage 的借口；(b) tree-depth 限制是实现问题，不是方法论约束。Murphy-Topel 校正（Appendix C）本应解决 generated regressors 引入的额外不确定性，但 71% 的覆盖率表明该校正在当前样本量下**不充分**。\n- 为什么影响接收：论文的核心贡献之一是提供\"contamination-corrected fair scores\"，但如果 posterior CIs 本身就不可靠，那么基于这些 CIs 做出的推断（如 Table 6 中 c_m 的 95% CI、Section 4.2 中\"zero contamination estimates\"的判断）都缺乏可信度。\n- 建议修改方向：(1) 使用 simulation-based calibration (SBC; Talts et al., 2018) 系统性诊断 posterior 校准问题的来源；(2) 考虑 parametric bootstrap 替代 Murphy-Topel 作为有限样本校正；(3) 如果 71% 是当前方法的固有限制，需在正文（而非仅 Limitations）中明确标注所有 CI 均应视为下界而非校准区间。\n\n**N2** [critical] 主结果 Δτ 统计不显著，但论文 framing 暗示方法有效\n- 具体位置：Abstract（\"nominally higher rank agreement\"）、Section 4.2（Table 1, bootstrap CI）\n- 问题：G-MFRM 的 Kendall τ = 0.857 vs baselines 0.786，bootstrap Δτ 95% CI 包含零。论文随后用 LOO cross-validation（ΔELPD_LOO = −60.0, SE = 9.4）作为替代证据，称之为\"decisive evidence\"。但 ΔELPD 衡量的是**模型拟合质量**（对观测评分的预测能力），而非**排名准确性**（与人类排名的一致性）——这两者之间存在逻辑跳跃。一个模型可以更好地拟合评分数据但并不改善最终排名。论文标题和 abstract 的核心 claim 是\"fair scores\"（即更准确的排名），但统计上无法拒绝\"G-MFRM 与 baseline 排名无差异\"的零假设。\n- 为什么影响接收：这是论文实证贡献的根基。如果排名改善不显著，\"fair scores\"的 claim 就缺乏直接证据支撑。\n- 建议修改方向：(1) 在更大规模的 benchmark 上验证（N ≥ 17 根据论文自身的 power 分析）；(2) 明确区分 model-fit evidence 和 ranking-accuracy evidence，不要用 LOO 结果替代 Δτ 显著性；(3) 如果无法获得更大样本，考虑将 contribution 重新框定为\"improved model fit and diagnostic capability\"而非\"fair scores\"。\n\n**N3** [critical] OVB 线性近似（Observation 1）缺乏形式化误差界\n- 具体位置：Section 2（Observation 1, Eq. 2-3）、Section 4.3 验证\n- 问题：Observation 1 将 ordinal logit link 下的 contamination omission bias 用线性 OVB 公式（Wooldridge, 2010; Angrist & Pischke, 2009）刻画。这一近似对线性模型精确成立，但对 ordinal logistic 模型仅为近似。论文用合成数据验证（Figure 1, r = 0.86, p < 0.001），但 r = 0.86 意味着约 26% 的方差未被解释。更关键的是，论文没有给出近似误差的**形式化上界**：在什么条件下（contamination effect 大小、score 分布极端程度）线性近似会严重偏离？r = 0.86 的合成验证条件（N = 50, I = 100, J = 8, 20 seeds）是否代表了真实场景的难度？\n- 为什么影响接收：Observation 1 是整篇论文的理论动机——它论证了为什么需要 G-MFRM。如果线性近似在某些现实条件下失效，论文的理论基础就不完整。\n- 建议修改方向：(1) 给出 Taylor 展开的高阶余项分析，明确近似误差与 c_m · e_i 乘积大小的关系；(2) 在合成实验中系统性地变化 contamination effect magnitude，展示近似质量如何随 effect size 变化；(3) 至少讨论在什么条件下近似会 break down。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Murphy-Topel 校正的有限样本性能未验证\n- 具体位置：Appendix C、Section 3.4\n- 问题：Murphy-Topel 校正（Murphy & Topel, 1985）是**渐近**方法，其有效性依赖大样本近似。当前设置下模型级参数（θ_n, c_m）的有效样本量仅为 N = 8，远低于渐近理论的适用范围。论文在 Appendix C 推导了校正公式并声称\"the inflation is concentrated on c_m for contaminated models\"，但未通过模拟验证该校正在 N = 8 时的实际 coverage。结合 N1 中 71% 的 CI coverage，有理由怀疑 Murphy-Topel 校正在此 setting 下系统性不足。\n- 建议：在合成数据上（N = 8, 50, 100）比较 Murphy-Topel 校正后 CI coverage 与 nominal level 的偏差，量化有限样本失准的程度。\n\n**W2** [warning] Stage 2 exposure 估计流程包含 ad hoc 设计选择\n- 具体位置：Section 3.2（Stage 2: Exposure estimation）、Section 4.1\n- 问题：Per-item exposure e_i 的估计结合了 (1) 固定参考模型 gpt-4-0314 的 anchoring（75% 权重）和 (2) cross-model agreement 信号（25% 权重），clipped 到 [0, 1]。这些设计选择——75/25 权重、参考模型选择、clipping 策略——均缺乏理论 justification 或 sensitivity analysis。论文提到\"LogProber can provide graded and/or additive non-binary signals, though it is not used in our current experiments\"，但未解释为何不用。\n- 建议：(1) 提供 sensitivity analysis，展示 60/40、80/20 等不同权重下结果的稳健性；(2) 解释参考模型选择的理由及更换参考模型的影响；(3) 如果设计选择对结果不敏感，明确声明。\n\n**W3** [warning] σ_crit 阈值的推导假设过强\n- 具体位置：Section 3.4（Error Propagation）、Eq. 6、Table 2\n- 问题：Attenuation factor λ(σ) = Var(e)/(Var(e) + σ²)（Eq. 6）来自经典的 errors-in-variables (EIV) 理论，但该公式假设：(a) exposure 估计误差为加性高斯噪声；(b) 误差与真实 exposure 独立；(c) 误差方差在所有 items 上同质（homoskedastic）。条件 (b) 和 (c) 在实践中不太可能成立——difficulty 更大的 items 或 exposure 极端值处的估计误差通常更大。σ_crit < 0.2（对应 6% ability RMSE 下降）的选择也缺乏 principled justification。\n- 建议：(1) 讨论 Gaussian/独立/同方差假设的合理性；(2) 在 heteroskedastic 误差下重做 attenuation 分析；(3) 解释 6% 阈值的选择依据。\n\n**W4** [warning] Theorem 1 证明过于压缩，关键步骤缺乏细节\n- 具体位置：Appendix A（Proof of Theorem 1）\n- 问题：证明分三步（Fisher information submatrix → item/judge blocks → Schur complement），总体结构正确，但关键技术细节不足：(a) Step 1 中 det F_n > 0 依赖 Var_e(e_i) > 0，但 Cauchy-Schwarz 不等式的应用条件（weighted variance with w_{ij} weights）需要更明确的推导；(b) Step 2 中\"connected design\"条件如何精确映射到 conditions (i)-(ii) 不够清晰；(c) Schur complement 从 block diagonal A 到 full F 的非奇异性推导跳步较大。此外，Theorem 1 给出的是**局部可辨识性**（local identifiability），而非全局可辨识性——论文应明确讨论这一局限。\n- 建议：扩展证明细节，特别是 Step 1 的 Cauchy-Schwarz 应用和 Step 3 的 Schur complement 推导；讨论局部 vs 全局可辨识性的实际影响。\n\n**W5** [warning] MCMC 收敛标准偏宽松\n- 具体位置：Section 4.1（MCMC 设置）\n- 问题：论文使用 R̂ < 1.05 和 bulk ESS > 300 作为收敛标准，引用\"standard practice (Gelman et al., 2013)\"。但 Vehtari et al. (2021)——论文自己引用的参考文献——已更新推荐为 R̂ < 1.01 和 tail-ESS > 400。论文实际报告了\"rank-normalized split-R̂ (Vehtari et al., 2021) and bulk effective sample size (ESS), with thresholds R̂ < 1.05 and ESS_bulk > 300\"——即引用了 Vehtari 2021 的方法但使用了 Gelman 2013 的更宽标准。\n- 建议：按 Vehtari et al. (2021) 推荐的 R̂ < 1.01 重新检查收敛性，报告 tail-ESS。\n\n**W6** [warning] N = 8 的 power 不足，但缺少正式 power analysis\n- 具体位置：Section 4.2, Limitations\n- 问题：论文在多处承认 N = 8 太小（\"not statistically significant at N = 8\"、\"N ≥ 17 models for 80% power\"），但未提供正式的 power analysis。论文自身计算出需要 N ≥ 17，但仅在括号中一笔带过。对于一篇以统计方法为核心贡献的论文，这个 gap 较为突出。\n- 建议：将 power analysis 提升为正文的一个 subsection 或至少一段完整讨论，明确说明当前实验设计在什么 effect size 下有多大 power。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 4.2 使用\"decisive evidence\"描述 LOO 结果（p.7），措辞过强。ΔELPD 是模型比较指标，不等同于对 ranking improvement 的 decisive evidence。建议改为\"strong evidence for improved model fit\"。\n- Table 2 中 exposure noise σ 的取值范围（0, 0.2, 0.4, 0.5）较粗糙。σ = 0.1 和 0.3 处的行为未展示，难以判断 σ_crit ≈ 0.2 是否为真正的转折点。\n- Appendix C 中 Murphy-Topel 校正的实现描述提到\"inflating Stage 3 posterior samples by √(diag(V_MTF)/diag(V_3))\"——这是一种近似实现方式，但未讨论其与直接从校正后协方差矩阵采样的差异。\n- Figure 1 (p.4) 的 scatter plot 纵轴标签\"Sequential δ bias (θ̂_max − θ̂_true)\"不够直观，建议添加简短解释。\n- 论文在 Section 5 (Related Work) 中引用了 CycleJudge (Zhu et al., 2026) 和 UDA (Zhang et al., 2026) 等同期工作，但对比讨论较简略。\n\n---\n\n## 主要优势\n\n- **问题形式化出色**：将 judge bias 和 benchmark contamination 的 confounding 形式化为 omitted variable bias（Observation 1），从计量经济学引入了清晰的理论框架。这一视角在 LLM evaluation 文献中是新颖的。\n- **可辨识性分析完整**：Propositions 1-2 给出了可辨识性的必要条件（exposure 变异），Theorem 1 给出了充分条件，Corollary 1 刻画了 gating 结构的作用。这套分析为三阶段估计流程提供了理论基础。\n- **诚实的结果报告**：论文坦承 Δτ 不显著（abstract 即提及），而非掩盖或 spin。P(Δτ > 0) = 0.927 的 one-sided 信息也提供了有用参考。\n- **消融设计合理**：Table 3 的消融实验系统性地移除各组件，清晰展示了 joint estimation vs sequential estimation 的增益来源。\n- **Generated regressors 问题的正式处理**：识别并处理 Stage 2 → Stage 3 的 error propagation（Murphy-Topel correction）是方法论上的加分项，尽管校正在有限样本下不完全充分。\n- **Judge severity profiles 有实用价值**：Table 4 的 judge severity 估计和 Section G 的 self-evaluation robustness 分析为 LLM judge panel 设计提供了实用诊断信息。\n\n---\n\n## 总结\n\n本文提出了一个有理论深度的框架来联合建模 judge bias 和 benchmark contamination，问题形式化和可辨识性分析是其主要贡献。然而，方法的统计验证存在三个相互关联的缺陷：(1) 主结果 Δτ 不显著，(2) posterior CI coverage 仅 71%，(3) Murphy-Topel 校正在 N = 8 下不充分。这三个问题共同指向一个核心担忧——当前实验规模不足以可靠验证方法的有效性。论文对这些限制的讨论是诚实的，但不够充分。建议在更大规模的评测集上验证，并系统性地解决 CI 校准问题，之后可以成为一篇有影响力的方法论贡献。当前版本适合 Findings 接收。\n",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-23T06:24:01.335616+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4222
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-23T06:24:05.013480+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_3/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-23T06:24:05.064219+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 396 · 2026-05-23T06:24:13.655981+00:00_

审稿意见已提交给 Review Director。

**核心判断**：Overall 3.0 (Findings)。方法框架（OVB 形式化 + G-MFRM + 可辨识性分析）有理论创新，但统计验证存在三个相互关联的关键缺陷：

1. **Δτ 不显著** — 排名改善无法拒绝零假设，论文用 LOO 替代但存在逻辑跳跃（model fit ≠ ranking accuracy）
2. **CI coverage 71%** — posterior 区间严重偏窄，Murphy-Topel 校正在 N=8 下不充分
3. **OVB 近似无误差界** — Observation 1 的线性近似仅有 r=0.86 的合成验证，缺乏形式化上界

这三个问题共同指向核心担忧：当前实验规模（N=8）不足以可靠验证方法有效性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 14

## Round 14

4 recorded events


### User

_source line 397 · 2026-05-23T06:25:25.185943+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿意见：新颖性与完整性

**Overall Assessment**: 3 / 5 (Findings)
**Confidence**: 4 / 5

### Must-Fix 问题

**N1** [critical] 单一 benchmark 评估不足以支撑 generality claims
- 全文唯一的真实数据评估在 Arena-Hard 上进行，仅含 8 个 target models。Kendall τ 从 baseline 的 0.786 提升至 0.857，bootstrapped 95% CI 为 [−0.227, +0.722]，跨越零。Table 1 显示所有 7 个 baseline 产生完全相同的排名——G-MFRM 的改善仅来自一个 rank swap（positions 2–3）。

**N2** [critical] OVB formalization 作为独立 contribution 定位过高
- Observation 1 本质上是将 Angrist & Pischke (2009) 的教科书 OVB 公式直接代入 MFRM 的线性近似。将教科书公式的直接应用列为首要 contribution，可能让熟悉计量经济学的 reviewer 认为新颖性不足。

**N3** [critical] 与 DG-IRT 的增量新颖性需更清晰界定
- G-MFRM 与 DG-IRT 的三点差异（连续 exposure、judge severity facet、外部估计 exposure）是 reasonable 的工程扩展，但核心建模思想（IRT + multiplicative contamination gating）直接来自 DG-IRT。

### Should-Fix 问题

**W1** [warning] Stage 2 exposure estimation 包含多个启发式选择，缺乏敏感性分析
- 75%/25% 权重、reference model 选择缺乏理论依据和 sensitivity analysis。

**W2** [warning] Bilinear contamination 模型假设 rank-1 交互结构，可能过于简化
- c_n · e_i 意味着所有模型的 contamination pattern 按标量缩放，miss 异质性。

**W3** [warning] CI overcoverage 71% 的实际影响未充分讨论
- 后验过度自信对 contamination 诊断可靠性的影响缺乏操作化建议。

**W4** [warning] Self-judging bias 未充分整合
- Qwen2.5-72B 和 LLaMA-3.3-70B 的 self-evaluation bias 未在 G-MFRM 中显式建模。

### Missing References
1. Polo et al. (2024) "tinyBenchmarks"
2. Ye et al. (2024) "Justice or Prejudice?"
3. Panickssery et al. (2024) "LLM Evaluators Recognize and Favor Their Own Generations"

---

请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W4) 逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-23T06:26:49.198569+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### [AGREE] R2-N1: 单一 benchmark 评估不足以支撑 generality claims\n\n同意。这与我自己的 N2 高度一致。Arena-Hard 上 N = 8 models 的评估规模过小，Δτ bootstrap CI 包含零，而所有 7 个 baseline 产生完全相同的排名这一事实进一步说明 G-MFRM 的改善仅为 positions 2–3 的一次 rank swap。从方法严谨性角度补充：论文自身在 Section 4.2 承认需要 N ≥ 17 才能达到 80% power（括号中一笔带过），这等于论文自己证明了当前实验设计 underpowered。单一 benchmark + underpowered design 是我给出 Soundness 3/5 的主要原因之一。\n\n### [REBUT] R2-N2: OVB formalization 作为独立 contribution 定位过高\n\n部分不同意。R2 的批评——Observation 1 \"本质上是教科书 OVB 公式的直接应用\"——低估了两个方面的贡献：\n\n1. **问题识别本身有价值**：在 LLM evaluation 文献中，judge bias 和 benchmark contamination 此前被视为独立问题分别处理（Section 5 综述了 CycleJudge、UDA、DCR、CosStaR 等工作，它们各自只处理一种偏差）。将两者的 confounding 形式化为 OVB 问题——即证明忽略 contamination 会**系统性地、方向性地**偏置 ability 估计（而非仅增加噪声）——是一个有实质内容的理论洞察。Figure 1 的合成验证（r = 0.86, p < 0.001）证实了偏差的方向性和可预测性。\n\n2. **从 OVB 诊断到 G-MFRM 建模有非平凡的方法论跳跃**：Observation 1 不仅标识了问题，还直接指导了 G-MFRM 的设计——gating term c_m · e_i 精确地补回了被遗漏的交互项。这种\"诊断→建模\"的一致性在方法论上是加分的。\n\n但我同意 R2 的隐含建议：论文在 Section 1 contributions list 中的措辞可以更精确。与其将 Observation 1 列为\"identify and characterize\"，不如明确为\"formalize the confounding between judge bias and contamination as an OVB problem in the MFRM framework, providing the theoretical motivation for the gating mechanism\"。这样既不过度 claim 公式的新颖性，又准确传达了应用层面的贡献。\n\n### [REBUT] R2-N3: 与 DG-IRT 的增量新颖性需更清晰界定\n\n部分不同意。R2 称核心建模思想\"直接来自 DG-IRT\"，但忽略了 G-MFRM 相对于 DG-IRT 的几个**方法论层面**的实质差异（而非仅工程扩展）：\n\n1. **可辨识性分析是全新的**：DG-IRT（Shu et al., 2023）将 exposure 视为已知的二元变量，不需要讨论可辨识性。G-MFRM 将 exposure 外部估计后固定，引入了 generated regressors 问题，必须证明参数仍可辨识。Propositions 1–2 和 Theorem 1（Section 3.3, Appendix A）构成了一套完整的可辨识性分析框架——包括必要条件（Proposition 2: constant exposure → unidentifiable）和充分条件（Theorem 1: Fisher information non-singularity via Schur complement）。这在 IRT/contamination 文献中是新的。\n\n2. **Error propagation 分析是全新的**：Section 3.4 的 attenuation factor 分析（Eq. 6）和 Appendix C 的 Murphy-Topel 校正处理了 DG-IRT 完全不涉及的统计问题——generated regressors 的不确定性传播。\n\n3. **Judge severity facet 不是简单\"添加\"**：多 facet 结构改变了模型的几何——Fisher information matrix 从 2-facet 变为 3-facet，Schur complement 证明的结构也相应不同（Appendix A, Step 2 处理 item and judge blocks）。\n\n我承认论文应更清晰地界定与 DG-IRT 的关系——当前 Section 3.1 末段的三点对比确实读起来像\"feature list\"而非\"methodological advancement\"。建议作者重写该段，强调可辨识性分析和 error propagation 框架是 DG-IRT 所没有的方法论贡献。\n\n---\n\n## Should-Fix 问题\n\n### [AGREE] R2-W1: Stage 2 exposure estimation 启发式选择缺乏敏感性分析\n\n完全同意。这与我自己的 W2 一致。75/25 权重、reference model（gpt-4-0314）选择、clipping to [0,1] 都是 ad hoc 设计。方法论角度补充：这些选择直接影响 e_i 的质量，而 e_i 通过 Theorem 1 的条件（Var(e_i) > 0）和 error propagation（Eq. 6）影响下游所有推断。对一篇强调统计严谨性的论文来说，核心输入变量的构造缺乏 sensitivity analysis 是一个明显缺口。\n\n### [AGREE] R2-W2: Bilinear rank-1 交互假设可能过于简化\n\n同意，且补充方法论分析。c_m · e_i 的 rank-1 结构意味着模型 m 在所有 items 上的 contamination 增益按同一标量 c_m 缩放。现实中，不同模型可能对不同类型的 items（如 coding vs reasoning）有异质性 contamination 模式。一个自然的扩展是矩阵分解模型 C_{mi}（低秩但非 rank-1），但这会显著增加参数量并可能破坏 Theorem 1 的可辨识性条件。论文应至少在 Limitations 中讨论 rank-1 假设的局限性，并说明放松该假设对可辨识性的影响。\n\n### [AGREE] R2-W3: CI coverage 71% 实际影响未充分讨论\n\n同意，但需纠正 R2 的术语：71% 的 empirical coverage（nominal 95%）是 **undercoverage**（CI 过窄、过度自信），不是\"overcoverage\"。这与我自己的 N1 一致——这是我审稿意见中最严重的问题之一。补充观察：Figure 5 的 coverage 数据来自合成数据（N = 50, I = 100），真实数据（N = 8）下的 coverage 可能更差，因为 Murphy-Topel 校正的渐近近似在更小样本下更不可靠。论文需要提供操作化建议：如果 CI 不可靠，用户应如何解读 Table 6 中的 c_m 估计？建议至少报告 point estimate 的 sign 和 magnitude 的稳健性（如通过 leave-one-judge-out），而非依赖 CI。\n\n### [REBUT] R2-W4: Self-judging bias 未充分整合\n\n部分不同意。论文在 Appendix G（Section G: Contamination Susceptibility Recovery）中专门分析了 self-evaluation robustness：Qwen2.5-72B 的 self-judging win rate 为 1,000/1,424（vs cross-judge 0.714），LLaMA-3.3-70B 为 0.952（vs 0.714）。论文的处理策略是 empirical validation 而非 structural modeling——通过排除 self-judging pairs 后展示排名不变来论证 robustness。\n\n从方法论角度，将 self-judging bias 显式建模为 G-MFRM 的一个额外 facet（如 s_{nj} indicator when model n = judge j）会增加一组 N×J 的交互参数，在 N = 8, J = 9 的情况下参数量激增（至多 72 个额外参数），导致严重的过拟合风险和可辨识性问题。当前的 empirical robustness check 是合理的实用策略。\n\n但我同意论文应在正文（而非仅 Appendix）中更显著地讨论 self-judging bias 的处理及其局限性，因为这是 LLM-as-a-judge 文献中的已知核心问题。\n",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### [AGREE] R2-N1: 单一 benchmark 评估不足以支撑 generality claims\n\n同意。这与我自己的 N2 高度一致。Arena-Hard 上 N = 8 models 的评估规模过小，Δτ bootstrap CI 包含零，而所有 7 个 baseline 产生完全相同的排名这一事实进一步说明 G-MFRM 的改善仅为 positions 2–3 的一次 rank swap。从方法严谨性角度补充：论文自身在 Section 4.2 承认需要 N ≥ 17 才能达到 80% power（括号中一笔带过），这等于论文自己证明了当前实验设计 underpowered。单一 benchmark + underpowered design 是我给出 Soundness 3/5 的主要原因之一。\n\n### [REBUT] R2-N2: OVB formalization 作为独立 contribution 定位过高\n\n部分不同意。R2 的批评——Observation 1 \"本质上是教科书 OVB 公式的直接应用\"——低估了两个方面的贡献：\n\n1. **问题识别本身有价值**：在 LLM evaluation 文献中，judge bias 和 benchmark contamination 此前被视为独立问题分别处理（Section 5 综述了 CycleJudge、UDA、DCR、CosStaR 等工作，它们各自只处理一种偏差）。将两者的 confounding 形式化为 OVB 问题——即证明忽略 contamination 会**系统性地、方向性地**偏置 ability 估计（而非仅增加噪声）——是一个有实质内容的理论洞察。Figure 1 的合成验证（r = 0.86, p < 0.001）证实了偏差的方向性和可预测性。\n\n2. **从 OVB 诊断到 G-MFRM 建模有非平凡的方法论跳跃**：Observation 1 不仅标识了问题，还直接指导了 G-MFRM 的设计——gating term c_m · e_i 精确地补回了被遗漏的交互项。这种\"诊断→建模\"的一致性在方法论上是加分的。\n\n但我同意 R2 的隐含建议：论文在 Section 1 contributions list 中的措辞可以更精确。与其将 Observation 1 列为\"identify and characterize\"，不如明确为\"formalize the confounding between judge bias and contamination as an OVB problem in the MFRM framework, providing the theoretical motivation for the gating mechanism\"。这样既不过度 claim 公式的新颖性，又准确传达了应用层面的贡献。\n\n### [REBUT] R2-N3: 与 DG-IRT 的增量新颖性需更清晰界定\n\n部分不同意。R2 称核心建模思想\"直接来自 DG-IRT\"，但忽略了 G-MFRM 相对于 DG-IRT 的几个**方法论层面**的实质差异（而非仅工程扩展）：\n\n1. **可辨识性分析是全新的**：DG-IRT（Shu et al., 2023）将 exposure 视为已知的二元变量，不需要讨论可辨识性。G-MFRM 将 exposure 外部估计后固定，引入了 generated regressors 问题，必须证明参数仍可辨识。Propositions 1–2 和 Theorem 1（Section 3.3, Appendix A）构成了一套完整的可辨识性分析框架——包括必要条件（Proposition 2: constant exposure → unidentifiable）和充分条件（Theorem 1: Fisher information non-singularity via Schur complement）。这在 IRT/contamination 文献中是新的。\n\n2. **Error propagation 分析是全新的**：Section 3.4 的 attenuation factor 分析（Eq. 6）和 Appendix C 的 Murphy-Topel 校正处理了 DG-IRT 完全不涉及的统计问题——generated regressors 的不确定性传播。\n\n3. **Judge severity facet 不是简单\"添加\"**：多 facet 结构改变了模型的几何——Fisher information matrix 从 2-facet 变为 3-facet，Schur complement 证明的结构也相应不同（Appendix A, Step 2 处理 item and judge blocks）。\n\n我承认论文应更清晰地界定与 DG-IRT 的关系——当前 Section 3.1 末段的三点对比确实读起来像\"feature list\"而非\"methodological advancement\"。建议作者重写该段，强调可辨识性分析和 error propagation 框架是 DG-IRT 所没有的方法论贡献。\n\n---\n\n## Should-Fix 问题\n\n### [AGREE] R2-W1: Stage 2 exposure estimation 启发式选择缺乏敏感性分析\n\n完全同意。这与我自己的 W2 一致。75/25 权重、reference model（gpt-4-0314）选择、clipping to [0,1] 都是 ad hoc 设计。方法论角度补充：这些选择直接影响 e_i 的质量，而 e_i 通过 Theorem 1 的条件（Var(e_i) > 0）和 error propagation（Eq. 6）影响下游所有推断。对一篇强调统计严谨性的论文来说，核心输入变量的构造缺乏 sensitivity analysis 是一个明显缺口。\n\n### [AGREE] R2-W2: Bilinear rank-1 交互假设可能过于简化\n\n同意，且补充方法论分析。c_m · e_i 的 rank-1 结构意味着模型 m 在所有 items 上的 contamination 增益按同一标量 c_m 缩放。现实中，不同模型可能对不同类型的 items（如 coding vs reasoning）有异质性 contamination 模式。一个自然的扩展是矩阵分解模型 C_{mi}（低秩但非 rank-1），但这会显著增加参数量并可能破坏 Theorem 1 的可辨识性条件。论文应至少在 Limitations 中讨论 rank-1 假设的局限性，并说明放松该假设对可辨识性的影响。\n\n### [AGREE] R2-W3: CI coverage 71% 实际影响未充分讨论\n\n同意，但需纠正 R2 的术语：71% 的 empirical coverage（nominal 95%）是 **undercoverage**（CI 过窄、过度自信），不是\"overcoverage\"。这与我自己的 N1 一致——这是我审稿意见中最严重的问题之一。补充观察：Figure 5 的 coverage 数据来自合成数据（N = 50, I = 100），真实数据（N = 8）下的 coverage 可能更差，因为 Murphy-Topel 校正的渐近近似在更小样本下更不可靠。论文需要提供操作化建议：如果 CI 不可靠，用户应如何解读 Table 6 中的 c_m 估计？建议至少报告 point estimate 的 sign 和 magnitude 的稳健性（如通过 leave-one-judge-out），而非依赖 CI。\n\n### [REBUT] R2-W4: Self-judging bias 未充分整合\n\n部分不同意。论文在 Appendix G（Section G: Contamination Susceptibility Recovery）中专门分析了 self-evaluation robustness：Qwen2.5-72B 的 self-judging win rate 为 1,000/1,424（vs cross-judge 0.714），LLaMA-3.3-70B 为 0.952（vs 0.714）。论文的处理策略是 empirical validation 而非 structural modeling——通过排除 self-judging pairs 后展示排名不变来论证 robustness。\n\n从方法论角度，将 self-judging bias 显式建模为 G-MFRM 的一个额外 facet（如 s_{nj} indicator when model n = judge j）会增加一组 N×J 的交互参数，在 N = 8, J = 9 的情况下参数量激增（至多 72 个额外参数），导致严重的过拟合风险和可辨识性问题。当前的 empirical robustness check 是合理的实用策略。\n\n但我同意论文应在正文（而非仅 Appendix）中更显著地讨论 self-judging bias 的处理及其局限性，因为这是 LLM-as-a-judge 文献中的已知核心问题。\n",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-23T06:26:53.369768+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4171
}
```

</details>

---


### Assistant

_source line 400 · 2026-05-23T06:27:04.745975+00:00_

已提交对 Reviewer 2 的逐条回应。总结：

- **N1 (单一 benchmark)**: [AGREE] — 与我自己的 N2 一致，N=8 underpowered，论文自己算出需要 N≥17
- **N2 (OVB 定位过高)**: [REBUT] — 问题识别本身有价值，OVB→gating mechanism 的 "诊断→建模" 链路非平凡，但措辞可更精确
- **N3 (vs DG-IRT 增量新颖性)**: [REBUT] — 可辨识性分析（Propositions 1-2, Theorem 1）和 error propagation 框架（Murphy-Topel）是 DG-IRT 所没有的方法论贡献，非仅工程扩展
- **W1 (Stage 2 ad hoc)**: [AGREE] — 与我自己的 W2 一致
- **W2 (rank-1 假设)**: [AGREE] — 补充了放松假设对可辨识性的影响分析
- **W3 (CI coverage)**: [AGREE] — 纠正了 R2 的术语（是 undercoverage 非 overcoverage），与我自己的 N1 一致
- **W4 (self-judging bias)**: [REBUT] — Appendix G 的 empirical robustness check 是合理策略，显式建模会导致 N=8 下过拟合

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 15

## Round 15

66 recorded events


### User

_source line 401 · 2026-05-23T12:00:23.730135+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。

## Venue 信息
- **目标**: EMNLP 2026 (via ACL Rolling Review)
- **截止日期**: 2026-05-25 (AoE)
- **格式**: Long paper, 8 页正文限制 + unlimited references + mandatory Limitations section (不计页数)
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **审稿方式**: Double-blind
- **匿名规则**: 无匿名期要求，但论文必须匿名化
- **Appendix**: 双栏格式，reviewer 无义务阅读但可参考

## 论文文件
- 主文件: `docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/submitted.pdf`

## 你的审查侧重

### 1. 数学和理论严谨性
- Observation 1 (OVB): 线性近似从 OVB 迁移到 nonlinear MFRM 是否严谨？r=0.86 的 simulation validation 是否充分？
- Proposition 1-2 和 Theorem 1: 证明是否完整、逻辑是否正确？条件是否充分必要？
- Error propagation (§3.4): σ_crit 推导的 i.i.d. Gaussian 假设是否合理？attenuation factor 的推导是否正确？
- Murphy-Topel variance correction (Appendix): 推导是否正确？N=8 下渐近方法是否适用？

### 2. 实验设计与统计声明
- 主结果 (Table 1): Δτ=+0.071 不显著（bootstrap CI 跨零）——论文如何处理这一点？声明是否诚实？
- 7 个 baselines 产生完全相同排名——是否可信？论文解释是否充分？
- LOO-CV (ΔELPD=-55.7): 用于支持什么结论？是否存在 model fit ≠ ranking accuracy 的逻辑跳跃？
- Synthetic experiments: N=50 vs N=8 的外推是否合理？
- MCMC 收敛: R̂≤1.03, ESS=174 是否满足要求？引用与阈值是否一致？
- CI coverage 71%: 论文承认但仍报告 CI——是否误导？

### 3. 可复现性
- 代码/数据可用性
- 实验细节是否充分
- MCMC 配置是否完整

请按 ARR 标准输出完整审稿报告，包含：Summary, Strengths, Weaknesses (Must-Fix / Should-Fix / Minor), Questions, Missing References, Overall Assessment (1-5 scale per EMNLP 2026), Confidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-23T12:00:37.988974+00:00_

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
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
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

_source line 403 · 2026-05-23T12:00:38.039510+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-23T12:00:43.068165+00:00_

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
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 405 · 2026-05-23T12:00:43.872623+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR reviewer form soundness excitement reproducibility scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR reviewer form soundness excitement reproducibility scoring"
  }
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-23T12:00:45.851779+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/submitted.pdf",
  "project": "gated_mfrm_judge_bias",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/submitted.pdf",
    "project": "gated_mfrm_judge_bias",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-23T12:00:50.493434+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found comprehensive information about ACL Rolling Review 2026. Here are the key findings:

## Reviewer Guidelines

Reviewers are asked to: (1) read the paper and get the first impression, (2) search for related work, and if qualified to review only some aspects, state in the review which major parts were not checked. Additionally, reviewers should check for academic conflicts of interest and recuse themselves if the submission is very close to their own work about to be submitted.

## Review Form Criteria

The review form incl
…[truncated 1056 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7425
}
```

</details>

---


### Tool result

_source line 408 · 2026-05-23T12:00:51.202756+00:00_

Web search results for query: "EMNLP 2026 ARR reviewer form soundness excitement reproducibility scoring"

Links: [{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Thank you to our 2025 reviewers","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12921489/"},{"title":"ConfReady: A RAG based Assistant and Dataset for Conference Checklist Responses","url":"https://arxiv.org/pdf/2408.04675"}]

Based on the search results, here's information about the ARR reviewer form scoring system that applies to EMNLP 2026:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

**Soundness Score:**
The soundness scores must be justified by the text of the review. If you give a low soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it. Low reproducibility scores should be justified.

**Excitement Score:**
Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

**Overall Recommendation Score:**
The Overall assessment score is an e
…[truncated 540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7330
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-23T12:00:53.116071+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 552.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.1}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-prod4
…[truncated 372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7264
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-23T12:01:00.280509+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with ALL scoring dimensions, their scales (1-5 etc.), and descriptions for each score level. Include: soundness, excitement/novelty, overall assessment, confidence, reproducibility, and any other dimensions. List every score option with its exact description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with ALL scoring dimensions, their scales (1-5 etc.), and descriptions for each score level. Include: soundness, excitement/novelty, overall assessment, confidence, reproducibility, and any other dimensions. List every score option with its exact description."
  }
}
```

</details>

---


### Tool call

_source line 411 · 2026-05-23T12:01:01.386624+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-23T12:01:01.691106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 413 · 2026-05-23T12:01:02.293936+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 414 · 2026-05-23T12:01:02.802872+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1416
}
```

</details>

---


### Tool call

_source line 415 · 2026-05-23T12:01:02.803321+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 416 · 2026-05-23T12:01:03.159484+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1468
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-23T12:01:03.764283+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1470
}
```

</details>

---


### Tool result

_source line 418 · 2026-05-23T12:01:03.966333+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1163
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-23T12:01:06.930625+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. Reviewer Confidence
Scale: 1-5
- **5:** "Positive that my evaluation is correct. I read the paper very carefully..."
- **4:** "Quite sure. I tried to check the important points carefully..."
- **3:** "Pretty sure, but there's a chance I missed something..."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details..."
- **1:** "Not my area, or paper is very hard to understand..."

## 2. Soundness
Scale: 1-5 (with .5 increments)
- **5:** "Excellent: This study is one of the most thorough I have seen..."
- **4:** "Strong: This study provides sufficient support for all claims..."
- **3:** "Acceptable: This study provides sufficient support for main claims..."
- **2:** "Poor: Some main claims are not sufficiently supported..."
- **1:** "Major Issues: This study is not yet sufficiently thorough..."

## 3. Excitement
Scale: 1-5 (with .5 increments)
- **5:** "Highly Exciting: I would recommend this paper to others..."
- **4:** "Exciting: I would mention this paper to others..."
- **3:** "Interesting: I might mention some points..."
- **2:** "Potentially Interesting: does not resonate with me..."
- **1:** "Not Exciting: does not resonate with me..."

## 4. Overall Assessment
Scale: 1-5 (with .5 increments)
- **5:** Consider for Award (top 2.5%)
- **4:** Conference acceptance
- **3:** Findings acceptance
- **2:** Resubmit next cycle
- **1:** Do not resubmit

## 5. Reproducibility
Scale: 1-5
- **5:** Results easily reproducible
- **4:** Mostly reproducible with minor variations
- **3:** Reproducible with difficulty; underspecified parameters
- **2:** Hard to reproduce; unavailable data
- **1:** Cannot reproduce

## 6. Datasets & Software
Each scored 1-5:
- **5:** Enabling for research directions
- **4:** Useful for ongoing work
- **3:** Potentially useful
- **2:** Documentary value only
- **1:** None released

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6650
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-23T12:01:14.279600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 421 · 2026-05-23T12:01:14.481649+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-23T12:01:14.482100+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 423 · 2026-05-23T12:01:14.482356+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 424 · 2026-05-23T12:01:16.854500+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2574
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-23T12:01:18.679377+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4197
}
```

</details>

---


### Tool result

_source line 426 · 2026-05-23T12:01:18.680902+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4198
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-23T12:01:18.682100+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4199
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-23T12:01:25.347482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 429 · 2026-05-23T12:01:26.461613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 430 · 2026-05-23T12:01:27.118282+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1770
}
```

</details>

---


### Tool call

_source line 431 · 2026-05-23T12:01:27.471457+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/submitted.pdf",
  "project": "gated_mfrm_judge_bias",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/submitted.pdf",
    "project": "gated_mfrm_judge_bias",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 432 · 2026-05-23T12:01:27.876137+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1414
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-23T12:01:29.142138+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 438.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 410.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 424.4}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.7}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 295.6}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1670
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-23T12:01:31.909670+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-23T12:01:35.023592+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3113
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-23T12:01:35.174487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-23T12:01:37.032042+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1857
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-23T12:01:37.183591+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 439 · 2026-05-23T12:01:37.237653+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-23T12:01:37.238073+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 441 · 2026-05-23T12:01:37.238325+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 442 · 2026-05-23T12:01:38.720506+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1482
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-23T12:01:39.675858+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2438
}
```

</details>

---


### Tool result

_source line 444 · 2026-05-23T12:01:39.676922+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2493
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-23T12:01:39.677886+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2439
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-23T12:04:20.243645+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-23T12:04:20.294400+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{amsthm}
14	\usepackage{booktabs}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	
18	\newtheorem{observation}{Observation}
19	\newtheorem{proposition}{Proposition}
20	\newtheorem{theorem}{Theorem}
21	\newtheorem{corollary}{Corollary}
22	
23	\graphicspath{{../../figures/paper/}}
24	
25	\title{Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model\\for Disentangling Judge Bias and Contamination in LLM Evaluation}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	\input{introduction}
34	\input{background}
35	\input{method}
36	\input{experiments}
37	\input{related_work}
38	\input{conclusion}
39	
40	\section*{Limitations}
41	\input{limitations}
42	
43	\bibliography{references}
44	
45	\appendix
46	\input{appendix}
47	
48	\end{document}
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-23T12:04:23.077608+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/",
  "description": "List paper source files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/",
    "description": "List paper source files"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-23T12:04:23.228729+00:00_

_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
appendix.tex
background.tex
conclusion.tex
experiments.tex
figures
introduction.tex
limitations.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
method.tex
references.bib
related_work.tex
sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-23T12:04:25.688640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-23T12:04:25.889819+00:00_

1	\section{The G-MFRM Framework}
2	\label{sec:method}
3	
4	Section~\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and a hierarchical HalfNormal prior for the contamination term, are motivated by the identifiability analysis in \S\ref{sec:identifiability} and the error propagation bounds in \S\ref{sec:error_prop}.
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{fig1_framework}
9	\caption{Overview of the G-MFRM three-stage calibration procedure. Stage~1 fits a standard MFRM to obtain initial estimates $(\hat{\theta}, \hat{b}, \hat{d})$. Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring and cross-model agreement). Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\tilde{\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}
10	\label{fig:framework}
11	\end{figure}
12	
13	\subsection{Model Specification}
14	\label{sec:model_spec}
15	
16	G-MFRM extends the standard MFRM \citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\ref{eq:mfrm}):
17	%
18	\begin{equation}
19	\label{eq:gmfrm}
20	\log \frac{P(Y_{nij} \geq k)}{P(Y_{nij} < k)} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i,
21	\end{equation}
22	%
23	where all terms carry the definitions from Section~\ref{sec:confounding}. The gating structure $c_n \cdot e_i$ separates the model-specific and item-specific components of contamination: $c_n \geq 0$ captures how much model $n$ benefits from memorized benchmark content, while $e_i \in [0,1]$ quantifies
…[truncated 10829 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-23T12:04:25.890212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-23T12:04:25.990818+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	\label{sec:setup}
6	
7	\paragraph{Data and models.} We evaluate on Arena-Hard \citep{li2024arenahard}, a benchmark of 316 multi-turn conversational items selected for high separability among frontier models. After filtering for full coverage across all judges and target models, the evaluation set comprises 176 items in a connected incomplete design (5{,}661 observations; 44.7\% fill rate of the full $N \times I \times J$ tensor). Eight target models spanning proprietary and open-source families are evaluated (Table~\ref{tab:main_results}). Ground-truth rankings are derived from Chatbot Arena human preference data \citep{zheng2023mtbench}.
8	
9	\paragraph{Judges.} Nine LLM judges score all model responses in position-swapped pairwise mode: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini-2.5-Pro, Mistral-Large-2, LLaMA-3.3-70B, Qwen2.5-72B, and Qwen3-235B. Position swapping controls for position bias and doubles the effective observation count. Two models---Qwen2.5-72B and LLaMA-3.3-70B---serve as both judge and target; $d_j$ absorbs systematic self-evaluation bias, and excluding self-judging observations leaves rankings unchanged ($\tau = 0.857$; Appendix~\ref{app:self_eval}).
10	
11	\paragraph{Exposure estimation.} Per-item exposure $e_i$ is estimated via a two-source pipeline (\S\ref{sec:staged}): reference model anchoring with gpt-4-0314 as anchor (75\% weight) and cross-model agreement (25\% weight). The pipeline is robust to weight configuration (Spearman $\rho \geq 0.998$ across all configurations tested).
12	
13	\paragraph{MCMC.} We use NumPyro NUTS with 4{,}000 warmup and 4{,}000 sampling iterations across 4 chains (target acceptance 0.95). The contamination prior follows the hierarchical HalfNormal specification (Eq.~\ref{eq:contam_prior}). Convergence is assessed via rank-normalized split-$\hat{R}$ \citep{vehtari2021rhat} with conventional $\hat{R} < 1.05$ and E
…[truncated 8750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-23T12:04:33.721626+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-23T12:04:33.722029+00:00_

1	\section{Confounding in LLM Evaluation}
2	\label{sec:confounding}
3	
4	The Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies
5	%
6	\begin{equation}
7	\label{eq:mfrm}
8	\log \frac{P(Y_{nij} \geq k \mid \theta_n, b_i, d_j, \tau_k)}{P(Y_{nij} < k \mid \theta_n, b_i, d_j, \tau_k)} = \theta_n - b_i - d_j - \tau_k,
9	\end{equation}
10	%
11	where $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\theta_n$ is the ability of model $n$ ($n = 1, \ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \ldots, J$), and $\tau_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for item difficulty and judge severity. \citet{jiao2025mfrm_llm} applied this framework to compare ten LLM raters with human experts, showing that MFRM separates genuine ability from systematic judge effects in multi-judge panels.
12	
13	However, standard MFRM assumes that all systematic sources of score variation are captured by the modeled facets. This assumption breaks down when some models have been exposed to benchmark items during training \citep{dcr2025}. Such contamination inflates scores on exposed items through memorization rather than genuine ability. We represent this effect as an interaction $c_n \cdot e_i$, where $c_n \geq 0$ is the contamination susceptibility of model $n$ and $e_i \in [0, 1]$ is the exposure level of item $i$. The complete data-generating process becomes
14	%
15	\begin{equation}
16	\label{eq:full}
17	\eta_{nijk} = \theta_n - b_i - d_j - \tau_k 
…[truncated 3907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-23T12:04:33.922953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-23T12:04:33.973556+00:00_

1	We identify six limitations. First, although Theorem~\ref{thm:sufficient} requires only a connected design, the current evaluation achieves 44.7\% fill rate (5{,}661 of 12{,}672 potential cells); sparser designs may compromise identifiability of $c_n$ for models with few observed exposed items. Relatedly, sparse observations per item produce elevated item-level mean-square residuals (92/176 items), though model- and judge-level fit remains acceptable. Second, Stage~2 exposure estimation relies on a reference model anchor (gpt-4-0314), and exposure estimate quality depends on the anchor remaining uncontaminated relative to the benchmark; as benchmarks age, anchor validity should be periodically re-assessed. Third, the current evaluation uses a single benchmark (Arena-Hard) with eight target models; post-hoc power analysis indicates that detecting $\Delta\tau = 0.071$ at $\alpha = 0.05$ requires $N \approx 17$ models for 80\% power, while $N = 8$ yields approximately 50\% power, explaining the non-significant bootstrap result. Generalization to other benchmarks and larger model populations remains to be verified. Fourth, empirical CI coverage differs by parameter type: ability estimates $\theta$ approach nominal coverage at moderate sample sizes (${\sim}$90\% at $N = 8$), while contamination susceptibility $c_n$ exhibits moderate posterior overconfidence (71\% at $N = 50$, 68\% at $N = 8$; \citealp{talts2018sbc}). The $c_n$ under-coverage reflects the multiplicative coupling $c_n \cdot e_i$ and the HalfNormal prior's boundary constraint at $c_n = 0$, which systematically narrows posterior credible intervals. Point estimates and rank orderings ($\tau = 0.857$) are unaffected; $c_n$ estimates are best interpreted as directional diagnostics rather than calibrated intervals. Fifth, while self-evaluation sensitivity analysis (Appendix~\ref{app:self_eval}) confirms robust rankings when excluding self-judging observations, a more comprehensive analysis removing overlapping
…[truncated 483 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-23T12:04:34.325503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-23T12:04:34.627550+00:00_

1	\section{Proof of Theorem~\ref{thm:sufficient}}
2	\label{app:proof}
3	
4	We prove that the G-MFRM is locally identifiable under the conditions of Theorem~\ref{thm:sufficient}. Following \citet{rothenberg1971}, a parametric model is locally identifiable at the true parameter vector $\boldsymbol{\psi}_0$ if and only if the Fisher information matrix $\mathbf{F}(\boldsymbol{\psi}_0)$ is non-singular.
5	
6	\paragraph{Setup.} The G-MFRM parameter vector is $\boldsymbol{\psi} = (\boldsymbol{\theta}, \mathbf{c}, \mathbf{b}, \mathbf{d}, \boldsymbol{\tau})$, where $\boldsymbol{\theta} \in \mathbb{R}^{N-1}$ (after the location constraint $\sum_n \theta_n = 0$), $\mathbf{c} \in \mathbb{R}_{\geq 0}^N$, $\mathbf{b} \in \mathbb{R}^I$, $\mathbf{d} \in \mathbb{R}^J$, and $\boldsymbol{\tau} \in \mathbb{R}^{K-1}$. The exposure vector $\mathbf{e} = (e_1, \ldots, e_I)$ is fixed externally and treated as known. The linear predictor is $\eta_{nijk} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i$, with partial derivatives:
7	%
8	\begin{align*}
9	\frac{\partial \eta_{nijk}}{\partial \theta_n} &= 1, \quad
10	\frac{\partial \eta_{nijk}}{\partial c_n} = e_i, \quad
11	\frac{\partial \eta_{nijk}}{\partial b_i} = -1, \\
12	\frac{\partial \eta_{nijk}}{\partial d_j} &= -1, \quad
13	\frac{\partial \eta_{nijk}}{\partial \tau_k} = -1.
14	\end{align*}
15	
16	\paragraph{Fisher information weights.} For each observation cell $(n,i,j)$, the Fisher information weight under the cumulative logit model is
17	%
18	\begin{equation}
19	\label{eq:fisher_weight}
20	w_{nij} = \sum_{k=1}^{K} \frac{\bigl[\sigma'(\eta_{nijk}) - \sigma'(\eta_{nij,k+1})\bigr]^2}{P(Y_{nij} = k)},
21	\end{equation}
22	%
23	where $\sigma(x) = (1 + e^{-x})^{-1}$, $\sigma'(x) = \sigma(x)(1 - \sigma(x))$, and we set $\sigma'(\eta_{nij,0}) = \sigma'(\eta_{nij,K+1}) = 0$ at the boundaries. Since $P(Y_{nij} = k) > 0$ for all categories and $\sigma'(\cdot) > 0$, we have $w_{nij} > 0$ for all $(n,i,j)$.
24	
25	\paragraph{Step 1: The $(\theta_n,
…[truncated 28863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-23T12:07:48.378751+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告\n\n**论文**: Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**审查侧重**: 方法严谨性 + 实验有效性\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n**一句话总结**: 理论框架严谨且有原创性（OVB 形式化、可识别性证明、误差传播分析），但核心实证结果（N=8, Δτ=+0.071）统计不显著，且 contamination susceptibility 的 CI coverage 仅 68-71%，实际效用在当前评测规模下尚未得到充分验证。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 理论推导完整正确（Propositions 1-2, Theorem 1），但 N=8 下主结果不显著，c_n 的 95% CI 实际 coverage 仅 68-71%，Murphy-Topel 渐近校正在 N=8 下可靠性存疑 |\n| Excitement | 3.5/5 | 将 OVB 框架引入 LLM evaluation contamination 是新颖且重要的贡献，将教育测量学 (IRT) 和 NLP 评测有效连接；但实际排名改善不显著，限制了当前实用价值 |\n| Reproducibility | 3/5 | MCMC 配置完整（4 chains, 4000 warmup, 4000 sampling, NumPyro NUTS），先验设定明确；但代码未公开（承诺 acceptance 后发布），Stage 2 exposure pipeline 的具体预处理步骤（如 316→176 items 的过滤标准）不够详细 |\n| Confidence | 4/5 | 仔细核查了数学推导（Fisher information, Cauchy-Schwarz, Schur complement, Murphy-Topel），通读了全部 16 页含附录 |\n\n---\n\n## Summary\n\n本文提出 G-MFRM（Gated Many-Facet Rasch Model），在标准 MFRM 的线性预测器中引入乘性 contamination gating 项 c_n · e_i，将模型能力、judge severity 和 contamination susceptibility 纳入统一框架联合估计。论文的核心 insight 是：忽略 contamination 项会产生 omitted variable bias (OVB)，使受污染模型的能力被高估。论文提供了完整的可识别性分析（Propositions 1-2, Theorem 1），error propagation bounds（§3.4），以及 Murphy-Topel 方差校正（Appendix C）。在合成数据（N=50）上，G-MFRM 将 θ-RMSE 降低 51.2%；在 Arena-Hard 实际数据（N=8）上，排名相关性从 τ=0.786 提高到 0.857，但统计不显著（bootstrap CI 跨零）。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Contamination susceptibility c_n 的 95% CI coverage 仅 68-71%，严重偏离 95% 名义水平\n- 具体位置：Limitations 第 4 点；Appendix Q；Table 7 caption (\"empirical coverage ~71%\")\n- 问题：在 N=8 时 c_n coverage 为 67.9%，N=50 时也仅 71%（Appendix Q）。这意味着论文报告的 c_n 置信区间系统性过窄，约 1/3 的情况下真值落在区间外。论文在 Table 7 caption 中标注了 \"empirical coverage ~71%\"，在 Limitations 中也有提及，但问题是：(1) coverage 从 N=8 到 N=50 几乎没有改善（68%→71%），说明这不是小样本问题，而是模型结构性缺陷（乘性耦合 + HalfNormal 边界约束）；(2) 论文仍然在主表中报告了具体的 c_n 95% CI 值（如 GPT-3.5-Turbo: [4.40, 6.80]），可能误导读者认为这些区间是校准的。\n- 为什么影响接收：如果 uncertainty quantification 不可靠，那么基于 c_n 的诊断功能（论文声称的主要实用价值之一）就缺乏量化基础。论文虽然诚实地报告了这一问题，但没有提出解决方案或讨论根本原因是否可修复。\n- 建议修改方向：(1) 在 Table 7 中明确标注 \"coverage-uncalibrated\" 而非简单脚注；(2) 探索 simulation-based calibration (SBC; Talts et al., 2018) 的校正方法；(3) 讨论 coverage 不随 N 改善是否暗示模型 misspecification（如 rank-1 假设过强）；(4) 考虑 posterior predictive p-values 作为替代诊断。\n\n**N2** [critical] N=8 下主结果统计不显著，且 power analysis 显示需要 N≥17 才有 80% power\n- 具体位置：§4.2 \"ranking improvement is not statistically significant at N = 8\"；Appendix M (Power Analysis)\n- 问题：Δτ = +0.071 的 bootstrap 95% CI 为 [-0.071, 0.071]，完全对称于零。这并非巧合——Kendall τ 在 N=8 时的最小非零增量恰好是 2/C(8,2) ≈ 0.071，因此 CI 的宽度恰好等于一个 concordant pair swap。这意味着在 N=8 的离散分辨率下，该方法的改善根本无法被检测到。Power analysis 显示 N=8 仅有 ~50% power（Appendix M），而 80% power 需要 N≈17。论文诚实报告了这些，但问题是：如果当前规模下无法统计验证方法的核心声明（ranking improvement），那么 Arena-Hard 实验的证据力大打折扣。\n- 为什么影响接收：一篇声称改善 ranking accuracy 的论文，其主要实验无法在统计上支持这一声明。虽然合成实验（N=50）显示显著改善，但 real-data 验证是必需的。\n- 建议修改方向：(1) 扩展到至少一个更大规模的评测（N≥17），如 LMSYS Chatbot Arena 完整排名或 AlpacaEval 2.0；(2) 如果无法获得更多模型，考虑使用 per-item 预测精度（而非 rank correlation）作为辅助指标，因为 LOO-CV (ΔELPD = -55.7, |Δ/SE| = 5.9) 已经显示了显著的 predictive fit 改善；(3) 明确将论文定位为\"理论 + 诊断贡献\"而非\"ranking improvement\"。\n\n**N3** [critical] Murphy-Topel 渐近校正在 N=8 下的适用性存疑\n- 具体位置：§3.4; Appendix C (Eq. 16: V_MT = V_3 + V_3 C V_2 C^T V_3)\n- 问题：Murphy-Topel (1985) 的方差校正基于大样本渐近理论。在本文中，\"样本量\"对应目标模型数 N=8。这远低于渐近方法通常需要的样本量（经验法则 N≥30）。论文用 bootstrap 估计 V_2 并用有限差分计算 cross-derivative C，这在小样本下可能产生不稳定的估计。c_n 的 CI coverage 仅 68-71% 可能部分归因于 Murphy-Topel 校正的不充分。\n- 为什么影响接收：Murphy-Topel 校正是论文声称的方法论贡献之一（\"neither of which exists for DG-IRT or any prior gated measurement model\"，§3.1）。如果该校正在 paper 自身的评测规模下不工作，这削弱了贡献的实用价值。\n- 建议修改方向：(1) 用 simulation 验证 Murphy-Topel 校正在不同 N 下的 coverage 改善（相对于无校正的 naive posterior），报告 coverage with vs without 校正的对比；(2) 讨论小样本下的替代方案（如 parametric bootstrap 或 double bootstrap）；(3) 如果校正效果微弱，诚实报告。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 7 个 baseline 产生完全相同的排名，使对比缺乏信息量\n- 具体位置：Table 1; §4.2 第 1 段\n- 问题：所有 7 个 baseline（Raw Average, MFRM-only, Sequential, CyclicJudge, CyclicJudge+discard, DCR Factor, Pref. Leakage）产生完全相同的 τ=0.786, ρ=0.905。论文解释为\"ability scores also vary by < 0.03 logits across methods\"（§4.2），但这实际上意味着所有现有方法在当前数据上的行为几乎一致——即 baseline space 完全退化。这使得 G-MFRM 的比较对象实质上只是 \"raw average\"，而不是 7 种不同的校准方法。\n- 建议：(1) 报告 per-model ability estimates 的 pairwise 差异（如 max |θ_baseline_i - θ_baseline_j|），验证 baseline 间确实几乎无差异；(2) 讨论这一现象是 N=8 的 artifact 还是反映了更深层的问题（如所有方法在大规模数据上是否也会趋同）。\n\n**W2** [warning] Rank-1 contamination 结构假设过强\n- 具体位置：§3.1 (Eq. 4); Limitations 第 6 点\n- 问题：c_n · e_i 是一个 rank-1 分解，假设所有模型通过同一 item-level exposure pattern 受污染，仅在 magnitude 上不同。实际上，不同模型可能对不同领域的 items 有不同程度的 memorization（如 coding vs. reasoning）。论文在 Limitations 中提到了 higher-rank decomposition Σ_r c_{nr} · e_{ir}，但没有讨论当 rank-1 假设被违反时 G-MFRM 的行为（是 graceful degradation 还是 systematic bias）。\n- 建议：在合成实验中加入 rank-2 或 domain-specific contamination 的 misspecification 测试，报告 G-MFRM 在 rank-1 假设被违反时的性能退化程度。\n\n**W3** [warning] LOO-CV (ΔELPD) 和 ranking accuracy 之间存在逻辑跳跃\n- 具体位置：§4.2 第 3 段 (\"LOO cross-validation strongly favors G-MFRM\")\n- 问题：ΔELPD_LOO = -55.7 (|Δ/SE| = 5.9) 证明 G-MFRM 有更好的 predictive fit for held-out responses。但论文在同一段中将此与 ranking improvement 并列讨论，给读者造成 \"model fit improvement → ranking improvement\" 的印象。然而 Table 1 已经表明 ranking improvement 不显著。Better model fit 不等于 better ranking——一个模型可以更好地拟合 response patterns 但对 aggregate rankings 没有影响（甚至可能拟合了噪声而非信号）。\n- 建议：明确区分两条 evidence line：(1) LOO-CV 支持 contamination term 的建模必要性（model fit），(2) ranking improvement 在当前 N 下不显著（practical utility）。不要在同一段中混合这两个论点。\n\n**W4** [warning] MCMC 收敛诊断未达到 Vehtari et al. (2021) 推荐标准\n- 具体位置：§4.2 倒数第 2 段 (\"R̂ ≤ 1.03...minimum bulk ESS of 174\")\n- 问题：论文使用 R̂ < 1.05 和 ESS > 100 的阈值，引用 Gelman et al. (2013)。但论文同时引用的 Vehtari et al. (2021) 推荐 R̂ < 1.01 和 ESS_bulk > 400。实际达到的 R̂ ≤ 1.03 和 ESS_min = 174 在两个标准之间。论文诚实地承认\"do not meet the stricter criteria\"并将此与 CI coverage 问题联系，这是好的。但 ESS = 174 意味着有效样本量较低，posterior summaries 可能有非平凡的 MCMC 误差。\n- 建议：(1) 报告 ESS_tail（不仅是 ESS_bulk），因为 HalfNormal 先验下 c_n 的 tail behavior 对 CI coverage 很重要；(2) 考虑增加 sampling iterations（如 8000 或 16000）以改善 ESS；(3) 量化 MCMC 误差对 τ 点估计的影响（如跨 chain 的 τ 变异性）。\n\n**W5** [warning] OVB 线性近似 r=0.86 的 gap 未充分讨论\n- 具体位置：§2 (Observation 1 footnote); Figure 1\n- 问题：Observation 1 依赖线性近似将 OVB 从线性模型迁移到非线性 MFRM。Synthetic validation 显示 Pearson r=0.86 (p<0.001)，解释约 74% 的方差。论文在脚注中承认这是\"approximation\"，但正文中将其作为核心理论动机使用（\"this confounding undermines both sequential estimation strategies\"）。r=0.86 意味着 26% 的 bias variance 未被线性近似捕获——这部分可能来自非线性效应、交互项、或极端 c_n·e_i 值。\n- 建议：(1) 在 Figure 1 中可视化残差的分布（r=0.86 的 scatter 之外），检查是否有系统性偏差；(2) 讨论在什么 c_n·e_i 量级下线性近似开始失效；(3) 强调实际模型（G-MFRM）不依赖此近似（仅用于动机论证）。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Abstract**: \"joint estimation achieves 0.124 ± 0.016, a 51.2% reduction\" 是合成数据结果（N=50），但 Abstract 中先出现的 \"τ = 0.857 vs. 0.786\" 是实际数据（N=8）。两者的 N 不同但并列呈现，可能造成混淆。建议更明确地分隔。\n\n2. **§4.1 \"316 multi-turn conversational items\"**: 经过过滤后仅剩 176 items（44.7% fill rate）。过滤标准（\"filtering for full coverage across all judges and target models\"）应更详细说明——是要求每个 item 被所有 9 个 judge 评分过，还是被至少 k 个 judge 评分过？\n\n3. **Table 7** (Appendix N): c_n 的 95% CI 宽度较大（如 Qwen3-8B: [0.14, 2.50]），跨越了近 2 个数量级。在 coverage 仅 71% 的情况下报告这样宽的\"95% CI\"的实际诊断价值有限。\n\n4. **Self-evaluation** (Appendix I): Qwen2.5-72B 自评 win rate = 1.000 (42/42)，这个完美自评率值得在正文中提及，因为它是 judge bias 的一个极端案例。\n\n5. **§3.2 Stage 2**: reference model anchor 使用 gpt-4-0314。如果该锚模型本身对 Arena-Hard items 有 contamination（尽管 2023 年的模型较早），exposure 估计会系统性偏低。论文在 Limitations 第 2 点提及但未量化风险。\n\n---\n\n## 主要优势\n\n1. **理论贡献扎实**: 将 benchmark contamination 形式化为 MFRM 中的 OVB 是一个新颖且有说服力的框架。Observation 1 清晰地解释了为什么 sequential estimation（先去 bias 或先去 contamination）都不能解决问题——这是本文最核心的 insight。\n\n2. **可识别性分析完整**: Propositions 1-2 给出了必要条件（exposure variation），Theorem 1 给出了充分条件（connected design + exposure variation）。Appendix A 的证明通过 Fisher information matrix 的 Cauchy-Schwarz 分解和 Schur complement 论证，技术上正确且完整。这是首次为 gated IRT 模型建立形式化的可识别性条件。\n\n3. **诚实透明的报告**: 论文明确承认主结果不显著（Δτ CI 跨零），CI coverage 不理想（68-71%），MCMC 未达到最严格标准。这种诚实性在学术论文中值得赞赏，使读者能准确评估证据强度。\n\n4. **合成实验设计周密**: 覆盖了 error propagation（Table 2）、ablation（Table 3）、matched-scale calibration（Appendix P）、power analysis（Appendix M）、CI coverage（Appendix Q）。特别是 matched-scale 合成实验（N=8, I=176, J=9）精确匹配了实际评测配置，Δτ_synthetic = +0.072 与 Δτ_real = +0.071 高度一致。\n\n5. **诊断输出有实用价值**: per-model c_n、per-judge d_j 的估计提供了可操作的诊断信息（如识别哪些模型可能受污染、哪些 judge 偏严/偏松），即使 ranking improvement 本身不显著。Table 8 (Bias Absorption) 中 Δθ 与 c_n 的完美秩相关 (Spearman ρ=1.0) 是 OVB 理论预测的有力实证确认。\n\n---\n\n## Questions for Authors\n\n1. Murphy-Topel 校正相对于 naive posterior 提供了多少 coverage 改善？能否报告 coverage with vs without Murphy-Topel 的对比？\n\n2. 在 real data 中，Var(e_i) 的实际值是多少？这决定了 σ_crit 的具体阈值，对实际应用中判断 Stage 2 估计质量至关重要。\n\n3. 如果将 rank-1 假设放松为 rank-2（如 coding/reasoning 两个维度），可识别性条件如何变化？Theorem 1 是否可以推广？\n\n4. 7 个 baseline 在更大 N 下（如 Chatbot Arena 全部 ~50 个模型）是否仍然产生相同排名？\n\n---\n\n## Missing References\n\n- Ye et al. (2024), \"Benchmarking Benchmark Leakage in Large Language Models\" — 与本文的 contamination detection 高度相关，讨论了多种 leakage detection 方法\n- Oren et al. (2024), \"Proving Test Set Contamination in Black Box Language Models\" — 提出了统计检验方法来检测 contamination，可与本文的 c_n 估计方法做方法论对比\n\n---\n\n## Overall Assessment\n\n**3.5 / 5 — Borderline Conference**\n\n本文的理论框架（OVB 形式化 + 可识别性证明 + 误差传播分析）是扎实且原创的方法论贡献，将教育测量学的经典工具适配到 LLM 评测的新场景。然而，核心实证结果在 N=8 下不显著，c_n 的 CI coverage 问题（68-71%）暗示模型可能存在结构性缺陷（而非仅仅是小样本问题），Murphy-Topel 校正在小样本下的可靠性未得到验证。如果作者能在更大规模上验证（N≥17）或充分 address CI coverage 问题，论文将是强 conference paper。当前状态适合 Findings 或 borderline conference。",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告\n\n**论文**: Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**审查侧重**: 方法严谨性 + 实验有效性\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n**一句话总结**: 理论框架严谨且有原创性（OVB 形式化、可识别性证明、误差传播分析），但核心实证结果（N=8, Δτ=+0.071）统计不显著，且 contamination susceptibility 的 CI coverage 仅 68-71%，实际效用在当前评测规模下尚未得到充分验证。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 理论推导完整正确（Propositions 1-2, Theorem 1），但 N=8 下主结果不显著，c_n 的 95% CI 实际 coverage 仅 68-71%，Murphy-Topel 渐近校正在 N=8 下可靠性存疑 |\n| Excitement | 3.5/5 | 将 OVB 框架引入 LLM evaluation contamination 是新颖且重要的贡献，将教育测量学 (IRT) 和 NLP 评测有效连接；但实际排名改善不显著，限制了当前实用价值 |\n| Reproducibility | 3/5 | MCMC 配置完整（4 chains, 4000 warmup, 4000 sampling, NumPyro NUTS），先验设定明确；但代码未公开（承诺 acceptance 后发布），Stage 2 exposure pipeline 的具体预处理步骤（如 316→176 items 的过滤标准）不够详细 |\n| Confidence | 4/5 | 仔细核查了数学推导（Fisher information, Cauchy-Schwarz, Schur complement, Murphy-Topel），通读了全部 16 页含附录 |\n\n---\n\n## Summary\n\n本文提出 G-MFRM（Gated Many-Facet Rasch Model），在标准 MFRM 的线性预测器中引入乘性 contamination gating 项 c_n · e_i，将模型能力、judge severity 和 contamination susceptibility 纳入统一框架联合估计。论文的核心 insight 是：忽略 contamination 项会产生 omitted variable bias (OVB)，使受污染模型的能力被高估。论文提供了完整的可识别性分析（Propositions 1-2, Theorem 1），error propagation bounds（§3.4），以及 Murphy-Topel 方差校正（Appendix C）。在合成数据（N=50）上，G-MFRM 将 θ-RMSE 降低 51.2%；在 Arena-Hard 实际数据（N=8）上，排名相关性从 τ=0.786 提高到 0.857，但统计不显著（bootstrap CI 跨零）。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Contamination susceptibility c_n 的 95% CI coverage 仅 68-71%，严重偏离 95% 名义水平\n- 具体位置：Limitations 第 4 点；Appendix Q；Table 7 caption (\"empirical coverage ~71%\")\n- 问题：在 N=8 时 c_n coverage 为 67.9%，N=50 时也仅 71%（Appendix Q）。这意味着论文报告的 c_n 置信区间系统性过窄，约 1/3 的情况下真值落在区间外。论文在 Table 7 caption 中标注了 \"empirical coverage ~71%\"，在 Limitations 中也有提及，但问题是：(1) coverage 从 N=8 到 N=50 几乎没有改善（68%→71%），说明这不是小样本问题，而是模型结构性缺陷（乘性耦合 + HalfNormal 边界约束）；(2) 论文仍然在主表中报告了具体的 c_n 95% CI 值（如 GPT-3.5-Turbo: [4.40, 6.80]），可能误导读者认为这些区间是校准的。\n- 为什么影响接收：如果 uncertainty quantification 不可靠，那么基于 c_n 的诊断功能（论文声称的主要实用价值之一）就缺乏量化基础。论文虽然诚实地报告了这一问题，但没有提出解决方案或讨论根本原因是否可修复。\n- 建议修改方向：(1) 在 Table 7 中明确标注 \"coverage-uncalibrated\" 而非简单脚注；(2) 探索 simulation-based calibration (SBC; Talts et al., 2018) 的校正方法；(3) 讨论 coverage 不随 N 改善是否暗示模型 misspecification（如 rank-1 假设过强）；(4) 考虑 posterior predictive p-values 作为替代诊断。\n\n**N2** [critical] N=8 下主结果统计不显著，且 power analysis 显示需要 N≥17 才有 80% power\n- 具体位置：§4.2 \"ranking improvement is not statistically significant at N = 8\"；Appendix M (Power Analysis)\n- 问题：Δτ = +0.071 的 bootstrap 95% CI 为 [-0.071, 0.071]，完全对称于零。这并非巧合——Kendall τ 在 N=8 时的最小非零增量恰好是 2/C(8,2) ≈ 0.071，因此 CI 的宽度恰好等于一个 concordant pair swap。这意味着在 N=8 的离散分辨率下，该方法的改善根本无法被检测到。Power analysis 显示 N=8 仅有 ~50% power（Appendix M），而 80% power 需要 N≈17。论文诚实报告了这些，但问题是：如果当前规模下无法统计验证方法的核心声明（ranking improvement），那么 Arena-Hard 实验的证据力大打折扣。\n- 为什么影响接收：一篇声称改善 ranking accuracy 的论文，其主要实验无法在统计上支持这一声明。虽然合成实验（N=50）显示显著改善，但 real-data 验证是必需的。\n- 建议修改方向：(1) 扩展到至少一个更大规模的评测（N≥17），如 LMSYS Chatbot Arena 完整排名或 AlpacaEval 2.0；(2) 如果无法获得更多模型，考虑使用 per-item 预测精度（而非 rank correlation）作为辅助指标，因为 LOO-CV (ΔELPD = -55.7, |Δ/SE| = 5.9) 已经显示了显著的 predictive fit 改善；(3) 明确将论文定位为\"理论 + 诊断贡献\"而非\"ranking improvement\"。\n\n**N3** [critical] Murphy-Topel 渐近校正在 N=8 下的适用性存疑\n- 具体位置：§3.4; Appendix C (Eq. 16: V_MT = V_3 + V_3 C V_2 C^T V_3)\n- 问题：Murphy-Topel (1985) 的方差校正基于大样本渐近理论。在本文中，\"样本量\"对应目标模型数 N=8。这远低于渐近方法通常需要的样本量（经验法则 N≥30）。论文用 bootstrap 估计 V_2 并用有限差分计算 cross-derivative C，这在小样本下可能产生不稳定的估计。c_n 的 CI coverage 仅 68-71% 可能部分归因于 Murphy-Topel 校正的不充分。\n- 为什么影响接收：Murphy-Topel 校正是论文声称的方法论贡献之一（\"neither of which exists for DG-IRT or any prior gated measurement model\"，§3.1）。如果该校正在 paper 自身的评测规模下不工作，这削弱了贡献的实用价值。\n- 建议修改方向：(1) 用 simulation 验证 Murphy-Topel 校正在不同 N 下的 coverage 改善（相对于无校正的 naive posterior），报告 coverage with vs without 校正的对比；(2) 讨论小样本下的替代方案（如 parametric bootstrap 或 double bootstrap）；(3) 如果校正效果微弱，诚实报告。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 7 个 baseline 产生完全相同的排名，使对比缺乏信息量\n- 具体位置：Table 1; §4.2 第 1 段\n- 问题：所有 7 个 baseline（Raw Average, MFRM-only, Sequential, CyclicJudge, CyclicJudge+discard, DCR Factor, Pref. Leakage）产生完全相同的 τ=0.786, ρ=0.905。论文解释为\"ability scores also vary by < 0.03 logits across methods\"（§4.2），但这实际上意味着所有现有方法在当前数据上的行为几乎一致——即 baseline space 完全退化。这使得 G-MFRM 的比较对象实质上只是 \"raw average\"，而不是 7 种不同的校准方法。\n- 建议：(1) 报告 per-model ability estimates 的 pairwise 差异（如 max |θ_baseline_i - θ_baseline_j|），验证 baseline 间确实几乎无差异；(2) 讨论这一现象是 N=8 的 artifact 还是反映了更深层的问题（如所有方法在大规模数据上是否也会趋同）。\n\n**W2** [warning] Rank-1 contamination 结构假设过强\n- 具体位置：§3.1 (Eq. 4); Limitations 第 6 点\n- 问题：c_n · e_i 是一个 rank-1 分解，假设所有模型通过同一 item-level exposure pattern 受污染，仅在 magnitude 上不同。实际上，不同模型可能对不同领域的 items 有不同程度的 memorization（如 coding vs. reasoning）。论文在 Limitations 中提到了 higher-rank decomposition Σ_r c_{nr} · e_{ir}，但没有讨论当 rank-1 假设被违反时 G-MFRM 的行为（是 graceful degradation 还是 systematic bias）。\n- 建议：在合成实验中加入 rank-2 或 domain-specific contamination 的 misspecification 测试，报告 G-MFRM 在 rank-1 假设被违反时的性能退化程度。\n\n**W3** [warning] LOO-CV (ΔELPD) 和 ranking accuracy 之间存在逻辑跳跃\n- 具体位置：§4.2 第 3 段 (\"LOO cross-validation strongly favors G-MFRM\")\n- 问题：ΔELPD_LOO = -55.7 (|Δ/SE| = 5.9) 证明 G-MFRM 有更好的 predictive fit for held-out responses。但论文在同一段中将此与 ranking improvement 并列讨论，给读者造成 \"model fit improvement → ranking improvement\" 的印象。然而 Table 1 已经表明 ranking improvement 不显著。Better model fit 不等于 better ranking——一个模型可以更好地拟合 response patterns 但对 aggregate rankings 没有影响（甚至可能拟合了噪声而非信号）。\n- 建议：明确区分两条 evidence line：(1) LOO-CV 支持 contamination term 的建模必要性（model fit），(2) ranking improvement 在当前 N 下不显著（practical utility）。不要在同一段中混合这两个论点。\n\n**W4** [warning] MCMC 收敛诊断未达到 Vehtari et al. (2021) 推荐标准\n- 具体位置：§4.2 倒数第 2 段 (\"R̂ ≤ 1.03...minimum bulk ESS of 174\")\n- 问题：论文使用 R̂ < 1.05 和 ESS > 100 的阈值，引用 Gelman et al. (2013)。但论文同时引用的 Vehtari et al. (2021) 推荐 R̂ < 1.01 和 ESS_bulk > 400。实际达到的 R̂ ≤ 1.03 和 ESS_min = 174 在两个标准之间。论文诚实地承认\"do not meet the stricter criteria\"并将此与 CI coverage 问题联系，这是好的。但 ESS = 174 意味着有效样本量较低，posterior summaries 可能有非平凡的 MCMC 误差。\n- 建议：(1) 报告 ESS_tail（不仅是 ESS_bulk），因为 HalfNormal 先验下 c_n 的 tail behavior 对 CI coverage 很重要；(2) 考虑增加 sampling iterations（如 8000 或 16000）以改善 ESS；(3) 量化 MCMC 误差对 τ 点估计的影响（如跨 chain 的 τ 变异性）。\n\n**W5** [warning] OVB 线性近似 r=0.86 的 gap 未充分讨论\n- 具体位置：§2 (Observation 1 footnote); Figure 1\n- 问题：Observation 1 依赖线性近似将 OVB 从线性模型迁移到非线性 MFRM。Synthetic validation 显示 Pearson r=0.86 (p<0.001)，解释约 74% 的方差。论文在脚注中承认这是\"approximation\"，但正文中将其作为核心理论动机使用（\"this confounding undermines both sequential estimation strategies\"）。r=0.86 意味着 26% 的 bias variance 未被线性近似捕获——这部分可能来自非线性效应、交互项、或极端 c_n·e_i 值。\n- 建议：(1) 在 Figure 1 中可视化残差的分布（r=0.86 的 scatter 之外），检查是否有系统性偏差；(2) 讨论在什么 c_n·e_i 量级下线性近似开始失效；(3) 强调实际模型（G-MFRM）不依赖此近似（仅用于动机论证）。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Abstract**: \"joint estimation achieves 0.124 ± 0.016, a 51.2% reduction\" 是合成数据结果（N=50），但 Abstract 中先出现的 \"τ = 0.857 vs. 0.786\" 是实际数据（N=8）。两者的 N 不同但并列呈现，可能造成混淆。建议更明确地分隔。\n\n2. **§4.1 \"316 multi-turn conversational items\"**: 经过过滤后仅剩 176 items（44.7% fill rate）。过滤标准（\"filtering for full coverage across all judges and target models\"）应更详细说明——是要求每个 item 被所有 9 个 judge 评分过，还是被至少 k 个 judge 评分过？\n\n3. **Table 7** (Appendix N): c_n 的 95% CI 宽度较大（如 Qwen3-8B: [0.14, 2.50]），跨越了近 2 个数量级。在 coverage 仅 71% 的情况下报告这样宽的\"95% CI\"的实际诊断价值有限。\n\n4. **Self-evaluation** (Appendix I): Qwen2.5-72B 自评 win rate = 1.000 (42/42)，这个完美自评率值得在正文中提及，因为它是 judge bias 的一个极端案例。\n\n5. **§3.2 Stage 2**: reference model anchor 使用 gpt-4-0314。如果该锚模型本身对 Arena-Hard items 有 contamination（尽管 2023 年的模型较早），exposure 估计会系统性偏低。论文在 Limitations 第 2 点提及但未量化风险。\n\n---\n\n## 主要优势\n\n1. **理论贡献扎实**: 将 benchmark contamination 形式化为 MFRM 中的 OVB 是一个新颖且有说服力的框架。Observation 1 清晰地解释了为什么 sequential estimation（先去 bias 或先去 contamination）都不能解决问题——这是本文最核心的 insight。\n\n2. **可识别性分析完整**: Propositions 1-2 给出了必要条件（exposure variation），Theorem 1 给出了充分条件（connected design + exposure variation）。Appendix A 的证明通过 Fisher information matrix 的 Cauchy-Schwarz 分解和 Schur complement 论证，技术上正确且完整。这是首次为 gated IRT 模型建立形式化的可识别性条件。\n\n3. **诚实透明的报告**: 论文明确承认主结果不显著（Δτ CI 跨零），CI coverage 不理想（68-71%），MCMC 未达到最严格标准。这种诚实性在学术论文中值得赞赏，使读者能准确评估证据强度。\n\n4. **合成实验设计周密**: 覆盖了 error propagation（Table 2）、ablation（Table 3）、matched-scale calibration（Appendix P）、power analysis（Appendix M）、CI coverage（Appendix Q）。特别是 matched-scale 合成实验（N=8, I=176, J=9）精确匹配了实际评测配置，Δτ_synthetic = +0.072 与 Δτ_real = +0.071 高度一致。\n\n5. **诊断输出有实用价值**: per-model c_n、per-judge d_j 的估计提供了可操作的诊断信息（如识别哪些模型可能受污染、哪些 judge 偏严/偏松），即使 ranking improvement 本身不显著。Table 8 (Bias Absorption) 中 Δθ 与 c_n 的完美秩相关 (Spearman ρ=1.0) 是 OVB 理论预测的有力实证确认。\n\n---\n\n## Questions for Authors\n\n1. Murphy-Topel 校正相对于 naive posterior 提供了多少 coverage 改善？能否报告 coverage with vs without Murphy-Topel 的对比？\n\n2. 在 real data 中，Var(e_i) 的实际值是多少？这决定了 σ_crit 的具体阈值，对实际应用中判断 Stage 2 估计质量至关重要。\n\n3. 如果将 rank-1 假设放松为 rank-2（如 coding/reasoning 两个维度），可识别性条件如何变化？Theorem 1 是否可以推广？\n\n4. 7 个 baseline 在更大 N 下（如 Chatbot Arena 全部 ~50 个模型）是否仍然产生相同排名？\n\n---\n\n## Missing References\n\n- Ye et al. (2024), \"Benchmarking Benchmark Leakage in Large Language Models\" — 与本文的 contamination detection 高度相关，讨论了多种 leakage detection 方法\n- Oren et al. (2024), \"Proving Test Set Contamination in Black Box Language Models\" — 提出了统计检验方法来检测 contamination，可与本文的 c_n 估计方法做方法论对比\n\n---\n\n## Overall Assessment\n\n**3.5 / 5 — Borderline Conference**\n\n本文的理论框架（OVB 形式化 + 可识别性证明 + 误差传播分析）是扎实且原创的方法论贡献，将教育测量学的经典工具适配到 LLM 评测的新场景。然而，核心实证结果在 N=8 下不显著，c_n 的 CI coverage 问题（68-71%）暗示模型可能存在结构性缺陷（而非仅仅是小样本问题），Murphy-Topel 校正在小样本下的可靠性未得到验证。如果作者能在更大规模上验证（N≥17）或充分 address CI coverage 问题，论文将是强 conference paper。当前状态适合 Findings 或 borderline conference。",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-23T12:07:53.100363+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4721
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-23T12:08:01.960514+00:00_

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
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
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

_source line 463 · 2026-05-23T12:08:02.011191+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-23T12:08:05.426031+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-23T12:08:05.426482+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 466 · 2026-05-23T12:08:07.981262+00:00_

PDF 临时图片已清理。审稿完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 16

## Round 16

12 recorded events


### User

_source line 467 · 2026-05-23T12:12:54.638619+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。特别关注你们在评分和关键判断上的分歧。

---

## Reviewer 2 完整审稿原文

**Overall**: 3.0 / 5 — Findings

**一句话总结**: 问题形式化（OVB framing）优雅，方法论完整，但核心贡献是已有技术（MFRM + DG-IRT gating）的组合，且唯一的真实数据评估仅 8 个模型、主结果不显著，不足以支撑 main conference。

### Must-Fix

**N1** [critical] Abstract 超过 200 词限制（EMNLP 2026 硬约束）
- 多种计数方法均显示 abstract 约 209–213 词，超出 EMNLP 2026 的 200 词上限。这是 desk rejection 风险项。

**N2** [critical] 真实数据评估仅 8 个目标模型，主排名改进不具统计显著性
- Arena-Hard 评估仅含 8 个 target models。Bootstrap Δτ 95% CI = [−0.071, +0.071]（包含零），posterior median τ = 0.786。论文自身 power analysis 承认 N=8 仅有 ~50% power。

**N3** [critical] 增量新颖性——MFRM + DG-IRT gating 的技术组合
- G-MFRM 核心建模贡献是在 MFRM 中加入 DG-IRT 的乘性 gating。扩展包括 binary→continuous, single→multi-rater, identifiability + error propagation 分析。但 (1)(2) 是自然泛化，(3) 是标准数学工具的应用。identifiability 条件（connected design、J≥2、exposure variation）直觉上显然。

### Should-Fix

**W1** [warning] Contamination 验证的循环性风险
- Stage 2 用 reference model anchoring 估计 e_i，Stage 3 用 e_i 估计 c_n。验证方式是"c_n directionally consistent with known training data exposure"。但 c_n 的高低本质上反映的是模型在 high-e_i items 上的超常表现——信息已编码在 e_i 里。

**W2** [warning] Stage 2 对 reference model 的依赖
- 整个 contamination estimation 质量取决于 gpt-4-0314 的可靠性。未做换用不同 anchor model 的 robustness check。

**W3** [warning] "First joint contamination-severity diagnostic" claim 需更精确
- Li et al. (2024, Preference Leakage) 已识别 judge-specific contamination patterns。"first" claim 没有足够限定词。

**W4** [warning] 七个 baseline 产生完全相同排名
- N=8 下各种校正方法对排名无影响，OVB 问题可能 practically irrelevant。

### Minor

**M1** Related Work 压缩至约半页，部分文献覆盖流于表面。
**M2** 可能遗漏的近期相关工作：arXiv:2506.22316 (June 2025), arXiv:2511.21140 (Nov 2025), 4PL-IRT framework (Oct 2025)。
**M3** Abstract 中 synthetic 和 real-data 结果区分不够明确。
**M4** Table 2 中 σ 值的量纲未与 real-data 实际噪声水平对接。
**M5** Observation 1 线性近似 r=0.86，26% 方差未解释。

### Strengths
**S1** OVB 形式化优雅。**S2** Identifiability + error propagation 保证。**S3** 结果报告诚实。**S4** Appendix 极其全面。**S5** 写作质量高。

### Missing References
可能遗漏 3 篇 2025-2026 相关工作（见 M2）。

---

请逐条回应上述所有 Must-Fix、Should-Fix 和 Minor 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-23T12:13:48.433771+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-23T12:13:48.434133+00:00_

1	\begin{abstract}
2	LLM-as-a-judge evaluation corrects for judge bias and benchmark contamination independently, but sequential correction produces biased model ability estimates. We formalize this failure as an omitted variable bias (OVB) problem: when judge severity and contamination effects are both present, any estimator that models one while omitting the other yields asymptotically biased ability estimates---even when the two facets are uncorrelated. We propose the Gated Many-Facet Rasch Model (G-MFRM), which jointly calibrates model ability, item difficulty, judge severity, and contamination susceptibility through staged estimation with externally anchored per-item exposure indicators. Formal identifiability analysis proves that fixing exposure externally is both necessary and sufficient for parameter separation under standard multi-judge designs. Error propagation analysis establishes a critical noise threshold $\sigma_{\mathrm{crit}} = \sqrt{\mathrm{Var}(e_i)}$ below which ability estimates degrade by less than 6\%. In synthetic experiments ($N = 50$, $I = 100$, $J = 8$), G-MFRM reduces ability RMSE by 51.2\% relative to sequential estimation ($p < 0.001$). On Arena-Hard with 8 target models and 9 judges, G-MFRM identifies per-model contamination signals (estimated $c_n > 1.0$ for top-4 models, directionally consistent with known training data exposure; posterior CI coverage is 71\% in synthetic validation) and interpretable judge severity profiles, with nominally higher rank agreement ($\tau = 0.857$ vs.\ $0.786$; bootstrap $\Delta\tau$ CI includes zero at this sample size). LOO cross-validation confirms improved predictive fit for G-MFRM over standard MFRM ($\Delta\mathrm{ELPD} = -55.7$, $|\Delta/\mathrm{SE}| = 5.9$).
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-23T12:13:54.560861+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "echo 'LLM-as-a-judge evaluation corrects for judge bias and benchmark contamination independently, but sequential correction produces biased model ability estimates. We formalize this failure as an omitted variable bias (OVB) problem: when judge severity and contamination effects are both present, any estimator that models one while omitting the other yields asymptotically biased ability estimates---even when the two facets are uncorrelated. We propose the Gated Many-Facet Rasch Model (G-MFRM), which jointly calibrates model ability, item difficulty, judge severity, and contamination susceptibility through staged estimation with externally anchored per-item exposure indicators. Formal identifiability analysis proves that fixing exposure externally is both necessary and sufficient for parameter separation under standard multi-judge designs. Error propagation analysis establishes a critical noise threshold below which ability estimates degrade by less than 6%. In synthetic experiments, G-MFRM reduces ability RMSE by 51.2% relative to sequential estimation. On Arena-Hard with 8 target models and 9 judges, G-MFRM identifies per-model contamination signals for top-4 models, directionally consistent with known training data exposure; posterior CI coverage is 71% in synthetic validation and interpretable judge severity profiles, with nominally higher rank agreement; bootstrap CI includes zero at this sample size. LOO cross-validation confirms improved predictive fit for G-MFRM over standard MFRM.' | wc -w",
  "description": "Count abstract words (plain text, excluding math)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "echo 'LLM-as-a-judge evaluation corrects for judge bias and benchmark contamination independently, but sequential correction produces biased model ability estimates. We formalize this failure as an omitted variable bias (OVB) problem: when judge severity and contamination effects are both present, any estimator that models one while omitting the other yields asymptotically biased ability estimates---even when the two facets are uncorrelated. We propose the Gated Many-Facet Rasch Model (G-MFRM), which jointly calibrates model ability, item difficulty, judge severity, and contamination susceptibility through staged estimation with externally anchored per-item exposure indicators. Formal identifiability analysis proves that fixing exposure externally is both necessary and sufficient for parameter separation under standard multi-judge designs. Error propagation analysis establishes a critical noise threshold below which ability estimates degrade by less than 6%. In synthetic experiments, G-MFRM reduces ability RMSE by 51.2% relative to sequential estimation. On Arena-Hard with 8 target models and 9 judges, G-MFRM identifies per-model contamination signals for top-4 models, directionally consistent with known training data exposure; posterior CI coverage is 71% in synthetic validation and interpretable judge severity profiles, with nominally higher rank agreement; bootstrap CI includes zero at this sample size. LOO cross-validation confirms improved predictive fit for G-MFRM over standard MFRM.' | wc -w",
    "description": "Count abstract words (plain text, excluding math)"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-23T12:13:54.762061+00:00_

198

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-23T12:14:02.043247+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex | sed 's/\\\\begin{abstract}//' | sed 's/\\\\end{abstract}//' | sed 's/\\$[^$]*\\$//g' | sed \"s/\\\\\\\\'//\" | sed 's/~/ /g' | tr -s ' ' | wc -w",
  "description": "Count abstract words stripping LaTeX math"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex | sed 's/\\\\begin{abstract}//' | sed 's/\\\\end{abstract}//' | sed 's/\\$[^$]*\\$//g' | sed \"s/\\\\\\\\'//\" | sed 's/~/ /g' | tr -s ' ' | wc -w",
    "description": "Count abstract words stripping LaTeX math"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-23T12:14:02.245709+00:00_

208

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-23T12:14:21.771603+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# More realistic word count: replace math with text equivalents\ncat /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex | \\\n  sed 's/\\\\begin{abstract}//' | sed 's/\\\\end{abstract}//' | \\\n  sed 's/\\$\\\\sigma_{\\\\mathrm{crit}} = \\\\sqrt{\\\\mathrm{Var}(e_i)}\\$/sigma_crit equals sqrt Var e_i/' | \\\n  sed 's/\\$N = 50\\$/N=50/g' | sed 's/\\$I = 100\\$/I=100/g' | sed 's/\\$J = 8\\$/J=8/g' | \\\n  sed 's/\\$c_n > 1.0\\$/c_n>1.0/' | \\\n  sed 's/\\$\\\\tau = 0.857\\$/tau=0.857/' | sed 's/\\$0.786\\$/0.786/' | \\\n  sed 's/\\$\\\\Delta\\\\tau\\$/Delta-tau/g' | \\\n  sed 's/\\$p < 0.001\\$/p<0.001/' | \\\n  sed 's/\\$\\\\Delta\\\\mathrm{ELPD} = -55.7\\$/Delta-ELPD=-55.7/' | \\\n  sed 's/\\$|\\\\Delta\\/\\\\mathrm{SE}| = 5.9\\$/Delta-SE=5.9/' | \\\n  sed 's/\\$[^$]*\\$//g' | \\\n  sed 's/---/—/g' | sed 's/\\\\\\\\//g' | sed \"s/~/ /g\" | \\\n  tr -s ' ' '\\n' | grep -v '^$' | wc -l",
  "description": "Count abstract words with math rendered as text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "# More realistic word count: replace math with text equivalents\ncat /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex | \\\n  sed 's/\\\\begin{abstract}//' | sed 's/\\\\end{abstract}//' | \\\n  sed 's/\\$\\\\sigma_{\\\\mathrm{crit}} = \\\\sqrt{\\\\mathrm{Var}(e_i)}\\$/sigma_crit equals sqrt Var e_i/' | \\\n  sed 's/\\$N = 50\\$/N=50/g' | sed 's/\\$I = 100\\$/I=100/g' | sed 's/\\$J = 8\\$/J=8/g' | \\\n  sed 's/\\$c_n > 1.0\\$/c_n>1.0/' | \\\n  sed 's/\\$\\\\tau = 0.857\\$/tau=0.857/' | sed 's/\\$0.786\\$/0.786/' | \\\n  sed 's/\\$\\\\Delta\\\\tau\\$/Delta-tau/g' | \\\n  sed 's/\\$p < 0.001\\$/p<0.001/' | \\\n  sed 's/\\$\\\\Delta\\\\mathrm{ELPD} = -55.7\\$/Delta-ELPD=-55.7/' | \\\n  sed 's/\\$|\\\\Delta\\/\\\\mathrm{SE}| = 5.9\\$/Delta-SE=5.9/' | \\\n  sed 's/\\$[^$]*\\$//g' | \\\n  sed 's/---/—/g' | sed 's/\\\\\\\\//g' | sed \"s/~/ /g\" | \\\n  tr -s ' ' '\\n' | grep -v '^$' | wc -l",
    "description": "Count abstract words with math rendered as text"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-23T12:14:21.927768+00:00_

215

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 156
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-23T12:15:56.878742+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: Abstract 超过 200 词限制**\n同意。我独立验证了词数：去除 LaTeX math 后约 208 词，渲染为文本后约 215 词，确实超出 EMNLP 2026 的 200 词硬约束。这是格式违规，属于 desk rejection 风险。但我认为不应定为 \"critical\"——这是一个 5 分钟即可修复的编辑问题（删减约 15 词），不影响论文的科学内容。建议降级为 Should-Fix 或 Minor。\n\n**[AGREE] R2-N2: 真实数据评估仅 8 个模型，主结果不显著**\n完全同意，这也是我的 N2。Δτ=+0.071 的 bootstrap CI [-0.071, +0.071] 对称跨零，N=8 下 Kendall τ 的离散分辨率恰好是 0.071（= 2/C(8,2)），使得任何单步排名改善都无法被统计检测到。Power analysis (Appendix M) 确认 N≈17 才有 80% power。这是论文最核心的实证弱点。\n\n**[REBUT] R2-N3: \"增量新颖性——MFRM + DG-IRT 的技术组合\"**\n我不同意将此定性为\"增量\"或\"已有技术的自然组合\"。理由如下：\n\n1. **OVB 形式化本身是新颖贡献**：Observation 1（§2）将 contamination 遗漏形式化为 MFRM 中的 OVB，并证明 sequential estimation（无论先去 bias 还是先去 contamination）都无法解决这一问题。这一 insight 不依赖于任何特定的建模方案，而是对 LLM evaluation 领域现有范式的根本性批判。据我所知，这是首次在 LLM-as-a-judge 文献中给出这一严格论证。\n\n2. **Identifiability 条件并非\"直觉上显然\"**：Reviewer 2 称条件\"intuitive\"，但 (a) DG-IRT (Shu et al., 2013) 没有任何可识别性分析——原始论文使用 EM 估计而未讨论参数可分离性；(b) Theorem 1 的证明核心——Fisher information block 的 Cauchy-Schwarz 分解（Appendix A, Eq. 9）——揭示了 Var_w(e_i) > 0 是关键条件，这直接解释了为什么 constant exposure 导致不可识别（Proposition 2），并为实际数据收集提供了可操作的设计指南。\"事后看来直觉\"和\"事前形式化证明\"之间有本质差别。\n\n3. **Binary→continuous 和 single→multi-rater 不仅是\"自然泛化\"**：continuous exposure 改善了 c_n-RMSE 40%（Table 3 ablation, Appendix D: binary gating c_n-RMSE = 0.833 vs continuous = 0.593, p < 0.001），证明 graded modeling 带来了实质性改善。Multi-rater 设计使得 judge severity d_j 成为可估计的独立 facet，这在 DG-IRT 的单 rater 框架中根本不存在。\n\n4. **Murphy-Topel 方差校正在 staged IRT 中的首次应用**（§3.4, Appendix C）：这不是\"标准工具的简单应用\"——Murphy-Topel 原始公式 (1985) 针对线性模型，将其适配到 MCMC-based cumulative logit 模型需要推导 cross-derivative matrix C 的具体形式（Appendix C, Eq. 15），并通过 bootstrap + finite differences 实现。此前没有 gated IRT 或任何 IRT 模型使用过这一方法。\n\n综上，虽然 G-MFRM 的 model specification（Eq. 4）可以被描述为\"MFRM + gating term\"，但论文的核心贡献在于围绕这一模型的理论分析体系（OVB、identifiability、error propagation、Murphy-Topel），而非模型本身的 specification。这些分析在 gated IRT 文献中没有先例。我维持 3.5 (Borderline Conference) 的评分——理论贡献值得 conference consideration，但实证弱点（N=8）阻止更高评分。\n\n---\n\n### Should-Fix\n\n**[AGREE with nuance] R2-W1: Contamination 验证的循环性风险**\nReviewer 2 指出了一个重要的方法论隐患：e_i 定义了\"哪些 items 受暴露\"，c_n 捕获\"模型在 high-e_i items 上的超常表现\"，这在信息论意义上确实有循环性。\n\n但我认为需要区分两个层次：\n- **模型层面**：G-MFRM 的 c_n · e_i 结构在设计上就是这样工作的——它 decompose 了 model-item interaction 为 model-specific susceptibility × item-specific exposure。这不是 bug，而是 feature——问题在于这种分解是否有独立验证。\n- **验证层面**：论文用 model age 作为外部 proxy 验证 c_n 的 face validity（§4.2: older models have higher c_n）。这是弱验证但并非循环——model age 是独立于 e_i 和 response data 的信息。Table 8 (Appendix O) 中 Δθ 与 c_n 的 perfect rank correlation (Spearman ρ=1.0) 验证的是 OVB 理论预测而非 contamination ground truth。\n\n**建议作者**：承认 contamination \"ground truth\" 在 LLM 评测中本质上不可获得，并更明确地将 c_n 定位为\"在高暴露 items 上的 differential performance\"指标，而非对\"真实污染程度\"的直接测量。\n\n**[AGREE] R2-W2: Stage 2 对 reference model 的依赖**\n同意。Appendix L (Table 6) 仅测试了 anchoring/agreement 权重配置的鲁棒性（75/25 vs 50/50 vs 90/10 vs 100/0），但所有配置都使用相同的 anchor model (gpt-4-0314)。换用不同 anchor（如 Claude 3 Opus 或 Llama-2-70B 等同期模型）的 robustness check 是缺失的。这也是我的 Minor #5 中提到的问题。不过，考虑到 exposure pipeline 的输出经过 clipping 到 [0,1] 和 composite weighting，不同 anchor 之间的差异可能不大。\n\n**[AGREE with nuance] R2-W3: \"First joint contamination-severity diagnostic\" claim 需更精确**\n同意需要更精确的限定。但我想补充：Li et al. (2024, Preference Leakage) 识别了 judge-specific contamination patterns，但其方法是 detect-and-discard（移除 contaminated items），而非在统一测量模型中 jointly estimate contamination susceptibility 和 judge severity 作为 continuous parameters。G-MFRM 的 \"first\" 可以限定为 \"first measurement-theoretic framework that jointly estimates model-specific contamination susceptibility and judge severity as continuous facets within a single IRT model\"。这个区分是有意义的——detect-and-discard 丢弃了信息，而 G-MFRM 利用 contamination signal 来改善能力估计。\n\n**[AGREE] R2-W4: 七个 baseline 产生完全相同排名**\n完全同意，这也是我的 W1。所有 7 个 baseline 在 N=8 下产生 τ=0.786, ρ=0.905，使比较缺乏信息量。论文在 §4.2 解释为 ability scores 差异 < 0.03 logits，这虽然合理但实际上意味着 baseline space 退化。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1: Related Work 压缩**\n同意 Related Work（§5）约半页，部分文献仅一句话覆盖。但考虑到 8 页正文限制，这种压缩在 space budget 约束下是合理的。如果审稿人认为特定 related work 讨论不足，应指出具体缺失的对比论述。\n\n**[NEUTRAL] R2-M2: 遗漏的近期相关工作**\n无法独立验证这三篇 arXiv 论文的内容和相关性。如果确实高度相关且已在提交截止前公开，作者应纳入讨论。但 arXiv preprints 不一定构成 \"missing references\"——取决于发布时间是否在 submission deadline 之前。\n\n**[AGREE] R2-M3: Abstract 中 synthetic 和 real-data 结果区分不够明确**\n同意，这也是我的 Minor #1。两组结果并列但 N 不同，可能造成混淆。\n\n**[AGREE] R2-M4: Table 2 σ 值未与 real-data 噪声水平对接**\n同意。Table 2 (§4.3) 的 σ ∈ {0, 0.1, 0.2, 0.5} 是合成实验中的注入噪声。论文未报告 real data 中 Stage 2 exposure estimation 的实际 σ 估计值，也未报告 real data 的 Var(e_i)。这使得读者无法判断 real-data 的 exposure 噪声是否低于 σ_crit = √Var(e_i) ≈ 0.2（§3.4 中的理论阈值）。这也是我对 R1 的 Question 2 中提出的问题。\n\n**[AGREE] R2-M5: Observation 1 线性近似 r=0.86**\n同意，这也是我的 W5。r=0.86 解释 74% 方差，26% 未解释。但我补充：G-MFRM 的实际模型（Eq. 4）不依赖此线性近似——Observation 1 仅用于 motivation/intuition，实际估计使用完整的非线性 cumulative logit 模型。因此 r=0.86 的 gap 影响的是论文的叙事说服力，而非方法本身的有效性。\n\n---\n\n### 关于评分分歧\n\nReviewer 2 给出 3.0 (Findings)，我给出 3.5 (Borderline Conference)。核心分歧在于 **N3（新颖性判断）**。\n\nReviewer 2 将贡献概括为 \"已有技术的组合\"（MFRM + DG-IRT gating），我认为这低估了理论分析的独立价值。具体来说：\n\n- 如果论文仅提出 G-MFRM 模型（Eq. 4）并跑实验，我同意这是增量贡献，3.0 合理。\n- 但论文的核心贡献是 **围绕这一模型的理论分析体系**：OVB 形式化解释了为什么 sequential estimation 必然失败（§2）、identifiability proof 给出了参数可分离的充要条件（§3.3）、error propagation analysis 量化了 staged estimation 的误差边界（§3.4）、Murphy-Topel 校正处理了 generated regressors 问题（Appendix C）。这些分析对 gated IRT 文献是全新的。\n\n然而，实证弱点（N=8 不显著、CI coverage 68-71%）阻止了更高评分。**如果实证结果在 N≥17 下显著**，这将是清晰的 4.0 (Conference) 论文。当前状态下，我维持 3.5：理论贡献介于 Findings 和 Conference 之间。",
  "reviewer_id": "1",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: Abstract 超过 200 词限制**\n同意。我独立验证了词数：去除 LaTeX math 后约 208 词，渲染为文本后约 215 词，确实超出 EMNLP 2026 的 200 词硬约束。这是格式违规，属于 desk rejection 风险。但我认为不应定为 \"critical\"——这是一个 5 分钟即可修复的编辑问题（删减约 15 词），不影响论文的科学内容。建议降级为 Should-Fix 或 Minor。\n\n**[AGREE] R2-N2: 真实数据评估仅 8 个模型，主结果不显著**\n完全同意，这也是我的 N2。Δτ=+0.071 的 bootstrap CI [-0.071, +0.071] 对称跨零，N=8 下 Kendall τ 的离散分辨率恰好是 0.071（= 2/C(8,2)），使得任何单步排名改善都无法被统计检测到。Power analysis (Appendix M) 确认 N≈17 才有 80% power。这是论文最核心的实证弱点。\n\n**[REBUT] R2-N3: \"增量新颖性——MFRM + DG-IRT 的技术组合\"**\n我不同意将此定性为\"增量\"或\"已有技术的自然组合\"。理由如下：\n\n1. **OVB 形式化本身是新颖贡献**：Observation 1（§2）将 contamination 遗漏形式化为 MFRM 中的 OVB，并证明 sequential estimation（无论先去 bias 还是先去 contamination）都无法解决这一问题。这一 insight 不依赖于任何特定的建模方案，而是对 LLM evaluation 领域现有范式的根本性批判。据我所知，这是首次在 LLM-as-a-judge 文献中给出这一严格论证。\n\n2. **Identifiability 条件并非\"直觉上显然\"**：Reviewer 2 称条件\"intuitive\"，但 (a) DG-IRT (Shu et al., 2013) 没有任何可识别性分析——原始论文使用 EM 估计而未讨论参数可分离性；(b) Theorem 1 的证明核心——Fisher information block 的 Cauchy-Schwarz 分解（Appendix A, Eq. 9）——揭示了 Var_w(e_i) > 0 是关键条件，这直接解释了为什么 constant exposure 导致不可识别（Proposition 2），并为实际数据收集提供了可操作的设计指南。\"事后看来直觉\"和\"事前形式化证明\"之间有本质差别。\n\n3. **Binary→continuous 和 single→multi-rater 不仅是\"自然泛化\"**：continuous exposure 改善了 c_n-RMSE 40%（Table 3 ablation, Appendix D: binary gating c_n-RMSE = 0.833 vs continuous = 0.593, p < 0.001），证明 graded modeling 带来了实质性改善。Multi-rater 设计使得 judge severity d_j 成为可估计的独立 facet，这在 DG-IRT 的单 rater 框架中根本不存在。\n\n4. **Murphy-Topel 方差校正在 staged IRT 中的首次应用**（§3.4, Appendix C）：这不是\"标准工具的简单应用\"——Murphy-Topel 原始公式 (1985) 针对线性模型，将其适配到 MCMC-based cumulative logit 模型需要推导 cross-derivative matrix C 的具体形式（Appendix C, Eq. 15），并通过 bootstrap + finite differences 实现。此前没有 gated IRT 或任何 IRT 模型使用过这一方法。\n\n综上，虽然 G-MFRM 的 model specification（Eq. 4）可以被描述为\"MFRM + gating term\"，但论文的核心贡献在于围绕这一模型的理论分析体系（OVB、identifiability、error propagation、Murphy-Topel），而非模型本身的 specification。这些分析在 gated IRT 文献中没有先例。我维持 3.5 (Borderline Conference) 的评分——理论贡献值得 conference consideration，但实证弱点（N=8）阻止更高评分。\n\n---\n\n### Should-Fix\n\n**[AGREE with nuance] R2-W1: Contamination 验证的循环性风险**\nReviewer 2 指出了一个重要的方法论隐患：e_i 定义了\"哪些 items 受暴露\"，c_n 捕获\"模型在 high-e_i items 上的超常表现\"，这在信息论意义上确实有循环性。\n\n但我认为需要区分两个层次：\n- **模型层面**：G-MFRM 的 c_n · e_i 结构在设计上就是这样工作的——它 decompose 了 model-item interaction 为 model-specific susceptibility × item-specific exposure。这不是 bug，而是 feature——问题在于这种分解是否有独立验证。\n- **验证层面**：论文用 model age 作为外部 proxy 验证 c_n 的 face validity（§4.2: older models have higher c_n）。这是弱验证但并非循环——model age 是独立于 e_i 和 response data 的信息。Table 8 (Appendix O) 中 Δθ 与 c_n 的 perfect rank correlation (Spearman ρ=1.0) 验证的是 OVB 理论预测而非 contamination ground truth。\n\n**建议作者**：承认 contamination \"ground truth\" 在 LLM 评测中本质上不可获得，并更明确地将 c_n 定位为\"在高暴露 items 上的 differential performance\"指标，而非对\"真实污染程度\"的直接测量。\n\n**[AGREE] R2-W2: Stage 2 对 reference model 的依赖**\n同意。Appendix L (Table 6) 仅测试了 anchoring/agreement 权重配置的鲁棒性（75/25 vs 50/50 vs 90/10 vs 100/0），但所有配置都使用相同的 anchor model (gpt-4-0314)。换用不同 anchor（如 Claude 3 Opus 或 Llama-2-70B 等同期模型）的 robustness check 是缺失的。这也是我的 Minor #5 中提到的问题。不过，考虑到 exposure pipeline 的输出经过 clipping 到 [0,1] 和 composite weighting，不同 anchor 之间的差异可能不大。\n\n**[AGREE with nuance] R2-W3: \"First joint contamination-severity diagnostic\" claim 需更精确**\n同意需要更精确的限定。但我想补充：Li et al. (2024, Preference Leakage) 识别了 judge-specific contamination patterns，但其方法是 detect-and-discard（移除 contaminated items），而非在统一测量模型中 jointly estimate contamination susceptibility 和 judge severity 作为 continuous parameters。G-MFRM 的 \"first\" 可以限定为 \"first measurement-theoretic framework that jointly estimates model-specific contamination susceptibility and judge severity as continuous facets within a single IRT model\"。这个区分是有意义的——detect-and-discard 丢弃了信息，而 G-MFRM 利用 contamination signal 来改善能力估计。\n\n**[AGREE] R2-W4: 七个 baseline 产生完全相同排名**\n完全同意，这也是我的 W1。所有 7 个 baseline 在 N=8 下产生 τ=0.786, ρ=0.905，使比较缺乏信息量。论文在 §4.2 解释为 ability scores 差异 < 0.03 logits，这虽然合理但实际上意味着 baseline space 退化。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1: Related Work 压缩**\n同意 Related Work（§5）约半页，部分文献仅一句话覆盖。但考虑到 8 页正文限制，这种压缩在 space budget 约束下是合理的。如果审稿人认为特定 related work 讨论不足，应指出具体缺失的对比论述。\n\n**[NEUTRAL] R2-M2: 遗漏的近期相关工作**\n无法独立验证这三篇 arXiv 论文的内容和相关性。如果确实高度相关且已在提交截止前公开，作者应纳入讨论。但 arXiv preprints 不一定构成 \"missing references\"——取决于发布时间是否在 submission deadline 之前。\n\n**[AGREE] R2-M3: Abstract 中 synthetic 和 real-data 结果区分不够明确**\n同意，这也是我的 Minor #1。两组结果并列但 N 不同，可能造成混淆。\n\n**[AGREE] R2-M4: Table 2 σ 值未与 real-data 噪声水平对接**\n同意。Table 2 (§4.3) 的 σ ∈ {0, 0.1, 0.2, 0.5} 是合成实验中的注入噪声。论文未报告 real data 中 Stage 2 exposure estimation 的实际 σ 估计值，也未报告 real data 的 Var(e_i)。这使得读者无法判断 real-data 的 exposure 噪声是否低于 σ_crit = √Var(e_i) ≈ 0.2（§3.4 中的理论阈值）。这也是我对 R1 的 Question 2 中提出的问题。\n\n**[AGREE] R2-M5: Observation 1 线性近似 r=0.86**\n同意，这也是我的 W5。r=0.86 解释 74% 方差，26% 未解释。但我补充：G-MFRM 的实际模型（Eq. 4）不依赖此线性近似——Observation 1 仅用于 motivation/intuition，实际估计使用完整的非线性 cumulative logit 模型。因此 r=0.86 的 gap 影响的是论文的叙事说服力，而非方法本身的有效性。\n\n---\n\n### 关于评分分歧\n\nReviewer 2 给出 3.0 (Findings)，我给出 3.5 (Borderline Conference)。核心分歧在于 **N3（新颖性判断）**。\n\nReviewer 2 将贡献概括为 \"已有技术的组合\"（MFRM + DG-IRT gating），我认为这低估了理论分析的独立价值。具体来说：\n\n- 如果论文仅提出 G-MFRM 模型（Eq. 4）并跑实验，我同意这是增量贡献，3.0 合理。\n- 但论文的核心贡献是 **围绕这一模型的理论分析体系**：OVB 形式化解释了为什么 sequential estimation 必然失败（§2）、identifiability proof 给出了参数可分离的充要条件（§3.3）、error propagation analysis 量化了 staged estimation 的误差边界（§3.4）、Murphy-Topel 校正处理了 generated regressors 问题（Appendix C）。这些分析对 gated IRT 文献是全新的。\n\n然而，实证弱点（N=8 不显著、CI coverage 68-71%）阻止了更高评分。**如果实证结果在 N≥17 下显著**，这将是清晰的 4.0 (Conference) 论文。当前状态下，我维持 3.5：理论贡献介于 Findings 和 Conference 之间。",
    "reviewer_id": "1",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-23T12:16:01.415767+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4537
}
```

</details>

---


### Assistant

_source line 478 · 2026-05-23T12:16:10.055040+00:00_

已提交对 Reviewer 2 的逐条回应。

核心分歧在 **N3（新颖性）**：我 REBUT 了"增量组合"的判断——论文的核心贡献不是 model specification（MFRM + gating），而是围绕它的理论分析体系（OVB 形式化、identifiability proof、error propagation、Murphy-Topel），这些在 gated IRT 文献中没有先例。

对其余 10 个问题中的 9 个（N1, N2, W1-W4, M1, M3-M5）我 AGREE 或 AGREE with nuance，M2 保持 NEUTRAL（无法独立验证 arXiv 论文相关性）。

整体评分维持 3.5 vs Reviewer 2 的 3.0，分歧集中在理论贡献的权重判断上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1"
}
```

</details>

---


## Round 17

## Round 17

70 recorded events


### User

_source line 479 · 2026-05-25T21:15:46.612610+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性**审查。

**目标 Venue**: EMNLP 2026（通过 ARR 统一审稿）
**格式要求**: 长文正文 8 页，参考文献不限，Limitations 必须，ACL 模板，double-blind
**Deadline**: 2026-05-26
**论文路径**: `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex`
**PDF**: `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/submitted.pdf`

**你的审查侧重**：
1. **OVB 形式化**：Observation 1 将线性 OVB 结果应用于非线性 MFRM——近似质量是否充分论证？r=0.80 的解释是否合理？
2. **G-MFRM 模型规约**：Eq. 4 的 gating 结构 c_n·e_i 设计合理性，HalfNormal hierarchical prior 的选择，与 DG-IRT (Shu 2013) 的增量贡献
3. **Identifiability 分析**：Propositions 1-2 和 Theorem 1 的证明正确性（Appendix A），Cauchy-Schwarz + Schur complement 论证，local vs global identifiability 讨论
4. **Error propagation**：Murphy-Topel correction 在 N=8 下的适用性，σ_crit 阈值推导假设（i.i.d. Gaussian），CI coverage 68-71% 的结构性问题
5. **MCMC 收敛**：R̂/ESS 报告与引用标准一致性，convergence diagnostics 充分性
6. **统计检验**：合成实验 p 值，真实数据 bootstrap Δτ CI 包含零的解释，LOO-ELPD 与 ranking accuracy 的关系

**评分标准（EMNLP ARR）**：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit

请输出完整审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment（含评分和置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-25T21:15:55.560776+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-25T21:15:55.611830+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/review_reviewer_1_51c3c93c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-25T21:15:57.575874+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*review-reviewer-session-start*",
  "path": "/home/ubuntu/.agent-ml-research-prod43"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*review-reviewer-session-start*",
    "path": "/home/ubuntu/.agent-ml-research-prod43"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-25T21:15:59.506330+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 1930
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-25T21:16:01.273803+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start*",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start*",
    "path": "/home/ubuntu/agent-ml-research"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-25T21:16:03.434925+00:00_

/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 2161
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-25T21:16:05.215587+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-25T21:16:05.266326+00:00_

1	---
2	name: review-reviewer-session-start
3	description: Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。
4	priority: 8
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 2
11	roles: []
12	---
13	
14	# Review Reviewer Session 启动流程
15	
16	执行顺序：
17	1. 读取论文文件（`projects/{project}/paper/main.tex` 或类似路径）
18	2. 检查论文格式状态：
19	   - 页数是否在 venue 要求内（若已知 venue）
20	   - LaTeX 是否可编译（调用 `ssh_execute` 运行 `pdflatex` 或 `latexmk`）
21	   - 图表是否有标题和标签
22	3. 视觉检查：如果已有编译好的 PDF，使用 `paper-visual-review` skill 渲染关键页面（首页、图表页、参考文献页），检查排版溢出、公式渲染、图表质量等视觉问题
23	4. 检查投稿材料清单：
24	   - cover letter 是否存在
25	   - 补充材料是否准备
26	   - 参考文献格式是否正确
27	5. 向 Review Director 汇报（`review_reviewer_post_to_director`）：
28	   - 论文当前状态
29	   - 发现的格式问题（如有）
30	   - 视觉检查结果（如有）
31	   - 缺少的材料（如有）
32	
33	此流程在 Review Director 分配任务后执行。
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-25T21:16:07.978112+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,WebSearch,WebFetch,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,WebSearch,WebFetch,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-25T21:16:08.028776+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-25T21:16:11.943567+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 491 · 2026-05-25T21:16:14.152571+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/submitted.pdf",
  "project": "gated_mfrm_judge_bias",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/submitted.pdf",
    "project": "gated_mfrm_judge_bias",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 492 · 2026-05-25T21:16:19.520817+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Review Form Criteria

The review form distinguishes between different types of papers and uses specific criteria:

- The main criteria for Findings are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

- The Over
…[truncated 1105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7577
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-25T21:16:21.581688+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 981.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 469.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 430.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 469.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.1}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-prod4
…[truncated 372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7429
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-25T21:16:26.599029+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions (soundness, excitement, overall assessment, confidence, etc.), their scales, and detailed descriptions for each score level. Include any guidance on what constitutes each score."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions (soundness, excitement, overall assessment, confidence, etc.), their scales, and detailed descriptions for each score level. Include any guidance on what constitutes each score."
  }
}
```

</details>

---


### Tool call

_source line 495 · 2026-05-25T21:16:27.653601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-25T21:16:28.107559+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 497 · 2026-05-25T21:16:28.358669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 498 · 2026-05-25T21:16:29.368585+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1714
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-25T21:16:30.125173+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1766
}
```

</details>

---


### Tool result

_source line 500 · 2026-05-25T21:16:30.176230+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2068
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-25T21:16:34.340850+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with half-point options)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1-5 (with half-point options)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make effort to attend."
- **3**: "Interesting: I might mention some points or attend if time permits."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 4. **Overall Assessment**
Scale: 1-5 (with half-point options)
- **5**: "Consider for Award: Could be considered for outstanding paper award (top 2.5%)."
- **4**: "Conference: Could be accepted to an ACL conference."
- **3**: "Findings: Could be accepted to ACL Findings."
- **2**: "Resubmit next cycle: Needs substantial revisions."
- **1**: "Do not resubmit: Requires complete rework or lacks relevance."

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce
…[truncated 709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7741
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-25T21:16:38.560130+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 503 · 2026-05-25T21:16:39.726623+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 504 · 2026-05-25T21:16:40.233362+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1673
}
```

</details>

---


### Tool call

_source line 505 · 2026-05-25T21:16:40.235607+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---
