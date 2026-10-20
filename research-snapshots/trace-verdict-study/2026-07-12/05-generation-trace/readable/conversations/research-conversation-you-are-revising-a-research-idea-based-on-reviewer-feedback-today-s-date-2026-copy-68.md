# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/967cf362-df51-4fa3-8b99-78ae3dd47db6.jsonl`
- **Structured JSON:** [`214d7ce34a4af52cb22c.json`](../../sessions/21/214d7ce34a4af52cb22c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T07:47:03.576Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T07:47:03.576Z",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning\",\n  \"core_problem\": \"Cross-lingual instruction tuning for low-resource languages defaults to English as the sole pivot, creating systematic gaps for languages that are typologically distant from English—particularly those with agglutinative morphology, non-Latin scripts, or SOV word order. Three peer-reviewed ACL 2025 benchmarks—KazMMLU (Kazakh), MiLiC-Eval (Tibetan, Uyghur, Kazakh, Mongolian), and TUMLU (Turkic languages including Kazakh and Uyghur)—confirm that even frontier multilingual LLMs (GPT-4, Llama-3.1, Qwen-2.5) achieve near-random performance on Mongolian comprehension tasks and substantially below-par accuracy on Kazakh and Uyghur relative to typologically proximate high-resource languages. No existing instruction tuning method uses typological distance to continuously weight data-source selection across a multi-pivot mixture for these under-represented language families.\",\n  \"opportunity\": \"Three complementary ACL 2025 benchmarks provide peer-reviewed grounding for the performance gap. KazMMLU (arXiv:2502.12829; ACL 2025 long paper) comprises 23K Kazakh-language questions spanning STEM, humanities, and social sciences sourced from authentic educational materials; evaluation of Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 shows 'substantial room for improvement' for all models on Kazakh, despite the language having 20 million speakers. MiLiC-Eval (arXiv:2503.01150; ACL 2025 Findings) covers Tibetan, Uyghur, Kazakh, and Mongolian across 9 tasks with 24K instances; GPT-4o-mini achieves only slightly above random on Mongolian tasks, and models exhibit only 'preliminary understanding' of Tibetan and Kazakh. TUMLU (arXiv:2502.11020; ACL 2025 long paper) provides 38K native questions spanning 11 academic subjects across Turkic languages including Kazakh and Uyghur, enabling controlled within-family comparisons that isolate the effect of lower training corpus size. The XLM-SWCM paper (arXiv:2502.10852) additionally shows that encoder-based shared-weight cross-lingual pretraining partially bridges these gaps—Kazakh ROUGE-L summarization score of 5.6 is notably the lowest among the four minority languages studied—but this approach does not scale to instruction-following for decoder LLMs. CLO (arXiv:2505.14297; ACL 2025) shows that DPO-style cross-lingual preference optimization with only 3,200 samples outperforms standard SFT with 6,400 samples, establishing strong data efficiency for cross-lingual transfer. These findings together create a clear opening: by weighting instruction data from multiple source languages inversely by URIEL+ typological distance and introducing a staged curriculum, we can build a principled multi-pivot training regime that directly addresses the English-pivot bottleneck for agglutinative low-resource targets.\",\n  \"landscape\": \"PLUG (ACL 2024) established that English-pivot cross-lingual instruction generation improves multilingual instruction following—but its reported 29% improvement was measured on Chinese, Korean, Italian, and Spanish. Whether the English-pivot advantage holds for typologically distant agglutinative languages with non-Latin scripts (Kazakh, Mongolian, Uyghur) is an assumption that TWMP directly tests rather than takes for granted. CLO (arXiv:2505.14297; ACL 2025) improves data efficiency via DPO-style cross-lingual preference optimization using 6,400 OpenAssistant samples machine-translated by M2M100; it fixes English as the sole source language without varying source selection by typological distance. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh, English, Russian, and Turkish, and demonstrates that Turkish as an auxiliary language improves Kazakh performance—directly motivating TWMP's inclusion of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc four-language selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language, with principled pivot selection replacing language-specific engineering. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving a 12.72% average Win Rate improvement on X-AlpacaEval; it uses English as the sole source and implicit reward annotation without typological weighting—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from that work. 'Family Matters' (arXiv:2510.00810) applies language transfer and LoRA merging from typologically related Nordic languages to Faroese—demonstrating that typological proximity helps—but as a single-language case study with no generalizable training recipe. 'Cross-Linguistic Transfer in Multilingual NLP' (arXiv:2505.13908) analyzes language family and morphology effects empirically without proposing a training method. Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) decouples task and language LoRA adapters but does not use typological features to parameterize or weight the language adapter. 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678; Tianyu Liu et al., March 2026) introduces a DPO-inspired method—concurrent with TWMP—that enforces factual consistency of model responses across 26 languages and 9 LLMs; its preference pairs encode semantic equivalence of knowledge across languages (chosen = factually consistent cross-lingual response, rejected = factually inconsistent response). This objective is orthogonal to TWMP's: DCO addresses what the model says across languages (knowledge coherence), while TWMP addresses which language it responds in when given instructions in any of multiple pivot languages (instruction-language fidelity). DCO does not address low-resource instruction tuning, multi-pivot source selection, or typological-distance weighting. Two works require careful differentiation from TWMP. First, TIPA (arXiv:2601.16629; EACL 2026 Findings) constructs proxy language adapters by aggregating existing MAD-X adapters weighted by typological similarity across 230+ languages—entirely without training. TIPA is orthogonal to TWMP in three key ways: (1) it is training-free inference-time adapter aggregation, whereas TWMP learns from a typologically-weighted data curriculum; (2) it operates on encoder-based MAD-X modules for classification tasks, whereas TWMP targets decoder LLM instruction tuning; (3) TIPA has not been applied to instruction generation or to languages not already represented by a dedicated adapter. Second, 'Linguistically-Informed Multilingual Instruction Tuning' (arXiv:2410.07809) uses 289-dimensional legacy URIEL TYPO vectors with k-means clustering to select 14 discrete representative languages from a 52-language pool (one per cluster) for LoRA fine-tuning on Bactrian-X, showing that typologically diverse selection beats random selection. TWMP differs substantially: rather than discrete cluster-representative selection, TWMP applies continuous inverse-distance sampling weights over the full Aya collection using compact URIEL+ features (300-dim, Laplacian Score selected); it adds a staged cosine-distance curriculum schedule; it integrates a multi-source DPO preference optimization objective for language fidelity; and it directly targets Kazakh, Mongolian, and Uyghur—languages for which arXiv:2410.07809's evaluation suite (XNLI, XCOPA, XStoryCloze, XWinograd, PAWS-X) provides zero coverage. The combination of continuous URIEL+ weighting, staged curriculum, precisely formulated multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering the target languages constitutes a principled and differentiated advance.\",\n  \"approach\": \"We propose Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, which replaces PLUG's single-English pivot with a principled mixture over multiple source languages drawn from the Aya collection (513M instances across 114 languages).\\n\\nAya pivot coverage is verified before training: Turkish (high-resource, multi-million instances), Kyrgyz (~4.1M instances in the Aya collection language split), Uzbek (confirmed present as an underrepresented language with meaningful coverage), and Azerbaijani all qualify as pivot sources. A minimum threshold of 5,000 Aya instances per pivot language is enforced; languages below this threshold are excluded from the mixture. All qualifying pivot languages and their instance counts are reported in an appendix table. Kazakh, Mongolian, and Uyghur serve exclusively as evaluation targets and are never included in the pivot mixture.\\n\\nTypological distances are computed using URIEL+ (arXiv:2409.18472, COLING 2025; available via the urielplus Python library at github.com/LeeLanguageLab/URIELPlus) rather than the legacy lang2vec 289-dimensional binary features. URIEL+ expands coverage to 4,366 languages with approximately 800 features (607 grammar features covering syntactic and morphological dimensions, plus 193 sound features), and applies SoftImpute for missing-value imputation—critical for reducing sparsity in Kazakh, Uzbek, and Kyrgyz, where legacy URIEL features are known to be sparse. URIEL+ explicitly represents Kazakh's multi-script properties (Cyrillic, Latin, and Arabic) via script vectors. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), which demonstrates that a Laplacian Score 300-feature subset of URIEL+ achieves Spearman ρ=0.358 on typological alignment tasks versus ρ=0.260 for the full 800-feature set while also improving downstream cross-lingual NLP performance, we apply this feature selection before computing cosine distances. Data-sampling weights are assigned inversely proportional to these 300-feature URIEL+ cosine distances, so morphologically close pivots such as Turkish or Uzbek for Kazakh receive substantially higher weight than English.\\n\\nThe staged curriculum uses three phases calibrated by the empirical URIEL+ distance distribution of qualifying Aya pivot languages relative to each target language. Let D_25 and D_60 denote the 25th and 60th percentile distances from the target language to all qualifying Aya pivots (computed once, before training). Stage 1 (epochs 1–3): exclusively sources with cosine distance < D_25—for Kazakh, approximately ≤0.32, capturing Turkish, Kyrgyz, Uzbek, and Azerbaijani. Stage 2 (epochs 4–6): sources with distance < D_60 (approximately ≤0.56 for Kazakh), expanding to Russian, Arabic, and other mid-distance languages. Stage 3 (epochs 7–10): full mixture over all qualifying pivot languages with continuous inverse-distance weights. Thresholds are target-specific and computed from the actual Aya-pivot distance distribution; for Mongolian, where no Turkic pivot falls within D_25, the closest available Aya sources (Korean, Finnish, Turkish) are used across all three stages with correspondingly small weights—this distance-constrained Mongolian setting is a controlled finding of interest. Ablations compare: no curriculum (full weighted mixture from epoch 1), 2-stage (merging Stages 1–2), 3-stage (proposed), and linear interpolation between stages.\\n\\nThe CLO-style DPO preference optimization objective is precisely extended to the multi-source setting. For each source pivot language s_i and target language t, preference pairs are defined as: chosen = (x_{s_i}, y^w_t)—an instruction in source language s_i paired with a model-generated response identified as being in the target language t; rejected = (x_{s_i}, y^l_{s_i})—the same instruction paired with a model-generated response in source language s_i. This formulation promotes target-language responses to source-language instructions and differs from CLO's English-source objective in a critical respect: CLO's English-input pair (chosen=English response, rejected=target-language response) is designed to preserve English capability by penalizing cross-lingual output for English inputs. TWMP inverts this preference because the training goal is acquisition of cross-lingual target-language instruction following: for any source-language input, we want the model to respond in the target language. TWMP does not use CLO's second pair type (target-language input → prefer target-language response) because target-language training data is explicitly excluded.\\n\\nPreference pairs are constructed entirely without target-language labels via automatic language identification: given each source-language instruction x_{s_i}, we sample K=8 candidate responses from Qwen3.5-9B at temperature 0.7; apply fastText language identification (lid.176.bin) to each candidate; assign responses identified as the target language to the chosen pool and responses identified as the source language to the rejected pool; apply a minimum 20-token length gate to both pools to exclude degenerate or near-empty responses; pair the highest-scoring chosen (by fastText language ID confidence) with the lowest-scoring rejected per instruction. Instructions yielding no target-language candidates in K=8 samples after the length filter are discarded. An ablation row in the DPO evaluation table compares fastText-only selection (no length gate) against length-gated selection (≥20 tokens) to quantify the quality impact of this filter; this also characterizes the frequency of degenerate responses per source-target pair. As a mandatory prerequisite check, we run a 500-instruction probe per source-target language pair on the base Qwen3.5-9B and verify that target-language responses (meeting the ≥20-token gate) appear in >5% of K=8 samples; any pivot language pair failing this check is excluded from DPO training (falling back to SFT-weighted sampling only) for that target language. This probe is reported as a characterization result: for close Turkic pivots (Turkish→Kazakh), we expect the frequency to exceed 5% given Qwen3.5-9B's broad multilingual coverage; for distant pivots (English→Mongolian), the check may filter some source languages, which is informative about which pivots can drive DPO-based cross-lingual preference learning.\\n\\nWe apply QLoRA fine-tuning of Qwen3.5-9B (released March 2026; 248K-token vocabulary spanning 201 languages; the Qwen3.5 small series has 0.8B/2B/4B/9B variants—no 7B exists) on this weighted multi-pivot dataset, targeting Kazakh, Mongolian, and Uyghur as primary evaluation cases. Evaluation uses three ACL 2025 benchmarks: KazMMLU for Kazakh, MiLiC-Eval for all three targets across 9 tasks, and TUMLU for Kazakh and Uyghur within a controlled within-Turkic-family comparison. PLUG and CLO serve as primary baselines. Typological weighting ablations compare: full 800-feature URIEL+ vs. Laplacian-selected 300 features vs. syntax-only (474 features) vs. morphology-only (133 features) vs. the k-means discrete selection baseline from arXiv:2410.07809. Swahili serves as a held-out agglutinative generalization target not used during hyperparameter design. Note: TyDi QA covers Arabic, Bengali, Finnish, Indonesian, Japanese, Kiswahili, Korean, Russian, Telugu, and Thai—it does not include Kazakh, Mongolian, or Uyghur and is not used here.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~200h A100 (15–20 QLoRA runs × 10–13h each on Qwen3.5-9B, covering 3 primary target languages, PLUG/CLO baselines, URIEL+ sub-space ablations, curriculum schedule variants, DPO quality gate ablation row, and DPO prerequisite probe runs)\",\n      \"gpu_utilization\": \"LOW (~25–35%): GPU sits idle during code writing, debugging, data pipeline work, result analysis, and paper writing; runs are launched manually and often queue overnight\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$300 (200h × $1.50/h on Lambda Labs A100)\",\n      \"h100_equivalent\": \"~120h H100 (within ≤200 H100-hour budget constraint at typical A100/H100 performance ratio of ~0.6×)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~310h A100 (agent explores broader hyperparameter space with human approval gates; ~55% more runs than manual)\",\n      \"gpu_utilization\": \"MODERATE (~55–65%): agent queues follow-up experiments immediately after each run completes, filling GPU idle between human check-ins\",\n      \"timeline\": \"6–8 weeks\",\n      \"team\": \"1 researcher, ~30min/day check-in to approve experiment configs and review intermediate results\",\n      \"claude_api_cost\": \"~$150–250 (~1,500–2,500 conversation turns coordinating experiment scheduling, result parsing, and ablation planning)\",\n      \"estimated_gpu_cost\": \"~$465 (310h × $1.50/h)\",\n      \"h100_equivalent\": \"~186h H100 (within ≤200 H100-hour budget constraint at ~0.6× A100/H100 ratio, leaving ~14h headroom)\",\n      \"risk_note\": \"Choice of URIEL+ feature subspace (full 800-feature vs. Laplacian 300-feature vs. syntax-only) and the DPO prerequisite probe threshold require human judgment at key decision points; an automated agent may converge on a locally optimal weighting scheme that under-performs on the held-out Swahili generalization target\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~600h A100 (3–5× more experiments: grid search over distance metrics, curriculum schedule shapes, LoRA rank/alpha, 5+ target languages including Swahili and Kyrgyz for generalization, plus replication runs)\",\n      \"gpu_utilization\": \"NEAR-ZERO idle—agent schedules jobs back-to-back across all target languages in parallel, launches follow-up ablations immediately on job completion, and runs nightly sweeps without human bottleneck\",\n      \"timeline\": \"5–10 days with 4× concurrent A100s; ~3 weeks on a single A100\",\n      \"team\": \"0 (initial setup of experiment configs, data paths, and evaluation harness only)\",\n      \"claude_api_cost\": \"~$400–650 (~4,000–6,500 turns for full experiment orchestration, result parsing, ablation tree exploration, and report drafting)\",\n      \"estimated_gpu_cost\": \"~$900 (600h × $1.50/h)\",\n      \"h100_equivalent\": \"~360h H100 — EXCEEDS the ≤200 H100-hour hard budget constraint. Auto_research mode is documented for completeness but is NOT a viable deployment option within the stated budget. Use manual mode (~120 H100h) or human_in_loop mode (~186 H100h) to remain within budget.\",\n      \"speed_bottleneck\": \"GPU count is the primary bottleneck: 4 concurrent A100s reduces wall-clock time to ~5 days; API rate limits become secondary when running >8 parallel experiment threads\",\n      \"risk_note\": \"CONSTRAINT VIOLATION: 600 A100h ≈ 360 H100h, exceeding the ≤200 H100-hour hard budget. Additionally, unconstrained exploration may overfit the URIEL+ weighting function to the 3 initial target languages; Swahili as a held-out agglutinative target is required to detect this overfitting early.\"\n    }\n  },\n  \"target_venues\": [\n    \"ACL 2027 (ARR submission deadline August 3, 2026) — primary target; provides adequate time for validation on additional typological clusters beyond Turkic–Mongolic, and for a paper of this scope (multi-pivot curriculum + ablations + 3 evaluation benchmarks) that cannot realistically reach conference quality in under 6 weeks\",\n    \"EMNLP 2026 (ACL Rolling Review, rolling deadlines throughout 2026) — viable only if the team has prior QLoRA fine-tuning infrastructure already in place and can begin experiments immediately\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning (ACL 2024) [29% improvement on Chinese/Korean/Italian/Spanish; Turkic/Mongolic gap is untested]\",\n    \"Cross-Lingual Optimization for Language Transfer in Large Language Models (CLO; ACL 2025, arXiv:2505.14297) [DPO-style cross-lingual preference optimization using English-only source and M2M100 translation; baseline and methodological reference for TWMP's multi-source DPO extension]\",\n    \"Llama-3.1-Sherkala-8B-Chat (arXiv:2503.01493) [trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish; demonstrates Turkish as auxiliary language improves Kazakh performance via full fine-tuning; differentiated from TWMP's generalizable LoRA recipe parameterized by continuous URIEL+ distances]\",\n    \"Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) [implicit reward transfer from English-aligned DPO model to annotate cross-lingual preference pairs; 12.72% Win Rate improvement on X-AlpacaEval; English-only source with no typological weighting—differentiated from TWMP's multi-pivot source selection and low-resource agglutinative targets]\",\n    \"URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base (arXiv:2409.18472, COLING 2025) [~800-feature typological database covering 4,366 languages with SoftImpute for low-resource Turkic languages; replaces legacy lang2vec 289-dim URIEL in TWMP; official repository: github.com/LeeLanguageLab/URIELPlus]\",\n    \"Less is More: The Effectiveness of Compact Typological Language Representations (arXiv:2509.20129, EMNLP 2025) [Laplacian Score 300-feature URIEL+ subset (ρ=0.358) outperforms full 800-feature URIEL+ (ρ=0.260) for typological alignment and downstream cross-lingual NLP; justifies TWMP's feature selection step]\",\n    \"Optimizing Language Models for Crosslingual Knowledge Consistency (arXiv:2603.04678; Tianyu Liu et al., March 2026) [concurrent DPO-inspired work targeting factual consistency across 26 languages and 9 LLMs—orthogonal to TWMP's language-fidelity DPO objective; differentiated in related work]\",\n    \"TIPA: Typologically Informed Parameter Aggregation (arXiv:2601.16629, EACL 2026 Findings) [training-free encoder adapter aggregation across 230+ languages—differentiated from TWMP's training-time decoder curriculum]\",\n    \"Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) [discrete k-means language selection using legacy 289-dim URIEL TYPO features on BLOOM/mGPT/mT5—differentiated from TWMP's continuous URIEL+ weighting, staged curriculum, multi-source DPO, and Turkic/Mongolic targets]\",\n    \"KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan (ACL 2025, arXiv:2502.12829) [primary Kazakh evaluation benchmark, 23K questions, peer-reviewed]\",\n    \"MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages (ACL 2025 Findings, arXiv:2503.01150) [primary evaluation for Uyghur, Kazakh, Mongolian across 9 tasks]\",\n    \"TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages (ACL 2025, arXiv:2502.11020) [38K questions for Kazakh, Uyghur, and other Turkic languages; within-family controlled comparison]\",\n    \"Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages (arXiv:2502.10852) [encoder-based cross-lingual transfer for Tibetan/Uyghur/Kazakh/Mongolian; motivation for decoder LLM gap]\",\n    \"Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese (arXiv:2510.00810, 2025)\",\n    \"Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology (arXiv:2505.13908, 2025)\",\n    \"Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) [workshop paper, not main conference]\",\n    \"Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models (arXiv:2603.21036, 2026) [supplementary qualitative observation; single-author preprint with 50 hand-crafted questions—not primary motivation anchor]\"\n  ],\n  \"description\": \"This paper introduces Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, a method for adapting decoder LLMs to low-resource languages that are typologically distant from English. Rather than using a single English pivot as in PLUG, we compute typological distances using URIEL+ (arXiv:2409.18472, COLING 2025; urielplus Python library at github.com/LeeLanguageLab/URIELPlus), which covers ~800 features across 4,366 languages with SoftImpute imputation—critical for low-resource Turkic languages where legacy lang2vec 289-dim URIEL is known to be sparse. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), we apply Laplacian Score feature selection to reduce URIEL+ to 300 compact features (Spearman ρ=0.358 vs. ρ=0.260 for the full 800-feature set) before computing cosine distances and assigning inverse-distance sampling weights over the Aya collection. Aya pivot coverage is verified: Turkish (multi-million instances), Kyrgyz (~4.1M instances), and Uzbek all clear a 5,000-instance minimum threshold; Kazakh, Mongolian, and Uyghur are evaluation-only targets excluded from the pivot pool. A staged 3-phase curriculum progressively introduces more distant pivots using percentile thresholds computed from the empirical URIEL+ distance distribution of qualifying Aya pivots per target: Stage 1 (epochs 1–3) uses sources within the 25th percentile distance threshold (~≤0.32 for Kazakh, capturing Turkish/Kyrgyz/Uzbek/Azerbaijani); Stage 2 (epochs 4–6) expands to the 60th percentile (~≤0.56); Stage 3 (epochs 7–10) uses the full weighted mixture. The DPO preference optimization objective is precisely formulated for the multi-source case: for source pivot s_i and target t, chosen = (instruction in s_i, model-generated response in t); rejected = (instruction in s_i, model-generated response in s_i). This inverts CLO's English-input pair direction—CLO prefers English responses to English inputs (preserving English capability), while TWMP prefers target-language responses to any source-language input (promoting cross-lingual instruction following). Pairs are auto-constructed by sampling K=8 responses per instruction from Qwen3.5-9B, applying fastText language identification, and applying a minimum 20-token length gate to both chosen and rejected pools to exclude degenerate responses; no target-language training labels are required. An ablation row compares fastText-only selection against length-gated selection to quantify the quality impact of this filter. A mandatory 500-instruction prerequisite probe verifies >5% target-language response frequency (post-length-gate) per source-target pair; pairs failing this check fall back to SFT-only. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish and demonstrates the value of Turkish as an auxiliary language for Kazakh via full fine-tuning, motivating TWMP's Turkic pivot inclusion; TWMP generalizes this insight into a principled LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) uses implicit reward transfer from English-aligned models to annotate cross-lingual DPO pairs (12.72% Win Rate on X-AlpacaEval); TWMP extends this direction to multi-pivot source selection weighted by typological distance targeting low-resource agglutinative languages absent from that work. Concurrent work 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678, March 2026) uses DPO for factual consistency across 26 languages—orthogonal in objective (knowledge coherence vs. language fidelity) and not addressing low-resource instruction tuning. Two directly adjacent works are carefully differentiated: TIPA (EACL 2026) aggregates MAD-X encoder adapters at inference time without training; arXiv:2410.07809 uses k-means on legacy 289-dim URIEL for discrete language selection on BLOOM/mGPT with zero Kazakh/Mongolian/Uyghur coverage. We fine-tune Qwen3.5-9B with QLoRA (released March 2026; 248K-token vocabulary, 201 languages; 0.8B/2B/4B/9B series—no 7B variant), targeting Kazakh, Mongolian, and Uyghur, evaluated on KazMMLU, MiLiC-Eval, and TUMLU (all ACL 2025). Ablations cover full URIEL+ vs. Laplacian-300 vs. syntax-only vs. morphology-only vs. k-means discrete baseline; curriculum variants; DPO quality gate (fastText-only vs. length-gated); DPO vs. SFT-only. Swahili is the held-out agglutinative generalization target. Manual mode (200 A100h ≈ 120 H100h) and human-in-loop mode (310 A100h ≈ 186 H100h) stay within the ≤200 H100-hour budget; auto_research mode (600 A100h ≈ 360 H100h) exceeds the constraint and is not viable within budget. ACL 2027 (ARR August 3, 2026) is the primary target venue.\",\n  \"project_name\": \"typological_multi_pivot\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"SIGNIFICANT (PATTERN) – All five Round 5 issues remain unaddressed in Round 6 for the second consecutive round. (1) Foroutan et al. (arXiv:2510.25947, ICLR-submitted): not in landscape or key_references. (2) LangGPS (arXiv:2511.10229, AAAI 2026 main): not in landscape or key_references — this is a peer-reviewed AAAI 2026 competitor on multilingual instruction tuning data selection across 22 languages including low-resource targets, and its omission is the most damaging gap. (3) Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings): not cited despite being published November 2024 and appearing in ACL Anthology. (4) arXiv:2502.13647 (ACL 2025 Long, Kazakh instruction tuning): not cited despite being a direct Kazakh-targeting baseline. (5) URIEL+ expansion (arXiv:2510.27183, LREC 2026): not cited despite directly extending the typological tool TWMP relies on.\", \"MODERATE (NEW) – Budget-Xfer (arXiv:2603.27651, March 2026) proposes budget-constrained source language selection for multi-source cross-lingual transfer, jointly optimizing which source languages to include and how much data to allocate from each — directly parallel to TWMP's multi-pivot selection problem. It evaluates on three African target languages (Hausa, Yoruba, Swahili) using a 288-experiment suite. While it targets classification tasks rather than instruction tuning, EMNLP reviewers in the cross-lingual track will expect it to be cited and contrasted: Budget-Xfer frames source selection as resource allocation without typological features or curriculum ordering; TWMP provides principled URIEL+-based weighting and staged scheduling.\", \"MINOR (PERSISTENT) – Per-instruction chosen-pool fallback characterization remains incomplete. The approach section states that 'instructions yielding no target-language candidates in K=8 samples after the length filter are discarded' but does not report the per-instruction fallback rate as a characterization result. Round 5 feedback specifically requested one sentence confirming these instructions fall back to SFT-weighted objective (not silent skip) and reporting the empirical fallback rate per source-target pair. The current text says they are 'discarded,' which implies silent skip rather than SFT fallback — this ambiguity must be resolved and the frequency reported.\"]\nFeedback: This is Round 6. The core method is technically sound, the DPO formulation is precise, the compute budget is within constraint, and the evaluation design is appropriate. However, the same five citations flagged in Round 5 are absent for the second consecutive round, and a new paper (Budget-Xfer, arXiv:2603.27651) has appeared that is directly adjacent. Here is the exact text to add for each outstanding item:\n\n(1) Foroutan et al. (Section 2, one sentence): 'Revisiting Multilingual Data Mixtures [Foroutan et al., 2025] studies reweighting across 25–400 languages at pretraining scale (1.1B–3B parameters); TWMP operates at instruction-tuning scale—10 epochs, LoRA, narrow near-family pivot pool—where the data volume, optimization dynamics, and gradient signal are qualitatively different from the pretraining regime.'\n\n(2) LangGPS (Section 2, one paragraph — highest priority): 'LangGPS [Ye et al., AAAI 2026, arXiv:2511.10229] selects multilingual instruction data based on language separability scores derived from the model's own representation space, demonstrating improvements across 22 languages including low-resource targets. Unlike LangGPS, TWMP uses external typological features from URIEL+ to derive a pivot ordering independent of training dynamics, and integrates a staged curriculum and multi-source DPO objective that LangGPS does not address.'\n\n(3) Code-Switching Curriculum (Section 2, one sentence): 'Code-Switching Curriculum Learning [Yoo et al., ACL 2025 Findings, arXiv:2411.02460] proposes a 3-stage curriculum (token-level → sentence-level → monolingual code-switching) for a single language pair; TWMP's curriculum operates over a pool of typologically ordered pivot languages without code-switching and targets a set of related agglutinative languages rather than a single target.'\n\n(4) Kazakh instruction tuning (Section 2, one sentence): 'Laiyk et al. [ACL 2025 Long, arXiv:2502.13647] fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP does not require any target-language instruction labels and applies equally to Mongolian and Uyghur, where no comparable GPT-4-assisted dataset currently exists.'\n\n(5) URIEL+ expansion (Section 3, one sentence): 'A concurrent LREC 2026 extension [Shipton et al., arXiv:2510.27183] adds script vectors and Glottolog genealogies to URIEL+, covering 26,449 languages; TWMP uses the COLING 2025 base version [arXiv:2409.18472] with SoftImpute, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for the qualifying Aya pivot languages.'\n\n(6) Budget-Xfer (Section 2, one sentence): 'Budget-Xfer [arXiv:2603.27651, 2026] formulates multi-source cross-lingual transfer as a budget-constrained allocation problem for NER/sentiment tasks; TWMP's typological-distance weighting and staged curriculum provide a principled ordering mechanism for instruction tuning that Budget-Xfer does not address.'\n\n(7) Fix the per-instruction fallback: Change 'Instructions yielding no target-language candidates in K=8 samples after the length filter are discarded' to 'Instructions yielding no target-language candidates in K=8 samples after the length filter fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe.'\n\nAll seven items are writing-only changes requiring no new experiments. ACL 2027 (ARR August 3, 2026) remains the appropriate primary target. At Round 6, the paper cannot pass until at minimum items (1)–(5) are resolved.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.5 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T07:47:03.581Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T07:47:03.581Z",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-10T07:47:03.620Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning",
  "core_problem": "Cross-lingual instruction tuning for low-resource languages defaults to English as the sole pivot, creating systematic gaps for languages that are typologically distant from English—particularly those with agglutinative morphology, non-Latin scripts, or SOV word order. Three peer-reviewed ACL 2025 benchmarks—KazMMLU (Kazakh), MiLiC-Eval (Tibetan, Uyghur, Kazakh, Mongolian), and TUMLU (Turkic languages including Kazakh and Uyghur)—confirm that even frontier multilingual LLMs (GPT-4, Llama-3.1, Qwen-2.5) achieve near-random performance on Mongolian comprehension tasks and substantially below-par accuracy on Kazakh and Uyghur relative to typologically proximate high-resource languages. No existing instruction tuning method uses typological distance to continuously weight data-source selection across a multi-pivot mixture for these under-represented language families.",
  "opportunity": "Three complementary ACL 2025 benchmarks provide peer-reviewed grounding for the performance gap. KazMMLU (arXiv:2502.12829; ACL 2025 long paper) comprises 23K Kazakh-language questions spanning STEM, humanities, and social sciences sourced from authentic educational materials; evaluation of Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 shows 'substantial room for improvement' for all models on Kazakh, despite the language having 20 million speakers. MiLiC-Eval (arXiv:2503.01150; ACL 2025 Findings) covers Tibetan, Uyghur, Kazakh, and Mongolian across 9 tasks with 24K instances; GPT-4o-mini achieves only slightly above random on Mongolian tasks, and models exhibit only 'preliminary understanding' of Tibetan and Kazakh. TUMLU (arXiv:2502.11020; ACL 2025 long paper) provides 38K native questions spanning 11 academic subjects across Turkic languages including Kazakh and Uyghur, enabling controlled within-family comparisons that isolate the effect of lower training corpus size. The XLM-SWCM paper (arXiv:2502.10852) additionally shows that encoder-based shared-weight cross-lingual pretraining partially bridges these gaps—Kazakh ROUGE-L summarization score of 5.6 is notably the lowest among the four minority languages studied—but this approach does not scale to instruction-following for decoder LLMs. CLO (arXiv:2505.14297; ACL 2025) shows that DPO-style cross-lingual preference optimization with only 3,200 samples outperforms standard SFT with 6,400 samples, establishing strong data efficiency for cross-lingual transfer. These findings together create a clear opening: by weighting instruction data from multiple source languages inversely by URIEL+ typological distance and introducing a staged curriculum, we can build a principled multi-pivot training regime that directly addresses the English-pivot bottleneck for agglutinative low-resource targets.",
  "landscape": "PLUG (ACL 2024) established that English-pivot cross-lingual instruction generation improves multilingual instruction following—but its reported 29% improvement was measured on Chinese, Korean, Italian, and Spanish. Whether the English-pivot advantage holds for typologically distant agglutinative languages with non-Latin scripts (Kazakh, Mongolian, Uyghur) is an assumption that TWMP directly tests rather than takes for granted. CLO (arXiv:2505.14297; ACL 2025) improves data efficiency via DPO-style cross-lingual preference optimization using 6,400 OpenAssistant samples machine-translated by M2M100; it fixes English as the sole source language without varying source selection by typological distance. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh, English, Russian, and Turkish, and demonstrates that Turkish as an auxiliary language improves Kazakh performance—directly motivating TWMP's inclusion of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc four-language selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language, with principled pivot selection replacing language-specific engineering. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving a 12.72% average Win Rate improvement on X-AlpacaEval; it uses English as the sole source and implicit reward annotation without typological weighting—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from that work. 'Family Matters' (arXiv:2510.00810) applies language transfer and LoRA merging from typologically related Nordic languages to Faroese—demonstrating that typological proximity helps—but as a single-language case study with no generalizable training recipe. 'Cross-Linguistic Transfer in Multilingual NLP' (arXiv:2505.13908) analyzes language family and morphology effects empirically without proposing a training method. Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) decouples task and language LoRA adapters but does not use typological features to parameterize or weight the language adapter. 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678; Tianyu Liu et al., March 2026) introduces a DPO-inspired method—concurrent with TWMP—that enforces factual consistency of model responses across 26 languages and 9 LLMs; its preference pairs encode semantic equivalence of knowledge across languages (chosen = factually consistent cross-lingual response, rejected = factually inconsistent response). This objective is orthogonal to TWMP's: DCO addresses what the model says across languages (knowledge coherence), while TWMP addresses which language it responds in when given instructions in any of multiple pivot languages (instruction-language fidelity). DCO does not address low-resource instruction tuning, multi-pivot source selection, or typological-distance weighting. Two works require careful differentiation from TWMP. First, TIPA (arXiv:2601.16629; EACL 2026 Findings) constructs proxy language adapters by aggregating existing MAD-X adapters weighted by typological similarity across 230+ languages—entirely without training. TIPA is orthogonal to TWMP in three key ways: (1) it is training-free inference-time adapter aggregation, whereas TWMP learns from a typologically-weighted data curriculum; (2) it operates on encoder-based MAD-X modules for classification tasks, whereas TWMP targets decoder LLM instruction tuning; (3) TIPA has not been applied to instruction generation or to languages not already represented by a dedicated adapter. Second, 'Linguistically-Informed Multilingual Instruction Tuning' (arXiv:2410.07809) uses 289-dimensional legacy URIEL TYPO vectors with k-means clustering to select 14 discrete representative languages from a 52-language pool (one per cluster) for LoRA fine-tuning on Bactrian-X, showing that typologically diverse selection beats random selection. TWMP differs substantially: rather than discrete cluster-representative selection, TWMP applies continuous inverse-distance sampling weights over the full Aya collection using compact URIEL+ features (300-dim, Laplacian Score selected); it adds a staged cosine-distance curriculum schedule; it integrates a multi-source DPO preference optimization objective for language fidelity; and it directly targets Kazakh, Mongolian, and Uyghur—languages for which arXiv:2410.07809's evaluation suite (XNLI, XCOPA, XStoryCloze, XWinograd, PAWS-X) provides zero coverage. The combination of continuous URIEL+ weighting, staged curriculum, precisely formulated multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering the target languages constitutes a principled and differentiated advance.",
  "approach": "We propose Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, which replaces PLUG's single-English pivot with a principled mixture over multiple source languages drawn from the Aya collection (513M instances across 114 languages).\n\nAya pivot coverage is verified before training: Turkish (high-resource, multi-million instances), Kyrgyz (~4.1M instances in the Aya collection language split), Uzbek (confirmed present as an underrepresented language with meaningful coverage), and Azerbaijani all qualify as pivot sources. A minimum threshold of 5,000 Aya instances per pivot language is enforced; languages below this threshold are excluded from the mixture. All qualifying pivot languages and their instance counts are reported in an appendix table. Kazakh, Mongolian, and Uyghur serve exclusively as evaluation targets and are never included in the pivot mixture.\n\nTypological distances are computed using URIEL+ (arXiv:2409.18472, COLING 2025; available via the urielplus Python library at github.com/LeeLanguageLab/URIELPlus) rather than the legacy lang2vec 289-dimensional binary features. URIEL+ expands coverage to 4,366 languages with approximately 800 features (607 grammar features covering syntactic and morphological dimensions, plus 193 sound features), and applies SoftImpute for missing-value imputation—critical for reducing sparsity in Kazakh, Uzbek, and Kyrgyz, where legacy URIEL features are known to be sparse. URIEL+ explicitly represents Kazakh's multi-script properties (Cyrillic, Latin, and Arabic) via script vectors. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), which demonstrates that a Laplacian Score 300-feature subset of URIEL+ achieves Spearman ρ=0.358 on typological alignment tasks versus ρ=0.260 for the full 800-feature set while also improving downstream cross-lingual NLP performance, we apply this feature selection before computing cosine distances. Data-sampling weights are assigned inversely proportional to these 300-feature URIEL+ cosine distances, so morphologically close pivots such as Turkish or Uzbek for Kazakh receive substantially higher weight than English.\n\nThe staged curriculum uses three phases calibrated by the empirical URIEL+ distance distribution of qualifying Aya pivot languages relative to each target language. Let D_25 and D_60 denote the 25th and 60th percentile distances from the target language to all qualifying Aya pivots (computed once, before training). Stage 1 (epochs 1–3): exclusively sources with cosine distance < D_25—for Kazakh, approximately ≤0.32, capturing Turkish, Kyrgyz, Uzbek, and Azerbaijani. Stage 2 (epochs 4–6): sources with distance < D_60 (approximately ≤0.56 for Kazakh), expanding to Russian, Arabic, and other mid-distance languages. Stage 3 (epochs 7–10): full mixture over all qualifying pivot languages with continuous inverse-distance weights. Thresholds are target-specific and computed from the actual Aya-pivot distance distribution; for Mongolian, where no Turkic pivot falls within D_25, the closest available Aya sources (Korean, Finnish, Turkish) are used across all three stages with correspondingly small weights—this distance-constrained Mongolian setting is a controlled finding of interest. Ablations compare: no curriculum (full weighted mixture from epoch 1), 2-stage (merging Stages 1–2), 3-stage (proposed), and linear interpolation between stages.\n\nThe CLO-style DPO preference optimization objective is precisely extended to the multi-source setting. For each source pivot language s_i and target language t, preference pairs are defined as: chosen = (x_{s_i}, y^w_t)—an instruction in source language s_i paired with a model-generated response identified as being in the target language t; rejected = (x_{s_i}, y^l_{s_i})—the same instruction paired with a model-generated response in source language s_i. This formulation promotes target-language responses to source-language instructions and differs from CLO's English-source objective in a critical respect: CLO's English-input pair (chosen=English response, rejected=target-language response) is designed to preserve English capability by penalizing cross-lingual output for English inputs. TWMP inverts this preference because the training goal is acquisition of cross-lingual target-language instruction following: for any source-language input, we want the model to respond in the target language. TWMP does not use CLO's second pair type (target-language input → prefer target-language response) because target-language training data is explicitly excluded.\n\nPreference pairs are constructed entirely without target-language labels via automatic language identification: given each source-language instruction x_{s_i}, we sample K=8 candidate responses from Qwen3.5-9B at temperature 0.7; apply fastText language identification (lid.176.bin) to each candidate; assign responses identified as the target language to the chosen pool and responses identified as the source language to the rejected pool; apply a minimum 20-token length gate to both pools to exclude degenerate or near-empty responses; pair the highest-scoring chosen (by fastText language ID confidence) with the lowest-scoring rejected per instruction. Instructions yielding no target-language candidates in K=8 samples after the length filter are discarded. An ablation row in the DPO evaluation table compares fastText-only selection (no length gate) against length-gated selection (≥20 tokens) to quantify the quality impact of this filter; this also characterizes the frequency of degenerate responses per source-target pair. As a mandatory prerequisite check, we run a 500-instruction probe per source-target language pair on the base Qwen3.5-9B and verify that target-language responses (meeting the ≥20-token gate) appear in >5% of K=8 samples; any pivot language pair failing this check is excluded from DPO training (falling back to SFT-weighted sampling only) for that target language. This probe is reported as a characterization result: for close Turkic pivots (Turkish→Kazakh), we expect the frequency to exceed 5% given Qwen3.5-9B's broad multilingual coverage; for distant pivots (English→Mongolian), the check may filter some source languages, which is informative about which pivots can drive DPO-based cross-lingual preference learning.\n\nWe apply QLoRA fine-tuning of Qwen3.5-9B (released March 2026; 248K-token vocabulary spanning 201 languages; the Qwen3.5 small series has 0.8B/2B/4B/9B variants—no 7B exists) on this weighted multi-pivot dataset, targeting Kazakh, Mongolian, and Uyghur as primary evaluation cases. Evaluation uses three ACL 2025 benchmarks: KazMMLU for Kazakh, MiLiC-Eval for all three targets across 9 tasks, and TUMLU for Kazakh and Uyghur within a controlled within-Turkic-family comparison. PLUG and CLO serve as primary baselines. Typological weighting ablations compare: full 800-feature URIEL+ vs. Laplacian-selected 300 features vs. syntax-only (474 features) vs. morphology-only (133 features) vs. the k-means discrete selection baseline from arXiv:2410.07809. Swahili serves as a held-out agglutinative generalization target not used during hyperparameter design. Note: TyDi QA covers Arabic, Bengali, Finnish, Indonesian, Japanese, Kiswahili, Korean, Russian, Telugu, and Thai—it does not include Kazakh, Mongolian, or Uyghur and is not used here.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200h A100 (15–20 QLoRA runs × 10–13h each on Qwen3.5-9B, covering 3 primary target languages, PLUG/CLO baselines, URIEL+ sub-space ablations, curriculum schedule variants, DPO quality gate ablation row, and DPO prerequisite probe runs)",
      "gpu_utilization": "LOW (~25–35%): GPU sits idle during code writing, debugging, data pipeline work, result analysis, and paper writing; runs are launched manually and often queue overnight",
      "timeline": "4–6 months",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$300 (200h × $1.50/h on Lambda Labs A100)",
      "h100_equivalent": "~120h H100 (within ≤200 H100-hour budget constraint at typical A100/H100 performance ratio of ~0.6×)"
    },
    "human_in_loop": {
      "gpu_hours": "~310h A100 (agent explores broader hyperparameter space with human approval gates; ~55% more runs than manual)",
      "gpu_utilization": "MODERATE (~55–65%): agent queues follow-up experiments immediately after each run completes, filling GPU idle between human check-ins",
      "timeline": "6–8 weeks",
      "team": "1 researcher, ~30min/day check-in to approve experiment configs and review intermediate results",
      "claude_api_cost": "~$150–250 (~1,500–2,500 conversation turns coordinating experiment scheduling, result parsing, and ablation planning)",
      "estimated_gpu_cost": "~$465 (310h × $1.50/h)",
      "h100_equivalent": "~186h H100 (within ≤200 H100-hour budget constraint at ~0.6× A100/H100 ratio, leaving ~14h headroom)",
      "risk_note": "Choice of URIEL+ feature subspace (full 800-feature vs. Laplacian 300-feature vs. syntax-only) and the DPO prerequisite probe threshold require human judgment at key decision points; an automated agent may converge on a locally optimal weighting scheme that under-performs on the held-out Swahili generalization target"
    },
    "auto_research": {
      "gpu_hours": "~600h A100 (3–5× more experiments: grid search over distance metrics, curriculum schedule shapes, LoRA rank/alpha, 5+ target languages including Swahili and Kyrgyz for generalization, plus replication runs)",
      "gpu_utilization": "NEAR-ZERO idle—agent schedules jobs back-to-back across all target languages in parallel, launches follow-up ablations immediately on job completion, and runs nightly sweeps without human bottleneck",
      "timeline": "5–10 days with 4× concurrent A100s; ~3 weeks on a single A100",
      "team": "0 (initial setup of experiment configs, data paths, and evaluation harness only)",
      "claude_api_cost": "~$400–650 (~4,000–6,500 turns for full experiment orchestration, result parsing, ablation tree exploration, and report drafting)",
      "estimated_gpu_cost": "~$900 (600h × $1.50/h)",
      "h100_equivalent": "~360h H100 — EXCEEDS the ≤200 H100-hour hard budget constraint. Auto_research mode is documented for completeness but is NOT a viable deployment option within the stated budget. Use manual mode (~120 H100h) or human_in_loop mode (~186 H100h) to remain within budget.",
      "speed_bottleneck": "GPU count is the primary bottleneck: 4 concurrent A100s reduces wall-clock time to ~5 days; API rate limits become secondary when running >8 parallel experiment threads",
      "risk_note": "CONSTRAINT VIOLATION: 600 A100h ≈ 360 H100h, exceeding the ≤200 H100-hour hard budget. Additionally, unconstrained exploration may overfit the URIEL+ weighting function to the 3 initial target languages; Swahili as a held-out agglutinative target is required to detect this overfitting early."
    }
  },
  "target_venues": [
    "ACL 2027 (ARR submission deadline August 3, 2026) — primary target; provides adequate time for validation on additional typological clusters beyond Turkic–Mongolic, and for a paper of this scope (multi-pivot curriculum + ablations + 3 evaluation benchmarks) that cannot realistically reach conference quality in under 6 weeks",
    "EMNLP 2026 (ACL Rolling Review, rolling deadlines throughout 2026) — viable only if the team has prior QLoRA fine-tuning infrastructure already in place and can begin experiments immediately"
  ],
  "level": "solid",
  "key_references": [
    "PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning (ACL 2024) [29% improvement on Chinese/Korean/Italian/Spanish; Turkic/Mongolic gap is untested]",
    "Cross-Lingual Optimization for Language Transfer in Large Language Models (CLO; ACL 2025, arXiv:2505.14297) [DPO-style cross-lingual preference optimization using English-only source and M2M100 translation; baseline and methodological reference for TWMP's multi-source DPO extension]",
    "Llama-3.1-Sherkala-8B-Chat (arXiv:2503.01493) [trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish; demonstrates Turkish as auxiliary language improves Kazakh performance via full fine-tuning; differentiated from TWMP's generalizable LoRA recipe parameterized by continuous URIEL+ distances]",
    "Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) [implicit reward transfer from English-aligned DPO model to annotate cross-lingual preference pairs; 12.72% Win Rate improvement on X-AlpacaEval; English-only source with no typological weighting—differentiated from TWMP's multi-pivot source selection and low-resource agglutinative targets]",
    "URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base (arXiv:2409.18472, COLING 2025) [~800-feature typological database covering 4,366 languages with SoftImpute for low-resource Turkic languages; replaces legacy lang2vec 289-dim URIEL in TWMP; official repository: github.com/LeeLanguageLab/URIELPlus]",
    "Less is More: The Effectiveness of Compact Typological Language Representations (arXiv:2509.20129, EMNLP 2025) [Laplacian Score 300-feature URIEL+ subset (ρ=0.358) outperforms full 800-feature URIEL+ (ρ=0.260) for typological alignment and downstream cross-lingual NLP; justifies TWMP's feature selection step]",
    "Optimizing Language Models for Crosslingual Knowledge Consistency (arXiv:2603.04678; Tianyu Liu et al., March 2026) [concurrent DPO-inspired work targeting factual consistency across 26 languages and 9 LLMs—orthogonal to TWMP's language-fidelity DPO objective; differentiated in related work]",
    "TIPA: Typologically Informed Parameter Aggregation (arXiv:2601.16629, EACL 2026 Findings) [training-free encoder adapter aggregation across 230+ languages—differentiated from TWMP's training-time decoder curriculum]",
    "Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) [discrete k-means language selection using legacy 289-dim URIEL TYPO features on BLOOM/mGPT/mT5—differentiated from TWMP's continuous URIEL+ weighting, staged curriculum, multi-source DPO, and Turkic/Mongolic targets]",
    "KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan (ACL 2025, arXiv:2502.12829) [primary Kazakh evaluation benchmark, 23K questions, peer-reviewed]",
    "MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages (ACL 2025 Findings, arXiv:2503.01150) [primary evaluation for Uyghur, Kazakh, Mongolian across 9 tasks]",
    "TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages (ACL 2025, arXiv:2502.11020) [38K questions for Kazakh, Uyghur, and other Turkic languages; within-family controlled comparison]",
    "Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages (arXiv:2502.10852) [encoder-based cross-lingual transfer for Tibetan/Uyghur/Kazakh/Mongolian; motivation for decoder LLM gap]",
    "Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese (arXiv:2510.00810, 2025)",
    "Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology (arXiv:2505.13908, 2025)",
    "Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) [workshop paper, not main conference]",
    "Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models (arXiv:2603.21036, 2026) [supplementary qualitative observation; single-author preprint with 50 hand-crafted questions—not primary motivation anchor]"
  ],
  "description": "This paper introduces Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, a method for adapting decoder LLMs to low-resource languages that are typologically distant from English. Rather than using a single English pivot as in PLUG, we compute typological distances using URIEL+ (arXiv:2409.18472, COLING 2025; urielplus Python library at github.com/LeeLanguageLab/URIELPlus), which covers ~800 features across 4,366 languages with SoftImpute imputation—critical for low-resource Turkic languages where legacy lang2vec 289-dim URIEL is known to be sparse. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), we apply Laplacian Score feature selection to reduce URIEL+ to 300 compact features (Spearman ρ=0.358 vs. ρ=0.260 for the full 800-feature set) before computing cosine distances and assigning inverse-distance sampling weights over the Aya collection. Aya pivot coverage is verified: Turkish (multi-million instances), Kyrgyz (~4.1M instances), and Uzbek all clear a 5,000-instance minimum threshold; Kazakh, Mongolian, and Uyghur are evaluation-only targets excluded from the pivot pool. A staged 3-phase curriculum progressively introduces more distant pivots using percentile thresholds computed from the empirical URIEL+ distance distribution of qualifying Aya pivots per target: Stage 1 (epochs 1–3) uses sources within the 25th percentile distance threshold (~≤0.32 for Kazakh, capturing Turkish/Kyrgyz/Uzbek/Azerbaijani); Stage 2 (epochs 4–6) expands to the 60th percentile (~≤0.56); Stage 3 (epochs 7–10) uses the full weighted mixture. The DPO preference optimization objective is precisely formulated for the multi-source case: for source pivot s_i and target t, chosen = (instruction in s_i, model-generated response in t); rejected = (instruction in s_i, model-generated response in s_i). This inverts CLO's English-input pair direction—CLO prefers English responses to English inputs (preserving English capability), while TWMP prefers target-language responses to any source-language input (promoting cross-lingual instruction following). Pairs are auto-constructed by sampling K=8 responses per instruction from Qwen3.5-9B, applying fastText language identification, and applying a minimum 20-token length gate to both chosen and rejected pools to exclude degenerate responses; no target-language training labels are required. An ablation row compares fastText-only selection against length-gated selection to quantify the quality impact of this filter. A mandatory 500-instruction prerequisite probe verifies >5% target-language response frequency (post-length-gate) per source-target pair; pairs failing this check fall back to SFT-only. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish and demonstrates the value of Turkish as an auxiliary language for Kazakh via full fine-tuning, motivating TWMP's Turkic pivot inclusion; TWMP generalizes this insight into a principled LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) uses implicit reward transfer from English-aligned models to annotate cross-lingual DPO pairs (12.72% Win Rate on X-AlpacaEval); TWMP extends this direction to multi-pivot source selection weighted by typological distance targeting low-resource agglutinative languages absent from that work. Concurrent work 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678, March 2026) uses DPO for factual consistency across 26 languages—orthogonal in objective (knowledge coherence vs. language fidelity) and not addressing low-resource instruction tuning. Two directly adjacent works are carefully differentiated: TIPA (EACL 2026) aggregates MAD-X encoder adapters at inference time without training; arXiv:2410.07809 uses k-means on legacy 289-dim URIEL for discrete language selection on BLOOM/mGPT with zero Kazakh/Mongolian/Uyghur coverage. We fine-tune Qwen3.5-9B with QLoRA (released March 2026; 248K-token vocabulary, 201 languages; 0.8B/2B/4B/9B series—no 7B variant), targeting Kazakh, Mongolian, and Uyghur, evaluated on KazMMLU, MiLiC-Eval, and TUMLU (all ACL 2025). Ablations cover full URIEL+ vs. Laplacian-300 vs. syntax-only vs. morphology-only vs. k-means discrete baseline; curriculum variants; DPO quality gate (fastText-only vs. length-gated); DPO vs. SFT-only. Swahili is the held-out agglutinative generalization target. Manual mode (200 A100h ≈ 120 H100h) and human-in-loop mode (310 A100h ≈ 186 H100h) stay within the ≤200 H100-hour budget; auto_research mode (600 A100h ≈ 360 H100h) exceeds the constraint and is not viable within budget. ACL 2027 (ARR August 3, 2026) is the primary target venue.",
  "project_name": "typological_multi_pivot",
  "source": "web_research"
}

