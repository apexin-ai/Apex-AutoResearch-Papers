# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Read and Steer: Probe-Guided Clai

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/229ceea7-2481-45c0-9011-ca8f5c9ddaac.jsonl`
- **Structured JSON:** [`c2f17798153ea2997ddc.json`](../../sessions/c2/c2f17798153ea2997ddc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T01:48:40.206Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T01:48:40.206Z",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation\n\n**状态**: 待审阅  \n**级别**: top-tier  \n**创建时间**: 2026-05-15T15:11:55.979393+00:00\n\n## 描述\nWe propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. Motivated by two key findings — Han et al. (EMNLP 2025) showed lightweight probes detect claim-level factuality in long-form hidden states, and Miao & Ungar (2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features — RaS combines both insights in a novel way: it reads claim-level accuracy signals via factuality probes during autoregressive generation and steers verbalized confidence to match via targeted activation intervention along the orthogonal confidence direction, all within a single forward pass. A key design improvement is sub-sentence probe monitoring: rather than waiting for sentence boundaries, RaS evaluates an exponential moving average of probe scores every K tokens (K=8), enabling mid-claim steering activation when uncertainty is detected — consistent with evidence that hallucination signals emerge at span onset (Obeso et al., 2025) and that confidence representations are cached at answer-adjacent positions (Kumaran et al., 2026). Unlike O'Neill et al.'s probe→steer pipeline (which uses an external observer for binary hallucination reduction), RaS self-probes for graded confidence calibration with no second model. Unlike CARE (SIGIR 2025, which uses post-hoc iterative fact correction), RaS operates within the forward pass. Unlike Han et al.'s neuron clamping (binary suppression of hallucinations), RaS produces calibrated verbal hedging proportional to the model's internal uncertainty. Unlike CURE, CAG, and LoVeC, it requires no base model training — only lightweight linear probe fitting and contrastive direction extraction. The probe-guided adaptive steering formula (α = β × max(0, θ − EMA_score)) relates to CAST's conditional steering (ICLR 2025) and CLAS's context-dependent steering but is driven by continuous per-claim factuality signals rather than PCA-derived condition vectors or general context sensing. The framework includes a dedicated pilot experiment verifying the accuracy-confidence orthogonality at 70B scale in long-form generation — extending Miao & Ungar's finding beyond the 7–8B QA setting where it was established. We evaluate on Llama 3.1-70B (primary, testing scaling) and Llama 3.1-8B (sanity check, direct comparison with prior work) using FActScore and LongFact, measuring claim-level ECE, Brier score, AUROC, factual precision, and steering latency distribution. We target ≥25% claim-level ECE reduction (conservatively discounted from Miao & Ungar's 70–90% response-level QA results, given additional challenges of claim-level granularity, long-form generation, and 70B scale), with ≥40% as a stretch goal, while preserving FActScore within 2%. All experiments fit within ~195 H100-hours.\n\n## 核心问题\nLLMs generate long-form outputs where hallucinated claims are expressed with the same high confidence as factual ones. Existing approaches either detect hallucinations at claim level without calibrating expressed confidence (Han et al., EMNLP 2025 — binary probes + neuron clamping; O'Neill et al., July 2025 — external observer probe + binary steering), calibrate confidence only at response level for short-form QA (Ji et al., EMNLP 2025; Miao & Ungar, 2026; CORAL, 2026), perform fact-level calibration via post-hoc iterative correction rather than during generation (CARE, SIGIR 2025), use probe-guided steering without claim-level granularity or long-form scope (ITI, NeurIPS 2023; CLAS, 2026; ActCab/CoDec, EMNLP 2024), apply conditional or adaptive steering for behavioral control rather than calibrated confidence expression (CAST, ICLR 2025; Spherical Steering, ICML 2026; FLAS, 2026), or require multi-stage training of the base model (CURE, April 2026; CAG, May 2026; LoVeC, May 2025). No existing method performs claim-level calibrated uncertainty expression in long-form generation during a single forward pass without base model training. Furthermore, the accuracy-confidence orthogonality that enables clean steering (Miao & Ungar, 2026) has only been validated on 7–8B models for short-form QA — whether it holds at 70B scale in long-form generation is an open question with practical implications for the entire probe-guided steering paradigm.\n\n## 机遇 / Why Now\nFour recent results create a convergent opportunity: (1) Han et al. (EMNLP Findings 2025) showed lightweight linear probes on hidden states detect claim-level factuality in long-form generation, matching expensive multi-sample methods at up to 100× fewer FLOPs — but their neuron clamping intervention is binary (suppress/allow), not calibrated; (2) Miao & Ungar (March 2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features (cosine similarity < 0.04), meaning models internally know when they're wrong but fail to express this — and that adaptive CAA steering along these directions achieves major calibration improvement (ECE 14.9→3.7 on Llama-3.1-8B, 35.1→3.3 on Mistral-7B), but only for response-level QA on 7–8B models; (3) Kumaran et al. (March 2026) demonstrated that confidence representations are cached at answer-adjacent positions before verbalization, enabling real-time detection during generation — critically, their finding that hallucination signals emerge at the onset of hallucinated spans supports sub-sentence probe monitoring; (4) CLAS (April 2026) demonstrated that probe-derived adaptive steering works on models up to Llama 3.1-70B across 11 benchmarks, providing evidence that the steering mechanism scales — though not specifically for confidence calibration. Combining these — reading claim-level accuracy signals via probes during long-form generation, then steering verbalized confidence to match in real time — is unexplored and fills a specific gap. Critically, testing whether the accuracy-confidence orthogonality extends to 70B scale and long-form generation is itself a contribution that informs the feasibility of the entire probe-guided confidence steering paradigm.\n\n## 方法思路\nWe propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. The system reads internal accuracy signals per-claim via lightweight probes and steers verbalized confidence to match via targeted activation intervention, producing naturally hedged language for uncertain claims while leaving confident-and-correct claims untouched.\n\n**Pilot Experiment — Orthogonality Verification at Scale (~8h, 2× H100, first week):** Before committing the full experimental budget, we replicate Miao & Ungar's orthogonality analysis on Llama 3.1-70B in a long-form generation setting. We extract accuracy and confidence directions from biography-generation hidden states (not QA), measure their cosine similarity, and compare against the < 0.04 value found at 7–8B scale. This pilot has three outcomes: (a) orthogonality holds (cosine < 0.1) — proceed as planned, report the scaling result as a contribution; (b) orthogonality partially holds (cosine 0.1–0.3) — adapt steering to project out the accuracy component from the confidence direction before steering, proceed with modified approach; (c) orthogonality fails (cosine > 0.3) — report as an important negative finding about the limits of linear feature geometry at scale, fall back to the 8B-only configuration with reduced total compute (~70h). All three outcomes produce publishable results.\n\n**Offline Stage 1 — Factuality Probe Training (~20h wall on 2× H100 for 70B; ~4h on 1× H100 for 8B; one-time per model):** Generate long-form outputs (biographies, factual descriptions) from the target model, decompose into atomic claims using FActScore/OpenFActScore decomposition, verify claim factuality against knowledge sources. Extract hidden states at each claim's token span across multiple layers (following Han et al.'s layer-group methodology). Train lightweight linear probes (logistic regression on span-aggregated hidden states) to predict continuous factuality confidence scores. Unlike Han et al.'s binary factuality labels, we train on soft labels derived from verification confidence, enabling graded uncertainty estimation.\n\n**Offline Stage 2 — Verbalized-Confidence Direction Extraction (included in Stage 1 compute; one-time per model):** Extract a verbalized-confidence steering direction via contrastive activation pairs: generate matched claim pairs where the same factual content is expressed with high confidence ('X was born in Y') vs. hedged uncertainty ('X was reportedly born in Y, though I am not certain'). The mean activation difference yields the steering direction, following the contrastive methodology from Ji et al. (VUF) and Miao & Ungar (CAA). For the 70B model, if the pilot reveals partial orthogonality degradation, we apply Gram-Schmidt orthogonalization to project the confidence direction away from the accuracy direction before use.\n\n**Online Stage — Sub-Sentence Probe-Guided Steering During Generation:** During autoregressive generation: (1) At each generated token, run the factuality probe on its hidden states — this is a single matrix-vector multiplication with negligible overhead (~0.001% of the forward pass). (2) Maintain a running exponential moving average (EMA) of probe scores over a sliding window of the last K tokens (default K=8), providing smoothed uncertainty estimates that avoid triggering on single noisy tokens while enabling sub-sentence response. (3) When the EMA drops below the calibrated threshold θ, immediately activate steering — even mid-sentence. This means RaS can begin hedging within the current claim by steering subsequent tokens toward uncertainty-expressing language (e.g., generating qualifiers like 'reportedly,' 'I believe,' or reformulations for the remaining tokens in the sentence). The steering magnitude follows the adaptive formula: α = β × max(0, θ − EMA_score), where β is calibrated on a held-out validation set. This adaptive formula is conceptually related to CAST's conditional steering (apply only when a condition is met) and CLAS's context-dependent steering, but driven by continuous per-claim factuality probe scores rather than PCA-derived category membership (CAST) or general context sensing vectors (CLAS). (4) Deactivate steering when the EMA recovers above threshold θ, indicating the model has returned to confident territory.\n\n**Steering latency analysis:** The sub-sentence trigger design means that in the best case, the probe detects uncertainty within the first few tokens of a claim (consistent with Kumaran et al.'s finding that confidence signals are cached at answer-adjacent positions and Obeso et al.'s evidence that hallucination signals are detectable at span onset), and steering activates mid-claim with ~K/2 token latency. We will empirically measure the distribution of steering activation timing relative to claim boundaries: what fraction of uncertain claims receive hedging (a) within the same sentence, (b) within K tokens, and (c) only in subsequent sentences. If probe signals rise early in claims as prior work suggests, mid-claim steering should be feasible for most uncertain claims. For claims where steering activates late, the output exhibits forward-looking uncertainty conditioning — subsequent generation is explicitly uncertainty-aware — which we acknowledge as a known tradeoff and measure empirically.\n\n**Key design choices addressing known limitations:** (a) EMA-smoothed probe scores over K-token windows avoid single-token noise while enabling sub-sentence response — a substantial improvement over sentence-boundary-only evaluation. (b) Single-pass online monitoring eliminates the two-pass chicken-and-egg problem — no position-aligned regeneration needed. (c) Continuous calibrated steering (not binary neuron clamping) produces graded hedging proportional to internal uncertainty, distinguishing this from Han et al.'s binary intervention and O'Neill et al.'s binary hallucination steering. (d) Operating on the verbalized-confidence direction (orthogonal to accuracy per Miao & Ungar, verified at 70B scale in our pilot) means steering affects expression style without corrupting the model's factual knowledge. (e) Self-probing eliminates the need for an external observer model (unlike O'Neill et al.), keeping the framework single-pass with negligible compute overhead. (f) Adaptive steering magnitude based on probe-detected need may mitigate the diminishing effectiveness of uniform CAA at larger scales (ICML 2025 scaling laws), since steering is only applied where needed and at probe-calibrated intensity.\n\n**Models:** Llama 3.1-70B-Instruct as primary (standard dense transformer architecture, well-studied for probing and steering, large enough to test scaling of the orthogonality finding, with CLAS confirming probe-derived steering viability at this scale). Llama 3.1-8B-Instruct as lightweight sanity check (enables direct comparison with Miao & Ungar and Ji et al. baselines on the same model family, validates the pipeline in well-charted territory). Both models use standard transformer attention across all layers, avoiding the untested territory of hybrid DeltaNet architectures (e.g., Qwen 3.5) where linear probe and steering techniques lack validation.\n\n**Benchmarks:** FActScore (biography generation, primary) and LongFact (diverse long-form factuality). Metrics: claim-level ECE, Brier score (calibration quality), AUROC (uncertainty detection), FActScore/factual precision (to verify steering does not degrade content quality), MT-Bench fluency subset (to verify generation quality preservation), and steering latency distribution (fraction of uncertain claims hedged within-sentence vs. forward-conditioned). We also report the cosine similarity between accuracy and confidence directions at 70B scale as a standalone mechanistic finding.\n\n**Quantitative targets:** We expect RaS to achieve: (1) claim-level ECE reduction of ≥25% relative to unsteered baselines on both FActScore and LongFact (primary target), with ≥40% as a stretch goal — the primary target is conservative given that Miao & Ungar's response-level results (70–90% ECE reduction on QA) face additional challenges at claim-level granularity in long-form generation at 70B scale, including noisy claim boundary detection, probe signal dilution from long-context hidden states, and sub-sentence steering latency; (2) FActScore preservation within 2% of unsteered baseline (steering affects verbal expression, not factual content); (3) uncertainty detection AUROC ≥0.80 (probe-based); (4) superior calibration (lower ECE) compared to Han et al.'s binary neuron clamping at comparable or better FActScore; (5) ≥60% of uncertain claims receiving within-sentence hedging via sub-sentence triggers.\n\n**Comparisons (3 baselines):** (1) Unsteered baseline (cost: ~3h), (2) Han et al.'s probes + neuron clamping (closest representation-based method for long-form; cost: ~13h), (3) CURE (closest training-based method for claim-level calibration, if reproducible; cost: ~14h). We discuss but do not reimplement O'Neill et al. (external observer, different setting), CARE (post-hoc correction, different mechanism), and LoVeC (RL-based, high reproduction cost).\n\n**Ablations (3 core):** (1) Probe-only detection without steering (measures probe quality in isolation), (2) Uniform steering without probe guidance (constant steering magnitude — tests whether probe-adaptive steering outperforms naive uniform application), (3) Steering strength sensitivity (varying β, θ, and K-token window size — analyzes latency vs. signal quality tradeoff).\n\n## 研究现状\n**Foundational probe→steer paradigm:** ITI (Li et al., NeurIPS 2023) introduced inference-time intervention: linear probes identify truthful directions in attention heads, and activations are shifted along these directions during generation. Foundational work, but targets truthfulness (content change) rather than calibrated confidence expression, and only on TruthfulQA.\n\n**Closest prior work — claim-level probing in long-form generation:** Han et al. (EMNLP Findings 2025) trained simple linear probes on LLM hidden states that detect claim-level hallucinations in long-form generation with performance matching expensive multi-sample methods (up to 100× fewer FLOPs), testing on models up to Llama 3.1-405B. Their neuron clamping causally reduces hallucinations by fixing activations of factuality-correlated neurons — but this is a binary intervention (suppress or allow) that does not produce calibrated verbal uncertainty expression. Obeso et al. (arXiv 2509.03531, 2025) trains entity-level probes for real-time streaming hallucination detection in long-form generation (AUC 0.90 on Llama-3.3-70B) — detection only, no calibrated steering.\n\n**Closest prior work — observer-model probe→steer for hallucinations:** O'Neill et al. (arXiv 2507.23221, July 2025) demonstrated that a generator-agnostic observer model can detect contextual hallucinations via a linear probe on its residual stream, isolating a single transferable direction that outperforms baselines by 5–27 points across Gemma-2 models (2B–27B), and that manipulating this direction causally steers generator hallucination rates. RaS differs on three axes: (a) self-probing rather than requiring an external observer model, eliminating the overhead of a second forward pass; (b) graded confidence calibration rather than binary hallucination detection/reduction — RaS produces proportionally hedged language, not just fewer hallucinations; (c) claim-level granularity in long-form factual generation rather than span-level detection in context-grounded settings.\n\n**Closest prior work — calibrated confidence steering:** Miao & Ungar (arXiv 2603.25052, March 2026) discovered that calibration accuracy and verbalized confidence are orthogonal linear features (cosine similarity < 0.04), and proposed two-stage adaptive CAA steering that reads internal accuracy and steers verbalized output to match, achieving ECE improvements from 14.9→3.7 (Llama-3.1-8B) and 35.1→3.3 (Mistral-7B) — but only for response-level short-form QA on 7–8B models. They explicitly acknowledge: 'Whether the linear encoding findings hold at larger scales remains open. Evaluation is restricted to question-answering tasks; extending to open-ended generation would require rethinking how the probe target is constructed.' Ji et al. (EMNLP 2025) discovered the Verbal Uncertainty Feature (VUF) and proposed MUC with ~30% reduction in confident hallucinations — also response-level, short-form, on ≤8B models.\n\n**Same-group prior work — CORAL:** CORAL (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) uses regularized MLP probes on residual activations to predict correctness and steers at inference time, achieving 10% accuracy and 50% ECE improvements. However, CORAL targets MCQA on 7B models with response-level steering — no claim-level decomposition or long-form generation. RaS differs in (a) claim-level granularity via factuality probes, (b) long-form generation scope, and (c) confidence expression calibration rather than answer correctness steering.\n\n**Fact-level calibration via iterative correction:** CARE (Yuan et al., SIGIR 2025; arXiv 2411.13343) proposes fact-level confidence calibration for long-form generation, decomposing responses into atomic facts, estimating per-fact confidence, and using high-confidence facts to iteratively refine low-confidence ones via ConFix. CARE addresses the same problem space (fact-level calibration in long-form outputs) but via a fundamentally different mechanism: post-hoc multi-pass correction through prompting, rather than single-pass activation steering during generation. RaS operates within the forward pass with no regeneration, targets verbal confidence expression rather than factual correction, and requires no external confidence estimation pipeline.\n\n**Conditional and adaptive steering methods:** CAST (Arditi et al., ICLR 2025) introduced conditional activation steering where a PCA-derived condition vector determines whether to apply a behavior vector via thresholded cosine similarity: h' ← h + f(sim(h, proj_c h)) · α · v. CAST's 'if condition, then steer' paradigm is conceptually related to RaS's probe-triggered steering, but CAST uses a PCA-derived condition vector for behavioral categories (e.g., content moderation), while RaS uses a data-driven factuality probe score for continuous uncertainty calibration — the probe provides graded confidence estimates, not binary category membership. Spherical Steering (You et al., arXiv 2602.08169, February 2026; ICML 2026) replaces additive steering with norm-preserving geodesic rotation and uses a vMF-based confidence gate for input-adaptive strength, achieving +10% on TruthfulQA with Llama-3.1-8B — but targets truthfulness in MCQ rather than calibrated confidence expression in long-form generation. FLAS (Jin et al., arXiv 2605.05892, May 2026) learns a concept-conditioned velocity field enabling curved, multi-step trajectories through activation space, outperforming prompting on AxBench with Gemma-2 models — a more expressive steering mechanism than linear CAA, but tested only on small models (2B–9B) for general behavior control, not confidence calibration.\n\n**Activation calibration + guided decoding:** ActCab/CoDec (EMNLP 2024) trains a linear layer on LM last-layer activations for confidence calibration, then uses confidence-guided decoding to elicit truthful answers. Same conceptual pipeline (activation-based calibration → guided generation) but operates at response level on QA, and modifies decoding probabilities rather than verbalized confidence expression.\n\n**Adaptive steering strength:** CLAS (Hsu et al., arXiv 2604.24693, April 2026) introduces context-dependent linear activation steering where steering strength adapts via learned sensing vectors: α_ℓ,t = (c_ℓ · [h_ℓ,t, 1]). Tested on Llama-3.1-70B across 11 benchmarks, demonstrating that probe-derived adaptive steering scales to 70B. RaS's α = β × max(0, threshold − probe_score) adapts similarly but is driven by factuality probe scores per-claim rather than a general context sensing vector, and targets confidence calibration specifically.\n\n**Mechanistic understanding:** 'How do LLMs Compute Verbal Confidence?' (Kumaran et al., arXiv 2603.17839, March 2026) provides convergent evidence that confidence representations emerge at answer-adjacent positions via cached retrieval, supporting the feasibility of online detection during generation. Their finding that signals are cached before verbalization motivates sub-sentence probe monitoring.\n\n**Training-free steering baselines:** SteerConf (NeurIPS 2025) does prompt-based training-free confidence steering via multi-prompt aggregation. ACT (WWW 2025) applies tuning-free diverse steering vectors with adaptive intensity for truthfulness, scaling to 65B.\n\n**Claim-level long-form calibration (training-based):** CURE (arXiv 2604.12046, April 2026) uses multi-stage training to teach claim-level confidence reasoning, improving accuracy by up to 39.9%. CAG (arXiv 2605.01749, May 2026) achieves up to 13% factuality gain via training-based calibration-aware generation. LoVeC (arXiv 2505.23912, May 2025) uses RL to train LLMs to append on-the-fly confidence scores per statement in long-form generation, achieving 20× speedup over self-consistency methods. All three require base model fine-tuning or RL.\n\n**Post-generation claim-level approaches:** CSS (arXiv 2604.17487, April 2026) decomposes answers into claims and backs off uncertain ones using external verifiers. Selective Abstraction (arXiv 2602.11908, February 2026) replaces low-confidence atoms with confident abstractions.\n\n**Residual-stream anomaly detection:** PCNET (arXiv 2605.05953, May 2026) uses probabilistic circuits on residual streams for hallucination detection + contrastive decoding, reaching up to 99% AUROC — but targets short-form QA and changes content (different token selection) rather than expressing calibrated uncertainty.\n\n**Scaling concerns for activation steering:** Scaling laws for activation steering (ICML 2025) show that CAA effectiveness diminishes with model size on Llama 2 (7B→13B→70B) for behavioral steering (refusal). Endogenous steering resistance (arXiv 2602.06941, February 2026) shows Llama-3.3-70B has 3.8% ESR rate (vs <1% for smaller models). However, CLAS demonstrates successful probe-derived steering on Llama-3.1-70B, suggesting that adaptive, probe-guided steering may be more robust at scale than uniform CAA.\n\n**Gap:** No existing work combines claim-level factuality probing (à la Han et al.) with calibrated activation steering along the verbalized-confidence direction (à la Miao & Ungar) in a single-pass, online framework for long-form generation. O'Neill et al.'s probe→steer pipeline is closest structurally but uses an external observer for binary hallucination reduction rather than self-probing for graded confidence calibration. CARE addresses fact-level calibration in long-form outputs but via post-hoc correction rather than real-time activation steering. CAST provides conditional steering but for behavioral categories, not continuous confidence calibration. This intersection — reading internal accuracy per-claim and steering verbalized confidence to match during generation — is the contribution space. Additionally, no work has tested whether the accuracy-confidence orthogonality discovered at 7–8B scale holds at 70B or in long-form generation contexts, making this verification itself a contribution to the mechanistic understanding of confidence representations.\n\n## 目标 Venue\n- AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — ~10 weeks; conference Feb 16-23, Montréal) — PRIMARY\n- ARR August 2026 (submission Aug 3, 2026 — ~11 weeks; committable to EMNLP 2026 Oct 24-29 or later *ACL venues)\n- ICLR 2027 (expected submission ~Oct 2026, ~20 weeks; comfortable timeline)\n\n## 关键参考\n- Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation (Han et al., Findings of EMNLP 2025) — closest prior work: claim-level probes + neuron clamping in long-form generation\n- A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations (O'Neill et al., arXiv 2507.23221, July 2025) — closest probe→steer pipeline: external observer linear probe detects and steers hallucinations across Gemma-2 2B–27B; differs from RaS in using external observer (vs. self-probing), binary hallucination steering (vs. graded confidence calibration), and context-grounded settings (vs. long-form factual generation)\n- Closing the Confidence-Faithfulness Gap in LLMs (Miao & Ungar, arXiv 2603.25052, March 2026) — accuracy-confidence orthogonality discovery + adaptive CAA steering; explicitly notes scaling and long-form extension as open questions\n- Correctness-Optimized Residual Activation Lens [CORAL] (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) — same group; MLP probes → correctness steering on MCQA at 7B scale; must differentiate as response-level, short-form only\n- Fact-Level Calibration and Correction for Long-Form Generations [CARE/ConFix] (Yuan et al., SIGIR 2025; arXiv 2411.13343) — fact-level confidence calibration + iterative correction via high-confidence facts refining low-confidence ones; same problem space but fundamentally different mechanism (post-hoc multi-pass correction vs. single-pass activation steering)\n- Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025) — VUF discovery and MUC for response-level short-form QA\n- Inference-Time Intervention: Eliciting Truthful Answers from a Language Model [ITI] (Li et al., NeurIPS 2023) — foundational probe→steer paradigm using linear probes on attention heads for truthfulness\n- Programming Refusal with Conditional Activation Steering [CAST] (Arditi et al., ICLR 2025) — conditional steering via PCA-derived condition vectors with thresholded activation; conceptually related 'if condition, then steer' paradigm, but targets behavioral categories rather than continuous confidence calibration\n- Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., arXiv 2602.08169, February 2026; ICML 2026) — norm-preserving geodesic rotation with vMF confidence gating; +10% on TruthfulQA with Llama-3.1-8B; targets truthfulness MCQ, not calibrated confidence in long-form\n- Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention [FLAS] (Jin et al., arXiv 2605.05892, May 2026) — learned concept-conditioned velocity field for curved activation trajectories; more expressive than linear CAA but tested on Gemma-2 2B–9B for general behavior control\n- Enhancing Language Model Factuality via Activation-Based Confidence Calibration and Guided Decoding [ActCab/CoDec] (EMNLP 2024) — activation calibration + confidence-guided decoding for QA factuality\n- Contextual Linear Activation Steering [CLAS] (Hsu et al., arXiv 2604.24693, April 2026) — probe-derived adaptive steering with context-dependent strength; tested on Llama-3.1-70B, confirming steering viability at 70B scale\n- How do LLMs Compute Verbal Confidence? (Kumaran et al., arXiv 2603.17839, March 2026) — mechanistic evidence for cached confidence retrieval at answer-adjacent positions; supports feasibility of sub-sentence probe monitoring\n- Reinforcement Learning for Better Verbalized Confidence in Long-Form Generation [LoVeC] (arXiv 2505.23912, May 2025) — RL-based on-the-fly confidence scoring per statement in long-form generation; training-based\n- Scaling Laws for Activation Steering with Llama 2 Models and Refusal Mechanisms (ICML 2025) — demonstrates CAA effectiveness diminishes with model size (7B→70B); informs our adaptive steering design\n- Endogenous Resistance to Activation Steering in Language Models (arXiv 2602.06941, February 2026) — Llama-3.3-70B shows 3.8% endogenous steering resistance; relevant scaling concern\n- Does Transformer Interpretability Transfer to RNNs? (2024) — probing and CAA partially transfer to recurrent architectures with reduced effectiveness; motivates our choice of standard transformer models\n- SteerConf: Steering LLMs for Confidence Elicitation (Zhou et al., NeurIPS 2025) — prompt-based training-free confidence calibration\n- Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025) — diverse steering vectors with adaptive intensity control\n- Real-Time Detection of Hallucinated Entities in Long-Form Generation (Obeso et al., arXiv 2509.03531, 2025) — entity-level streaming probes for long-form generation; evidence that hallucination signals are detectable at span onset\n- Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits [PCNET] (arXiv 2605.05953, May 2026) — residual stream anomaly detection + contrastive decoding intervention\n- Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, January 2026) — online hallucination detection as evolving latent state\n- Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration [CURE] (arXiv 2604.12046, April 2026) — multi-stage training for claim-level confidence reasoning\n- Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality [CAG] (arXiv 2605.01749, May 2026) — training-based calibration-aware generation\n- Atomic Calibration of LLMs in Long-Form Generations (Findings of AACL-IJCNLP 2025) — showed poor claim-level calibration in long-form outputs\n- Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control [CSS] (arXiv 2604.17487, April 2026) — post-generation specificity control via external verifiers\n- When Should LLMs Be Less Specific? Selective Abstraction for Reliable Long-Form Text Generation (arXiv 2602.11908, February 2026)\n- Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs (ICML 2024) — linear probes approximate semantic entropy at response level\n- FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023)\n- Long-form Factuality in Large Language Models [LongFact/SAFE] (NeurIPS 2024)\n- Steering Language Models With Activation Engineering (Turner et al., arXiv 2308.10248, 2023)\n\n## 资源估算\n### auto_research\n- **claude_api_cost**: $200-400 (~3000-6000 Opus turns)\n- **estimated_gpu_cost**: $490-680\n- **gpu_hours**: ~195h H100 80GB (agent explores probe architectures, layer selections, K-window sizes, steering schedules on 70B primary model with 8B sanity checks, plus evaluation)\n- **gpu_utilization**: ~80-90% — continuous experiment pipeline with minimal idle\n- **risk_note**: Without human judgment, agent may over-optimize probe thresholds and K-window sizes on validation set rather than ensuring robustness, may miss qualitative assessment of hedging naturalness (mid-sentence steering coherence requires human evaluation), and critically may not correctly interpret the orthogonality pilot results (the decision to proceed vs. pivot requires understanding of the mechanistic implications)\n- **speed_bottleneck**: Long-form generation throughput on Llama 3.1-70B with 2× H100 tensor parallelism (~20-30 tok/s) — generating and evaluating hundreds of long-form responses per configuration is the computational bottleneck\n- **team**: 0 researchers (initial setup + final review only)\n- **timeline**: 7-10 days with 2× H100 80GB\n\n### human_in_loop\n- **claude_api_cost**: $100-200 (~1500-3000 Opus turns)\n- **estimated_gpu_cost**: $425-595\n- **gpu_hours**: ~170h H100 80GB (agent handles pipeline code, probe training iteration, evaluation scripting; human approves pilot results, probe design, steering threshold calibration, and ablation priorities)\n- **gpu_utilization**: ~50-65% — agent queues experiments between human check-ins\n- **risk_note**: Primary risk: whether accuracy-confidence orthogonality holds at 70B scale in long-form generation — the ~8h pilot experiment validates this before committing the full budget. If orthogonality breaks (outcome c), we fall back to an 8B-only paper with the negative scaling result as a contribution, reducing total compute to ~70h H100. Secondary risk: whether sub-sentence probe-guided steering produces natural hedging at 70B or creates incoherent mid-sentence shifts — qualitative human assessment of hedging naturalness across K-token window sizes is essential. Tertiary risk: CAA effectiveness diminishing at 70B scale (per ICML 2025 scaling laws), though our adaptive probe-guided approach may be more robust than uniform steering.\n- **team**: 1 researcher, ~30min/day for methodology decisions, pilot outcome assessment, and qualitative hedging evaluation\n- **timeline**: 3-4 weeks\n\n### manual\n- **estimated_gpu_cost**: $490-680 (at ~$2.50-3.50/hr H100 80GB spot)\n- **gpu_hours**: ~195h H100 80GB (orthogonality pilot ~8h [2×H100], probe training + direction extraction ~24h [20h 70B on 2×H100, 4h 8B on 1×H100], Llama 3.1-70B evaluation on FActScore + LongFact ~85h [2×H100], Llama 3.1-8B sanity check ~12h [1×H100], baseline comparisons ~30h [unsteered ~3h, Han et al. ~13h, CURE ~14h], core ablations ×3 ~25h, debugging/rerun buffer ~11h)\n- **gpu_utilization**: ~25-35% effective — GPU idles during code development, pipeline debugging, and results analysis\n- **team**: 1-2 researchers with mechanistic interpretability and activation steering experience\n- **timeline**: 5-6 weeks (1 researcher full-time)\n\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T01:48:40.218Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T01:48:40.218Z",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac"
}
```

