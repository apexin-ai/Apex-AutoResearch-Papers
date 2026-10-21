# Reviewer 2 coordination — Part 1 of 7

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

[Transcript overview](../reviewer-2-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/61/612e3ccdc1fa1ccf1a84.json)

## Round 1

## Round 1

66 recorded events


### User

_source line 1 · 2026-05-16T21:55:39.752770+00:00_

[Round 1 审稿请求]:

## Reviewer 2 (R2): Novelty and Related Work Assessment

**Paper**: "Hidden States Universally Encode Safety Commitment Better Than Text: A Cross-Architecture Evaluation of Reasoning Model Monitoring"

---

### Summary

The paper presents an empirical study of detecting "commitment points" in reasoning model chain-of-thought traces where safety reasoning permanently ceases. It compares hidden-state probes, text-based monitors, and unsupervised geometric methods across 4 models (r1-8b Llama, r1-32b Qwen2.5, QwQ-32B Qwen2.5, OpenThinker-7B Qwen2.5). Three claims are made: (1) HS temporal probes achieve lower pre-CP FPR (14-16% vs 27-36% text, pooled p=0.003), (2) temporal context W=15 universally improves coverage +5-7pp, and (3) pre-textual detection remains fundamentally unreliable (median lead=0). A supplementary cross-model transfer finding shows 67-74% accuracy across architectures.

---

### Strengths

- **Genuine problem identification and gap-filling**: The observation that existing hidden-state jailbreak detectors (TrajGuard, SafeSwitch, SIREN) were designed for adversarial-input attacks on instruction-tuned models and have never been evaluated on reasoning-model self-jailbreak is correct. This represents a legitimate research gap given that reasoning models pose qualitatively different safety challenges (internal deliberation failure vs. external attack). The "commitment point" formalization as a detection target is a reasonable contribution.

- **Informative negative result with principled explanation**: The finding that pre-textual detection is unreliable (median lead = 0, only 38-45% of detections precede textual CP) combined with oracle decomposition (62% of gap attributable to future information) provides a useful boundary result. The mutual information analysis (MI=0.42 for current state, MI->0.03 for future labels) gives mechanistic grounding that elevates this beyond a simple "method X failed" report.

- **Cross-architecture consistency adds credibility**: The pooled analysis across 3-4 models with low heterogeneity (I^2=0.12) strengthens all three claims. The consistent optimal layer depth (44-47%), consistent FPR ranges (14-16%), and consistent temporal gains (+5-7pp) across two architecture families and two scales constitute stronger evidence than a single-model study.

- **Signal geometry insight is transferable**: The Fisher discriminant analysis revealing high separability in full space (Fisher ~17-18) but collapse in PCA-3 (Fisher ~1) provides a concrete, actionable explanation for why covariance-based geometric detectors fail. This insight transfers beyond this specific paper to anyone designing safety detectors.

- **Appropriate empirical framing**: The authors correctly position this as an empirical study rather than claiming a novel method, which is honest given that the core techniques (temporal window LR, GRU) are standard. The framing as "what works, what fails, and why" is appropriate.

- **Cross-model transfer finding is non-trivial**: 67-74% transfer accuracy across architecture families (vs. 50% chance) reveals shared safety geometry. The structured comparison (within-family 73-74% vs. cross-family 68-71%) provides a clean decomposition of architecture vs. training effects.

---

### Weaknesses

- **Limited methodological novelty is the central concern (major)**: The core detection methods are: (a) logistic regression on concatenated sliding-window features, (b) GRU on hidden-state sequences, (c) TF-IDF probes on text. None of these are new. Temporal window feature concatenation has been standard in NLP since at least Ratnaparkhi (1996) and in probing classifiers since Conneau et al. (2018). The paper acknowledges this ("simplicity is the finding"), but for a top venue, even an empirical study typically requires either a novel evaluation methodology, a surprising finding that overturns prior beliefs, or depth of insight that standard tools alone cannot provide. The "hidden states beat text" result, while useful, is broadly expected from the representation probing literature — hidden states encode richer information than surface text by construction (they are the causal antecedent of text generation).

- **"Hidden states beat text" is expected, not surprising (major)**: The central claim that hidden-state probes outperform text-based probes is arguably the expected outcome from first principles. Hidden states contain strictly more information than the text they generate (text is a lossy projection of hidden states via the unembedding layer). The probing classifiers literature (Belinkov et al. 2017, Conneau et al. 2018, Hewitt & Manning 2019) has long established that hidden representations encode linguistic and semantic properties better than surface features. The finding would be novel only if text OUTPERFORMED hidden states, requiring explanation. The precision advantage (16% vs 27-36% FPR) quantifies the expected gap rather than revealing something unexpected. The paper needs to argue why this quantification is itself the contribution — is the magnitude surprising? Is it actionable?

- **"Pre-textual detection unreliable" finding is partially tautological (major)**: The commitment point is defined as "the first step after which safety reasoning permanently ceases." A probe trained to detect "current step is post-CP" will by definition fire at or after the CP, because the training signal is derived from the CP label. The "fundamentally unreliable" framing conflates two distinct issues: (a) whether hidden states at step t encode information about whether safety reasoning will cease after step t (genuinely interesting), and (b) whether a probe trained on post-hoc CP labels can fire before those labels say the transition occurred (definitionally constrained). The oracle's advantage comes from accessing future labels, which is a property of the task definition, not a discovery about representations. The MI decomposition partially addresses this but the paper does not sufficiently distinguish the definitional from the empirical component.

- **Cross-architecture transfer finding is not novel in isolation (moderate)**: Cross-model transfer of probing classifiers has been studied extensively. Frank (2603.18280) showed cross-model safety probe transfer fails; Conneau et al. (2020) showed cross-lingual transfer of probes; stitching and CKA-based similarity analyses are well-established. The finding that safety commitment transfers at 67-74% is useful data but not methodologically novel. The contribution would be stronger if the paper analyzed WHY transfer works (what geometric structure is shared) rather than just reporting accuracy numbers.

- **Related work has significant gaps (major)**: With only 14 citations, the paper omits several critical lines of work:

  1. **Probing classifiers methodology** (Belinkov et al. 2017; Conneau et al. 2018; Hewitt & Manning 2019; Hewitt & Liang 2019 control tasks) — The entire methodological framework this paper uses comes from this literature. The control task critique (Hewitt & Liang 2019) is particularly relevant: does the temporal window probe learn genuine safety-state information, or does it exploit structural regularities (e.g., positional encoding of "late in trace")? Without a control task, the probe's performance cannot be attributed to safety-specific information.

  2. **Activation patching / causal tracing** (Meng et al. 2022; Conmy et al. 2023) — These methods establish causal (not merely correlational) relationships between hidden states and model behavior. The paper's probes demonstrate correlation between hidden states and CP labels but never establish that intervening at the detected step would actually prevent harmful output. This is a critical gap for the safety narrative.

  3. **Representation engineering and steering vectors** (Zou et al. 2023; Turner et al. 2023; Arditi et al. 2024 is cited but the broader RepE framework is underexplored) — These works establish that safety-relevant linear directions exist in hidden-state space and can be used for both detection and intervention. The paper's Fisher discriminant analysis is essentially rediscovering this property in a new context without acknowledging the theoretical framework.

  4. **Process supervision and step-level reasoning evaluation** (Lightman et al. 2023 is cited but not discussed; Uesato et al. 2022; Wang et al. 2023 Math-Shepherd) — Process Reward Models perform step-level classification on reasoning traces, which is structurally identical to this paper's task (classifying each step as pre/post-CP). The connection between PRMs and safety commitment detection is deep and unexplored.

  5. **Mechanistic interpretability / circuit analysis** (Olsson et al. 2022; Wang et al. 2022 IOI; Nanda et al. 2023) — Understanding which circuits are responsible for safety reasoning would provide mechanistic grounding for why probes work at specific layers.

  6. **Jailbreak detection literature beyond the cited works** (Robey et al. 2023 SmoothLLM; Alon & Kamfonas 2023; Jain et al. 2023 perplexity-based) — These provide alternative detection paradigms.

  7. **Time series change-point detection in deep learning** (beyond BOCPD/CUSUM; e.g., Killick et al. 2012 PELT; Truong et al. 2020 survey) — The paper evaluates only BOCPD and CUSUM but the change-point detection literature is much richer.

- **"Universally" in title is overclaimed (moderate)**: The paper tests 4 models, of which 3 share the Qwen2.5 base architecture (r1-32b, QwQ-32B, OpenThinker-7B). Only 1 model (r1-8b) represents Llama. This is effectively a study of "Qwen2.5-based reasoning models + one Llama model." Claiming "universal" from this sample is a stretch. A true universality claim would require testing across more diverse architectures (Mistral, Gemma, Phi, etc.) and more diverse training procedures (RLHF vs. distillation vs. RL from scratch).

- **14 citations is far below venue expectations (moderate)**: A typical EMNLP main conference empirical paper includes 30-60 references. 14 citations for a paper that claims to bridge hidden-state detection and reasoning model safety — two mature subfields — signals either insufficient literature engagement or deliberate omission. The related work section at 1 page with 3 subsections is thin.

- **Empirical study vs. methodological contribution creates venue fit tension (moderate)**: Top venues (EMNLP Main) typically expect either a novel method OR an empirical study of sufficient depth/scale to constitute a benchmark contribution. This paper offers neither a new method nor a large-scale benchmark. The scale (209 traces per model, 43 test) is small. The methods are standard. The contribution lives in the "findings" space — systematic evaluation revealing consistent patterns — which may be better suited to Findings than Main.

---

### Questions for Authors

1. How do you respond to the concern that "hidden states outperform text features" is the expected outcome from representation theory? What would be the paper's contribution if a reviewer considers this finding unsurprising? Is the magnitude of the gap (16% vs 27-36% FPR) itself surprising, and if so, what prior would have predicted a smaller gap?

2. Have you considered a control task (Hewitt & Liang 2019) to verify that the temporal probe is not simply learning positional heuristics (e.g., "steps near the end of traces are post-commitment")? Given that 41.6% of commitment points fall in the last 10% of traces, positional confounds are a serious concern.

3. Can you establish that detecting the commitment point is causally relevant to preventing harm? Specifically, if you intervene (truncate, steer) at the detected step, does the model actually avoid generating harmful output? Without this causal validation, the detection task may be correlational rather than actionable.

4. Why are fundamental probing methodology works (Belinkov et al. 2017, Conneau et al. 2018, Hewitt & Manning 2019) absent from the related work? These provide the methodological foundation for your entire approach.

5. How do you justify the "universally" claim in the title given that 3 of 4 models share the Qwen2.5 architecture? Would you consider softening to "consistently across architectures" or similar?

6. The paper defines commitment point as "last safety label + 1" from HarmThoughts annotations. How robust is this definition to annotation noise? What is the inter-annotator agreement on the safety labels that determine CP position? If annotations shift by 1-2 steps, your lead time measurements (median=0) become meaningless.

7. Why is the cross-model transfer result presented as a finding rather than being explored in depth? What geometric properties are shared? Does CKA/CCA analysis reveal what structure transfers? This feels like a potentially strong contribution that is underdeveloped.

8. How does this work relate to Process Reward Models (Lightman et al. 2023), which also perform step-level classification on reasoning traces? Could a PRM trained on safety labels serve as both a detector and an intervention trigger?

---

### Preliminary Tendency: Borderline Reject (leaning reject)

**Justification**: The paper addresses a genuine and timely problem, and the cross-architecture consistency of findings provides useful empirical grounding. However, the contribution sits in a difficult position: the methods are not novel (standard probing), the central finding ("hidden states beat text") is largely expected from first principles, the negative result on pre-textual detection may be partially tautological given the task definition, and the related work coverage is inadequate for the claims being made. The "universality" claim is not supported by the model diversity (3/4 models share one architecture). With only 14 citations and no engagement with the probing methodology literature that undergirds the entire approach, the paper appears undercooked for a top venue Main track.

The strongest elements are: (1) the oracle decomposition establishing information-theoretic limits, (2) the consistent cross-architecture patterns with pooled statistics, and (3) the signal geometry insight explaining geometric detector failure. These could anchor a strong Findings paper. For Main track, the paper would need: deeper engagement with related work (30+ citations), causal validation of detection utility, a control task demonstrating the probe learns safety-specific rather than positional information, and either a novel method component or substantially more model diversity to support the "universal" framing.

The gap between this paper's ambition (universal claims, comprehensive cross-architecture evaluation) and its evidence base (209 traces, 4 models with 3 sharing an architecture, 14 citations, standard methods) is the fundamental tension that pushes toward rejection.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-16T21:56:16.408274+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-16T21:56:17.011027+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_2_f461d57a.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-16T21:56:17.463071+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-16T21:56:19.069469+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T203948/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T203948/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/worst/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 1606
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-16T21:56:19.069900+00:00_

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
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
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

_source line 7 · 2026-05-16T21:56:19.120332+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-16T21:56:31.263296+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-16T21:56:31.715242+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-16T21:56:31.765779+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-16T21:56:32.217818+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-16T21:56:32.218165+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 13 · 2026-05-16T21:56:32.770352+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 review form scoring criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 review form scoring criteria dimensions"
  }
}
```

</details>

---


### Tool result

_source line 14 · 2026-05-16T21:56:38.894045+00:00_

Web search results for query: "EMNLP 2026 reviewer guidelines review form criteria"

Links: [{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025)","url":"http://aclrollingreview.org/incentives2025"},{"title":"EMNLP 2026 | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"}]

Based on the search results, I can provide you with information about EMNLP 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

For main vs Findings papers, the main criteria for Findings are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

The review rating scale includes:
- 5 = Consider for Award: papers that could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)
- 2 = Resubmit next cycle: papers that need substantial revisions that can be completed by the next ARR cycle
- 1.5 = Resubmit after next cycle: papers that need substantial revisions that cannot be complet
…[truncated 811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6675
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-16T21:56:39.045135+00:00_

Web search results for query: "ACL ARR 2026 review form scoring criteria dimensions"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL ARR 2026 | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026"}]

Based on the search results, I can provide you with information about the ACL ARR 2026 review form scoring criteria and dimensions:

## Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Key Scoring Criteria:

**1
…[truncated 1005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6274
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-16T21:56:43.795644+00:00_

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
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
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

_source line 17 · 2026-05-16T21:56:43.796027+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-16T21:56:45.753446+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-16T21:56:46.055189+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T203948/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T203948/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/worst/paper.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-16T21:56:46.105881+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-16T21:56:46.156627+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/best/custom.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/median/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-16T21:56:57.419039+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their exact scales (numerical values and descriptions), and any guidance on how to score each dimension. Include soundness, excitement, overall recommendation, and any other scored fields."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their exact scales (numerical values and descriptions), and any guidance on how to score each dimension. Include soundness, excitement, overall recommendation, and any other scored fields."
  }
}
```

</details>

---


### Tool call

_source line 23 · 2026-05-16T21:56:57.971266+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.pdf",
  "pages": "1-5",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.pdf",
    "pages": "1-5",
    "dpi": "200"
  }
}
```

</details>

---


### Tool result

_source line 24 · 2026-05-16T21:57:03.895000+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5: "Positive that my evaluation is correct"
- 4: "Quite sure" with low likelihood of missing important details
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend my evaluation, but fairly likely missed details"
- 1: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- 5: "Excellent: This study is one of the most thorough"
- 4: "Strong: provides sufficient support for all claims"
- 3: "Acceptable: provides sufficient support for main claims"
- 2: "Poor: main claims not sufficiently supported"
- 1: "Major Issues: not sufficiently thorough for publication"

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- 5: "Highly Exciting: would recommend to others"
- 4: "Exciting: would mention to others"
- 3: "Interesting: might mention some points"
- 2: "Potentially Interesting: doesn't resonate with reviewer"
- 1: "Not Exciting: lacks relevance to NLP community"

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- 5: Consider for Award (top 2.5% papers)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle (substantial revisions needed)
- 1: Do not resubmit (fundamental issues)

## 5. **Reproducibility**
Scale: 1-5
- 5: Results easily reproducible
- 4: Mostly reproducible with minor variations
- 3: Reproducible with some difficulty
- 2: Hard to reproduce; limited data availability
- 1: Cannot reproduce results

## 6. **Datasets**
Scale: 1-5
- 5: Enabling impact on research choices
- 4: Useful for ongoing work
- 3: Potentially useful
- 2: Documentary value only
- 1: No usable datasets

## 7. **Software**
Scale: 1-5 (mirrors dataset scoring)

## 8. **Author Identity Knowledge**
Scale: 1-5 (confidentiality check, not quality metric)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6475
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-16T21:57:05.912397+00:00_

Error: result (2,562,366 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-2-f461d57a/c320b57d-134b-4fcd-abaa-18f60670f2c2/tool-results/mcp-agent-ml-research-pdf_to_images-1778968625786.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-2-f461d57a/c320b57d-134b-4fcd-abaa-18f60670f2c2/tool-results/mcp-agent-ml-research-pdf_to_images-1778968625786.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-2-f461d57a/c320b57d-134b-4fcd-abaa-18f60670f2c2/tool-results/mcp-agent-ml-research-pdf_to_images-1778968625786.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7941
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-16T21:57:13.800899+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*_pdf_images/**/*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*_pdf_images/**/*.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-16T21:57:17.815714+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p5.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 4014
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-16T21:57:18.619799+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best -name \"*.png\" 2>/dev/null | sort",
  "description": "Find PNG images from PDF rendering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best -name \"*.png\" 2>/dev/null | sort",
    "description": "Find PNG images from PDF rendering"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-16T21:57:18.821405+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p5.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-16T21:57:25.847397+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.pdf 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Get PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.pdf 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Get PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-16T21:57:25.948228+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Sat May 16 21:42:43 2026 UTC
ModDate:         Sat May 16 21:42:43 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           10
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       156030 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-16T21:57:31.669719+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.pdf",
  "pages": "6-10",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.pdf",
    "pages": "6-10",
    "dpi": "200"
  }
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-16T21:57:32.173579+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-16T21:57:32.827700+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-16T21:57:33.381866+00:00_

Error: result (1,938,687 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-2-f461d57a/c320b57d-134b-4fcd-abaa-18f60670f2c2/tool-results/mcp-agent-ml-research-pdf_to_images-1778968653205.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-2-f461d57a/c320b57d-134b-4fcd-abaa-18f60670f2c2/tool-results/mcp-agent-ml-research-pdf_to_images-1778968653205.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-2-f461d57a/c320b57d-134b-4fcd-abaa-18f60670f2c2/tool-results/mcp-agent-ml-research-pdf_to_images-1778968653205.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1712
}
```

</details>

---


### Tool result

_source line 36 · 2026-05-16T21:57:36.951474+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4123
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-16T21:57:37.002734+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4829
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-16T21:57:44.004943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-16T21:57:45.009125+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-16T21:57:45.514272+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-16T21:57:46.072798+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2067
}
```

</details>

---


### Tool result

_source line 42 · 2026-05-16T21:57:48.452338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3443
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-16T21:57:48.705536+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3191
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-16T21:57:53.632713+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/_pdf_images/paper_p*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/_pdf_images/paper_p*.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-16T21:57:53.683775+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p8.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p10.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-16T21:57:57.197699+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 47 · 2026-05-16T21:57:58.202276+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 48 · 2026-05-16T21:57:58.810042+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1612
}
```

</details>

---


### Tool call

_source line 49 · 2026-05-16T21:57:59.163345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-16T21:57:59.818416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 51 · 2026-05-16T21:57:59.971869+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/_pdf_images/paper_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 52 · 2026-05-16T21:58:01.140263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2937
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-16T21:58:01.191987+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1220
}
```

</details>

---


### Tool result

_source line 54 · 2026-05-16T21:58:02.450746+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2632
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-16T21:58:02.451541+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3288
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-16T21:58:35.004468+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-16T21:58:35.708275+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"未找到 .bib 文件: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-16T21:58:35.708734+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.tex"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-16T21:58:35.960283+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	\usepackage{natbib}
13	\usepackage{hyperref}
14	
15	\newcommand{\method}{ContrastiveTrace}
16	\newcommand{\dataset}{HarmThoughts}
17	
18	\title{Hidden States Universally Encode Safety Commitment Better Than Text:\\A Cross-Architecture Evaluation of Reasoning Model Monitoring}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	Reasoning models (e.g., DeepSeek-R1, QwQ) exhibit ``self-jailbreak,'' where extended chain-of-thought (CoT) reasoning culminates in a commitment point at which safety reasoning permanently ceases and harmful content generation begins. Existing hidden-state detectors target adversarial inputs on standard language models and have never been evaluated on this internal reasoning failure mode. We present the first systematic cross-architecture evaluation of safety commitment detection, comparing hidden-state probes, text-based monitors, and unsupervised geometric methods across four reasoning models spanning two architecture families (Llama, Qwen2.5) and two scales (7--8B, 32B). Our pooled three-model analysis (p=0.003, $I^2$=0.12) establishes that hidden-state temporal probes achieve pre-commitment false positive rates of 14--16\%, compared to 27--36\% for text-based probes, a precision advantage that is consistent across all tested architectures. Temporal context (window size $W$=15) universally improves coverage by 5--7 percentage points regardless of modality. However, pre-textual detection remains fundamentally unreliable: median detection lead is 0 steps across all models, with only 38--45\% of detections preceding the textual commitment point. Cross-model transfer experiments reveal shared safety geometry across arch
…[truncated 30216 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-16T22:00:01.002757+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL fields, ALL scoring scales with exact numerical values and their text descriptions. Include: soundness scale (each level 1-5 with description), excitement scale (each level 1-5 with description), overall assessment scale (each level with description), confidence scale, reproducibility, and any other scored dimensions. Also extract any guidance text about what makes a paper suitable for Main conference vs Findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL fields, ALL scoring scales with exact numerical values and their text descriptions. Include: soundness scale (each level 1-5 with description), excitement scale (each level 1-5 with description), overall assessment scale (each level with description), confidence scale, reproducibility, and any other scored dimensions. Also extract any guidance text about what makes a paper suitable for Main conference vs Findings."
  }
}
```

</details>

---


### Tool call

_source line 61 · 2026-05-16T22:00:02.660037+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what constitutes a strong vs weak paper, how to assess novelty, how to assess related work adequacy, what makes a paper suitable for Main conference vs Findings, ethical considerations, and any specific guidance on empirical papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what constitutes a strong vs weak paper, how to assess novelty, how to assess related work adequacy, what makes a paper suitable for Main conference vs Findings, ethical considerations, and any specific guidance on empirical papers."
  }
}
```

</details>

---


### Tool result

_source line 62 · 2026-05-16T22:00:07.197319+00:00_

# ACL Rolling Review Form - Complete Scoring Scales

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: does not resonate with me."

## Overall Assessment
- **5**: Consider for Award (top 2.5%)
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings acceptance (emphasis on "soundness and reproducibility")
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## Reproducibility
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results."
- **1**: "They would not be able to reproduce the results."

## Datasets & Software
Both use identical 5-point scales from "Enabling" (5) to "No
…[truncated 33 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6194
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-16T22:00:14.516858+00:00_

# ARR Reviewer Guidelines: Key Assessment Criteria

## Strong vs. Weak Papers

**Strong papers demonstrate:**
- Clear research questions with appropriate scope for their contribution type
- Sufficient evidence supporting all claims made
- Technical soundness and valid argumentation
- Appropriate methodology choices linked to research goals

**Weak papers typically exhibit:**
- Unclear or overclaimed contributions (R4)
- Insufficient justification for methodological choices (M4)
- Missing or misrepresented related work (G3)
- Vague key terms left undefined (G4)

## Novelty Assessment

The guidelines caution against dismissing work as "not novel" without evidence. Key points:

- Novel work is often harder to publish; reviewers should avoid unnecessary conservatism (H4)
- Contribution types beyond modeling—resources, analyses, reproductions, surveys—deserve fair evaluation
- Missing references to prior work only constitute a weakness if that work was "published (not preprinted) 3+ months before" the deadline (H12)

## Related Work Adequacy

Authors must fairly represent prior contributions and clarify their work's novelty relative to it (G3). However:

- "Missing recent baselines" requires specificity about which methods should be included and why
- Requests for comparisons to closed-source LLMs are only justified "if it directly bears on the claim the authors are making" (H14)

## Main Conference vs. Findings Distinction

The guidelines note both venues require "sufficient soundness and reproducibility," but the main conference may prioritize impact and novelty more heavily. Papers with significant practical contributions—efficiency improvements or high-quality resources for underserved languages—merit consideration even without maximum novelty.

## Ethical Considerations

**Key obligations:**
- Confidentiality of submissions; avoid uploading materials to "non-privacy-preserving" AI tools
- Double-blind review requires not actively seeking author identity; postpone re
…[truncated 1301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 11856
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-16T22:03:34.667397+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 (R2): Novelty and Related Work Assessment\n\n**Paper**: \"Hidden States Universally Encode Safety Commitment Better Than Text: A Cross-Architecture Evaluation of Reasoning Model Monitoring\"\n\n**审稿依据**: ACL ARR Review Form (2026)，重点聚焦 novelty 和 related work 维度。\n\n---\n\n## 总体评分\n\n**Overall**: 2.5/5 (Borderline Findings)\n**一句话总结**: 论文定位了一个真实且重要的问题（推理模型自我越狱的 commitment point 检测），实验设计合理、统计分析扎实，但核心发现缺乏惊喜性，方法论无新意，related work 覆盖严重不足（仅 14 篇引用），且 \"universally\" 的声称与实际模型多样性不匹配。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 实验方法论基本合理：bootstrap pooled analysis、I²异质性检验、5-seed GRU 稳定性报告均为正面。但缺少 control task 以排除位置混淆因素，且 oracle decomposition 的方法学细节不清。 |\n| Excitement | 2/5 | 核心发现（HS优于text）从表征理论角度是预期结果；方法均为标准工具的直接应用；pre-textual detection 的负结果有价值但部分受限于任务定义。 |\n| Overall | 2.5/5 | 介于 Borderline Findings 和 Findings 之间。需要大幅补充 related work、修正 overclaim、增加 control task。 |\n| Confidence | 4/5 | 熟悉 probing classifier 文献和 LLM 安全检测方向。 |\n| Reproducibility | 3/5 | 模型和数据集有名称但未提供代码；超参数部分说明（layer sweep、W sweep）；HarmThoughts 数据集的标注协议未在论文中详细描述。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Related Work 覆盖严重不足，缺失本文方法论的奠基文献\n\n- 具体位置：Section 2（Related Work，仅 1 页 3 段），References（14 篇）\n- 问题：论文的核心方法是在 transformer hidden states 上训练 logistic regression / GRU 探针做分类。这正是 **probing classifiers** 范式的直接应用，但以下奠基工作完全未被引用：\n  - Belinkov et al. (2017) \"What do neural machine translation models learn about morphology?\" — 开创了 hidden-state probing 范式\n  - Conneau et al. (2018) \"What you can cram into a single $&!#* vector\" — 系统评估 probing 方法论\n  - Hewitt & Manning (2019) \"A structural probe for finding syntax in word representations\" — probing 分析的标准参考\n  - **Hewitt & Liang (2019) \"Designing and interpreting probes with control tasks\"** — 提出 control task 来验证 probe 是否学到了目标属性而非数据伪相关。**这对本文至关重要**（详见 N2）。\n  \n  此外，以下相关方向也缺失：\n  - Activation patching / causal tracing (Meng et al. 2022, Conmy et al. 2023) — 建立 hidden state 与行为之间的因果关系（非仅相关性）\n  - 更广泛的 jailbreak detection 文献 (SmoothLLM, perplexity-based methods)\n  - 更丰富的 change-point detection 文献（论文仅评估 BOCPD 和 CUSUM 两种方法）\n  - Cross-model probe transfer 的已有研究 (Conneau et al. 2020 跨语言 probe 迁移, CKA/CCA 表征相似性分析)\n\n- 为什么影响接收：ACL/EMNLP 实证论文通常引用 30-60 篇。14 篇引用对于一篇横跨 hidden-state probing 和 reasoning model safety 两个成熟子领域的论文来说，显示出文献调研的明显不足。审稿人（包括我）会质疑作者是否充分了解自己方法的学术脉络。ARR reviewer guidelines 明确要求 \"Authors must fairly represent prior contributions and clarify their work's novelty relative to it.\"\n- 建议修改方向：(1) 增加一个 \"Probing Classifiers\" 子段落，讨论 probe 方法论传统及本文在其中的定位；(2) 讨论 causal vs correlational 的区别并明确本文的贡献边界；(3) 引用量至少达到 30 篇以上。\n\n**N2** [critical] 缺少 Control Task，无法排除位置混淆因素\n\n- 具体位置：Section 4.1（Methods - Hidden-State Probes），Section 6.2（Layer Selection Ablation）\n- 问题：Hewitt & Liang (2019) 提出的 control task 方法论对本文高度相关。论文定义 commitment point 为 \"safety reasoning permanently ceases\" 的第一步（Section 3.1, line 64），这意味着 CP 在 trace 中的位置可能与 trace 长度强相关（长 trace 中 CP 趋向于出现在中后段）。论文使用的 temporal probe 的输入包含 positional encoding 信息（通过 hidden states 隐含传递），因此一个严重的混淆可能是：probe 并没有学到 \"safety commitment state\"，而是学到了 \"trace 的相对位置\"。\n\n  论文提供了 209 traces/model，每条 20-80 步（Section 3.3），但完全没有报告 CP 位置的分布统计。如果 CP 集中在 trace 后半段，那么 probe 的准确率可能部分源于位置启发式而非安全状态信息。\n\n  一个标准的验证方式是：构造 control task（例如用随机的 CP 位置标签训练 probe），如果 control probe 达到接近实际 probe 的准确率，则实际 probe 的 selectivity 存疑。\n- 为什么影响接收：这是方法论层面的根本性遗漏。没有 control task，论文无法区分 probe 学到的是 safety-specific 信息还是 positional heuristics。这直接影响 Finding 1（HS 优于 text）的可信度——如果 HS probe 比 text probe 好只是因为 hidden states 更好地编码了位置信息，核心结论就需要重新解释。\n- 建议修改方向：(1) 报告 CP 位置在 trace 中的分布；(2) 实施 Hewitt & Liang 2019 风格的 control task；(3) 如果 control selectivity 低，这反而能加强论文的 claim。\n\n**N3** [critical] 标题和正文中 \"Universally\" 的声称与模型多样性不匹配\n\n- 具体位置：Title, Abstract (line 26), Section 7 Discussion (line 400-401), Section 8 Conclusion (line 413-414)\n- 问题：论文测试了 4 个模型：r1-8b (Llama), r1-32b (Qwen2.5), QwQ-32B (Qwen2.5), OpenThinker-7B (Qwen2.5)。其中 3/4 基于 Qwen2.5 架构。Table 8 (2×2 architecture × scale matrix) 中 4 个格子有 3 个是 Qwen2.5。这不构成对 \"universal\" 的充分支撑。\n\n  \"Universal\" 意味着跨架构的普遍性，需要在 Llama, Qwen, Mistral, Gemma, Phi 等多样架构上验证。目前的证据支撑的是 \"consistent across Qwen2.5-based reasoning models and one Llama model\"。\n\n  ARR reviewer guidelines 明确警告：\"Appropriately scope claims to evaluated samples—a few QA benchmarks ≠ general 'reasoning' capability.\"\n- 为什么影响接收：Overclaimed contribution 是 ARR 审稿中的常见 reject 原因 (H12/R4)。标题级别的 overclaim 尤其敏感。\n- 建议修改方向：将 \"Universally\" 改为 \"Consistently Across Architectures\" 或 \"Across Multiple Architecture Families\"。在 Limitations 中明确承认 Qwen2.5 偏重的问题。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"Hidden states 优于 text\" 是预期结果，论文未充分论证其贡献的非显然性\n\n- 具体位置：Abstract (Finding 1), Section 5.1, Table 6\n- 问题：Hidden states 是 text 的因果前件——text 是 hidden states 经 unembedding 层的有损投影。因此 hidden states 编码的信息严格多于 surface text。Probing 文献（Belinkov et al. 2017 起）已反复确认 hidden representations 比 surface features 更好地编码各类语言和语义属性。本文 Finding 1 的方向（HS 优于 text）从信息论角度是默认预期。\n\n  论文需要论证的不是 \"HS 比 text 好\" 这一方向，而是：(a) gap 的大小是否出乎意料（14-16% vs 27-36% FPR，即约 2 倍差距——这个量级是否有实践意义？是否有先验预期？），或 (b) 在这个特定任务（reasoning trace 中的 commitment detection）中有什么独特性使得这一比较有新价值。\n\n  当前论文将此作为 \"core finding\"，但从 reviewer 角度，这更像是一个 calibration measurement 而非 discovery。\n- 建议：在 Discussion 中显式讨论为什么这个定量对比在推理模型安全这个特定语境下有独立价值。例如：text-based monitors 在部署中成本更低，因此定量确认 HS 的精确度优势（以及何时这个优势重要到值得承担 HS extraction 的额外成本）是有实践价值的。\n\n**W2** [warning] Probing 是相关性而非因果性，论文缺少因果验证的讨论\n\n- 具体位置：Section 4 (Methods), Section 7 (Discussion - Practical implications)\n- 问题：论文的 probe 建立的是 hidden states 与 CP labels 之间的相关性，而非因果关系。Section 7 的 \"Practical implications\" 段落建议 \"hidden-state temporal probes at layer 44% with W=15 provide the best precision/coverage tradeoff\"，但从未验证：如果在检测到的时间步进行干预（截断、steering、重采样），模型是否真的会避免生成有害输出？\n\n  Activation patching (Meng et al. 2022) 和 causal tracing 技术可以建立这种因果链接。如果 probe 检测到 post-CP 但干预无效，那么检测的实际部署价值就存疑。\n\n  论文不需要实施完整的因果验证，但应在 Discussion/Limitations 中明确承认这一 gap 并讨论其影响。\n- 建议：在 Limitations 段落增加因果验证的讨论；将 \"Practical implications\" 的措辞从 \"provide the best tradeoff\" 调整为 \"suggest promising candidates for future intervention studies\"。\n\n**W3** [warning] Process Reward Models (PRMs) 与本文任务的结构性联系未被探索\n\n- 具体位置：Section 2 (Related Work, Change-point detection paragraph), References [prm]\n- 问题：Lightman et al. (2023) 被引用但仅作为 \"score individual reasoning steps\" 一笔带过。事实上，PRMs 在 reasoning traces 上进行逐步分类，这与本文的 commitment point detection 在任务结构上高度相似——都是 step-level binary classification on reasoning traces。\n\n  本文未讨论的关键问题：(1) 能否用 safety-labeled PRM 同时完成检测和干预？(2) PRM 的训练数据量级（通常远大于 209 traces）对 probe 性能有何影响？(3) PRM 文献中关于 outcome supervision vs process supervision 的发现是否适用于 commitment detection？\n  \n  Uesato et al. (2022) 和 Wang et al. (2023, Math-Shepherd) 等 process supervision 工作也完全缺失。\n- 建议：在 Related Work 中增加关于 PRMs 和 process supervision 的讨论段落，明确论述二者的结构相似性和差异。\n\n**W4** [warning] Cross-model transfer 结果有价值但分析不够深入\n\n- 具体位置：Section 4.4, Section 5.3, Table 3\n- 问题：67-74% 的跨模型迁移准确率（vs 50% chance）是一个有趣的发现，within-family (73-74%) vs cross-family (68-71%) 的差距提供了清晰的分解。但分析止步于报告数字——没有回答 \"为什么 transfer work？\"\n\n  具体缺失：(1) 什么几何结构是共享的？CKA (Kornblith et al. 2019) 或 CCA 分析可以量化表征空间的结构相似性。(2) transfer 性能与哪些因素相关——训练数据来源、蒸馏 teacher 模型、RLHF vs 蒸馏训练方式？(3) 论文提到用 \"learned linear projection head\" (Section 4.4) 做维度映射，但 projection head 的训练需要多少对齐数据？这个细节没有交代。\n\n  这个 finding 如果深入分析，可能是论文最有价值的贡献，但当前以 \"supplementary finding\" 的方式呈现浪费了其潜力。\n- 建议：增加表征相似性分析（CKA/CCA），讨论 transfer 的 mechanism 而非仅报告 accuracy。\n\n**W5** [warning] Oracle decomposition 方法学不清晰\n\n- 具体位置：Section 5.7, Table 7\n- 问题：Table 7 将 probe 与 oracle 之间的 gap 分解为三个来源：Future labels (62%), Multi-step trajectory (28%), Global trace context (10%)。但论文未详细说明这个分解是如何计算的。具体问题：\n  - \"Future labels (K-step)\" 的 K 是多少？如何从 62% 这个数字得到？\n  - \"Multi-step trajectory: 28%, Probe Access: Partial\" 中 \"Partial\" 的含义和量化依据是什么？\n  - 三个 source 的加和恰好为 100%，这是分解方法的性质还是近似？\n  - 这个分解是否在多个模型上计算？各模型的分解比例是否一致？\n\n  作为论文的关键分析之一（支撑 Finding 3），方法学透明度不足。\n- 建议：在正文或 Appendix 中详细说明 oracle decomposition 的计算过程和各分量的定义。\n\n---\n\n## 小问题（不影响接收）\n\n- **格式**：论文使用 `\\documentclass[11pt,a4paper]{article}` 而非 ACL/EMNLP 官方模板 (acl_natbib.sty)，margin 设置 (`\\usepackage[margin=1in]{geometry}`) 与 ACL 格式不一致。如果目标是 EMNLP 投稿，需要切换到官方模板。\n- **OpenThinker-7B 使用不一致**：Section 3.3 列出了 4 个模型，但 Tables 1-6 主要只报告 r1-8b、r1-32b、QwQ-32B 三个模型。OpenThinker-7B 仅在 Table 8 出现。如果声称 4 模型评估，应在所有主要表格中包含 OpenThinker-7B。\n- **引用格式**：References 中多条使用 \"et al.\" 缩写而非列出完整作者列表，不符合 ACL 引用规范 (natbib 风格)。部分引用缺少 arXiv ID（如 HarmThoughts, Self-jailbreaking, SIREN, SafeRemind, SafeThink）。\n- **Appendix 内容稀少**：Appendix A 仅包含 6 条置信区间数据和 Table 12。对于 10 页论文，Appendix 可以承载更多实验细节（CP 位置分布、完整的 per-model 消融结果、text probe 详细结果等）。\n- **Abstract 中 \"pooled p=0.003\" 的 p 值来源**：Abstract 引用 pooled p=0.003，Table 6 确认该值，但 bootstrap resampling 的 p 值计算方式未在方法论中说明。\n\n---\n\n## 主要优势\n\n- **问题定位准确**：识别了 reasoning model self-jailbreak 与传统 adversarial attack 的本质区别（内部推理失败 vs 外部攻击），commitment point 作为检测目标的形式化是合理的。\n- **实验设计系统**：2×2 (architecture × scale) design、pooled bootstrap analysis with I² heterogeneity test、多种方法 head-to-head 比较的实验框架质量高。\n- **有价值的负结果**：geometric methods (TrajGuard/Mahalanobis) 的普遍失败（Table 5, max Δ < 0.025）配合 Fisher ratio 分析（full space 18-19 → PCA-3 约 1.0）给出了可操作的解释，对后续工作有指导意义。\n- **统计严谨性**：I²=0.08-0.21 的低异质性、bootstrap CIs（Appendix A）、5-seed GRU 稳定性报告等体现了良好的统计实践。\n\n---\n\n## 对 Director 的额外说明\n\n1. **关于任务消息中提供的 review 草稿**：Director 转发的 review 草稿总体方向正确，但有几处与论文实际内容不符：\n   - 草稿提到 \"mutual information analysis (MI=0.42 for current state, MI→0.03 for future labels)\"——论文中 **不存在** MI 分析，论文使用的是 oracle decomposition (Table 7)。\n   - 草稿称 \"Fisher ~17-18\"，论文实际报告 \"18-19\"（Section 5.1）。\n   - 草稿提到 \"41.6% of commitment points fall in the last 10% of traces\"——论文中 **无此统计**。\n   - 草稿引用 \"Frank (2603.18280)\"——这不是有效的 arXiv ID 格式，疑似幻觉引用。\n\n2. **与 ARR reviewer guidelines 的对齐**：ARR guidelines 明确警告 \"reviewers should avoid unnecessary conservatism\" on novelty，且 \"Criticizing negative results or simple solutions when they soundly answer the research question\" 是应避免的 pitfall。本文的负结果（pre-textual detection unreliable）和简单方法（LR probe）如果确实能 soundly answer the research question，不应因为 \"not novel enough\" 而被否定。但前提是 related work coverage 和 overclaim 问题得到修复。\n\n3. **Findings vs Main 的建议**：当前版本在补充 related work（N1）、增加 control task（N2）、修正 overclaim（N3）后，可以达到 Findings 水平。如果进一步深化 cross-model transfer 分析（W4）并增加模型多样性（至少加入 1-2 个非 Qwen2.5 模型），则可考虑 Main track。\n",
  "reviewer_id": "2",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 (R2): Novelty and Related Work Assessment\n\n**Paper**: \"Hidden States Universally Encode Safety Commitment Better Than Text: A Cross-Architecture Evaluation of Reasoning Model Monitoring\"\n\n**审稿依据**: ACL ARR Review Form (2026)，重点聚焦 novelty 和 related work 维度。\n\n---\n\n## 总体评分\n\n**Overall**: 2.5/5 (Borderline Findings)\n**一句话总结**: 论文定位了一个真实且重要的问题（推理模型自我越狱的 commitment point 检测），实验设计合理、统计分析扎实，但核心发现缺乏惊喜性，方法论无新意，related work 覆盖严重不足（仅 14 篇引用），且 \"universally\" 的声称与实际模型多样性不匹配。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 实验方法论基本合理：bootstrap pooled analysis、I²异质性检验、5-seed GRU 稳定性报告均为正面。但缺少 control task 以排除位置混淆因素，且 oracle decomposition 的方法学细节不清。 |\n| Excitement | 2/5 | 核心发现（HS优于text）从表征理论角度是预期结果；方法均为标准工具的直接应用；pre-textual detection 的负结果有价值但部分受限于任务定义。 |\n| Overall | 2.5/5 | 介于 Borderline Findings 和 Findings 之间。需要大幅补充 related work、修正 overclaim、增加 control task。 |\n| Confidence | 4/5 | 熟悉 probing classifier 文献和 LLM 安全检测方向。 |\n| Reproducibility | 3/5 | 模型和数据集有名称但未提供代码；超参数部分说明（layer sweep、W sweep）；HarmThoughts 数据集的标注协议未在论文中详细描述。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Related Work 覆盖严重不足，缺失本文方法论的奠基文献\n\n- 具体位置：Section 2（Related Work，仅 1 页 3 段），References（14 篇）\n- 问题：论文的核心方法是在 transformer hidden states 上训练 logistic regression / GRU 探针做分类。这正是 **probing classifiers** 范式的直接应用，但以下奠基工作完全未被引用：\n  - Belinkov et al. (2017) \"What do neural machine translation models learn about morphology?\" — 开创了 hidden-state probing 范式\n  - Conneau et al. (2018) \"What you can cram into a single $&!#* vector\" — 系统评估 probing 方法论\n  - Hewitt & Manning (2019) \"A structural probe for finding syntax in word representations\" — probing 分析的标准参考\n  - **Hewitt & Liang (2019) \"Designing and interpreting probes with control tasks\"** — 提出 control task 来验证 probe 是否学到了目标属性而非数据伪相关。**这对本文至关重要**（详见 N2）。\n  \n  此外，以下相关方向也缺失：\n  - Activation patching / causal tracing (Meng et al. 2022, Conmy et al. 2023) — 建立 hidden state 与行为之间的因果关系（非仅相关性）\n  - 更广泛的 jailbreak detection 文献 (SmoothLLM, perplexity-based methods)\n  - 更丰富的 change-point detection 文献（论文仅评估 BOCPD 和 CUSUM 两种方法）\n  - Cross-model probe transfer 的已有研究 (Conneau et al. 2020 跨语言 probe 迁移, CKA/CCA 表征相似性分析)\n\n- 为什么影响接收：ACL/EMNLP 实证论文通常引用 30-60 篇。14 篇引用对于一篇横跨 hidden-state probing 和 reasoning model safety 两个成熟子领域的论文来说，显示出文献调研的明显不足。审稿人（包括我）会质疑作者是否充分了解自己方法的学术脉络。ARR reviewer guidelines 明确要求 \"Authors must fairly represent prior contributions and clarify their work's novelty relative to it.\"\n- 建议修改方向：(1) 增加一个 \"Probing Classifiers\" 子段落，讨论 probe 方法论传统及本文在其中的定位；(2) 讨论 causal vs correlational 的区别并明确本文的贡献边界；(3) 引用量至少达到 30 篇以上。\n\n**N2** [critical] 缺少 Control Task，无法排除位置混淆因素\n\n- 具体位置：Section 4.1（Methods - Hidden-State Probes），Section 6.2（Layer Selection Ablation）\n- 问题：Hewitt & Liang (2019) 提出的 control task 方法论对本文高度相关。论文定义 commitment point 为 \"safety reasoning permanently ceases\" 的第一步（Section 3.1, line 64），这意味着 CP 在 trace 中的位置可能与 trace 长度强相关（长 trace 中 CP 趋向于出现在中后段）。论文使用的 temporal probe 的输入包含 positional encoding 信息（通过 hidden states 隐含传递），因此一个严重的混淆可能是：probe 并没有学到 \"safety commitment state\"，而是学到了 \"trace 的相对位置\"。\n\n  论文提供了 209 traces/model，每条 20-80 步（Section 3.3），但完全没有报告 CP 位置的分布统计。如果 CP 集中在 trace 后半段，那么 probe 的准确率可能部分源于位置启发式而非安全状态信息。\n\n  一个标准的验证方式是：构造 control task（例如用随机的 CP 位置标签训练 probe），如果 control probe 达到接近实际 probe 的准确率，则实际 probe 的 selectivity 存疑。\n- 为什么影响接收：这是方法论层面的根本性遗漏。没有 control task，论文无法区分 probe 学到的是 safety-specific 信息还是 positional heuristics。这直接影响 Finding 1（HS 优于 text）的可信度——如果 HS probe 比 text probe 好只是因为 hidden states 更好地编码了位置信息，核心结论就需要重新解释。\n- 建议修改方向：(1) 报告 CP 位置在 trace 中的分布；(2) 实施 Hewitt & Liang 2019 风格的 control task；(3) 如果 control selectivity 低，这反而能加强论文的 claim。\n\n**N3** [critical] 标题和正文中 \"Universally\" 的声称与模型多样性不匹配\n\n- 具体位置：Title, Abstract (line 26), Section 7 Discussion (line 400-401), Section 8 Conclusion (line 413-414)\n- 问题：论文测试了 4 个模型：r1-8b (Llama), r1-32b (Qwen2.5), QwQ-32B (Qwen2.5), OpenThinker-7B (Qwen2.5)。其中 3/4 基于 Qwen2.5 架构。Table 8 (2×2 architecture × scale matrix) 中 4 个格子有 3 个是 Qwen2.5。这不构成对 \"universal\" 的充分支撑。\n\n  \"Universal\" 意味着跨架构的普遍性，需要在 Llama, Qwen, Mistral, Gemma, Phi 等多样架构上验证。目前的证据支撑的是 \"consistent across Qwen2.5-based reasoning models and one Llama model\"。\n\n  ARR reviewer guidelines 明确警告：\"Appropriately scope claims to evaluated samples—a few QA benchmarks ≠ general 'reasoning' capability.\"\n- 为什么影响接收：Overclaimed contribution 是 ARR 审稿中的常见 reject 原因 (H12/R4)。标题级别的 overclaim 尤其敏感。\n- 建议修改方向：将 \"Universally\" 改为 \"Consistently Across Architectures\" 或 \"Across Multiple Architecture Families\"。在 Limitations 中明确承认 Qwen2.5 偏重的问题。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"Hidden states 优于 text\" 是预期结果，论文未充分论证其贡献的非显然性\n\n- 具体位置：Abstract (Finding 1), Section 5.1, Table 6\n- 问题：Hidden states 是 text 的因果前件——text 是 hidden states 经 unembedding 层的有损投影。因此 hidden states 编码的信息严格多于 surface text。Probing 文献（Belinkov et al. 2017 起）已反复确认 hidden representations 比 surface features 更好地编码各类语言和语义属性。本文 Finding 1 的方向（HS 优于 text）从信息论角度是默认预期。\n\n  论文需要论证的不是 \"HS 比 text 好\" 这一方向，而是：(a) gap 的大小是否出乎意料（14-16% vs 27-36% FPR，即约 2 倍差距——这个量级是否有实践意义？是否有先验预期？），或 (b) 在这个特定任务（reasoning trace 中的 commitment detection）中有什么独特性使得这一比较有新价值。\n\n  当前论文将此作为 \"core finding\"，但从 reviewer 角度，这更像是一个 calibration measurement 而非 discovery。\n- 建议：在 Discussion 中显式讨论为什么这个定量对比在推理模型安全这个特定语境下有独立价值。例如：text-based monitors 在部署中成本更低，因此定量确认 HS 的精确度优势（以及何时这个优势重要到值得承担 HS extraction 的额外成本）是有实践价值的。\n\n**W2** [warning] Probing 是相关性而非因果性，论文缺少因果验证的讨论\n\n- 具体位置：Section 4 (Methods), Section 7 (Discussion - Practical implications)\n- 问题：论文的 probe 建立的是 hidden states 与 CP labels 之间的相关性，而非因果关系。Section 7 的 \"Practical implications\" 段落建议 \"hidden-state temporal probes at layer 44% with W=15 provide the best precision/coverage tradeoff\"，但从未验证：如果在检测到的时间步进行干预（截断、steering、重采样），模型是否真的会避免生成有害输出？\n\n  Activation patching (Meng et al. 2022) 和 causal tracing 技术可以建立这种因果链接。如果 probe 检测到 post-CP 但干预无效，那么检测的实际部署价值就存疑。\n\n  论文不需要实施完整的因果验证，但应在 Discussion/Limitations 中明确承认这一 gap 并讨论其影响。\n- 建议：在 Limitations 段落增加因果验证的讨论；将 \"Practical implications\" 的措辞从 \"provide the best tradeoff\" 调整为 \"suggest promising candidates for future intervention studies\"。\n\n**W3** [warning] Process Reward Models (PRMs) 与本文任务的结构性联系未被探索\n\n- 具体位置：Section 2 (Related Work, Change-point detection paragraph), References [prm]\n- 问题：Lightman et al. (2023) 被引用但仅作为 \"score individual reasoning steps\" 一笔带过。事实上，PRMs 在 reasoning traces 上进行逐步分类，这与本文的 commitment point detection 在任务结构上高度相似——都是 step-level binary classification on reasoning traces。\n\n  本文未讨论的关键问题：(1) 能否用 safety-labeled PRM 同时完成检测和干预？(2) PRM 的训练数据量级（通常远大于 209 traces）对 probe 性能有何影响？(3) PRM 文献中关于 outcome supervision vs process supervision 的发现是否适用于 commitment detection？\n  \n  Uesato et al. (2022) 和 Wang et al. (2023, Math-Shepherd) 等 process supervision 工作也完全缺失。\n- 建议：在 Related Work 中增加关于 PRMs 和 process supervision 的讨论段落，明确论述二者的结构相似性和差异。\n\n**W4** [warning] Cross-model transfer 结果有价值但分析不够深入\n\n- 具体位置：Section 4.4, Section 5.3, Table 3\n- 问题：67-74% 的跨模型迁移准确率（vs 50% chance）是一个有趣的发现，within-family (73-74%) vs cross-family (68-71%) 的差距提供了清晰的分解。但分析止步于报告数字——没有回答 \"为什么 transfer work？\"\n\n  具体缺失：(1) 什么几何结构是共享的？CKA (Kornblith et al. 2019) 或 CCA 分析可以量化表征空间的结构相似性。(2) transfer 性能与哪些因素相关——训练数据来源、蒸馏 teacher 模型、RLHF vs 蒸馏训练方式？(3) 论文提到用 \"learned linear projection head\" (Section 4.4) 做维度映射，但 projection head 的训练需要多少对齐数据？这个细节没有交代。\n\n  这个 finding 如果深入分析，可能是论文最有价值的贡献，但当前以 \"supplementary finding\" 的方式呈现浪费了其潜力。\n- 建议：增加表征相似性分析（CKA/CCA），讨论 transfer 的 mechanism 而非仅报告 accuracy。\n\n**W5** [warning] Oracle decomposition 方法学不清晰\n\n- 具体位置：Section 5.7, Table 7\n- 问题：Table 7 将 probe 与 oracle 之间的 gap 分解为三个来源：Future labels (62%), Multi-step trajectory (28%), Global trace context (10%)。但论文未详细说明这个分解是如何计算的。具体问题：\n  - \"Future labels (K-step)\" 的 K 是多少？如何从 62% 这个数字得到？\n  - \"Multi-step trajectory: 28%, Probe Access: Partial\" 中 \"Partial\" 的含义和量化依据是什么？\n  - 三个 source 的加和恰好为 100%，这是分解方法的性质还是近似？\n  - 这个分解是否在多个模型上计算？各模型的分解比例是否一致？\n\n  作为论文的关键分析之一（支撑 Finding 3），方法学透明度不足。\n- 建议：在正文或 Appendix 中详细说明 oracle decomposition 的计算过程和各分量的定义。\n\n---\n\n## 小问题（不影响接收）\n\n- **格式**：论文使用 `\\documentclass[11pt,a4paper]{article}` 而非 ACL/EMNLP 官方模板 (acl_natbib.sty)，margin 设置 (`\\usepackage[margin=1in]{geometry}`) 与 ACL 格式不一致。如果目标是 EMNLP 投稿，需要切换到官方模板。\n- **OpenThinker-7B 使用不一致**：Section 3.3 列出了 4 个模型，但 Tables 1-6 主要只报告 r1-8b、r1-32b、QwQ-32B 三个模型。OpenThinker-7B 仅在 Table 8 出现。如果声称 4 模型评估，应在所有主要表格中包含 OpenThinker-7B。\n- **引用格式**：References 中多条使用 \"et al.\" 缩写而非列出完整作者列表，不符合 ACL 引用规范 (natbib 风格)。部分引用缺少 arXiv ID（如 HarmThoughts, Self-jailbreaking, SIREN, SafeRemind, SafeThink）。\n- **Appendix 内容稀少**：Appendix A 仅包含 6 条置信区间数据和 Table 12。对于 10 页论文，Appendix 可以承载更多实验细节（CP 位置分布、完整的 per-model 消融结果、text probe 详细结果等）。\n- **Abstract 中 \"pooled p=0.003\" 的 p 值来源**：Abstract 引用 pooled p=0.003，Table 6 确认该值，但 bootstrap resampling 的 p 值计算方式未在方法论中说明。\n\n---\n\n## 主要优势\n\n- **问题定位准确**：识别了 reasoning model self-jailbreak 与传统 adversarial attack 的本质区别（内部推理失败 vs 外部攻击），commitment point 作为检测目标的形式化是合理的。\n- **实验设计系统**：2×2 (architecture × scale) design、pooled bootstrap analysis with I² heterogeneity test、多种方法 head-to-head 比较的实验框架质量高。\n- **有价值的负结果**：geometric methods (TrajGuard/Mahalanobis) 的普遍失败（Table 5, max Δ < 0.025）配合 Fisher ratio 分析（full space 18-19 → PCA-3 约 1.0）给出了可操作的解释，对后续工作有指导意义。\n- **统计严谨性**：I²=0.08-0.21 的低异质性、bootstrap CIs（Appendix A）、5-seed GRU 稳定性报告等体现了良好的统计实践。\n\n---\n\n## 对 Director 的额外说明\n\n1. **关于任务消息中提供的 review 草稿**：Director 转发的 review 草稿总体方向正确，但有几处与论文实际内容不符：\n   - 草稿提到 \"mutual information analysis (MI=0.42 for current state, MI→0.03 for future labels)\"——论文中 **不存在** MI 分析，论文使用的是 oracle decomposition (Table 7)。\n   - 草稿称 \"Fisher ~17-18\"，论文实际报告 \"18-19\"（Section 5.1）。\n   - 草稿提到 \"41.6% of commitment points fall in the last 10% of traces\"——论文中 **无此统计**。\n   - 草稿引用 \"Frank (2603.18280)\"——这不是有效的 arXiv ID 格式，疑似幻觉引用。\n\n2. **与 ARR reviewer guidelines 的对齐**：ARR guidelines 明确警告 \"reviewers should avoid unnecessary conservatism\" on novelty，且 \"Criticizing negative results or simple solutions when they soundly answer the research question\" 是应避免的 pitfall。本文的负结果（pre-textual detection unreliable）和简单方法（LR probe）如果确实能 soundly answer the research question，不应因为 \"not novel enough\" 而被否定。但前提是 related work coverage 和 overclaim 问题得到修复。\n\n3. **Findings vs Main 的建议**：当前版本在补充 related work（N1）、增加 control task（N2）、修正 overclaim（N3）后，可以达到 Findings 水平。如果进一步深化 cross-model transfer 分析（W4）并增加模型多样性（至少加入 1-2 个非 Qwen2.5 模型），则可考虑 Main track。\n",
    "reviewer_id": "2",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-16T22:03:38.435720+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3768
}
```

</details>

---


### Assistant

_source line 66 · 2026-05-16T22:03:48.526000+00:00_

审稿意见已提交给 Review Director。

**审稿结论**: Overall 2.5/5 (Borderline Findings)

三个 Must-Fix 问题：
1. **Related Work 严重不足**（14篇引用，缺失 probing classifier 奠基文献 Belinkov 2017 / Conneau 2018 / Hewitt & Manning 2019 / Hewitt & Liang 2019 等）
2. **缺少 Control Task**（无法排除 probe 学到位置启发式而非安全状态信息的可能）
3. **"Universally" overclaim**（3/4 模型基于 Qwen2.5，不足以支撑"普遍性"声称）

另外发现 Director 转发的 review 草稿中有几处与论文实际内容不符的事实错误（MI 分析不存在、Fisher 数值偏差、CP 位置分布统计不存在、疑似幻觉引用），已在提交中注明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2"
}
```

</details>

---


## Round 2

## Round 2

14 recorded events


### User

_source line 67 · 2026-05-16T22:12:13.901702+00:00_

[Round 1 审稿请求]:
[Round 1 — 交叉分享] 请逐条回应 Reviewer 1 的审稿意见

以下是 R1 的完整审稿原文。请对每个 Must-Fix 和 Should-Fix 逐条标注 `[AGREE]` 或 `[REBUT]`（附简短理由）。关注与你自己发现的重叠、互补或矛盾之处。

---

**R1 Overall**: 2.5/5

**Must-Fix**:

**N1** [critical] 数据划分报告矛盾：Section 3.3 报告 "209 traces (166 train / 43 test)" 但 Section 5.7 写 "n=125 training traces"。166≠125。如果实际是 125/41/43 (60/20/20)，则 validation set 用途（layer/threshold selection）需明确说明以排除 leakage。

**N2** [critical] k=3 pooled meta-analysis 的 I² 统计效力不足——k<5 时 Cochran's Q power 极低，I²=0.12 的 CI 可能从 0% 到 >75%。更严重的是，3 个模型非独立（r1-8b/r1-32b 同源蒸馏，r1-32b/QwQ-32B 共享 base architecture），违反 meta-analysis 独立性假设。

**N3** [critical] "Cross-architecture" 2×2 设计不平衡——Llama 仅 1 个模型（r1-8b），缺 Llama/32B cell，无法分离 architecture vs scale 效应。

**N4** [critical] OpenThinker-7B 数据缺失——声称 4 模型评估，但 pooled analysis 仅用 3 个，排除理由未说明，疑似选择性报告。

**Should-Fix**:

**W1** Hidden state 提取方式未指定（last token? mean pooling? first token?）

**W2** Text baseline 过弱（TF-IDF vs 4096-d hidden states），应加 sentence embeddings / fine-tuned 模型 baseline。

**W3** CP 定义鲁棒性未讨论——是否存在 near-CP oscillation？HarmThoughts IAA 是多少？

**W4** Bootstrap 实施不透明：resampling unit (trace vs step)? CI 类型 (percentile? BCa?)? n=43 的 bootstrap CI 本身不稳定。

**W5** BOCPD baseline 有方法描述无结果数据。

**W6** GRU 5-seed std=9-11% 意味着实践中不可复现，应标记为 exploratory。

**W7** Cross-model transfer 的 projection head 训练数据未说明——如果用了 target model 标注数据则不是 "transfer" 而是 "alignment"。

---

请逐条回应，格式如下：
```
[R1-N1] [AGREE/REBUT] 理由...
[R1-N2] [AGREE/REBUT] 理由...
...
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-16T22:12:28.753967+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.tex",
  "offset": "86",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.tex",
    "offset": "86",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-16T22:12:29.255866+00:00_

86	\item \textbf{OpenThinker-7B}: Qwen2.5-based, 28 layers, comparable scale to r1-8b.
87	\end{itemize}
88	
89	Traces come from the HarmThoughts dataset with 209 traces per model (166 train / 43 test). Each trace contains 20--80 reasoning steps with per-step safety annotations.
90	
91	\section{Methods}
92	
93	\subsection{Hidden-State Probes}
94	
95	\paragraph{Static logistic regression.}
96	For each reasoning step $t$, we extract the hidden state $h_t^{(\ell)}$ at layer $\ell$ and train a logistic regression classifier to predict whether $t \geq \text{CP}$. Layer selection follows a sweep procedure; we find the optimal layer consistently at 44--47\% depth across all models (Table~\ref{tab:layer_ablation}).
97	
98	\paragraph{Temporal logistic regression.}
99	We concatenate hidden states from a window of $W$ consecutive steps: $\mathbf{z}_t = [h_{t-W+1}^{(\ell)}, \ldots, h_t^{(\ell)}]$ and train logistic regression on the concatenated features. The default window $W$=15 captures the critical transition period (Section~\ref{sec:window_ablation}).
100	
101	\paragraph{GRU sequence model.}
102	A GRU with hidden dimension 256 processes the sequence of hidden states from 7 layers (evenly spaced) and predicts commitment state at each step. We report 5-seed mean and standard deviation to quantify training instability.
103	
104	\subsection{Text-Based Probes}
105	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-16T22:12:29.908290+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "125|n=125|training traces",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "125|n=125|training traces",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-16T22:12:29.959030+00:00_

396:GRU achieves higher coverage (78--81\%) but at the cost of substantially higher safe FPR (58--61\% vs. 35--37\% for temporal LR). For deployment scenarios prioritizing precision in the pre-commitment window, temporal LR remains optimal. The coverage variance across seeds (std 9--11\%) confirms that training data scarcity ($n$=125 training traces) prevents stable training of higher-capacity models.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-16T22:12:31.113679+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "BOCPD|bocpd|changepoint|change.point",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "BOCPD|bocpd|changepoint|change.point",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-16T22:12:31.164367+00:00_

37:We address this gap with a systematic evaluation of detection methods for reasoning-model safety commitment. Our evaluation spans four models across two architecture families (Llama-based DeepSeek-R1-Distill-Llama-8B, Qwen2.5-based DeepSeek-R1-Distill-Qwen-32B, QwQ-32B, and OpenThinker-7B) and compares hidden-state probes, text-based monitors, unsupervised geometric detectors, and sequential change-point methods. Three findings emerge consistently across all tested architectures:
58:Bayesian Online Change-Point Detection (BOCPD) \cite{bocpd} and CUSUM \cite{cusum} detect distributional shifts in sequential data. Process Reward Models (PRMs) \cite{prm} score individual reasoning steps. We evaluate BOCPD on hidden-state trajectories as a sequential baseline but find it does not outperform simple temporal probes for pre-commitment detection.
113:\paragraph{BOCPD.}
464:\bibitem[Adams and MacKay(2007)]{bocpd}
466:\newblock Bayesian online changepoint detection.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-16T22:12:45.836770+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "projection|align|transfer.*train|train.*transfer",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "projection|align|transfer.*train|train.*transfer",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-16T22:12:46.288820+00:00_

26:[Omitted long matching line]
47:Additionally, cross-model transfer experiments demonstrate that probes trained on one model achieve 67--74\% accuracy on a different architecture (vs. 50\% chance), revealing shared safety geometry across reasoning models.
118:To test whether safety commitment has shared geometric structure across architectures, we train probes on one model and evaluate on another. A learned linear projection head (input dimension $\to$ 256 $\to$ target dimension) maps between representational spaces of models with different hidden dimensions.
178:\caption{Cross-model transfer accuracy. A learned linear projection maps between hidden spaces. All conditions exceed chance (50\%), revealing shared safety geometry.}
414:[Omitted long matching line]
486:\newblock SafeThink: Thinking-level safety alignment for large reasoning models.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-16T22:12:46.891395+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "extract|pooling|mean|last token|first token|hidden.state",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "extract|pooling|mean|last token|first token|hidden.state",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T212347/best/paper.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-16T22:12:46.942175+00:00_

26:[Omitted long matching line]
35:[Omitted long matching line]
37:We address this gap with a systematic evaluation of detection methods for reasoning-model safety commitment. Our evaluation spans four models across two architecture families (Llama-based DeepSeek-R1-Distill-Llama-8B, Qwen2.5-based DeepSeek-R1-Distill-Qwen-32B, QwQ-32B, and OpenThinker-7B) and compares hidden-state probes, text-based monitors, unsupervised geometric detectors, and sequential change-point methods. Three findings emerge consistently across all tested architectures:
42:\item Temporal context ($W$=15 reasoning steps) universally improves coverage by 5--7 percentage points for both hidden-state and text probes. The coverage improvement is method-agnostic; the precision advantage is modality-specific.
52:[Omitted long matching line]
55:[Omitted long matching line]
58:Bayesian Online Change-Point Detection (BOCPD) \cite{bocpd} and CUSUM \cite{cusum} detect distributional shifts in sequential data. Process Reward Models (PRMs) \cite{prm} score individual reasoning steps. We evaluate BOCPD on hidden-state trajectories as a sequential baseline but find it does not outperform simple temporal probes for pre-commitment detection.
83:\item \textbf{DeepSeek-R1-Distill-Llama-8B} (r1-8b): Llama-based, 32 layers, 4096-d hidden states.
84:\item \textbf{DeepSeek-R1-Distill-Qwen-32B} (r1-32b): Qwen2.5-based, 64 layers, 5120-d hidden states.
85:\item \textbf{QwQ-32B}: Qwen2.5-based, 64 layers, 5120-d hidden states.
96:For each reasoning step $t$, we extract the hidden state $h_t^{(\ell)}$ at layer $\ell$ and train a logistic regression classifier to predict whether $t \geq \text{CP}$. Layer selection follows a sweep procedure; we find the optimal layer consistently at 44--47\% depth across all models (Table~\ref{tab:layer_ablation}).
99:We concatenate hidden states from a window of $W$ consecutive steps: $\mathbf{z}_t = [h_{t-W+1}^{(\ell)}, \ldots, h_t^{(\ell)}]$ and train logistic regression on the conca
…[truncated 4240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-16T22:14:39.741449+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# R2 交叉回应 R1 审稿意见\n\n已逐条核实 R1 的每个 issue 对照论文原文（paper.tex）。\n\n---\n\n## Must-Fix 逐条回应\n\n**[R1-N1] [AGREE]** 数据划分矛盾确实存在，我在自己的审稿中未注意到这一点。\n\nSection 3.3 (line 89) 明确写 \"209 traces per model (166 train / 43 test)\"，但 Section 6.4 (line 396) 写 \"training data scarcity (n=125 training traces)\"。166 ≠ 125，差 41 条——很可能存在一个未声明的 validation set (125 train / 41 val / 43 test)。如果 validation set 用于 layer selection (Section 4.1, Table 10) 和 threshold tuning，这属于正常实验设计，但 **必须在论文中明确说明**。如果 validation labels 泄入了 probe 训练，则 Table 1-2 的结果都可能被高估。这是一个会直接动摇可信度的报告缺陷。\n\n**[R1-N2] [AGREE]** k=3 meta-analysis 的统计效力问题是严肃的方法论批评。\n\n我补充两点：(1) R1 关于 I²=0.12 的置信区间可能从 0% 到 >75% 的判断是正确的——Higgins et al. (2003) 的原始论文指出 k<5 时 I² 的估计高度不稳定；(2) 独立性问题比 R1 表述的更严重——r1-8b 和 r1-32b 不仅 \"同源蒸馏\"（都从 DeepSeek-R1 蒸馏），且蒸馏 teacher 相同，意味着 hidden state 中可能编码了来自同一 teacher 的 safety 信号，这使得 pooled effect 实际上过度估计了 generalizability。论文将 pooled p=0.003 放在 Abstract 中作为核心证据，如果这个统计值本身 underpowered 且违反前提假设，则 Finding 1 的置信度需要 substantial downgrade。\n\n不过，我认为这不应该导致 reject——作者可以：(a) 降低 pooled analysis 的地位，强调 per-model consistency 而非 pooled p-value；(b) 在论文中承认 k=3 的 limitation 和 independence concern。核心发现（HS 在每个单独模型上都优于 text）的 pattern 是真实的，问题在于统计包装的过度声称。\n\n**[R1-N3] [AGREE]** 2×2 不平衡是一个真实的实验设计限制。\n\n我在自己的审稿 (R2-N3) 中从 \"Universally\" overclaim 的角度提出了本质相同的批评。R1 的表述更精确——Llama 仅占 1 cell，无法分离 architecture vs scale 效应。\n\n补充一点：这个限制可能是客观约束造成的。据我所知，目前不存在 Llama-based 32B reasoning distillation model（DeepSeek-R1 只蒸馏了 Llama 8B 和 70B，没有 32B）。但论文应该 **明确声明** 这一约束并降低 \"cross-architecture\" 的声称强度，而不是默默让读者假设这是一个平衡设计。\n\n**[R1-N4] [AGREE]** OpenThinker-7B 从 pooled analysis 中排除但未解释，这构成潜在的选择性报告。\n\n我在自己的审稿中将此列为小问题（\"OpenThinker-7B 使用不一致\"），但 R1 将其升级为 Must-Fix 是合理的。论文 Section 5.1 (line 124) 写 \"all three primary models\"——为什么 OpenThinker-7B 不是 \"primary\"？如果是因为其结果与其他模型不一致，则必须报告并讨论；如果只是因为实验还没做完，则要明确说明。声称 4 模型评估但 pooled analysis 只用 3 个，是容易被审稿人质疑诚信的做法。\n\n---\n\n## Should-Fix 逐条回应\n\n**[R1-W1] [AGREE]** Hidden state 提取方式（last token / mean pooling / first token of each reasoning step）确实未在论文中说明。\n\nSection 4.1 (line 96) 只写 \"extract the hidden state h_t^(ℓ) at layer ℓ\"，没有指定 aggregation。对于一个 \"reasoning step\" 包含多个 token 的情况，提取方式会显著影响 probe 性能。这是一个会影响 reproducibility 的遗漏。\n\n**[R1-W2] [AGREE]** TF-IDF 作为 text baseline 确实较弱。\n\n4096/5120-d hidden states vs TF-IDF sparse features 的对比存在信息量级的不对等。论文声称 \"matched methodology\"（Section 4.2, line 106：\"identical probe architectures\"），但 feature representation 层面的 mismatch 使得 \"modality comparison\" 的结论可能只是反映了特征工程的差距。加入 sentence-level embeddings (e.g., BGE, E5) 或 fine-tuned classifier 作为更 competitive 的 text baseline 是合理要求。\n\n不过，我要指出 ARR guidelines 的 H13 条：\"Do not demand extra experiments beyond what validates the stated claim.\" 如果作者的 claim 是 \"hidden states provide lower FPR than text-based monitors in our evaluation setup\"（which is what Section 5.1 states），那么 TF-IDF 作为一种已发表的 text 监控范式是一个可接受的 baseline。关键是论文需要把 claim scope 限制为 \"compared to TF-IDF-based text probes\" 而非 generic \"text-based monitors\"。\n\n**[R1-W3] [AGREE]** CP 定义鲁棒性是我自己审稿中 N2 (control task) 的延伸问题。\n\n论文的 CP 定义是 \"min{t : y_s = 1 for all s ≥ t}\"（Section 3.1, line 64），要求从 CP 开始 **所有后续步都是 harmful**。如果存在 near-CP oscillation（safety reasoning 在 CP 附近反复出现和消失），这个定义会把 CP 推到 trace 的最后几步，导致所有 detection 方法在 CP 处都有 positional bias。HarmThoughts 的 IAA（inter-annotator agreement）是评估这一问题的关键信息，但论文中完全缺失。\n\n**[R1-W4] [AGREE]** Bootstrap 实施细节确实不够透明。\n\n我在审稿中也注意到 Abstract 中 p=0.003 的 p 值来源不明。R1 的追问更具体：resampling unit 是 trace-level 还是 step-level？这很关键——如果是 step-level resampling，则同一 trace 内的 steps 之间的自相关性会导致 CI 过窄。n=43 test traces 的 bootstrap 本身 variance 就大，需要报告 BCa 或 percentile CI 类型。\n\n**[R1-W5] [AGREE]** 这是一个可验证的缺陷——论文原文确认存在。\n\nSection 2 (line 58) 声称 \"We evaluate BOCPD on hidden-state trajectories as a sequential baseline but find it does not outperform simple temporal probes\"。Section 4.3 (line 113-114) 描述了 BOCPD 方法（λ=10）。但 **全文没有任何 table 或数字报告 BOCPD 的结果**。这属于 \"有 claim 无 evidence\" 的严重问题——一个 baseline 如果被声称 \"evaluated\"，其结果必须以数据呈现，否则审稿人无法验证 claim。\n\n**[R1-W6] [AGREE]** GRU std=9-11%（Table 12）确实使其部署可靠性存疑。\n\n但我对 \"标记为 exploratory\" 这一建议持保留态度。论文已经在 Section 6.4 中将 GRU 定位为 precision-coverage tradeoff 的一端（coverage +20pp at +22pp safe FPR cost），并推荐 temporal LR 作为 practical default。GRU 的高 variance 反而支撑了论文的一个隐含论点：在 n=125 training traces 的小数据场景下，高容量模型不如简单 probe 稳定。这本身是一个有价值的 observation，无需降级为 exploratory。\n\n**[R1-W7] [AGREE]** Projection head 的训练数据来源是一个关键的未回答问题。\n\nSection 4.4 (line 118) 写 \"A learned linear projection head (input dimension → 256 → target dimension) maps between representational spaces\"，但完全没有说明：(1) projection head 用什么数据训练？如果用了 target model 的 labeled data，则这不是零样本 transfer 而是有监督的 alignment——67-74% accuracy 的意义就完全不同了。(2) projection head 需要多少对齐数据？这决定了 transfer 的实用性。(3) 256-d bottleneck 是否约束了 transfer 的信息通量？\n\n这个问题与我的审稿 W4 互补——我关注的是 \"why does transfer work\" 的分析深度，R1 关注的是 transfer 实验的方法学诚实性。两者都需要在 revision 中解决。\n\n---\n\n## 与 R2 审稿的交叉对比\n\n**重叠**：\n- R1-N3 ≈ R2-N3：模型多样性不足 / \"Universally\" overclaim\n- R1-N4 部分对应 R2 小问题中的 OpenThinker-7B 使用不一致\n- R1-W3 与 R2-N2 互补：R1 关注 CP 定义鲁棒性/IAA，R2 关注 control task 排除 positional confound\n\n**R1 发现了 R2 遗漏的关键问题**：\n- R1-N1（数据划分矛盾 166 vs 125）—— 我完全没有注意到这个数字不一致\n- R1-W5（BOCPD 有方法无数据）—— 我也遗漏了这一点\n\n**R2 补充了 R1 未涉及的维度**：\n- R2-N1（related work 覆盖不足，probing classifier 奠基文献缺失）—— R1 未讨论引用充分性\n- R2-W1（\"HS beats text\" 的非惊喜性）—— R1 未从信息论角度讨论 finding 的 novelty\n- R2-W2（correlational vs causal）—— R1 未讨论因果验证缺失\n- R2-W3（PRM 结构性联系）—— R1 未讨论 process supervision 文献的关联\n\n**整体判断**：R1 和 R2 的评分趋同（均 2.5/5）。R1 偏重实验方法论和数据诚实性，R2 偏重 novelty 和文献脉络。两者合在一起，形成对论文的全面评价。核心共识是：问题有价值、实验框架合理，但 execution 有多处方法学不透明，claims 超出证据支撑范围，related work 不足。修复后适合 Findings，当前状态距 Main track 有距离。\n",
  "reviewer_id": "2",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# R2 交叉回应 R1 审稿意见\n\n已逐条核实 R1 的每个 issue 对照论文原文（paper.tex）。\n\n---\n\n## Must-Fix 逐条回应\n\n**[R1-N1] [AGREE]** 数据划分矛盾确实存在，我在自己的审稿中未注意到这一点。\n\nSection 3.3 (line 89) 明确写 \"209 traces per model (166 train / 43 test)\"，但 Section 6.4 (line 396) 写 \"training data scarcity (n=125 training traces)\"。166 ≠ 125，差 41 条——很可能存在一个未声明的 validation set (125 train / 41 val / 43 test)。如果 validation set 用于 layer selection (Section 4.1, Table 10) 和 threshold tuning，这属于正常实验设计，但 **必须在论文中明确说明**。如果 validation labels 泄入了 probe 训练，则 Table 1-2 的结果都可能被高估。这是一个会直接动摇可信度的报告缺陷。\n\n**[R1-N2] [AGREE]** k=3 meta-analysis 的统计效力问题是严肃的方法论批评。\n\n我补充两点：(1) R1 关于 I²=0.12 的置信区间可能从 0% 到 >75% 的判断是正确的——Higgins et al. (2003) 的原始论文指出 k<5 时 I² 的估计高度不稳定；(2) 独立性问题比 R1 表述的更严重——r1-8b 和 r1-32b 不仅 \"同源蒸馏\"（都从 DeepSeek-R1 蒸馏），且蒸馏 teacher 相同，意味着 hidden state 中可能编码了来自同一 teacher 的 safety 信号，这使得 pooled effect 实际上过度估计了 generalizability。论文将 pooled p=0.003 放在 Abstract 中作为核心证据，如果这个统计值本身 underpowered 且违反前提假设，则 Finding 1 的置信度需要 substantial downgrade。\n\n不过，我认为这不应该导致 reject——作者可以：(a) 降低 pooled analysis 的地位，强调 per-model consistency 而非 pooled p-value；(b) 在论文中承认 k=3 的 limitation 和 independence concern。核心发现（HS 在每个单独模型上都优于 text）的 pattern 是真实的，问题在于统计包装的过度声称。\n\n**[R1-N3] [AGREE]** 2×2 不平衡是一个真实的实验设计限制。\n\n我在自己的审稿 (R2-N3) 中从 \"Universally\" overclaim 的角度提出了本质相同的批评。R1 的表述更精确——Llama 仅占 1 cell，无法分离 architecture vs scale 效应。\n\n补充一点：这个限制可能是客观约束造成的。据我所知，目前不存在 Llama-based 32B reasoning distillation model（DeepSeek-R1 只蒸馏了 Llama 8B 和 70B，没有 32B）。但论文应该 **明确声明** 这一约束并降低 \"cross-architecture\" 的声称强度，而不是默默让读者假设这是一个平衡设计。\n\n**[R1-N4] [AGREE]** OpenThinker-7B 从 pooled analysis 中排除但未解释，这构成潜在的选择性报告。\n\n我在自己的审稿中将此列为小问题（\"OpenThinker-7B 使用不一致\"），但 R1 将其升级为 Must-Fix 是合理的。论文 Section 5.1 (line 124) 写 \"all three primary models\"——为什么 OpenThinker-7B 不是 \"primary\"？如果是因为其结果与其他模型不一致，则必须报告并讨论；如果只是因为实验还没做完，则要明确说明。声称 4 模型评估但 pooled analysis 只用 3 个，是容易被审稿人质疑诚信的做法。\n\n---\n\n## Should-Fix 逐条回应\n\n**[R1-W1] [AGREE]** Hidden state 提取方式（last token / mean pooling / first token of each reasoning step）确实未在论文中说明。\n\nSection 4.1 (line 96) 只写 \"extract the hidden state h_t^(ℓ) at layer ℓ\"，没有指定 aggregation。对于一个 \"reasoning step\" 包含多个 token 的情况，提取方式会显著影响 probe 性能。这是一个会影响 reproducibility 的遗漏。\n\n**[R1-W2] [AGREE]** TF-IDF 作为 text baseline 确实较弱。\n\n4096/5120-d hidden states vs TF-IDF sparse features 的对比存在信息量级的不对等。论文声称 \"matched methodology\"（Section 4.2, line 106：\"identical probe architectures\"），但 feature representation 层面的 mismatch 使得 \"modality comparison\" 的结论可能只是反映了特征工程的差距。加入 sentence-level embeddings (e.g., BGE, E5) 或 fine-tuned classifier 作为更 competitive 的 text baseline 是合理要求。\n\n不过，我要指出 ARR guidelines 的 H13 条：\"Do not demand extra experiments beyond what validates the stated claim.\" 如果作者的 claim 是 \"hidden states provide lower FPR than text-based monitors in our evaluation setup\"（which is what Section 5.1 states），那么 TF-IDF 作为一种已发表的 text 监控范式是一个可接受的 baseline。关键是论文需要把 claim scope 限制为 \"compared to TF-IDF-based text probes\" 而非 generic \"text-based monitors\"。\n\n**[R1-W3] [AGREE]** CP 定义鲁棒性是我自己审稿中 N2 (control task) 的延伸问题。\n\n论文的 CP 定义是 \"min{t : y_s = 1 for all s ≥ t}\"（Section 3.1, line 64），要求从 CP 开始 **所有后续步都是 harmful**。如果存在 near-CP oscillation（safety reasoning 在 CP 附近反复出现和消失），这个定义会把 CP 推到 trace 的最后几步，导致所有 detection 方法在 CP 处都有 positional bias。HarmThoughts 的 IAA（inter-annotator agreement）是评估这一问题的关键信息，但论文中完全缺失。\n\n**[R1-W4] [AGREE]** Bootstrap 实施细节确实不够透明。\n\n我在审稿中也注意到 Abstract 中 p=0.003 的 p 值来源不明。R1 的追问更具体：resampling unit 是 trace-level 还是 step-level？这很关键——如果是 step-level resampling，则同一 trace 内的 steps 之间的自相关性会导致 CI 过窄。n=43 test traces 的 bootstrap 本身 variance 就大，需要报告 BCa 或 percentile CI 类型。\n\n**[R1-W5] [AGREE]** 这是一个可验证的缺陷——论文原文确认存在。\n\nSection 2 (line 58) 声称 \"We evaluate BOCPD on hidden-state trajectories as a sequential baseline but find it does not outperform simple temporal probes\"。Section 4.3 (line 113-114) 描述了 BOCPD 方法（λ=10）。但 **全文没有任何 table 或数字报告 BOCPD 的结果**。这属于 \"有 claim 无 evidence\" 的严重问题——一个 baseline 如果被声称 \"evaluated\"，其结果必须以数据呈现，否则审稿人无法验证 claim。\n\n**[R1-W6] [AGREE]** GRU std=9-11%（Table 12）确实使其部署可靠性存疑。\n\n但我对 \"标记为 exploratory\" 这一建议持保留态度。论文已经在 Section 6.4 中将 GRU 定位为 precision-coverage tradeoff 的一端（coverage +20pp at +22pp safe FPR cost），并推荐 temporal LR 作为 practical default。GRU 的高 variance 反而支撑了论文的一个隐含论点：在 n=125 training traces 的小数据场景下，高容量模型不如简单 probe 稳定。这本身是一个有价值的 observation，无需降级为 exploratory。\n\n**[R1-W7] [AGREE]** Projection head 的训练数据来源是一个关键的未回答问题。\n\nSection 4.4 (line 118) 写 \"A learned linear projection head (input dimension → 256 → target dimension) maps between representational spaces\"，但完全没有说明：(1) projection head 用什么数据训练？如果用了 target model 的 labeled data，则这不是零样本 transfer 而是有监督的 alignment——67-74% accuracy 的意义就完全不同了。(2) projection head 需要多少对齐数据？这决定了 transfer 的实用性。(3) 256-d bottleneck 是否约束了 transfer 的信息通量？\n\n这个问题与我的审稿 W4 互补——我关注的是 \"why does transfer work\" 的分析深度，R1 关注的是 transfer 实验的方法学诚实性。两者都需要在 revision 中解决。\n\n---\n\n## 与 R2 审稿的交叉对比\n\n**重叠**：\n- R1-N3 ≈ R2-N3：模型多样性不足 / \"Universally\" overclaim\n- R1-N4 部分对应 R2 小问题中的 OpenThinker-7B 使用不一致\n- R1-W3 与 R2-N2 互补：R1 关注 CP 定义鲁棒性/IAA，R2 关注 control task 排除 positional confound\n\n**R1 发现了 R2 遗漏的关键问题**：\n- R1-N1（数据划分矛盾 166 vs 125）—— 我完全没有注意到这个数字不一致\n- R1-W5（BOCPD 有方法无数据）—— 我也遗漏了这一点\n\n**R2 补充了 R1 未涉及的维度**：\n- R2-N1（related work 覆盖不足，probing classifier 奠基文献缺失）—— R1 未讨论引用充分性\n- R2-W1（\"HS beats text\" 的非惊喜性）—— R1 未从信息论角度讨论 finding 的 novelty\n- R2-W2（correlational vs causal）—— R1 未讨论因果验证缺失\n- R2-W3（PRM 结构性联系）—— R1 未讨论 process supervision 文献的关联\n\n**整体判断**：R1 和 R2 的评分趋同（均 2.5/5）。R1 偏重实验方法论和数据诚实性，R2 偏重 novelty 和文献脉络。两者合在一起，形成对论文的全面评价。核心共识是：问题有价值、实验框架合理，但 execution 有多处方法学不透明，claims 超出证据支撑范围，related work 不足。修复后适合 Findings，当前状态距 Main track 有距离。\n",
    "reviewer_id": "2",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-16T22:14:43.411930+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3670
}
```

</details>

---


### Assistant

_source line 80 · 2026-05-16T22:14:50.331214+00:00_

交叉回应已提交。总结：

- R1 的 4 个 Must-Fix 全部 **[AGREE]**，其中 N1（166 vs 125 数据矛盾）和 N4（OpenThinker-7B 选择性排除）是我自己审稿中遗漏的关键问题
- R1 的 7 个 Should-Fix 全部 **[AGREE]**，其中 W5（BOCPD 有方法描述无结果数据）是一个可直接验证的缺陷
- R1 偏重实验方法论诚实性，R2 偏重 novelty/related work，两份审稿互补形成完整评价
- 核心共识：2.5/5，修复后适合 Findings，当前距 Main track 有差距

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2"
}
```

</details>

---


## Round 3

## Round 3

56 recorded events


### User

_source line 81 · 2026-05-17T04:23:45.762844+00:00_

[Round 2 审稿请求]:
## Round 2 审稿任务 — Reviewer 2（新颖性/贡献 + 写作质量 + 格式合规）

**论文**: "Temporal Probing for Safety Commitment Detection in Reasoning Models"
**Venue**: EMNLP 2026 ARR (May cycle, deadline 2026-05-25)
**格式**: ACL long paper, 8 pages + unlimited refs + 1 page Limitations, double-blind, `\usepackage[review]{acl}`
**论文路径**: `projects/contrastive_trace_safety/docs/paper/main.tex`（sections/ 子目录含各章节）

---

### 你的审查侧重

1. **新颖性与贡献评估**：
   - 核心 claim "temporal context dominates modality choice" 是否足够 novel 支撑 EMNLP main track
   - 三个贡献是否均有对应实验支撑、是否 incremental
   - Negative results (TrajGuard/BOCPD/transfer failure) 的价值：是否提供了 non-trivial insight
   - 与 TrajGuard (2026), SafeSwitch (2025), SIREN (2026) 的差异化是否清晰

2. **写作质量**：
   - Abstract 是否清晰传达问题/方法/结论（检查是否过长、是否堆砌数据）
   - Introduction 叙事线是否连贯（问题→gap→insight→贡献）
   - Discussion 是否与 Conclusion 内容重复
   - 检查 AI 写作痕迹：em-dash (—)、-ing phrases 结尾、过度分段、"Furthermore/Moreover/Additionally" 连续使用
   - 术语一致性：CP/commitment point 首次使用时是否有定义

3. **Related Work 质量**：
   - 是否从论文堆砌变为有组织的主题式比较
   - 引用覆盖度：probing、causal interp、safety detection、reasoning safety、PRM 是否齐全
   - positioning 是否清晰（本文 vs 已有方法的差异）

4. **格式合规**：
   - `\documentclass[11pt]{article}` + `\usepackage[review]{acl}` 是否等价于官方模板
   - Limitations section 是否存在且不超过 1 page
   - Responsible NLP Checklist 是否完整
   - 匿名性：是否泄露作者信息
   - References 格式：是否使用 natbib/ACL bibliography style
   - Appendix bug disclosure (M002) 是否适合正文 vs 补充材料

5. **Round 1 遗留问题核查**（重点验证以下是否已充分解决）：
   - C1: 标题 overclaim 是否解决？
   - C6: Related Work 是否从 14 citations 扩展到足够量级？
   - S8: "HS > text" 的 novelty 论证是否改善？（新 framing 是 "temporal > modality"）
   - S9: Probing 相关性 vs 因果性是否在 Limitations 声明？
   - S10: PRM 联系是否在 Related Work 讨论？
   - F1: LaTeX 模板是否官方？
   - F2: Responsible NLP Checklist 是否存在？
   - F3: References 格式是否修复？
   - F4: Table 格式是否统一？

---

### 输出格式

```
## Summary (2-3句)

## Strengths (逐条)

## Weaknesses (逐条，标注severity: critical/warning/info)

## Questions to Authors

## Round 1 Issue Resolution Check
[逐条列出上述 C1/C6/S8/S9/S10/F1/F2/F3/F4 的当前状态: resolved/partially/unresolved]

## Overall Assessment (1-5分 + 1句总评)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-17T04:23:54.669896+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-17T04:23:54.770894+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-17T04:24:00.845172+00:00_

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
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 85 · 2026-05-17T04:24:02.200530+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-17T04:24:02.200928+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 87 · 2026-05-17T04:24:03.405524+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/contrastive_trace_safety/docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/contrastive_trace_safety/docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5"
  }
}
```

</details>

---


### Tool result

_source line 88 · 2026-05-17T04:24:03.456209+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-17T04:24:08.124037+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

I found information about ARR (ACL Rolling Review) 2026 reviewer guidelines and review form criteria. Here's what the search results reveal:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while confere
…[truncated 1607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7278
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-17T04:24:11.598382+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/contrastive_trace_safety/docs/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/contrastive_trace_safety/docs/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-17T04:24:12.050501+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/acl2023.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/figures/fig2_temporal_improvement.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/figures/fig3_model_dependency.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/figures/fig3_model_dependency.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen
…[truncated 783 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-17T04:24:13.104816+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. List all fields a reviewer must fill out and the scoring rubric for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. List all fields a reviewer must fill out and the scoring rubric for each dimension."
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-17T04:24:20.783025+00:00_

# ACL Rolling Review Form: Complete Structure

## Required Text Fields
1. **Paper Summary** - Overview of paper topic and content
2. **Summary of Strengths** - Reasons supporting publication at selective venues
3. **Summary of Weaknesses** - Concerns prioritizing other papers (numbered format requested)
4. **Comments/Suggestions/Typos** - Additional improvement feedback

## Scoring Dimensions

### Reviewer Confidence
Scale: 1-5
- 5 = "Positive that my evaluation is correct"
- 4 = "Quite sure" with unlikely missed details
- 3 = "Pretty sure" but possible oversights
- 2 = "Willing to defend" evaluation despite likely gaps
- 1 = "Not my area" or highly unclear work

### Soundness
Scale: 1-5 (with half-point increments)
- 5 = "Excellent: most thorough study of its type"
- 4 = "Strong: sufficient support for claims"
- 3 = "Acceptable: main claims supported"
- 2 = "Poor: major technical/methodological problems"
- 1 = "Major Issues: insufficient for publication"

### Excitement
Scale: 1-5 (with half-point increments)
- 5 = "Highly Exciting: recommend to others"
- 4 = "Exciting: mention to others"
- 3 = "Interesting: might mention points"
- 2 = "Potentially Interesting: may resonate with community"
- 1 = "Not Exciting: unrelated to computational linguistics"

### Overall Assessment
Scale: 1-5 (with half-point increments)
- 5 = "Consider for Award"
- 4 = "Conference acceptance"
- 3 = "Findings acceptance"
- 2 = "Resubmit next cycle"
- 1 = "Do not resubmit"

## Additional Required Sections

### Open-Ended Questions
- **Best Paper Justification** - Required if scoring 4.5 or 5
- **Limitations and Societal Impact** - Assessment of author discussion
- **Ethical Concerns** - Review against ACL code of ethics
- **Needs Ethics Review** - Recommendation for specialized review

### Reproducibility
Scale: 1-5
- 5 = "Could easily reproduce results"
- 4 = "Mostly reproducible"
- 3 = "Reproducible with difficulty"
- 2 = "Hard to reproduce"
- 1 = "Cannot reproduce"

### Datasets
Scale: 1-
…[truncated 395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7678
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-17T04:24:26.038447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-17T04:24:26.503068+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{subcaption}
11	\usepackage{xcolor}
12	\usepackage{hyperref}
13	\usepackage{cleveref}
14	
15	\title{Temporal Probing for Safety Commitment Detection in Reasoning Models}
16	
17	\author{Anonymous ARR Submission}
18	
19	\begin{document}
20	\maketitle
21	
22	\begin{abstract}
23	\input{sections/abstract}
24	\end{abstract}
25	
26	\input{sections/introduction}
27	
28	\input{sections/related_work}
29	
30	\input{sections/method}
31	
32	\input{sections/experiments}
33	
34	\input{sections/conclusion}
35	
36	\input{sections/limitations}
37	
38	\bibliography{references}
39	
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 464
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-17T04:24:26.503398+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-17T04:24:26.955057+00:00_

1	Large Language Models (LLMs) with Chain-of-Thought (CoT) reasoning can self-jailbreak: their extended reasoning traces sometimes transition from safe deliberation to committed generation of harmful content. Detecting the precise moment of this safety commitment is essential for real-time intervention, yet no prior work has systematically compared hidden-state (HS) probes against text-based monitors for this task under controlled conditions. We present the first cross-model evaluation of temporal probing methods for safety commitment detection. Our study spans three reasoning models (DeepSeek-R1 8B/32B, QwQ-32B) across two architectures and two scales, and compares HS probes, text monitors, temporal windowing, Gated Recurrent Unit (GRU) sequence models, and geometric baselines including Mahalanobis distance, Bayesian Online Change Point Detection, and Cumulative Sum (CUSUM). Our results reveal three findings. First, temporal context is the dominant factor: expanding the observation window from 1 to 25 reasoning steps improves precision by 12.9 percentage points and reduces false positive rate (FPR) across all models and modalities. Second, the modality advantage is model-dependent: on R1-8B, HS probes Pareto-dominate text probes (+22.4pp precision, $p{<}0.001$; +8.2pp accuracy, $p{=}0.005$; both surviving Bonferroni correction), while on 32B models it ranges from directional (R1-32B, $p{=}0.080$) to absent (QwQ-32B, $p{=}0.828$), with no result surviving Bonferroni correction. Third, geometric distance methods and cross-model transfer fail entirely, and change-point methods (BOCPD, CUSUM) do not improve early detection despite high coverage, defining clear boundaries of current approaches. Control tasks confirm that probes capture genuine safety-relevant structure rather than superficial distributional shifts.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-17T04:24:26.955553+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-17T04:24:27.357547+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Reasoning models such as DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq} have advanced language model capabilities by scaling chain-of-thought (CoT) inference, producing extended internal deliberation before generating final responses. These models interleave safety-aware reasoning with content generation across dozens of reasoning steps, and this very capacity for self-reflection introduces a new failure mode. Recent work has documented that reasoning models can ``self-jailbreak'': even without adversarial input modifications, the model's own CoT may transition from considering safety constraints to committing to produce harmful content~\cite{harmthoughts,selfjailbreak}. In such cases, the model's reasoning trace contains a \textbf{Safety Commitment Point} (CP), the first step after which safety reasoning permanently ceases and harmful generation proceeds unchecked. Detecting this transition in real time is essential for monitoring systems that must intervene before harmful content reaches users.
4	
5	Existing safety detectors were designed for a different threat model. Methods based on hidden-state (HS) probing, such as TrajGuard~\cite{trajguard} and SafeSwitch~\cite{safeswitch}, monitor internal activations to classify adversarial inputs and achieve high accuracy (above 95\%) on standard Large Language Models (LLMs). Text-based monitors like SafeRemind~\cite{saferemind} and SafeThink~\cite{safethink} scan generated reasoning text for safety violations. Both families target external attacks on model inputs rather than the model's own internal commitment process. A fundamental question remains unanswered: when detecting safety commitment within multi-step reasoning, should a monitoring system read the model's hidden states or its generated text? Intuition suggests that HS features (4096 dimensions of internal computation) should be far more informative than text embeddings (384 dimensions from a sentence encode
…[truncated 4123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-17T04:24:27.357983+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-17T04:24:27.409108+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Probing Neural Representations.}
4	Linear probes are a standard tool for investigating learned representations~\citep{alain2017understanding,belinkov2017morphology,conneau2018probing,belinkov2019analysis}. \citet{hewitt2019structural} show that syntax trees are linearly recoverable from contextual embeddings. \citet{hewitt2019control} introduce control tasks and selectivity to distinguish genuine signal from probe memorization. We extend probing from linguistic to safety-relevant properties, adopting the control task methodology to validate our probes.
5	
6	\paragraph{Causal Interpretability.}
7	Causal abstraction~\citep{geiger2021causal}, causal mediation analysis~\citep{vig2020causal}, ROME~\citep{meng2022locating}, and ACDC~\citep{conmy2023circuit} establish causal relationships between representations and model behavior. These methods require expensive interventions during inference. Our approach is explicitly correlational: we establish that safety commitment is \textit{decodable} from hidden states without claiming causality, trading causal guarantees for practical applicability.
8	
9	\paragraph{Hidden-State Safety Detection.}
10	TrajGuard~\citep{trajguard} uses Mahalanobis distance on hidden-state trajectories, SafeSwitch~\citep{safeswitch} trains hidden-state classifiers for safety interventions, and SIREN~\citep{siren} monitors internal representations during generation. Representation Engineering~\citep{zou2023representation} identifies linear safety directions, and \citet{arditi2024refusal} show refusal is mediated by a single direction. These works identify static safety directions; we study the \textit{temporal evolution} of safety commitment during multi-step reasoning. On the attack side, GCG~\citep{zou2023gcg} generates universal adversarial suffixes, while SmoothLLM~\citep{robey2023smoothllm} and perplexity filtering~\citep{alon2023perplexity} defend at the input level. We focus on det
…[truncated 1993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-17T04:24:30.822184+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-17T04:24:31.274233+00:00_

1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	\subsection{Safety Commitment Point}
5	\label{sec:commitment-point}
6	
7	When a reasoning model is jailbroken, its CoT transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first step after which safety reasoning permanently ceases. We operationalize this on HarmThoughts~\cite{harmthoughts} traces: the CP is the earliest step $t^*$ such that no subsequent step contains safety reasoning. Steps before CP are \emph{pre-commitment}; steps after are \emph{post-commitment}.
8	
9	\subsection{Metrics}
10	\label{sec:metrics}
11	
12	Let $s_t$ denote the probe score at step $t$, $\tau$ the threshold, and $t^*$ the annotated CP.
13	
14	\textbf{Coverage}: fraction of jailbreak traces where any step exceeds $\tau$. \textbf{Pre-CP FPR}: we report both step-level (pooling all pre-CP steps) and trace-level (mean per-trace FPR, treating each trace as an independent observation for paired statistical comparison). \textbf{Precision}: fraction of threshold-exceeding steps that are post-CP. \textbf{Lead time}: steps between first detection and CP ($t^* - t_{\text{detect}}$).
15	
16	All modality comparisons use a two-sided paired permutation test (1000 resamples) on trace-level values, with Bonferroni correction ($\alpha{=}0.017$, 3 models). We use detection criterion $K{=}1$ (single crossing) throughout.
17	
18	\subsection{Models and Data}
19	\label{sec:models-data}
20	
21	We study three models spanning two architectures and two scales:
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\begin{tabular}{lcccccc}
27	\toprule
28	\textbf{Model} & \textbf{Arch.} & \textbf{Params} & \textbf{Layers} & \textbf{Hidden} & \textbf{Traces} & \textbf{Test} \\
29	\midrule
30	R1-8B & Llama & 8B & 32 & 4096 & 209 & 43 \\
31	R1-32B & Qwen & 32B & 64 & 5120 & 100 & 20 \\
32	QwQ-32B & Qwen & 32B & 64 & 5120 & 95 & 19 \\
33	\bottomrule
34	\end{tabular}
35	\caption{
…[truncated 2586 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-17T04:24:31.274646+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-17T04:24:31.726798+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate contrastive trace probes across three reasoning models (R1-8B, R1-32B, QwQ-32B), two signal modalities (hidden states and text), and multiple temporal aggregation strategies. Our experiments address four questions: (1) How much does temporal context improve detection? (2) Does the choice of signal modality matter? (3) Can sequence models detect unsafe reasoning earlier? (4) Do probes transfer across models?
5	
6	\subsection{Temporal Context as Primary Factor}
7	\label{sec:temporal_primary}
8	
9	The most consistent finding across all experimental conditions is that temporal context improves probe precision and reduces FPR, regardless of signal modality. \cref{fig:window_ablation} shows this pattern for R1-8B; precision and FPR gains hold across all three models, though balanced accuracy improvement is model-dependent.
10	
11	\begin{figure}[t]
12	\centering
13	\includegraphics[width=\columnwidth]{figures/fig2_temporal_improvement.pdf}
14	\caption{Effect of temporal window size on R1-8B HS probe performance. Precision increases monotonically from 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR decreases from 9.65\% to 4.83\%. Coverage decreases as larger windows make the probe more conservative.}
15	\label{fig:window_ablation}
16	\end{figure}
17	
18	On R1-8B, increasing window size from $W{=}1$ to $W{=}25$ improves balanced accuracy from 77.8\% to 81.0\% (+3.2pp), precision from 69.3\% to 82.2\% (+12.9pp), and reduces step-level FPR from 9.65\% to 4.83\% ($-$4.8pp). QwQ-32B shows a similar monotonic pattern (+3.2pp accuracy, +7.4pp precision, $-$5.9pp FPR from $W{=}1$ to $W{=}25$). R1-32B exhibits a non-monotonic trajectory: accuracy peaks at $W{=}10$ then declines below the $W{=}1$ baseline by $W{=}25$ (71.8\% $\rightarrow$ 70.3\%), though precision and FPR still improve (+1.7pp, $-$5.5pp). Across all three models, FPR consistently decreases with larger windows (\cref{tab:temporal_main}). Larger windows mak
…[truncated 11742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-17T04:24:31.727333+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-17T04:24:32.681228+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why temporal context dominates modality choice.}
5	Information-theoretic reasoning suggests that hidden states (4096 dimensions of internal computation) should dominate text features (384-dimensional sentence embeddings) by a wide margin. In practice, the temporal dimension matters more than signal richness. Complete window sweeps ($W{=}1$ to $25$) confirm this across both modalities (Section~\ref{sec:temporal_primary}): HS probes gain +3.2pp accuracy, +12.9pp precision, and $-$4.8pp FPR, while text probes gain +12.0pp accuracy, +23.2pp precision, and $-$14.0pp FPR. Text probes benefit more from temporal context than HS probes, which strengthens the claim that temporal structure is the primary factor. HS probes start from a higher baseline (benefiting from richer internal signal), so their marginal gains from temporal context are smaller. Text probes, beginning with weaker single-step features, extract proportionally more from observing multi-step progressions. These gains are consistent and model-agnostic, unlike modality differences which vary by model. Safety commitment is a gradual process: the model progressively consolidates its intent over multiple reasoning steps, and observing this progression provides the dominant information gain.
6	
7	\paragraph{Why the modality advantage is model-dependent.}
8	R1-8B is the only model where HS probes Pareto-dominate text probes with statistical confirmation (+22.4pp precision, $p{<}0.001$; +8.2pp accuracy, $p{=}0.005$; both surviving Bonferroni correction). On the 32B models, the pattern diverges. R1-32B shows directional HS advantages (+8.4pp accuracy, $p{=}0.080$; +9.4pp precision, $p{=}0.050$) consistent with the R1-8B pattern but underpowered with only 20 test traces. QwQ-32B shows no meaningful modality difference (+0.9pp accuracy, $p{=}0.828$; +5.7pp precision, $p{=}0.346$). R1-8B is a Llama-based model trained through distillation, a process that comp
…[truncated 3873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-17T04:24:32.681576+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-17T04:24:32.782275+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	We presented the first systematic evaluation of safety commitment detection in reasoning models, comparing hidden-state probes, text monitors, temporal windowing, sequence models, and geometric baselines across three models (DeepSeek-R1 8B/32B, QwQ-32B), two architectures, and two parameter scales.
4	
5	\paragraph{Why temporal context dominates.}
6	Information-theoretic reasoning suggests that hidden states (4096 dimensions) should dominate text features (384 dimensions) by a wide margin. In practice, the temporal dimension matters more than signal richness. Text probes benefit \textit{more} from temporal context than HS probes (+12.0pp accuracy, +23.2pp precision from $W{=}1$ to $25$ vs.\ +3.2pp, +12.9pp for HS), strengthening the claim that the bottleneck is temporal rather than informational. Safety commitment is a gradual process: the model progressively consolidates intent over multiple steps, and observing this progression provides the dominant information gain.
7	
8	\paragraph{Model-dependent modality advantage.}
9	On R1-8B, HS probes Pareto-dominate text probes (+22.4pp precision, $p{<}0.001$; +8.2pp accuracy, $p{=}0.005$; both surviving Bonferroni correction). On 32B models, the advantage ranges from directional (R1-32B, $p{=}0.080$) to absent (QwQ-32B, $p{=}0.828$). R1-8B is a Llama-based distilled model where compression may concentrate safety signal in hidden representations; larger Qwen-based models reason natively through extended CoT, and their text already carries safety signal at comparable precision-FPR tradeoffs.
10	
11	\paragraph{Method boundaries.}
12	BOCPD achieves high coverage (93\%) but not early detection; CUSUM underperforms simple thresholding; TrajGuard's geometric approach fails because safe and jailbreak trajectories occupy indistinguishable activation regions; cross-model transfer fails entirely. These negative results define clear boundaries: safety commitment is gradua
…[truncated 1019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-17T04:24:32.782691+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-17T04:24:32.833216+00:00_

1	\section{Limitations}\label{sec:limitations}
2	
3	\paragraph{Statistical power and operating point confounds.}
4	Only DeepSeek-R1-8B shows HS probes Pareto-dominating text probes across all metrics ($p = 0.044$ for FPR, not Bonferroni-corrected). On 32B models, HS probes show directional accuracy advantages (+8.4pp on R1-32B, $p{=}0.080$; +0.9pp on QwQ-32B, $p{=}0.828$) but neither survives Bonferroni correction, making it impossible to declare Pareto dominance for either modality. Each model uses a different optimal window size ($W{=}15, 10, 5$ respectively), further complicating cross-model modality comparisons. With 43 test traces for R1-8B and approximately 20 for each 32B model, statistical power is limited. With only ${\sim}20$ test traces per 32B model, our bootstrap tests lack power to detect moderate effect sizes (Cohen's $d < 0.5$), meaning the non-significant results ($p{=}0.080$, $p{=}0.828$) cannot be interpreted as evidence of absence. Larger evaluation sets with matched temporal conditions are needed to determine whether the R1-8B dominance pattern generalizes.
5	
6	\paragraph{Correlation, not causation.}
7	Our probing methodology establishes that safety commitment is \emph{decodable} from intermediate hidden states. It does not demonstrate that these representations causally drive the model's safe or unsafe behavior. Causal intervention studies, such as activation patching at the identified commitment point, would be necessary to verify that the probed features are mechanistically load-bearing rather than epiphenomenal.
8	
9	\paragraph{Commitment point definition.}
10	The commitment point (CP) annotation relies on detecting the presence or absence of explicit safety reasoning in the chain-of-thought. Edge cases exist where models oscillate between safe and unsafe reasoning within a single trace, or embed safety-relevant considerations inside otherwise harmful text. We have not yet conducted inter-annotator agreement studies or sensitivity analyses 
…[truncated 1505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-17T04:24:37.902305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-17T04:24:38.204082+00:00_

1	\appendix
2	
3	\section{Responsible NLP Research Checklist}
4	\label{app:checklist}
5	
6	We address the ARR Responsible NLP Research requirements below.
7	
8	\begin{itemize}
9	    \item \textbf{Limitations discussed:} Yes (\cref{sec:limitations}).
10	    \item \textbf{Potential risks:} This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark.
11	    \item \textbf{Computational budget:} Our experiments involve 3 models with 209, 100, and 95 traces respectively (404 total), using linear probes and single-layer GRUs. Total compute is minimal (under 2 GPU-hours on a single RTX A6000). No large-scale pretraining or finetuning was performed.
12	    \item \textbf{Data:} We use HarmThoughts, a publicly available benchmark with step-level safety annotations. No new data collection was performed.
13	    \item \textbf{Human subjects:} No human subjects research was conducted.
14	    \item \textbf{Reproducibility:} All hyperparameters are reported in \cref{app:gru_details,app:bocpd_config}. Code and corrected data will be released upon publication.
15	\end{itemize}
16	
17	
18	\section{Layer Sweep Results}
19	\label{app:layer_sweep}
20	
21	For each model, we sweep all transformer layers and score each candidate layer using the product of balanced accuracy and crossing rate (accuracy-weighted layer selection, defined in \cref{sec:detection-methods}). This composite metric selects layers that simultaneously achieve good classification and reliable threshold crossing on jailbreak traces.
22	
23	The selected layers are: R1-8B layer 14 (of 32 total, 43.8\% depth), R1-32B layer 10 (of 64, 15.6\% depth), and QwQ-32B layer 2 (of 64, 3.1\% depth). Optimal layer depth is highly model-specific (43.8\%/15.6\%/3.1\%), with no convergence pattern across architectures. Early layers work best fo
…[truncated 14782 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-17T04:24:38.204473+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-17T04:24:38.255195+00:00_

1	@article{trajguard,
2	  title={TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense},
3	  author={Liu, Cheng and Liu, Xiaolei and Li, Xingyu and Xin, Bangzhou and Ding, Kangyi},
4	  journal={arXiv preprint arXiv:2604.07727},
5	  year={2026},
6	  url={https://arxiv.org/abs/2604.07727}
7	}
8	
9	@inproceedings{safeswitch,
10	  title={SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals},
11	  author={Han, Peixuan and Qian, Cheng and Chen, Xiusi and Zhang, Yuji and Ji, Heng and Zhang, Denghui},
12	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
13	  year={2025},
14	  url={https://arxiv.org/abs/2502.01042}
15	}
16	
17	@inproceedings{siren,
18	  title={LLM Safety From Within: Detecting Harmful Content with Internal Representations},
19	  author={Jiao, Difan and Liu, Yilun and Yuan, Ye and Tang, Zhenwei and Du, Linfeng and Wu, Haolun and Anderson, Ashton},
20	  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
21	  year={2026},
22	  url={https://arxiv.org/abs/2604.18519}
23	}
24	
25	@article{saferemind,
26	  title={How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs},
27	  author={Kim, Su-Hyeon and Jin, Hyundong and Lee, Yejin and Han, Yo-Sub},
28	  journal={arXiv preprint arXiv:2601.03662},
29	  year={2026},
30	  url={https://arxiv.org/abs/2601.03662}
31	}
32	
33	@article{safethink,
34	  title={Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away},
35	  author={Ghosal, Soumya Suvra and Chakraborty, Souradip and Singh, Vaibhav and Huang, Furong and Manocha, Dinesh and Bedi, Amrit Singh},
36	  journal={arXiv preprint arXiv:2602.11096},
37	  year={2026},
38	  url={https://arxiv.org/abs/2602.11096}
39	}
40	
41	@article{selfjailbreak,
42	  title={Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training},
43	
…[truncated 10511 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-17T04:24:45.800135+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/acl.sty",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/acl.sty",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-17T04:24:46.805824+00:00_

1	% This is the LaTex style file for *ACL.
2	% The official sources can be found at
3	%
4	%     https://github.com/acl-org/acl-style-files/
5	%
6	% This package is activated by adding
7	%
8	%    \usepackage{acl}
9	%
10	% to your LaTeX file. When submitting your paper for review, add the "review" option:
11	%
12	%    \usepackage[review]{acl}
13	
14	\newif\ifacl@finalcopy
15	\newif\ifacl@anonymize
16	\newif\ifacl@linenumbers
17	\newif\ifacl@pagenumbers
18	\DeclareOption{final}{\acl@finalcopytrue\acl@anonymizefalse\acl@linenumbersfalse\acl@pagenumbersfalse}
19	\DeclareOption{review}{\acl@finalcopyfalse\acl@anonymizetrue\acl@linenumberstrue\acl@pagenumberstrue}
20	\DeclareOption{preprint}{\acl@finalcopytrue\acl@anonymizefalse\acl@linenumbersfalse\acl@pagenumberstrue}
21	\ExecuteOptions{final} % final copy is the default
22	
23	% include hyperref, unless user specifies nohyperref option like this:
24	% \usepackage[nohyperref]{acl}
25	\newif\ifacl@hyperref
26	\DeclareOption{hyperref}{\acl@hyperreftrue}
27	\DeclareOption{nohyperref}{\acl@hyperreffalse}
28	\ExecuteOptions{hyperref} % default is to use hyperref
29	\ProcessOptions\relax
30	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-17T04:24:47.760054+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/*.tex 2>/dev/null || echo \"no matches\"",
  "description": "Count em-dash and en-dash occurrences in tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/*.tex 2>/dev/null || echo \"no matches\"",
    "description": "Count em-dash and en-dash occurrences in tex files"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-17T04:24:48.464778+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex:0
no matches

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-17T04:24:48.565507+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\bibliographystyle",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\bibliographystyle",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-17T04:24:48.616186+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/acl.sty:195:\bibliographystyle{acl_natbib}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/acl2023.sty:195:\bibliographystyle{acl_natbib}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-17T04:24:54.842518+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-17T04:24:54.943367+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-17T04:24:56.399342+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-17T04:24:56.399798+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex:15:\paragraph{Process Supervision and Sequential Monitoring.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:117:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:122:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:143:\caption{Negative results. BOCPD achieves high coverage but worse lead time than simple thresholding. Mahalanobis distances are indistinguishable between safe and jailbreak trajectories.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:150:We test probe transfer across models using PCA alignment. All directions fail: the best transfer (QwQ-32B $\rightarrow$ R1-32B) achieves 67.3\% against a within-model baseline of 65.2\%, a margin within noise. Safety representations are model-specific, requiring per-model probe training.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:155:An oracle using ground-truth labels with $K{=}5$ detection criterion achieves +31 steps lead; our best method (GRU) achieves +4.5 steps, leaving an 85.5\% information gap. Hidden states encode current safety state but carr
…[truncated 2392 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-17T04:24:56.901740+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"@\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib",
  "description": "Count bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"@\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib",
    "description": "Count bib entries"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-17T04:24:57.052824+00:00_

32

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-17T04:25:01.623843+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"^@\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib",
  "description": "Count bib entries (lines starting with @)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"^@\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib",
    "description": "Count bib entries (lines starting with @)"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-17T04:25:02.577050+00:00_

32

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-17T04:25:02.828134+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\input\\{sections/discussion\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\input\\{sections/discussion\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-17T04:25:02.828502+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-17T04:25:23.683839+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "project": "contrastive_trace_safety",
  "skip_online": "False"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
    "project": "contrastive_trace_safety",
    "skip_online": "False"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-17T04:25:53.729266+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 32, \"total_citations\": 54, \"unique_cited_keys\": 32, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 24, \"online_not_found\": 8, \"online_mismatch\": 0}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"trajguard\", \"type\": \"article\", \"title\": \"TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense\", \"authors\": \"Liu, Cheng and Liu, Xiaolei and Li, Xingyu and Xin, Bangzhou and Ding, Kangyi\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.07727\"}, {\"key\": \"safeswitch\", \"type\": \"inproceedings\", \"title\": \"SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals\", \"authors\": \"Han, Peixuan and Qian, Cheng and Chen, Xiusi and Zhang, Yuji and Ji, Heng and Zh...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2025\"}, {\"key\": \"siren\", \"type\": \"inproceedings\", \"title\": \"LLM Safety From Within: Detecting Harmful Content with Internal Representations\", \"authors\": \"Jiao, Difan and Liu, Yilun and Yuan, Ye and Tang, Zhenwei and Du, Linfeng and Wu...\", \"year\": \"2026\", \"venue\": \"Proceedings of the 64th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"saferemind\", \"type\": \"article\", \"title\": \"How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs\", \"authors\": \"Kim, Su-Hyeon and Jin, Hyundong and Lee, Yejin and Han, Yo-Sub\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2601.03662\"}, {\"key\": \"safethink\", \"type\": \"article\", \"title\": \"Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away\", \"authors\": \"Ghosal, Soumya Suvra and Chakraborty, Souradip and Singh, Vaibhav and Huang, Fur...\", \"year\": \"202
…[truncated 25158 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 30045
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-17T04:28:08.741866+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 2 Review\n\n**Paper**: \"Temporal Probing for Safety Commitment Detection in Reasoning Models\"\n**Venue**: EMNLP 2026 ARR (May cycle)\n\n---\n\n## Summary (2-3句)\n\n本文是首个系统比较 hidden-state probes 与 text monitors 在 reasoning model safety commitment detection 上表现的实证研究。核心发现是 temporal context（观察窗口大小）对检测质量的贡献大于信号模态选择，且 HS probe 优势是 model-dependent 的（仅在 R1-8B 统计显著）。相比 Round 1，论文在标题、Related Work、格式合规、统计方法等方面有实质改善，但 novelty ceiling 和 statistical power 问题仍是主要限制。\n\n---\n\n## Strengths\n\n**S1. 实验设计严谨，统计方法规范。** Bonferroni correction、paired permutation tests、bootstrap CIs、per-seed breakdowns 一应俱全。对非显著结果的谨慎解读（\"cannot be interpreted as evidence of absence\"，Limitations §1）体现了良好的统计素养。\n\n**S2. Temporal > modality 的核心 finding 有说服力。** Table 2 + Figure 2 + Appendix Table 3 + Appendix Table 4（text window ablation）形成完整的证据链。文本 probes 从 temporal context 获益更大（+12.0pp accuracy vs +3.2pp for HS）这一点特别有力地支撑了\"bottleneck is temporal\"的 claim。\n\n**S3. Negative results 有信息量且诚实。** TrajGuard 的 Mahalanobis distance 失效（d=6.64-6.73 indistinguishable，Table 5）、BOCPD 的 coverage-timing tradeoff、cross-model transfer 全面失败——这些结果对后续研究有实际导向价值，不是 trivial 的\"方法 X 不 work\"。\n\n**S4. Control task validation 和 position baseline 设计合理。** 用 Hewitt & Liang (2019) 框架验证 selectivity，额外加 position-only baseline，且诚实报告 QwQ-32B position baseline 略优于 HS probe 的不利结果（Section 5.4），显示科学诚信。\n\n**S5. Bug disclosure (Appendix F) 体现透明度。** 主动披露 M002 bug 及其对 QwQ-32B 结果的影响，在 ML 论文中罕见且值得肯定。\n\n**S6. Related Work 组织清晰。** 6 个 paragraph 主题分明（Probing / Causal / HS Safety / Reasoning Safety / PRM / Cross-Model），每段末尾明确 positioning 本文位置，不是论文堆砌。\n\n---\n\n## Weaknesses\n\n**W1 [warning] Abstract 过长且数据堆砌，不符合 150-250 word 惯例。**\n- 具体位置：sections/abstract.tex\n- 问题：Abstract 约 280-300 words（远超典型 EMNLP paper 的 200 word 甜点），大量堆砌具体数字（+12.9pp, +22.4pp, p<0.001, +8.2pp, p=0.005, p=0.080, p=0.828, 93%, +31 steps, 85.5%）。审稿人在 30 秒内难以提取核心 insight。\n- 建议：保留\"temporal > modality\"和\"model-dependent\"两个核心 finding 各用 1 个代表性数字，删除 Bonferroni、BOCPD、CUSUM 等细节，控制在 200 words 以内。Abstract 不是 Results 的缩写。\n\n**W2 [warning] 核心贡献的 novelty ceiling：empirical comparison without methodological contribution。**\n- 具体位置：Introduction contribution list (items 1-3)\n- 问题：三个贡献均为 empirical observations（temporal context matters, modality is model-dependent, negative results）。论文未提出新的检测方法、新的理论框架或新的数据集。对 EMNLP main track 而言，一篇纯 benchmarking + negative results 的论文需要更强的\"so what\"——读完后 practitioner 应该做什么不同的事情？目前的 deployment recommendation（Section 6 最后一段：\"start with temporal windowing, then evaluate modality per model\"）过于直觉化，缺乏 novelty。\n- 为什么影响评分：EMNLP 的 Excitement 维度要求论文不只是 informative，还要 exciting。当 takeaway 是\"加大窗口、per-model 调参\"，excitement 有限。\n- 建议：考虑是否能将 temporal windowing 形式化为一种新方法（而非仅仅是 concatenation），或提出 adaptive window selection 策略作为 actionable contribution。\n\n**W3 [warning] Statistical power 不足削弱 Contribution 2。**\n- 具体位置：Table 1 (n=20, n=19 for 32B models), Section 5.2, Limitations §1\n- 问题：Contribution 2 声称\"modality advantage is model-dependent\"，但 32B 的 non-significant results 可能纯粹因为 power 不足（n≈20，Cohen's d<0.5 不可检测）。这意味着\"model-dependent\"的 claim 同样可以解读为\"underpowered\"。论文在 Limitations 中承认了这一点（\"cannot be interpreted as evidence of absence\"），但在 Abstract/Introduction/Conclusion 中仍将其作为核心贡献宣传，存在 overclaim 风险。\n- 建议：在 Abstract 和 Introduction 中明确 qualify 这是\"tentative evidence\"而非 definitive finding for 32B models。\n\n**W4 [warning] Architecture/scale/distillation 三重 confound 未充分讨论。**\n- 具体位置：Limitations §6, Discussion ¶2\n- 问题：R1-8B 是唯一的 Llama 架构、唯一的 8B 模型、唯一的 distilled model。HS probe 优势可能来自 (a) Llama vs Qwen 架构差异, (b) 8B vs 32B scale, (c) distillation vs native reasoning，或三者的交互。论文在 Discussion 中猜测\"distillation compresses safety signal\"但无证据。Limitations §6 提到 confound 但仅占 3 行。\n- 建议：这是论文最核心的 confound，应该在 Discussion 中有一个独立 paragraph 系统讨论三种 alternative explanations 和可能的 disambiguation 方案（e.g., 测试 Llama-3 70B native model 或 Qwen-2.5 7B distilled model）。\n\n**W5 [warning] High FPR on safe traces (39-62%) 与 deployment framing 矛盾。**\n- 具体位置：Limitations §5, Discussion ¶3 (\"Deployment implications\"), Conclusion ¶4\n- 问题：Limitations 中承认所有方法在纯 safe traces 上 FPR 为 39-62%，但 Discussion 和 Conclusion 仍然用 \"deployment recommendations\" 的 framing 给出实践建议。一个 FPR 40%+ 的系统在任何生产环境中都不可用。这种 framing gap 会让审稿人感到 disconnect。\n- 建议：将 \"deployment recommendations\" 改为 \"design guidelines for future monitoring systems\" 或类似措辞，明确当前方法是 diagnostic tool 而非 production-ready。\n\n**W6 [info] \"Discussion and Conclusion\" 合并节与 Experiments 的叙事重复。**\n- 具体位置：sections/conclusion.tex 全文 vs sections/experiments.tex\n- 问题：Conclusion 的前三个 paragraph（temporal dominance, model-dependent, method boundaries）几乎逐句重复 Section 5 的结论，仅增加少量解释。对 8-page 正文而言，0.5-1 page 的重复浪费了宝贵空间。\n- 建议：Conclusion 应极度精简（1 paragraph recap + future work），把省出的空间用于扩展 Discussion 中 W4 指出的 confound 分析。\n\n**W7 [info] CP 定义的 annotation reliability 未报告。**\n- 具体位置：Section 3.1, Limitations §3\n- 问题：Safety Commitment Point 定义为\"the first step after which safety reasoning permanently ceases\"，但 Limitations 承认\"edge cases exist where models oscillate\"且\"have not yet conducted inter-annotator agreement studies\"。对于一个以 CP detection 为核心任务的论文，不报告 IAA 是一个明显缺陷。HarmThoughts 数据集是否提供了 IAA 数据？\n- 建议：至少报告 HarmThoughts 原始 annotation 的 IAA（如果有），或在 5 个随机 sample 上做 pilot IAA study。\n\n---\n\n## Questions to Authors\n\n1. Abstract 中 \"both surviving Bonferroni correction\" 仅适用于 R1-8B。能否在 Abstract 中明确限定这是 R1-8B 的结果，避免读者误以为是跨模型结论？\n\n2. Table 3 (HS vs Text) 中 QwQ-32B 的 text probe FPR (17.8%) 优于 HS (20.8%)，但正文仅在一句中提及。在 QwQ-32B 上 text probe 是否 Pareto-dominate HS probe？如果是，这应该在 Contribution 2 中明确。\n\n3. Oracle gap analysis (Section 5.7) 的 85.5% 是如何计算的？(+31 - +4.5) / +31 = 85.5%？这个 metric 是否对 oracle 的 lead time 选择敏感？K=5 的选择依据是什么？\n\n4. 为什么 text probe 用 all-MiniLM-L6-v2 (384-d) 而非更强的 encoder (e.g., E5-large, GTE-large)? 如果用更强的 text encoder，modality gap 可能缩小甚至逆转。\n\n5. Layer selection (R1-8B: layer 14/32, R1-32B: layer 10/64, QwQ-32B: layer 2/64) 的巨大差异是否意味着不同模型的 safety information 编码位置完全不同？这对 Contribution 3 (transfer failure) 的解释有何意义？\n\n---\n\n## Round 1 Issue Resolution Check\n\n| Issue | Status | Evidence |\n|-------|--------|----------|\n| **C1**: 标题 overclaim | ✅ Resolved | 新标题 \"Temporal Probing for Safety Commitment Detection in Reasoning Models\" 描述性强，无 overclaim |\n| **C6**: Related Work 从 14 citations 扩展 | ✅ Resolved | 32 references, 6 thematic paragraphs, 覆盖 probing/causal/safety/PRM/cross-model |\n| **S8**: \"HS > text\" novelty 论证 | ✅ Resolved | 重新 framing 为 \"temporal > modality\"，有完整 window sweep 支撑 |\n| **S9**: Correlation vs causation 声明 | ✅ Resolved | Limitations §2 明确声明 \"does not demonstrate causal\" |\n| **S10**: PRM 联系 | ✅ Resolved | Related Work ¶5 \"Process Supervision and Sequential Monitoring\" 明确讨论 |\n| **F1**: LaTeX 模板官方 | ✅ Resolved | acl.sty 来自 github.com/acl-org/acl-style-files/, `\\usepackage[review]{acl}` |\n| **F2**: Responsible NLP Checklist | ✅ Resolved | Appendix A 完整填写 |\n| **F3**: References 格式 | ✅ Resolved | 使用 acl_natbib.bst, natbib commands (citep/citet) |\n| **F4**: Table 格式统一 | ✅ Resolved | 所有表格使用 booktabs (toprule/midrule/bottomrule)，格式一致 |\n\n**所有 Round 1 问题均已解决。**\n\n---\n\n## Overall Assessment\n\n**Soundness**: 3.5/5 — 实验设计规范，统计方法正确，但 power 不足和 confound 问题限制了结论强度。\n\n**Excitement**: 2.5/5 — \"Temporal context matters more than modality\" 的 finding 有价值但 methodological contribution 缺失，takeaway 偏向常识（\"多看几步更准\"）。对于纯 empirical study，novelty ceiling 限制了 excitement。\n\n**Reproducibility**: 4/5 — 所有超参报告完整，数据来自公开 benchmark，计算量极低。代码未提供但承诺 release。\n\n**Overall**: 3.0/5 (Findings acceptance)\n\n**一句话总评**: 一篇方法论严谨、统计规范的 empirical study，Round 1 遗留问题全部解决，但缺乏 methodological novelty 且核心 claim 受 statistical power 和 confound 限制，更适合 Findings 而非 main conference track。",
  "reviewer_id": "2",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 2 Review\n\n**Paper**: \"Temporal Probing for Safety Commitment Detection in Reasoning Models\"\n**Venue**: EMNLP 2026 ARR (May cycle)\n\n---\n\n## Summary (2-3句)\n\n本文是首个系统比较 hidden-state probes 与 text monitors 在 reasoning model safety commitment detection 上表现的实证研究。核心发现是 temporal context（观察窗口大小）对检测质量的贡献大于信号模态选择，且 HS probe 优势是 model-dependent 的（仅在 R1-8B 统计显著）。相比 Round 1，论文在标题、Related Work、格式合规、统计方法等方面有实质改善，但 novelty ceiling 和 statistical power 问题仍是主要限制。\n\n---\n\n## Strengths\n\n**S1. 实验设计严谨，统计方法规范。** Bonferroni correction、paired permutation tests、bootstrap CIs、per-seed breakdowns 一应俱全。对非显著结果的谨慎解读（\"cannot be interpreted as evidence of absence\"，Limitations §1）体现了良好的统计素养。\n\n**S2. Temporal > modality 的核心 finding 有说服力。** Table 2 + Figure 2 + Appendix Table 3 + Appendix Table 4（text window ablation）形成完整的证据链。文本 probes 从 temporal context 获益更大（+12.0pp accuracy vs +3.2pp for HS）这一点特别有力地支撑了\"bottleneck is temporal\"的 claim。\n\n**S3. Negative results 有信息量且诚实。** TrajGuard 的 Mahalanobis distance 失效（d=6.64-6.73 indistinguishable，Table 5）、BOCPD 的 coverage-timing tradeoff、cross-model transfer 全面失败——这些结果对后续研究有实际导向价值，不是 trivial 的\"方法 X 不 work\"。\n\n**S4. Control task validation 和 position baseline 设计合理。** 用 Hewitt & Liang (2019) 框架验证 selectivity，额外加 position-only baseline，且诚实报告 QwQ-32B position baseline 略优于 HS probe 的不利结果（Section 5.4），显示科学诚信。\n\n**S5. Bug disclosure (Appendix F) 体现透明度。** 主动披露 M002 bug 及其对 QwQ-32B 结果的影响，在 ML 论文中罕见且值得肯定。\n\n**S6. Related Work 组织清晰。** 6 个 paragraph 主题分明（Probing / Causal / HS Safety / Reasoning Safety / PRM / Cross-Model），每段末尾明确 positioning 本文位置，不是论文堆砌。\n\n---\n\n## Weaknesses\n\n**W1 [warning] Abstract 过长且数据堆砌，不符合 150-250 word 惯例。**\n- 具体位置：sections/abstract.tex\n- 问题：Abstract 约 280-300 words（远超典型 EMNLP paper 的 200 word 甜点），大量堆砌具体数字（+12.9pp, +22.4pp, p<0.001, +8.2pp, p=0.005, p=0.080, p=0.828, 93%, +31 steps, 85.5%）。审稿人在 30 秒内难以提取核心 insight。\n- 建议：保留\"temporal > modality\"和\"model-dependent\"两个核心 finding 各用 1 个代表性数字，删除 Bonferroni、BOCPD、CUSUM 等细节，控制在 200 words 以内。Abstract 不是 Results 的缩写。\n\n**W2 [warning] 核心贡献的 novelty ceiling：empirical comparison without methodological contribution。**\n- 具体位置：Introduction contribution list (items 1-3)\n- 问题：三个贡献均为 empirical observations（temporal context matters, modality is model-dependent, negative results）。论文未提出新的检测方法、新的理论框架或新的数据集。对 EMNLP main track 而言，一篇纯 benchmarking + negative results 的论文需要更强的\"so what\"——读完后 practitioner 应该做什么不同的事情？目前的 deployment recommendation（Section 6 最后一段：\"start with temporal windowing, then evaluate modality per model\"）过于直觉化，缺乏 novelty。\n- 为什么影响评分：EMNLP 的 Excitement 维度要求论文不只是 informative，还要 exciting。当 takeaway 是\"加大窗口、per-model 调参\"，excitement 有限。\n- 建议：考虑是否能将 temporal windowing 形式化为一种新方法（而非仅仅是 concatenation），或提出 adaptive window selection 策略作为 actionable contribution。\n\n**W3 [warning] Statistical power 不足削弱 Contribution 2。**\n- 具体位置：Table 1 (n=20, n=19 for 32B models), Section 5.2, Limitations §1\n- 问题：Contribution 2 声称\"modality advantage is model-dependent\"，但 32B 的 non-significant results 可能纯粹因为 power 不足（n≈20，Cohen's d<0.5 不可检测）。这意味着\"model-dependent\"的 claim 同样可以解读为\"underpowered\"。论文在 Limitations 中承认了这一点（\"cannot be interpreted as evidence of absence\"），但在 Abstract/Introduction/Conclusion 中仍将其作为核心贡献宣传，存在 overclaim 风险。\n- 建议：在 Abstract 和 Introduction 中明确 qualify 这是\"tentative evidence\"而非 definitive finding for 32B models。\n\n**W4 [warning] Architecture/scale/distillation 三重 confound 未充分讨论。**\n- 具体位置：Limitations §6, Discussion ¶2\n- 问题：R1-8B 是唯一的 Llama 架构、唯一的 8B 模型、唯一的 distilled model。HS probe 优势可能来自 (a) Llama vs Qwen 架构差异, (b) 8B vs 32B scale, (c) distillation vs native reasoning，或三者的交互。论文在 Discussion 中猜测\"distillation compresses safety signal\"但无证据。Limitations §6 提到 confound 但仅占 3 行。\n- 建议：这是论文最核心的 confound，应该在 Discussion 中有一个独立 paragraph 系统讨论三种 alternative explanations 和可能的 disambiguation 方案（e.g., 测试 Llama-3 70B native model 或 Qwen-2.5 7B distilled model）。\n\n**W5 [warning] High FPR on safe traces (39-62%) 与 deployment framing 矛盾。**\n- 具体位置：Limitations §5, Discussion ¶3 (\"Deployment implications\"), Conclusion ¶4\n- 问题：Limitations 中承认所有方法在纯 safe traces 上 FPR 为 39-62%，但 Discussion 和 Conclusion 仍然用 \"deployment recommendations\" 的 framing 给出实践建议。一个 FPR 40%+ 的系统在任何生产环境中都不可用。这种 framing gap 会让审稿人感到 disconnect。\n- 建议：将 \"deployment recommendations\" 改为 \"design guidelines for future monitoring systems\" 或类似措辞，明确当前方法是 diagnostic tool 而非 production-ready。\n\n**W6 [info] \"Discussion and Conclusion\" 合并节与 Experiments 的叙事重复。**\n- 具体位置：sections/conclusion.tex 全文 vs sections/experiments.tex\n- 问题：Conclusion 的前三个 paragraph（temporal dominance, model-dependent, method boundaries）几乎逐句重复 Section 5 的结论，仅增加少量解释。对 8-page 正文而言，0.5-1 page 的重复浪费了宝贵空间。\n- 建议：Conclusion 应极度精简（1 paragraph recap + future work），把省出的空间用于扩展 Discussion 中 W4 指出的 confound 分析。\n\n**W7 [info] CP 定义的 annotation reliability 未报告。**\n- 具体位置：Section 3.1, Limitations §3\n- 问题：Safety Commitment Point 定义为\"the first step after which safety reasoning permanently ceases\"，但 Limitations 承认\"edge cases exist where models oscillate\"且\"have not yet conducted inter-annotator agreement studies\"。对于一个以 CP detection 为核心任务的论文，不报告 IAA 是一个明显缺陷。HarmThoughts 数据集是否提供了 IAA 数据？\n- 建议：至少报告 HarmThoughts 原始 annotation 的 IAA（如果有），或在 5 个随机 sample 上做 pilot IAA study。\n\n---\n\n## Questions to Authors\n\n1. Abstract 中 \"both surviving Bonferroni correction\" 仅适用于 R1-8B。能否在 Abstract 中明确限定这是 R1-8B 的结果，避免读者误以为是跨模型结论？\n\n2. Table 3 (HS vs Text) 中 QwQ-32B 的 text probe FPR (17.8%) 优于 HS (20.8%)，但正文仅在一句中提及。在 QwQ-32B 上 text probe 是否 Pareto-dominate HS probe？如果是，这应该在 Contribution 2 中明确。\n\n3. Oracle gap analysis (Section 5.7) 的 85.5% 是如何计算的？(+31 - +4.5) / +31 = 85.5%？这个 metric 是否对 oracle 的 lead time 选择敏感？K=5 的选择依据是什么？\n\n4. 为什么 text probe 用 all-MiniLM-L6-v2 (384-d) 而非更强的 encoder (e.g., E5-large, GTE-large)? 如果用更强的 text encoder，modality gap 可能缩小甚至逆转。\n\n5. Layer selection (R1-8B: layer 14/32, R1-32B: layer 10/64, QwQ-32B: layer 2/64) 的巨大差异是否意味着不同模型的 safety information 编码位置完全不同？这对 Contribution 3 (transfer failure) 的解释有何意义？\n\n---\n\n## Round 1 Issue Resolution Check\n\n| Issue | Status | Evidence |\n|-------|--------|----------|\n| **C1**: 标题 overclaim | ✅ Resolved | 新标题 \"Temporal Probing for Safety Commitment Detection in Reasoning Models\" 描述性强，无 overclaim |\n| **C6**: Related Work 从 14 citations 扩展 | ✅ Resolved | 32 references, 6 thematic paragraphs, 覆盖 probing/causal/safety/PRM/cross-model |\n| **S8**: \"HS > text\" novelty 论证 | ✅ Resolved | 重新 framing 为 \"temporal > modality\"，有完整 window sweep 支撑 |\n| **S9**: Correlation vs causation 声明 | ✅ Resolved | Limitations §2 明确声明 \"does not demonstrate causal\" |\n| **S10**: PRM 联系 | ✅ Resolved | Related Work ¶5 \"Process Supervision and Sequential Monitoring\" 明确讨论 |\n| **F1**: LaTeX 模板官方 | ✅ Resolved | acl.sty 来自 github.com/acl-org/acl-style-files/, `\\usepackage[review]{acl}` |\n| **F2**: Responsible NLP Checklist | ✅ Resolved | Appendix A 完整填写 |\n| **F3**: References 格式 | ✅ Resolved | 使用 acl_natbib.bst, natbib commands (citep/citet) |\n| **F4**: Table 格式统一 | ✅ Resolved | 所有表格使用 booktabs (toprule/midrule/bottomrule)，格式一致 |\n\n**所有 Round 1 问题均已解决。**\n\n---\n\n## Overall Assessment\n\n**Soundness**: 3.5/5 — 实验设计规范，统计方法正确，但 power 不足和 confound 问题限制了结论强度。\n\n**Excitement**: 2.5/5 — \"Temporal context matters more than modality\" 的 finding 有价值但 methodological contribution 缺失，takeaway 偏向常识（\"多看几步更准\"）。对于纯 empirical study，novelty ceiling 限制了 excitement。\n\n**Reproducibility**: 4/5 — 所有超参报告完整，数据来自公开 benchmark，计算量极低。代码未提供但承诺 release。\n\n**Overall**: 3.0/5 (Findings acceptance)\n\n**一句话总评**: 一篇方法论严谨、统计规范的 empirical study，Round 1 遗留问题全部解决，但缺乏 methodological novelty 且核心 claim 受 statistical power 和 confound 限制，更适合 Findings 而非 main conference track。",
    "reviewer_id": "2",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-17T04:28:12.426925+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3685
}
```

</details>

---


### Assistant

_source line 136 · 2026-05-17T04:28:18.247620+00:00_

审稿报告已提交给 Review Director。

核心判断：论文在 Round 1 后改善显著（所有格式和结构问题已修复），实验方法严谨、统计规范。主要限制是 (1) 纯 empirical study 缺乏 methodological novelty，(2) 32B 模型统计 power 不足使核心 claim 之一（model-dependent advantage）standing on weak ground，(3) architecture/scale/distillation 三重 confound。建议评级 3.0/5，适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2"
}
```

</details>

---


## Round 4

## Round 4

4 recorded events


### User

_source line 137 · 2026-05-17T04:29:01.874362+00:00_

[Round 2 审稿请求]:
## 交叉分享 — Reviewer 1 的完整审稿意见

以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Weakness 和 Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 1 Weaknesses:

**W1 [critical] 多重比较校正不完整。** Bonferroni 只校正 3 models (α=0.017)，但每模型内同时测 3 metrics (acc, prec, FPR)。完整应为 α=0.0056 (9 tests)。R1-8B accuracy p=0.005 在 α=0.0056 下为边际。需论证为何不校正指标数（如 metrics 非独立）或改用 FDR。

**W2 [critical] Cross-model transfer "PCA alignment" 实现完全缺失。** Section 5.6 仅一段话，无 components 数、对齐方法(Procrustes/CCA?)、不同维度模型映射方式、projection head 训练数据。Negative result 不可复现。

**W3 [warning] 排除 23% test traces (10/43 undefined precision) 需更强论证。** 可能系统性偏向某类 trace。建议报告被排除 traces 特征分布或用 F1 替代。

**W4 [warning] QwQ-32B position baseline > HS probe 对核心 claim 的冲击未讨论。** Position baseline 70.6% > HS 67.8%，temporal window 改善可能仅因给了更多位置信息。

**W5 [warning] Multi-layer GRU per-seed 数据缺失。** Main text 报告 best result (+4.5±3.0)，但 Appendix 只有 single-layer per-seed。

**W6 [warning] R1-32B non-monotonic window 解释薄弱。** 归因 "overfitting on smaller dataset" 但未验证（val 是否同步下降？增强正则能否缓解？）。

**W7 [info] Figure 3 bootstrap CI 方法未说明（percentile/BCa）。

**W8 [info] Oracle gap 85.5% 的 framing 过于绝对。** Oracle 是不可达上界，"information gap" 用语暗示可弥合。

---

### Reviewer 1 Questions:

1. Bonferroni 只校正模型数不校正指标数的理由？metrics 间相关性估计？
2. PCA alignment 具体方法？保留 components 数？不同维度如何映射？projection head 训练数据？
3. 被排除 10 条 traces 的长度和 CP 位置是否与其余 33 条有统计差异？
4. QwQ-32B 是否尝试过 residual probe（去除 position 信号后再 probe）？
5. R1-32B 在 W=15/20/25 时 val set 是否也 degrade？

---

### Reviewer 1 Overall: 3.5/5 (Borderline Conference)

请对以上每条 W1-W8 和 Q1-Q5 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-17T04:30:30.136891+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1 意见\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R1-W1: 多重比较校正不完整。**\n同意这是一个有意义的统计方法论问题。论文在 Section 3.2 仅声明 \"Bonferroni correction (α=0.017, 3 models)\" 但未论证为何不校正 metrics 数量。三个 metrics (acc, prec, FPR) 虽然从同一 confusion matrix 派生故存在相关性，但论文未提供这一论证。在 α=0.0056 下，R1-8B accuracy p=0.005 确实为边际显著。不过我补充一点：precision p<0.001 在任何合理校正下仍然显著，所以 R1-8B 的核心 claim (HS dominance) 不会因此完全崩塌，只是从\"三指标全显著\"降级为\"precision 显著 + accuracy 边际\"。建议作者在 revision 中加入 metrics 非独立性的显式论证（如报告 metrics 间 Pearson correlation）或改用 Holm-Bonferroni/FDR。\n\n**[AGREE] R1-W2: Cross-model transfer PCA alignment 实现缺失。**\n完全同意。Section 5.6 仅一段话（3行），作为 Contribution 3 (\"comprehensive negative results\") 的核心支撑之一，这个实验的 reproducibility 是零。我在自己的审稿中没有单独列出这一点，但 Reviewer 1 指出后确认这是一个 critical gap。具体需要补充：(1) PCA components 保留数及选择标准, (2) 不同维度模型（4096 vs 5120）的对齐方法, (3) 是否尝试了 Procrustes/CCA 等替代方案, (4) alignment 是否在 train split 上拟合。没有这些，\"transfer fails entirely\" 的 claim 无法验证——也许只是 alignment 方法选择不当。\n\n**[AGREE] R1-W3: 排除 23% traces 需更强论证。**\n部分同意。论文脚注声称排除是 \"conservative\"（Section 5.2），但未提供被排除 10 条 traces 的特征分析。10/43 = 23% 的排除率不低。我同意 Reviewer 1 的建议——报告被排除 traces 的长度分布和 CP 位置，或使用 F1 (定义 precision=0 when TP=0) 作为替代 metric 进行 sensitivity analysis。不过我认为 severity 应为 info 而非 warning，因为论文脚注的逻辑是自洽的（\"both probes correctly abstain\" → 排除不利于 HS probe），只是需要数据验证��\n\n**[AGREE] R1-W4: QwQ-32B position baseline > HS probe 的冲击。**\n同意且这一点与我的 W4 (architecture/scale/distillation confound) 相关。Section 5.4 报告 position baseline 70.6% > HS probe 67.8% on QwQ-32B，但 Discussion 中未充分讨论其对 \"temporal > modality\" claim 的含义。如果 temporal windowing 的收益主要来自给 probe 更多位置信息（而非更丰富的 temporal dynamics），那么核心 finding 的 interesting-ness 大幅降低——它变成了 \"knowing where you are in the trace helps\"，这是 trivial 的。\n\n不过我补充一个 nuance：在 R1-8B 上，HS probe 明确优于 position baseline (FPR 8.1% vs 15.8%，Section 5.4)，说明 R1-8B 的 hidden states 确实编码了超越位置的安全信息。问题是 QwQ-32B layer 2 (仅 3.1% depth) 的选择本身可能就有问题——如此浅的 layer 主要编码 token-level / positional features 是合理的。论文需要讨论：QwQ-32B 的 best-layer 如此浅是否反映了 layer selection metric 的局限性，而非模型本身缺乏深层安全信号。\n\n**[AGREE] R1-W5: Multi-layer GRU per-seed 数据缺失。**\n同意。Main text Section 5.3 报告 \"best result (R1-8B multi-layer GRU) achieves +4.5±3.0 steps lead with 72.9% crossing accuracy\"，但 Appendix C Table 6 只有 single-layer GRU per-seed 数据（mean lead +3.5±2.3）。数据不匹配——main text 的 +4.5 来自 multi-layer 但 appendix 报告的是 single-layer 的 +3.5。这是 reproducibility gap，需要补充 multi-layer per-seed 表格���\n\n**[AGREE] R1-W6: R1-32B non-monotonic window 解释薄弱。**\n同意。Appendix B 将 W>10 的 accuracy 下降归因于 \"overfitting on smaller dataset (n=100)\" 但这是 speculation without evidence。如果是 overfitting，应该能在 val set 上观察到类似趋势，或通过增强正则化缓解。论文未提供任何验证。我在自己的审稿中没有单独提出这一点，但认为 Reviewer 1 的质疑是合理的——至少应报告 val set 在 W=15/20/25 时的表现。\n\n**[AGREE] R1-W7: Figure 3 CI 方法未说明。**\n同意，属于 minor reporting gap。Figure 3 caption 说 \"bootstrap 95% CIs\" 但未指定 percentile vs BCa vs normal approximation。对于小样本 (n=19-43) 且可能偏斜的 FPR 分布，method 选择会影响 CI 宽度。应在 caption 或方法节中补充。\n\n**[REBUT] R1-W8: Oracle gap framing 过于绝对。**\n部分不同意。论文在 Section 5.7 和 Discussion ¶5 中确实使用了 \"fundamental bottleneck\" 和 \"information gap\" 的措辞，Reviewer 1 认为暗示可弥合但实际不可达。然而，论文在 Discussion ¶5 最后明确写道：\"the model at step t has not yet 'decided' what it will do at step t+k for large k, and no amount of representational analysis can extract information that does not yet exist in the computation.\" 这句话已经表达了 \"不可达\" 的含义。我认为 \"information gap\" 的用语确实可以改进（如改为 \"performance ceiling\"），但论文的实际论述并未暗示这个 gap 完全可弥合。Severity 应为 info 而非 warning。\n\n---\n\n### Questions 逐条回应\n\n**[AGREE] Q1: Bonferroni 只校正模型数不校正指标数的理由？**\n同上 W1 回应。论文确实缺乏对这一选择的显式论证。需要补充。\n\n**[AGREE] Q2: PCA alignment 具体方法？**\n同上 W2 回应。完全缺失，需要补充完整实验细节。\n\n**[AGREE] Q3: 被排除 traces 的统计特征？**\n合理要求。论文应至少报告被排除 10 条 traces 的平均长度和 CP 相对位置，以排除系统性偏差。\n\n**[AGREE] Q4: Residual probe 去除 position 信号？**\n好建议。如果 QwQ-32B 在去除 position 信号后 HS probe 表现下降，则证实 layer 2 主要编码 positional 信息；如果保持，则证实有独立安全信号。这是一个 actionable experiment 建议。\n\n**[AGREE] Q5: R1-32B val set 在大 window 时是否也 degrade？**\n同上 W6 回应。这是验证 \"overfitting\" 假说的最直接方式。\n\n---\n\n### 总结\n\nReviewer 1 的 8 条 Weakness 中，我同意 7 条（W1-W7），对 1 条部分反驳（W8，论文已在 Discussion 中 qualify 了 oracle gap 的不可达性）。5 个 Questions 全部同意需要作者回应。\n\n**最关键的共识问题**：W2 (transfer 实验不可复现) 和 W4 (position baseline 对 temporal claim 的冲击) 与我的审稿意见形成交叉验证，是 revision 中必须解决的问题。\n\n**我和 Reviewer 1 的分歧**：我对 W3 的 severity 评估较低（info vs warning），因为排除逻辑是自洽的，只是缺数据验证。\n\n**我的额外关注**（Reviewer 1 未提及）：(1) Abstract 过长/数据堆砌问题, (2) Novelty ceiling (纯 empirical study 无 methodological contribution), (3) Safe trace FPR 39-62% 与 deployment framing 的矛盾。这三点是我认为区分 \"Findings vs Main\" 的关键因素。",
  "reviewer_id": "2",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 交叉回应 Reviewer 1 意见\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R1-W1: 多重比较校正不完整。**\n同意这是一个有意义的统计方法论问题。论文在 Section 3.2 仅声明 \"Bonferroni correction (α=0.017, 3 models)\" 但未论证为何不校正 metrics 数量。三个 metrics (acc, prec, FPR) 虽然从同一 confusion matrix 派生故存在相关性，但论文未提供这一论证。在 α=0.0056 下，R1-8B accuracy p=0.005 确实为边际显著。不过我补充一点：precision p<0.001 在任何合理校正下仍然显著，所以 R1-8B 的核心 claim (HS dominance) 不会因此完全崩塌，只是从\"三指标全显著\"降级为\"precision 显著 + accuracy 边际\"。建议作者在 revision 中加入 metrics 非独立性的显式论证（如报告 metrics 间 Pearson correlation）或改用 Holm-Bonferroni/FDR。\n\n**[AGREE] R1-W2: Cross-model transfer PCA alignment 实现缺失。**\n完全同意。Section 5.6 仅一段话（3行），作为 Contribution 3 (\"comprehensive negative results\") 的核心支撑之一，这个实验的 reproducibility 是零。我在自己的审稿中没有单独列出这一点，但 Reviewer 1 指出后确认这是一个 critical gap。具体需要补充：(1) PCA components 保留数及选择标准, (2) 不同维度模型（4096 vs 5120）的对齐方法, (3) 是否尝试了 Procrustes/CCA 等替代方案, (4) alignment 是否在 train split 上拟合。没有这些，\"transfer fails entirely\" 的 claim 无法验证——也许只是 alignment 方法选择不当。\n\n**[AGREE] R1-W3: 排除 23% traces 需更强论证。**\n部分同意。论文脚注声称排除是 \"conservative\"（Section 5.2），但未提供被排除 10 条 traces 的特征分析。10/43 = 23% 的排除率不低。我同意 Reviewer 1 的建议——报告被排除 traces 的长度分布和 CP 位置，或使用 F1 (定义 precision=0 when TP=0) 作为替代 metric 进行 sensitivity analysis。不过我认为 severity 应为 info 而非 warning，因为论文脚注的逻辑是自洽的（\"both probes correctly abstain\" → 排除不利于 HS probe），只是需要数据验证��\n\n**[AGREE] R1-W4: QwQ-32B position baseline > HS probe 的冲击。**\n同意且这一点与我的 W4 (architecture/scale/distillation confound) 相关。Section 5.4 报告 position baseline 70.6% > HS probe 67.8% on QwQ-32B，但 Discussion 中未充分讨论其对 \"temporal > modality\" claim 的含义。如果 temporal windowing 的收益主要来自给 probe 更多位置信息（而非更丰富的 temporal dynamics），那么核心 finding 的 interesting-ness 大幅降低——它变成了 \"knowing where you are in the trace helps\"，这是 trivial 的。\n\n不过我补充一个 nuance：在 R1-8B 上，HS probe 明确优于 position baseline (FPR 8.1% vs 15.8%，Section 5.4)，说明 R1-8B 的 hidden states 确实编码了超越位置的安全信息。问题是 QwQ-32B layer 2 (仅 3.1% depth) 的选择本身可能就有问题——如此浅的 layer 主要编码 token-level / positional features 是合理的。论文需要讨论：QwQ-32B 的 best-layer 如此浅是否反映了 layer selection metric 的局限性，而非模型本身缺乏深层安全信号。\n\n**[AGREE] R1-W5: Multi-layer GRU per-seed 数据缺失。**\n同意。Main text Section 5.3 报告 \"best result (R1-8B multi-layer GRU) achieves +4.5±3.0 steps lead with 72.9% crossing accuracy\"，但 Appendix C Table 6 只有 single-layer GRU per-seed 数据（mean lead +3.5±2.3）。数据不匹配——main text 的 +4.5 来自 multi-layer 但 appendix 报告的是 single-layer 的 +3.5。这是 reproducibility gap，需要补充 multi-layer per-seed 表格���\n\n**[AGREE] R1-W6: R1-32B non-monotonic window 解释薄弱。**\n同意。Appendix B 将 W>10 的 accuracy 下降归因于 \"overfitting on smaller dataset (n=100)\" 但这是 speculation without evidence。如果是 overfitting，应该能在 val set 上观察到类似趋势，或通过增强正则化缓解。论文未提供任何验证。我在自己的审稿中没有单独提出这一点，但认为 Reviewer 1 的质疑是合理的——至少应报告 val set 在 W=15/20/25 时的表现。\n\n**[AGREE] R1-W7: Figure 3 CI 方法未说明。**\n同意，属于 minor reporting gap。Figure 3 caption 说 \"bootstrap 95% CIs\" 但未指定 percentile vs BCa vs normal approximation。对于小样本 (n=19-43) 且可能偏斜的 FPR 分布，method 选择会影响 CI 宽度。应在 caption 或方法节中补充。\n\n**[REBUT] R1-W8: Oracle gap framing 过于绝对。**\n部分不同意。论文在 Section 5.7 和 Discussion ¶5 中确实使用了 \"fundamental bottleneck\" 和 \"information gap\" 的措辞，Reviewer 1 认为暗示可弥合但实际不可达。然而，论文在 Discussion ¶5 最后明确写道：\"the model at step t has not yet 'decided' what it will do at step t+k for large k, and no amount of representational analysis can extract information that does not yet exist in the computation.\" 这句话已经表达了 \"不可达\" 的含义。我认为 \"information gap\" 的用语确实可以改进（如改为 \"performance ceiling\"），但论文的实际论述并未暗示这个 gap 完全可弥合。Severity 应为 info 而非 warning。\n\n---\n\n### Questions 逐条回应\n\n**[AGREE] Q1: Bonferroni 只校正模型数不校正指标数的理由？**\n同上 W1 回应。论文确实缺乏对这一选择的显式论证。需要补充。\n\n**[AGREE] Q2: PCA alignment 具体方法？**\n同上 W2 回应。完全缺失，需要补充完整实验细节。\n\n**[AGREE] Q3: 被排除 traces 的统计特征？**\n合理要求。论文应至少报告被排除 10 条 traces 的平均长度和 CP 相对位置，以排除系统性偏差。\n\n**[AGREE] Q4: Residual probe 去除 position 信号？**\n好建议。如果 QwQ-32B 在去除 position 信号后 HS probe 表现下降，则证实 layer 2 主要编码 positional 信息；如果保持，则证实有独立安全信号。这是一个 actionable experiment 建议。\n\n**[AGREE] Q5: R1-32B val set 在大 window 时是否也 degrade？**\n同上 W6 回应。这是验证 \"overfitting\" 假说的最直接方式。\n\n---\n\n### 总结\n\nReviewer 1 的 8 条 Weakness 中，我同意 7 条（W1-W7），对 1 条部分反驳（W8，论文已在 Discussion 中 qualify 了 oracle gap 的不可达性）。5 个 Questions 全部同意需要作者回应。\n\n**最关键的共识问题**：W2 (transfer 实验不可复现) 和 W4 (position baseline 对 temporal claim 的冲击) 与我的审稿意见形成交叉验证，是 revision 中必须解决的问题。\n\n**我和 Reviewer 1 的分歧**：我对 W3 的 severity 评估较低（info vs warning），因为排除逻辑是自洽的，只是缺数据验证。\n\n**我的额外关注**（Reviewer 1 未提及）：(1) Abstract 过长/数据堆砌问题, (2) Novelty ceiling (纯 empirical study 无 methodological contribution), (3) Safe trace FPR 39-62% 与 deployment framing 的矛盾。这三点是我认为区分 \"Findings vs Main\" 的关键因素。",
    "reviewer_id": "2",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-17T04:30:34.665481+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4528
}
```

</details>

---


### Assistant

_source line 140 · 2026-05-17T04:30:38.721969+00:00_

交叉回应已提交。对 Reviewer 1 的 8 条 Weakness 中 7 条表示同意，对 W8 (oracle gap framing) 部分反驳（论文已在 Discussion 中明确了不可达性）。5 个 Questions 全部同意需要作者回应。核心共识集中在 transfer 实验不可复现 (W2) 和 position baseline 对 temporal claim 的冲击 (W4)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2"
}
```

</details>

---


## Round 5

## Round 5

46 recorded events


### User

_source line 141 · 2026-05-17T11:31:36.376119+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 完整性 + 写作质量**

### 论文信息
- **标题**: "Temporal Probing for Safety Commitment Detection in Reasoning Models"
- **论文路径**: `projects/contrastive_trace_safety/docs/paper/main.tex`（sections/ 子目录包含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex）
- **References**: `references.bib`（32 篇引用）

### 目标 Venue
- **EMNLP 2026** via ARR May cycle
- **Deadline**: 2026-05-25
- **页数限制**: 8 页正文 + unlimited references（Long Paper）
- **模板**: ACL official style，`\usepackage[review]{acl}`
- **匿名规则**: Double-blind
- **附加要求**: Limitations section（不计页数）+ Responsible NLP Research Checklist

### 你的审查重点

请从以下维度严格审查，每个 Weakness 必须给出具体的 section/table/figure 引用：

1. **新颖性与贡献定位**
   - "Temporal context dominates modality choice" 是否构成足够新颖的 contribution？这是否只是 "more features = better performance" 的特殊情况？
   - 纯 empirical study（无新方法提出）在 EMNLP main track 的竞争力？是否更适合 Findings track？
   - 三条 contributions 是否都有充分的实验支撑？是否存在 overclaim？
   - 与 TrajGuard、SafeSwitch、SIREN 等 hidden-state safety detection 工作的增量贡献是否清楚？

2. **Related Work 覆盖度与 Positioning**
   - 32 篇引用是否覆盖了所有关键方向？有无遗漏的重要相关工作？
   - 特别关注：reasoning model safety（2025-2026 最新工作）、temporal/sequential probing methods、safety monitoring in deployment
   - Related Work 是否做了充分的 positioning（不是 survey，而是说明自己的位置）？
   - 用 WebSearch 搜索 2025-2026 年最新的 reasoning model safety 和 hidden-state probing 论文，检查是否有遗漏

3. **叙事连贯性与写作质量**
   - Abstract → Introduction → Method → Experiments → Conclusion 是否形成一条统一主线？
   - Abstract 是否过长/数据堆砌？是否在 30 秒内传达了核心价值？
   - 是否存在 AI 写作标志（破折号、-ing 短语结尾、过度分段、"Furthermore/Moreover" 堆砌）？
   - Discussion + Conclusion 合并后是否仍有重复？空间利用是否高效？
   - Limitations section 是否全面且诚实？

4. **格式合规性**
   - ACL 模板使用是否正确？
   - 页数是否符合 8 页限制（正文）？
   - 图表质量：caption 是否自包含？数字精度是否一致？最优结果是否加粗？
   - 引用格式是否一致（natbib）？bib 条目是否完整（venue, year, pages）？
   - NLP Checklist 是否认真填写？
   - 匿名化是否彻底（无作者信息泄露）？

5. **Bug disclosure (Appendix F)**
   - QwQ-32B text probe bug 的 disclosure 是否充分？对结论的影响评估是否可信？

### 输出格式

```
## Summary
[2-3句]

## Strengths
[S1] ...
[S2] ...

## Weaknesses
[W1] [severity: critical/warning/info] ...
[W2] ...

## Questions
[Q1] ...

## Missing References
[如有]

## Overall Assessment
Score: [strong reject / weak reject / borderline / weak accept / strong accept]
Confidence: [1-5]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-17T11:31:49.952148+00:00_

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
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
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

_source line 143 · 2026-05-17T11:31:49.952715+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-17T11:31:54.413237+00:00_

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
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 145 · 2026-05-17T11:31:55.317035+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 146 · 2026-05-17T11:31:56.120778+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{subcaption}
11	\usepackage{xcolor}
12	\usepackage{colortbl}
13	\usepackage{hyperref}
14	\usepackage{cleveref}
15	
16	\title{Temporal Probing for Safety Commitment Detection in Reasoning Models}
17	
18	\author{Anonymous ARR Submission}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{sections/abstract}
25	\end{abstract}
26	
27	\input{sections/introduction}
28	
29	\input{sections/related_work}
30	
31	\input{sections/method}
32	
33	\input{sections/experiments}
34	
35	\input{sections/conclusion}
36	
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\input{sections/appendix}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 147 · 2026-05-17T11:31:56.221476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 148 · 2026-05-17T11:31:56.373831+00:00_

1	Large Language Models (LLMs) with Chain-of-Thought (CoT) reasoning can self-jailbreak: their extended reasoning traces sometimes transition from safe deliberation to committed harmful generation. Detecting this safety commitment in real time is essential for monitoring systems, yet no prior work has systematically compared hidden-state (HS) probes against text-based monitors for this task. We present the first cross-model evaluation of temporal probing for safety commitment detection, spanning four reasoning models, two architectures (Llama, Qwen), two training methods (R1 distillation, STILL), and two scales (7-8B, 32B). Our results reveal that temporal context dominates modality choice: expanding the observation window improves precision by up to 12.9 percentage points (pp) and reduces false positive rate across all conditions. The residual modality advantage is scale-dependent: at 7-8B, HS probes significantly outperform text probes on both tested models (R1-8B precision +22.4pp, $p{<}0.001$; OT-7B precision +21.2pp, $p{<}0.001$; 5/12 tests surviving Holm-Bonferroni correction), while at 32B no significant difference emerges on either model. Geometric distance methods, change-point detectors, and cross-model transfer all fail, defining clear boundaries of current approaches. Control tasks confirm genuine safety structure (selectivity 7.5--18.3pp above chance).
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 149 · 2026-05-17T11:31:56.374268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 150 · 2026-05-17T11:31:56.424887+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Reasoning models such as DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq} have advanced language model capabilities by scaling chain-of-thought (CoT) inference, producing extended internal deliberation before generating final responses. These models interleave safety-aware reasoning with content generation across dozens of reasoning steps, and this very capacity for self-reflection introduces a new failure mode. Recent work has documented that reasoning models can ``self-jailbreak'': even without adversarial input modifications, the model's own CoT may transition from considering safety constraints to committing to produce harmful content~\cite{harmthoughts,selfjailbreak}. In such cases, the model's reasoning trace contains a \textbf{Safety Commitment Point} (CP), the first step after which safety reasoning permanently ceases and harmful generation proceeds unchecked. Detecting this transition in real time is essential for monitoring systems that must intervene before harmful content reaches users.
4	
5	Existing safety detectors were designed for a different threat model. Methods based on hidden-state (HS) probing, such as TrajGuard~\cite{trajguard} and SafeSwitch~\cite{safeswitch}, monitor internal activations to classify adversarial inputs and achieve high accuracy (above 95\%) on standard Large Language Models (LLMs). Text-based monitors like SafeRemind~\cite{saferemind} and SafeThink~\cite{safethink} scan generated reasoning text for safety violations. Both families target external attacks on model inputs rather than the model's own internal commitment process. A fundamental question remains unanswered: when detecting safety commitment within multi-step reasoning, should a monitoring system read the model's hidden states or its generated text? Intuition suggests that HS features (4096 dimensions of internal computation) should be far more informative than text embeddings (384 dimensions from a sentence encode
…[truncated 3783 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-17T11:32:07.367041+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's a summary of the ACL Rolling Review (ARR) reviewer guidelines, review form criteria, and scoring for 2025-2026:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be ju
…[truncated 1472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 12953
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-17T11:32:11.381462+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-17T11:32:11.532780+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Probing Neural Representations.}
4	Linear probes are a standard tool for investigating learned representations~\citep{alain2017understanding,belinkov2017morphology,conneau2018probing,belinkov2019analysis}. \citet{hewitt2019structural} show that syntax trees are linearly recoverable from contextual embeddings. \citet{hewitt2019control} introduce control tasks and selectivity to distinguish genuine signal from probe memorization. We extend probing from linguistic to safety-relevant properties, adopting the control task methodology to validate our probes.
5	
6	\paragraph{Causal Interpretability.}
7	Causal abstraction~\citep{geiger2021causal}, causal mediation analysis~\citep{vig2020causal}, ROME~\citep{meng2022locating}, and ACDC~\citep{conmy2023circuit} establish causal relationships between representations and model behavior. These methods require expensive interventions during inference. Our approach is explicitly correlational: we establish that safety commitment is \textit{decodable} from hidden states without claiming causality, trading causal guarantees for practical applicability.
8	
9	\paragraph{Hidden-State Safety Detection.}
10	TrajGuard~\citep{trajguard} uses Mahalanobis distance on hidden-state trajectories, SafeSwitch~\citep{safeswitch} trains hidden-state classifiers for safety interventions, and SIREN~\citep{siren} monitors internal representations during generation. Representation Engineering~\citep{zou2023representation} identifies linear safety directions, and \citet{arditi2024refusal} show refusal is mediated by a single direction. These works identify static safety directions; we study the \textit{temporal evolution} of safety commitment during multi-step reasoning. On the attack side, GCG~\citep{zou2023gcg} generates universal adversarial suffixes, while SmoothLLM~\citep{robey2023smoothllm} and perplexity filtering~\citep{alon2023perplexity} defend at the input level. We focus on det
…[truncated 1993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-17T11:32:11.583447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-17T11:32:12.085582+00:00_

1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	\subsection{Safety Commitment Point}
5	\label{sec:commitment-point}
6	
7	When a reasoning model is jailbroken, its CoT transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first step after which safety reasoning permanently ceases. We operationalize this on HarmThoughts~\cite{harmthoughts} traces: the CP is the earliest step $t^*$ such that no subsequent step contains safety reasoning. Steps before CP are \emph{pre-commitment}; steps after are \emph{post-commitment}.
8	
9	\subsection{Metrics}
10	\label{sec:metrics}
11	
12	Let $s_t$ denote the probe score at step $t$, $\tau$ the threshold, and $t^*$ the annotated CP.
13	
14	\textbf{Coverage}: fraction of jailbreak traces where any step exceeds $\tau$. \textbf{Pre-CP FPR}: we report both step-level (pooling all pre-CP steps) and trace-level (mean per-trace FPR, treating each trace as an independent observation for paired statistical comparison). \textbf{Precision}: fraction of threshold-exceeding steps that are post-CP. \textbf{Lead time}: steps between first detection and CP ($t^* - t_{\text{detect}}$).
15	
16	All modality comparisons use a two-sided paired permutation test (1000 resamples) on trace-level values. We conduct 12 hypothesis tests (3 metrics $\times$ 4 models) and apply the Holm-Bonferroni step-down procedure ($\alpha{=}0.05$). Tests are ranked by $p$-value: R1-8B precision ($p{<}0.001$, threshold 0.00417, significant), OT-7B balanced accuracy ($p{<}0.001$, threshold 0.00455, significant), OT-7B precision ($p{<}0.001$, threshold 0.005, significant), OT-7B FPR ($p{<}0.001$, threshold 0.00556, significant), R1-8B accuracy ($p{=}0.005$, threshold 0.00625, significant), R1-8B FPR ($p{=}0.044$, threshold 0.00714, not significant). Five of twelve tests survive correction, contributed by two independent models at 7-8B scale. This procedure treats all metrics as indepe
…[truncated 3665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-17T11:32:12.086070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-17T11:32:12.588083+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate contrastive trace probes across four reasoning models (R1-8B, OT-7B, R1-32B, QwQ-32B), two signal modalities (hidden states and text), and multiple temporal aggregation strategies. Our experiments address four questions: (1) How much does temporal context improve detection? (2) Does the choice of signal modality matter? (3) Can sequence models detect unsafe reasoning earlier? (4) Do probes transfer across models?
5	
6	\subsection{Temporal Context as Primary Factor}
7	\label{sec:temporal_primary}
8	
9	The most consistent finding across all experimental conditions is that temporal context improves probe precision and reduces FPR across all four models and both modalities. For HS probes, all four models show improving precision and FPR with larger windows; OT-7B balanced accuracy is the exception, peaking at $W{=}3$ and declining at larger windows while its precision and FPR continue to improve. \cref{fig:window_ablation} shows the pattern for R1-8B.
10	
11	\begin{figure}[t]
12	\centering
13	\includegraphics[width=\columnwidth]{figures/fig2_temporal_improvement.pdf}
14	\caption{Effect of temporal window size on R1-8B HS probe performance. Precision increases monotonically from 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR decreases from 9.65\% to 4.83\%. Coverage decreases as larger windows make the probe more conservative.}
15	\label{fig:window_ablation}
16	\end{figure}
17	
18	On R1-8B, increasing window size from $W{=}1$ to $W{=}25$ improves balanced accuracy from 77.8\% to 81.0\% (+3.2pp), precision from 69.3\% to 82.2\% (+12.9pp), and reduces step-level FPR from 9.65\% to 4.83\% ($-$4.8pp). QwQ-32B shows a similar monotonic pattern (+3.2pp accuracy, +7.4pp precision, $-$5.9pp FPR from $W{=}1$ to $W{=}25$). R1-32B exhibits a non-monotonic trajectory: accuracy peaks at $W{=}10$ then declines below the $W{=}1$ baseline by $W{=}25$ (71.8\% $\rightarrow$ 70.3\%), though precision and FPR still improve (+1.7
…[truncated 14094 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-17T11:32:12.889531+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-17T11:32:12.990365+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	\paragraph{Why temporal context dominates.}
4	Information-theoretic reasoning suggests that hidden states (4096 dimensions) should dominate text features (384 dimensions) by a wide margin. In practice, the temporal dimension matters more than signal richness. Text probes benefit universally from temporal context across all four models. HS probes show improving precision and FPR on all four models; OT-7B balanced accuracy saturates at $W{=}3$, though precision and FPR continue improving through $W{=}20$. Safety commitment is a gradual process: the model progressively consolidates intent over multiple steps, and observing this progression provides the dominant information gain.
5	
6	\paragraph{Position signal as supporting evidence.}
7	On QwQ-32B, the position-only baseline (70.6\%) slightly exceeds the HS probe at layer 2 (67.8\%), directly supporting the core thesis: safety commitment on this model is inferable from temporal position ($p{=}0.828$ for HS vs.\ text). Optimal probe depth varies by scale: 7-8B models select mid-depth layers (R1-8B 44\%, OT-7B 57\%), while 32B models favor shallow layers (QwQ-32B 3\%, R1-32B 16\%) where positional features dominate. All models maintain high selectivity (7.5--18.3pp), confirming genuine learned structure regardless of whether position provides a competitive alternative signal.
8	
9	\paragraph{Scale as the primary moderator.}
10	OT-7B partially resolves the confound between architecture, scale, and training method. R1-8B (Llama, R1-distilled) and OT-7B (Qwen, STILL-trained) share the 7-8B scale but differ in architecture and training; both show significant HS advantages, ruling out architecture and training as sole explanations. Conversely, R1-32B and QwQ-32B share the 32B scale and neither shows significant HS advantages despite different training paradigms, making scale the primary moderator. Whether the 32B non-significance reflects scale per se or an inte
…[truncated 2317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-17T11:32:26.056168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-17T11:32:26.559521+00:00_

1	\section{Limitations}\label{sec:limitations}
2	
3	\paragraph{Statistical power and operating point confounds.}
4	At 7-8B, both R1-8B and OT-7B show significant HS advantages (5/12 tests surviving Holm-Bonferroni). OT-7B achieves Pareto dominance with all three metrics significant ($p{<}0.001$); R1-8B shows significant precision ($p{<}0.001$) and accuracy ($p{=}0.005$), with FPR directionally favorable ($p{=}0.044$, not surviving correction). At 32B, HS probes show directional accuracy advantages (+8.4pp on R1-32B, $p{=}0.080$; +0.9pp on QwQ-32B, $p{=}0.828$) but neither survives correction. Each model uses a different optimal window size ($W{=}15, 3, 10, 5$ for R1-8B, OT-7B, R1-32B, QwQ-32B respectively), complicating cross-model modality comparisons. R1-32B shows directional effects of similar magnitude to 7-8B models (+9.4pp precision) but with test sets roughly half the size ($n{=}20$ vs.\ 43--47), limiting detection sensitivity. QwQ-32B shows substantially smaller effects (+0.9pp balanced accuracy), suggesting the non-significance may reflect a genuine absence rather than insufficient power. Future work should prioritize collecting larger R1-32B trace sets ($n{\geq}50$) to resolve this ambiguity.
5	
6	\paragraph{Correlation, not causation.}
7	Our probing methodology establishes that safety commitment is \emph{decodable} from intermediate hidden states. It does not demonstrate that these representations causally drive the model's safe or unsafe behavior. Causal intervention studies, such as activation patching at the identified commitment point, would be necessary to verify that the probed features are mechanistically load-bearing rather than epiphenomenal.
8	
9	\paragraph{Commitment point definition.}
10	The commitment point (CP) annotation relies on detecting the presence or absence of explicit safety reasoning in the chain-of-thought. Edge cases exist where models oscillate between safe and unsafe reasoning, or embed safety-relevant considerations inside oth
…[truncated 1990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-17T11:32:26.560043+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool call

_source line 163 · 2026-05-17T11:32:26.961796+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 164 · 2026-05-17T11:32:27.012718+00:00_

1	@article{trajguard,
2	  title={TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense},
3	  author={Liu, Cheng and Liu, Xiaolei and Li, Xingyu and Xin, Bangzhou and Ding, Kangyi},
4	  journal={arXiv preprint arXiv:2604.07727},
5	  year={2026},
6	  url={https://arxiv.org/abs/2604.07727}
7	}
8	
9	@inproceedings{safeswitch,
10	  title={SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals},
11	  author={Han, Peixuan and Qian, Cheng and Chen, Xiusi and Zhang, Yuji and Ji, Heng and Zhang, Denghui},
12	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
13	  year={2025},
14	  url={https://arxiv.org/abs/2502.01042}
15	}
16	
17	@inproceedings{siren,
18	  title={LLM Safety From Within: Detecting Harmful Content with Internal Representations},
19	  author={Jiao, Difan and Liu, Yilun and Yuan, Ye and Tang, Zhenwei and Du, Linfeng and Wu, Haolun and Anderson, Ashton},
20	  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
21	  year={2026},
22	  url={https://arxiv.org/abs/2604.18519}
23	}
24	
25	@article{saferemind,
26	  title={How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs},
27	  author={Kim, Su-Hyeon and Jin, Hyundong and Lee, Yejin and Han, Yo-Sub},
28	  journal={arXiv preprint arXiv:2601.03662},
29	  year={2026},
30	  url={https://arxiv.org/abs/2601.03662}
31	}
32	
33	@article{safethink,
34	  title={Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away},
35	  author={Ghosal, Soumya Suvra and Chakraborty, Souradip and Singh, Vaibhav and Huang, Furong and Manocha, Dinesh and Bedi, Amrit Singh},
36	  journal={arXiv preprint arXiv:2602.11096},
37	  year={2026},
38	  url={https://arxiv.org/abs/2602.11096}
39	}
40	
41	@article{selfjailbreak,
42	  title={Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training},
43	
…[truncated 11380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-17T11:32:27.114098+00:00_

1	\appendix
2	
3	\section{Responsible NLP Research Checklist}
4	\label{app:checklist}
5	
6	We address the ARR Responsible NLP Research requirements below.
7	
8	\begin{itemize}
9	    \item \textbf{Limitations discussed:} Yes (\cref{sec:limitations}).
10	    \item \textbf{Potential risks:} This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark.
11	    \item \textbf{Computational budget:} Our experiments involve 4 models with 209, 228, 100, and 95 traces respectively (632 total), using linear probes and single-layer GRUs. Total compute is minimal (under 4 GPU-hours on a single RTX A6000). No large-scale pretraining or finetuning was performed.
12	    \item \textbf{Data:} We use HarmThoughts, a publicly available benchmark with step-level safety annotations. No new data collection was performed.
13	    \item \textbf{Human subjects:} No human subjects research was conducted.
14	    \item \textbf{Reproducibility:} All hyperparameters are reported in \cref{app:gru_details,app:bocpd_config}. Code and corrected data will be released upon publication.
15	\end{itemize}
16	
17	
18	\section{Layer Sweep Results}
19	\label{app:layer_sweep}
20	
21	For each model, we sweep all transformer layers and score each candidate layer using the product of balanced accuracy and crossing rate (accuracy-weighted layer selection, defined in \cref{sec:detection-methods}). This composite metric selects layers that simultaneously achieve good classification and reliable threshold crossing on jailbreak traces.
22	
23	The selected layers are: R1-8B layer 14 (of 32, 43.8\% depth), OT-7B layer 16 (of 28, 57\% depth), R1-32B layer 10 (of 64, 15.6\% depth), and QwQ-32B layer 2 (of 64, 3.1\% depth). Optimal layer depth shows a scale-dependent pattern: 7-8B models select mid-depth layers (43.8\%/57\%), whil
…[truncated 27182 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-17T11:32:32.183164+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 soundness excitement overall recommendation scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 soundness excitement overall recommendation scale"
  }
}
```

</details>

---


### Tool call

_source line 167 · 2026-05-17T11:32:32.735872+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "reasoning model safety hidden state probing 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "reasoning model safety hidden state probing 2025 2026 arXiv"
  }
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-17T11:32:33.288165+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"chain of thought\" safety monitoring detection commitment 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"chain of thought\" safety monitoring detection commitment 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-17T11:32:40.173594+00:00_

Web search results for query: "ACL ARR review form 2025 soundness excitement overall recommendation scale"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"},{"title":"ACL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/acl-statistics/acl-2025-statistics/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, I found detailed information about the ACL ARR 2025 review form with the three key scores: soundness, excitement, and overall recommendation.

## Summary of ACL ARR 2025 Review Scores

Starting with 
…[truncated 1823 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7990
}
```

</details>

---


### Tool result

_source line 170 · 2026-05-17T11:32:40.475176+00:00_

Web search results for query: "reasoning model safety hidden state probing 2025 2026 arXiv"

Links: [{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/html/2504.05419v1"},{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification | OpenReview","url":"https://openreview.net/forum?id=O6I0Av7683"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.17305v1"},{"title":"[2504.05419] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/abs/2504.05419"},{"title":"Monitoring Latent World States in Language Models with Propositional Probes | OpenReview","url":"https://openreview.net/forum?id=0yvZm2AjUr"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"Artificial Intelligence","url":"https://arxiv.org/list/cs.AI/new"},{"title":"The Rogue Scalpel: Activation Steering Compromises LLM Safety","url":"https://arxiv.org/html/2509.22067v2"},{"title":"[2502.12659] The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1","url":"https://arxiv.org/abs/2502.12659"},{"title":"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/html/2605.13772"}]

Based on the search results, here are the key findings related to reasoning model safety and hidden state probing from recent arXiv papers in 2025-2026:

## Key Research Papers

**1. Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification**

This April 2025 paper studies recent advances in reasoning models like OpenAI's o1 and DeepSeek-R1. The researchers investigate whether models encode answer correctness by probing hidden states, specifically segmenting Chain-of-Thought sequences into chunks and training a binary classifier to
…[truncated 1289 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7739
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-17T11:32:41.435905+00:00_

Web search results for query: ""chain of thought" safety monitoring detection commitment 2025 2026"

Links: [{"title":"Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety","url":"https://arxiv.org/pdf/2507.11473"},{"title":"[2507.11473] Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety","url":"https://arxiv.org/abs/2507.11473"},{"title":"Reading the Mind of the Machine: Why GPT-5’s Chain-of-Thought Monitoring Matters for AI Safety | American Enterprise Institute - AEI","url":"https://www.aei.org/technology-and-innovation/reading-the-mind-of-the-machine-why-gpt-5s-chain-of-thought-monitoring-matters-for-ai-safety/"},{"title":"(PDF) Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety","url":"https://www.researchgate.net/publication/393724531_Chain_of_Thought_Monitorability_A_New_and_Fragile_Opportunity_for_AI_Safety"},{"title":"😸 OpenAI's new research paper on monitorability is wild","url":"https://www.theneurondaily.com/p/openai-s-new-research-paper-is-wild"},{"title":"Chain of thought monitoring | Shallow Review 2025","url":"https://shallowreview.ai/Black_box_safety/Chain_of_thought_monitoring"},{"title":"Chain of Thought Monitorability: A New and Fragile ...","url":"https://www.lesswrong.com/posts/7xneDbsgj6yJDJMjK/chain-of-thought-monitorability-a-new-and-fragile"},{"title":"Chain-of-Thought Monitorability","url":"https://www.emergentmind.com/topics/cot-monitorability"},{"title":"Reading GPT’s Mind — Analysis of Chain-of-Thought Monitorability as a Contingent and Fragile Opportunity for Mitigating Risks in Advanced AI Systems. | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/reading-gpts-mind-analysis-of-chain-of-thought-monitorability-as-a-contingent-and-fragile-aaa503ba21c5"},{"title":"Evaluating chain-of-thought monitorability | OpenAI","url":"https://openai.com/index/evaluating-chain-of-thought-monitorability/"}]

Based on the search results, here's what I foun
…[truncated 1592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8147
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-17T11:32:51.041115+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"probing hidden states\" \"self-verification\" reasoning model 2504.05419"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"probing hidden states\" \"self-verification\" reasoning model 2504.05419"
  }
}
```

</details>

---


### Tool call

_source line 173 · 2026-05-17T11:32:51.393424+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CRAFT reasoning-based safety alignment large reasoning model 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CRAFT reasoning-based safety alignment large reasoning model 2026 arXiv"
  }
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-17T11:32:51.444178+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"hidden risks\" \"large reasoning models\" safety assessment R1 2502.12659"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"hidden risks\" \"large reasoning models\" safety assessment R1 2502.12659"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-17T11:32:55.910245+00:00_

Web search results for query: ""probing hidden states" "self-verification" reasoning model 2504.05419"

Links: [{"title":"[2504.05419] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/abs/2504.05419"},{"title":"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification | alphaXiv","url":"https://www.alphaxiv.org/resources/2504.05419"},{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/html/2504.05419v1"},{"title":"dblp: Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification.","url":"https://dblp.org/rec/journals/corr/abs-2504-05419.html"},{"title":"(PDF) Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://www.researchgate.net/publication/390601804_Reasoning_Models_Know_When_They're_Right_Probing_Hidden_States_for_Self-Verification"},{"title":"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2504.05419"},{"title":"GitHub - AngelaZZZ-611/reasoning_models_probing · GitHub","url":"https://github.com/AngelaZZZ-611/reasoning_models_probing"},{"title":"[2504.05419v1] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/abs/2504.05419v1"},{"title":"The Geometry of Self-Verification in a Task-Specific Reasoning Model","url":"https://arxiv.org/html/2504.14379v1"},{"title":"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"http://paperreading.club/page?id=298036"}]

## Search Results for "probing hidden states" "self-verification" reasoning model 2504.05419

I found the paper you're searching for. Here's what I discovered:

**Paper Title:** "Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification"

**Key Research Focus:
…[truncated 1204 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4869
}
```

</details>

---


### Tool result

_source line 176 · 2026-05-17T11:32:56.562825+00:00_

Web search results for query: ""hidden risks" "large reasoning models" safety assessment R1 2502.12659"

Links: [{"title":"[2502.12659] The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1","url":"https://arxiv.org/abs/2502.12659"},{"title":"Paper page - The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1","url":"https://huggingface.co/papers/2502.12659"},{"title":"The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1","url":"https://arxiv.org/html/2502.12659v1"},{"title":"The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1 | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.12659"},{"title":"[2502.12659v1] The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1","url":"https://arxiv.org/abs/2502.12659v1"},{"title":"[Literature Review] The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1","url":"https://www.themoonlight.io/en/review/the-hidden-risks-of-large-reasoning-models-a-safety-assessment-of-r1"},{"title":"[PDF] The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1 | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Hidden-Risks-of-Large-Reasoning-Models:-A-of-R1-Zhou-Liu/a26a44d8999faf96364718084459e188869dc177"},{"title":"[2502.12659v3] The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1","url":"https://arxiv.org/abs/2502.12659v3"},{"title":"[2502.12659v4] The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1","url":"https://arxiv.org/abs/2502.12659v4"},{"title":"The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1","url":"https://powerdrill.ai/discover/summary-the-hidden-risks-of-large-reasoning-models-a-cm7ceg4wwk22a07t70eyeg46w"}]

I found the research paper you were looking for. Here's what the search revealed:

The paper "The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1" was submitted on February 18, 2025, and examines large reasoning models (LRM
…[truncated 857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5118
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-17T11:33:00.477525+00:00_

Web search results for query: "CRAFT reasoning-based safety alignment large reasoning model 2026 arXiv"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2603.17305v1"},{"title":"[2603.17305] Contrastive Reasoning Alignment: Reinforcement Learning from Hidden Representations","url":"https://arxiv.org/abs/2603.17305"},{"title":"[2604.18946] Reasoning Structure Matters for Safety Alignment of Reasoning Models","url":"https://arxiv.org/abs/2604.18946"},{"title":"[2603.17368] Towards Safer Large Reasoning Models by Promoting Safety Decision-Making before Chain-of-Thought Generation","url":"https://arxiv.org/abs/2603.17368"},{"title":"Safety in Large Reasoning Models: A Survey","url":"https://arxiv.org/html/2504.17704v1"},{"title":"Reasoning-Based Safety Alignment","url":"https://www.emergentmind.com/topics/reasoning-based-safety-alignment"},{"title":"[2602.11096] Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away","url":"https://arxiv.org/abs/2602.11096"},{"title":"[2503.00555] Safety Tax: Safety Alignment Makes Your Large Reasoning Models Less Reasonable","url":"https://arxiv.org/abs/2503.00555"},{"title":"What Matters For Safety Alignment?","url":"https://arxiv.org/html/2601.03868"},{"title":"Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model","url":"https://arxiv.org/html/2505.06538v1"}]

Based on the search results, I found detailed information about CRAFT:

## CRAFT: Contrastive Reasoning Alignment for Safety in Large Reasoning Models

CRAFT is a red-teaming alignment framework that leverages model reasoning capabilities and hidden representations to improve robustness against jailbreak attacks. Unlike prior defenses that operate primarily at the output level, CRAFT aligns large reasoning models to generate safety-aware reasoning traces by explicitly optimizing objectives defined over the hidden state space.

### Methodology

CRAFT integrates contrastive representation lear
…[truncated 1177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9084
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-17T11:33:04.794112+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"reasoning structure matters\" safety alignment reasoning models 2604.18946"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"reasoning structure matters\" safety alignment reasoning models 2604.18946"
  }
}
```

</details>

---


### Tool call

_source line 179 · 2026-05-17T11:33:05.246202+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"safety decision-making before chain-of-thought\" 2603.17368"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"safety decision-making before chain-of-thought\" 2603.17368"
  }
}
```

</details>

---


### Tool result

_source line 180 · 2026-05-17T11:33:10.616499+00:00_

Web search results for query: ""reasoning structure matters" safety alignment reasoning models 2604.18946"

Links: [{"title":"[2604.18946] Reasoning Structure Matters for Safety Alignment of Reasoning Models","url":"https://arxiv.org/abs/2604.18946"},{"title":"Reasoning Structure Matters for Safety Alignment of Reasoning Models","url":"https://arxiv.org/pdf/2604.18946"},{"title":"Deliberative Alignment is Deep, but Uncertainty Remains: Inference time safety improvement in reasoning via attribution of unsafe behavior to base model","url":"https://arxiv.org/html/2604.09665v2"},{"title":"How Sensitive Are Safety Benchmarks to Judge Configuration Choices?This arXiv posting is the author’s original, pre-peer-review manuscript. The paper has been accepted at the 22nd International Conference on Intelligent Computing (ICIC 2026), Toronto, Canada, July 22–26, 2026, and a revised version will appear in Springer Communications in Computer and Information Science (CCIS). The final published version may differ from this preprint in aspects including but not limited to formatting, wording, figure","url":"https://arxiv.org/html/2604.24074v1"},{"title":"ThinkSafe: Self-Generated Safety Alignment for Reasoning Models","url":"https://arxiv.org/html/2601.23143"},{"title":"Safety Alignment Shouldn't Be Complicated | OpenReview","url":"https://openreview.net/forum?id=9H91juqfgb"},{"title":"[2503.00555] Safety Tax: Safety Alignment Makes Your Large Reasoning Models Less Reasonable","url":"https://arxiv.org/abs/2503.00555"},{"title":"STAR-1: Safer Alignment of Reasoning LLMs with 1K Data","url":"https://ucsc-vlaa.github.io/STAR-1/"},{"title":"Reasoning-Based Safety Alignment","url":"https://www.emergentmind.com/topics/reasoning-based-safety-alignment"},{"title":"Safety in Large Reasoning Models: A Survey","url":"https://aclanthology.org/2025.findings-emnlp.185.pdf"}]

Based on the search results, I found the paper you're looking for:

## "Reasoning Structure Matters for Safety Alignment 
…[truncated 1224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5822
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-17T11:33:10.968335+00:00_

Web search results for query: ""safety decision-making before chain-of-thought" 2603.17368"

Links: [{"title":"[2603.17368] Towards Safer Large Reasoning Models by Promoting Safety Decision-Making before Chain-of-Thought Generation","url":"https://arxiv.org/abs/2603.17368"},{"title":"Towards Safer Large Reasoning Models by Promoting Safety Decision-Making before Chain-of-Thought Generation","url":"https://arxiv.org/html/2603.17368"},{"title":"SAFECHAIN: Safety of Language Models with Long Chain- ...","url":"https://aclanthology.org/2025.findings-acl.1197.pdf"},{"title":"Reading GPT’s Mind — Analysis of Chain-of-Thought Monitorability as a Contingent and Fragile Opportunity for Mitigating Risks in Advanced AI Systems. | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/reading-gpts-mind-analysis-of-chain-of-thought-monitorability-as-a-contingent-and-fragile-aaa503ba21c5"},{"title":"What is chain-of-thought monitoring?","url":"https://aisafety.info/questions/NM36/What-is-chain-of-thought-monitoring"},{"title":"Chain-of-Thought Injection as an Inference-Time Safety Intervention | OpenReview","url":"https://openreview.net/forum?id=v0XkjgeD6U"},{"title":"Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention","url":"https://arxiv.org/html/2509.24393v1"},{"title":"Train your brain: For safer decisions, pause and think","url":"https://www.saif.com/safety-and-health/train-your-brain-for-safer-decisions-pause-and-think.html"},{"title":"A Potential Strategy for AI Safety — Chain of Thought Monitorability — EA Forum","url":"https://forum.effectivealtruism.org/posts/HvF94NoWTTCWiezk8/a-potential-strategy-for-ai-safety-chain-of-thought"},{"title":"AI-agentic Deliberation for Policy-embedded CoT Data ...","url":"https://aclanthology.org/2025.findings-acl.1166.pdf"}]

I found the paper! Here's what the search reveals:

Large reasoning models (LRMs) achieved remarkable performance via chain-of-thought (CoT), but recent studies showed that 
…[truncated 1030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5722
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-17T11:33:16.590812+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-17T11:35:24.403750+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 34, \"total_citations\": 57, \"unique_cited_keys\": 34, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 26, \"online_not_found\": 8, \"online_mismatch\": 0}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"trajguard\", \"type\": \"article\", \"title\": \"TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense\", \"authors\": \"Liu, Cheng and Liu, Xiaolei and Li, Xingyu and Xin, Bangzhou and Ding, Kangyi\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.07727\"}, {\"key\": \"safeswitch\", \"type\": \"inproceedings\", \"title\": \"SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals\", \"authors\": \"Han, Peixuan and Qian, Cheng and Chen, Xiusi and Zhang, Yuji and Ji, Heng and Zh...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2025\"}, {\"key\": \"siren\", \"type\": \"inproceedings\", \"title\": \"LLM Safety From Within: Detecting Harmful Content with Internal Representations\", \"authors\": \"Jiao, Difan and Liu, Yilun and Yuan, Ye and Tang, Zhenwei and Du, Linfeng and Wu...\", \"year\": \"2026\", \"venue\": \"Proceedings of the 64th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"saferemind\", \"type\": \"article\", \"title\": \"How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs\", \"authors\": \"Kim, Su-Hyeon and Jin, Hyundong and Lee, Yejin and Han, Yo-Sub\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2601.03662\"}, {\"key\": \"safethink\", \"type\": \"article\", \"title\": \"Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away\", \"authors\": \"Ghosal, Soumya Suvra and Chakraborty, Souradip and Singh, Vaibhav and Huang, Fur...\", \"year\": \"202
…[truncated 26703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 127812
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-17T11:38:18.303125+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 1 Review — Reviewer 2 (新颖性 + 完整性 + 写作质量)\n\n---\n\n## Summary\n\n本文对 reasoning model 中 safety commitment point 检测进行了系统性 empirical 比较，覆盖 4 个模型、2 种模态（hidden states vs. text）、多种 temporal aggregation 策略。核心发现是 temporal context 的增益大于 modality 选择，且 HS 优势随 scale 消失（7-8B 显著，32B 不显著）。论文提供了全面的负面结果（BOCPD、Mahalanobis、cross-model transfer 均失败）。然而，主要贡献的新颖性不足——\"更多时序上下文提升分类器性能\" 是预期内的结果，且论文将其 framing 为 \"counterintuitive\" 存在 overclaim。作为纯 empirical study，缺乏新方法提出，在 EMNLP main track 竞争力存疑。\n\n---\n\n## Strengths\n\n[S1] **实验设计严谨**：控制变量清晰（同任务、同数据、同评估协议），Holm-Bonferroni 多重比较校正恰当，control task validation 确认 probe 捕获真正的 safety structure（Section 5.5, Table 5）。统计方法论在这个领域的论文中属于上乘。\n\n[S2] **负面结果有价值**：系统性证明 TrajGuard Mahalanobis distance（Table 6）、BOCPD/CUSUM（Appendix E）、cross-model transfer（Section 5.6）均失败，并给出合理解释（commitment 是渐进过程而非 abrupt change）。这些结果对后续研究有指导意义。\n\n[S3] **透明度高**：Appendix F 的 bug disclosure 值得称赞——主动披露 QwQ-32B text probe 的初始化 bug 及其对中间结果的影响，所有报告数字均为修正后结果。这在学术论文中罕见且正面。\n\n[S4] **覆盖两个 scale、两种架构、两种训练方法**：OT-7B（Qwen + STILL）和 R1-8B（Llama + R1 distillation）的交叉验证在一定程度上解耦了 architecture/training/scale confound。\n\n[S5] **Limitations section 全面诚实**：明确承认高 FPR（39-62%）、小样本 32B、text encoder 偏差、缺少 inter-annotator agreement 等，未试图掩盖弱点。\n\n---\n\n## Weaknesses\n\n[W1] [severity: critical] **核心贡献新颖性不足——\"temporal context dominates modality\" 是预期内结果**\n- 具体位置：Section 5.1, Introduction Contribution 1\n- 问题：Temporal windowing 本质是将特征从 $d$ 扩展到 $W \\times d$，为分类器提供更多信息。这与 \"more features = better performance\" 无本质区别。论文在 Introduction 第 9 行声称 \"Our central finding is counterintuitive\"，但给定一个 binary classification 任务，扩大输入特征窗口提升 precision 是标准 ML 预期。\n- 更关键的是：在 7-8B 模型上，modality gap 达 +22.4pp precision（Table 3），而 temporal improvement 最大为 +12.9pp（Section 5.1）。因此 **在 7-8B scale 上 modality 才是更大的因素**。\"Temporal dominates modality\" 这个 framing 只在跨 scale 平均后成立，是一个 cherry-picked narrative。\n- 为什么影响接收：作为论文的核心 contribution，如果其 \"counterintuitive\" 属性不成立，paper 的主要 novelty 支撑就大幅削弱。\n- 建议：(1) 去掉 \"counterintuitive\" 的 framing；(2) 重新定位为 \"temporal context is a universal, low-cost improvement regardless of modality\"——这是一个 useful practical finding 但不构成 surprising insight。\n\n[W2] [severity: critical] **纯 empirical study 无新方法，main track 竞争力不足**\n- 具体位置：全文\n- 问题：所有使用的方法都是现有的：logistic regression probing、GRU sequence model、temporal concatenation、BOCPD、CUSUM、Mahalanobis distance。论文未提出任何新的检测方法、新的 objective、或新的理论框架。HarmThoughts 数据集也非本文贡献。\n- 对比：TrajGuard 提出了 streaming Mahalanobis detection；SafeSwitch 提出了 internal activation-based steering；SIREN 提出了 representation-based detection pipeline。本文仅是对已有方法的 comparative evaluation。\n- 为什么影响接收：EMNLP main track 通常期待 methodological novelty 或 transformative insight。纯 benchmark/comparison paper 更适合 Findings track。\n- 建议：如果目标是 main track，需要补充一个 novel component——例如利用 temporal finding 设计一个新的 adaptive detection 算法并在 deployment-realistic setting 下验证。Appendix G 的 two-stage detection 是一个方向，但 +1.3pp 的 marginal gain 太弱。\n\n[W3] [severity: critical] **Contribution 1 与实验证据不完全一致（overclaim）**\n- 具体位置：Introduction Contribution 1; Section 6 paragraph 1\n- 问题：Contribution 1 宣称 \"The bottleneck in commitment detection is temporal, not informational\"。但：\n  - R1-8B：modality gap = +22.4pp precision；temporal gain (W=1→25) = +12.9pp\n  - OT-7B：modality gap = +21.2pp precision；temporal gain (W=1→25) = +6.1pp\n  - 在这两个模型上，**modality gap > temporal gain**\n  - 只有在 32B 模型上，modality gap 消失（+5.7-9.4pp, n.s.），temporal gain 才成为 primary factor\n- Contribution 1 的措辞暗示这是 universal finding，但实际只在 32B scale 成立。\n- 建议：修改为 \"Temporal context provides universal gains across all conditions, but modality remains the dominant factor at 7-8B scale\"。\n\n[W4] [severity: warning] **Related Work 遗漏多篇 2025-2026 高相关工作**\n- 具体位置：Section 2\n- 遗漏的重要论文：\n  1. **Zhang et al. (2025), \"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification\"** (arXiv:2504.05419)——同样对 reasoning model hidden states 做 probing，检测 correctness，甚至分段 CoT 做分类。方法论高度重叠，必须讨论。\n  2. **Luo et al. (2026), \"Contrastive Reasoning Alignment: Reinforcement Learning from Hidden Representations\"** (arXiv:2603.17305, CRAFT)——在 hidden state space 做 contrastive learning 分离 safe/unsafe reasoning trajectories，与本文的 \"contrastive trace\" 概念直接相关。\n  3. **Zhou et al. (2025), \"The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1\"** (arXiv:2502.12659)——R1 安全性评估，作为背景必引。\n  4. **arXiv:2604.18946, \"Reasoning Structure Matters for Safety Alignment of Reasoning Models\"**——讨论 reasoning structure 与 safety 的关系。\n  5. **arXiv:2603.17368, \"Towards Safer Large Reasoning Models by Promoting Safety Decision-Making before Chain-of-Thought Generation\"**——在 CoT 生成前做 safety decision，与 commitment point 概念相关。\n- 32 篇引用对于 EMNLP Long Paper 偏少（目标量级 ~40-60 篇），特别是 2025-2026 年的 reasoning model safety 文献覆盖不足。\n- 建议：补充以上论文并明确 positioning（特别是与 Zhang et al. 2025 的方法论区别）。\n\n[W5] [severity: warning] **Abstract 数据堆砌，叙事性弱**\n- 具体位置：sections/abstract.tex\n- 问题：191 words 的 Abstract 包含了 12 个数字/统计量（12.9pp, +22.4pp, $p<0.001$, 5/12 tests, 7.5-18.3pp 等），读起来像 Results 的压缩版而非 compelling story。审稿人 30 秒内难以从中提取核心价值——哪些数字是 essential 的？为什么这些发现对 community 重要？\n- \"Our results reveal that temporal context dominates modality choice\" 这句是叙事核心，但被前后的数字淹没了。\n- 建议：保留 2-3 个最关键数字（如 temporal gain range 和 modality gap 的 scale-dependent pattern），其余移至正文。强化 \"why this matters\" 的叙事（e.g., 对 deployment safety monitoring 的设计启示）。\n\n[W6] [severity: warning] **Text encoder confound 削弱 modality comparison 的可信度**\n- 具体位置：Limitations Section（acknowledged），但 Section 5.2 的 claim 未充分 qualify\n- 问题：HS features 为 3584-5120 维，text features 为 384 维（MiniLM）。当 temporal window W=15 时，HS 输入为 15×4096=61440 维 vs text 15×384=5760 维——维度差距达 10:1。Logistic regression 在高维空间有 inherent advantage。论文在 Limitations 中承认这一点，但 Section 5.2 的 conclusions 和 Contribution 2 (\"HS advantage is scale-dependent\") 未加 qualifier。\n- 特别是：OT-7B 使用 W=3 matched comparison（Bootstrap CI 报告），但 R1-8B 使用 W=15 的 unmatched window（Table 3 caption），两种 modality 的 window size 不同。\n- 建议：在 Section 5.2 显著位置加入 caveat；使用更强的 text encoder（如 E5-large 1024-d）的 ablation 可以大幅增强结论的可信度。\n\n[W7] [severity: warning] **32B 结论基于极小样本（n=19-20），统计效力存疑**\n- 具体位置：Table 3 (QwQ-32B n=19, R1-32B n=20); Section 5.2\n- 问题：R1-32B 的 effect size (+9.4pp precision, p=0.050) 与 7-8B 模型的 effect size (+22.4pp) 在同一方向上。给定 n=20 的 power 极低（post-hoc power analysis 对 d≈0.5 的 paired test 约为 30-40%），non-significance 可能仅反映 power 不足而非真正的 null effect。论文在 Section 5.2 最后一段承认 \"This is not a statistical power artifact\" 并引用 effect size 差异作为证据，但 R1-32B 的 effect size (+9.4pp) 并不 trivially small。\n- \"Scale-dependent\" 结论基于 2 models per scale，其中 32B 的 2 个模型给出不一致的 evidence（R1-32B directional, QwQ-32B null）。\n- 建议：在结论中明确标注 \"provisional pending larger 32B evaluation\"；或收集更多 R1-32B traces 以达到 n≥50。\n\n[W8] [severity: warning] **Discussion + Conclusion 合并后仍有大量重复**\n- 具体位置：Section 6\n- 问题：Section 6 的 5 个 paragraphs 与 Introduction Contribution list、Section 5.2 final paragraph、Abstract 高度重复。\"Temporal context dominates...\" 这个 finding 在全文中重复出现至少 7 次（Abstract, Intro para 3, Contribution 1, Section 5.1 last para, Section 6 para 1, Section 6 \"Design implications\", Section 6 \"Conclusion\"）。这不是强调，是冗余。\n- 建议：Conclusion paragraph 应聚焦 implications 和 future work，避免重述已在 experiments section 详细展开的数字。\n\n[W9] [severity: info] **AI 写作痕迹**\n- 具体位置：多处\n- 问题：\n  - En-dash 用作解释性连接：\"Safety Commitment Point (CP), the first step after which...\" 不过未发现 em-dash (—)\n  - \"-ing phrase\" 结尾出现多次：Introduction line 3 \"producing extended internal deliberation before generating final responses\"；Related Work \"trading causal guarantees for practical applicability\"\n  - Section 5.2: \"ruling out architecture- or training-specific confounds\" — 这种长分词短语结构\n  - Introduction 段落过度分段（5 段 contribution 展开但每段之间逻辑衔接自然，这一点尚可）\n- 程度：不严重，整体写作质量在中上水平，但可进一步打磨。\n\n---\n\n## Questions\n\n[Q1] Contribution 1 claims \"temporal, not informational\" bottleneck. But at 7-8B, the modality gap (+22pp) exceeds the temporal gain (+12.9pp). How do you reconcile this? Under what interpretation does \"temporal dominates\" hold at 7-8B?\n\n[Q2] Why was MiniLM-L6-v2 (384-d) chosen as the text encoder instead of a stronger encoder (e.g., E5-large at 1024-d, or even Llama-based embeddings at 4096-d)? The 10:1 dimensionality gap at matched window sizes is a serious confound for the modality comparison.\n\n[Q3] The Commitment Point definition depends on \"no subsequent step contains safety reasoning.\" How robust is this to traces where safety reasoning briefly resurfaces late (oscillation)? What fraction of traces exhibit such oscillation patterns?\n\n[Q4] Section 5.5 reports QwQ-32B best layer at 3.1% depth (layer 2). This seems anomalously shallow—effectively just positional encoding plus minimal transformation. Does this suggest the probe for QwQ-32B is fundamentally different from what's happening at R1-8B (layer 14, 44% depth)? If so, can we meaningfully compare \"modality effects\" across these models?\n\n[Q5] The oracle gap is 85.5% (Section 5.7). Given this enormous gap, do you think the current probing approach has a realistic path to deployment, or is this primarily a diagnostic/characterization tool? The Conclusion's \"design implications\" paragraph seems to conflate these two use cases.\n\n---\n\n## Missing References\n\n1. Zhang et al. (2025), \"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification\" (arXiv:2504.05419) — **critical omission**, directly probes reasoning model hidden states for step-level properties\n2. Luo et al. (2026), \"Contrastive Reasoning Alignment: Reinforcement Learning from Hidden Representations\" (arXiv:2603.17305) — contrastive hidden-state learning for safety in reasoning models\n3. Zhou et al. (2025), \"The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1\" (arXiv:2502.12659) — R1 safety assessment\n4. arXiv:2604.18946, \"Reasoning Structure Matters for Safety Alignment of Reasoning Models\" — reasoning structure and safety\n5. arXiv:2603.17368, \"Towards Safer Large Reasoning Models by Promoting Safety Decision-Making before Chain-of-Thought Generation\" — pre-CoT safety decision-making\n\n---\n\n## Format Compliance\n\n- ✅ `\\usepackage[review]{acl}` 正确\n- ✅ 匿名化：`\\author{Anonymous ARR Submission}`\n- ✅ Limitations section 存在且内容充实\n- ✅ Responsible NLP Research Checklist 存在（Appendix A）\n- ✅ 引用格式一致（natbib, cite/citep/citet）\n- ✅ 所有 bib 条目无 orphan/missing（验证通过）\n- ⚠️ 页数需确认——正文内容量看似在 8 页限制边缘\n- ⚠️ Table 3 QwQ-32B 的 text FPR (17.8%) < HS FPR (20.8%)，但未加粗 text 的 best——加粗规则不一致\n\n---\n\n## Bug Disclosure Assessment (Appendix F)\n\n- 披露充分：清楚说明了 bug 的性质（midpoint heuristic placeholder）、发现过程、修正方法\n- 影响评估可信：声称所有 reported numbers 使用修正后 pipeline，且 bug 仅影响 QwQ-32B text baseline\n- 唯一不足：未报告 bug 存在了多长时间、影响了哪些中间 design decisions（例如，是否在 bug 存在期间做出了 \"HS better than text on QwQ-32B\" 的结论并据此 framing 了全文？）\n\n---\n\n## Overall Assessment\n\n**Soundness: 3.5/5** — 实验设计严谨、统计方法恰当、limitations 诚实；但 text encoder confound 未充分处理，32B 样本量不足以支撑 strong claim\n\n**Excitement: 2.5/5** — 问题本身重要且 timely，但核心发现（temporal context helps, HS better at small scale）缺乏 surprise value；纯 empirical 无新方法\n\n**Overall Recommendation: 2.5 (Leaning Reject)**\n\n**Confidence: 4/5** — 对 probing methods、safety detection literature、和统计方法论均较为熟悉\n\n**一句话总结**：实验执行质量高、透明度佳，但核心 contribution 的新颖性不足以支撑 main track——\"temporal context helps\" 是 expected result, overclaim 为 \"counterintuitive\" 削弱了可信度。建议：(1) 重新定位 narrative（acknowledge temporal gain is expected, focus on the scale-dependent modality finding as primary contribution），(2) 补充 missing references 和 stronger text encoder ablation，(3) 考虑投 Findings track。",
  "reviewer_id": "2",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 1 Review — Reviewer 2 (新颖性 + 完整性 + 写作质量)\n\n---\n\n## Summary\n\n本文对 reasoning model 中 safety commitment point 检测进行了系统性 empirical 比较，覆盖 4 个模型、2 种模态（hidden states vs. text）、多种 temporal aggregation 策略。核心发现是 temporal context 的增益大于 modality 选择，且 HS 优势随 scale 消失（7-8B 显著，32B 不显著）。论文提供了全面的负面结果（BOCPD、Mahalanobis、cross-model transfer 均失败）。然而，主要贡献的新颖性不足——\"更多时序上下文提升分类器性能\" 是预期内的结果，且论文将其 framing 为 \"counterintuitive\" 存在 overclaim。作为纯 empirical study，缺乏新方法提出，在 EMNLP main track 竞争力存疑。\n\n---\n\n## Strengths\n\n[S1] **实验设计严谨**：控制变量清晰（同任务、同数据、同评估协议），Holm-Bonferroni 多重比较校正恰当，control task validation 确认 probe 捕获真正的 safety structure（Section 5.5, Table 5）。统计方法论在这个领域的论文中属于上乘。\n\n[S2] **负面结果有价值**：系统性证明 TrajGuard Mahalanobis distance（Table 6）、BOCPD/CUSUM（Appendix E）、cross-model transfer（Section 5.6）均失败，并给出合理解释（commitment 是渐进过程而非 abrupt change）。这些结果对后续研究有指导意义。\n\n[S3] **透明度高**：Appendix F 的 bug disclosure 值得称赞——主动披露 QwQ-32B text probe 的初始化 bug 及其对中间结果的影响，所有报告数字均为修正后结果。这在学术论文中罕见且正面。\n\n[S4] **覆盖两个 scale、两种架构、两种训练方法**：OT-7B（Qwen + STILL）和 R1-8B（Llama + R1 distillation）的交叉验证在一定程度上解耦了 architecture/training/scale confound。\n\n[S5] **Limitations section 全面诚实**：明确承认高 FPR（39-62%）、小样本 32B、text encoder 偏差、缺少 inter-annotator agreement 等，未试图掩盖弱点。\n\n---\n\n## Weaknesses\n\n[W1] [severity: critical] **核心贡献新颖性不足——\"temporal context dominates modality\" 是预期内结果**\n- 具体位置：Section 5.1, Introduction Contribution 1\n- 问题：Temporal windowing 本质是将特征从 $d$ 扩展到 $W \\times d$，为分类器提供更多信息。这与 \"more features = better performance\" 无本质区别。论文在 Introduction 第 9 行声称 \"Our central finding is counterintuitive\"，但给定一个 binary classification 任务，扩大输入特征窗口提升 precision 是标准 ML 预期。\n- 更关键的是：在 7-8B 模型上，modality gap 达 +22.4pp precision（Table 3），而 temporal improvement 最大为 +12.9pp（Section 5.1）。因此 **在 7-8B scale 上 modality 才是更大的因素**。\"Temporal dominates modality\" 这个 framing 只在跨 scale 平均后成立，是一个 cherry-picked narrative。\n- 为什么影响接收：作为论文的核心 contribution，如果其 \"counterintuitive\" 属性不成立，paper 的主要 novelty 支撑就大幅削弱。\n- 建议：(1) 去掉 \"counterintuitive\" 的 framing；(2) 重新定位为 \"temporal context is a universal, low-cost improvement regardless of modality\"——这是一个 useful practical finding 但不构成 surprising insight。\n\n[W2] [severity: critical] **纯 empirical study 无新方法，main track 竞争力不足**\n- 具体位置：全文\n- 问题：所有使用的方法都是现有的：logistic regression probing、GRU sequence model、temporal concatenation、BOCPD、CUSUM、Mahalanobis distance。论文未提出任何新的检测方法、新的 objective、或新的理论框架。HarmThoughts 数据集也非本文贡献。\n- 对比：TrajGuard 提出了 streaming Mahalanobis detection；SafeSwitch 提出了 internal activation-based steering；SIREN 提出了 representation-based detection pipeline。本文仅是对已有方法的 comparative evaluation。\n- 为什么影响接收：EMNLP main track 通常期待 methodological novelty 或 transformative insight。纯 benchmark/comparison paper 更适合 Findings track。\n- 建议：如果目标是 main track，需要补充一个 novel component——例如利用 temporal finding 设计一个新的 adaptive detection 算法并在 deployment-realistic setting 下验证。Appendix G 的 two-stage detection 是一个方向，但 +1.3pp 的 marginal gain 太弱。\n\n[W3] [severity: critical] **Contribution 1 与实验证据不完全一致（overclaim）**\n- 具体位置：Introduction Contribution 1; Section 6 paragraph 1\n- 问题：Contribution 1 宣称 \"The bottleneck in commitment detection is temporal, not informational\"。但：\n  - R1-8B：modality gap = +22.4pp precision；temporal gain (W=1→25) = +12.9pp\n  - OT-7B：modality gap = +21.2pp precision；temporal gain (W=1→25) = +6.1pp\n  - 在这两个模型上，**modality gap > temporal gain**\n  - 只有在 32B 模型上，modality gap 消失（+5.7-9.4pp, n.s.），temporal gain 才成为 primary factor\n- Contribution 1 的措辞暗示这是 universal finding，但实际只在 32B scale 成立。\n- 建议：修改为 \"Temporal context provides universal gains across all conditions, but modality remains the dominant factor at 7-8B scale\"。\n\n[W4] [severity: warning] **Related Work 遗漏多篇 2025-2026 高相关工作**\n- 具体位置：Section 2\n- 遗漏的重要论文：\n  1. **Zhang et al. (2025), \"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification\"** (arXiv:2504.05419)——同样对 reasoning model hidden states 做 probing，检测 correctness，甚至分段 CoT 做分类。方法论高度重叠，必须讨论。\n  2. **Luo et al. (2026), \"Contrastive Reasoning Alignment: Reinforcement Learning from Hidden Representations\"** (arXiv:2603.17305, CRAFT)——在 hidden state space 做 contrastive learning 分离 safe/unsafe reasoning trajectories，与本文的 \"contrastive trace\" 概念直接相关。\n  3. **Zhou et al. (2025), \"The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1\"** (arXiv:2502.12659)——R1 安全性评估，作为背景必引。\n  4. **arXiv:2604.18946, \"Reasoning Structure Matters for Safety Alignment of Reasoning Models\"**——讨论 reasoning structure 与 safety 的关系。\n  5. **arXiv:2603.17368, \"Towards Safer Large Reasoning Models by Promoting Safety Decision-Making before Chain-of-Thought Generation\"**——在 CoT 生成前做 safety decision，与 commitment point 概念相关。\n- 32 篇引用对于 EMNLP Long Paper 偏少（目标量级 ~40-60 篇），特别是 2025-2026 年的 reasoning model safety 文献覆盖不足。\n- 建议：补充以上论文并明确 positioning（特别是与 Zhang et al. 2025 的方法论区别）。\n\n[W5] [severity: warning] **Abstract 数据堆砌，叙事性弱**\n- 具体位置：sections/abstract.tex\n- 问题：191 words 的 Abstract 包含了 12 个数字/统计量（12.9pp, +22.4pp, $p<0.001$, 5/12 tests, 7.5-18.3pp 等），读起来像 Results 的压缩版而非 compelling story。审稿人 30 秒内难以从中提取核心价值——哪些数字是 essential 的？为什么这些发现对 community 重要？\n- \"Our results reveal that temporal context dominates modality choice\" 这句是叙事核心，但被前后的数字淹没了。\n- 建议：保留 2-3 个最关键数字（如 temporal gain range 和 modality gap 的 scale-dependent pattern），其余移至正文。强化 \"why this matters\" 的叙事（e.g., 对 deployment safety monitoring 的设计启示）。\n\n[W6] [severity: warning] **Text encoder confound 削弱 modality comparison 的可信度**\n- 具体位置：Limitations Section（acknowledged），但 Section 5.2 的 claim 未充分 qualify\n- 问题：HS features 为 3584-5120 维，text features 为 384 维（MiniLM）。当 temporal window W=15 时，HS 输入为 15×4096=61440 维 vs text 15×384=5760 维——维度差距达 10:1。Logistic regression 在高维空间有 inherent advantage。论文在 Limitations 中承认这一点，但 Section 5.2 的 conclusions 和 Contribution 2 (\"HS advantage is scale-dependent\") 未加 qualifier。\n- 特别是：OT-7B 使用 W=3 matched comparison（Bootstrap CI 报告），但 R1-8B 使用 W=15 的 unmatched window（Table 3 caption），两种 modality 的 window size 不同。\n- 建议：在 Section 5.2 显著位置加入 caveat；使用更强的 text encoder（如 E5-large 1024-d）的 ablation 可以大幅增强结论的可信度。\n\n[W7] [severity: warning] **32B 结论基于极小样本（n=19-20），统计效力存疑**\n- 具体位置：Table 3 (QwQ-32B n=19, R1-32B n=20); Section 5.2\n- 问题：R1-32B 的 effect size (+9.4pp precision, p=0.050) 与 7-8B 模型的 effect size (+22.4pp) 在同一方向上。给定 n=20 的 power 极低（post-hoc power analysis 对 d≈0.5 的 paired test 约为 30-40%），non-significance 可能仅反映 power 不足而非真正的 null effect。论文在 Section 5.2 最后一段承认 \"This is not a statistical power artifact\" 并引用 effect size 差异作为证据，但 R1-32B 的 effect size (+9.4pp) 并不 trivially small。\n- \"Scale-dependent\" 结论基于 2 models per scale，其中 32B 的 2 个模型给出不一致的 evidence（R1-32B directional, QwQ-32B null）。\n- 建议：在结论中明确标注 \"provisional pending larger 32B evaluation\"；或收集更多 R1-32B traces 以达到 n≥50。\n\n[W8] [severity: warning] **Discussion + Conclusion 合并后仍有大量重复**\n- 具体位置：Section 6\n- 问题：Section 6 的 5 个 paragraphs 与 Introduction Contribution list、Section 5.2 final paragraph、Abstract 高度重复。\"Temporal context dominates...\" 这个 finding 在全文中重复出现至少 7 次（Abstract, Intro para 3, Contribution 1, Section 5.1 last para, Section 6 para 1, Section 6 \"Design implications\", Section 6 \"Conclusion\"）。这不是强调，是冗余。\n- 建议：Conclusion paragraph 应聚焦 implications 和 future work，避免重述已在 experiments section 详细展开的数字。\n\n[W9] [severity: info] **AI 写作痕迹**\n- 具体位置：多处\n- 问题：\n  - En-dash 用作解释性连接：\"Safety Commitment Point (CP), the first step after which...\" 不过未发现 em-dash (—)\n  - \"-ing phrase\" 结尾出现多次：Introduction line 3 \"producing extended internal deliberation before generating final responses\"；Related Work \"trading causal guarantees for practical applicability\"\n  - Section 5.2: \"ruling out architecture- or training-specific confounds\" — 这种长分词短语结构\n  - Introduction 段落过度分段（5 段 contribution 展开但每段之间逻辑衔接自然，这一点尚可）\n- 程度：不严重，整体写作质量在中上水平，但可进一步打磨。\n\n---\n\n## Questions\n\n[Q1] Contribution 1 claims \"temporal, not informational\" bottleneck. But at 7-8B, the modality gap (+22pp) exceeds the temporal gain (+12.9pp). How do you reconcile this? Under what interpretation does \"temporal dominates\" hold at 7-8B?\n\n[Q2] Why was MiniLM-L6-v2 (384-d) chosen as the text encoder instead of a stronger encoder (e.g., E5-large at 1024-d, or even Llama-based embeddings at 4096-d)? The 10:1 dimensionality gap at matched window sizes is a serious confound for the modality comparison.\n\n[Q3] The Commitment Point definition depends on \"no subsequent step contains safety reasoning.\" How robust is this to traces where safety reasoning briefly resurfaces late (oscillation)? What fraction of traces exhibit such oscillation patterns?\n\n[Q4] Section 5.5 reports QwQ-32B best layer at 3.1% depth (layer 2). This seems anomalously shallow—effectively just positional encoding plus minimal transformation. Does this suggest the probe for QwQ-32B is fundamentally different from what's happening at R1-8B (layer 14, 44% depth)? If so, can we meaningfully compare \"modality effects\" across these models?\n\n[Q5] The oracle gap is 85.5% (Section 5.7). Given this enormous gap, do you think the current probing approach has a realistic path to deployment, or is this primarily a diagnostic/characterization tool? The Conclusion's \"design implications\" paragraph seems to conflate these two use cases.\n\n---\n\n## Missing References\n\n1. Zhang et al. (2025), \"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification\" (arXiv:2504.05419) — **critical omission**, directly probes reasoning model hidden states for step-level properties\n2. Luo et al. (2026), \"Contrastive Reasoning Alignment: Reinforcement Learning from Hidden Representations\" (arXiv:2603.17305) — contrastive hidden-state learning for safety in reasoning models\n3. Zhou et al. (2025), \"The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1\" (arXiv:2502.12659) — R1 safety assessment\n4. arXiv:2604.18946, \"Reasoning Structure Matters for Safety Alignment of Reasoning Models\" — reasoning structure and safety\n5. arXiv:2603.17368, \"Towards Safer Large Reasoning Models by Promoting Safety Decision-Making before Chain-of-Thought Generation\" — pre-CoT safety decision-making\n\n---\n\n## Format Compliance\n\n- ✅ `\\usepackage[review]{acl}` 正确\n- ✅ 匿名化：`\\author{Anonymous ARR Submission}`\n- ✅ Limitations section 存在且内容充实\n- ✅ Responsible NLP Research Checklist 存在（Appendix A）\n- ✅ 引用格式一致（natbib, cite/citep/citet）\n- ✅ 所有 bib 条目无 orphan/missing（验证通过）\n- ⚠️ 页数需确认——正文内容量看似在 8 页限制边缘\n- ⚠️ Table 3 QwQ-32B 的 text FPR (17.8%) < HS FPR (20.8%)，但未加粗 text 的 best——加粗规则不一致\n\n---\n\n## Bug Disclosure Assessment (Appendix F)\n\n- 披露充分：清楚说明了 bug 的性质（midpoint heuristic placeholder）、发现过程、修正方法\n- 影响评估可信：声称所有 reported numbers 使用修正后 pipeline，且 bug 仅影响 QwQ-32B text baseline\n- 唯一不足：未报告 bug 存在了多长时间、影响了哪些中间 design decisions（例如，是否在 bug 存在期间做出了 \"HS better than text on QwQ-32B\" 的结论并据此 framing 了全文？）\n\n---\n\n## Overall Assessment\n\n**Soundness: 3.5/5** — 实验设计严谨、统计方法恰当、limitations 诚实；但 text encoder confound 未充分处理，32B 样本量不足以支撑 strong claim\n\n**Excitement: 2.5/5** — 问题本身重要且 timely，但核心发现（temporal context helps, HS better at small scale）缺乏 surprise value；纯 empirical 无新方法\n\n**Overall Recommendation: 2.5 (Leaning Reject)**\n\n**Confidence: 4/5** — 对 probing methods、safety detection literature、和统计方法论均较为熟悉\n\n**一句话总结**：实验执行质量高、透明度佳，但核心 contribution 的新颖性不足以支撑 main track——\"temporal context helps\" 是 expected result, overclaim 为 \"counterintuitive\" 削弱了可信度。建议：(1) 重新定位 narrative（acknowledge temporal gain is expected, focus on the scale-dependent modality finding as primary contribution），(2) 补充 missing references 和 stronger text encoder ablation，(3) 考虑投 Findings track。",
    "reviewer_id": "2",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-17T11:38:22.049086+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3745
}
```

</details>

---


### Assistant

_source line 186 · 2026-05-17T11:38:30.433747+00:00_

审稿完成，已提交给 Review Director。

核心判断：**Leaning Reject (2.5/5)**。

主要问题：
1. **新颖性不足**——"temporal context helps classification" 是标准 ML 预期，framing 为 "counterintuitive" 构成 overclaim
2. **纯 empirical study 无新方法**——所有技术组件均为现有方法的直接应用，更适合 Findings track
3. **Contribution 1 与证据不一致**——在 7-8B 上 modality gap (+22pp) > temporal gain (+12.9pp)，"temporal dominates" 仅在 32B 成立
4. **Related Work 遗漏**——至少 5 篇 2025-2026 高相关论文未引用（特别是 Zhang et al. 2025 的 hidden-state probing for reasoning models）

论文的实验执行质量、统计严谨性和透明度值得肯定，但 contribution framing 需要大幅调整。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2"
}
```

</details>

---


## Round 6

## Round 6

4 recorded events


### User

_source line 187 · 2026-05-17T11:41:19.332467+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

### Reviewer 1 Summary
本文首次系统评估了推理模型中安全承诺检测的两种信号模态，覆盖四个模型、两种架构、两种训练方法和两种规模。核心发现：temporal context 的贡献大于信号模态选择；HS 优势在 7-8B 显著，在 32B 消失。负面结果定义了当前方法的边界。研究问题有价值且实验设计总体合理，但存在若干影响核心 claim 可信度的方法论问题。

### Reviewer 1 Strengths
[S1] 研究问题定义清晰且有实际意义。
[S2] 实验设计体现了良好的控制变量思想。四个模型覆盖 2 架构 × 2 规模 × 2 训练方法，OT-7B 的引入有价值。
[S3] 统计方法学总体审慎。Holm-Bonferroni、metric 间相关性说明、effect size 报告。
[S4] 负面结果的系统报告值得赞赏。Bug disclosure 体现科学透明度。
[S5] Control task 验证方法论规范。
[S6] Temporal context dominance 的发现具有实际应用价值——practitioner-friendly takeaway。

### Reviewer 1 Weaknesses (Must-Fix)

**[W1] [critical] Negative results 仅在 R1-8B 上验证，但结论泛化到所有模型**
- BOCPD、CUSUM 全参数 sweep 和 Mahalanobis distance 仅在 R1-8B 上执行
- 论文将结论泛化为 "safety commitment is gradual rather than abrupt"（Section 5 第 3 段），作为三大贡献之一仅有单模型证据
- 不同架构和规模的 transition dynamics 可能不同（QwQ-32B layer 2 vs R1-8B layer 14 的巨大差异就是证据）
- 建议至少在一个 32B 模型和 OT-7B 上运行 BOCPD/Mahalanobis，或严格限定 claim

**[W2] [critical] Layer selection metric（accuracy × crossing rate）缺乏论证**
- 未解释为什么选择乘法（而非加法、加权和、带约束优化）
- 导致 QwQ-32B 选择 layer 2 (3.1% depth)——论文自己承认 "encodes primarily positional features"
- OT-7B Table 6: layer 0 score (35.5) > layer 16 (21.8)，但实际选了 layer 16——矛盾
- 如果换标准，QwQ-32B 可能选不同层，scale-dependent claim 可能改变
- 建议：(1) layer selection metric 消融；(2) 解释 OT-7B 矛盾；(3) 报告 QwQ-32B alternative layer 下的结果

**[W3] [critical] GRU 评估使用不一致的实验协议，主要结果难以验证**
- Main text: R1-8B multi-layer GRU "+4.5±3.0 steps lead" (70/30 split)
- Table 7 (Appendix D): single-layer mean lead +3.5±2.3
- Table 8 (Appendix D): multi-layer mean lead = 7.01±1.40 (60/20/20 split)
- 同一方法 lead 从 4.5 到 7.0 步，差异 ~60%
- Main text 核心 GRU 数字的 per-seed 结果未在任何地方报告
- GRU 是 oracle gap 计算基础（Section 4.7），lead 浮动导致 gap 从 77%-89% 都有可能

### Reviewer 1 Weaknesses (Should-Fix)

**[W4] [warning] 32B 统计功效不足以区分 "无效果" 与 "检测不到效果"**
- R1-32B (n=20) precision gap +9.4pp (p=0.050) 与 7-8B 同方向
- Section 4.2 声称 "not a statistical power artifact" 但论证不充分——R1-32B effect size 不小，只是 QwQ-32B 小
- 建议将 R1-32B 标为 inconclusive

**[W5] [warning] Cross-model transfer PCA 不是 alignment，结论过度推断**
- PCA 是 dimensionality reduction 而非 alignment
- 真正的 alignment baselines（Procrustes、CCA、learned linear map）均未尝试
- 声称 "safety representations are model-specific" 过强，应限定为 "PCA-based transfer fails"

**[W6] [warning] QwQ-32B position baseline > HS probe 对 probe 解读构成威胁**
- Position-only 70.6% > HS probe 67.8%
- 如果 probe 分类不如 position baseline，selectivity 可解释性存疑
- 与 W2 联动：alternative layer 可能改变结果

**[W7] [warning] R1-32B selectivity 仅 7.5pp，接近 5pp 阈值且无 CI**
- Control experiment 仅重复 5 次，未报告 std 或 bootstrap CI
- 如果 CI 覆盖 5pp，R1-32B "genuine safety signal" 结论不成立

**[W8] [warning] 每个模型使用不同最优 W，跨模型比较存在 confound**
- R1-8B W=15, OT-7B W=3——R1-8B 享受了 5 倍 temporal smoothing
- 声称 "remarkably consistent +22.4pp and +21.2pp" 但在不同 W 下比较
- 缺少 R1-8B 在 W=3 下的 matched comparison

**[W9] [warning] Precision-undefined traces 排除未做偏差分析**
- 未报告排除了多少 traces
- 不同 modality coverage 差异可能导致系统性偏差

### Reviewer 1 Minor Issues
[M1] R1-8B text W=25 precision (64.8%) 接近 HS W=1 (69.3%)——足够长的 text window 可能消除 modality gap
[M2] 1000 permutation resamples 的 p-value 分辨率限制
[M3] CP 标注无 IAA
[M4] Two-stage detection 仅在 R1-8B 上测试
[M5] discussion.tex 存在但未被 include

### Reviewer 1 Questions
[Q1] OT-7B Table 6: Layer 0 score (35.5) > layer 16 (21.8)，为什么选了 layer 16？
[Q2] Trace-level vs step-level FPR 关系？trace 长度不等时 equal weighting 是否合理？
[Q3] Safe trace FPR 39-62% 远高于 jailbreak pre-CP FPR 4.83-32%，原因？
[Q4] Oracle gap 计算中 K=5 vs K=1 的比较是否 fair？

### Reviewer 1 Missing References
- Turpin et al., 2024 (CoT faithfulness)
- Li et al., 2024 (Inference-Time Intervention)

### Reviewer 1 Overall: 3/5 (Accept to Findings), Confidence 4

---

请对以上每个 Weakness（W1-W9）、Minor Issues（M1-M5）、Questions（Q1-Q4）和 Missing References 分别给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-17T11:43:36.897261+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 交叉回应 — Reviewer 2 对 Reviewer 1 审稿意见的逐条评判\n\n---\n\n### Must-Fix Weaknesses\n\n**[AGREE] R1-Issue-W1: Negative results ��在 R1-8B 验证但结论泛化**\n\n同意这是一个重要缺陷。Section 5.5 Table 6 和 Appendix E 的 BOCPD/CUSUM/Mahalanobis sweep 确实仅覆盖 R1-8B。而 Contribution 3 (\"Comprehensive negative results define method boundaries\") 以及 Section 6 \"Method boundaries\" paragraph 使用的是全称判断：\"safety commitment is gradual rather than abrupt, model-specific rather than universal\"。考虑到 QwQ-32B 的 optimal layer 在 3.1% depth（与 R1-8B 的 44% depth 完全不同），两者的 transition dynamics 可能存在本质差异。至少应在 OT-7B 或一个 32B 模型上验证 BOCPD 是否同样失败。\n\n**[AGREE] R1-Issue-W2: Layer selection metric 缺乏论证且存在 OT-7B 矛盾**\n\n同意。这是方法论上一个实质性漏洞。关键证据：\n\n1. Appendix C Table (tab:ot7b_layer_sweep) 明确显示 Layer 0 score = 35.5 > Layer 16 score = 21.8。论文说 \"selected after correction of a layer selection bug\" 并声称 layer 16 \"achieves the highest balanced accuracy among transformer layers\"——这暗示 bug 修复后改变了 selection criterion（从 acc×crossing_rate 变为 \"最高 balanced accuracy among non-embedding layers\"），但 **未明确说明新 criterion 是什么**。\n\n2. 乘法 metric 的合理性完全未论证。为什么 accuracy 和 crossing rate 的乘积是正确的 proxy？如果换用 accuracy alone，QwQ-32B 可能选择更深的层（layer 2 accuracy 未必最高），整个 \"scale-dependent layer depth\" 的 narrative 可能改变。\n\n3. 与我的 review Q4 一致：QwQ-32B layer 2 (3.1% depth) 的选择使得该模型的 probe 本质上是不同性质的分类器，却与 R1-8B layer 14 (44% depth) 做 modality comparison。\n\n建议确实应包括 layer selection metric ablation。\n\n**[REBUT] R1-Issue-W3: GRU 评估协议不一致**\n\n部分反驳。Reviewer 1 将此定性为 critical，但：\n\n1. 论文在 Appendix D Table 8 caption 中明确说明：\"Main text results (§5.3) use a 70/30 train/test split with different test traces, accounting for the difference in lead values.\" 两套数字来自不同 split 并非隐瞒——是为了提供不同 protocol 下的 robustness evidence。\n\n2. Lead time 从 4.5 变到 7.0 步确实差异大，但 GRU 的 lead time variance 本身就高（Table 7 单 seed 从 +0.9 到 +4.8 步），这是该 model class 的固有特征，不是 reporting 问题。\n\n3. Oracle gap 计算（Section 5.7）用的是 \"+4.5 steps\" (main text protocol)。虽然换 protocol 后 gap 会变，但 oracle 的 +31 steps 远超所有 GRU 数字，gap 从 85.5% 变到 77.4%（用 7.0 steps）不改变 \"enormous gap\" 的定性结论。\n\n不过我同意 main text 核心 GRU 数字（+4.5±3.0）应在附录中提供 per-seed 分解。目前只有 70/30 split 的 aggregate 数字，而 60/20/20 split 有 per-seed 报告，这确实造成了不对称的可验证性。将 severity 从 critical 降到 warning 更合适。\n\n---\n\n### Should-Fix Weaknesses\n\n**[AGREE] R1-Issue-W4: 32B 统计功效不足**\n\n完全同意，与我的 W7 一致。R1-32B precision +9.4pp (p=0.050) 的 effect size 不小——它与 R1-8B 同方向，p-value 恰好在 boundary 上。Section 5.2 声称 \"not a statistical power artifact\" 的论证依赖于 \"32B effect sizes are smaller\"，但这只对 QwQ-32B (+5.7pp) 成立，对 R1-32B (+9.4pp) 不成立。应将 R1-32B 标注为 inconclusive 而非归入 \"no significant advantage\" 阵营。\n\n**[AGREE] R1-Issue-W5: PCA ≠ alignment，结论 overclaimed**\n\n同意。Appendix H 自己承认 \"No cross-model alignment step (Procrustes rotation, CCA, or learned projection) is applied\"。在没有尝试 proper alignment methods 的情况下，Section 5.6 结论 \"safety commitment is encoded in model-specific geometric configurations rather than a universal subspace\" 中的 \"rather than a universal subspace\" 部分过强。PCA 只证明了 unaligned projection 不 work，这是 necessary condition 而非 sufficient evidence for model-specificity。\n\n不过要补充：论文在 Appendix H 最后确实加了 qualifier：\"PCA is a standard linear alignment baseline; its failure indicates that the problem lies in the representations themselves rather than in the choice of alignment method.\" 这个论证有一定道理但不 conclusive——Procrustes fitted on labeled data could still succeed.\n\n**[AGREE] R1-Issue-W6: QwQ-32B position > HS**\n\n同意这构成对 probe 解读的威胁。Position baseline 70.6% > HS probe 67.8% 意味着：在 QwQ-32B 上，knowing what step you're at 比 reading the hidden state at layer 2 更 informative。论文的 defense（selectivity 15.3pp 确认 genuine structure）逻辑上成立——selectivity 证明 probe 学到了超越 random 的结构——但如果该结构不如 position 有用，其 practical 和 interpretive value 都受到质疑。\n\n这与 W2 (layer selection) 强耦合：如果 QwQ-32B 选择更深的层（如 layer 10-20），position baseline 可能不再 dominant。\n\n**[REBUT] R1-Issue-W7: R1-32B selectivity 7.5pp 接近 threshold 且无 CI**\n\n部分反驳。7.5pp 确实接近 5pp threshold，但：\n\n1. Appendix F 报告 control experiment 重复 5 次取 mean，5 次实验的 variance 通常较低（permuted labels 的分类器 accuracy 集中在 chance level 附近）。\n2. 5pp 是 Hewitt & Liang (2019) 推荐的 \"typically considered meaningful\" 阈值（Section 5.5 引用），不是 hard cutoff。7.5pp 是该阈值的 1.5 倍。\n3. 更重要的是：R1-32B 的弱 selectivity 与其整体弱表现一致（Table 3: 最低 accuracy 79.4% at 32B, 最高 FPR 24.2%）。这不是一个需要 \"rescue\" 的结果——论文应该（也确实在 Appendix F 最后）承认 R1-32B signal 最弱。\n\n但同意应报告 5 次实验的 std。\n\n**[REBUT] R1-Issue-W8: 不同 W 下比较存在 confound**\n\n反驳。Reviewer 1 的 concern 基于误读。\n\nTable 3 caption 明确写道：\"HS vs. text probes at each model's validation-selected window (W=15 for R1-8B, W=3 for OT-7B, W=10 for R1-32B, W=5 for QwQ-32B)\"——**每个模型内，HS 和 text 使用相同的 W**。R1-8B 的比较是 HS(W=15) vs Text(W=15)；OT-7B 是 HS(W=3) vs Text(W=3)。modality comparison 在每个模型内是 matched 的。\n\n\"Remarkably consistent +22.4pp and +21.2pp\" 比较的是两个模型各自 matched-W 条件下的 precision gap，不是跨模型用不同 W 比较。这是合法的：两个独立模型各自得出 ~22pp gap，构成 replication evidence。\n\n跨模型不同 W 确实使 absolute performance 不可直接比较（R1-8B 76.8% vs OT-7B 55.8%），但 precision **gap** 的一致性才是论文的 claim。\n\n不过，Reviewer 1 关于 \"缺少 R1-8B 在 W=3 下的 matched comparison\" 的建议是合理的——如果在 W=3 下 R1-8B 的 modality gap 同样是 ~22pp，就更强地支持结论。Appendix B Table (tab:window_full) 有 W=3 HS data (72.3% precision) 但没有对应的 text W=3 数据（text window ablation Table 只报告了 text，没有 matched HS-vs-text comparison at W=3）。\n\n**[AGREE] R1-Issue-W9: Precision-undefined traces 排除未做偏差分析**\n\n同意。Section 5.2 footnote 提到 \"Precision comparisons exclude traces where neither probe produced a positive prediction\"，但未报告：(1) 排除了多少 traces，(2) HS 和 text 的 coverage 差异是否导致不同 traces 被排除。如果 text probe coverage 更高（Appendix B 确认 text W=1 coverage 95.4% vs HS W=1 72.1%），那么 text probe 的 precision 计算包含了更多 \"difficult\" traces（接近 decision boundary），这会系统性压低 text precision，放大 modality gap。这是一个被忽略的 systematic bias source。\n\n---\n\n### Minor Issues\n\n**[AGREE] R1-Issue-M1: Text W=25 接近 HS W=1**\n\n同意观察。Appendix B Table (tab:text_window): R1-8B text W=25 precision = 64.8%；Table (tab:window_full): R1-8B HS W=1 precision = 69.3%。差距仅 4.5pp。这意味着 25 步 text context ≈ 1 步 HS context，暗示 modality gap 可以通过足够的 temporal context 弥合。论文未讨论这一 implication，但它实际上 **支持** \"temporal dominates\" 的 narrative（text 通过更多 context 可接近 HS 单步性能）。\n\n**[AGREE] R1-Issue-M2: 1000 permutations 的 p-value 分辨率**\n\n同意但不重要。1000 resamples 意味着 p-value 分辨率为 0.001。论文报告的几个关键 p-values 是 \"p<0.001\"，这在 1000 permutations 下意味着 0/1000 resamples 超过观察值——真实 p-value 可能远小于 0.001，报告为 \"<0.001\" 是恰当的。不影响结论。\n\n**[AGREE] R1-Issue-M3: CP 标注无 IAA**\n\n同意，与我的 Q3 一致。论文 Limitations 承认了这���点。\n\n**[AGREE] R1-Issue-M4: Two-stage detection 仅 R1-8B**\n\n同意。Appendix G 仅在 R1-8B 上测试 two-stage，且 gain 仅 +1.3pp。Minor issue。\n\n**[REBUT] R1-Issue-M5: discussion.tex 存在但未被 include**\n\n反驳。main.tex line 35 `\\input{sections/conclusion}` 对应的文件实际标题是 \"Discussion and Conclusion\"（Section 6），文件名为 conclusion.tex 但内容是合并的 Discussion+Conclusion。这不是遗漏——是文件命名与内容不一致（section title 为 \"Discussion and Conclusion\"），但排版输出是正确的。如果 discussion.tex 确实是另一个未被 include 的文件，那就是 leftover artifact。不影响论文内容评估。\n\n---\n\n### Questions\n\n**[AGREE] R1-Q1: OT-7B layer selection 矛盾**\n\n同意这需要解释。已在 W2 回应中详述。\n\n**[REBUT] R1-Q2: Trace-level vs step-level FPR 的 weighting**\n\n论文在 Section 3.2 解释了两种 FPR 的关系：step-level pooling 所有 pre-CP steps（长 trace 贡献更多 steps），trace-level 是 per-trace mean FPR 然后 equal-weighting traces。Equal weighting traces 是合理的——它对应 \"每条 trace 是一次部署中的一个 query\" 的 deployment scenario。如果按 step 加权，长 trace（如 OT-7B ~80 steps）会 dominate，不符合实际意义。两种都有道理，论文选择 trace-level 做 statistical test 是为了满足 paired test 的独立性假设。\n\n**[AGREE] R1-Q3: Safe trace FPR 39-62% 远高于 jailbreak pre-CP FPR**\n\n这是一个重要但论文未充分解释的 discrepancy。Section 6 \"Design implications\" 报告 safe trace FPR 39-62%，而 Table 3 的 pre-CP FPR 为 10-32%。差异来源可能是：(1) safe traces 的 reasoning pattern 不同于 jailbreak traces 的 pre-CP 部分（selection bias——只有最终 jailbreak 的 traces 被标注），(2) probe threshold 在 jailbreak traces 上 tuned。这是 probe 不可部署的核心原因之一，论文应更显著地讨论。\n\n**[REBUT] R1-Q4: Oracle gap K=5 vs K=1 comparison fairness**\n\nSection 5.7 说 \"An oracle using ground-truth labels with K=5 detection criterion achieves +31 steps lead; our best method (GRU) achieves +4.5 steps\"。Oracle 用 K=5 是因为 ground-truth labels 允许 consecutive confirmation 而不牺牲 accuracy——这是 oracle 的 privilege。实际方法用 K=1 是因为 higher K 会严重降低 coverage。两者的比较目的不是 \"fair comparison\" 而是 \"upper bound estimation\"——即使你知道真实 labels，你能多早检测到？这个 framing 是合理的，但论文应明确说明 oracle gap 是 best-case upper bound 而非 apples-to-apples comparison。\n\n---\n\n### Missing References\n\n**[REBUT] Turpin et al., 2024 (CoT faithfulness)**\n\n论文已引用 Chen et al. (2025) \"Reasoning Models Don't Always Say What They Think\"（references.bib 中 chen2025unfaithful），这是 CoT faithfulness 的 more recent 和 directly relevant 工作（focused on reasoning models 而非 general LLMs）。Turpin et al. (2024) \"Language Models Don't Always Say What They Think\" 是 precursor，值得引用但并非 critical omission。Agree it should be added but disagree it's a major gap.\n\n**[AGREE] Li et al., 2024 (Inference-Time Intervention, ITI)**\n\n同意应引用。ITI 在 hidden states 上做 inference-time intervention 来修正 model behavior，与本文 \"hidden states encode safety information\" 的 premise 直接相关。它也是 \"from probing to intervention\" 路径的重要 precedent。\n\n---\n\n### Overall Assessment 回应\n\n同意 Reviewer 1 的 overall assessment (3/5, Accept to Findings)。我给出了更低的 2.5 (Leaning Reject)，主要基于 novelty concern（我的 W1-W3 与 R1 的 weaknesses 互补）。两份 review 的共识是：\n\n1. 实验执行质量高、透明度好\n2. 核心 contribution novelty 不足以支撑 main track\n3. 若干方法论 issues（layer selection、32B power、negative results 单模型）需要 address\n4. Findings track 更合适\n\n与 R1 的主要分歧在：(1) 我认为 \"temporal dominates\" 的 overclaim 是 critical issue（R1 未强调此点），(2) R1 强调 GRU protocol 不一致为 critical（我认为是 warning level），(3) 我比 R1 更关注 missing recent references（5 篇 vs 2 篇）。",
  "reviewer_id": "2",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 交叉回应 — Reviewer 2 对 Reviewer 1 审稿意见的逐条评判\n\n---\n\n### Must-Fix Weaknesses\n\n**[AGREE] R1-Issue-W1: Negative results ��在 R1-8B 验证但结论泛化**\n\n同意这是一个重要缺陷。Section 5.5 Table 6 和 Appendix E 的 BOCPD/CUSUM/Mahalanobis sweep 确实仅覆盖 R1-8B。而 Contribution 3 (\"Comprehensive negative results define method boundaries\") 以及 Section 6 \"Method boundaries\" paragraph 使用的是全称判断：\"safety commitment is gradual rather than abrupt, model-specific rather than universal\"。考虑到 QwQ-32B 的 optimal layer 在 3.1% depth（与 R1-8B 的 44% depth 完全不同），两者的 transition dynamics 可能存在本质差异。至少应在 OT-7B 或一个 32B 模型上验证 BOCPD 是否同样失败。\n\n**[AGREE] R1-Issue-W2: Layer selection metric 缺乏论证且存在 OT-7B 矛盾**\n\n同意。这是方法论上一个实质性漏洞。关键证据：\n\n1. Appendix C Table (tab:ot7b_layer_sweep) 明确显示 Layer 0 score = 35.5 > Layer 16 score = 21.8。论文说 \"selected after correction of a layer selection bug\" 并声称 layer 16 \"achieves the highest balanced accuracy among transformer layers\"——这暗示 bug 修复后改变了 selection criterion（从 acc×crossing_rate 变为 \"最高 balanced accuracy among non-embedding layers\"），但 **未明确说明新 criterion 是什么**。\n\n2. 乘法 metric 的合理性完全未论证。为什么 accuracy 和 crossing rate 的乘积是正确的 proxy？如果换用 accuracy alone，QwQ-32B 可能选择更深的层（layer 2 accuracy 未必最高），整个 \"scale-dependent layer depth\" 的 narrative 可能改变。\n\n3. 与我的 review Q4 一致：QwQ-32B layer 2 (3.1% depth) 的选择使得该模型的 probe 本质上是不同性质的分类器，却与 R1-8B layer 14 (44% depth) 做 modality comparison。\n\n建议确实应包括 layer selection metric ablation。\n\n**[REBUT] R1-Issue-W3: GRU 评估协议不一致**\n\n部分反驳。Reviewer 1 将此定性为 critical，但：\n\n1. 论文在 Appendix D Table 8 caption 中明确说明：\"Main text results (§5.3) use a 70/30 train/test split with different test traces, accounting for the difference in lead values.\" 两套数字来自不同 split 并非隐瞒——是为了提供不同 protocol 下的 robustness evidence。\n\n2. Lead time 从 4.5 变到 7.0 步确实差异大，但 GRU 的 lead time variance 本身就高（Table 7 单 seed 从 +0.9 到 +4.8 步），这是该 model class 的固有特征，不是 reporting 问题。\n\n3. Oracle gap 计算（Section 5.7）用的是 \"+4.5 steps\" (main text protocol)。虽然换 protocol 后 gap 会变，但 oracle 的 +31 steps 远超所有 GRU 数字，gap 从 85.5% 变到 77.4%（用 7.0 steps）不改变 \"enormous gap\" 的定性结论。\n\n不过我同意 main text 核心 GRU 数字（+4.5±3.0）应在附录中提供 per-seed 分解。目前只有 70/30 split 的 aggregate 数字，而 60/20/20 split 有 per-seed 报告，这确实造成了不对称的可验证性。将 severity 从 critical 降到 warning 更合适。\n\n---\n\n### Should-Fix Weaknesses\n\n**[AGREE] R1-Issue-W4: 32B 统计功效不足**\n\n完全同意，与我的 W7 一致。R1-32B precision +9.4pp (p=0.050) 的 effect size 不小——它与 R1-8B 同方向，p-value 恰好在 boundary 上。Section 5.2 声称 \"not a statistical power artifact\" 的论证依赖于 \"32B effect sizes are smaller\"，但这只对 QwQ-32B (+5.7pp) 成立，对 R1-32B (+9.4pp) 不成立。应将 R1-32B 标注为 inconclusive 而非归入 \"no significant advantage\" 阵营。\n\n**[AGREE] R1-Issue-W5: PCA ≠ alignment，结论 overclaimed**\n\n同意。Appendix H 自己承认 \"No cross-model alignment step (Procrustes rotation, CCA, or learned projection) is applied\"。在没有尝试 proper alignment methods 的情况下，Section 5.6 结论 \"safety commitment is encoded in model-specific geometric configurations rather than a universal subspace\" 中的 \"rather than a universal subspace\" 部分过强。PCA 只证明了 unaligned projection 不 work，这是 necessary condition 而非 sufficient evidence for model-specificity。\n\n不过要补充：论文在 Appendix H 最后确实加了 qualifier：\"PCA is a standard linear alignment baseline; its failure indicates that the problem lies in the representations themselves rather than in the choice of alignment method.\" 这个论证有一定道理但不 conclusive——Procrustes fitted on labeled data could still succeed.\n\n**[AGREE] R1-Issue-W6: QwQ-32B position > HS**\n\n同意这构成对 probe 解读的威胁。Position baseline 70.6% > HS probe 67.8% 意味着：在 QwQ-32B 上，knowing what step you're at 比 reading the hidden state at layer 2 更 informative。论文的 defense（selectivity 15.3pp 确认 genuine structure）逻辑上成立——selectivity 证明 probe 学到了超越 random 的结构——但如果该结构不如 position 有用，其 practical 和 interpretive value 都受到质疑。\n\n这与 W2 (layer selection) 强耦合：如果 QwQ-32B 选择更深的层（如 layer 10-20），position baseline 可能不再 dominant。\n\n**[REBUT] R1-Issue-W7: R1-32B selectivity 7.5pp 接近 threshold 且无 CI**\n\n部分反驳。7.5pp 确实接近 5pp threshold，但：\n\n1. Appendix F 报告 control experiment 重复 5 次取 mean，5 次实验的 variance 通常较低（permuted labels 的分类器 accuracy 集中在 chance level 附近）。\n2. 5pp 是 Hewitt & Liang (2019) 推荐的 \"typically considered meaningful\" 阈值（Section 5.5 引用），不是 hard cutoff。7.5pp 是该阈值的 1.5 倍。\n3. 更重要的是：R1-32B 的弱 selectivity 与其整体弱表现一致（Table 3: 最低 accuracy 79.4% at 32B, 最高 FPR 24.2%）。这不是一个需要 \"rescue\" 的结果——论文应该（也确实在 Appendix F 最后）承认 R1-32B signal 最弱。\n\n但同意应报告 5 次实验的 std。\n\n**[REBUT] R1-Issue-W8: 不同 W 下比较存在 confound**\n\n反驳。Reviewer 1 的 concern 基于误读。\n\nTable 3 caption 明确写道：\"HS vs. text probes at each model's validation-selected window (W=15 for R1-8B, W=3 for OT-7B, W=10 for R1-32B, W=5 for QwQ-32B)\"——**每个模型内，HS 和 text 使用相同的 W**。R1-8B 的比较是 HS(W=15) vs Text(W=15)；OT-7B 是 HS(W=3) vs Text(W=3)。modality comparison 在每个模型内是 matched 的。\n\n\"Remarkably consistent +22.4pp and +21.2pp\" 比较的是两个模型各自 matched-W 条件下的 precision gap，不是跨模型用不同 W 比较。这是合法的：两个独立模型各自得出 ~22pp gap，构成 replication evidence。\n\n跨模型不同 W 确实使 absolute performance 不可直接比较（R1-8B 76.8% vs OT-7B 55.8%），但 precision **gap** 的一致性才是论文的 claim。\n\n不过，Reviewer 1 关于 \"缺少 R1-8B 在 W=3 下的 matched comparison\" 的建议是合理的——如果在 W=3 下 R1-8B 的 modality gap 同样是 ~22pp，就更强地支持结论。Appendix B Table (tab:window_full) 有 W=3 HS data (72.3% precision) 但没有对应的 text W=3 数据（text window ablation Table 只报告了 text，没有 matched HS-vs-text comparison at W=3）。\n\n**[AGREE] R1-Issue-W9: Precision-undefined traces 排除未做偏差分析**\n\n同意。Section 5.2 footnote 提到 \"Precision comparisons exclude traces where neither probe produced a positive prediction\"，但未报告：(1) 排除了多少 traces，(2) HS 和 text 的 coverage 差异是否导致不同 traces 被排除。如果 text probe coverage 更高（Appendix B 确认 text W=1 coverage 95.4% vs HS W=1 72.1%），那么 text probe 的 precision 计算包含了更多 \"difficult\" traces（接近 decision boundary），这会系统性压低 text precision，放大 modality gap。这是一个被忽略的 systematic bias source。\n\n---\n\n### Minor Issues\n\n**[AGREE] R1-Issue-M1: Text W=25 接近 HS W=1**\n\n同意观察。Appendix B Table (tab:text_window): R1-8B text W=25 precision = 64.8%；Table (tab:window_full): R1-8B HS W=1 precision = 69.3%。差距仅 4.5pp。这意味着 25 步 text context ≈ 1 步 HS context，暗示 modality gap 可以通过足够的 temporal context 弥合。论文未讨论这一 implication，但它实际上 **支持** \"temporal dominates\" 的 narrative（text 通过更多 context 可接近 HS 单步性能）。\n\n**[AGREE] R1-Issue-M2: 1000 permutations 的 p-value 分辨率**\n\n同意但不重要。1000 resamples 意味着 p-value 分辨率为 0.001。论文报告的几个关键 p-values 是 \"p<0.001\"，这在 1000 permutations 下意味着 0/1000 resamples 超过观察值——真实 p-value 可能远小于 0.001，报告为 \"<0.001\" 是恰当的。不影响结论。\n\n**[AGREE] R1-Issue-M3: CP 标注无 IAA**\n\n同意，与我的 Q3 一致。论文 Limitations 承认了这���点。\n\n**[AGREE] R1-Issue-M4: Two-stage detection 仅 R1-8B**\n\n同意。Appendix G 仅在 R1-8B 上测试 two-stage，且 gain 仅 +1.3pp。Minor issue。\n\n**[REBUT] R1-Issue-M5: discussion.tex 存在但未被 include**\n\n反驳。main.tex line 35 `\\input{sections/conclusion}` 对应的文件实际标题是 \"Discussion and Conclusion\"（Section 6），文件名为 conclusion.tex 但内容是合并的 Discussion+Conclusion。这不是遗漏——是文件命名与内容不一致（section title 为 \"Discussion and Conclusion\"），但排版输出是正确的。如果 discussion.tex 确实是另一个未被 include 的文件，那就是 leftover artifact。不影响论文内容评估。\n\n---\n\n### Questions\n\n**[AGREE] R1-Q1: OT-7B layer selection 矛盾**\n\n同意这需要解释。已在 W2 回应中详述。\n\n**[REBUT] R1-Q2: Trace-level vs step-level FPR 的 weighting**\n\n论文在 Section 3.2 解释了两种 FPR 的关系：step-level pooling 所有 pre-CP steps（长 trace 贡献更多 steps），trace-level 是 per-trace mean FPR 然后 equal-weighting traces。Equal weighting traces 是合理的——它对应 \"每条 trace 是一次部署中的一个 query\" 的 deployment scenario。如果按 step 加权，长 trace（如 OT-7B ~80 steps）会 dominate，不符合实际意义。两种都有道理，论文选择 trace-level 做 statistical test 是为了满足 paired test 的独立性假设。\n\n**[AGREE] R1-Q3: Safe trace FPR 39-62% 远高于 jailbreak pre-CP FPR**\n\n这是一个重要但论文未充分解释的 discrepancy。Section 6 \"Design implications\" 报告 safe trace FPR 39-62%，而 Table 3 的 pre-CP FPR 为 10-32%。差异来源可能是：(1) safe traces 的 reasoning pattern 不同于 jailbreak traces 的 pre-CP 部分（selection bias——只有最终 jailbreak 的 traces 被标注），(2) probe threshold 在 jailbreak traces 上 tuned。这是 probe 不可部署的核心原因之一，论文应更显著地讨论。\n\n**[REBUT] R1-Q4: Oracle gap K=5 vs K=1 comparison fairness**\n\nSection 5.7 说 \"An oracle using ground-truth labels with K=5 detection criterion achieves +31 steps lead; our best method (GRU) achieves +4.5 steps\"。Oracle 用 K=5 是因为 ground-truth labels 允许 consecutive confirmation 而不牺牲 accuracy——这是 oracle 的 privilege。实际方法用 K=1 是因为 higher K 会严重降低 coverage。两者的比较目的不是 \"fair comparison\" 而是 \"upper bound estimation\"——即使你知道真实 labels，你能多早检测到？这个 framing 是合理的，但论文应明确说明 oracle gap 是 best-case upper bound 而非 apples-to-apples comparison。\n\n---\n\n### Missing References\n\n**[REBUT] Turpin et al., 2024 (CoT faithfulness)**\n\n论文已引用 Chen et al. (2025) \"Reasoning Models Don't Always Say What They Think\"（references.bib 中 chen2025unfaithful），这是 CoT faithfulness 的 more recent 和 directly relevant 工作（focused on reasoning models 而非 general LLMs）。Turpin et al. (2024) \"Language Models Don't Always Say What They Think\" 是 precursor，值得引用但并非 critical omission。Agree it should be added but disagree it's a major gap.\n\n**[AGREE] Li et al., 2024 (Inference-Time Intervention, ITI)**\n\n同意应引用。ITI 在 hidden states 上做 inference-time intervention 来修正 model behavior，与本文 \"hidden states encode safety information\" 的 premise 直接相关。它也是 \"from probing to intervention\" 路径的重要 precedent。\n\n---\n\n### Overall Assessment 回应\n\n同意 Reviewer 1 的 overall assessment (3/5, Accept to Findings)。我给出了更低的 2.5 (Leaning Reject)，主要基于 novelty concern（我的 W1-W3 与 R1 的 weaknesses 互补）。两份 review 的共识是：\n\n1. 实验执行质量高、透明度好\n2. 核心 contribution novelty 不足以支撑 main track\n3. 若干方法论 issues（layer selection、32B power、negative results 单模型）需要 address\n4. Findings track 更合适\n\n与 R1 的主要分歧在：(1) 我认为 \"temporal dominates\" 的 overclaim 是 critical issue（R1 未强调此点），(2) R1 强调 GRU protocol 不一致为 critical（我认为是 warning level），(3) 我比 R1 更关注 missing recent references（5 篇 vs 2 篇）。",
    "reviewer_id": "2",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-17T11:43:40.612274+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3715
}
```

</details>

---


### Assistant

_source line 190 · 2026-05-17T11:43:48.009064+00:00_

交叉回应已提交给 Director。总结：

- **W1-W2**: AGREE（negative results 单模型泛化 + layer selection 矛盾都是实质缺陷）
- **W3**: REBUT（不同 protocol 有解释，severity 应降为 warning）
- **W4-W6**: AGREE
- **W7**: 部分 REBUT（7.5pp 是 threshold 的 1.5 倍，但应报告 std）
- **W8**: REBUT（每个模型内 HS/text 使用相同 W，modality gap 比较是 matched 的）
- **W9**: AGREE（coverage 差异导致的 systematic bias 被忽略）

两份 review 核心共识：experimental quality 高但 novelty 不足，更适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2"
}
```

</details>

---


## Round 7

## Round 7

62 recorded events


### User

_source line 191 · 2026-05-17T17:22:56.201102+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性、完整性与写作质量**审查。

## Venue 信息
- **目标会议**: EMNLP 2026 via ARR
- **截止日期**: 2026-05-25
- **格式**: Long paper, 8页正文 + 无限参考文献, ACL 官方模板 (`\usepackage[review]{acl}`)
- **审稿模式**: Double-blind
- **Limitations section**: 必须有，不计入页数
- **评分标准**: 5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit

## 论文路径
`projects/contrastive_trace_safety/docs/paper/main.tex`
各章节在 `projects/contrastive_trace_safety/docs/paper/sections/` 下。
References: `projects/contrastive_trace_safety/docs/paper/references.bib`

## 你的审查侧重
1. **Novelty assessment**: 这篇是empirical study还是methodological contribution？Layer selection sensitivity analysis 是否构成genuine methodological contribution？与probing literature中已知的layer selection问题相比novelty在哪？适合Main conference还是Findings track？
2. **Contribution framing calibration**: 
   - Contribution 1 "Layer selection sensitivity as methodological finding" — 是否overclaim？"any study that uses composite metrics...risks the same bias" 这个泛化是否有足够支撑？
   - Contribution 2 "Universal HS advantage" — "universal" 在4个模型上是否成立？R1-32B W=1 only + 25% coverage 是否qualify "advantage"？QwQ-32B lead time负值是否undermine practical value？
   - Contribution 3 "Comprehensive negative results" — 6 alternative methods 是否足够"comprehensive"？
3. **Related Work覆盖度**: 
   - 33 references 对EMNLP long paper是否足够？
   - 是否遗漏2025-2026关键论文？特别是：reasoning model safety新进展、probing methodology进展、hidden state detection领域
   - Positioning：本文与TrajGuard/SafeSwitch/SIREN的区别是否清楚？与SafeThink/SafeRemind的比较是否公平？
4. **AI写作痕迹检查**:
   - Em-dash (—) 和 en-dash (–) 使用是否合规？
   - -ing phrase endings是否过多？
   - 过渡词堆砌（Furthermore/Moreover/Additionally）？
   - 段落是否过度分段？
   - 用词黑名单检查（leverage/utilize/delve into/novel等）
5. **叙事一致性**: Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成连贯主线？有无章节间的framing矛盾？
6. **Abstract质量**: 150-250 words？是否数据堆砌？审稿人能否30秒判断价值？
7. **格式合规**: ACL模板、页数、匿名、Limitations section、Responsible NLP Checklist
8. **Discussion + Conclusion**: 是否存在叙事重复？是否有不必要的内容重复？

## 历史 Issue Tracker 中与你侧重相关的 open/in_progress issues
- **C6** (in_progress): Related Work 32篇仍偏少，遗漏5篇2025-2026高相关论文
- **R2-W8** (in_progress): Novelty ceiling — 纯empirical study，共识Findings track更合适。D030 layer selection sensitivity analysis现在构成methodological contribution
- **R2-W9** (in_progress): Abstract仍含7+统计量
- **R2-W11** (in_progress): Discussion+Conclusion叙事重复，'temporal context dominates'全文重复7+次
- **R2-W14** (in_progress): Text encoder选择可能扩大modality gap，Contribution 2未加qualifier
- **R3-W1** (in_progress): Contribution 1 overclaim — 7-8B上modality gap > temporal gain，'counterintuitive'构成overclaim。D030重写为'universal temporal improvement'
- **R3-W4** (in_progress): Related Work遗漏6篇verified missing references
- **S7** (in_progress): Transfer projection head training data未说明

请阅读论文全文（main.tex + 所有 sections + appendix + references.bib），给出完整审稿报告，包含：
- Summary (2-3句)
- Strengths (逐条)
- Weaknesses (逐条，标注 severity: critical/warning/info，must-fix/should-fix/nice-to-have)
- Questions for authors
- Missing references (如有，用WebSearch验证真实性)
- Overall assessment (评分 + 置信度)
- Detailed per-section comments

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-17T17:23:06.351164+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-17T17:23:06.401802+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-17T17:23:12.076409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-17T17:23:12.528494+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{subcaption}
11	\usepackage{xcolor}
12	\usepackage{colortbl}
13	\usepackage{hyperref}
14	\usepackage{cleveref}
15	
16	\title{Temporal Probing for Safety Commitment Detection in Reasoning Models}
17	
18	\author{Anonymous ARR Submission}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{sections/abstract}
25	\end{abstract}
26	
27	\input{sections/introduction}
28	
29	\input{sections/related_work}
30	
31	\input{sections/method}
32	
33	\input{sections/experiments}
34	
35	\input{sections/discussion}
36	
37	\input{sections/conclusion}
38	
39	\input{sections/limitations}
40	
41	\bibliography{references}
42	
43	\input{sections/appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-17T17:23:12.579139+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-17T17:23:13.483410+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-17T17:23:13.483782+00:00_

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
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 199 · 2026-05-17T17:23:14.186779+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 200 · 2026-05-17T17:23:21.418946+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's what I found about the ACL ARR (ACL Rolling Review) 2025/2026 reviewer guidelines, review form criteria, and scoring:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must b
…[truncated 1418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7935
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-17T17:24:21.973849+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 34, \"total_citations\": 46, \"unique_cited_keys\": 18, \"orphan_bib\": 19, \"missing_bib\": 3, \"duplicate_keys\": 0, \"online_verified\": 26, \"online_not_found\": 8, \"online_mismatch\": 0}, \"cross_check\": {\"orphan_bib\": [\"alain2017understanding\", \"alon2023perplexity\", \"arditi2024refusal\", \"bansal2021stitching\", \"belinkov2017morphology\", \"chen2025unfaithful\", \"conmy2023circuit\", \"conneau2018probing\", \"geiger2021causal\", \"hewitt2019structural\", \"kornblith2019cka\", \"lightman2023prm\", \"meng2022locating\", \"robey2023smoothllm\", \"uesato2022process\", \"vig2020causal\", \"wang2024prm\", \"wang2025lrmsafety\", \"zou2023gcg\"], \"missing_bib\": [\"belinkov2022probing\", \"burns2023discovering\", \"tenney2019bert\"], \"orphan_count\": 19, \"missing_count\": 3}, \"bib_entries\": [{\"key\": \"trajguard\", \"type\": \"article\", \"title\": \"TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense\", \"authors\": \"Liu, Cheng and Liu, Xiaolei and Li, Xingyu and Xin, Bangzhou and Ding, Kangyi\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.07727\"}, {\"key\": \"safeswitch\", \"type\": \"inproceedings\", \"title\": \"SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals\", \"authors\": \"Han, Peixuan and Qian, Cheng and Chen, Xiusi and Zhang, Yuji and Ji, Heng and Zh...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2025\"}, {\"key\": \"siren\", \"type\": \"inproceedings\", \"title\": \"LLM Safety From Within: Detecting Harmful Content with Internal Representations\", \"authors\": \"Jiao, Difan and Liu, Yilun and Yuan, Ye and Tang, Zhenwei and Du, Linfeng and Wu...\", \"year\": \"2026\", \"venue\": \"Proceedings of the 64th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"saferemind\", \"type\": \"article\", \"title\": \"H
…[truncated 25958 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 67787
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-17T17:24:27.648195+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-17T17:24:28.150402+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-17T17:24:29.506527+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Especially: soundness scale, excitement scale, overall assessment scale, reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Especially: soundness scale, excitement scale, overall assessment scale, reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-17T17:24:36.508834+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me."

## Overall Assessment
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## Reproducibility
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible; minor variations possible
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: Results cannot be reproduced

## Datasets & Software
Scale: 1-5 each
- **5**: Enabling f
…[truncated 313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7002
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-17T17:24:40.725135+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-17T17:24:41.127021+00:00_

1	Large Language Models (LLMs) with Chain-of-Thought (CoT) reasoning can self-jailbreak: their extended reasoning traces sometimes transition from safe deliberation to committed harmful generation. Detecting this safety commitment in real time requires comparison of hidden-state (HS) and text-based monitors, yet no prior work systematically compares these modalities or examines how layer selection methodology affects the outcome. We present the first cross-model evaluation of temporal safety probing across four reasoning models, two architectures (Llama, Qwen), two training methods (R1 distillation, STILL), and two scales (7--8B, 32B). We discover that layer selection metric bias entirely determines whether an HS advantage appears: a natural composite metric systematically selects shallow layers at 32B scale and masks the HS signal. At correctly selected layers, all 12 Holm--Bonferroni-corrected hypothesis tests confirm significant HS superiority, with precision gains of +15.4 to +23.6 percentage points (pp) across all four models. Temporal windowing universally improves both modalities. Six alternative approaches (BOCPD/CUSUM change-point detection, Mahalanobis distance, Representation Engineering, MLP probes, CCS, cross-model transfer) all fail, which establishes clear boundaries for current methods. Control task selectivity of 7.5--18.3pp above chance confirms genuine learned safety structure.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-17T17:24:41.177587+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-17T17:24:41.579711+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Reasoning models such as DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq} scale inference-time computation through extended chains of thought (CoT), producing dozens of internal reasoning steps before generating a final response. This deliberative process interleaves safety-aware reasoning with content generation across many steps, and the very capacity for self-reflection introduces a failure mode absent from standard instruction-tuned models. Recent analyses have documented that reasoning models can ``self-jailbreak'': without any adversarial modification to the input prompt, the model's own CoT transitions from considering safety constraints to committing to produce harmful content~\cite{harmthoughts,selfjailbreak}. In a typical self-jailbreak trace, the model begins by acknowledging that a request may be harmful, engages in several steps of safety deliberation, and then gradually shifts toward compliance before abandoning safety reasoning entirely. We refer to the first reasoning step after which safety deliberation permanently ceases as the \textbf{Safety Commitment Point} (CP). Before the CP, the model is still weighing refusal; after it, harmful generation proceeds unchecked. This failure mode is qualitatively different from adversarial jailbreaks on standard LLMs: the harmful transition originates within the model's own reasoning rather than from a crafted input. Detecting this transition in real time is essential for monitoring systems that must intervene before harmful content reaches users, yet no existing detector was designed for this internal commitment process.
4	
5	Existing safety detectors target a fundamentally different problem. Hidden-state (HS) probing methods such as TrajGuard~\cite{trajguard} and SafeSwitch~\cite{safeswitch} monitor internal activations to classify adversarial inputs directed at instruction-tuned Large Language Models (LLMs), achieving above 95\% defense rates on standard b
…[truncated 5987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-17T17:24:41.630469+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-17T17:24:42.082628+00:00_

1	\section{Related Work}\label{sec:related-work}
2	
3	\paragraph{Safety in Reasoning Models.}
4	Reasoning models such as DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq} introduce a qualitatively new safety failure: the model's own chain of thought can transition from safety-aware deliberation to harmful content generation without any adversarial input modification. \citet{harmthoughts} document this self-jailbreak phenomenon and provide step-level annotations of reasoning traces, establishing that commitment to harmful output emerges gradually across multiple reasoning steps. \citet{selfjailbreak} characterize the statistical properties of self-jailbreak, showing that longer reasoning chains increase circumvention probability, but do not propose a deployable detection mechanism. On the mitigation side, SafeThink~\cite{safethink} steers early reasoning steps toward safety through text-level CoT monitoring, while SafeRemind~\cite{saferemind} inserts entropy-triggered safety reminders into the reasoning stream. Both operate on generated text and assume that safety violations are linguistically explicit in the CoT. These works collectively characterize the problem or propose text-level interventions; none conducts a systematic modality comparison to determine whether hidden states or text better supports commitment detection.
5	
6	\paragraph{Hidden-State Safety Detection.}
7	A parallel line of work uses internal model activations to detect safety violations. TrajGuard~\cite{trajguard} computes Mahalanobis distance from safe activation trajectories and achieves above 95\% defense rates on standard instruction-tuned LLMs. SafeSwitch~\cite{safeswitch} trains hidden-state classifiers that trigger safety interventions when activation patterns indicate harmful intent. SIREN~\cite{siren} monitors internal representations during generation and detects harmful content before it reaches users. These methods share a critical assumption: the threat originates from adversarial mani
…[truncated 3681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-17T17:24:42.083101+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-17T17:24:43.037013+00:00_

1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	\subsection{Safety Commitment Point}
5	\label{sec:commitment-point}
6	
7	When a reasoning model is jailbroken, its chain-of-thought (CoT) transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety reasoning permanently ceases. Formally, given a trace of $T$ reasoning steps, the CP is the earliest step $t^*$ such that no step $t > t^*$ contains safety-relevant deliberation. Steps before CP are \emph{pre-commitment} (the model is still considering refusal); steps at or after CP are \emph{post-commitment} (the model has irrevocably committed to harmful output).
8	
9	We operationalize this definition on HarmThoughts~\citep{harmthoughts} traces, which provide step-level annotations of safety reasoning. Each step receives a binary label: pre-CP ($y_t = 0$ for $t < t^*$) or post-CP ($y_t = 1$ for $t \geq t^*$). The detection task is binary classification at each step, producing a score $s_t \in [0, 1]$ that estimates the probability that the model has passed its commitment point by step $t$.
10	
11	We study four reasoning models spanning two architectures (Llama and Qwen) and two parameter scales (7--8B and 32B), summarized in \cref{tab:models}.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\begin{tabular}{lcccccc}
17	\toprule
18	\textbf{Model} & \textbf{Arch.} & \textbf{Params} & \textbf{Layers} & \textbf{Hidden} & \textbf{Traces} & \textbf{Test} \\
19	\midrule
20	R1-8B & Llama & 8B & 32 & 4096 & 209 & 43 \\
21	OT-7B & Qwen & 7B & 28 & 3584 & 228 & 47 \\
22	R1-32B & Qwen & 32B & 64 & 5120 & 100 & 20 \\
23	QwQ-32B & Qwen & 32B & 64 & 5120 & 95 & 19 \\
24	\bottomrule
25	\end{tabular}
26	\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep{deepseekr1}; QwQ-32B~\citep{qwq} is a native reasoning model; OT-7B~\citep{openthinker} is trained with STILL~\citep{still} on Qw
…[truncated 11727 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-17T17:24:43.087737+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-17T17:24:43.489784+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	We evaluate temporal probes across four reasoning models (\cref{tab:models}), comparing hidden-state (HS) and text modalities under different layer selection criteria. Our experiments address three questions: (1)~Does the layer selection metric determine whether HS probes appear effective? (2)~Do HS probes outperform text probes at correctly selected layers? (3)~Which alternative detection methods fail, and why?
4	
5	\subsection{Experimental Setup}\label{sec:setup}
6	
7	\paragraph{Models and data.} We study four models spanning two architectures and two parameter scales: R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (Qwen-7B, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level commitment point (CP) annotations. We use a 60/20/20 train/validation/test split across all models (\cref{tab:models}).
8	
9	\paragraph{Training and evaluation.} All probes use L2-regularized logistic regression with balanced class weights. For each model, we select the temporal window $W$ on the validation set from $W \in \{1, 3, 5, 10, 15, 20, 25\}$. HS probes extract last-token hidden states from a selected transformer layer; text probes encode each reasoning step with all-MiniLM-L6-v2 (384 dimensions). Detection requires $K{=}5$ consecutive threshold crossings. Modality comparisons use a two-sided null-centered bootstrap test (1000 resamples) with Holm-Bonferroni step-down correction across 12 tests (3 metrics $\times$ 4 models, $\alpha{=}0.05$).
10	
11	\paragraph{Layer selection.} We evaluate five layer selection metrics per model (\cref{sec:layer-sensitivity}). The biased composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers for 32B models because representational volatility at early layers inflates the crossing rate component. Four unbiased metrics (pure b
…[truncated 16467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-17T17:24:43.490181+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-17T17:24:43.992460+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Layer selection as researcher degree of freedom.}
4	Layer selection is an underexamined methodological choice in the probing literature that can silently determine a study's conclusions. Our five-metric ablation (\cref{sec:layer-results}) demonstrates that a single metric component, the crossing rate, reverses the central finding of an HS vs.\ text comparison: at biased layers, only 5 of 12 tests survive Holm-Bonferroni correction, producing an apparent scale-dependent modality effect; at corrected layers, all 12 tests pass. The mechanism is general: crossing rate rewards representational volatility at shallow layers independently of discriminative power, and any composite metric that incorporates threshold-crossing frequency risks the same systematic bias toward early layers. This bias is not specific to safety probing. Any threshold-based detection study that uses crossing rate as a layer selection criterion, whether for sentiment, factuality, or toxicity, could produce analogous reversals. We recommend that probing studies report results under at least two independent layer selection criteria, and that five-metric ablations (or at minimum, results at multiple candidate layers spanning shallow, middle, and deep positions) become standard practice. The cost is modest: evaluating five metrics across all layers adds minutes to an experiment that takes hours. The alternative is that conclusions about representational structure reflect layer selection methodology rather than the phenomenon under study.
5	
6	\paragraph{Temporal context and modality choice.}
7	Information-theoretic reasoning suggests that hidden states (4096 to 5120 dimensions of internal computation) should dominate text features (384-dimensional sentence embeddings) purely by signal capacity. Both temporal context and modality choice significantly improve detection, but their relative magnitudes differ by scale. At 7--8B, the modality advanta
…[truncated 4023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-17T17:24:43.992952+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-17T17:24:43.993178+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first systematic evaluation of safety commitment detection across four reasoning models that span two architectures (Llama, Qwen), two training methods (R1 distillation, STILL), and two scales (7--8B, 32B).
4	The central methodological finding is that layer selection metric bias can reverse a study's main conclusion.
5	A composite metric that incorporates crossing rate systematically selects shallow layers at 32B scale, entirely masking the hidden-state advantage and producing the appearance of a scale-dependent effect.
6	When layers are selected by balanced accuracy alone, four independent metrics converge on deep layers (94--98\% depth for 32B models), and all 12 Holm-Bonferroni-corrected hypothesis tests confirm significant hidden-state superiority, with precision gains of +15.4 to +23.6pp across all four models.
7	Six alternative approaches fail to match supervised linear probes: BOCPD and CUSUM cannot detect gradual commitment transitions, Mahalanobis distance misses signal concentrated in minor principal components, Representation Engineering yields model-dependent results, MLP probes overfit at 32B sample sizes, CCS provides no gain over standard probing, and cross-model transfer collapses due to model-specific safety representations.
8	These negative results collectively confirm that safety commitment is gradual, model-specific, and invisible to geometric or unsupervised methods.
9	
10	For practitioners and future probing studies, we recommend temporal windowing ($W{=}3$--$15$) paired with principled layer selection based on pure balanced accuracy as robust defaults.
11	Layer selection sensitivity analysis should become standard practice: without it, composite metrics that embed crossing rate can silently bias conclusions toward shallow layers where positional features dominate.
12	At 32B scale, per-model validation is essential because models with identical architecture but different t
…[truncated 705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-17T17:24:44.445127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-17T17:24:44.998671+00:00_

1	\section{Limitations}\label{sec:limitations}
2	
3	\paragraph{R1-32B statistical narrowness.}
4	Only $W{=}1$ passes Bonferroni correction for R1-32B, covering 25\% of the window range (5 of 20 traces per fold). The dimensionality constraint of $51200 \times W$ features for $n{=}20$ traces prevents reliable evaluation at larger window sizes. Whether collecting more training traces would resolve this statistical limitation remains unknown.
5	
6	\paragraph{QwQ-32B timing limitation.}
7	On QwQ-32B, hidden-state probes achieve higher accuracy than text probes but detect commitment later: HS lead time is negative ($-1.2$ to $+1.9$ steps) compared to text lead time of $3.7$--$12.3$ steps. A position-only baseline achieves comparable balanced accuracy (0.746 vs.\ HS 0.740), suggesting that much of the detection signal on this model is positional rather than representational. The practical value of marginally higher accuracy with later detection depends on the deployment context.
8	
9	\paragraph{High safe-trace false positive rate.}
10	All probing methods produce 39--62\% false positive rates on safe traces at standard operating thresholds. Current probes characterize the commitment phenomenon as a research tool rather than constitute production-ready detectors. The 85.5\% oracle gap between passive monitoring and active intervention shows that early detection via passive probing captures only a fraction of the theoretically available safety signal.
11	
12	\paragraph{Scale and architecture coverage.}
13	We evaluate 4 models spanning 2 architectures (Qwen-2.5, LLaMA-3.1) and 2 parameter scales (7--8B, 32B). Intermediate scales (13B, 70B) that would test whether the observed layer-selection pattern interpolates smoothly are missing. We also lack evaluation on proprietary reasoning models (e.g., o1, o3), where chain-of-thought structure may differ substantially.
14	
15	\paragraph{Text encoder as baseline.}
16	Text probes use a single 384-dimensional encoder (all-MiniLM-L6-v2).
…[truncated 551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-17T17:24:45.049372+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-17T17:24:45.451658+00:00_

1	\appendix
2	
3	\section{Responsible NLP Research Checklist}
4	\label{app:checklist}
5	
6	We address the ARR Responsible NLP Research requirements below.
7	
8	\begin{itemize}
9	    \item \textbf{Limitations discussed:} Yes (\cref{sec:limitations}).
10	    \item \textbf{Potential risks:} This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark.
11	    \item \textbf{Computational budget:} Our experiments involve 4 models with 209, 228, 100, and 95 traces respectively (632 total), using linear probes and single-layer GRUs. Total compute is minimal (under 4 GPU-hours on a single RTX A6000). No large-scale pretraining or finetuning was performed.
12	    \item \textbf{Data:} We use HarmThoughts, a publicly available benchmark with step-level safety annotations. No new data collection was performed.
13	    \item \textbf{Human subjects:} No human subjects research was conducted.
14	    \item \textbf{Reproducibility:} All hyperparameters are reported in \cref{app:gru_details,app:bocpd_config}. Code and corrected data will be released upon publication.
15	\end{itemize}
16	
17	
18	\section{Layer Sweep Results}
19	\label{app:layer_sweep}
20	
21	For each model, we sweep all transformer layers and evaluate five candidate selection metrics: (1)~balanced accuracy $\times$ crossing rate (the biased composite), (2)~pure balanced accuracy, (3)~precision, (4)~inverse pre-CP FPR, and (5)~an additive composite. The biased composite systematically selects shallow layers for 32B models because early-layer representations exhibit higher crossing rates (more frequent threshold crossings) regardless of discriminative power. The four unbiased metrics converge on deep layers for all models.
22	
23	\paragraph{Selected layers.} R1-8B: all five metrics agree on layer~14 (44\% depth). OT-7B: biased m
…[truncated 29948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-17T17:24:45.452082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-17T17:24:45.503277+00:00_

1	@article{trajguard,
2	  title={TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense},
3	  author={Liu, Cheng and Liu, Xiaolei and Li, Xingyu and Xin, Bangzhou and Ding, Kangyi},
4	  journal={arXiv preprint arXiv:2604.07727},
5	  year={2026},
6	  url={https://arxiv.org/abs/2604.07727}
7	}
8	
9	@inproceedings{safeswitch,
10	  title={SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals},
11	  author={Han, Peixuan and Qian, Cheng and Chen, Xiusi and Zhang, Yuji and Ji, Heng and Zhang, Denghui},
12	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
13	  year={2025},
14	  url={https://arxiv.org/abs/2502.01042}
15	}
16	
17	@inproceedings{siren,
18	  title={LLM Safety From Within: Detecting Harmful Content with Internal Representations},
19	  author={Jiao, Difan and Liu, Yilun and Yuan, Ye and Tang, Zhenwei and Du, Linfeng and Wu, Haolun and Anderson, Ashton},
20	  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
21	  year={2026},
22	  url={https://arxiv.org/abs/2604.18519}
23	}
24	
25	@article{saferemind,
26	  title={How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs},
27	  author={Kim, Su-Hyeon and Jin, Hyundong and Lee, Yejin and Han, Yo-Sub},
28	  journal={arXiv preprint arXiv:2601.03662},
29	  year={2026},
30	  url={https://arxiv.org/abs/2601.03662}
31	}
32	
33	@article{safethink,
34	  title={Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away},
35	  author={Ghosal, Soumya Suvra and Chakraborty, Souradip and Singh, Vaibhav and Huang, Furong and Manocha, Dinesh and Bedi, Amrit Singh},
36	  journal={arXiv preprint arXiv:2602.11096},
37	  year={2026},
38	  url={https://arxiv.org/abs/2602.11096}
39	}
40	
41	@article{selfjailbreak,
42	  title={Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training},
43	
…[truncated 11380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-17T17:24:58.000243+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-17T17:24:58.301912+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-17T17:24:58.804394+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-17T17:25:00.261248+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-17T17:25:01.220797+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.|Furthermore|Moreover|Additionally|delve|leverage|utilize|facilitate|myriad|plethora|paradigm shift|in the realm of",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.|Furthermore|Moreover|Additionally|delve|leverage|utilize|facilitate|myriad|plethora|paradigm shift|in the realm of",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-17T17:25:01.848847+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:7:\paragraph{Models and data.} We study four models spanning two architectures and two parameter scales: R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (Qwen-7B, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level commitment point (CP) annotations. We use a 60/20/20 train/validation/test split across all models (\cref{tab:models}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:109:The complementary profiles suggest that the practical value of HS monitoring depends on model-specific detection requirements. Early warning applications favor R1-32B's high lead time despite narrow coverage. Broad reliable detection applications favor QwQ-32B's robust significance despite poor timing. These divergent patterns within the same architecture underscore that per-model validation is essential.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:113:\cref{tab:negative} summarizes seven alternative detection approaches that fail to match supervised temporal probing. The failures span change-point detection, geometric methods, direction-based probing, nonlinear models, semi-supervised learning, and cross-model transfer.
/home/ubuntu/.agent-ml-research-
…[truncated 5853 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 628
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-17T17:25:01.849753+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "hidden state probing safety detection LLM jailbreak 2025 2026 reasoning model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "hidden state probing safety detection LLM jailbreak 2025 2026 reasoning model"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-17T17:25:10.180694+00:00_

Web search results for query: "hidden state probing safety detection LLM jailbreak 2025 2026 reasoning model"

Links: [{"title":"HiddenDetect: Detecting Jailbreak Attacks against Large Vision-Language Models via Monitoring Hidden States","url":"https://arxiv.org/html/2502.14744v1"},{"title":"How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.139/"},{"title":"[2406.05644] How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States","url":"https://arxiv.org/abs/2406.05644"},{"title":"Explain LLM Safety through Intermediate Hidden States","url":"https://aclanthology.org/2024.findings-emnlp.139.pdf"},{"title":"[2604.16824] SafeDream: Safety World Model for Proactive Early Jailbreak Detection","url":"https://arxiv.org/abs/2604.16824"},{"title":"GitHub - ydyjya/LLM-IHS-Explanation","url":"https://github.com/ydyjya/LLM-IHS-Explanation"},{"title":"Alert: Zero-shot LLM Jailbreak Detection via Internal Discrepancy Amplification","url":"https://arxiv.org/html/2601.03600v1"},{"title":"Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection","url":"https://arxiv.org/html/2605.02958"},{"title":"JBShield: Defending Large Language Models from Jailbreak Attacks","url":"https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-341-zhang-shenyi.pdf"},{"title":"Machine Learning for Detection and Analysis of Novel LLM Jailbreaks.","url":"https://arxiv.org/html/2510.01644v2"}]

Based on the search results, here are the key findings on hidden state probing for safety detection and LLM jailbreak research:

## Recent Research on Hidden State-Based Jailbreak Detection

### Core Mechanisms of Safety Through Hidden States

Research employs weak classifiers to explain LLM safety through intermediate hidden states, confirming that LLMs learn ethical concepts during pre-training rather than ali
…[truncated 1438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8330
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-17T17:25:17.459838+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"layer selection\" probing transformer \"researcher degree of freedom\" 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"layer selection\" probing transformer \"researcher degree of freedom\" 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 235 · 2026-05-17T17:25:17.912355+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "reasoning model safety chain-of-thought jailbreak detection 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "reasoning model safety chain-of-thought jailbreak detection 2025 2026 arXiv"
  }
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-17T17:25:18.315933+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"refusal direction\" \"safety probing\" hidden state LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"refusal direction\" \"safety probing\" hidden state LLM 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-17T17:25:24.347245+00:00_

Web search results for query: ""layer selection" probing transformer "researcher degree of freedom" 2024 2025"

Links: [{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.10986"},{"title":"DKAMFormer: Domain Knowledge-Augmented Multiscale Transformer for Remaining Useful Life Prediction of Aeroengine","url":"https://www.ieee-jas.net/en/article/doi/10.1109/JAS.2025.125126"},{"title":"Transformers without Normalization Jiachen Zhu1,2 Xinlei Chen1 Kaiming He3","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhu_Transformers_without_Normalization_CVPR_2025_paper.pdf"},{"title":"Published as a conference paper at ICLR 2025 ADAPTIVE TRANSFORMER PROGRAMS:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf"},{"title":"Machine Learning Jan 2025","url":"https://arxiv.org/list/cs.LG/2025-01?skip=1575&show=2000"},{"title":"Weight-sparse transformers have interpretable circuits","url":"https://cdn.openai.com/pdf/41df8f28-d4ef-43e9-aed2-823f9393e470/circuit-sparsity-paper.pdf"},{"title":"Inner Thinking Transformer: Leveraging Dynamic Depth ...","url":"https://aclanthology.org/2025.acl-long.1369.pdf"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://arxiv.org/html/2510.03282v1"},{"title":"Published as a conference paper at ICLR 2024 LINEARITY OF RELATION DECODING IN","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/2b6d7285306fe896fca9b2e9a02ff6ec-Paper-Conference.pdf"}]

I performed the web search for your query about "layer selection probing transformer researcher degree of freedom" in 2024-2025. Here are the relevant findings:

The search results returned several papers related to transformer probing and interpretability from
…[truncated 1431 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6887
}
```

</details>

---


### Tool result

_source line 238 · 2026-05-17T17:25:26.405393+00:00_

Web search results for query: ""refusal direction" "safety probing" hidden state LLM 2025 2026"

Links: [{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"The Hidden Dimensions of LLM Alignment:","url":"https://arxiv.org/pdf/2502.09674"},{"title":"The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Safety Analysis","url":"https://arxiv.org/html/2502.09674v2"},{"title":"Anchoring Refusal Direction: Mitigating Safety Risks in Tuning via Projection Constraint","url":"https://arxiv.org/html/2509.06795"},{"title":"Refusal Direction in LLM Safety","url":"https://www.emergentmind.com/topics/refusal-direction"},{"title":"SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals","url":"https://arxiv.org/pdf/2502.1042"},{"title":"LLMs Encode Harmfulness and Refusal Separately Jiachen Zhao","url":"https://openreview.net/pdf?id=zLkpt30ngy"},{"title":"Refusal Head in LLM Safety Mechanisms","url":"https://www.emergentmind.com/topics/refusal-head"},{"title":"LLMs Encode Harmfulness and Refusal Separately","url":"https://chats-lab.github.io/LLMs_Encode_Harmfulness_Refusal_Separately/"},{"title":"LLMs Encode Harmfulness and Refusal Separately","url":"https://arxiv.org/html/2507.11878v1"}]

Based on the search results, here's what I found about refusal direction, safety probing, and hidden states in LLMs from recent 2025-2026 research:

## Key Findings on Refusal Direction

Recent research has identified the refusal direction (r-direction) in the hidden states, which plays a pivotal role in governing refusal behavior. Amplifying the hidden state along the r-direction can induce LLMs to generate refusal responses, while ablating it can encourage LLMs to produce affirmative responses.

## Multi-Dimensional Safety Features

Recent work has moved beyond single-direction models. A dominant direction governs the model's refusal behavior, w
…[truncated 1301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8089
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-17T17:25:27.007567+00:00_

Web search results for query: "reasoning model safety chain-of-thought jailbreak detection 2025 2026 arXiv"

Links: [{"title":"H-CoT: Hĳacking the Chain-of-Thought Safety Reasoning ...","url":"https://arxiv.org/pdf/2502.12893"},{"title":"[2501.19180] Enhancing Model Defense Against Jailbreaks with Proactive Safety Reasoning","url":"https://arxiv.org/abs/2501.19180"},{"title":"Chain-of-Thought Hijacking","url":"https://arxiv.org/html/2510.26418v1"},{"title":"[2502.12893] H-CoT: Hijacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models, Including OpenAI o1/o3, DeepSeek-R1, and Gemini 2.0 Flash Thinking","url":"https://arxiv.org/abs/2502.12893"},{"title":"H-CoT: Hijacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models, Including OpenAI o1/o3, DeepSeek-R1, and Gemini 2.0 Flash Thinking","url":"https://arxiv.org/html/2502.12893v1"},{"title":"Beyond Surface-Level Detection: Towards Cognitive-Driven Defense Against Jailbreak Attacks via Meta-Operations Reasoning","url":"https://arxiv.org/html/2508.03054v1"},{"title":"Safer Reasoning Traces: Measuring and Mitigating Chain-of-Thought","url":"https://arxiv.org/pdf/2603.05618"},{"title":"H-CoT: Hijacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models, Including OpenAI o1/o3, DeepSeek-R1, and Gemini 2.0 Flash Thinking | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/h-cot-hijacking-chain-thought-safety-reasoning"},{"title":"Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety","url":"https://arxiv.org/html/2507.11473v2"},{"title":"When Models Outthink Their Safety: Mitigating Self-Jailbreak in Large Reasoning Models with Chain-of-Guardrails","url":"https://arxiv.org/html/2510.21285v1"}]

I've performed a web search on reasoning model safety, chain-of-thought, and jailbreak detection research from 2025-2026 on arXiv. Here are the key findings:

## Major Research Papers Fou
…[truncated 1918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9095
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-17T17:26:45.581614+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", (highlighting|demonstrating|suggesting|indicating|confirming|establishing|showing|making|producing|underscoring|motivating|providing|enabling|ensuring|reducing|improving|capturing)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", (highlighting|demonstrating|suggesting|indicating|confirming|establishing|showing|making|producing|underscoring|motivating|providing|enabling|ensuring|reducing|improving|capturing)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-17T17:26:46.033855+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:82:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex:9:We operationalize this definition on HarmThoughts~\citep{harmthoughts} traces, which provide step-level annotations of safety reasoning. Each step receives a binary label: pre-CP ($y_t = 0$ for $t < t^*$) or post-CP ($y_t = 1$ for $t \geq t^*$). The detection task is binary classification at each step, producing a score $s_t \in [0, 1]$ that estimates the probability that the model has passed its commitment point by step $t$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex:37:\paragraph{Text probes.} We encode each step's text using all-MiniLM-L6-v2, producing a 384-dimensional sentence embedding $\mathbf{e}_t \in \mathbb{R}^{384}$. The same logistic regression procedure is applied to these embeddings. Text probes represent detection performance from surface-leve
…[truncated 3998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-17T17:26:47.037925+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cref\\{sec:temporal_primary\\}|\\\\cref\\{sec:gru\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cref\\{sec:temporal_primary\\}|\\\\cref\\{sec:gru\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-17T17:26:47.490039+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex:31:\cref{tab:window_full} reports the complete window size ablation across all four models and seven window sizes. The main text (\cref{sec:temporal_primary}) presents R1-8B results; here we provide the full data.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex:213:\caption{Per-seed performance of GRU and logistic regression (LR) probes on R1-8B under a 60/20/20 cross-validation protocol (seeds 42, 123, 456). Single = layer 14 only; Multi = 7-layer concatenation (layers 12--24, stride 2). Lead = steps before CP at first sustained crossing. Main text results (\cref{sec:gru}) use a 70/30 train/test split with different test traces, accounting for the difference in lead values.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-17T17:26:47.590863+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"How Alignment and Jailbreak Work\" \"Intermediate Hidden States\" EMNLP 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"How Alignment and Jailbreak Work\" \"Intermediate Hidden States\" EMNLP 2024"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-17T17:26:52.961234+00:00_

Web search results for query: ""How Alignment and Jailbreak Work" "Intermediate Hidden States" EMNLP 2024"

Links: [{"title":"How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.139/"},{"title":"[2406.05644] How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States","url":"https://arxiv.org/abs/2406.05644"},{"title":"How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States [Quick Review]","url":"https://liner.com/review/how-alignment-and-jailbreak-work-explain-llm-safety-through-intermediate"},{"title":"dblp: How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States.","url":"https://dblp.org/rec/conf/emnlp/ZhouYZXHL24.html"},{"title":"Explain LLM Safety through Intermediate Hidden States","url":"https://aclanthology.org/2024.findings-emnlp.139.pdf"},{"title":"How Alignment and Jailbreak Work: Explain LLM Safety ...","url":"https://www.scilit.com/publications/c2ee9b65d93dbbbb45941e8b9ad43cc1"},{"title":"How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States | Request PDF","url":"https://www.researchgate.net/publication/386203615_How_Alignment_and_Jailbreak_Work_Explain_LLM_Safety_through_Intermediate_Hidden_States"},{"title":"How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States | AI Security Portal","url":"https://aisecurity-portal.org/en/literature-database/how-alignment-and-jailbreak-work-explain-llm-safety-through-intermediate-hidden-states/"},{"title":"(PDF) How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States","url":"https://www.researchgate.net/publication/381307904_How_Alignment_and_Jailbreak_Work_Explain_LLM_Safety_through_Intermediate_Hidden_States"},{"title":"How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States - Consensus","url"
…[truncated 1359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5370
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-17T17:27:25.608289+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "novel|first|universal|comprehensive|groundbreaking|revolutionary",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content",
  "-i": "True",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "novel|first|universal|comprehensive|groundbreaking|revolutionary",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content",
    "-i": "True",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-17T17:27:26.110652+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:65:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:69:Text probes benefit universally from larger temporal windows across all four models. Balanced accuracy improves by +3 to +12pp and precision by +8 to +23pp from $W{=}1$ to $W{=}25$, with consistent FPR reductions.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex:3:This work provides the first systematic evaluation of safety commitment detection across four reasoning models that span two architectures (Llama, Qwen), two training methods (R1 distillation, STILL), and two scales (7--8B, 32B).
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex:68:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex:87:\paragraph{Cross-model transfer.} We project hidden states into a shared subspace via PCA and evaluate whether a probe trained on one model transfers to another, testing the universality of commitment representations.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex:94:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sectio
…[truncated 2791 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-17T17:27:26.311812+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{sec:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{sec:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-17T17:27:26.412811+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex:1:\section{Related Work}\label{sec:related-work}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:1:\section{Experiments}\label{sec:experiments}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:5:\subsection{Experimental Setup}\label{sec:setup}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:13:\subsection{Layer Selection Results}\label{sec:layer-results}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:38:\subsection{HS vs.\ Text Comparison}\label{sec:hs-text}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:67:\subsection{Temporal Context Effects}\label{sec:temporal}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:84:\subsection{32B Model-Specific Analysis}\label{sec:32b-analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:111:\subsection{Negative Results}\label{sec:negative}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex:1:\section{Conclusion}\label{sec:conclusion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex:1:\section{Discussion}\label{sec:discussion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex:2:\label{sec:method}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex:5:\label{sec:commitment-point}
…[truncated 1041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-17T17:31:04.522991+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告 — Round 1\n\n**论文**: Temporal Probing for Safety Commitment Detection in Reasoning Models\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**审查侧重**: 新颖性、完整性与写作质量\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 (Findings)\n**一句话总结**: 扎实的 empirical study，layer selection bias 发现有价值，但核心方法是标准 linear probing，novelty ceiling 限制了 main conference 贡献，且引用覆盖度严重不足、多处 framing overclaim。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 实验设计合理，统计方法严谨（Holm-Bonferroni），但 control task selectivity 在 biased layers 上计算（QwQ-32B L2, R1-32B L10）而非 corrected layers，削弱了核心 validation；32B 样本量极小（n=19-20） |\n| Excitement | 2.5/5 | Layer selection bias 发现对 probing community 有方法论价值，但不构成 paradigm-level insight；核心方法无新意（标准 logistic regression probing） |\n| Reproducibility | 4.0/5 | 超参数充分报告，承诺释放代码，bug disclosure 透明；但 HarmThoughts 数据集的 CP annotation 质量和一致性未验证 |\n| Overall Assessment | 3.0/5 | 适合 Findings track：方法论贡献窄（一个 specific metric bias），empirical findings 扎实但无新方法提出 |\n| Confidence | 4/5 | 熟悉 probing methodology 和 LLM safety 文献 |\n\n---\n\n## Summary\n\n本文对四个 reasoning model 进行 safety commitment point 检测的系统评估，比较 hidden-state (HS) 和 text-based probes 的表现。核心发现是 layer selection metric 中的 crossing rate 成分会系统性偏向 shallow layers，掩盖 HS 优势；在 corrected deep layers 上 HS probes 在所有模型上显著优于 text probes。六种替代方法均失败。论文实验设计严谨、统计处理规范，但核心方法是标准 linear probing，novelty 主要来自一个 specific metric bias 的识别，适合 Findings track。\n\n---\n\n## 主要优势\n\n**S1.** Layer selection sensitivity analysis 是本文最强贡献。five-metric ablation 设计严谨，揭示了 crossing rate 如何通过 shallow-layer volatility 系统性偏向早期层，且机制解释清晰（Section 3.3, Table 2）。这对 probing community 有实际指导价值。\n\n**S2.** 统计方法严谨。12 tests 使用 Holm-Bonferroni step-down correction 控制 family-wise error rate，bootstrap 置信区间报告完整，避免了 multiple comparison 常见的 p-hacking 问题（Section 3.6）。\n\n**S3.** Negative results 报告全面且有分析深度。每个失败方法都有 mechanistic 解释：BOCPD/CUSUM 失败因为 commitment 是 gradual 的，Mahalanobis 失败因为信号在 minor PCA components，cross-model transfer 失败说明 safety representations 是 model-specific 的（Section 4.5, Table 4）。\n\n**S4.** Bug disclosure (Appendix F) 体现了科学诚信，主动披露 M002 bug 及其对中间结果的影响。\n\n**S5.** 实验设计覆盖了 2 architectures × 2 scales × 2 training methods 的组合，减少了单一 confound 的风险。\n\n**S6.** Discussion 中的 cross-model divergence 分析（R1-32B vs QwQ-32B，Table 3）提供了有价值的 practical insight，说明同一架构不同训练方法产生截然不同的 detection profiles。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **Control task selectivity 在 biased layers 上计算，corrected layers 无 selectivity 数据**\n- 具体位置：Appendix C (app:control), line 264\n- 问题：QwQ-32B selectivity (15.3pp) 在 L2 计算，R1-32B selectivity (7.5pp) 在 L10 计算。论文承认 \"selectivity scores were computed at the originally selected layers before the layer selection bias was discovered\"，但仅 speculate \"selectivity at corrected layers would equal or exceed the values reported here\"。\n- 为什么影响接收：Control task 是验证 probe 是否 capture genuine safety structure 而非 positional artifacts 的核心 validation。本文的中心论点是 deep layers 才是正确选择，但 deep-layer probes 的 selectivity 未经验证。特别是 R1-32B L10 selectivity 仅 7.5pp（刚过 5pp 阈值），在 L63 上的 selectivity 可能更低也可能更高——这不是可以 speculate 的。QwQ-32B 在 L2 时 position baseline 已经超过 HS probe (70.6% vs 67.8%)，L60 的 selectivity 必须实测。\n- 建议修改方向：在 corrected layers (L60, L63) 重新计算 selectivity，这只需几分钟计算时间。如果 corrected-layer selectivity 低于 5pp，核心 claim 将面临严重挑战。\n\n**N2** [critical] **引用严重不足：仅 15 篇有效引用，3 篇 cited 但 missing from .bib**\n- 具体位置：references.bib, 全文\n- 问题：\n  - (a) **3 篇编译错误**：`belinkov2022probing`（method.tex:68）、`burns2023discovering`（introduction.tex:17, method.tex:85, experiments.tex:139）、`tenney2019bert`（related_work.tex:10, method.tex:68）在 tex 中被 \\cite 但 .bib 中不存在，LaTeX 编译会产生 undefined citation 警告。\n  - (b) **19 篇 orphan 条目**在 .bib 中但未在任何 tex 文件中引用，包括多篇高度相关论文：arditi2024refusal（refusal direction，直接相关）、chen2025unfaithful（reasoning model unfaithfulness）、wang2025lrmsafety（LRM safety survey）、alain2017understanding 和 conneau2018probing（经典 probing 论文）。\n  - (c) **总有效引用仅 15 篇**，远低于 EMNLP long paper 典型的 40-60 篇。\n- 为什么影响接收：审稿人会立刻看出调研不充分。3 篇 undefined citation 说明论文未经完整编译验证。\n- 建议修改方向：(1) 补全 3 篇 missing bib 条目；(2) 将 orphan 中高度相关的论文（至少 arditi2024refusal, chen2025unfaithful, wang2025lrmsafety, alain2017understanding, conneau2018probing）整合进正文引用；(3) 补充下面 N3 列出的 missing references。\n\n**N3** [critical] **Related Work 遗漏多篇 2024-2026 高相关论文**\n- 具体位置：Section 2\n- 遗漏论文（经 WebSearch 验证真实性）：\n  1. **Zhou et al. (2024)** \"How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States\" — EMNLP 2024 Findings。使用 weak classifiers 分析 LLM safety 在不同 layer 的表达方式，发现 early layers 识别 malicious input、middle layers 关联 emotion、deep layers 映射到 refusal tokens。与本文的 layer-level analysis 和 HS safety detection 直接相关。\n  2. **Zhao et al. (2025)** \"LLMs Encode Harmfulness and Refusal Separately\" — 发现 harmfulness 和 refusal 在不同 token position 编码，多个 orthogonal feature directions 预测 refusal behavior。与本文的 refusal direction 和 RepE 分析直接相关。\n  3. **H-CoT (2025)** \"Hijacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models\" — 展示 reasoning model CoT safety 被 hijack 的新攻击方式，与 self-jailbreak 问题直接相关。\n  4. **SafeDream (2026)** \"Safety World Model for Proactive Early Jailbreak Detection\" (arXiv:2604.16824) — 用 world model 进行 proactive jailbreak detection，与本文的 early detection 目标直接相关。\n  5. **\"Tracing the Dynamics of Refusal\" (2026)** (arXiv:2605.02958) — 利用 latent refusal trajectories 进行 jailbreak detection，与本文的 hidden-state trajectory 分析高度重叠。\n- 为什么影响接收：(1)(2) 是 published venue papers，与本文核心研究问题直接相关，遗漏说明文献调研不充分。(5) 与本文的 research question 高度重叠，不引用会被审稿人认为有意回避。\n- 建议修改方向：在 Related Work 的 \"Hidden-State Safety Detection\" 段落中引用 (1)(2)(5)，在 \"Safety in Reasoning Models\" 段落中引用 (3)(4)。补充 positioning：本文与 (1)(5) 的区别在于 temporal commitment detection 和 cross-model comparison，而非 static HS classification。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Contribution 2 \"Universal HS advantage\" overclaim**\n- 具体位置：Introduction 第 15 行, Abstract\n- 问题：\"Universal\" 在 4 个模型上成立，但有重大 qualifier：R1-32B 仅 W=1 达到显著性，coverage 仅 25%（5 of 20 traces）；QwQ-32B lead time 为负（-1.2 to +1.9 steps），text probes 早 3.7-12.3 steps 检测到。QwQ-32B position baseline accuracy (0.746) 与 HS probe (0.740) 几乎相同。\n- 建议：将 \"Universal HS advantage\" 改为 \"Consistent HS precision advantage\" 或类似表述，并在 Contribution 列表中添加 qualifier。\"Universal\" 暗示无条件成立，与实际数据矛盾。\n\n**W2** [warning] **Contribution 1 泛化 claim 支撑不足**\n- 具体位置：Introduction 第 9 行 — \"any study that uses composite metrics to select probe layers risks the same systematic bias\"\n- 问题：这一泛化仅基于一个 composite metric（bal_acc × crossing_rate）在一个 task（safety commitment detection）上的观察。没有测试其他 composite metrics（如 F1 × coverage、AUC × sensitivity 等）在其他 probing tasks（sentiment、factuality、toxicity）上是否产生同样的 bias。\n- 建议：弱化为 \"composite metrics that incorporate threshold-crossing frequency risk the same bias\"（实际在 Discussion 中已有此措辞），确保 Introduction 中的 claim 与 Discussion 一致，不过度泛化。\n\n**W3** [warning] **Abstract 数据堆砌（8+ quantitative claims）**\n- 具体位置：sections/abstract.tex\n- 问题：~190 words 中包含：(1) \"four reasoning models, two architectures, two training methods, two scales\" (2) \"12 Holm-Bonferroni-corrected\" (3) \"+15.4 to +23.6 pp\" (4) \"Six alternative approaches\" + 列举 (5) \"7.5-18.3pp\" (6) 多个方法名缩写。审稿人 30 秒阅读时难以提取核心叙事。\n- 建议：Abstract 保留 3 个关键数字：precision gain 范围、12/12 test pass rate、一个 negative result summary。删除 \"7.5-18.3pp\" 和 6 个方法的逐一列举。\n\n**W4** [warning] **Discussion 与 Conclusion 叙事高度重复**\n- 具体位置：sections/discussion.tex 全文 vs sections/conclusion.tex 全文\n- 问题：两个 section 覆盖几乎相同的 4 个话题：(a) layer selection as researcher DOF (b) temporal context (c) cross-model divergence (d) design implications / future work。Conclusion 本质上是 Discussion 的压缩版。示例重复：\"temporal windowing ($W{=}3$ to $15$) paired with principled layer selection\" 在 Discussion 和 Conclusion 中几乎逐字重复。\"per-model validation is essential\" 在两处均出现。\"85.5% oracle gap\" 在两处均出现。\n- 建议：Conclusion 应仅概括 findings 和 implications（3-4 句），将 detailed analysis、recommendations 和 future work 方向保留在 Discussion 中。目前 Conclusion 15 句太长且与 Discussion 冗余。\n\n**W5** [warning] **Text encoder 选择限制 Contribution 2 的 claim 强度**\n- 具体位置：Section 3.2, Limitations\n- 问题：Text probes 使用 all-MiniLM-L6-v2（384 维），这是一个较弱的 sentence encoder。HS probes 使用 4096-5120 维 hidden states，维度差距约 10-13 倍。Limitations 中承认 \"Larger encoders or domain-fine-tuned models might narrow the observed HS-text accuracy gap\"，但 Contribution 2 的 framing 并未加此 qualifier。\n- 建议：在 Contribution 2 中明确说明 text baseline 使用的是 384-d general-purpose encoder，HS advantage 的 magnitude 可能随更强 text encoder 缩小。\n\n**W6** [warning] **Dangling cross-references**\n- 具体位置：appendix.tex:31 `\\cref{sec:temporal_primary}`、appendix.tex:213 `\\cref{sec:gru}`\n- 问题：`sec:temporal_primary` 不存在（实际 label 是 `sec:temporal`）。`sec:gru` 不存在（GRU 结果仅在 Appendix D，无对应 main text section）。这两个 dangling refs 会在编译时产生 \"??\" 显示。\n- 建议：修复为正确的 label。\n\n**W7** [warning] **32B 模型样本量问题**\n- 具体位置：Table 1, Section 4\n- 问题：R1-32B n=20 test traces, QwQ-32B n=19 test traces。R1-32B 在 W≥3 时因 dimensionality constraint (5120×W features vs n=20) 无法达到显著性，这本质上是 sample size 不足导致的。在如此小的样本上做 bootstrap 1000 resamples 的 p-value 可信度有限。\n- 建议：Discussion 中更明确地讨论 small-sample limitations。考虑报告 effect size (Cohen's d) 作为 p-value 的补充，因为 small-n bootstrap 的 p-value 对个别 extreme traces 很敏感。\n\n**W8** [warning] **Novelty ceiling — empirical study 定位**\n- 具体位置：全文\n- 问题：本文核心方法是 L2-regularized logistic regression（标准方法），应用于 safety commitment detection（新 task）。唯一的方法论贡献是识别 crossing rate bias（一个 specific metric 的 specific bias）。论文没有提出新的 detection 方法、新的 probe 架构、或新的 theoretical framework。这是 well-executed empirical study + narrow methodological finding 的组合。\n- 建议：(a) 如果定位为 Main conference，需要更强的方法论贡献（如提出 bias-corrected layer selection procedure 作为 general tool）。(b) 如果接受 Findings track 定位，当前 framing 是合适的。建议在 Introduction 中更诚实地 position 为 empirical study with methodological finding，而非暗示方法论突破。\n\n---\n\n## 小问题（不影响接收）\n\n- **I1**: Abstract 中 \"Holm--Bonferroni\" 使用了 en-dash (--) 而不是 hyphen (-)。Holm-Bonferroni 是 hyphenated compound name，应使用 hyphen。同一问题出现在正文多处。\n- **I2**: Introduction 段 9 中 \"the first systematic evaluation\" 和 Conclusion 段 3 重复使用相同措辞。\n- **I3**: -ing 短语结尾：related_work.tex:4 \"establishing that commitment...emerges gradually\"、related_work.tex:13 \"motivating the application\"、discussion.tex:4 \"producing an apparent scale-dependent modality effect\" 等。约 15 处 -ing participial endings，数量中等，不严重但可精简。\n- **I4**: 19 篇 orphan bib entries 应清理，保持 bib 文件与 tex 引用同步。\n- **I5**: Table 4 (Negative results) 中 RepE 行的 footnote $^a$ 信息量大但压缩过度，建议在正文中展开。\n\n---\n\n## Questions for Authors\n\n1. **Control task at corrected layers**: 是否有 L60 (QwQ-32B) 和 L63 (R1-32B) 的 selectivity 数据？如果没有，请计算并报告。如果 selectivity < 5pp，如何解释 HS advantage？\n\n2. **Text encoder sensitivity**: 是否测试过更强的 text encoder（如 all-mpnet-base-v2, 768-d; 或 domain-specific encoder）？如果 768-d encoder 将 precision gap 从 +22pp 缩小到 +10pp，Contribution 2 的 practical significance 如何？\n\n3. **CP annotation reliability**: HarmThoughts 的 step-level CP annotations 的 inter-annotator agreement 是多少？如果 annotation noise 较高，probe performance 的 ceiling 可能被 label quality 限制而非 representation quality 限制。\n\n4. **Dimensionality confound**: HS probes 输入 4096-5120 维，text probes 输入 384 维。是否考虑过用 PCA 将 HS 降至 384 维后再比较？这可以控制 dimensionality confound，isolate pure information content 的差异。\n\n5. **Position baseline at corrected layers**: Table 3 报告 QwQ-32B position baseline 与 HS probe balanced accuracy 差距仅 -0.6pp。在 L60 上的 HS vs position comparison 是否仍如此接近？\n\n---\n\n## Missing References（经 WebSearch 验证）\n\n| # | 论文 | Venue/Year | 与本文关系 | 验证状态 |\n|---|------|-----------|-----------|---------|\n| 1 | Zhou et al. \"How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States\" | EMNLP 2024 Findings | Layer-level safety analysis, directly relevant | ✅ Verified via ACL Anthology |\n| 2 | Zhao et al. \"LLMs Encode Harmfulness and Refusal Separately\" | 2025 | Refusal direction multi-dimensionality | ✅ Verified via OpenReview |\n| 3 | H-CoT: \"Hijacking the Chain-of-Thought Safety Reasoning\" | arXiv 2502.12893 (2025) | Reasoning model CoT jailbreak | ✅ Verified via arXiv |\n| 4 | SafeDream: \"Safety World Model for Proactive Early Jailbreak Detection\" | arXiv 2604.16824 (2026) | Proactive jailbreak detection | ✅ Verified via arXiv |\n| 5 | \"Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection\" | arXiv 2605.02958 (2026) | Refusal trajectory detection, high overlap | ✅ Verified via arXiv |\n| 6 | \"Safer Reasoning Traces: Measuring and Mitigating Chain-of-Thought\" | arXiv 2603.05618 (2026) | CoT safety measurement | ✅ Verified via arXiv |\n\n加上 .bib 中已有但未 cite 的高相关论文（arditi2024refusal, chen2025unfaithful, wang2025lrmsafety, alain2017understanding, conneau2018probing），Related Work 部分至少应增加 ~11 篇引用。\n\n---\n\n## Detailed Per-Section Comments\n\n### Abstract\n- 字数 ~190 words，在 150-250 范围内，但信息密度过高。\n- 前两句（problem + gap）清晰有效。\n- 后半段堆砌统计量，削弱叙事流畅度。\n- \"the first cross-model evaluation\" — 考虑到 Zhou et al. (2024) 已做过跨模型 hidden-state safety 分析（7B-70B），\"the first\" 需要更精确的 scope qualifier。\n\n### Introduction\n- 5 段结构完整，叙事逻辑从 self-jailbreak → existing detectors → modality gap → this work → contributions 清晰。\n- 第 3 段（\"The comparison...never been conducted\"）的 gap 陈述有效但略长。\n- Contribution 列表详细且有 section 指向，格式规范。\n- \"entirely determines\" (line 9) 用词过强——应为 \"can determine\" 或 \"significantly affects\"。\n\n### Related Work\n- 4 段组织清晰（Safety in Reasoning Models / HS Detection / Probing Methodology / Change-Point Methods）。\n- 第 2 段 positioning TrajGuard/SafeSwitch/SIREN 做得好，说明了与本文 setting 的本质区别。\n- 整体引用太少（Related Work 段内仅引用 ~12 篇），远低于同类 EMNLP long paper。\n- 缺少 \"Refusal Direction\" 或 \"Safety Representation\" 相关 subsection，应至少讨论 Arditi et al. 2024 和 Zhao et al. 2025。\n\n### Method (Section 3)\n- CP 定义清晰且可操作化（formalized on HarmThoughts annotations）。\n- Layer selection sensitivity analysis (Section 3.3) 是本文最强部分，mechanistic explanation 和 five-metric ablation 设计合理。\n- Baseline 方法覆盖合理，但缺少 attention-based methods。\n- Evaluation protocol 中 bootstrap 程序描述清晰。\n- Transfer projection head (Section 3.4, cross-model transfer) 的 training data 说明不够：PCA \"fitted on the full dataset (including test traces)\" — 这是 data leakage favorable to transfer，但论文承认了这一点。\n\n### Experiments (Section 4)\n- Table 2 (layer selection) 和 Table 3 (HS vs text) 是核心 evidence，呈现清晰。\n- Section 4.4 (32B analysis) 的 per-model 拆分是好的分析决策，避免了 misleading aggregation。\n- Section 4.5 (negative results) Table 4 压缩过度，footnotes 承载太多信息。\n- 缺少 GRU 结果在 main text 的 discussion（方法中描述了 GRU，但结果全在 Appendix D，且 `\\cref{sec:gru}` 是 dangling reference）。\n\n### Discussion\n- 四段讨论覆盖了 layer selection DOF、temporal context、cross-model divergence 和 design implications。\n- \"39-62% FPR on safe traces\" 的坦诚报告是优点。\n- \"85.5% oracle gap\" 的引入有意义，但其计算细节仅在 Appendix E，main text 应提供更多 context。\n- \"temporal windowing ($W{=}3$ to $15$)\" 作为推荐，与 Conclusion 高度重复。\n\n### Conclusion\n- 基本是 Discussion 的压缩重述，缺乏独立价值。\n- 应缩短至 3-4 句核心 takeaway + future work。\n\n### Limitations\n- 6 条 limitations 覆盖全面，包括 statistical narrowness、timing limitation、FPR、scale coverage、text encoder 和 single dataset。\n- 坦诚度高，这是优点。\n\n### Appendix\n- Appendix F (Bug Disclosure) 是重要的 transparency contribution。\n- Appendix G (Two-Stage Detection) 的 marginal improvement (+1.3pp) 说明 fixed-window 已接近 signal ceiling。\n- Appendix C (Control Task) 的 layer provenance 问题如上述 N1。\n\n### 格式合规\n- ✅ `\\usepackage[review]{acl}` — 正确\n- ✅ Double-blind — `\\author{Anonymous ARR Submission}`\n- ✅ Limitations section — 存在，不计入页数\n- ✅ Responsible NLP Checklist — Appendix A\n- ⚠️ 页数：无法从 tex 精确计算，但正文内容量看起来接近 8 页限制。\n- ⚠️ Dangling references: `sec:temporal_primary`, `sec:gru` — 会产生 \"??\" 输出\n\n### AI 写作痕迹\n- ✅ Em-dash (—): 无发现\n- ✅ 解释性 en-dash (–): 无发现\n- ⚠️ -ing phrase endings: ~15 处，中等密度，不严重\n- ✅ 过渡词堆砌: 未见 Furthermore/Moreover/Additionally 连续使用\n- ✅ 黑名单用词: 未见 delve/leverage/utilize/facilitate/myriad/plethora\n- ✅ 段落分段: 正常长度，未过度分段\n- 整体写作质量高于平均，AI 痕迹可控\n\n---\n\n## 最终判断\n\n**推荐**: 3.0 (Findings)\n\n核心理由：\n1. 方法论贡献窄——layer selection bias 是 valuable observation 但不构成 main conference level insight\n2. 核心方法无创新（标准 linear probing）\n3. 引用覆盖度严重不足（15 effective citations, 3 compilation errors, multiple important missing papers）\n4. Control task validation 在 biased layers 计算是方法论缺陷\n5. Multiple overclaims (universal, first, comprehensive) 需要 toning down\n\n如果 N1-N3 能修复（特别是 corrected-layer selectivity 实测结果良好），且 overclaims 得到校准，本文是一篇 solid Findings paper。\n",
  "reviewer_id": "2",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告 — Round 1\n\n**论文**: Temporal Probing for Safety Commitment Detection in Reasoning Models\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**审查侧重**: 新颖性、完整性与写作质量\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 (Findings)\n**一句话总结**: 扎实的 empirical study，layer selection bias 发现有价值，但核心方法是标准 linear probing，novelty ceiling 限制了 main conference 贡献，且引用覆盖度严重不足、多处 framing overclaim。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 实验设计合理，统计方法严谨（Holm-Bonferroni），但 control task selectivity 在 biased layers 上计算（QwQ-32B L2, R1-32B L10）而非 corrected layers，削弱了核心 validation；32B 样本量极小（n=19-20） |\n| Excitement | 2.5/5 | Layer selection bias 发现对 probing community 有方法论价值，但不构成 paradigm-level insight；核心方法无新意（标准 logistic regression probing） |\n| Reproducibility | 4.0/5 | 超参数充分报告，承诺释放代码，bug disclosure 透明；但 HarmThoughts 数据集的 CP annotation 质量和一致性未验证 |\n| Overall Assessment | 3.0/5 | 适合 Findings track：方法论贡献窄（一个 specific metric bias），empirical findings 扎实但无新方法提出 |\n| Confidence | 4/5 | 熟悉 probing methodology 和 LLM safety 文献 |\n\n---\n\n## Summary\n\n本文对四个 reasoning model 进行 safety commitment point 检测的系统评估，比较 hidden-state (HS) 和 text-based probes 的表现。核心发现是 layer selection metric 中的 crossing rate 成分会系统性偏向 shallow layers，掩盖 HS 优势；在 corrected deep layers 上 HS probes 在所有模型上显著优于 text probes。六种替代方法均失败。论文实验设计严谨、统计处理规范，但核心方法是标准 linear probing，novelty 主要来自一个 specific metric bias 的识别，适合 Findings track。\n\n---\n\n## 主要优势\n\n**S1.** Layer selection sensitivity analysis 是本文最强贡献。five-metric ablation 设计严谨，揭示了 crossing rate 如何通过 shallow-layer volatility 系统性偏向早期层，且机制解释清晰（Section 3.3, Table 2）。这对 probing community 有实际指导价值。\n\n**S2.** 统计方法严谨。12 tests 使用 Holm-Bonferroni step-down correction 控制 family-wise error rate，bootstrap 置信区间报告完整，避免了 multiple comparison 常见的 p-hacking 问题（Section 3.6）。\n\n**S3.** Negative results 报告全面且有分析深度。每个失败方法都有 mechanistic 解释：BOCPD/CUSUM 失败因为 commitment 是 gradual 的，Mahalanobis 失败因为信号在 minor PCA components，cross-model transfer 失败说明 safety representations 是 model-specific 的（Section 4.5, Table 4）。\n\n**S4.** Bug disclosure (Appendix F) 体现了科学诚信，主动披露 M002 bug 及其对中间结果的影响。\n\n**S5.** 实验设计覆盖了 2 architectures × 2 scales × 2 training methods 的组合，减少了单一 confound 的风险。\n\n**S6.** Discussion 中的 cross-model divergence 分析（R1-32B vs QwQ-32B，Table 3）提供了有价值的 practical insight，说明同一架构不同训练方法产生截然不同的 detection profiles。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **Control task selectivity 在 biased layers 上计算，corrected layers 无 selectivity 数据**\n- 具体位置：Appendix C (app:control), line 264\n- 问题：QwQ-32B selectivity (15.3pp) 在 L2 计算，R1-32B selectivity (7.5pp) 在 L10 计算。论文承认 \"selectivity scores were computed at the originally selected layers before the layer selection bias was discovered\"，但仅 speculate \"selectivity at corrected layers would equal or exceed the values reported here\"。\n- 为什么影响接收：Control task 是验证 probe 是否 capture genuine safety structure 而非 positional artifacts 的核心 validation。本文的中心论点是 deep layers 才是正确选择，但 deep-layer probes 的 selectivity 未经验证。特别是 R1-32B L10 selectivity 仅 7.5pp（刚过 5pp 阈值），在 L63 上的 selectivity 可能更低也可能更高——这不是可以 speculate 的。QwQ-32B 在 L2 时 position baseline 已经超过 HS probe (70.6% vs 67.8%)，L60 的 selectivity 必须实测。\n- 建议修改方向：在 corrected layers (L60, L63) 重新计算 selectivity，这只需几分钟计算时间。如果 corrected-layer selectivity 低于 5pp，核心 claim 将面临严重挑战。\n\n**N2** [critical] **引用严重不足：仅 15 篇有效引用，3 篇 cited 但 missing from .bib**\n- 具体位置：references.bib, 全文\n- 问题：\n  - (a) **3 篇编译错误**：`belinkov2022probing`（method.tex:68）、`burns2023discovering`（introduction.tex:17, method.tex:85, experiments.tex:139）、`tenney2019bert`（related_work.tex:10, method.tex:68）在 tex 中被 \\cite 但 .bib 中不存在，LaTeX 编译会产生 undefined citation 警告。\n  - (b) **19 篇 orphan 条目**在 .bib 中但未在任何 tex 文件中引用，包括多篇高度相关论文：arditi2024refusal（refusal direction，直接相关）、chen2025unfaithful（reasoning model unfaithfulness）、wang2025lrmsafety（LRM safety survey）、alain2017understanding 和 conneau2018probing（经典 probing 论文）。\n  - (c) **总有效引用仅 15 篇**，远低于 EMNLP long paper 典型的 40-60 篇。\n- 为什么影响接收：审稿人会立刻看出调研不充分。3 篇 undefined citation 说明论文未经完整编译验证。\n- 建议修改方向：(1) 补全 3 篇 missing bib 条目；(2) 将 orphan 中高度相关的论文（至少 arditi2024refusal, chen2025unfaithful, wang2025lrmsafety, alain2017understanding, conneau2018probing）整合进正文引用；(3) 补充下面 N3 列出的 missing references。\n\n**N3** [critical] **Related Work 遗漏多篇 2024-2026 高相关论文**\n- 具体位置：Section 2\n- 遗漏论文（经 WebSearch 验证真实性）：\n  1. **Zhou et al. (2024)** \"How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States\" — EMNLP 2024 Findings。使用 weak classifiers 分析 LLM safety 在不同 layer 的表达方式，发现 early layers 识别 malicious input、middle layers 关联 emotion、deep layers 映射到 refusal tokens。与本文的 layer-level analysis 和 HS safety detection 直接相关。\n  2. **Zhao et al. (2025)** \"LLMs Encode Harmfulness and Refusal Separately\" — 发现 harmfulness 和 refusal 在不同 token position 编码，多个 orthogonal feature directions 预测 refusal behavior。与本文的 refusal direction 和 RepE 分析直接相关。\n  3. **H-CoT (2025)** \"Hijacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models\" — 展示 reasoning model CoT safety 被 hijack 的新攻击方式，与 self-jailbreak 问题直接相关。\n  4. **SafeDream (2026)** \"Safety World Model for Proactive Early Jailbreak Detection\" (arXiv:2604.16824) — 用 world model 进行 proactive jailbreak detection，与本文的 early detection 目标直接相关。\n  5. **\"Tracing the Dynamics of Refusal\" (2026)** (arXiv:2605.02958) — 利用 latent refusal trajectories 进行 jailbreak detection，与本文的 hidden-state trajectory 分析高度重叠。\n- 为什么影响接收：(1)(2) 是 published venue papers，与本文核心研究问题直接相关，遗漏说明文献调研不充分。(5) 与本文的 research question 高度重叠，不引用会被审稿人认为有意回避。\n- 建议修改方向：在 Related Work 的 \"Hidden-State Safety Detection\" 段落中引用 (1)(2)(5)，在 \"Safety in Reasoning Models\" 段落中引用 (3)(4)。补充 positioning：本文与 (1)(5) 的区别在于 temporal commitment detection 和 cross-model comparison，而非 static HS classification。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Contribution 2 \"Universal HS advantage\" overclaim**\n- 具体位置：Introduction 第 15 行, Abstract\n- 问题：\"Universal\" 在 4 个模型上成立，但有重大 qualifier：R1-32B 仅 W=1 达到显著性，coverage 仅 25%（5 of 20 traces）；QwQ-32B lead time 为负（-1.2 to +1.9 steps），text probes 早 3.7-12.3 steps 检测到。QwQ-32B position baseline accuracy (0.746) 与 HS probe (0.740) 几乎相同。\n- 建议：将 \"Universal HS advantage\" 改为 \"Consistent HS precision advantage\" 或类似表述，并在 Contribution 列表中添加 qualifier。\"Universal\" 暗示无条件成立，与实际数据矛盾。\n\n**W2** [warning] **Contribution 1 泛化 claim 支撑不足**\n- 具体位置：Introduction 第 9 行 — \"any study that uses composite metrics to select probe layers risks the same systematic bias\"\n- 问题：这一泛化仅基于一个 composite metric（bal_acc × crossing_rate）在一个 task（safety commitment detection）上的观察。没有测试其他 composite metrics（如 F1 × coverage、AUC × sensitivity 等）在其他 probing tasks（sentiment、factuality、toxicity）上是否产生同样的 bias。\n- 建议：弱化为 \"composite metrics that incorporate threshold-crossing frequency risk the same bias\"（实际在 Discussion 中已有此措辞），确保 Introduction 中的 claim 与 Discussion 一致，不过度泛化。\n\n**W3** [warning] **Abstract 数据堆砌（8+ quantitative claims）**\n- 具体位置：sections/abstract.tex\n- 问题：~190 words 中包含：(1) \"four reasoning models, two architectures, two training methods, two scales\" (2) \"12 Holm-Bonferroni-corrected\" (3) \"+15.4 to +23.6 pp\" (4) \"Six alternative approaches\" + 列举 (5) \"7.5-18.3pp\" (6) 多个方法名缩写。审稿人 30 秒阅读时难以提取核心叙事。\n- 建议：Abstract 保留 3 个关键数字：precision gain 范围、12/12 test pass rate、一个 negative result summary。删除 \"7.5-18.3pp\" 和 6 个方法的逐一列举。\n\n**W4** [warning] **Discussion 与 Conclusion 叙事高度重复**\n- 具体位置：sections/discussion.tex 全文 vs sections/conclusion.tex 全文\n- 问题：两个 section 覆盖几乎相同的 4 个话题：(a) layer selection as researcher DOF (b) temporal context (c) cross-model divergence (d) design implications / future work。Conclusion 本质上是 Discussion 的压缩版。示例重复：\"temporal windowing ($W{=}3$ to $15$) paired with principled layer selection\" 在 Discussion 和 Conclusion 中几乎逐字重复。\"per-model validation is essential\" 在两处均出现。\"85.5% oracle gap\" 在两处均出现。\n- 建议：Conclusion 应仅概括 findings 和 implications（3-4 句），将 detailed analysis、recommendations 和 future work 方向保留在 Discussion 中。目前 Conclusion 15 句太长且与 Discussion 冗余。\n\n**W5** [warning] **Text encoder 选择限制 Contribution 2 的 claim 强度**\n- 具体位置：Section 3.2, Limitations\n- 问题：Text probes 使用 all-MiniLM-L6-v2（384 维），这是一个较弱的 sentence encoder。HS probes 使用 4096-5120 维 hidden states，维度差距约 10-13 倍。Limitations 中承认 \"Larger encoders or domain-fine-tuned models might narrow the observed HS-text accuracy gap\"，但 Contribution 2 的 framing 并未加此 qualifier。\n- 建议：在 Contribution 2 中明确说明 text baseline 使用的是 384-d general-purpose encoder，HS advantage 的 magnitude 可能随更强 text encoder 缩小。\n\n**W6** [warning] **Dangling cross-references**\n- 具体位置：appendix.tex:31 `\\cref{sec:temporal_primary}`、appendix.tex:213 `\\cref{sec:gru}`\n- 问题：`sec:temporal_primary` 不存在（实际 label 是 `sec:temporal`）。`sec:gru` 不存在（GRU 结果仅在 Appendix D，无对应 main text section）。这两个 dangling refs 会在编译时产生 \"??\" 显示。\n- 建议：修复为正确的 label。\n\n**W7** [warning] **32B 模型样本量问题**\n- 具体位置：Table 1, Section 4\n- 问题：R1-32B n=20 test traces, QwQ-32B n=19 test traces。R1-32B 在 W≥3 时因 dimensionality constraint (5120×W features vs n=20) 无法达到显著性，这本质上是 sample size 不足导致的。在如此小的样本上做 bootstrap 1000 resamples 的 p-value 可信度有限。\n- 建议：Discussion 中更明确地讨论 small-sample limitations。考虑报告 effect size (Cohen's d) 作为 p-value 的补充，因为 small-n bootstrap 的 p-value 对个别 extreme traces 很敏感。\n\n**W8** [warning] **Novelty ceiling — empirical study 定位**\n- 具体位置：全文\n- 问题：本文核心方法是 L2-regularized logistic regression（标准方法），应用于 safety commitment detection（新 task）。唯一的方法论贡献是识别 crossing rate bias（一个 specific metric 的 specific bias）。论文没有提出新的 detection 方法、新的 probe 架构、或新的 theoretical framework。这是 well-executed empirical study + narrow methodological finding 的组合。\n- 建议：(a) 如果定位为 Main conference，需要更强的方法论贡献（如提出 bias-corrected layer selection procedure 作为 general tool）。(b) 如果接受 Findings track 定位，当前 framing 是合适的。建议在 Introduction 中更诚实地 position 为 empirical study with methodological finding，而非暗示方法论突破。\n\n---\n\n## 小问题（不影响接收）\n\n- **I1**: Abstract 中 \"Holm--Bonferroni\" 使用了 en-dash (--) 而不是 hyphen (-)。Holm-Bonferroni 是 hyphenated compound name，应使用 hyphen。同一问题出现在正文多处。\n- **I2**: Introduction 段 9 中 \"the first systematic evaluation\" 和 Conclusion 段 3 重复使用相同措辞。\n- **I3**: -ing 短语结尾：related_work.tex:4 \"establishing that commitment...emerges gradually\"、related_work.tex:13 \"motivating the application\"、discussion.tex:4 \"producing an apparent scale-dependent modality effect\" 等。约 15 处 -ing participial endings，数量中等，不严重但可精简。\n- **I4**: 19 篇 orphan bib entries 应清理，保持 bib 文件与 tex 引用同步。\n- **I5**: Table 4 (Negative results) 中 RepE 行的 footnote $^a$ 信息量大但压缩过度，建议在正文中展开。\n\n---\n\n## Questions for Authors\n\n1. **Control task at corrected layers**: 是否有 L60 (QwQ-32B) 和 L63 (R1-32B) 的 selectivity 数据？如果没有，请计算并报告。如果 selectivity < 5pp，如何解释 HS advantage？\n\n2. **Text encoder sensitivity**: 是否测试过更强的 text encoder（如 all-mpnet-base-v2, 768-d; 或 domain-specific encoder）？如果 768-d encoder 将 precision gap 从 +22pp 缩小到 +10pp，Contribution 2 的 practical significance 如何？\n\n3. **CP annotation reliability**: HarmThoughts 的 step-level CP annotations 的 inter-annotator agreement 是多少？如果 annotation noise 较高，probe performance 的 ceiling 可能被 label quality 限制而非 representation quality 限制。\n\n4. **Dimensionality confound**: HS probes 输入 4096-5120 维，text probes 输入 384 维。是否考虑过用 PCA 将 HS 降至 384 维后再比较？这可以控制 dimensionality confound，isolate pure information content 的差异。\n\n5. **Position baseline at corrected layers**: Table 3 报告 QwQ-32B position baseline 与 HS probe balanced accuracy 差距仅 -0.6pp。在 L60 上的 HS vs position comparison 是否仍如此接近？\n\n---\n\n## Missing References（经 WebSearch 验证）\n\n| # | 论文 | Venue/Year | 与本文关系 | 验证状态 |\n|---|------|-----------|-----------|---------|\n| 1 | Zhou et al. \"How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States\" | EMNLP 2024 Findings | Layer-level safety analysis, directly relevant | ✅ Verified via ACL Anthology |\n| 2 | Zhao et al. \"LLMs Encode Harmfulness and Refusal Separately\" | 2025 | Refusal direction multi-dimensionality | ✅ Verified via OpenReview |\n| 3 | H-CoT: \"Hijacking the Chain-of-Thought Safety Reasoning\" | arXiv 2502.12893 (2025) | Reasoning model CoT jailbreak | ✅ Verified via arXiv |\n| 4 | SafeDream: \"Safety World Model for Proactive Early Jailbreak Detection\" | arXiv 2604.16824 (2026) | Proactive jailbreak detection | ✅ Verified via arXiv |\n| 5 | \"Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection\" | arXiv 2605.02958 (2026) | Refusal trajectory detection, high overlap | ✅ Verified via arXiv |\n| 6 | \"Safer Reasoning Traces: Measuring and Mitigating Chain-of-Thought\" | arXiv 2603.05618 (2026) | CoT safety measurement | ✅ Verified via arXiv |\n\n加上 .bib 中已有但未 cite 的高相关论文（arditi2024refusal, chen2025unfaithful, wang2025lrmsafety, alain2017understanding, conneau2018probing），Related Work 部分至少应增加 ~11 篇引用。\n\n---\n\n## Detailed Per-Section Comments\n\n### Abstract\n- 字数 ~190 words，在 150-250 范围内，但信息密度过高。\n- 前两句（problem + gap）清晰有效。\n- 后半段堆砌统计量，削弱叙事流畅度。\n- \"the first cross-model evaluation\" — 考虑到 Zhou et al. (2024) 已做过跨模型 hidden-state safety 分析（7B-70B），\"the first\" 需要更精确的 scope qualifier。\n\n### Introduction\n- 5 段结构完整，叙事逻辑从 self-jailbreak → existing detectors → modality gap → this work → contributions 清晰。\n- 第 3 段（\"The comparison...never been conducted\"）的 gap 陈述有效但略长。\n- Contribution 列表详细且有 section 指向，格式规范。\n- \"entirely determines\" (line 9) 用词过强——应为 \"can determine\" 或 \"significantly affects\"。\n\n### Related Work\n- 4 段组织清晰（Safety in Reasoning Models / HS Detection / Probing Methodology / Change-Point Methods）。\n- 第 2 段 positioning TrajGuard/SafeSwitch/SIREN 做得好，说明了与本文 setting 的本质区别。\n- 整体引用太少（Related Work 段内仅引用 ~12 篇），远低于同类 EMNLP long paper。\n- 缺少 \"Refusal Direction\" 或 \"Safety Representation\" 相关 subsection，应至少讨论 Arditi et al. 2024 和 Zhao et al. 2025。\n\n### Method (Section 3)\n- CP 定义清晰且可操作化（formalized on HarmThoughts annotations）。\n- Layer selection sensitivity analysis (Section 3.3) 是本文最强部分，mechanistic explanation 和 five-metric ablation 设计合理。\n- Baseline 方法覆盖合理，但缺少 attention-based methods。\n- Evaluation protocol 中 bootstrap 程序描述清晰。\n- Transfer projection head (Section 3.4, cross-model transfer) 的 training data 说明不够：PCA \"fitted on the full dataset (including test traces)\" — 这是 data leakage favorable to transfer，但论文承认了这一点。\n\n### Experiments (Section 4)\n- Table 2 (layer selection) 和 Table 3 (HS vs text) 是核心 evidence，呈现清晰。\n- Section 4.4 (32B analysis) 的 per-model 拆分是好的分析决策，避免了 misleading aggregation。\n- Section 4.5 (negative results) Table 4 压缩过度，footnotes 承载太多信息。\n- 缺少 GRU 结果在 main text 的 discussion（方法中描述了 GRU，但结果全在 Appendix D，且 `\\cref{sec:gru}` 是 dangling reference）。\n\n### Discussion\n- 四段讨论覆盖了 layer selection DOF、temporal context、cross-model divergence 和 design implications。\n- \"39-62% FPR on safe traces\" 的坦诚报告是优点。\n- \"85.5% oracle gap\" 的引入有意义，但其计算细节仅在 Appendix E，main text 应提供更多 context。\n- \"temporal windowing ($W{=}3$ to $15$)\" 作为推荐，与 Conclusion 高度重复。\n\n### Conclusion\n- 基本是 Discussion 的压缩重述，缺乏独立价值。\n- 应缩短至 3-4 句核心 takeaway + future work。\n\n### Limitations\n- 6 条 limitations 覆盖全面，包括 statistical narrowness、timing limitation、FPR、scale coverage、text encoder 和 single dataset。\n- 坦诚度高，这是优点。\n\n### Appendix\n- Appendix F (Bug Disclosure) 是重要的 transparency contribution。\n- Appendix G (Two-Stage Detection) 的 marginal improvement (+1.3pp) 说明 fixed-window 已接近 signal ceiling。\n- Appendix C (Control Task) 的 layer provenance 问题如上述 N1。\n\n### 格式合规\n- ✅ `\\usepackage[review]{acl}` — 正确\n- ✅ Double-blind — `\\author{Anonymous ARR Submission}`\n- ✅ Limitations section — 存在，不计入页数\n- ✅ Responsible NLP Checklist — Appendix A\n- ⚠️ 页数：无法从 tex 精确计算，但正文内容量看起来接近 8 页限制。\n- ⚠️ Dangling references: `sec:temporal_primary`, `sec:gru` — 会产生 \"??\" 输出\n\n### AI 写作痕迹\n- ✅ Em-dash (—): 无发现\n- ✅ 解释性 en-dash (–): 无发现\n- ⚠️ -ing phrase endings: ~15 处，中等密度，不严重\n- ✅ 过渡词堆砌: 未见 Furthermore/Moreover/Additionally 连续使用\n- ✅ 黑名单用词: 未见 delve/leverage/utilize/facilitate/myriad/plethora\n- ✅ 段落分段: 正常长度，未过度分段\n- 整体写作质量高于平均，AI 痕迹可控\n\n---\n\n## 最终判断\n\n**推荐**: 3.0 (Findings)\n\n核心理由：\n1. 方法论贡献窄——layer selection bias 是 valuable observation 但不构成 main conference level insight\n2. 核心方法无创新（标准 linear probing）\n3. 引用覆盖度严重不足（15 effective citations, 3 compilation errors, multiple important missing papers）\n4. Control task validation 在 biased layers 计算是方法论缺陷\n5. Multiple overclaims (universal, first, comprehensive) 需要 toning down\n\n如果 N1-N3 能修复（特别是 corrected-layer selectivity 实测结果良好），且 overclaims 得到校准，本文是一篇 solid Findings paper。\n",
    "reviewer_id": "2",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-17T17:31:08.440758+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3917
}
```

</details>

---


### Assistant

_source line 252 · 2026-05-17T17:31:19.186820+00:00_

审稿报告已提交给 Review Director。

**核心结论**：Overall 3.0/5 (Findings track)。

三个 Must-Fix 问题：
1. Control task selectivity 在 biased layers 计算（L2, L10），corrected layers (L60, L63) 缺实测数据
2. 3 篇 cited 但 missing from .bib 的引用会导致编译错误；总有效引用仅 15 篇，远低于 EMNLP long paper 标准
3. Related Work 遗漏至少 6 篇 2024-2026 高相关论文（Zhou et al. EMNLP'24, "Tracing the Dynamics of Refusal" 等）

主要 Should-Fix："Universal HS advantage" overclaim、Abstract 数据堆砌、Discussion/Conclusion 重复。

写作质量方面：无 em-dash，-ing 短语中等密度，整体 AI 痕迹可控。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2"
}
```

</details>

---


## Round 8

## Round 8

4 recorded events


### User

_source line 253 · 2026-05-17T17:34:34.602286+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）
- 特别关注与你自己报告中观点不同的地方

---

### Reviewer 1 的 Must-Fix 问题

**R1-N1** [critical] Control task selectivity 未在 corrected layers 计算，构成方法论循环
- 与你的 N1 相同的 concern
- R1 特别指出这构成"循环论证"：用 probe 性能来推断 selectivity，而 selectivity 本应独立验证 probe 是否捕获语义信号

**R1-N2** [critical] 3 个核心引用缺失导致编译错误
- belinkov2022probing, tenney2019bert, burns2023discovering
- 与你的 N2(a) 部分相同

**R1-N3** [critical] Cross-model transfer claim 过度概括
- Abstract "cross-model transfer fails entirely, confirming that safety representations are model-specific"
- R1 认为 PCA 是最简单的线性降维，其失败不能证明 "transfer fails entirely"
- 更强对齐方法（CCA, Procrustes, learned projection, model stitching）可能产生不同结论
- bib 中已有 Kornblith et al. 2019 (CKA) 和 Bansal et al. 2021 (model stitching) 但未引用

### Reviewer 1 的 Should-Fix 问题

**R1-W1** [warning] Bootstrap 仅 1000 次重采样，低于发表标准（推荐 10,000）
- p-value 分辨率限制在 0.001
- 32B 小样本 + 低重采样数组合削弱推断

**R1-W2** [warning] 数据划分不一致：
- 主文 60/20/20 vs GRU 70/30 vs Two-stage n=55
- GRU 与 LR probe 结果不直接可比
- n=55 来源不明

**R1-W3** [warning] QwQ-32B position baseline 与 HS 竞争性（-0.6pp）未在 Abstract/Contributions 充分体现

**R1-W4** [warning] 5-metric ablation 的 4 个 "unbiased" 指标数学上高度相关
- Precision 和 inverse FPR 基于混淆矩阵相同单元格
- Additive composite 包含其他三个
- "four independent metrics agree" 夸大证据强度

**R1-W5** [warning] 32B 样本量限制在 Abstract/Contributions 中被系统性淡化

**R1-W6** [warning] BOCPD/CUSUM 在 OT-7B 和 32B 上 "0% detection" 缺少支撑数据表

**R1-W7** [warning] 负面方法计数不一致：Abstract "Six" vs Table 4 列出 7 个

### Reviewer 1 的 Overall Assessment
- **3.0 / 5 (Findings)**
- Soundness 3.0, Excitement 3.5, Reproducibility 2.5
- Layer selection sensitivity 有价值但 32B 实验验证存在多个方法论缺口

---

请对以上每条 must-fix 和 should-fix 给出 [AGREE] 或 [REBUT] 回应。特别注意：
1. R1-N3（cross-model transfer overclaim）你的报告中未重点关注，请给出独立判断
2. R1-W1（bootstrap 1000 vs 10000）和 R1-W4（metric independence）是 R1 独有的 concern
3. R1-W2（数据划分不一致）提供了比你的分析更具体的三处矛盾

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-17T17:37:21.085906+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 交叉回应 — Reviewer 1 审稿意见\n\n---\n\n## Must-Fix 逐条回应\n\n### [AGREE] R1-N1: Control task selectivity 未在 corrected layers 计算\n\n同意，且这与我的 N1 完全一致。R1 的 \"循环论证\" 表述比我的更准确——selectivity 的功能是**独立验证** probe 是否捕获语义信号，而非从 probe 性能反推 selectivity。Appendix C (line 264) 作者自己承认 \"selectivity scores were computed at the originally selected layers before the layer selection bias was discovered\"，然后 speculate \"selectivity at corrected layers would equal or exceed the values reported here\"。这个 speculation 恰恰违背了 control task 的验证逻辑。\n\n补充证据：QwQ-32B 在 L2 时 position baseline 已超过 HS probe (0.746 vs 0.740, Table 3)，说明 L2 处 positional feature 主导。如果 deep layers (L60) 确实编码了更强的 semantic safety signal，selectivity 应该更高——但这需要实测，不能推断。计算 cost 极低（几分钟），属于必须补的实验。\n\n---\n\n### [AGREE] R1-N2: 3 个核心引用缺失导致编译错误\n\n完全同意，与我的 N2(a) 一致。belinkov2022probing 在 method.tex:68 被引用作为 deep-layer probing 的文献支撑，burns2023discovering 在 introduction.tex:17 和 method.tex:85 被引用作为 CCS 的原始论文，tenney2019bert 在 related_work.tex:10 被引用论证 layer-wise representation 分布。这三篇是论文核心论证链上的引用，缺失会导致编译产生 undefined citation warnings，审稿人看到 \"[?]\" 会直接扣分。\n\n---\n\n### [AGREE] R1-N3: Cross-model transfer claim 过度概括\n\n同意 R1 的判断。我在 Round 1 报告中未重点关注此问题，现在认为 R1 的分析是正确的。\n\n**理由：**\n\n1. **方法覆盖不足**：Appendix H (app:transfer_details) 明确说 \"No cross-model alignment step (Procrustes rotation, CCA, or learned projection) is applied\"。PCA 是最简单的线性降维，它不做任何 cross-model alignment，仅独立地对两个模型的 hidden states 做 variance-based projection。PCA 失败仅能证明 \"variance-preserving projection 不足以实现 transfer\"，不能证明 \"transfer fails entirely\"。\n\n2. **Orphan bib 暴露了意识但未执行**：kornblith2019cka (CKA) 和 bansal2021stitching (model stitching) 在 .bib 中存在但未被引用（我的 N2 orphan list 中已列出）。这说明作者知道这些更强的对齐方法存在，但选择不实验也不讨论。审稿人看到 bib 中有但正文不引用，会更强烈地质疑 claim 的诚实度。\n\n3. **逻辑问题**：Abstract 的 \"cross-model transfer fails entirely, confirming that safety representations are model-specific\" 是一个 strong universal claim。但 Appendix H 中 QwQ→R1-32B direct transfer 达到 67.3%（超过 within-model baseline 65.2%），作者自己也承认 \"exceeds the within-model baseline\"。用 \"fails entirely\" 来描述一个超过 baseline 的结果是 misleading。虽然 1% crossing rate 确实使其无实用价值，但正确的 claim 应是 \"fails to achieve practical utility\" 而非 \"fails entirely\"。\n\n4. **更强方法可能改变结论**：CCA 可以找到 maximally correlated subspaces，Procrustes 可以做 orthogonal alignment，learned projection (如 linear regression mapping) 可以适应 non-trivial geometric differences。如果 safety signal 确实存在于两个模型中但 geometric configuration 不同（论文自己的解释），那么 alignment methods 正是为解决此问题设计的。\n\n**建议**：将 \"fails entirely\" 改为 \"fails under linear dimensionality reduction (PCA)\"，并在 Discussion 中承认更强 alignment methods 可能产生不同结论。\n\n---\n\n## Should-Fix 逐条回应\n\n### [AGREE] R1-W1: Bootstrap 仅 1000 次重采样\n\n部分同意。1000 resamples 在 NLP 文献中很常见，对于 p < 0.001 级别的显著性结果足够可靠。但 R1 的 concern 在 32B 小样本场景下更有力：n=19-20 的 bootstrap 每次仅抽 19-20 个 traces，1000 次重采样可能不足以稳定地估计 sampling distribution 的尾部。\n\n具体看 borderline p-values：R1-8B FPR p=0.044 (Section 4.3, line 59)、R1-32B FPR p=0.007。0.044 意味着 1000 次中仅 ~44 次超过观测值，bootstrap standard error 约为 ±0.006，即真实 p 可能在 0.038-0.050 之间波动。这在 Holm-Bonferroni correction 下仍然 pass（adjusted threshold 为 0.05/10=0.005 对于最后几个 test），但精度确实有限。\n\n10,000 resamples 是低成本改进（几秒钟），在审稿意见要求下没有理由不做。但这不是 critical issue——即使 p-value 分辨率提高，不太可能改变 12/12 pass 的结论。\n\n---\n\n### [AGREE] R1-W2: 数据划分不一致\n\n完全同意。R1 比我的分析更具体，发现了三处明确矛盾：\n\n1. **60/20/20 vs 70/30**：Main text 全部使用 60/20/20 (Table 1)，但 GRU appendix (appendix.tex:213) 明确说 \"Main text results (\\cref{sec:gru}) use a 70/30 train/test split with different test traces\"。这意味着 GRU 和 LR probe 的 test set 不同，lead time 和 accuracy 数字不可直接比较。\n\n2. **n=55 来源不明**：Two-stage detection (Appendix G, appendix.tex:344) 说 \"R1-8B test traces (n=55; 39 jailbreak, 16 benign)\"。但 Table 1 报告 R1-8B test set 为 n=43。55 ≠ 43。可能的解释是 two-stage 用了 validation + test 合并，但论文未说明。\n\n3. **可比性问题**：不同 split 意味着不同 test traces，如果 R1-8B 存在 outlier traces（如特别长或特别短的），不同 split 可能选中不同 outliers，导致 metrics 差异反映 split 选择而非方法差异。\n\n这不影响 core claim（HS vs text comparison 使用一致的 60/20/20），但影响 GRU 和 two-stage 的可信度。应在 Appendix 中明确标注每个实验的 split，或统一为 60/20/20。\n\n---\n\n### [AGREE] R1-W3: QwQ-32B position baseline 竞争性被淡化\n\n同意，与我的 W1 一致。Table 3 报告 \"HS vs Position: -0.6pp\"，但 Abstract 和 Contribution 2 仍使用 \"Universal HS advantage\" 表述。当 position baseline 达到 HS probe 同等水平时，\"HS advantage\" 的 practical significance 大幅降低。作者在 Experiments Section 4.4 中有坦诚讨论，但 Abstract/Contributions 的 framing 没有反映这一 qualification。\n\n---\n\n### [AGREE] R1-W4: 5-metric ablation 的 \"independent\" claim 被夸大\n\n同意。R1 的数学分析是准确的：\n\n- **Precision** = TP/(TP+FP)，**Inverse FPR** = TN/(TN+FP) = 1 - FP/(TN+FP)。两者都通过 FP 耦合——低 FP 同时推高 precision 和 inverse FPR。\n- **Additive composite** = bal_acc + precision - FPR，字面上包含其他三个指标的线性组合。\n- **Balanced accuracy** = (sensitivity + specificity)/2，其中 specificity = TN/(TN+FP) = inverse FPR。所以 bal_acc 和 inverse FPR 也有数学耦合。\n\n这意味着 \"四个 unbiased metrics 独立收敛\" 实际上是 ~1.5-2 个独立信号（pure discrimination ability 和 FP-based metrics）在不同 formulations 下的一致表现。证据强度被 overcounted。\n\n但 R1-W4 不改变核心结论：crossing rate 是唯一导致 shallow-layer selection 的 component。论文的正确 framing 应该是 \"所有不含 crossing rate 的指标都选择 deep layers\"，而非 \"四个独立指标收敛\"。\n\n---\n\n### [AGREE] R1-W5: 32B 样本量限制被系统性淡化\n\n同意，与我的 W7 一致。Abstract 中 \"across all four models\" 和 \"all 12 tests pass\" 的措辞暗示四个模型的 evidence 同等强度，但实际上 7-8B (n=43-47) 的统计功效远高于 32B (n=19-20)。R1-32B 仅 W=1 pass 且 coverage 25%，本质上是 sample-size-limited artifact。建议 Abstract 中加入 \"with caveats at 32B scale\" 或类似 qualifier。\n\n---\n\n### [AGREE] R1-W6: BOCPD/CUSUM 在 OT-7B 和 32B 上 \"0% detection\" 缺少支撑数据\n\n完全同意。Appendix F (Table in app:bocpd_config) 仅提供 R1-8B 的 BOCPD/CUSUM sweep 结果。Section 4.5 (line 135) claim \"On OT-7B and both 32B models, BOCPD achieves 0% detection across all hazard rate configurations\"，但没有任何 table 或 figure 支撑这一 claim。\n\nR1-8B 上 BOCPD 在 λ=5 时达到 97% detection rate，而其他三个模型全部 0%——这是一个极端差异，需要解释 *为什么* 以及 supporting data。可能的解释包括 trace 长度差异、probe score 分布差异等，但论文未讨论。至少应提供 OT-7B 和 32B 的 sweep table 或 summary statistics。\n\n---\n\n### [AGREE] R1-W7: 负面方法计数不一致\n\n同意。Abstract 和 Introduction Contribution 3 说 \"Six alternative approaches\"/\"Six alternative detection methods\"，而 Section 4.5 (line 113) 说 \"seven alternative detection approaches\"。Table 4 列出 7 行（BOCPD, CUSUM, Mahalanobis, RepE, MLP, CCS, Transfer）。\n\nAbstract 将 BOCPD/CUSUM 合并计为一类（\"BOCPD/CUSUM change-point detection\"），但 Table 4 分列且它们有不同的 failure modes 和不同的 performance profiles（BOCPD 在 R1-8B 93% detection, CUSUM 在所有模型上 underperform threshold）。如果合并计数，应在 Table 4 中也合并行或加说明。如果分列，应将 Abstract 改为 \"Seven\"。\n\n---\n\n## R1 Overall Assessment 与我的对比\n\n| 维度 | R1 | R2 (我) | 分歧分析 |\n|------|-----|---------|---------|\n| Soundness | 3.0 | 3.0 | **一致** |\n| Excitement | 3.5 | 2.5 | **分歧**：R1 给 layer selection finding 更高 novelty credit。我认为该 finding 虽有价值但过于 narrow（one specific metric bias），不构成方法论突破。 |\n| Reproducibility | 2.5 | 4.0 | **分歧**：R1 因数据 split 不一致和缺失 data tables 降分。我基于 hyperparameter 充分报告、bug disclosure 和 code release 承诺给高分。经交叉审查，我认为 R1 的 concern 有理——data split 不一致 (R1-W2) 确实影响 reproducibility，我调整为 **3.5/5**。 |\n| Overall | 3.0 | 3.0 | **一致**：Findings track |\n\n**Excitement 分歧说明**：R1 的 3.5 暗示论文接近 Main conference 下界。我维持 2.5，理由是：(1) 核心方法是标准 logistic regression，无方法创新；(2) layer selection bias finding 虽然对 probing community 有指导价值，但 scope 很窄——仅证明了一个 specific metric (bal_acc × crossing_rate) 在一个 specific task 上的 bias，泛化证据不足（我的 W2）；(3) R1-W4 进一步削弱了 \"four independent metrics converge\" 的 evidence strength。如果作者能在 rebuttal 中展示该 bias 在其他 probing tasks 上也成立，我愿意上调至 3.0。\n\n---\n\n## 新增观察（基于交叉审查）\n\nR1-N3 提醒我注意了一个我之前未重点分析的模式：**bib 中的 orphan entries 暴露了 \"知道但不做\" 的问题**。kornblith2019cka, bansal2021stitching 在 bib 中但不 cited，说明作者在文献调研阶段找到了这些更强的 representation comparison 方法，但既没有实验也没有在正文中讨论为什么不使用。这比单纯的遗漏更严重——它暗示作者可能意识到更强方法会弱化 \"transfer fails entirely\" 的 claim。\n\n结合我的 N2 (19 orphan entries)，bib 文件的状态整体反映了 rushed submission：文献被收集但未整合进正文。\n\n---\n\n## 总结\n\nR1 的 7 条 should-fix 中有多条提供了比我更具体的分析（特别是 W2 数据 split、W4 metric independence、W7 方法计数），补充了我的审查盲区。R1-N3 (cross-model transfer overclaim) 是我应该但未在 Round 1 重点关注的问题。\n\n两位 Reviewer 在 Overall Assessment (3.0, Findings) 和 Soundness (3.0) 上完全一致，分歧集中在 Excitement 和 Reproducibility 的子维度上。核心共识：这是一篇 well-executed empirical study，layer selection finding 有价值，但 novelty ceiling、sample size limitations、引用不足和多处 overclaim 限制了其 Main conference competitiveness。\n",
  "reviewer_id": "2",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 交叉回应 — Reviewer 1 审稿意见\n\n---\n\n## Must-Fix 逐条回应\n\n### [AGREE] R1-N1: Control task selectivity 未在 corrected layers 计算\n\n同意，且这与我的 N1 完全一致。R1 的 \"循环论证\" 表述比我的更准确——selectivity 的功能是**独立验证** probe 是否捕获语义信号，而非从 probe 性能反推 selectivity。Appendix C (line 264) 作者自己承认 \"selectivity scores were computed at the originally selected layers before the layer selection bias was discovered\"，然后 speculate \"selectivity at corrected layers would equal or exceed the values reported here\"。这个 speculation 恰恰违背了 control task 的验证逻辑。\n\n补充证据：QwQ-32B 在 L2 时 position baseline 已超过 HS probe (0.746 vs 0.740, Table 3)，说明 L2 处 positional feature 主导。如果 deep layers (L60) 确实编码了更强的 semantic safety signal，selectivity 应该更高——但这需要实测，不能推断。计算 cost 极低（几分钟），属于必须补的实验。\n\n---\n\n### [AGREE] R1-N2: 3 个核心引用缺失导致编译错误\n\n完全同意，与我的 N2(a) 一致。belinkov2022probing 在 method.tex:68 被引用作为 deep-layer probing 的文献支撑，burns2023discovering 在 introduction.tex:17 和 method.tex:85 被引用作为 CCS 的原始论文，tenney2019bert 在 related_work.tex:10 被引用论证 layer-wise representation 分布。这三篇是论文核心论证链上的引用，缺失会导致编译产生 undefined citation warnings，审稿人看到 \"[?]\" 会直接扣分。\n\n---\n\n### [AGREE] R1-N3: Cross-model transfer claim 过度概括\n\n同意 R1 的判断。我在 Round 1 报告中未重点关注此问题，现在认为 R1 的分析是正确的。\n\n**理由：**\n\n1. **方法覆盖不足**：Appendix H (app:transfer_details) 明确说 \"No cross-model alignment step (Procrustes rotation, CCA, or learned projection) is applied\"。PCA 是最简单的线性降维，它不做任何 cross-model alignment，仅独立地对两个模型的 hidden states 做 variance-based projection。PCA 失败仅能证明 \"variance-preserving projection 不足以实现 transfer\"，不能证明 \"transfer fails entirely\"。\n\n2. **Orphan bib 暴露了意识但未执行**：kornblith2019cka (CKA) 和 bansal2021stitching (model stitching) 在 .bib 中存在但未被引用（我的 N2 orphan list 中已列出）。这说明作者知道这些更强的对齐方法存在，但选择不实验也不讨论。审稿人看到 bib 中有但正文不引用，会更强烈地质疑 claim 的诚实度。\n\n3. **逻辑问题**：Abstract 的 \"cross-model transfer fails entirely, confirming that safety representations are model-specific\" 是一个 strong universal claim。但 Appendix H 中 QwQ→R1-32B direct transfer 达到 67.3%（超过 within-model baseline 65.2%），作者自己也承认 \"exceeds the within-model baseline\"。用 \"fails entirely\" 来描述一个超过 baseline 的结果是 misleading。虽然 1% crossing rate 确实使其无实用价值，但正确的 claim 应是 \"fails to achieve practical utility\" 而非 \"fails entirely\"。\n\n4. **更强方法可能改变结论**：CCA 可以找到 maximally correlated subspaces，Procrustes 可以做 orthogonal alignment，learned projection (如 linear regression mapping) 可以适应 non-trivial geometric differences。如果 safety signal 确实存在于两个模型中但 geometric configuration 不同（论文自己的解释），那么 alignment methods 正是为解决此问题设计的。\n\n**建议**：将 \"fails entirely\" 改为 \"fails under linear dimensionality reduction (PCA)\"，并在 Discussion 中承认更强 alignment methods 可能产生不同结论。\n\n---\n\n## Should-Fix 逐条回应\n\n### [AGREE] R1-W1: Bootstrap 仅 1000 次重采样\n\n部分同意。1000 resamples 在 NLP 文献中很常见，对于 p < 0.001 级别的显著性结果足够可靠。但 R1 的 concern 在 32B 小样本场景下更有力：n=19-20 的 bootstrap 每次仅抽 19-20 个 traces，1000 次重采样可能不足以稳定地估计 sampling distribution 的尾部。\n\n具体看 borderline p-values：R1-8B FPR p=0.044 (Section 4.3, line 59)、R1-32B FPR p=0.007。0.044 意味着 1000 次中仅 ~44 次超过观测值，bootstrap standard error 约为 ±0.006，即真实 p 可能在 0.038-0.050 之间波动。这在 Holm-Bonferroni correction 下仍然 pass（adjusted threshold 为 0.05/10=0.005 对于最后几个 test），但精度确实有限。\n\n10,000 resamples 是低成本改进（几秒钟），在审稿意见要求下没有理由不做。但这不是 critical issue——即使 p-value 分辨率提高，不太可能改变 12/12 pass 的结论。\n\n---\n\n### [AGREE] R1-W2: 数据划分不一致\n\n完全同意。R1 比我的分析更具体，发现了三处明确矛盾：\n\n1. **60/20/20 vs 70/30**：Main text 全部使用 60/20/20 (Table 1)，但 GRU appendix (appendix.tex:213) 明确说 \"Main text results (\\cref{sec:gru}) use a 70/30 train/test split with different test traces\"。这意味着 GRU 和 LR probe 的 test set 不同，lead time 和 accuracy 数字不可直接比较。\n\n2. **n=55 来源不明**：Two-stage detection (Appendix G, appendix.tex:344) 说 \"R1-8B test traces (n=55; 39 jailbreak, 16 benign)\"。但 Table 1 报告 R1-8B test set 为 n=43。55 ≠ 43。可能的解释是 two-stage 用了 validation + test 合并，但论文未说明。\n\n3. **可比性问题**：不同 split 意味着不同 test traces，如果 R1-8B 存在 outlier traces（如特别长或特别短的），不同 split 可能选中不同 outliers，导致 metrics 差异反映 split 选择而非方法差异。\n\n这不影响 core claim（HS vs text comparison 使用一致的 60/20/20），但影响 GRU 和 two-stage 的可信度。应在 Appendix 中明确标注每个实验的 split，或统一为 60/20/20。\n\n---\n\n### [AGREE] R1-W3: QwQ-32B position baseline 竞争性被淡化\n\n同意，与我的 W1 一致。Table 3 报告 \"HS vs Position: -0.6pp\"，但 Abstract 和 Contribution 2 仍使用 \"Universal HS advantage\" 表述。当 position baseline 达到 HS probe 同等水平时，\"HS advantage\" 的 practical significance 大幅降低。作者在 Experiments Section 4.4 中有坦诚讨论，但 Abstract/Contributions 的 framing 没有反映这一 qualification。\n\n---\n\n### [AGREE] R1-W4: 5-metric ablation 的 \"independent\" claim 被夸大\n\n同意。R1 的数学分析是准确的：\n\n- **Precision** = TP/(TP+FP)，**Inverse FPR** = TN/(TN+FP) = 1 - FP/(TN+FP)。两者都通过 FP 耦合——低 FP 同时推高 precision 和 inverse FPR。\n- **Additive composite** = bal_acc + precision - FPR，字面上包含其他三个指标的线性组合。\n- **Balanced accuracy** = (sensitivity + specificity)/2，其中 specificity = TN/(TN+FP) = inverse FPR。所以 bal_acc 和 inverse FPR 也有数学耦合。\n\n这意味着 \"四个 unbiased metrics 独立收敛\" 实际上是 ~1.5-2 个独立信号（pure discrimination ability 和 FP-based metrics）在不同 formulations 下的一致表现。证据强度被 overcounted。\n\n但 R1-W4 不改变核心结论：crossing rate 是唯一导致 shallow-layer selection 的 component。论文的正确 framing 应该是 \"所有不含 crossing rate 的指标都选择 deep layers\"，而非 \"四个独立指标收敛\"。\n\n---\n\n### [AGREE] R1-W5: 32B 样本量限制被系统性淡化\n\n同意，与我的 W7 一致。Abstract 中 \"across all four models\" 和 \"all 12 tests pass\" 的措辞暗示四个模型的 evidence 同等强度，但实际上 7-8B (n=43-47) 的统计功效远高于 32B (n=19-20)。R1-32B 仅 W=1 pass 且 coverage 25%，本质上是 sample-size-limited artifact。建议 Abstract 中加入 \"with caveats at 32B scale\" 或类似 qualifier。\n\n---\n\n### [AGREE] R1-W6: BOCPD/CUSUM 在 OT-7B 和 32B 上 \"0% detection\" 缺少支撑数据\n\n完全同意。Appendix F (Table in app:bocpd_config) 仅提供 R1-8B 的 BOCPD/CUSUM sweep 结果。Section 4.5 (line 135) claim \"On OT-7B and both 32B models, BOCPD achieves 0% detection across all hazard rate configurations\"，但没有任何 table 或 figure 支撑这一 claim。\n\nR1-8B 上 BOCPD 在 λ=5 时达到 97% detection rate，而其他三个模型全部 0%——这是一个极端差异，需要解释 *为什么* 以及 supporting data。可能的解释包括 trace 长度差异、probe score 分布差异等，但论文未讨论。至少应提供 OT-7B 和 32B 的 sweep table 或 summary statistics。\n\n---\n\n### [AGREE] R1-W7: 负面方法计数不一致\n\n同意。Abstract 和 Introduction Contribution 3 说 \"Six alternative approaches\"/\"Six alternative detection methods\"，而 Section 4.5 (line 113) 说 \"seven alternative detection approaches\"。Table 4 列出 7 行（BOCPD, CUSUM, Mahalanobis, RepE, MLP, CCS, Transfer）。\n\nAbstract 将 BOCPD/CUSUM 合并计为一类（\"BOCPD/CUSUM change-point detection\"），但 Table 4 分列且它们有不同的 failure modes 和不同的 performance profiles（BOCPD 在 R1-8B 93% detection, CUSUM 在所有模型上 underperform threshold）。如果合并计数，应在 Table 4 中也合并行或加说明。如果分列，应将 Abstract 改为 \"Seven\"。\n\n---\n\n## R1 Overall Assessment 与我的对比\n\n| 维度 | R1 | R2 (我) | 分歧分析 |\n|------|-----|---------|---------|\n| Soundness | 3.0 | 3.0 | **一致** |\n| Excitement | 3.5 | 2.5 | **分歧**：R1 给 layer selection finding 更高 novelty credit。我认为该 finding 虽有价值但过于 narrow（one specific metric bias），不构成方法论突破。 |\n| Reproducibility | 2.5 | 4.0 | **分歧**：R1 因数据 split 不一致和缺失 data tables 降分。我基于 hyperparameter 充分报告、bug disclosure 和 code release 承诺给高分。经交叉审查，我认为 R1 的 concern 有理——data split 不一致 (R1-W2) 确实影响 reproducibility，我调整为 **3.5/5**。 |\n| Overall | 3.0 | 3.0 | **一致**：Findings track |\n\n**Excitement 分歧说明**：R1 的 3.5 暗示论文接近 Main conference 下界。我维持 2.5，理由是：(1) 核心方法是标准 logistic regression，无方法创新；(2) layer selection bias finding 虽然对 probing community 有指导价值，但 scope 很窄——仅证明了一个 specific metric (bal_acc × crossing_rate) 在一个 specific task 上的 bias，泛化证据不足（我的 W2）；(3) R1-W4 进一步削弱了 \"four independent metrics converge\" 的 evidence strength。如果作者能在 rebuttal 中展示该 bias 在其他 probing tasks 上也成立，我愿意上调至 3.0。\n\n---\n\n## 新增观察（基于交叉审查）\n\nR1-N3 提醒我注意了一个我之前未重点分析的模式：**bib 中的 orphan entries 暴露了 \"知道但不做\" 的问题**。kornblith2019cka, bansal2021stitching 在 bib 中但不 cited，说明作者在文献调研阶段找到了这些更强的 representation comparison 方法，但既没有实验也没有在正文中讨论为什么不使用。这比单纯的遗漏更严重——它暗示作者可能意识到更强方法会弱化 \"transfer fails entirely\" 的 claim。\n\n结合我的 N2 (19 orphan entries)，bib 文件的状态整体反映了 rushed submission：文献被收集但未整合进正文。\n\n---\n\n## 总结\n\nR1 的 7 条 should-fix 中有多条提供了比我更具体的分析（特别是 W2 数据 split、W4 metric independence、W7 方法计数），补充了我的审查盲区。R1-N3 (cross-model transfer overclaim) 是我应该但未在 Round 1 重点关注的问题。\n\n两位 Reviewer 在 Overall Assessment (3.0, Findings) 和 Soundness (3.0) 上完全一致，分歧集中在 Excitement 和 Reproducibility 的子维度上。核心共识：这是一篇 well-executed empirical study，layer selection finding 有价值，但 novelty ceiling、sample size limitations、引用不足和多处 overclaim 限制了其 Main conference competitiveness。\n",
    "reviewer_id": "2",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-17T17:37:24.903550+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3817
}
```

</details>

---


### Assistant

_source line 256 · 2026-05-17T17:37:34.390054+00:00_

交叉回应已提交。对 R1 的 3 条 must-fix 和 7 条 should-fix 全部给出 [AGREE]，无 [REBUT]。

关键判断：
- **R1-N3 (cross-model transfer overclaim)** 是我 Round 1 的审查盲区，R1 分析正确——PCA 失败不能证明 "transfer fails entirely"，bib 中有 CKA/stitching 论文但未 cited 加重了问题
- **R1-W4 (metric independence)** 是有价值的新 concern——四个 "unbiased" metrics 数学上耦合，实际独立信号约 1.5-2 个
- Reproducibility 从 4.0 下调至 3.5（采纳 R1-W2 数据 split 不一致 concern）
- Overall 维持 3.0 (Findings)，两位 Reviewer 共识

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2"
}
```

</details>

---


## Round 9

## Round 9

80 recorded events


### User

_source line 257 · 2026-05-17T18:44:02.634038+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2（新颖性 + 论文完整性）

### Venue 信息
- **目标**: EMNLP 2026 (Findings track), 通过 ARR 提交
- **截止日期**: 2026-05-25
- **格式**: ACL 官方模板, 8页正文 + unlimited references, double-blind
- **模板**: `\usepackage[review]{acl}` (已确认)
- **匿名**: `Anonymous ARR Submission` (已确认)

### 论文路径
`projects/contrastive_trace_safety/docs/paper/main.tex`
各 section 在 `sections/` 子目录下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex
References: `references.bib` (31 entries)

### 论文概要
标题: "Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models"

核心: layer selection metric 偏差可以逆转 HS probe 结论。在4个推理模型上，corrected deep layers 显示 HS probe 一致优于 text probe (all-MiniLM-L6-v2 384d)。7种替代方法全部失败。

### 你的审查侧重（新颖性 + 论文完整性）
请重点评估以下方面：

1. **Novelty 和 Contribution 评估**
   - Layer selection sensitivity 作为 primary methodological contribution 的新颖性和影响力
   - 对 probing 社区的实际贡献程度——这是已知问题的系统验证还是真正的新发现？
   - "HS > text" 的结论在给定维度差距(4096-5120d vs 384d)的情况下是否 trivially expected？
   - 与 Findings track 定位是否匹配？

2. **Related Work 覆盖度**
   - 31 citations 是否足够？是否遗漏了重要的 2024-2026 年工作？
   - 用 WebSearch 验证以下领域的覆盖：
     a. Reasoning model safety (self-jailbreak, CoT manipulation)
     b. Hidden-state probing for safety
     c. Layer selection methodology in probing
     d. Change-point detection in neural activations
   - Positioning 是否清晰（本文 vs 现有工作的增量在哪里）？

3. **写作质量**
   - Abstract 是否满足 EMNLP 标准（150-250 words, 四个必答问题）？
   - Introduction 叙事线是否完整（5段结构）？
   - 全文主线统一性——Abstract/Intro/Method/Results/Discussion 是否讲同一个故事？
   - 检查 AI 写作痕迹：
     a. `grep "—"` 检查 em-dash 使用
     b. `grep " – "` 检查解释性 en-dash
     c. `-ing` 短语结尾
     d. 过度分段
     e. "Furthermore/Moreover/Additionally" 连续使用
     f. 用词黑名单("delve", "leverage", "utilize", "facilitate", "myriad", "plethora")
   - Discussion 和 Conclusion 是否有重复内容？

4. **Format 合规性**
   - 正文是否在 8 页限制内？
   - Limitations section 位置是否正确（conclusion 之后）？
   - Responsible NLP Research Checklist 是否完整？
   - 所有 cross-references (\cref) 是否有效？
   - 表格格式是否一致（booktabs）？
   - 图表 caption 是否自包含？

5. **Bug disclosure (Appendix F)**
   - 论文包含一个 bug disclosure (M002 QwQ-32B text probe initialization bug)
   - 评估这个 disclosure 的诚实度和对最终结论的影响
   - 是否有其他未声明的实验流程变更？

6. **Appendix 质量**
   - 附录是否在正文中都有引用？
   - 附录信息是否必要？有没有可以移到正文或删除的？
   - GRU per-seed results、BOCPD sweep、Transfer details 是否充分？

请产出标准审稿报告，包含 Summary, Strengths, Weaknesses, Questions, Missing References, Detailed Comments。

**评分参考（EMNLP 2026 ARR）**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit。半分制。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-17T18:44:10.369895+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-17T18:44:10.420727+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_2_f461d57a.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-17T18:44:12.948265+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-17T18:44:12.999013+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-17T18:44:15.560484+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-17T18:44:15.611220+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-17T18:44:22.083788+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-17T18:44:22.184978+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-17T18:44:28.431940+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-17T18:44:28.482649+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{subcaption}
11	\usepackage{xcolor}
12	\usepackage{colortbl}
13	\usepackage{hyperref}
14	\usepackage{cleveref}
15	
16	\title{Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models}
17	
18	\author{Anonymous ARR Submission}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{sections/abstract}
25	\end{abstract}
26	
27	\input{sections/introduction}
28	
29	\input{sections/related_work}
30	
31	\input{sections/method}
32	
33	\input{sections/experiments}
34	
35	\input{sections/discussion}
36	
37	\input{sections/conclusion}
38	
39	\input{sections/limitations}
40	
41	\bibliography{references}
42	
43	\input{sections/appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-17T18:44:31.345665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-17T18:44:31.797787+00:00_

1	Large Language Models (LLMs) with chain-of-thought (CoT) reasoning can self-jailbreak: their extended reasoning traces sometimes transition from safe deliberation to committed harmful generation. Detecting this \emph{safety commitment} in real time is essential for monitoring systems, yet no prior work has systematically compared hidden-state (HS) probes against text-based monitors for this task. We present the first cross-model evaluation of temporal probing for safety commitment detection across four reasoning models spanning two architectures (Llama, Qwen), two training methods (R1 distillation, STILL), and two scales (7--8B, 32B). Our primary methodological finding is that layer selection methodology can reverse a study's conclusions: the composite metric \texttt{bal\_acc $\times$ crossing\_rate} systematically selects shallow layers at 32B scale, entirely masking the hidden-state advantage. At correctly selected layers, all 12 Holm-Bonferroni-corrected hypothesis tests confirm significant HS superiority, with precision gains of +15 to +24 percentage points (pp) across all four models ($n{=}19$--$47$ test traces; $n{=}19$--$20$ at 32B scale). Temporal windowing universally improves both modalities, providing the most robust single default for safety monitoring. Seven alternative approaches (change-point detection, geometric distance, Representation Engineering, CCS, nonlinear probes, cross-model transfer via PCA projection and direct application) all fail, establishing clear boundaries of current methods. Control tasks confirm genuine safety-specific structure (selectivity 12.5--19.7pp above chance).
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-17T18:44:31.798160+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-17T18:44:32.250071+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Reasoning models such as DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq} scale inference-time computation through extended chains of thought (CoT), producing dozens of internal reasoning steps before generating a final response. This deliberative process interleaves safety-aware reasoning with content generation across many steps, and the very capacity for self-reflection introduces a failure mode absent from standard instruction-tuned models. Recent analyses have documented that reasoning models can ``self-jailbreak'': without any adversarial modification to the input prompt, the model's own CoT transitions from considering safety constraints to committing to produce harmful content~\cite{harmthoughts,selfjailbreak}. In a typical self-jailbreak trace, the model begins by acknowledging that a request may be harmful, engages in several steps of safety deliberation, and then gradually shifts toward compliance before abandoning safety reasoning entirely. We refer to the first reasoning step after which safety deliberation permanently ceases as the \textbf{Safety Commitment Point} (CP). Before the CP, the model is still weighing refusal; after it, harmful generation proceeds unchecked. This failure mode is qualitatively different from adversarial jailbreaks on standard LLMs: the harmful transition originates within the model's own reasoning rather than from a crafted input. Detecting this transition in real time is essential for monitoring systems that must intervene before harmful content reaches users, yet no existing detector was designed for this internal commitment process.
4	
5	Existing safety detectors target a fundamentally different problem. Hidden-state (HS) probing methods such as TrajGuard~\cite{trajguard} and SafeSwitch~\cite{safeswitch} monitor internal activations to classify adversarial inputs directed at instruction-tuned Large Language Models (LLMs), achieving above 95\% defense rates on standard b
…[truncated 6277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-17T18:44:32.300789+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-17T18:44:32.702759+00:00_

1	\section{Related Work}\label{sec:related-work}
2	
3	\paragraph{Safety in Reasoning Models.}
4	Reasoning models such as DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq} introduce a qualitatively new safety failure: the model's own chain of thought can transition from safety-aware deliberation to harmful content generation without any adversarial input modification~\cite{wang2025lrmsafety}. \citet{harmthoughts} document this self-jailbreak phenomenon and provide step-level annotations of reasoning traces, establishing that commitment to harmful output emerges gradually across multiple reasoning steps. \citet{selfjailbreak} characterize the statistical properties of self-jailbreak, showing that longer reasoning chains increase circumvention probability, but do not propose a deployable detection mechanism. H-CoT~\cite{hcot2025} demonstrates that reasoning chains can be externally hijacked to bypass safety constraints, complementing the self-jailbreak phenomenon where harmful transitions originate from the model's own deliberation. The reliability of reasoning traces is further complicated by unfaithful reasoning~\cite{chen2025unfaithful}, where models' stated reasoning does not reflect their actual decision process, motivating hidden-state monitoring that bypasses text entirely. On the mitigation side, SafeThink~\cite{safethink} steers early reasoning steps toward safety through text-level CoT monitoring, while SafeRemind~\cite{saferemind} inserts entropy-triggered safety reminders into the reasoning stream. \citet{ahrend2026safer_traces} measure and mitigate information leakage in reasoning traces, addressing a complementary safety dimension. Concurrent work traces refusal dynamics in standard language models~\cite{hu2026refusal_dynamics}; our work differs in focusing on the self-jailbreak commitment process specific to reasoning models, with an emphasis on the methodological finding that layer selection metrics can reverse probe-based conclusions. These works collec
…[truncated 5627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-17T18:44:32.803559+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-17T18:44:33.657321+00:00_

1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	\subsection{Safety Commitment Point}
5	\label{sec:commitment-point}
6	
7	When a reasoning model is jailbroken, its chain-of-thought (CoT) transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety reasoning permanently ceases. Formally, given a trace of $T$ reasoning steps, the CP is the earliest step $t^*$ such that no step $t > t^*$ contains safety-relevant deliberation. Steps before CP are \emph{pre-commitment} (the model is still considering refusal); steps at or after CP are \emph{post-commitment} (the model has irrevocably committed to harmful output).
8	
9	We operationalize this definition on HarmThoughts~\citep{harmthoughts} traces, which provide step-level annotations of safety reasoning. Each step receives a binary label: pre-CP ($y_t = 0$ for $t < t^*$) or post-CP ($y_t = 1$ for $t \geq t^*$). The detection task is binary classification at each step, producing a score $s_t \in [0, 1]$ that estimates the probability that the model has passed its commitment point by step $t$.
10	
11	We study four reasoning models spanning two architectures (Llama and Qwen) and two parameter scales (7--8B and 32B), summarized in \cref{tab:models}.
12	
13	\begin{table}[t]
14	\centering
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{lccccc}
17	\toprule
18	\textbf{Model} & \textbf{Arch.} & \textbf{Params} & \textbf{Layers} & \textbf{Hidden} & \textbf{$n$ (total\,/\,test)} \\
19	\midrule
20	R1-8B & Llama & 8B & 32 & 4096 & 209\,/\,43 \\
21	OT-7B & Qwen & 7B & 28 & 3584 & 228\,/\,47 \\
22	R1-32B & Qwen & 32B & 64 & 5120 & 100\,/\,20 \\
23	QwQ-32B & Qwen & 32B & 64 & 5120 & 95\,/\,19 \\
24	\bottomrule
25	\end{tabular}}
26	\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep{deepseekr1}; QwQ-32B~\citep{qwq} is a native reasoning model; OT-7B~\citep{openthinker} is trained w
…[truncated 12058 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-17T18:44:33.808432+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-17T18:44:34.260987+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	We evaluate temporal probes across four reasoning models (\cref{tab:models}), comparing hidden-state (HS) and text modalities under different layer selection criteria. Our experiments address three questions: (1)~Does the layer selection metric determine whether HS probes appear effective? (2)~Do HS probes outperform text probes at correctly selected layers? (3)~Which alternative detection methods fail, and why?
4	
5	\subsection{Experimental Setup}\label{sec:setup}
6	
7	\paragraph{Models and data.} We study four models spanning two architectures and two parameter scales: R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (Qwen-7B, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level commitment point (CP) annotations. We use a 60/20/20 train/validation/test split across all models (\cref{tab:models}).
8	
9	\paragraph{Training and evaluation.} All probes use L2-regularized logistic regression with balanced class weights. For each model, we select the temporal window $W$ on the validation set from $W \in \{1, 3, 5, 10, 15, 20, 25\}$. HS probes extract last-token hidden states from a selected transformer layer; text probes encode each reasoning step with all-MiniLM-L6-v2 (384 dimensions). Detection requires $K{=}5$ consecutive threshold crossings. Modality comparisons use a two-sided null-centered bootstrap test (1000 resamples) with Holm-Bonferroni step-down correction across 12 tests (3 metrics $\times$ 4 models, $\alpha{=}0.05$).
10	
11	\paragraph{Layer selection.} We evaluate five layer selection metrics per model (\cref{sec:layer-sensitivity}). The biased composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers for 32B models because representational volatility at early layers inflates the crossing rate component. Four unbiased metrics (pure b
…[truncated 16986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-17T18:44:34.311767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-17T18:44:34.613402+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Layer selection as researcher degree of freedom.}
4	Layer selection is an underexamined methodological choice in the probing literature that can silently determine a study's conclusions. Our five-metric ablation (\cref{sec:layer-results}) demonstrates that a single metric component, the crossing rate, reverses the central finding of an HS vs.\ text comparison: at biased layers, only 5 of 12 tests survive Holm-Bonferroni correction, producing an apparent scale-dependent modality effect; at corrected layers, all 12 tests pass. The mechanism is general: crossing rate rewards representational volatility at shallow layers independently of discriminative power, and any composite metric that incorporates threshold-crossing frequency is susceptible to the same bias mechanism, whose practical impact depends on the specific task and model depth. This bias is not specific to safety probing. Any threshold-based detection study that uses crossing rate as a layer selection criterion, whether for sentiment, factuality, or toxicity, could produce analogous reversals. We recommend that probing studies report results under at least two complementary layer selection criteria, and that five-metric ablations (or at minimum, results at multiple candidate layers spanning shallow, middle, and deep positions) become standard practice. The cost is modest: evaluating five metrics across all layers adds minutes to an experiment that takes hours. The alternative is that conclusions about representational structure reflect layer selection methodology rather than the phenomenon under study. The control task provides independent corroboration: R1-32B selectivity increases from 7.5pp at the biased layer (L10) to 19.7pp at the corrected layer (L63), confirming that the biased metric selected layers where positional features dominate over genuine safety structure.
5	
6	\paragraph{Temporal context and modality choice.}
7	Information-theoreti
…[truncated 4454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-17T18:44:34.613975+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-17T18:44:35.066233+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first systematic cross-model evaluation of safety commitment detection across four reasoning models spanning two architectures, two training methods, and two scales.
4	The central methodological finding is that layer selection metric bias can reverse a study's main conclusion: a composite metric incorporating crossing rate systematically selects shallow layers at 32B scale, entirely masking the hidden-state advantage, while four complementary metrics converge on deep layers (94--98\% depth).
5	At correctly selected layers, all 12 Holm-Bonferroni-corrected tests confirm significant HS superiority (precision +15.4 to +23.6pp), and seven alternative methods fail, though practical detection profiles diverge by model (R1-32B provides early warning at narrow coverage; QwQ-32B provides broad significance with poor timing).
6	Closing the 85.5\% oracle gap between passive monitoring and the theoretical detection frontier will require causal intervention techniques such as activation patching, extension to multilingual and multi-turn settings, evaluation at intermediate scales (13B, 70B), and exploration of stronger cross-model alignment methods beyond the PCA-based and direct transfer approaches tested here.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-17T18:44:35.066578+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-17T18:44:35.217328+00:00_

1	\section{Limitations}\label{sec:limitations}
2	
3	\paragraph{R1-32B statistical narrowness.}
4	Only $W{=}1$ passes Bonferroni correction for R1-32B, with only 25\% trace coverage (5 of 20 test traces detected). The dimensionality constraint of $51200 \times W$ features for $n{=}20$ traces prevents reliable evaluation at larger window sizes. Whether collecting more training traces would resolve this statistical limitation remains unknown.
5	
6	\paragraph{QwQ-32B timing limitation.}
7	On QwQ-32B, hidden-state probes achieve higher accuracy than text probes but detect commitment later: HS lead time is negative ($-1.2$ to $+1.9$ steps) compared to text lead time of $3.7$--$12.3$ steps. A position-only baseline achieves comparable balanced accuracy (0.746 vs.\ HS 0.740), suggesting that much of the detection signal on this model is positional rather than representational. The practical value of marginally higher accuracy with later detection depends on the deployment context.
8	
9	\paragraph{High safe-trace false positive rate.}
10	All probing methods produce high false positive rates on safe traces at standard operating thresholds (39--52\% across methods on R1-8B). Current probes characterize the commitment phenomenon as a research tool rather than constitute production-ready detectors. The 85.5\% oracle gap between passive monitoring and active intervention shows that early detection via passive probing captures only a fraction of the theoretically available safety signal.
11	
12	\paragraph{Scale and architecture coverage.}
13	We evaluate 4 models spanning 2 architectures (Qwen-2.5, LLaMA-3.1) and 2 parameter scales (7--8B, 32B). Intermediate scales (13B, 70B) that would test whether the observed layer-selection pattern interpolates smoothly are missing. We also lack evaluation on proprietary reasoning models (e.g., o1, o3), where chain-of-thought structure may differ substantially.
14	
15	\paragraph{Text encoder as baseline.}
16	Text probes use a single 384-dimensi
…[truncated 1021 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-17T18:44:35.568876+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-17T18:44:36.071240+00:00_

1	\appendix
2	
3	\section{Responsible NLP Research Checklist}
4	\label{app:checklist}
5	
6	We address the ARR Responsible NLP Research requirements below.
7	
8	\begin{itemize}
9	    \item \textbf{Limitations discussed:} Yes (\cref{sec:limitations}).
10	    \item \textbf{Potential risks:} This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark.
11	    \item \textbf{Computational budget:} Our experiments involve 4 models with 209, 228, 100, and 95 traces respectively (632 total), using linear probes and single-layer GRUs. Total compute is minimal (under 4 GPU-hours on a single RTX A6000). No large-scale pretraining or finetuning was performed.
12	    \item \textbf{Data:} We use HarmThoughts, a publicly available benchmark with step-level safety annotations. No new data collection was performed.
13	    \item \textbf{Human subjects:} No human subjects research was conducted.
14	    \item \textbf{Reproducibility:} All hyperparameters are reported in \cref{app:gru_details,app:bocpd_config}. Code and corrected data will be released upon publication.
15	\end{itemize}
16	
17	
18	\section{Layer Sweep Results}
19	\label{app:layer_sweep}
20	
21	For each model, we sweep all transformer layers and evaluate five candidate selection metrics: (1)~balanced accuracy $\times$ crossing rate (the biased composite), (2)~pure balanced accuracy, (3)~precision, (4)~inverse pre-CP FPR, and (5)~an additive composite. The biased composite systematically selects shallow layers for 32B models because early-layer representations exhibit higher crossing rates (more frequent threshold crossings) regardless of discriminative power. The four unbiased metrics converge on deep layers for all models.
22	
23	\paragraph{Selected layers.} R1-8B: all five metrics agree on layer~14 (44\% depth). OT-7B: biased m
…[truncated 33122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-17T18:44:36.071644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-17T18:44:37.024858+00:00_

1	@article{trajguard,
2	  title={TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense},
3	  author={Liu, Cheng and Liu, Xiaolei and Li, Xingyu and Xin, Bangzhou and Ding, Kangyi},
4	  journal={arXiv preprint arXiv:2604.07727},
5	  year={2026},
6	  url={https://arxiv.org/abs/2604.07727}
7	}
8	
9	@inproceedings{safeswitch,
10	  title={SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals},
11	  author={Han, Peixuan and Qian, Cheng and Chen, Xiusi and Zhang, Yuji and Ji, Heng and Zhang, Denghui},
12	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
13	  year={2025},
14	  url={https://arxiv.org/abs/2502.01042}
15	}
16	
17	@inproceedings{siren,
18	  title={LLM Safety From Within: Detecting Harmful Content with Internal Representations},
19	  author={Jiao, Difan and Liu, Yilun and Yuan, Ye and Tang, Zhenwei and Du, Linfeng and Wu, Haolun and Anderson, Ashton},
20	  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
21	  year={2026},
22	  url={https://arxiv.org/abs/2604.18519}
23	}
24	
25	@article{saferemind,
26	  title={How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs},
27	  author={Kim, Su-Hyeon and Jin, Hyundong and Lee, Yejin and Han, Yo-Sub},
28	  journal={arXiv preprint arXiv:2601.03662},
29	  year={2026},
30	  url={https://arxiv.org/abs/2601.03662}
31	}
32	
33	@article{safethink,
34	  title={Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away},
35	  author={Ghosal, Soumya Suvra and Chakraborty, Souradip and Singh, Vaibhav and Huang, Furong and Manocha, Dinesh and Bedi, Amrit Singh},
36	  journal={arXiv preprint arXiv:2602.11096},
37	  year={2026},
38	  url={https://arxiv.org/abs/2602.11096}
39	}
40	
41	@article{selfjailbreak,
42	  title={Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training},
43	
…[truncated 9793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-17T18:44:37.025240+00:00_

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
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 289 · 2026-05-17T18:44:37.877400+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 290 · 2026-05-17T18:44:45.664848+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's information about ACL ARR 2025-2026 reviewer guidelines, review form, and scoring criteria:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text 
…[truncated 1391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8639
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-17T18:45:25.047958+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 31, \"total_citations\": 62, \"unique_cited_keys\": 31, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 26, \"online_not_found\": 5, \"online_mismatch\": 0}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"trajguard\", \"type\": \"article\", \"title\": \"TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense\", \"authors\": \"Liu, Cheng and Liu, Xiaolei and Li, Xingyu and Xin, Bangzhou and Ding, Kangyi\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.07727\"}, {\"key\": \"safeswitch\", \"type\": \"inproceedings\", \"title\": \"SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals\", \"authors\": \"Han, Peixuan and Qian, Cheng and Chen, Xiusi and Zhang, Yuji and Ji, Heng and Zh...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2025\"}, {\"key\": \"siren\", \"type\": \"inproceedings\", \"title\": \"LLM Safety From Within: Detecting Harmful Content with Internal Representations\", \"authors\": \"Jiao, Difan and Liu, Yilun and Yuan, Ye and Tang, Zhenwei and Du, Linfeng and Wu...\", \"year\": \"2026\", \"venue\": \"Proceedings of the 64th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"saferemind\", \"type\": \"article\", \"title\": \"How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs\", \"authors\": \"Kim, Su-Hyeon and Jin, Hyundong and Lee, Yejin and Han, Yo-Sub\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2601.03662\"}, {\"key\": \"safethink\", \"type\": \"article\", \"title\": \"Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away\", \"authors\": \"Ghosal, Soumya Suvra and Chakraborty, Souradip and Singh, Vaibhav and Huang, Fur...\", \"year\": \"202
…[truncated 25378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 47170
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-17T18:45:31.772267+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. I need the exact dimensions (soundness, excitement, overall assessment, etc.), the scoring scales for each, and descriptions of each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. I need the exact dimensions (soundness, excitement, overall assessment, etc.), the scoring scales for each, and descriptions of each score level."
  }
}
```

</details>

---


### Tool call

_source line 293 · 2026-05-17T18:45:34.080477+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 294 · 2026-05-17T18:45:34.532629+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 295 · 2026-05-17T18:45:35.034969+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 296 · 2026-05-17T18:45:35.486996+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 297 · 2026-05-17T18:45:35.989238+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 298 · 2026-05-17T18:45:36.441374+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:7:\paragraph{Models and data.} We study four models spanning two architectures and two parameter scales: R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (Qwen-7B, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level commitment point (CP) annotations. We use a 60/20/20 train/validation/test split across all models (\cref{tab:models}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:109:The complementary profiles suggest that the practical value of HS monitoring depends on model-specific detection requirements. Early warning applications favor R1-32B's high lead time despite narrow coverage. Broad reliable detection applications favor QwQ-32B's robust significance despite poor timing. These divergent patterns within the same architecture underscore that per-model validation is essential.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:113:\cref{tab:negative} summarizes seven alternative detection approaches that fail to match supervised temporal probing. The failures span change-point detection, geometric methods, direction-based probing, nonlinear models, semi-supervised learning, and cross-model transfer.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex:6:Closing the 85.5\% oracle gap between passive monitoring and the
…[truncated 4832 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 299 · 2026-05-17T18:45:36.943725+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 300 · 2026-05-17T18:45:37.847535+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 301 · 2026-05-17T18:45:38.349856+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "delve|leverage|utilize|facilitate|myriad|plethora",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "delve|leverage|utilize|facilitate|myriad|plethora",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 302 · 2026-05-17T18:45:38.801937+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-17T18:45:50.108694+00:00_

# ACL Rolling Review Form: Complete Criteria and Scales

## Primary Scoring Dimensions

### 1. Reviewer Confidence
**Scale: 1-5**
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure" but some details might be missed
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation" but likely missed details
- **1**: "Not my area, or paper is very hard to understand"

### 2. Soundness
**Scale: 1-5 (with .5 increments)**
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all claims"
- **3**: "Acceptable: sufficient support for main claims"
- **2**: "Poor: main claims not sufficiently supported"
- **1**: "Major Issues: not sufficiently thorough to warrant publication"

### 3. Excitement
**Scale: 1-5 (with .5 increments)**
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points"
- **2**: "Potentially Interesting: does not resonate with me"
- **1**: "Not Exciting: does not resonate with me, nor others"

### 4. Overall Assessment
**Scale: 1-5 (with .5 increments)**
- **5**: "Consider for Award" (top 2.5% papers)
- **4**: "Conference: could be accepted"
- **3**: "Findings: could be accepted to Findings track"
- **2**: "Resubmit next cycle"
- **1**: "Do not resubmit"

## Secondary Evaluation Dimensions

### 5. Reproducibility
**Scale: 1-5**
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: Cannot reproduce results

### 6. Datasets Value
**Scale: 1-5**
- **5**: "Enabling" for research decisions
- **4**: "Useful" for ongoing work
- **3**: "Potentially useful"
- **2**: "Documentary" for replication only
- **1**: No usable datasets

### 
…[truncated 543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 18336
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-17T18:45:50.259729+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search missing related work",
  "prompt": "I'm reviewing a paper on \"Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models\" for EMNLP 2026. I need to check whether important recent works (2024-2026) are missing from the paper's references. The paper currently cites 31 references.\n\nPlease search the web for recent works in these areas and report titles+authors of important papers that might be missing:\n\n1. Reasoning model safety / self-jailbreak / CoT manipulation (2024-2026) - The paper already cites: harmthoughts, selfjailbreak, H-CoT, SafeThink, SafeRemind, SafeDream, chen2025unfaithful, ahrend2026safer_traces, hu2026refusal_dynamics, wang2025lrmsafety\n\n2. Hidden-state probing for safety detection (2024-2026) - Already cites: TrajGuard, SafeSwitch, SIREN, zhou2024alignment, arditi2024refusal, zhao2025harmfulness\n\n3. Layer selection methodology in probing / probing methodology (2024-2026) - Already cites: belinkov2019analysis, belinkov2022probing, hewitt2019control, tenney2019bert, alain2017understanding, conneau2018probing\n\n4. Change-point detection in neural activations - Already cites: adams2007bayesian (BOCPD), burns2023discovering (CCS), zou2023representation (RepE)\n\nSearch for: \"reasoning model safety jailbreak 2025 2026\", \"hidden state probing safety LLM 2025 2026\", \"layer selection probing methodology transformer 2025\", \"activation probing layer selection sensitivity\". Report which important papers are NOT in the above lists."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Search missing related work",
    "prompt": "I'm reviewing a paper on \"Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models\" for EMNLP 2026. I need to check whether important recent works (2024-2026) are missing from the paper's references. The paper currently cites 31 references.\n\nPlease search the web for recent works in these areas and report titles+authors of important papers that might be missing:\n\n1. Reasoning model safety / self-jailbreak / CoT manipulation (2024-2026) - The paper already cites: harmthoughts, selfjailbreak, H-CoT, SafeThink, SafeRemind, SafeDream, chen2025unfaithful, ahrend2026safer_traces, hu2026refusal_dynamics, wang2025lrmsafety\n\n2. Hidden-state probing for safety detection (2024-2026) - Already cites: TrajGuard, SafeSwitch, SIREN, zhou2024alignment, arditi2024refusal, zhao2025harmfulness\n\n3. Layer selection methodology in probing / probing methodology (2024-2026) - Already cites: belinkov2019analysis, belinkov2022probing, hewitt2019control, tenney2019bert, alain2017understanding, conneau2018probing\n\n4. Change-point detection in neural activations - Already cites: adams2007bayesian (BOCPD), burns2023discovering (CCS), zou2023representation (RepE)\n\nSearch for: \"reasoning model safety jailbreak 2025 2026\", \"hidden state probing safety LLM 2025 2026\", \"layer selection probing methodology transformer 2025\", \"activation probing layer selection sensitivity\". Report which important papers are NOT in the above lists."
  }
}
```

</details>

---


### Tool call

_source line 305 · 2026-05-17T18:45:51.514990+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "reasoning model safety jailbreak 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "reasoning model safety jailbreak 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-17T18:45:51.716131+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "hidden state probing safety LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "hidden state probing safety LLM 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 307 · 2026-05-17T18:45:51.716481+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "layer selection probing methodology transformer 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "layer selection probing methodology transformer 2025"
  }
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-17T18:45:51.917637+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "activation probing layer selection sensitivity neural networks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "activation probing layer selection sensitivity neural networks"
  }
}
```

</details>

---


### Tool call

_source line 309 · 2026-05-17T18:45:52.118804+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoT manipulation reasoning models safety 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoT manipulation reasoning models safety 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-17T18:45:52.370179+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "probing refusal mechanisms language models 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "probing refusal mechanisms language models 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-17T18:45:59.043256+00:00_

Web search results for query: "layer selection probing methodology transformer 2025"

Links: [{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"Probing Layers: Where Transformers Encode Linguistic Structure - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/probing-layers"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/d9e42b4d7163931f3689d6d6fbaa11d0-Paper-Conference.pdf"},{"title":"A lightweight deep learning framework for transformer fault diagnosis in smart grids using multiple scale CNN features | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-96290-2"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2412.04703"},{"title":"Article Not peer-reviewed version Locate, Steer, and Improve: A Practical","url":"https://www.preprints.org/frontend/manuscript/0461f28c43bc6be17ca9822186e8ceb0/download_pub"},{"title":"Adaptive layer and token selection for efficient fine-tuning of vision transformers - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0925231225018880"},{"title":"Transformers without Normalization Jiachen Zhu1,2 Xinlei Chen1 Kaiming He3","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhu_Transformers_without_Normalization_CVPR_2025_paper.pdf"},{"title":"Exploring Pooling Strategies and Layer Aggregation in Transformer Encoders for Text Classification | OpenReview","url":"https://openreview.net/forum?id=JPjj4GClBr"},{"title":"Circuits Updates - July 2025","url":"https://transformer-circuits.pub/2025/july-update/index.html"}]

I found several relevant results on layer selection and probing methodologies in transformers from 2025. Here's a summary of the key findings:

## Recent Research on Layer Selection and Probin
…[truncated 1701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7326
}
```

</details>

---


### Tool result

_source line 312 · 2026-05-17T18:45:59.144122+00:00_

Web search results for query: "activation probing layer selection sensitivity neural networks"

Links: [{"title":"Application of Sensitivity Analysis Methods for Studying Neural Network Models","url":"https://arxiv.org/html/2504.15100v1"},{"title":"Exploring specialization and sensitivity of convolutional neural networks in the context of simultaneous image augmentations","url":"https://arxiv.org/html/2503.03283v1"},{"title":"Stochastic Selection of Activation Layers for Convolutional Neural Networks - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/32183334/"},{"title":"Understanding intermediate layers using linear classiﬁer probes Guillaume Alain","url":"https://arxiv.org/pdf/1610.01644"},{"title":"Sensitivity and Generalization in Neural Networks","url":"https://arxiv.org/pdf/1802.08760"},{"title":"A novel sensitivity-based method for feature selection | Journal of Big Data | Full Text","url":"https://journalofbigdata.springeropen.com/articles/10.1186/s40537-021-00515-w"},{"title":"Interpretability of neural network using layer conductance analysis for the concept detection | Journal of Engineering and Applied Science | Full Text","url":"https://jeas.springeropen.com/articles/10.1186/s44147-025-00719-4"},{"title":"Sensitivity Analysis of Neural Networks • NeuralSens","url":"https://jaipizgon.github.io/NeuralSens/"},{"title":"Stochastic Selection of Activation Layers for Convolutional Neural Networks - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7147370/"},{"title":"Computation of CNN’s Sensitivity to Input Perturbation | Neural Processing Letters | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11063-020-10420-7"}]

Based on the web search results, here's what I found on activation probing, layer selection, and sensitivity in neural networks:

## Activation Probing and Layer Analysis

Researchers monitor features at every layer of a model and measure how suitable they are for classification, which helps better understand the role
…[truncated 1446 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7226
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-17T18:45:59.295356+00:00_

Web search results for query: "CoT manipulation reasoning models safety 2024 2025"

Links: [{"title":"Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety","url":"https://tomekkorbak.com/cot-monitorability-is-a-fragile-opportunity/cot_monitoring.pdf"},{"title":"Can Reasoning Models Obfuscate Reasoning? Stress-Testing Chain-of-Thought Monitorability","url":"https://arxiv.org/html/2510.19851v1"},{"title":"Monitoring Reasoning Models for Misbehavior and the Risks of","url":"https://cdn.openai.com/pdf/34f2ada6-870f-4c26-9790-fd8def56387f/CoT_Monitoring.pdf"},{"title":"Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety","url":"https://arxiv.org/html/2507.11473v1"},{"title":"[2507.11473] Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety","url":"https://arxiv.org/abs/2507.11473"},{"title":"Reasoning Models Struggle to Control their Chains of Thought Chen Yueh-Han∗","url":"https://cdn.openai.com/pdf/a21c39c1-fa07-41db-9078-973a12620117/cot_controllability.pdf"},{"title":"INVESTIGATING COT MONITORABILITY IN LARGE ...","url":"https://openreview.net/pdf/3236ca18d010cce2d999055eb0e1eeb5df1624cb.pdf"},{"title":"Safety Understanding and Reasoning Enhancement for ...","url":"https://aclanthology.org/2025.emnlp-main.384.pdf"},{"title":"Reasoning Models Don’t Always Say What They Think Yanda Chen Joe Benton","url":"https://assets.anthropic.com/m/71876fabef0f0ed4/original/reasoning_models_paper.pdf"},{"title":"Chain of Thought Monitorability - Frontier Model Forum","url":"https://www.frontiermodelforum.org/issue-briefs/chain-of-thought-monitorability/"}]

Based on the search results, here's what recent research reveals about Chain-of-Thought (CoT) manipulation and reasoning model safety in 2024-2025:

## Key Safety Concerns

CoT can be unfaithful, especially when models have incentives to hide their reasoning. When integrating CoT monitors into reinforcement learning rewards with too much optimization, agent
…[truncated 1248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7176
}
```

</details>

---


### Tool result

_source line 314 · 2026-05-17T18:45:59.396232+00:00_

Web search results for query: "probing refusal mechanisms language models 2024 2025"

Links: [{"title":"[2406.11717] Refusal in Language Models Is Mediated by a Single Direction","url":"https://arxiv.org/abs/2406.11717"},{"title":"Refusal in Language Models Is Mediated by a Single Direction Andy Arditi∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/f545448535dfde4f9786555403ab7c49-Paper-Conference.pdf"},{"title":"ICML Poster The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence","url":"https://icml.cc/virtual/2025/poster/46298"},{"title":"The Geometry of Refusal in Large Language Models:","url":"https://arxiv.org/pdf/2502.17420"},{"title":"Beyond I’m Sorry, I Can’t: Dissecting Large-Language-Model Refusal","url":"https://arxiv.org/html/2509.09708v1"},{"title":"There Is More to Refusal in Large Language Models than a Single Direction","url":"https://www.arxiv.org/pdf/2602.02132"},{"title":"Refusal in Language Models Is Mediated by a Single Direction - MATS Research","url":"https://www.matsprogram.org/research/refusal-in-language-models-is-mediated-by-a-single-direction"},{"title":"Refusal in Language Models Is Mediated by a Single Direction","url":"https://www.researchgate.net/publication/381510906_Refusal_in_Language_Models_Is_Mediated_by_a_Single_Direction"},{"title":"Understanding Refusal in Language Models with Sparse ...","url":"https://aclanthology.org/2025.findings-emnlp.338.pdf"},{"title":"There Is More to Refusal in Large Language Models than a Single Direction","url":"https://arxiv.org/html/2602.02132v1"}]

Based on the search results, here's what recent research has found about probing refusal mechanisms in language models:

## Key Research Findings (2024-2025)

**Single Direction vs. Multi-Directional Mechanisms**

Research in 2024 showed that refusal is mediated by a one-dimensional subspace across 13 popular open-source chat models up to 72B parameters in size. This work found a single dir
…[truncated 1360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7026
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-17T18:46:00.601741+00:00_

Web search results for query: "reasoning model safety jailbreak 2025 2026"

Links: [{"title":"Large reasoning models are autonomous jailbreak agents | Nature Communications","url":"https://www.nature.com/articles/s41467-026-69010-1"},{"title":"LLM Jailbreaks 2024–2026: Techniques, Risks & Defense Strategies","url":"https://startup-house.com/blog/llm-jailbreak-techniques"},{"title":"Large reasoning models are autonomous jailbreak agents - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12881495/"},{"title":"AI's ability to 'think' makes it more vulnerable to new jailbreak attacks, new research suggests | Fortune","url":"https://fortune.com/2025/11/07/ai-reasoning-models-more-vulnerable-jailbreak-attacks-study/"},{"title":"[2501.19180] Enhancing Model Defense Against Jailbreaks with Proactive Safety Reasoning","url":"https://arxiv.org/abs/2501.19180"},{"title":"[2509.11629] Reasoned Safety Alignment: Ensuring Jailbreak Defense via Answer-Then-Check","url":"https://arxiv.org/abs/2509.11629"},{"title":"When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models","url":"https://arxiv.org/html/2510.21285v4"},{"title":"TeleAI-Safety: A comprehensive LLM jailbreaking benchmark towards attacks,","url":"https://arxiv.org/pdf/2512.05485"},{"title":"Reasoned Safety Alignment: Ensuring Jailbreak Defense via Answer-Then-Check | OpenReview","url":"https://openreview.net/forum?id=DK6AToxJNo"},{"title":"[2510.21285] When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models","url":"https://arxiv.org/abs/2510.21285"}]

Based on the search results, here's what recent research shows about reasoning model safety and jailbreak vulnerabilities in 2025-2026:

## Key Findings on Reasoning Model Vulnerabilities

### Autonomous Jailbreak Attacks

Large reasoning models can autonomously plan and execute persuasive multi-turn attacks to systematically bypass safety mechanisms in widely used AI systems. The p
…[truncated 1696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9086
}
```

</details>

---


### Tool result

_source line 316 · 2026-05-17T18:46:04.517394+00:00_

Web search results for query: "hidden state probing safety LLM 2025 2026"

Links: [{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"Mitigating Fine-tuning Risks in LLMs via Safety-Aware Probing Optimization","url":"https://openreview.net/pdf/d3af68681e03b57216283500b00c33f907c7c4e4.pdf"},{"title":"Monitoring Latent World States in Language Models with Propositional Probes | OpenReview","url":"https://openreview.net/forum?id=0yvZm2AjUr"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs | medRxiv","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full"},{"title":"Mitigating Fine-tuning Risks in LLMs via Safety-Aware Probing Optimization","url":"https://arxiv.org/pdf/2505.16737"},{"title":"Probing LLM Hidden States","url":"https://apxml.com/courses/how-to-build-a-large-language-model/chapter-23-analyzing-model-behavior/probing-internal-representations"},{"title":"The Hidden Dimensions of LLM Alignment:","url":"https://arxiv.org/pdf/2502.09674"},{"title":"UNCERTAINTY-AWARE LLM PROBING","url":"https://openreview.net/pdf/63e1228ab913455a780def6612d437e0de89555a.pdf"},{"title":"Towards Fully Exploiting LLM Internal States to Enhance ...","url":"https://aclanthology.org/2025.acl-long.1184.pdf"},{"title":"New Technique Shows Gaps in LLM Safety Screening","url":"https://www.bankinfosecurity.com/new-technique-shows-gaps-in-llm-safety-screening-a-30060"}]

I found several recent papers and research on hidden state probing and LLM safety from 2025-2026. Here's what I discovered:

## Key Research Areas

**PING Framework (2025)**: PING (Probing INternal states of Generative models) is an open-source framework that trains lightweight probes on frozen, HuggingFace-compatible transformers to deliver structured predictions with minimal compute overhead. On an LLM that has been explicitly safety-tuned
…[truncated 1373 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 12801
}
```

</details>

---


### Tool call

_source line 317 · 2026-05-17T18:46:06.324901+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "mechanistic interpretability refusal safety neurons 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "mechanistic interpretability refusal safety neurons 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-17T18:46:06.776865+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "training-induced alignment safety features LLM representations 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "training-induced alignment safety features LLM representations 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 319 · 2026-05-17T18:46:06.977987+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "sparse autoencoders LLM safety interpretability 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "sparse autoencoders LLM safety interpretability 2025"
  }
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-17T18:46:07.379924+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "multimodal layer dependency probing transformers 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "multimodal layer dependency probing transformers 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 321 · 2026-05-17T18:46:07.430737+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "representational collapse layer transformers safety alignment 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "representational collapse layer transformers safety alignment 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 322 · 2026-05-17T18:46:14.456255+00:00_

Web search results for query: "sparse autoencoders LLM safety interpretability 2025"

Links: [{"title":"[2510.02917] Mechanistic Interpretability of Code Correctness in LLMs via Sparse Autoencoders","url":"https://arxiv.org/abs/2510.02917"},{"title":"[2503.05613] A Survey on Sparse Autoencoders: Interpreting the Internal Mechanisms of Large Language Models","url":"https://arxiv.org/abs/2503.05613"},{"title":"GSAE: Graph-Regularized Sparse Autoencoders for Robust LLM Safety Steering","url":"https://www.arxiv.org/pdf/2512.06655"},{"title":"A Survey on Sparse Autoencoders: Interpreting the Internal Mechanisms of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.89/"},{"title":"NeurIPS Poster Sparse Autoencoders Learn Monosemantic Features in Vision-Language Models","url":"https://neurips.cc/virtual/2025/poster/119210"},{"title":"Mechanistic Interpretability of Code Correctness in LLMs via Sparse Autoencoders | OpenReview","url":"https://openreview.net/forum?id=FyQPpkASsV"},{"title":"On the Identifiability of Concepts from Large Language Model Activations | OpenReview","url":"https://openreview.net/forum?id=dGQubVJQx6"},{"title":"Mechanistic Interpretability of Code Correctness in LLMs via Sparse Autoencoders","url":"https://arxiv.org/html/2510.02917v1"},{"title":"Evaluation of Sparse Autoencoder-based Refusal Features in LLMs","url":"https://repositum.tuwien.at/bitstream/20.500.12708/220332/1/Kerl%20Tilman%20-%202025%20-%20Evaluation%20of%20Sparse%20Autoencoder-based%20Refusal%20Features%20in...pdf"},{"title":"Transcoders Beat Sparse Autoencoders for Interpretability","url":"https://arxiv.org/html/2501.18823v1"}]

I've found several relevant research papers and developments on sparse autoencoders (SAEs) for LLM safety and interpretability from 2025. Here's what I found:

## Key Research Areas

**Mechanistic Interpretability Framework**

Sparse Autoencoders (SAEs) have emerged as a promising method due to their ability to disenta
…[truncated 1486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7478
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-17T18:46:14.758998+00:00_

Web search results for query: "multimodal layer dependency probing transformers 2024 2025"

Links: [{"title":"[2510.21518] Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/abs/2510.21518"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/html/2510.21518"},{"title":"979-8-3503-4125-6/23/$31.00 ©2024 IEEE IEEE SPMB 2024 December 2, 20234","url":"https://isip.piconepress.com/conferences/ieee_spmb/2024/papers/l02_01.pdf"},{"title":"Transformer Models Overview","url":"https://www.emergentmind.com/topics/transformer-based-models"},{"title":"Multimodal transformers: AI foundation models, Part 1 - The SAS Data Science Blog","url":"https://blogs.sas.com/content/subconsciousmusings/2025/03/21/multimodal-transformers-ai-foundation-models-part-1/"},{"title":"Multi-modal Transformers - Yan Lin's Blog","url":"https://blog.yanlincs.com/ml-tech/multi-modal-transformer/"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf"},{"title":"Multimodal Diffusion Transformer","url":"https://www.emergentmind.com/topics/multimodal-diffusion-transformer"},{"title":"Multimodal Transformers are Hierarchical Modal-wise ...","url":"https://aclanthology.org/2025.acl-long.109.pdf"},{"title":"A Review of Transformer-Based Models for Computer Vision Tasks: Capturing Global Context and Spatial Relationships","url":"https://arxiv.org/html/2408.15178v1"}]

Based on the web search results, here's what I found regarding multimodal layer dependency probing in transformers from 2024-2025:

## Key Recent Research

A notable recent paper is "Head Pursuit: Probing Attention Specialization in Multimodal Transformers," which shows consistent patterns of specialization at the head level across both unimodal and multimodal transformers. The research validates the approach on language ta
…[truncated 1498 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7379
}
```

</details>

---


### Tool result

_source line 324 · 2026-05-17T18:46:15.010357+00:00_

Web search results for query: "mechanistic interpretability refusal safety neurons 2024 2025"

Links: [{"title":"Mechanistic Interpretability for AI Safety — A Review | Leonard F. Bereska","url":"https://leonardbereska.github.io/blog/2024/mechinterpreview/"},{"title":"Mechanistic Interpretability for AI Safety A Review","url":"https://arxiv.org/html/2404.14082v1"},{"title":"Mechanistic Interpretability for AI Safety A Review","url":"https://openreview.net/pdf/ea3c9a4135caad87031d3e445a80d0452f83da5d.pdf"},{"title":"Mechanistic?","url":"https://aclanthology.org/2024.blackboxnlp-1.30.pdf"},{"title":"Aligning AI Through Internal Understanding: The Role of Interpretability","url":"https://arxiv.org/html/2509.08592v1"},{"title":"Mechanistic interpretability — The Dan MacKinlay stable of variably-well-consider’d enterprises","url":"https://danmackinlay.name/notebook/ai_mech_interp.html"},{"title":"Mechanistic Interpretability for Large Language Model Alignment: Progress, Challenges, and Future Directions","url":"https://arxiv.org/html/2602.11180v1"},{"title":"[2404.14082] Mechanistic Interpretability for AI Safety -- A Review","url":"https://arxiv.org/abs/2404.14082"},{"title":"A Practical Review of Mechanistic Interpretability for Transformer-Based Language Models","url":"https://arxiv.org/html/2407.02646v4"},{"title":"Mechanistic Interpretability: Peeking Inside an LLM | Towards Data Science","url":"https://towardsdatascience.com/mechanistic-interpretability-peeking-inside-an-llm/"}]

I've completed the web search for your query on mechanistic interpretability, refusal safety neurons from 2024-2025. Here's a summary of the key findings:

## Overview of Recent Research

Mechanistic interpretability involves reverse engineering the computational mechanisms and representations learned by neural networks into human-understandable algorithms and concepts to provide a granular, causal understanding.

## Refusal Mechanisms Research

A particularly notable finding in this area 
…[truncated 1573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8685
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-17T18:46:16.014445+00:00_

Web search results for query: "training-induced alignment safety features LLM representations 2024 2025"

Links: [{"title":"The Hidden Dimensions of LLM Alignment:","url":"https://arxiv.org/pdf/2502.09674"},{"title":"Purifying Finetuning Data to Preserve LLM Safety Alignment","url":"https://aclanthology.org/2025.emnlp-main.406.pdf"},{"title":"ICML Poster Improving LLM Safety Alignment with Dual-Objective Optimization","url":"https://icml.cc/virtual/2025/poster/45626"},{"title":"arXiv:2505.15710v1 [cs.CL] 21 May 2025 Advancing LLM Safe Alignment with","url":"https://arxiv.org/pdf/2505.15710"},{"title":"Safety Alignment of Large Language Models via Contrasting Safe and Harmful Distributions","url":"https://arxiv.org/html/2406.16743v2"},{"title":"A Survey on Training-free Alignment of Large Language Models","url":"https://arxiv.org/html/2508.09016v1"},{"title":"[2507.19672] Alignment and Safety in Large Language Models: Safety Mechanisms, Training Paradigms, and Emerging Challenges","url":"https://arxiv.org/abs/2507.19672"},{"title":"Published as a conference paper at ICLR 2025 SALORA: SAFETY-ALIGNMENT PRESERVED","url":"https://yangzhangalmo.github.io/papers/ICLR25.pdf"},{"title":"Efficient Safety Alignment of Large Language Models via Preference","url":"https://aclanthology.org/2025.acl-long.1504.pdf"},{"title":"SAFETY ALIGNMENT SHOULD BE MADE MORE THAN ...","url":"https://openreview.net/pdf?id=6Mxhg9PtDE"}]

I've completed the web search for "training-induced alignment safety features LLM representations 2024 2025". Here are the key findings:

## Search Results Summary

The search returned several highly relevant papers from 2024-2025 exploring how safety alignment features are represented in LLM internal structures:

### Key Research Areas:

1. **Safety Feature Representations in Latent Space**
   - Research identifies specific directions in activation space that represent meaningful features like toxicity, truthfulness, and refusal
   - Safety features of LLMs can 
…[truncated 1699 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9237
}
```

</details>

---


### Tool result

_source line 326 · 2026-05-17T18:46:16.366149+00:00_

Web search results for query: "representational collapse layer transformers safety alignment 2024 2025"

Links: [{"title":"On the Role of Attention Masks and LayerNorm in Transformers Xinyi Wu1","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/1ac3030fc57850b0fb11dfe9d4880ad7-Paper-Conference.pdf"},{"title":"ANALYZ- ING AND ENHANCING LAYER-WISE SIMILARITY","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/03d113a060c0ac93a5859517a0f07271-Paper-Conference.pdf"},{"title":"Purifying Finetuning Data to Preserve LLM Safety Alignment","url":"https://aclanthology.org/2025.emnlp-main.406.pdf"},{"title":"SAFETY ALIGNMENT SHOULD BE MADE MORE THAN ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/88be023075a5a3ff3dc3b5d26623fa22-Paper-Conference.pdf"},{"title":"[2505.24333] Two failure modes of deep transformers and how to avoid them: a unified theory of signal propagation at initialisation","url":"https://arxiv.org/abs/2505.24333"},{"title":"SIMPLIFYING TRANSFORMER BLOCKS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/24fd58f52ff8d0496add8da3991644e9-Paper-Conference.pdf"},{"title":"How Transformers Actually Break","url":"https://www.b2bnn.com/2025/11/how-transformers-actually-break/"},{"title":"To appear at the ICLR 2025 Workshop on Representational Alignment (Re-Align)","url":"https://openreview.net/pdf?id=kqrnhp3nNS"},{"title":"Published as a conference paper at ICLR 2025 ADAPTIVE TRANSFORMER PROGRAMS:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf"},{"title":"Elon Musk on Grok AI Safety: Keeping Honest Models, Killing Decepticons","url":"https://www.basenor.com/blogs/news/elon-musk-on-grok-ai-safety-keeping-honest-models-killing-decepticons"}]

Based on the search results, I found several relevant papers and research on representational collapse, transformers, safety, and alignment from 2024-2025:

## Key Research Findings:

### Represent
…[truncated 1835 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8935
}
```

</details>

---


### Tool call

_source line 327 · 2026-05-17T18:46:18.023362+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"layer wise\" probing semantic syntactic safety 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"layer wise\" probing semantic syntactic safety 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-17T18:46:18.482810+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "circuit analysis safety jailbreaking transformer 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "circuit analysis safety jailbreaking transformer 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 329 · 2026-05-17T18:46:18.678036+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "faithfulness reasoning traces interpretability 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "faithfulness reasoning traces interpretability 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 330 · 2026-05-17T18:46:24.623242+00:00_

Web search results for query: "circuit analysis safety jailbreaking transformer 2024 2025"

Links: [{"title":"Circuits Updates - April 2025","url":"https://transformer-circuits.pub/2025/april-update/index.html"},{"title":"Transformer Circuits Thread","url":"https://transformer-circuits.pub/"},{"title":"Circuits Updates - July 2025","url":"https://transformer-circuits.pub/2025/july-update/index.html"},{"title":"Circuits Updates - January 2024","url":"https://transformer-circuits.pub/2024/jan-update/index.html"},{"title":"Frontiers | Analysis of interturn short circuit in regulating winding of power transformer based on field-circuit coupling","url":"https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2024.1393436/full"},{"title":"Isolation Transformers Market Size, Research, Competitive Analysis & Forecast 2033","url":"https://www.verifiedmarketreports.com/product/isolation-transformers-market/"},{"title":"A Mathematical Framework for Transformer Circuits","url":"https://transformer-circuits.pub/2021/framework/index.html"},{"title":"arXiv:2505.06295v1 [cs.LG] 7 May 2025","url":"https://arxiv.org/pdf/2505.06295"},{"title":"Circuits Updates - March 2024","url":"https://transformer-circuits.pub/2024/march-update"},{"title":"Research on electromagnetic vibration and noise of transformer under short circuit conditions | AIP Advances | AIP Publishing","url":"https://pubs.aip.org/aip/adv/article/15/3/035018/3339475/Research-on-electromagnetic-vibration-and-noise-of"}]

Based on the search results, I found relevant information about circuit analysis, safety, jailbreaking, and transformers from 2024-2025:

## Transformer Circuits and Safety Research (2024-2025)

Recent research from the Transformer Circuits Thread investigated jailbreak attempts on language models, analyzing why models refuse harmful requests like "making a bomb" and how obfuscation techniques can bypass safety measures. The research uses circuit tracing methodology to understand the i
…[truncated 853 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6140
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-17T18:46:25.828079+00:00_

Web search results for query: "faithfulness reasoning traces interpretability 2024 2025"

Links: [{"title":"FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness","url":"https://arxiv.org/html/2509.13334v1"},{"title":"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2510.04040v1"},{"title":"faithcot-bench: benchmarking instance- level faithfulness of ...","url":"https://arxiv.org/pdf/2510.04040"},{"title":"A Curry-Howard Framework for Verifying LLM Reasoning","url":"https://arxiv.org/pdf/2510.01069"},{"title":"FiDeLiS: Faithful Reasoning in Large Language Models for ...","url":"https://aclanthology.org/2025.findings-acl.436.pdf"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2602.11201v1"},{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://openreview.net/pdf?id=lN3yKqqzF1"},{"title":"Towards Transparent Reasoning: What Drives Faithfulness in Large Language Models?","url":"https://arxiv.org/html/2510.24236v2"},{"title":"Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution","url":"https://arxiv.org/html/2602.16154v1"},{"title":"Accepted papers | FoRLM @ NeurIPS'25","url":"https://reasoning-workshop.github.io/accepted/"}]

Based on the web search results, here's what's currently being researched on faithfulness reasoning traces interpretability in 2024-2025:

## Key Research Areas

**Chain-of-Thought (CoT) Faithfulness Problem**

Recent work reveals that reasoning traces are frequently unfaithful—the model's final answer does not actually depend on the intermediate steps it generates. An increasing number of studies have examined the faithfulness of CoT, a key concept in interpretability that assesses whether an explanation aligns with the model's actual reasoning or decision-making process.

**Recent Methods and Solutions**

1. **FRIT 
…[truncated 1127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7150
}
```

</details>

---


### Tool result

_source line 332 · 2026-05-17T18:46:26.029212+00:00_

Web search results for query: ""layer wise" probing semantic syntactic safety 2024 2025"

Links: [{"title":"Neuron-Guided Interpretation of Code LLMs: Where, Why, and How?","url":"https://arxiv.org/pdf/2512.19980"},{"title":"PromptGuard a structured framework for injection resilient language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-31086-y"},{"title":"A Review of Developmental Interpretability in Large Language Models","url":"https://arxiv.org/pdf/2508.15841"},{"title":"SYNTACTIC AND SEMANTIC CONTROL OF LARGE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a2d537e69a6c6638a3630eef835f07de-Paper-Conference.pdf"},{"title":"Explainability and Interpretability of Multilingual Large ...","url":"https://aclanthology.org/2025.emnlp-main.1033.pdf"},{"title":"Published as a conference paper at ICLR 2025 THE SEMANTIC HUB HYPOTHESIS:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/84fb08ae30ab266953d1ff72eb0611b1-Paper-Conference.pdf"},{"title":"‘Layer su Layer’: Identifying and Disambiguating the Italian npn Construction in BERT’s family","url":"https://arxiv.org/html/2604.03673v1"},{"title":"Depth Gives a False Sense of Privacy: LLM Internal States ...","url":"https://www.usenix.org/system/files/usenixsecurity25-dong-tian.pdf"},{"title":"SemanticCamo: Jailbreaking Large Language Models ...","url":"https://aclanthology.org/2025.findings-acl.745.pdf"},{"title":"Quantity-Quality Enhanced Self-Training Network for ...","url":"https://www.computer.org/csdl/journal/tp/2025/05/10851436/23JRInHTYis"}]

I found several relevant results for your search on layer-wise probing and semantic/syntactic analysis. Here are the key findings:

## Recent Research (2024-2025)

**Layer-wise Probing Methods:**
For each transformer layer of a frozen model, a linear classifier using multinomial logistic regression is trained, with the underlying model weights held constant and only the probe's parameters updated. A secondary, s
…[truncated 1521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8005
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-17T18:46:54.003670+00:00_

Based on my comprehensive web search across six different query angles, here is a detailed report of potentially important recent papers (2024-2026) that may be missing from your paper's references:

## MISSING PAPERS IDENTIFIED

### Category 1: Reasoning Model Safety & Self-Jailbreak (2024-2026)

**New papers NOT in your cited list:**

1. **"Large reasoning models are autonomous jailbreak agents"** - Nature Communications (2025/2026) - Studies how advanced reasoning models like DeepSeek-R1, Gemini 2.5 Flash can autonomously plan multi-turn jailbreak attacks with 97.14% success rates

2. **"When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models"** (arXiv:2510.21285) - Directly addresses the self-jailbreak failure mode where models override their initial safety judgments during reasoning

3. **"Enhancing Model Defense Against Jailbreaks with Proactive Safety Reasoning"** (arXiv:2501.19180) - Proposes Safety Chain-of-Thought (SCoT) defense strategy

4. **"Reasoned Safety Alignment: Ensuring Jailbreak Defense via Answer-Then-Check"** (arXiv:2509.11629 or OpenReview) - Applies reasoning to mitigate jailbreaks before generating answers

5. **"Can Reasoning Models Obfuscate Reasoning? Stress-Testing Chain-of-Thought Monitorability"** (arXiv:2510.19851) - Critical work on CoT obfuscation and whether safety monitors can be defeated

6. **"Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety"** (arXiv:2507.11473) - Documents vulnerabilities in CoT-based monitoring; shows high-pressure obfuscation can defeat monitors

7. **"Reasoning Models Don't Always Say What They Think"** - Anthropic work on unfaithful reasoning (may overlap with chen2025unfaithful you already cite, but distinct results)

---

### Category 2: Hidden-State Probing for Safety Detection (2024-2026)

**New papers NOT in your cited list:**

8. **"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs"** (2025, medRxiv)
…[truncated 7841 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 63743
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-17T18:50:04.671035+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: \"Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models\"\n**审查侧重**: 新颖性 + 论文完整性\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n**一句话总结**: 扎实的方法论观察（layer selection bias 可逆转结论）配合严格的统计框架，但核心 HS-vs-text 对比因文本基线过弱（384d vs 4096-5120d）而说服力不足，实用价值受限于高 FPR 和极小样本量。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0 / 5 | 核心 claim 有统计支撑但存在未控制的维度混淆变量；32B 样本量过小（n=19-20）；QwQ-32B 结果实质上削弱了主论点 |\n| Excitement | 2.5 / 5 | Layer selection sensitivity 观察有用但机制直白（crossing rate 在浅层因 volatility 膨胀）；对 probing 社区的影响面窄；\"HS > text\" 结论在给定维度差距下缺乏惊奇性 |\n| Reproducibility | 4.0 / 5 | 超参数、统计流程、seed 结果均详细报告；代码承诺发布但目前不可用 |\n| Reviewer Confidence | 4 / 5 | 仔细阅读全文、附录和引用，对 probing 方法论和 safety monitoring 较熟悉 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **文本基线维度过弱，核心对比存在严重混淆变量**\n- 具体位置：Section 3.2（Probe Architecture）、Section 4.3（HS vs. Text Comparison）、Section 6 Limitations para 5\n- 问题：HS probe 使用 4096-5120 维特征，text probe 使用 all-MiniLM-L6-v2 的 384 维嵌入，维度比为 10-13x。论文的核心结论 \"HS probes significantly outperform text probes\" 无法与 \"高维特征优于低维特征\" 区分开。这不是 modality 的胜利，可能只是 dimensionality 的胜利。\n- Limitations Section 承认了这一点（\"Larger encoders or domain-fine-tuned models might narrow the observed HS-text accuracy gap\"），但仅以一段文字轻描带过，没有做任何实验验证。\n- 为什么影响接收：论文的 Contribution 2（\"Consistent HS precision advantage at correctly selected layers\"）建立在这个对比之上。如果 text probe 换成 768d 或 1024d 的编码器（如 all-mpnet-base-v2 或 BGE-base），precision gap 可能大幅缩小甚至消失。在没有控制维度变量的情况下，12/12 Holm-Bonferroni 通过并不能证明 modality 优势。\n- 建议修改方向：(a) 至少增加一个中等维度的 text encoder（如 768d）作为额外 baseline；(b) 或对 HS 特征做 PCA 降维到 384d 后重新对比，isolate modality effect from dimensionality effect；(c) 或将 framing 从 \"HS outperforms text\" 调整为 \"HS at full dimensionality outperforms a specific lightweight text baseline\"，并在 Abstract/Intro 中明确限定。\n\n**N2** [critical] **QwQ-32B 结果实质性削弱主论点但论文叙事未充分反映**\n- 具体位置：Section 4.5（Table 5）、Section 5 Discussion para 3\n- 问题：QwQ-32B 的 HS probe lead time 为负值（-1.2 到 +1.9 步），而 text probe lead time 为 +3.7 到 +12.3 步。Position-only baseline 达到 0.746 bal_acc，与 HS probe（0.740）不可区分。这意味着对 QwQ-32B 而言：(1) HS probe 检测到 safety commitment 比 text probe 更**晚**，(2) HS probe 相对于简单的位置特征**没有增量贡献**。\n- 论文在 Discussion 和 Limitations 中提到了这些数字，但 Abstract 和 Introduction 的叙事仍然是 \"all 12 tests confirm significant HS superiority\" — 这在技术层面是真的（precision 确实更高），但对读者产生误导：一个检测**更晚**且**不优于位置基线**的 probe 在实际部署中并不 \"superior\"。\n- 为什么影响接收：Abstract 和 Introduction 构建的 narrative（\"HS probes significantly outperform text probes across all four models\"）与实验细节之间存在 framing gap。审稿人读完 Section 4.5 后会感到 narrative 不诚实。\n- 建议修改方向：Abstract 和 Introduction 应明确区分 per-step accuracy superiority 和 practical detection superiority。建议 Abstract 增加一句类似 \"however, practical detection profiles diverge: one 32B model shows HS detection timing worse than text\" 的限定。Contribution 2 应将限定条件提升到与主张同等的 prominence。\n\n**N3** [critical] **32B 模型样本量不足以支撑强统计结论**\n- 具体位置：Table 1（n=19-20 test traces for 32B）、Section 4.3、Appendix B\n- 问题：R1-32B 有 20 条测试 trace，QwQ-32B 有 19 条。R1-32B 在 W=1 时仅 25% coverage（5 of 20 traces detected）。Bootstrap 1000 resamples 并不创造信息——对 20 个样本做 bootstrap 的置信区间仍然很宽。论文报告 p<0.001 for R1-32B，但 effective sample size 是 5 条 detected traces 的指标值差异。\n- R1-32B 在 W≥3 时统计显著性消失（\"due to dimensionality constraint\"），这进一步说明 W=1 的显著结果可能是统计 artifact。论文将此归因于 \"51200×W features for n=20 traces\"，但维度灾难在 W=1 时同样存在（5120d features, n=20 traces），只是因为 W=1 时 feature dim = 5120 < n×features 的某个阈值而勉强通过。\n- 为什么影响接收：对一个有 4 个模型的研究，其中 2 个模型（占一半）的证据质量明显不足。审稿人会质疑这些 p-value 是否可靠。\n- 建议修改方向：(a) 降低对 32B 结论的 confidence level——在 Abstract/Intro 中明确标注样本量限制；(b) 考虑 leave-one-out 或其他适合小样本的统计方法作为 robustness check；(c) 如果可能，收集更多 32B traces。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Related Work 缺少 2024-2026 年重要工作**\n- 具体位置：Section 2\n- 问题：31 citations 对于 EMNLP 长文偏少。通过 WebSearch 发现以下重要遗漏：\n  - **Multi-dimensional refusal**：\"There Is More to Refusal in Large Language Models than a Single Direction\"（2025, arXiv:2602.02132）——直接挑战论文引用的 Arditi et al. 的 single-direction model，证明 refusal 使用复杂的 concept cones 而非单一方向。\"The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence\"（ICML 2025）同理。这些工作与本文的 layer-wise probe analysis 高度相关。\n  - **CoT monitorability**：\"Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety\"（arXiv:2507.11473）——论证 CoT monitoring 的脆弱性，直接关系到 text probe 的假设基础。\n  - **自主 jailbreak**：\"Large Reasoning Models Are Autonomous Jailbreak Agents\"（Nature Communications 2025/2026）——self-jailbreak 领域的重要后续工作。\n  - **Safety-aware probing**：\"Towards Fully Exploiting LLM Internal States to Enhance Safety\"（ACL 2025）——直接相关的 HS safety 工作。\n- 建议：补充至少 5-8 条高相关引用，特别是 multi-dimensional refusal 和 CoT monitorability 方向。\n\n**W2** [warning] **Discussion 与 Conclusion 内容显著重复**\n- 具体位置：Section 5（Discussion）vs Section 6（Conclusion）\n- 问题：Conclusion 第 2-4 句几乎完全重复 Discussion 的核心内容（layer selection bias reversal、12/12 HB tests、oracle gap 85.5%、future work directions）。Discussion para 4 的 future work 列表（activation patching, multilingual, multi-turn, 13B/70B）与 Conclusion 最后一句逐项重合。\n- 建议：Conclusion 压缩为 3-4 句，聚焦 takeaway message 和 broader impact，删除与 Discussion 重复的技术细节。\n\n**W3** [warning] **GRU 实验使用不同的 data split（70/30 vs 60/20/20），交叉对比不可靠**\n- 具体位置：Appendix E（GRU Training Details）第 1 段\n- 问题：主实验（logistic regression）使用 60/20/20 split，GRU 实验使用 70/30 split。不同的 split 意味着不同的 test set，direct performance comparison between LR and GRU 是 confounded。Appendix E 中的 Table 8 虽然在 60/20/20 下对比了 GRU 和 LR，但这与主文使用的 GRU 数字不一致。\n- 建议：在正文中明确标注 GRU 使用不同 split，或统一为 60/20/20。\n\n**W4** [warning] **Contribution 3（\"comprehensive negative results\"）的 framing 过度**\n- 具体位置：Introduction Contribution 3、Section 4.6\n- 问题：论文声称 7 种方法 \"all fail\"，但 RepE on QwQ-32B 达到 0.756 bal_acc（supervised LR 为 0.740），并不算 \"fail\"。Cross-model transfer QwQ→R1-32B 达到 67.3% accuracy（超过 within-model baseline）。\"All fail\" 的叙事过度简化了 nuanced 结果。\n- 建议：改为 \"produce inconsistent or limited results\" 或 \"fail to reliably match supervised probing\"，并在 Contribution 3 中标注 RepE 的 model-dependent performance。\n\n**W5** [warning] **Novelty 相对于 Findings track 的定位**\n- 问题：论文的核心 methodological finding 是 \"crossing_rate 在浅层因 representational volatility 而膨胀，导致 composite metric bias\"。这个机制在被指出后是相当直觉的——浅层更 volatile，volatile 表征更频繁 cross threshold，threshold-crossing rate 因此人为升高。这更像是一个 useful cautionary note 而非 deep methodological insight。\n- 论文将此提升为 \"implications beyond our specific task: any study that uses composite metrics to select probe layers is susceptible to the same bias mechanism\"（Discussion para 1），但没有在其他任务上验证这一泛化声称。\n- 建议：如果能在另一个 probing 任务（如 sentiment、factuality）上复现 layer selection reversal，泛化声称的说服力会大幅提升。否则应限定为 safety probing 领域的发现。\n\n---\n\n## 小问题（不影响接收）\n\n- **Abstract 第 1 句**缺少 \"(LLMs)\" 的全称定义——虽然 LLM 已是通用缩写，但 Abstract 应自包含。实际上第 1 句写了 \"Large Language Models (LLMs)\"，已有定义。无问题。\n- **Table 5 (32B cross-model divergence)**：QwQ-32B \"HS vs. Position\" 为 -0.6pp，即 HS probe 不如位置基线——这个数字应该加粗或用其他方式标注以引起读者注意。\n- **Appendix D (OT-7B detailed results)**：Table 6 的 caption 提到 \"correction of a layer selection bug\"，但正文中没有详细说明这个 bug 与 Appendix F 的 M002 bug 是什么关系。如果是不同的 bug，需要说明。\n- **Appendix F (Bug Disclosure)**：disclosure 诚实且详细，值得肯定。但 \"midpoint heuristic placeholder\" 的初始化方式非常不寻常——这看起来不像是典型的 coding error，更像是 deliberate placeholder。建议说明这个 placeholder 最初是在什么开发阶段、出于什么目的引入的。\n- **references.bib**：`openthinker` 引用标题为 \"OpenThoughts\" 但 bib key 为 `openthinker`——不影响编译但可能导致混淆。QwQ 引用类型为 `misc` 且 venue 为空——建议标注为技术报告或 blog post。\n\n---\n\n## 主要优势\n\n1. **方法论严谨性**：Holm-Bonferroni correction, null-centered bootstrap, control tasks, selectivity metrics——统计框架在同类工作中属上乘。\n2. **透明度优秀**：Bug disclosure（Appendix F）在 ML 论文中罕见，体现了良好的科学道德。Limitations section 诚实全面，覆盖了多数 weakness。\n3. **负结果的系统报告**：7 种替代方法的失败模式分析有真正的信息量，帮助后续研究者避免重复劳动。\n4. **实验覆盖广度**：4 个模型 × 2 架构 × 2 scale × 5 layer metrics × 7 window sizes × 7 baselines——在资源受限下做到了合理的覆盖。\n5. **写作质量**：无明显 AI 写作痕迹（零 em-dash、零 en-dash、无黑名单用词），叙事连贯，主线统一性较好（尽管 QwQ 的 nuance 被 underrepresented）。\n\n---\n\n## Questions to Authors\n\n1. 如果将 HS 特征 PCA 降维到 384d（与 text encoder 维度匹配），12/12 HB tests 中有多少仍然 pass？\n2. QwQ-32B position baseline 达到 0.746 vs HS 0.740——论文如何论证 QwQ 上的 HS probe 检测到了 \"genuine safety structure\" 而非仅仅是 positional artifact？Selectivity 为 14.4pp 但这是 vs. random labels，不是 vs. position features。\n3. 论文使用单一数据集（HarmThoughts）。如果换用不同的 jailbreak 类型或不同的 CP annotation protocol，layer selection sensitivity 结论是否 robust？\n4. R1-32B 在 W=1 时 coverage 仅 25%（5/20 traces）。报告的 precision +15.4pp 实际上基于这 5 条 trace 的差异。能否报告这 5 条 trace 的具体 precision 值及其 variance？\n5. Appendix D 提到 \"correction of a layer selection bug\" for OT-7B——这个 bug 与 Appendix F 的 M002 bug 是同一个还是不同的问题？\n\n---\n\n## Missing References（经 WebSearch 验证）\n\n以下论文与本文高度相关但未被引用：\n\n1. \"There Is More to Refusal in Large Language Models than a Single Direction\" (2025, arXiv:2602.02132) — 证明 refusal 使用 multi-dimensional concept cones，挑战 Arditi et al. 的 single-direction 假设\n2. \"The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence\" (ICML 2025) — 同上\n3. \"Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety\" (2025, arXiv:2507.11473) — CoT monitoring 脆弱性\n4. \"Towards Fully Exploiting LLM Internal States to Enhance Safety\" (ACL 2025) — HS safety probing\n5. \"Large Reasoning Models Are Autonomous Jailbreak Agents\" (Nature Communications 2025/2026) — 自主 jailbreak\n6. \"Safety Alignment Should Be Made More Than Skin-Deep\" (ICLR 2025) — 跨层 safety 信息分布\n\n---\n\n## 引用验证结果\n\n通过 `verify_references` 工具验证了全部 31 条引用：\n- 26/31 在 OpenAlex 确认真实\n- 5 条未在 OpenAlex 找到但均为真实论文（DeepSeek-R1、QwQ、RepE、H-CoT、chen2025unfaithful——均可通过 arXiv 确认）\n- 0 orphan entries、0 missing bib entries\n- 无虚构引用",
  "reviewer_id": "2",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: \"Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models\"\n**审查侧重**: 新颖性 + 论文完整性\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n**一句话总结**: 扎实的方法论观察（layer selection bias 可逆转结论）配合严格的统计框架，但核心 HS-vs-text 对比因文本基线过弱（384d vs 4096-5120d）而说服力不足，实用价值受限于高 FPR 和极小样本量。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0 / 5 | 核心 claim 有统计支撑但存在未控制的维度混淆变量；32B 样本量过小（n=19-20）；QwQ-32B 结果实质上削弱了主论点 |\n| Excitement | 2.5 / 5 | Layer selection sensitivity 观察有用但机制直白（crossing rate 在浅层因 volatility 膨胀）；对 probing 社区的影响面窄；\"HS > text\" 结论在给定维度差距下缺乏惊奇性 |\n| Reproducibility | 4.0 / 5 | 超参数、统计流程、seed 结果均详细报告；代码承诺发布但目前不可用 |\n| Reviewer Confidence | 4 / 5 | 仔细阅读全文、附录和引用，对 probing 方法论和 safety monitoring 较熟悉 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **文本基线维度过弱，核心对比存在严重混淆变量**\n- 具体位置：Section 3.2（Probe Architecture）、Section 4.3（HS vs. Text Comparison）、Section 6 Limitations para 5\n- 问题：HS probe 使用 4096-5120 维特征，text probe 使用 all-MiniLM-L6-v2 的 384 维嵌入，维度比为 10-13x。论文的核心结论 \"HS probes significantly outperform text probes\" 无法与 \"高维特征优于低维特征\" 区分开。这不是 modality 的胜利，可能只是 dimensionality 的胜利。\n- Limitations Section 承认了这一点（\"Larger encoders or domain-fine-tuned models might narrow the observed HS-text accuracy gap\"），但仅以一段文字轻描带过，没有做任何实验验证。\n- 为什么影响接收：论文的 Contribution 2（\"Consistent HS precision advantage at correctly selected layers\"）建立在这个对比之上。如果 text probe 换成 768d 或 1024d 的编码器（如 all-mpnet-base-v2 或 BGE-base），precision gap 可能大幅缩小甚至消失。在没有控制维度变量的情况下，12/12 Holm-Bonferroni 通过并不能证明 modality 优势。\n- 建议修改方向：(a) 至少增加一个中等维度的 text encoder（如 768d）作为额外 baseline；(b) 或对 HS 特征做 PCA 降维到 384d 后重新对比，isolate modality effect from dimensionality effect；(c) 或将 framing 从 \"HS outperforms text\" 调整为 \"HS at full dimensionality outperforms a specific lightweight text baseline\"，并在 Abstract/Intro 中明确限定。\n\n**N2** [critical] **QwQ-32B 结果实质性削弱主论点但论文叙事未充分反映**\n- 具体位置：Section 4.5（Table 5）、Section 5 Discussion para 3\n- 问题：QwQ-32B 的 HS probe lead time 为负值（-1.2 到 +1.9 步），而 text probe lead time 为 +3.7 到 +12.3 步。Position-only baseline 达到 0.746 bal_acc，与 HS probe（0.740）不可区分。这意味着对 QwQ-32B 而言：(1) HS probe 检测到 safety commitment 比 text probe 更**晚**，(2) HS probe 相对于简单的位置特征**没有增量贡献**。\n- 论文在 Discussion 和 Limitations 中提到了这些数字，但 Abstract 和 Introduction 的叙事仍然是 \"all 12 tests confirm significant HS superiority\" — 这在技术层面是真的（precision 确实更高），但对读者产生误导：一个检测**更晚**且**不优于位置基线**的 probe 在实际部署中并不 \"superior\"。\n- 为什么影响接收：Abstract 和 Introduction 构建的 narrative（\"HS probes significantly outperform text probes across all four models\"）与实验细节之间存在 framing gap。审稿人读完 Section 4.5 后会感到 narrative 不诚实。\n- 建议修改方向：Abstract 和 Introduction 应明确区分 per-step accuracy superiority 和 practical detection superiority。建议 Abstract 增加一句类似 \"however, practical detection profiles diverge: one 32B model shows HS detection timing worse than text\" 的限定。Contribution 2 应将限定条件提升到与主张同等的 prominence。\n\n**N3** [critical] **32B 模型样本量不足以支撑强统计结论**\n- 具体位置：Table 1（n=19-20 test traces for 32B）、Section 4.3、Appendix B\n- 问题：R1-32B 有 20 条测试 trace，QwQ-32B 有 19 条。R1-32B 在 W=1 时仅 25% coverage（5 of 20 traces detected）。Bootstrap 1000 resamples 并不创造信息——对 20 个样本做 bootstrap 的置信区间仍然很宽。论文报告 p<0.001 for R1-32B，但 effective sample size 是 5 条 detected traces 的指标值差异。\n- R1-32B 在 W≥3 时统计显著性消失（\"due to dimensionality constraint\"），这进一步说明 W=1 的显著结果可能是统计 artifact。论文将此归因于 \"51200×W features for n=20 traces\"，但维度灾难在 W=1 时同样存在（5120d features, n=20 traces），只是因为 W=1 时 feature dim = 5120 < n×features 的某个阈值而勉强通过。\n- 为什么影响接收：对一个有 4 个模型的研究，其中 2 个模型（占一半）的证据质量明显不足。审稿人会质疑这些 p-value 是否可靠。\n- 建议修改方向：(a) 降低对 32B 结论的 confidence level——在 Abstract/Intro 中明确标注样本量限制；(b) 考虑 leave-one-out 或其他适合小样本的统计方法作为 robustness check；(c) 如果可能，收集更多 32B traces。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Related Work 缺少 2024-2026 年重要工作**\n- 具体位置：Section 2\n- 问题：31 citations 对于 EMNLP 长文偏少。通过 WebSearch 发现以下重要遗漏：\n  - **Multi-dimensional refusal**：\"There Is More to Refusal in Large Language Models than a Single Direction\"（2025, arXiv:2602.02132）——直接挑战论文引用的 Arditi et al. 的 single-direction model，证明 refusal 使用复杂的 concept cones 而非单一方向。\"The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence\"（ICML 2025）同理。这些工作与本文的 layer-wise probe analysis 高度相关。\n  - **CoT monitorability**：\"Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety\"（arXiv:2507.11473）——论证 CoT monitoring 的脆弱性，直接关系到 text probe 的假设基础。\n  - **自主 jailbreak**：\"Large Reasoning Models Are Autonomous Jailbreak Agents\"（Nature Communications 2025/2026）——self-jailbreak 领域的重要后续工作。\n  - **Safety-aware probing**：\"Towards Fully Exploiting LLM Internal States to Enhance Safety\"（ACL 2025）——直接相关的 HS safety 工作。\n- 建议：补充至少 5-8 条高相关引用，特别是 multi-dimensional refusal 和 CoT monitorability 方向。\n\n**W2** [warning] **Discussion 与 Conclusion 内容显著重复**\n- 具体位置：Section 5（Discussion）vs Section 6（Conclusion）\n- 问题：Conclusion 第 2-4 句几乎完全重复 Discussion 的核心内容（layer selection bias reversal、12/12 HB tests、oracle gap 85.5%、future work directions）。Discussion para 4 的 future work 列表（activation patching, multilingual, multi-turn, 13B/70B）与 Conclusion 最后一句逐项重合。\n- 建议：Conclusion 压缩为 3-4 句，聚焦 takeaway message 和 broader impact，删除与 Discussion 重复的技术细节。\n\n**W3** [warning] **GRU 实验使用不同的 data split（70/30 vs 60/20/20），交叉对比不可靠**\n- 具体位置：Appendix E（GRU Training Details）第 1 段\n- 问题：主实验（logistic regression）使用 60/20/20 split，GRU 实验使用 70/30 split。不同的 split 意味着不同的 test set，direct performance comparison between LR and GRU 是 confounded。Appendix E 中的 Table 8 虽然在 60/20/20 下对比了 GRU 和 LR，但这与主文使用的 GRU 数字不一致。\n- 建议：在正文中明确标注 GRU 使用不同 split，或统一为 60/20/20。\n\n**W4** [warning] **Contribution 3（\"comprehensive negative results\"）的 framing 过度**\n- 具体位置：Introduction Contribution 3、Section 4.6\n- 问题：论文声称 7 种方法 \"all fail\"，但 RepE on QwQ-32B 达到 0.756 bal_acc（supervised LR 为 0.740），并不算 \"fail\"。Cross-model transfer QwQ→R1-32B 达到 67.3% accuracy（超过 within-model baseline）。\"All fail\" 的叙事过度简化了 nuanced 结果。\n- 建议：改为 \"produce inconsistent or limited results\" 或 \"fail to reliably match supervised probing\"，并在 Contribution 3 中标注 RepE 的 model-dependent performance。\n\n**W5** [warning] **Novelty 相对于 Findings track 的定位**\n- 问题：论文的核心 methodological finding 是 \"crossing_rate 在浅层因 representational volatility 而膨胀，导致 composite metric bias\"。这个机制在被指出后是相当直觉的——浅层更 volatile，volatile 表征更频繁 cross threshold，threshold-crossing rate 因此人为升高。这更像是一个 useful cautionary note 而非 deep methodological insight。\n- 论文将此提升为 \"implications beyond our specific task: any study that uses composite metrics to select probe layers is susceptible to the same bias mechanism\"（Discussion para 1），但没有在其他任务上验证这一泛化声称。\n- 建议：如果能在另一个 probing 任务（如 sentiment、factuality）上复现 layer selection reversal，泛化声称的说服力会大幅提升。否则应限定为 safety probing 领域的发现。\n\n---\n\n## 小问题（不影响接收）\n\n- **Abstract 第 1 句**缺少 \"(LLMs)\" 的全称定义——虽然 LLM 已是通用缩写，但 Abstract 应自包含。实际上第 1 句写了 \"Large Language Models (LLMs)\"，已有定义。无问题。\n- **Table 5 (32B cross-model divergence)**：QwQ-32B \"HS vs. Position\" 为 -0.6pp，即 HS probe 不如位置基线——这个数字应该加粗或用其他方式标注以引起读者注意。\n- **Appendix D (OT-7B detailed results)**：Table 6 的 caption 提到 \"correction of a layer selection bug\"，但正文中没有详细说明这个 bug 与 Appendix F 的 M002 bug 是什么关系。如果是不同的 bug，需要说明。\n- **Appendix F (Bug Disclosure)**：disclosure 诚实且详细，值得肯定。但 \"midpoint heuristic placeholder\" 的初始化方式非常不寻常——这看起来不像是典型的 coding error，更像是 deliberate placeholder。建议说明这个 placeholder 最初是在什么开发阶段、出于什么目的引入的。\n- **references.bib**：`openthinker` 引用标题为 \"OpenThoughts\" 但 bib key 为 `openthinker`——不影响编译但可能导致混淆。QwQ 引用类型为 `misc` 且 venue 为空——建议标注为技术报告或 blog post。\n\n---\n\n## 主要优势\n\n1. **方法论严谨性**：Holm-Bonferroni correction, null-centered bootstrap, control tasks, selectivity metrics——统计框架在同类工作中属上乘。\n2. **透明度优秀**：Bug disclosure（Appendix F）在 ML 论文中罕见，体现了良好的科学道德。Limitations section 诚实全面，覆盖了多数 weakness。\n3. **负结果的系统报告**：7 种替代方法的失败模式分析有真正的信息量，帮助后续研究者避免重复劳动。\n4. **实验覆盖广度**：4 个模型 × 2 架构 × 2 scale × 5 layer metrics × 7 window sizes × 7 baselines——在资源受限下做到了合理的覆盖。\n5. **写作质量**：无明显 AI 写作痕迹（零 em-dash、零 en-dash、无黑名单用词），叙事连贯，主线统一性较好（尽管 QwQ 的 nuance 被 underrepresented）。\n\n---\n\n## Questions to Authors\n\n1. 如果将 HS 特征 PCA 降维到 384d（与 text encoder 维度匹配），12/12 HB tests 中有多少仍然 pass？\n2. QwQ-32B position baseline 达到 0.746 vs HS 0.740——论文如何论证 QwQ 上的 HS probe 检测到了 \"genuine safety structure\" 而非仅仅是 positional artifact？Selectivity 为 14.4pp 但这是 vs. random labels，不是 vs. position features。\n3. 论文使用单一数据集（HarmThoughts）。如果换用不同的 jailbreak 类型或不同的 CP annotation protocol，layer selection sensitivity 结论是否 robust？\n4. R1-32B 在 W=1 时 coverage 仅 25%（5/20 traces）。报告的 precision +15.4pp 实际上基于这 5 条 trace 的差异。能否报告这 5 条 trace 的具体 precision 值及其 variance？\n5. Appendix D 提到 \"correction of a layer selection bug\" for OT-7B——这个 bug 与 Appendix F 的 M002 bug 是同一个还是不同的问题？\n\n---\n\n## Missing References（经 WebSearch 验证）\n\n以下论文与本文高度相关但未被引用：\n\n1. \"There Is More to Refusal in Large Language Models than a Single Direction\" (2025, arXiv:2602.02132) — 证明 refusal 使用 multi-dimensional concept cones，挑战 Arditi et al. 的 single-direction 假设\n2. \"The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence\" (ICML 2025) — 同上\n3. \"Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety\" (2025, arXiv:2507.11473) — CoT monitoring 脆弱性\n4. \"Towards Fully Exploiting LLM Internal States to Enhance Safety\" (ACL 2025) — HS safety probing\n5. \"Large Reasoning Models Are Autonomous Jailbreak Agents\" (Nature Communications 2025/2026) — 自主 jailbreak\n6. \"Safety Alignment Should Be Made More Than Skin-Deep\" (ICLR 2025) — 跨层 safety 信息分布\n\n---\n\n## 引用验证结果\n\n通过 `verify_references` 工具验证了全部 31 条引用：\n- 26/31 在 OpenAlex 确认真实\n- 5 条未在 OpenAlex 找到但均为真实论文（DeepSeek-R1、QwQ、RepE、H-CoT、chen2025unfaithful——均可通过 arXiv 确认）\n- 0 orphan entries、0 missing bib entries\n- 无虚构引用",
    "reviewer_id": "2",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-17T18:50:08.386578+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3715
}
```

</details>

---


### Assistant

_source line 336 · 2026-05-17T18:50:19.641832+00:00_

审稿报告已提交给 Review Director。

**评分摘要**：Overall 3.0 (Findings)，Soundness 3.0，Excitement 2.5。

**三个 Must-Fix 问题**：
1. 文本基线维度过弱（384d vs 4096-5120d），HS 优势可能是维度的胜利而非 modality 的胜利
2. QwQ-32B 结果（HS 检测更晚、不优于位置基线）实质性削弱主论点，但 Abstract/Intro 叙事未充分反映
3. 32B 样本量不足（n=19-20），R1-32B 在 W=1 仅 5 条 trace 被检测

**五个 Should-Fix 问题**：Related Work 遗漏重要 2024-2026 论文、Discussion/Conclusion 重复、GRU 使用不同 data split、"all fail" framing 过度、novelty 泛化声称缺乏跨任务验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2"
}
```

</details>

---


## Round 10

## Round 10

2 recorded events


### User

_source line 337 · 2026-05-17T18:51:12.682726+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题。对每条意见使用：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

以下是 Reviewer 1 的完整审稿意见：

### Must-Fix 问题

**N1** [critical] **文本基线维度严重不对等，削弱核心 claim**
- HS 特征维度为 4096-5120d，文本基线 all-MiniLM-L6-v2 仅 384d，维度差 10.7x-13.3x。在使用 L2 正则化逻辑回归时，更高维度的输入天然拥有更多可利用的特征空间。论文 Limitations 中承认 "Larger encoders or domain-fine-tuned models might narrow the observed HS-text accuracy gap"，但正文中的核心 claim "12/12 Holm-Bonferroni corrected tests confirm significant HS superiority" 未做任何限定。
- 论文的第二条 contribution 建立在这个对比之上。如果用更强的文本编码器（如 E5-large 1024d、GTE-large 1024d、或 instructor-xl 768d），+15-24pp 的精度优势可能大幅缩小。当前比较等价于证明 "5120 维特征优于 384 维特征"。

**N2** [critical] **"12/12 Holm-Bonferroni 通过"夸大了证据强度**
- 12 个测试 = 3 指标 × 4 模型。但 3 个指标（balanced accuracy, precision, FPR）在统计上高度相关。同一模型内的 3 个测试实质上不是独立测试。真实的独立确认数更接近 4（4 个模型各一个），而非 12。Holm-Bonferroni 校正在相关测试下过于保守地设定阈值，但同时 "12/12" 的呈现方式给审稿人虚假的信心。

**N3** [critical] **QwQ-32B 上位置基线 > HS 探针，实质性削弱 contribution claim**
- QwQ-32B 位置基线 balanced accuracy = 0.746，HS 探针 = 0.740。仅用 t/T 作输入的简单分类器比 HS 探针表现更好。如果位置特征足以达到甚至超过 HS 探针的辨别力，那么 HS 探针可能主要在学习位置信号而非安全语义。
- 建议在回归中加入位置特征作为控制变量后重新测试 HS-text 差异，或对 QwQ 的 claim 做更诚实的限定。

### Should-Fix 问题

**W1** [warning] **32B 样本量（n=19-20）的统计功效未充分讨论**
- R1-32B 在 W=1 时仅 25% 覆盖率（5/20 traces），意味着统计测试实际基于 5 个检出 trace 的指标差异。论文未报告效应量的置信区间。

**W2** [warning] **"四个互补指标收敛"夸大了独立性**
- 四个"互补"指标中真正独立收敛的证据约为 2 个指标（balanced accuracy + precision/FPR），而非 4 个。

**W3** [warning] **Negative results 的 framing 存在偏差**
- RepE on QwQ: balanced accuracy 0.756 超过 supervised LR 的 0.740，但被归类为 "failure"。
- BOCPD on R1-8B: 93% 检测率也被称为 "fail"。
- Cross-model transfer: 仅测试 PCA + direct，未尝试 CCA、Procrustes。

**W4** [warning] **主实验（Table 2）缺少多种子报告**
- 主对比实验似乎为单次运行。如果有种子敏感性，"12/12 tests pass" 可能在某些种子下不成立，特别是最弱测试 R1-8B FPR p=0.044。

**W5** [warning] **GRU 使用 70/30 split vs 主实验 60/20/20，结果不可直接比较**
- 不同的 split 意味着不同的 test set，direct performance comparison 是 confounded。

### 缺失引用
1. 更强文本编码器作为 baseline 的替代选项
2. LEACE / linear concept erasure (Belrose et al., 2023)
3. Causal probing / amnesic probing (Elazar et al., 2021)
4. Procrustes 对齐的原始文献

---

请对以上每条 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 338 · 2026-05-17T18:52:44.902588+00:00_

以下是我对 Reviewer 1 各条意见的逐条交叉回应。

---

## 交叉回应 Reviewer 1

### Must-Fix 问题

**[AGREE] R1-N1: 文本基线维度严重不对等**

完全同意。这与我的 N1 一致。384d vs 4096-5120d 的维度差是本文最严重的混淆变量。论文在 Section 5 Discussion para 2 中甚至自己承认 "Information-theoretic reasoning suggests that hidden states (4096 to 5120 dimensions of internal computation) should dominate text features (384-dimensional sentence embeddings) purely by signal capacity"，这等于承认了当前结果可能完全由维度差驱动。Contribution 2 的 claim 在没有控制维度的情况下无法成立。

补充 R1 未提到的一点：temporal windowing 进一步放大了维度差异。在 W=15 时，HS 输入维度为 4096×15=61440d（R1-8B），而 text 为 384×15=5760d——维度比从 10.7x 扩大到 10.7x 不变但绝对差距剧增，使得 L2 正则化的效力在两个 modality 上不可比。

---

**[AGREE with nuance] R1-N2: "12/12 Holm-Bonferroni 通过"夸大了证据强度**

部分同意。R1 的核心论点（3 个 metrics 高度相关，独立确认数接近 4 而非 12）在直觉上是正确的。Balanced accuracy、precision、FPR 在同一模型的同一混淆矩阵上计算，它们的 bootstrap 差异在 resample 间高度正相关。

但需要指出一个技术细节：Holm-Bonferroni 在任意依赖结构下都能有效控制 family-wise error rate，这是其设计保证（见 Holm 1979 原文）。因此 "12/12 pass" 作为 FWER 控制的声明在统计上是 valid 的。R1 的真正问题在于**呈现方式**（"12/12" 给人 12 条独立证据线的错觉）而非统计程序本身。

建议作者将呈现改为 "all 4 models show significant HS advantage on all three metrics"，强调 4 个独立模型而非 12 个相关测试。

---

**[AGREE] R1-N3: QwQ-32B 位置基线 > HS 探针**

完全同意，这与我的 N2 高度重合。数据非常清楚：

- Position baseline bal_acc = 0.746（Section 4.5, Table 5）
- HS probe bal_acc = 0.740（同表）
- 差异 = -0.6pp，即 HS probe **不如**仅用 step index 的简单分类器

论文的 control task selectivity（14.4pp, Appendix E）看似证明了 "genuine safety structure"，但 selectivity 测的是 real labels vs. random labels 的差异，不是 real features vs. position features 的差异。一个主要编码位置信号的 probe 仍然会有高 selectivity（因为 position 与真实 label 有真实相关性）。

R1 建议 "在回归中加入位置特征作为控制变量" 是一个 minimal 且可行的修复方案，我支持这个建议。对 QwQ-32B 而言，当前证据只能支持 "HS probe achieves higher precision at the cost of later detection"，不能支持 "HS probe captures genuine safety structure beyond position"。

---

### Should-Fix 问题

**[AGREE] R1-W1: 32B 样本量统计功效不足**

同意，与我的 N3 一致。R1-32B coverage 25%（5/20 traces）意味着 lead time 和 precision 的 bootstrap 差异实际上只基于 5 个样本对。论文未报告效应量置信区间是一个重要遗漏。

补充：QwQ-32B n=19 test traces 同样受限。虽然 QwQ 在所有 15 个 window sizes 上都 pass HB（Section 4.5），但 19 条 trace 的 bootstrap CI 仍然很宽。论文应至少报告 precision 差异的 95% CI（Appendix C 的 OT-7B 有报告 CI [14.0, 29.6]，但主文 Table 3 未提供 32B 的 CI）。

---

**[AGREE] R1-W2: "四个互补指标收敛"夸大了独立性**

同意。论文自己在 Section 3.3 第 4 段承认了这一点："Precision and inverse FPR are mathematically related through false positives, and the additive composite includes the other three"。实质上：

- Precision 和 inverse FPR 共享 false positive 信息 → 1 个独立信号
- Additive composite = bal_acc + precision - FPR → 完全由前三者派生，0 个新信息
- 真正独立的收敛证据 = pure balanced accuracy + precision/FPR family ≈ 2 个信号

论文在声称 "four of five complementary metrics converge on deep layers" 时，使用 "complementary" 一词暗示了不存在的独立性。建议改为 "four alternative metrics, though partially correlated, all converge on deep layers"。

---

**[AGREE] R1-W3: Negative results framing 存在偏差**

同意，与我的 W4 一致。具体证据：

1. **RepE on QwQ-32B**：0.756 bal_acc > supervised LR 0.740（Section 4.6, Table 4 footnote a）。一个无监督方向估计法超过了有监督 probe，这不是 "failure"，这是 interesting positive result。论文将其归类为 negative result 是因为 RepE 在 R1-32B 上失败（0.559），但 per-model 的 mixed results 不等于 "fail"。
2. **BOCPD on R1-8B**：93% detection rate（Appendix G, Table 9）远超 simple threshold 的 65.1%。论文以 lead time 差（+3.5 vs +4.9 steps）将其判为失败，但在 coverage-critical 的部署场景中 BOCPD 优势明显。
3. **Cross-model transfer**：仅测试了 PCA + direct transfer（Section 4.6, Appendix H）。论文自己提到 "CCA, Procrustes rotation remain unexplored"（Introduction Contribution 3）。在未尝试更强方法的情况下声称 "cross-model transfer fails" 是 overstatement。

R1 的建议（区分 "fail" vs "produce mixed/limited results"）是合理的。

---

**[REBUT] R1-W4: 主实验缺少多种子报告**

不完全同意。L2-regularized logistic regression 在给定固定数据 split 和超参数后是**确定性**算法——不存在 seed 敏感性问题。论文使用固定的 60/20/20 split（Section 4.1），因此主实验结果是 reproducible 的。GRU 实验因 weight initialization 有随机性，论文在 Appendix E Table 7-8 中报告了 per-seed results。

R1 的真正关切应该是 **split sensitivity**（不同的 train/test 划分是否改变结论），而非 seed sensitivity。对此，bootstrap test 提供了部分 robustness evidence（1000 resamples），但 cross-validation 或 multiple random splits 会更有说服力。论文未做 k-fold cross-validation 是一个限制，但 "multi-seed" 这个表述对 LR 不适用。

不过，R1 提到的最弱测试 R1-8B FPR p=0.044（Appendix B, Table 2 rank 12）确实 margin 很小（threshold 0.05），不同 split 下有可能失败。这是一个合理的担忧，但解决方案应是报告 split robustness 而非 seed robustness。

---

**[AGREE] R1-W5: GRU split 差异**

完全同意，与我的 W3 一致。70/30 vs 60/20/20 的不同 split 使 GRU 与 LR 的直接对比不可靠（Appendix E 第 1 段明确说明了这一差异）。Appendix E Table 8 提供了 60/20/20 下的对比数据，但这与主文引用的 GRU 数字不一致，增加了理解难度。

---

### 缺失引用

**[AGREE]** LEACE / linear concept erasure (Belrose et al., 2023) 和 amnesic probing (Elazar et al., 2021) 是 probing methodology 的重要工作，与本文的 layer selection 讨论直接相关。Procrustes 对齐的原始文献在论文提到 "Procrustes rotation remain unexplored" 时确实应该引用。这些遗漏进一步支持了我在 W1 中指出的 related work 覆盖不足问题。

---

## 总结

在 R1 的 3 个 Must-Fix 中，我全部 AGREE（N1 维度混淆、N2 测试相关性误导、N3 QwQ 位置基线问题）。这三条与我自己的 N1、N2 高度重合，说明两位 reviewer 独立识别了相同的核心问题。

在 5 个 Should-Fix 中，我 AGREE 4 条（W1、W2、W3、W5），REBUT 1 条（W4 关于 multi-seed——LR 是确定性的，但 split sensitivity 是合理关切）。

**两位 reviewer 的共识核心问题**：384d text baseline 过弱导致 HS-text 对比的 claim 不可信，QwQ-32B 结果削弱主论点，32B 样本量不足。这三个问题如果不修复，论文的 Contribution 2 基本不成立。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2"
}
```

</details>

---


## Round 11

## Round 11

62 recorded events


### User

_source line 339 · 2026-05-18T01:36:44.989855+00:00_

[Round 1 审稿请求]:
你负责 **新颖性 + 完整性 + 写作质量** 的审查。

## 论文信息
- **标题**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
- **路径**: projects/contrastive_trace_safety/docs/paper/main.tex（各 section 在 sections/ 子目录）
- **目标 Venue**: EMNLP 2026 via ARR May cycle（Findings track）
- **Deadline**: 2026-05-25
- **格式要求**: ACL template `[review]`, double-blind, 8 pages + unlimited refs, Limitations section required, Responsible NLP Checklist required
- **匿名规则**: Double-blind，不能出现作者信息
- **评分标准 (EMNLP 2026 ARR)**: 5=Award(~2.5%), 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 你的审查重点

### 1. Novelty 评估（Findings track 标准）
- 核心贡献是 methodological finding（层选择影响结论）还是 empirical study（HS vs text comparison）？
- Layer selection sensitivity 作为贡献的推广价值：仅在安全 probing 中验证，Discussion 声称"any threshold-based detection study"——但改用 "We hypothesize" 是否足够？
- 与 TrajGuard、SafeSwitch、SIREN 等同期工作相比，增量贡献是什么？
- 对 Findings track 的 novelty 门槛是否达标？

### 2. Related Work 完整性
- 当前 31 篇引用是否覆盖核心领域：
  - Safety in reasoning models（self-jailbreak, CoT hijacking, unfaithful reasoning）
  - Hidden-state safety detection（alignment probing, refusal directions, TrajGuard, SafeSwitch, SIREN, SafeDream）
  - Probing methodology（Hewitt control tasks, LEACE, amnesic probing, layer-wise probing）
  - Change-point detection（BOCPD, CCS, RepE）
- 是否还有遗漏？特别关注 2025-2026 年的高相关论文
- Related Work 的 positioning 是否清晰——论文相对于已有工作的增量在哪里？

### 3. 叙事与 Framing 准确性
- Abstract：~190 words，是否在 150-250 范围内？是否回答了四个必答问题？是否仍有数据堆砌？
- Introduction 的 5 段叙事结构是否完整？从问题到贡献的逻辑链是否连贯？
- "Consistent HS advantage" claim vs QwQ-32B 的实际情况（position baseline > HS，lead time 负值）：Abstract/Intro 是否充分反映这一 caveat？
- Contribution 1-3 是否每条都有对应的 section/table 支撑？
- Negative results "produce inconsistent or limited results" 是否准确反映了 RepE-QwQ 的部分成功？

### 4. 写作质量（去 AI 痕迹）
- 检查 em-dash（—）和解释性 en-dash（–）使用
- 检查 -ing 短语结尾、过度分段、过渡词堆积
- Discussion 和 Conclusion 是否仍有内容重复？（历史 issue：Round 5 报告 0.3-0.5 页重复）
- 专有名词首次出现是否有定义？缩写是否在 Abstract 内定义？
- 用词黑名单："delve into", "leverage", "utilize", "facilitate", "a myriad of" 等

### 5. 格式与合规
- ACL template `[review]` 选项是否正确？
- Double-blind 匿名是否完整（无作者信息、无 deanonymizing URLs）？
- Limitations section 是否在 conclusion 之后、references 之前？
- Responsible NLP Checklist 是否完整且认真填写？
- 图表质量：字体大小、信息密度、caption 自包含

### 6. 历史 issue 验证（来自 review_issues.yaml 的 open items）
以下 Round 5 open issues 请重点检查是否已修复：
- **R5-N3**: QwQ position baseline > HS + 负 lead time 是否反映到 Abstract/Intro
- **R5-W2**: Negative results framing 是否从 "all fail" 改为更准确的表述
- **R5-W3**: Related Work 是否补充了 2024-2026 高相关论文
- **R5-W4**: Discussion/Conclusion 逐句对应重复是否消除
- **R5-W5**: Layer selection 泛化 claim 是否降级为 hypothesis
- **C6**: Related Work 引用量是否充足

请按 ARR 审稿标准给出完整审稿报告：Summary, Strengths, Weaknesses（严格评估），Questions, Missing References, Overall Assessment (使用 EMNLP 2026 评分标准), Detailed Comments。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-18T01:36:53.965493+00:00_

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
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
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

_source line 341 · 2026-05-18T01:36:54.016123+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-18T01:36:57.583942+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-18T01:36:58.236956+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{subcaption}
11	\usepackage{xcolor}
12	\usepackage{colortbl}
13	\usepackage{hyperref}
14	\usepackage{cleveref}
15	
16	\title{Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models}
17	
18	\author{Anonymous ARR Submission}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{sections/abstract}
25	\end{abstract}
26	
27	\input{sections/introduction}
28	
29	\input{sections/related_work}
30	
31	\input{sections/method}
32	
33	\input{sections/experiments}
34	
35	\input{sections/discussion}
36	
37	\input{sections/conclusion}
38	
39	\input{sections/limitations}
40	
41	\bibliography{references}
42	
43	\input{sections/appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-18T01:36:58.539019+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-18T01:36:58.740385+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-18T01:36:58.740935+00:00_

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
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-18T01:37:05.142701+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

I've found the search results for ACL ARR reviewer guidelines, review form, and scoring criteria. Here's what the current guidelines indicate for 2025-2026:

## Reviewer Scores

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores m
…[truncated 1213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6401
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-18T01:37:09.663686+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc.), and descriptions. Include soundness, excitement, overall assessment scales and any other rated dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc.), and descriptions. Include soundness, excitement, overall assessment scales and any other rated dimensions."
  }
}
```

</details>

---


### Tool call

_source line 349 · 2026-05-18T01:37:09.715104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 350 · 2026-05-18T01:37:10.019022+00:00_

1	Large Language Models (LLMs) with chain-of-thought (CoT) reasoning can self-jailbreak: their extended reasoning traces sometimes transition from safe deliberation to committed harmful generation. Detecting this \emph{safety commitment} in real time is essential for monitoring systems, yet no prior work has systematically compared hidden-state (HS) probes against text-based monitors for this task. We present the first cross-model evaluation of temporal probing for safety commitment detection across four reasoning models spanning two architectures (Llama, Qwen), two training methods (R1 distillation, STILL), and two scales (7--8B, 32B). Our primary methodological finding is that layer selection methodology can reverse a study's conclusions: the composite metric \texttt{bal\_acc $\times$ crossing\_rate} systematically selects shallow layers at 32B scale, entirely masking the hidden-state advantage. At correctly selected layers, HS probes significantly outperform text probes on all four models across all three metrics (12 tests, Holm-Bonferroni step-down correction, $\alpha{=}0.05$), with precision gains of +15 to +24 percentage points (pp) ($n{=}19$--$47$ test traces; $n{=}19$--$20$ at 32B scale), though with model-specific detection timing trade-offs at 32B scale. Temporal windowing universally improves both modalities, providing the most robust single default for safety monitoring. Seven alternative approaches (change-point detection, geometric distance, Representation Engineering, CCS, nonlinear probes, cross-model transfer via PCA projection and direct application) produce inconsistent or limited results, defining clear method boundaries. Control tasks confirm genuine safety-specific structure (selectivity 12.5--19.7pp above chance).
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 351 · 2026-05-18T01:37:10.119945+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 352 · 2026-05-18T01:37:10.572201+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Reasoning models such as DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq} scale inference-time computation through extended chains of thought (CoT). Recent work documents that these models can ``self-jailbreak'': without adversarial input modification, the CoT transitions from safety-aware deliberation to committed harmful generation~\cite{harmthoughts,selfjailbreak}. We define the first reasoning step after which safety deliberation permanently ceases as the \textbf{Safety Commitment Point} (CP). This failure mode differs qualitatively from adversarial jailbreaks on standard LLMs because the harmful transition originates within the model's own reasoning. Detecting this transition in real time is essential for monitoring systems that must intervene before harmful content reaches users.
4	
5	Existing safety detectors target fundamentally different problems. Hidden-state (HS) methods such as TrajGuard~\cite{trajguard} and SafeSwitch~\cite{safeswitch} classify adversarial inputs at the token level, while text monitors like SafeRemind~\cite{saferemind} scan generated reasoning for explicit violations. Neither tracks the gradual, multi-step commitment process. A fundamental question remains: should a monitoring system read the model's hidden states or its generated text? This comparison has never been conducted under controlled conditions. Na\"ive reasoning suggests HS features (up to 5120 dimensions) should dominate text embeddings (384d sentence encoder), but no prior work tests this systematically. A further complication is that HS probes require selecting which transformer layer to monitor, a choice rarely scrutinized but potentially decisive.
6	
7	We present the first systematic evaluation across four reasoning models spanning two architectures (Llama, Qwen) and two scales (7--8B, 32B). Our central finding is methodological: the choice of layer selection metric entirely determines whether an HS advantage is obser
…[truncated 1665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 353 · 2026-05-18T01:37:10.622890+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 354 · 2026-05-18T01:37:10.673647+00:00_

1	\section{Related Work}\label{sec:related-work}
2	
3	\paragraph{Safety in Reasoning Models.}
4	Reasoning models introduce a qualitatively new failure mode: the model's own chain of thought can transition from safety-aware deliberation to harmful generation without adversarial input modification~\cite{wang2025lrmsafety}. \citet{harmthoughts} document this self-jailbreak phenomenon with step-level annotations, while \citet{selfjailbreak} show that longer reasoning chains increase circumvention probability. \citet{hagendorff2026lrm_jailbreak} demonstrate that reasoning models can autonomously jailbreak other LLMs with 97\% success, identifying reasoning capability itself as a safety threat. H-CoT~\cite{hcot2025} shows reasoning chains can be externally hijacked, complementing internally-originating transitions. Unfaithful reasoning~\cite{chen2025unfaithful} further motivates hidden-state monitoring that bypasses text. On mitigation, SafeThink~\cite{safethink} steers early reasoning toward safety, SafeRemind~\cite{saferemind} inserts entropy-triggered reminders, and \citet{korbak2025cot_monitorability} argue that CoT monitorability is valuable but fragile. \citet{ahrend2026safer_traces} address information leakage in traces; \citet{hu2026refusal_dynamics} trace refusal dynamics in standard LLMs. None conducts a systematic modality comparison for commitment detection.
5	
6	\paragraph{Hidden-State Safety Detection.}
7	Internal activations can detect safety violations in standard LLMs. \citet{zhou2024alignment} show safety-relevant information distributes across layers, while \citet{qi2025shallow_alignment} find that alignment operates primarily over early output tokens. \citet{arditi2024refusal} identify a single refusal direction, but \citet{zhao2025harmfulness} show harmfulness and refusal are encoded separately. \citet{joad2026refusal_multi} reveal eleven category-specific refusal directions, and \citet{wollschlager2025geometry} formalize multi-dimensionality through 
…[truncated 2350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-18T01:37:16.548289+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: Quite sure; unlikely to have missed something affecting ratings
- **3**: Pretty sure, but chance of missing details or math verification
- **2**: Willing to defend evaluation, but fairly likely missed details
- **1**: Not my area or paper very hard to understand; educated guess

## 2. Soundness
Scale: 1-5 (with half-point increments)
- **5**: "This study is one of the most thorough I have seen"
- **4**: Strong; provides sufficient support with optional extra experiments
- **3**: Acceptable; supports main claims with minor details needed
- **2**: Poor; main claims lack sufficient support, major technical problems
- **1**: "Major Issues: This study is not yet sufficiently thorough"

## 3. Excitement
Scale: 1-5 (with half-point increments)
- **5**: Highly Exciting; would recommend to others
- **4**: Exciting; would mention to others
- **3**: Interesting; might mention or attend presentation
- **2**: Potentially Interesting; doesn't resonate personally
- **1**: Not Exciting; unlikely to resonate with community

## 4. Overall Assessment
Scale: 1-5 (with half-point increments)
- **5**: Consider for Award
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings acceptance
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## 5. Reproducibility
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with possible minor variations
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: Cannot reproduce results

## 6. Datasets & Software Value
Both use identical 1-5 scales assessing utility and impact for other researchers.

## 7. Author Identity Knowledge
Scale: 1-5, rangi
…[truncated 49 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6884
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-18T01:37:20.365731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-18T01:37:20.768366+00:00_

1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	\subsection{Safety Commitment Point}
5	\label{sec:commitment-point}
6	
7	When a reasoning model is jailbroken, its chain-of-thought (CoT) transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety reasoning permanently ceases. Steps before CP are \emph{pre-commitment} ($y_t = 0$); steps at or after CP are \emph{post-commitment} ($y_t = 1$). The detection task produces a score $s_t \in [0, 1]$ estimating whether the model has passed its CP by step $t$.
8	
9	We study four reasoning models spanning two architectures and two scales (\cref{tab:models}).
10	
11	\begin{table}[t]
12	\centering
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{lccccc}
15	\toprule
16	\textbf{Model} & \textbf{Arch.} & \textbf{Params} & \textbf{Layers} & \textbf{Hidden} & \textbf{$n$ (total\,/\,test)} \\
17	\midrule
18	R1-8B & Llama & 8B & 32 & 4096 & 209\,/\,43 \\
19	OT-7B & Qwen & 7B & 28 & 3584 & 228\,/\,47 \\
20	R1-32B & Qwen & 32B & 64 & 5120 & 100\,/\,20 \\
21	QwQ-32B & Qwen & 32B & 64 & 5120 & 95\,/\,19 \\
22	\bottomrule
23	\end{tabular}}
24	\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep{deepseekr1}; QwQ-32B~\citep{qwq} is a native reasoning model; OT-7B~\citep{openthinker} is trained with STILL~\citep{still} on Qwen2.5-7B. Data: HarmThoughts~\citep{harmthoughts} with step-level CP annotations. Split: 60/20/20.}
25	\label{tab:models}
26	\end{table}
27	
28	\subsection{Probe Architecture}
29	\label{sec:probe-architecture}
30	
31	\paragraph{Hidden-state (HS) probes.} At each step $t$, we extract the last-token hidden state $\mathbf{h}_t^{(\ell)} \in \mathbb{R}^d$ from layer $\ell$ and train an L2-regularized logistic regression classifier (balanced class weights, $C{=}1.0$, LBFGS, max\_iter${}=2000$) on binary CP labels. Layer selection is analyzed in \cref{sec:layer-sensitivity}
…[truncated 2620 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-18T01:37:20.769006+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-18T01:37:21.321641+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	We evaluate temporal probes across four reasoning models (\cref{tab:models}), comparing hidden-state (HS) and text modalities under different layer selection criteria.
4	
5	\subsection{Setup}\label{sec:setup}
6	
7	We study R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (Qwen-7B, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level CP annotations (60/20/20 split). HS probes extract last-token hidden states from a selected layer; text probes encode each step with all-MiniLM-L6-v2 (384d). Both use L2-regularized logistic regression with temporal windowing $W \in \{1, 3, 5, 10, 15, 20, 25\}$ selected on validation. Detection requires $K{=}5$ consecutive threshold crossings. Modality comparisons use a two-sided null-centered bootstrap (1000 resamples) with Holm-Bonferroni step-down correction (3 metrics $\times$ 4 models $= 12$ tests, $\alpha{=}0.05$). Within each model, the three metrics are positively correlated by construction, making the correction stricter than under independence.
8	
9	\subsection{Layer Selection Results}\label{sec:layer-results}
10	
11	\cref{tab:layer_selection} shows that the biased composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers for 32B models: L2 (3\% depth) for QwQ-32B and L10 (16\%) for R1-32B. Four unbiased metrics (pure balanced accuracy, precision, inverse FPR, additive composite) converge on deep layers: L60 (94\%) and L63 (98\%). Metrics from two measurement families (accuracy-based and false-positive-based) agree. The mechanism is that shallow layers produce more volatile representations, inflating crossing rate independently of discriminative power (\cref{sec:layer-sensitivity}).
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\begin{tabular}{lccc}
17	\toprule
18	\textbf{Model} & \textbf{Biased}$^a$
…[truncated 9170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-18T01:37:21.322119+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-18T01:37:21.875349+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Layer selection as researcher degree of freedom.}
4	Layer selection is an underexamined methodological choice in the probing literature that can silently determine a study's conclusions. Our five-metric ablation (\cref{sec:layer-results}) demonstrates that a single metric component, the crossing rate, reverses the central finding of an HS vs.\ text comparison: at biased layers, only 5 of 12 tests survive Holm-Bonferroni correction, producing an apparent scale-dependent modality effect; at corrected layers, HS probes are significant on all four models across all three metrics (12/12 tests pass). The mechanism is general: crossing rate rewards representational volatility at shallow layers independently of discriminative power, and any composite metric that incorporates threshold-crossing frequency is susceptible to the same bias mechanism, whose practical impact depends on the specific task and model depth. This bias is not specific to safety probing. We hypothesize that any threshold-based detection study that uses crossing rate as a layer selection criterion, whether for sentiment, factuality, or toxicity, could produce analogous reversals. Validation on other probing tasks is needed to confirm generality. We recommend that probing studies report results under at least two complementary layer selection criteria, and that five-metric ablations (or at minimum, results at multiple candidate layers spanning shallow, middle, and deep positions) become standard practice. Even among unbiased metrics, the choice between threshold-based and threshold-free criteria affects layer selection: AUROC peaks at mid-depth layers (${\sim}50\%$) while precision peaks at deep layers ($>90\%$), further demonstrating that layer selection methodology is a critical researcher degree of freedom. The cost of ablation is modest: evaluating five metrics across all layers adds minutes to an experiment that takes hours. The alternative 
…[truncated 4935 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-18T01:37:21.926084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-18T01:37:21.976824+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We present the first controlled comparison of hidden-state and text-based probes for safety commitment detection in reasoning models, evaluated across four models spanning two architectures and two scales.
4	The central finding is methodological: a composite layer selection metric incorporating crossing rate reverses the study's main conclusion at 32B scale, while metrics from two measurement families (accuracy-based and false-positive-based) converge on deep layers where HS probes significantly outperform text probes on all four models (Holm-Bonferroni correction, 12 tests, $\alpha{=}0.05$; precision +15.4 to +23.6pp).
5	Future work should close the 85.5\% oracle gap through causal intervention techniques, extend to multilingual and multi-turn settings, and explore stronger cross-model alignment methods beyond PCA-based transfer.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-18T01:37:27.366295+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-18T01:37:27.768276+00:00_

1	\section{Limitations}\label{sec:limitations}
2	
3	\paragraph{R1-32B statistical narrowness.}
4	Only $W{=}1$ passes Bonferroni correction for R1-32B, with only 25\% trace coverage (5 of 20 test traces detected). The dimensionality constraint of $51200 \times W$ features for $n{=}20$ traces prevents reliable evaluation at larger window sizes. Whether collecting more training traces would resolve this statistical limitation remains unknown.
5	
6	\paragraph{QwQ-32B timing limitation.}
7	On QwQ-32B, hidden-state probes achieve higher accuracy than text probes but detect commitment later: HS lead time is negative ($-1.2$ to $+1.9$ steps) compared to text lead time of $3.7$--$12.3$ steps. A position-only baseline achieves comparable balanced accuracy (0.746 vs.\ HS 0.740), suggesting that much of the detection signal on this model is positional rather than representational. The practical value of marginally higher accuracy with later detection depends on the deployment context.
8	
9	\paragraph{High safe-trace false positive rate.}
10	All probing methods produce high false positive rates on safe traces at standard operating thresholds (39--52\% across methods on R1-8B). Current probes characterize the commitment phenomenon as a research tool rather than constitute production-ready detectors. The 85.5\% oracle gap between passive monitoring and active intervention shows that early detection via passive probing captures only a fraction of the theoretically available safety signal.
11	
12	\paragraph{Scale and architecture coverage.}
13	We evaluate 4 models spanning 2 architectures (Qwen-2.5, LLaMA-3.1) and 2 parameter scales (7--8B, 32B). Intermediate scales (13B, 70B) that would test whether the observed layer-selection pattern interpolates smoothly are missing. We also lack evaluation on proprietary reasoning models (e.g., o1, o3), where chain-of-thought structure may differ substantially.
14	
15	\paragraph{Text encoder as baseline.}
16	Text probes use a single 384-dimensi
…[truncated 1021 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-18T01:37:27.768860+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-18T01:37:28.221385+00:00_

1	\appendix
2	
3	\section{Responsible NLP Research Checklist}
4	\label{app:checklist}
5	
6	We address the ARR Responsible NLP Research requirements below.
7	
8	\begin{itemize}
9	    \item \textbf{Limitations discussed:} Yes (\cref{sec:limitations}).
10	    \item \textbf{Potential risks:} This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark.
11	    \item \textbf{Computational budget:} Our experiments involve 4 models with 209, 228, 100, and 95 traces respectively (632 total), using linear probes and single-layer GRUs. Total compute is minimal (under 4 GPU-hours on a single RTX A6000). No large-scale pretraining or finetuning was performed.
12	    \item \textbf{Data:} We use HarmThoughts, a publicly available benchmark with step-level safety annotations. No new data collection was performed.
13	    \item \textbf{Human subjects:} No human subjects research was conducted.
14	    \item \textbf{Reproducibility:} All hyperparameters are reported in \cref{app:gru_details,app:bocpd_config}. Code and corrected data will be released upon publication.
15	\end{itemize}
16	
17	
18	\section{Layer Sweep Results}
19	\label{app:layer_sweep}
20	
21	For each model, we sweep all transformer layers and evaluate five candidate selection metrics: (1)~balanced accuracy $\times$ crossing rate (the biased composite), (2)~pure balanced accuracy, (3)~precision, (4)~inverse pre-CP FPR, and (5)~an additive composite. The biased composite systematically selects shallow layers for 32B models because early-layer representations exhibit higher crossing rates (more frequent threshold crossings) regardless of discriminative power. The four unbiased metrics converge on deep layers for all models.
22	
23	\paragraph{Selected layers.} R1-8B: all five metrics agree on layer~14 (44\% depth). OT-7B: biased m
…[truncated 38460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-18T01:37:28.623392+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-18T01:37:28.674046+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-18T01:37:33.191679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-18T01:37:33.644169+00:00_

1	@article{trajguard,
2	  title={TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense},
3	  author={Liu, Cheng and Liu, Xiaolei and Li, Xingyu and Xin, Bangzhou and Ding, Kangyi},
4	  journal={arXiv preprint arXiv:2604.07727},
5	  year={2026},
6	  url={https://arxiv.org/abs/2604.07727}
7	}
8	
9	@inproceedings{safeswitch,
10	  title={SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals},
11	  author={Han, Peixuan and Qian, Cheng and Chen, Xiusi and Zhang, Yuji and Ji, Heng and Zhang, Denghui},
12	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
13	  year={2025},
14	  url={https://arxiv.org/abs/2502.01042}
15	}
16	
17	@inproceedings{siren,
18	  title={LLM Safety From Within: Detecting Harmful Content with Internal Representations},
19	  author={Jiao, Difan and Liu, Yilun and Yuan, Ye and Tang, Zhenwei and Du, Linfeng and Wu, Haolun and Anderson, Ashton},
20	  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
21	  year={2026},
22	  url={https://arxiv.org/abs/2604.18519}
23	}
24	
25	@article{saferemind,
26	  title={How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs},
27	  author={Kim, Su-Hyeon and Jin, Hyundong and Lee, Yejin and Han, Yo-Sub},
28	  journal={arXiv preprint arXiv:2601.03662},
29	  year={2026},
30	  url={https://arxiv.org/abs/2601.03662}
31	}
32	
33	@article{safethink,
34	  title={Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away},
35	  author={Ghosal, Soumya Suvra and Chakraborty, Souradip and Singh, Vaibhav and Huang, Furong and Manocha, Dinesh and Bedi, Amrit Singh},
36	  journal={arXiv preprint arXiv:2602.11096},
37	  year={2026},
38	  url={https://arxiv.org/abs/2602.11096}
39	}
40	
41	@article{selfjailbreak,
42	  title={Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training},
43	
…[truncated 13250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-18T01:37:35.065811+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the full reviewer guidelines, especially: what reviewers should look for in novelty, soundness, excitement; how to assess Findings-track papers; what constitutes a good vs bad review; specific scoring guidance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the full reviewer guidelines, especially: what reviewers should look for in novelty, soundness, excitement; how to assess Findings-track papers; what constitutes a good vs bad review; specific scoring guidance."
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-18T01:37:42.799850+00:00_

# ARR Reviewer Guidelines: Core Assessment Principles

## Key Assessment Dimensions

ARR reviewers evaluate papers on three orthogonal scores:

**Soundness**: Technical validity and methodological rigor. Per guidelines, "The soundness scores must be justified by the text of the review." Low soundness without documented flaws indicates unconscious bias rather than legitimate critique.

**Excitement**: Personal interest independent of technical merit. This acknowledges that "preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper."

**Overall Recommendation**: A composite judgment balancing soundness, excitement, novelty, and potential impact—recognizing that significant contributions may lack personal appeal.

## What Makes Sound Research

Reviewers should verify:
- **Technical correctness** and complete, valid proofs
- **Appropriate scope** matching stated claims
- **Sufficient evidence** for assertions made (not speculative conclusions)
- **Statistical rigor** including significance testing and effect sizes
- **Reproducible details** enabling independent replication

## Common Reviewer Pitfalls (Heuristics to Avoid)

The guidelines identify 17 problematic reasoning patterns, including:

- Dismissing findings as "obvious in retrospect" (hindsight bias)
- Requiring SOTA results when papers claim other contributions
- Demanding unnecessary experiments beyond what claims require
- Imposing methodological preferences unrelated to the research question
- Penalizing acknowledged limitations as weaknesses

## Review Quality Standards

**Strong reviews are**:
- Specific with concrete examples and citations
- Professional in tone, avoiding sarcasm or dismissiveness
- Focused on evidence rather than preference
- Attentive to author responses during discussion periods

**Weak reviews**:
- Make vague assertions ("not clear," "missing details")
- Conflate personal taste with techn
…[truncated 366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7734
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-18T01:37:50.682388+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "hidden state probing safety detection reasoning models 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "hidden state probing safety detection reasoning models 2025 2026 arxiv"
  }
}
```

</details>

---


### Tool call

_source line 375 · 2026-05-18T01:37:51.034131+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"layer selection\" probing transformer sensitivity methodology 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"layer selection\" probing transformer sensitivity methodology 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 376 · 2026-05-18T01:37:58.374705+00:00_

Web search results for query: ""layer selection" probing transformer sensitivity methodology 2024 2025"

Links: [{"title":"arXiv:2507.05246v1 [cs.AI] 7 Jul 2025 2025-07-08","url":"https://arxiv.org/pdf/2507.05246"},{"title":"Next-Latent Prediction Transformers Learn Compact World Models","url":"https://arxiv.org/html/2511.05963v1"},{"title":"Inner Thinking Transformer: Leveraging Dynamic Depth ...","url":"https://aclanthology.org/2025.acl-long.1369.pdf"},{"title":"Power Transformer Prognostics and Health Management ...","url":"https://www.preprints.org/manuscript/202501.1113/v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2412.04703"},{"title":"Chapter 1: Transformer Interpretability - ARENA","url":"http://learn.arena.education/chapter1_transformer_interp/11_probing/intro/"},{"title":"Probing the limit of hydrologic predictability with the Transformer network | Earth & Environmental Systems Modeling","url":"https://eesm.science.energy.gov/publications/probing-limit-hydrologic-predictability-transformer-network"},{"title":"Transformers for Remote Sensing: A Systematic Review and Analysis - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11175147/"},{"title":"NORMALIZATION IN ATTENTION DYNAMICS Nikita Karagodin1 Shu Ge2 Yury Polyanskiy1","url":"https://people.lids.mit.edu/yp/homepage/data/2025_attn_normalization.pdf"},{"title":"A Review of Transformer-Based Models for Computer Vision Tasks: Capturing Global Context and Spatial Relationships","url":"https://arxiv.org/html/2408.15178v1"}]

Based on the search results, I found some relevant research on probing and transformer analysis from 2024-2025. Here are the key findings:

## Probing Methodology and Layer Selection

Recent research trains linear probes on the hidden states of frozen transformer models to analyze what information is captured at different layers and to predict future tokens. A layer sweep methodology is used to understand which layers best represent speci
…[truncated 1294 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7340
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-18T01:37:59.429665+00:00_

Web search results for query: "hidden state probing safety detection reasoning models 2025 2026 arxiv"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2603.17305v1"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/html/2504.05419v1"},{"title":"The Rogue Scalpel: Activation Steering Compromises LLM Safety","url":"https://arxiv.org/html/2509.22067v2"},{"title":"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/html/2605.13772"},{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification | OpenReview","url":"https://openreview.net/forum?id=O6I0Av7683"},{"title":"Artificial Intelligence","url":"https://arxiv.org/list/cs.AI/new"},{"title":"[2504.05419] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/abs/2504.05419"},{"title":"[2510.11529] Hallucination Detection via Internal States and Structured Reasoning Consistency in Large Language Models","url":"https://arxiv.org/abs/2510.11529"},{"title":"arXiv:2504.05419v1 [cs.AI] 7 Apr 2025","url":"https://arxiv.org/pdf/2504.05419"}]

The web search found several recent papers on arxiv related to hidden state probing, safety detection, and reasoning models from 2025-2026:

## Key Papers Found:

1. **CRAFT: Reasoning-Based Safety Alignment for Large Reasoning Models** (March 2026)
   - The paper addresses "superficial safety alignment" where large reasoning models generate unethical reasoning traces that may leak harmful information, even when the final response is safe.
   - CRAFT aligns reasoning at the latent level to avoid explicit harmful expressions and guide the reasoning process toward positive v
…[truncated 1623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8747
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-18T01:38:03.144955+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"reasoning model\" safety \"chain of thought\" jailbreak detection internal representation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"reasoning model\" safety \"chain of thought\" jailbreak detection internal representation 2026"
  }
}
```

</details>

---


### Tool call

_source line 379 · 2026-05-18T01:38:05.705523+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—|–",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—|–",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 380 · 2026-05-18T01:38:05.756946+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-18T01:38:11.377744+00:00_

Web search results for query: ""reasoning model" safety "chain of thought" jailbreak detection internal representation 2026"

Links: [{"title":"When Models Outthink Their Safety: Mitigating Self-Jailbreak in Large Reasoning Models with Chain-of-Guardrails","url":"https://arxiv.org/html/2510.21285v1"},{"title":"When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models","url":"https://arxiv.org/html/2510.21285v4"},{"title":"Automated Interpretability-Driven Model Auditing and Control: A Research Agenda","url":"https://aigi.ox.ac.uk/wp-content/uploads/2026/01/Automated_interp_Research_Agenda.pdf"},{"title":"[2501.19180] Enhancing Model Defense Against Jailbreaks with Proactive Safety Reasoning","url":"https://arxiv.org/abs/2501.19180"},{"title":"Chain-of-Thought Hijacking","url":"https://arxiv.org/html/2510.26418v1"},{"title":"AI Test: Leveraging Iteration to Extract Chain-of-Thought","url":"https://www.lumenova.ai/ai-experiments/frontier-ai-test-chain-of-thought-leak/"},{"title":"[2502.12893] H-CoT: Hijacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models, Including OpenAI o1/o3, DeepSeek-R1, and Gemini 2.0 Flash Thinking","url":"https://arxiv.org/abs/2502.12893"},{"title":"Reading GPT’s Mind — Analysis of Chain-of-Thought Monitorability as a Contingent and Fragile Opportunity for Mitigating Risks in Advanced AI Systems. | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/reading-gpts-mind-analysis-of-chain-of-thought-monitorability-as-a-contingent-and-fragile-aaa503ba21c5"},{"title":"H-CoT: Hijacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models, Including OpenAI o1/o3, DeepSeek-R1, and Gemini 2.0 Flash Thinking","url":"https://arxiv.org/html/2502.12893v1"},{"title":"(PDF) H-CoT: Hijacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models, Including OpenAI o1/o3, DeepSeek-R1, and Gemini 2.0 Flash 
…[truncated 2060 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8232
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-18T01:38:17.612276+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-18T01:38:18.064670+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:54:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:116:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex:12:\paragraph{Design implications for safety monitoring.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex:35:\paragraph{Temporal windowing.} For window size $W$, we concatenate features from steps $[t{-}W{+}1, \ldots, t]$. We evaluate $W \in \{1, 3, 5, 10, 15, 20, 25\}$ and select per-model on validation. GRU sequence models are also evaluated (\cref{app:gru_details}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex:13:We evaluate 4 models spanning 2 architectures (Qwen-2.5, LLaMA-3.1) and 2 parameter scales (7--8B, 32B). Intermediate scales (13B, 70B) that would test whether the observed layer-selection pattern interpolates smoothly are missing. We also lack evaluation on proprietary reasoning models (e.g., o1, o3), where chain-of-thought structure may differ substantially.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastiv
…[truncated 1662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-18T01:38:19.018541+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|Notably|It is worth noting",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally|Notably|It is worth noting",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-18T01:38:19.471274+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-18T01:38:20.475302+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "delve|leverage|utilize|facilitate|myriad|plethora",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "delve|leverage|utilize|facilitate|myriad|plethora",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-18T01:38:20.525961+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-18T01:38:27.416832+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", highlighting|, demonstrating|, indicating|, suggesting|, establishing|, confirming|, providing|, showing|, enabling|, making",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", highlighting|, demonstrating|, indicating|, suggesting|, establishing|, confirming|, providing|, showing|, enabling|, making",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-18T01:38:27.868923+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:56:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:60:R1-32B and QwQ-32B share the Qwen-32B architecture (64 layers, 5120 hidden) but present opposite detection profiles (\cref{tab:32b_divergence}), making training method the likely differentiator.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex:77:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex:33:\paragraph{Text probes.} Each step's text is encoded with all-MiniLM-L6-v2 ($\mathbb{R}^{384}$). The same logistic regression is applied, providing a surface-level modality baseline.
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex:52:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex:7:On QwQ-32B, hidden-state probes achieve higher accuracy than text probes but detect commitment later: HS lead time is negative ($-1.2$ to $+1.9$ steps) compared to text lead time of $3.7$--$12.3$ steps. A position-only baselin
…[truncated 2041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-18T01:38:28.019751+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-18T01:38:59.103042+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 38, \"total_citations\": 59, \"unique_cited_keys\": 38, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 32, \"online_not_found\": 5, \"online_mismatch\": 1}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"trajguard\", \"type\": \"article\", \"title\": \"TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense\", \"authors\": \"Liu, Cheng and Liu, Xiaolei and Li, Xingyu and Xin, Bangzhou and Ding, Kangyi\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.07727\"}, {\"key\": \"safeswitch\", \"type\": \"inproceedings\", \"title\": \"SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals\", \"authors\": \"Han, Peixuan and Qian, Cheng and Chen, Xiusi and Zhang, Yuji and Ji, Heng and Zh...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: EMNLP 2025\"}, {\"key\": \"siren\", \"type\": \"inproceedings\", \"title\": \"LLM Safety From Within: Detecting Harmful Content with Internal Representations\", \"authors\": \"Jiao, Difan and Liu, Yilun and Yuan, Ye and Tang, Zhenwei and Du, Linfeng and Wu...\", \"year\": \"2026\", \"venue\": \"Proceedings of the 64th Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"saferemind\", \"type\": \"article\", \"title\": \"How Does the Thinking Step Influence Model Safety? An Entropy-based Safety Reminder for LRMs\", \"authors\": \"Kim, Su-Hyeon and Jin, Hyundong and Lee, Yejin and Han, Yo-Sub\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2601.03662\"}, {\"key\": \"safethink\", \"type\": \"article\", \"title\": \"Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away\", \"authors\": \"Ghosal, Soumya Suvra and Chakraborty, Souradip and Singh, Vaibhav and Huang, Fur...\", \"year\": \"202
…[truncated 29886 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 31083
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-18T01:40:20.800832+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections && wc -w abstract.tex",
  "description": "Count words in abstract"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections && wc -w abstract.tex",
    "description": "Count words in abstract"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-18T01:40:21.102533+00:00_

220 abstract.tex
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_2_f461d57a

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-18T01:40:21.454797+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\\\\\bibliography",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\\\\\bibliography",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-18T01:40:21.555594+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-18T01:40:24.385565+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "bibliography",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "bibliography",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-18T01:40:24.486523+00:00_

41:\bibliography{references}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-18T01:42:29.551176+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告 (Round 1)\n\n**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models\n**Venue**: EMNLP 2026 via ARR (Findings track)\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 方法论发现（层选择敏感性）真实且有价值，但核心叙事对 QwQ-32B 的不利证据包装不足，novelty 偏窄，整体处于 Findings track 的可接受下限。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法严谨（Holm-Bonferroni, 控制任务, 维度匹配），但\"Consistent HS advantage\"的 framing 与 QwQ 实际表现存在张力；样本量小（n=19-47 test traces）|\n| Excitement | 2.5/5 | 方法论警示有用但不打开新研究方向；negative results 对领域有参考价值但 excitement 有限 |\n| Reproducibility | 4/5 | 超参数完整报告，数据集公开（HarmThoughts），代码承诺发布，计算量低（<4 GPU-hours）|\n| Reviewer Confidence | 4/5 | 仔细阅读了全文含附录，熟悉 probing methodology 和 safety 领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract/Introduction 对 QwQ-32B 不利证据的呈现严重不足（R5-N3 未充分修复）\n\n- 具体位置：abstract.tex L1（\"with model-specific detection timing trade-offs at 32B scale\"）; introduction.tex L13（\"Model-specific timing trade-offs qualify practical implications at 32B\"）\n- 问题：Abstract 和 Introduction 用极度模糊的语言（\"model-specific detection timing trade-offs\"）掩盖了三个关键事实：\n  1. QwQ-32B 的 position-only baseline 在 balanced accuracy 上与 HS 持平（0.746 vs 0.740, Table 4, Section 4.4）\n  2. QwQ-32B HS 的 lead time 为负值（−1.2 to +1.9 steps），意味着 HS 探针比 text 探针更晚检测到 commitment（Section 4.3 Caveats）\n  3. QwQ 的 position baseline margin 仅为 −0.6pp（Table 4）\n  \n  读完 Abstract + Introduction 的读者会得出\"HS 在所有四个模型上全面优于 text\"的印象。Contribution 2 直接写\"Consistent HS advantage at corrected layers\"，但\"consistent\"一词在 QwQ 的语境下是误导性的——统计显著性 ≠ 实用性优势。一个统计显著但 lead time 为负、与 position baseline 持平的结果，不应被包装为\"advantage\"。\n- 为什么影响接收：审稿人最敏感于 overclaimed results。如果读完全文才发现 Abstract/Intro 的 framing 与实验证据之间存在系统性偏差，会严重损害论文可信度。\n- 建议修改方向：\n  - Abstract 中 \"with model-specific detection timing trade-offs at 32B scale\" 应替换为更具信息量的描述，如 \"though one 32B model shows negative lead time and competitive position baselines, complicating practical deployment\"\n  - Contribution 2 从 \"Consistent HS advantage\" 改为 \"Statistically significant HS advantage with model-specific practical trade-offs\"\n  - Introduction 应用 1-2 句话明确描述 QwQ 的 position baseline 竞争力和 negative lead time\n\n**N2** [critical] BGE-large 编码器实验大幅削弱核心 claim，但 Abstract/Introduction 完全未提及\n\n- 具体位置：Appendix (app:encoder_robustness), Table in appendix\n- 问题：当 text encoder 从 MiniLM-384d 升级到 BGE-large-1024d 时，4 个模型中仅 1 个（OT-7B）的 HS 优势在 Holm-Bonferroni 校正后仍显著（+18.1pp, p<0.001）。其余 3 个模型的 effect sizes 大幅缩小且不再显著（R1-8B +5.8pp p=0.185; R1-32B +11.7pp p=0.027 不过 HB; QwQ +9.4pp p=0.132）。这意味着论文的核心 claim——\"HS probes significantly outperform text probes\"——在很大程度上依赖于选择了一个较弱的 384d text baseline。论文在 Limitations 中承认了这一点（\"Larger encoders... might narrow the observed HS-text accuracy gap\"），但这不仅是 Limitations 级别的 caveat，而是直接影响主要贡献（C2）可信度的证据。\n- 为什么影响接收：如果 HS 优势的主要来源是 text baseline 太弱而非 HS 真正携带更多信息，那么论文的核心叙事需要重新 framing。当前写法将最强反驳证据藏在附录中，审稿人会认为这是选择性呈现。\n- 建议修改方向：\n  - 正文 Section 4.3 的 dimensionality control 段落应整合 BGE-large 结果，明确说明：强编码器下 HS 优势方向一致但统计显著性大幅减弱\n  - Abstract 中 \"precision gains of +15 to +24pp\" 应注明这是对 MiniLM baseline 的结果\n  - 将核心 claim 调整为：HS 对弱 text baseline 有显著优势，对强 text baseline 仍有方向性优势但量级和显著性大幅降低\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Novelty 偏窄——层选择敏感性作为 standalone contribution 的推广价值有限\n\n- 问题：核心贡献是\"crossing rate 作为层选择指标在 32B 模型上会选出浅层，从而掩盖 HS 优势\"。这是一个有效的方法论警示，但：\n  1. 仅在安全 probing 的 4 个模型上验证，未在其他 probing 任务（sentiment, factuality, toxicity）上测试\n  2. Discussion 中已降级为 \"We hypothesize\"（R5-W5 已修复），但 title 将 \"Layer Selection Sensitivity\" 作为第一主题词，暗示了比实际更广的适用范围\n  3. 与 TrajGuard (2026)、SafeSwitch (EMNLP 2025)、SIREN (ACL 2026) 相比，本文不提出新的检测方法，而是提供了一个关于如何正确评估已有方法的 meta-level insight\n- 对 Findings track 而言：方法论 finding + negative results 的组合达到 Findings 的最低门槛，但不是 strong accept 级别的 novelty\n- 建议：如果能在 1-2 个非安全 probing 任务上验证层选择敏感性（即使是 toy experiment），会显著增强贡献的推广价值\n\n**W2** [warning] Negative results 的 framing 仍可更精确（R5-W2 部分修复）\n\n- 具体位置：abstract.tex（\"produce inconsistent or limited results\"）; introduction.tex L15; experiments.tex Section 4.6\n- 问题：当前 framing \"inconsistent or limited results\" 比之前更好，但仍将 7 种方法笼统归为一类。实际上：\n  - RepE on QwQ 达到 0.756 bal_acc（接近 supervised 的 0.778），只是 precision 差（0.512 vs 0.700）\n  - BOCPD on R1-8B 达到 93% detection rate（高于 simple threshold 的 65.1%），只是 lead time 差\n  - 这些并非\"失败\"，而是在特定维度上的 trade-off\n- 建议：将 \"produce inconsistent or limited results\" 改为更 nuanced 的表述，如 \"show task- or model-specific partial success without matching supervised probes on the primary precision criterion\"\n\n**W3** [warning] Related Work 引用基本充足但有几个显著遗漏\n\n- 具体位置：Section 2 (related_work.tex)\n- 当前 38 篇引用覆盖了主要类别，且组织结构清晰。但以下论文高度相关且缺失：\n  1. **\"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification\"** (arXiv 2504.05419, 2025)：在 reasoning model 上做 hidden-state probing 检测正确性，方法论几乎相同（linear probes on hidden states of reasoning models），是最直接的相关工作之一\n  2. **\"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry\"** (arXiv 2605.13772, 2026)：step-level hidden-state probing for detection in reasoning traces，与本文共享 \"step-level hidden-state temporal detection\" 的核心设计\n  3. **\"When Models Outthink Their Safety\" (Chain-of-Guardrails/COG)** (arXiv 2510.21285)：直接针对 reasoning model self-jailbreak 的防御方法\n  4. **\"Detecting Strategic Deception Using Linear Probes\"**：将 truth probing 扩展到欺骗检测，与本文的 probing methodology 直接相关\n- 这些遗漏中 #1 和 #2 尤为关键——审稿人很可能熟悉这些工作并注意到缺失\n- 建议：补充上述引用并在 Related Work 中 position 本文与它们的区别\n\n**W4** [warning] 样本量极小对统计推断的制约讨论不够充分\n\n- 具体位置：Table 1 (method.tex L24), Section 4.4\n- 问题：32B 模型的 test set 仅 n=19-20 traces。在 bootstrap (1000 resamples) 中，n=19 的 resampling 空间非常有限。Holm-Bonferroni 在小样本下虽然控制了 FWER，但 bootstrap CI 的覆盖率在 n<30 时可能偏低。论文未讨论：\n  1. bootstrap 在 n=19-20 下的有效性——Efron 的经验法则建议 n≥25 \n  2. 效应量的不确定性——+15.4pp precision difference 在 n=20 下的 CI 宽度\n  3. 是否做过 permutation test 作为 bootstrap 的 robustness check\n- 这不否定结果，但会让有统计方法论背景的审稿人产生疑虑\n- 建议：在 Limitations 或方法部分加入对小样本 bootstrap 有效性的简短讨论，或补充 permutation test 结果\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Abstract 中 \"$n{=}19$--$47$ test traces; $n{=}19$--$20$ at 32B scale\" 信息密度过高。Abstract 不需要报告具体样本量，可移至方法部分。\n- **M2**: abstract.tex 约 220 words（含 LaTeX markup），实际渲染可能在 185-195 words，在 150-250 范围内但偏上限。数字堆砌程度仍然较高（\"12 tests, Holm-Bonferroni step-down correction, α=0.05\" 对 abstract 而言过于技术化）。\n- **M3**: Discussion 段落 1（\"Layer selection as researcher degree of freedom\"）是全文最长的单个段落，约 15+ 句，建议拆分为 2 段（机制描述 + 推荐实践）。\n- **M4**: method.tex L33 \"providing a surface-level modality baseline\" 和 experiments.tex L60 \"making training method the likely differentiator\" 是轻微的 -ing 短语结尾，可改写但不严重。\n- **M5**: Responsible NLP Checklist (app:checklist) 较为简略。\"Potential risks\" 一项仅说\"We do not develop new attack methods\"，但未讨论该研究可能被用于反向工程安全机制的风险。建议更详细地讨论 dual-use 问题。\n- **M6**: references.bib 中 `burns2023discovering` 标注为 2023 但 OpenAlex 匹配到 2022 年版本；`alain2017understanding` 标注 2017 但 OpenAlex 匹配 2016。年份应以出版版本为准核实。\n- **M7**: Appendix B (Holm-Bonferroni table) 的 caption 放在表格上方（`\\caption` before `\\begin{tabular}`），但 Appendix E (BOCPD sweep) 的 caption 也在上方——两者一致，没有问题。但如果与正文表格的 caption 位置不统一，建议统一。\n\n---\n\n## 历史 Issue 验证\n\n| Issue | 状态 | 评价 |\n|-------|------|------|\n| R5-N3: QwQ position baseline > HS + 负 lead time 是否反映到 Abstract/Intro | **未充分修复** | Abstract 用 \"model-specific detection timing trade-offs\" 一笔带过，Introduction 同样模糊。具体数值和含义仍仅出现在 Section 4.3-4.4。见 N1。|\n| R5-W2: Negative results framing | **部分修复** | 从 \"all fail\" 改为 \"inconsistent or limited results\"，更准确但仍可更 nuanced。见 W2。|\n| R5-W3: Related Work 补充 2024-2026 高相关论文 | **部分修复** | 新增了 SafeDream (2026), SIREN (2026), hu2026, ahrend2026 等，但仍缺少几篇高度相关的 hidden-state probing on reasoning models 论文。见 W3。|\n| R5-W4: Discussion/Conclusion 重复 | **已修复** | Conclusion 已压缩为 3 句话，与 Discussion 无逐句重复。|\n| R5-W5: Layer selection 泛化 claim 降级为 hypothesis | **已修复** | Discussion 明确使用 \"We hypothesize\" 并注明 \"Validation on other probing tasks is needed to confirm generality\"。|\n| C6: Related Work 引用量 | **部分修复** | 从之前的 ~31 篇增至 38 篇，涵盖主要领域，但几个关键遗漏仍存在。见 W3。|\n\n---\n\n## Missing References\n\n1. **Stechly et al. (2025)** \"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification\" — arXiv 2504.05419. 在 reasoning model 上做 hidden-state probing，方法论与本文高度相似，是必须引用的直接相关工作。\n2. **\"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry\"** (2026) — arXiv 2605.13772. Step-level hidden-state analysis for detection in reasoning traces。\n3. **\"When Models Outthink Their Safety: Mitigating Self-Jailbreak in Large Reasoning Models with Chain-of-Guardrails\"** — arXiv 2510.21285. 直接针对 self-jailbreak 的防御。\n4. **\"Enhancing Model Defense Against Jailbreaks with Proactive Safety Reasoning\" (SCoT)** — arXiv 2501.19180.\n\n---\n\n## 主要优势\n\n1. **实验方法论严谨**：Holm-Bonferroni 12-test 校正、控制任务、PCA 维度匹配、BGE-large 编码器 robustness check 构成了一个多层验证体系，远超该领域多数 empirical study 的标准。\n2. **层选择敏感性发现有实际价值**：crossing rate 偏差机制的识别和五指标消融是一个可复用的方法论贡献，尽管尚未在安全 probing 以外验证。\n3. **负面结果的系统报告**：7 种替代方法的详细失败分析（特别是 RepE 的 precision 问题和 BOCPD 的 gradual transition 问题）对后续研究者有直接参考价值。\n4. **Bug 披露和透明度**：Appendix F 的 M002 bug disclosure 展示了良好的科学诚信实践，在 ML 论文中非常少见。\n5. **写作质量总体良好**：无 em-dash、无用词黑名单词汇、无 \"Furthermore/Moreover\" 堆积、无过度分段。Discussion/Conclusion 重复问题已解决。技术写作精确度高。\n6. **Limitations 部分诚实全面**：7 个具体限制逐一列出，包括 QwQ timing limitation、high FPR、single dataset 等，没有回避核心弱点。\n\n---\n\n## 最终评估\n\n这篇论文在方法论严谨性上表现突出，层选择敏感性是一个真实且有用的发现。但存在两个影响评分的核心问题：(1) Abstract/Introduction 对 QwQ-32B 不利证据的呈现远不够透明，构成了系统性的 framing bias；(2) BGE-large 实验表明 HS 优势在很大程度上依赖弱 text baseline，但这一关键证据被藏在附录中。如果这两个问题在正文中得到坦诚呈现，论文的可信度会显著提升，即使 claim 变得更温和。\n\n对 Findings track 而言，方法论 finding + negative results + 诚实的 limitations 的组合达到了接受门槛（3.0），但 framing 问题如果未修复，有被降至 2.5（Borderline Findings）的风险。\n\n**Overall Assessment: 3.0 (Findings)**\n",
  "reviewer_id": "2",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告 (Round 1)\n\n**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models\n**Venue**: EMNLP 2026 via ARR (Findings track)\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 方法论发现（层选择敏感性）真实且有价值，但核心叙事对 QwQ-32B 的不利证据包装不足，novelty 偏窄，整体处于 Findings track 的可接受下限。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法严谨（Holm-Bonferroni, 控制任务, 维度匹配），但\"Consistent HS advantage\"的 framing 与 QwQ 实际表现存在张力；样本量小（n=19-47 test traces）|\n| Excitement | 2.5/5 | 方法论警示有用但不打开新研究方向；negative results 对领域有参考价值但 excitement 有限 |\n| Reproducibility | 4/5 | 超参数完整报告，数据集公开（HarmThoughts），代码承诺发布，计算量低（<4 GPU-hours）|\n| Reviewer Confidence | 4/5 | 仔细阅读了全文含附录，熟悉 probing methodology 和 safety 领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract/Introduction 对 QwQ-32B 不利证据的呈现严重不足（R5-N3 未充分修复）\n\n- 具体位置：abstract.tex L1（\"with model-specific detection timing trade-offs at 32B scale\"）; introduction.tex L13（\"Model-specific timing trade-offs qualify practical implications at 32B\"）\n- 问题：Abstract 和 Introduction 用极度模糊的语言（\"model-specific detection timing trade-offs\"）掩盖了三个关键事实：\n  1. QwQ-32B 的 position-only baseline 在 balanced accuracy 上与 HS 持平（0.746 vs 0.740, Table 4, Section 4.4）\n  2. QwQ-32B HS 的 lead time 为负值（−1.2 to +1.9 steps），意味着 HS 探针比 text 探针更晚检测到 commitment（Section 4.3 Caveats）\n  3. QwQ 的 position baseline margin 仅为 −0.6pp（Table 4）\n  \n  读完 Abstract + Introduction 的读者会得出\"HS 在所有四个模型上全面优于 text\"的印象。Contribution 2 直接写\"Consistent HS advantage at corrected layers\"，但\"consistent\"一词在 QwQ 的语境下是误导性的——统计显著性 ≠ 实用性优势。一个统计显著但 lead time 为负、与 position baseline 持平的结果，不应被包装为\"advantage\"。\n- 为什么影响接收：审稿人最敏感于 overclaimed results。如果读完全文才发现 Abstract/Intro 的 framing 与实验证据之间存在系统性偏差，会严重损害论文可信度。\n- 建议修改方向：\n  - Abstract 中 \"with model-specific detection timing trade-offs at 32B scale\" 应替换为更具信息量的描述，如 \"though one 32B model shows negative lead time and competitive position baselines, complicating practical deployment\"\n  - Contribution 2 从 \"Consistent HS advantage\" 改为 \"Statistically significant HS advantage with model-specific practical trade-offs\"\n  - Introduction 应用 1-2 句话明确描述 QwQ 的 position baseline 竞争力和 negative lead time\n\n**N2** [critical] BGE-large 编码器实验大幅削弱核心 claim，但 Abstract/Introduction 完全未提及\n\n- 具体位置：Appendix (app:encoder_robustness), Table in appendix\n- 问题：当 text encoder 从 MiniLM-384d 升级到 BGE-large-1024d 时，4 个模型中仅 1 个（OT-7B）的 HS 优势在 Holm-Bonferroni 校正后仍显著（+18.1pp, p<0.001）。其余 3 个模型的 effect sizes 大幅缩小且不再显著（R1-8B +5.8pp p=0.185; R1-32B +11.7pp p=0.027 不过 HB; QwQ +9.4pp p=0.132）。这意味着论文的核心 claim——\"HS probes significantly outperform text probes\"——在很大程度上依赖于选择了一个较弱的 384d text baseline。论文在 Limitations 中承认了这一点（\"Larger encoders... might narrow the observed HS-text accuracy gap\"），但这不仅是 Limitations 级别的 caveat，而是直接影响主要贡献（C2）可信度的证据。\n- 为什么影响接收：如果 HS 优势的主要来源是 text baseline 太弱而非 HS 真正携带更多信息，那么论文的核心叙事需要重新 framing。当前写法将最强反驳证据藏在附录中，审稿人会认为这是选择性呈现。\n- 建议修改方向：\n  - 正文 Section 4.3 的 dimensionality control 段落应整合 BGE-large 结果，明确说明：强编码器下 HS 优势方向一致但统计显著性大幅减弱\n  - Abstract 中 \"precision gains of +15 to +24pp\" 应注明这是对 MiniLM baseline 的结果\n  - 将核心 claim 调整为：HS 对弱 text baseline 有显著优势，对强 text baseline 仍有方向性优势但量级和显著性大幅降低\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Novelty 偏窄——层选择敏感性作为 standalone contribution 的推广价值有限\n\n- 问题：核心贡献是\"crossing rate 作为层选择指标在 32B 模型上会选出浅层，从而掩盖 HS 优势\"。这是一个有效的方法论警示，但：\n  1. 仅在安全 probing 的 4 个模型上验证，未在其他 probing 任务（sentiment, factuality, toxicity）上测试\n  2. Discussion 中已降级为 \"We hypothesize\"（R5-W5 已修复），但 title 将 \"Layer Selection Sensitivity\" 作为第一主题词，暗示了比实际更广的适用范围\n  3. 与 TrajGuard (2026)、SafeSwitch (EMNLP 2025)、SIREN (ACL 2026) 相比，本文不提出新的检测方法，而是提供了一个关于如何正确评估已有方法的 meta-level insight\n- 对 Findings track 而言：方法论 finding + negative results 的组合达到 Findings 的最低门槛，但不是 strong accept 级别的 novelty\n- 建议：如果能在 1-2 个非安全 probing 任务上验证层选择敏感性（即使是 toy experiment），会显著增强贡献的推广价值\n\n**W2** [warning] Negative results 的 framing 仍可更精确（R5-W2 部分修复）\n\n- 具体位置：abstract.tex（\"produce inconsistent or limited results\"）; introduction.tex L15; experiments.tex Section 4.6\n- 问题：当前 framing \"inconsistent or limited results\" 比之前更好，但仍将 7 种方法笼统归为一类。实际上：\n  - RepE on QwQ 达到 0.756 bal_acc（接近 supervised 的 0.778），只是 precision 差（0.512 vs 0.700）\n  - BOCPD on R1-8B 达到 93% detection rate（高于 simple threshold 的 65.1%），只是 lead time 差\n  - 这些并非\"失败\"，而是在特定维度上的 trade-off\n- 建议：将 \"produce inconsistent or limited results\" 改为更 nuanced 的表述，如 \"show task- or model-specific partial success without matching supervised probes on the primary precision criterion\"\n\n**W3** [warning] Related Work 引用基本充足但有几个显著遗漏\n\n- 具体位置：Section 2 (related_work.tex)\n- 当前 38 篇引用覆盖了主要类别，且组织结构清晰。但以下论文高度相关且缺失：\n  1. **\"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification\"** (arXiv 2504.05419, 2025)：在 reasoning model 上做 hidden-state probing 检测正确性，方法论几乎相同（linear probes on hidden states of reasoning models），是最直接的相关工作之一\n  2. **\"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry\"** (arXiv 2605.13772, 2026)：step-level hidden-state probing for detection in reasoning traces，与本文共享 \"step-level hidden-state temporal detection\" 的核心设计\n  3. **\"When Models Outthink Their Safety\" (Chain-of-Guardrails/COG)** (arXiv 2510.21285)：直接针对 reasoning model self-jailbreak 的防御方法\n  4. **\"Detecting Strategic Deception Using Linear Probes\"**：将 truth probing 扩展到欺骗检测，与本文的 probing methodology 直接相关\n- 这些遗漏中 #1 和 #2 尤为关键——审稿人很可能熟悉这些工作并注意到缺失\n- 建议：补充上述引用并在 Related Work 中 position 本文与它们的区别\n\n**W4** [warning] 样本量极小对统计推断的制约讨论不够充分\n\n- 具体位置：Table 1 (method.tex L24), Section 4.4\n- 问题：32B 模型的 test set 仅 n=19-20 traces。在 bootstrap (1000 resamples) 中，n=19 的 resampling 空间非常有限。Holm-Bonferroni 在小样本下虽然控制了 FWER，但 bootstrap CI 的覆盖率在 n<30 时可能偏低。论文未讨论：\n  1. bootstrap 在 n=19-20 下的有效性——Efron 的经验法则建议 n≥25 \n  2. 效应量的不确定性——+15.4pp precision difference 在 n=20 下的 CI 宽度\n  3. 是否做过 permutation test 作为 bootstrap 的 robustness check\n- 这不否定结果，但会让有统计方法论背景的审稿人产生疑虑\n- 建议：在 Limitations 或方法部分加入对小样本 bootstrap 有效性的简短讨论，或补充 permutation test 结果\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Abstract 中 \"$n{=}19$--$47$ test traces; $n{=}19$--$20$ at 32B scale\" 信息密度过高。Abstract 不需要报告具体样本量，可移至方法部分。\n- **M2**: abstract.tex 约 220 words（含 LaTeX markup），实际渲染可能在 185-195 words，在 150-250 范围内但偏上限。数字堆砌程度仍然较高（\"12 tests, Holm-Bonferroni step-down correction, α=0.05\" 对 abstract 而言过于技术化）。\n- **M3**: Discussion 段落 1（\"Layer selection as researcher degree of freedom\"）是全文最长的单个段落，约 15+ 句，建议拆分为 2 段（机制描述 + 推荐实践）。\n- **M4**: method.tex L33 \"providing a surface-level modality baseline\" 和 experiments.tex L60 \"making training method the likely differentiator\" 是轻微的 -ing 短语结尾，可改写但不严重。\n- **M5**: Responsible NLP Checklist (app:checklist) 较为简略。\"Potential risks\" 一项仅说\"We do not develop new attack methods\"，但未讨论该研究可能被用于反向工程安全机制的风险。建议更详细地讨论 dual-use 问题。\n- **M6**: references.bib 中 `burns2023discovering` 标注为 2023 但 OpenAlex 匹配到 2022 年版本；`alain2017understanding` 标注 2017 但 OpenAlex 匹配 2016。年份应以出版版本为准核实。\n- **M7**: Appendix B (Holm-Bonferroni table) 的 caption 放在表格上方（`\\caption` before `\\begin{tabular}`），但 Appendix E (BOCPD sweep) 的 caption 也在上方——两者一致，没有问题。但如果与正文表格的 caption 位置不统一，建议统一。\n\n---\n\n## 历史 Issue 验证\n\n| Issue | 状态 | 评价 |\n|-------|------|------|\n| R5-N3: QwQ position baseline > HS + 负 lead time 是否反映到 Abstract/Intro | **未充分修复** | Abstract 用 \"model-specific detection timing trade-offs\" 一笔带过，Introduction 同样模糊。具体数值和含义仍仅出现在 Section 4.3-4.4。见 N1。|\n| R5-W2: Negative results framing | **部分修复** | 从 \"all fail\" 改为 \"inconsistent or limited results\"，更准确但仍可更 nuanced。见 W2。|\n| R5-W3: Related Work 补充 2024-2026 高相关论文 | **部分修复** | 新增了 SafeDream (2026), SIREN (2026), hu2026, ahrend2026 等，但仍缺少几篇高度相关的 hidden-state probing on reasoning models 论文。见 W3。|\n| R5-W4: Discussion/Conclusion 重复 | **已修复** | Conclusion 已压缩为 3 句话，与 Discussion 无逐句重复。|\n| R5-W5: Layer selection 泛化 claim 降级为 hypothesis | **已修复** | Discussion 明确使用 \"We hypothesize\" 并注明 \"Validation on other probing tasks is needed to confirm generality\"。|\n| C6: Related Work 引用量 | **部分修复** | 从之前的 ~31 篇增至 38 篇，涵盖主要领域，但几个关键遗漏仍存在。见 W3。|\n\n---\n\n## Missing References\n\n1. **Stechly et al. (2025)** \"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification\" — arXiv 2504.05419. 在 reasoning model 上做 hidden-state probing，方法论与本文高度相似，是必须引用的直接相关工作。\n2. **\"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry\"** (2026) — arXiv 2605.13772. Step-level hidden-state analysis for detection in reasoning traces。\n3. **\"When Models Outthink Their Safety: Mitigating Self-Jailbreak in Large Reasoning Models with Chain-of-Guardrails\"** — arXiv 2510.21285. 直接针对 self-jailbreak 的防御。\n4. **\"Enhancing Model Defense Against Jailbreaks with Proactive Safety Reasoning\" (SCoT)** — arXiv 2501.19180.\n\n---\n\n## 主要优势\n\n1. **实验方法论严谨**：Holm-Bonferroni 12-test 校正、控制任务、PCA 维度匹配、BGE-large 编码器 robustness check 构成了一个多层验证体系，远超该领域多数 empirical study 的标准。\n2. **层选择敏感性发现有实际价值**：crossing rate 偏差机制的识别和五指标消融是一个可复用的方法论贡献，尽管尚未在安全 probing 以外验证。\n3. **负面结果的系统报告**：7 种替代方法的详细失败分析（特别是 RepE 的 precision 问题和 BOCPD 的 gradual transition 问题）对后续研究者有直接参考价值。\n4. **Bug 披露和透明度**：Appendix F 的 M002 bug disclosure 展示了良好的科学诚信实践，在 ML 论文中非常少见。\n5. **写作质量总体良好**：无 em-dash、无用词黑名单词汇、无 \"Furthermore/Moreover\" 堆积、无过度分段。Discussion/Conclusion 重复问题已解决。技术写作精确度高。\n6. **Limitations 部分诚实全面**：7 个具体限制逐一列出，包括 QwQ timing limitation、high FPR、single dataset 等，没有回避核心弱点。\n\n---\n\n## 最终评估\n\n这篇论文在方法论严谨性上表现突出，层选择敏感性是一个真实且有用的发现。但存在两个影响评分的核心问题：(1) Abstract/Introduction 对 QwQ-32B 不利证据的呈现远不够透明，构成了系统性的 framing bias；(2) BGE-large 实验表明 HS 优势在很大程度上依赖弱 text baseline，但这一关键证据被藏在附录中。如果这两个问题在正文中得到坦诚呈现，论文的可信度会显著提升，即使 claim 变得更温和。\n\n对 Findings track 而言，方法论 finding + negative results + 诚实的 limitations 的组合达到了接受门槛（3.0），但 framing 问题如果未修复，有被降至 2.5（Borderline Findings）的风险。\n\n**Overall Assessment: 3.0 (Findings)**\n",
    "reviewer_id": "2",
    "project": "contrastive_trace_safety"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-18T01:42:33.618805+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4067
}
```

</details>

---


### Assistant

_source line 400 · 2026-05-18T01:42:42.825773+00:00_

审稿报告已提交给 Review Director。

报告核心结论：**Overall 3.0 (Findings)**。

两个 Must-Fix 问题：
1. **N1**: Abstract/Intro 对 QwQ-32B 的不利证据（负 lead time、position baseline 持平）用 "model-specific timing trade-offs" 一笔带过，构成 framing bias。Contribution 2 的 "Consistent HS advantage" 措辞在 QwQ 语境下有误导性。
2. **N2**: BGE-large (1024d) 编码器实验中 4 个模型仅 1 个通过 HB 校正，核心 HS 优势很大程度依赖弱 text baseline，但此关键证据仅在附录中呈现。

四个 Should-Fix：novelty 偏窄（W1）、negative results framing 可更精确（W2）、缺少几篇高度相关引用如 "Probing Hidden States for Self-Verification" 和 "Step-Level Hallucination Detection via Hidden-State Transport Geometry"（W3）、小样本 bootstrap 有效性讨论不足（W4）。

历史 issues 中 R5-W4（Discussion/Conclusion 重复）和 R5-W5（泛化 claim 降级）已修复；R5-N3（QwQ caveat）和 R5-W3（Related Work 补充）仅部分修复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2"
}
```

</details>

---


## Round 12

## Round 12

12 recorded events


### User

_source line 401 · 2026-05-18T01:44:05.299886+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个观点标注 **[AGREE]** 并说明理由，或 **[REBUT]** 并提供具体证据（cite 论文中的 Section/Table/Figure）。

---

# Reviewer 1 审稿报告（Round 1）

**Overall**: 3.0 (Findings)

## Must-Fix 问题

**N1** [critical] 12/12 Holm-Bonferroni 呈现给出独立性错觉（R5-N2 未修复）
- 全文多处强调 "12/12 tests pass"，给读者 12 条独立证据的印象。但 3 个 metrics 正相关，有效独立确认数约 4-8。
- HB 在正相关下确实控制 FWER（更保守），但 "12/12 pass" 的修辞效果远超实际含义。
- 建议：改为 "all 4 models × 3 correlated metrics"，明确有效独立性。

**N2** [critical] 32B 模型效应量缺失 95% CI（R5-W1 未修复）
- Table 2 报告 Δ 值但无 95% bootstrap CI。n=19-20 下 CI 对评估效应量可靠性至关重要。
- 仅 Appendix E (OT-7B) 给出 CI [14.0, 29.6]。
- 建议：Table 2 增加 95% CI 列。

**N3** [critical] BGE-large 结果（1/4 显著）实质性削弱 HS advantage 但主文讨论不充分
- BGE-large (1024d) 替换 MiniLM (384d) 后，仅 OT-7B 显著（+18.1pp, p<0.001, 过 HB）。R1-8B p=0.185, R1-32B p=0.027（不过 HB）, QwQ p=0.132。
- 主文仅一句带过（"effect sizes narrow"），将详细数据放附录。
- 核心 claim 的普适性如果取决于弱 baseline，claim scope 需重新限定。
- 建议：主文用至少一段正面讨论；claim 调整为 "HS significantly outperforms a 384d encoder; with stronger encoders, advantage narrows and becomes model-dependent"。

## Should-Fix 问题

**W1** [warning] "四个互补指标收敛"实质独立性 ≈ 2（R5-W6 未修复）
- Precision 和 inverse FPR 数学上高度耦合。Additive composite 增加冗余。
- 建议：改为 "metrics from two complementary families"，量化 rank correlation。

**W2** [warning] PCA-384d 控制实验未报告哪 2/12 测试失败
- 10/12 通过但不知哪个 model×metric 失败。方差保留 79-92% 意味着判别信号可能在 minor components 中。
- 建议：报告失败测试的具体组合。

**W3** [warning] R1-32B W=1 significance 基于 5 个 detected traces
- Coverage=25%（5/20），基于 5 样本的 precision 有极大抽样方差。
- 建议：报告 5-trace precision 的 bootstrap CI，讨论 C=1.0 在 p>>n 下的适当性。

**W4** [warning] QwQ-32B position baseline 竞争力问题
- Position-only baseline 在 bal_acc 上击败 HS probe（0.705 vs 0.667）。
- "All four models" 掩盖了 QwQ 的 HS 优势主要在 precision 而非 accuracy。
- 建议：在主文中直接说明，限定 "HS advantage on all four models" 内涵。

**W5** [warning] 不同实验方法使用不同数据划分
- 60/20/20 vs 70/30 vs merged，跨方法比较时未标注差异。
- 建议：每次跨方法比较时标注数据划分。

**W6** [warning] AUROC 选择中层而非深层，被轻描淡写
- AUROC 是最标准的 threshold-free 指标，选中层 (~50% depth) 而非深层。
- 论文以 "层选择方法论" 为核心贡献，但对 AUROC 不同意见的分析不够深入。
- 建议：报告 AUROC 层处的 HS vs text 对比，讨论分歧机理。

**W7** [warning] Negative results framing 过于笼统
- BOCPD 93% detection, RepE QwQ 0.756 bal_acc 被 blanket framing 掩盖。
- 建议：改为 "no alternative method achieves consistent cross-model performance"。

## 小问题
- Abstract 中 n=19-47 后分号连接 n=19-20 给人两组数据感
- Section 3.5 和 4.1 bootstrap/HB 描述重复
- Appendix G control task 有部分重复段落

## 主要优势
1. 层选择敏感性发现有重要方法论价值
2. 实验覆盖面好（4 模型，2 架构，2 训练方法，2 规模）
3. 透明度高（bug disclosure, control task, position baseline, negative results）
4. Temporal windowing 分析全面
5. 问题定义清晰

## 历史 Issue 验证
- R5-N1: 部分修复
- R5-N2: **未修复** → 本轮 N1
- R5-W1: **未修复** → 本轮 N2
- R5-W6: **未修复** → 本轮 W1

---

请逐条回应 N1-N3, W1-W7, 以及小问题部分。对每个观点给出 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-18T01:44:12.550904+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
  "offset": "46",
  "limit": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex",
    "offset": "46",
    "limit": "12"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-18T01:44:13.504852+00:00_

46	\bottomrule
47	\end{tabular}
48	\caption{HS vs.\ text at corrected layers. $\Delta$: HS$-$text difference (pp). HB: Holm-Bonferroni pass count ($\alpha{=}0.05$, 12 tests). Bootstrap: 1000 resamples, two-sided null-centered.}
49	\label{tab:hs_vs_text}
50	\end{table}
51	
52	HS probes significantly outperform text probes on all four models across all three metrics (\cref{tab:hs_vs_text}). Precision gains range from +15.4pp (R1-32B) to +23.6pp (QwQ-32B). The advantage is consistent across architectures (Llama vs.\ Qwen) and training methods (R1 distillation vs.\ STILL). Control task selectivity confirms genuine safety signal: 12.5--19.7pp above chance across all models (\cref{app:control}).
53	
54	\paragraph{Dimensionality control.} PCA reduction of HS features to 384d (matching text encoder dimensionality, 79--92\% variance retained) preserves the precision advantage on all four models (+16.8 to +23.1pp, all $p{<}0.012$), with 10/12 Holm-Bonferroni tests passing. This confirms a modality effect rather than a capacity artifact. As a complementary robustness check, we replace MiniLM (384d) with BGE-large (1024d, a 2.7$\times$ stronger encoder). The HS advantage persists directionally on all four models and remains significant for OT-7B (+18.1pp, $p{<}0.001$); effect sizes narrow for the remaining models, consistent with the prediction in our Limitations that stronger encoders would reduce the gap (\cref{app:encoder_robustness}).
55	
56	\paragraph{Caveats.} R1-32B achieves significance only at $W{=}1$ with 25\% coverage (5/20 traces); at $W{\geq}3$, dimensionality ($51200 \times W$ for $n{=}20$) prevents significance. QwQ-32B HS lead time is negative ($-$1.2 to +1.9 steps vs.\ text 3.7--12.3 steps): higher precision at later detection. On benign traces, probes produce 39--52\% false alarm rates, indicating that current methods characterize the commitment phenomenon rather than constitute production-ready detectors. Per-model details in \cref{sec:32b-analysis}.
57	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-18T01:44:13.505356+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex",
  "offset": "49",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex",
    "offset": "49",
    "limit": "5"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-18T01:44:13.958372+00:00_

49	\subsection{Evaluation Protocol}
50	\label{sec:evaluation}
51	
52	We report balanced accuracy, precision, pre-CP FPR (step-level and trace-level), coverage, and lead time (steps between first detection and true CP). Detection requires $K{=}5$ consecutive threshold crossings. Modality comparisons use two-sided null-centered bootstrap (1000 resamples) with Holm-Bonferroni step-down correction (3 metrics $\times$ 4 models $= 12$ tests, $\alpha{=}0.05$). Within each model, the three metrics are positively correlated by construction, making the correction stricter than under independence. Control task selectivity~\citep{hewitt2019control} validates genuine representational structure (\cref{app:control}).
53	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-18T01:44:14.259944+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex",
  "offset": "1",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex",
    "offset": "1",
    "limit": "5"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-18T01:44:14.310551+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Layer selection as researcher degree of freedom.}
4	Layer selection is an underexamined methodological choice in the probing literature that can silently determine a study's conclusions. Our five-metric ablation (\cref{sec:layer-results}) demonstrates that a single metric component, the crossing rate, reverses the central finding of an HS vs.\ text comparison: at biased layers, only 5 of 12 tests survive Holm-Bonferroni correction, producing an apparent scale-dependent modality effect; at corrected layers, HS probes are significant on all four models across all three metrics (12/12 tests pass). The mechanism is general: crossing rate rewards representational volatility at shallow layers independently of discriminative power, and any composite metric that incorporates threshold-crossing frequency is susceptible to the same bias mechanism, whose practical impact depends on the specific task and model depth. This bias is not specific to safety probing. We hypothesize that any threshold-based detection study that uses crossing rate as a layer selection criterion, whether for sentiment, factuality, or toxicity, could produce analogous reversals. Validation on other probing tasks is needed to confirm generality. We recommend that probing studies report results under at least two complementary layer selection criteria, and that five-metric ablations (or at minimum, results at multiple candidate layers spanning shallow, middle, and deep positions) become standard practice. Even among unbiased metrics, the choice between threshold-based and threshold-free criteria affects layer selection: AUROC peaks at mid-depth layers (${\sim}50\%$) while precision peaks at deep layers ($>90\%$), further demonstrating that layer selection methodology is a critical researcher degree of freedom. The cost of ablation is modest: evaluating five metrics across all layers adds minutes to an experiment that takes hours. The alternative 
…[truncated 406 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-18T01:44:18.728154+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "offset": "292",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4a087be8d8cfffc128323993d357d229:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
    "offset": "292",
    "limit": "15"
  }
}
```

</details>

---