## Reviewer feedback (round 6)
Issues: ["SIGNIFICANT (PATTERN) – All five Round 5 issues remain unaddressed in Round 6 for the second consecutive round. (1) Foroutan et al. (arXiv:2510.25947, ICLR-submitted): not in landscape or key_references. (2) LangGPS (arXiv:2511.10229, AAAI 2026 main): not in landscape or key_references — this is a peer-reviewed AAAI 2026 competitor on multilingual instruction tuning data selection across 22 languages including low-resource targets, and its omission is the most damaging gap. (3) Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings): not cited despite being published November 2024 and appearing in ACL Anthology. (4) arXiv:2502.13647 (ACL 2025 Long, Kazakh instruction tuning): not cited despite being a direct Kazakh-targeting baseline. (5) URIEL+ expansion (arXiv:2510.27183, LREC 2026): not cited despite directly extending the typological tool TWMP relies on.", "MODERATE (NEW) – Budget-Xfer (arXiv:2603.27651, March 2026) proposes budget-constrained source language selection for multi-source cross-lingual transfer, jointly optimizing which source languages to include and how much data to allocate from each — directly parallel to TWMP's multi-pivot selection problem. It evaluates on three African target languages (Hausa, Yoruba, Swahili) using a 288-experiment suite. While it targets classification tasks rather than instruction tuning, EMNLP reviewers in the cross-lingual track will expect it to be cited and contrasted: Budget-Xfer frames source selection as resource allocation without typological features or curriculum ordering; TWMP provides principled URIEL+-based weighting and staged scheduling.", "MINOR (PERSISTENT) – Per-instruction chosen-pool fallback characterization remains incomplete. The approach section states that 'instructions yielding no target-language candidates in K=8 samples after the length filter are discarded' but does not report the per-instruction fallback rate as a characterization result. Round 5 feedback specifically requested one sentence confirming these instructions fall back to SFT-weighted objective (not silent skip) and reporting the empirical fallback rate per source-target pair. The current text says they are 'discarded,' which implies silent skip rather than SFT fallback — this ambiguity must be resolved and the frequency reported."]
Feedback: This is Round 6. The core method is technically sound, the DPO formulation is precise, the compute budget is within constraint, and the evaluation design is appropriate. However, the same five citations flagged in Round 5 are absent for the second consecutive round, and a new paper (Budget-Xfer, arXiv:2603.27651) has appeared that is directly adjacent. Here is the exact text to add for each outstanding item:

(1) Foroutan et al. (Section 2, one sentence): 'Revisiting Multilingual Data Mixtures [Foroutan et al., 2025] studies reweighting across 25–400 languages at pretraining scale (1.1B–3B parameters); TWMP operates at instruction-tuning scale—10 epochs, LoRA, narrow near-family pivot pool—where the data volume, optimization dynamics, and gradient signal are qualitatively different from the pretraining regime.'

(2) LangGPS (Section 2, one paragraph — highest priority): 'LangGPS [Ye et al., AAAI 2026, arXiv:2511.10229] selects multilingual instruction data based on language separability scores derived from the model's own representation space, demonstrating improvements across 22 languages including low-resource targets. Unlike LangGPS, TWMP uses external typological features from URIEL+ to derive a pivot ordering independent of training dynamics, and integrates a staged curriculum and multi-source DPO objective that LangGPS does not address.'

(3) Code-Switching Curriculum (Section 2, one sentence): 'Code-Switching Curriculum Learning [Yoo et al., ACL 2025 Findings, arXiv:2411.02460] proposes a 3-stage curriculum (token-level → sentence-level → monolingual code-switching) for a single language pair; TWMP's curriculum operates over a pool of typologically ordered pivot languages without code-switching and targets a set of related agglutinative languages rather than a single target.'

