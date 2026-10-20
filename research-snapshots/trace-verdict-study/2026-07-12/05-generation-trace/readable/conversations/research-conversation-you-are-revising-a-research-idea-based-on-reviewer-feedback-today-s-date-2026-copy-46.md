# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-09 (UTC).** ## Original idea { "tit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/03b3a10b-92bf-4e7e-aee3-dad2ca50626d.jsonl`
- **Structured JSON:** [`d7bc7ef92fde89bd5b2c.json`](../../sessions/d7/d7bc7ef92fde89bd5b2c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-09T21:12:32.967Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-09T21:12:32.967Z",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-09 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Genealogical Depth Scoring for Recursive Web Corpus Decontamination\",\n  \"core_problem\": \"Current AI-generated text detectors are binary (human vs. AI), but training corpora increasingly contain 'second-generation' synthetic text: AI outputs from models that were themselves trained on AI-generated data. This generational depth is unmeasured and unaddressed by any existing detector. Strong Model Collapse (ICLR 2025) establishes that even non-vanishing fractions (~1%) of synthetic data trigger performance collapse, yet the paper treats all synthetic data equivalently — making no distinction between Gen1 text (one model generation removed from human data) and Gen2+ text (recursively compounded). The depth-dependent contribution to collapse severity is entirely uncharacterized, and no current method can assign a generational depth score to a raw training document. Critically, recent work (arXiv:2605.01647, May 2026) demonstrates a 'Wall of Separation' where AI-AI divergence in character-distribution space is significantly smaller than human-AI divergence — making within-model generational discrimination (Gen1 vs. Gen2 from the same fine-tuned model) a harder detection problem than binary human/AI classification and motivating our use of embedding-space features that target cumulative semantic drift orthogonal to character-level surface signals.\",\n  \"opportunity\": \"By April 2025, 74.2% of newly created web pages contain some AI-generated text — of which 2.5% are fully AI-generated and 71.7% are human-AI blends, where human content has been AI-revised or AI-assisted (Ahrefs, 900K pages, April 2025). These blended documents may occupy an intermediate 'Gen0.5' depth position between Gen0 and Gen1 that depth scoring can address more precisely than binary detection, and they represent the dominant contamination modality at web scale. Complete decontamination is operationally infeasible — there is not enough uncontaminated human text to replace even the fully AI-generated fraction — shifting the practical research question from 'remove all synthetic data' (impossible at web scale) to 'which synthetic documents to prioritize for removal given a fixed filtering budget.' Depth-stratified decontamination addresses this directly: if Gen2+ documents are disproportionately harmful relative to Gen1 documents, preferential removal of deeper-generation text maximizes collapse mitigation per unit of filtering effort. This claim is explicitly scoped to *severity reduction per filtering budget*, not collapse prevention, and is tested in controlled fixed-total-size depth-composition conditions that isolate the effect of contamination depth from dataset volume — making the causal evidence for the governance claim empirically clean. Strong Model Collapse (ICLR 2025) provides the urgency but not the answer — it shows synthetic data is harmful at any non-vanishing fraction but gives no guidance on whether all synthetic data is equally harmful. Crucially, the paper does not distinguish Gen1 from Gen2 synthetic data at all, leaving the depth-dependent harm gradient completely unmeasured. A depth classifier that enables tiered decontamination — or, if depth discrimination fails, definitively establishes that binary filtering suffices — constitutes a concrete empirical contribution with direct governance impact, aligned with EMNLP 2026's special theme 'New Missions for NLP Research,' which explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance.'\",\n  \"landscape\": \"Model collapse from recursive synthetic training is established (Shumailov et al., Nature 2024; Strong Model Collapse, ICLR 2025) and the limiting theory predicts collapse at any non-vanishing synthetic fraction. Mitigation via real-data accumulation (arXiv:2404.01413) or verifier-guided retraining (arXiv:2510.16657) is active. arXiv:2602.10531 ('From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources', February 2026) analyzes the statistical dynamics of iterative training on data contaminated with synthetic samples using a mixture-model framework, showing that improvement over collapsed models is possible when sufficient fresh real data is present; it does not assign generational depth labels to documents or propose a depth-stratified filtering method. Training-side collapse prevention via Truncated Cross-Entropy loss (ForTIFAI, arXiv:2509.08972) selectively ignores high-confidence tokens during training to filter synthetic artifacts — a complementary but orthogonal approach to our upstream corpus-level depth detection: ForTIFAI does not classify documents by generational depth and does not operate pre-training. The closest upstream related work, 'Machine-generated text detection prevents language model collapse' (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025), directly bridges AI-text detection and collapse prevention: it trains encoder-only binary classifiers (evaluating RoBERTa, DeBERTa-v3, and ModernBERT) to distinguish human from AI-generated text, then applies importance resampling — weighting each training document by (1-q(x))^b where q(x) is the classifier's AI-probability score — to up-weight likely human content during recursive training. Experiments across GPT-2 and SmolLM2 (124M–1.7B parameters) demonstrate that binary-classifier-guided resampling prevents collapse and even improves over training on purely human data. Critically, arXiv:2502.15654 treats all AI-generated text as equivalent regardless of generational provenance: importance weights depend only on a single binary human/AI probability, with no distinction between Gen1 text (one fine-tuning cycle removed from human data) and Gen2+ text (recursively compounded). Our work directly addresses this gap: if depth-stratified resampling weights — proportional to estimated generational distance from Gen0 — yield greater collapse-severity reduction per resampled document than flat binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over arXiv:2502.15654's strategy under budget-constrained filtering. The dual null-hypothesis design explicitly covers the scenario where depth discrimination fails (AUC < 0.65), in which case our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant and binary resampling is sufficient — a governance finding with direct practical value. A mathematical framework for how recursive publication compresses text through drift and selection is developed in arXiv:2604.08554 but does not propose a depth classifier. The framework is derived for variable-order n-gram agents and does not address transformer fine-tuning; extension to neural models is an open theoretical question that our experiments probe empirically. AI-generated text detection (arXiv:2303.11156, arXiv:2509.18880) addresses binary classification and reaches AUC ~0.85-0.90 for Gen1 text, uniformly treating all AI-generated text as equivalent regardless of generational provenance. Embedding-based representations show intrinsic separability between AI-generated and human text in compressed embedding spaces (arXiv:2408.10437), motivating our use of embedding-space distance features alongside surface-level signals. 'Understanding Transformers via N-gram Statistics' (arXiv:2407.12034, NeurIPS 2024) provides empirical motivation for applying n-gram-derived theoretical predictions to transformer fine-tuning: transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions across TinyStories and Wikipedia, suggesting transformer distributional behavior closely approximates n-gram statistics at the local prediction level — supporting our hypothesis that the monotonic drift prediction of arXiv:2604.08554 (derived for n-gram agents) extends to transformer fine-tuning at the distributional level, with our experiments constituting a direct empirical test of this generalization. 'Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection' (arXiv:2605.01647, May 2026) introduces the Letter Distribution Score (LD-Score) and establishes a 'Wall of Separation' where human-AI divergence significantly exceeds AI-AI divergence in character-distribution space — with the direct implication that within-model generational divergence (Gen1 vs. Gen2 from the same fine-tuned 0.6B model) is smaller still than cross-model AI-AI divergence. This finding validates our architectural choice to prioritize embedding-space features over character-distribution proxies: our mean cosine distance from Gen0 centroid and within-document embedding variance operate in a representation space where cumulative semantic drift — predicted to accumulate monotonically by arXiv:2604.08554's recursive drift-selection framework — may remain detectable even when surface and character-level signals converge. The pre-specified AUC threshold (0.65) and dual null-hypothesis pivot design explicitly account for the scenario where depth discrimination fails at the document level despite embedding-space features. No paper in the contamination detection surveys (arXiv:2502.14425, arXiv:2406.04244) addresses generation depth as a variable. The closest concurrent work — 'Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models' (arXiv:2511.17602, Nov 2025) — asks whether synthetic data overlaps with evaluation benchmarks, not how many generative cycles deep a document is; generational ancestry is orthogonal to benchmark overlap. 'Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training?' (TrainProVe, CVPR 2025, arXiv:2503.09122) achieves >99% accuracy verifying which text-to-image model generated a given image, using model access and generalization error bounds — differentiation is sharp: TrainProVe operates in the image domain and requires model weights access, while our method operates on raw text documents with no model access, enabling upstream corpus-level pre-filtering. Both address data governance but via entirely complementary mechanisms. 'A Closer Look at Model Collapse' (arXiv:2509.16499, NeurIPS 2025 Spotlight) identifies a generalization-to-memorization transition but studies diffusion models and does not distinguish depth levels in training data.\",\n  \"approach\": \"We build a controlled genealogical corpus by running a 2-step recursive train-generate loop with Qwen3-0.6B (the smallest Qwen3 model, chosen to minimize sequential compute cost while still exhibiting measurable distributional drift per generation), producing text with verified depth labels Gen0 (human, sourced from FineWeb-Edu and C4), Gen1, and Gen2, yielding ~200K labeled documents per depth level across diverse domains. All generated documents are hard-capped at 512 tokens maximum length: this cap is enforced at generation time via the `max_new_tokens=512` parameter, making generation time deterministic and reviewable. At 200K documents × 512 tokens = 102M tokens per generational step, batched A100 inference at 3,000–5,000 tok/s for Qwen3-0.6B yields approximately 6–9 GPU hours per step — consistent with the timeline estimate below. The 512-token cap is scientifically defensible for depth discrimination: surface-level signals (surprisal burstiness, lexical diversity, n-gram entropy) and embedding-space signals (mean cosine distance from Gen0 centroid, within-document window embedding variance) are fully computable over 512-token documents, and ordinal regression classifiers trained on short-document depth signals are directly comparable to the binary detectors in arXiv:2502.15654, which also operate on variable-length web documents.\\n\\nWe disable Qwen3-0.6B thinking mode during all generative steps via the hard switch `enable_thinking=False` in `tokenizer.apply_chat_template`, rather than the soft `/no_think` instruction tag — because GitHub discussion QwenLM/Qwen3 #1329 documents that the 0.6B model lacks sufficient instruction-following capacity to reliably honor `/no_think` when placed in the system prompt, and silent failure would inject `&lt;think>…&lt;/think>` reasoning traces into Gen1/Gen2 documents that are absent from Gen0 human text, making depth levels trivially separable by token-level artifacts rather than genuine semantic drift and invalidating the AUC signal. The `enable_thinking=False` hard switch operates at the tokenizer template level and does not depend on the model's instruction-following capacity. As a final post-hoc verification, every generated document is scanned for `&lt;think>` tokens and discarded if any are found, before corpus inclusion.\\n\\nLimiting to Gen0/Gen1/Gen2 compresses the sequential corpus construction bottleneck to approximately 2 wallclock days: Qwen3-0.6B fine-tuning on a 200K-document sample runs in ~4-6 GPU hours on A100, and generation of 200K new 512-token documents runs in ~6-9 GPU hours, for ~12-15 GPU hours per generational step. The hard sequential dependency spans only 2 steps.\\n\\nWe train a DeBERTa-v3-large ordinal regression classifier jointly on raw text and depth-diagnostic features spanning two categories: (a) surface-level signals — per-token surprisal variance (burstiness), lexical diversity decay (MTLD and type-token ratio), and n-gram entropy compression ratio; and (b) embedding-space signals — (i) mean cosine distance of within-document window embeddings from the pre-computed Gen0 centroid (capturing average depth of embedding drift from human text), and (ii) variance of per-window cosine distances from the Gen0 centroid within the document (capturing within-document heterogeneity of embedding drift). Both embedding features are computed from non-overlapping 128-token window embeddings produced by sentence-transformers/all-MiniLM-L6-v2; feature (i) measures central tendency and feature (ii) measures distributional spread — distinct geometric properties: a Gen2 document may exhibit both higher mean distance from Gen0 and more heterogeneous window-level drift than a Gen1 document, as cumulative generational compression produces uneven semantic displacement within a document. We integrate these five scalar depth-diagnostic features by concatenating them to the DeBERTa-v3-large CLS token representation (1024-dim), then training an ordinal regression head over this joint 1029-dim representation; the Gen0 embedding centroid is precomputed offline from a held-out Gen0 reference set of 10K documents using sentence-transformers/all-MiniLM-L6-v2 and is not updated during classifier training.\\n\\nEmbedding-space features are specifically motivated by the 'Wall of Separation' established in arXiv:2605.01647 (May 2026): AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence (Gen1→Gen2 from the same fine-tuned 0.6B model) is smaller still. Surface-level and character-distribution signals are therefore unlikely to reliably discriminate depth levels in this setting; our mean cosine distance from Gen0 centroid and within-document embedding variance instead target cumulative semantic drift that arXiv:2604.08554's recursive drift-selection framework predicts to accumulate monotonically across generations even when character distributions plateau — providing detection signal orthogonal to surface proxies. The argument is: our embedding-space features target cumulative semantic drift that persists even when surface divergence converges, consistent with the monotonic drift predicted by arXiv:2604.08554 — with the explicit caveat that arXiv:2604.08554 derives this prediction for variable-order n-gram agents, not transformer fine-tuning. We hypothesize the generalization holds because transformer next-token distributions closely approximate n-gram statistics at the local prediction level (arXiv:2407.12034, NeurIPS 2024, reports 68–79% agreement between transformer predictions and n-gram rulesets across two corpora), suggesting transformer fine-tuning implicitly performs distributional compression analogous to n-gram compression, for which cumulative drift is expected to accumulate monotonically. Our classifier and collapse experiments directly test whether this hypothesized generalization from n-gram theory to transformer practice holds empirically.\\n\\nCentral technical risk and dual null-hypothesis design: We pre-specify two complementary pre-registered outcome scenarios to ensure a definitive, interpretable empirical finding under all classifier and collapse experiment outcomes. (Primary null) If the ordinal classifier falls below AUC 0.65 on Gen1/Gen2 discrimination, the finding is publishable: depth beyond Gen1 is linguistically indistinguishable at the document level using current text-level and embedding-level methods, implying binary filtering suffices — consistent with the implicit assumption of arXiv:2502.15654. In this case, the collapse validation experiments automatically pivot to directly comparing binary (Gen0-only) filtering against depth-stratified filtering at fixed corpus size. (Secondary null) If the classifier achieves AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between conditions (b) (100K Gen0 + 100K Gen1) and (c) (67K Gen0 + 67K Gen1 + 66K Gen2) at fixed total corpus size (paired t-test, α = 0.05, across 3 random seeds), we report this as a distinct secondary null outcome: depth detection is feasible but equal-fraction Gen2 contamination causes no additional collapse-severity beyond equal-fraction Gen1 contamination at GPT-2 scale — the marginal harm-per-generation curve is flat at this model size, binary filtering is sufficient for practical governance at small scales, and preferential Gen2 removal yields no measurable advantage at this scale. This finding has direct governance implications while leaving open whether depth stratification provides additional value at larger model scales, explicitly reserved as future work. All four logical combinations of (AUC pass/fail) × (collapse severity parity/non-parity) produce pre-specified, interpretable empirical contributions with distinct governance implications.\\n\\nThe trained classifier is applied zero-shot to real FineWeb and C4 slices to estimate depth-distribution statistics of existing pretraining corpora. Collapse validation uses a GPT-2-scale LM fine-tuned on three fixed-total-size depth-composition conditions (200K training documents each), following the controlled-composition standard of Strong Model Collapse (ICLR 2025): (a) Gen0-only: 200K Gen0; (b) Gen0+Gen1: 100K Gen0 + 100K Gen1; (c) Gen0+Gen1+Gen2: 67K Gen0 + 67K Gen1 + 66K Gen2. These corpora are constructed by subsampling from the already-generated 200K-document pools at each depth level, requiring no additional generation compute. Fixing total corpus size at 200K across all three conditions isolates the causal effect of depth composition from dataset volume: any observed collapse severity difference between conditions reflects contamination depth, not training set size — making the central governance claim ('Gen2 contamination is more harmful per document than Gen1 at equal contamination rate') empirically defensible. Collapse severity is tracked via held-out human-text perplexity and output tail entropy across multiple recursive training generations, explicitly scoped to measuring *severity as a function of depth composition at fixed scale* rather than collapse prevention — consistent with Strong Model Collapse's any-fraction harm finding. GenDepth-Bench is scoped to 2 model families: Qwen3-0.6B (primary) and Llama-3.2-1B (secondary, run through the same recursive loop to test cross-model generalizability of depth signals, explicitly optional — executed only if compute budget permits; see resource estimate). Coverage of 5+ model families is explicitly reserved as future work.\\n\\n16-Day Critical Path (EMNLP 2026 ARR deadline May 25, 2026; today May 9, 2026):\\n— Days 1-2: Environment setup; sample 200K Gen0 docs from FineWeb-Edu/C4 (truncated to 512 tokens); prepare evaluation suite and draft intro/related-work sections.\\n— Days 2-3 (sequential bottleneck step 1): Fine-tune Qwen3-0.6B on Gen0 (~4-6h GPU); generate 200K Gen1 documents at max 512 tokens each (~6-9h GPU; 200K × 512 tokens = 102M tokens ÷ 3,000–5,000 tok/s ≈ 6–9h) with `enable_thinking=False` hard switch and post-hoc `&lt;think>` token scan.\\n— Days 3-4 (sequential bottleneck step 2): Fine-tune Qwen3-0.6B-v2 on Gen1 (~4-6h GPU); generate 200K Gen2 documents at max 512 tokens each (~6-9h GPU) with same thinking-mode controls.\\n— Days 3-8 (PARALLEL TRACK A): DeBERTa-v3-large ordinal training begins with Gen0+Gen1 data at Day 3; adds Gen2 data when available at Day 5; ablations over surface vs. embedding feature subsets.\\n— Days 5-10 (PARALLEL TRACK B): GPT-2-scale collapse experiments begin at Day 5 with fixed-size conditions (a) Gen0-only: 200K Gen0 and (b) Gen0+Gen1: 100K Gen0+100K Gen1 (subsampled from existing pools); add condition (c) Gen0+Gen1+Gen2: 67K each at Day 6 when Gen2 corpus is available. Llama-3.2-1B recursive corpus generation runs in parallel if compute budget is below 160h H100-equivalent at Day 5.\\n— Days 7-9: Full classifier evaluation; if Gen1/Gen2 AUC < 0.65, activate primary null-hypothesis binary filtering comparison experiments; if AUC ≥ 0.65 but collapse severity parity detected between conditions (b) and (c), record secondary null outcome and report governance implications.\\n— Days 9-10: Zero-shot depth scoring on real FineWeb/C4 slices.\\n— Days 10-12: Feature importance ablations; cross-model generalizability check on Llama-3.2-1B-generated corpus (if optional Llama recursive corpus was generated).\\n— Days 12-16: Analysis, writing, revision, and submission.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~210h A100 (40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B, each step generating 200K documents at 512 tokens max = 102M tokens ÷ ~3,500 tok/s average ≈ ~8h per step, ×2 steps = ~16h generation + ~24h fine-tuning over 2 steps + 50h DeBERTa-v3-large fine-tuning and ablations + 120h GPT-2-scale collapse validation experiments across 3 fixed-size depth-composition conditions)\",\n      \"gpu_utilization\": \"High idle rate (~40-60%): GPU waits while researcher designs experiment configs, interprets collapse curves, debugs depth signal quality, and writes between each stage over several months\",\n      \"timeline\": \"4-6 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$370 at $1.75/h blended A100 average (RunPod ~$1.49/h, Lambda ~$2.06/h); approximately 70 H100-equivalent hours\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~320h A100 (agent handles training loop queuing and ablation scheduling; human approves depth-feature selection, collapse experiment design, AUC threshold decision for null-hypothesis activation, and Llama-3.2-1B second-family validation)\",\n      \"gpu_utilization\": \"Moderate idle rate (~15-25%): agent queues overnight runs and fills GPU gaps between sequential generational steps; handles parallel DeBERTa and collapse experiment scheduling\",\n      \"timeline\": \"6-10 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$60-120 (~600-800 agent turns at $0.08-0.15/turn for experiment design, result interpretation, and iteration guidance)\",\n      \"estimated_gpu_cost\": \"~$560 at $1.75/h average A100; approximately 107 H100-equivalent hours\",\n      \"risk_note\": \"Key bottleneck: 2-step sequential corpus construction (train on GenN → generate GenN+1 at 512 tokens max → train again) cannot be parallelized; each step adds ~1 wallclock day with Qwen3-0.6B. The 512-token document cap makes generation time deterministic: 200K × 512 tokens = 102M tokens ÷ 3,000–5,000 tok/s ≈ 6–9h per step, matching the timeline estimate and eliminating schedule uncertainty from variable document lengths. Corpus construction for collapse experiments uses fixed-total-size subsampling (200K per condition) from the already-generated per-depth pools — no additional generation compute required. Pre-specified dual null-hypothesis design (primary: AUC < 0.65; secondary: AUC ≥ 0.65 but collapse severity parity between fixed-size conditions (b) and (c)) means the agent has clear decision rules without requiring researcher judgment to pivot, covering all four logical outcome combinations.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~490h A100 / ~163h H100-equivalent hours (mandatory, within ≤200h hard constraint): 40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B (200K documents × 512 tokens max per step = 102M tokens; at 3,000–5,000 tok/s ≈ 6–9h generation per step, ×2 steps; plus ~12h fine-tuning per step = ~40h total) + 120h DeBERTa-v3-large fine-tuning and ablations with 2x hyperparameter search across depth-feature combinations (surface-only, embedding-only, combined) + 240h GPT-2-scale collapse validation experiments across 3 fixed-total-size depth-composition conditions (Qwen3-0.6B family) with 3 collapse metrics + 90h auxiliary ablations (feature importance, zero-shot FineWeb/C4 scoring, null-hypothesis binary filtering comparison if AUC threshold triggered). Llama-3.2-1B recursive corpus generation and collapse experiments (~60-90h A100 / ~20-30h H100-equivalent) are explicitly optional from the start: executed only if compute budget remains below 160h H100-equivalent at Day 10; otherwise deprioritized to zero-shot depth scoring only, maintaining a genuine 40h safety buffer against the 200h hard ceiling.\",\n      \"gpu_utilization\": \"Near-zero idle (<5%): agent queues hyperparameter sweeps and ablations 24/7, filling GPU cycles between sequential generational construction steps with parallel auxiliary experiments\",\n      \"timeline\": \"13-16 days with 4-6 concurrent A100s\",\n      \"team\": \"0 (4-6h one-time setup: genealogical corpus schema with 512-token document cap, experiment grid, AUC threshold 0.65 for primary null-hypothesis activation, paired t-test criterion for secondary null-hypothesis activation between fixed-size conditions (b) and (c), stopping conditions)\",\n      \"claude_api_cost\": \"$250-400 (~2500-3000 agent turns for experiment orchestration, result analysis, and adaptive exploration)\",\n      \"estimated_gpu_cost\": \"~$856 at $1.75/h average A100 (mandatory only); ~$960 including optional Llama-3.2-1B corpus if budget permits\",\n      \"speed_bottleneck\": \"2-step sequential corpus construction is the hard wallclock floor; the 512-token document cap makes per-step generation time deterministic at ~6-9h (102M tokens ÷ 3,000–5,000 tok/s), eliminating schedule uncertainty; GPU count limits simultaneous ablation breadth during non-sequential phases\",\n      \"risk_note\": \"Corpus construction for collapse experiments uses fixed-total-size subsampling (200K per condition from already-generated per-depth pools) — no additional generation compute. Depth signal may be weak between Gen1 and Gen2 from the same small model — a risk compounded by the 'Wall of Separation' finding (arXiv:2605.01647): AI-AI surface divergence is substantially smaller than human-AI divergence, making within-model generational discrimination harder still. Pre-specified dual null-hypothesis design covers all outcomes: primary null (AUC < 0.65) redirects to binary filtering comparison at fixed corpus size; secondary null (AUC ≥ 0.65 but collapse severity parity between fixed-size conditions (b) and (c)) reports depth detection as feasible but equal-fraction Gen2 contamination as causing no incremental governance harm beyond Gen1 at GPT-2 scale. Embedding-space features (mean cosine distance from Gen0 centroid and within-document embedding variance over 128-token windows) partially mitigate the primary null risk by targeting cumulative semantic drift invisible at the surface level. Budget contingency: Llama-3.2-1B recursive corpus generation is explicitly optional from the start; if compute approaches 160h H100-equivalent during execution, Llama-3.2-1B recursive corpus is deprioritized to zero-shot depth scoring only (no new collapse experiments), saving ~60-90h A100 (~20-30h H100-equivalent) and maintaining a genuine 40h buffer against the 200h hard ceiling.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; special theme 'New Missions for NLP Research' explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance' — near-perfect topical alignment; conference October 24-29, Budapest)\",\n    \"NAACL 2027 (ARR cycle deadline TBD, expected ~late 2026; safe backup with more time for thorough collapse validation experiments and additional model families)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"AI models collapse when trained on recursively generated data (Nature 2024)\",\n    \"Strong Model Collapse (ICLR 2025) — establishes collapse at any non-vanishing synthetic fraction (~1% example); holds total corpus size fixed while varying synthetic fraction (the controlled design our collapse experiments follow); does not distinguish Gen1 from Gen2 synthetic data; this gap is what we fill\",\n    \"Machine-generated text detection prevents language model collapse (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025) — closest upstream prior work: trains binary encoder-only classifiers (evaluating RoBERTa, DeBERTa-v3, ModernBERT) with importance resampling — weights ∝ (1-q(x))^b — to prevent collapse at GPT-2/SmolLM2 scale (124M–1.7B parameters); treats all AI-generated text equivalently without generational depth distinction; our work directly extends this: if depth-stratified resampling weights yield greater collapse-severity reduction per decontamination unit than binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over binary resampling under budget constraints; if not (AUC < 0.65 or collapse severity parity between fixed-size conditions (b) and (c)), our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant\",\n    \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources (arXiv:2602.10531, February 2026) — analyzes the statistical dynamics of iterative training on contaminated data using a mixture-model framework, showing that improvement over collapsed models is possible when sufficient fresh real data is present; does not assign generational depth labels to documents or propose a depth-stratified filtering method\",\n    \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (arXiv:2404.01413)\",\n    \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence (arXiv:2510.16657)\",\n    \"ForTIFAI: Fending Off Recursive Training Induced Failure for AI Models (arXiv:2509.08972) — training-side collapse prevention via Truncated Cross-Entropy loss; orthogonal to our upstream corpus-level depth detection; does not classify documents by generational depth\",\n    \"Drift and Selection in LLM Text Ecosystems (arXiv:2604.08554) — mathematical framework for how recursive publication compresses text through drift and selection; derived for variable-order n-gram agents (not transformer fine-tuning); does not propose a depth classifier or detection method; motivates our prediction that embedding-space drift accumulates monotonically across generations even when surface distributions plateau, under the hypothesis that transformer fine-tuning implicitly performs distributional compression analogous to n-gram compression — a generalization our experiments directly test\",\n    \"Understanding Transformers via N-gram Statistics (arXiv:2407.12034, NeurIPS 2024) — transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions across TinyStories and Wikipedia; provides empirical grounding for our hypothesis that the monotonic drift prediction of arXiv:2604.08554 (derived for n-gram agents) extends to transformer fine-tuning at the distributional level\",\n    \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection (arXiv:2605.01647, May 2026) — establishes 'Wall of Separation' where human-AI divergence significantly exceeds AI-AI divergence in character-distribution space; within-model generational gap (Gen1→Gen2 from same fine-tuned model) is smaller still; directly threatens surface-level discriminability; our counter-argument: embedding-space features (mean cosine distance from Gen0 centroid and within-document window embedding variance, computed over non-overlapping 128-token windows via sentence-transformers/all-MiniLM-L6-v2) target cumulative semantic drift orthogonal to character-distribution signals; the pre-specified dual null-hypothesis design accounts for the possibility that depth discrimination fails despite embedding-space features\",\n    \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective (NeurIPS 2025 Spotlight)\",\n    \"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (ACL 2024)\",\n    \"Can AI-Generated Text be Reliably Detected? (arXiv:2303.11156)\",\n    \"Diversity Boosts AI-Generated Text Detection (arXiv:2509.18880)\",\n    \"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models (arXiv:2511.17602) — asks whether synthetic data overlaps with evaluation benchmarks; generational ancestry is orthogonal to benchmark overlap\",\n    \"Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training? (TrainProVe, CVPR 2025, arXiv:2503.09122) — achieves >99% accuracy in image domain using model access and generalization error bounds; differentiation: our method operates on raw text with no model access, enabling upstream corpus-level pre-filtering; different modality and mechanism address the same governance goal\",\n    \"Understanding Generative AI Content with Embedding Models (arXiv:2408.10437) — demonstrates intrinsic separability of AI-generated and human text in compressed embedding space; motivates our use of embedding-space cosine distance and within-document variance features for depth discrimination beyond surface-level signals\",\n    \"Benchmark Data Contamination of Large Language Models: A Survey (arXiv:2406.04244)\",\n    \"A Survey on Data Contamination for Large Language Models (arXiv:2502.14425)\"\n  ],\n  \"description\": \"As web corpora become saturated with AI-generated content (74.2% of new web pages contain some AI text by April 2025, of which 2.5% are fully AI-generated and 71.7% are human-AI blends; Ahrefs, 900K pages), complete decontamination is operationally infeasible, shifting the question to: which synthetic documents cause the most harm and should be removed first? We propose Genealogical Depth Scoring, a method extending binary AI-text detection to ordinal depth classification (Gen0=human, Gen1, Gen2), trained on a controlled corpus produced by 2-step recursive train-generate loops using Qwen3-0.6B with thinking mode disabled via the hard switch `enable_thinking=False` in `tokenizer.apply_chat_template` — rather than the soft `/no_think` instruction tag, which silently fails for the 0.6B model when placed in the system prompt (GitHub QwenLM/Qwen3 discussion #1329) and would introduce `&lt;think>…&lt;/think>` artifacts that make depth levels trivially separable by token-level signals rather than genuine semantic drift — with post-hoc discard of any documents containing `&lt;think>` tokens before corpus inclusion. All generated documents are hard-capped at 512 tokens via `max_new_tokens=512`, yielding 200K × 512 tokens = 102M tokens per generational step; at 3,000–5,000 tok/s for Qwen3-0.6B on A100 this takes approximately 6–9 GPU hours per step, making the generation timeline deterministic and anchored to a verifiable arithmetic bound. The classifier combines DeBERTa-v3-large fine-tuning with two classes of depth-diagnostic features: surface-level signals (surprisal burstiness, lexical diversity decay, n-gram entropy compression ratio) and embedding-space signals — (i) mean cosine distance of within-document window embeddings from the Gen0 centroid, and (ii) variance of per-window cosine distances from the Gen0 centroid within the document, both computed over non-overlapping 128-token windows via sentence-transformers/all-MiniLM-L6-v2. Feature (i) captures average drift from human text in embedding space; feature (ii) captures within-document heterogeneity of that drift — distinct geometric properties (central tendency vs. distributional spread) that together characterize the document's depth signature. These five scalar features are concatenated to the DeBERTa-v3-large CLS token representation (1024-dim) and passed to an ordinal regression head trained over the joint 1029-dim representation; the Gen0 centroid is precomputed offline and not updated during training. The embedding-space features directly address the 'Wall of Separation' documented in arXiv:2605.01647 (May 2026) — AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence is smaller still — by targeting cumulative semantic drift that arXiv:2604.08554 predicts to accumulate monotonically across recursive generations even when surface statistics plateau. Because arXiv:2604.08554 derives this prediction for variable-order n-gram agents rather than transformer fine-tuning, we ground the generalization in arXiv:2407.12034 (NeurIPS 2024), which shows transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions, and treat our classifier and collapse experiments as a direct empirical test of whether this theoretical extension holds. We pre-specify a dual null-hypothesis design: (primary null) if Gen1/Gen2 AUC < 0.65, depth is linguistically indistinguishable and binary filtering suffices; (secondary null) if AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between fixed-size conditions (b) (100K Gen0 + 100K Gen1) and (c) (67K Gen0 + 67K Gen1 + 66K Gen2), equal-fraction Gen2 contamination causes no additional collapse-severity beyond equal-fraction Gen1 contamination at GPT-2 scale — depth detection is feasible but depth-stratified filtering provides no incremental governance benefit at small model scale. All four logical outcomes produce pre-specified, interpretable empirical contributions. Collapse validation compares three fixed-total-size depth-composition conditions (200K documents each: (a) Gen0-only; (b) 100K Gen0+100K Gen1; (c) 67K Gen0+67K Gen1+66K Gen2), constructed by subsampling from the already-generated 200K-document pools at each depth level — no additional generation compute. Fixing total corpus size across all conditions isolates the causal effect of depth composition from dataset volume, making the central governance claim ('Gen2 contamination is more harmful per document than Gen1 at equal contamination rate, supporting preferential Gen2 removal per filtering unit') empirically defensible. Results are framed as *collapse severity as a function of contamination depth composition at fixed scale*, directly informing the real-world budget-constrained decontamination problem. TrainProVe (CVPR 2025) addresses related governance goals via model access in the image domain; ForTIFAI (arXiv:2509.08972) prevents collapse at training time via modified loss; arXiv:2502.15654 (Feb 2025) prevents collapse via binary detection with importance resampling but treats all AI text equivalently without generational depth distinction; arXiv:2602.10531 (Feb 2026) analyzes collapse dynamics statistically via mixture models but does not classify text by generational depth — our work is the first to assign generational depth scores to raw text corpus documents upstream of training, and directly tests whether depth-stratified resampling yields greater collapse-severity reduction per filtering unit than binary resampling. We release GenDepth-Bench covering 2 model families (Qwen3-0.6B primary; Llama-3.2-1B secondary, optional pending compute budget), with 5+ family coverage as explicit future work. Targets EMNLP 2026's special theme on synthetic data feedback loops and data governance.\",\n  \"project_name\": \"gen_depth_decontam\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 8)\nIssues: [\"REPLICABILITY GAP — Ordinal regression head type unspecified: The approach specifies concatenating 5 scalar features to the DeBERTa-v3-large CLS token (1029-dim joint representation) and training an 'ordinal regression head,' but does not specify which ordinal regression method. For 3 ordered classes (Gen0, Gen1, Gen2), common implementations differ in boundary-structure assumptions: (a) CORAL-loss based with 2 auxiliary binary classifiers (arXiv:1901.07884; arXiv:2111.08851), (b) proportional odds logistic regression with 2 threshold parameters, or (c) 3-class softmax with ordinal label weighting. Reviewers checking replicability will notice this gap. Fix: add one sentence specifying the implementation, e.g., 'We use CORAL-loss based ordinal regression (arXiv:2111.08851) decomposing the 3-class problem into 2 binary classifiers with shared feature weights and independently trained bias terms over the 1029-dim joint representation.' This closes the replicability gap without any experimental change.\", \"STATISTICAL POWER ACKNOWLEDGMENT MISSING — Secondary null hypothesis is underpowered: The pre-specified secondary null criterion (paired t-test, α=0.05, N=3 seeds, df=2) has a critical t-value of 4.303, providing power < 20% for Cohen's d < 2.0. If Gen2 contamination causes a real but moderate increase in collapse severity (e.g., 10–20% worse perplexity), 3 seeds cannot detect it, and non-rejection would falsely validate the 'depth stratification provides no incremental benefit' conclusion. This is the weakest statistical link in the pre-registered design and a reviewer will attack it. Fix: add one sentence explicitly acknowledging the limitation, e.g., 'We note that with 3 seeds the secondary null test is powered primarily to detect large effect sizes; non-rejection at this scale does not rule out moderate depth effects detectable with more seeds, which we reserve as future work at larger compute budgets.' This converts a reviewer attack surface into a transparent acknowledged limitation.\", \"MISSING CITATION — arXiv:2509.04796 'Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training' (September 2025): This paper demonstrates a three-stage recursive training phenomenon where surface fluency persists while factual accuracy collapses — providing complementary empirical support for the claim that deeper-generation text causes qualitatively distinct harm that perplexity alone may understate. An area chair familiar with the model collapse literature (likely at EMNLP 2026 given the special theme) may flag its absence. One citation line in the landscape section suffices: 'arXiv:2509.04796 shows that factual accuracy collapses faster than perplexity in recursive synthetic training — motivating depth-stratified decontamination as a mechanism to preferentially remove documents at generational depths where factual quality is most degraded; it does not classify documents by generational depth or propose a depth-stratified filtering method.'\"]\nFeedback: All seven Round 7 issues are resolved: the 512-token document cap is explicitly stated with anchored arithmetic (200K × 512 tokens ÷ 3,000–5,000 tok/s = 6–9h per step), arXiv:2602.10531 is cited and differentiated, and all prior round issues remain correctly addressed. Three targeted fixes will complete this proposal: (1) Specify the ordinal regression head implementation — add one sentence naming the method (recommend CORAL-loss based, citing arXiv:2111.08851, since it is rank-consistent and well-tested for 3-class ordinal problems with PyTorch implementations readily available). (2) Add one sentence acknowledging the 3-seed secondary null test is powered for large effect sizes only, explicitly reserving higher-powered validation as future work. (3) Add arXiv:2509.04796 to the landscape with a one-line differentiation. All three fixes require under 30 minutes of writing and zero new experiments. Independent novelty verification confirms no competing work on generational depth scoring for corpus decontamination exists through May 2026.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 8 轮修订，近 3 轮的平均分从 3.8 到 3.8，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-09T21:12:32.972Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-09T21:12:32.972Z",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-09T21:12:33.020Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-09 (UTC).**

## Original idea
{
  "title": "Genealogical Depth Scoring for Recursive Web Corpus Decontamination",
  "core_problem": "Current AI-generated text detectors are binary (human vs. AI), but training corpora increasingly contain 'second-generation' synthetic text: AI outputs from models that were themselves trained on AI-generated data. This generational depth is unmeasured and unaddressed by any existing detector. Strong Model Collapse (ICLR 2025) establishes that even non-vanishing fractions (~1%) of synthetic data trigger performance collapse, yet the paper treats all synthetic data equivalently — making no distinction between Gen1 text (one model generation removed from human data) and Gen2+ text (recursively compounded). The depth-dependent contribution to collapse severity is entirely uncharacterized, and no current method can assign a generational depth score to a raw training document. Critically, recent work (arXiv:2605.01647, May 2026) demonstrates a 'Wall of Separation' where AI-AI divergence in character-distribution space is significantly smaller than human-AI divergence — making within-model generational discrimination (Gen1 vs. Gen2 from the same fine-tuned model) a harder detection problem than binary human/AI classification and motivating our use of embedding-space features that target cumulative semantic drift orthogonal to character-level surface signals.",
  "opportunity": "By April 2025, 74.2% of newly created web pages contain some AI-generated text — of which 2.5% are fully AI-generated and 71.7% are human-AI blends, where human content has been AI-revised or AI-assisted (Ahrefs, 900K pages, April 2025). These blended documents may occupy an intermediate 'Gen0.5' depth position between Gen0 and Gen1 that depth scoring can address more precisely than binary detection, and they represent the dominant contamination modality at web scale. Complete decontamination is operationally infeasible — there is not enough uncontaminated human text to replace even the fully AI-generated fraction — shifting the practical research question from 'remove all synthetic data' (impossible at web scale) to 'which synthetic documents to prioritize for removal given a fixed filtering budget.' Depth-stratified decontamination addresses this directly: if Gen2+ documents are disproportionately harmful relative to Gen1 documents, preferential removal of deeper-generation text maximizes collapse mitigation per unit of filtering effort. This claim is explicitly scoped to *severity reduction per filtering budget*, not collapse prevention, and is tested in controlled fixed-total-size depth-composition conditions that isolate the effect of contamination depth from dataset volume — making the causal evidence for the governance claim empirically clean. Strong Model Collapse (ICLR 2025) provides the urgency but not the answer — it shows synthetic data is harmful at any non-vanishing fraction but gives no guidance on whether all synthetic data is equally harmful. Crucially, the paper does not distinguish Gen1 from Gen2 synthetic data at all, leaving the depth-dependent harm gradient completely unmeasured. A depth classifier that enables tiered decontamination — or, if depth discrimination fails, definitively establishes that binary filtering suffices — constitutes a concrete empirical contribution with direct governance impact, aligned with EMNLP 2026's special theme 'New Missions for NLP Research,' which explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance.'",
  "landscape": "Model collapse from recursive synthetic training is established (Shumailov et al., Nature 2024; Strong Model Collapse, ICLR 2025) and the limiting theory predicts collapse at any non-vanishing synthetic fraction. Mitigation via real-data accumulation (arXiv:2404.01413) or verifier-guided retraining (arXiv:2510.16657) is active. arXiv:2602.10531 ('From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources', February 2026) analyzes the statistical dynamics of iterative training on data contaminated with synthetic samples using a mixture-model framework, showing that improvement over collapsed models is possible when sufficient fresh real data is present; it does not assign generational depth labels to documents or propose a depth-stratified filtering method. Training-side collapse prevention via Truncated Cross-Entropy loss (ForTIFAI, arXiv:2509.08972) selectively ignores high-confidence tokens during training to filter synthetic artifacts — a complementary but orthogonal approach to our upstream corpus-level depth detection: ForTIFAI does not classify documents by generational depth and does not operate pre-training. The closest upstream related work, 'Machine-generated text detection prevents language model collapse' (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025), directly bridges AI-text detection and collapse prevention: it trains encoder-only binary classifiers (evaluating RoBERTa, DeBERTa-v3, and ModernBERT) to distinguish human from AI-generated text, then applies importance resampling — weighting each training document by (1-q(x))^b where q(x) is the classifier's AI-probability score — to up-weight likely human content during recursive training. Experiments across GPT-2 and SmolLM2 (124M–1.7B parameters) demonstrate that binary-classifier-guided resampling prevents collapse and even improves over training on purely human data. Critically, arXiv:2502.15654 treats all AI-generated text as equivalent regardless of generational provenance: importance weights depend only on a single binary human/AI probability, with no distinction between Gen1 text (one fine-tuning cycle removed from human data) and Gen2+ text (recursively compounded). Our work directly addresses this gap: if depth-stratified resampling weights — proportional to estimated generational distance from Gen0 — yield greater collapse-severity reduction per resampled document than flat binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over arXiv:2502.15654's strategy under budget-constrained filtering. The dual null-hypothesis design explicitly covers the scenario where depth discrimination fails (AUC < 0.65), in which case our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant and binary resampling is sufficient — a governance finding with direct practical value. A mathematical framework for how recursive publication compresses text through drift and selection is developed in arXiv:2604.08554 but does not propose a depth classifier. The framework is derived for variable-order n-gram agents and does not address transformer fine-tuning; extension to neural models is an open theoretical question that our experiments probe empirically. AI-generated text detection (arXiv:2303.11156, arXiv:2509.18880) addresses binary classification and reaches AUC ~0.85-0.90 for Gen1 text, uniformly treating all AI-generated text as equivalent regardless of generational provenance. Embedding-based representations show intrinsic separability between AI-generated and human text in compressed embedding spaces (arXiv:2408.10437), motivating our use of embedding-space distance features alongside surface-level signals. 'Understanding Transformers via N-gram Statistics' (arXiv:2407.12034, NeurIPS 2024) provides empirical motivation for applying n-gram-derived theoretical predictions to transformer fine-tuning: transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions across TinyStories and Wikipedia, suggesting transformer distributional behavior closely approximates n-gram statistics at the local prediction level — supporting our hypothesis that the monotonic drift prediction of arXiv:2604.08554 (derived for n-gram agents) extends to transformer fine-tuning at the distributional level, with our experiments constituting a direct empirical test of this generalization. 'Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection' (arXiv:2605.01647, May 2026) introduces the Letter Distribution Score (LD-Score) and establishes a 'Wall of Separation' where human-AI divergence significantly exceeds AI-AI divergence in character-distribution space — with the direct implication that within-model generational divergence (Gen1 vs. Gen2 from the same fine-tuned 0.6B model) is smaller still than cross-model AI-AI divergence. This finding validates our architectural choice to prioritize embedding-space features over character-distribution proxies: our mean cosine distance from Gen0 centroid and within-document embedding variance operate in a representation space where cumulative semantic drift — predicted to accumulate monotonically by arXiv:2604.08554's recursive drift-selection framework — may remain detectable even when surface and character-level signals converge. The pre-specified AUC threshold (0.65) and dual null-hypothesis pivot design explicitly account for the scenario where depth discrimination fails at the document level despite embedding-space features. No paper in the contamination detection surveys (arXiv:2502.14425, arXiv:2406.04244) addresses generation depth as a variable. The closest concurrent work — 'Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models' (arXiv:2511.17602, Nov 2025) — asks whether synthetic data overlaps with evaluation benchmarks, not how many generative cycles deep a document is; generational ancestry is orthogonal to benchmark overlap. 'Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training?' (TrainProVe, CVPR 2025, arXiv:2503.09122) achieves >99% accuracy verifying which text-to-image model generated a given image, using model access and generalization error bounds — differentiation is sharp: TrainProVe operates in the image domain and requires model weights access, while our method operates on raw text documents with no model access, enabling upstream corpus-level pre-filtering. Both address data governance but via entirely complementary mechanisms. 'A Closer Look at Model Collapse' (arXiv:2509.16499, NeurIPS 2025 Spotlight) identifies a generalization-to-memorization transition but studies diffusion models and does not distinguish depth levels in training data.",
  "approach": "We build a controlled genealogical corpus by running a 2-step recursive train-generate loop with Qwen3-0.6B (the smallest Qwen3 model, chosen to minimize sequential compute cost while still exhibiting measurable distributional drift per generation), producing text with verified depth labels Gen0 (human, sourced from FineWeb-Edu and C4), Gen1, and Gen2, yielding ~200K labeled documents per depth level across diverse domains. All generated documents are hard-capped at 512 tokens maximum length: this cap is enforced at generation time via the `max_new_tokens=512` parameter, making generation time deterministic and reviewable. At 200K documents × 512 tokens = 102M tokens per generational step, batched A100 inference at 3,000–5,000 tok/s for Qwen3-0.6B yields approximately 6–9 GPU hours per step — consistent with the timeline estimate below. The 512-token cap is scientifically defensible for depth discrimination: surface-level signals (surprisal burstiness, lexical diversity, n-gram entropy) and embedding-space signals (mean cosine distance from Gen0 centroid, within-document window embedding variance) are fully computable over 512-token documents, and ordinal regression classifiers trained on short-document depth signals are directly comparable to the binary detectors in arXiv:2502.15654, which also operate on variable-length web documents.\n\nWe disable Qwen3-0.6B thinking mode during all generative steps via the hard switch `enable_thinking=False` in `tokenizer.apply_chat_template`, rather than the soft `/no_think` instruction tag — because GitHub discussion QwenLM/Qwen3 #1329 documents that the 0.6B model lacks sufficient instruction-following capacity to reliably honor `/no_think` when placed in the system prompt, and silent failure would inject `&lt;think>…&lt;/think>` reasoning traces into Gen1/Gen2 documents that are absent from Gen0 human text, making depth levels trivially separable by token-level artifacts rather than genuine semantic drift and invalidating the AUC signal. The `enable_thinking=False` hard switch operates at the tokenizer template level and does not depend on the model's instruction-following capacity. As a final post-hoc verification, every generated document is scanned for `&lt;think>` tokens and discarded if any are found, before corpus inclusion.\n\nLimiting to Gen0/Gen1/Gen2 compresses the sequential corpus construction bottleneck to approximately 2 wallclock days: Qwen3-0.6B fine-tuning on a 200K-document sample runs in ~4-6 GPU hours on A100, and generation of 200K new 512-token documents runs in ~6-9 GPU hours, for ~12-15 GPU hours per generational step. The hard sequential dependency spans only 2 steps.\n\nWe train a DeBERTa-v3-large ordinal regression classifier jointly on raw text and depth-diagnostic features spanning two categories: (a) surface-level signals — per-token surprisal variance (burstiness), lexical diversity decay (MTLD and type-token ratio), and n-gram entropy compression ratio; and (b) embedding-space signals — (i) mean cosine distance of within-document window embeddings from the pre-computed Gen0 centroid (capturing average depth of embedding drift from human text), and (ii) variance of per-window cosine distances from the Gen0 centroid within the document (capturing within-document heterogeneity of embedding drift). Both embedding features are computed from non-overlapping 128-token window embeddings produced by sentence-transformers/all-MiniLM-L6-v2; feature (i) measures central tendency and feature (ii) measures distributional spread — distinct geometric properties: a Gen2 document may exhibit both higher mean distance from Gen0 and more heterogeneous window-level drift than a Gen1 document, as cumulative generational compression produces uneven semantic displacement within a document. We integrate these five scalar depth-diagnostic features by concatenating them to the DeBERTa-v3-large CLS token representation (1024-dim), then training an ordinal regression head over this joint 1029-dim representation; the Gen0 embedding centroid is precomputed offline from a held-out Gen0 reference set of 10K documents using sentence-transformers/all-MiniLM-L6-v2 and is not updated during classifier training.\n\nEmbedding-space features are specifically motivated by the 'Wall of Separation' established in arXiv:2605.01647 (May 2026): AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence (Gen1→Gen2 from the same fine-tuned 0.6B model) is smaller still. Surface-level and character-distribution signals are therefore unlikely to reliably discriminate depth levels in this setting; our mean cosine distance from Gen0 centroid and within-document embedding variance instead target cumulative semantic drift that arXiv:2604.08554's recursive drift-selection framework predicts to accumulate monotonically across generations even when character distributions plateau — providing detection signal orthogonal to surface proxies. The argument is: our embedding-space features target cumulative semantic drift that persists even when surface divergence converges, consistent with the monotonic drift predicted by arXiv:2604.08554 — with the explicit caveat that arXiv:2604.08554 derives this prediction for variable-order n-gram agents, not transformer fine-tuning. We hypothesize the generalization holds because transformer next-token distributions closely approximate n-gram statistics at the local prediction level (arXiv:2407.12034, NeurIPS 2024, reports 68–79% agreement between transformer predictions and n-gram rulesets across two corpora), suggesting transformer fine-tuning implicitly performs distributional compression analogous to n-gram compression, for which cumulative drift is expected to accumulate monotonically. Our classifier and collapse experiments directly test whether this hypothesized generalization from n-gram theory to transformer practice holds empirically.\n\nCentral technical risk and dual null-hypothesis design: We pre-specify two complementary pre-registered outcome scenarios to ensure a definitive, interpretable empirical finding under all classifier and collapse experiment outcomes. (Primary null) If the ordinal classifier falls below AUC 0.65 on Gen1/Gen2 discrimination, the finding is publishable: depth beyond Gen1 is linguistically indistinguishable at the document level using current text-level and embedding-level methods, implying binary filtering suffices — consistent with the implicit assumption of arXiv:2502.15654. In this case, the collapse validation experiments automatically pivot to directly comparing binary (Gen0-only) filtering against depth-stratified filtering at fixed corpus size. (Secondary null) If the classifier achieves AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between conditions (b) (100K Gen0 + 100K Gen1) and (c) (67K Gen0 + 67K Gen1 + 66K Gen2) at fixed total corpus size (paired t-test, α = 0.05, across 3 random seeds), we report this as a distinct secondary null outcome: depth detection is feasible but equal-fraction Gen2 contamination causes no additional collapse-severity beyond equal-fraction Gen1 contamination at GPT-2 scale — the marginal harm-per-generation curve is flat at this model size, binary filtering is sufficient for practical governance at small scales, and preferential Gen2 removal yields no measurable advantage at this scale. This finding has direct governance implications while leaving open whether depth stratification provides additional value at larger model scales, explicitly reserved as future work. All four logical combinations of (AUC pass/fail) × (collapse severity parity/non-parity) produce pre-specified, interpretable empirical contributions with distinct governance implications.\n\nThe trained classifier is applied zero-shot to real FineWeb and C4 slices to estimate depth-distribution statistics of existing pretraining corpora. Collapse validation uses a GPT-2-scale LM fine-tuned on three fixed-total-size depth-composition conditions (200K training documents each), following the controlled-composition standard of Strong Model Collapse (ICLR 2025): (a) Gen0-only: 200K Gen0; (b) Gen0+Gen1: 100K Gen0 + 100K Gen1; (c) Gen0+Gen1+Gen2: 67K Gen0 + 67K Gen1 + 66K Gen2. These corpora are constructed by subsampling from the already-generated 200K-document pools at each depth level, requiring no additional generation compute. Fixing total corpus size at 200K across all three conditions isolates the causal effect of depth composition from dataset volume: any observed collapse severity difference between conditions reflects contamination depth, not training set size — making the central governance claim ('Gen2 contamination is more harmful per document than Gen1 at equal contamination rate') empirically defensible. Collapse severity is tracked via held-out human-text perplexity and output tail entropy across multiple recursive training generations, explicitly scoped to measuring *severity as a function of depth composition at fixed scale* rather than collapse prevention — consistent with Strong Model Collapse's any-fraction harm finding. GenDepth-Bench is scoped to 2 model families: Qwen3-0.6B (primary) and Llama-3.2-1B (secondary, run through the same recursive loop to test cross-model generalizability of depth signals, explicitly optional — executed only if compute budget permits; see resource estimate). Coverage of 5+ model families is explicitly reserved as future work.\n\n16-Day Critical Path (EMNLP 2026 ARR deadline May 25, 2026; today May 9, 2026):\n— Days 1-2: Environment setup; sample 200K Gen0 docs from FineWeb-Edu/C4 (truncated to 512 tokens); prepare evaluation suite and draft intro/related-work sections.\n— Days 2-3 (sequential bottleneck step 1): Fine-tune Qwen3-0.6B on Gen0 (~4-6h GPU); generate 200K Gen1 documents at max 512 tokens each (~6-9h GPU; 200K × 512 tokens = 102M tokens ÷ 3,000–5,000 tok/s ≈ 6–9h) with `enable_thinking=False` hard switch and post-hoc `&lt;think>` token scan.\n— Days 3-4 (sequential bottleneck step 2): Fine-tune Qwen3-0.6B-v2 on Gen1 (~4-6h GPU); generate 200K Gen2 documents at max 512 tokens each (~6-9h GPU) with same thinking-mode controls.\n— Days 3-8 (PARALLEL TRACK A): DeBERTa-v3-large ordinal training begins with Gen0+Gen1 data at Day 3; adds Gen2 data when available at Day 5; ablations over surface vs. embedding feature subsets.\n— Days 5-10 (PARALLEL TRACK B): GPT-2-scale collapse experiments begin at Day 5 with fixed-size conditions (a) Gen0-only: 200K Gen0 and (b) Gen0+Gen1: 100K Gen0+100K Gen1 (subsampled from existing pools); add condition (c) Gen0+Gen1+Gen2: 67K each at Day 6 when Gen2 corpus is available. Llama-3.2-1B recursive corpus generation runs in parallel if compute budget is below 160h H100-equivalent at Day 5.\n— Days 7-9: Full classifier evaluation; if Gen1/Gen2 AUC < 0.65, activate primary null-hypothesis binary filtering comparison experiments; if AUC ≥ 0.65 but collapse severity parity detected between conditions (b) and (c), record secondary null outcome and report governance implications.\n— Days 9-10: Zero-shot depth scoring on real FineWeb/C4 slices.\n— Days 10-12: Feature importance ablations; cross-model generalizability check on Llama-3.2-1B-generated corpus (if optional Llama recursive corpus was generated).\n— Days 12-16: Analysis, writing, revision, and submission.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~210h A100 (40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B, each step generating 200K documents at 512 tokens max = 102M tokens ÷ ~3,500 tok/s average ≈ ~8h per step, ×2 steps = ~16h generation + ~24h fine-tuning over 2 steps + 50h DeBERTa-v3-large fine-tuning and ablations + 120h GPT-2-scale collapse validation experiments across 3 fixed-size depth-composition conditions)",
      "gpu_utilization": "High idle rate (~40-60%): GPU waits while researcher designs experiment configs, interprets collapse curves, debugs depth signal quality, and writes between each stage over several months",
      "timeline": "4-6 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$370 at $1.75/h blended A100 average (RunPod ~$1.49/h, Lambda ~$2.06/h); approximately 70 H100-equivalent hours"
    },
    "human_in_loop": {
      "gpu_hours": "~320h A100 (agent handles training loop queuing and ablation scheduling; human approves depth-feature selection, collapse experiment design, AUC threshold decision for null-hypothesis activation, and Llama-3.2-1B second-family validation)",
      "gpu_utilization": "Moderate idle rate (~15-25%): agent queues overnight runs and fills GPU gaps between sequential generational steps; handles parallel DeBERTa and collapse experiment scheduling",
      "timeline": "6-10 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$60-120 (~600-800 agent turns at $0.08-0.15/turn for experiment design, result interpretation, and iteration guidance)",
      "estimated_gpu_cost": "~$560 at $1.75/h average A100; approximately 107 H100-equivalent hours",
      "risk_note": "Key bottleneck: 2-step sequential corpus construction (train on GenN → generate GenN+1 at 512 tokens max → train again) cannot be parallelized; each step adds ~1 wallclock day with Qwen3-0.6B. The 512-token document cap makes generation time deterministic: 200K × 512 tokens = 102M tokens ÷ 3,000–5,000 tok/s ≈ 6–9h per step, matching the timeline estimate and eliminating schedule uncertainty from variable document lengths. Corpus construction for collapse experiments uses fixed-total-size subsampling (200K per condition) from the already-generated per-depth pools — no additional generation compute required. Pre-specified dual null-hypothesis design (primary: AUC < 0.65; secondary: AUC ≥ 0.65 but collapse severity parity between fixed-size conditions (b) and (c)) means the agent has clear decision rules without requiring researcher judgment to pivot, covering all four logical outcome combinations."
    },
    "auto_research": {
      "gpu_hours": "~490h A100 / ~163h H100-equivalent hours (mandatory, within ≤200h hard constraint): 40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B (200K documents × 512 tokens max per step = 102M tokens; at 3,000–5,000 tok/s ≈ 6–9h generation per step, ×2 steps; plus ~12h fine-tuning per step = ~40h total) + 120h DeBERTa-v3-large fine-tuning and ablations with 2x hyperparameter search across depth-feature combinations (surface-only, embedding-only, combined) + 240h GPT-2-scale collapse validation experiments across 3 fixed-total-size depth-composition conditions (Qwen3-0.6B family) with 3 collapse metrics + 90h auxiliary ablations (feature importance, zero-shot FineWeb/C4 scoring, null-hypothesis binary filtering comparison if AUC threshold triggered). Llama-3.2-1B recursive corpus generation and collapse experiments (~60-90h A100 / ~20-30h H100-equivalent) are explicitly optional from the start: executed only if compute budget remains below 160h H100-equivalent at Day 10; otherwise deprioritized to zero-shot depth scoring only, maintaining a genuine 40h safety buffer against the 200h hard ceiling.",
      "gpu_utilization": "Near-zero idle (<5%): agent queues hyperparameter sweeps and ablations 24/7, filling GPU cycles between sequential generational construction steps with parallel auxiliary experiments",
      "timeline": "13-16 days with 4-6 concurrent A100s",
      "team": "0 (4-6h one-time setup: genealogical corpus schema with 512-token document cap, experiment grid, AUC threshold 0.65 for primary null-hypothesis activation, paired t-test criterion for secondary null-hypothesis activation between fixed-size conditions (b) and (c), stopping conditions)",
      "claude_api_cost": "$250-400 (~2500-3000 agent turns for experiment orchestration, result analysis, and adaptive exploration)",
      "estimated_gpu_cost": "~$856 at $1.75/h average A100 (mandatory only); ~$960 including optional Llama-3.2-1B corpus if budget permits",
      "speed_bottleneck": "2-step sequential corpus construction is the hard wallclock floor; the 512-token document cap makes per-step generation time deterministic at ~6-9h (102M tokens ÷ 3,000–5,000 tok/s), eliminating schedule uncertainty; GPU count limits simultaneous ablation breadth during non-sequential phases",
      "risk_note": "Corpus construction for collapse experiments uses fixed-total-size subsampling (200K per condition from already-generated per-depth pools) — no additional generation compute. Depth signal may be weak between Gen1 and Gen2 from the same small model — a risk compounded by the 'Wall of Separation' finding (arXiv:2605.01647): AI-AI surface divergence is substantially smaller than human-AI divergence, making within-model generational discrimination harder still. Pre-specified dual null-hypothesis design covers all outcomes: primary null (AUC < 0.65) redirects to binary filtering comparison at fixed corpus size; secondary null (AUC ≥ 0.65 but collapse severity parity between fixed-size conditions (b) and (c)) reports depth detection as feasible but equal-fraction Gen2 contamination as causing no incremental governance harm beyond Gen1 at GPT-2 scale. Embedding-space features (mean cosine distance from Gen0 centroid and within-document embedding variance over 128-token windows) partially mitigate the primary null risk by targeting cumulative semantic drift invisible at the surface level. Budget contingency: Llama-3.2-1B recursive corpus generation is explicitly optional from the start; if compute approaches 160h H100-equivalent during execution, Llama-3.2-1B recursive corpus is deprioritized to zero-shot depth scoring only (no new collapse experiments), saving ~60-90h A100 (~20-30h H100-equivalent) and maintaining a genuine 40h buffer against the 200h hard ceiling."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; special theme 'New Missions for NLP Research' explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance' — near-perfect topical alignment; conference October 24-29, Budapest)",
    "NAACL 2027 (ARR cycle deadline TBD, expected ~late 2026; safe backup with more time for thorough collapse validation experiments and additional model families)"
  ],
  "level": "solid",
  "key_references": [
    "AI models collapse when trained on recursively generated data (Nature 2024)",
    "Strong Model Collapse (ICLR 2025) — establishes collapse at any non-vanishing synthetic fraction (~1% example); holds total corpus size fixed while varying synthetic fraction (the controlled design our collapse experiments follow); does not distinguish Gen1 from Gen2 synthetic data; this gap is what we fill",
    "Machine-generated text detection prevents language model collapse (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025) — closest upstream prior work: trains binary encoder-only classifiers (evaluating RoBERTa, DeBERTa-v3, ModernBERT) with importance resampling — weights ∝ (1-q(x))^b — to prevent collapse at GPT-2/SmolLM2 scale (124M–1.7B parameters); treats all AI-generated text equivalently without generational depth distinction; our work directly extends this: if depth-stratified resampling weights yield greater collapse-severity reduction per decontamination unit than binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over binary resampling under budget constraints; if not (AUC < 0.65 or collapse severity parity between fixed-size conditions (b) and (c)), our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant",
    "From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources (arXiv:2602.10531, February 2026) — analyzes the statistical dynamics of iterative training on contaminated data using a mixture-model framework, showing that improvement over collapsed models is possible when sufficient fresh real data is present; does not assign generational depth labels to documents or propose a depth-stratified filtering method",
    "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (arXiv:2404.01413)",
    "Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence (arXiv:2510.16657)",
    "ForTIFAI: Fending Off Recursive Training Induced Failure for AI Models (arXiv:2509.08972) — training-side collapse prevention via Truncated Cross-Entropy loss; orthogonal to our upstream corpus-level depth detection; does not classify documents by generational depth",
    "Drift and Selection in LLM Text Ecosystems (arXiv:2604.08554) — mathematical framework for how recursive publication compresses text through drift and selection; derived for variable-order n-gram agents (not transformer fine-tuning); does not propose a depth classifier or detection method; motivates our prediction that embedding-space drift accumulates monotonically across generations even when surface distributions plateau, under the hypothesis that transformer fine-tuning implicitly performs distributional compression analogous to n-gram compression — a generalization our experiments directly test",
    "Understanding Transformers via N-gram Statistics (arXiv:2407.12034, NeurIPS 2024) — transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions across TinyStories and Wikipedia; provides empirical grounding for our hypothesis that the monotonic drift prediction of arXiv:2604.08554 (derived for n-gram agents) extends to transformer fine-tuning at the distributional level",
    "Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection (arXiv:2605.01647, May 2026) — establishes 'Wall of Separation' where human-AI divergence significantly exceeds AI-AI divergence in character-distribution space; within-model generational gap (Gen1→Gen2 from same fine-tuned model) is smaller still; directly threatens surface-level discriminability; our counter-argument: embedding-space features (mean cosine distance from Gen0 centroid and within-document window embedding variance, computed over non-overlapping 128-token windows via sentence-transformers/all-MiniLM-L6-v2) target cumulative semantic drift orthogonal to character-distribution signals; the pre-specified dual null-hypothesis design accounts for the possibility that depth discrimination fails despite embedding-space features",
    "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective (NeurIPS 2025 Spotlight)",
    "RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (ACL 2024)",
    "Can AI-Generated Text be Reliably Detected? (arXiv:2303.11156)",
    "Diversity Boosts AI-Generated Text Detection (arXiv:2509.18880)",
    "Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models (arXiv:2511.17602) — asks whether synthetic data overlaps with evaluation benchmarks; generational ancestry is orthogonal to benchmark overlap",
    "Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training? (TrainProVe, CVPR 2025, arXiv:2503.09122) — achieves >99% accuracy in image domain using model access and generalization error bounds; differentiation: our method operates on raw text with no model access, enabling upstream corpus-level pre-filtering; different modality and mechanism address the same governance goal",
    "Understanding Generative AI Content with Embedding Models (arXiv:2408.10437) — demonstrates intrinsic separability of AI-generated and human text in compressed embedding space; motivates our use of embedding-space cosine distance and within-document variance features for depth discrimination beyond surface-level signals",
    "Benchmark Data Contamination of Large Language Models: A Survey (arXiv:2406.04244)",
    "A Survey on Data Contamination for Large Language Models (arXiv:2502.14425)"
  ],
  "description": "As web corpora become saturated with AI-generated content (74.2% of new web pages contain some AI text by April 2025, of which 2.5% are fully AI-generated and 71.7% are human-AI blends; Ahrefs, 900K pages), complete decontamination is operationally infeasible, shifting the question to: which synthetic documents cause the most harm and should be removed first? We propose Genealogical Depth Scoring, a method extending binary AI-text detection to ordinal depth classification (Gen0=human, Gen1, Gen2), trained on a controlled corpus produced by 2-step recursive train-generate loops using Qwen3-0.6B with thinking mode disabled via the hard switch `enable_thinking=False` in `tokenizer.apply_chat_template` — rather than the soft `/no_think` instruction tag, which silently fails for the 0.6B model when placed in the system prompt (GitHub QwenLM/Qwen3 discussion #1329) and would introduce `&lt;think>…&lt;/think>` artifacts that make depth levels trivially separable by token-level signals rather than genuine semantic drift — with post-hoc discard of any documents containing `&lt;think>` tokens before corpus inclusion. All generated documents are hard-capped at 512 tokens via `max_new_tokens=512`, yielding 200K × 512 tokens = 102M tokens per generational step; at 3,000–5,000 tok/s for Qwen3-0.6B on A100 this takes approximately 6–9 GPU hours per step, making the generation timeline deterministic and anchored to a verifiable arithmetic bound. The classifier combines DeBERTa-v3-large fine-tuning with two classes of depth-diagnostic features: surface-level signals (surprisal burstiness, lexical diversity decay, n-gram entropy compression ratio) and embedding-space signals — (i) mean cosine distance of within-document window embeddings from the Gen0 centroid, and (ii) variance of per-window cosine distances from the Gen0 centroid within the document, both computed over non-overlapping 128-token windows via sentence-transformers/all-MiniLM-L6-v2. Feature (i) captures average drift from human text in embedding space; feature (ii) captures within-document heterogeneity of that drift — distinct geometric properties (central tendency vs. distributional spread) that together characterize the document's depth signature. These five scalar features are concatenated to the DeBERTa-v3-large CLS token representation (1024-dim) and passed to an ordinal regression head trained over the joint 1029-dim representation; the Gen0 centroid is precomputed offline and not updated during training. The embedding-space features directly address the 'Wall of Separation' documented in arXiv:2605.01647 (May 2026) — AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence is smaller still — by targeting cumulative semantic drift that arXiv:2604.08554 predicts to accumulate monotonically across recursive generations even when surface statistics plateau. Because arXiv:2604.08554 derives this prediction for variable-order n-gram agents rather than transformer fine-tuning, we ground the generalization in arXiv:2407.12034 (NeurIPS 2024), which shows transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions, and treat our classifier and collapse experiments as a direct empirical test of whether this theoretical extension holds. We pre-specify a dual null-hypothesis design: (primary null) if Gen1/Gen2 AUC < 0.65, depth is linguistically indistinguishable and binary filtering suffices; (secondary null) if AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between fixed-size conditions (b) (100K Gen0 + 100K Gen1) and (c) (67K Gen0 + 67K Gen1 + 66K Gen2), equal-fraction Gen2 contamination causes no additional collapse-severity beyond equal-fraction Gen1 contamination at GPT-2 scale — depth detection is feasible but depth-stratified filtering provides no incremental governance benefit at small model scale. All four logical outcomes produce pre-specified, interpretable empirical contributions. Collapse validation compares three fixed-total-size depth-composition conditions (200K documents each: (a) Gen0-only; (b) 100K Gen0+100K Gen1; (c) 67K Gen0+67K Gen1+66K Gen2), constructed by subsampling from the already-generated 200K-document pools at each depth level — no additional generation compute. Fixing total corpus size across all conditions isolates the causal effect of depth composition from dataset volume, making the central governance claim ('Gen2 contamination is more harmful per document than Gen1 at equal contamination rate, supporting preferential Gen2 removal per filtering unit') empirically defensible. Results are framed as *collapse severity as a function of contamination depth composition at fixed scale*, directly informing the real-world budget-constrained decontamination problem. TrainProVe (CVPR 2025) addresses related governance goals via model access in the image domain; ForTIFAI (arXiv:2509.08972) prevents collapse at training time via modified loss; arXiv:2502.15654 (Feb 2025) prevents collapse via binary detection with importance resampling but treats all AI text equivalently without generational depth distinction; arXiv:2602.10531 (Feb 2026) analyzes collapse dynamics statistically via mixture models but does not classify text by generational depth — our work is the first to assign generational depth scores to raw text corpus documents upstream of training, and directly tests whether depth-stratified resampling yields greater collapse-severity reduction per filtering unit than binary resampling. We release GenDepth-Bench covering 2 model families (Qwen3-0.6B primary; Llama-3.2-1B secondary, optional pending compute budget), with 5+ family coverage as explicit future work. Targets EMNLP 2026's special theme on synthetic data feedback loops and data governance.",
  "project_name": "gen_depth_decontam",
  "source": "web_research"
}