---

## Round 1

42 recorded events

### User

_source line 3 · 2026-05-16T01:48:40.646Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation

**状态**: 待审阅  
**级别**: top-tier  
**创建时间**: 2026-05-15T15:11:55.979393+00:00

## 描述
We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. Motivated by two key findings — Han et al. (EMNLP 2025) showed lightweight probes detect claim-level factuality in long-form hidden states, and Miao & Ungar (2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features — RaS combines both insights in a novel way: it reads claim-level accuracy signals via factuality probes during autoregressive generation and steers verbalized confidence to match via targeted activation intervention along the orthogonal confidence direction, all within a single forward pass. A key design improvement is sub-sentence probe monitoring: rather than waiting for sentence boundaries, RaS evaluates an exponential moving average of probe scores every K tokens (K=8), enabling mid-claim steering activation when uncertainty is detected — consistent with evidence that hallucination signals emerge at span onset (Obeso et al., 2025) and that confidence representations are cached at answer-adjacent positions (Kumaran et al., 2026). Unlike O'Neill et al.'s probe→steer pipeline (which uses an external observer for binary hallucination reduction), RaS self-probes for graded confidence calibration with no second model. Unlike CARE (SIGIR 2025, which uses post-hoc iterative fact correction), RaS operates within the forward pass. Unlike Han et al.'s neuron clamping (binary suppression of hallucinations), RaS produces calibrated verbal hedging proportional to the model's internal uncertainty. Unlike CURE, CAG, and LoVeC, it requires no base model training — only lightweight linear probe fitting and contrastive direction extraction. The probe-guided adaptive steering formula (α = β × max(0, θ − EMA_score)) relates to CAST's conditional steering (ICLR 2025) and CLAS's context-dependent steering but is driven by continuous per-claim factuality signals rather than PCA-derived condition vectors or general context sensing. The framework includes a dedicated pilot experiment verifying the accuracy-confidence orthogonality at 70B scale in long-form generation — extending Miao & Ungar's finding beyond the 7–8B QA setting where it was established. We evaluate on Llama 3.1-70B (primary, testing scaling) and Llama 3.1-8B (sanity check, direct comparison with prior work) using FActScore and LongFact, measuring claim-level ECE, Brier score, AUROC, factual precision, and steering latency distribution. We target ≥25% claim-level ECE reduction (conservatively discounted from Miao & Ungar's 70–90% response-level QA results, given additional challenges of claim-level granularity, long-form generation, and 70B scale), with ≥40% as a stretch goal, while preserving FActScore within 2%. All experiments fit within ~195 H100-hours.

