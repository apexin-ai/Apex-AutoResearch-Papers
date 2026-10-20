# Research conversation: You are an expert ML reviewer at a top venue (acceptance rate ~25%). Review the following paper using a 6-point scale: 1

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-adcca37aec0a4bd30.jsonl`
- **Structured JSON:** [`04562b61f02064d49150.json`](../../sessions/04/04562b61f02064d49150.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

49 recorded events

### User

_source line 1 · 2026-05-16T16:24:14.324Z_

You are an expert ML reviewer at a top venue (acceptance rate ~25%). Review the following paper using a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept.

## Paper Summary

**Title:** Distributional Depth Profiling: An Empirical Study of Differential Feature Response in Recursive LLM Generation

**Core idea:** The paper introduces "generation depth estimation" — determining how many successive rounds of LLM generation produced a given text (depth 0 = human, depth 1 = first LLM generation, depth 2+ = recursive). Unlike binary real-vs-synthetic detection, this is ordinal. They identify a "differential depth response" pattern: central-tendency/diversity features (entropy_mean, TTR, hapax_ratio) drift monotonically with depth, while distributional shape features (entropy_std, tail_decay) remain near-stationary. This is consistent with a location shift in the NLL distribution.

**Method:** 7 handcrafted features computed under a held-out reference model (Pythia-410M), classified with XGBoost. Evaluation uses leave-one-generator-out (LOGO) across 5 generators from 3 families (Pythia, Qwen3, OLMo), all ≤2.8B parameters.

**Key results:**
- Feature ablation (Table 1): Full 7-feat ensemble 0.81, Surface-only 0.75, Reference-only 0.71 (5-fold CV on Pythia-2.8B)
- Per-feature trend (Table 2): hapax ρ=-0.65, TTR ρ=-0.63, entropy_mean ρ=-0.55 drift; shape features near-zero
- Perplexity by depth: monotonically decreasing (13.5, 5.0, 3.1, 2.2, 1.8; ρ=-0.92)
- LOGO cross-generator (Table 3): avg 3-class F1=0.78, range 0.73–0.84, std=0.042
- Leave-one-family-out (Table 4): Pythia-out 0.74, Qwen-out 0.78, OLMo-out 0.80
- Paraphrastic vs continuation chains (Table 5): continuation 3-class 0.78 vs paraphrastic 0.72; feature drift magnitude ratio 0.65×
- 5-class ordinal (Table 6): F1=0.49, gen2/gen3 confusion rate 0.45, ordinal methods +1-2pp over flat
- End-to-end QLoRA Qwen3-0.6B (Table 7): CV F1=0.89, LOGO F1=0.72, gap=17pp vs XGBoost's 3pp gap
- Negative downstream result: depth-aware curation does not outperform random subsampling

**Paper structure:** 7 pages, sections: Introduction, Related Work, Method (problem formulation, feature extraction, classifier, evaluation protocol), Experiments (ablation, cross-generator, paraphrastic comparison, 5-class ordinal, end-to-end neural), Discussion, Conclusion. References: 10 entries.

## Experimental Design Reference (from design document)

The paper was designed to cover the following experiments:
1. **feature_ablation_and_trend** (plan_001): Feature ablation + per-feature trend + perplexity validation — COVERED in Section 4.1
2. **cross_generator_evaluation** (plan_002): 5-generator LOGO + leave-one-family-out — COVERED in Section 4.2
3. **paraphrastic_comparison** (plan_006): Paraphrastic vs continuation chains — COVERED in Section 4.3
4. **finer_grained_ordinal** (plan_009): 5-class ordinal classification — COVERED in Section 4.4
5. **end_to_end_classifier** (plan_012): QLoRA fine-tuned classifier comparison — COVERED in Section 4.5

Additionally, a downstream data curation experiment is mentioned in the abstract/conclusion but not given its own section (negative result reported inline).

## Your Review Task

Provide a comprehensive review covering ALL of the following dimensions. Be specific and cite evidence from the paper.

### 1. Summary (3-4 sentences)
Summarize the paper's contributions in your own words.

### 2. Strengths (bulleted list, ≥4 items)
What does this paper do well? Consider: novelty of task formulation, experimental rigor, clarity, practical relevance, honest reporting of limitations.

### 3. Weaknesses (bulleted list, ≥4 items)
What are the paper's shortcomings? Consider:
- Scale limitations (all generators ≤2.8B — how well does this generalize to 7B, 70B, etc.?)
- Feature engineering vs deeper analysis (are 7 hand-picked features principled or ad hoc?)
- The reference model choice (Pythia-410M) — is this justified? What happens with a different reference model?
- Statistical rigor (confidence intervals, significance tests)
- Missing experiments or baselines
- The downstream negative result — is it well-controlled?
- Writing quality and organization
- Novelty concerns relative to existing synthetic text detection and model collapse literature

### 4. Questions for Authors (≥3 items)
What would you ask the authors to clarify or provide?

### 5. Missing References or Related Work
Are there important related works not cited?

### 6. Experiment Coverage Assessment
Compare the paper's experiments against the 5 planned experiments listed above. Are any experiments superficially covered or missing important details? Is the downstream result adequately described?

### 7. Overall Assessment
- **Soundness** (1-5): Are the claims well-supported?
- **Novelty** (1-5): How new is this contribution?
- **Significance** (1-5): How impactful is this work?
- **Clarity** (1-5): How well-written is the paper?
- **Overall Score** (1-6 scale): Your recommendation with justification
- **Confidence** (1-5): How confident are you in your assessment?

Be rigorous but fair. This is a 7-page empirical study that explicitly positions itself as a "systematic empirical study with measurable cross-architecture limitations" rather than claiming universal characterization. Evaluate the claims the paper actually makes, not strawman stronger claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "e9dc1d36-b5dc-46a9-81ad-e868353e85d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T16:24:14.328Z_

```json
{
  "parentUuid": "e9dc1d36-b5dc-46a9-81ad-e868353e85d5",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
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
      "TodoWrite",
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
      "TodoWrite",
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
  "uuid": "608c76ff-009d-45be-8db6-a443dc1b8f66",
  "timestamp": "2026-05-16T16:24:14.328Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 3 · 2026-05-16T16:24:17.610Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018kHfS5AaFg2LLzjQ93zHbB`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "608c76ff-009d-45be-8db6-a443dc1b8f66",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZJvFF3xauHy4fp3eSD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbabe8f4-a052-4559-a653-36d7e800af2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rWyYQCe9Wu3pchXbb6WkD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16694,
      "cache_read_input_tokens": 0,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16694
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 88,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16694,
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

### Tool result

_source line 4 · 2026-05-16T16:24:17.619Z_

<details><summary>↩ Tool result · `toolu_018kHfS5AaFg2LLzjQ93zHbB`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbabe8f4-a052-4559-a653-36d7e800af2b",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "9435a9f7-644a-45a0-92f3-8db6db4fb8b2",
  "sourceToolAssistantUUID": "cbabe8f4-a052-4559-a653-36d7e800af2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T16:24:20.846Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NuW3WhoHGet189jAX3qryE`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_framing.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9435a9f7-644a-45a0-92f3-8db6db4fb8b2",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZKATWZfNifqn4mSbym",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36bfffbe-2dcd-48a4-8246-87921c279267",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUtcnLXQyujgAucuHHhYdZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 16694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1270,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T16:24:20.861Z_

<details><summary>↩ Tool result · `toolu_01NuW3WhoHGet189jAX3qryE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-fingerprint\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 ARR (deadline: May 25, 2026)** — D012\\n- Fallback: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\\n\\n## Core Insight\\nNon-paraphrastic LLM generation chains exhibit **differential depth response**: **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **distributional shape features** (entropy_std, tail_decay) remain near-stationary. This differential response is consistent with recursive generation inducing a **location shift** in the NLL distribution — the text becomes progressively more predictable (mean shifts) while the functional form of the distribution is preserved (shape is invariant). The genuine novelty is not the drift/stationarity split per se (which follows from location-shift properties), but: (a) the **task formulation** (ordinal depth estimation beyond binary detection), (b) **empirical validation** across 6 generators / 3 model families (including 7B+ scale) showing this pattern is robust, (c) the practical consequence that combining both feature types yields **complementary signal** for depth classification. **Primary metric (D017)**: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, excluding gen-0 due to shared-seed leakage). 3-class LOGO F1 = 0.789 reported as supplementary with gen-0 caveat. Per-generator held-out F1: 0.68–0.86 (std=0.058). Key finding: in binary evaluation (no gen-0 leakage), 7-feature (0.723) > 4-baseline ensemble (0.712) — baseline advantage in 3-class was entirely from gen-0 classification. Depth signal is scale-invariant as a phenomenon, though cross-scale classifier transfer shows a moderate gap (8B held-out F1=0.69 vs ≤2.8B 0.76-0.85).\\n\\n## Core Claims (3 条，均可证伪)\\n\\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth with F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation). Primary metric: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, gen-0 excluded due to shared-seed overlap). 3-class (gen-0/gen-1/gen-2+) LOGO F1 = 0.789 supplementary with caveat.\\n\\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Depth-dependent features exhibit differential response: central-tendency/diversity features (entropy_mean, TTR, hapax_ratio) drift monotonically with depth (consistent with location shift in NLL distribution), while shape features (entropy_std, tail_decay) remain near-stationary. In binary eval, 7-feature ensemble (0.723) outperforms 4-baseline detector ensemble (0.712) by +1.1pp and all individual detectors (+1.1–19.9pp). The 4-baseline advantage in 3-class (0.796 vs 0.789) is entirely from gen-0 classification. Ordinal-specific methods (CORAL 0.771, Frank-Hall 0.793) do not outperform XGBoost (0.789) — CI overlap at 3-class granularity.\\n\\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality compared to random subsampling. At equal data count, size_matched (random control, ppl=2.367) outperforms depth01 (depth-stratified, 2.387) and binary_filtered (2.389). The primary determinant is data quantity, not depth composition (all 12K samples → ppl=2.335). Depth fingerprinting is an effective **diagnostic** tool for characterizing provenance, but not a **curative** tool for data curation. This honest negative finding is reported transparently.\\n\\n## Story Spine\\n\\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\\n\\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation. When repurposed as ordinal depth predictors, single detector scores (Avg-LogProb 0.737, LD-Score 0.655, FastDetectGPT 0.688, Binoculars 0.417 under 6-gen LOGO) show moderate signal but **high per-generator F1 variance** (e.g., AvgLogProb range 0.615–0.805, 19.0pp span), making them unreliable as standalone depth estimators.\\n\\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing **differential depth response**: level/diversity features (including reference-model entropy_mean) drift monotonically with depth, while distributional shape features (entropy variance, tail decay) remain near-stationary. This split is about **what the feature measures** (central tendency vs shape), not where it comes from. The combination of drifting and stationary features yields a 7-feature ensemble that **significantly and consistently** outperforms all single-detector baselines: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, p<0.001 vs Avg-LogProb 0.712, LD-Score 0.701, FastDetectGPT 0.616, Binoculars 0.524). In the leak-free binary evaluation, 7-feature (0.723) > 4-baseline ensemble (0.712), reversing the 3-class result where baseline advantage came entirely from gen-0 classification. The practical advantage is **reliability across unknown generators** — per-generator F1 std = 0.058 for our ensemble vs higher variance for individual detectors.\\n\\n**Headline result template**: \\\"On non-paraphrastic continuation chains across 6 base-model generators from 3 model families (0.6B–8.2B), our 7-feature distributional ensemble achieves binary LOGO F1 of 0.72 for leak-free depth discrimination (gen-1 vs gen-2+), outperforming all individual detection baselines. Per-generator held-out F1 ranges from 0.68 to 0.86 (std=0.051). Depth-aware data curation does not outperform random subsampling for downstream CLM quality, establishing depth fingerprinting as a diagnostic tool for provenance characterization, not a curative tool for data selection.\\\"\\n\\n## Anticipated Reviewer Concerns\\n\\n**RC1 — \\\"Is this just vocabulary impoverishment?\\\"**: Surface features alone achieve 0.73 macro-F1, but full 7-feature ensemble achieves 0.789 3-class / 0.723 binary (p<0.001). We don't claim reference features are \\\"better\\\" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting level/diversity). Note: \\\"fingerprint\\\" in the paper refers to the full feature vector's combination, not just reference-model features.\\n\\n**RC7 — Pre-registered prediction (LD-Score)**: LD-Score (character-distribution signature) measures character-level distributional properties. We predict it is a **level feature** (sensitive to vocabulary/character frequency shifts) and should exhibit **H₂ drift** with depth. This prediction is registered before plan_011 execution as an out-of-sample test of the level/shape framework.\\n\\n**RC2 — \\\"Does this generalize beyond Pythia?\\\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\\n\\n**RC3 — \\\"Is 3-class sufficient? Why not finer-grained?\\\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\\n\\n**RC4 — \\\"How realistic are single-model chains?\\\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\\n\\n**RC5 — \\\"What about human editing / post-processing?\\\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\\n\\n**RC6 — \\\"Ecological validity — continuation vs real web content\\\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\\n\\n**RC8 — \\\"Aren't these just OOD detection features?\\\"**: Reference-model entropy statistics are functionally NLL-based OOD scores (same signal backbone as DetectGPT/GLTR/Binoculars). Our contribution is NOT the features themselves but: (a) the problem formulation (ordinal depth estimation, not binary detection), (b) the empirical discovery that these features exhibit dual dynamics (level drift vs shape stationarity) under recursive generation, and (c) the practical application to risk-stratified data curation. Paper must explicitly connect to OOD detection + perplexity-based detection literature and position the contribution as primarily empirical/conceptual rather than methodological.\\n\\n**RC9 — \\\"Only ≤2.8B generators — does this transfer to frontier scale?\\\"**: **Answered (plan-014, D011).** Qwen3-8B (7.6B params) added as 6th generator. Depth signal IS present at 8B scale — all feature-depth Spearman correlations significant. Cross-scale transfer gap: 8B held-out F1=0.69 vs ≤2.8B 0.76-0.85. P0-B volume-matched control: adding Qwen3-8B's +1.1pp improvement is 94% from generator diversity, not data volume. **Paper framing**: depth signal universality supported; cross-scale gap is honest limitation; scope narrowed to base models (see N3/N4 fixes).\\n\\n**RC10 — \\\"Text length confound\\\"**: Hapax ratio and TTR are mechanically length-dependent. If generation chains produce texts of systematically different lengths, surface features may track length artifacts rather than distributional drift. → Length distribution analysis + length-normalized features + length-matched comparison (plan_013). Critical confound control.\\n\\n**RC11 — \\\"Downstream utility — single run, no CIs\\\"**: Depth-aware filtering advantage must be validated with multiple seeds + bootstrap CIs + sample-count-matched comparison (to control for data size confound). Must use non-Pythia model for downstream fine-tuning (OLMo-1B) to avoid reference model circularity (Pythia-410M as both feature extractor and eval model).\\n\\n## Contribution Positioning (D006+D007)\\nThe contribution is **primarily empirical and conceptual**, not methodological:\\n1. **Problem formulation**: Ordinal depth estimation as a new task beyond binary detection (genuinely novel — no prior work)\\n2. **Empirical characterization**: Differential depth response across 6 generators / 3 families (including 7B+ scale), with robust cross-generator generalization (binary LOGO F1=0.723, 3-class LOGO F1=0.789). Scale-invariant phenomenon with honest cross-scale transfer gap.\\n3. **Negative finding**: Depth-aware data curation does NOT improve downstream CLM quality — depth fingerprinting is diagnostic, not curative (D009).\\n\\n**Framing discipline (D007 — re-dream consensus):**\\n- Do NOT call the drift/stationarity split a \\\"discovery\\\" — it follows from location-shift properties of the NLL distribution (means shift under distributional drift, shapes don't). Acknowledge this explicitly.\\n- Do NOT use H1/H2 terminology (overloads time-series unit-root convention). Use \\\"drifting\\\" vs \\\"stationary\\\" or \\\"differential response.\\\"\\n- Do NOT overclaim \\\"dual dynamics\\\" as a novel theoretical framework. Use \\\"differential depth response\\\" — more calibrated.\\n- Consider renaming \\\"distributional fingerprinting\\\" → \\\"distributional depth profiling\\\" (fingerprinting implies source identification, creates confusion with LLM attribution literature).\\n- Provide at least a speculative theoretical motivation for WHY shape features remain stationary (e.g., \\\"shape is determined by sampling mechanism and architecture, invariant to input content drift\\\").\\n- Report **realistic performance range** (0.68–0.86 per-generator held-out F1, binary LOGO F1=0.\\n\\n... [截断: 省略 1630 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 13630, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36bfffbe-2dcd-48a4-8246-87921c279267",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "1ce225ed-8c40-444d-914d-9ec1f52f6396",
  "sourceToolAssistantUUID": "36bfffbe-2dcd-48a4-8246-87921c279267",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T16:24:21.836Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NaCgbRwN22XWkCpks7NpXg`</summary>

```json
{
  "pattern": "artifacts/_project/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ce225ed-8c40-444d-914d-9ec1f52f6396",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZKATWZfNifqn4mSbym",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c7b93ff-5d1f-4c34-a045-57ed1ef8d320",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUtcnLXQyujgAucuHHhYdZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 16694,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1270
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 16694,
          "cache_creation_input_tokens": 1270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1270,
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

### Tool result

_source line 8 · 2026-05-16T16:24:21.875Z_

<details><summary>↩ Tool result · `toolu_01NaCgbRwN22XWkCpks7NpXg`</summary>

```text
artifacts/_project/paper/ethics.tex
artifacts/_project/paper/appendix_length.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix_confusion_matrix.tex
artifacts/_project/paper/appendix_dataset_stats.tex
artifacts/_project/paper/appendix_downstream.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/appendix_lofo.tex
artifacts/_project/paper/appendix_qlora.tex
artifacts/_project/paper/appendix_human_edit.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/table1.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/appendix_prompt_type.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/table2.tex
artifacts/_project/paper/table4.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/appendix_classifier.tex
artifacts/_project/paper/appendix_finer_depth.tex
artifacts/_project/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c7b93ff-5d1f-4c34-a045-57ed1ef8d320",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "a2bf0f67-f64e-4528-a723-3c2b3c334971",
  "sourceToolAssistantUUID": "1c7b93ff-5d1f-4c34-a045-57ed1ef8d320",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T16:24:24.702Z_

<details open><summary>🔧 Tool call — Read · `toolu_019gVcNKaEzqtuZ1x5wvDFZH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2bf0f67-f64e-4528-a723-3c2b3c334971",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZKUumebZcwCRmXAJBa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c123e162-c1a7-4577-a77c-17154dfd57d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9JyFNTPG3zAjan2ihFku7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4052,
      "cache_read_input_tokens": 17964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4052,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T16:24:24.713Z_

<details><summary>↩ Tool result · `toolu_019gVcNKaEzqtuZ1x5wvDFZH`</summary>

```text
1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	Recursive application of language models---where each generation step conditions on prior LLM output---produces text with progressively altered distributional properties.
4	We study this phenomenon under controlled conditions, restricting to base (pretrained) models to isolate the generation mechanism from instruction-tuning effects.
5	We formulate \emph{ordinal depth estimation}---classifying text by generation depth rather than a binary real-vs-synthetic label---and characterize a \emph{differential depth response}: central-tendency features drift monotonically with depth while upper-tail shape features remain near-stationary, consistent with a location shift in the token-level NLL distribution with partial shape preservation.
6	A 7-feature ensemble exploiting this complementarity achieves binary F1\,=\,0.694 for depth discrimination across eight generators from five model families, significantly outperforming all individual detection baselines.
7	We additionally report that depth-aware data curation does not improve downstream language model quality over random subsampling at equal sample count.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c123e162-c1a7-4577-a77c-17154dfd57d5",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "f0331430-2245-4efd-a140-f50378f02b65",
  "sourceToolAssistantUUID": "c123e162-c1a7-4577-a77c-17154dfd57d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T16:24:25.177Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HwiT7o6BonmiLtXN2wvPpP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0331430-2245-4efd-a140-f50378f02b65",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZKUumebZcwCRmXAJBa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e79b4d5-f92e-4538-aa8b-88140ddeed38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9JyFNTPG3zAjan2ihFku7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4052,
      "cache_read_input_tokens": 17964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4052,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T16:24:25.183Z_

<details><summary>↩ Tool result · `toolu_01HwiT7o6BonmiLtXN2wvPpP`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-crawled corpora increasingly contain LLM-generated text---estimates suggest that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}---and this proportion grows as generated text re-enters the web and seeds subsequent generation.
5	The result is recursive generation chains whose outputs progressively diverge from human-written text.
6	Understanding the distributional properties of such recursive generation is a prerequisite for characterizing text provenance, yet the phenomenon itself---how distributional features evolve across generation depths---remains underexplored.
7	
8	We study distributional drift in non-paraphrastic generation chains under controlled conditions, using eight base (pretrained) models from five families (Pythia, OLMo, Qwen, Llama, Mistral) spanning multiple scales.
9	We restrict to base models as a deliberate design choice: instruction-tuning introduces confounds---output length variability, format constraints, safety-driven distribution shaping---that obscure the generation mechanism's intrinsic behavior.
10	Preliminary experiments confirm this concern: instruct models show substantially degraded depth signal (\S\ref{sec:discussion}), motivating the controlled base-model setting as the appropriate starting point for isolating recursive drift phenomena.
11	
12	Existing detectors \cite{fast_detectgpt,binoculars,ld_score,detectgpt}, like classical out-of-distribution methods \cite{ood_baseline,energy_ood,mahalanobis_ood}, provide binary real-vs-synthetic classification, conflating qualitatively different material.
13	A first-generation continuation retains much of the source distribution's lexical and structural properties; deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.
14	We formulate \emph{ordinal depth estimation}---classifying text into generation depth classes (gen-0\,/\,gen-1\,/\,gen-2+) rather than producing a binary label---and refer to the overall framework as \emph{depth fingerprinting}.
15	No existing method addresses this task in non-paraphrastic continuation chains.
16	When repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance (\S\ref{sec:results-baselines}), making any single detector unreliable.
17	Concurrent work on iterative paraphrasing chains \cite{broken_telephone,markovian_chains} analyzes convergence under semantic-preservation constraints; we study non-paraphrastic chains where the absence of semantic anchoring permits richer depth signal.
18	
19	We characterize a \emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy, type-token ratio, and hapax ratio---drift monotonically with generation depth, while upper-tail features (entropy max, tail decay) remain near-stationary.
20	We hypothesize that recursive generation induces a location shift in the NLL distribution with partial shape preservation; under this account, the softmax ceiling constrains upper-tail behavior regardless of input content, while variance shows moderate drift.
21	Combining features from all three response tiers---strong-drift, moderate-drift, and near-stationary---yields a 7-feature ensemble that achieves binary F1\,=\,0.694 for leak-free depth discrimination (gen-1 vs.\ gen-2+).
22	However, the strength of this signal is prompt-type dependent: continuation chains exhibit stronger drift than elaboration or rewriting chains (\S\ref{sec:discussion}).
23	
24	We additionally report a negative finding: despite the effectiveness of quality-based data curation for pretraining \cite{fineweb,dolma}, depth-aware curation does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 vs.\ 2.387).
25	
26	Our contributions are:
27	\begin{enumerate}[nosep,leftmargin=*]
28	    \item \textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for characterizing how distributional properties evolve across recursive generation depths.
29	    \item \textbf{Empirical characterization.} We document differential depth response across eight base-model generators spanning five model families: a 7-feature ensemble spanning three response tiers achieves binary F1\,=\,0.694 for leak-free depth discrimination, outperforming all individual detection baselines ($p < 0.001$).
30	\end{enumerate}
31	
32	The remainder of this paper is organized as follows.
33	\S\ref{sec:related} surveys related work on text detection, model collapse, and data quality.
34	\S\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.
35	\S\ref{sec:results} presents classification results, differential depth response analysis, and baseline comparisons.
36	\S\ref{sec:discussion} discusses mechanistic hypotheses and scope boundaries.
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e79b4d5-f92e-4538-aa8b-88140ddeed38",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "01c164e5-d19c-404d-8c34-5ebebbb1d9dd",
  "sourceToolAssistantUUID": "5e79b4d5-f92e-4538-aa8b-88140ddeed38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T16:24:25.719Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tx8CzCwMG9DkRUbdVFnPoD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01c164e5-d19c-404d-8c34-5ebebbb1d9dd",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZKUumebZcwCRmXAJBa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aba424c0-5536-4ecb-96d6-a4fe38d8fee4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9JyFNTPG3zAjan2ihFku7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4052,
      "cache_read_input_tokens": 17964,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4052
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 17964,
          "cache_creation_input_tokens": 4052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4052,
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

