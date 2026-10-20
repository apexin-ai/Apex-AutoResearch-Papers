# Research conversation: Title EncoGuard: Learning Encoding-Invariant Safety Features via Complexity-Structured Curriculum Training ## Problem St

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/b0da184f-7f91-4b76-a7d1-8dca52f60a8b.jsonl`
- **Structured JSON:** [`df87a8a9b719cb1dbfe6.json`](../../sessions/df/df87a8a9b719cb1dbfe6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T12:19:26.460Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:19:26.460Z",
  "sessionId": "b0da184f-7f91-4b76-a7d1-8dca52f60a8b",
  "content": "## Title\n\nEncoGuard: Learning Encoding-Invariant Safety Features via Complexity-Structured Curriculum Training\n\n## Problem Statement\n\nEncoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, and their nested compositions) exploit a fundamental vulnerability in LLM safety guardrails: classifiers trained on plaintext or limited encoding variations fail catastrophically when inputs are transformed through encoding schemes not seen during training. The core challenge is not merely defending against known encodings, but achieving **generalization to unseen encoding families**—a property that no existing defense reliably provides.\n\n## Core Thesis\n\nWe hypothesize that a classifier trained via **complexity-structured curriculum**—where encoding attacks are presented in order of a principled complexity metric—learns **encoding-invariant harmful-content features** that generalize to held-out encoding types unseen during training. This generalization arises because curriculum ordering enables the classifier to first build robust token-level encoding-detection primitives on simple encodings, which then serve as compositional building blocks for recognizing complex encodings. In contrast, flat augmentation and random-order training suffer from catastrophic confusion: noisy gradients from complex encodings in early training interfere with the formation of these foundational features.\n\nThis principle—that attack spaces with composable primitives and natural complexity ordering benefit from structured curriculum defense—is general beyond encoding attacks. We demonstrate it on the encoding domain as a canonical instance where complexity is formally quantifiable.\n\n## Key Contributions\n\n1. **Primary Contribution (Feature Learning Insight):** We demonstrate that complexity-structured curriculum training produces encoding-invariant representations that generalize to entirely unseen encoding families (Braille, Morse, custom ciphers), while flat augmentation and random-order training do not. This is evidence that curriculum ordering teaches compositional encoding-detection features rather than memorizing specific encoding patterns.\n\n2. **Formalized Encoding Complexity Score (ECS):** We define a principled complexity metric combining nesting depth, character-per-token (CPT) ratio deviation, and tokenizer perplexity, which determines curriculum ordering. We show that ECS predicts classifier difficulty on held-out encodings, validating it as a transferable methodological contribution.\n\n3. **Co-Evolutionary Training Framework:** We instantiate the curriculum principle via a GRPO-trained attacker that generates encoding attacks of escalating ECS, paired with an SFT classifier that trains on curriculum-ordered adversarial data. The co-evolutionary dynamic ensures the curriculum adapts to the classifier's current capability frontier.\n\n4. **Comprehensive Evaluation:** We evaluate on both external benchmarks (HarmBench, JailbreakBench, WildGuardTest with encoding perturbations) and a purpose-built EncoAttack benchmark, with controlled ablations isolating the curriculum ordering effect.\n\n## Methodology\n\n### Encoding Complexity Score (ECS)\n\nWe define ECS for an encoding transformation $e$ as:\n\n$$ECS(e) = \\alpha \\cdot \\text{NestingDepth}(e) + \\beta \\cdot \\text{CPT\\_Deviation}(e) + \\gamma \\cdot \\text{TokenizerPerplexity}(e)$$\n\nwhere:\n- NestingDepth: number of compositional encoding layers (1 for single, 2+ for nested)\n- CPT_Deviation: absolute deviation of the encoded text's characters-per-token ratio from plaintext baseline\n- TokenizerPerplexity: perplexity of the target model's tokenizer on the encoded text\n\nWeights $\\alpha, \\beta, \\gamma$ are set via pilot study measuring classifier error rate correlation. The curriculum presents attacks in monotonically increasing ECS order.\n\n### Mechanistic Motivation for Curriculum Ordering\n\nUnder flat exposure, the classifier simultaneously receives simple encodings (e.g., base64 with clean token boundaries) and complex nested encodings (e.g., ROT13-inside-base64 with homoglyph substitution). For complex encodings, the gradient signal in early training is effectively noise—the classifier has not yet developed the basic encoding-detection features needed to parse these inputs. These noisy gradients interfere with feature learning on simple encodings, creating catastrophic confusion.\n\nCurriculum ordering resolves this: Stage 1 (low-ECS) training builds robust token-level encoding-detection features—recognizing base64 character distributions, identifying ROT-shifted alphabetic patterns, detecting homoglyph Unicode ranges. These features are encoding-type-agnostic compositional primitives. Stage 2 (high-ECS) training then leverages these primitives to parse nested compositions, with gradient signal that is now informative rather than noisy.\n\nThis mechanism predicts generalization: if the classifier learns compositional encoding-detection primitives (rather than memorizing specific encoding types), it should recognize novel encodings that share structural properties with training encodings—e.g., Braille (character substitution like homoglyphs) or Morse (symbolic encoding like base64).\n\n### Why Not Learned Canonicalization?\n\nA natural alternative is training a seq2seq model to decode arbitrary encodings back to plaintext, then applying a standard guardrail classifier. We argue this pipeline approach is fundamentally limited:\n\n1. **Error propagation**: Canonicalization errors (even partial) directly cause classifier failure. For nested encodings with 3+ layers, each decoding step compounds errors.\n2. **Adversarial canonicalization game**: Against an adaptive attacker, the canonicalizer itself becomes the attack surface. The attacker can craft encodings that are decodable by humans but confuse the canonicalizer—this is merely shifting the adversarial robustness problem rather than solving it.\n3. **Partial encoding ambiguity**: Real attacks mix encoded and plaintext segments. Correctly identifying which portions to decode requires semantic understanding of the content—precisely the capability we need the end-to-end system to have.\n\nEnd-to-end encoding-robust classification sidesteps these issues by learning features that are directly invariant to encoding transformations.\n\n### Co-Evolutionary Training Loop\n\n**Attacker (Qwen2.5-1.5B, GRPO-trained):**\n- Generates encoding attack prompts with ECS constrained to current curriculum stage\n- Reward: +1 if generated encoding bypasses current classifier AND oracle confirms harmful content; -1 otherwise\n- Entropy regularization: penalizes collapse to single encoding type (maintains diversity within ECS band)\n\n**Classifier (Qwen2.5-4B, SFT):**\n- Trains on curriculum-ordered adversarial examples: Stage 1 (ECS ≤ threshold_1), then Stage 2 (ECS > threshold_1)\n- FPR rollback: if false positive rate on clean benign data exceeds 2%, revert to previous checkpoint\n- Semantic deduplication: removes near-duplicate training examples (cosine similarity > 0.95 on sentence embeddings)\n\n**Oracle:** GPT-4o judges whether decoded content is genuinely harmful. Deterministic decoder cross-validates; samples where oracle and deterministic decoder disagree are excluded.\n\n**Training Schedule:** 2 rounds of co-evolution. Each round: attacker generates within ECS band → oracle filters → classifier trains on filtered data. Round 1 = low-ECS band, Round 2 = high-ECS band.\n\n**Fallback Plan:** If co-evolutionary loop proves unstable, we fall back to static curriculum-ordered SFT: pre-generate curriculum-ordered training data using rule-based encoding generators (no GRPO attacker), train classifier on this static dataset. This still validates the core curriculum ordering hypothesis (H1, H2) while sacrificing the co-evolutionary contribution (H4).\n\n### Compute and Cost Estimation\n\n- **Hardware:** 4× A100 80GB GPUs\n- **Attacker training:** ~6 hours per round (1.5B model, GRPO on ~5K samples)\n- **Classifier training:** ~8 hours per round (4B model, SFT on ~10K samples)\n- **Total training wall-clock:** ~30 hours for 2 rounds (including data generation and filtering)\n- **Oracle API cost:** Estimated 15K-20K GPT-4o calls across 2 rounds ≈ $150-300\n- **Rate limit strategy:** Batch API with async calls, 500 requests/minute tier\n- **Compute normalization for baselines:** Training FLOPs (primary), supplemented by training tokens and wall-clock time reporting. All ablation variants use identical 4B classifier architecture, identical training steps, identical total data volume.\n\n## Experimental Design\n\n### Hypotheses\n\n- **H1 (Curriculum > Random):** Curriculum-ordered training achieves ≥10pp lower encoding-ASR than random-order training at equivalent FLOPs.\n- **H2 (Generalization):** Curriculum-trained classifier maintains ≤30% encoding-ASR on held-out encoding families (Braille, Morse, custom cipher) where random-order and flat augmentation exceed 60% ASR.\n- **H3 (ECS Predictiveness):** ECS correlates with classifier error rate (Spearman ρ ≥ 0.7) on held-out encodings, validating the metric as a principled difficulty measure.\n- **H4 (Co-evolution > Static):** Co-evolutionary training outperforms static curriculum SFT by ≥5pp on composite encodings (if co-evolutionary loop is successfully implemented).\n\n### Baselines and Ablations\n\n**Controlled comparisons (same architecture, same FLOPs):**\n1. **Random-order training:** Same data, same total steps, random presentation order. 5 random seeds, report mean ± std.\n2. **Flat augmentation:** All encoding types mixed uniformly in every batch (no ordering).\n3. **Reverse curriculum:** Stage 2 data first, then Stage 1 data (tests whether ordering direction matters vs. mere staging).\n4. **Static curriculum SFT:** Curriculum-ordered data without co-evolutionary attacker (isolates curriculum effect from co-evolution effect).\n\n**Indicative comparisons (different architectures, reported in Discussion):**\n5. **Broken-Token CPT-Filtering:** Rule-based approach; numbers from published results on comparable attack types.\n6. **TRYLOCK Layer 0:** Rule-based canonicalization; published numbers on overlapping benchmarks.\n\n### Evaluation Protocol\n\n**External benchmarks (primary evidence):**\n- HarmBench (encoding-perturbed variant): standard harmful prompts with encoding applied\n- JailbreakBench: encoding attack subset\n- WildGuardTest: encoding-perturbed variant\n\n**EncoAttack (supplementary deep analysis):**\n- 500 base prompts sourced from HarmBench (200) + AdvBench (150) + WildGuardTest (150), covering 10+ harm categories\n- 8 encoding types × 3 nesting levels = 24 conditions per prompt → 12,000 test cases\n- Encoding implementation: independent codebase from training pipeline, different random seeds for partial encoding positions\n- Validation: confirm attacks bypass undefended LlamaGuard-3 at ≥80% rate (ensuring attack validity)\n\n**Held-out encoding families (generalization test):**\n- Braille Unicode substitution\n- Morse code symbolic encoding\n- Custom Caesar-variant cipher (shift determined by position)\n- NATO phonetic alphabet encoding\n- These 4 encoding families are NEVER seen during training in any form\n\n**Metrics:**\n- Encoding-ASR (attack success rate): primary metric\n- Clean FPR (false positive rate on benign inputs): safety constraint (must stay ≤2%)\n- Per-encoding-type breakdown\n- ECS correlation analysis on held-out encodings\n\n### Learning Dynamics Analysis\n\n- Record classifier encoding-ASR at every 500 training steps\n- Plot per-encoding-type ASR curves showing curriculum-induced learning trajectory\n- Compare learning dynamics between curriculum vs. random-order (expecting earlier convergence on low-ECS encodings under curriculum)\n\n### Oracle Reliability Pilot\n\nBefore full training, conduct pilot on 100 samples per ECS band:\n- Measure GPT-4o decode accuracy and harmful/benign judgment agreement with deterministic decoder\n- If agreement rate < 80% for high-ECS band, adjust oracle strategy (e.g., use deterministic decoder only for Stage 2)\n\n## Stability Mechanisms (Engineering Choices)\n\nThe following mechanisms are borrowed from prior work (TriPlay-RL diversity penalty, standard RL stabilization) and are not claimed as contributions:\n- **Entropy regularization:** Prevents attacker collapse to single encoding type\n- **FPR rollback:** Prevents classifier from becoming overly aggressive\n- **Semantic deduplication:** Prevents training on near-duplicate examples\n\nWe report trigger frequencies for each mechanism as indirect evidence of utility. Full ablation of these components is planned for camera-ready.\n\n## Timeline (10-day plan)\n\n- Days 1-2: Implement ECS metric, encoding generators, data pipeline\n- Days 3-4: Train Stage 1 (low-ECS curriculum) + random-order baseline (seed 1-3)\n- Days 5-6: Train Stage 2 (high-ECS curriculum) + remaining baselines\n- Day 7: Full evaluation on all benchmarks + held-out encodings\n- Days 8-9: Analysis, ablations (reverse curriculum), writing\n- Day 10: Buffer / camera-ready extensions\n\n**If co-evolutionary loop fails by Day 4:** Switch to static curriculum SFT fallback, still completing H1-H3 validation."
}
```