## Reviewer feedback (round 8)
Issues: ["REPLICABILITY GAP — Ordinal regression head type unspecified: The approach specifies concatenating 5 scalar features to the DeBERTa-v3-large CLS token (1029-dim joint representation) and training an 'ordinal regression head,' but does not specify which ordinal regression method. For 3 ordered classes (Gen0, Gen1, Gen2), common implementations differ in boundary-structure assumptions: (a) CORAL-loss based with 2 auxiliary binary classifiers (arXiv:1901.07884; arXiv:2111.08851), (b) proportional odds logistic regression with 2 threshold parameters, or (c) 3-class softmax with ordinal label weighting. Reviewers checking replicability will notice this gap. Fix: add one sentence specifying the implementation, e.g., 'We use CORAL-loss based ordinal regression (arXiv:2111.08851) decomposing the 3-class problem into 2 binary classifiers with shared feature weights and independently trained bias terms over the 1029-dim joint representation.' This closes the replicability gap without any experimental change.", "STATISTICAL POWER ACKNOWLEDGMENT MISSING — Secondary null hypothesis is underpowered: The pre-specified secondary null criterion (paired t-test, α=0.05, N=3 seeds, df=2) has a critical t-value of 4.303, providing power < 20% for Cohen's d < 2.0. If Gen2 contamination causes a real but moderate increase in collapse severity (e.g., 10–20% worse perplexity), 3 seeds cannot detect it, and non-rejection would falsely validate the 'depth stratification provides no incremental benefit' conclusion. This is the weakest statistical link in the pre-registered design and a reviewer will attack it. Fix: add one sentence explicitly acknowledging the limitation, e.g., 'We note that with 3 seeds the secondary null test is powered primarily to detect large effect sizes; non-rejection at this scale does not rule out moderate depth effects detectable with more seeds, which we reserve as future work at larger compute budgets.' This converts a reviewer attack surface into a transparent acknowledged limitation.", "MISSING CITATION — arXiv:2509.04796 'Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training' (September 2025): This paper demonstrates a three-stage recursive training phenomenon where surface fluency persists while factual accuracy collapses — providing complementary empirical support for the claim that deeper-generation text causes qualitatively distinct harm that perplexity alone may understate. An area chair familiar with the model collapse literature (likely at EMNLP 2026 given the special theme) may flag its absence. One citation line in the landscape section suffices: 'arXiv:2509.04796 shows that factual accuracy collapses faster than perplexity in recursive synthetic training — motivating depth-stratified decontamination as a mechanism to preferentially remove documents at generational depths where factual quality is most degraded; it does not classify documents by generational depth or propose a depth-stratified filtering method.'"]
Feedback: All seven Round 7 issues are resolved: the 512-token document cap is explicitly stated with anchored arithmetic (200K × 512 tokens ÷ 3,000–5,000 tok/s = 6–9h per step), arXiv:2602.10531 is cited and differentiated, and all prior round issues remain correctly addressed. Three targeted fixes will complete this proposal: (1) Specify the ordinal regression head implementation — add one sentence naming the method (recommend CORAL-loss based, citing arXiv:2111.08851, since it is rank-consistent and well-tested for 3-class ordinal problems with PyTorch implementations readily available). (2) Add one sentence acknowledging the 3-seed secondary null test is powered for large effect sizes only, explicitly reserving higher-powered validation as future work. (3) Add arXiv:2509.04796 to the landscape with a one-line differentiation. All three fixes require under 30 minutes of writing and zero new experiments. Independent novelty verification confirms no competing work on generational depth scoring for corpus decontamination exists through May 2026.

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
这个 idea 已经经过 8 轮修订，近 3 轮的平均分从 3.8 到 3.8，没有明显改善。

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
  "promptId": "c21f7a39-88cd-479f-9bae-235f728d85d3",
  "type": "user",
  "uuid": "e3a844a7-95ce-4353-8734-e2b791731c3e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-09T21:12:33.016Z_