### Tool result

_source line 14 · 2026-05-16T16:24:25.728Z_

<details><summary>↩ Tool result · `toolu_01Tx8CzCwMG9DkRUbdVFnPoD`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
8	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
9	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
10	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
11	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
12	
13	\subsection{Generation Chain Construction}
14	\label{sec:generation}
15	
16	We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
17	This selection covers parameter scales from 0.6B to 8B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
18	
19	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
20	The same pool of seed passages serves as gen-0 for all generators.
21	We use shared seeds across generators to ensure that cross-generator comparisons control for input content, isolating the effect of the generation model from source text variation.
22	In LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.
23	We address this with a supplementary binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
24	Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\texttt{Continue the following text: \{text\}}''.
25	All generation uses temperature $\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.
26	The theoretical yield is $8 \times {\sim}1{,}000 \times 5 \approx 40{,}000$ texts; after removing generation failures, exact duplicates, and passages shorter than 50 tokens, 37{,}058 texts remain.
27	For classification, depths 2--4 are collapsed into the $2{+}$ class.
28	
29	\subsection{Feature Extraction}
30	\label{sec:features}
31	
32	The seven features are motivated by two complementary views of distributional drift.
33	Reference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.
34	Together, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).
35	This two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\S\ref{sec:results-differential}).
36	
37	We extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.
38	
39	\paragraph{Reference-model features.}
40	A held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.
41	Although Pythia-410M shares the GPT-NeoX architecture with two of the eight generators, cross-family reference model experiments (\S\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by only 0.024 across Pythia, OLMo, and Qwen references).
42	From the resulting NLL sequence, we extract five statistics:
43	\begin{itemize}[nosep,leftmargin=*]
44	    \item \textbf{entropy\_mean}\footnote{We use ``entropy'' as shorthand for token-level negative log-likelihood under the reference model, following convention in prior detection work. These are point-wise NLL values, not Shannon entropy of the full distribution.}: mean token-level NLL, capturing the average predictability of the text under the reference model;
45	    \item \textbf{entropy\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;
46	    \item \textbf{entropy\_max}: maximum token-level NLL, capturing the most surprising token;
47	    \item \textbf{entropy\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs.
48	    Although entropy\_min shows near-zero marginal impact in leave-one-feature-out analysis ($\Delta$F1\,=\,+0.01\,pp), we retain it for completeness of the NLL summary statistics (mean, std, max, min) and because removing it does not improve performance;
49	    \item \textbf{tail\_decay}: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.
50	    Sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\,pp) across thresholds from the 85th to 95th percentile.
51	\end{itemize}
52	
53	\paragraph{Surface features.}
54	Two features capture lexical diversity without requiring a reference model:
55	\begin{itemize}[nosep,leftmargin=*]
56	    \item \textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);
57	    \item \textbf{hapax\_ratio}: proportion of words appearing exactly once (\emph{hapax legomena}).
58	\end{itemize}
59	
60	\paragraph{Feature complementarity.}
61	The grouping reflects an empirical pattern we term \emph{differential depth response}: central-tendency and diversity features (entropy\_mean, TTR, hapax\_ratio) show strong monotonic drift with generation depth ($|\rho| = 0.61$--$0.65$); entropy\_min and entropy\_std show moderate drift ($|\rho| = 0.20$--$0.41$); and upper-tail features (entropy\_max, tail\_decay) remain near-stationary ($|\rho| < 0.05$).
62	This differential behavior---consistent with recursive generation compressing the lower tail of the NLL distribution while preserving upper-tail behavior---motivates combining both feature types.
63	As shown in \S\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.
64	
65	\subsection{Evaluation Protocol}
66	\label{sec:evaluation}
67	
68	\paragraph{Cross-validation.}
69	To evaluate generalization to unseen generators, we use \textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the eight generators is held out for testing and the remaining seven provide training data.
70	We additionally report \textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.
71	
72	\paragraph{Classifier.}
73	We use XGBoost \cite{xgboost} as the classifier throughout.
74	Gradient-boosted trees handle heterogeneous feature scales and nonlinear interactions without extensive hyperparameter tuning, and their feature importance scores support interpretability.
75	We use $n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, and learning rate $0.1$ for the 7-feature ensemble.
76	Baseline detectors (\S\ref{sec:results-baselines}) use the same XGBoost framework with $n\_\text{estimators}{=}100$ and $\max\_\text{depth}{=}3$ to avoid overfitting their single-feature input.
77	LOGO F1 is stable across random seeds (mean\,=\,0.762, std\,=\,0.001 over 5 seeds), confirming that results are not sensitive to classifier initialization.
78	Alternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.
79	%% TODO: update ordinal method numbers from 8gen results (CORAL/Frank-Hall F1 vs 0.762 baseline)
80	We evaluated two ordinal-specific methods (CORAL \cite{coral_ordinal}, Frank-Hall ordinal ensemble \cite{frank_hall_ordinal}); neither significantly outperforms multiclass XGBoost (3-class LOGO F1, CIs overlapping), confirming that with only three ordinal levels, ordinal structure provides minimal additional benefit.
81	
82	\paragraph{Metrics and statistical testing.}
83	The primary metric is \textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.
84	We report per-class F1 scores and 95\% confidence intervals via \emph{percentile bootstrap} ($n{=}1{,}000$), resampling at the document level within each held-out fold.
85	For pairwise model comparisons (e.g., full features vs.\ ablated subsets), we use the \textbf{McNemar test} on disagreement tables.
86	For comparisons against detection baselines, we use \textbf{paired bootstrap} significance tests.
87	All reported $p$-values are two-sided.
88	We report six pairwise comparisons in \S\ref{sec:results-baselines}; applying Bonferroni correction ($\alpha_{\text{adj}} = 0.05/6 = 0.0083$), all remain significant at $p < 0.001$.
89	Feature--depth correlations (\S\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.
90	
91	\paragraph{Baselines.}
92	We compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
93	Each baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.
94	
95	\paragraph{Length confound control.}
96	Since TTR and hapax\_ratio are mechanically length-dependent, we verify that depth signal is not an artifact of systematic length variation.
97	We conduct three complementary analyses: (1) Spearman correlation between text length and each feature (requiring $|\rho| < 0.15$ for non-confounded features), (2) classification with length-normalized features, and (3) comparison on length-matched subsets.
98	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aba424c0-5536-4ecb-96d6-a4fe38d8fee4",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "03485b17-11ed-4d8a-8442-0db0255a27fc",
  "sourceToolAssistantUUID": "aba424c0-5536-4ecb-96d6-a4fe38d8fee4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T16:24:30.446Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EKGjv6B64rGZGiFL2BwJBh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03485b17-11ed-4d8a-8442-0db0255a27fc",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZKm7M1SquTY3qcAnKK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8be6e8a2-a4c0-496a-b545-133dcc06aff7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GjADq7QkCsAhrgntYwK6v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4939,
      "cache_read_input_tokens": 22016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4939,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T16:24:30.452Z_

<details><summary>↩ Tool result · `toolu_01EKGjv6B64rGZGiFL2BwJBh`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate depth fingerprinting along four axes: cross-generator classification (\S\ref{sec:results-classification}), differential depth response of individual features (\S\ref{sec:results-differential}), comparison with existing detection baselines (\S\ref{sec:results-baselines}), and downstream utility for data curation (\S\ref{sec:results-downstream}).
5	
6	\subsection{Depth Classification Performance}
7	\label{sec:results-classification}
8	
9	Table~\ref{tab:logo-results} reports leave-one-generator-out (LOGO) macro-F1 for 3-class depth estimation (gen-0\,/\,gen-1\,/\,gen-2+) across eight generators spanning five model families and parameter counts from 0.6B to 8B.
10	
11	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; Table~\ref{tab:logo-results}; $N$\,=\,37{,}058). Because gen-0 seed texts are shared across generators (\S\ref{sec:generation}), the gen-0 class F1 may be inflated; we therefore report a leak-free binary evaluation (gen-1 vs.\ gen-2+, F1\,=\,0.694, CI [0.688, 0.700]; $N$\,=\,29{,}095) as the primary metric in \S\ref{sec:results-baselines}.
12	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B); 3-class F1 ranges from 0.682 (Mistral-7B) to 0.806 (Pythia-1B).
13	The primary difficulty lies in distinguishing gen-1 from gen-2+, where feature margins narrow.
14	
15	\paragraph{Cross-scale transfer.}
16	The eight-generator evaluation includes two large-scale models: Qwen3-8B (8B) and Mistral-7B (7B).
17	Depth signal persists at scale, though with a moderate gap: Mistral-7B binary F1\,=\,0.633 (lowest among all generators) vs.\ the 8-gen average of 0.694, confirming that cross-scale transfer incurs predictable degradation for generators substantially larger than the training-set majority.
18	
19	\paragraph{Cross-family generalization.}
20	Leave-one-family-out (LOFO) evaluation---holding out an entire model family and training on the remaining four---yields binary F1 of 0.687 (Pythia), 0.707 (OLMo), 0.687 (Qwen), 0.708 (Llama), and 0.643 (Mistral), with average 0.686 (average $\Delta$\,=\,$-$0.8\,pp vs.\ LOGO binary), confirming that depth features transfer across architectural families with only modest degradation.
21	
22	\paragraph{Cross-model chains.}
23	Cross-model chains---where each generation step uses a randomly selected generator---yield 3-class F1\,=\,0.809 and binary F1\,=\,0.764 under 5-fold stratified cross-validation, confirming that depth signal persists under generator heterogeneity.
24	
25	\paragraph{Length confound control.}
26	Text length correlates weakly with depth (Spearman $|\rho| < 0.14$).
27	Length-normalized feature trends are preserved, and length-matched subsampling yields comparable or higher F1 ($\Delta$\,=\,+0.041), ruling out length as a confound (Appendix~\ref{app:length}).
28	
29	
30	\begin{table}[t]
31	\centering
32	\small
33	\begin{tabular}{llccccc}
34	\toprule
35	\textbf{Generator} & \textbf{Family} & \textbf{Params} & \textbf{3-class F1} & \textbf{Binary F1} & \textbf{Binary CI} \\
36	\midrule
37	Pythia-2.8B     & Pythia  & 2.8B & 0.798 & \textbf{0.724} & [0.707, 0.742] \\
38	Pythia-1B       & Pythia  & 1.0B & \textbf{0.806} & 0.718 & [0.700, 0.735] \\
39	Qwen3-1.7B     & Qwen    & 1.7B & 0.772 & 0.709 & [0.693, 0.726] \\
40	Llama-3.2-3B   & Llama   & 3.2B & 0.775 & 0.697 & [0.680, 0.713] \\
41	OLMo-2-1B      & OLMo    & 1.0B & 0.781 & 0.695 & [0.679, 0.711] \\
42	Qwen3-8B       & Qwen    & 8.0B & 0.714 & 0.692 & [0.674, 0.708] \\
43	Qwen3-0.6B     & Qwen    & 0.6B & 0.780 & 0.691 & [0.673, 0.709] \\
44	Mistral-7B     & Mistral & 7.0B & 0.682 & 0.633 & [0.617, 0.648] \\
45	\midrule
46	\multicolumn{3}{l}{\textbf{Average (8-gen LOGO)}} & \textbf{0.762} & \textbf{0.694} & [0.688, 0.700] \\
47	\bottomrule
48	\end{tabular}
49	\caption{8-generator LOGO macro-F1 for the 7-feature ensemble (bootstrap 95\% CIs on binary F1, $n$\,=\,1000). Binary F1 (gen-1 vs.\ gen-2+) is the primary metric; 3-class includes the shared gen-0 class (\S\ref{sec:generation}).}
50	\label{tab:logo-results}
51	\end{table}
52	
53	%% TODO: update ordinal regression numbers from 8gen results
54	\paragraph{Ordinal regression comparison.}
55	CORAL ordinal regression \cite{coral_ordinal} and Frank-Hall ordinal reduction \cite{frank_hall_ordinal} achieve comparable 3-class F1 with all CIs overlapping the standard XGBoost (0.762).
56	Explicitly encoding ordinal structure does not yield a measurable gain, likely because 3-class granularity provides insufficient ordinal resolution for ranking-aware losses.
57	
58	
59	\subsection{Differential Depth Response}
60	\label{sec:results-differential}
61	
62	Features exhibit \emph{differential depth response}: central-tendency and diversity measures drift monotonically with depth, while upper-tail shape measures show negligible depth sensitivity.
63	This pattern is consistent with recursive generation inducing a location shift in the token-level NLL distribution---the text becomes progressively more predictable (mean shifts), while upper-tail behavior is preserved by the softmax ceiling.
64	
65	\begin{figure}[t]
66	\centering
67	\includegraphics[width=\columnwidth]{fig1_differential_response.pdf}
68	\caption{Differential depth response: Spearman correlations between individual features and generation depth (pooled across all eight generators, $N$\,=\,37{,}058). Features partition into three tiers: strong drift (hapax ratio $\rho = -0.647$, TTR $-0.630$, entropy mean $-0.610$; $|\rho| > 0.6$), moderate drift (entropy min $-0.406$, entropy std $|\rho| = 0.200$), and near-stationary (entropy max $|\rho| = 0.050$, tail decay $0.040$; $|\rho| < 0.05$). Cross-generator pooling produces minimal attenuation (per-generator medians ${\leq}$0.02 stronger).}
69	\label{fig:feature-drift}
70	\end{figure}
71	
72	Pooled Spearman correlations with depth (Figure~\ref{fig:feature-drift}) partition features into three response tiers: \emph{strong drift} (hapax ratio $\rho = -0.647$, TTR $\rho = -0.630$, entropy mean $\rho = -0.610$; pooled $|\rho| = 0.61$--$0.65$), \emph{moderate drift} (entropy min $\rho = -0.406$, entropy std $|\rho| = 0.200$; $|\rho| = 0.20$--$0.41$), and \emph{near-stationary} (entropy max $|\rho| = 0.050$, tail decay $|\rho| = 0.040$; $|\rho| < 0.05$).
73	Entropy std ($|\rho| = 0.200$) occupies an intermediate position, showing moderate depth sensitivity---substantially weaker than central-tendency features but clearly distinct from the near-stationary entropy max and tail decay.
74	Per-generator median correlations are slightly stronger than pooled values (e.g., hapax median $\rho = -0.662$ vs.\ pooled $-0.647$), confirming that cross-generator aggregation introduces only mild attenuation.
75	However, these correlations are computed on continuation chains; elaboration and rewriting chains show substantially weaker drift (Appendix~\ref{app:prompt-type}), and this prompt-type dependence bounds the generality of the differential response characterization.
76	
77	\paragraph{Feature complementarity.}
78	Table~\ref{tab:ablation} reports ablation results.
79	Under 10-fold cross-validation (Table~\ref{tab:ablation}), the full 7-feature set (F1\,=\,0.773) significantly outperforms both surface-only features (TTR, hapax\_ratio; F1\,=\,0.688) and reference-only features (entropy mean/std/max/min, tail\_decay; F1\,=\,0.713; McNemar $p \approx 0$).
80	Permutation importance ranks hapax ratio highest (0.269), followed by entropy mean (0.164) and TTR (0.159).
81	Surface features capture vocabulary impoverishment; reference features capture distributional shift---neither subsumes the other.
82	
83	\paragraph{Cross-family reference models.}
84	To confirm that differential depth response is not an artifact of the Pythia-410M reference model, we recompute all features using two cross-family references: OLMo-2-1B (1B) and Qwen3-0.6B.
85	All three reference models achieve comparable LOGO F1: Pythia-410M\,=\,0.789, OLMo-2-1B\,=\,0.795, Qwen3-0.6B\,=\,0.813 (spread 0.024; Table~\ref{tab:cross-ref}).\footnote{Cross-reference evaluation uses the original 6-generator subset for controlled comparison; main results use all 8 generators.}
86	Entropy drift direction is consistently negative across all reference models (Table~\ref{tab:cross-ref}), confirming that the differential depth response is a property of recursive generation, not of the specific reference model used.
87	
88	\input{table4}
89	
90	
91	\begin{table}[t]
92	\centering
93	\small
94	\begin{tabular}{lcc}
95	\toprule
96	\textbf{Feature set} & \textbf{F1} & \textbf{Top feature (importance)} \\
97	\midrule
98	Full (7 features)     & 0.773 & hapax\_ratio (0.269) \\
99	Surface only (2)      & 0.688 & hapax\_ratio (0.320) \\
100	Reference only (5)    & 0.713 & entropy\_mean (0.218) \\
101	\bottomrule
102	\end{tabular}
103	\caption{Feature ablation (8-gen 10-fold CV). Full $>$ surface (+8.5\,pp) and Full $>$ reference (+5.9\,pp) confirms complementarity between surface diversity features and reference-model distributional features.}
104	\label{tab:ablation}
105	\end{table}
106	
107	Leave-one-feature-out analysis confirms that 6 of 7 features contribute positively, with entropy\_max showing the largest marginal impact despite modest split frequency (Appendix~\ref{app:lofo}).
108	
109	
110	\subsection{Comparison with Detection Baselines}
111	\label{sec:results-baselines}
112	
113	\begin{figure}[t]
114	\centering
115	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.png}
116	\caption{LOGO macro-F1 with 95\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Per-generator held-out F1 varies more for single detectors than for the ensemble.}
117	\label{fig:baseline-ci}
118	\end{figure}
119	
120	We repurpose four existing detection scores as ordinal depth predictors by training the same classifier on each score as a single feature, using identical LOGO evaluation.
121	All four baselines were originally designed for binary human-vs-machine classification; to our knowledge, the 3-class depth estimation results reported here are the first for this task, with no prior SOTA for comparison.
122	Because gen-0 seed texts are shared across generators (\S\ref{sec:generation}), 3-class LOGO evaluation creates a train--test overlap for the gen-0 class.
123	We therefore report both 3-class and binary (gen-1 vs.\ gen-2+) results; the binary metric is the primary measure of depth discrimination (Table~\ref{tab:baselines}).
124	
125	\begin{table}[t]
126	\centering
127	\small
128	\begin{tabular}{lcc}
129	\toprule
130	\textbf{Method} & \textbf{3-class F1} & \textbf{Binary F1} \\
131	\midrule
132	7-feature ensemble    & 0.762 & \textbf{0.694} \\
133	4-det.\ + surface     & 0.771 & 0.690 \\
134	4-detector ens.\      & 0.769 & 0.684 \\
135	Avg-LogProb           & 0.685 & 0.642 \\
136	LD-Score              & 0.618 & 0.657 \\
137	FastDetectGPT         & 0.655 & 0.566 \\
138	Binoculars            & 0.398 & 0.516 \\
139	\bottomrule
140	\end{tabular}
141	\caption{Depth classification under unified LOGO evaluation. \textbf{3-class}: gen-0/gen-1/gen-2+ (gen-0 samples shared across generators; see \S\ref{sec:generation}). \textbf{Binary}: gen-1 vs.\ gen-2+ only, eliminating the gen-0 train--test overlap. The 7-feature ensemble achieves the highest binary F1 among all methods; on 3-class F1, the multi-detector ensembles hold a slight edge. (8-generator LOGO.)}
142	\label{tab:baselines}
143	\end{table}
144	
145	The 7-feature ensemble achieves binary F1\,=\,0.694, outperforming every individual baseline ($p < 0.001$ for all; Table~\ref{tab:baselines}).
146	On the primary binary metric, the 7-feature ensemble also edges out the 4-detector+surface ensemble (0.690) and the 4-detector ensemble (0.684), confirming that surface diversity features capture signal complementary to detection scores.
147	On 3-class discrimination, the multi-detector ensemble holds a slight advantage (+0.9\,pp), reflecting the additional information in combining four independent detection signals; this gap is driven by gen-0 classification, as existing detectors do not capture the finer depth signal between gen-1 and gen-2+.
148	Crucially, our features are individually interpretable and require only a single lightweight reference model, versus four independent detector pipelines.
149	The 7-feature ensemble requires a single reference-model forward pass per document (Pythia-410M, 410M parameters); the 4-detector ensemble requires four separate scoring models performing independent inference---approximately 4$\times$ computational cost for a statistically non-significant $+$0.4\,pp binary F1 difference (bootstrap CIs overlapping at 95\% level).
150	
151	
152	\subsection{Downstream Utility}
153	\label{sec:results-downstream}
154	
155	Depth-aware data curation does not improve downstream language model quality.
156	Fine-tuning OLMo-2-0425-1B on five data variants (3 seeds each) shows that data quantity dominates depth composition: random subsampling (ppl\,=\,2.367) outperforms depth-stratified selection (ppl\,=\,2.387) at equal sample count (Appendix~\ref{app:downstream}).
157	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8be6e8a2-a4c0-496a-b545-133dcc06aff7",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "d11a2a6e-4c27-4f66-8d4d-4e49a96cb09b",
  "sourceToolAssistantUUID": "8be6e8a2-a4c0-496a-b545-133dcc06aff7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T16:24:31.017Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YbuGoy2dFtvQAKzLk5ATeQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d11a2a6e-4c27-4f66-8d4d-4e49a96cb09b",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZKm7M1SquTY3qcAnKK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5aad26a8-de15-43c9-a59d-ba6803ee6e52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GjADq7QkCsAhrgntYwK6v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4939,
      "cache_read_input_tokens": 22016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4939,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T16:24:31.021Z_

