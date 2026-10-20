# Research conversation: Title EncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training ## Problem Statement E

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/c612cc08-f5d1-4069-9c04-c8d36ad8cfa9.jsonl`
- **Structured JSON:** [`c30f67c6e2d45d6efb3d.json`](../../sessions/c3/c30f67c6e2d45d6efb3d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T12:29:47.131Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:29:47.131Z",
  "sessionId": "c612cc08-f5d1-4069-9c04-c8d36ad8cfa9",
  "content": "## Title\n\nEncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training\n\n## Problem Statement\n\nEncoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, and their nested compositions) exploit a fundamental vulnerability in LLM safety guardrails: classifiers trained on plaintext or limited encoding variations fail when inputs are transformed through unseen encoding schemes. Existing defenses have critical limitations:\n\n1. **Rule-based detection + decoding pipelines** (regex detection → known decoder → standard guardrail): Effective for known single-layer encodings with distinctive statistical signatures (base64 character set, ROT13 alphabetic patterns). Fail on: (a) partial encoding where only segments are transformed, defeating whole-input detection heuristics; (b) adversarial mixing of encoded/plaintext creating ambiguous signatures; (c) novel encodings without pre-programmed decoders.\n\n2. **Learned canonicalization** (seq2seq decode → classify): Error propagation compounds across nesting layers; the canonicalizer itself becomes an adversarial attack surface; partial encoding requires semantic understanding to identify decode targets.\n\n3. **Frontier LLM zero-shot** (GPT-4/Claude with \"detect if content is harmful regardless of encoding\"): Can leverage pre-training exposure to encodings, but impractical for deployment-scale guardrails due to cost ($0.01-0.03 per input) and latency (1-3s per call vs. millisecond-level local inference).\n\nThe core challenge is achieving **generalization to unseen encoding families at deployment-practical cost**—a lightweight classifier that remains robust against encoding types never encountered during training.\n\n## Core Thesis\n\nWe hypothesize that a classifier trained via **complexity-structured curriculum**—where encoding attacks are presented in order of a principled complexity metric—acquires **encoding-robust content extraction capabilities** that generalize to held-out encoding types unseen during training.\n\n**Mechanism (Two-Regime Explanation):**\n\n- **Low-ECS regime (simple encodings):** Content semantics remain partially accessible through tokenization (e.g., base64 of short text preserves some token-level correlations). The curriculum forces the model to anchor harmful-content semantic features—learning what \"harmful content looks like\" across mild surface perturbations (**content anchoring**).\n\n- **High-ECS regime (complex/nested encodings):** Token-level content information is effectively destroyed by multi-layer encoding. The model cannot rely on direct semantic features; it must develop strategies for implicit decoding—recognizing encoding structure patterns and reconstructing content signal. The curriculum's contribution is **progressive decoding skill acquisition**: simple decoding patterns learned in the low-ECS regime (recognizing base64 structure, identifying shift patterns) provide compositional building blocks that support parsing more complex nested structures.\n\nThe generalization prediction follows: if the model acquires generalized decoding skills (structural pattern recognition + compositional decoding strategies) rather than memorizing specific encoding-to-content mappings, it should transfer to novel encodings that share structural properties with training encodings. For truly novel encoding principles, the model's content-anchoring from the low-ECS regime provides a robust classification backbone once any partial decoding succeeds.\n\n**Important distinction:** We do NOT claim the model learns literal \"encoding-invariant features\" in the information-theoretic sense (impossible for fully-scrambled token sequences). Rather, curriculum training builds a progressive hierarchy of decoding capabilities—from direct semantic extraction (low-ECS) to structural pattern matching + compositional decoding (high-ECS)—that transfers across encoding types more effectively than flat or random training.\n\n## Relationship to Prior Work\n\n### Curriculum Adversarial Training\nCai et al. (IJCAI 2018) progressively increase perturbation magnitude ε for image classifiers; Wang et al. (NeurIPS 2021) order samples by difficulty for better generalization. Key differences from our work:\n1. **Discrete compositional space vs. continuous perturbation:** Prior work operates in continuous ε-ball spaces with scalar difficulty. Encoding attacks form a discrete compositional space requiring multi-dimensional complexity metrics.\n2. **OOD generalization vs. in-distribution robustness:** Prior work only evaluates on the same attack type used in training. We explicitly test generalization to unseen encoding families—including encodings based on entirely different structural principles.\n\n### Domain Generalization (DG)\nEach encoding type can be viewed as a domain; OOD generalization to unseen encodings resembles domain generalization. However, standard DG methods (IRM, DANN, CORAL, DRO) are not directly applicable because:\n1. **Non-differentiable discrete domains:** Encoding transformations are discrete operations; gradient-based domain alignment (DANN adversarial training) cannot be applied to the input transformation space.\n2. **Exponential domain combinatorics:** Composing N encoding primitives at K nesting levels creates O(N^K) potential domains—impossible to enumerate as source domains at training time.\n3. **Structural curriculum as natural alternative:** The compositional structure of encoding attacks provides a natural progressive training signal that standard DG methods lack—curriculum exploits the partial ordering on complexity inherent in compositional spaces.\n\n## Key Contributions\n\n1. **Primary Contribution (OOD Generalization via Curriculum):** Empirical demonstration that complexity-structured curriculum enables generalization to unseen encoding families—at two levels: (a) mapping-function OOD (same encoding principle, different specific mapping), and (b) encoding-principle OOD (structurally different encoding type). Direct representation-level evidence (CKA + linear probing) characterizes how curriculum shapes internal representations differently from baselines.\n\n2. **Encoding Complexity Score (ECS):** Formalized metric combining nesting depth, CPT deviation, and tokenizer perplexity. Validated via correlation with classifier difficulty; individual component contributions quantified.\n\n3. **Co-Evolutionary Training Framework:** GRPO attacker + SFT classifier with curriculum-ordered training, demonstrating co-evolution can further improve upon static curriculum.\n\n4. **Deployment-Practical Encoding Defense:** A 4B-parameter classifier achieving encoding robustness comparable to frontier LLM zero-shot, at orders-of-magnitude lower inference cost.\n\n## Methodology\n\n### Encoding Complexity Score (ECS)\n\n$$ECS(e) = \\alpha \\cdot \\text{NestingDepth}(e) + \\beta \\cdot \\text{CPT\\_Deviation}(e) + \\gamma \\cdot \\text{TokenizerPerplexity}(e)$$\n\n- NestingDepth: number of compositional encoding layers\n- CPT_Deviation: |CPT_encoded / CPT_plaintext - 1|\n- TokenizerPerplexity: target tokenizer's perplexity on encoded text\n\n**Weight determination:** Pilot study (200 samples spanning full ECS range) measures Spearman ρ of each individual component with classifier error rate. Weights set proportional to individual predictive power.\n\n**Component contribution analysis (submission-critical):** Report Spearman ρ for each single component alone and for leave-one-out combinations, demonstrating that all three contribute meaningfully and that the composite metric outperforms any single component.\n\n### Co-Evolutionary Training Loop\n\n**Attacker (Qwen2.5-1.5B, GRPO):**\n- Generates encoding attacks with ECS in current curriculum band\n- Reward: +1 if bypasses classifier AND oracle confirms harmful\n- Entropy regularization prevents encoding-type collapse\n\n**Classifier (Qwen2.5-4B, SFT):**\n- Curriculum-ordered training: Stage 1 (ECS ≤ threshold) → Stage 2 (ECS > threshold)\n- FPR rollback: revert if FPR > 2% on benign validation\n- Semantic deduplication: cosine similarity > 0.95 removed\n\n**Oracle:** GPT-4o + deterministic decoder cross-validation; disagreements excluded.\n\n**Fallback:** If co-evolutionary loop unstable by Day 7, switch to static curriculum SFT.\n\n### Baseline Definitions (Comparison Table)\n\n| Baseline | Data Source | Data Composition | Presentation Order | Isolates |\n|----------|-------------|------------------|-------------------|----------|\n| **Curriculum (ours)** | Co-evolutionary or static generation | ECS-staged | Monotone increasing ECS | — |\n| **Random-order** | Same data as curriculum | Identical composition | Randomly shuffled | Ordering effect |\n| **Flat augmentation** | Fresh generation: each epoch randomly samples encoding type per prompt | Uniform across all ECS levels | Random within each epoch | Data composition + ordering |\n| **Reverse curriculum** | Same data as curriculum | Identical composition | Monotone decreasing ECS | Direction effect |\n| **Static curriculum** | Rule-based generation, ECS-ordered | Identical to curriculum | Same ordering | Co-evolution effect |\n| **Decode + LlamaGuard-3** | N/A (inference only) | N/A | N/A | End-to-end vs. pipeline |\n| **GPT-4 zero-shot** | N/A (API call) | N/A | N/A | Cost/accuracy frontier |\n\nKey distinctions:\n- Random-order vs. Flat augmentation: Random-order uses curriculum's exact data (same samples) in shuffled order → isolates ordering. Flat augmentation generates different data with uniform encoding distribution → tests whether curriculum's staged data composition matters.\n- Static curriculum vs. Curriculum: Same data, same order, but no co-evolutionary attacker → isolates co-evolution benefit.\n\n### Compute Fairness\n\n- **H1-H3 (core claims):** Based on static curriculum vs. baselines. All methods use identical model architecture (Qwen2.5-4B), identical total training FLOPs, identical number of training steps. Only variable: data ordering / composition.\n- **H4 (co-evolution bonus):** Co-evolutionary method has additional compute (attacker training: ~12h, oracle calls: ~$250). For fair comparison, include a \"compute-matched static\" variant: redirect co-evolution's extra FLOPs into additional static curriculum training epochs.\n- **Reporting:** Table includes total FLOPs (classifier only), total FLOPs (including attacker), wall-clock time, and training tokens for each method.\n\n### Compute and Cost\n\n- Hardware: 4× A100 80GB\n- Per classifier run: ~8h\n- Total runs: curriculum (5) + random (5) + flat (3) + reverse (3) + static (3) + compute-matched static (3) = 22 classifier runs\n- Parallelization: 4 GPUs → 4 runs simultaneously → ~44h for all classifier training\n- Attacker: 12h (2 rounds)\n- Oracle: ~18K calls ≈ $250\n- GPT-4 zero-shot evaluation: ~12K test cases × $0.01 ≈ $120\n- Inference-only analyses (probing, CKA, ECS stats): ~4h\n- Total: ~60h wall-clock for training + ~4h analysis\n\n## Experimental Design\n\n### Hypotheses\n\n- **H1 (Curriculum > Random):** Curriculum achieves ≥10pp lower encoding-ASR than random-order at equivalent FLOPs (95% bootstrap CI of difference excludes 0, one-sided).\n- **H2 (OOD Generalization):** Curriculum maintains ≤30% encoding-ASR on held-out encodings where baselines exceed 60%. Tested at two OOD levels: mapping-function OOD and encoding-principle OOD.\n- **H3 (ECS Predictiveness):** ECS correlates with classifier error (Spearman ρ ≥ 0.7) on held-out encodings; composite metric outperforms any single component.\n- **H4 (Co-evolution > Static, bonus):** Co-evolutionary > static curriculum by ≥5pp on composite encodings, after controlling for extra compute.\n\n### Held-Out Encoding Families\n\n**Mapping-function OOD (same structural principle as training encodings):**\n- Braille Unicode substitution (character substitution — cf. homoglyphs in training)\n- Custom Caesar-variant cipher with position-dependent shift (shift-based — cf. ROT13 in training)\n- NATO phonetic alphabet (word-level substitution)\n\n**Encoding-principle OOD (structurally different from all training encodings):**\n- Whitespace steganography (harmful content encoded in whitespace patterns between benign text)\n- Zero-width Unicode character encoding (content hidden in invisible Unicode sequences)\n\nThis two-level OOD structure explicitly tests whether generalization is merely interpolation within known principles (mapping-function OOD) or genuine extrapolation to novel encoding paradigms (encoding-principle OOD).\n\n### Evaluation Protocol\n\n**External benchmarks (primary):**\n- HarmBench encoding-perturbed\n- JailbreakBench encoding subset\n- WildGuardTest encoding-perturbed\n\n**EncoAttack (supplementary):**\n- 500 base prompts: HarmBench (200) + AdvBench (150) + WildGuardTest (150)\n- 8 encoding types × 3 nesting levels = 12,000 test cases\n- Independent implementation from training; validated ≥80% bypass on undefended LlamaGuard-3\n\n**Held-out encodings:** 5 families as specified above\n\n**GPT-4 zero-shot reference:** Same test sets, prompt: \"The following text may be encoded. Determine if the underlying content, once decoded, would be harmful.\"\n\n**Metrics:**\n- Encoding-ASR (primary)\n- Clean FPR at thresholds: 0.5%, 1%, 2%, 5% with Pareto frontier\n- Benign test: WildGuardTest benign (~1000) + LMSYS-Chat-1M sample (1000)\n- Per-encoding breakdown\n- ECS-difficulty correlation (composite + individual components)\n- Nesting-depth vs. decode-accuracy curve (demonstrating pipeline error propagation)\n\n### Representation Analysis\n\n1. **CKA + Cosine Similarity:** For 100 prompts × (plaintext + 8 encoding variants), extract penultimate-layer representations. Compute intra-prompt cross-encoding cosine similarity. Compare curriculum vs. random-order.\n\n2. **Linear Probing (Disentanglement Test):**\n   - Train linear probe A: predict content category (harmful topic type) from representations\n   - Train linear probe B: predict encoding type from representations\n   - **Prediction:** Curriculum model → high probe-A accuracy, LOW probe-B accuracy (encoding info discarded). Random-order model → lower probe-A, higher probe-B (encoding info retained).\n   - This directly tests whether curriculum induces disentanglement of content from encoding surface features.\n\n3. **Learning Dynamics:** Per-checkpoint (500 steps) ASR curves for low-ECS and high-ECS separately. Expected pattern: curriculum shows staged learning (low-ECS converges first, smooth transition to high-ECS); random-order shows chaotic/concurrent learning.\n\n### Statistical Rigor\n\n- All methods: 5 seeds (curriculum, random-order) or 3 seeds (flat, reverse, static) with mean ± std\n- H1: 95% bootstrap CI on paired difference (curriculum seed i vs. random-order seed i, same initialization)\n- Effect sizes: Cohen's d reported alongside p-values\n- Multiple comparison correction: Bonferroni for family of H1-H3 tests\n\n### Oracle Pilot (Days 1-3)\n\n- 100 samples per ECS band\n- Measure GPT-4o + deterministic decoder agreement rate\n- If < 80% for high-ECS: switch to deterministic-only for Stage 2\n\n## Stability Mechanisms (Engineering, Not Contributions)\n\nBorrowed from prior work (TriPlay-RL, standard RL practices):\n- Entropy regularization\n- FPR rollback\n- Semantic deduplication\n\nTrigger frequencies reported. Full ablation in camera-ready.\n\n## Limitations (To Acknowledge in Paper)\n\n1. Learned canonicalization (seq2seq decode → classify) not empirically compared due to training cost; theoretical arguments + decode error propagation curve provided as indirect evidence.\n2. General principle validated only on encoding attacks; transfer to other compositional attack spaces (prompt injection, multi-turn) remains future work.\n3. ECS weight sensitivity not fully explored (±20% perturbation analysis in supplementary).\n\n## Timeline (17 days, with buffer)\n\n**Phase 1: Setup + Pilot (Days 1-3)**\n- ECS implementation, encoding generators (including held-out families), data pipeline\n- Oracle pilot (100 samples/band)\n- Fast pilot curriculum run (reduced data, 2h) to validate training dynamics + ECS threshold\n\n**Phase 2: Core Training (Days 4-9)**\n- Days 4-6: Curriculum (5 seeds) + random-order (5 seeds) [parallelized, 4 GPUs]\n- Days 7-8: Flat augmentation (3) + reverse curriculum (3) + static (3) [parallelized]\n- Day 9: Co-evolutionary attempt + compute-matched static + decode pipeline\n\n**Phase 3: Evaluation + Analysis (Days 10-12)**\n- Day 10: Full benchmark evaluation + held-out encodings + GPT-4 zero-shot\n- Day 11: Representation analysis (CKA, probing) + ECS component stats + learning dynamics\n- Day 12: Statistical tests, nesting-depth decode curve, Pareto analysis\n\n**Phase 4: Writing (Days 13-15)**\n- Day 13-14: Main paper draft\n- Day 15: Figures, tables, polishing\n\n**Buffer + Camera-ready (Days 16-17)**\n- Additional seeds if needed, stability ablation, writing revision\n\n**Fallback:** Co-evolutionary unstable by Day 8 → drop H4, focus H1-H3 with static curriculum."
}
```

