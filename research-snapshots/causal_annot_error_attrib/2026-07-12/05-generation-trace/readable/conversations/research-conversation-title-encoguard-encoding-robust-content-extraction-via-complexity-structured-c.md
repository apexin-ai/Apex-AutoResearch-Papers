# Research conversation: Title EncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training ## Problem Statement E

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/39ccf7db-6f91-457c-a309-3c70b4b82d47.jsonl`
- **Structured JSON:** [`88be47d461f0ba8d7da8.json`](../../sessions/88/88be47d461f0ba8d7da8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T12:37:21.549Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:37:21.549Z",
  "sessionId": "39ccf7db-6f91-457c-a309-3c70b4b82d47",
  "content": "## Title\n\nEncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training\n\n## Problem Statement\n\nEncoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, and their nested compositions) exploit a fundamental vulnerability in LLM safety guardrails: classifiers trained on plaintext or limited encoding variations fail when inputs are transformed through unseen encoding schemes. Existing defenses have critical limitations:\n\n1. **Rule-based detection + decoding pipelines** (regex detection → known decoder → standard guardrail): Effective for known single-layer encodings with distinctive statistical signatures. Fail on: (a) partial encoding, (b) adversarial mixing of encoded/plaintext, (c) novel encodings without pre-programmed decoders.\n\n2. **Learned/LM-based canonicalization** (small LM decode → classify): Error propagation compounds across nesting layers; the canonicalizer itself becomes an adversarial attack surface; partial encoding requires semantic understanding to identify decode targets.\n\n3. **Frontier LLM zero-shot** (GPT-4/Claude prompted to detect harmful content regardless of encoding): Leverages pre-training exposure but impractical for deployment-scale guardrails ($0.01-0.03 per input, 1-3s latency vs. millisecond-level local inference).\n\nThe core challenge is achieving **generalization to unseen encoding families at deployment-practical cost**—a lightweight classifier that remains robust against encoding types never encountered during training.\n\n## Core Thesis\n\nWe hypothesize that a classifier trained via **complexity-structured curriculum**—where encoding attacks are presented in order of a principled complexity metric—acquires **encoding-robust content extraction capabilities** that generalize to held-out encoding types unseen during training.\n\n**Mechanism (Two-Regime, with Differential Prediction):**\n\n- **Low-ECS regime (simple encodings):** Content semantics remain partially accessible through tokenization. Curriculum forces the model to anchor harmful-content semantic features despite mild surface perturbation (**content anchoring**).\n\n- **High-ECS regime (complex/nested encodings):** Token-level content information is destroyed by multi-layer encoding. The model develops strategies for implicit decoding—recognizing encoding structure patterns and compositionally reconstructing content signal (**progressive decoding skill acquisition**).\n\n**Differential prediction distinguishing our mechanism from trivial catastrophic-interference prevention:** If the mechanism is progressive decoding skill acquisition (compositional skill building), curriculum's advantage over random-order should *increase with nesting depth* (deeper nesting requires more compositional decoding skill). If the mechanism is merely preventing catastrophic interference (protecting base content features), the advantage should be approximately uniform across nesting depths. We explicitly test this prediction.\n\n**Important clarification:** We do NOT claim literal \"encoding-invariant features\" in the information-theoretic sense (impossible for fully-scrambled sequences). Rather, curriculum builds a progressive hierarchy of decoding capabilities that transfers across encoding types sharing structural properties with training encodings. We explicitly characterize where this transfer succeeds (same encoding principle, different mapping) and where it reaches its limits (fundamentally different encoding paradigms)—establishing **scope conditions** for curriculum-induced generalization.\n\n## Relationship to Prior Work\n\n### Curriculum Adversarial Training\nCai et al. (IJCAI 2018): progressive perturbation magnitude for images. Wang et al. (NeurIPS 2021): ordered SGD by difficulty. Key differences:\n1. **Discrete compositional space vs. continuous perturbation:** Encoding attacks form a combinatorial space (N primitives × K nesting levels) requiring multi-dimensional complexity metrics, unlike scalar ε-balls.\n2. **OOD generalization vs. in-distribution robustness:** We explicitly test generalization to unseen encoding families, not just robustness to trained attack types.\n\n**Why curriculum works here but has mixed results elsewhere:** Encoding space possesses *intrinsic compositional structure with natural difficulty ordering*—nesting depth provides a non-arbitrary complexity axis. This contrasts with domains where curriculum orderings are artificial/researcher-imposed (known failure mode in curriculum literature).\n\n### Domain Generalization (DG)\nEach encoding type as a domain; OOD generalization ≈ DG to unseen domains. Standard DG methods (IRM, DANN, CORAL, DRO) ARE applicable to this setting (contrary to some claims about discrete spaces—DANN operates on representations, DRO on loss weighting). However, we hypothesize that **curriculum is superior to standard DG here** because DG methods treat domains as unstructured categories, while curriculum explicitly exploits the compositional complexity structure of the encoding space. We empirically validate this with Group DRO and DANN baselines.\n\n### Compositional Generalization\nThe encoding attack space (N primitives × K layers = O(N^K) compositions) is a discrete compositional transformation space, connecting to the compositional generalization literature (SCAN, COGS). Our work investigates whether structured curriculum can facilitate compositional generalization in transformation spaces—a question not addressed by prior compositional generalization work, which focuses on input-output mapping generalization rather than adversarial robustness.\n\n## Key Contributions\n\n1. **Primary Contribution (OOD Generalization + Scope Conditions):** Empirical demonstration that complexity-structured curriculum enables generalization to unseen encoding types at two levels—mapping-function OOD (strong transfer) and encoding-principle OOD (limited transfer, establishing scope conditions). Direct representation-level evidence (CKA + linear probing) + mechanistic differential prediction (nesting-depth-dependent advantage).\n\n2. **Encoding Complexity Score (ECS):** Formalized metric validated via cross-classifier correlation analysis; individual components quantified; shown to predict difficulty independently of training method.\n\n3. **Co-Evolutionary Training Framework:** GRPO attacker + SFT classifier with curriculum ordering, demonstrating co-evolution further improves upon static curriculum.\n\n4. **Deployment-Practical Encoding Defense:** 4B classifier achieving encoding robustness competitive with frontier LLM zero-shot at orders-of-magnitude lower latency and cost (quantified with formal inference benchmarks).\n\n## Methodology\n\n### Encoding Complexity Score (ECS)\n\n$$ECS(e) = \\alpha \\cdot \\text{NestingDepth}(e) + \\beta \\cdot \\text{CPT\\_Deviation}(e) + \\gamma \\cdot \\text{TokenizerPerplexity}(e)$$\n\n**Weight calibration:** Using a minimally-trained baseline classifier (Qwen2.5-4B fine-tuned only on plaintext harmful/benign data, ~1h training), measure each component's Spearman ρ with classifier error across 200 encoding variants. Weights set proportional to individual predictive power. This avoids circular dependency with curriculum training.\n\n**Component contribution analysis:** Report (a) single-component Spearman ρ, (b) leave-one-out ρ change, (c) composite vs. best single component. All computed on evaluation data without retraining.\n\n**Cross-classifier validation (H3):** Report ECS correlation with error rates from: (i) minimally-trained baseline, (ii) random-order trained classifier, (iii) curriculum-trained classifier. High correlation across all three demonstrates ECS captures intrinsic encoding difficulty, not training-method-specific difficulty.\n\n### Training Design\n\n**Attacker (Qwen2.5-1.5B, GRPO):**\n- Generates encoding attacks within current curriculum ECS band\n- Reward: +1 if bypasses classifier AND oracle confirms harmful\n- Entropy regularization prevents encoding-type collapse\n\n**Classifier (Qwen2.5-4B, SFT):**\n- Curriculum-ordered: Stage 1 (ECS ≤ threshold) → Stage 2 (ECS > threshold)\n- FPR rollback: revert if FPR > 2%\n- Semantic deduplication (cosine > 0.95)\n\n**Class Balance and Shortcut Prevention:**\n- Training batch composition: 50% harmful-encoded + 50% benign\n- **Critical:** Benign training data ALSO undergoes encoding augmentation (same encoding types and ECS distribution as harmful data). This prevents the classifier from learning \"encoded = harmful\" shortcut—it must learn to detect harmful *content* regardless of encoding, not merely detect encoding's *presence*.\n- Benign data source: LMSYS-Chat-1M (5K samples) + WildGuardTest benign (1K samples), encoded with same pipeline\n\n**Oracle:** GPT-4o + deterministic decoder cross-validation; disagreements excluded.\n\n**Fallback:** If co-evolutionary loop unstable by Day 7, switch to static curriculum SFT.\n\n### Baseline Definitions\n\n| Method | Data Source | Ordering | Key Variable | Seeds |\n|--------|------------|----------|--------------|-------|\n| **Curriculum (ours)** | Co-evolutionary/static, ECS-staged | Monotone ↑ ECS | — | 5 |\n| **Random-order** | Same data as curriculum | Shuffled | Ordering | 5 |\n| **Flat augmentation** | Uniform random encoding per prompt per epoch | Random | Data composition + ordering | 3 |\n| **Reverse curriculum** | Same data | Monotone ↓ ECS | Direction | 3 |\n| **Static curriculum** | Rule-based, ECS-ordered | Same as curriculum | Co-evolution effect | 3 |\n| **Group DRO** | Same data as flat | Worst-group (encoding type) loss | DG approach | 3 |\n| **DANN** | Same data as flat | Gradient reversal on encoding type | DG approach | 3 |\n| **Qwen2.5-1.5B decode → LlamaGuard-3** | N/A (inference) | N/A | Pipeline approach | 1 |\n| **Deterministic decode → LlamaGuard-3** | N/A (inference) | N/A | Rule-based pipeline | 1 |\n| **GPT-4 zero-shot** | N/A (API) | N/A | Cost/accuracy frontier | 1 |\n\nKey distinctions:\n- Random-order vs. Flat: Random-order = same data, shuffled (isolates ordering). Flat = uniform encoding sampling (different data distribution).\n- Group DRO / DANN: Standard DG methods using encoding type as domain label. Tests whether structured curriculum > unstructured domain-invariance objectives.\n\n### Compute Fairness\n\n- **H1-H3 (core claims):** Static curriculum vs. baselines. All use identical Qwen2.5-4B, identical training FLOPs (measured and reported), identical total steps. Variable: data ordering/composition/loss function.\n- **H4 (co-evolution, bonus):** Extra compute from attacker. Include compute-matched static variant (extra FLOPs → more training epochs) for fair comparison.\n- **Reporting:** Table with total classifier FLOPs, total system FLOPs (incl. attacker), wall-clock, training tokens per method.\n\n### Compute and Cost\n\n- Hardware: 4× A100 80GB\n- Per classifier run: ~8h\n- Total classifier runs: 5+5+3+3+3+3+3 = 25 runs → parallelized 4 at a time → ~50h\n- Attacker: 12h (2 rounds)\n- Oracle: ~18K calls ≈ $250\n- GPT-4 zero-shot eval: ~15K calls ≈ $150\n- Inference analyses (probing, CKA, latency): ~4h\n- Total: ~66h wall-clock training + evaluation\n\n## Experimental Design\n\n### Hypotheses\n\n- **H1 (Curriculum > Random):** Curriculum achieves ≥10pp lower encoding-ASR than random-order (95% bootstrap CI excludes 0, Cohen's d reported).\n- **H2a (Mapping-Function OOD):** Curriculum maintains ≤20% ASR on mapping-function OOD encodings (Braille, custom cipher, NATO phonetic) where baselines exceed 50%.\n- **H2b (Encoding-Principle OOD — Scope Condition):** On structurally different encoding principles (Pig Latin, T9 keypad), report curriculum vs. baselines gap. If curriculum outperforms by ≥15pp → evidence of broader generalization. If no significant difference → establishes scope boundary (curriculum generalizes within structural families, not across fundamentally different paradigms). Both outcomes are informative.\n- **H3 (ECS Predictiveness):** ECS correlates with error (Spearman ρ ≥ 0.7) across multiple classifiers; composite outperforms any single component.\n- **H4 (Co-evolution > Static, bonus):** Co-evolutionary > static by ≥5pp on composite encodings after compute normalization.\n\n**Differential Prediction (Mechanism Test):**\n- Partition test results by nesting depth (1, 2, 3)\n- Compute (curriculum ASR - random ASR) at each depth\n- Progressive decoding hypothesis → gap increases with depth\n- Catastrophic interference hypothesis → gap approximately constant\n- Report trend with significance test\n\n### Held-Out Encoding Families\n\n**Mapping-function OOD (same structural principle, different specific mapping):**\n- Braille Unicode substitution (character substitution — cf. homoglyphs)\n- Custom Caesar cipher with position-dependent shift (shift-based — cf. ROT13)\n- NATO phonetic alphabet (word-level substitution — novel granularity)\n- Morse code (symbolic encoding — cf. base64)\n\n**Encoding-principle OOD (boundary test — structurally different paradigm):**\n- Pig Latin variant (syllable rearrangement — morphological transformation, unlike any character/symbol substitution in training)\n- T9 phone keypad encoding (multi-character → single digit mapping with ambiguity — lossy encoding unlike all training encodings which are lossless)\n\n**Tokenizer Audit (Day 1-2):** Verify all held-out encodings survive tokenize → detokenize round-trip with information preservation rate ≥ 90%. Replace any encoding that fails this check.\n\n### Evaluation Protocol\n\n**External benchmarks (primary):**\n- HarmBench encoding-perturbed\n- JailbreakBench encoding subset\n- WildGuardTest encoding-perturbed\n\n**EncoAttack (supplementary):**\n- 500 base prompts: HarmBench (200) + AdvBench (150) + WildGuardTest (150)\n- 8 encoding types × 3 nesting levels = 12,000 test cases\n- Independent implementation from training pipeline\n- Validated ≥80% bypass on undefended LlamaGuard-3\n\n**Held-out encodings:** 6 families as above (4 mapping-function + 2 encoding-principle)\n\n**GPT-4 zero-shot reference:** Same test sets\n\n**Metrics:**\n- Encoding-ASR (primary)\n- **Clean FPR on plaintext benign** (WildGuardTest benign ~1000 + LMSYS-Chat-1M 1000)\n- **Encoded-benign FPR** (500 benign prompts × encoding augmented — CRITICAL: tests whether classifier detects harmful content vs. detects encoding presence)\n- FPR at multiple thresholds (0.5%, 1%, 2%, 5%) with Pareto frontier\n- Per-encoding-type breakdown\n- Nesting-depth-stratified curriculum advantage (differential prediction)\n- ECS correlation (composite + individual + cross-classifier)\n- Nesting-depth vs. decode-accuracy curve (error propagation for pipeline baselines)\n\n**Inference Performance:**\n- Latency: single A100, batch=1 and batch=32, median + p99 (ms)\n- Throughput: queries/second\n- Cost per query: based on A100 hourly rate vs. GPT-4 API\n- Compare: EncoGuard vs. Qwen-decode+LlamaGuard vs. GPT-4 zero-shot\n\n### Representation Analysis\n\n1. **CKA + Cosine Similarity:** 100 prompts × (plaintext + 8 encoding variants), penultimate-layer representations. Intra-prompt cross-encoding similarity: curriculum vs. baselines.\n\n2. **Linear Probing (Disentanglement):**\n   - Probe A: predict content category → curriculum should match or exceed baselines\n   - Probe B: predict encoding type → curriculum should show LOWER accuracy (encoding info discarded)\n   - Encoded-benign probing: verify that benign encoded inputs are NOT classified as harmful clusters\n\n3. **Learning Dynamics:** Per-checkpoint (500 steps) ASR curves, stratified by ECS level. Expected: curriculum shows staged convergence; random-order shows chaotic learning.\n\n### Statistical Rigor\n\n- Curriculum + random-order: 5 seeds each. Others: 3 seeds.\n- H1: 95% bootstrap CI on paired difference + Cohen's d\n- H2a/H2b: Reported with confidence intervals\n- Bonferroni correction for H1-H3 family\n- All results tables include mean ± std\n\n### Oracle Pilot (Day 1-2)\n\n100 samples per ECS band. GPT-4o + deterministic decoder agreement. < 80% → deterministic-only for that band.\n\n## Stability Mechanisms (Not Contributions)\n\n- Entropy regularization, FPR rollback, semantic deduplication\n- Trigger frequencies reported; full ablation in camera-ready\n\n## Acknowledged Limitations\n\n1. Full learned canonicalization (seq2seq) not trained as baseline; addressed via small-LM decode pipeline + nesting-depth error curve\n2. General principle validated only on encoding attacks; other compositional spaces = future work\n3. ECS weight sensitivity: ±20% perturbation in supplementary\n4. Encoding-principle OOD may show limited/no curriculum advantage—reported as scope condition\n\n## Timeline (17 days)\n\n**Phase 1: Setup + Pilot (Days 1-3)**\n- ECS implementation, encoding generators (all 6 held-out families), data pipeline\n- Tokenizer audit for all held-out encodings\n- Oracle pilot (100/band)\n- Fast pilot run (reduced data, 2h) → validate training dynamics, ECS threshold, class balance\n\n**Phase 2: Core Training (Days 4-9)**\n- Days 4-6: Curriculum (5 seeds) + random-order (5 seeds) [4 GPU parallel]\n- Days 7-8: Flat (3) + reverse (3) + Group DRO (3) + DANN (3) [parallel]\n- Day 9: Static curriculum (3) + compute-matched static (3) + co-evolutionary attempt\n\n**Phase 3: Evaluation + Analysis (Days 10-12)**\n- Day 10: Full benchmark eval + held-out + GPT-4 zero-shot + pipeline baselines\n- Day 11: Representation analysis + ECS stats + learning dynamics + encoded-benign eval\n- Day 12: Statistical tests, nesting-depth analysis, latency benchmarks, Pareto curves\n\n**Phase 4: Writing (Days 13-15)**\n- Drafting + figures + tables\n\n**Buffer (Days 16-17)**\n- Additional runs if needed, stability ablation, revision\n\n**Fallback:** Co-evolutionary unstable by Day 8 → focus H1-H3 with static curriculum."
}
```

