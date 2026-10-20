# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Entity-Anchored Contrastive Align

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/e7d63c9f-d9c2-416a-905a-2b7021ac9422.jsonl`
- **Structured JSON:** [`dad19ae11db8987338a9.json`](../../sessions/da/dad19ae11db8987338a9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:52:01.174Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:52:01.174Z",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Entity-Anchored Contrastive Alignment for Cross-Lingual Knowledge Conductivity\n\n## Description\nEACA is a continued pretraining method that introduces InfoNCE contrastive loss on entity-span hidden states alongside standard next-token prediction, targeting entity-level cross-lingual knowledge conductivity — a capability that CLiKA (NAACL 2024) established is not substantially improved by existing multilingual pretraining or instruction tuning (XRR < 0.01). Unlike CCL-XCoT (sentence/paragraph-level contrastive CPT) and Liu & Niehues (ACL 2025, sentence-level middle-layer contrastive fine-tuning), EACA anchors contrastive pairs to Wikidata QIDs using FactNet's 1.7B entity-grounded atomic facts, operating at the entity level — the granularity empirically shown to be the bottleneck for cross-lingual consistency (entity alignment correlates at r > 0.7 with consistency, arXiv:2510.10280). This extends KBioXLM's (EMNLP Findings 2023) precedent of multi-granularity entity alignment in multilingual pretraining from encoder-based masking objectives in a specialized domain to explicit contrastive alignment in decoder-only LLMs for general-domain conductivity. Entity spans are marked with LEIA-style [ENT]/[/ENT] tokens using DaMuEL (12.3B QID-annotated tokens across 53 languages) as the primary annotation source for 10 of 13 target languages, supplemented by a Wikipedia wikilinks-to-QID extraction pipeline for the 3 uncovered Tier 3 languages (SW/YO/KM) and mReFinED entity linking for non-hyperlinked mention gap-filling, with 1.5-2 weeks budgeted for preprocessing. Representations are extracted via mean-pooling at middle layers (~layer 16, validated via Phase 0 sweep). The proposal explicitly addresses the script barrier identified by Ifergan et al. (NAACL Findings 2025) and Bandarkar et al. (arXiv:2603.17070): script similarity dominates representation sharing (~37.6% same-script CKR vs. <10-20% cross-script), but entity priming disproportionately helps cross-script transfer, motivating entity-level alignment as targeting the right bottleneck. Cross-script QID pairs receive transliteration-augmented entity markers (e.g., [ENT]北京 (Beijing)[/ENT]), inspired by TransliCo (ACL 2024), with mandatory script-grouped evaluation (same-script vs. cross-script gains). Stratified batch construction uses 128-256 entities per batch with class-aware false-negative masking, type-aware hard negatives (~50% same-type entities via Wikidata P31 properties, following Robinson et al. ICLR 2021), and asymmetric positive sets for entities with uneven language coverage (K_min = 3 languages per QID). Joint optimization (L_NTP + λ·L_contrastive, λ=0.1 with warmup) includes gradient conflict monitoring: cosine similarity between NTP and contrastive gradients is tracked every 100 steps, with PCGrad (Yu et al., NeurIPS 2020) activated if conflicts exceed 30% of steps, and GradNorm (Chen et al., ICML 2018) for dynamic λ adjustment if gradient magnitudes diverge beyond 10:1. Inverse-frequency weighting prioritizes low-resource entity-facts. Catastrophic forgetting is mitigated through LoRA (rank 64) on middle layers (10-22), 15% general-domain replay, and cosine LR scheduling. A tiered language selection spans 13 languages across ~7 scripts: Tier 1 (EN/ZH/JA/DE), Tier 2 (AR/HI/TR/ID/VI/TH), Tier 3 (SW/YO/KM), with mandatory Phase 0 FactNet coverage audit and contingency replacements. Phase 0 pilot (500M tokens, 5 languages spanning ≥3 scripts, ~130 H100 hours) includes baselines against sentence-level contrastive (CCL-XCoT), middle-layer sentence contrastive (Liu & Niehues), masking-based entity alignment (KBioXLM-style adaptation), LEIA augmentation, and standard CPT, plus layer sweep, gradient analysis, and script-grouped evaluation. Six key novelties: (1) entity-level contrastive anchoring vs. sentence-level, (2) structured knowledge grounding via FactNet QIDs vs. parallel text, (3) frequency-aware weighting, (4) joint NTP+contrastive optimization with gradient conflict monitoring at entity level during CPT, (5) script-aware transliteration augmentation for cross-script entity alignment, (6) direct targeting of CLiKA's conductivity gap with script-stratified evaluation.\n\n## Core Problem\nCan entity-level contrastive alignment — anchored to Wikidata QIDs and grounded in FactNet's structured atomic facts — improve cross-lingual knowledge conductivity (as defined by CLiKA's XRR metric, Gao et al. NAACL 2024) more effectively than sentence/paragraph-level contrastive continued pretraining (e.g., CCL-XCoT) or sentence-level middle-layer alignment (Liu & Niehues, ACL 2025)? CLiKA established that neither multilingual pretraining nor instruction tuning substantially improves conductivity, with XRR scores below 0.01 for most non-English languages. EACA hypothesizes that this conductivity barrier persists because prior methods align at sentence/document granularity — conflating entity-specific factual knowledge with syntactic and discourse-level variation — whereas factual knowledge is inherently structured around entities (subject-property-object triples). A critical complication, identified by Ifergan et al. (NAACL Findings 2025) and Bandarkar et al. (arXiv:2603.17070), is that script similarity is the dominant factor in cross-lingual representation sharing: high behavioral consistency does not imply shared internal representation for cross-script language pairs, and script match — not language family — is the primary predictor of knowledge transfer failure. Crucially, however, Bandarkar et al.'s entity priming experiment shows that providing source-language entity names disproportionately improves cross-script transfer, directly implicating entity-level mapping failure as the mechanism behind the script barrier. This suggests that entity-level contrastive alignment targets the right bottleneck, but that cross-script entity alignment requires additional support (e.g., transliteration augmentation) beyond what same-script entity alignment needs. EACA therefore addresses a two-level problem: (1) entity-level alignment as the fundamental unit of factual knowledge transfer, and (2) script-aware strategies to bridge the representation gap across writing systems.\n\n## Opportunity\nCCL-XCoT (EMNLP 2025 Findings) demonstrates that contrastive continued pretraining reduces cross-lingual hallucination by up to 62% but operates at sentence/paragraph granularity with parallel text. Liu & Niehues (ACL 2025) show that middle-layer contrastive alignment (layer 16 of 32 in LLaMA-3-8B) significantly improves cross-lingual transfer for downstream tasks, but again at sentence-level granularity and for task-specific fine-tuning rather than factual consistency. CLiKA (NAACL 2024) reveals a critical gap: existing multilingual pretraining and instruction tuning improve surface-level consistency but fail to improve knowledge conductivity (XRR < 0.01), suggesting that fundamentally different alignment granularity is needed. Meanwhile, FactNet (arXiv:2602.03417, Feb 2026) provides 1.7B entity-grounded atomic facts across 316 Wikipedia editions with Wikidata QID linking — enabling entity-level contrastive pairs grounded in structured knowledge. Entity Lens (BlackboxNLP 2025) confirms that decoder LLMs develop entity-specific internal mechanisms to represent multi-token entities. Liu et al. (EMNLP 2025 Findings) show that cross-lingual transfer is frequency-driven, with low-frequency facts benefiting most. Critically, recent evidence from entity-level alignment analysis (Liu, Wang et al., arXiv:2510.10280) demonstrates that cross-lingual factual consistency correlates strongly with entity alignment (Pearson r > 0.7), with over 99% of consistent facts exhibiting successful entity alignment — providing direct empirical motivation for entity-level rather than sentence-level contrastive objectives. Marco et al. ('Unveiling LLMs', arXiv:2404.03623) further establish that factual knowledge about subject entities concentrates in middle layers (L5-L21 for LLaMA-2-7B). KBioXLM (EMNLP Findings 2023) provides an important precedent: it demonstrated that multi-granularity knowledge alignment (entity masking, relation masking, passage relation prediction) during continued pretraining of XLM-R yields +20 F1 points on cross-lingual zero-shot biomedical tasks, establishing entity-anchored alignment as effective — but using masking-based reconstruction on encoders rather than contrastive loss on decoder LLMs, and targeting downstream task transfer rather than factual conductivity. Ifergan et al. (NAACL Findings 2025) reveal a deeper challenge: using knowledge editing as a probe for representation sharing, they find script similarity is the dominant factor (same-script CKR ~37.6% in Mistral; cross-script <10-20%), and that behavioral consistency diverges sharply from representation sharing for cross-script pairs. Bandarkar et al. (arXiv:2603.17070, March 2026) confirm this with regression analysis showing script match as the primary predictor after controlling for model capability and question difficulty (~13% accuracy gap), but critically, their entity priming experiment shows that providing source-language entity names disproportionately improves cross-script questions — directly implicating entity mapping as the bottleneck. TransliCo (ACL 2024) demonstrates that transliteration-based contrastive learning bridges script barriers using only 5% of training data on encoders. DaMuEL (2023) provides 12.3B tokens with QID-linked entity annotations across 53 languages, enabling efficient preprocessing for 10 of EACA's 13 target languages. The opportunity is to combine these insights — entity-level anchoring + structured knowledge grounding + middle-layer extraction + inverse-frequency weighting + script-aware strategies — into a contrastive CPT method that targets the specific granularity (entities), representation layer (middle), data regime (low-frequency facts), and script barriers where current methods demonstrably fall short.\n\n## Related Work / Landscape\nThe cross-lingual factual consistency landscape spans several complementary approaches. CCL-XCoT (EMNLP 2025 Findings) is the primary baseline, employing InfoNCE symmetric contrastive loss during continued pretraining with a sentence-to-paragraph curriculum on Gemma-7B and LLaMA-3.1-8B using LoRA on layers 9-19/11-22, reducing hallucination by 62%, but operating at sentence/paragraph granularity without entity grounding or frequency weighting. Liu & Niehues (ACL 2025) represent the closest methodological precedent for contrastive alignment: they apply contrastive loss on mean-pooled sentence representations at middle layers (specifically layer 16 of 32 for LLaMA-3-8B-Instruct) during task-specific fine-tuning with LoRA (rank 8), demonstrating +1.5 F1 on slot filling and +1.5 BLEU on MT across 35 languages — however, they use sentence-level alignment with alternating (not joint) task/alignment training, target downstream task transfer rather than factual consistency, use parallel text rather than structured knowledge, and include no frequency weighting. EACA differentiates from Liu & Niehues on five axes: (1) entity-level rather than sentence-level granularity, (2) continued pretraining for factual consistency rather than task-specific fine-tuning, (3) FactNet-grounded contrastive pairs rather than parallel text, (4) joint NTP+contrastive objective rather than alternating training, and (5) inverse-frequency weighting for underrepresented facts. KBioXLM (Geng et al., EMNLP Findings 2023, arXiv:2311.11564) is an important precedent for multi-granularity entity-anchored alignment in multilingual pretraining. It performs continued pretraining on XLM-R using three alignment objectives grounded in UMLS biomedical knowledge: entity masking (code-switching entity mentions across EN-CN and predicting masked entity tokens via MLM cross-entropy), relation masking (masking relation tokens in subject-predicate-object triples), and passage relation prediction (3-way classification on aligned EN-CN Wikipedia passages). KBioXLM achieves +20 F1 points on cross-lingual zero-shot biomedical NER/RE. EACA extends this paradigm along four dimensions: (a) decoder-only LLMs vs. encoder (XLM-R), requiring contrastive loss on hidden states rather than masking-based reconstruction, since decoder LLMs lack bidirectional context for effective mask prediction; (b) general domain vs. biomedical, using FactNet's 1.7B facts across 316 editions vs. UMLS's specialized ontology; (c) explicit contrastive alignment (InfoNCE) vs. implicit alignment through masking, directly optimizing cross-lingual entity representation similarity rather than relying on the prediction bottleneck; (d) conductivity metric (CLiKA's XRR) vs. downstream task transfer, targeting the specific capability that prior methods fail to improve. CLiKA (Gao et al., NAACL 2024) provides the diagnostic framework: they define knowledge conductivity as the Cross-Retrieval Ratio (XRR) — retrieving knowledge learned in one language using another — and find that neither multilingual pretraining nor instruction tuning substantially improves XRR (scores < 0.01 for most non-English languages), with no concrete solutions proposed. The entity-level alignment analysis (Liu, Wang et al., arXiv:2510.10280) provides strong empirical support: cross-lingual consistency correlates with entity alignment at r > 0.7, and their SubInj method yields +14-32% recall and +17-44% consistency gains, but only at inference time; EACA aims to achieve this alignment at training time. On the script barrier dimension, Ifergan et al. ('Beneath the Surface of Consistency', NAACL Findings 2025, arXiv:2408.10646) demonstrate via knowledge editing probes on 7 decoder LLMs (7B scale) that script similarity is the dominant factor in cross-lingual knowledge representation sharing (CKR): same-script Latin pairs show ~37.6% average CKR in Mistral, while cross-script pairs show <10-20% transfer; crucially, they find that high behavioral consistency (CKC) does not imply shared representation for cross-script pairs, with E[NCL] consistently exceeding E[NTL]. Even targeted language extension pretraining achieves only marginal cross-script CKR improvement. Bandarkar et al. ('Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts', arXiv:2603.17070, March 2026) confirm via regression analysis on ECLeKTic and MultiLoKo that script match — not language family — is the primary predictor of knowledge transfer failure (~13% accuracy gap), but their entity priming experiment reveals that providing source-language entity names disproportionately improves cross-script questions, directly implicating entity mapping as the cross-script bottleneck. TransliCo (Liu et al., ACL 2024, arXiv:2401.06620) addresses script barriers through transliteration contrastive modeling (TCM), fine-tuning Glot500-m on 5% of data with Latin transliterations as contrastive targets, producing Furina which outperforms Glot500-m on cross-script zero-shot transfer — but operates on encoders at sentence level without entity grounding. Transliteration-based post-training alignment (Moosa et al., EMNLP Findings 2024, arXiv:2406.19759) achieves up to 50% improvement on cross-script English-centric transfer with even larger gains for non-English sources. EACA incorporates this insight by adding transliteration-augmented entity contrastive pairs for cross-script language combinations as a complementary mechanism. NeighXLM (EMNLP 2025 Findings) introduces neighbor-augmented contrastive pretraining for low-resource languages without parallel data, but targets general cross-lingual transfer rather than entity-specific factual consistency. PreAlign (EMNLP 2024) uses code-switching pretraining with word-level alignment but lacks entity anchoring. CrossIC-PT (EMNLP 2025) interleaves bilingual Wikipedia content without entity-level grounding. LEIA (ACL Findings 2024) inserts English entity names with [translate]/[/translate] markers during continued pretraining of decoder LLMs, improving cross-lingual transfer but without contrastive loss or frequency weighting. EntityCS (EMNLP Findings 2022) performs entity-centric code switching with Wikidata but is limited to encoder-only models. Entity Lens (BlackboxNLP 2025) reveals that decoder LLMs develop entity-specific mechanisms to represent and manipulate multi-token entities via task vectors. The middle-layer factual knowledge claim is supported by Liu & Niehues (ACL 2025) showing layer 16 of 32 has strongest cross-lingual retrieval alignment, and Marco et al. (arXiv:2404.03623) demonstrating via dynamic knowledge graphs that middle layers (L5-L21) encode comprehensive factual knowledge while late layers show 90%+ degradation. ELO (arXiv:2601.03648, Jan 2026) demonstrates efficient layer-specific optimization with 6.46x speedup from selective middle-layer updates. FactNet (arXiv:2602.03417) provides 1.7B entity-grounded facts across 316 Wikipedia editions with significant coverage skew. CLM-Bench (arXiv:2601.17397) shows edit vectors are nearly orthogonal across languages, further motivating entity-level alignment. DCO (arXiv:2603.04678, March 2026) proposes DPO-inspired post-hoc consistency optimization, complementary to pretraining-time methods. Veitsman et al. (arXiv:2603.18863, March 2026) find that sentence-level contrastive alignment fails for token-level tasks in XLM-R encoders, supporting entity-level approaches for entity-centric tasks. Cultural knowledge asymmetry research (ACL 2025) confirms that frequency drives cross-lingual transferability.\n\n## Approach\nEACA adds an InfoNCE contrastive loss on entity-span hidden states to the standard next-token prediction (NTP) objective during continued pretraining. The method comprises five integrated components: entity preprocessing, entity-level contrastive alignment, script-aware augmentation, stratified batch construction, and joint optimization with gradient monitoring.\n\n**1. Entity Preprocessing Pipeline.** Entity boundary annotation uses a two-stage pipeline. Stage 1 (primary): DaMuEL (2023), which provides 12.3B QID-annotated tokens across 53 languages (CC BY-SA), is used directly for the 10 target languages it covers (EN/ZH/JA/DE/AR/HI/TR/ID/VI/TH). DaMuEL provides start/end token indices per entity mention with Wikidata QID links, extracted from Wikipedia wikilinks and expanded via lemmatization and alias matching (~17% recall gain over raw wikilinks). Stage 2 (Tier 3 gap-filling): For the 3 Tier 3 languages not covered by DaMuEL (SW/YO/KM), a lightweight Wikipedia wikilinks extraction pipeline resolves hyperlinks to QIDs via Wikidata sitelinks (~50-60% mention coverage). mReFinED (EMNLP Findings 2023), which is 44-60x faster than comparable entity linkers, is applied as a second pass on high-resource languages to annotate non-hyperlinked entity mentions where higher recall is needed. Entity boundaries are marked with LEIA-style [ENT]/[/ENT] tokens around linked mentions. Preprocessing budget: 1.5-2 weeks engineering time, ~2-4 GPU-days on A100 for mReFinED gap-filling, ~24-48 CPU-hours for wikilinks extraction across Tier 3 languages. This pipeline is on the critical path and must complete before Phase 0.\n\n**2. Entity-Level Contrastive Alignment.** Entity representations are extracted via mean-pooling over hidden states within the [ENT]...[/ENT] span at a designated middle layer (defaulting to layer 16 for 32-layer models based on Liu & Niehues' ACL 2025 finding and Marco et al.'s analysis; validated via Phase 0 sweep over layers 12-20), with loss propagation blocked on boundary markers themselves. Contrastive pairs are constructed per QID from FactNet: positive pairs consist of atomic fact descriptions for the same QID across languages, while negatives come from different QIDs within the same batch (detailed in Component 4). Inverse-frequency weighting assigns higher contrastive loss weight to facts with lower cross-lingual FactNet coverage, directly targeting low-resource facts where CLiKA's conductivity analysis shows the largest gap.\n\nTheoretical motivation for entity-level granularity: Three converging lines of evidence support entity-level over sentence-level contrastive alignment for factual consistency: (1) Entity alignment analysis (arXiv:2510.10280) demonstrates Pearson r > 0.7 between entity alignment and cross-lingual consistency, with >99% of consistent facts showing successful entity alignment — establishing entities as the bottleneck for consistency; (2) CLM-Bench's finding that cross-lingual edit vectors are nearly orthogonal implies that factual knowledge editing, which operates at entity-level (subject-property-object triples), requires entity-aligned representations rather than sentence-aligned ones; (3) CLiKA's failure result — that sentence/document-level pretraining and instruction tuning do not improve conductivity — suggests that coarser-grained alignment conflates entity-specific factual knowledge with syntactic and discourse-level variation, diluting the alignment signal.\n\n**3. Script Barrier Mitigation.** EACA's 13 target languages span ~7 scripts (Latin: EN/DE/TR/ID/VI/SW/YO; CJK: ZH/JA; Arabic: AR; Devanagari: HI; Thai: TH; Khmer: KM). Ifergan et al. (NAACL Findings 2025) demonstrate that cross-lingual representation sharing (CKR) clusters strongly by script family (~37.6% same-script CKR vs. <10-20% cross-script in Mistral-7B), and Bandarkar et al. (arXiv:2603.17070) confirm script match as the primary predictor of transfer failure (~13% gap). This poses a genuine risk that entity-level contrastive alignment may primarily improve same-script entity alignment while showing limited gains for cross-script pairs. However, two findings provide grounds for cautious optimism: (a) Bandarkar et al.'s entity priming experiment shows source-language entity names disproportionately improve cross-script transfer, implicating entity mapping — not script-level representation — as the cross-script bottleneck for factual knowledge; (b) TransliCo (ACL 2024) demonstrates that transliteration-based contrastive learning bridges script barriers on encoders using only 5% of training data. EACA therefore incorporates a script-aware augmentation strategy: for cross-script QID pairs (e.g., EN-ZH, EN-AR, EN-HI, EN-TH, EN-KM), entity mentions in non-Latin scripts are supplemented with Latin transliterations appended within the [ENT] boundary (e.g., [ENT]北京 (Beijing)[/ENT]), providing a lexical bridge for the contrastive objective. This is tested as an ablation (EACA vs. EACA+translit) to isolate the contribution of transliteration augmentation beyond entity-level alignment. The evaluation plan includes mandatory script-grouped analysis: same-script entity alignment gains (Latin-Latin, CJK-CJK) vs. cross-script gains (Latin-CJK, Latin-Arabic, Latin-Devanagari, etc.), reporting both entity cosine similarity and downstream factual consistency metrics separately for each script-pair category. If Phase 0 reveals that cross-script entity alignment gains are <50% of same-script gains despite transliteration augmentation, this will be explicitly reported as a limitation and the analysis will quantify what fraction of EACA's overall conductivity improvement comes from same-script vs. cross-script alignment.\n\n**4. Stratified Batch Construction with Type-Aware Hard Negatives.** Effective contrastive learning is highly sensitive to negative quality (Robinson et al., ICLR 2021). EACA uses stratified mini-batching: each batch contains K_batch = 128-256 unique QIDs, with all available language instances per QID forming the positive set (asymmetric positive sets accommodate QIDs present in only 2-3 languages without dropping them). Minimum language coverage per QID is K_min = 3 languages; QIDs with fewer than 3 language instances are filtered during preprocessing. Class-Aware Masking (CAM) ensures that all instances of the same QID are excluded from the InfoNCE denominator, preventing false-negative contamination. For hard negative mining, type-aware stratification ensures ~50% of in-batch negatives share the anchor entity's Wikidata type (e.g., Q5/human, Q515/city, Q4830453/organization) — forcing the model to discriminate on fine-grained entity identity rather than coarse type. This is implemented via Wikidata instance-of (P31) properties, grouping entities into 8-10 macro-types for sampling. The remaining ~50% are random negatives for diversity. Batch composition is balanced across script families to ensure cross-script contrastive signals appear in every batch. The InfoNCE loss for entity e with QID q is: L_entity(q) = -log[exp(sim(h_q^i, h_q^j)/τ) / (exp(sim(h_q^i, h_q^j)/τ) + Σ_{k≠q} exp(sim(h_q^i, h_k)/τ))], where h_q^i, h_q^j are entity representations from different languages for the same QID, and h_k are representations from different QIDs, with τ = 0.07 as the temperature (tuned in Phase 0 over {0.05, 0.07, 0.1}).\n\n**5. Joint Optimization with Gradient Monitoring.** The joint objective is L_total = L_NTP + λ * L_entity_contrastive, with λ initialized at 0.1 (following guidance from headless LM work showing λ ∈ [0.01, 0.1] is appropriate for contrastive + generation joint training during CPT). A potential tension exists: NTP learns language-specific token distributions while contrastive loss pulls entity representations together across languages. Unlike Liu & Niehues' alternating approach, EACA uses joint optimization to ensure entity alignment co-adapts with the language modeling objective — but addresses gradient conflict risk through three mechanisms: (a) Phase 0 gradient analysis: cosine similarity between ∇L_NTP and ∇L_entity_contrastive is computed every 100 steps on the shared LoRA parameters. If gradient cosine similarity is negative for >30% of monitored steps, PCGrad projection (Yu et al., NeurIPS 2020) is applied — projecting the contrastive gradient onto the normal plane of the NTP gradient to eliminate destructive interference. (b) GradNorm (Chen et al., ICML 2018) is implemented as an optional dynamic λ adjustment mechanism: if the gradient magnitude ratio between the two losses drifts beyond 10:1, GradNorm normalizes to equalize learning rates. (c) λ warmup: contrastive loss weight ramps linearly from 0 to λ_target over the first 10% of training steps, allowing NTP to stabilize before contrastive pressure is introduced. Phase 0 reports gradient conflict frequency, cosine similarity distribution, and whether PCGrad/GradNorm activation was required — this informs the full training configuration. If gradient conflicts are severe (>50% of steps) even with PCGrad, the fallback is alternating optimization (NTP steps → contrastive steps per batch) following Liu & Niehues' validated approach.\n\nCatastrophic forgetting is mitigated through three mechanisms: (a) LoRA (rank 64) applied to middle layers only (layers 10-22), following CCL-XCoT's selective layer approach and ELO's findings that first/last layers are critical for general capabilities; (b) 15% general-domain English replay data mixed into training batches; (c) cosine learning rate schedule with linear warmup (peak LR 2e-5). Language selection follows a tiered strategy: Tier 1 comprises 4 anchor languages (EN/ZH/JA/DE, >1M entity-fact pairs), Tier 2 includes 6 mid-resource languages (AR/HI/TR/ID/VI/TH, 100K-1M pairs), and Tier 3 covers 3 low-resource languages (SW/YO/KM). Tier 3 viability assessment based on Wikipedia article counts (SW: ~117K, YO: ~37K, KM: ~12K) and FactNet's 0.36 low-resource yield rate estimates approximately 50K-200K entity-fact pairs for Swahili, 15K-60K for Yoruba, and 5K-25K for Khmer. None of the Tier 3 languages are covered by DaMuEL, so all three rely on the Wikipedia wikilinks extraction pipeline (Stage 2 above). A mandatory FactNet coverage audit in Phase 0 will report exact entity-fact pair counts for all 13 languages; minimum viable threshold is set at 10K entity-fact pairs per language (sufficient for contrastive batching at size 128-256 with adequate negative diversity). If any Tier 3 language falls below threshold, contingency replacements include Bengali (BN, ~157K Wikipedia articles), Tagalog (TL, ~115K articles), or Hausa (HA, ~8K articles but stronger NLP benchmark coverage). Languages below 25K pairs receive LEIA-style English entity augmentation to supplement contrastive pairs.\n\nPhase 0 pilot uses 500M tokens across 5 languages (3 Tier-1 + 2 Tier-2, selected to span at least 3 scripts for script barrier analysis) for approximately 130 H100 hours, with baselines including: (a) CCL-XCoT-style sentence-level contrastive CPT, (b) Liu & Niehues-style middle-layer sentence-level contrastive alignment (the closest methodological comparison, testing entity-level vs. sentence-level at the same middle layer), (c) LEIA-style entity augmentation without contrastive loss, (d) standard CPT, and (e) KBioXLM-style entity masking adaptation (masking [ENT]-bounded tokens and predicting via NTP, without contrastive loss — testing contrastive vs. masking-based entity alignment on decoders). Phase 0 additionally includes: a layer sweep (layers 12, 14, 16, 18, 20) to empirically determine optimal entity extraction depth; gradient conflict analysis (cosine similarity monitoring, PCGrad activation rate); and script-grouped entity alignment analysis (same-script vs. cross-script gains). Go/no-go criteria require entity cosine similarity improvement of at least 0.05, BMLAMA-53 consistency improvement of at least 2 points, no TyDiQA degradation beyond 1 point, AND gradient conflict rate below 50% (with or without PCGrad). Full training processes 1.5-2.5B tokens on LLaMA-3.1-8B (primary) and Gemma-7B (secondary, for CCL-XCoT comparability) across all 13 languages. A complementary EACA+DCO experiment tests whether pretraining-time and post-hoc consistency methods yield cumulative gains. Evaluation covers BMLAMA-53, TyDiQA-GoldP, X-CODAH, LiveCLKTBench, and CLiKA's XRR metric (to directly measure conductivity improvement), plus entity representation cosine similarity analysis. All metrics are reported with script-grouped breakdowns (same-script pairs, cross-script pairs, overall) as a mandatory analysis dimension. Ablations cover: entity-level vs. sentence-level contrastive (the central hypothesis), contrastive vs. masking-based entity alignment (EACA vs. KBioXLM-style adaptation), EACA vs. EACA+transliteration augmentation (script barrier mitigation), frequency weighting on/off, type-aware vs. random negatives, number of languages, layer selection, joint vs. alternating training, gradient conflict mitigation (none vs. PCGrad vs. GradNorm), contrastive pair construction (FactNet-grounded vs. parallel-text-based), and K_min language threshold (2 vs. 3 vs. 5).\n\n## Inspiration\nCCL-XCoT contrastive CPT framework (EMNLP 2025 Findings) + Liu & Niehues middle-layer contrastive alignment (ACL 2025) + FactNet entity-grounded facts (arXiv:2602.03417) + LEIA entity boundary markers (ACL 2024) + CLiKA conductivity diagnostic (NAACL 2024) + Entity-level alignment in crosslingual consistency (arXiv:2510.10280) + Entity Lens entity-specific mechanisms (BlackboxNLP 2025) + Marco et al. middle-layer factual knowledge (arXiv:2404.03623) + ELO selective layer optimization (arXiv:2601.03648) + Liu et al. frequency-driven transfer (EMNLP 2025) + CLM-Bench orthogonal edit vectors (arXiv:2601.17397) + cultural knowledge asymmetry frequency hypothesis (ACL 2025) + Ifergan et al. script-CKR dominance (NAACL Findings 2025) + Bandarkar et al. script barrier in reasoning models (arXiv:2603.17070) + TransliCo transliteration-contrastive script bridging (ACL 2024) + KBioXLM multi-granularity entity alignment (EMNLP Findings 2023) + DaMuEL QID-annotated corpus (2023) + Robinson et al. hard negative mining (ICLR 2021) + PCGrad gradient surgery (NeurIPS 2020) + GradNorm dynamic loss weighting (ICML 2018)\n\n## Key References\n- CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer Method for Mitigating Hallucination Generation (EMNLP Findings 2025)\n- Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs [Liu & Niehues] (ACL 2025, arXiv:2502.14830)\n- Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly [CLiKA] (NAACL 2024, arXiv:2404.04659)\n- On the Entity-Level Alignment in Crosslingual Consistency [Liu, Wang et al.] (arXiv:2510.10280)\n- FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding (arXiv 2026)\n- LEIA: Facilitating Cross-lingual Knowledge Transfer in Language Models with Entity-based Data Augmentation (ACL Findings 2024)\n- On the Representations of Entities in Auto-regressive Large Language Models [Entity Lens] (BlackboxNLP 2025, arXiv:2510.09421)\n- Unveiling LLMs: The Evolution of Latent Representations in a Dynamic Knowledge Graph [Marco et al.] (arXiv:2404.03623)\n- Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs [Ifergan et al.] (NAACL Findings 2025, arXiv:2408.10646)\n- Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts [Bandarkar et al.] (arXiv:2603.17070, March 2026)\n- TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models (ACL 2024, arXiv:2401.06620)\n- Breaking the Script Barrier in Multilingual Pre-Trained Language Models with Transliteration-Based Post-Training Alignment [Moosa et al.] (EMNLP Findings 2024, arXiv:2406.19759)\n- KBioXLM: A Knowledge-anchored Biomedical Multilingual Pretrained Language Model [Geng et al.] (EMNLP Findings 2023, arXiv:2311.11564)\n- DaMuEL: A Large Multilingual Dataset for Entity Linking (arXiv:2306.09288, 2023)\n- Contrastive Learning with Hard Negative Samples [Robinson et al.] (ICLR 2021)\n- Gradient Surgery for Multi-Task Learning [PCGrad, Yu et al.] (NeurIPS 2020)\n- GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks [Chen et al.] (ICML 2018)\n- mReFinED: An Efficient End-to-End Multilingual Entity Linking Model (EMNLP Findings 2023)\n- NeighXLM: Enhancing Cross-Lingual Transfer in Low-Resource Languages via Neighbor-Augmented Contrastive Pretraining (EMNLP Findings 2025)\n- mLUKE: The Power of Entity Representations in Multilingual Pretrained Language Models (ACL 2022)\n- ELO: Efficient Layer-Specific Optimization for Continual Pretraining of Multilingual LLMs (arXiv 2026)\n- Tracing Multilingual Factual Knowledge Acquisition in Pretraining (EMNLP Findings 2025)\n- PreAlign: Boosting Cross-Lingual Transfer by Early Establishment of Multilingual Alignment (EMNLP 2024)\n- Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training [CrossIC-PT] (EMNLP 2025)\n- Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon (ACL 2025)\n- EntityCS: Improving Zero-Shot Cross-lingual Transfer with Entity-Centric Code Switching (EMNLP Findings 2022)\n- Optimizing Language Models for Crosslingual Knowledge Consistency [DCO] (arXiv 2026)\n- Cross-Lingual Consistency of Factual Knowledge in Multilingual Language Models [BMLAMA] (EMNLP 2023)\n- LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs (arXiv 2025)\n- Why Better Cross-Lingual Alignment Fails for Better Cross-Lingual Transfer: Case of Encoders [Veitsman et al.] (arXiv 2026)\n- CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing (arXiv 2026)\n- DoLa: Decoding by Contrasting Layers Improves Factuality and Faithfulness of Large Language Models (ICLR 2024)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '1100-1550 H100 (Preprocessing: ~10-15 GPU-days A100 for mReFinED; Phase 0: ~130 including layer sweep + gradient analysis; Full training: ~800-1100; Evaluation: ~70; Ablations: ~90-165 including script/masking/gradient ablations)', 'timeline': '4.5-5.5 months (includes 1.5-2 weeks preprocessing pipeline)', 'estimated_gpu_cost': '$2,200-3,100 (at ~$2/H100-hr spot)'}\n- **human_in_loop**: {'gpu_hours': '900-1250 H100', 'timeline': '3.5-4.5 months', 'claude_api_cost': '$300-450 (FactNet coverage audit, DaMuEL integration, preprocessing pipeline, gradient analysis visualization, evaluation analysis, paper drafting)', 'estimated_gpu_cost': '$1,800-2,500'}\n- **auto_research**: {'gpu_hours': '1100-1600 H100', 'timeline': '3-4 months', 'claude_api_cost': '$600-950 (full pipeline automation: DaMuEL integration + mReFinED gap-filling + Tier 3 wikilinks pipeline + FactNet coverage audit + Tier 3 viability check, entity marker insertion, layer sweep, gradient analysis, hyperparameter sweep, script-grouped analysis, ablation analysis, paper writing)', 'estimated_gpu_cost': '$2,200-3,200', 'speed_bottleneck': 'Preprocessing pipeline (1.5-2 weeks) is on critical path before Phase 0; Phase 0 pilot (2-3 weeks including layer sweep, gradient analysis, and script-grouped evaluation) must complete before full training; full training wallclock ~30-50 hours per run on 8xH100; sequential dependency: preprocessing → FactNet audit gates Tier 3 language selection → pilot go/no-go gates full training'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T18:52:01.178Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:52:01.178Z",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422"
}
```

