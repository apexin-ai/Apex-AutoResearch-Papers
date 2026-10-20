# Research conversation: Title EncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training ## Problem Statement E

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/905ff011-121d-4414-b83a-6a85a0380894.jsonl`
- **Structured JSON:** [`f297441c45095898ecbc.json`](../../sessions/f2/f297441c45095898ecbc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T12:37:21.688Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:37:21.688Z",
  "sessionId": "905ff011-121d-4414-b83a-6a85a0380894",
  "content": "## Title\n\nEncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training\n\n## Problem Statement\n\nEncoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, and their nested compositions) exploit a fundamental vulnerability in LLM safety guardrails: classifiers trained on plaintext or limited encoding variations fail when inputs are transformed through unseen encoding schemes. Existing defenses have critical limitations:\n\n1. **Rule-based detection + decoding pipelines** (regex detection → known decoder → standard guardrail): Effective for known single-layer encodings with distinctive statistical signatures. Fail on: (a) partial encoding, (b) adversarial mixing of encoded/plaintext, (c) novel encodings without pre-programmed decoders.\n\n2. **Learned/LM-based canonicalization** (small LM decode → classify): Error propagation compounds across nesting layers; the canonicalizer itself becomes an adversarial attack surface; partial encoding requires semantic understanding to identify decode targets.\n\n3. **Frontier LLM zero-shot** (GPT-4/Claude prompted to detect harmful content regardless of encoding): Leverages pre-training exposure but impractical for deployment-scale guardrails ($0.01-0.03 per input, 1-3s latency vs. millisecond-level local inference).\n\nThe core challenge is achieving **generalization to unseen encoding families at deployment-practical cost**—a lightweight classifier that remains robust against encoding types never encountered during training.\n\n## Core Thesis\n\nWe hypothesize that a classifier trained via **complexity-structured curriculum**—where encoding attacks are presented in order of a principled complexity metric—acquires **encoding-robust content extraction capabilities** that generalize to held-out encoding types unseen during training.\n\n**Mechanism (Two-Regime, with Differential Prediction):**\n\n- **Low-ECS regime (simple encodings):** Content semantics remain partially accessible through tokenization. Curriculum forces the model to anchor harmful-content semantic features despite mild surface perturbation (**content anchoring**).\n\n- **High-ECS regime (complex/nested encodings):** Token-level content information is destroyed by multi-layer encoding. The model develops strategies for implicit decoding—recognizing encoding structure patterns and compositionally reconstructing content signal (**progressive decoding skill acquisition**).\n\n**Differential prediction distinguishing our mechanism from trivial catastrophic-interference prevention:** If the mechanism is progressive decoding skill acquisition (compositional skill building), curriculum's advantage over random-order should *increase with nesting depth* (deeper nesting requires more compositional decoding skill). If the mechanism is merely preventing catastrophic interference (protecting base content features), the advantage should be approximately uniform across nesting depths. We explicitly test this prediction.\n\n**Important clarification:** We do NOT claim literal \"encoding-invariant features\" in the information-theoretic sense (impossible for fully-scrambled sequences). Rather, curriculum builds a progressive hierarchy of decoding capabilities that transfers across encoding types sharing structural properties with training encodings. We explicitly characterize where this transfer succeeds (same encoding principle, different mapping) and where it reaches its limits (fundamentally different encoding paradigms)—establishing **scope conditions** for curriculum-induced generalization.\n\n## Relationship to Prior Work\n\n### Curriculum Adversarial Training\nCai et al. (IJCAI 2018): progressive perturbation magnitude for images. Wang et al. (NeurIPS 2021): ordered SGD by difficulty. Key differences:\n1. **Discrete compositional space vs. continuous perturbation:** Encoding attacks form a combinatorial space (N primitives × K nesting levels) requiring multi-dimensional complexity metrics, unlike scalar ε-balls.\n2. **OOD generalization vs. in-distribution robustness:** We explicitly test generalization to unseen encoding families, not just robustness to trained attack types.\n\n**Why curriculum works here but has mixed results elsewhere:** Encoding space possesses *intrinsic compositional structure with natural difficulty ordering*—nesting depth provides a non-arbitrary complexity axis. This contrasts with domains where curriculum orderings are artificial/researcher-imposed (known failure mode in curriculum literature).\n\n### Domain Generalization (DG)\nEach encoding type as a domain; OOD generalization ≈ DG to unseen domains. Standard DG methods (IRM, DANN, CORAL, DRO) ARE applicable to this setting (contrary to some claims about discrete spaces—DANN operates on representations, DRO on loss weighting). However, we hypothesize that **curriculum is superior to standard DG here** because DG methods treat domains as unstructured categories, while curriculum explicitly exploits the compositional complexity structure of the encoding space. We empirically validate this with Group DRO and DANN baselines.\n\n### Compositional Generalization\nThe encoding attack space (N primitives × K layers = O(N^K) compositions) is a discrete compositional transformation space, connecting to the compositional generalization literature (SCAN, COGS). Our work investigates whether structured curriculum can facilitate compositional generalization in transformation spaces—a question not addressed by prior compositional generalization work, which focuses on input-output mapping generalization rather than adversarial robustness.\n\n## Key Contributions\n\n1. **Primary Contribution (OOD Generalization + Scope Conditions):** Empirical demonstration that complexity-structured curriculum enables generalization to unseen encoding types at two levels—mapping-function OOD (strong transfer) and encoding-principle OOD (limited transfer, establishing scope conditions). Direct representation-level evidence (CKA + linear probing) + mechanistic differential prediction (nesting-depth-dependent advantage).\n\n2. **Encoding Complexity Score (ECS):** Formalized metric validated via cross-classifier correlation analysis; individual components quantified; shown to predict difficulty independently of training method.\n\n3. **Co-Evolutionary Training Framework:** GRPO attacker + SFT classifier with curriculum ordering, demonstrating co-evolution further improves upon static curriculum.\n\n4. **Deployment-Practical Encoding Defense:** 4B classifier achieving encoding robustness competitive with frontier LLM zero-shot at orders-of-magnitude lower latency and cost (quantified with formal inference benchmarks).\n\n## Methodology\n\n### Encoding Complexity Score (ECS)\n\n$$ECS(e) = \\alpha \\cdot \\text{NestingDepth}(e) + \\beta \\cdot \\text{CPT\\_Deviation}(e) + \\gamma \\cdot \\text{TokenizerPerplexity}(e)$$\n\n**Weight calibration:** Using a minimally-trained baseline classifier (Qwen2.5-4B fine-tuned only on plaintext harmful/benign data, ~1h training), measure each component's Spearman ρ with classifier error across 200 encoding variants. Weights set proportional to individual predictive power. This avoids circular dependency with curriculum training.\n\n**Component contribution analysis:** Report (a) single-component Spearman ρ, (b) leave-one-out ρ change, (c) composite vs. best single component. All computed on evaluation data without retraining.\n\n**Cross-classifier validation (H3):** Report ECS correlation with error rates from: (i) minimally-trained baseline, (ii) random-order trained classifier, (iii) curriculum-trained classifier. High correlation across all three demonstrates ECS captures intrinsic encoding difficulty, not training-method-specific difficulty.\n\n### Training Design\n\n**Attacker (Qwen2.5-1.5B, GRPO):**\n- Generates encoding attacks within current curriculum ECS band\n- Reward: +1 if bypasses classifier AND oracle confirms harmful\n- Entropy regularization prevents encoding-type collapse\n\n**Classifier (Qwen2.5-4B, SFT):**\n- Curriculum-ordered: Stage 1 (ECS ≤ threshold) → Stage 2 (ECS > threshold)\n- FPR rollback: revert if FPR > 2%\n- Semantic deduplication (cosine > 0.95)\n\n**Class Balance and Shortcut Prevention:**\n- Training batch composition: 50% harmful-encoded + 50% benign\n- **Critical:** Benign training data ALSO undergoes encoding augmentation (same encoding types and ECS distribution as harmful data). This prevents the classifier from learning \"encoded = harmful\" shortcut—it must learn to detect harmful *content* regardless of encoding, not merely detect encoding's *presence*.\n- Benign data source: LMSYS-Chat-1M (5K samples) + WildGuardTest benign (1K samples), encoded with same pipeline\n\n**Oracle:** GPT-4o + deterministic decoder cross-validation; disagreements excluded.\n\n**Fallback:** If co-evolutionary loop unstable by Day 7, switch to static curriculum SFT.\n\n### Baseline Definitions\n\n| Method | Data Source | Ordering | Key Variable | Seeds |\n|--------|------------|----------|--------------|-------|\n| **Curriculum (ours)** | Co-evolutionary/static, ECS-staged | Monotone ↑ ECS | — | 5 |\n| **Random-order** | Same data as curriculum | Shuffled | Ordering | 5 |\n| **Flat augmentation** | Uniform random encoding per prompt per epoch | Random | Data composition + ordering | 3 |\n| **Reverse curriculum** | Same data | Monotone ↓ ECS | Direction | 3 |\n| **Static curriculum** | Rule-based, ECS-ordered | Same as curriculum | Co-evolution effect | 3 |\n| **Group DRO** | Same data as flat | Worst-group (encoding type) loss | DG approach | 3 |\n| **DANN** | Same data as flat | Gradient reversal on encoding type | DG approach | 3 |\n| **Qwen2.5-1.5B decode → LlamaGuard-3** | N/A (inference) | N/A | Pipeline approach | 1 |\n| **Deterministic decode → LlamaGuard-3** | N/A (inference) | N/A | Rule-based pipeline | 1 |\n| **GPT-4 zero-shot** | N/A (API) | N/A | Cost/accuracy frontier | 1 |\n\nKey distinctions:\n- Random-order vs. Flat: Random-order = same data, shuffled (isolates ordering). Flat = uniform encoding sampling (different data distribution).\n- Group DRO / DANN: Standard DG methods using encoding type as domain label. Tests whether structured curriculum > unstructured domain-invariance objectives.\n\n### Compute Fairness\n\n- **H1-H3 (core claims):** Static curriculum vs. baselines. All use identical Qwen2.5-4B, identical training FLOPs (measured and reported), identical total steps. Variable: data ordering/composition/loss function.\n- **H4 (co-evolution, bonus):** Extra compute from attacker. Include compute-matched static variant (extra FLOPs → more training epochs) for fair comparison.\n- **Reporting:** Table with total classifier FLOPs, total system FLOPs (incl. attacker), wall-clock, training tokens per method.\n\n### Compute and Cost\n\n- Hardware: 4× A100 80GB\n- Per classifier run: ~8h\n- Total classifier runs: 5+5+3+3+3+3+3 = 25 runs → parallelized 4 at a time → ~50h\n- Attacker: 12h (2 rounds)\n- Oracle: ~18K calls ≈ $250\n- GPT-4 zero-shot eval: ~15K calls ≈ $150\n- Inference analyses (probing, CKA, latency): ~4h\n- Total: ~66h wall-clock training + evaluation\n\n## Experimental Design\n\n### Hypotheses\n\n- **H1 (Curriculum > Random):** Curriculum achieves ≥10pp lower encoding-ASR than random-order (95% bootstrap CI excludes 0, Cohen's d reported).\n- **H2a (Mapping-Function OOD):** Curriculum maintains ≤20% ASR on mapping-function OOD encodings (Braille, custom cipher, NATO phonetic) where baselines exceed 50%.\n- **H2b (Encoding-Principle OOD — Scope Condition):** On structurally different encoding principles (Pig Latin, T9 keypad), report curriculum vs. baselines gap. If curriculum outperforms by ≥15pp → evidence of broader generalization. If no significant difference → establishes scope boundary (curriculum generalizes within structural families, not across fundamentally different paradigms). Both outcomes are informative.\n- **H3 (ECS Predictiveness):** ECS correlates with error (Spearman ρ ≥ 0.7) across multiple classifiers; composite outperforms any single component.\n- **H4 (Co-evolution > Static, bonus):** Co-evolutionary > static by ≥5pp on composite encodings after compute normalization.\n\n**Differential Prediction (Mechanism Test):**\n- Partition test results by nesting depth (1, 2, 3)\n- Compute (curriculum ASR - random ASR) at each depth\n- Progressive decoding hypothesis → gap increases with depth\n- Catastrophic interference hypothesis → gap approximately constant\n- Report trend with significance test\n\n### Held-Out Encoding Families\n\n**Mapping-function OOD (same structural principle, different specific mapping):**\n- Braille Unicode substitution (character substitution — cf. homoglyphs)\n- Custom Caesar cipher with position-dependent shift (shift-based — cf. ROT13)\n- NATO phonetic alphabet (word-level substitution — novel granularity)\n- Morse code (symbolic encoding — cf. base64)\n\n**Encoding-principle OOD (boundary test — structurally different paradigm):**\n- Pig Latin variant (syllable rearrangement — morphological transformation, unlike any character/symbol substitution in training)\n- T9 phone keypad encoding (multi-character → single digit mapping with ambiguity — lossy encoding unlike all training encodings which are lossless)\n\n**Tokenizer Audit (Day 1-2):** Verify all held-out encodings survive tokenize → detokenize round-trip with information preservation rate ≥ 90%. Replace any encoding that fails this check.\n\n### Evaluation Protocol\n\n**External benchmarks (primary):**\n- HarmBench encoding-perturbed\n- JailbreakBench encoding subset\n- WildGuardTest encoding-perturbed\n\n**EncoAttack (supplementary):**\n- 500 base prompts: HarmBench (200) + AdvBench (150) + WildGuardTest (150)\n- 8 encoding types × 3 nesting levels = 12,000 test cases\n- Independent implementation from training pipeline\n- Validated ≥80% bypass on undefended LlamaGuard-3\n\n**Held-out encodings:** 6 families as above (4 mapping-function + 2 encoding-principle)\n\n**GPT-4 zero-shot reference:** Same test sets\n\n**Metrics:**\n- Encoding-ASR (primary)\n- **Clean FPR on plaintext benign** (WildGuardTest benign ~1000 + LMSYS-Chat-1M 1000)\n- **Encoded-benign FPR** (500 benign prompts × encoding augmented — CRITICAL: tests whether classifier detects harmful content vs. detects encoding presence)\n- FPR at multiple thresholds (0.5%, 1%, 2%, 5%) with Pareto frontier\n- Per-encoding-type breakdown\n- Nesting-depth-stratified curriculum advantage (differential prediction)\n- ECS correlation (composite + individual + cross-classifier)\n- Nesting-depth vs. decode-accuracy curve (error propagation for pipeline baselines)\n\n**Inference Performance:**\n- Latency: single A100, batch=1 and batch=32, median + p99 (ms)\n- Throughput: queries/second\n- Cost per query: based on A100 hourly rate vs. GPT-4 API\n- Compare: EncoGuard vs. Qwen-decode+LlamaGuard vs. GPT-4 zero-shot\n\n### Representation Analysis\n\n1. **CKA + Cosine Similarity:** 100 prompts × (plaintext + 8 encoding variants), penultimate-layer representations. Intra-prompt cross-encoding similarity: curriculum vs. baselines.\n\n2. **Linear Probing (Disentanglement):**\n   - Probe A: predict content category → curriculum should match or exceed baselines\n   - Probe B: predict encoding type → curriculum should show LOWER accuracy (encoding info discarded)\n   - Encoded-benign probing: verify that benign encoded inputs are NOT classified as harmful clusters\n\n3. **Learning Dynamics:** Per-checkpoint (500 steps) ASR curves, stratified by ECS level. Expected: curriculum shows staged convergence; random-order shows chaotic learning.\n\n### Statistical Rigor\n\n- Curriculum + random-order: 5 seeds each. Others: 3 seeds.\n- H1: 95% bootstrap CI on paired difference + Cohen's d\n- H2a/H2b: Reported with confidence intervals\n- Bonferroni correction for H1-H3 family\n- All results tables include mean ± std\n\n### Oracle Pilot (Day 1-2)\n\n100 samples per ECS band. GPT-4o + deterministic decoder agreement. < 80% → deterministic-only for that band.\n\n## Stability Mechanisms (Not Contributions)\n\n- Entropy regularization, FPR rollback, semantic deduplication\n- Trigger frequencies reported; full ablation in camera-ready\n\n## Acknowledged Limitations\n\n1. Full learned canonicalization (seq2seq) not trained as baseline; addressed via small-LM decode pipeline + nesting-depth error curve\n2. General principle validated only on encoding attacks; other compositional spaces = future work\n3. ECS weight sensitivity: ±20% perturbation in supplementary\n4. Encoding-principle OOD may show limited/no curriculum advantage—reported as scope condition\n\n## Timeline (17 days)\n\n**Phase 1: Setup + Pilot (Days 1-3)**\n- ECS implementation, encoding generators (all 6 held-out families), data pipeline\n- Tokenizer audit for all held-out encodings\n- Oracle pilot (100/band)\n- Fast pilot run (reduced data, 2h) → validate training dynamics, ECS threshold, class balance\n\n**Phase 2: Core Training (Days 4-9)**\n- Days 4-6: Curriculum (5 seeds) + random-order (5 seeds) [4 GPU parallel]\n- Days 7-8: Flat (3) + reverse (3) + Group DRO (3) + DANN (3) [parallel]\n- Day 9: Static curriculum (3) + compute-matched static (3) + co-evolutionary attempt\n\n**Phase 3: Evaluation + Analysis (Days 10-12)**\n- Day 10: Full benchmark eval + held-out + GPT-4 zero-shot + pipeline baselines\n- Day 11: Representation analysis + ECS stats + learning dynamics + encoded-benign eval\n- Day 12: Statistical tests, nesting-depth analysis, latency benchmarks, Pareto curves\n\n**Phase 4: Writing (Days 13-15)**\n- Drafting + figures + tables\n\n**Buffer (Days 16-17)**\n- Additional runs if needed, stability ablation, revision\n\n**Fallback:** Co-evolutionary unstable by Day 8 → focus H1-H3 with static curriculum."
}
```

