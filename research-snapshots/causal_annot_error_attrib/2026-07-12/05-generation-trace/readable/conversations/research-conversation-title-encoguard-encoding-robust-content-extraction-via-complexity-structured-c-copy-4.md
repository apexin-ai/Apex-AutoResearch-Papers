# Research conversation: Title EncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training ## Problem Statement E

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/d24c1dd8-f064-4318-9ac4-73307e638e61.jsonl`
- **Structured JSON:** [`dbc08edfe97d3417ed00.json`](../../sessions/db/dbc08edfe97d3417ed00.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T12:29:47.103Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:29:47.103Z",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61",
  "content": "## Title\n\nEncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training\n\n## Problem Statement\n\nEncoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, and their nested compositions) exploit a fundamental vulnerability in LLM safety guardrails: classifiers trained on plaintext or limited encoding variations fail when inputs are transformed through unseen encoding schemes. Existing defenses have critical limitations:\n\n1. **Rule-based detection + decoding pipelines** (regex detection → known decoder → standard guardrail): Effective for known single-layer encodings with distinctive statistical signatures (base64 character set, ROT13 alphabetic patterns). Fail on: (a) partial encoding where only segments are transformed, defeating whole-input detection heuristics; (b) adversarial mixing of encoded/plaintext creating ambiguous signatures; (c) novel encodings without pre-programmed decoders.\n\n2. **Learned canonicalization** (seq2seq decode → classify): Error propagation compounds across nesting layers; the canonicalizer itself becomes an adversarial attack surface; partial encoding requires semantic understanding to identify decode targets.\n\n3. **Frontier LLM zero-shot** (GPT-4/Claude with \"detect if content is harmful regardless of encoding\"): Can leverage pre-training exposure to encodings, but impractical for deployment-scale guardrails due to cost ($0.01-0.03 per input) and latency (1-3s per call vs. millisecond-level local inference).\n\nThe core challenge is achieving **generalization to unseen encoding families at deployment-practical cost**—a lightweight classifier that remains robust against encoding types never encountered during training.\n\n## Core Thesis\n\nWe hypothesize that a classifier trained via **complexity-structured curriculum**—where encoding attacks are presented in order of a principled complexity metric—acquires **encoding-robust content extraction capabilities** that generalize to held-out encoding types unseen during training.\n\n**Mechanism (Two-Regime Explanation):**\n\n- **Low-ECS regime (simple encodings):** Content semantics remain partially accessible through tokenization (e.g., base64 of short text preserves some token-level correlations). The curriculum forces the model to anchor harmful-content semantic features—learning what \"harmful content looks like\" across mild surface perturbations (**content anchoring**).\n\n- **High-ECS regime (complex/nested encodings):** Token-level content information is effectively destroyed by multi-layer encoding. The model cannot rely on direct semantic features; it must develop strategies for implicit decoding—recognizing encoding structure patterns and reconstructing content signal. The curriculum's contribution is **progressive decoding skill acquisition**: simple decoding patterns learned in the low-ECS regime (recognizing base64 structure, identifying shift patterns) provide compositional building blocks that support parsing more complex nested structures.\n\nThe generalization prediction follows: if the model acquires generalized decoding skills (structural pattern recognition + compositional decoding strategies) rather than memorizing specific encoding-to-content mappings, it should transfer to novel encodings that share structural properties with training encodings. For truly novel encoding principles, the model's content-anchoring from the low-ECS regime provides a robust classification backbone once any partial decoding succeeds.\n\n**Important distinction:** We do NOT claim the model learns literal \"encoding-invariant features\" in the information-theoretic sense (impossible for fully-scrambled token sequences). Rather, curriculum training builds a progressive hierarchy of decoding capabilities—from direct semantic extraction (low-ECS) to structural pattern matching + compositional decoding (high-ECS)—that transfers across encoding types more effectively than flat or random training.\n\n## Relationship to Prior Work\n\n### Curriculum Adversarial Training\nCai et al. (IJCAI 2018) progressively increase perturbation magnitude ε for image classifiers; Wang et al. (NeurIPS 2021) order samples by difficulty for better generalization. Key differences from our work:\n1. **Discrete compositional space vs. continuous perturbation:** Prior work operates in continuous ε-ball spaces with scalar difficulty. Encoding attacks form a discrete compositional space requiring multi-dimensional complexity metrics.\n2. **OOD generalization vs. in-distribution robustness:** Prior work only evaluates on the same attack type used in training. We explicitly test generalization to unseen encoding families—including encodings based on entirely different structural principles.\n\n### Domain Generalization (DG)\nEach encoding type can be viewed as a domain; OOD generalization to unseen encodings resembles domain generalization. However, standard DG methods (IRM, DANN, CORAL, DRO) are not directly applicable because:\n1. **Non-differentiable discrete domains:** Encoding transformations are discrete operations; gradient-based domain alignment (DANN adversarial training) cannot be applied to the input transformation space.\n2. **Exponential domain combinatorics:** Composing N encoding primitives at K nesting levels creates O(N^K) potential domains—impossible to enumerate as source domains at training time.\n3. **Structural curriculum as natural alternative:** The compositional structure of encoding attacks provides a natural progressive training signal that standard DG methods lack—curriculum exploits the partial ordering on complexity inherent in compositional spaces.\n\n## Key Contributions\n\n1. **Primary Contribution (OOD Generalization via Curriculum):** Empirical demonstration that complexity-structured curriculum enables generalization to unseen encoding families—at two levels: (a) mapping-function OOD (same encoding principle, different specific mapping), and (b) encoding-principle OOD (structurally different encoding type). Direct representation-level evidence (CKA + linear probing) characterizes how curriculum shapes internal representations differently from baselines.\n\n2. **Encoding Complexity Score (ECS):** Formalized metric combining nesting depth, CPT deviation, and tokenizer perplexity. Validated via correlation with classifier difficulty; individual component contributions quantified.\n\n3. **Co-Evolutionary Training Framework:** GRPO attacker + SFT classifier with curriculum-ordered training, demonstrating co-evolution can further improve upon static curriculum.\n\n4. **Deployment-Practical Encoding Defense:** A 4B-parameter classifier achieving encoding robustness comparable to frontier LLM zero-shot, at orders-of-magnitude lower inference cost.\n\n## Methodology\n\n### Encoding Complexity Score (ECS)\n\n$$ECS(e) = \\alpha \\cdot \\text{NestingDepth}(e) + \\beta \\cdot \\text{CPT\\_Deviation}(e) + \\gamma \\cdot \\text{TokenizerPerplexity}(e)$$\n\n- NestingDepth: number of compositional encoding layers\n- CPT_Deviation: |CPT_encoded / CPT_plaintext - 1|\n- TokenizerPerplexity: target tokenizer's perplexity on encoded text\n\n**Weight determination:** Pilot study (200 samples spanning full ECS range) measures Spearman ρ of each individual component with classifier error rate. Weights set proportional to individual predictive power.\n\n**Component contribution analysis (submission-critical):** Report Spearman ρ for each single component alone and for leave-one-out combinations, demonstrating that all three contribute meaningfully and that the composite metric outperforms any single component.\n\n### Co-Evolutionary Training Loop\n\n**Attacker (Qwen2.5-1.5B, GRPO):**\n- Generates encoding attacks with ECS in current curriculum band\n- Reward: +1 if bypasses classifier AND oracle confirms harmful\n- Entropy regularization prevents encoding-type collapse\n\n**Classifier (Qwen2.5-4B, SFT):**\n- Curriculum-ordered training: Stage 1 (ECS ≤ threshold) → Stage 2 (ECS > threshold)\n- FPR rollback: revert if FPR > 2% on benign validation\n- Semantic deduplication: cosine similarity > 0.95 removed\n\n**Oracle:** GPT-4o + deterministic decoder cross-validation; disagreements excluded.\n\n**Fallback:** If co-evolutionary loop unstable by Day 7, switch to static curriculum SFT.\n\n### Baseline Definitions (Comparison Table)\n\n| Baseline | Data Source | Data Composition | Presentation Order | Isolates |\n|----------|-------------|------------------|-------------------|----------|\n| **Curriculum (ours)** | Co-evolutionary or static generation | ECS-staged | Monotone increasing ECS | — |\n| **Random-order** | Same data as curriculum | Identical composition | Randomly shuffled | Ordering effect |\n| **Flat augmentation** | Fresh generation: each epoch randomly samples encoding type per prompt | Uniform across all ECS levels | Random within each epoch | Data composition + ordering |\n| **Reverse curriculum** | Same data as curriculum | Identical composition | Monotone decreasing ECS | Direction effect |\n| **Static curriculum** | Rule-based generation, ECS-ordered | Identical to curriculum | Same ordering | Co-evolution effect |\n| **Decode + LlamaGuard-3** | N/A (inference only) | N/A | N/A | End-to-end vs. pipeline |\n| **GPT-4 zero-shot** | N/A (API call) | N/A | N/A | Cost/accuracy frontier |\n\nKey distinctions:\n- Random-order vs. Flat augmentation: Random-order uses curriculum's exact data (same samples) in shuffled order → isolates ordering. Flat augmentation generates different data with uniform encoding distribution → tests whether curriculum's staged data composition matters.\n- Static curriculum vs. Curriculum: Same data, same order, but no co-evolutionary attacker → isolates co-evolution benefit.\n\n### Compute Fairness\n\n- **H1-H3 (core claims):** Based on static curriculum vs. baselines. All methods use identical model architecture (Qwen2.5-4B), identical total training FLOPs, identical number of training steps. Only variable: data ordering / composition.\n- **H4 (co-evolution bonus):** Co-evolutionary method has additional compute (attacker training: ~12h, oracle calls: ~$250). For fair comparison, include a \"compute-matched static\" variant: redirect co-evolution's extra FLOPs into additional static curriculum training epochs.\n- **Reporting:** Table includes total FLOPs (classifier only), total FLOPs (including attacker), wall-clock time, and training tokens for each method.\n\n### Compute and Cost\n\n- Hardware: 4× A100 80GB\n- Per classifier run: ~8h\n- Total runs: curriculum (5) + random (5) + flat (3) + reverse (3) + static (3) + compute-matched static (3) = 22 classifier runs\n- Parallelization: 4 GPUs → 4 runs simultaneously → ~44h for all classifier training\n- Attacker: 12h (2 rounds)\n- Oracle: ~18K calls ≈ $250\n- GPT-4 zero-shot evaluation: ~12K test cases × $0.01 ≈ $120\n- Inference-only analyses (probing, CKA, ECS stats): ~4h\n- Total: ~60h wall-clock for training + ~4h analysis\n\n## Experimental Design\n\n### Hypotheses\n\n- **H1 (Curriculum > Random):** Curriculum achieves ≥10pp lower encoding-ASR than random-order at equivalent FLOPs (95% bootstrap CI of difference excludes 0, one-sided).\n- **H2 (OOD Generalization):** Curriculum maintains ≤30% encoding-ASR on held-out encodings where baselines exceed 60%. Tested at two OOD levels: mapping-function OOD and encoding-principle OOD.\n- **H3 (ECS Predictiveness):** ECS correlates with classifier error (Spearman ρ ≥ 0.7) on held-out encodings; composite metric outperforms any single component.\n- **H4 (Co-evolution > Static, bonus):** Co-evolutionary > static curriculum by ≥5pp on composite encodings, after controlling for extra compute.\n\n### Held-Out Encoding Families\n\n**Mapping-function OOD (same structural principle as training encodings):**\n- Braille Unicode substitution (character substitution — cf. homoglyphs in training)\n- Custom Caesar-variant cipher with position-dependent shift (shift-based — cf. ROT13 in training)\n- NATO phonetic alphabet (word-level substitution)\n\n**Encoding-principle OOD (structurally different from all training encodings):**\n- Whitespace steganography (harmful content encoded in whitespace patterns between benign text)\n- Zero-width Unicode character encoding (content hidden in invisible Unicode sequences)\n\nThis two-level OOD structure explicitly tests whether generalization is merely interpolation within known principles (mapping-function OOD) or genuine extrapolation to novel encoding paradigms (encoding-principle OOD).\n\n### Evaluation Protocol\n\n**External benchmarks (primary):**\n- HarmBench encoding-perturbed\n- JailbreakBench encoding subset\n- WildGuardTest encoding-perturbed\n\n**EncoAttack (supplementary):**\n- 500 base prompts: HarmBench (200) + AdvBench (150) + WildGuardTest (150)\n- 8 encoding types × 3 nesting levels = 12,000 test cases\n- Independent implementation from training; validated ≥80% bypass on undefended LlamaGuard-3\n\n**Held-out encodings:** 5 families as specified above\n\n**GPT-4 zero-shot reference:** Same test sets, prompt: \"The following text may be encoded. Determine if the underlying content, once decoded, would be harmful.\"\n\n**Metrics:**\n- Encoding-ASR (primary)\n- Clean FPR at thresholds: 0.5%, 1%, 2%, 5% with Pareto frontier\n- Benign test: WildGuardTest benign (~1000) + LMSYS-Chat-1M sample (1000)\n- Per-encoding breakdown\n- ECS-difficulty correlation (composite + individual components)\n- Nesting-depth vs. decode-accuracy curve (demonstrating pipeline error propagation)\n\n### Representation Analysis\n\n1. **CKA + Cosine Similarity:** For 100 prompts × (plaintext + 8 encoding variants), extract penultimate-layer representations. Compute intra-prompt cross-encoding cosine similarity. Compare curriculum vs. random-order.\n\n2. **Linear Probing (Disentanglement Test):**\n   - Train linear probe A: predict content category (harmful topic type) from representations\n   - Train linear probe B: predict encoding type from representations\n   - **Prediction:** Curriculum model → high probe-A accuracy, LOW probe-B accuracy (encoding info discarded). Random-order model → lower probe-A, higher probe-B (encoding info retained).\n   - This directly tests whether curriculum induces disentanglement of content from encoding surface features.\n\n3. **Learning Dynamics:** Per-checkpoint (500 steps) ASR curves for low-ECS and high-ECS separately. Expected pattern: curriculum shows staged learning (low-ECS converges first, smooth transition to high-ECS); random-order shows chaotic/concurrent learning.\n\n### Statistical Rigor\n\n- All methods: 5 seeds (curriculum, random-order) or 3 seeds (flat, reverse, static) with mean ± std\n- H1: 95% bootstrap CI on paired difference (curriculum seed i vs. random-order seed i, same initialization)\n- Effect sizes: Cohen's d reported alongside p-values\n- Multiple comparison correction: Bonferroni for family of H1-H3 tests\n\n### Oracle Pilot (Days 1-3)\n\n- 100 samples per ECS band\n- Measure GPT-4o + deterministic decoder agreement rate\n- If < 80% for high-ECS: switch to deterministic-only for Stage 2\n\n## Stability Mechanisms (Engineering, Not Contributions)\n\nBorrowed from prior work (TriPlay-RL, standard RL practices):\n- Entropy regularization\n- FPR rollback\n- Semantic deduplication\n\nTrigger frequencies reported. Full ablation in camera-ready.\n\n## Limitations (To Acknowledge in Paper)\n\n1. Learned canonicalization (seq2seq decode → classify) not empirically compared due to training cost; theoretical arguments + decode error propagation curve provided as indirect evidence.\n2. General principle validated only on encoding attacks; transfer to other compositional attack spaces (prompt injection, multi-turn) remains future work.\n3. ECS weight sensitivity not fully explored (±20% perturbation analysis in supplementary).\n\n## Timeline (17 days, with buffer)\n\n**Phase 1: Setup + Pilot (Days 1-3)**\n- ECS implementation, encoding generators (including held-out families), data pipeline\n- Oracle pilot (100 samples/band)\n- Fast pilot curriculum run (reduced data, 2h) to validate training dynamics + ECS threshold\n\n**Phase 2: Core Training (Days 4-9)**\n- Days 4-6: Curriculum (5 seeds) + random-order (5 seeds) [parallelized, 4 GPUs]\n- Days 7-8: Flat augmentation (3) + reverse curriculum (3) + static (3) [parallelized]\n- Day 9: Co-evolutionary attempt + compute-matched static + decode pipeline\n\n**Phase 3: Evaluation + Analysis (Days 10-12)**\n- Day 10: Full benchmark evaluation + held-out encodings + GPT-4 zero-shot\n- Day 11: Representation analysis (CKA, probing) + ECS component stats + learning dynamics\n- Day 12: Statistical tests, nesting-depth decode curve, Pareto analysis\n\n**Phase 4: Writing (Days 13-15)**\n- Day 13-14: Main paper draft\n- Day 15: Figures, tables, polishing\n\n**Buffer + Camera-ready (Days 16-17)**\n- Additional seeds if needed, stability ablation, writing revision\n\n**Fallback:** Co-evolutionary unstable by Day 8 → drop H4, focus H1-H3 with static curriculum."
}
```