---

## Round 1

51 recorded events

### User

_source line 3 · 2026-05-19T18:52:01.191Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Entity-Anchored Contrastive Alignment for Cross-Lingual Knowledge Conductivity

## Description
EACA is a continued pretraining method that introduces InfoNCE contrastive loss on entity-span hidden states alongside standard next-token prediction, targeting entity-level cross-lingual knowledge conductivity — a capability that CLiKA (NAACL 2024) established is not substantially improved by existing multilingual pretraining or instruction tuning (XRR < 0.01). Unlike CCL-XCoT (sentence/paragraph-level contrastive CPT) and Liu & Niehues (ACL 2025, sentence-level middle-layer contrastive fine-tuning), EACA anchors contrastive pairs to Wikidata QIDs using FactNet's 1.7B entity-grounded atomic facts, operating at the entity level — the granularity empirically shown to be the bottleneck for cross-lingual consistency (entity alignment correlates at r > 0.7 with consistency, arXiv:2510.10280). This extends KBioXLM's (EMNLP Findings 2023) precedent of multi-granularity entity alignment in multilingual pretraining from encoder-based masking objectives in a specialized domain to explicit contrastive alignment in decoder-only LLMs for general-domain conductivity. Entity spans are marked with LEIA-style [ENT]/[/ENT] tokens using DaMuEL (12.3B QID-annotated tokens across 53 languages) as the primary annotation source for 10 of 13 target languages, supplemented by a Wikipedia wikilinks-to-QID extraction pipeline for the 3 uncovered Tier 3 languages (SW/YO/KM) and mReFinED entity linking for non-hyperlinked mention gap-filling, with 1.5-2 weeks budgeted for preprocessing. Representations are extracted via mean-pooling at middle layers (~layer 16, validated via Phase 0 sweep). The proposal explicitly addresses the script barrier identified by Ifergan et al. (NAACL Findings 2025) and Bandarkar et al. (arXiv:2603.17070): script similarity dominates representation sharing (~37.6% same-script CKR vs. <10-20% cross-script), but entity priming disproportionately helps cross-script transfer, motivating entity-level alignment as targeting the right bottleneck. Cross-script QID pairs receive transliteration-augmented entity markers (e.g., [ENT]北京 (Beijing)[/ENT]), inspired by TransliCo (ACL 2024), with mandatory script-grouped evaluation (same-script vs. cross-script gains). Stratified batch construction uses 128-256 entities per batch with class-aware false-negative masking, type-aware hard negatives (~50% same-type entities via Wikidata P31 properties, following Robinson et al. ICLR 2021), and asymmetric positive sets for entities with uneven language coverage (K_min = 3 languages per QID). Joint optimization (L_NTP + λ·L_contrastive, λ=0.1 with warmup) includes gradient conflict monitoring: cosine similarity between NTP and contrastive gradients is tracked every 100 steps, with PCGrad (Yu et al., NeurIPS 2020) activated if conflicts exceed 30% of steps, and GradNorm (Chen et al., ICML 2018) for dynamic λ adjustment if gradient magnitudes diverge beyond 10:1. Inverse-frequency weighting prioritizes low-resource entity-facts. Catastrophic forgetting is mitigated through LoRA (rank 64) on middle layers (10-22), 15% general-domain replay, and cosine LR scheduling. A tiered language selection spans 13 languages across ~7 scripts: Tier 1 (EN/ZH/JA/DE), Tier 2 (AR/HI/TR/ID/VI/TH), Tier 3 (SW/YO/KM), with mandatory Phase 0 FactNet coverage audit and contingency replacements. Phase 0 pilot (500M tokens, 5 languages spanning ≥3 scripts, ~130 H100 hours) includes baselines against sentence-level contrastive (CCL-XCoT), middle-layer sentence contrastive (Liu & Niehues), masking-based entity alignment (KBioXLM-style adaptation), LEIA augmentation, and standard CPT, plus layer sweep, gradient analysis, and script-grouped evaluation. Six key novelties: (1) entity-level contrastive anchoring vs. sentence-level, (2) structured knowledge grounding via FactNet QIDs vs. parallel text, (3) frequency-aware weighting, (4) joint NTP+contrastive optimization with gradient conflict monitoring at entity level during CPT, (5) script-aware transliteration augmentation for cross-script entity alignment, (6) direct targeting of CLiKA's conductivity gap with script-stratified evaluation.

## Core Problem
Can entity-level contrastive alignment — anchored to Wikidata QIDs and grounded in FactNet's structured atomic facts — improve cross-lingual knowledge conductivity (as defined by CLiKA's XRR metric, Gao et al. NAACL 2024) more effectively than sentence/paragraph-level contrastive continued pretraining (e.g., CCL-XCoT) or sentence-level middle-layer alignment (Liu & Niehues, ACL 2025)? CLiKA established that neither multilingual pretraining nor instruction tuning substantially improves conductivity, with XRR scores below 0.01 for most non-English languages. EACA hypothesizes that this conductivity barrier persists because prior methods align at sentence/document granularity — conflating entity-specific factual knowledge with syntactic and discourse-level variation — whereas factual knowledge is inherently structured around entities (subject-property-object triples). A critical complication, identified by Ifergan et al. (NAACL Findings 2025) and Bandarkar et al. (arXiv:2603.17070), is that script similarity is the dominant factor in cross-lingual representation sharing: high behavioral consistency does not imply shared internal representation for cross-script language pairs, and script match — not language family — is the primary predictor of knowledge transfer failure. Crucially, however, Bandarkar et al.'s entity priming experiment shows that providing source-language entity names disproportionately improves cross-script transfer, directly implicating entity-level mapping failure as the mechanism behind the script barrier. This suggests that entity-level contrastive alignment targets the right bottleneck, but that cross-script entity alignment requires additional support (e.g., transliteration augmentation) beyond what same-script entity alignment needs. EACA therefore addresses a two-level problem: (1) entity-level alignment as the fundamental unit of factual knowledge transfer, and (2) script-aware strategies to bridge the representation gap across writing systems.

## Opportunity
CCL-XCoT (EMNLP 2025 Findings) demonstrates that contrastive continued pretraining reduces cross-lingual hallucination by up to 62% but operates at sentence/paragraph granularity with parallel text. Liu & Niehues (ACL 2025) show that middle-layer contrastive alignment (layer 16 of 32 in LLaMA-3-8B) significantly improves cross-lingual transfer for downstream tasks, but again at sentence-level granularity and for task-specific fine-tuning rather than factual consistency. CLiKA (NAACL 2024) reveals a critical gap: existing multilingual pretraining and instruction tuning improve surface-level consistency but fail to improve knowledge conductivity (XRR < 0.01), suggesting that fundamentally different alignment granularity is needed. Meanwhile, FactNet (arXiv:2602.03417, Feb 2026) provides 1.7B entity-grounded atomic facts across 316 Wikipedia editions with Wikidata QID linking — enabling entity-level contrastive pairs grounded in structured knowledge. Entity Lens (BlackboxNLP 2025) confirms that decoder LLMs develop entity-specific internal mechanisms to represent multi-token entities. Liu et al. (EMNLP 2025 Findings) show that cross-lingual transfer is frequency-driven, with low-frequency facts benefiting most. Critically, recent evidence from entity-level alignment analysis (Liu, Wang et al., arXiv:2510.10280) demonstrates that cross-lingual factual consistency correlates strongly with entity alignment (Pearson r > 0.7), with over 99% of consistent facts exhibiting successful entity alignment — providing direct empirical motivation for entity-level rather than sentence-level contrastive objectives. Marco et al. ('Unveiling LLMs', arXiv:2404.03623) further establish that factual knowledge about subject entities concentrates in middle layers (L5-L21 for LLaMA-2-7B). KBioXLM (EMNLP Findings 2023) provides an important precedent: it demonstrated that multi-granularity knowledge alignment (entity masking, relation masking, passage relation prediction) during continued pretraining of XLM-R yields +20 F1 points on cross-lingual zero-shot biomedical tasks, establishing entity-anchored alignment as effective — but using masking-based reconstruction on encoders rather than contrastive loss on decoder LLMs, and targeting downstream task transfer rather than factual conductivity. Ifergan et al. (NAACL Findings 2025) reveal a deeper challenge: using knowledge editing as a probe for representation sharing, they find script similarity is the dominant factor (same-script CKR ~37.6% in Mistral; cross-script <10-20%), and that behavioral consistency diverges sharply from representation sharing for cross-script pairs. Bandarkar et al. (arXiv:2603.17070, March 2026) confirm this with regression analysis showing script match as the primary predictor after controlling for model capability and question difficulty (~13% accuracy gap), but critically, their entity priming experiment shows that providing source-language entity names disproportionately improves cross-script questions — directly implicating entity mapping as the bottleneck. TransliCo (ACL 2024) demonstrates that transliteration-based contrastive learning bridges script barriers using only 5% of training data on encoders. DaMuEL (2023) provides 12.3B tokens with QID-linked entity annotations across 53 languages, enabling efficient preprocessing for 10 of EACA's 13 target languages. The opportunity is to combine these insights — entity-level anchoring + structured knowledge grounding + middle-layer extraction + inverse-frequency weighting + script-aware strategies — into a contrastive CPT method that targets the specific granularity (entities), representation layer (middle), data regime (low-frequency facts), and script barriers where current methods demonstrably fall short.