---

### Runtime record

_source line 2 · 2026-05-16T12:37:21.693Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:37:21.693Z",
  "sessionId": "905ff011-121d-4414-b83a-6a85a0380894"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-16T12:37:21.708Z_

## Title

EncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training

## Problem Statement

Encoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, and their nested compositions) exploit a fundamental vulnerability in LLM safety guardrails: classifiers trained on plaintext or limited encoding variations fail when inputs are transformed through unseen encoding schemes. Existing defenses have critical limitations:

1. **Rule-based detection + decoding pipelines** (regex detection → known decoder → standard guardrail): Effective for known single-layer encodings with distinctive statistical signatures. Fail on: (a) partial encoding, (b) adversarial mixing of encoded/plaintext, (c) novel encodings without pre-programmed decoders.

2. **Learned/LM-based canonicalization** (small LM decode → classify): Error propagation compounds across nesting layers; the canonicalizer itself becomes an adversarial attack surface; partial encoding requires semantic understanding to identify decode targets.

3. **Frontier LLM zero-shot** (GPT-4/Claude prompted to detect harmful content regardless of encoding): Leverages pre-training exposure but impractical for deployment-scale guardrails ($0.01-0.03 per input, 1-3s latency vs. millisecond-level local inference).

The core challenge is achieving **generalization to unseen encoding families at deployment-practical cost**—a lightweight classifier that remains robust against encoding types never encountered during training.