## 核心问题
LLMs generate long-form outputs where hallucinated claims are expressed with the same high confidence as factual ones. Existing approaches either detect hallucinations at claim level without calibrating expressed confidence (Han et al., EMNLP 2025 — binary probes + neuron clamping; O'Neill et al., July 2025 — external observer probe + binary steering), calibrate confidence only at response level for short-form QA (Ji et al., EMNLP 2025; Miao & Ungar, 2026; CORAL, 2026), perform fact-level calibration via post-hoc iterative correction rather than during generation (CARE, SIGIR 2025), use probe-guided steering without claim-level granularity or long-form scope (ITI, NeurIPS 2023; CLAS, 2026; ActCab/CoDec, EMNLP 2024), apply conditional or adaptive steering for behavioral control rather than calibrated confidence expression (CAST, ICLR 2025; Spherical Steering, ICML 2026; FLAS, 2026), or require multi-stage training of the base model (CURE, April 2026; CAG, May 2026; LoVeC, May 2025). No existing method performs claim-level calibrated uncertainty expression in long-form generation during a single forward pass without base model training. Furthermore, the accuracy-confidence orthogonality that enables clean steering (Miao & Ungar, 2026) has only been validated on 7–8B models for short-form QA — whether it holds at 70B scale in long-form generation is an open question with practical implications for the entire probe-guided steering paradigm.

## 机遇 / Why Now
Four recent results create a convergent opportunity: (1) Han et al. (EMNLP Findings 2025) showed lightweight linear probes on hidden states detect claim-level factuality in long-form generation, matching expensive multi-sample methods at up to 100× fewer FLOPs — but their neuron clamping intervention is binary (suppress/allow), not calibrated; (2) Miao & Ungar (March 2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features (cosine similarity < 0.04), meaning models internally know when they're wrong but fail to express this — and that adaptive CAA steering along these directions achieves major calibration improvement (ECE 14.9→3.7 on Llama-3.1-8B, 35.1→3.3 on Mistral-7B), but only for response-level QA on 7–8B models; (3) Kumaran et al. (March 2026) demonstrated that confidence representations are cached at answer-adjacent positions before verbalization, enabling real-time detection during generation — critically, their finding that hallucination signals emerge at the onset of hallucinated spans supports sub-sentence probe monitoring; (4) CLAS (April 2026) demonstrated that probe-derived adaptive steering works on models up to Llama 3.1-70B across 11 benchmarks, providing evidence that the steering mechanism scales — though not specifically for confidence calibration. Combining these — reading claim-level accuracy signals via probes during long-form generation, then steering verbalized confidence to match in real time — is unexplored and fills a specific gap. Critically, testing whether the accuracy-confidence orthogonality extends to 70B scale and long-form generation is itself a contribution that informs the feasibility of the entire probe-guided confidence steering paradigm.

## 方法思路
We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. The system reads internal accuracy signals per-claim via lightweight probes and steers verbalized confidence to match via targeted activation intervention, producing naturally hedged language for uncertain claims while leaving confident-and-correct claims untouched.

**Pilot Experiment — Orthogonality Verification at Scale (~8h, 2× H100, first week):** Before committing the full experimental budget, we replicate Miao & Ungar's orthogonality analysis on Llama 3.1-70B in a long-form generation setting. We extract accuracy and confidence directions from biography-generation hidden states (not QA), measure their cosine similarity, and compare against the < 0.04 value found at 7–8B scale. This pilot has three outcomes: (a) orthogonality holds (cosine < 0.1) — proceed as planned, report the scaling result as a contribution; (b) orthogonality partially holds (cosine 0.1–0.3) — adapt steering to project out the accuracy component from the confidence direction before steering, proceed with modified approach; (c) orthogonality fails (cosine > 0.3) — report as an important negative finding about the limits of linear feature geometry at scale, fall back to the 8B-only configuration with reduced total compute (~70h). All three outcomes produce publishable results.

**Offline Stage 1 — Factuality Probe Training (~20h wall on 2× H100 for 70B; ~4h on 1× H100 for 8B; one-time per model):** Generate long-form outputs (biographies, factual descriptions) from the target model, decompose into atomic claims using FActScore/OpenFActScore decomposition, verify claim factuality against knowledge sources. Extract hidden states at each claim's token span across multiple layers (following Han et al.'s layer-group methodology). Train lightweight linear probes (logistic regression on span-aggregated hidden states) to predict continuous factuality confidence scores. Unlike Han et al.'s binary factuality labels, we train on soft labels derived from verification confidence, enabling graded uncertainty estimation.

**Offline Stage 2 — Verbalized-Confidence Direction Extraction (included in Stage 1 compute; one-time per model):** Extract a verbalized-confidence steering direction via contrastive activation pairs: generate matched claim pairs where the same factual content is expressed with high confidence ('X was born in Y') vs. hedged uncertainty ('X was reportedly born in Y, though I am not certain'). The mean activation difference yields the steering direction, following the contrastive methodology from Ji et al. (VUF) and Miao & Ungar (CAA). For the 70B model, if the pilot reveals partial orthogonality degradation, we apply Gram-Schmidt orthogonalization to project the confidence direction away from the accuracy direction before use.

**Online Stage — Sub-Sentence Probe-Guided Steering During Generation:** During autoregressive generation: (1) At each generated token, run the factuality probe on its hidden states — this is a single matrix-vector multiplication with negligible overhead (~0.001% of the forward pass). (2) Maintain a running exponential moving average (EMA) of probe scores over a sliding window of the last K tokens (default K=8), providing smoothed uncertainty estimates that avoid triggering on single noisy tokens while enabling sub-sentence response. (3) When the EMA drops below the calibrated threshold θ, immediately activate steering — even mid-sentence. This means RaS can begin hedging within the current claim by steering subsequent tokens toward uncertainty-expressing language (e.g., generating qualifiers like 'reportedly,' 'I believe,' or reformulations for the remaining tokens in the sentence). The steering magnitude follows the adaptive formula: α = β × max(0, θ − EMA_score), where β is calibrated on a held-out validation set. This adaptive formula is conceptually related to CAST's conditional steering (apply only when a condition is met) and CLAS's context-dependent steering, but driven by continuous per-claim factuality probe scores rather than PCA-derived category membership (CAST) or general context sensing vectors (CLAS). (4) Deactivate steering when the EMA recovers above threshold θ, indicating the model has returned to confident territory.

**Steering latency analysis:** The sub-sentence trigger design means that in the best case, the probe detects uncertainty within the first few tokens of a claim (consistent with Kumaran et al.'s finding that confidence signals are cached at answer-adjacent positions and Obeso et al.'s evidence that hallucination signals are detectable at span onset), and steering activates mid-claim with ~K/2 token latency. We will empirically measure the distribution of steering activation timing relative to claim boundaries: what fraction of uncertain claims receive hedging (a) within the same sentence, (b) within K tokens, and (c) only in subsequent sentences. If probe signals rise early in claims as prior work suggests, mid-claim steering should be feasible for most uncertain claims. For claims where steering activates late, the output exhibits forward-looking uncertainty conditioning — subsequent generation is explicitly uncertainty-aware — which we acknowledge as a known tradeoff and measure empirically.

**Key design choices addressing known limitations:** (a) EMA-smoothed probe scores over K-token windows avoid single-token noise while enabling sub-sentence response — a substantial improvement over sentence-boundary-only evaluation. (b) Single-pass online monitoring eliminates the two-pass chicken-and-egg problem — no position-aligned regeneration needed. (c) Continuous calibrated steering (not binary neuron clamping) produces graded hedging proportional to internal uncertainty, distinguishing this from Han et al.'s binary intervention and O'Neill et al.'s binary hallucination steering. (d) Operating on the verbalized-confidence direction (orthogonal to accuracy per Miao & Ungar, verified at 70B scale in our pilot) means steering affects expression style without corrupting the model's factual knowledge. (e) Self-probing eliminates the need for an external observer model (unlike O'Neill et al.), keeping the framework single-pass with negligible compute overhead. (f) Adaptive steering magnitude based on probe-detected need may mitigate the diminishing effectiveness of uniform CAA at larger scales (ICML 2025 scaling laws), since steering is only applied where needed and at probe-calibrated intensity.

**Models:** Llama 3.1-70B-Instruct as primary (standard dense transformer architecture, well-studied for probing and steering, large enough to test scaling of the orthogonality finding, with CLAS confirming probe-derived steering viability at this scale). Llama 3.1-8B-Instruct as lightweight sanity check (enables direct comparison with Miao & Ungar and Ji et al. baselines on the same model family, validates the pipeline in well-charted territory). Both models use standard transformer attention across all layers, avoiding the untested territory of hybrid DeltaNet architectures (e.g., Qwen 3.5) where linear probe and steering techniques lack validation.

**Benchmarks:** FActScore (biography generation, primary) and LongFact (diverse long-form factuality). Metrics: claim-level ECE, Brier score (calibration quality), AUROC (uncertainty detection), FActScore/factual precision (to verify steering does not degrade content quality), MT-Bench fluency subset (to verify generation quality preservation), and steering latency distribution (fraction of uncertain claims hedged within-sentence vs. forward-conditioned). We also report the cosine similarity between accuracy and confidence directions at 70B scale as a standalone mechanistic finding.

**Quantitative targets:** We expect RaS to achieve: (1) claim-level ECE reduction of ≥25% relative to unsteered baselines on both FActScore and LongFact (primary target), with ≥40% as a stretch goal — the primary target is conservative given that Miao & Ungar's response-level results (70–90% ECE reduction on QA) face additional challenges at claim-level granularity in long-form generation at 70B scale, including noisy claim boundary detection, probe signal dilution from long-context hidden states, and sub-sentence steering latency; (2) FActScore preservation within 2% of unsteered baseline (steering affects verbal expression, not factual content); (3) uncertainty detection AUROC ≥0.80 (probe-based); (4) superior calibration (lower ECE) compared to Han et al.'s binary neuron clamping at comparable or better FActScore; (5) ≥60% of uncertain claims receiving within-sentence hedging via sub-sentence triggers.

**Comparisons (3 baselines):** (1) Unsteered baseline (cost: ~3h), (2) Han et al.'s probes + neuron clamping (closest representation-based method for long-form; cost: ~13h), (3) CURE (closest training-based method for claim-level calibration, if reproducible; cost: ~14h). We discuss but do not reimplement O'Neill et al. (external observer, different setting), CARE (post-hoc correction, different mechanism), and LoVeC (RL-based, high reproduction cost).

**Ablations (3 core):** (1) Probe-only detection without steering (measures probe quality in isolation), (2) Uniform steering without probe guidance (constant steering magnitude — tests whether probe-adaptive steering outperforms naive uniform application), (3) Steering strength sensitivity (varying β, θ, and K-token window size — analyzes latency vs. signal quality tradeoff).

## 研究现状
**Foundational probe→steer paradigm:** ITI (Li et al., NeurIPS 2023) introduced inference-time intervention: linear probes identify truthful directions in attention heads, and activations are shifted along these directions during generation. Foundational work, but targets truthfulness (content change) rather than calibrated confidence expression, and only on TruthfulQA.

**Closest prior work — claim-level probing in long-form generation:** Han et al. (EMNLP Findings 2025) trained simple linear probes on LLM hidden states that detect claim-level hallucinations in long-form generation with performance matching expensive multi-sample methods (up to 100× fewer FLOPs), testing on models up to Llama 3.1-405B. Their neuron clamping causally reduces hallucinations by fixing activations of factuality-correlated neurons — but this is a binary intervention (suppress or allow) that does not produce calibrated verbal uncertainty expression. Obeso et al. (arXiv 2509.03531, 2025) trains entity-level probes for real-time streaming hallucination detection in long-form generation (AUC 0.90 on Llama-3.3-70B) — detection only, no calibrated steering.

**Closest prior work — observer-model probe→steer for hallucinations:** O'Neill et al. (arXiv 2507.23221, July 2025) demonstrated that a generator-agnostic observer model can detect contextual hallucinations via a linear probe on its residual stream, isolating a single transferable direction that outperforms baselines by 5–27 points across Gemma-2 models (2B–27B), and that manipulating this direction causally steers generator hallucination rates. RaS differs on three axes: (a) self-probing rather than requiring an external observer model, eliminating the overhead of a second forward pass; (b) graded confidence calibration rather than binary hallucination detection/reduction — RaS produces proportionally hedged language, not just fewer hallucinations; (c) claim-level granularity in long-form factual generation rather than span-level detection in context-grounded settings.

**Closest prior work — calibrated confidence steering:** Miao & Ungar (arXiv 2603.25052, March 2026) discovered that calibration accuracy and verbalized confidence are orthogonal linear features (cosine similarity < 0.04), and proposed two-stage adaptive CAA steering that reads internal accuracy and steers verbalized output to match, achieving ECE improvements from 14.9→3.7 (Llama-3.1-8B) and 35.1→3.3 (Mistral-7B) — but only for response-level short-form QA on 7–8B models. They explicitly acknowledge: 'Whether the linear encoding findings hold at larger scales remains open. Evaluation is restricted to question-answering tasks; extending to open-ended generation would require rethinking how the probe target is constructed.' Ji et al. (EMNLP 2025) discovered the Verbal Uncertainty Feature (VUF) and proposed MUC with ~30% reduction in confident hallucinations — also response-level, short-form, on ≤8B models.

**Same-group prior work — CORAL:** CORAL (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) uses regularized MLP probes on residual activations to predict correctness and steers at inference time, achieving 10% accuracy and 50% ECE improvements. However, CORAL targets MCQA on 7B models with response-level steering — no claim-level decomposition or long-form generation. RaS differs in (a) claim-level granularity via factuality probes, (b) long-form generation scope, and (c) confidence expression calibration rather than answer correctness steering.

**Fact-level calibration via iterative correction:** CARE (Yuan et al., SIGIR 2025; arXiv 2411.13343) proposes fact-level confidence calibration for long-form generation, decomposing responses into atomic facts, estimating per-fact confidence, and using high-confidence facts to iteratively refine low-confidence ones via ConFix. CARE addresses the same problem space (fact-level calibration in long-form outputs) but via a fundamentally different mechanism: post-hoc multi-pass correction through prompting, rather than single-pass activation steering during generation. RaS operates within the forward pass with no regeneration, targets verbal confidence expression rather than factual correction, and requires no external confidence estimation pipeline.

**Conditional and adaptive steering methods:** CAST (Arditi et al., ICLR 2025) introduced conditional activation steering where a PCA-derived condition vector determines whether to apply a behavior vector via thresholded cosine similarity: h' ← h + f(sim(h, proj_c h)) · α · v. CAST's 'if condition, then steer' paradigm is conceptually related to RaS's probe-triggered steering, but CAST uses a PCA-derived condition vector for behavioral categories (e.g., content moderation), while RaS uses a data-driven factuality probe score for continuous uncertainty calibration — the probe provides graded confidence estimates, not binary category membership. Spherical Steering (You et al., arXiv 2602.08169, February 2026; ICML 2026) replaces additive steering with norm-preserving geodesic rotation and uses a vMF-based confidence gate for input-adaptive strength, achieving +10% on TruthfulQA with Llama-3.1-8B — but targets truthfulness in MCQ rather than calibrated confidence expression in long-form generation. FLAS (Jin et al., arXiv 2605.05892, May 2026) learns a concept-conditioned velocity field enabling curved, multi-step trajectories through activation space, outperforming prompting on AxBench with Gemma-2 models — a more expressive steering mechanism than linear CAA, but tested only on small models (2B–9B) for general behavior control, not confidence calibration.

**Activation calibration + guided decoding:** ActCab/CoDec (EMNLP 2024) trains a linear layer on LM last-layer activations for confidence calibration, then uses confidence-guided decoding to elicit truthful answers. Same conceptual pipeline (activation-based calibration → guided generation) but operates at response level on QA, and modifies decoding probabilities rather than verbalized confidence expression.

**Adaptive steering strength:** CLAS (Hsu et al., arXiv 2604.24693, April 2026) introduces context-dependent linear activation steering where steering strength adapts via learned sensing vectors: α_ℓ,t = (c_ℓ · [h_ℓ,t, 1]). Tested on Llama-3.1-70B across 11 benchmarks, demonstrating that probe-derived adaptive steering scales to 70B. RaS's α = β × max(0, threshold − probe_score) adapts similarly but is driven by factuality probe scores per-claim rather than a general context sensing vector, and targets confidence calibration specifically.

**Mechanistic understanding:** 'How do LLMs Compute Verbal Confidence?' (Kumaran et al., arXiv 2603.17839, March 2026) provides convergent evidence that confidence representations emerge at answer-adjacent positions via cached retrieval, supporting the feasibility of online detection during generation. Their finding that signals are cached before verbalization motivates sub-sentence probe monitoring.

**Training-free steering baselines:** SteerConf (NeurIPS 2025) does prompt-based training-free confidence steering via multi-prompt aggregation. ACT (WWW 2025) applies tuning-free diverse steering vectors with adaptive intensity for truthfulness, scaling to 65B.

**Claim-level long-form calibration (training-based):** CURE (arXiv 2604.12046, April 2026) uses multi-stage training to teach claim-level confidence reasoning, improving accuracy by up to 39.9%. CAG (arXiv 2605.01749, May 2026) achieves up to 13% factuality gain via training-based calibration-aware generation. LoVeC (arXiv 2505.23912, May 2025) uses RL to train LLMs to append on-the-fly confidence scores per statement in long-form generation, achieving 20× speedup over self-consistency methods. All three require base model fine-tuning or RL.

**Post-generation claim-level approaches:** CSS (arXiv 2604.17487, April 2026) decomposes answers into claims and backs off uncertain ones using external verifiers. Selective Abstraction (arXiv 2602.11908, February 2026) replaces low-confidence atoms with confident abstractions.

**Residual-stream anomaly detection:** PCNET (arXiv 2605.05953, May 2026) uses probabilistic circuits on residual streams for hallucination detection + contrastive decoding, reaching up to 99% AUROC — but targets short-form QA and changes content (different token selection) rather than expressing calibrated uncertainty.

**Scaling concerns for activation steering:** Scaling laws for activation steering (ICML 2025) show that CAA effectiveness diminishes with model size on Llama 2 (7B→13B→70B) for behavioral steering (refusal). Endogenous steering resistance (arXiv 2602.06941, February 2026) shows Llama-3.3-70B has 3.8% ESR rate (vs <1% for smaller models). However, CLAS demonstrates successful probe-derived steering on Llama-3.1-70B, suggesting that adaptive, probe-guided steering may be more robust at scale than uniform CAA.

**Gap:** No existing work combines claim-level factuality probing (à la Han et al.) with calibrated activation steering along the verbalized-confidence direction (à la Miao & Ungar) in a single-pass, online framework for long-form generation. O'Neill et al.'s probe→steer pipeline is closest structurally but uses an external observer for binary hallucination reduction rather than self-probing for graded confidence calibration. CARE addresses fact-level calibration in long-form outputs but via post-hoc correction rather than real-time activation steering. CAST provides conditional steering but for behavioral categories, not continuous confidence calibration. This intersection — reading internal accuracy per-claim and steering verbalized confidence to match during generation — is the contribution space. Additionally, no work has tested whether the accuracy-confidence orthogonality discovered at 7–8B scale holds at 70B or in long-form generation contexts, making this verification itself a contribution to the mechanistic understanding of confidence representations.

## 目标 Venue
- AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — ~10 weeks; conference Feb 16-23, Montréal) — PRIMARY
- ARR August 2026 (submission Aug 3, 2026 — ~11 weeks; committable to EMNLP 2026 Oct 24-29 or later *ACL venues)
- ICLR 2027 (expected submission ~Oct 2026, ~20 weeks; comfortable timeline)

## 关键参考
- Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation (Han et al., Findings of EMNLP 2025) — closest prior work: claim-level probes + neuron clamping in long-form generation
- A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations (O'Neill et al., arXiv 2507.23221, July 2025) — closest probe→steer pipeline: external observer linear probe detects and steers hallucinations across Gemma-2 2B–27B; differs from RaS in using external observer (vs. self-probing), binary hallucination steering (vs. graded confidence calibration), and context-grounded settings (vs. long-form factual generation)
- Closing the Confidence-Faithfulness Gap in LLMs (Miao & Ungar, arXiv 2603.25052, March 2026) — accuracy-confidence orthogonality discovery + adaptive CAA steering; explicitly notes scaling and long-form extension as open questions
- Correctness-Optimized Residual Activation Lens [CORAL] (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) — same group; MLP probes → correctness steering on MCQA at 7B scale; must differentiate as response-level, short-form only
- Fact-Level Calibration and Correction for Long-Form Generations [CARE/ConFix] (Yuan et al., SIGIR 2025; arXiv 2411.13343) — fact-level confidence calibration + iterative correction via high-confidence facts refining low-confidence ones; same problem space but fundamentally different mechanism (post-hoc multi-pass correction vs. single-pass activation steering)
- Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025) — VUF discovery and MUC for response-level short-form QA
- Inference-Time Intervention: Eliciting Truthful Answers from a Language Model [ITI] (Li et al., NeurIPS 2023) — foundational probe→steer paradigm using linear probes on attention heads for truthfulness
- Programming Refusal with Conditional Activation Steering [CAST] (Arditi et al., ICLR 2025) — conditional steering via PCA-derived condition vectors with thresholded activation; conceptually related 'if condition, then steer' paradigm, but targets behavioral categories rather than continuous confidence calibration
- Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., arXiv 2602.08169, February 2026; ICML 2026) — norm-preserving geodesic rotation with vMF confidence gating; +10% on TruthfulQA with Llama-3.1-8B; targets truthfulness MCQ, not calibrated confidence in long-form
- Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention [FLAS] (Jin et al., arXiv 2605.05892, May 2026) — learned concept-conditioned velocity field for curved activation trajectories; more expressive than linear CAA but tested on Gemma-2 2B–9B for general behavior control
- Enhancing Language Model Factuality via Activation-Based Confidence Calibration and Guided Decoding [ActCab/CoDec] (EMNLP 2024) — activation calibration + confidence-guided decoding for QA factuality
- Contextual Linear Activation Steering [CLAS] (Hsu et al., arXiv 2604.24693, April 2026) — probe-derived adaptive steering with context-dependent strength; tested on Llama-3.1-70B, confirming steering viability at 70B scale
- How do LLMs Compute Verbal Confidence? (Kumaran et al., arXiv 2603.17839, March 2026) — mechanistic evidence for cached confidence retrieval at answer-adjacent positions; supports feasibility of sub-sentence probe monitoring
- Reinforcement Learning for Better Verbalized Confidence in Long-Form Generation [LoVeC] (arXiv 2505.23912, May 2025) — RL-based on-the-fly confidence scoring per statement in long-form generation; training-based
- Scaling Laws for Activation Steering with Llama 2 Models and Refusal Mechanisms (ICML 2025) — demonstrates CAA effectiveness diminishes with model size (7B→70B); informs our adaptive steering design
- Endogenous Resistance to Activation Steering in Language Models (arXiv 2602.06941, February 2026) — Llama-3.3-70B shows 3.8% endogenous steering resistance; relevant scaling concern
- Does Transformer Interpretability Transfer to RNNs? (2024) — probing and CAA partially transfer to recurrent architectures with reduced effectiveness; motivates our choice of standard transformer models
- SteerConf: Steering LLMs for Confidence Elicitation (Zhou et al., NeurIPS 2025) — prompt-based training-free confidence calibration
- Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025) — diverse steering vectors with adaptive intensity control
- Real-Time Detection of Hallucinated Entities in Long-Form Generation (Obeso et al., arXiv 2509.03531, 2025) — entity-level streaming probes for long-form generation; evidence that hallucination signals are detectable at span onset
- Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits [PCNET] (arXiv 2605.05953, May 2026) — residual stream anomaly detection + contrastive decoding intervention
- Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, January 2026) — online hallucination detection as evolving latent state
- Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration [CURE] (arXiv 2604.12046, April 2026) — multi-stage training for claim-level confidence reasoning
- Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality [CAG] (arXiv 2605.01749, May 2026) — training-based calibration-aware generation
- Atomic Calibration of LLMs in Long-Form Generations (Findings of AACL-IJCNLP 2025) — showed poor claim-level calibration in long-form outputs
- Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control [CSS] (arXiv 2604.17487, April 2026) — post-generation specificity control via external verifiers
- When Should LLMs Be Less Specific? Selective Abstraction for Reliable Long-Form Text Generation (arXiv 2602.11908, February 2026)
- Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs (ICML 2024) — linear probes approximate semantic entropy at response level
- FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023)
- Long-form Factuality in Large Language Models [LongFact/SAFE] (NeurIPS 2024)
- Steering Language Models With Activation Engineering (Turner et al., arXiv 2308.10248, 2023)

