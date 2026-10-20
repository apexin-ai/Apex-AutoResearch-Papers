# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-15 (UTC).** ## Original idea { "tit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/chats/exported-trajectories/account-3/a802c1f0-a070-4179-b6b1-b61559232c83.jsonl`
- **Structured JSON:** [`f06824f5bbea7dcecb43.json`](../../sessions/f0/f06824f5bbea7dcecb43.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T14:24:52.429Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T14:24:52.429Z",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-15 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation\",\n  \"core_problem\": \"LLMs generate long-form outputs where hallucinated claims are expressed with the same high confidence as factual ones. Existing approaches either detect hallucinations at claim level without calibrating expressed confidence (Han et al., EMNLP 2025 — binary probes + neuron clamping), calibrate confidence only at response level for short-form QA (Ji et al., EMNLP 2025; Miao & Ungar, 2026; CORAL, 2026), use probe-guided steering without claim-level granularity or long-form scope (ITI, NeurIPS 2023; CLAS, 2026; ActCab/CoDec, EMNLP 2024), or require multi-stage training of the base model (CURE, April 2026; CAG, May 2026; LoVeC, May 2025). No existing method performs claim-level calibrated uncertainty expression in long-form generation without base model training. Furthermore, the accuracy-confidence orthogonality that enables clean steering (Miao & Ungar, 2026) has only been validated on 7–8B models for short-form QA — whether it holds at 70B scale in long-form generation is an open question with practical implications for the entire probe-guided steering paradigm.\",\n  \"opportunity\": \"Four recent results create a convergent opportunity: (1) Han et al. (EMNLP Findings 2025) showed lightweight linear probes on hidden states detect claim-level factuality in long-form generation, matching expensive multi-sample methods at up to 100× fewer FLOPs — but their neuron clamping intervention is binary (suppress/allow), not calibrated; (2) Miao & Ungar (March 2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features (cosine similarity < 0.04), meaning models internally know when they're wrong but fail to express this — and that adaptive CAA steering along these directions achieves major calibration improvement (ECE 14.9→3.7 on Llama-3.1-8B, 35.1→3.3 on Mistral-7B), but only for response-level QA on 7–8B models; (3) Kumaran et al. (March 2026) demonstrated that confidence representations are cached at answer-adjacent positions before verbalization, enabling real-time detection during generation; (4) CLAS (April 2026) demonstrated that probe-derived adaptive steering works on models up to Llama 3.1-70B across 11 benchmarks, providing evidence that the steering mechanism scales — though not specifically for confidence calibration. Combining these — reading claim-level accuracy signals via probes during long-form generation, then steering verbalized confidence to match — is unexplored and fills a specific gap. Critically, testing whether the accuracy-confidence orthogonality extends to 70B scale and long-form generation is itself a contribution that informs the feasibility of the entire probe-guided confidence steering paradigm.\",\n  \"landscape\": \"**Foundational probe→steer paradigm:** ITI (Li et al., NeurIPS 2023) introduced inference-time intervention: linear probes identify truthful directions in attention heads, and activations are shifted along these directions during generation. Foundational work, but targets truthfulness (content change) rather than calibrated confidence expression, and only on TruthfulQA.\\n\\n**Closest prior work — claim-level probing in long-form generation:** Han et al. (EMNLP Findings 2025) trained simple linear probes on LLM hidden states that detect claim-level hallucinations in long-form generation with performance matching expensive multi-sample methods (up to 100× fewer FLOPs), testing on models up to Llama 3.1-405B. Their neuron clamping causally reduces hallucinations by fixing activations of factuality-correlated neurons — but this is a binary intervention (suppress or allow) that does not produce calibrated verbal uncertainty expression. Obeso et al. (arXiv 2509.03531, 2025) trains entity-level probes for real-time streaming hallucination detection in long-form generation (AUC 0.90 on Llama-3.3-70B) — detection only, no calibrated steering.\\n\\n**Closest prior work — calibrated confidence steering:** Miao & Ungar (arXiv 2603.25052, March 2026) discovered that calibration accuracy and verbalized confidence are orthogonal linear features (cosine similarity < 0.04), and proposed two-stage adaptive CAA steering that reads internal accuracy and steers verbalized output to match, achieving ECE improvements from 14.9→3.7 (Llama-3.1-8B) and 35.1→3.3 (Mistral-7B) — but only for response-level short-form QA on 7–8B models. They explicitly acknowledge: 'Whether the linear encoding findings hold at larger scales remains open. Evaluation is restricted to question-answering tasks; extending to open-ended generation would require rethinking how the probe target is constructed.' Ji et al. (EMNLP 2025) discovered the Verbal Uncertainty Feature (VUF) and proposed MUC with ~30% reduction in confident hallucinations — also response-level, short-form, on ≤8B models.\\n\\n**Same-group prior work — CORAL:** CORAL (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) uses regularized MLP probes on residual activations to predict correctness and steers at inference time, achieving 10% accuracy and 50% ECE improvements. However, CORAL targets MCQA on 7B models with response-level steering — no claim-level decomposition or long-form generation. RaS differs in (a) claim-level granularity via factuality probes, (b) long-form generation scope, and (c) confidence expression calibration rather than answer correctness steering.\\n\\n**Activation calibration + guided decoding:** ActCab/CoDec (EMNLP 2024) trains a linear layer on LM last-layer activations for confidence calibration, then uses confidence-guided decoding to elicit truthful answers. Same conceptual pipeline (activation-based calibration → guided generation) but operates at response level on QA, and modifies decoding probabilities rather than verbalized confidence expression.\\n\\n**Adaptive steering strength:** CLAS (Hsu et al., arXiv 2604.24693, April 2026) introduces context-dependent linear activation steering where steering strength adapts via learned sensing vectors: α_ℓ,t = (c_ℓ · [h_ℓ,t, 1]). Tested on Llama-3.1-70B across 11 benchmarks, demonstrating that probe-derived adaptive steering scales to 70B. RaS's α = β × max(0, threshold − probe_score) adapts similarly but is driven by factuality probe scores per-claim rather than a general context sensing vector, and targets confidence calibration specifically.\\n\\n**Mechanistic understanding:** 'How do LLMs Compute Verbal Confidence?' (Kumaran et al., arXiv 2603.17839, March 2026) provides convergent evidence that confidence representations emerge at answer-adjacent positions via cached retrieval, supporting the feasibility of online detection during generation.\\n\\n**Training-free steering baselines:** SteerConf (NeurIPS 2025) does prompt-based training-free confidence steering via multi-prompt aggregation. ACT (WWW 2025) applies tuning-free diverse steering vectors with adaptive intensity for truthfulness, scaling to 65B.\\n\\n**Claim-level long-form calibration (training-based):** CURE (arXiv 2604.12046, April 2026) uses multi-stage training to teach claim-level confidence reasoning, improving accuracy by up to 39.9%. CAG (arXiv 2605.01749, May 2026) achieves up to 13% factuality gain via training-based calibration-aware generation. LoVeC (arXiv 2505.23912, May 2025) uses RL to train LLMs to append on-the-fly confidence scores per statement in long-form generation, achieving 20× speedup over self-consistency methods. All three require base model fine-tuning or RL.\\n\\n**Post-generation claim-level approaches:** CSS (arXiv 2604.17487, April 2026) decomposes answers into claims and backs off uncertain ones using external verifiers. Selective Abstraction (arXiv 2602.11908, February 2026) replaces low-confidence atoms with confident abstractions.\\n\\n**Residual-stream anomaly detection:** PCNET (arXiv 2605.05953, May 2026) uses probabilistic circuits on residual streams for hallucination detection + contrastive decoding, reaching up to 99% AUROC — but targets short-form QA and changes content (different token selection) rather than expressing calibrated uncertainty.\\n\\n**Scaling concerns for activation steering:** Scaling laws for activation steering (ICML 2025) show that CAA effectiveness diminishes with model size on Llama 2 (7B→13B→70B) for behavioral steering (refusal). Endogenous steering resistance (arXiv 2602.06941, February 2026) shows Llama-3.3-70B has 3.8% ESR rate (vs <1% for smaller models). However, CLAS demonstrates successful probe-derived steering on Llama-3.1-70B, suggesting that adaptive, probe-guided steering may be more robust at scale than uniform CAA.\\n\\n**Gap:** No existing work combines claim-level factuality probing (à la Han et al.) with calibrated activation steering along the verbalized-confidence direction (à la Miao & Ungar) in a single-pass, online framework for long-form generation. This intersection — reading internal accuracy per-claim and steering verbalized confidence to match during generation — is the contribution space. Additionally, no work has tested whether the accuracy-confidence orthogonality discovered at 7–8B scale holds at 70B or in long-form generation contexts, making this verification itself a contribution to the mechanistic understanding of confidence representations.\",\n  \"approach\": \"We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. The system reads internal accuracy signals per-claim via lightweight probes and steers verbalized confidence to match via targeted activation intervention, producing naturally hedged language for uncertain claims while leaving confident-and-correct claims untouched.\\n\\n**Pilot Experiment — Orthogonality Verification at Scale (~8h, 2× H100, first week):** Before committing the full experimental budget, we replicate Miao & Ungar's orthogonality analysis on Llama 3.1-70B in a long-form generation setting. We extract accuracy and confidence directions from biography-generation hidden states (not QA), measure their cosine similarity, and compare against the < 0.04 value found at 7–8B scale. This pilot has three outcomes: (a) orthogonality holds (cosine < 0.1) — proceed as planned, report the scaling result as a contribution; (b) orthogonality partially holds (cosine 0.1–0.3) — adapt steering to project out the accuracy component from the confidence direction before steering, proceed with modified approach; (c) orthogonality fails (cosine > 0.3) — report as an important negative finding about the limits of linear feature geometry at scale, fall back to the 8B-only configuration. All three outcomes produce publishable results.\\n\\n**Offline Stage 1 — Factuality Probe Training (~12h wall, 2× H100 for 70B; ~4h, 1× H100 for 8B; one-time per model):** Generate long-form outputs (biographies, factual descriptions) from the target model, decompose into atomic claims using FActScore/OpenFActScore decomposition, verify claim factuality against knowledge sources. Extract hidden states at each claim's token span across multiple layers (following Han et al.'s layer-group methodology). Train lightweight linear probes (logistic regression on span-aggregated hidden states) to predict continuous factuality confidence scores. Unlike Han et al.'s binary factuality labels, we train on soft labels derived from verification confidence, enabling graded uncertainty estimation.\\n\\n**Offline Stage 2 — Verbalized-Confidence Direction Extraction (~5h wall, 2× H100 for 70B; ~2h, 1× H100 for 8B; one-time per model):** Extract a verbalized-confidence steering direction via contrastive activation pairs: generate matched claim pairs where the same factual content is expressed with high confidence ('X was born in Y') vs. hedged uncertainty ('X was reportedly born in Y, though I am not certain'). The mean activation difference yields the steering direction, following the contrastive methodology from Ji et al. (VUF) and Miao & Ungar (CAA). For the 70B model, if the pilot reveals partial orthogonality degradation, we apply Gram-Schmidt orthogonalization to project the confidence direction away from the accuracy direction before use.\\n\\n**Online Stage — Probe-Guided Steering During Generation:** During autoregressive generation: (1) At each generated token, run the factuality probe on its hidden states — this is a single matrix-vector multiplication with negligible overhead. (2) Maintain a running mean probe score over the current sentence span using a sliding window. (3) At sentence boundaries (detected from generated punctuation — periods, newlines — which are trivially available during generation), evaluate the accumulated probe score against a calibrated threshold. (4) If the probe indicates internal uncertainty (score below threshold) while the generation shows no hedging markers, apply a steering offset along the extracted verbalized-confidence direction on subsequent tokens, with steering magnitude α proportional to the miscalibration gap: α = β × max(0, threshold − probe_score), where β is calibrated on a held-out validation set. This adaptive formula is conceptually related to CLAS's context-dependent steering, but driven by per-claim factuality probe scores rather than general input-context sensing vectors. (5) Deactivate steering when the probe score recovers above threshold.\\n\\n**Key design choices addressing known limitations:** (a) Span-aggregated probe scores over the full claim token range avoid the single-token prefix-contamination problem — the signal reflects the entire claim, not just the cumulative prefix. (b) Single-pass online monitoring eliminates the two-pass chicken-and-egg problem identified for the original CL-MUC approach — no position-aligned regeneration needed. (c) Continuous calibrated steering (not binary neuron clamping) produces graded hedging proportional to internal uncertainty, distinguishing this from Han et al.'s binary intervention. (d) Operating on the verbalized-confidence direction (orthogonal to accuracy per Miao & Ungar, verified at 70B scale in our pilot) means steering affects expression style without corrupting the model's factual knowledge. (e) Adaptive steering magnitude based on probe-detected need may mitigate the diminishing effectiveness of uniform CAA at larger scales (ICML 2025 scaling laws), since steering is only applied where needed and at probe-calibrated intensity.\\n\\n**Models:** Llama 3.1-70B-Instruct as primary (standard dense transformer architecture, well-studied for probing and steering, large enough to test scaling of the orthogonality finding, with CLAS confirming probe-derived steering viability at this scale). Llama 3.1-8B-Instruct as validation (enables direct comparison with Miao & Ungar and Ji et al. baselines on the same model family, validates the pipeline in well-charted territory before scaling). Both models use standard transformer attention across all layers, avoiding the untested territory of hybrid DeltaNet architectures (e.g., Qwen 3.5) where linear probe and steering techniques lack validation.\\n\\n**Benchmarks:** FActScore (biography generation, primary) and LongFact (diverse long-form factuality). Metrics: claim-level ECE, Brier score (calibration quality), AUROC (uncertainty detection), FActScore/factual precision (to verify steering does not degrade content quality), and MT-Bench fluency subset (to verify generation quality preservation). We also report the cosine similarity between accuracy and confidence directions at 70B scale as a standalone mechanistic finding.\\n\\n**Quantitative targets:** We expect RaS to achieve: (1) claim-level ECE reduction of ≥40% relative to unsteered baselines on both FActScore and LongFact; (2) FActScore preservation within 2% of unsteered baseline (steering affects verbal expression, not factual content); (3) uncertainty detection AUROC ≥0.80 (probe-based); (4) superior calibration (lower ECE) compared to Han et al.'s binary neuron clamping at comparable or better FActScore. These targets are informed by Miao & Ungar's response-level results (ECE reductions of 70–90% on QA), discounted for the harder claim-level long-form setting.\\n\\n**Comparisons:** (1) Unsteered baseline, (2) Han et al.'s probes + neuron clamping (closest representation-based method for long-form), (3) CURE (closest training-based method, if reproducible), (4) LoVeC (RL-based long-form verbalized confidence, if reproducible), (5) Ablations: probe-only detection without steering, uniform steering without probe guidance, VUF-only steering (Ji et al.'s original method applied per-claim), CORAL-style MLP probes vs. linear probes, varying layers for probe extraction, steering strength sensitivity, CLAS-style sensing vector vs. probe-score-driven adaptation.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~250h H100 80GB (orthogonality pilot ~8h [2×H100], probe training + direction extraction ~34h [20h 70B on 2×H100, 6h 8B], Llama 3.1-70B generation + evaluation on FActScore + LongFact ~100h [2×H100], Llama 3.1-8B validation ~25h, baseline comparisons ~45h, ablations ~38h)\",\n      \"gpu_utilization\": \"~20-30% effective — GPU idles during code development, pipeline debugging, and results analysis\",\n      \"timeline\": \"5-7 weeks (1 researcher full-time)\",\n      \"team\": \"1-2 researchers with mechanistic interpretability and activation steering experience\",\n      \"estimated_gpu_cost\": \"$625-875 (at ~$2.50-3.50/hr H100 80GB spot)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~200h H100 80GB (agent handles pipeline code, probe training iteration, evaluation scripting; human approves pilot results, probe design, steering threshold calibration, and ablation priorities)\",\n      \"gpu_utilization\": \"~45-60% — agent queues experiments between human check-ins\",\n      \"timeline\": \"3-4 weeks\",\n      \"team\": \"1 researcher, ~30min/day for methodology decisions, pilot outcome assessment, and qualitative hedging evaluation\",\n      \"claude_api_cost\": \"$100-200 (~1500-3000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$500-700\",\n      \"risk_note\": \"Primary risk: whether accuracy-confidence orthogonality holds at 70B scale in long-form generation — the ~8h pilot experiment validates this before committing the full budget. If orthogonality breaks (outcome c), we fall back to an 8B-only paper with the negative scaling result as a contribution, reducing total compute to ~80h H100. Secondary risk: whether probe-guided steering produces natural hedging at 70B or degrades fluency — qualitative human assessment is essential. Tertiary risk: CAA effectiveness diminishing at 70B scale (per ICML 2025 scaling laws), though our adaptive probe-guided approach may be more robust than uniform steering.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~280h H100 80GB (agent explores probe architectures, layer selections, steering schedules across both models, plus comprehensive evaluation)\",\n      \"gpu_utilization\": \"~80-90% — continuous experiment pipeline with minimal idle\",\n      \"timeline\": \"7-10 days with 2× H100 80GB\",\n      \"team\": \"0 researchers (initial setup + final review only)\",\n      \"claude_api_cost\": \"$200-400 (~3000-6000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$700-980\",\n      \"speed_bottleneck\": \"Long-form generation throughput on Llama 3.1-70B with 2× H100 tensor parallelism (~20-30 tok/s) — generating and evaluating hundreds of long-form responses per configuration is the computational bottleneck\",\n      \"risk_note\": \"Without human judgment, agent may over-optimize probe thresholds on validation set rather than ensuring robustness, may miss qualitative assessment of hedging naturalness, and critically may not correctly interpret the orthogonality pilot results (the decision to proceed vs. pivot requires understanding of the mechanistic implications)\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — ~10 weeks; conference Feb 16-23, Montréal) — PRIMARY\",\n    \"ARR August 2026 (submission Aug 3, 2026 — ~11 weeks; committable to EMNLP 2026 Oct 24-29 or later *ACL venues)\",\n    \"ICLR 2027 (expected submission ~Oct 2026, ~20 weeks; comfortable timeline)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation (Han et al., Findings of EMNLP 2025) — closest prior work: claim-level probes + neuron clamping in long-form generation\",\n    \"Closing the Confidence-Faithfulness Gap in LLMs (Miao & Ungar, arXiv 2603.25052, March 2026) — accuracy-confidence orthogonality discovery + adaptive CAA steering; explicitly notes scaling and long-form extension as open questions\",\n    \"Correctness-Optimized Residual Activation Lens [CORAL] (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) — same group; MLP probes → correctness steering on MCQA at 7B scale; must differentiate as response-level, short-form only\",\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025) — VUF discovery and MUC for response-level short-form QA\",\n    \"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model [ITI] (Li et al., NeurIPS 2023) — foundational probe→steer paradigm using linear probes on attention heads for truthfulness\",\n    \"Enhancing Language Model Factuality via Activation-Based Confidence Calibration and Guided Decoding [ActCab/CoDec] (EMNLP 2024) — activation calibration + confidence-guided decoding for QA factuality\",\n    \"Contextual Linear Activation Steering [CLAS] (Hsu et al., arXiv 2604.24693, April 2026) — probe-derived adaptive steering with context-dependent strength; tested on Llama-3.1-70B, confirming steering viability at 70B scale\",\n    \"How do LLMs Compute Verbal Confidence? (Kumaran et al., arXiv 2603.17839, March 2026) — mechanistic evidence for cached confidence retrieval at answer-adjacent positions\",\n    \"Reinforcement Learning for Better Verbalized Confidence in Long-Form Generation [LoVeC] (arXiv 2505.23912, May 2025) — RL-based on-the-fly confidence scoring per statement in long-form generation; training-based\",\n    \"Scaling Laws for Activation Steering with Llama 2 Models and Refusal Mechanisms (ICML 2025) — demonstrates CAA effectiveness diminishes with model size (7B→70B); informs our adaptive steering design\",\n    \"Endogenous Resistance to Activation Steering in Language Models (arXiv 2602.06941, February 2026) — Llama-3.3-70B shows 3.8% endogenous steering resistance; relevant scaling concern\",\n    \"Does Transformer Interpretability Transfer to RNNs? (2024) — probing and CAA partially transfer to recurrent architectures with reduced effectiveness; motivates our choice of standard transformer models\",\n    \"SteerConf: Steering LLMs for Confidence Elicitation (Zhou et al., NeurIPS 2025) — prompt-based training-free confidence calibration\",\n    \"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025) — diverse steering vectors with adaptive intensity control\",\n    \"Real-Time Detection of Hallucinated Entities in Long-Form Generation (Obeso et al., arXiv 2509.03531, 2025) — entity-level streaming probes for long-form generation\",\n    \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits [PCNET] (arXiv 2605.05953, May 2026) — residual stream anomaly detection + contrastive decoding intervention\",\n    \"Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, January 2026) — online hallucination detection as evolving latent state\",\n    \"Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration [CURE] (arXiv 2604.12046, April 2026) — multi-stage training for claim-level confidence reasoning\",\n    \"Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality [CAG] (arXiv 2605.01749, May 2026) — training-based calibration-aware generation\",\n    \"Atomic Calibration of LLMs in Long-Form Generations (Findings of AACL-IJCNLP 2025) — showed poor claim-level calibration in long-form outputs\",\n    \"Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control [CSS] (arXiv 2604.17487, April 2026) — post-generation specificity control via external verifiers\",\n    \"When Should LLMs Be Less Specific? Selective Abstraction for Reliable Long-Form Text Generation (arXiv 2602.11908, February 2026)\",\n    \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs (ICML 2024) — linear probes approximate semantic entropy at response level\",\n    \"FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023)\",\n    \"Long-form Factuality in Large Language Models [LongFact/SAFE] (NeurIPS 2024)\",\n    \"Steering Language Models With Activation Engineering (Turner et al., arXiv 2308.10248, 2023)\"\n  ],\n  \"description\": \"We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. Motivated by two key findings — Han et al. (EMNLP 2025) showed lightweight probes detect claim-level factuality in long-form hidden states, and Miao & Ungar (2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features — RaS combines both insights in a novel way: it reads claim-level accuracy signals via factuality probes during autoregressive generation and steers verbalized confidence to match via targeted activation intervention along the orthogonal confidence direction, all within a single forward pass. Unlike Han et al.'s neuron clamping (binary suppression of hallucinations), RaS produces calibrated verbal hedging proportional to the model's internal uncertainty. Unlike CURE, CAG, and LoVeC, it requires no base model training — only lightweight linear probe fitting and contrastive direction extraction. The probe-guided adaptive steering formula (α = β × max(0, threshold − probe_score)) relates to CLAS's context-dependent steering but is driven by per-claim factuality signals rather than general context sensing, and targets confidence expression rather than content correctness (as in ITI, CORAL, and ActCab/CoDec). The framework includes a dedicated pilot experiment verifying the accuracy-confidence orthogonality at 70B scale in long-form generation — extending Miao & Ungar's finding beyond the 7–8B QA setting where it was established. We evaluate on Llama 3.1-70B (primary, testing scaling) and Llama 3.1-8B (validation, direct comparison with prior work) using FActScore and LongFact, measuring claim-level ECE, Brier score, AUROC, and factual precision. We expect ≥40% claim-level ECE reduction over unsteered baselines while preserving FActScore within 2%. Both models use standard transformer architectures, avoiding the untested hybrid DeltaNet territory (e.g., Qwen 3.5) where linear probing and activation steering techniques lack validation. All experiments fit within ~250 H100-hours.\",\n  \"project_name\": \"probe_guided_claim_calibration\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 3)\nIssues: [\"COMPUTE EXCEEDS CONSTRAINT: Manual mode estimates ~250h H100-hours, auto mode ~280h, and even HIL mode is at the exact 200h limit. The user's hard constraint is ≤200 H100-hours total. The breakdown shows ~38h for ablations and ~45h for baselines — both need trimming, and dropping the 8B validation track (~25h) or reducing 70B evaluation scope would help.\", \"MISSING COMPETITOR — 'A Single Direction of Truth' (O'Neill et al., arXiv 2507.23221, July 2025): Uses a linear probe on an observer model's residual stream to detect hallucinations (outperforming baselines by 5–27 points on Gemma-2 2B–27B), then uses the probe direction as a steering vector to causally reduce hallucination rates. While it uses an external observer model (vs. RaS's self-probing) and targets binary hallucination (vs. calibrated confidence), the probe→steer pipeline is very close. Must be cited with clear differentiation: RaS self-probes claim-level factuality for graded confidence calibration; O'Neill et al. use an observer model for binary hallucination detection/reduction.\", \"MISSING COMPETITOR — CARE (Yuan et al., SIGIR 2025): Fact-level calibration and correction framework for long-form generation using confidence-aware fact correction where high-confidence facts iteratively refine low-confidence ones. Directly addresses the same problem (fact-level calibration in long-form) with a different mechanism (iterative correction vs. activation steering). Must be cited.\", \"SENTENCE-BOUNDARY STEERING LATENCY: The approach evaluates accumulated probe scores 'at sentence boundaries' and applies steering to 'subsequent tokens.' This means an uncertain claim within Sentence N is generated with confident language, and hedging only appears in Sentence N+1 onward. The output reads as 'Barack Obama was born in Kenya. However, I am not fully certain about the above.' — the hallucinated claim itself remains confidently expressed. This is a fundamental design limitation that either (a) should be acknowledged as a known tradeoff, (b) mitigated with sub-sentence evaluation triggers (e.g., every K tokens or at clause boundaries), or (c) reframed as 'forward-looking uncertainty conditioning' rather than 'per-claim calibrated hedging.'\", \"QUANTITATIVE TARGETS MAY BE OVEROPTIMISTIC: The ≥40% claim-level ECE reduction target is derived by 'discounting' Miao & Ungar's response-level QA results (70–90% ECE reduction). But claim-level ECE in long-form generation faces additional challenges: noisy claim boundary detection, probe signal dilution from long-context hidden states, and the sentence-boundary steering latency. A more conservative target (e.g., ≥25% ECE reduction) would be more defensible.\", \"MISSING ADVANCED STEERING BASELINES: The proposal compares against static VUF steering but not against recent adaptive steering methods that could serve as stronger baselines: Spherical Steering (You et al., Feb 2026 — rotation-based with confidence gating), CAST (IBM, ICLR 2025 — conditional activation steering), and FLAS (Jin et al., May 2026 — flow-based activation steering). At minimum, CAST's conditional steering paradigm (apply steering only when a condition is met) is conceptually close to probe-triggered steering and should be discussed.\"]\nFeedback: The proposal has improved substantially since Round 1 — replacing Qwen3.5, fixing the two-pass problem, citing CORAL/CLAS/ITI/ActCab, and adding the orthogonality pilot are all strong revisions. The core gap remains real. Here are the remaining fixes:\n\n**1. Reduce compute to ≤200 H100-hours (REQUIRED):**\nThe most straightforward path: drop the 8B validation track (~25h saved), reduce ablations from 5 to 3 (~15h saved), and tighten baseline comparisons to the 2 most relevant (Han et al. neuron clamping + CURE) (~15h saved). This brings the total to ~195h. Alternatively, reduce the 70B evaluation corpus size by 30% and keep the 8B track as a lighter sanity check (~10h instead of 25h).\n\n**2. Cite 'A Single Direction of Truth' and CARE:**\nO'Neill et al. (2025) is the closest probe→steer work for hallucinations. Differentiate on three axes: (a) self-probing vs. external observer, (b) calibrated confidence vs. binary hallucination, (c) claim-level granularity in long-form vs. span-level in short contexts. CARE (SIGIR 2025) should be cited as a parallel approach to fact-level calibration that uses iterative correction rather than activation steering.\n\n**3. Address the steering latency problem (CRITICAL for technical credibility):**\nThree options, in order of preference:\n(a) **Best: Sub-sentence triggers.** Evaluate probe scores every K tokens (e.g., K=8) with a running exponential average, and trigger steering mid-sentence when the score drops below threshold. This hedges the CURRENT claim by steering later tokens in the same sentence (e.g., steering mid-generation produces 'Obama was born in — well, I believe it may have been — Kenya, though I'm not fully certain'). The cost is slightly more frequent threshold checks, which is negligible.\n(b) **Acceptable: Acknowledge and empirically measure the latency.** Report what fraction of uncertain claims get hedged within the same sentence vs. in subsequent sentences. If the probe signal rises early in claims (as Kumaran et al.'s cached-retrieval finding suggests), mid-claim steering may be feasible even with sentence-boundary triggers.\n(c) **Minimum: Reframe as 'forward-looking uncertainty conditioning.'** Acknowledge that RaS conditions subsequent generation on detected uncertainty, producing uncertainty-aware continuation rather than per-claim hedging.\n\n**4. Temper quantitative targets:**\nSet the primary ECE reduction target at ≥25% (vs. ≥40%), noting that Miao & Ungar's 70–90% reductions were on response-level QA with 7–8B models, and claim-level long-form calibration at 70B is substantially harder. Keep ≥40% as a stretch goal. This protects the paper from appearing to underperform its own targets.\n\n**5. Discuss CAST (ICLR 2025) as conceptual relative:**\nCAST's conditional activation steering (apply steering only when activation patterns match a condition) is conceptually close to probe-triggered steering. One sentence in the landscape distinguishing RaS's data-driven probe threshold from CAST's learned condition vector is sufficient.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\")."
}
```

---

### Runtime record

_source line 2 · 2026-05-15T14:24:52.434Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T14:24:52.434Z",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

## Round 1

79 recorded events

### User

_source line 3 · 2026-05-15T14:24:52.479Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-15 (UTC).**

## Original idea
{
  "title": "Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation",
  "core_problem": "LLMs generate long-form outputs where hallucinated claims are expressed with the same high confidence as factual ones. Existing approaches either detect hallucinations at claim level without calibrating expressed confidence (Han et al., EMNLP 2025 — binary probes + neuron clamping), calibrate confidence only at response level for short-form QA (Ji et al., EMNLP 2025; Miao & Ungar, 2026; CORAL, 2026), use probe-guided steering without claim-level granularity or long-form scope (ITI, NeurIPS 2023; CLAS, 2026; ActCab/CoDec, EMNLP 2024), or require multi-stage training of the base model (CURE, April 2026; CAG, May 2026; LoVeC, May 2025). No existing method performs claim-level calibrated uncertainty expression in long-form generation without base model training. Furthermore, the accuracy-confidence orthogonality that enables clean steering (Miao & Ungar, 2026) has only been validated on 7–8B models for short-form QA — whether it holds at 70B scale in long-form generation is an open question with practical implications for the entire probe-guided steering paradigm.",
  "opportunity": "Four recent results create a convergent opportunity: (1) Han et al. (EMNLP Findings 2025) showed lightweight linear probes on hidden states detect claim-level factuality in long-form generation, matching expensive multi-sample methods at up to 100× fewer FLOPs — but their neuron clamping intervention is binary (suppress/allow), not calibrated; (2) Miao & Ungar (March 2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features (cosine similarity < 0.04), meaning models internally know when they're wrong but fail to express this — and that adaptive CAA steering along these directions achieves major calibration improvement (ECE 14.9→3.7 on Llama-3.1-8B, 35.1→3.3 on Mistral-7B), but only for response-level QA on 7–8B models; (3) Kumaran et al. (March 2026) demonstrated that confidence representations are cached at answer-adjacent positions before verbalization, enabling real-time detection during generation; (4) CLAS (April 2026) demonstrated that probe-derived adaptive steering works on models up to Llama 3.1-70B across 11 benchmarks, providing evidence that the steering mechanism scales — though not specifically for confidence calibration. Combining these — reading claim-level accuracy signals via probes during long-form generation, then steering verbalized confidence to match — is unexplored and fills a specific gap. Critically, testing whether the accuracy-confidence orthogonality extends to 70B scale and long-form generation is itself a contribution that informs the feasibility of the entire probe-guided confidence steering paradigm.",
  "landscape": "**Foundational probe→steer paradigm:** ITI (Li et al., NeurIPS 2023) introduced inference-time intervention: linear probes identify truthful directions in attention heads, and activations are shifted along these directions during generation. Foundational work, but targets truthfulness (content change) rather than calibrated confidence expression, and only on TruthfulQA.\n\n**Closest prior work — claim-level probing in long-form generation:** Han et al. (EMNLP Findings 2025) trained simple linear probes on LLM hidden states that detect claim-level hallucinations in long-form generation with performance matching expensive multi-sample methods (up to 100× fewer FLOPs), testing on models up to Llama 3.1-405B. Their neuron clamping causally reduces hallucinations by fixing activations of factuality-correlated neurons — but this is a binary intervention (suppress or allow) that does not produce calibrated verbal uncertainty expression. Obeso et al. (arXiv 2509.03531, 2025) trains entity-level probes for real-time streaming hallucination detection in long-form generation (AUC 0.90 on Llama-3.3-70B) — detection only, no calibrated steering.\n\n**Closest prior work — calibrated confidence steering:** Miao & Ungar (arXiv 2603.25052, March 2026) discovered that calibration accuracy and verbalized confidence are orthogonal linear features (cosine similarity < 0.04), and proposed two-stage adaptive CAA steering that reads internal accuracy and steers verbalized output to match, achieving ECE improvements from 14.9→3.7 (Llama-3.1-8B) and 35.1→3.3 (Mistral-7B) — but only for response-level short-form QA on 7–8B models. They explicitly acknowledge: 'Whether the linear encoding findings hold at larger scales remains open. Evaluation is restricted to question-answering tasks; extending to open-ended generation would require rethinking how the probe target is constructed.' Ji et al. (EMNLP 2025) discovered the Verbal Uncertainty Feature (VUF) and proposed MUC with ~30% reduction in confident hallucinations — also response-level, short-form, on ≤8B models.\n\n**Same-group prior work — CORAL:** CORAL (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) uses regularized MLP probes on residual activations to predict correctness and steers at inference time, achieving 10% accuracy and 50% ECE improvements. However, CORAL targets MCQA on 7B models with response-level steering — no claim-level decomposition or long-form generation. RaS differs in (a) claim-level granularity via factuality probes, (b) long-form generation scope, and (c) confidence expression calibration rather than answer correctness steering.\n\n**Activation calibration + guided decoding:** ActCab/CoDec (EMNLP 2024) trains a linear layer on LM last-layer activations for confidence calibration, then uses confidence-guided decoding to elicit truthful answers. Same conceptual pipeline (activation-based calibration → guided generation) but operates at response level on QA, and modifies decoding probabilities rather than verbalized confidence expression.\n\n**Adaptive steering strength:** CLAS (Hsu et al., arXiv 2604.24693, April 2026) introduces context-dependent linear activation steering where steering strength adapts via learned sensing vectors: α_ℓ,t = (c_ℓ · [h_ℓ,t, 1]). Tested on Llama-3.1-70B across 11 benchmarks, demonstrating that probe-derived adaptive steering scales to 70B. RaS's α = β × max(0, threshold − probe_score) adapts similarly but is driven by factuality probe scores per-claim rather than a general context sensing vector, and targets confidence calibration specifically.\n\n**Mechanistic understanding:** 'How do LLMs Compute Verbal Confidence?' (Kumaran et al., arXiv 2603.17839, March 2026) provides convergent evidence that confidence representations emerge at answer-adjacent positions via cached retrieval, supporting the feasibility of online detection during generation.\n\n**Training-free steering baselines:** SteerConf (NeurIPS 2025) does prompt-based training-free confidence steering via multi-prompt aggregation. ACT (WWW 2025) applies tuning-free diverse steering vectors with adaptive intensity for truthfulness, scaling to 65B.\n\n**Claim-level long-form calibration (training-based):** CURE (arXiv 2604.12046, April 2026) uses multi-stage training to teach claim-level confidence reasoning, improving accuracy by up to 39.9%. CAG (arXiv 2605.01749, May 2026) achieves up to 13% factuality gain via training-based calibration-aware generation. LoVeC (arXiv 2505.23912, May 2025) uses RL to train LLMs to append on-the-fly confidence scores per statement in long-form generation, achieving 20× speedup over self-consistency methods. All three require base model fine-tuning or RL.\n\n**Post-generation claim-level approaches:** CSS (arXiv 2604.17487, April 2026) decomposes answers into claims and backs off uncertain ones using external verifiers. Selective Abstraction (arXiv 2602.11908, February 2026) replaces low-confidence atoms with confident abstractions.\n\n**Residual-stream anomaly detection:** PCNET (arXiv 2605.05953, May 2026) uses probabilistic circuits on residual streams for hallucination detection + contrastive decoding, reaching up to 99% AUROC — but targets short-form QA and changes content (different token selection) rather than expressing calibrated uncertainty.\n\n**Scaling concerns for activation steering:** Scaling laws for activation steering (ICML 2025) show that CAA effectiveness diminishes with model size on Llama 2 (7B→13B→70B) for behavioral steering (refusal). Endogenous steering resistance (arXiv 2602.06941, February 2026) shows Llama-3.3-70B has 3.8% ESR rate (vs <1% for smaller models). However, CLAS demonstrates successful probe-derived steering on Llama-3.1-70B, suggesting that adaptive, probe-guided steering may be more robust at scale than uniform CAA.\n\n**Gap:** No existing work combines claim-level factuality probing (à la Han et al.) with calibrated activation steering along the verbalized-confidence direction (à la Miao & Ungar) in a single-pass, online framework for long-form generation. This intersection — reading internal accuracy per-claim and steering verbalized confidence to match during generation — is the contribution space. Additionally, no work has tested whether the accuracy-confidence orthogonality discovered at 7–8B scale holds at 70B or in long-form generation contexts, making this verification itself a contribution to the mechanistic understanding of confidence representations.",
  "approach": "We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. The system reads internal accuracy signals per-claim via lightweight probes and steers verbalized confidence to match via targeted activation intervention, producing naturally hedged language for uncertain claims while leaving confident-and-correct claims untouched.\n\n**Pilot Experiment — Orthogonality Verification at Scale (~8h, 2× H100, first week):** Before committing the full experimental budget, we replicate Miao & Ungar's orthogonality analysis on Llama 3.1-70B in a long-form generation setting. We extract accuracy and confidence directions from biography-generation hidden states (not QA), measure their cosine similarity, and compare against the < 0.04 value found at 7–8B scale. This pilot has three outcomes: (a) orthogonality holds (cosine < 0.1) — proceed as planned, report the scaling result as a contribution; (b) orthogonality partially holds (cosine 0.1–0.3) — adapt steering to project out the accuracy component from the confidence direction before steering, proceed with modified approach; (c) orthogonality fails (cosine > 0.3) — report as an important negative finding about the limits of linear feature geometry at scale, fall back to the 8B-only configuration. All three outcomes produce publishable results.\n\n**Offline Stage 1 — Factuality Probe Training (~12h wall, 2× H100 for 70B; ~4h, 1× H100 for 8B; one-time per model):** Generate long-form outputs (biographies, factual descriptions) from the target model, decompose into atomic claims using FActScore/OpenFActScore decomposition, verify claim factuality against knowledge sources. Extract hidden states at each claim's token span across multiple layers (following Han et al.'s layer-group methodology). Train lightweight linear probes (logistic regression on span-aggregated hidden states) to predict continuous factuality confidence scores. Unlike Han et al.'s binary factuality labels, we train on soft labels derived from verification confidence, enabling graded uncertainty estimation.\n\n**Offline Stage 2 — Verbalized-Confidence Direction Extraction (~5h wall, 2× H100 for 70B; ~2h, 1× H100 for 8B; one-time per model):** Extract a verbalized-confidence steering direction via contrastive activation pairs: generate matched claim pairs where the same factual content is expressed with high confidence ('X was born in Y') vs. hedged uncertainty ('X was reportedly born in Y, though I am not certain'). The mean activation difference yields the steering direction, following the contrastive methodology from Ji et al. (VUF) and Miao & Ungar (CAA). For the 70B model, if the pilot reveals partial orthogonality degradation, we apply Gram-Schmidt orthogonalization to project the confidence direction away from the accuracy direction before use.\n\n**Online Stage — Probe-Guided Steering During Generation:** During autoregressive generation: (1) At each generated token, run the factuality probe on its hidden states — this is a single matrix-vector multiplication with negligible overhead. (2) Maintain a running mean probe score over the current sentence span using a sliding window. (3) At sentence boundaries (detected from generated punctuation — periods, newlines — which are trivially available during generation), evaluate the accumulated probe score against a calibrated threshold. (4) If the probe indicates internal uncertainty (score below threshold) while the generation shows no hedging markers, apply a steering offset along the extracted verbalized-confidence direction on subsequent tokens, with steering magnitude α proportional to the miscalibration gap: α = β × max(0, threshold − probe_score), where β is calibrated on a held-out validation set. This adaptive formula is conceptually related to CLAS's context-dependent steering, but driven by per-claim factuality probe scores rather than general input-context sensing vectors. (5) Deactivate steering when the probe score recovers above threshold.\n\n**Key design choices addressing known limitations:** (a) Span-aggregated probe scores over the full claim token range avoid the single-token prefix-contamination problem — the signal reflects the entire claim, not just the cumulative prefix. (b) Single-pass online monitoring eliminates the two-pass chicken-and-egg problem identified for the original CL-MUC approach — no position-aligned regeneration needed. (c) Continuous calibrated steering (not binary neuron clamping) produces graded hedging proportional to internal uncertainty, distinguishing this from Han et al.'s binary intervention. (d) Operating on the verbalized-confidence direction (orthogonal to accuracy per Miao & Ungar, verified at 70B scale in our pilot) means steering affects expression style without corrupting the model's factual knowledge. (e) Adaptive steering magnitude based on probe-detected need may mitigate the diminishing effectiveness of uniform CAA at larger scales (ICML 2025 scaling laws), since steering is only applied where needed and at probe-calibrated intensity.\n\n**Models:** Llama 3.1-70B-Instruct as primary (standard dense transformer architecture, well-studied for probing and steering, large enough to test scaling of the orthogonality finding, with CLAS confirming probe-derived steering viability at this scale). Llama 3.1-8B-Instruct as validation (enables direct comparison with Miao & Ungar and Ji et al. baselines on the same model family, validates the pipeline in well-charted territory before scaling). Both models use standard transformer attention across all layers, avoiding the untested territory of hybrid DeltaNet architectures (e.g., Qwen 3.5) where linear probe and steering techniques lack validation.\n\n**Benchmarks:** FActScore (biography generation, primary) and LongFact (diverse long-form factuality). Metrics: claim-level ECE, Brier score (calibration quality), AUROC (uncertainty detection), FActScore/factual precision (to verify steering does not degrade content quality), and MT-Bench fluency subset (to verify generation quality preservation). We also report the cosine similarity between accuracy and confidence directions at 70B scale as a standalone mechanistic finding.\n\n**Quantitative targets:** We expect RaS to achieve: (1) claim-level ECE reduction of ≥40% relative to unsteered baselines on both FActScore and LongFact; (2) FActScore preservation within 2% of unsteered baseline (steering affects verbal expression, not factual content); (3) uncertainty detection AUROC ≥0.80 (probe-based); (4) superior calibration (lower ECE) compared to Han et al.'s binary neuron clamping at comparable or better FActScore. These targets are informed by Miao & Ungar's response-level results (ECE reductions of 70–90% on QA), discounted for the harder claim-level long-form setting.\n\n**Comparisons:** (1) Unsteered baseline, (2) Han et al.'s probes + neuron clamping (closest representation-based method for long-form), (3) CURE (closest training-based method, if reproducible), (4) LoVeC (RL-based long-form verbalized confidence, if reproducible), (5) Ablations: probe-only detection without steering, uniform steering without probe guidance, VUF-only steering (Ji et al.'s original method applied per-claim), CORAL-style MLP probes vs. linear probes, varying layers for probe extraction, steering strength sensitivity, CLAS-style sensing vector vs. probe-score-driven adaptation.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~250h H100 80GB (orthogonality pilot ~8h [2×H100], probe training + direction extraction ~34h [20h 70B on 2×H100, 6h 8B], Llama 3.1-70B generation + evaluation on FActScore + LongFact ~100h [2×H100], Llama 3.1-8B validation ~25h, baseline comparisons ~45h, ablations ~38h)",
      "gpu_utilization": "~20-30% effective — GPU idles during code development, pipeline debugging, and results analysis",
      "timeline": "5-7 weeks (1 researcher full-time)",
      "team": "1-2 researchers with mechanistic interpretability and activation steering experience",
      "estimated_gpu_cost": "$625-875 (at ~$2.50-3.50/hr H100 80GB spot)"
    },
    "human_in_loop": {
      "gpu_hours": "~200h H100 80GB (agent handles pipeline code, probe training iteration, evaluation scripting; human approves pilot results, probe design, steering threshold calibration, and ablation priorities)",
      "gpu_utilization": "~45-60% — agent queues experiments between human check-ins",
      "timeline": "3-4 weeks",
      "team": "1 researcher, ~30min/day for methodology decisions, pilot outcome assessment, and qualitative hedging evaluation",
      "claude_api_cost": "$100-200 (~1500-3000 Opus turns)",
      "estimated_gpu_cost": "$500-700",
      "risk_note": "Primary risk: whether accuracy-confidence orthogonality holds at 70B scale in long-form generation — the ~8h pilot experiment validates this before committing the full budget. If orthogonality breaks (outcome c), we fall back to an 8B-only paper with the negative scaling result as a contribution, reducing total compute to ~80h H100. Secondary risk: whether probe-guided steering produces natural hedging at 70B or degrades fluency — qualitative human assessment is essential. Tertiary risk: CAA effectiveness diminishing at 70B scale (per ICML 2025 scaling laws), though our adaptive probe-guided approach may be more robust than uniform steering."
    },
    "auto_research": {
      "gpu_hours": "~280h H100 80GB (agent explores probe architectures, layer selections, steering schedules across both models, plus comprehensive evaluation)",
      "gpu_utilization": "~80-90% — continuous experiment pipeline with minimal idle",
      "timeline": "7-10 days with 2× H100 80GB",
      "team": "0 researchers (initial setup + final review only)",
      "claude_api_cost": "$200-400 (~3000-6000 Opus turns)",
      "estimated_gpu_cost": "$700-980",
      "speed_bottleneck": "Long-form generation throughput on Llama 3.1-70B with 2× H100 tensor parallelism (~20-30 tok/s) — generating and evaluating hundreds of long-form responses per configuration is the computational bottleneck",
      "risk_note": "Without human judgment, agent may over-optimize probe thresholds on validation set rather than ensuring robustness, may miss qualitative assessment of hedging naturalness, and critically may not correctly interpret the orthogonality pilot results (the decision to proceed vs. pivot requires understanding of the mechanistic implications)"
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — ~10 weeks; conference Feb 16-23, Montréal) — PRIMARY",
    "ARR August 2026 (submission Aug 3, 2026 — ~11 weeks; committable to EMNLP 2026 Oct 24-29 or later *ACL venues)",
    "ICLR 2027 (expected submission ~Oct 2026, ~20 weeks; comfortable timeline)"
  ],
  "level": "solid",
  "key_references": [
    "Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation (Han et al., Findings of EMNLP 2025) — closest prior work: claim-level probes + neuron clamping in long-form generation",
    "Closing the Confidence-Faithfulness Gap in LLMs (Miao & Ungar, arXiv 2603.25052, March 2026) — accuracy-confidence orthogonality discovery + adaptive CAA steering; explicitly notes scaling and long-form extension as open questions",
    "Correctness-Optimized Residual Activation Lens [CORAL] (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) — same group; MLP probes → correctness steering on MCQA at 7B scale; must differentiate as response-level, short-form only",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025) — VUF discovery and MUC for response-level short-form QA",
    "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model [ITI] (Li et al., NeurIPS 2023) — foundational probe→steer paradigm using linear probes on attention heads for truthfulness",
    "Enhancing Language Model Factuality via Activation-Based Confidence Calibration and Guided Decoding [ActCab/CoDec] (EMNLP 2024) — activation calibration + confidence-guided decoding for QA factuality",
    "Contextual Linear Activation Steering [CLAS] (Hsu et al., arXiv 2604.24693, April 2026) — probe-derived adaptive steering with context-dependent strength; tested on Llama-3.1-70B, confirming steering viability at 70B scale",
    "How do LLMs Compute Verbal Confidence? (Kumaran et al., arXiv 2603.17839, March 2026) — mechanistic evidence for cached confidence retrieval at answer-adjacent positions",
    "Reinforcement Learning for Better Verbalized Confidence in Long-Form Generation [LoVeC] (arXiv 2505.23912, May 2025) — RL-based on-the-fly confidence scoring per statement in long-form generation; training-based",
    "Scaling Laws for Activation Steering with Llama 2 Models and Refusal Mechanisms (ICML 2025) — demonstrates CAA effectiveness diminishes with model size (7B→70B); informs our adaptive steering design",
    "Endogenous Resistance to Activation Steering in Language Models (arXiv 2602.06941, February 2026) — Llama-3.3-70B shows 3.8% endogenous steering resistance; relevant scaling concern",
    "Does Transformer Interpretability Transfer to RNNs? (2024) — probing and CAA partially transfer to recurrent architectures with reduced effectiveness; motivates our choice of standard transformer models",
    "SteerConf: Steering LLMs for Confidence Elicitation (Zhou et al., NeurIPS 2025) — prompt-based training-free confidence calibration",
    "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025) — diverse steering vectors with adaptive intensity control",
    "Real-Time Detection of Hallucinated Entities in Long-Form Generation (Obeso et al., arXiv 2509.03531, 2025) — entity-level streaming probes for long-form generation",
    "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits [PCNET] (arXiv 2605.05953, May 2026) — residual stream anomaly detection + contrastive decoding intervention",
    "Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, January 2026) — online hallucination detection as evolving latent state",
    "Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration [CURE] (arXiv 2604.12046, April 2026) — multi-stage training for claim-level confidence reasoning",
    "Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality [CAG] (arXiv 2605.01749, May 2026) — training-based calibration-aware generation",
    "Atomic Calibration of LLMs in Long-Form Generations (Findings of AACL-IJCNLP 2025) — showed poor claim-level calibration in long-form outputs",
    "Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control [CSS] (arXiv 2604.17487, April 2026) — post-generation specificity control via external verifiers",
    "When Should LLMs Be Less Specific? Selective Abstraction for Reliable Long-Form Text Generation (arXiv 2602.11908, February 2026)",
    "Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs (ICML 2024) — linear probes approximate semantic entropy at response level",
    "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023)",
    "Long-form Factuality in Large Language Models [LongFact/SAFE] (NeurIPS 2024)",
    "Steering Language Models With Activation Engineering (Turner et al., arXiv 2308.10248, 2023)"
  ],
  "description": "We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. Motivated by two key findings — Han et al. (EMNLP 2025) showed lightweight probes detect claim-level factuality in long-form hidden states, and Miao & Ungar (2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features — RaS combines both insights in a novel way: it reads claim-level accuracy signals via factuality probes during autoregressive generation and steers verbalized confidence to match via targeted activation intervention along the orthogonal confidence direction, all within a single forward pass. Unlike Han et al.'s neuron clamping (binary suppression of hallucinations), RaS produces calibrated verbal hedging proportional to the model's internal uncertainty. Unlike CURE, CAG, and LoVeC, it requires no base model training — only lightweight linear probe fitting and contrastive direction extraction. The probe-guided adaptive steering formula (α = β × max(0, threshold − probe_score)) relates to CLAS's context-dependent steering but is driven by per-claim factuality signals rather than general context sensing, and targets confidence expression rather than content correctness (as in ITI, CORAL, and ActCab/CoDec). The framework includes a dedicated pilot experiment verifying the accuracy-confidence orthogonality at 70B scale in long-form generation — extending Miao & Ungar's finding beyond the 7–8B QA setting where it was established. We evaluate on Llama 3.1-70B (primary, testing scaling) and Llama 3.1-8B (validation, direct comparison with prior work) using FActScore and LongFact, measuring claim-level ECE, Brier score, AUROC, and factual precision. We expect ≥40% claim-level ECE reduction over unsteered baselines while preserving FActScore within 2%. Both models use standard transformer architectures, avoiding the untested hybrid DeltaNet territory (e.g., Qwen 3.5) where linear probing and activation steering techniques lack validation. All experiments fit within ~250 H100-hours.",
  "project_name": "probe_guided_claim_calibration",
  "source": "web_research"
}

## Reviewer feedback (round 3)
Issues: ["COMPUTE EXCEEDS CONSTRAINT: Manual mode estimates ~250h H100-hours, auto mode ~280h, and even HIL mode is at the exact 200h limit. The user's hard constraint is ≤200 H100-hours total. The breakdown shows ~38h for ablations and ~45h for baselines — both need trimming, and dropping the 8B validation track (~25h) or reducing 70B evaluation scope would help.", "MISSING COMPETITOR — 'A Single Direction of Truth' (O'Neill et al., arXiv 2507.23221, July 2025): Uses a linear probe on an observer model's residual stream to detect hallucinations (outperforming baselines by 5–27 points on Gemma-2 2B–27B), then uses the probe direction as a steering vector to causally reduce hallucination rates. While it uses an external observer model (vs. RaS's self-probing) and targets binary hallucination (vs. calibrated confidence), the probe→steer pipeline is very close. Must be cited with clear differentiation: RaS self-probes claim-level factuality for graded confidence calibration; O'Neill et al. use an observer model for binary hallucination detection/reduction.", "MISSING COMPETITOR — CARE (Yuan et al., SIGIR 2025): Fact-level calibration and correction framework for long-form generation using confidence-aware fact correction where high-confidence facts iteratively refine low-confidence ones. Directly addresses the same problem (fact-level calibration in long-form) with a different mechanism (iterative correction vs. activation steering). Must be cited.", "SENTENCE-BOUNDARY STEERING LATENCY: The approach evaluates accumulated probe scores 'at sentence boundaries' and applies steering to 'subsequent tokens.' This means an uncertain claim within Sentence N is generated with confident language, and hedging only appears in Sentence N+1 onward. The output reads as 'Barack Obama was born in Kenya. However, I am not fully certain about the above.' — the hallucinated claim itself remains confidently expressed. This is a fundamental design limitation that either (a) should be acknowledged as a known tradeoff, (b) mitigated with sub-sentence evaluation triggers (e.g., every K tokens or at clause boundaries), or (c) reframed as 'forward-looking uncertainty conditioning' rather than 'per-claim calibrated hedging.'", "QUANTITATIVE TARGETS MAY BE OVEROPTIMISTIC: The ≥40% claim-level ECE reduction target is derived by 'discounting' Miao & Ungar's response-level QA results (70–90% ECE reduction). But claim-level ECE in long-form generation faces additional challenges: noisy claim boundary detection, probe signal dilution from long-context hidden states, and the sentence-boundary steering latency. A more conservative target (e.g., ≥25% ECE reduction) would be more defensible.", "MISSING ADVANCED STEERING BASELINES: The proposal compares against static VUF steering but not against recent adaptive steering methods that could serve as stronger baselines: Spherical Steering (You et al., Feb 2026 — rotation-based with confidence gating), CAST (IBM, ICLR 2025 — conditional activation steering), and FLAS (Jin et al., May 2026 — flow-based activation steering). At minimum, CAST's conditional steering paradigm (apply steering only when a condition is met) is conceptually close to probe-triggered steering and should be discussed."]
Feedback: The proposal has improved substantially since Round 1 — replacing Qwen3.5, fixing the two-pass problem, citing CORAL/CLAS/ITI/ActCab, and adding the orthogonality pilot are all strong revisions. The core gap remains real. Here are the remaining fixes:

**1. Reduce compute to ≤200 H100-hours (REQUIRED):**
The most straightforward path: drop the 8B validation track (~25h saved), reduce ablations from 5 to 3 (~15h saved), and tighten baseline comparisons to the 2 most relevant (Han et al. neuron clamping + CURE) (~15h saved). This brings the total to ~195h. Alternatively, reduce the 70B evaluation corpus size by 30% and keep the 8B track as a lighter sanity check (~10h instead of 25h).

**2. Cite 'A Single Direction of Truth' and CARE:**
O'Neill et al. (2025) is the closest probe→steer work for hallucinations. Differentiate on three axes: (a) self-probing vs. external observer, (b) calibrated confidence vs. binary hallucination, (c) claim-level granularity in long-form vs. span-level in short contexts. CARE (SIGIR 2025) should be cited as a parallel approach to fact-level calibration that uses iterative correction rather than activation steering.

**3. Address the steering latency problem (CRITICAL for technical credibility):**
Three options, in order of preference:
(a) **Best: Sub-sentence triggers.** Evaluate probe scores every K tokens (e.g., K=8) with a running exponential average, and trigger steering mid-sentence when the score drops below threshold. This hedges the CURRENT claim by steering later tokens in the same sentence (e.g., steering mid-generation produces 'Obama was born in — well, I believe it may have been — Kenya, though I'm not fully certain'). The cost is slightly more frequent threshold checks, which is negligible.
(b) **Acceptable: Acknowledge and empirically measure the latency.** Report what fraction of uncertain claims get hedged within the same sentence vs. in subsequent sentences. If the probe signal rises early in claims (as Kumaran et al.'s cached-retrieval finding suggests), mid-claim steering may be feasible even with sentence-boundary triggers.
(c) **Minimum: Reframe as 'forward-looking uncertainty conditioning.'** Acknowledge that RaS conditions subsequent generation on detected uncertainty, producing uncertainty-aware continuation rather than per-claim hedging.

**4. Temper quantitative targets:**
Set the primary ECE reduction target at ≥25% (vs. ≥40%), noting that Miao & Ungar's 70–90% reductions were on response-level QA with 7–8B models, and claim-level long-form calibration at 70B is substantially harder. Keep ≥40% as a stretch goal. This protects the paper from appearing to underperform its own targets.

**5. Discuss CAST (ICLR 2025) as conceptual relative:**
CAST's conditional activation steering (apply steering only when activation patterns match a condition) is conceptually close to probe-triggered steering. One sentence in the landscape distinguishing RaS's data-driven probe threshold from CAST's learned condition vector is sufficient.

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "08c963d2-c493-4608-a390-ca658143e76f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T14:24:52.475Z_

```json
{
  "parentUuid": "08c963d2-c493-4608-a390-ca658143e76f",
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
  "uuid": "b61e2e6f-b71f-4250-b77d-ff40b58e579b",
  "timestamp": "2026-05-15T14:24:52.475Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T14:24:52.476Z_

```json
{
  "parentUuid": "b61e2e6f-b71f-4250-b77d-ff40b58e579b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8009c785-5cc4-4580-931b-e86883d8d4b7",
  "timestamp": "2026-05-15T14:24:52.476Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-15 (UTC).**  ## Original idea {   \"title\": \"Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Lo…",
  "leafUuid": "8009c785-5cc4-4580-931b-e86883d8d4b7",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Claim-level confidence calibration in long-form generation via steering",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

### Assistant

_source line 8 · 2026-05-15T14:24:58.664Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully and plan my research approach:

1. **Compute constraint (≤200 H100-hours)** - Need to trim the budget
2. **Missing competitor: "A Single Direction of Truth" (O'Neill et al., arXiv 2507.23221)** - Need to find and read this paper
3. **Missing competitor: CARE (Yuan et al., SIGIR 2025)** - Need to find and read this paper
4. **Sentence-boundary steering latency** - Critical design issue


5. **Overoptimistic quantitative targets** - Need to temper expectations
6. **Missing advanced steering baselines: CAST, Spherical Steering, FLAS** - Need to find and discuss these methods

I should start by searching for all these papers and understanding what they contribute to the field.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8009c785-5cc4-4580-931b-e86883d8d4b7",
  "isSidechain": false,
  "requestId": "req_011Cb4WQ5QBoaT2e61u1KgQD",
  "type": "assistant",
  "uuid": "8bad0f72-66f3-48e4-b0f7-c5e2256e02af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqVtn1D9LKmP3uWnMLr5WY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15109,
      "cache_read_input_tokens": 11841,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15109,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 310,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15109
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

_source line 9 · 2026-05-15T14:24:58.678Z_

I'll research the reviewer's flagged issues in parallel — searching for the missing competitors and advanced steering baselines — then synthesize and revise.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bad0f72-66f3-48e4-b0f7-c5e2256e02af",
  "isSidechain": false,
  "requestId": "req_011Cb4WQ5QBoaT2e61u1KgQD",
  "type": "assistant",
  "uuid": "aebf26cb-e4f4-4220-ba8d-946c78a4245e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqVtn1D9LKmP3uWnMLr5WY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15109,
      "cache_read_input_tokens": 11841,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15109,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 310,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15109
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

_source line 10 · 2026-05-15T14:24:59.108Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Qe2wa9JyhVSb3YvaQha5Ec`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aebf26cb-e4f4-4220-ba8d-946c78a4245e",
  "isSidechain": false,
  "requestId": "req_011Cb4WQ5QBoaT2e61u1KgQD",
  "type": "assistant",
  "uuid": "5d89d81e-8aa8-4aee-bdf9-ec287e01d365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqVtn1D9LKmP3uWnMLr5WY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15109,
      "cache_read_input_tokens": 11841,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15109,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 310,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15109
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

_source line 11 · 2026-05-15T14:24:59.114Z_

<details><summary>↩ Tool result · `toolu_01Qe2wa9JyhVSb3YvaQha5Ec`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d89d81e-8aa8-4aee-bdf9-ec287e01d365",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "d571df63-5e3c-43e5-8424-83e3e1fd3fa5",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "5d89d81e-8aa8-4aee-bdf9-ec287e01d365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-15T14:25:01.704Z_

Now let me search for all the missing competitors and baselines in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d571df63-5e3c-43e5-8424-83e3e1fd3fa5",
  "isSidechain": false,
  "requestId": "req_011Cb4WQa3NMHeXMuxxSLx6G",
  "type": "assistant",
  "uuid": "93b1c7b2-a575-4007-8d63-dc7b343a6537",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hh1HScf1mkcJz39FCX92xY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1329,
      "cache_read_input_tokens": 26950,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 26950,
          "cache_creation_input_tokens": 1329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1329
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

_source line 13 · 2026-05-15T14:25:02.348Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YKZfn491tXuf2YTR36BPgt`</summary>

```json
{
  "query": "O'Neill \"A Single Direction of Truth\" arXiv 2507.23221 probe steering hallucination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93b1c7b2-a575-4007-8d63-dc7b343a6537",
  "isSidechain": false,
  "requestId": "req_011Cb4WQa3NMHeXMuxxSLx6G",
  "type": "assistant",
  "uuid": "60de720d-9afe-4d32-9b73-71b65f2db373",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hh1HScf1mkcJz39FCX92xY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1329,
      "cache_read_input_tokens": 26950,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 26950,
          "cache_creation_input_tokens": 1329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1329
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

_source line 14 · 2026-05-15T14:25:08.802Z_

<details><summary>↩ Tool result · `toolu_01YKZfn491tXuf2YTR36BPgt`</summary>

```text
Web search results for query: "O'Neill "A Single Direction of Truth" arXiv 2507.23221 probe steering hallucination"

Links: [{"title":"[2507.23221] A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations","url":"https://arxiv.org/abs/2507.23221"},{"title":"A Single Direction of Truth: An Observer Model’s Linear Residual Probe","url":"https://arxiv.org/pdf/2507.23221"},{"title":"A Single Direction of Truth: An Observer Model’s Linear Residual Probe Exposes and Steers Contextual Hallucinations","url":"https://arxiv.org/html/2507.23221v1"},{"title":"Computer Science Jul 2025","url":"https://arxiv.org/list/cs/2025-07?skip=10600&show=25"}]

I found the paper! Here's what the search results reveal:

"A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations" by Charles O'Neill and colleagues addresses contextual hallucinations in AI and demonstrates that a generator-agnostic observer model can detect hallucinations via a single forward pass and a linear probe on its residual stream.

Key findings include:

- The probe isolates a single, transferable linear direction separating hallucinated from faithful text, outperforming baselines by 5-27 points and showing robust mid-layer performance across Gemma-2 models (2B to 27B).

- Gradient-times-activation localizes this signal to sparse, late-layer MLP activity.

- Manipulating this direction causally steers generator hallucination rates, proving its actionability.

- The results provide novel evidence of internal, low-dimensional hallucination tracking linked to specific MLP sub-circuits, and the authors released the 2000-example ContraTales benchmark for realistic assessment of such solutions.

The paper was published on July 31, 2025, as arXiv preprint 2507.23221.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60de720d-9afe-4d32-9b73-71b65f2db373",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "ce1cc560-afeb-42b6-ab6b-f2ce0126d748",
  "toolUseResult": {
    "query": "O'Neill \"A Single Direction of Truth\" arXiv 2507.23221 probe steering hallucination",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V1bxu9j6iHdqBWCHZccu2v",
        "content": [
          {
            "title": "[2507.23221] A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations",
            "url": "https://arxiv.org/abs/2507.23221"
          },
          {
            "title": "A Single Direction of Truth: An Observer Model’s Linear Residual Probe",
            "url": "https://arxiv.org/pdf/2507.23221"
          },
          {
            "title": "A Single Direction of Truth: An Observer Model’s Linear Residual Probe Exposes and Steers Contextual Hallucinations",
            "url": "https://arxiv.org/html/2507.23221v1"
          },
          {
            "title": "Computer Science Jul 2025",
            "url": "https://arxiv.org/list/cs/2025-07?skip=10600&show=25"
          }
        ]
      },
      "I found the paper! Here's what the search results reveal:\n\n\"A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations\" by Charles O'Neill and colleagues addresses contextual hallucinations in AI and demonstrates that a generator-agnostic observer model can detect hallucinations via a single forward pass and a linear probe on its residual stream.\n\nKey findings include:\n\n- The probe isolates a single, transferable linear direction separating hallucinated from faithful text, outperforming baselines by 5-27 points and showing robust mid-layer performance across Gemma-2 models (2B to 27B).\n\n- Gradient-times-activation localizes this signal to sparse, late-layer MLP activity.\n\n- Manipulating this direction causally steers generator hallucination rates, proving its actionability.\n\n- The results provide novel evidence of internal, low-dimensional hallucination tracking linked to specific MLP sub-circuits, and the authors released the 2000-example ContraTales benchmark for realistic assessment of such solutions.\n\nThe paper was published on July 31, 2025, as arXiv preprint 2507.23221."
    ],
    "durationSeconds": 6.449502452999999
  },
  "sourceToolAssistantUUID": "60de720d-9afe-4d32-9b73-71b65f2db373",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T14:25:11.274Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EmGDQ51Hu53NZosSrFVMmj`</summary>

```json
{
  "query": "CARE Yuan SIGIR 2025 fact-level calibration correction long-form generation confidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce1cc560-afeb-42b6-ab6b-f2ce0126d748",
  "isSidechain": false,
  "requestId": "req_011Cb4WRGxjwowwXca1qK6bf",
  "type": "assistant",
  "uuid": "8f0fc668-cdfb-4473-89a8-1637b8fcc4ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZg4BdEgRA72WXwEUf1aHJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 28279,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 28279,
          "cache_creation_input_tokens": 625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 625
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

_source line 16 · 2026-05-15T14:25:16.504Z_

<details><summary>↩ Tool result · `toolu_01EmGDQ51Hu53NZosSrFVMmj`</summary>

```text
Web search results for query: "CARE Yuan SIGIR 2025 fact-level calibration correction long-form generation confidence"

Links: [{"title":"Fact-Level Calibration and Correction for Long-Form Generations | Request PDF","url":"https://www.researchgate.net/publication/393657638_Fact-Level_Calibration_and_Correction_for_Long-Form_Generations"},{"title":"SIGIR 2025, Padua, 13-18 July | Accepted Papers - Unipd","url":"https://sigir2025.dei.unipd.it/accepted-papers.html"},{"title":"Atomic Calibration of LLMs in Long-Form Generations","url":"https://arxiv.org/html/2410.13246v2"},{"title":"[2410.13246] Atomic Calibration of LLMs in Long-Form Generations","url":"https://arxiv.org/abs/2410.13246"},{"title":"SIGIR-AP 2025","url":"https://www.sigir-ap.org/sigir-ap-2025/accepted-papers/index.html"},{"title":"The Great Nugget Recall: Automating Fact Extraction and RAG Evaluation with Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/393658928_The_Great_Nugget_Recall_Automating_Fact_Extraction_and_RAG_Evaluation_with_Large_Language_Models"},{"title":"SIGIR-AP 2025 Tutorial Proposal:","url":"https://www.researchgate.net/profile/Su_Weihang/publication/396210825_SIGIR-AP_2025_Tutorial_Proposal_Dynamic_and_Parametric_Retrieval-Augmented_Generation/links/68e2347ef3032e2b4be6b800/SIGIR-AP-2025-Tutorial-Proposal-Dynamic-and-Parametric-Retrieval-Augmented-Generation.pdf"},{"title":"Conformal Linguistic Calibration: Trading-off between Factuality and Specificity","url":"https://arxiv.org/html/2502.19110v1"},{"title":"[2402.06544] Calibrating Long-form Generations from Large Language Models","url":"https://arxiv.org/abs/2402.06544"},{"title":"VeriCite: Towards Reliable Citations in Retrieval-Augmented Generation via Rigorous Verification | Proceedings of the 2025 Annual International ACM SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific Region","url":"https://dl.acm.org/doi/10.1145/3767695.3769505"}]

Based on the search results, I found information about the paper you're looking for:

"Fact-Level Calibration and Correction for Long-Form Generations" is a paper by Yige Yuan, Bingbing Xu, Hexiang Tan, Fei Sun, Teng Xiao, Wei Li, Huawei Shen, and Xueqi Cheng, and it was published on July 13, 2025 at SIGIR '25: The 48th International ACM SIGIR Conference on Research and Development in Information Retrieval.

The paper appears to be related to addressing calibration and correction challenges in long-form text generation. This work decomposes sentences into atomic claims and assigns confidence scores to each claim, which aligns with the "fact-level" aspect mentioned in your query about confidence calibration.

The research contributes to the broader field of ensuring that language models' confidence scores accurately reflect the factuality of their outputs in longer, more complex generations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f0fc668-cdfb-4473-89a8-1637b8fcc4ce",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "1de5f24b-b1f4-497b-aa03-ba7e7961f84b",
  "toolUseResult": {
    "query": "CARE Yuan SIGIR 2025 fact-level calibration correction long-form generation confidence",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FjU8dqjNR3fAMHnuykDqed",
        "content": [
          {
            "title": "Fact-Level Calibration and Correction for Long-Form Generations | Request PDF",
            "url": "https://www.researchgate.net/publication/393657638_Fact-Level_Calibration_and_Correction_for_Long-Form_Generations"
          },
          {
            "title": "SIGIR 2025, Padua, 13-18 July | Accepted Papers - Unipd",
            "url": "https://sigir2025.dei.unipd.it/accepted-papers.html"
          },
          {
            "title": "Atomic Calibration of LLMs in Long-Form Generations",
            "url": "https://arxiv.org/html/2410.13246v2"
          },
          {
            "title": "[2410.13246] Atomic Calibration of LLMs in Long-Form Generations",
            "url": "https://arxiv.org/abs/2410.13246"
          },
          {
            "title": "SIGIR-AP 2025",
            "url": "https://www.sigir-ap.org/sigir-ap-2025/accepted-papers/index.html"
          },
          {
            "title": "The Great Nugget Recall: Automating Fact Extraction and RAG Evaluation with Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/393658928_The_Great_Nugget_Recall_Automating_Fact_Extraction_and_RAG_Evaluation_with_Large_Language_Models"
          },
          {
            "title": "SIGIR-AP 2025 Tutorial Proposal:",
            "url": "https://www.researchgate.net/profile/Su_Weihang/publication/396210825_SIGIR-AP_2025_Tutorial_Proposal_Dynamic_and_Parametric_Retrieval-Augmented_Generation/links/68e2347ef3032e2b4be6b800/SIGIR-AP-2025-Tutorial-Proposal-Dynamic-and-Parametric-Retrieval-Augmented-Generation.pdf"
          },
          {
            "title": "Conformal Linguistic Calibration: Trading-off between Factuality and Specificity",
            "url": "https://arxiv.org/html/2502.19110v1"
          },
          {
            "title": "[2402.06544] Calibrating Long-form Generations from Large Language Models",
            "url": "https://arxiv.org/abs/2402.06544"
          },
          {
            "title": "VeriCite: Towards Reliable Citations in Retrieval-Augmented Generation via Rigorous Verification | Proceedings of the 2025 Annual International ACM SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific Region",
            "url": "https://dl.acm.org/doi/10.1145/3767695.3769505"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\n\"Fact-Level Calibration and Correction for Long-Form Generations\" is a paper by Yige Yuan, Bingbing Xu, Hexiang Tan, Fei Sun, Teng Xiao, Wei Li, Huawei Shen, and Xueqi Cheng, and it was published on July 13, 2025 at SIGIR '25: The 48th International ACM SIGIR Conference on Research and Development in Information Retrieval.\n\nThe paper appears to be related to addressing calibration and correction challenges in long-form text generation. This work decomposes sentences into atomic claims and assigns confidence scores to each claim, which aligns with the \"fact-level\" aspect mentioned in your query about confidence calibration.\n\nThe research contributes to the broader field of ensuring that language models' confidence scores accurately reflect the factuality of their outputs in longer, more complex generations."
    ],
    "durationSeconds": 5.226768871
  },
  "sourceToolAssistantUUID": "8f0fc668-cdfb-4473-89a8-1637b8fcc4ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T14:25:19.099Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fh6p1GaqP63oDAM1Bbd7uq`</summary>

```json
{
  "query": "CAST conditional activation steering ICLR 2025 language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1de5f24b-b1f4-497b-aa03-ba7e7961f84b",
  "isSidechain": false,
  "requestId": "req_011Cb4WRqzqVzaRQkT7Cmbz9",
  "type": "assistant",
  "uuid": "429a709b-9110-45f1-b0e4-497b5b45b82e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AhWfoAzt8g9xiLXKNqPvoP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 983,
      "cache_read_input_tokens": 28904,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 28904,
          "cache_creation_input_tokens": 983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 983
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

_source line 18 · 2026-05-15T14:25:27.204Z_

<details><summary>↩ Tool result · `toolu_01Fh6p1GaqP63oDAM1Bbd7uq`</summary>

```text
Web search results for query: "CAST conditional activation steering ICLR 2025 language model"

Links: [{"title":"Published as a conference paper at ICLR 2025 PROGRAMMING REFUSAL WITH","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/e2dd53601de57c773343a7cdf09fae1c-Paper-Conference.pdf"},{"title":"[2409.05907] Programming Refusal with Conditional Activation Steering","url":"https://arxiv.org/abs/2409.05907"},{"title":"Programming Refusal with Conditional Activation Steering | OpenReview","url":"https://openreview.net/forum?id=Oi47wc10sm"},{"title":"Paper Code 50+ ! Conditional Activation Steering Programming Refusal with","url":"https://iclr.cc/media/iclr-2025/Slides/29806.pdf"},{"title":"GitHub - IBM/activation-steering: [ICLR 2025] General-purpose activation steering library · GitHub","url":"https://github.com/IBM/activation-steering"},{"title":"activation-steering/docs/faq.md at main · IBM/activation-steering","url":"https://github.com/IBM/activation-steering/blob/main/docs/faq.md"},{"title":"Programming Refusal with Conditional Activation Steering for ICLR 2025 - IBM Research","url":"https://research.ibm.com/publications/programming-refusal-with-conditional-activation-steering"},{"title":"ICLR Poster Programming Refusal with Conditional Activation Steering","url":"https://iclr.cc/virtual/2025/poster/29806"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Programming Refusal with Conditional Activation Steering","url":"https://arxiv.org/html/2409.05907v3"}]

Based on the search results, here's what I found about CAST (Conditional Activation Steering):

## Overview

Conditional Activation Steering (CAST) is a method that analyzes LLM activation patterns during inference to selectively apply or withhold activation steering based on the input context. CAST is a spotlight paper at ICLR 2025.

## Key Innovation

CAST allows selective refusal, refusing harmful prompts while minimizing the harmless refusal rate. This addresses a major limitation of existing methods: adding a "refusal vector" using existing activation steering methods increases refusal rates indiscriminately across all inputs, limiting the model's utility.

## Technical Approach

The method introduces a new type of steering vector called a condition vector, representing certain activation patterns induced by the prompt during inference, and a simple similarity calculation between this condition vector and the model's activation at inference time effectively serves as a switch, determining whether to apply the refusal vector.

## Practical Applications

Using CAST, one can systematically control LLM behavior with rules like "if input is about hate speech or adult content, then refuse" or "if input is not about legal advice, then refuse," allowing for selective modification of responses to specific content while maintaining normal responses to other content, all without requiring weight optimization.

## Implementation

CAST maintains the data, runtime, and compute efficiency of activation steering while adding controllability, enabling the implementation of behavioral rules in LLMs without significant costs. The researchers have released an open-source implementation at github.com/IBM/activation-steering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "429a709b-9110-45f1-b0e4-497b5b45b82e",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "0af6f84d-fe2b-4e5c-9175-64e37a236458",
  "toolUseResult": {
    "query": "CAST conditional activation steering ICLR 2025 language model",
    "results": [
      {
        "tool_use_id": "srvtoolu_016b3hmZwSZdbHKqSCdV8qTe",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2025 PROGRAMMING REFUSAL WITH",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/e2dd53601de57c773343a7cdf09fae1c-Paper-Conference.pdf"
          },
          {
            "title": "[2409.05907] Programming Refusal with Conditional Activation Steering",
            "url": "https://arxiv.org/abs/2409.05907"
          },
          {
            "title": "Programming Refusal with Conditional Activation Steering | OpenReview",
            "url": "https://openreview.net/forum?id=Oi47wc10sm"
          },
          {
            "title": "Paper Code 50+ ! Conditional Activation Steering Programming Refusal with",
            "url": "https://iclr.cc/media/iclr-2025/Slides/29806.pdf"
          },
          {
            "title": "GitHub - IBM/activation-steering: [ICLR 2025] General-purpose activation steering library · GitHub",
            "url": "https://github.com/IBM/activation-steering"
          },
          {
            "title": "activation-steering/docs/faq.md at main · IBM/activation-steering",
            "url": "https://github.com/IBM/activation-steering/blob/main/docs/faq.md"
          },
          {
            "title": "Programming Refusal with Conditional Activation Steering for ICLR 2025 - IBM Research",
            "url": "https://research.ibm.com/publications/programming-refusal-with-conditional-activation-steering"
          },
          {
            "title": "ICLR Poster Programming Refusal with Conditional Activation Steering",
            "url": "https://iclr.cc/virtual/2025/poster/29806"
          },
          {
            "title": "Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra",
            "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"
          },
          {
            "title": "Programming Refusal with Conditional Activation Steering",
            "url": "https://arxiv.org/html/2409.05907v3"
          }
        ]
      },
      "Based on the search results, here's what I found about CAST (Conditional Activation Steering):\n\n## Overview\n\nConditional Activation Steering (CAST) is a method that analyzes LLM activation patterns during inference to selectively apply or withhold activation steering based on the input context. CAST is a spotlight paper at ICLR 2025.\n\n## Key Innovation\n\nCAST allows selective refusal, refusing harmful prompts while minimizing the harmless refusal rate. This addresses a major limitation of existing methods: adding a \"refusal vector\" using existing activation steering methods increases refusal rates indiscriminately across all inputs, limiting the model's utility.\n\n## Technical Approach\n\nThe method introduces a new type of steering vector called a condition vector, representing certain activation patterns induced by the prompt during inference, and a simple similarity calculation between this condition vector and the model's activation at inference time effectively serves as a switch, determining whether to apply the refusal vector.\n\n## Practical Applications\n\nUsing CAST, one can systematically control LLM behavior with rules like \"if input is about hate speech or adult content, then refuse\" or \"if input is not about legal advice, then refuse,\" allowing for selective modification of responses to specific content while maintaining normal responses to other content, all without requiring weight optimization.\n\n## Implementation\n\nCAST maintains the data, runtime, and compute efficiency of activation steering while adding controllability, enabling the implementation of behavioral rules in LLMs without significant costs. The researchers have released an open-source implementation at github.com/IBM/activation-steering."
    ],
    "durationSeconds": 8.101293770999996
  },
  "sourceToolAssistantUUID": "429a709b-9110-45f1-b0e4-497b5b45b82e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T14:25:30.690Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GEQXaA1kpSee4HJRto71Hb`</summary>

```json
{
  "query": "FLAS \"flow-based activation steering\" Jin 2026 language model arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0af6f84d-fe2b-4e5c-9175-64e37a236458",
  "isSidechain": false,
  "requestId": "req_011Cb4WSdpPSbQcJyA65rhGv",
  "type": "assistant",
  "uuid": "d761566d-4e54-43ca-a560-bd925b4f46b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8SNXC1idXz6ePJHyoovAf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 938,
      "cache_read_input_tokens": 29887,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 938,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 29887,
          "cache_creation_input_tokens": 938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 938
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

_source line 20 · 2026-05-15T14:25:39.677Z_

<details><summary>↩ Tool result · `toolu_01GEQXaA1kpSee4HJRto71Hb`</summary>

```text
Web search results for query: "FLAS "flow-based activation steering" Jin 2026 language model arXiv"

Links: [{"title":"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/html/2605.05892"},{"title":"[2605.05892] Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/abs/2605.05892"},{"title":"[2308.10248] Activation Addition: Steering Language Models Without Optimization","url":"https://ar5iv.labs.arxiv.org/html/2308.10248"},{"title":"Activation Addition: Steering Language Models Without Optimization","url":"https://arxiv.org/pdf/2308.10248v3"},{"title":"[2308.10248] Steering Language Models With Activation Engineering","url":"https://arxiv.org/abs/2308.10248"},{"title":"STEERING LANGUAGE MODELS WITH ACTIVATION EN- GINEERING Alexander Matt Turner","url":"https://arxiv.org/pdf/2308.10248"},{"title":"Steering Language Models With Activation Engineering","url":"https://arxiv.org/html/2308.10248v5"},{"title":"[2604.24693] Contextual Linear Activation Steering of Language Models","url":"https://arxiv.org/abs/2604.24693"},{"title":"GitHub - ZFancy/awesome-activation-engineering: A curated list of resources for activation engineering · GitHub","url":"https://github.com/ZFancy/awesome-activation-engineering"},{"title":"The Rogue Scalpel: Activation Steering Compromises LLM Safety","url":"https://arxiv.org/html/2509.22067v2"}]

Based on the search results, I found information about the paper you're looking for:

## FLAS: Flow-based Activation Steering

FLAS (Flow-based Activation Steering) learns a general, concept-conditioned velocity field for controlling language model behavior. The paper is by Zehao Jin and colleagues at Georgia Institute of Technology.

### Key Contributions

Activation steering has emerged as a promising alternative for controlling language-model behavior at inference time by modifying intermediate representations while keeping model parameters frozen, but existing steering methods typically restrict steering interventions to fixed, single-step, position-invariant transforms.

FLAS replaces a fixed one-step intervention with a learned, time-conditioned velocity field that adapts as the activation evolves and, when integrated over multiple steps, can follow curved trajectories through activation space.

### Performance Results

FLAS is the first learned method to consistently outperform prompting on AxBench, reaching held-out harmonic means of 1.015 on Gemma-2-2B-IT and 1.113 on Gemma-2-9B-IT without per-concept tuning.

### Paper Details

The paper was posted on arXiv with ID 2605.05892 and was submitted on May 7, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d761566d-4e54-43ca-a560-bd925b4f46b2",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "86fec683-80eb-43ef-97b8-fbf6875bf19e",
  "toolUseResult": {
    "query": "FLAS \"flow-based activation steering\" Jin 2026 language model arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VyGo9rswYyWPaKBswgnDNq",
        "content": [
          {
            "title": "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention",
            "url": "https://arxiv.org/html/2605.05892"
          },
          {
            "title": "[2605.05892] Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention",
            "url": "https://arxiv.org/abs/2605.05892"
          },
          {
            "title": "[2308.10248] Activation Addition: Steering Language Models Without Optimization",
            "url": "https://ar5iv.labs.arxiv.org/html/2308.10248"
          },
          {
            "title": "Activation Addition: Steering Language Models Without Optimization",
            "url": "https://arxiv.org/pdf/2308.10248v3"
          },
          {
            "title": "[2308.10248] Steering Language Models With Activation Engineering",
            "url": "https://arxiv.org/abs/2308.10248"
          },
          {
            "title": "STEERING LANGUAGE MODELS WITH ACTIVATION EN- GINEERING Alexander Matt Turner",
            "url": "https://arxiv.org/pdf/2308.10248"
          },
          {
            "title": "Steering Language Models With Activation Engineering",
            "url": "https://arxiv.org/html/2308.10248v5"
          },
          {
            "title": "[2604.24693] Contextual Linear Activation Steering of Language Models",
            "url": "https://arxiv.org/abs/2604.24693"
          },
          {
            "title": "GitHub - ZFancy/awesome-activation-engineering: A curated list of resources for activation engineering · GitHub",
            "url": "https://github.com/ZFancy/awesome-activation-engineering"
          },
          {
            "title": "The Rogue Scalpel: Activation Steering Compromises LLM Safety",
            "url": "https://arxiv.org/html/2509.22067v2"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\n## FLAS: Flow-based Activation Steering\n\nFLAS (Flow-based Activation Steering) learns a general, concept-conditioned velocity field for controlling language model behavior. The paper is by Zehao Jin and colleagues at Georgia Institute of Technology.\n\n### Key Contributions\n\nActivation steering has emerged as a promising alternative for controlling language-model behavior at inference time by modifying intermediate representations while keeping model parameters frozen, but existing steering methods typically restrict steering interventions to fixed, single-step, position-invariant transforms.\n\nFLAS replaces a fixed one-step intervention with a learned, time-conditioned velocity field that adapts as the activation evolves and, when integrated over multiple steps, can follow curved trajectories through activation space.\n\n### Performance Results\n\nFLAS is the first learned method to consistently outperform prompting on AxBench, reaching held-out harmonic means of 1.015 on Gemma-2-2B-IT and 1.113 on Gemma-2-9B-IT without per-concept tuning.\n\n### Paper Details\n\nThe paper was posted on arXiv with ID 2605.05892 and was submitted on May 7, 2026."
    ],
    "durationSeconds": 8.983303699000004
  },
  "sourceToolAssistantUUID": "d761566d-4e54-43ca-a560-bd925b4f46b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-15 (UTC).**  ## Original idea {   \"title\": \"Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Lo…",
  "leafUuid": "86fec683-80eb-43ef-97b8-fbf6875bf19e",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Claim-level confidence calibration in long-form generation via steering",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

### Tool call

_source line 23 · 2026-05-15T14:25:43.306Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016wLufH3vHhTNxVjntXk7jB`</summary>

```json
{
  "query": "Spherical Steering You 2026 rotation confidence gating activation steering arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86fec683-80eb-43ef-97b8-fbf6875bf19e",
  "isSidechain": false,
  "requestId": "req_011Cb4WTZGa6ociLKmrLn9hq",
  "type": "assistant",
  "uuid": "5a787970-43f9-4791-b3c1-df38499ac79f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mWeoiEdLXBDDJGGTGvdFy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 30825,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 825,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 30825,
          "cache_creation_input_tokens": 825,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 825
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

_source line 24 · 2026-05-15T14:25:54.012Z_

<details><summary>↩ Tool result · `toolu_016wLufH3vHhTNxVjntXk7jB`</summary>

```text
Web search results for query: "Spherical Steering You 2026 rotation confidence gating activation steering arXiv"

Links: [{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/html/2602.08169v1"},{"title":"[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/abs/2602.08169"},{"title":"GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub","url":"https://github.com/chili-lab/Spherical-Steering"},{"title":"(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"},{"title":"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/html/2605.05892"},{"title":"Publications","url":"https://hanjiechen.github.io/publication.html"},{"title":"Angular Steering: Behavior Control via Rotation in Activation Space","url":"https://arxiv.org/html/2510.26243v1"},{"title":"[2510.26243] Angular Steering: Behavior Control via Rotation in Activation Space","url":"https://arxiv.org/abs/2510.26243"},{"title":"Spherical Steering is highly complementary to few-shot prompting.... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Spherical-Steering-is-highly-complementary-to-few-shot-prompting-Performance-on_fig3_400605038"},{"title":"Adaptive Rotary Steering with Joint Autoregression for Robust Extraction of Closely Moving Speakers in Dynamic Scenarios","url":"https://arxiv.org/html/2601.12345v1"}]

I found the research paper you're looking for! Here are the key findings about "Spherical Steering: Geometry-Aware Activation Rotation for Language Models":

## Overview

Spherical Steering is an inference-time activation steering method for controlling language models via geometry-consistent interventions. Instead of the standard activation addition, Spherical Steering performs a rotation: it treats steering as a directional update in representation space and rotates hidden activations along a geodesic toward a target direction, while keeping activation magnitudes intact.

## Key Technical Features

The method rotates directly in the original space via hyperspherical geodesics with norm preservation without relying on a low-dimensional projection or PCA assumptions, and uses confidence gating for input-adaptive intervention strength.

A von Mises-Fisher (vMF)-based confidence gate is used to set an input-adaptive steering strength.

## Core Mechanism

Spherical Steering extracts a contrastive truthfulness signal from positive/negative examples and interprets the resulting prototype as defining a truthfulness axis in representation space. Viewing normalized hidden states as directions on the unit hypersphere, the approach steers by rotating the current activation along a geodesic toward the truthful direction (and away from its antipodal hallucinated direction), rather than injecting a fixed additive offset.

## Performance Results

Extensive experiments across multiple-choice benchmarks demonstrate that Spherical Steering significantly outperforms addition-based baselines (notably by +10% on TruthfulQA, COPA, and Storycloze), while simultaneously maintaining the model's general open-ended generation quality.

The paper was authored by Zejia You, Chunyuan Deng, and Hanjie Chen and is available on arXiv as 2602.08169.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a787970-43f9-4791-b3c1-df38499ac79f",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "f7c91322-0e87-4822-bc24-d6ea56cd80d1",
  "toolUseResult": {
    "query": "Spherical Steering You 2026 rotation confidence gating activation steering arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_016qr22C3zntTwwKALeVqUQJ",
        "content": [
          {
            "title": "Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://arxiv.org/html/2602.08169v1"
          },
          {
            "title": "[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://arxiv.org/abs/2602.08169"
          },
          {
            "title": "GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub",
            "url": "https://github.com/chili-lab/Spherical-Steering"
          },
          {
            "title": "(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"
          },
          {
            "title": "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention",
            "url": "https://arxiv.org/html/2605.05892"
          },
          {
            "title": "Publications",
            "url": "https://hanjiechen.github.io/publication.html"
          },
          {
            "title": "Angular Steering: Behavior Control via Rotation in Activation Space",
            "url": "https://arxiv.org/html/2510.26243v1"
          },
          {
            "title": "[2510.26243] Angular Steering: Behavior Control via Rotation in Activation Space",
            "url": "https://arxiv.org/abs/2510.26243"
          },
          {
            "title": "Spherical Steering is highly complementary to few-shot prompting.... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Spherical-Steering-is-highly-complementary-to-few-shot-prompting-Performance-on_fig3_400605038"
          },
          {
            "title": "Adaptive Rotary Steering with Joint Autoregression for Robust Extraction of Closely Moving Speakers in Dynamic Scenarios",
            "url": "https://arxiv.org/html/2601.12345v1"
          }
        ]
      },
      "I found the research paper you're looking for! Here are the key findings about \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models\":\n\n## Overview\n\nSpherical Steering is an inference-time activation steering method for controlling language models via geometry-consistent interventions. Instead of the standard activation addition, Spherical Steering performs a rotation: it treats steering as a directional update in representation space and rotates hidden activations along a geodesic toward a target direction, while keeping activation magnitudes intact.\n\n## Key Technical Features\n\nThe method rotates directly in the original space via hyperspherical geodesics with norm preservation without relying on a low-dimensional projection or PCA assumptions, and uses confidence gating for input-adaptive intervention strength.\n\nA von Mises-Fisher (vMF)-based confidence gate is used to set an input-adaptive steering strength.\n\n## Core Mechanism\n\nSpherical Steering extracts a contrastive truthfulness signal from positive/negative examples and interprets the resulting prototype as defining a truthfulness axis in representation space. Viewing normalized hidden states as directions on the unit hypersphere, the approach steers by rotating the current activation along a geodesic toward the truthful direction (and away from its antipodal hallucinated direction), rather than injecting a fixed additive offset.\n\n## Performance Results\n\nExtensive experiments across multiple-choice benchmarks demonstrate that Spherical Steering significantly outperforms addition-based baselines (notably by +10% on TruthfulQA, COPA, and Storycloze), while simultaneously maintaining the model's general open-ended generation quality.\n\nThe paper was authored by Zejia You, Chunyuan Deng, and Hanjie Chen and is available on arXiv as 2602.08169."
    ],
    "durationSeconds": 10.702161660000005
  },
  "sourceToolAssistantUUID": "5a787970-43f9-4791-b3c1-df38499ac79f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T14:25:56.962Z_

Now let me fetch the actual papers for deeper reading.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7c91322-0e87-4822-bc24-d6ea56cd80d1",
  "isSidechain": false,
  "requestId": "req_011Cb4WUcFRzrSf2t7LyeoRY",
  "type": "assistant",
  "uuid": "663d0776-4987-4ab4-a7be-26f431e4a9ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DaUWa54QucjPgKZVN6K21",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1019,
      "cache_read_input_tokens": 31650,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1019,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 31650,
          "cache_creation_input_tokens": 1019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1019
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

_source line 26 · 2026-05-15T14:25:58.913Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LfW91uozLjCgiYCmB3Z2S4`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.23221",
  "prompt": "Extract the full abstract, key method details, models used, results (numbers), and limitations. What exactly does the probe→steer pipeline look like? Is this self-probing or external observer? What scale models? What benchmarks?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "663d0776-4987-4ab4-a7be-26f431e4a9ba",
  "isSidechain": false,
  "requestId": "req_011Cb4WUcFRzrSf2t7LyeoRY",
  "type": "assistant",
  "uuid": "8b0230ee-5b46-4f63-bd43-c2af17a393f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DaUWa54QucjPgKZVN6K21",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1019,
      "cache_read_input_tokens": 31650,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1019,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 31650,
          "cache_creation_input_tokens": 1019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1019
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

_source line 27 · 2026-05-15T14:26:05.356Z_

<details><summary>↩ Tool result · `toolu_01LfW91uozLjCgiYCmB3Z2S4`</summary>

```text
# Paper Summary: "A Single Direction of Truth"

## Full Abstract
"Contextual hallucinations -- statements unsupported by given context -- remain a significant challenge in AI. We demonstrate a practical interpretability insight: a generator-agnostic observer model detects hallucinations via a single forward pass and a linear probe on its residual stream. This probe isolates a single, transferable linear direction separating hallucinated from faithful text, outperforming baselines by 5-27 points and showing robust mid-layer performance across Gemma-2 models (2B to 27B). Gradient-times-activation localises this signal to sparse, late-layer MLP activity. Critically, manipulating this direction causally steers generator hallucination rates, proving its actionability."

## Key Method Details
The approach uses an **external observer model** architecture—not self-probing. A separate model detects hallucinations through:
1. Single forward pass on residual stream
2. Linear probe isolating one separable direction
3. Gradient-times-activation analysis to localize signals to late-layer MLP sub-circuits

## Probe→Steer Pipeline
- **Detection**: Linear probe identifies hallucination direction in residual activations
- **Localization**: Gradient-times-activation pinpoints sparse MLP activity responsible
- **Steering**: Direct manipulation of this direction causally reduces generator hallucination rates

## Models Tested
Gemma-2 family: 2B, 7B, and 27B parameter sizes

## Results
- Outperforms baselines by 5-27 percentage points
- Robust mid-layer performance across model scales
- Causal steering demonstrates actionability

## Benchmark
ContraTales: 2,000-example benchmark for contextual hallucination assessment

## Notable Limitation
Paper emphasizes internal low-dimensional structure but doesn't detail generalization beyond Gemma-2 or other architectures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b0230ee-5b46-4f63-bd43-c2af17a393f3",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "d3595e10-1824-4f2c-a15c-2738f5e39fcd",
  "toolUseResult": {
    "bytes": 46658,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: \"A Single Direction of Truth\"\n\n## Full Abstract\n\"Contextual hallucinations -- statements unsupported by given context -- remain a significant challenge in AI. We demonstrate a practical interpretability insight: a generator-agnostic observer model detects hallucinations via a single forward pass and a linear probe on its residual stream. This probe isolates a single, transferable linear direction separating hallucinated from faithful text, outperforming baselines by 5-27 points and showing robust mid-layer performance across Gemma-2 models (2B to 27B). Gradient-times-activation localises this signal to sparse, late-layer MLP activity. Critically, manipulating this direction causally steers generator hallucination rates, proving its actionability.\"\n\n## Key Method Details\nThe approach uses an **external observer model** architecture—not self-probing. A separate model detects hallucinations through:\n1. Single forward pass on residual stream\n2. Linear probe isolating one separable direction\n3. Gradient-times-activation analysis to localize signals to late-layer MLP sub-circuits\n\n## Probe→Steer Pipeline\n- **Detection**: Linear probe identifies hallucination direction in residual activations\n- **Localization**: Gradient-times-activation pinpoints sparse MLP activity responsible\n- **Steering**: Direct manipulation of this direction causally reduces generator hallucination rates\n\n## Models Tested\nGemma-2 family: 2B, 7B, and 27B parameter sizes\n\n## Results\n- Outperforms baselines by 5-27 percentage points\n- Robust mid-layer performance across model scales\n- Causal steering demonstrates actionability\n\n## Benchmark\nContraTales: 2,000-example benchmark for contextual hallucination assessment\n\n## Notable Limitation\nPaper emphasizes internal low-dimensional structure but doesn't detail generalization beyond Gemma-2 or other architectures.",
    "durationMs": 6439,
    "url": "https://arxiv.org/abs/2507.23221"
  },
  "sourceToolAssistantUUID": "8b0230ee-5b46-4f63-bd43-c2af17a393f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28 · 2026-05-15T14:26:05.363Z_

```json
{
  "parentUuid": "d3595e10-1824-4f2c-a15c-2738f5e39fcd",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a56d04fe-47db-46e8-9609-cf6f218bda44",
  "timestamp": "2026-05-15T14:26:05.363Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 29 · 2026-05-15T14:26:08.762Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MtUoKCux3KdRH7uDwN53zZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2409.05907",
  "prompt": "Extract the full abstract, key method details for CAST (Conditional Activation Steering). How does the condition vector work? What determines when steering is applied vs withheld? What models and benchmarks? How is this different from probe-guided steering?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a56d04fe-47db-46e8-9609-cf6f218bda44",
  "isSidechain": false,
  "requestId": "req_011Cb4WVSjirkLECMUUqW3iY",
  "type": "assistant",
  "uuid": "bc244770-8f43-462f-8f35-2538e9c74b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HpcxxA5MCqrXKDbNxCZ4QH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 695,
      "cache_read_input_tokens": 32669,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 695,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 32669,
          "cache_creation_input_tokens": 695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 695
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

_source line 30 · 2026-05-15T14:26:13.745Z_

<details><summary>↩ Tool result · `toolu_01MtUoKCux3KdRH7uDwN53zZ`</summary>

```text
# Conditional Activation Steering (CAST) Overview

## Full Abstract
"LLMs have shown remarkable capabilities, but precisely controlling their response behavior remains challenging. Existing activation steering methods alter LLM behavior indiscriminately, limiting their practical applicability in settings where selective responses are essential, such as content moderation or domain-specific assistants."

The method enables selective refusal through rules like: "if input is about hate speech or adult content, then refuse" or "if input is not about legal advice, then refuse."

## Key Method Details

The webpage indicates CAST works by examining "LLM activation patterns during inference to selectively apply or withhold activation steering based on the input context." The core mechanism relies on the insight that "different categories of prompts activate distinct patterns in the model's hidden states."

## Condition Vector Mechanism

Unfortunately, the webpage does not provide specific technical details about how the condition vector operates, the precise mechanisms determining when steering activates versus remains withheld, or the mathematical formulation.

## Models and Benchmarks

The abstract and page content do not specify which models were evaluated, benchmark datasets, or experimental results.

## Differentiation from Probe-Guided Steering

The webpage does not discuss probe-guided steering or comparative differences from other steering approaches.

## Notable Feature

The framework operates "without requiring weight optimization" and includes an "open-source implementation."

For comprehensive technical details, consulting the full paper would be necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc244770-8f43-462f-8f35-2538e9c74b47",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "fc38f3f0-5a50-4d74-a826-93c9417710bc",
  "toolUseResult": {
    "bytes": 47694,
    "code": 200,
    "codeText": "OK",
    "result": "# Conditional Activation Steering (CAST) Overview\n\n## Full Abstract\n\"LLMs have shown remarkable capabilities, but precisely controlling their response behavior remains challenging. Existing activation steering methods alter LLM behavior indiscriminately, limiting their practical applicability in settings where selective responses are essential, such as content moderation or domain-specific assistants.\"\n\nThe method enables selective refusal through rules like: \"if input is about hate speech or adult content, then refuse\" or \"if input is not about legal advice, then refuse.\"\n\n## Key Method Details\n\nThe webpage indicates CAST works by examining \"LLM activation patterns during inference to selectively apply or withhold activation steering based on the input context.\" The core mechanism relies on the insight that \"different categories of prompts activate distinct patterns in the model's hidden states.\"\n\n## Condition Vector Mechanism\n\nUnfortunately, the webpage does not provide specific technical details about how the condition vector operates, the precise mechanisms determining when steering activates versus remains withheld, or the mathematical formulation.\n\n## Models and Benchmarks\n\nThe abstract and page content do not specify which models were evaluated, benchmark datasets, or experimental results.\n\n## Differentiation from Probe-Guided Steering\n\nThe webpage does not discuss probe-guided steering or comparative differences from other steering approaches.\n\n## Notable Feature\n\nThe framework operates \"without requiring weight optimization\" and includes an \"open-source implementation.\"\n\nFor comprehensive technical details, consulting the full paper would be necessary.",
    "durationMs": 4980,
    "url": "https://arxiv.org/abs/2409.05907"
  },
  "sourceToolAssistantUUID": "bc244770-8f43-462f-8f35-2538e9c74b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T14:26:17.549Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DU4qUNsBkMBYJpxk4AmpGE`</summary>

```json
{
  "url": "https://arxiv.org/html/2409.05907v3",
  "prompt": "Extract the technical details of CAST: How does the condition vector work mathematically? What is the formula for deciding when to apply steering? How is the condition vector computed? What models were tested (sizes)? Key results numbers?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc38f3f0-5a50-4d74-a826-93c9417710bc",
  "isSidechain": false,
  "requestId": "req_011Cb4WW4cj8rPpKPQYnE65N",
  "type": "assistant",
  "uuid": "0e12d298-98f1-4723-8577-b4a106624171",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNQGpvuwNaHATLX2dZE3j8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 460,
      "cache_read_input_tokens": 33364,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 460,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 33364,
          "cache_creation_input_tokens": 460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 460
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

_source line 32 · 2026-05-15T14:26:25.700Z_

<details><summary>↩ Tool result · `toolu_01DU4qUNsBkMBYJpxk4AmpGE`</summary>

```text
# Conditional Activation Steering (CAST) Technical Details

## Mathematical Formulation

The core steering equation is:

**h' ← h + f(sim(h, proj_c h)) · α · v**

Where:
- **h** = hidden state at a layer
- **c** = condition vector
- **v** = behavior vector
- **α** = scaling factor
- **proj_c h** = projection of h onto c, computed as: (c⊗c / c·c) · h

The projection formula decomposes the hidden state along the condition vector's direction.

## Condition Checking Function

The thresholding function determines activation:

"f(sim(h, proj_c h)) = 1 if sim(h, proj_c h) > θ, else 0"

Here, sim uses cosine similarity: **sim(h,g) = h·g / (|h||g|)**

In practice, a nonlinear variant applies: sim(h, tanh(proj_c h)) for more predictable behavior.

The three key hyperparameters are: optimal layer, threshold value θ, and comparison direction (> or <).

## Condition Vector Computation

Both condition and behavior vectors undergo identical extraction via PCA:

**vector_l = PCA(H_l+ - μ_l, H_l- - μ_l)**

Where μ_l = (H_l+ + H_l-) / 2 (mean-centered activation)

The critical distinction: "for behavior vectors, we take the average hidden states for suffixes of each example. For condition vectors, we take the average hidden states for all tokens of each example."

## Models Tested

**Sizes evaluated:**
- Qwen 1.5 Chat: 1.8B, 32B
- Llama 2 Chat: 13B
- Llama 3.1 Inst: 8B
- NeuralDaredevil: 8B
- Hermes 2 Pro: 8B
- OLMo SFT: 7B
- Zephyr Beta: 7B
- Danube 3 Chat: 4B

## Key Results

On harmful vs. harmless test sets (500 harmless, 450 harmful prompts):

| Model | Harmful Refusal | Harmless Refusal |
|-------|-----------------|------------------|
| Qwen 1.5 1.8B | 90.67% | 2.20% |
| Hermes 2 Pro | 83.33% | 2.40% |
| OLMo SFT | 86.22% | 6.00% |

"Across all seven tested models...conditioning a behavior vector on condition vector selectively increases refusal rates for harmful content while leaving harmless prompt refusal rates largely unchanged."

Standard activation steering (without conditioning) increased refusal indiscriminately—reaching ~96% refusal on harmless prompts versus CAST's ~2%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e12d298-98f1-4723-8577-b4a106624171",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "56aff898-6549-449f-9743-90724edbe397",
  "toolUseResult": {
    "bytes": 554833,
    "code": 200,
    "codeText": "OK",
    "result": "# Conditional Activation Steering (CAST) Technical Details\n\n## Mathematical Formulation\n\nThe core steering equation is:\n\n**h' ← h + f(sim(h, proj_c h)) · α · v**\n\nWhere:\n- **h** = hidden state at a layer\n- **c** = condition vector\n- **v** = behavior vector\n- **α** = scaling factor\n- **proj_c h** = projection of h onto c, computed as: (c⊗c / c·c) · h\n\nThe projection formula decomposes the hidden state along the condition vector's direction.\n\n## Condition Checking Function\n\nThe thresholding function determines activation:\n\n\"f(sim(h, proj_c h)) = 1 if sim(h, proj_c h) > θ, else 0\"\n\nHere, sim uses cosine similarity: **sim(h,g) = h·g / (|h||g|)**\n\nIn practice, a nonlinear variant applies: sim(h, tanh(proj_c h)) for more predictable behavior.\n\nThe three key hyperparameters are: optimal layer, threshold value θ, and comparison direction (> or <).\n\n## Condition Vector Computation\n\nBoth condition and behavior vectors undergo identical extraction via PCA:\n\n**vector_l = PCA(H_l+ - μ_l, H_l- - μ_l)**\n\nWhere μ_l = (H_l+ + H_l-) / 2 (mean-centered activation)\n\nThe critical distinction: \"for behavior vectors, we take the average hidden states for suffixes of each example. For condition vectors, we take the average hidden states for all tokens of each example.\"\n\n## Models Tested\n\n**Sizes evaluated:**\n- Qwen 1.5 Chat: 1.8B, 32B\n- Llama 2 Chat: 13B\n- Llama 3.1 Inst: 8B\n- NeuralDaredevil: 8B\n- Hermes 2 Pro: 8B\n- OLMo SFT: 7B\n- Zephyr Beta: 7B\n- Danube 3 Chat: 4B\n\n## Key Results\n\nOn harmful vs. harmless test sets (500 harmless, 450 harmful prompts):\n\n| Model | Harmful Refusal | Harmless Refusal |\n|-------|-----------------|------------------|\n| Qwen 1.5 1.8B | 90.67% | 2.20% |\n| Hermes 2 Pro | 83.33% | 2.40% |\n| OLMo SFT | 86.22% | 6.00% |\n\n\"Across all seven tested models...conditioning a behavior vector on condition vector selectively increases refusal rates for harmful content while leaving harmless prompt refusal rates largely unchanged.\"\n\nStandard activation steering (without conditioning) increased refusal indiscriminately—reaching ~96% refusal on harmless prompts versus CAST's ~2%.",
    "durationMs": 8149,
    "url": "https://arxiv.org/html/2409.05907v3"
  },
  "sourceToolAssistantUUID": "0e12d298-98f1-4723-8577-b4a106624171",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T14:26:29.910Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WnD4souSf9iV95t5GReZGy`</summary>

```json
{
  "url": "https://www.researchgate.net/publication/393657638_Fact-Level_Calibration_and_Correction_for_Long-Form_Generations",
  "prompt": "Extract the full abstract, method details, and key results for the CARE paper on fact-level calibration and correction for long-form generations. What is the specific mechanism? How does the iterative correction work? What models and benchmarks? Key numbers?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56aff898-6549-449f-9743-90724edbe397",
  "isSidechain": false,
  "requestId": "req_011Cb4WWwnjmboEKyJiQS9ZX",
  "type": "assistant",
  "uuid": "cc338bb1-2722-4dda-a39d-0bf066781585",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TAGDDsrCYQ2gGhp4txtZ9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 846,
      "cache_read_input_tokens": 33824,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 846,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 33824,
          "cache_creation_input_tokens": 846,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 846
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

_source line 34 · 2026-05-15T14:26:30.142Z_

<details><summary>↩ Tool result · reported error · `toolu_01WnD4souSf9iV95t5GReZGy`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc338bb1-2722-4dda-a39d-0bf066781585",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "d803e3eb-37ac-47a2-ba55-150301ea87ce",
  "toolUseResult": "Error: Request failed with status code 403",
  "sourceToolAssistantUUID": "cc338bb1-2722-4dda-a39d-0bf066781585",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T14:26:32.822Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0128R5aVB4CNUcsaEJq1CEPW`</summary>

```json
{
  "query": "CARE \"fact-level calibration and correction\" long-form generation arXiv Yuan Xu Tan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d803e3eb-37ac-47a2-ba55-150301ea87ce",
  "isSidechain": false,
  "requestId": "req_011Cb4WXGi2Wz2ceyVsRVggV",
  "type": "assistant",
  "uuid": "0d477e0e-2ada-44df-917d-b7985566459e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gAaBvqrdDweKbBm4coB8r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 186,
      "cache_read_input_tokens": 34670,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 186,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 34670,
          "cache_creation_input_tokens": 186,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 186
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

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-15 (UTC).**  ## Original idea {   \"title\": \"Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Lo…",
  "leafUuid": "0d477e0e-2ada-44df-917d-b7985566459e",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Claim-level confidence calibration in long-form generation via steering",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

### Tool result

_source line 38 · 2026-05-15T14:26:38.493Z_

<details><summary>↩ Tool result · `toolu_0128R5aVB4CNUcsaEJq1CEPW`</summary>

```text
Web search results for query: "CARE "fact-level calibration and correction" long-form generation arXiv Yuan Xu Tan"

Links: [{"title":"Fact-Level Calibration and Correction for Long-Form Generations | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3726302.3730195"},{"title":"Fact-Level Calibration and Correction for Long-Form Generations | Request PDF","url":"https://www.researchgate.net/publication/393657638_Fact-Level_Calibration_and_Correction_for_Long-Form_Generations"},{"title":"Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality","url":"https://arxiv.org/html/2605.01749"},{"title":"[2411.13343] Fact-Level Confidence Calibration and Self-Correction","url":"https://arxiv.org/abs/2411.13343"},{"title":"Atomic Calibration of LLMs in Long-Form Generations","url":"https://arxiv.org/html/2410.13246v1"},{"title":"[2402.06544] Calibrating Long-form Generations from Large Language Models","url":"https://arxiv.org/abs/2402.06544"},{"title":"[2605.01749] Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality","url":"https://arxiv.org/abs/2605.01749"},{"title":"Computer Vision and Pattern Recognition Jun 2025","url":"https://www.arxiv.org/list/cs.CV/2025-06?skip=800&show=2000"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/html/2511.00280v1"},{"title":"Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey","url":"https://arxiv.org/html/2503.15850v1"}]

Based on the search results, I found relevant information about the paper you're looking for:

On July 13, 2025, Yige Yuan and others published "Fact-Level Calibration and Correction for Long-Form Generations". 

The paper appears in search results on both ResearchGate and in the ACM SIGIR proceedings. The work introduces CARE (Confidence-Aware Fact Correction), a method that leverages high-confidence facts to iteratively refine and correct low-confidence ones.

The paper addresses an important challenge in long-form text generation: current calibration methods for LLMs typically estimate two scalars to represent overall response confidence and correctness, which is inadequate for long-form generation where the response includes multiple atomic facts and may be partially confident and correct. The authors propose a Fact-Level Calibration framework that operates at a finer granularity, calibrating confidence to relevance-weighted correctness at the fact level.

The paper has been published in the Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d477e0e-2ada-44df-917d-b7985566459e",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "bd39c554-a31b-4270-bc6b-63958f22d0d5",
  "toolUseResult": {
    "query": "CARE \"fact-level calibration and correction\" long-form generation arXiv Yuan Xu Tan",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CNE3Cuj6YKVjkeMxFQCkcZ",
        "content": [
          {
            "title": "Fact-Level Calibration and Correction for Long-Form Generations | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval",
            "url": "https://dl.acm.org/doi/10.1145/3726302.3730195"
          },
          {
            "title": "Fact-Level Calibration and Correction for Long-Form Generations | Request PDF",
            "url": "https://www.researchgate.net/publication/393657638_Fact-Level_Calibration_and_Correction_for_Long-Form_Generations"
          },
          {
            "title": "Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality",
            "url": "https://arxiv.org/html/2605.01749"
          },
          {
            "title": "[2411.13343] Fact-Level Confidence Calibration and Self-Correction",
            "url": "https://arxiv.org/abs/2411.13343"
          },
          {
            "title": "Atomic Calibration of LLMs in Long-Form Generations",
            "url": "https://arxiv.org/html/2410.13246v1"
          },
          {
            "title": "[2402.06544] Calibrating Long-form Generations from Large Language Models",
            "url": "https://arxiv.org/abs/2402.06544"
          },
          {
            "title": "[2605.01749] Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality",
            "url": "https://arxiv.org/abs/2605.01749"
          },
          {
            "title": "Computer Vision and Pattern Recognition Jun 2025",
            "url": "https://www.arxiv.org/list/cs.CV/2025-06?skip=800&show=2000"
          },
          {
            "title": "Calibration Across Layers: Understanding Calibration Evolution in LLMs",
            "url": "https://arxiv.org/html/2511.00280v1"
          },
          {
            "title": "Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey",
            "url": "https://arxiv.org/html/2503.15850v1"
          }
        ]
      },
      "Based on the search results, I found relevant information about the paper you're looking for:\n\nOn July 13, 2025, Yige Yuan and others published \"Fact-Level Calibration and Correction for Long-Form Generations\". \n\nThe paper appears in search results on both ResearchGate and in the ACM SIGIR proceedings. The work introduces CARE (Confidence-Aware Fact Correction), a method that leverages high-confidence facts to iteratively refine and correct low-confidence ones.\n\nThe paper addresses an important challenge in long-form text generation: current calibration methods for LLMs typically estimate two scalars to represent overall response confidence and correctness, which is inadequate for long-form generation where the response includes multiple atomic facts and may be partially confident and correct. The authors propose a Fact-Level Calibration framework that operates at a finer granularity, calibrating confidence to relevance-weighted correctness at the fact level.\n\nThe paper has been published in the Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval."
    ],
    "durationSeconds": 5.6669686419999925
  },
  "sourceToolAssistantUUID": "0d477e0e-2ada-44df-917d-b7985566459e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T14:26:41.566Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013DsvZNdnWiNcXcYD3SZAqr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.13343",
  "prompt": "Extract the full abstract, method overview, models tested, and key results for this paper on Fact-Level Confidence Calibration and Self-Correction. Is this the CARE paper? What is the full title and authors?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd39c554-a31b-4270-bc6b-63958f22d0d5",
  "isSidechain": false,
  "requestId": "req_011Cb4WXtS6oDRPtCsvQzJpZ",
  "type": "assistant",
  "uuid": "ba6acc0e-124e-4488-9fc3-b0f07e5c782d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZJNYq6fDh79cn4e5LCdbp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 34856,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 34856,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 855
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

_source line 40 · 2026-05-15T14:26:48.867Z_

<details><summary>↩ Tool result · `toolu_013DsvZNdnWiNcXcYD3SZAqr`</summary>

```text
# Fact-Level Confidence Calibration and Self-Correction

## Full Title and Authors
**Title:** "Fact-Level Confidence Calibration and Self-Correction"

**Authors:** Yige Yuan, Bingbing Xu, Hexiang Tan, Fei Sun, Teng Xiao, Wei Li, Huawei Shen, Xueqi Cheng

## Is This the CARE Paper?
No, this is not the CARE paper. This paper introduces **ConFix** (Confidence-Guided Fact-level Self-Correction), a distinct method.

## Abstract
The researchers address a limitation in current LLM confidence calibration approaches. Rather than assigning single confidence scores to entire responses, they propose operating at finer granularity. Their framework calibrates "confidence to relevance-weighted correctness at the fact level" for multi-fact responses. The analysis led to ConFix, which leverages "high-confidence facts within a response as additional knowledge to improve low-confidence ones."

## Method Overview
The approach involves two components:
1. A Fact-Level Calibration framework that evaluates individual facts against relevance-weighted correctness
2. ConFix, which uses high-confidence facts as internal knowledge to enhance lower-confidence statements

## Models and Datasets Tested
The paper reports testing across:
- **Four datasets** (specific names not listed in this abstract)
- **Six models** (specific models not identified in provided content)

## Key Results
ConFix "effectively mitigates hallucinations without requiring external knowledge sources such as retrieval systems."

Code is available on GitHub.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba6acc0e-124e-4488-9fc3-b0f07e5c782d",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "f7a31f43-9625-4980-b7ac-5a10139e9049",
  "toolUseResult": {
    "bytes": 46358,
    "code": 200,
    "codeText": "OK",
    "result": "# Fact-Level Confidence Calibration and Self-Correction\n\n## Full Title and Authors\n**Title:** \"Fact-Level Confidence Calibration and Self-Correction\"\n\n**Authors:** Yige Yuan, Bingbing Xu, Hexiang Tan, Fei Sun, Teng Xiao, Wei Li, Huawei Shen, Xueqi Cheng\n\n## Is This the CARE Paper?\nNo, this is not the CARE paper. This paper introduces **ConFix** (Confidence-Guided Fact-level Self-Correction), a distinct method.\n\n## Abstract\nThe researchers address a limitation in current LLM confidence calibration approaches. Rather than assigning single confidence scores to entire responses, they propose operating at finer granularity. Their framework calibrates \"confidence to relevance-weighted correctness at the fact level\" for multi-fact responses. The analysis led to ConFix, which leverages \"high-confidence facts within a response as additional knowledge to improve low-confidence ones.\"\n\n## Method Overview\nThe approach involves two components:\n1. A Fact-Level Calibration framework that evaluates individual facts against relevance-weighted correctness\n2. ConFix, which uses high-confidence facts as internal knowledge to enhance lower-confidence statements\n\n## Models and Datasets Tested\nThe paper reports testing across:\n- **Four datasets** (specific names not listed in this abstract)\n- **Six models** (specific models not identified in provided content)\n\n## Key Results\nConFix \"effectively mitigates hallucinations without requiring external knowledge sources such as retrieval systems.\"\n\nCode is available on GitHub.",
    "durationMs": 7297,
    "url": "https://arxiv.org/abs/2411.13343"
  },
  "sourceToolAssistantUUID": "ba6acc0e-124e-4488-9fc3-b0f07e5c782d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T14:26:52.443Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019vePUzAwp9euDCPcYDEHUg`</summary>

```json
{
  "url": "https://dl.acm.org/doi/10.1145/3726302.3730195",
  "prompt": "Extract the full abstract, method details, key results, and any mention of CARE framework from this SIGIR 2025 paper on Fact-Level Calibration and Correction for Long-Form Generations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7a31f43-9625-4980-b7ac-5a10139e9049",
  "isSidechain": false,
  "requestId": "req_011Cb4WYeyW6F4GVNwwZ8hkZ",
  "type": "assistant",
  "uuid": "2dbeb7ab-4bb6-4a64-8030-19529cfe9aff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rU21qkHd7JZFWce5nhVk7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 35711,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 35711,
          "cache_creation_input_tokens": 509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 509
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

_source line 42 · 2026-05-15T14:26:52.661Z_

<details><summary>↩ Tool result · reported error · `toolu_019vePUzAwp9euDCPcYDEHUg`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2dbeb7ab-4bb6-4a64-8030-19529cfe9aff",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "32754013-abda-4ad4-8f3b-bb8d5d9c1d2c",
  "toolUseResult": "Error: Request failed with status code 403",
  "sourceToolAssistantUUID": "2dbeb7ab-4bb6-4a64-8030-19529cfe9aff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T14:26:55.187Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R9Fysq6hfZYXyxmM6RXfDK`</summary>

```json
{
  "query": "\"Fact-Level Confidence Calibration and Self-Correction\" ConFix SIGIR 2025 arXiv 2411.13343"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32754013-abda-4ad4-8f3b-bb8d5d9c1d2c",
  "isSidechain": false,
  "requestId": "req_011Cb4WYvyBHVVPMeobxefHo",
  "type": "assistant",
  "uuid": "ef5edba9-0964-495c-893e-29ad7d2b3756",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZMvM53EbaJSFWx5WhqgM2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 163,
      "cache_read_input_tokens": 36220,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 36220,
          "cache_creation_input_tokens": 163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 163
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

_source line 44 · 2026-05-15T14:27:03.663Z_

<details><summary>↩ Tool result · `toolu_01R9Fysq6hfZYXyxmM6RXfDK`</summary>

```text
Web search results for query: ""Fact-Level Confidence Calibration and Self-Correction" ConFix SIGIR 2025 arXiv 2411.13343"

Links: [{"title":"[2411.13343] Fact-Level Confidence Calibration and Self-Correction","url":"https://arxiv.org/abs/2411.13343"},{"title":"Fact-Level Confidence Calibration and Self-Correction","url":"https://arxiv.org/html/2411.13343"},{"title":"Fact-Level Calibration and Correction for Long-Form Generations | Request PDF","url":"https://www.researchgate.net/publication/393657638_Fact-Level_Calibration_and_Correction_for_Long-Form_Generations"},{"title":"Fact-Level Calibration and Correction for Long-Form Generations | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3726302.3730195"},{"title":"Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in Large Language Models","url":"https://arxiv.org/html/2502.11028v3"},{"title":"\"C\"³: Confidence Calibration Model Cascade for Inference-Efficient Cross-Lingual Natural Language Understanding","url":"https://arxiv.org/html/2402.15991v1"},{"title":"[2303.02970] Rethinking Confidence Calibration for Failure Prediction","url":"https://arxiv.org/abs/2303.02970"},{"title":"Calibrated Interpretation: Confidence Estimation in Semantic Parsing | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00598/117737/Calibrated-Interpretation-Confidence-Estimation-in"},{"title":"Evaluating and Calibrating LLM Confidence on Questions with Multiple Correct Answers","url":"https://arxiv.org/html/2602.07842v1"},{"title":"Scaling Truth: The Confidence Paradox in AI Fact-Checking","url":"https://arxiv.org/html/2509.08803v1"}]

I found the paper you're looking for. Here are the key details about "Fact-Level Confidence Calibration and Self-Correction":

## Overview

This work addresses confidence calibration in LLMs, which involves aligning their self-assessed confidence with the actual accuracy of their responses, enabling them to self-evaluate the correctness of their outputs.

## The ConFix Method

ConFix is a self-correction method based on a fact-level calibration framework designed to enhance generation and reduce hallucinations without relying on external knowledge sources. 

The approach proposes a fact-level calibration framework that operates at a finer granularity, calibrating confidence to relevance-weighted correctness at the fact level. This is an improvement over existing methods because current calibration methods for LLMs typically estimate two scalars to represent overall response confidence and correctness, which is inadequate for long-form generation where the response includes multiple atomic facts and may be partially confident and correct, and these methods also overlook the relevance of each fact to the query.

## How it Works

ConFix first segments the response into multiple facts and evaluates their confidence vector, then uses the high-confidence facts and their associated confidence scores as additional knowledge to augment low-confidence facts, with the aim of all facts within the response achieving high confidence.

## Results

Experiments with ConFix across four datasets and six models reveal that it can significantly reduce the occurrence of hallucinations, thereby increasing the models' reliability and enabling their real-world applications.

The paper was published on arXiv on November 20, 2024 (arXiv:2411.13343) and has been accepted to SIGIR 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef5edba9-0964-495c-893e-29ad7d2b3756",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "3b99f407-5a95-4086-8218-2abaa6392277",
  "toolUseResult": {
    "query": "\"Fact-Level Confidence Calibration and Self-Correction\" ConFix SIGIR 2025 arXiv 2411.13343",
    "results": [
      {
        "tool_use_id": "srvtoolu_015PUR5BLRkEXpKSZzvwHifR",
        "content": [
          {
            "title": "[2411.13343] Fact-Level Confidence Calibration and Self-Correction",
            "url": "https://arxiv.org/abs/2411.13343"
          },
          {
            "title": "Fact-Level Confidence Calibration and Self-Correction",
            "url": "https://arxiv.org/html/2411.13343"
          },
          {
            "title": "Fact-Level Calibration and Correction for Long-Form Generations | Request PDF",
            "url": "https://www.researchgate.net/publication/393657638_Fact-Level_Calibration_and_Correction_for_Long-Form_Generations"
          },
          {
            "title": "Fact-Level Calibration and Correction for Long-Form Generations | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval",
            "url": "https://dl.acm.org/doi/10.1145/3726302.3730195"
          },
          {
            "title": "Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in Large Language Models",
            "url": "https://arxiv.org/html/2502.11028v3"
          },
          {
            "title": "\"C\"³: Confidence Calibration Model Cascade for Inference-Efficient Cross-Lingual Natural Language Understanding",
            "url": "https://arxiv.org/html/2402.15991v1"
          },
          {
            "title": "[2303.02970] Rethinking Confidence Calibration for Failure Prediction",
            "url": "https://arxiv.org/abs/2303.02970"
          },
          {
            "title": "Calibrated Interpretation: Confidence Estimation in Semantic Parsing | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00598/117737/Calibrated-Interpretation-Confidence-Estimation-in"
          },
          {
            "title": "Evaluating and Calibrating LLM Confidence on Questions with Multiple Correct Answers",
            "url": "https://arxiv.org/html/2602.07842v1"
          },
          {
            "title": "Scaling Truth: The Confidence Paradox in AI Fact-Checking",
            "url": "https://arxiv.org/html/2509.08803v1"
          }
        ]
      },
      "I found the paper you're looking for. Here are the key details about \"Fact-Level Confidence Calibration and Self-Correction\":\n\n## Overview\n\nThis work addresses confidence calibration in LLMs, which involves aligning their self-assessed confidence with the actual accuracy of their responses, enabling them to self-evaluate the correctness of their outputs.\n\n## The ConFix Method\n\nConFix is a self-correction method based on a fact-level calibration framework designed to enhance generation and reduce hallucinations without relying on external knowledge sources. \n\nThe approach proposes a fact-level calibration framework that operates at a finer granularity, calibrating confidence to relevance-weighted correctness at the fact level. This is an improvement over existing methods because current calibration methods for LLMs typically estimate two scalars to represent overall response confidence and correctness, which is inadequate for long-form generation where the response includes multiple atomic facts and may be partially confident and correct, and these methods also overlook the relevance of each fact to the query.\n\n## How it Works\n\nConFix first segments the response into multiple facts and evaluates their confidence vector, then uses the high-confidence facts and their associated confidence scores as additional knowledge to augment low-confidence facts, with the aim of all facts within the response achieving high confidence.\n\n## Results\n\nExperiments with ConFix across four datasets and six models reveal that it can significantly reduce the occurrence of hallucinations, thereby increasing the models' reliability and enabling their real-world applications.\n\nThe paper was published on arXiv on November 20, 2024 (arXiv:2411.13343) and has been accepted to SIGIR 2025."
    ],
    "durationSeconds": 8.472365216000005
  },
  "sourceToolAssistantUUID": "ef5edba9-0964-495c-893e-29ad7d2b3756",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T14:27:07.963Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FLdZPEbYpUvqAg2NYeecyX`</summary>

```json
{
  "url": "https://arxiv.org/html/2411.13343",
  "prompt": "Extract: 1) The exact name of the framework (is it called CARE or ConFix?), 2) The full technical method - how does fact-level calibration work exactly? 3) Models tested and their sizes, 4) Benchmarks used, 5) Key quantitative results (ECE numbers, accuracy improvements), 6) Does it require model training or is it inference-time only?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b99f407-5a95-4086-8218-2abaa6392277",
  "isSidechain": false,
  "requestId": "req_011Cb4WZk4sjZtGAusU8HyVV",
  "type": "assistant",
  "uuid": "ea101338-a9ff-4fca-99a6-3c4b8a284bb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KgzmLrkA7ATGqiASuHkdZE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1051,
      "cache_read_input_tokens": 36383,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1051,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 36383,
          "cache_creation_input_tokens": 1051,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1051
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

_source line 46 · 2026-05-15T14:27:14.394Z_

<details><summary>↩ Tool result · `toolu_01FLdZPEbYpUvqAg2NYeecyX`</summary>

```text
# Fact-Level Confidence Calibration Framework Analysis

## 1. Framework Name
The framework is called **ConFix** (Confidence-Guided Fact-Level Self-Correction). There is no mention of "CARE" in the document.

## 2. Technical Method
Fact-level calibration operates through four components:

- **Fact Extraction**: Breaking responses into atomic facts using GPT-4
- **Correctness & Relevance Evaluation**: Assessing each fact's accuracy and pertinence to queries using the SAFE pipeline
- **Confidence Estimation**: Computing confidence vectors (not scalars) using three methods—verbalization-based, logit-based (isTrueLogit), and consistency-based approaches
- **Calibration Metrics**: Measuring alignment between confidence and "relevance-weighted correctness" via Fact-Level Expected Calibration Error (F-ECE)

ConFix then uses high-confidence facts as references to revise low-confidence facts through factor extraction and iterative correction.

## 3. Models Tested
Five models across different scales:
- LLaMA-7b-chat and LLaMA-13b-chat
- Vicuna-7b and Vicuna-13b
- GPT-3.5-turbo

## 4. Benchmarks
Two primary datasets:
- **LongFact**: Assesses factuality in open-ended responses
- **ASQA**: Focuses on ambiguous factoid questions with multiple valid answers

## 5. Key Quantitative Results
From Table 1, fact-level calibration shows substantially higher variance across models. For example, GPT-3.5-turbo achieved F-ECE scores of 0.0856 (Verbalization) and 0.0715 (Consistency) on LongFact. Error correction (Table 3) demonstrated 46-53% improvement rates for most models.

## 6. Training Requirements
**Inference-time only**—no model retraining required. The framework operates through prompting during generation, making it computationally efficient and broadly applicable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea101338-a9ff-4fca-99a6-3c4b8a284bb3",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "6b4170d2-20ea-423d-82e1-99d85b39c520",
  "toolUseResult": {
    "bytes": 352343,
    "code": 200,
    "codeText": "OK",
    "result": "# Fact-Level Confidence Calibration Framework Analysis\n\n## 1. Framework Name\nThe framework is called **ConFix** (Confidence-Guided Fact-Level Self-Correction). There is no mention of \"CARE\" in the document.\n\n## 2. Technical Method\nFact-level calibration operates through four components:\n\n- **Fact Extraction**: Breaking responses into atomic facts using GPT-4\n- **Correctness & Relevance Evaluation**: Assessing each fact's accuracy and pertinence to queries using the SAFE pipeline\n- **Confidence Estimation**: Computing confidence vectors (not scalars) using three methods—verbalization-based, logit-based (isTrueLogit), and consistency-based approaches\n- **Calibration Metrics**: Measuring alignment between confidence and \"relevance-weighted correctness\" via Fact-Level Expected Calibration Error (F-ECE)\n\nConFix then uses high-confidence facts as references to revise low-confidence facts through factor extraction and iterative correction.\n\n## 3. Models Tested\nFive models across different scales:\n- LLaMA-7b-chat and LLaMA-13b-chat\n- Vicuna-7b and Vicuna-13b\n- GPT-3.5-turbo\n\n## 4. Benchmarks\nTwo primary datasets:\n- **LongFact**: Assesses factuality in open-ended responses\n- **ASQA**: Focuses on ambiguous factoid questions with multiple valid answers\n\n## 5. Key Quantitative Results\nFrom Table 1, fact-level calibration shows substantially higher variance across models. For example, GPT-3.5-turbo achieved F-ECE scores of 0.0856 (Verbalization) and 0.0715 (Consistency) on LongFact. Error correction (Table 3) demonstrated 46-53% improvement rates for most models.\n\n## 6. Training Requirements\n**Inference-time only**—no model retraining required. The framework operates through prompting during generation, making it computationally efficient and broadly applicable.",
    "durationMs": 6425,
    "url": "https://arxiv.org/html/2411.13343"
  },
  "sourceToolAssistantUUID": "ea101338-a9ff-4fca-99a6-3c4b8a284bb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T14:27:18.199Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FL94T2o3Te4N47CgKTHkVv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05892",
  "prompt": "Extract the full abstract, key method details, models tested, benchmarks, and key results for FLAS (Flow-based Activation Steering). How does the flow-based approach differ from linear CAA? What are the key numbers?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b4170d2-20ea-423d-82e1-99d85b39c520",
  "isSidechain": false,
  "requestId": "req_011Cb4WaXwe3vH9EijCrKHcs",
  "type": "assistant",
  "uuid": "7630af3d-2a0e-483f-8892-a9707cd174f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014UB8XZprrLyaS6uUNoWkd8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 37434,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 662,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 37434,
          "cache_creation_input_tokens": 662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 662
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

_source line 48 · 2026-05-15T14:27:23.962Z_

<details><summary>↩ Tool result · `toolu_01FL94T2o3Te4N47CgKTHkVv`</summary>

```text
# FLAS: Flow-based Activation Steering Summary

## Full Abstract
"Activation steering has emerged as a promising alternative for controlling language-model behavior at inference time by modifying intermediate representations while keeping model parameters frozen."

The method addresses limitations in existing steering approaches that are outperformed by prompting and generalize poorly.

## Key Method Details

FLAS learns a concept-conditioned velocity field that transports unsteered activations to steered ones. Unlike prior methods that assume "fixed, single-step, position-invariant transforms," the flow-based approach enables:

- **Curved, multi-step trajectories** through activation space
- **Token-varying interventions** (position-dependent)
- General concept-conditioned dynamics rather than fixed vectors

This contrasts with linear CAA (Concept Activation Analysis), which applies static directional adjustments, whereas FLAS models dynamic flow paths.

## Models Tested
- Gemma-2-2B-IT
- Gemma-2-9B-IT

## Benchmark & Key Results

Evaluated on **AxBench**, FLAS achieved:
- **1.015 harmonic mean** (Gemma-2-2B-IT)
- **1.113 harmonic mean** (Gemma-2-9B-IT)

Notably, "FLAS is the first learned method to consistently outperform prompting" without requiring per-concept tuning, suggesting the learned flow geometry reveals incomplete understanding of activation space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7630af3d-2a0e-483f-8892-a9707cd174f9",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "f16b8682-3ec2-420d-9f4e-22d51eaeaf1e",
  "toolUseResult": {
    "bytes": 46297,
    "code": 200,
    "codeText": "OK",
    "result": "# FLAS: Flow-based Activation Steering Summary\n\n## Full Abstract\n\"Activation steering has emerged as a promising alternative for controlling language-model behavior at inference time by modifying intermediate representations while keeping model parameters frozen.\"\n\nThe method addresses limitations in existing steering approaches that are outperformed by prompting and generalize poorly.\n\n## Key Method Details\n\nFLAS learns a concept-conditioned velocity field that transports unsteered activations to steered ones. Unlike prior methods that assume \"fixed, single-step, position-invariant transforms,\" the flow-based approach enables:\n\n- **Curved, multi-step trajectories** through activation space\n- **Token-varying interventions** (position-dependent)\n- General concept-conditioned dynamics rather than fixed vectors\n\nThis contrasts with linear CAA (Concept Activation Analysis), which applies static directional adjustments, whereas FLAS models dynamic flow paths.\n\n## Models Tested\n- Gemma-2-2B-IT\n- Gemma-2-9B-IT\n\n## Benchmark & Key Results\n\nEvaluated on **AxBench**, FLAS achieved:\n- **1.015 harmonic mean** (Gemma-2-2B-IT)\n- **1.113 harmonic mean** (Gemma-2-9B-IT)\n\nNotably, \"FLAS is the first learned method to consistently outperform prompting\" without requiring per-concept tuning, suggesting the learned flow geometry reveals incomplete understanding of activation space.",
    "durationMs": 5759,
    "url": "https://arxiv.org/abs/2605.05892"
  },
  "sourceToolAssistantUUID": "7630af3d-2a0e-483f-8892-a9707cd174f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 49_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-15 (UTC).**  ## Original idea {   \"title\": \"Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Lo…",
  "leafUuid": "f16b8682-3ec2-420d-9f4e-22d51eaeaf1e",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "Claim-level confidence calibration in long-form generation via steering",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

### Tool call

_source line 51 · 2026-05-15T14:27:27.715Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015Dmm8Ne2VUsxRiyAkNFdtn`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.08169",
  "prompt": "Extract the full abstract, key method details for Spherical Steering. How does the confidence gating work? What is the vMF-based gate? Models tested, benchmarks, key results (especially TruthfulQA numbers)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f16b8682-3ec2-420d-9f4e-22d51eaeaf1e",
  "isSidechain": false,
  "requestId": "req_011Cb4WbEqmgSN454ZmHRVVA",
  "type": "assistant",
  "uuid": "3558282b-f4fc-4c10-a6af-f0eb50687736",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0133Ztbpn8JtL8fFum4xU4Wu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 478,
      "cache_read_input_tokens": 38096,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 478,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 133,
          "cache_read_input_tokens": 38096,
          "cache_creation_input_tokens": 478,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 478
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

_source line 52 · 2026-05-15T14:27:33.040Z_

<details><summary>↩ Tool result · `toolu_015Dmm8Ne2VUsxRiyAkNFdtn`</summary>

```text
# Spherical Steering: Geometry-Aware Activation Rotation - Summary

## Full Abstract
"Inference-time steering has emerged as a promising paradigm for controlling language models (LMs) without the cost of retraining. However, standard approaches typically rely on activation addition, a geometric operation that inevitably alters the magnitude of hidden representations."

The method addresses representation collapse concerns by rotating activations along geodesics toward target directions while preserving signal integrity. A confidence gate dynamically adjusts steering strength based on input uncertainty.

## Key Method Details
Rather than shifting activations with fixed vectors (standard addition-based approaches), Spherical Steering performs **norm-preserving rotation** of activations. This geometric consistency approach maintains the magnitude of hidden representations while guiding them toward target concepts.

## Confidence Gating
The document mentions incorporating "a confidence gate that dynamically modulates steering strength based on input uncertainty," but the abstract provided does not contain specific technical details about the vMF-based gate implementation or mathematical formulation.

## Results
- **TruthfulQA**: +10% improvement over addition-based baselines
- **COPA and Storycloze**: +10% improvement
- The method maintains general open-ended generation quality while achieving these gains

## Models and Benchmarks
The abstract references "multiple-choice benchmarks" but doesn't specify which language models were tested or provide a comprehensive benchmark list in the content provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3558282b-f4fc-4c10-a6af-f0eb50687736",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "c8feda1b-3f2c-47ea-b387-f911df6cac2f",
  "toolUseResult": {
    "bytes": 47357,
    "code": 200,
    "codeText": "OK",
    "result": "# Spherical Steering: Geometry-Aware Activation Rotation - Summary\n\n## Full Abstract\n\"Inference-time steering has emerged as a promising paradigm for controlling language models (LMs) without the cost of retraining. However, standard approaches typically rely on activation addition, a geometric operation that inevitably alters the magnitude of hidden representations.\"\n\nThe method addresses representation collapse concerns by rotating activations along geodesics toward target directions while preserving signal integrity. A confidence gate dynamically adjusts steering strength based on input uncertainty.\n\n## Key Method Details\nRather than shifting activations with fixed vectors (standard addition-based approaches), Spherical Steering performs **norm-preserving rotation** of activations. This geometric consistency approach maintains the magnitude of hidden representations while guiding them toward target concepts.\n\n## Confidence Gating\nThe document mentions incorporating \"a confidence gate that dynamically modulates steering strength based on input uncertainty,\" but the abstract provided does not contain specific technical details about the vMF-based gate implementation or mathematical formulation.\n\n## Results\n- **TruthfulQA**: +10% improvement over addition-based baselines\n- **COPA and Storycloze**: +10% improvement\n- The method maintains general open-ended generation quality while achieving these gains\n\n## Models and Benchmarks\nThe abstract references \"multiple-choice benchmarks\" but doesn't specify which language models were tested or provide a comprehensive benchmark list in the content provided.",
    "durationMs": 5322,
    "url": "https://arxiv.org/abs/2602.08169"
  },
  "sourceToolAssistantUUID": "3558282b-f4fc-4c10-a6af-f0eb50687736",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 53 · 2026-05-15T14:27:33.042Z_

```json
{
  "parentUuid": "c8feda1b-3f2c-47ea-b387-f911df6cac2f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ef032a94-23b2-4374-986e-58ec83854c34",
  "timestamp": "2026-05-15T14:27:33.042Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 54 · 2026-05-15T14:27:36.219Z_

Now let me do a deeper read of the Spherical Steering paper and search for any sub-sentence steering or mid-generation intervention approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef032a94-23b2-4374-986e-58ec83854c34",
  "isSidechain": false,
  "requestId": "req_011Cb4Wbucf7dTHctZ4UMmyT",
  "type": "assistant",
  "uuid": "190c0259-c48b-483e-956a-7b323078743b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWLZp8emd8FEWAKMWDNuna",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 561,
      "cache_read_input_tokens": 38574,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 38574,
          "cache_creation_input_tokens": 561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 561
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

_source line 55 · 2026-05-15T14:27:37.391Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016eoHeBYopWXSadEtXxCYcW`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.08169v1",
  "prompt": "Extract: 1) The exact mathematical formulation of the vMF confidence gate, 2) How steering strength is modulated, 3) What models were tested (exact model names and sizes), 4) Key quantitative results table. Focus on technical depth."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "190c0259-c48b-483e-956a-7b323078743b",
  "isSidechain": false,
  "requestId": "req_011Cb4Wbucf7dTHctZ4UMmyT",
  "type": "assistant",
  "uuid": "de25efb7-ec37-4cbf-b64b-d0851895ced9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWLZp8emd8FEWAKMWDNuna",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 561,
      "cache_read_input_tokens": 38574,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 38574,
          "cache_creation_input_tokens": 561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 561
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

_source line 56 · 2026-05-15T14:27:45.722Z_

<details><summary>↩ Tool result · `toolu_016eoHeBYopWXSadEtXxCYcW`</summary>

```text
# Spherical Steering: Technical Summary

## 1. vMF Confidence Gate Formulation

The von Mises-Fisher based confidence gate maps alignment scores to steering strength via:

**Alignment scoring:** The method computes cosine similarities between the current activation direction and both truthful/hallucinated poles: *sT = μT⊤ĥ(l)* and *sH = μH⊤ĥ(l)*

**Probability normalization:** These similarities feed into a two-class softmax using the vMF exponential form: *pT = eκsT/(eκsT + eκsH)* and *pH = eκsH/(eκsT + eκsH)*

**Confidence computation:** A difference score δ = pH - pT ∈ [-1,1] quantifies hallucination tendency.

**Thresholded mapping:** Steering strength becomes: *t = 0 if δ ≤ β; otherwise t = clip(α·(δ-β)/(1-β), 0, 1)*, where β controls selectivity threshold and α controls rotation magnitude.

## 2. Steering Strength Modulation

Rather than fixed intervention, the method implements **input-adaptive control**. The gate activates only when activations align more with hallucinated directions (δ > β). The rotation magnitude scales via parameter α ∈ (0,1], where higher values enable stronger rotations. Concentration parameter κ acts as temperature, controlling transition sharpness without altering state ordering.

## 3. Models Evaluated

Two instruction-tuned models were tested:
- **LLaMA-3.1-8B-Instruct**
- **Qwen-2.5-7B-Instruct**

## 4. Key Results

| Model | Method | MC1 | MC2 | TRUE×INFO |
|-------|--------|-----|-----|-----------|
| LLaMA-3.1-8B | Baseline | 34.15% | 53.32% | 48.24% |
| LLaMA-3.1-8B | **Spherical Steering** | **49.95%** | **68.51%** | **54.63%** |
| Qwen-2.5-7B | Baseline | 35.87% | 54.95% | 74.40% |
| Qwen-2.5-7B | **Spherical Steering** | **48.71%** | **66.90%** | **77.84%** |

The method achieves simultaneous improvements in multiple-choice accuracy and open-ended generation quality across both models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de25efb7-ec37-4cbf-b64b-d0851895ced9",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "8f46d7a0-3ec8-49b3-b499-1e9414e1df80",
  "toolUseResult": {
    "bytes": 390719,
    "code": 200,
    "codeText": "OK",
    "result": "# Spherical Steering: Technical Summary\n\n## 1. vMF Confidence Gate Formulation\n\nThe von Mises-Fisher based confidence gate maps alignment scores to steering strength via:\n\n**Alignment scoring:** The method computes cosine similarities between the current activation direction and both truthful/hallucinated poles: *sT = μT⊤ĥ(l)* and *sH = μH⊤ĥ(l)*\n\n**Probability normalization:** These similarities feed into a two-class softmax using the vMF exponential form: *pT = eκsT/(eκsT + eκsH)* and *pH = eκsH/(eκsT + eκsH)*\n\n**Confidence computation:** A difference score δ = pH - pT ∈ [-1,1] quantifies hallucination tendency.\n\n**Thresholded mapping:** Steering strength becomes: *t = 0 if δ ≤ β; otherwise t = clip(α·(δ-β)/(1-β), 0, 1)*, where β controls selectivity threshold and α controls rotation magnitude.\n\n## 2. Steering Strength Modulation\n\nRather than fixed intervention, the method implements **input-adaptive control**. The gate activates only when activations align more with hallucinated directions (δ > β). The rotation magnitude scales via parameter α ∈ (0,1], where higher values enable stronger rotations. Concentration parameter κ acts as temperature, controlling transition sharpness without altering state ordering.\n\n## 3. Models Evaluated\n\nTwo instruction-tuned models were tested:\n- **LLaMA-3.1-8B-Instruct**\n- **Qwen-2.5-7B-Instruct**\n\n## 4. Key Results\n\n| Model | Method | MC1 | MC2 | TRUE×INFO |\n|-------|--------|-----|-----|-----------|\n| LLaMA-3.1-8B | Baseline | 34.15% | 53.32% | 48.24% |\n| LLaMA-3.1-8B | **Spherical Steering** | **49.95%** | **68.51%** | **54.63%** |\n| Qwen-2.5-7B | Baseline | 35.87% | 54.95% | 74.40% |\n| Qwen-2.5-7B | **Spherical Steering** | **48.71%** | **66.90%** | **77.84%** |\n\nThe method achieves simultaneous improvements in multiple-choice accuracy and open-ended generation quality across both models.",
    "durationMs": 8324,
    "url": "https://arxiv.org/html/2602.08169v1"
  },
  "sourceToolAssistantUUID": "de25efb7-ec37-4cbf-b64b-d0851895ced9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T14:27:49.359Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017V2eb8udwCbQrNX44aJk4F`</summary>

```json
{
  "query": "sub-sentence activation steering mid-generation intervention token-level steering trigger LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f46d7a0-3ec8-49b3-b499-1e9414e1df80",
  "isSidechain": false,
  "requestId": "req_011Cb4WcrMESj2bx7b77Nroh",
  "type": "assistant",
  "uuid": "d72d364d-e925-48bd-b6f6-7c9ae8792b32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hyoboPEPzEc3VRgK59mvG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 39135,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 39135,
          "cache_creation_input_tokens": 809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 809
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

_source line 58 · 2026-05-15T14:27:57.076Z_

<details><summary>↩ Tool result · `toolu_017V2eb8udwCbQrNX44aJk4F`</summary>

```text
Web search results for query: "sub-sentence activation steering mid-generation intervention token-level steering trigger LLM 2025 2026"

Links: [{"title":"Activation Steering for Masked Diffusion Language Models","url":"https://arxiv.org/html/2512.24143v1"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Control Reinforcement Learning: Interpretable Token-Level Steering of LLMs via Sparse Autoencoder Features","url":"https://arxiv.org/html/2602.10437"},{"title":"Activation Steering in LLMs","url":"https://www.emergentmind.com/topics/activation-steering-method"},{"title":"Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors | OpenReview","url":"https://openreview.net/forum?id=8WQ7VTfPTl"},{"title":"Activation Addition: Steering Language Models Without Optimization","url":"https://arxiv.org/html/2308.10248v4"},{"title":"semantics-adaptive activation intervention","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf"},{"title":"Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/html/2605.03907"},{"title":"Steering Language Models Before They Speak: Logit-Level Interventions","url":"https://arxiv.org/pdf/2601.10960"},{"title":"Steering Language Models in Multi-Token Generation: A Case Study on Tense and Aspect","url":"https://arxiv.org/html/2509.12065v1"}]

I've completed the web search for your query about sub-sentence activation steering, mid-generation intervention, and token-level steering in LLMs. Here are the key findings:

## Recent Research on Token-Level and Mid-Generation Steering (2025-2026)

Control Reinforcement Learning (CRL) is a framework that trains a policy to select SAE features for steering at each token, producing interpretable intervention logs showing which features change model outputs when amplified.

Flexible Activation Steering with Backtracking (FASB) determines the necessity and strength of intervention on-the-fly based on classifiers probing activation states, incorporating a backtracking mechanism to correct previously deviated token predictions.

Conditional Activation Steering (CAST), presented at ICLR 2025 as a spotlight paper, represents a significant development in steering, where the method analyzes activation patterns during inference to decide whether to steer.

## Mid-Generation Intervention Approaches

Recent work moves beyond constant steering approaches to compute different steering coefficients for each steered activation, with per-token steering coefficients proposed to make the presence of steering vectors uniform across token positions.

Semantics-Adaptive Dynamic Intervention (SADI) constructs a dynamic steering vector to intervene model activations at inference time, dynamically steering model behavior by scaling element-wise activations based on input semantics.

Research has also examined activation projections along feature directions representing categorical values like tense (present, past, future) in models like Qwen-7B.

These approaches represent significant advances in fine-grained, context-aware steering that can operate at the token level during generation, moving beyond static intervention methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d72d364d-e925-48bd-b6f6-7c9ae8792b32",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "cefae608-b6ca-4186-9df7-e3e8926a821d",
  "toolUseResult": {
    "query": "sub-sentence activation steering mid-generation intervention token-level steering trigger LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Djy97wpxjaXa8B9ssiqst4",
        "content": [
          {
            "title": "Activation Steering for Masked Diffusion Language Models",
            "url": "https://arxiv.org/html/2512.24143v1"
          },
          {
            "title": "Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra",
            "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"
          },
          {
            "title": "Control Reinforcement Learning: Interpretable Token-Level Steering of LLMs via Sparse Autoencoder Features",
            "url": "https://arxiv.org/html/2602.10437"
          },
          {
            "title": "Activation Steering in LLMs",
            "url": "https://www.emergentmind.com/topics/activation-steering-method"
          },
          {
            "title": "Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors | OpenReview",
            "url": "https://openreview.net/forum?id=8WQ7VTfPTl"
          },
          {
            "title": "Activation Addition: Steering Language Models Without Optimization",
            "url": "https://arxiv.org/html/2308.10248v4"
          },
          {
            "title": "semantics-adaptive activation intervention",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf"
          },
          {
            "title": "Steer Like the LLM: Activation Steering that Mimics Prompting",
            "url": "https://arxiv.org/html/2605.03907"
          },
          {
            "title": "Steering Language Models Before They Speak: Logit-Level Interventions",
            "url": "https://arxiv.org/pdf/2601.10960"
          },
          {
            "title": "Steering Language Models in Multi-Token Generation: A Case Study on Tense and Aspect",
            "url": "https://arxiv.org/html/2509.12065v1"
          }
        ]
      },
      "I've completed the web search for your query about sub-sentence activation steering, mid-generation intervention, and token-level steering in LLMs. Here are the key findings:\n\n## Recent Research on Token-Level and Mid-Generation Steering (2025-2026)\n\nControl Reinforcement Learning (CRL) is a framework that trains a policy to select SAE features for steering at each token, producing interpretable intervention logs showing which features change model outputs when amplified.\n\nFlexible Activation Steering with Backtracking (FASB) determines the necessity and strength of intervention on-the-fly based on classifiers probing activation states, incorporating a backtracking mechanism to correct previously deviated token predictions.\n\nConditional Activation Steering (CAST), presented at ICLR 2025 as a spotlight paper, represents a significant development in steering, where the method analyzes activation patterns during inference to decide whether to steer.\n\n## Mid-Generation Intervention Approaches\n\nRecent work moves beyond constant steering approaches to compute different steering coefficients for each steered activation, with per-token steering coefficients proposed to make the presence of steering vectors uniform across token positions.\n\nSemantics-Adaptive Dynamic Intervention (SADI) constructs a dynamic steering vector to intervene model activations at inference time, dynamically steering model behavior by scaling element-wise activations based on input semantics.\n\nResearch has also examined activation projections along feature directions representing categorical values like tense (present, past, future) in models like Qwen-7B.\n\nThese approaches represent significant advances in fine-grained, context-aware steering that can operate at the token level during generation, moving beyond static intervention methods."
    ],
    "durationSeconds": 7.714172204000002
  },
  "sourceToolAssistantUUID": "d72d364d-e925-48bd-b6f6-7c9ae8792b32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T14:28:00.133Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UFuMxuk7tx8wcWb6uTK5qm`</summary>

```json
{
  "query": "claim-level ECE calibration long-form generation LLM 2025 2026 benchmark results state of the art"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cefae608-b6ca-4186-9df7-e3e8926a821d",
  "isSidechain": false,
  "requestId": "req_011Cb4WdgQDgSeRfjHyAG4Yt",
  "type": "assistant",
  "uuid": "c1a0588d-beef-4140-b888-c5d5b7227367",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qt9wwDfMq453Vu3MXcqcr7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 39944,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 949,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 39944,
          "cache_creation_input_tokens": 949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 949
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

_source line 60 · 2026-05-15T14:28:08.508Z_

<details><summary>↩ Tool result · `toolu_01UFuMxuk7tx8wcWb6uTK5qm`</summary>

```text
Web search results for query: "claim-level ECE calibration long-form generation LLM 2025 2026 benchmark results state of the art"

Links: [{"title":"Benchmarking LLM Uncertainty and Calibration with ...","url":"https://aclanthology.org/2026.eacl-long.106.pdf"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"LLM Uncertainty Quantification Should Be More Human- ...","url":"https://arxiv.org/pdf/2506.07461"},{"title":"LLM as a Judge: A 2026 Guide to Automated Model Assessment | Label Your Data","url":"https://labelyourdata.com/articles/llm-as-a-judge"},{"title":"LLM Benchmarks 2026: 30+ Models Ranked — MMLU, SWE-bench, Arena Elo & Pricing","url":"https://iternal.ai/llm-selection-guide"},{"title":"Long-Context Language Modeling Benchmarks","url":"https://www.emergentmind.com/topics/long-context-language-modeling-benchmarks"},{"title":"Top LLM Evaluation Benchmarks and How They Work","url":"https://deepchecks.com/top-llm-evaluation-benchmarks-and-how-they-work/"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.742/"},{"title":"Benchmarking LLMs via Uncertainty Quantification Fanghua Ye1,2 Mingming Yang1","url":"https://discovery.ucl.ac.uk/id/eprint/10217368/1/1565_Benchmarking_LLMs_via_Unc.pdf"}]

I found relevant search results on LLM calibration and benchmarking. Here's what the research shows:

## Key Findings on ECE Calibration and LLM Benchmarking

### Calibration Metrics in Recent Research

ECE remains a popular metric for measuring calibration error of LLM uncertainty quantification methods, with 16 papers using ECE to measure calibration error, though many evaluation sets were smaller than 5k datapoints. At smaller dataset scales, smECE (smoothed ECE) should be preferred over standard ECE.

### State-of-the-Art Findings (2025-2026)

Recent research analyzing open-weight models on the MMLU benchmark uncovered a distinct confidence correction phase in upper layers, and identified a low-dimensional calibration direction in the residual stream whose perturbation significantly improves calibration metrics (ECE and MCE) without harming accuracy.

### Uncertainty Quantification for Long-Form Generation

Proposed methods based on behavioral features offer strong performance across AUROC, ECE, and Brier Score, approaching that of Semantic Entropy, which relies on multiple generations. LongGenBench introduces CR (Main Task Completion), STIC-1 (execution adherence), and STIC-2 (placement precision) for evaluating long-form generation with multiple metrics weighted for overall scores.

### Research Recommendations

Studies should work to understand the relationship between LLM UQ metrics (like ECE, Brier score) and human-AI team performance, as most papers focus on standard calibration measures such as Brier score, ECE, or AURUC on simple QA tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1a0588d-beef-4140-b888-c5d5b7227367",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "47728883-b12a-4a1b-9232-6d33a5724553",
  "toolUseResult": {
    "query": "claim-level ECE calibration long-form generation LLM 2025 2026 benchmark results state of the art",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QjWjaaA4auoUXLs1Y7ViZU",
        "content": [
          {
            "title": "Benchmarking LLM Uncertainty and Calibration with ...",
            "url": "https://aclanthology.org/2026.eacl-long.106.pdf"
          },
          {
            "title": "LLM Benchmarks 2026 - Compare AI Benchmarks and Tests",
            "url": "https://llm-stats.com/benchmarks"
          },
          {
            "title": "LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT",
            "url": "https://www.lxt.ai/blog/llm-benchmarks/"
          },
          {
            "title": "LLM Uncertainty Quantification Should Be More Human- ...",
            "url": "https://arxiv.org/pdf/2506.07461"
          },
          {
            "title": "LLM as a Judge: A 2026 Guide to Automated Model Assessment | Label Your Data",
            "url": "https://labelyourdata.com/articles/llm-as-a-judge"
          },
          {
            "title": "LLM Benchmarks 2026: 30+ Models Ranked — MMLU, SWE-bench, Arena Elo & Pricing",
            "url": "https://iternal.ai/llm-selection-guide"
          },
          {
            "title": "Long-Context Language Modeling Benchmarks",
            "url": "https://www.emergentmind.com/topics/long-context-language-modeling-benchmarks"
          },
          {
            "title": "Top LLM Evaluation Benchmarks and How They Work",
            "url": "https://deepchecks.com/top-llm-evaluation-benchmarks-and-how-they-work/"
          },
          {
            "title": "Calibration Across Layers: Understanding Calibration Evolution in LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.742/"
          },
          {
            "title": "Benchmarking LLMs via Uncertainty Quantification Fanghua Ye1,2 Mingming Yang1",
            "url": "https://discovery.ucl.ac.uk/id/eprint/10217368/1/1565_Benchmarking_LLMs_via_Unc.pdf"
          }
        ]
      },
      "I found relevant search results on LLM calibration and benchmarking. Here's what the research shows:\n\n## Key Findings on ECE Calibration and LLM Benchmarking\n\n### Calibration Metrics in Recent Research\n\nECE remains a popular metric for measuring calibration error of LLM uncertainty quantification methods, with 16 papers using ECE to measure calibration error, though many evaluation sets were smaller than 5k datapoints. At smaller dataset scales, smECE (smoothed ECE) should be preferred over standard ECE.\n\n### State-of-the-Art Findings (2025-2026)\n\nRecent research analyzing open-weight models on the MMLU benchmark uncovered a distinct confidence correction phase in upper layers, and identified a low-dimensional calibration direction in the residual stream whose perturbation significantly improves calibration metrics (ECE and MCE) without harming accuracy.\n\n### Uncertainty Quantification for Long-Form Generation\n\nProposed methods based on behavioral features offer strong performance across AUROC, ECE, and Brier Score, approaching that of Semantic Entropy, which relies on multiple generations. LongGenBench introduces CR (Main Task Completion), STIC-1 (execution adherence), and STIC-2 (placement precision) for evaluating long-form generation with multiple metrics weighted for overall scores.\n\n### Research Recommendations\n\nStudies should work to understand the relationship between LLM UQ metrics (like ECE, Brier score) and human-AI team performance, as most papers focus on standard calibration measures such as Brier score, ECE, or AURUC on simple QA tasks."
    ],
    "durationSeconds": 8.370772024000006
  },
  "sourceToolAssistantUUID": "c1a0588d-beef-4140-b888-c5d5b7227367",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T14:28:11.596Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019TmhhJBsn2xyxL6y3NZZAo`</summary>

```json
{
  "query": "probe score early claim detection hallucination hidden state signal timing when does probe detect uncertainty token position 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47728883-b12a-4a1b-9232-6d33a5724553",
  "isSidechain": false,
  "requestId": "req_011Cb4WeXJZNSfKcPZkP7ouX",
  "type": "assistant",
  "uuid": "c21e7876-333d-4296-9006-26bec6e08ae1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Jq2HBeXpP5Ptvu3MeEiTb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1004,
      "cache_read_input_tokens": 40893,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1004,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 40893,
          "cache_creation_input_tokens": 1004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1004
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

_source line 62 · 2026-05-15T14:28:18.601Z_

<details><summary>↩ Tool result · `toolu_019TmhhJBsn2xyxL6y3NZZAo`</summary>

```text
Web search results for query: "probe score early claim detection hallucination hidden state signal timing when does probe detect uncertainty token position 2025 2026"

Links: [{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs","url":"https://arxiv.org/html/2507.16488"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable ...","url":"https://aclanthology.org/2025.acl-long.880.pdf"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://www.hallucination-probes.com/"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination","url":"https://arxiv.org/pdf/2507.16488"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/html/2603.05465v1"},{"title":"Token-Level Truth: Real-Time Hallucination Detection for Production LLMs | vLLM Blog","url":"https://blog.vllm.ai/2025/12/14/halugate.html"},{"title":"REAL-TIME DETECTION OF HALLUCINATED ENTITIES","url":"https://openreview.net/pdf?id=YxJEMTflww"},{"title":"Beyond Token Probes: Hallucination Detection via","url":"https://openreview.net/pdf/8c1a20caf3d46334d96c8131e9ff069d2ff949b2.pdf"},{"title":"Token-Level Hallucination Detection","url":"https://www.emergentmind.com/topics/token-level-hallucination-detection"}]

Based on the search results, here's what I found regarding probe score detection of hallucinations, particularly around timing and token position:

## Early Detection and Timing

Hallucination signals are most detectable at the onset of hallucinated spans (first token), suggesting probes can detect uncertainty early in generation. Hallucination risk is detectable before generation in some vision-language models, indicating that signals exist prior to token production.

## Hidden State Signals and Token Position

Probes run in the same forward pass and flag unsupported entities as tokens are produced with negligible computational overhead. Linear probes predict from hidden activations whether a token is part of a hallucinated entity.

The location of predictive signals for hallucinations widely varies across LLMs, even for the same dataset, and error signals' positions vary across layers and tokens.

## Multi-Token Aggregation

Interestingly, aggregation of multi-token evidence or probing internal activations consistently surpasses single-token baselines, suggesting that while signals are detectable early, combining information across multiple token positions improves detection accuracy.

## Real-Time Detection Capability

Real-time and streaming inference is feasible with lightweight probes and attention-based models, enabling detection during generation rather than post-hoc analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c21e7876-333d-4296-9006-26bec6e08ae1",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "d57af1c4-1051-490b-bd08-17f3d3c769ce",
  "toolUseResult": {
    "query": "probe score early claim detection hallucination hidden state signal timing when does probe detect uncertainty token position 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RAiizEb34jf4gNJy5BuFmr",
        "content": [
          {
            "title": "ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs",
            "url": "https://arxiv.org/html/2507.16488"
          },
          {
            "title": "Real-Time Detection of Hallucinated Entities in Long-Form Generation",
            "url": "https://arxiv.org/html/2509.03531v1"
          },
          {
            "title": "ICR Probe: Tracking Hidden State Dynamics for Reliable ...",
            "url": "https://aclanthology.org/2025.acl-long.880.pdf"
          },
          {
            "title": "Real-Time Detection of Hallucinated Entities in Long-Form Generation",
            "url": "https://www.hallucination-probes.com/"
          },
          {
            "title": "ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination",
            "url": "https://arxiv.org/pdf/2507.16488"
          },
          {
            "title": "HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token",
            "url": "https://arxiv.org/html/2603.05465v1"
          },
          {
            "title": "Token-Level Truth: Real-Time Hallucination Detection for Production LLMs | vLLM Blog",
            "url": "https://blog.vllm.ai/2025/12/14/halugate.html"
          },
          {
            "title": "REAL-TIME DETECTION OF HALLUCINATED ENTITIES",
            "url": "https://openreview.net/pdf?id=YxJEMTflww"
          },
          {
            "title": "Beyond Token Probes: Hallucination Detection via",
            "url": "https://openreview.net/pdf/8c1a20caf3d46334d96c8131e9ff069d2ff949b2.pdf"
          },
          {
            "title": "Token-Level Hallucination Detection",
            "url": "https://www.emergentmind.com/topics/token-level-hallucination-detection"
          }
        ]
      },
      "Based on the search results, here's what I found regarding probe score detection of hallucinations, particularly around timing and token position:\n\n## Early Detection and Timing\n\nHallucination signals are most detectable at the onset of hallucinated spans (first token), suggesting probes can detect uncertainty early in generation. Hallucination risk is detectable before generation in some vision-language models, indicating that signals exist prior to token production.\n\n## Hidden State Signals and Token Position\n\nProbes run in the same forward pass and flag unsupported entities as tokens are produced with negligible computational overhead. Linear probes predict from hidden activations whether a token is part of a hallucinated entity.\n\nThe location of predictive signals for hallucinations widely varies across LLMs, even for the same dataset, and error signals' positions vary across layers and tokens.\n\n## Multi-Token Aggregation\n\nInterestingly, aggregation of multi-token evidence or probing internal activations consistently surpasses single-token baselines, suggesting that while signals are detectable early, combining information across multiple token positions improves detection accuracy.\n\n## Real-Time Detection Capability\n\nReal-time and streaming inference is feasible with lightweight probes and attention-based models, enabling detection during generation rather than post-hoc analysis."
    ],
    "durationSeconds": 7.000491216000024
  },
  "sourceToolAssistantUUID": "c21e7876-333d-4296-9006-26bec6e08ae1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 63_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-15 (UTC).**  ## Original idea {   \"title\": \"Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Lo…",
  "leafUuid": "d57af1c4-1051-490b-bd08-17f3d3c769ce",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Claim-level confidence calibration in long-form generation via steering",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

### Tool call

_source line 65 · 2026-05-15T14:28:25.770Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AshYFNoW1HeZAGnuo9MZw4`</summary>

```json
{
  "query": "Kumaran \"How do LLMs Compute Verbal Confidence\" 2603.17839 cached retrieval answer-adjacent positions early signal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d57af1c4-1051-490b-bd08-17f3d3c769ce",
  "isSidechain": false,
  "requestId": "req_011Cb4WfGSd1iZUY1We4z9UY",
  "type": "assistant",
  "uuid": "465a2443-1a98-45b4-b82e-7fbed3f5fa1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ne833AAKghPTFMeBcFHo6y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 859,
      "cache_read_input_tokens": 41897,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 859,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 41897,
          "cache_creation_input_tokens": 859,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 859
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

_source line 66 · 2026-05-15T14:28:31.796Z_

<details><summary>↩ Tool result · `toolu_01AshYFNoW1HeZAGnuo9MZw4`</summary>

```text
Web search results for query: "Kumaran "How do LLMs Compute Verbal Confidence" 2603.17839 cached retrieval answer-adjacent positions early signal"

Links: [{"title":"[2603.17839] How do LLMs Compute Verbal Confidence","url":"https://arxiv.org/abs/2603.17839"},{"title":"How do LLMs Compute Verbal Confidence?","url":"https://arxiv.org/html/2603.17839v1"},{"title":"How do LLMs Compute Verbal Confidence | Computing Research Repository | DeepDyve","url":"https://www.deepdyve.com/lp/arxiv/how-do-llms-compute-verbal-confidence-gRipbFraNC"},{"title":"fly51fly on X: \"[CL] How do LLMs Compute Verbal Confidence D Kumaran, A Conmy, F Barbero, S Osindero… [Google DeepMind] (2026) https://t.co/Eg3MbRks7u https://t.co/efitBcG7EK\" / X","url":"https://x.com/fly51fly/status/2034742652735037708"},{"title":"Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/html/2603.25052v1"},{"title":"Verbal Confidence Saturation in 3–9B Open-Weight Instruction-Tuned LLMs: A Pre-Registered Psychometric Validity Screen","url":"https://arxiv.org/html/2604.22215"}]

I found the research paper you're looking for. "How do LLMs Compute Verbal Confidence" is about verbal confidence—prompting LLMs to state their confidence as a number or category—which is widely used to extract uncertainty estimates from black-box models.

The paper addresses two questions: first, when confidence is computed - just-in-time when requested, or automatically during answer generation and cached for later retrieval; and second, what verbal confidence represents - token log-probabilities, or a richer evaluation of answer quality.

Focusing on Gemma 3 27B and Qwen 2.5 7B, the researchers provide convergent evidence for cached retrieval. Activation steering, patching, noising, and swap experiments reveal that confidence representations emerge at answer-adjacent positions before appearing at the verbalization site. Attention blocking pinpoints the information flow: confidence is gathered from answer tokens, cached at the first post-answer position, then retrieved for output.

The paper (arXiv:2603.17839) was submitted on March 18, 2026, with a revised version on March 31, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "465a2443-1a98-45b4-b82e-7fbed3f5fa1e",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "2eea6105-7a60-41a6-9ed6-13d0e676b539",
  "toolUseResult": {
    "query": "Kumaran \"How do LLMs Compute Verbal Confidence\" 2603.17839 cached retrieval answer-adjacent positions early signal",
    "results": [
      {
        "tool_use_id": "srvtoolu_01266YvpGYqEJD8QnmJm49td",
        "content": [
          {
            "title": "[2603.17839] How do LLMs Compute Verbal Confidence",
            "url": "https://arxiv.org/abs/2603.17839"
          },
          {
            "title": "How do LLMs Compute Verbal Confidence?",
            "url": "https://arxiv.org/html/2603.17839v1"
          },
          {
            "title": "How do LLMs Compute Verbal Confidence | Computing Research Repository | DeepDyve",
            "url": "https://www.deepdyve.com/lp/arxiv/how-do-llms-compute-verbal-confidence-gRipbFraNC"
          },
          {
            "title": "fly51fly on X: \"[CL] How do LLMs Compute Verbal Confidence D Kumaran, A Conmy, F Barbero, S Osindero… [Google DeepMind] (2026) https://t.co/Eg3MbRks7u https://t.co/efitBcG7EK\" / X",
            "url": "https://x.com/fly51fly/status/2034742652735037708"
          },
          {
            "title": "Closing the Confidence-Faithfulness Gap in Large Language Models",
            "url": "https://arxiv.org/html/2603.25052v1"
          },
          {
            "title": "Verbal Confidence Saturation in 3–9B Open-Weight Instruction-Tuned LLMs: A Pre-Registered Psychometric Validity Screen",
            "url": "https://arxiv.org/html/2604.22215"
          }
        ]
      },
      "I found the research paper you're looking for. \"How do LLMs Compute Verbal Confidence\" is about verbal confidence—prompting LLMs to state their confidence as a number or category—which is widely used to extract uncertainty estimates from black-box models.\n\nThe paper addresses two questions: first, when confidence is computed - just-in-time when requested, or automatically during answer generation and cached for later retrieval; and second, what verbal confidence represents - token log-probabilities, or a richer evaluation of answer quality.\n\nFocusing on Gemma 3 27B and Qwen 2.5 7B, the researchers provide convergent evidence for cached retrieval. Activation steering, patching, noising, and swap experiments reveal that confidence representations emerge at answer-adjacent positions before appearing at the verbalization site. Attention blocking pinpoints the information flow: confidence is gathered from answer tokens, cached at the first post-answer position, then retrieved for output.\n\nThe paper (arXiv:2603.17839) was submitted on March 18, 2026, with a revised version on March 31, 2026."
    ],
    "durationSeconds": 6.022365370999992
  },
  "sourceToolAssistantUUID": "465a2443-1a98-45b4-b82e-7fbed3f5fa1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-15T14:28:35.272Z_

Good — I now have all the key information. Let me do one more search on compute estimates for 70B model experiments to validate the resource trimming.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eea6105-7a60-41a6-9ed6-13d0e676b539",
  "isSidechain": false,
  "requestId": "req_011Cb4WgEpfY2z7dQy9JU6sw",
  "type": "assistant",
  "uuid": "a0c39184-c8d9-49af-843c-de0263bcd808",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FtgS2wKbMYbMStirVbuQp3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 756,
      "cache_read_input_tokens": 42756,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 756,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 113,
          "cache_read_input_tokens": 42756,
          "cache_creation_input_tokens": 756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 756
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

_source line 68 · 2026-05-15T14:28:36.388Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018E9NgEPa6fC9mpLuCt2F7v`</summary>

```json
{
  "query": "Llama 3.1 70B FActScore biography generation compute cost H100 GPU hours experiment 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0c39184-c8d9-49af-843c-de0263bcd808",
  "isSidechain": false,
  "requestId": "req_011Cb4WgEpfY2z7dQy9JU6sw",
  "type": "assistant",
  "uuid": "226274ac-da4b-427d-9ac4-c17199c643ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FtgS2wKbMYbMStirVbuQp3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 756,
      "cache_read_input_tokens": 42756,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 756,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 113,
          "cache_read_input_tokens": 42756,
          "cache_creation_input_tokens": 756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 756
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

_source line 69 · 2026-05-15T14:28:47.104Z_

<details><summary>↩ Tool result · `toolu_018E9NgEPa6fC9mpLuCt2F7v`</summary>

```text
Web search results for query: "Llama 3.1 70B FActScore biography generation compute cost H100 GPU hours experiment 2025 2026"

Links: [{"title":"What You Need to Know About Meta Llama 3.3 70B","url":"https://www.hyperstack.cloud/blog/thought-leadership/what-is-meta-llama-3-3-70b-features-use-cases-more"},{"title":"Evaluating Llama‑3.3‑70B Inference on NVIDIA H100 and A100 GPUs","url":"https://dlewis.io/evaluating-llama-33-70b-inference-h100-a100/"},{"title":"Evaluating Llama 3.3 70B Inference on NVIDIA H100 and A100 GPUs","url":"https://blog.silexdata.com/blog/evaluating-llama-33-70b-inference-h100-a100/"},{"title":"Testing Llama 3.3 70B inference performance on NVIDIA GH200 in Lambda Cloud","url":"https://www.baseten.co/blog/testing-llama-inference-performance-nvidia-gh200-lambda-cloud/"},{"title":"meta-llama/Llama-3.1-70B · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.1-70B"},{"title":"llama.cpp: Fast Local LLM Inference, Hardware Choices & Tuning","url":"https://www.clarifai.com/blog/ilama.cpp"},{"title":"Llama 3.3 70B Guide: Benchmarks, Hardware, Pricing, API, and Real-World Use Cases - Ucstrategies News","url":"https://ucstrategies.com/news/llama-3-3-70b-guide-benchmarks-hardware-pricing-api-and-real-world-use-cases/"},{"title":"llama3-70b-instruct Model by Meta | NVIDIA NIM","url":"https://build.nvidia.com/meta/llama3-70b/modelcard"},{"title":"Should I run Llama 70B on an NVIDIA H100 or A100? | AI FAQ | Jarvis Labs","url":"https://jarvislabs.ai/ai-faqs/should-i-run-llama-70b-on-an-nvidia-h100-or-a100"},{"title":"Nvidia H100 GPU Server Ollama Performance Test: The Best Choice for LLM Reasoning","url":"https://www.databasemart.com/blog/ollama-gpu-benchmark-h100"}]

I found information about Llama 3.1 70B compute costs with H100 GPUs, but the search results don't contain specific information about FActScore biography generation experiments with compute cost measurements. Let me search more specifically for that:

Links: [{"title":"FactScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation | Research - AI at Meta","url":"https://ai.meta.com/research/publications/factscore-fine-grained-atomic-evaluation-of-factual-precision-in-long-form-text-generation/"},{"title":"[2305.14251] FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation","url":"https://arxiv.org/abs/2305.14251"},{"title":"FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation","url":"https://arxiv.org/html/2305.14251"},{"title":"FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.741/"},{"title":"GitHub - shmsw25/FActScore: A package to evaluate factuality of long-form generation. Original implementation of our EMNLP 2023 paper \"FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation\" · GitHub","url":"https://github.com/shmsw25/factscore"},{"title":"FACTSCORE: Fine-grained Atomic Evaluation of Factual ...","url":"https://aclanthology.org/2023.emnlp-main.741.pdf"},{"title":"factscore · PyPI","url":"https://pypi.org/project/factscore/"},{"title":"An Analysis of Multilingual FActScore","url":"https://aclanthology.org/2024.emnlp-main.247.pdf"},{"title":"Assessing Factuality of Multilingual LLMs using FActScore","url":"https://openreview.net/pdf?id=lkrH6ovzsj"},{"title":"Mohit Iyyer on X: \"We just released VeriScore, a variant of FactScore that only extracts and evaluates *verifiable* claims from a long-form LLM-generated text. This makes it possible to evaluate factuality on more complex tasks than e.g. biography generation. Check out paper/code for more!!\" / X","url":"https://x.com/MohitIyyer/status/1806774242437918818"}]

Based on my web search results, I found relevant information about these topics, though the search results don't contain a specific single paper that combines all these elements together. Here's what I found:

## Llama 3.1 70B Training Compute Costs

Llama 3.1 training utilized a cumulative of 39.3M GPU hours of computation on H100-80GB (TDP of 700W) type hardware. This represents the full training cost across all Llama 3.1 sizes (8B, 70B, and 405B models).

## FActScore Biography Generation

FActScore breaks a generation into a series of atomic facts and computes the percentage of atomic facts supported by a reliable knowledge source. In their evaluation of people biographies generated by state-of-the-art commercial LMs, ChatGPT achieved 58%.

Evaluating 6,500 generations from a new set of 13 recent LMs would have cost $26K if evaluated by humans using manual evaluation, but running FActScore costs about $1 of the API cost per 100 sentences. For instance, if you have 100 generations, each with 5 sentences on average, it costs $5 in total.

## H100 GPU Performance and Inference

Llama 3.1 70B averaged 89 tokens per second on NVIDIA H100, and at 89 tokens per second on H100, the model generates a 200-line function in about 15 seconds.

However, I did not find a specific 2025-2026 experiment that combines Llama 3.1 70B, FActScore biography generation evaluation, and detailed H100 GPU hour compute cost measurements in a single research paper or report.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "226274ac-da4b-427d-9ac4-c17199c643ba",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "040cce09-7b92-44c6-84bd-65ff93e4863a",
  "toolUseResult": {
    "query": "Llama 3.1 70B FActScore biography generation compute cost H100 GPU hours experiment 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011JNJmN9M2LSTgohWU4C4PZ",
        "content": [
          {
            "title": "What You Need to Know About Meta Llama 3.3 70B",
            "url": "https://www.hyperstack.cloud/blog/thought-leadership/what-is-meta-llama-3-3-70b-features-use-cases-more"
          },
          {
            "title": "Evaluating Llama‑3.3‑70B Inference on NVIDIA H100 and A100 GPUs",
            "url": "https://dlewis.io/evaluating-llama-33-70b-inference-h100-a100/"
          },
          {
            "title": "Evaluating Llama 3.3 70B Inference on NVIDIA H100 and A100 GPUs",
            "url": "https://blog.silexdata.com/blog/evaluating-llama-33-70b-inference-h100-a100/"
          },
          {
            "title": "Testing Llama 3.3 70B inference performance on NVIDIA GH200 in Lambda Cloud",
            "url": "https://www.baseten.co/blog/testing-llama-inference-performance-nvidia-gh200-lambda-cloud/"
          },
          {
            "title": "meta-llama/Llama-3.1-70B · Hugging Face",
            "url": "https://huggingface.co/meta-llama/Llama-3.1-70B"
          },
          {
            "title": "llama.cpp: Fast Local LLM Inference, Hardware Choices & Tuning",
            "url": "https://www.clarifai.com/blog/ilama.cpp"
          },
          {
            "title": "Llama 3.3 70B Guide: Benchmarks, Hardware, Pricing, API, and Real-World Use Cases - Ucstrategies News",
            "url": "https://ucstrategies.com/news/llama-3-3-70b-guide-benchmarks-hardware-pricing-api-and-real-world-use-cases/"
          },
          {
            "title": "llama3-70b-instruct Model by Meta | NVIDIA NIM",
            "url": "https://build.nvidia.com/meta/llama3-70b/modelcard"
          },
          {
            "title": "Should I run Llama 70B on an NVIDIA H100 or A100? | AI FAQ | Jarvis Labs",
            "url": "https://jarvislabs.ai/ai-faqs/should-i-run-llama-70b-on-an-nvidia-h100-or-a100"
          },
          {
            "title": "Nvidia H100 GPU Server Ollama Performance Test: The Best Choice for LLM Reasoning",
            "url": "https://www.databasemart.com/blog/ollama-gpu-benchmark-h100"
          }
        ]
      },
      "I found information about Llama 3.1 70B compute costs with H100 GPUs, but the search results don't contain specific information about FActScore biography generation experiments with compute cost measurements. Let me search more specifically for that:",
      {
        "tool_use_id": "srvtoolu_01XvC9Fpvp7mKvUFBZq1Y3aG",
        "content": [
          {
            "title": "FactScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation | Research - AI at Meta",
            "url": "https://ai.meta.com/research/publications/factscore-fine-grained-atomic-evaluation-of-factual-precision-in-long-form-text-generation/"
          },
          {
            "title": "[2305.14251] FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation",
            "url": "https://arxiv.org/abs/2305.14251"
          },
          {
            "title": "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation",
            "url": "https://arxiv.org/html/2305.14251"
          },
          {
            "title": "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation - ACL Anthology",
            "url": "https://aclanthology.org/2023.emnlp-main.741/"
          },
          {
            "title": "GitHub - shmsw25/FActScore: A package to evaluate factuality of long-form generation. Original implementation of our EMNLP 2023 paper \"FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation\" · GitHub",
            "url": "https://github.com/shmsw25/factscore"
          },
          {
            "title": "FACTSCORE: Fine-grained Atomic Evaluation of Factual ...",
            "url": "https://aclanthology.org/2023.emnlp-main.741.pdf"
          },
          {
            "title": "factscore · PyPI",
            "url": "https://pypi.org/project/factscore/"
          },
          {
            "title": "An Analysis of Multilingual FActScore",
            "url": "https://aclanthology.org/2024.emnlp-main.247.pdf"
          },
          {
            "title": "Assessing Factuality of Multilingual LLMs using FActScore",
            "url": "https://openreview.net/pdf?id=lkrH6ovzsj"
          },
          {
            "title": "Mohit Iyyer on X: \"We just released VeriScore, a variant of FactScore that only extracts and evaluates *verifiable* claims from a long-form LLM-generated text. This makes it possible to evaluate factuality on more complex tasks than e.g. biography generation. Check out paper/code for more!!\" / X",
            "url": "https://x.com/MohitIyyer/status/1806774242437918818"
          }
        ]
      },
      "Based on my web search results, I found relevant information about these topics, though the search results don't contain a specific single paper that combines all these elements together. Here's what I found:\n\n## Llama 3.1 70B Training Compute Costs\n\nLlama 3.1 training utilized a cumulative of 39.3M GPU hours of computation on H100-80GB (TDP of 700W) type hardware. This represents the full training cost across all Llama 3.1 sizes (8B, 70B, and 405B models).\n\n## FActScore Biography Generation\n\nFActScore breaks a generation into a series of atomic facts and computes the percentage of atomic facts supported by a reliable knowledge source. In their evaluation of people biographies generated by state-of-the-art commercial LMs, ChatGPT achieved 58%.\n\nEvaluating 6,500 generations from a new set of 13 recent LMs would have cost $26K if evaluated by humans using manual evaluation, but running FActScore costs about $1 of the API cost per 100 sentences. For instance, if you have 100 generations, each with 5 sentences on average, it costs $5 in total.\n\n## H100 GPU Performance and Inference\n\nLlama 3.1 70B averaged 89 tokens per second on NVIDIA H100, and at 89 tokens per second on H100, the model generates a 200-line function in about 15 seconds.\n\nHowever, I did not find a specific 2025-2026 experiment that combines Llama 3.1 70B, FActScore biography generation evaluation, and detailed H100 GPU hour compute cost measurements in a single research paper or report."
    ],
    "durationSeconds": 10.710659526000002
  },
  "sourceToolAssistantUUID": "226274ac-da4b-427d-9ac4-c17199c643ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-15T14:30:58.282Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to revise the research idea. Let me synthesize what I've learned:

1. **O'Neill et al. (2507.23221)**: Uses external observer model's linear probe on residual stream to detect and steer contextual hallucinations. Tested on Gemma-2 2B-27B. Key differences from RaS: (a) external observer vs self-probing, (b) binary hallucination detection vs calibrated confidence, (c) contextual hallucinations with given context vs long-form factual generation.

2. **ConFix/CARE (Yuan et al., SIGIR 2025, arXiv 2411.13343)**: Fact-level calibration framework that uses high-confidence facts to iteratively refine low-confidence ones. 

The approach is inference-time with no training required, tested across LLaMA, Vicuna, and GPT-3.5-turbo on benchmarks like LongFact and ASQA. The paper title appears to be "Fact-Level Calibration and Correction for Long-Form Generations," though there's some naming variation in how it's been referenced.

CAST at ICLR 2025 uses conditional activation steering with a formula that applies a threshold function to similarity scores between hidden states and projected condition vectors, scaled by a behavior vector. It's been evaluated on models ranging from 1.8B to 32B parameters, and the condition vector essentially gates when steering should occur—similar in spirit to probe-triggered steering but using PCA-derived vectors instead of learned probe thresholds.

FLAS, a more recent approach from May 2026, takes a different angle by learning concept-conditioned velocity fields that guide curved activation trajectories, though it's only been tested on smaller models like Gemma-2. Spherical Steering from February 2026 uses rotation-based steering with a vMF confidence gate that clips the steering intensity based on the difference between predicted hidden and target hidden states, achieving around 10% improvement on TruthfulQA when tested on LLaMA-3.1-8B and Qwen-2.5-7B.

For the compute budget issue, I'm cutting the 8B validation track down to a lighter sanity check saving about 15 hours, reducing ablations from five to three for another 15 hours saved, and tightening baselines to just the two most relevant approaches to save another 15 hours. The revised budget keeps the orthogonality pilot and core probe training intact, scales back the 70B generation by reducing the corpus size, and focuses the baseline comparisons on Han et al. and CURE only. I'm breaking down the revised timeline with the hybrid approach: keeping the 8B model as a lighter sanity check at 10 hours instead of 25, reducing the 70B evaluation to 80 hours, trimming ablations to just the 3 core ones at 23 hours, and cutting baseline comparisons to 30 hours. That puts me at 175 hours total with about a 25-hour buffer, which feels solid. But I should double-check whether I'm actually hitting the reviewer's target of 2 most relevant baselines instead of the broader set I've listed. - Probe + direction extraction 8B: 4h
- 70B evaluation: 85h
- 8B sanity check: 12h
- Baselines: 30h (unsteered ~3h, Han et al. ~13h, CURE ~14h)
- Ablations (3): 25h
- Buffer for debugging and reruns

That gets me to around 185h with some headroom. Let me recalibrate to use the full 195h budget more efficiently by bumping up the evaluation and ablation time slightly—85h for 70B evaluation, 25h for the three core ablations, and 30h for baselines should give me enough compute to be thorough without overcommitting.

Now I need to address how O'Neill et al. and ConFix differ from this work. O'Neill uses self-probing on smaller models like Gemma with binary hallucination detection, whereas I'm doing external steering on Llama 3.1 with calibrated confidence scores across claim-level granularity. ConFix takes a different angle entirely—it's prompt-based iterative correction applied post-hoc, while I'm doing single-pass activation steering that requires no external knowledge pipeline.

For the steering latency concern, the reviewer wants sub-sentence level triggers rather than full-sentence ones.  I can compute probe scores at every token with negligible overhead, maintain an exponential moving average over a sliding window, and trigger steering immediately when the signal drops below threshold. The key insight is that I need a minimum window of around 8 tokens for the probe signal to be reliable, so latency is bounded by that token count rather than waiting for a sentence boundary. I'll go with this approach as the primary method.

Now I'm adjusting the quantitative targets—bringing the primary goal down to 25% ECE reduction with 40% as a stretch target. I should also add a sentence to the landscape section distinguishing the probe threshold approach from CAST's PCA-derived condition vector.

Let me reconsider the mid-sentence steering mechanism more carefully. If the probe detects uncertainty partway through a claim like "Barack Obama was born in," steering the later tokens in that same sentence could help hedge the statement, but I need to verify this actually produces coherent output rather than jarring transitions.

The key insight is to run the factuality probe continuously at each token position with minimal overhead, tracking an exponential moving average across a sliding window. When this average dips below the threshold, steering activates immediately—even mid-sentence—allowing the model to inject hedging language or qualifiers into the remaining tokens of the current claim. The steering strength adapts based on how far the score has dropped. Once the EMA climbs back above threshold, steering deactivates.

This approach catches uncertain claims early (ideally within the first few tokens), though there's typically a latency of around half the window size before the EMA registers the drop. The confidence direction should naturally produce appropriate hedging tokens like "reportedly" or "I believe" rather than creating awkward disruptions. Now I'm ready to pull all these pieces together into the final design.

I'm refining the technical specifications: cutting compute down to under 200 H100-hours, expanding the related work section with recent papers on uncertainty and steering, redesigning the online steering mechanism to trigger more frequently at the sub-sentence level, adjusting the ECE targets to be more realistic, streamlining the ablations to focus on the most critical comparisons, and narrowing the baselines to the most relevant approaches. The core concept stays intact—this is really about tightening the execution and scope. Now I need to structure this into the JSON format and make sure I'm capturing all the related work properly, including approaches like CARE and ConFix that address similar problems. I'm trying to pin down the exact naming and framing of this paper—the reviewer calls it "CARE" but the arXiv version uses "ConFix," and the SIGIR 2025 published title appears to be "Fact-Level Calibration and Correction for Long-Form Generations." I need to verify which name is most accurate for the final version. I'm settling on citing the SIGIR 2025 publication with the full title "Fact-Level Calibration and Correction for Long-Form Generations" by Yuan et al., and I'll adopt the reviewer's naming convention of CARE since they're referencing the published version. Now I need to write out the revised JSON response, which will be substantial. I'm also reconsidering the sub-sentence steering example the reviewer provided where Obama's birthplace gets interrupted mid-sentence.

The reviewer's example feels a bit artificial for how language models actually work. In practice, sub-sentence steering wouldn't create those parenthetical hesitations — instead, it shifts the probability distribution toward uncertainty markers at each token position where steering is applied. So if steering activates partway through a sentence, the subsequent tokens would naturally favor hedging language rather than inserting awkward asides. A more realistic output would be something like "Barack Obama was reportedly born in Honolulu, Hawaii, likely on August 4, 1961" where the uncertainty is woven into the phrasing itself rather than breaking the sentence structure.

The key advantage here is that the probe signal from early tokens already encodes information about factuality, enabling detection before the model commits to a particular claim. Now I'm working through the complete revised approach and getting more precise about the compute requirements — breaking down the resource allocation across the orthogonality pilot, probe training for both model sizes, and the main evaluation phases.

For the wall clock timeline, with dual H100s handling the 70B work, I'm looking at roughly 100 hours of continuous compute time, which translates to about 4-5 weeks accounting for gaps between runs.

Breaking this into phases: the first week covers the pilot and probe training, weeks two and three handle the main evaluation and baselines, week four focuses on ablations and analysis, and week five is reserved for writing and buffer time. That gives me a solid 5-week schedule that fits within the AAAI 2027 submission window.

Now I'm double-checking the paper name—the reviewer mentioned "CARE" but my research indicated it was "ConFix". Let me verify if there's a specific version that uses the CARE naming.

Looking back at my search results, the ResearchGate description mentioned "CARE (Confidence-Aware Fact Correction)" while the arXiv version (2411.13343) was titled "Fact-Level Confidence Calibration and Self-Correction" and called the method ConFix. It appears the SIGIR 2025 published version may have renamed it to CARE, or CARE is the broader framework with ConFix as the specific algorithm. Since the reviewer uses CARE and that aligns with the published version, I'll go with that naming. I'm settling on CARE as the acronym for the SIGIR 2025 paper, though the exact expansion isn't crucial for citation purposes. Now I need to refine how I describe the sub-sentence triggering mechanism—the key insight is that instead of waiting for sentence boundaries, the approach evaluates an exponential moving average of probe scores every K tokens (with K=8 as default), allowing it to catch uncertainty mid-sentence and trigger steering when needed. This gives better signal quality through smoothing while still enabling responsive corrections. Let me draft the full JSON response with these clarifications. Now I'm organizing the JSON structure to capture all the revisions—updating the core problem to reference the new papers, refining the approach with sub-sentence detection and reduced scope, and adjusting the resource estimates accordingly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "040cce09-7b92-44c6-84bd-65ff93e4863a",
  "isSidechain": false,
  "requestId": "req_011Cb4WhNJQSvvCzmH9yoWb7",
  "type": "assistant",
  "uuid": "9f549f62-ea85-43a0-86c1-de11a070b3cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xri3W3iMxZw9VS73cQgWBU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1810,
      "cache_read_input_tokens": 43512,
      "output_tokens": 15810,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15810,
          "cache_read_input_tokens": 43512,
          "cache_creation_input_tokens": 1810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1810
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

_source line 71 · 2026-05-15T14:31:04.895Z_

I've now gathered detailed information on all flagged papers. Let me synthesize the findings:

- **O'Neill et al. (2507.23221)**: External observer model's linear probe detects contextual hallucinations on Gemma-2 2B–27B, with causal steering. Key difference from RaS: external observer (not self-probing), binary hallucination (not calibrated confidence), contextual (not long-form factual).
- **ConFix/CARE (Yuan et al., SIGIR 2025)**: Fact-level calibration + correction via high-confidence facts refining low-confidence ones. Inference-time, multi-pass post-hoc correction — different mechanism entirely from activation steering.
- **CAST (ICLR 2025)**: Condition vector + threshold determines when to apply behavior vector. Formula: h' ← h + f(sim(h, proj_c h)) · α · v. Conceptually close to probe-triggered steering.
- **Spherical Steering (ICML 2026)**: vMF confidence-gated rotation, +10% on TruthfulQA. Norm-preserving but tested on 7–8B models for truthfulness MCQ.
- **FLAS (May 2026)**: Flow-based learned velocity field, curved trajectories, Gemma-2 2B/9B on AxBench.

The sub-sentence steering latency is a real design flaw. Research confirms probe signals are detectable at hallucination onset (first tokens), supporting mid-claim intervention with a sliding window.

Now I'll compose the complete revised idea addressing all six issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f549f62-ea85-43a0-86c1-de11a070b3cd",
  "isSidechain": false,
  "requestId": "req_011Cb4WhNJQSvvCzmH9yoWb7",
  "type": "assistant",
  "uuid": "5b8f3f53-da21-47cf-8163-c540f9f45e7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xri3W3iMxZw9VS73cQgWBU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1810,
      "cache_read_input_tokens": 43512,
      "output_tokens": 15810,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15810,
          "cache_read_input_tokens": 43512,
          "cache_creation_input_tokens": 1810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1810
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

_source line 72 · 2026-05-15T14:34:53.061Z_

<details open><summary>🔧 Tool call — Write · `toolu_01VgkgiU6M4jueejfJzbcEuA`</summary>

```json
{
  "file_path": "/tmp/revised_idea.json",
  "content": "{\n  \"change_type\": \"minor\",\n  \"title\": \"Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation\",\n  \"core_problem\": \"LLMs generate long-form outputs where hallucinated claims are expressed with the same high confidence as factual ones. Existing approaches either detect hallucinations at claim level without calibrating expressed confidence (Han et al., EMNLP 2025 — binary probes + neuron clamping; O'Neill et al., July 2025 — external observer probe + binary steering), calibrate confidence only at response level for short-form QA (Ji et al., EMNLP 2025; Miao & Ungar, 2026; CORAL, 2026), perform fact-level calibration via post-hoc iterative correction rather than during generation (CARE, SIGIR 2025), use probe-guided steering without claim-level granularity or long-form scope (ITI, NeurIPS 2023; CLAS, 2026; ActCab/CoDec, EMNLP 2024), apply conditional or adaptive steering for behavioral control rather than calibrated confidence expression (CAST, ICLR 2025; Spherical Steering, ICML 2026; FLAS, 2026), or require multi-stage training of the base model (CURE, April 2026; CAG, May 2026; LoVeC, May 2025). No existing method performs claim-level calibrated uncertainty expression in long-form generation during a single forward pass without base model training. Furthermore, the accuracy-confidence orthogonality that enables clean steering (Miao & Ungar, 2026) has only been validated on 7–8B models for short-form QA — whether it holds at 70B scale in long-form generation is an open question with practical implications for the entire probe-guided steering paradigm.\",\n  \"opportunity\": \"Four recent results create a convergent opportunity: (1) Han et al. (EMNLP Findings 2025) showed lightweight linear probes on hidden states detect claim-level factuality in long-form generation, matching expensive multi-sample methods at up to 100× fewer FLOPs — but their neuron clamping intervention is binary (suppress/allow), not calibrated; (2) Miao & Ungar (March 2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features (cosine similarity < 0.04), meaning models internally know when they're wrong but fail to express this — and that adaptive CAA steering along these directions achieves major calibration improvement (ECE 14.9→3.7 on Llama-3.1-8B, 35.1→3.3 on Mistral-7B), but only for response-level QA on 7–8B models; (3) Kumaran et al. (March 2026) demonstrated that confidence representations are cached at answer-adjacent positions before verbalization, enabling real-time detection during generation — critically, their finding that hallucination signals emerge at the onset of hallucinated spans supports sub-sentence probe monitoring; (4) CLAS (April 2026) demonstrated that probe-derived adaptive steering works on models up to Llama 3.1-70B across 11 benchmarks, providing evidence that the steering mechanism scales — though not specifically for confidence calibration. Combining these — reading claim-level accuracy signals via probes during long-form generation, then steering verbalized confidence to match in real time — is unexplored and fills a specific gap. Critically, testing whether the accuracy-confidence orthogonality extends to 70B scale and long-form generation is itself a contribution that informs the feasibility of the entire probe-guided confidence steering paradigm.\",\n  \"landscape\": \"**Foundational probe→steer paradigm:** ITI (Li et al., NeurIPS 2023) introduced inference-time intervention: linear probes identify truthful directions in attention heads, and activations are shifted along these directions during generation. Foundational work, but targets truthfulness (content change) rather than calibrated confidence expression, and only on TruthfulQA.\\n\\n**Closest prior work — claim-level probing in long-form generation:** Han et al. (EMNLP Findings 2025) trained simple linear probes on LLM hidden states that detect claim-level hallucinations in long-form generation with performance matching expensive multi-sample methods (up to 100× fewer FLOPs), testing on models up to Llama 3.1-405B. Their neuron clamping causally reduces hallucinations by fixing activations of factuality-correlated neurons — but this is a binary intervention (suppress or allow) that does not produce calibrated verbal uncertainty expression. Obeso et al. (arXiv 2509.03531, 2025) trains entity-level probes for real-time streaming hallucination detection in long-form generation (AUC 0.90 on Llama-3.3-70B) — detection only, no calibrated steering.\\n\\n**Closest prior work — observer-model probe→steer for hallucinations:** O'Neill et al. (arXiv 2507.23221, July 2025) demonstrated that a generator-agnostic observer model can detect contextual hallucinations via a linear probe on its residual stream, isolating a single transferable direction that outperforms baselines by 5–27 points across Gemma-2 models (2B–27B), and that manipulating this direction causally steers generator hallucination rates. RaS differs on three axes: (a) self-probing rather than requiring an external observer model, eliminating the overhead of a second forward pass; (b) graded confidence calibration rather than binary hallucination detection/reduction — RaS produces proportionally hedged language, not just fewer hallucinations; (c) claim-level granularity in long-form factual generation rather than span-level detection in context-grounded settings.\\n\\n**Closest prior work — calibrated confidence steering:** Miao & Ungar (arXiv 2603.25052, March 2026) discovered that calibration accuracy and verbalized confidence are orthogonal linear features (cosine similarity < 0.04), and proposed two-stage adaptive CAA steering that reads internal accuracy and steers verbalized output to match, achieving ECE improvements from 14.9→3.7 (Llama-3.1-8B) and 35.1→3.3 (Mistral-7B) — but only for response-level short-form QA on 7–8B models. They explicitly acknowledge: 'Whether the linear encoding findings hold at larger scales remains open. Evaluation is restricted to question-answering tasks; extending to open-ended generation would require rethinking how the probe target is constructed.' Ji et al. (EMNLP 2025) discovered the Verbal Uncertainty Feature (VUF) and proposed MUC with ~30% reduction in confident hallucinations — also response-level, short-form, on ≤8B models.\\n\\n**Same-group prior work — CORAL:** CORAL (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) uses regularized MLP probes on residual activations to predict correctness and steers at inference time, achieving 10% accuracy and 50% ECE improvements. However, CORAL targets MCQA on 7B models with response-level steering — no claim-level decomposition or long-form generation. RaS differs in (a) claim-level granularity via factuality probes, (b) long-form generation scope, and (c) confidence expression calibration rather than answer correctness steering.\\n\\n**Fact-level calibration via iterative correction:** CARE (Yuan et al., SIGIR 2025) proposes fact-level confidence calibration for long-form generation, decomposing responses into atomic facts, estimating per-fact confidence, and using high-confidence facts to iteratively refine low-confidence ones via ConFix. CARE addresses the same problem space (fact-level calibration in long-form outputs) but via a fundamentally different mechanism: post-hoc multi-pass correction through prompting, rather than single-pass activation steering during generation. RaS operates within the forward pass with no regeneration, targets verbal confidence expression rather than factual correction, and requires no external confidence estimation pipeline.\\n\\n**Conditional and adaptive steering methods:** CAST (Arditi et al., ICLR 2025) introduced conditional activation steering where a PCA-derived condition vector determines whether to apply a behavior vector via thresholded cosine similarity: h' ← h + f(sim(h, proj_c h)) · α · v. CAST's 'if condition, then steer' paradigm is conceptually related to RaS's probe-triggered steering, but CAST uses a PCA-derived condition vector for behavioral categories (e.g., content moderation), while RaS uses a data-driven factuality probe score for continuous uncertainty calibration — the probe provides graded confidence estimates, not binary category membership. Spherical Steering (You et al., arXiv 2602.08169, February 2026; ICML 2026) replaces additive steering with norm-preserving geodesic rotation and uses a vMF-based confidence gate for input-adaptive strength, achieving +10% on TruthfulQA with Llama-3.1-8B — but targets truthfulness in MCQ rather than calibrated confidence expression in long-form generation. FLAS (Jin et al., arXiv 2605.05892, May 2026) learns a concept-conditioned velocity field enabling curved, multi-step trajectories through activation space, outperforming prompting on AxBench with Gemma-2 models — a more expressive steering mechanism than linear CAA, but tested only on small models (2B–9B) for general behavior control, not confidence calibration.\\n\\n**Activation calibration + guided decoding:** ActCab/CoDec (EMNLP 2024) trains a linear layer on LM last-layer activations for confidence calibration, then uses confidence-guided decoding to elicit truthful answers. Same conceptual pipeline (activation-based calibration → guided generation) but operates at response level on QA, and modifies decoding probabilities rather than verbalized confidence expression.\\n\\n**Adaptive steering strength:** CLAS (Hsu et al., arXiv 2604.24693, April 2026) introduces context-dependent linear activation steering where steering strength adapts via learned sensing vectors: α_ℓ,t = (c_ℓ · [h_ℓ,t, 1]). Tested on Llama-3.1-70B across 11 benchmarks, demonstrating that probe-derived adaptive steering scales to 70B. RaS's α = β × max(0, threshold − probe_score) adapts similarly but is driven by factuality probe scores per-claim rather than a general context sensing vector, and targets confidence calibration specifically.\\n\\n**Mechanistic understanding:** 'How do LLMs Compute Verbal Confidence?' (Kumaran et al., arXiv 2603.17839, March 2026) provides convergent evidence that confidence representations emerge at answer-adjacent positions via cached retrieval, supporting the feasibility of online detection during generation. Their finding that signals are cached before verbalization motivates sub-sentence probe monitoring.\\n\\n**Training-free steering baselines:** SteerConf (NeurIPS 2025) does prompt-based training-free confidence steering via multi-prompt aggregation. ACT (WWW 2025) applies tuning-free diverse steering vectors with adaptive intensity for truthfulness, scaling to 65B.\\n\\n**Claim-level long-form calibration (training-based):** CURE (arXiv 2604.12046, April 2026) uses multi-stage training to teach claim-level confidence reasoning, improving accuracy by up to 39.9%. CAG (arXiv 2605.01749, May 2026) achieves up to 13% factuality gain via training-based calibration-aware generation. LoVeC (arXiv 2505.23912, May 2025) uses RL to train LLMs to append on-the-fly confidence scores per statement in long-form generation, achieving 20× speedup over self-consistency methods. All three require base model fine-tuning or RL.\\n\\n**Post-generation claim-level approaches:** CSS (arXiv 2604.17487, April 2026) decomposes answers into claims and backs off uncertain ones using external verifiers. Selective Abstraction (arXiv 2602.11908, February 2026) replaces low-confidence atoms with confident abstractions.\\n\\n**Residual-stream anomaly detection:** PCNET (arXiv 2605.05953, May 2026) uses probabilistic circuits on residual streams for hallucination detection + contrastive decoding, reaching up to 99% AUROC — but targets short-form QA and changes content (different token selection) rather than expressing calibrated uncertainty.\\n\\n**Scaling concerns for activation steering:** Scaling laws for activation steering (ICML 2025) show that CAA effectiveness diminishes with model size on Llama 2 (7B→13B→70B) for behavioral steering (refusal). Endogenous steering resistance (arXiv 2602.06941, February 2026) shows Llama-3.3-70B has 3.8% ESR rate (vs <1% for smaller models). However, CLAS demonstrates successful probe-derived steering on Llama-3.1-70B, suggesting that adaptive, probe-guided steering may be more robust at scale than uniform CAA.\\n\\n**Gap:** No existing work combines claim-level factuality probing (à la Han et al.) with calibrated activation steering along the verbalized-confidence direction (à la Miao & Ungar) in a single-pass, online framework for long-form generation. O'Neill et al.'s probe→steer pipeline is closest structurally but uses an external observer for binary hallucination reduction rather than self-probing for graded confidence calibration. CARE addresses fact-level calibration in long-form outputs but via post-hoc correction rather than real-time activation steering. CAST provides conditional steering but for behavioral categories, not continuous confidence calibration. This intersection — reading internal accuracy per-claim and steering verbalized confidence to match during generation — is the contribution space. Additionally, no work has tested whether the accuracy-confidence orthogonality discovered at 7–8B scale holds at 70B or in long-form generation contexts, making this verification itself a contribution to the mechanistic understanding of confidence representations.\",\n  \"approach\": \"We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. The system reads internal accuracy signals per-claim via lightweight probes and steers verbalized confidence to match via targeted activation intervention, producing naturally hedged language for uncertain claims while leaving confident-and-correct claims untouched.\\n\\n**Pilot Experiment — Orthogonality Verification at Scale (~8h, 2× H100, first week):** Before committing the full experimental budget, we replicate Miao & Ungar's orthogonality analysis on Llama 3.1-70B in a long-form generation setting. We extract accuracy and confidence directions from biography-generation hidden states (not QA), measure their cosine similarity, and compare against the < 0.04 value found at 7–8B scale. This pilot has three outcomes: (a) orthogonality holds (cosine < 0.1) — proceed as planned, report the scaling result as a contribution; (b) orthogonality partially holds (cosine 0.1–0.3) — adapt steering to project out the accuracy component from the confidence direction before steering, proceed with modified approach; (c) orthogonality fails (cosine > 0.3) — report as an important negative finding about the limits of linear feature geometry at scale, fall back to the 8B-only configuration with reduced total compute (~80h). All three outcomes produce publishable results.\\n\\n**Offline Stage 1 — Factuality Probe Training (~20h wall on 2× H100 for 70B; ~4h on 1× H100 for 8B; one-time per model):** Generate long-form outputs (biographies, factual descriptions) from the target model, decompose into atomic claims using FActScore/OpenFActScore decomposition, verify claim factuality against knowledge sources. Extract hidden states at each claim's token span across multiple layers (following Han et al.'s layer-group methodology). Train lightweight linear probes (logistic regression on span-aggregated hidden states) to predict continuous factuality confidence scores. Unlike Han et al.'s binary factuality labels, we train on soft labels derived from verification confidence, enabling graded uncertainty estimation.\\n\\n**Offline Stage 2 — Verbalized-Confidence Direction Extraction (~included in Stage 1 compute; one-time per model):** Extract a verbalized-confidence steering direction via contrastive activation pairs: generate matched claim pairs where the same factual content is expressed with high confidence ('X was born in Y') vs. hedged uncertainty ('X was reportedly born in Y, though I am not certain'). The mean activation difference yields the steering direction, following the contrastive methodology from Ji et al. (VUF) and Miao & Ungar (CAA). For the 70B model, if the pilot reveals partial orthogonality degradation, we apply Gram-Schmidt orthogonalization to project the confidence direction away from the accuracy direction before use.\\n\\n**Online Stage — Sub-Sentence Probe-Guided Steering During Generation:** During autoregressive generation: (1) At each generated token, run the factuality probe on its hidden states — this is a single matrix-vector multiplication with negligible overhead (~0.001% of the forward pass). (2) Maintain a running exponential moving average (EMA) of probe scores over a sliding window of the last K tokens (default K=8), providing smoothed uncertainty estimates that avoid triggering on single noisy tokens while enabling sub-sentence response. (3) When the EMA drops below the calibrated threshold θ, immediately activate steering — even mid-sentence. This means RaS can begin hedging within the current claim by steering subsequent tokens toward uncertainty-expressing language (e.g., generating qualifiers like 'reportedly,' 'I believe,' or reformulations for the remaining tokens in the sentence). The steering magnitude follows the adaptive formula: α = β × max(0, θ − EMA_score), where β is calibrated on a held-out validation set. This adaptive formula is conceptually related to CAST's conditional steering (apply only when a condition is met) and CLAS's context-dependent steering, but driven by continuous per-claim factuality probe scores rather than PCA-derived category membership (CAST) or general context sensing vectors (CLAS). (4) Deactivate steering when the EMA recovers above threshold θ, indicating the model has returned to confident territory.\\n\\n**Steering latency analysis:** The sub-sentence trigger design means that in the best case, the probe detects uncertainty within the first few tokens of a claim (consistent with Kumaran et al.'s finding that confidence signals are cached at answer-adjacent positions and Obeso et al.'s evidence that hallucination signals are detectable at span onset), and steering activates mid-claim with ~K/2 token latency. We will empirically measure the distribution of steering activation timing relative to claim boundaries: what fraction of uncertain claims receive hedging (a) within the same sentence, (b) within K tokens, and (c) only in subsequent sentences. If probe signals rise early in claims as prior work suggests, mid-claim steering should be feasible for most uncertain claims. For claims where steering activates late, the output exhibits forward-looking uncertainty conditioning — subsequent generation is explicitly uncertainty-aware — which we acknowledge as a known tradeoff and measure empirically.\\n\\n**Key design choices addressing known limitations:** (a) Span-aggregated probe scores with EMA smoothing over K-token windows avoid single-token noise while enabling sub-sentence response — a substantial improvement over sentence-boundary-only evaluation. (b) Single-pass online monitoring eliminates the two-pass chicken-and-egg problem — no position-aligned regeneration needed. (c) Continuous calibrated steering (not binary neuron clamping) produces graded hedging proportional to internal uncertainty, distinguishing this from Han et al.'s binary intervention and O'Neill et al.'s binary hallucination steering. (d) Operating on the verbalized-confidence direction (orthogonal to accuracy per Miao & Ungar, verified at 70B scale in our pilot) means steering affects expression style without corrupting the model's factual knowledge. (e) Self-probing eliminates the need for an external observer model (unlike O'Neill et al.), keeping the framework single-pass with negligible compute overhead. (f) Adaptive steering magnitude based on probe-detected need may mitigate the diminishing effectiveness of uniform CAA at larger scales (ICML 2025 scaling laws), since steering is only applied where needed and at probe-calibrated intensity.\\n\\n**Models:** Llama 3.1-70B-Instruct as primary (standard dense transformer architecture, well-studied for probing and steering, large enough to test scaling of the orthogonality finding, with CLAS confirming probe-derived steering viability at this scale). Llama 3.1-8B-Instruct as lightweight sanity check (enables direct comparison with Miao & Ungar and Ji et al. baselines on the same model family, validates the pipeline in well-charted territory). Both models use standard transformer attention across all layers, avoiding the untested territory of hybrid DeltaNet architectures (e.g., Qwen 3.5) where linear probe and steering techniques lack validation.\\n\\n**Benchmarks:** FActScore (biography generation, primary) and LongFact (diverse long-form factuality). Metrics: claim-level ECE, Brier score (calibration quality), AUROC (uncertainty detection), FActScore/factual precision (to verify steering does not degrade content quality), MT-Bench fluency subset (to verify generation quality preservation), and steering latency distribution (fraction of uncertain claims hedged within-sentence vs. forward-conditioned). We also report the cosine similarity between accuracy and confidence directions at 70B scale as a standalone mechanistic finding.\\n\\n**Quantitative targets:** We expect RaS to achieve: (1) claim-level ECE reduction of ≥25% relative to unsteered baselines on both FActScore and LongFact (primary target), with ≥40% as a stretch goal — the primary target is conservative given that Miao & Ungar's response-level results (70–90% ECE reduction on QA) face additional challenges at claim-level granularity in long-form generation at 70B scale, including noisy claim boundary detection, probe signal dilution from long-context hidden states, and sub-sentence steering latency; (2) FActScore preservation within 2% of unsteered baseline (steering affects verbal expression, not factual content); (3) uncertainty detection AUROC ≥0.80 (probe-based); (4) superior calibration (lower ECE) compared to Han et al.'s binary neuron clamping at comparable or better FActScore; (5) ≥60% of uncertain claims receiving within-sentence hedging via sub-sentence triggers.\\n\\n**Comparisons (3 baselines):** (1) Unsteered baseline (cost: ~3h), (2) Han et al.'s probes + neuron clamping (closest representation-based method for long-form; cost: ~13h), (3) CURE (closest training-based method for claim-level calibration, if reproducible; cost: ~14h). We discuss but do not reimplement O'Neill et al. (external observer, different setting), CARE (post-hoc correction, different mechanism), and LoVeC (RL-based, high reproduction cost).\\n\\n**Ablations (3 core):** (1) Probe-only detection without steering (measures probe quality in isolation), (2) Uniform steering without probe guidance (constant steering magnitude — tests whether probe-adaptive steering outperforms naive uniform application), (3) Steering strength sensitivity (varying β and θ, including analysis of K-token window size impact on latency vs. signal quality tradeoff).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~195h H100 80GB (orthogonality pilot ~8h [2×H100], probe training + direction extraction ~24h [20h 70B on 2×H100, 4h 8B on 1×H100], Llama 3.1-70B evaluation on FActScore + LongFact ~85h [2×H100], Llama 3.1-8B sanity check ~12h [1×H100], baseline comparisons ~30h [unsteered ~3h, Han et al. ~13h, CURE ~14h], core ablations ×3 ~25h, debugging/rerun buffer ~11h)\",\n      \"gpu_utilization\": \"~25-35% effective — GPU idles during code development, pipeline debugging, and results analysis\",\n      \"timeline\": \"5-6 weeks (1 researcher full-time)\",\n      \"team\": \"1-2 researchers with mechanistic interpretability and activation steering experience\",\n      \"estimated_gpu_cost\": \"$490-680 (at ~$2.50-3.50/hr H100 80GB spot)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~170h H100 80GB (agent handles pipeline code, probe training iteration, evaluation scripting; human approves pilot results, probe design, steering threshold calibration, and ablation priorities)\",\n      \"gpu_utilization\": \"~50-65% — agent queues experiments between human check-ins\",\n      \"timeline\": \"3-4 weeks\",\n      \"team\": \"1 researcher, ~30min/day for methodology decisions, pilot outcome assessment, and qualitative hedging evaluation\",\n      \"claude_api_cost\": \"$100-200 (~1500-3000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$425-595\",\n      \"risk_note\": \"Primary risk: whether accuracy-confidence orthogonality holds at 70B scale in long-form generation — the ~8h pilot experiment validates this before committing the full budget. If orthogonality breaks (outcome c), we fall back to an 8B-only paper with the negative scaling result as a contribution, reducing total compute to ~70h H100. Secondary risk: whether sub-sentence probe-guided steering produces natural hedging at 70B or creates incoherent mid-sentence shifts — qualitative human assessment of hedging naturalness across K-token window sizes is essential. Tertiary risk: CAA effectiveness diminishing at 70B scale (per ICML 2025 scaling laws), though our adaptive probe-guided approach may be more robust than uniform steering.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~195h H100 80GB (agent explores probe architectures, layer selections, K-window sizes, steering schedules on 70B primary model with 8B sanity checks, plus evaluation)\",\n      \"gpu_utilization\": \"~80-90% — continuous experiment pipeline with minimal idle\",\n      \"timeline\": \"7-10 days with 2× H100 80GB\",\n      \"team\": \"0 researchers (initial setup + final review only)\",\n      \"claude_api_cost\": \"$200-400 (~3000-6000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$490-680\",\n      \"speed_bottleneck\": \"Long-form generation throughput on Llama 3.1-70B with 2× H100 tensor parallelism (~20-30 tok/s) — generating and evaluating hundreds of long-form responses per configuration is the computational bottleneck\",\n      \"risk_note\": \"Without human judgment, agent may over-optimize probe thresholds and K-window sizes on validation set rather than ensuring robustness, may miss qualitative assessment of hedging naturalness (mid-sentence steering coherence requires human evaluation), and critically may not correctly interpret the orthogonality pilot results (the decision to proceed vs. pivot requires understanding of the mechanistic implications)\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — ~10 weeks; conference Feb 16-23, Montréal) — PRIMARY\",\n    \"ARR August 2026 (submission Aug 3, 2026 — ~11 weeks; committable to EMNLP 2026 Oct 24-29 or later *ACL venues)\",\n    \"ICLR 2027 (expected submission ~Oct 2026, ~20 weeks; comfortable timeline)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation (Han et al., Findings of EMNLP 2025) — closest prior work: claim-level probes + neuron clamping in long-form generation\",\n    \"A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations (O'Neill et al., arXiv 2507.23221, July 2025) — closest probe→steer pipeline: external observer linear probe detects and steers hallucinations across Gemma-2 2B–27B; differs from RaS in using external observer (vs. self-probing), binary hallucination steering (vs. graded confidence calibration), and context-grounded settings (vs. long-form factual generation)\",\n    \"Closing the Confidence-Faithfulness Gap in LLMs (Miao & Ungar, arXiv 2603.25052, March 2026) — accuracy-confidence orthogonality discovery + adaptive CAA steering; explicitly notes scaling and long-form extension as open questions\",\n    \"Correctness-Optimized Residual Activation Lens [CORAL] (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) — same group; MLP probes → correctness steering on MCQA at 7B scale; must differentiate as response-level, short-form only\",\n    \"Fact-Level Calibration and Correction for Long-Form Generations [CARE/ConFix] (Yuan et al., SIGIR 2025; arXiv 2411.13343) — fact-level confidence calibration + iterative correction via high-confidence facts refining low-confidence ones; same problem space but fundamentally different mechanism (post-hoc multi-pass correction vs. single-pass activation steering)\",\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025) — VUF discovery and MUC for response-level short-form QA\",\n    \"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model [ITI] (Li et al., NeurIPS 2023) — foundational probe→steer paradigm using linear probes on attention heads for truthfulness\",\n    \"Programming Refusal with Conditional Activation Steering [CAST] (Arditi et al., ICLR 2025) — conditional steering via PCA-derived condition vectors with thresholded activation; conceptually related 'if condition, then steer' paradigm, but targets behavioral categories rather than continuous confidence calibration\",\n    \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., arXiv 2602.08169, February 2026; ICML 2026) — norm-preserving geodesic rotation with vMF confidence gating; +10% on TruthfulQA with Llama-3.1-8B; targets truthfulness MCQ, not calibrated confidence in long-form\",\n    \"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention [FLAS] (Jin et al., arXiv 2605.05892, May 2026) — learned concept-conditioned velocity field for curved activation trajectories; more expressive than linear CAA but tested on Gemma-2 2B–9B for general behavior control\",\n    \"Enhancing Language Model Factuality via Activation-Based Confidence Calibration and Guided Decoding [ActCab/CoDec] (EMNLP 2024) — activation calibration + confidence-guided decoding for QA factuality\",\n    \"Contextual Linear Activation Steering [CLAS] (Hsu et al., arXiv 2604.24693, April 2026) — probe-derived adaptive steering with context-dependent strength; tested on Llama-3.1-70B, confirming steering viability at 70B scale\",\n    \"How do LLMs Compute Verbal Confidence? (Kumaran et al., arXiv 2603.17839, March 2026) — mechanistic evidence for cached confidence retrieval at answer-adjacent positions; supports feasibility of sub-sentence probe monitoring\",\n    \"Reinforcement Learning for Better Verbalized Confidence in Long-Form Generation [LoVeC] (arXiv 2505.23912, May 2025) — RL-based on-the-fly confidence scoring per statement in long-form generation; training-based\",\n    \"Scaling Laws for Activation Steering with Llama 2 Models and Refusal Mechanisms (ICML 2025) — demonstrates CAA effectiveness diminishes with model size (7B→70B); informs our adaptive steering design\",\n    \"Endogenous Resistance to Activation Steering in Language Models (arXiv 2602.06941, February 2026) — Llama-3.3-70B shows 3.8% endogenous steering resistance; relevant scaling concern\",\n    \"Does Transformer Interpretability Transfer to RNNs? (2024) — probing and CAA partially transfer to recurrent architectures with reduced effectiveness; motivates our choice of standard transformer models\",\n    \"SteerConf: Steering LLMs for Confidence Elicitation (Zhou et al., NeurIPS 2025) — prompt-based training-free confidence calibration\",\n    \"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025) — diverse steering vectors with adaptive intensity control\",\n    \"Real-Time Detection of Hallucinated Entities in Long-Form Generation (Obeso et al., arXiv 2509.03531, 2025) — entity-level streaming probes for long-form generation; evidence that hallucination signals are detectable at span onset\",\n    \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits [PCNET] (arXiv 2605.05953, May 2026) — residual stream anomaly detection + contrastive decoding intervention\",\n    \"Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, January 2026) — online hallucination detection as evolving latent state\",\n    \"Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration [CURE] (arXiv 2604.12046, April 2026) — multi-stage training for claim-level confidence reasoning\",\n    \"Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality [CAG] (arXiv 2605.01749, May 2026) — training-based calibration-aware generation\",\n    \"Atomic Calibration of LLMs in Long-Form Generations (Findings of AACL-IJCNLP 2025) — showed poor claim-level calibration in long-form outputs\",\n    \"Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control [CSS] (arXiv 2604.17487, April 2026) — post-generation specificity control via external verifiers\",\n    \"When Should LLMs Be Less Specific? Selective Abstraction for Reliable Long-Form Text Generation (arXiv 2602.11908, February 2026)\",\n    \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs (ICML 2024) — linear probes approximate semantic entropy at response level\",\n    \"FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023)\",\n    \"Long-form Factuality in Large Language Models [LongFact/SAFE] (NeurIPS 2024)\",\n    \"Steering Language Models With Activation Engineering (Turner et al., arXiv 2308.10248, 2023)\"\n  ],\n  \"description\": \"We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. Motivated by two key findings — Han et al. (EMNLP 2025) showed lightweight probes detect claim-level factuality in long-form hidden states, and Miao & Ungar (2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features — RaS combines both insights in a novel way: it reads claim-level accuracy signals via factuality probes during autoregressive generation and steers verbalized confidence to match via targeted activation intervention along the orthogonal confidence direction, all within a single forward pass. A key design improvement is sub-sentence probe monitoring: rather than waiting for sentence boundaries, RaS evaluates an exponential moving average of probe scores every K tokens (K=8), enabling mid-claim steering activation when uncertainty is detected — consistent with evidence that hallucination signals emerge at span onset (Obeso et al., 2025) and that confidence representations are cached at answer-adjacent positions (Kumaran et al., 2026). Unlike O'Neill et al.'s probe→steer pipeline (which uses an external observer for binary hallucination reduction), RaS self-probes for graded confidence calibration with no second model. Unlike CARE (SIGIR 2025, which uses post-hoc iterative fact correction), RaS operates within the forward pass. Unlike Han et al.'s neuron clamping (binary suppression of hallucinations), RaS produces calibrated verbal hedging proportional to the model's internal uncertainty. Unlike CURE, CAG, and LoVeC, it requires no base model training — only lightweight linear probe fitting and contrastive direction extraction. The probe-guided adaptive steering formula (α = β × max(0, θ − EMA_score)) relates to CAST's conditional steering (ICLR 2025) and CLAS's context-dependent steering but is driven by continuous per-claim factuality signals rather than PCA-derived condition vectors or general context sensing. The framework includes a dedicated pilot experiment verifying the accuracy-confidence orthogonality at 70B scale in long-form generation — extending Miao & Ungar's finding beyond the 7–8B QA setting where it was established. We evaluate on Llama 3.1-70B (primary, testing scaling) and Llama 3.1-8B (sanity check, direct comparison with prior work) using FActScore and LongFact, measuring claim-level ECE, Brier score, AUROC, factual precision, and steering latency distribution. We target ≥25% claim-level ECE reduction (conservatively discounted from Miao & Ungar's 70–90% response-level QA results, given additional challenges of claim-level granularity, long-form generation, and 70B scale), with ≥40% as a stretch goal, while preserving FActScore within 2%. All experiments fit within ~195 H100-hours.\",\n  \"project_name\": \"probe_guided_claim_calibration\",\n  \"source\": \"web_research\"\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b8f3f53-da21-47cf-8163-c540f9f45e7a",
  "isSidechain": false,
  "requestId": "req_011Cb4WhNJQSvvCzmH9yoWb7",
  "type": "assistant",
  "uuid": "b4ed6717-be9d-4686-ae31-ca8cbf8dc430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xri3W3iMxZw9VS73cQgWBU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1810,
      "cache_read_input_tokens": 43512,
      "output_tokens": 15810,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15810,
          "cache_read_input_tokens": 43512,
          "cache_creation_input_tokens": 1810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1810
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

_source line 73 · 2026-05-15T14:34:53.076Z_

<details><summary>↩ Tool result · reported error · `toolu_01VgkgiU6M4jueejfJzbcEuA`</summary>

```text
Claude requested permissions to write to /tmp/revised_idea.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4ed6717-be9d-4686-ae31-ca8cbf8dc430",
  "isSidechain": false,
  "promptId": "341f4af0-8fe7-4307-8328-fe863851ecd4",
  "type": "user",
  "uuid": "9573c968-cd07-42ba-8e85-957eef2ea526",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_idea.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "b4ed6717-be9d-4686-ae31-ca8cbf8dc430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 74 · 2026-05-15T14:34:53.081Z_

```json
{
  "parentUuid": "9573c968-cd07-42ba-8e85-957eef2ea526",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a235d5f7-5695-4a44-9caa-538447d70946",
  "timestamp": "2026-05-15T14:34:53.081Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 75_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-15 (UTC).**  ## Original idea {   \"title\": \"Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Lo…",
  "leafUuid": "a235d5f7-5695-4a44-9caa-538447d70946",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

### Runtime record

_source line 76_

```json
{
  "type": "ai-title",
  "aiTitle": "Claim-level confidence calibration in long-form generation via steering",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

### Assistant

_source line 77 · 2026-05-15T14:38:28.845Z_

Here is the complete revised idea as JSON, addressing all six reviewer issues:

```json
{
  "change_type": "minor",
  "title": "Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation",
  "core_problem": "LLMs generate long-form outputs where hallucinated claims are expressed with the same high confidence as factual ones. Existing approaches either detect hallucinations at claim level without calibrating expressed confidence (Han et al., EMNLP 2025 — binary probes + neuron clamping; O'Neill et al., July 2025 — external observer probe + binary steering), calibrate confidence only at response level for short-form QA (Ji et al., EMNLP 2025; Miao & Ungar, 2026; CORAL, 2026), perform fact-level calibration via post-hoc iterative correction rather than during generation (CARE, SIGIR 2025), use probe-guided steering without claim-level granularity or long-form scope (ITI, NeurIPS 2023; CLAS, 2026; ActCab/CoDec, EMNLP 2024), apply conditional or adaptive steering for behavioral control rather than calibrated confidence expression (CAST, ICLR 2025; Spherical Steering, ICML 2026; FLAS, 2026), or require multi-stage training of the base model (CURE, April 2026; CAG, May 2026; LoVeC, May 2025). No existing method performs claim-level calibrated uncertainty expression in long-form generation during a single forward pass without base model training. Furthermore, the accuracy-confidence orthogonality that enables clean steering (Miao & Ungar, 2026) has only been validated on 7–8B models for short-form QA — whether it holds at 70B scale in long-form generation is an open question with practical implications for the entire probe-guided steering paradigm.",
  "opportunity": "Four recent results create a convergent opportunity: (1) Han et al. (EMNLP Findings 2025) showed lightweight linear probes on hidden states detect claim-level factuality in long-form generation, matching expensive multi-sample methods at up to 100× fewer FLOPs — but their neuron clamping intervention is binary (suppress/allow), not calibrated; (2) Miao & Ungar (March 2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features (cosine similarity < 0.04), meaning models internally know when they're wrong but fail to express this — and that adaptive CAA steering along these directions achieves major calibration improvement (ECE 14.9→3.7 on Llama-3.1-8B, 35.1→3.3 on Mistral-7B), but only for response-level QA on 7–8B models; (3) Kumaran et al. (March 2026) demonstrated that confidence representations are cached at answer-adjacent positions before verbalization, enabling real-time detection during generation — critically, their finding that hallucination signals emerge at the onset of hallucinated spans supports sub-sentence probe monitoring; (4) CLAS (April 2026) demonstrated that probe-derived adaptive steering works on models up to Llama 3.1-70B across 11 benchmarks, providing evidence that the steering mechanism scales — though not specifically for confidence calibration. Combining these — reading claim-level accuracy signals via probes during long-form generation, then steering verbalized confidence to match in real time — is unexplored and fills a specific gap. Critically, testing whether the accuracy-confidence orthogonality extends to 70B scale and long-form generation is itself a contribution that informs the feasibility of the entire probe-guided confidence steering paradigm.",
  "landscape": "**Foundational probe→steer paradigm:** ITI (Li et al., NeurIPS 2023) introduced inference-time intervention: linear probes identify truthful directions in attention heads, and activations are shifted along these directions during generation. Foundational work, but targets truthfulness (content change) rather than calibrated confidence expression, and only on TruthfulQA.\n\n**Closest prior work — claim-level probing in long-form generation:** Han et al. (EMNLP Findings 2025) trained simple linear probes on LLM hidden states that detect claim-level hallucinations in long-form generation with performance matching expensive multi-sample methods (up to 100× fewer FLOPs), testing on models up to Llama 3.1-405B. Their neuron clamping causally reduces hallucinations by fixing activations of factuality-correlated neurons — but this is a binary intervention (suppress or allow) that does not produce calibrated verbal uncertainty expression. Obeso et al. (arXiv 2509.03531, 2025) trains entity-level probes for real-time streaming hallucination detection in long-form generation (AUC 0.90 on Llama-3.3-70B) — detection only, no calibrated steering.\n\n**Closest prior work — observer-model probe→steer for hallucinations:** O'Neill et al. (arXiv 2507.23221, July 2025) demonstrated that a generator-agnostic observer model can detect contextual hallucinations via a linear probe on its residual stream, isolating a single transferable direction that outperforms baselines by 5–27 points across Gemma-2 models (2B–27B), and that manipulating this direction causally steers generator hallucination rates. RaS differs on three axes: (a) self-probing rather than requiring an external observer model, eliminating the overhead of a second forward pass; (b) graded confidence calibration rather than binary hallucination detection/reduction — RaS produces proportionally hedged language, not just fewer hallucinations; (c) claim-level granularity in long-form factual generation rather than span-level detection in context-grounded settings.\n\n**Closest prior work — calibrated confidence steering:** Miao & Ungar (arXiv 2603.25052, March 2026) discovered that calibration accuracy and verbalized confidence are orthogonal linear features (cosine similarity < 0.04), and proposed two-stage adaptive CAA steering that reads internal accuracy and steers verbalized output to match, achieving ECE improvements from 14.9→3.7 (Llama-3.1-8B) and 35.1→3.3 (Mistral-7B) — but only for response-level short-form QA on 7–8B models. They explicitly acknowledge: 'Whether the linear encoding findings hold at larger scales remains open. Evaluation is restricted to question-answering tasks; extending to open-ended generation would require rethinking how the probe target is constructed.' Ji et al. (EMNLP 2025) discovered the Verbal Uncertainty Feature (VUF) and proposed MUC with ~30% reduction in confident hallucinations — also response-level, short-form, on ≤8B models.\n\n**Same-group prior work — CORAL:** CORAL (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) uses regularized MLP probes on residual activations to predict correctness and steers at inference time, achieving 10% accuracy and 50% ECE improvements. However, CORAL targets MCQA on 7B models with response-level steering — no claim-level decomposition or long-form generation. RaS differs in (a) claim-level granularity via factuality probes, (b) long-form generation scope, and (c) confidence expression calibration rather than answer correctness steering.\n\n**Fact-level calibration via iterative correction:** CARE (Yuan et al., SIGIR 2025; arXiv 2411.13343) proposes fact-level confidence calibration for long-form generation, decomposing responses into atomic facts, estimating per-fact confidence, and using high-confidence facts to iteratively refine low-confidence ones via ConFix. CARE addresses the same problem space (fact-level calibration in long-form outputs) but via a fundamentally different mechanism: post-hoc multi-pass correction through prompting, rather than single-pass activation steering during generation. RaS operates within the forward pass with no regeneration, targets verbal confidence expression rather than factual correction, and requires no external confidence estimation pipeline.\n\n**Conditional and adaptive steering methods:** CAST (Arditi et al., ICLR 2025) introduced conditional activation steering where a PCA-derived condition vector determines whether to apply a behavior vector via thresholded cosine similarity: h' ← h + f(sim(h, proj_c h)) · α · v. CAST's 'if condition, then steer' paradigm is conceptually related to RaS's probe-triggered steering, but CAST uses a PCA-derived condition vector for behavioral categories (e.g., content moderation), while RaS uses a data-driven factuality probe score for continuous uncertainty calibration — the probe provides graded confidence estimates, not binary category membership. Spherical Steering (You et al., arXiv 2602.08169, February 2026; ICML 2026) replaces additive steering with norm-preserving geodesic rotation and uses a vMF-based confidence gate for input-adaptive strength, achieving +10% on TruthfulQA with Llama-3.1-8B — but targets truthfulness in MCQ rather than calibrated confidence expression in long-form generation. FLAS (Jin et al., arXiv 2605.05892, May 2026) learns a concept-conditioned velocity field enabling curved, multi-step trajectories through activation space, outperforming prompting on AxBench with Gemma-2 models — a more expressive steering mechanism than linear CAA, but tested only on small models (2B–9B) for general behavior control, not confidence calibration.\n\n**Activation calibration + guided decoding:** ActCab/CoDec (EMNLP 2024) trains a linear layer on LM last-layer activations for confidence calibration, then uses confidence-guided decoding to elicit truthful answers. Same conceptual pipeline (activation-based calibration → guided generation) but operates at response level on QA, and modifies decoding probabilities rather than verbalized confidence expression.\n\n**Adaptive steering strength:** CLAS (Hsu et al., arXiv 2604.24693, April 2026) introduces context-dependent linear activation steering where steering strength adapts via learned sensing vectors: α_ℓ,t = (c_ℓ · [h_ℓ,t, 1]). Tested on Llama-3.1-70B across 11 benchmarks, demonstrating that probe-derived adaptive steering scales to 70B. RaS's α = β × max(0, threshold − probe_score) adapts similarly but is driven by factuality probe scores per-claim rather than a general context sensing vector, and targets confidence calibration specifically.\n\n**Mechanistic understanding:** 'How do LLMs Compute Verbal Confidence?' (Kumaran et al., arXiv 2603.17839, March 2026) provides convergent evidence that confidence representations emerge at answer-adjacent positions via cached retrieval, supporting the feasibility of online detection during generation. Their finding that signals are cached before verbalization motivates sub-sentence probe monitoring.\n\n**Training-free steering baselines:** SteerConf (NeurIPS 2025) does prompt-based training-free confidence steering via multi-prompt aggregation. ACT (WWW 2025) applies tuning-free diverse steering vectors with adaptive intensity for truthfulness, scaling to 65B.\n\n**Claim-level long-form calibration (training-based):** CURE (arXiv 2604.12046, April 2026) uses multi-stage training to teach claim-level confidence reasoning, improving accuracy by up to 39.9%. CAG (arXiv 2605.01749, May 2026) achieves up to 13% factuality gain via training-based calibration-aware generation. LoVeC (arXiv 2505.23912, May 2025) uses RL to train LLMs to append on-the-fly confidence scores per statement in long-form generation, achieving 20× speedup over self-consistency methods. All three require base model fine-tuning or RL.\n\n**Post-generation claim-level approaches:** CSS (arXiv 2604.17487, April 2026) decomposes answers into claims and backs off uncertain ones using external verifiers. Selective Abstraction (arXiv 2602.11908, February 2026) replaces low-confidence atoms with confident abstractions.\n\n**Residual-stream anomaly detection:** PCNET (arXiv 2605.05953, May 2026) uses probabilistic circuits on residual streams for hallucination detection + contrastive decoding, reaching up to 99% AUROC — but targets short-form QA and changes content (different token selection) rather than expressing calibrated uncertainty.\n\n**Scaling concerns for activation steering:** Scaling laws for activation steering (ICML 2025) show that CAA effectiveness diminishes with model size on Llama 2 (7B→13B→70B) for behavioral steering (refusal). Endogenous steering resistance (arXiv 2602.06941, February 2026) shows Llama-3.3-70B has 3.8% ESR rate (vs <1% for smaller models). However, CLAS demonstrates successful probe-derived steering on Llama-3.1-70B, suggesting that adaptive, probe-guided steering may be more robust at scale than uniform CAA.\n\n**Gap:** No existing work combines claim-level factuality probing (à la Han et al.) with calibrated activation steering along the verbalized-confidence direction (à la Miao & Ungar) in a single-pass, online framework for long-form generation. O'Neill et al.'s probe→steer pipeline is closest structurally but uses an external observer for binary hallucination reduction rather than self-probing for graded confidence calibration. CARE addresses fact-level calibration in long-form outputs but via post-hoc correction rather than real-time activation steering. CAST provides conditional steering but for behavioral categories, not continuous confidence calibration. This intersection — reading internal accuracy per-claim and steering verbalized confidence to match during generation — is the contribution space. Additionally, no work has tested whether the accuracy-confidence orthogonality discovered at 7–8B scale holds at 70B or in long-form generation contexts, making this verification itself a contribution to the mechanistic understanding of confidence representations.",
  "approach": "We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. The system reads internal accuracy signals per-claim via lightweight probes and steers verbalized confidence to match via targeted activation intervention, producing naturally hedged language for uncertain claims while leaving confident-and-correct claims untouched.\n\n**Pilot Experiment — Orthogonality Verification at Scale (~8h, 2× H100, first week):** Before committing the full experimental budget, we replicate Miao & Ungar's orthogonality analysis on Llama 3.1-70B in a long-form generation setting. We extract accuracy and confidence directions from biography-generation hidden states (not QA), measure their cosine similarity, and compare against the < 0.04 value found at 7–8B scale. This pilot has three outcomes: (a) orthogonality holds (cosine < 0.1) — proceed as planned, report the scaling result as a contribution; (b) orthogonality partially holds (cosine 0.1–0.3) — adapt steering to project out the accuracy component from the confidence direction before steering, proceed with modified approach; (c) orthogonality fails (cosine > 0.3) — report as an important negative finding about the limits of linear feature geometry at scale, fall back to the 8B-only configuration with reduced total compute (~70h). All three outcomes produce publishable results.\n\n**Offline Stage 1 — Factuality Probe Training (~20h wall on 2× H100 for 70B; ~4h on 1× H100 for 8B; one-time per model):** Generate long-form outputs (biographies, factual descriptions) from the target model, decompose into atomic claims using FActScore/OpenFActScore decomposition, verify claim factuality against knowledge sources. Extract hidden states at each claim's token span across multiple layers (following Han et al.'s layer-group methodology). Train lightweight linear probes (logistic regression on span-aggregated hidden states) to predict continuous factuality confidence scores. Unlike Han et al.'s binary factuality labels, we train on soft labels derived from verification confidence, enabling graded uncertainty estimation.\n\n**Offline Stage 2 — Verbalized-Confidence Direction Extraction (included in Stage 1 compute; one-time per model):** Extract a verbalized-confidence steering direction via contrastive activation pairs: generate matched claim pairs where the same factual content is expressed with high confidence ('X was born in Y') vs. hedged uncertainty ('X was reportedly born in Y, though I am not certain'). The mean activation difference yields the steering direction, following the contrastive methodology from Ji et al. (VUF) and Miao & Ungar (CAA). For the 70B model, if the pilot reveals partial orthogonality degradation, we apply Gram-Schmidt orthogonalization to project the confidence direction away from the accuracy direction before use.\n\n**Online Stage — Sub-Sentence Probe-Guided Steering During Generation:** During autoregressive generation: (1) At each generated token, run the factuality probe on its hidden states — this is a single matrix-vector multiplication with negligible overhead (~0.001% of the forward pass). (2) Maintain a running exponential moving average (EMA) of probe scores over a sliding window of the last K tokens (default K=8), providing smoothed uncertainty estimates that avoid triggering on single noisy tokens while enabling sub-sentence response. (3) When the EMA drops below the calibrated threshold θ, immediately activate steering — even mid-sentence. This means RaS can begin hedging within the current claim by steering subsequent tokens toward uncertainty-expressing language (e.g., generating qualifiers like 'reportedly,' 'I believe,' or reformulations for the remaining tokens in the sentence). The steering magnitude follows the adaptive formula: α = β × max(0, θ − EMA_score), where β is calibrated on a held-out validation set. This adaptive formula is conceptually related to CAST's conditional steering (apply only when a condition is met) and CLAS's context-dependent steering, but driven by continuous per-claim factuality probe scores rather than PCA-derived category membership (CAST) or general context sensing vectors (CLAS). (4) Deactivate steering when the EMA recovers above threshold θ, indicating the model has returned to confident territory.\n\n**Steering latency analysis:** The sub-sentence trigger design means that in the best case, the probe detects uncertainty within the first few tokens of a claim (consistent with Kumaran et al.'s finding that confidence signals are cached at answer-adjacent positions and Obeso et al.'s evidence that hallucination signals are detectable at span onset), and steering activates mid-claim with ~K/2 token latency. We will empirically measure the distribution of steering activation timing relative to claim boundaries: what fraction of uncertain claims receive hedging (a) within the same sentence, (b) within K tokens, and (c) only in subsequent sentences. If probe signals rise early in claims as prior work suggests, mid-claim steering should be feasible for most uncertain claims. For claims where steering activates late, the output exhibits forward-looking uncertainty conditioning — subsequent generation is explicitly uncertainty-aware — which we acknowledge as a known tradeoff and measure empirically.\n\n**Key design choices addressing known limitations:** (a) EMA-smoothed probe scores over K-token windows avoid single-token noise while enabling sub-sentence response — a substantial improvement over sentence-boundary-only evaluation. (b) Single-pass online monitoring eliminates the two-pass chicken-and-egg problem — no position-aligned regeneration needed. (c) Continuous calibrated steering (not binary neuron clamping) produces graded hedging proportional to internal uncertainty, distinguishing this from Han et al.'s binary intervention and O'Neill et al.'s binary hallucination steering. (d) Operating on the verbalized-confidence direction (orthogonal to accuracy per Miao & Ungar, verified at 70B scale in our pilot) means steering affects expression style without corrupting the model's factual knowledge. (e) Self-probing eliminates the need for an external observer model (unlike O'Neill et al.), keeping the framework single-pass with negligible compute overhead. (f) Adaptive steering magnitude based on probe-detected need may mitigate the diminishing effectiveness of uniform CAA at larger scales (ICML 2025 scaling laws), since steering is only applied where needed and at probe-calibrated intensity.\n\n**Models:** Llama 3.1-70B-Instruct as primary (standard dense transformer architecture, well-studied for probing and steering, large enough to test scaling of the orthogonality finding, with CLAS confirming probe-derived steering viability at this scale). Llama 3.1-8B-Instruct as lightweight sanity check (enables direct comparison with Miao & Ungar and Ji et al. baselines on the same model family, validates the pipeline in well-charted territory). Both models use standard transformer attention across all layers, avoiding the untested territory of hybrid DeltaNet architectures (e.g., Qwen 3.5) where linear probe and steering techniques lack validation.\n\n**Benchmarks:** FActScore (biography generation, primary) and LongFact (diverse long-form factuality). Metrics: claim-level ECE, Brier score (calibration quality), AUROC (uncertainty detection), FActScore/factual precision (to verify steering does not degrade content quality), MT-Bench fluency subset (to verify generation quality preservation), and steering latency distribution (fraction of uncertain claims hedged within-sentence vs. forward-conditioned). We also report the cosine similarity between accuracy and confidence directions at 70B scale as a standalone mechanistic finding.\n\n**Quantitative targets:** We expect RaS to achieve: (1) claim-level ECE reduction of ≥25% relative to unsteered baselines on both FActScore and LongFact (primary target), with ≥40% as a stretch goal — the primary target is conservative given that Miao & Ungar's response-level results (70–90% ECE reduction on QA) face additional challenges at claim-level granularity in long-form generation at 70B scale, including noisy claim boundary detection, probe signal dilution from long-context hidden states, and sub-sentence steering latency; (2) FActScore preservation within 2% of unsteered baseline (steering affects verbal expression, not factual content); (3) uncertainty detection AUROC ≥0.80 (probe-based); (4) superior calibration (lower ECE) compared to Han et al.'s binary neuron clamping at comparable or better FActScore; (5) ≥60% of uncertain claims receiving within-sentence hedging via sub-sentence triggers.\n\n**Comparisons (3 baselines):** (1) Unsteered baseline (cost: ~3h), (2) Han et al.'s probes + neuron clamping (closest representation-based method for long-form; cost: ~13h), (3) CURE (closest training-based method for claim-level calibration, if reproducible; cost: ~14h). We discuss but do not reimplement O'Neill et al. (external observer, different setting), CARE (post-hoc correction, different mechanism), and LoVeC (RL-based, high reproduction cost).\n\n**Ablations (3 core):** (1) Probe-only detection without steering (measures probe quality in isolation), (2) Uniform steering without probe guidance (constant steering magnitude — tests whether probe-adaptive steering outperforms naive uniform application), (3) Steering strength sensitivity (varying β, θ, and K-token window size — analyzes latency vs. signal quality tradeoff).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~195h H100 80GB (orthogonality pilot ~8h [2×H100], probe training + direction extraction ~24h [20h 70B on 2×H100, 4h 8B on 1×H100], Llama 3.1-70B evaluation on FActScore + LongFact ~85h [2×H100], Llama 3.1-8B sanity check ~12h [1×H100], baseline comparisons ~30h [unsteered ~3h, Han et al. ~13h, CURE ~14h], core ablations ×3 ~25h, debugging/rerun buffer ~11h)",
      "gpu_utilization": "~25-35% effective — GPU idles during code development, pipeline debugging, and results analysis",
      "timeline": "5-6 weeks (1 researcher full-time)",
      "team": "1-2 researchers with mechanistic interpretability and activation steering experience",
      "estimated_gpu_cost": "$490-680 (at ~$2.50-3.50/hr H100 80GB spot)"
    },
    "human_in_loop": {
      "gpu_hours": "~170h H100 80GB (agent handles pipeline code, probe training iteration, evaluation scripting; human approves pilot results, probe design, steering threshold calibration, and ablation priorities)",
      "gpu_utilization": "~50-65% — agent queues experiments between human check-ins",
      "timeline": "3-4 weeks",
      "team": "1 researcher, ~30min/day for methodology decisions, pilot outcome assessment, and qualitative hedging evaluation",
      "claude_api_cost": "$100-200 (~1500-3000 Opus turns)",
      "estimated_gpu_cost": "$425-595",
      "risk_note": "Primary risk: whether accuracy-confidence orthogonality holds at 70B scale in long-form generation — the ~8h pilot experiment validates this before committing the full budget. If orthogonality breaks (outcome c), we fall back to an 8B-only paper with the negative scaling result as a contribution, reducing total compute to ~70h H100. Secondary risk: whether sub-sentence probe-guided steering produces natural hedging at 70B or creates incoherent mid-sentence shifts — qualitative human assessment of hedging naturalness across K-token window sizes is essential. Tertiary risk: CAA effectiveness diminishing at 70B scale (per ICML 2025 scaling laws), though our adaptive probe-guided approach may be more robust than uniform steering."
    },
    "auto_research": {
      "gpu_hours": "~195h H100 80GB (agent explores probe architectures, layer selections, K-window sizes, steering schedules on 70B primary model with 8B sanity checks, plus evaluation)",
      "gpu_utilization": "~80-90% — continuous experiment pipeline with minimal idle",
      "timeline": "7-10 days with 2× H100 80GB",
      "team": "0 researchers (initial setup + final review only)",
      "claude_api_cost": "$200-400 (~3000-6000 Opus turns)",
      "estimated_gpu_cost": "$490-680",
      "speed_bottleneck": "Long-form generation throughput on Llama 3.1-70B with 2× H100 tensor parallelism (~20-30 tok/s) — generating and evaluating hundreds of long-form responses per configuration is the computational bottleneck",
      "risk_note": "Without human judgment, agent may over-optimize probe thresholds and K-window sizes on validation set rather than ensuring robustness, may miss qualitative assessment of hedging naturalness (mid-sentence steering coherence requires human evaluation), and critically may not correctly interpret the orthogonality pilot results (the decision to proceed vs. pivot requires understanding of the mechanistic implications)"
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — ~10 weeks; conference Feb 16-23, Montréal) — PRIMARY",
    "ARR August 2026 (submission Aug 3, 2026 — ~11 weeks; committable to EMNLP 2026 Oct 24-29 or later *ACL venues)",
    "ICLR 2027 (expected submission ~Oct 2026, ~20 weeks; comfortable timeline)"
  ],
  "level": "solid",
  "key_references": [
    "Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation (Han et al., Findings of EMNLP 2025) — closest prior work: claim-level probes + neuron clamping in long-form generation",
    "A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations (O'Neill et al., arXiv 2507.23221, July 2025) — closest probe→steer pipeline: external observer linear probe detects and steers hallucinations across Gemma-2 2B–27B; differs from RaS in using external observer (vs. self-probing), binary hallucination steering (vs. graded confidence calibration), and context-grounded settings (vs. long-form factual generation)",
    "Closing the Confidence-Faithfulness Gap in LLMs (Miao & Ungar, arXiv 2603.25052, March 2026) — accuracy-confidence orthogonality discovery + adaptive CAA steering; explicitly notes scaling and long-form extension as open questions",
    "Correctness-Optimized Residual Activation Lens [CORAL] (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) — same group; MLP probes → correctness steering on MCQA at 7B scale; must differentiate as response-level, short-form only",
    "Fact-Level Calibration and Correction for Long-Form Generations [CARE/ConFix] (Yuan et al., SIGIR 2025; arXiv 2411.13343) — fact-level confidence calibration + iterative correction via high-confidence facts refining low-confidence ones; same problem space but fundamentally different mechanism (post-hoc multi-pass correction vs. single-pass activation steering)",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025) — VUF discovery and MUC for response-level short-form QA",
    "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model [ITI] (Li et al., NeurIPS 2023) — foundational probe→steer paradigm using linear probes on attention heads for truthfulness",
    "Programming Refusal with Conditional Activation Steering [CAST] (Arditi et al., ICLR 2025) — conditional steering via PCA-derived condition vectors with thresholded activation; conceptually related 'if condition, then steer' paradigm, but targets behavioral categories rather than continuous confidence calibration",
    "Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., arXiv 2602.08169, February 2026; ICML 2026) — norm-preserving geodesic rotation with vMF confidence gating; +10% on TruthfulQA with Llama-3.1-8B; targets truthfulness MCQ, not calibrated confidence in long-form",
    "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention [FLAS] (Jin et al., arXiv 2605.05892, May 2026) — learned concept-conditioned velocity field for curved activation trajectories; more expressive than linear CAA but tested on Gemma-2 2B–9B for general behavior control",
    "Enhancing Language Model Factuality via Activation-Based Confidence Calibration and Guided Decoding [ActCab/CoDec] (EMNLP 2024) — activation calibration + confidence-guided decoding for QA factuality",
    "Contextual Linear Activation Steering [CLAS] (Hsu et al., arXiv 2604.24693, April 2026) — probe-derived adaptive steering with context-dependent strength; tested on Llama-3.1-70B, confirming steering viability at 70B scale",
    "How do LLMs Compute Verbal Confidence? (Kumaran et al., arXiv 2603.17839, March 2026) — mechanistic evidence for cached confidence retrieval at answer-adjacent positions; supports feasibility of sub-sentence probe monitoring",
    "Reinforcement Learning for Better Verbalized Confidence in Long-Form Generation [LoVeC] (arXiv 2505.23912, May 2025) — RL-based on-the-fly confidence scoring per statement in long-form generation; training-based",
    "Scaling Laws for Activation Steering with Llama 2 Models and Refusal Mechanisms (ICML 2025) — demonstrates CAA effectiveness diminishes with model size (7B→70B); informs our adaptive steering design",
    "Endogenous Resistance to Activation Steering in Language Models (arXiv 2602.06941, February 2026) — Llama-3.3-70B shows 3.8% endogenous steering resistance; relevant scaling concern",
    "Does Transformer Interpretability Transfer to RNNs? (2024) — probing and CAA partially transfer to recurrent architectures with reduced effectiveness; motivates our choice of standard transformer models",
    "SteerConf: Steering LLMs for Confidence Elicitation (Zhou et al., NeurIPS 2025) — prompt-based training-free confidence calibration",
    "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025) — diverse steering vectors with adaptive intensity control",
    "Real-Time Detection of Hallucinated Entities in Long-Form Generation (Obeso et al., arXiv 2509.03531, 2025) — entity-level streaming probes for long-form generation; evidence that hallucination signals are detectable at span onset",
    "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits [PCNET] (arXiv 2605.05953, May 2026) — residual stream anomaly detection + contrastive decoding intervention",
    "Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, January 2026) — online hallucination detection as evolving latent state",
    "Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration [CURE] (arXiv 2604.12046, April 2026) — multi-stage training for claim-level confidence reasoning",
    "Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality [CAG] (arXiv 2605.01749, May 2026) — training-based calibration-aware generation",
    "Atomic Calibration of LLMs in Long-Form Generations (Findings of AACL-IJCNLP 2025) — showed poor claim-level calibration in long-form outputs",
    "Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control [CSS] (arXiv 2604.17487, April 2026) — post-generation specificity control via external verifiers",
    "When Should LLMs Be Less Specific? Selective Abstraction for Reliable Long-Form Text Generation (arXiv 2602.11908, February 2026)",
    "Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs (ICML 2024) — linear probes approximate semantic entropy at response level",
    "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023)",
    "Long-form Factuality in Large Language Models [LongFact/SAFE] (NeurIPS 2024)",
    "Steering Language Models With Activation Engineering (Turner et al., arXiv 2308.10248, 2023)"
  ],
  "description": "We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. Motivated by two key findings — Han et al. (EMNLP 2025) showed lightweight probes detect claim-level factuality in long-form hidden states, and Miao & Ungar (2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features — RaS combines both insights in a novel way: it reads claim-level accuracy signals via factuality probes during autoregressive generation and steers verbalized confidence to match via targeted activation intervention along the orthogonal confidence direction, all within a single forward pass. A key design improvement is sub-sentence probe monitoring: rather than waiting for sentence boundaries, RaS evaluates an exponential moving average of probe scores every K tokens (K=8), enabling mid-claim steering activation when uncertainty is detected — consistent with evidence that hallucination signals emerge at span onset (Obeso et al., 2025) and that confidence representations are cached at answer-adjacent positions (Kumaran et al., 2026). Unlike O'Neill et al.'s probe→steer pipeline (which uses an external observer for binary hallucination reduction), RaS self-probes for graded confidence calibration with no second model. Unlike CARE (SIGIR 2025, which uses post-hoc iterative fact correction), RaS operates within the forward pass. Unlike Han et al.'s neuron clamping (binary suppression of hallucinations), RaS produces calibrated verbal hedging proportional to the model's internal uncertainty. Unlike CURE, CAG, and LoVeC, it requires no base model training — only lightweight linear probe fitting and contrastive direction extraction. The probe-guided adaptive steering formula (α = β × max(0, θ − EMA_score)) relates to CAST's conditional steering (ICLR 2025) and CLAS's context-dependent steering but is driven by continuous per-claim factuality signals rather than PCA-derived condition vectors or general context sensing. The framework includes a dedicated pilot experiment verifying the accuracy-confidence orthogonality at 70B scale in long-form generation — extending Miao & Ungar's finding beyond the 7–8B QA setting where it was established. We evaluate on Llama 3.1-70B (primary, testing scaling) and Llama 3.1-8B (sanity check, direct comparison with prior work) using FActScore and LongFact, measuring claim-level ECE, Brier score, AUROC, factual precision, and steering latency distribution. We target ≥25% claim-level ECE reduction (conservatively discounted from Miao & Ungar's 70–90% response-level QA results, given additional challenges of claim-level granularity, long-form generation, and 70B scale), with ≥40% as a stretch goal, while preserving FActScore within 2%. All experiments fit within ~195 H100-hours.",
  "project_name": "probe_guided_claim_calibration",
  "source": "web_research"
}
```

---

**Summary of changes addressing each reviewer issue:**

1. **Compute ≤200h** — Reduced to ~195h H100 by: downgrading 8B from full validation to sanity check (25h→12h), trimming ablations from 5 to 3 core (38h→25h), tightening baselines to 3 (45h→30h), and adding an 11h debug buffer. HIL mode at ~170h.

2. **O'Neill et al. + CARE cited** — O'Neill et al. gets a dedicated landscape section with three-axis differentiation (self-probing vs. observer, graded vs. binary, long-form vs. contextual). CARE/ConFix (Yuan et al., SIGIR 2025) gets its own section differentiating post-hoc multi-pass correction from single-pass activation steering.

3. **Steering latency fixed (sub-sentence triggers)** — Replaced sentence-boundary evaluation with EMA-smoothed probe scores over K-token sliding windows (K=8), enabling mid-claim steering activation. Added explicit steering latency analysis: empirically measuring the fraction of uncertain claims hedged within-sentence vs. forward-conditioned. Motivated by Kumaran et al.'s cached-retrieval finding and Obeso et al.'s evidence that hallucination signals appear at span onset.

4. **Targets tempered** — Primary ECE reduction target lowered from ≥40% to ≥25%, with ≥40% as a stretch goal. Explicit rationale for the discount: claim-level granularity, long-form generation, 70B scale, and sub-sentence latency challenges.

5. **CAST discussed** — Added dedicated paragraph in landscape section comparing CAST's PCA-derived condition vector for behavioral categories vs. RaS's data-driven factuality probe for continuous uncertainty calibration. Also added Spherical Steering (ICML 2026) and FLAS (May 2026) for completeness.

6. **New metric** — Added "≥60% within-sentence hedging rate" as target (5), and steering latency distribution as a reported metric.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a235d5f7-5695-4a44-9caa-538447d70946",
  "isSidechain": false,
  "requestId": "req_011Cb4XAM2GNYHwrqEaScnE8",
  "type": "assistant",
  "uuid": "475a172c-6681-444b-a93b-9b747fafd690",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnsapKR8RRpYHvyzmRvX7V",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15947,
      "cache_read_input_tokens": 45322,
      "output_tokens": 9982,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15947,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9982,
          "cache_read_input_tokens": 45322,
          "cache_creation_input_tokens": 15947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15947
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

_source line 78_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-15 (UTC).**  ## Original idea {   \"title\": \"Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Lo…",
  "leafUuid": "475a172c-6681-444b-a93b-9b747fafd690",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Claim-level confidence calibration in long-form generation via steering",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

### Runtime record

_source line 80_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-15 (UTC).**  ## Original idea {   \"title\": \"Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Lo…",
  "leafUuid": "475a172c-6681-444b-a93b-9b747fafd690",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "ai-title",
  "aiTitle": "Claim-level confidence calibration in long-form generation via steering",
  "sessionId": "a802c1f0-a070-4179-b6b1-b61559232c83"
}
```

---