```json
{
  "parentUuid": "e3a844a7-95ce-4353-8734-e2b791731c3e",
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
  "uuid": "84f72cd5-fce0-4c09-aee7-408dd0cd4be3",
  "timestamp": "2026-05-09T21:12:33.016Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-09T21:12:33.016Z_

```json
{
  "parentUuid": "84f72cd5-fce0-4c09-aee7-408dd0cd4be3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "da1af1ae-3466-4280-8ba4-c343ff1d3715",
  "timestamp": "2026-05-09T21:12:33.016Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-09 (UTC).**  ## Original idea {   \"title\": \"Genealogical Depth Scoring for Recursive Web Corpus Decontamination\",…",
  "leafUuid": "da1af1ae-3466-4280-8ba4-c343ff1d3715",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Generational depth scoring for synthetic text corpus decontamination",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d"
}
```

---

### Assistant

_source line 8 · 2026-05-09T21:13:05.991Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully before deciding on my approach.

## Current State Analysis

This idea has gone through 8 rounds of revision with scores staying around 3.8 for the last 3 rounds. The reviewer feedback in Round 8 identifies 3 specific, targeted fixes:

1. **REPLICABILITY GAP**: Specify the ordinal regression head implementation (CORAL-loss based, one sentence)
2. **STATISTICAL POWER ACKNOWLEDGMENT**: Add one sentence acknowledging 3-seed test is underpowered for moderate effects
3. **MISSING CITATION**: Add arXiv:2509.04796 to landscape


## Should I Pivot or Stay the Course?

The stagnation is concerning, but looking at the details: the reviewer explicitly states all seven Round 7 issues are resolved, and these three remaining fixes are genuinely minor—the reviewer estimates under 30 minutes of work with zero new experiments needed. The positive framing ("will complete this proposal") suggests these targeted changes could push the score higher, so I should implement them rather than abandon the direction. might be that despite resolving individual issues, the score hasn't risen because:
- Each round introduces the same number of new issues as it resolves
- OR the fundamental scoring is plateau'd at this level regardless

However, looking at this round's feedback: the reviewer says these 3 fixes will "complete" the proposal and explicitly says they're all minor (under 30 minutes). This suggests that after these fixes, the proposal might break through the 3.8 plateau.

The 3 issues in Round 8 are:
1. One sentence about CORAL-loss specification → This is genuinely minor, just replicability
2. One sentence about statistical power → This is important but only requires an acknowledgment, not a redesign
3. One citation → Also minor

Given the reviewer's positive assessment ("Independent novelty verification confirms no competing work on generational depth scoring for corpus decontamination exists through May 2026"), this doesn't seem like a case where pivoting is warranted. The idea has genuine novelty, the core problem is valid, and we're at the finishing-line stage.

Before finalizing, I should verify the key papers I'm citing—looking up arXiv:2509.04796, the CORAL-loss papers, and confirming there's no competing work I've missed. The real question is whether fixing these minor issues will actually lift the score past 3.8 or if it's genuinely stuck there. at 3.8 due to some deeper issue?

Looking at the review feedback: the reviewer doesn't mention any fundamental issues with the approach. The feedback is specific, technical, and fixable. The idea has:
- Clear novelty (no competing work)
- Strong motivation (model collapse literature)
- Good methodology 
- Dual null-hypothesis design (handles negative results)
- Strong connection to EMNLP 2026 special theme

I think the 3.8 plateau might just be because each round of review is discovering new minor issues, but the trajectory is toward completion. This round feels like the last set of genuine issues. Let me proceed with a **minor revision** to address the 3 specific issues.

## Plan for Revision

1. **Ordinal Regression Specification**: Add to the `approach` section and `description` a sentence specifying CORAL-loss based ordinal regression with 2 auxiliary binary classifiers sharing feature weights with independently trained bias terms.

2. **Statistical Power Acknowledgment**: Add to the `approach` section (secondary null hypothesis section) a sentence acknowledging that with 3 seeds, the test is powered primarily for large effect sizes.

3. **Missing Citation arXiv:2509.04796**: Add to `landscape`, `key_references`, and mention in relevant parts.

Now I need to track down these papers and verify the details before incorporating them. I'm looking for the knowledge collapse paper and the CORAL ordinal regression work to make sure I cite them correctly. I'll verify the CORAL citation details and do a quick check for any recent competing work on this topic before making the targeted revisions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da1af1ae-3466-4280-8ba4-c343ff1d3715",
  "isSidechain": false,
  "requestId": "req_011Casgdg7iyNAc5X9P3s9QC",
  "type": "assistant",
  "uuid": "664ee97b-1996-46e1-b18b-636ab307f5b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XjEnuN9jyrWKpVZyfyfNt7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17748,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2256,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 17748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17748
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-09T21:13:07.714Z_

Looking at this situation: 8 rounds of revision, 3 rounds at 3.8, but the Round 8 reviewer is saying "all prior issues resolved" and the 3 remaining fixes are explicitly minor. This doesn't signal a fundamental framing problem — it signals we're near completion. Before deciding pivot vs. minor fix, I need to verify the 3 cited papers and check for any new competing work that could threaten novelty.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "664ee97b-1996-46e1-b18b-636ab307f5b8",
  "isSidechain": false,
  "requestId": "req_011Casgdg7iyNAc5X9P3s9QC",
  "type": "assistant",
  "uuid": "7f4d3654-8caa-4597-9df8-09b65b9f3800",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XjEnuN9jyrWKpVZyfyfNt7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17748,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2256,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 17748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17748
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-09T21:13:13.515Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016mqtEmnbjevxoYAMmzMssM`</summary>