## Core Thesis

We hypothesize that a classifier trained via **complexity-structured curriculum**—where encoding attacks are presented in order of a principled complexity metric—acquires **encoding-robust content extraction capabilities** that generalize to held-out encoding types unseen during training.

**Mechanism (Two-Regime, with Differential Prediction):**

- **Low-ECS regime (simple encodings):** Content semantics remain partially accessible through tokenization. Curriculum forces the model to anchor harmful-content semantic features despite mild surface perturbation (**content anchoring**).

- **High-ECS regime (complex/nested encodings):** Token-level content information is destroyed by multi-layer encoding. The model develops strategies for implicit decoding—recognizing encoding structure patterns and compositionally reconstructing content signal (**progressive decoding skill acquisition**).

**Differential prediction distinguishing our mechanism from trivial catastrophic-interference prevention:** If the mechanism is progressive decoding skill acquisition (compositional skill building), curriculum's advantage over random-order should *increase with nesting depth* (deeper nesting requires more compositional decoding skill). If the mechanism is merely preventing catastrophic interference (protecting base content features), the advantage should be approximately uniform across nesting depths. We explicitly test this prediction.

**Important clarification:** We do NOT claim literal "encoding-invariant features" in the information-theoretic sense (impossible for fully-scrambled sequences). Rather, curriculum builds a progressive hierarchy of decoding capabilities that transfers across encoding types sharing structural properties with training encodings. We explicitly characterize where this transfer succeeds (same encoding principle, different mapping) and where it reaches its limits (fundamentally different encoding paradigms)—establishing **scope conditions** for curriculum-induced generalization.