<details><summary>↩ Tool result · `toolu_01YbuGoy2dFtvQAKzLk5ATeQ`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Partial shape preservation: mechanistic hypothesis.}
5	Near-stationary features (entropy\_max, tail\_decay) remain stable across generation depths ($|\rho| < 0.05$), while drifting features shift monotonically (\S\ref{sec:results-differential}).
6	Entropy\_std shows moderate pooled correlation ($|\rho| = 0.200$), intermediate between the strongly drifting central-tendency features and the near-stationary upper-tail features.
7	The refined pattern is \emph{lower-tail compression with upper-tail preservation}: entropy\_min (the NLL floor) decreases with depth ($\rho = -0.406$; per-generator $|\rho|$ up to 0.51), indicating that the model's most confident predictions become progressively more confident under recursion; meanwhile entropy\_max (the NLL ceiling) is unchanged ($|\rho| = 0.050$).
8	Mechanistically, recursive generation compresses the lower tail of the NLL distribution while preserving upper-tail behavior, resulting in a net location shift with partial shape preservation.
9	The softmax and top-$p$ sampler impose an effective ceiling on per-token surprise, explaining upper-tail invariance; but conditioning on progressively more predictable context allows the model to produce increasingly confident (low-NLL) tokens, compressing the lower tail.
10	Cross-generator pooling produces minimal attenuation for entropy\_std (per-generator median $|\rho| = 0.209$, pooled $|\rho| = 0.200$), indicating consistent moderate depth sensitivity across generators.
11	This predicts that upper-tail features should remain approximately stationary until generation depth reaches the model's fixed-point distribution, a regime not yet observed in our chain lengths ($\leq$4 steps).
12	Sampling ablation is consistent with this account: depth signal is robust to moderate temperature variation (${\leq}0.3$\,pp for $t \in [0.5, 0.7]$) but degrades substantially at $t = 1.0$ ($-6$\,pp; Appendix~\ref{app:sampling-sensitivity}), where the sampling mechanism itself becomes the dominant source of distributional shape variation, overwhelming the depth signal.
13	
14	\paragraph{Comparison with detector ensembles.}
15	On the primary binary metric (gen-1 vs.\ gen-2+), our 7-feature ensemble (F1\,=\,0.694) outperforms all individual detection baselines and edges out the 4-detector+surface ensemble (0.690) under 8-generator LOGO evaluation.
16	On 3-class discrimination, the multi-detector ensemble holds a slight advantage (+0.9\,pp), reflecting the additional information in combining four independent detection signals.
17	We do not claim feature-engineering superiority: the primary contributions are the task formulation (ordinal depth estimation beyond binary detection), the empirical characterization of differential depth response, and interpretability---seven summary statistics from a single lightweight reference model versus four independent detection pipelines.
18	On binary classification specifically, the 4-detector+surface ensemble achieves marginally higher pooled F1 (0.705 vs.\ 0.694), though this difference is not statistically significant (bootstrap CIs overlapping at the 95\% level).
19	That both approaches converge on near-identical binary performance suggests depth signal is accessible through multiple feature families; our approach offers a simpler, more interpretable route to the same discriminative boundary.
20	
21	\paragraph{Reference model choice.}
22	Qwen3-0.6B serves dual roles as both generator and cross-family reference model in Table~\ref{tab:cross-ref}, creating a potential self-referencing bias.
23	The measured advantage is modest: Qwen3-0.6B reference achieves LOGO F1\,=\,0.813 versus 0.789 for Pythia-410M (+2.4\,pp), within the range of inter-reference variation (spread 0.024; evaluated on the original 6-generator subset).
24	Qwen3-8B shows a pronounced same-family advantage under the Qwen3-0.6B reference (F1\,=\,0.757 vs.\ 0.685 with Pythia-410M), suggesting that architectural similarity between generator and reference facilitates depth signal extraction at scale.
25	All main results use Pythia-410M as the default reference to avoid this overlap; the cross-reference experiment (\S\ref{sec:results-differential}) serves solely to confirm that differential depth response is reference-model-independent.
26	
27	\paragraph{Prompt-type dependence.}
28	Differential depth response strength varies substantially across prompt types.
29	Continuation chains exhibit 16.9\% depth retention loss by gen-4, while elaboration chains retain 98.6\% of samples (Appendix~\ref{app:prompt-type}).
30	The 7-feature ensemble achieves within-type CV F1 of 0.781 for continuation vs.\ 0.730 for elaboration; cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms shared signal despite differing drift magnitudes.
31	Together with the paraphrastic attenuation reported below (binary F1\,=\,0.671 vs.\ 0.749 for continuation), these results bound depth fingerprinting's primary applicability to continuation-style generation, where distributional drift is strongest; near-paraphrastic settings approach the method's detection floor as semantic-preservation constraints anchor distributional shift \cite{broken_telephone}.
32	
33	\paragraph{Corpus-level vs.\ document-level utility.}
34	The practical value of depth estimation depends on the unit of analysis.
35	At the individual document level, gen-1 per-class F1\,=\,0.64 implies a 36\% misclassification rate---insufficient for automated filtering but suitable for flagging suspect documents for human review.
36	At the corpus level, aggregate depth composition can be estimated with substantially lower error: over $n$ documents, estimation error scales as $O(1/\sqrt{n})$---analogous to opinion polling, where individual voter prediction is unreliable but population-level estimates are actionable---making corpus-level provenance characterization reliable even with moderate per-document accuracy.
37	The 3-class design explicitly targets the most informative boundaries: human vs.\ machine (gen-0 vs.\ gen-1+) and shallow vs.\ deep recursion (gen-1 vs.\ gen-2+), where the distributional distinction is most actionable.
38	
39	\paragraph{Relation to model collapse.}
40	Our results relate to, but are distinct from, model collapse \cite{curse_of_recursion,strong_model_collapse,self_consuming_mad}.
41	In training-loop collapse, gradient updates on self-generated data cause progressive mode collapse---catastrophic diversity loss after 5--10 retraining generations \cite{curse_of_recursion}.
42	Our inference-chain setting involves no parameter updates; drift instead accumulates through repeated sampling from the model's high-probability regions, yielding a milder effect (hapax ratio declines ${\sim}$14\% over 4 depths).
43	Both processes share declining diversity, but they diverge in distributional shape: training collapse alters the distribution's functional form as learned parameters shift, whereas inference chains exhibit partial shape preservation---upper-tail features remain stationary because the decoding mechanism remains fixed, though variance (entropy\_std) shows moderate drift.
44	Speculatively, these trends suggest that surface features may serve as leading indicators of deeper distributional shifts, though this hypothesis requires longitudinal validation.
45	Topic drift mediates rather than confounds this process: semantic narrowing accounts for less than 9\% of feature variance (maximum $R^2 = 0.082$ for entropy\_mean), and shape features are near-independent of semantic drift ($|\rho| = 0.068$).
46	
47	\paragraph{Granularity ceiling.}
48	Five-class depth estimation reduces macro F1 from 0.770 to 0.488 (10-fold CV, 8-generator dataset); gen-2 and gen-3 are inseparable (per-class F1\,$\approx$\,0.24), establishing three classes as the practical ceiling for handcrafted features (Appendix~\ref{app:finer-depth}).
49	QLoRA fine-tuning raises 3-class F1 to 0.905 (+11.6\,pp over XGBoost; Appendix~\ref{app:qlora}), confirming exploitable depth signal beyond summary statistics.
50	
51	\paragraph{Robustness to post-generation editing.}
52	Depth features degrade gracefully under simulated editing: 20\% random token replacement reduces 3-class F1 by only 6.0\,pp, while LLM rephrasing drops binary F1 by 6.3\,pp (Appendix~\ref{app:human-edit}).
53	This asymmetry---surface noise is tolerable, systematic distributional manipulation is not---is consistent with depth signal residing in aggregate distributional properties rather than individual token choices.
54	
55	\paragraph{Paraphrastic chains.}
56	Initial paraphrastic experiments exhibited reversed entropy--depth correlations ($\rho = +0.394$), but removing contaminated samples aligned correlations with continuation chains ($\rho = -0.533$), confirming the reversal was an artifact.
57	On clean data, paraphrastic chains achieve binary F1\,=\,0.671 (vs.\ 0.749 for continuation), consistent with faster convergence under semantic-preservation constraints \cite{broken_telephone}.
58	Cross-transfer is effective (para$\to$cont F1\,=\,0.770, cont$\to$para 0.743), indicating shared depth signal.
59	
60	\paragraph{Instruct tuning.}
61	Instruction-tuned models show substantially weaker depth fingerprints (OLMo-Instruct LOGO F1\,=\,0.338 vs.\ 0.764 base; Qwen3-0.6B-Instruct 0.667 vs.\ 0.816 base).
62	Length-matched controls reduce correlations to near zero (all $|\rho| < 0.02$ for Qwen3-0.6B), and binary classification is near chance (F1\,$\approx$\,0.5), indicating that depth signal is not operationally detectable in instruct chains.
63	This justifies our restriction to base models: instruction tuning introduces distributional effects (output length regulation, format constraints) that dominate the subtler recursive drift signal, making base models the appropriate setting for isolating the generation mechanism.
64	
65	\paragraph{Negative downstream finding.}
66	Depth-aware curation does not improve downstream language model quality over random subsampling (\S\ref{sec:results-downstream}).
67	This negative result carries positive information value: it rules out depth-based filtering as a data selection strategy, sparing practitioners from building depth-conditional pipelines that would not yield quality gains.
68	The dominant factor is data quantity, not depth composition---consistent with findings emphasizing data volume over curation sophistication \cite{self_consuming_mad}.
69	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5aad26a8-de15-43c9-a59d-ba6803ee6e52",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "246e4d67-bc83-4e7e-ab84-641327665d9c",
  "sourceToolAssistantUUID": "5aad26a8-de15-43c9-a59d-ba6803ee6e52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T16:24:35.503Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M5A7NfsogYV9zmuTKFTQAw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "246e4d67-bc83-4e7e-ab84-641327665d9c",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZLAWG4GHgpij1zWT8b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad2edca3-5a24-46c4-9968-db3becd41086",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8BApfu2MZJk4ihq22Hua9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7486,
      "cache_read_input_tokens": 26955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7486,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T16:24:35.512Z_