```json
{
  "description": "Research CORAL ordinal regression papers and knowledge collapse paper",
  "subagent_type": "Explore",
  "prompt": "I need you to fetch and summarize the abstracts/key details of three specific arXiv papers. Use WebFetch on the arXiv abstract pages for each. Report what you find for each paper.\n\n1. arXiv:2509.04796 - The reviewer describes it as \"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\" (September 2025). Fetch https://arxiv.org/abs/2509.04796 and report: actual title, authors, abstract, and key findings about recursive synthetic training and factual collapse vs. fluency.\n\n2. arXiv:2111.08851 - Reviewer describes it as a CORAL-loss ordinal regression paper. Fetch https://arxiv.org/abs/2111.08851 and report: actual title, authors, abstract, and what ordinal regression method it introduces.\n\n3. arXiv:1901.07884 - Original CORAL paper. Fetch https://arxiv.org/abs/1901.07884 and report: actual title, authors, and what ordinal regression method it introduces.\n\nReport findings accurately — I need to verify these citations are correct before using them in a research paper revision."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f4d3654-8caa-4597-9df8-09b65b9f3800",
  "isSidechain": false,
  "requestId": "req_011Casgdg7iyNAc5X9P3s9QC",
  "type": "assistant",
  "uuid": "46e69413-8e67-43e2-ae9a-28a61ae8d40b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XjEnuN9jyrWKpVZyfyfNt7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17748,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2256,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 17748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17748
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-09T21:13:20.166Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GJixFZNfthBf6ExL1M9L1H`</summary>

