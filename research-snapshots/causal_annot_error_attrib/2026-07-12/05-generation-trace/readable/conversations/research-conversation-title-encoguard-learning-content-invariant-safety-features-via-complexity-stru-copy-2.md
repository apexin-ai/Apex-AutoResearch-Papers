# Research conversation: Title EncoGuard: Learning Content-Invariant Safety Features via Complexity-Structured Curriculum for Encoding-Based Atta

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/031381c6-d0f3-4dbb-bfe2-0f8311bded45.jsonl`
- **Structured JSON:** [`12a775cc438d9eb406f0.json`](../../sessions/12/12a775cc438d9eb406f0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T12:23:58.187Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:23:58.187Z",
  "sessionId": "031381c6-d0f3-4dbb-bfe2-0f8311bded45",
  "content": "## Title\n\nEncoGuard: Learning Content-Invariant Safety Features via Complexity-Structured Curriculum for Encoding-Based Attacks\n\n## Problem Statement\n\nEncoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, and their nested compositions) exploit a fundamental vulnerability in LLM safety guardrails: classifiers trained on plaintext or limited encoding variations fail when inputs are transformed through unseen encoding schemes. Existing defenses fall into two categories, both with critical limitations:\n\n1. **Rule-based detection + decoding pipelines** (e.g., regex-based encoding detection → known decoder → standard guardrail): Effective for known single-layer encodings with distinctive statistical signatures, but fail on (a) partial encoding where only segments are transformed, (b) adversarial mixing of encoded/plaintext to evade detection heuristics, and (c) novel encodings without pre-programmed decoders.\n\n2. **Learned canonicalization** (seq2seq decode → classify): Suffers from error propagation in nested encodings, creates a new adversarial attack surface (the canonicalizer itself), and requires semantic understanding to identify which portions to decode.\n\nThe core challenge is achieving **generalization to unseen encoding families**—classifiers that remain robust against encoding types never encountered during training. No existing defense reliably provides this capability.\n\n## Core Thesis\n\nWe hypothesize that a classifier trained via **complexity-structured curriculum**—where encoding attacks are presented in order of a principled complexity metric—learns **content-invariant safety features** that generalize to held-out encoding types unseen during training. The key mechanism is **representation disentanglement**: curriculum ordering forces the model to first anchor the semantic signature of harmful content under low-noise surface perturbations (simple encodings), then learn to preserve this semantic signature under progressively higher-noise perturbations (complex encodings). The result is a representation space where harmful content clusters by semantic meaning regardless of surface encoding—a separation of content features from encoding-specific surface features.\n\nThis differs fundamentally from memorizing encoding-specific detection patterns. A model that merely memorizes base64 character distributions cannot generalize to Braille; but a model that has learned to extract content semantics despite surface perturbation can generalize to any encoding that preserves underlying content structure.\n\n**General Principle:** This approach instantiates a broader defense paradigm for compositional attack spaces: when attacks are built from composable primitives with natural complexity ordering, structured curriculum training can induce invariance to attack-specific surface features while preserving task-relevant content features. We demonstrate this principle on encoding attacks as the canonical instance where complexity is formally quantifiable.\n\n## Relationship to Prior Work on Curriculum Adversarial Training\n\nCurriculum-based approaches to adversarial robustness exist (Cai et al., IJCAI 2018: progressively increasing perturbation magnitude for image classifiers; Wang et al., NeurIPS 2021: ordered SGD by sample difficulty). Our work differs in two critical dimensions:\n\n1. **Discrete compositional attack space vs. continuous perturbation space:** Prior work operates in continuous ε-ball perturbation spaces where difficulty is a scalar magnitude. Encoding attacks form a discrete compositional space where primitives (base64, ROT13, homoglyphs) can be arbitrarily nested—requiring a multi-dimensional complexity metric rather than a single scalar.\n\n2. **OOD generalization vs. in-distribution robustness:** Prior curriculum adversarial training only evaluates robustness against the same attack types used during training (within the same ε-ball). We explicitly evaluate generalization to **entirely unseen encoding families** (Braille, Morse, custom ciphers)—demonstrating that curriculum ordering induces transferable content-invariance, not just better in-distribution fitting. This OOD generalization claim is our primary novel contribution.\n\n## Key Contributions\n\n1. **Primary Contribution (Representation Disentanglement via Curriculum):** We demonstrate that complexity-structured curriculum training produces content-invariant representations that generalize to entirely unseen encoding families (Braille, Morse, custom cipher, NATO phonetic), while flat augmentation and random-order training do not. We provide direct representation-level evidence (CKA similarity analysis) that curriculum-trained models cluster same-content different-encoding inputs more tightly than baselines.\n\n2. **Formalized Encoding Complexity Score (ECS):** A principled complexity metric combining nesting depth, character-per-token (CPT) ratio deviation, and tokenizer perplexity. We validate that ECS predicts classifier difficulty on held-out encodings (Spearman ρ), establishing it as a transferable methodological contribution for any encoding-related defense work.\n\n3. **Co-Evolutionary Training Framework:** GRPO-trained attacker generates encoding attacks of escalating ECS, paired with SFT classifier trained on curriculum-ordered adversarial data. The co-evolutionary dynamic ensures curriculum adapts to classifier capability frontier.\n\n4. **Comprehensive Controlled Evaluation:** Controlled ablations (random-order, flat augmentation, reverse curriculum, static curriculum, decode-then-classify pipeline) with multi-seed statistical validation, supplemented by representation analysis directly verifying the content-invariance claim.\n\n## Methodology\n\n### Encoding Complexity Score (ECS)\n\n$$ECS(e) = \\alpha \\cdot \\text{NestingDepth}(e) + \\beta \\cdot \\text{CPT\\_Deviation}(e) + \\gamma \\cdot \\text{TokenizerPerplexity}(e)$$\n\n- NestingDepth: number of compositional encoding layers\n- CPT_Deviation: absolute deviation of encoded text's characters-per-token ratio from plaintext baseline\n- TokenizerPerplexity: perplexity of target model's tokenizer on encoded text\n\nWeights determined via pilot study measuring correlation of each component with classifier error rate on a validation set. Pilot results reported to justify weight selection. Full leave-one-out component ablation planned for camera-ready.\n\n### Mechanistic Motivation: Content-Invariance via Progressive Noise Escalation\n\nUnder flat exposure, the classifier simultaneously encounters simple encodings (low surface noise, content semantics still partially accessible through tokenization) and complex nested encodings (high surface noise, content semantics completely obscured at token level). For high-noise inputs in early training, the model cannot extract content signal—gradients from these samples are effectively random with respect to content features, interfering with content-feature learning on low-noise inputs.\n\nCurriculum ordering resolves this by staged noise escalation:\n- **Stage 1 (low-ECS):** Simple encodings partially preserve content-correlated token patterns. The model learns to extract harmful-content semantic features despite mild surface perturbation, anchoring a content representation.\n- **Stage 2 (high-ECS):** Complex encodings fully obscure surface patterns. But the model already has anchored content features from Stage 1—it now learns to access these features through higher-noise channels, effectively learning encoding-invariance as noise robustness.\n\nThis predicts generalization: a model that has learned \"extract content semantics despite surface noise\" should transfer to any novel encoding that preserves content structure—regardless of the specific noise pattern. Braille (character substitution) and Morse (symbolic re-encoding) are different noise types but preserve content, so a content-invariant model should handle them.\n\n### Why Not Simpler Alternatives?\n\n**Rule-based detection + decode:** For known single-layer encodings (base64, ROT13) with distinctive character-set signatures, regex detection + decode + standard guardrail achieves high accuracy at near-zero cost. Our method targets the regime where this fails:\n- **Partial encoding:** Only segments of input are encoded, defeating whole-input detection heuristics\n- **Adversarial mixing:** Attacker deliberately mixes encoded/plaintext to create ambiguous statistical signatures\n- **Novel encodings:** No pre-programmed decoder exists (the motivating scenario for generalization)\n\nWe include a Deterministic-Decode + LlamaGuard-3 baseline to empirically demonstrate this boundary.\n\n**Learned canonicalization:** (1) Error propagation—each nested decode step compounds errors; (2) canonicalizer becomes a new attack surface; (3) partial encoding requires semantic understanding to identify decode targets.\n\n### Co-Evolutionary Training Loop\n\n**Attacker (Qwen2.5-1.5B, GRPO-trained):**\n- Generates encoding attacks with ECS constrained to current curriculum stage\n- Reward: +1 if encoding bypasses current classifier AND oracle confirms harmful content\n- Entropy regularization prevents collapse to single encoding type\n\n**Classifier (Qwen2.5-4B, SFT):**\n- Trains on curriculum-ordered adversarial examples (Stage 1: ECS ≤ threshold, Stage 2: ECS > threshold)\n- FPR rollback: revert checkpoint if FPR exceeds 2% on benign validation set\n- Semantic deduplication: removes near-duplicates (cosine similarity > 0.95)\n\n**Oracle:** GPT-4o judges content harmfulness. Deterministic decoder cross-validates; disagreements excluded.\n\n**Fallback Plan:** If co-evolutionary loop proves unstable by Day 6, fall back to static curriculum-ordered SFT (pre-generated curriculum data, no GRPO attacker). This still validates H1-H3.\n\n### Compute and Cost\n\n- Hardware: 4× A100 80GB\n- Classifier training: ~8h per run × 3 seeds × 2 stages = ~48h (parallelizable across GPUs)\n- Baselines: random-order (5 seeds × 8h = 40h), flat augmentation (3 seeds × 8h = 24h), reverse curriculum (3 seeds × 8h = 24h), static curriculum (3 seeds × 8h = 24h)\n- Attacker training: ~6h per round × 2 rounds = 12h\n- Oracle: ~18K calls ≈ $200-350\n- Representation analysis: inference only, ~2h\n- Total: ~160h GPU-hours (manageable on 4×A100 over 16 days with parallelization)\n- Compute normalization: training FLOPs (primary), with training tokens and wall-clock reported\n\n## Experimental Design\n\n### Hypotheses\n\n- **H1 (Curriculum > Random):** Curriculum-ordered training achieves ≥10pp lower encoding-ASR than random-order at equivalent FLOPs (validated by paired t-test across seeds, p < 0.05).\n- **H2 (OOD Generalization):** Curriculum-trained classifier maintains ≤30% encoding-ASR on held-out encoding families (Braille, Morse, custom cipher, NATO phonetic) where random-order and flat augmentation exceed 60%.\n- **H3 (ECS Predictiveness):** ECS correlates with classifier error rate (Spearman ρ ≥ 0.7) on held-out encodings.\n- **H4 (Co-evolution > Static):** Co-evolutionary training outperforms static curriculum SFT by ≥5pp on composite encodings (conditional on co-evolutionary loop stability).\n\n### Baselines and Ablations\n\n**Controlled comparisons (same architecture, same FLOPs, multi-seed):**\n1. Random-order training: 5 seeds, mean ± std\n2. Flat augmentation: 3 seeds\n3. Reverse curriculum (high-ECS first, then low-ECS): 3 seeds\n4. Static curriculum SFT (no co-evolutionary attacker): 3 seeds\n5. **Deterministic-Decode + LlamaGuard-3 pipeline:** Deterministic decoder attempts to decode input, decoded text classified by LlamaGuard-3. No training needed.\n\n**Curriculum (our method):** 3 seeds, mean ± std\n\n**Indicative comparisons (Discussion section):**\n6. Broken-Token CPT-Filtering (published numbers)\n7. TRYLOCK Layer 0 (published numbers)\n\n### Evaluation Protocol\n\n**External benchmarks (primary evidence):**\n- HarmBench encoding-perturbed variant\n- JailbreakBench encoding attack subset\n- WildGuardTest encoding-perturbed variant\n\n**EncoAttack (supplementary analysis):**\n- 500 base prompts: HarmBench (200) + AdvBench (150) + WildGuardTest (150), 10+ harm categories\n- 8 encoding types × 3 nesting levels = 12,000 test cases\n- Independent encoding implementation from training pipeline\n- Validation: ≥80% bypass rate on undefended LlamaGuard-3\n\n**Held-out encoding families (generalization test—NEVER seen during training):**\n- Braille Unicode substitution\n- Morse code symbolic encoding\n- Custom Caesar-variant cipher (position-dependent shift)\n- NATO phonetic alphabet encoding\n\n**Metrics:**\n- Encoding-ASR (primary)\n- Clean FPR at multiple thresholds (0.5%, 1%, 2%, 5%) with Pareto frontier analysis\n- Benign test set: WildGuardTest benign split (~1000) + LMSYS-Chat-1M random sample (1000)\n- Per-encoding-type breakdown\n- ECS-difficulty correlation on held-out encodings\n\n### Representation Analysis (Direct Evidence for Content-Invariance)\n\nFor each of 100 harmful prompts, generate plaintext + 8 encoding variants. Extract classifier penultimate-layer representations. Compute:\n1. **Intra-prompt cross-encoding similarity:** Average cosine similarity between same-prompt different-encoding representations\n2. **CKA analysis:** Centered Kernel Alignment between encoding-variant representation matrices\n3. **Compare curriculum-trained vs. random-order-trained:** Prediction—curriculum model shows significantly higher intra-prompt similarity (content clusters by meaning, not by encoding type)\n\nThis directly validates \"encoding-invariant representations\" without relying solely on task-level metrics.\n\n### Learning Dynamics\n\n- Per-checkpoint (every 500 steps) encoding-ASR curves\n- Separate curves for low-ECS and high-ECS encodings\n- Expected: curriculum shows earlier convergence on low-ECS, smooth transition to high-ECS; random-order shows chaotic learning on both\n\n### Oracle Reliability Pilot\n\nBefore full training: 100 samples per ECS band, measure GPT-4o agreement with deterministic decoder. If agreement < 80% for high-ECS, switch to deterministic-only oracle for Stage 2.\n\n## Stability Mechanisms (Not Claimed as Contributions)\n\n- Entropy regularization (from TriPlay-RL diversity penalty)\n- FPR rollback (standard safety constraint)\n- Semantic deduplication (standard data quality)\n\nTrigger frequencies reported as indirect utility evidence. Full ablation in camera-ready.\n\n## Timeline (16 days)\n\n**Submission-critical (Days 1-12):**\n- Days 1-3: ECS implementation, encoding generators, data pipeline, oracle pilot\n- Days 4-7: Curriculum training (3 seeds) + random-order (5 seeds) + flat augmentation (3 seeds) [parallelized across GPUs]\n- Days 8-9: Reverse curriculum (3 seeds) + decode-pipeline baseline + co-evolutionary attempt\n- Days 10-11: Full evaluation on all benchmarks + held-out encodings + representation analysis\n- Day 12: Core results analysis, statistical tests, main writing\n\n**Camera-ready extensions (Days 13-16 + post-submission):**\n- Day 13-14: ECS component leave-one-out ablation (3 runs)\n- Day 15: Stability mechanism ablation\n- Day 16: Writing polish, full 5-seed curriculum if time permits\n\n**Fallback trigger:** If co-evolutionary loop unstable by Day 6, switch to static curriculum SFT."
}
```

