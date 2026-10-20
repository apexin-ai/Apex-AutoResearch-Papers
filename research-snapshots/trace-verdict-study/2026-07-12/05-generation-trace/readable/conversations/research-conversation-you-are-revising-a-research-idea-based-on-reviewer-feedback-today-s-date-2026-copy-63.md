# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/6d7de733-2eec-460b-a21c-5e6b1efdf935.jsonl`
- **Structured JSON:** [`21acef91a899d996788e.json`](../../sessions/21/21acef91a899d996788e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T08:25:00.863Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T08:25:00.863Z",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning\",\n  \"core_problem\": \"Cross-lingual instruction tuning for low-resource languages defaults to English as the sole pivot, creating systematic gaps for languages that are typologically distant from English—particularly those with agglutinative morphology, non-Latin scripts, or SOV word order. Three peer-reviewed ACL 2025 benchmarks—KazMMLU (Kazakh), MiLiC-Eval (Tibetan, Uyghur, Kazakh, Mongolian), and TUMLU (Turkic languages including Kazakh and Uyghur)—confirm that even frontier multilingual LLMs (GPT-4, Llama-3.1, Qwen-2.5) achieve near-random performance on Mongolian comprehension tasks and substantially below-par accuracy on Kazakh and Uyghur relative to typologically proximate high-resource languages. No existing instruction tuning method uses typological distance to continuously weight data-source selection across a multi-pivot mixture for these under-represented language families.\",\n  \"opportunity\": \"Three complementary ACL 2025 benchmarks provide peer-reviewed grounding for the performance gap. KazMMLU (arXiv:2502.12829; ACL 2025 long paper) comprises 23K questions total (approximately 11K in Kazakh, 12K in Russian) spanning STEM, humanities, and social sciences sourced from authentic Kazakhstani educational materials; for TWMP's Kazakh instruction evaluation, only the Kazakh-language subset (~11K questions) is relevant; evaluation of Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 shows 'substantial room for improvement' for all models on Kazakh, despite the language having 20 million speakers. MiLiC-Eval (arXiv:2503.01150; ACL 2025 Findings) covers Tibetan, Uyghur, Kazakh, and Mongolian across 9 tasks with 24K instances; GPT-4o-mini achieves only slightly above random on Mongolian tasks, and models exhibit only 'preliminary understanding' of Tibetan and Kazakh. TUMLU (arXiv:2502.11020; ACL 2025 long paper) provides 38K native questions spanning 11 academic subjects across Turkic languages including Kazakh and Uyghur, enabling controlled within-family comparisons that isolate the effect of lower training corpus size. The XLM-SWCM paper (arXiv:2502.10852) additionally shows that encoder-based shared-weight cross-lingual pretraining partially bridges these gaps—Kazakh ROUGE-L summarization score of 5.6 is notably the lowest among the four minority languages studied—but this approach does not scale to instruction-following for decoder LLMs. CLO (arXiv:2505.14297; ACL 2025) shows that DPO-style cross-lingual preference optimization with only 3,200 samples outperforms standard SFT with 6,400 samples, establishing strong data efficiency for cross-lingual transfer. 'Do Chinese Models Speak Chinese Languages?' (arXiv:2504.00289, April 2026) evaluates 10 LLMs across 21 language variants and finds that Llama3-Instruct is the only model showing distinctive Uyghur capability while most models reach only ~75% Mongolian identification accuracy; Chinese LLMs do not outperform Western counterparts on minority languages including Uyghur and Mongolian, confirming that the performance gap TWMP targets persists even in the most recent model generation. These findings together create a clear opening: by weighting instruction data from multiple source languages inversely by URIEL+ typological distance and introducing a staged curriculum, we can build a principled multi-pivot training regime that directly addresses the English-pivot bottleneck for agglutinative low-resource targets.\",\n  \"landscape\": \"PLUG (ACL 2024) established that English-pivot cross-lingual instruction generation improves multilingual instruction following—but its reported 29% improvement was measured on Chinese, Korean, Italian, and Spanish. Whether the English-pivot advantage holds for typologically distant agglutinative languages with non-Latin scripts (Kazakh, Mongolian, Uyghur) is an assumption that TWMP directly tests rather than takes for granted. CLO (arXiv:2505.14297; ACL 2025) improves data efficiency via DPO-style cross-lingual preference optimization using 6,400 OpenAssistant samples machine-translated by M2M100; it fixes English as the sole source language without varying source selection by typological distance. PROM [NAACL 2025, aclanthology.org/2025.naacl-short.19/] (Pivoted and Regulated Optimization for Multilingual Instruction Learning) treats English as an internal pivot and disentangles English vs. target-language training objectives via separate regularized losses to reduce negative interference; like PLUG and CLO, PROM presupposes a single English pivot without addressing typological distance, multi-pivot source selection, or agglutinative low-resource targets such as Kazakh, Mongolian, and Uyghur. LangGPS [Ye et al., AAAI 2026, arXiv:2511.10229] selects multilingual instruction data based on language separability scores derived from the model's own representation space, demonstrating improvements across 22 languages including low-resource targets. Unlike LangGPS, TWMP uses external typological features from URIEL+ to derive a pivot ordering independent of training dynamics, and integrates a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer [arXiv:2603.27651, 2026; submitted to SIGIR 2026 Short Paper track] formulates multi-source cross-lingual transfer as a budget-constrained allocation problem for NER/sentiment tasks; TWMP's typological-distance weighting and staged curriculum provide a principled ordering mechanism for instruction tuning that Budget-Xfer does not address. Code-Switching Curriculum Learning [Yoo et al., ACL 2025 Findings, arXiv:2411.02460] proposes a 3-stage curriculum (token-level → sentence-level → monolingual code-switching) for a single language pair; TWMP's curriculum operates over a pool of typologically ordered pivot languages without code-switching and targets a set of related agglutinative languages rather than a single target. Revisiting Multilingual Data Mixtures [Foroutan et al., 2025, arXiv:2510.25947] studies reweighting across 25–400 languages at pretraining scale (1.1B–3B parameters); TWMP operates at instruction-tuning scale—10 epochs, LoRA, narrow near-family pivot pool—where the data volume, optimization dynamics, and gradient signal are qualitatively different from the pretraining regime. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh, English, Russian, and Turkish, and demonstrates that Turkish as an auxiliary language improves Kazakh performance—directly motivating TWMP's inclusion of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc four-language selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language, with principled pivot selection replacing language-specific engineering. Laiyk et al. [ACL 2025 Long, arXiv:2502.13647] fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP does not require any target-language instruction labels and applies equally to Mongolian and Uyghur, where no comparable GPT-4-assisted dataset currently exists. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving a 12.72% average Win Rate improvement on X-AlpacaEval; it uses English as the sole source and implicit reward annotation without typological weighting—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from that work. 'Family Matters' (arXiv:2510.00810) applies language transfer and LoRA merging from typologically related Nordic languages to Faroese—demonstrating that typological proximity helps—but as a single-language case study with no generalizable training recipe. 'Cross-Linguistic Transfer in Multilingual NLP' (arXiv:2505.13908) analyzes language family and morphology effects empirically without proposing a training method. Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) decouples task and language LoRA adapters but does not use typological features to parameterize or weight the language adapter. 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678; Tianyu Liu et al., March 2026) introduces a DPO-inspired method—concurrent with TWMP—that enforces factual consistency of model responses across 26 languages and 9 LLMs; its preference pairs encode semantic equivalence of knowledge across languages (chosen = factually consistent cross-lingual response, rejected = factually inconsistent response). This objective is orthogonal to TWMP's: DCO addresses what the model says across languages (knowledge coherence), while TWMP addresses which language it responds in when given instructions in any of multiple pivot languages (instruction-language fidelity). DCO does not address low-resource instruction tuning, multi-pivot source selection, or typological-distance weighting. A concurrent theoretical framework 'Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family' (arXiv:2604.06202, April 2026) proposes the Turkic Transfer Coefficient (TTC), a composite typological similarity metric combining morphological, lexical, syntactic, and script compatibility for Turkic languages. Unlike TWMP, arXiv:2604.06202 is a theoretical analysis without training method, instruction tuning experiments, or evaluation on KazMMLU, MiLiC-Eval, or TUMLU; it corroborates the motivation for Turkic-pivot weighting but does not instantiate it empirically. Two works require careful differentiation from TWMP. First, TIPA (arXiv:2601.16629; EACL 2026 Findings) constructs proxy language adapters by aggregating existing MAD-X adapters weighted by typological similarity across 230+ languages—entirely without training. TIPA is orthogonal to TWMP in three key ways: (1) it is training-free inference-time adapter aggregation, whereas TWMP learns from a typologically-weighted data curriculum; (2) it operates on encoder-based MAD-X modules for classification tasks, whereas TWMP targets decoder LLM instruction tuning; (3) TIPA has not been applied to instruction generation or to languages not already represented by a dedicated adapter. Second, 'Linguistically-Informed Multilingual Instruction Tuning' (arXiv:2410.07809) uses 289-dimensional legacy URIEL TYPO vectors with k-means clustering to select 14 discrete representative languages from a 52-language pool (one per cluster) for LoRA fine-tuning on Bactrian-X, showing that typologically diverse selection beats random selection. TWMP differs substantially: rather than discrete cluster-representative selection, TWMP applies continuous inverse-distance sampling weights over the full Aya collection using compact URIEL+ features (300-dim, Laplacian Score selected); it adds a staged cosine-distance curriculum schedule; it integrates a multi-source DPO preference optimization objective for language fidelity; and it directly targets Kazakh, Mongolian, and Uyghur—languages for which arXiv:2410.07809's evaluation suite (XNLI, XCOPA, XStoryCloze, XWinograd, PAWS-X) provides zero coverage. The combination of continuous URIEL+ weighting, staged curriculum, precisely formulated multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering the target languages constitutes a principled and differentiated advance.\",\n  \"approach\": \"We propose Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, which replaces PLUG's single-English pivot with a principled mixture over multiple source languages drawn from the Aya collection (513M instances across 114 languages).\\n\\nAya pivot coverage is verified before training: Turkish (high-resource, multi-million instances), Kyrgyz (~4.1M instances in the Aya collection language split), Uzbek (confirmed present as an underrepresented language with meaningful coverage), and Azerbaijani all qualify as pivot sources. A minimum threshold of 5,000 Aya instances per pivot language is enforced; languages below this threshold are excluded from the mixture. All qualifying pivot languages and their instance counts are reported in an appendix table. Kazakh, Mongolian, and Uyghur serve exclusively as evaluation targets and are never included in the pivot mixture.\\n\\nTypological distances are computed using URIEL+ (arXiv:2409.18472, COLING 2025; available via the urielplus Python library at github.com/LeeLanguageLab/URIELPlus) rather than the legacy lang2vec 289-dimensional binary features. URIEL+ expands coverage to 4,366 languages with approximately 800 features (607 grammar features covering syntactic and morphological dimensions, plus 193 sound features), and applies SoftImpute for missing-value imputation—critical for reducing sparsity in Kazakh, Uzbek, and Kyrgyz, where legacy URIEL features are known to be sparse. URIEL+ explicitly represents Kazakh's multi-script properties (Cyrillic, Latin, and Arabic) via script vectors. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds script vectors and Glottolog genealogies to URIEL+, covering 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for the qualifying Aya pivot languages. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), which demonstrates that a Laplacian Score 300-feature subset of URIEL+ achieves Spearman ρ=0.358 (p=0.061; measured against linguistic similarity distance alignment metric G_d, Table 1) versus ρ=0.260 for the full 800-feature set, and additionally yields +7.8% improvement on LangRank downstream cross-lingual NLP tasks, we apply this feature selection before computing cosine distances. The downstream task gains (+7.8% LangRank) provide the primary empirical justification for the feature selection step; the typological alignment improvement (p=0.061) is directionally consistent but borderline significant and should not be cited as standalone evidence. Data-sampling weights are assigned inversely proportional to these 300-feature URIEL+ cosine distances, so morphologically close pivots such as Turkish or Uzbek for Kazakh receive substantially higher weight than English.\\n\\nThe staged curriculum uses three phases calibrated by the empirical URIEL+ distance distribution of qualifying Aya pivot languages relative to each target language. Let D_25 and D_60 denote the 25th and 60th percentile distances from the target language to all qualifying Aya pivots (computed once, before training). Stage 1 (epochs 1–3): exclusively sources with cosine distance < D_25—for Kazakh, approximately ≤0.32, capturing Turkish, Kyrgyz, Uzbek, and Azerbaijani. Stage 2 (epochs 4–6): sources with distance < D_60 (approximately ≤0.56 for Kazakh), expanding to Russian, Arabic, and other mid-distance languages. Stage 3 (epochs 7–10): full mixture over all qualifying pivot languages with continuous inverse-distance weights. Thresholds are target-specific and computed from the actual Aya-pivot distance distribution; for Mongolian, where no Turkic pivot falls within D_25, the closest available Aya sources (Korean, Finnish, Turkish) are used across all three stages with correspondingly small weights—this distance-constrained Mongolian setting is a controlled finding of interest. Ablations compare: no curriculum (full weighted mixture from epoch 1), 2-stage (merging Stages 1–2), 3-stage (proposed), and linear interpolation between stages.\\n\\nThe CLO-style DPO preference optimization objective is precisely extended to the multi-source setting. For each source pivot language s_i and target language t, preference pairs are defined as: chosen = (x_{s_i}, y^w_t)—an instruction in source language s_i paired with a model-generated response identified as being in the target language t; rejected = (x_{s_i}, y^l_{s_i})—the same instruction paired with a model-generated response in source language s_i. This formulation promotes target-language responses to source-language instructions and differs from CLO's English-source objective in a critical respect: CLO's English-input pair (chosen=English response, rejected=target-language response) is designed to preserve English capability by penalizing cross-lingual output for English inputs. TWMP inverts this preference because the training goal is acquisition of cross-lingual target-language instruction following: for any source-language input, we want the model to respond in the target language. TWMP does not use CLO's second pair type (target-language input → prefer target-language response) because target-language training data is explicitly excluded.\\n\\nPreference pairs are constructed entirely without target-language labels via automatic language identification: given each source-language instruction x_{s_i}, we sample K=8 candidate responses from Qwen3.5-9B at temperature 0.7; apply fastText language identification (lid.176.bin) to each candidate; assign responses identified as the target language to the chosen pool and responses identified as the source language to the rejected pool; apply a minimum 20-token length gate to both pools to exclude degenerate or near-empty responses; pair the highest-scoring chosen (by fastText language ID confidence) with the lowest-scoring rejected per instruction. Instructions yielding no target-language candidates in K=8 samples after the length filter fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row in the DPO evaluation table compares fastText-only selection (no length gate) against length-gated selection (≥20 tokens) to quantify the quality impact of this filter; this also characterizes the frequency of degenerate responses per source-target pair. As a mandatory prerequisite check, we run a 500-instruction probe per source-target language pair on the base Qwen3.5-9B and verify that target-language responses (meeting the ≥20-token gate) appear in >5% of K=8 samples; any pivot language pair failing this check is excluded from DPO training (falling back to SFT-weighted sampling only) for that target language. This probe is reported as a characterization result: for close Turkic pivots (Turkish→Kazakh), we expect the frequency to exceed 5% given Qwen3.5-9B's broad multilingual coverage; for distant pivots (English→Mongolian), the check may filter some source languages, which is informative about which pivots can drive DPO-based cross-lingual preference learning.\\n\\nWe apply QLoRA fine-tuning of Qwen3.5-9B (released March 2026; 248K-token vocabulary spanning 201 languages; the Qwen3.5 small series has 0.8B/2B/4B/9B variants—no 7B exists) on this weighted multi-pivot dataset, targeting Kazakh, Mongolian, and Uyghur as primary evaluation cases. Evaluation uses three ACL 2025 benchmarks: KazMMLU for Kazakh (Kazakh-language subset, ~11K questions), MiLiC-Eval for all three targets across 9 tasks, and TUMLU for Kazakh and Uyghur within a controlled within-Turkic-family comparison. PLUG, PROM [NAACL 2025], and CLO serve as primary English-pivot baselines. Typological weighting ablations compare: full 800-feature URIEL+ vs. Laplacian-selected 300 features vs. syntax-only (474 features) vs. morphology-only (133 features) vs. the k-means discrete selection baseline from arXiv:2410.07809. Swahili serves as a held-out agglutinative generalization target not used during hyperparameter design. Note: TyDi QA covers Arabic, Bengali, Finnish, Indonesian, Japanese, Kiswahili, Korean, Russian, Telugu, and Thai—it does not include Kazakh, Mongolian, or Uyghur and is not used here.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~200h A100 (15–20 QLoRA runs × 10–13h each on Qwen3.5-9B, covering 3 primary target languages, PLUG/CLO/PROM baselines, URIEL+ sub-space ablations, curriculum schedule variants, DPO quality gate ablation row, and DPO prerequisite probe runs)\",\n      \"gpu_utilization\": \"LOW (~25–35%): GPU sits idle during code writing, debugging, data pipeline work, result analysis, and paper writing; runs are launched manually and often queue overnight\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$300 (200h × $1.50/h on Lambda Labs A100)\",\n      \"h100_equivalent\": \"~120h H100 (within ≤200 H100-hour budget constraint at typical A100/H100 performance ratio of ~0.6×)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~310h A100 (agent explores broader hyperparameter space with human approval gates; ~55% more runs than manual)\",\n      \"gpu_utilization\": \"MODERATE (~55–65%): agent queues follow-up experiments immediately after each run completes, filling GPU idle between human check-ins\",\n      \"timeline\": \"6–8 weeks\",\n      \"team\": \"1 researcher, ~30min/day check-in to approve experiment configs and review intermediate results\",\n      \"claude_api_cost\": \"~$150–250 (~1,500–2,500 conversation turns coordinating experiment scheduling, result parsing, and ablation planning)\",\n      \"estimated_gpu_cost\": \"~$465 (310h × $1.50/h)\",\n      \"h100_equivalent\": \"~186h H100 (within ≤200 H100-hour budget constraint at ~0.6× A100/H100 ratio, leaving ~14h headroom)\",\n      \"risk_note\": \"Choice of URIEL+ feature subspace (full 800-feature vs. Laplacian 300-feature vs. syntax-only) and the DPO prerequisite probe threshold require human judgment at key decision points; an automated agent may converge on a locally optimal weighting scheme that under-performs on the held-out Swahili generalization target\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~600h A100 (3–5× more experiments: grid search over distance metrics, curriculum schedule shapes, LoRA rank/alpha, 5+ target languages including Swahili and Kyrgyz for generalization, plus replication runs)\",\n      \"gpu_utilization\": \"NEAR-ZERO idle—agent schedules jobs back-to-back across all target languages in parallel, launches follow-up ablations immediately on job completion, and runs nightly sweeps without human bottleneck\",\n      \"timeline\": \"5–10 days with 4× concurrent A100s; ~3 weeks on a single A100\",\n      \"team\": \"0 (initial setup of experiment configs, data paths, and evaluation harness only)\",\n      \"claude_api_cost\": \"~$400–650 (~4,000–6,500 turns for full experiment orchestration, result parsing, ablation tree exploration, and report drafting)\",\n      \"estimated_gpu_cost\": \"~$900 (600h × $1.50/h)\",\n      \"h100_equivalent\": \"~360h H100 — EXCEEDS the ≤200 H100-hour hard budget constraint. Auto_research mode is documented for completeness but is NOT a viable deployment option within the stated budget. Use manual mode (~120 H100h) or human_in_loop mode (~186 H100h) to remain within budget.\",\n      \"speed_bottleneck\": \"GPU count is the primary bottleneck: 4 concurrent A100s reduces wall-clock time to ~5 days; API rate limits become secondary when running >8 parallel experiment threads\",\n      \"risk_note\": \"CONSTRAINT VIOLATION: 600 A100h ≈ 360 H100h, exceeding the ≤200 H100-hour hard budget. Additionally, unconstrained exploration may overfit the URIEL+ weighting function to the 3 initial target languages; Swahili as a held-out agglutinative target is required to detect this overfitting early.\"\n    }\n  },\n  \"target_venues\": [\n    \"ACL 2027 (ARR submission deadline August 3, 2026) — primary target; provides adequate time for validation on additional typological clusters beyond Turkic–Mongolic, and for a paper of this scope (multi-pivot curriculum + ablations + 3 evaluation benchmarks) that cannot realistically reach conference quality in under 6 weeks\",\n    \"EMNLP 2026 (ACL Rolling Review, rolling deadlines throughout 2026) — viable only if the team has prior QLoRA fine-tuning infrastructure already in place and can begin experiments immediately\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning (ACL 2024) [29% improvement on Chinese/Korean/Italian/Spanish; Turkic/Mongolic gap is untested]\",\n    \"Cross-Lingual Optimization for Language Transfer in Large Language Models (CLO; ACL 2025, arXiv:2505.14297) [DPO-style cross-lingual preference optimization using English-only source and M2M100 translation; baseline and methodological reference for TWMP's multi-source DPO extension]\",\n    \"PROM: Pivoted and Regulated Optimization for Multilingual Instruction Learning (NAACL 2025, aclanthology.org/2025.naacl-short.19/) [treats English as an internal pivot and disentangles English vs. target-language training objectives via regulated losses to reduce negative interference; like PLUG and CLO, fixes English as the sole pivot without addressing typological distance, multi-pivot sequencing, or agglutinative low-resource targets—cited as an English-pivot baseline alongside PLUG and CLO]\",\n    \"LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning (Ye et al., AAAI 2026, arXiv:2511.10229) [selects multilingual instruction data using language separability scores from the model's own representation space across 22 languages including low-resource targets; differentiated from TWMP's external URIEL+ typological weighting independent of training dynamics, staged curriculum, and multi-source DPO objective]\",\n    \"Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages (Idris et al., arXiv:2603.27651, 2026; submitted to SIGIR 2026 Short Paper track) [multi-source cross-lingual transfer as budget-constrained resource allocation for NER and sentiment analysis on Hausa, Yoruba, and Swahili across 288 experiments; no typological features or curriculum ordering—differentiated from TWMP's URIEL+-weighted staged instruction tuning; note: preprint only, acceptance not yet confirmed]\",\n    \"Code-Switching Curriculum Learning for Multilingual Transfer in LLMs (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) [3-stage curriculum (token-level → sentence-level → monolingual code-switching) for single language pair; primary focus Korean, with Japanese and Indonesian—differentiated from TWMP's multi-pivot typological curriculum without code-switching targeting a family of related agglutinative languages]\",\n    \"Revisiting Multilingual Data Mixtures in Language Model Pretraining (Foroutan et al., arXiv:2510.25947, ICLR-submitted 2025) [multilingual data reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); differentiated from TWMP's instruction-tuning-scale LoRA curriculum where data volume, optimization dynamics, and gradient signal are qualitatively different]\",\n    \"Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh (Laiyk et al., ACL 2025 Long, arXiv:2502.13647) [10,600 GPT-4o-assisted Kazakh instruction examples fine-tuning Qwen/Falcon/Gemma; requires target-language labels and is Kazakh-specific—differentiated from TWMP's label-free multi-target approach covering Mongolian and Uyghur equally]\",\n    \"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+ (Shipton et al., LREC 2026, arXiv:2510.27183) [extends URIEL+ with script vectors and Glottolog genealogies for 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages]\",\n    \"Llama-3.1-Sherkala-8B-Chat (arXiv:2503.01493) [trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish; demonstrates Turkish as auxiliary language improves Kazakh performance via full fine-tuning; differentiated from TWMP's generalizable LoRA recipe parameterized by continuous URIEL+ distances]\",\n    \"Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) [implicit reward transfer from English-aligned DPO model to annotate cross-lingual preference pairs; 12.72% Win Rate improvement on X-AlpacaEval; English-only source with no typological weighting—differentiated from TWMP's multi-pivot source selection and low-resource agglutinative targets]\",\n    \"URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base (arXiv:2409.18472, COLING 2025) [~800-feature typological database covering 4,366 languages with SoftImpute for low-resource Turkic languages; replaces legacy lang2vec 289-dim URIEL in TWMP; official repository: github.com/LeeLanguageLab/URIELPlus]\",\n    \"Less is More: The Effectiveness of Compact Typological Language Representations (arXiv:2509.20129, EMNLP 2025) [Laplacian Score 300-feature URIEL+ subset achieves ρ=0.358 (p=0.061; measured on linguistic distance alignment against G_d metric, Table 1) vs. ρ=0.260 for full 800-feature URIEL+; downstream improvement of +7.8% on LangRank tasks; ρ values verified from paper HTML; downstream gains provide the primary justification for TWMP's feature selection step—the typological alignment improvement is directionally consistent but borderline significant]\",\n    \"Optimizing Language Models for Crosslingual Knowledge Consistency (arXiv:2603.04678; Tianyu Liu et al., March 2026) [concurrent DPO-inspired work targeting factual consistency across 26 languages and 9 LLMs—orthogonal to TWMP's language-fidelity DPO objective; differentiated in related work]\",\n    \"TIPA: Typologically Informed Parameter Aggregation (arXiv:2601.16629, EACL 2026 Findings) [training-free encoder adapter aggregation across 230+ languages—differentiated from TWMP's training-time decoder curriculum]\",\n    \"Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) [discrete k-means language selection using legacy 289-dim URIEL TYPO features on BLOOM/mGPT/mT5—differentiated from TWMP's continuous URIEL+ weighting, staged curriculum, multi-source DPO, and Turkic/Mongolic targets]\",\n    \"Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family (arXiv:2604.06202, April 2026) [theoretical framework introducing Turkic Transfer Coefficient (TTC) combining morphological, lexical, syntactic, and script compatibility; no training method or instruction tuning experiments; no evaluation on KazMMLU/MiLiC-Eval/TUMLU—corroborates motivation for Turkic-pivot weighting without instantiating it empirically]\",\n    \"KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan (ACL 2025, arXiv:2502.12829) [primary Kazakh evaluation benchmark; 23K total questions (approximately 11K in Kazakh, 12K in Russian) sourced from authentic Kazakhstani educational materials; peer-reviewed; TWMP evaluates on the Kazakh-language subset only]\",\n    \"MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages (ACL 2025 Findings, arXiv:2503.01150) [primary evaluation for Uyghur, Kazakh, Mongolian across 9 tasks]\",\n    \"TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages (ACL 2025, arXiv:2502.11020) [38K questions for Kazakh, Uyghur, and other Turkic languages; within-family controlled comparison]\",\n    \"Do Chinese Models Speak Chinese Languages? (arXiv:2504.00289, April 2026) [evaluates 10 LLMs across 21 language variants including Uyghur, Mongolian, Kazakh, and Tibetan; Llama3-Instruct is uniquely capable at Uyghur and ranks highest on Mongolian; Chinese LLMs do not outperform Western counterparts on minority languages—contemporary evidence for the performance gap TWMP addresses]\",\n    \"Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages (arXiv:2502.10852) [encoder-based cross-lingual transfer for Tibetan/Uyghur/Kazakh/Mongolian; motivation for decoder LLM gap]\",\n    \"Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese (arXiv:2510.00810, 2025)\",\n    \"Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology (arXiv:2505.13908, 2025)\",\n    \"Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) [workshop paper, not main conference]\",\n    \"Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models (arXiv:2603.21036, 2026) [supplementary qualitative observation; single-author preprint with 50 hand-crafted questions—not primary motivation anchor]\"\n  ],\n  \"description\": \"This paper introduces Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, a method for adapting decoder LLMs to low-resource languages that are typologically distant from English. Rather than using a single English pivot as in PLUG, we compute typological distances using URIEL+ (arXiv:2409.18472, COLING 2025; urielplus Python library at github.com/LeeLanguageLab/URIELPlus), which covers ~800 features across 4,366 languages with SoftImpute imputation—critical for low-resource Turkic languages where legacy lang2vec 289-dim URIEL is known to be sparse. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds Glottolog genealogies covering 26,449 languages; TWMP uses the COLING 2025 base version, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), we apply Laplacian Score feature selection to reduce URIEL+ to 300 compact features (Spearman ρ=0.358, p=0.061, measured on linguistic distance alignment with G_d metric, Table 1; +7.8% improvement on LangRank downstream tasks; vs. ρ=0.260 for the full 800-feature set; ρ values verified from paper HTML—the downstream gains are the primary justification, as the typological alignment improvement is directionally consistent but borderline significant) before computing cosine distances and assigning inverse-distance sampling weights over the Aya collection. Aya pivot coverage is verified: Turkish (multi-million instances), Kyrgyz (~4.1M instances), and Uzbek all clear a 5,000-instance minimum threshold; Kazakh, Mongolian, and Uyghur are evaluation-only targets excluded from the pivot pool. Contemporary evidence from 'Do Chinese Models Speak Chinese Languages?' (arXiv:2504.00289, April 2026), which evaluates 10 LLMs across 21 language variants, shows that Llama3-Instruct is the only evaluated model with distinctive Uyghur capability and that Chinese LLMs do not outperform Western counterparts on minority languages including Uyghur and Mongolian—confirming that no current model family addresses the performance gap TWMP targets. LangGPS (Ye et al., AAAI 2026, arXiv:2511.10229) selects multilingual instruction data by language separability from the model's own representation space across 22 languages; TWMP instead uses external URIEL+ features independent of training dynamics, with a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer (Idris et al., arXiv:2603.27651, 2026; submitted to SIGIR 2026 Short Paper track) frames multi-source transfer as budget-constrained allocation for NER/sentiment tasks without typological features or curriculum ordering—TWMP's principled weighting and staged scheduling address instruction tuning specifically. A staged 3-phase curriculum progressively introduces more distant pivots using percentile thresholds computed from the empirical URIEL+ distance distribution of qualifying Aya pivots per target: Stage 1 (epochs 1–3) uses sources within the 25th percentile distance threshold (~≤0.32 for Kazakh, capturing Turkish/Kyrgyz/Uzbek/Azerbaijani); Stage 2 (epochs 4–6) expands to the 60th percentile (~≤0.56); Stage 3 (epochs 7–10) uses the full weighted mixture. Code-Switching Curriculum Learning (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) proposes a 3-stage code-switching curriculum for a single language pair; TWMP's curriculum spans a typologically ordered pool of pivot languages without code-switching. The DPO preference optimization objective is precisely formulated for the multi-source case: for source pivot s_i and target t, chosen = (instruction in s_i, model-generated response in t); rejected = (instruction in s_i, model-generated response in s_i). This inverts CLO's English-input pair direction—CLO prefers English responses to English inputs (preserving English capability), while TWMP prefers target-language responses to any source-language input (promoting cross-lingual instruction following). PROM [NAACL 2025] similarly treats English as an internal pivot and disentangles English and target-language training objectives via regulated losses; like PLUG and CLO, PROM fixes a single English pivot without addressing typological distance or multi-pivot sequencing for agglutinative targets—all three serve as English-pivot baselines in TWMP's evaluation. Pairs are auto-constructed by sampling K=8 responses per instruction from Qwen3.5-9B, applying fastText language identification, and applying a minimum 20-token length gate to both chosen and rejected pools to exclude degenerate responses; no target-language training labels are required. Instructions yielding no target-language candidates post-gate fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row compares fastText-only selection against length-gated selection to quantify the quality impact of this filter. A mandatory 500-instruction prerequisite probe verifies >5% target-language response frequency (post-length-gate) per source-target pair; pairs failing this check fall back to SFT-only. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish and demonstrates the value of Turkish as an auxiliary language for Kazakh via full fine-tuning, motivating TWMP's Turkic pivot inclusion; TWMP generalizes this insight into a principled LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target. Laiyk et al. (ACL 2025 Long, arXiv:2502.13647) fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP requires no target-language labels and applies equally to Mongolian and Uyghur where no comparable dataset exists. Revisiting Multilingual Data Mixtures (Foroutan et al., arXiv:2510.25947) studies reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); TWMP targets instruction-tuning scale where data volume, optimization dynamics, and gradient signal are qualitatively different. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) uses implicit reward transfer from English-aligned models to annotate cross-lingual DPO pairs (12.72% Win Rate on X-AlpacaEval); TWMP extends this direction to multi-pivot source selection weighted by typological distance targeting low-resource agglutinative languages absent from that work. Concurrent work 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678, March 2026) uses DPO for factual consistency across 26 languages—orthogonal in objective (knowledge coherence vs. language fidelity) and not addressing low-resource instruction tuning. A concurrent theoretical framework (arXiv:2604.06202, April 2026) proposes the Turkic Transfer Coefficient (TTC) for cross-lingual adaptation within the Turkic family but offers no training method or instruction tuning experiments. Two directly adjacent works are carefully differentiated: TIPA (EACL 2026) aggregates MAD-X encoder adapters at inference time without training; arXiv:2410.07809 uses k-means on legacy 289-dim URIEL for discrete language selection on BLOOM/mGPT with zero Kazakh/Mongolian/Uyghur coverage. We fine-tune Qwen3.5-9B with QLoRA (released March 2026; 248K-token vocabulary, 201 languages; 0.8B/2B/4B/9B series—no 7B variant), targeting Kazakh, Mongolian, and Uyghur, evaluated on KazMMLU (Kazakh-language subset, ~11K questions), MiLiC-Eval, and TUMLU (all ACL 2025). Ablations cover full URIEL+ vs. Laplacian-300 vs. syntax-only vs. morphology-only vs. k-means discrete baseline; curriculum variants; DPO quality gate (fastText-only vs. length-gated); DPO vs. SFT-only. Swahili is the held-out agglutinative generalization target. Manual mode (200 A100h ≈ 120 H100h) and human-in-loop mode (310 A100h ≈ 186 H100h) stay within the ≤200 H100-hour budget; auto_research mode (600 A100h ≈ 360 H100h) exceeds the constraint and is not viable within budget. ACL 2027 (ARR August 3, 2026) is the primary target venue.\",\n  \"project_name\": \"typological_multi_pivot\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 9)\nIssues: [\"MINOR (NEW) – 'Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models' (arXiv:2505.16385, May 2026) appears in search results as a concurrent work using pivot-based methods for cross-lingual transfer. Its title directly parallels TWMP's multi-pivot framing. The paper is recent enough (May 2026) that the generator may have missed it. The generator should fetch the abstract of arXiv:2505.16385 to determine whether it uses typological-distance-based pivot selection or curriculum ordering; if it does, it constitutes a concurrent work requiring explicit differentiation in Section 2. If it addresses only semantic-space pivots (concept alignment) orthogonal to typological distance, a one-sentence dismissal suffices.\", \"MINOR (NEW) – 'Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+' (arXiv:2510.19217, October 2025) proposes structure-aware URIEL+ representations—speaker-weighted geographic distributions, hyperbolic embeddings for genealogy, and latent variable models for typology—directly addressing URIEL+ distance calibration quality. Since TWMP's entire weighting scheme rests on cosine distances computed from URIEL+ features, this adjacent work on URIEL+ representation quality should be acknowledged (one sentence suffices) or explicitly noted as an avenue for future improvement alongside the already-cited arXiv:2510.27183 LREC 2026 extension. The omission is less critical than the arXiv:2510.27183 gap (which is already fixed), but the paper has been available since October 2025 and EMNLP reviewers working on multilingual representation may notice it.\"]\nFeedback: This is Round 9. Both Round 8 issues are fully resolved: Budget-Xfer is now correctly cited as 'submitted to SIGIR 2026 Short Paper track' with 'preprint only, acceptance not yet confirmed,' and the 'Less is More' ρ values (ρ=0.358, p=0.061 for Laplacian-300; ρ=0.260 for full 800-feature; +7.8% LangRank) are independently verified from the ACL Anthology paper (aclanthology.org/2025.emnlp-main.1310/) and confirmed accurate. Independent search found two new minor items:\n\n(1) Check arXiv:2505.16385 ('Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models', May 2026). Fetch the abstract and determine whether it uses typological-distance-based pivot selection or curriculum ordering. If so, add one sentence differentiating it from TWMP's URIEL+-weighted staged curriculum; if it addresses semantic-space alignment orthogonal to typological distance, one sentence dismissal suffices.\n\n(2) Add arXiv:2510.19217 ('Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+') to the URIEL+ tooling paragraph in Section 3 (alongside the already-cited arXiv:2510.27183). One sentence: 'A concurrent representation study [arXiv:2510.19217] proposes structure-aware URIEL+ calibration via hyperbolic genealogy embeddings and latent typology models; TWMP uses the standard COLING 2025 URIEL+ cosine distances with SoftImpute, which suffice for the qualifying Aya pivot languages.'\n\nBoth are writing-only additions requiring no new experiments. Round 10 will force a pass/fail determination: if these two minor items are addressed, the paper meets the bar for ACL 2027 (ARR August 3, 2026) as a solid methodological contribution with clear differentiation, verified compute feasibility, and peer-reviewed evaluation grounding. The primary remaining uncertainty is empirical (actual performance gains over CLO/PROM/LangGPS baselines), which is expected at the proposal stage.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 9 轮修订，近 3 轮的平均分从 3.8 到 3.6，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T08:25:00.867Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T08:25:00.867Z",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935"
}
```

---

## Round 1

21 recorded events

### User

_source line 3 · 2026-05-10T08:25:00.894Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning",
  "core_problem": "Cross-lingual instruction tuning for low-resource languages defaults to English as the sole pivot, creating systematic gaps for languages that are typologically distant from English—particularly those with agglutinative morphology, non-Latin scripts, or SOV word order. Three peer-reviewed ACL 2025 benchmarks—KazMMLU (Kazakh), MiLiC-Eval (Tibetan, Uyghur, Kazakh, Mongolian), and TUMLU (Turkic languages including Kazakh and Uyghur)—confirm that even frontier multilingual LLMs (GPT-4, Llama-3.1, Qwen-2.5) achieve near-random performance on Mongolian comprehension tasks and substantially below-par accuracy on Kazakh and Uyghur relative to typologically proximate high-resource languages. No existing instruction tuning method uses typological distance to continuously weight data-source selection across a multi-pivot mixture for these under-represented language families.",
  "opportunity": "Three complementary ACL 2025 benchmarks provide peer-reviewed grounding for the performance gap. KazMMLU (arXiv:2502.12829; ACL 2025 long paper) comprises 23K questions total (approximately 11K in Kazakh, 12K in Russian) spanning STEM, humanities, and social sciences sourced from authentic Kazakhstani educational materials; for TWMP's Kazakh instruction evaluation, only the Kazakh-language subset (~11K questions) is relevant; evaluation of Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 shows 'substantial room for improvement' for all models on Kazakh, despite the language having 20 million speakers. MiLiC-Eval (arXiv:2503.01150; ACL 2025 Findings) covers Tibetan, Uyghur, Kazakh, and Mongolian across 9 tasks with 24K instances; GPT-4o-mini achieves only slightly above random on Mongolian tasks, and models exhibit only 'preliminary understanding' of Tibetan and Kazakh. TUMLU (arXiv:2502.11020; ACL 2025 long paper) provides 38K native questions spanning 11 academic subjects across Turkic languages including Kazakh and Uyghur, enabling controlled within-family comparisons that isolate the effect of lower training corpus size. The XLM-SWCM paper (arXiv:2502.10852) additionally shows that encoder-based shared-weight cross-lingual pretraining partially bridges these gaps—Kazakh ROUGE-L summarization score of 5.6 is notably the lowest among the four minority languages studied—but this approach does not scale to instruction-following for decoder LLMs. CLO (arXiv:2505.14297; ACL 2025) shows that DPO-style cross-lingual preference optimization with only 3,200 samples outperforms standard SFT with 6,400 samples, establishing strong data efficiency for cross-lingual transfer. 'Do Chinese Models Speak Chinese Languages?' (arXiv:2504.00289, April 2026) evaluates 10 LLMs across 21 language variants and finds that Llama3-Instruct is the only model showing distinctive Uyghur capability while most models reach only ~75% Mongolian identification accuracy; Chinese LLMs do not outperform Western counterparts on minority languages including Uyghur and Mongolian, confirming that the performance gap TWMP targets persists even in the most recent model generation. These findings together create a clear opening: by weighting instruction data from multiple source languages inversely by URIEL+ typological distance and introducing a staged curriculum, we can build a principled multi-pivot training regime that directly addresses the English-pivot bottleneck for agglutinative low-resource targets.",
  "landscape": "PLUG (ACL 2024) established that English-pivot cross-lingual instruction generation improves multilingual instruction following—but its reported 29% improvement was measured on Chinese, Korean, Italian, and Spanish. Whether the English-pivot advantage holds for typologically distant agglutinative languages with non-Latin scripts (Kazakh, Mongolian, Uyghur) is an assumption that TWMP directly tests rather than takes for granted. CLO (arXiv:2505.14297; ACL 2025) improves data efficiency via DPO-style cross-lingual preference optimization using 6,400 OpenAssistant samples machine-translated by M2M100; it fixes English as the sole source language without varying source selection by typological distance. PROM [NAACL 2025, aclanthology.org/2025.naacl-short.19/] (Pivoted and Regulated Optimization for Multilingual Instruction Learning) treats English as an internal pivot and disentangles English vs. target-language training objectives via separate regularized losses to reduce negative interference; like PLUG and CLO, PROM presupposes a single English pivot without addressing typological distance, multi-pivot source selection, or agglutinative low-resource targets such as Kazakh, Mongolian, and Uyghur. LangGPS [Ye et al., AAAI 2026, arXiv:2511.10229] selects multilingual instruction data based on language separability scores derived from the model's own representation space, demonstrating improvements across 22 languages including low-resource targets. Unlike LangGPS, TWMP uses external typological features from URIEL+ to derive a pivot ordering independent of training dynamics, and integrates a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer [arXiv:2603.27651, 2026; submitted to SIGIR 2026 Short Paper track] formulates multi-source cross-lingual transfer as a budget-constrained allocation problem for NER/sentiment tasks; TWMP's typological-distance weighting and staged curriculum provide a principled ordering mechanism for instruction tuning that Budget-Xfer does not address. Code-Switching Curriculum Learning [Yoo et al., ACL 2025 Findings, arXiv:2411.02460] proposes a 3-stage curriculum (token-level → sentence-level → monolingual code-switching) for a single language pair; TWMP's curriculum operates over a pool of typologically ordered pivot languages without code-switching and targets a set of related agglutinative languages rather than a single target. Revisiting Multilingual Data Mixtures [Foroutan et al., 2025, arXiv:2510.25947] studies reweighting across 25–400 languages at pretraining scale (1.1B–3B parameters); TWMP operates at instruction-tuning scale—10 epochs, LoRA, narrow near-family pivot pool—where the data volume, optimization dynamics, and gradient signal are qualitatively different from the pretraining regime. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh, English, Russian, and Turkish, and demonstrates that Turkish as an auxiliary language improves Kazakh performance—directly motivating TWMP's inclusion of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc four-language selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language, with principled pivot selection replacing language-specific engineering. Laiyk et al. [ACL 2025 Long, arXiv:2502.13647] fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP does not require any target-language instruction labels and applies equally to Mongolian and Uyghur, where no comparable GPT-4-assisted dataset currently exists. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving a 12.72% average Win Rate improvement on X-AlpacaEval; it uses English as the sole source and implicit reward annotation without typological weighting—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from that work. 'Family Matters' (arXiv:2510.00810) applies language transfer and LoRA merging from typologically related Nordic languages to Faroese—demonstrating that typological proximity helps—but as a single-language case study with no generalizable training recipe. 'Cross-Linguistic Transfer in Multilingual NLP' (arXiv:2505.13908) analyzes language family and morphology effects empirically without proposing a training method. Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) decouples task and language LoRA adapters but does not use typological features to parameterize or weight the language adapter. 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678; Tianyu Liu et al., March 2026) introduces a DPO-inspired method—concurrent with TWMP—that enforces factual consistency of model responses across 26 languages and 9 LLMs; its preference pairs encode semantic equivalence of knowledge across languages (chosen = factually consistent cross-lingual response, rejected = factually inconsistent response). This objective is orthogonal to TWMP's: DCO addresses what the model says across languages (knowledge coherence), while TWMP addresses which language it responds in when given instructions in any of multiple pivot languages (instruction-language fidelity). DCO does not address low-resource instruction tuning, multi-pivot source selection, or typological-distance weighting. A concurrent theoretical framework 'Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family' (arXiv:2604.06202, April 2026) proposes the Turkic Transfer Coefficient (TTC), a composite typological similarity metric combining morphological, lexical, syntactic, and script compatibility for Turkic languages. Unlike TWMP, arXiv:2604.06202 is a theoretical analysis without training method, instruction tuning experiments, or evaluation on KazMMLU, MiLiC-Eval, or TUMLU; it corroborates the motivation for Turkic-pivot weighting but does not instantiate it empirically. Two works require careful differentiation from TWMP. First, TIPA (arXiv:2601.16629; EACL 2026 Findings) constructs proxy language adapters by aggregating existing MAD-X adapters weighted by typological similarity across 230+ languages—entirely without training. TIPA is orthogonal to TWMP in three key ways: (1) it is training-free inference-time adapter aggregation, whereas TWMP learns from a typologically-weighted data curriculum; (2) it operates on encoder-based MAD-X modules for classification tasks, whereas TWMP targets decoder LLM instruction tuning; (3) TIPA has not been applied to instruction generation or to languages not already represented by a dedicated adapter. Second, 'Linguistically-Informed Multilingual Instruction Tuning' (arXiv:2410.07809) uses 289-dimensional legacy URIEL TYPO vectors with k-means clustering to select 14 discrete representative languages from a 52-language pool (one per cluster) for LoRA fine-tuning on Bactrian-X, showing that typologically diverse selection beats random selection. TWMP differs substantially: rather than discrete cluster-representative selection, TWMP applies continuous inverse-distance sampling weights over the full Aya collection using compact URIEL+ features (300-dim, Laplacian Score selected); it adds a staged cosine-distance curriculum schedule; it integrates a multi-source DPO preference optimization objective for language fidelity; and it directly targets Kazakh, Mongolian, and Uyghur—languages for which arXiv:2410.07809's evaluation suite (XNLI, XCOPA, XStoryCloze, XWinograd, PAWS-X) provides zero coverage. The combination of continuous URIEL+ weighting, staged curriculum, precisely formulated multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering the target languages constitutes a principled and differentiated advance.",
  "approach": "We propose Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, which replaces PLUG's single-English pivot with a principled mixture over multiple source languages drawn from the Aya collection (513M instances across 114 languages).\n\nAya pivot coverage is verified before training: Turkish (high-resource, multi-million instances), Kyrgyz (~4.1M instances in the Aya collection language split), Uzbek (confirmed present as an underrepresented language with meaningful coverage), and Azerbaijani all qualify as pivot sources. A minimum threshold of 5,000 Aya instances per pivot language is enforced; languages below this threshold are excluded from the mixture. All qualifying pivot languages and their instance counts are reported in an appendix table. Kazakh, Mongolian, and Uyghur serve exclusively as evaluation targets and are never included in the pivot mixture.\n\nTypological distances are computed using URIEL+ (arXiv:2409.18472, COLING 2025; available via the urielplus Python library at github.com/LeeLanguageLab/URIELPlus) rather than the legacy lang2vec 289-dimensional binary features. URIEL+ expands coverage to 4,366 languages with approximately 800 features (607 grammar features covering syntactic and morphological dimensions, plus 193 sound features), and applies SoftImpute for missing-value imputation—critical for reducing sparsity in Kazakh, Uzbek, and Kyrgyz, where legacy URIEL features are known to be sparse. URIEL+ explicitly represents Kazakh's multi-script properties (Cyrillic, Latin, and Arabic) via script vectors. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds script vectors and Glottolog genealogies to URIEL+, covering 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for the qualifying Aya pivot languages. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), which demonstrates that a Laplacian Score 300-feature subset of URIEL+ achieves Spearman ρ=0.358 (p=0.061; measured against linguistic similarity distance alignment metric G_d, Table 1) versus ρ=0.260 for the full 800-feature set, and additionally yields +7.8% improvement on LangRank downstream cross-lingual NLP tasks, we apply this feature selection before computing cosine distances. The downstream task gains (+7.8% LangRank) provide the primary empirical justification for the feature selection step; the typological alignment improvement (p=0.061) is directionally consistent but borderline significant and should not be cited as standalone evidence. Data-sampling weights are assigned inversely proportional to these 300-feature URIEL+ cosine distances, so morphologically close pivots such as Turkish or Uzbek for Kazakh receive substantially higher weight than English.\n\nThe staged curriculum uses three phases calibrated by the empirical URIEL+ distance distribution of qualifying Aya pivot languages relative to each target language. Let D_25 and D_60 denote the 25th and 60th percentile distances from the target language to all qualifying Aya pivots (computed once, before training). Stage 1 (epochs 1–3): exclusively sources with cosine distance < D_25—for Kazakh, approximately ≤0.32, capturing Turkish, Kyrgyz, Uzbek, and Azerbaijani. Stage 2 (epochs 4–6): sources with distance < D_60 (approximately ≤0.56 for Kazakh), expanding to Russian, Arabic, and other mid-distance languages. Stage 3 (epochs 7–10): full mixture over all qualifying pivot languages with continuous inverse-distance weights. Thresholds are target-specific and computed from the actual Aya-pivot distance distribution; for Mongolian, where no Turkic pivot falls within D_25, the closest available Aya sources (Korean, Finnish, Turkish) are used across all three stages with correspondingly small weights—this distance-constrained Mongolian setting is a controlled finding of interest. Ablations compare: no curriculum (full weighted mixture from epoch 1), 2-stage (merging Stages 1–2), 3-stage (proposed), and linear interpolation between stages.\n\nThe CLO-style DPO preference optimization objective is precisely extended to the multi-source setting. For each source pivot language s_i and target language t, preference pairs are defined as: chosen = (x_{s_i}, y^w_t)—an instruction in source language s_i paired with a model-generated response identified as being in the target language t; rejected = (x_{s_i}, y^l_{s_i})—the same instruction paired with a model-generated response in source language s_i. This formulation promotes target-language responses to source-language instructions and differs from CLO's English-source objective in a critical respect: CLO's English-input pair (chosen=English response, rejected=target-language response) is designed to preserve English capability by penalizing cross-lingual output for English inputs. TWMP inverts this preference because the training goal is acquisition of cross-lingual target-language instruction following: for any source-language input, we want the model to respond in the target language. TWMP does not use CLO's second pair type (target-language input → prefer target-language response) because target-language training data is explicitly excluded.\n\nPreference pairs are constructed entirely without target-language labels via automatic language identification: given each source-language instruction x_{s_i}, we sample K=8 candidate responses from Qwen3.5-9B at temperature 0.7; apply fastText language identification (lid.176.bin) to each candidate; assign responses identified as the target language to the chosen pool and responses identified as the source language to the rejected pool; apply a minimum 20-token length gate to both pools to exclude degenerate or near-empty responses; pair the highest-scoring chosen (by fastText language ID confidence) with the lowest-scoring rejected per instruction. Instructions yielding no target-language candidates in K=8 samples after the length filter fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row in the DPO evaluation table compares fastText-only selection (no length gate) against length-gated selection (≥20 tokens) to quantify the quality impact of this filter; this also characterizes the frequency of degenerate responses per source-target pair. As a mandatory prerequisite check, we run a 500-instruction probe per source-target language pair on the base Qwen3.5-9B and verify that target-language responses (meeting the ≥20-token gate) appear in >5% of K=8 samples; any pivot language pair failing this check is excluded from DPO training (falling back to SFT-weighted sampling only) for that target language. This probe is reported as a characterization result: for close Turkic pivots (Turkish→Kazakh), we expect the frequency to exceed 5% given Qwen3.5-9B's broad multilingual coverage; for distant pivots (English→Mongolian), the check may filter some source languages, which is informative about which pivots can drive DPO-based cross-lingual preference learning.\n\nWe apply QLoRA fine-tuning of Qwen3.5-9B (released March 2026; 248K-token vocabulary spanning 201 languages; the Qwen3.5 small series has 0.8B/2B/4B/9B variants—no 7B exists) on this weighted multi-pivot dataset, targeting Kazakh, Mongolian, and Uyghur as primary evaluation cases. Evaluation uses three ACL 2025 benchmarks: KazMMLU for Kazakh (Kazakh-language subset, ~11K questions), MiLiC-Eval for all three targets across 9 tasks, and TUMLU for Kazakh and Uyghur within a controlled within-Turkic-family comparison. PLUG, PROM [NAACL 2025], and CLO serve as primary English-pivot baselines. Typological weighting ablations compare: full 800-feature URIEL+ vs. Laplacian-selected 300 features vs. syntax-only (474 features) vs. morphology-only (133 features) vs. the k-means discrete selection baseline from arXiv:2410.07809. Swahili serves as a held-out agglutinative generalization target not used during hyperparameter design. Note: TyDi QA covers Arabic, Bengali, Finnish, Indonesian, Japanese, Kiswahili, Korean, Russian, Telugu, and Thai—it does not include Kazakh, Mongolian, or Uyghur and is not used here.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200h A100 (15–20 QLoRA runs × 10–13h each on Qwen3.5-9B, covering 3 primary target languages, PLUG/CLO/PROM baselines, URIEL+ sub-space ablations, curriculum schedule variants, DPO quality gate ablation row, and DPO prerequisite probe runs)",
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
    "PROM: Pivoted and Regulated Optimization for Multilingual Instruction Learning (NAACL 2025, aclanthology.org/2025.naacl-short.19/) [treats English as an internal pivot and disentangles English vs. target-language training objectives via regulated losses to reduce negative interference; like PLUG and CLO, fixes English as the sole pivot without addressing typological distance, multi-pivot sequencing, or agglutinative low-resource targets—cited as an English-pivot baseline alongside PLUG and CLO]",
    "LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning (Ye et al., AAAI 2026, arXiv:2511.10229) [selects multilingual instruction data using language separability scores from the model's own representation space across 22 languages including low-resource targets; differentiated from TWMP's external URIEL+ typological weighting independent of training dynamics, staged curriculum, and multi-source DPO objective]",
    "Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages (Idris et al., arXiv:2603.27651, 2026; submitted to SIGIR 2026 Short Paper track) [multi-source cross-lingual transfer as budget-constrained resource allocation for NER and sentiment analysis on Hausa, Yoruba, and Swahili across 288 experiments; no typological features or curriculum ordering—differentiated from TWMP's URIEL+-weighted staged instruction tuning; note: preprint only, acceptance not yet confirmed]",
    "Code-Switching Curriculum Learning for Multilingual Transfer in LLMs (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) [3-stage curriculum (token-level → sentence-level → monolingual code-switching) for single language pair; primary focus Korean, with Japanese and Indonesian—differentiated from TWMP's multi-pivot typological curriculum without code-switching targeting a family of related agglutinative languages]",
    "Revisiting Multilingual Data Mixtures in Language Model Pretraining (Foroutan et al., arXiv:2510.25947, ICLR-submitted 2025) [multilingual data reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); differentiated from TWMP's instruction-tuning-scale LoRA curriculum where data volume, optimization dynamics, and gradient signal are qualitatively different]",
    "Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh (Laiyk et al., ACL 2025 Long, arXiv:2502.13647) [10,600 GPT-4o-assisted Kazakh instruction examples fine-tuning Qwen/Falcon/Gemma; requires target-language labels and is Kazakh-specific—differentiated from TWMP's label-free multi-target approach covering Mongolian and Uyghur equally]",
    "Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+ (Shipton et al., LREC 2026, arXiv:2510.27183) [extends URIEL+ with script vectors and Glottolog genealogies for 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages]",
    "Llama-3.1-Sherkala-8B-Chat (arXiv:2503.01493) [trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish; demonstrates Turkish as auxiliary language improves Kazakh performance via full fine-tuning; differentiated from TWMP's generalizable LoRA recipe parameterized by continuous URIEL+ distances]",
    "Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) [implicit reward transfer from English-aligned DPO model to annotate cross-lingual preference pairs; 12.72% Win Rate improvement on X-AlpacaEval; English-only source with no typological weighting—differentiated from TWMP's multi-pivot source selection and low-resource agglutinative targets]",
    "URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base (arXiv:2409.18472, COLING 2025) [~800-feature typological database covering 4,366 languages with SoftImpute for low-resource Turkic languages; replaces legacy lang2vec 289-dim URIEL in TWMP; official repository: github.com/LeeLanguageLab/URIELPlus]",
    "Less is More: The Effectiveness of Compact Typological Language Representations (arXiv:2509.20129, EMNLP 2025) [Laplacian Score 300-feature URIEL+ subset achieves ρ=0.358 (p=0.061; measured on linguistic distance alignment against G_d metric, Table 1) vs. ρ=0.260 for full 800-feature URIEL+; downstream improvement of +7.8% on LangRank tasks; ρ values verified from paper HTML; downstream gains provide the primary justification for TWMP's feature selection step—the typological alignment improvement is directionally consistent but borderline significant]",
    "Optimizing Language Models for Crosslingual Knowledge Consistency (arXiv:2603.04678; Tianyu Liu et al., March 2026) [concurrent DPO-inspired work targeting factual consistency across 26 languages and 9 LLMs—orthogonal to TWMP's language-fidelity DPO objective; differentiated in related work]",
    "TIPA: Typologically Informed Parameter Aggregation (arXiv:2601.16629, EACL 2026 Findings) [training-free encoder adapter aggregation across 230+ languages—differentiated from TWMP's training-time decoder curriculum]",
    "Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) [discrete k-means language selection using legacy 289-dim URIEL TYPO features on BLOOM/mGPT/mT5—differentiated from TWMP's continuous URIEL+ weighting, staged curriculum, multi-source DPO, and Turkic/Mongolic targets]",
    "Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family (arXiv:2604.06202, April 2026) [theoretical framework introducing Turkic Transfer Coefficient (TTC) combining morphological, lexical, syntactic, and script compatibility; no training method or instruction tuning experiments; no evaluation on KazMMLU/MiLiC-Eval/TUMLU—corroborates motivation for Turkic-pivot weighting without instantiating it empirically]",
    "KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan (ACL 2025, arXiv:2502.12829) [primary Kazakh evaluation benchmark; 23K total questions (approximately 11K in Kazakh, 12K in Russian) sourced from authentic Kazakhstani educational materials; peer-reviewed; TWMP evaluates on the Kazakh-language subset only]",
    "MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages (ACL 2025 Findings, arXiv:2503.01150) [primary evaluation for Uyghur, Kazakh, Mongolian across 9 tasks]",
    "TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages (ACL 2025, arXiv:2502.11020) [38K questions for Kazakh, Uyghur, and other Turkic languages; within-family controlled comparison]",
    "Do Chinese Models Speak Chinese Languages? (arXiv:2504.00289, April 2026) [evaluates 10 LLMs across 21 language variants including Uyghur, Mongolian, Kazakh, and Tibetan; Llama3-Instruct is uniquely capable at Uyghur and ranks highest on Mongolian; Chinese LLMs do not outperform Western counterparts on minority languages—contemporary evidence for the performance gap TWMP addresses]",
    "Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages (arXiv:2502.10852) [encoder-based cross-lingual transfer for Tibetan/Uyghur/Kazakh/Mongolian; motivation for decoder LLM gap]",
    "Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese (arXiv:2510.00810, 2025)",
    "Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology (arXiv:2505.13908, 2025)",
    "Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) [workshop paper, not main conference]",
    "Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models (arXiv:2603.21036, 2026) [supplementary qualitative observation; single-author preprint with 50 hand-crafted questions—not primary motivation anchor]"
  ],
  "description": "This paper introduces Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, a method for adapting decoder LLMs to low-resource languages that are typologically distant from English. Rather than using a single English pivot as in PLUG, we compute typological distances using URIEL+ (arXiv:2409.18472, COLING 2025; urielplus Python library at github.com/LeeLanguageLab/URIELPlus), which covers ~800 features across 4,366 languages with SoftImpute imputation—critical for low-resource Turkic languages where legacy lang2vec 289-dim URIEL is known to be sparse. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds Glottolog genealogies covering 26,449 languages; TWMP uses the COLING 2025 base version, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), we apply Laplacian Score feature selection to reduce URIEL+ to 300 compact features (Spearman ρ=0.358, p=0.061, measured on linguistic distance alignment with G_d metric, Table 1; +7.8% improvement on LangRank downstream tasks; vs. ρ=0.260 for the full 800-feature set; ρ values verified from paper HTML—the downstream gains are the primary justification, as the typological alignment improvement is directionally consistent but borderline significant) before computing cosine distances and assigning inverse-distance sampling weights over the Aya collection. Aya pivot coverage is verified: Turkish (multi-million instances), Kyrgyz (~4.1M instances), and Uzbek all clear a 5,000-instance minimum threshold; Kazakh, Mongolian, and Uyghur are evaluation-only targets excluded from the pivot pool. Contemporary evidence from 'Do Chinese Models Speak Chinese Languages?' (arXiv:2504.00289, April 2026), which evaluates 10 LLMs across 21 language variants, shows that Llama3-Instruct is the only evaluated model with distinctive Uyghur capability and that Chinese LLMs do not outperform Western counterparts on minority languages including Uyghur and Mongolian—confirming that no current model family addresses the performance gap TWMP targets. LangGPS (Ye et al., AAAI 2026, arXiv:2511.10229) selects multilingual instruction data by language separability from the model's own representation space across 22 languages; TWMP instead uses external URIEL+ features independent of training dynamics, with a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer (Idris et al., arXiv:2603.27651, 2026; submitted to SIGIR 2026 Short Paper track) frames multi-source transfer as budget-constrained allocation for NER/sentiment tasks without typological features or curriculum ordering—TWMP's principled weighting and staged scheduling address instruction tuning specifically. A staged 3-phase curriculum progressively introduces more distant pivots using percentile thresholds computed from the empirical URIEL+ distance distribution of qualifying Aya pivots per target: Stage 1 (epochs 1–3) uses sources within the 25th percentile distance threshold (~≤0.32 for Kazakh, capturing Turkish/Kyrgyz/Uzbek/Azerbaijani); Stage 2 (epochs 4–6) expands to the 60th percentile (~≤0.56); Stage 3 (epochs 7–10) uses the full weighted mixture. Code-Switching Curriculum Learning (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) proposes a 3-stage code-switching curriculum for a single language pair; TWMP's curriculum spans a typologically ordered pool of pivot languages without code-switching. The DPO preference optimization objective is precisely formulated for the multi-source case: for source pivot s_i and target t, chosen = (instruction in s_i, model-generated response in t); rejected = (instruction in s_i, model-generated response in s_i). This inverts CLO's English-input pair direction—CLO prefers English responses to English inputs (preserving English capability), while TWMP prefers target-language responses to any source-language input (promoting cross-lingual instruction following). PROM [NAACL 2025] similarly treats English as an internal pivot and disentangles English and target-language training objectives via regulated losses; like PLUG and CLO, PROM fixes a single English pivot without addressing typological distance or multi-pivot sequencing for agglutinative targets—all three serve as English-pivot baselines in TWMP's evaluation. Pairs are auto-constructed by sampling K=8 responses per instruction from Qwen3.5-9B, applying fastText language identification, and applying a minimum 20-token length gate to both chosen and rejected pools to exclude degenerate responses; no target-language training labels are required. Instructions yielding no target-language candidates post-gate fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row compares fastText-only selection against length-gated selection to quantify the quality impact of this filter. A mandatory 500-instruction prerequisite probe verifies >5% target-language response frequency (post-length-gate) per source-target pair; pairs failing this check fall back to SFT-only. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish and demonstrates the value of Turkish as an auxiliary language for Kazakh via full fine-tuning, motivating TWMP's Turkic pivot inclusion; TWMP generalizes this insight into a principled LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target. Laiyk et al. (ACL 2025 Long, arXiv:2502.13647) fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP requires no target-language labels and applies equally to Mongolian and Uyghur where no comparable dataset exists. Revisiting Multilingual Data Mixtures (Foroutan et al., arXiv:2510.25947) studies reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); TWMP targets instruction-tuning scale where data volume, optimization dynamics, and gradient signal are qualitatively different. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) uses implicit reward transfer from English-aligned models to annotate cross-lingual DPO pairs (12.72% Win Rate on X-AlpacaEval); TWMP extends this direction to multi-pivot source selection weighted by typological distance targeting low-resource agglutinative languages absent from that work. Concurrent work 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678, March 2026) uses DPO for factual consistency across 26 languages—orthogonal in objective (knowledge coherence vs. language fidelity) and not addressing low-resource instruction tuning. A concurrent theoretical framework (arXiv:2604.06202, April 2026) proposes the Turkic Transfer Coefficient (TTC) for cross-lingual adaptation within the Turkic family but offers no training method or instruction tuning experiments. Two directly adjacent works are carefully differentiated: TIPA (EACL 2026) aggregates MAD-X encoder adapters at inference time without training; arXiv:2410.07809 uses k-means on legacy 289-dim URIEL for discrete language selection on BLOOM/mGPT with zero Kazakh/Mongolian/Uyghur coverage. We fine-tune Qwen3.5-9B with QLoRA (released March 2026; 248K-token vocabulary, 201 languages; 0.8B/2B/4B/9B series—no 7B variant), targeting Kazakh, Mongolian, and Uyghur, evaluated on KazMMLU (Kazakh-language subset, ~11K questions), MiLiC-Eval, and TUMLU (all ACL 2025). Ablations cover full URIEL+ vs. Laplacian-300 vs. syntax-only vs. morphology-only vs. k-means discrete baseline; curriculum variants; DPO quality gate (fastText-only vs. length-gated); DPO vs. SFT-only. Swahili is the held-out agglutinative generalization target. Manual mode (200 A100h ≈ 120 H100h) and human-in-loop mode (310 A100h ≈ 186 H100h) stay within the ≤200 H100-hour budget; auto_research mode (600 A100h ≈ 360 H100h) exceeds the constraint and is not viable within budget. ACL 2027 (ARR August 3, 2026) is the primary target venue.",
  "project_name": "typological_multi_pivot",
  "source": "web_research"
}

## Reviewer feedback (round 9)
Issues: ["MINOR (NEW) – 'Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models' (arXiv:2505.16385, May 2026) appears in search results as a concurrent work using pivot-based methods for cross-lingual transfer. Its title directly parallels TWMP's multi-pivot framing. The paper is recent enough (May 2026) that the generator may have missed it. The generator should fetch the abstract of arXiv:2505.16385 to determine whether it uses typological-distance-based pivot selection or curriculum ordering; if it does, it constitutes a concurrent work requiring explicit differentiation in Section 2. If it addresses only semantic-space pivots (concept alignment) orthogonal to typological distance, a one-sentence dismissal suffices.", "MINOR (NEW) – 'Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+' (arXiv:2510.19217, October 2025) proposes structure-aware URIEL+ representations—speaker-weighted geographic distributions, hyperbolic embeddings for genealogy, and latent variable models for typology—directly addressing URIEL+ distance calibration quality. Since TWMP's entire weighting scheme rests on cosine distances computed from URIEL+ features, this adjacent work on URIEL+ representation quality should be acknowledged (one sentence suffices) or explicitly noted as an avenue for future improvement alongside the already-cited arXiv:2510.27183 LREC 2026 extension. The omission is less critical than the arXiv:2510.27183 gap (which is already fixed), but the paper has been available since October 2025 and EMNLP reviewers working on multilingual representation may notice it."]
Feedback: This is Round 9. Both Round 8 issues are fully resolved: Budget-Xfer is now correctly cited as 'submitted to SIGIR 2026 Short Paper track' with 'preprint only, acceptance not yet confirmed,' and the 'Less is More' ρ values (ρ=0.358, p=0.061 for Laplacian-300; ρ=0.260 for full 800-feature; +7.8% LangRank) are independently verified from the ACL Anthology paper (aclanthology.org/2025.emnlp-main.1310/) and confirmed accurate. Independent search found two new minor items:

(1) Check arXiv:2505.16385 ('Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models', May 2026). Fetch the abstract and determine whether it uses typological-distance-based pivot selection or curriculum ordering. If so, add one sentence differentiating it from TWMP's URIEL+-weighted staged curriculum; if it addresses semantic-space alignment orthogonal to typological distance, one sentence dismissal suffices.

(2) Add arXiv:2510.19217 ('Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+') to the URIEL+ tooling paragraph in Section 3 (alongside the already-cited arXiv:2510.27183). One sentence: 'A concurrent representation study [arXiv:2510.19217] proposes structure-aware URIEL+ calibration via hyperbolic genealogy embeddings and latent typology models; TWMP uses the standard COLING 2025 URIEL+ cosine distances with SoftImpute, which suffice for the qualifying Aya pivot languages.'

Both are writing-only additions requiring no new experiments. Round 10 will force a pass/fail determination: if these two minor items are addressed, the paper meets the bar for ACL 2027 (ARR August 3, 2026) as a solid methodological contribution with clear differentiation, verified compute feasibility, and peer-reviewed evaluation grounding. The primary remaining uncertainty is empirical (actual performance gains over CLO/PROM/LangGPS baselines), which is expected at the proposal stage.

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
这个 idea 已经经过 9 轮修订，近 3 轮的平均分从 3.8 到 3.6，没有明显改善。

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
  "promptId": "93ff0712-c390-41e4-8983-1f0a5d6df198",
  "type": "user",
  "uuid": "fc613737-6cda-4dde-878a-fbd918b2d0b7",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T08:25:00.892Z_

```json
{
  "parentUuid": "fc613737-6cda-4dde-878a-fbd918b2d0b7",
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
  "uuid": "dbafbd67-b54c-458c-b176-e805c565107f",
  "timestamp": "2026-05-10T08:25:00.892Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T08:25:00.892Z_

```json
{
  "parentUuid": "dbafbd67-b54c-458c-b176-e805c565107f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c07ee108-6b36-477e-965b-44388b4ca251",
  "timestamp": "2026-05-10T08:25:00.892Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
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
  "leafUuid": "c07ee108-6b36-477e-965b-44388b4ca251",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise TWMP for ACL 2027 to address concurrent pivot methods and URIEL+ calibration",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935"
}
```

---

### Assistant

_source line 8 · 2026-05-10T08:25:17.675Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully before proceeding.

**Current State:**
- This is Round 9 of revisions
- The idea has been through many iterations with stagnating scores (3.8 to 3.6 over recent rounds)
- The reviewer feedback for this round is actually quite positive - both Round 8 issues are fully resolved
- Round 9 has only two NEW MINOR issues that require writing-only additions (no new experiments)
- The reviewer says "Round 10 will force a pass/fail determination" and if these two minor items are addressed, "the paper meets the bar for ACL 2027"


- I need to handle two specific papers: one on semantic pivots for cross-lingual transfer where I'll need to check if it uses typological-distance-based selection or curriculum ordering to determine how to differentiate from our work, and another on modality matching in URIEL+ that just needs a single sentence addition.

The reviewer is signaling these are genuinely minor writing fixes, not fundamental issues with the approach. Rather than overhaul the paper, I should make these targeted additions and fetch the first paper to understand exactly what it does so I can position our work correctly against it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c07ee108-6b36-477e-965b-44388b4ca251",
  "isSidechain": false,
  "requestId": "req_011CatZuuEu1YPFaFmxSoENB",
  "type": "assistant",
  "uuid": "b7841212-4994-4d85-bbd2-1764cfe795ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Vn4DAqCcdk8Md4uafJZA6k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18646,
      "cache_read_input_tokens": 11631,
      "output_tokens": 632,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18646,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 632,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18646,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18646
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

_source line 9 · 2026-05-10T08:25:18.073Z_

I'll fetch both flagged papers before writing any text, so the differentiation is grounded in what they actually say.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7841212-4994-4d85-bbd2-1764cfe795ef",
  "isSidechain": false,
  "requestId": "req_011CatZuuEu1YPFaFmxSoENB",
  "type": "assistant",
  "uuid": "cab4e248-c9ad-4252-94f9-4348b10b6738",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Vn4DAqCcdk8Md4uafJZA6k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18646,
      "cache_read_input_tokens": 11631,
      "output_tokens": 632,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18646,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 632,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18646,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18646
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

_source line 10 · 2026-05-10T08:25:18.226Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01F5CTFtNAayHXtpMR15sodc`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cab4e248-c9ad-4252-94f9-4348b10b6738",
  "isSidechain": false,
  "requestId": "req_011CatZuuEu1YPFaFmxSoENB",
  "type": "assistant",
  "uuid": "895ba274-f7b9-4ddf-9474-5ce6d9913326",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Vn4DAqCcdk8Md4uafJZA6k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18646,
      "cache_read_input_tokens": 11631,
      "output_tokens": 632,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18646,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 632,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18646,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18646
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

_source line 11 · 2026-05-10T08:25:18.235Z_

<details><summary>↩ Tool result · `toolu_01F5CTFtNAayHXtpMR15sodc`</summary>

````text
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
  "parentUuid": "895ba274-f7b9-4ddf-9474-5ce6d9913326",
  "isSidechain": false,
  "promptId": "93ff0712-c390-41e4-8983-1f0a5d6df198",
  "type": "user",
  "uuid": "2cc88969-bfd1-4de2-8ecc-14b35f89b6e5",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "895ba274-f7b9-4ddf-9474-5ce6d9913326",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T08:25:20.715Z_

<details><summary>Logged reasoning block</summary>

```text
Good, now let me fetch both papers simultaneously.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cc88969-bfd1-4de2-8ecc-14b35f89b6e5",
  "isSidechain": false,
  "requestId": "req_011CatZwAhbo8qepWGwwJPUA",
  "type": "assistant",
  "uuid": "543f3029-0daa-480c-a55a-fcff237e229a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SukfzY2NvfsRQTtGigKtyH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 30277,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 348,
          "cache_read_input_tokens": 30277,
          "cache_creation_input_tokens": 1153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1153
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

_source line 13 · 2026-05-10T08:25:21.099Z_

Fetching both papers in parallel now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "543f3029-0daa-480c-a55a-fcff237e229a",
  "isSidechain": false,
  "requestId": "req_011CatZwAhbo8qepWGwwJPUA",
  "type": "assistant",
  "uuid": "d1724d9a-041a-459d-b38a-d04bd203aab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SukfzY2NvfsRQTtGigKtyH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 30277,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 348,
          "cache_read_input_tokens": 30277,
          "cache_creation_input_tokens": 1153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1153
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

_source line 14 · 2026-05-10T08:25:24.355Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JSYs35nybFG8mWV3yvxpu9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.16385",
  "prompt": "Extract the full abstract and any method overview. Specifically: does this paper use typological-distance-based pivot selection (e.g., URIEL, lang2vec, or similar typological databases)? Does it use a curriculum over multiple source languages ordered by linguistic distance? What does \"semantic pivots\" mean here — is it about concept-space/semantic alignment between languages, or about typological proximity? What are the target languages and what baselines does it compare to?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1724d9a-041a-459d-b38a-d04bd203aab8",
  "isSidechain": false,
  "requestId": "req_011CatZwAhbo8qepWGwwJPUA",
  "type": "assistant",
  "uuid": "1fbbc9c8-a691-45a3-a07a-81c2fa5bf7c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SukfzY2NvfsRQTtGigKtyH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 30277,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 348,
          "cache_read_input_tokens": 30277,
          "cache_creation_input_tokens": 1153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1153
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

_source line 15 · 2026-05-10T08:25:25.694Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XgajTrByRZRkM2qZFD11Ed`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.19217",
  "prompt": "Extract the full abstract and method overview. What does this paper propose for URIEL+ distance calibration? Does it use hyperbolic embeddings, latent variable models, speaker-weighted geographic distributions? What is the main contribution relative to standard URIEL+ cosine distance? What downstream tasks does it evaluate on?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fbbc9c8-a691-45a3-a07a-81c2fa5bf7c6",
  "isSidechain": false,
  "requestId": "req_011CatZwAhbo8qepWGwwJPUA",
  "type": "assistant",
  "uuid": "1e32d6f8-fefc-4786-9279-1a288e602036",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SukfzY2NvfsRQTtGigKtyH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 30277,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 348,
          "cache_read_input_tokens": 30277,
          "cache_creation_input_tokens": 1153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1153
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

_source line 16 · 2026-05-10T08:25:29.566Z_

<details><summary>↩ Tool result · `toolu_01JSYs35nybFG8mWV3yvxpu9`</summary>

```text
# Analysis of "Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models"

## Full Abstract

"Large language models (LLMs) demonstrate remarkable ability in cross-lingual tasks. Understanding how LLMs acquire this ability is crucial for their interpretability. To quantify the cross-lingual ability of LLMs accurately, we propose a Word-Level Cross-Lingual Translation Task. To find how LLMs learn cross-lingual ability, we trace the outputs of LLMs' intermediate layers in the word translation task. We identify and distinguish two distinct behaviors in the forward pass of LLMs: co-occurrence behavior and semantic pivot behavior. We attribute LLMs' two distinct behaviors to the co-occurrence frequency of words and find the semantic pivot from the pre-training dataset. Finally, to apply our findings to improve the cross-lingual ability of LLMs, we reconstruct a semantic pivot-aware pre-training dataset using documents with a high proportion of semantic pivots."

## Key Findings from Available Content

**Typological Distance Approach:** No evidence in the provided page content indicates use of URIEL, lang2vec, or typological databases.

**Semantic Pivots Definition:** The abstract describes semantic pivots as phenomena identified in intermediate layer outputs of LLMs during word translation tasks. Rather than typological proximity, this appears to relate to how LLMs internally process cross-lingual relationships at different computational layers.

**Missing Information:** The page excerpt does not specify target languages, baseline comparisons, or curriculum learning strategies. These details would require accessing the full paper PDF or HTML version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fbbc9c8-a691-45a3-a07a-81c2fa5bf7c6",
  "isSidechain": false,
  "promptId": "93ff0712-c390-41e4-8983-1f0a5d6df198",
  "type": "user",
  "uuid": "6e47bc37-2486-4811-af8a-d3a1ddf67155",
  "toolUseResult": {
    "bytes": 45925,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of \"Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models\"\n\n## Full Abstract\n\n\"Large language models (LLMs) demonstrate remarkable ability in cross-lingual tasks. Understanding how LLMs acquire this ability is crucial for their interpretability. To quantify the cross-lingual ability of LLMs accurately, we propose a Word-Level Cross-Lingual Translation Task. To find how LLMs learn cross-lingual ability, we trace the outputs of LLMs' intermediate layers in the word translation task. We identify and distinguish two distinct behaviors in the forward pass of LLMs: co-occurrence behavior and semantic pivot behavior. We attribute LLMs' two distinct behaviors to the co-occurrence frequency of words and find the semantic pivot from the pre-training dataset. Finally, to apply our findings to improve the cross-lingual ability of LLMs, we reconstruct a semantic pivot-aware pre-training dataset using documents with a high proportion of semantic pivots.\"\n\n## Key Findings from Available Content\n\n**Typological Distance Approach:** No evidence in the provided page content indicates use of URIEL, lang2vec, or typological databases.\n\n**Semantic Pivots Definition:** The abstract describes semantic pivots as phenomena identified in intermediate layer outputs of LLMs during word translation tasks. Rather than typological proximity, this appears to relate to how LLMs internally process cross-lingual relationships at different computational layers.\n\n**Missing Information:** The page excerpt does not specify target languages, baseline comparisons, or curriculum learning strategies. These details would require accessing the full paper PDF or HTML version.",
    "durationMs": 5205,
    "url": "https://arxiv.org/abs/2505.16385"
  },
  "sourceToolAssistantUUID": "1fbbc9c8-a691-45a3-a07a-81c2fa5bf7c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T08:25:30.393Z_

<details><summary>↩ Tool result · `toolu_01XgajTrByRZRkM2qZFD11Ed`</summary>

```text
# Paper Summary: URIEL+ Distance Calibration

## Full Abstract
The paper addresses limitations in URIEL+ by proposing "type-matched language distances" with structure-aware representations for each distance category. It introduces speaker-weighted distributions for geography, hyperbolic embeddings for genealogy, and latent variable modeling for typology, unified into a composite distance metric. The authors demonstrate improvements in zero-shot transfer benchmarks where distance relevance aligns with task requirements.

## Key Methodological Innovations

The paper proposes three novel components:

1. **Geographic Distance**: "speaker-weighted distributions for geography"
2. **Genealogical Distance**: Hyperbolic embeddings (as stated)
3. **Typological Distance**: A latent variables model (as stated)

## Primary Contribution

Rather than URIEL+'s uniform vector representations, this work develops task-aware distance calibration. The abstract indicates the main advance is moving beyond "one-size-fits-all vector representations" toward modality-specific approaches with a "robust, task-agnostic composite distance."

## Evaluation Scope

The paper evaluates on "multiple zero-shot transfer benchmarks," though specific task names aren't detailed in the provided content. The authors note improvements "when the distance type is relevant to the task" and gains "in most tasks" using the composite distance metric.

**Publication**: Accepted to EACL 2026 Student Research Workshop
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e32d6f8-fefc-4786-9279-1a288e602036",
  "isSidechain": false,
  "promptId": "93ff0712-c390-41e4-8983-1f0a5d6df198",
  "type": "user",
  "uuid": "8ec44b91-7313-478e-b5f5-d6c5f4888729",
  "toolUseResult": {
    "bytes": 46987,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: URIEL+ Distance Calibration\n\n## Full Abstract\nThe paper addresses limitations in URIEL+ by proposing \"type-matched language distances\" with structure-aware representations for each distance category. It introduces speaker-weighted distributions for geography, hyperbolic embeddings for genealogy, and latent variable modeling for typology, unified into a composite distance metric. The authors demonstrate improvements in zero-shot transfer benchmarks where distance relevance aligns with task requirements.\n\n## Key Methodological Innovations\n\nThe paper proposes three novel components:\n\n1. **Geographic Distance**: \"speaker-weighted distributions for geography\"\n2. **Genealogical Distance**: Hyperbolic embeddings (as stated)\n3. **Typological Distance**: A latent variables model (as stated)\n\n## Primary Contribution\n\nRather than URIEL+'s uniform vector representations, this work develops task-aware distance calibration. The abstract indicates the main advance is moving beyond \"one-size-fits-all vector representations\" toward modality-specific approaches with a \"robust, task-agnostic composite distance.\"\n\n## Evaluation Scope\n\nThe paper evaluates on \"multiple zero-shot transfer benchmarks,\" though specific task names aren't detailed in the provided content. The authors note improvements \"when the distance type is relevant to the task\" and gains \"in most tasks\" using the composite distance metric.\n\n**Publication**: Accepted to EACL 2026 Student Research Workshop",
    "durationMs": 4695,
    "url": "https://arxiv.org/abs/2510.19217"
  },
  "sourceToolAssistantUUID": "1e32d6f8-fefc-4786-9279-1a288e602036",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T08:26:40.368Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have good information on both papers:

**arXiv:2505.16385 ("Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models"):**
- This paper is about understanding/interpretability of how LLMs develop cross-lingual ability
- "Semantic pivots" refers to internal LLM behaviors observed in intermediate layer outputs during word translation tasks — it's about co-occurrence behavior vs. semantic pivot behavior in the forward pass
- They reconstruct a pre-training dataset using documents with high proportion of semantic pivots
- No typological distance, no URIEL, no curriculum ordering over multiple source languages


- This is orthogonal to TWMP — it's an interpretability and pre-training data curation paper, not an instruction tuning method

**arXiv:2510.19217 ("Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+"):**
- Accepted to EACL 2026 Student Research Workshop rather than the main conference
- Proposes structure-aware URIEL+ representations using speaker-weighted distributions for geography, hyperbolic embeddings for genealogy, and latent variable models for typology, unified into a composite distance metric
- Evaluates on zero-shot transfer benchmarks
- This is actually adjacent work worth acknowledging since TWMP relies on standard URIEL+ cosine distances with SoftImpute, so the methodological overlap warrants a brief mention of how their approach differs from ours.

For the arXiv:2510.19217 paper accepted to EACL 2026 Student Research Workshop, I should clarify that it proposes structure-aware URIEL+ calibration through hyperbolic genealogy embeddings and latent typology models, whereas TWMP simply uses the standard cosine distances with SoftImpute for the qualifying Aya pivot languages—a simpler but sufficient approach.

The reviewer's signal is clear: these are the final two minor issues blocking acceptance, and Round 10 will be the decision point. I shouldn't overhaul the paper or second-guess the core idea—the fundamental approach is sound, and the stagnation likely stems from accumulated small issues rather than conceptual problems. These are writing-only fixes, so I'll keep the changes minimal and focused.

Now I'm integrating both papers into the JSON: adding a dismissal of arXiv:2505.16385 in the landscape section as concurrent work, placing arXiv:2510.19217 in the approach section's URIEL+ paragraph alongside the existing citation, and updating the key references list.

Updating the JSON structure... Now I'm inserting the new arXiv:2510.19217 reference into the approach section right after the LREC 2026 extension mention, describing how it proposes structure-aware calibration methods while noting that TWMP uses the standard COLING 2025 version with SoftImpute instead. I'll also add both papers to the key references and update the description field with the relevant details.

For arXiv:2505.16385, I've checked the abstract and it focuses on semantic pivot behavior within LLM intermediate layers during word translation—completely separate from typological distance-based curriculum ordering, so a brief one-sentence dismissal in Section 2 is appropriate rather than treating it as concurrent work.

For arXiv:2510.19217, the reviewer wants me to acknowledge it uses structure-aware URIEL+ calibration with hyperbolic genealogy embeddings, but note that TWMP's standard URIEL+ cosine distances with SoftImpute are sufficient for the Aya languages we're working with. I should also mention it was accepted to EACL 2026 Student Research Workshop.

Now I'm integrating these into the landscape section, placing the arXiv:2505.16385 dismissal near the other concurrent works discussion and adding the arXiv:2510.19217 comparison where URIEL+ is mentioned. I'm organizing where to insert these two new papers into the JSON structure. The first one about semantic pivots goes into the landscape section after the DCO discussion, and the second about URIEL+ calibration goes into the approach section after the existing arXiv reference. I need to be precise about placement and then add both to the key_references list. I'm scanning through the landscape section to find where arXiv:2505.16385 fits best—it looks like it should go near the concurrent works on cross-lingual transfer, probably after the TTC discussion since they're both analyzing similar phenomena around the same time. I'm drafting a sentence that positions this work alongside those theoretical frameworks, focusing on how it traces cross-lingual abilities through intermediate layer behavior. "'Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models' (arXiv:2505.16385, May 2026) traces how LLMs leverage co-occurrence patterns from pre-training to enable cross-lingual transfer, proposing dataset curation strategies; it's fundamentally about interpretability at the pre-training stage and doesn't engage with typological distance, curriculum ordering, or instruction tuning—completely separate from TWMP's approach."

For the URIEL+ section, I'm noting that TWMP relies on the standard COLING 2025 base version with SoftImpute and the Laplacian-selected feature subset, which provides adequate coverage for the Aya pivot languages, while acknowledging that the concurrent arXiv:2510.19217 work on speaker-weighted geographic calibration and hyperbolic genealogy embeddings represents a promising direction for future refinement.

Now I need to carefully structure the JSON updates—adding the dismissal of arXiv:2505.16385 to the landscape section after the TTC paragraph, inserting arXiv:2510.19217 into the approach field following the arXiv:2510.27183 discussion, updating the description with relevant mentions, and adding the two new references in their proper positions within key_references.

Assembling the complete JSON response... Now I'm crafting the specific sentences to integrate these two papers. For the first one, I need a dismissal that explains why it's orthogonal—it focuses on semantic pivots in pre-training and dataset curation without touching typological distance or curriculum ordering. For the second, I'm acknowledging a concurrent study that proposes URIEL+ calibration with geographic and genealogical embeddings. Then I'll add both to the key references section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ec44b91-7313-478e-b5f5-d6c5f4888729",
  "isSidechain": false,
  "requestId": "req_011CatZx4SM8kas1TdZ5MqUE",
  "type": "assistant",
  "uuid": "b9754997-cd67-4b2f-add7-7b342b15a0ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MLD5orCoXF9ggaxqH8kq9H",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1075,
      "cache_read_input_tokens": 31430,
      "output_tokens": 16505,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16505,
          "cache_read_input_tokens": 31430,
          "cache_creation_input_tokens": 1075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1075
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

_source line 19 · 2026-05-10T08:31:22.914Z_

Both papers are now clear. Key findings:

- **arXiv:2505.16385** is an interpretability/pre-training curation paper. "Semantic pivots" = co-occurrence behaviors in LLM intermediate layers during word translation — nothing to do with typological distance, URIEL, or curriculum ordering. One-sentence dismissal suffices.
- **arXiv:2510.19217** (EACL 2026 Student Research Workshop) proposes speaker-weighted geography, hyperbolic genealogy embeddings, and latent typology models for URIEL+ distance calibration — directly adjacent to TWMP's distance weighting step, worth a one-sentence acknowledgment.

Both are writing-only additions. This is correctly a `minor` change — the reviewer is signaling the idea is ready to pass with these two fixes. Pivoting now would be counterproductive.

```json
{
  "title": "Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruction Tuning",
  "core_problem": "Cross-lingual instruction tuning for low-resource languages defaults to English as the sole pivot, creating systematic gaps for languages that are typologically distant from English—particularly those with agglutinative morphology, non-Latin scripts, or SOV word order. Three peer-reviewed ACL 2025 benchmarks—KazMMLU (Kazakh), MiLiC-Eval (Tibetan, Uyghur, Kazakh, Mongolian), and TUMLU (Turkic languages including Kazakh and Uyghur)—confirm that even frontier multilingual LLMs (GPT-4, Llama-3.1, Qwen-2.5) achieve near-random performance on Mongolian comprehension tasks and substantially below-par accuracy on Kazakh and Uyghur relative to typologically proximate high-resource languages. No existing instruction tuning method uses typological distance to continuously weight data-source selection across a multi-pivot mixture for these under-represented language families.",
  "opportunity": "Three complementary ACL 2025 benchmarks provide peer-reviewed grounding for the performance gap. KazMMLU (arXiv:2502.12829; ACL 2025 long paper) comprises 23K questions total (approximately 11K in Kazakh, 12K in Russian) spanning STEM, humanities, and social sciences sourced from authentic Kazakhstani educational materials; for TWMP's Kazakh instruction evaluation, only the Kazakh-language subset (~11K questions) is relevant; evaluation of Llama-3.1, Qwen-2.5, GPT-4, and DeepSeek V3 shows 'substantial room for improvement' for all models on Kazakh, despite the language having 20 million speakers. MiLiC-Eval (arXiv:2503.01150; ACL 2025 Findings) covers Tibetan, Uyghur, Kazakh, and Mongolian across 9 tasks with 24K instances; GPT-4o-mini achieves only slightly above random on Mongolian tasks, and models exhibit only 'preliminary understanding' of Tibetan and Kazakh. TUMLU (arXiv:2502.11020; ACL 2025 long paper) provides 38K native questions spanning 11 academic subjects across Turkic languages including Kazakh and Uyghur, enabling controlled within-family comparisons that isolate the effect of lower training corpus size. The XLM-SWCM paper (arXiv:2502.10852) additionally shows that encoder-based shared-weight cross-lingual pretraining partially bridges these gaps—Kazakh ROUGE-L summarization score of 5.6 is notably the lowest among the four minority languages studied—but this approach does not scale to instruction-following for decoder LLMs. CLO (arXiv:2505.14297; ACL 2025) shows that DPO-style cross-lingual preference optimization with only 3,200 samples outperforms standard SFT with 6,400 samples, establishing strong data efficiency for cross-lingual transfer. 'Do Chinese Models Speak Chinese Languages?' (arXiv:2504.00289, April 2026) evaluates 10 LLMs across 21 language variants and finds that Llama3-Instruct is the only model showing distinctive Uyghur capability while most models reach only ~75% Mongolian identification accuracy; Chinese LLMs do not outperform Western counterparts on minority languages including Uyghur and Mongolian, confirming that the performance gap TWMP targets persists even in the most recent model generation. These findings together create a clear opening: by weighting instruction data from multiple source languages inversely by URIEL+ typological distance and introducing a staged curriculum, we can build a principled multi-pivot training regime that directly addresses the English-pivot bottleneck for agglutinative low-resource targets.",
  "landscape": "PLUG (ACL 2024) established that English-pivot cross-lingual instruction generation improves multilingual instruction following—but its reported 29% improvement was measured on Chinese, Korean, Italian, and Spanish. Whether the English-pivot advantage holds for typologically distant agglutinative languages with non-Latin scripts (Kazakh, Mongolian, Uyghur) is an assumption that TWMP directly tests rather than takes for granted. CLO (arXiv:2505.14297; ACL 2025) improves data efficiency via DPO-style cross-lingual preference optimization using 6,400 OpenAssistant samples machine-translated by M2M100; it fixes English as the sole source language without varying source selection by typological distance. PROM [NAACL 2025, aclanthology.org/2025.naacl-short.19/] (Pivoted and Regulated Optimization for Multilingual Instruction Learning) treats English as an internal pivot and disentangles English vs. target-language training objectives via separate regularized losses to reduce negative interference; like PLUG and CLO, PROM presupposes a single English pivot without addressing typological distance, multi-pivot source selection, or agglutinative low-resource targets such as Kazakh, Mongolian, and Uyghur. LangGPS [Ye et al., AAAI 2026, arXiv:2511.10229] selects multilingual instruction data based on language separability scores derived from the model's own representation space, demonstrating improvements across 22 languages including low-resource targets. Unlike LangGPS, TWMP uses external typological features from URIEL+ to derive a pivot ordering independent of training dynamics, and integrates a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer [arXiv:2603.27651, 2026; submitted to SIGIR 2026 Short Paper track] formulates multi-source cross-lingual transfer as a budget-constrained allocation problem for NER/sentiment tasks; TWMP's typological-distance weighting and staged curriculum provide a principled ordering mechanism for instruction tuning that Budget-Xfer does not address. Code-Switching Curriculum Learning [Yoo et al., ACL 2025 Findings, arXiv:2411.02460] proposes a 3-stage curriculum (token-level → sentence-level → monolingual code-switching) for a single language pair; TWMP's curriculum operates over a pool of typologically ordered pivot languages without code-switching and targets a set of related agglutinative languages rather than a single target. Revisiting Multilingual Data Mixtures [Foroutan et al., 2025, arXiv:2510.25947] studies reweighting across 25–400 languages at pretraining scale (1.1B–3B parameters); TWMP operates at instruction-tuning scale—10 epochs, LoRA, narrow near-family pivot pool—where the data volume, optimization dynamics, and gradient signal are qualitatively different from the pretraining regime. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh, English, Russian, and Turkish, and demonstrates that Turkish as an auxiliary language improves Kazakh performance—directly motivating TWMP's inclusion of Turkic pivots. Unlike Sherkala-Chat's Kazakh-specific full fine-tuning with ad-hoc four-language selection, TWMP provides a generalizable LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target language, with principled pivot selection replacing language-specific engineering. Laiyk et al. [ACL 2025 Long, arXiv:2502.13647] fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP does not require any target-language instruction labels and applies equally to Mongolian and Uyghur, where no comparable GPT-4-assisted dataset currently exists. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) annotates cross-lingual DPO pairs using implicit reward transfer from an English-aligned model, achieving a 12.72% average Win Rate improvement on X-AlpacaEval; it uses English as the sole source and implicit reward annotation without typological weighting—TWMP extends this direction to multi-pivot source selection weighted by typological distance and targets low-resource agglutinative languages absent from that work. 'Family Matters' (arXiv:2510.00810) applies language transfer and LoRA merging from typologically related Nordic languages to Faroese—demonstrating that typological proximity helps—but as a single-language case study with no generalizable training recipe. 'Cross-Linguistic Transfer in Multilingual NLP' (arXiv:2505.13908) analyzes language family and morphology effects empirically without proposing a training method. Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) decouples task and language LoRA adapters but does not use typological features to parameterize or weight the language adapter. 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678; Tianyu Liu et al., March 2026) introduces a DPO-inspired method—concurrent with TWMP—that enforces factual consistency of model responses across 26 languages and 9 LLMs; its preference pairs encode semantic equivalence of knowledge across languages (chosen = factually consistent cross-lingual response, rejected = factually inconsistent response). This objective is orthogonal to TWMP's: DCO addresses what the model says across languages (knowledge coherence), while TWMP addresses which language it responds in when given instructions in any of multiple pivot languages (instruction-language fidelity). DCO does not address low-resource instruction tuning, multi-pivot source selection, or typological-distance weighting. A concurrent theoretical framework 'Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family' (arXiv:2604.06202, April 2026) proposes the Turkic Transfer Coefficient (TTC), a composite typological similarity metric combining morphological, lexical, syntactic, and script compatibility for Turkic languages. Unlike TWMP, arXiv:2604.06202 is a theoretical analysis without training method, instruction tuning experiments, or evaluation on KazMMLU, MiLiC-Eval, or TUMLU; it corroborates the motivation for Turkic-pivot weighting but does not instantiate it empirically. 'Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models' (arXiv:2505.16385, May 2026) identifies 'semantic pivot' behaviors in LLM intermediate layers during word-level translation tasks and curates pre-training datasets to increase the proportion of such pivots; the paper addresses cross-lingual interpretability and pre-training data curation without using typological distance metrics, URIEL, curriculum ordering over pivot languages, or instruction tuning—entirely orthogonal to TWMP. Two works require careful differentiation from TWMP. First, TIPA (arXiv:2601.16629; EACL 2026 Findings) constructs proxy language adapters by aggregating existing MAD-X adapters weighted by typological similarity across 230+ languages—entirely without training. TIPA is orthogonal to TWMP in three key ways: (1) it is training-free inference-time adapter aggregation, whereas TWMP learns from a typologically-weighted data curriculum; (2) it operates on encoder-based MAD-X modules for classification tasks, whereas TWMP targets decoder LLM instruction tuning; (3) TIPA has not been applied to instruction generation or to languages not already represented by a dedicated adapter. Second, 'Linguistically-Informed Multilingual Instruction Tuning' (arXiv:2410.07809) uses 289-dimensional legacy URIEL TYPO vectors with k-means clustering to select 14 discrete representative languages from a 52-language pool (one per cluster) for LoRA fine-tuning on Bactrian-X, showing that typologically diverse selection beats random selection. TWMP differs substantially: rather than discrete cluster-representative selection, TWMP applies continuous inverse-distance sampling weights over the full Aya collection using compact URIEL+ features (300-dim, Laplacian Score selected); it adds a staged cosine-distance curriculum schedule; it integrates a multi-source DPO preference optimization objective for language fidelity; and it directly targets Kazakh, Mongolian, and Uyghur—languages for which arXiv:2410.07809's evaluation suite (XNLI, XCOPA, XStoryCloze, XWinograd, PAWS-X) provides zero coverage. The combination of continuous URIEL+ weighting, staged curriculum, precisely formulated multi-source DPO loss, and evaluation on three ACL 2025 benchmarks covering the target languages constitutes a principled and differentiated advance.",
  "approach": "We propose Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, which replaces PLUG's single-English pivot with a principled mixture over multiple source languages drawn from the Aya collection (513M instances across 114 languages).\n\nAya pivot coverage is verified before training: Turkish (high-resource, multi-million instances), Kyrgyz (~4.1M instances in the Aya collection language split), Uzbek (confirmed present as an underrepresented language with meaningful coverage), and Azerbaijani all qualify as pivot sources. A minimum threshold of 5,000 Aya instances per pivot language is enforced; languages below this threshold are excluded from the mixture. All qualifying pivot languages and their instance counts are reported in an appendix table. Kazakh, Mongolian, and Uyghur serve exclusively as evaluation targets and are never included in the pivot mixture.\n\nTypological distances are computed using URIEL+ (arXiv:2409.18472, COLING 2025; available via the urielplus Python library at github.com/LeeLanguageLab/URIELPlus) rather than the legacy lang2vec 289-dimensional binary features. URIEL+ expands coverage to 4,366 languages with approximately 800 features (607 grammar features covering syntactic and morphological dimensions, plus 193 sound features), and applies SoftImpute for missing-value imputation—critical for reducing sparsity in Kazakh, Uzbek, and Kyrgyz, where legacy URIEL features are known to be sparse. URIEL+ explicitly represents Kazakh's multi-script properties (Cyrillic, Latin, and Arabic) via script vectors. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds script vectors and Glottolog genealogies to URIEL+, covering 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for the qualifying Aya pivot languages. A concurrent representation study (arXiv:2510.19217, EACL 2026 Student Research Workshop) proposes structure-aware URIEL+ calibration via speaker-weighted geographic distributions, hyperbolic genealogy embeddings, and latent typology models unified into a composite distance; TWMP uses the standard COLING 2025 URIEL+ cosine distances with SoftImpute, which suffice for the qualifying Aya pivot languages, and arXiv:2510.19217's calibration approach is noted as an avenue for future improvement. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), which demonstrates that a Laplacian Score 300-feature subset of URIEL+ achieves Spearman ρ=0.358 (p=0.061; measured against linguistic similarity distance alignment metric G_d, Table 1) versus ρ=0.260 for the full 800-feature set, and additionally yields +7.8% improvement on LangRank downstream cross-lingual NLP tasks, we apply this feature selection before computing cosine distances. The downstream task gains (+7.8% LangRank) provide the primary empirical justification for the feature selection step; the typological alignment improvement (p=0.061) is directionally consistent but borderline significant and should not be cited as standalone evidence. Data-sampling weights are assigned inversely proportional to these 300-feature URIEL+ cosine distances, so morphologically close pivots such as Turkish or Uzbek for Kazakh receive substantially higher weight than English.\n\nThe staged curriculum uses three phases calibrated by the empirical URIEL+ distance distribution of qualifying Aya pivot languages relative to each target language. Let D_25 and D_60 denote the 25th and 60th percentile distances from the target language to all qualifying Aya pivots (computed once, before training). Stage 1 (epochs 1–3): exclusively sources with cosine distance < D_25—for Kazakh, approximately ≤0.32, capturing Turkish, Kyrgyz, Uzbek, and Azerbaijani. Stage 2 (epochs 4–6): sources with distance < D_60 (approximately ≤0.56 for Kazakh), expanding to Russian, Arabic, and other mid-distance languages. Stage 3 (epochs 7–10): full mixture over all qualifying pivot languages with continuous inverse-distance weights. Thresholds are target-specific and computed from the actual Aya-pivot distance distribution; for Mongolian, where no Turkic pivot falls within D_25, the closest available Aya sources (Korean, Finnish, Turkish) are used across all three stages with correspondingly small weights—this distance-constrained Mongolian setting is a controlled finding of interest. Ablations compare: no curriculum (full weighted mixture from epoch 1), 2-stage (merging Stages 1–2), 3-stage (proposed), and linear interpolation between stages.\n\nThe CLO-style DPO preference optimization objective is precisely extended to the multi-source setting. For each source pivot language s_i and target language t, preference pairs are defined as: chosen = (x_{s_i}, y^w_t)—an instruction in source language s_i paired with a model-generated response identified as being in the target language t; rejected = (x_{s_i}, y^l_{s_i})—the same instruction paired with a model-generated response in source language s_i. This formulation promotes target-language responses to source-language instructions and differs from CLO's English-source objective in a critical respect: CLO's English-input pair (chosen=English response, rejected=target-language response) is designed to preserve English capability by penalizing cross-lingual output for English inputs. TWMP inverts this preference because the training goal is acquisition of cross-lingual target-language instruction following: for any source-language input, we want the model to respond in the target language. TWMP does not use CLO's second pair type (target-language input → prefer target-language response) because target-language training data is explicitly excluded.\n\nPreference pairs are constructed entirely without target-language labels via automatic language identification: given each source-language instruction x_{s_i}, we sample K=8 candidate responses from Qwen3.5-9B at temperature 0.7; apply fastText language identification (lid.176.bin) to each candidate; assign responses identified as the target language to the chosen pool and responses identified as the source language to the rejected pool; apply a minimum 20-token length gate to both pools to exclude degenerate or near-empty responses; pair the highest-scoring chosen (by fastText language ID confidence) with the lowest-scoring rejected per instruction. Instructions yielding no target-language candidates in K=8 samples after the length filter fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row in the DPO evaluation table compares fastText-only selection (no length gate) against length-gated selection (≥20 tokens) to quantify the quality impact of this filter; this also characterizes the frequency of degenerate responses per source-target pair. As a mandatory prerequisite check, we run a 500-instruction probe per source-target language pair on the base Qwen3.5-9B and verify that target-language responses (meeting the ≥20-token gate) appear in >5% of K=8 samples; any pivot language pair failing this check is excluded from DPO training (falling back to SFT-weighted sampling only) for that target language. This probe is reported as a characterization result: for close Turkic pivots (Turkish→Kazakh), we expect the frequency to exceed 5% given Qwen3.5-9B's broad multilingual coverage; for distant pivots (English→Mongolian), the check may filter some source languages, which is informative about which pivots can drive DPO-based cross-lingual preference learning.\n\nWe apply QLoRA fine-tuning of Qwen3.5-9B (released March 2026; 248K-token vocabulary spanning 201 languages; the Qwen3.5 small series has 0.8B/2B/4B/9B variants—no 7B exists) on this weighted multi-pivot dataset, targeting Kazakh, Mongolian, and Uyghur as primary evaluation cases. Evaluation uses three ACL 2025 benchmarks: KazMMLU for Kazakh (Kazakh-language subset, ~11K questions), MiLiC-Eval for all three targets across 9 tasks, and TUMLU for Kazakh and Uyghur within a controlled within-Turkic-family comparison. PLUG, PROM [NAACL 2025], and CLO serve as primary English-pivot baselines. Typological weighting ablations compare: full 800-feature URIEL+ vs. Laplacian-selected 300 features vs. syntax-only (474 features) vs. morphology-only (133 features) vs. the k-means discrete selection baseline from arXiv:2410.07809. Swahili serves as a held-out agglutinative generalization target not used during hyperparameter design. Note: TyDi QA covers Arabic, Bengali, Finnish, Indonesian, Japanese, Kiswahili, Korean, Russian, Telugu, and Thai—it does not include Kazakh, Mongolian, or Uyghur and is not used here.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200h A100 (15–20 QLoRA runs × 10–13h each on Qwen3.5-9B, covering 3 primary target languages, PLUG/CLO/PROM baselines, URIEL+ sub-space ablations, curriculum schedule variants, DPO quality gate ablation row, and DPO prerequisite probe runs)",
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
    "PROM: Pivoted and Regulated Optimization for Multilingual Instruction Learning (NAACL 2025, aclanthology.org/2025.naacl-short.19/) [treats English as an internal pivot and disentangles English vs. target-language training objectives via regulated losses to reduce negative interference; like PLUG and CLO, fixes English as the sole pivot without addressing typological distance, multi-pivot sequencing, or agglutinative low-resource targets—cited as an English-pivot baseline alongside PLUG and CLO]",
    "LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning (Ye et al., AAAI 2026, arXiv:2511.10229) [selects multilingual instruction data using language separability scores from the model's own representation space across 22 languages including low-resource targets; differentiated from TWMP's external URIEL+ typological weighting independent of training dynamics, staged curriculum, and multi-source DPO objective]",
    "Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages (Idris et al., arXiv:2603.27651, 2026; submitted to SIGIR 2026 Short Paper track) [multi-source cross-lingual transfer as budget-constrained resource allocation for NER and sentiment analysis on Hausa, Yoruba, and Swahili across 288 experiments; no typological features or curriculum ordering—differentiated from TWMP's URIEL+-weighted staged instruction tuning; note: preprint only, acceptance not yet confirmed]",
    "Code-Switching Curriculum Learning for Multilingual Transfer in LLMs (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) [3-stage curriculum (token-level → sentence-level → monolingual code-switching) for single language pair; primary focus Korean, with Japanese and Indonesian—differentiated from TWMP's multi-pivot typological curriculum without code-switching targeting a family of related agglutinative languages]",
    "Revisiting Multilingual Data Mixtures in Language Model Pretraining (Foroutan et al., arXiv:2510.25947, ICLR-submitted 2025) [multilingual data reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); differentiated from TWMP's instruction-tuning-scale LoRA curriculum where data volume, optimization dynamics, and gradient signal are qualitatively different]",
    "Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh (Laiyk et al., ACL 2025 Long, arXiv:2502.13647) [10,600 GPT-4o-assisted Kazakh instruction examples fine-tuning Qwen/Falcon/Gemma; requires target-language labels and is Kazakh-specific—differentiated from TWMP's label-free multi-target approach covering Mongolian and Uyghur equally]",
    "Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+ (Shipton et al., LREC 2026, arXiv:2510.27183) [extends URIEL+ with script vectors and Glottolog genealogies for 26,449 languages; TWMP uses the COLING 2025 base version (arXiv:2409.18472) with SoftImpute, which provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages]",
    "Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+ (arXiv:2510.19217, EACL 2026 Student Research Workshop) [proposes structure-aware URIEL+ calibration via speaker-weighted geographic distributions, hyperbolic genealogy embeddings, and latent typology models unified into a composite distance; TWMP uses standard COLING 2025 URIEL+ cosine distances with SoftImpute, which suffice for qualifying Aya pivot languages; arXiv:2510.19217's calibration approach is noted as an avenue for future improvement]",
    "Llama-3.1-Sherkala-8B-Chat (arXiv:2503.01493) [trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish; demonstrates Turkish as auxiliary language improves Kazakh performance via full fine-tuning; differentiated from TWMP's generalizable LoRA recipe parameterized by continuous URIEL+ distances]",
    "Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) [implicit reward transfer from English-aligned DPO model to annotate cross-lingual preference pairs; 12.72% Win Rate improvement on X-AlpacaEval; English-only source with no typological weighting—differentiated from TWMP's multi-pivot source selection and low-resource agglutinative targets]",
    "URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base (arXiv:2409.18472, COLING 2025) [~800-feature typological database covering 4,366 languages with SoftImpute for low-resource Turkic languages; replaces legacy lang2vec 289-dim URIEL in TWMP; official repository: github.com/LeeLanguageLab/URIELPlus]",
    "Less is More: The Effectiveness of Compact Typological Language Representations (arXiv:2509.20129, EMNLP 2025) [Laplacian Score 300-feature URIEL+ subset achieves ρ=0.358 (p=0.061; measured on linguistic distance alignment against G_d metric, Table 1) vs. ρ=0.260 for full 800-feature URIEL+; downstream improvement of +7.8% on LangRank tasks; ρ values verified from paper HTML; downstream gains provide the primary justification for TWMP's feature selection step—the typological alignment improvement is directionally consistent but borderline significant]",
    "Optimizing Language Models for Crosslingual Knowledge Consistency (arXiv:2603.04678; Tianyu Liu et al., March 2026) [concurrent DPO-inspired work targeting factual consistency across 26 languages and 9 LLMs—orthogonal to TWMP's language-fidelity DPO objective; differentiated in related work]",
    "Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models (arXiv:2505.16385, May 2026) [analyzes LLM cross-lingual ability by tracing intermediate-layer outputs in word-level translation tasks, where 'semantic pivots' denote co-occurrence-driven internal behaviors in pre-training data; proposes pre-training dataset curation—entirely orthogonal to TWMP's typological-distance-weighted instruction tuning curriculum; no use of typological distance metrics, URIEL, or curriculum ordering over pivot languages]",
    "TIPA: Typologically Informed Parameter Aggregation (arXiv:2601.16629, EACL 2026 Findings) [training-free encoder adapter aggregation across 230+ languages—differentiated from TWMP's training-time decoder curriculum]",
    "Linguistically-Informed Multilingual Instruction Tuning (arXiv:2410.07809) [discrete k-means language selection using legacy 289-dim URIEL TYPO features on BLOOM/mGPT/mT5—differentiated from TWMP's continuous URIEL+ weighting, staged curriculum, multi-source DPO, and Turkic/Mongolic targets]",
    "Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family (arXiv:2604.06202, April 2026) [theoretical framework introducing Turkic Transfer Coefficient (TTC) combining morphological, lexical, syntactic, and script compatibility; no training method or instruction tuning experiments; no evaluation on KazMMLU/MiLiC-Eval/TUMLU—corroborates motivation for Turkic-pivot weighting without instantiating it empirically]",
    "KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan (ACL 2025, arXiv:2502.12829) [primary Kazakh evaluation benchmark; 23K total questions (approximately 11K in Kazakh, 12K in Russian) sourced from authentic Kazakhstani educational materials; peer-reviewed; TWMP evaluates on the Kazakh-language subset only]",
    "MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages (ACL 2025 Findings, arXiv:2503.01150) [primary evaluation for Uyghur, Kazakh, Mongolian across 9 tasks]",
    "TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages (ACL 2025, arXiv:2502.11020) [38K questions for Kazakh, Uyghur, and other Turkic languages; within-family controlled comparison]",
    "Do Chinese Models Speak Chinese Languages? (arXiv:2504.00289, April 2026) [evaluates 10 LLMs across 21 language variants including Uyghur, Mongolian, Kazakh, and Tibetan; Llama3-Instruct is uniquely capable at Uyghur and ranks highest on Mongolian; Chinese LLMs do not outperform Western counterparts on minority languages—contemporary evidence for the performance gap TWMP addresses]",
    "Multilingual Encoder Knows more than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages (arXiv:2502.10852) [encoder-based cross-lingual transfer for Tibetan/Uyghur/Kazakh/Mongolian; motivation for decoder LLM gap]",
    "Family Matters: Language Transfer and Merging for Adapting Small LLMs to Faroese (arXiv:2510.00810, 2025)",
    "Cross-Linguistic Transfer in Multilingual NLP: The Role of Language Families and Morphology (arXiv:2505.13908, 2025)",
    "Multi-Linguistic LoRA Merging (NeurIPS 2025 ER Workshop) [workshop paper, not main conference]",
    "Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models (arXiv:2603.21036, 2026) [supplementary qualitative observation; single-author preprint with 50 hand-crafted questions—not primary motivation anchor]"
  ],
  "description": "This paper introduces Typologically-Weighted Multi-Pivot (TWMP) instruction tuning, a method for adapting decoder LLMs to low-resource languages that are typologically distant from English. Rather than using a single English pivot as in PLUG, we compute typological distances using URIEL+ (arXiv:2409.18472, COLING 2025; urielplus Python library at github.com/LeeLanguageLab/URIELPlus), which covers ~800 features across 4,366 languages with SoftImpute imputation—critical for low-resource Turkic languages where legacy lang2vec 289-dim URIEL is known to be sparse. A concurrent LREC 2026 extension (Shipton et al., arXiv:2510.27183) adds Glottolog genealogies covering 26,449 languages; TWMP uses the COLING 2025 base version, which already provides sufficient feature coverage and Laplacian-selected 300-feature subset for qualifying Aya pivot languages. A concurrent representation study (arXiv:2510.19217, EACL 2026 Student Research Workshop) proposes structure-aware URIEL+ calibration via speaker-weighted geographic distributions, hyperbolic genealogy embeddings, and latent typology models unified into a composite distance; TWMP uses the standard COLING 2025 URIEL+ cosine distances with SoftImpute, which suffice for the qualifying Aya pivot languages, and arXiv:2510.19217's calibration approach is noted as an avenue for future improvement. Following 'Less is More' (arXiv:2509.20129, EMNLP 2025), we apply Laplacian Score feature selection to reduce URIEL+ to 300 compact features (Spearman ρ=0.358, p=0.061, measured on linguistic distance alignment with G_d metric, Table 1; +7.8% improvement on LangRank downstream tasks; vs. ρ=0.260 for the full 800-feature set; ρ values verified from paper HTML—the downstream gains are the primary justification, as the typological alignment improvement is directionally consistent but borderline significant) before computing cosine distances and assigning inverse-distance sampling weights over the Aya collection. Aya pivot coverage is verified: Turkish (multi-million instances), Kyrgyz (~4.1M instances), and Uzbek all clear a 5,000-instance minimum threshold; Kazakh, Mongolian, and Uyghur are evaluation-only targets excluded from the pivot pool. Contemporary evidence from 'Do Chinese Models Speak Chinese Languages?' (arXiv:2504.00289, April 2026), which evaluates 10 LLMs across 21 language variants, shows that Llama3-Instruct is the only evaluated model with distinctive Uyghur capability and that Chinese LLMs do not outperform Western counterparts on minority languages including Uyghur and Mongolian—confirming that no current model family addresses the performance gap TWMP targets. LangGPS (Ye et al., AAAI 2026, arXiv:2511.10229) selects multilingual instruction data by language separability from the model's own representation space across 22 languages; TWMP instead uses external URIEL+ features independent of training dynamics, with a staged curriculum and multi-source DPO objective that LangGPS does not address. Budget-Xfer (Idris et al., arXiv:2603.27651, 2026; submitted to SIGIR 2026 Short Paper track) frames multi-source transfer as budget-constrained allocation for NER/sentiment tasks without typological features or curriculum ordering—TWMP's principled weighting and staged scheduling address instruction tuning specifically. 'Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models' (arXiv:2505.16385, May 2026) identifies 'semantic pivot' behaviors in LLM intermediate layers during word-level translation tasks and curates pre-training datasets accordingly; this work addresses cross-lingual interpretability and pre-training data curation without using typological distance metrics, URIEL, or curriculum ordering over pivot languages—entirely orthogonal to TWMP. A staged 3-phase curriculum progressively introduces more distant pivots using percentile thresholds computed from the empirical URIEL+ distance distribution of qualifying Aya pivots per target: Stage 1 (epochs 1–3) uses sources within the 25th percentile distance threshold (~≤0.32 for Kazakh, capturing Turkish/Kyrgyz/Uzbek/Azerbaijani); Stage 2 (epochs 4–6) expands to the 60th percentile (~≤0.56); Stage 3 (epochs 7–10) uses the full weighted mixture. Code-Switching Curriculum Learning (Yoo et al., ACL 2025 Findings, arXiv:2411.02460) proposes a 3-stage code-switching curriculum for a single language pair; TWMP's curriculum spans a typologically ordered pool of pivot languages without code-switching. The DPO preference optimization objective is precisely formulated for the multi-source case: for source pivot s_i and target t, chosen = (instruction in s_i, model-generated response in t); rejected = (instruction in s_i, model-generated response in s_i). This inverts CLO's English-input pair direction—CLO prefers English responses to English inputs (preserving English capability), while TWMP prefers target-language responses to any source-language input (promoting cross-lingual instruction following). PROM [NAACL 2025] similarly treats English as an internal pivot and disentangles English and target-language training objectives via regulated losses; like PLUG and CLO, PROM fixes a single English pivot without addressing typological distance or multi-pivot sequencing for agglutinative targets—all three serve as English-pivot baselines in TWMP's evaluation. Pairs are auto-constructed by sampling K=8 responses per instruction from Qwen3.5-9B, applying fastText language identification, and applying a minimum 20-token length gate to both chosen and rejected pools to exclude degenerate responses; no target-language training labels are required. Instructions yielding no target-language candidates post-gate fall back to the SFT-weighted sampling objective for that instruction; the per-source-target fallback rate (fraction of instructions with empty post-gate chosen pools) is reported as a characterization result alongside the prerequisite probe. An ablation row compares fastText-only selection against length-gated selection to quantify the quality impact of this filter. A mandatory 500-instruction prerequisite probe verifies >5% target-language response frequency (post-length-gate) per source-target pair; pairs failing this check fall back to SFT-only. Sherkala-Chat (arXiv:2503.01493) trains Llama-3.1-8B on 45.3B tokens of Kazakh+English+Russian+Turkish and demonstrates the value of Turkish as an auxiliary language for Kazakh via full fine-tuning, motivating TWMP's Turkic pivot inclusion; TWMP generalizes this insight into a principled LoRA-based recipe parameterized by continuous URIEL+ distances applicable to any agglutinative target. Laiyk et al. (ACL 2025 Long, arXiv:2502.13647) fine-tune on 10,600 GPT-4o-assisted Kazakh instruction examples; TWMP requires no target-language labels and applies equally to Mongolian and Uyghur where no comparable dataset exists. Revisiting Multilingual Data Mixtures (Foroutan et al., arXiv:2510.25947) studies reweighting at pretraining scale (1.1B–3B parameters, 25–400 languages); TWMP targets instruction-tuning scale where data volume, optimization dynamics, and gradient signal are qualitatively different. Implicit Cross-Lingual Rewarding (arXiv:2503.04647; ACL 2025 Findings) uses implicit reward transfer from English-aligned models to annotate cross-lingual DPO pairs (12.72% Win Rate on X-AlpacaEval); TWMP extends this direction to multi-pivot source selection weighted by typological distance targeting low-resource agglutinative languages absent from that work. Concurrent work 'Optimizing Language Models for Crosslingual Knowledge Consistency' (arXiv:2603.04678, March 2026) uses DPO for factual consistency across 26 languages—orthogonal in objective (knowledge coherence vs. language fidelity) and not addressing low-resource instruction tuning. A concurrent theoretical framework (arXiv:2604.06202, April 2026) proposes the Turkic Transfer Coefficient (TTC) for cross-lingual adaptation within the Turkic family but offers no training method or instruction tuning experiments. Two directly adjacent works are carefully differentiated: TIPA (EACL 2026) aggregates MAD-X encoder adapters at inference time without training; arXiv:2410.07809 uses k-means on legacy 289-dim URIEL for discrete language selection on BLOOM/mGPT with zero Kazakh/Mongolian/Uyghur coverage. We fine-tune Qwen3.5-9B with QLoRA (released March 2026; 248K-token vocabulary, 201 languages; 0.8B/2B/4B/9B series—no 7B variant), targeting Kazakh, Mongolian, and Uyghur, evaluated on KazMMLU (Kazakh-language subset, ~11K questions), MiLiC-Eval, and TUMLU (all ACL 2025). Ablations cover full URIEL+ vs. Laplacian-300 vs. syntax-only vs. morphology-only vs. k-means discrete baseline; curriculum variants; DPO quality gate (fastText-only vs. length-gated); DPO vs. SFT-only. Swahili is the held-out agglutinative generalization target. Manual mode (200 A100h ≈ 120 H100h) and human-in-loop mode (310 A100h ≈ 186 H100h) stay within the ≤200 H100-hour budget; auto_research mode (600 A100h ≈ 360 H100h) exceeds the constraint and is not viable within budget. ACL 2027 (ARR August 3, 2026) is the primary target venue.",
  "project_name": "typological_multi_pivot",
  "source": "web_research",
  "change_type": "minor"
}
```

---

**What changed and why:**

**arXiv:2505.16385** — Verified via abstract fetch: "semantic pivots" in this paper are intermediate-layer co-occurrence behaviors during *word translation*, not typological language proximity. The paper proposes pre-training data curation with no URIEL, no curriculum, no instruction tuning. One-sentence dismissal added to `landscape`, `description`, and `key_references`.

**arXiv:2510.19217** — Verified: EACL 2026 Student Research Workshop paper proposing hyperbolic genealogy embeddings + latent typology models + speaker-weighted geography for URIEL+ distance calibration. One sentence added to the URIEL+ paragraph in `approach` and `description`, noting TWMP uses standard COLING 2025 cosine distances (sufficient for qualifying pivots) and flagging arXiv:2510.19217 as a future improvement avenue. Added to `key_references`.

No new experiments required; no framing changes needed. The reviewer's signal that Round 10 is pass/fail makes a pivot unjustified — the idea is structurally sound and these are the last two open items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9754997-cd67-4b2f-add7-7b342b15a0ad",
  "isSidechain": false,
  "requestId": "req_011CatZx4SM8kas1TdZ5MqUE",
  "type": "assistant",
  "uuid": "9ce8521a-ad79-4e9c-8a91-ab4e87f17865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MLD5orCoXF9ggaxqH8kq9H",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1075,
      "cache_read_input_tokens": 31430,
      "output_tokens": 16505,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16505,
          "cache_read_input_tokens": 31430,
          "cache_creation_input_tokens": 1075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1075
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruc…",
  "leafUuid": "9ce8521a-ad79-4e9c-8a91-ab4e87f17865",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise TWMP for ACL 2027 to address concurrent pivot methods and URIEL+ calibration",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Typologically-Weighted Multi-Pivot Curriculum for Low-Resource Instruc…",
  "leafUuid": "9ce8521a-ad79-4e9c-8a91-ab4e87f17865",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise TWMP for ACL 2027 to address concurrent pivot methods and URIEL+ calibration",
  "sessionId": "6d7de733-2eec-460b-a21c-5e6b1efdf935"
}
```

---