```json
{
  "description": "Search for competing work on generational depth detection for AI text",
  "subagent_type": "Explore",
  "prompt": "I'm working on a research paper about \"Genealogical Depth Scoring for Recursive Web Corpus Decontamination\" — specifically, assigning ordinal generation depth labels (Gen0=human, Gen1=AI, Gen2=AI-trained-on-AI) to training corpus documents to enable depth-stratified decontamination. The claim is this is novel with no competing work through May 2026.\n\nPlease search for any papers that might challenge this novelty claim. Use WebSearch with these queries:\n1. \"generational depth\" \"AI-generated text\" detection 2025 2026\n2. \"recursive synthetic data\" depth scoring classification\n3. \"second generation\" synthetic text detection corpus decontamination\n4. \"multi-generation\" AI text detection ordinal\n\nAlso search for any new work on knowledge collapse in LLMs from late 2025 or 2026 beyond what's cited (Shumailov Nature 2024, Strong Model Collapse ICLR 2025, arXiv:2602.10531).\n\nReport any papers found that directly address generational depth assignment to text documents. Be specific about what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46e69413-8e67-43e2-ae9a-28a61ae8d40b",
  "isSidechain": false,
  "requestId": "req_011Casgdg7iyNAc5X9P3s9QC",
  "type": "assistant",
  "uuid": "39201fbf-6de4-4d36-946a-e674fe552f73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XjEnuN9jyrWKpVZyfyfNt7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17748,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2256,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 17748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17748
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-09T21:13:29.366Z_

<details><summary>↩ Tool result · `toolu_016mqtEmnbjevxoYAMmzMssM`</summary>

```text
## Citation Verification Report

Here are the verified details for all three papers:

### 1. arXiv:2509.04796 - Knowledge Collapse in LLMs

**Actual Title:** "Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training"

**Authors:** Figarri Keisha, Zekun Wu, Ze Wang, Adriano Koshiyama, Philip Treleaven

**Abstract:** The paper investigates knowledge collapse when language models train repeatedly on synthetic data they generate themselves. It identifies a phenomenon where factual accuracy deteriorates while surface-level writing quality (fluency) remains intact, producing "confidently wrong" outputs.

**Key Findings:**
- Follows a three-stage degradation pattern where models maintain fluent output while factual accuracy erodes
- The collapse is instruction-dependent (conditional on formatting) rather than uniform
- Domain-specific synthetic training mitigates the problem while maintaining computational efficiency
- Developed detection framework combining model-level indicators with task-specific metrics

**Citation Status:** ✓ Matches reviewer's description accurately

---

### 2. arXiv:2111.08851 - Ordinal Regression Paper

**Actual Title:** "Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities"

**Authors:** Xintong Shi, Wenzhi Cao, Sebastian Raschka

**Abstract:** Proposes CORN (Conditional Ordinal Regression Network) for ordinal regression in deep neural networks using conditional probability distributions and the chain rule during training.

**Method Introduced:** CORN (Conditional Ordinal Regression Network) - improves upon CORAL by eliminating its weight-sharing constraint in the output layer, enhancing network expressiveness. Architecture-agnostic and compatible with any deep neural network classifier.

**Citation Status:** ⚠ **CAUTION** - This is NOT a CORAL-loss paper. It's a CORN paper that builds upon/improves CORAL. The reviewer's description calling it "a CORAL-loss ordinal regression paper" appears inaccurate.

---

### 3. arXiv:1901.07884 - Original CORAL Paper

**Actual Title:** "Rank consistent ordinal regression for neural networks with application to age estimation"

**Authors:** Wenzhi Cao, Vahid Mirjalili, Sebastian Raschka

**Abstract:** Addresses how standard loss functions fail to capture ordering information. Proposes CORAL (COnsistent RAnk Logits), which transforms ordinal targets into binary classification subtasks while ensuring rank consistency.

**Method Introduced:** CORAL (COnsistent RAnk Logits) - converts ordinal prediction into multiple binary classification problems with theoretical guarantees for rank-monotonicity. Works with any neural network architecture.

**Citation Status:** ✓ Correctly identified as the original CORAL paper

---

### Summary for Your Research