---

### Runtime record

_source line 2 · 2026-05-16T12:19:26.464Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:19:26.464Z",
  "sessionId": "b0da184f-7f91-4b76-a7d1-8dca52f60a8b"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-16T12:19:26.479Z_

## Title

EncoGuard: Learning Encoding-Invariant Safety Features via Complexity-Structured Curriculum Training

## Problem Statement

Encoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, and their nested compositions) exploit a fundamental vulnerability in LLM safety guardrails: classifiers trained on plaintext or limited encoding variations fail catastrophically when inputs are transformed through encoding schemes not seen during training. The core challenge is not merely defending against known encodings, but achieving **generalization to unseen encoding families**—a property that no existing defense reliably provides.

## Core Thesis

We hypothesize that a classifier trained via **complexity-structured curriculum**—where encoding attacks are presented in order of a principled complexity metric—learns **encoding-invariant harmful-content features** that generalize to held-out encoding types unseen during training. This generalization arises because curriculum ordering enables the classifier to first build robust token-level encoding-detection primitives on simple encodings, which then serve as compositional building blocks for recognizing complex encodings. In contrast, flat augmentation and random-order training suffer from catastrophic confusion: noisy gradients from complex encodings in early training interfere with the formation of these foundational features.

This principle—that attack spaces with composable primitives and natural complexity ordering benefit from structured curriculum defense—is general beyond encoding attacks. We demonstrate it on the encoding domain as a canonical instance where complexity is formally quantifiable.