## Relationship to Prior Work

### Curriculum Adversarial Training
Cai et al. (IJCAI 2018): progressive perturbation magnitude for images. Wang et al. (NeurIPS 2021): ordered SGD by difficulty. Key differences:
1. **Discrete compositional space vs. continuous perturbation:** Encoding attacks form a combinatorial space (N primitives × K nesting levels) requiring multi-dimensional complexity metrics, unlike scalar ε-balls.
2. **OOD generalization vs. in-distribution robustness:** We explicitly test generalization to unseen encoding families, not just robustness to trained attack types.

**Why curriculum works here but has mixed results elsewhere:** Encoding space possesses *intrinsic compositional structure with natural difficulty ordering*—nesting depth provides a non-arbitrary complexity axis. This contrasts with domains where curriculum orderings are artificial/researcher-imposed (known failure mode in curriculum literature).

### Domain Generalization (DG)
Each encoding type as a domain; OOD generalization ≈ DG to unseen domains. Standard DG methods (IRM, DANN, CORAL, DRO) ARE applicable to this setting (contrary to some claims about discrete spaces—DANN operates on representations, DRO on loss weighting). However, we hypothesize that **curriculum is superior to standard DG here** because DG methods treat domains as unstructured categories, while curriculum explicitly exploits the compositional complexity structure of the encoding space. We empirically validate this with Group DRO and DANN baselines.

### Compositional Generalization
The encoding attack space (N primitives × K layers = O(N^K) compositions) is a discrete compositional transformation space, connecting to the compositional generalization literature (SCAN, COGS). Our work investigates whether structured curriculum can facilitate compositional generalization in transformation spaces—a question not addressed by prior compositional generalization work, which focuses on input-output mapping generalization rather than adversarial robustness.

## Key Contributions

1. **Primary Contribution (OOD Generalization + Scope Conditions):** Empirical demonstration that complexity-structured curriculum enables generalization to unseen encoding types at two levels—mapping-function OOD (strong transfer) and encoding-principle OOD (limited transfer, establishing scope conditions). Direct representation-level evidence (CKA + linear probing) + mechanistic differential prediction (nesting-depth-dependent advantage).

2. **Encoding Complexity Score (ECS):** Formalized metric validated via cross-classifier correlation analysis; individual components quantified; shown to predict difficulty independently of training method.

3. **Co-Evolutionary Training Framework:** GRPO attacker + SFT classifier with curriculum ordering, demonstrating co-evolution further improves upon static curriculum.

4. **Deployment-Practical Encoding Defense:** 4B classifier achieving encoding robustness competitive with frontier LLM zero-shot at orders-of-magnitude lower latency and cost (quantified with formal inference benchmarks).

## Methodology

### Encoding Complexity Score (ECS)

$$ECS(e) = \alpha \cdot \text{NestingDepth}(e) + \beta \cdot \text{CPT\_Deviation}(e) + \gamma \cdot \text{TokenizerPerplexity}(e)$$

**Weight calibration:** Using a minimally-trained baseline classifier (Qwen2.5-4B fine-tuned only on plaintext harmful/benign data, ~1h training), measure each component's Spearman ρ with classifier error across 200 encoding variants. Weights set proportional to individual predictive power. This avoids circular dependency with curriculum training.

**Component contribution analysis:** Report (a) single-component Spearman ρ, (b) leave-one-out ρ change, (c) composite vs. best single component. All computed on evaluation data without retraining.

**Cross-classifier validation (H3):** Report ECS correlation with error rates from: (i) minimally-trained baseline, (ii) random-order trained classifier, (iii) curriculum-trained classifier. High correlation across all three demonstrates ECS captures intrinsic encoding difficulty, not training-method-specific difficulty.