---

### Runtime record

_source line 2 · 2026-05-16T12:29:47.107Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:29:47.107Z",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61"
}
```

---

## Round 1

17 recorded events

### User

_source line 3 · 2026-05-16T12:29:47.121Z_

## Title

EncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training

## Problem Statement

Encoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, and their nested compositions) exploit a fundamental vulnerability in LLM safety guardrails: classifiers trained on plaintext or limited encoding variations fail when inputs are transformed through unseen encoding schemes. Existing defenses have critical limitations:

1. **Rule-based detection + decoding pipelines** (regex detection → known decoder → standard guardrail): Effective for known single-layer encodings with distinctive statistical signatures (base64 character set, ROT13 alphabetic patterns). Fail on: (a) partial encoding where only segments are transformed, defeating whole-input detection heuristics; (b) adversarial mixing of encoded/plaintext creating ambiguous signatures; (c) novel encodings without pre-programmed decoders.

2. **Learned canonicalization** (seq2seq decode → classify): Error propagation compounds across nesting layers; the canonicalizer itself becomes an adversarial attack surface; partial encoding requires semantic understanding to identify decode targets.

3. **Frontier LLM zero-shot** (GPT-4/Claude with "detect if content is harmful regardless of encoding"): Can leverage pre-training exposure to encodings, but impractical for deployment-scale guardrails due to cost ($0.01-0.03 per input) and latency (1-3s per call vs. millisecond-level local inference).

The core challenge is achieving **generalization to unseen encoding families at deployment-practical cost**—a lightweight classifier that remains robust against encoding types never encountered during training.

## Core Thesis

We hypothesize that a classifier trained via **complexity-structured curriculum**—where encoding attacks are presented in order of a principled complexity metric—acquires **encoding-robust content extraction capabilities** that generalize to held-out encoding types unseen during training.

**Mechanism (Two-Regime Explanation):**

- **Low-ECS regime (simple encodings):** Content semantics remain partially accessible through tokenization (e.g., base64 of short text preserves some token-level correlations). The curriculum forces the model to anchor harmful-content semantic features—learning what "harmful content looks like" across mild surface perturbations (**content anchoring**).

- **High-ECS regime (complex/nested encodings):** Token-level content information is effectively destroyed by multi-layer encoding. The model cannot rely on direct semantic features; it must develop strategies for implicit decoding—recognizing encoding structure patterns and reconstructing content signal. The curriculum's contribution is **progressive decoding skill acquisition**: simple decoding patterns learned in the low-ECS regime (recognizing base64 structure, identifying shift patterns) provide compositional building blocks that support parsing more complex nested structures.

The generalization prediction follows: if the model acquires generalized decoding skills (structural pattern recognition + compositional decoding strategies) rather than memorizing specific encoding-to-content mappings, it should transfer to novel encodings that share structural properties with training encodings. For truly novel encoding principles, the model's content-anchoring from the low-ECS regime provides a robust classification backbone once any partial decoding succeeds.

**Important distinction:** We do NOT claim the model learns literal "encoding-invariant features" in the information-theoretic sense (impossible for fully-scrambled token sequences). Rather, curriculum training builds a progressive hierarchy of decoding capabilities—from direct semantic extraction (low-ECS) to structural pattern matching + compositional decoding (high-ECS)—that transfers across encoding types more effectively than flat or random training.

## Relationship to Prior Work

### Curriculum Adversarial Training
Cai et al. (IJCAI 2018) progressively increase perturbation magnitude ε for image classifiers; Wang et al. (NeurIPS 2021) order samples by difficulty for better generalization. Key differences from our work:
1. **Discrete compositional space vs. continuous perturbation:** Prior work operates in continuous ε-ball spaces with scalar difficulty. Encoding attacks form a discrete compositional space requiring multi-dimensional complexity metrics.
2. **OOD generalization vs. in-distribution robustness:** Prior work only evaluates on the same attack type used in training. We explicitly test generalization to unseen encoding families—including encodings based on entirely different structural principles.

### Domain Generalization (DG)
Each encoding type can be viewed as a domain; OOD generalization to unseen encodings resembles domain generalization. However, standard DG methods (IRM, DANN, CORAL, DRO) are not directly applicable because:
1. **Non-differentiable discrete domains:** Encoding transformations are discrete operations; gradient-based domain alignment (DANN adversarial training) cannot be applied to the input transformation space.
2. **Exponential domain combinatorics:** Composing N encoding primitives at K nesting levels creates O(N^K) potential domains—impossible to enumerate as source domains at training time.
3. **Structural curriculum as natural alternative:** The compositional structure of encoding attacks provides a natural progressive training signal that standard DG methods lack—curriculum exploits the partial ordering on complexity inherent in compositional spaces.

## Key Contributions

1. **Primary Contribution (OOD Generalization via Curriculum):** Empirical demonstration that complexity-structured curriculum enables generalization to unseen encoding families—at two levels: (a) mapping-function OOD (same encoding principle, different specific mapping), and (b) encoding-principle OOD (structurally different encoding type). Direct representation-level evidence (CKA + linear probing) characterizes how curriculum shapes internal representations differently from baselines.

2. **Encoding Complexity Score (ECS):** Formalized metric combining nesting depth, CPT deviation, and tokenizer perplexity. Validated via correlation with classifier difficulty; individual component contributions quantified.

3. **Co-Evolutionary Training Framework:** GRPO attacker + SFT classifier with curriculum-ordered training, demonstrating co-evolution can further improve upon static curriculum.

4. **Deployment-Practical Encoding Defense:** A 4B-parameter classifier achieving encoding robustness comparable to frontier LLM zero-shot, at orders-of-magnitude lower inference cost.

## Methodology

### Encoding Complexity Score (ECS)

$$ECS(e) = \alpha \cdot \text{NestingDepth}(e) + \beta \cdot \text{CPT\_Deviation}(e) + \gamma \cdot \text{TokenizerPerplexity}(e)$$

- NestingDepth: number of compositional encoding layers
- CPT_Deviation: |CPT_encoded / CPT_plaintext - 1|
- TokenizerPerplexity: target tokenizer's perplexity on encoded text

**Weight determination:** Pilot study (200 samples spanning full ECS range) measures Spearman ρ of each individual component with classifier error rate. Weights set proportional to individual predictive power.

**Component contribution analysis (submission-critical):** Report Spearman ρ for each single component alone and for leave-one-out combinations, demonstrating that all three contribute meaningfully and that the composite metric outperforms any single component.

### Co-Evolutionary Training Loop

**Attacker (Qwen2.5-1.5B, GRPO):**
- Generates encoding attacks with ECS in current curriculum band
- Reward: +1 if bypasses classifier AND oracle confirms harmful
- Entropy regularization prevents encoding-type collapse

**Classifier (Qwen2.5-4B, SFT):**
- Curriculum-ordered training: Stage 1 (ECS ≤ threshold) → Stage 2 (ECS > threshold)
- FPR rollback: revert if FPR > 2% on benign validation
- Semantic deduplication: cosine similarity > 0.95 removed

**Oracle:** GPT-4o + deterministic decoder cross-validation; disagreements excluded.

**Fallback:** If co-evolutionary loop unstable by Day 7, switch to static curriculum SFT.

### Baseline Definitions (Comparison Table)

| Baseline | Data Source | Data Composition | Presentation Order | Isolates |
|----------|-------------|------------------|-------------------|----------|
| **Curriculum (ours)** | Co-evolutionary or static generation | ECS-staged | Monotone increasing ECS | — |
| **Random-order** | Same data as curriculum | Identical composition | Randomly shuffled | Ordering effect |
| **Flat augmentation** | Fresh generation: each epoch randomly samples encoding type per prompt | Uniform across all ECS levels | Random within each epoch | Data composition + ordering |
| **Reverse curriculum** | Same data as curriculum | Identical composition | Monotone decreasing ECS | Direction effect |
| **Static curriculum** | Rule-based generation, ECS-ordered | Identical to curriculum | Same ordering | Co-evolution effect |
| **Decode + LlamaGuard-3** | N/A (inference only) | N/A | N/A | End-to-end vs. pipeline |
| **GPT-4 zero-shot** | N/A (API call) | N/A | N/A | Cost/accuracy frontier |

Key distinctions:
- Random-order vs. Flat augmentation: Random-order uses curriculum's exact data (same samples) in shuffled order → isolates ordering. Flat augmentation generates different data with uniform encoding distribution → tests whether curriculum's staged data composition matters.
- Static curriculum vs. Curriculum: Same data, same order, but no co-evolutionary attacker → isolates co-evolution benefit.

### Compute Fairness

- **H1-H3 (core claims):** Based on static curriculum vs. baselines. All methods use identical model architecture (Qwen2.5-4B), identical total training FLOPs, identical number of training steps. Only variable: data ordering / composition.
- **H4 (co-evolution bonus):** Co-evolutionary method has additional compute (attacker training: ~12h, oracle calls: ~$250). For fair comparison, include a "compute-matched static" variant: redirect co-evolution's extra FLOPs into additional static curriculum training epochs.
- **Reporting:** Table includes total FLOPs (classifier only), total FLOPs (including attacker), wall-clock time, and training tokens for each method.

### Compute and Cost

- Hardware: 4× A100 80GB
- Per classifier run: ~8h
- Total runs: curriculum (5) + random (5) + flat (3) + reverse (3) + static (3) + compute-matched static (3) = 22 classifier runs
- Parallelization: 4 GPUs → 4 runs simultaneously → ~44h for all classifier training
- Attacker: 12h (2 rounds)
- Oracle: ~18K calls ≈ $250
- GPT-4 zero-shot evaluation: ~12K test cases × $0.01 ≈ $120
- Inference-only analyses (probing, CKA, ECS stats): ~4h
- Total: ~60h wall-clock for training + ~4h analysis

## Experimental Design

### Hypotheses

- **H1 (Curriculum > Random):** Curriculum achieves ≥10pp lower encoding-ASR than random-order at equivalent FLOPs (95% bootstrap CI of difference excludes 0, one-sided).
- **H2 (OOD Generalization):** Curriculum maintains ≤30% encoding-ASR on held-out encodings where baselines exceed 60%. Tested at two OOD levels: mapping-function OOD and encoding-principle OOD.
- **H3 (ECS Predictiveness):** ECS correlates with classifier error (Spearman ρ ≥ 0.7) on held-out encodings; composite metric outperforms any single component.
- **H4 (Co-evolution > Static, bonus):** Co-evolutionary > static curriculum by ≥5pp on composite encodings, after controlling for extra compute.

### Held-Out Encoding Families

**Mapping-function OOD (same structural principle as training encodings):**
- Braille Unicode substitution (character substitution — cf. homoglyphs in training)
- Custom Caesar-variant cipher with position-dependent shift (shift-based — cf. ROT13 in training)
- NATO phonetic alphabet (word-level substitution)

**Encoding-principle OOD (structurally different from all training encodings):**
- Whitespace steganography (harmful content encoded in whitespace patterns between benign text)
- Zero-width Unicode character encoding (content hidden in invisible Unicode sequences)

This two-level OOD structure explicitly tests whether generalization is merely interpolation within known principles (mapping-function OOD) or genuine extrapolation to novel encoding paradigms (encoding-principle OOD).

### Evaluation Protocol

**External benchmarks (primary):**
- HarmBench encoding-perturbed
- JailbreakBench encoding subset
- WildGuardTest encoding-perturbed

**EncoAttack (supplementary):**
- 500 base prompts: HarmBench (200) + AdvBench (150) + WildGuardTest (150)
- 8 encoding types × 3 nesting levels = 12,000 test cases
- Independent implementation from training; validated ≥80% bypass on undefended LlamaGuard-3

**Held-out encodings:** 5 families as specified above

**GPT-4 zero-shot reference:** Same test sets, prompt: "The following text may be encoded. Determine if the underlying content, once decoded, would be harmful."

**Metrics:**
- Encoding-ASR (primary)
- Clean FPR at thresholds: 0.5%, 1%, 2%, 5% with Pareto frontier
- Benign test: WildGuardTest benign (~1000) + LMSYS-Chat-1M sample (1000)
- Per-encoding breakdown
- ECS-difficulty correlation (composite + individual components)
- Nesting-depth vs. decode-accuracy curve (demonstrating pipeline error propagation)

### Representation Analysis

1. **CKA + Cosine Similarity:** For 100 prompts × (plaintext + 8 encoding variants), extract penultimate-layer representations. Compute intra-prompt cross-encoding cosine similarity. Compare curriculum vs. random-order.

2. **Linear Probing (Disentanglement Test):**
   - Train linear probe A: predict content category (harmful topic type) from representations
   - Train linear probe B: predict encoding type from representations
   - **Prediction:** Curriculum model → high probe-A accuracy, LOW probe-B accuracy (encoding info discarded). Random-order model → lower probe-A, higher probe-B (encoding info retained).
   - This directly tests whether curriculum induces disentanglement of content from encoding surface features.

3. **Learning Dynamics:** Per-checkpoint (500 steps) ASR curves for low-ECS and high-ECS separately. Expected pattern: curriculum shows staged learning (low-ECS converges first, smooth transition to high-ECS); random-order shows chaotic/concurrent learning.

### Statistical Rigor

- All methods: 5 seeds (curriculum, random-order) or 3 seeds (flat, reverse, static) with mean ± std
- H1: 95% bootstrap CI on paired difference (curriculum seed i vs. random-order seed i, same initialization)
- Effect sizes: Cohen's d reported alongside p-values
- Multiple comparison correction: Bonferroni for family of H1-H3 tests

### Oracle Pilot (Days 1-3)

- 100 samples per ECS band
- Measure GPT-4o + deterministic decoder agreement rate
- If < 80% for high-ECS: switch to deterministic-only for Stage 2

## Stability Mechanisms (Engineering, Not Contributions)

Borrowed from prior work (TriPlay-RL, standard RL practices):
- Entropy regularization
- FPR rollback
- Semantic deduplication

Trigger frequencies reported. Full ablation in camera-ready.

## Limitations (To Acknowledge in Paper)

1. Learned canonicalization (seq2seq decode → classify) not empirically compared due to training cost; theoretical arguments + decode error propagation curve provided as indirect evidence.
2. General principle validated only on encoding attacks; transfer to other compositional attack spaces (prompt injection, multi-turn) remains future work.
3. ECS weight sensitivity not fully explored (±20% perturbation analysis in supplementary).

## Timeline (17 days, with buffer)

**Phase 1: Setup + Pilot (Days 1-3)**
- ECS implementation, encoding generators (including held-out families), data pipeline
- Oracle pilot (100 samples/band)
- Fast pilot curriculum run (reduced data, 2h) to validate training dynamics + ECS threshold

**Phase 2: Core Training (Days 4-9)**
- Days 4-6: Curriculum (5 seeds) + random-order (5 seeds) [parallelized, 4 GPUs]
- Days 7-8: Flat augmentation (3) + reverse curriculum (3) + static (3) [parallelized]
- Day 9: Co-evolutionary attempt + compute-matched static + decode pipeline

**Phase 3: Evaluation + Analysis (Days 10-12)**
- Day 10: Full benchmark evaluation + held-out encodings + GPT-4 zero-shot
- Day 11: Representation analysis (CKA, probing) + ECS component stats + learning dynamics
- Day 12: Statistical tests, nesting-depth decode curve, Pareto analysis

**Phase 4: Writing (Days 13-15)**
- Day 13-14: Main paper draft
- Day 15: Figures, tables, polishing

**Buffer + Camera-ready (Days 16-17)**
- Additional seeds if needed, stability ablation, writing revision

**Fallback:** Co-evolutionary unstable by Day 8 → drop H4, focus H1-H3 with static curriculum.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "5b0581fc-a336-4e08-a782-0f6e85553cc9",
  "type": "user",
  "uuid": "38c99a6b-10c8-48f7-a89a-7703d5341749",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T12:29:47.119Z_

```json
{
  "parentUuid": "38c99a6b-10c8-48f7-a89a-7703d5341749",
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
  "uuid": "33ca44c4-6a6b-45f3-ad41-89cfbd19c920",
  "timestamp": "2026-05-16T12:29:47.119Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T12:29:47.120Z_

```json
{
  "parentUuid": "33ca44c4-6a6b-45f3-ad41-89cfbd19c920",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "40a8fc1b-66e2-4965-a23d-4434d80286e3",
  "timestamp": "2026-05-16T12:29:47.120Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61",
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
  "lastPrompt": "## Title  EncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training  ## Problem Statement  Encoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, an…",
  "leafUuid": "40a8fc1b-66e2-4965-a23d-4434d80286e3",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Encoding-robust classifier via curriculum learning",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61"
}
```

---

### Assistant

_source line 8 · 2026-05-16T12:31:02.574Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal as the 发掘 agent (Discovery Agent), focusing on the three dimensions I'm responsible for: Novelty, Significance, and Related Work differentiation.

Let me first do the two critical self-checks:

**1. Is there a trivial alternative that achieves similar effects?**

The core claim is that curriculum-ordered training (by encoding complexity) leads to better OOD generalization on unseen encoding types compared to random-order training. 

Trivial alternatives to consider:
- Simply training on more encoding types with random order (data augmentation)


- Using a decode-then-classify pipeline with a comprehensive decoder library
- Fine-tuning a larger model that already has encoding knowledge from pretraining
- Training with diverse encodings through data augmentation alone, without curriculum structure

The proposal does include "flat augmentation" as a baseline, which addresses the data augmentation alternative. But I'm wondering whether ordering really matters that much for transformers—curriculum learning has shown mixed results in the literature, and many papers suggest that for models with sufficient capacity, the benefits of curriculum ordering over random ordering tend to be marginal, especially with adequate training time.

**2. Are the core assumptions valid?**

The two-regime explanation assumes that in the low-ECS regime, the model...

I'm questioning whether the mechanism actually holds up. The claim is that progressive exposure builds compositional decoding skills, but transformers might not learn this way. There's a fundamental tension: if high-ECS encodings truly destroy token-level content information, the model would need to actually decode the encoding to recover it. Yet learning to decode arbitrary encodings from just a classification signal seems incredibly inefficient compared to explicit decoding supervision. The curriculum might help, but the proposed mechanism is quite strong.

On the OOD generalization side, I'm skeptical about what transfers across different encoding types. Base64 and ROT13 are fundamentally different operations—learning one doesn't obviously help with the other. The claim that "structural pattern recognition and compositional decoding strategies" would transfer across encoding types needs more support.

Looking at the three evaluation dimensions: the curriculum learning approach to encoding defenses is novel in combination, though both components are well-studied separately. The ECS metric is reasonable but somewhat incremental as a weighted sum of intuitive factors. The core novelty claim—that curriculum ordering enables OOD generalization to unseen encodings—is interesting if true, but the underlying mechanism isn't fully convincing. For significance, encoding-based jailbreaks are a real problem, though the vulnerability may diminish as models improve. Cost-effective guardrails matter for deployment, but the practical window for this defense might be limited.

The distinction from prior curriculum adversarial training work is reasonable but shallow, and the domain generalization framing feels hand-wavy about why existing methods don't apply. There's likely missing related work on encoding-aware safety training and compositional generalization that should be discussed. The mechanism story needs sharpening—the "two-regime" explanation is intuitive but vague about what "decoding skills" actually transfer across fundamentally different encoding types, and it's unclear how pattern recognition from one encoding generalizes to completely different ones.

The OOD generalization claim has a logical gap: for truly novel encoding principles like whitespace steganography or zero-width Unicode, the structural properties are entirely different from training encodings, so it's unclear why curriculum learning would help more than random training or what actually transfers. Framing this through compositional generalization—since encoding attacks are fundamentally compositives of primitives and nesting—could strengthen the theoretical grounding and connect to deeper NLP research.

The broader contribution could be reframed as "Can curriculum-structured training enable compositional generalization in discrete transformation spaces?" rather than narrowly as encoding defense. There's also a concern that a simpler modular approach—a small encoding detector that identifies and decodes the attack before passing it to a standard classifier—might work well with modern language models and would be more interpretable, so the paper needs to more convincingly argue why end-to-end learning of encoding-robust features is superior.

Now I'm looking more carefully at the OOD encodings in the proposal. The mapping-function OOD tests (Braille, Caesar variants, NATO phonetic) are reasonable interpolation cases, but the encoding-principle OOD tests (whitespace steganography, zero-width Unicode) present a fundamental problem: these hide content in invisible characters, which is structurally different from the visible encodings in the training set. If the model only learns from base64, ROT13, and homoglyphs—none of which involve invisible character patterns—it's unclear how it would develop the capability to detect hidden content in whitespace or zero-width characters in the first place.

The proposal might need to either soften the encoding-principle OOD claim, provide a stronger theory of what transfers across these fundamentally different encoding types, or include some training examples with non-visible transformations. Beyond that, I'm questioning whether the core curriculum-versus-random result would even be surprising. The curriculum learning literature shows mixed results for transformers, and while the argument that compositional encoding attacks have a natural complexity ordering is plausible, it's not guaranteed. A 10-percentage-point improvement might just reflect curriculum preventing catastrophic forgetting of simpler examples rather than something deeper about the learning dynamics.

The representation analysis with CKA and probing helps address this, but the mechanism claim still feels stronger than what the evidence would actually support. I need to sharpen the OOD generalization claim since encoding-principle OOD seems overreached, and I should frame the significance more around compositional generalization instead. The mechanism story also needs a clearer falsifiable prediction. There's a trivial alternative about modular decode-then-classify with smaller language models, though the proposal does partially address this with the decode pipeline baseline. But there's another angle worth raising: what if simply training on much wider diversity of encodings achieves similar results?

Looking at the baselines more carefully, they seem reasonably well-designed to isolate the curriculum effect—random-order uses the same data while flat augmentation uses different data but covers all encoding types. That should help distinguish whether ordering matters or just diversity. I'm also wondering about the ECS metric itself, which is a weighted linear combination of three components. There's no clear justification for why a linear combination is the right functional form, and there could be interactions between nesting depth and tokenizer perplexity that a linear model would miss. Finally, the related work seems to be missing the compositional generalization literature like SCAN and COGS, which are directly relevant to the claim that curriculum helps with compositional encoding spaces.

I should also check for recent work on encoding-aware safety, self-play approaches in red-teaming, and curriculum learning results for transformers that might be mixed or negative. There's also a growing body of work on encoding-based jailbreaks—papers on cipher attacks and various red-teaming approaches—that the proposal should position itself against more carefully. Let me search for these gaps and then formulate my final assessment.

The proposal has genuine novelty but some real vulnerabilities. The encoding-principle OOD claim is the crux of the contribution, yet if it only works for mapping-function OOD, that's interpolation rather than true generalization and reviewers will penalize it heavily. I can strengthen the significance by connecting this to compositional generalization, which is a hot area and gives the encoding attack domain a cleaner testbed. The mechanism around "implicit decoding skills" transferring across different encoding types needs to be more precisely specified. There's also a gap in the related work—compositional generalization literature and recent encoding-specific safety papers should be addressed. Finally, the curriculum versus random result might not be as novel as presented, so the paper needs to preemptively explain why this goes beyond standard curriculum learning findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40a8fc1b-66e2-4965-a23d-4434d80286e3",
  "isSidechain": false,
  "requestId": "req_011Cb6FRy4kjwWBWMF1RyoHu",
  "type": "assistant",
  "uuid": "a13ab44f-f7da-4a85-9641-49f8eb36db9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCkSSJJfYDpoM9sY7HErGV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5622,
      "cache_read_input_tokens": 13247,
      "output_tokens": 3060,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3060,
          "cache_read_input_tokens": 13247,
          "cache_creation_input_tokens": 5622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5622
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

_source line 9 · 2026-05-16T12:31:02.610Z_

I need to carefully analyze this proposal before providing my assessment. Let me first check for highly relevant recent work that could threaten the novelty claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a13ab44f-f7da-4a85-9641-49f8eb36db9a",
  "isSidechain": false,
  "requestId": "req_011Cb6FRy4kjwWBWMF1RyoHu",
  "type": "assistant",
  "uuid": "9833becc-6541-422b-adc4-ff4a4d8bc50f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCkSSJJfYDpoM9sY7HErGV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5622,
      "cache_read_input_tokens": 13247,
      "output_tokens": 3060,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3060,
          "cache_read_input_tokens": 13247,
          "cache_creation_input_tokens": 5622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5622
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

_source line 10 · 2026-05-16T12:31:07.160Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01PCDLqYztkrcybMXmF9nHMk`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search recent encoding jailbreak work",
  "prompt": "Search the web for the most relevant recent papers (2024-2026) on: (1) encoding-based jailbreak defenses for LLMs, specifically any that use curriculum learning or progressive training; (2) compositional generalization applied to adversarial robustness; (3) any paper specifically training lightweight classifiers to be robust against encoded/ciphered jailbreak attacks. I need to assess whether the novelty claim of \"curriculum-structured training for encoding-robust safety classifiers\" has been preempted. Use WebSearch if available, otherwise report what you know. Keep findings concise - just paper titles, key ideas, and how they relate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9833becc-6541-422b-adc4-ff4a4d8bc50f",
  "isSidechain": false,
  "requestId": "req_011Cb6FRy4kjwWBWMF1RyoHu",
  "type": "assistant",
  "uuid": "0b71216a-ffcf-4a40-a3d6-4f864fe8fa48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCkSSJJfYDpoM9sY7HErGV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5622,
      "cache_read_input_tokens": 13247,
      "output_tokens": 3060,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3060,
          "cache_read_input_tokens": 13247,
          "cache_creation_input_tokens": 5622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5622
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

_source line 11 · 2026-05-16T12:31:09.994Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DGxXVuuk2KWeokvE9NHTnj`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search curriculum learning transformer results",
  "prompt": "Search the web for recent papers (2023-2026) on curriculum learning for transformers / large language models, specifically: (1) papers showing that curriculum ordering provides significant vs. marginal benefits for transformer models; (2) any negative results or mixed results about curriculum learning for LLMs; (3) curriculum learning for compositional generalization. I need to assess whether the claim \"curriculum ordering matters significantly for OOD generalization\" is well-supported or controversial in the current literature. Use WebSearch if available, otherwise report what you know. Keep findings concise."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b71216a-ffcf-4a40-a3d6-4f864fe8fa48",
  "isSidechain": false,
  "requestId": "req_011Cb6FRy4kjwWBWMF1RyoHu",
  "type": "assistant",
  "uuid": "f5dd4ab0-4972-4c27-a4b6-a2df6a3e4484",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCkSSJJfYDpoM9sY7HErGV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5622,
      "cache_read_input_tokens": 13247,
      "output_tokens": 3060,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3060,
          "cache_read_input_tokens": 13247,
          "cache_creation_input_tokens": 5622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5622
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

_source line 12 · 2026-05-16T12:31:19.093Z_

<details><summary>↩ Tool result · `toolu_01PCDLqYztkrcybMXmF9nHMk`</summary>

```text
I need permission to use web search tools. Let me report what I can based on my knowledge cutoff (February 2025):

## Key Papers & Trends (Knowledge Cutoff: Feb 2025)

Based on my training data, here are the most relevant recent developments:

**Encoding-Based Jailbreak Defenses:**
- **"Robustness to Adversarial Prompts" (2024)** - Work on detecting encoded/obfuscated prompts, but typically uses static classifiers without curriculum learning
- **"Universal Adversarial Triggers" defenses (2024)** - Generally address prompt-level attacks, less focus on encoding robustness specifically
- Limited papers explicitly combining curriculum learning with encoding-robust defenses as of Feb 2025

**Compositional Generalization & Adversarial Robustness:**
- **"Compositional Generalization in Large Language Models" (2024)** - Focuses on model capability, not robustness
- **"Adversarial Robustness through Decomposition" (2024)** - Addresses compositional approaches to adversarial training but not specifically for encoding attacks

**Lightweight Classifiers for Jailbreak Defense:**
- **"On the Robustness of Language Models to Grammatical Errors" (2024)** - Related work on robustness but not encoding-specific
- **"Safety Classifiers for Prompt Detection" (2024)** - Work on lightweight detectors exists but without explicit curriculum learning for encoding variants

## Assessment:

**Your novelty claim appears relatively strong.** The specific combination of:
1. Curriculum-structured training
2. Encoding-robust safety classifiers  
3. Progressive exposure to increasing encoding complexity

...does not appear to be explicitly addressed in papers available up to Feb 2025. Most defenses use either static classifiers or general adversarial training without the curriculum-progressive structure you're proposing.

**Note:** To get the most current picture (2025-2026), you would need WebSearch/WebFetch permissions enabled. I recommend checking arXiv directly for papers published after February 2025.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b71216a-ffcf-4a40-a3d6-4f864fe8fa48",
  "isSidechain": false,
  "promptId": "5b0581fc-a336-4e08-a782-0f6e85553cc9",
  "type": "user",
  "uuid": "9baea4f6-2a9f-4cbe-bb03-61dedca241c6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for the most relevant recent papers (2024-2026) on: (1) encoding-based jailbreak defenses for LLMs, specifically any that use curriculum learning or progressive training; (2) compositional generalization applied to adversarial robustness; (3) any paper specifically training lightweight classifiers to be robust against encoded/ciphered jailbreak attacks. I need to assess whether the novelty claim of \"curriculum-structured training for encoding-robust safety classifiers\" has been preempted. Use WebSearch if available, otherwise report what you know. Keep findings concise - just paper titles, key ideas, and how they relate.",
    "agentId": "a2deb56823c63c456",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "I need permission to use web search tools. Let me report what I can based on my knowledge cutoff (February 2025):\n\n## Key Papers & Trends (Knowledge Cutoff: Feb 2025)\n\nBased on my training data, here are the most relevant recent developments:\n\n**Encoding-Based Jailbreak Defenses:**\n- **\"Robustness to Adversarial Prompts\" (2024)** - Work on detecting encoded/obfuscated prompts, but typically uses static classifiers without curriculum learning\n- **\"Universal Adversarial Triggers\" defenses (2024)** - Generally address prompt-level attacks, less focus on encoding robustness specifically\n- Limited papers explicitly combining curriculum learning with encoding-robust defenses as of Feb 2025\n\n**Compositional Generalization & Adversarial Robustness:**\n- **\"Compositional Generalization in Large Language Models\" (2024)** - Focuses on model capability, not robustness\n- **\"Adversarial Robustness through Decomposition\" (2024)** - Addresses compositional approaches to adversarial training but not specifically for encoding attacks\n\n**Lightweight Classifiers for Jailbreak Defense:**\n- **\"On the Robustness of Language Models to Grammatical Errors\" (2024)** - Related work on robustness but not encoding-specific\n- **\"Safety Classifiers for Prompt Detection\" (2024)** - Work on lightweight detectors exists but without explicit curriculum learning for encoding variants\n\n## Assessment:\n\n**Your novelty claim appears relatively strong.** The specific combination of:\n1. Curriculum-structured training\n2. Encoding-robust safety classifiers  \n3. Progressive exposure to increasing encoding complexity\n\n...does not appear to be explicitly addressed in papers available up to Feb 2025. Most defenses use either static classifiers or general adversarial training without the curriculum-progressive structure you're proposing.\n\n**Note:** To get the most current picture (2025-2026), you would need WebSearch/WebFetch permissions enabled. I recommend checking arXiv directly for papers published after February 2025."
      }
    ],
    "totalDurationMs": 11925,
    "totalTokens": 18613,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 534,
      "cache_read_input_tokens": 17587,
      "output_tokens": 485,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 534
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 485,
          "cache_read_input_tokens": 17587,
          "cache_creation_input_tokens": 534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 534,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "0b71216a-ffcf-4a40-a3d6-4f864fe8fa48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## Title  EncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training  ## Problem Statement  Encoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, an…",
  "leafUuid": "9baea4f6-2a9f-4cbe-bb03-61dedca241c6",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Encoding-robust classifier via curriculum learning",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61"
}
```

---

### Tool result

_source line 15 · 2026-05-16T12:31:19.322Z_

<details><summary>↩ Tool result · `toolu_01DGxXVuuk2KWeokvE9NHTnj`</summary>

```text
I don't have WebSearch permissions enabled in this environment. However, based on my knowledge cutoff (February 2025), I can share what the literature landscape looked like before that point:

## What I Know About Curriculum Learning for LLMs (Pre-Feb 2025)

**Papers showing significant benefits:**
- Early work by Bengio et al. (2009) and subsequent studies showed curriculum learning can improve sample efficiency, though most were on smaller models
- Some recent papers on "data ordering" for transformers showed non-trivial improvements in convergence speed
- Work on "easy-to-hard" curriculum for pretraining suggested ordering can matter

**Mixed/Negative Results:**
- There's emerging skepticism about whether curriculum learning provides benefits commensurate with the computational cost of reordering
- Some papers found that random shuffling performs nearly as well as carefully designed curricula
- The "no free lunch" perspective: gains on one task may not transfer to others
- Scaling laws research (Chinchilla, Compute-Optimal) suggested that data quality matters less than often assumed at large scales

**Compositional Generalization:**
- Limited direct evidence that curriculum learning significantly improves compositional generalization in LLMs
- SCAN and similar compositional generalization benchmarks showed mixed results
- Some work suggests curriculum helps but the effect sizes are often small

**Current Consensus Issues:**
- Most curriculum learning work predates the scale of modern LLMs (GPT-3+, Claude, PaLM scale)
- Few papers directly compare curriculum vs. non-curriculum at scales >10B parameters
- Reproducibility concerns: what works for BERT may not work for GPT-scale models
- The claim about "curriculum ordering matters significantly for OOD generalization" remains somewhat **controversial** — there's limited large-scale empirical evidence for LLMs specifically

**Recommendation:** To get current findings beyond February 2025, you'd want to check:
- ArXiv preprints in cs.LG and cs.CL from 2025-2026
- Recent papers from major venues (ICLR 2025, NeurIPS 2025, ACL 2026)
- Papers specifically mentioning "data ordering," "example ordering," or "training dynamics" for foundation models

The consensus seems to be shifting toward skepticism, but strong negative results papers are rarer than positive ones due to publication bias.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5dd4ab0-4972-4c27-a4b6-a2df6a3e4484",
  "isSidechain": false,
  "promptId": "5b0581fc-a336-4e08-a782-0f6e85553cc9",
  "type": "user",
  "uuid": "186c503e-23e6-459b-9daa-87317d4c7d37",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for recent papers (2023-2026) on curriculum learning for transformers / large language models, specifically: (1) papers showing that curriculum ordering provides significant vs. marginal benefits for transformer models; (2) any negative results or mixed results about curriculum learning for LLMs; (3) curriculum learning for compositional generalization. I need to assess whether the claim \"curriculum ordering matters significantly for OOD generalization\" is well-supported or controversial in the current literature. Use WebSearch if available, otherwise report what you know. Keep findings concise.",
    "agentId": "a5ec6cef1fb8a523c",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "I don't have WebSearch permissions enabled in this environment. However, based on my knowledge cutoff (February 2025), I can share what the literature landscape looked like before that point:\n\n## What I Know About Curriculum Learning for LLMs (Pre-Feb 2025)\n\n**Papers showing significant benefits:**\n- Early work by Bengio et al. (2009) and subsequent studies showed curriculum learning can improve sample efficiency, though most were on smaller models\n- Some recent papers on \"data ordering\" for transformers showed non-trivial improvements in convergence speed\n- Work on \"easy-to-hard\" curriculum for pretraining suggested ordering can matter\n\n**Mixed/Negative Results:**\n- There's emerging skepticism about whether curriculum learning provides benefits commensurate with the computational cost of reordering\n- Some papers found that random shuffling performs nearly as well as carefully designed curricula\n- The \"no free lunch\" perspective: gains on one task may not transfer to others\n- Scaling laws research (Chinchilla, Compute-Optimal) suggested that data quality matters less than often assumed at large scales\n\n**Compositional Generalization:**\n- Limited direct evidence that curriculum learning significantly improves compositional generalization in LLMs\n- SCAN and similar compositional generalization benchmarks showed mixed results\n- Some work suggests curriculum helps but the effect sizes are often small\n\n**Current Consensus Issues:**\n- Most curriculum learning work predates the scale of modern LLMs (GPT-3+, Claude, PaLM scale)\n- Few papers directly compare curriculum vs. non-curriculum at scales >10B parameters\n- Reproducibility concerns: what works for BERT may not work for GPT-scale models\n- The claim about \"curriculum ordering matters significantly for OOD generalization\" remains somewhat **controversial** — there's limited large-scale empirical evidence for LLMs specifically\n\n**Recommendation:** To get current findings beyond February 2025, you'd want to check:\n- ArXiv preprints in cs.LG and cs.CL from 2025-2026\n- Recent papers from major venues (ICLR 2025, NeurIPS 2025, ACL 2026)\n- Papers specifically mentioning \"data ordering,\" \"example ordering,\" or \"training dynamics\" for foundation models\n\nThe consensus seems to be shifting toward skepticism, but strong negative results papers are rarer than positive ones due to publication bias."
      }
    ],
    "totalDurationMs": 9325,
    "totalTokens": 18163,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 484,
      "cache_read_input_tokens": 17132,
      "output_tokens": 540,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 484
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 540,
          "cache_read_input_tokens": 17132,
          "cache_creation_input_tokens": 484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 484,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 5
    }
  },
  "sourceToolAssistantUUID": "f5dd4ab0-4972-4c27-a4b6-a2df6a3e4484",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-16T12:31:44.628Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me synthesize my analysis based on what I know and the search results.

Key takeaways from the search:
1. The specific combination of curriculum + encoding-robust safety classifiers appears novel (no direct preemption found up to Feb 2025)
2. Curriculum learning for transformers has mixed/controversial results - this is a significant concern
3. Limited evidence that curriculum helps with compositional generalization at scale

Now let me formulate my discovery points carefully.

Let me think through each dimension:

**Novelty Assessment:**


The combination itself is novel, though each component—curriculum learning, encoding attacks, safety classifiers—is well-established. The real novelty hinges on whether curriculum ordering actually improves out-of-distribution generalization, but that claim faces real skepticism in the transformer literature. The ECS metric feels incremental, and while the two-regime mechanism is intriguing, it's largely speculative.

**Significance Assessment:**
Encoding attacks matter but represent a shrinking threat surface. The practical angle of using a smaller classifier to protect against frontier models is compelling, though the broader question about compositional generalization carries more weight than the specific encoding-attack application.

**Related Work Gaps:**
The paper seems to overlook the compositional generalization literature—SCAN, COGS, and related benchmarks—which is a notable gap given the core claims about generalization.

Now I'm identifying the actual vulnerabilities in the proposal. The encoding-principle OOD claim overreaches significantly: whitespace steganography and zero-width Unicode are fundamentally different from base64 or ROT13, requiring the model to detect invisible characters rather than recognize visible patterns. That's the most critical weakness and also where the novelty actually lives. Reframing this around compositional generalization would strengthen both the novelty and significance, since the encoding space is inherently compositional. I also need a falsifiable prediction that distinguishes the mechanism from a simpler explanation—that curriculum learning just prevents catastrophic forgetting rather than enabling genuine compositional generalization.

Given the mixed results in curriculum learning literature, I need to directly confront why this domain should be different. And the core claim needs genuine tension: if curriculum helps, reviewers dismiss it as obvious; if it doesn't, it's just another negative result. The paper has to set up a real surprise, not just "we tried curriculum and it worked."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "186c503e-23e6-459b-9daa-87317d4c7d37",
  "isSidechain": false,
  "requestId": "req_011Cb6FYmSxFLHjYLUynasCi",
  "type": "assistant",
  "uuid": "dcf94bbf-8517-4886-b9af-d70c997b5d49",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJThaCkpPwN2Xt7xnpzA9q",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4130,
      "cache_read_input_tokens": 18869,
      "output_tokens": 3515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4130,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3515,
          "cache_read_input_tokens": 18869,
          "cache_creation_input_tokens": 4130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4130
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

_source line 17 · 2026-05-16T12:32:53.768Z_

Now I have enough context to provide a thorough assessment. Let me deliver my analysis.

---

【状态】: 有发掘空间

---

【发掘点 1】
- 维度: 前提假设质疑 / novelty 锐化
- 内容: **Encoding-principle OOD 的 claim 存在逻辑断裂，是整篇论文最脆弱也最关键的点。** 训练编码族（base64, ROT13, homoglyphs）的共同特征是：编码后的内容在 token 层面是 *可见的*——它们改变了字符/词的 surface form，但信息仍然承载在可见 token 序列中。模型可以通过学习 visible token patterns 来做 implicit decoding。然而，两个 encoding-principle OOD 测试族——whitespace steganography 和 zero-width Unicode——的核心机制是将有害内容 *隐藏在不可见字符中*。这是一个根本不同的信息承载方式：模型需要检测的不是"可见 token 序列的结构规律"，而是"不可见字符序列中隐藏的信息"。Curriculum 训练中积累的所有"结构模式识别 + 组合解码策略"都是基于可见 token 的——这些技能为什么能迁移到检测不可见字符中的信息？Proposal 中的 two-regime mechanism 完全没有覆盖这个 gap。如果 encoding-principle OOD 实验结果为 negative（高概率），论文的核心 novelty claim 就从"真正的 OOD 泛化"降级为"同一编码原理内的插值"——这对审稿人的 surprise factor 是致命打击。**建议：要么 (a) 将 encoding-principle OOD 的测试族替换为与训练编码 share 相同信息承载方式但 mapping 不同的编码（如 Morse code、自定义字母替换表、phonetic encoding），保持 genuine OOD 但在逻辑上可解释为什么技能能迁移；要么 (b) 保留 whitespace/zero-width 但将其重新定位为 "boundary test"——明确预测这些族上 curriculum 不应该 outperform random（这反而成为理解 curriculum 泛化边界的积极贡献）。选项 (b) 实际上更有学术价值：它展示了 curriculum 泛化的 *scope conditions*，比一个模糊的"we generalize to everything"claim 更有说服力。**
- 价值: 直接决定 Novelty 维度的天花板。如果 OOD claim 站不住，核心贡献从"范式级发现"降为"工程优化"。修复此点后，novelty claim 从 vulnerable 变为 robust——无论结果是正面还是负面，都有清晰的学术故事。

【发掘点 2】
- 维度: significance 提升
- 内容: **当前 framing 将 significance 限制在了 "encoding attack defense" 这一狭窄应用上，遗漏了一个更有影响力的研究问题。** 编码攻击空间本质上是一个 *离散组合变换空间*（N 个编码原语 × K 层嵌套 = O(N^K) 种组合）。Curriculum 在此空间中促进 OOD 泛化的问题，实质上是 **compositional generalization** 的一个实例——这是 NLP/ML 领域持续关注的核心难题（SCAN, COGS, compositional generalization benchmarks）。但 proposal 完全没有连接到这一文献。建议将论文的上位研究问题重新 frame 为："Can complexity-structured curriculum enable compositional generalization in discrete transformation spaces?"——encoding attacks 是这个更大问题的 *testbed*，而非全部贡献。这样做的好处：(1) Significance 从 "safety engineering" 升级为 "fundamental learning dynamics"；(2) 吸引 compositional generalization 社区的审稿人兴趣；(3) 为 limitations 中提到的 "transfer to other compositional attack spaces" 提供自然的理论框架。
- 价值: 命中 Significance 维度。将论文的潜在影响力从 safety subcommunity 扩展到 broader ML audience，直接影响审稿人对 "importance of research question" 的评分。

【发掘点 3】
- 维度: 核心 claim 强化
- 内容: **Curriculum 优于 random ordering 的 mechanism story 缺少与最 trivial 的替代解释之间的区分。** 一个更简单的解释是：curriculum ordering 之所以有效，不是因为它构建了"progressive decoding skill hierarchy"，而仅仅是因为它 **避免了早期训练阶段被高 ECS 样本淹没导致的 catastrophic interference**——模型先在简单样本上稳定学到 content features，这些 features 在后续高 ECS 阶段不会被完全覆盖。这是标准的 curriculum learning benefit，不需要任何 "implicit decoding skill acquisition" 的新颖机制。如果这个 trivial 解释成立，novelty 就大打折扣——论文只是重新确认了"easy-to-hard ordering helps"这个已知结论在新 domain 上的适用性。**要区分这两个解释，需要一个关键的 falsifiable prediction：** 如果机制是 "progressive decoding skill acquisition"（组合性技能构建），那么 curriculum 的优势应该随 nesting depth 增加而 *扩大*（因为更深的嵌套更依赖组合性解码技能）。如果机制仅是 "catastrophic interference prevention"，优势应该在所有 nesting depth 上大致均匀（因为保护的只是 base content features）。建议在论文中明确提出这个 differential prediction，并在实验中按 nesting depth 分层报告 curriculum vs. random 的 gap。这不仅加强 mechanism claim，还提供了独立的 analytical contribution。
- 价值: 命中 Novelty 维度。如果不区分 trivial mechanism，审稿人极可能提出"this is just standard curriculum learning benefit"的质疑——这是 novelty 的最大威胁之一。提出 differential prediction 把论文从 "empirical observation" 升级为 "mechanistic understanding"。

【发掘点 4】
- 维度: related work 差异化
- 内容: **Compositional generalization 文献的缺失是一个显著的 related work gap，可能导致审稿人认为作者对问题的理论背景理解不足。** SCAN (Lake & Baroni, 2018)、COGS (Kim & Linzen, 2020)、以及后续大量关于 transformer compositional generalization 能力与局限的工作，直接关系到本文的核心 claim：在组合空间中通过 curriculum 实现 OOD 泛化。此外，curriculum learning 在 transformer 上的 mixed results（部分工作显示 marginal improvement，部分显示 anti-curriculum 同样有效）需要被直接 acknowledge 并解释为什么本文的 domain 不同——具体来说，encoding attack 的组合空间有一个 *natural partial ordering on complexity*（nesting depth 提供了非人工定义的 difficulty metric），这在很多 curriculum learning 失败的 domain 中是不存在的。这个论证如果做好，反而能把 related work 的潜在威胁转化为 novelty 的支撑："curriculum works here because the domain has intrinsic compositional structure that provides a principled difficulty ordering, unlike the arbitrary orderings that fail in prior work."
- 价值: 命中 Related Work 差异化维度。补上此 gap 同时达到两个效果：(1) 消除审稿人"authors missed key related work"的负面印象；(2) 将 encoding domain 的结构特殊性转化为论文的理论 selling point。

【发掘点 5】
- 维度: trivial alternative 威胁
- 内容: **Proposal 低估了 modular decode-then-classify pipeline 在现代 small LM 时代的竞争力。** 论文将 "learned canonicalization" 列为已有方法并以 "error propagation + adversarial attack surface" 驳回，但这一驳斥基于隐含假设：decoder 是一个独立的 seq2seq 模型。然而，如果 decoder 本身就是一个 instruction-following small LM（如 Qwen2.5-1.5B with "decode this text" prompt），其解码能力可能相当强——因为这些模型在 pretraining 中已经见过大量编码/解码的 text。这个 pipeline（1.5B decoder → LlamaGuard-3）总参数量与 proposal 的 4B classifier 相当，但具有更好的 interpretability 和 modularity。**如果不在实验中包含一个 "modern small-LM decoder + standard guardrail" baseline，审稿人很可能会要求补充。** 建议在 baseline 中增加 "Qwen2.5-1.5B decode → LlamaGuard-3 classify" pipeline，并在 nesting-depth vs. accuracy 曲线上展示 error propagation 的实证证据（proposal 中已提到此曲线但仅作为 indirect evidence）。这实际上是一个可以赢的比较：multi-layer nesting 下 pipeline 的 error compounding 应该表现明显差于 end-to-end classifier。
- 价值: 命中 Novelty 维度（消除 trivial alternative 威胁）。如果审稿人认为存在一个更简单的替代方案没被比较，novelty score 会显著下降。主动展示 end-to-end 优于 modular pipeline（尤其在高 nesting depth），反而成为 supporting evidence for the core approach。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcf94bbf-8517-4886-b9af-d70c997b5d49",
  "isSidechain": false,
  "requestId": "req_011Cb6FYmSxFLHjYLUynasCi",
  "type": "assistant",
  "uuid": "024d18cb-be6a-4ca1-8ff6-0d9a009000c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJThaCkpPwN2Xt7xnpzA9q",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4130,
      "cache_read_input_tokens": 18869,
      "output_tokens": 3515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4130,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3515,
          "cache_read_input_tokens": 18869,
          "cache_creation_input_tokens": 4130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4130
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

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## Title  EncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training  ## Problem Statement  Encoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, an…",
  "leafUuid": "024d18cb-be6a-4ca1-8ff6-0d9a009000c1",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Encoding-robust classifier via curriculum learning",
  "sessionId": "d24c1dd8-f064-4318-9ac4-73307e638e61"
}
```

---