(4) Kazakh instruction tuning (Section 2, one sentence): 'Laiyk et al. [ACL 2025 Long, arXiv:2502.13647] fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP does not require any target-language instruction labels and applies equally to Mongolian and Uyghur, where no comparable GPT-4-assisted dataset currently exists.'

(5) URIEL+ expansion (Section 3, one sentence): 'A concurrent LREC 2026 extension [Shipton et al., arXiv:2510.27183] adds script vectors and Glottolog genealogies to URIEL+, covering 26,449 languages; TWMP uses the COLING 2025 base version [arXiv:2409.18472] with SoftImpute, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for the qualifying Aya pivot languages.'

(6) Budget-Xfer (Section 2, one sentence): 'Budget-Xfer [arXiv:2603.27651, 2026] formulates multi-source cross-lingual transfer as a budget-constrained allocation problem for NER/sentiment tasks; TWMP's typological-distance weighting and staged curriculum provide a principled ordering mechanism for instruction tuning that Budget-Xfer does not address.'

(7) Fix the per-instruction fallback: Change 'Instructions yielding no target-language candidates in K=8 samples after the length filter are discarded' to 'Instructions yielding no target-language candidates in K=8 samples after the length filter fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe.'

All seven items are writing-only changes requiring no new experiments. ACL 2027 (ARR August 3, 2026) remains the appropriate primary target. At Round 6, the paper cannot pass until at minimum items (1)–(5) are resolved.

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
  "promptId": "0c201752-9958-4eef-a252-56537162bf6a",
  "type": "user",
  "uuid": "78ee667c-8573-44a9-ab8c-ed0bb5c7e397",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T07:47:03.617Z_

```json
{
  "parentUuid": "78ee667c-8573-44a9-ab8c-ed0bb5c7e397",
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
  "uuid": "4232666e-5ced-4bd0-b6f0-8f41674c4edd",
  "timestamp": "2026-05-10T07:47:03.617Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T07:47:03.617Z_

```json
{
  "parentUuid": "4232666e-5ced-4bd0-b6f0-8f41674c4edd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "dcd03c7b-5b9f-443d-afa5-3144f9a50533",
  "timestamp": "2026-05-10T07:47:03.617Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruc…",
  "leafUuid": "dcd03c7b-5b9f-443d-afa5-3144f9a50533",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise TWMP core problem and landscape for Round 7",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6"
}
```

---

### Assistant

_source line 8 · 2026-05-10T07:47:25.325Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully before deciding on the approach.

**Current State Assessment:**

This idea has been through 6 rounds of revision with stagnation. The reviewer feedback for Round 6 is very specific - it's mostly about missing citations (7 specific items) rather than fundamental methodological issues. The reviewer explicitly says:
- "The core method is technically sound, the DPO formulation is precise, the compute budget is within constraint, and the evaluation design is appropriate."
- "All seven items are writing-only changes requiring no new experiments."

So this is NOT a case where the approach is fundamentally flawed. The stagnation seems to be caused by persistent failure to add specific citations, not by fundamental problems with the idea.
 
Now I need to pull those six missing papers and read through them to understand what they contribute to the landscape, then integrate them into the references and text. I also need to fix the per-instruction fallback issue and make sure all seven items are properly addressed in the revision. to the landscape and key_references

Since the reviewer provides exact text to add for each item, and the core methodology is sound, this is a **minor** revision focused purely on adding the missing citations and fixing the fallback description.

Let me fetch the papers to verify their content before adding them.

Actually, given the instructions to do deep research, let me fetch these papers. But given that the reviewer has already provided the exact text to add, I should verify the papers exist and their content matches, then make the additions.

Let me use the WebFetch/WebSearch tools to look up these papers and verify their content.

I'll need to search for several papers: Foroutan et al. arXiv:2510.25947, LangGPS arXiv:2511.10229, Code-Switching Curriculum arXiv:2411.02460, arXiv:2502.13647, URIEL+ expansion arXiv:2510.27183, Budget-Xfer, and arXiv:2603.27651. I'll launch a general-purpose agent to handle these searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcd03c7b-5b9f-443d-afa5-3144f9a50533",
  "isSidechain": false,
  "requestId": "req_011CatX22CRHWhHXzXfAFvRY",
  "type": "assistant",
  "uuid": "46034e8a-a6b4-4017-b109-9f001f9afec1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KdzWuM3J2cXmVsybwxDfi2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15983,
      "cache_read_input_tokens": 11631,
      "output_tokens": 729,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 729,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 15983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15983
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

_source line 9 · 2026-05-10T07:47:25.991Z_

Looking at the situation: 6 rounds in, core method is sound per the reviewer, and all remaining issues are citation additions plus one prose fix. I'll fetch all six missing papers in parallel to verify their content before integrating them, then produce a complete revised JSON.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46034e8a-a6b4-4017-b109-9f001f9afec1",
  "isSidechain": false,
  "requestId": "req_011CatX22CRHWhHXzXfAFvRY",
  "type": "assistant",
  "uuid": "97cee615-3024-44c6-83dc-2d4d47285fbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KdzWuM3J2cXmVsybwxDfi2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15983,
      "cache_read_input_tokens": 11631,
      "output_tokens": 729,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 729,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 15983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15983
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

_source line 10 · 2026-05-10T07:47:26.178Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PtaenAaR4hvAmjkiiovHkb`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97cee615-3024-44c6-83dc-2d4d47285fbd",
  "isSidechain": false,
  "requestId": "req_011CatX22CRHWhHXzXfAFvRY",
  "type": "assistant",
  "uuid": "f477a79d-e124-4ff5-a240-8105c1f8499e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KdzWuM3J2cXmVsybwxDfi2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15983,
      "cache_read_input_tokens": 11631,
      "output_tokens": 729,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 729,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 15983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15983
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

_source line 11 · 2026-05-10T07:47:26.185Z_

<details><summary>↩ Tool result · `toolu_01PtaenAaR4hvAmjkiiovHkb`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "f477a79d-e124-4ff5-a240-8105c1f8499e",
  "isSidechain": false,
  "promptId": "0c201752-9958-4eef-a252-56537162bf6a",
  "type": "user",
  "uuid": "32e78fe6-635c-4bad-a33f-6221631679bb",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "f477a79d-e124-4ff5-a240-8105c1f8499e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T07:47:28.521Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch all six missing papers in parallel to verify their content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32e78fe6-635c-4bad-a33f-6221631679bb",
  "isSidechain": false,
  "requestId": "req_011CatX3gpQSmsG37sxm2chX",
  "type": "assistant",
  "uuid": "a3f62aad-e4f0-49a3-98e8-0eea2b601c50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BXwZ1n9UVfyumZ37PMpjrg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1746,
      "cache_read_input_tokens": 27614,
      "output_tokens": 718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 718,
          "cache_read_input_tokens": 27614,
          "cache_creation_input_tokens": 1746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1746
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

_source line 13 · 2026-05-10T07:47:29.331Z_

Now fetching all six missing papers in parallel to verify their content before writing the revision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3f62aad-e4f0-49a3-98e8-0eea2b601c50",
  "isSidechain": false,
  "requestId": "req_011CatX3gpQSmsG37sxm2chX",
  "type": "assistant",
  "uuid": "932931b3-84a4-41ca-a147-0d18785efb5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BXwZ1n9UVfyumZ37PMpjrg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1746,
      "cache_read_input_tokens": 27614,
      "output_tokens": 718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 718,
          "cache_read_input_tokens": 27614,
          "cache_creation_input_tokens": 1746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1746
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

_source line 14 · 2026-05-10T07:47:33.249Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BvVRn3NUsoBxuZ4m28ufm7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.25947",
  "prompt": "Extract the title, authors, venue/conference, abstract, and key methodology. What does this paper study about multilingual data mixtures? What scale of models and languages does it cover?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "932931b3-84a4-41ca-a147-0d18785efb5f",
  "isSidechain": false,
  "requestId": "req_011CatX3gpQSmsG37sxm2chX",
  "type": "assistant",
  "uuid": "cb1837a5-9a78-41df-a6f0-3529aeae77e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BXwZ1n9UVfyumZ37PMpjrg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1746,
      "cache_read_input_tokens": 27614,
      "output_tokens": 718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 718,
          "cache_read_input_tokens": 27614,
          "cache_creation_input_tokens": 1746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1746
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

_source line 15 · 2026-05-10T07:47:33.746Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CSB43Prn9vR2YTsf8PSP6n`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.10229",
  "prompt": "Extract the title, authors, venue/conference, abstract, and key methodology. What is LangGPS? How does it select multilingual instruction data? What languages does it cover? What is its evaluation setup?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb1837a5-9a78-41df-a6f0-3529aeae77e7",
  "isSidechain": false,
  "requestId": "req_011CatX3gpQSmsG37sxm2chX",
  "type": "assistant",
  "uuid": "80e2f01c-b353-40d7-b8bb-01f5038a645d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BXwZ1n9UVfyumZ37PMpjrg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1746,
      "cache_read_input_tokens": 27614,
      "output_tokens": 718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 718,
          "cache_read_input_tokens": 27614,
          "cache_creation_input_tokens": 1746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1746
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

_source line 16 · 2026-05-10T07:47:33.809Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WzvAe93iX6KSy2N2YfQS3Y`</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.02460",
  "prompt": "Extract the title, authors, venue/conference, abstract, and key methodology. What is the code-switching curriculum? What stages does it have? What languages/tasks does it target?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80e2f01c-b353-40d7-b8bb-01f5038a645d",
  "isSidechain": false,
  "requestId": "req_011CatX3gpQSmsG37sxm2chX",
  "type": "assistant",
  "uuid": "50eba097-39d3-44f9-86b2-5ef14f44d763",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BXwZ1n9UVfyumZ37PMpjrg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1746,
      "cache_read_input_tokens": 27614,
      "output_tokens": 718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 718,
          "cache_read_input_tokens": 27614,
          "cache_creation_input_tokens": 1746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1746
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

_source line 17 · 2026-05-10T07:47:35.054Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015LT8ru4jkxiZ6MuhnoQFSo`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.13647",
  "prompt": "Extract the title, authors, venue/conference, abstract, and key methodology. Is this about Kazakh instruction tuning? How many examples? What model is fine-tuned? What benchmarks are used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50eba097-39d3-44f9-86b2-5ef14f44d763",
  "isSidechain": false,
  "requestId": "req_011CatX3gpQSmsG37sxm2chX",
  "type": "assistant",
  "uuid": "00d6549f-624a-41b8-be51-7aa661f48255",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BXwZ1n9UVfyumZ37PMpjrg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1746,
      "cache_read_input_tokens": 27614,
      "output_tokens": 718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 718,
          "cache_read_input_tokens": 27614,
          "cache_creation_input_tokens": 1746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1746
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

_source line 18 · 2026-05-10T07:47:36.323Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014WKsh8QF4XnUFEGCamhJbi`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.27183",
  "prompt": "Extract the title, authors, venue/conference, abstract, and key methodology. How does this extend URIEL+? How many languages does it cover? What new features does it add?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00d6549f-624a-41b8-be51-7aa661f48255",
  "isSidechain": false,
  "requestId": "req_011CatX3gpQSmsG37sxm2chX",
  "type": "assistant",
  "uuid": "bba9e542-ff84-438e-96fc-417110f3fb8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BXwZ1n9UVfyumZ37PMpjrg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1746,
      "cache_read_input_tokens": 27614,
      "output_tokens": 718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 718,
          "cache_read_input_tokens": 27614,
          "cache_creation_input_tokens": 1746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1746
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

_source line 19 · 2026-05-10T07:47:37.617Z_

<details><summary>↩ Tool result · `toolu_01BvVRn3NUsoBxuZ4m28ufm7`</summary>

```text
# Paper Summary: Multilingual Data Mixtures in Language Model Pretraining

**Title:** "Revisiting Multilingual Data Mixtures in Language Model Pretraining"

**Authors:** Negar Foroutan, Paul Teiletche, Ayush Kumar Tarun, Antoine Bosselut

**Venue:** Under Review (arXiv preprint, submitted October 29, 2025)

**Abstract:** The researchers investigated how different multilingual data combinations affect LLM pretraining. They trained models on diverse language corpora to challenge prevailing assumptions about multilinguality trade-offs. Key findings include: combining English with multilingual data doesn't necessarily harm performance when languages have sufficient tokens; English serves effectively as a pivot language across language families; and increasing languages from 25 to 400 doesn't produce the expected "curse of multilinguality."

## Study Focus

This work examines whether "multilingual data, when balanced appropriately, can enhance language model capabilities" without performance degradation, particularly for low-resource languages.

## Scale & Coverage

- **Model sizes:** 1.1B and 3B parameter LLMs
- **Language diversity:** 25 to 400 languages across various corpora
- **Key insight:** Performance doesn't significantly degrade as language count increases at this model scale
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb1837a5-9a78-41df-a6f0-3529aeae77e7",
  "isSidechain": false,
  "promptId": "0c201752-9958-4eef-a252-56537162bf6a",
  "type": "user",
  "uuid": "45d9b240-1de3-489f-b8de-da9ddadfe529",
  "toolUseResult": {
    "bytes": 46842,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: Multilingual Data Mixtures in Language Model Pretraining\n\n**Title:** \"Revisiting Multilingual Data Mixtures in Language Model Pretraining\"\n\n**Authors:** Negar Foroutan, Paul Teiletche, Ayush Kumar Tarun, Antoine Bosselut\n\n**Venue:** Under Review (arXiv preprint, submitted October 29, 2025)\n\n**Abstract:** The researchers investigated how different multilingual data combinations affect LLM pretraining. They trained models on diverse language corpora to challenge prevailing assumptions about multilinguality trade-offs. Key findings include: combining English with multilingual data doesn't necessarily harm performance when languages have sufficient tokens; English serves effectively as a pivot language across language families; and increasing languages from 25 to 400 doesn't produce the expected \"curse of multilinguality.\"\n\n## Study Focus\n\nThis work examines whether \"multilingual data, when balanced appropriately, can enhance language model capabilities\" without performance degradation, particularly for low-resource languages.\n\n## Scale & Coverage\n\n- **Model sizes:** 1.1B and 3B parameter LLMs\n- **Language diversity:** 25 to 400 languages across various corpora\n- **Key insight:** Performance doesn't significantly degrade as language count increases at this model scale",
    "durationMs": 4365,
    "url": "https://arxiv.org/abs/2510.25947"
  },
  "sourceToolAssistantUUID": "cb1837a5-9a78-41df-a6f0-3529aeae77e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-10T07:47:38.016Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013ck7VEbbrpBq54aN1wNPxt`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.27651",
  "prompt": "Extract the title, authors, venue/conference, abstract, and key methodology. What is Budget-Xfer? What is the budget-constrained source language selection problem? What target languages and tasks does it evaluate on? How does it differ from typological-distance-based approaches?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45d9b240-1de3-489f-b8de-da9ddadfe529",
  "isSidechain": false,
  "requestId": "req_011CatX3gpQSmsG37sxm2chX",
  "type": "assistant",
  "uuid": "a53493e6-059f-4a5c-9daa-f6c682b6dbcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BXwZ1n9UVfyumZ37PMpjrg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1746,
      "cache_read_input_tokens": 27614,
      "output_tokens": 718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 718,
          "cache_read_input_tokens": 27614,
          "cache_creation_input_tokens": 1746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1746
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

_source line 21 · 2026-05-10T07:47:39.374Z_

<details><summary>↩ Tool result · `toolu_01WzvAe93iX6KSy2N2YfQS3Y`</summary>

```text
# Paper Summary: Code-Switching Curriculum Learning for Multilingual Transfer in LLMs

**Title:** Code-Switching Curriculum Learning for Multilingual Transfer in LLMs

**Authors:** Haneul Yoo, Cheonbok Park, Sangdoo Yun, Alice Oh, Hwaran Lee

**Venue:** Findings of ACL 2025

## Abstract Overview

The researchers address performance degradation in large language models for low-resource languages by proposing a training approach inspired by human second language acquisition. The method uses "the practice of language alternation in a conversation" to improve cross-lingual transfer capabilities.

## Code-Switching Curriculum Learning (CSCL)

CSCL comprises **three progressive stages**:

1. **Token-level code-switching** – alternating individual words between languages
2. **Sentence-level code-switching** – mixing full sentences from different languages
3. **Monolingual corpora** – pure single-language training data

This staged approach mimics how humans gradually develop multilingual proficiency.

## Languages & Models Tested

- **Primary focus:** Korean (low-resource)
- **Extended evaluation:** Japanese (high-resource) and Indonesian (low-resource)
- **Models used:** Qwen 2, Gemma 2, and Phi 3.5

The methodology demonstrates particular effectiveness "in low-resource settings where high-quality, monolingual corpora for language transfer are hardly available."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50eba097-39d3-44f9-86b2-5ef14f44d763",
  "isSidechain": false,
  "promptId": "0c201752-9958-4eef-a252-56537162bf6a",
  "type": "user",
  "uuid": "9ecb9ab7-6432-47e4-98d9-ce7f60ef19ca",
  "toolUseResult": {
    "bytes": 46676,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: Code-Switching Curriculum Learning for Multilingual Transfer in LLMs\n\n**Title:** Code-Switching Curriculum Learning for Multilingual Transfer in LLMs\n\n**Authors:** Haneul Yoo, Cheonbok Park, Sangdoo Yun, Alice Oh, Hwaran Lee\n\n**Venue:** Findings of ACL 2025\n\n## Abstract Overview\n\nThe researchers address performance degradation in large language models for low-resource languages by proposing a training approach inspired by human second language acquisition. The method uses \"the practice of language alternation in a conversation\" to improve cross-lingual transfer capabilities.\n\n## Code-Switching Curriculum Learning (CSCL)\n\nCSCL comprises **three progressive stages**:\n\n1. **Token-level code-switching** – alternating individual words between languages\n2. **Sentence-level code-switching** – mixing full sentences from different languages\n3. **Monolingual corpora** – pure single-language training data\n\nThis staged approach mimics how humans gradually develop multilingual proficiency.\n\n## Languages & Models Tested\n\n- **Primary focus:** Korean (low-resource)\n- **Extended evaluation:** Japanese (high-resource) and Indonesian (low-resource)\n- **Models used:** Qwen 2, Gemma 2, and Phi 3.5\n\nThe methodology demonstrates particular effectiveness \"in low-resource settings where high-quality, monolingual corpora for language transfer are hardly available.\"",
    "durationMs": 5562,
    "url": "https://arxiv.org/abs/2411.02460"
  },
  "sourceToolAssistantUUID": "50eba097-39d3-44f9-86b2-5ef14f44d763",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T07:47:39.640Z_

<details><summary>↩ Tool result · `toolu_015LT8ru4jkxiZ6MuhnoQFSo`</summary>

```text
# Paper Summary

