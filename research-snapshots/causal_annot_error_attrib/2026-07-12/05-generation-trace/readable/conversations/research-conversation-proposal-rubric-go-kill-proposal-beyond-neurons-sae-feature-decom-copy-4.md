# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Beyond Neurons: SAE Feature Decom

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/ce70cc30-ca05-41af-b67a-765df91c77b1.jsonl`
- **Structured JSON:** [`54cafdf1f9384a2e6c4d.json`](../../sessions/54/54cafdf1f9384a2e6c4d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T21:01:40.031Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T21:01:40.031Z",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation\n\n## Description\nCurrent cross-lingual knowledge editing faces a universal portability bottleneck: not just LU-LAFNs (COLING 2025) but ALL current methods achieve near-zero portability EM (< 10) on Bi-ZsRE, with the LU-LAFNs authors themselves noting 'all methods underperform on this metric without significant difference.' We hypothesize that this bottleneck has a specific causal mechanism: polysemantic neurons entangle factual relational structure with language identity, so any neuron-level editing that removes language components inevitably corrupts relational knowledge needed for portability. This hypothesis is independently supported by Mondal et al. (NAACL 2025 InsightsNLP), who showed that neuron-level language-specific interventions are insufficient for cross-lingual transfer even outside the editing setting.\n\nWe propose SAE-Projected Editing: using pre-trained Qwen-Scope SAEs (64K features on Qwen3-8B) and Llama Scope SAEs (128K features on Llama-3.1-8B) to decompose edit vectors into finer-grained sparse features, classify each as language-specific or language-agnostic via cross-lingual activation-probability contrasts, then apply adaptive soft projection that suppresses language-specific components proportionally to their Factual Causal Effect (FCE) — a per-feature ablation-based metric measuring how much factual recall degrades when the feature is removed. Unlike binary feature zeroing — which Farrell et al. (2024) showed is ineffective — our adaptive λ-projection preserves factual content encoded in partially-entangled features while removing pure language-identity signal.\n\n**Engagement with SAE intervention skepticism:** Peng et al. (arXiv:2506.23845) argue SAEs are better for discovery than intervention; however, Arad et al. (EMNLP 2025) directly rebut this by showing that output-score-based feature selection yields 2–3× improvement in SAE steering, matching supervised methods. The critique applies to naive feature selection, not SAE interventions as a paradigm. We incorporate output-score filtering into our pipeline. Chou et al. (arXiv:2507.13410) provide further feasibility evidence: modifying a single SAE feature achieves up to 90% language steering success on Gemma-2B/9B. Leask et al. (ICLR 2025) show SAE features are not atomic canonical units — larger latents decompose into sub-components. We accommodate this by: (a) treating features as a continuous weighted basis rather than binary switches, (b) using adaptive λ coefficients that handle partial feature overlap, and (c) ablating across SAE widths (16K/64K/128K) to identify task-appropriate granularity per Leask et al.'s recommendation.\n\n**FeatureEdit context note:** The +23% reliability and 2.8× generalization gains from FeatureEdit (ACL 2025) are for knowledge erasure on the PrivacyParaRel privacy dataset using Gemma-2 models, not factual knowledge editing or cross-lingual propagation. We cite these as evidence that features outperform neurons as representation-level intervention units, but do not assume these specific gains transfer to the editing setting.\n\n**FCE metric protocol:** For each of ~64K SAE features, we first compute point-biserial correlation r_pb between feature activation magnitude and binary factual recall success across ≥5,000 multilingual facts (computational cost: ~4 GPU-hours for forward passes). The top ~2K features by |r_pb| undergo full causal ablation: each feature is individually zeroed, and the change in factual recall probability is measured (FCE). This two-stage approach reduces the 64K × 5K evaluation matrix to a tractable 2K × 5K, requiring ~40 GPU-hours. Bootstrap confidence intervals (1000 resamples) provide uncertainty estimates for FCE values. As a validation check, we compute Spearman rank correlation between r_pb and FCE on the 2K features to verify the proxy quality.\n\nKey contributions: (1) First application of SAE feature decomposition to cross-lingual knowledge editing, providing ~5-10× finer granularity than neuron-level LAFN identification; (2) Adaptive soft projection mechanism that explicitly accounts for factual-language feature entanglement via a concrete, causal FCE metric with a two-stage efficient computation protocol; (3) Principled engagement with SAE intervention skepticism (Peng et al., Leask et al.) through output-score filtering, continuous-basis treatment, and multi-width ablation; (4) Testable portability hypothesis: if SAE features do NOT improve portability EM over neuron-level approaches (ablation A3), this falsifies the polysemanticity-entanglement explanation and has standalone diagnostic value; (5) Reconstruction fidelity validation protocol establishing whether SAE round-trip preserves edit vector quality across dictionary sizes.\n\nWe evaluate on CLM-Bench (zh-en), Bi-ZsRE, and MzsRE across 12 languages, targeting improvements over LU-LAFNs (77.87 Bi-ZsRE avg on bloomz-7b1-mt; MzsRE results reported as per-language heatmaps rather than a single average) particularly on portability metrics. Primary baselines: LU-LAFNs, FeatureEdit (adapted cross-lingual), MEMIT, AlphaEdit, M-MEMIT, X-KDE, LangEdit.\n\n**Risk mitigation:** The core risk is that the portability bottleneck is NOT caused by polysemantic entanglement but by a more fundamental limitation (e.g., the portability metric itself measuring reasoning ability that editing cannot improve). We address this through: (a) explicit FCE measurement before editing to quantify the entanglement ceiling, (b) adaptive λ-projection that preserves high-FCE features, (c) reconstruction fidelity go/no-go gate, (d) ablation A3 as a direct falsification test, and (e) relational follow-up evaluation (A2) that provides a complementary portability measure independent of the Bi-ZsRE metric. If SAE features fail to improve portability, the negative result still contributes a rigorous decomposition analysis of what fraction of factual information resides in language-specific vs. language-agnostic features — valuable for the multilingual interpretability community. Fallback: hybrid approach combining SAE-projected editing for low-entanglement facts with LU-LAFNs for high-entanglement cases.\n\n## Core Problem\nCross-lingual knowledge editing methods face two linked failures: (1) raw edit vectors reside in nearly orthogonal, language-specific subspaces (CLM-Bench), and (2) neuron-level approaches like LU-LAFNs that identify language-agnostic neurons achieve high monolingual reliability but suffer catastrophically low portability (26.43% F1, EM < 5) — a failure shared by ALL current methods (all EM < 10 on Bi-ZsRE portability), suggesting a fundamental representation-level bottleneck. We hypothesize that this bottleneck stems from polysemantic neurons entangling factual relational structure with language identity: edits that operate at neuron granularity cannot cleanly separate these components, corrupting relational knowledge during cross-lingual transfer. Can sparse autoencoder feature decomposition — which yields finer-grained, more monosemantic units — provide a cleaner separation that better preserves relational structure, and is this hypothesis even testable given recent challenges to SAE feature canonicality (Leask et al., ICLR 2025)?\n\n## Opportunity\nCLM-Bench (arXiv:2601.17397, Jan 2026) provided geometric evidence that Chinese and English edit vectors are nearly orthogonal, explaining why ROME/MEMIT fail cross-lingually (~20% reliability). LU-LAFNs (COLING 2025) achieved 77.87 avg on Bi-ZsRE by targeting language-agnostic neurons, but its neuron-level approach identifies 67.9% of neurons as LAFNs — an extremely coarse decomposition reflecting neuron polysemanticity — and ALL methods achieve near-zero portability EM (< 10 across the board), which the authors attribute to the difficulty of measuring reasoning without a reasoning process. Crucially, Mondal et al. (NAACL 2025 InsightsNLP) independently showed that neuron-level language-specific interventions are insufficient for cross-lingual transfer on XNLI/XQuAD, reinforcing the case that neuron-level decomposition is fundamentally too coarse.\n\nMeanwhile, FeatureEdit (ACL 2025) demonstrated that SAE features outperform neurons for knowledge erasure on PrivacyParaRel (~0.80 vs ~0.65 reliability, ~0.70 vs ~0.25 generalization on Gemma-2 2B/9B) — though notably this was for privacy-knowledge erasure, not factual editing or cross-lingual propagation, so these gains may not directly transfer. LangSAE (arXiv:2601.04768) proved SAE-based language identity removal improves cross-lingual retrieval by +21.9% nDCG@20. Chou et al. (arXiv:2507.13410) achieved up to 90% language steering success by modifying a single SAE feature on Gemma-2B/9B, demonstrating that SAE-based language manipulation is feasible and precise.\n\nHowever, recent work challenges SAE interventions: Peng et al. (arXiv:2506.23845) argue SAEs are better for concept discovery than acting on known concepts, finding SAE-based steering underperforms prompting/fine-tuning. Critically, Arad et al. (EMNLP 2025) rebut this: proper feature selection via output-score filtering yields 2–3× improvement in SAE steering, matching supervised methods — the issue was feature selection, not SAE interventions per se. Leask et al. (ICLR 2025) show SAE features aren't canonical atomic units — larger latents decompose into combinations — but recommend pragmatic choice of dictionary size suited to task, and our adaptive soft projection naturally accommodates non-atomicity by treating features as a continuous basis rather than binary switches.\n\nThe missing link: no work has combined SAE feature-level decomposition with cross-lingual knowledge editing. SAE features offer ~64K monosemantic units (vs. ~14K polysemantic neurons), enabling more precisely targeted language-component manipulation that may better preserve relational/factual structure — a hypothesis we propose to test directly.\n\n## Related Work / Landscape\nCross-lingual knowledge editing is a recognized open problem: the survey (arXiv:2505.14393) identifies language anisotropy and edit scalability as key challenges. The field is structured in three tiers:\n\n**Tier 1 — Direct multilingual editing baselines:** MEMIT/M-MEMIT apply locate-then-edit across languages (74.86 avg on Bi-ZsRE but ~20% cross-lingual reliability). AlphaEdit (ICLR 2025) uses null-space constraints. Merging Methods for MKE (arXiv:2605.13919, May 2026) explores vector merging with shared covariance for 12-language editing but without representation-level decomposition.\n\n**Tier 2 — Neuron/representation-level multilingual editing:** LU-LAFNs (COLING 2025, arXiv:2406.16416) is the closest prior work — identifies language-agnostic factual neurons via activation frequency intersection across languages, achieving 77.87 avg on Bi-ZsRE (bloomz-7b1-mt). However, it identifies 67.9% of neurons as LAFNs (extremely coarse), and ALL methods achieve near-zero portability (EM < 10, F1 ~26-36%), which the authors acknowledge as a universal challenge rather than a method-specific failure. Mondal et al. (NAACL 2025 InsightsNLP, arXiv:2503.17456) provide independent evidence that neuron-level language-specific interventions are insufficient for cross-lingual transfer. MEMLA (arXiv:2406.11566) uses neuron masking with LoRA but doesn't leverage monosemantic features. X-KDE (ACL 2025 Findings, arXiv:2502.14645) uses instruction tuning + preference optimization (+8.19% avg improvement). LangEdit (ACL 2025 Findings, arXiv:2506.10800) applies null-space projection for multilingual sequential editing across 6 languages.\n\n**Tier 3 — SAE-based editing and language feature work (our building blocks):** FeatureEdit from 'The Knowledge Microscope' (ACL 2025, arXiv:2502.12483) is the first SAE-feature-based model editing method — uses Gemma Scope JumpReLU SAEs to identify knowledge features and zero out specific weight positions. On the PrivacyParaRel knowledge-erasure benchmark (not factual editing), features achieve ~0.80 reliability (vs. ~0.65 for neurons) and ~0.70 generalization (vs. ~0.25), demonstrating features' advantage for representation-level interventions. However, it is monolingual English-only, targets knowledge erasure rather than cross-lingual propagation, and these gains may not directly transfer to the editing setting. SSPU (EMNLP 2025, arXiv:2505.24428) shows SAE-guided subspace projection via QR decomposition can unlearn knowledge while preserving non-target capabilities. LangSAE (arXiv:2601.04768) removes language identity from embeddings using SAE feature suppression (+21.9% nDCG@20). SAE-LAPE/LangFIR (arXiv:2604.03532) discover sparse language-specific features using activation probability contrasts. SASFT (ICLR 2026) shows SAE-guided fine-tuning preserves targeted knowledge. SpARE (NAACL 2025, arXiv:2410.15999) uses SAE-based representation engineering for knowledge selection steering but not cross-lingually. SCAN (arXiv:2603.15226, Mar 2026) uses sparse transcoders for lifelong editing on Qwen3/Llama3.1 but addresses sequential stability, not cross-lingual transfer. Farrell et al. (arXiv:2410.19278) found that zero ablation of SAE features is ineffective for knowledge unlearning — negative scaling is necessary. Chou et al. (arXiv:2507.13410) achieved up to 90% language steering success by modifying single SAE features on Gemma-2B/9B, providing direct feasibility evidence for SAE-based language manipulation.\n\n**Tier 4 — SAE intervention skepticism and counter-evidence (critical context):** Peng et al. (arXiv:2506.23845) argue SAEs are better for discovering unknown concepts than acting on known ones, finding SAE-based steering underperforms prompting/fine-tuning. However, Arad et al. (EMNLP 2025, arXiv:2505.20063) directly rebut this: by distinguishing 'input features' (capture input patterns) from 'output features' (causally affect model behavior) and filtering by output scores, SAE steering achieves 2–3× improvement, matching supervised methods. The issue was naive feature selection, not SAE interventions as a paradigm. Zhao et al. (arXiv:2505.15038) further show denoising concept vectors via SAE improves steering 4–16%. SAE-SSV (EMNLP 2025, arXiv:2505.16188) achieves high steering success rates using supervised feature selection in sparse spaces. Leask et al. (ICLR 2025, arXiv:2502.04878) demonstrate SAE features are neither atomic nor canonical — meta-SAEs decompose latents into sub-components (e.g., 'Einstein' → 'scientist' + 'Germany' + 'famous person'), and smaller SAEs miss information captured by larger ones. They recommend pragmatic dictionary size selection rather than assuming canonicality. Our approach accommodates this by treating SAE features as a practical continuous basis with adaptive coefficients, not as binary canonical units.\n\n**The gap:** No work combines SAE feature decomposition with cross-lingual knowledge editing. Specifically, no one has (a) used monosemantic SAE features instead of polysemantic neurons to decompose cross-lingual edit vectors, (b) tested whether finer-grained decomposition causally improves portability by preserving relational structure, or (c) engaged with the feature-selection insights from Arad et al. to ensure intervention-effective features are targeted.\n\n## Approach\n**Phase 1: Feature Classification with Output-Score Filtering (Weeks 1-2).** Leverage pre-trained SAEs — Qwen-Scope (64K features, 16× expansion) on Qwen3-8B and Llama Scope (128K features, 32× expansion) on Llama-3.1-8B — to decompose residual-stream activations at editing-critical layers (layers 12-25 for Qwen3-8B based on LU-LAFNs' LAFN distribution peaks). Classify each feature as language-specific, language-agnostic, or factual using activation-probability contrasts across Chinese, English, and 4+ additional languages (following SAE-LAPE/LangFIR methodology). Critically, following Arad et al.'s (EMNLP 2025) insight that input-pattern features and output-causal features rarely co-occur, compute output scores for all features to ensure we target features that causally affect model behavior, not merely correlational activations — this addresses the core criticism of Peng et al. For each language-specific feature f_i, compute its Factual Causal Effect (FCE): ablate f_i and measure the change in correct factual recall probability across a multilingual fact corpus of ≥5,000 facts (drawn from Bi-ZsRE + MzsRE test sets, held out from editing evaluation). FCE(f_i) = |P(correct | f_i active) - P(correct | f_i ablated)|. This produces a per-feature entanglement map. FCE is preferred over mutual information because: (a) it is causal rather than correlational, (b) it avoids the curse-of-dimensionality problems that plague MI estimation with 64K+ features (KSG estimators break down beyond ~10 dimensions), and (c) it is directly interpretable as the factual cost of removing a feature. As a computationally efficient proxy during initial screening, we also compute point-biserial correlation r_pb between feature activation magnitude and binary factual recall success, filtering to the top ~2K candidate features for full FCE ablation (reducing 64K × 5K evaluations to ~2K × 5K).\n\n**Phase 2: SAE-Projected Editing with Adaptive Soft Projection (Weeks 3-5).** For a given ROME/MEMIT edit vector e, decompose it into the SAE feature basis: e ≈ Σ_j α_j d_j (where d_j are SAE decoder directions and α_j are coefficients from the encoder). Following Farrell et al.'s finding that binary zeroing is ineffective and Leask et al.'s evidence that features are not atomic canonical units, we apply adaptive soft projection that treats features as a continuous basis: e_proj = e - Σ_{i ∈ L_spec} λ_i · α_i · d_i, where λ_i ∈ [0, 1] is inversely proportional to FCE(f_i) — features with high factual causal effect are preserved more, pure language-identity features (low FCE, high language specificity) are fully suppressed. This formulation naturally handles Leask et al.'s non-atomicity concern: since features are weighted continuously rather than treated as binary switches, partial overlap between sub-features is accommodated through the λ gradient. The projected vector e_proj is then applied via the standard locate-then-edit pipeline.\n\n**Phase 3: Reconstruction Fidelity Validation (Weeks 3-4, parallel).** Before full-scale editing, validate that SAE round-trip reconstruction preserves edit vector fidelity. Measure: (a) cosine similarity between original and reconstructed edit vectors, (b) monolingual edit success rate with SAE-reconstructed vectors (no language feature removal) vs. original ROME/MEMIT — this isolates reconstruction error from projection effects. If reconstruction degrades edit quality by >5%, investigate top-k sparsity adjustments or layer-specific SAE selection. Following Leask et al.'s recommendation, test multiple SAE widths (16K, 64K, 128K where available) to identify task-appropriate granularity rather than assuming larger is better. Establish a reconstruction quality threshold as a go/no-go gate.\n\n**Phase 4: Evaluation and Ablation (Weeks 5-8).** Evaluate on CLM-Bench (1,010 zh-en pairs), Bi-ZsRE, and MzsRE (12 languages) using Qwen3-8B and Llama-3.1-8B. Primary baselines: LU-LAFNs (77.87/Bi-ZsRE on bloomz-7b1-mt — the SOTA to beat), FeatureEdit (adapted to cross-lingual setting), MEMIT, AlphaEdit, M-MEMIT, X-KDE, LangEdit. Secondary baselines: SCAN, MEMLA. Key ablations: (A1) Full zeroing vs. soft projection — measuring factual content loss, directly testing Farrell et al.'s finding in the cross-lingual setting. (A2) Relational structure preservation: for edited facts, measure whether the model correctly answers relational follow-up questions (e.g., after editing 'capital of X', test 'X is in which continent?') — this directly tests the portability hypothesis. (A3) Feature granularity: SAE features (64K/128K) vs. neuron-level LAFNs (~10K) vs. random subspace projection — if SAE features do not improve portability over neurons, this falsifies our core hypothesis. (A4) λ scheduling: fixed λ vs. FCE-adaptive λ vs. oracle λ (per-fact optimal). (A5) Layer selection: which layers' SAEs are most critical for cross-lingual transfer. (A6) SAE width: 16K vs. 64K vs. 128K features, testing Leask et al.'s prediction that task-appropriate granularity matters more than raw dictionary size. (A7) Output-score filtering (per Arad et al.): restrict projection to high-output-score features vs. all language-classified features.\n\n## Inspiration\nLU-LAFNs' universal portability failure (all methods EM < 10) revealing a fundamental representation-level bottleneck + Mondal et al.'s independent evidence that neuron-level language interventions are insufficient + FeatureEdit's demonstration that SAE features outperform neurons for knowledge erasure + LangSAE proving language features can be surgically suppressed + Chou et al.'s 90% language steering with single SAE features + CLM-Bench's geometric evidence of language-specific subspaces + SSPU's QR-decomposition subspace methodology + Arad et al.'s insight that output-score feature selection rescues SAE interventions + Farrell et al.'s finding that soft scaling outperforms zero ablation\n\n## Key References\n- LU-LAFNs: Multilingual Knowledge Editing with Language-Agnostic Factual Neurons (COLING 2025, arXiv:2406.16416) — PRIMARY BASELINE\n- FeatureEdit / The Knowledge Microscope: Features as Better Analytical Lenses than Neurons (ACL 2025, arXiv:2502.12483) — METHODOLOGICAL PREDECESSOR (knowledge erasure, not editing)\n- CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing (arXiv 2026, arXiv:2601.17397)\n- LangSAE Editing: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal (arXiv 2026, arXiv:2601.04768)\n- LangEdit: Mitigating Negative Interference in Multilingual Sequential Knowledge Editing through Null-Space Constraints (ACL 2025 Findings, arXiv:2506.10800)\n- SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing (arXiv 2026, arXiv:2603.15226)\n- SSPU: Model Unlearning via Sparse Autoencoder Subspace Guided Projections (EMNLP 2025, arXiv:2505.24428)\n- Applying Sparse Autoencoders to Unlearn Knowledge in Language Models (arXiv 2024, arXiv:2410.19278)\n- X-KDE: Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs (ACL 2025 Findings, arXiv:2502.14645)\n- MEMLA: Enhancing Multilingual Knowledge Editing with Neuron-Masked Low-Rank Adaptation (arXiv 2024, arXiv:2406.11566)\n- Editing Across Languages: A Survey of Multilingual Knowledge Editing (arXiv 2025, arXiv:2505.14393)\n- SAE-LAPE: Unveiling Language-Specific Features in Large Language Models via Sparse Autoencoders (ACL 2025, arXiv:2505.05111)\n- LinguaLens: Towards Interpreting Linguistic Mechanisms of Large Language Models via Sparse Auto-Encoder (EMNLP 2025)\n- SASFT: Sparse Autoencoder-guided Supervised Finetuning to Mitigate Unexpected Code-Switching in LLMs (ICLR 2026)\n- AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models (ICLR 2025)\n- SpARE: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering (NAACL 2025, arXiv:2410.15999)\n- LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering (arXiv 2026, arXiv:2604.03532)\n- Merging Methods for Multilingual Knowledge Editing for Large Language Models: An Empirical Odyssey (arXiv 2026, arXiv:2605.13919)\n- SALVE: Sparse Autoencoder-Latent Vector Editing for Mechanistic Control of Neural Networks (arXiv 2025, arXiv:2512.15938)\n- Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models (arXiv 2026, arXiv:2605.11887)\n- Llama Scope: Extracting Millions of Features from Llama-3.1-8B with Sparse Autoencoders (arXiv 2024, arXiv:2410.20526)\n- Language-Specific Neurons: The Key to Multilingual Capabilities in Large Language Models (ACL 2024, arXiv:2402.16438)\n- Peng et al.: Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts (arXiv 2025, arXiv:2506.23845) — ADVERSARIAL: argues SAEs underperform for interventions\n- Leask et al.: Sparse Autoencoders Do Not Find Canonical Units of Analysis (ICLR 2025, arXiv:2502.04878) — ADVERSARIAL: shows features are not atomic/canonical\n- Arad et al.: SAEs Are Good for Steering — If You Select the Right Features (EMNLP 2025, arXiv:2505.20063) — REBUTTAL to Peng et al.: output-score filtering yields 2-3× improvement\n- Mondal et al.: Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer (NAACL 2025 InsightsNLP, arXiv:2503.17456) — SUPPORTS motivation: neuron-level is insufficient\n- Chou et al.: Causal Language Control in Multilingual Transformers via Sparse Feature Steering (arXiv 2025, arXiv:2507.13410) — FEASIBILITY: 90% language steering with single SAE feature\n- Zhao et al.: Denoising Concept Vectors with Sparse Autoencoders for Improved Language Model Steering (arXiv 2025, arXiv:2505.15038) — SAE steering improves 4-16% with denoising\n- SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models (EMNLP 2025, arXiv:2505.16188)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '450-550 (SAE feature classification + FCE ablation analysis ~120h on 1×A100 — increased due to per-feature ablation; reconstruction fidelity validation across SAE widths ~40h; editing experiments across 2 models × 3 benchmarks × 8+ baselines ~250h; ablation studies A1-A7 ~120h; analysis ~40h)', 'timeline': '10-12 weeks', 'estimated_gpu_cost': '$1,125-$1,375 (A100 at ~$2.50/hr; major savings from pre-trained Qwen-Scope and Llama Scope SAEs)'}\n- **human_in_loop**: {'gpu_hours': '400-500', 'timeline': '7-9 weeks', 'claude_api_cost': '$150-$250 (code generation for SAE analysis pipeline, FCE computation, experiment orchestration)', 'estimated_gpu_cost': '$1,000-$1,250'}\n- **auto_research**: {'gpu_hours': '400-500', 'timeline': '5-7 weeks', 'claude_api_cost': '$400-$550 (end-to-end experiment management, hyperparameter sweeps for λ, paper drafting)', 'estimated_gpu_cost': '$1,000-$1,250', 'speed_bottleneck': 'FCE ablation requires sequential per-feature evaluation (mitigated by r_pb pre-screening to ~2K features); sequential editing experiments per model-benchmark pair; CLM-Bench evaluation involves Chinese cultural knowledge judgment requiring human spot-checking'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T21:01:40.036Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T21:01:40.036Z",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-19T21:01:40.058Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation

## Description
Current cross-lingual knowledge editing faces a universal portability bottleneck: not just LU-LAFNs (COLING 2025) but ALL current methods achieve near-zero portability EM (< 10) on Bi-ZsRE, with the LU-LAFNs authors themselves noting 'all methods underperform on this metric without significant difference.' We hypothesize that this bottleneck has a specific causal mechanism: polysemantic neurons entangle factual relational structure with language identity, so any neuron-level editing that removes language components inevitably corrupts relational knowledge needed for portability. This hypothesis is independently supported by Mondal et al. (NAACL 2025 InsightsNLP), who showed that neuron-level language-specific interventions are insufficient for cross-lingual transfer even outside the editing setting.

We propose SAE-Projected Editing: using pre-trained Qwen-Scope SAEs (64K features on Qwen3-8B) and Llama Scope SAEs (128K features on Llama-3.1-8B) to decompose edit vectors into finer-grained sparse features, classify each as language-specific or language-agnostic via cross-lingual activation-probability contrasts, then apply adaptive soft projection that suppresses language-specific components proportionally to their Factual Causal Effect (FCE) — a per-feature ablation-based metric measuring how much factual recall degrades when the feature is removed. Unlike binary feature zeroing — which Farrell et al. (2024) showed is ineffective — our adaptive λ-projection preserves factual content encoded in partially-entangled features while removing pure language-identity signal.

**Engagement with SAE intervention skepticism:** Peng et al. (arXiv:2506.23845) argue SAEs are better for discovery than intervention; however, Arad et al. (EMNLP 2025) directly rebut this by showing that output-score-based feature selection yields 2–3× improvement in SAE steering, matching supervised methods. The critique applies to naive feature selection, not SAE interventions as a paradigm. We incorporate output-score filtering into our pipeline. Chou et al. (arXiv:2507.13410) provide further feasibility evidence: modifying a single SAE feature achieves up to 90% language steering success on Gemma-2B/9B. Leask et al. (ICLR 2025) show SAE features are not atomic canonical units — larger latents decompose into sub-components. We accommodate this by: (a) treating features as a continuous weighted basis rather than binary switches, (b) using adaptive λ coefficients that handle partial feature overlap, and (c) ablating across SAE widths (16K/64K/128K) to identify task-appropriate granularity per Leask et al.'s recommendation.

**FeatureEdit context note:** The +23% reliability and 2.8× generalization gains from FeatureEdit (ACL 2025) are for knowledge erasure on the PrivacyParaRel privacy dataset using Gemma-2 models, not factual knowledge editing or cross-lingual propagation. We cite these as evidence that features outperform neurons as representation-level intervention units, but do not assume these specific gains transfer to the editing setting.

**FCE metric protocol:** For each of ~64K SAE features, we first compute point-biserial correlation r_pb between feature activation magnitude and binary factual recall success across ≥5,000 multilingual facts (computational cost: ~4 GPU-hours for forward passes). The top ~2K features by |r_pb| undergo full causal ablation: each feature is individually zeroed, and the change in factual recall probability is measured (FCE). This two-stage approach reduces the 64K × 5K evaluation matrix to a tractable 2K × 5K, requiring ~40 GPU-hours. Bootstrap confidence intervals (1000 resamples) provide uncertainty estimates for FCE values. As a validation check, we compute Spearman rank correlation between r_pb and FCE on the 2K features to verify the proxy quality.

Key contributions: (1) First application of SAE feature decomposition to cross-lingual knowledge editing, providing ~5-10× finer granularity than neuron-level LAFN identification; (2) Adaptive soft projection mechanism that explicitly accounts for factual-language feature entanglement via a concrete, causal FCE metric with a two-stage efficient computation protocol; (3) Principled engagement with SAE intervention skepticism (Peng et al., Leask et al.) through output-score filtering, continuous-basis treatment, and multi-width ablation; (4) Testable portability hypothesis: if SAE features do NOT improve portability EM over neuron-level approaches (ablation A3), this falsifies the polysemanticity-entanglement explanation and has standalone diagnostic value; (5) Reconstruction fidelity validation protocol establishing whether SAE round-trip preserves edit vector quality across dictionary sizes.

We evaluate on CLM-Bench (zh-en), Bi-ZsRE, and MzsRE across 12 languages, targeting improvements over LU-LAFNs (77.87 Bi-ZsRE avg on bloomz-7b1-mt; MzsRE results reported as per-language heatmaps rather than a single average) particularly on portability metrics. Primary baselines: LU-LAFNs, FeatureEdit (adapted cross-lingual), MEMIT, AlphaEdit, M-MEMIT, X-KDE, LangEdit.

**Risk mitigation:** The core risk is that the portability bottleneck is NOT caused by polysemantic entanglement but by a more fundamental limitation (e.g., the portability metric itself measuring reasoning ability that editing cannot improve). We address this through: (a) explicit FCE measurement before editing to quantify the entanglement ceiling, (b) adaptive λ-projection that preserves high-FCE features, (c) reconstruction fidelity go/no-go gate, (d) ablation A3 as a direct falsification test, and (e) relational follow-up evaluation (A2) that provides a complementary portability measure independent of the Bi-ZsRE metric. If SAE features fail to improve portability, the negative result still contributes a rigorous decomposition analysis of what fraction of factual information resides in language-specific vs. language-agnostic features — valuable for the multilingual interpretability community. Fallback: hybrid approach combining SAE-projected editing for low-entanglement facts with LU-LAFNs for high-entanglement cases.

## Core Problem
Cross-lingual knowledge editing methods face two linked failures: (1) raw edit vectors reside in nearly orthogonal, language-specific subspaces (CLM-Bench), and (2) neuron-level approaches like LU-LAFNs that identify language-agnostic neurons achieve high monolingual reliability but suffer catastrophically low portability (26.43% F1, EM < 5) — a failure shared by ALL current methods (all EM < 10 on Bi-ZsRE portability), suggesting a fundamental representation-level bottleneck. We hypothesize that this bottleneck stems from polysemantic neurons entangling factual relational structure with language identity: edits that operate at neuron granularity cannot cleanly separate these components, corrupting relational knowledge during cross-lingual transfer. Can sparse autoencoder feature decomposition — which yields finer-grained, more monosemantic units — provide a cleaner separation that better preserves relational structure, and is this hypothesis even testable given recent challenges to SAE feature canonicality (Leask et al., ICLR 2025)?

## Opportunity
CLM-Bench (arXiv:2601.17397, Jan 2026) provided geometric evidence that Chinese and English edit vectors are nearly orthogonal, explaining why ROME/MEMIT fail cross-lingually (~20% reliability). LU-LAFNs (COLING 2025) achieved 77.87 avg on Bi-ZsRE by targeting language-agnostic neurons, but its neuron-level approach identifies 67.9% of neurons as LAFNs — an extremely coarse decomposition reflecting neuron polysemanticity — and ALL methods achieve near-zero portability EM (< 10 across the board), which the authors attribute to the difficulty of measuring reasoning without a reasoning process. Crucially, Mondal et al. (NAACL 2025 InsightsNLP) independently showed that neuron-level language-specific interventions are insufficient for cross-lingual transfer on XNLI/XQuAD, reinforcing the case that neuron-level decomposition is fundamentally too coarse.

Meanwhile, FeatureEdit (ACL 2025) demonstrated that SAE features outperform neurons for knowledge erasure on PrivacyParaRel (~0.80 vs ~0.65 reliability, ~0.70 vs ~0.25 generalization on Gemma-2 2B/9B) — though notably this was for privacy-knowledge erasure, not factual editing or cross-lingual propagation, so these gains may not directly transfer. LangSAE (arXiv:2601.04768) proved SAE-based language identity removal improves cross-lingual retrieval by +21.9% nDCG@20. Chou et al. (arXiv:2507.13410) achieved up to 90% language steering success by modifying a single SAE feature on Gemma-2B/9B, demonstrating that SAE-based language manipulation is feasible and precise.

However, recent work challenges SAE interventions: Peng et al. (arXiv:2506.23845) argue SAEs are better for concept discovery than acting on known concepts, finding SAE-based steering underperforms prompting/fine-tuning. Critically, Arad et al. (EMNLP 2025) rebut this: proper feature selection via output-score filtering yields 2–3× improvement in SAE steering, matching supervised methods — the issue was feature selection, not SAE interventions per se. Leask et al. (ICLR 2025) show SAE features aren't canonical atomic units — larger latents decompose into combinations — but recommend pragmatic choice of dictionary size suited to task, and our adaptive soft projection naturally accommodates non-atomicity by treating features as a continuous basis rather than binary switches.

The missing link: no work has combined SAE feature-level decomposition with cross-lingual knowledge editing. SAE features offer ~64K monosemantic units (vs. ~14K polysemantic neurons), enabling more precisely targeted language-component manipulation that may better preserve relational/factual structure — a hypothesis we propose to test directly.

## Related Work / Landscape
Cross-lingual knowledge editing is a recognized open problem: the survey (arXiv:2505.14393) identifies language anisotropy and edit scalability as key challenges. The field is structured in three tiers:

**Tier 1 — Direct multilingual editing baselines:** MEMIT/M-MEMIT apply locate-then-edit across languages (74.86 avg on Bi-ZsRE but ~20% cross-lingual reliability). AlphaEdit (ICLR 2025) uses null-space constraints. Merging Methods for MKE (arXiv:2605.13919, May 2026) explores vector merging with shared covariance for 12-language editing but without representation-level decomposition.

**Tier 2 — Neuron/representation-level multilingual editing:** LU-LAFNs (COLING 2025, arXiv:2406.16416) is the closest prior work — identifies language-agnostic factual neurons via activation frequency intersection across languages, achieving 77.87 avg on Bi-ZsRE (bloomz-7b1-mt). However, it identifies 67.9% of neurons as LAFNs (extremely coarse), and ALL methods achieve near-zero portability (EM < 10, F1 ~26-36%), which the authors acknowledge as a universal challenge rather than a method-specific failure. Mondal et al. (NAACL 2025 InsightsNLP, arXiv:2503.17456) provide independent evidence that neuron-level language-specific interventions are insufficient for cross-lingual transfer. MEMLA (arXiv:2406.11566) uses neuron masking with LoRA but doesn't leverage monosemantic features. X-KDE (ACL 2025 Findings, arXiv:2502.14645) uses instruction tuning + preference optimization (+8.19% avg improvement). LangEdit (ACL 2025 Findings, arXiv:2506.10800) applies null-space projection for multilingual sequential editing across 6 languages.

**Tier 3 — SAE-based editing and language feature work (our building blocks):** FeatureEdit from 'The Knowledge Microscope' (ACL 2025, arXiv:2502.12483) is the first SAE-feature-based model editing method — uses Gemma Scope JumpReLU SAEs to identify knowledge features and zero out specific weight positions. On the PrivacyParaRel knowledge-erasure benchmark (not factual editing), features achieve ~0.80 reliability (vs. ~0.65 for neurons) and ~0.70 generalization (vs. ~0.25), demonstrating features' advantage for representation-level interventions. However, it is monolingual English-only, targets knowledge erasure rather than cross-lingual propagation, and these gains may not directly transfer to the editing setting. SSPU (EMNLP 2025, arXiv:2505.24428) shows SAE-guided subspace projection via QR decomposition can unlearn knowledge while preserving non-target capabilities. LangSAE (arXiv:2601.04768) removes language identity from embeddings using SAE feature suppression (+21.9% nDCG@20). SAE-LAPE/LangFIR (arXiv:2604.03532) discover sparse language-specific features using activation probability contrasts. SASFT (ICLR 2026) shows SAE-guided fine-tuning preserves targeted knowledge. SpARE (NAACL 2025, arXiv:2410.15999) uses SAE-based representation engineering for knowledge selection steering but not cross-lingually. SCAN (arXiv:2603.15226, Mar 2026) uses sparse transcoders for lifelong editing on Qwen3/Llama3.1 but addresses sequential stability, not cross-lingual transfer. Farrell et al. (arXiv:2410.19278) found that zero ablation of SAE features is ineffective for knowledge unlearning — negative scaling is necessary. Chou et al. (arXiv:2507.13410) achieved up to 90% language steering success by modifying single SAE features on Gemma-2B/9B, providing direct feasibility evidence for SAE-based language manipulation.

**Tier 4 — SAE intervention skepticism and counter-evidence (critical context):** Peng et al. (arXiv:2506.23845) argue SAEs are better for discovering unknown concepts than acting on known ones, finding SAE-based steering underperforms prompting/fine-tuning. However, Arad et al. (EMNLP 2025, arXiv:2505.20063) directly rebut this: by distinguishing 'input features' (capture input patterns) from 'output features' (causally affect model behavior) and filtering by output scores, SAE steering achieves 2–3× improvement, matching supervised methods. The issue was naive feature selection, not SAE interventions as a paradigm. Zhao et al. (arXiv:2505.15038) further show denoising concept vectors via SAE improves steering 4–16%. SAE-SSV (EMNLP 2025, arXiv:2505.16188) achieves high steering success rates using supervised feature selection in sparse spaces. Leask et al. (ICLR 2025, arXiv:2502.04878) demonstrate SAE features are neither atomic nor canonical — meta-SAEs decompose latents into sub-components (e.g., 'Einstein' → 'scientist' + 'Germany' + 'famous person'), and smaller SAEs miss information captured by larger ones. They recommend pragmatic dictionary size selection rather than assuming canonicality. Our approach accommodates this by treating SAE features as a practical continuous basis with adaptive coefficients, not as binary canonical units.

**The gap:** No work combines SAE feature decomposition with cross-lingual knowledge editing. Specifically, no one has (a) used monosemantic SAE features instead of polysemantic neurons to decompose cross-lingual edit vectors, (b) tested whether finer-grained decomposition causally improves portability by preserving relational structure, or (c) engaged with the feature-selection insights from Arad et al. to ensure intervention-effective features are targeted.

## Approach
**Phase 1: Feature Classification with Output-Score Filtering (Weeks 1-2).** Leverage pre-trained SAEs — Qwen-Scope (64K features, 16× expansion) on Qwen3-8B and Llama Scope (128K features, 32× expansion) on Llama-3.1-8B — to decompose residual-stream activations at editing-critical layers (layers 12-25 for Qwen3-8B based on LU-LAFNs' LAFN distribution peaks). Classify each feature as language-specific, language-agnostic, or factual using activation-probability contrasts across Chinese, English, and 4+ additional languages (following SAE-LAPE/LangFIR methodology). Critically, following Arad et al.'s (EMNLP 2025) insight that input-pattern features and output-causal features rarely co-occur, compute output scores for all features to ensure we target features that causally affect model behavior, not merely correlational activations — this addresses the core criticism of Peng et al. For each language-specific feature f_i, compute its Factual Causal Effect (FCE): ablate f_i and measure the change in correct factual recall probability across a multilingual fact corpus of ≥5,000 facts (drawn from Bi-ZsRE + MzsRE test sets, held out from editing evaluation). FCE(f_i) = |P(correct | f_i active) - P(correct | f_i ablated)|. This produces a per-feature entanglement map. FCE is preferred over mutual information because: (a) it is causal rather than correlational, (b) it avoids the curse-of-dimensionality problems that plague MI estimation with 64K+ features (KSG estimators break down beyond ~10 dimensions), and (c) it is directly interpretable as the factual cost of removing a feature. As a computationally efficient proxy during initial screening, we also compute point-biserial correlation r_pb between feature activation magnitude and binary factual recall success, filtering to the top ~2K candidate features for full FCE ablation (reducing 64K × 5K evaluations to ~2K × 5K).

**Phase 2: SAE-Projected Editing with Adaptive Soft Projection (Weeks 3-5).** For a given ROME/MEMIT edit vector e, decompose it into the SAE feature basis: e ≈ Σ_j α_j d_j (where d_j are SAE decoder directions and α_j are coefficients from the encoder). Following Farrell et al.'s finding that binary zeroing is ineffective and Leask et al.'s evidence that features are not atomic canonical units, we apply adaptive soft projection that treats features as a continuous basis: e_proj = e - Σ_{i ∈ L_spec} λ_i · α_i · d_i, where λ_i ∈ [0, 1] is inversely proportional to FCE(f_i) — features with high factual causal effect are preserved more, pure language-identity features (low FCE, high language specificity) are fully suppressed. This formulation naturally handles Leask et al.'s non-atomicity concern: since features are weighted continuously rather than treated as binary switches, partial overlap between sub-features is accommodated through the λ gradient. The projected vector e_proj is then applied via the standard locate-then-edit pipeline.

**Phase 3: Reconstruction Fidelity Validation (Weeks 3-4, parallel).** Before full-scale editing, validate that SAE round-trip reconstruction preserves edit vector fidelity. Measure: (a) cosine similarity between original and reconstructed edit vectors, (b) monolingual edit success rate with SAE-reconstructed vectors (no language feature removal) vs. original ROME/MEMIT — this isolates reconstruction error from projection effects. If reconstruction degrades edit quality by >5%, investigate top-k sparsity adjustments or layer-specific SAE selection. Following Leask et al.'s recommendation, test multiple SAE widths (16K, 64K, 128K where available) to identify task-appropriate granularity rather than assuming larger is better. Establish a reconstruction quality threshold as a go/no-go gate.

**Phase 4: Evaluation and Ablation (Weeks 5-8).** Evaluate on CLM-Bench (1,010 zh-en pairs), Bi-ZsRE, and MzsRE (12 languages) using Qwen3-8B and Llama-3.1-8B. Primary baselines: LU-LAFNs (77.87/Bi-ZsRE on bloomz-7b1-mt — the SOTA to beat), FeatureEdit (adapted to cross-lingual setting), MEMIT, AlphaEdit, M-MEMIT, X-KDE, LangEdit. Secondary baselines: SCAN, MEMLA. Key ablations: (A1) Full zeroing vs. soft projection — measuring factual content loss, directly testing Farrell et al.'s finding in the cross-lingual setting. (A2) Relational structure preservation: for edited facts, measure whether the model correctly answers relational follow-up questions (e.g., after editing 'capital of X', test 'X is in which continent?') — this directly tests the portability hypothesis. (A3) Feature granularity: SAE features (64K/128K) vs. neuron-level LAFNs (~10K) vs. random subspace projection — if SAE features do not improve portability over neurons, this falsifies our core hypothesis. (A4) λ scheduling: fixed λ vs. FCE-adaptive λ vs. oracle λ (per-fact optimal). (A5) Layer selection: which layers' SAEs are most critical for cross-lingual transfer. (A6) SAE width: 16K vs. 64K vs. 128K features, testing Leask et al.'s prediction that task-appropriate granularity matters more than raw dictionary size. (A7) Output-score filtering (per Arad et al.): restrict projection to high-output-score features vs. all language-classified features.

## Inspiration
LU-LAFNs' universal portability failure (all methods EM < 10) revealing a fundamental representation-level bottleneck + Mondal et al.'s independent evidence that neuron-level language interventions are insufficient + FeatureEdit's demonstration that SAE features outperform neurons for knowledge erasure + LangSAE proving language features can be surgically suppressed + Chou et al.'s 90% language steering with single SAE features + CLM-Bench's geometric evidence of language-specific subspaces + SSPU's QR-decomposition subspace methodology + Arad et al.'s insight that output-score feature selection rescues SAE interventions + Farrell et al.'s finding that soft scaling outperforms zero ablation

## Key References
- LU-LAFNs: Multilingual Knowledge Editing with Language-Agnostic Factual Neurons (COLING 2025, arXiv:2406.16416) — PRIMARY BASELINE
- FeatureEdit / The Knowledge Microscope: Features as Better Analytical Lenses than Neurons (ACL 2025, arXiv:2502.12483) — METHODOLOGICAL PREDECESSOR (knowledge erasure, not editing)
- CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing (arXiv 2026, arXiv:2601.17397)
- LangSAE Editing: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal (arXiv 2026, arXiv:2601.04768)
- LangEdit: Mitigating Negative Interference in Multilingual Sequential Knowledge Editing through Null-Space Constraints (ACL 2025 Findings, arXiv:2506.10800)
- SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing (arXiv 2026, arXiv:2603.15226)
- SSPU: Model Unlearning via Sparse Autoencoder Subspace Guided Projections (EMNLP 2025, arXiv:2505.24428)
- Applying Sparse Autoencoders to Unlearn Knowledge in Language Models (arXiv 2024, arXiv:2410.19278)
- X-KDE: Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs (ACL 2025 Findings, arXiv:2502.14645)
- MEMLA: Enhancing Multilingual Knowledge Editing with Neuron-Masked Low-Rank Adaptation (arXiv 2024, arXiv:2406.11566)
- Editing Across Languages: A Survey of Multilingual Knowledge Editing (arXiv 2025, arXiv:2505.14393)
- SAE-LAPE: Unveiling Language-Specific Features in Large Language Models via Sparse Autoencoders (ACL 2025, arXiv:2505.05111)
- LinguaLens: Towards Interpreting Linguistic Mechanisms of Large Language Models via Sparse Auto-Encoder (EMNLP 2025)
- SASFT: Sparse Autoencoder-guided Supervised Finetuning to Mitigate Unexpected Code-Switching in LLMs (ICLR 2026)
- AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models (ICLR 2025)
- SpARE: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering (NAACL 2025, arXiv:2410.15999)
- LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering (arXiv 2026, arXiv:2604.03532)
- Merging Methods for Multilingual Knowledge Editing for Large Language Models: An Empirical Odyssey (arXiv 2026, arXiv:2605.13919)
- SALVE: Sparse Autoencoder-Latent Vector Editing for Mechanistic Control of Neural Networks (arXiv 2025, arXiv:2512.15938)
- Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models (arXiv 2026, arXiv:2605.11887)
- Llama Scope: Extracting Millions of Features from Llama-3.1-8B with Sparse Autoencoders (arXiv 2024, arXiv:2410.20526)
- Language-Specific Neurons: The Key to Multilingual Capabilities in Large Language Models (ACL 2024, arXiv:2402.16438)
- Peng et al.: Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts (arXiv 2025, arXiv:2506.23845) — ADVERSARIAL: argues SAEs underperform for interventions
- Leask et al.: Sparse Autoencoders Do Not Find Canonical Units of Analysis (ICLR 2025, arXiv:2502.04878) — ADVERSARIAL: shows features are not atomic/canonical
- Arad et al.: SAEs Are Good for Steering — If You Select the Right Features (EMNLP 2025, arXiv:2505.20063) — REBUTTAL to Peng et al.: output-score filtering yields 2-3× improvement
- Mondal et al.: Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer (NAACL 2025 InsightsNLP, arXiv:2503.17456) — SUPPORTS motivation: neuron-level is insufficient
- Chou et al.: Causal Language Control in Multilingual Transformers via Sparse Feature Steering (arXiv 2025, arXiv:2507.13410) — FEASIBILITY: 90% language steering with single SAE feature
- Zhao et al.: Denoising Concept Vectors with Sparse Autoencoders for Improved Language Model Steering (arXiv 2025, arXiv:2505.15038) — SAE steering improves 4-16% with denoising
- SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models (EMNLP 2025, arXiv:2505.16188)

## Resource Estimate
- **manual**: {'gpu_hours': '450-550 (SAE feature classification + FCE ablation analysis ~120h on 1×A100 — increased due to per-feature ablation; reconstruction fidelity validation across SAE widths ~40h; editing experiments across 2 models × 3 benchmarks × 8+ baselines ~250h; ablation studies A1-A7 ~120h; analysis ~40h)', 'timeline': '10-12 weeks', 'estimated_gpu_cost': '$1,125-$1,375 (A100 at ~$2.50/hr; major savings from pre-trained Qwen-Scope and Llama Scope SAEs)'}
- **human_in_loop**: {'gpu_hours': '400-500', 'timeline': '7-9 weeks', 'claude_api_cost': '$150-$250 (code generation for SAE analysis pipeline, FCE computation, experiment orchestration)', 'estimated_gpu_cost': '$1,000-$1,250'}
- **auto_research**: {'gpu_hours': '400-500', 'timeline': '5-7 weeks', 'claude_api_cost': '$400-$550 (end-to-end experiment management, hyperparameter sweeps for λ, paper drafting)', 'estimated_gpu_cost': '$1,000-$1,250', 'speed_bottleneck': 'FCE ablation requires sequential per-feature evaluation (mitigated by r_pb pre-screening to ~2K features); sequential editing experiments per model-benchmark pair; CLM-Bench evaluation involves Chinese cultural knowledge judgment requiring human spot-checking'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4974de4e-b7e6-441b-8009-479d1eed0b35",
  "type": "user",
  "uuid": "f4f480a1-242c-4f84-8c48-bfc40edbcfa8",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T21:01:40.056Z_

```json
{
  "parentUuid": "f4f480a1-242c-4f84-8c48-bfc40edbcfa8",
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
  "uuid": "18c0f4c8-8dae-47fd-88b6-7e91e001453b",
  "timestamp": "2026-05-19T21:01:40.056Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T21:01:40.056Z_

```json
{
  "parentUuid": "18c0f4c8-8dae-47fd-88b6-7e91e001453b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "840b2aef-cae4-4ae6-b0a1-54228d9f2174",
  "timestamp": "2026-05-19T21:01:40.056Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation  ## Description Current c…",
  "leafUuid": "840b2aef-cae4-4ae6-b0a1-54228d9f2174",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE feature decomposition for cross-lingual knowledge editing",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1"
}
```

---

### Assistant

_source line 8 · 2026-05-19T21:02:00.187Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate this proposal for CoRL 2026 (Conference on Robot Learning). Let me first note something important - this proposal is about cross-lingual knowledge editing in LLMs using Sparse Autoencoders (SAEs). This is an NLP/interpretability paper, NOT a robotics paper. CoRL is a robotics conference. This is a critical mismatch that I need to address.

Wait, let me re-read the task description. It says "评估其投稿 CoRL 2026 主会的中稿潜力". So they want to submit this to CoRL 2026. 

There's a fundamental problem here - this is clearly an NLP and interpretability paper about knowledge editing in language models, while CoRL focuses on robot learning, perception, manipulation, planning, and control. The venue and research area don't align at all. I should flag this as a critical issue, though I'll proceed with the evaluation as requested.

Looking at the rubric more carefully, it mentions "NLP/CL 领域的影响力" (impact on NLP/CL), which suggests the template might be designed for NLP conferences, not robotics. There's a mismatch between what the user asked me to evaluate and what the rubric is actually assessing. Regardless, I need to evaluate the core research quality and note the venue problem as a major concern.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "840b2aef-cae4-4ae6-b0a1-54228d9f2174",
  "isSidechain": false,
  "requestId": "req_011CbCbthQGnzjFVDHmgSSN2",
  "type": "assistant",
  "uuid": "8c3243cf-3d45-4fa1-b804-cf689d9838ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Y5hBgk8zhCXr66zj5Uwxz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8887,
      "cache_read_input_tokens": 13985,
      "output_tokens": 699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8887,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 699,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 8887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8887
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

_source line 9 · 2026-05-19T21:02:00.209Z_

I need to do thorough research on this proposal's domain before evaluating it. Let me first note that this proposal targets **CoRL 2026** (Conference on Robot Learning), but the content is about cross-lingual knowledge editing in LLMs — a pure NLP/interpretability topic. This is a critical venue mismatch that I'll address after completing my research.

Let me search for the key related works and current state of this field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c3243cf-3d45-4fa1-b804-cf689d9838ed",
  "isSidechain": false,
  "requestId": "req_011CbCbthQGnzjFVDHmgSSN2",
  "type": "assistant",
  "uuid": "d690cd14-bd05-47c5-bab3-8d2e48ab153f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Y5hBgk8zhCXr66zj5Uwxz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8887,
      "cache_read_input_tokens": 13985,
      "output_tokens": 699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8887,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 699,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 8887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8887
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

_source line 10 · 2026-05-19T21:02:00.219Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RFqCttE2gWJxRqMX2n2xbr`</summary>

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
  "parentUuid": "d690cd14-bd05-47c5-bab3-8d2e48ab153f",
  "isSidechain": false,
  "requestId": "req_011CbCbthQGnzjFVDHmgSSN2",
  "type": "assistant",
  "uuid": "6aa7c085-c986-442c-97ed-1064bda67876",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Y5hBgk8zhCXr66zj5Uwxz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8887,
      "cache_read_input_tokens": 13985,
      "output_tokens": 699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8887,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 699,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 8887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8887
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

_source line 11 · 2026-05-19T21:02:00.225Z_

<details><summary>↩ Tool result · `toolu_01RFqCttE2gWJxRqMX2n2xbr`</summary>

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
  "parentUuid": "6aa7c085-c986-442c-97ed-1064bda67876",
  "isSidechain": false,
  "promptId": "4974de4e-b7e6-441b-8009-479d1eed0b35",
  "type": "user",
  "uuid": "0a983b48-64e2-42c4-bda1-a3f00376b649",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "6aa7c085-c986-442c-97ed-1064bda67876",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T21:02:07.951Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now do the required research searches. I'll search for:
1. Cross-lingual knowledge editing recent papers 2025-2026
2. SAE (Sparse Autoencoder) interventions for knowledge editing
3. LU-LAFNs and portability bottleneck
4. CoRL 2026 topics and scope
5. FeatureEdit ACL 2025
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a983b48-64e2-42c4-bda1-a3f00376b649",
  "isSidechain": false,
  "requestId": "req_011CbCbvBffn97czZdLPT2Rg",
  "type": "assistant",
  "uuid": "d69724a0-8d59-4374-85ae-b22d0e64d52b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNVi2zYbGA48E3BE8fy2ui",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 22872,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 273,
          "cache_read_input_tokens": 22872,
          "cache_creation_input_tokens": 1226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1226
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

_source line 13 · 2026-05-19T21:02:08.489Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y7NVhDbK17r5dAgi719zR7`</summary>

```json
{
  "query": "cross-lingual knowledge editing LLMs 2025 2026 survey portability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d69724a0-8d59-4374-85ae-b22d0e64d52b",
  "isSidechain": false,
  "requestId": "req_011CbCbvBffn97czZdLPT2Rg",
  "type": "assistant",
  "uuid": "d146043c-f201-4b36-ac22-827b9c780af9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNVi2zYbGA48E3BE8fy2ui",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 22872,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 273,
          "cache_read_input_tokens": 22872,
          "cache_creation_input_tokens": 1226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1226
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

_source line 14 · 2026-05-19T21:02:09.437Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EJishZ2Lfcb2V99qRqb7Kz`</summary>

```json
{
  "query": "sparse autoencoder SAE feature steering intervention knowledge editing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d146043c-f201-4b36-ac22-827b9c780af9",
  "isSidechain": false,
  "requestId": "req_011CbCbvBffn97czZdLPT2Rg",
  "type": "assistant",
  "uuid": "6340b7c5-38d5-432c-8216-a4b1bbd4bef9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNVi2zYbGA48E3BE8fy2ui",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 22872,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 273,
          "cache_read_input_tokens": 22872,
          "cache_creation_input_tokens": 1226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1226
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

_source line 15 · 2026-05-19T21:02:09.542Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JRMvevgYQY8ZgTiCR9S6d8`</summary>

```json
{
  "query": "CoRL 2026 conference topics scope call for papers robot learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6340b7c5-38d5-432c-8216-a4b1bbd4bef9",
  "isSidechain": false,
  "requestId": "req_011CbCbvBffn97czZdLPT2Rg",
  "type": "assistant",
  "uuid": "0ebc493f-1981-48ae-909a-ec054fc1f6ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNVi2zYbGA48E3BE8fy2ui",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 22872,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 273,
          "cache_read_input_tokens": 22872,
          "cache_creation_input_tokens": 1226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1226
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

_source line 16 · 2026-05-19T21:02:16.439Z_

<details><summary>↩ Tool result · `toolu_01Y7NVhDbK17r5dAgi719zR7`</summary>

```text
Web search results for query: "cross-lingual knowledge editing LLMs 2025 2026 survey portability"

Links: [{"title":"Cross-Lingual Knowledge Editing in Large Language Models","url":"https://arxiv.org/pdf/2309.08952"},{"title":"Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs","url":"https://arxiv.org/pdf/2502.14645"},{"title":"Knowledge Editing for LLMs Papers","url":"https://github.com/zjunlp/KnowledgeEditingPapers"},{"title":"Retrieval-augmented Multilingual Knowledge Editing","url":"https://labs.aveni.ai/wp-content/uploads/2025/02/Retrieval-augmented-Multilingual-Knowledge-Editing.pdf"},{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge   Representation Sharing in LLMs","url":"https://arxiv.org/pdf/2408.10646"},{"title":"Editing Across Languages: A Survey of Multilingual Knowledge Editing","url":"https://alt.qcri.org/~ndurrani/pubs/EMNLP25a.pdf"},{"title":"CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing","url":"https://arxiv.org/pdf/2601.17397"}]

Based on the web search results, here's what I found about cross-lingual knowledge editing in LLMs:

## Recent Research Overview

While most existing approaches focus on monolingual editing, as LLMs are increasingly required to handle multilingual queries, monolingual solutions often fail. Several studies on multilingual knowledge editing have emerged, with some methods extending the edited language from single to multiple.

## Key Findings on Portability

Current results indicate that it remains challenging for multi-lingual LLMs to generalize the edited knowledge to other languages. Although current KE methods have achieved high reliability in monolingual settings, a successful edit should ideally propagate across languages, such as updating the "Prime Minister of the UK" in English to spontaneously correct the knowledge when queried in Chinese.

## Recent Work (2025-2026)

Several recent papers address these challenges:

- A 2025 framework called "Edit Once, Update Everywhere" addresses how LLMs need methods to update outdated information efficiently across languages.

- Recent work shows that script differences (e.g., Devanagari vs. Tamil) reduce edit transferability, highlighting script divergence as a limiting factor.

- A benchmark called CLM-Bench has been created for benchmarking and analyzing cross-lingual misalignment of LLMs in knowledge editing.

A comprehensive survey titled "Editing Across Languages: A Survey of Multilingual Knowledge Editing" is also available addressing these topics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d146043c-f201-4b36-ac22-827b9c780af9",
  "isSidechain": false,
  "promptId": "4974de4e-b7e6-441b-8009-479d1eed0b35",
  "type": "user",
  "uuid": "29117c80-31e4-44d5-9427-98ad63440296",
  "toolUseResult": {
    "query": "cross-lingual knowledge editing LLMs 2025 2026 survey portability",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BURpCyHXjUHrysUEoBreq1",
        "content": [
          {
            "title": "Cross-Lingual Knowledge Editing in Large Language Models",
            "url": "https://arxiv.org/pdf/2309.08952"
          },
          {
            "title": "Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs",
            "url": "https://arxiv.org/pdf/2502.14645"
          },
          {
            "title": "Knowledge Editing for LLMs Papers",
            "url": "https://github.com/zjunlp/KnowledgeEditingPapers"
          },
          {
            "title": "Retrieval-augmented Multilingual Knowledge Editing",
            "url": "https://labs.aveni.ai/wp-content/uploads/2025/02/Retrieval-augmented-Multilingual-Knowledge-Editing.pdf"
          },
          {
            "title": "Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge   Representation Sharing in LLMs",
            "url": "https://arxiv.org/pdf/2408.10646"
          },
          {
            "title": "Editing Across Languages: A Survey of Multilingual Knowledge Editing",
            "url": "https://alt.qcri.org/~ndurrani/pubs/EMNLP25a.pdf"
          },
          {
            "title": "CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing",
            "url": "https://arxiv.org/pdf/2601.17397"
          }
        ]
      },
      "Based on the web search results, here's what I found about cross-lingual knowledge editing in LLMs:\n\n## Recent Research Overview\n\nWhile most existing approaches focus on monolingual editing, as LLMs are increasingly required to handle multilingual queries, monolingual solutions often fail. Several studies on multilingual knowledge editing have emerged, with some methods extending the edited language from single to multiple.\n\n## Key Findings on Portability\n\nCurrent results indicate that it remains challenging for multi-lingual LLMs to generalize the edited knowledge to other languages. Although current KE methods have achieved high reliability in monolingual settings, a successful edit should ideally propagate across languages, such as updating the \"Prime Minister of the UK\" in English to spontaneously correct the knowledge when queried in Chinese.\n\n## Recent Work (2025-2026)\n\nSeveral recent papers address these challenges:\n\n- A 2025 framework called \"Edit Once, Update Everywhere\" addresses how LLMs need methods to update outdated information efficiently across languages.\n\n- Recent work shows that script differences (e.g., Devanagari vs. Tamil) reduce edit transferability, highlighting script divergence as a limiting factor.\n\n- A benchmark called CLM-Bench has been created for benchmarking and analyzing cross-lingual misalignment of LLMs in knowledge editing.\n\nA comprehensive survey titled \"Editing Across Languages: A Survey of Multilingual Knowledge Editing\" is also available addressing these topics."
    ],
    "durationSeconds": 7.9429313079999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d146043c-f201-4b36-ac22-827b9c780af9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T21:02:17.240Z_

<details><summary>↩ Tool result · `toolu_01EJishZ2Lfcb2V99qRqb7Kz`</summary>

```text
Web search results for query: "sparse autoencoder SAE feature steering intervention knowledge editing 2025 2026"

Links: [{"title":"Aligned Sparse Autoencoder (SAE)","url":"https://www.emergentmind.com/topics/aligned-sparse-autoencoder-sae"},{"title":"Feature Steering in Neural Networks","url":"https://www.emergentmind.com/topics/feature-steering"},{"title":"Sparse Autoencoder Framework","url":"https://www.emergentmind.com/topics/sparse-autoencoder-based-framework"},{"title":"Sparse Autoencoder Steering","url":"https://www.emergentmind.com/topics/sparse-autoencoder-steering"},{"title":"CorrSteer: Generation-Time LLM Steering via Correlated Sparse Autoencoder Features","url":"https://arxiv.org/html/2508.12535"},{"title":"Sparse Autoencoder Frameworks","url":"https://www.emergentmind.com/topics/sparse-autoencoder-frameworks"},{"title":"Control Reinforcement Learning: Interpretable Token-Level Steering of LLMs via Sparse Autoencoder Features","url":"https://arxiv.org/pdf/2602.10437"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based   Representation Engineering","url":"https://arxiv.org/pdf/2410.15999"}]

I found comprehensive information about recent work on sparse autoencoders (SAEs), feature steering, intervention techniques, and knowledge editing from 2025-2026. Here are the key developments:

## Steering and Control in LLMs

Automated discovery and selection of task-aligned features enable direct manipulation of reasoning paths, bias mitigation, refusal induction, and error correction with interpretable interventions (with recent work from August 2025 and January 2026).

## Knowledge Editing

Dedicated, semantically supervised concept slots permit predictable "concept swaps" or ontology-level knowledge edits in LLMs (December 2025).

## Feature Steering Methods

Recent approaches include:

- CorrSteer selects features by evaluating Pearson correlations between SAE activations and task performance metrics over held-out inference samples (August 2025)
- SAE-TS reduces the side effects of steering by linearly approximating feature directions
- SPARE utilizes Mutual Information to select features and their coefficients

## Intervention Applications

Explicit interventions in latent space can steer model outputs for fairness, safety, or instruction following. Additional applications include robust unlearning through SAE-based subspaces with increased adversarial robustness (May 2025) and hallucination detection and mitigation through SAE-driven query enrichment (March 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6340b7c5-38d5-432c-8216-a4b1bbd4bef9",
  "isSidechain": false,
  "promptId": "4974de4e-b7e6-441b-8009-479d1eed0b35",
  "type": "user",
  "uuid": "492975cb-d2fc-45db-8b26-d4c619b01469",
  "toolUseResult": {
    "query": "sparse autoencoder SAE feature steering intervention knowledge editing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Gq7HP9FgREc6b8ViYD6Tre",
        "content": [
          {
            "title": "Aligned Sparse Autoencoder (SAE)",
            "url": "https://www.emergentmind.com/topics/aligned-sparse-autoencoder-sae"
          },
          {
            "title": "Feature Steering in Neural Networks",
            "url": "https://www.emergentmind.com/topics/feature-steering"
          },
          {
            "title": "Sparse Autoencoder Framework",
            "url": "https://www.emergentmind.com/topics/sparse-autoencoder-based-framework"
          },
          {
            "title": "Sparse Autoencoder Steering",
            "url": "https://www.emergentmind.com/topics/sparse-autoencoder-steering"
          },
          {
            "title": "CorrSteer: Generation-Time LLM Steering via Correlated Sparse Autoencoder Features",
            "url": "https://arxiv.org/html/2508.12535"
          },
          {
            "title": "Sparse Autoencoder Frameworks",
            "url": "https://www.emergentmind.com/topics/sparse-autoencoder-frameworks"
          },
          {
            "title": "Control Reinforcement Learning: Interpretable Token-Level Steering of LLMs via Sparse Autoencoder Features",
            "url": "https://arxiv.org/pdf/2602.10437"
          },
          {
            "title": "Steering Knowledge Selection Behaviours in LLMs via SAE-Based   Representation Engineering",
            "url": "https://arxiv.org/pdf/2410.15999"
          }
        ]
      },
      "I found comprehensive information about recent work on sparse autoencoders (SAEs), feature steering, intervention techniques, and knowledge editing from 2025-2026. Here are the key developments:\n\n## Steering and Control in LLMs\n\nAutomated discovery and selection of task-aligned features enable direct manipulation of reasoning paths, bias mitigation, refusal induction, and error correction with interpretable interventions (with recent work from August 2025 and January 2026).\n\n## Knowledge Editing\n\nDedicated, semantically supervised concept slots permit predictable \"concept swaps\" or ontology-level knowledge edits in LLMs (December 2025).\n\n## Feature Steering Methods\n\nRecent approaches include:\n\n- CorrSteer selects features by evaluating Pearson correlations between SAE activations and task performance metrics over held-out inference samples (August 2025)\n- SAE-TS reduces the side effects of steering by linearly approximating feature directions\n- SPARE utilizes Mutual Information to select features and their coefficients\n\n## Intervention Applications\n\nExplicit interventions in latent space can steer model outputs for fairness, safety, or instruction following. Additional applications include robust unlearning through SAE-based subspaces with increased adversarial robustness (May 2025) and hallucination detection and mitigation through SAE-driven query enrichment (March 2025)."
    ],
    "durationSeconds": 7.800150243,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6340b7c5-38d5-432c-8216-a4b1bbd4bef9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T21:02:17.340Z_

<details><summary>↩ Tool result · `toolu_01JRMvevgYQY8ZgTiCR9S6d8`</summary>

```text
Web search results for query: "CoRL 2026 conference topics scope call for papers robot learning"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - About CoRL","url":"https://www.corl.org/about-corl"},{"title":"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models","url":"https://arxiv.org/pdf/2512.11908"}]

Based on the search results, here's what I found about CoRL 2026 conference topics and the call for papers:

## Conference Overview

The Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.

## Topics and Scope

CoRL welcomes papers in areas such as: Learning representations for robotic perception and control, Learning robot foundation models or general-purpose knowledge systems for robotics, Imitation learning for robotics, Reinforcement learning for control of physical robots, Learning approaches to robot safety and alignment, Applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics, Robot systems, hardware, and sensors for learning and data-driven approaches, Theoretical foundations of robot learning, including generalization theory and uncertainty quantification, and Video models and latent world models for robot learning.

CoRL covers topics including imitation learning, reinforcement learning for robots, sim-to-real transfer, robot perception through learning, learned manipulation and locomotion, and learning-based planning.

## Submission Requirements

Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.

The paper submission deadline is May 29, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ebc493f-1981-48ae-909a-ec054fc1f6ed",
  "isSidechain": false,
  "promptId": "4974de4e-b7e6-441b-8009-479d1eed0b35",
  "type": "user",
  "uuid": "4bffdf3a-9578-4abc-963e-bdafbe648c1d",
  "toolUseResult": {
    "query": "CoRL 2026 conference topics scope call for papers robot learning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JpikypHNXsv8YzExMfy1XE",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI",
            "url": "https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"
          },
          {
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "CoRL 2026 - Call for Workshops",
            "url": "https://www.corl.org/contributions/call-for-workshops"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "CoRL 2026 - About CoRL",
            "url": "https://www.corl.org/about-corl"
          },
          {
            "title": "Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models",
            "url": "https://arxiv.org/pdf/2512.11908"
          }
        ]
      },
      "Based on the search results, here's what I found about CoRL 2026 conference topics and the call for papers:\n\n## Conference Overview\n\nThe Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.\n\n## Topics and Scope\n\nCoRL welcomes papers in areas such as: Learning representations for robotic perception and control, Learning robot foundation models or general-purpose knowledge systems for robotics, Imitation learning for robotics, Reinforcement learning for control of physical robots, Learning approaches to robot safety and alignment, Applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics, Robot systems, hardware, and sensors for learning and data-driven approaches, Theoretical foundations of robot learning, including generalization theory and uncertainty quantification, and Video models and latent world models for robot learning.\n\nCoRL covers topics including imitation learning, reinforcement learning for robots, sim-to-real transfer, robot perception through learning, learned manipulation and locomotion, and learning-based planning.\n\n## Submission Requirements\n\nSubmissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\n\nThe paper submission deadline is May 29, 2026."
    ],
    "durationSeconds": 7.795363984000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0ebc493f-1981-48ae-909a-ec054fc1f6ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation  ## Description Current c…",
  "leafUuid": "4bffdf3a-9578-4abc-963e-bdafbe648c1d",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE feature decomposition for cross-lingual knowledge editing",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1"
}
```

---

### Assistant

_source line 21 · 2026-05-19T21:02:24.125Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have confirmed that CoRL 2026 is indeed about robot learning - manipulation, navigation, locomotion, reinforcement learning, etc. This NLP/interpretability paper about cross-lingual knowledge editing in LLMs is fundamentally mismatched with CoRL.

Let me do a couple more searches to verify some specific claims in the proposal and understand the SAE intervention landscape better.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bffdf3a-9578-4abc-963e-bdafbe648c1d",
  "isSidechain": false,
  "requestId": "req_011CbCbwSccfjGB3ddaMNsYM",
  "type": "assistant",
  "uuid": "fa393cf4-7be2-4c8d-974a-94c70762dbb4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pa6fKHBvTdmLvXCta2ahn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2385,
      "cache_read_input_tokens": 24098,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 24098,
          "cache_creation_input_tokens": 2385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2385
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

_source line 22 · 2026-05-19T21:02:25.155Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VB8kY6ybrXk1mmADdPEVEK`</summary>