## 资源估算
### auto_research
- **claude_api_cost**: $200-400 (~3000-6000 Opus turns)
- **estimated_gpu_cost**: $490-680
- **gpu_hours**: ~195h H100 80GB (agent explores probe architectures, layer selections, K-window sizes, steering schedules on 70B primary model with 8B sanity checks, plus evaluation)
- **gpu_utilization**: ~80-90% — continuous experiment pipeline with minimal idle
- **risk_note**: Without human judgment, agent may over-optimize probe thresholds and K-window sizes on validation set rather than ensuring robustness, may miss qualitative assessment of hedging naturalness (mid-sentence steering coherence requires human evaluation), and critically may not correctly interpret the orthogonality pilot results (the decision to proceed vs. pivot requires understanding of the mechanistic implications)
- **speed_bottleneck**: Long-form generation throughput on Llama 3.1-70B with 2× H100 tensor parallelism (~20-30 tok/s) — generating and evaluating hundreds of long-form responses per configuration is the computational bottleneck
- **team**: 0 researchers (initial setup + final review only)
- **timeline**: 7-10 days with 2× H100 80GB

### human_in_loop
- **claude_api_cost**: $100-200 (~1500-3000 Opus turns)
- **estimated_gpu_cost**: $425-595
- **gpu_hours**: ~170h H100 80GB (agent handles pipeline code, probe training iteration, evaluation scripting; human approves pilot results, probe design, steering threshold calibration, and ablation priorities)
- **gpu_utilization**: ~50-65% — agent queues experiments between human check-ins
- **risk_note**: Primary risk: whether accuracy-confidence orthogonality holds at 70B scale in long-form generation — the ~8h pilot experiment validates this before committing the full budget. If orthogonality breaks (outcome c), we fall back to an 8B-only paper with the negative scaling result as a contribution, reducing total compute to ~70h H100. Secondary risk: whether sub-sentence probe-guided steering produces natural hedging at 70B or creates incoherent mid-sentence shifts — qualitative human assessment of hedging naturalness across K-token window sizes is essential. Tertiary risk: CAA effectiveness diminishing at 70B scale (per ICML 2025 scaling laws), though our adaptive probe-guided approach may be more robust than uniform steering.
- **team**: 1 researcher, ~30min/day for methodology decisions, pilot outcome assessment, and qualitative hedging evaluation
- **timeline**: 3-4 weeks

### manual
- **estimated_gpu_cost**: $490-680 (at ~$2.50-3.50/hr H100 80GB spot)
- **gpu_hours**: ~195h H100 80GB (orthogonality pilot ~8h [2×H100], probe training + direction extraction ~24h [20h 70B on 2×H100, 4h 8B on 1×H100], Llama 3.1-70B evaluation on FActScore + LongFact ~85h [2×H100], Llama 3.1-8B sanity check ~12h [1×H100], baseline comparisons ~30h [unsteered ~3h, Han et al. ~13h, CURE ~14h], core ablations ×3 ~25h, debugging/rerun buffer ~11h)
- **gpu_utilization**: ~25-35% effective — GPU idles during code development, pipeline debugging, and results analysis
- **team**: 1-2 researchers with mechanistic interpretability and activation steering experience
- **timeline**: 5-6 weeks (1 researcher full-time)



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "3f8ed21f-38b7-43d1-9f98-87b3b218ef2a",
  "type": "user",
  "uuid": "8d514b39-670d-4af0-9f27-acf584d0b8c6",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T01:48:40.632Z_

```json
{
  "parentUuid": "8d514b39-670d-4af0-9f27-acf584d0b8c6",
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
  "uuid": "05e36fdf-5033-4b64-9717-d20b8f8669c5",
  "timestamp": "2026-05-16T01:48:40.632Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T01:48:40.632Z_

```json
{
  "parentUuid": "05e36fdf-5033-4b64-9717-d20b8f8669c5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "660fc650-d9c5-4bde-b48e-450a00850442",
  "timestamp": "2026-05-16T01:48:40.632Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation  **状态**: 待审阅   **级别**:…",
  "leafUuid": "660fc650-d9c5-4bde-b48e-450a00850442",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate claim-level confidence calibration proposal",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac"
}
```

---

### Assistant

_source line 8 · 2026-05-16T01:49:37.930Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully evaluate this proposal for EMNLP 2026 main conference. I need to assess the idea quality across Novelty, Significance, and Related Work dimensions, and provide a probability estimate.

Let me first understand the core idea:

**Read-and-Steer (RaS)**: A single-pass framework that:
1. Uses lightweight linear probes to detect claim-level factuality during autoregressive generation (reading internal accuracy signals)
2. Steers verbalized confidence to match via targeted activation intervention along the orthogonal confidence direction
3. Does this at sub-sentence granularity (every K tokens) within a single forward pass
 
Now I'm tracing back where these components come from. Han et al. established claim-level factuality probes for long-form generation, while Miao & Ungar showed that accuracy and confidence are orthogonal and developed adaptive steering—though they only tested it on smaller models for response-level QA. Kumaran et al. demonstrated confidence caching at strategic positions, and CLAS proved that probe-based adaptive steering scales to 70B models. The obvious question is whether this is just applying Miao & Ungar's method at the claim level instead of the response level.

The core concern is that RaS might just be combining existing pieces—taking Han et al.'s probes and Miao & Ungar's steering direction and putting them together in a single pass. The engineering does add some complexity with sub-sentence probe monitoring, EMA smoothing, and adaptive magnitude formulas, plus verification that orthogonality holds at 70B scale. But conceptually, once you've read both papers, combining them feels like the natural next step, and the proposal doesn't seem to push beyond what those prior works already suggest.

There are some real risks here though. The orthogonality assumption at 70B is uncertain and only backed by a pilot experiment. Steering mid-sentence could easily break generation coherence. And there's a gap between how linear probes perform in offline factuality analysis versus during actual generation when context is constantly shifting—that transfer assumption isn't trivial.

Looking at the novelty angle, this is really an engineering combination of existing techniques—factuality probes plus confidence steering applied to claim-level long-form generation. O'Neill et al. and CORAL already do probe-to-steer approaches, so what RaS adds is the specific pairing of self-probing with graded calibration at the claim level in a single pass. That's a useful combination but fairly predictable. The orthogonality verification at 70B is a nice secondary result but mostly replicates prior findings. The sub-sentence EMA monitoring is solid engineering but just a straightforward sliding window—nothing fundamentally novel there.

The problem itself matters though.  Calibrated confidence at the claim level during long-form generation is a real gap with practical value. But the impact is constrained: it only applies to transformer models with known probe properties, the 25% ECE reduction is modest, and it requires offline probe training per model. The related work section is impressively comprehensive, which actually highlights how crowded this space has become—CURE, CAG, CARE, CORAL, O'Neill et al., CLAS, CAST all working on similar problems. RaS finds a specific niche but it's a narrow one.

The claimed gap itself is defined by a conjunction of constraints: claim-level calibration, long-form generation, single forward pass, no base model training. This "gap by conjunction" approach can be risky—reviewers might question why all these constraints need to hold simultaneously rather than seeing it as a natural problem boundary. I should check if any very recent work already addresses this specific combination.

Looking at the overall picture, the strengths are clear: a well-defined gap, elegant combination of two complementary techniques, a real-world problem, solid experimental design with pilot results, and appropriately conservative targets. The main weakness at the idea level is that novelty is primarily combinatorial—applying two existing techniques together in a somewhat predictable way. If the core result shows a 25% ECE reduction, reviewers might feel they would have anticipated this outcome, especially given how crowded the space is with concurrent work. The sub-sentence steering coherence issue is also a genuine technical challenge that's hard to solve purely through engineering.

Weighing everything—moderate novelty that's combinatorial and somewhat predictable, moderate-to-strong significance on an important but incremental problem, strong related work coverage that reveals a saturated landscape, and a core finding that wouldn't be surprising if positive—I'm looking at roughly 25-35% for EMNLP main.

Though reconsidering, there are some genuinely solid aspects here: the orthogonality verification at 70B is a real contribution, the sub-sentence probe monitoring is well-designed, and the single-pass self-probing approach is cleaner than prior work. But these feel more like execution-level refinements than fundamental breakthroughs. So I'm settling on moderate novelty, moderate-to-strong significance, and strong related work coverage, putting my estimate at 25-35% with a median around 28%.

Let me think through what a reviewer would actually say if they saw positive results. They'd likely call it a competent paper that combines existing approaches effectively, but the novelty question would still linger.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "660fc650-d9c5-4bde-b48e-450a00850442",
  "isSidechain": false,
  "requestId": "req_011Cb5QYVRazqWMj8Y71sY5m",
  "type": "assistant",
  "uuid": "9c6db0ab-5a69-4978-b461-379667173007",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013iC9oEpPkZjAEkYxxyPfEG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24257,
      "cache_read_input_tokens": 0,
      "output_tokens": 2031,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2031,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 24257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24257
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

_source line 9 · 2026-05-16T01:49:39.046Z_

I need to assess this proposal's idea quality. Let me first search for very recent work that might overlap with or already cover this idea space, then perform my evaluation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c6db0ab-5a69-4978-b461-379667173007",
  "isSidechain": false,
  "requestId": "req_011Cb5QYVRazqWMj8Y71sY5m",
  "type": "assistant",
  "uuid": "91a65d6b-b3ad-4381-a410-62e502977c00",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013iC9oEpPkZjAEkYxxyPfEG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24257,
      "cache_read_input_tokens": 0,
      "output_tokens": 2031,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2031,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 24257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24257
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

_source line 10 · 2026-05-16T01:49:39.258Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HivcWRjUY6Aq4j7vNTByyx`</summary>

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
  "parentUuid": "91a65d6b-b3ad-4381-a410-62e502977c00",
  "isSidechain": false,
  "requestId": "req_011Cb5QYVRazqWMj8Y71sY5m",
  "type": "assistant",
  "uuid": "85e9454e-da83-4a07-937b-91922285e21f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013iC9oEpPkZjAEkYxxyPfEG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24257,
      "cache_read_input_tokens": 0,
      "output_tokens": 2031,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2031,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 24257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24257
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

_source line 11 · 2026-05-16T01:49:39.271Z_

<details><summary>↩ Tool result · `toolu_01HivcWRjUY6Aq4j7vNTByyx`</summary>

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
  "parentUuid": "85e9454e-da83-4a07-937b-91922285e21f",
  "isSidechain": false,
  "promptId": "3f8ed21f-38b7-43d1-9f98-87b3b218ef2a",
  "type": "user",
  "uuid": "9669e02a-a905-4128-97fc-6ec4ff1f9201",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "85e9454e-da83-4a07-937b-91922285e21f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-16T01:49:41.647Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search for recent work that might overlap with this proposal's core idea space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9669e02a-a905-4128-97fc-6ec4ff1f9201",
  "isSidechain": false,
  "requestId": "req_011Cb5Qcm5XsUzsASnw72kev",
  "type": "assistant",
  "uuid": "b5d4cf29-a700-44cd-a04e-23f62863d66e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXV1h7CvTBdjqyQg4QA1nq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2555,
      "cache_read_input_tokens": 24257,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 113,
          "cache_read_input_tokens": 24257,
          "cache_creation_input_tokens": 2555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2555
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

_source line 13 · 2026-05-16T01:49:42.321Z_

Let me search for recent overlapping work across several dimensions simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5d4cf29-a700-44cd-a04e-23f62863d66e",
  "isSidechain": false,
  "requestId": "req_011Cb5Qcm5XsUzsASnw72kev",
  "type": "assistant",
  "uuid": "06e7e435-ad26-4b58-9d2e-84c4f460ae76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXV1h7CvTBdjqyQg4QA1nq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2555,
      "cache_read_input_tokens": 24257,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 113,
          "cache_read_input_tokens": 24257,
          "cache_creation_input_tokens": 2555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2555
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

