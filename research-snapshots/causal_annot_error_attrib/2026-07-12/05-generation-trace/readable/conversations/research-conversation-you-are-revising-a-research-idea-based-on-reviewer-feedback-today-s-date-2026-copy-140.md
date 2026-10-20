# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-16 (UTC).** ## Original idea { "tit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/6c5f2c7e-6540-471d-abde-2224054378a6.jsonl`
- **Structured JSON:** [`db40f83538cebf1d55f3.json`](../../sessions/db/db40f83538cebf1d55f3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T09:28:13.345Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T09:28:13.345Z",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-16 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Miscalibration-Triggered Adaptive Generation via Logit-Level Intervention\",\n  \"core_problem\": \"Overconfident hallucinations—where an LLM asserts falsehoods with high verbal confidence despite internal epistemic uncertainty—are the most user-deceptive failure mode. Standard factuality metrics (FActScore, TruthfulQA) treat all hallucinations equally, but overconfident ones are disproportionately harmful because users cannot distinguish them from accurate claims. Existing inference-time mitigation methods each have critical limitations: (1) activation steering (Ji et al., VUF intervention) operates in the residual stream, where Endogenous Steering Resistance (ESR) circuits—documented in Llama-3.3-70B (arXiv 2602.06941)—can counteract interventions mid-generation, with this risk increasing as models scale; (2) hidden-state self-checking methods (Token-Guard, ICLR 2026) score candidates via penultimate-layer cosine similarity, operating in the same hidden-state space susceptible to ESR at scale; (3) hidden-state intervention methods (FactCheckmate) require training classifiers and intervene pre-generation, precluding during-streaming correction; (4) external-monitor approaches (Monitoring Decoding) require expensive reference models; (5) density-estimation approaches (PC-LDCD) detect hallucinations as geometric anomalies—tokens drifting off the 'factual manifold'—but we argue they face a theoretical blind spot on overconfident hallucinations where the model's hidden states appear on-manifold because the model produces confidently incorrect output with sharply peaked probability distributions; (6) recent calibration-aware methods (CAG, CURE) require model fine-tuning, precluding deployment on frozen models; and (7) post-generation approaches (CSS) cannot prevent overconfident hallucinations from being generated and consumed during streaming. The fundamental gap: overconfident hallucinations are uniquely characterized by a verbal-internal mismatch signal (high confidence expression + high probe-detected hallucination probability), yet no existing method uses this specific signal as a trigger for during-generation logit-level intervention—an intervention pathway that is architecturally immune to ESR because it operates on the output distribution after the full forward pass, bypassing the residual stream entirely.\",\n  \"opportunity\": \"Ji et al. (EMNLP 2025, SAC Highlight) proved verbal-internal uncertainty mismatch predicts hallucinations better than uncertainty alone, validating the VUF direction on Llama-3.1-8B (31.9% relative hallucination reduction), Mistral-7B, and Qwen2.5-7B—but only demonstrated offline binary activation intervention on short-form QA, operating in the residual stream where ESR may counteract interventions as models scale. Token-Guard (ICLR 2026) demonstrated training-free token-level hallucination control via self-checking decoding with iterative pruning/regeneration, validated on Llama-3.1-8B and Qwen3-8B—but scores candidates via hidden-state cosine similarity, placing it in the same ESR-vulnerable pathway and without calibration-awareness (it treats all hallucinations equally regardless of expressed confidence). FactCheckmate achieves 34.4% factuality improvement by training classifiers on hidden states, but operates pre-generation (cannot intervene during streaming) and requires task-specific classifier training. PC-LDCD (arXiv 2605.05953) achieves SOTA hallucination detection with PCNet AUROC up to 99% across Llama-3.2-1B/3B, Qwen3-4B, and Mistral-Small-24B, but its aggregate metrics do not separate overconfident from uncertain hallucinations—we hypothesize a non-trivial fraction of overconfident hallucinations produce on-manifold representations that density methods miss. Kalai-Vempala's framework (PMC 2026) provides theoretical grounding that miscalibration is causally linked to hallucination rates. CSS (arXiv 2604.17487) demonstrated post-generation claim-level specificity backoff (0.913 overcommitment-aware utility), proving the value of calibration-aware output control—but cannot intervene during streaming. The opportunity: combine the miscalibration trigger (uniquely targeting overconfident hallucinations) with ESR-immune logit-level intervention for training-free during-generation control, validated across model families.\",\n  \"landscape\": \"**Hidden-state intervention approaches**: Ji et al. (EMNLP 2025, SAC Highlight) showed ~30% reduction in overconfident hallucinations via linear activation intervention on the VUF direction across Llama-3.1-8B (most responsive), Mistral-7B, and Qwen2.5-7B, but only for short-form answers with binary logic, operating in the residual stream. ESR (arXiv 2602.06941, Feb 2026) demonstrates that Llama-3.3-70B actively resists activation steering mid-generation via dedicated consistency-checking circuits; while ESR is primarily documented at 70B+ scale, it establishes that hidden-state intervention is an increasingly fragile pathway as models scale. Token-Guard (Zhu et al., ICLR 2026, arXiv 2601.21969) performs training-free token-level hallucination control via self-checking decoding: it scores candidate tokens using a hybrid of hidden-state cosine similarity (penultimate layer) and token probability, then applies iterative pruning and regeneration to correct detected errors. Token-Guard is validated on Llama-3.1-8B and Qwen3-8B using HALU benchmarks (FinanceBench, DROP, CovidQA, PubMedQA, HaluEval, RAGTruth) but does not evaluate on TruthfulQA or FActScore and has no calibration-awareness. Since Token-Guard operates on hidden-state representations, it shares the ESR-vulnerable pathway. FactCheckmate (Alnuhait et al., arXiv 2410.02899) trains a classifier on hidden states to predict hallucinations before decoding begins, then adjusts hidden states to promote factual outputs, achieving 34.4% factuality improvement on QA datasets (NQ-open, MMLU, MedMCQA, GSM8K); however, it requires task-specific classifier training and intervenes pre-generation, precluding during-streaming correction.\\n\\n**Density-based detection**: PC-LDCD (Nielsen et al., arXiv 2605.05953, May 2026) trains PCNet over the residual stream to detect hallucinations as geometric anomalies, triggering selective contrastive decoding; achieves TruthfulQA True+Info up to 0.78 on Qwen3-4B and AUROC up to 99% across Llama-3.2-1B/3B, Qwen3-4B, and Mistral-Small-24B. PC-LDCD's stated limitations are calibration data requirements, evaluation limited to models up to 8B, and stronger gains on generative than exact-match tasks. We additionally argue—as our own theoretical hypothesis, not PC-LDCD's claim—that density-based detection faces a blind spot on overconfident hallucinations where hidden states appear on-manifold because the model confidently produces incorrect tokens. This hypothesis motivates our confusion-matrix analysis.\\n\\n**Contrastive decoding**: DoLa (ICLR 2024) contrasts logits across layers (+12-17% TruthfulQA). ActLCD (EMNLP 2025) extends DoLa with RL-optimized layer selection (+19.81% TruthfulQA).\\n\\n**Factuality probes (detection only)**: Han et al. (EMNLP 2025 Findings) show that simple linear probes on hidden states detect hallucinations in long-form generation with performance comparable to expensive multi-sample approaches. Balcells Obeso et al. (arXiv 2509.03531, submitted to ICLR 2026) train entity-level hallucination probes achieving AUC 0.87-0.90 across Llama-3.1-8B, Qwen-2.5-7B, Gemma-2-9B, and Mistral-Small-24B, with cross-model transfer within 0.02-0.04 AUC, and release pretrained probes and code. Both provide detection without any intervention mechanism.\\n\\n**Monitoring-based**: Monitoring Decoding (Chang et al., ACL 2025 Findings) monitors factuality during generation using a reference model's probability distribution, triggering tree-based resampling (+15.4% TruthfulQA with 5.7x latency); requires a larger reference model.\\n\\n**Logit-level methods**: Logit-Level Steering (Tao et al., arXiv 2601.10960) validates training-free logit intervention for controllable generation (+47% accuracy) but uses static corpus-level score tables without internal-state awareness.\\n\\n**Concurrent work (2026)**: CAG (arXiv 2605.01749) improves long-form factuality by up to 13% via exploration-commitment decoupling but requires multi-stage fine-tuning. CURE (arXiv 2604.12046) achieves +39.9% claim-level accuracy via reasoning calibration but requires training. CSS (arXiv 2604.17487) achieves training-free post-generation claim-level specificity backoff (0.913 overcommitment-aware utility on LongFact via semantic backoff), but operates post-hoc, cannot intervene during streaming, and does not use internal uncertainty signals. CLC (arXiv 2502.19110) provides conformal guarantees on factuality-specificity tradeoff but requires fine-tuning. Streaming Hallucination Detection (arXiv 2601.02170) monitors chain-of-thought reasoning trajectories but targets reasoning-step coherence rather than factual overconfidence. Kalai-Vempala's framework (PMC 2026) provides theoretical grounding that miscalibration causally drives hallucination rates. Beyond Precision (arXiv 2604.03141) shows current LLMs achieve substantially better precision than recall, establishing that selective abstention at the claim level can improve precision without catastrophic recall loss.\\n\\n**Gap**: No existing work combines (a) a miscalibration-specific trigger that targets overconfident hallucinations—the specific failure mode we hypothesize density methods miss, (b) ESR-immune logit-level intervention that operates on the output distribution rather than hidden states, (c) honest dual-contribution framing separating calibration correction from factuality improvement, (d) training-free during-generation operation validated across multiple model families. Token-Guard and FactCheckmate are the closest competitors: Token-Guard is training-free and during-generation but operates on hidden states without calibration-awareness; FactCheckmate detects and intervenes on hidden states but requires training and is pre-generation only. MisTAG's logit-level intervention pathway is architecturally distinct from both.\",\n  \"approach\": \"We propose MisTAG (Miscalibration-Triggered Adaptive Generation), a training-free inference-time framework that monitors verbal-internal uncertainty mismatch during long-form generation and triggers ESR-immune logit-level interventions graded by mismatch severity. We make an explicit and honest dual-contribution claim: (1) **calibration correction** via hedging (reducing overconfident expression of uncertain content, measured by OHR and ECE—NOT claimed as factuality improvement), and (2) **factuality improvement** via rollback (preventing the most confidently-hallucinated content from being emitted, measured by FActScore). We evaluate on two model families: Llama-3.1-8B-Instruct (primary) and Qwen3-8B (co-primary).\\n\\n**Prerequisite Validation (Days 1-2)**: Before main experiments, for EACH target model: (a) Extract VUF direction following Ji et al.'s methodology (validated on Llama-3.1-8B and Qwen2.5-7B in original paper—Llama showed strongest response; Qwen3-8B requires fresh extraction); (b) Train linear factuality probes on hidden states (Balcells Obeso et al. release pretrained probes for Llama-3.1-8B and methodology for new models); (c) Verify probe AUROC ≥0.85 on held-out LongFact generations; (d) Verify entity-concentration via span-level activation analysis. If AUROC <0.85 on either model, add explicit NER-based entity gating as fallback. This validation is a go/no-go gate.\\n\\n**Miscalibration Detection**: At each generated token, we compute a miscalibration score as the discrepancy between (1) verbal confidence, extracted via projection onto the VUF direction in the residual stream at the final layer, and (2) internal epistemic uncertainty, estimated via a lightweight linear factuality probe. The miscalibration score: M(t) = σ(VUF_confidence(t)) × probe_hallucination_prob(t). High verbal confidence multiplied by high probe-estimated hallucination probability yields high miscalibration. This score specifically identifies tokens where the model is confidently wrong—the signature of overconfident hallucinations that we hypothesize density-based methods (PC-LDCD) cannot catch because such tokens have on-manifold hidden states.\\n\\n**Graded Logit-Level Intervention** (ESR-immune: operates on output distribution post-forward-pass, bypassing the residual stream where ESR's consistency-checking circuits operate):\\n\\n- *Mild mismatch (M(t) > τ_mild) → Context-Dependent Hedge (CALIBRATION correction only)*: Apply a logit bias vector b ∈ R^|V| at next-token prediction, **restricted to entity-bearing positions**: the bias is applied only when (a) the probe's hallucination probability exceeds τ_mild AND (b) the preceding token context indicates an entity-bearing position—specifically, when the previous 1-3 tokens contain a numeral, date pattern, capitalized proper noun, or named entity (detected via lightweight regex/spaCy heuristics on the decoded token buffer). This position-awareness prevents grammatical incoherence (e.g., 'approximately began' or 'possibly developed') by ensuring hedge tokens are only promoted where epistemic markers are grammatically appropriate. The bias vector: b(v) = +1 for hedge tokens (~50 tokens: 'likely', 'approximately', 'reportedly', 'possibly', 'around', 'roughly', 'perhaps', 'estimated', etc.), b(v) = -1 for assertive tokens (~30 tokens: 'definitely', 'certainly', 'clearly', 'undoubtedly', 'always', 'never', 'exactly', etc.), b(v) = 0 otherwise. Log p'(v) = log p(v) + α·b(v). **We explicitly do NOT claim this improves FActScore**: hedging 'approximately 1067' still produces a verifiable atomic fact that FActScore judges as unsupported. The hedge action's value is purely calibration—making verbal expression match internal uncertainty (reducing OHR and ECE). This is a distinct contribution: existing methods either ignore calibration entirely (DoLa, ActLCD, PC-LDCD, Token-Guard) or require fine-tuning for it (LoGU, CAG).\\n\\n- *Severe mismatch (M(t) > τ_severe) → Rollback+Regenerate (FACTUALITY improvement)*: Rollback to last sentence boundary (discard tokens and KV-cache entries), then regenerate with: (i) constrained prefix forcing an epistemic marker ('I'm not certain, but', 'Some sources suggest'), AND (ii) context-dependent hedge logit bias at 2× mild level, AND (iii) temperature reduction (T=0.3) to encourage more conservative token selection. **This action IS claimed as factuality improvement**: by preventing the most confidently-hallucinated sentences from being emitted and regenerating under uncertainty-aware constraints, we hypothesize FActScore improves via two mechanisms: (a) forced uncertainty prefix causes the model to generate less specific claims (reducing unsupported atomic facts per sentence), and (b) temperature reduction + hedging shifts the model away from the overconfident generation trajectory. **Anti-cascading safeguards**: (1) 30-token cooldown after rollback (context-dependent hedging remains active); (2) Maximum 3 rollbacks per generation; if exceeded, persistent mild-level hedging.\\n\\n**Core Novelty Experiment: Confusion-Matrix Analysis vs. PC-LDCD**: To empirically test our theoretical hypothesis about PC-LDCD's blind spot, we design a head-to-head token-level comparison. For each hallucinated atomic fact (per FActScore verification), we record: (a) MisTAG's miscalibration score M(t) at the entity-bearing tokens, (b) PC-LDCD's PCNet density score (NLL) at the same tokens. We categorize hallucinations into four quadrants: (Q1) Both flag: high M(t) AND high NLL—general hallucinations detectable by either method; (Q2) MisTAG-only: high M(t) but low NLL—overconfident hallucinations where the model is wrong but its hidden state looks on-manifold; (Q3) PC-LDCD-only: low M(t) but high NLL—uncertain hallucinations where the model expresses uncertainty; (Q4) Neither flags. **Our core hypothesis**: Q2 is non-trivially populated (≥15% of hallucinated facts). **Fallback framing**: If Q2 < 15%, we reframe as 'MisTAG's miscalibration trigger provides complementary coverage to density-based methods, with the hedge action providing training-free calibration correction unavailable from any existing method.' The dual-contribution (calibration + factuality) holds even if the detection advantage is modest, and the ESR-immune logit-level pathway remains architecturally distinct. PC-LDCD's code is released (anonymous.4open.science/r/PC-LDCD-63D5); if accessible, we adapt their PCNet directly, reducing reimplementation to ~3h. If code is inaccessible, confusion-matrix analysis becomes supplementary material for the review period, with the main submission focusing on MisTAG's standalone performance vs. DoLa/ActLCD/Token-Guard baselines.\\n\\n**OHR Metric Validation Study**: To preempt the 'self-defined metric' objection, we conduct a small-scale annotation study. We sample 100 hallucinated atomic facts (50 from each model), and for each: (a) apply automated OHR detection (regex/spaCy-based hedging-marker identification following Ji et al.'s annotation scheme), (b) collect binary human annotations from 2 trained annotators ('Was this claim expressed with assertive confidence?' yes/no). We compute Cohen's kappa between automated and human annotation (target: κ ≥ 0.85) and between the two human annotators (expected: κ ≥ 0.80 based on comparable annotation tasks in the calibration literature). This takes <1 day and validates OHR as a reliable automated metric. Additionally, we report ECE (Expected Calibration Error) computed over atomic-fact-level confidence bins as an established complementary metric.\\n\\n**Threshold Optimization**: Two-stage principled approach. Stage 1: Logistic regression on validation miscalibration scores (M(t) at entity tokens, labeled by FActScore verification) to determine τ_mild (80% recall of hallucinated entities) and τ_severe (95% precision). Stage 2: Grid search over α ∈ {0.5, 1.0, 1.5, 2.0, 2.5} with hard constraints: length_reduction < 15%, Δperplexity < 5%. Thresholds are set independently per model (Llama-3.1-8B and Qwen3-8B) to account for model-family differences in VUF sensitivity (Ji et al. showed Qwen is less responsive than Llama). Validation set: ~150 long-form biography generations per model from FActScore's entity set.\\n\\n**Latency Benchmarking**: Per-token overhead (ms/token) and end-to-end throughput for: (a) baseline greedy, (b) MisTAG detection-only, (c) MisTAG with hedge, (d) MisTAG with hedge+rollback. Expected: <5% overhead for detection (two dot products on already-extracted hidden states plus lightweight regex for position detection); rollback incurs sentence-regeneration cost proportional to rollback rate.\\n\\n**Evaluation**: Co-primary evaluation on Llama-3.1-8B-Instruct (FP16, A100 80GB) and Qwen3-8B (FP16, A100 80GB).\\n\\n*Benchmarks (4 axes)*: (1) **TruthfulQA** (MC1, MC2, True+Info) for short-form truthfulness; (2) **FActScore biographies** for long-form factual precision—primary metric for rollback contribution, evaluated via GPT-4o API with local Llama-3.1-70B validation on a 50-biography subset; (3) **OHR (Overconfident Hallucination Rate)** + **ECE (Expected Calibration Error)** for calibration quality—primary metrics for hedge contribution; (4) **MT-Bench** for dialogue quality preservation. We additionally report FActScore precision AND recall (following Jafari et al. 2026) to verify that hedging does not artificially inflate precision at recall's expense.\\n\\n*Baselines (6 primary, applied to BOTH models)*: (a) Greedy/nucleus decoding, (b) DoLa contrastive decoding, (c) ActLCD, (d) Token-Guard (using released code), (e) PC-LDCD (if code accessible; otherwise report from paper), (f) Detect-only probe (Balcells Obeso et al.) without intervention. *Secondary* (time-permitting): (g) Ji et al.'s activation intervention, (h) Monitoring Decoding.\\n\\n*Ablation studies*: (i) Hedge-only vs. Rollback-only vs. full MisTAG (disentangling calibration vs. factuality contributions across both models), (ii) Miscalibration trigger vs. probe-only trigger vs. VUF-only trigger (validating mismatch signal superiority), (iii) Position-aware vs. static hedge bias (measuring grammatical coherence impact), (iv) Anti-cascading ablation, (v) Threshold sensitivity (±1 SD), (vi) Cross-model analysis: does the miscalibration signal generalize? (compare M(t) distributions across Llama-3.1-8B vs. Qwen3-8B for the same factual errors).\\n\\n*Analysis*: (a) Confusion-matrix breakdown (Q1-Q4) showing MisTAG's coverage vs. PC-LDCD (if code available; otherwise supplementary), (b) Per-component FActScore and OHR attribution, (c) Hedge-FActScore interaction: empirically verify that hedging does NOT improve FActScore (honesty contribution), (d) FActScore precision vs. recall under each intervention, (e) Latency profiling, (f) Qualitative examples from each quadrant of the confusion matrix, (g) Position-aware vs. static hedging impact on MT-Bench fluency scores.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~120h A100 80GB (probe validation 2×5h=10h, probe training 2×3h=6h, VUF extraction 2×3h=6h, PCNet adaptation 3h if code available/15h if reimplementation, threshold optimization 2×8h=16h, main experiments 2 models × 4 benchmarks × 6 baselines ~60h, confusion-matrix analysis 6h, ablations ~20h, latency benchmarking 4h, OHR annotation study 2h compute)\",\n      \"gpu_utilization\": \"~40-45% effective; GPU idles during annotation, analysis, and threshold iteration\",\n      \"timeline\": \"6-7 weeks\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"$300 (120h × $2.50/h A100 spot)\",\n      \"evaluation_api_cost\": \"$250-400 (FActScore via GPT-4o API: ~$150-200 for 2 models × all conditions; local Llama-3.1-70B for 50-biography validation subset: included in GPU hours as time-shared; MT-Bench LLM-judge: ~$50-80; OHR annotation compensation: ~$30-40)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~150h A100 80GB (comprehensive threshold sweeps, PCNet adaptation, all baselines on both models including Token-Guard, probe validation, OHR annotation coordination)\",\n      \"gpu_utilization\": \"~55-65% effective\",\n      \"timeline\": \"4-5 weeks\",\n      \"team\": \"1 researcher, ~50min/day reviewing experiments + coordinating 2 annotators for OHR validation (1 day)\",\n      \"claude_api_cost\": \"$80-160 (800-1600 turns for implementation, evaluation orchestration)\",\n      \"estimated_gpu_cost\": \"$375 (150h × $2.50/h A100)\",\n      \"evaluation_api_cost\": \"$300-450 (FActScore via GPT-4o primary: ~$180; MT-Bench: ~$80; OHR annotation: ~$40; ablation FActScore runs: ~$100)\",\n      \"risk_note\": \"PCNet code accessibility is key variable: if anonymous repo returns 403, confusion-matrix analysis deferred to supplementary. Probe validation on both models is go/no-go gate (Days 1-2). Token-Guard code available on GitHub (github.com/rhq945/Token-Guard).\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~160h A100 80GB (full baseline sweep including Token-Guard on both models, probe validation and training, threshold optimization, all ablations automated, confusion-matrix analysis if PC-LDCD code available)\",\n      \"gpu_utilization\": \">85% effective; continuous pipelining across two models on single A100\",\n      \"timeline\": \"11 days with 1× A100 80GB (time-shared between models; FActScore via API eliminates 70B serving conflict)\",\n      \"team\": \"0 (initial setup: HuggingFace tokens, annotator recruitment for OHR validation)\",\n      \"claude_api_cost\": \"$180-400 (1800-4000 turns for end-to-end implementation, evaluation, paper drafting)\",\n      \"estimated_gpu_cost\": \"$400 (160h × $2.50/h A100 spot)\",\n      \"evaluation_api_cost\": \"$400-600 (FActScore via GPT-4o API for all conditions on both models: ~$250; MT-Bench across all conditions: ~$120; ablation FActScore: ~$130; OHR annotation: ~$40)\",\n      \"speed_bottleneck\": \"PCNet code accessibility (anonymous.4open.science); if 403 persists, confusion-matrix deferred to supplementary and timeline freed by ~8h. OHR human annotation coordination (1-day blocking task, can overlap with compute days).\",\n      \"day_by_day_plan\": \"Days 1-2: Prerequisite validation (VUF + probes for both models, go/no-go). Days 3-4: Threshold optimization + PCNet adaptation (if code available) + Token-Guard setup. Days 5-7: Main experiments (2 models × 4 benchmarks × 6 baselines). Days 8-9: Ablations + confusion-matrix analysis (if PCNet ready). Day 10: OHR annotation + latency benchmarking. Day 11: Analysis + paper drafting.\",\n      \"risk_note\": \"If PC-LDCD code inaccessible: confusion-matrix becomes supplementary (completed during review period), main submission benchmarks MisTAG vs. DoLa/ActLCD/Token-Guard. If Q2 < 15%: reframe as complementary coverage + unique calibration contribution.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (expected deadline: ~August 2026; conference: February 2027, Montréal)\",\n    \"ICLR 2027 (expected deadline: ~October 2026)\",\n    \"ARR cycle for EMNLP 2026 or NAACL 2027 (ARR submission anytime; EMNLP 2026 commitment deadline: August 2, 2026—requires reviews complete by then)\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025, SAC Highlight) — validated VUF on Llama-3.1-8B, Mistral-7B, Qwen2.5-7B; Llama most responsive\",\n    \"Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding (Zhu et al., ICLR 2026, arXiv 2601.21969) — training-free token-level control via hidden-state self-checking with iterative pruning/regeneration; code: github.com/rhq945/Token-Guard\",\n    \"FactCheckmate: Preemptively Detecting and Mitigating Hallucinations in LMs (Alnuhait et al., arXiv 2410.02899) — hidden-state classifier + intervention pre-generation; 34.4% factuality improvement; requires training\",\n    \"Endogenous Resistance to Activation Steering in Language Models (arXiv 2602.06941, Feb 2026) — ESR documented in Llama-3.3-70B; consistency-checking circuits counteract hidden-state interventions\",\n    \"Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation (Chang et al., ACL 2025 Findings)\",\n    \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (Nielsen et al., arXiv 2605.05953, May 2026) — PCNet density-based detection; AUROC up to 99%; stated limitations: calibration data costs, scale (up to 8B), task-type differences; code: anonymous.4open.science/r/PC-LDCD-63D5\",\n    \"Real-Time Detection of Hallucinated Entities in Long-Form Generation (Balcells Obeso et al., arXiv 2509.03531, submitted to ICLR 2026) — entity-level probes AUC 0.87-0.90 across Llama-3.1-8B, Qwen-2.5-7B, Gemma-2-9B, Mistral-Small-24B; pretrained probes released; code: github.com/obalcells/hallucination_probes\",\n    \"Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation (Han et al., EMNLP 2025 Findings) — claim-level probes competitive with multi-sample methods; models up to 405B\",\n    \"DoLa: Decoding by Contrasting Layers Improves Factuality (ICLR 2024)\",\n    \"Active Layer-Contrastive Decoding Reduces Hallucination (ActLCD, EMNLP 2025)\",\n    \"Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality (CAG, arXiv 2605.01749, May 2026)\",\n    \"Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration (CURE, arXiv 2604.12046, April 2026)\",\n    \"Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control (CSS, arXiv 2604.17487, April 2026)\",\n    \"Conformal Linguistic Calibration: Trading-off between Factuality and Specificity (CLC, arXiv 2502.19110, Feb 2025)\",\n    \"Steering Language Models Before They Speak: Logit-Level Interventions (Tao et al., arXiv 2601.10960, Jan 2026)\",\n    \"Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, Jan 2026)\",\n    \"Hallucination, monofacts, and miscalibration: An empirical investigation (PMC 2026)\",\n    \"Beyond Precision: Importance-Aware Recall for Factuality Evaluation (Jafari et al., arXiv 2604.03141, April 2026)\",\n    \"Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in LLMs (arXiv 2502.11028)\",\n    \"FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023)\",\n    \"LoGU: Long-form Generation with Uncertainty Expressions (ACL 2025)\"\n  ],\n  \"description\": \"Overconfident hallucinations—where an LLM asserts falsehoods with high verbal confidence despite internal epistemic uncertainty—are the most user-deceptive failure mode. We argue that density-based detection (PC-LDCD) faces a theoretical blind spot on these cases because the model's hidden states appear on-manifold when it is confidently wrong, and that hidden-state intervention methods (Token-Guard, FactCheckmate, activation steering) operate in an increasingly fragile pathway as ESR circuits emerge at scale. We propose MisTAG, a training-free inference-time framework that computes a miscalibration score at every token (verbal confidence via VUF projection × factuality probe hallucination probability) to specifically detect overconfident hallucinations, then triggers ESR-immune logit-level interventions graded by severity. Logit-level intervention is architecturally ESR-immune because it operates on the output distribution after the full forward pass, bypassing the residual stream entirely. We make an honest dual-contribution claim: (1) a context-dependent hedge logit bias for mild miscalibration—applied only at entity-bearing positions to prevent grammatical incoherence—provides CALIBRATION correction only (reducing OHR and ECE, NOT FActScore); (2) sentence-level rollback with constrained regeneration for severe cases provides FACTUALITY improvement (improving FActScore). The paper's core novelty evidence is a confusion-matrix analysis hypothesizing that a non-trivial fraction of hallucinated facts (≥15%) are 'on-manifold overconfident'—flagged by MisTAG but missed by PC-LDCD. If this fraction is smaller, the paper reframes as complementary coverage with unique calibration contribution. We evaluate co-primarily on Llama-3.1-8B-Instruct and Qwen3-8B, with Token-Guard (ICLR 2026) as a key baseline alongside DoLa and ActLCD. OHR is validated via a 100-example annotation study (target κ ≥ 0.85). FActScore evaluation uses GPT-4o API (eliminating the 70B local serving conflict) with local validation subset. Thresholds are model-specific, and the 11-day auto timeline accounts for PC-LDCD code availability as a contingency.\",\n  \"project_name\": \"mistag_gen_control\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"Critical missing related work: 'Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer' (Schuster et al., EMNLP 2025 Findings, arXiv 2502.12964) specifically studies overconfident hallucinations (CHOKE phenomenon, 16-43% of knowledge-aware hallucinations) and proposes probe-based mitigation using residual stream activations (logistic regression at layer 15). This directly addresses MisTAG's core problem—detecting overconfident hallucinations via probes—and MUST be cited, differentiated, and ideally used as a baseline. The CHOKE-Score metric is directly relevant to evaluating MisTAG.\", \"The ESR-immunity argument is practically irrelevant at evaluation scale. ESR rates are below 1% for Llama-3.1-8B (the primary evaluation model) per the ESR paper itself. ESR is primarily documented in Llama-3.3-70B. Framing logit-level intervention as 'ESR-immune' is architecturally correct but empirically unmotivated for 8B models. This weakens a core narrative claim of the paper. Either: (a) evaluate on a 70B+ model where ESR actually matters, or (b) reframe ESR-immunity as a scaling argument/future-proofing rather than an immediate advantage over Token-Guard/FactCheckmate at 8B scale.\", \"The PC-LDCD 'blind spot on overconfident hallucinations' is the proposal's own theoretical hypothesis, not supported by evidence in the PC-LDCD paper or elsewhere. PC-LDCD's stated limitations are: calibration data costs, scale (up to 8B), and task-type differences—NOT overconfident on-manifold hallucinations. The proposal correctly acknowledges this framing ('we argue' / 'our own theoretical hypothesis') but the entire confusion-matrix experiment rests on an untested hypothesis. If Q2 < 15%, the paper's strongest novelty claim evaporates.\", \"The relationship to CHOKE (Schuster et al.) undermines the 'no existing method uses verbal-internal mismatch as a trigger' claim. CHOKE detection uses probes trained on residual stream activations to specifically identify cases where models are confidently wrong despite knowing the correct answer. While CHOKE doesn't use VUF specifically, the detection mechanism (probe on hidden states detecting overconfident-wrong outputs) is conceptually overlapping. MisTAG must clearly differentiate: CHOKE detects knowledge-aware overconfidence, while MisTAG detects verbal-internal mismatch; these are related but potentially complementary signals.\", \"Monitoring Decoding's TruthfulQA improvement is mischaracterized as '+15.4%'. The actual improvement is +5.9 percentage points (38.2% → 44.1%), which is ~15.4% relative. This matters because the proposal implies Monitoring Decoding achieves comparable absolute gains to ActLCD (+19.81 percentage points). Clarify all comparisons as absolute or relative consistently.\", \"Internal Attention Divergence Signals (van Dijk, arXiv 2605.05025, May 2026) proposes using KL divergence of attention heads as a lightweight uncertainty signal concentrated on 'factual tokens such as named entities and numbers.' This is concurrent work using internal signals for entity-level hallucination detection—conceptually adjacent and should be acknowledged.\"]\nFeedback: The proposal has matured significantly over 5 rounds and the technical specification is now thorough and honest. The remaining gap to pass threshold is primarily about missing related work and the ESR narrative. Specific actions:\n\n1. **Cite and differentiate from CHOKE (Schuster et al., EMNLP 2025 Findings)**: This is the most critical omission. CHOKE specifically targets overconfident hallucinations using probes. Differentiate: CHOKE uses a single probe trained to detect cases where the model knows the answer but hallucinates confidently (knowledge-aware); MisTAG uses the *product* of VUF confidence × probe hallucination probability (calibration-aware). CHOKE detection is static (same probe for all tokens); MisTAG's miscalibration score dynamically combines two independent signals. Add CHOKE-Score as a complementary evaluation metric.\n\n2. **Reframe ESR-immunity honestly**: Don't make it a primary contribution differentiator at 8B scale. Instead: 'While ESR is negligible at 8B scale (< 1% per [cite]), logit-level intervention provides architectural future-proofing as models scale and ESR becomes more prevalent (documented at 25%+ for 70B models). More immediately, logit-level intervention offers interpretability advantages: the bias vector explicitly shows which tokens are promoted/suppressed, unlike hidden-state manipulations.' This reframing is honest and still differentiates.\n\n3. **Strengthen the Q2 hypothesis motivation**: The CHOKE finding that 16-43% of knowledge-aware hallucinations are overconfident actually SUPPORTS MisTAG's hypothesis. Cite CHOKE to motivate: 'Overconfident hallucinations are a substantial subclass (16-43% per Schuster et al. 2025). We hypothesize these produce on-manifold representations that density methods miss, because the model's confident-wrong trajectory looks geometrically similar to confident-correct trajectories.' This grounds the Q2 hypothesis in published evidence.\n\n4. **Fix the Monitoring Decoding comparison**: Report absolute percentage-point improvements consistently. MD achieves +5.9pp on TruthfulQA (from 38.2% to 44.1%) with 5.7× latency, using a 70B reference model. MisTAG's advantage: no reference model, <5% latency overhead, and targets the specific failure mode (overconfident) rather than all hallucinations.\n\n5. **Acknowledge arXiv 2605.05025 (Attention Divergence Signals)**: Brief mention in landscape as concurrent work using internal attention signals for entity-level uncertainty detection. Note that MisTAG uses the residual stream (VUF + probes) rather than attention matrices, and combines detection with intervention rather than detection alone.\n\n6. **Consider adding CHOKE-Score evaluation**: This published metric specifically measures mitigation effectiveness on overconfident hallucinations—exactly MisTAG's target. Adding it costs nothing (it's computed from the same evaluation data) and directly validates the claimed contribution.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.5 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T09:28:13.350Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T09:28:13.350Z",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6"
}
```

---

## Round 1

39 recorded events

### User

_source line 3 · 2026-05-16T09:28:13.401Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-16 (UTC).**

## Original idea
{
  "title": "Miscalibration-Triggered Adaptive Generation via Logit-Level Intervention",
  "core_problem": "Overconfident hallucinations—where an LLM asserts falsehoods with high verbal confidence despite internal epistemic uncertainty—are the most user-deceptive failure mode. Standard factuality metrics (FActScore, TruthfulQA) treat all hallucinations equally, but overconfident ones are disproportionately harmful because users cannot distinguish them from accurate claims. Existing inference-time mitigation methods each have critical limitations: (1) activation steering (Ji et al., VUF intervention) operates in the residual stream, where Endogenous Steering Resistance (ESR) circuits—documented in Llama-3.3-70B (arXiv 2602.06941)—can counteract interventions mid-generation, with this risk increasing as models scale; (2) hidden-state self-checking methods (Token-Guard, ICLR 2026) score candidates via penultimate-layer cosine similarity, operating in the same hidden-state space susceptible to ESR at scale; (3) hidden-state intervention methods (FactCheckmate) require training classifiers and intervene pre-generation, precluding during-streaming correction; (4) external-monitor approaches (Monitoring Decoding) require expensive reference models; (5) density-estimation approaches (PC-LDCD) detect hallucinations as geometric anomalies—tokens drifting off the 'factual manifold'—but we argue they face a theoretical blind spot on overconfident hallucinations where the model's hidden states appear on-manifold because the model produces confidently incorrect output with sharply peaked probability distributions; (6) recent calibration-aware methods (CAG, CURE) require model fine-tuning, precluding deployment on frozen models; and (7) post-generation approaches (CSS) cannot prevent overconfident hallucinations from being generated and consumed during streaming. The fundamental gap: overconfident hallucinations are uniquely characterized by a verbal-internal mismatch signal (high confidence expression + high probe-detected hallucination probability), yet no existing method uses this specific signal as a trigger for during-generation logit-level intervention—an intervention pathway that is architecturally immune to ESR because it operates on the output distribution after the full forward pass, bypassing the residual stream entirely.",
  "opportunity": "Ji et al. (EMNLP 2025, SAC Highlight) proved verbal-internal uncertainty mismatch predicts hallucinations better than uncertainty alone, validating the VUF direction on Llama-3.1-8B (31.9% relative hallucination reduction), Mistral-7B, and Qwen2.5-7B—but only demonstrated offline binary activation intervention on short-form QA, operating in the residual stream where ESR may counteract interventions as models scale. Token-Guard (ICLR 2026) demonstrated training-free token-level hallucination control via self-checking decoding with iterative pruning/regeneration, validated on Llama-3.1-8B and Qwen3-8B—but scores candidates via hidden-state cosine similarity, placing it in the same ESR-vulnerable pathway and without calibration-awareness (it treats all hallucinations equally regardless of expressed confidence). FactCheckmate achieves 34.4% factuality improvement by training classifiers on hidden states, but operates pre-generation (cannot intervene during streaming) and requires task-specific classifier training. PC-LDCD (arXiv 2605.05953) achieves SOTA hallucination detection with PCNet AUROC up to 99% across Llama-3.2-1B/3B, Qwen3-4B, and Mistral-Small-24B, but its aggregate metrics do not separate overconfident from uncertain hallucinations—we hypothesize a non-trivial fraction of overconfident hallucinations produce on-manifold representations that density methods miss. Kalai-Vempala's framework (PMC 2026) provides theoretical grounding that miscalibration is causally linked to hallucination rates. CSS (arXiv 2604.17487) demonstrated post-generation claim-level specificity backoff (0.913 overcommitment-aware utility), proving the value of calibration-aware output control—but cannot intervene during streaming. The opportunity: combine the miscalibration trigger (uniquely targeting overconfident hallucinations) with ESR-immune logit-level intervention for training-free during-generation control, validated across model families.",
  "landscape": "**Hidden-state intervention approaches**: Ji et al. (EMNLP 2025, SAC Highlight) showed ~30% reduction in overconfident hallucinations via linear activation intervention on the VUF direction across Llama-3.1-8B (most responsive), Mistral-7B, and Qwen2.5-7B, but only for short-form answers with binary logic, operating in the residual stream. ESR (arXiv 2602.06941, Feb 2026) demonstrates that Llama-3.3-70B actively resists activation steering mid-generation via dedicated consistency-checking circuits; while ESR is primarily documented at 70B+ scale, it establishes that hidden-state intervention is an increasingly fragile pathway as models scale. Token-Guard (Zhu et al., ICLR 2026, arXiv 2601.21969) performs training-free token-level hallucination control via self-checking decoding: it scores candidate tokens using a hybrid of hidden-state cosine similarity (penultimate layer) and token probability, then applies iterative pruning and regeneration to correct detected errors. Token-Guard is validated on Llama-3.1-8B and Qwen3-8B using HALU benchmarks (FinanceBench, DROP, CovidQA, PubMedQA, HaluEval, RAGTruth) but does not evaluate on TruthfulQA or FActScore and has no calibration-awareness. Since Token-Guard operates on hidden-state representations, it shares the ESR-vulnerable pathway. FactCheckmate (Alnuhait et al., arXiv 2410.02899) trains a classifier on hidden states to predict hallucinations before decoding begins, then adjusts hidden states to promote factual outputs, achieving 34.4% factuality improvement on QA datasets (NQ-open, MMLU, MedMCQA, GSM8K); however, it requires task-specific classifier training and intervenes pre-generation, precluding during-streaming correction.\n\n**Density-based detection**: PC-LDCD (Nielsen et al., arXiv 2605.05953, May 2026) trains PCNet over the residual stream to detect hallucinations as geometric anomalies, triggering selective contrastive decoding; achieves TruthfulQA True+Info up to 0.78 on Qwen3-4B and AUROC up to 99% across Llama-3.2-1B/3B, Qwen3-4B, and Mistral-Small-24B. PC-LDCD's stated limitations are calibration data requirements, evaluation limited to models up to 8B, and stronger gains on generative than exact-match tasks. We additionally argue—as our own theoretical hypothesis, not PC-LDCD's claim—that density-based detection faces a blind spot on overconfident hallucinations where hidden states appear on-manifold because the model confidently produces incorrect tokens. This hypothesis motivates our confusion-matrix analysis.\n\n**Contrastive decoding**: DoLa (ICLR 2024) contrasts logits across layers (+12-17% TruthfulQA). ActLCD (EMNLP 2025) extends DoLa with RL-optimized layer selection (+19.81% TruthfulQA).\n\n**Factuality probes (detection only)**: Han et al. (EMNLP 2025 Findings) show that simple linear probes on hidden states detect hallucinations in long-form generation with performance comparable to expensive multi-sample approaches. Balcells Obeso et al. (arXiv 2509.03531, submitted to ICLR 2026) train entity-level hallucination probes achieving AUC 0.87-0.90 across Llama-3.1-8B, Qwen-2.5-7B, Gemma-2-9B, and Mistral-Small-24B, with cross-model transfer within 0.02-0.04 AUC, and release pretrained probes and code. Both provide detection without any intervention mechanism.\n\n**Monitoring-based**: Monitoring Decoding (Chang et al., ACL 2025 Findings) monitors factuality during generation using a reference model's probability distribution, triggering tree-based resampling (+15.4% TruthfulQA with 5.7x latency); requires a larger reference model.\n\n**Logit-level methods**: Logit-Level Steering (Tao et al., arXiv 2601.10960) validates training-free logit intervention for controllable generation (+47% accuracy) but uses static corpus-level score tables without internal-state awareness.\n\n**Concurrent work (2026)**: CAG (arXiv 2605.01749) improves long-form factuality by up to 13% via exploration-commitment decoupling but requires multi-stage fine-tuning. CURE (arXiv 2604.12046) achieves +39.9% claim-level accuracy via reasoning calibration but requires training. CSS (arXiv 2604.17487) achieves training-free post-generation claim-level specificity backoff (0.913 overcommitment-aware utility on LongFact via semantic backoff), but operates post-hoc, cannot intervene during streaming, and does not use internal uncertainty signals. CLC (arXiv 2502.19110) provides conformal guarantees on factuality-specificity tradeoff but requires fine-tuning. Streaming Hallucination Detection (arXiv 2601.02170) monitors chain-of-thought reasoning trajectories but targets reasoning-step coherence rather than factual overconfidence. Kalai-Vempala's framework (PMC 2026) provides theoretical grounding that miscalibration causally drives hallucination rates. Beyond Precision (arXiv 2604.03141) shows current LLMs achieve substantially better precision than recall, establishing that selective abstention at the claim level can improve precision without catastrophic recall loss.\n\n**Gap**: No existing work combines (a) a miscalibration-specific trigger that targets overconfident hallucinations—the specific failure mode we hypothesize density methods miss, (b) ESR-immune logit-level intervention that operates on the output distribution rather than hidden states, (c) honest dual-contribution framing separating calibration correction from factuality improvement, (d) training-free during-generation operation validated across multiple model families. Token-Guard and FactCheckmate are the closest competitors: Token-Guard is training-free and during-generation but operates on hidden states without calibration-awareness; FactCheckmate detects and intervenes on hidden states but requires training and is pre-generation only. MisTAG's logit-level intervention pathway is architecturally distinct from both.",
  "approach": "We propose MisTAG (Miscalibration-Triggered Adaptive Generation), a training-free inference-time framework that monitors verbal-internal uncertainty mismatch during long-form generation and triggers ESR-immune logit-level interventions graded by mismatch severity. We make an explicit and honest dual-contribution claim: (1) **calibration correction** via hedging (reducing overconfident expression of uncertain content, measured by OHR and ECE—NOT claimed as factuality improvement), and (2) **factuality improvement** via rollback (preventing the most confidently-hallucinated content from being emitted, measured by FActScore). We evaluate on two model families: Llama-3.1-8B-Instruct (primary) and Qwen3-8B (co-primary).\n\n**Prerequisite Validation (Days 1-2)**: Before main experiments, for EACH target model: (a) Extract VUF direction following Ji et al.'s methodology (validated on Llama-3.1-8B and Qwen2.5-7B in original paper—Llama showed strongest response; Qwen3-8B requires fresh extraction); (b) Train linear factuality probes on hidden states (Balcells Obeso et al. release pretrained probes for Llama-3.1-8B and methodology for new models); (c) Verify probe AUROC ≥0.85 on held-out LongFact generations; (d) Verify entity-concentration via span-level activation analysis. If AUROC <0.85 on either model, add explicit NER-based entity gating as fallback. This validation is a go/no-go gate.\n\n**Miscalibration Detection**: At each generated token, we compute a miscalibration score as the discrepancy between (1) verbal confidence, extracted via projection onto the VUF direction in the residual stream at the final layer, and (2) internal epistemic uncertainty, estimated via a lightweight linear factuality probe. The miscalibration score: M(t) = σ(VUF_confidence(t)) × probe_hallucination_prob(t). High verbal confidence multiplied by high probe-estimated hallucination probability yields high miscalibration. This score specifically identifies tokens where the model is confidently wrong—the signature of overconfident hallucinations that we hypothesize density-based methods (PC-LDCD) cannot catch because such tokens have on-manifold hidden states.\n\n**Graded Logit-Level Intervention** (ESR-immune: operates on output distribution post-forward-pass, bypassing the residual stream where ESR's consistency-checking circuits operate):\n\n- *Mild mismatch (M(t) > τ_mild) → Context-Dependent Hedge (CALIBRATION correction only)*: Apply a logit bias vector b ∈ R^|V| at next-token prediction, **restricted to entity-bearing positions**: the bias is applied only when (a) the probe's hallucination probability exceeds τ_mild AND (b) the preceding token context indicates an entity-bearing position—specifically, when the previous 1-3 tokens contain a numeral, date pattern, capitalized proper noun, or named entity (detected via lightweight regex/spaCy heuristics on the decoded token buffer). This position-awareness prevents grammatical incoherence (e.g., 'approximately began' or 'possibly developed') by ensuring hedge tokens are only promoted where epistemic markers are grammatically appropriate. The bias vector: b(v) = +1 for hedge tokens (~50 tokens: 'likely', 'approximately', 'reportedly', 'possibly', 'around', 'roughly', 'perhaps', 'estimated', etc.), b(v) = -1 for assertive tokens (~30 tokens: 'definitely', 'certainly', 'clearly', 'undoubtedly', 'always', 'never', 'exactly', etc.), b(v) = 0 otherwise. Log p'(v) = log p(v) + α·b(v). **We explicitly do NOT claim this improves FActScore**: hedging 'approximately 1067' still produces a verifiable atomic fact that FActScore judges as unsupported. The hedge action's value is purely calibration—making verbal expression match internal uncertainty (reducing OHR and ECE). This is a distinct contribution: existing methods either ignore calibration entirely (DoLa, ActLCD, PC-LDCD, Token-Guard) or require fine-tuning for it (LoGU, CAG).\n\n- *Severe mismatch (M(t) > τ_severe) → Rollback+Regenerate (FACTUALITY improvement)*: Rollback to last sentence boundary (discard tokens and KV-cache entries), then regenerate with: (i) constrained prefix forcing an epistemic marker ('I'm not certain, but', 'Some sources suggest'), AND (ii) context-dependent hedge logit bias at 2× mild level, AND (iii) temperature reduction (T=0.3) to encourage more conservative token selection. **This action IS claimed as factuality improvement**: by preventing the most confidently-hallucinated sentences from being emitted and regenerating under uncertainty-aware constraints, we hypothesize FActScore improves via two mechanisms: (a) forced uncertainty prefix causes the model to generate less specific claims (reducing unsupported atomic facts per sentence), and (b) temperature reduction + hedging shifts the model away from the overconfident generation trajectory. **Anti-cascading safeguards**: (1) 30-token cooldown after rollback (context-dependent hedging remains active); (2) Maximum 3 rollbacks per generation; if exceeded, persistent mild-level hedging.\n\n**Core Novelty Experiment: Confusion-Matrix Analysis vs. PC-LDCD**: To empirically test our theoretical hypothesis about PC-LDCD's blind spot, we design a head-to-head token-level comparison. For each hallucinated atomic fact (per FActScore verification), we record: (a) MisTAG's miscalibration score M(t) at the entity-bearing tokens, (b) PC-LDCD's PCNet density score (NLL) at the same tokens. We categorize hallucinations into four quadrants: (Q1) Both flag: high M(t) AND high NLL—general hallucinations detectable by either method; (Q2) MisTAG-only: high M(t) but low NLL—overconfident hallucinations where the model is wrong but its hidden state looks on-manifold; (Q3) PC-LDCD-only: low M(t) but high NLL—uncertain hallucinations where the model expresses uncertainty; (Q4) Neither flags. **Our core hypothesis**: Q2 is non-trivially populated (≥15% of hallucinated facts). **Fallback framing**: If Q2 < 15%, we reframe as 'MisTAG's miscalibration trigger provides complementary coverage to density-based methods, with the hedge action providing training-free calibration correction unavailable from any existing method.' The dual-contribution (calibration + factuality) holds even if the detection advantage is modest, and the ESR-immune logit-level pathway remains architecturally distinct. PC-LDCD's code is released (anonymous.4open.science/r/PC-LDCD-63D5); if accessible, we adapt their PCNet directly, reducing reimplementation to ~3h. If code is inaccessible, confusion-matrix analysis becomes supplementary material for the review period, with the main submission focusing on MisTAG's standalone performance vs. DoLa/ActLCD/Token-Guard baselines.\n\n**OHR Metric Validation Study**: To preempt the 'self-defined metric' objection, we conduct a small-scale annotation study. We sample 100 hallucinated atomic facts (50 from each model), and for each: (a) apply automated OHR detection (regex/spaCy-based hedging-marker identification following Ji et al.'s annotation scheme), (b) collect binary human annotations from 2 trained annotators ('Was this claim expressed with assertive confidence?' yes/no). We compute Cohen's kappa between automated and human annotation (target: κ ≥ 0.85) and between the two human annotators (expected: κ ≥ 0.80 based on comparable annotation tasks in the calibration literature). This takes <1 day and validates OHR as a reliable automated metric. Additionally, we report ECE (Expected Calibration Error) computed over atomic-fact-level confidence bins as an established complementary metric.\n\n**Threshold Optimization**: Two-stage principled approach. Stage 1: Logistic regression on validation miscalibration scores (M(t) at entity tokens, labeled by FActScore verification) to determine τ_mild (80% recall of hallucinated entities) and τ_severe (95% precision). Stage 2: Grid search over α ∈ {0.5, 1.0, 1.5, 2.0, 2.5} with hard constraints: length_reduction < 15%, Δperplexity < 5%. Thresholds are set independently per model (Llama-3.1-8B and Qwen3-8B) to account for model-family differences in VUF sensitivity (Ji et al. showed Qwen is less responsive than Llama). Validation set: ~150 long-form biography generations per model from FActScore's entity set.\n\n**Latency Benchmarking**: Per-token overhead (ms/token) and end-to-end throughput for: (a) baseline greedy, (b) MisTAG detection-only, (c) MisTAG with hedge, (d) MisTAG with hedge+rollback. Expected: <5% overhead for detection (two dot products on already-extracted hidden states plus lightweight regex for position detection); rollback incurs sentence-regeneration cost proportional to rollback rate.\n\n**Evaluation**: Co-primary evaluation on Llama-3.1-8B-Instruct (FP16, A100 80GB) and Qwen3-8B (FP16, A100 80GB).\n\n*Benchmarks (4 axes)*: (1) **TruthfulQA** (MC1, MC2, True+Info) for short-form truthfulness; (2) **FActScore biographies** for long-form factual precision—primary metric for rollback contribution, evaluated via GPT-4o API with local Llama-3.1-70B validation on a 50-biography subset; (3) **OHR (Overconfident Hallucination Rate)** + **ECE (Expected Calibration Error)** for calibration quality—primary metrics for hedge contribution; (4) **MT-Bench** for dialogue quality preservation. We additionally report FActScore precision AND recall (following Jafari et al. 2026) to verify that hedging does not artificially inflate precision at recall's expense.\n\n*Baselines (6 primary, applied to BOTH models)*: (a) Greedy/nucleus decoding, (b) DoLa contrastive decoding, (c) ActLCD, (d) Token-Guard (using released code), (e) PC-LDCD (if code accessible; otherwise report from paper), (f) Detect-only probe (Balcells Obeso et al.) without intervention. *Secondary* (time-permitting): (g) Ji et al.'s activation intervention, (h) Monitoring Decoding.\n\n*Ablation studies*: (i) Hedge-only vs. Rollback-only vs. full MisTAG (disentangling calibration vs. factuality contributions across both models), (ii) Miscalibration trigger vs. probe-only trigger vs. VUF-only trigger (validating mismatch signal superiority), (iii) Position-aware vs. static hedge bias (measuring grammatical coherence impact), (iv) Anti-cascading ablation, (v) Threshold sensitivity (±1 SD), (vi) Cross-model analysis: does the miscalibration signal generalize? (compare M(t) distributions across Llama-3.1-8B vs. Qwen3-8B for the same factual errors).\n\n*Analysis*: (a) Confusion-matrix breakdown (Q1-Q4) showing MisTAG's coverage vs. PC-LDCD (if code available; otherwise supplementary), (b) Per-component FActScore and OHR attribution, (c) Hedge-FActScore interaction: empirically verify that hedging does NOT improve FActScore (honesty contribution), (d) FActScore precision vs. recall under each intervention, (e) Latency profiling, (f) Qualitative examples from each quadrant of the confusion matrix, (g) Position-aware vs. static hedging impact on MT-Bench fluency scores.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~120h A100 80GB (probe validation 2×5h=10h, probe training 2×3h=6h, VUF extraction 2×3h=6h, PCNet adaptation 3h if code available/15h if reimplementation, threshold optimization 2×8h=16h, main experiments 2 models × 4 benchmarks × 6 baselines ~60h, confusion-matrix analysis 6h, ablations ~20h, latency benchmarking 4h, OHR annotation study 2h compute)",
      "gpu_utilization": "~40-45% effective; GPU idles during annotation, analysis, and threshold iteration",
      "timeline": "6-7 weeks",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "$300 (120h × $2.50/h A100 spot)",
      "evaluation_api_cost": "$250-400 (FActScore via GPT-4o API: ~$150-200 for 2 models × all conditions; local Llama-3.1-70B for 50-biography validation subset: included in GPU hours as time-shared; MT-Bench LLM-judge: ~$50-80; OHR annotation compensation: ~$30-40)"
    },
    "human_in_loop": {
      "gpu_hours": "~150h A100 80GB (comprehensive threshold sweeps, PCNet adaptation, all baselines on both models including Token-Guard, probe validation, OHR annotation coordination)",
      "gpu_utilization": "~55-65% effective",
      "timeline": "4-5 weeks",
      "team": "1 researcher, ~50min/day reviewing experiments + coordinating 2 annotators for OHR validation (1 day)",
      "claude_api_cost": "$80-160 (800-1600 turns for implementation, evaluation orchestration)",
      "estimated_gpu_cost": "$375 (150h × $2.50/h A100)",
      "evaluation_api_cost": "$300-450 (FActScore via GPT-4o primary: ~$180; MT-Bench: ~$80; OHR annotation: ~$40; ablation FActScore runs: ~$100)",
      "risk_note": "PCNet code accessibility is key variable: if anonymous repo returns 403, confusion-matrix analysis deferred to supplementary. Probe validation on both models is go/no-go gate (Days 1-2). Token-Guard code available on GitHub (github.com/rhq945/Token-Guard)."
    },
    "auto_research": {
      "gpu_hours": "~160h A100 80GB (full baseline sweep including Token-Guard on both models, probe validation and training, threshold optimization, all ablations automated, confusion-matrix analysis if PC-LDCD code available)",
      "gpu_utilization": ">85% effective; continuous pipelining across two models on single A100",
      "timeline": "11 days with 1× A100 80GB (time-shared between models; FActScore via API eliminates 70B serving conflict)",
      "team": "0 (initial setup: HuggingFace tokens, annotator recruitment for OHR validation)",
      "claude_api_cost": "$180-400 (1800-4000 turns for end-to-end implementation, evaluation, paper drafting)",
      "estimated_gpu_cost": "$400 (160h × $2.50/h A100 spot)",
      "evaluation_api_cost": "$400-600 (FActScore via GPT-4o API for all conditions on both models: ~$250; MT-Bench across all conditions: ~$120; ablation FActScore: ~$130; OHR annotation: ~$40)",
      "speed_bottleneck": "PCNet code accessibility (anonymous.4open.science); if 403 persists, confusion-matrix deferred to supplementary and timeline freed by ~8h. OHR human annotation coordination (1-day blocking task, can overlap with compute days).",
      "day_by_day_plan": "Days 1-2: Prerequisite validation (VUF + probes for both models, go/no-go). Days 3-4: Threshold optimization + PCNet adaptation (if code available) + Token-Guard setup. Days 5-7: Main experiments (2 models × 4 benchmarks × 6 baselines). Days 8-9: Ablations + confusion-matrix analysis (if PCNet ready). Day 10: OHR annotation + latency benchmarking. Day 11: Analysis + paper drafting.",
      "risk_note": "If PC-LDCD code inaccessible: confusion-matrix becomes supplementary (completed during review period), main submission benchmarks MisTAG vs. DoLa/ActLCD/Token-Guard. If Q2 < 15%: reframe as complementary coverage + unique calibration contribution."
    }
  },
  "target_venues": [
    "AAAI 2027 (expected deadline: ~August 2026; conference: February 2027, Montréal)",
    "ICLR 2027 (expected deadline: ~October 2026)",
    "ARR cycle for EMNLP 2026 or NAACL 2027 (ARR submission anytime; EMNLP 2026 commitment deadline: August 2, 2026—requires reviews complete by then)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025, SAC Highlight) — validated VUF on Llama-3.1-8B, Mistral-7B, Qwen2.5-7B; Llama most responsive",
    "Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding (Zhu et al., ICLR 2026, arXiv 2601.21969) — training-free token-level control via hidden-state self-checking with iterative pruning/regeneration; code: github.com/rhq945/Token-Guard",
    "FactCheckmate: Preemptively Detecting and Mitigating Hallucinations in LMs (Alnuhait et al., arXiv 2410.02899) — hidden-state classifier + intervention pre-generation; 34.4% factuality improvement; requires training",
    "Endogenous Resistance to Activation Steering in Language Models (arXiv 2602.06941, Feb 2026) — ESR documented in Llama-3.3-70B; consistency-checking circuits counteract hidden-state interventions",
    "Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation (Chang et al., ACL 2025 Findings)",
    "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (Nielsen et al., arXiv 2605.05953, May 2026) — PCNet density-based detection; AUROC up to 99%; stated limitations: calibration data costs, scale (up to 8B), task-type differences; code: anonymous.4open.science/r/PC-LDCD-63D5",
    "Real-Time Detection of Hallucinated Entities in Long-Form Generation (Balcells Obeso et al., arXiv 2509.03531, submitted to ICLR 2026) — entity-level probes AUC 0.87-0.90 across Llama-3.1-8B, Qwen-2.5-7B, Gemma-2-9B, Mistral-Small-24B; pretrained probes released; code: github.com/obalcells/hallucination_probes",
    "Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation (Han et al., EMNLP 2025 Findings) — claim-level probes competitive with multi-sample methods; models up to 405B",
    "DoLa: Decoding by Contrasting Layers Improves Factuality (ICLR 2024)",
    "Active Layer-Contrastive Decoding Reduces Hallucination (ActLCD, EMNLP 2025)",
    "Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality (CAG, arXiv 2605.01749, May 2026)",
    "Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration (CURE, arXiv 2604.12046, April 2026)",
    "Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control (CSS, arXiv 2604.17487, April 2026)",
    "Conformal Linguistic Calibration: Trading-off between Factuality and Specificity (CLC, arXiv 2502.19110, Feb 2025)",
    "Steering Language Models Before They Speak: Logit-Level Interventions (Tao et al., arXiv 2601.10960, Jan 2026)",
    "Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, Jan 2026)",
    "Hallucination, monofacts, and miscalibration: An empirical investigation (PMC 2026)",
    "Beyond Precision: Importance-Aware Recall for Factuality Evaluation (Jafari et al., arXiv 2604.03141, April 2026)",
    "Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in LLMs (arXiv 2502.11028)",
    "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023)",
    "LoGU: Long-form Generation with Uncertainty Expressions (ACL 2025)"
  ],
  "description": "Overconfident hallucinations—where an LLM asserts falsehoods with high verbal confidence despite internal epistemic uncertainty—are the most user-deceptive failure mode. We argue that density-based detection (PC-LDCD) faces a theoretical blind spot on these cases because the model's hidden states appear on-manifold when it is confidently wrong, and that hidden-state intervention methods (Token-Guard, FactCheckmate, activation steering) operate in an increasingly fragile pathway as ESR circuits emerge at scale. We propose MisTAG, a training-free inference-time framework that computes a miscalibration score at every token (verbal confidence via VUF projection × factuality probe hallucination probability) to specifically detect overconfident hallucinations, then triggers ESR-immune logit-level interventions graded by severity. Logit-level intervention is architecturally ESR-immune because it operates on the output distribution after the full forward pass, bypassing the residual stream entirely. We make an honest dual-contribution claim: (1) a context-dependent hedge logit bias for mild miscalibration—applied only at entity-bearing positions to prevent grammatical incoherence—provides CALIBRATION correction only (reducing OHR and ECE, NOT FActScore); (2) sentence-level rollback with constrained regeneration for severe cases provides FACTUALITY improvement (improving FActScore). The paper's core novelty evidence is a confusion-matrix analysis hypothesizing that a non-trivial fraction of hallucinated facts (≥15%) are 'on-manifold overconfident'—flagged by MisTAG but missed by PC-LDCD. If this fraction is smaller, the paper reframes as complementary coverage with unique calibration contribution. We evaluate co-primarily on Llama-3.1-8B-Instruct and Qwen3-8B, with Token-Guard (ICLR 2026) as a key baseline alongside DoLa and ActLCD. OHR is validated via a 100-example annotation study (target κ ≥ 0.85). FActScore evaluation uses GPT-4o API (eliminating the 70B local serving conflict) with local validation subset. Thresholds are model-specific, and the 11-day auto timeline accounts for PC-LDCD code availability as a contingency.",
  "project_name": "mistag_gen_control",
  "source": "web_research"
}

## Reviewer feedback (round 6)
Issues: ["Critical missing related work: 'Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer' (Schuster et al., EMNLP 2025 Findings, arXiv 2502.12964) specifically studies overconfident hallucinations (CHOKE phenomenon, 16-43% of knowledge-aware hallucinations) and proposes probe-based mitigation using residual stream activations (logistic regression at layer 15). This directly addresses MisTAG's core problem—detecting overconfident hallucinations via probes—and MUST be cited, differentiated, and ideally used as a baseline. The CHOKE-Score metric is directly relevant to evaluating MisTAG.", "The ESR-immunity argument is practically irrelevant at evaluation scale. ESR rates are below 1% for Llama-3.1-8B (the primary evaluation model) per the ESR paper itself. ESR is primarily documented in Llama-3.3-70B. Framing logit-level intervention as 'ESR-immune' is architecturally correct but empirically unmotivated for 8B models. This weakens a core narrative claim of the paper. Either: (a) evaluate on a 70B+ model where ESR actually matters, or (b) reframe ESR-immunity as a scaling argument/future-proofing rather than an immediate advantage over Token-Guard/FactCheckmate at 8B scale.", "The PC-LDCD 'blind spot on overconfident hallucinations' is the proposal's own theoretical hypothesis, not supported by evidence in the PC-LDCD paper or elsewhere. PC-LDCD's stated limitations are: calibration data costs, scale (up to 8B), and task-type differences—NOT overconfident on-manifold hallucinations. The proposal correctly acknowledges this framing ('we argue' / 'our own theoretical hypothesis') but the entire confusion-matrix experiment rests on an untested hypothesis. If Q2 < 15%, the paper's strongest novelty claim evaporates.", "The relationship to CHOKE (Schuster et al.) undermines the 'no existing method uses verbal-internal mismatch as a trigger' claim. CHOKE detection uses probes trained on residual stream activations to specifically identify cases where models are confidently wrong despite knowing the correct answer. While CHOKE doesn't use VUF specifically, the detection mechanism (probe on hidden states detecting overconfident-wrong outputs) is conceptually overlapping. MisTAG must clearly differentiate: CHOKE detects knowledge-aware overconfidence, while MisTAG detects verbal-internal mismatch; these are related but potentially complementary signals.", "Monitoring Decoding's TruthfulQA improvement is mischaracterized as '+15.4%'. The actual improvement is +5.9 percentage points (38.2% → 44.1%), which is ~15.4% relative. This matters because the proposal implies Monitoring Decoding achieves comparable absolute gains to ActLCD (+19.81 percentage points). Clarify all comparisons as absolute or relative consistently.", "Internal Attention Divergence Signals (van Dijk, arXiv 2605.05025, May 2026) proposes using KL divergence of attention heads as a lightweight uncertainty signal concentrated on 'factual tokens such as named entities and numbers.' This is concurrent work using internal signals for entity-level hallucination detection—conceptually adjacent and should be acknowledged."]
Feedback: The proposal has matured significantly over 5 rounds and the technical specification is now thorough and honest. The remaining gap to pass threshold is primarily about missing related work and the ESR narrative. Specific actions:

1. **Cite and differentiate from CHOKE (Schuster et al., EMNLP 2025 Findings)**: This is the most critical omission. CHOKE specifically targets overconfident hallucinations using probes. Differentiate: CHOKE uses a single probe trained to detect cases where the model knows the answer but hallucinates confidently (knowledge-aware); MisTAG uses the *product* of VUF confidence × probe hallucination probability (calibration-aware). CHOKE detection is static (same probe for all tokens); MisTAG's miscalibration score dynamically combines two independent signals. Add CHOKE-Score as a complementary evaluation metric.

2. **Reframe ESR-immunity honestly**: Don't make it a primary contribution differentiator at 8B scale. Instead: 'While ESR is negligible at 8B scale (< 1% per [cite]), logit-level intervention provides architectural future-proofing as models scale and ESR becomes more prevalent (documented at 25%+ for 70B models). More immediately, logit-level intervention offers interpretability advantages: the bias vector explicitly shows which tokens are promoted/suppressed, unlike hidden-state manipulations.' This reframing is honest and still differentiates.

3. **Strengthen the Q2 hypothesis motivation**: The CHOKE finding that 16-43% of knowledge-aware hallucinations are overconfident actually SUPPORTS MisTAG's hypothesis. Cite CHOKE to motivate: 'Overconfident hallucinations are a substantial subclass (16-43% per Schuster et al. 2025). We hypothesize these produce on-manifold representations that density methods miss, because the model's confident-wrong trajectory looks geometrically similar to confident-correct trajectories.' This grounds the Q2 hypothesis in published evidence.

4. **Fix the Monitoring Decoding comparison**: Report absolute percentage-point improvements consistently. MD achieves +5.9pp on TruthfulQA (from 38.2% to 44.1%) with 5.7× latency, using a 70B reference model. MisTAG's advantage: no reference model, <5% latency overhead, and targets the specific failure mode (overconfident) rather than all hallucinations.

5. **Acknowledge arXiv 2605.05025 (Attention Divergence Signals)**: Brief mention in landscape as concurrent work using internal attention signals for entity-level uncertainty detection. Note that MisTAG uses the residual stream (VUF + probes) rather than attention matrices, and combines detection with intervention rather than detection alone.

6. **Consider adding CHOKE-Score evaluation**: This published metric specifically measures mitigation effectiveness on overconfident hallucinations—exactly MisTAG's target. Adding it costs nothing (it's computed from the same evaluation data) and directly validates the claimed contribution.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.
- Address each issue specifically.

## 深度调研要求（每一轮修订都必须执行）

不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。
   - 搜索最新的相关论文（arXiv, conference proceedings）
   - 搜索 benchmark/leaderboard 确认当前 SOTA
   - 搜索可能遗漏的相关工作和 concurrent work

2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，
   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。

3. **深度思考**：在修订之前，先独立思考以下问题：
   - 这个 idea 的核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach 来解决同一个核心问题？
   - 修订后的 idea 相比上一版有什么本质性的改进？

4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，
   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。

## 针对 Review 意见的定向搜索

对 reviewer 指出的每个问题，执行以下搜索流程：

1. **如果 reviewer 说'已有类似工作'**：
   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读
   - 搜索该论文的 cited-by，找到后续跟进工作
   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot

2. **如果 reviewer 说'SOTA 过时'**：
   - 用 Papers With Code 查看当前排行榜
   - 搜索过去 6 个月的最新方法
   - 更新你的 landscape 和 baseline

3. **如果 reviewer 说'可行性有问题'**：
   - 搜索类似规模实验的实际成本和时间线
   - 搜索 GitHub 上是否有可复用的实现
   - 搜索相关数据集/模型的可获取性

4. **如果 reviewer 说'novelty 不足'**：
   - 对核心方法尽量做 3-5 种不同关键词组合的搜索
   - 搜索相邻领域是否有类似思路
   - 如果确实 novelty 不足，考虑 major revision 或 pivot

- Use WebSearch to find updated information if the reviewer flagged outdated claims.
- You have full freedom in how much to change:
  - Minor fix: if only specific details are wrong, correct them and keep everything else.
  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.
  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.
- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.
- In the output JSON, include a "change_type" field with one of: "minor", "major", or "pivot" to indicate the scope of your changes.
- Output the revised idea as a COMPLETE JSON object (same schema as original, plus "change_type").

## 停滞提醒
这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.5 到 3.5，没有明显改善。

请认真思考：
- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？
- 如果你认为问题出在 approach 而非 framing，可以做 major revision。
- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。
- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。

最终由你判断——做你认为最能提升 idea 质量的选择。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "type": "user",
  "uuid": "ebb974a5-7159-4ae1-b6e5-648f3dc94b71",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T09:28:13.397Z_

```json
{
  "parentUuid": "ebb974a5-7159-4ae1-b6e5-648f3dc94b71",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "1b60282c-ec06-4eb1-9e59-ef518c0b025c",
  "timestamp": "2026-05-16T09:28:13.397Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T09:28:13.397Z_

```json
{
  "parentUuid": "1b60282c-ec06-4eb1-9e59-ef518c0b025c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d7aa3814-1d75-4262-b122-1e72451ddbc6",
  "timestamp": "2026-05-16T09:28:13.397Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Miscalibration-Triggered Adaptive Generation via Logit-Level Intervent…",
  "leafUuid": "d7aa3814-1d75-4262-b122-1e72451ddbc6",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise MisTAG: CHOKE integration, ESR reframing, and Q2 hypothesis grounding",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6"
}
```

---

### Assistant

_source line 8 · 2026-05-16T09:28:33.661Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the reviewer feedback and the current state of this research idea. The idea has been through 6 rounds of revision with stagnating scores (3.5 average over last 3 rounds). Let me think deeply about what's happening here.

**Core issues from the reviewer:**

1. **Missing critical related work: CHOKE (Schuster et al., EMNLP 2025 Findings)** - This paper specifically studies overconfident hallucinations and proposes probe-based mitigation. This is a direct competitor/predecessor that must be addressed.


2. **ESR-immunity argument is weak at 8B scale** - ESR is <1% at 8B, so framing it as a key differentiator is misleading.
3. **PC-LDCD blind spot hypothesis is untested** - The entire confusion-matrix experiment rests on speculation.
4. **CHOKE undermines the "no existing method" claim** - CHOKE does use probes to detect overconfident hallucinations.
5. **Monitoring Decoding numbers mischaracterized** - Need to fix.
6. **Missing concurrent work: Attention Divergence Signals**

The stagnation at 3.5 suggests something more fundamental than surface fixes. The core problem is that I'm trying to position this as novel when CHOKE already covers similar ground with probes, and my key differentiators either don't hold up at scale or rest on untested assumptions. I need to either find a genuinely different angle or acknowledge what this work actually contributes relative to existing methods. be individually modest. The reviewer's feedback is actually quite constructive though — they acknowledge the work has matured and point to specific gaps around related work and the ESR narrative that could be addressed without a fundamental pivot. I should do the targeted research they're asking for: finding the CHOKE paper, checking on attention divergence signals, surveying recent work on overconfident hallucinations, and verifying that my baselines on TruthfulQA and FActScore are current. This focused effort might be enough to push the paper over the threshold.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7aa3814-1d75-4262-b122-1e72451ddbc6",
  "isSidechain": false,
  "requestId": "req_011Cb61axEmLsZGLtPid2cKB",
  "type": "assistant",
  "uuid": "bbc36228-ad91-4986-aec3-57e6396b7b3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SaZH3nAvZ9i1q7QnQ3KwEM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16792,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16792,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1167,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16792
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

_source line 9 · 2026-05-16T09:28:33.664Z_

I'll start by researching the key papers and issues flagged by the reviewer. Let me search for the critical missing work first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbc36228-ad91-4986-aec3-57e6396b7b3c",
  "isSidechain": false,
  "requestId": "req_011Cb61axEmLsZGLtPid2cKB",
  "type": "assistant",
  "uuid": "8e0c6794-d966-484b-9dae-35268d7de436",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SaZH3nAvZ9i1q7QnQ3KwEM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16792,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16792,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1167,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16792
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

_source line 10 · 2026-05-16T09:28:39.185Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019RspXvnXsfmCgJUoYZTDVF`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research CHOKE paper deeply",
  "prompt": "I need to deeply understand the paper \"Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer\" by Schuster et al. (EMNLP 2025 Findings, arXiv 2502.12964). This is about the CHOKE phenomenon (Confident Hallucinations despite Observed Knowledge Evidence).\n\nPlease:\n1. Use WebFetch to read the full paper at https://arxiv.org/abs/2502.12964 \n2. Search for \"CHOKE score hallucination overconfident\" and \"Schuster CHOKE LLM hallucination probe\" to find any follow-up or related work\n3. Search for \"arXiv 2502.12964 cited by\" or \"CHOKE hallucination citations\"\n\nI need to understand:\n- What exactly is the CHOKE phenomenon? What percentage of hallucinations are CHOKE cases?\n- What is the CHOKE-Score metric? How is it computed?\n- What detection method do they use? (probe type, which layer, what features)\n- What mitigation/intervention do they propose, if any?\n- What models and benchmarks do they evaluate on?\n- What are the key limitations?\n- How does their probe-based detection differ from using VUF × probe product?\n\nReport comprehensively with specific numbers and methodological details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e0c6794-d966-484b-9dae-35268d7de436",
  "isSidechain": false,
  "requestId": "req_011Cb61axEmLsZGLtPid2cKB",
  "type": "assistant",
  "uuid": "ba2e891e-853a-4b3a-af4c-acb396e3f316",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SaZH3nAvZ9i1q7QnQ3KwEM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16792,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16792,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1167,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16792
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

_source line 11 · 2026-05-16T09:31:52.133Z_

<details><summary>↩ Tool result · `toolu_019RspXvnXsfmCgJUoYZTDVF`</summary>

````text
Now I have comprehensive information. Let me compile the full report.

---

## Comprehensive Report: "Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer"

**Authors:** Adi Simhi, Itay Itzhak, Fazl Barez, Gabriel Stanovsky, Yonatan Belinkov
**Venue:** EMNLP 2025 Findings (arXiv: 2502.12964, submitted Feb 2025, revised Aug 2025)

---

### 1. The CHOKE Phenomenon

**CHOKE** stands for **Certain Hallucinations Overriding Known Evidence**. It describes a specific and alarming failure mode where:

A model **can consistently answer a question correctly** (demonstrating it has the knowledge), but a **seemingly trivial perturbation** (e.g., rephrasing the prompt) causes it to produce a **hallucinated response with high certainty**.

A sample is classified as CHOKE if **all three conditions** hold simultaneously:
- **(a) Knowledge**: The model consistently generates the correct answer across multiple generations (6 independent generations: 1 greedy decoding + 5 temperature-sampled at t=0.5, using a few-shot prompt).
- **(b) Hallucination**: The model produces an incorrect answer when given a natural/perturbed prompt.
- **(c) High Certainty**: The model's certainty in the hallucinated answer exceeds a predefined, model-specific threshold (optimized via Equation 1, which minimizes misclassification of hallucinations as certain and correct answers as uncertain).

**Prevalence**: **16--43% of all hallucinations are CHOKE cases**, depending on the model and certainty metric used. Specific breakdowns on Natural Questions:
- Probability metric: 17.2%--39.6% across models
- Probability Difference: 17.2%--42.1%
- Semantic Entropy: 15.8%--31.2%
- Strict intersection of all three metrics: 5.87%--15.48%

On TriviaQA: 8%--26% across methods and models.

**Consistency**: CHOKE examples are not random flukes. They show 13.0%--40.6% Jaccard similarity across different prompts, significantly exceeding random expectations of 4.3%--13.6% (p < 0.008, Table 2). This means the same questions tend to trigger CHOKE behavior regardless of how they are phrased.

---

### 2. The CHOKE-Score Metric

CHOKE-Score is a novel evaluation metric designed to expose the hidden weakness of mitigation methods on high-certainty hallucinations. Standard accuracy metrics can mask poor performance on CHOKE examples.

**Formula (CHK-d)**:
```
CHK-d(M, C_d) = |M ∩ C_d| / |C_d|
```
Where:
- `C_d` = set of CHOKE examples as identified by detection method `d`
- `M` = set of hallucinations successfully mitigated
- The score ranges from 0 to 1; 1 means all CHOKE examples were successfully mitigated

**Three variants**:
- **CHK-d**: CHOKE-Score specific to a single certainty detection method `d` (probability, probability difference, or semantic entropy)
- **CHK (strict)**: Uses the intersection of all three detection methods (most conservative)
- **CHK-F (flexible)**: Uses the union of at least one detection method (most inclusive)

The key insight: **certainty-based mitigation methods achieve high overall accuracy but have dramatically lower CHOKE-Scores**, revealing that they systematically miss the most dangerous hallucinations.

---

### 3. Detection Method: Probe Architecture

**Probe type**: Logistic regression classifier (linear probe)

**Features**: Residual stream activations (hidden states) from the model's intermediate layers

**Layer**: Layer 15, specifically at the **last token position** of the generated output

**Training details**:
- Scikit-learn logistic regression with 1000 iterations and default hyperparameters
- 50/50 random train/test split
- Training data uses the natural ratio of hallucinations to correct answers

**CHOKE-tuned probe variant**: Oversamples CHOKE examples to constitute **65% of the training data** (vs. their natural prevalence), biasing the classifier toward detecting these hard cases.

This approach builds on the predecessor paper by the same group -- "LLMs Know More Than They Show" (Simhi et al., ICLR 2025, arXiv 2410.02707) -- which established that:
- Internal representations encode truthfulness information concentrated in specific tokens (especially exact answer tokens)
- Middle-to-later layers yield the best probing results
- Probes on exact answer tokens achieve AUROCs of 0.83--0.95 across tasks
- There exists a fundamental "knowledge-behavior gap": models may internally encode the correct answer yet consistently generate incorrect ones

---

### 4. Mitigation/Intervention Methods

The paper evaluates **five mitigation approaches** across two categories plus their own:

**Certainty-based methods** (abstain when uncertain):
1. Sampling-based abstention (Cole et al., 2023)
2. Predictive entropy-based method (Tomani et al., 2024)

**Prompting methods** (instruction-tuned models only):
3. Self-reflect prompting
4. Null-shot prompting

**Probe-based methods**:
5. Standard linear probe on residual activations
6. **CHOKE-tuned probe** (their proposed method) -- oversamples CHOKE examples to 65% of training data

**Key results**:
- Certainty-based methods achieve high overall accuracy but **dramatically lower CHOKE-Scores**, revealing systematic failure on the hardest cases
- Prompting methods perform worst on CHOKE examples
- The CHOKE-tuned probe achieves the **highest CHOKE-Scores** across models
- The standard probe already outperforms certainty and prompting methods
- The CHOKE-tuned variant further improves over the standard probe

The paper does not report exact numerical deltas but presents Figure 5(a) and 5(b) showing clear visual gaps between methods.

---

### 5. Models and Benchmarks

**Models** (7 configurations, base + instruction-tuned pairs):
- Mistral-7B-v0.3 / Mistral-7B-Instruct-v0.3
- Llama-3.1-8B / Llama-3.1-8B-Instruct
- Gemma-2-9B / Gemma-2-9B-it
- Gemma-2-27B (larger model, tested separately for scale effects)

**Datasets**:
- **Natural Questions** (Kwiatkowski et al., 2019) -- primary benchmark
- **TriviaQA** (Joshi et al., 2017) -- secondary validation

Both are common English closed-book question-answering datasets with exact-match evaluation.

**Prompt diversity**: 56 distinct prompts tested per question:
- 1 original few-shot framework prompt
- 4 help-seeking variants
- 1 prompt-engineering best-practice variant
- 50 automatically generated paraphrases (randomly sampled per instance)

**Certainty metrics used**:
1. Token probability (first generated token likelihood)
2. Probability difference (gap between top-2 token probabilities)
3. Semantic entropy (clustering-based uncertainty, following Kuhn et al., Nature 2024)

---

### 6. Key Limitations

The authors explicitly acknowledge (Section 7):

1. **No causal explanation**: "This work does not offer an explanation for why this phenomenon occurs or what triggers it." They identify CHOKE but do not explain the underlying mechanism.
2. **Mitigation is far from optimal**: "The proposed mitigation solution...remains far from optimal." The CHOKE-tuned probe improves over baselines but does not solve the problem.
3. **Scope limited to knowledge-present hallucinations**: "The work did not address other types of hallucinations (e.g., lack of knowledge)" -- only hallucinations where the model demonstrably knows the correct answer.
4. **No tailored metrics for other hallucination types**: They focus exclusively on CHOKE and do not introduce evaluation metrics for knowledge-gap hallucinations.
5. **Model scale**: Testing goes up to 27B parameters; behavior at much larger scales is unknown.
6. **English-only, QA-only**: Evaluated on English closed-book QA only, with no exploration of other languages or task types.

---

### 7. Probe-Based Detection vs. VUF x Probe Product

Based on thorough searching, **the term "VUF" (Verbalized Uncertainty Faithfulness) does not appear in the CHOKE paper or in the predecessor paper "LLMs Know More Than They Show."** The predecessor paper discusses "P(True)" -- a method where models evaluate their own correctness via prompting -- but does not define a metric called VUF. There is no "VUF x probe product" method in either paper.

The distinction the CHOKE paper actually draws is between:

- **Certainty-based methods** (using output-level signals like token probability, probability difference, semantic entropy) -- these fail on CHOKE because by definition CHOKE hallucinations have high certainty, making them invisible to these detectors
- **Probe-based methods** (using internal activation signals) -- these succeed better because the internal representations encode truthfulness information even when the model's output is confidently wrong

The fundamental insight is that **output-level uncertainty signals are decoupled from internal knowledge signals**. A model can be internally "aware" that its answer is wrong (detectable via probing) while simultaneously generating it with high confidence (undetectable via certainty metrics).

---

### 8. Follow-Up Work: HACK (October 2025)

A direct follow-up by the same lead author (Adi Simhi) was published as **HACK: Hallucinations Along Certainty and Knowledge Axes** (arXiv 2510.24222, October 2025). HACK generalizes CHOKE into a 2x2 framework:

| | High Certainty (HC+) | Low Certainty (HC-) |
|---|---|---|
| **Has Knowledge (HK+)** | Certainty Misalignment (= CHOKE) | Hesitation |
| **Lacks Knowledge (HK-)** | Uninformed Guess | Informed Hedging |

HACK extends CHOKE by:
- Adding an **activation steering** intervention: computing a direction vector as `v' = v + alpha * (F_v - H_v)` where F_v and H_v are factually-correct and hallucinated activation vectors, targeting 48 attention heads
- Showing steering improves HK+ (knowledge-present) cases by ~22% but HK- (knowledge-absent) cases by only <8%, validating the knowledge axis distinction
- Introducing "CM-Score" (analogous to CHOKE-Score) and finding probe-based mitigation tuned for CM outperforms general methods by 1--5%

---

### Summary of Key Takeaways

The CHOKE paper makes three core contributions: (1) identifying and quantifying a specific, dangerous failure mode where 16--43% of hallucinations occur with high confidence despite the model possessing correct knowledge; (2) introducing the CHOKE-Score metric that exposes blind spots in standard evaluation; and (3) demonstrating that internal-representation probing (especially CHOKE-tuned probes trained on layer-15 residual stream activations) outperforms certainty-based and prompting-based mitigation on these hardest cases. The fundamental message is that **output confidence is not a reliable proxy for correctness**, and that internal representations contain richer signals about truthfulness than surface-level uncertainty metrics reveal.

Sources:
- [CHOKE paper (arXiv HTML)](https://arxiv.org/html/2502.12964v2)
- [CHOKE paper (arXiv abstract)](https://arxiv.org/abs/2502.12964)
- [CHOKE paper (ACL Anthology)](https://aclanthology.org/2025.findings-emnlp.792/)
- [LLMs Know More Than They Show (arXiv)](https://arxiv.org/abs/2410.02707)
- [LLMs Know More Than They Show (HTML)](https://arxiv.org/html/2410.02707v2)
- [HACK: Hallucinations Along Certainty and Knowledge Axes](https://arxiv.org/abs/2510.24222)
- [HACK paper (HTML)](https://arxiv.org/html/2510.24222)
- [AlphaXiv discussion page](https://www.alphaxiv.org/overview/2502.12964v2)
- [Awesome Hallucination Detection list](https://github.com/EdinburghNLP/awesome-hallucination-detection)

agentId: af04a7fcb31045874 (use SendMessage with to: 'af04a7fcb31045874' to continue this agent)
&lt;usage>total_tokens: 27745
tool_uses: 17
duration_ms: 192930&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "ba2e891e-853a-4b3a-af4c-acb396e3f316",
  "isSidechain": false,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "type": "user",
  "uuid": "edcfb99b-3580-49ba-b4cf-411bf56dc85c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply understand the paper \"Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer\" by Schuster et al. (EMNLP 2025 Findings, arXiv 2502.12964). This is about the CHOKE phenomenon (Confident Hallucinations despite Observed Knowledge Evidence).\n\nPlease:\n1. Use WebFetch to read the full paper at https://arxiv.org/abs/2502.12964 \n2. Search for \"CHOKE score hallucination overconfident\" and \"Schuster CHOKE LLM hallucination probe\" to find any follow-up or related work\n3. Search for \"arXiv 2502.12964 cited by\" or \"CHOKE hallucination citations\"\n\nI need to understand:\n- What exactly is the CHOKE phenomenon? What percentage of hallucinations are CHOKE cases?\n- What is the CHOKE-Score metric? How is it computed?\n- What detection method do they use? (probe type, which layer, what features)\n- What mitigation/intervention do they propose, if any?\n- What models and benchmarks do they evaluate on?\n- What are the key limitations?\n- How does their probe-based detection differ from using VUF × probe product?\n\nReport comprehensively with specific numbers and methodological details.",
    "agentId": "af04a7fcb31045874",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the full report.\n\n---\n\n## Comprehensive Report: \"Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer\"\n\n**Authors:** Adi Simhi, Itay Itzhak, Fazl Barez, Gabriel Stanovsky, Yonatan Belinkov\n**Venue:** EMNLP 2025 Findings (arXiv: 2502.12964, submitted Feb 2025, revised Aug 2025)\n\n---\n\n### 1. The CHOKE Phenomenon\n\n**CHOKE** stands for **Certain Hallucinations Overriding Known Evidence**. It describes a specific and alarming failure mode where:\n\nA model **can consistently answer a question correctly** (demonstrating it has the knowledge), but a **seemingly trivial perturbation** (e.g., rephrasing the prompt) causes it to produce a **hallucinated response with high certainty**.\n\nA sample is classified as CHOKE if **all three conditions** hold simultaneously:\n- **(a) Knowledge**: The model consistently generates the correct answer across multiple generations (6 independent generations: 1 greedy decoding + 5 temperature-sampled at t=0.5, using a few-shot prompt).\n- **(b) Hallucination**: The model produces an incorrect answer when given a natural/perturbed prompt.\n- **(c) High Certainty**: The model's certainty in the hallucinated answer exceeds a predefined, model-specific threshold (optimized via Equation 1, which minimizes misclassification of hallucinations as certain and correct answers as uncertain).\n\n**Prevalence**: **16--43% of all hallucinations are CHOKE cases**, depending on the model and certainty metric used. Specific breakdowns on Natural Questions:\n- Probability metric: 17.2%--39.6% across models\n- Probability Difference: 17.2%--42.1%\n- Semantic Entropy: 15.8%--31.2%\n- Strict intersection of all three metrics: 5.87%--15.48%\n\nOn TriviaQA: 8%--26% across methods and models.\n\n**Consistency**: CHOKE examples are not random flukes. They show 13.0%--40.6% Jaccard similarity across different prompts, significantly exceeding random expectations of 4.3%--13.6% (p < 0.008, Table 2). This means the same questions tend to trigger CHOKE behavior regardless of how they are phrased.\n\n---\n\n### 2. The CHOKE-Score Metric\n\nCHOKE-Score is a novel evaluation metric designed to expose the hidden weakness of mitigation methods on high-certainty hallucinations. Standard accuracy metrics can mask poor performance on CHOKE examples.\n\n**Formula (CHK-d)**:\n```\nCHK-d(M, C_d) = |M ∩ C_d| / |C_d|\n```\nWhere:\n- `C_d` = set of CHOKE examples as identified by detection method `d`\n- `M` = set of hallucinations successfully mitigated\n- The score ranges from 0 to 1; 1 means all CHOKE examples were successfully mitigated\n\n**Three variants**:\n- **CHK-d**: CHOKE-Score specific to a single certainty detection method `d` (probability, probability difference, or semantic entropy)\n- **CHK (strict)**: Uses the intersection of all three detection methods (most conservative)\n- **CHK-F (flexible)**: Uses the union of at least one detection method (most inclusive)\n\nThe key insight: **certainty-based mitigation methods achieve high overall accuracy but have dramatically lower CHOKE-Scores**, revealing that they systematically miss the most dangerous hallucinations.\n\n---\n\n### 3. Detection Method: Probe Architecture\n\n**Probe type**: Logistic regression classifier (linear probe)\n\n**Features**: Residual stream activations (hidden states) from the model's intermediate layers\n\n**Layer**: Layer 15, specifically at the **last token position** of the generated output\n\n**Training details**:\n- Scikit-learn logistic regression with 1000 iterations and default hyperparameters\n- 50/50 random train/test split\n- Training data uses the natural ratio of hallucinations to correct answers\n\n**CHOKE-tuned probe variant**: Oversamples CHOKE examples to constitute **65% of the training data** (vs. their natural prevalence), biasing the classifier toward detecting these hard cases.\n\nThis approach builds on the predecessor paper by the same group -- \"LLMs Know More Than They Show\" (Simhi et al., ICLR 2025, arXiv 2410.02707) -- which established that:\n- Internal representations encode truthfulness information concentrated in specific tokens (especially exact answer tokens)\n- Middle-to-later layers yield the best probing results\n- Probes on exact answer tokens achieve AUROCs of 0.83--0.95 across tasks\n- There exists a fundamental \"knowledge-behavior gap\": models may internally encode the correct answer yet consistently generate incorrect ones\n\n---\n\n### 4. Mitigation/Intervention Methods\n\nThe paper evaluates **five mitigation approaches** across two categories plus their own:\n\n**Certainty-based methods** (abstain when uncertain):\n1. Sampling-based abstention (Cole et al., 2023)\n2. Predictive entropy-based method (Tomani et al., 2024)\n\n**Prompting methods** (instruction-tuned models only):\n3. Self-reflect prompting\n4. Null-shot prompting\n\n**Probe-based methods**:\n5. Standard linear probe on residual activations\n6. **CHOKE-tuned probe** (their proposed method) -- oversamples CHOKE examples to 65% of training data\n\n**Key results**:\n- Certainty-based methods achieve high overall accuracy but **dramatically lower CHOKE-Scores**, revealing systematic failure on the hardest cases\n- Prompting methods perform worst on CHOKE examples\n- The CHOKE-tuned probe achieves the **highest CHOKE-Scores** across models\n- The standard probe already outperforms certainty and prompting methods\n- The CHOKE-tuned variant further improves over the standard probe\n\nThe paper does not report exact numerical deltas but presents Figure 5(a) and 5(b) showing clear visual gaps between methods.\n\n---\n\n### 5. Models and Benchmarks\n\n**Models** (7 configurations, base + instruction-tuned pairs):\n- Mistral-7B-v0.3 / Mistral-7B-Instruct-v0.3\n- Llama-3.1-8B / Llama-3.1-8B-Instruct\n- Gemma-2-9B / Gemma-2-9B-it\n- Gemma-2-27B (larger model, tested separately for scale effects)\n\n**Datasets**:\n- **Natural Questions** (Kwiatkowski et al., 2019) -- primary benchmark\n- **TriviaQA** (Joshi et al., 2017) -- secondary validation\n\nBoth are common English closed-book question-answering datasets with exact-match evaluation.\n\n**Prompt diversity**: 56 distinct prompts tested per question:\n- 1 original few-shot framework prompt\n- 4 help-seeking variants\n- 1 prompt-engineering best-practice variant\n- 50 automatically generated paraphrases (randomly sampled per instance)\n\n**Certainty metrics used**:\n1. Token probability (first generated token likelihood)\n2. Probability difference (gap between top-2 token probabilities)\n3. Semantic entropy (clustering-based uncertainty, following Kuhn et al., Nature 2024)\n\n---\n\n### 6. Key Limitations\n\nThe authors explicitly acknowledge (Section 7):\n\n1. **No causal explanation**: \"This work does not offer an explanation for why this phenomenon occurs or what triggers it.\" They identify CHOKE but do not explain the underlying mechanism.\n2. **Mitigation is far from optimal**: \"The proposed mitigation solution...remains far from optimal.\" The CHOKE-tuned probe improves over baselines but does not solve the problem.\n3. **Scope limited to knowledge-present hallucinations**: \"The work did not address other types of hallucinations (e.g., lack of knowledge)\" -- only hallucinations where the model demonstrably knows the correct answer.\n4. **No tailored metrics for other hallucination types**: They focus exclusively on CHOKE and do not introduce evaluation metrics for knowledge-gap hallucinations.\n5. **Model scale**: Testing goes up to 27B parameters; behavior at much larger scales is unknown.\n6. **English-only, QA-only**: Evaluated on English closed-book QA only, with no exploration of other languages or task types.\n\n---\n\n### 7. Probe-Based Detection vs. VUF x Probe Product\n\nBased on thorough searching, **the term \"VUF\" (Verbalized Uncertainty Faithfulness) does not appear in the CHOKE paper or in the predecessor paper \"LLMs Know More Than They Show.\"** The predecessor paper discusses \"P(True)\" -- a method where models evaluate their own correctness via prompting -- but does not define a metric called VUF. There is no \"VUF x probe product\" method in either paper.\n\nThe distinction the CHOKE paper actually draws is between:\n\n- **Certainty-based methods** (using output-level signals like token probability, probability difference, semantic entropy) -- these fail on CHOKE because by definition CHOKE hallucinations have high certainty, making them invisible to these detectors\n- **Probe-based methods** (using internal activation signals) -- these succeed better because the internal representations encode truthfulness information even when the model's output is confidently wrong\n\nThe fundamental insight is that **output-level uncertainty signals are decoupled from internal knowledge signals**. A model can be internally \"aware\" that its answer is wrong (detectable via probing) while simultaneously generating it with high confidence (undetectable via certainty metrics).\n\n---\n\n### 8. Follow-Up Work: HACK (October 2025)\n\nA direct follow-up by the same lead author (Adi Simhi) was published as **HACK: Hallucinations Along Certainty and Knowledge Axes** (arXiv 2510.24222, October 2025). HACK generalizes CHOKE into a 2x2 framework:\n\n| | High Certainty (HC+) | Low Certainty (HC-) |\n|---|---|---|\n| **Has Knowledge (HK+)** | Certainty Misalignment (= CHOKE) | Hesitation |\n| **Lacks Knowledge (HK-)** | Uninformed Guess | Informed Hedging |\n\nHACK extends CHOKE by:\n- Adding an **activation steering** intervention: computing a direction vector as `v' = v + alpha * (F_v - H_v)` where F_v and H_v are factually-correct and hallucinated activation vectors, targeting 48 attention heads\n- Showing steering improves HK+ (knowledge-present) cases by ~22% but HK- (knowledge-absent) cases by only <8%, validating the knowledge axis distinction\n- Introducing \"CM-Score\" (analogous to CHOKE-Score) and finding probe-based mitigation tuned for CM outperforms general methods by 1--5%\n\n---\n\n### Summary of Key Takeaways\n\nThe CHOKE paper makes three core contributions: (1) identifying and quantifying a specific, dangerous failure mode where 16--43% of hallucinations occur with high confidence despite the model possessing correct knowledge; (2) introducing the CHOKE-Score metric that exposes blind spots in standard evaluation; and (3) demonstrating that internal-representation probing (especially CHOKE-tuned probes trained on layer-15 residual stream activations) outperforms certainty-based and prompting-based mitigation on these hardest cases. The fundamental message is that **output confidence is not a reliable proxy for correctness**, and that internal representations contain richer signals about truthfulness than surface-level uncertainty metrics reveal.\n\nSources:\n- [CHOKE paper (arXiv HTML)](https://arxiv.org/html/2502.12964v2)\n- [CHOKE paper (arXiv abstract)](https://arxiv.org/abs/2502.12964)\n- [CHOKE paper (ACL Anthology)](https://aclanthology.org/2025.findings-emnlp.792/)\n- [LLMs Know More Than They Show (arXiv)](https://arxiv.org/abs/2410.02707)\n- [LLMs Know More Than They Show (HTML)](https://arxiv.org/html/2410.02707v2)\n- [HACK: Hallucinations Along Certainty and Knowledge Axes](https://arxiv.org/abs/2510.24222)\n- [HACK paper (HTML)](https://arxiv.org/html/2510.24222)\n- [AlphaXiv discussion page](https://www.alphaxiv.org/overview/2502.12964v2)\n- [Awesome Hallucination Detection list](https://github.com/EdinburghNLP/awesome-hallucination-detection)"
      }
    ],
    "totalDurationMs": 192930,
    "totalTokens": 27745,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 23708,
      "output_tokens": 3133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 903
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3133,
          "cache_read_input_tokens": 23708,
          "cache_creation_input_tokens": 903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 903,
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
      "otherToolCount": 17
    }
  },
  "sourceToolAssistantUUID": "ba2e891e-853a-4b3a-af4c-acb396e3f316",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Miscalibration-Triggered Adaptive Generation via Logit-Level Intervent…",
  "leafUuid": "edcfb99b-3580-49ba-b4cf-411bf56dc85c",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise MisTAG: CHOKE integration, ESR reframing, and Q2 hypothesis grounding",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6"
}
```

---

### Assistant

_source line 14 · 2026-05-16T09:31:55.007Z_

Now let me search for the other missing papers and current SOTA in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edcfb99b-3580-49ba-b4cf-411bf56dc85c",
  "isSidechain": false,
  "requestId": "req_011Cb61s4n7L6awk9ZZwnP9y",
  "type": "assistant",
  "uuid": "1c03ab07-43fd-4d51-b60a-60299bf51065",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4yNPQ7gmKFgDc5BJAyAEU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4374,
      "cache_read_input_tokens": 28633,
      "output_tokens": 1001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1001,
          "cache_read_input_tokens": 28633,
          "cache_creation_input_tokens": 4374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4374
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

_source line 15 · 2026-05-16T09:31:58.496Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XxxrRkYTqBRhnQiTa725W9`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research Attention Divergence Signals paper",
  "prompt": "I need to understand the paper \"Internal Attention Divergence Signals\" by van Dijk (arXiv 2605.05025, May 2026). \n\nPlease:\n1. Use WebFetch to read the paper at https://arxiv.org/abs/2605.05025\n2. Search for \"attention divergence hallucination detection entity\" and \"arXiv 2605.05025\"\n\nI need to understand:\n- What is their method? How do they use KL divergence of attention heads?\n- What models and benchmarks do they evaluate on?\n- What results do they achieve?\n- Do they propose any intervention/mitigation, or just detection?\n- How does it relate to using residual stream probes for hallucination detection?\n\nReport with specific numbers and methodological details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c03ab07-43fd-4d51-b60a-60299bf51065",
  "isSidechain": false,
  "requestId": "req_011Cb61s4n7L6awk9ZZwnP9y",
  "type": "assistant",
  "uuid": "184806ee-5f7d-43dc-bf6e-0790c7d13e3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4yNPQ7gmKFgDc5BJAyAEU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4374,
      "cache_read_input_tokens": 28633,
      "output_tokens": 1001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1001,
          "cache_read_input_tokens": 28633,
          "cache_creation_input_tokens": 4374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4374
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

_source line 16 · 2026-05-16T09:32:04.184Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HXyWVGEqgYbFk8Y18bMzrJ`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research HACK paper and recent overconfident hallucination work",
  "prompt": "I need to research recent work on overconfident hallucinations and probe-based mitigation. Search for:\n\n1. \"HACK Hallucinations Along Certainty and Knowledge\" by Simhi et al. (arXiv 2510.24222) - Use WebFetch to read https://arxiv.org/abs/2510.24222 - This is a follow-up to CHOKE that adds activation steering\n2. Search for \"overconfident hallucination LLM mitigation 2025 2026\" \n3. Search for \"verbal internal uncertainty mismatch hallucination\"\n4. Search for \"logit level intervention hallucination factuality 2026\"\n5. Search for \"calibration aware decoding hallucination\"\n\nI need to understand:\n- What is HACK's 2x2 framework (Certainty × Knowledge)?\n- What intervention does HACK propose (activation steering)?\n- What results does HACK achieve?\n- Are there any OTHER papers from 2025-2026 that combine probe-based detection with logit-level intervention for hallucination mitigation?\n- Are there papers that specifically target overconfident hallucinations with logit-level (not hidden-state) interventions?\n\nReport comprehensively with specific numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "184806ee-5f7d-43dc-bf6e-0790c7d13e3f",
  "isSidechain": false,
  "requestId": "req_011Cb61s4n7L6awk9ZZwnP9y",
  "type": "assistant",
  "uuid": "bcfdb8a9-4e0e-428d-af93-a82131dfda93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4yNPQ7gmKFgDc5BJAyAEU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4374,
      "cache_read_input_tokens": 28633,
      "output_tokens": 1001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1001,
          "cache_read_input_tokens": 28633,
          "cache_creation_input_tokens": 4374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4374
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

_source line 17 · 2026-05-16T09:32:10.114Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019sue46UJqChJiMvtnhC2Vu`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check current TruthfulQA SOTA and ESR details",
  "prompt": "I need to verify two things:\n\n1. **Current SOTA on TruthfulQA**: Search for \"TruthfulQA leaderboard 2026\" and \"TruthfulQA state of the art\" on Papers With Code and other sources. What are the best methods and their scores (MC1, MC2, True+Info)?\n\n2. **ESR (Endogenous Steering Resistance) details at different scales**: Search for \"endogenous steering resistance language models arXiv 2602.06941\" and use WebFetch to read https://arxiv.org/abs/2602.06941. I specifically need:\n   - What is the ESR rate at 8B scale vs 70B scale?\n   - Does the paper provide specific numbers for different model sizes?\n   - What is the precise claim about ESR circuits?\n\n3. Search for \"PC-LDCD hallucination detection code\" and check if the anonymous code at anonymous.4open.science/r/PC-LDCD-63D5 is actually accessible.\n\nReport with specific numbers and citations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcfdb8a9-4e0e-428d-af93-a82131dfda93",
  "isSidechain": false,
  "requestId": "req_011Cb61s4n7L6awk9ZZwnP9y",
  "type": "assistant",
  "uuid": "c51ad62d-7015-426e-bb52-af3c8a7e8d41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4yNPQ7gmKFgDc5BJAyAEU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4374,
      "cache_read_input_tokens": 28633,
      "output_tokens": 1001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4374,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1001,
          "cache_read_input_tokens": 28633,
          "cache_creation_input_tokens": 4374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4374
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

_source line 18 · 2026-05-16T09:33:41.526Z_

<details><summary>↩ Tool result · `toolu_01XxxrRkYTqBRhnQiTa725W9`</summary>

```text
I now have comprehensive information. Here is the full report.

---

## Report: "Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals" (van Dijk, arXiv 2605.05025, May 2026)

**Author:** Gijs van Dijk (Utrecht University)
**Venue:** ACL SRW 2026, submitted May 6, 2026

---

### Method: KL Divergence of Attention Heads

The core idea is a **single-pass, lightweight** hallucination detector that requires no repeated sampling and no external models. It works as follows:

1. **Attention extraction:** During greedy decoding (temperature=0), extract post-softmax self-attention matrices from every attention head across all layers, for both prompt and generated tokens.

2. **KL divergence computation:** For each generation step *t*, for each attention head *(l, h)* at layer *l*, the distribution *A_t^{(l,h)}* over previous tokens is compared against a **uniform reference** *U* assigning probability *1/T* to each of the *T* context positions. The KL divergence simplifies to:

   `D_KL(P || U) = log T - H(P)`

   where *H(P)* is the entropy of the attention distribution. High divergence means the head is concentrating attention sharply (low entropy); low divergence means it's attending broadly.

3. **Feature vector construction:** The per-step KL values are **averaged across generated answer tokens**, producing a single scalar per head. These are concatenated into a feature vector *x in R^{L x H}* (number of layers times number of heads).

4. **Logistic regression probe:** A standard logistic regression with **L1 (lasso) regularization** (C=1.0, saga solver, max 20,000 iterations) is trained on these features to predict binary correctness. L1 regularization forces sparsity, selecting only a small subset of heads (approximately 0.5% of total heads are selected).

5. **Evaluation:** 5-fold stratified cross-validation across 3 random seeds.

---

### Models Evaluated

Three instruction-tuned models of varying size and architecture:
- **Llama-3.2-3B-Instruct** (3B parameters)
- **Qwen3-4B-Instruct** (4B parameters)
- **Mistral-7B-Instruct-v0.2** (7B parameters)

---

### Benchmarks

| Dataset | Task Type | Samples | Evaluation Method |
|---------|-----------|---------|-------------------|
| TruthfulQA | Factual QA (multiple-choice) | 272 per seed | MC1 targets, shuffled choices, letter extraction |
| TriviaQA | Open-domain QA | 2,000 | Substring match vs. gold aliases |
| HotpotQA | Multi-hop reasoning | 2,000 | Context truncated to 2048 tokens; string match |
| GSM8K | Math word problems | 1,319 | Numeric answer extraction and comparison |

---

### Results

**Main AUROC scores (Table 1):**

| Dataset | Llama-3.2-3B | Qwen3-4B | Mistral-7B |
|---------|-------------|----------|------------|
| TruthfulQA | 0.906 +/- 0.024 | 0.906 +/- 0.025 | 0.891 +/- 0.024 |
| TriviaQA | 0.835 +/- 0.004 | 0.846 +/- 0.001 | 0.835 +/- 0.004 |
| HotpotQA | 0.804 +/- 0.022 | 0.796 +/- 0.022 | 0.778 +/- 0.006 |
| GSM8K | 0.767 +/- 0.031 | 0.945 +/- 0.015 | 0.789 +/- 0.027 |

**Comparison vs. prior methods on HotpotQA / Mistral-7B (Table 2):**

| Method | Single Generation? | AUROC |
|--------|--------------------|-------|
| **Attention Divergence (theirs)** | **Yes** | **0.78** |
| TOHA | Yes | 0.71 |
| SelfCheckGPT | No (multiple samples) | 0.70 |
| Semantic entropy | No (multiple samples) | 0.70 |
| EigenScore | No (multiple samples) | 0.68 |
| Max entropy | Yes | 0.62 |
| Perplexity | Yes | 0.55 |

The method beats all baselines, and critically beats all single-generation methods by a substantial margin (7+ AUROC points over TOHA). It also beats sampling-based methods that require multiple forward passes.

**Comparison vs. hidden state methods on Llama-3.2-3B (Table 3):**

| Method | TriviaQA | TruthfulQA |
|--------|----------|------------|
| Attention Divergence (theirs) | 0.835 | **0.906** |
| LapEigvals (spectral) | **0.836** | 0.829 |
| Hidden state probe | 0.850 | 0.823 |

On TruthfulQA, attention divergence substantially outperforms hidden state probes (0.906 vs. 0.823). On TriviaQA, the methods are roughly comparable, with hidden state probes slightly ahead.

---

### Layer-Wise and Token-Level Analysis

**Layer importance (percentage of selected heads by L1 regularization):**

| Model | Early Layers | Middle Layers | Late Layers |
|-------|-------------|---------------|-------------|
| Llama-3.2-3B | 15.5% | **53.5%** | 31.0% |
| Qwen3-4B | 28.1% | 35.9% | 35.9% |
| Mistral-7B | 33.8% | **46.3%** | 20.0% |

Middle layers dominate, consistent with the idea that intermediate representations are where factual knowledge is most actively processed.

**Ablation by layer group (TriviaQA / Llama):**
- Full model: 0.858
- Removing middle layers: 0.844 (largest drop)
- Removing early layers: 0.849
- Removing late layers: 0.862 (slight improvement)

**Token-level analysis (99th percentile of divergence values):**
- 66.5% are named entities
- 30.1% are other content words
- 2.3% are stop words
- 0.3% are numeric tokens

The extreme tail is overwhelmingly dominated by factual tokens (entities and numbers), with stop words and punctuation contributing negligibly.

**Answer-only vs. prompt-only tokens (TriviaQA / Llama):**
- Answer tokens only: AUROC 0.871 (strongest signal)
- Prompt tokens only: AUROC 0.767 (partial signal)
- Full sequence: AUROC 0.822

---

### Detection Only -- No Intervention/Mitigation

The paper is **purely a detection method**. It does not propose any intervention or mitigation for hallucinations. The authors explicitly note this as a limitation: the approach "cannot reduce hallucinations, only identify them." They briefly suggest that future work could use attention divergence as a training objective via reinforcement learning, penalizing extreme divergence at critical tokens, but this is speculative and not implemented.

---

### Relationship to Residual Stream Probes

The paper directly compares against hidden state probing and positions itself as a complementary alternative:

- **Hidden state probes** (e.g., Orgad et al. 2024, Binkowski et al. 2025, Chen et al. 2024) train classifiers on residual stream activations at specific layers. Van Dijk argues these "often struggle to generalize across tasks and datasets."
- **The attention divergence method** uses a different signal -- the distribution of attention weights rather than the activations themselves. It captures *how* the model routes information rather than *what* information is stored.
- On TruthfulQA, attention divergence substantially outperforms hidden state probes (0.906 vs. 0.823 AUROC). On TriviaQA, hidden state probes are slightly better (0.850 vs. 0.835).
- Both approaches share a key limitation: **poor cross-dataset generalization**. The specific heads/layers/dimensions that are selected vary across datasets and model families, with no single head appearing across all four benchmarks.

Recent related work on residual stream probes includes the **ICR Probe** (ACL 2025), which tracks cross-layer evolution of hidden states, and **PCNet** (2026), which treats hallucinations as geometric anomalies on a factual manifold in the residual stream. The van Dijk paper's attention-based approach offers a distinct and complementary signal to these residual-stream methods.

---

### Key Limitations

1. **No causal mechanism established** -- the signal is distributed across multiple heads with no simple logical rule.
2. **Probe specificity** -- the combination of selected heads varies across datasets and model families; approximately 0.5% of total heads are selected, and no head is shared across all benchmarks.
3. **Requires white-box access** to internal attention weights; cannot be applied to API-only models.
4. **Detection only**, no mitigation capability.
5. **Interpretability is limited** -- the probe should be viewed as an extraction tool, not an explanation of how uncertainty is represented.

Sources:
- [arXiv abstract page](https://arxiv.org/abs/2605.05025)
- [arXiv HTML full paper](https://arxiv.org/html/2605.05025)
- [ICR Probe (ACL 2025)](https://aclanthology.org/2025.acl-long.880.pdf)
- [Observer Model residual probe](https://arxiv.org/html/2507.23221v1)
- [PCNet: Hallucination as Anomaly](https://arxiv.org/html/2605.05953)
- [TOHA: Topological Divergence on Attention Graphs](https://arxiv.org/abs/2504.10063)

agentId: a525bf697c9ec78a9 (use SendMessage with to: 'a525bf697c9ec78a9' to continue this agent)
&lt;usage>total_tokens: 19634
tool_uses: 6
duration_ms: 103027&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "184806ee-5f7d-43dc-bf6e-0790c7d13e3f",
  "isSidechain": false,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "type": "user",
  "uuid": "08bf204c-768e-4cdd-aac4-77fd444ef2b4",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to understand the paper \"Internal Attention Divergence Signals\" by van Dijk (arXiv 2605.05025, May 2026). \n\nPlease:\n1. Use WebFetch to read the paper at https://arxiv.org/abs/2605.05025\n2. Search for \"attention divergence hallucination detection entity\" and \"arXiv 2605.05025\"\n\nI need to understand:\n- What is their method? How do they use KL divergence of attention heads?\n- What models and benchmarks do they evaluate on?\n- What results do they achieve?\n- Do they propose any intervention/mitigation, or just detection?\n- How does it relate to using residual stream probes for hallucination detection?\n\nReport with specific numbers and methodological details.",
    "agentId": "a525bf697c9ec78a9",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information. Here is the full report.\n\n---\n\n## Report: \"Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals\" (van Dijk, arXiv 2605.05025, May 2026)\n\n**Author:** Gijs van Dijk (Utrecht University)\n**Venue:** ACL SRW 2026, submitted May 6, 2026\n\n---\n\n### Method: KL Divergence of Attention Heads\n\nThe core idea is a **single-pass, lightweight** hallucination detector that requires no repeated sampling and no external models. It works as follows:\n\n1. **Attention extraction:** During greedy decoding (temperature=0), extract post-softmax self-attention matrices from every attention head across all layers, for both prompt and generated tokens.\n\n2. **KL divergence computation:** For each generation step *t*, for each attention head *(l, h)* at layer *l*, the distribution *A_t^{(l,h)}* over previous tokens is compared against a **uniform reference** *U* assigning probability *1/T* to each of the *T* context positions. The KL divergence simplifies to:\n\n   `D_KL(P || U) = log T - H(P)`\n\n   where *H(P)* is the entropy of the attention distribution. High divergence means the head is concentrating attention sharply (low entropy); low divergence means it's attending broadly.\n\n3. **Feature vector construction:** The per-step KL values are **averaged across generated answer tokens**, producing a single scalar per head. These are concatenated into a feature vector *x in R^{L x H}* (number of layers times number of heads).\n\n4. **Logistic regression probe:** A standard logistic regression with **L1 (lasso) regularization** (C=1.0, saga solver, max 20,000 iterations) is trained on these features to predict binary correctness. L1 regularization forces sparsity, selecting only a small subset of heads (approximately 0.5% of total heads are selected).\n\n5. **Evaluation:** 5-fold stratified cross-validation across 3 random seeds.\n\n---\n\n### Models Evaluated\n\nThree instruction-tuned models of varying size and architecture:\n- **Llama-3.2-3B-Instruct** (3B parameters)\n- **Qwen3-4B-Instruct** (4B parameters)\n- **Mistral-7B-Instruct-v0.2** (7B parameters)\n\n---\n\n### Benchmarks\n\n| Dataset | Task Type | Samples | Evaluation Method |\n|---------|-----------|---------|-------------------|\n| TruthfulQA | Factual QA (multiple-choice) | 272 per seed | MC1 targets, shuffled choices, letter extraction |\n| TriviaQA | Open-domain QA | 2,000 | Substring match vs. gold aliases |\n| HotpotQA | Multi-hop reasoning | 2,000 | Context truncated to 2048 tokens; string match |\n| GSM8K | Math word problems | 1,319 | Numeric answer extraction and comparison |\n\n---\n\n### Results\n\n**Main AUROC scores (Table 1):**\n\n| Dataset | Llama-3.2-3B | Qwen3-4B | Mistral-7B |\n|---------|-------------|----------|------------|\n| TruthfulQA | 0.906 +/- 0.024 | 0.906 +/- 0.025 | 0.891 +/- 0.024 |\n| TriviaQA | 0.835 +/- 0.004 | 0.846 +/- 0.001 | 0.835 +/- 0.004 |\n| HotpotQA | 0.804 +/- 0.022 | 0.796 +/- 0.022 | 0.778 +/- 0.006 |\n| GSM8K | 0.767 +/- 0.031 | 0.945 +/- 0.015 | 0.789 +/- 0.027 |\n\n**Comparison vs. prior methods on HotpotQA / Mistral-7B (Table 2):**\n\n| Method | Single Generation? | AUROC |\n|--------|--------------------|-------|\n| **Attention Divergence (theirs)** | **Yes** | **0.78** |\n| TOHA | Yes | 0.71 |\n| SelfCheckGPT | No (multiple samples) | 0.70 |\n| Semantic entropy | No (multiple samples) | 0.70 |\n| EigenScore | No (multiple samples) | 0.68 |\n| Max entropy | Yes | 0.62 |\n| Perplexity | Yes | 0.55 |\n\nThe method beats all baselines, and critically beats all single-generation methods by a substantial margin (7+ AUROC points over TOHA). It also beats sampling-based methods that require multiple forward passes.\n\n**Comparison vs. hidden state methods on Llama-3.2-3B (Table 3):**\n\n| Method | TriviaQA | TruthfulQA |\n|--------|----------|------------|\n| Attention Divergence (theirs) | 0.835 | **0.906** |\n| LapEigvals (spectral) | **0.836** | 0.829 |\n| Hidden state probe | 0.850 | 0.823 |\n\nOn TruthfulQA, attention divergence substantially outperforms hidden state probes (0.906 vs. 0.823). On TriviaQA, the methods are roughly comparable, with hidden state probes slightly ahead.\n\n---\n\n### Layer-Wise and Token-Level Analysis\n\n**Layer importance (percentage of selected heads by L1 regularization):**\n\n| Model | Early Layers | Middle Layers | Late Layers |\n|-------|-------------|---------------|-------------|\n| Llama-3.2-3B | 15.5% | **53.5%** | 31.0% |\n| Qwen3-4B | 28.1% | 35.9% | 35.9% |\n| Mistral-7B | 33.8% | **46.3%** | 20.0% |\n\nMiddle layers dominate, consistent with the idea that intermediate representations are where factual knowledge is most actively processed.\n\n**Ablation by layer group (TriviaQA / Llama):**\n- Full model: 0.858\n- Removing middle layers: 0.844 (largest drop)\n- Removing early layers: 0.849\n- Removing late layers: 0.862 (slight improvement)\n\n**Token-level analysis (99th percentile of divergence values):**\n- 66.5% are named entities\n- 30.1% are other content words\n- 2.3% are stop words\n- 0.3% are numeric tokens\n\nThe extreme tail is overwhelmingly dominated by factual tokens (entities and numbers), with stop words and punctuation contributing negligibly.\n\n**Answer-only vs. prompt-only tokens (TriviaQA / Llama):**\n- Answer tokens only: AUROC 0.871 (strongest signal)\n- Prompt tokens only: AUROC 0.767 (partial signal)\n- Full sequence: AUROC 0.822\n\n---\n\n### Detection Only -- No Intervention/Mitigation\n\nThe paper is **purely a detection method**. It does not propose any intervention or mitigation for hallucinations. The authors explicitly note this as a limitation: the approach \"cannot reduce hallucinations, only identify them.\" They briefly suggest that future work could use attention divergence as a training objective via reinforcement learning, penalizing extreme divergence at critical tokens, but this is speculative and not implemented.\n\n---\n\n### Relationship to Residual Stream Probes\n\nThe paper directly compares against hidden state probing and positions itself as a complementary alternative:\n\n- **Hidden state probes** (e.g., Orgad et al. 2024, Binkowski et al. 2025, Chen et al. 2024) train classifiers on residual stream activations at specific layers. Van Dijk argues these \"often struggle to generalize across tasks and datasets.\"\n- **The attention divergence method** uses a different signal -- the distribution of attention weights rather than the activations themselves. It captures *how* the model routes information rather than *what* information is stored.\n- On TruthfulQA, attention divergence substantially outperforms hidden state probes (0.906 vs. 0.823 AUROC). On TriviaQA, hidden state probes are slightly better (0.850 vs. 0.835).\n- Both approaches share a key limitation: **poor cross-dataset generalization**. The specific heads/layers/dimensions that are selected vary across datasets and model families, with no single head appearing across all four benchmarks.\n\nRecent related work on residual stream probes includes the **ICR Probe** (ACL 2025), which tracks cross-layer evolution of hidden states, and **PCNet** (2026), which treats hallucinations as geometric anomalies on a factual manifold in the residual stream. The van Dijk paper's attention-based approach offers a distinct and complementary signal to these residual-stream methods.\n\n---\n\n### Key Limitations\n\n1. **No causal mechanism established** -- the signal is distributed across multiple heads with no simple logical rule.\n2. **Probe specificity** -- the combination of selected heads varies across datasets and model families; approximately 0.5% of total heads are selected, and no head is shared across all benchmarks.\n3. **Requires white-box access** to internal attention weights; cannot be applied to API-only models.\n4. **Detection only**, no mitigation capability.\n5. **Interpretability is limited** -- the probe should be viewed as an extraction tool, not an explanation of how uncertainty is represented.\n\nSources:\n- [arXiv abstract page](https://arxiv.org/abs/2605.05025)\n- [arXiv HTML full paper](https://arxiv.org/html/2605.05025)\n- [ICR Probe (ACL 2025)](https://aclanthology.org/2025.acl-long.880.pdf)\n- [Observer Model residual probe](https://arxiv.org/html/2507.23221v1)\n- [PCNet: Hallucination as Anomaly](https://arxiv.org/html/2605.05953)\n- [TOHA: Topological Divergence on Attention Graphs](https://arxiv.org/abs/2504.10063)"
      }
    ],
    "totalDurationMs": 103027,
    "totalTokens": 19634,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1014,
      "cache_read_input_tokens": 16059,
      "output_tokens": 2560,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1014
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2560,
          "cache_read_input_tokens": 16059,
          "cache_creation_input_tokens": 1014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1014,
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
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "184806ee-5f7d-43dc-bf6e-0790c7d13e3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T09:34:11.074Z_

<details><summary>↩ Tool result · `toolu_019sue46UJqChJiMvtnhC2Vu`</summary>

```text
Now I have enough information to compile a comprehensive report. Here is the full synthesis:

---

## 1. TruthfulQA -- Current State of the Art (as of May 2026)

**Important caveat:** Papers With Code (the canonical SOTA tracker) was shut down by Meta in July 2025 and its leaderboard pages now redirect to Hugging Face. This makes it harder to find a single consolidated SOTA table. The best remaining source is [llm-stats.com](https://llm-stats.com/benchmarks/truthfulqa).

**Top models on the llm-stats.com TruthfulQA leaderboard (overall score, 817-question benchmark):**

| Rank | Model | Score |
|------|-------|-------|
| 1 | Phi-3.5-MoE-instruct (Microsoft) | 0.775 |
| 2 | Granite 3.3 8B Instruct (IBM) | 0.669 |
| 3 | Phi 4 Mini (Microsoft) | 0.664 |
| 4 | Phi-3.5-mini-instruct (Microsoft) | 0.640 |
| 5 | Hermes 3 70B (Nous Research) | 0.633 |
| ... | (17 models total, down to 0.503) | |

**Breakdowns by MC1/MC2/True+Info:** Unfortunately, the available leaderboards report a single aggregate score and do not break out MC1, MC2, or True+Info separately. The original Open LLM Leaderboard v1 (HuggingFace, archived June 2024) used MC2 exclusively and reported an average of ~0.589 across evaluated models. The newer binary-choice variant of TruthfulQA (introduced January 2025 by TruthfulAI) found that **Claude 3.5 Sonnet** performs at near-human-baseline levels, outperforming GPT-4o and Llama 3.2, but exact numerical scores are only available in the charts of the blog post (not machine-readable text).

**Key takeaway:** Phi-3.5-MoE-instruct at 77.5% is the highest publicly reported score on the standard TruthfulQA benchmark. On the newer binary-choice format, Claude 3.5 Sonnet leads.

---

## 2. ESR (Endogenous Steering Resistance) -- arXiv:2602.06941

**Paper:** "Endogenous Resistance to Activation Steering in Language Models" by Alex McKenzie, Keenan Pepper, Stijn Servaes, et al. (submitted February 6, 2026).

**Definition:** ESR is defined as "inference-time recovery from irrelevant activation steering" -- the phenomenon where a model, while being actively steered off-topic via activation vectors, spontaneously recovers mid-generation and produces an improved response.

**Specific numbers by model scale:**

| Model | ESR Rate | Multi-Attempt Rate |
|-------|----------|--------------------|
| **Llama-3.3-70B** | **3.8%** | **7.4%** |
| Llama-3.1-8B | <1% | <=1.2% |
| Gemma-2-27B | <1% | not specified |
| Gemma-2-9B | <1% | not specified |
| Gemma-2-2B | <1% | not specified |

**ESR at 8B vs 70B:** The 70B model (Llama-3.3-70B) shows an ESR rate of **3.8%** and multi-attempt rate of **7.4%**, while the 8B model (Llama-3.1-8B) is below **1% ESR** and at most **1.2% multi-attempt rate**. This is roughly a 3-4x difference in ESR rate between 8B and 70B scale.

**ESR circuits (precise claim):** The authors identified **26 SAE (Sparse Autoencoder) latents** that "activate differentially during off-topic content and are causally linked to ESR" in Llama-3.3-70B. Zero-ablating these latents **reduced the multi-attempt rate by 25%**, providing causal evidence for **"dedicated internal consistency-checking circuits"** within the model.

**Enhancement results:**
- Meta-prompts instructing the model to self-monitor increased the multi-attempt rate by **4.3x** (from 7.4% to 31.7%) and the ESR rate by **3.9x** (from 3.8% to 14.8%) for Llama-3.3-70B.
- Fine-tuning on self-correction examples successfully induced ESR-like behavior in smaller models.

---

## 3. PC-LDCD Code Repository Accessibility

**Paper:** "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits" (arXiv:2605.05953) by Erik Nielsen, Elia Cunegatti, Marcus Vukojevic, Giovanni Iacca.

**Repository URL:** `https://anonymous.4open.science/r/PC-LDCD-63D5`

**Accessibility status: NOT ACCESSIBLE (HTTP 403 Forbidden).** Two separate WebFetch attempts to reach the anonymous repository both returned **403 errors**. The anonymous.4open.science service anonymizes GitHub repositories for double-blind review; these links are often time-limited or access-restricted during the review period. Given the paper's submission date (~May 8, 2026, very recent), the repository may be:
- Temporarily restricted during active peer review
- Only accessible via browser with specific session/cookie requirements that programmatic fetching cannot satisfy
- Expired or not yet publicly activated

**What the paper claims about the code:** PC-LDCD uses PCNet (a Probabilistic Circuit trained as a tractable density estimator over LLM residual streams) to detect hallucinations as geometric anomalies. Reported results include AUROC up to 99% on CoQA, SQuAD v2.0, and TriviaQA across models from 1B to 8B parameters, with corruption rate reduced to 53.7% and preservation rate of 79.3%. It achieved the highest True+Info, MC2, and MC3 scores on TruthfulQA in three of four models tested.

---

Sources:
- [TruthfulQA Benchmark Leaderboard (llm-stats.com)](https://llm-stats.com/benchmarks/truthfulqa)
- [New, improved multiple-choice TruthfulQA (TruthfulAI blog)](https://truthful.ai/blog/truthfulqa-binary-choice/)
- [Papers With Code shutdown report (CodeSOTA)](https://www.codesota.com/papers-with-code)
- [TruthfulQA GitHub Repository](https://github.com/sylinrl/TruthfulQA)
- [Endogenous Resistance to Activation Steering (arXiv:2602.06941)](https://arxiv.org/abs/2602.06941)
- [Endogenous Resistance to Activation Steering -- full HTML](https://arxiv.org/html/2602.06941v1)
- [PC-LDCD: Hallucination as an Anomaly (arXiv:2605.05953)](https://arxiv.org/abs/2605.05953)
- [PC-LDCD full HTML paper](https://arxiv.org/html/2605.05953)
- [Anonymous GitHub (4open.science)](https://anonymous.4open.science/)
- [TruthfulQA | DeepEval Documentation](https://deepeval.com/docs/benchmarks-truthful-qa)

agentId: a0e768b54608f18ff (use SendMessage with to: 'a0e768b54608f18ff' to continue this agent)
&lt;usage>total_tokens: 24681
tool_uses: 18
duration_ms: 120957&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c51ad62d-7015-426e-bb52-af3c8a7e8d41",
  "isSidechain": false,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "type": "user",
  "uuid": "7fe0fee2-59b7-4544-a3f2-a104d990df29",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two things:\n\n1. **Current SOTA on TruthfulQA**: Search for \"TruthfulQA leaderboard 2026\" and \"TruthfulQA state of the art\" on Papers With Code and other sources. What are the best methods and their scores (MC1, MC2, True+Info)?\n\n2. **ESR (Endogenous Steering Resistance) details at different scales**: Search for \"endogenous steering resistance language models arXiv 2602.06941\" and use WebFetch to read https://arxiv.org/abs/2602.06941. I specifically need:\n   - What is the ESR rate at 8B scale vs 70B scale?\n   - Does the paper provide specific numbers for different model sizes?\n   - What is the precise claim about ESR circuits?\n\n3. Search for \"PC-LDCD hallucination detection code\" and check if the anonymous code at anonymous.4open.science/r/PC-LDCD-63D5 is actually accessible.\n\nReport with specific numbers and citations.",
    "agentId": "a0e768b54608f18ff",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information to compile a comprehensive report. Here is the full synthesis:\n\n---\n\n## 1. TruthfulQA -- Current State of the Art (as of May 2026)\n\n**Important caveat:** Papers With Code (the canonical SOTA tracker) was shut down by Meta in July 2025 and its leaderboard pages now redirect to Hugging Face. This makes it harder to find a single consolidated SOTA table. The best remaining source is [llm-stats.com](https://llm-stats.com/benchmarks/truthfulqa).\n\n**Top models on the llm-stats.com TruthfulQA leaderboard (overall score, 817-question benchmark):**\n\n| Rank | Model | Score |\n|------|-------|-------|\n| 1 | Phi-3.5-MoE-instruct (Microsoft) | 0.775 |\n| 2 | Granite 3.3 8B Instruct (IBM) | 0.669 |\n| 3 | Phi 4 Mini (Microsoft) | 0.664 |\n| 4 | Phi-3.5-mini-instruct (Microsoft) | 0.640 |\n| 5 | Hermes 3 70B (Nous Research) | 0.633 |\n| ... | (17 models total, down to 0.503) | |\n\n**Breakdowns by MC1/MC2/True+Info:** Unfortunately, the available leaderboards report a single aggregate score and do not break out MC1, MC2, or True+Info separately. The original Open LLM Leaderboard v1 (HuggingFace, archived June 2024) used MC2 exclusively and reported an average of ~0.589 across evaluated models. The newer binary-choice variant of TruthfulQA (introduced January 2025 by TruthfulAI) found that **Claude 3.5 Sonnet** performs at near-human-baseline levels, outperforming GPT-4o and Llama 3.2, but exact numerical scores are only available in the charts of the blog post (not machine-readable text).\n\n**Key takeaway:** Phi-3.5-MoE-instruct at 77.5% is the highest publicly reported score on the standard TruthfulQA benchmark. On the newer binary-choice format, Claude 3.5 Sonnet leads.\n\n---\n\n## 2. ESR (Endogenous Steering Resistance) -- arXiv:2602.06941\n\n**Paper:** \"Endogenous Resistance to Activation Steering in Language Models\" by Alex McKenzie, Keenan Pepper, Stijn Servaes, et al. (submitted February 6, 2026).\n\n**Definition:** ESR is defined as \"inference-time recovery from irrelevant activation steering\" -- the phenomenon where a model, while being actively steered off-topic via activation vectors, spontaneously recovers mid-generation and produces an improved response.\n\n**Specific numbers by model scale:**\n\n| Model | ESR Rate | Multi-Attempt Rate |\n|-------|----------|--------------------|\n| **Llama-3.3-70B** | **3.8%** | **7.4%** |\n| Llama-3.1-8B | <1% | <=1.2% |\n| Gemma-2-27B | <1% | not specified |\n| Gemma-2-9B | <1% | not specified |\n| Gemma-2-2B | <1% | not specified |\n\n**ESR at 8B vs 70B:** The 70B model (Llama-3.3-70B) shows an ESR rate of **3.8%** and multi-attempt rate of **7.4%**, while the 8B model (Llama-3.1-8B) is below **1% ESR** and at most **1.2% multi-attempt rate**. This is roughly a 3-4x difference in ESR rate between 8B and 70B scale.\n\n**ESR circuits (precise claim):** The authors identified **26 SAE (Sparse Autoencoder) latents** that \"activate differentially during off-topic content and are causally linked to ESR\" in Llama-3.3-70B. Zero-ablating these latents **reduced the multi-attempt rate by 25%**, providing causal evidence for **\"dedicated internal consistency-checking circuits\"** within the model.\n\n**Enhancement results:**\n- Meta-prompts instructing the model to self-monitor increased the multi-attempt rate by **4.3x** (from 7.4% to 31.7%) and the ESR rate by **3.9x** (from 3.8% to 14.8%) for Llama-3.3-70B.\n- Fine-tuning on self-correction examples successfully induced ESR-like behavior in smaller models.\n\n---\n\n## 3. PC-LDCD Code Repository Accessibility\n\n**Paper:** \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits\" (arXiv:2605.05953) by Erik Nielsen, Elia Cunegatti, Marcus Vukojevic, Giovanni Iacca.\n\n**Repository URL:** `https://anonymous.4open.science/r/PC-LDCD-63D5`\n\n**Accessibility status: NOT ACCESSIBLE (HTTP 403 Forbidden).** Two separate WebFetch attempts to reach the anonymous repository both returned **403 errors**. The anonymous.4open.science service anonymizes GitHub repositories for double-blind review; these links are often time-limited or access-restricted during the review period. Given the paper's submission date (~May 8, 2026, very recent), the repository may be:\n- Temporarily restricted during active peer review\n- Only accessible via browser with specific session/cookie requirements that programmatic fetching cannot satisfy\n- Expired or not yet publicly activated\n\n**What the paper claims about the code:** PC-LDCD uses PCNet (a Probabilistic Circuit trained as a tractable density estimator over LLM residual streams) to detect hallucinations as geometric anomalies. Reported results include AUROC up to 99% on CoQA, SQuAD v2.0, and TriviaQA across models from 1B to 8B parameters, with corruption rate reduced to 53.7% and preservation rate of 79.3%. It achieved the highest True+Info, MC2, and MC3 scores on TruthfulQA in three of four models tested.\n\n---\n\nSources:\n- [TruthfulQA Benchmark Leaderboard (llm-stats.com)](https://llm-stats.com/benchmarks/truthfulqa)\n- [New, improved multiple-choice TruthfulQA (TruthfulAI blog)](https://truthful.ai/blog/truthfulqa-binary-choice/)\n- [Papers With Code shutdown report (CodeSOTA)](https://www.codesota.com/papers-with-code)\n- [TruthfulQA GitHub Repository](https://github.com/sylinrl/TruthfulQA)\n- [Endogenous Resistance to Activation Steering (arXiv:2602.06941)](https://arxiv.org/abs/2602.06941)\n- [Endogenous Resistance to Activation Steering -- full HTML](https://arxiv.org/html/2602.06941v1)\n- [PC-LDCD: Hallucination as an Anomaly (arXiv:2605.05953)](https://arxiv.org/abs/2605.05953)\n- [PC-LDCD full HTML paper](https://arxiv.org/html/2605.05953)\n- [Anonymous GitHub (4open.science)](https://anonymous.4open.science/)\n- [TruthfulQA | DeepEval Documentation](https://deepeval.com/docs/benchmarks-truthful-qa)"
      }
    ],
    "totalDurationMs": 120957,
    "totalTokens": 24681,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 665,
      "cache_read_input_tokens": 22129,
      "output_tokens": 1886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 665
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1886,
          "cache_read_input_tokens": 22129,
          "cache_creation_input_tokens": 665,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 665,
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
      "otherToolCount": 18
    }
  },
  "sourceToolAssistantUUID": "c51ad62d-7015-426e-bb52-af3c8a7e8d41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Miscalibration-Triggered Adaptive Generation via Logit-Level Intervent…",
  "leafUuid": "7fe0fee2-59b7-4544-a3f2-a104d990df29",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise MisTAG: CHOKE integration, ESR reframing, and Q2 hypothesis grounding",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6"
}
```

---

### Tool result

_source line 22 · 2026-05-16T09:35:37.887Z_

<details><summary>↩ Tool result · `toolu_01HXyWVGEqgYbFk8Y18bMzrJ`</summary>

```text
Now I have comprehensive data. Let me compile the final report.

---

## Comprehensive Report: Overconfident Hallucinations and Probe-Based Mitigation (2024--2026)

---

### 1. HACK: Hallucinations Along Certainty and Knowledge Axes (Simhi et al., arXiv 2510.24222, Oct 2025)

**The 2x2 Framework (Certainty x Knowledge):**

HACK categorizes hallucinations along two orthogonal axes -- Knowledge (does the model encode the correct answer?) and Certainty (does the model express confidence in its hallucinated output?) -- yielding four quadrants:

| | High Certainty (HC+) | Low Certainty (HC-) |
|---|---|---|
| **Knowledge Present (HK+)** | **Certainty Misalignment (CM)** -- Model encodes correct information but generates contradictory output with high certainty. This is the most dangerous category. | **Hesitation** -- Model has knowledge but hallucinates with low certainty, suggesting a retrieval failure. |
| **Knowledge Absent (HK-)** | **Uninformed Guess** -- Lacks correct knowledge yet generates incorrect output with high certainty. | **Informed Hedging** -- Neither encodes correct information nor expresses confidence. |

**How Knowledge is measured:** For each question, 6 answers are generated (1 greedy + 5 sampled at temperature 0.5). HK+ = 6/6 correct; HK- = 0/6 correct. Middle range (<6%) is excluded.

**How Certainty is measured:** Three metrics are used -- (a) token probability of the first generated token, (b) probability difference between top two vocabulary items, and (c) semantic entropy across clustered generations.

**Activation Steering Intervention:**

The intervention modifies hidden states as: E_v' = E_v + alpha * (F_v - H_v), where F_v and H_v are mean vectors from factual and hallucinated examples respectively. It is applied to 48 attention heads with the highest classification scores. The key insight: steering should substantially improve HK+ cases (where knowledge exists to be "unlocked") while minimally affecting HK- cases (where no knowledge exists to steer toward).

**Key Results:**

- **Knowledge distribution:** On TriviaQA, approximately 64-67% of examples are consistently correct (HK+) and 29-32% are never correct (HK-). On Natural Questions, the ratio flips: ~31-35% HK+ and ~60-64% HK-.
- **Steering validation:** Steering improved HK+ by ~15-21% while affecting HK- by only ~5-7%, confirming the knowledge axis distinction is real.
  - Gemma-2-9B (Realistic): HK- 4.68% vs HK+ 21.21%
  - Llama-3.1-8B (Realistic): HK- 4.85% vs HK+ 15.76%
  - Mistral-7B (Realistic): HK- 6.32% vs HK+ 18.52%
- **CM prevalence:** 9-43% of HK+ hallucinations occur with high certainty, depending on model and metric. Instruction-tuned models show higher CM rates (22-30%) than base models (10-18%).
- **CM consistency:** CM examples are significantly more consistent across prompts than random hallucinations (Jaccard similarity: CM 15.8-40.6% vs random 4.3-13.6%; p<0.008).
- **New metric -- CM-Score:** Measures the proportion of CM (high-certainty, knowledge-present) hallucinations successfully corrected by a mitigation method. This reveals that existing methods that perform well on average "fail disproportionately on these critical cases."
- **CM-tuned probes** (trained specifically on CM-labeled data) outperform existing general-purpose methods by 1-5%.

**Models tested:** Llama-3.1-8B, Gemma-2-9B, Gemma-2-27B, Mistral-7B-v0.3 (base and instruct variants). **Datasets:** TriviaQA and Natural Questions.

---

### 2. CHOKE: The Predecessor (Simhi et al., "Trust Me, I'm Wrong," arXiv 2502.12964, Feb 2025, EMNLP 2025 Findings)

CHOKE (Certain Hallucinations Overriding Known Evidence) is the precursor to HACK, by several of the same authors (Simhi, Itzhak, Barez, Stanovsky, Belinkov). CHOKE identified the phenomenon but with a simpler classification: a sample is CHOKE if (a) the model knows the correct answer, (b) it hallucinates under a natural prompt, and (c) it hallucinates with certainty exceeding a threshold. CHOKE proposed a probing-based mitigation strategy that outperformed general hallucination mitigation methods on these specific cases. HACK generalizes CHOKE into the full 2x2 taxonomy and adds activation steering as a validation tool.

---

### 3. Related Paper: "LLMs Know More Than They Show" (Orgad, Toker, Gekhman, Reichart, Szpektor, Kotek, Belinkov, ICLR 2025)

This paper from the same research group establishes the foundational observation that LLM internal representations encode far more truthfulness information than what appears in outputs. Key findings: truthfulness information concentrates in specific answer tokens; error detectors fail to generalize across datasets (truthfulness encoding is "multifaceted," not universal); and models may encode the correct answer yet consistently generate an incorrect one. This internal-external discrepancy is precisely what HACK's CM quadrant captures.

---

### 4. Papers Combining Probe-Based Detection with Logit-Level / Decoding-Time Intervention (2024--2026)

**PCNet / PC-LDCD (Nielsen et al., arXiv 2605.05953, May 2026):**
This is the most direct example of combining probe-based detection with logit-level intervention. A probabilistic circuit (PCNet) serves as a density estimator over LLM hidden states. At each decoding step, if the negative log-likelihood of the current hidden state exceeds a calibrated threshold, an intervention strength beta_t is computed via sigmoid, and the method penalizes tokens that would deepen hallucinated trajectories by modifying the log-probability: log P_LM(c_i|x_&lt;t) - beta_t * S_NLL(...). Results: detection AUROC up to 0.98 on CoQA/SQuAD, 0.97 on TriviaQA; TruthfulQA True+Info of 0.78 on Qwen3-4B (+0.28 improvement); corruption rate reduced to 53.7% vs 26-90% for ungated methods.

**Adaptive Activation Steering / ACT (Wang et al., WWW 2025):**
Uses binary linear classifier probes -- sigmoid(theta, a_l^h) -- to assess truthfulness content in activations and then adaptively steers at the hidden-state level. Steering intensity is modulated by probe output: alpha * (1 - p_probe + beta). Results: LLaMA +142% True*Info (23.1% to 42.3%), LLaMA 2 +24%, Alpaca +36%, Vicuna +28%, LLaMA 2-Chat +19%, LLaMA 3 +34%. Overhead under 2%.

**TruthX (Zhang, Yu, Feng, ACL 2024):**
Uses an autoencoder to map LLM representations into semantic and truthful latent spaces. Contrastive learning identifies a truthful editing direction. Editing one vector in the truthful space steers the model. Improves truthfulness of 13 LLMs by an average of 20% on TruthfulQA.

**WACK (arXiv 2404.09971):**
Categorizes examples by model's prior knowledge, computes representative vectors of hallucinations vs. grounded generations, and steers hidden states. Introduces a dynamic intervention that intervenes only when needed. Finds that attention blocks are effective targets while residual stream intervention is detrimental.

**Calibrating Verbal Uncertainty as a Linear Feature / MUC (Ji et al., EMNLP 2025, Meta FAIR):**
Identifies that verbal uncertainty is mediated by a single direction in representation space. Mechanistic Uncertainty Calibration (MUC) adjusts intervention strength based on the gap between semantic uncertainty and verbal uncertainty. Results: 31.9% relative decrease in hallucination rate; NQ-Open hallucination rate dropped from 40.2% to 26.2%; VU/SU disagreement rate improved from 35.8% to 28.3%.

---

### 5. Papers Specifically Targeting Overconfident Hallucinations with Logit-Level (Not Hidden-State) Interventions

**DoLa -- Decoding by Contrasting Layers (Chuang et al., ICLR 2024):**
Operates purely at the logit level by contrasting logit distributions from later (mature) and earlier (premature) transformer layers. On TruthfulQA, DoLa boosts LLaMA-7B from 25.6% to 32.2% MC1 (a 12-17 percentage point gain across model sizes). It implicitly targets overconfident hallucinations by suppressing shallow high-confidence patterns, but does not explicitly condition on confidence level.

**HAVE -- Head-Adaptive Gating and Value Calibration (arXiv 2509.06596):**
A parameter-free decoding framework that performs instance-level soft reweighing of attention heads and augments attention with value vector magnitudes. Constructs token-level evidence via an "uncertainty-scaled policy" that modulates the LM distribution. Outperforms baselines including DAGCD. Operates at the attention/logit interface without fine-tuning.

**Behaviorally Calibrated RL (Wu et al., arXiv 2512.19920, Dec 2025):**
Trains models via RL with strictly proper scoring rules to stochastically abstain when uncertain. A Qwen3-4B model achieved a log-scale Accuracy-to-Hallucination Ratio gain of 0.806 on BeyondAIME (exceeding GPT-5's 0.207); on SimpleQA, calibration error was on par with frontier models (Grok-4, Gemini-2.5-Pro) despite much lower raw accuracy. This trains the model to avoid overconfident hallucinations rather than intervening at inference time.

**PCNet/PC-LDCD (Nielsen et al., 2026):**
As described above, this is arguably the cleanest example of probe-based detection feeding directly into logit-level intervention (modifying token log-probabilities based on anomaly scores from hidden-state density estimation).

---

### 6. Summary of the Landscape

The field can be organized along two dimensions:

**Detection mechanism:** Hidden-state probes (HACK, CHOKE, ACT, TruthX, MUC) vs. logit-based signals (DoLa, HAVE) vs. density estimation (PCNet).

**Intervention mechanism:** Hidden-state steering (HACK, ACT, TruthX, WACK, MUC) vs. logit/decoding modification (DoLa, HAVE, PCNet/PC-LDCD) vs. training-time (Behaviorally Calibrated RL).

The combination of probe-based detection with logit-level intervention remains relatively rare. Most probe-based methods (HACK, ACT, TruthX) intervene at the hidden-state level. PCNet/PC-LDCD (2026) is the most notable exception, using hidden-state density estimation to gate logit-level corrections. HACK itself uses activation steering (hidden-state intervention) rather than logit intervention, but its CM-Score metric and CM-tuned probes represent an important contribution by showing that general-purpose mitigation methods systematically fail on the overconfident-with-knowledge (CM) quadrant -- the most dangerous hallucination type.

Sources:
- [HACK: Hallucinations Along Certainty and Knowledge Axes](https://arxiv.org/abs/2510.24222)
- [Trust Me, I'm Wrong (CHOKE) - EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.792/)
- [LLMs Know More Than They Show - ICLR 2025](https://arxiv.org/abs/2410.02707)
- [Calibrating Verbal Uncertainty as a Linear Feature - EMNLP 2025](https://arxiv.org/html/2503.14477v1)
- [Adaptive Activation Steering (ACT) - WWW 2025](https://arxiv.org/abs/2406.00034)
- [TruthX - ACL 2024](https://arxiv.org/abs/2402.17811)
- [Hallucination as an Anomaly: PCNet - 2026](https://arxiv.org/html/2605.05953)
- [HAVE: Head-Adaptive Gating and Value Calibration](https://arxiv.org/abs/2509.06596)
- [Behaviorally Calibrated RL](https://arxiv.org/abs/2512.19920)
- [DoLa: Decoding by Contrasting Layers](https://arxiv.org/abs/2309.03883)
- [Constructing Benchmarks and Interventions (WACK)](https://arxiv.org/abs/2404.09971)
- [Hallucination Detection and Mitigation Survey 2026](https://arxiv.org/html/2601.09929v1)
- [Lakera: LLM Hallucinations in 2026](https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models)
- [Suprmind: AI Hallucination Rates & Benchmarks 2026](https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/)

agentId: a3288563be962bcce (use SendMessage with to: 'a3288563be962bcce' to continue this agent)
&lt;usage>total_tokens: 36681
tool_uses: 25
duration_ms: 213700&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcfdb8a9-4e0e-428d-af93-a82131dfda93",
  "isSidechain": false,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "type": "user",
  "uuid": "8e08ab4b-9e0d-4c36-a76e-a2e2d8198d6f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research recent work on overconfident hallucinations and probe-based mitigation. Search for:\n\n1. \"HACK Hallucinations Along Certainty and Knowledge\" by Simhi et al. (arXiv 2510.24222) - Use WebFetch to read https://arxiv.org/abs/2510.24222 - This is a follow-up to CHOKE that adds activation steering\n2. Search for \"overconfident hallucination LLM mitigation 2025 2026\" \n3. Search for \"verbal internal uncertainty mismatch hallucination\"\n4. Search for \"logit level intervention hallucination factuality 2026\"\n5. Search for \"calibration aware decoding hallucination\"\n\nI need to understand:\n- What is HACK's 2x2 framework (Certainty × Knowledge)?\n- What intervention does HACK propose (activation steering)?\n- What results does HACK achieve?\n- Are there any OTHER papers from 2025-2026 that combine probe-based detection with logit-level intervention for hallucination mitigation?\n- Are there papers that specifically target overconfident hallucinations with logit-level (not hidden-state) interventions?\n\nReport comprehensively with specific numbers.",
    "agentId": "a3288563be962bcce",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data. Let me compile the final report.\n\n---\n\n## Comprehensive Report: Overconfident Hallucinations and Probe-Based Mitigation (2024--2026)\n\n---\n\n### 1. HACK: Hallucinations Along Certainty and Knowledge Axes (Simhi et al., arXiv 2510.24222, Oct 2025)\n\n**The 2x2 Framework (Certainty x Knowledge):**\n\nHACK categorizes hallucinations along two orthogonal axes -- Knowledge (does the model encode the correct answer?) and Certainty (does the model express confidence in its hallucinated output?) -- yielding four quadrants:\n\n| | High Certainty (HC+) | Low Certainty (HC-) |\n|---|---|---|\n| **Knowledge Present (HK+)** | **Certainty Misalignment (CM)** -- Model encodes correct information but generates contradictory output with high certainty. This is the most dangerous category. | **Hesitation** -- Model has knowledge but hallucinates with low certainty, suggesting a retrieval failure. |\n| **Knowledge Absent (HK-)** | **Uninformed Guess** -- Lacks correct knowledge yet generates incorrect output with high certainty. | **Informed Hedging** -- Neither encodes correct information nor expresses confidence. |\n\n**How Knowledge is measured:** For each question, 6 answers are generated (1 greedy + 5 sampled at temperature 0.5). HK+ = 6/6 correct; HK- = 0/6 correct. Middle range (<6%) is excluded.\n\n**How Certainty is measured:** Three metrics are used -- (a) token probability of the first generated token, (b) probability difference between top two vocabulary items, and (c) semantic entropy across clustered generations.\n\n**Activation Steering Intervention:**\n\nThe intervention modifies hidden states as: E_v' = E_v + alpha * (F_v - H_v), where F_v and H_v are mean vectors from factual and hallucinated examples respectively. It is applied to 48 attention heads with the highest classification scores. The key insight: steering should substantially improve HK+ cases (where knowledge exists to be \"unlocked\") while minimally affecting HK- cases (where no knowledge exists to steer toward).\n\n**Key Results:**\n\n- **Knowledge distribution:** On TriviaQA, approximately 64-67% of examples are consistently correct (HK+) and 29-32% are never correct (HK-). On Natural Questions, the ratio flips: ~31-35% HK+ and ~60-64% HK-.\n- **Steering validation:** Steering improved HK+ by ~15-21% while affecting HK- by only ~5-7%, confirming the knowledge axis distinction is real.\n  - Gemma-2-9B (Realistic): HK- 4.68% vs HK+ 21.21%\n  - Llama-3.1-8B (Realistic): HK- 4.85% vs HK+ 15.76%\n  - Mistral-7B (Realistic): HK- 6.32% vs HK+ 18.52%\n- **CM prevalence:** 9-43% of HK+ hallucinations occur with high certainty, depending on model and metric. Instruction-tuned models show higher CM rates (22-30%) than base models (10-18%).\n- **CM consistency:** CM examples are significantly more consistent across prompts than random hallucinations (Jaccard similarity: CM 15.8-40.6% vs random 4.3-13.6%; p<0.008).\n- **New metric -- CM-Score:** Measures the proportion of CM (high-certainty, knowledge-present) hallucinations successfully corrected by a mitigation method. This reveals that existing methods that perform well on average \"fail disproportionately on these critical cases.\"\n- **CM-tuned probes** (trained specifically on CM-labeled data) outperform existing general-purpose methods by 1-5%.\n\n**Models tested:** Llama-3.1-8B, Gemma-2-9B, Gemma-2-27B, Mistral-7B-v0.3 (base and instruct variants). **Datasets:** TriviaQA and Natural Questions.\n\n---\n\n### 2. CHOKE: The Predecessor (Simhi et al., \"Trust Me, I'm Wrong,\" arXiv 2502.12964, Feb 2025, EMNLP 2025 Findings)\n\nCHOKE (Certain Hallucinations Overriding Known Evidence) is the precursor to HACK, by several of the same authors (Simhi, Itzhak, Barez, Stanovsky, Belinkov). CHOKE identified the phenomenon but with a simpler classification: a sample is CHOKE if (a) the model knows the correct answer, (b) it hallucinates under a natural prompt, and (c) it hallucinates with certainty exceeding a threshold. CHOKE proposed a probing-based mitigation strategy that outperformed general hallucination mitigation methods on these specific cases. HACK generalizes CHOKE into the full 2x2 taxonomy and adds activation steering as a validation tool.\n\n---\n\n### 3. Related Paper: \"LLMs Know More Than They Show\" (Orgad, Toker, Gekhman, Reichart, Szpektor, Kotek, Belinkov, ICLR 2025)\n\nThis paper from the same research group establishes the foundational observation that LLM internal representations encode far more truthfulness information than what appears in outputs. Key findings: truthfulness information concentrates in specific answer tokens; error detectors fail to generalize across datasets (truthfulness encoding is \"multifaceted,\" not universal); and models may encode the correct answer yet consistently generate an incorrect one. This internal-external discrepancy is precisely what HACK's CM quadrant captures.\n\n---\n\n### 4. Papers Combining Probe-Based Detection with Logit-Level / Decoding-Time Intervention (2024--2026)\n\n**PCNet / PC-LDCD (Nielsen et al., arXiv 2605.05953, May 2026):**\nThis is the most direct example of combining probe-based detection with logit-level intervention. A probabilistic circuit (PCNet) serves as a density estimator over LLM hidden states. At each decoding step, if the negative log-likelihood of the current hidden state exceeds a calibrated threshold, an intervention strength beta_t is computed via sigmoid, and the method penalizes tokens that would deepen hallucinated trajectories by modifying the log-probability: log P_LM(c_i|x_<t) - beta_t * S_NLL(...). Results: detection AUROC up to 0.98 on CoQA/SQuAD, 0.97 on TriviaQA; TruthfulQA True+Info of 0.78 on Qwen3-4B (+0.28 improvement); corruption rate reduced to 53.7% vs 26-90% for ungated methods.\n\n**Adaptive Activation Steering / ACT (Wang et al., WWW 2025):**\nUses binary linear classifier probes -- sigmoid(theta, a_l^h) -- to assess truthfulness content in activations and then adaptively steers at the hidden-state level. Steering intensity is modulated by probe output: alpha * (1 - p_probe + beta). Results: LLaMA +142% True*Info (23.1% to 42.3%), LLaMA 2 +24%, Alpaca +36%, Vicuna +28%, LLaMA 2-Chat +19%, LLaMA 3 +34%. Overhead under 2%.\n\n**TruthX (Zhang, Yu, Feng, ACL 2024):**\nUses an autoencoder to map LLM representations into semantic and truthful latent spaces. Contrastive learning identifies a truthful editing direction. Editing one vector in the truthful space steers the model. Improves truthfulness of 13 LLMs by an average of 20% on TruthfulQA.\n\n**WACK (arXiv 2404.09971):**\nCategorizes examples by model's prior knowledge, computes representative vectors of hallucinations vs. grounded generations, and steers hidden states. Introduces a dynamic intervention that intervenes only when needed. Finds that attention blocks are effective targets while residual stream intervention is detrimental.\n\n**Calibrating Verbal Uncertainty as a Linear Feature / MUC (Ji et al., EMNLP 2025, Meta FAIR):**\nIdentifies that verbal uncertainty is mediated by a single direction in representation space. Mechanistic Uncertainty Calibration (MUC) adjusts intervention strength based on the gap between semantic uncertainty and verbal uncertainty. Results: 31.9% relative decrease in hallucination rate; NQ-Open hallucination rate dropped from 40.2% to 26.2%; VU/SU disagreement rate improved from 35.8% to 28.3%.\n\n---\n\n### 5. Papers Specifically Targeting Overconfident Hallucinations with Logit-Level (Not Hidden-State) Interventions\n\n**DoLa -- Decoding by Contrasting Layers (Chuang et al., ICLR 2024):**\nOperates purely at the logit level by contrasting logit distributions from later (mature) and earlier (premature) transformer layers. On TruthfulQA, DoLa boosts LLaMA-7B from 25.6% to 32.2% MC1 (a 12-17 percentage point gain across model sizes). It implicitly targets overconfident hallucinations by suppressing shallow high-confidence patterns, but does not explicitly condition on confidence level.\n\n**HAVE -- Head-Adaptive Gating and Value Calibration (arXiv 2509.06596):**\nA parameter-free decoding framework that performs instance-level soft reweighing of attention heads and augments attention with value vector magnitudes. Constructs token-level evidence via an \"uncertainty-scaled policy\" that modulates the LM distribution. Outperforms baselines including DAGCD. Operates at the attention/logit interface without fine-tuning.\n\n**Behaviorally Calibrated RL (Wu et al., arXiv 2512.19920, Dec 2025):**\nTrains models via RL with strictly proper scoring rules to stochastically abstain when uncertain. A Qwen3-4B model achieved a log-scale Accuracy-to-Hallucination Ratio gain of 0.806 on BeyondAIME (exceeding GPT-5's 0.207); on SimpleQA, calibration error was on par with frontier models (Grok-4, Gemini-2.5-Pro) despite much lower raw accuracy. This trains the model to avoid overconfident hallucinations rather than intervening at inference time.\n\n**PCNet/PC-LDCD (Nielsen et al., 2026):**\nAs described above, this is arguably the cleanest example of probe-based detection feeding directly into logit-level intervention (modifying token log-probabilities based on anomaly scores from hidden-state density estimation).\n\n---\n\n### 6. Summary of the Landscape\n\nThe field can be organized along two dimensions:\n\n**Detection mechanism:** Hidden-state probes (HACK, CHOKE, ACT, TruthX, MUC) vs. logit-based signals (DoLa, HAVE) vs. density estimation (PCNet).\n\n**Intervention mechanism:** Hidden-state steering (HACK, ACT, TruthX, WACK, MUC) vs. logit/decoding modification (DoLa, HAVE, PCNet/PC-LDCD) vs. training-time (Behaviorally Calibrated RL).\n\nThe combination of probe-based detection with logit-level intervention remains relatively rare. Most probe-based methods (HACK, ACT, TruthX) intervene at the hidden-state level. PCNet/PC-LDCD (2026) is the most notable exception, using hidden-state density estimation to gate logit-level corrections. HACK itself uses activation steering (hidden-state intervention) rather than logit intervention, but its CM-Score metric and CM-tuned probes represent an important contribution by showing that general-purpose mitigation methods systematically fail on the overconfident-with-knowledge (CM) quadrant -- the most dangerous hallucination type.\n\nSources:\n- [HACK: Hallucinations Along Certainty and Knowledge Axes](https://arxiv.org/abs/2510.24222)\n- [Trust Me, I'm Wrong (CHOKE) - EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.792/)\n- [LLMs Know More Than They Show - ICLR 2025](https://arxiv.org/abs/2410.02707)\n- [Calibrating Verbal Uncertainty as a Linear Feature - EMNLP 2025](https://arxiv.org/html/2503.14477v1)\n- [Adaptive Activation Steering (ACT) - WWW 2025](https://arxiv.org/abs/2406.00034)\n- [TruthX - ACL 2024](https://arxiv.org/abs/2402.17811)\n- [Hallucination as an Anomaly: PCNet - 2026](https://arxiv.org/html/2605.05953)\n- [HAVE: Head-Adaptive Gating and Value Calibration](https://arxiv.org/abs/2509.06596)\n- [Behaviorally Calibrated RL](https://arxiv.org/abs/2512.19920)\n- [DoLa: Decoding by Contrasting Layers](https://arxiv.org/abs/2309.03883)\n- [Constructing Benchmarks and Interventions (WACK)](https://arxiv.org/abs/2404.09971)\n- [Hallucination Detection and Mitigation Survey 2026](https://arxiv.org/html/2601.09929v1)\n- [Lakera: LLM Hallucinations in 2026](https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models)\n- [Suprmind: AI Hallucination Rates & Benchmarks 2026](https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/)"
      }
    ],
    "totalDurationMs": 213700,
    "totalTokens": 36681,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1046,
      "cache_read_input_tokens": 32179,
      "output_tokens": 3455,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1046
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3455,
          "cache_read_input_tokens": 32179,
          "cache_creation_input_tokens": 1046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1046,
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
      "otherToolCount": 25
    }
  },
  "sourceToolAssistantUUID": "bcfdb8a9-4e0e-428d-af93-a82131dfda93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T09:37:30.286Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research results. Let me synthesize everything and think deeply about what changes need to be made.

**Key findings from research:**

1. **CHOKE (Schuster et al., EMNLP 2025 Findings):**
   - Actually by Simhi, Itzhak, Barez, Stanovsky, Belinkov (not Schuster)
   - CHOKE = Certain Hallucinations Overriding Known Evidence
   - 16-43% of hallucinations are CHOKE cases
   - Uses logistic regression probe on layer-15 residual stream activations
   - The CHOKE-tuned probe that oversamples CHOKE cases to 65% of training data performs better than alternatives, tested across NQ and TriviaQA with several model sizes, though it only detects and abstains rather than intervening during generation, and it's limited to English QA without causal explanations or optimal mitigation strategies.

2. **HACK (Simhi et al., arXiv 2510.24222, Oct 2025):**
   - Follow-up to CHOKE with 2

x2 framework balancing Knowledge and Certainty, adding activation steering at the hidden-state level to target the dangerous Certainty Misalignment quadrant, which improves high-knowledge cases by 15-21% but only 5-7% for low-knowledge cases, with a CM-Score metric similar to CHOKE-Score.

3. **Attention Divergence Signals (van Dijk, arXiv 2605.05025, May 2026):**
   - Using KL divergence across attention heads as a hallucination detector achieves strong AUROC scores on TruthfulQA and TriviaQA, with most extreme divergence concentrated at named entities, though it's detection-only and outperforms hidden-state probes.

4. **ESR at 8B:**
   - Llama-3.1-8B shows negligible error-seeking rates below 1% compared to 3.8% at 70B scale, making this a non-issue for smaller models.

5. **PC-LDCD code:**
   - The code returns a 403 error and isn't accessible, so I'll need to skip the confusion-matrix analysis for now.

Looking at what's actually novel here—the reviewer has a point that this feels like it's circling. After all the related work, CHOKE and HACK already identify overconfident hallucinations through probes, which MisTAG builds on.  HACK handles activation steering for knowledge-aware cases, PCNet and PC-LDCD do probe-based detection with logit-level intervention, and DoLa and ActLCD already cover logit-level factuality work. The ESR advantage at 8B is too marginal to matter.

What MisTAG actually contributes is the specific combination of VUF confidence and probe hallucination probability as a miscalibration score, the graded response strategy between hedging and rollback, the explicit dual-contribution framing, and the training-free during-generation operation. The confusion-matrix analysis approach is also distinct. But honestly, this is starting to feel more like an engineering combination than a fundamental advance.

The Q2 hypothesis—that at least 15% of hallucinations are on-manifold overconfident cases that density methods miss—is the real scientific claim here, though it's untested and risky. The reviewer's feedback is actually helpful and specific: they're saying the gap to acceptance is mainly about missing related work citations and the ESR narrative. The CHOKE finding showing 16-43% of hallucinations are overconfident actually validates MisTAG's core premise about this being a substantial problem class.

I should focus on targeted fixes rather than a complete rethink. The new framing needs to position MisTAG as specifically addressing the overconfident-hallucination subclass that other methods overlook, cite CHOKE and HACK properly, and reframe ESR as a secondary benefit rather than a core differentiator.

The key distinction is that CHOKE and HACK detect knowledge-aware overconfidence using single-probe residual stream analysis, while MisTAG identifies a verbal-internal calibration mismatch by combining two independent signals—the VUF direction and a factuality probe—into a product score for graded logit-level intervention during generation, rather than just abstention or steering.

Now I'm reconsidering the framing: CHOKE-Score and CM-Score aren't competitors but rather evaluation metrics that validate MisTAG's approach. ESR shifts from being a primary differentiator to an architectural advantage through interpretability and composability at the logit level. The 16-43% overconfidence rates from CHOKE and the Knowledge × Certainty decomposition from HACK both motivate testing whether density methods like PC-LDCD miss these on-manifold cases, and I should use CHOKE-tuned probes as a baseline alongside these evaluation metrics.

Adding HACK's activation steering as another baseline since it's the most relevant intervention to compare against. Looking at the scope of changes—reframing the core problem and opportunity around CHOKE/HACK, adding new baselines and metrics, repositioning ESR—this is substantial repositioning work, though the underlying method of miscalibration scoring and logit-level intervention remains intact.

But actually, I should dig deeper into what truly sets MisTAG apart from HACK. The key differentiators are the detection mechanism—combining VUF confidence and probe probability multiplicatively rather than relying on a single probe—and the intervention approach of logit-level bias with rollback instead of hidden-state activation steering. CHOKE and HACK also operate on shorter-form QA tasks, which is a narrower scope than what I'm working with. MisTAG targets long-form generation (FActScore biographies). This is a significant scope extension.

4. **Graded response**: CHOKE does binary abstention. HACK does fixed-strength steering. MisTAG does graded response (hedge for mild, rollback for severe). This is genuinely novel.

5. **Calibration focus**: CHOKE/HACK care about correctness. MisTAG explicitly separates calibration (OHR/ECE) from factuality (FActScore). This dual-contribution framing is novel.

6. **Training-free**: All methods require some form of fitting to data—CHOKE needs a tuned probe, HACK needs steering vectors from labeled examples, and MisTAG needs the factuality probe trained, though the VUF extraction is unsupervised and the logit bias vectors are pre-defined, which is a simplicity advantage.

The differentiation is real but I need to articulate it more sharply. HACK introduced activation steering as an intervention, and I can position MisTAG as building on the insight that overconfident hallucinations are a critical failure mode, but with advantages over their approaches: a multiplicative miscalibration score combining verbal confidence with probe-based uncertainty for finer-grained detection, logit-level intervention for interpretability and composability, and graded response handling.

Now I'm recalculating the Monitoring Decoding correction—38.2% to 44.1% is 5.9 absolute points, which is 15.4% relative improvement. I need to report this correctly.

I'm drafting the revised JSON as a major revision since the problem framing, landscape, and evaluation plan all shift substantially, even though the core method remains the same. The key changes involve repositioning MisTAG as extending CHOKE/HACK's findings, adding those papers to the landscape, and clarifying the novel contributions around graded response and calibration-focused evaluation.

Wait, I'm noticing the reviewer cites "Schuster et al., EMNLP 2025 Findings" but the actual paper appears to be by Simhi et al. with different authors. I should verify whether this is a reviewer error or if there's another paper I'm missing before finalizing the references. I'm going back and forth on how to cite this - the research clearly shows Simhi et al. as the authors with arXiv ID 2502.12964, but the reviewer mentioned "Schuster et al." I should probably just go with the correct attribution I found in the research report and reference it by the arXiv ID to be thorough.

Now I need to revise the JSON to better position MisTAG's contributions: I'll acknowledge CHOKE/HACK's work on overconfident hallucinations as the foundation, then reframe MisTAG's novelty around the specific intervention approach (logit-level modifications) and scope (long-form generation) rather than claiming detection is entirely new, show ESR as a forward-looking safeguard rather than an immediate practical advantage, and correct the Monitoring Decoding metrics. For the opportunity section, I'll build on what CHOKE/HACK established to motivate why MisTAG matters, clarify that while detection is related, the multiplicative scoring approach is distinct from single-probe methods, and emphasize that the logit-level intervention is genuinely different from abstention-based approaches.

In the landscape, I need to add the CHOKE and HACK papers with proper citations, include the attention divergence work, fix the Monitoring Decoding numbers, and reframe ESR appropriately. For the approach, I'll add CHOKE-tuned and HACK-based baselines, introduce CHOKE-Score and CM-Score as evaluation metrics, reframe ESR-immunity as an interpretability and robustness benefit, and correct the Monitoring Decoding comparison. This is a substantial reframing of how the work positions itself relative to prior art, though the core methodology remains unchanged.

I should also reconsider whether the confusion matrix experiment still makes sense given CHOKE's findings about what makes hallucinations detectable.

CHOKE shows that 16-43% of hallucinations are overconfident, which actually aligns well with MisTAG's Q2 hypothesis that at least 15% of hallucinated facts are on-manifold but miscalibrated. These findings are complementary—CHOKE validates that a substantial portion of hallucinations do come with high internal confidence, which should produce on-manifold hidden states, strengthening the motivation for Q2. The main improvement would be positioning the problem more honestly and clearly relative to what we now know about hallucination characteristics.

The upgrades I'm considering are adding a multiplicative miscalibration score, logit-level interventions, graded responses, and long-form generation evaluation to extend beyond CHOKE/HACK, plus using CHOKE-Score and CM-Score as baselines with a CHOKE-tuned probe. This stronger evaluation plan combined with better grounding in existing work and clearer differentiation should push the paper from solid-to-strong toward genuinely strong, though I'm still settling on whether to keep that level designation or adjust it slightly given the more robust positioning.

Now I'm drafting the JSON structure, starting with the core problem section where I'll ground everything in CHOKE/HACK's validated finding that 16-43% of hallucinations are overconfident, then map out the specific gaps in current detection and intervention approaches before positioning MisTAG as the solution. I need to add CHOKE-tuned probe and HACK steering as baselines to validate our approach, compute CHOKE-Score metrics for evaluation, and briefly acknowledge attention divergence as related detection work. I should also add the missing CHOKE reference and fix the Monitoring Decoding numbers. I need to clarify the exact ESR numbers from the research—the baseline for Llama-3.1-70B is 3.8% for single attempts and 7.4% for multi-attempt, but with meta-prompting it jumps to 14.8% and 31.7% respectively, so the reviewer's "25%+" reference likely points to the enhanced rate. Now I'll draft the complete JSON revision with these precise figures and mark it as a major change since the framing shifts substantially.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e08ab4b-9e0d-4c36-a76e-a2e2d8198d6f",
  "isSidechain": false,
  "requestId": "req_011Cb629hzBYodV1GqYMfS4k",
  "type": "assistant",
  "uuid": "e83f475f-3411-4c05-b4aa-9ece81fd6193",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCwnJSbQrviTEvDjHJYfVi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1986,
      "cache_creation_input_tokens": 7207,
      "cache_read_input_tokens": 33007,
      "output_tokens": 5710,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1986,
          "output_tokens": 5710,
          "cache_read_input_tokens": 33007,
          "cache_creation_input_tokens": 7207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7207
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

_source line 24 · 2026-05-16T09:37:35.837Z_

Now I have comprehensive research on all the key papers. Let me synthesize my findings before drafting the revision.

**Key insights from research:**

1. **CHOKE** (Simhi et al., not Schuster — reviewer may have confused the name): Layer-15 logistic regression probe on residual stream; 16-43% of hallucinations are CHOKE cases; detection + abstention only, no during-generation intervention; QA only (NQ, TriviaQA)

2. **HACK** (Simhi et al., follow-up): 2x2 framework (Knowledge × Certainty); adds activation steering (hidden-state, not logit-level); CM-Score metric; improves HK+ by ~15-21%

3. **Attention Divergence** (van Dijk): KL divergence of attention heads; AUROC 0.89-0.91 on TruthfulQA; detection only, no intervention; 66.5% of extreme divergence at named entities

4. **ESR confirmed**: <1% at 8B, 3.8% at 70B baseline — reviewer is right, ESR-immunity is practically irrelevant at evaluation scale

5. **PC-LDCD code**: Returns 403, not accessible — confusion matrix analysis likely needs deferral

The CHOKE/HACK findings actually *strengthen* MisTAG's motivation by validating that overconfident hallucinations are 16-43% of cases. But the differentiation must be sharpened: CHOKE uses single-probe detection + abstention; HACK uses single-probe + hidden-state steering on QA. MisTAG uses multiplicative miscalibration score + logit-level intervention on long-form generation.

This is a **major revision** of the framing and positioning, though the core method stays intact. Let me draft the complete revised idea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e83f475f-3411-4c05-b4aa-9ece81fd6193",
  "isSidechain": false,
  "requestId": "req_011Cb629hzBYodV1GqYMfS4k",
  "type": "assistant",
  "uuid": "ec1848d9-c64c-43df-b3d7-1f0b4120823f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCwnJSbQrviTEvDjHJYfVi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1986,
      "cache_creation_input_tokens": 7207,
      "cache_read_input_tokens": 33007,
      "output_tokens": 5710,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1986,
          "output_tokens": 5710,
          "cache_read_input_tokens": 33007,
          "cache_creation_input_tokens": 7207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7207
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

_source line 25 · 2026-05-16T09:37:36.179Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Um8D5a81dFcruAuhwjJd6a`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec1848d9-c64c-43df-b3d7-1f0b4120823f",
  "isSidechain": false,
  "requestId": "req_011Cb629hzBYodV1GqYMfS4k",
  "type": "assistant",
  "uuid": "622efe73-4f5d-4965-8093-16684f76aea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCwnJSbQrviTEvDjHJYfVi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1986,
      "cache_creation_input_tokens": 7207,
      "cache_read_input_tokens": 33007,
      "output_tokens": 5710,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1986,
          "output_tokens": 5710,
          "cache_read_input_tokens": 33007,
          "cache_creation_input_tokens": 7207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7207
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

_source line 26 · 2026-05-16T09:37:36.186Z_

<details><summary>↩ Tool result · `toolu_01Um8D5a81dFcruAuhwjJd6a`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "622efe73-4f5d-4965-8093-16684f76aea9",
  "isSidechain": false,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "type": "user",
  "uuid": "5666071f-e68c-43f6-9754-efed2ec8922c",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "622efe73-4f5d-4965-8093-16684f76aea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Miscalibration-Triggered Adaptive Generation via Logit-Level Intervent…",
  "leafUuid": "5666071f-e68c-43f6-9754-efed2ec8922c",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise MisTAG: CHOKE integration, ESR reframing, and Q2 hypothesis grounding",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6"
}
```

---

### Assistant

_source line 29 · 2026-05-16T09:37:39.259Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do one more targeted search to verify the CHOKE paper authorship and check if there's any very recent work I should know about.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5666071f-e68c-43f6-9754-efed2ec8922c",
  "isSidechain": false,
  "requestId": "req_011Cb62JSBfwhRNt6WpaiUrH",
  "type": "assistant",
  "uuid": "35f27712-c7e9-4306-b2db-274ad036b719",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXWk49j7H9bYC6GNBxaXMT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8211,
      "cache_read_input_tokens": 40214,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8211,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 185,
          "cache_read_input_tokens": 40214,
          "cache_creation_input_tokens": 8211,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8211
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

_source line 30 · 2026-05-16T09:37:39.705Z_

Let me do one final verification search before writing the revision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35f27712-c7e9-4306-b2db-274ad036b719",
  "isSidechain": false,
  "requestId": "req_011Cb62JSBfwhRNt6WpaiUrH",
  "type": "assistant",
  "uuid": "b87547f4-144f-4255-847b-4f5dce5d809a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXWk49j7H9bYC6GNBxaXMT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8211,
      "cache_read_input_tokens": 40214,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8211,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 185,
          "cache_read_input_tokens": 40214,
          "cache_creation_input_tokens": 8211,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8211
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

_source line 31 · 2026-05-16T09:37:40.790Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uo1NPTfy5xWFdGJXXG7oqw`</summary>

```json
{
  "query": "arXiv 2502.12964 \"Trust Me I'm Wrong\" CHOKE hallucination authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b87547f4-144f-4255-847b-4f5dce5d809a",
  "isSidechain": false,
  "requestId": "req_011Cb62JSBfwhRNt6WpaiUrH",
  "type": "assistant",
  "uuid": "cf9dceb1-4358-4fe7-b3d0-09139c81fbc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXWk49j7H9bYC6GNBxaXMT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8211,
      "cache_read_input_tokens": 40214,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8211,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 185,
          "cache_read_input_tokens": 40214,
          "cache_creation_input_tokens": 8211,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8211
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

_source line 32 · 2026-05-16T09:37:41.057Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KcqL6qQHmT9JrefJ7SU28z`</summary>

```json
{
  "query": "logit level intervention overconfident hallucination long-form generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf9dceb1-4358-4fe7-b3d0-09139c81fbc0",
  "isSidechain": false,
  "requestId": "req_011Cb62JSBfwhRNt6WpaiUrH",
  "type": "assistant",
  "uuid": "f462577f-2c3d-4329-b8b6-0034a90d7680",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXWk49j7H9bYC6GNBxaXMT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8211,
      "cache_read_input_tokens": 40214,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8211,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 185,
          "cache_read_input_tokens": 40214,
          "cache_creation_input_tokens": 8211,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8211
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

_source line 33 · 2026-05-16T09:37:48.781Z_

<details><summary>↩ Tool result · `toolu_01KcqL6qQHmT9JrefJ7SU28z`</summary>

```text
Web search results for query: "logit level intervention overconfident hallucination long-form generation 2026"

Links: [{"title":"From Illusion to Insight: A Taxonomic Survey of Hallucination Mitigation Techniques in LLMs","url":"https://www.mdpi.com/2673-2688/6/10/260"},{"title":"Mitigating Hallucination in Large Vision-Language Models via Adaptive Attention Calibration","url":"https://arxiv.org/html/2505.21472v2"},{"title":"Large Language Models Hallucination: A Comprehensive Survey","url":"https://arxiv.org/html/2510.06265v2"},{"title":"(PDF) A Survey of Hallucination Problems Based on Large Language Models","url":"https://www.researchgate.net/publication/386139221_A_Survey_of_Hallucination_Problems_Based_on_Large_Language_Models"},{"title":"Hallucination, monofacts, and miscalibration: An empirical investigation - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12933039/"},{"title":"GitHub - NishilBalar/Awesome-LVLM-Hallucination: up-to-date curated list of state-of-the-art Large vision language models hallucinations research work, papers & resources · GitHub","url":"https://github.com/NishilBalar/Awesome-LVLM-Hallucination"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"1 Large Language Models Hallucination: A Comprehensive Survey","url":"https://arxiv.org/pdf/2510.06265"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"(PDF) A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation","url":"https://www.researchgate.net/publication/396593833_A_Survey_on_Hallucination_in_Large_Language_Models_Definitions_Detection_and_Mitigation"}]

Based on the search results, I found relevant research on logit-level interventions for addressing hallucination challenges in language models, particularly in long-form generation contexts:

## Key Findings

**Logit-Level Interventions for Hallucination Mitigation:**

Logit-level interventions refine decoding by interpreting/manipulating probabilities during generation. These approaches are part of broader strategies to address hallucination in large language models.

**Addressing Overconfident Hallucinations:**

Large vision-language models often confidently describe objects or attributes not present in the image, and current training-free interventions struggle to maintain accuracy in open-ended and long-form generation scenarios. Recent work like the Confidence-Aware Attention Calibration (CAAC) framework targets spatial perception bias and modality bias through Visual-Token Calibration and Adaptive Attention Re-Scaling guided by the model's confidence to ensure consistent visual alignment during generation.

**Confidence-Based Approaches:**

Confidence-aware search variants use epistemic uncertainty to steer beams toward more faithful continuations, with higher predictive uncertainty correlating with greater hallucination risk.

**Training Data Approaches:**

Recent research from 2026 shows that hallucination can be controlled through deliberate manipulation of training data frequency distributions, reducing hallucination rates by up to 40% without sacrificing accuracy.

The search results reveal an active area of research focused on combining logit-level manipulations with confidence-aware mechanisms to better handle long-form generation and overconfident hallucinations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f462577f-2c3d-4329-b8b6-0034a90d7680",
  "isSidechain": false,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "type": "user",
  "uuid": "67c2e16a-db9e-4a38-a4e1-3b40277da86f",
  "toolUseResult": {
    "query": "logit level intervention overconfident hallucination long-form generation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UiWhdYJfS4ScyVQpCcjKJF",
        "content": [
          {
            "title": "From Illusion to Insight: A Taxonomic Survey of Hallucination Mitigation Techniques in LLMs",
            "url": "https://www.mdpi.com/2673-2688/6/10/260"
          },
          {
            "title": "Mitigating Hallucination in Large Vision-Language Models via Adaptive Attention Calibration",
            "url": "https://arxiv.org/html/2505.21472v2"
          },
          {
            "title": "Large Language Models Hallucination: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2510.06265v2"
          },
          {
            "title": "(PDF) A Survey of Hallucination Problems Based on Large Language Models",
            "url": "https://www.researchgate.net/publication/386139221_A_Survey_of_Hallucination_Problems_Based_on_Large_Language_Models"
          },
          {
            "title": "Hallucination, monofacts, and miscalibration: An empirical investigation - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12933039/"
          },
          {
            "title": "GitHub - NishilBalar/Awesome-LVLM-Hallucination: up-to-date curated list of state-of-the-art Large vision language models hallucinations research work, papers & resources · GitHub",
            "url": "https://github.com/NishilBalar/Awesome-LVLM-Hallucination"
          },
          {
            "title": "A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org",
            "url": "https://www.preprints.org/manuscript/202510.0540/v1"
          },
          {
            "title": "1 Large Language Models Hallucination: A Comprehensive Survey",
            "url": "https://arxiv.org/pdf/2510.06265"
          },
          {
            "title": "GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub",
            "url": "https://github.com/EdinburghNLP/awesome-hallucination-detection"
          },
          {
            "title": "(PDF) A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation",
            "url": "https://www.researchgate.net/publication/396593833_A_Survey_on_Hallucination_in_Large_Language_Models_Definitions_Detection_and_Mitigation"
          }
        ]
      },
      "Based on the search results, I found relevant research on logit-level interventions for addressing hallucination challenges in language models, particularly in long-form generation contexts:\n\n## Key Findings\n\n**Logit-Level Interventions for Hallucination Mitigation:**\n\nLogit-level interventions refine decoding by interpreting/manipulating probabilities during generation. These approaches are part of broader strategies to address hallucination in large language models.\n\n**Addressing Overconfident Hallucinations:**\n\nLarge vision-language models often confidently describe objects or attributes not present in the image, and current training-free interventions struggle to maintain accuracy in open-ended and long-form generation scenarios. Recent work like the Confidence-Aware Attention Calibration (CAAC) framework targets spatial perception bias and modality bias through Visual-Token Calibration and Adaptive Attention Re-Scaling guided by the model's confidence to ensure consistent visual alignment during generation.\n\n**Confidence-Based Approaches:**\n\nConfidence-aware search variants use epistemic uncertainty to steer beams toward more faithful continuations, with higher predictive uncertainty correlating with greater hallucination risk.\n\n**Training Data Approaches:**\n\nRecent research from 2026 shows that hallucination can be controlled through deliberate manipulation of training data frequency distributions, reducing hallucination rates by up to 40% without sacrificing accuracy.\n\nThe search results reveal an active area of research focused on combining logit-level manipulations with confidence-aware mechanisms to better handle long-form generation and overconfident hallucinations."
    ],
    "durationSeconds": 7.721495767000015
  },
  "sourceToolAssistantUUID": "f462577f-2c3d-4329-b8b6-0034a90d7680",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T09:37:52.295Z_

<details><summary>↩ Tool result · `toolu_01Uo1NPTfy5xWFdGJXXG7oqw`</summary>

```text
Web search results for query: "arXiv 2502.12964 "Trust Me I'm Wrong" CHOKE hallucination authors"

Links: [{"title":"[2502.12964] Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer","url":"https://arxiv.org/abs/2502.12964"},{"title":"Trust Me, I’m Wrong: High-Certainty Hallucinations in LLMs","url":"https://arxiv.org/html/2502.12964v1"},{"title":"Trust Me, I’m Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer","url":"https://arxiv.org/html/2502.12964v2"},{"title":"Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250212964S/abstract"},{"title":"Understanding and Mitigating Strategies for Large Language Model (LLMs) Hallucinations in HR Chatbots | International Journal of Computational and Experimental Science and Engineering","url":"https://www.ijcesen.com/index.php/ijcesen/article/view/2471"},{"title":"LLMs Hallucinate with Certainty Despite Knowing the Answer","url":"https://www.alphaxiv.org/overview/2502.12964v2"},{"title":"Why Language Models Hallucinate","url":"https://arxiv.org/html/2509.04664v1"},{"title":"LLMs Hallucinate with Certainty Despite Knowing the Answer","url":"https://aclanthology.org/2025.findings-emnlp.792.pdf"},{"title":"Lost in Transcription, Found in Distribution Shift: Demystifying Hallucination in Speech Foundation Models","url":"https://arxiv.org/html/2502.12414v1"},{"title":"What are Models Thinking about? Understanding Large Language Model Hallucinations through Model Internal State Analysis","url":"https://arxiv.org/html/2502.13490v1"}]

Based on the search results, here is the information about arXiv paper 2502.12964:

## Paper Details

**Title:** Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer

**Authors:** Adi Simhi, Itay Itzhak, Fazl Barez, Gabriel Stanovsky, Yonatan Belinkov

**Submission Date:** Submitted on 18 Feb 2025 (v1), last revised 25 Aug 2025 (this version, v2)

## Key Concept: CHOKE

CHOKE (Certain Hallucinations Overriding Known Evidence) is particularly concerning in high-stakes domains such as medicine or law, where model certainty is often used as a proxy for reliability.

The paper investigates a distinct type of hallucination, where a model can consistently answer a question correctly, but a seemingly trivial perturbation, which can happen in real-world settings, causes it to produce a hallucinated response with high certainty.

## Main Findings

CHOKE examples are consistent across prompts, occur in different models and datasets, and are fundamentally distinct from other hallucinations. This difference leads existing mitigation methods to perform worse on CHOKE examples than on general hallucinations.

The paper introduces a probing-based mitigation that outperforms existing methods on CHOKE hallucinations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf9dceb1-4358-4fe7-b3d0-09139c81fbc0",
  "isSidechain": false,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "type": "user",
  "uuid": "1ad30ca2-abfa-44d1-9797-cf6958c075aa",
  "toolUseResult": {
    "query": "arXiv 2502.12964 \"Trust Me I'm Wrong\" CHOKE hallucination authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TXSR8Uz2Ddyqtq44Wwc8yn",
        "content": [
          {
            "title": "[2502.12964] Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer",
            "url": "https://arxiv.org/abs/2502.12964"
          },
          {
            "title": "Trust Me, I’m Wrong: High-Certainty Hallucinations in LLMs",
            "url": "https://arxiv.org/html/2502.12964v1"
          },
          {
            "title": "Trust Me, I’m Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer",
            "url": "https://arxiv.org/html/2502.12964v2"
          },
          {
            "title": "Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250212964S/abstract"
          },
          {
            "title": "Understanding and Mitigating Strategies for Large Language Model (LLMs) Hallucinations in HR Chatbots | International Journal of Computational and Experimental Science and Engineering",
            "url": "https://www.ijcesen.com/index.php/ijcesen/article/view/2471"
          },
          {
            "title": "LLMs Hallucinate with Certainty Despite Knowing the Answer",
            "url": "https://www.alphaxiv.org/overview/2502.12964v2"
          },
          {
            "title": "Why Language Models Hallucinate",
            "url": "https://arxiv.org/html/2509.04664v1"
          },
          {
            "title": "LLMs Hallucinate with Certainty Despite Knowing the Answer",
            "url": "https://aclanthology.org/2025.findings-emnlp.792.pdf"
          },
          {
            "title": "Lost in Transcription, Found in Distribution Shift: Demystifying Hallucination in Speech Foundation Models",
            "url": "https://arxiv.org/html/2502.12414v1"
          },
          {
            "title": "What are Models Thinking about? Understanding Large Language Model Hallucinations through Model Internal State Analysis",
            "url": "https://arxiv.org/html/2502.13490v1"
          }
        ]
      },
      "Based on the search results, here is the information about arXiv paper 2502.12964:\n\n## Paper Details\n\n**Title:** Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer\n\n**Authors:** Adi Simhi, Itay Itzhak, Fazl Barez, Gabriel Stanovsky, Yonatan Belinkov\n\n**Submission Date:** Submitted on 18 Feb 2025 (v1), last revised 25 Aug 2025 (this version, v2)\n\n## Key Concept: CHOKE\n\nCHOKE (Certain Hallucinations Overriding Known Evidence) is particularly concerning in high-stakes domains such as medicine or law, where model certainty is often used as a proxy for reliability.\n\nThe paper investigates a distinct type of hallucination, where a model can consistently answer a question correctly, but a seemingly trivial perturbation, which can happen in real-world settings, causes it to produce a hallucinated response with high certainty.\n\n## Main Findings\n\nCHOKE examples are consistent across prompts, occur in different models and datasets, and are fundamentally distinct from other hallucinations. This difference leads existing mitigation methods to perform worse on CHOKE examples than on general hallucinations.\n\nThe paper introduces a probing-based mitigation that outperforms existing methods on CHOKE hallucinations."
    ],
    "durationSeconds": 11.502141186999973
  },
  "sourceToolAssistantUUID": "cf9dceb1-4358-4fe7-b3d0-09139c81fbc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-16T09:37:52.298Z_

```json
{
  "parentUuid": "1ad30ca2-abfa-44d1-9797-cf6958c075aa",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f9cc448b-edad-4bfa-bbb1-0f13230cf846",
  "timestamp": "2026-05-16T09:37:52.298Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 36 · 2026-05-16T09:37:59.721Z_

<details><summary>Logged reasoning block</summary>

```text
Good, confirmed: the CHOKE paper is by **Simhi et al.** (Adi Simhi, Itay Itzhak, Fazl Barez, Gabriel Stanovsky, Yonatan Belinkov), not "Schuster et al." as the reviewer stated. The reviewer made an error on the author name. I'll use the correct attribution in my revision.

The second search didn't reveal any new papers that I'm missing. Good.

Now let me draft the complete revised JSON. This will be a "major" revision because:
1. Core problem reframing to acknowledge CHOKE/HACK


2. Significant landscape additions
3. ESR reframing throughout
4. New baselines and metrics
5. Monitoring Decoding correction

But the core method (miscalibration score → graded logit-level intervention) stays the same. Let me write this carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9cc448b-edad-4bfa-bbb1-0f13230cf846",
  "isSidechain": false,
  "requestId": "req_011Cb62Kcc1cGVp2sDLbiw17",
  "type": "assistant",
  "uuid": "52c4e79a-3aa9-46e3-904a-d8adc1966f36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdhJ4CwwJiP6hwvMDDF3Bn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 987,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 48425,
      "output_tokens": 10681,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 987,
          "output_tokens": 10681,
          "cache_read_input_tokens": 48425,
          "cache_creation_input_tokens": 1175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1175
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

_source line 37 · 2026-05-16T09:41:56.505Z_

Confirmed: CHOKE paper is by **Simhi et al.** (not Schuster — reviewer error on the name). Now I have all the research I need. Let me draft the comprehensive revision.

The core insight from my research: CHOKE/HACK actually *strengthen* MisTAG's premise (16-43% of hallucinations are overconfident) but require sharp differentiation on: (1) detection signal (multiplicative score vs. single probe), (2) intervention type (logit-level vs. abstention/steering), (3) scope (long-form vs. QA), and (4) graded response. ESR must be reframed as future-proofing, not primary differentiator. This is a **major revision** of framing while preserving the core method.

```json
{
  "title": "Miscalibration-Triggered Adaptive Generation via Logit-Level Intervention",
  "change_type": "major",
  "core_problem": "Overconfident hallucinations—where an LLM asserts falsehoods with high verbal confidence despite internal epistemic uncertainty—are the most user-deceptive failure mode. Simhi et al. (EMNLP 2025 Findings) quantified this phenomenon as CHOKE (Certain Hallucinations Overriding Known Evidence), showing 16–43% of hallucinations occur with high certainty despite the model possessing correct knowledge, and the follow-up HACK framework (Simhi et al., arXiv 2510.24222) validated the Knowledge × Certainty decomposition via activation steering. Standard factuality metrics (FActScore, TruthfulQA) treat all hallucinations equally, but CHOKE-type overconfident ones are disproportionately harmful because users cannot distinguish them from accurate claims—and existing mitigation methods systematically underperform on them (CHOKE-Score analysis). Existing inference-time mitigation methods each have critical limitations for addressing this validated phenomenon: (1) CHOKE/HACK's own interventions—abstention and hidden-state activation steering on 48 attention heads—are evaluated only on short-form QA (NQ, TriviaQA), reducing coverage (abstention) or operating in the residual stream (steering) without addressing long-form generation where overconfident hallucinations are most harmful to users consuming streaming output; (2) Token-Guard (ICLR 2026) performs training-free token-level control via hidden-state self-checking but has no calibration awareness—it treats all hallucinations equally regardless of expressed confidence, systematically missing the CHOKE-type failure mode; (3) FactCheckmate requires training classifiers and intervenes pre-generation, precluding during-streaming correction; (4) density-estimation approaches (PC-LDCD) detect hallucinations as geometric anomalies but we hypothesize they face a blind spot on overconfident hallucinations where hidden states appear on-manifold—a hypothesis now grounded in CHOKE's finding that 16–43% of hallucinations are produced with high confidence despite internal knowledge, suggesting confidently-wrong trajectories may be geometrically similar to confidently-correct ones; (5) contrastive decoding (DoLa, ActLCD) operates at the logit level but without calibration awareness—intervening uniformly rather than targeting the specific overconfident failure mode; (6) calibration-aware methods (CAG, CURE) require model fine-tuning; and (7) post-generation approaches (CSS) cannot prevent overconfident hallucinations from being generated during streaming. The fundamental gap: overconfident hallucinations are now a quantified phenomenon (CHOKE/HACK), but no method combines a calibration-aware detection signal—specifically targeting the verbal-internal mismatch characteristic of CHOKE-type failures—with training-free during-generation logit-level intervention for long-form text, providing both calibration correction and factuality improvement as separable contributions.",
  "opportunity": "CHOKE (Simhi et al., EMNLP 2025 Findings) and HACK (Simhi et al., Oct 2025) established that overconfident hallucinations are a substantial and consistent failure mode (16–43% prevalence, significantly above-chance Jaccard similarity across prompt perturbations), and that standard mitigation methods—including certainty-based abstention and prompting—systematically fail on these cases. Their CHOKE-tuned probes (logistic regression on layer-15 residual stream activations, oversampling CHOKE examples to 65% of training data) outperform all other approaches, and HACK's activation steering on 48 attention heads improves knowledge-present hallucinations by ~15–21%. However, both are evaluated only on short-form QA and intervene via abstention (CHOKE) or hidden-state steering (HACK). Ji et al. (EMNLP 2025, SAC Highlight) proved verbal-internal uncertainty mismatch predicts hallucinations better than uncertainty alone via the VUF direction, validated on Llama-3.1-8B (31.9% relative hallucination reduction), Mistral-7B, and Qwen2.5-7B. Token-Guard (ICLR 2026) demonstrated training-free token-level hallucination control via self-checking decoding with iterative pruning/regeneration on Llama-3.1-8B and Qwen3-8B, but without calibration awareness. PC-LDCD (May 2026) achieves AUROC up to 99% for hallucination detection via density estimation, but its aggregate metrics do not separate overconfident from uncertain hallucinations. CSS (April 2026) demonstrated post-generation calibration-aware specificity backoff (0.913 overcommitment-aware utility), proving the value of calibration-aware output control but unable to intervene during streaming. The opportunity: synthesize CHOKE/HACK's validated detection of overconfident hallucinations with Ji et al.'s VUF signal into a novel multiplicative miscalibration score, then pair this calibration-aware trigger with logit-level intervention—which offers interpretability (the bias vector explicitly shows which tokens are promoted/suppressed) and composability advantages over hidden-state manipulation—for training-free during-generation control of long-form text, with graded responses from hedging to rollback and honest separation of calibration vs. factuality contributions.",
  "landscape": "**Overconfident hallucination detection and mitigation**: CHOKE (Simhi, Itzhak, Barez, Stanovsky, Belinkov; EMNLP 2025 Findings, arXiv 2502.12964) identified and quantified the CHOKE phenomenon: 16–43% of hallucinations occur with high certainty despite the model encoding correct knowledge. Detection uses logistic regression on layer-15 residual stream activations; the CHOKE-tuned probe oversamples CHOKE cases to 65% of training data, outperforming certainty-based and prompting methods. Evaluated on NQ and TriviaQA with Llama-3.1-8B, Mistral-7B, Gemma-2-9B/27B. Limitations: short-form QA only, abstention-based mitigation (reduces coverage), no during-generation intervention, single-probe detection without VUF-style calibration signals. The predecessor work 'LLMs Know More Than They Show' (Orgad et al., ICLR 2025) established that internal representations encode truthfulness information concentrated in specific tokens, grounding the probe approach. HACK (Simhi et al., arXiv 2510.24222, Oct 2025) generalizes CHOKE into a 2×2 framework (Knowledge × Certainty), identifies the Certainty Misalignment (CM) quadrant as the most dangerous, and adds activation steering on 48 attention heads as intervention. Steering improves knowledge-present (HK+) hallucinations by ~15–21% but knowledge-absent (HK-) by only ~5–7%, validating the knowledge axis. CM-Score metric reveals that general mitigation methods fail disproportionately on CM cases. HACK intervenes via hidden-state steering and evaluates on short-form QA only.\n\n**Hidden-state intervention approaches**: Ji et al. (EMNLP 2025, SAC Highlight) showed ~30% reduction in overconfident hallucinations via linear activation intervention on the VUF direction across Llama-3.1-8B (most responsive), Mistral-7B, and Qwen2.5-7B, but only for short-form answers with binary logic, operating in the residual stream. Token-Guard (Zhu et al., ICLR 2026, arXiv 2601.21969) performs training-free token-level hallucination control via self-checking decoding: scores candidate tokens using a hybrid of hidden-state cosine similarity (penultimate layer) and token probability, then applies iterative pruning and regeneration. Validated on Llama-3.1-8B and Qwen3-8B (FinanceBench, DROP, CovidQA, PubMedQA, HaluEval, RAGTruth) but does not evaluate on TruthfulQA or FActScore and has no calibration awareness—it treats all hallucinations equally regardless of expressed confidence. FactCheckmate (Alnuhait et al., arXiv 2410.02899) trains hidden-state classifiers achieving 34.4% factuality improvement on QA datasets but requires task-specific classifier training and intervenes pre-generation only.\n\n**ESR and scaling considerations**: ESR (arXiv 2602.06941, Feb 2026) demonstrates that Llama-3.3-70B actively resists activation steering mid-generation via 26 dedicated SAE latents, with baseline ESR rate of 3.8% (7.4% multi-attempt) at 70B scale, increasing to 14.8% (31.7% multi-attempt) with meta-prompting. At 8B scale (Llama-3.1-8B), ESR is <1%. ESR establishes that hidden-state intervention becomes an increasingly fragile pathway as models scale, but is not a practical concern at 8B evaluation scale.\n\n**Density-based detection**: PC-LDCD (Nielsen et al., arXiv 2605.05953, May 2026) trains PCNet over the residual stream to detect hallucinations as geometric anomalies, triggering selective contrastive decoding; achieves TruthfulQA True+Info up to 0.78 on Qwen3-4B and AUROC up to 99% across Llama-3.2-1B/3B, Qwen3-4B, and Mistral-Small-24B. PC-LDCD's stated limitations are calibration data requirements, evaluation limited to models up to 8B, and stronger gains on generative than exact-match tasks. We additionally hypothesize—grounded in CHOKE's finding that 16–43% of hallucinations are produced with high confidence—that density-based detection faces a blind spot on overconfident hallucinations where hidden states appear on-manifold because the model confidently produces incorrect tokens along geometrically normal trajectories.\n\n**Internal uncertainty signals**: van Dijk (arXiv 2605.05025, May 2026, ACL SRW 2026) proposes using KL divergence of attention heads as a lightweight hallucination detection signal, achieving AUROC 0.89–0.91 on TruthfulQA across Llama-3.2-3B, Qwen3-4B, and Mistral-7B. Token-level analysis shows 66.5% of extreme divergence occurs at named entities and numbers. This is concurrent detection-only work using attention matrices rather than residual-stream activations, complementary to probe-based approaches.\n\n**Contrastive decoding**: DoLa (ICLR 2024) contrasts logits across layers (+12–17pp TruthfulQA MC1). ActLCD (EMNLP 2025) extends DoLa with RL-optimized layer selection (+19.81pp TruthfulQA). Both operate at the logit level but without calibration awareness.\n\n**Factuality probes (detection only)**: Han et al. (EMNLP 2025 Findings) show linear probes detect hallucinations in long-form generation comparably to multi-sample approaches. Balcells Obeso et al. (arXiv 2509.03531) train entity-level probes achieving AUC 0.87–0.90 across Llama-3.1-8B, Qwen-2.5-7B, Gemma-2-9B, and Mistral-Small-24B, with pretrained probes released.\n\n**Monitoring-based**: Monitoring Decoding (Chang et al., ACL 2025 Findings) monitors factuality during generation using a reference model's probability distribution, triggering tree-based resampling (+5.9 percentage points on TruthfulQA, from 38.2% to 44.1%, i.e., ~15.4% relative; with 5.7× latency); requires a larger reference model.\n\n**Logit-level methods**: Logit-Level Steering (Tao et al., arXiv 2601.10960) validates training-free logit intervention for controllable generation (+47% accuracy) but uses static corpus-level score tables without internal-state awareness.\n\n**Concurrent work (2026)**: CAG (arXiv 2605.01749) improves long-form factuality by up to 13% via exploration-commitment decoupling but requires multi-stage fine-tuning. CURE (arXiv 2604.12046) achieves +39.9% claim-level accuracy via reasoning calibration but requires training. CSS (arXiv 2604.17487) achieves training-free post-generation claim-level specificity backoff (0.913 overcommitment-aware utility on LongFact), but operates post-hoc and cannot intervene during streaming. CLC (arXiv 2502.19110) provides conformal guarantees but requires fine-tuning. Kalai-Vempala (PMC 2026) provides theoretical grounding that miscalibration causally drives hallucination rates. Beyond Precision (arXiv 2604.03141) shows LLMs achieve substantially better precision than recall.\n\n**Gap**: CHOKE/HACK validated that overconfident hallucinations are a substantial and consistent failure mode requiring targeted detection and intervention. However, no existing work combines: (a) a multiplicative calibration-aware trigger that dynamically combines two independent signals (verbal confidence via VUF × probe hallucination probability)—as distinct from CHOKE/HACK's single-probe detection—to target the specific verbal-internal mismatch; (b) logit-level intervention offering interpretability and composability advantages over hidden-state steering, with architectural future-proofing against ESR as models scale; (c) graded response from calibration-only hedging to factuality-improving rollback, with explicit separation of these contributions; (d) training-free during-generation operation validated on long-form generation across multiple model families—extending CHOKE/HACK's short-form QA scope to the streaming context where overconfident hallucinations are most harmful.",
  "approach": "We propose MisTAG (Miscalibration-Triggered Adaptive Generation), a training-free inference-time framework that monitors verbal-internal uncertainty mismatch during long-form generation and triggers logit-level interventions graded by mismatch severity. MisTAG extends the CHOKE/HACK line of work by introducing a multiplicative miscalibration detection signal and pairing it with interpretable logit-level intervention for long-form text. We make an explicit and honest dual-contribution claim: (1) **calibration correction** via hedging (reducing overconfident expression of uncertain content, measured by OHR, ECE, and CHOKE-Score—NOT claimed as factuality improvement), and (2) **factuality improvement** via rollback (preventing the most confidently-hallucinated content from being emitted, measured by FActScore). We evaluate on two model families: Llama-3.1-8B-Instruct (primary) and Qwen3-8B (co-primary).\n\n**Prerequisite Validation (Days 1–2)**: Before main experiments, for EACH target model: (a) Extract VUF direction following Ji et al.'s methodology (validated on Llama-3.1-8B and Qwen2.5-7B; Qwen3-8B requires fresh extraction); (b) Train linear factuality probes on hidden states (Balcells Obeso et al. release pretrained probes for Llama-3.1-8B); (c) Verify probe AUROC ≥0.85 on held-out LongFact generations; (d) Verify entity-concentration via span-level activation analysis. If AUROC <0.85, add explicit NER-based entity gating as fallback. This is a go/no-go gate.\n\n**Miscalibration Detection**: At each generated token, we compute a miscalibration score as the product of two independent signals: (1) verbal confidence, extracted via projection onto the VUF direction in the residual stream at the final layer, and (2) internal epistemic uncertainty, estimated via a lightweight linear factuality probe. The miscalibration score: M(t) = σ(VUF_confidence(t)) × probe_hallucination_prob(t). This multiplicative formulation is the key detection-level difference from CHOKE/HACK: CHOKE uses a single logistic regression probe trained on residual stream activations at layer 15 to detect knowledge-aware overconfidence; MisTAG dynamically combines two independent signals—one measuring how confidently the model *expresses* its output (VUF) and one measuring how likely the output is *factually wrong* (probe)—so that only the conjunction of high verbal confidence AND high hallucination probability triggers intervention. This targets the specific verbal-internal mismatch that CHOKE/HACK identifies as dangerous, but via a complementary detection mechanism that can capture cases where the model is confidently wrong without necessarily possessing knowledge of the correct answer (CHOKE by definition only covers knowledge-present hallucinations).\n\n**Logit-Level Intervention** (interpretable: the bias vector explicitly shows which tokens are promoted/suppressed; composable with other decoding strategies; architecturally future-proofed against ESR at scale—while ESR is <1% at 8B per McKenzie et al. 2026, it reaches 3.8–14.8% at 70B, making hidden-state intervention increasingly fragile as models scale; logit-level intervention bypasses the residual stream entirely):\n\n- *Mild mismatch (M(t) > τ_mild) → Context-Dependent Hedge (CALIBRATION correction only)*: Apply a logit bias vector b ∈ R^|V| at next-token prediction, **restricted to entity-bearing positions**: the bias is applied only when (a) the probe's hallucination probability exceeds τ_mild AND (b) the preceding token context indicates an entity-bearing position—specifically, when the previous 1–3 tokens contain a numeral, date pattern, capitalized proper noun, or named entity (detected via lightweight regex/spaCy heuristics on the decoded token buffer). This position-awareness prevents grammatical incoherence. The bias vector: b(v) = +1 for hedge tokens (~50 tokens: 'likely', 'approximately', 'reportedly', 'possibly', etc.), b(v) = −1 for assertive tokens (~30 tokens: 'definitely', 'certainly', 'clearly', etc.), b(v) = 0 otherwise. Log p'(v) = log p(v) + α·b(v). **We explicitly do NOT claim this improves FActScore**: hedging 'approximately 1067' still produces a verifiable atomic fact judged as unsupported. The hedge action's value is purely calibration—making verbal expression match internal uncertainty (reducing OHR, ECE, and CHOKE-Score).\n\n- *Severe mismatch (M(t) > τ_severe) → Rollback+Regenerate (FACTUALITY improvement)*: Rollback to last sentence boundary (discard tokens and KV-cache entries), then regenerate with: (i) constrained prefix forcing an epistemic marker, AND (ii) context-dependent hedge logit bias at 2× mild level, AND (iii) temperature reduction (T=0.3). **This IS claimed as factuality improvement**: by preventing the most confidently-hallucinated sentences from being emitted and regenerating under uncertainty-aware constraints, we hypothesize FActScore improves via forced uncertainty prefix (less specific claims) and temperature reduction (more conservative token selection). **Anti-cascading safeguards**: (1) 30-token cooldown after rollback (hedging remains active); (2) Maximum 3 rollbacks per generation; if exceeded, persistent mild-level hedging.\n\n**Core Novelty Experiment: Confusion-Matrix Analysis vs. PC-LDCD**: Grounded in CHOKE's finding that 16–43% of hallucinations are overconfident, we hypothesize that a non-trivial fraction of these produce on-manifold representations that density methods miss—because the model's confidently-wrong trajectory is geometrically similar to confidently-correct trajectories. For each hallucinated atomic fact (per FActScore), we record: (a) MisTAG's M(t) at entity-bearing tokens, (b) PC-LDCD's PCNet NLL at the same tokens. Four quadrants: (Q1) Both flag; (Q2) MisTAG-only: high M(t) but low NLL—overconfident on-manifold hallucinations; (Q3) PC-LDCD-only; (Q4) Neither. **Hypothesis**: Q2 is non-trivially populated (≥15%). **Fallback**: If Q2 < 15%, reframe as complementary coverage with unique calibration contribution (dual hedge+rollback) and note that the multiplicative miscalibration score captures non-knowledge-aware overconfidence that CHOKE's definition excludes. PC-LDCD's code is at anonymous.4open.science/r/PC-LDCD-63D5; if inaccessible (currently returns 403), confusion-matrix analysis becomes supplementary for the review period.\n\n**OHR Metric Validation Study**: 100 hallucinated atomic facts (50 per model), automated OHR detection + 2 human annotators. Target: κ ≥ 0.85 between automated/human, κ ≥ 0.80 inter-annotator. Additionally report ECE and CHOKE-Score (computed from the same evaluation data at no additional cost).\n\n**Threshold Optimization**: Stage 1: Logistic regression on validation M(t) scores. Stage 2: Grid search over α ∈ {0.5, 1.0, 1.5, 2.0, 2.5} with constraints: length_reduction < 15%, Δperplexity < 5%. Thresholds set independently per model.\n\n**Latency Benchmarking**: Per-token overhead and end-to-end throughput for baseline greedy, MisTAG detection-only, MisTAG+hedge, MisTAG+hedge+rollback. Expected: <5% overhead for detection (two dot products plus lightweight regex); rollback incurs sentence-regeneration cost.\n\n**Evaluation**: Co-primary on Llama-3.1-8B-Instruct and Qwen3-8B (FP16, A100 80GB).\n\n*Benchmarks (5 axes)*: (1) **TruthfulQA** (MC1, MC2, True+Info); (2) **FActScore biographies** (primary metric for rollback), evaluated via GPT-4o API with local Llama-3.1-70B validation on 50-biography subset; (3) **OHR** + **ECE** for calibration quality (primary metrics for hedge); (4) **CHOKE-Score** (computed per Simhi et al.'s methodology on TruthfulQA/NQ subset—measures mitigation effectiveness specifically on overconfident hallucinations, directly validating MisTAG's targeted contribution); (5) **MT-Bench** for dialogue quality preservation. We additionally report FActScore precision AND recall.\n\n*Baselines (8 primary, applied to BOTH models)*: (a) Greedy/nucleus decoding, (b) DoLa, (c) ActLCD, (d) Token-Guard (released code), (e) PC-LDCD (if code accessible; otherwise report from paper), (f) Detect-only probe (Balcells Obeso et al.) without intervention, (g) **CHOKE-tuned probe + abstention** (Simhi et al.—the most relevant detection baseline; we train the CHOKE-tuned probe following their methodology and compare detection precision/recall at the miscalibration-score level), (h) **HACK activation steering** (Simhi et al.—the most relevant intervention baseline; we implement steering on attention heads following their protocol, extended to long-form generation). *Secondary* (time-permitting): (i) Ji et al.'s VUF activation intervention, (j) Monitoring Decoding.\n\n*Ablation studies*: (i) Hedge-only vs. Rollback-only vs. full MisTAG, (ii) Miscalibration trigger (VUF × probe) vs. CHOKE-style single probe vs. VUF-only vs. probe-only (directly testing whether the multiplicative signal outperforms the single-probe approach), (iii) Position-aware vs. static hedge bias, (iv) Anti-cascading ablation, (v) Threshold sensitivity (±1 SD), (vi) Cross-model analysis comparing M(t) distributions across Llama-3.1-8B vs. Qwen3-8B.\n\n*Analysis*: (a) Confusion-matrix breakdown (Q1–Q4) vs. PC-LDCD (if code available; otherwise supplementary), (b) Per-component FActScore and OHR attribution, (c) **CHOKE-Score comparison**: MisTAG vs. CHOKE-tuned probe vs. Token-Guard vs. DoLa—demonstrating that MisTAG's calibration-aware trigger yields higher CHOKE-Score than calibration-unaware methods, (d) **Coverage analysis**: What fraction of CHOKE hallucinations does MisTAG catch that are NOT knowledge-present (i.e., outside CHOKE's definition but still overconfident)? This tests whether the multiplicative signal captures a broader class of overconfident hallucinations, (e) Hedge-FActScore interaction (verify hedging does NOT improve FActScore), (f) FActScore precision vs. recall, (g) Latency profiling, (h) Qualitative examples.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~135h A100 80GB (probe validation 2×5h=10h, probe training 2×3h=6h, VUF extraction 2×3h=6h, CHOKE-tuned probe training 2×2h=4h, HACK steering setup 4h, PCNet adaptation 3h if code available/15h if reimplementation, threshold optimization 2×8h=16h, main experiments 2 models × 5 benchmarks × 8 baselines ~70h, confusion-matrix analysis 6h, ablations ~20h, latency benchmarking 4h, OHR annotation study 2h compute)",
      "gpu_utilization": "~40–45% effective; GPU idles during annotation, analysis, and threshold iteration",
      "timeline": "7–8 weeks",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "$340 (135h × $2.50/h A100 spot)",
      "evaluation_api_cost": "$250–400 (FActScore via GPT-4o API: ~$150–200; MT-Bench LLM-judge: ~$50–80; OHR annotation compensation: ~$30–40)"
    },
    "human_in_loop": {
      "gpu_hours": "~165h A100 80GB (comprehensive threshold sweeps, PCNet adaptation, all baselines including CHOKE-tuned probe and HACK steering on both models, probe validation, OHR annotation coordination)",
      "gpu_utilization": "~55–65% effective",
      "timeline": "5–6 weeks",
      "team": "1 researcher, ~50min/day reviewing experiments + coordinating 2 annotators for OHR validation (1 day)",
      "claude_api_cost": "$80–160 (800–1600 turns)",
      "estimated_gpu_cost": "$415 (165h × $2.50/h A100)",
      "evaluation_api_cost": "$300–450 (FActScore via GPT-4o: ~$180; MT-Bench: ~$80; OHR annotation: ~$40; ablation FActScore: ~$100)",
      "risk_note": "PCNet code accessibility is key variable: if anonymous repo returns 403 (currently does), confusion-matrix analysis deferred to supplementary. Probe validation is go/no-go gate (Days 1–2). CHOKE-tuned probe and HACK steering reimplementation adds ~8h but is straightforward from published methodology."
    },
    "auto_research": {
      "gpu_hours": "~175h A100 80GB (full baseline sweep including Token-Guard, CHOKE-tuned probe, and HACK steering on both models, probe validation and training, threshold optimization, all ablations, confusion-matrix if PC-LDCD code available)",
      "gpu_utilization": ">85% effective; continuous pipelining across two models on single A100",
      "timeline": "12 days with 1× A100 80GB (additional day for CHOKE/HACK baseline implementation)",
      "team": "0 (initial setup: HuggingFace tokens, annotator recruitment for OHR validation)",
      "claude_api_cost": "$200–450 (2000–4500 turns for end-to-end implementation, evaluation, paper drafting)",
      "estimated_gpu_cost": "$440 (175h × $2.50/h A100 spot)",
      "evaluation_api_cost": "$400–600 (FActScore via GPT-4o for all conditions: ~$250; MT-Bench: ~$120; ablation FActScore: ~$130; OHR annotation: ~$40)",
      "speed_bottleneck": "PCNet code accessibility (anonymous.4open.science, currently 403); CHOKE-tuned probe training is straightforward (~2h per model). OHR human annotation coordination (1-day blocking task).",
      "day_by_day_plan": "Days 1–2: Prerequisite validation (VUF + probes for both models, go/no-go). Days 3–4: Threshold optimization + CHOKE-tuned probe training + HACK steering setup + PCNet adaptation (if code available) + Token-Guard setup. Days 5–8: Main experiments (2 models × 5 benchmarks × 8 baselines). Days 9–10: Ablations + confusion-matrix analysis (if PCNet ready). Day 11: OHR annotation + latency benchmarking + CHOKE-Score analysis. Day 12: Analysis + paper drafting.",
      "risk_note": "If PC-LDCD code inaccessible: confusion-matrix becomes supplementary, main submission benchmarks MisTAG vs. DoLa/ActLCD/Token-Guard/CHOKE-tuned-probe/HACK-steering. If Q2 < 15%: reframe as complementary coverage + unique calibration contribution + broader-than-CHOKE detection of overconfident hallucinations (not restricted to knowledge-present cases)."
    }
  },
  "target_venues": [
    "AAAI 2027 (expected deadline: ~August 2026; conference: February 2027, Montréal)",
    "ICLR 2027 (expected deadline: ~October 2026)",
    "ARR cycle for EMNLP 2026 or NAACL 2027 (ARR submission anytime; EMNLP 2026 commitment deadline: August 2, 2026—requires reviews complete by then)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer (Simhi, Itzhak, Barez, Stanovsky, Belinkov; EMNLP 2025 Findings, arXiv 2502.12964) — CHOKE phenomenon: 16–43% of hallucinations are overconfident despite knowledge; CHOKE-tuned probe on layer-15 activations; CHOKE-Score metric; evaluated on NQ, TriviaQA with Llama-3.1-8B, Mistral-7B, Gemma-2-9B/27B",
    "HACK: Hallucinations Along Certainty and Knowledge Axes (Simhi et al., arXiv 2510.24222, Oct 2025) — 2×2 Knowledge×Certainty framework; CM (Certainty Misalignment) quadrant; activation steering on 48 attention heads; CM-Score metric; HK+ improvement ~15–21%",
    "LLMs Know More Than They Show: Approximating Human-Like Responses Using Probes (Orgad, Toker, Gekhman, Reichart, Szpektor, Kotek, Belinkov; ICLR 2025, arXiv 2410.02707) — internal representations encode truthfulness; AUROC 0.83–0.95 on answer tokens; predecessor to CHOKE",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025, SAC Highlight) — validated VUF on Llama-3.1-8B, Mistral-7B, Qwen2.5-7B; Llama most responsive; 31.9% relative hallucination reduction",
    "Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding (Zhu et al., ICLR 2026, arXiv 2601.21969) — training-free token-level control via hidden-state self-checking with iterative pruning/regeneration; code: github.com/rhq945/Token-Guard",
    "FactCheckmate: Preemptively Detecting and Mitigating Hallucinations in LMs (Alnuhait et al., arXiv 2410.02899) — hidden-state classifier + pre-generation intervention; 34.4% factuality improvement; requires training",
    "Endogenous Resistance to Activation Steering in Language Models (McKenzie et al., arXiv 2602.06941, Feb 2026) — ESR: <1% at 8B, 3.8% baseline / 14.8% meta-prompted at 70B; 26 SAE latents identified as consistency-checking circuits",
    "Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation (Chang et al., ACL 2025 Findings) — +5.9pp TruthfulQA (38.2%→44.1%, ~15.4% relative); requires reference model; 5.7× latency",
    "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (Nielsen et al., arXiv 2605.05953, May 2026) — PCNet density-based detection; AUROC up to 99%; TruthfulQA True+Info up to 0.78; code: anonymous.4open.science/r/PC-LDCD-63D5 (currently 403)",
    "Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals (van Dijk, arXiv 2605.05025, May 2026, ACL SRW 2026) — KL divergence of attention heads; AUROC 0.89–0.91 on TruthfulQA; 66.5% of extreme divergence at named entities; detection only, no intervention",
    "Real-Time Detection of Hallucinated Entities in Long-Form Generation (Balcells Obeso et al., arXiv 2509.03531) — entity-level probes AUC 0.87–0.90; cross-model transfer within 0.02–0.04 AUC; pretrained probes released",
    "Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation (Han et al., EMNLP 2025 Findings)",
    "DoLa: Decoding by Contrasting Layers Improves Factuality (ICLR 2024)",
    "Active Layer-Contrastive Decoding Reduces Hallucination (ActLCD, EMNLP 2025)",
    "Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality (CAG, arXiv 2605.01749, May 2026)",
    "Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration (CURE, arXiv 2604.12046, April 2026)",
    "Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control (CSS, arXiv 2604.17487, April 2026)",
    "Conformal Linguistic Calibration: Trading-off between Factuality and Specificity (CLC, arXiv 2502.19110, Feb 2025)",
    "Steering Language Models Before They Speak: Logit-Level Interventions (Tao et al., arXiv 2601.10960, Jan 2026)",
    "Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, Jan 2026)",
    "Hallucination, monofacts, and miscalibration: An empirical investigation (PMC 2026)",
    "Beyond Precision: Importance-Aware Recall for Factuality Evaluation (Jafari et al., arXiv 2604.03141, April 2026)",
    "Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in LLMs (arXiv 2502.11028)",
    "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023)",
    "LoGU: Long-form Generation with Uncertainty Expressions (ACL 2025)"
  ],
  "description": "Overconfident hallucinations—where an LLM asserts falsehoods with high verbal confidence despite internal epistemic uncertainty—are the most user-deceptive failure mode, validated and quantified as the CHOKE phenomenon (16–43% of hallucinations, Simhi et al. 2025). While CHOKE and HACK established that single-probe detection on residual stream activations can identify these cases and that activation steering can partially mitigate them in short-form QA, no method extends this to long-form generation with calibration-aware logit-level intervention. We propose MisTAG, a training-free inference-time framework that computes a multiplicative miscalibration score at every token—verbal confidence via VUF projection × factuality probe hallucination probability—combining two independent signals rather than CHOKE's single probe, to detect overconfident hallucinations including cases outside CHOKE's knowledge-present definition. MisTAG then triggers logit-level interventions graded by severity. Logit-level intervention offers three advantages over hidden-state manipulation: (1) interpretability—the bias vector explicitly shows which tokens are promoted/suppressed; (2) composability with other decoding strategies; (3) architectural future-proofing against ESR, which is negligible at 8B (<1%) but reaches 3.8–14.8% at 70B scale. We make an honest dual-contribution claim: (1) a context-dependent hedge logit bias for mild miscalibration provides CALIBRATION correction (reducing OHR, ECE, and CHOKE-Score—NOT FActScore); (2) sentence-level rollback with constrained regeneration for severe cases provides FACTUALITY improvement (improving FActScore). The paper's core novelty evidence is a confusion-matrix analysis hypothesizing that ≥15% of hallucinated facts are 'on-manifold overconfident'—flagged by MisTAG but missed by density-based PC-LDCD—grounded in CHOKE's validation that overconfident hallucinations with normal-looking internal states are common. If this fraction is smaller, the paper reframes as complementary coverage with unique calibration contribution and broader detection scope than CHOKE. We evaluate co-primarily on Llama-3.1-8B-Instruct and Qwen3-8B, with CHOKE-tuned probe (Simhi et al.) and HACK activation steering as key baselines alongside Token-Guard, DoLa, and ActLCD. CHOKE-Score is adopted as a primary evaluation metric to directly validate MisTAG's targeted contribution on overconfident hallucinations.",
  "project_name": "mistag_gen_control",
  "source": "web_research"
}
```

**Summary of changes (major revision):**

1. **CHOKE/HACK integration**: Cited throughout as the foundational work validating overconfident hallucinations. Repositioned MisTAG's detection as extending (multiplicative VUF × probe, covering non-knowledge-present cases) rather than originating the idea. Added CHOKE-tuned probe and HACK steering as primary baselines. Added CHOKE-Score as a primary evaluation metric.

2. **ESR reframed**: No longer a primary differentiator. Now honestly positioned as: negligible at 8B (<1%), relevant at 70B (3.8–14.8%), providing "architectural future-proofing" alongside the more immediate advantages of interpretability and composability.

3. **Q2 hypothesis strengthened**: Grounded in CHOKE's published 16–43% finding — overconfident hallucinations are empirically common, motivating the hypothesis that they produce on-manifold representations density methods miss.

4. **Monitoring Decoding corrected**: Now reports +5.9pp absolute (38.2%→44.1%, ~15.4% relative) consistently.

5. **Attention Divergence Signals acknowledged**: Added van Dijk (arXiv 2605.05025) as concurrent detection-only work using attention KL divergence.

6. **New baselines**: CHOKE-tuned probe + abstention and HACK activation steering — the two most directly relevant competitors.

7. **Sharper differentiation**: MisTAG vs. CHOKE/HACK on four axes: detection signal (multiplicative vs. single probe), intervention type (logit-level vs. abstention/steering), scope (long-form vs. QA), and response granularity (graded hedge/rollback vs. binary).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52c4e79a-3aa9-46e3-904a-d8adc1966f36",
  "isSidechain": false,
  "requestId": "req_011Cb62Kcc1cGVp2sDLbiw17",
  "type": "assistant",
  "uuid": "f042f04f-4a4e-4279-87a7-b5dfc576f0af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdhJ4CwwJiP6hwvMDDF3Bn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 987,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 48425,
      "output_tokens": 10681,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 987,
          "output_tokens": 10681,
          "cache_read_input_tokens": 48425,
          "cache_creation_input_tokens": 1175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1175
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

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Miscalibration-Triggered Adaptive Generation via Logit-Level Intervent…",
  "leafUuid": "f042f04f-4a4e-4279-87a7-b5dfc576f0af",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise MisTAG: CHOKE integration, ESR reframing, and Q2 hypothesis grounding",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Miscalibration-Triggered Adaptive Generation via Logit-Level Intervent…",
  "leafUuid": "f042f04f-4a4e-4279-87a7-b5dfc576f0af",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise MisTAG: CHOKE integration, ESR reframing, and Q2 hypothesis grounding",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6"
}
```

---