### Training Design

**Attacker (Qwen2.5-1.5B, GRPO):**
- Generates encoding attacks within current curriculum ECS band
- Reward: +1 if bypasses classifier AND oracle confirms harmful
- Entropy regularization prevents encoding-type collapse

**Classifier (Qwen2.5-4B, SFT):**
- Curriculum-ordered: Stage 1 (ECS ≤ threshold) → Stage 2 (ECS > threshold)
- FPR rollback: revert if FPR > 2%
- Semantic deduplication (cosine > 0.95)

**Class Balance and Shortcut Prevention:**
- Training batch composition: 50% harmful-encoded + 50% benign
- **Critical:** Benign training data ALSO undergoes encoding augmentation (same encoding types and ECS distribution as harmful data). This prevents the classifier from learning "encoded = harmful" shortcut—it must learn to detect harmful *content* regardless of encoding, not merely detect encoding's *presence*.
- Benign data source: LMSYS-Chat-1M (5K samples) + WildGuardTest benign (1K samples), encoded with same pipeline

**Oracle:** GPT-4o + deterministic decoder cross-validation; disagreements excluded.

**Fallback:** If co-evolutionary loop unstable by Day 7, switch to static curriculum SFT.

### Baseline Definitions

| Method | Data Source | Ordering | Key Variable | Seeds |
|--------|------------|----------|--------------|-------|
| **Curriculum (ours)** | Co-evolutionary/static, ECS-staged | Monotone ↑ ECS | — | 5 |
| **Random-order** | Same data as curriculum | Shuffled | Ordering | 5 |
| **Flat augmentation** | Uniform random encoding per prompt per epoch | Random | Data composition + ordering | 3 |
| **Reverse curriculum** | Same data | Monotone ↓ ECS | Direction | 3 |
| **Static curriculum** | Rule-based, ECS-ordered | Same as curriculum | Co-evolution effect | 3 |
| **Group DRO** | Same data as flat | Worst-group (encoding type) loss | DG approach | 3 |
| **DANN** | Same data as flat | Gradient reversal on encoding type | DG approach | 3 |
| **Qwen2.5-1.5B decode → LlamaGuard-3** | N/A (inference) | N/A | Pipeline approach | 1 |
| **Deterministic decode → LlamaGuard-3** | N/A (inference) | N/A | Rule-based pipeline | 1 |
| **GPT-4 zero-shot** | N/A (API) | N/A | Cost/accuracy frontier | 1 |

Key distinctions:
- Random-order vs. Flat: Random-order = same data, shuffled (isolates ordering). Flat = uniform encoding sampling (different data distribution).
- Group DRO / DANN: Standard DG methods using encoding type as domain label. Tests whether structured curriculum > unstructured domain-invariance objectives.

### Compute Fairness

- **H1-H3 (core claims):** Static curriculum vs. baselines. All use identical Qwen2.5-4B, identical training FLOPs (measured and reported), identical total steps. Variable: data ordering/composition/loss function.
- **H4 (co-evolution, bonus):** Extra compute from attacker. Include compute-matched static variant (extra FLOPs → more training epochs) for fair comparison.
- **Reporting:** Table with total classifier FLOPs, total system FLOPs (incl. attacker), wall-clock, training tokens per method.

### Compute and Cost

- Hardware: 4× A100 80GB
- Per classifier run: ~8h
- Total classifier runs: 5+5+3+3+3+3+3 = 25 runs → parallelized 4 at a time → ~50h
- Attacker: 12h (2 rounds)
- Oracle: ~18K calls ≈ $250
- GPT-4 zero-shot eval: ~15K calls ≈ $150
- Inference analyses (probing, CKA, latency): ~4h
- Total: ~66h wall-clock training + evaluation

## Experimental Design

### Hypotheses

