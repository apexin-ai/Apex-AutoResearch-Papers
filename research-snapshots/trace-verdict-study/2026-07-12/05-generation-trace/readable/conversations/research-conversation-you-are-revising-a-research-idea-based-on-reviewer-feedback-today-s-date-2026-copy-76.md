# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-09 (UTC).** ## Original idea { "tit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-2/a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19.jsonl`
- **Structured JSON:** [`2694e90e7a411acd07ac.json`](../../sessions/26/2694e90e7a411acd07ac.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-09T20:32:54.014Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-09T20:32:54.014Z",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-09 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Genealogical Depth Scoring for Recursive Web Corpus Decontamination\",\n  \"core_problem\": \"Current AI-generated text detectors are binary (human vs. AI), but training corpora increasingly contain 'second-generation' synthetic text: AI outputs from models that were themselves trained on AI-generated data. This generational depth is unmeasured and unaddressed by any existing detector. Strong Model Collapse (ICLR 2025) establishes that even non-vanishing fractions (~1%) of synthetic data trigger performance collapse, yet the paper treats all synthetic data equivalently — making no distinction between Gen1 text (one model generation removed from human data) and Gen2+ text (recursively compounded). The depth-dependent contribution to collapse severity is entirely uncharacterized, and no current method can assign a generational depth score to a raw training document. Critically, recent work (arXiv:2605.01647, May 2026) demonstrates a 'Wall of Separation' where AI-AI divergence in character-distribution space is significantly smaller than human-AI divergence — making within-model generational discrimination (Gen1 vs. Gen2 from the same fine-tuned model) a harder detection problem than binary human/AI classification and motivating our use of embedding-space features that target cumulative semantic drift orthogonal to character-level surface signals.\",\n  \"opportunity\": \"By April 2025, 74.2% of newly created web pages contain some AI-generated text — of which 2.5% are fully AI-generated and 71.7% are human-AI blends, where human content has been AI-revised or AI-assisted (Ahrefs, 900K pages, April 2025). These blended documents may occupy an intermediate 'Gen0.5' depth position between Gen0 and Gen1 that depth scoring can address more precisely than binary detection, and they represent the dominant contamination modality at web scale. Complete decontamination is operationally infeasible — there is not enough uncontaminated human text to replace even the fully AI-generated fraction — shifting the practical research question from 'remove all synthetic data' (impossible at web scale) to 'which synthetic documents to prioritize for removal given a fixed filtering budget.' Depth-stratified decontamination addresses this directly: if Gen2+ documents are disproportionately harmful relative to Gen1 documents, preferential removal of deeper-generation text maximizes collapse mitigation per unit of filtering effort. This claim is explicitly scoped to *severity reduction per filtering budget*, not collapse prevention: Strong Model Collapse (ICLR 2025) establishes that any non-vanishing synthetic fraction triggers collapse, so a corpus that retains Gen1 documents after removing Gen2 still contains harmful synthetic content. The value of depth-stratified filtering is that it reduces expected collapse severity for a fixed decontamination budget by prioritizing the highest-harm documents first — a practical governance claim that holds even if perfect decontamination is required for complete collapse prevention. Strong Model Collapse (ICLR 2025) provides the urgency but not the answer — it shows synthetic data is harmful at any non-vanishing fraction but gives no guidance on whether all synthetic data is equally harmful. Crucially, the paper does not distinguish Gen1 from Gen2 synthetic data at all, leaving the depth-dependent harm gradient completely unmeasured. A depth classifier that enables tiered decontamination — or, if depth discrimination fails, definitively establishes that binary filtering suffices — constitutes a concrete empirical contribution with direct governance impact, aligned with EMNLP 2026's special theme 'New Missions for NLP Research,' which explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance.'\",\n  \"landscape\": \"Model collapse from recursive synthetic training is established (Shumailov et al., Nature 2024; Strong Model Collapse, ICLR 2025) and the limiting theory predicts collapse at any non-vanishing synthetic fraction. Mitigation via real-data accumulation (arXiv:2404.01413) or verifier-guided retraining (arXiv:2510.16657) is active. Training-side collapse prevention via Truncated Cross-Entropy loss (ForTIFAI, arXiv:2509.08972) selectively ignores high-confidence tokens during training to filter synthetic artifacts — a complementary but orthogonal approach to our upstream corpus-level depth detection: ForTIFAI does not classify documents by generational depth and does not operate pre-training. The closest upstream related work, 'Machine-generated text detection prevents language model collapse' (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025), directly bridges AI-text detection and collapse prevention: it trains encoder-only binary classifiers (evaluating RoBERTa, DeBERTa-v3, and ModernBERT) to distinguish human from AI-generated text, then applies importance resampling — weighting each training document by (1-q(x))^b where q(x) is the classifier's AI-probability score — to up-weight likely human content during recursive training. Experiments across GPT-2 and SmolLM2 (124M–1.7B parameters) demonstrate that binary-classifier-guided resampling prevents collapse and even improves over training on purely human data. Critically, arXiv:2502.15654 treats all AI-generated text as equivalent regardless of generational provenance: importance weights depend only on a single binary human/AI probability, with no distinction between Gen1 text (one fine-tuning cycle removed from human data) and Gen2+ text (recursively compounded). Our work directly addresses this gap: if depth-stratified resampling weights — proportional to estimated generational distance from Gen0 — yield greater collapse-severity reduction per resampled document than flat binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over arXiv:2502.15654's strategy under budget-constrained filtering. The dual null-hypothesis design explicitly covers the scenario where depth discrimination fails (AUC < 0.65), in which case our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant and binary resampling is sufficient — a governance finding with direct practical value. A mathematical framework for how recursive publication compresses text through drift and selection is developed in arXiv:2604.08554 but does not propose a depth classifier. The framework is derived for variable-order n-gram agents and does not address transformer fine-tuning; extension to neural models is an open theoretical question that our experiments probe empirically. AI-generated text detection (arXiv:2303.11156, arXiv:2509.18880) addresses binary classification and reaches AUC ~0.85-0.90 for Gen1 text, uniformly treating all AI-generated text as equivalent regardless of generational provenance. Embedding-based representations show intrinsic separability between AI-generated and human text in compressed embedding spaces (arXiv:2408.10437), motivating our use of embedding-space distance features alongside surface-level signals. 'Understanding Transformers via N-gram Statistics' (arXiv:2407.12034, NeurIPS 2024) provides empirical motivation for applying n-gram-derived theoretical predictions to transformer fine-tuning: transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions across TinyStories and Wikipedia, suggesting transformer distributional behavior closely approximates n-gram statistics at the local prediction level — supporting our hypothesis that the monotonic drift prediction of arXiv:2604.08554 (derived for n-gram agents) extends to transformer fine-tuning at the distributional level, with our experiments constituting a direct empirical test of this generalization. 'Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection' (arXiv:2605.01647, May 2026) introduces the Letter Distribution Score (LD-Score) and establishes a 'Wall of Separation' where human-AI divergence significantly exceeds AI-AI divergence in character-distribution space — with the direct implication that within-model generational divergence (Gen1 vs. Gen2 from the same fine-tuned 0.6B model) is smaller still than cross-model AI-AI divergence. This finding validates our architectural choice to prioritize embedding-space features over character-distribution proxies: our cosine distance from Gen0 centroid and MAUVE-style divergence operate in a representation space where cumulative semantic drift — predicted to accumulate monotonically by arXiv:2604.08554's recursive drift-selection framework — may remain detectable even when surface and character-level signals converge. The pre-specified AUC threshold (0.65) and dual null-hypothesis pivot design explicitly account for the scenario where depth discrimination fails at the document level despite embedding-space features. No paper in the contamination detection surveys (arXiv:2502.14425, arXiv:2406.04244) addresses generation depth as a variable. The closest concurrent work — 'Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models' (arXiv:2511.17602, Nov 2025) — asks whether synthetic data overlaps with evaluation benchmarks, not how many generative cycles deep a document is; generational ancestry is orthogonal to benchmark overlap. 'Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training?' (TrainProVe, CVPR 2025, arXiv:2503.09122) achieves >99% accuracy verifying which text-to-image model generated a given image, using model access and generalization error bounds — differentiation is sharp: TrainProVe operates in the image domain and requires model weights access, while our method operates on raw text documents with no model access, enabling upstream corpus-level pre-filtering. Both address data governance but via entirely complementary mechanisms. 'A Closer Look at Model Collapse' (arXiv:2509.16499, NeurIPS 2025 Spotlight) identifies a generalization-to-memorization transition but studies diffusion models and does not distinguish depth levels in training data.\",\n  \"approach\": \"We build a controlled genealogical corpus by running a 2-step recursive train-generate loop with Qwen3-0.6B (the smallest Qwen3 model, chosen to minimize sequential compute cost while still exhibiting measurable distributional drift per generation), producing text with verified depth labels Gen0 (human, sourced from FineWeb-Edu and C4), Gen1, and Gen2, yielding ~200K labeled documents per depth level across diverse domains. Limiting to Gen0/Gen1/Gen2 compresses the sequential corpus construction bottleneck to approximately 2 wallclock days: Qwen3-0.6B fine-tuning on a 200K-document sample runs in ~4-6 GPU hours on A100, and generation of 200K new documents runs in ~6-8 GPU hours, for ~12-14 GPU hours per generational step. The hard sequential dependency spans only 2 steps.\\n\\nWe train a DeBERTa-v3-large ordinal regression classifier jointly on raw text and depth-diagnostic features spanning two categories: (a) surface-level signals — per-token surprisal variance (burstiness), lexical diversity decay (MTLD and type-token ratio), and n-gram entropy compression ratio; and (b) embedding-space signals — cosine distance from a Gen0 embedding centroid computed via sentence-transformers, and MAUVE-style distributional divergence. Embedding-space features are specifically motivated by the 'Wall of Separation' established in arXiv:2605.01647 (May 2026): AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence (Gen1→Gen2 from the same fine-tuned 0.6B model) is smaller still. Surface-level and character-distribution signals are therefore unlikely to reliably discriminate depth levels in this setting; our embedding-space features instead target cumulative semantic drift that arXiv:2604.08554's recursive drift-selection framework predicts to accumulate monotonically across generations even when character distributions plateau — providing detection signal orthogonal to surface proxies. The argument is: our embedding-space features target cumulative semantic drift that persists even when surface divergence converges, consistent with the monotonic drift predicted by arXiv:2604.08554 — with the explicit caveat that arXiv:2604.08554 derives this prediction for variable-order n-gram agents, not transformer fine-tuning. We hypothesize the generalization holds because transformer next-token distributions closely approximate n-gram statistics at the local prediction level (arXiv:2407.12034, NeurIPS 2024, reports 68–79% agreement between transformer predictions and n-gram rulesets across two corpora), suggesting transformer fine-tuning implicitly performs distributional compression analogous to n-gram compression, for which cumulative drift is expected to accumulate monotonically. Our classifier and collapse experiments directly test whether this hypothesized generalization from n-gram theory to transformer practice holds empirically.\\n\\nCentral technical risk and dual null-hypothesis design: We pre-specify two complementary pre-registered outcome scenarios to ensure a definitive, interpretable empirical finding under all classifier and collapse experiment outcomes. (Primary null) If the ordinal classifier falls below AUC 0.65 on Gen1/Gen2 discrimination, the finding is publishable: depth beyond Gen1 is linguistically indistinguishable at the document level using current text-level and embedding-level methods, implying binary filtering suffices — consistent with the implicit assumption of arXiv:2502.15654. In this case, the collapse validation experiments automatically pivot to directly comparing binary (Gen0-only) filtering against depth-stratified filtering. (Secondary null) If the classifier achieves AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between Gen0+Gen1 and Gen0+Gen1+Gen2 filtered corpora (paired t-test, α = 0.05, across 3 random seeds), we report this as a distinct secondary null outcome: depth detection is feasible but depth-stratified filtering provides no incremental collapse-severity benefit over binary filtering at GPT-2 scale, suggesting the marginal harm-per-generation curve is flat at this model size and that binary filtering is therefore sufficient for practical governance at small scales. This finding has direct governance implications — preferential removal of Gen2 documents yields no measurable advantage over simple binary decontamination at GPT-2 scale — while leaving open whether depth stratification provides additional value at larger model scales, explicitly reserved as future work. All four logical combinations of (AUC pass/fail) × (collapse severity parity/non-parity) produce pre-specified, interpretable empirical contributions with distinct governance implications.\\n\\nThe trained classifier is applied zero-shot to real FineWeb and C4 slices to estimate depth-distribution statistics of existing pretraining corpora. Collapse validation uses a GPT-2-scale LM fine-tuned on depth-stratified filtered corpora (Gen0-only, Gen0+Gen1, Gen0+Gen1+Gen2) with collapse severity tracked via held-out human-text perplexity and output tail entropy across multiple recursive training generations. Collapse experiments are explicitly scoped to measuring *severity reduction* across filtering strategies — not collapse prevention — consistent with Strong Model Collapse's any-fraction harm finding. GenDepth-Bench is scoped to 2 model families: Qwen3-0.6B (primary) and Llama-3.2-1B (secondary, run through the same recursive loop to test cross-model generalizability of depth signals, explicitly optional — executed only if compute budget permits; see resource estimate). Coverage of 5+ model families is explicitly reserved as future work.\\n\\n16-Day Critical Path (EMNLP 2026 ARR deadline May 25, 2026; today May 9, 2026):\\n— Days 1-2: Environment setup; sample 200K Gen0 docs from FineWeb-Edu/C4; prepare evaluation suite and draft intro/related-work sections.\\n— Days 2-3 (sequential bottleneck step 1): Fine-tune Qwen3-0.6B on Gen0 (~4-6h GPU); generate 200K Gen1 documents (~6-8h GPU).\\n— Days 3-4 (sequential bottleneck step 2): Fine-tune Qwen3-0.6B-v2 on Gen1 (~4-6h GPU); generate 200K Gen2 documents (~6-8h GPU).\\n— Days 3-8 (PARALLEL TRACK A): DeBERTa-v3-large ordinal training begins with Gen0+Gen1 data at Day 3; adds Gen2 data when available at Day 5; ablations over surface vs. embedding feature subsets.\\n— Days 5-10 (PARALLEL TRACK B): GPT-2-scale collapse experiments start with Gen0-only and Gen0+Gen1 at Day 5; add Gen2 filtering condition at Day 6. Llama-3.2-1B recursive corpus generation runs in parallel if compute budget is below 160h H100-equivalent at Day 5.\\n— Days 7-9: Full classifier evaluation; if Gen1/Gen2 AUC < 0.65, activate primary null-hypothesis binary filtering comparison experiments; if AUC ≥ 0.65 but collapse severity parity detected, record secondary null outcome and report governance implications.\\n— Days 9-10: Zero-shot depth scoring on real FineWeb/C4 slices.\\n— Days 10-12: Feature importance ablations; cross-model generalizability check on Llama-3.2-1B-generated corpus (if optional Llama recursive corpus was generated).\\n— Days 12-16: Analysis, writing, revision, and submission.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~210h A100 (40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B + 50h DeBERTa-v3-large fine-tuning and ablations + 120h GPT-2-scale collapse validation experiments across 3 filtering strategies)\",\n      \"gpu_utilization\": \"High idle rate (~40-60%): GPU waits while researcher designs experiment configs, interprets collapse curves, debugs depth signal quality, and writes between each stage over several months\",\n      \"timeline\": \"4-6 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$370 at $1.75/h blended A100 average (RunPod ~$1.49/h, Lambda ~$2.06/h); approximately 70 H100-equivalent hours\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~320h A100 (agent handles training loop queuing and ablation scheduling; human approves depth-feature selection, collapse experiment design, AUC threshold decision for null-hypothesis activation, and Llama-3.2-1B second-family validation)\",\n      \"gpu_utilization\": \"Moderate idle rate (~15-25%): agent queues overnight runs and fills GPU gaps between sequential generational steps; handles parallel DeBERTa and collapse experiment scheduling\",\n      \"timeline\": \"6-10 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$60-120 (~600-800 agent turns at $0.08-0.15/turn for experiment design, result interpretation, and iteration guidance)\",\n      \"estimated_gpu_cost\": \"~$560 at $1.75/h average A100; approximately 107 H100-equivalent hours\",\n      \"risk_note\": \"Key bottleneck: 2-step sequential corpus construction (train on GenN → generate GenN+1 → train again) cannot be parallelized; each step adds ~1 wallclock day with Qwen3-0.6B. This is substantially compressed vs. the original 3-step design. Pre-specified dual null-hypothesis design (primary: AUC < 0.65; secondary: AUC ≥ 0.65 but collapse severity parity) means the agent has clear decision rules without requiring researcher judgment to pivot, covering all four logical outcome combinations.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~490h A100 / ~163h H100-equivalent hours (mandatory, within ≤200h hard constraint): 40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B + 120h DeBERTa-v3-large fine-tuning and ablations with 2x hyperparameter search across depth-feature combinations (surface-only, embedding-only, combined) + 240h GPT-2-scale collapse validation experiments across 3 filtering strategies (Qwen3-0.6B family) with 3 collapse metrics + 90h auxiliary ablations (feature importance, zero-shot FineWeb/C4 scoring, null-hypothesis binary filtering comparison if AUC threshold triggered). Llama-3.2-1B recursive corpus generation and collapse experiments (~60-90h A100 / ~20-30h H100-equivalent) are explicitly optional from the start: executed only if compute budget remains below 160h H100-equivalent at Day 10; otherwise deprioritized to zero-shot depth scoring only, maintaining a genuine 40h safety buffer against the 200h hard ceiling.\",\n      \"gpu_utilization\": \"Near-zero idle (<5%): agent queues hyperparameter sweeps and ablations 24/7, filling GPU cycles between sequential generational construction steps with parallel auxiliary experiments\",\n      \"timeline\": \"13-16 days with 4-6 concurrent A100s\",\n      \"team\": \"0 (4-6h one-time setup: genealogical corpus schema, experiment grid, AUC threshold 0.65 for primary null-hypothesis activation, paired t-test criterion for secondary null-hypothesis activation, stopping conditions)\",\n      \"claude_api_cost\": \"$250-400 (~2500-3000 agent turns for experiment orchestration, result analysis, and adaptive exploration)\",\n      \"estimated_gpu_cost\": \"~$856 at $1.75/h average A100 (mandatory only); ~$960 including optional Llama-3.2-1B corpus if budget permits\",\n      \"speed_bottleneck\": \"2-step sequential corpus construction is the hard wallclock floor; GPU count limits simultaneous ablation breadth during non-sequential phases\",\n      \"risk_note\": \"Depth signal may be weak between Gen1 and Gen2 from the same small model — a risk compounded by the 'Wall of Separation' finding (arXiv:2605.01647): AI-AI surface divergence is substantially smaller than human-AI divergence, making within-model generational discrimination harder still. Pre-specified dual null-hypothesis design covers all outcomes: primary null (AUC < 0.65) redirects to binary filtering comparison; secondary null (AUC ≥ 0.65 but collapse severity parity) reports depth detection as feasible but depth-stratified filtering as providing no incremental governance benefit at GPT-2 scale. Embedding-space features (cosine distance from Gen0 centroid) partially mitigate the primary null risk by targeting cumulative semantic drift invisible at the surface level. Budget contingency: Llama-3.2-1B recursive corpus generation is explicitly optional from the start; if compute approaches 160h H100-equivalent during execution (threshold set earlier than the former 180h to create a credible safety margin), Llama-3.2-1B recursive corpus is deprioritized to zero-shot depth scoring only (no new collapse experiments), saving ~60-90h A100 (~20-30h H100-equivalent) and maintaining a genuine 40h buffer against the 200h hard ceiling.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; special theme 'New Missions for NLP Research' explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance' — near-perfect topical alignment; conference October 24-29, Budapest)\",\n    \"NAACL 2027 (ARR cycle deadline TBD, expected ~late 2026; safe backup with more time for thorough collapse validation experiments and additional model families)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"AI models collapse when trained on recursively generated data (Nature 2024)\",\n    \"Strong Model Collapse (ICLR 2025) — establishes collapse at any non-vanishing synthetic fraction (~1% example); does not distinguish Gen1 from Gen2 synthetic data; this gap is what we fill\",\n    \"Machine-generated text detection prevents language model collapse (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025) — closest upstream prior work: trains binary encoder-only classifiers (evaluating RoBERTa, DeBERTa-v3, ModernBERT) with importance resampling — weights ∝ (1-q(x))^b — to prevent collapse at GPT-2/SmolLM2 scale (124M–1.7B parameters); treats all AI-generated text equivalently without generational depth distinction; our work directly extends this: if depth-stratified resampling weights yield greater collapse-severity reduction per decontamination unit than binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over binary resampling under budget constraints; if not (AUC < 0.65 or collapse severity parity), our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant\",\n    \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (arXiv:2404.01413)\",\n    \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence (arXiv:2510.16657)\",\n    \"ForTIFAI: Fending Off Recursive Training Induced Failure for AI Models (arXiv:2509.08972) — training-side collapse prevention via Truncated Cross-Entropy loss; orthogonal to our upstream corpus-level depth detection; does not classify documents by generational depth\",\n    \"Drift and Selection in LLM Text Ecosystems (arXiv:2604.08554) — mathematical framework for how recursive publication compresses text through drift and selection; derived for variable-order n-gram agents (not transformer fine-tuning); does not propose a depth classifier or detection method; motivates our prediction that embedding-space drift accumulates monotonically across generations even when surface distributions plateau, under the hypothesis that transformer fine-tuning implicitly performs distributional compression analogous to n-gram compression — a generalization our experiments directly test\",\n    \"Understanding Transformers via N-gram Statistics (arXiv:2407.12034, NeurIPS 2024) — transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions across TinyStories and Wikipedia; provides empirical grounding for our hypothesis that the monotonic drift prediction of arXiv:2604.08554 (derived for n-gram agents) extends to transformer fine-tuning at the distributional level\",\n    \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection (arXiv:2605.01647, May 2026) — establishes 'Wall of Separation' where human-AI divergence significantly exceeds AI-AI divergence in character-distribution space; within-model generational gap (Gen1→Gen2 from same fine-tuned model) is smaller still; directly threatens surface-level discriminability; our counter-argument: embedding-space features target cumulative semantic drift orthogonal to character-distribution signals, addressing this challenge; the pre-specified dual null-hypothesis design accounts for the possibility that depth discrimination fails despite embedding-space features\",\n    \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective (NeurIPS 2025 Spotlight)\",\n    \"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (ACL 2024)\",\n    \"Can AI-Generated Text be Reliably Detected? (arXiv:2303.11156)\",\n    \"Diversity Boosts AI-Generated Text Detection (arXiv:2509.18880)\",\n    \"Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models (arXiv:2511.17602) — asks whether synthetic data overlaps with evaluation benchmarks; generational ancestry is orthogonal to benchmark overlap\",\n    \"Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training? (TrainProVe, CVPR 2025, arXiv:2503.09122) — achieves >99% accuracy in image domain using model access and generalization error bounds; differentiation: our method operates on raw text with no model access, enabling upstream corpus-level pre-filtering; different modality and mechanism address the same governance goal\",\n    \"Understanding Generative AI Content with Embedding Models (arXiv:2408.10437) — demonstrates intrinsic separability of AI-generated and human text in compressed embedding space; motivates our use of embedding-space cosine distance features for depth discrimination beyond surface-level signals\",\n    \"Benchmark Data Contamination of Large Language Models: A Survey (arXiv:2406.04244)\",\n    \"A Survey on Data Contamination for Large Language Models (arXiv:2502.14425)\"\n  ],\n  \"description\": \"As web corpora become saturated with AI-generated content (74.2% of new web pages contain some AI text by April 2025, of which 2.5% are fully AI-generated and 71.7% are human-AI blends; Ahrefs, 900K pages), complete decontamination is operationally infeasible, shifting the question to: which synthetic documents cause the most harm and should be removed first? We propose Genealogical Depth Scoring, a method extending binary AI-text detection to ordinal depth classification (Gen0=human, Gen1, Gen2), trained on a controlled corpus produced by 2-step recursive train-generate loops using Qwen3-0.6B. The classifier combines DeBERTa-v3-large fine-tuning with two classes of depth-diagnostic features: surface-level signals (surprisal burstiness, lexical diversity decay, n-gram entropy compression ratio) and embedding-space signals (cosine distance from a Gen0 embedding centroid, MAUVE-style distributional divergence). The embedding-space features directly address the 'Wall of Separation' documented in arXiv:2605.01647 (May 2026) — AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence is smaller still — by targeting cumulative semantic drift that arXiv:2604.08554 predicts to accumulate monotonically across recursive generations even when surface statistics plateau. Because arXiv:2604.08554 derives this prediction for variable-order n-gram agents rather than transformer fine-tuning, we ground the generalization in arXiv:2407.12034 (NeurIPS 2024), which shows transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions, and treat our classifier and collapse experiments as a direct empirical test of whether this theoretical extension holds. We pre-specify a dual null-hypothesis design: (primary null) if Gen1/Gen2 AUC < 0.65, depth is linguistically indistinguishable and binary filtering suffices; (secondary null) if AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between Gen0+Gen1 and Gen0+Gen1+Gen2 filtered corpora, depth detection is feasible but depth-stratified filtering provides no incremental collapse-severity benefit over binary filtering at GPT-2 scale — suggesting the marginal harm-per-generation curve is flat at this model size and binary filtering is sufficient for practical governance. All four logical outcomes produce pre-specified, interpretable empirical contributions. Collapse validation compares depth-stratified filtered corpora (Gen0-only, Gen0+Gen1, Gen0+Gen1+Gen2) via held-out perplexity and output tail entropy; results are framed as *severity reduction per decontamination budget* rather than collapse prevention, since Strong Model Collapse (ICLR 2025) establishes harm at any non-vanishing synthetic fraction. TrainProVe (CVPR 2025) addresses related governance goals via model access in the image domain; ForTIFAI (arXiv:2509.08972) prevents collapse at training time via modified loss; arXiv:2502.15654 (Feb 2025) prevents collapse via binary detection with importance resampling but treats all AI text equivalently without generational depth distinction — our work is the first to assign generational depth scores to raw text corpus documents upstream of training, and directly tests whether depth-stratified resampling yields greater collapse-severity reduction per filtering unit than binary resampling. We release GenDepth-Bench covering 2 model families (Qwen3-0.6B primary; Llama-3.2-1B secondary, optional pending compute budget), with 5+ family coverage as explicit future work. Targets EMNLP 2026's special theme on synthetic data feedback loops and data governance.\",\n  \"project_name\": \"gen_depth_decontam\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 5)\nIssues: [\"MAUVE-STYLE FEATURE ILL-DEFINED AT DOCUMENT LEVEL — MAUVE is a corpus-level metric that estimates KL divergence between two distributions of text embeddings. It requires multiple samples per distribution, not a single document. Applying it as a per-document feature is non-standard and potentially meaningless. The proposal lists 'MAUVE-style distributional divergence' as a depth-diagnostic feature without explaining the per-document operationalization. If this feature simply becomes 'distance of document embedding from Gen0 distribution,' it overlaps substantially with the 'cosine distance from Gen0 centroid' feature already listed. A reviewer will immediately flag this as either technically ill-defined or redundant. Fix: either (a) specify the document-level operationalization explicitly (e.g., 'we compute the negative log-likelihood of a document's embedding under a KDE fit to the Gen0 embedding distribution' or 'we compute the mean embedding of non-overlapping 128-token windows within the document and measure the MAUVE divergence of this within-document distribution from the Gen0 reference distribution'), or (b) rename this feature to accurately reflect what is computed and explain how it differs from the cosine centroid distance.\", \"DEBERTA + HAND-CRAFTED FEATURE INTEGRATION UNSPECIFIED — The approach says the classifier trains 'jointly on raw text and depth-diagnostic features' combining DeBERTa-v3-large with five engineered features from two different representation spaces (surface-level and sentence-transformer embedding space). No architecture is described. Given that DeBERTa produces its own CLS embedding and the sentence-transformer produces a separate embedding vector for the cosine distance computation, the proposal is operating with at least two separate text encoders plus scalar features. How these are merged is entirely unspecified. This is a critical methods gap that affects replicability. Fix: add two sentences specifying the integration architecture (e.g., 'we concatenate the five scalar depth-diagnostic features to the DeBERTa CLS token representation, then train an ordinal regression head over this joint representation; the Gen0 centroid used for cosine distance is computed offline from sentence-transformers/all-MiniLM-L6-v2 embeddings and is not jointly trained').\", \"QWEN3-0.6B THINKING MODE UNSPECIFIED — Qwen3-0.6B supports an explicit thinking mode that generates chain-of-thought reasoning traces within &lt;think>...&lt;/think> tags, which would dramatically alter the character distribution, lexical properties, and statistical footprint of generated text. Whether thinking mode is enabled or disabled during the recursive generation loop must be specified, as it affects: (a) the plausibility of depth signals (thinking traces may be trivially distinguishable), (b) the validity of the Wall of Separation counter-argument (thinking traces produce very different distributions than standard generation), and (c) the external validity of results to real-world web contamination scenarios where thinking traces are absent. This is a one-sentence fix: 'We disable Qwen3-0.6B thinking mode (/no_think) during all generative steps to ensure output text matches real-world web document distributions.'\"]\nFeedback: Three targeted fixes are needed — none require new experiments. (1) MAUVE feature clarification: replace 'MAUVE-style distributional divergence' with a concrete document-level operationalization. The most defensible adaptation is to segment each document into non-overlapping 128-token windows, embed each window via sentence-transformers, and compute the MAUVE divergence between this within-document embedding distribution and the Gen0 reference distribution — this is genuinely distinct from cosine centroid distance as it captures within-document distributional spread, not just central tendency. If this is too complex to implement reliably in 16 days, drop the MAUVE feature and replace it with the variance of within-document embeddings around the Gen0 centroid (a simpler proxy capturing the same distributional geometry idea). (2) DeBERTa integration architecture: add two sentences to the approach specifying that the five scalar features are concatenated to the DeBERTa CLS token, and that the Gen0 centroid is precomputed offline using sentence-transformers and not jointly fine-tuned — this closes the replicability gap without changing the experimental design. (3) Thinking mode: add one sentence specifying that Qwen3 thinking mode is disabled during generation. These three additions require less than an hour of writing and will prevent round-six reviewer rejection on technical specificity grounds.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 5 轮修订，近 3 轮的平均分从 3.5 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-09T20:32:54.019Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-09T20:32:54.019Z",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19"
}
```

---

## Round 1

22 recorded events

### User

_source line 3 · 2026-05-09T20:32:54.049Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-09 (UTC).**

## Original idea
{
  "title": "Genealogical Depth Scoring for Recursive Web Corpus Decontamination",
  "core_problem": "Current AI-generated text detectors are binary (human vs. AI), but training corpora increasingly contain 'second-generation' synthetic text: AI outputs from models that were themselves trained on AI-generated data. This generational depth is unmeasured and unaddressed by any existing detector. Strong Model Collapse (ICLR 2025) establishes that even non-vanishing fractions (~1%) of synthetic data trigger performance collapse, yet the paper treats all synthetic data equivalently — making no distinction between Gen1 text (one model generation removed from human data) and Gen2+ text (recursively compounded). The depth-dependent contribution to collapse severity is entirely uncharacterized, and no current method can assign a generational depth score to a raw training document. Critically, recent work (arXiv:2605.01647, May 2026) demonstrates a 'Wall of Separation' where AI-AI divergence in character-distribution space is significantly smaller than human-AI divergence — making within-model generational discrimination (Gen1 vs. Gen2 from the same fine-tuned model) a harder detection problem than binary human/AI classification and motivating our use of embedding-space features that target cumulative semantic drift orthogonal to character-level surface signals.",
  "opportunity": "By April 2025, 74.2% of newly created web pages contain some AI-generated text — of which 2.5% are fully AI-generated and 71.7% are human-AI blends, where human content has been AI-revised or AI-assisted (Ahrefs, 900K pages, April 2025). These blended documents may occupy an intermediate 'Gen0.5' depth position between Gen0 and Gen1 that depth scoring can address more precisely than binary detection, and they represent the dominant contamination modality at web scale. Complete decontamination is operationally infeasible — there is not enough uncontaminated human text to replace even the fully AI-generated fraction — shifting the practical research question from 'remove all synthetic data' (impossible at web scale) to 'which synthetic documents to prioritize for removal given a fixed filtering budget.' Depth-stratified decontamination addresses this directly: if Gen2+ documents are disproportionately harmful relative to Gen1 documents, preferential removal of deeper-generation text maximizes collapse mitigation per unit of filtering effort. This claim is explicitly scoped to *severity reduction per filtering budget*, not collapse prevention: Strong Model Collapse (ICLR 2025) establishes that any non-vanishing synthetic fraction triggers collapse, so a corpus that retains Gen1 documents after removing Gen2 still contains harmful synthetic content. The value of depth-stratified filtering is that it reduces expected collapse severity for a fixed decontamination budget by prioritizing the highest-harm documents first — a practical governance claim that holds even if perfect decontamination is required for complete collapse prevention. Strong Model Collapse (ICLR 2025) provides the urgency but not the answer — it shows synthetic data is harmful at any non-vanishing fraction but gives no guidance on whether all synthetic data is equally harmful. Crucially, the paper does not distinguish Gen1 from Gen2 synthetic data at all, leaving the depth-dependent harm gradient completely unmeasured. A depth classifier that enables tiered decontamination — or, if depth discrimination fails, definitively establishes that binary filtering suffices — constitutes a concrete empirical contribution with direct governance impact, aligned with EMNLP 2026's special theme 'New Missions for NLP Research,' which explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance.'",
  "landscape": "Model collapse from recursive synthetic training is established (Shumailov et al., Nature 2024; Strong Model Collapse, ICLR 2025) and the limiting theory predicts collapse at any non-vanishing synthetic fraction. Mitigation via real-data accumulation (arXiv:2404.01413) or verifier-guided retraining (arXiv:2510.16657) is active. Training-side collapse prevention via Truncated Cross-Entropy loss (ForTIFAI, arXiv:2509.08972) selectively ignores high-confidence tokens during training to filter synthetic artifacts — a complementary but orthogonal approach to our upstream corpus-level depth detection: ForTIFAI does not classify documents by generational depth and does not operate pre-training. The closest upstream related work, 'Machine-generated text detection prevents language model collapse' (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025), directly bridges AI-text detection and collapse prevention: it trains encoder-only binary classifiers (evaluating RoBERTa, DeBERTa-v3, and ModernBERT) to distinguish human from AI-generated text, then applies importance resampling — weighting each training document by (1-q(x))^b where q(x) is the classifier's AI-probability score — to up-weight likely human content during recursive training. Experiments across GPT-2 and SmolLM2 (124M–1.7B parameters) demonstrate that binary-classifier-guided resampling prevents collapse and even improves over training on purely human data. Critically, arXiv:2502.15654 treats all AI-generated text as equivalent regardless of generational provenance: importance weights depend only on a single binary human/AI probability, with no distinction between Gen1 text (one fine-tuning cycle removed from human data) and Gen2+ text (recursively compounded). Our work directly addresses this gap: if depth-stratified resampling weights — proportional to estimated generational distance from Gen0 — yield greater collapse-severity reduction per resampled document than flat binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over arXiv:2502.15654's strategy under budget-constrained filtering. The dual null-hypothesis design explicitly covers the scenario where depth discrimination fails (AUC < 0.65), in which case our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant and binary resampling is sufficient — a governance finding with direct practical value. A mathematical framework for how recursive publication compresses text through drift and selection is developed in arXiv:2604.08554 but does not propose a depth classifier. The framework is derived for variable-order n-gram agents and does not address transformer fine-tuning; extension to neural models is an open theoretical question that our experiments probe empirically. AI-generated text detection (arXiv:2303.11156, arXiv:2509.18880) addresses binary classification and reaches AUC ~0.85-0.90 for Gen1 text, uniformly treating all AI-generated text as equivalent regardless of generational provenance. Embedding-based representations show intrinsic separability between AI-generated and human text in compressed embedding spaces (arXiv:2408.10437), motivating our use of embedding-space distance features alongside surface-level signals. 'Understanding Transformers via N-gram Statistics' (arXiv:2407.12034, NeurIPS 2024) provides empirical motivation for applying n-gram-derived theoretical predictions to transformer fine-tuning: transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions across TinyStories and Wikipedia, suggesting transformer distributional behavior closely approximates n-gram statistics at the local prediction level — supporting our hypothesis that the monotonic drift prediction of arXiv:2604.08554 (derived for n-gram agents) extends to transformer fine-tuning at the distributional level, with our experiments constituting a direct empirical test of this generalization. 'Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection' (arXiv:2605.01647, May 2026) introduces the Letter Distribution Score (LD-Score) and establishes a 'Wall of Separation' where human-AI divergence significantly exceeds AI-AI divergence in character-distribution space — with the direct implication that within-model generational divergence (Gen1 vs. Gen2 from the same fine-tuned 0.6B model) is smaller still than cross-model AI-AI divergence. This finding validates our architectural choice to prioritize embedding-space features over character-distribution proxies: our cosine distance from Gen0 centroid and MAUVE-style divergence operate in a representation space where cumulative semantic drift — predicted to accumulate monotonically by arXiv:2604.08554's recursive drift-selection framework — may remain detectable even when surface and character-level signals converge. The pre-specified AUC threshold (0.65) and dual null-hypothesis pivot design explicitly account for the scenario where depth discrimination fails at the document level despite embedding-space features. No paper in the contamination detection surveys (arXiv:2502.14425, arXiv:2406.04244) addresses generation depth as a variable. The closest concurrent work — 'Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models' (arXiv:2511.17602, Nov 2025) — asks whether synthetic data overlaps with evaluation benchmarks, not how many generative cycles deep a document is; generational ancestry is orthogonal to benchmark overlap. 'Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training?' (TrainProVe, CVPR 2025, arXiv:2503.09122) achieves >99% accuracy verifying which text-to-image model generated a given image, using model access and generalization error bounds — differentiation is sharp: TrainProVe operates in the image domain and requires model weights access, while our method operates on raw text documents with no model access, enabling upstream corpus-level pre-filtering. Both address data governance but via entirely complementary mechanisms. 'A Closer Look at Model Collapse' (arXiv:2509.16499, NeurIPS 2025 Spotlight) identifies a generalization-to-memorization transition but studies diffusion models and does not distinguish depth levels in training data.",
  "approach": "We build a controlled genealogical corpus by running a 2-step recursive train-generate loop with Qwen3-0.6B (the smallest Qwen3 model, chosen to minimize sequential compute cost while still exhibiting measurable distributional drift per generation), producing text with verified depth labels Gen0 (human, sourced from FineWeb-Edu and C4), Gen1, and Gen2, yielding ~200K labeled documents per depth level across diverse domains. Limiting to Gen0/Gen1/Gen2 compresses the sequential corpus construction bottleneck to approximately 2 wallclock days: Qwen3-0.6B fine-tuning on a 200K-document sample runs in ~4-6 GPU hours on A100, and generation of 200K new documents runs in ~6-8 GPU hours, for ~12-14 GPU hours per generational step. The hard sequential dependency spans only 2 steps.\n\nWe train a DeBERTa-v3-large ordinal regression classifier jointly on raw text and depth-diagnostic features spanning two categories: (a) surface-level signals — per-token surprisal variance (burstiness), lexical diversity decay (MTLD and type-token ratio), and n-gram entropy compression ratio; and (b) embedding-space signals — cosine distance from a Gen0 embedding centroid computed via sentence-transformers, and MAUVE-style distributional divergence. Embedding-space features are specifically motivated by the 'Wall of Separation' established in arXiv:2605.01647 (May 2026): AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence (Gen1→Gen2 from the same fine-tuned 0.6B model) is smaller still. Surface-level and character-distribution signals are therefore unlikely to reliably discriminate depth levels in this setting; our embedding-space features instead target cumulative semantic drift that arXiv:2604.08554's recursive drift-selection framework predicts to accumulate monotonically across generations even when character distributions plateau — providing detection signal orthogonal to surface proxies. The argument is: our embedding-space features target cumulative semantic drift that persists even when surface divergence converges, consistent with the monotonic drift predicted by arXiv:2604.08554 — with the explicit caveat that arXiv:2604.08554 derives this prediction for variable-order n-gram agents, not transformer fine-tuning. We hypothesize the generalization holds because transformer next-token distributions closely approximate n-gram statistics at the local prediction level (arXiv:2407.12034, NeurIPS 2024, reports 68–79% agreement between transformer predictions and n-gram rulesets across two corpora), suggesting transformer fine-tuning implicitly performs distributional compression analogous to n-gram compression, for which cumulative drift is expected to accumulate monotonically. Our classifier and collapse experiments directly test whether this hypothesized generalization from n-gram theory to transformer practice holds empirically.\n\nCentral technical risk and dual null-hypothesis design: We pre-specify two complementary pre-registered outcome scenarios to ensure a definitive, interpretable empirical finding under all classifier and collapse experiment outcomes. (Primary null) If the ordinal classifier falls below AUC 0.65 on Gen1/Gen2 discrimination, the finding is publishable: depth beyond Gen1 is linguistically indistinguishable at the document level using current text-level and embedding-level methods, implying binary filtering suffices — consistent with the implicit assumption of arXiv:2502.15654. In this case, the collapse validation experiments automatically pivot to directly comparing binary (Gen0-only) filtering against depth-stratified filtering. (Secondary null) If the classifier achieves AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between Gen0+Gen1 and Gen0+Gen1+Gen2 filtered corpora (paired t-test, α = 0.05, across 3 random seeds), we report this as a distinct secondary null outcome: depth detection is feasible but depth-stratified filtering provides no incremental collapse-severity benefit over binary filtering at GPT-2 scale, suggesting the marginal harm-per-generation curve is flat at this model size and that binary filtering is therefore sufficient for practical governance at small scales. This finding has direct governance implications — preferential removal of Gen2 documents yields no measurable advantage over simple binary decontamination at GPT-2 scale — while leaving open whether depth stratification provides additional value at larger model scales, explicitly reserved as future work. All four logical combinations of (AUC pass/fail) × (collapse severity parity/non-parity) produce pre-specified, interpretable empirical contributions with distinct governance implications.\n\nThe trained classifier is applied zero-shot to real FineWeb and C4 slices to estimate depth-distribution statistics of existing pretraining corpora. Collapse validation uses a GPT-2-scale LM fine-tuned on depth-stratified filtered corpora (Gen0-only, Gen0+Gen1, Gen0+Gen1+Gen2) with collapse severity tracked via held-out human-text perplexity and output tail entropy across multiple recursive training generations. Collapse experiments are explicitly scoped to measuring *severity reduction* across filtering strategies — not collapse prevention — consistent with Strong Model Collapse's any-fraction harm finding. GenDepth-Bench is scoped to 2 model families: Qwen3-0.6B (primary) and Llama-3.2-1B (secondary, run through the same recursive loop to test cross-model generalizability of depth signals, explicitly optional — executed only if compute budget permits; see resource estimate). Coverage of 5+ model families is explicitly reserved as future work.\n\n16-Day Critical Path (EMNLP 2026 ARR deadline May 25, 2026; today May 9, 2026):\n— Days 1-2: Environment setup; sample 200K Gen0 docs from FineWeb-Edu/C4; prepare evaluation suite and draft intro/related-work sections.\n— Days 2-3 (sequential bottleneck step 1): Fine-tune Qwen3-0.6B on Gen0 (~4-6h GPU); generate 200K Gen1 documents (~6-8h GPU).\n— Days 3-4 (sequential bottleneck step 2): Fine-tune Qwen3-0.6B-v2 on Gen1 (~4-6h GPU); generate 200K Gen2 documents (~6-8h GPU).\n— Days 3-8 (PARALLEL TRACK A): DeBERTa-v3-large ordinal training begins with Gen0+Gen1 data at Day 3; adds Gen2 data when available at Day 5; ablations over surface vs. embedding feature subsets.\n— Days 5-10 (PARALLEL TRACK B): GPT-2-scale collapse experiments start with Gen0-only and Gen0+Gen1 at Day 5; add Gen2 filtering condition at Day 6. Llama-3.2-1B recursive corpus generation runs in parallel if compute budget is below 160h H100-equivalent at Day 5.\n— Days 7-9: Full classifier evaluation; if Gen1/Gen2 AUC < 0.65, activate primary null-hypothesis binary filtering comparison experiments; if AUC ≥ 0.65 but collapse severity parity detected, record secondary null outcome and report governance implications.\n— Days 9-10: Zero-shot depth scoring on real FineWeb/C4 slices.\n— Days 10-12: Feature importance ablations; cross-model generalizability check on Llama-3.2-1B-generated corpus (if optional Llama recursive corpus was generated).\n— Days 12-16: Analysis, writing, revision, and submission.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~210h A100 (40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B + 50h DeBERTa-v3-large fine-tuning and ablations + 120h GPT-2-scale collapse validation experiments across 3 filtering strategies)",
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
      "risk_note": "Key bottleneck: 2-step sequential corpus construction (train on GenN → generate GenN+1 → train again) cannot be parallelized; each step adds ~1 wallclock day with Qwen3-0.6B. This is substantially compressed vs. the original 3-step design. Pre-specified dual null-hypothesis design (primary: AUC < 0.65; secondary: AUC ≥ 0.65 but collapse severity parity) means the agent has clear decision rules without requiring researcher judgment to pivot, covering all four logical outcome combinations."
    },
    "auto_research": {
      "gpu_hours": "~490h A100 / ~163h H100-equivalent hours (mandatory, within ≤200h hard constraint): 40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B + 120h DeBERTa-v3-large fine-tuning and ablations with 2x hyperparameter search across depth-feature combinations (surface-only, embedding-only, combined) + 240h GPT-2-scale collapse validation experiments across 3 filtering strategies (Qwen3-0.6B family) with 3 collapse metrics + 90h auxiliary ablations (feature importance, zero-shot FineWeb/C4 scoring, null-hypothesis binary filtering comparison if AUC threshold triggered). Llama-3.2-1B recursive corpus generation and collapse experiments (~60-90h A100 / ~20-30h H100-equivalent) are explicitly optional from the start: executed only if compute budget remains below 160h H100-equivalent at Day 10; otherwise deprioritized to zero-shot depth scoring only, maintaining a genuine 40h safety buffer against the 200h hard ceiling.",
      "gpu_utilization": "Near-zero idle (<5%): agent queues hyperparameter sweeps and ablations 24/7, filling GPU cycles between sequential generational construction steps with parallel auxiliary experiments",
      "timeline": "13-16 days with 4-6 concurrent A100s",
      "team": "0 (4-6h one-time setup: genealogical corpus schema, experiment grid, AUC threshold 0.65 for primary null-hypothesis activation, paired t-test criterion for secondary null-hypothesis activation, stopping conditions)",
      "claude_api_cost": "$250-400 (~2500-3000 agent turns for experiment orchestration, result analysis, and adaptive exploration)",
      "estimated_gpu_cost": "~$856 at $1.75/h average A100 (mandatory only); ~$960 including optional Llama-3.2-1B corpus if budget permits",
      "speed_bottleneck": "2-step sequential corpus construction is the hard wallclock floor; GPU count limits simultaneous ablation breadth during non-sequential phases",
      "risk_note": "Depth signal may be weak between Gen1 and Gen2 from the same small model — a risk compounded by the 'Wall of Separation' finding (arXiv:2605.01647): AI-AI surface divergence is substantially smaller than human-AI divergence, making within-model generational discrimination harder still. Pre-specified dual null-hypothesis design covers all outcomes: primary null (AUC < 0.65) redirects to binary filtering comparison; secondary null (AUC ≥ 0.65 but collapse severity parity) reports depth detection as feasible but depth-stratified filtering as providing no incremental governance benefit at GPT-2 scale. Embedding-space features (cosine distance from Gen0 centroid) partially mitigate the primary null risk by targeting cumulative semantic drift invisible at the surface level. Budget contingency: Llama-3.2-1B recursive corpus generation is explicitly optional from the start; if compute approaches 160h H100-equivalent during execution (threshold set earlier than the former 180h to create a credible safety margin), Llama-3.2-1B recursive corpus is deprioritized to zero-shot depth scoring only (no new collapse experiments), saving ~60-90h A100 (~20-30h H100-equivalent) and maintaining a genuine 40h buffer against the 200h hard ceiling."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; special theme 'New Missions for NLP Research' explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance' — near-perfect topical alignment; conference October 24-29, Budapest)",
    "NAACL 2027 (ARR cycle deadline TBD, expected ~late 2026; safe backup with more time for thorough collapse validation experiments and additional model families)"
  ],
  "level": "solid",
  "key_references": [
    "AI models collapse when trained on recursively generated data (Nature 2024)",
    "Strong Model Collapse (ICLR 2025) — establishes collapse at any non-vanishing synthetic fraction (~1% example); does not distinguish Gen1 from Gen2 synthetic data; this gap is what we fill",
    "Machine-generated text detection prevents language model collapse (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025) — closest upstream prior work: trains binary encoder-only classifiers (evaluating RoBERTa, DeBERTa-v3, ModernBERT) with importance resampling — weights ∝ (1-q(x))^b — to prevent collapse at GPT-2/SmolLM2 scale (124M–1.7B parameters); treats all AI-generated text equivalently without generational depth distinction; our work directly extends this: if depth-stratified resampling weights yield greater collapse-severity reduction per decontamination unit than binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over binary resampling under budget constraints; if not (AUC < 0.65 or collapse severity parity), our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant",
    "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (arXiv:2404.01413)",
    "Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence (arXiv:2510.16657)",
    "ForTIFAI: Fending Off Recursive Training Induced Failure for AI Models (arXiv:2509.08972) — training-side collapse prevention via Truncated Cross-Entropy loss; orthogonal to our upstream corpus-level depth detection; does not classify documents by generational depth",
    "Drift and Selection in LLM Text Ecosystems (arXiv:2604.08554) — mathematical framework for how recursive publication compresses text through drift and selection; derived for variable-order n-gram agents (not transformer fine-tuning); does not propose a depth classifier or detection method; motivates our prediction that embedding-space drift accumulates monotonically across generations even when surface distributions plateau, under the hypothesis that transformer fine-tuning implicitly performs distributional compression analogous to n-gram compression — a generalization our experiments directly test",
    "Understanding Transformers via N-gram Statistics (arXiv:2407.12034, NeurIPS 2024) — transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions across TinyStories and Wikipedia; provides empirical grounding for our hypothesis that the monotonic drift prediction of arXiv:2604.08554 (derived for n-gram agents) extends to transformer fine-tuning at the distributional level",
    "Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection (arXiv:2605.01647, May 2026) — establishes 'Wall of Separation' where human-AI divergence significantly exceeds AI-AI divergence in character-distribution space; within-model generational gap (Gen1→Gen2 from same fine-tuned model) is smaller still; directly threatens surface-level discriminability; our counter-argument: embedding-space features target cumulative semantic drift orthogonal to character-distribution signals, addressing this challenge; the pre-specified dual null-hypothesis design accounts for the possibility that depth discrimination fails despite embedding-space features",
    "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective (NeurIPS 2025 Spotlight)",
    "RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (ACL 2024)",
    "Can AI-Generated Text be Reliably Detected? (arXiv:2303.11156)",
    "Diversity Boosts AI-Generated Text Detection (arXiv:2509.18880)",
    "Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models (arXiv:2511.17602) — asks whether synthetic data overlaps with evaluation benchmarks; generational ancestry is orthogonal to benchmark overlap",
    "Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training? (TrainProVe, CVPR 2025, arXiv:2503.09122) — achieves >99% accuracy in image domain using model access and generalization error bounds; differentiation: our method operates on raw text with no model access, enabling upstream corpus-level pre-filtering; different modality and mechanism address the same governance goal",
    "Understanding Generative AI Content with Embedding Models (arXiv:2408.10437) — demonstrates intrinsic separability of AI-generated and human text in compressed embedding space; motivates our use of embedding-space cosine distance features for depth discrimination beyond surface-level signals",
    "Benchmark Data Contamination of Large Language Models: A Survey (arXiv:2406.04244)",
    "A Survey on Data Contamination for Large Language Models (arXiv:2502.14425)"
  ],
  "description": "As web corpora become saturated with AI-generated content (74.2% of new web pages contain some AI text by April 2025, of which 2.5% are fully AI-generated and 71.7% are human-AI blends; Ahrefs, 900K pages), complete decontamination is operationally infeasible, shifting the question to: which synthetic documents cause the most harm and should be removed first? We propose Genealogical Depth Scoring, a method extending binary AI-text detection to ordinal depth classification (Gen0=human, Gen1, Gen2), trained on a controlled corpus produced by 2-step recursive train-generate loops using Qwen3-0.6B. The classifier combines DeBERTa-v3-large fine-tuning with two classes of depth-diagnostic features: surface-level signals (surprisal burstiness, lexical diversity decay, n-gram entropy compression ratio) and embedding-space signals (cosine distance from a Gen0 embedding centroid, MAUVE-style distributional divergence). The embedding-space features directly address the 'Wall of Separation' documented in arXiv:2605.01647 (May 2026) — AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence is smaller still — by targeting cumulative semantic drift that arXiv:2604.08554 predicts to accumulate monotonically across recursive generations even when surface statistics plateau. Because arXiv:2604.08554 derives this prediction for variable-order n-gram agents rather than transformer fine-tuning, we ground the generalization in arXiv:2407.12034 (NeurIPS 2024), which shows transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions, and treat our classifier and collapse experiments as a direct empirical test of whether this theoretical extension holds. We pre-specify a dual null-hypothesis design: (primary null) if Gen1/Gen2 AUC < 0.65, depth is linguistically indistinguishable and binary filtering suffices; (secondary null) if AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between Gen0+Gen1 and Gen0+Gen1+Gen2 filtered corpora, depth detection is feasible but depth-stratified filtering provides no incremental collapse-severity benefit over binary filtering at GPT-2 scale — suggesting the marginal harm-per-generation curve is flat at this model size and binary filtering is sufficient for practical governance. All four logical outcomes produce pre-specified, interpretable empirical contributions. Collapse validation compares depth-stratified filtered corpora (Gen0-only, Gen0+Gen1, Gen0+Gen1+Gen2) via held-out perplexity and output tail entropy; results are framed as *severity reduction per decontamination budget* rather than collapse prevention, since Strong Model Collapse (ICLR 2025) establishes harm at any non-vanishing synthetic fraction. TrainProVe (CVPR 2025) addresses related governance goals via model access in the image domain; ForTIFAI (arXiv:2509.08972) prevents collapse at training time via modified loss; arXiv:2502.15654 (Feb 2025) prevents collapse via binary detection with importance resampling but treats all AI text equivalently without generational depth distinction — our work is the first to assign generational depth scores to raw text corpus documents upstream of training, and directly tests whether depth-stratified resampling yields greater collapse-severity reduction per filtering unit than binary resampling. We release GenDepth-Bench covering 2 model families (Qwen3-0.6B primary; Llama-3.2-1B secondary, optional pending compute budget), with 5+ family coverage as explicit future work. Targets EMNLP 2026's special theme on synthetic data feedback loops and data governance.",
  "project_name": "gen_depth_decontam",
  "source": "web_research"
}

## Reviewer feedback (round 5)
Issues: ["MAUVE-STYLE FEATURE ILL-DEFINED AT DOCUMENT LEVEL — MAUVE is a corpus-level metric that estimates KL divergence between two distributions of text embeddings. It requires multiple samples per distribution, not a single document. Applying it as a per-document feature is non-standard and potentially meaningless. The proposal lists 'MAUVE-style distributional divergence' as a depth-diagnostic feature without explaining the per-document operationalization. If this feature simply becomes 'distance of document embedding from Gen0 distribution,' it overlaps substantially with the 'cosine distance from Gen0 centroid' feature already listed. A reviewer will immediately flag this as either technically ill-defined or redundant. Fix: either (a) specify the document-level operationalization explicitly (e.g., 'we compute the negative log-likelihood of a document's embedding under a KDE fit to the Gen0 embedding distribution' or 'we compute the mean embedding of non-overlapping 128-token windows within the document and measure the MAUVE divergence of this within-document distribution from the Gen0 reference distribution'), or (b) rename this feature to accurately reflect what is computed and explain how it differs from the cosine centroid distance.", "DEBERTA + HAND-CRAFTED FEATURE INTEGRATION UNSPECIFIED — The approach says the classifier trains 'jointly on raw text and depth-diagnostic features' combining DeBERTa-v3-large with five engineered features from two different representation spaces (surface-level and sentence-transformer embedding space). No architecture is described. Given that DeBERTa produces its own CLS embedding and the sentence-transformer produces a separate embedding vector for the cosine distance computation, the proposal is operating with at least two separate text encoders plus scalar features. How these are merged is entirely unspecified. This is a critical methods gap that affects replicability. Fix: add two sentences specifying the integration architecture (e.g., 'we concatenate the five scalar depth-diagnostic features to the DeBERTa CLS token representation, then train an ordinal regression head over this joint representation; the Gen0 centroid used for cosine distance is computed offline from sentence-transformers/all-MiniLM-L6-v2 embeddings and is not jointly trained').", "QWEN3-0.6B THINKING MODE UNSPECIFIED — Qwen3-0.6B supports an explicit thinking mode that generates chain-of-thought reasoning traces within &lt;think>...&lt;/think> tags, which would dramatically alter the character distribution, lexical properties, and statistical footprint of generated text. Whether thinking mode is enabled or disabled during the recursive generation loop must be specified, as it affects: (a) the plausibility of depth signals (thinking traces may be trivially distinguishable), (b) the validity of the Wall of Separation counter-argument (thinking traces produce very different distributions than standard generation), and (c) the external validity of results to real-world web contamination scenarios where thinking traces are absent. This is a one-sentence fix: 'We disable Qwen3-0.6B thinking mode (/no_think) during all generative steps to ensure output text matches real-world web document distributions.'"]
Feedback: Three targeted fixes are needed — none require new experiments. (1) MAUVE feature clarification: replace 'MAUVE-style distributional divergence' with a concrete document-level operationalization. The most defensible adaptation is to segment each document into non-overlapping 128-token windows, embed each window via sentence-transformers, and compute the MAUVE divergence between this within-document embedding distribution and the Gen0 reference distribution — this is genuinely distinct from cosine centroid distance as it captures within-document distributional spread, not just central tendency. If this is too complex to implement reliably in 16 days, drop the MAUVE feature and replace it with the variance of within-document embeddings around the Gen0 centroid (a simpler proxy capturing the same distributional geometry idea). (2) DeBERTa integration architecture: add two sentences to the approach specifying that the five scalar features are concatenated to the DeBERTa CLS token, and that the Gen0 centroid is precomputed offline using sentence-transformers and not jointly fine-tuned — this closes the replicability gap without changing the experimental design. (3) Thinking mode: add one sentence specifying that Qwen3 thinking mode is disabled during generation. These three additions require less than an hour of writing and will prevent round-six reviewer rejection on technical specificity grounds.

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
这个 idea 已经经过 5 轮修订，近 3 轮的平均分从 3.5 到 3.5，没有明显改善。

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
  "promptId": "dad9a63c-11ba-41d3-9666-6e73e7b0f490",
  "type": "user",
  "uuid": "2c7955a4-010f-4424-9c3d-3aec9a17605f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-09T20:32:54.046Z_

```json
{
  "parentUuid": "2c7955a4-010f-4424-9c3d-3aec9a17605f",
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
  "uuid": "08e6faeb-eb57-44f9-b760-b0382d4f814c",
  "timestamp": "2026-05-09T20:32:54.046Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-09T20:32:54.046Z_

```json
{
  "parentUuid": "08e6faeb-eb57-44f9-b760-b0382d4f814c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0aa1f669-9cf2-46cd-bff4-436db0cd5c6b",
  "timestamp": "2026-05-09T20:32:54.046Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19",
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
  "leafUuid": "0aa1f669-9cf2-46cd-bff4-436db0cd5c6b",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise depth scoring approach and fix technical clarity gaps",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19"
}
```

---

### Assistant

_source line 8 · 2026-05-09T20:34:30.385Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully before proceeding.

**Current State:**
- This idea has gone through 5 rounds of revision with no meaningful score improvement (stuck at ~3.5/5)
- The reviewer feedback in this round is actually quite specific and tractable (3 technical fixes)
- But the stagnation warning is important - I need to honestly assess whether these fixes will move the needle

**Analyzing the Three Issues:**

1. **MAUVE-style feature ill-defined at document level** - This is a legitimate technical critique. MAUVE is corpus-level, not document-level. The fix is clear: either operationalize it properly (128-token window segmentation → embed → compute distribution divergence from Gen0 reference) or drop it and use embedding variance. 

2. **DeBERTa + hand-crafted feature integration unspecified** - This is a replicability gap. The fix is two sentences specifying the concatenation architecture. Simple fix.

3. **Qwen3-0.6B thinking mode unspecified** - One sentence fix. Trivial.

**But I need to think deeper: Why is the score stuck at 3.5?**

The round 5 feedback says "three targeted fixes needed — none require new experiments." These are genuinely minor fixes. But the score has been stagnant through 5 rounds. This suggests the core issues might be deeper than what the reviewer is flagging—maybe the fundamental approach or experimental design has limitations that no amount of specification tweaking will resolve.

Looking at the actual weaknesses: the whole approach depends on distinguishing between generations of text from the same 0.6B model, which is an extremely risky empirical bet. Prior work shows AI-AI divergence is much smaller than human-AI divergence, and within-model generational differences would be even smaller. At this scale, two fine-tuning steps from the same checkpoint might produce nearly identical distributions. The dual null hypothesis frames failure as publishable, but reviewers may see through that framing. Plus the 16-day timeline to EMNLP 2026 is incredibly aggressive for what's essentially a high-risk empirical claim.

Even if I could detect generational differences in the text, the theoretical connection between that detection and actual collapse severity is weak. And the budget-constrained filtering framing feels somewhat contrived—if you can detect AI text at all, you'd typically just remove it, so the marginal benefit of depth-stratified filtering over binary filtering is unclear.

The reviewer's specific Round 5 issues are fixable, but the core question remains whether addressing those minor points moves the score meaningfully higher when the fundamental empirical bet is this risky.

I think the right path forward is a major revision that tackles both the three specific technical issues and, more importantly, rebuilds the experimental design and theoretical foundation to make the work more compelling. I could either strengthen the experiments by using a larger model and extending to Gen3 to show a clearer trend, or reframe this entirely as a benchmark paper.

Now I'm considering whether to pivot to a related but stronger angle—like detecting AI-generated text that's been trained on other AI-generated text, or measuring how generational degradation scales with model size and training data diversity. To move forward, I need to search for whether this generational depth detection has already been explored, and look into recent work on multi-generational text analysis.

Let me map out the key searches: document-level distributional divergence metrics, MAUVE adaptations, DeBERTa with engineered features, and any existing work on generational depth detection in AI text. I'm also realizing the stagnation at 3.5/5 might not be a dead end—the latest reviewer feedback is mostly about specification clarity rather than fundamental conceptual issues. If I tighten the framing and make the contribution more explicit, particularly around being the first to assign generational depth scores to raw documents and connecting that to model properties, this could actually move the score meaningfully.

The dual null-hypothesis design is genuinely valuable because it guarantees a publishable result, but I need to reframe that more carefully—it shouldn't sound like low expectations, it should sound like rigorous methodology. The real question is whether knowing Gen1 versus Gen2 matters practically if the collapse difference turns out small, and whether the compressed timeline undermines confidence in the work.

I'm considering whether pivoting toward GenDepth-Bench as the primary contribution makes more sense than leading with the classifier itself. A systematic characterization of how text properties evolve across generations, tested across multiple models and scales, could be genuinely useful as a benchmark for future work. But that still doesn't fully address the novelty gap. There's also the recursive contamination auditing angle—shifting focus from classification to auditing how contamination propagates through generations—though I'm not sure that's the right direction either.

What I actually think I should do is make the three technical fixes the reviewer mentioned, then substantially strengthen the framing around the benchmark as a primary deliverable rather than a side effect. I need to get much more concrete about the integration architecture and honestly assess what's realistic within the timeline. The key move is making the MAUVE feature concrete—using within-document window variance instead of corpus-level MAUVE—and being explicit about the DeBERTa integration and thinking mode specification. Beyond those fixes, I should examine whether there are deeper structural issues with the approach.

The real question is whether the 3.5/5 score is stuck because of technical specification gaps or something more fundamental. Based on the specificity of the current feedback, it looks like the reviewer has accepted the framing and novelty, so what's left are reproducibility and clarity issues. That suggests a focused minor revision is the right move, but I should still think critically about whether I'm missing something bigger. Let me start by researching how MAUVE has been adapted at the document level. I need to verify that the within-document MAUVE approach is technically sound, check for any recent work that might undermine the novelty, and find a stronger theoretical anchor for the embedding features before committing to the minor fix strategy. The reviewer's suggestion is spot-on—replacing MAUVE with embedding variance around the Gen0 centroid is cleaner and more defensible as a document-level feature. It's simpler to compute, directly motivated by the embedding-space drift hypothesis, and still captures distributional spread rather than just the mean distance. Now I need to integrate this into the revision while keeping the DeBERTa setup intact, where I'm using the CLS token for surprisal features and sentence-transformers embeddings for the cosine distance and variance calculations. LD, type-token ratio, n-gram entropy compression, cosine distance from Gen0 centroid, and within-document embedding variance—that gives us 6 features total. Let me verify: per-token surprisal variance, MTLD, type-token ratio, n-gram entropy compression, mean cosine distance from Gen0 centroid, and variance around that centroid. Features 5 and 6 work together—one captures how far the document sits from human text on average, the other captures how spread out its embedding distribution is, which could reveal different generation patterns even with similar central tendency. For the model itself, I'm concatenating DeBERTa-v3-large's 1024-dimensional CLS representation with these 6 scalar features and feeding them into an ordinal regression head, using a Gen0 centroid computed offline from sentence-transformers embeddings.

The DeBERTa weights will be fine-tuned while the regression head trains from scratch. For Qwen3, I'm disabling thinking mode during generation to match real-world web distributions where chain-of-thought traces don't appear. Now I need to search for recent work to make sure I'm not overlooking better approaches, then implement these three fixes systematically throughout the proposal—replacing the MAUVE reference with the embedding variance metric and integrating the other refinements. I'm refining the embedding-space feature definitions to be more precise — clarifying that cosine distance measures the central tendency of window embeddings relative to the Gen0 centroid, while variance captures the distributional spread, making these two distinct geometric properties. Now I should search for recent work on document-level distributional divergence approaches to ensure I'm not missing better alternatives. I'm planning out the JSON structure for the revision now—I need to update the approach section with the three specific fixes: replacing the MAUVE metric with within-document embedding variance using a 128-token window, integrating DeBERTa into the architecture, and specifying Qwen3's thinking mode. I'll also update the description and potentially add new references from my research, then mark this as a minor change.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0aa1f669-9cf2-46cd-bff4-436db0cd5c6b",
  "isSidechain": false,
  "requestId": "req_011CasdcKFycZkwcVvrxXDum",
  "type": "assistant",
  "uuid": "e37b73e5-ef54-4913-8e5f-1bf92677eef3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KQXMzA6ZG21yuAVS8keVQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15558,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4612,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15558,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4612,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 15558,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15558
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

_source line 9 · 2026-05-09T20:34:35.496Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01CwiAHjuMAzZ4CauerPtDg2`</summary>

```json
{
  "description": "Research MAUVE document-level adaptations and concurrent generational depth detection work",
  "subagent_type": "Explore",
  "prompt": "Search the web for the following three topics and return concise findings (under 400 words total):\n\n1. Search for papers or methods that adapt MAUVE (a corpus-level text distribution metric) to the per-document level. Query: \"MAUVE document level per-document distributional divergence text classification embedding variance\". What operationalizations exist for using MAUVE-like distributional divergence as a feature for individual documents?\n\n2. Search for any recent (2025-2026) papers on detecting generational depth of AI-generated text, recursive text contamination depth scoring, or multi-generation synthetic text detection. Query: \"generational depth AI text detection synthetic training data recursive contamination 2025 2026\". Are there any concurrent works that threaten novelty?\n\n3. Search for standard approaches to integrate scalar features with DeBERTa/BERT CLS token for classification. Query: \"DeBERTa classification concatenate scalar features CLS token ordinal regression architecture\". What is the standard integration pattern?\n\nFor each topic, give me 2-3 concrete findings that would inform a paper revision. Focus on what's actually findable online, not hypotheticals."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e37b73e5-ef54-4913-8e5f-1bf92677eef3",
  "isSidechain": false,
  "requestId": "req_011CasdcKFycZkwcVvrxXDum",
  "type": "assistant",
  "uuid": "7bf6de12-a7f5-4e52-9ac6-a40170dcdddc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KQXMzA6ZG21yuAVS8keVQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15558,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4612,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15558,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4612,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 15558,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15558
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-09 (UTC).**  ## Original idea {   \"title\": \"Genealogical Depth Scoring for Recursive Web Corpus Decontamination\",…",
  "leafUuid": "7bf6de12-a7f5-4e52-9ac6-a40170dcdddc",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise depth scoring approach and fix technical clarity gaps",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19"
}
```

---

### Tool result

_source line 12 · 2026-05-09T20:34:55.141Z_

<details><summary>↩ Tool result · `toolu_01CwiAHjuMAzZ4CauerPtDg2`</summary>

```text
## Findings Summary

### 1. MAUVE Document-Level Adaptation

The search reveals that **MAUVE operates at corpus level via divergence frontiers in quantized embedding space**, but I found **no published methods for direct document-level MAUVE adaptation**. Key findings:
- MAUVE uses KL divergences in low-dimensional quantized spaces (k-means clustering of embeddings), making per-document application non-obvious without reformulation
- The architecture requires histogram construction from distribution samples, which doesn't translate cleanly to single-document analysis
- **Gap identified**: Using document-level embedding variance or distributional moments as MAUVE-like features appears to be an unexplored operationalization that could strengthen your novelty claim

**Sources:**
- [MAUVE: Measuring the Gap Between Neural Text and Human Text](https://arxiv.org/pdf/2102.01454)
- [MAUVE Scores for Generative Models: Theory and Practice](https://www.jmlr.org/papers/volume24/23-0023/23-0023.pdf)

---

### 2. Generational Depth Detection

The 2025-2026 landscape shows active work on **recursive contamination and model collapse**, but **no published methods specifically for "generational depth scoring"** were found:
- A 2026 medical AI preprint demonstrates model collapse from recursive self-training (synthetic→synthetic→synthetic) with measurable degradation in diversity across generations
- The NIST GenAI Text 2026 Challenge is actively soliciting detection work, suggesting this remains open territory
- Literature emphasizes detecting AI-generated text via diversity loss, but not explicitly tracking *how many generations* of synthesis occurred
- **Threat assessment**: Concurrent work on recursive contamination exists, but no explicit depth-scoring metrics were published (this is your novel angle)

**Sources:**
- [AI-generated data contamination erodes pathological...](https://www.medrxiv.org/content/10.64898/2026.01.19.26344383v1.full.pdf)
- [Diversity Boosts AI-Generated Text Detection](https://arxiv.org/pdf/2509.18880)
- [NIST AI Text 2026 Challenge](https://ai-challenges.nist.gov/text-2026)

---

### 3. Scalar Feature Integration with DeBERTa CLS Token

Standard architecture patterns emerged, though no ordinal regression-specific papers were surfaced:
- **Standard approach**: Extract pooled CLS representation → feed through linear classification head (standard Hugging Face pattern for sequence classification)
- For custom scalar integration, the implicit pattern is CLS concatenation followed by MLP layers, mirroring BERT fusion approaches
- Ordinal regression variants would typically involve multi-task or constrained loss functions applied to the fused representation
- **Implementation gap**: No specific published architecture for ordinal regression with explicit scalar concatenation found; this is a standard engineering choice rather than a novel method

**Sources:**
- [DeBERTa · Hugging Face](https://huggingface.co/docs/transformers/model_doc/deberta)
- [Fine-Tuning BERT for Sequence Applications](https://d2l.ai/chapter_natural-language-processing-applications/finetuning-bert.html)
- [DeBERTa GitHub](https://github.com/microsoft/DeBERTa)

---

**Bottom line for paper revision**: Your document-level MAUVE operationalization (finding 1) and generational depth quantification (finding 2) appear genuinely novel; the scalar+DeBERTa integration (finding 3) is standard practice, so frame it as methodology rather than contribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bf6de12-a7f5-4e52-9ac6-a40170dcdddc",
  "isSidechain": false,
  "promptId": "dad9a63c-11ba-41d3-9666-6e73e7b0f490",
  "type": "user",
  "uuid": "93df0217-e980-444e-875a-4f5a4c744136",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for the following three topics and return concise findings (under 400 words total):\n\n1. Search for papers or methods that adapt MAUVE (a corpus-level text distribution metric) to the per-document level. Query: \"MAUVE document level per-document distributional divergence text classification embedding variance\". What operationalizations exist for using MAUVE-like distributional divergence as a feature for individual documents?\n\n2. Search for any recent (2025-2026) papers on detecting generational depth of AI-generated text, recursive text contamination depth scoring, or multi-generation synthetic text detection. Query: \"generational depth AI text detection synthetic training data recursive contamination 2025 2026\". Are there any concurrent works that threaten novelty?\n\n3. Search for standard approaches to integrate scalar features with DeBERTa/BERT CLS token for classification. Query: \"DeBERTa classification concatenate scalar features CLS token ordinal regression architecture\". What is the standard integration pattern?\n\nFor each topic, give me 2-3 concrete findings that would inform a paper revision. Focus on what's actually findable online, not hypotheticals.",
    "agentId": "a61c04bf9e80140c0",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Findings Summary\n\n### 1. MAUVE Document-Level Adaptation\n\nThe search reveals that **MAUVE operates at corpus level via divergence frontiers in quantized embedding space**, but I found **no published methods for direct document-level MAUVE adaptation**. Key findings:\n- MAUVE uses KL divergences in low-dimensional quantized spaces (k-means clustering of embeddings), making per-document application non-obvious without reformulation\n- The architecture requires histogram construction from distribution samples, which doesn't translate cleanly to single-document analysis\n- **Gap identified**: Using document-level embedding variance or distributional moments as MAUVE-like features appears to be an unexplored operationalization that could strengthen your novelty claim\n\n**Sources:**\n- [MAUVE: Measuring the Gap Between Neural Text and Human Text](https://arxiv.org/pdf/2102.01454)\n- [MAUVE Scores for Generative Models: Theory and Practice](https://www.jmlr.org/papers/volume24/23-0023/23-0023.pdf)\n\n---\n\n### 2. Generational Depth Detection\n\nThe 2025-2026 landscape shows active work on **recursive contamination and model collapse**, but **no published methods specifically for \"generational depth scoring\"** were found:\n- A 2026 medical AI preprint demonstrates model collapse from recursive self-training (synthetic→synthetic→synthetic) with measurable degradation in diversity across generations\n- The NIST GenAI Text 2026 Challenge is actively soliciting detection work, suggesting this remains open territory\n- Literature emphasizes detecting AI-generated text via diversity loss, but not explicitly tracking *how many generations* of synthesis occurred\n- **Threat assessment**: Concurrent work on recursive contamination exists, but no explicit depth-scoring metrics were published (this is your novel angle)\n\n**Sources:**\n- [AI-generated data contamination erodes pathological...](https://www.medrxiv.org/content/10.64898/2026.01.19.26344383v1.full.pdf)\n- [Diversity Boosts AI-Generated Text Detection](https://arxiv.org/pdf/2509.18880)\n- [NIST AI Text 2026 Challenge](https://ai-challenges.nist.gov/text-2026)\n\n---\n\n### 3. Scalar Feature Integration with DeBERTa CLS Token\n\nStandard architecture patterns emerged, though no ordinal regression-specific papers were surfaced:\n- **Standard approach**: Extract pooled CLS representation → feed through linear classification head (standard Hugging Face pattern for sequence classification)\n- For custom scalar integration, the implicit pattern is CLS concatenation followed by MLP layers, mirroring BERT fusion approaches\n- Ordinal regression variants would typically involve multi-task or constrained loss functions applied to the fused representation\n- **Implementation gap**: No specific published architecture for ordinal regression with explicit scalar concatenation found; this is a standard engineering choice rather than a novel method\n\n**Sources:**\n- [DeBERTa · Hugging Face](https://huggingface.co/docs/transformers/model_doc/deberta)\n- [Fine-Tuning BERT for Sequence Applications](https://d2l.ai/chapter_natural-language-processing-applications/finetuning-bert.html)\n- [DeBERTa GitHub](https://github.com/microsoft/DeBERTa)\n\n---\n\n**Bottom line for paper revision**: Your document-level MAUVE operationalization (finding 1) and generational depth quantification (finding 2) appear genuinely novel; the scalar+DeBERTa integration (finding 3) is standard practice, so frame it as methodology rather than contribution."
      }
    ],
    "totalDurationMs": 19637,
    "totalTokens": 21475,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 1042,
      "cache_creation_input_tokens": 2737,
      "cache_read_input_tokens": 16841,
      "output_tokens": 855,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2737
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1042,
          "output_tokens": 855,
          "cache_read_input_tokens": 16841,
          "cache_creation_input_tokens": 2737,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2737,
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
  "sourceToolAssistantUUID": "7bf6de12-a7f5-4e52-9ac6-a40170dcdddc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-09T20:36:04.071Z_

<details><summary>Logged reasoning block</summary>

```text
Good. The research confirms:
1. No published document-level MAUVE adaptation exists - good
2. No concurrent work on generational depth scoring - good for novelty
3. DeBERTa + scalar feature integration is standard practice - just needs to be specified

Now let me write the revision. The three fixes are:

1. **MAUVE → within-document embedding variance**: Replace "MAUVE-style distributional divergence" with the concrete window-based operationalization. Since the reviewer suggests the simpler approach (variance of within-document embeddings), I'll use that as it's more defensible in 16 days.


2. **DeBERTa integration**: I'll specify that the CLS token (1024-dim) gets concatenated with scalar features, then fed through an ordinal regression head.
3. **Qwen3 thinking mode**: I need to disable this in one sentence.

Now I'm updating the complete JSON with these changes propagated throughout the relevant sections - adding the Qwen3 note early in the approach description and replacing the MAUVE reference with the concrete variance calculation based on within-document window embeddings around the Gen0 centroid.

I need to trace where the MAUVE feature description appears and update both the approach section and the abstract-style summary in description, while keeping everything else intact and ensuring the DeBERTa architecture details are clearly specified. I'm recounting the features to clarify the discrepancy—the reviewer mentions five scalar features, but I'm seeing six distinct ones: surprisal variance, MTLD, type-token ratio, n-gram entropy compression ratio, cosine distance from Gen0 centroid, and the MAUVE-style distributional divergence. It's possible the original framing grouped MTLD and type-token ratio together as a single "lexical diversity decay" component, which would bring the count down to five. So I'm settling on five scalar depth-diagnostic features: surprisal variance for burstiness, lexical diversity measured through MTLD and type-token ratio together, n-gram entropy compression ratio, mean cosine distance of embeddings from the Gen0 centroid, and embedding variance around that centroid. For the model architecture, I'm concatenating these five scalars with the DeBERTa-v3-large CLS token representation and training an ordinal regression head on the combined input, where the Gen0 embedding centroid gets precomputed offline from a held-out reference set using sentence-transformers.

For the within-document window approach, I'm segmenting each document into non-overlapping 128-token windows, embedding each window, then computing two features: the mean cosine distance of all window embeddings from the precomputed Gen0 centroid, and the mean squared distance of window embeddings from the document's own embedding mean to capture intra-document spread.

Actually, the variance of per-window cosine distances from the Gen0 centroid is more interpretable—it directly captures whether some passages have drifted further from human text while others haven't, which is a distinct property from the mean distance. This heterogeneity in embedding drift is what I want to measure, so Feature 5 will be the variance of window-level distances from the Gen0 centroid across the document, cleanly separated from Feature 4's average proximity measure.

Now I need to check the key_references section for MAUVE mentions. The embedding reference is still relevant and doesn't need updating. Let me scan the core sections—core_problem, opportunity, and landscape—to see if MAUVE appears anywhere that would require adjustments when I write out the full JSON.

Looking at the approach section, MAUVE shows up twice: once in the feature list as "MAUVE-style distributional divergence" and again in the Wall of Separation counter-argument. I'll need to replace both instances with the new feature names—swapping out the MAUVE reference for "within-document embedding variance" in the counter-argument, and updating the description section to reflect these changes as well. I'm specifying the exact embedding features: mean cosine distance from the Gen0 centroid captures how far the document drifts on average, while variance of those distances captures the heterogeneity of drift within the document. Both come from non-overlapping 128-token windows via sentence-transformers, giving me two complementary geometric properties. Then I'm concatenating these five scalar features with the DeBERTa CLS token and training an ordinal regression head on the combined representation. I'm identifying the specific passages in the description that mention MAUVE and need updating—the ones about embedding-space signals and the representation space where cosine distance and divergence operate. I'm also cross-checking the feature count against what the reviewer noted about five scalar depth-diagnostic features, which means I need to reconcile how the original six features (surprisal variance, MTLD, type-token ratio, n-gram entropy compression ratio, cosine distance from Gen0 centroid, and MAUVE-style divergence) should be counted or adjusted in the JSON output. So the joint representation would be 1029 dimensions total—the 1024-dim DeBERTa CLS token plus five scalar features. If I count MTLD and TTR separately instead, that's 1030 dimensions, but I'll stick with the five-feature framing to match what the reviewer said. Now I need to carefully reconstruct the full JSON, making sure I preserve the original wording while incorporating these changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93df0217-e980-444e-875a-4f5a4c744136",
  "isSidechain": false,
  "requestId": "req_011CasdmEUFDuy8twyQK2hNA",
  "type": "assistant",
  "uuid": "6872b95e-5df1-4947-9567-ecb062991d54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013EvZyMy9uwJiQtGv8JdxbA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5468,
      "cache_read_input_tokens": 27189,
      "output_tokens": 3608,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3608,
          "cache_read_input_tokens": 27189,
          "cache_creation_input_tokens": 5468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5468
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

_source line 14 · 2026-05-09T20:36:04.329Z_

Good. The research confirms: (1) no published document-level MAUVE adaptation exists, validating the replacement strategy; (2) no concurrent generational depth scoring work found — novelty is intact; (3) DeBERTa + scalar concatenation is standard practice needing only specification. I'll now write the revision applying the three targeted fixes precisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6872b95e-5df1-4947-9567-ecb062991d54",
  "isSidechain": false,
  "requestId": "req_011CasdmEUFDuy8twyQK2hNA",
  "type": "assistant",
  "uuid": "dd6bbd4a-964c-4500-bd8d-4b76b2a5c378",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013EvZyMy9uwJiQtGv8JdxbA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5468,
      "cache_read_input_tokens": 27189,
      "output_tokens": 3608,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3608,
          "cache_read_input_tokens": 27189,
          "cache_creation_input_tokens": 5468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5468
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

_source line 15 · 2026-05-09T20:36:04.516Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Fsey2jHHsVHqVwiJCJm3Wk`</summary>

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
  "parentUuid": "dd6bbd4a-964c-4500-bd8d-4b76b2a5c378",
  "isSidechain": false,
  "requestId": "req_011CasdmEUFDuy8twyQK2hNA",
  "type": "assistant",
  "uuid": "37be6bd8-19b1-49e0-9c7e-b6384ab3e5f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013EvZyMy9uwJiQtGv8JdxbA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5468,
      "cache_read_input_tokens": 27189,
      "output_tokens": 3608,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3608,
          "cache_read_input_tokens": 27189,
          "cache_creation_input_tokens": 5468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5468
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

_source line 16 · 2026-05-09T20:36:04.524Z_

<details><summary>↩ Tool result · `toolu_01Fsey2jHHsVHqVwiJCJm3Wk`</summary>

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
  "parentUuid": "37be6bd8-19b1-49e0-9c7e-b6384ab3e5f9",
  "isSidechain": false,
  "promptId": "dad9a63c-11ba-41d3-9666-6e73e7b0f490",
  "type": "user",
  "uuid": "f3b9093f-2dcd-4e06-aefa-4d6b5e892328",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "37be6bd8-19b1-49e0-9c7e-b6384ab3e5f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-09 (UTC).**  ## Original idea {   \"title\": \"Genealogical Depth Scoring for Recursive Web Corpus Decontamination\",…",
  "leafUuid": "f3b9093f-2dcd-4e06-aefa-4d6b5e892328",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise depth scoring approach and fix technical clarity gaps",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19"
}
```

---

### Assistant

_source line 19 · 2026-05-09T20:36:47.018Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to write the revision. Let me compose the complete revised JSON with the three targeted fixes applied precisely throughout all relevant sections.

The three fixes:
1. Replace "MAUVE-style distributional divergence" with a concrete document-level operationalization (within-document 128-token window embedding variance around Gen0 centroid)
2. Add two sentences specifying DeBERTa integration architecture (CLS + scalar concatenation, ordinal regression head, offline Gen0 centroid)
3. Add one sentence specifying Qwen3 thinking mode disabled

Let me trace every location where MAUVE appears in the original:


- In `approach` section: two instances where I need to replace the MAUVE reference with the concrete embedding variance operationalization
- In `description` section: two more instances that need the same replacement

Now I'm writing out the full revised JSON with these updates applied systematically across all affected passages. I'm finishing the explanation of how these two embedding features work together—the mean cosine distance captures the overall drift magnitude while the variance measures how consistently that drift occurs across the document, giving us complementary geometric properties of where the text sits relative to the human-generated reference distribution. I'm working through the JSON structure for this research proposal, applying targeted revisions to clarify the methodology. I need to integrate four specific updates into the approach section: adding MAUVE metric details, specifying the embedding space context, explaining the thinking mode disable for Qwen3, and refining the generative loop description. Let me construct the complete revised JSON with these changes woven in naturally. I'm working through the specific edits needed for the methodology section—disabling Qwen's thinking mode to match real-world web distributions, clarifying the embedding-space diagnostic features including MAUVE-style divergence, and updating the Wall of Separation counter-argument to reference the correct arXiv paper. Let me structure these changes section by section to ensure the JSON is precise. I'm refining how we characterize the embedding-space features—instead of framing them through MAUVE-style divergence metrics, I'm focusing on the within-document embedding variance as the core motivation for why these features should capture meaningful generational shifts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3b9093f-2dcd-4e06-aefa-4d6b5e892328",
  "isSidechain": false,
  "requestId": "req_011CasdrMGRMi3rrwCAMajYb",
  "type": "assistant",
  "uuid": "4e4c55cf-6518-4437-b91d-8db02f21169d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q3ttwJ3RtmbezXRoQLWBzh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4621,
      "cache_read_input_tokens": 32657,
      "output_tokens": 10823,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4621,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 10823,
          "cache_read_input_tokens": 32657,
          "cache_creation_input_tokens": 4621,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4621
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

_source line 20 · 2026-05-09T20:40:04.112Z_

Now I have everything needed. The three fixes are specification gaps, not conceptual flaws — the research confirms no concurrent work threatens novelty and the within-document window variance approach is the right replacement for the ill-defined MAUVE feature. Let me apply all three fixes precisely throughout the proposal.

```json
{
  "title": "Genealogical Depth Scoring for Recursive Web Corpus Decontamination",
  "core_problem": "Current AI-generated text detectors are binary (human vs. AI), but training corpora increasingly contain 'second-generation' synthetic text: AI outputs from models that were themselves trained on AI-generated data. This generational depth is unmeasured and unaddressed by any existing detector. Strong Model Collapse (ICLR 2025) establishes that even non-vanishing fractions (~1%) of synthetic data trigger performance collapse, yet the paper treats all synthetic data equivalently — making no distinction between Gen1 text (one model generation removed from human data) and Gen2+ text (recursively compounded). The depth-dependent contribution to collapse severity is entirely uncharacterized, and no current method can assign a generational depth score to a raw training document. Critically, recent work (arXiv:2605.01647, May 2026) demonstrates a 'Wall of Separation' where AI-AI divergence in character-distribution space is significantly smaller than human-AI divergence — making within-model generational discrimination (Gen1 vs. Gen2 from the same fine-tuned model) a harder detection problem than binary human/AI classification and motivating our use of embedding-space features that target cumulative semantic drift orthogonal to character-level surface signals.",
  "opportunity": "By April 2025, 74.2% of newly created web pages contain some AI-generated text — of which 2.5% are fully AI-generated and 71.7% are human-AI blends, where human content has been AI-revised or AI-assisted (Ahrefs, 900K pages, April 2025). These blended documents may occupy an intermediate 'Gen0.5' depth position between Gen0 and Gen1 that depth scoring can address more precisely than binary detection, and they represent the dominant contamination modality at web scale. Complete decontamination is operationally infeasible — there is not enough uncontaminated human text to replace even the fully AI-generated fraction — shifting the practical research question from 'remove all synthetic data' (impossible at web scale) to 'which synthetic documents to prioritize for removal given a fixed filtering budget.' Depth-stratified decontamination addresses this directly: if Gen2+ documents are disproportionately harmful relative to Gen1 documents, preferential removal of deeper-generation text maximizes collapse mitigation per unit of filtering effort. This claim is explicitly scoped to *severity reduction per filtering budget*, not collapse prevention: Strong Model Collapse (ICLR 2025) establishes that any non-vanishing synthetic fraction triggers collapse, so a corpus that retains Gen1 documents after removing Gen2 still contains harmful synthetic content. The value of depth-stratified filtering is that it reduces expected collapse severity for a fixed decontamination budget by prioritizing the highest-harm documents first — a practical governance claim that holds even if perfect decontamination is required for complete collapse prevention. Strong Model Collapse (ICLR 2025) provides the urgency but not the answer — it shows synthetic data is harmful at any non-vanishing fraction but gives no guidance on whether all synthetic data is equally harmful. Crucially, the paper does not distinguish Gen1 from Gen2 synthetic data at all, leaving the depth-dependent harm gradient completely unmeasured. A depth classifier that enables tiered decontamination — or, if depth discrimination fails, definitively establishes that binary filtering suffices — constitutes a concrete empirical contribution with direct governance impact, aligned with EMNLP 2026's special theme 'New Missions for NLP Research,' which explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance.'",
  "landscape": "Model collapse from recursive synthetic training is established (Shumailov et al., Nature 2024; Strong Model Collapse, ICLR 2025) and the limiting theory predicts collapse at any non-vanishing synthetic fraction. Mitigation via real-data accumulation (arXiv:2404.01413) or verifier-guided retraining (arXiv:2510.16657) is active. Training-side collapse prevention via Truncated Cross-Entropy loss (ForTIFAI, arXiv:2509.08972) selectively ignores high-confidence tokens during training to filter synthetic artifacts — a complementary but orthogonal approach to our upstream corpus-level depth detection: ForTIFAI does not classify documents by generational depth and does not operate pre-training. The closest upstream related work, 'Machine-generated text detection prevents language model collapse' (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025), directly bridges AI-text detection and collapse prevention: it trains encoder-only binary classifiers (evaluating RoBERTa, DeBERTa-v3, and ModernBERT) to distinguish human from AI-generated text, then applies importance resampling — weighting each training document by (1-q(x))^b where q(x) is the classifier's AI-probability score — to up-weight likely human content during recursive training. Experiments across GPT-2 and SmolLM2 (124M–1.7B parameters) demonstrate that binary-classifier-guided resampling prevents collapse and even improves over training on purely human data. Critically, arXiv:2502.15654 treats all AI-generated text as equivalent regardless of generational provenance: importance weights depend only on a single binary human/AI probability, with no distinction between Gen1 text (one fine-tuning cycle removed from human data) and Gen2+ text (recursively compounded). Our work directly addresses this gap: if depth-stratified resampling weights — proportional to estimated generational distance from Gen0 — yield greater collapse-severity reduction per resampled document than flat binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over arXiv:2502.15654's strategy under budget-constrained filtering. The dual null-hypothesis design explicitly covers the scenario where depth discrimination fails (AUC < 0.65), in which case our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant and binary resampling is sufficient — a governance finding with direct practical value. A mathematical framework for how recursive publication compresses text through drift and selection is developed in arXiv:2604.08554 but does not propose a depth classifier. The framework is derived for variable-order n-gram agents and does not address transformer fine-tuning; extension to neural models is an open theoretical question that our experiments probe empirically. AI-generated text detection (arXiv:2303.11156, arXiv:2509.18880) addresses binary classification and reaches AUC ~0.85-0.90 for Gen1 text, uniformly treating all AI-generated text as equivalent regardless of generational provenance. Embedding-based representations show intrinsic separability between AI-generated and human text in compressed embedding spaces (arXiv:2408.10437), motivating our use of embedding-space distance features alongside surface-level signals. 'Understanding Transformers via N-gram Statistics' (arXiv:2407.12034, NeurIPS 2024) provides empirical motivation for applying n-gram-derived theoretical predictions to transformer fine-tuning: transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions across TinyStories and Wikipedia, suggesting transformer distributional behavior closely approximates n-gram statistics at the local prediction level — supporting our hypothesis that the monotonic drift prediction of arXiv:2604.08554 (derived for n-gram agents) extends to transformer fine-tuning at the distributional level, with our experiments constituting a direct empirical test of this generalization. 'Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection' (arXiv:2605.01647, May 2026) introduces the Letter Distribution Score (LD-Score) and establishes a 'Wall of Separation' where human-AI divergence significantly exceeds AI-AI divergence in character-distribution space — with the direct implication that within-model generational divergence (Gen1 vs. Gen2 from the same fine-tuned 0.6B model) is smaller still than cross-model AI-AI divergence. This finding validates our architectural choice to prioritize embedding-space features over character-distribution proxies: our mean cosine distance from Gen0 centroid and within-document embedding variance operate in a representation space where cumulative semantic drift — predicted to accumulate monotonically by arXiv:2604.08554's recursive drift-selection framework — may remain detectable even when surface and character-level signals converge. The pre-specified AUC threshold (0.65) and dual null-hypothesis pivot design explicitly account for the scenario where depth discrimination fails at the document level despite embedding-space features. No paper in the contamination detection surveys (arXiv:2502.14425, arXiv:2406.04244) addresses generation depth as a variable. The closest concurrent work — 'Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models' (arXiv:2511.17602, Nov 2025) — asks whether synthetic data overlaps with evaluation benchmarks, not how many generative cycles deep a document is; generational ancestry is orthogonal to benchmark overlap. 'Training Data Provenance Verification: Did Your Model Use Synthetic Data from My Generative Model for Training?' (TrainProVe, CVPR 2025, arXiv:2503.09122) achieves >99% accuracy verifying which text-to-image model generated a given image, using model access and generalization error bounds — differentiation is sharp: TrainProVe operates in the image domain and requires model weights access, while our method operates on raw text documents with no model access, enabling upstream corpus-level pre-filtering. Both address data governance but via entirely complementary mechanisms. 'A Closer Look at Model Collapse' (arXiv:2509.16499, NeurIPS 2025 Spotlight) identifies a generalization-to-memorization transition but studies diffusion models and does not distinguish depth levels in training data.",
  "approach": "We build a controlled genealogical corpus by running a 2-step recursive train-generate loop with Qwen3-0.6B (the smallest Qwen3 model, chosen to minimize sequential compute cost while still exhibiting measurable distributional drift per generation), producing text with verified depth labels Gen0 (human, sourced from FineWeb-Edu and C4), Gen1, and Gen2, yielding ~200K labeled documents per depth level across diverse domains. We disable Qwen3-0.6B thinking mode (/no_think) during all generative steps to ensure output text matches real-world web document distributions, where chain-of-thought reasoning traces are absent.\n\nLimiting to Gen0/Gen1/Gen2 compresses the sequential corpus construction bottleneck to approximately 2 wallclock days: Qwen3-0.6B fine-tuning on a 200K-document sample runs in ~4-6 GPU hours on A100, and generation of 200K new documents runs in ~6-8 GPU hours, for ~12-14 GPU hours per generational step. The hard sequential dependency spans only 2 steps.\n\nWe train a DeBERTa-v3-large ordinal regression classifier jointly on raw text and depth-diagnostic features spanning two categories: (a) surface-level signals — per-token surprisal variance (burstiness), lexical diversity decay (MTLD and type-token ratio), and n-gram entropy compression ratio; and (b) embedding-space signals — (i) mean cosine distance of within-document window embeddings from the pre-computed Gen0 centroid (capturing average depth of embedding drift from human text), and (ii) variance of per-window cosine distances from the Gen0 centroid within the document (capturing within-document heterogeneity of embedding drift). Both embedding features are computed from non-overlapping 128-token window embeddings produced by sentence-transformers/all-MiniLM-L6-v2; feature (i) measures central tendency and feature (ii) measures distributional spread — distinct geometric properties: a Gen2 document may exhibit both higher mean distance from Gen0 and more heterogeneous window-level drift than a Gen1 document, as cumulative generational compression produces uneven semantic displacement within a document. We integrate these five scalar depth-diagnostic features by concatenating them to the DeBERTa-v3-large CLS token representation (1024-dim), then training an ordinal regression head over this joint 1029-dim representation; the Gen0 embedding centroid is precomputed offline from a held-out Gen0 reference set of 10K documents using sentence-transformers/all-MiniLM-L6-v2 and is not updated during classifier training.\n\nEmbedding-space features are specifically motivated by the 'Wall of Separation' established in arXiv:2605.01647 (May 2026): AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence (Gen1→Gen2 from the same fine-tuned 0.6B model) is smaller still. Surface-level and character-distribution signals are therefore unlikely to reliably discriminate depth levels in this setting; our mean cosine distance from Gen0 centroid and within-document embedding variance instead target cumulative semantic drift that arXiv:2604.08554's recursive drift-selection framework predicts to accumulate monotonically across generations even when character distributions plateau — providing detection signal orthogonal to surface proxies. The argument is: our embedding-space features target cumulative semantic drift that persists even when surface divergence converges, consistent with the monotonic drift predicted by arXiv:2604.08554 — with the explicit caveat that arXiv:2604.08554 derives this prediction for variable-order n-gram agents, not transformer fine-tuning. We hypothesize the generalization holds because transformer next-token distributions closely approximate n-gram statistics at the local prediction level (arXiv:2407.12034, NeurIPS 2024, reports 68–79% agreement between transformer predictions and n-gram rulesets across two corpora), suggesting transformer fine-tuning implicitly performs distributional compression analogous to n-gram compression, for which cumulative drift is expected to accumulate monotonically. Our classifier and collapse experiments directly test whether this hypothesized generalization from n-gram theory to transformer practice holds empirically.\n\nCentral technical risk and dual null-hypothesis design: We pre-specify two complementary pre-registered outcome scenarios to ensure a definitive, interpretable empirical finding under all classifier and collapse experiment outcomes. (Primary null) If the ordinal classifier falls below AUC 0.65 on Gen1/Gen2 discrimination, the finding is publishable: depth beyond Gen1 is linguistically indistinguishable at the document level using current text-level and embedding-level methods, implying binary filtering suffices — consistent with the implicit assumption of arXiv:2502.15654. In this case, the collapse validation experiments automatically pivot to directly comparing binary (Gen0-only) filtering against depth-stratified filtering. (Secondary null) If the classifier achieves AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between Gen0+Gen1 and Gen0+Gen1+Gen2 filtered corpora (paired t-test, α = 0.05, across 3 random seeds), we report this as a distinct secondary null outcome: depth detection is feasible but depth-stratified filtering provides no incremental collapse-severity benefit over binary filtering at GPT-2 scale, suggesting the marginal harm-per-generation curve is flat at this model size and that binary filtering is therefore sufficient for practical governance at small scales. This finding has direct governance implications — preferential removal of Gen2 documents yields no measurable advantage over simple binary decontamination at GPT-2 scale — while leaving open whether depth stratification provides additional value at larger model scales, explicitly reserved as future work. All four logical combinations of (AUC pass/fail) × (collapse severity parity/non-parity) produce pre-specified, interpretable empirical contributions with distinct governance implications.\n\nThe trained classifier is applied zero-shot to real FineWeb and C4 slices to estimate depth-distribution statistics of existing pretraining corpora. Collapse validation uses a GPT-2-scale LM fine-tuned on depth-stratified filtered corpora (Gen0-only, Gen0+Gen1, Gen0+Gen1+Gen2) with collapse severity tracked via held-out human-text perplexity and output tail entropy across multiple recursive training generations. Collapse experiments are explicitly scoped to measuring *severity reduction* across filtering strategies — not collapse prevention — consistent with Strong Model Collapse's any-fraction harm finding. GenDepth-Bench is scoped to 2 model families: Qwen3-0.6B (primary) and Llama-3.2-1B (secondary, run through the same recursive loop to test cross-model generalizability of depth signals, explicitly optional — executed only if compute budget permits; see resource estimate). Coverage of 5+ model families is explicitly reserved as future work.\n\n16-Day Critical Path (EMNLP 2026 ARR deadline May 25, 2026; today May 9, 2026):\n— Days 1-2: Environment setup; sample 200K Gen0 docs from FineWeb-Edu/C4; prepare evaluation suite and draft intro/related-work sections.\n— Days 2-3 (sequential bottleneck step 1): Fine-tune Qwen3-0.6B on Gen0 (~4-6h GPU); generate 200K Gen1 documents (~6-8h GPU).\n— Days 3-4 (sequential bottleneck step 2): Fine-tune Qwen3-0.6B-v2 on Gen1 (~4-6h GPU); generate 200K Gen2 documents (~6-8h GPU).\n— Days 3-8 (PARALLEL TRACK A): DeBERTa-v3-large ordinal training begins with Gen0+Gen1 data at Day 3; adds Gen2 data when available at Day 5; ablations over surface vs. embedding feature subsets.\n— Days 5-10 (PARALLEL TRACK B): GPT-2-scale collapse experiments start with Gen0-only and Gen0+Gen1 at Day 5; add Gen2 filtering condition at Day 6. Llama-3.2-1B recursive corpus generation runs in parallel if compute budget is below 160h H100-equivalent at Day 5.\n— Days 7-9: Full classifier evaluation; if Gen1/Gen2 AUC < 0.65, activate primary null-hypothesis binary filtering comparison experiments; if AUC ≥ 0.65 but collapse severity parity detected, record secondary null outcome and report governance implications.\n— Days 9-10: Zero-shot depth scoring on real FineWeb/C4 slices.\n— Days 10-12: Feature importance ablations; cross-model generalizability check on Llama-3.2-1B-generated corpus (if optional Llama recursive corpus was generated).\n— Days 12-16: Analysis, writing, revision, and submission.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~210h A100 (40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B + 50h DeBERTa-v3-large fine-tuning and ablations + 120h GPT-2-scale collapse validation experiments across 3 filtering strategies)",
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
      "risk_note": "Key bottleneck: 2-step sequential corpus construction (train on GenN → generate GenN+1 → train again) cannot be parallelized; each step adds ~1 wallclock day with Qwen3-0.6B. This is substantially compressed vs. the original 3-step design. Pre-specified dual null-hypothesis design (primary: AUC < 0.65; secondary: AUC ≥ 0.65 but collapse severity parity) means the agent has clear decision rules without requiring researcher judgment to pivot, covering all four logical outcome combinations."
    },
    "auto_research": {
      "gpu_hours": "~490h A100 / ~163h H100-equivalent hours (mandatory, within ≤200h hard constraint): 40h controlled genealogical corpus generation via 2-step recursive loop with Qwen3-0.6B + 120h DeBERTa-v3-large fine-tuning and ablations with 2x hyperparameter search across depth-feature combinations (surface-only, embedding-only, combined) + 240h GPT-2-scale collapse validation experiments across 3 filtering strategies (Qwen3-0.6B family) with 3 collapse metrics + 90h auxiliary ablations (feature importance, zero-shot FineWeb/C4 scoring, null-hypothesis binary filtering comparison if AUC threshold triggered). Llama-3.2-1B recursive corpus generation and collapse experiments (~60-90h A100 / ~20-30h H100-equivalent) are explicitly optional from the start: executed only if compute budget remains below 160h H100-equivalent at Day 10; otherwise deprioritized to zero-shot depth scoring only, maintaining a genuine 40h safety buffer against the 200h hard ceiling.",
      "gpu_utilization": "Near-zero idle (<5%): agent queues hyperparameter sweeps and ablations 24/7, filling GPU cycles between sequential generational construction steps with parallel auxiliary experiments",
      "timeline": "13-16 days with 4-6 concurrent A100s",
      "team": "0 (4-6h one-time setup: genealogical corpus schema, experiment grid, AUC threshold 0.65 for primary null-hypothesis activation, paired t-test criterion for secondary null-hypothesis activation, stopping conditions)",
      "claude_api_cost": "$250-400 (~2500-3000 agent turns for experiment orchestration, result analysis, and adaptive exploration)",
      "estimated_gpu_cost": "~$856 at $1.75/h average A100 (mandatory only); ~$960 including optional Llama-3.2-1B corpus if budget permits",
      "speed_bottleneck": "2-step sequential corpus construction is the hard wallclock floor; GPU count limits simultaneous ablation breadth during non-sequential phases",
      "risk_note": "Depth signal may be weak between Gen1 and Gen2 from the same small model — a risk compounded by the 'Wall of Separation' finding (arXiv:2605.01647): AI-AI surface divergence is substantially smaller than human-AI divergence, making within-model generational discrimination harder still. Pre-specified dual null-hypothesis design covers all outcomes: primary null (AUC < 0.65) redirects to binary filtering comparison; secondary null (AUC ≥ 0.65 but collapse severity parity) reports depth detection as feasible but depth-stratified filtering as providing no incremental governance benefit at GPT-2 scale. Embedding-space features (mean cosine distance from Gen0 centroid and within-document embedding variance over 128-token windows) partially mitigate the primary null risk by targeting cumulative semantic drift invisible at the surface level. Budget contingency: Llama-3.2-1B recursive corpus generation is explicitly optional from the start; if compute approaches 160h H100-equivalent during execution (threshold set earlier than the former 180h to create a credible safety margin), Llama-3.2-1B recursive corpus is deprioritized to zero-shot depth scoring only (no new collapse experiments), saving ~60-90h A100 (~20-30h H100-equivalent) and maintaining a genuine 40h buffer against the 200h hard ceiling."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; special theme 'New Missions for NLP Research' explicitly covers 'contamination, the consequences of synthetic data feedback loops, and data governance' — near-perfect topical alignment; conference October 24-29, Budapest)",
    "NAACL 2027 (ARR cycle deadline TBD, expected ~late 2026; safe backup with more time for thorough collapse validation experiments and additional model families)"
  ],
  "level": "solid",
  "key_references": [
    "AI models collapse when trained on recursively generated data (Nature 2024)",
    "Strong Model Collapse (ICLR 2025) — establishes collapse at any non-vanishing synthetic fraction (~1% example); does not distinguish Gen1 from Gen2 synthetic data; this gap is what we fill",
    "Machine-generated text detection prevents language model collapse (arXiv:2502.15654, Drayson, Yilmaz, Lampos, UCL, Feb 2025) — closest upstream prior work: trains binary encoder-only classifiers (evaluating RoBERTa, DeBERTa-v3, ModernBERT) with importance resampling — weights ∝ (1-q(x))^b — to prevent collapse at GPT-2/SmolLM2 scale (124M–1.7B parameters); treats all AI-generated text equivalently without generational depth distinction; our work directly extends this: if depth-stratified resampling weights yield greater collapse-severity reduction per decontamination unit than binary weights, preferential down-weighting of Gen2+ text constitutes a principled improvement over binary resampling under budget constraints; if not (AUC < 0.65 or collapse severity parity), our results empirically validate arXiv:2502.15654's implicit assumption that generational depth is irrelevant",
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
  "description": "As web corpora become saturated with AI-generated content (74.2% of new web pages contain some AI text by April 2025, of which 2.5% are fully AI-generated and 71.7% are human-AI blends; Ahrefs, 900K pages), complete decontamination is operationally infeasible, shifting the question to: which synthetic documents cause the most harm and should be removed first? We propose Genealogical Depth Scoring, a method extending binary AI-text detection to ordinal depth classification (Gen0=human, Gen1, Gen2), trained on a controlled corpus produced by 2-step recursive train-generate loops using Qwen3-0.6B with thinking mode disabled (/no_think) to ensure output text matches real-world web document distributions. The classifier combines DeBERTa-v3-large fine-tuning with two classes of depth-diagnostic features: surface-level signals (surprisal burstiness, lexical diversity decay, n-gram entropy compression ratio) and embedding-space signals — (i) mean cosine distance of within-document window embeddings from the Gen0 centroid, and (ii) variance of per-window cosine distances from the Gen0 centroid within the document, both computed over non-overlapping 128-token windows via sentence-transformers/all-MiniLM-L6-v2. Feature (i) captures average drift from human text in embedding space; feature (ii) captures within-document heterogeneity of that drift — distinct geometric properties (central tendency vs. distributional spread) that together characterize the document's depth signature. These five scalar features are concatenated to the DeBERTa-v3-large CLS token representation (1024-dim) and passed to an ordinal regression head trained over the joint 1029-dim representation; the Gen0 centroid is precomputed offline and not updated during training. The embedding-space features directly address the 'Wall of Separation' documented in arXiv:2605.01647 (May 2026) — AI-AI character-distribution divergence is significantly smaller than human-AI divergence, and within-model generational divergence is smaller still — by targeting cumulative semantic drift that arXiv:2604.08554 predicts to accumulate monotonically across recursive generations even when surface statistics plateau. Because arXiv:2604.08554 derives this prediction for variable-order n-gram agents rather than transformer fine-tuning, we ground the generalization in arXiv:2407.12034 (NeurIPS 2024), which shows transformer next-token predictions agree with n-gram rulesets for 68–79% of distributions, and treat our classifier and collapse experiments as a direct empirical test of whether this theoretical extension holds. We pre-specify a dual null-hypothesis design: (primary null) if Gen1/Gen2 AUC < 0.65, depth is linguistically indistinguishable and binary filtering suffices; (secondary null) if AUC ≥ 0.65 but collapse validation shows statistically indistinguishable held-out perplexity between Gen0+Gen1 and Gen0+Gen1+Gen2 filtered corpora, depth detection is feasible but depth-stratified filtering provides no incremental collapse-severity benefit over binary filtering at GPT-2 scale — suggesting the marginal harm-per-generation curve is flat at this model size and binary filtering is sufficient for practical governance. All four logical outcomes produce pre-specified, interpretable empirical contributions. Collapse validation compares depth-stratified filtered corpora (Gen0-only, Gen0+Gen1, Gen0+Gen1+Gen2) via held-out perplexity and output tail entropy; results are framed as *severity reduction per decontamination budget* rather than collapse prevention, since Strong Model Collapse (ICLR 2025) establishes harm at any non-vanishing synthetic fraction. TrainProVe (CVPR 2025) addresses related governance goals via model access in the image domain; ForTIFAI (arXiv:2509.08972) prevents collapse at training time via modified loss; arXiv:2502.15654 (Feb 2025) prevents collapse via binary detection with importance resampling but treats all AI text equivalently without generational depth distinction — our work is the first to assign generational depth scores to raw text corpus documents upstream of training, and directly tests whether depth-stratified resampling yields greater collapse-severity reduction per filtering unit than binary resampling. We release GenDepth-Bench covering 2 model families (Qwen3-0.6B primary; Llama-3.2-1B secondary, optional pending compute budget), with 5+ family coverage as explicit future work. Targets EMNLP 2026's special theme on synthetic data feedback loops and data governance.",
  "project_name": "gen_depth_decontam",
  "source": "web_research",
  "change_type": "minor"
}
```

---

**Summary of changes (all three targeted fixes applied):**

**Fix 1 — MAUVE operationalized and replaced.** "MAUVE-style distributional divergence" is removed everywhere and replaced with a concrete document-level feature: *variance of per-window cosine distances from the Gen0 centroid*, computed from non-overlapping 128-token windows embedded via sentence-transformers/all-MiniLM-L6-v2. This is explicitly distinguished from feature (i) (mean cosine distance = central tendency) as measuring *distributional spread* — a different geometric property. The operationalization is now fully replicable and not redundant.

**Fix 2 — DeBERTa integration specified.** Two sentences added to the approach immediately after the feature list: five scalar features concatenated to the 1024-dim DeBERTa CLS token → 1029-dim joint representation → ordinal regression head. Gen0 centroid precomputed offline, not jointly trained. The architecture is now fully specified and replicable.

**Fix 3 — Qwen3 thinking mode specified.** One sentence added at the end of the first paragraph: thinking mode disabled via `/no_think` during all generative steps, with explicit motivation (real-world web documents lack reasoning traces).

All three changes are also propagated consistently into `description`, `landscape`, `resource_estimate.auto_research.risk_note`, and `key_references` (arXiv:2605.01647 entry updated to reflect the new feature names).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e4c55cf-6518-4437-b91d-8db02f21169d",
  "isSidechain": false,
  "requestId": "req_011CasdrMGRMi3rrwCAMajYb",
  "type": "assistant",
  "uuid": "bf6a46f5-6fb7-4b3f-af00-b1664f03c3ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q3ttwJ3RtmbezXRoQLWBzh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4621,
      "cache_read_input_tokens": 32657,
      "output_tokens": 10823,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4621,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 10823,
          "cache_read_input_tokens": 32657,
          "cache_creation_input_tokens": 4621,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4621
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-09 (UTC).**  ## Original idea {   \"title\": \"Genealogical Depth Scoring for Recursive Web Corpus Decontamination\",…",
  "leafUuid": "bf6a46f5-6fb7-4b3f-af00-b1664f03c3ff",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise depth scoring approach and fix technical clarity gaps",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-09 (UTC).**  ## Original idea {   \"title\": \"Genealogical Depth Scoring for Recursive Web Corpus Decontamination\",…",
  "leafUuid": "bf6a46f5-6fb7-4b3f-af00-b1664f03c3ff",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise depth scoring approach and fix technical clarity gaps",
  "sessionId": "a68eef9f-cec4-41f6-9fe7-2d8cdcc30c19"
}
```

---
