# Research conversation: Title EncoGuard: Learning Encoding-Invariant Safety Features via Complexity-Structured Curriculum Training ## Problem St

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/a7d6b8f5-4057-4d41-b2ff-8e10e79ef9d7.jsonl`
- **Structured JSON:** [`bf7f817c538c14855dd9.json`](../../sessions/bf/bf7f817c538c14855dd9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T12:19:26.391Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:19:26.391Z",
  "sessionId": "a7d6b8f5-4057-4d41-b2ff-8e10e79ef9d7",
  "content": "## Title\n\nEncoGuard: Learning Encoding-Invariant Safety Features via Complexity-Structured Curriculum Training\n\n## Problem Statement\n\nEncoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, and their nested compositions) exploit a fundamental vulnerability in LLM safety guardrails: classifiers trained on plaintext or limited encoding variations fail catastrophically when inputs are transformed through encoding schemes not seen during training. The core challenge is not merely defending against known encodings, but achieving **generalization to unseen encoding families**—a property that no existing defense reliably provides.\n\n## Core Thesis\n\nWe hypothesize that a classifier trained via **complexity-structured curriculum**—where encoding attacks are presented in order of a principled complexity metric—learns **encoding-invariant harmful-content features** that generalize to held-out encoding types unseen during training. This generalization arises because curriculum ordering enables the classifier to first build robust token-level encoding-detection primitives on simple encodings, which then serve as compositional building blocks for recognizing complex encodings. In contrast, flat augmentation and random-order training suffer from catastrophic confusion: noisy gradients from complex encodings in early training interfere with the formation of these foundational features.\n\nThis principle—that attack spaces with composable primitives and natural complexity ordering benefit from structured curriculum defense—is general beyond encoding attacks. We demonstrate it on the encoding domain as a canonical instance where complexity is formally quantifiable.\n\n## Key Contributions\n\n1. **Primary Contribution (Feature Learning Insight):** We demonstrate that complexity-structured curriculum training produces encoding-invariant representations that generalize to entirely unseen encoding families (Braille, Morse, custom ciphers), while flat augmentation and random-order training do not. This is evidence that curriculum ordering teaches compositional encoding-detection features rather than memorizing specific encoding patterns.\n\n2. **Formalized Encoding Complexity Score (ECS):** We define a principled complexity metric combining nesting depth, character-per-token (CPT) ratio deviation, and tokenizer perplexity, which determines curriculum ordering. We show that ECS predicts classifier difficulty on held-out encodings, validating it as a transferable methodological contribution.\n\n3. **Co-Evolutionary Training Framework:** We instantiate the curriculum principle via a GRPO-trained attacker that generates encoding attacks of escalating ECS, paired with an SFT classifier that trains on curriculum-ordered adversarial data. The co-evolutionary dynamic ensures the curriculum adapts to the classifier's current capability frontier.\n\n4. **Comprehensive Evaluation:** We evaluate on both external benchmarks (HarmBench, JailbreakBench, WildGuardTest with encoding perturbations) and a purpose-built EncoAttack benchmark, with controlled ablations isolating the curriculum ordering effect.\n\n## Methodology\n\n### Encoding Complexity Score (ECS)\n\nWe define ECS for an encoding transformation $e$ as:\n\n$$ECS(e) = \\alpha \\cdot \\text{NestingDepth}(e) + \\beta \\cdot \\text{CPT\\_Deviation}(e) + \\gamma \\cdot \\text{TokenizerPerplexity}(e)$$\n\nwhere:\n- NestingDepth: number of compositional encoding layers (1 for single, 2+ for nested)\n- CPT_Deviation: absolute deviation of the encoded text's characters-per-token ratio from plaintext baseline\n- TokenizerPerplexity: perplexity of the target model's tokenizer on the encoded text\n\nWeights $\\alpha, \\beta, \\gamma$ are set via pilot study measuring classifier error rate correlation. The curriculum presents attacks in monotonically increasing ECS order.\n\n### Mechanistic Motivation for Curriculum Ordering\n\nUnder flat exposure, the classifier simultaneously receives simple encodings (e.g., base64 with clean token boundaries) and complex nested encodings (e.g., ROT13-inside-base64 with homoglyph substitution). For complex encodings, the gradient signal in early training is effectively noise—the classifier has not yet developed the basic encoding-detection features needed to parse these inputs. These noisy gradients interfere with feature learning on simple encodings, creating catastrophic confusion.\n\nCurriculum ordering resolves this: Stage 1 (low-ECS) training builds robust token-level encoding-detection features—recognizing base64 character distributions, identifying ROT-shifted alphabetic patterns, detecting homoglyph Unicode ranges. These features are encoding-type-agnostic compositional primitives. Stage 2 (high-ECS) training then leverages these primitives to parse nested compositions, with gradient signal that is now informative rather than noisy.\n\nThis mechanism predicts generalization: if the classifier learns compositional encoding-detection primitives (rather than memorizing specific encoding types), it should recognize novel encodings that share structural properties with training encodings—e.g., Braille (character substitution like homoglyphs) or Morse (symbolic encoding like base64).\n\n### Why Not Learned Canonicalization?\n\nA natural alternative is training a seq2seq model to decode arbitrary encodings back to plaintext, then applying a standard guardrail classifier. We argue this pipeline approach is fundamentally limited:\n\n1. **Error propagation**: Canonicalization errors (even partial) directly cause classifier failure. For nested encodings with 3+ layers, each decoding step compounds errors.\n2. **Adversarial canonicalization game**: Against an adaptive attacker, the canonicalizer itself becomes the attack surface. The attacker can craft encodings that are decodable by humans but confuse the canonicalizer—this is merely shifting the adversarial robustness problem rather than solving it.\n3. **Partial encoding ambiguity**: Real attacks mix encoded and plaintext segments. Correctly identifying which portions to decode requires semantic understanding of the content—precisely the capability we need the end-to-end system to have.\n\nEnd-to-end encoding-robust classification sidesteps these issues by learning features that are directly invariant to encoding transformations.\n\n### Co-Evolutionary Training Loop\n\n**Attacker (Qwen2.5-1.5B, GRPO-trained):**\n- Generates encoding attack prompts with ECS constrained to current curriculum stage\n- Reward: +1 if generated encoding bypasses current classifier AND oracle confirms harmful content; -1 otherwise\n- Entropy regularization: penalizes collapse to single encoding type (maintains diversity within ECS band)\n\n**Classifier (Qwen2.5-4B, SFT):**\n- Trains on curriculum-ordered adversarial examples: Stage 1 (ECS ≤ threshold_1), then Stage 2 (ECS > threshold_1)\n- FPR rollback: if false positive rate on clean benign data exceeds 2%, revert to previous checkpoint\n- Semantic deduplication: removes near-duplicate training examples (cosine similarity > 0.95 on sentence embeddings)\n\n**Oracle:** GPT-4o judges whether decoded content is genuinely harmful. Deterministic decoder cross-validates; samples where oracle and deterministic decoder disagree are excluded.\n\n**Training Schedule:** 2 rounds of co-evolution. Each round: attacker generates within ECS band → oracle filters → classifier trains on filtered data. Round 1 = low-ECS band, Round 2 = high-ECS band.\n\n**Fallback Plan:** If co-evolutionary loop proves unstable, we fall back to static curriculum-ordered SFT: pre-generate curriculum-ordered training data using rule-based encoding generators (no GRPO attacker), train classifier on this static dataset. This still validates the core curriculum ordering hypothesis (H1, H2) while sacrificing the co-evolutionary contribution (H4).\n\n### Compute and Cost Estimation\n\n- **Hardware:** 4× A100 80GB GPUs\n- **Attacker training:** ~6 hours per round (1.5B model, GRPO on ~5K samples)\n- **Classifier training:** ~8 hours per round (4B model, SFT on ~10K samples)\n- **Total training wall-clock:** ~30 hours for 2 rounds (including data generation and filtering)\n- **Oracle API cost:** Estimated 15K-20K GPT-4o calls across 2 rounds ≈ $150-300\n- **Rate limit strategy:** Batch API with async calls, 500 requests/minute tier\n- **Compute normalization for baselines:** Training FLOPs (primary), supplemented by training tokens and wall-clock time reporting. All ablation variants use identical 4B classifier architecture, identical training steps, identical total data volume.\n\n## Experimental Design\n\n### Hypotheses\n\n- **H1 (Curriculum > Random):** Curriculum-ordered training achieves ≥10pp lower encoding-ASR than random-order training at equivalent FLOPs.\n- **H2 (Generalization):** Curriculum-trained classifier maintains ≤30% encoding-ASR on held-out encoding families (Braille, Morse, custom cipher) where random-order and flat augmentation exceed 60% ASR.\n- **H3 (ECS Predictiveness):** ECS correlates with classifier error rate (Spearman ρ ≥ 0.7) on held-out encodings, validating the metric as a principled difficulty measure.\n- **H4 (Co-evolution > Static):** Co-evolutionary training outperforms static curriculum SFT by ≥5pp on composite encodings (if co-evolutionary loop is successfully implemented).\n\n### Baselines and Ablations\n\n**Controlled comparisons (same architecture, same FLOPs):**\n1. **Random-order training:** Same data, same total steps, random presentation order. 5 random seeds, report mean ± std.\n2. **Flat augmentation:** All encoding types mixed uniformly in every batch (no ordering).\n3. **Reverse curriculum:** Stage 2 data first, then Stage 1 data (tests whether ordering direction matters vs. mere staging).\n4. **Static curriculum SFT:** Curriculum-ordered data without co-evolutionary attacker (isolates curriculum effect from co-evolution effect).\n\n**Indicative comparisons (different architectures, reported in Discussion):**\n5. **Broken-Token CPT-Filtering:** Rule-based approach; numbers from published results on comparable attack types.\n6. **TRYLOCK Layer 0:** Rule-based canonicalization; published numbers on overlapping benchmarks.\n\n### Evaluation Protocol\n\n**External benchmarks (primary evidence):**\n- HarmBench (encoding-perturbed variant): standard harmful prompts with encoding applied\n- JailbreakBench: encoding attack subset\n- WildGuardTest: encoding-perturbed variant\n\n**EncoAttack (supplementary deep analysis):**\n- 500 base prompts sourced from HarmBench (200) + AdvBench (150) + WildGuardTest (150), covering 10+ harm categories\n- 8 encoding types × 3 nesting levels = 24 conditions per prompt → 12,000 test cases\n- Encoding implementation: independent codebase from training pipeline, different random seeds for partial encoding positions\n- Validation: confirm attacks bypass undefended LlamaGuard-3 at ≥80% rate (ensuring attack validity)\n\n**Held-out encoding families (generalization test):**\n- Braille Unicode substitution\n- Morse code symbolic encoding\n- Custom Caesar-variant cipher (shift determined by position)\n- NATO phonetic alphabet encoding\n- These 4 encoding families are NEVER seen during training in any form\n\n**Metrics:**\n- Encoding-ASR (attack success rate): primary metric\n- Clean FPR (false positive rate on benign inputs): safety constraint (must stay ≤2%)\n- Per-encoding-type breakdown\n- ECS correlation analysis on held-out encodings\n\n### Learning Dynamics Analysis\n\n- Record classifier encoding-ASR at every 500 training steps\n- Plot per-encoding-type ASR curves showing curriculum-induced learning trajectory\n- Compare learning dynamics between curriculum vs. random-order (expecting earlier convergence on low-ECS encodings under curriculum)\n\n### Oracle Reliability Pilot\n\nBefore full training, conduct pilot on 100 samples per ECS band:\n- Measure GPT-4o decode accuracy and harmful/benign judgment agreement with deterministic decoder\n- If agreement rate < 80% for high-ECS band, adjust oracle strategy (e.g., use deterministic decoder only for Stage 2)\n\n## Stability Mechanisms (Engineering Choices)\n\nThe following mechanisms are borrowed from prior work (TriPlay-RL diversity penalty, standard RL stabilization) and are not claimed as contributions:\n- **Entropy regularization:** Prevents attacker collapse to single encoding type\n- **FPR rollback:** Prevents classifier from becoming overly aggressive\n- **Semantic deduplication:** Prevents training on near-duplicate examples\n\nWe report trigger frequencies for each mechanism as indirect evidence of utility. Full ablation of these components is planned for camera-ready.\n\n## Timeline (10-day plan)\n\n- Days 1-2: Implement ECS metric, encoding generators, data pipeline\n- Days 3-4: Train Stage 1 (low-ECS curriculum) + random-order baseline (seed 1-3)\n- Days 5-6: Train Stage 2 (high-ECS curriculum) + remaining baselines\n- Day 7: Full evaluation on all benchmarks + held-out encodings\n- Days 8-9: Analysis, ablations (reverse curriculum), writing\n- Day 10: Buffer / camera-ready extensions\n\n**If co-evolutionary loop fails by Day 4:** Switch to static curriculum SFT fallback, still completing H1-H3 validation."
}
```