<details><summary>↩ Tool result · `toolu_01M5A7NfsogYV9zmuTKFTQAw`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests \cite{gltr,grover,release_strategies} to zero-shot reference-model approaches \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers \cite{feat_aug_transformer,reliable_detection,ld_score}.
8	Recent work pursues diverse signals including intrinsic dimensionality \cite{intrinsic_dimension}, surprisal diversity \cite{diveye}, and distributional gap measures \cite{generator_barrier}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
9	A persistent limitation is that these methods produce binary (real vs.\ synthetic) decisions.
10	Recent multi-class extensions---role recognition in human-LLM collaboration \cite{beyond_binary} and multi-generator attribution \cite{semeval2024_task8}---discriminate among different \emph{sources} rather than recursive generation \emph{depth}.
11	%% TODO: update baseline range from 8gen results
12	Even when detection scores correlate with depth, they exhibit high cross-generator variance as ordinal predictors (Table~\ref{tab:baselines}), because each captures a single distributional property that generalizes inconsistently \cite{paraphrase_evades,detection_possibilities}.
13	Our contribution is not a new detection method but the task formulation (ordinal depth estimation) and the finding that combining features across three differential response tiers yields consistent cross-generator performance.
14	
15	\paragraph{Source attribution vs.\ depth estimation.}
16	Source attribution identifies \emph{which} model generated a text \cite{uchendu_attribution,munir_looking_glass}; depth estimation answers \emph{how many recursive steps} produced it.
17	The two tasks are orthogonal, and our LOGO evaluation decouples generator identity from depth by holding out entire generators.
18	
19	\subsection{Model Collapse and Iterative Generation}
20	\label{sec:related-collapse}
21	
22	Self-consuming generative models progressively lose distributional coverage \cite{self_consuming_mad}, and model collapse is inevitable without fresh human data \cite{curse_of_recursion}, though careful data mixing can mitigate this \cite{model_collapse_avoidable,strong_model_collapse}.
23	These studies focus on \emph{training-loop} degradation; our setting studies \emph{inference chains}, where a fixed model generates text conditioned on its own prior output without retraining.
24	
25	Two concurrent works are most directly relevant.
26	\citet{broken_telephone} analyze paraphrasing and translation chains, showing progressive information loss.
27	\citet{markovian_chains} demonstrate that semantic-preservation constraints induce attractor dynamics bounding distinguishable depth to approximately three classes.
28	We differ in studying \emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal, and in focusing on \emph{estimating} depth rather than characterizing convergence.
29	
30	\subsection{Vocabulary Diversity and Stylometry}
31	\label{sec:related-diversity}
32	
33	Declining lexical diversity in LLM-generated text is documented in both training \cite{curious_decline} and deployment \cite{writing_diversity} settings.
34	Our surface features---TTR and hapax ratio---are classical stylometric measures \cite{stamatatos_survey,koppel_authorship} that we apply to inference chains, showing monotonic diversity decline across depths without model retraining.
35	We push beyond generator identity \cite{uchendu_attribution} to the \emph{depth} dimension, and show that diversity declines monotonically even under top-$p$ sampling \cite{nucleus_sampling}.
36	
37	\subsection{Data Quality and Provenance}
38	\label{sec:related-provenance}
39	
40	Scalable data curation relies on quality signals: distribution matching \cite{dsir}, LLM-based scoring \cite{qurating}, and perplexity filtering \cite{ccnet}, as demonstrated by large-scale efforts such as FineWeb \cite{fineweb} and Dolma \cite{dolma}.
41	Generation depth is a complementary provenance signal characterizing \emph{how many steps removed} text is from a human source.
42	
43	Proactive provenance through watermarking \cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns during generation, but watermark strength decays across multi-step chains \cite{chainwash}, motivating passive post-hoc methods.
44	Our depth fingerprinting operates on text alone without generator cooperation.
45	At the feature level, our NLL analysis connects to \citet{min_k_percent}, who use the probability tail for membership inference; we analyze the full NLL distribution for ordinal depth estimation.
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad2edca3-5a24-46c4-9968-db3becd41086",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "e20f5a61-c843-4d23-81cb-76264d56db0a",
  "sourceToolAssistantUUID": "ad2edca3-5a24-46c4-9968-db3becd41086",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T16:24:36.059Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Jqj4t4FPTBnHdH9DnhqPk1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e20f5a61-c843-4d23-81cb-76264d56db0a",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZLAWG4GHgpij1zWT8b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1055596-9455-4a15-bc37-a1f04f2ee4d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8BApfu2MZJk4ihq22Hua9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7486,
      "cache_read_input_tokens": 26955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7486,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T16:24:36.063Z_