- **H1 (Curriculum > Random):** Curriculum achieves ≥10pp lower encoding-ASR than random-order (95% bootstrap CI excludes 0, Cohen's d reported).
- **H2a (Mapping-Function OOD):** Curriculum maintains ≤20% ASR on mapping-function OOD encodings (Braille, custom cipher, NATO phonetic) where baselines exceed 50%.
- **H2b (Encoding-Principle OOD — Scope Condition):** On structurally different encoding principles (Pig Latin, T9 keypad), report curriculum vs. baselines gap. If curriculum outperforms by ≥15pp → evidence of broader generalization. If no significant difference → establishes scope boundary (curriculum generalizes within structural families, not across fundamentally different paradigms). Both outcomes are informative.
- **H3 (ECS Predictiveness):** ECS correlates with error (Spearman ρ ≥ 0.7) across multiple classifiers; composite outperforms any single component.
- **H4 (Co-evolution > Static, bonus):** Co-evolutionary > static by ≥5pp on composite encodings after compute normalization.

**Differential Prediction (Mechanism Test):**
- Partition test results by nesting depth (1, 2, 3)
- Compute (curriculum ASR - random ASR) at each depth
- Progressive decoding hypothesis → gap increases with depth
- Catastrophic interference hypothesis → gap approximately constant
- Report trend with significance test

### Held-Out Encoding Families

**Mapping-function OOD (same structural principle, different specific mapping):**
- Braille Unicode substitution (character substitution — cf. homoglyphs)
- Custom Caesar cipher with position-dependent shift (shift-based — cf. ROT13)
- NATO phonetic alphabet (word-level substitution — novel granularity)
- Morse code (symbolic encoding — cf. base64)

**Encoding-principle OOD (boundary test — structurally different paradigm):**
- Pig Latin variant (syllable rearrangement — morphological transformation, unlike any character/symbol substitution in training)
- T9 phone keypad encoding (multi-character → single digit mapping with ambiguity — lossy encoding unlike all training encodings which are lossless)

**Tokenizer Audit (Day 1-2):** Verify all held-out encodings survive tokenize → detokenize round-trip with information preservation rate ≥ 90%. Replace any encoding that fails this check.

### Evaluation Protocol

**External benchmarks (primary):**
- HarmBench encoding-perturbed
- JailbreakBench encoding subset
- WildGuardTest encoding-perturbed

**EncoAttack (supplementary):**
- 500 base prompts: HarmBench (200) + AdvBench (150) + WildGuardTest (150)
- 8 encoding types × 3 nesting levels = 12,000 test cases
- Independent implementation from training pipeline
- Validated ≥80% bypass on undefended LlamaGuard-3

**Held-out encodings:** 6 families as above (4 mapping-function + 2 encoding-principle)

**GPT-4 zero-shot reference:** Same test sets

**Metrics:**
- Encoding-ASR (primary)
- **Clean FPR on plaintext benign** (WildGuardTest benign ~1000 + LMSYS-Chat-1M 1000)
- **Encoded-benign FPR** (500 benign prompts × encoding augmented — CRITICAL: tests whether classifier detects harmful content vs. detects encoding presence)
- FPR at multiple thresholds (0.5%, 1%, 2%, 5%) with Pareto frontier
- Per-encoding-type breakdown
- Nesting-depth-stratified curriculum advantage (differential prediction)
- ECS correlation (composite + individual + cross-classifier)
- Nesting-depth vs. decode-accuracy curve (error propagation for pipeline baselines)

**Inference Performance:**
- Latency: single A100, batch=1 and batch=32, median + p99 (ms)
- Throughput: queries/second
- Cost per query: based on A100 hourly rate vs. GPT-4 API
- Compare: EncoGuard vs. Qwen-decode+LlamaGuard vs. GPT-4 zero-shot

### Representation Analysis

1. **CKA + Cosine Similarity:** 100 prompts × (plaintext + 8 encoding variants), penultimate-layer representations. Intra-prompt cross-encoding similarity: curriculum vs. baselines.

2. **Linear Probing (Disentanglement):**
   - Probe A: predict content category → curriculum should match or exceed baselines
   - Probe B: predict encoding type → curriculum should show LOWER accuracy (encoding info discarded)
   - Encoded-benign probing: verify that benign encoded inputs are NOT classified as harmful clusters

3. **Learning Dynamics:** Per-checkpoint (500 steps) ASR curves, stratified by ECS level. Expected: curriculum shows staged convergence; random-order shows chaotic learning.

### Statistical Rigor

- Curriculum + random-order: 5 seeds each. Others: 3 seeds.
- H1: 95% bootstrap CI on paired difference + Cohen's d
- H2a/H2b: Reported with confidence intervals
- Bonferroni correction for H1-H3 family
- All results tables include mean ± std

### Oracle Pilot (Day 1-2)

100 samples per ECS band. GPT-4o + deterministic decoder agreement. < 80% → deterministic-only for that band.

## Stability Mechanisms (Not Contributions)

- Entropy regularization, FPR rollback, semantic deduplication
- Trigger frequencies reported; full ablation in camera-ready

## Acknowledged Limitations

1. Full learned canonicalization (seq2seq) not trained as baseline; addressed via small-LM decode pipeline + nesting-depth error curve
2. General principle validated only on encoding attacks; other compositional spaces = future work
3. ECS weight sensitivity: ±20% perturbation in supplementary
4. Encoding-principle OOD may show limited/no curriculum advantage—reported as scope condition

## Timeline (17 days)

**Phase 1: Setup + Pilot (Days 1-3)**
- ECS implementation, encoding generators (all 6 held-out families), data pipeline
- Tokenizer audit for all held-out encodings
- Oracle pilot (100/band)
- Fast pilot run (reduced data, 2h) → validate training dynamics, ECS threshold, class balance

**Phase 2: Core Training (Days 4-9)**
- Days 4-6: Curriculum (5 seeds) + random-order (5 seeds) [4 GPU parallel]
- Days 7-8: Flat (3) + reverse (3) + Group DRO (3) + DANN (3) [parallel]
- Day 9: Static curriculum (3) + compute-matched static (3) + co-evolutionary attempt

**Phase 3: Evaluation + Analysis (Days 10-12)**
- Day 10: Full benchmark eval + held-out + GPT-4 zero-shot + pipeline baselines
- Day 11: Representation analysis + ECS stats + learning dynamics + encoded-benign eval
- Day 12: Statistical tests, nesting-depth analysis, latency benchmarks, Pareto curves

**Phase 4: Writing (Days 13-15)**
- Drafting + figures + tables

**Buffer (Days 16-17)**
- Additional runs if needed, stability ablation, revision

**Fallback:** Co-evolutionary unstable by Day 8 → focus H1-H3 with static curriculum.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "047dae7d-8979-4fd2-9094-8ed92aaa944e",
  "type": "user",
  "uuid": "a41a7142-8fe0-469c-9890-837c71701178",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "905ff011-121d-4414-b83a-6a85a0380894",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T12:37:21.707Z_

```json
{
  "parentUuid": "a41a7142-8fe0-469c-9890-837c71701178",
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
  "uuid": "21835515-55e4-4df2-a633-1e80e8a08d2d",
  "timestamp": "2026-05-16T12:37:21.707Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "905ff011-121d-4414-b83a-6a85a0380894",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T12:37:21.707Z_

```json
{
  "parentUuid": "21835515-55e4-4df2-a633-1e80e8a08d2d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a0cda084-c443-489c-a1d2-1239fa27d740",
  "timestamp": "2026-05-16T12:37:21.707Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "905ff011-121d-4414-b83a-6a85a0380894",
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
  "leafUuid": "a0cda084-c443-489c-a1d2-1239fa27d740",
  "sessionId": "905ff011-121d-4414-b83a-6a85a0380894"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "EncoGuard: Encoding-robust LLM defense via curriculum",
  "sessionId": "905ff011-121d-4414-b83a-6a85a0380894"
}
```

---

### Assistant

_source line 8 · 2026-05-16T12:38:29.773Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal as the "发掘 agent" (Discovery Agent). My job is to assess the idea's ceiling potential across three dimensions: Novelty, Significance, and Related Work differentiation. I need to be objective and focus only on the idea itself, not experimental design.

Let me first ask myself the two critical questions:

**1. Is there a trivial alternative that could achieve similar effects?**

The proposal is about training a classifier with curriculum learning (ordering by encoding complexity) to make it robust to unseen encoding-based jailbreaks. The trivial alternatives would be:


- Simply training on more diverse encodings (flat augmentation) — this is actually a baseline they include
- Using a deterministic decoder pipeline — they include this as a baseline
- Simply increasing model size — they address cost concerns

The key claim is that *ordering* matters, not just *exposure*. The random-order baseline directly tests this. However, there's a deeper concern: if you train on enough encoding types, does the ordering really matter? Curriculum learning literature shows mixed results—many papers find that random ordering works just as well with sufficient data. The proposal hinges on whether encoding space complexity actually benefits from structured progression, which isn't obviously true without seeing the results.

The core assumption is that encoding attacks have meaningful compositional structure that curriculum can exploit. This makes sense for nested encodings like base64(ROT13(x)) being harder than ROT13(x), but claiming this leads to generalization across unseen encoding families requires a stronger assumption: that decoding skills transfer meaningfully between different encoding types. That's the critical piece that needs validation.

Looking at novelty, curriculum learning for adversarial robustness isn't new, and applying it to encoding-based jailbreaks is somewhat incremental. The specific angle about compositional generalization through curriculum ordering is where the novelty lies.

On significance, encoding-based jailbreaks are a real problem, and testing on smaller models has practical deployment value. But there's a real arms race concern—once published, attackers will likely shift to entirely different attack vectors. The broader impact hinges on whether this curriculum-for-compositional-generalization approach generalizes to other domains, which the authors flag as future work.

The related work section does well distinguishing this from adversarial training approaches and domain generalization, and the compositional generalization angle feels genuinely novel.

But stepping back, the core mechanistic claim about "progressive decoding skill acquisition" is actually pretty vague. What are these skills exactly? If the model learns to recognize base64 byte patterns and decode them, that's a very specific skill that won't transfer to Braille substitution or other encoding schemes. The transfer mechanism needs a clearer theoretical foundation. And honestly, the most interesting finding might be buried—that curriculum helps within structural families but fails across different encoding paradigms. That's actually a sharp insight about the limits of compositional generalization.

The proposal could also lean harder into mechanistic interpretability by asking what circuits are being built during this curriculum learning process, rather than just treating it as an empirical phenomenon. And reframing the contribution as "curriculum learning for compositional generalization in discrete transformation spaces" feels like a bigger, more significant claim than just an encoding defense technique.

Looking more carefully, I see the paper already touches on compositional generalization, so let me think about what's genuinely novel here. The strongest angle seems to be that curriculum works specifically when the task space has intrinsic compositional hierarchy — this could become a real theoretical contribution about the conditions under which curriculum enables compositional generalization, rather than just "we applied curriculum to encoding attacks." Framing the encoding-principle OOD limitation as a positive finding about boundary conditions is also stronger than treating it as a weakness. And there's a real question worth investigating: would simply training on more encoding types at once eliminate the need for curriculum entirely? , does curriculum still matter? The proposal's claim is that ordering matters, but it's possible that with sufficient coverage, ordering becomes irrelevant. This is a real concern that could undermine the contribution.

Actually, wait. Let me reconsider. The proposal's core claim is about *generalization to unseen encodings*. If you just scale up coverage, you reduce the "unseen" space but never eliminate it. So curriculum is claimed to be better at generalizing to the remaining unseen types. This is a valid differentiation... but only if the held-out encodings are genuinely difficult to generalize to. If Braille substitution is basically the same as homoglyph substitution from the model's perspective, then generalization isn't surprising and doesn't require curriculum.

There's an interesting connection to in-context learning that the proposal overlooks. When curriculum trains the model to handle increasingly complex encodings, it might be building something like in-context learning — the model learns to recognize encoding patterns, internally decode them, and classify the content. This connects to how transformers implement algorithms and could strengthen the novelty claim.

Stepping back, I think this work has merit but sits at the borderline for EMNLP main conference. The core contribution is curriculum learning applied to encoding-based jailbreak defense with mechanistic analysis and scope conditions. The novelty is moderate — it's a solid application of an existing technique to a specific problem. The significance is moderate too — encoding jailbreaks matter but represent a somewhat narrow threat model. The execution looks strong, though that's not really my focus here.

The real question is whether the framing can be sharpened to make a broader scientific claim. I see three key angles: reframing this as a general finding about compositional generalization in discrete transformation spaces with encoding attacks as the case study, positioning the scope conditions as the headline finding rather than a limitation, and directly testing whether simply scaling model capacity with flat augmentation could achieve similar results.

There's also a credibility concern around whether a 4B model can actually learn to implicitly decode nested encodings like base64(ROT13(x)) in a single forward pass, given how dramatically base64 changes the token space. The model doesn't need perfect decoding, but I need to think through whether the mechanism I'm proposing is actually plausible at this scale.

Actually, the bar is much lower than full decoding — the model just needs to extract enough signal to distinguish harmful from benign content based on structural patterns in the encodings. That's learnable without understanding the full transformation. The encoded-benign test case already validates this distinction: if the model correctly classifies encoded-benign as benign rather than just flagging all encoded content as harmful, it's doing something beyond simple encoding detection.

This raises a potential novelty issue though — if the model is really just learning to pattern-match on encoding signatures correlated with harmful content rather than acquiring progressive decoding skills, the contribution becomes much more incremental. But the proposal's evaluation design actually addresses this concern, so I think the framing just needs to be more precise about what's actually happening.

The real opportunity here is to reframe the contribution around why curriculum learning specifically unlocks this capability compared to alternatives like scaling model size or adding more training data, and to position the scope conditions as a positive scientific finding rather than a limitation. There's also an underexplored connection to compositional generalization theory that could strengthen the theoretical grounding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0cda084-c443-489c-a1d2-1239fa27d740",
  "isSidechain": false,
  "requestId": "req_011Cb6G1UbBvkc4eEXsmXLxp",
  "type": "assistant",
  "uuid": "1dba050f-f229-4474-89a7-fd4b5d729efe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "905ff011-121d-4414-b83a-6a85a0380894",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCSLZjaqDGzMUfV2o8NtpM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5980,
      "cache_read_input_tokens": 13247,
      "output_tokens": 4235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5980,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4235,
          "cache_read_input_tokens": 13247,
          "cache_creation_input_tokens": 5980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5980
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

_source line 9 · 2026-05-16T12:39:12.001Z_

【状态】: 有发掘空间

---

【发掘点 1】
- 维度: significance 提升 / 核心 claim 强化
- 内容: 当前 framing 将论文定位为"encoding jailbreak 的防御方法"，但论文真正回答的科学问题更大：**"结构化 curriculum 何时能诱导离散组合变换空间中的 compositional generalization？"** Encoding attacks 只是这个问题的一个 case study。建议将 primary contribution 重新定位为：对这个更一般性问题给出实证回答（positive result within structural families + negative/limited result across paradigms），safety 应用是高价值 instantiation 而非目的本身。这样论文的 audience 从 safety 社区扩展到 representation learning + compositional generalization 社区，reviewer pool 中 "觉得这只是 engineering trick" 的概率显著降低。
- 价值: 命中 Significance。EMNLP main 的 bar 要求 general insight；当前 framing 太窄（只对 encoding jailbreak 有用），会被审稿人归类为 "application paper"。拓宽后 contribution 的 ceiling 提升一个 tier。

【发掘点 2】
- 维度: novelty 锐化
- 内容: 当前 proposal 的 differential prediction（curriculum advantage 随 nesting depth 增加 → 支持 progressive decoding 而非 catastrophic interference prevention）是 novelty 最锐利的点，但它被埋在 methodology 中。建议将其提升为 **论文的核心 scientific claim**："Curriculum induces compositional decoding skill building, not merely interference prevention—evidenced by depth-dependent advantage." 这个 claim 区别于所有已有 curriculum learning 工作（它们只证明 curriculum works，不区分 WHY it works）。如果 differential prediction 得到验证，这是对 curriculum learning mechanism 的 novel empirical insight，不仅限于 encoding 场景。
- 价值: 命中 Novelty。现有 curriculum learning 文献几乎没有 mechanistic explanation 的 empirical test。这个 differential prediction 从 "我们方法好" 升级为 "我们理解了为什么好"，直接回应 "why not just random order with more epochs" 的 reviewer challenge。

【发掘点 3】
- 维度: trivial alternative 威胁
- 内容: 论文未充分回应一个 trivial alternative：**如果将模型从 4B 放大到 7B/13B + flat augmentation，是否能匹配 4B + curriculum 的 OOD 性能？** 如果是，则 curriculum 的贡献退化为 "compute-efficiency trick"（降低发表价值）。论文需要明确其 claim 是 (a) curriculum 在同等模型规模下带来 fundamental generalization capability improvement（不可通过 scaling 替代），还是 (b) curriculum 是 efficiency method（同等性能用更小模型）。目前 proposal 暗示 (a) 但未排除 (b)。建议在 core thesis 中显式声明：curriculum exploits compositional structure that model scaling alone cannot discover without appropriate training signal ordering——并用 representation analysis (CKA/probing) 来区分 (curriculum 诱导出 qualitatively different representations, not just stronger versions of the same representations)。
- 价值: 命中 Novelty。如果审稿人认为 "你只是用了 curriculum 因为你 model 小，大模型不需要"，整个 novelty claim 崩塌。显式回应这个 alternative 并提供 representation-level 证据将堵住最危险的 review attack。

【发掘点 4】
- 维度: related work 差异化
- 内容: 论文与 compositional generalization 文献的连接目前停留在 surface level（"connecting to SCAN, COGS"）。但存在一个更直接相关的工作线：**meta-learning for compositional generalization**——如 Lake & Baroni (2018) 关于 systematic generalization、以及后续使用 meta-learning curriculum 来诱导 compositional skills 的工作（如 ICLR 2023 的 compositional generalization via meta-learning）。如果这些工作已经证明 structured training ordering 能帮助 compositional tasks，那本文的 novelty 需要更精确地定位：不是 "curriculum helps compositional generalization"（已知），而是 "在 adversarial robustness 的离散变换空间中，curriculum 的优势来源与 NLP compositional tasks 中的机制不同（decoding skill vs. syntactic rule generalization）"。
- 价值: 命中 Related Work 差异化。如果审稿人熟悉 compositional generalization + meta-learning 文献，缺乏对这条线的显式区分会被视为 insufficient awareness of related work，直接扣分。

【发掘点 5】
- 维度: 前提假设质疑
- 内容: 核心假设 "high-ECS regime 中 token-level content information is destroyed" 需要验证。如果 4B model 在 base64(ROT13(x)) 上确实无法从 token 层面获取任何 content signal，那它能通过 curriculum "学会 implicit decoding" 的假设依赖于一个未说明的前提：**训练数据中存在足够的中间复杂度样本来建立 decoding skill 的 gradient path**。但如果 ECS 空间中存在 "complexity cliff"（某个 nesting level 之后信息突然断崖式消失），curriculum 的 gradual 优势就不存在——模型在某个 threshold 以上无法学到任何东西，无论顺序如何。建议在 core thesis 中显式加入 **continuity assumption**: the encoding space provides a smooth difficulty gradient (no phase transition in extractable information). 并在 pilot phase 验证此假设（per-layer information retention measurement）。
- 价值: 命中 Novelty 的根基。如果这个 continuity assumption 不成立，整个 "progressive skill acquisition" 的机制故事崩塌，differential prediction 也失去诊断力。显式声明并验证此假设反而加强了论文的 scientific rigor，让审稿人无法用 "but what if the gradient isn't smooth" 来攻击。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dba050f-f229-4474-89a7-fd4b5d729efe",
  "isSidechain": false,
  "requestId": "req_011Cb6G1UbBvkc4eEXsmXLxp",
  "type": "assistant",
  "uuid": "548dc5c3-d3df-4606-9a57-0c7cebcd02fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "905ff011-121d-4414-b83a-6a85a0380894",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCSLZjaqDGzMUfV2o8NtpM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5980,
      "cache_read_input_tokens": 13247,
      "output_tokens": 4235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5980,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4235,
          "cache_read_input_tokens": 13247,
          "cache_creation_input_tokens": 5980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5980
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
  "leafUuid": "548dc5c3-d3df-4606-9a57-0c7cebcd02fd",
  "sessionId": "905ff011-121d-4414-b83a-6a85a0380894"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "EncoGuard: Encoding-robust LLM defense via curriculum",
  "sessionId": "905ff011-121d-4414-b83a-6a85a0380894"
}
```

---