---

### Runtime record

_source line 2 · 2026-05-16T12:23:58.195Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:23:58.195Z",
  "sessionId": "031381c6-d0f3-4dbb-bfe2-0f8311bded45"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-16T12:23:58.210Z_

## Title

EncoGuard: Learning Content-Invariant Safety Features via Complexity-Structured Curriculum for Encoding-Based Attacks

## Problem Statement

Encoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, and their nested compositions) exploit a fundamental vulnerability in LLM safety guardrails: classifiers trained on plaintext or limited encoding variations fail when inputs are transformed through unseen encoding schemes. Existing defenses fall into two categories, both with critical limitations:

1. **Rule-based detection + decoding pipelines** (e.g., regex-based encoding detection → known decoder → standard guardrail): Effective for known single-layer encodings with distinctive statistical signatures, but fail on (a) partial encoding where only segments are transformed, (b) adversarial mixing of encoded/plaintext to evade detection heuristics, and (c) novel encodings without pre-programmed decoders.

2. **Learned canonicalization** (seq2seq decode → classify): Suffers from error propagation in nested encodings, creates a new adversarial attack surface (the canonicalizer itself), and requires semantic understanding to identify which portions to decode.

The core challenge is achieving **generalization to unseen encoding families**—classifiers that remain robust against encoding types never encountered during training. No existing defense reliably provides this capability.