**Papers 1 and 3 are correctly cited.** However, **Paper 2 requires clarification**: It's a CORN paper that improves upon CORAL, not a CORAL-loss paper itself. If you're citing it as a CORAL-related work, make sure your text distinguishes that it proposes CORN as an enhancement, not as CORAL itself.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46e69413-8e67-43e2-ae9a-28a61ae8d40b",
  "isSidechain": false,
  "promptId": "c21f7a39-88cd-479f-9bae-235f728d85d3",
  "type": "user",
  "uuid": "63953533-2f5e-49e2-b469-9f8c7da3671c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to fetch and summarize the abstracts/key details of three specific arXiv papers. Use WebFetch on the arXiv abstract pages for each. Report what you find for each paper.\n\n1. arXiv:2509.04796 - The reviewer describes it as \"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\" (September 2025). Fetch https://arxiv.org/abs/2509.04796 and report: actual title, authors, abstract, and key findings about recursive synthetic training and factual collapse vs. fluency.\n\n2. arXiv:2111.08851 - Reviewer describes it as a CORAL-loss ordinal regression paper. Fetch https://arxiv.org/abs/2111.08851 and report: actual title, authors, abstract, and what ordinal regression method it introduces.\n\n3. arXiv:1901.07884 - Original CORAL paper. Fetch https://arxiv.org/abs/1901.07884 and report: actual title, authors, and what ordinal regression method it introduces.\n\nReport findings accurately — I need to verify these citations are correct before using them in a research paper revision.",
    "agentId": "a00f2ecaa7a776582",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Citation Verification Report\n\nHere are the verified details for all three papers:\n\n### 1. arXiv:2509.04796 - Knowledge Collapse in LLMs\n\n**Actual Title:** \"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\"\n\n**Authors:** Figarri Keisha, Zekun Wu, Ze Wang, Adriano Koshiyama, Philip Treleaven\n\n**Abstract:** The paper investigates knowledge collapse when language models train repeatedly on synthetic data they generate themselves. It identifies a phenomenon where factual accuracy deteriorates while surface-level writing quality (fluency) remains intact, producing \"confidently wrong\" outputs.\n\n**Key Findings:**\n- Follows a three-stage degradation pattern where models maintain fluent output while factual accuracy erodes\n- The collapse is instruction-dependent (conditional on formatting) rather than uniform\n- Domain-specific synthetic training mitigates the problem while maintaining computational efficiency\n- Developed detection framework combining model-level indicators with task-specific metrics\n\n**Citation Status:** ✓ Matches reviewer's description accurately\n\n---\n\n### 2. arXiv:2111.08851 - Ordinal Regression Paper\n\n**Actual Title:** \"Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities\"\n\n**Authors:** Xintong Shi, Wenzhi Cao, Sebastian Raschka\n\n**Abstract:** Proposes CORN (Conditional Ordinal Regression Network) for ordinal regression in deep neural networks using conditional probability distributions and the chain rule during training.\n\n**Method Introduced:** CORN (Conditional Ordinal Regression Network) - improves upon CORAL by eliminating its weight-sharing constraint in the output layer, enhancing network expressiveness. Architecture-agnostic and compatible with any deep neural network classifier.\n\n**Citation Status:** ⚠ **CAUTION** - This is NOT a CORAL-loss paper. It's a CORN paper that builds upon/improves CORAL. The reviewer's description calling it \"a CORAL-loss ordinal regression paper\" appears inaccurate.\n\n---\n\n### 3. arXiv:1901.07884 - Original CORAL Paper\n\n**Actual Title:** \"Rank consistent ordinal regression for neural networks with application to age estimation\"\n\n**Authors:** Wenzhi Cao, Vahid Mirjalili, Sebastian Raschka\n\n**Abstract:** Addresses how standard loss functions fail to capture ordering information. Proposes CORAL (COnsistent RAnk Logits), which transforms ordinal targets into binary classification subtasks while ensuring rank consistency.\n\n**Method Introduced:** CORAL (COnsistent RAnk Logits) - converts ordinal prediction into multiple binary classification problems with theoretical guarantees for rank-monotonicity. Works with any neural network architecture.\n\n**Citation Status:** ✓ Correctly identified as the original CORAL paper\n\n---\n\n### Summary for Your Research\n\n**Papers 1 and 3 are correctly cited.** However, **Paper 2 requires clarification**: It's a CORN paper that improves upon CORAL, not a CORAL-loss paper itself. If you're citing it as a CORAL-related work, make sure your text distinguishes that it proposes CORN as an enhancement, not as CORAL itself."
      }
    ],
    "totalDurationMs": 15846,
    "totalTokens": 17152,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 488,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 14493,
      "output_tokens": 761,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1410
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 488,
          "output_tokens": 761,
          "cache_read_input_tokens": 14493,
          "cache_creation_input_tokens": 1410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1410,
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
      "otherToolCount": 3
    }
  },
  "sourceToolAssistantUUID": "46e69413-8e67-43e2-ae9a-28a61ae8d40b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-09T21:13:41.389Z_

<details><summary>↩ Tool result · `toolu_01GJixFZNfthBf6ExL1M9L1H`</summary>

```text
## Search Results Summary

I've completed searches for papers addressing generational depth scoring and related work on knowledge collapse in LLMs. Here's what I found:

### Direct Relevance to Generational Depth Scoring

**No papers found** that directly address "generational depth scoring" for recursive web corpus decontamination or ordinal generation labeling (Gen0/Gen1/Gen2) of training documents. The specific framing of your work—assigning ordinal depth labels to enable depth-stratified decontamination—does not appear in the literature reviewed.

### Relevant But Distinct Work

**Knowledge Collapse Research (Late 2025-2026):**
- **[2509.04796] "Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training"** — This is new work directly on recursive synthetic training degradation, distinct from the Shumailov Nature 2024 and ICLR 2025 papers you cited. It describes a three-stage collapse phenomenon where accuracy plummets while surface fluency persists.
- **[2510.04226] "Epistemic Diversity and Knowledge Collapse in Large Language Models"** — Another recent work addressing knowledge collapse from an epistemic diversity angle (new beyond what you cited).

These represent significant recent work on the recursive contamination problem but focus on detecting/measuring degradation rather than proactively assigning generation depth to corpus documents.

**Synthetic Data Depth/Scoring Work:**
- Papers on recursive synthetic data generation mention "depth levels" and "complexity scoring" (Google's Simula framework), but these apply depth concepts to the *generation process* itself, not to post-hoc classification of existing corpus documents.

**AI-Generated Text Detection:**
- Recent work (2025-2026) focuses on detecting whether text is AI-generated vs. human-authored (binary or multiclass), not on assigning ordinal generation depth (Gen0/Gen1/Gen2).

### Conclusion

**The novelty claim appears defensible** based on this search. No existing papers explicitly address assigning ordinal generational depth labels to training corpus documents for decontamination purposes. The closest work tackles either:
1. Detecting knowledge collapse effects post-hoc, or
2. Managing depth during synthetic data generation (not corpus classification)

The concept of labeling corpus documents with generation depth for stratified decontamination strategies appears to be novel through May 2026.

---

Sources:
- [Epistemic Diversity and Knowledge Collapse in Large Language Models](https://arxiv.org/abs/2510.04226)
- [Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training](https://arxiv.org/abs/2509.04796)
- [AI-Generated Text Detection: A Comprehensive Review of Active and Passive Approaches](https://www.sciencedirect.com/org/science/article/pii/S1546221826000482)
- [GitHub - awesome-data-contamination: The Paper List on Data Contamination for Large Language Models](https://github.com/lyy1994/awesome-data-contamination)
- [DeTeCtive: Detecting AI-generated Text via Multi-Level Contrastive Learning](https://openreview.net/forum?id=cdTTTJfJe3)
- [AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification](https://arxiv.org/html/2505.11550v1)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39201fbf-6de4-4d36-946a-e674fe552f73",
  "isSidechain": false,
  "promptId": "c21f7a39-88cd-479f-9bae-235f728d85d3",
  "type": "user",
  "uuid": "ee3b0bc8-a5f5-45aa-8ded-8fced788fc17",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm working on a research paper about \"Genealogical Depth Scoring for Recursive Web Corpus Decontamination\" — specifically, assigning ordinal generation depth labels (Gen0=human, Gen1=AI, Gen2=AI-trained-on-AI) to training corpus documents to enable depth-stratified decontamination. The claim is this is novel with no competing work through May 2026.\n\nPlease search for any papers that might challenge this novelty claim. Use WebSearch with these queries:\n1. \"generational depth\" \"AI-generated text\" detection 2025 2026\n2. \"recursive synthetic data\" depth scoring classification\n3. \"second generation\" synthetic text detection corpus decontamination\n4. \"multi-generation\" AI text detection ordinal\n\nAlso search for any new work on knowledge collapse in LLMs from late 2025 or 2026 beyond what's cited (Shumailov Nature 2024, Strong Model Collapse ICLR 2025, arXiv:2602.10531).\n\nReport any papers found that directly address generational depth assignment to text documents. Be specific about what you find.",
    "agentId": "ae69b0fbfdcc10a7f",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Search Results Summary\n\nI've completed searches for papers addressing generational depth scoring and related work on knowledge collapse in LLMs. Here's what I found:\n\n### Direct Relevance to Generational Depth Scoring\n\n**No papers found** that directly address \"generational depth scoring\" for recursive web corpus decontamination or ordinal generation labeling (Gen0/Gen1/Gen2) of training documents. The specific framing of your work—assigning ordinal depth labels to enable depth-stratified decontamination—does not appear in the literature reviewed.\n\n### Relevant But Distinct Work\n\n**Knowledge Collapse Research (Late 2025-2026):**\n- **[2509.04796] \"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\"** — This is new work directly on recursive synthetic training degradation, distinct from the Shumailov Nature 2024 and ICLR 2025 papers you cited. It describes a three-stage collapse phenomenon where accuracy plummets while surface fluency persists.\n- **[2510.04226] \"Epistemic Diversity and Knowledge Collapse in Large Language Models\"** — Another recent work addressing knowledge collapse from an epistemic diversity angle (new beyond what you cited).\n\nThese represent significant recent work on the recursive contamination problem but focus on detecting/measuring degradation rather than proactively assigning generation depth to corpus documents.\n\n**Synthetic Data Depth/Scoring Work:**\n- Papers on recursive synthetic data generation mention \"depth levels\" and \"complexity scoring\" (Google's Simula framework), but these apply depth concepts to the *generation process* itself, not to post-hoc classification of existing corpus documents.\n\n**AI-Generated Text Detection:**\n- Recent work (2025-2026) focuses on detecting whether text is AI-generated vs. human-authored (binary or multiclass), not on assigning ordinal generation depth (Gen0/Gen1/Gen2).\n\n### Conclusion\n\n**The novelty claim appears defensible** based on this search. No existing papers explicitly address assigning ordinal generational depth labels to training corpus documents for decontamination purposes. The closest work tackles either:\n1. Detecting knowledge collapse effects post-hoc, or\n2. Managing depth during synthetic data generation (not corpus classification)\n\nThe concept of labeling corpus documents with generation depth for stratified decontamination strategies appears to be novel through May 2026.\n\n---\n\nSources:\n- [Epistemic Diversity and Knowledge Collapse in Large Language Models](https://arxiv.org/abs/2510.04226)\n- [Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training](https://arxiv.org/abs/2509.04796)\n- [AI-Generated Text Detection: A Comprehensive Review of Active and Passive Approaches](https://www.sciencedirect.com/org/science/article/pii/S1546221826000482)\n- [GitHub - awesome-data-contamination: The Paper List on Data Contamination for Large Language Models](https://github.com/lyy1994/awesome-data-contamination)\n- [DeTeCtive: Detecting AI-generated Text via Multi-Level Contrastive Learning](https://openreview.net/forum?id=cdTTTJfJe3)\n- [AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification](https://arxiv.org/html/2505.11550v1)"
      }
    ],
    "totalDurationMs": 21218,
    "totalTokens": 20579,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5287,
      "cache_read_input_tokens": 14472,
      "output_tokens": 813,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5287
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 813,
          "cache_read_input_tokens": 14472,
          "cache_creation_input_tokens": 5287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5287,
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
  "sourceToolAssistantUUID": "39201fbf-6de4-4d36-946a-e674fe552f73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-09 (UTC).**  ## Original idea {   \"title\": \"Genealogical Depth Scoring for Recursive Web Corpus Decontamination\",…",
  "leafUuid": "ee3b0bc8-a5f5-45aa-8ded-8fced788fc17",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generational depth scoring for synthetic text corpus decontamination",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d"
}
```

---

### Assistant

_source line 16 · 2026-05-09T21:14:34.224Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have the key information:

1. **arXiv:2509.04796** - Confirmed as "Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training" - the description matches what the reviewer says. This is a valid citation to add.

2. **arXiv:2111.08851** - This is actually the CORN paper, not CORAL. The reviewer recommended citing it as "CORAL-loss based ordinal regression (arXiv:2111.08851)" but this is actually CORN (Conditional Ordinal Regression Network), which improves upon CORAL by removing the weight-sharing constraint. This is an important distinction.


3. **arXiv:1901.07884** - Confirmed as the original CORAL paper. So there's a mismatch here — the reviewer suggested using CORN but labeled it as CORAL. I need to decide whether to cite the original CORAL paper, use CORN with the correct attribution, or mention both since CORN is the more advanced version for deep networks.

The key issue is that CORN actually removes CORAL's weight-sharing constraint, so if the description mentions shared feature weights with independent bias terms, that's describing CORAL, not CORN. I should cite arXiv:1901.07884 for the correct method, and can optionally reference CORN as an alternative. I need to settle on CORAL since the reviewer's description of "2 binary classifiers with shared feature weights and independently trained bias terms" matches it exactly, and I can mention CORN as an alternative that removes the weight-sharing constraint. The key is being precise about which method I'm actually using and making sure the description aligns with the paper I cite. I found another relevant paper on knowledge collapse that could fit the narrative, but since the reviewer didn't flag it as missing, I'll leave it out to avoid scope creep. Now I'm organizing the three concrete changes needed: clarifying the ordinal regression method with the correct CORAL citation, adding a sentence acknowledging the statistical limitations of the 3-seed evaluation, and including the recent decontamination work in the references. Let me structure the full revision as a JSON update. I'm deciding between citing CORAL (arXiv:1901.07884) or CORN (arXiv:2111.08851) for the ordinal regression implementation. Since CORAL matches the description of using 2 binary classifiers with shared feature weights and independent bias parameters, I'll go with that citation and keep the sentence focused on the actual method being used.

Now I need to make the key revisions to the JSON: adding the CORAL loss specification in the approach section, incorporating the new arXiv:2509.04796 reference in the landscape section, and updating the key references with both papers.

Updating the JSON structure... We're using DeBERTa-v3-large with an ordinal regression head trained via CORAL loss, which decomposes the 3-class problem into two binary classifiers sharing feature weights but with independent bias terms across the joint 1029-dimensional representation. For the secondary null, we're testing whether held-out perplexity remains statistically indistinguishable across the three data composition conditions at fixed corpus size using a paired t-test with α = 0.05 across 3 seeds—though with only 3 seeds and a critical t-value of 4.303, we're primarily powered to detect very large effects (Cohen's d > 2.0), so moderate depth effects like 10–20% perplexity degradation wouldn't be reliably caught, and we'd need larger compute budgets to properly validate such effects. For the landscape, I'm adding a reference to arXiv:2509.04796 on knowledge collapse in LLMs, which shows how fluency can persist while factual accuracy degrades under recursive synthetic training. I found another relevant paper on epistemic diversity and knowledge collapse, but since the reviewer didn't mention it and I want to keep this revision focused and minimal, I'll skip adding it. Now I'll put together the complete JSON for this update.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee3b0bc8-a5f5-45aa-8ded-8fced788fc17",
  "isSidechain": false,
  "requestId": "req_011CasgiiB9Cfaq8Z4zmwDHp",
  "type": "assistant",
  "uuid": "86200b9a-3679-4873-a116-74f76c44679e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QgmR78CjPWEtdVnUh9jL3D",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3884,
      "cache_read_input_tokens": 29379,
      "output_tokens": 14280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14280,
          "cache_read_input_tokens": 29379,
          "cache_creation_input_tokens": 3884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3884
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-09T21:18:48.190Z_

Good. Key findings from research:

1. **arXiv:2509.04796** confirmed: "Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training" — three-stage collapse where fluency persists but factual accuracy collapses, exactly as the reviewer described.

2. **Critical citation correction**: arXiv:2111.08851 is actually **CORN** (Conditional Ordinal Regression Network), not CORAL. CORN *removes* the weight-sharing constraint CORAL uses. The reviewer's recommended sentence ("shared feature weights and independently trained bias terms") describes **CORAL**, which is arXiv:1901.07884. I'll cite the correct paper.

3. **Novelty confirmed**: no competing work on generational depth scoring for corpus decontamination through May 2026.

Decision: **minor revision** — the reviewer is right that three targeted fixes complete the proposal. The stagnation at 3.8 is from sequential issue discovery, not a fundamental framing problem; the idea has solid novelty and the reviewer's tone is definitively positive this round.