---

### Runtime record

_source line 2 · 2026-05-16T12:19:26.402Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:19:26.402Z",
  "sessionId": "a7d6b8f5-4057-4d41-b2ff-8e10e79ef9d7"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-16T12:19:26.429Z_

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
  "promptId": "f375e472-8bd8-4ea9-86ab-b6625ce54016",
  "type": "user",
  "uuid": "40cba54c-b179-4920-9e8f-59b248e88367",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a7d6b8f5-4057-4d41-b2ff-8e10e79ef9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T12:19:26.427Z_

```json
{
  "parentUuid": "40cba54c-b179-4920-9e8f-59b248e88367",
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
  "uuid": "2c279eb9-612e-4609-adef-5c67cd4352bd",
  "timestamp": "2026-05-16T12:19:26.427Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a7d6b8f5-4057-4d41-b2ff-8e10e79ef9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T12:19:26.427Z_

```json
{
  "parentUuid": "2c279eb9-612e-4609-adef-5c67cd4352bd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f5cce8e1-4e92-4a24-8c7e-8da7e69e4360",
  "timestamp": "2026-05-16T12:19:26.427Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a7d6b8f5-4057-4d41-b2ff-8e10e79ef9d7",
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
  "aiTitle": "EncoGuard: curriculum-based encoding-robust safety training",
  "sessionId": "a7d6b8f5-4057-4d41-b2ff-8e10e79ef9d7"
}
```

---

### Assistant

_source line 7 · 2026-05-16T12:20:08.802Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal from the perspective of experimental design and technical execution completeness. I need to evaluate:

1. Baseline coverage
2. Experimental design rigor
3. Evaluation metrics and protocol
4. Ablation design
5. Feasibility (compute, data, time, etc.)

Let me go through this systematically.

**Baselines:**
- Random-order training (same data, same FLOPs) - good controlled comparison
- Flat augmentation - good
- Reverse curriculum - clever, tests directionality


- Static curriculum SFT - isolates curriculum from co-evolution
- Broken-Token CPT-Filtering and TRYLOCK Layer 0 - both rule-based approaches from published work

I'm noticing some concerns with the baseline setup. The published results for comparisons 5 and 6 aren't reproduced directly, which weakens the claims if the benchmarks don't align perfectly. I'm also wondering whether there are other neural network-based defense baselines I should consider, or if a simpler approach like fine-tuning on augmented data without any curriculum structure would be a useful control.

There's also the canonicalization baseline—decode-then-classify—that the paper argues against methodologically but never actually tests empirically, even though they acknowledge it as a natural alternative.

For evaluation, I'm looking at external benchmarks like HarmBench, JailbreakBench, and WildGuardTest with encoding perturbations, plus EncoAttack with 12,000 test cases and held-out encoding families. The metrics cover encoding-ASR, clean FPR, per-encoding breakdowns, and ECS correlation. But I need to clarify how the encoding-perturbed variants of those benchmarks are created—whether they're standard or custom—and validate that approach if it's novel.

On ablations, the design covers random vs curriculum ordering, reverse curriculum directionality, static vs co-evolutionary training, and ECS correlation analysis. But I'm noticing gaps: the ECS formula itself has three weighted components that should be tested individually, different curriculum pacing strategies could matter, and sensitivity to curriculum thresholds isn't addressed.

The feasibility section raises a red flag on the timeline—10 days to implement ECS, build encoding generators, set up the co-evolutionary GRPO loop, run all baselines, and complete evaluation feels extremely tight unless there's already substantial infrastructure in place. The co-evolutionary training on a 1.5B model also assumes hyperparameters work immediately, and running 5 random seeds for the baseline adds significant compute overhead that needs clarification. They're using training FLOPs as the primary metric for compute fairness, supplemented by tokens and wall-clock time.

Now I'm thinking through the potential issues with their approach. The oracle reliability concern is real—if GPT-4o struggles to judge heavily encoded content, the training signal degrades in Stage 2, and the fallback to a deterministic decoder might not handle the encodings the attacker generates. The held-out encoding families seem reasonably diverse for encoding-level attacks, though they don't cover structurally different approaches like steganography. The generalization claim in H2 is quite strong—if random-order achieves 45% instead of 60%, the contribution threshold becomes ambiguous.

I'm also noticing some methodological gaps: curriculum ordering only gets one seed while random-order gets five, so I can't measure variance properly. The 2% FPR constraint feels like a hard cutoff without ROC curve analysis or tradeoff reporting. They're missing an empirical test of the canonicalization baseline despite arguing against it theoretically. And the ECS weight setting via pilot study could be circular if the pilot and main evaluation overlap—they need to clarify that weights come from a separate validation set.

Overall, this is a reasonably well-designed proposal with clear hypotheses,

The main fixable issues are the missing canonicalization baseline, unequal statistical rigor across conditions, no ECS component ablation, and the need for FPR-ASR tradeoff analysis beyond just the hard cutoff. The 10-day timeline is also concerning given the scope, though if they have existing infrastructure and a fallback plan, it might work for a first submission. The bigger risk is whether GPT-4o can reliably decode the complex encodings they're relying on as ground truth.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5cce8e1-4e92-4a24-8c7e-8da7e69e4360",
  "isSidechain": false,
  "requestId": "req_011Cb6EeDKU2Y78hrNdRKYr1",
  "type": "assistant",
  "uuid": "126aa895-621c-48f3-b682-cdfb8f341629",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a7d6b8f5-4057-4d41-b2ff-8e10e79ef9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yhS5WVW17XawR3d3yxaWu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4508,
      "cache_read_input_tokens": 13279,
      "output_tokens": 3878,
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
          "output_tokens": 3878,
          "cache_read_input_tokens": 13279,
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

_source line 8 · 2026-05-16T12:20:58.325Z_

【状态】: 有缺陷待补救

---

【缺陷 1】
- 类别: baseline 不足或过时
- 问题: Proposal 在 Methodology 中用整段文字论证"Why Not Learned Canonicalization?"并列出三条理论原因，但实验设计中**没有对应的经验性 baseline**。无论理论论证多充分，reviewer 几乎一定会问 "show me the number"。当前 baseline 列表缺少一个 decode-then-classify pipeline（即使是简单实现）的定量对比。
- 严重度: 可补救
- 补救方案: 增加一个 "Oracle-Decode + LlamaGuard-3" baseline：用确定性解码器（proposal 中已有此组件）解码输入，再接标准 guardrail 分类器。对简单编码此 baseline 应表现良好，对嵌套编码应展示 error propagation 问题，从而用数据而非纯理论支撑 end-to-end 方法的优势。此 baseline 零额外训练开销，仅需推理时间。

【缺陷 2】
- 类别: 实验设计不足（统计严谨性）
- 问题: Random-order baseline 规定了 5 random seeds 报告 mean ± std，但 curriculum-ordered training（核心方法）**没有说明用多少 seeds**。如果 curriculum 只跑 1 次而 random-order 跑 5 次，reviewer 会质疑 curriculum 的表现是否为幸运种子的产物。尤其是 H1 声称 "≥10pp" 的提升幅度需要统计检验支撑。
- 严重度: 可补救
- 补救方案: 对 curriculum-ordered training 同样跑 3-5 seeds（至少 3 seeds），报告 mean ± std，并对 H1 进行配对 t-test 或 bootstrap confidence interval。Compute budget 相应增加约 2× classifier training time（~16 hours），在 4×A100 集群上仍可承受。

【缺陷 3】
- 类别: ablation 不完整
- 问题: ECS 由三个加权组件（NestingDepth, CPT_Deviation, TokenizerPerplexity）组成，权重通过 pilot study 确定。但实验设计中没有对 ECS 组件进行 ablation——如果去掉其中一项，curriculum ordering 是否同样有效？Reviewer 会质疑三项是否都 necessary，以及权重设定是否 robust。
- 严重度: 可补救
- 补救方案: 增加 3 个 leave-one-out ablation：分别去掉 NestingDepth/CPT_Deviation/TokenizerPerplexity，仅用剩余两项排序训练数据，评估 H1 指标变化。这不需要额外数据生成（排序改变即可），计算开销为 3× classifier training ≈ 24 hours。此外报告 ECS 权重在合理范围内的 sensitivity analysis（±20% 扰动）。

【缺陷 4】
- 类别: 评估方案缺陷
- 问题: Clean FPR 约束为硬性 ≤2% cutoff，但没有设计 FPR-ASR tradeoff 分析。如果 curriculum 方法在 2% FPR 时 ASR=20%，而 random-order 在 3% FPR 时 ASR=22%，单看 2% 截断线上的比较是不公平的。此外，proposal 未明确指定 benign test set 的来源和规模。
- 严重度: 可补救
- 补救方案: (1) 增加 ROC 曲线/FPR-ASR Pareto frontier 分析：在多个 FPR 阈值（0.5%, 1%, 2%, 5%）下报告对应 ASR，绘制 Pareto 曲线。(2) 明确 benign test set：使用 WildGuardTest 的 benign split（~1000 条）+ LMSYS-Chat-1M 随机采样 1000 条，两个分布分别报告 FPR。

【缺陷 5】
- 类别: 可行性问题（时间线）
- 问题: 10 天时间线对所述工作量极度紧张。仅列举必须完成的独立工作流：(a) ECS 实现 + encoding generator 代码库；(b) GRPO attacker 训练；(c) 4 个 controlled baselines（含 5 seeds for random-order）；(d) oracle pilot + 全量 oracle 调用；(e) 4 个外部 benchmark 的 encoding-perturbed 版本构建；(f) EncoAttack 12K test cases 生成 + 验证；(g) held-out encoding 实现。即使不算写作，纯实验执行按 proposal 给出的 ~30h 训练时间 × 多个 seeds 和 ablations，在 4×A100 上并行度有限。
- 严重度: 可补救
- 补救方案: (1) 将时间线扩展至 14-16 天，或明确标注哪些实验可并行（不同 seed 的 baseline 可以同时跑在不同 GPU 上）。(2) 对 camera-ready ablations（ECS component ablation、stability mechanism ablation）与 submission-critical experiments 做优先级区分，仅在初稿中完成 H1-H3 核心实验，标注 "camera-ready 完善"。(3) 补上缺陷 2 和缺陷 3 增加的实验所需时间。

【缺陷 6】
- 类别: 实验设计不足（表征层面证据缺失）
- 问题: Core thesis 声称 curriculum training 产生 "encoding-invariant representations" 和 "compositional encoding-detection primitives"，但实验设计中唯一的验证是 task-level metrics（ASR/FPR）和 learning dynamics curves。**没有表征层面的直接证据**证明模型确实学到了 encoding-invariant features，而非通过其他机制（如记忆更多模式）实现泛化。Reviewer 可以合理质疑："也许 curriculum 只是更好的数据调度策略，并不真的产生 invariant representations。"
- 严重度: 可补救
- 补救方案: 增加一个 representation analysis 实验：(1) 对相同 harmful prompt 的 plaintext / 各种编码变体提取 classifier 倒数第二层表征；(2) 计算 curriculum-trained vs random-order-trained 模型上，同一 prompt 不同编码间的 CKA/cosine similarity；(3) 预期：curriculum 模型中同一 prompt 不同编码的表征应更聚集（higher similarity），直接支撑 "encoding-invariant" 的 claim。此分析仅需推理，无额外训练开销。

---

**总结**：实验设计整体框架 solid（假设清晰、controlled comparisons 设计合理、fallback plan 务实），但存在上述 6 个可补救缺陷。其中**缺陷 1（canonicalization baseline）和缺陷 6（表征证据）**对 reviewer 说服力影响最大，建议优先修复。所有缺陷均不涉及方向性致命问题，补救后实验设计可达 EMNLP 主会门槛。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "126aa895-621c-48f3-b682-cdfb8f341629",
  "isSidechain": false,
  "requestId": "req_011Cb6EeDKU2Y78hrNdRKYr1",
  "type": "assistant",
  "uuid": "df7dd090-34aa-49f3-8bcf-533e3394b045",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a7d6b8f5-4057-4d41-b2ff-8e10e79ef9d7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yhS5WVW17XawR3d3yxaWu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4508,
      "cache_read_input_tokens": 13279,
      "output_tokens": 3878,
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
          "output_tokens": 3878,
          "cache_read_input_tokens": 13279,
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
  "leafUuid": "df7dd090-34aa-49f3-8bcf-533e3394b045",
  "sessionId": "a7d6b8f5-4057-4d41-b2ff-8e10e79ef9d7"
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "EncoGuard: curriculum-based encoding-robust safety training",
  "sessionId": "a7d6b8f5-4057-4d41-b2ff-8e10e79ef9d7"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## Title  EncoGuard: Learning Encoding-Invariant Safety Features via Complexity-Structured Curriculum Training  ## Problem Statement  Encoding-based jailbreak attacks (base64, ROT13, homoglyph substit…",
  "leafUuid": "df7dd090-34aa-49f3-8bcf-533e3394b045",
  "sessionId": "a7d6b8f5-4057-4d41-b2ff-8e10e79ef9d7"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "EncoGuard: curriculum-based encoding-robust safety training",
  "sessionId": "a7d6b8f5-4057-4d41-b2ff-8e10e79ef9d7"
}
```

---