<details><summary>↩ Tool result · `toolu_01Jqj4t4FPTBnHdH9DnhqPk1`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced ordinal generation depth estimation as a task for characterizing how distributional properties evolve across recursive LLM generation.
5	In a controlled study of eight base-model generators from five families (0.6B--8B parameters), we documented differential depth response: central-tendency features drift monotonically while upper-tail features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution with partial shape preservation.
6	A 7-feature ensemble achieves binary F1\,=\,0.694 for leak-free depth discrimination (gen-1 vs.\ gen-2+), and cross-model chains confirm signal persistence under generator heterogeneity (3-class F1\,=\,0.809, binary F1\,=\,0.764).
7	Depth-aware data curation does not improve downstream language model quality, indicating that depth composition per se does not determine training utility.
8	
9	These results establish depth fingerprinting as a tool for understanding recursive generation phenomena in base models.
10	Extending to instruction-tuned models---where depth signal degrades substantially---and frontier-scale generators (70B+) are priorities for future work.
11	All code, data, and trained models will be released upon publication to facilitate reproducibility.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1055596-9455-4a15-bc37-a1f04f2ee4d3",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "90974c7b-7d7c-45f8-8a80-b39bf6840fde",
  "sourceToolAssistantUUID": "a1055596-9455-4a15-bc37-a1f04f2ee4d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T16:24:36.606Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QxXbKgRirGJuUCYAbXKoDy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90974c7b-7d7c-45f8-8a80-b39bf6840fde",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZLAWG4GHgpij1zWT8b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25a9cb5f-d6f9-4994-801f-53dd696745a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8BApfu2MZJk4ihq22Hua9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7486,
      "cache_read_input_tokens": 26955,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7486
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 26955,
          "cache_creation_input_tokens": 7486,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7486,
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

### Tool result

_source line 24 · 2026-05-16T16:24:36.610Z_

<details><summary>↩ Tool result · `toolu_01QxXbKgRirGJuUCYAbXKoDy`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects, enabling controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1\,=\,0.338 (vs.\ 0.764 base) and Qwen3-0.6B with chat template to 0.667 (vs.\ 0.816 base).
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth fingerprinting to instruct models requires addressing these confounds---length regulation, format constraints, safety-driven distribution shaping---that instruction tuning introduces.
10	
11	Our experiments include generators up to 8B parameters (Qwen3-8B) and 7B (Mistral-7B).
12	Depth signal persists at scale, but cross-scale transfer incurs a moderate gap (Mistral-7B binary F1\,=\,0.633 vs.\ 0.694 average).
13	Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.
14	
15	Differential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type F1\,=\,0.781) compared to elaboration (0.730), rewriting (0.737), and paraphrastic chains (binary F1\,=\,0.671 vs.\ 0.749 for continuation).
16	DDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.
17	Cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms shared signal, yet additional prompt types (e.g., summarization, instruction following) and cross-generator $\times$ cross-prompt interactions remain untested.
18	
19	Our primary evaluation uses single-generator chains; cross-model chains (\S\ref{sec:results-classification}) confirm depth signal under generator heterogeneity (3-class F1\,=\,0.809, binary F1\,=\,0.764), though the eight generators represent a controlled laboratory setting rather than the full diversity of real-world contamination.
20	Simulated human editing (\S\ref{sec:discussion}) suggests graceful degradation, but the gap between simulated token replacement and real-world post-processing remains untested.
21	
22	The reference model is fixed to Pythia-410M throughout, although cross-family reference experiments (\S\ref{sec:results-differential}) confirm the phenomenon is not reference-specific (spread 0.024 across three references).
23	All seed texts are English Wikipedia excerpts; generalization to other languages and domains remains untested.
24	
25	Our default analysis uses fixed decoding parameters (temperature 0.7, nucleus $p{=}0.9$). A sampling ablation (Appendix~\ref{app:sampling-sensitivity}) shows robustness to moderate variation ($t \in [0.5, 0.7]$, ${\leq}0.3$\,pp) but substantial degradation at $t{=}1.0$ ($-6$\,pp), indicating that depth fingerprinting assumes standard decoding regimes.
26	
27	We use 3-class granularity (gen-0\,/\,gen-1\,/\,gen-2+). A 5-class evaluation (Appendix~\ref{app:finer-depth}) yields LOGO F1\,$\approx$\,0.50, with depths 2--4 mutually indistinguishable, validating the 3-class design as the practical resolution limit.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25a9cb5f-d6f9-4994-801f-53dd696745a4",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "c90731b6-04fa-4886-9b04-f0ca9fb481ac",
  "sourceToolAssistantUUID": "25a9cb5f-d6f9-4994-801f-53dd696745a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T16:24:39.631Z_

<details open><summary>🔧 Tool call — Read · `toolu_013YHPwqS592rsBrmoKw4z5Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_downstream.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c90731b6-04fa-4886-9b04-f0ca9fb481ac",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZLZi2HT2TVpwTV1z1v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4dfa5820-f6da-49f0-ad10-bd0a201815b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KgLGvFB4oFd5WnzWy33rVd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 34441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2978,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T16:24:39.635Z_

<details><summary>↩ Tool result · `toolu_013YHPwqS592rsBrmoKw4z5Q`</summary>

```text
1	Can depth-aware data curation improve downstream language model quality?
2	We fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\ref{tab:downstream}).
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\begin{tabular}{lrcl}
8	\toprule
9	\textbf{Variant} & \textbf{$n$} & \textbf{Test PPL} & \textbf{Boot 95\% CI} \\
10	\midrule
11	All depths            & 12{,}299 & 2.335 $\pm$ 0.000 & [2.335, 2.335] \\
12	Size-matched (random) & 3{,}951  & 2.367 $\pm$ 0.000 & [2.367, 2.367] \\
13	Depth 0--1 only       & 3{,}951  & 2.387 $\pm$ 0.001 & [2.387, 2.388] \\
14	Binary-filtered       & 3{,}951  & 2.389 $\pm$ 0.000 & [2.389, 2.389] \\
15	Depth 0 only          & 797      & 2.681 $\pm$ 0.001 & [2.681, 2.682] \\
16	\bottomrule
17	\end{tabular}
18	\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\pm$ std across 3 seeds; bootstrap 95\% CI from $10{,}000$ seed-level resamples). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389). (6-generator data; fine-tuning evaluation.)}
19	\label{tab:downstream}
20	\end{table}
21	
22	The directional evidence is consistent: all three seeds rank the full training set above size-matched and depth-filtered alternatives, though the comparison is statistically underpowered (minimum achievable $p = 0.25$ for $n = 3$ paired comparisons).
23	Training on all 12{,}299 samples yields the lowest perplexity (2.335).
24	At equal sample count ($n$\,=\,3{,}951), random subsampling (2.367) \emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).
25	Cross-seed variance is below 0.002 across all variants, confirming the robustness of this null result.
26	
27	Restricting training to human-only text (depth 0, $n$\,=\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\times$ reduction in data volume rather than depth composition per se.
28	
29	A paired sign-flip test over 3 seeds yields $p = 0.25$ for size-matched vs.\ depth 0--1 ($\Delta$\,ppl\,=\,$0.020$); the test is severely underpowered (minimum achievable $p$-value with $n$\,=\,3 is $0.25$).
30	All three seeds show size-matched $<$ depth 0--1 (cross-seed variance $< 0.001$), providing consistent directional evidence despite insufficient statistical power.
31	A paired bootstrap ($10{,}000$ resamples) on the per-seed PPL differences gives a 95\% CI of $[-0.0203, -0.0193]$ for size-matched minus depth 0--1, excluding zero; the all-data vs.\ size-matched difference has CI $[-0.0326, -0.0316]$.
32	Cohen's $d = -34.8$ (Hedges' $g = -19.9$) reflects the near-zero cross-seed variance, not practical importance: the absolute PPL difference is 0.020 on a baseline of 2.367.
33	
34	\paragraph{Statistical caveats.}
35	Bootstrap CIs are computed from $n$\,=\,3 seed-level aggregate perplexities; with 3 observations, bootstrap resampling produces only 10 distinct sample means, so the CIs should be interpreted as reflecting low seed-to-seed variance rather than high statistical confidence.
36	Document-level bootstrap (resampling over the 3{,}138 eval documents) would be more informative but requires per-sample losses that were not retained.
37	The extremely large $|d|$ values arise because the denominator (cross-seed standard deviation $\approx 0.0006$) is tiny; the numerator (PPL difference $\approx 0.02$) represents $<1\%$ of the baseline perplexity.
38	
39	Knowing the generation depth of a document does not, by itself, make it more or less useful for training.
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dfa5820-f6da-49f0-ad10-bd0a201815b7",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "cc4444e5-60c1-4ea6-91ee-f86dfe203176",
  "sourceToolAssistantUUID": "4dfa5820-f6da-49f0-ad10-bd0a201815b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T16:24:40.104Z_