```json
{
  "title": "Genealogical Depth Scoring for Recursive Web Corpus Decontamination",
  "change_type": "minor",
  "core_problem": "Current AI-generated text detectors are binary (human vs. AI), but training corpora increasingly contain 'second-generation' synthetic text: AI outputs from models that were themselves trained on AI-generated data. This generational depth is unmeasured and unaddressed by any existing detector. Strong Model Collapse (ICLR 2025) establishes that even non-vanishing fractions (~1%) of synthetic data trigger performance collapse, yet the paper treats all synthetic data equivalently — making no distinction between Gen1 text (one model generation removed from human data) and Gen2+ text (recursively compounded). The depth-dependent contribution to collapse severity is entirely uncharacterized, and no current method can assign a generational depth score to a raw training document. Critically, recent work (arXiv:2605.01647, May 2026) demonstrates a 'Wall of Separation' where AI-AI divergence in character-distribution space is significantly smaller than human-AI divergence — making within-model generational discrimination (Gen1 vs. Gen2 from the same fine-tuned model) a harder detection problem than binary human/AI classification and motivating our use of embedding-space features that target cumulative semantic drift orthogonal to character-level surface signals.",
  "opportunity": "By April 2025, 74.2% of newly created web pages contain some AI-generated text — of which 2.5% are fully AI-generated and 71.7% are human-AI blends, where human content has been AI-revised or AI-assisted (Ahrefs, 900K pages, April 2025). These blended documents may occupy an intermediate 'Gen0.5' depth position between Gen0 and Gen1 that depth scoring can address more precisely than binary detection, and they represent the dominant contamination modality at web scale. Complete decontamination is operationally infeasible — there is not enough uncontaminated human text to replace even the fully AI-generated fraction — shifting the practical research question from 'remove all synthetic data' (impossible at web scale) to 'which synthetic documents to prioritize for removal given a fixed filtering budget.' Depth-stratified decontamination addresses this directly: if Gen2+ documents are disproportionately harmful relative to Gen1 documents, preferential removal of deeper-generation text maximizes collapse mitigation per unit of filtering effort. This claim is explicitly scoped to *severity reduction per filtering budget*, not collapse prevention, and is tested in controlled fixed-total-size depth-composition conditions that isolate the effect of contamination depth from dataset volume — making the causal evidence for the governance claim empirically clean. Strong Model Collapse (ICLR 2025) provides the urgency but not the answer — it shows synthetic data is harmful at any non-vanishing fraction but gives no guidance on whether all synthetic data is equally harmful. Crucially, the paper does not distinguish Gen1 from Gen2 synthetic data at all, leaving the depth-dependent harm gradient completely unmeasured. A depth classifier that enables tiered decontamination — or, if depth discrimination fails, definitively establishes that binary filtering suffices — constitutes a concrete empirical contribution with direct governance impact, aligned with EMNLP 2026's special theme 'New Missions for NLP Research,' which explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance.'",
  "landscape": "Model collapse from recursive synthetic training is established (Shumailov et al., Nature 2024; Strong Model Collapse, ICLR 2025) and the limiting theory predicts collapse at any non-vanishing synthetic fraction. Mitigation via real-data accumulation (arXiv:2404.01413) or verifier-guided retraining (arXiv:2510.16657) is active. arXiv:2602.10531 ('From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources', February 2026) analyzes the statistical dynamics of iterative training on data contaminated with synthetic samples using a mixture-model framework, showing that improvement over collapsed models is possible when sufficient fresh real data is present; it does not assign generational depth labels to documents or propose a depth-stratified filtering method. 'Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training' (arXiv:2509.04796, September 2025) demonstrates a three-stage recursive training phenomenon where surface fluency persists while factual accuracy collapses — producing confidently wrong outputs whose instruction-dependent degradation is not captured by perplexity alone. This finding provides complementary empirical support for depth-stratified decontamination: if factual accuracy collapses faster than perplexity across recursive synthetic training rounds, preferential removal of Gen2+ documents — which have accumulated more recursive compression — targets the generational depths where factual quality is most degraded, offering governance value that held-out perplexity metrics alone understate. arXiv:2509.04796 does not classify documents by generational depth, does not propose a depth-stratified filtering method, and does not control training composition by depth level. Training-side collapse prevention via Truncated Cross-Entropy loss (ForTIFAI, arXiv:2509.08972) selectively ignores high-confidence tokens during training to filter synthetic artifacts — a complementary but orthogonal approach to our upstream corpus-level depth detection: ForTIFAI does not classify documents by generational depth and does not operate pre-training. The closest upstream related work, 'Machine-generated text detection prevents language model collapse' (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025), directly bridges AI-text detection and collapse prevention: it trains encoder-only binary classifiers (evaluating RoBERTa, DeBERTa-v3, and ModernBERT) to distinguish human from AI-generated text, then applies importance resampling — weighting each training document by (1-q(x))^b where q(x) is the classifier's AI-probability score — to up-weight likely human content during recursive training. Experiments across GPT-2 and SmolLM2 (124M–1.7B parameters) demonstrate that binary-classifier-guided resampling prevents collapse and even improves over training on purely human data. Critically, arXiv:2502.15654 treats all AI-generated text as equivalent regardless of generational provenance: importance weights depend only on a single binary human/AI probability, with no distinction between Gen1 text (one fine-tuning cycle removed from human data) and Gen2+ text (recursively compounded). Our work directly addresses this gap: if depth-stratified resampling weights — proportional to estimated generational distance from Gen0 — yield greater collapse-severity reduction per resampled document than flat binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over arXiv:2502.15654's strategy under budget-constrained filtering. The dual null-hypothesis design explicitly covers the scenario where depth discrimination fails (AUC < 0.65), in which case our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant and binary resampling is sufficient — a governance finding with direct practical value. A mathematical framework for how recursive publication compresses text through drift and selection is developed in arXiv:2604.08554 but does not propose a depth classifier. The framework is derived for variable-order n-gram agents and does not address transformer fine-tuning; extension to neural models is an open theoretical question that our experiments probe empirically. AI-generated text detection (arXiv:2303.11156, arXiv:2509.18880) addresses binary classification and reaches AUC ~0.85-0.90 for Gen1 text, uniformly treating all AI-generated text as equivalent regardless of generational provenance. Embedding-based representations show intrinsic separability between AI-generated and human text in compressed embedding spaces (arXiv:2408.10437), motivating our use of embedding-space distance features alongside surface-level signals. 'Understanding Transformers via N-gram Statistics' (arXiv:2407.12034, NeurIPS 2024) provides empirical motivation for applying n-gram-derived theoretical predictions to transformer fine-tuning: transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions across TinyStories and Wikipedia, suggesting transformer distributional behavior closely approximates n-gram statistics at the local prediction level — supporting our hypothesis that the monotonic drift prediction of arXiv:2604.08554 (derived for n-gram agents) extends to transformer fine-tuning at the distributional level, with our experiments constituting a direct empirical test of this generalization. 'Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection' (arXiv:2605.01647, May 2026) introduces the Letter Distribution Score (LD-Score) and establishes a 'Wall of Separation' where human-AI divergence significantly exceeds AI-AI divergence in character-distribution space — with the direct implication that within-model generational divergence (Gen1 vs. Gen2 from the same fine-tuned 0.6B model) is smaller still than cross-model AI-AI divergence. This finding validates our architectural choice to prioritize embedding-space features over character-distribution proxies: our mean cosine distance from Gen0 centroid and within-document embedding variance operate in a representation space where cumulative semantic drift — predicted to accumulate monotonically by arXiv:2604.08554's recursive drift-selection framework — may remain detectable even when surface and character-level signals converge. The pre-specified AUC threshold (0.65) and dual null-hypothesis pivot design explicitly account for the scenario where depth discrimination fails at the document level despite embedding-space features. No paper in the contamination detection surveys (arXiv:2502.14425, arXiv:2406.04244) addresses generation depth as a variable. The closest concurrent work — 'Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models' (arXiv:2511.17602, Nov 2025) — asks whether synthetic data overlaps with evaluation benchmarks, not how many generative cycles deep a document is; generational ancestry is orthogonal to benchmark overlap. 'Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training?' (TrainProVe, CVPR 2025, arXiv:2503.09122) achieves >99% accuracy verifying which text-to-image model generated a given image, using model access and generalization error bounds — differentiation is sharp: TrainProVe operates in the image domain and requires model weights access, while our method operates on raw text documents with no model access, enabling upstream corpus-level pre-filtering. Both address data governance but via entirely complementary mechanisms. 'A Closer Look at Model Collapse' (arXiv:2509.16499, NeurIPS 2025 Spotlight) identifies a generalization-to-memorization transition but studies diffusion models and does not distinguish depth levels in training data.",
  "approach": "We build a controlled genealogical corpus by running a 2-step recursive train-generate loop with Qwen3-0.6B (the smallest Qwen3 model, chosen to minimize sequential compute cost while still exhibiting measurable distributional drift per generation), producing text with verified depth labels Gen0 (human, sourced from FineWeb-Edu and C4), Gen1, and Gen2, yielding ~200K labeled documents per depth level across diverse domains. All generated documents are hard-capped at 512 tokens maximum length: this cap is enforced at generation time via the `max_new_tokens=512` parameter, making generation time deterministic and reviewable. At 200K documents × 512 tokens = 102M tokens per generational step, batched A100 inference at 3,000–5,000 tok/s for Qwen3-0.6B yields approximately 6–9 GPU hours per step — consistent with the timeline estimate below. The 512-token cap is scientifically defensible for depth discrimination: surface-level signals (surprisal burstiness, lexical diversity, n-gram entropy) and embedding-space signals (mean cosine distance from Gen0 centroid, within-document window embedding variance) are fully computable over 512-token documents, and ordinal regression classifiers trained on short-document depth signals are directly comparable to the binary detectors in arXiv:2502.15654, which also operate on variable-length web documents.\n\nWe disable Qwen3-0.6B thinking mode during all generative steps via the hard switch `enable_thinking=False` in `tokenizer.apply_chat_template`, rather than the soft `/no_think` instruction tag — because GitHub discussion QwenLM/Qwen3 #1329 documents that the 0.6B model lacks sufficient instruction-following capacity to reliably honor `/no_think` when placed in the system prompt, and silent failure would inject `&lt;think>…&lt;/think>` reasoning traces into Gen1/Gen2 documents that are absent from Gen0 human text, making depth levels trivially separable by token-level artifacts rather than genuine semantic drift and invalidating the AUC signal. The `enable_thinking=False` hard switch operates at the tokenizer template level and does not depend on the model's instruction-following capacity. As a final post-hoc verification, every generated document is scanned for `&lt;think>` tokens and discarded if any are found, before corpus inclusion.\n\nLimiting to Gen0/Gen1/Gen2 compresses the sequential corpus construction bottleneck to approximately 2 wallclock days: Qwen3-0.6B fine-tuning on a 200K-document sample runs in ~4-6 GPU hours on A100, and generation of 200K new 512-token documents runs in ~6-9 GPU hours, for ~12-15 GPU hours per generational step. The hard sequential dependency spans only 2 steps.\n\nWe train a DeBERTa-v3-large ordinal regression classifier jointly on raw text and depth-diagnostic features spanning two categories: (a) surface-level signals — per-token surprisal variance (burstiness), lexical diversity decay (MTLD and type-token ratio), and n-gram entropy compression ratio; and (b) embedding-space signals — (i) mean cosine distance of within-document window embeddings from the pre-computed Gen0 centroid (capturing average depth of embedding drift from human text), and (ii) variance of per-window cosine distances from the Gen0 centroid within the document (capturing within-document heterogeneity of embedding drift). Both embedding features are computed from non-overlapping 128-token window embeddings produced by sentence-transformers/all-MiniLM-L6-v2; feature (i) measures central tendency and feature (ii) measures distributional spread — distinct geometric properties: a Gen2 document may exhibit both higher mean distance from Gen0 and more heterogeneous window-level drift than a Gen1 document, as cumulative generational compression produces uneven semantic displacement within a document. We integrate these five scalar depth-diagnostic features by concatenating them to the DeBERTa-v3-large CLS token representation (1024-dim), then training an ordinal regression head over this joint 1029-dim representation; the Gen0 embedding centroid is precomputed offline from a held-out Gen0 reference set of 10K documents using sentence-transformers/all-MiniLM-L6-v2 and is not updated during classifier training. We implement the ordinal regression head using CORAL loss (arXiv:1901.07884), decomposing the 3-class ordinal problem into 2 binary classifiers with shared feature weights and independently trained bias parameters over the 1029-dim joint representation — a rank-consistent formulation that guarantees monotone probability predictions across the Gen0 < Gen1 < Gen2 ordering.\n\nEmbedding-space features are specifically motivated by the 'Wall of Separation' established in arXiv:2605.01647 (May 2026): AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence (Gen1→Gen2 from the same fine-tuned 0.6B model) is smaller still. Surface-level and character-distribution signals are therefore unlikely to reliably discriminate depth levels in this setting; our mean cosine distance from Gen0 centroid and within-document embedding variance instead target cumulative semantic drift that arXiv:2604.08554's recursive drift-selection framework predicts to accumulate monotonically across generations even when character distributions plateau — providing detection signal orthogonal to surface proxies. The argument is: our embedding-space features target cumulative semantic drift that persists even when surface divergence converges, consistent with the monotonic drift predicted by arXiv:2604.08554 — with the explicit caveat that arXiv:2604.08554 derives this prediction for variable-order n-gram agents, not transformer fine-tuning. We hypothesize the generalization holds because transformer next-token distributions closely approximate n-gram statistics at the local prediction level (arXiv:2407.12034, NeurIPS 2024, reports 68–79% agreement between transformer predictions and n-gram rulesets across two corpora), suggesting transformer fine-tuning implicitly performs distributional compression analogous to n-gram compression, for which cumulative drift is expected to accumulate monotonically. Our classifier and collapse experiments directly test whether this hypothesized generalization from n-gram theory to transformer practice holds empirically.\n\nCentral technical risk and dual null-hypothesis design: We pre-specify two complementary pre-registered outcome scenarios to ensure a definitive, interpretable empirical finding under all classifier and collapse experiment outcomes. (Primary null) If the ordinal classifier falls below AUC 0.65 on Gen1/Gen2 discrimination, the finding is publishable: depth beyond Gen1 is linguistically indistinguishable at the document level using current text-level and embedding-level methods, implying binary filtering suffices — consistent with the implicit assumption of arXiv:2502.15654. In this case, the collapse validation experiments automatically pivot to directly comparing binary (Gen0-only) filtering against depth-stratified filtering at fixed corpus size. (Secondary null) If the classifier achieves AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between conditions (b) (100K Gen0 + 100K Gen1) and (c) (67K Gen0 + 67K Gen1 + 66K Gen2) at fixed total corpus size (paired t-test, α = 0.05, across 3 random seeds), we report this as a distinct secondary null outcome: depth detection is feasible but equal-fraction Gen2 contamination causes no additional collapse-severity beyond equal-fraction Gen1 contamination at GPT-2 scale — the marginal harm-per-generation curve is flat at this model size, binary filtering is sufficient for practical governance at small scales, and preferential Gen2 removal yields no measurable advantage at this scale. We note that with 3 seeds the secondary null test (paired t-test, df=2, critical t=4.303) is powered primarily to detect large effect sizes (Cohen's d > 2.0); moderate depth effects such as 10–20% worse perplexity would not be reliably detected at this seed count, and non-rejection does not rule out such moderate effects — higher-powered validation at larger compute budgets is explicitly reserved as future work. This finding has direct governance implications while leaving open whether depth stratification provides additional value at larger model scales, explicitly reserved as future work. All four logical combinations of (AUC pass/fail) × (collapse severity parity/non-parity) produce pre-specified, interpretable empirical contributions with distinct governance implications.\n\nThe trained classifier is applied zero-shot to real FineWeb and C4 slices to estimate depth-distribution statistics of existing pretraining corpora. Collapse validation uses a GPT-2-scale LM fine-tuned on three fixed-total-size depth-composition conditions (200K training documents each), following the controlled-composition standard of Strong Model Collapse (ICLR 2025): (a) Gen0-only: 200K Gen0; (b) Gen0+Gen1: 100K Gen0 + 100K Gen1; (c) Gen0+Gen1+Gen2: 67K Gen0 + 67K Gen1 + 66K Gen2. These corpora are constructed by subsampling from the already-generated 200K-document pools at each depth level, requiring no additional generation compute. Fixing total corpus size at 200K across all three conditions isolates the causal effect of depth composition from dataset volume: any observed collapse severity difference between conditions reflects contamination depth, not training set size — making the central governance claim ('Gen2 contamination is more harmful per document than Gen1 at equal contamination rate') empirically defensible. Collapse severity is tracked via held-out human-text perplexity and output tail entropy across multiple recursive training generations, explicitly scoped to measuring *severity as a function of depth composition at fixed scale* rather than collapse prevention — consistent with Strong Model Collapse's any-fraction harm finding. GenDepth-Bench is scoped to 2 model families: Qwen3-0.6B (primary) and Llama-3.2-1B (secondary, run through the same recursive loop to test cross-model generalizability of depth signals, explicitly optional — executed only if compute budget permits; see resource estimate). Coverage of 5+ model families is explicitly reserved as future work.\n\n16-Day Critical Path (EMNLP 2026 ARR deadline May 25, 2026; today May 9, 2026):\n— Days 1-2: Environment setup; sample 200K Gen0 docs from FineWeb-Edu/C4 (truncated to 512 tokens); prepare evaluation suite and draft intro/related-work sections.\n— Days 2-3 (sequential bottleneck step 1): Fine-tune Qwen3-0.6B on Gen0 (~4-6h GPU); generate 200K Gen1 documents at max 512 tokens each (~6-9h GPU; 200K × 512 tokens = 102M tokens ÷ 3,000–5,000 tok/s ≈ 6–9h) with `enable_thinking=False` hard switch and post-hoc `&lt;think>` token scan.\n— Days 3-4 (sequential bottleneck step 2): Fine-tune Qwen3-0.6B-v2 on Gen1 (~4-6h GPU); generate 200K Gen2 documents at max 512 tokens each (~6-9h GPU) with same thinking-mode controls.\n— Days 3-8 (PARALLEL TRACK A): DeBERTa-v3-large ordinal training begins with Gen0+Gen1 data at Day 3; adds Gen2 data when available at Day 5; ablations over surface vs. embedding feature subsets.\n— Days 5-10 (PARALLEL TRACK B): GPT-2-scale collapse experiments begin at Day 5 with fixed-size conditions (a) Gen0-only: 200K Gen0 and (b) Gen0+Gen1: 100K Gen0+100K Gen1 (subsampled from existing pools); add condition (c) Gen0+Gen1+Gen2: 67K each at Day 6 when Gen2 corpus is available. Llama-3.2-1B recursive corpus generation runs in parallel if compute budget is below 160h H100-equivalent at Day 5.\n— Days 7-9: Full classifier evaluation; if Gen1/Gen2 AUC < 0.65, activate primary null-hypothesis binary filtering comparison experiments; if AUC ≥ 0.65 but collapse severity parity detected between conditions (b) and (c), record secondary null outcome and report governance implications.\n— Days 9-10: Zero-shot depth scoring on real FineWeb/C4 slices.\n— Days 10-12: Feature importance ablations; cross-model generalizability check on Llama-3.2-1B-generated corpus (if optional Llama recursive corpus was generated).\n— Days 12-16: Analysis, writing, revision, and submission.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~210h A100 (40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B, each step generating 200K documents at 512 tokens max = 102M tokens ÷ ~3,500 tok/s average ≈ ~8h per step, ×2 steps = ~16h generation + ~24h fine-tuning over 2 steps + 50h DeBERTa-v3-large fine-tuning and ablations + 120h GPT-2-scale collapse validation experiments across 3 fixed-size depth-composition conditions)",
      "gpu_utilization": "High idle rate (~40-60%): GPU waits while researcher designs experiment configs, interprets collapse curves, debugs depth signal quality, and writes between each stage over several months",
      "timeline": "4-6 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$370 at $1.75/h blended A100 average (RunPod ~$1.49/h, Lambda ~$2.06/h); approximately 70 H100-equivalent hours"
    },
    "human_in_loop": {
      "gpu_hours": "~320h A100 (agent handles training loop queuing and ablation scheduling; human approves depth-feature selection, collapse experiment design, AUC threshold decision for null-hypothesis activation, and Llama-3.2-1B second-family validation)",
      "gpu_utilization": "Moderate idle rate (~15-25%): agent queues overnight runs and fills GPU gaps between sequential generational steps; handles parallel DeBERTa and collapse experiment scheduling",
      "timeline": "6-10 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$60-120 (~600-800 agent turns at $0.08-0.15/turn for experiment design, result interpretation, and iteration guidance)",
      "estimated_gpu_cost": "~$560 at $1.75/h average A100; approximately 107 H100-equivalent hours",
      "risk_note": "Key bottleneck: 2-step sequential corpus construction (train on GenN → generate GenN+1 at 512 tokens max → train again) cannot be parallelized; each step adds ~1 wallclock day with Qwen3-0.6B. The 512-token document cap makes generation time deterministic: 200K × 512 tokens = 102M tokens ÷ 3,000–5,000 tok/s ≈ 6–9h per step, matching the timeline estimate and eliminating schedule uncertainty from variable document lengths. Corpus construction for collapse experiments uses fixed-total-size subsampling (200K per condition) from the already-generated per-depth pools — no additional generation compute required. Pre-specified dual null-hypothesis design (primary: AUC < 0.65; secondary: AUC ≥ 0.65 but collapse severity parity between fixed-size conditions (b) and (c)) means the agent has clear decision rules without requiring researcher judgment to pivot, covering all four logical outcome combinations."
    },
    "auto_research": {
      "gpu_hours": "~490h A100 / ~163h H100-equivalent hours (mandatory, within ≤200h hard constraint): 40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B (200K documents × 512 tokens max per step = 102M tokens; at 3,000–5,000 tok/s ≈ 6–9h generation per step, ×2 steps; plus ~12h fine-tuning per step = ~40h total) + 120h DeBERTa-v3-large fine-tuning and ablations with 2x hyperparameter search across depth-feature combinations (surface-only, embedding-only, combined) + 240h GPT-2-scale collapse validation experiments across 3 fixed-total-size depth-composition conditions (Qwen3-0.6B family) with 3 collapse metrics + 90h auxiliary ablations (feature importance, zero-shot FineWeb/C4 scoring, null-hypothesis binary filtering comparison if AUC threshold triggered). Llama-3.2-1B recursive corpus generation and collapse experiments (~60-90h A100 / ~20-30h H100-equivalent) are explicitly optional from the start: executed only if compute budget remains below 160h H100-equivalent at Day 10; otherwise deprioritized to zero-shot depth scoring only, maintaining a genuine 40h safety buffer against the 200h hard ceiling.",
      "gpu_utilization": "Near-zero idle (<5%): agent queues hyperparameter sweeps and ablations 24/7, filling GPU cycles between sequential generational construction steps with parallel auxiliary experiments",
      "timeline": "13-16 days with 4-6 concurrent A100s",
      "team": "0 (4-6h one-time setup: genealogical corpus schema with 512-token document cap, experiment grid, AUC threshold 0.65 for primary null-hypothesis activation, paired t-test criterion for secondary null-hypothesis activation between fixed-size conditions (b) and (c), stopping conditions)",
      "claude_api_cost": "$250-400 (~2500-3000 agent turns for experiment orchestration, result analysis, and adaptive exploration)",
      "estimated_gpu_cost": "~$856 at $1.75/h average A100 (mandatory only); ~$960 including optional Llama-3.2-1B corpus if budget permits",
      "speed_bottleneck": "2-step sequential corpus construction is the hard wallclock floor; the 512-token document cap makes per-step generation time deterministic at ~6-9h (102M tokens ÷ 3,000–5,000 tok/s), eliminating schedule uncertainty; GPU count limits simultaneous ablation breadth during non-sequential phases",
      "risk_note": "Corpus construction for collapse experiments uses fixed-total-size subsampling (200K per condition from already-generated per-depth pools) — no additional generation compute. Depth signal may be weak between Gen1 and Gen2 from the same small model — a risk compounded by the 'Wall of Separation' finding (arXiv:2605.01647): AI-AI surface divergence is substantially smaller than human-AI divergence, making within-model generational discrimination harder still. Pre-specified dual null-hypothesis design covers all outcomes: primary null (AUC < 0.65) redirects to binary filtering comparison at fixed corpus size; secondary null (AUC ≥ 0.65 but collapse severity parity between fixed-size conditions (b) and (c)) reports depth detection as feasible but equal-fraction Gen2 contamination as causing no incremental governance harm beyond Gen1 at GPT-2 scale. Embedding-space features (mean cosine distance from Gen0 centroid and within-document embedding variance over 128-token windows) partially mitigate the primary null risk by targeting cumulative semantic drift invisible at the surface level. Budget contingency: Llama-3.2-1B recursive corpus generation is explicitly optional from the start; if compute approaches 160h H100-equivalent during execution, Llama-3.2-1B recursive corpus is deprioritized to zero-shot depth scoring only (no new collapse experiments), saving ~60-90h A100 (~20-30h H100-equivalent) and maintaining a genuine 40h buffer against the 200h hard ceiling."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; special theme 'New Missions for NLP Research' explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance' — near-perfect topical alignment; conference October 24-29, Budapest)",
    "NAACL 2027 (ARR cycle deadline TBD, expected ~late 2026; safe backup with more time for thorough collapse validation experiments and additional model families)"
  ],
  "level": "solid",
  "key_references": [
    "AI models collapse when trained on recursively generated data (Nature 2024)",
    "Strong Model Collapse (ICLR 2025) — establishes collapse at any non-vanishing synthetic fraction (~1% example); holds total corpus size fixed while varying synthetic fraction (the controlled design our collapse experiments follow); does not distinguish Gen1 from Gen2 synthetic data; this gap is what we fill",
    "Machine-generated text detection prevents language model collapse (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025) — closest upstream prior work: trains binary encoder-only classifiers (evaluating RoBERTa, DeBERTa-v3, ModernBERT) with importance resampling — weights ∝ (1-q(x))^b — to prevent collapse at GPT-2/SmolLM2 scale (124M–1.7B parameters); treats all AI-generated text equivalently without generational depth distinction; our work directly extends this: if depth-stratified resampling weights yield greater collapse-severity reduction per decontamination unit than binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over binary resampling under budget constraints; if not (AUC < 0.65 or collapse severity parity between fixed-size conditions (b) and (c)), our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant",
    "From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources (arXiv:2602.10531, February 2026) — analyzes the statistical dynamics of iterative training on contaminated data using a mixture-model framework, showing that improvement over collapsed models is possible when sufficient fresh real data is present; does not assign generational depth labels to documents or propose a depth-stratified filtering method",
    "Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training (arXiv:2509.04796, September 2025) — demonstrates three-stage recursive training phenomenon where surface fluency persists while factual accuracy collapses; motivates depth-stratified decontamination as a mechanism to preferentially remove documents at generational depths where factual quality is most degraded; does not classify documents by generational depth or propose a depth-stratified filtering method",
    "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (arXiv:2404.01413)",
    "Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence (arXiv:2510.16657)",
    "ForTIFAI: Fending Off Recursive Training Induced Failure for AI Models (arXiv:2509.08972) — training-side collapse prevention via Truncated Cross-Entropy loss; orthogonal to our upstream corpus-level depth detection; does not classify documents by generational depth",
    "Drift and Selection in LLM Text Ecosystems (arXiv:2604.08554) — mathematical framework for how recursive publication compresses text through drift and selection; derived for variable-order n-gram agents (not transformer fine-tuning); does not propose a depth classifier or detection method; motivates our prediction that embedding-space drift accumulates monotonically across generations even when surface distributions plateau, under the hypothesis that transformer fine-tuning implicitly performs distributional compression analogous to n-gram compression — a generalization our experiments directly test",
    "Understanding Transformers via N-gram Statistics (arXiv:2407.12034, NeurIPS 2024) — transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions across TinyStories and Wikipedia; provides empirical grounding for our hypothesis that the monotonic drift prediction of arXiv:2604.08554 (derived for n-gram agents) extends to transformer fine-tuning at the distributional level",
    "Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection (arXiv:2605.01647, May 2026) — establishes 'Wall of Separation' where human-AI divergence significantly exceeds AI-AI divergence in character-distribution space; within-model generational gap (Gen1→Gen2 from same fine-tuned model) is smaller still; directly threatens surface-level discriminability; our counter-argument: embedding-space features (mean cosine distance from Gen0 centroid and within-document window embedding variance, computed over non-overlapping 128-token windows via sentence-transformers/all-MiniLM-L6-v2) target cumulative semantic drift orthogonal to character-distribution signals; the pre-specified dual null-hypothesis design accounts for the possibility that depth discrimination fails despite embedding-space features",
    "Rank consistent ordinal regression for neural networks with application to age estimation (CORAL, arXiv:1901.07884, Cao et al.) — introduces CORAL loss for rank-consistent ordinal regression, decomposing the K-class ordinal problem into K-1 binary classifiers with shared feature weights and independently trained bias parameters; the ordinal regression head implementation used in this work",
    "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective (NeurIPS 2025 Spotlight)",
    "RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (ACL 2024)",
    "Can AI-Generated Text be Reliably Detected? (arXiv:2303.11156)",
    "Diversity Boosts AI-Generated Text Detection (arXiv:2509.18880)",
    "Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models (arXiv:2511.17602) — asks whether synthetic data overlaps with evaluation benchmarks; generational ancestry is orthogonal to benchmark overlap",
    "Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training? (TrainProVe, CVPR 2025, arXiv:2503.09122) — achieves >99% accuracy in image domain using model access and generalization error bounds; differentiation: our method operates on raw text with no model access, enabling upstream corpus-level pre-filtering; different modality and mechanism address the same governance goal",
    "Understanding Generative AI Content with Embedding Models (arXiv:2408.10437) — demonstrates intrinsic separability of AI-generated and human text in compressed embedding space; motivates our use of embedding-space cosine distance and within-document variance features for depth discrimination beyond surface-level signals",
    "Benchmark Data Contamination of Large Language Models: A Survey (arXiv:2406.04244)",
    "A Survey on Data Contamination for Large Language Models (arXiv:2502.14425)"
  ],
  "description": "As web corpora become saturated with AI-generated content (74.2% of new web pages contain some AI text by April 2025, of which 2.5% are fully AI-generated and 71.7% are human-AI blends; Ahrefs, 900K pages), complete decontamination is operationally infeasible, shifting the question to: which synthetic documents cause the most harm and should be removed first? We propose Genealogical Depth Scoring, a method extending binary AI-text detection to ordinal depth classification (Gen0=human, Gen1, Gen2), trained on a controlled corpus produced by 2-step recursive train-generate loops using Qwen3-0.6B with thinking mode disabled via the hard switch `enable_thinking=False` in `tokenizer.apply_chat_template` — rather than the soft `/no_think` instruction tag, which silently fails for the 0.6B model when placed in the system prompt (GitHub QwenLM/Qwen3 discussion #1329) and would introduce `&lt;think>…&lt;/think>` artifacts that make depth levels trivially separable by token-level signals rather than genuine semantic drift — with post-hoc discard of any documents containing `&lt;think>` tokens before corpus inclusion. All generated documents are hard-capped at 512 tokens via `max_new_tokens=512`, yielding 200K × 512 tokens = 102M tokens per generational step; at 3,000–5,000 tok/s for Qwen3-0.6B on A100 this takes approximately 6–9 GPU hours per step, making the generation timeline deterministic and anchored to a verifiable arithmetic bound. The classifier combines DeBERTa-v3-large fine-tuning with two classes of depth-diagnostic features: surface-level signals (surprisal burstiness, lexical diversity decay, n-gram entropy compression ratio) and embedding-space signals — (i) mean cosine distance of within-document window embeddings from the Gen0 centroid, and (ii) variance of per-window cosine distances from the Gen0 centroid within the document, both computed over non-overlapping 128-token windows via sentence-transformers/all-MiniLM-L6-v2. Feature (i) captures average drift from human text in embedding space; feature (ii) captures within-document heterogeneity of that drift — distinct geometric properties (central tendency vs. distributional spread) that together characterize the document's depth signature. These five scalar features are concatenated to the DeBERTa-v3-large CLS token representation (1024-dim) and passed to an ordinal regression head trained over the joint 1029-dim representation; we implement the head using CORAL loss (arXiv:1901.07884), decomposing the 3-class ordinal problem into 2 binary classifiers with shared feature weights and independently trained bias parameters — a rank-consistent formulation guaranteeing monotone probability predictions across the Gen0 < Gen1 < Gen2 ordering. The Gen0 centroid is precomputed offline and not updated during training. The embedding-space features directly address the 'Wall of Separation' documented in arXiv:2605.01647 (May 2026) — AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence is smaller still — by targeting cumulative semantic drift that arXiv:2604.08554 predicts to accumulate monotonically across recursive generations even when surface statistics plateau. Because arXiv:2604.08554 derives this prediction for variable-order n-gram agents rather than transformer fine-tuning, we ground the generalization in arXiv:2407.12034 (NeurIPS 2024), which shows transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions, and treat our classifier and collapse experiments as a direct empirical test of whether this theoretical extension holds. arXiv:2509.04796 (September 2025) additionally shows that factual accuracy collapses faster than perplexity under recursive synthetic training, providing complementary motivation: depth-stratified decontamination preferentially removes documents at generational depths where factual quality is most degraded, offering governance value that perplexity metrics alone understate. We pre-specify a dual null-hypothesis design: (primary null) if Gen1/Gen2 AUC < 0.65, depth is linguistically indistinguishable and binary filtering suffices; (secondary null) if AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between fixed-size conditions (b) (100K Gen0 + 100K Gen1) and (c) (67K Gen0 + 67K Gen1 + 66K Gen2) — noting that with 3 seeds (paired t-test, df=2, critical t=4.303) the test is powered primarily to detect large effect sizes and non-rejection does not rule out moderate depth effects — equal-fraction Gen2 contamination causes no additional collapse-severity beyond equal-fraction Gen1 contamination at GPT-2 scale, leaving depth stratification's incremental value at larger scales as future work. All four logical outcomes produce pre-specified, interpretable empirical contributions. Collapse validation compares three fixed-total-size depth-composition conditions (200K documents each: (a) Gen0-only; (b) 100K Gen0+100K Gen1; (c) 67K Gen0+67K Gen1+66K Gen2), constructed by subsampling from the already-generated 200K-document pools at each depth level — no additional generation compute. Fixing total corpus size across all conditions isolates the causal effect of depth composition from dataset volume, making the central governance claim ('Gen2 contamination is more harmful per document than Gen1 at equal contamination rate, supporting preferential Gen2 removal per filtering unit') empirically defensible. TrainProVe (CVPR 2025) addresses related governance goals via model access in the image domain; ForTIFAI (arXiv:2509.08972) prevents collapse at training time via modified loss; arXiv:2502.15654 (Feb 2025) prevents collapse via binary detection with importance resampling but treats all AI text equivalently without generational depth distinction; arXiv:2602.10531 (Feb 2026) analyzes collapse dynamics statistically via mixture models but does not classify text by generational depth — our work is the first to assign generational depth scores to raw text corpus documents upstream of training, and directly tests whether depth-stratified resampling yields greater collapse-severity reduction per filtering unit than binary resampling. We release GenDepth-Bench covering 2 model families (Qwen3-0.6B primary; Llama-3.2-1B secondary, optional pending compute budget), with 5+ family coverage as explicit future work. Targets EMNLP 2026's special theme on synthetic data feedback loops and data governance.",
  "project_name": "gen_depth_decontam",
  "source": "web_research"
}
```

