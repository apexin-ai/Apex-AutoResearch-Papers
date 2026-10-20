# Research conversation: You are Reviewer 2 in a paper review roundtable. Your focus is **novelty + related work + story consistency**. Do NOT ev

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 3
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a8e2640886a51143f.jsonl`
- **Structured JSON:** [`4d1a7e7de69b108629a6.json`](../../sessions/4d/4d1a7e7de69b108629a6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

3 recorded events

### User

_source line 1 · 2026-05-18T17:04:26.753Z_

You are Reviewer 2 in a paper review roundtable. Your focus is **novelty + related work + story consistency**. Do NOT evaluate method implementation details or experiment design (that's Reviewer 1's job). Do NOT evaluate formatting.

## Paper Summary (I've read the full 12-page PDF)

Title: "Ordinal Depth Estimation for Recursive Model-Generated Text: A Depth Degradation Atlas"

The paper formalizes ordinal generation depth estimation as a new task: given a text passage and a reference model, predict its recursive generation depth d ∈ {0,1,...,K}. d=0 = human text. Benchmark: 3 models (Pythia-1.4B, OLMo-1B, GPT-2 XL) × 3 strategies (nucleus, temperature, top-k) × 4 depths × 5000 passages each. 19 statistical features (perplexity, surprisal, diversity). Random Forest is best classifier (70-85% 4-class accuracy).

**Contributions claimed (Introduction p.2):**
1. Task formalization and benchmark (3 models × 3 strategies × 4 depths, 70-85% accuracy)
2. Depth Degradation Atlas: first systematic empirical characterization of recursive text degradation — (a) perplexity tail statistics as universal markers, (b) non-uniform inter-depth distances, (c) EDD boundary, (d) strategy-dependent feature trajectory reversal
3. Cross-strategy pipeline: two-stage approach, +11.5pp over naive transfer

**Related Work (Section 2, ~1 page):**
- Model Collapse and Recursive Training: Shumailov 2024, Alemohammad 2024, Dohmatob 2024, Gerstgrasser 2024, Drayson 2025. Positioning: "shifts from 'how does text degrade' to 'can we estimate depth from text alone.'"
- Machine-Generated Text Detection: Binoculars (Hans 2024), Fast-DetectGPT (Bao 2024), LOKI (Liu 2024), DivEye (He 2024), Uchendu 2020. Positioning: "all designed for binary classification, not ordinal depth."
- Decoding Strategy Effects: Holtzman 2020, Garces Arias 2025. Only 2 citations.
- Data Curation and Quality Filtering: DSIR (Xie 2023), QuRating (Wettig 2024). Positioning: "complementary signal."

Total references: ~28.

**Key experimental findings:**
- Within-strategy RF: 70-85% 4-class accuracy
- Cross-strategy: naive 59.1%, two-stage pipeline 70.5%, oracle 78.3%
- 14B (Qwen2.5-14B, nucleus only): 68% accuracy, attenuated signal
- API/instruct: 42-45% accuracy (feature shift from p90_ppl to surprisal_range)
- Wild data: 19-32% FPR on web-crawl, <2% on WikiText
- Binary detector baselines: Fast-DetectGPT 54%, Binoculars 48% when calibrated for ordinal task
- DCOL negative result: contrastive ordinal learning failed (64.4%)
- Theoretical motivation: EDD bound, tail erosion connection (labeled "motivation not contribution")

**Abstract claims:** "70-85% four-class accuracy (chance=25%)", "preliminary experiments on Qwen2.5-14B confirm depth signal persistence at mainstream model scale (68% accuracy, chance=25%), with attenuated inter-depth discrimination compared to 1B models"

**Conclusion claims:** "feature-based classifiers achieve 70-85% four-class accuracy", "Preliminary 14B results confirm signal persistence at larger scale, while honest reporting of limitations (API model attenuation, cross-strategy reversal, wild data FPR) delineates the boundaries of current feasibility"

## Your Task

Produce a structured review report:
1. **Summary** (3-4 sentences)
2. **Strengths** (bullet points, focus on novelty/related work/story)
3. **Weaknesses** (each labeled Major/Minor + idea/presentation layer)
   - Major issue definition: novelty claim unverifiable due to missing related work, scope-venue mismatch, claims contradicted by own experiments
   - For each Major, explain WHY it's Major not Minor
4. **Questions for Authors** (2-4 questions)
5. **Score** (1-6 scale, 1=Strong Reject, 6=Strong Accept; calibrate against top ML venue ~25% acceptance)
6. **Confidence** (1-5)

Key considerations for your analysis:
- Is "task formalization + systematic empirical study" sufficient novelty for a top ML venue without algorithmic innovation?
- Does the Depth Degradation Atlas constitute a novel contribution or is it descriptive statistics?
- Does the gap between binary detectors (48-54%) and the proposed method (78.3%) justify a separate paper, or is it incremental?
- Are the story claims in Abstract/Intro consistent with what the experiments actually show?
- Is the Related Work landscape sufficiently covered? Any critical missing areas (data decontamination, membership inference, corpus fingerprinting)?
- How does the narrow practical scope (base models only, known strategy required, high wild FPR) affect the paper's positioning?

Be rigorous but fair. Acknowledge genuine novelty in task formalization while being honest about methodological limitations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7bf4f82b-d1ef-48c0-9f3c-c65591804b21",
  "agentId": "a8e2640886a51143f",
  "type": "user",
  "uuid": "0d35a1a4-9b26-4d1c-9dd8-a99ca93c14f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "54767580-3114-45ce-b1df-d1aec2ac2b43",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T17:04:26.765Z_

```json
{
  "parentUuid": "0d35a1a4-9b26-4d1c-9dd8-a99ca93c14f0",
  "isSidechain": true,
  "agentId": "a8e2640886a51143f",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "ba80b665-99a8-4137-834f-9c9969b58f6c",
  "timestamp": "2026-05-18T17:04:26.765Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "54767580-3114-45ce-b1df-d1aec2ac2b43",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T17:05:29.110Z_

## Review Report

### 1. Summary

This paper introduces ordinal generation depth estimation as a formal task—predicting how many recursive AI-generation rounds a text has undergone—and constructs a benchmark spanning three base language models, three decoding strategies, and four depth levels. The central contribution branded as the "Depth Degradation Atlas" is a systematic empirical characterization of how statistical text features evolve across depths. A two-stage cross-strategy transfer pipeline is proposed and evaluated. The paper sits at the intersection of model collapse research and machine-generated text detection, claiming a novel task framing that bridges both literatures.

---

### 2. Strengths

- **Genuine task novelty at the framing level.** Ordinal depth estimation is a meaningful recast of the model collapse problem: shifting from "does recursion degrade text?" to "can we estimate how much?" is a defensible and non-trivial epistemic repositioning. No prior paper in the Related Work cited appears to have operationalized this as a supervised ordinal prediction task with a benchmark.

- **Benchmark construction is systematic and replicable.** The 3 × 3 × 4 × 5000 design is principled, and fixing models to publicly available checkpoints (Pythia, OLMo, GPT-2 XL) means results are independently reproducible—a genuine service to the community even if the methods are modest.

- **Honest treatment of failure modes.** The paper reports DCOL failure, API model attenuation (42-45%), and wild data FPR (19-32%) without burying them. This epistemic honesty strengthens credibility.

- **The Atlas findings are mostly internally consistent.** The story from Section 2 through the core results (within-strategy accuracy, cross-strategy transfer gap, EDD boundary) follows a coherent narrative arc.

---

### 3. Weaknesses

---

**[Major — Novelty] Related Work omits directly adjacent literature that could undermine the novelty claim**

The paper positions itself as the first to estimate recursive depth from text features, but three adjacent literatures are either absent or critically underrepresented:

*Membership inference and data decontamination.* A substantial body of work (e.g., Shi et al. 2024 "Detecting Pretraining Data from Large Language Models"; Maini et al. 2023 "TOFU"; Min et al. 2023 "SiLo") addresses the problem of determining whether text was seen during training or generated—a problem structurally adjacent to "was this text generated at depth d?" The absence of any engagement with this literature is not a minor omission: if membership inference methods can already distinguish provenance at fine granularity, the novelty claim for ordinal depth estimation requires a much more careful differential argument. The paper does not make this argument.

*Corpus fingerprinting and watermarking.* Work on text watermarking (Kirchenbauer et al. 2023; Aaronson/Scott; Christ et al. 2024) and corpus-level fingerprinting directly addresses recursive contamination detection with stronger guarantees. If watermarking achieves provenance tracking with near-zero FPR, the 19-32% wild data FPR of the proposed approach looks not just limited but potentially superseded by an unacknowledged parallel line of work. The paper must either engage this literature or explain why the "no watermark" setting (which the paper presumably assumes) is the relevant practical regime.

*Why this is Major, not Minor:* A reviewer cannot confidently assess whether the novelty claim is valid without knowing whether these adjacent methods, when adapted to ordinal depth, already solve or substantially overlap with the proposed task. The missing citations are not peripheral—they are precisely the work a motivated practitioner would reach for first. Until these are addressed, Contribution 1 (task formalization as novel) remains unverified.

---

**[Major — Scope/Venue Fit] The practical scope is so constrained that the task framing may not hold under real conditions**

The benchmark is built exclusively on base (non-instruction-tuned) models. The instruct/API experiments show 42-45% accuracy and a feature shift from p90_ppl to surprisal_range—a qualitatively different feature regime. This is not a minor robustness check: it means the core Atlas findings (tail erosion, inter-depth distances, EDD boundary) may not generalize to the model class that produces the overwhelming majority of real-world AI-generated text in 2026. The paper acknowledges this as a limitation, but frames it as "boundary delineation" rather than a fundamental scope restriction.

The wild data FPR of 19-32% on web-crawl text further undermines practical deployment. For any realistic use case (corpus decontamination, AI content auditing), a nearly 1-in-4 false positive rate on naturally occurring text is prohibitive.

Combined, these two facts mean the system works well only when: (a) the source model is known, (b) the decoding strategy is known, (c) the model is a base model, and (d) the deployment domain is clean. This is an extremely narrow operational regime.

*Why this is Major, not Minor:* The paper's framing throughout—Abstract, Introduction, Conclusion—implies practical relevance for "real-world AI content proliferation" scenarios. The experimental evidence contradicts this framing. This is a story consistency failure (Abstract/Introduction claims vs. actual experimental scope), not just a limitation disclosure. The paper either needs to substantially reframe its claims or substantially expand the experimental scope to base models only, and be explicit that the Atlas characterizes a lab setting rather than a deployment-relevant one.

---

**[Major — Contribution Inflation] The "Depth Degradation Atlas" as a standalone contribution is primarily descriptive statistics**

The four Atlas findings—(a) perplexity tail statistics as universal markers, (b) non-uniform inter-depth distances, (c) EDD boundary, (d) strategy-dependent feature trajectory reversal—are observational characterizations derived from computing 19 statistical features over the benchmark corpus. The EDD bound is labeled by the authors themselves as "motivation not contribution." Finding (d) is the most potentially interesting but is described in terms of existence rather than mechanism; the paper does not explain *why* reversal occurs under certain strategies.

The implicit claim is that the Atlas is to depth estimation what distributional semantics atlases are to NLP: a structured empirical foundation that enables future work. This is a legitimate contribution type, but it requires the empirical characterization to be genuinely surprising, systematic, and predictive. What is missing is: (1) any test of whether the Atlas findings predict depth signal behavior on held-out models (the 14B experiment is suggestive but uses only nucleus sampling); (2) any principled account of which features will universally versus strategy-dependently track depth.

*Why this is Major, not Minor:* If Contribution 2 (the Atlas) is reduced to "we computed 19 features and found that some track depth better than others," the paper's novelty rests almost entirely on Contribution 1 (task formalization + benchmark) and Contribution 3 (two-stage pipeline). A 3-model, 3-strategy benchmark with a Random Forest classifier and an +11.5pp pipeline improvement is below the methodological bar for a top ML venue unless the task formalization and empirical findings are genuinely landmark. The Atlas needs to be either mechanistically grounded or demonstrated to generalize beyond the training distribution.

---

**[Minor — Story Consistency / Presentation] The gap between binary baselines and the proposed system is partially conflated**

The paper presents Fast-DetectGPT (54%) and Binoculars (48%) as evidence that binary detectors "cannot directly address" ordinal depth estimation. This is formally correct—they were not designed for this task—but the comparison is not quite fair as stated. The proposed within-strategy RF (70-85%) has access to the oracle strategy label and is evaluated in-distribution. The oracle cross-strategy accuracy (78.3%) is the right comparison point for the proposed pipeline (70.5%), but the binary baseline comparison uses a different evaluation regime. The paper should clarify what exactly is being compared and ensure the delta is not inflated by evaluation asymmetry.

---

**[Minor — Related Work Coverage] Decoding Strategy Effects subsection is underweighted**

Only two citations (Holtzman 2020, Garces Arias 2025) cover decoding strategy effects, yet strategy-dependent feature trajectory reversal is one of the four Atlas findings. The minimal coverage here creates the impression of incomplete surveying precisely where the paper's most interesting empirical finding lives. Additional relevant work on sampling behavior and output distribution shifts under different decoding regimes should be incorporated.

---

### 4. Questions for Authors

1. **On missing related work:** How do membership inference methods (e.g., Shi et al. 2024's Min-K% Prob) perform when adapted to the ordinal depth prediction task on your benchmark? If they achieve competitive accuracy without any training on depth-labeled data, what does this imply about the task's relationship to the already-solved pretraining detection problem?

2. **On the Atlas's generalizability:** The feature trajectory reversal under different strategies (Finding d) is described observationally. Is there a mechanistic account of why this reversal occurs? And does the Atlas predict anything testable about depth signal behavior on models not in the benchmark—e.g., can you prospectively predict which features will generalize to the 14B setting before running that experiment?

3. **On scope framing:** Given that instruct models (which dominate real-world AI text production) yield 42-45% accuracy and feature regimes that differ qualitatively from base models, would the authors characterize the current system as applicable to real-world AI content auditing, or is it primarily a scientific instrument for studying the model collapse phenomenon in controlled settings? The paper currently implies the former; the results suggest the latter.

4. **On the cross-strategy pipeline's practical requirement:** The two-stage pipeline requires knowing (or inferring) the source model's decoding strategy. In a real deployment scenario, this is typically unknown. What is the accuracy of Stage 1 (strategy identification), and does it compound errors with Stage 2 in ways that close the gap with the reported 70.5%?

---

### 5. Score

**2.5 — Borderline Findings**

Calibration rationale: The task formalization is genuinely novel and the benchmark construction is principled—this is not a reject. However, the three Major issues compound: (1) unengaged adjacent literature makes the novelty claim unverifiable; (2) the practical scope is too narrow to support the real-world framing; (3) the Atlas as currently presented is observational description without mechanistic grounding or demonstrated generalization. The Random Forest + 19 handcrafted features methodology is well below what top ML venues expect for empirical systems contributions. The paper is a reasonable fit for an empirical findings track (hence Findings rather than Main), but requires substantial revision to clarify scope, engage missing literature, and either ground the Atlas mechanistically or honestly reframe it as exploratory characterization.

If the authors can: (a) demonstrate the method is distinct from or strictly subsumes membership inference approaches; (b) provide a mechanistic account of at least one Atlas finding; (c) reframe claims to match the base-model-only operational regime—then the score could move to 3 (Findings-acceptable).

---

### 6. Confidence

**4 out of 5**

Strong familiarity with model collapse, machine-generated text detection, and membership inference literatures. Minor uncertainty on the completeness of the corpus fingerprinting/watermarking literature survey, which could affect the severity of Major Issue 1 in either direction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba80b665-99a8-4137-834f-9c9969b58f6c",
  "isSidechain": true,
  "agentId": "a8e2640886a51143f",
  "requestId": "req_011CbAPzapuB16RHAtT9TEAF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6225b6b0-09fb-4f3d-acfc-156386f6b240",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "54767580-3114-45ce-b1df-d1aec2ac2b43",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XKMFC8x27ayDR4tdtTk3wB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8694,
      "cache_read_input_tokens": 8114,
      "output_tokens": 2687,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8694
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2687,
          "cache_read_input_tokens": 8114,
          "cache_creation_input_tokens": 8694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8694,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