<details open><summary>🔧 Tool call — Read · `toolu_019JYTV91pnFvD7WhtbUTbCX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc4444e5-60c1-4ea6-91ee-f86dfe203176",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZLZi2HT2TVpwTV1z1v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f396188a-98aa-43ed-8760-71bf18c900fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KgLGvFB4oFd5WnzWy33rVd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 34441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2978,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T16:24:40.113Z_

<details><summary>↩ Tool result · `toolu_019JYTV91pnFvD7WhtbUTbCX`</summary>

```text
1	We evaluate finer-grained 5-class depth classification (gen-0 through gen-4) using the same 7-feature ensemble under 10-fold stratified cross-validation on the full 8-generator dataset.
2	
3	\begin{table}[h]
4	\centering
5	\small
6	\begin{tabular}{lcc}
7	\toprule
8	\textbf{Granularity} & \textbf{Macro F1} \\
9	\midrule
10	3-class (gen-0 / gen-1 / gen-2+) & 0.770 \\
11	5-class (gen-0 through gen-4)    & 0.488 \\
12	\bottomrule
13	\end{tabular}
14	\caption{Granularity comparison. (8-generator, 10-fold stratified CV.)}
15	\label{tab:5class-logo}
16	\end{table}
17	
18	\begin{table}[h]
19	\centering
20	\small
21	\begin{tabular}{lccccc}
22	\toprule
23	\textbf{Metric} & \textbf{Gen-0} & \textbf{Gen-1} & \textbf{Gen-2} & \textbf{Gen-3} & \textbf{Gen-4} \\
24	\midrule
25	Per-class F1 & 0.917 & 0.593 & 0.240 & 0.234 & 0.451 \\
26	\bottomrule
27	\end{tabular}
28	\caption{Per-class F1 for 5-class depth estimation. (8-generator, 10-fold stratified CV.)}
29	\label{tab:5class-perclass}
30	\end{table}
31	
32	\paragraph{Analysis.}
33	Moving from 3-class (gen-0 / gen-1 / gen-2+) to 5-class classification reduces macro F1 from 0.770 to 0.488 (Table~\ref{tab:5class-logo}).
34	The degradation is concentrated in the middle depths: gen-2 and gen-3 achieve only 0.240 and 0.234 F1, respectively (Table~\ref{tab:5class-perclass}).
35	These two classes are effectively inseparable, with adjacent-depth confusion (gen-2$\leftrightarrow$gen-3) accounting for the majority of errors---consistent with the intuition that deeper recursive generations converge in surface-level statistical fingerprints.
36	Gen-0 (human text) remains highly distinguishable (F1\,=\,0.917), and gen-1 retains moderate separability (F1\,=\,0.593).
37	Notably, features with weaker depth response in the 3-class setting become substantially more important under 5-class evaluation: permutation importance of entropy\_std increases by 93\% and tail\_decay by 400\% relative to 3-class, yet these gains are insufficient to resolve adjacent depths.
38	These results support the 3-class grouping adopted in the main paper: collapsing gen-2+ preserves the most informative boundary (human vs.\ first-generation vs.\ deeper recursion) while avoiding the noise introduced by near-identical adjacent depths.
39	
40	\paragraph{Classifier comparison.}
41	To verify that 5-class degradation reflects feature-level limitations rather than classifier choice, we note that alternative classifiers yield comparable 5-class performance (Appendix~\ref{app:classifier-comparison}): the gen-2/gen-3 boundary is the primary failure mode across all methods, ruling out classifier capacity as the bottleneck.
42	This establishes 3-class granularity as the practical ceiling for surface and entropy features.
43	At the 3-class level, ordinal-specific methods (CORAL ordinal regression, Frank-Hall reduction) similarly fail to improve over multiclass XGBoost (\S\ref{sec:results}), confirming that the bottleneck is feature separability across all granularities, not the modeling of label ordinality.
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f396188a-98aa-43ed-8760-71bf18c900fb",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "5b33007a-06c3-4f30-9bd1-20abc35de7e2",
  "sourceToolAssistantUUID": "f396188a-98aa-43ed-8760-71bf18c900fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T16:24:40.723Z_

<details open><summary>🔧 Tool call — Read · `toolu_012uoYjVcDDEfXFGwKS3uo3q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b33007a-06c3-4f30-9bd1-20abc35de7e2",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZLZi2HT2TVpwTV1z1v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f9c4b71-5c1c-402b-9ec5-650bab058ec3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KgLGvFB4oFd5WnzWy33rVd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 34441,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2978
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 248,
          "cache_read_input_tokens": 34441,
          "cache_creation_input_tokens": 2978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2978,
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

### Tool result

_source line 30 · 2026-05-16T16:24:40.729Z_

<details><summary>↩ Tool result · `toolu_012uoYjVcDDEfXFGwKS3uo3q`</summary>

```text
1	To verify that the depth signal resides in the features rather than the classifier,
2	we evaluate Logistic Regression and Random Forest
3	in place of XGBoost under 10-fold stratified cross-validation on the full 8-generator dataset (Table~\ref{tab:alt-classifier}).
4	All other settings---the same 7 features, 3-class labels, and class-balanced downsampling---are
5	kept identical. For Logistic Regression we apply standard scaling to the features.
6	
7	\begin{table}[h]
8	\centering
9	\caption{Classifier comparison (8-generator, 10-fold stratified CV; 3-class and binary).}
10	\label{tab:alt-classifier}
11	\small
12	\begin{tabular}{lcc}
13	\toprule
14	Classifier & 3-class F1 & Binary F1 \\
15	\midrule
16	XGBoost          & \textbf{0.770} & 0.701 \\
17	Random Forest    & 0.724 & 0.697 \\
18	Logistic Regr.   & 0.708 & 0.701 \\
19	\bottomrule
20	\end{tabular}
21	\end{table}
22	
23	XGBoost shows a clear advantage on 3-class F1 (+4.5\,pp vs.\ Random Forest), while binary F1 is essentially tied across all three classifiers ($\leq$0.4\,pp spread).
24	Even a linear model reaches binary F1\,=\,0.701---well above the 0.50 chance baseline---confirming that discriminative power originates in the features, not in classifier capacity.
25	The 3-class gap reflects XGBoost's ability to model nonlinear feature interactions that separate gen-1 from gen-2+, where margins are narrow.
26	
27	\subsection*{Sampling Sensitivity Analysis}
28	\label{app:sampling-sensitivity}
29	
30	To assess robustness to decoding hyperparameters, we regenerate continuation chains under three sampling configurations and re-evaluate the LOGO pipeline (Table~\ref{tab:sampling-ablation}).
31	
32	\begin{table}[h]
33	\centering
34	\caption{Depth classification under varying sampling parameters. All other settings match the default pipeline. (6-generator LOGO; 3-class and binary.)}
35	\label{tab:sampling-ablation}
36	\small
37	\begin{tabular}{lcc ccc}
38	\toprule
39	Config & Temp.\ & Top-$p$ & 3-class F1 & Binary F1 & $\rho$(entropy\_mean) \\
40	\midrule
41	Low        & 0.5 & 0.80 & 0.785 & 0.797 & $-0.694$ \\
42	Default    & 0.7 & 0.90 & 0.788 & 0.799 & $-0.602$ \\
43	High       & 1.0 & 0.95 & 0.726 & 0.733 & $-0.002$ \\
44	\bottomrule
45	\end{tabular}
46	\end{table}
47	
48	The depth signal is robust to moderate sampling variation: low and default configurations differ by at most 0.3\,pp in both 3-class and binary F1, and entropy--depth Spearman correlations remain strongly negative ($\rho \leq -0.60$).
49	At high temperature ($t{=}1.0$, top-$p{=}0.95$), classification degrades by approximately 6\,pp and the entropy--depth correlation collapses to near zero ($\rho = -0.002$).
50	The degradation is not uniform across generators: Qwen3-1.7B drops to a held-out F1 of 0.42 under the high-temperature configuration, far below the 6-generator average of 0.726.
51	This is consistent with the hypothesis that depth features are shaped by the sampling mechanism (\S\ref{sec:discussion}): elevated temperature injects sufficient randomness to flatten the distributional drift that accumulates across generation steps, effectively masking the depth signal.
52	The practical implication is that depth fingerprinting applies reliably under standard decoding regimes but should not be expected to generalize to high-entropy sampling settings.
53	
54	\subsection*{Training Set Size Sensitivity}
55	\label{app:training-size}
56	
57	To assess whether depth classification requires large training sets, we subsample the training data at four fractions and evaluate under 10-fold stratified CV on the full 8-generator dataset (Table~\ref{tab:training-size}).
58	
59	\begin{table}[h]
60	\centering
61	\caption{Effect of training set size on 3-class depth classification. (8-generator, 10-fold stratified CV.)}
62	\label{tab:training-size}
63	\small
64	\begin{tabular}{lc}
65	\toprule
66	Training Fraction & 3-class F1 \\
67	\midrule
68	25\%  & 0.754 \\
69	50\%  & 0.764 \\
70	75\%  & 0.768 \\
71	100\% & 0.769 \\
72	\bottomrule
73	\end{tabular}
74	\end{table}
75	
76	Performance saturates quickly: the gap between 25\% and 100\% training data is only 1.6\,pp, indicating that depth signal is robust to training set size and does not require large annotated corpora to extract.
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f9c4b71-5c1c-402b-9ec5-650bab058ec3",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "4df26377-b8df-4385-95b1-08f5d690e5da",
  "sourceToolAssistantUUID": "0f9c4b71-5c1c-402b-9ec5-650bab058ec3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T16:24:43.835Z_

<details open><summary>🔧 Tool call — Read · `toolu_011JMWT2G1GTN87hcVxHWFXq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4df26377-b8df-4385-95b1-08f5d690e5da",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZLsNAEZLSkUYowMbLE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cff5a81e-2fdb-4b00-9505-96fbd05eeb6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lfc5XyXGiNeTjnjo7s2uRw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4113,
      "cache_read_input_tokens": 37419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4113,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T16:24:43.840Z_

<details><summary>↩ Tool result · `toolu_011JMWT2G1GTN87hcVxHWFXq`</summary>

```text
1	%% TODO: re-run LOFO on 8-gen protocol and update all numbers below
2	We complement the permutation importance analysis (\S\ref{sec:results-differential}) with a leave-one-feature-out ablation. Each row drops one of the seven features and re-evaluates the full 8-gen LOGO protocol; $\Delta$ is the change relative to the full 7-feature ensemble (F1\,=\,0.762).
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\begin{tabular}{lcc}
8	\toprule
9	\textbf{Dropped feature} & \textbf{LOGO F1} & $\boldsymbol{\Delta}$ \textbf{vs Full} \\
10	\midrule
11	entropy\_max    & 0.774 & $-$1.50\,pp \\
12	entropy\_mean   & 0.783 & $-$0.63\,pp \\
13	ttr             & 0.784 & $-$0.55\,pp \\
14	hapax\_ratio    & 0.785 & $-$0.42\,pp \\
15	tail\_decay     & 0.786 & $-$0.33\,pp \\
16	entropy\_std    & 0.786 & $-$0.29\,pp \\
17	entropy\_min    & 0.789 & $+$0.01\,pp \\
18	\midrule
19	Full (7 features) & 0.789 & --- \\
20	\bottomrule
21	\end{tabular}
22	\caption{Leave-one-feature-out ablation (8-gen LOGO). Each row drops one feature and re-evaluates with the LOGO protocol. Sorted by impact magnitude.}
23	\label{tab:lofo}
24	\end{table}
25	
26	\paragraph{Analysis.}
27	Entropy\_max causes the largest degradation when removed ($-$1.5\,pp), despite ranking only fourth in permutation importance (split frequency 0.063). This indicates that entropy\_max provides unique signal---capturing the most surprising token under the reference model---that is not redundant with other features.
28	Conversely, entropy\_min is fully redundant ($\Delta$\,=\,+0.01\,pp), consistent with its near-zero permutation importance (0.015).
29	Six of seven features contribute positively to the ensemble, confirming that the 7-feature design is not over-specified.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cff5a81e-2fdb-4b00-9505-96fbd05eeb6d",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "731f94ed-eb84-4fe7-9db1-3055fa9919e2",
  "sourceToolAssistantUUID": "cff5a81e-2fdb-4b00-9505-96fbd05eeb6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T16:24:44.357Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SzWB5o1i6DMzg7LRfaX6aQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_prompt_type.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "731f94ed-eb84-4fe7-9db1-3055fa9919e2",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZLsNAEZLSkUYowMbLE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3b62e00-bb61-4347-91c2-187f0544238b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lfc5XyXGiNeTjnjo7s2uRw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4113,
      "cache_read_input_tokens": 37419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4113,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T16:24:44.361Z_

<details><summary>↩ Tool result · `toolu_01SzWB5o1i6DMzg7LRfaX6aQ`</summary>

```text
1	We evaluate depth fingerprinting under three prompt types using Pythia-2.8B: \emph{continuation} (``Continue the following text''), \emph{elaboration} (``Elaborate on the following text''), and \emph{inspired rewriting} (``Write a new passage inspired by the following text''). Each uses 995 seeds $\times$ 5 depths.
2	
3	\paragraph{Within-prompt-type classification.}
4	5-fold CV macro-F1: continuation 0.78, rewriting 0.74, elaboration 0.73. All three prompt types exhibit the same differential depth response pattern: drifting features (hapax ratio, TTR, entropy mean, entropy min) show consistent monotonic trends, near-stationary features (entropy max, tail decay) show negligible change, and entropy std shows moderate sensitivity intermediate between the two groups.
5	
6	\paragraph{Cross-prompt-type transfer (LOPTO).}
7	Leave-one-prompt-type-out evaluation yields average F1\,=\,0.753, confirming that depth signal transfers across prompt types. Feature decay rates differ: continuation shows the strongest drift (16.9\% total retention loss over the full 4-step chain), followed by rewriting (6.1\%) and elaboration (1.4\%), consistent with continuation chains applying less semantic constraint on the output.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3b62e00-bb61-4347-91c2-187f0544238b",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "085e41c0-b8ba-4799-8f9e-8655d46e84b4",
  "sourceToolAssistantUUID": "f3b62e00-bb61-4347-91c2-187f0544238b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T16:24:45.010Z_

<details open><summary>🔧 Tool call — Read · `toolu_016BCvNsRAquU2zfqHZN9fEt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "085e41c0-b8ba-4799-8f9e-8655d46e84b4",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZLsNAEZLSkUYowMbLE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5db05498-f44c-4508-b2d7-2c7c15e71aa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lfc5XyXGiNeTjnjo7s2uRw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4113,
      "cache_read_input_tokens": 37419,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4113
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 250,
          "cache_read_input_tokens": 37419,
          "cache_creation_input_tokens": 4113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4113,
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