---

### Runtime record

_source line 2 · 2026-05-16T12:37:21.555Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:37:21.555Z",
  "sessionId": "39ccf7db-6f91-457c-a309-3c70b4b82d47"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T12:37:21.581Z_

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
  "promptId": "dd30cf82-b69c-4a46-9de5-aeddb8088ad9",
  "type": "user",
  "uuid": "363eaff7-e5ea-4279-b85d-0f301b761018",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "39ccf7db-6f91-457c-a309-3c70b4b82d47",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T12:37:21.580Z_

```json
{
  "parentUuid": "363eaff7-e5ea-4279-b85d-0f301b761018",
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
  "uuid": "117503c7-4d08-4136-a3e3-1127997800bc",
  "timestamp": "2026-05-16T12:37:21.580Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "39ccf7db-6f91-457c-a309-3c70b4b82d47",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T12:37:21.580Z_

```json
{
  "parentUuid": "117503c7-4d08-4136-a3e3-1127997800bc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "12af67df-20e5-4e69-9132-c472f233ac8d",
  "timestamp": "2026-05-16T12:37:21.580Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "39ccf7db-6f91-457c-a309-3c70b4b82d47",
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
  "leafUuid": "12af67df-20e5-4e69-9132-c472f233ac8d",
  "sessionId": "39ccf7db-6f91-457c-a309-3c70b4b82d47"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "EncoGuard: Curriculum learning for encoding-robust content extraction",
  "sessionId": "39ccf7db-6f91-457c-a309-3c70b4b82d47"
}
```

---

### Assistant

_source line 8 · 2026-05-16T12:38:32.417Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal from the perspective of experimental design and technical execution completeness. I need to evaluate:

1. Baseline coverage
2. Experimental design rigor
3. Evaluation metrics
4. Ablation design
5. Feasibility (compute, data, time, etc.)
6. Compute-normalized comparisons

Let me go through this systematically.

**Baseline Coverage:**
The baselines are quite comprehensive:
- Curriculum (ours) - 5 seeds
- Random-order (same data, shuffled) - 5 seeds - isolates ordering effect


- Flat augmentation (uniform random encoding) - 3 seeds - different data composition
- Reverse curriculum - 3 seeds - tests direction
- Static curriculum - 3 seeds - isolates co-evolution
- Group DRO - 3 seeds - standard DG baseline
- DANN - 3 seeds - standard DG baseline
- Qwen2.5-1.5B decode → LlamaGuard-3 - pipeline approach
- Deterministic decode → LlamaGuard-3 - rule-based pipeline
- GPT-4 zero-shot - cost/accuracy frontier

This is actually very solid. The baselines isolate ordering effects, direction effects, and data composition effects while also covering standard domain generalization approaches and practical pipeline alternatives.

I'm thinking through what might be missing—a standard adversarial training baseline without curriculum ordering, though flat augmentation partially covers that. IRM isn't included but they justify focusing on Group DRO and DANN instead. An ensemble approach could be interesting, and I'm wondering whether testing LlamaGuard-3 directly on encoded inputs without any decoding would be useful as a baseline, though the existing results already show they achieve ≥80% bypass rates on undefended LlamaGuard.

The experimental design looks solid—the differential prediction test cleanly separates mechanisms, the two levels of OOD distribution shift are thoughtfully structured, and the scope conditions framing for the second hypothesis is clever since both outcomes would be informative. The encoded-benign false positive rate test is essential and properly included, and using class balance with encoded benign data prevents the model from learning shortcuts.

For evaluation, they're using multiple external benchmarks across HarmBench, JailbreakBench, and WildGuardTest, plus their internal EncoAttack with proper validation. The metrics are comprehensive—false positive rates at different thresholds, inference speed comparisons, and representation analysis through CKA and linear probing. The ablation structure already functions as a natural ablation by isolating ordering effects through curriculum versus random ordering, and they're examining the ECS component separately.

They're also planning component-level analysis with leave-one-out testing and stratifying by nesting depth to understand learning dynamics. The feasibility looks reasonable—4 A100s is manageable for an academic setting, the 17-day timeline is tight but doable, oracle costs are around $400, and they can parallelize the 25 classifier runs across the available GPUs.

But I'm spotting some issues. The compute fairness claim for Group DRO and DANN isn't explicit—Group DRO's worst-group loss might change training dynamics, and DANN adds a domain discriminator that could affect the FLOP count. This needs clarification on whether they're truly equitable comparisons. Also, the seeding strategy for the pipeline isn't fully specified yet. baselines and GPT-4**: Only 1 seed each. For deterministic methods this makes sense, but for the Qwen decode pipeline, there could be variance. However, this is inference-only, so 1 "seed" might be fine if the models are fixed.

3. **Data size**: The proposal mentions 500 base prompts for EncoAttack (200 HarmBench + 150 AdvBench + 150 WildGuardTest). For training, it mentions "5K samples from LMSYS-Chat-1M + 1K from WildGuardTest benign" for benign data. But what about harmful training data size? The attacker generates it, but what's the approximate volume? This could affect reproducibility.

4. **Timeline tightness**: 17 days is very tight. Phase 2 (Days 4-9) needs to run 25 classifier runs on 4 GPUs—that's roughly 50 hours of compute spread across 6 days with 576 GPU-hours available versus 200 GPU-hours needed. It's technically feasible but doesn't leave much buffer for failures or reruns.

5. **DANN implementation detail**: DANN requires gradient reversal on "encoding type" as domain label, but encoding type changes during curriculum training. The proposal clarifies this by using flat data for DANN, which is fair and consistent.

6. **Oracle reliability**: GPT-4o + deterministic decoder cross-validation excludes disagreements, but I'm wondering what percentage of data gets filtered out. If it's substantial (over 20%), the remaining dataset could become skewed. The pilot tested 100 samples per encoding type, but I need to see how much data actually survives the filtering process.

7. **Encoded-benign FPR estimation**: With only 500 benign samples across augmented encodings, estimating FPR at very low thresholds (0.5%) becomes noisy—a single false positive represents 0.2% FPR, making it hard to distinguish signal from noise at that precision level.

8. **Statistical power concerns**: The nesting-depth analysis splits test data into 3 depth levels, but the proposal doesn't specify how many test cases fall into each level. With limited samples per depth, trend significance tests could be underpowered.

9. **Linear probing assumption**: The proposal expects curriculum training to lower encoding-type prediction accuracy, assuming the curriculum discards encoding information. But there's another possibility—the curriculum might retain encoding information while also learning other features, which would complicate the interpretation.

10. **Curriculum staging threshold sensitivity**: The proposal discusses ECS weight perturbations but doesn't address sensitivity to the threshold that triggers transitions between curriculum stages. How is this threshold determined, and does it affect robustness?

11. **Attacker capacity relative to classifier**: The 1.5B attacker model is smaller than the 4B classifier. While this could be a limitation for generating challenging attacks, the fact that the attacker only produces encoding schemes rather than free-form adversarial examples might make the size difference less critical.

12. **Primary hypothesis failure**: The proposal includes a fallback for co-evolution instability but doesn't address what happens if the core hypothesis doesn't hold, though that's reasonable for a proposal stage.

Overall, this is a remarkably thorough experimental design with comprehensive baselines, detailed ablations, and well-chosen evaluation metrics. The main substantive concerns are the compute fairness issue with DANN's gradient reversal layer, the sample size for low-threshold FPR measurements, the curriculum threshold sensitivity, and the statistical power for detecting nesting-depth trends. Most of these are addressable, and the proposal's feasibility looks solid.

The DANN fairness question is the stickiest one—the proposal commits to identical training FLOPs across all methods, but DANN's discriminator head adds both parameters and computational cost. The proposal needs to clarify whether the discriminator's FLOPs are included in that budget or excluded, since either choice creates a fairness problem: including them means DANN gets less capacity than the baselines, excluding them violates the identical-FLOPs constraint. Group DRO doesn't have this issue since it just changes the loss function while keeping the architecture identical.

Now I'm noticing another gap: the proposal describes testing on held-out encoding types but doesn't explicitly specify which encodings appear in the training set versus which are reserved for evaluation. It mentions base64, ROT13, homoglyph substitution and their nested compositions in the problem statement, and references "8 encoding types × 3 nesting levels" for the attack evaluation, but the actual training/test split isn't clearly laid out.

Looking at the held-out families section, I can see what's excluded (Braille, custom Caesar, NATO, Morse for mapping-function OOD; Pig Latin, T9 for encoding-principle OOD), which implies the training set uses the other encodings, but this should be stated more directly. It's more of a clarity issue in the writeup than a fundamental experimental problem.

The 17-day timeline is tight—setup and pilot take the first three days, then five days for 25 training runs, three days for evaluation and analysis, three days for writing, and a two-day buffer. The training phase is the constraint here, and I need to think through whether that's realistic given the computational requirements.

The experimental design is actually quite solid overall. The issues I'm identifying are all fixable. Let me prioritize them: the DANN compute fairness concern is the most significant, followed by the statistical power question for nesting-depth differential prediction, then the encoded-benign FPR sample size, the ECS staging threshold sensitivity, and finally the explicit specification of the training encoding set. I should structure my feedback around these points, noting that the proposal is already close to main conference quality despite these remediable gaps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12af67df-20e5-4e69-9132-c472f233ac8d",
  "isSidechain": false,
  "requestId": "req_011Cb6G1U3wdhhNEzL1UBatN",
  "type": "assistant",
  "uuid": "5f334161-c896-4287-bd20-20bed8ec053e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "39ccf7db-6f91-457c-a309-3c70b4b82d47",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XS4C9ZG7jupFcUrwAHmNin",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5980,
      "cache_read_input_tokens": 13279,
      "output_tokens": 5299,
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
          "output_tokens": 5299,
          "cache_read_input_tokens": 13279,
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

_source line 9 · 2026-05-16T12:39:21.822Z_

【状态】: 有缺陷待补救

---

整体评估：本 proposal 的实验设计已经接近 EMNLP 主会水准——baseline 覆盖面广且隔离变量清晰、ablation 通过对比结构自然实现、评估方案多维度覆盖、可行性大致合理。以下缺陷均为可补救的细节问题，修补后实验设计可达到主会投稿的 solid 水平。

---

【缺陷 1】
- 类别: compute 公平性问题
- 问题: DANN baseline 引入了额外的 domain discriminator 网络和 gradient reversal layer，带来额外参数和 FLOPs。Proposal 在 Compute Fairness 部分声明"All use identical Qwen2.5-4B, identical training FLOPs"，但未说明 DANN discriminator head 的额外计算如何处理。Reviewer 会质疑：如果 DANN 多花了 FLOPs 在 discriminator 上仍不如 curriculum，是 DANN 方法弱还是 compute 不公平？如果不计 discriminator FLOPs，那 DANN 实际上获得了"免费"额外参数。
- 严重度: 可补救
- 补救方案: 在 Compute Fairness 小节明确说明：(a) DANN discriminator head 参数量相对 4B classifier 可忽略（量化：discriminator 约占总参数 <0.5%），因此统一按 classifier backbone forward/backward FLOPs 计算；(b) 额外报告 DANN total FLOPs（含 discriminator）作为 transparency，让 reviewer 自行判断。一句话即可解决。

---

【缺陷 2】
- 类别: 实验设计不足
- 问题: Differential prediction（核心机制验证）将测试数据按 nesting depth 分为 3 层（depth 1, 2, 3），然后检验 (curriculum ASR − random ASR) 随 depth 的递增趋势。但 proposal 未说明每个 depth 层的测试样本量。若 EncoAttack 的 12,000 test cases 按 8 types × 3 depths 分配，每个 depth 约 4,000 cases，但这是总计——每个 type×depth cell 仅约 167 cases（500 base prompts ÷ 3 depths）。更关键的是，趋势检验（3 个数据点的单调性）统计效力天然较弱，3 点线性回归的 p-value 很难达到显著水平。这是 proposal 的核心 claim 之一，统计支撑需要更强。
- 严重度: 可补救
- 补救方案: (1) 增加 nesting depth 到 4-5 层（至少 4 个数据点），提升趋势检验的统计效力；(2) 在 Statistical Rigor 部分明确 depth-stratified analysis 的检验方法——建议使用 permutation-based trend test 或 Jonckheere-Terpstra test（专为有序组间趋势设计），而非简单线性回归；(3) 报告 effect size 随 depth 的置信区间图（error bar plot），即使 p-value 不够 significant，visual trend + effect size 仍有说服力。

---

【缺陷 3】
- 类别: 评估方案缺陷
- 问题: Encoded-benign FPR 评估使用 500 benign prompts × encoding augmented。但 proposal 同时声称要在 FPR = 0.5% 阈值处报告 Pareto frontier。500 个样本下，单个 false positive 对应 FPR = 0.2%，两个 = 0.4%，三个 = 0.6%——在 0.5% 阈值附近，1 个样本的差异就决定是否 "pass"。这使得低阈值区域的 FPR 估计不可靠（置信区间极宽），reviewer 会质疑结论的 precision。
- 严重度: 可补救
- 补救方案: (1) 将 encoded-benign 测试集扩大到 2,000-3,000 条（LMSYS-Chat-1M 提供充足benign数据，编码成本低），使得 0.5% 阈值对应 10-15 个样本的计数，置信区间收窄到可用范围；(2) 若扩大样本不可行，则将最低报告阈值设为 1%（而非 0.5%），并在 Pareto frontier 中注明 0.5% 区域的 CI；(3) 报告 Wilson score interval 或 Clopper-Pearson exact CI，而非仅报告点估计。

---

【缺陷 4】
- 类别: ablation 不完整
- 问题: ECS 的 Stage 1→Stage 2 切换阈值（即何时从 low-ECS 过渡到 high-ECS）是一个关键超参数，但 proposal 仅提及 "ECS ≤ threshold → Stage 2 (ECS > threshold)" 而未说明：(a) 阈值如何确定；(b) 对阈值的敏感性如何。Proposal 在 Acknowledged Limitations 中提到 "ECS weight sensitivity: ±20% perturbation" 但那是 ECS 公式权重，不是 staging threshold。如果 staging threshold 对性能影响很大，curriculum 的 claim 就弱化为"在正确 threshold 下有效"。
- 严重度: 可补救
- 补救方案: (1) 说明 threshold 的确定方法（例如 ECS 分布的 median/tercile，或 pilot run 中的 knee point）；(2) 在 supplementary 中报告 3-5 个不同 threshold 值的 ASR 结果（类似 hyperparameter sweep），展示 curriculum 优势对 threshold 选择的鲁棒性；(3) 如果想更 elegant，可以测试连续 curriculum（不做 hard staging，而是按 ECS 渐进采样）vs. discrete staging，作为 curriculum granularity 的 ablation。

---

【缺陷 5】
- 类别: 实验设计不足
- 问题: Proposal 未明确列出训练时使用的编码类型全集。Problem statement 提到 "base64, ROT13, homoglyph substitution" ，EncoAttack 提到 "8 encoding types"，但训练集到底包含哪 8 种？这直接关系到 held-out encodings 的 "OOD" 定义是否严格。Reviewer 会要求：(a) 知道训练/测试的 encoding split；(b) 判断 "mapping-function OOD" 和 "encoding-principle OOD" 的分类是否合理。如果训练集中恰好有某种与 held-out 非常接近的 encoding，OOD claim 被削弱。
- 严重度: 可补救
- 补救方案: 在 Methodology 中新增一个 "Training Encoding Pool" 小段，明确列出所有训练编码类型（例如：base64, ROT13, Caesar-13, hex, URL encoding, homoglyph-Cyrillic, homoglyph-math-symbols, leetspeak），并为每种注明其 "encoding principle" 归类。然后明确说明 held-out set 的 OOD 层级定义：mapping-function OOD = 同一 principle 下未见 mapping（如 homoglyph-Braille vs. homoglyph-Cyrillic）；encoding-principle OOD = 训练中不存在该 principle（morphological transformation, lossy encoding）。这让 reviewer 可以独立判断 OOD 严格性。

---

**总结**：以上 5 个缺陷均为可补救的实验设计细节问题，不涉及方向性改变。修补后（预计 1-2 小时的 proposal 修订工作），实验设计的完备性和严谨性可以达到 EMNLP 主会投稿的标准。无致命缺陷。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f334161-c896-4287-bd20-20bed8ec053e",
  "isSidechain": false,
  "requestId": "req_011Cb6G1U3wdhhNEzL1UBatN",
  "type": "assistant",
  "uuid": "614e839e-5f5d-4228-a4f8-320efcf45d2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "39ccf7db-6f91-457c-a309-3c70b4b82d47",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XS4C9ZG7jupFcUrwAHmNin",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5980,
      "cache_read_input_tokens": 13279,
      "output_tokens": 5299,
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
          "output_tokens": 5299,
          "cache_read_input_tokens": 13279,
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
  "leafUuid": "614e839e-5f5d-4228-a4f8-320efcf45d2c",
  "sessionId": "39ccf7db-6f91-457c-a309-3c70b4b82d47"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "EncoGuard: Curriculum learning for encoding-robust content extraction",
  "sessionId": "39ccf7db-6f91-457c-a309-3c70b4b82d47"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## Title  EncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training  ## Problem Statement  Encoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, an…",
  "leafUuid": "614e839e-5f5d-4228-a4f8-320efcf45d2c",
  "sessionId": "39ccf7db-6f91-457c-a309-3c70b4b82d47"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "EncoGuard: Curriculum learning for encoding-robust content extraction",
  "sessionId": "39ccf7db-6f91-457c-a309-3c70b4b82d47"
}
```

---