## Key Contributions

1. **Primary Contribution (Feature Learning Insight):** We demonstrate that complexity-structured curriculum training produces encoding-invariant representations that generalize to entirely unseen encoding families (Braille, Morse, custom ciphers), while flat augmentation and random-order training do not. This is evidence that curriculum ordering teaches compositional encoding-detection features rather than memorizing specific encoding patterns.

2. **Formalized Encoding Complexity Score (ECS):** We define a principled complexity metric combining nesting depth, character-per-token (CPT) ratio deviation, and tokenizer perplexity, which determines curriculum ordering. We show that ECS predicts classifier difficulty on held-out encodings, validating it as a transferable methodological contribution.

3. **Co-Evolutionary Training Framework:** We instantiate the curriculum principle via a GRPO-trained attacker that generates encoding attacks of escalating ECS, paired with an SFT classifier that trains on curriculum-ordered adversarial data. The co-evolutionary dynamic ensures the curriculum adapts to the classifier's current capability frontier.

4. **Comprehensive Evaluation:** We evaluate on both external benchmarks (HarmBench, JailbreakBench, WildGuardTest with encoding perturbations) and a purpose-built EncoAttack benchmark, with controlled ablations isolating the curriculum ordering effect.

## Methodology

### Encoding Complexity Score (ECS)