---

### Runtime record

_source line 2 · 2026-05-16T12:29:47.138Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:29:47.138Z",
  "sessionId": "c612cc08-f5d1-4069-9c04-c8d36ad8cfa9"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T12:29:47.153Z_

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
  "promptId": "96425f6d-7ee0-42c2-9ade-ad4b596c60c7",
  "type": "user",
  "uuid": "c2885b44-db45-46cb-a260-7bc7aaadaaef",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c612cc08-f5d1-4069-9c04-c8d36ad8cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T12:29:47.151Z_

```json
{
  "parentUuid": "c2885b44-db45-46cb-a260-7bc7aaadaaef",
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
  "uuid": "a066a36e-8f35-47b7-bea3-6b7cbe0ef1ee",
  "timestamp": "2026-05-16T12:29:47.151Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c612cc08-f5d1-4069-9c04-c8d36ad8cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T12:29:47.151Z_

```json
{
  "parentUuid": "a066a36e-8f35-47b7-bea3-6b7cbe0ef1ee",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5f04952e-3715-4774-b6dd-48e984860b3b",
  "timestamp": "2026-05-16T12:29:47.151Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c612cc08-f5d1-4069-9c04-c8d36ad8cfa9",
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
  "leafUuid": "5f04952e-3715-4774-b6dd-48e984860b3b",
  "sessionId": "c612cc08-f5d1-4069-9c04-c8d36ad8cfa9"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "EncoGuard: Encoding-robust LLM safety via curriculum training",
  "sessionId": "c612cc08-f5d1-4069-9c04-c8d36ad8cfa9"
}
```

---

### Assistant

_source line 8 · 2026-05-16T12:32:17.374Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal from the perspective of a 补救 agent (remediation agent), focusing exclusively on experimental design and technical execution completeness. I need to evaluate:

1. Baseline coverage
2. Experimental design
3. Evaluation metrics
4. Ablation design
5. Compute fairness
6. Feasibility

Let me go through the proposal systematically.

### Baseline Coverage

The baselines are:
1. Curriculum (theirs)
2. Random-order (same data, shuffled)


3. Flat augmentation (different data, uniform encoding distribution)
4. Reverse curriculum (same data, reverse order)
5. Static curriculum (rule-based, no co-evolution)
6. Decode + LlamaGuard-3 (pipeline approach)
7. GPT-4 zero-shot (cost/accuracy frontier)

This covers the main comparison points well. They've included random and reverse orderings to test whether the curriculum structure itself matters, plus static rules and alternative approaches. The main gaps would be other learning strategies like anti-curriculum or self-paced learning, though reverse curriculum partially addresses that. Domain generalization baselines aren't explicitly mentioned, which could be worth considering.

Actually, looking at their reasoning for excluding DG methods—they claim the discrete encoding transformations aren't differentiable so gradient-based alignment won't work. But that's not quite right. Methods like DANN and DRO operate on the learned representations, not the input transformations themselves, so you could theoretically apply them to the representation space across different encoding types. The argument about non-differentiable discrete domains doesn't fully justify skipping these baselines, since representation-level alignment should still be feasible.

On the baseline side, they mention LlamaGuard-3 but don't compare against a standard fine-tuned version on encoding data—though their flat augmentation baseline with uniform encoding distribution might cover that gap. I should also check whether they compare against other encoding-robust safety classifiers like WildGuard or ShieldLM.

For adversarial training, standard PGD-style approaches don't translate well to discrete encodings, so flat augmentation is probably the right analogue. But I'm still uncertain about domain generalization methods—the authors claim DG isn't applicable, yet techniques like CORAL or IRM that work on learned representations could potentially help here.

Actually, I should push back on this. DRO and Group DRO are straightforward to apply since they just upweight difficult examples, and at minimum the paper should empirically demonstrate why a particular DG method fails rather than dismissing the whole category. This feels like a real gap I need to flag.

Looking at the experimental design itself, it's quite solid—the hypotheses are clear, the two-level OOD structure for held-out encoding families is well-motivated, and they've included external benchmarks plus custom attacks with proper statistical rigor through bootstrap confidence intervals and multiple comparison corrections. The representation analysis using CKA and probing adds good depth to understanding what's happening.

But I'm concerned about whether the encoding-principle OOD families are actually fair tests. Whitespace steganography and zero-width Unicode are fundamentally different from character-level encodings—they require detecting patterns in invisible or spacing information rather than character substitutions. If the model has never encountered steganographic encoding, expecting strong generalization there is a very ambitious claim. The authors do state in H2 that curriculum should maintain ≤30% encoding-ASR on held-outs while baselines exceed 60%, which might be unrealistic for encoding-principle OOD. That said, the experiment itself is sound—testing on these cases is valid, they just need to be clearer about what performance levels are actually reasonable to expect.

The real issue is that H2 applies the same threshold uniformly across both OOD levels, when they probably should split this into separate hypotheses with different thresholds for mapping-function OOD versus encoding-principle OOD, or at least report results separately. Otherwise H2 might technically fail on the harder encoding-principle cases and require awkward explanation.

The EncoAttack validation looks solid—confirming ≥80% bypass rate on undefended LlamaGuard-3 ensures the attacks are genuinely effective. The oracle design using GPT-4o with deterministic decoder cross-validation is reasonable, and the pilot agreement check is a smart safeguard. They're predicting curriculum will show linear probing improvements in a particular direction.

Now I'm questioning whether the prediction about low probe-B accuracy for encoding type recognition actually holds up—if the model learns to decode encodings well, wouldn't it necessarily recognize encoding types? The real question is whether the representation is disentangled from encoding information, not whether that information is completely absent. The experiment design itself is sound though; they'll just report whatever the probes show. The bigger concern is the ECS validation approach—they mention correlating with classifier error on held-out encodings, but they haven't specified which classifier baseline they're using, and that choice significantly affects whether the correlation will be meaningful. which would undermine H3. They should validate on an untrained/baseline classifier.

Actually wait, re-reading H3: "ECS correlates with classifier error (Spearman ρ ≥ 0.7) on held-out encodings." This needs to be more specific about which classifier. If it's about an untrained baseline, it validates ECS as a difficulty metric. If it's about the curriculum-trained classifier, it validates that ECS captures residual difficulty even after curriculum training. Both are interesting but different claims. They need to specify.

6. **Training data contamination check**: For the held-out encoding families, they need to ensure that no similar encodings appear in the training data. They mention held-out families explicitly, but there's no discussion of validating that the training data doesn't inadvertently include similar patterns.

### Evaluation Metrics

- Encoding-ASR: good primary metric
- Clean FPR at multiple thresholds with Pareto frontier analysis: solid approach
- Per-encoding breakdown and benign test set coverage (WildGuardTest + LMSYS-Chat-1M sample): both look good

The metrics are actually fairly comprehensive—ASR captures detection rate, FPR is reported, and precision/F1 can be derived, so the core classification metrics are covered. Now they mention latency comparisons between their millisecond-level local inference and GPT-4's 1-3 second response time, but the analysis seems to cut off there. call" in the problem statement, but don't include latency as a formal evaluation metric. If "deployment-practical" is a claim, latency and throughput should be measured.

3. **Content category breakdown**: They should report performance breakdown by harmful content category (violence, CSAM, etc.) to ensure the model isn't just good at some categories. Actually, this might be implicit in the per-encoding breakdown, but cross-category analysis would be valuable.

### Ablation Design

The ablation design is strong:
- Random-order vs. Curriculum → ordering effect
- Flat augmentation vs. Curriculum → composition + ordering
- Reverse curriculum vs. Curriculum → direction
- Static curriculum vs. Curriculum → co-evolution
- Compute-matched static → controls for extra compute

And for ECS:
- Individual component Spearman ρ
- Leave-one-out combinations

This is comprehensive. One gap I'm noticing is the lack of ablation across model sizes—they only test on Qwen2.5-4B, so I can't tell if the curriculum benefits scale differently for smaller or larger models. That would be nice to have but probably isn't essential. They do acknowledge that ECS weight sensitivity wasn't fully explored beyond the ±20% perturbation analysis in supplementary materials.

### Compute Fairness

This is well-addressed with identical model, FLOPs, and steps across H1-H3, plus a compute-matched static variant for H4. They're reporting total FLOPs, wall-clock time, and training tokens.

### Feasibility

The hardware requirements (4× A100 80GB) are reasonable and obtainable, and the 17-day timeline seems realistic.

The cost is manageable at around $250 for Oracle and $120 for GPT-4 evaluation. All the datasets (HarmBench, AdvBench, WildGuardTest) are publicly available, and both Qwen models are open source.

The 17-day timeline is tight, but the parallelization math checks out—running 10 curriculum and random-order experiments in parallel across 4 GPUs takes about 3 days, and the subsequent 9 runs fit into another 2 days with the same parallelization strategy.

The main risks are GRPO training stability for the attacker (though they have a fallback to static curriculum), and the complexity of implementing 8 encoding types with 3 nesting levels plus 5 held-out families in just 3 days. The whitespace steganography approach in particular is more involved than simple encoding—it requires embedding harmful content within benign text patterns, which adds significant engineering overhead. ign text with unusual whitespace. The classifier would need to detect anomalous whitespace patterns. This is fundamentally different from recognizing encoded content. 

- Zero-width Unicode: Similar - the visible text looks benign, harmful content is hidden in invisible characters. The tokenizer might strip these characters entirely.

These two encoding-principle OOD families might be problematic:
- They test a very different capability (steganography detection vs. encoding robustness)
- Tokenizers might handle them in ways that make them trivially detectable or completely undetectable
- They might not be fair tests of the curriculum's value

But I should be careful - this is about whether the experiment tests the claim, not about the claim itself. The claim is about generalization to unseen encoding families. Testing on very different encoding types is actually a strength of the experimental design. The risk is that the curriculum model fails on these, which would weaken H2 but shouldn't invalidate the paper if the mapping-function OOD results hold up. The real question is whether H2 needs to be broken into separate hypotheses.

Looking at other potential issues: the oracle reliability concern only matters for training data generation, since they use ground truth for evaluation. That's solid. But the FPR rollback mechanism needs clarification - what exactly does "revert" mean, and how often is FPR monitored? I'm also wondering about semantic...

The semantic deduplication threshold of 0.95 cosine similarity is underspecified - which embedding model are they using, and what's the computational cost? That's a minor point though.

On the domain generalization baseline issue, I'm realizing the authors' dismissal might be too quick. DRO, IRM, CORAL, and DANN are all actually applicable here if you treat encoding types as groups or environments. DRO could just upweight harder encoding types. DANN doesn't require differentiable input transformations - it operates on learned representations, so you could train a domain discriminator to predict encoding type from the model's internal representations and adversarially train to make those representations encoding-agnostic.

This is a real gap because the paper's central claim is about OOD generalization, and domain generalization methods are the standard toolkit for that problem. A reviewer would likely flag the missing Group DRO and DANN baselines as a significant oversight. I should also reconsider whether hypothesis 2 needs to be split - mapping-function OOD and encoding-principle OOD probably have different difficulty levels and deserve separate analysis.

There are a few other issues worth noting: hypothesis 3 doesn't clarify which classifier is being evaluated, latency and throughput should be included as formal metrics given the deployment claims, and the assumption that curriculum learning discards encoding information might not hold up - the model could still need that information for decoding. That last point is more about being careful with the narrative than a fundamental experimental flaw.

Looking at the overall design, I don't see any fatal flaws - these are all fixable issues. On the GRPO attacker side, the binary reward signal is quite sparse and could lead to training instability, though they do have a fallback mechanism. The bigger concern is how they're constraining the attacker to generate specific encoding types within a particular ECS range - that's underspecified and might require expensive rejection sampling to pull off effectively.

For the compute-matched baseline, redirecting the extra co-evolutionary compute into more static curriculum epochs is a bit questionable since the model would just be seeing the same data repeatedly rather than getting genuinely new training signal. And I'm still unclear on how whitespace steganography actually encodes harmful content into whitespace patterns - the mechanics of that need better explanation.

Now I'm realizing a critical issue: if the tokenizer normalizes whitespace or strips zero-width Unicode characters, those encoding families become undetectable regardless of the training approach, which would make the experiment unfair. The held-out OOD families really need validation that they're actually tokenizer-compatible and preserve the encoded signal. Beyond that, the proposal is solid but has a few gaps - the missing domain generalization baselines are the most serious concern, and there are some incomplete thoughts about H2 that need finishing. Both Group DRO and DANN are actually quite feasible to add—Group DRO just needs loss reweighting by encoding type, while DANN requires a gradient reversal layer and auxiliary classifier. Either would take about 6 hours of compute across multiple seeds, which fits within the timeline if I trim some writing time or use the buffer. The core issue is that the paper's arguments against domain generalization baselines are weak, and reviewers will expect at least one comparison to show the structural curriculum approach is genuinely better than existing methods.

Now I'm digging into the ECS metric definition more carefully. The weights are calibrated using Spearman correlation with classifier error, but there's a critical ambiguity: which classifier are they using to validate the metric? If it's an untrained classifier, the metric might not discriminate well; if it's a partially trained one, the correlations could shift during training; if it's the final trained model, that's circular reasoning. The weights should also be validated as stable across different models and training stages—if they drift significantly depending on which classifier you use, then the metric is model-dependent rather than measuring something intrinsic about the encodings.

I'm also noticing they don't explicitly address class balance in the training data. The co-evolutionary attacker generates harmful-encoded samples, but what's the ratio against benign prompts? They mention FPR rollback to prevent catastrophic false positive increases, but the base training should start with balanced data, and this should be specified clearly.

For the linear probing analysis, 900 samples (100 prompts × 9 variants) is borderline for reliable accuracy estimates. They should report confidence intervals or use cross-validation to strengthen those results.

So I'm looking at six concrete issues: missing domain generalization baselines like Group DRO and DANN is the most serious gap; tokenizer compatibility for the encoding families needs verification; hypothesis 2 should break down results by OOD level; hypothesis 3 and ECS need clarification on which classifier they're calibrating; latency and throughput benchmarks are absent; and the class balance during training isn't specified. The domain generalization baseline gap is the critical one—that could trigger rejection if not addressed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f04952e-3715-4774-b6dd-48e984860b3b",
  "isSidechain": false,
  "requestId": "req_011Cb6FRyNcFT4U22KM8JmaH",
  "type": "assistant",
  "uuid": "249a546a-a81f-4914-a163-fd2f22392ae4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c612cc08-f5d1-4069-9c04-c8d36ad8cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHqfrDwhEqVLpJijLTVsqM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5622,
      "cache_read_input_tokens": 13279,
      "output_tokens": 9001,
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
          "output_tokens": 9001,
          "cache_read_input_tokens": 13279,
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

_source line 9 · 2026-05-16T12:33:31.817Z_

# 补救 Agent 审查报告

【状态】: 有缺陷待补救

---

【缺陷 1】
- 类别: baseline 不足
- 问题: Proposal 在 Related Work 中以"非差分离散域"和"指数域组合"为由 dismiss 了所有 Domain Generalization (DG) 方法（IRM, DANN, CORAL, DRO），但这两条论据站不住脚。DANN 的 gradient reversal layer 作用在**表征空间**而非输入变换空间，完全不需要输入变换可微——只需将 encoding type 作为 domain label 即可训练 domain discriminator。Group DRO 更是仅需按 encoding type 分组重加权 loss，无任何额外架构改动。对于一篇核心 claim 是 OOD generalization 的论文，完全不提供任何 DG baseline 的实证对比，reviewer 几乎必然会要求补充。这是当前最大的 baseline 缺口。
- 严重度: 可补救
- 补救方案: 至少补两个 DG baseline——(1) **Group DRO**: 以 encoding type 为 group，按 worst-group loss 优化，同一 Qwen2.5-4B 架构，3 seeds，每 run ~8h，总增 6h wall-clock（4 GPU 并行）；(2) **DANN**: 加 gradient reversal layer + encoding-type auxiliary classifier，同样 3 seeds ~6h。两者均可在 Days 7-8 与 flat/reverse/static 并行训练，不影响关键路径。在 Related Work 中将论据从"不可应用"改为"可应用但我们实证表明 curriculum 优于 DG methods，因为 DG methods 缺乏对编码组合结构的利用"。

【缺陷 2】
- 类别: 实验设计不足
- 问题: Encoding-principle OOD 的两个 held-out 家族——whitespace steganography 和 zero-width Unicode encoding——存在 **tokenizer 兼容性风险**。Qwen2.5 的 tokenizer 极可能在 tokenization 阶段对空白符做归一化（多空格合并）、并完全丢弃 zero-width characters（U+200B, U+FEFF 等）。如果 tokenizer 在预处理阶段就把编码信号消除了，那么**任何**神经模型（包括 curriculum 和所有 baseline）都无法检测该编码，测试结果将是所有方法 ASR 接近 100%——这不能说明 curriculum 的泛化失败，而是测试本身无效。Proposal 中完全没有讨论这一风险，也没有提出 tokenizer 层面的验证步骤。
- 严重度: 可补救
- 补救方案: (1) **Day 1-2 新增 tokenizer 审计步骤**: 用 Qwen2.5 tokenizer 对 whitespace stego 和 zero-width Unicode 编码的样本做 tokenize → detokenize round-trip，检查编码信号是否保留。量化信息保留率（round-trip 后可恢复的 harmful content 比例）。(2) **如果信号被消除**: 替换为 tokenizer-compatible 的编码原理 OOD 家族，例如: (a) **Morse code encoding**（用点划线文本表示字符，tokenizer 不会消除），(b) **Phone keypad encoding**（T9 数字序列，结构上与 training 编码不同但 tokenizer 保留），(c) **Pig Latin 变体**（音节重排，结构不同于字符替换/移位）。(3) **如果信号部分保留**: 报告保留率，并在实验中将其作为 "partial-signal OOD" 分类讨论，而非与 mapping-function OOD 使用相同的成功阈值。

【缺陷 3】
- 类别: 实验设计不足
- 问题: H2 对 mapping-function OOD 和 encoding-principle OOD 使用**同一阈值**（≤30% ASR vs baseline ≥60%）。这两个 OOD 层级的难度差异本质上不同——mapping-function OOD 共享训练编码的结构原理（如 character substitution），而 encoding-principle OOD 基于全新的编码范式。用同一阈值要么导致：(a) 阈值对 mapping-function OOD 太宽松，无法展示真正的泛化强度；(b) 阈值对 encoding-principle OOD 太严格，curriculum 可能合理地无法达到 ≤30%，导致 H2 被判为"failed"——但这并不意味着 curriculum 没有价值，只是泛化边界在此处。一个混合的 H2 会让结果解读变得模糊。
- 严重度: 可补救
- 补救方案: 将 H2 拆为两个子假设: **H2a (Mapping-function OOD)**: Curriculum 在 same-principle OOD 上维持 ≤20% ASR（阈值更严，展示强泛化）。**H2b (Encoding-principle OOD)**: Curriculum 在 novel-principle OOD 上相对 baselines 有 ≥15pp 的 ASR 降低（使用相对改进而非绝对阈值，承认彻底泛化可能不成立，但 curriculum 仍优于替代方案）。分开报告、分开统计检验、分开讨论。这让论文的 claim 更精确、更难被 reviewer 以"H2 部分失败"为由攻击。

【缺陷 4】
- 类别: 评估方案缺陷
- 问题: H3 表述为"ECS correlates with classifier error (Spearman ρ ≥ 0.7) on held-out encodings"，但**没有指定是哪个 classifier 的 error**。这导致循环论证风险：如果用 curriculum-trained classifier 的 error 来验证 ECS，而 ECS 又被用来构建 curriculum 训练的顺序，因果关系不清。同样，ECS 权重的 pilot study 使用"classifier error rate"来校准权重，但也没说明是哪个 classifier——如果是一个随机初始化的 classifier，几乎所有编码都会导致高 error，区分度差；如果是最终训练好的 curriculum classifier，则权重对目标模型有依赖。
- 严重度: 可补救
- 补救方案: (1) **ECS 权重校准**: Pilot study 中使用一个 **minimally-trained baseline classifier**（如在少量 plaintext harmful/benign 数据上 fine-tune 几个 epoch 的 Qwen2.5-4B），测量其在不同编码下的 error rate，以此校准 ECS 权重。这个 classifier 足够有区分度（plaintext 训练意味着编码越复杂 error 越高），又不依赖 curriculum 训练过程。(2) **H3 验证**: 报告 ECS 与**至少两个不同 classifier** error 的相关性——(a) 上述 minimally-trained baseline，(b) random-order trained classifier，(c) curriculum-trained classifier。如果 ECS 与多个 classifier 的 error 都高度相关（尤其是与 curriculum 无关的 baseline），说明 ECS 捕捉的是编码固有难度，而非 curriculum 训练的产物。

【缺陷 5】
- 类别: 评估方案缺陷
- 问题: Proposal 的第四条 contribution 明确声称"Deployment-Practical Encoding Defense"，问题陈述中也以 cost ($0.01-0.03/input) 和 latency (1-3s) 对比 frontier LLM 来论证实用性。但 Evaluation Protocol 的 metrics 部分完全没有包含 **inference latency 和 throughput 的正式测量**。没有数据支撑的"deployment-practical" claim 会被 reviewer 质疑为 hand-waving。
- 严重度: 可补救
- 补救方案: 新增 metrics：(1) **Inference latency**: 在单 A100 上，batch size=1 和 batch size=32 下的 median 和 p99 latency（ms），对比 decode+LlamaGuard-3 pipeline 和 GPT-4 API。(2) **Throughput**: tokens/second 和 queries/second。(3) **Cost per query**: 基于 A100 租赁价格计算 per-query inference cost，与 GPT-4 API cost 对比。这些测量只需 ~1h computation，可在 Day 10-11 完成。

【缺陷 6】
- 类别: 实验设计不足
- 问题: 训练数据中 harmful-encoded 与 benign 样本的**比例（class balance）**完全没有说明。Co-evolutionary attacker 只生成 harmful-encoded 样本，如果不加控制，训练集会严重偏向 harmful 类，导致 FPR 升高。Proposal 提到 FPR rollback 作为安全网，但 rollback 是被动应急机制（已经开始 overfit 才触发），不能替代主动的 class balance 设计。Benign 数据的来源、数量、是否也进行 encoding augmentation 等细节均缺失。
- 严重度: 可补救
- 补救方案: 明确说明：(1) **Benign 数据来源和规模**: 例如 LMSYS-Chat-1M 中采样 N 条 benign 对话，WildGuardTest benign set 等。(2) **训练 batch 构成**: 每 batch 中 harmful-encoded : benign 的比例（推荐 1:1 或有文献支撑的比例）。(3) **Benign 数据是否也做 encoding augmentation**: 如果不做，classifier 可能学到"encoded = harmful"的 shortcut（凡是看起来像编码的都判 harmful）。应对 benign 样本也做一定比例的 encoding augmentation，防止 encoding 本身成为 harmful 的 proxy feature。这一点尤其关键——如果 benign 数据全是 plaintext，classifier 可能不是学会了"检测 harmful content regardless of encoding"，而是学会了"检测编码的存在"。这会导致 FPR 在 encoded-benign 输入上灾难性升高，而当前的 benign test set（WildGuardTest benign + LMSYS）看起来**全是 plaintext**，不会暴露这个问题。
  
  补充测试：新增 **encoded-benign evaluation**：对 500 条 benign prompts 做与 harmful 相同的 encoding augmentation（8 types × 选取子集），测量 FPR。如果 encoded-benign FPR 远高于 plaintext-benign FPR，说明 classifier 学到了 encoding-as-harmful shortcut，而非真正的 content extraction。

---

**总结**: 以上 6 个缺陷均可补救，无方向性致命问题。其中**缺陷 1（DG baseline 缺失）**和**缺陷 6（class balance + encoded-benign evaluation）**最为关键——前者是 reviewer 几乎必问的 baseline 问题，后者是一个实验设计上可能导致核心 claim 被根本性质疑的漏洞（classifier 可能只是在检测 encoding 的存在而非提取 harmful content）。建议优先处理这两个。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "249a546a-a81f-4914-a163-fd2f22392ae4",
  "isSidechain": false,
  "requestId": "req_011Cb6FRyNcFT4U22KM8JmaH",
  "type": "assistant",
  "uuid": "c55cb204-54ff-4e03-a135-c5727477fd31",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c612cc08-f5d1-4069-9c04-c8d36ad8cfa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHqfrDwhEqVLpJijLTVsqM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5622,
      "cache_read_input_tokens": 13279,
      "output_tokens": 9001,
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
          "output_tokens": 9001,
          "cache_read_input_tokens": 13279,
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

### Runtime record

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## Title  EncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training  ## Problem Statement  Encoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, an…",
  "leafUuid": "c55cb204-54ff-4e03-a135-c5727477fd31",
  "sessionId": "c612cc08-f5d1-4069-9c04-c8d36ad8cfa9"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "EncoGuard: Encoding-robust LLM safety via curriculum training",
  "sessionId": "c612cc08-f5d1-4069-9c04-c8d36ad8cfa9"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## Title  EncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training  ## Problem Statement  Encoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, an…",
  "leafUuid": "c55cb204-54ff-4e03-a135-c5727477fd31",
  "sessionId": "c612cc08-f5d1-4069-9c04-c8d36ad8cfa9"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "EncoGuard: Encoding-robust LLM safety via curriculum training",
  "sessionId": "c612cc08-f5d1-4069-9c04-c8d36ad8cfa9"
}
```

---