## Core Thesis

We hypothesize that a classifier trained via **complexity-structured curriculum**—where encoding attacks are presented in order of a principled complexity metric—learns **content-invariant safety features** that generalize to held-out encoding types unseen during training. The key mechanism is **representation disentanglement**: curriculum ordering forces the model to first anchor the semantic signature of harmful content under low-noise surface perturbations (simple encodings), then learn to preserve this semantic signature under progressively higher-noise perturbations (complex encodings). The result is a representation space where harmful content clusters by semantic meaning regardless of surface encoding—a separation of content features from encoding-specific surface features.

This differs fundamentally from memorizing encoding-specific detection patterns. A model that merely memorizes base64 character distributions cannot generalize to Braille; but a model that has learned to extract content semantics despite surface perturbation can generalize to any encoding that preserves underlying content structure.

**General Principle:** This approach instantiates a broader defense paradigm for compositional attack spaces: when attacks are built from composable primitives with natural complexity ordering, structured curriculum training can induce invariance to attack-specific surface features while preserving task-relevant content features. We demonstrate this principle on encoding attacks as the canonical instance where complexity is formally quantifiable.

## Relationship to Prior Work on Curriculum Adversarial Training

Curriculum-based approaches to adversarial robustness exist (Cai et al., IJCAI 2018: progressively increasing perturbation magnitude for image classifiers; Wang et al., NeurIPS 2021: ordered SGD by sample difficulty). Our work differs in two critical dimensions:

1. **Discrete compositional attack space vs. continuous perturbation space:** Prior work operates in continuous ε-ball perturbation spaces where difficulty is a scalar magnitude. Encoding attacks form a discrete compositional space where primitives (base64, ROT13, homoglyphs) can be arbitrarily nested—requiring a multi-dimensional complexity metric rather than a single scalar.

2. **OOD generalization vs. in-distribution robustness:** Prior curriculum adversarial training only evaluates robustness against the same attack types used during training (within the same ε-ball). We explicitly evaluate generalization to **entirely unseen encoding families** (Braille, Morse, custom ciphers)—demonstrating that curriculum ordering induces transferable content-invariance, not just better in-distribution fitting. This OOD generalization claim is our primary novel contribution.

## Key Contributions

1. **Primary Contribution (Representation Disentanglement via Curriculum):** We demonstrate that complexity-structured curriculum training produces content-invariant representations that generalize to entirely unseen encoding families (Braille, Morse, custom cipher, NATO phonetic), while flat augmentation and random-order training do not. We provide direct representation-level evidence (CKA similarity analysis) that curriculum-trained models cluster same-content different-encoding inputs more tightly than baselines.

2. **Formalized Encoding Complexity Score (ECS):** A principled complexity metric combining nesting depth, character-per-token (CPT) ratio deviation, and tokenizer perplexity. We validate that ECS predicts classifier difficulty on held-out encodings (Spearman ρ), establishing it as a transferable methodological contribution for any encoding-related defense work.

3. **Co-Evolutionary Training Framework:** GRPO-trained attacker generates encoding attacks of escalating ECS, paired with SFT classifier trained on curriculum-ordered adversarial data. The co-evolutionary dynamic ensures curriculum adapts to classifier capability frontier.

4. **Comprehensive Controlled Evaluation:** Controlled ablations (random-order, flat augmentation, reverse curriculum, static curriculum, decode-then-classify pipeline) with multi-seed statistical validation, supplemented by representation analysis directly verifying the content-invariance claim.

## Methodology

### Encoding Complexity Score (ECS)

$$ECS(e) = \alpha \cdot \text{NestingDepth}(e) + \beta \cdot \text{CPT\_Deviation}(e) + \gamma \cdot \text{TokenizerPerplexity}(e)$$

- NestingDepth: number of compositional encoding layers
- CPT_Deviation: absolute deviation of encoded text's characters-per-token ratio from plaintext baseline
- TokenizerPerplexity: perplexity of target model's tokenizer on encoded text

Weights determined via pilot study measuring correlation of each component with classifier error rate on a validation set. Pilot results reported to justify weight selection. Full leave-one-out component ablation planned for camera-ready.

### Mechanistic Motivation: Content-Invariance via Progressive Noise Escalation

Under flat exposure, the classifier simultaneously encounters simple encodings (low surface noise, content semantics still partially accessible through tokenization) and complex nested encodings (high surface noise, content semantics completely obscured at token level). For high-noise inputs in early training, the model cannot extract content signal—gradients from these samples are effectively random with respect to content features, interfering with content-feature learning on low-noise inputs.

Curriculum ordering resolves this by staged noise escalation:
- **Stage 1 (low-ECS):** Simple encodings partially preserve content-correlated token patterns. The model learns to extract harmful-content semantic features despite mild surface perturbation, anchoring a content representation.
- **Stage 2 (high-ECS):** Complex encodings fully obscure surface patterns. But the model already has anchored content features from Stage 1—it now learns to access these features through higher-noise channels, effectively learning encoding-invariance as noise robustness.

This predicts generalization: a model that has learned "extract content semantics despite surface noise" should transfer to any novel encoding that preserves content structure—regardless of the specific noise pattern. Braille (character substitution) and Morse (symbolic re-encoding) are different noise types but preserve content, so a content-invariant model should handle them.

### Why Not Simpler Alternatives?

**Rule-based detection + decode:** For known single-layer encodings (base64, ROT13) with distinctive character-set signatures, regex detection + decode + standard guardrail achieves high accuracy at near-zero cost. Our method targets the regime where this fails:
- **Partial encoding:** Only segments of input are encoded, defeating whole-input detection heuristics
- **Adversarial mixing:** Attacker deliberately mixes encoded/plaintext to create ambiguous statistical signatures
- **Novel encodings:** No pre-programmed decoder exists (the motivating scenario for generalization)

We include a Deterministic-Decode + LlamaGuard-3 baseline to empirically demonstrate this boundary.

**Learned canonicalization:** (1) Error propagation—each nested decode step compounds errors; (2) canonicalizer becomes a new attack surface; (3) partial encoding requires semantic understanding to identify decode targets.

### Co-Evolutionary Training Loop

**Attacker (Qwen2.5-1.5B, GRPO-trained):**
- Generates encoding attacks with ECS constrained to current curriculum stage
- Reward: +1 if encoding bypasses current classifier AND oracle confirms harmful content
- Entropy regularization prevents collapse to single encoding type

**Classifier (Qwen2.5-4B, SFT):**
- Trains on curriculum-ordered adversarial examples (Stage 1: ECS ≤ threshold, Stage 2: ECS > threshold)
- FPR rollback: revert checkpoint if FPR exceeds 2% on benign validation set
- Semantic deduplication: removes near-duplicates (cosine similarity > 0.95)

**Oracle:** GPT-4o judges content harmfulness. Deterministic decoder cross-validates; disagreements excluded.

**Fallback Plan:** If co-evolutionary loop proves unstable by Day 6, fall back to static curriculum-ordered SFT (pre-generated curriculum data, no GRPO attacker). This still validates H1-H3.

### Compute and Cost