We define ECS for an encoding transformation $e$ as:

$$ECS(e) = \alpha \cdot \text{NestingDepth}(e) + \beta \cdot \text{CPT\_Deviation}(e) + \gamma \cdot \text{TokenizerPerplexity}(e)$$

where:
- NestingDepth: number of compositional encoding layers (1 for single, 2+ for nested)
- CPT_Deviation: absolute deviation of the encoded text's characters-per-token ratio from plaintext baseline
- TokenizerPerplexity: perplexity of the target model's tokenizer on the encoded text

Weights $\alpha, \beta, \gamma$ are set via pilot study measuring classifier error rate correlation. The curriculum presents attacks in monotonically increasing ECS order.

### Mechanistic Motivation for Curriculum Ordering

Under flat exposure, the classifier simultaneously receives simple encodings (e.g., base64 with clean token boundaries) and complex nested encodings (e.g., ROT13-inside-base64 with homoglyph substitution). For complex encodings, the gradient signal in early training is effectively noise—the classifier has not yet developed the basic encoding-detection features needed to parse these inputs. These noisy gradients interfere with feature learning on simple encodings, creating catastrophic confusion.

Curriculum ordering resolves this: Stage 1 (low-ECS) training builds robust token-level encoding-detection features—recognizing base64 character distributions, identifying ROT-shifted alphabetic patterns, detecting homoglyph Unicode ranges. These features are encoding-type-agnostic compositional primitives. Stage 2 (high-ECS) training then leverages these primitives to parse nested compositions, with gradient signal that is now informative rather than noisy.

This mechanism predicts generalization: if the classifier learns compositional encoding-detection primitives (rather than memorizing specific encoding types), it should recognize novel encodings that share structural properties with training encodings—e.g., Braille (character substitution like homoglyphs) or Morse (symbolic encoding like base64).

### Why Not Learned Canonicalization?

A natural alternative is training a seq2seq model to decode arbitrary encodings back to plaintext, then applying a standard guardrail classifier. We argue this pipeline approach is fundamentally limited:

1. **Error propagation**: Canonicalization errors (even partial) directly cause classifier failure. For nested encodings with 3+ layers, each decoding step compounds errors.
2. **Adversarial canonicalization game**: Against an adaptive attacker, the canonicalizer itself becomes the attack surface. The attacker can craft encodings that are decodable by humans but confuse the canonicalizer—this is merely shifting the adversarial robustness problem rather than solving it.
3. **Partial encoding ambiguity**: Real attacks mix encoded and plaintext segments. Correctly identifying which portions to decode requires semantic understanding of the content—precisely the capability we need the end-to-end system to have.

End-to-end encoding-robust classification sidesteps these issues by learning features that are directly invariant to encoding transformations.

### Co-Evolutionary Training Loop

**Attacker (Qwen2.5-1.5B, GRPO-trained):**
- Generates encoding attack prompts with ECS constrained to current curriculum stage
- Reward: +1 if generated encoding bypasses current classifier AND oracle confirms harmful content; -1 otherwise
- Entropy regularization: penalizes collapse to single encoding type (maintains diversity within ECS band)

**Classifier (Qwen2.5-4B, SFT):**
- Trains on curriculum-ordered adversarial examples: Stage 1 (ECS ≤ threshold_1), then Stage 2 (ECS > threshold_1)
- FPR rollback: if false positive rate on clean benign data exceeds 2%, revert to previous checkpoint
- Semantic deduplication: removes near-duplicate training examples (cosine similarity > 0.95 on sentence embeddings)

**Oracle:** GPT-4o judges whether decoded content is genuinely harmful. Deterministic decoder cross-validates; samples where oracle and deterministic decoder disagree are excluded.

**Training Schedule:** 2 rounds of co-evolution. Each round: attacker generates within ECS band → oracle filters → classifier trains on filtered data. Round 1 = low-ECS band, Round 2 = high-ECS band.

**Fallback Plan:** If co-evolutionary loop proves unstable, we fall back to static curriculum-ordered SFT: pre-generate curriculum-ordered training data using rule-based encoding generators (no GRPO attacker), train classifier on this static dataset. This still validates the core curriculum ordering hypothesis (H1, H2) while sacrificing the co-evolutionary contribution (H4).