### Tool result

_source line 36 · 2026-05-16T16:24:45.014Z_

<details><summary>↩ Tool result · `toolu_016BCvNsRAquU2zfqHZN9fEt`</summary>

```text
1	%% TODO: re-run human-edit robustness on 8-gen dataset and update table below
2	To assess whether depth features are robust to post-generation human editing, we simulate two editing scenarios on the full generation chain dataset and re-evaluate the 8-generator LOGO pipeline (Table~\ref{tab:human-edit}).
3	
4	\paragraph{Random token replacement.}
5	We randomly replace 5\%, 10\%, or 20\% of tokens in each text with uniformly sampled vocabulary items, simulating unstructured human edits (typo corrections, word substitutions).
6	Classification degrades gracefully: 3-class F1 drops by 3.5\,pp at 5\% replacement and 6.0\,pp at 20\%, while binary F1 (gen-1 vs.\ gen-2+) remains nearly unchanged ($\Delta \leq 0.8$\,pp).
7	The asymmetry is expected---random edits primarily disrupt human-vs-machine separation (gen-0 classification) by injecting noise into surface features, but the depth-discriminative distributional signal between gen-1 and gen-2+ is distributed across enough tokens to survive moderate perturbation.
8	
9	\paragraph{LLM rephrase.}
10	We rephrase each text using an instruction-tuned LLM, simulating the common scenario where users lightly edit LLM-generated text with LLM assistance.
11	Three-class F1 drops modestly ($-3.4$\,pp), comparable to 5\% random replacement.
12	However, binary F1 drops substantially ($-6.3$\,pp), indicating that LLM rephrasing specifically erodes the distributional differences between generation depths---consistent with the rephraser imposing its own distributional signature that partially overwrites the depth fingerprint.
13	
14	\begin{table}[h]
15	\centering
16	\small
17	\caption{Human-edit robustness under 8-gen LOGO evaluation. Baseline uses unmodified generation chains.}
18	\label{tab:human-edit}
19	\begin{tabular}{lcccc}
20	\toprule
21	\textbf{Condition} & \textbf{3-class F1} & \textbf{Binary F1} & \textbf{$\Delta$ 3-class} & \textbf{$\Delta$ binary} \\
22	\midrule
23	Baseline          & 0.762 & 0.694 & ---       & ---       \\
24	Random 5\%        & 0.754 & 0.718 & $-3.5$\,pp & $-0.6$\,pp \\
25	Random 10\%       & 0.743 & 0.717 & $-4.6$\,pp & $-0.7$\,pp \\
26	Random 20\%       & 0.729 & 0.717 & $-6.0$\,pp & $-0.8$\,pp \\
27	LLM rephrase      & 0.755 & 0.662 & $-3.4$\,pp & $-6.3$\,pp \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	The contrasting degradation patterns reveal that random noise and LLM rephrasing attack different aspects of the depth signal.
33	Random replacement degrades surface features (TTR, hapax ratio) that drive gen-0 separation, while preserving the reference-model entropy distribution that distinguishes gen-1 from gen-2+.
34	LLM rephrasing, by contrast, reshapes the entropy distribution itself, collapsing the depth-discriminative signal while leaving gen-0 separation relatively intact (the rephrased text is still recognizably machine-generated).
35	This suggests that depth fingerprinting is more vulnerable to systematic distributional manipulation than to surface-level noise---a practical consideration for deployment in settings where LLM-assisted editing is prevalent.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5db05498-f44c-4508-b2d7-2c7c15e71aa0",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "e9fea1a1-0ce5-4c33-aaca-d29e5344f1dc",
  "sourceToolAssistantUUID": "5db05498-f44c-4508-b2d7-2c7c15e71aa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T16:24:55.601Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UmTTniccFUYx6qMnWEphj5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9fea1a1-0ce5-4c33-aaca-d29e5344f1dc",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZMBgEgXJGjAa1CKQrr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06100e30-d92e-478c-8e05-609ee0da2844",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012LQb6DuLV89Vv4PAhzi8QP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2292,
      "cache_read_input_tokens": 41532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2292,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T16:24:55.605Z_

<details><summary>↩ Tool result · `toolu_01UmTTniccFUYx6qMnWEphj5`</summary>

```text
1	To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \cite{qlora}.
2	
3	\paragraph{Setup.}
4	%% TODO: re-run QLoRA on 8-gen dataset and update numbers below
5	We fine-tune Qwen3-0.6B-Base with LoRA rank 16, learning rate $2 \times 10^{-4}$, and 3 epochs on the same 8-generator dataset used throughout, framing depth estimation as 5-class sequence classification (gen-0 through gen-4).
6	For 3-class evaluation, we collapse predictions into gen-0\,/\,gen-1\,/\,gen-2+ post hoc.
7	All results use the same LOGO protocol as the main experiments.
8	
9	\begin{table}[h]
10	\centering
11	\small
12	\caption{QLoRA end-to-end depth classification vs.\ XGBoost on handcrafted features, under LOGO evaluation.}
13	\label{tab:qlora}
14	\begin{tabular}{lccc}
15	\toprule
16	\textbf{Method} & \textbf{5-class F1} & \textbf{3-class F1} & \textbf{Per-class F1 (5-class)} \\
17	\midrule
18	XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.762 & --- \\
19	QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	\paragraph{Results.}
25	QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003), a +14.3\,pp improvement over the XGBoost baseline (0.762).
26	On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
27	The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
28	
29	\paragraph{Hyperparameter robustness.}
30	A second run with LoRA rank 32 and seed 123 yields 5-class F1\,=\,0.587 ($\pm$0.005) and 3-class F1\,=\,0.905 ($\pm$0.004), confirming stability across hyperparameter and seed variation ($\Delta < 1$\,pp on both metrics).
31	
32	\paragraph{Implications.}
33	The substantial 3-class improvement demonstrates that raw token embeddings contain depth signal beyond what summary statistics capture---the seven handcrafted features are a strong but lossy compression of the full distributional information.
34	End-to-end fine-tuning exploits token-level patterns (e.g., positional regularities, n-gram repetitions) that aggregate features cannot represent.
35	This confirms that the depth signal documented in our main analysis is real and exploitable beyond engineered features, while the handcrafted approach retains practical advantages: interpretability, computational efficiency (no GPU inference), and the ability to reveal the differential depth response pattern that motivates the task formulation.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06100e30-d92e-478c-8e05-609ee0da2844",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "cf2f0e7e-4ab0-4d99-903e-df4470fc31ae",
  "sourceToolAssistantUUID": "06100e30-d92e-478c-8e05-609ee0da2844",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T16:24:56.217Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DXx5pj3XMLarYDEJxtmyos`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf2f0e7e-4ab0-4d99-903e-df4470fc31ae",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZMBgEgXJGjAa1CKQrr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "199e98e9-2409-466a-b164-cb2590d40ddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012LQb6DuLV89Vv4PAhzi8QP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2292,
      "cache_read_input_tokens": 41532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2292,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T16:24:56.236Z_

<details><summary>↩ Tool result · `toolu_01DXx5pj3XMLarYDEJxtmyos`</summary>

```text
1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	
11	\graphicspath{{../chart/}}
12	
13	\title{Depth Fingerprinting: Ordinal Generation Depth Estimation\\in Non-Paraphrastic LLM Text Chains}
14	
15	\author{Anonymous}
16	
17	\begin{document}
18	\maketitle
19	
20	\input{abstract}
21	
22	\input{introduction}
23	\input{related_work}
24	\input{method}
25	\input{results}
26	
27	\input{discussion}
28	\input{conclusion}
29	\input{limitations}
30	\input{ethics}
31	
32	\bibliography{references}
33	
34	\appendix
35	\section{Length Confound Analysis}
36	\label{app:length}
37	\input{appendix_length}
38	
39	\section{Prompt Type Generalization}
40	\label{app:prompt-type}
41	\input{appendix_prompt_type}
42	
43	\section{Finer-Grained Depth Classification}
44	\label{app:finer-depth}
45	\input{appendix_finer_depth}
46	
47	\section{End-to-End Depth Classification (QLoRA)}
48	\label{app:qlora}
49	\input{appendix_qlora}
50	
51	\section{Leave-One-Feature-Out Analysis}
52	\label{app:lofo}
53	\input{appendix_lofo}
54	
55	\section{Confusion Matrix}
56	\label{app:confusion}
57	\input{appendix_confusion_matrix}
58	
59	\section{Classifier Sensitivity}
60	\label{app:classifier}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "199e98e9-2409-466a-b164-cb2590d40ddb",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "15d52940-1bc9-4023-80c8-cc1447de4f97",
  "sourceToolAssistantUUID": "199e98e9-2409-466a-b164-cb2590d40ddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T16:24:59.705Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MUSRBnv3chuSAFP5pA5X4G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "offset": 60,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15d52940-1bc9-4023-80c8-cc1447de4f97",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZN225vGggrp44cT6px",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b19e665-370c-452a-945d-2a9d9beed221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhN8W3GmjXMT54nz6EKeZb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1817,
      "cache_read_input_tokens": 43824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1817,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T16:24:59.711Z_

<details><summary>↩ Tool result · `toolu_01MUSRBnv3chuSAFP5pA5X4G`</summary>

```text
60	\label{app:classifier}
61	\input{appendix_classifier}
62	
63	\section{Human-Edit Robustness}
64	\label{app:human-edit}
65	\input{appendix_human_edit}
66	
67	\section{Downstream Utility}
68	\label{app:downstream}
69	\input{appendix_downstream}
70	
71	\input{appendix_dataset_stats}
72	
73	\end{document}
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b19e665-370c-452a-945d-2a9d9beed221",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "97bc73eb-e3c6-4e2b-9b83-7c33f6fe9bbb",
  "sourceToolAssistantUUID": "2b19e665-370c-452a-945d-2a9d9beed221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T16:24:59.998Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RuzaCsf4brzwH3ncHJSszJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table4.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97bc73eb-e3c6-4e2b-9b83-7c33f6fe9bbb",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZN225vGggrp44cT6px",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d4679ef-c783-43a5-92d2-0d920925a254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhN8W3GmjXMT54nz6EKeZb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1817,
      "cache_read_input_tokens": 43824,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1817
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 43824,
          "cache_creation_input_tokens": 1817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1817,
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

### Tool result

_source line 44 · 2026-05-16T16:25:00.001Z_

<details><summary>↩ Tool result · `toolu_01RuzaCsf4brzwH3ncHJSszJ`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\begin{tabular}{llccc}
5	\toprule
6	\textbf{Reference Model} & \textbf{Family} & \textbf{Params} & \textbf{LOGO F1} & \textbf{Entropy Drift Range} \\
7	\midrule
8	Pythia-410M & Pythia & 410M & 0.789 & [$-$1.19, $-$1.40] \\
9	OLMo-2-1B  & OLMo   & 1.0B & 0.795 & [$-$0.61, $-$0.91] \\
10	Qwen3-0.6B & Qwen   & 0.6B & 0.813 & [$-$0.96, $-$1.35] \\
11	\bottomrule
12	\end{tabular}
13	\caption{Cross-family reference model validation (3-class).
14	Evaluated on the original 6-generator subset for controlled comparison; main results use all 8 generators.
15	Cross-reference spread is 0.024, confirming that depth signal is reference-model-independent.
16	Drift direction is consistently negative across all three reference models; magnitude varies with reference model capacity.}
17	\label{tab:cross-ref}
18	\end{table}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d4679ef-c783-43a5-92d2-0d920925a254",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "3e230572-337a-4ef6-be9d-4f0ecfc5c308",
  "sourceToolAssistantUUID": "5d4679ef-c783-43a5-92d2-0d920925a254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T16:25:03.132Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DEFPh9QwNcv7CSwWsHfadB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e230572-337a-4ef6-be9d-4f0ecfc5c308",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZNHjtjmTCY1SnQsSUr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69731734-667b-43f3-9038-828cbd603b02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NrYJbBU7C6o1ztfbKMcenw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 45641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 854,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T16:25:03.136Z_

<details><summary>↩ Tool result · `toolu_01DEFPh9QwNcv7CSwWsHfadB`</summary>

```text
1	% Appendix A — Length Confound Analysis
2	% Data source: plan-013 (23,032 samples, 5 generators)
3	
4	Surface diversity features (TTR, hapax ratio) mechanically depend on text length:
5	shorter texts yield higher type-token ratios by construction.
6	If generation depth systematically shortens text, observed depth trends could be length artifacts rather than genuine distributional shifts.
7	We rule this out with three complementary analyses.
8	
9	\paragraph{(a) Length--depth correlation.}
10	We compute Spearman rank correlation between word count and depth across all five generators.
11	Correlations are weak and inconsistent in sign:
12	$\rho$ ranges from $-0.066$ (Pythia-1B) to $+0.134$ (OLMo-2-1B), with $|\rho| < 0.14$ in every case.
13	One generator (Qwen3-0.6B) shows no significant correlation ($\rho = 0.012$, $p = 0.43$).
14	Length and depth are thus near-independent in our corpus.
15	
16	\paragraph{(b) Length-normalized feature trends.}
17	To eliminate residual length effects, we recompute TTR and hapax ratio on fixed 200-word windows.
18	After normalization, monotonic depth trends are fully preserved for all generators; moreover, Spearman correlations between normalized features and depth \emph{increase} in absolute value (e.g., Pythia-2.8B TTR: $\rho = -0.633 \to -0.715$).
19	Length removal sharpens the depth signal rather than diminishing it, confirming that the signal is not a length artifact.
20	
21	\paragraph{(c) Length-matched classification.}
22	We subsample the dataset so that word-count distributions are equalized across depth classes, then retrain the 3-class XGBoost classifier (\S\ref{sec:results-classification}).
23	Macro-F1 changes by $\Delta = +0.041$ relative to the unmatched baseline---performance \emph{improves} when length variance is removed.
24	This is consistent with length acting as noise rather than signal.
25	
26	\paragraph{Conclusion.}
27	We observe a dropout bias: shorter texts are more likely to fall below the minimum-length threshold at deeper generation stages.
28	However, this bias does not drive the depth fingerprint.
29	All three analyses converge on the same conclusion: the depth signal captured by our feature ensemble is independent of text-length variation.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69731734-667b-43f3-9038-828cbd603b02",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "39a28bfa-443e-4b84-8ed6-c90ef2e6bef3",
  "sourceToolAssistantUUID": "69731734-667b-43f3-9038-828cbd603b02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T16:25:03.368Z_