```json
{
  "query": "LU-LAFNs language-agnostic factual neurons COLING 2025 portability EM Bi-ZsRE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa393cf4-7be2-4c8d-974a-94c70762dbb4",
  "isSidechain": false,
  "requestId": "req_011CbCbwSccfjGB3ddaMNsYM",
  "type": "assistant",
  "uuid": "82b5ce44-9460-4380-aa1c-469a136d0125",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pa6fKHBvTdmLvXCta2ahn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2385,
      "cache_read_input_tokens": 24098,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 24098,
          "cache_creation_input_tokens": 2385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2385
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

_source line 23 · 2026-05-19T21:02:26.111Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019xQ9AwiahfbuQ9rALYz85f`</summary>

```json
{
  "query": "FeatureEdit knowledge microscope ACL 2025 SAE features knowledge erasure arXiv 2502.12483"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82b5ce44-9460-4380-aa1c-469a136d0125",
  "isSidechain": false,
  "requestId": "req_011CbCbwSccfjGB3ddaMNsYM",
  "type": "assistant",
  "uuid": "5ae828da-b0b9-476f-af1b-1d751818e2f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pa6fKHBvTdmLvXCta2ahn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2385,
      "cache_read_input_tokens": 24098,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 24098,
          "cache_creation_input_tokens": 2385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2385
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

_source line 24 · 2026-05-19T21:02:33.315Z_

<details><summary>↩ Tool result · `toolu_019xQ9AwiahfbuQ9rALYz85f`</summary>

```text
Web search results for query: "FeatureEdit knowledge microscope ACL 2025 SAE features knowledge erasure arXiv 2502.12483"