**Title:** "Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh"

**Authors:** Nurkhan Laiyk, Daniil Orel, Rituraj Joshi, Maiya Goloburda, Yuxia Wang, Preslav Nakov, Fajri Koto

**Venue:** arXiv (Computer Science - Computation and Language category)

**Is this about Kazakh instruction tuning?** Yes, directly.

**Dataset Size:** 10,600 samples in the instruction-following dataset

**Models Fine-tuned:** Qwen, Falcon, and Gemma

**Methodology:** The researchers employed "LLM-assisted data generation, comparing open-weight and closed-weight models" with GPT-4o selected as the backbone. All dataset entries underwent manual verification for quality assurance.

**Benchmarks/Evaluation:** The paper demonstrates "consistent performance improvements in both multiple-choice and generative tasks" on the fine-tuned models.

**Key Focus:** The work addresses the gap in instruction tuning for low-resource languages by creating a dataset covering institutional and cultural knowledge relevant to Kazakhstan, particularly in procedural, legal, and governance domains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00d6549f-624a-41b8-be51-7aa661f48255",
  "isSidechain": false,
  "promptId": "0c201752-9958-4eef-a252-56537162bf6a",
  "type": "user",
  "uuid": "432e867f-3098-4fe9-a8f8-b02f08dce7f1",
  "toolUseResult": {
    "bytes": 46281,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** \"Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh\"\n\n**Authors:** Nurkhan Laiyk, Daniil Orel, Rituraj Joshi, Maiya Goloburda, Yuxia Wang, Preslav Nakov, Fajri Koto\n\n**Venue:** arXiv (Computer Science - Computation and Language category)\n\n**Is this about Kazakh instruction tuning?** Yes, directly.\n\n**Dataset Size:** 10,600 samples in the instruction-following dataset\n\n**Models Fine-tuned:** Qwen, Falcon, and Gemma\n\n**Methodology:** The researchers employed \"LLM-assisted data generation, comparing open-weight and closed-weight models\" with GPT-4o selected as the backbone. All dataset entries underwent manual verification for quality assurance.\n\n**Benchmarks/Evaluation:** The paper demonstrates \"consistent performance improvements in both multiple-choice and generative tasks\" on the fine-tuned models.\n\n**Key Focus:** The work addresses the gap in instruction tuning for low-resource languages by creating a dataset covering institutional and cultural knowledge relevant to Kazakhstan, particularly in procedural, legal, and governance domains.",
    "durationMs": 4577,
    "url": "https://arxiv.org/abs/2502.13647"
  },
  "sourceToolAssistantUUID": "00d6549f-624a-41b8-be51-7aa661f48255",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T07:47:39.975Z_

<details><summary>↩ Tool result · `toolu_01CSB43Prn9vR2YTsf8PSP6n`</summary>

```text
# LangGPS: Research Summary

**Title:** "LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning"

**Authors:** Yangfan Ye, Xiaocheng Feng, Xiachong Feng, Lei Huang, Weitao Ma, Qichen Hong, Yunfei Lu, Duyu Tang, Dandan Tu, and Bing Qin

**Venue:** AAAI 2026 Main Track (Accepted)

## What is LangGPS?

LangGPS is a lightweight framework designed to improve multilingual instruction tuning by selecting training data based on language separability—a metric measuring "how well samples in different languages can be distinguished in the model's representation space."

## Data Selection Methodology

The approach operates in two stages:
1. **Filtering** training data according to separability scores
2. **Refinement** of the selected subset using existing selection methods

This combination allows the framework to enhance the effectiveness of conventional selection approaches.

## Language Coverage & Evaluation

The research demonstrates results across **22 languages** and **six benchmarks**, showing particular improvements for:
- Understanding tasks
- Low-resource languages

## Key Findings

The study reveals that highly separable samples create clearer language boundaries and enable faster model adaptation, while low-separability samples function as "bridges for cross-lingual alignment." The research also identifies language separability as useful for multilingual curriculum learning approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80e2f01c-b353-40d7-b8bb-01f5038a645d",
  "isSidechain": false,
  "promptId": "0c201752-9958-4eef-a252-56537162bf6a",
  "type": "user",
  "uuid": "db187e38-1ec0-41c0-89ee-cbaa66eb9a31",
  "toolUseResult": {
    "bytes": 48534,
    "code": 200,
    "codeText": "OK",
    "result": "# LangGPS: Research Summary\n\n**Title:** \"LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning\"\n\n**Authors:** Yangfan Ye, Xiaocheng Feng, Xiachong Feng, Lei Huang, Weitao Ma, Qichen Hong, Yunfei Lu, Duyu Tang, Dandan Tu, and Bing Qin\n\n**Venue:** AAAI 2026 Main Track (Accepted)\n\n## What is LangGPS?\n\nLangGPS is a lightweight framework designed to improve multilingual instruction tuning by selecting training data based on language separability—a metric measuring \"how well samples in different languages can be distinguished in the model's representation space.\"\n\n## Data Selection Methodology\n\nThe approach operates in two stages:\n1. **Filtering** training data according to separability scores\n2. **Refinement** of the selected subset using existing selection methods\n\nThis combination allows the framework to enhance the effectiveness of conventional selection approaches.\n\n## Language Coverage & Evaluation\n\nThe research demonstrates results across **22 languages** and **six benchmarks**, showing particular improvements for:\n- Understanding tasks\n- Low-resource languages\n\n## Key Findings\n\nThe study reveals that highly separable samples create clearer language boundaries and enable faster model adaptation, while low-separability samples function as \"bridges for cross-lingual alignment.\" The research also identifies language separability as useful for multilingual curriculum learning approaches.",
    "durationMs": 6227,
    "url": "https://arxiv.org/abs/2511.10229"
  },
  "sourceToolAssistantUUID": "80e2f01c-b353-40d7-b8bb-01f5038a645d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruc…",
  "leafUuid": "db187e38-1ec0-41c0-89ee-cbaa66eb9a31",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise TWMP core problem and landscape for Round 7",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6"
}
```

---

### Tool result

_source line 26 · 2026-05-10T07:47:42.059Z_

<details><summary>↩ Tool result · `toolu_014WKsh8QF4XnUFEGCamhJbi`</summary>

```text
# URIEL+ Paper Summary

**Title:** "Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+"

**Authors:** Mason Shipton, York Hay Ng, Aditya Khan, Phuong Hanh Hoang, Xiang Lu, A. Seza Doğruöz, En-Shiun Annie Lee

**Venue:** LREC 2026

## Abstract
The research addresses data sparsity in URIEL+, a linguistic knowledge base. The authors note that the original resource suffered from "missing feature types, incomplete language entries, and limited genealogical coverage," particularly hindering low-resource language support.

## Extensions to URIEL+

The team made three primary improvements:

1. **Script Vectors**: Introduced writing system representations for 7,488 languages
2. **Language Integration**: Added 18,710 languages via Glottolog database connection
3. **Feature Propagation**: Expanded imputation across language family relationships for 26,449 languages

## Coverage & Impact

- **Language Coverage**: Increased by up to 19,015 languages (1,007% expansion)
- **Sparsity Reduction**: 14% decrease in script vector feature sparsity
- **Imputation Quality**: Metrics improved by up to 35%
- **Performance**: Cross-lingual transfer tasks showed gains reaching "up to 6% in certain setups"

## Key Methodology

The approach propagates typological and script features across genealogies, enabling better support for multilingual research particularly benefiting lower-resourced language communities.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bba9e542-ff84-438e-96fc-417110f3fb8c",
  "isSidechain": false,
  "promptId": "0c201752-9958-4eef-a252-56537162bf6a",
  "type": "user",
  "uuid": "0d22804a-69e0-46d8-aef7-8b88edc7e52c",
  "toolUseResult": {
    "bytes": 46772,
    "code": 200,
    "codeText": "OK",
    "result": "# URIEL+ Paper Summary\n\n**Title:** \"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+\"\n\n**Authors:** Mason Shipton, York Hay Ng, Aditya Khan, Phuong Hanh Hoang, Xiang Lu, A. Seza Doğruöz, En-Shiun Annie Lee\n\n**Venue:** LREC 2026\n\n## Abstract\nThe research addresses data sparsity in URIEL+, a linguistic knowledge base. The authors note that the original resource suffered from \"missing feature types, incomplete language entries, and limited genealogical coverage,\" particularly hindering low-resource language support.\n\n## Extensions to URIEL+\n\nThe team made three primary improvements:\n\n1. **Script Vectors**: Introduced writing system representations for 7,488 languages\n2. **Language Integration**: Added 18,710 languages via Glottolog database connection\n3. **Feature Propagation**: Expanded imputation across language family relationships for 26,449 languages\n\n## Coverage & Impact\n\n- **Language Coverage**: Increased by up to 19,015 languages (1,007% expansion)\n- **Sparsity Reduction**: 14% decrease in script vector feature sparsity\n- **Imputation Quality**: Metrics improved by up to 35%\n- **Performance**: Cross-lingual transfer tasks showed gains reaching \"up to 6% in certain setups\"\n\n## Key Methodology\n\nThe approach propagates typological and script features across genealogies, enabling better support for multilingual research particularly benefiting lower-resourced language communities.",
    "durationMs": 5733,
    "url": "https://arxiv.org/abs/2510.27183"
  },
  "sourceToolAssistantUUID": "bba9e542-ff84-438e-96fc-417110f3fb8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T07:47:43.062Z_

<details><summary>↩ Tool result · `toolu_013ck7VEbbrpBq54aN1wNPxt`</summary>

```text
# Budget-Xfer: Paper Summary

**Title:** "Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages"

**Authors:** Tewodros Kederalah Idris, Roald Eiselen, Prasenjit Mitra

**Venue:** SIGIR 2026 Short Paper track

## What is Budget-Xfer?

Budget-Xfer is a framework that tackles multi-source cross-lingual transfer learning by treating it as "a budget-constrained resource allocation problem." Rather than simply selecting source languages, the system simultaneously decides which languages to include and how much training data to allocate from each, given a fixed annotation budget.

## The Core Problem

The research identifies a critical flaw in existing approaches: traditional source language comparisons don't control for total training data volume, making it impossible to distinguish whether performance gains come from better language selection or simply from using more data. Budget-Xfer solves this by keeping total annotation resources constant.

## Evaluation Scope

The framework was tested on:
- **Target languages:** Hausa, Yoruba, Swahili (African languages)
- **Tasks:** Named entity recognition (NER) and sentiment analysis
- **Scale:** 288 experiments across two multilingual models

## Key Differences from Typological Approaches

The research reveals that "the value of embedding similarity as a selection proxy is task-dependent," with random selection actually outperforming similarity-based methods for NER. This suggests typological distance measures don't reliably predict cross-lingual transfer success across different tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a53493e6-059f-4a5c-9daa-f6c682b6dbcc",
  "isSidechain": false,
  "promptId": "0c201752-9958-4eef-a252-56537162bf6a",
  "type": "user",
  "uuid": "b96e3f61-09ec-4940-a932-e656025b91a1",
  "toolUseResult": {
    "bytes": 46700,
    "code": 200,
    "codeText": "OK",
    "result": "# Budget-Xfer: Paper Summary\n\n**Title:** \"Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages\"\n\n**Authors:** Tewodros Kederalah Idris, Roald Eiselen, Prasenjit Mitra\n\n**Venue:** SIGIR 2026 Short Paper track\n\n## What is Budget-Xfer?\n\nBudget-Xfer is a framework that tackles multi-source cross-lingual transfer learning by treating it as \"a budget-constrained resource allocation problem.\" Rather than simply selecting source languages, the system simultaneously decides which languages to include and how much training data to allocate from each, given a fixed annotation budget.\n\n## The Core Problem\n\nThe research identifies a critical flaw in existing approaches: traditional source language comparisons don't control for total training data volume, making it impossible to distinguish whether performance gains come from better language selection or simply from using more data. Budget-Xfer solves this by keeping total annotation resources constant.\n\n## Evaluation Scope\n\nThe framework was tested on:\n- **Target languages:** Hausa, Yoruba, Swahili (African languages)\n- **Tasks:** Named entity recognition (NER) and sentiment analysis\n- **Scale:** 288 experiments across two multilingual models\n\n## Key Differences from Typological Approaches\n\nThe research reveals that \"the value of embedding similarity as a selection proxy is task-dependent,\" with random selection actually outperforming similarity-based methods for NER. This suggests typological distance measures don't reliably predict cross-lingual transfer success across different tasks.",
    "durationMs": 5045,
    "url": "https://arxiv.org/abs/2603.27651"
  },
  "sourceToolAssistantUUID": "a53493e6-059f-4a5c-9daa-f6c682b6dbcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T07:52:45.079Z_

<details><summary>Logged reasoning block</summary>