- Hardware: 4× A100 80GB
- Classifier training: ~8h per run × 3 seeds × 2 stages = ~48h (parallelizable across GPUs)
- Baselines: random-order (5 seeds × 8h = 40h), flat augmentation (3 seeds × 8h = 24h), reverse curriculum (3 seeds × 8h = 24h), static curriculum (3 seeds × 8h = 24h)
- Attacker training: ~6h per round × 2 rounds = 12h
- Oracle: ~18K calls ≈ $200-350
- Representation analysis: inference only, ~2h
- Total: ~160h GPU-hours (manageable on 4×A100 over 16 days with parallelization)
- Compute normalization: training FLOPs (primary), with training tokens and wall-clock reported

## Experimental Design

### Hypotheses

- **H1 (Curriculum > Random):** Curriculum-ordered training achieves ≥10pp lower encoding-ASR than random-order at equivalent FLOPs (validated by paired t-test across seeds, p < 0.05).
- **H2 (OOD Generalization):** Curriculum-trained classifier maintains ≤30% encoding-ASR on held-out encoding families (Braille, Morse, custom cipher, NATO phonetic) where random-order and flat augmentation exceed 60%.
- **H3 (ECS Predictiveness):** ECS correlates with classifier error rate (Spearman ρ ≥ 0.7) on held-out encodings.
- **H4 (Co-evolution > Static):** Co-evolutionary training outperforms static curriculum SFT by ≥5pp on composite encodings (conditional on co-evolutionary loop stability).

### Baselines and Ablations

**Controlled comparisons (same architecture, same FLOPs, multi-seed):**
1. Random-order training: 5 seeds, mean ± std
2. Flat augmentation: 3 seeds
3. Reverse curriculum (high-ECS first, then low-ECS): 3 seeds
4. Static curriculum SFT (no co-evolutionary attacker): 3 seeds
5. **Deterministic-Decode + LlamaGuard-3 pipeline:** Deterministic decoder attempts to decode input, decoded text classified by LlamaGuard-3. No training needed.

**Curriculum (our method):** 3 seeds, mean ± std

**Indicative comparisons (Discussion section):**
6. Broken-Token CPT-Filtering (published numbers)
7. TRYLOCK Layer 0 (published numbers)

### Evaluation Protocol

**External benchmarks (primary evidence):**
- HarmBench encoding-perturbed variant
- JailbreakBench encoding attack subset
- WildGuardTest encoding-perturbed variant

**EncoAttack (supplementary analysis):**
- 500 base prompts: HarmBench (200) + AdvBench (150) + WildGuardTest (150), 10+ harm categories
- 8 encoding types × 3 nesting levels = 12,000 test cases
- Independent encoding implementation from training pipeline
- Validation: ≥80% bypass rate on undefended LlamaGuard-3

**Held-out encoding families (generalization test—NEVER seen during training):**
- Braille Unicode substitution
- Morse code symbolic encoding
- Custom Caesar-variant cipher (position-dependent shift)
- NATO phonetic alphabet encoding

**Metrics:**
- Encoding-ASR (primary)
- Clean FPR at multiple thresholds (0.5%, 1%, 2%, 5%) with Pareto frontier analysis
- Benign test set: WildGuardTest benign split (~1000) + LMSYS-Chat-1M random sample (1000)
- Per-encoding-type breakdown
- ECS-difficulty correlation on held-out encodings

### Representation Analysis (Direct Evidence for Content-Invariance)

For each of 100 harmful prompts, generate plaintext + 8 encoding variants. Extract classifier penultimate-layer representations. Compute:
1. **Intra-prompt cross-encoding similarity:** Average cosine similarity between same-prompt different-encoding representations
2. **CKA analysis:** Centered Kernel Alignment between encoding-variant representation matrices
3. **Compare curriculum-trained vs. random-order-trained:** Prediction—curriculum model shows significantly higher intra-prompt similarity (content clusters by meaning, not by encoding type)

This directly validates "encoding-invariant representations" without relying solely on task-level metrics.

### Learning Dynamics

- Per-checkpoint (every 500 steps) encoding-ASR curves
- Separate curves for low-ECS and high-ECS encodings
- Expected: curriculum shows earlier convergence on low-ECS, smooth transition to high-ECS; random-order shows chaotic learning on both

### Oracle Reliability Pilot

Before full training: 100 samples per ECS band, measure GPT-4o agreement with deterministic decoder. If agreement < 80% for high-ECS, switch to deterministic-only oracle for Stage 2.

## Stability Mechanisms (Not Claimed as Contributions)

- Entropy regularization (from TriPlay-RL diversity penalty)
- FPR rollback (standard safety constraint)
- Semantic deduplication (standard data quality)

Trigger frequencies reported as indirect utility evidence. Full ablation in camera-ready.

## Timeline (16 days)

**Submission-critical (Days 1-12):**
- Days 1-3: ECS implementation, encoding generators, data pipeline, oracle pilot
- Days 4-7: Curriculum training (3 seeds) + random-order (5 seeds) + flat augmentation (3 seeds) [parallelized across GPUs]
- Days 8-9: Reverse curriculum (3 seeds) + decode-pipeline baseline + co-evolutionary attempt
- Days 10-11: Full evaluation on all benchmarks + held-out encodings + representation analysis
- Day 12: Core results analysis, statistical tests, main writing

**Camera-ready extensions (Days 13-16 + post-submission):**
- Day 13-14: ECS component leave-one-out ablation (3 runs)
- Day 15: Stability mechanism ablation
- Day 16: Writing polish, full 5-seed curriculum if time permits

**Fallback trigger:** If co-evolutionary loop unstable by Day 6, switch to static curriculum SFT.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b4f3c58d-7621-49a1-8289-da67de803d58",
  "type": "user",
  "uuid": "eb52de7a-e9e8-4030-ac2d-6a517b7cc8fd",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "031381c6-d0f3-4dbb-bfe2-0f8311bded45",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T12:23:58.208Z_