Links: [{"title":"[2502.12483] The Knowledge Microscope: Features as Better Analytical Lenses than Neurons","url":"https://arxiv.org/abs/2502.12483"},{"title":"The Knowledge Microscope: Features as Better Analytical Lenses than Neurons","url":"https://arxiv.org/html/2502.12483"},{"title":"The Knowledge Microscope: Features as Better Analytical Lenses than   Neurons","url":"https://arxiv.org/pdf/2502.12483"},{"title":"Precise In-Parameter Concept Erasure in Large Language Models","url":"https://arxiv.org/pdf/2505.22586"},{"title":"Representation-Aware Unlearning via Activation Signatures: From Suppression to Knowledge-Signature Erasure","url":"https://arxiv.org/pdf/2601.10566"}]

Based on the search results, here's what I found:

The paper validates that Sparse Autoencoders (SAE) can effectively decompose neurons into features, which serve as alternative analytical units.

The research identifies three key advantages of features over neurons: (1) Features exhibit stronger influence on knowledge expression and superior interpretability. (2) Features demonstrate enhanced monosemanticity, showing distinct activation patterns between related and unrelated facts. (3) Features achieve better privacy protection than neurons, demonstrated through their proposed FeatureEdit method.

FeatureEdit achieves higher success rates in erasing privacy-sensitive knowledge from LMs while maintaining better generalization across semantically equivalent rephrase queries and causes less damage to the model's general capabilities.