## Related Work / Landscape
The cross-lingual factual consistency landscape spans several complementary approaches. CCL-XCoT (EMNLP 2025 Findings) is the primary baseline, employing InfoNCE symmetric contrastive loss during continued pretraining with a sentence-to-paragraph curriculum on Gemma-7B and LLaMA-3.1-8B using LoRA on layers 9-19/11-22, reducing hallucination by 62%, but operating at sentence/paragraph granularity without entity grounding or frequency weighting. Liu & Niehues (ACL 2025) represent the closest methodological precedent for contrastive alignment: they apply contrastive loss on mean-pooled sentence representations at middle layers (specifically layer 16 of 32 for LLaMA-3-8B-Instruct) during task-specific fine-tuning with LoRA (rank 8), demonstrating +1.5 F1 on slot filling and +1.5 BLEU on MT across 35 languages — however, they use sentence-level alignment with alternating (not joint) task/alignment training, target downstream task transfer rather than factual consistency, use parallel text rather than structured knowledge, and include no frequency weighting. EACA differentiates from Liu & Niehues on five axes: (1) entity-level rather than sentence-level granularity, (2) continued pretraining for factual consistency rather than task-specific fine-tuning, (3) FactNet-grounded contrastive pairs rather than parallel text, (4) joint NTP+contrastive objective rather than alternating training, and (5) inverse-frequency weighting for underrepresented facts. KBioXLM (Geng et al., EMNLP Findings 2023, arXiv:2311.11564) is an important precedent for multi-granularity entity-anchored alignment in multilingual pretraining. It performs continued pretraining on XLM-R using three alignment objectives grounded in UMLS biomedical knowledge: entity masking (code-switching entity mentions across EN-CN and predicting masked entity tokens via MLM cross-entropy), relation masking (masking relation tokens in subject-predicate-object triples), and passage relation prediction (3-way classification on aligned EN-CN Wikipedia passages). KBioXLM achieves +20 F1 points on cross-lingual zero-shot biomedical NER/RE. EACA extends this paradigm along four dimensions: (a) decoder-only LLMs vs. encoder (XLM-R), requiring contrastive loss on hidden states rather than masking-based reconstruction, since decoder LLMs lack bidirectional context for effective mask prediction; (b) general domain vs. biomedical, using FactNet's 1.7B facts across 316 editions vs. UMLS's specialized ontology; (c) explicit contrastive alignment (InfoNCE) vs. implicit alignment through masking, directly optimizing cross-lingual entity representation similarity rather than relying on the prediction bottleneck; (d) conductivity metric (CLiKA's XRR) vs. downstream task transfer, targeting the specific capability that prior methods fail to improve. CLiKA (Gao et al., NAACL 2024) provides the diagnostic framework: they define knowledge conductivity as the Cross-Retrieval Ratio (XRR) — retrieving knowledge learned in one language using another — and find that neither multilingual pretraining nor instruction tuning substantially improves XRR (scores < 0.01 for most non-English languages), with no concrete solutions proposed. The entity-level alignment analysis (Liu, Wang et al., arXiv:2510.10280) provides strong empirical support: cross-lingual consistency correlates with entity alignment at r > 0.7, and their SubInj method yields +14-32% recall and +17-44% consistency gains, but only at inference time; EACA aims to achieve this alignment at training time. On the script barrier dimension, Ifergan et al. ('Beneath the Surface of Consistency', NAACL Findings 2025, arXiv:2408.10646) demonstrate via knowledge editing probes on 7 decoder LLMs (7B scale) that script similarity is the dominant factor in cross-lingual knowledge representation sharing (CKR): same-script Latin pairs show ~37.6% average CKR in Mistral, while cross-script pairs show <10-20% transfer; crucially, they find that high behavioral consistency (CKC) does not imply shared representation for cross-script pairs, with E[NCL] consistently exceeding E[NTL]. Even targeted language extension pretraining achieves only marginal cross-script CKR improvement. Bandarkar et al. ('Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts', arXiv:2603.17070, March 2026) confirm via regression analysis on ECLeKTic and MultiLoKo that script match — not language family — is the primary predictor of knowledge transfer failure (~13% accuracy gap), but their entity priming experiment reveals that providing source-language entity names disproportionately improves cross-script questions, directly implicating entity mapping as the cross-script bottleneck. TransliCo (Liu et al., ACL 2024, arXiv:2401.06620) addresses script barriers through transliteration contrastive modeling (TCM), fine-tuning Glot500-m on 5% of data with Latin transliterations as contrastive targets, producing Furina which outperforms Glot500-m on cross-script zero-shot transfer — but operates on encoders at sentence level without entity grounding. Transliteration-based post-training alignment (Moosa et al., EMNLP Findings 2024, arXiv:2406.19759) achieves up to 50% improvement on cross-script English-centric transfer with even larger gains for non-English sources. EACA incorporates this insight by adding transliteration-augmented entity contrastive pairs for cross-script language combinations as a complementary mechanism. NeighXLM (EMNLP 2025 Findings) introduces neighbor-augmented contrastive pretraining for low-resource languages without parallel data, but targets general cross-lingual transfer rather than entity-specific factual consistency. PreAlign (EMNLP 2024) uses code-switching pretraining with word-level alignment but lacks entity anchoring. CrossIC-PT (EMNLP 2025) interleaves bilingual Wikipedia content without entity-level grounding. LEIA (ACL Findings 2024) inserts English entity names with [translate]/[/translate] markers during continued pretraining of decoder LLMs, improving cross-lingual transfer but without contrastive loss or frequency weighting. EntityCS (EMNLP Findings 2022) performs entity-centric code switching with Wikidata but is limited to encoder-only models. Entity Lens (BlackboxNLP 2025) reveals that decoder LLMs develop entity-specific mechanisms to represent and manipulate multi-token entities via task vectors. The middle-layer factual knowledge claim is supported by Liu & Niehues (ACL 2025) showing layer 16 of 32 has strongest cross-lingual retrieval alignment, and Marco et al. (arXiv:2404.03623) demonstrating via dynamic knowledge graphs that middle layers (L5-L21) encode comprehensive factual knowledge while late layers show 90%+ degradation. ELO (arXiv:2601.03648, Jan 2026) demonstrates efficient layer-specific optimization with 6.46x speedup from selective middle-layer updates. FactNet (arXiv:2602.03417) provides 1.7B entity-grounded facts across 316 Wikipedia editions with significant coverage skew. CLM-Bench (arXiv:2601.17397) shows edit vectors are nearly orthogonal across languages, further motivating entity-level alignment. DCO (arXiv:2603.04678, March 2026) proposes DPO-inspired post-hoc consistency optimization, complementary to pretraining-time methods. Veitsman et al. (arXiv:2603.18863, March 2026) find that sentence-level contrastive alignment fails for token-level tasks in XLM-R encoders, supporting entity-level approaches for entity-centric tasks. Cultural knowledge asymmetry research (ACL 2025) confirms that frequency drives cross-lingual transferability.

## Approach
EACA adds an InfoNCE contrastive loss on entity-span hidden states to the standard next-token prediction (NTP) objective during continued pretraining. The method comprises five integrated components: entity preprocessing, entity-level contrastive alignment, script-aware augmentation, stratified batch construction, and joint optimization with gradient monitoring.

**1. Entity Preprocessing Pipeline.** Entity boundary annotation uses a two-stage pipeline. Stage 1 (primary): DaMuEL (2023), which provides 12.3B QID-annotated tokens across 53 languages (CC BY-SA), is used directly for the 10 target languages it covers (EN/ZH/JA/DE/AR/HI/TR/ID/VI/TH). DaMuEL provides start/end token indices per entity mention with Wikidata QID links, extracted from Wikipedia wikilinks and expanded via lemmatization and alias matching (~17% recall gain over raw wikilinks). Stage 2 (Tier 3 gap-filling): For the 3 Tier 3 languages not covered by DaMuEL (SW/YO/KM), a lightweight Wikipedia wikilinks extraction pipeline resolves hyperlinks to QIDs via Wikidata sitelinks (~50-60% mention coverage). mReFinED (EMNLP Findings 2023), which is 44-60x faster than comparable entity linkers, is applied as a second pass on high-resource languages to annotate non-hyperlinked entity mentions where higher recall is needed. Entity boundaries are marked with LEIA-style [ENT]/[/ENT] tokens around linked mentions. Preprocessing budget: 1.5-2 weeks engineering time, ~2-4 GPU-days on A100 for mReFinED gap-filling, ~24-48 CPU-hours for wikilinks extraction across Tier 3 languages. This pipeline is on the critical path and must complete before Phase 0.

**2. Entity-Level Contrastive Alignment.** Entity representations are extracted via mean-pooling over hidden states within the [ENT]...[/ENT] span at a designated middle layer (defaulting to layer 16 for 32-layer models based on Liu & Niehues' ACL 2025 finding and Marco et al.'s analysis; validated via Phase 0 sweep over layers 12-20), with loss propagation blocked on boundary markers themselves. Contrastive pairs are constructed per QID from FactNet: positive pairs consist of atomic fact descriptions for the same QID across languages, while negatives come from different QIDs within the same batch (detailed in Component 4). Inverse-frequency weighting assigns higher contrastive loss weight to facts with lower cross-lingual FactNet coverage, directly targeting low-resource facts where CLiKA's conductivity analysis shows the largest gap.

Theoretical motivation for entity-level granularity: Three converging lines of evidence support entity-level over sentence-level contrastive alignment for factual consistency: (1) Entity alignment analysis (arXiv:2510.10280) demonstrates Pearson r > 0.7 between entity alignment and cross-lingual consistency, with >99% of consistent facts showing successful entity alignment — establishing entities as the bottleneck for consistency; (2) CLM-Bench's finding that cross-lingual edit vectors are nearly orthogonal implies that factual knowledge editing, which operates at entity-level (subject-property-object triples), requires entity-aligned representations rather than sentence-aligned ones; (3) CLiKA's failure result — that sentence/document-level pretraining and instruction tuning do not improve conductivity — suggests that coarser-grained alignment conflates entity-specific factual knowledge with syntactic and discourse-level variation, diluting the alignment signal.

**3. Script Barrier Mitigation.** EACA's 13 target languages span ~7 scripts (Latin: EN/DE/TR/ID/VI/SW/YO; CJK: ZH/JA; Arabic: AR; Devanagari: HI; Thai: TH; Khmer: KM). Ifergan et al. (NAACL Findings 2025) demonstrate that cross-lingual representation sharing (CKR) clusters strongly by script family (~37.6% same-script CKR vs. <10-20% cross-script in Mistral-7B), and Bandarkar et al. (arXiv:2603.17070) confirm script match as the primary predictor of transfer failure (~13% gap). This poses a genuine risk that entity-level contrastive alignment may primarily improve same-script entity alignment while showing limited gains for cross-script pairs. However, two findings provide grounds for cautious optimism: (a) Bandarkar et al.'s entity priming experiment shows source-language entity names disproportionately improve cross-script transfer, implicating entity mapping — not script-level representation — as the cross-script bottleneck for factual knowledge; (b) TransliCo (ACL 2024) demonstrates that transliteration-based contrastive learning bridges script barriers on encoders using only 5% of training data. EACA therefore incorporates a script-aware augmentation strategy: for cross-script QID pairs (e.g., EN-ZH, EN-AR, EN-HI, EN-TH, EN-KM), entity mentions in non-Latin scripts are supplemented with Latin transliterations appended within the [ENT] boundary (e.g., [ENT]北京 (Beijing)[/ENT]), providing a lexical bridge for the contrastive objective. This is tested as an ablation (EACA vs. EACA+translit) to isolate the contribution of transliteration augmentation beyond entity-level alignment. The evaluation plan includes mandatory script-grouped analysis: same-script entity alignment gains (Latin-Latin, CJK-CJK) vs. cross-script gains (Latin-CJK, Latin-Arabic, Latin-Devanagari, etc.), reporting both entity cosine similarity and downstream factual consistency metrics separately for each script-pair category. If Phase 0 reveals that cross-script entity alignment gains are <50% of same-script gains despite transliteration augmentation, this will be explicitly reported as a limitation and the analysis will quantify what fraction of EACA's overall conductivity improvement comes from same-script vs. cross-script alignment.

**4. Stratified Batch Construction with Type-Aware Hard Negatives.** Effective contrastive learning is highly sensitive to negative quality (Robinson et al., ICLR 2021). EACA uses stratified mini-batching: each batch contains K_batch = 128-256 unique QIDs, with all available language instances per QID forming the positive set (asymmetric positive sets accommodate QIDs present in only 2-3 languages without dropping them). Minimum language coverage per QID is K_min = 3 languages; QIDs with fewer than 3 language instances are filtered during preprocessing. Class-Aware Masking (CAM) ensures that all instances of the same QID are excluded from the InfoNCE denominator, preventing false-negative contamination. For hard negative mining, type-aware stratification ensures ~50% of in-batch negatives share the anchor entity's Wikidata type (e.g., Q5/human, Q515/city, Q4830453/organization) — forcing the model to discriminate on fine-grained entity identity rather than coarse type. This is implemented via Wikidata instance-of (P31) properties, grouping entities into 8-10 macro-types for sampling. The remaining ~50% are random negatives for diversity. Batch composition is balanced across script families to ensure cross-script contrastive signals appear in every batch. The InfoNCE loss for entity e with QID q is: L_entity(q) = -log[exp(sim(h_q^i, h_q^j)/τ) / (exp(sim(h_q^i, h_q^j)/τ) + Σ_{k≠q} exp(sim(h_q^i, h_k)/τ))], where h_q^i, h_q^j are entity representations from different languages for the same QID, and h_k are representations from different QIDs, with τ = 0.07 as the temperature (tuned in Phase 0 over {0.05, 0.07, 0.1}).

**5. Joint Optimization with Gradient Monitoring.** The joint objective is L_total = L_NTP + λ * L_entity_contrastive, with λ initialized at 0.1 (following guidance from headless LM work showing λ ∈ [0.01, 0.1] is appropriate for contrastive + generation joint training during CPT). A potential tension exists: NTP learns language-specific token distributions while contrastive loss pulls entity representations together across languages. Unlike Liu & Niehues' alternating approach, EACA uses joint optimization to ensure entity alignment co-adapts with the language modeling objective — but addresses gradient conflict risk through three mechanisms: (a) Phase 0 gradient analysis: cosine similarity between ∇L_NTP and ∇L_entity_contrastive is computed every 100 steps on the shared LoRA parameters. If gradient cosine similarity is negative for >30% of monitored steps, PCGrad projection (Yu et al., NeurIPS 2020) is applied — projecting the contrastive gradient onto the normal plane of the NTP gradient to eliminate destructive interference. (b) GradNorm (Chen et al., ICML 2018) is implemented as an optional dynamic λ adjustment mechanism: if the gradient magnitude ratio between the two losses drifts beyond 10:1, GradNorm normalizes to equalize learning rates. (c) λ warmup: contrastive loss weight ramps linearly from 0 to λ_target over the first 10% of training steps, allowing NTP to stabilize before contrastive pressure is introduced. Phase 0 reports gradient conflict frequency, cosine similarity distribution, and whether PCGrad/GradNorm activation was required — this informs the full training configuration. If gradient conflicts are severe (>50% of steps) even with PCGrad, the fallback is alternating optimization (NTP steps → contrastive steps per batch) following Liu & Niehues' validated approach.

Catastrophic forgetting is mitigated through three mechanisms: (a) LoRA (rank 64) applied to middle layers only (layers 10-22), following CCL-XCoT's selective layer approach and ELO's findings that first/last layers are critical for general capabilities; (b) 15% general-domain English replay data mixed into training batches; (c) cosine learning rate schedule with linear warmup (peak LR 2e-5). Language selection follows a tiered strategy: Tier 1 comprises 4 anchor languages (EN/ZH/JA/DE, >1M entity-fact pairs), Tier 2 includes 6 mid-resource languages (AR/HI/TR/ID/VI/TH, 100K-1M pairs), and Tier 3 covers 3 low-resource languages (SW/YO/KM). Tier 3 viability assessment based on Wikipedia article counts (SW: ~117K, YO: ~37K, KM: ~12K) and FactNet's 0.36 low-resource yield rate estimates approximately 50K-200K entity-fact pairs for Swahili, 15K-60K for Yoruba, and 5K-25K for Khmer. None of the Tier 3 languages are covered by DaMuEL, so all three rely on the Wikipedia wikilinks extraction pipeline (Stage 2 above). A mandatory FactNet coverage audit in Phase 0 will report exact entity-fact pair counts for all 13 languages; minimum viable threshold is set at 10K entity-fact pairs per language (sufficient for contrastive batching at size 128-256 with adequate negative diversity). If any Tier 3 language falls below threshold, contingency replacements include Bengali (BN, ~157K Wikipedia articles), Tagalog (TL, ~115K articles), or Hausa (HA, ~8K articles but stronger NLP benchmark coverage). Languages below 25K pairs receive LEIA-style English entity augmentation to supplement contrastive pairs.

Phase 0 pilot uses 500M tokens across 5 languages (3 Tier-1 + 2 Tier-2, selected to span at least 3 scripts for script barrier analysis) for approximately 130 H100 hours, with baselines including: (a) CCL-XCoT-style sentence-level contrastive CPT, (b) Liu & Niehues-style middle-layer sentence-level contrastive alignment (the closest methodological comparison, testing entity-level vs. sentence-level at the same middle layer), (c) LEIA-style entity augmentation without contrastive loss, (d) standard CPT, and (e) KBioXLM-style entity masking adaptation (masking [ENT]-bounded tokens and predicting via NTP, without contrastive loss — testing contrastive vs. masking-based entity alignment on decoders). Phase 0 additionally includes: a layer sweep (layers 12, 14, 16, 18, 20) to empirically determine optimal entity extraction depth; gradient conflict analysis (cosine similarity monitoring, PCGrad activation rate); and script-grouped entity alignment analysis (same-script vs. cross-script gains). Go/no-go criteria require entity cosine similarity improvement of at least 0.05, BMLAMA-53 consistency improvement of at least 2 points, no TyDiQA degradation beyond 1 point, AND gradient conflict rate below 50% (with or without PCGrad). Full training processes 1.5-2.5B tokens on LLaMA-3.1-8B (primary) and Gemma-7B (secondary, for CCL-XCoT comparability) across all 13 languages. A complementary EACA+DCO experiment tests whether pretraining-time and post-hoc consistency methods yield cumulative gains. Evaluation covers BMLAMA-53, TyDiQA-GoldP, X-CODAH, LiveCLKTBench, and CLiKA's XRR metric (to directly measure conductivity improvement), plus entity representation cosine similarity analysis. All metrics are reported with script-grouped breakdowns (same-script pairs, cross-script pairs, overall) as a mandatory analysis dimension. Ablations cover: entity-level vs. sentence-level contrastive (the central hypothesis), contrastive vs. masking-based entity alignment (EACA vs. KBioXLM-style adaptation), EACA vs. EACA+transliteration augmentation (script barrier mitigation), frequency weighting on/off, type-aware vs. random negatives, number of languages, layer selection, joint vs. alternating training, gradient conflict mitigation (none vs. PCGrad vs. GradNorm), contrastive pair construction (FactNet-grounded vs. parallel-text-based), and K_min language threshold (2 vs. 3 vs. 5).

## Inspiration
CCL-XCoT contrastive CPT framework (EMNLP 2025 Findings) + Liu & Niehues middle-layer contrastive alignment (ACL 2025) + FactNet entity-grounded facts (arXiv:2602.03417) + LEIA entity boundary markers (ACL 2024) + CLiKA conductivity diagnostic (NAACL 2024) + Entity-level alignment in crosslingual consistency (arXiv:2510.10280) + Entity Lens entity-specific mechanisms (BlackboxNLP 2025) + Marco et al. middle-layer factual knowledge (arXiv:2404.03623) + ELO selective layer optimization (arXiv:2601.03648) + Liu et al. frequency-driven transfer (EMNLP 2025) + CLM-Bench orthogonal edit vectors (arXiv:2601.17397) + cultural knowledge asymmetry frequency hypothesis (ACL 2025) + Ifergan et al. script-CKR dominance (NAACL Findings 2025) + Bandarkar et al. script barrier in reasoning models (arXiv:2603.17070) + TransliCo transliteration-contrastive script bridging (ACL 2024) + KBioXLM multi-granularity entity alignment (EMNLP Findings 2023) + DaMuEL QID-annotated corpus (2023) + Robinson et al. hard negative mining (ICLR 2021) + PCGrad gradient surgery (NeurIPS 2020) + GradNorm dynamic loss weighting (ICML 2018)

## Key References
- CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer Method for Mitigating Hallucination Generation (EMNLP Findings 2025)
- Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs [Liu & Niehues] (ACL 2025, arXiv:2502.14830)
- Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly [CLiKA] (NAACL 2024, arXiv:2404.04659)
- On the Entity-Level Alignment in Crosslingual Consistency [Liu, Wang et al.] (arXiv:2510.10280)
- FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding (arXiv 2026)
- LEIA: Facilitating Cross-lingual Knowledge Transfer in Language Models with Entity-based Data Augmentation (ACL Findings 2024)
- On the Representations of Entities in Auto-regressive Large Language Models [Entity Lens] (BlackboxNLP 2025, arXiv:2510.09421)
- Unveiling LLMs: The Evolution of Latent Representations in a Dynamic Knowledge Graph [Marco et al.] (arXiv:2404.03623)
- Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs [Ifergan et al.] (NAACL Findings 2025, arXiv:2408.10646)
- Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts [Bandarkar et al.] (arXiv:2603.17070, March 2026)
- TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models (ACL 2024, arXiv:2401.06620)
- Breaking the Script Barrier in Multilingual Pre-Trained Language Models with Transliteration-Based Post-Training Alignment [Moosa et al.] (EMNLP Findings 2024, arXiv:2406.19759)
- KBioXLM: A Knowledge-anchored Biomedical Multilingual Pretrained Language Model [Geng et al.] (EMNLP Findings 2023, arXiv:2311.11564)
- DaMuEL: A Large Multilingual Dataset for Entity Linking (arXiv:2306.09288, 2023)
- Contrastive Learning with Hard Negative Samples [Robinson et al.] (ICLR 2021)
- Gradient Surgery for Multi-Task Learning [PCGrad, Yu et al.] (NeurIPS 2020)
- GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks [Chen et al.] (ICML 2018)
- mReFinED: An Efficient End-to-End Multilingual Entity Linking Model (EMNLP Findings 2023)
- NeighXLM: Enhancing Cross-Lingual Transfer in Low-Resource Languages via Neighbor-Augmented Contrastive Pretraining (EMNLP Findings 2025)
- mLUKE: The Power of Entity Representations in Multilingual Pretrained Language Models (ACL 2022)
- ELO: Efficient Layer-Specific Optimization for Continual Pretraining of Multilingual LLMs (arXiv 2026)
- Tracing Multilingual Factual Knowledge Acquisition in Pretraining (EMNLP Findings 2025)
- PreAlign: Boosting Cross-Lingual Transfer by Early Establishment of Multilingual Alignment (EMNLP 2024)
- Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training [CrossIC-PT] (EMNLP 2025)
- Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon (ACL 2025)
- EntityCS: Improving Zero-Shot Cross-lingual Transfer with Entity-Centric Code Switching (EMNLP Findings 2022)
- Optimizing Language Models for Crosslingual Knowledge Consistency [DCO] (arXiv 2026)
- Cross-Lingual Consistency of Factual Knowledge in Multilingual Language Models [BMLAMA] (EMNLP 2023)
- LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs (arXiv 2025)
- Why Better Cross-Lingual Alignment Fails for Better Cross-Lingual Transfer: Case of Encoders [Veitsman et al.] (arXiv 2026)
- CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing (arXiv 2026)
- DoLa: Decoding by Contrasting Layers Improves Factuality and Faithfulness of Large Language Models (ICLR 2024)

## Resource Estimate
- **manual**: {'gpu_hours': '1100-1550 H100 (Preprocessing: ~10-15 GPU-days A100 for mReFinED; Phase 0: ~130 including layer sweep + gradient analysis; Full training: ~800-1100; Evaluation: ~70; Ablations: ~90-165 including script/masking/gradient ablations)', 'timeline': '4.5-5.5 months (includes 1.5-2 weeks preprocessing pipeline)', 'estimated_gpu_cost': '$2,200-3,100 (at ~$2/H100-hr spot)'}
- **human_in_loop**: {'gpu_hours': '900-1250 H100', 'timeline': '3.5-4.5 months', 'claude_api_cost': '$300-450 (FactNet coverage audit, DaMuEL integration, preprocessing pipeline, gradient analysis visualization, evaluation analysis, paper drafting)', 'estimated_gpu_cost': '$1,800-2,500'}
- **auto_research**: {'gpu_hours': '1100-1600 H100', 'timeline': '3-4 months', 'claude_api_cost': '$600-950 (full pipeline automation: DaMuEL integration + mReFinED gap-filling + Tier 3 wikilinks pipeline + FactNet coverage audit + Tier 3 viability check, entity marker insertion, layer sweep, gradient analysis, hyperparameter sweep, script-grouped analysis, ablation analysis, paper writing)', 'estimated_gpu_cost': '$2,200-3,200', 'speed_bottleneck': 'Preprocessing pipeline (1.5-2 weeks) is on critical path before Phase 0; Phase 0 pilot (2-3 weeks including layer sweep, gradient analysis, and script-grouped evaluation) must complete before full training; full training wallclock ~30-50 hours per run on 8xH100; sequential dependency: preprocessing → FactNet audit gates Tier 3 language selection → pilot go/no-go gates full training'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "1f34f9d0-00e1-4c36-9ca2-ad9281ece0e9",
  "type": "user",
  "uuid": "a5b86d26-0fce-43ed-92a2-30ced68c41fb",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:52:01.189Z_

```json
{
  "parentUuid": "a5b86d26-0fce-43ed-92a2-30ced68c41fb",
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
  "uuid": "d4892df8-58ed-4a75-b2b1-fcfc3608717e",
  "timestamp": "2026-05-19T18:52:01.189Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:52:01.189Z_

```json
{
  "parentUuid": "d4892df8-58ed-4a75-b2b1-fcfc3608717e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5b6b3aac-aaaf-42db-8a14-77d6b49b74ae",
  "timestamp": "2026-05-19T18:52:01.189Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Entity-Anchored Contrastive Alignment for Cross-Lingual Knowledge Conductivity  ## Description EACA is a continu…",
  "leafUuid": "5b6b3aac-aaaf-42db-8a14-77d6b49b74ae",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate entity-level cross-lingual alignment proposal",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:52:16.275Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 submission. Let me first carefully read and understand the proposal, then conduct web searches to understand the field landscape before making my assessment.

Wait - the user says CoRL 2026, but the proposal is about cross-lingual knowledge conductivity in language models. CoRL is the Conference on Robot Learning. This seems like a mismatch - this proposal seems more suited for ACL, EMNLP, NAACL, or similar NLP/CL venues. Let me re-read...

Actually, looking more carefully, the user's system prompt says "评估其投稿 CoRL 2026 主会的中稿潜力" - evaluating submission potential for CoRL 2026 main conference. 

There's definitely a venue mismatch here - this is clearly an NLP/multilingual LLM paper, not a robotics paper. But the rubric mentions "对 NLP/CL 领域的影响力", so perhaps the user meant a Computational Linguistics venue and "CoRL" is a typo or misunderstanding. Rather than get stuck on the venue name, I should focus on evaluating the proposal's quality and potential for a top-tier NLP/CL conference.

Before I assess the idea, I need to search for recent work in this space to understand the current landscape - specifically around cross-lingual knowledge alignment, contrastive pretraining approaches, entity-level alignment, and how multilingual LLMs handle script barriers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b6b3aac-aaaf-42db-8a14-77d6b49b74ae",
  "isSidechain": false,
  "requestId": "req_011CbCS1HRAtpFxf1iv3ay9U",
  "type": "assistant",
  "uuid": "e378823c-722b-4e8c-a724-e91525c3f8fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A12eRh7to9fHk6qMFExn62",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11687,
      "cache_read_input_tokens": 13985,
      "output_tokens": 623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 623,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 11687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11687
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

_source line 9 · 2026-05-19T18:52:16.282Z_

I need to conduct thorough field research before making any assessment. Let me start with targeted web searches on the key topics in this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e378823c-722b-4e8c-a724-e91525c3f8fe",
  "isSidechain": false,
  "requestId": "req_011CbCS1HRAtpFxf1iv3ay9U",
  "type": "assistant",
  "uuid": "2c6711fa-4bb0-4a72-9456-251a7d2e59ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A12eRh7to9fHk6qMFExn62",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11687,
      "cache_read_input_tokens": 13985,
      "output_tokens": 623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 623,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 11687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11687
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

_source line 10 · 2026-05-19T18:52:16.297Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015JXJi6CRo7iYFGEADke9Fm`</summary>

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
  "parentUuid": "2c6711fa-4bb0-4a72-9456-251a7d2e59ec",
  "isSidechain": false,
  "requestId": "req_011CbCS1HRAtpFxf1iv3ay9U",
  "type": "assistant",
  "uuid": "6b35f03b-846d-45cf-92c5-f93ac273db86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A12eRh7to9fHk6qMFExn62",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11687,
      "cache_read_input_tokens": 13985,
      "output_tokens": 623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 623,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 11687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11687
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

_source line 11 · 2026-05-19T18:52:16.304Z_

<details><summary>↩ Tool result · `toolu_015JXJi6CRo7iYFGEADke9Fm`</summary>

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
  "parentUuid": "6b35f03b-846d-45cf-92c5-f93ac273db86",
  "isSidechain": false,
  "promptId": "1f34f9d0-00e1-4c36-9ca2-ad9281ece0e9",
  "type": "user",
  "uuid": "5b185b8e-d91b-4994-824f-7a741cf51d46",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "6b35f03b-846d-45cf-92c5-f93ac273db86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T18:52:20.353Z_

Now let me conduct the required field research with multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b185b8e-d91b-4994-824f-7a741cf51d46",
  "isSidechain": false,
  "requestId": "req_011CbCS2QExfWDmragGkmAtD",
  "type": "assistant",
  "uuid": "5dd70a9f-e034-46f9-919d-fb8d786722e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcLxScWvXRvu8b8ATZ1S4B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 25672,
      "output_tokens": 323,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1148,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 323,
          "cache_read_input_tokens": 25672,
          "cache_creation_input_tokens": 1148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1148
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

_source line 13 · 2026-05-19T18:52:20.803Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L756nSVkF8tiooLwuWQNGc`</summary>

```json
{
  "query": "CLiKA cross-lingual knowledge conductivity NAACL 2024 XRR metric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5dd70a9f-e034-46f9-919d-fb8d786722e1",
  "isSidechain": false,
  "requestId": "req_011CbCS2QExfWDmragGkmAtD",
  "type": "assistant",
  "uuid": "967e6559-6af9-4cdc-bbdf-35f88630180d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcLxScWvXRvu8b8ATZ1S4B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 25672,
      "output_tokens": 323,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1148,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 323,
          "cache_read_input_tokens": 25672,
          "cache_creation_input_tokens": 1148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1148
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

_source line 14 · 2026-05-19T18:52:21.281Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JNWECLQHthW1nnzWXEC5KY`</summary>

```json
{
  "query": "CCL-XCoT contrastive cross-lingual continued pretraining hallucination EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "967e6559-6af9-4cdc-bbdf-35f88630180d",
  "isSidechain": false,
  "requestId": "req_011CbCS2QExfWDmragGkmAtD",
  "type": "assistant",
  "uuid": "5266b378-4f6f-4958-80ce-f085a8b7c735",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcLxScWvXRvu8b8ATZ1S4B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 25672,
      "output_tokens": 323,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1148,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 323,
          "cache_read_input_tokens": 25672,
          "cache_creation_input_tokens": 1148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1148
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

_source line 15 · 2026-05-19T18:52:21.839Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DduZTCK2qjMk2Nr2ncA4BJ`</summary>

```json
{
  "query": "entity-level cross-lingual alignment contrastive learning multilingual LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5266b378-4f6f-4958-80ce-f085a8b7c735",
  "isSidechain": false,
  "requestId": "req_011CbCS2QExfWDmragGkmAtD",
  "type": "assistant",
  "uuid": "ebbb0a81-1f11-4edb-b682-a83dfca376ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcLxScWvXRvu8b8ATZ1S4B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 25672,
      "output_tokens": 323,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1148,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 323,
          "cache_read_input_tokens": 25672,
          "cache_creation_input_tokens": 1148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1148
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

_source line 16 · 2026-05-19T18:52:22.222Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018CMmkiGTswWXhCnf2JX22S`</summary>

```json
{
  "query": "FactNet billion-scale knowledge graph multilingual factual grounding arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebbb0a81-1f11-4edb-b682-a83dfca376ee",
  "isSidechain": false,
  "requestId": "req_011CbCS2QExfWDmragGkmAtD",
  "type": "assistant",
  "uuid": "6601e7ba-8c2b-4090-8ff0-ee5677b93dc9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcLxScWvXRvu8b8ATZ1S4B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 25672,
      "output_tokens": 323,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1148,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 323,
          "cache_read_input_tokens": 25672,
          "cache_creation_input_tokens": 1148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1148
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

_source line 17 · 2026-05-19T18:52:22.778Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015CyVwwkWis9ffhTTL6a5mv`</summary>

```json
{
  "query": "script barrier multilingual LLM cross-lingual knowledge transfer Bandarkar Ifergan 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6601e7ba-8c2b-4090-8ff0-ee5677b93dc9",
  "isSidechain": false,
  "requestId": "req_011CbCS2QExfWDmragGkmAtD",
  "type": "assistant",
  "uuid": "3b2a05c6-61b4-4f54-a2d2-884f27440ff5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcLxScWvXRvu8b8ATZ1S4B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 25672,
      "output_tokens": 323,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1148,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 323,
          "cache_read_input_tokens": 25672,
          "cache_creation_input_tokens": 1148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1148
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

_source line 18 · 2026-05-19T18:52:26.900Z_

<details><summary>↩ Tool result · `toolu_01L756nSVkF8tiooLwuWQNGc`</summary>

```text
Web search results for query: "CLiKA cross-lingual knowledge conductivity NAACL 2024 XRR metric"

Links: [{"title":"[Quick Review] Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly","url":"https://liner.com/review/multilingual-pretraining-and-instruction-tuning-improve-crosslingual-knowledge-alignment-but"},{"title":"Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.339/"},{"title":"[PDF] Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Multilingual-Pretraining-and-Instruction-Tuning-But-Gao-Hu/8f2630c308b46ce02a06ff623fcbc130d481481d"},{"title":"Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly","url":"https://arxiv.org/html/2404.04659v1"},{"title":"Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual   Knowledge Alignment, But Only Shallowly","url":"https://arxiv.org/pdf/2404.04659"},{"title":"Teaching Llama a New Language Through Cross-Lingual Knowledge Transfer - ACL Anthology","url":"https://aclanthology.org/2024.findings-naacl.210/"},{"title":"Key ingredients for effective zero-shot cross-lingual knowledge transfer in generative tasks - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.401/"},{"title":"Accepted Papers - NAACL-HLT 2024","url":"https://2024.naacl.org/program/accepted_papers/"}]

Based on the search results, I found detailed information about CLiKA and the XRR metric from the NAACL 2024 paper:

## CLiKA Framework

CLiKA is a systematic framework to assess the cross-lingual knowledge alignment of LLMs in the Performance, Consistency and Conductivity levels, and explored the effect of multilingual pretraining and instruction tuning on the degree of alignment.

## XRR Metric

The Cross-retrieval ratio (XRR) is a metric for Conductivity within the CLiKA framework. The Fictional knowledge dataset, comprising artificial entity-relation knowledge with English-only relation training, enables direct measurement of knowledge conductivity from English to other languages.

## Key Findings

The overall cross-lingual knowledge alignment, especially in the conductivity level, is unsatisfactory for all tested LLMs, and neither multilingual pretraining nor instruction tuning can substantially improve the cross-lingual knowledge conductivity.

The paper is titled "Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly" and was presented at NAACL 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "967e6559-6af9-4cdc-bbdf-35f88630180d",
  "isSidechain": false,
  "promptId": "1f34f9d0-00e1-4c36-9ca2-ad9281ece0e9",
  "type": "user",
  "uuid": "ecc14429-385f-4485-98b1-b193381df442",
  "toolUseResult": {
    "query": "CLiKA cross-lingual knowledge conductivity NAACL 2024 XRR metric",
    "results": [
      {
        "tool_use_id": "srvtoolu_018FnJKZHdBJKSwbSNHrqG7K",
        "content": [
          {
            "title": "[Quick Review] Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly",
            "url": "https://liner.com/review/multilingual-pretraining-and-instruction-tuning-improve-crosslingual-knowledge-alignment-but"
          },
          {
            "title": "Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-long.339/"
          },
          {
            "title": "[PDF] Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Multilingual-Pretraining-and-Instruction-Tuning-But-Gao-Hu/8f2630c308b46ce02a06ff623fcbc130d481481d"
          },
          {
            "title": "Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly",
            "url": "https://arxiv.org/html/2404.04659v1"
          },
          {
            "title": "Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual   Knowledge Alignment, But Only Shallowly",
            "url": "https://arxiv.org/pdf/2404.04659"
          },
          {
            "title": "Teaching Llama a New Language Through Cross-Lingual Knowledge Transfer - ACL Anthology",
            "url": "https://aclanthology.org/2024.findings-naacl.210/"
          },
          {
            "title": "Key ingredients for effective zero-shot cross-lingual knowledge transfer in generative tasks - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-long.401/"
          },
          {
            "title": "Accepted Papers - NAACL-HLT 2024",
            "url": "https://2024.naacl.org/program/accepted_papers/"
          }
        ]
      },
      "Based on the search results, I found detailed information about CLiKA and the XRR metric from the NAACL 2024 paper:\n\n## CLiKA Framework\n\nCLiKA is a systematic framework to assess the cross-lingual knowledge alignment of LLMs in the Performance, Consistency and Conductivity levels, and explored the effect of multilingual pretraining and instruction tuning on the degree of alignment.\n\n## XRR Metric\n\nThe Cross-retrieval ratio (XRR) is a metric for Conductivity within the CLiKA framework. The Fictional knowledge dataset, comprising artificial entity-relation knowledge with English-only relation training, enables direct measurement of knowledge conductivity from English to other languages.\n\n## Key Findings\n\nThe overall cross-lingual knowledge alignment, especially in the conductivity level, is unsatisfactory for all tested LLMs, and neither multilingual pretraining nor instruction tuning can substantially improve the cross-lingual knowledge conductivity.\n\nThe paper is titled \"Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly\" and was presented at NAACL 2024."
    ],
    "durationSeconds": 6.091950001000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "967e6559-6af9-4cdc-bbdf-35f88630180d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T18:52:27.367Z_

<details><summary>↩ Tool result · `toolu_018CMmkiGTswWXhCnf2JX22S`</summary>

```text
Web search results for query: "FactNet billion-scale knowledge graph multilingual factual grounding arXiv 2026"

Links: [{"title":"[2602.03417] FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding","url":"https://arxiv.org/abs/2602.03417"},{"title":"FactNet: Multilingual Knowledge Graph & FNAR","url":"https://www.emergentmind.com/topics/factnet"},{"title":"FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding","url":"https://arxiv.org/pdf/2602.03417"},{"title":"GitHub - yl-shen/factnet: FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding · GitHub","url":"https://github.com/yl-shen/factnet"},{"title":"FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding","url":"https://arxiv.org/html/2602.03417v1"},{"title":"(PDF) FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding","url":"https://www.researchgate.net/publication/400415601_FactNet_A_Billion-Scale_Knowledge_Graph_for_Multilingual_Factual_Grounding"}]

Based on the search results, here's what I found about FactNet:

## FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding

FactNet is a massive, open-source resource designed to unify 1.7 billion atomic assertions with 3.01 billion auditable evidence pointers derived exclusively from 316 Wikipedia editions.

**Key Features:**

- **Construction Method**: Unlike recent synthetic approaches, FactNet employs a strictly deterministic construction pipeline, ensuring that every evidence unit is recoverable with byte-level precision.

- **Performance**: Extensive auditing confirms a high grounding precision of 92.1%, even in long-tail languages.

- **Architecture**: The graph couples Wikidata claims with native evidence (from Wikipedia) via three layers: FactStatement (atomic unit), FactSense (grounded span with byte-offsets), and FactSynset (cross-lingual normalization).

- **Evaluation Suite**: FactNet-Bench is a comprehensive evaluation suite for Knowledge Graph Completion, Question Answering, and Fact Checking.

**Publication Details:**

The paper was submitted to arXiv on February 3, 2026, with the identifier arXiv:2602.03417.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6601e7ba-8c2b-4090-8ff0-ee5677b93dc9",
  "isSidechain": false,
  "promptId": "1f34f9d0-00e1-4c36-9ca2-ad9281ece0e9",
  "type": "user",
  "uuid": "40a0b0b6-7f7a-4717-979c-287ca020335e",
  "toolUseResult": {
    "query": "FactNet billion-scale knowledge graph multilingual factual grounding arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CsnQUPrT8ttjasRjFXhhKs",
        "content": [
          {
            "title": "[2602.03417] FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding",
            "url": "https://arxiv.org/abs/2602.03417"
          },
          {
            "title": "FactNet: Multilingual Knowledge Graph & FNAR",
            "url": "https://www.emergentmind.com/topics/factnet"
          },
          {
            "title": "FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding",
            "url": "https://arxiv.org/pdf/2602.03417"
          },
          {
            "title": "GitHub - yl-shen/factnet: FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding · GitHub",
            "url": "https://github.com/yl-shen/factnet"
          },
          {
            "title": "FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding",
            "url": "https://arxiv.org/html/2602.03417v1"
          },
          {
            "title": "(PDF) FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding",
            "url": "https://www.researchgate.net/publication/400415601_FactNet_A_Billion-Scale_Knowledge_Graph_for_Multilingual_Factual_Grounding"
          }
        ]
      },
      "Based on the search results, here's what I found about FactNet:\n\n## FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding\n\nFactNet is a massive, open-source resource designed to unify 1.7 billion atomic assertions with 3.01 billion auditable evidence pointers derived exclusively from 316 Wikipedia editions.\n\n**Key Features:**\n\n- **Construction Method**: Unlike recent synthetic approaches, FactNet employs a strictly deterministic construction pipeline, ensuring that every evidence unit is recoverable with byte-level precision.\n\n- **Performance**: Extensive auditing confirms a high grounding precision of 92.1%, even in long-tail languages.\n\n- **Architecture**: The graph couples Wikidata claims with native evidence (from Wikipedia) via three layers: FactStatement (atomic unit), FactSense (grounded span with byte-offsets), and FactSynset (cross-lingual normalization).\n\n- **Evaluation Suite**: FactNet-Bench is a comprehensive evaluation suite for Knowledge Graph Completion, Question Answering, and Fact Checking.\n\n**Publication Details:**\n\nThe paper was submitted to arXiv on February 3, 2026, with the identifier arXiv:2602.03417."
    ],
    "durationSeconds": 5.141912371999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6601e7ba-8c2b-4090-8ff0-ee5677b93dc9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T18:52:28.964Z_

<details><summary>↩ Tool result · `toolu_01DduZTCK2qjMk2Nr2ncA4BJ`</summary>

```text
Web search results for query: "entity-level cross-lingual alignment contrastive learning multilingual LLM 2025 2026"

Links: [{"title":"Improving In-context Learning of Multilingual Generative Language Models   with Cross-lingual Alignment","url":"https://arxiv.org/pdf/2311.08089"},{"title":"Multi-Level Contrastive Learning for Cross-Lingual Alignment | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel7/9745891/9746004/09747720.pdf"},{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://arxiv.org/pdf/2504.09378"},{"title":"Speak in Context: Multilingual ASR with Speech–Context Alignment via Contrastive Learning","url":"https://arxiv.org/html/2603.06505"},{"title":"Multi-Level Contrastive Learning for Cross-Lingual Alignment","url":"https://arxiv.org/pdf/2202.13083"},{"title":"On the Entity-Level Alignment in Crosslingual Consistency","url":"https://arxiv.org/pdf/2510.10280"},{"title":"AlignX: Advancing Multilingual Large Language Models ...","url":"https://aclanthology.org/2025.emnlp-main.328.pdf"},{"title":"Probing the Emergence of Cross-lingual Alignment during LLM Training","url":"https://arxiv.org/pdf/2406.13229"}]

I've found several relevant research papers and articles on entity-level cross-lingual alignment, contrastive learning, and multilingual LLMs from 2025-2026. Here are the key findings:

## Recent Research on Cross-Lingual Alignment in Multilingual LLMs

LLMs have demonstrated remarkable capabilities in multilingual tasks, including translation, question answering, and factual recall, and recent work has been focused on understanding how these systems achieve cross-lingual consistency.

**Entity-Level Alignment:** Entity alignment is important and facilitates consistent factual recall across languages. Alignment facilitates two crucial transition stages in multilingual factual recall: (1) mapping language-specific inputs into a shared conceptual space, and (2) projecting the shared latent representation back into the correct surface realization in the target languages.

**Contrastive Learning Approaches:** Multilingual contrastive learning aims to align the internal representations of models across different languages. Additionally, unlike sentence-level alignment used in most previous studies, multi-level approaches explicitly integrate word-level information of each pair of parallel sentences into contrastive learning.

**2025-2026 Research:** MEXA is a cross-lingual retrieval-based score for languages other than English, computed by comparing non-English representations to English representations from the same model across a fixed set of parallel texts, and MEXA scores are strongly correlated with multilingual task accuracy.

The search results indicate active research in this area with recent papers focusing on understanding and improving cross-lingual alignment mechanisms in multilingual language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebbb0a81-1f11-4edb-b682-a83dfca376ee",
  "isSidechain": false,
  "promptId": "1f34f9d0-00e1-4c36-9ca2-ad9281ece0e9",
  "type": "user",
  "uuid": "aaca7d46-7084-4ee4-8d1a-e1beba1b06e7",
  "toolUseResult": {
    "query": "entity-level cross-lingual alignment contrastive learning multilingual LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HbBLaXf6THiMcG9tY5Zask",
        "content": [
          {
            "title": "Improving In-context Learning of Multilingual Generative Language Models   with Cross-lingual Alignment",
            "url": "https://arxiv.org/pdf/2311.08089"
          },
          {
            "title": "Multi-Level Contrastive Learning for Cross-Lingual Alignment | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/iel7/9745891/9746004/09747720.pdf"
          },
          {
            "title": "Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs",
            "url": "https://arxiv.org/pdf/2504.09378"
          },
          {
            "title": "Speak in Context: Multilingual ASR with Speech–Context Alignment via Contrastive Learning",
            "url": "https://arxiv.org/html/2603.06505"
          },
          {
            "title": "Multi-Level Contrastive Learning for Cross-Lingual Alignment",
            "url": "https://arxiv.org/pdf/2202.13083"
          },
          {
            "title": "On the Entity-Level Alignment in Crosslingual Consistency",
            "url": "https://arxiv.org/pdf/2510.10280"
          },
          {
            "title": "AlignX: Advancing Multilingual Large Language Models ...",
            "url": "https://aclanthology.org/2025.emnlp-main.328.pdf"
          },
          {
            "title": "Probing the Emergence of Cross-lingual Alignment during LLM Training",
            "url": "https://arxiv.org/pdf/2406.13229"
          }
        ]
      },
      "I've found several relevant research papers and articles on entity-level cross-lingual alignment, contrastive learning, and multilingual LLMs from 2025-2026. Here are the key findings:\n\n## Recent Research on Cross-Lingual Alignment in Multilingual LLMs\n\nLLMs have demonstrated remarkable capabilities in multilingual tasks, including translation, question answering, and factual recall, and recent work has been focused on understanding how these systems achieve cross-lingual consistency.\n\n**Entity-Level Alignment:** Entity alignment is important and facilitates consistent factual recall across languages. Alignment facilitates two crucial transition stages in multilingual factual recall: (1) mapping language-specific inputs into a shared conceptual space, and (2) projecting the shared latent representation back into the correct surface realization in the target languages.\n\n**Contrastive Learning Approaches:** Multilingual contrastive learning aims to align the internal representations of models across different languages. Additionally, unlike sentence-level alignment used in most previous studies, multi-level approaches explicitly integrate word-level information of each pair of parallel sentences into contrastive learning.\n\n**2025-2026 Research:** MEXA is a cross-lingual retrieval-based score for languages other than English, computed by comparing non-English representations to English representations from the same model across a fixed set of parallel texts, and MEXA scores are strongly correlated with multilingual task accuracy.\n\nThe search results indicate active research in this area with recent papers focusing on understanding and improving cross-lingual alignment mechanisms in multilingual language models."
    ],
    "durationSeconds": 7.122672519,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ebbb0a81-1f11-4edb-b682-a83dfca376ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Entity-Anchored Contrastive Alignment for Cross-Lingual Knowledge Conductivity  ## Description EACA is a continu…",
  "leafUuid": "aaca7d46-7084-4ee4-8d1a-e1beba1b06e7",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate entity-level cross-lingual alignment proposal",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422"
}
```

---

### Tool result

_source line 23 · 2026-05-19T18:52:30.280Z_

<details><summary>↩ Tool result · `toolu_01JNWECLQHthW1nnzWXEC5KY`</summary>

```text
Web search results for query: "CCL-XCoT contrastive cross-lingual continued pretraining hallucination EMNLP 2025"

Links: [{"title":"CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer Method for Mitigating Hallucination Generation","url":"https://arxiv.org/html/2507.14239"},{"title":"CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer Method for Mitigating Hallucination Generation","url":"https://arxiv.org/pdf/2507.14239"},{"title":"[2507.14239] CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer Method for Mitigating Hallucination Generation","url":"https://arxiv.org/abs/2507.14239"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer ...","url":"https://aclanthology.org/2025.findings-emnlp.93.pdf"},{"title":"Cross-Lingual Continuous Pretraining","url":"https://www.emergentmind.com/topics/cross-lingual-continuous-pretraining"}]

I found relevant information about CCL-XCoT. Here's what the search results show:

## Overview

CCL-XCoT (Curriculum-based Contrastive Learning-based Cross-lingual Chain-of-Thought) is proposed by Weihua Zheng, Roy Ka-Wei Lee, Zhengyuan Liu, Kui Wu, AiTi Aw, and Bowei Zou from the Institute for Infocomm Research.

## Problem and Approach

Multilingual Large Language Models demonstrate strong generalization across languages, yet they remain prone to hallucinations, especially in low-resource languages, due to training data imbalances.

CCL-XCoT is a two-stage fine-tuning framework for mitigating hallucination in MLLMs. The approach first enhances cross-lingual semantic alignment through curriculum-based contrastive learning combined with next-token prediction during continued pre-training. Then it introduces a cross-lingual Chain-of-Thought (XCoT) prompting strategy during instruction fine-tuning, which guides the model to reason in a high-resource language before generating answers in the target low-resource language.

## Results

Experimental results show that CCL-XCoT reduces hallucination rates by up to 62% and substantially improves factual knowledge transfer across language pairs, without relying on external retrieval or multi-model ensembles.

## Publication

The paper was accepted as a Findings paper at EMNLP 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5266b378-4f6f-4958-80ce-f085a8b7c735",
  "isSidechain": false,
  "promptId": "1f34f9d0-00e1-4c36-9ca2-ad9281ece0e9",
  "type": "user",
  "uuid": "93a60eb6-9136-4d00-b2fc-ad0d7fb4e877",
  "toolUseResult": {
    "query": "CCL-XCoT contrastive cross-lingual continued pretraining hallucination EMNLP 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_018pVmAmVTE7dG2zFkHXAN8G",
        "content": [
          {
            "title": "CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer Method for Mitigating Hallucination Generation",
            "url": "https://arxiv.org/html/2507.14239"
          },
          {
            "title": "CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer Method for Mitigating Hallucination Generation",
            "url": "https://arxiv.org/pdf/2507.14239"
          },
          {
            "title": "[2507.14239] CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer Method for Mitigating Hallucination Generation",
            "url": "https://arxiv.org/abs/2507.14239"
          },
          {
            "title": "Accepted Findings Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/program/find_papers/"
          },
          {
            "title": "CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.93.pdf"
          },
          {
            "title": "Cross-Lingual Continuous Pretraining",
            "url": "https://www.emergentmind.com/topics/cross-lingual-continuous-pretraining"
          }
        ]
      },
      "I found relevant information about CCL-XCoT. Here's what the search results show:\n\n## Overview\n\nCCL-XCoT (Curriculum-based Contrastive Learning-based Cross-lingual Chain-of-Thought) is proposed by Weihua Zheng, Roy Ka-Wei Lee, Zhengyuan Liu, Kui Wu, AiTi Aw, and Bowei Zou from the Institute for Infocomm Research.\n\n## Problem and Approach\n\nMultilingual Large Language Models demonstrate strong generalization across languages, yet they remain prone to hallucinations, especially in low-resource languages, due to training data imbalances.\n\nCCL-XCoT is a two-stage fine-tuning framework for mitigating hallucination in MLLMs. The approach first enhances cross-lingual semantic alignment through curriculum-based contrastive learning combined with next-token prediction during continued pre-training. Then it introduces a cross-lingual Chain-of-Thought (XCoT) prompting strategy during instruction fine-tuning, which guides the model to reason in a high-resource language before generating answers in the target low-resource language.\n\n## Results\n\nExperimental results show that CCL-XCoT reduces hallucination rates by up to 62% and substantially improves factual knowledge transfer across language pairs, without relying on external retrieval or multi-model ensembles.\n\n## Publication\n\nThe paper was accepted as a Findings paper at EMNLP 2025."
    ],
    "durationSeconds": 8.995807243,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5266b378-4f6f-4958-80ce-f085a8b7c735",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T18:52:30.792Z_

<details><summary>↩ Tool result · `toolu_015CyVwwkWis9ffhTTL6a5mv`</summary>

```text
Web search results for query: "script barrier multilingual LLM cross-lingual knowledge transfer Bandarkar Ifergan 2025 2026"

Links: [{"title":"Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts","url":"https://arxiv.org/pdf/2603.17070"},{"title":"Crosslingual Capabilities and Knowledge Barriers in Multilingual Large Language Models | OpenReview","url":"https://openreview.net/forum?id=BCyAlMoyx5"},{"title":"Crosslingual Capabilities and Knowledge Barriers in Multilingual Large   Language Models","url":"https://arxiv.org/pdf/2406.16135"},{"title":"LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs","url":"https://arxiv.org/pdf/2511.14774"},{"title":"Breaking the Script Barrier in Multilingual Pre-Trained Language Models   with Transliteration-Based Post-Training Alignment","url":"https://arxiv.org/pdf/2406.19759"},{"title":"Crosslingual Capabilities and Knowledge Barriers in Multilingual Large Language Models","url":"https://arxiv.org/html/2406.16135v1"},{"title":"Understanding Cross-Lingual Inconsistency in Large Language Models","url":"https://arxiv.org/html/2505.13141v1"}]

Based on the search results, I found several relevant research papers on script barriers, multilingual LLMs, and cross-lingual knowledge transfer:

## Key Research Findings

A research paper by Lucas Bandarkar and colleagues analyzes shortcomings in cross-lingual knowledge transfer in large, modern reasoning LLMs, demonstrating that the perceived gap in knowledge transfer is primarily a script barrier. Their regression analysis shows that script match—not language or family—is the primary predictor of knowledge transfer failure once model capability and question difficulty are accounted for.

The researchers developed a synthetic generation pipeline to design supervised fine-tuning samples to encourage models to better reason about transliteration ambiguities when trying to fetch parametric knowledge at inference-time, and showed that teaching models to reason better reduces the cross-script transfer gap.

## Related Research

Research has observed that script diversity or the script barrier of represented languages hinders knowledge transfer, an issue that has been observed even in the case of related languages. Token representations from different scripts have been shown to be almost perfectly linearly separated, indicating that models struggle to learn a common representation space.

The search also returned papers by Ifergan and colleagues exploring cross-lingual knowledge representation sharing in LLMs, which aligns with your query about cross-lingual knowledge transfer research from 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b2a05c6-61b4-4f54-a2d2-884f27440ff5",
  "isSidechain": false,
  "promptId": "1f34f9d0-00e1-4c36-9ca2-ad9281ece0e9",
  "type": "user",
  "uuid": "e72e3be9-c06d-4423-bb42-adf1caffcd7b",
  "toolUseResult": {
    "query": "script barrier multilingual LLM cross-lingual knowledge transfer Bandarkar Ifergan 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PxrXEWtmmzPBW9Pzq7Enon",
        "content": [
          {
            "title": "Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts",
            "url": "https://arxiv.org/pdf/2603.17070"
          },
          {
            "title": "Crosslingual Capabilities and Knowledge Barriers in Multilingual Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=BCyAlMoyx5"
          },
          {
            "title": "Crosslingual Capabilities and Knowledge Barriers in Multilingual Large   Language Models",
            "url": "https://arxiv.org/pdf/2406.16135"
          },
          {
            "title": "LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs",
            "url": "https://arxiv.org/pdf/2511.14774"
          },
          {
            "title": "Breaking the Script Barrier in Multilingual Pre-Trained Language Models   with Transliteration-Based Post-Training Alignment",
            "url": "https://arxiv.org/pdf/2406.19759"
          },
          {
            "title": "Crosslingual Capabilities and Knowledge Barriers in Multilingual Large Language Models",
            "url": "https://arxiv.org/html/2406.16135v1"
          },
          {
            "title": "Understanding Cross-Lingual Inconsistency in Large Language Models",
            "url": "https://arxiv.org/html/2505.13141v1"
          }
        ]
      },
      "Based on the search results, I found several relevant research papers on script barriers, multilingual LLMs, and cross-lingual knowledge transfer:\n\n## Key Research Findings\n\nA research paper by Lucas Bandarkar and colleagues analyzes shortcomings in cross-lingual knowledge transfer in large, modern reasoning LLMs, demonstrating that the perceived gap in knowledge transfer is primarily a script barrier. Their regression analysis shows that script match—not language or family—is the primary predictor of knowledge transfer failure once model capability and question difficulty are accounted for.\n\nThe researchers developed a synthetic generation pipeline to design supervised fine-tuning samples to encourage models to better reason about transliteration ambiguities when trying to fetch parametric knowledge at inference-time, and showed that teaching models to reason better reduces the cross-script transfer gap.\n\n## Related Research\n\nResearch has observed that script diversity or the script barrier of represented languages hinders knowledge transfer, an issue that has been observed even in the case of related languages. Token representations from different scripts have been shown to be almost perfectly linearly separated, indicating that models struggle to learn a common representation space.\n\nThe search also returned papers by Ifergan and colleagues exploring cross-lingual knowledge representation sharing in LLMs, which aligns with your query about cross-lingual knowledge transfer research from 2025-2026."
    ],
    "durationSeconds": 8.009489313000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3b2a05c6-61b4-4f54-a2d2-884f27440ff5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T18:52:34.336Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pz51F5VoE66iU55xojpFcC`</summary>

```json
{
  "query": "Liu Niehues middle-layer representation alignment cross-lingual transfer ACL 2025 arXiv 2502.14830"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e72e3be9-c06d-4423-bb42-adf1caffcd7b",
  "isSidechain": false,
  "requestId": "req_011CbCS3TooMMQmRzuvWFJfV",
  "type": "assistant",
  "uuid": "b0a2dc43-f0f4-4778-9fe6-14c1cc4e41e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJnuLEA9y4aTnsSTFt9SEo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3983,
      "cache_read_input_tokens": 26820,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 26820,
          "cache_creation_input_tokens": 3983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3983
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

_source line 26 · 2026-05-19T18:52:35.198Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Drib3Fx18THd4xqxtzJ2Vo`</summary>

```json
{
  "query": "KBioXLM entity masking multilingual pretraining biomedical EMNLP 2023 cross-lingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0a2dc43-f0f4-4778-9fe6-14c1cc4e41e3",
  "isSidechain": false,
  "requestId": "req_011CbCS3TooMMQmRzuvWFJfV",
  "type": "assistant",
  "uuid": "e8041f82-0f59-4f50-b313-239382d4534c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJnuLEA9y4aTnsSTFt9SEo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3983,
      "cache_read_input_tokens": 26820,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 26820,
          "cache_creation_input_tokens": 3983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3983
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

_source line 27 · 2026-05-19T18:52:35.972Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NiJFWPJ2Vi1GhwYa6i7iXq`</summary>

```json
{
  "query": "entity-level contrastive alignment decoder LLM factual knowledge cross-lingual 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8041f82-0f59-4f50-b313-239382d4534c",
  "isSidechain": false,
  "requestId": "req_011CbCS3TooMMQmRzuvWFJfV",
  "type": "assistant",
  "uuid": "c28cf60d-1e38-4b8c-8a57-7d8a94a1e662",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJnuLEA9y4aTnsSTFt9SEo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3983,
      "cache_read_input_tokens": 26820,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 26820,
          "cache_creation_input_tokens": 3983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3983
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

_source line 28 · 2026-05-19T18:52:40.353Z_

<details><summary>↩ Tool result · `toolu_01Pz51F5VoE66iU55xojpFcC`</summary>

```text
Web search results for query: "Liu Niehues middle-layer representation alignment cross-lingual transfer ACL 2025 arXiv 2502.14830"

Links: [{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.778/"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | Request PDF","url":"https://www.researchgate.net/publication/394303200_Middle-Layer_Representation_Alignment_for_Cross-Lingual_Transfer_in_Fine-Tuned_LLMs"},{"title":"[2502.14830] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/abs/2502.14830"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual ...","url":"https://aclanthology.org/2025.acl-long.778.pdf"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/html/2502.14830v1"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in","url":"https://openreview.net/pdf/165a4c42ede4fa7182ef5ba60ec0669f5606b9b8.pdf"},{"title":"Can you map it to English? The Role of Cross-Lingual ...","url":"https://aclanthology.org/2026.eacl-long.225.pdf"},{"title":"[Literature Review] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://www.themoonlight.io/en/review/middle-layer-representation-alignment-for-cross-lingual-transfer-in-fine-tuned-llms"}]

I found the paper you're looking for! Here's what I found:

## Paper Overview

The paper "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs" by Danni Liu and Jan Niehues was published at the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) in Vienna, Austria.

## Key Findings

Through analysis of LLM internal representations from over 1,000+ language pairs, the authors discovered that middle layers exhibit the strongest potential for cross-lingual alignment. Building on this finding, they propose a middle-layer alignment objective integrated into task-specific training.

## Research Results

Their experiments on slot filling, machine translation, and structured text generation show consistent improvements in cross-lingual transfer, especially to lower-resource languages, and the method is robust to the choice of alignment languages and generalizes to languages unseen during alignment.

## ArXiv Details

The paper is available on arXiv as arXiv paper 2502.14830, submitted on February 20, 2025, with the latest version (v3) from June 2, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0a2dc43-f0f4-4778-9fe6-14c1cc4e41e3",
  "isSidechain": false,
  "promptId": "1f34f9d0-00e1-4c36-9ca2-ad9281ece0e9",
  "type": "user",
  "uuid": "fb859383-8bdb-4365-b9fa-42456cbdae91",
  "toolUseResult": {
    "query": "Liu Niehues middle-layer representation alignment cross-lingual transfer ACL 2025 arXiv 2502.14830",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PoY2vbPmMQH5AmkEieipXy",
        "content": [
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.778/"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | Request PDF",
            "url": "https://www.researchgate.net/publication/394303200_Middle-Layer_Representation_Alignment_for_Cross-Lingual_Transfer_in_Fine-Tuned_LLMs"
          },
          {
            "title": "[2502.14830] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs",
            "url": "https://arxiv.org/abs/2502.14830"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual ...",
            "url": "https://aclanthology.org/2025.acl-long.778.pdf"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs",
            "url": "https://arxiv.org/html/2502.14830v1"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in",
            "url": "https://openreview.net/pdf/165a4c42ede4fa7182ef5ba60ec0669f5606b9b8.pdf"
          },
          {
            "title": "Can you map it to English? The Role of Cross-Lingual ...",
            "url": "https://aclanthology.org/2026.eacl-long.225.pdf"
          },
          {
            "title": "[Literature Review] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs",
            "url": "https://www.themoonlight.io/en/review/middle-layer-representation-alignment-for-cross-lingual-transfer-in-fine-tuned-llms"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\n## Paper Overview\n\nThe paper \"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs\" by Danni Liu and Jan Niehues was published at the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) in Vienna, Austria.\n\n## Key Findings\n\nThrough analysis of LLM internal representations from over 1,000+ language pairs, the authors discovered that middle layers exhibit the strongest potential for cross-lingual alignment. Building on this finding, they propose a middle-layer alignment objective integrated into task-specific training.\n\n## Research Results\n\nTheir experiments on slot filling, machine translation, and structured text generation show consistent improvements in cross-lingual transfer, especially to lower-resource languages, and the method is robust to the choice of alignment languages and generalizes to languages unseen during alignment.\n\n## ArXiv Details\n\nThe paper is available on arXiv as arXiv paper 2502.14830, submitted on February 20, 2025, with the latest version (v3) from June 2, 2025."
    ],
    "durationSeconds": 6.013051708999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b0a2dc43-f0f4-4778-9fe6-14c1cc4e41e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T18:52:41.245Z_

<details><summary>↩ Tool result · `toolu_01Drib3Fx18THd4xqxtzJ2Vo`</summary>

```text
Web search results for query: "KBioXLM entity masking multilingual pretraining biomedical EMNLP 2023 cross-lingual"

Links: [{"title":"KBioXLM: A Knowledge-anchored Biomedical Multilingual Pretrained Language Model - ACL Anthology","url":"https://aclanthology.org/2023.findings-emnlp.751/"},{"title":"KBioXLM: A Knowledge-anchored Biomedical Multilingual Pretrained   Language Model","url":"https://arxiv.org/pdf/2311.11564"},{"title":"Paper page - KBioXLM: A Knowledge-anchored Biomedical Multilingual Pretrained Language Model","url":"https://huggingface.co/papers/2311.11564"},{"title":"[2311.11564] KBioXLM: A Knowledge-anchored Biomedical Multilingual Pretrained Language Model","url":"https://arxiv.org/abs/2311.11564"},{"title":"KBioXLM: A Knowledge-anchored Biomedical Multilingual Pretrained Language Model | OpenReview","url":"https://openreview.net/forum?id=JC7uPaMwpW"},{"title":"3RD MULTILINGUAL REPRESENTATION LEARNING (MRL) WORKSHOP @EMNLP 2023","url":"https://sigtyp.github.io/ws2023-mrl.html"},{"title":"Linguistic entity masking to improve cross-lingual representation of multilingual language models for low-resource languages | Knowledge and Information Systems","url":"https://link.springer.com/article/10.1007/s10115-025-02520-4"}]

Based on the search results, I found comprehensive information about KBioXLM:

KBioXLM is a Knowledge-anchored Biomedical Multilingual Pretrained Language Model published at EMNLP 2023. 

The model achieves a biomedical multilingual corpus by incorporating three granularity knowledge alignments (entity, fact, and passage levels) into monolingual corpora. The researchers design three corresponding training tasks (entity masking, relation masking, and passage relation prediction) and continue training on top of the XLM-R model to enhance its domain cross-lingual ability.

Experimental results demonstrate that the model significantly outperforms monolingual and multilingual pretrained models in cross-lingual zero-shot and few-shot scenarios, achieving improvements of up to 10+ points. To validate the effectiveness of the model, the authors translate the English benchmarks of multiple tasks into Chinese.

The model addresses a key challenge in the biomedical domain: the scarcity of non-English domain corpora, not to mention parallel data, poses a significant hurdle in training multilingual biomedical models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8041f82-0f59-4f50-b313-239382d4534c",
  "isSidechain": false,
  "promptId": "1f34f9d0-00e1-4c36-9ca2-ad9281ece0e9",
  "type": "user",
  "uuid": "feca55fd-5d67-4389-997c-b72d126c8977",
  "toolUseResult": {
    "query": "KBioXLM entity masking multilingual pretraining biomedical EMNLP 2023 cross-lingual",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SsZD3TQgp3975hzxHBdvyH",
        "content": [
          {
            "title": "KBioXLM: A Knowledge-anchored Biomedical Multilingual Pretrained Language Model - ACL Anthology",
            "url": "https://aclanthology.org/2023.findings-emnlp.751/"
          },
          {
            "title": "KBioXLM: A Knowledge-anchored Biomedical Multilingual Pretrained   Language Model",
            "url": "https://arxiv.org/pdf/2311.11564"
          },
          {
            "title": "Paper page - KBioXLM: A Knowledge-anchored Biomedical Multilingual Pretrained Language Model",
            "url": "https://huggingface.co/papers/2311.11564"
          },
          {
            "title": "[2311.11564] KBioXLM: A Knowledge-anchored Biomedical Multilingual Pretrained Language Model",
            "url": "https://arxiv.org/abs/2311.11564"
          },
          {
            "title": "KBioXLM: A Knowledge-anchored Biomedical Multilingual Pretrained Language Model | OpenReview",
            "url": "https://openreview.net/forum?id=JC7uPaMwpW"
          },
          {
            "title": "3RD MULTILINGUAL REPRESENTATION LEARNING (MRL) WORKSHOP @EMNLP 2023",
            "url": "https://sigtyp.github.io/ws2023-mrl.html"
          },
          {
            "title": "Linguistic entity masking to improve cross-lingual representation of multilingual language models for low-resource languages | Knowledge and Information Systems",
            "url": "https://link.springer.com/article/10.1007/s10115-025-02520-4"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about KBioXLM:\n\nKBioXLM is a Knowledge-anchored Biomedical Multilingual Pretrained Language Model published at EMNLP 2023. \n\nThe model achieves a biomedical multilingual corpus by incorporating three granularity knowledge alignments (entity, fact, and passage levels) into monolingual corpora. The researchers design three corresponding training tasks (entity masking, relation masking, and passage relation prediction) and continue training on top of the XLM-R model to enhance its domain cross-lingual ability.\n\nExperimental results demonstrate that the model significantly outperforms monolingual and multilingual pretrained models in cross-lingual zero-shot and few-shot scenarios, achieving improvements of up to 10+ points. To validate the effectiveness of the model, the authors translate the English benchmarks of multiple tasks into Chinese.\n\nThe model addresses a key challenge in the biomedical domain: the scarcity of non-English domain corpora, not to mention parallel data, poses a significant hurdle in training multilingual biomedical models."
    ],
    "durationSeconds": 6.043313939,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e8041f82-0f59-4f50-b313-239382d4534c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T18:52:43.872Z_

<details><summary>↩ Tool result · `toolu_01NiJFWPJ2Vi1GhwYa6i7iXq`</summary>

```text
Web search results for query: "entity-level contrastive alignment decoder LLM factual knowledge cross-lingual 2025 2026"

Links: [{"title":"On the Entity-Level Alignment in Crosslingual Consistency","url":"https://arxiv.org/pdf/2510.10280"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual ...","url":"https://aclanthology.org/2025.acl-long.778.pdf"},{"title":"When Language Shapes Thought: Cross-Lingual Transfer of Factual Knowledge in Question Answering","url":"https://arxiv.org/pdf/2505.24409"},{"title":"CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing","url":"https://arxiv.org/pdf/2601.17397"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/pdf/2502.14830"},{"title":"CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer Method for Mitigating Hallucination Generation","url":"https://arxiv.org/pdf/2507.14239"}]

I found several relevant research papers from 2025-2026 on this topic. Here's a summary of the search results:

The search returned multiple papers addressing cross-lingual alignment and factual knowledge in LLMs:

1. **Entity-Level Alignment in Crosslingual Consistency**: LLMs have demonstrated remarkable capabilities in multilingual tasks, including translation, question answering, and factual recall, with crosslingual consistency—the ability to recall the same fact correctly across different languages—emerging as a desirable property for evaluating multilingual LLMs. Entity alignment is important and facilitates consistent factual recall across languages.

2. **Middle-Layer Representation Alignment**: Recent work quantifies cross-lingual alignment in Llama 3 and Qwen 2.5, then applies insights to improve cross-lingual transfer in task-specific fine-tuning by alternatively training on alignment and task-specific data to improve cross-lingual generalization to languages without fine-tuning data.

3. **Cross-Lingual Factual Knowledge Transfer**: Aligning the model's internal thought with the knowledge required for the task is critical for successful cross-lingual transfer.

4. **Contrastive Learning Approaches**: Curriculum-based contrastive learning has been introduced to align multilingual semantic spaces, improving factual understanding and yielding up to 20% gains on crosslingual NLU tasks.

These papers collectively explore mechanisms for improving cross-lingual factual knowledge alignment in large language models through entity-level and representation-level approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c28cf60d-1e38-4b8c-8a57-7d8a94a1e662",
  "isSidechain": false,
  "promptId": "1f34f9d0-00e1-4c36-9ca2-ad9281ece0e9",
  "type": "user",
  "uuid": "6f4e9d7d-d53c-43b8-b58a-407918226bb1",
  "toolUseResult": {
    "query": "entity-level contrastive alignment decoder LLM factual knowledge cross-lingual 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Dx8wszzv2agt729cb3mYSw",
        "content": [
          {
            "title": "On the Entity-Level Alignment in Crosslingual Consistency",
            "url": "https://arxiv.org/pdf/2510.10280"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual ...",
            "url": "https://aclanthology.org/2025.acl-long.778.pdf"
          },
          {
            "title": "When Language Shapes Thought: Cross-Lingual Transfer of Factual Knowledge in Question Answering",
            "url": "https://arxiv.org/pdf/2505.24409"
          },
          {
            "title": "CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing",
            "url": "https://arxiv.org/pdf/2601.17397"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs",
            "url": "https://arxiv.org/pdf/2502.14830"
          },
          {
            "title": "CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer Method for Mitigating Hallucination Generation",
            "url": "https://arxiv.org/pdf/2507.14239"
          }
        ]
      },
      "I found several relevant research papers from 2025-2026 on this topic. Here's a summary of the search results:\n\nThe search returned multiple papers addressing cross-lingual alignment and factual knowledge in LLMs:\n\n1. **Entity-Level Alignment in Crosslingual Consistency**: LLMs have demonstrated remarkable capabilities in multilingual tasks, including translation, question answering, and factual recall, with crosslingual consistency—the ability to recall the same fact correctly across different languages—emerging as a desirable property for evaluating multilingual LLMs. Entity alignment is important and facilitates consistent factual recall across languages.\n\n2. **Middle-Layer Representation Alignment**: Recent work quantifies cross-lingual alignment in Llama 3 and Qwen 2.5, then applies insights to improve cross-lingual transfer in task-specific fine-tuning by alternatively training on alignment and task-specific data to improve cross-lingual generalization to languages without fine-tuning data.\n\n3. **Cross-Lingual Factual Knowledge Transfer**: Aligning the model's internal thought with the knowledge required for the task is critical for successful cross-lingual transfer.\n\n4. **Contrastive Learning Approaches**: Curriculum-based contrastive learning has been introduced to align multilingual semantic spaces, improving factual understanding and yielding up to 20% gains on crosslingual NLU tasks.\n\nThese papers collectively explore mechanisms for improving cross-lingual factual knowledge alignment in large language models through entity-level and representation-level approaches."
    ],
    "durationSeconds": 7.896786869999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c28cf60d-1e38-4b8c-8a57-7d8a94a1e662",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-19T18:52:43.883Z_

```json
{
  "parentUuid": "6f4e9d7d-d53c-43b8-b58a-407918226bb1",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9617045a-53cb-400c-8f18-658d1a6e33fd",
  "timestamp": "2026-05-19T18:52:43.883Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Entity-Anchored Contrastive Alignment for Cross-Lingual Knowledge Conductivity  ## Description EACA is a continu…",
  "leafUuid": "9617045a-53cb-400c-8f18-658d1a6e33fd",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate entity-level cross-lingual alignment proposal",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422"
}
```

---

### Tool call

_source line 34 · 2026-05-19T18:52:47.202Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011zFEsw9H6P8XNV4yNBthDa`</summary>

```json
{
  "query": "TransliCo transliteration contrastive learning script barrier multilingual ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9617045a-53cb-400c-8f18-658d1a6e33fd",
  "isSidechain": false,
  "requestId": "req_011CbCS4Rm3fwVnLo9Wp8Y7e",
  "type": "assistant",
  "uuid": "ba418849-9a0c-4d28-a37c-25a25fc32267",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXhs3bS76SW6PoyVwiRmKC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2504,
      "cache_read_input_tokens": 30803,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2504,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 30803,
          "cache_creation_input_tokens": 2504,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2504
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

### Tool call

_source line 35 · 2026-05-19T18:52:48.235Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NsGp66WMQ9Xo9kYbU3Ty2T`</summary>

```json
{
  "query": "DaMuEL multilingual entity linking dataset Wikidata QID 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba418849-9a0c-4d28-a37c-25a25fc32267",
  "isSidechain": false,
  "requestId": "req_011CbCS4Rm3fwVnLo9Wp8Y7e",
  "type": "assistant",
  "uuid": "99884cb3-2e4e-49d6-9e92-252b89a95a58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXhs3bS76SW6PoyVwiRmKC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2504,
      "cache_read_input_tokens": 30803,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2504,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 30803,
          "cache_creation_input_tokens": 2504,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2504
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

### Tool call

_source line 36 · 2026-05-19T18:52:48.813Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BxQxpuY3TmPxLR7wEm1Ujk`</summary>

```json
{
  "query": "cross-lingual factual consistency entity alignment training time improvement 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99884cb3-2e4e-49d6-9e92-252b89a95a58",
  "isSidechain": false,
  "requestId": "req_011CbCS4Rm3fwVnLo9Wp8Y7e",
  "type": "assistant",
  "uuid": "a5a30a4e-a8f3-40b4-8f90-5e4c0aef07ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXhs3bS76SW6PoyVwiRmKC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2504,
      "cache_read_input_tokens": 30803,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2504,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 30803,
          "cache_creation_input_tokens": 2504,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2504
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

_source line 37 · 2026-05-19T18:52:53.014Z_

<details><summary>↩ Tool result · `toolu_011zFEsw9H6P8XNV4yNBthDa`</summary>

```text
Web search results for query: "TransliCo transliteration contrastive learning script barrier multilingual ACL 2024"

Links: [{"title":"TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.136/"},{"title":"[2401.06620] TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models","url":"https://arxiv.org/abs/2401.06620"},{"title":"TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models","url":"https://www.emergentmind.com/papers/2401.06620"},{"title":"[PDF] TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TransliCo:-A-Contrastive-Learning-Framework-to-the-Liu-Ma/0bb0b4507683a0ad4271e1245234b80f03683f50"},{"title":"(PDF) TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models","url":"https://www.researchgate.net/publication/384214335_TransliCo_A_Contrastive_Learning_Framework_to_Address_the_Script_Barrier_in_Multilingual_Pretrained_Language_Models"},{"title":"publications | Yihong Liu (刘一宏)","url":"https://yihongl1u.github.io/publications/"},{"title":"TransliCo: A Contrastive Learning Framework to Address the Script   Barrier in Multilingual Pretrained Language Models","url":"https://arxiv.org/pdf/2401.06620"},{"title":"TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models","url":"https://arxiv.org/html/2401.06620v1"}]

Based on the search results, I found relevant information about TransliCo:

TransliCo is a Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models, presented at the 62nd Annual Meeting of the Association for Computational Linguistics (ACL 2024) in Bangkok, Thailand.

Many closely related languages use different scripts, which poses difficulty for multilingual pretrained language models (mPLMs) in learning crosslingual knowledge through lexical overlap, resulting in a script barrier where representations from different scripts are located in different subspaces.

TransliCo is a framework that optimizes the Transliteration Contrastive Modeling (TCM) objective to fine-tune an mPLM by contrasting sentences in its training data and their transliterations in a unified script (Latin), which enhances uniformity in the representation space for different scripts.

Using Glot500-m, an mPLM pretrained on over 500 languages, as the source model, the framework was fine-tuned on 5% of its training data to create Furina, which better aligns representations from distinct scripts and outperforms the original Glot500-m on various zero-shot crosslingual transfer tasks.

The paper was authored by Yihong Liu, Chunlan Ma, Haotian Ye, and Hinrich Schütze from the Center for Information and Language Processing at LMU Munich.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba418849-9a0c-4d28-a37c-25a25fc32267",
  "isSidechain": false,
  "promptId": "1f34f9d0-00e1-4c36-9ca2-ad9281ece0e9",
  "type": "user",
  "uuid": "f00b4deb-a610-40dd-b358-c35de2a4bb70",
  "toolUseResult": {
    "query": "TransliCo transliteration contrastive learning script barrier multilingual ACL 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PddGYw3ErSawydw9hsfGYv",
        "content": [
          {
            "title": "TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.acl-long.136/"
          },
          {
            "title": "[2401.06620] TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models",
            "url": "https://arxiv.org/abs/2401.06620"
          },
          {
            "title": "TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models",
            "url": "https://www.emergentmind.com/papers/2401.06620"
          },
          {
            "title": "[PDF] TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/TransliCo:-A-Contrastive-Learning-Framework-to-the-Liu-Ma/0bb0b4507683a0ad4271e1245234b80f03683f50"
          },
          {
            "title": "(PDF) TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models",
            "url": "https://www.researchgate.net/publication/384214335_TransliCo_A_Contrastive_Learning_Framework_to_Address_the_Script_Barrier_in_Multilingual_Pretrained_Language_Models"
          },
          {
            "title": "publications | Yihong Liu (刘一宏)",
            "url": "https://yihongl1u.github.io/publications/"
          },
          {
            "title": "TransliCo: A Contrastive Learning Framework to Address the Script   Barrier in Multilingual Pretrained Language Models",
            "url": "https://arxiv.org/pdf/2401.06620"
          },
          {
            "title": "TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models",
            "url": "https://arxiv.org/html/2401.06620v1"
          }
        ]
      },
      "Based on the search results, I found relevant information about TransliCo:\n\nTransliCo is a Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models, presented at the 62nd Annual Meeting of the Association for Computational Linguistics (ACL 2024) in Bangkok, Thailand.\n\nMany closely related languages use different scripts, which poses difficulty for multilingual pretrained language models (mPLMs) in learning crosslingual knowledge through lexical overlap, resulting in a script barrier where representations from different scripts are located in different subspaces.\n\nTransliCo is a framework that optimizes the Transliteration Contrastive Modeling (TCM) objective to fine-tune an mPLM by contrasting sentences in its training data and their transliterations in a unified script (Latin), which enhances uniformity in the representation space for different scripts.\n\nUsing Glot500-m, an mPLM pretrained on over 500 languages, as the source model, the framework was fine-tuned on 5% of its training data to create Furina, which better aligns representations from distinct scripts and outperforms the original Glot500-m on various zero-shot crosslingual transfer tasks.\n\nThe paper was authored by Yihong Liu, Chunlan Ma, Haotian Ye, and Hinrich Schütze from the Center for Information and Language Processing at LMU Munich."
    ],
    "durationSeconds": 5.808782503000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ba418849-9a0c-4d28-a37c-25a25fc32267",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T18:52:54.120Z_

<details><summary>↩ Tool result · `toolu_01NsGp66WMQ9Xo9kYbU3Ty2T`</summary>

```text
Web search results for query: "DaMuEL multilingual entity linking dataset Wikidata QID 2023"

Links: [{"title":"[2306.09288] DaMuEL: A Large Multilingual Dataset for Entity Linking","url":"https://arxiv.org/abs/2306.09288"},{"title":"DaMuEL: A Large Multilingual Dataset for Entity Linking","url":"https://arxiv.org/pdf/2306.09288"},{"title":"DaMuEL 1.0: A Large Multilingual Dataset for Entity Linking","url":"https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-5047"},{"title":"DaMuEL 1.0: A Large Multilingual Dataset for Entity Linking - Dataset - B2FIND","url":"https://b2find.eudat.eu/dataset/68113207-3ac4-5d3f-9bc6-16e571879b23"},{"title":"DaMuEL: A Large Multilingual Dataset for Entity Linking | Request PDF","url":"https://www.researchgate.net/publication/371606524_DaMuEL_A_Large_Multilingual_Dataset_for_Entity_Linking"},{"title":"DaMuEL: A Large Multilingual Dataset for Entity Linking","url":"https://arxiv.org/html/2306.09288"},{"title":"DLnLD: Deep Learning and Linked Data @LREC-COLING-2024, pages 31–44","url":"https://aclanthology.org/2024.dlnld-1.3.pdf"}]

Based on the search results, here's information about the DaMuEL multilingual entity linking dataset:

DaMuEL is a large multilingual dataset for entity linking containing data in 53 languages. The dataset consists of two components: a knowledge base that contains language-agnostic information about entities, including their claims from Wikidata and named entity types (PER, ORG, LOC, EVENT, BRAND, WORK_OF_ART, MANUFACTURED); and Wikipedia texts with entity mentions linked to the knowledge base, along with language-specific text from Wikidata such as labels, aliases, and descriptions, stored separately for each language.

The Wikidata QID is used as a persistent, language-agnostic identifier, enabling the combination of the knowledge base with language-specific texts and information for each entity. The dataset contains 27.9M named entities in the knowledge base and 12.3G tokens from Wikipedia texts. 

The dataset is published under the CC BY-SA license, and the paper was submitted in June 2023.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99884cb3-2e4e-49d6-9e92-252b89a95a58",
  "isSidechain": false,
  "promptId": "1f34f9d0-00e1-4c36-9ca2-ad9281ece0e9",
  "type": "user",
  "uuid": "d1ea4ea6-5672-42f4-8e9c-1ed0ac588ada",
  "toolUseResult": {
    "query": "DaMuEL multilingual entity linking dataset Wikidata QID 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L1WRrCVefTvRaVdfqRJQLJ",
        "content": [
          {
            "title": "[2306.09288] DaMuEL: A Large Multilingual Dataset for Entity Linking",
            "url": "https://arxiv.org/abs/2306.09288"
          },
          {
            "title": "DaMuEL: A Large Multilingual Dataset for Entity Linking",
            "url": "https://arxiv.org/pdf/2306.09288"
          },
          {
            "title": "DaMuEL 1.0: A Large Multilingual Dataset for Entity Linking",
            "url": "https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-5047"
          },
          {
            "title": "DaMuEL 1.0: A Large Multilingual Dataset for Entity Linking - Dataset - B2FIND",
            "url": "https://b2find.eudat.eu/dataset/68113207-3ac4-5d3f-9bc6-16e571879b23"
          },
          {
            "title": "DaMuEL: A Large Multilingual Dataset for Entity Linking | Request PDF",
            "url": "https://www.researchgate.net/publication/371606524_DaMuEL_A_Large_Multilingual_Dataset_for_Entity_Linking"
          },
          {
            "title": "DaMuEL: A Large Multilingual Dataset for Entity Linking",
            "url": "https://arxiv.org/html/2306.09288"
          },
          {
            "title": "DLnLD: Deep Learning and Linked Data @LREC-COLING-2024, pages 31–44",
            "url": "https://aclanthology.org/2024.dlnld-1.3.pdf"
          }
        ]
      },
      "Based on the search results, here's information about the DaMuEL multilingual entity linking dataset:\n\nDaMuEL is a large multilingual dataset for entity linking containing data in 53 languages. The dataset consists of two components: a knowledge base that contains language-agnostic information about entities, including their claims from Wikidata and named entity types (PER, ORG, LOC, EVENT, BRAND, WORK_OF_ART, MANUFACTURED); and Wikipedia texts with entity mentions linked to the knowledge base, along with language-specific text from Wikidata such as labels, aliases, and descriptions, stored separately for each language.\n\nThe Wikidata QID is used as a persistent, language-agnostic identifier, enabling the combination of the knowledge base with language-specific texts and information for each entity. The dataset contains 27.9M named entities in the knowledge base and 12.3G tokens from Wikipedia texts. \n\nThe dataset is published under the CC BY-SA license, and the paper was submitted in June 2023."
    ],
    "durationSeconds": 5.881573803999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "99884cb3-2e4e-49d6-9e92-252b89a95a58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T18:52:58.670Z_

<details><summary>↩ Tool result · `toolu_01BxQxpuY3TmPxLR7wEm1Ujk`</summary>

```text
Web search results for query: "cross-lingual factual consistency entity alignment training time improvement 2025 2026 arXiv"

Links: [{"title":"[2510.10280] On the Entity-Level Alignment in Crosslingual Consistency","url":"https://arxiv.org/abs/2510.10280"},{"title":"On the Entity-Level Alignment in Crosslingual Consistency","url":"https://arxiv.org/html/2510.10280"},{"title":"Cross-Lingual Consistency in Multilingual Models","url":"https://www.emergentmind.com/topics/cross-lingual-consistency-clc"},{"title":"Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation","url":"https://arxiv.org/html/2605.12515"},{"title":"Multilingual Factual Consistency Evaluation","url":"https://www.emergentmind.com/topics/multilingual-factual-consistency-evaluation"},{"title":"On the Entity-Level Alignment in Crosslingual Consistency","url":"https://arxiv.org/pdf/2510.10280"},{"title":"Traveling Across Languages: Benchmarking Cross-Lingual Consistency in Multimodal LLMs","url":"https://arxiv.org/html/2505.15075v1"}]

Based on the search results, I found several relevant papers and resources on cross-lingual factual consistency and entity alignment from 2025-2026:

## Key Findings:

**Recent arXiv Paper (October 2025):**

A paper on entity-level alignment in cross-lingual consistency found that consistency is strongly correlated with entity alignment, and proposed SubSub and SubInj methods that integrate English translations of subjects into prompts, leading to substantial gains in both factual recall accuracy and consistency.

**Training and Methodological Improvements:**

Cross-lingual word alignment objectives and code-switching training are among the most effective strategies for boosting knowledge consistency and performance parity. Additionally, prior work has proposed various training interventions, such as constructing multilingual parallel batches and applying contrastive learning to align internal representations.

**Mechanistic Insights:**

Mechanistic analysis reveals that these interventions reinforce entity representation alignment in the conceptual space through the model's internal pivot-language processing, offering practical strategies for improving multilingual factual prediction.

**Additional Context:**

The SubInj and SubSub prompt-engineering interventions effectively boost both cross-lingual factual recall and answer consistency, especially for low-resource or non-Latin scripts.

The search results show active research in this area with multiple papers from 2025-2026 exploring entity alignment as a key factor for improving cross-lingual factual consistency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5a30a4e-a8f3-40b4-8f90-5e4c0aef07ea",
  "isSidechain": false,
  "promptId": "1f34f9d0-00e1-4c36-9ca2-ad9281ece0e9",
  "type": "user",
  "uuid": "1c8a8b78-f963-41ce-86db-3eaeb8f120e8",
  "toolUseResult": {
    "query": "cross-lingual factual consistency entity alignment training time improvement 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AKiJzqwht7r5MUUuYMJoUR",
        "content": [
          {
            "title": "[2510.10280] On the Entity-Level Alignment in Crosslingual Consistency",
            "url": "https://arxiv.org/abs/2510.10280"
          },
          {
            "title": "On the Entity-Level Alignment in Crosslingual Consistency",
            "url": "https://arxiv.org/html/2510.10280"
          },
          {
            "title": "Cross-Lingual Consistency in Multilingual Models",
            "url": "https://www.emergentmind.com/topics/cross-lingual-consistency-clc"
          },
          {
            "title": "Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation",
            "url": "https://arxiv.org/html/2605.12515"
          },
          {
            "title": "Multilingual Factual Consistency Evaluation",
            "url": "https://www.emergentmind.com/topics/multilingual-factual-consistency-evaluation"
          },
          {
            "title": "On the Entity-Level Alignment in Crosslingual Consistency",
            "url": "https://arxiv.org/pdf/2510.10280"
          },
          {
            "title": "Traveling Across Languages: Benchmarking Cross-Lingual Consistency in Multimodal LLMs",
            "url": "https://arxiv.org/html/2505.15075v1"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and resources on cross-lingual factual consistency and entity alignment from 2025-2026:\n\n## Key Findings:\n\n**Recent arXiv Paper (October 2025):**\n\nA paper on entity-level alignment in cross-lingual consistency found that consistency is strongly correlated with entity alignment, and proposed SubSub and SubInj methods that integrate English translations of subjects into prompts, leading to substantial gains in both factual recall accuracy and consistency.\n\n**Training and Methodological Improvements:**\n\nCross-lingual word alignment objectives and code-switching training are among the most effective strategies for boosting knowledge consistency and performance parity. Additionally, prior work has proposed various training interventions, such as constructing multilingual parallel batches and applying contrastive learning to align internal representations.\n\n**Mechanistic Insights:**\n\nMechanistic analysis reveals that these interventions reinforce entity representation alignment in the conceptual space through the model's internal pivot-language processing, offering practical strategies for improving multilingual factual prediction.\n\n**Additional Context:**\n\nThe SubInj and SubSub prompt-engineering interventions effectively boost both cross-lingual factual recall and answer consistency, especially for low-resource or non-Latin scripts.\n\nThe search results show active research in this area with multiple papers from 2025-2026 exploring entity alignment as a key factor for improving cross-lingual factual consistency."
    ],
    "durationSeconds": 9.854481957999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a5a30a4e-a8f3-40b4-8f90-5e4c0aef07ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-19T18:53:02.176Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the field. Let me also search for any direct competitors that might be doing something very similar to EACA - entity-level contrastive alignment during continued pretraining for cross-lingual factual consistency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c8a8b78-f963-41ce-86db-3eaeb8f120e8",
  "isSidechain": false,
  "requestId": "req_011CbCS5WxcVK2P2fXyLASWk",
  "type": "assistant",
  "uuid": "a172351b-5cd0-48c7-8be7-367a79ee56f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3DJoz7aLawPXAfxLtRyr1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4948,
      "cache_read_input_tokens": 30803,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 30803,
          "cache_creation_input_tokens": 4948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4948
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-19T18:53:03.147Z_

Let me do one more targeted search to check for any very close competitors doing entity-level contrastive CPT.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a172351b-5cd0-48c7-8be7-367a79ee56f1",
  "isSidechain": false,
  "requestId": "req_011CbCS5WxcVK2P2fXyLASWk",
  "type": "assistant",
  "uuid": "f80a11e2-3330-4b23-a898-1fa1f0f63c6f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3DJoz7aLawPXAfxLtRyr1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4948,
      "cache_read_input_tokens": 30803,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 30803,
          "cache_creation_input_tokens": 4948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4948
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-19T18:53:04.106Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xf9kj856o691dJoDioRdoj`</summary>

```json
{
  "query": "\"entity contrastive\" \"continued pretraining\" OR \"continual pretraining\" cross-lingual decoder LLM Wikidata 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f80a11e2-3330-4b23-a898-1fa1f0f63c6f",
  "isSidechain": false,
  "requestId": "req_011CbCS5WxcVK2P2fXyLASWk",
  "type": "assistant",
  "uuid": "6c55e61b-6a28-4763-a5ae-dfad6c73c49f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3DJoz7aLawPXAfxLtRyr1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4948,
      "cache_read_input_tokens": 30803,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 30803,
          "cache_creation_input_tokens": 4948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4948
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T18:53:04.397Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014ku7eu2wGJucTcjbJYJfF4`</summary>

```json
{
  "query": "LEIA entity augmentation cross-lingual LLM ACL 2024 decoder continued pretraining"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c55e61b-6a28-4763-a5ae-dfad6c73c49f",
  "isSidechain": false,
  "requestId": "req_011CbCS5WxcVK2P2fXyLASWk",
  "type": "assistant",
  "uuid": "b1204665-03ec-4b3c-a369-7e4b000004cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3DJoz7aLawPXAfxLtRyr1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4948,
      "cache_read_input_tokens": 30803,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 30803,
          "cache_creation_input_tokens": 4948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4948
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T18:53:11.889Z_

<details><summary>↩ Tool result · `toolu_014ku7eu2wGJucTcjbJYJfF4`</summary>

```text
Web search results for query: "LEIA entity augmentation cross-lingual LLM ACL 2024 decoder continued pretraining"

Links: [{"title":"LEIA: Facilitating Cross-Lingual Knowledge Transfer in Language Models with Entity-based Data Augmentation","url":"https://arxiv.org/html/2402.11485v1"},{"title":"LEIA: Facilitating Cross-lingual Knowledge Transfer in Language Models with Entity-based Data Augmentation - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.419/"},{"title":"Enhancing LLM Language Adaption through Cross-lingual ...","url":"https://aclanthology.org/2025.emnlp-main.1380.pdf"},{"title":"Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training","url":"https://arxiv.org/html/2504.20484"},{"title":"[2402.11485] LEIA: Facilitating Cross-lingual Knowledge Transfer in Language Models with Entity-based Data Augmentation","url":"https://arxiv.org/abs/2402.11485"},{"title":"LEIA: Facilitating Cross-lingual Knowledge Transfer in Language Models   with Entity-based Data Augmentation","url":"https://arxiv.org/pdf/2402.11485"},{"title":"Large Vocabulary Size Improves Large Language Models","url":"https://arxiv.org/html/2406.16508v1"},{"title":"Cross-Lingual Continuous Pretraining","url":"https://www.emergentmind.com/topics/cross-lingual-continuous-pretraining"}]

Based on the search results, here's what I found about LEIA:

## LEIA Overview

LEIA is a language adaptation tuning method that utilizes Wikipedia entity names aligned across languages, involving augmenting the target language corpus with English entity names and training the model using left-to-right language modeling.

## Key Details

**Purpose and Motivation:**
LEIA was designed to address the popularity of adapting English-based large language models to other languages through cross-lingual transfer, as existing language adaptation methods often overlook the benefits of cross-lingual supervision.

**Technical Approach:**
For each hyperlink in the Wikipedia corpus, the English name of the referred entity is inserted next to the hyperlink, enclosed within special `&lt;translate>` and `&lt;/translate>` tokens, with the English name extracted from the corresponding English Wikipedia page identified using interlanguage links.

**Performance and Publication:**
LEIA was assessed on diverse question answering datasets using 7B-parameter LLMs, demonstrating significant performance gains across various non-English languages. The paper was published in the Findings of the Association for Computational Linguistics: ACL 2024 in Bangkok, Thailand.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1204665-03ec-4b3c-a369-7e4b000004cc",
  "isSidechain": false,
  "promptId": "1f34f9d0-00e1-4c36-9ca2-ad9281ece0e9",
  "type": "user",
  "uuid": "3f0cd52d-1fbe-4084-9899-2f648c00252c",
  "toolUseResult": {
    "query": "LEIA entity augmentation cross-lingual LLM ACL 2024 decoder continued pretraining",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MpoTpxj6hXmEyhLkuB6Htb",
        "content": [
          {
            "title": "LEIA: Facilitating Cross-Lingual Knowledge Transfer in Language Models with Entity-based Data Augmentation",
            "url": "https://arxiv.org/html/2402.11485v1"
          },
          {
            "title": "LEIA: Facilitating Cross-lingual Knowledge Transfer in Language Models with Entity-based Data Augmentation - ACL Anthology",
            "url": "https://aclanthology.org/2024.findings-acl.419/"
          },
          {
            "title": "Enhancing LLM Language Adaption through Cross-lingual ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1380.pdf"
          },
          {
            "title": "Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training",
            "url": "https://arxiv.org/html/2504.20484"
          },
          {
            "title": "[2402.11485] LEIA: Facilitating Cross-lingual Knowledge Transfer in Language Models with Entity-based Data Augmentation",
            "url": "https://arxiv.org/abs/2402.11485"
          },
          {
            "title": "LEIA: Facilitating Cross-lingual Knowledge Transfer in Language Models   with Entity-based Data Augmentation",
            "url": "https://arxiv.org/pdf/2402.11485"
          },
          {
            "title": "Large Vocabulary Size Improves Large Language Models",
            "url": "https://arxiv.org/html/2406.16508v1"
          },
          {
            "title": "Cross-Lingual Continuous Pretraining",
            "url": "https://www.emergentmind.com/topics/cross-lingual-continuous-pretraining"
          }
        ]
      },
      "Based on the search results, here's what I found about LEIA:\n\n## LEIA Overview\n\nLEIA is a language adaptation tuning method that utilizes Wikipedia entity names aligned across languages, involving augmenting the target language corpus with English entity names and training the model using left-to-right language modeling.\n\n## Key Details\n\n**Purpose and Motivation:**\nLEIA was designed to address the popularity of adapting English-based large language models to other languages through cross-lingual transfer, as existing language adaptation methods often overlook the benefits of cross-lingual supervision.\n\n**Technical Approach:**\nFor each hyperlink in the Wikipedia corpus, the English name of the referred entity is inserted next to the hyperlink, enclosed within special `&lt;translate>` and `&lt;/translate>` tokens, with the English name extracted from the corresponding English Wikipedia page identified using interlanguage links.\n\n**Performance and Publication:**\nLEIA was assessed on diverse question answering datasets using 7B-parameter LLMs, demonstrating significant performance gains across various non-English languages. The paper was published in the Findings of the Association for Computational Linguistics: ACL 2024 in Bangkok, Thailand."
    ],
    "durationSeconds": 7.486565217999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b1204665-03ec-4b3c-a369-7e4b000004cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Entity-Anchored Contrastive Alignment for Cross-Lingual Knowledge Conductivity  ## Description EACA is a continu…",
  "leafUuid": "3f0cd52d-1fbe-4084-9899-2f648c00252c",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate entity-level cross-lingual alignment proposal",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422"
}
```

---

### Tool result

_source line 47 · 2026-05-19T18:53:12.833Z_

<details><summary>↩ Tool result · `toolu_01Xf9kj856o691dJoDioRdoj`</summary>

```text
Web search results for query: ""entity contrastive" "continued pretraining" OR "continual pretraining" cross-lingual decoder LLM Wikidata 2025 2026"

Links: [{"title":"Cross-Lingual Continuous Pretraining","url":"https://www.emergentmind.com/topics/cross-lingual-continuous-pretraining"},{"title":"Cross-lingual Transfer Learning","url":"https://www.emergentmind.com/topics/cross-lingual-transfer-learning-63a7cac1-c2ae-4704-8e27-a49a3951a0c1"},{"title":"Exploring Pretraining via Active Forgetting for Improving Cross Lingual Transfer for Decoder Language Models","url":"https://arxiv.org/html/2410.16168"},{"title":"Continual Pre-Training for Cross-Lingual LLM Adaptation: Enhancing Japanese Language Capabilities","url":"https://arxiv.org/html/2404.17790v1"},{"title":"Improving Self-training for Cross-lingual Named Entity Recognition with   Contrastive and Prototype Learning","url":"https://arxiv.org/pdf/2305.13628"},{"title":"C3: Continued Pretraining with Contrastive Weak Supervision for Cross   Language Ad-Hoc Retrieval","url":"https://arxiv.org/pdf/2204.11989"}]

Based on the web search results, I found several relevant research papers and topics related to your query:

## Key Findings:

Comparable corpora (Wikipedia interwiki links, retrieved web passages) can serve for weak contrastive supervision in cross-lingual pretraining where parallel data is scarce.

Encoder-decoder (mBART, mT5, XLM) and decoder-only (LLaMA, BLOOM, XGLM) architectures each support cross-lingual adaptation.

There is a particularly relevant paper titled "C3: Continued Pretraining with Contrastive Weak Supervision for Cross Language Ad-Hoc Retrieval", which directly addresses the combination of continued pretraining with contrastive methods. This work uses comparable Wikipedia articles in different languages to further pretrain multilingual pretrained models.

Additionally, research from early 2025 discusses semantic retrieval extending the availability of in-context pairs beyond strict factual overlap, enabling large-scale augmentation of cross-lingual contexts using embeddings and approximate nearest neighbor search.

There's also work on continual pre-training for cross-lingual LLM adaptation, with vocabulary expansion being a main motivation for improving training and generation capabilities.

The search results contain recent material from 2025-2026 covering cross-lingual decoder LLMs with continued/continual pretraining approaches, though the specific combination of all your search terms (entity contrastive with Wikidata) was not explicitly highlighted in these particular results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c55e61b-6a28-4763-a5ae-dfad6c73c49f",
  "isSidechain": false,
  "promptId": "1f34f9d0-00e1-4c36-9ca2-ad9281ece0e9",
  "type": "user",
  "uuid": "7923f9b2-257e-4b27-9cdb-080e9ed74194",
  "toolUseResult": {
    "query": "\"entity contrastive\" \"continued pretraining\" OR \"continual pretraining\" cross-lingual decoder LLM Wikidata 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014vT4W4J7bohcSE3fKHMkZc",
        "content": [
          {
            "title": "Cross-Lingual Continuous Pretraining",
            "url": "https://www.emergentmind.com/topics/cross-lingual-continuous-pretraining"
          },
          {
            "title": "Cross-lingual Transfer Learning",
            "url": "https://www.emergentmind.com/topics/cross-lingual-transfer-learning-63a7cac1-c2ae-4704-8e27-a49a3951a0c1"
          },
          {
            "title": "Exploring Pretraining via Active Forgetting for Improving Cross Lingual Transfer for Decoder Language Models",
            "url": "https://arxiv.org/html/2410.16168"
          },
          {
            "title": "Continual Pre-Training for Cross-Lingual LLM Adaptation: Enhancing Japanese Language Capabilities",
            "url": "https://arxiv.org/html/2404.17790v1"
          },
          {
            "title": "Improving Self-training for Cross-lingual Named Entity Recognition with   Contrastive and Prototype Learning",
            "url": "https://arxiv.org/pdf/2305.13628"
          },
          {
            "title": "C3: Continued Pretraining with Contrastive Weak Supervision for Cross   Language Ad-Hoc Retrieval",
            "url": "https://arxiv.org/pdf/2204.11989"
          }
        ]
      },
      "Based on the web search results, I found several relevant research papers and topics related to your query:\n\n## Key Findings:\n\nComparable corpora (Wikipedia interwiki links, retrieved web passages) can serve for weak contrastive supervision in cross-lingual pretraining where parallel data is scarce.\n\nEncoder-decoder (mBART, mT5, XLM) and decoder-only (LLaMA, BLOOM, XGLM) architectures each support cross-lingual adaptation.\n\nThere is a particularly relevant paper titled \"C3: Continued Pretraining with Contrastive Weak Supervision for Cross Language Ad-Hoc Retrieval\", which directly addresses the combination of continued pretraining with contrastive methods. This work uses comparable Wikipedia articles in different languages to further pretrain multilingual pretrained models.\n\nAdditionally, research from early 2025 discusses semantic retrieval extending the availability of in-context pairs beyond strict factual overlap, enabling large-scale augmentation of cross-lingual contexts using embeddings and approximate nearest neighbor search.\n\nThere's also work on continual pre-training for cross-lingual LLM adaptation, with vocabulary expansion being a main motivation for improving training and generation capabilities.\n\nThe search results contain recent material from 2025-2026 covering cross-lingual decoder LLMs with continued/continual pretraining approaches, though the specific combination of all your search terms (entity contrastive with Wikidata) was not explicitly highlighted in these particular results."
    ],
    "durationSeconds": 8.723657171,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6c55e61b-6a28-4763-a5ae-dfad6c73c49f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-19T18:54:16.115Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of the field. Let me synthesize my analysis:

## Field Landscape Summary

1. **CLiKA (NAACL 2024)** - Established that cross-lingual knowledge conductivity (XRR < 0.01) is not improved by existing multilingual pretraining or instruction tuning. This is a real, confirmed finding.

2. **CCL-XCoT (EMNLP 2025 Findings)** - Sentence/paragraph-level contrastive CPT that reduces hallucination by up to 62%. Operates at sentence/paragraph granularity.
   
3. **Liu & Niehues (ACL 2025)** - Uses middle-layer contrastive alignment during task-specific fine-tuning, with layer 16 emerging as the optimal depth.

4. **KBioXLM (EMNLP Findings 2023)** - Applies entity masking on the encoder side in biomedical contexts, demonstrating that entity-level alignment strengthens cross-lingual transfer.

5. **Entity-Level Alignment (arXiv:2510.10280)** - Demonstrates strong correlation (r > 0.7) between entity alignment and cross-lingual consistency, though their SubInj approach only works at inference time.

6. **Script Barrier** - [thinking appears to continue]

7. **TransliCo (ACL 2024)** - Uses transliteration-based contrastive learning on encoders to overcome script barriers.

8. **FactNet (arXiv 2026)** - A substantial resource containing 1.7B entity-grounded atomic facts.

9. **DaMuEL (2023)** - Another major resource with 12.3B QID-annotated tokens spanning 53 languages.

10. **LEIA (ACL 2024)** - Performs entity-based data augmentation using English entity names, but without contrastive loss.

Now I'm looking at the novelty angle—the core distinction here is that entity-level contrastive alignment during training differs from the sentence or paragraph-level approaches others have explored.

The genuinely novel aspects are the specific pairing of entity-level contrastive loss with decoder LLMs during continued pretraining, leveraging FactNet's structured facts to build those entity pairs, and combining transliteration augmentation with this entity-focused contrastive framework. However, the proposal largely recombines existing techniques—contrastive continued pretraining from prior work, middle-layer extraction methods, entity anchoring strategies from knowledge-based approaches, transliteration handling, and structured knowledge integration. The underlying hypothesis that entity-level alignment outperforms sentence-level for factual knowledge transfer is the central claim, but it's built from established components rather than introducing fundamentally new mechanisms.

I'm now questioning whether this approach offers meaningful advantages over simpler alternatives. SubInj achieves substantial gains just by inserting English entity names at inference time without any training modifications, which raises the question of whether the training-time investment in EACA provides enough additional value. Similarly, LEIA already does entity augmentation during continued pretraining and shows strong results—so the critical question becomes whether adding contrastive loss is the real differentiator or if basic entity augmentation alone would be sufficient as a baseline.

The core problem is legitimate and CLiKA's finding about existing methods failing to improve cross-lingual retrieval is a genuine gap, but the actual marginal improvement from entity-level contrastive alignment over simpler approaches like CCL-XCoT combined with LEIA-style augmentation remains unclear. The pipeline's complexity—requiring DaMuEL, FactNet, mReFinED, and transliteration—also limits practical applicability.

The related work section is impressively comprehensive and positions the work clearly against all major competitors, but this thoroughness inadvertently highlights how many existing pieces the proposal is building on, which somewhat undermines the novelty claim.

The real vulnerability is that this feels like an engineered synthesis of six to eight existing techniques—entity markers, contrastive losses, middle-layer fusion, entity grounding, transliteration, structured data integration, gradient surgery, and frequency weighting—assembled to address a specific granularity gap. Reviewers might view this as a clever combination of known methods rather than a fundamentally new contribution, and if results are positive, the response could be "this was predictable given what we already know about entity alignment." The core issue is that entity-level alignment improving consistency feels almost inevitable given the correlation evidence, which makes the contribution feel incremental. There are simpler alternatives that could achieve similar results without the added complexity, and the pipeline's many moving parts make it hard to isolate what's actually driving improvements. Stepping back to evaluate this for a top NLP venue rather than robotics, the idea addresses a real gap but the assembly-of-existing-pieces nature combined with the predictability of the main finding caps how novel it feels — I'd estimate this lands around 25% probability of acceptance. I think the user likely meant COLM or another top NLP venue rather than CoRL, so I'll evaluate this for the NLP/CL community. The idea is methodologically sound and addresses a real problem, but the core insight—that entity-level alignment improves cross-lingual consistency—is fairly predictable and already somewhat established in the literature. The contribution feels more like careful engineering than a conceptual breakthrough, so I'm settling on around 30% probability for acceptance at a top venue.

But I should reconsider this estimate upward slightly. The fact that EACA targets CLiKA's XRR metric where existing methods completely fail (all below 0.01) is actually quite significant—if this approach can show meaningful improvement there, that would be genuinely surprising and impactful. Plus, the mechanistic grounding from entity priming research goes deeper than just observing a correlation. I'm revising my estimate to around 32%, accounting for this stronger motivation. When I look at the alternatives like SubInj and LEIA, they either only work at inference time or don't specifically target factual consistency, so EACA's approach of modifying internal representations through contrastive learning does offer something distinct.

The real question is whether the experimental results actually demonstrate meaningful gains over these simpler baselines, and that's where the contribution either lands or falls short. The core limitation remains that the insight itself—entity-level alignment improves entity-level consistency—is fairly intuitive, and this feels more like solid engineering than a conceptual leap. But given the specific gap it's targeting, I'd settle on a 25-35% range with a median around 30%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7923f9b2-257e-4b27-9cdb-080e9ed74194",
  "isSidechain": false,
  "requestId": "req_011CbCS6ZbeKMgDd4ahzvSk2",
  "type": "assistant",
  "uuid": "41ce22ca-b277-4324-bd49-35ca7bf0c7c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFpd3NrMmvwhdQ6rat7NS2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 712,
      "cache_creation_input_tokens": 964,
      "cache_read_input_tokens": 35751,
      "output_tokens": 7624,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 964,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 712,
          "output_tokens": 7624,
          "cache_read_input_tokens": 35751,
          "cache_creation_input_tokens": 964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 964
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

_source line 49 · 2026-05-19T18:55:56.379Z_

Now I have sufficient research to make an informed assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- CLiKA: "Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly" (NAACL 2024, arXiv:2404.04659): 定义了 Cross-Retrieval Ratio (XRR) 度量 conductivity，发现所有测试 LLM 的 XRR < 0.01，多语言预训练和指令微调均无法实质性提升 conductivity。这是 proposal 的核心动机，已验证为真实存在的论文和发现。
- CCL-XCoT (EMNLP Findings 2025, arXiv:2507.14239): 句子/段落粒度的对比学习 CPT，在 Gemma-7B 和 LLaMA-3.1-8B 上将跨语言幻觉降低 62%。使用课程化对比学习 + NTP，是最直接的句子级 baseline。该论文真实存在，但发表时间需注意——arXiv 为 2025 年 7 月，作为 EMNLP 2025 Findings 发表。
- Liu & Niehues (ACL 2025, arXiv:2502.14830): 中间层（layer 16/32）句子级对比对齐，用于任务特定微调，在 slot filling 上 +1.5 F1，MT 上 +1.5 BLEU。验证了中间层是跨语言对齐的最佳位置，但仅在句子粒度和下游任务迁移。真实论文，ACL 2025 已发表。
- "On the Entity-Level Alignment in Crosslingual Consistency" (arXiv:2510.10280): 发现实体对齐与跨语言一致性的 Pearson r > 0.7，>99% 一致的事实展示成功的实体对齐。提出 SubInj 方法（推理时插入英文实体名）获得 +14-32% recall 和 +17-44% 一致性提升。**关键竞争者**：此推理时方法已经取得了显著效果。
- KBioXLM (EMNLP Findings 2023, arXiv:2311.11564): 在 XLM-R（encoder）上使用多粒度知识对齐（实体掩码、关系掩码、段落关系预测）进行 CPT，在跨语言零样本生物医学任务上 +20 F1。真实论文，但限于 encoder + 生物医学领域。
- FactNet (arXiv:2602.03417, Feb 2026): 1.7B 实体锚定原子事实，316 个 Wikipedia 版本，Wikidata QID 链接，92.1% 精度。已在 arXiv 发布，GitHub 存在。是 EACA 的核心数据资源。
- TransliCo (ACL 2024, arXiv:2401.06620): 在 encoder (Glot500-m) 上使用音译对比学习，5% 数据即可桥接脚本障碍。ACL 2024 真实论文。
- DaMuEL (arXiv:2306.09288, 2023): 12.3B QID 标注 tokens，53 语言。真实数据集，CC BY-SA 许可。
- Bandarkar et al. (arXiv:2603.17070, March 2026): 确认 script match 是知识迁移的主要预测因子（~13% gap），关键的 entity priming 实验显示提供源语言实体名可不成比例地改善跨脚本迁移。真实 arXiv 论文。
- Ifergan et al. (NAACL Findings 2025, arXiv:2408.10646): 通过知识编辑探针发现 script similarity 主导跨语言知识表征共享（同脚本 CKR ~37.6% vs. 跨脚本 <10-20%）。真实论文。
- LEIA (ACL Findings 2024, arXiv:2402.11485): 在 decoder LLM CPT 中插入英文实体名（[translate]/[/translate] 标记），无对比损失，改善跨语言迁移。**关键 trivial alternative 候选者**。
- EntityCS (EMNLP Findings 2022): 实体级代码切换，但限于 encoder。
- Entity Lens (BlackboxNLP 2025, arXiv:2510.09421): decoder LLM 发展出实体特定机制来表征多 token 实体。

- **调研总结**: 跨语言事实一致性领域正处于快速发展期。CLiKA 揭示的 conductivity gap（XRR < 0.01）是一个公认的未解决问题。现有方法沿两条路线发展：(1) 句子/段落级对比 CPT（CCL-XCoT, Liu & Niehues），在下游任务和幻觉上有效但未解决实体级 conductivity；(2) 推理时实体增强（SubInj, LEIA 式方法），有效但不改变模型内部表征。EACA 提出的"实体级对比 CPT"位于两条路线的交汇点，但这个交汇点目前确实没有被已有工作直接占据。

【Trivial Alternative 检验】:
存在两个需要认真对待的 trivial alternative：

1. **SubInj（推理时实体增强）**：arXiv:2510.10280 的 SubInj 方法仅在推理时将英文实体名注入提示，就获得 +14-32% recall 和 +17-44% 一致性提升。这是零训练成本的方法。EACA 需要 1100-1600 H100 小时和 4-5 个月工程时间——如果最终效果与 SubInj 相当或仅小幅优于 SubInj，成本效益比极差。EACA 的增量价值论述是：训练时对齐改变模型内部表征，应该比推理时 prompt engineering 更根本、更泛化（不依赖于特定 prompt 格式）。这个论述逻辑上成立，但需要实验验证。

2. **LEIA + CCL-XCoT 组合**：LEIA 已经在 CPT 中使用实体标记增强，CCL-XCoT 已经在 CPT 中使用对比学习。一个直接的 baseline 是将 LEIA 的实体标记与 CCL-XCoT 的句子级对比损失简单组合。如果这个简单组合已经能获得大部分收益，EACA 的"实体级对比对齐"的边际贡献就会被压缩。Proposal 意识到了 LEIA 作为 baseline 的存在（Phase 0 包含了 LEIA augmentation baseline），但没有明确讨论 "LEIA + 句子级对比" 这个组合 baseline 的威胁。

**增量价值判断**：EACA 的真正增量在于将对比信号从句子级降到实体级并用结构化知识（FactNet QID）锚定正样本对。理论动机有据（r > 0.7 相关性，CLiKA 的 failure result），但这个增量是否大到足以 justify 系统复杂度，是实验需要回答的核心问题。Trivial alternative 威胁等级：**中等偏高**。

【前提假设检验】:
核心 claim 的逻辑链条：
1. ✅ CLiKA 表明现有方法无法提升 conductivity（XRR < 0.01）→ **有实证支持**
2. ✅ 实体对齐与跨语言一致性强相关（r > 0.7）→ **有实证支持**（arXiv:2510.10280）
3. ⚠️ **"句子级对比之所以不改善 conductivity，是因为粒度太粗，conflating entity-specific knowledge with syntactic variation"** → **这是未经验证的假设**。CLiKA 测试的是标准多语言预训练和指令微调，CCL-XCoT 的句子级对比确实降低了幻觉 62%，但其对 CLiKA 的 XRR 指标的影响未知。Proposal 假设句子级对比无法改善 XRR，但这并未被实验验证——CCL-XCoT 论文没有报告 XRR 指标。
4. ⚠️ **"实体级对比对齐可以改善模型内部表征，而非仅仅是推理时效果"** → **合理但未验证**。SubInj 的成功表明实体对齐是瓶颈，但 SubInj 是推理时的，EACA 假设训练时对比学习可以将这种对齐内化到模型表征中。虽然这在理论上合理（对比学习改变表征空间是有先例的），但在 decoder LLM 的 CPT 阶段使用实体级 InfoNCE 是否能有效改变中间层表征，以及是否比 NTP 自然学习的表征更好，并无先例。
5. ⚠️ **"在 decoder LLM 上的实体级对比损失不会严重干扰自回归语言建模能力"** → 这是一个工程假设，有 CCL-XCoT 的句子级先例支持，但实体级对比（每个 batch 128-256 个 QID 的正/负样本对）的梯度动态与句子级可能不同。Proposal 通过 PCGrad 和 GradNorm 设计了缓解机制，但这本身就暗示了风险。

**最关键的未验证假设**：第 3 点——"句子级对比之所以失败是因为粒度问题"。如果句子级对比实际上也能改善 XRR（只是没人测过），那 EACA 的核心动机就被削弱。

【3 维度打分】:

1. **Novelty: 中** — 
   EACA 的核心贡献是将对比 CPT 的粒度从句子级降至实体级，并用结构化知识图谱（FactNet QID）锚定对比对。这个组合在已有工作中确实不存在：CCL-XCoT 是句子级对比 CPT（EMNLP 2025 Findings），Liu & Niehues 是句子级中间层对比微调（ACL 2025），KBioXLM 是 encoder 上的实体掩码（EMNLP 2023 Findings），LEIA 是实体增强 CPT 无对比损失（ACL 2024 Findings），TransliCo 是 encoder 上的音译对比（ACL 2024）。EACA 位于这些工作的交叉点，这个特定的组合点确实是空白的。然而，novelty 主要来自"组合"而非"新概念"——每个组件（实体标记、对比损失、中间层提取、知识图谱锚定、音译增强、梯度冲突监控）都有明确的来源。对于审稿人来说，问题在于这是"principled synthesis"还是"incremental combination"——这很大程度上取决于实验结果是否显著超越各组件的简单组合。此外，arXiv:2510.10280 已经建立了"实体对齐 → 一致性"的强相关性，使得 EACA 的方向几乎是"显而易见的下一步"，降低了 surprise factor。

2. **Significance: 中偏强** — 
   研究问题（跨语言知识 conductivity）是领域内公认的重要问题。CLiKA (NAACL 2024) 明确表明所有现有方法在 XRR 指标上几乎为零，这是一个 well-documented failure。如果 EACA 能够实质性提升 XRR（即便是从 <0.01 提升到 0.05-0.1），这将是一个有影响力的结果，因为它回答了一个目前无解的问题。此外，脚本障碍问题（Ifergan et al. NAACL 2025; Bandarkar et al. 2026）是多语言 NLP 的持久挑战，EACA 对此的针对性处理（音译增强 + 脚本分组评估）增加了实用价值。但 significance 受限于：(a) 实际应用场景——conductivity 改善对终端用户的实际影响尚不清楚；(b) 仅在 8B 模型上验证，scaling behavior 未知；(c) 如果效果仅在 same-script 上显著而 cross-script 改善有限（考虑到脚本障碍的严重性），影响力会打折。

3. **Related Work: 强** — 
   这是 proposal 最强的维度。覆盖范围极为全面：从诊断框架（CLiKA）、对比 CPT（CCL-XCoT）、中间层对齐（Liu & Niehues）、实体级先例（KBioXLM、LEIA、EntityCS）、实体表征分析（Entity Lens、Marco et al.）、脚本障碍（Ifergan et al.、Bandarkar et al.、TransliCo）到数据资源（FactNet、DaMuEL），几乎无遗漏。差异化定位清晰——对 CCL-XCoT 有 5 轴差异分析，对 Liu & Niehues 有详细的粒度/目标/数据比较，对 KBioXLM 有 4 维度扩展论述。所有我能搜到的关键引用都被准确引用和描述。唯一的轻微不足是未讨论"LEIA + 句子级对比"这个组合 baseline 的威胁。

【概率估计】: [25% - 35%] 中位 30%

【估计理由】: 
Novelty 为中是主要限制因素。idea 的核心洞见（"实体级对齐是 conductivity 的瓶颈，应该用实体级对比学习来解决"）是被现有证据（r > 0.7 相关性）高度预测的"下一步"，而不是反直觉的发现。审稿人很可能会说"the motivation is sound, but the contribution is primarily the engineering effort of putting known pieces together"。Significance 中偏强——问题确实重要且 well-documented，但受制于 trivial alternative 威胁（SubInj 推理时已获得显著效果）。Related Work 强——但相关工作的完备性不能提升 idea 本身的 novelty 天花板。概率上界（35%）需要实验结果显著超越所有 trivial alternatives + 在 cross-script 上也有明显效果；下界（25%）对应审稿人认定为 incremental combination 的情况。注意：如果目标会议确实是 CoRL（Conference on Robot Learning），此 proposal 完全 off-topic，概率接近 0%——此处按 NLP/CL 顶会估计。

【主要风险】: 
1. **"Principled engineering" vs. "new idea" 的审稿认知风险**：每个组件都有明确来源，核心假设（实体级 > 句子级）几乎是 arXiv:2510.10280 相关性结果的直接推论。审稿人可能认为这是"well-executed combination"而非"novel contribution"，在 novelty 维度给出 borderline reject。
2. **Trivial alternative 的实验失败风险**：如果 SubInj（零训练成本的推理时方法）或 "LEIA + CCL-XCoT" 简单组合在 XRR 指标上与 EACA 效果相当，则 EACA 的 1100+ H100 小时投入和复杂 pipeline 难以 justify。这不是 idea 本身的缺陷，但它意味着 idea 的成功高度依赖于实验 delta 的大小。
```

Sources:
- [CLiKA - NAACL 2024](https://aclanthology.org/2024.naacl-long.339/)
- [CCL-XCoT - EMNLP Findings 2025](https://arxiv.org/abs/2507.14239)
- [Liu & Niehues - ACL 2025](https://aclanthology.org/2025.acl-long.778/)
- [Entity-Level Alignment in Crosslingual Consistency](https://arxiv.org/abs/2510.10280)
- [KBioXLM - EMNLP Findings 2023](https://aclanthology.org/2023.findings-emnlp.751/)
- [FactNet - arXiv 2026](https://arxiv.org/abs/2602.03417)
- [TransliCo - ACL 2024](https://aclanthology.org/2024.acl-long.136/)
- [DaMuEL](https://arxiv.org/abs/2306.09288)
- [Bandarkar et al. - Script Barrier](https://arxiv.org/abs/2603.17070)
- [LEIA - ACL Findings 2024](https://aclanthology.org/2024.findings-acl.419/)
- [Ifergan et al. - NAACL Findings 2025](https://arxiv.org/abs/2408.10646)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41ce22ca-b277-4324-bd49-35ca7bf0c7c2",
  "isSidechain": false,
  "requestId": "req_011CbCS6ZbeKMgDd4ahzvSk2",
  "type": "assistant",
  "uuid": "2f8933ef-5094-437a-8ac6-abbb8d2d2b71",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFpd3NrMmvwhdQ6rat7NS2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 712,
      "cache_creation_input_tokens": 964,
      "cache_read_input_tokens": 35751,
      "output_tokens": 7624,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 964,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 712,
          "output_tokens": 7624,
          "cache_read_input_tokens": 35751,
          "cache_creation_input_tokens": 964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 964
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

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Entity-Anchored Contrastive Alignment for Cross-Lingual Knowledge Conductivity  ## Description EACA is a continu…",
  "leafUuid": "2f8933ef-5094-437a-8ac6-abbb8d2d2b71",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate entity-level cross-lingual alignment proposal",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Entity-Anchored Contrastive Alignment for Cross-Lingual Knowledge Conductivity  ## Description EACA is a continu…",
  "leafUuid": "2f8933ef-5094-437a-8ac6-abbb8d2d2b71",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate entity-level cross-lingual alignment proposal",
  "sessionId": "e7d63c9f-d9c2-416a-905a-2b7021ac9422"
}
```

---