```text
I now have all the information I need. Let me analyze each paper carefully:

1. **Foroutan et al. (arXiv:2510.25947)** - "Revisiting Multilingual Data Mixtures in Language Model Pretraining"
   - Under review at ICLR (submitted Oct 2025)
   - Studies multilingual data combinations at pretraining scale (1.1B-3B parameters)
   - 25 to 400 languages
   - Key finding: English serves as pivot across language families; combining multilingual data doesn't necessarily harm performance
   - The reviewer's suggested text correctly characterizes this: "studies reweighting across 25–400 languages at pretraining scale (1.1B–3B parameters); TWMP operates at instruction-tuning scale—10 epochs, LoRA, narrow near-family pivot pool—where the data volume, optimization dynamics, and gradient signal are qualitatively different from the pretraining regime."
   
2. **LangGPS (arXiv:2511.10229)** - "LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning"
   - AAAI 2026 Main Track
   - Leverages language separability scores derived from the model's representation space to select data, tested across 22 languages and 6 benchmarks
   - Differs from TWMP in that it relies on internal representation features rather than external typological knowledge, and lacks the staged curriculum or multi-source DPO components

3. **Code-Switching Curriculum (arXiv:2411**

Now looking at the code-switching approach from Yoo et al., which uses a three-stage progression from token-level mixing through sentence-level to monolingual data, focusing primarily on Korean with Japanese and Indonesian as secondary languages—this is distinct from TWMP's multi-pivot language strategy without code-switching integration. The next paper examines a case study in Kazakh using GPT-4o-assisted data creation to fine-tune various model architectures.

Continuing through the related work, I see URIEL+ has expanded significantly to cover 26,449 languages through script vectors and Glottolog integration, though TWMP relies on the base COLING 2025 version which already provides adequate coverage. Budget-Xfer addresses source language selection constraints specifically for African language transfer, which is another angle on the cross-lingual transfer problem. TWMP should clarify that its typological-distance weighting applies specifically to instruction tuning rather than classification tasks like those in Budget-Xfer. The reviewer's feedback is accurate—these are all minor writing changes and citation additions, so this qualifies as a minor revision. Budget-Xfer's key insight about random selection outperforming similarity-based methods for NER is particularly relevant here since it highlights how task-dependent these selection strategies are.

Now I'm preparing the revised JSON with the new citations. I need to add six papers to the landscape section with the exact text the reviewer provided, fix the per-instruction fallback description, add six papers to key references, and update the overall description to reflect these additions. The landscape additions will include the Foroutan et al. paper on multilingual data mixtures, which operates at pretraining scale with much larger parameter counts and data volumes compared to TWMP's instruction-tuning approach. The Code-Switching Curriculum approach differs from TWMP in that it focuses on a single language pair with token-to-monolingual progression, whereas TWMP orchestrates multiple typologically-ordered pivot languages without code-switching to target related agglutinative languages. I'm also noting how TWMP's approach contrasts with language-specific instruction tuning efforts like the Kazakh dataset work, since TWMP requires no target-language labels and generalizes across Mongolian, Uyghur, and other low-resource settings where such datasets don't exist. Finally, while concurrent work is expanding URIEL+ with script vectors and genealogical data, TWMP builds on the established COLING 2025 version of the typological resource. I'm finishing the fallback description—when instructions don't yield target-language candidates after filtering, they revert to SFT-weighted sampling, and I'll track the fallback rate as a characterization metric alongside the prerequisite probe. Now I'm structuring the JSON update to integrate the six new papers into the landscape, prioritizing LangGPS as the most critical addition since it's a peer-reviewed AAAI 2026 competitor on multilingual instruction tuning, then positioning the others near relevant discussion points about data mixtures and curriculum learning. I'm adding the URIEL+ expansion details to the approach section and fixing the fallback mechanism description to clarify how instructions with empty candidate pools are handled through the SFT-weighted sampling objective, then reporting the per-source-target fallback rates as a characterization result. I need to update the description field to mention LangGPS as a key addition and note the fallback mechanism fix. I'm also realizing Budget-Xfer is at SIGIR 2026, not EMNLP—the reviewer was referring to EMNLP as a potential venue for TWMP, so I should add the SIGIR venue to the key_references entry. For Foroutan et al., I need to check whether it's still under review or has been published since the WebFetch showed it as submitted in October.

Now I'm organizing the landscape section additions by theme: LangGPS goes after CLO since it's about multilingual instruction tuning data selection, Foroutan et al. fits near the pretraining discussion, Budget-Xfer belongs near the parallel discussion, Code-Switching Curriculum goes with curriculum learning, and Laiyk et al. should be near Sherkala-Chat since both are Kazakh-specific. Let me structure the full JSON output with these changes integrated. Now I'm positioning Laiyk et al. alongside Sherkala-Chat since they both focus on Kazakh-specific work, then I'll compile the complete JSON with all six new papers integrated into the key_references section and landscape accordingly. PLUG showed English-pivot instruction generation works for typologically similar languages like Chinese and Spanish, but I'm testing whether that advantage extends to agglutinative languages with non-Latin scripts like Kazakh and Mongolian—something PLUG didn't validate. CLO improves efficiency through cross-lingual preference optimization but locks English as the sole source language, whereas I'm varying source selection by typological distance. LangGPS uses representation-space separability scores to select multilingual instruction data across 22 languages, but my approach directly leverages typological structure rather than learned separability metrics.

Compared to these methods, TWMP's key distinction is using external typological features to establish a pivot ordering independent of training dynamics, combined with a staged curriculum and multi-source DPO objective that neither LangGPS nor Budget-Xfer address. Budget-Xfer treats multi-source transfer as a budget allocation problem for NER and sentiment tasks, but doesn't provide the principled ordering mechanism that typological distance weighting gives. Code-Switching Curriculum Learning proposes a three-stage progression for a single language pair, whereas I'm operating over a pool of typologically ordered pivots targeting multiple related agglutinative languages without code-switching. Finally, Revisiting Multilingual Data Mixtures studies reweighting across hundreds of languages at pretraining scale with billions of parameters, while my work operates at the instruction-tuning scale with LoRA and a much smaller training budget.

Sherkala-Chat directly motivates the approach by showing Turkish improves Kazakh performance, but it relies on full fine-tuning with ad-hoc language selection rather than a generalizable recipe. I'm providing a LoRA-based method parameterized by continuous URIEL+ distances that applies to any agglutinative target, replacing language-specific engineering with principled pivot selection. Unlike Laiyk et al., which requires target-language instruction examples, my approach doesn't depend on any target-language data.

The next work on implicit cross-lingual rewarding achieves strong improvements through English-only reward transfer, but without typological weighting—I'm extending that to multi-pivot selection weighted by linguistic distance and focusing on low-resource agglutinative languages they don't cover. Family Matters demonstrates that typological proximity helps with transfer, but it's a single-language case study rather than a generalizable framework.

Cross-linguistic transfer research has analyzed language family and morphology effects empirically, and recent work on LoRA merging decouples task and language adapters, though neither uses typological features to weight the language component. There's also concurrent work enforcing factual consistency across 26 languages through DPO-style preference pairs, but that's orthogonal to what I'm doing—they're targeting semantic equivalence while I'm focused on alignment quality through typologically-informed training.

Now I'm distinguishing TWMP from TIPA, which aggregates existing MAD-X adapters weighted by typological similarity across 230+ languages entirely at inference time without training. The key differences are that TIPA is training-free adapter aggregation versus my typologically-weighted curriculum learning, and it operates on encoder-based modules for classification while I'm targeting decoder language models.

The second comparison is with 'Linguistically-Informed Multilingual Instruction Tuning', which uses k-means clustering on URIEL TYPO vectors to select 14 representative languages from 52 for LoRA fine-tuning. My approach diverges significantly—I'm using continuous inverse-distance sampling weights across the full Aya collection with compact URIEL+ features, adding a staged cosine-distance curriculum schedule, and integrating multi-source DPO preference optimization for language fidelity.

Crucially, I'm directly targeting Kazakh, Mongolian, and Uyghur, which have zero coverage in that prior work's evaluation suite. The combination of continuous URIEL+ weighting, staged curriculum, multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering these target languages represents a principled differentiation.

For the approach section, I need to clarify the URIEL+ expansion and fix the fallback sentence. After explaining how URIEL+ captures Kazakh's multi-script properties, I should note that while a concurrent LREC 2026 extension adds script vectors and genealogies to cover more languages, TWMP uses the COLING 2025 base version with SoftImpute, which already provides sufficient feature coverage and the Laplacian-selected 300-feature subset needed for the pivot languages.

For the fallback behavior, instead of saying instructions with no candidates are discarded, I should clarify that they fall back to SFT-weighted sampling for that instruction, and I'll report the per-source-target fallback rate as a characterization result alongside the prerequisite probe.

Now I need to write out the complete JSON output carefully, making sure to incorporate the key new additions like LangGPS and Budget-Xfer into the description, and also update the fallback text to match this clarification rather than the old "discarded" language. I'm adding the key references with their differentiators—Foroutan et al. on multilingual pretraining reweighting, LangGPS using language separability scores across 22 languages, and a code-switching curriculum approach for language pairs, each contrasted against TWMP's specific methodology. arXiv:2510.27183) extends URIEL+ with script vectors and genealogical data covering 26,449 languages, and TWMP leverages the COLING 2025 version which gives us sufficient coverage for the Aya pivot selection. Budget-Xfer (arXiv:2603.27651) tackles multi-source cross-lingual transfer as a budget-constrained problem for African language NER and sentiment tasks, but it doesn't use typological features or curriculum staging like TWMP does.

Now I need to refine the approach section with two key updates: first, clarifying how URIEL+ handles Kazakh's script properties and situating it within the broader LREC extension, and second, changing how we handle instructions that don't yield target candidates—instead of discarding them, they'll fall back to SFT-weighted sampling, and I'll track the fallback rate as a characterization metric.

For the description field, I'm reconsidering what to emphasize. The text is already quite dense, so I'll integrate mentions of LangGPS as a point of differentiation (showing how our typological approach differs from representation-space methods), add Budget-Xfer where relevant, and incorporate the URIEL+ expansion details. I need to locate the right spots in the description to weave these in naturally without making it unwieldy.

Now I'm ready to construct the full JSON output. But first, let me verify the venue information for arXiv:2502.13647—the reviewer notes it as ACL 2025 Long, but I should confirm whether the WebFetch data aligns with that or if it's still showing as a preprint.

For arXiv:2510.25947, the reviewer indicates it's ICLR-submitted, so I'll use that designation even though the WebFetch shows "Under Review."

I'm organizing the landscape additions strategically: LangGPS follows CLO since both address multilingual instruction data selection, then Budget-Xfer for its multi-source selection focus, and Code-Switching Curriculum for curriculum-related work. PLUG showed English-pivot cross-lingual instruction generation works well for Romance and East Asian languages, but whether that advantage extends to typologically distant agglutinative languages like Kazakh remains untested—something TWMP directly investigates. CLO uses DPO-style preference optimization with machine-translated data but locks English as the sole source language, whereas LangGPS selects instruction data based on the model's own representation space across 22 languages. TWMP differs by leveraging external typological features from URIEL+ to determine pivot ordering independent of training dynamics, and combines staged curriculum learning with multi-source DPO in ways LangGPS doesn't.

Budget-Xfer frames multi-source transfer as a budget allocation problem for specific tasks, but TWMP's typological weighting and curriculum provide a more principled ordering mechanism for instruction tuning. Code-Switching Curriculum Learning proposes a three-stage progression for single language pairs, while TWMP operates over a pool of typologically ordered pivots targeting a set of related agglutinative languages instead. Revisiting Multilingual Data Mixtures studies reweighting at pretraining scale across hundreds of languages, whereas TWMP operates at the instruction-tuning scale with LoRA and a narrow pivot pool, where the data volume and optimization dynamics are fundamentally different.

Sherkala-Chat demonstrates that Turkish improves Kazakh performance when trained together, which directly motivated TWMP's inclusion of Turkic pivots, but unlike that work's Kazakh-specific full fine-tuning with ad-hoc language selection, TWMP provides a generalizable LoRA-based approach parameterized by continuous typological distances that applies to any agglutinative target language with principled pivot selection. Laiyk et al. fine-tune on GPT-4-assisted Kazakh instruction examples, whereas TWMP requires no target-language labels and extends equally to Mongolian and Uyghur where such datasets don't exist.

Implicit Cross-Lingual Rewarding uses English as the sole source with implicit reward annotation, achieving strong improvements on X-AlpacaEval, but TWMP extends this by weighting multiple pivot sources by typological distance and targeting low-resource agglutinative languages absent from that work. Family Matters shows that typological proximity helps with language transfer and LoRA merging for Faroese, but it's a single-language case study without a generalizable recipe. I'm also looking at how language family and morphology effects are analyzed empirically across cross-linguistic transfer work.

Now I'm examining several concurrent and related approaches. Multi-Linguistic LoRA Merging decouples task and language adapters but doesn't use typological features to weight them. There's a concurrent DPO-inspired method that enforces factual consistency across 26 languages and 9 LLMs—this is orthogonal to TWMP since it addresses knowledge coherence across languages rather than instruction-language fidelity when responding in multiple pivot languages, and it doesn't tackle low-resource instruction tuning or typological weighting. I'm also differentiating TWMP from TIPA, which constructs proxy language adapters by aggregating existing models.

TIPA differs fundamentally: it's training-free inference-time aggregation using typological similarity across 230+ languages, whereas TWMP learns from a typologically-weighted curriculum; TIPA works on encoder-based classification modules rather than decoder LLM instruction tuning; and it hasn't been applied to instruction generation or languages without dedicated adapters. There's also a recent approach using URIEL typological vectors with k-means clustering to select 14 representative languages from 52 for LoRA fine-tuning on Bactrian-X, showing typologically diverse selection outperforms random selection—but TWMP takes a substantially different approach.

Instead of discrete cluster representatives, I'm applying continuous inverse-distance sampling weights across the full Aya collection using compact URIEL+ features selected via Laplacian Score, adding a staged cosine-distance curriculum schedule and multi-source DPO preference optimization for language fidelity. Critically, TWMP directly targets Kazakh, Mongolian, and Uyghur—languages that receive zero coverage in the prior work's evaluation suite—and the combination of continuous URIEL+ weighting, staged curriculum, multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering these target languages represents a principled differentiation.

Now I'm refining the approach section by adding an expansion on how URIEL+ captures Kazakh's multi-script properties and fixing the fallback mechanism so that instructions with no target-language candidates after filtering fall back to SFT-weighted sampling rather than being discarded, with the per-source-target fallback rate reported as a characterization result. tuning, which replaces PLUG's single-English pivot with a principled mixture over multiple source languages drawn from the Aya collection (513M instances across 114 languages).

Aya pivot coverage is verified before training: Turkish (high-resource, multi-million instances), Kyrgyz (~4.1M instances in the Aya collection language split), Uzbek (confirmed present as an underrepresented language with meaningful coverage), and Azerbaijani all qualify as pivot sources. A minimum threshold of 5,000 Aya instances per pivot language is enforced; languages below this threshold are excluded from the mixture. All qualifying pivot languages and their instance counts are reported in an appendix table. Kazakh, Mongolian, and Uyghur serve exclusively as evaluation targets and are never included in the pivot mixture.

For typological distances, I'm using URIEL+ instead of the legacy lang2vec approach—it covers 4,366 languages with roughly 800 features spanning grammar, syntax, morphology, and sound properties, plus SoftImpute for handling missing values in sparse languages like Kazakh, Uzbek, and Kyrgyz. URIEL+ also captures Kazakh's multi-script nature through dedicated script vectors, and a concurrent extension adds even broader genealogical and script coverage, though I'm working with the COLING 2025 base version here.

Following recent work showing that a Laplacian-selected 300-feature subset of URIEL+ actually outperforms the full 800-feature set on typological tasks and improves downstream cross-lingual performance, I apply this feature selection before computing cosine distances between languages. The data-sampling weights are then inversely proportional to these distances, so morphologically similar pivots like Turkish or Uzbek get substantially higher weight than English when training on Kazakh.

For the curriculum, I'm calibrating three training phases based on the distance distribution of qualifying Aya pivot languages relative to each target. I compute the 25th and 60th percentile distances once before training—for Kazakh these are roughly 0.32 and 0.56 respectively. Stage 1 uses only the closest pivots, Stage 2 expands to mid-distance languages, and Stage 3 trains on the full mixture with continuous inverse-distance weighting, with thresholds computed specifically for each target language.

Mongolian is an interesting edge case where no Turkic pivot falls within the closest percentile, so I use the nearest available sources (Korean, Finnish, Turkish) across all stages with appropriately small weights. I'm comparing this curriculum approach against baselines: no curriculum at all, a 2-stage variant, and linear interpolation between stages.

For the preference optimization, I'm extending the CLO-style DPO objective to handle multiple source languages. Each preference pair consists of a chosen example pairing a source instruction with a model response in the target language, contrasted against a rejected example using the same source instruction but a lower-quality response in the source language.

This inverts CLO's original design—where English inputs prefer English responses to preserve English capability—because my goal is the opposite: I want the model to follow instructions in any source language while responding in the target language. I'm constructing these preference pairs automatically using language identification on sampled model outputs rather than relying on target-language labels.

For each source-language instruction, I sample multiple candidate responses, use fastText to identify which ones are in the target language versus the source language, filter out anything under 20 tokens to remove low-quality outputs, then pair the highest-confidence target-language response with the lowest-confidence source-language response. If an instruction doesn't produce any valid target-language candidates after filtering, I fall back to the SFT-weighted sampling approach instead, and I'm tracking how often this happens as a quality metric.

Before running the full DPO training, I run a prerequisite check on 500 instructions per language pair using the base Qwen3.5-9B model to verify that target-language responses meeting the 20-token threshold appear in at least 5% of the K=8 samples—if a language pair fails this check, I exclude it from DPO and use SFT-weighted sampling only. This tells me which language pairs are viable for cross-lingual preference learning, especially for distant pairs like English-to-Mongolian where the base model might struggle.

Now I'm setting up QLoRA fine-tuning on Qwen3.5-9B...

For evaluation, I'm using three ACL 2025 benchmarks—KazMMLU for Kazakh, MiLiC-Eval covering all three target languages across 9 tasks, and TUMLU for within-Turkic comparisons—with PLUG and CLO as baselines. I'm also running ablations on the typological weighting to compare the full 800-feature URIEL+ representation against reduced feature sets like Laplacian-selected 300 features, syntax-only, morphology-only, and the k-means discrete baseline.

For generalization testing, I'm holding out Swahili as an agglutinative language that wasn't touched during hyperparameter tuning. I should note that TyDi QA, while covering ten languages, doesn't include any of my three primary targets—Kazakh, Mongolian, or Uyghur—so it's not part of this evaluation.

Now I'm working through the description field, which needs to incorporate several related papers. I'm adding mentions of LangGPS, which uses language separability scores from model representations across 22 languages, contrasting with my approach of using external URIEL+ typological features. Budget-Xfer frames multi-source transfer as a budget allocation problem for NER and sentiment tasks without relying on typological information or curriculum ordering. I'm also noting that a concurrent LREC 2026 extension covers significantly more languages than the COLING 2025 base version I'm using.

For the fallback mechanism, the description already clarifies that pairs failing the 500-instruction prerequisite probe fall back to SFT-only training, and I should make sure to report the per-source-target fallback rates to show how often this happens across different language pairs.

Now I'm ready to construct the complete JSON with all the methodology details properly documented. The three benchmarks provide concrete evidence: KazMMLU contains 23K authentic Kazakh educational questions where all tested models show substantial gaps despite the language having 20 million speakers; MiLiC-Eval spans four languages with 24K instances and reveals that even GPT-4o-mini performs barely above random on Mongolian while showing only preliminary understanding of Tibetan and Kazakh; TUMLU further documents these performance disparities across Turkic languages.

Now looking at approaches to address these gaps—TUMLU's 38K native questions enable controlled comparisons isolating the effect of training corpus size, while XLM-SWCM demonstrates that encoder-based cross-lingual pretraining can partially close the gap (though Kazakh still achieves the lowest ROUGE-L score at 5.6) but doesn't scale to decoder-based instruction-following. Most promisingly, CLO shows that cross-lingual preference optimization with just 3,200 samples outperforms standard supervised fine-tuning with 6,400 samples, suggesting a more efficient path forward.

This creates a clear opportunity: by weighting instruction data from multiple source languages based on typological distance and introducing a staged curriculum, I can build a multi-pivot training approach that directly sidesteps the English-pivot bottleneck for agglutinative low-resource languages. The existing literature on English-pivot instruction generation (PLUG) showed 29% improvements, but only on typologically similar languages like Chinese, Korean, Italian, and Spanish—whether this advantage extends to agglutinative languages with non-Latin scripts like Kazakh, Mongolian, and Uyghur is precisely what needs testing rather than assumed.

Looking at related work, CLO improves data efficiency through cross-lingual preference optimization but fixes English as the sole source without varying selection by typological distance. LangGPS selects multilingual instruction data based on the model's own representation space and shows improvements across 22 languages, but it relies on training dynamics rather than external typological features like URIEL+, and doesn't incorporate a staged curriculum or multi-source DPO. Budget-Xfer frames multi-source transfer as a budget allocation problem for NER and sentiment tasks, but lacks the principled typological ordering and curriculum staging that instruction tuning requires. Code-Switching Curriculum Learning proposes a three-stage progression for single language pairs, whereas my approach operates over a typologically ordered pool of multiple pivots simultaneously.

At the pretraining scale, Revisiting Multilingual Data Mixtures studies reweighting across hundreds of languages with billions of parameters, but instruction tuning operates in a fundamentally different regime—limited epochs, LoRA, and a narrow pivot pool where gradient dynamics are qualitatively distinct. Sherkala-Chat demonstrates that Turkish as an auxiliary language benefits Kazakh performance through full fine-tuning on a four-language mixture, which directly motivates my inclusion of Turkic pivots, but my approach generalizes this insight with a systematic typological framework rather than ad-hoc language selection.

TWMP provides a principled, reusable LoRA recipe parameterized by continuous URIEL+ distances that applies to any agglutinative target language, whereas Laiyk et al. requires target-language instruction labels—a constraint that doesn't exist for Mongolian and Uyghur where no comparable annotated datasets are available. Implicit Cross-Lingual Rewarding uses English as the sole source for reward transfer and achieves strong improvements on X-AlpacaEval, but it still relies on implicit annotation from an English-aligned model rather than operating directly on the target language.

Looking at related work, 'Family Matters' demonstrates that typological proximity helps through LoRA merging on Faroese, but it's a single-language case study without a generalizable recipe. 'Cross-Linguistic Transfer in Multilingual NLP' analyzes morphology effects empirically but doesn't propose a training method. Multi-Linguistic LoRA Merging decouples task and language adapters but doesn't use typological features to weight them. The concurrent DPO-inspired method from Tianyu Liu et al. appears to be moving in a similar direction, though the details are still emerging. with TWMP—that enforces factual consistency of model responses across 26 languages and 9 LLMs; its preference pairs encode semantic equivalence of knowledge across languages (chosen = factually consistent cross-lingual response, rejected = factually inconsistent response). This objective is orthogonal to TWMP's: DCO addresses what the model says across languages (knowledge coherence), while TWMP addresses which language it responds in when given instructions in any of multiple pivot languages (instruction-language fidelity). DCO does not address low-resource instruction tuning, multi-pivot source selection, or typological-distance weighting. Two works require careful differentiation from TWMP. First, TIPA constructs proxy language adapters by aggregating existing MAD-X adapters weighted by typological similarity across 230+ languages without any training, operating on encoder-based modules for classification rather than decoder LLM instruction tuning, and hasn't been applied to instruction generation or languages without dedicated adapters. Second, 'Linguistically-Informed Multilingual Instruction Tuning' uses discrete cluster-representative language selection for LoRA fine-tuning, whereas TWMP applies continuous inverse-distance sampling weights over the full Aya collection using compact URIEL+ features with a staged cosine-distance curriculum and multi-source DPO preference optimization, directly targeting Kazakh, Mongolian, and Uyghur on three ACL 2025 benchmarks where prior work provides zero coverage.

For TWMP itself, I'm using multiple source languages from the Aya collection as pivots—Turkish, Kyrgyz, Uzbek, and Azerbaijani all meet the 5,000-instance minimum threshold—while keeping Kazakh, Mongolian, and Uyghur exclusively as evaluation targets. Typological distances come from URIEL+ rather than legacy features, giving me access to 4,366 languages with approximately 800 features covering grammar and sound patterns, with SoftImpute handling missing values to reduce sparsity. Kazakh, Uzbek, and Kyrgyz, where legacy URIEL features are known to be sparse. URIEL+ explicitly represents Kazakh's multi-script properties (Cyrillic, Latin, and Arabic) via script vectors. A concurrent LREC 2026 extension adds script vectors and Glottolog genealogies to URIEL+, covering 26,449 languages; TWMP uses the COLING 2025 base version with SoftImpute, which already provides sufficient feature coverage and a Laplacian-selected 300-feature subset for the qualifying Aya pivot languages. Following recent work demonstrating that a 300-feature URIEL+ subset achieves better typological alignment and downstream cross-lingual NLP performance than the full 800-feature set, we apply this feature selection before computing cosine distances. Data-sampling weights are assigned inversely proportional to these distances, so morphologically close pivots like Turkish or Uzbek for Kazakh receive substantially higher weight than English.

The staged curriculum uses three phases calibrated by the empirical URIEL+ distance distribution of qualifying Aya pivot languages relative to each target language. Stage 1 (epochs 1–3) exclusively sources with the closest distances—for Kazakh, approximately ≤0.32, capturing Turkish, Kyrgyz, Uzbek, and Azerbaijani. Stage 2 (epochs 4–6) expands to mid-distance languages like Russian and Arabic. Stage 3 (epochs 7–10) uses the full mixture with continuous inverse-distance weights. Thresholds are target-specific; for Mongolian, where no Turkic pivot falls within the closest tier, the available sources are used across all stages with smaller weights—a controlled finding showing how distance constraints shape the curriculum.

The DPO preference optimization extends to the multi-source setting by defining chosen pairs as source-language instructions paired with target-language responses, and rejected pairs as the same instruction paired with source-language responses. This inverts CLO's preference structure because the goal is cross-lingual target-language instruction following rather than preserving English capability. Preference pairs are constructed entirely without target-language labels via automatic language identification, sampling K responses from each source-language instruction. Now I'm comparing different typological feature sets—the full 800-feature URIEL+ against Laplacian-selected 300 features, syntax-only, morphology-only, and the k-means baseline—to see which linguistic properties matter most for cross-lingual transfer. Swahili is held out as a test case for agglutinative languages not seen during tuning, and I'm noting that TyDi QA doesn't cover my target languages so it's not part of this evaluation. I'm working through how to integrate these recent papers into the description without making it too verbose. I need to add LangGPS and Budget-Xfer as key comparisons, plus brief mentions of Laiyk et al. for the Kazakh work and the Code-Switching Curriculum research. The main challenge is keeping the description concise while highlighting what makes TWMP distinct—it doesn't rely on target-language labels or external typological features the way these other approaches do. I need to finalize the JSON output with all the documentation updates—adding the concurrent LREC extension note to the URIEL+ description, clarifying the fallback behavior for instructions with no target-language candidates, and marking these as minor changes since they're purely editorial additions without methodological shifts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b96e3f61-09ec-4940-a932-e656025b91a1",
  "isSidechain": false,
  "requestId": "req_011CatX4viMRzCfXfNrLMyWr",
  "type": "assistant",
  "uuid": "67670851-273d-4c78-9ef0-a2643d99e3dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TH5rUo5mzuPTBXcc3jxWPN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2847,
      "cache_read_input_tokens": 29360,
      "output_tokens": 29240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2847,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 29240,
          "cache_read_input_tokens": 29360,
          "cache_creation_input_tokens": 2847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2847
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

_source line 29 · 2026-05-10T07:55:23.071Z_

All six papers verified. Key findings:
- **Foroutan et al.** (arXiv:2510.25947): ICLR-submitted, 1.1B–3B models, 25–400 languages at pretraining scale — clearly different regime from TWMP
- **LangGPS** (arXiv:2511.10229): AAAI 2026 main track, uses model-internal representation space for separability scoring, 22 languages — most important missing citation
- **Code-Switching Curriculum** (arXiv:2411.02460): ACL 2025 Findings, 3-stage curriculum for a single language pair (Korean primary) — different from TWMP's multi-pivot pool
- **Laiyk et al.** (arXiv:2502.13647): 10,600 GPT-4o-assisted Kazakh examples, fine-tunes Qwen/Falcon/Gemma — requires target labels unlike TWMP
- **URIEL+ expansion** (arXiv:2510.27183): LREC 2026 by Shipton et al., 26,449 languages via Glottolog — TWMP uses the COLING 2025 base which suffices
- **Budget-Xfer** (arXiv:2603.27651): SIGIR 2026 short paper, budget-constrained source selection for NER/sentiment on African languages — no typological features or curriculum

Assessment: this is genuinely a minor revision. The reviewer is correct — all 7 fixes are writing-only. The core method is sound; the repeated stagnation is purely citation debt. I'll now produce the complete revised JSON integrating all 7 items.

```json
{
  "title": "Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning",
  "change_type": "minor",
  "core_problem": "Cross-lingual instruction tuning for low-resource languages defaults to English as the sole pivot, creating systematic gaps for languages that are typologically distant from English—particularly those with agglutinative morphology, non-Latin scripts, or SOV word order. Three peer-reviewed ACL 2025 benchmarks—KazMMLU (Kazakh), MiLiC-Eval (Tibetan, Uyghur, Kazakh, Mongolian), and TUMLU (Turkic languages including Kazakh and Uyghur)—confirm that even frontier multilingual LLMs (GPT-4, Llama-3.1, Qwen-2.5) achieve near-random performance on Mongolian comprehension tasks and substantially below-par accuracy on Kazakh and Uyghur relative to typologically proximate high-resource languages. No existing instruction tuning method uses typological distance to continuously weight data-source selection across a multi-pivot mixture for these under-represented language families.",
  "opportunity": "Three complementary ACL 2025 benchmarks provide peer-reviewed grounding for the performance gap. KazMMLU (arXiv:2502.12829; ACL 2025 long paper) comprises 23K Kazakh-language questions spanning STEM, humanities, and social sciences sourced from authentic educational materials; evaluation of Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 shows 'substantial room for improvement' for all models on Kazakh, despite the language having 20 million speakers. MiLiC-Eval (arXiv:2503.01150; ACL 2025 Findings) covers Tibetan, Uyghur, Kazakh, and Mongolian across 9 tasks with 24K instances; GPT-4o-mini achieves only slightly above random on Mongolian tasks, and models exhibit only 'preliminary understanding' of Tibetan and Kazakh. TUMLU (arXiv:2502.11020; ACL 2025 long paper) provides 38K native questions spanning 11 academic subjects across Turkic languages including Kazakh and Uyghur, enabling controlled within-family comparisons that isolate the effect of lower training corpus size. The XLM-SWCM paper (arXiv:2502.10852) additionally shows that encoder-based shared-weight cross-lingual pretraining partially bridges these gaps—Kazakh ROUGE-L summarization score of 5.6 is notably the lowest among the four minority languages studied—but this approach does not scale to instruction-following for decoder LLMs. CLO (arXiv:2505.14297; ACL 2025) shows that DPO-style cross-lingual preference optimization with only 3,200 samples outperforms standard SFT with 6,400 samples, establishing strong data efficiency for cross-lingual transfer. These findings together create a clear opening: by weighting instruction data from multiple source languages inversely by URIEL+ typological distance and introducing a staged curriculum, we can build a principled multi-pivot training regime that directly addresses the English-pivot bottleneck for agglutinative low-resource targets.",
  "landscape": "PLUG (ACL 2024) established that English-pivot cross-lingual instruction generation improves multilingual instruction following—but its reported 29% improvement was measured on Chinese, Korean, Italian, and Spanish. Whether the English-pivot advantage holds for typologically distant agglutinative languages with non-Latin scripts (Kazakh, Mongolian, Uyghur) is an assumption that TWMP directly tests rather than takes for granted. CLO (arXiv:2505.14297; ACL 2025) improves data efficiency via DPO-style cross-lingual preference optimization using 6,400 OpenAssistant samples machine-translated by M2M100; it fixes English as the sole source language without varying source selection by typological distance. LangGPS [Ye et al., AAAI 2026, arXiv:2511.10229] selects multilingual instruction data based on language separability scores derived from the model's own representation space, demonstrating improvements across 22 languages including low-resource targets. Unlike LangGPS, TWMP uses external typological features from URIEL+ to derive a pivot ordering independent of training dynamics, and integrates a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer [arXiv:2603.27651, SIGIR 2026] formulates multi-source cross-lingual transfer as a budget-constrained allocation problem for NER/sentiment tasks; TWMP's typological-distance weighting and staged curriculum provide a principled ordering mechanism for instruction tuning that Budget-Xfer does not address. Code-Switching Curriculum Learning [Yoo et al., ACL 2025 Findings, arXiv:2411.02460] proposes a 3-stage curriculum (token-level → sentence-level → monolingual code-switching) for a single language pair; TWMP's curriculum operates over a pool of typologically ordered pivot languages without code-switching and targets a set of related agglutinative languages rather than a single target. Revisiting Multilingual Data Mixtures [Foroutan et al., 2025, arXiv:2510.25947] studies reweighting across 25–400 languages at pretraining scale (1.1B–3B parameters); TWMP operates at instruction-tuning scale—10 epochs, LoRA, narrow near-family pivot pool—where the data volume, optimization dynamics, and gradient signal are qualitatively different from the pretraining regime. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh, English, Russian, and Turkish, and demonstrates that Turkish as an auxiliary language improves Kazakh performance—directly motivating TWMP's inclusion of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc four-language selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language, with principled pivot selection replacing language-specific engineering. Laiyk et al. [ACL 2025 Long, arXiv:2502.13647] fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP does not require any target-language instruction labels and applies equally to Mongolian and Uyghur, where no comparable GPT-4-assisted dataset currently exists. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving a 12.72% average Win Rate improvement on X-AlpacaEval; it uses English as the sole source and implicit reward annotation without typological weighting—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from that work. 'Family Matters' (arXiv:2510.00810) applies language transfer and LoRA merging from typologically related Nordic languages to Faroese—demonstrating that typological proximity helps—but as a single-language case study with no generalizable training recipe. 'Cross-Linguistic Transfer in Multilingual NLP' (arXiv:2505.13908) analyzes language family and morphology effects empirically without proposing a training method. Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) decouples task and language LoRA adapters but does not use typological features to parameterize or weight the language adapter. 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678; Tianyu Liu et al., March 2026) introduces a DPO-inspired method—concurrent with TWMP—that enforces factual consistency of model responses across 26 languages and 9 LLMs; its preference pairs encode semantic equivalence of knowledge across languages (chosen = factually consistent cross-lingual response, rejected = factually inconsistent response). This objective is orthogonal to TWMP's: DCO addresses what the model says across languages (knowledge coherence), while TWMP addresses which language it responds in when given instructions in any of multiple pivot languages (instruction-language fidelity). DCO does not address low-resource instruction tuning, multi-pivot source selection, or typological-distance weighting. Two works require careful differentiation from TWMP. First, TIPA (arXiv:2601.16629; EACL 2026 Findings) constructs proxy language adapters by aggregating existing MAD-X adapters weighted by typological similarity across 230+ languages—entirely without training. TIPA is orthogonal to TWMP in three key ways: (1) it is training-free inference-time adapter aggregation, whereas TWMP learns from a typologically-weighted data curriculum; (2) it operates on encoder-based MAD-X modules for classification tasks, whereas TWMP targets decoder LLM instruction tuning; (3) TIPA has not been applied to instruction generation or to languages not already represented by a dedicated adapter. Second, 'Linguistically-Informed Multilingual Instruction Tuning' (arXiv:2410.07809) uses 289-dimensional legacy URIEL TYPO vectors with k-means clustering to select 14 discrete representative languages from a 52-language pool (one per cluster) for LoRA fine-tuning on Bactrian-X, showing that typologically diverse selection beats random selection. TWMP differs substantially: rather than discrete cluster-representative selection, TWMP applies continuous inverse-distance sampling weights over the full Aya collection using compact URIEL+ features (300-dim, Laplacian Score selected); it adds a staged cosine-distance curriculum schedule; it integrates a multi-source DPO preference optimization objective for language fidelity; and it directly targets Kazakh, Mongolian, and Uyghur—languages for which arXiv:2410.07809's evaluation suite (XNLI, XCOPA, XStoryCloze, XWinograd, PAWS-X) provides zero coverage. The combination of continuous URIEL+ weighting, staged curriculum, precisely formulated multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering the target languages constitutes a principled and differentiated advance.",
  "approach": "We propose Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, which replaces PLUG's single-English pivot with a principled mixture over multiple source languages drawn from the Aya collection (513M instances across 114 languages).\n\nAya pivot coverage is verified before training: Turkish (high-resource, multi-million instances), Kyrgyz (~4.1M instances in the Aya collection language split), Uzbek (confirmed present as an underrepresented language with meaningful coverage), and Azerbaijani all qualify as pivot sources. A minimum threshold of 5,000 Aya instances per pivot language is enforced; languages below this threshold are excluded from the mixture. All qualifying pivot languages and their instance counts are reported in an appendix table. Kazakh, Mongolian, and Uyghur serve exclusively as evaluation targets and are never included in the pivot mixture.\n\nTypological distances are computed using URIEL+ (arXiv:2409.18472, COLING 2025; available via the urielplus Python library at github.com/LeeLanguageLab/URIELPlus) rather than the legacy lang2vec 289-dimensional binary features. URIEL+ expands coverage to 4,366 languages with approximately 800 features (607 grammar features covering syntactic and morphological dimensions, plus 193 sound features), and applies SoftImpute for missing-value imputation—critical for reducing sparsity in Kazakh, Uzbek, and Kyrgyz, where legacy URIEL features are known to be sparse. URIEL+ explicitly represents Kazakh's multi-script properties (Cyrillic, Latin, and Arabic) via script vectors. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds script vectors and Glottolog genealogies to URIEL+, covering 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for the qualifying Aya pivot languages. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), which demonstrates that a Laplacian Score 300-feature subset of URIEL+ achieves Spearman ρ=0.358 on typological alignment tasks versus ρ=0.260 for the full 800-feature set while also improving downstream cross-lingual NLP performance, we apply this feature selection before computing cosine distances. Data-sampling weights are assigned inversely proportional to these 300-feature URIEL+ cosine distances, so morphologically close pivots such as Turkish or Uzbek for Kazakh receive substantially higher weight than English.\n\nThe staged curriculum uses three phases calibrated by the empirical URIEL+ distance distribution of qualifying Aya pivot languages relative to each target language. Let D_25 and D_60 denote the 25th and 60th percentile distances from the target language to all qualifying Aya pivots (computed once, before training). Stage 1 (epochs 1–3): exclusively sources with cosine distance < D_25—for Kazakh, approximately ≤0.32, capturing Turkish, Kyrgyz, Uzbek, and Azerbaijani. Stage 2 (epochs 4–6): sources with distance < D_60 (approximately ≤0.56 for Kazakh), expanding to Russian, Arabic, and other mid-distance languages. Stage 3 (epochs 7–10): full mixture over all qualifying pivot languages with continuous inverse-distance weights. Thresholds are target-specific and computed from the actual Aya-pivot distance distribution; for Mongolian, where no Turkic pivot falls within D_25, the closest available Aya sources (Korean, Finnish, Turkish) are used across all three stages with correspondingly small weights—this distance-constrained Mongolian setting is a controlled finding of interest. Ablations compare: no curriculum (full weighted mixture from epoch 1), 2-stage (merging Stages 1–2), 3-stage (proposed), and linear interpolation between stages.\n\nThe CLO-style DPO preference optimization objective is precisely extended to the multi-source setting. For each source pivot language s_i and target language t, preference pairs are defined as: chosen = (x_{s_i}, y^w_t)—an instruction in source language s_i paired with a model-generated response identified as being in the target language t; rejected = (x_{s_i}, y^l_{s_i})—the same instruction paired with a model-generated response in source language s_i. This formulation promotes target-language responses to source-language instructions and differs from CLO's English-source objective in a critical respect: CLO's English-input pair (chosen=English response, rejected=target-language response) is designed to preserve English capability by penalizing cross-lingual output for English inputs. TWMP inverts this preference because the training goal is acquisition of cross-lingual target-language instruction following: for any source-language input, we want the model to respond in the target language. TWMP does not use CLO's second pair type (target-language input → prefer target-language response) because target-language training data is explicitly excluded.\n\nPreference pairs are constructed entirely without target-language labels via automatic language identification: given each source-language instruction x_{s_i}, we sample K=8 candidate responses from Qwen3.5-9B at temperature 0.7; apply fastText language identification (lid.176.bin) to each candidate; assign responses identified as the target language to the chosen pool and responses identified as the source language to the rejected pool; apply a minimum 20-token length gate to both pools to exclude degenerate or near-empty responses; pair the highest-scoring chosen (by fastText language ID confidence) with the lowest-scoring rejected per instruction. Instructions yielding no target-language candidates in K=8 samples after the length filter fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row in the DPO evaluation table compares fastText-only selection (no length gate) against length-gated selection (≥20 tokens) to quantify the quality impact of this filter; this also characterizes the frequency of degenerate responses per source-target pair. As a mandatory prerequisite check, we run a 500-instruction probe per source-target language pair on the base Qwen3.5-9B and verify that target-language responses (meeting the ≥20-token gate) appear in >5% of K=8 samples; any pivot language pair failing this check is excluded from DPO training (falling back to SFT-weighted sampling only) for that target language. This probe is reported as a characterization result: for close Turkic pivots (Turkish→Kazakh), we expect the frequency to exceed 5% given Qwen3.5-9B's broad multilingual coverage; for distant pivots (English→Mongolian), the check may filter some source languages, which is informative about which pivots can drive DPO-based cross-lingual preference learning.\n\nWe apply QLoRA fine-tuning of Qwen3.5-9B (released March 2026; 248K-token vocabulary spanning 201 languages; the Qwen3.5 small series has 0.8B/2B/4B/9B variants—no 7B exists) on this weighted multi-pivot dataset, targeting Kazakh, Mongolian, and Uyghur as primary evaluation cases. Evaluation uses three ACL 2025 benchmarks: KazMMLU for Kazakh, MiLiC-Eval for all three targets across 9 tasks, and TUMLU for Kazakh and Uyghur within a controlled within-Turkic-family comparison. PLUG and CLO serve as primary baselines. Typological weighting ablations compare: full 800-feature URIEL+ vs. Laplacian-selected 300 features vs. syntax-only (474 features) vs. morphology-only (133 features) vs. the k-means discrete selection baseline from arXiv:2410.07809. Swahili serves as a held-out agglutinative generalization target not used during hyperparameter design. Note: TyDi QA covers Arabic, Bengali, Finnish, Indonesian, Japanese, Kiswahili, Korean, Russian, Telugu, and Thai—it does not include Kazakh, Mongolian, or Uyghur and is not used here.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200h A100 (15–20 QLoRA runs × 10–13h each on Qwen3.5-9B, covering 3 primary target languages, PLUG/CLO baselines, URIEL+ sub-space ablations, curriculum schedule variants, DPO quality gate ablation row, and DPO prerequisite probe runs)",
      "gpu_utilization": "LOW (~25–35%): GPU sits idle during code writing, debugging, data pipeline work, result analysis, and paper writing; runs are launched manually and often queue overnight",
      "timeline": "4–6 months",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$300 (200h × $1.50/h on Lambda Labs A100)",
      "h100_equivalent": "~120h H100 (within ≤200 H100-hour budget constraint at typical A100/H100 performance ratio of ~0.6×)"
    },
    "human_in_loop": {
      "gpu_hours": "~310h A100 (agent explores broader hyperparameter space with human approval gates; ~55% more runs than manual)",
      "gpu_utilization": "MODERATE (~55–65%): agent queues follow-up experiments immediately after each run completes, filling GPU idle between human check-ins",
      "timeline": "6–8 weeks",
      "team": "1 researcher, ~30min/day check-in to approve experiment configs and review intermediate results",
      "claude_api_cost": "~$150–250 (~1,500–2,500 conversation turns coordinating experiment scheduling, result parsing, and ablation planning)",
      "estimated_gpu_cost": "~$465 (310h × $1.50/h)",
      "h100_equivalent": "~186h H100 (within ≤200 H100-hour budget constraint at ~0.6× A100/H100 ratio, leaving ~14h headroom)",
      "risk_note": "Choice of URIEL+ feature subspace (full 800-feature vs. Laplacian 300-feature vs. syntax-only) and the DPO prerequisite probe threshold require human judgment at key decision points; an automated agent may converge on a locally optimal weighting scheme that under-performs on the held-out Swahili generalization target"
    },
    "auto_research": {
      "gpu_hours": "~600h A100 (3–5× more experiments: grid search over distance metrics, curriculum schedule shapes, LoRA rank/alpha, 5+ target languages including Swahili and Kyrgyz for generalization, plus replication runs)",
      "gpu_utilization": "NEAR-ZERO idle—agent schedules jobs back-to-back across all target languages in parallel, launches follow-up ablations immediately on job completion, and runs nightly sweeps without human bottleneck",
      "timeline": "5–10 days with 4× concurrent A100s; ~3 weeks on a single A100",
      "team": "0 (initial setup of experiment configs, data paths, and evaluation harness only)",
      "claude_api_cost": "~$400–650 (~4,000–6,500 turns for full experiment orchestration, result parsing, ablation tree exploration, and report drafting)",
      "estimated_gpu_cost": "~$900 (600h × $1.50/h)",
      "h100_equivalent": "~360h H100 — EXCEEDS the ≤200 H100-hour hard budget constraint. Auto_research mode is documented for completeness but is NOT a viable deployment option within the stated budget. Use manual mode (~120 H100h) or human_in_loop mode (~186 H100h) to remain within budget.",
      "speed_bottleneck": "GPU count is the primary bottleneck: 4 concurrent A100s reduces wall-clock time to ~5 days; API rate limits become secondary when running >8 parallel experiment threads",
      "risk_note": "CONSTRAINT VIOLATION: 600 A100h ≈ 360 H100h, exceeding the ≤200 H100-hour hard budget. Additionally, unconstrained exploration may overfit the URIEL+ weighting function to the 3 initial target languages; Swahili as a held-out agglutinative target is required to detect this overfitting early."
    }
  },
  "target_venues": [
    "ACL 2027 (ARR submission deadline August 3, 2026) — primary target; provides adequate time for validation on additional typological clusters beyond Turkic–Mongolic, and for a paper of this scope (multi-pivot curriculum + ablations + 3 evaluation benchmarks) that cannot realistically reach conference quality in under 6 weeks",
    "EMNLP 2026 (ACL Rolling Review, rolling deadlines throughout 2026) — viable only if the team has prior QLoRA fine-tuning infrastructure already in place and can begin experiments immediately"
  ],
  "level": "solid",
  "key_references": [
    "PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning (ACL 2024) [29% improvement on Chinese/Korean/Italian/Spanish; Turkic/Mongolic gap is untested]",
    "Cross-Lingual Optimization for Language Transfer in Large Language Models (CLO; ACL 2025, arXiv:2505.14297) [DPO-style cross-lingual preference optimization using English-only source and M2M100 translation; baseline and methodological reference for TWMP's multi-source DPO extension]",
    "LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning (Ye et al., AAAI 2026, arXiv:2511.10229) [selects multilingual instruction data using language separability scores from the model's own representation space across 22 languages including low-resource targets; differentiated from TWMP's external URIEL+ typological weighting independent of training dynamics, staged curriculum, and multi-source DPO objective]",
    "Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages (Idris et al., SIGIR 2026, arXiv:2603.27651) [multi-source cross-lingual transfer as budget-constrained resource allocation for NER and sentiment analysis on Hausa, Yoruba, and Swahili across 288 experiments; no typological features or curriculum ordering—differentiated from TWMP's URIEL+-weighted staged instruction tuning]",
    "Code-Switching Curriculum Learning for Multilingual Transfer in LLMs (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) [3-stage curriculum (token-level → sentence-level → monolingual code-switching) for single language pair; primary focus Korean, with Japanese and Indonesian—differentiated from TWMP's multi-pivot typological curriculum without code-switching targeting a family of related agglutinative languages]",
    "Revisiting Multilingual Data Mixtures in Language Model Pretraining (Foroutan et al., arXiv:2510.25947, ICLR-submitted 2025) [multilingual data reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); differentiated from TWMP's instruction-tuning-scale LoRA curriculum where data volume, optimization dynamics, and gradient signal are qualitatively different]",
    "Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh (Laiyk et al., ACL 2025 Long, arXiv:2502.13647) [10,600 GPT-4o-assisted Kazakh instruction examples fine-tuning Qwen/Falcon/Gemma; requires target-language labels and is Kazakh-specific—differentiated from TWMP's label-free multi-target approach covering Mongolian and Uyghur equally]",
    "Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+ (Shipton et al., LREC 2026, arXiv:2510.27183) [extends URIEL+ with script vectors and Glottolog genealogies for 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages]",
    "Llama-3.1-Sherkala-8B-Chat (arXiv:2503.01493) [trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish; demonstrates Turkish as auxiliary language improves Kazakh performance via full fine-tuning; differentiated from TWMP's generalizable LoRA recipe parameterized by continuous URIEL+ distances]",
    "Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) [implicit reward transfer from English-aligned DPO model to annotate cross-lingual preference pairs; 12.72% Win Rate improvement on X-AlpacaEval; English-only source with no typological weighting—differentiated from TWMP's multi-pivot source selection and low-resource agglutinative targets]",
    "URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base (arXiv:2409.18472, COLING 2025) [~800-feature typological database covering 4,366 languages with SoftImpute for low-resource Turkic languages; replaces legacy lang2vec 289-dim URIEL in TWMP; official repository: github.com/LeeLanguageLab/URIELPlus]",
    "Less is More: The Effectiveness of Compact Typological Language Representations (arXiv:2509.20129, EMNLP 2025) [Laplacian Score 300-feature URIEL+ subset (ρ=0.358) outperforms full 800-feature URIEL+ (ρ=0.260) for typological alignment and downstream cross-lingual NLP; justifies TWMP's feature selection step]",
    "Optimizing Language Models for Crosslingual Knowledge Consistency (arXiv:2603.04678; Tianyu Liu et al., March 2026) [concurrent DPO-inspired work targeting factual consistency across 26 languages and 9 LLMs—orthogonal to TWMP's language-fidelity DPO objective; differentiated in related work]",
    "TIPA: Typologically Informed Parameter Aggregation (arXiv:2601.16629, EACL 2026 Findings) [training-free encoder adapter aggregation across 230+ languages—differentiated from TWMP's training-time decoder curriculum]",
    "Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) [discrete k-means language selection using legacy 289-dim URIEL TYPO features on BLOOM/mGPT/mT5—differentiated from TWMP's continuous URIEL+ weighting, staged curriculum, multi-source DPO, and Turkic/Mongolic targets]",
    "KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan (ACL 2025, arXiv:2502.12829) [primary Kazakh evaluation benchmark, 23K questions, peer-reviewed]",
    "MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages (ACL 2025 Findings, arXiv:2503.01150) [primary evaluation for Uyghur, Kazakh, Mongolian across 9 tasks]",
    "TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages (ACL 2025, arXiv:2502.11020) [38K questions for Kazakh, Uyghur, and other Turkic languages; within-family controlled comparison]",
    "Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages (arXiv:2502.10852) [encoder-based cross-lingual transfer for Tibetan/Uyghur/Kazakh/Mongolian; motivation for decoder LLM gap]",
    "Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese (arXiv:2510.00810, 2025)",
    "Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology (arXiv:2505.13908, 2025)",
    "Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) [workshop paper, not main conference]",
    "Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models (arXiv:2603.21036, 2026) [supplementary qualitative observation; single-author preprint with 50 hand-crafted questions—not primary motivation anchor]"
  ],
  "description": "This paper introduces Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, a method for adapting decoder LLMs to low-resource languages that are typologically distant from English. Rather than using a single English pivot as in PLUG, we compute typological distances using URIEL+ (arXiv:2409.18472, COLING 2025; urielplus Python library at github.com/LeeLanguageLab/URIELPlus), which covers ~800 features across 4,366 languages with SoftImpute imputation—critical for low-resource Turkic languages where legacy lang2vec 289-dim URIEL is known to be sparse. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds Glottolog genealogies covering 26,449 languages; TWMP uses the COLING 2025 base version, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), we apply Laplacian Score feature selection to reduce URIEL+ to 300 compact features (Spearman ρ=0.358 vs. ρ=0.260 for the full 800-feature set) before computing cosine distances and assigning inverse-distance sampling weights over the Aya collection. Aya pivot coverage is verified: Turkish (multi-million instances), Kyrgyz (~4.1M instances), and Uzbek all clear a 5,000-instance minimum threshold; Kazakh, Mongolian, and Uyghur are evaluation-only targets excluded from the pivot pool. LangGPS (Ye et al., AAAI 2026, arXiv:2511.10229) selects multilingual instruction data by language separability from the model's own representation space across 22 languages; TWMP instead uses external URIEL+ features independent of training dynamics, with a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer (Idris et al., SIGIR 2026, arXiv:2603.27651) frames multi-source transfer as budget-constrained allocation for NER/sentiment tasks without typological features or curriculum ordering—TWMP's principled weighting and staged scheduling address instruction tuning specifically. A staged 3-phase curriculum progressively introduces more distant pivots using percentile thresholds computed from the empirical URIEL+ distance distribution of qualifying Aya pivots per target: Stage 1 (epochs 1–3) uses sources within the 25th percentile distance threshold (~≤0.32 for Kazakh, capturing Turkish/Kyrgyz/Uzbek/Azerbaijani); Stage 2 (epochs 4–6) expands to the 60th percentile (~≤0.56); Stage 3 (epochs 7–10) uses the full weighted mixture. Code-Switching Curriculum Learning (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) proposes a 3-stage code-switching curriculum for a single language pair; TWMP's curriculum spans a typologically ordered pool of pivot languages without code-switching. The DPO preference optimization objective is precisely formulated for the multi-source case: for source pivot s_i and target t, chosen = (instruction in s_i, model-generated response in t); rejected = (instruction in s_i, model-generated response in s_i). This inverts CLO's English-input pair direction—CLO prefers English responses to English inputs (preserving English capability), while TWMP prefers target-language responses to any source-language input (promoting cross-lingual instruction following). Pairs are auto-constructed by sampling K=8 responses per instruction from Qwen3.5-9B, applying fastText language identification, and applying a minimum 20-token length gate to both chosen and rejected pools to exclude degenerate responses; no target-language training labels are required. Instructions yielding no target-language candidates post-gate fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row compares fastText-only selection against length-gated selection to quantify the quality impact of this filter. A mandatory 500-instruction prerequisite probe verifies >5% target-language response frequency (post-length-gate) per source-target pair; pairs failing this check fall back to SFT-only. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish and demonstrates the value of Turkish as an auxiliary language for Kazakh via full fine-tuning, motivating TWMP's Turkic pivot inclusion; TWMP generalizes this insight into a principled LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target. Laiyk et al. (ACL 2025 Long, arXiv:2502.13647) fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP requires no target-language labels and applies equally to Mongolian and Uyghur where no comparable dataset exists. Revisiting Multilingual Data Mixtures (Foroutan et al., arXiv:2510.25947) studies reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); TWMP targets instruction-tuning scale where data volume, optimization dynamics, and gradient signal are qualitatively different. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) uses implicit reward transfer from English-aligned models to annotate cross-lingual DPO pairs (12.72% Win Rate on X-AlpacaEval); TWMP extends this direction to multi-pivot source selection weighted by typological distance targeting low-resource agglutinative languages absent from that work. Concurrent work 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678, March 2026) uses DPO for factual consistency across 26 languages—orthogonal in objective (knowledge coherence vs. language fidelity) and not addressing low-resource instruction tuning. Two directly adjacent works are carefully differentiated: TIPA (EACL 2026) aggregates MAD-X encoder adapters at inference time without training; arXiv:2410.07809 uses k-means on legacy 289-dim URIEL for discrete language selection on BLOOM/mGPT with zero Kazakh/Mongolian/Uyghur coverage. We fine-tune Qwen3.5-9B with QLoRA (released March 2026; 248K-token vocabulary, 201 languages; 0.8B/2B/4B/9B series—no 7B variant), targeting Kazakh, Mongolian, and Uyghur, evaluated on KazMMLU, MiLiC-Eval, and TUMLU (all ACL 2025). Ablations cover full URIEL+ vs. Laplacian-300 vs. syntax-only vs. morphology-only vs. k-means discrete baseline; curriculum variants; DPO quality gate (fastText-only vs. length-gated); DPO vs. SFT-only. Swahili is the held-out agglutinative generalization target. Manual mode (200 A100h ≈ 120 H100h) and human-in-loop mode (310 A100h ≈ 186 H100h) stay within the ≤200 H100-hour budget; auto_research mode (600 A100h ≈ 360 H100h) exceeds the constraint and is not viable within budget. ACL 2027 (ARR August 3, 2026) is the primary target venue.",
  "project_name": "typological_multi_pivot",
  "source": "web_research"
}
```

---

**Summary of all 7 changes made:**

| # | Item | Location | Action |
|---|------|----------|--------|
| 1 | Foroutan et al. (arXiv:2510.25947) | `landscape` (after CLO/LangGPS block) | Added one sentence contrasting pretraining-scale reweighting vs. TWMP's instruction-tuning scale |
| 2 | LangGPS (arXiv:2511.10229, AAAI 2026) | `landscape` (directly after CLO, as highest priority) | Added one paragraph: model-internal separability vs. TWMP's external URIEL+ features; no staged curriculum or multi-source DPO |
| 3 | Code-Switching Curriculum (arXiv:2411.02460, ACL 2025 Findings) | `landscape` (after LangGPS/Budget-Xfer) | Added one sentence: single-pair 3-stage code-switching vs. TWMP's multi-pivot typological pool |
| 4 | Laiyk et al. (arXiv:2502.13647, ACL 2025 Long) | `landscape` (after Sherkala-Chat) | Added one sentence: GPT-4o-assisted Kazakh labels required; TWMP is label-free and covers Mongolian/Uyghur |
| 5 | URIEL+ expansion (arXiv:2510.27183, LREC 2026) | `approach` paragraph 3 (after script vectors sentence) | Added one sentence: 26,449-language extension noted; TWMP uses COLING 2025 base which suffices |
| 6 | Budget-Xfer (arXiv:2603.27651, SIGIR 2026) | `landscape` (after LangGPS) | Added one sentence: budget-constrained NER/sentiment allocation vs. TWMP's typological-weighted instruction tuning |
| 7 | Per-instruction fallback | `approach` paragraph 6 | Changed "are discarded" → "fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe" |

All 7 items are reflected in both `landscape`/`approach` and propagated into `description` and `key_references`. No methodological changes; `change_type: "minor"`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67670851-273d-4c78-9ef0-a2643d99e3dd",
  "isSidechain": false,
  "requestId": "req_011CatX4viMRzCfXfNrLMyWr",
  "type": "assistant",
  "uuid": "c4a7edb4-1b19-41d0-8f5f-e83a3250b9c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TH5rUo5mzuPTBXcc3jxWPN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2847,
      "cache_read_input_tokens": 29360,
      "output_tokens": 29240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2847,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 29240,
          "cache_read_input_tokens": 29360,
          "cache_creation_input_tokens": 2847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2847
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruc…",
  "leafUuid": "c4a7edb4-1b19-41d0-8f5f-e83a3250b9c4",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise TWMP core problem and landscape for Round 7",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruc…",
  "leafUuid": "c4a7edb4-1b19-41d0-8f5f-e83a3250b9c4",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise TWMP core problem and landscape for Round 7",
  "sessionId": "967cf362-df51-4fa3-8b99-78ae3dd47db6"
}
```

---