_source line 14 · 2026-05-16T01:49:43.000Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KWC6EgxorGPsTrRNibnkbS`</summary>

```json
{
  "query": "claim-level confidence calibration long-form generation activation steering 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06e7e435-ad26-4b58-9d2e-84c4f460ae76",
  "isSidechain": false,
  "requestId": "req_011Cb5Qcm5XsUzsASnw72kev",
  "type": "assistant",
  "uuid": "ea5107c4-0be2-40db-825f-8b072e69a3f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXV1h7CvTBdjqyQg4QA1nq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2555,
      "cache_read_input_tokens": 24257,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 113,
          "cache_read_input_tokens": 24257,
          "cache_creation_input_tokens": 2555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2555
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

_source line 15 · 2026-05-16T01:49:50.460Z_

<details><summary>↩ Tool result · `toolu_01KWC6EgxorGPsTrRNibnkbS`</summary>

```text
Web search results for query: "claim-level confidence calibration long-form generation activation steering 2026"

Links: [{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Atomic Calibration of LLMs in Long-Form Generations | OpenReview","url":"https://openreview.net/forum?id=rzsjUC45xf"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2503.02623"},{"title":"Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework","url":"https://arxiv.org/html/2503.02863v1"},{"title":"ACTIVATION STEERING VIA GENERATIVE CAUSAL MEDIATION","url":"https://openreview.net/pdf/a041b1716bc888e0dd914c089c581a12e13b61d5.pdf"},{"title":"arXiv:2502.19649v3 [cs.LG] 12 Mar 2025 - Jan Wehner","url":"https://janwehner.com/files/representation_engineering.pdf"},{"title":"Calibrating Long-form Generations from Large Language ...","url":"https://aclanthology.org/2024.findings-emnlp.785.pdf"},{"title":"Calibrating Verbalized Confidence with Self-Generated Distractors | OpenReview","url":"https://openreview.net/forum?id=pZs4hhemXc"},{"title":"Steering Awareness: Detecting Activation Steering from Within","url":"https://arxiv.org/html/2511.21399v3"},{"title":"Fact-Level Calibration and Correction for Long-Form ...","url":"https://dl.acm.org/doi/pdf/10.1145/3726302.3730195"}]

Based on the web search results, here's what I found regarding the query on claim-level confidence calibration, long-form generation, and activation steering in 2026:

## Key Research Areas

**Atomic/Claim-Level Calibration in Long-Form Generation:**

Research systematically studies atomic calibration, which evaluates factuality calibration at a fine-grained level by decomposing long responses into atomic claims. LLMs exhibit poorer calibration at the atomic level during long-form generation. Researchers categorize existing confidence elicitation methods into discriminative and generative types, and propose new confidence fusion strategies to improve calibration.

**Confidence Calibration Methods:**

Recent work focuses on training models to express calibrated confidence. A reward function based on the logarithmic scoring rule has been optimized through reinforcement-learning-based policy optimization for directly and seamlessly training confidence calibration in LLM generations.

**Activation Steering and Confidence:**

Steering can shift model calibration—adding an uncertainty vector can shift the distribution of token probabilities, sometimes improving factual accuracy (the model hedges instead of committing to a wrong answer) and sometimes degrading it (the model hedges on things it actually knew).

**Advanced Steering Techniques:**

Fine-grained steering is where the field is going, with AUSteer decomposing activations into single-dimension "atomic units" and steering only the discriminative ones, with adaptive per-input strengths.

These developments represent emerging research directions in making LLM confidence estimation more reliable for longer, complex outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea5107c4-0be2-40db-825f-8b072e69a3f3",
  "isSidechain": false,
  "promptId": "3f8ed21f-38b7-43d1-9f98-87b3b218ef2a",
  "type": "user",
  "uuid": "8f3c8bad-c308-479b-82d1-ce07f43aff97",
  "toolUseResult": {
    "query": "claim-level confidence calibration long-form generation activation steering 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ER529D7inrYuUzfYRf2gzF",
        "content": [
          {
            "title": "Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra",
            "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"
          },
          {
            "title": "Atomic Calibration of LLMs in Long-Form Generations | OpenReview",
            "url": "https://openreview.net/forum?id=rzsjUC45xf"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2503.02623"
          },
          {
            "title": "Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework",
            "url": "https://arxiv.org/html/2503.02863v1"
          },
          {
            "title": "ACTIVATION STEERING VIA GENERATIVE CAUSAL MEDIATION",
            "url": "https://openreview.net/pdf/a041b1716bc888e0dd914c089c581a12e13b61d5.pdf"
          },
          {
            "title": "arXiv:2502.19649v3 [cs.LG] 12 Mar 2025 - Jan Wehner",
            "url": "https://janwehner.com/files/representation_engineering.pdf"
          },
          {
            "title": "Calibrating Long-form Generations from Large Language ...",
            "url": "https://aclanthology.org/2024.findings-emnlp.785.pdf"
          },
          {
            "title": "Calibrating Verbalized Confidence with Self-Generated Distractors | OpenReview",
            "url": "https://openreview.net/forum?id=pZs4hhemXc"
          },
          {
            "title": "Steering Awareness: Detecting Activation Steering from Within",
            "url": "https://arxiv.org/html/2511.21399v3"
          },
          {
            "title": "Fact-Level Calibration and Correction for Long-Form ...",
            "url": "https://dl.acm.org/doi/pdf/10.1145/3726302.3730195"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding the query on claim-level confidence calibration, long-form generation, and activation steering in 2026:\n\n## Key Research Areas\n\n**Atomic/Claim-Level Calibration in Long-Form Generation:**\n\nResearch systematically studies atomic calibration, which evaluates factuality calibration at a fine-grained level by decomposing long responses into atomic claims. LLMs exhibit poorer calibration at the atomic level during long-form generation. Researchers categorize existing confidence elicitation methods into discriminative and generative types, and propose new confidence fusion strategies to improve calibration.\n\n**Confidence Calibration Methods:**\n\nRecent work focuses on training models to express calibrated confidence. A reward function based on the logarithmic scoring rule has been optimized through reinforcement-learning-based policy optimization for directly and seamlessly training confidence calibration in LLM generations.\n\n**Activation Steering and Confidence:**\n\nSteering can shift model calibration—adding an uncertainty vector can shift the distribution of token probabilities, sometimes improving factual accuracy (the model hedges instead of committing to a wrong answer) and sometimes degrading it (the model hedges on things it actually knew).\n\n**Advanced Steering Techniques:**\n\nFine-grained steering is where the field is going, with AUSteer decomposing activations into single-dimension \"atomic units\" and steering only the discriminative ones, with adaptive per-input strengths.\n\nThese developments represent emerging research directions in making LLM confidence estimation more reliable for longer, complex outputs."
    ],
    "durationSeconds": 7.454295126000011,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ea5107c4-0be2-40db-825f-8b072e69a3f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation  **状态**: 待审阅   **级别**:…",
  "leafUuid": "8f3c8bad-c308-479b-82d1-ce07f43aff97",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate claim-level confidence calibration proposal",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac"
}
```

---

### Tool call

_source line 18 · 2026-05-16T01:49:53.602Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WsKyAFMcavuqgUFjJdVYia`</summary>

```json
{
  "query": "Miao Ungar accuracy confidence orthogonality CAA steering calibration 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f3c8bad-c308-479b-82d1-ce07f43aff97",
  "isSidechain": false,
  "requestId": "req_011Cb5Qdb5nsbZpkCRoF2UQs",
  "type": "assistant",
  "uuid": "5424d52f-b732-443a-aa8e-7eba2328cb0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gqz9XHvHV7wgpiX5sx7caC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 982,
      "cache_read_input_tokens": 26812,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 982,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 26812,
          "cache_creation_input_tokens": 982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 982
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

_source line 19 · 2026-05-16T01:50:00.391Z_

<details><summary>↩ Tool result · `toolu_01WsKyAFMcavuqgUFjJdVYia`</summary>

```text
Web search results for query: "Miao Ungar accuracy confidence orthogonality CAA steering calibration 2026 arxiv"

Links: [{"title":"Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/html/2603.25052v1"},{"title":"[2603.25052] Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/abs/2603.25052"},{"title":"[2603.25052v1] Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/abs/2603.25052v1"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation","url":"https://arxiv.org/html/2503.02863v2"},{"title":"A Unified Understanding and Evaluation of Steering Methods","url":"https://arxiv.org/html/2502.02716v2"},{"title":"Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework","url":"https://arxiv.org/html/2503.02863v1"},{"title":"Representation Engineering for Large-Language Models: Survey and Research Challenges","url":"https://arxiv.org/html/2502.17601v1"},{"title":"Steering Awareness: Detecting Activation Steering from Within","url":"https://arxiv.org/html/2511.21399v3"},{"title":"A Unified Understanding and Evaluation of Steering Methods Shawn Im Sharon Li","url":"https://www.arxiv.org/pdf/2502.02716"},{"title":"[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/abs/2602.06022"}]

I found relevant research papers by Miao and Ungar on this topic. Here are the key results:

## Primary Paper: "Closing the Confidence-Faithfulness Gap in Large Language Models"

The paper is authored by Miranda Muqing Miao and Lyle Ungar from the University of Pennsylvania, and was submitted to arXiv on March 26, 2026.

**Main Findings:**

The work presents a mechanistic interpretability analysis of verbalized confidence, using linear probes and contrastive activation addition (CAA) steering to show that calibration and verbalized confidence signals are encoded linearly but are orthogonal to one another — a finding consistent across three open-weight models and four datasets.

When models are prompted to simultaneously reason through a problem and verbalize a confidence score, the reasoning process disrupts the verbalized confidence direction, exacerbating miscalibration.

**Solution Approach:**

The authors' two-stage pipeline reads the model's internal accuracy estimate and steers the output to match it, achieving substantially lower calibration error than both unsteered verbalized confidence and SteerConf across all evaluated models.

## Related Work: "CORAL" Paper

Miao et al. also introduced CORAL (Correctness-Optimized Residual Activation Lens), a regularized inference-time steering method that consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5424d52f-b732-443a-aa8e-7eba2328cb0f",
  "isSidechain": false,
  "promptId": "3f8ed21f-38b7-43d1-9f98-87b3b218ef2a",
  "type": "user",
  "uuid": "862fe4b2-8d07-4e00-8bfc-a78be9749e3f",
  "toolUseResult": {
    "query": "Miao Ungar accuracy confidence orthogonality CAA steering calibration 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_0157vEPHsoYFLZSkX5YnRaSh",
        "content": [
          {
            "title": "Closing the Confidence-Faithfulness Gap in Large Language Models",
            "url": "https://arxiv.org/html/2603.25052v1"
          },
          {
            "title": "[2603.25052] Closing the Confidence-Faithfulness Gap in Large Language Models",
            "url": "https://arxiv.org/abs/2603.25052"
          },
          {
            "title": "[2603.25052v1] Closing the Confidence-Faithfulness Gap in Large Language Models",
            "url": "https://arxiv.org/abs/2603.25052v1"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation",
            "url": "https://arxiv.org/html/2503.02863v2"
          },
          {
            "title": "A Unified Understanding and Evaluation of Steering Methods",
            "url": "https://arxiv.org/html/2502.02716v2"
          },
          {
            "title": "Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework",
            "url": "https://arxiv.org/html/2503.02863v1"
          },
          {
            "title": "Representation Engineering for Large-Language Models: Survey and Research Challenges",
            "url": "https://arxiv.org/html/2502.17601v1"
          },
          {
            "title": "Steering Awareness: Detecting Activation Steering from Within",
            "url": "https://arxiv.org/html/2511.21399v3"
          },
          {
            "title": "A Unified Understanding and Evaluation of Steering Methods Shawn Im Sharon Li",
            "url": "https://www.arxiv.org/pdf/2502.02716"
          },
          {
            "title": "[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://arxiv.org/abs/2602.06022"
          }
        ]
      },
      "I found relevant research papers by Miao and Ungar on this topic. Here are the key results:\n\n## Primary Paper: \"Closing the Confidence-Faithfulness Gap in Large Language Models\"\n\nThe paper is authored by Miranda Muqing Miao and Lyle Ungar from the University of Pennsylvania, and was submitted to arXiv on March 26, 2026.\n\n**Main Findings:**\n\nThe work presents a mechanistic interpretability analysis of verbalized confidence, using linear probes and contrastive activation addition (CAA) steering to show that calibration and verbalized confidence signals are encoded linearly but are orthogonal to one another — a finding consistent across three open-weight models and four datasets.\n\nWhen models are prompted to simultaneously reason through a problem and verbalize a confidence score, the reasoning process disrupts the verbalized confidence direction, exacerbating miscalibration.\n\n**Solution Approach:**\n\nThe authors' two-stage pipeline reads the model's internal accuracy estimate and steers the output to match it, achieving substantially lower calibration error than both unsteered verbalized confidence and SteerConf across all evaluated models.\n\n## Related Work: \"CORAL\" Paper\n\nMiao et al. also introduced CORAL (Correctness-Optimized Residual Activation Lens), a regularized inference-time steering method that consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average."
    ],
    "durationSeconds": 6.783339624999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5424d52f-b732-443a-aa8e-7eba2328cb0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-16T01:50:03.058Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019LAoxt9xYv1qdbchaMZ3Qk`</summary>

```json
{
  "query": "probe-guided steering confidence calibration long-form generation single pass 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "862fe4b2-8d07-4e00-8bfc-a78be9749e3f",
  "isSidechain": false,
  "requestId": "req_011Cb5QeK9s2ENiCN95bCEEN",
  "type": "assistant",
  "uuid": "7a7d21af-9075-439a-9477-bd1d795779a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JnsKDvvun2e8i23wMjWDmb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 27794,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 885,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 27794,
          "cache_creation_input_tokens": 885,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 885
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

_source line 21 · 2026-05-16T01:50:09.931Z_

<details><summary>↩ Tool result · `toolu_019LAoxt9xYv1qdbchaMZ3Qk`</summary>

```text
Web search results for query: "probe-guided steering confidence calibration long-form generation single pass 2026"

Links: [{"title":"Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework","url":"https://arxiv.org/html/2503.02863v1"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation","url":"https://arxiv.org/html/2503.02863v2"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation Ziang Zhou","url":"https://openreview.net/pdf/2dea5d57488bdb780105be0720fc4b246ed074ec.pdf"},{"title":"Simple Factuality Probes Detect Hallucinations in Long- ...","url":"https://aclanthology.org/2025.findings-emnlp.880.pdf"},{"title":"Calibrating Long-form Generations from Large Language ...","url":"https://aclanthology.org/2024.findings-emnlp.785.pdf"},{"title":"Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt","url":"https://arxiv.org/pdf/2503.02863v1"},{"title":"(PDF) Reinforcement Learning for Better Verbalized Confidence in Long-Form Generation","url":"https://www.researchgate.net/publication/392315230_Reinforcement_Learning_for_Better_Verbalized_Confidence_in_Long-Form_Generation"},{"title":"Robust Behavior Control in LLMs via Steering Target Atoms","url":"https://aclanthology.org/2025.acl-long.1139.pdf"},{"title":"Fact-Level Confidence Calibration: Empowering Confidence-Guided LLM Self-Correction | OpenReview","url":"https://openreview.net/forum?id=bCAxEwwmBr"},{"title":"Atomic Calibration of LLMs in Long-Form Generations | OpenReview","url":"https://openreview.net/forum?id=rzsjUC45xf"}]

Based on the web search results, I found relevant research related to your query about probe-guided steering, confidence calibration, and long-form generation. Here are the key findings:

## SteerConf Framework

SteerConf is a novel framework that leverages the steerability of LLMs' confidence scores to enhance their reliability through a steering prompt strategy to guide LLMs in generating confidence scores in a specified direction (e.g., conservative or optimistic) by employing prompts with varying steering intensities.

The framework systematically steers LLMs' confidence scores to improve their calibration and reliability, introducing three key components: (1) a steering prompt strategy that guides LLMs to produce confidence scores in specified directions by leveraging prompts with varying steering levels; (2) a steered confidence consistency measure that quantifies alignment across multiple steered confidences to enhance calibration; and (3) a steered confidence calibration method that aggregates confidence scores using consistency measures and applies linear quantization for answer selection.

## Long-Form Generation Confidence

For long-form text generation specifically, research addresses producing well-calibrated factual statements in a single decoding pass through a reinforcement learning (RL)-based approach that enables LLMs to produce well-calibrated confidence estimates during text generation.

Atomic calibration evaluates factuality calibration at a fine-grained level by decomposing long responses into atomic claims.

The research indicates that explicit instructions can inflate or deflate confidence scores in a regulated manner across multiple models including GPT3.5, LLAMA3-70b, and GPT4.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a7d21af-9075-439a-9477-bd1d795779a2",
  "isSidechain": false,
  "promptId": "3f8ed21f-38b7-43d1-9f98-87b3b218ef2a",
  "type": "user",
  "uuid": "77d90ee3-373c-4476-a4f3-55f34cfee5c8",
  "toolUseResult": {
    "query": "probe-guided steering confidence calibration long-form generation single pass 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XxMN1rDqEagS7uGuqy18FE",
        "content": [
          {
            "title": "Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework",
            "url": "https://arxiv.org/html/2503.02863v1"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation",
            "url": "https://arxiv.org/html/2503.02863v2"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation Ziang Zhou",
            "url": "https://openreview.net/pdf/2dea5d57488bdb780105be0720fc4b246ed074ec.pdf"
          },
          {
            "title": "Simple Factuality Probes Detect Hallucinations in Long- ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.880.pdf"
          },
          {
            "title": "Calibrating Long-form Generations from Large Language ...",
            "url": "https://aclanthology.org/2024.findings-emnlp.785.pdf"
          },
          {
            "title": "Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt",
            "url": "https://arxiv.org/pdf/2503.02863v1"
          },
          {
            "title": "(PDF) Reinforcement Learning for Better Verbalized Confidence in Long-Form Generation",
            "url": "https://www.researchgate.net/publication/392315230_Reinforcement_Learning_for_Better_Verbalized_Confidence_in_Long-Form_Generation"
          },
          {
            "title": "Robust Behavior Control in LLMs via Steering Target Atoms",
            "url": "https://aclanthology.org/2025.acl-long.1139.pdf"
          },
          {
            "title": "Fact-Level Confidence Calibration: Empowering Confidence-Guided LLM Self-Correction | OpenReview",
            "url": "https://openreview.net/forum?id=bCAxEwwmBr"
          },
          {
            "title": "Atomic Calibration of LLMs in Long-Form Generations | OpenReview",
            "url": "https://openreview.net/forum?id=rzsjUC45xf"
          }
        ]
      },
      "Based on the web search results, I found relevant research related to your query about probe-guided steering, confidence calibration, and long-form generation. Here are the key findings:\n\n## SteerConf Framework\n\nSteerConf is a novel framework that leverages the steerability of LLMs' confidence scores to enhance their reliability through a steering prompt strategy to guide LLMs in generating confidence scores in a specified direction (e.g., conservative or optimistic) by employing prompts with varying steering intensities.\n\nThe framework systematically steers LLMs' confidence scores to improve their calibration and reliability, introducing three key components: (1) a steering prompt strategy that guides LLMs to produce confidence scores in specified directions by leveraging prompts with varying steering levels; (2) a steered confidence consistency measure that quantifies alignment across multiple steered confidences to enhance calibration; and (3) a steered confidence calibration method that aggregates confidence scores using consistency measures and applies linear quantization for answer selection.\n\n## Long-Form Generation Confidence\n\nFor long-form text generation specifically, research addresses producing well-calibrated factual statements in a single decoding pass through a reinforcement learning (RL)-based approach that enables LLMs to produce well-calibrated confidence estimates during text generation.\n\nAtomic calibration evaluates factuality calibration at a fine-grained level by decomposing long responses into atomic claims.\n\nThe research indicates that explicit instructions can inflate or deflate confidence scores in a regulated manner across multiple models including GPT3.5, LLAMA3-70b, and GPT4."
    ],
    "durationSeconds": 6.868008130999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7a7d21af-9075-439a-9477-bd1d795779a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T01:50:13.154Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KFaqfhftbenmAhioayMHFG`</summary>

```json
{
  "query": "\"read and steer\" OR \"self-probing steering\" OR \"factuality probe confidence steering\" claim-level 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77d90ee3-373c-4476-a4f3-55f34cfee5c8",
  "isSidechain": false,
  "requestId": "req_011Cb5Qf1xnqerP5SSqhATAu",
  "type": "assistant",
  "uuid": "86d01cf6-2a34-4a91-9a60-54e980644286",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQ5mxJ5jukADN4vDiXkqhv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 28679,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 965,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 28679,
          "cache_creation_input_tokens": 965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 965
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-16T01:50:20.262Z_

<details><summary>↩ Tool result · `toolu_01KFaqfhftbenmAhioayMHFG`</summary>

```text
Web search results for query: ""read and steer" OR "self-probing steering" OR "factuality probe confidence steering" claim-level 2026"

Links: [{"title":"Probing and Steering Evaluation Awareness of Language Models","url":"https://arxiv.org/html/2507.01786v2"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation","url":"https://arxiv.org/html/2503.02863v2"},{"title":"Confidence-Guided Probing Methods","url":"https://www.emergentmind.com/topics/confidence-guided-probing-method"},{"title":"Steering Awareness: Models Can Be Trained to Detect ...","url":"https://www.lesswrong.com/posts/D7zQkrDjAKaa293EA/steering-awareness-models-can-be-trained-to-detect"},{"title":"Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt","url":"https://arxiv.org/pdf/2503.02863v1"},{"title":"Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework","url":"https://arxiv.org/html/2503.02863v1"},{"title":"An Introduction to Representation Engineering","url":"https://www.lesswrong.com/posts/3ghj8EuKzwD3MQR5G/an-introduction-to-representation-engineering-an-activation"},{"title":"Linear Personality Probing and Steering in LLMs: A Big Five Study","url":"https://arxiv.org/html/2512.17639v1"},{"title":"EasySteer: A Unified Framework for High-Performance and Extensible LLM Steering | by Dixon | Medium","url":"https://medium.com/@huguosuo/easysteer-a-unified-framework-for-high-performance-and-extensible-llm-steering-fee414a8262d"},{"title":"Depth-Wise Activation Steering for Honest Language Models","url":"https://arxiv.org/html/2512.07667"}]

Based on the search results, I found several relevant research papers and frameworks related to your query about steering, probing, and confidence methods in 2026. Here are the key findings:

## Relevant Research

**1. Probing and Steering Evaluation Awareness** 
Modern language models develop internal representations distinguishing evaluation contexts from deployment scenarios, with linear probes that reliably detect this evaluation awareness. Using evaluations-relevant SAE features to steer models can partially uncover sandbagging.

**2. SteerConf: Steering LLMs for Confidence Elicitation**
LLMs can be steered to produce confidence scores in a specific direction when explicitly instructed to be more conservative or optimistic. SteeringConf comprises three components: a confidence steering mechanism that steers LLM confidence through tailored prompts, an aggregation module that aggregates multiple steered confidences, and a selection criteria to choose the steered answer with best confidence alignment.

**3. Steering Awareness Detection**
LLMs can be trained to detect activation steering robustly, with lightweight fine-tuning allowing models to learn when a steering vector was injected into their residual stream.

**4. Depth-Wise Activation Steering for Honesty**
A training-free activation steering method weights steering strength across network depth using a Gaussian schedule, and on the MASK benchmark, Gaussian scheduling improves honesty over no-steering and single-layer baselines in six of seven models.

These methods represent recent advances in understanding and controlling LLM behavior through probing and steering techniques, with applications to confidence calibration and factuality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86d01cf6-2a34-4a91-9a60-54e980644286",
  "isSidechain": false,
  "promptId": "3f8ed21f-38b7-43d1-9f98-87b3b218ef2a",
  "type": "user",
  "uuid": "dc8b01ea-c5c9-4065-ad23-b3ed7742a0ff",
  "toolUseResult": {
    "query": "\"read and steer\" OR \"self-probing steering\" OR \"factuality probe confidence steering\" claim-level 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011YLdVEyMd5pDAmjunjPisW",
        "content": [
          {
            "title": "Probing and Steering Evaluation Awareness of Language Models",
            "url": "https://arxiv.org/html/2507.01786v2"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation",
            "url": "https://arxiv.org/html/2503.02863v2"
          },
          {
            "title": "Confidence-Guided Probing Methods",
            "url": "https://www.emergentmind.com/topics/confidence-guided-probing-method"
          },
          {
            "title": "Steering Awareness: Models Can Be Trained to Detect ...",
            "url": "https://www.lesswrong.com/posts/D7zQkrDjAKaa293EA/steering-awareness-models-can-be-trained-to-detect"
          },
          {
            "title": "Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt",
            "url": "https://arxiv.org/pdf/2503.02863v1"
          },
          {
            "title": "Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework",
            "url": "https://arxiv.org/html/2503.02863v1"
          },
          {
            "title": "An Introduction to Representation Engineering",
            "url": "https://www.lesswrong.com/posts/3ghj8EuKzwD3MQR5G/an-introduction-to-representation-engineering-an-activation"
          },
          {
            "title": "Linear Personality Probing and Steering in LLMs: A Big Five Study",
            "url": "https://arxiv.org/html/2512.17639v1"
          },
          {
            "title": "EasySteer: A Unified Framework for High-Performance and Extensible LLM Steering | by Dixon | Medium",
            "url": "https://medium.com/@huguosuo/easysteer-a-unified-framework-for-high-performance-and-extensible-llm-steering-fee414a8262d"
          },
          {
            "title": "Depth-Wise Activation Steering for Honest Language Models",
            "url": "https://arxiv.org/html/2512.07667"
          }
        ]
      },
      "Based on the search results, I found several relevant research papers and frameworks related to your query about steering, probing, and confidence methods in 2026. Here are the key findings:\n\n## Relevant Research\n\n**1. Probing and Steering Evaluation Awareness** \nModern language models develop internal representations distinguishing evaluation contexts from deployment scenarios, with linear probes that reliably detect this evaluation awareness. Using evaluations-relevant SAE features to steer models can partially uncover sandbagging.\n\n**2. SteerConf: Steering LLMs for Confidence Elicitation**\nLLMs can be steered to produce confidence scores in a specific direction when explicitly instructed to be more conservative or optimistic. SteeringConf comprises three components: a confidence steering mechanism that steers LLM confidence through tailored prompts, an aggregation module that aggregates multiple steered confidences, and a selection criteria to choose the steered answer with best confidence alignment.\n\n**3. Steering Awareness Detection**\nLLMs can be trained to detect activation steering robustly, with lightweight fine-tuning allowing models to learn when a steering vector was injected into their residual stream.\n\n**4. Depth-Wise Activation Steering for Honesty**\nA training-free activation steering method weights steering strength across network depth using a Gaussian schedule, and on the MASK benchmark, Gaussian scheduling improves honesty over no-steering and single-layer baselines in six of seven models.\n\nThese methods represent recent advances in understanding and controlling LLM behavior through probing and steering techniques, with applications to confidence calibration and factuality."
    ],
    "durationSeconds": 7.102290181000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "86d01cf6-2a34-4a91-9a60-54e980644286",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T01:50:22.506Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dm8MiV5CDN1RCLoLthgKFJ`</summary>

```json
{
  "query": "O'Neill observer model probe steer hallucination 2507.23221 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc8b01ea-c5c9-4065-ad23-b3ed7742a0ff",
  "isSidechain": false,
  "requestId": "req_011Cb5Qfn8rwgUHcGg3EQwVM",
  "type": "assistant",
  "uuid": "852c6d80-b1c3-44ed-a2dd-7a3e2f9c2c6f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018puGJRJFYnYfTvFZXikhiV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 983,
      "cache_read_input_tokens": 29644,
      "output_tokens": 71,
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
          "output_tokens": 71,
          "cache_read_input_tokens": 29644,
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

_source line 25 · 2026-05-16T01:50:29.736Z_

<details><summary>↩ Tool result · `toolu_01Dm8MiV5CDN1RCLoLthgKFJ`</summary>

```text
Web search results for query: "O'Neill observer model probe steer hallucination 2507.23221 2025"

Links: [{"title":"[2507.23221] A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations","url":"https://arxiv.org/abs/2507.23221"},{"title":"A Single Direction of Truth: An Observer Model’s Linear Residual Probe Exposes and Steers Contextual Hallucinations","url":"https://arxiv.org/html/2507.23221"},{"title":"A Single Direction of Truth: An Observer Model’s Linear Residual Probe","url":"https://arxiv.org/pdf/2507.23221"},{"title":"Computer Science Jul 2025","url":"https://arxiv.org/list/cs/2025-07?skip=10600&show=25"},{"title":"Self-Consistency and Probe-Based Hallucination Detection","url":"https://www.emergentmind.com/topics/self-consistency-probe-based-hallucination-detection"},{"title":"Simple Factuality Probes Detect Hallucinations in Long- ...","url":"https://aclanthology.org/2025.findings-emnlp.880.pdf"},{"title":"[2503.01917] Steer LLM Latents for Hallucination Detection","url":"https://arxiv.org/abs/2503.01917"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs","url":"https://arxiv.org/html/2507.16488v1"},{"title":"Investigating VLM Hallucination from a Cognitive Psychology Perspective: A First Step Toward Interpretation with Intriguing Observations","url":"https://arxiv.org/html/2507.03123"},{"title":"A Survey of Multimodal Hallucination Evaluation and Detection","url":"https://arxiv.org/html/2507.19024v2"}]

I found the research paper you're looking for! Here's what it's about:

## Paper Summary

The paper "A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations" was submitted on July 31, 2025 by Charles O'Neill, Slava Chalnev, Chi Chi Zhao, Max Kirkby, and Mudith Jayasekara.

### Key Findings

The research demonstrates a practical interpretability insight: a generator-agnostic observer model detects hallucinations via a single forward pass and a linear probe on its residual stream.

This probe isolates a single, transferable linear direction separating hallucinated from faithful text, outperforming baselines by 5-27 points and showing robust mid-layer performance across Gemma-2 models (2B to 27B).

Critically, manipulating this direction causally steers generator hallucination rates, proving its actionability.

### Contributions

The results offer novel evidence of internal, low-dimensional hallucination tracking linked to specific MLP sub-circuits, exploitable for detection and mitigation. The authors release the 2000-example ContraTales benchmark for realistic assessment of such solutions.

The paper can be found on arXiv at: https://arxiv.org/abs/2507.23221


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "852c6d80-b1c3-44ed-a2dd-7a3e2f9c2c6f",
  "isSidechain": false,
  "promptId": "3f8ed21f-38b7-43d1-9f98-87b3b218ef2a",
  "type": "user",
  "uuid": "8bd67a7a-d428-4e3f-95c1-5334ecbd21c9",
  "toolUseResult": {
    "query": "O'Neill observer model probe steer hallucination 2507.23221 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0152KF4cRXHmE9Vk5Rdj6UmD",
        "content": [
          {
            "title": "[2507.23221] A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations",
            "url": "https://arxiv.org/abs/2507.23221"
          },
          {
            "title": "A Single Direction of Truth: An Observer Model’s Linear Residual Probe Exposes and Steers Contextual Hallucinations",
            "url": "https://arxiv.org/html/2507.23221"
          },
          {
            "title": "A Single Direction of Truth: An Observer Model’s Linear Residual Probe",
            "url": "https://arxiv.org/pdf/2507.23221"
          },
          {
            "title": "Computer Science Jul 2025",
            "url": "https://arxiv.org/list/cs/2025-07?skip=10600&show=25"
          },
          {
            "title": "Self-Consistency and Probe-Based Hallucination Detection",
            "url": "https://www.emergentmind.com/topics/self-consistency-probe-based-hallucination-detection"
          },
          {
            "title": "Simple Factuality Probes Detect Hallucinations in Long- ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.880.pdf"
          },
          {
            "title": "[2503.01917] Steer LLM Latents for Hallucination Detection",
            "url": "https://arxiv.org/abs/2503.01917"
          },
          {
            "title": "ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs",
            "url": "https://arxiv.org/html/2507.16488v1"
          },
          {
            "title": "Investigating VLM Hallucination from a Cognitive Psychology Perspective: A First Step Toward Interpretation with Intriguing Observations",
            "url": "https://arxiv.org/html/2507.03123"
          },
          {
            "title": "A Survey of Multimodal Hallucination Evaluation and Detection",
            "url": "https://arxiv.org/html/2507.19024v2"
          }
        ]
      },
      "I found the research paper you're looking for! Here's what it's about:\n\n## Paper Summary\n\nThe paper \"A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations\" was submitted on July 31, 2025 by Charles O'Neill, Slava Chalnev, Chi Chi Zhao, Max Kirkby, and Mudith Jayasekara.\n\n### Key Findings\n\nThe research demonstrates a practical interpretability insight: a generator-agnostic observer model detects hallucinations via a single forward pass and a linear probe on its residual stream.\n\nThis probe isolates a single, transferable linear direction separating hallucinated from faithful text, outperforming baselines by 5-27 points and showing robust mid-layer performance across Gemma-2 models (2B to 27B).\n\nCritically, manipulating this direction causally steers generator hallucination rates, proving its actionability.\n\n### Contributions\n\nThe results offer novel evidence of internal, low-dimensional hallucination tracking linked to specific MLP sub-circuits, exploitable for detection and mitigation. The authors release the 2000-example ContraTales benchmark for realistic assessment of such solutions.\n\nThe paper can be found on arXiv at: https://arxiv.org/abs/2507.23221"
    ],
    "durationSeconds": 7.227075335999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "852c6d80-b1c3-44ed-a2dd-7a3e2f9c2c6f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation  **状态**: 待审阅   **级别**:…",
  "leafUuid": "8bd67a7a-d428-4e3f-95c1-5334ecbd21c9",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate claim-level confidence calibration proposal",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac"
}
```

---

### Tool call

_source line 28 · 2026-05-16T01:50:32.297Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015QunJdHBEMexSaLWHs7twv`</summary>

```json
{
  "query": "CLAS contextual linear activation steering Hsu 2604.24693 Llama 70B 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bd67a7a-d428-4e3f-95c1-5334ecbd21c9",
  "isSidechain": false,
  "requestId": "req_011Cb5QgUch5vhfUofTJijQF",
  "type": "assistant",
  "uuid": "4ccbcfd2-c8aa-47fb-8715-89f3a1c95298",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UC3nEWH5MabwP2vR87k451",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 901,
      "cache_read_input_tokens": 30627,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 901,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 30627,
          "cache_creation_input_tokens": 901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 901
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

_source line 29 · 2026-05-16T01:50:38.555Z_

<details><summary>↩ Tool result · `toolu_015QunJdHBEMexSaLWHs7twv`</summary>

```text
Web search results for query: "CLAS contextual linear activation steering Hsu 2604.24693 Llama 70B 2026"

Links: [{"title":"Contextual Linear Activation Steering of Language Models","url":"https://arxiv.org/html/2604.24693"},{"title":"[2604.24693] Contextual Linear Activation Steering of Language Models","url":"https://arxiv.org/abs/2604.24693"},{"title":"GitHub - bhdsc/CLAS: Official implementation of Contextual Linear Activation Steering of Language Models (CLAS) · GitHub","url":"https://github.com/bhdsc/CLAS"},{"title":"[2312.06681] Steering Llama 2 via Contrastive Activation Addition","url":"https://arxiv.org/abs/2312.06681"},{"title":"Steering Llama 2 via Contrastive Activation Addition Anonymous ACL submission","url":"https://openreview.net/pdf/fef73d66faa293a57e7fb327978f41a61cd38637.pdf"},{"title":"Scaling laws for activation steering with Llama 2 models and refusal mechanisms","url":"https://arxiv.org/html/2507.11771v1"},{"title":"Steering Llama 2 via Contrastive Activation Addition","url":"https://www.researchgate.net/publication/384215189_Steering_Llama_2_via_Contrastive_Activation_Addition"},{"title":"Steering Llama 2 via Contrastive Activation Addition - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.828/"},{"title":"Steering Llama 2 via Contrastive Activation Addition","url":"https://aclanthology.org/2024.acl-long.828.pdf"},{"title":"Steering Llama 2 via Contrastive Activation Addition","url":"https://arxiv.org/html/2312.06681v2"}]

Based on the search results, here's what I found about CLAS (Contextual Linear Activation Steering):

## Overview

CLAS is a method that dynamically adapts linear activation steering to context-dependent steering strengths. The paper was authored by Brandon Hsu and 3 other authors, and it addresses limitations of existing activation steering approaches.

## Key Problem and Solution

Existing methods often apply a fixed steering strength to all tokens, resulting in inconsistent steering quality across diverse input prompts. CLAS solves this by dynamically adjusting steering strengths based on context.

## Performance and Evaluation

Across eleven steering benchmarks and four model families, CLAS consistently outperforms standard linear activation steering and matches or exceeds the performance of ReFT and LoRA in settings with limited labeled data. The method was evaluated across four different instruction-tuned models: Qwen2.5-7B, Llama-3.1-70B, Llama-3.1-8B, and Llama-3.2-1B.

## Implementation Details

CLAS learns a per-block sensing vector using AdamW to minimize the next-token prediction loss. The authors propose CLAS as a scalable, interpretable, and accurate method for specializing and steering large language models.

The paper (arXiv:2604.24693) was submitted on April 27, 2026, and has an official implementation available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ccbcfd2-c8aa-47fb-8715-89f3a1c95298",
  "isSidechain": false,
  "promptId": "3f8ed21f-38b7-43d1-9f98-87b3b218ef2a",
  "type": "user",
  "uuid": "a016a44b-dd3e-4715-b970-774a1e5fbac5",
  "toolUseResult": {
    "query": "CLAS contextual linear activation steering Hsu 2604.24693 Llama 70B 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RvR9DWj6Buy4ueWLWVQLPJ",
        "content": [
          {
            "title": "Contextual Linear Activation Steering of Language Models",
            "url": "https://arxiv.org/html/2604.24693"
          },
          {
            "title": "[2604.24693] Contextual Linear Activation Steering of Language Models",
            "url": "https://arxiv.org/abs/2604.24693"
          },
          {
            "title": "GitHub - bhdsc/CLAS: Official implementation of Contextual Linear Activation Steering of Language Models (CLAS) · GitHub",
            "url": "https://github.com/bhdsc/CLAS"
          },
          {
            "title": "[2312.06681] Steering Llama 2 via Contrastive Activation Addition",
            "url": "https://arxiv.org/abs/2312.06681"
          },
          {
            "title": "Steering Llama 2 via Contrastive Activation Addition Anonymous ACL submission",
            "url": "https://openreview.net/pdf/fef73d66faa293a57e7fb327978f41a61cd38637.pdf"
          },
          {
            "title": "Scaling laws for activation steering with Llama 2 models and refusal mechanisms",
            "url": "https://arxiv.org/html/2507.11771v1"
          },
          {
            "title": "Steering Llama 2 via Contrastive Activation Addition",
            "url": "https://www.researchgate.net/publication/384215189_Steering_Llama_2_via_Contrastive_Activation_Addition"
          },
          {
            "title": "Steering Llama 2 via Contrastive Activation Addition - ACL Anthology",
            "url": "https://aclanthology.org/2024.acl-long.828/"
          },
          {
            "title": "Steering Llama 2 via Contrastive Activation Addition",
            "url": "https://aclanthology.org/2024.acl-long.828.pdf"
          },
          {
            "title": "Steering Llama 2 via Contrastive Activation Addition",
            "url": "https://arxiv.org/html/2312.06681v2"
          }
        ]
      },
      "Based on the search results, here's what I found about CLAS (Contextual Linear Activation Steering):\n\n## Overview\n\nCLAS is a method that dynamically adapts linear activation steering to context-dependent steering strengths. The paper was authored by Brandon Hsu and 3 other authors, and it addresses limitations of existing activation steering approaches.\n\n## Key Problem and Solution\n\nExisting methods often apply a fixed steering strength to all tokens, resulting in inconsistent steering quality across diverse input prompts. CLAS solves this by dynamically adjusting steering strengths based on context.\n\n## Performance and Evaluation\n\nAcross eleven steering benchmarks and four model families, CLAS consistently outperforms standard linear activation steering and matches or exceeds the performance of ReFT and LoRA in settings with limited labeled data. The method was evaluated across four different instruction-tuned models: Qwen2.5-7B, Llama-3.1-70B, Llama-3.1-8B, and Llama-3.2-1B.\n\n## Implementation Details\n\nCLAS learns a per-block sensing vector using AdamW to minimize the next-token prediction loss. The authors propose CLAS as a scalable, interpretable, and accurate method for specializing and steering large language models.\n\nThe paper (arXiv:2604.24693) was submitted on April 27, 2026, and has an official implementation available on GitHub."
    ],
    "durationSeconds": 6.2532481359999945,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4ccbcfd2-c8aa-47fb-8715-89f3a1c95298",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T01:50:40.640Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JUeBMDWHSQMCJAhmX5bczY`</summary>

```json
{
  "query": "AUSteer atomic unit steering activation decomposition fine-grained 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a016a44b-dd3e-4715-b970-774a1e5fbac5",
  "isSidechain": false,
  "requestId": "req_011Cb5Qh8L5PUZwSvVNYa6fT",
  "type": "assistant",
  "uuid": "f4c3148e-f8b8-4554-9ff1-390249e2874e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqE5egKoS8YPPuEkuPPT4k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 931,
      "cache_read_input_tokens": 31528,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 931,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 31528,
          "cache_creation_input_tokens": 931,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 931
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

_source line 31 · 2026-05-16T01:50:47.593Z_

<details><summary>↩ Tool result · `toolu_01JUeBMDWHSQMCJAhmX5bczY`</summary>

```text
Web search results for query: "AUSteer atomic unit steering activation decomposition fine-grained 2026"

Links: [{"title":"GitHub - zijian678/AUSteer: ICLR 2026 Fine-Grained Activation Steering: Steering Less, Achieving More · GitHub","url":"https://github.com/zijian678/AUSteer"},{"title":"[2602.04428] Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/abs/2602.04428"},{"title":"Published as a conference paper at ICLR 2026 FINE-GRAINED ACTIVATION STEERING:","url":"https://openreview.net/pdf?id=guSVafqhrB"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More | OpenReview","url":"https://openreview.net/forum?id=guSVafqhrB"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/html/2602.04428v1"},{"title":"FINE-GRAINED ACTIVATION STEERING","url":"https://openreview.net/pdf/a9cada056ebe41df04f02a22bc25b2fe3d125857.pdf"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"EmoSteer-TTS: Fine-Grained and Training-Free Emotion-Controllable Text-to-Speech via Activation Steering | OpenReview","url":"https://openreview.net/forum?id=6p9n68cxGM"},{"title":"[2508.03543] EmoSteer-TTS: Fine-Grained and Training-Free Emotion-Controllable Text-to-Speech via Activation Steering","url":"https://arxiv.org/abs/2508.03543"},{"title":"EmoSteer-TTS: Fine-Grained and Training-Free Emotion-Controllable Text-to-Speech via Activation Steering | Request PDF","url":"https://www.researchgate.net/publication/394322706_EmoSteer-TTS_Fine-Grained_and_Training-Free_Emotion-Controllable_Text-to-Speech_via_Activation_Steering"}]

Based on the search results, I found comprehensive information about AUSteer:

## AUSteer Overview

AUSteer is an ICLR 2026 paper on "Fine-Grained Activation Steering: Steering Less, Achieving More" that breaks LLM blocks into fine-grained atomic units (AUs) for targeted intervention.

## Core Concept

Block-level activations are inherently heterogeneous, entangling beneficial, irrelevant, and harmful features. The method decomposes block activations into fine-grained atomic unit (AU)-level activations, where each AU-level activation corresponds to a single dimension of the block activation, and each AU denotes a slice of the block weight matrix.

## The Problem Addressed

Existing methods typically intervene at the block level, steering the bundled activations of selected attention heads, feedforward networks, or residual streams, which is inefficient because different AUs or dimensions control distinct token distributions in LLM outputs.

## Methodology

AUSteer is a simple and efficient method that operates at a finer granularity of the AU level. It first identifies discriminative AUs globally by computing activation momenta on contrastive samples, then assigns adaptive steering strengths tailored to diverse inputs and selected AU activations.

## Results

Comprehensive experiments on multiple LLMs and tasks show that AUSteer consistently surpasses advanced baselines while steering considerably fewer activations. Using far fewer steered activations (at most 100), AUSteer significantly outperforms these methods across diverse tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4c3148e-f8b8-4554-9ff1-390249e2874e",
  "isSidechain": false,
  "promptId": "3f8ed21f-38b7-43d1-9f98-87b3b218ef2a",
  "type": "user",
  "uuid": "c5426930-9ba2-4b2c-957f-e80ff5a0b1dd",
  "toolUseResult": {
    "query": "AUSteer atomic unit steering activation decomposition fine-grained 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HFGTwjEpvZhdfnbvjDtZte",
        "content": [
          {
            "title": "GitHub - zijian678/AUSteer: ICLR 2026 Fine-Grained Activation Steering: Steering Less, Achieving More · GitHub",
            "url": "https://github.com/zijian678/AUSteer"
          },
          {
            "title": "[2602.04428] Fine-Grained Activation Steering: Steering Less, Achieving More",
            "url": "https://arxiv.org/abs/2602.04428"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 FINE-GRAINED ACTIVATION STEERING:",
            "url": "https://openreview.net/pdf?id=guSVafqhrB"
          },
          {
            "title": "Fine-Grained Activation Steering: Steering Less, Achieving More | OpenReview",
            "url": "https://openreview.net/forum?id=guSVafqhrB"
          },
          {
            "title": "Fine-Grained Activation Steering: Steering Less, Achieving More",
            "url": "https://arxiv.org/html/2602.04428v1"
          },
          {
            "title": "FINE-GRAINED ACTIVATION STEERING",
            "url": "https://openreview.net/pdf/a9cada056ebe41df04f02a22bc25b2fe3d125857.pdf"
          },
          {
            "title": "Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra",
            "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"
          },
          {
            "title": "EmoSteer-TTS: Fine-Grained and Training-Free Emotion-Controllable Text-to-Speech via Activation Steering | OpenReview",
            "url": "https://openreview.net/forum?id=6p9n68cxGM"
          },
          {
            "title": "[2508.03543] EmoSteer-TTS: Fine-Grained and Training-Free Emotion-Controllable Text-to-Speech via Activation Steering",
            "url": "https://arxiv.org/abs/2508.03543"
          },
          {
            "title": "EmoSteer-TTS: Fine-Grained and Training-Free Emotion-Controllable Text-to-Speech via Activation Steering | Request PDF",
            "url": "https://www.researchgate.net/publication/394322706_EmoSteer-TTS_Fine-Grained_and_Training-Free_Emotion-Controllable_Text-to-Speech_via_Activation_Steering"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about AUSteer:\n\n## AUSteer Overview\n\nAUSteer is an ICLR 2026 paper on \"Fine-Grained Activation Steering: Steering Less, Achieving More\" that breaks LLM blocks into fine-grained atomic units (AUs) for targeted intervention.\n\n## Core Concept\n\nBlock-level activations are inherently heterogeneous, entangling beneficial, irrelevant, and harmful features. The method decomposes block activations into fine-grained atomic unit (AU)-level activations, where each AU-level activation corresponds to a single dimension of the block activation, and each AU denotes a slice of the block weight matrix.\n\n## The Problem Addressed\n\nExisting methods typically intervene at the block level, steering the bundled activations of selected attention heads, feedforward networks, or residual streams, which is inefficient because different AUs or dimensions control distinct token distributions in LLM outputs.\n\n## Methodology\n\nAUSteer is a simple and efficient method that operates at a finer granularity of the AU level. It first identifies discriminative AUs globally by computing activation momenta on contrastive samples, then assigns adaptive steering strengths tailored to diverse inputs and selected AU activations.\n\n## Results\n\nComprehensive experiments on multiple LLMs and tasks show that AUSteer consistently surpasses advanced baselines while steering considerably fewer activations. Using far fewer steered activations (at most 100), AUSteer significantly outperforms these methods across diverse tasks."
    ],
    "durationSeconds": 6.949780883999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f4c3148e-f8b8-4554-9ff1-390249e2874e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-16T01:50:47.597Z_

```json
{
  "parentUuid": "c5426930-9ba2-4b2c-957f-e80ff5a0b1dd",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8498bd34-9b35-469b-9924-61d980238fa0",
  "timestamp": "2026-05-16T01:50:47.597Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 33 · 2026-05-16T01:50:51.286Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LeLjnuVeR9iWVtvNtgS6AX`</summary>

```json
{
  "query": "activation steering confidence calibration claim level hallucination hedging verbal uncertainty 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8498bd34-9b35-469b-9924-61d980238fa0",
  "isSidechain": false,
  "requestId": "req_011Cb5QhnzWmphcr3HxExVBr",
  "type": "assistant",
  "uuid": "ff26ece7-200f-40f6-8701-441376b92b66",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018J5fnqK8BgtyVFsZpQRP7f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 32459,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 32459,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1151
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

_source line 34 · 2026-05-16T01:50:58.636Z_

<details><summary>↩ Tool result · `toolu_01LeLjnuVeR9iWVtvNtgS6AX`</summary>

```text
Web search results for query: "activation steering confidence calibration claim level hallucination hedging verbal uncertainty 2026 arxiv"

Links: [{"title":"[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/abs/2503.14477"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/html/2503.14477v1"},{"title":"Hallucinations Undermine Trust; Metacognition is a Way Forward","url":"https://arxiv.org/html/2605.01428"},{"title":"[2603.17839] How do LLMs Compute Verbal Confidence","url":"https://arxiv.org/abs/2603.17839"},{"title":"[2601.15703] Agentic Uncertainty Quantification","url":"https://arxiv.org/abs/2601.15703"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/397424902_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"VL-Calibration: Decoupled Confidence Calibration for Large Vision-Language Models Reasoning","url":"https://arxiv.org/html/2604.09529v1"},{"title":"Trusted Uncertainty in Large Language Models: A Unified Framework for Confidence Calibration and Risk-Controlled Refusal","url":"https://arxiv.org/html/2509.01455"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.187/"},{"title":"Revisiting Uncertainty Estimation and Calibration of Large ...","url":"https://arxiv.org/pdf/2505.23854"}]

Based on the search results, I found several highly relevant papers that match your query. Here are the key findings:

## Primary Result: "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations"

The research finds that "verbal uncertainty" is governed by a single linear feature in the representation space of LLMs, and demonstrates that the mismatch between semantic and verbal uncertainty is a better predictor of hallucinations than semantic uncertainty alone, with interventions on verbal uncertainty at inference time achieving an average relative reduction of ~30% in confident hallucinations on short-form answers.

## Related Recent Work (2026)

Another recent paper on "How do LLMs Compute Verbal Confidence" uses activation steering, patching, noising, and swap experiments to reveal that confidence representations emerge at answer-adjacent positions before appearing at the verbalization site.

## Additional Related Papers

Other papers in this research space include:
- An "Agentic Uncertainty Quantification" framework that transforms verbalized uncertainty into active, bi-directional control signals through System 1 (Uncertainty-Aware Memory) and System 2 (Uncertainty-Aware Reflection) mechanisms.
- Work noting that hallucinations should be understood not as any error, but as confident errors—incorrect information delivered without appropriate qualification—and that an error communicated with appropriate hedging is not a hallucination but a hypothesis offered for consideration.

These papers collectively address how LLMs compute and express verbal uncertainty, how this relates to semantic uncertainty, and methods for steering activations to calibrate confidence and reduce hallucinations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff26ece7-200f-40f6-8701-441376b92b66",
  "isSidechain": false,
  "promptId": "3f8ed21f-38b7-43d1-9f98-87b3b218ef2a",
  "type": "user",
  "uuid": "20a8ea00-2002-4771-9591-a33d7a315974",
  "toolUseResult": {
    "query": "activation steering confidence calibration claim level hallucination hedging verbal uncertainty 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UrtEprEQkPp2mPmHTd8DWd",
        "content": [
          {
            "title": "[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations",
            "url": "https://arxiv.org/abs/2503.14477"
          },
          {
            "title": "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations",
            "url": "https://arxiv.org/html/2503.14477v1"
          },
          {
            "title": "Hallucinations Undermine Trust; Metacognition is a Way Forward",
            "url": "https://arxiv.org/html/2605.01428"
          },
          {
            "title": "[2603.17839] How do LLMs Compute Verbal Confidence",
            "url": "https://arxiv.org/abs/2603.17839"
          },
          {
            "title": "[2601.15703] Agentic Uncertainty Quantification",
            "url": "https://arxiv.org/abs/2601.15703"
          },
          {
            "title": "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations",
            "url": "https://www.researchgate.net/publication/397424902_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"
          },
          {
            "title": "VL-Calibration: Decoupled Confidence Calibration for Large Vision-Language Models Reasoning",
            "url": "https://arxiv.org/html/2604.09529v1"
          },
          {
            "title": "Trusted Uncertainty in Large Language Models: A Unified Framework for Confidence Calibration and Risk-Controlled Refusal",
            "url": "https://arxiv.org/html/2509.01455"
          },
          {
            "title": "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.187/"
          },
          {
            "title": "Revisiting Uncertainty Estimation and Calibration of Large ...",
            "url": "https://arxiv.org/pdf/2505.23854"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers that match your query. Here are the key findings:\n\n## Primary Result: \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\"\n\nThe research finds that \"verbal uncertainty\" is governed by a single linear feature in the representation space of LLMs, and demonstrates that the mismatch between semantic and verbal uncertainty is a better predictor of hallucinations than semantic uncertainty alone, with interventions on verbal uncertainty at inference time achieving an average relative reduction of ~30% in confident hallucinations on short-form answers.\n\n## Related Recent Work (2026)\n\nAnother recent paper on \"How do LLMs Compute Verbal Confidence\" uses activation steering, patching, noising, and swap experiments to reveal that confidence representations emerge at answer-adjacent positions before appearing at the verbalization site.\n\n## Additional Related Papers\n\nOther papers in this research space include:\n- An \"Agentic Uncertainty Quantification\" framework that transforms verbalized uncertainty into active, bi-directional control signals through System 1 (Uncertainty-Aware Memory) and System 2 (Uncertainty-Aware Reflection) mechanisms.\n- Work noting that hallucinations should be understood not as any error, but as confident errors—incorrect information delivered without appropriate qualification—and that an error communicated with appropriate hedging is not a hallucination but a hypothesis offered for consideration.\n\nThese papers collectively address how LLMs compute and express verbal uncertainty, how this relates to semantic uncertainty, and methods for steering activations to calibrate confidence and reduce hallucinations."
    ],
    "durationSeconds": 7.334156008999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ff26ece7-200f-40f6-8701-441376b92b66",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-16T01:51:01.349Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me check if there's any very recent work that directly combines factuality probes with confidence steering in the way RaS proposes:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20a8ea00-2002-4771-9591-a33d7a315974",
  "isSidechain": false,
  "requestId": "req_011Cb5QicJ7TzJKvhMgyAwyg",
  "type": "assistant",
  "uuid": "bf1dc5ed-63ac-4cee-b478-e6158aa19c63",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGWs2h99JpptL7hsQDEySQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 33610,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 33610,
          "cache_creation_input_tokens": 936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 936
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

_source line 36 · 2026-05-16T01:51:02.342Z_

Now let me check one more critical search — whether anyone has already combined these specific components:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf1dc5ed-63ac-4cee-b478-e6158aa19c63",
  "isSidechain": false,
  "requestId": "req_011Cb5QicJ7TzJKvhMgyAwyg",
  "type": "assistant",
  "uuid": "dcc728b6-4910-4ae5-b0c4-a3464d793643",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGWs2h99JpptL7hsQDEySQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 33610,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 33610,
          "cache_creation_input_tokens": 936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 936
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

_source line 37 · 2026-05-16T01:51:02.825Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TnMWGXj8Pzo3ForLcGxVXe`</summary>

```json
{
  "query": "\"factuality probe\" \"confidence direction\" steering long-form generation real-time online 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcc728b6-4910-4ae5-b0c4-a3464d793643",
  "isSidechain": false,
  "requestId": "req_011Cb5QicJ7TzJKvhMgyAwyg",
  "type": "assistant",
  "uuid": "d18206f5-dc43-4015-b853-7e19e7973f6f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGWs2h99JpptL7hsQDEySQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 33610,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 33610,
          "cache_creation_input_tokens": 936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 936
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

_source line 38 · 2026-05-16T01:51:10.355Z_

<details><summary>↩ Tool result · `toolu_01TnMWGXj8Pzo3ForLcGxVXe`</summary>

```text
Web search results for query: ""factuality probe" "confidence direction" steering long-form generation real-time online 2026"

Links: [{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.880/"},{"title":"Survey on Factuality in Large Language Models","url":"https://dl.acm.org/doi/pdf/10.1145/3742420"},{"title":"The FACTS Leaderboard: A Comprehensive Benchmark for ...","url":"https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf"},{"title":"Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation | Request PDF","url":"https://www.researchgate.net/publication/397419109_Simple_Factuality_Probes_Detect_Hallucinations_in_Long-Form_Natural_Language_Generation"},{"title":"Investigating Factuality in Long-Form Text Generation: The Roles of Self-Known and Self-Unknown","url":"https://arxiv.org/html/2411.15993v2"},{"title":"Long-form factuality in large language models | OpenReview","url":"https://openreview.net/forum?id=4M9f8VMt2C"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation","url":"https://arxiv.org/html/2503.02863v2"},{"title":"FactScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation | Research - AI at Meta","url":"https://ai.meta.com/research/publications/factscore-fine-grained-atomic-evaluation-of-factual-precision-in-long-form-text-generation/"},{"title":"Fact Extraction and VERification","url":"https://fever.ai/"}]

Based on the search results, I found several relevant papers and research related to your query about factuality probes, confidence direction, and steering generation:

## Key Research Findings

LLM hidden states are highly predictive of factuality in long-form natural language generation and this information can be efficiently extracted at inference time using a lightweight probe. This appears in a paper titled "Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation," published in the Findings of EMNLP 2025.

### Real-time Generation Monitoring

A real-time, token-by-token monitoring framework continuously scores the factuality of partial responses during generation, and when an imminent hallucination is detected mid-generation, the decoding trajectory is dynamically altered to enforce factual consistency. This approach addresses the problem where "a single incorrect token forces subsequent fabrications."

### Confidence-based Steering

By applying different steering levels, LLMs can be probed for confidence in different directions and intensities, which can help better understand the LLM's confidence and uncertainty and facilitate accurate confidence estimation. This relates to the "SteerConf" framework for steering LLMs for confidence elicitation, published in May 2025.

### Long-form Generation Challenges

Research investigating factuality of long-form text generation across different language model families observes a consistent decline in factuality in sentences generated later in the sequence, with possible factors including diminished self-knowledge in later generations and the accumulation of earlier generation errors.

These developments represent active research areas in mitigating hallucinations and improving factual consistency in LLM generation through real-time monitoring and steering mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d18206f5-dc43-4015-b853-7e19e7973f6f",
  "isSidechain": false,
  "promptId": "3f8ed21f-38b7-43d1-9f98-87b3b218ef2a",
  "type": "user",
  "uuid": "db571c75-3548-488e-8dd1-d8ecad57644b",
  "toolUseResult": {
    "query": "\"factuality probe\" \"confidence direction\" steering long-form generation real-time online 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014kxeyuVkpMxZQcrEfbGuQo",
        "content": [
          {
            "title": "GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub",
            "url": "https://github.com/EdinburghNLP/awesome-hallucination-detection"
          },
          {
            "title": "Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-emnlp.880/"
          },
          {
            "title": "Survey on Factuality in Large Language Models",
            "url": "https://dl.acm.org/doi/pdf/10.1145/3742420"
          },
          {
            "title": "The FACTS Leaderboard: A Comprehensive Benchmark for ...",
            "url": "https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf"
          },
          {
            "title": "Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation | Request PDF",
            "url": "https://www.researchgate.net/publication/397419109_Simple_Factuality_Probes_Detect_Hallucinations_in_Long-Form_Natural_Language_Generation"
          },
          {
            "title": "Investigating Factuality in Long-Form Text Generation: The Roles of Self-Known and Self-Unknown",
            "url": "https://arxiv.org/html/2411.15993v2"
          },
          {
            "title": "Long-form factuality in large language models | OpenReview",
            "url": "https://openreview.net/forum?id=4M9f8VMt2C"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation",
            "url": "https://arxiv.org/html/2503.02863v2"
          },
          {
            "title": "FactScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation | Research - AI at Meta",
            "url": "https://ai.meta.com/research/publications/factscore-fine-grained-atomic-evaluation-of-factual-precision-in-long-form-text-generation/"
          },
          {
            "title": "Fact Extraction and VERification",
            "url": "https://fever.ai/"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and research related to your query about factuality probes, confidence direction, and steering generation:\n\n## Key Research Findings\n\nLLM hidden states are highly predictive of factuality in long-form natural language generation and this information can be efficiently extracted at inference time using a lightweight probe. This appears in a paper titled \"Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation,\" published in the Findings of EMNLP 2025.\n\n### Real-time Generation Monitoring\n\nA real-time, token-by-token monitoring framework continuously scores the factuality of partial responses during generation, and when an imminent hallucination is detected mid-generation, the decoding trajectory is dynamically altered to enforce factual consistency. This approach addresses the problem where \"a single incorrect token forces subsequent fabrications.\"\n\n### Confidence-based Steering\n\nBy applying different steering levels, LLMs can be probed for confidence in different directions and intensities, which can help better understand the LLM's confidence and uncertainty and facilitate accurate confidence estimation. This relates to the \"SteerConf\" framework for steering LLMs for confidence elicitation, published in May 2025.\n\n### Long-form Generation Challenges\n\nResearch investigating factuality of long-form text generation across different language model families observes a consistent decline in factuality in sentences generated later in the sequence, with possible factors including diminished self-knowledge in later generations and the accumulation of earlier generation errors.\n\nThese developments represent active research areas in mitigating hallucinations and improving factual consistency in LLM generation through real-time monitoring and steering mechanisms."
    ],
    "durationSeconds": 7.525640596999991,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d18206f5-dc43-4015-b853-7e19e7973f6f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation  **状态**: 待审阅   **级别**:…",
  "leafUuid": "db571c75-3548-488e-8dd1-d8ecad57644b",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate claim-level confidence calibration proposal",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac"
}
```

---

### Assistant

_source line 41 · 2026-05-16T01:52:16.362Z_

<details><summary>Logged reasoning block</summary>

```text
Based on my thorough search, I haven't found any existing work that directly combines claim-level factuality probes with calibrated confidence steering in long-form generation in a single pass. The gap identified in the proposal appears to be genuine.

Now let me finalize my assessment.

## Summary of Key Findings from Search

1. **The gap is real**: No existing work combines claim-level factuality probing with calibrated confidence steering in long-form generation in a single forward pass. The closest works are:
   - O'Neill et al.: probe→steer but external observer + binary
   - Miao & Ungar: accuracy-confidence orthogonality + CAA but response-level QA on small models
   - Han et al.: claim-level probes but binary neuron clamping
   - CARE: fact-level calibration but post-hoc

2. **The space is extremely crowded**: There are many concurrent works in this area, and the rate of publication is high. Risk of being scooped or having the novelty diluted by the time of submission.

3. **AUSteer (ICLR 2026)** is a relevant new method for fine-grained activation steering, though it's designed for general behavioral steering rather than confidence calibration in long-form generation specifically.

4. **The combination is predictable**: Given that Miao & Ungar explicitly state "extending" their approach, the natural next step of combining claim-level probing with confidence steering feels somewhat inevitable rather than surprising.

Now I'm considering whether simpler alternatives could achieve similar results. Post-hoc prompting—decomposing generated text into claims and regenerating uncertain ones with hedging—would be much simpler but requires multiple passes, whereas RaS operates in a single pass. There's also the option of applying uniform confidence steering without claim-level targeting, which would be even more straightforward but less precise. The question is whether these trade-offs actually matter in practice.

Looking at the ablations, if uniform steering performs nearly as well as the probe-guided approach, that suggests the added complexity of claim-level detection might not be justified. The core threat here is moderate—the paper needs to convincingly demonstrate that the integrated, single-pass steering genuinely outperforms these simpler baselines rather than just being a more complex version of something that already works.

On the foundational assumptions, the accuracy-confidence orthogonality at this scale is acknowledged as uncertain and tested empirically, which is good. But there's a question about whether linear probes trained offline actually transfer reliably when used for online monitoring during generation.

The real concerns are whether steering mid-sentence produces coherent output, whether the smoothing window is appropriately sized for the signal, and whether steering along the confidence direction truly leaves content untouched or if it subtly shifts what the model generates. These are all empirical questions that matter.

The novelty is mostly combinatorial—pulling together existing techniques from prior work into a single-pass framework. The individual pieces aren't new, though the specific integration is.

What's genuinely novel here is extending the core insight to claim-level long-form generation at 70B scale, which prior work identified as an open question. But the fundamental idea of reading internal accuracy signals and steering expressed confidence to match comes directly from prior work, so this feels more like a natural follow-up than a fundamental discovery. (vs. binary clamping)
3. O'Neill et al. (2025): RaS uses self-probing (vs. external observer) + graded (vs. binary)
4. CARE (SIGIR 2025): RaS does single-pass (vs. post-hoc)
5. CLAS (2026): RaS uses factuality-probe-driven (vs. general context)
6. CAST (ICLR 2025): RaS uses continuous factuality signal (vs. PCA-derived categories)
7. Ji et al. (EMNLP 2025): RaS extends to claim-level + long-form
8. AUSteer (ICLR 2026): RaS targets confidence calibration specifically

The core contribution boils down to applying the read-accuracy-steer-confidence paradigm at claim-level granularity in long-form generation within a single pass—a meaningful but incremental extension of existing work.

The problem itself matters: users genuinely need to understand which parts of a long response are reliable versus uncertain. If this works, it could let models naturally express hedged claims in extended outputs, demonstrate that accuracy-confidence separation holds at scale, and provide a general framework for probe-guided steering. That said, the approach has real constraints—it's architecture-specific, requires per-model probe training without zero-shot transfer, and faces other practical limitations.

A 25% ECE reduction would be respectable but not shocking given the existing components; 40%+ would turn heads. The orthogonality result at 70B scale is interesting but secondary. The related work is impressively thorough, which actually underscores how crowded this space has become—the novelty here is really the specific conjunction of constraints rather than any single breakthrough idea.

The proposal is solid and well-positioned, but the core contribution boils down to combining existing techniques in a fairly straightforward way. If it works as expected, reviewers would likely think "yeah, that makes sense," which limits the impact. The research landscape is saturated with similar efforts, creating real risk of being scooped or having the contribution feel incremental. Simpler baselines could potentially match the results too.

I'm estimating 25-35% probability, around 28% median. The ceiling is held back by the combinatorial nature of the novelty, the unsurprising expected outcome, and the extremely competitive field. Let me actually reconsider this more carefully.

There are some genuine strengths I should weigh more heavily: if the experiments pan out, the paper tells a clean story with solid ablations and positioning. The orthogonality result at 70B is a meaningful finding on its own. The sub-sentence monitoring mechanism is a real technical contribution, not trivial. The practical advantage of avoiding base model training matters. And EMNLP does reward empirical rigor and practical methods. But the combinatorial novelty, predictable results, and the fact that the space will be even more crowded by the EMNLP deadline in 2026 still pull the probability down.

So I'm settling on 25-33%, with a median of 28%. That's slightly above the typical EMNLP acceptance rate of 20-25%, which feels right for a paper with solid execution but moderate novelty—the kind that gets in when everything works well, but the core idea alone isn't strong enough to carry it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db571c75-3548-488e-8dd1-d8ecad57644b",
  "isSidechain": false,
  "requestId": "req_011Cb5QjUHgQoL3k21HANKj6",
  "type": "assistant",
  "uuid": "8d351a75-c602-41fc-89e8-3a81075c377c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q38BwA98iAPeqUizgU9Z1o",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1065,
      "cache_read_input_tokens": 34546,
      "output_tokens": 5796,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1065,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5796,
          "cache_read_input_tokens": 34546,
          "cache_creation_input_tokens": 1065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1065
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

_source line 42 · 2026-05-16T01:53:34.104Z_

Now I have sufficient information from my literature search to perform a thorough, objective evaluation. Let me compose the triage assessment.

---

```
【阶段】: Triage

【Trivial Alternative 检验】:
存在至少两个成本更低的替代方案需要对比：

(1) **Post-hoc probe→rewrite pipeline**: 先正常生成完整长文本，用 Han et al. 的 probes 离线检测每个 claim 的 factuality score，然后对低置信 claims 做 prompt-based 重写加入 hedging 语言。这条路线不需要任何 activation steering 技术，实现成本远低于 RaS，唯一劣势是多 pass。但"single-pass"在实际部署中是否真的是刚需？如果 post-hoc 方法能达到类似的 ECE 改善，RaS 的 single-pass 优势就只是工程便利而非学术贡献。

(2) **Uniform confidence steering（无 probe）**: 直接对整个生成过程施加 Miao & Ungar 的 confidence direction steering（固定强度），不做 claim-level probe 监控。如果 uniform steering 的 ECE 改善与 probe-guided adaptive steering 差距不大，那么 probe-guided 的精细化设计增量价值有限。proposal 中已包含此 ablation（"uniform steering without probe guidance"），说明作者也意识到了这个威胁——但这恰恰说明这是一个真实风险。

**增量价值**: RaS 的真正增量在于 *real-time, probe-adaptive, graded* steering——如果实验能证明 probe-guided 显著优于 uniform steering（not just statistically significant, but meaningfully better），且 single-pass 在质量上优于 post-hoc pipeline（例如 hedging 更自然、claim 边界处理更好），那增量价值成立。但这高度依赖实验结果，在 idea 层面无法确认。

【前提假设检验】:
核心逻辑链中有以下未验证假设：

(1) **Accuracy-confidence orthogonality at 70B + long-form（关键假设）**: Miao & Ungar 的 orthogonality 发现仅在 7-8B QA 设置下验证（cosine < 0.04）。proposal 将其外推到 70B 长文本生成场景，这是一个非平凡的假设。70B 模型的 representation geometry 可能不同；长文本生成的 hidden state dynamics 也不同于 short-form QA。proposal 设计了 pilot experiment 来验证——这是好的实验设计，但也说明这个假设本身是脆弱的。如果 orthogonality breaks（outcome c），整个方法论需要重大调整。

(2) **Offline-trained probes transfer to online streaming**: 离线训练的 factuality probes 基于完整 claim 的 hidden states。在线 generation 时，每 K=8 个 token 的 partial hidden states 是否能提供同样可靠的 factuality 信号？token-level probe accuracy 在 incomplete claims 上可能显著退化。这个假设在整个逻辑链中缺乏理论或实证支撑。

(3) **Mid-sentence steering coherence**: 在句子中间激活 activation steering 假设不会破坏生成连贯性。但 mid-sentence 改变 activation trajectory 可能导致语法不通顺或语义断裂——尤其是在 70B 模型上，steering resistance 更强（proposal 引用了 3.8% ESR rate）。"naturally hedged language" 的质量是一个 open question。

(4) **Confidence direction steering only affects expression, not content**: 基于 orthogonality 假设，steering verbalized confidence direction 不应影响 factual accuracy。但 orthogonality 是 approximate（cosine < 0.04 ≠ 0），在 cumulative steering over many tokens in long-form generation 中，即使微小的非正交分量也可能 accumulate 并影响 content quality。

【3 维度打分】:

1. **Novelty**: 中 — 
   核心贡献是 **组合式创新**：将 Han et al. 的 claim-level factuality probes（读）与 Miao & Ungar 的 confidence direction steering（写）组合为 single-pass framework。两个核心组件均直接借用自 prior work。Sub-sentence EMA monitoring 和 adaptive steering formula 是工程层面的设计贡献，但不构成 conceptual novelty。
   
   关键问题是：**这个组合是否 non-obvious？** Miao & Ungar 论文中明确指出 "extending to open-ended generation would require rethinking how the probe target is constructed" — 即原作者已经指明了这个方向。Han et al. 提供了 claim-level probes for long-form generation。将二者结合是一个 **predictable next step**，而非 surprising insight。与 O'Neill et al.（external observer + binary steering）的差异化也更多是 design choices（self-probing vs. external, graded vs. binary）而非 paradigm shift。
   
   Novelty 的正面：orthogonality-at-70B verification 作为 secondary contribution 有价值；self-probing + single-pass 的设计确实比 O'Neill et al. 更 elegant。但整体而言，剔除 surface differences 后，residual novelty = "apply read-accuracy-steer-confidence at claim level in long-form" ≈ 将已知方法推广到新的 setting。

2. **Significance**: 中 — 
   **问题本身重要**：claim-level calibrated uncertainty in long-form generation 是一个有实际应用价值的未解决问题，用户需要知道长文本输出中哪些部分可靠、哪些需要 caveat。
   
   **但 expected result 不够 surprising**：如果 RaS 达到 25% ECE reduction（primary target），审稿人的反应大概率是 "I would have guessed this works — you combined a good probe with a good steering direction, of course calibration improves."  即使达到 40% stretch goal，也不是 counter-intuitive。真正 surprising 的结果需要是：(a) the approach fails in unexpected ways that reveal something about representation geometry，或 (b) it works far better than component-wise predictions would suggest due to synergistic effects。proposal 没有给出为什么会出现 synergy 的理论论证。
   
   **推广性有限**：需要 per-model offline probe training + direction extraction；只在 standard transformer 上验证（explicitly avoids hybrid architectures like DeltaNet）；25% ECE reduction target 相比 Miao & Ungar response-level 的 70-90% reduction 是 substantial discount。
   
   **正面**：orthogonality scaling result 无论正负都有 mechanistic insight 价值；如果 sub-sentence steering 确实能产生自然的 hedging 语言，这在 deployment 层面有实际影响。

3. **Related Work**: 强 — 
   这是整个 proposal 最强的维度。Related work 覆盖极其详尽（~30 篇近期工作），对每篇相关工作的差异化定位清晰准确。特别是对 O'Neill et al.、CARE、CAST、CLAS、AUSteer 等 concurrent work 的定位明确了 RaS 在三个轴上的区分（self-probing vs. external, graded vs. binary, claim-level vs. response-level）。gap 的论证是充分的：确实没有现有工作在 "claim-level + calibrated + long-form + single-pass + no training" 这个交叉点上。
   
   **但有一个隐忧**：gap 是通过多个约束的 **conjunction** 定义的。审稿人可能质疑："Why do we need all these constraints to hold simultaneously? Is single-pass really necessary? Is no-training-required truly a hard constraint?" 这种 "gap by conjunction" 策略有时不够有说服力。此外，空间极度拥挤（CURE, CAG, CARE, CORAL, CLAS, CAST, O'Neill et al., AUSteer 等都是 2025-2026 的工作），到 ARR August 2026 提交时可能有更多重叠工作出现。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
三维度综合来看：Related Work（强）确保了定位清晰和 gap 论证充分，这是这篇工作的 floor support——不会因为 "missed related work" 或 "unclear positioning" 被拒。但 **Novelty（中）是限制上界的主要因素**：组合式创新、predictable next step、核心组件均借用 prior work，这些会让审稿人写出 "technically sound but limited novelty" 或 "incremental extension of Miao & Ungar to long-form setting"。Significance（中）提供 moderate support 但不足以弥补 novelty 的不足——expected result 如果 positive 不够 surprising，不足以让审稿人 champion 这篇论文。

在 EMNLP main conference（acceptance rate ~22-25%）的语境下，这篇论文处于 **borderline zone**：idea 方向正确、定位清晰，但内核不够突出。强执行 + 好结果可能把它推到 borderline accept，但 idea 本身无法 carry。中位 27% 反映了 "略高于 random submission 的基线概率，但 idea 质量本身不足以显著提升命中率"。

【主要风险】:
1. **"Obvious combination" 质疑**: 审稿人可能认为将 Han et al. probes + Miao & Ungar steering 组合是 straightforward engineering，缺乏 conceptual contribution。论文需要证明组合产生了 emergent benefits（不只是 component-wise 效果叠加），否则会被归类为 "systems paper" 或 "application paper"。
2. **Crowded space + scooping risk**: 2025-2026 年这个方向的工作发表速度极快（CURE 4月, CAG 5月, CLAS 4月, FLAS 5月, PCNET 5月...），到 ARR August 2026 deadline 时，可能已经有其他组完成了类似的 probe→steer for long-form confidence 组合。如果 Miao & Ungar 组（Penn）自己做了 long-form extension，RaS 的 novelty 将大幅缩水。
```

Sources:
- [Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, 2026)](https://arxiv.org/abs/2603.25052)
- [A Single Direction of Truth (O'Neill et al., 2025)](https://arxiv.org/abs/2507.23221)
- [CLAS: Contextual Linear Activation Steering (Hsu et al., 2026)](https://arxiv.org/abs/2604.24693)
- [AUSteer: Fine-Grained Activation Steering (ICLR 2026)](https://arxiv.org/abs/2602.04428)
- [Simple Factuality Probes Detect Hallucinations (Han et al., EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.880/)
- [Calibrating Verbal Uncertainty as a Linear Feature (Ji et al., EMNLP 2025)](https://arxiv.org/abs/2503.14477)
- [How do LLMs Compute Verbal Confidence (Kumaran et al., 2026)](https://arxiv.org/abs/2603.17839)
- [CORAL (Miao, Cho & Ungar, 2026)](https://arxiv.org/abs/2602.06022)
- [Activation Steering in 2026: A Practitioner's Field Guide](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)
- [CARE/ConFix: Fact-Level Calibration (SIGIR 2025)](https://dl.acm.org/doi/pdf/10.1145/3726302.3730195)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d351a75-c602-41fc-89e8-3a81075c377c",
  "isSidechain": false,
  "requestId": "req_011Cb5QjUHgQoL3k21HANKj6",
  "type": "assistant",
  "uuid": "9a52f033-01d8-419c-b482-0070a1850420",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q38BwA98iAPeqUizgU9Z1o",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1065,
      "cache_read_input_tokens": 34546,
      "output_tokens": 5796,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1065,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5796,
          "cache_read_input_tokens": 34546,
          "cache_creation_input_tokens": 1065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1065
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation  **状态**: 待审阅   **级别**:…",
  "leafUuid": "9a52f033-01d8-419c-b482-0070a1850420",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate claim-level confidence calibration proposal",
  "sessionId": "229ceea7-2481-45c0-9011-ca8f5c9ddaac"
}
```

---