<details open><summary>🔧 Tool call — Read · `toolu_015vqgUC9FeMiUswqQ3oKGHi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39a28bfa-443e-4b84-8ed6-c90ef2e6bef3",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZNHjtjmTCY1SnQsSUr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5218960b-bde5-430f-a09a-5d5aa8add48e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NrYJbBU7C6o1ztfbKMcenw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 45641,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 854
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 45641,
          "cache_creation_input_tokens": 854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 854,
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

### Tool result

_source line 48 · 2026-05-16T16:25:03.372Z_

<details><summary>↩ Tool result · `toolu_015vqgUC9FeMiUswqQ3oKGHi`</summary>

```text
1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage---how many recursive generation steps it has undergone---not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency---rather than content removal---is the objective.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5218960b-bde5-430f-a09a-5d5aa8add48e",
  "isSidechain": true,
  "promptId": "adf75226-c1c5-487b-860d-46216814c73c",
  "agentId": "adcca37aec0a4bd30",
  "type": "user",
  "uuid": "9b67ddde-3dfe-4a33-905a-679d4308fcca",
  "sourceToolAssistantUUID": "5218960b-bde5-430f-a09a-5d5aa8add48e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-16T16:26:37.777Z_

Now I have a thorough understanding of the paper. Let me compile my review.

---

## Review: Distributional Depth Profiling: An Empirical Study of Differential Feature Response in Recursive LLM Generation

### 1. Summary

This paper defines the novel task of ordinal generation depth estimation -- determining how many recursive LLM generation steps produced a given text (depth 0 = human, depth 1 = first-generation, depth 2+ = deeper recursion). The authors identify a "differential depth response" pattern where central-tendency/diversity features (entropy_mean, TTR, hapax_ratio) drift monotonically with depth while upper-tail shape features (entropy_max, tail_decay) remain near-stationary. A 7-feature XGBoost ensemble achieves binary LOGO F1 = 0.694 across 8 generators from 5 families. An honestly reported negative result shows that depth-aware curation does not improve downstream LM quality over random subsampling.

### 2. Strengths

- **Novel and well-motivated task formulation.** Ordinal depth estimation beyond binary detection is genuinely new. No prior work attempts to classify text by recursive generation depth in non-paraphrastic chains. The paper convincingly argues why "how many recursive steps" is more informative than "real or fake."

- **Rigorous evaluation protocol.** The LOGO and LOFO evaluation designs genuinely test cross-generator generalization. The authors identify and address the gen-0 train-test overlap issue by reporting a leak-free binary metric as the primary result -- a commendable methodological choice that many papers would sweep under the rug.

- **Comprehensive ablation and robustness testing.** The paper includes: feature ablation, cross-reference model validation (3 reference models, spread only 0.024), cross-model chains, sampling parameter sensitivity, length confound control (3 complementary analyses), prompt-type variation, human-edit robustness, classifier alternatives, training set size sensitivity, and 5-class granularity evaluation. This thoroughness exceeds the typical empirical study at this venue.

- **Honest reporting of limitations and negative results.** The downstream utility negative result is transparently reported. The instruct-model limitation (OLMo-Instruct drops to F1=0.338) is stated prominently rather than buried. The paper explicitly acknowledges prompt-type dependence, cross-scale degradation (Mistral-7B at 0.633), and the 3-class practical ceiling. This calibrated framing is refreshing.

- **Interpretable mechanistic hypothesis.** The "lower-tail compression with upper-tail preservation" explanation (softmax ceiling constrains maximum surprise, recursive conditioning compresses minimum surprise) is testable and well-argued. The connection between location shift in NLL distributions and differential feature behavior adds conceptual depth beyond pure empiricism.

- **Statistical rigor.** Bootstrap CIs throughout, McNemar tests for ablation, paired bootstrap for baseline comparisons, Bonferroni correction for multiple comparisons, and explicit acknowledgment of underpowered tests (downstream experiment with n=3 seeds).

### 3. Weaknesses

- **Limited ecological validity -- base models only.** The most critical limitation is that depth signal effectively vanishes for instruction-tuned models (F1 near chance for length-matched instruct chains). Since virtually all LLM-generated web text comes from instruct/RLHF models, the practical applicability of the entire framework is questionable. The paper acknowledges this but does not adequately address how the findings could be extended. This severely limits real-world impact.

- **Feature engineering is largely ad hoc despite principled framing.** The paper retroactively frames the 7 features as motivated by a location-shift hypothesis, but the feature set (5 NLL summary statistics + TTR + hapax) is essentially standard perplexity-based detection features repurposed. entropy_min contributes nothing (LOFO delta = +0.01pp), yet is retained "for completeness" -- this undercuts the claim of principled design. The LOFO table also shows the full set has F1=0.789 but individual feature removal causes at most 1.5pp degradation, suggesting high redundancy.

- **Modest absolute performance.** Binary F1 = 0.694 for the primary metric means ~30% of documents are misclassified between gen-1 and gen-2+. The paper acknowledges per-document unreliability (gen-1 F1=0.64, 36% error rate) and pivots to "corpus-level utility," but does not experimentally validate corpus-level estimation accuracy. The polling analogy is suggestive but unsubstantiated.

- **Limited generator scale.** While the paper includes 8B and 7B models (an improvement over the summary's claim of "all <=2.8B"), Mistral-7B is the worst-performing held-out generator (binary F1=0.633), and the paper lacks any generator at 13B+, 30B+, or 70B+ scale. Frontier models with higher fluency likely compress depth margins further, and the degradation trend from small to larger generators (clear from Table 1) suggests the approach may not scale.

- **Single domain (Wikipedia seeds only).** All generation chains start from English Wikipedia excerpts. No evaluation on creative writing, code, scientific text, social media, or multilingual content. Domain-specific vocabulary statistics (TTR, hapax) could behave very differently on technical or informal text.

- **Downstream experiment is statistically underpowered.** With n=3 seeds and minimum achievable p=0.25, the downstream experiment cannot establish statistical significance. The absolute PPL difference (0.020 on baseline 2.367, <1%) is within noise. While the negative result is directionally consistent, it is not conclusive. The paper's own "Statistical caveats" paragraph essentially admits this.

- **Cross-model chains are confounded.** The cross-model chain experiment (F1=0.809) uses stratified 5-fold CV rather than LOGO, making it non-comparable to the main LOGO results. The higher performance could reflect easier discrimination when multiple generators introduce diverse artifacts rather than genuine depth signal robustness.

- **Remaining TODO markers in the manuscript.** Multiple sections contain unresolved TODO comments (appendix_lofo.tex line 1, appendix_qlora.tex line 4, appendix_human_edit.tex line 1, results.tex line 53, related_work.tex line 11), indicating the paper is not submission-ready.

### 4. Questions for Authors

1. **Instruct model path forward:** Given that depth signal vanishes for instruction-tuned models, what specific mechanism do you hypothesize could recover it? Is there any preliminary evidence that a different feature set (e.g., syntactic or discourse-level features) could capture depth in instruct chains? Without this, the practical motivation (detecting recursive contamination in web data) is undermined.

2. **Corpus-level estimation accuracy:** You claim corpus-level depth composition estimation is reliable via O(1/sqrt(n)) error scaling. Can you provide empirical validation -- e.g., estimating the proportion of gen-2+ text in a mixed corpus at various corpus sizes and reporting calibration?

3. **Why not include learned features alongside handcrafted ones?** QLoRA achieves 3-class F1=0.905 vs. XGBoost's 0.762 -- a +14.3pp gap. This suggests the handcrafted features are a very lossy summary. Have you considered a hybrid: using the 7 handcrafted features for interpretability analysis while deploying the learned model for actual classification? This would strengthen both the diagnostic and practical contributions.

4. **Sensitivity to generation prompt wording:** You use a fixed continuation prompt. How sensitive are results to minor rephrasing of the generation prompt? The prompt-type analysis shows elaboration/rewriting chains have weaker signal, but within "continuation," small variations in the prompt template could also matter.

5. **The 4-detector+surface ensemble:** This baseline achieves 3-class F1=0.771, very close to your 7-feature ensemble (0.762). In binary, it is 0.690 vs 0.694 (not significant). Given that practitioners already have access to these detectors, what is the practical argument for your simpler features over the existing pipeline? Computational efficiency alone seems insufficient if the task itself (depth estimation of base-model text) has limited real-world application.

### 5. Missing References or Related Work

- **Watermark decay analysis:** The paper cites chainwash but does not discuss depth-dependent watermark degradation as a potential complementary signal.
- **Perplexity filtering at scale:** Wenzek et al. (2020, CCNet) and the FineWeb paper characterize perplexity distributions of web text; connecting to their findings about perplexity strata would strengthen the data quality narrative.
- **Membership inference literature:** Min-k% is cited briefly, but the connection to membership inference (detecting whether text was in training data) deserves more discussion since reference-model NLL features overlap heavily with MI features.
- **Repetition and n-gram statistics:** Holtzman et al. (2020) on degeneration and Welleck et al. (2020) on neural text degeneration document repetition in recursive/long generation; these are natural comparisons for the diversity decline.
- **Multi-class synthetic text detection:** The SemEval-2024 Task 8 citation is present but the connection to multi-generator attribution (e.g., source attribution surveys) could be expanded.

### 6. Experiment Coverage Assessment

Comparing against the 5 planned experiments:

1. **Feature ablation and trend (plan_001):** Thoroughly covered. Table of ablation results, LOFO analysis, permutation importance, Spearman correlations with depth, three-tier response characterization. The cross-reference model validation adds value beyond the original plan.

2. **Cross-generator evaluation (plan_002):** Well covered. 8-generator LOGO, 5-family LOFO, per-generator CIs, and cross-scale analysis. The expansion from the original 5-generator plan to 8 generators across 5 families strengthens this significantly.

3. **Paraphrastic comparison (plan_006):** Covered in Discussion section rather than Results, making it feel secondary. The contamination issue (reversed correlations requiring data cleaning) raises concerns about data quality. Results (binary F1=0.671 vs 0.749 for continuation) are interesting but the treatment is brief.

4. **Finer-grained ordinal (plan_009):** Adequately covered in Appendix. The finding that gen-2/gen-3 are inseparable (F1 ~0.24) supports the 3-class design. Ordinal regression comparison (CORAL, Frank-Hall) is mentioned but specific numbers are marked TODO for update.

5. **End-to-end classifier (plan_012):** Covered in Appendix. QLoRA results (+14.3pp) are compelling but the LOGO gap analysis mentioned in the summary (CV F1=0.89 vs LOGO F1=0.72, 17pp gap) seems to be from an older result set -- the current paper reports 0.905 3-class LOGO F1 without reporting a CV-vs-LOGO gap, which would have been informative about overfitting.

**Downstream result:** Mentioned in one brief paragraph in Results and one appendix section. Statistically underpowered (n=3), and the paper acknowledges this. The experiment is honest but not well-controlled enough to draw strong conclusions either way.

### 7. Overall Assessment

- **Soundness (3/5):** Core claims about differential depth response are well-supported empirically for base models. However, the instruct-model failure fundamentally limits the scope of what can be concluded about "recursive LLM generation" broadly. Some statistical tests are underpowered. The mechanistic hypothesis is plausible but remains speculative.

- **Novelty (4/5):** The task formulation (ordinal depth estimation) is genuinely novel. The differential depth response characterization, while following straightforwardly from location-shift properties as the authors acknowledge, is a useful empirical contribution. The combination of negative downstream result + positive diagnostic result is a mature framing.

- **Significance (2/5):** The limitation to base models severely constrains practical significance. With instruct models showing near-zero depth signal, the framework cannot address its motivating application (characterizing web contamination). The negative downstream result further reduces actionability. The primary value is scientific understanding of recursive generation dynamics in a controlled setting.

- **Clarity (4/5):** The paper is well-organized and clearly written. Evaluation protocol is transparent, limitations are honestly discussed, and the framing is appropriately calibrated. The remaining TODO markers are a distraction. The Discussion section covers many important dimensions but is dense.

- **Overall Score: 3 (Weak Reject)**

  The paper introduces a genuinely novel task formulation and conducts thorough experiments with admirable transparency about limitations. The differential depth response characterization is a solid empirical contribution. However, the practical impact is severely undermined by two findings within the paper itself: (1) depth signal vanishes for instruction-tuned models, which produce virtually all real-world LLM text, and (2) depth-aware curation provides no downstream benefit. This leaves the work as an intellectually interesting controlled study of base-model recursive generation dynamics -- valuable for understanding, but with unclear path to practical relevance. The modest absolute performance (binary F1=0.694, per-document error rate 36%), single-domain evaluation (Wikipedia only), and remaining TODO markers in the manuscript further weaken the submission. For a venue like EMNLP, I would want either stronger practical applicability or deeper theoretical insight (e.g., proving convergence rates, connecting to information-theoretic bounds on depth distinguishability).

- **Confidence (4/5):** I have read the full paper carefully including all appendices and am familiar with the related literature on synthetic text detection, model collapse, and data curation. My uncertainty is primarily around whether the community would value this as a "characterization study" even without immediate practical application -- different reviewers may weight novelty-of-formulation vs. practical-impact differently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b67ddde-3dfe-4a33-905a-679d4308fcca",
  "isSidechain": true,
  "agentId": "adcca37aec0a4bd30",
  "requestId": "req_011Cb6ZNY7aeN1V9auUyduAU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69299ddd-d6e4-4021-ba37-8f53b30495df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ec2149a7-b6c7-4246-a1a9-e6c336a9e562",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSe8HjtJGwS7pnvJ8pcF1F",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 46495,
      "output_tokens": 3312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3312,
          "cache_read_input_tokens": 46495,
          "cache_creation_input_tokens": 1037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1037,
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