```json
{
  "parentUuid": "eb52de7a-e9e8-4030-ac2d-6a517b7cc8fd",
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
  "uuid": "d7fcc31d-ae30-49a7-b814-bf6d505cd017",
  "timestamp": "2026-05-16T12:23:58.208Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "031381c6-d0f3-4dbb-bfe2-0f8311bded45",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T12:23:58.208Z_

```json
{
  "parentUuid": "d7fcc31d-ae30-49a7-b814-bf6d505cd017",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c4a2515c-83ea-49d6-a4c5-15a5eac6fb58",
  "timestamp": "2026-05-16T12:23:58.208Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "031381c6-d0f3-4dbb-bfe2-0f8311bded45",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## Title  EncoGuard: Learning Content-Invariant Safety Features via Complexity-Structured Curriculum for Encoding-Based Attacks  ## Problem Statement  Encoding-based jailbreak attacks (base64, ROT13,…",
  "leafUuid": "c4a2515c-83ea-49d6-a4c5-15a5eac6fb58",
  "sessionId": "031381c6-d0f3-4dbb-bfe2-0f8311bded45"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "EncoGuard: Encoding-Based Attack Defense via Curriculum Learning",
  "sessionId": "031381c6-d0f3-4dbb-bfe2-0f8311bded45"
}
```

---

### Assistant

_source line 8 · 2026-05-16T12:24:55.784Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal from the perspective of experimental design and technical execution. I need to evaluate:

1. Baseline coverage and fairness
2. Experimental design completeness
3. Evaluation metrics and protocol
4. Ablation design
5. Feasibility (compute, data, time, etc.)

Let me go through this systematically.

**Baselines:**
- Random-order training (5 seeds) ✓


- Flat augmentation (3 seeds) ✓
- Reverse curriculum (3 seeds) ✓
- Static curriculum SFT (3 seeds) ✓
- Deterministic-Decode + LlamaGuard-3 pipeline ✓
- Broken-Token CPT-Filtering (published numbers, indicative) ✓
- TRYLOCK Layer 0 (published numbers, indicative) ✓

This covers a solid range of controlled comparisons. Now I'm wondering what baselines might be conspicuously absent—the kind that would raise reviewer concerns. The main gap I'm seeing is whether we need a straightforward fine-tuning baseline applied across the full dataset without any curriculum or filtering strategy. encoding types without curriculum** — wait, that's essentially what "flat augmentation" is. OK.
2. **Anti-curriculum (easy last)** — that's the reverse curriculum. ✓
3. **A decoder-based approach (seq2seq canonicalization + classify)** — they mention this conceptually but don't include it as a baseline. They have "Deterministic-Decode + LlamaGuard-3" which is the rule-based decode approach, but not a learned canonicalization baseline.
4. **Existing published defense methods specific to encoding attacks** — They include Broken-Token and TRYLOCK as indicative comparisons. Are there others?

Actually, let me think more carefully. The "flat augmentation" baseline is essentially training on all encoding types without curriculum ordering, right? So this is the key comparison to show that curriculum ordering matters. And random-order is... training in random order? These might actually be different things — random-order probably takes the same curriculum-staged data but shuffles it, while flat augmentation trains on all encodings simultaneously from the start with uniform sampling. The distinction could be clearer, but they're testing whether the ordering itself matters versus just having the data.

**Evaluation Protocol:**
- External benchmarks: HarmBench, JailbreakBench, WildGuardTest — all encoding-perturbed ✓
- EncoAttack: custom benchmark with 12,000 test cases ✓
- Held-out encoding families: Braille, Morse, custom cipher, NATO phonetic ✓
- Metrics: Encoding-ASR, Clean FPR at multiple thresholds, per-encoding breakdown ✓
- Representation analysis: CKA, intra-prompt similarity ✓

**Ablation design:**
- Random vs. curriculum ordering ✓
- Reverse curriculum ✓
- Static vs. co-evolutionary ✓
- ECS component ablation (camera-ready) — not in main paper?
- Stability mechanism ablation (camera-ready) — not in main paper?

**Potential issues I see:**

1. **Seed count asymmetry**: Curriculum method uses 3 seeds while random-order uses 5 seeds. Why? This is unusual — typically you'd want equal seeds for fair comparison.

The evaluation setup looks comprehensive with external benchmarks, held-out encoding families, and multiple metrics including representation analysis. The ablations cover the key design choices around curriculum ordering and co-evolution, though some component ablations appear to be deferred to camera-ready. I'm noticing the seed count differs between baselines — curriculum uses 3 seeds while random-order uses 5, which seems like an odd asymmetry for a fair comparison.

There's also some ambiguity around what distinguishes "flat augmentation" from "random-order" baselines, and whether they're actually redundant. The proposal argues against learned canonicalization conceptually but doesn't include it as an empirical baseline, which could be a gap a reviewer points out. The ECS weights come from pilot study correlation, but the full ablation is deferred, which weakens the claim that ECS is a key contribution when its component importance isn't fully validated in the main paper. I should also check whether the compute costs are fairly distributed across methods.

The co-evolutionary approach with GRPO attacker and SFT classifier inherently requires more compute than static baselines, and while they mention FLOPs normalization, the 12 hours of attacker training adds compute not present in the baselines. Using GPT-4o as an oracle to judge harmfulness in heavily encoded text is also questionable—for deeply nested encodings, can it reliably assess content? They're planning a pilot with 100 samples per ECS band, but if agreement is low, switching to a deterministic-only oracle for Stage 2 introduces a confound. The validation criterion of ≥80% bypass rate on undefended LlamaGuard-3 confirms the test cases are actual attacks, though this is only on their custom benchmark.

I'm wondering about the external benchmarks—HarmBench, JailbreakBench, WildGuardTest with encoding perturbations—and whether these use standard perturbed versions or if the team creates their own encoding perturbations. The timeline is also concerning: 16 days is tight, and while the training schedule (11 runs across 4 days on 4×A100 GPUs) could theoretically fit if they run 4 in parallel at ~8 hours each, this doesn't account for debugging or hyperparameter tuning. The held-out encoding implementations—Braille, Morse, custom cipher, NATO phonetic—raises the question of who implements these and whether they're standardized.

There are also statistical design issues: they're planning paired t-tests with only 3 seeds for curriculum versus 5 for random-order, which creates an imbalance and gives the t-test very low power. The threshold definitions for H2 seem arbitrary—why ≤30% encoding-ASR for curriculum and >60% for baselines? If curriculum hits 35% and baselines hit 55%, the hypothesis technically fails even though the method shows improvement. I'm also noticing they haven't included a prompt-level defense baseline, like instructing the LLM to decode before responding.

Wait, I need to reconsider the setup here—this is about a safety classifier receiving potentially encoded text, not about making the LLM itself robust. So prompt-level defense is a different defense layer, but reviewers might still ask about it. There's also the question of whether the flat augmentation baseline uses the same total training data as the curriculum approach, since data volume matching matters for a fair comparison. And the claim about content-invariant features needs stronger support beyond just CKA and cosine similarity metrics.

Looking at what's actually working well: the external benchmarks are solid, the held-out encoding generalization test is well-designed, the compute normalization is reasonable, and the representation analysis provides mechanistic insight. The main concerns are moderate issues around seed count and statistical power, the distinction between flat augmentation and random ordering, the missing learned canonicalization baseline, and the deferred ECS ablation—all of which are fixable but worth addressing.

Now I'm weighing the severity of each gap against what reviewers at EMNLP would realistically push back on. The statistical power issue with only 3 seeds is the most significant, along with ensuring the co-evolutionary comparison is truly compute-matched and clarifying whether the learned canonicalization baseline is actually missing or just not emphasized. The incomplete thought about the distinction between approaches needs to be resolved before finalizing my assessment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4a2515c-83ea-49d6-a4c5-15a5eac6fb58",
  "isSidechain": false,
  "requestId": "req_011Cb6EzFN4YBE3HMMtBLk31",
  "type": "assistant",
  "uuid": "eaf2d75e-0bac-4cb9-8c6b-f80e68b886b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "031381c6-d0f3-4dbb-bfe2-0f8311bded45",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZtkPm9iCHjfsMzJqaB6VD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5070,
      "cache_read_input_tokens": 13279,
      "output_tokens": 5326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5070,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5326,
          "cache_read_input_tokens": 13279,
          "cache_creation_input_tokens": 5070,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5070
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

_source line 9 · 2026-05-16T12:26:02.342Z_

【状态】: 有缺陷待补救

---

【缺陷 1】
- 类别: 实验设计不足（统计效力）
- 问题: H1 声称用 paired t-test (p < 0.05) 验证 curriculum > random-order，但 curriculum 方法只有 3 seeds。3 个样本的 t-test 自由度为 2，统计功效极低——即使真实效应存在，也很难在 p<0.05 下拒绝零假设。更关键的是，curriculum 3 seeds vs. random-order 5 seeds 的不对称设计无法做标准 paired t-test（配对要求样本量相同）。这是一个审稿人几乎必然会挑战的统计设计缺陷。
- 严重度: 可补救
- 补救方案: (1) 将 curriculum 方法也跑 5 seeds，与 random-order 对齐，做 paired comparison（每对 seed 用相同 random initialization）；或者 (2) 若计算资源限制 seed 数量，改用 bootstrap confidence interval 或 Wilcoxon rank-sum test（非参数），不声称 paired t-test；(3) 在 timeline 中，Day 16 提到的 "full 5-seed curriculum if time permits" 应提升为 submission-critical，因为这是核心 claim H1 的统计基础。额外 2 runs × 8h = 16h GPU 在 4×A100 上完全可行。

【缺陷 2】
- 类别: baseline 不足或过时
- 问题: Proposal 明确论述了 "learned canonicalization (seq2seq decode → classify)" 作为现有防御的第二大类，并从理论上指出其缺陷（error propagation, new attack surface）。但实验中完全没有包含这类 baseline 的实证比较——只有 Deterministic-Decode + LlamaGuard-3（规则解码，非学习式）。审稿人会质疑：你声称比 learned canonicalization 更好，但没有实验证据。
- 严重度: 可补救
- 补救方案: 添加一个 learned decode-then-classify baseline。具体方案：(1) 用同规模模型（Qwen2.5-4B 或更小）fine-tune 一个 seq2seq decoder（input: encoded text, output: decoded plaintext），在相同训练编码类型上训练，然后将解码输出送入 LlamaGuard-3 分类。(2) 如果从头训练 canonicalizer 计算负担过重，可以使用 ALMA 或已有的 text normalization model 作为 proxy。(3) 最低成本替代：在 Discussion section 承认这是 limitation，但至少对 nested encoding 场景展示 deterministic decode 的 error propagation 曲线（随 nesting depth 增加，decode accuracy 如何衰减），间接支持论点。

【缺陷 3】
- 类别: compute 公平性问题
- 问题: 核心方法包含 co-evolutionary loop（GRPO attacker 12h + classifier curriculum training），而所有 baselines 只有 classifier 训练。Co-evolutionary 方法总 compute 明显超过 baselines。Proposal 声称 "same FLOPs" 但这只能指 classifier 部分的 FLOPs；attacker 的训练 FLOPs 和 oracle 调用是额外开销。H4 的 "co-evolution > static" 比较尤其需要澄清：如果把 co-evolution 的额外 compute 分配给 static baseline（如更多 epoch、更多 augmented data），static 是否仍逊色？
- 严重度: 可补救
- 补救方案: (1) 明确区分两层比较：H1-H3 的核心 claim 基于 static curriculum vs. baselines（compute 严格匹配），H4 是 bonus claim；(2) 对 H4，增加一个 "compute-matched static curriculum" 变体：把 co-evolutionary 额外消耗的 FLOPs 转化为 static curriculum 的 additional training steps 或 data augmentation rounds，证明 co-evolution 的优势不仅仅来自更多 compute；(3) 在 Table 中报告每个方法的 total training FLOPs（含 attacker 训练），让读者自行判断。

【缺陷 4】
- 类别: 实验设计不足（baseline 定义模糊）
- 问题: "Random-order training" 和 "Flat augmentation" 作为两个独立 baselines，但 proposal 未清晰定义二者区别。Random-order 是否指使用相同的 curriculum-staged data 但打乱顺序？Flat augmentation 是否指从所有编码类型中均匀采样而不分 stage？如果区别仅在于 data sampling strategy，需要明确；如果二者本质相同，则其中一个是冗余的。审稿人会追问 "your random-order and flat augmentation baselines seem identical."
- 严重度: 可补救
- 补救方案: 明确定义：(1) Random-order = 使用与 curriculum 完全相同的训练数据（含 co-evolutionary 生成或 static 数据），但呈现顺序完全随机化；(2) Flat augmentation = 对每个 base prompt，在每个 epoch 随机采样一种编码类型进行增强，不使用 ECS-ordered data generation，数据分布可能与 curriculum 不同。两者的关键区别应是：random-order 控制 data composition（isolates ordering effect），flat augmentation 控制 data generation strategy（different data distribution entirely）。在 methodology section 用一个对比表明确说明。

【缺陷 5】
- 类别: 评估方案缺陷（representation claim 证据链不完整）
- 问题: Proposal 的核心机制 claim 是 "content-invariant representations"（content clusters by meaning, not encoding type）。当前证据是 CKA + intra-prompt cosine similarity。但这些只能说明 same-content different-encoding 的表征更相似，不能直接证明 encoding information 被 disentangled out。一个模型可能同时保留 content 和 encoding 信息——只是 content 维度的 variance 更大。
- 严重度: 可补救
- 补救方案: 添加 linear probing experiment：(1) 在 curriculum-trained vs. random-order-trained 模型的 penultimate layer representations 上，分别训练两个 linear probe——一个预测 content category（harmful type），一个预测 encoding type。(2) Prediction: curriculum model 的 encoding-type probe accuracy 应显著低于 random-order model（encoding info 被丢弃），而 content-type probe accuracy 应更高或相当。这直接验证 "disentanglement" 而非仅仅 "similarity"。计算成本极低（linear probe 训练 < 5 min），可在 Day 10-11 的 representation analysis 阶段完成。

【缺陷 6】
- 类别: 评估方案缺陷（ECS 作为 contribution 的验证不足）
- 问题: ECS 被列为第二大 contribution，但其 component weight 的 ablation（"Full leave-one-out component ablation"）被推迟到 camera-ready。Submission 版本只有 pilot study justification + Spearman ρ 相关性。审稿人会质疑：如果 ECS 的 3 个 component 中某个 dominates（如 NestingDepth alone achieves ρ ≥ 0.65），那 ECS 作为 "formalized metric" 的增量贡献存疑。
- 严重度: 可补救
- 补救方案: 将 ECS component ablation 从 camera-ready 提升到 submission-critical。具体：(1) 计算 NestingDepth alone、CPT_Deviation alone、TokenizerPerplexity alone 分别与 classifier error 的 Spearman ρ；(2) 计算 leave-one-out（去掉每个 component）的 ρ 下降；(3) 这不需要重新训练模型，只需要在已有 evaluation data 上计算相关性——纯 inference/statistics 工作，< 2h。放在 Day 10-11 完成。

【缺陷 7】
- 类别: 可行性问题（timeline 紧张度）
- 问题: 16 天 timeline 中，Days 4-7 需要完成 11 runs（3 curriculum + 5 random + 3 flat），Days 8-9 再加 6 runs（3 reverse + co-evolutionary）+ decode pipeline。这假设所有 runs 一次成功，无需 hyperparameter tuning。实际操作中，第一轮 curriculum training 几乎必然需要 ECS threshold 调参（何时从 Stage 1 过渡到 Stage 2）、learning rate warm-up 调整等。如果 Day 4 的第一次 curriculum run 不收敛或 FPR 过高触发 rollback，整个 timeline 后移。
- 严重度: 可补救
- 补救方案: (1) Days 1-3 的 pilot phase 中增加 1 次 fast curriculum run（reduced data, 2h）用于验证 training dynamics 和 ECS threshold 的 rough range；(2) 为 Days 4-7 预留 1 天 buffer（可从 Day 13-14 的 camera-ready 工作中借）；(3) 如果 seed variance 大导致需要更多 runs，优先保证核心 H1 的 5-seed curriculum（最重要的统计 claim），其他 baselines 可接受 3 seeds。

---

**总结**：实验设计的整体框架是 solid 的（ablation 轴线合理、外部 benchmark 使用得当、held-out generalization 设计清晰、fallback plan 务实）。上述缺陷均为可补救的技术细节问题，不存在方向性致命缺陷。其中**缺陷 1（统计效力）**和**缺陷 5（probing experiment）**是审稿人最可能提出的 concern，建议优先处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eaf2d75e-0bac-4cb9-8c6b-f80e68b886b2",
  "isSidechain": false,
  "requestId": "req_011Cb6EzFN4YBE3HMMtBLk31",
  "type": "assistant",
  "uuid": "edc41caa-2497-44d6-8630-5465b46b8bfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "031381c6-d0f3-4dbb-bfe2-0f8311bded45",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZtkPm9iCHjfsMzJqaB6VD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5070,
      "cache_read_input_tokens": 13279,
      "output_tokens": 5326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5070,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5326,
          "cache_read_input_tokens": 13279,
          "cache_creation_input_tokens": 5070,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5070
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## Title  EncoGuard: Learning Content-Invariant Safety Features via Complexity-Structured Curriculum for Encoding-Based Attacks  ## Problem Statement  Encoding-based jailbreak attacks (base64, ROT13,…",
  "leafUuid": "edc41caa-2497-44d6-8630-5465b46b8bfc",
  "sessionId": "031381c6-d0f3-4dbb-bfe2-0f8311bded45"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "EncoGuard: Encoding-Based Attack Defense via Curriculum Learning",
  "sessionId": "031381c6-d0f3-4dbb-bfe2-0f8311bded45"
}
```

---
