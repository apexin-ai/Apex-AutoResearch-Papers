# Research conversation: You are a reviewer for a top ML venue (acceptance rate ~25%). Perform a thorough, blind review of the paper described be

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a7a40be56b4cc5cf2.jsonl`
- **Structured JSON:** [`9c100cf51de170f130f3.json`](../../sessions/9c/9c100cf51de170f130f3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-16T16:19:27.694Z_

You are a reviewer for a top ML venue (acceptance rate ~25%). Perform a thorough, blind review of the paper described below. Use a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept.

## Paper Summary

**Title:** Distributional Depth Profiling: Ordinal Estimation of Recursive LLM Generation Depth via Differential Feature Response

**Core Idea:** The paper introduces "ordinal depth estimation" — instead of binary real/synthetic detection, predict how many recursive LLM generation steps a text has undergone (generation depth). It identifies "differential depth response": central-tendency features (entropy mean, TTR, hapax ratio) drift monotonically with depth while shape features (entropy std, tail decay) remain stationary. A 7-feature XGBoost ensemble achieves 0.83 within-generator F1 and 0.81 LOGO F1 across 5 generators from 3 families.

**Structure (10 pages):**
1. Introduction — motivates recursive generation chains, binary detection limitations, proposes ordinal depth estimation
2. Related Work — binary detection (DetectGPT, Binoculars, Fast-DetectGPT, DNA-GPT), model collapse literature, data quality/provenance, stylometry
3. Method — problem formulation, chain construction (continuation + paraphrastic), 7 distributional features (4 drifting + 3 stationary) via Pythia-410M reference model, XGBoost + ordinal methods, LOGO evaluation
4. Experiments:
   - 4.1 Feature ablation: Full 7-feat=0.832, Surface-only(2)=0.774, Reference-only(5)=0.738; per-feature depth trends with clean drift/stationary partition (R²>0.88 vs R²<0.20); perplexity validation (13.5→1.72 across depths, ρ=−0.92)
   - 4.2 Cross-generator: 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B), LOGO avg F1=0.81 [0.798,0.822], std=0.032; leave-one-family-out only −1.5pp additional degradation; feature importance: hapax_ratio(0.285), ttr(0.172), entropy_mean(0.165)
   - 4.3 Paraphrastic vs continuation: continuation 3-class F1=0.79 vs paraphrastic 0.74; consistent drift direction but attenuated magnitude in paraphrastic; cross-transfer F1=0.74–0.77
   - 4.4 Finer-grained 5-class ordinal: F1=0.51 (vs 3-class 0.79), concordance=0.82; gen-2/gen-3 42% confusion; ordinal methods (CORAL, Frank-Hall) no improvement over XGBoost
   - 4.5 End-to-end QLoRA: Qwen3-0.6B reaches 0.91 3-class within-gen but 0.72 LOGO (−19pp gap); XGBoost maintains 0.79 LOGO (stable); E2E gains concentrate at shallow depths
5. Discussion — location-shift interpretation, architecture invariance, practical ceiling at 3-class, interpretability vs accuracy tradeoff, paraphrastic vs continuation analysis
6. Limitations — generator scale (≤2.8B), single-model chains, reference model dependency, depth resolution ceiling, no post-processing robustness
7. Conclusion

**Tables:** 10 tables total (feature ablation, depth trends, LOGO, family-out, para vs cont, drift comparison, granularity, 5-class per-depth, E2E comparison, per-depth E2E breakdown)
**References:** ~16 entries

## Imagined Experiment Coverage Check

The experiment design document lists these 5 planned experiments:
1. **feature_ablation_and_trend** (plan_001) — feature ablation full/ref-only/surface-only, per-feature depth trend, perplexity validation → COVERED in §4.1
2. **cross_generator_evaluation** (plan_002) — 5-gen LOGO, leave-one-family-out, feature ablation under LOGO → COVERED in §4.2
3. **paraphrastic_comparison** (plan_006) — parallel paraphrastic vs continuation chains, cross-transfer → COVERED in §4.3
4. **finer_grained_ordinal** (plan_009) — 5-class ordinal, per-depth F1, ordinal methods comparison → COVERED in §4.4
5. **end_to_end_classifier** (plan_012) — QLoRA fine-tuned classifiers, within-gen vs LOGO comparison → COVERED in §4.5

All 5 imagined experiments appear to be reported in the paper.

## Your Review Task

Produce a structured review with these sections:

### 1. Summary (3-5 sentences)
What the paper does and its main claims.

### 2. Strengths (bulleted, 4-8 items)
Be specific. Cite table/section numbers.

### 3. Weaknesses (bulleted, 4-8 items)
Be specific and constructive. For each weakness, indicate severity: (major) or (minor).

### 4. Questions for Authors (3-5 specific questions)

### 5. Missing Experiments or Analysis
Compare against the experiment design (5 planned experiments). Note any gaps in coverage, missing ablations, or experiments that were planned but not adequately reported.

### 6. Soundness (1-5 scale)
Are the claims well-supported by the evidence?

### 7. Significance (1-5 scale)
How important is this contribution?

### 8. Novelty (1-5 scale)
How new are the ideas or methods?

### 9. Clarity (1-5 scale)
How well-written and organized is the paper?

### 10. Overall Score (1-6 scale)
With 1-sentence justification.

### 11. Confidence (1-5 scale)
Your confidence in this assessment.

### 12. Recommendation
Accept / Weak Accept / Weak Reject / Reject, with 2-3 sentence justification.

Be rigorous. Top venues reject ~75% of submissions. Evaluate whether this paper makes a sufficient contribution for a top ML venue. Consider: novelty of the task formulation, strength of empirical evidence, theoretical depth, practical impact, limitations of the experimental setup (model scale, chain construction realism, etc.).


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b1a4d8f4-e741-4f98-be69-bdc664d72658",
  "agentId": "a7a40be56b4cc5cf2",
  "type": "user",
  "uuid": "28cef7c2-a03b-4200-bc2f-2285464a304b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T16:19:27.700Z_

```json
{
  "parentUuid": "28cef7c2-a03b-4200-bc2f-2285464a304b",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
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
  "uuid": "cd70487b-6e2d-4a80-9e3a-908d31c56846",
  "timestamp": "2026-05-16T16:19:27.700Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 3 · 2026-05-16T16:19:31.219Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015X88jtxA2JeDFzWdZVccnh`</summary>

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
  "parentUuid": "cd70487b-6e2d-4a80-9e3a-908d31c56846",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
  "requestId": "req_011Cb6YwnseWuAHaw6Threr6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dd8b5ee-0c54-423f-8f51-b3fd657c86f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRwJd1YPtHh5hq2eLNZy9U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16657,
      "cache_read_input_tokens": 0,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16657
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 88,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16657,
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

_source line 4 · 2026-05-16T16:19:31.224Z_

<details><summary>↩ Tool result · `toolu_015X88jtxA2JeDFzWdZVccnh`</summary>

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
  "parentUuid": "0dd8b5ee-0c54-423f-8f51-b3fd657c86f7",
  "isSidechain": true,
  "promptId": "b1a4d8f4-e741-4f98-be69-bdc664d72658",
  "agentId": "a7a40be56b4cc5cf2",
  "type": "user",
  "uuid": "7b01d2b2-82a8-42bb-8b10-911aca84bdeb",
  "sourceToolAssistantUUID": "0dd8b5ee-0c54-423f-8f51-b3fd657c86f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T16:19:34.933Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VjmZsH7SexUwbN9kBT1pqC`</summary>

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
  "parentUuid": "7b01d2b2-82a8-42bb-8b10-911aca84bdeb",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
  "requestId": "req_011Cb6Yx48fxCbbjcrmfjX2Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d0e81d3-cf4e-496a-aa18-6f30c03427e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtUKLNN34Rw29mcwAP1Z26",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 6 · 2026-05-16T16:19:34.946Z_

<details><summary>↩ Tool result · `toolu_01VjmZsH7SexUwbN9kBT1pqC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-fingerprint\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 ARR (deadline: May 25, 2026)** — D012\\n- Fallback: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\\n\\n## Core Insight\\nNon-paraphrastic LLM generation chains exhibit **differential depth response**: **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **distributional shape features** (entropy_std, tail_decay) remain near-stationary. This differential response is consistent with recursive generation inducing a **location shift** in the NLL distribution — the text becomes progressively more predictable (mean shifts) while the functional form of the distribution is preserved (shape is invariant). The genuine novelty is not the drift/stationarity split per se (which follows from location-shift properties), but: (a) the **task formulation** (ordinal depth estimation beyond binary detection), (b) **empirical validation** across 6 generators / 3 model families (including 7B+ scale) showing this pattern is robust, (c) the practical consequence that combining both feature types yields **complementary signal** for depth classification. **Primary metric (D017)**: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, excluding gen-0 due to shared-seed leakage). 3-class LOGO F1 = 0.789 reported as supplementary with gen-0 caveat. Per-generator held-out F1: 0.68–0.86 (std=0.058). Key finding: in binary evaluation (no gen-0 leakage), 7-feature (0.723) > 4-baseline ensemble (0.712) — baseline advantage in 3-class was entirely from gen-0 classification. Depth signal is scale-invariant as a phenomenon, though cross-scale classifier transfer shows a moderate gap (8B held-out F1=0.69 vs ≤2.8B 0.76-0.85).\\n\\n## Core Claims (3 条，均可证伪)\\n\\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth with F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation). Primary metric: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, gen-0 excluded due to shared-seed overlap). 3-class (gen-0/gen-1/gen-2+) LOGO F1 = 0.789 supplementary with caveat.\\n\\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Depth-dependent features exhibit differential response: central-tendency/diversity features (entropy_mean, TTR, hapax_ratio) drift monotonically with depth (consistent with location shift in NLL distribution), while shape features (entropy_std, tail_decay) remain near-stationary. In binary eval, 7-feature ensemble (0.723) outperforms 4-baseline detector ensemble (0.712) by +1.1pp and all individual detectors (+1.1–19.9pp). The 4-baseline advantage in 3-class (0.796 vs 0.789) is entirely from gen-0 classification. Ordinal-specific methods (CORAL 0.771, Frank-Hall 0.793) do not outperform XGBoost (0.789) — CI overlap at 3-class granularity.\\n\\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality compared to random subsampling. At equal data count, size_matched (random control, ppl=2.367) outperforms depth01 (depth-stratified, 2.387) and binary_filtered (2.389). The primary determinant is data quantity, not depth composition (all 12K samples → ppl=2.335). Depth fingerprinting is an effective **diagnostic** tool for characterizing provenance, but not a **curative** tool for data curation. This honest negative finding is reported transparently.\\n\\n## Story Spine\\n\\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\\n\\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation. When repurposed as ordinal depth predictors, single detector scores (Avg-LogProb 0.737, LD-Score 0.655, FastDetectGPT 0.688, Binoculars 0.417 under 6-gen LOGO) show moderate signal but **high per-generator F1 variance** (e.g., AvgLogProb range 0.615–0.805, 19.0pp span), making them unreliable as standalone depth estimators.\\n\\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing **differential depth response**: level/diversity features (including reference-model entropy_mean) drift monotonically with depth, while distributional shape features (entropy variance, tail decay) remain near-stationary. This split is about **what the feature measures** (central tendency vs shape), not where it comes from. The combination of drifting and stationary features yields a 7-feature ensemble that **significantly and consistently** outperforms all single-detector baselines: binary LOGO F1 = 0.723 (gen-1 vs gen-2+, p<0.001 vs Avg-LogProb 0.712, LD-Score 0.701, FastDetectGPT 0.616, Binoculars 0.524). In the leak-free binary evaluation, 7-feature (0.723) > 4-baseline ensemble (0.712), reversing the 3-class result where baseline advantage came entirely from gen-0 classification. The practical advantage is **reliability across unknown generators** — per-generator F1 std = 0.058 for our ensemble vs higher variance for individual detectors.\\n\\n**Headline result template**: \\\"On non-paraphrastic continuation chains across 6 base-model generators from 3 model families (0.6B–8.2B), our 7-feature distributional ensemble achieves binary LOGO F1 of 0.72 for leak-free depth discrimination (gen-1 vs gen-2+), outperforming all individual detection baselines. Per-generator held-out F1 ranges from 0.68 to 0.86 (std=0.051). Depth-aware data curation does not outperform random subsampling for downstream CLM quality, establishing depth fingerprinting as a diagnostic tool for provenance characterization, not a curative tool for data selection.\\\"\\n\\n## Anticipated Reviewer Concerns\\n\\n**RC1 — \\\"Is this just vocabulary impoverishment?\\\"**: Surface features alone achieve 0.73 macro-F1, but full 7-feature ensemble achieves 0.789 3-class / 0.723 binary (p<0.001). We don't claim reference features are \\\"better\\\" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting level/diversity). Note: \\\"fingerprint\\\" in the paper refers to the full feature vector's combination, not just reference-model features.\\n\\n**RC7 — Pre-registered prediction (LD-Score)**: LD-Score (character-distribution signature) measures character-level distributional properties. We predict it is a **level feature** (sensitive to vocabulary/character frequency shifts) and should exhibit **H₂ drift** with depth. This prediction is registered before plan_011 execution as an out-of-sample test of the level/shape framework.\\n\\n**RC2 — \\\"Does this generalize beyond Pythia?\\\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\\n\\n**RC3 — \\\"Is 3-class sufficient? Why not finer-grained?\\\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\\n\\n**RC4 — \\\"How realistic are single-model chains?\\\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\\n\\n**RC5 — \\\"What about human editing / post-processing?\\\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\\n\\n**RC6 — \\\"Ecological validity — continuation vs real web content\\\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\\n\\n**RC8 — \\\"Aren't these just OOD detection features?\\\"**: Reference-model entropy statistics are functionally NLL-based OOD scores (same signal backbone as DetectGPT/GLTR/Binoculars). Our contribution is NOT the features themselves but: (a) the problem formulation (ordinal depth estimation, not binary detection), (b) the empirical discovery that these features exhibit dual dynamics (level drift vs shape stationarity) under recursive generation, and (c) the practical application to risk-stratified data curation. Paper must explicitly connect to OOD detection + perplexity-based detection literature and position the contribution as primarily empirical/conceptual rather than methodological.\\n\\n**RC9 — \\\"Only ≤2.8B generators — does this transfer to frontier scale?\\\"**: **Answered (plan-014, D011).** Qwen3-8B (7.6B params) added as 6th generator. Depth signal IS present at 8B scale — all feature-depth Spearman correlations significant. Cross-scale transfer gap: 8B held-out F1=0.69 vs ≤2.8B 0.76-0.85. P0-B volume-matched control: adding Qwen3-8B's +1.1pp improvement is 94% from generator diversity, not data volume. **Paper framing**: depth signal universality supported; cross-scale gap is honest limitation; scope narrowed to base models (see N3/N4 fixes).\\n\\n**RC10 — \\\"Text length confound\\\"**: Hapax ratio and TTR are mechanically length-dependent. If generation chains produce texts of systematically different lengths, surface features may track length artifacts rather than distributional drift. → Length distribution analysis + length-normalized features + length-matched comparison (plan_013). Critical confound control.\\n\\n**RC11 — \\\"Downstream utility — single run, no CIs\\\"**: Depth-aware filtering advantage must be validated with multiple seeds + bootstrap CIs + sample-count-matched comparison (to control for data size confound). Must use non-Pythia model for downstream fine-tuning (OLMo-1B) to avoid reference model circularity (Pythia-410M as both feature extractor and eval model).\\n\\n## Contribution Positioning (D006+D007)\\nThe contribution is **primarily empirical and conceptual**, not methodological:\\n1. **Problem formulation**: Ordinal depth estimation as a new task beyond binary detection (genuinely novel — no prior work)\\n2. **Empirical characterization**: Differential depth response across 6 generators / 3 families (including 7B+ scale), with robust cross-generator generalization (binary LOGO F1=0.723, 3-class LOGO F1=0.789). Scale-invariant phenomenon with honest cross-scale transfer gap.\\n3. **Negative finding**: Depth-aware data curation does NOT improve downstream CLM quality — depth fingerprinting is diagnostic, not curative (D009).\\n\\n**Framing discipline (D007 — re-dream consensus):**\\n- Do NOT call the drift/stationarity split a \\\"discovery\\\" — it follows from location-shift properties of the NLL distribution (means shift under distributional drift, shapes don't). Acknowledge this explicitly.\\n- Do NOT use H1/H2 terminology (overloads time-series unit-root convention). Use \\\"drifting\\\" vs \\\"stationary\\\" or \\\"differential response.\\\"\\n- Do NOT overclaim \\\"dual dynamics\\\" as a novel theoretical framework. Use \\\"differential depth response\\\" — more calibrated.\\n- Consider renaming \\\"distributional fingerprinting\\\" → \\\"distributional depth profiling\\\" (fingerprinting implies source identification, creates confusion with LLM attribution literature).\\n- Provide at least a speculative theoretical motivation for WHY shape features remain stationary (e.g., \\\"shape is determined by sampling mechanism and architecture, invariant to input content drift\\\").\\n- Report **realistic performance range** (0.68–0.86 per-generator held-out F1, binary LOGO F1=0.\\n\\n... [截断: 省略 1630 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 13630, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d0e81d3-cf4e-496a-aa18-6f30c03427e3",
  "isSidechain": true,
  "promptId": "b1a4d8f4-e741-4f98-be69-bdc664d72658",
  "agentId": "a7a40be56b4cc5cf2",
  "type": "user",
  "uuid": "2e03e7c7-1192-4b25-b572-ff348ab438c6",
  "sourceToolAssistantUUID": "0d0e81d3-cf4e-496a-aa18-6f30c03427e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T16:19:35.403Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RuZZRqEKkEbupFQ9iep8Ri`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "ROADMAP.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e03e7c7-1192-4b25-b572-ff348ab438c6",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
  "requestId": "req_011Cb6Yx48fxCbbjcrmfjX2Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1ef6f6c-d6a5-401d-a996-50966fa1318b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtUKLNN34Rw29mcwAP1Z26",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16657,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1269
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 16657,
          "cache_creation_input_tokens": 1269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1269,
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

_source line 8 · 2026-05-16T16:19:35.412Z_

<details><summary>↩ Tool result · `toolu_01RuZZRqEKkEbupFQ9iep8Ri`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ROADMAP.md\", \"content\": \"## 核心方向\\n\\n> 最后更新: 2026-05-16 12:56 UTC | 更新原因: D038 定稿后全面更新：9-gen/6-family→8-gen/5-family，移除过时 phases，对齐 Reviewer critical\\n\\n递归 LLM 生成链展现 **differential depth response**：central-tendency/diversity 特征随深度漂移，shape 特征近稳态。7-feature ensemble 跨 **8 base-model generators / 5 families** 验证（D038 定稿：全部 rp=1.0 unfiltered）。**Primary metric (D017)**: binary LOGO F1（gen-1 vs gen-2+, leak-free）；3-class LOGO F1 supplementary。详见 paper_framing.md。\\n\\n## 投稿目标\\n- **主投: EMNLP 2026 ARR (DDL: 2026-05-25)** — ~9 天倒计时\\n- **策略**: 8-gen/5-family scope，D038 最终确定\\n\\n## 当前进展\\n- **阶段**: 论文数字更新（关键路径） + Gemma appendix 收尾\\n- **Main results 已完成**: 8-gen LOGO binary F1=0.694, 3-class=0.762 ✅\\n- **D038 定稿**: 8-gen rp=1.0 unfiltered main; Gemma rp=1.1 appendix only (rp-LOFO F1=0.518 FAIL)\\n- **Paper Agent**: 全文 scope+数字 Patch 进行中（6-gen→8-gen 更新）🔄\\n- **Gemma rp=1.1**: generation 进行中 (cuda:1, ~18% 进度) — appendix 用\\n\\n## 近期任务\\n\\n**最高优先级 — 论文数字更新：**\\n- [ ] Paper Agent 全文 Patch: abstract/intro/results/conclusion 数字 6-gen→8-gen\\n- [ ] 验证 discussion.tex \\\"16.9% depth retention loss\\\" 和 \\\"CV F1=0.781\\\" 来源\\n\\n**Gemma appendix（非阻塞）：**\\n- [ ] Gemma rp=1.1 generation 完成 → feature extraction\\n- [ ] Cross-rp analysis for appendix\\n- [ ] rp-LOFO 用修正 tail_decay 重跑（更新 appendix 数字，不影响 D038）\\n\\n**最终冲刺：**\\n- [ ] Round 5 内部审查 (submit_paper_to_review)\\n- [ ] 最终编译 + 提交\\n\\n## Claim 证据状态\\n| Claim | 状态 | 关键证据 |\\n|-------|------|---------|\\n| 1 — Depth Discriminability | ✅ | binary F1=0.694, 3-class=0.762 (8-gen LOGO) |\\n| 2 — Differential Depth Response | ✅ | 三档分类 D032, 3 ref models, 3 prompt types, length-controlled |\\n| 3 — Downstream Utility | ⬇️ 降级 (D029) | supplementary analysis only |\\n| Baseline comparison | ✅ | 7-feat ≈ 4-det+surface; 贡献在 simplicity + interpretability |\\n\\n## GPU 预算\\n- 分配: 4× RTX 5090 (autodl-5090: cuda:0-3)\\n- 当前: 1/4 活跃（cuda:1 Gemma generation），cuda:0/2/3 空闲\\n- Main results 计算已完成，剩余 GPU 需求仅 Gemma appendix + rp-LOFO rerun\\n- 已消耗: ~75h / 200h\\n\\n## rp-LOFO Gate 结果（D038）\\n- Llama proxy F1=0.518 → **FAIL** (< 0.60 threshold)\\n- 结论：Gemma rp=1.1 仅 appendix，main 报告 8-gen rp=1.0\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D038 | 2026-05-16 | D038: 最终论文策略 — 8-gen rp=1.0 unfiltered main result | plan-016-llama32-3b, plan-016-mistral-7b, plan-016-llama32-3b-rp11, plan-016-gemma2-2b |\\n| D037 | 2026-05-16 | D037: 撤回 D036 filter 策略。8/9 gen 不过滤（含自然退化），仅 Gemma | plan-016-llama32-3b, plan-016-mistral-7b |\\n| D036 | 2026-05-16 | D036: 撤回 D035，恢复 Llama rp=1.0+filter。最终 8/9 rp=1.0 | plan-016-llama32-3b, plan-016-llama32-3b-rp11 |\\n| D035 | 2026-05-16 | D035: D034 修正 — Llama 也需 rp=1.1。最终 7/9 rp=1.0 (原6+ | plan-016-llama32-3b, plan-016-llama32-3b-rp11, plan-016-mistral-7b, plan-016-gemma2-2b |\\n| D034 | 2026-05-16 | D034: Plan-016 rp 策略修正 — Llama/Mistral 用 rp=1.0（退化 | plan-016-llama32-3b, plan-016-llama32-3b-rp11, plan-016-mistral-7b, plan-016-gemma2-2b |\\n| D033 | 2026-05-16 | Plan-016 策略：rp=1.1 新模型纳入 main results（9-gen/6-fami | plan-016-llama32-3b-rp11 |\\n| D032 | 2026-05-16 | Pooled ρ 修正 → 三档分类替代二分法: strong drift (hapax/TTR/e | spearman_per_generator, plan-014 |\\n| D031 | 2026-05-16 | H_min reclassified as drifting feature; shape stat | spearman_per_generator |\\n| D030 | 2026-05-16 | Round 3 审稿 3.0/Findings: 大幅重写 framing 为 base-model | review-p0a-gen0-leakage, plan-004-v2, review-p1c-qwen06b-instruct |\\n| D029 | 2026-05-16 | Round 3 审稿处理：大幅重写 framing (base-model scope)，downs | review-p1c-qwen06b-instruct, review-p1c-olmo-instruct, plan-004-v2 |\\n\\n\\n\", \"total_chars\": 3422, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1ef6f6c-d6a5-401d-a996-50966fa1318b",
  "isSidechain": true,
  "promptId": "b1a4d8f4-e741-4f98-be69-bdc664d72658",
  "agentId": "a7a40be56b4cc5cf2",
  "type": "user",
  "uuid": "ebab376e-9a53-4f18-a5b4-b85c699b13cb",
  "sourceToolAssistantUUID": "b1ef6f6c-d6a5-401d-a996-50966fa1318b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T16:19:39.880Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KTfLn9p178UgZZizTz2B1x`</summary>

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
  "parentUuid": "ebab376e-9a53-4f18-a5b4-b85c699b13cb",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
  "requestId": "req_011Cb6YxMwV95adFhP36NX7S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2babc6f-7b4c-4c24-a3a4-73faa5de1609",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LfcLQQPvQWEZaL5m4Ph2gD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5889,
      "cache_read_input_tokens": 17926,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5889
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 17926,
          "cache_creation_input_tokens": 5889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5889,
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

_source line 10 · 2026-05-16T16:19:39.905Z_

<details><summary>↩ Tool result · `toolu_01KTfLn9p178UgZZizTz2B1x`</summary>

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
  "parentUuid": "e2babc6f-7b4c-4c24-a3a4-73faa5de1609",
  "isSidechain": true,
  "promptId": "b1a4d8f4-e741-4f98-be69-bdc664d72658",
  "agentId": "a7a40be56b4cc5cf2",
  "type": "user",
  "uuid": "362289e3-bd1c-4d62-9681-d3855b8bab90",
  "sourceToolAssistantUUID": "e2babc6f-7b4c-4c24-a3a4-73faa5de1609",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T16:19:43.043Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XVcQRxpzt2jFKupQaoXAtP`</summary>

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
  "parentUuid": "362289e3-bd1c-4d62-9681-d3855b8bab90",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
  "requestId": "req_011Cb6YxhPXHzaerCmLDYTPW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65398b32-edbf-4e75-8b12-8d234231fb6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESgZWYJWCpwJyztkWiFbKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 392,
      "cache_read_input_tokens": 23815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 12 · 2026-05-16T16:19:43.056Z_

<details><summary>↩ Tool result · `toolu_01XVcQRxpzt2jFKupQaoXAtP`</summary>

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
  "parentUuid": "65398b32-edbf-4e75-8b12-8d234231fb6a",
  "isSidechain": true,
  "promptId": "b1a4d8f4-e741-4f98-be69-bdc664d72658",
  "agentId": "a7a40be56b4cc5cf2",
  "type": "user",
  "uuid": "84c65b50-5edf-4c6f-92e5-2139c431da34",
  "sourceToolAssistantUUID": "65398b32-edbf-4e75-8b12-8d234231fb6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T16:19:43.565Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LT7xGieVj3QJ1QU76hgY8M`</summary>

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
  "parentUuid": "84c65b50-5edf-4c6f-92e5-2139c431da34",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
  "requestId": "req_011Cb6YxhPXHzaerCmLDYTPW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4363839-835e-42d7-acb3-a5e4c16e9b33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESgZWYJWCpwJyztkWiFbKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 392,
      "cache_read_input_tokens": 23815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 14 · 2026-05-16T16:19:43.570Z_

<details><summary>↩ Tool result · `toolu_01LT7xGieVj3QJ1QU76hgY8M`</summary>

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
  "parentUuid": "c4363839-835e-42d7-acb3-a5e4c16e9b33",
  "isSidechain": true,
  "promptId": "b1a4d8f4-e741-4f98-be69-bdc664d72658",
  "agentId": "a7a40be56b4cc5cf2",
  "type": "user",
  "uuid": "fd71ff1b-f3ad-4ce9-b057-a11f103620fb",
  "sourceToolAssistantUUID": "c4363839-835e-42d7-acb3-a5e4c16e9b33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T16:19:43.980Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KAU5K4FiTLGYSYJrv4AYTU`</summary>

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
  "parentUuid": "fd71ff1b-f3ad-4ce9-b057-a11f103620fb",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
  "requestId": "req_011Cb6YxhPXHzaerCmLDYTPW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "814e8740-4121-4b29-9a8e-f8a9ba346bf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESgZWYJWCpwJyztkWiFbKK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 392,
      "cache_read_input_tokens": 23815,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 23815,
          "cache_creation_input_tokens": 392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 392,
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

_source line 16 · 2026-05-16T16:19:43.985Z_

<details><summary>↩ Tool result · `toolu_01KAU5K4FiTLGYSYJrv4AYTU`</summary>

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
  "parentUuid": "814e8740-4121-4b29-9a8e-f8a9ba346bf9",
  "isSidechain": true,
  "promptId": "b1a4d8f4-e741-4f98-be69-bdc664d72658",
  "agentId": "a7a40be56b4cc5cf2",
  "type": "user",
  "uuid": "817cb93b-9c06-49a3-b2fc-26e78766ad09",
  "sourceToolAssistantUUID": "814e8740-4121-4b29-9a8e-f8a9ba346bf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T16:19:49.511Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RgAAEE7XpCSegawrLh8kLL`</summary>

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
  "parentUuid": "817cb93b-9c06-49a3-b2fc-26e78766ad09",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
  "requestId": "req_011Cb6YxzeM69p7dS6NqVaGP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58a8f160-cde7-42a5-b279-afbc157e41f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgD7ECq1h4rZkouprBb2kX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4939,
      "cache_read_input_tokens": 24207,
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

_source line 18 · 2026-05-16T16:19:49.520Z_

<details><summary>↩ Tool result · `toolu_01RgAAEE7XpCSegawrLh8kLL`</summary>

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
  "parentUuid": "58a8f160-cde7-42a5-b279-afbc157e41f6",
  "isSidechain": true,
  "promptId": "b1a4d8f4-e741-4f98-be69-bdc664d72658",
  "agentId": "a7a40be56b4cc5cf2",
  "type": "user",
  "uuid": "ecb15432-9bd8-499c-ba2b-447304dc7ecc",
  "sourceToolAssistantUUID": "58a8f160-cde7-42a5-b279-afbc157e41f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T16:19:50.036Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NvVvwz7SAE6wtdWizpAeUS`</summary>

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
  "parentUuid": "ecb15432-9bd8-499c-ba2b-447304dc7ecc",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
  "requestId": "req_011Cb6YxzeM69p7dS6NqVaGP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6ca4390-2727-42af-a98c-b2fb79cf2541",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgD7ECq1h4rZkouprBb2kX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4939,
      "cache_read_input_tokens": 24207,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4939
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 24207,
          "cache_creation_input_tokens": 4939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4939,
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

_source line 20 · 2026-05-16T16:19:50.041Z_

<details><summary>↩ Tool result · `toolu_01NvVvwz7SAE6wtdWizpAeUS`</summary>

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
  "parentUuid": "f6ca4390-2727-42af-a98c-b2fb79cf2541",
  "isSidechain": true,
  "promptId": "b1a4d8f4-e741-4f98-be69-bdc664d72658",
  "agentId": "a7a40be56b4cc5cf2",
  "type": "user",
  "uuid": "3ae87858-bd84-434c-8a93-987dde4ed0d3",
  "sourceToolAssistantUUID": "f6ca4390-2727-42af-a98c-b2fb79cf2541",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T16:19:54.458Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SFWnXbQ9QNP37bHHySLFZW`</summary>

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
  "parentUuid": "3ae87858-bd84-434c-8a93-987dde4ed0d3",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
  "requestId": "req_011Cb6YySenLxgi4ssdGRb4q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac6222cb-3cab-4950-b27a-5a7b7eef9db3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEvgxaJQ18Gdr7kA25Kq7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7486,
      "cache_read_input_tokens": 29146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7486,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 22 · 2026-05-16T16:19:54.464Z_

<details><summary>↩ Tool result · `toolu_01SFWnXbQ9QNP37bHHySLFZW`</summary>

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
  "parentUuid": "ac6222cb-3cab-4950-b27a-5a7b7eef9db3",
  "isSidechain": true,
  "promptId": "b1a4d8f4-e741-4f98-be69-bdc664d72658",
  "agentId": "a7a40be56b4cc5cf2",
  "type": "user",
  "uuid": "5e4b4233-56e5-47c2-b7a5-4b4c17d27fd1",
  "sourceToolAssistantUUID": "ac6222cb-3cab-4950-b27a-5a7b7eef9db3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T16:19:55.503Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PovWqMK2W3Vr3RphDL7EfQ`</summary>

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
  "parentUuid": "5e4b4233-56e5-47c2-b7a5-4b4c17d27fd1",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
  "requestId": "req_011Cb6YySenLxgi4ssdGRb4q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c1b4b53-a35a-4024-9a8a-d7dbb8cf904c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEvgxaJQ18Gdr7kA25Kq7R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7486,
      "cache_read_input_tokens": 29146,
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
          "cache_read_input_tokens": 29146,
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

### Tool call

_source line 24 · 2026-05-16T16:19:55.507Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fv3h63AzXMU8dTYSJz3TUC`</summary>

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
  "parentUuid": "0c1b4b53-a35a-4024-9a8a-d7dbb8cf904c",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
  "requestId": "req_011Cb6YySenLxgi4ssdGRb4q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97ad40d2-001d-4fb7-ade6-c164b65678e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEvgxaJQ18Gdr7kA25Kq7R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7486,
      "cache_read_input_tokens": 29146,
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
          "cache_read_input_tokens": 29146,
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

_source line 25 · 2026-05-16T16:19:55.513Z_

<details><summary>↩ Tool result · `toolu_01PovWqMK2W3Vr3RphDL7EfQ`</summary>

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
  "parentUuid": "0c1b4b53-a35a-4024-9a8a-d7dbb8cf904c",
  "isSidechain": true,
  "promptId": "b1a4d8f4-e741-4f98-be69-bdc664d72658",
  "agentId": "a7a40be56b4cc5cf2",
  "type": "user",
  "uuid": "32dc4308-7d0e-43d6-92b3-01cfe79ad191",
  "sourceToolAssistantUUID": "0c1b4b53-a35a-4024-9a8a-d7dbb8cf904c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T16:19:55.514Z_

<details><summary>↩ Tool result · `toolu_01Fv3h63AzXMU8dTYSJz3TUC`</summary>

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
  "parentUuid": "97ad40d2-001d-4fb7-ade6-c164b65678e3",
  "isSidechain": true,
  "promptId": "b1a4d8f4-e741-4f98-be69-bdc664d72658",
  "agentId": "a7a40be56b4cc5cf2",
  "type": "user",
  "uuid": "e9005573-8f1d-4088-b92b-ef48955a9b81",
  "sourceToolAssistantUUID": "97ad40d2-001d-4fb7-ade6-c164b65678e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T16:19:58.649Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Aj7iVR9h1AsTvpHB7KhZGx`</summary>

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
  "parentUuid": "e9005573-8f1d-4088-b92b-ef48955a9b81",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
  "requestId": "req_011Cb6YyqsXbNHAZwQLqwvGC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce64f8cb-927d-4000-8f7f-4bce2ba729dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxkFH7n2ioChmXBG4vdn5n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 36632,
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

_source line 28 · 2026-05-16T16:19:58.655Z_

<details><summary>↩ Tool result · `toolu_01Aj7iVR9h1AsTvpHB7KhZGx`</summary>

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
  "parentUuid": "ce64f8cb-927d-4000-8f7f-4bce2ba729dd",
  "isSidechain": true,
  "promptId": "b1a4d8f4-e741-4f98-be69-bdc664d72658",
  "agentId": "a7a40be56b4cc5cf2",
  "type": "user",
  "uuid": "ac709ea6-cede-45c7-8543-fcd3403a2765",
  "sourceToolAssistantUUID": "ce64f8cb-927d-4000-8f7f-4bce2ba729dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T16:19:59.021Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BJNnr2RLPuSUazngcyRXeU`</summary>

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
  "parentUuid": "ac709ea6-cede-45c7-8543-fcd3403a2765",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
  "requestId": "req_011Cb6YyqsXbNHAZwQLqwvGC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8f38ac2-96d5-4c74-a3a9-aaef1cbbf21d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxkFH7n2ioChmXBG4vdn5n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 36632,
      "output_tokens": 172,
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
          "output_tokens": 172,
          "cache_read_input_tokens": 36632,
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

_source line 30 · 2026-05-16T16:19:59.025Z_

<details><summary>↩ Tool result · `toolu_01BJNnr2RLPuSUazngcyRXeU`</summary>

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
  "parentUuid": "e8f38ac2-96d5-4c74-a3a9-aaef1cbbf21d",
  "isSidechain": true,
  "promptId": "b1a4d8f4-e741-4f98-be69-bdc664d72658",
  "agentId": "a7a40be56b4cc5cf2",
  "type": "user",
  "uuid": "39fbbf3c-e0f5-4256-b397-e51365c42e38",
  "sourceToolAssistantUUID": "e8f38ac2-96d5-4c74-a3a9-aaef1cbbf21d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-16T16:21:18.492Z_

Now I have a thorough understanding of the paper. Let me produce the review.

---

## Review: Distributional Depth Profiling: Ordinal Estimation of Recursive LLM Generation Depth via Differential Feature Response

### 1. Summary

This paper formulates "ordinal depth estimation" as a new task: predicting how many recursive LLM generation steps a text has undergone, going beyond binary real-vs-synthetic detection. The authors identify "differential depth response" where central-tendency features (entropy mean, TTR, hapax ratio) drift monotonically with depth while upper-tail shape features (entropy max, tail decay) remain stationary. A 7-feature XGBoost ensemble achieves binary LOGO F1 = 0.694 across 8 base-model generators from 5 families (0.6B-8B). The paper additionally reports a negative finding that depth-aware data curation does not improve downstream LM quality. The scope is explicitly restricted to base (pretrained) models, with instruct models showing degraded depth signal.

### 2. Strengths

- **Novel and well-motivated task formulation.** Ordinal depth estimation is genuinely new --- no prior work attempts this, and the motivation (web text increasingly contains multi-hop LLM output of varying provenance depth) is timely and practical. The 3-class formulation (gen-0/gen-1/gen-2+) is well-justified by the empirical granularity ceiling.

- **Thorough cross-generator evaluation.** The LOGO protocol across 8 generators from 5 families (Table 1) with confidence intervals, plus LOFO evaluation, provides convincing evidence that the phenomenon is not generator-specific. The spread across families is modest (-0.8pp average for LOFO vs LOGO).

- **Honest treatment of limitations.** The paper explicitly acknowledges the instruct-model failure (F1 drops to 0.338-0.667), the gen-0 leakage issue in 3-class LOGO (addressed via binary primary metric), prompt-type dependence, and the negative downstream finding. This intellectual honesty strengthens credibility.

- **Well-designed controls.** Length confound analysis, cross-family reference models (spread 0.024), sampling sensitivity ablation, alternative classifier comparison, and training size sensitivity all address natural concerns systematically.

- **Informative negative results.** Both the downstream utility finding (depth-aware curation is not curative) and the instruct-model failure are clearly reported and contextualized, providing genuine information value to the community.

- **Clean differential response characterization.** The three-tier partition (strong drift |rho|>0.6, moderate 0.20-0.41, near-stationary <0.05) with a mechanistic location-shift interpretation is elegant and well-supported by Figure 1.

- **Statistical rigor.** Bootstrap CIs, McNemar tests, Bonferroni correction, paired bootstrap for baseline comparisons, seed stability checks (std=0.001 over 5 seeds) --- the statistical methodology is appropriate throughout.

### 3. Weaknesses

- **(Major) Instruct-model failure severely limits practical impact.** The paper restricts to base models, but real-world recursive LLM output is overwhelmingly produced by instruction-tuned models. The dramatic signal collapse (OLMo-Instruct F1=0.338, Qwen-Instruct near chance after length matching) means the core finding has limited applicability to the motivating scenario (web contamination). The introduction frames the problem around web-crawled text, but the solution only works for base models --- a fundamental mismatch between motivation and scope.

- **(Major) Modest absolute performance.** Binary LOGO F1 = 0.694 means approximately 30% of depth predictions are wrong. Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724. The gen-1 per-class F1 of 0.64 implies 36% misclassification. While the paper acknowledges this is suited for corpus-level rather than document-level application, the practical utility at these error rates is unclear, especially given that the task requires only 3 classes.

- **(Major) Feature engineering is incremental over existing detection methods.** The 7-feature ensemble achieves binary F1=0.694 vs the 4-detector+surface ensemble at 0.690 --- a difference of 0.4pp that is explicitly acknowledged as statistically non-significant. The claimed "outperformance" of detection baselines is primarily over individual single-score detectors, not the natural multi-detector ensemble that a practitioner would use. The contribution is thus more about the task formulation than about the method.

- **(Minor) Narrow domain coverage.** All seed texts come from English Wikipedia. No experiments test other domains (news, social media, creative writing, code), languages, or text lengths. Wikipedia has distinctive stylistic properties, and depth drift dynamics may differ substantially in other registers.

- **(Minor) Chain construction is unrealistic.** The chains use a single fixed prompt ("Continue the following text:") with fixed decoding parameters (t=0.7, p=0.9). Real recursive generation involves diverse prompts, varying parameters, editing, and different models at each step. While cross-model chains are tested (F1=0.764-0.809), the cross-prompt results show significant dependence (continuation 0.781 vs elaboration 0.730), raising questions about real-world generalizability.

- **(Minor) Scale ceiling untested.** The largest models are 7-8B. Frontier models (70B+) likely produce text that is harder to distinguish from human text at any depth. The demonstrated degradation from small models (F1~0.72-0.81) to 7-8B models (F1=0.633-0.692) suggests the method may become ineffective at frontier scale, but this is not tested.

- **(Minor) Theoretical depth is limited.** The "location shift with partial shape preservation" account is descriptive rather than predictive. The paper does not derive expected drift rates, convergence properties, or formal connections to information-theoretic quantities. The mechanistic explanation (softmax ceiling constrains upper tail) is plausible but informal.

### 4. Questions for Authors

1. **Instruct models:** Given that the depth signal collapses for instruct models, can you articulate a realistic deployment scenario where base-model depth estimation would be needed? What fraction of web-crawled synthetic text is actually produced by base models?

2. **Marginal value over detection ensembles:** Since the 4-detector+surface ensemble achieves statistically equivalent binary F1 (0.690 vs 0.694), what is the concrete argument for using the 7-feature ensemble beyond interpretability? Does the 4x computational cost argument hold when practitioners typically already have access to detector scores?

3. **Convergence speed vs chain length:** You test chains up to depth 4. At what depth do you expect features to reach a fixed point? Is there evidence that gen-3 and gen-4 have already converged (explaining the 5-class gen-2/gen-3 confusion), and if so, does the 3-class formulation with gen-2+ actually capture a meaningful distinction?

4. **Reference model size sensitivity:** You use Pythia-410M (smaller than all generators). How does reference model size affect results? Would a larger reference model (e.g., Pythia-6.9B) that is closer to or exceeds generator scale change the differential response pattern?

5. **Topic drift confound:** You report topic drift accounts for <9% of feature variance, but this seems measured on a single prompt type. Does semantic narrowing play a larger role in longer chains (depth 3-4) or with elaboration-style prompts?

### 5. Missing Experiments or Analysis

Compared to the 5 planned experiments described in the design document:

1. **Feature ablation and trend (plan_001):** Adequately covered in Section 4.1/4.2. The per-feature depth trends and ablation are reported.

2. **Cross-generator evaluation (plan_002):** Covered with 8 generators. The expansion from the original 5 generators to 8 strengthens this.

3. **Paraphrastic comparison (plan_006):** Covered in the discussion section rather than a dedicated results subsection, with binary F1=0.671 and cross-transfer results. The treatment is somewhat compressed.

4. **Finer-grained ordinal (plan_009):** Covered in appendix with 5-class F1=0.488. Ordinal methods comparison is mentioned but exact numbers with CIs are missing (only "CIs overlapping" is stated).

5. **End-to-end classifier (plan_012):** Mentioned in discussion (QLoRA 3-class F1=0.905, +11.6pp) but relegated to appendix. The within-gen vs LOGO comparison gap that was planned is not fully reported with numbers in the main text.

**Additional gaps:**
- No error analysis or confusion matrix in the main text (only mentioned as appendix)
- No qualitative examples showing what features "look like" at different depths
- No analysis of failure modes (when does the classifier systematically fail?)
- The cross-model chain experiment (mixed generators per step) is mentioned briefly but deserves fuller treatment given its relevance to realistic scenarios

### 6. Soundness: 3/5

The empirical methodology is generally sound with appropriate controls and statistical testing. However, the primary metric (binary F1=0.694) is modest, the practical advantage over detection baselines is statistically non-significant, and the instruct-model failure fundamentally undermines the motivating framing. The gen-0 leakage issue, while handled through binary evaluation, complicates interpretation of 3-class results throughout.

### 7. Significance: 2/5

The task formulation is novel and potentially important, but the practical impact is severely limited by three factors: (1) restriction to base models when real-world synthetic text comes from instruct models, (2) modest absolute performance (F1~0.69), and (3) the negative downstream utility finding removes the most obvious application. The paper is primarily a characterization study of an interesting phenomenon with limited practical consequences in its current form.

### 8. Novelty: 3/5

The ordinal depth estimation task is genuinely novel --- no prior work formulates this problem. The differential depth response characterization is an interesting empirical finding. However, the features themselves (NLL statistics, TTR, hapax ratio) are entirely standard, the classifier (XGBoost) is off-the-shelf, and the observation that recursive generation reduces diversity is not surprising given model collapse literature. The novelty is primarily in the problem formulation and empirical characterization, not in methodology.

### 9. Clarity: 4/5

The paper is well-written and clearly organized. The task formulation, evaluation protocol, and results are presented logically. The discussion section provides good mechanistic interpretation. The honesty about limitations is commendable. Minor issues: some results are spread between main text, discussion, and appendix in ways that make it hard to get the full picture (e.g., paraphrastic results in discussion, QLoRA in appendix only mentioned briefly). The paper has several TODO comments remaining in the LaTeX source.

### 10. Overall Score: 3/6 (Weak Reject)

A well-executed empirical study with a genuinely novel task formulation, but limited practical significance due to the instruct-model failure, modest absolute performance, and non-significant advantage over baseline ensembles.

### 11. Confidence: 4/5

High confidence. The experimental methodology and claims are straightforward to evaluate. I have expertise in text detection and NLP evaluation methodology. Minor uncertainty about whether frontier-scale experiments would change the picture substantially.

### 12. Recommendation

**Weak Reject.** The paper introduces a legitimately novel task (ordinal depth estimation) and provides a thorough empirical characterization within its chosen scope. However, for a top ML venue, the contribution faces three critical issues: (1) the fundamental disconnect between the real-world motivation (web contamination by instruct models) and the method's applicability (base models only, where instruct models show near-zero signal); (2) the primary metric (binary F1=0.694) indicates only moderate discriminability for a 2-class problem, and the advantage over detection baselines is not statistically significant; (3) the negative downstream finding, while honestly reported, removes the clearest practical application. The work would benefit from either demonstrating a path to instruct-model generalization or identifying a concrete application domain where base-model depth estimation has demonstrated utility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39fbbf3c-e0f5-4256-b397-e51365c42e38",
  "isSidechain": true,
  "agentId": "a7a40be56b4cc5cf2",
  "requestId": "req_011Cb6Yz6sBJGnSBEGiKx26z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b0010af-955d-4a41-a592-1e233bf4c51b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "1451c1e1-cfa9-4438-b276-3ed5d963e54a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyBh4dCrzRdKwGAeMwfcsX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2720,
      "cache_read_input_tokens": 39610,
      "output_tokens": 2932,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2720
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2932,
          "cache_read_input_tokens": 39610,
          "cache_creation_input_tokens": 2720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2720,
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