### Compute and Cost Estimation

- **Hardware:** 4× A100 80GB GPUs
- **Attacker training:** ~6 hours per round (1.5B model, GRPO on ~5K samples)
- **Classifier training:** ~8 hours per round (4B model, SFT on ~10K samples)
- **Total training wall-clock:** ~30 hours for 2 rounds (including data generation and filtering)
- **Oracle API cost:** Estimated 15K-20K GPT-4o calls across 2 rounds ≈ $150-300
- **Rate limit strategy:** Batch API with async calls, 500 requests/minute tier
- **Compute normalization for baselines:** Training FLOPs (primary), supplemented by training tokens and wall-clock time reporting. All ablation variants use identical 4B classifier architecture, identical training steps, identical total data volume.

## Experimental Design

### Hypotheses

- **H1 (Curriculum > Random):** Curriculum-ordered training achieves ≥10pp lower encoding-ASR than random-order training at equivalent FLOPs.
- **H2 (Generalization):** Curriculum-trained classifier maintains ≤30% encoding-ASR on held-out encoding families (Braille, Morse, custom cipher) where random-order and flat augmentation exceed 60% ASR.
- **H3 (ECS Predictiveness):** ECS correlates with classifier error rate (Spearman ρ ≥ 0.7) on held-out encodings, validating the metric as a principled difficulty measure.
- **H4 (Co-evolution > Static):** Co-evolutionary training outperforms static curriculum SFT by ≥5pp on composite encodings (if co-evolutionary loop is successfully implemented).

### Baselines and Ablations

**Controlled comparisons (same architecture, same FLOPs):**
1. **Random-order training:** Same data, same total steps, random presentation order. 5 random seeds, report mean ± std.
2. **Flat augmentation:** All encoding types mixed uniformly in every batch (no ordering).
3. **Reverse curriculum:** Stage 2 data first, then Stage 1 data (tests whether ordering direction matters vs. mere staging).
4. **Static curriculum SFT:** Curriculum-ordered data without co-evolutionary attacker (isolates curriculum effect from co-evolution effect).

**Indicative comparisons (different architectures, reported in Discussion):**
5. **Broken-Token CPT-Filtering:** Rule-based approach; numbers from published results on comparable attack types.
6. **TRYLOCK Layer 0:** Rule-based canonicalization; published numbers on overlapping benchmarks.

### Evaluation Protocol

**External benchmarks (primary evidence):**
- HarmBench (encoding-perturbed variant): standard harmful prompts with encoding applied
- JailbreakBench: encoding attack subset
- WildGuardTest: encoding-perturbed variant

**EncoAttack (supplementary deep analysis):**
- 500 base prompts sourced from HarmBench (200) + AdvBench (150) + WildGuardTest (150), covering 10+ harm categories
- 8 encoding types × 3 nesting levels = 24 conditions per prompt → 12,000 test cases
- Encoding implementation: independent codebase from training pipeline, different random seeds for partial encoding positions
- Validation: confirm attacks bypass undefended LlamaGuard-3 at ≥80% rate (ensuring attack validity)

**Held-out encoding families (generalization test):**
- Braille Unicode substitution
- Morse code symbolic encoding
- Custom Caesar-variant cipher (shift determined by position)
- NATO phonetic alphabet encoding
- These 4 encoding families are NEVER seen during training in any form

**Metrics:**
- Encoding-ASR (attack success rate): primary metric
- Clean FPR (false positive rate on benign inputs): safety constraint (must stay ≤2%)
- Per-encoding-type breakdown
- ECS correlation analysis on held-out encodings

### Learning Dynamics Analysis

- Record classifier encoding-ASR at every 500 training steps
- Plot per-encoding-type ASR curves showing curriculum-induced learning trajectory
- Compare learning dynamics between curriculum vs. random-order (expecting earlier convergence on low-ECS encodings under curriculum)

### Oracle Reliability Pilot

Before full training, conduct pilot on 100 samples per ECS band:
- Measure GPT-4o decode accuracy and harmful/benign judgment agreement with deterministic decoder
- If agreement rate < 80% for high-ECS band, adjust oracle strategy (e.g., use deterministic decoder only for Stage 2)

## Stability Mechanisms (Engineering Choices)

The following mechanisms are borrowed from prior work (TriPlay-RL diversity penalty, standard RL stabilization) and are not claimed as contributions:
- **Entropy regularization:** Prevents attacker collapse to single encoding type
- **FPR rollback:** Prevents classifier from becoming overly aggressive
- **Semantic deduplication:** Prevents training on near-duplicate examples

We report trigger frequencies for each mechanism as indirect evidence of utility. Full ablation of these components is planned for camera-ready.

## Timeline (10-day plan)

- Days 1-2: Implement ECS metric, encoding generators, data pipeline
- Days 3-4: Train Stage 1 (low-ECS curriculum) + random-order baseline (seed 1-3)
- Days 5-6: Train Stage 2 (high-ECS curriculum) + remaining baselines
- Day 7: Full evaluation on all benchmarks + held-out encodings
- Days 8-9: Analysis, ablations (reverse curriculum), writing
- Day 10: Buffer / camera-ready extensions