---

**Summary of changes (minor revision):**

Three targeted fixes, zero experimental changes:

1. **Ordinal regression specified** — Added one sentence in `approach` and `description` naming CORAL loss (arXiv:1901.07884) as the implementation, with the rank-consistency guarantee. **Correction from reviewer**: the reviewer pointed to arXiv:2111.08851 (which is actually CORN, not CORAL — it *removes* the weight-sharing constraint). Since the desired architecture ("shared feature weights, independently trained bias terms") matches CORAL exactly, I cite arXiv:1901.07884 and added it to `key_references`.

2. **Statistical power acknowledged** — Added one sentence to the secondary null section: with 3 seeds (df=2, critical t=4.303), the test is powered for large effect sizes only; moderate effects are not ruled out by non-rejection; higher-powered validation reserved as future work. This converts the reviewer attack surface into a transparent limitation.

3. **arXiv:2509.04796 added** — Added to `landscape` with a full differentiation paragraph (motivates depth stratification as targeting generational depths where factual quality degrades, complementary to perplexity-based tracking; does not classify by depth or propose filtering), added to `key_references`, and referenced in `description`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86200b9a-3679-4873-a116-74f76c44679e",
  "isSidechain": false,
  "requestId": "req_011CasgiiB9Cfaq8Z4zmwDHp",
  "type": "assistant",
  "uuid": "21751a1a-9175-450d-b30d-dad4d753042f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QgmR78CjPWEtdVnUh9jL3D",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3884,
      "cache_read_input_tokens": 29379,
      "output_tokens": 14280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14280,
          "cache_read_input_tokens": 29379,
          "cache_creation_input_tokens": 3884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3884
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-09 (UTC).**  ## Original idea {   \"title\": \"Genealogical Depth Scoring for Recursive Web Corpus Decontamination\",…",
  "leafUuid": "21751a1a-9175-450d-b30d-dad4d753042f",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Generational depth scoring for synthetic text corpus decontamination",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-09 (UTC).**  ## Original idea {   \"title\": \"Genealogical Depth Scoring for Recursive Web Corpus Decontamination\",…",
  "leafUuid": "21751a1a-9175-450d-b30d-dad4d753042f",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generational depth scoring for synthetic text corpus decontamination",
  "sessionId": "03b3a10b-92bf-4e7e-aee3-dad2ca50626d"
}
```

---