The paper is titled "The Knowledge Microscope: Features as Better Analytical Lenses than Neurons" and was published on arXiv on February 27, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ae828da-b0b9-476f-af1b-1d751818e2f2",
  "isSidechain": false,
  "promptId": "4974de4e-b7e6-441b-8009-479d1eed0b35",
  "type": "user",
  "uuid": "696dff29-1790-46f8-9306-9683050eaf7f",
  "toolUseResult": {
    "query": "FeatureEdit knowledge microscope ACL 2025 SAE features knowledge erasure arXiv 2502.12483",
    "results": [
      {
        "tool_use_id": "srvtoolu_012A9mC4SyfNyVm8CKYCEqTz",
        "content": [
          {
            "title": "[2502.12483] The Knowledge Microscope: Features as Better Analytical Lenses than Neurons",
            "url": "https://arxiv.org/abs/2502.12483"
          },
          {
            "title": "The Knowledge Microscope: Features as Better Analytical Lenses than Neurons",
            "url": "https://arxiv.org/html/2502.12483"
          },
          {
            "title": "The Knowledge Microscope: Features as Better Analytical Lenses than   Neurons",
            "url": "https://arxiv.org/pdf/2502.12483"
          },
          {
            "title": "Precise In-Parameter Concept Erasure in Large Language Models",
            "url": "https://arxiv.org/pdf/2505.22586"
          },
          {
            "title": "Representation-Aware Unlearning via Activation Signatures: From Suppression to Knowledge-Signature Erasure",
            "url": "https://arxiv.org/pdf/2601.10566"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\nThe paper validates that Sparse Autoencoders (SAE) can effectively decompose neurons into features, which serve as alternative analytical units.\n\nThe research identifies three key advantages of features over neurons: (1) Features exhibit stronger influence on knowledge expression and superior interpretability. (2) Features demonstrate enhanced monosemanticity, showing distinct activation patterns between related and unrelated facts. (3) Features achieve better privacy protection than neurons, demonstrated through their proposed FeatureEdit method.\n\nFeatureEdit achieves higher success rates in erasing privacy-sensitive knowledge from LMs while maintaining better generalization across semantically equivalent rephrase queries and causes less damage to the model's general capabilities.\n\nThe paper is titled \"The Knowledge Microscope: Features as Better Analytical Lenses than Neurons\" and was published on arXiv on February 27, 2025."
    ],
    "durationSeconds": 7.200049286000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5ae828da-b0b9-476f-af1b-1d751818e2f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T21:02:34.075Z_

<details><summary>↩ Tool result · `toolu_01VB8kY6ybrXk1mmADdPEVEK`</summary>

```text
Web search results for query: "LU-LAFNs language-agnostic factual neurons COLING 2025 portability EM Bi-ZsRE"

Links: [{"title":"Multilingual Knowledge Editing with Language-Agnostic Factual Neurons - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.385/"},{"title":"Multilingual Knowledge Editing with Language-Agnostic Factual Neurons","url":"https://arxiv.org/html/2406.16416"},{"title":"Multilingual Knowledge Editing with Language-Agnostic Factual Neurons","url":"https://arxiv.org/pdf/2406.16416"},{"title":"Multilingual Knowledge Editing with Language-Agnostic ...","url":"https://aclanthology.org/2025.coling-main.385.pdf"},{"title":"[2406.16416] Multilingual Knowledge Editing with Language-Agnostic Factual Neurons","url":"https://arxiv.org/abs/2406.16416"},{"title":"Multilingual Knowledge Editing with Language-Agnostic Factual Neurons - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240616416Z/abstract"}]

Based on the search results, here's what I found about LU-LAFNs:

## Overview

LU-LAFNs (Locating and Updating Language-Agnostic Factual Neurons) is a method for multilingual knowledge editing that edits multilingual knowledge simultaneously.

## Key Concepts

The research discovers that the same factual knowledge in different languages generally activates a shared set of neurons, which are called language-agnostic factual neurons (LAFNs). These neurons represent the same factual knowledge shared across languages and imply the semantic connections among multilingual knowledge.

## Methodology

The LU-LAFNs architecture locates the corresponding language-agnostic factual neurons, then optimizes update values for modifying them, and stores the results in cache.

## Experimental Results

Experimental results on Bi-ZsRE and MzsRE benchmarks demonstrate that the method achieves the best edit performance, indicating the effectiveness of modeling the semantic connections among multilingual knowledge.

## Publication

The paper was published at COLING 2025, as indicated by the ACL Anthology entry for the conference held January 19-24, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82b5ce44-9460-4380-aa1c-469a136d0125",
  "isSidechain": false,
  "promptId": "4974de4e-b7e6-441b-8009-479d1eed0b35",
  "type": "user",
  "uuid": "b6cfe6ff-3c20-472e-b296-159ecaebf415",
  "toolUseResult": {
    "query": "LU-LAFNs language-agnostic factual neurons COLING 2025 portability EM Bi-ZsRE",
    "results": [
      {
        "tool_use_id": "srvtoolu_011h74VHfBXfc78yXkhBxpYk",
        "content": [
          {
            "title": "Multilingual Knowledge Editing with Language-Agnostic Factual Neurons - ACL Anthology",
            "url": "https://aclanthology.org/2025.coling-main.385/"
          },
          {
            "title": "Multilingual Knowledge Editing with Language-Agnostic Factual Neurons",
            "url": "https://arxiv.org/html/2406.16416"
          },
          {
            "title": "Multilingual Knowledge Editing with Language-Agnostic Factual Neurons",
            "url": "https://arxiv.org/pdf/2406.16416"
          },
          {
            "title": "Multilingual Knowledge Editing with Language-Agnostic ...",
            "url": "https://aclanthology.org/2025.coling-main.385.pdf"
          },
          {
            "title": "[2406.16416] Multilingual Knowledge Editing with Language-Agnostic Factual Neurons",
            "url": "https://arxiv.org/abs/2406.16416"
          },
          {
            "title": "Multilingual Knowledge Editing with Language-Agnostic Factual Neurons - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240616416Z/abstract"
          }
        ]
      },
      "Based on the search results, here's what I found about LU-LAFNs:\n\n## Overview\n\nLU-LAFNs (Locating and Updating Language-Agnostic Factual Neurons) is a method for multilingual knowledge editing that edits multilingual knowledge simultaneously.\n\n## Key Concepts\n\nThe research discovers that the same factual knowledge in different languages generally activates a shared set of neurons, which are called language-agnostic factual neurons (LAFNs). These neurons represent the same factual knowledge shared across languages and imply the semantic connections among multilingual knowledge.\n\n## Methodology\n\nThe LU-LAFNs architecture locates the corresponding language-agnostic factual neurons, then optimizes update values for modifying them, and stores the results in cache.\n\n## Experimental Results\n\nExperimental results on Bi-ZsRE and MzsRE benchmarks demonstrate that the method achieves the best edit performance, indicating the effectiveness of modeling the semantic connections among multilingual knowledge.\n\n## Publication\n\nThe paper was published at COLING 2025, as indicated by the ACL Anthology entry for the conference held January 19-24, 2025."
    ],
    "durationSeconds": 8.916244612999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "82b5ce44-9460-4380-aa1c-469a136d0125",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T21:02:40.182Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FgthoDiPd1PTkYZ6BHMFF8`</summary>

```json
{
  "query": "Peng et al \"sparse autoencoders\" \"unknown concepts\" \"not to act\" 2025 arXiv 2506.23845"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6cfe6ff-3c20-472e-b296-159ecaebf415",
  "isSidechain": false,
  "requestId": "req_011CbCbxgAE7djd1hxpN2Juo",
  "type": "assistant",
  "uuid": "108b7172-b16d-418f-b24e-f0713af81bf7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NSYstEkx5Q85gLrxnedy8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 497,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 26483,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 873,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 497,
          "output_tokens": 150,
          "cache_read_input_tokens": 26483,
          "cache_creation_input_tokens": 873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 873
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

_source line 27 · 2026-05-19T21:02:41.379Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GJb6Qy7TWnmLhsFRgiLshT`</summary>

```json
{
  "query": "Arad et al \"SAEs are good for steering\" \"select the right features\" EMNLP 2025 output-score"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "108b7172-b16d-418f-b24e-f0713af81bf7",
  "isSidechain": false,
  "requestId": "req_011CbCbxgAE7djd1hxpN2Juo",
  "type": "assistant",
  "uuid": "c03489a3-5e2b-494a-8232-4c99f62620be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NSYstEkx5Q85gLrxnedy8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 497,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 26483,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 873,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 497,
          "output_tokens": 150,
          "cache_read_input_tokens": 26483,
          "cache_creation_input_tokens": 873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 873
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

_source line 28 · 2026-05-19T21:02:46.497Z_

<details><summary>↩ Tool result · `toolu_01GJb6Qy7TWnmLhsFRgiLshT`</summary>

```text
Web search results for query: "Arad et al "SAEs are good for steering" "select the right features" EMNLP 2025 output-score"

Links: [{"title":"SAEs Are Good for Steering – If You Select the Right Features - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.519/"},{"title":"SAEs Are Good for Steering -- If You Select the Right Features | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/saes-are-good-steering-if-you-select"},{"title":"SAEs Are Good for Steering – If You Select the Right Features","url":"https://www.researchgate.net/publication/397422533_SAEs_Are_Good_for_Steering_-_If_You_Select_the_Right_Features"},{"title":"SAEs Are Good for Steering -- If You Select the Right Features - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250520063A/abstract"},{"title":"Feature Steering in Neural Networks","url":"https://www.emergentmind.com/topics/feature-steering"},{"title":"The Rogue Scalpel: Activation Steering Compromises LLM Safety","url":"https://arxiv.org/html/2509.22067v2"},{"title":"Enhancing LLM Steering through Sparse Autoencoder-Based Vector Refinement","url":"https://arxiv.org/html/2509.23799v2"},{"title":"SAEs Are Good for Steering -- If You Select the Right Features","url":"https://arxiv.org/pdf/2505.20063"}]

Perfect! I found the paper you were looking for. Here are the key details:

**Paper:** SAEs Are Good for Steering – If You Select the Right Features by Arad et al., published at EMNLP 2025

**Main Contribution:** The paper distinguishes between input features (which mainly capture patterns in the model's input) and output features (those that have a human-understandable effect on the model's output), and proposes input and output scores to characterize and locate these types of features.

**Output Score:** The output score is computed based on the rank and probability of representatives after intervention, with features having high output scores being more likely to be effective for steering.

**Key Finding:** After filtering out features with low output scores, steering with SAEs results in a 2–3x improvement, matching the performance of existing supervised methods.

The paper is available on the ACL Anthology at https://aclanthology.org/2025.emnlp-main.519/ and also on arXiv as arXiv:2505.20063.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c03489a3-5e2b-494a-8232-4c99f62620be",
  "isSidechain": false,
  "promptId": "4974de4e-b7e6-441b-8009-479d1eed0b35",
  "type": "user",
  "uuid": "8a00a543-bc83-4cf2-b3ad-9427ba1cf986",
  "toolUseResult": {
    "query": "Arad et al \"SAEs are good for steering\" \"select the right features\" EMNLP 2025 output-score",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CrzyqZBPGnfsdq3UFFNJzv",
        "content": [
          {
            "title": "SAEs Are Good for Steering – If You Select the Right Features - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.519/"
          },
          {
            "title": "SAEs Are Good for Steering -- If You Select the Right Features | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/saes-are-good-steering-if-you-select"
          },
          {
            "title": "SAEs Are Good for Steering – If You Select the Right Features",
            "url": "https://www.researchgate.net/publication/397422533_SAEs_Are_Good_for_Steering_-_If_You_Select_the_Right_Features"
          },
          {
            "title": "SAEs Are Good for Steering -- If You Select the Right Features - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250520063A/abstract"
          },
          {
            "title": "Feature Steering in Neural Networks",
            "url": "https://www.emergentmind.com/topics/feature-steering"
          },
          {
            "title": "The Rogue Scalpel: Activation Steering Compromises LLM Safety",
            "url": "https://arxiv.org/html/2509.22067v2"
          },
          {
            "title": "Enhancing LLM Steering through Sparse Autoencoder-Based Vector Refinement",
            "url": "https://arxiv.org/html/2509.23799v2"
          },
          {
            "title": "SAEs Are Good for Steering -- If You Select the Right Features",
            "url": "https://arxiv.org/pdf/2505.20063"
          }
        ]
      },
      "Perfect! I found the paper you were looking for. Here are the key details:\n\n**Paper:** SAEs Are Good for Steering – If You Select the Right Features by Arad et al., published at EMNLP 2025\n\n**Main Contribution:** The paper distinguishes between input features (which mainly capture patterns in the model's input) and output features (those that have a human-understandable effect on the model's output), and proposes input and output scores to characterize and locate these types of features.\n\n**Output Score:** The output score is computed based on the rank and probability of representatives after intervention, with features having high output scores being more likely to be effective for steering.\n\n**Key Finding:** After filtering out features with low output scores, steering with SAEs results in a 2–3x improvement, matching the performance of existing supervised methods.\n\nThe paper is available on the ACL Anthology at https://aclanthology.org/2025.emnlp-main.519/ and also on arXiv as arXiv:2505.20063."
    ],
    "durationSeconds": 5.112695002000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c03489a3-5e2b-494a-8232-4c99f62620be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T21:02:48.851Z_

<details><summary>↩ Tool result · `toolu_01FgthoDiPd1PTkYZ6BHMFF8`</summary>

```text
Web search results for query: "Peng et al "sparse autoencoders" "unknown concepts" "not to act" 2025 arXiv 2506.23845"

Links: [{"title":"[2506.23845] Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts","url":"https://arxiv.org/abs/2506.23845"},{"title":"[2506.23845v1] Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts","url":"https://arxiv.org/abs/2506.23845v1"},{"title":"Kenny Peng","url":"https://kennypeng.me/"},{"title":"(PDF) Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts","url":"https://www.researchgate.net/publication/393183364_Use_Sparse_Autoencoders_to_Discover_Unknown_Concepts_Not_to_Act_on_Known_Concepts"},{"title":"Sparse Autoencoders for Concept Discovery","url":"https://www.emergentmind.com/papers/2506.23845"},{"title":"ActivationReasoning: Logical Reasoning in Latent Activation Spaces","url":"https://arxiv.org/html/2510.18184v1"},{"title":"Causal Effect Estimation with Latent Textual Treatments","url":"https://arxiv.org/html/2602.15730v1"},{"title":"Re-envisioning Euclid Galaxy Morphology: Identifying and Interpreting Features with Sparse Autoencoders","url":"https://arxiv.org/html/2510.23749v2"},{"title":"Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/use-sparse-autoencoders-discover-unknown-concepts-not"},{"title":"Sparse Shift Autoencoders for Identifying Concepts from Large Language Model Activations","url":"https://arxiv.org/pdf/2502.12179"}]

I found the paper! Here's the information about the research:

The paper is titled "Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts" by Kenny Peng and 4 other authors, with arXiv identifier 2506.23845. The authors are Kenny Peng, Rajiv Movva, Jon Kleinberg, Emma Pierson, and Nikhil Garg.

**Main Argument:**
The paper argues that while SAEs may be less effective for acting on known concepts, SAEs are powerful tools for discovering unknown concepts. The work establishes a conceptual distinction that reconciles competing narratives surrounding SAEs.

**Applications:**
The authors outline use cases for SAEs in (i) ML interpretability, explainability, fairness, auditing, and safety, and (ii) social and health sciences.

The paper was submitted on June 30, 2025, and is available on arXiv at https://arxiv.org/abs/2506.23845.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "108b7172-b16d-418f-b24e-f0713af81bf7",
  "isSidechain": false,
  "promptId": "4974de4e-b7e6-441b-8009-479d1eed0b35",
  "type": "user",
  "uuid": "5471b8eb-2799-4e61-901a-6b30676c0a05",
  "toolUseResult": {
    "query": "Peng et al \"sparse autoencoders\" \"unknown concepts\" \"not to act\" 2025 arXiv 2506.23845",
    "results": [
      {
        "tool_use_id": "srvtoolu_018MkmphEk99aembFf8imrDe",
        "content": [
          {
            "title": "[2506.23845] Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts",
            "url": "https://arxiv.org/abs/2506.23845"
          },
          {
            "title": "[2506.23845v1] Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts",
            "url": "https://arxiv.org/abs/2506.23845v1"
          },
          {
            "title": "Kenny Peng",
            "url": "https://kennypeng.me/"
          },
          {
            "title": "(PDF) Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts",
            "url": "https://www.researchgate.net/publication/393183364_Use_Sparse_Autoencoders_to_Discover_Unknown_Concepts_Not_to_Act_on_Known_Concepts"
          },
          {
            "title": "Sparse Autoencoders for Concept Discovery",
            "url": "https://www.emergentmind.com/papers/2506.23845"
          },
          {
            "title": "ActivationReasoning: Logical Reasoning in Latent Activation Spaces",
            "url": "https://arxiv.org/html/2510.18184v1"
          },
          {
            "title": "Causal Effect Estimation with Latent Textual Treatments",
            "url": "https://arxiv.org/html/2602.15730v1"
          },
          {
            "title": "Re-envisioning Euclid Galaxy Morphology: Identifying and Interpreting Features with Sparse Autoencoders",
            "url": "https://arxiv.org/html/2510.23749v2"
          },
          {
            "title": "Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/use-sparse-autoencoders-discover-unknown-concepts-not"
          },
          {
            "title": "Sparse Shift Autoencoders for Identifying Concepts from Large Language Model Activations",
            "url": "https://arxiv.org/pdf/2502.12179"
          }
        ]
      },
      "I found the paper! Here's the information about the research:\n\nThe paper is titled \"Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts\" by Kenny Peng and 4 other authors, with arXiv identifier 2506.23845. The authors are Kenny Peng, Rajiv Movva, Jon Kleinberg, Emma Pierson, and Nikhil Garg.\n\n**Main Argument:**\nThe paper argues that while SAEs may be less effective for acting on known concepts, SAEs are powerful tools for discovering unknown concepts. The work establishes a conceptual distinction that reconciles competing narratives surrounding SAEs.\n\n**Applications:**\nThe authors outline use cases for SAEs in (i) ML interpretability, explainability, fairness, auditing, and safety, and (ii) social and health sciences.\n\nThe paper was submitted on June 30, 2025, and is available on arXiv at https://arxiv.org/abs/2506.23845."
    ],
    "durationSeconds": 8.665620516999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "108b7172-b16d-418f-b24e-f0713af81bf7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-19T21:03:00.898Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check if there's any existing work that already combines SAE with cross-lingual knowledge editing, and also verify some of the other key claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5471b8eb-2799-4e61-901a-6b30676c0a05",
  "isSidechain": false,
  "requestId": "req_011CbCbymRWPwpc1TaWQurPb",
  "type": "assistant",
  "uuid": "7a2403de-affb-49eb-a8ac-0011e8f0c71c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdEQVGKWzGreJceZPpYXvM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 697,
      "cache_creation_input_tokens": 1458,
      "cache_read_input_tokens": 27356,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1458,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 697,
          "output_tokens": 190,
          "cache_read_input_tokens": 27356,
          "cache_creation_input_tokens": 1458,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1458
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

_source line 31 · 2026-05-19T21:03:01.256Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WcuZmnksgCLjTzFom9s7Gf`</summary>

```json
{
  "query": "SAE sparse autoencoder cross-lingual knowledge editing multilingual factual editing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a2403de-affb-49eb-a8ac-0011e8f0c71c",
  "isSidechain": false,
  "requestId": "req_011CbCbymRWPwpc1TaWQurPb",
  "type": "assistant",
  "uuid": "b58b1550-ad9f-4211-9045-afeb722e4a02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdEQVGKWzGreJceZPpYXvM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 697,
      "cache_creation_input_tokens": 1458,
      "cache_read_input_tokens": 27356,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1458,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 697,
          "output_tokens": 190,
          "cache_read_input_tokens": 27356,
          "cache_creation_input_tokens": 1458,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1458
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

_source line 32 · 2026-05-19T21:03:02.330Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014rXdyfDPJrnYaVjn7q3BLx`</summary>

```json
{
  "query": "Chou et al \"causal language control\" multilingual SAE feature steering Gemma 2025 arXiv 2507.13410"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b58b1550-ad9f-4211-9045-afeb722e4a02",
  "isSidechain": false,
  "requestId": "req_011CbCbymRWPwpc1TaWQurPb",
  "type": "assistant",
  "uuid": "8935d92b-d774-40af-a2b2-b654c6d4799f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdEQVGKWzGreJceZPpYXvM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 697,
      "cache_creation_input_tokens": 1458,
      "cache_read_input_tokens": 27356,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1458,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 697,
          "output_tokens": 190,
          "cache_read_input_tokens": 27356,
          "cache_creation_input_tokens": 1458,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1458
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation  ## Description Current c…",
  "leafUuid": "8935d92b-d774-40af-a2b2-b654c6d4799f",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE feature decomposition for cross-lingual knowledge editing",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1"
}
```

---

### Tool result

_source line 35 · 2026-05-19T21:03:08.728Z_

<details><summary>↩ Tool result · `toolu_014rXdyfDPJrnYaVjn7q3BLx`</summary>

```text
Web search results for query: "Chou et al "causal language control" multilingual SAE feature steering Gemma 2025 arXiv 2507.13410"

Links: [{"title":"Causal Language Control in Multilingual Transformers via Sparse Feature Steering","url":"https://arxiv.org/html/2507.13410v1"},{"title":"[2507.13410] Causal Language Control in Multilingual Transformers via Sparse Feature Steering","url":"https://arxiv.org/abs/2507.13410"},{"title":"Causal Language Control in Multilingual Transformers via Sparse Feature","url":"https://arxiv.org/pdf/2507.13410"},{"title":"Causal Language Control in Multilingual Transformers via Sparse Feature Steering | Algoverse | Algoverse AI Research","url":"https://algoverseairesearch.org/news/causal-language-control"},{"title":"Artificial Intelligence Jul 2025","url":"https://arxiv.org/list/cs.AI/2025-07?skip=2325&show=2000"},{"title":"LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering","url":"https://arxiv.org/pdf/2604.03532"}]

I found the paper you're looking for! Here's what the search revealed:

"Causal Language Control in Multilingual Transformers via Sparse Feature Steering" by Chou et al. investigates whether sparse autoencoder (SAE) features can be leveraged to steer the generated language of LLMs during inference, using pretrained SAEs on the residual streams of Gemma-2B and Gemma-9B to identify features whose activations differ most significantly between English and four target languages: Chinese, Japanese, Spanish, and French.

By modifying just a single SAE feature at one transformer layer, they achieve controlled language shifts with up to 90% success, as measured by FastText language classification, while preserving semantic fidelity according to LaBSE (Language-Agnostic BERT Sentence Embedding) similarity.

Their analysis reveals that language steering is most effective in mid-to-late transformer layers and is amplified by specific attention heads disproportionately associated with language-sensitive SAE features.

The paper was published on arXiv as 2507.13410 in July 2025. You can access it directly at https://arxiv.org/abs/2507.13410.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8935d92b-d774-40af-a2b2-b654c6d4799f",
  "isSidechain": false,
  "promptId": "4974de4e-b7e6-441b-8009-479d1eed0b35",
  "type": "user",
  "uuid": "896d9265-dba3-47a6-ac84-e8093c9c8bc5",
  "toolUseResult": {
    "query": "Chou et al \"causal language control\" multilingual SAE feature steering Gemma 2025 arXiv 2507.13410",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GGZ5dqcS5Wq8HYxEHKTWPG",
        "content": [
          {
            "title": "Causal Language Control in Multilingual Transformers via Sparse Feature Steering",
            "url": "https://arxiv.org/html/2507.13410v1"
          },
          {
            "title": "[2507.13410] Causal Language Control in Multilingual Transformers via Sparse Feature Steering",
            "url": "https://arxiv.org/abs/2507.13410"
          },
          {
            "title": "Causal Language Control in Multilingual Transformers via Sparse Feature",
            "url": "https://arxiv.org/pdf/2507.13410"
          },
          {
            "title": "Causal Language Control in Multilingual Transformers via Sparse Feature Steering | Algoverse | Algoverse AI Research",
            "url": "https://algoverseairesearch.org/news/causal-language-control"
          },
          {
            "title": "Artificial Intelligence Jul 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-07?skip=2325&show=2000"
          },
          {
            "title": "LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering",
            "url": "https://arxiv.org/pdf/2604.03532"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search revealed:\n\n\"Causal Language Control in Multilingual Transformers via Sparse Feature Steering\" by Chou et al. investigates whether sparse autoencoder (SAE) features can be leveraged to steer the generated language of LLMs during inference, using pretrained SAEs on the residual streams of Gemma-2B and Gemma-9B to identify features whose activations differ most significantly between English and four target languages: Chinese, Japanese, Spanish, and French.\n\nBy modifying just a single SAE feature at one transformer layer, they achieve controlled language shifts with up to 90% success, as measured by FastText language classification, while preserving semantic fidelity according to LaBSE (Language-Agnostic BERT Sentence Embedding) similarity.\n\nTheir analysis reveals that language steering is most effective in mid-to-late transformer layers and is amplified by specific attention heads disproportionately associated with language-sensitive SAE features.\n\nThe paper was published on arXiv as 2507.13410 in July 2025. You can access it directly at https://arxiv.org/abs/2507.13410."
    ],
    "durationSeconds": 6.393935901999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8935d92b-d774-40af-a2b2-b654c6d4799f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T21:03:08.809Z_

<details><summary>↩ Tool result · `toolu_01WcuZmnksgCLjTzFom9s7Gf`</summary>

```text
Web search results for query: "SAE sparse autoencoder cross-lingual knowledge editing multilingual factual editing 2025 2026"

Links: [{"title":"LANGSAE EDITING: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal","url":"https://arxiv.org/pdf/2601.04768"},{"title":"Multilingual Knowledge Editing with Language-Agnostic Factual Neurons","url":"https://arxiv.org/pdf/2406.16416"},{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge   Representation Sharing in LLMs","url":"https://arxiv.org/pdf/2408.10646"},{"title":"LangSAE Editing: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal","url":"https://arxiv.org/html/2601.04768"},{"title":"Sparse Autoencoder Features for Classifications and Transferability","url":"https://aclanthology.org/2025.emnlp-main.1521.pdf"},{"title":"Mass-Editing Memory with Attention in Transformers: A cross-lingual   exploration of knowledge","url":"https://arxiv.org/pdf/2502.02173"},{"title":"[2507.11230] Sparse Autoencoders Can Capture Language-Specific Concepts Across Diverse Languages","url":"https://arxiv.org/abs/2507.11230"},{"title":"Qwen AI Releases Qwen-Scope: An Open-Source Sparse AutoEncoders (SAE) Suite That Turns LLM Internal Features into Practical Development Tools - MarkTechPost","url":"https://www.marktechpost.com/2026/05/01/qwen-ai-releases-qwen-scope-an-open-source-sparse-autoencoders-sae-suite-that-turns-llm-internal-features-into-practical-development-tools/"},{"title":"Causal Language Control in Multilingual Transformers via Sparse Feature Steering","url":"https://arxiv.org/pdf/2507.13410"},{"title":"Sparse Autoencoder Features for Classifications and Transferability - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1521/"}]

Based on the search results, I found several relevant papers on SAEs (Sparse Autoencoders) applied to cross-lingual and multilingual tasks:

## Key Research Areas:

### 1. **LangSAE Editing for Multilingual Information Retrieval**
LangSAE is an overcomplete sparse autoencoder trained on pooled embeddings, enabling language-associated factors to concentrate into latent units that can be selectively suppressed. This approach improves macro-average nDCG@20 by about +21.9% and +20.6% across Belebele and XQuAD benchmarks, respectively.

### 2. **SAEs for Language-Specific Concept Representation**
Researchers have explored sparse autoencoders for their ability to learn monosemantic features that represent concrete and abstract concepts across languages in LLMs. Features discovered in English transfer meaningfully to other languages without rediscovery, with performance declining with linguistic distance.

### 3. **Multilingual Knowledge Editing**
Multilingual knowledge editing (MKE) aims to simultaneously rectify factual knowledge across multilingual languages within large language models without resource-intensive retraining, presenting more challenges than monolingual knowledge editing since edited knowledge should be consistent across multiple languages.

### 4. **SAE-based Language Control**
Recent work on sparse autoencoders shows that transformer residual streams can be decomposed into interpretable directions, and methods such as Feature-Guided Activation Additions and SAE-Targeted Steering demonstrate that selectively activating SAE features can causally steer LLM behavior.

These papers represent recent advances (2025-2026) in applying SAEs to multilingual and cross-lingual tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b58b1550-ad9f-4211-9045-afeb722e4a02",
  "isSidechain": false,
  "promptId": "4974de4e-b7e6-441b-8009-479d1eed0b35",
  "type": "user",
  "uuid": "7fd40655-0f34-4942-8d1a-c3b9daddb10e",
  "toolUseResult": {
    "query": "SAE sparse autoencoder cross-lingual knowledge editing multilingual factual editing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011tMRfyUaoisBEyrazciJLp",
        "content": [
          {
            "title": "LANGSAE EDITING: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal",
            "url": "https://arxiv.org/pdf/2601.04768"
          },
          {
            "title": "Multilingual Knowledge Editing with Language-Agnostic Factual Neurons",
            "url": "https://arxiv.org/pdf/2406.16416"
          },
          {
            "title": "Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge   Representation Sharing in LLMs",
            "url": "https://arxiv.org/pdf/2408.10646"
          },
          {
            "title": "LangSAE Editing: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal",
            "url": "https://arxiv.org/html/2601.04768"
          },
          {
            "title": "Sparse Autoencoder Features for Classifications and Transferability",
            "url": "https://aclanthology.org/2025.emnlp-main.1521.pdf"
          },
          {
            "title": "Mass-Editing Memory with Attention in Transformers: A cross-lingual   exploration of knowledge",
            "url": "https://arxiv.org/pdf/2502.02173"
          },
          {
            "title": "[2507.11230] Sparse Autoencoders Can Capture Language-Specific Concepts Across Diverse Languages",
            "url": "https://arxiv.org/abs/2507.11230"
          },
          {
            "title": "Qwen AI Releases Qwen-Scope: An Open-Source Sparse AutoEncoders (SAE) Suite That Turns LLM Internal Features into Practical Development Tools - MarkTechPost",
            "url": "https://www.marktechpost.com/2026/05/01/qwen-ai-releases-qwen-scope-an-open-source-sparse-autoencoders-sae-suite-that-turns-llm-internal-features-into-practical-development-tools/"
          },
          {
            "title": "Causal Language Control in Multilingual Transformers via Sparse Feature Steering",
            "url": "https://arxiv.org/pdf/2507.13410"
          },
          {
            "title": "Sparse Autoencoder Features for Classifications and Transferability - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.1521/"
          }
        ]
      },
      "Based on the search results, I found several relevant papers on SAEs (Sparse Autoencoders) applied to cross-lingual and multilingual tasks:\n\n## Key Research Areas:\n\n### 1. **LangSAE Editing for Multilingual Information Retrieval**\nLangSAE is an overcomplete sparse autoencoder trained on pooled embeddings, enabling language-associated factors to concentrate into latent units that can be selectively suppressed. This approach improves macro-average nDCG@20 by about +21.9% and +20.6% across Belebele and XQuAD benchmarks, respectively.\n\n### 2. **SAEs for Language-Specific Concept Representation**\nResearchers have explored sparse autoencoders for their ability to learn monosemantic features that represent concrete and abstract concepts across languages in LLMs. Features discovered in English transfer meaningfully to other languages without rediscovery, with performance declining with linguistic distance.\n\n### 3. **Multilingual Knowledge Editing**\nMultilingual knowledge editing (MKE) aims to simultaneously rectify factual knowledge across multilingual languages within large language models without resource-intensive retraining, presenting more challenges than monolingual knowledge editing since edited knowledge should be consistent across multiple languages.\n\n### 4. **SAE-based Language Control**\nRecent work on sparse autoencoders shows that transformer residual streams can be decomposed into interpretable directions, and methods such as Feature-Guided Activation Additions and SAE-Targeted Steering demonstrate that selectively activating SAE features can causally steer LLM behavior.\n\nThese papers represent recent advances (2025-2026) in applying SAEs to multilingual and cross-lingual tasks."
    ],
    "durationSeconds": 7.548645061999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b58b1550-ad9f-4211-9045-afeb722e4a02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-19T21:03:08.813Z_

```json
{
  "parentUuid": "7fd40655-0f34-4942-8d1a-c3b9daddb10e",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "286a5140-388b-4771-ad66-f3aa35ea7951",
  "timestamp": "2026-05-19T21:03:08.813Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 38 · 2026-05-19T21:03:13.731Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information. Let me also check one more important thing - whether there's already a paper combining SAEs with cross-lingual knowledge editing (not just retrieval like LangSAE).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "286a5140-388b-4771-ad66-f3aa35ea7951",
  "isSidechain": false,
  "requestId": "req_011CbCc1EgsjNcYD1Hhbmbpc",
  "type": "assistant",
  "uuid": "99b3772e-4a96-4a68-8aa3-4a0d6b4cdd33",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016R7LijKy85NJq8hxykjqcJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 637,
      "cache_creation_input_tokens": 1981,
      "cache_read_input_tokens": 28814,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1981,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 637,
          "output_tokens": 139,
          "cache_read_input_tokens": 28814,
          "cache_creation_input_tokens": 1981,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1981
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

_source line 39 · 2026-05-19T21:03:14.647Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UsUqost5JqnXJdLLchqNzq`</summary>

```json
{
  "query": "\"SCAN\" sparse circuit anchor lifelong knowledge editing Qwen Llama 2026 arXiv 2603.15226"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99b3772e-4a96-4a68-8aa3-4a0d6b4cdd33",
  "isSidechain": false,
  "requestId": "req_011CbCc1EgsjNcYD1Hhbmbpc",
  "type": "assistant",
  "uuid": "06989e69-8723-476c-ae91-cceebeff8557",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016R7LijKy85NJq8hxykjqcJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 637,
      "cache_creation_input_tokens": 1981,
      "cache_read_input_tokens": 28814,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1981,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 637,
          "output_tokens": 139,
          "cache_read_input_tokens": 28814,
          "cache_creation_input_tokens": 1981,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1981
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

_source line 40 · 2026-05-19T21:03:21.168Z_

<details><summary>↩ Tool result · `toolu_01UsUqost5JqnXJdLLchqNzq`</summary>

```text
Web search results for query: ""SCAN" sparse circuit anchor lifelong knowledge editing Qwen Llama 2026 arXiv 2603.15226"

Links: [{"title":"SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing","url":"https://arxiv.org/pdf/2603.15226"},{"title":"Representation Interventions Enable Lifelong Unstructured Knowledge Control","url":"https://arxiv.org/pdf/2511.20892"},{"title":"Lifelong Knowledge Editing requires Better Regularization","url":"https://arxiv.org/pdf/2502.01636"},{"title":"Beyond Hard Writes and Rigid Preservation: Soft Recursive Least-Squares for Lifelong LLM Editing","url":"https://arxiv.org/pdf/2601.15686"},{"title":"MEMOIR: Lifelong Model Editing with Minimal Overwrite and Informed Retention for LLMs","url":"https://arxiv.org/pdf/2506.07899"},{"title":"Lifelong Knowledge Editing for LLMs with Retrieval-Augmented Continuous   Prompt Learning","url":"https://arxiv.org/pdf/2405.03279"}]

I found the paper! Here are the search results for your query:

**SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing** is a paper by Yuhuan Liu, Haitian Zhong, Xinyuan Xia, Qiang Liu, Shu Wu, and Liang Wang that addresses catastrophic forgetting and collapse in Large Language Models during sequential knowledge editing.

The paper identifies that the problem stems from dense editing paradigms treating models as black boxes, and proposes SCAN—a sparse editing framework based on Sparse Circuit Anchored Neuron which transforms editing into mechanism-aware manipulation by constructing a knowledge circuit via Sparse Transcoders.

Experiments on Gemma2, Qwen3, and Llama3.1 across CounterFact, ZsRE and WikiFactDiff demonstrate that SCAN achieves superior performance, maintaining model integrity on benchmarks like MMLU and GSM8K even after 3,000 sequential edits, whereas existing methods deteriorate progressively.

The paper is available on arXiv at: https://arxiv.org/pdf/2603.15226 and was published on March 17, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06989e69-8723-476c-ae91-cceebeff8557",
  "isSidechain": false,
  "promptId": "4974de4e-b7e6-441b-8009-479d1eed0b35",
  "type": "user",
  "uuid": "078c161d-a7bd-4500-8da4-f696204ab047",
  "toolUseResult": {
    "query": "\"SCAN\" sparse circuit anchor lifelong knowledge editing Qwen Llama 2026 arXiv 2603.15226",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L19GfLQ4yY4Vqc6uyFHkS8",
        "content": [
          {
            "title": "SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing",
            "url": "https://arxiv.org/pdf/2603.15226"
          },
          {
            "title": "Representation Interventions Enable Lifelong Unstructured Knowledge Control",
            "url": "https://arxiv.org/pdf/2511.20892"
          },
          {
            "title": "Lifelong Knowledge Editing requires Better Regularization",
            "url": "https://arxiv.org/pdf/2502.01636"
          },
          {
            "title": "Beyond Hard Writes and Rigid Preservation: Soft Recursive Least-Squares for Lifelong LLM Editing",
            "url": "https://arxiv.org/pdf/2601.15686"
          },
          {
            "title": "MEMOIR: Lifelong Model Editing with Minimal Overwrite and Informed Retention for LLMs",
            "url": "https://arxiv.org/pdf/2506.07899"
          },
          {
            "title": "Lifelong Knowledge Editing for LLMs with Retrieval-Augmented Continuous   Prompt Learning",
            "url": "https://arxiv.org/pdf/2405.03279"
          }
        ]
      },
      "I found the paper! Here are the search results for your query:\n\n**SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing** is a paper by Yuhuan Liu, Haitian Zhong, Xinyuan Xia, Qiang Liu, Shu Wu, and Liang Wang that addresses catastrophic forgetting and collapse in Large Language Models during sequential knowledge editing.\n\nThe paper identifies that the problem stems from dense editing paradigms treating models as black boxes, and proposes SCAN—a sparse editing framework based on Sparse Circuit Anchored Neuron which transforms editing into mechanism-aware manipulation by constructing a knowledge circuit via Sparse Transcoders.\n\nExperiments on Gemma2, Qwen3, and Llama3.1 across CounterFact, ZsRE and WikiFactDiff demonstrate that SCAN achieves superior performance, maintaining model integrity on benchmarks like MMLU and GSM8K even after 3,000 sequential edits, whereas existing methods deteriorate progressively.\n\nThe paper is available on arXiv at: https://arxiv.org/pdf/2603.15226 and was published on March 17, 2026."
    ],
    "durationSeconds": 6.5160247579999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "06989e69-8723-476c-ae91-cceebeff8557",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-19T21:03:50.021Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to write my evaluation. Let me synthesize what I've found:

1. **Venue Mismatch (CRITICAL)**: This proposal is about cross-lingual knowledge editing in LLMs using SAEs. CoRL 2026 is about **robot learning** — manipulation, navigation, locomotion, RL for physical robots, sim-to-real transfer, etc. This paper has ZERO relevance to CoRL. The acceptance probability at CoRL is essentially 0% because it would be desk-rejected for being out of scope.

2. **If we set aside the venue issue and evaluate the idea quality for an NLP venue** (like EMNLP, ACL, or NAACL):


The core contribution—using SAE features to decompose edit vectors and classify them as language-specific or language-agnostic before applying adaptive soft projection—does fill a genuine gap. Prior work hasn't directly combined SAE feature decomposition with cross-lingual knowledge editing, though related approaches exist in language identity removal and knowledge erasure. The novelty is solid but somewhat incremental, building on established techniques rather than introducing fundamentally new concepts.

The problem itself is well-motivated—current methods struggle with cross-lingual portability—but there's an underlying question about whether polysemantic entanglement is truly the bottleneck or if the real issue lies deeper in how knowledge editing fundamentally works. The proposal acknowledges this risk without fully resolving it.

Simpler alternatives exist: applying standard editing followed by post-hoc language steering, or removing language identity from the representation space before editing. The core claim that language and fact are entangled at the feature level—making the adaptive mechanism necessary—remains untested. The bigger concern is that the approach is heavily engineering-focused, layering multiple existing techniques together, and the central hypothesis about what causes portability failure hasn't been validated.

There's also a critical venue mismatch: CoRL explicitly requires robotics relevance and would desk-reject a pure NLP/interpretability paper. This belongs at ACL, EMNLP, NAACL, or COLM instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "078c161d-a7bd-4500-8da4-f696204ab047",
  "isSidechain": false,
  "requestId": "req_011CbCc29XbX5qfjWtRwnU1h",
  "type": "assistant",
  "uuid": "7c4954a3-9b92-4a7d-8c6c-6a5d96bd8d25",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WW8Sj22nufs51XpCWjYPkY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 30795,
      "output_tokens": 4328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1375,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4328,
          "cache_read_input_tokens": 30795,
          "cache_creation_input_tokens": 1375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1375
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

_source line 42 · 2026-05-19T21:05:00.431Z_

Now I have sufficient information to complete my evaluation. Let me compile my findings.

---

```
【阶段】: Triage

【领域调研】:
- LU-LAFNs (COLING 2025, arXiv:2406.16416): 最直接的 prior work。通过语言无关事实神经元实现多语言知识编辑，在 Bi-ZsRE 上 avg 77.87，但所有方法 portability EM < 10。本 proposal 试图用 SAE features 替代其 neuron-level 方法。
- FeatureEdit / The Knowledge Microscope (ACL 2025, arXiv:2502.12483): 首个 SAE feature-based 模型编辑方法，但仅用于英语 privacy knowledge erasure（非事实编辑、非跨语言）。reliability ~0.80 vs neurons ~0.65。
- LangSAE (arXiv:2601.04768): SAE 去除语言身份信息用于多语言检索，+21.9% nDCG@20。但应用场景是 retrieval，非 knowledge editing。
- Chou et al. (arXiv:2507.13410): 单个 SAE feature 修改即可实现 90% 语言控制成功率（Gemma-2B/9B），证明 SAE-based 语言操控可行。
- SCAN (arXiv:2603.15226, Mar 2026): Sparse Transcoders 用于 lifelong editing（Qwen3/Llama3.1），解决连续编辑稳定性问题，但不涉及跨语言。
- Peng et al. (arXiv:2506.23845): 论证 SAE 更适合发现未知概念而非操控已知概念。
- Arad et al. (EMNLP 2025, arXiv:2505.20063): 对 Peng et al. 的反驳——output-score filtering 使 SAE steering 提升 2-3×。
- Leask et al. (ICLR 2025, arXiv:2502.04878): SAE features 非原子/规范单元，larger SAEs decompose into sub-components。
- Mondal et al. (NAACL 2025, arXiv:2503.17456): 独立证据表明 neuron-level 语言干预不足以实现跨语言迁移。
- SAE-LAPE/LangFIR (arXiv:2604.03532): 使用激活概率对比发现稀疏语言特定特征。
- CLM-Bench (arXiv:2601.17397): 中英编辑向量几乎正交的几何证据。
- Merging Methods for MKE (arXiv:2605.13919, May 2026): 向量合并用于12语言编辑，但无表示级分解。

- 调研总结: 跨语言知识编辑是 2025-2026 活跃方向，neuron-level 方法（LU-LAFNs）已达瓶颈，SAE 在语言特征识别（LangSAE/SAE-LAPE）和知识擦除（FeatureEdit）上已有成果，但尚无工作将 SAE feature decomposition 直接用于跨语言知识编辑。该 proposal 处于一个真实但较为"显而易见的下一步"的位置。

【致命问题：会议选择错配】:
⚠️ **CoRL (Conference on Robot Learning) 2026 的主题范围包括：机器人感知、操控、导航、运动、强化学习、模仿学习、sim-to-real transfer 等。** 本 proposal 是纯 NLP/可解释性方向（跨语言知识编辑 + SAE），与 CoRL 的 scope 完全不匹配。CoRL 明确要求 "submissions should focus on a core robotics problem and demonstrate the relevance of proposed models to robotics." 该论文会在 desk review 阶段被拒稿。

合适的投稿目标应为：ACL 2026, EMNLP 2026, NAACL 2026, 或 COLM 2026。

【Trivial Alternative 检验】:
存在至少两个更简单的替代方案：
1. **Post-hoc language steering**: 先用标准 ROME/MEMIT 编辑，再用 Chou et al. 的单 feature 语言控制方法在推理时强制目标语言输出。这完全绕开了"编辑向量中分离语言成分"的复杂性。
2. **LangSAE + Standard Editing**: 先用 LangSAE 的方法去除表示空间中的语言身份信息（已被验证有效），再在去语言化空间中做标准编辑。

本 proposal 的增量价值取决于一个未经验证的核心假设：portability 失败是因为 polysemantic entanglement 而非更根本性的限制。如果 portability 失败是因为编辑只改变了表面关联而非深层关系推理能力（LU-LAFNs 作者自己倾向此解释），则无论分解粒度多细，都无法解决问题。adaptive λ-projection 相对于简单方案的真实增益可能很小。

【前提假设检验】:
核心逻辑链中存在以下未验证假设：
1. **"Portability 失败主要归因于 polysemantic entanglement"** —— 这是全文最关键的假设，但 LU-LAFNs 作者自己将 portability 失败归因于"the difficulty of measuring reasoning without a reasoning process"，暗示这可能是编辑范式的根本局限（编辑改变的是表面事实关联，无法影响多跳推理），而非粒度问题。
2. **"SAE features 的更细粒度分解能改善 relational structure preservation"** —— FeatureEdit 在 privacy erasure 上的优势不一定 transfer 到 factual editing + cross-lingual propagation。erasure（让模型忘记）和 propagation（让模型在其他语言推理）是本质不同的任务。
3. **"FCE metric 能有效识别 fact-entangled language features"** —— r_pb 作为 proxy 的质量未经验证；如果 factual information 分布式地编码在大量 features 中（而非集中在少数高 FCE features），则 top-2K 策略可能遗漏关键信息。

【3 维度打分】:
  1. Novelty: 中 — "SAE feature decomposition 用于跨语言知识编辑"这个组合确实是 novel 的（没有 prior work 做过），但本质上是将已有组件（LangSAE 的语言特征识别 + FeatureEdit 的 feature-level 编辑 + LU-LAFNs 的跨语言编辑框架）拼接在一起，并加了一个 adaptive λ 技术贡献。对于熟悉 SAE + knowledge editing 两个领域的人来说，这是一个"显而易见的下一步"。技术层面的 novelty（FCE + adaptive soft projection）是有意义的，但不是 paradigm-shifting。
  2. Significance: 中 — 问题本身（跨语言 portability 瓶颈）是重要且被广泛认可的。但如果核心假设错误（portability 失败不是粒度问题），这个方向就走不通。即使假设正确且实验 positive，审稿人可能会说 "SAE features are finer-grained than neurons, so they naturally work better — I would have guessed this"。另外，该方向的 downstream impact 有限：知识编辑本身在 LLM 快速迭代的时代实用性存疑。
  3. Related Work: 强 — Proposal 对相关工作的覆盖非常全面且诚实。对 adversarial work（Peng et al., Leask et al.）的主动引用和 engagement 是加分项。对 FeatureEdit 局限性的明确声明（privacy erasure ≠ factual editing）体现了学术诚信。差异化定位清晰。

【概率估计】: 
- 对 CoRL 2026: 0-2%（desk reject，完全不在 scope 内）
- 对 NLP 主会（ACL/EMNLP/NAACL 主会）: 20-30%，中位 25%

【估计理由】: 
对 CoRL: 论文主题与会议 scope 零重叠，会被 desk reject。
对 NLP 主会（假设投到正确 venue）: Related Work 维度强，但 Novelty 和 Significance 均为"中"，限制了上界。核心贡献是一个"显而易见的组合"加上有意义但非突破性的技术细节（FCE + adaptive λ）。即使实验 positive，审稿人最可能的反应是 "natural next step, solid execution, but not surprising"——这通常对应 borderline accept/reject。上界被 Significance 限制：核心假设可能错误，且即使正确也不够 surprising。

【主要风险】:
1. **会议选择致命错误**: CoRL 与本文 scope 完全不匹配，投稿 = 浪费一轮时间。必须改投 NLP venue。
2. **核心假设可能错误**: Portability 失败可能源于编辑范式的根本局限（无法影响多跳推理），而非粒度不够。如果如此，无论 SAE features 多好都不会改善 portability，整个 project 的核心 claim 就被 falsify 了。Proposal 虽然设计了 fallback（"negative result 也有价值"），但对于 CoRL/顶会来说 negative result paper 的接收标准更高。
```

---

**总结**: 这是一个形式上非常完善、related work 覆盖极好的 proposal，但有两个核心问题：

1. **投稿 CoRL 是致命的 venue 错配**——这是一篇纯 NLP/interpretability 论文，CoRL 只接收机器人学习相关工作，会被 desk reject。建议改投 ACL/EMNLP/NAACL 2026。

2. **Idea 内核是"显而易见的下一步"**——将 SAE features 替代 neurons 用于跨语言编辑，对于同时了解 SAE interpretability 和 multilingual knowledge editing 两个领域的人来说，这个 idea 的 surprise factor 不高。技术层面的 adaptive λ-projection 有贡献，但不足以将论文提升到 "surprising" 档次。

Sources:
- [LU-LAFNs (COLING 2025)](https://aclanthology.org/2025.coling-main.385/)
- [FeatureEdit / The Knowledge Microscope (arXiv:2502.12483)](https://arxiv.org/abs/2502.12483)
- [CLM-Bench (arXiv:2601.17397)](https://arxiv.org/pdf/2601.17397)
- [LangSAE (arXiv:2601.04768)](https://arxiv.org/pdf/2601.04768)
- [Chou et al. (arXiv:2507.13410)](https://arxiv.org/abs/2507.13410)
- [Peng et al. (arXiv:2506.23845)](https://arxiv.org/abs/2506.23845)
- [Arad et al. (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.519/)
- [SCAN (arXiv:2603.15226)](https://arxiv.org/pdf/2603.15226)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 About](https://www.corl.org/about-corl)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c4954a3-9b92-4a7d-8c6c-6a5d96bd8d25",
  "isSidechain": false,
  "requestId": "req_011CbCc29XbX5qfjWtRwnU1h",
  "type": "assistant",
  "uuid": "98e2fe5b-1f1e-4faa-a2bc-ea430e529dc6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WW8Sj22nufs51XpCWjYPkY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 30795,
      "output_tokens": 4328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1375,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4328,
          "cache_read_input_tokens": 30795,
          "cache_creation_input_tokens": 1375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1375
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation  ## Description Current c…",
  "leafUuid": "98e2fe5b-1f1e-4faa-a2bc-ea430e529dc6",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE feature decomposition for cross-lingual knowledge editing",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation  ## Description Current c…",
  "leafUuid": "98e2fe5b-1f1e-4faa-a2bc-ea430e529dc6",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE feature decomposition for cross-lingual knowledge editing",
  "sessionId": "ce70cc30-ca05-41af-b67a-765df91c77b1"
}
```

---