**If co-evolutionary loop fails by Day 4:** Switch to static curriculum SFT fallback, still completing H1-H3 validation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "2220114a-1b8f-40f4-867c-837b84ad3ba1",
  "type": "user",
  "uuid": "0f77b24a-da15-4434-85df-4d21dbb4b4ea",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0da184f-7f91-4b76-a7d1-8dca52f60a8b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T12:19:26.477Z_

```json
{
  "parentUuid": "0f77b24a-da15-4434-85df-4d21dbb4b4ea",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "ffb2a30f-7532-4a95-91b7-8824b6f91418",
  "timestamp": "2026-05-16T12:19:26.477Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0da184f-7f91-4b76-a7d1-8dca52f60a8b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T12:19:26.477Z_

```json
{
  "parentUuid": "ffb2a30f-7532-4a95-91b7-8824b6f91418",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "78d44672-c991-44ad-99bd-c7cd213c7e1e",
  "timestamp": "2026-05-16T12:19:26.477Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0da184f-7f91-4b76-a7d1-8dca52f60a8b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "EncoGuard: Encoding-invariant safety via curriculum training",
  "sessionId": "b0da184f-7f91-4b76-a7d1-8dca52f60a8b"
}
```

---

### Assistant

_source line 7 · 2026-05-16T12:20:12.721Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal as the "发掘 agent" (Discovery Agent), focusing on the three dimensions I'm responsible for: Novelty, Significance, and Related Work differentiation.

Let me first think through the two critical questions:

**1. Is there a trivial alternative that achieves similar effects?**

The proposal does address the "learned canonicalization" alternative, arguing it has error propagation issues. But there are other trivial alternatives to consider:

- Simply training on more diverse encodings (data augmentation) without curriculum ordering. The proposal claims this doesn't work (flat augmentation baseline), but the claim that curriculum ordering specifically provides generalization is the key novelty. 

The real question is whether curriculum learning actually produces fundamentally different feature representations, or if it's just optimizing the training process slightly better.

- Another trivial alternative: input preprocessing/normalization. Many encoding schemes have detectable signatures (base64 character distributions, Unicode ranges for homoglyphs). A simple rule-based detector + decoder pipeline might handle this without any ML. The proposal partially addresses this with the canonicalization argument but doesn't fully engage with why simple detection heuristics + known decoders wouldn't work.

- What about simply increasing model size or pretraining data diversity? If a larger model has seen more encoding patterns during pretraining, it might already have encoding-invariant features.

**2. Is the core claim's premise valid?**

The core claim is: "curriculum ordering enables the classifier to first build robust token-level encoding-detection primitives on simple encodings, then progressively handle more complex cases." I need to examine whether this premise actually holds or if the improvements come from something else entirely.

The mechanistic hypothesis assumes that simple encodings teach composable primitives that transfer to unseen encodings. But here's the problem: if the model learns base64 and ROT13 detection features, why would those help with Braille or Morse code? Those are fundamentally different encoding mechanisms. The compositionality argument works for nested versions of known encodings, but generalizing to entirely new encoding families requires learning something more abstract—like detecting unusual character distributions as a signal that text might be encoded, then looking for harmful patterns regardless of the specific encoding scheme. This suggests the generalization claim might be overstated; the curriculum could help with compositions of known encodings, but truly novel encoding families represent a much stronger generalization challenge.

Now I'm assessing the novelty across three dimensions. The core claim is that curriculum ordering by complexity produces encoding-invariant features that generalize to unseen encodings. Curriculum learning itself is well-established, as is adversarial training with co-evolution and encoding-specific defenses like SmoothLLM. The combination is novel, but it's not clear if it's a fundamental insight or just a surface-level integration of existing techniques. The ECS metric adds some novelty—combining three measures with learned weights—but it's fairly straightforward. The strongest novelty angle is actually the feature learning insight: if curriculum ordering genuinely produces qualitatively different internal representations compared to standard training, that would be the real contribution.

For significance, encoding-based jailbreaks are a real problem, but they're just one category in a broader jailbreak landscape. Many systems already use multiple defense layers, and if LLMs improve at understanding encodings through better pretraining, the problem might naturally diminish. The principle about structured curriculum defense for composable attack spaces could be significant if it generalizes beyond this one domain, but the paper only demonstrates it on encoding attacks.

I'm now looking at how this work differentiates from related approaches like GradientCuff and SmoothLLM, which are recent defenses against jailbreaks.  The proposal mentions Broken-Token and TRYLOCK as comparisons but treats them somewhat superficially—there's likely more recent work on encoding-robust classification that deserves deeper engagement. I'm also considering how this differs from standard curriculum learning applied to robustness, adversarial training approaches like TRADES and PGD-based methods, and RL-based red-teaming work.

The key tension I'm seeing is that the generalization claim—that the approach works on entirely unseen encoding families—needs a clearer mechanistic explanation. The compositional primitives argument doesn't fully explain why features learned on one encoding family would transfer to completely novel ones.

There's also a broader principle here that feels undersold: the idea that attack spaces with composable primitives and natural complexity ordering benefit from structured curriculum defense could apply far beyond encoding attacks to prompt injection or multi-step social engineering. The paper should either lean into this wider framing or be more precise about its scope. And actually, the most transferable contribution might be ECS as a difficulty predictor—if it correlates with classifier error, that's a genuinely useful signal that could generalize across different attack types.

The "encoding-invariant features" claim needs more precision too. Rather than treating it as a hypothesis, I should commit to mechanistic analysis—showing via probing or representational similarity that the model learns a common representation for harmful content across different encodings, not just that it has better encoding coverage. That would be a much stronger scientific claim.

The proposal itself is well-structured with clear hypotheses and fallback plans, but there are some conceptual gaps worth tightening. The jump from "curriculum helps with compositions of known encodings" to "curriculum helps with entirely novel encoding families" is the core novelty claim, yet it's not rigorously argued. The broader applicability claim is mentioned but underdeveloped, and I haven't engaged with what curriculum learning theory actually predicts about when and why curriculum should help. There's real discovery space here if I sharpen these points.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78d44672-c991-44ad-99bd-c7cd213c7e1e",
  "isSidechain": false,
  "requestId": "req_011Cb6EeDcLK4o8g64ZydFL8",
  "type": "assistant",
  "uuid": "25e9cffd-831b-4b8b-a2df-9ae1ff7af5ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0da184f-7f91-4b76-a7d1-8dca52f60a8b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6FFT67nhihT1M1xN4N7Da",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4508,
      "cache_read_input_tokens": 13247,
      "output_tokens": 3838,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4508,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3838,
          "cache_read_input_tokens": 13247,
          "cache_creation_input_tokens": 4508,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4508
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

### Assistant

_source line 8 · 2026-05-16T12:21:03.864Z_

【状态】: 有发掘空间

---

【发掘点 1】
- 维度: 前提假设质疑 / 核心 claim 强化
- 内容: 当前 proposal 的逻辑链存在一个未弥合的跳跃：mechanistic explanation 声称 curriculum 帮助模型学习"compositional encoding-detection primitives"（如识别 base64 字符分布、ROT-shifted 模式、homoglyph Unicode ranges），但随后声称这些 primitives 能泛化到 **结构上完全不同的编码家族**（Braille、Morse）。问题是：检测 base64 字符分布的 feature 为什么会帮助识别 Braille Unicode substitution？它们共享的不是"编码检测原语"，而是一个更高阶的 meta-capability——"在 surface form 异常时仍然提取 semantic harmful content"。如果真正的泛化机制是学到了 **content-invariance under surface perturbation**（类似 vision 中的 texture vs. shape bias），而非 compositional encoding detection，那核心 claim 应该重新表述为："curriculum ordering 迫使模型先在低噪声环境下锚定 harmful content 的 semantic signature，再学会在高噪声环境下 preserve 这个 signature"——这个 framing 比"compositional primitives"更精确、更 testable、也更 novel。
- 价值: 如果机制描述与泛化 claim 之间有逻辑裂缝，审稿人会精准攻击这个点："你们说学的是 encoding-detection primitives，但 Braille 和 base64 没有共享的 detection primitive，所以泛化结果要么说明你们的机制假设是错的，要么说明泛化是巧合。" 修正这个 framing 能让核心 claim 的逻辑链条闭合，同时让 novelty 更锐利——从"curriculum helps learn compositional features"（curriculum learning 文献里相对 familiar 的 claim）升级为"curriculum ordering induces content-level invariance that separates semantic features from surface encoding features"（一个关于 representation disentanglement 的更深刻 claim）。命中 **Novelty** 和 **Significance** 两个维度。

【发掘点 2】
- 维度: significance 提升
- 内容: 当前 proposal 的 broader principle——"attack spaces with composable primitives and natural complexity ordering benefit from structured curriculum defense"——被声明了但没有被 operationalize。这个 principle 如果成立，意味着同样的方法论可以迁移到 **multi-step prompt injection**（简单指令注入 → 嵌套上下文操控）、**multi-turn social engineering**（单轮诱导 → 多轮渐进式）、**code injection attacks**（直接恶意代码 → 混淆/打包/多层编码的恶意代码）。但目前 paper 只在 encoding domain 做一个 instance，读起来像"一个 encoding defense 方法恰好用了 curriculum"，而非"一个通用 principle 在 encoding domain 的 canonical demonstration"。建议在 framing 层面做 pivot：核心贡献不是"一个更好的 encoding defense"，而是"structured complexity curriculum 作为 compositional attack space 的通用防御原理，以 encoding attacks 作为形式化最清晰的验证场"。
- 价值: 如果只 pitch 为 encoding defense，significance 被限定在"encoding jailbreak"这个子问题里——审稿人可能觉得这个问题窄、会被更好的 tokenizer 或更大的预训练数据自然解决。但如果 pitch 为通用 principle + canonical demonstration，significance 立刻上升一个量级：这为整个 adversarial robustness 社区提供了一个新的 defense paradigm。同时，evaluation 中可以加一小段 discussion："如果该 principle 成立，以下攻击类型应该也适用..."作为 future work teaser，但不需要实验证明。命中 **Significance**。

【发掘点 3】
- 维度: trivial alternative 威胁
- 内容: Proposal 讨论了 "learned canonicalization" 这个替代方案并给出了合理的反驳。但忽略了一个更 trivial 的替代：**simple rule-based encoding detection + known decoder + standard guardrail**。大多数编码（base64、ROT13、Morse、Braille）都有极其明显的统计 signature（字符集限制、固定 pattern）。一个 regex/heuristic 检测器 + 已知解码器的 pipeline，对于单层编码和大多数双层嵌套，可能达到 90%+ 的检测率——成本几乎为零。论文需要明确论证：(1) 这个 trivial pipeline 在什么条件下失败（partial encoding? adversarial mixing of encoded and plaintext?），(2) 对于这些失败 cases，curriculum-trained classifier 的优势具体体现在哪。如果不正面回应这个 alternative，审稿人会问："为什么不直接用 regex 检测 + decode + LlamaGuard？"
- 价值: 这不是要否定 idea，而是要求在 introduction/motivation 中 explicitly 建立 problem boundary：rule-based 方法在 X 条件下有效但在 Y 条件下失败（Y = partial encoding、adversarial mixing、novel encodings with no known decoder），本工作正是解决 Y 的。这让 novelty claim 的 scope 更精确，也让 evaluation 的 focus 更有说服力。如果不处理这个点，整个 paper 的 motivation 会被"为什么不用简单方法"这一个问题击穿。命中 **Novelty**（通过明确 incremental value 的边界）。

【发掘点 4】
- 维度: related work 差异化
- 内容: Curriculum learning 用于 adversarial robustness 不是新概念。Specifically：(1) **Cai et al., "Curriculum Adversarial Training" (IJCAI 2018)**——按 adversarial perturbation 强度递增训练 image classifiers；(2) **Wang et al., "Ordered SGD" (NeurIPS 2021)**——按 sample difficulty 排序训练以提高 generalization。当前 proposal 需要明确与这些 prior arts 的差异化：不只是"curriculum + adversarial training"的简单组合，而是 (a) 在离散 compositional attack space（而非连续 perturbation space）中定义 complexity metric，(b) 验证 curriculum 在 **out-of-distribution attack types** 上的泛化（prior work 只测 in-distribution robustness），(c) ECS 作为 domain-specific complexity formalization 的贡献。如果不 explicitly engage with curriculum adversarial training 的 prior art，审稿人一定会问："这和 curriculum adversarial training 比有什么本质区别？"
- 价值: 这是 related work 差异化的硬伤。如果审稿人认为这只是"curriculum adversarial training applied to NLP encoding domain"，novelty 评分会大幅下降。需要 clearly articulate 本工作的 unique insight：curriculum 在 **compositional discrete attack space** 中能诱导 **OOD generalization**——这是 prior curriculum adversarial training work 从未验证过的 claim，也是本文最强的 novelty angle。命中 **Related Work 差异化** 和 **Novelty**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25e9cffd-831b-4b8b-a2df-9ae1ff7af5ba",
  "isSidechain": false,
  "requestId": "req_011Cb6EeDcLK4o8g64ZydFL8",
  "type": "assistant",
  "uuid": "b75e2464-5130-4ec6-84e6-102693955e15",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0da184f-7f91-4b76-a7d1-8dca52f60a8b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6FFT67nhihT1M1xN4N7Da",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4508,
      "cache_read_input_tokens": 13247,
      "output_tokens": 3838,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4508,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3838,
          "cache_read_input_tokens": 13247,
          "cache_creation_input_tokens": 4508,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4508
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

### Runtime record

_source line 9_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## Title  EncoGuard: Learning Encoding-Invariant Safety Features via Complexity-Structured Curriculum Training  ## Problem Statement  Encoding-based jailbreak attacks (base64, ROT13, homoglyph substit…",
  "leafUuid": "b75e2464-5130-4ec6-84e6-102693955e15",
  "sessionId": "b0da184f-7f91-4b76-a7d1-8dca52f60a8b"
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "EncoGuard: Encoding-invariant safety via curriculum training",
  "sessionId": "b0da184f-7f91-4b76-a7d1-8dca52f60a8b"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## Title  EncoGuard: Learning Encoding-Invariant Safety Features via Complexity-Structured Curriculum Training  ## Problem Statement  Encoding-based jailbreak attacks (base64, ROT13, homoglyph substit…",
  "leafUuid": "b75e2464-5130-4ec6-84e6-102693955e15",
  "sessionId": "b0da184f-7f91-4b76-a7d1-8dca52f60a8b"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "EncoGuard: Encoding-invariant safety via curriculum training",
  "sessionId": "b0da184f-7f91-4b76-a7d1-8dca52f60a8b"
}
```

---
