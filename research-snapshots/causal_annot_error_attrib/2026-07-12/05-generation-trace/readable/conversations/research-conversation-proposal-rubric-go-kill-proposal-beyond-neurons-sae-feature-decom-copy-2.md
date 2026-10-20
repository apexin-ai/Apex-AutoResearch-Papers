# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Beyond Neurons: SAE Feature Decom

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/eb252af3-dc52-43cd-8394-fe1b586a4d8f.jsonl`
- **Structured JSON:** [`b6fcccbcf52611beac59.json`](../../sessions/b6/b6fcccbcf52611beac59.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:48:53.166Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:48:53.166Z",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation\n\n## Description\nCurrent cross-lingual knowledge editing faces a universal portability bottleneck: not just LU-LAFNs (COLING 2025) but ALL current methods achieve near-zero portability EM (< 10) on Bi-ZsRE, with the LU-LAFNs authors themselves noting 'all methods underperform on this metric without significant difference.' We hypothesize that this bottleneck has a specific causal mechanism: polysemantic neurons entangle factual relational structure with language identity, so any neuron-level editing that removes language components inevitably corrupts relational knowledge needed for portability. This hypothesis is independently supported by Mondal et al. (NAACL 2025 InsightsNLP), who showed that neuron-level language-specific interventions are insufficient for cross-lingual transfer even outside the editing setting.\n\nWe propose SAE-Projected Editing: using pre-trained Qwen-Scope SAEs (64K features on Qwen3-8B) and Llama Scope SAEs (128K features on Llama-3.1-8B) to decompose edit vectors into finer-grained sparse features, classify each as language-specific or language-agnostic via cross-lingual activation-probability contrasts, then apply adaptive soft projection that suppresses language-specific components proportionally to their Factual Causal Effect (FCE) — a per-feature ablation-based metric measuring how much factual recall degrades when the feature is removed. Unlike binary feature zeroing — which Farrell et al. (2024) showed is ineffective — our adaptive λ-projection preserves factual content encoded in partially-entangled features while removing pure language-identity signal.\n\n**Engagement with SAE intervention skepticism:** Peng et al. (arXiv:2506.23845) argue SAEs are better for discovery than intervention; however, Arad et al. (EMNLP 2025) directly rebut this by showing that output-score-based feature selection yields 2–3× improvement in SAE steering, matching supervised methods. The critique applies to naive feature selection, not SAE interventions as a paradigm. We incorporate output-score filtering into our pipeline. Chou et al. (arXiv:2507.13410) provide further feasibility evidence: modifying a single SAE feature achieves up to 90% language steering success on Gemma-2B/9B. Leask et al. (ICLR 2025) show SAE features are not atomic canonical units — larger latents decompose into sub-components. We accommodate this by: (a) treating features as a continuous weighted basis rather than binary switches, (b) using adaptive λ coefficients that handle partial feature overlap, and (c) ablating across SAE widths (16K/64K/128K) to identify task-appropriate granularity per Leask et al.'s recommendation.\n\n**FeatureEdit context note:** The +23% reliability and 2.8× generalization gains from FeatureEdit (ACL 2025) are for knowledge erasure on the PrivacyParaRel privacy dataset using Gemma-2 models, not factual knowledge editing or cross-lingual propagation. We cite these as evidence that features outperform neurons as representation-level intervention units, but do not assume these specific gains transfer to the editing setting.\n\n**FCE metric protocol:** For each of ~64K SAE features, we first compute point-biserial correlation r_pb between feature activation magnitude and binary factual recall success across ≥5,000 multilingual facts (computational cost: ~4 GPU-hours for forward passes). The top ~2K features by |r_pb| undergo full causal ablation: each feature is individually zeroed, and the change in factual recall probability is measured (FCE). This two-stage approach reduces the 64K × 5K evaluation matrix to a tractable 2K × 5K, requiring ~40 GPU-hours. Bootstrap confidence intervals (1000 resamples) provide uncertainty estimates for FCE values. As a validation check, we compute Spearman rank correlation between r_pb and FCE on the 2K features to verify the proxy quality.\n\nKey contributions: (1) First application of SAE feature decomposition to cross-lingual knowledge editing, providing ~5-10× finer granularity than neuron-level LAFN identification; (2) Adaptive soft projection mechanism that explicitly accounts for factual-language feature entanglement via a concrete, causal FCE metric with a two-stage efficient computation protocol; (3) Principled engagement with SAE intervention skepticism (Peng et al., Leask et al.) through output-score filtering, continuous-basis treatment, and multi-width ablation; (4) Testable portability hypothesis: if SAE features do NOT improve portability EM over neuron-level approaches (ablation A3), this falsifies the polysemanticity-entanglement explanation and has standalone diagnostic value; (5) Reconstruction fidelity validation protocol establishing whether SAE round-trip preserves edit vector quality across dictionary sizes.\n\nWe evaluate on CLM-Bench (zh-en), Bi-ZsRE, and MzsRE across 12 languages, targeting improvements over LU-LAFNs (77.87 Bi-ZsRE avg on bloomz-7b1-mt; MzsRE results reported as per-language heatmaps rather than a single average) particularly on portability metrics. Primary baselines: LU-LAFNs, FeatureEdit (adapted cross-lingual), MEMIT, AlphaEdit, M-MEMIT, X-KDE, LangEdit.\n\n**Risk mitigation:** The core risk is that the portability bottleneck is NOT caused by polysemantic entanglement but by a more fundamental limitation (e.g., the portability metric itself measuring reasoning ability that editing cannot improve). We address this through: (a) explicit FCE measurement before editing to quantify the entanglement ceiling, (b) adaptive λ-projection that preserves high-FCE features, (c) reconstruction fidelity go/no-go gate, (d) ablation A3 as a direct falsification test, and (e) relational follow-up evaluation (A2) that provides a complementary portability measure independent of the Bi-ZsRE metric. If SAE features fail to improve portability, the negative result still contributes a rigorous decomposition analysis of what fraction of factual information resides in language-specific vs. language-agnostic features — valuable for the multilingual interpretability community. Fallback: hybrid approach combining SAE-projected editing for low-entanglement facts with LU-LAFNs for high-entanglement cases.\n\n## Core Problem\nCross-lingual knowledge editing methods face two linked failures: (1) raw edit vectors reside in nearly orthogonal, language-specific subspaces (CLM-Bench), and (2) neuron-level approaches like LU-LAFNs that identify language-agnostic neurons achieve high monolingual reliability but suffer catastrophically low portability (26.43% F1, EM < 5) — a failure shared by ALL current methods (all EM < 10 on Bi-ZsRE portability), suggesting a fundamental representation-level bottleneck. We hypothesize that this bottleneck stems from polysemantic neurons entangling factual relational structure with language identity: edits that operate at neuron granularity cannot cleanly separate these components, corrupting relational knowledge during cross-lingual transfer. Can sparse autoencoder feature decomposition — which yields finer-grained, more monosemantic units — provide a cleaner separation that better preserves relational structure, and is this hypothesis even testable given recent challenges to SAE feature canonicality (Leask et al., ICLR 2025)?\n\n## Opportunity\nCLM-Bench (arXiv:2601.17397, Jan 2026) provided geometric evidence that Chinese and English edit vectors are nearly orthogonal, explaining why ROME/MEMIT fail cross-lingually (~20% reliability). LU-LAFNs (COLING 2025) achieved 77.87 avg on Bi-ZsRE by targeting language-agnostic neurons, but its neuron-level approach identifies 67.9% of neurons as LAFNs — an extremely coarse decomposition reflecting neuron polysemanticity — and ALL methods achieve near-zero portability EM (< 10 across the board), which the authors attribute to the difficulty of measuring reasoning without a reasoning process. Crucially, Mondal et al. (NAACL 2025 InsightsNLP) independently showed that neuron-level language-specific interventions are insufficient for cross-lingual transfer on XNLI/XQuAD, reinforcing the case that neuron-level decomposition is fundamentally too coarse.\n\nMeanwhile, FeatureEdit (ACL 2025) demonstrated that SAE features outperform neurons for knowledge erasure on PrivacyParaRel (~0.80 vs ~0.65 reliability, ~0.70 vs ~0.25 generalization on Gemma-2 2B/9B) — though notably this was for privacy-knowledge erasure, not factual editing or cross-lingual propagation, so these gains may not directly transfer. LangSAE (arXiv:2601.04768) proved SAE-based language identity removal improves cross-lingual retrieval by +21.9% nDCG@20. Chou et al. (arXiv:2507.13410) achieved up to 90% language steering success by modifying a single SAE feature on Gemma-2B/9B, demonstrating that SAE-based language manipulation is feasible and precise.\n\nHowever, recent work challenges SAE interventions: Peng et al. (arXiv:2506.23845) argue SAEs are better for concept discovery than acting on known concepts, finding SAE-based steering underperforms prompting/fine-tuning. Critically, Arad et al. (EMNLP 2025) rebut this: proper feature selection via output-score filtering yields 2–3× improvement in SAE steering, matching supervised methods — the issue was feature selection, not SAE interventions per se. Leask et al. (ICLR 2025) show SAE features aren't canonical atomic units — larger latents decompose into combinations — but recommend pragmatic choice of dictionary size suited to task, and our adaptive soft projection naturally accommodates non-atomicity by treating features as a continuous basis rather than binary switches.\n\nThe missing link: no work has combined SAE feature-level decomposition with cross-lingual knowledge editing. SAE features offer ~64K monosemantic units (vs. ~14K polysemantic neurons), enabling more precisely targeted language-component manipulation that may better preserve relational/factual structure — a hypothesis we propose to test directly.\n\n## Related Work / Landscape\nCross-lingual knowledge editing is a recognized open problem: the survey (arXiv:2505.14393) identifies language anisotropy and edit scalability as key challenges. The field is structured in three tiers:\n\n**Tier 1 — Direct multilingual editing baselines:** MEMIT/M-MEMIT apply locate-then-edit across languages (74.86 avg on Bi-ZsRE but ~20% cross-lingual reliability). AlphaEdit (ICLR 2025) uses null-space constraints. Merging Methods for MKE (arXiv:2605.13919, May 2026) explores vector merging with shared covariance for 12-language editing but without representation-level decomposition.\n\n**Tier 2 — Neuron/representation-level multilingual editing:** LU-LAFNs (COLING 2025, arXiv:2406.16416) is the closest prior work — identifies language-agnostic factual neurons via activation frequency intersection across languages, achieving 77.87 avg on Bi-ZsRE (bloomz-7b1-mt). However, it identifies 67.9% of neurons as LAFNs (extremely coarse), and ALL methods achieve near-zero portability (EM < 10, F1 ~26-36%), which the authors acknowledge as a universal challenge rather than a method-specific failure. Mondal et al. (NAACL 2025 InsightsNLP, arXiv:2503.17456) provide independent evidence that neuron-level language-specific interventions are insufficient for cross-lingual transfer. MEMLA (arXiv:2406.11566) uses neuron masking with LoRA but doesn't leverage monosemantic features. X-KDE (ACL 2025 Findings, arXiv:2502.14645) uses instruction tuning + preference optimization (+8.19% avg improvement). LangEdit (ACL 2025 Findings, arXiv:2506.10800) applies null-space projection for multilingual sequential editing across 6 languages.\n\n**Tier 3 — SAE-based editing and language feature work (our building blocks):** FeatureEdit from 'The Knowledge Microscope' (ACL 2025, arXiv:2502.12483) is the first SAE-feature-based model editing method — uses Gemma Scope JumpReLU SAEs to identify knowledge features and zero out specific weight positions. On the PrivacyParaRel knowledge-erasure benchmark (not factual editing), features achieve ~0.80 reliability (vs. ~0.65 for neurons) and ~0.70 generalization (vs. ~0.25), demonstrating features' advantage for representation-level interventions. However, it is monolingual English-only, targets knowledge erasure rather than cross-lingual propagation, and these gains may not directly transfer to the editing setting. SSPU (EMNLP 2025, arXiv:2505.24428) shows SAE-guided subspace projection via QR decomposition can unlearn knowledge while preserving non-target capabilities. LangSAE (arXiv:2601.04768) removes language identity from embeddings using SAE feature suppression (+21.9% nDCG@20). SAE-LAPE/LangFIR (arXiv:2604.03532) discover sparse language-specific features using activation probability contrasts. SASFT (ICLR 2026) shows SAE-guided fine-tuning preserves targeted knowledge. SpARE (NAACL 2025, arXiv:2410.15999) uses SAE-based representation engineering for knowledge selection steering but not cross-lingually. SCAN (arXiv:2603.15226, Mar 2026) uses sparse transcoders for lifelong editing on Qwen3/Llama3.1 but addresses sequential stability, not cross-lingual transfer. Farrell et al. (arXiv:2410.19278) found that zero ablation of SAE features is ineffective for knowledge unlearning — negative scaling is necessary. Chou et al. (arXiv:2507.13410) achieved up to 90% language steering success by modifying single SAE features on Gemma-2B/9B, providing direct feasibility evidence for SAE-based language manipulation.\n\n**Tier 4 — SAE intervention skepticism and counter-evidence (critical context):** Peng et al. (arXiv:2506.23845) argue SAEs are better for discovering unknown concepts than acting on known ones, finding SAE-based steering underperforms prompting/fine-tuning. However, Arad et al. (EMNLP 2025, arXiv:2505.20063) directly rebut this: by distinguishing 'input features' (capture input patterns) from 'output features' (causally affect model behavior) and filtering by output scores, SAE steering achieves 2–3× improvement, matching supervised methods. The issue was naive feature selection, not SAE interventions as a paradigm. Zhao et al. (arXiv:2505.15038) further show denoising concept vectors via SAE improves steering 4–16%. SAE-SSV (EMNLP 2025, arXiv:2505.16188) achieves high steering success rates using supervised feature selection in sparse spaces. Leask et al. (ICLR 2025, arXiv:2502.04878) demonstrate SAE features are neither atomic nor canonical — meta-SAEs decompose latents into sub-components (e.g., 'Einstein' → 'scientist' + 'Germany' + 'famous person'), and smaller SAEs miss information captured by larger ones. They recommend pragmatic dictionary size selection rather than assuming canonicality. Our approach accommodates this by treating SAE features as a practical continuous basis with adaptive coefficients, not as binary canonical units.\n\n**The gap:** No work combines SAE feature decomposition with cross-lingual knowledge editing. Specifically, no one has (a) used monosemantic SAE features instead of polysemantic neurons to decompose cross-lingual edit vectors, (b) tested whether finer-grained decomposition causally improves portability by preserving relational structure, or (c) engaged with the feature-selection insights from Arad et al. to ensure intervention-effective features are targeted.\n\n## Approach\n**Phase 1: Feature Classification with Output-Score Filtering (Weeks 1-2).** Leverage pre-trained SAEs — Qwen-Scope (64K features, 16× expansion) on Qwen3-8B and Llama Scope (128K features, 32× expansion) on Llama-3.1-8B — to decompose residual-stream activations at editing-critical layers (layers 12-25 for Qwen3-8B based on LU-LAFNs' LAFN distribution peaks). Classify each feature as language-specific, language-agnostic, or factual using activation-probability contrasts across Chinese, English, and 4+ additional languages (following SAE-LAPE/LangFIR methodology). Critically, following Arad et al.'s (EMNLP 2025) insight that input-pattern features and output-causal features rarely co-occur, compute output scores for all features to ensure we target features that causally affect model behavior, not merely correlational activations — this addresses the core criticism of Peng et al. For each language-specific feature f_i, compute its Factual Causal Effect (FCE): ablate f_i and measure the change in correct factual recall probability across a multilingual fact corpus of ≥5,000 facts (drawn from Bi-ZsRE + MzsRE test sets, held out from editing evaluation). FCE(f_i) = |P(correct | f_i active) - P(correct | f_i ablated)|. This produces a per-feature entanglement map. FCE is preferred over mutual information because: (a) it is causal rather than correlational, (b) it avoids the curse-of-dimensionality problems that plague MI estimation with 64K+ features (KSG estimators break down beyond ~10 dimensions), and (c) it is directly interpretable as the factual cost of removing a feature. As a computationally efficient proxy during initial screening, we also compute point-biserial correlation r_pb between feature activation magnitude and binary factual recall success, filtering to the top ~2K candidate features for full FCE ablation (reducing 64K × 5K evaluations to ~2K × 5K).\n\n**Phase 2: SAE-Projected Editing with Adaptive Soft Projection (Weeks 3-5).** For a given ROME/MEMIT edit vector e, decompose it into the SAE feature basis: e ≈ Σ_j α_j d_j (where d_j are SAE decoder directions and α_j are coefficients from the encoder). Following Farrell et al.'s finding that binary zeroing is ineffective and Leask et al.'s evidence that features are not atomic canonical units, we apply adaptive soft projection that treats features as a continuous basis: e_proj = e - Σ_{i ∈ L_spec} λ_i · α_i · d_i, where λ_i ∈ [0, 1] is inversely proportional to FCE(f_i) — features with high factual causal effect are preserved more, pure language-identity features (low FCE, high language specificity) are fully suppressed. This formulation naturally handles Leask et al.'s non-atomicity concern: since features are weighted continuously rather than treated as binary switches, partial overlap between sub-features is accommodated through the λ gradient. The projected vector e_proj is then applied via the standard locate-then-edit pipeline.\n\n**Phase 3: Reconstruction Fidelity Validation (Weeks 3-4, parallel).** Before full-scale editing, validate that SAE round-trip reconstruction preserves edit vector fidelity. Measure: (a) cosine similarity between original and reconstructed edit vectors, (b) monolingual edit success rate with SAE-reconstructed vectors (no language feature removal) vs. original ROME/MEMIT — this isolates reconstruction error from projection effects. If reconstruction degrades edit quality by >5%, investigate top-k sparsity adjustments or layer-specific SAE selection. Following Leask et al.'s recommendation, test multiple SAE widths (16K, 64K, 128K where available) to identify task-appropriate granularity rather than assuming larger is better. Establish a reconstruction quality threshold as a go/no-go gate.\n\n**Phase 4: Evaluation and Ablation (Weeks 5-8).** Evaluate on CLM-Bench (1,010 zh-en pairs), Bi-ZsRE, and MzsRE (12 languages) using Qwen3-8B and Llama-3.1-8B. Primary baselines: LU-LAFNs (77.87/Bi-ZsRE on bloomz-7b1-mt — the SOTA to beat), FeatureEdit (adapted to cross-lingual setting), MEMIT, AlphaEdit, M-MEMIT, X-KDE, LangEdit. Secondary baselines: SCAN, MEMLA. Key ablations: (A1) Full zeroing vs. soft projection — measuring factual content loss, directly testing Farrell et al.'s finding in the cross-lingual setting. (A2) Relational structure preservation: for edited facts, measure whether the model correctly answers relational follow-up questions (e.g., after editing 'capital of X', test 'X is in which continent?') — this directly tests the portability hypothesis. (A3) Feature granularity: SAE features (64K/128K) vs. neuron-level LAFNs (~10K) vs. random subspace projection — if SAE features do not improve portability over neurons, this falsifies our core hypothesis. (A4) λ scheduling: fixed λ vs. FCE-adaptive λ vs. oracle λ (per-fact optimal). (A5) Layer selection: which layers' SAEs are most critical for cross-lingual transfer. (A6) SAE width: 16K vs. 64K vs. 128K features, testing Leask et al.'s prediction that task-appropriate granularity matters more than raw dictionary size. (A7) Output-score filtering (per Arad et al.): restrict projection to high-output-score features vs. all language-classified features.\n\n## Inspiration\nLU-LAFNs' universal portability failure (all methods EM < 10) revealing a fundamental representation-level bottleneck + Mondal et al.'s independent evidence that neuron-level language interventions are insufficient + FeatureEdit's demonstration that SAE features outperform neurons for knowledge erasure + LangSAE proving language features can be surgically suppressed + Chou et al.'s 90% language steering with single SAE features + CLM-Bench's geometric evidence of language-specific subspaces + SSPU's QR-decomposition subspace methodology + Arad et al.'s insight that output-score feature selection rescues SAE interventions + Farrell et al.'s finding that soft scaling outperforms zero ablation\n\n## Key References\n- LU-LAFNs: Multilingual Knowledge Editing with Language-Agnostic Factual Neurons (COLING 2025, arXiv:2406.16416) — PRIMARY BASELINE\n- FeatureEdit / The Knowledge Microscope: Features as Better Analytical Lenses than Neurons (ACL 2025, arXiv:2502.12483) — METHODOLOGICAL PREDECESSOR (knowledge erasure, not editing)\n- CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing (arXiv 2026, arXiv:2601.17397)\n- LangSAE Editing: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal (arXiv 2026, arXiv:2601.04768)\n- LangEdit: Mitigating Negative Interference in Multilingual Sequential Knowledge Editing through Null-Space Constraints (ACL 2025 Findings, arXiv:2506.10800)\n- SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing (arXiv 2026, arXiv:2603.15226)\n- SSPU: Model Unlearning via Sparse Autoencoder Subspace Guided Projections (EMNLP 2025, arXiv:2505.24428)\n- Applying Sparse Autoencoders to Unlearn Knowledge in Language Models (arXiv 2024, arXiv:2410.19278)\n- X-KDE: Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs (ACL 2025 Findings, arXiv:2502.14645)\n- MEMLA: Enhancing Multilingual Knowledge Editing with Neuron-Masked Low-Rank Adaptation (arXiv 2024, arXiv:2406.11566)\n- Editing Across Languages: A Survey of Multilingual Knowledge Editing (arXiv 2025, arXiv:2505.14393)\n- SAE-LAPE: Unveiling Language-Specific Features in Large Language Models via Sparse Autoencoders (ACL 2025, arXiv:2505.05111)\n- LinguaLens: Towards Interpreting Linguistic Mechanisms of Large Language Models via Sparse Auto-Encoder (EMNLP 2025)\n- SASFT: Sparse Autoencoder-guided Supervised Finetuning to Mitigate Unexpected Code-Switching in LLMs (ICLR 2026)\n- AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models (ICLR 2025)\n- SpARE: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering (NAACL 2025, arXiv:2410.15999)\n- LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering (arXiv 2026, arXiv:2604.03532)\n- Merging Methods for Multilingual Knowledge Editing for Large Language Models: An Empirical Odyssey (arXiv 2026, arXiv:2605.13919)\n- SALVE: Sparse Autoencoder-Latent Vector Editing for Mechanistic Control of Neural Networks (arXiv 2025, arXiv:2512.15938)\n- Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models (arXiv 2026, arXiv:2605.11887)\n- Llama Scope: Extracting Millions of Features from Llama-3.1-8B with Sparse Autoencoders (arXiv 2024, arXiv:2410.20526)\n- Language-Specific Neurons: The Key to Multilingual Capabilities in Large Language Models (ACL 2024, arXiv:2402.16438)\n- Peng et al.: Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts (arXiv 2025, arXiv:2506.23845) — ADVERSARIAL: argues SAEs underperform for interventions\n- Leask et al.: Sparse Autoencoders Do Not Find Canonical Units of Analysis (ICLR 2025, arXiv:2502.04878) — ADVERSARIAL: shows features are not atomic/canonical\n- Arad et al.: SAEs Are Good for Steering — If You Select the Right Features (EMNLP 2025, arXiv:2505.20063) — REBUTTAL to Peng et al.: output-score filtering yields 2-3× improvement\n- Mondal et al.: Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer (NAACL 2025 InsightsNLP, arXiv:2503.17456) — SUPPORTS motivation: neuron-level is insufficient\n- Chou et al.: Causal Language Control in Multilingual Transformers via Sparse Feature Steering (arXiv 2025, arXiv:2507.13410) — FEASIBILITY: 90% language steering with single SAE feature\n- Zhao et al.: Denoising Concept Vectors with Sparse Autoencoders for Improved Language Model Steering (arXiv 2025, arXiv:2505.15038) — SAE steering improves 4-16% with denoising\n- SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models (EMNLP 2025, arXiv:2505.16188)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '450-550 (SAE feature classification + FCE ablation analysis ~120h on 1×A100 — increased due to per-feature ablation; reconstruction fidelity validation across SAE widths ~40h; editing experiments across 2 models × 3 benchmarks × 8+ baselines ~250h; ablation studies A1-A7 ~120h; analysis ~40h)', 'timeline': '10-12 weeks', 'estimated_gpu_cost': '$1,125-$1,375 (A100 at ~$2.50/hr; major savings from pre-trained Qwen-Scope and Llama Scope SAEs)'}\n- **human_in_loop**: {'gpu_hours': '400-500', 'timeline': '7-9 weeks', 'claude_api_cost': '$150-$250 (code generation for SAE analysis pipeline, FCE computation, experiment orchestration)', 'estimated_gpu_cost': '$1,000-$1,250'}\n- **auto_research**: {'gpu_hours': '400-500', 'timeline': '5-7 weeks', 'claude_api_cost': '$400-$550 (end-to-end experiment management, hyperparameter sweeps for λ, paper drafting)', 'estimated_gpu_cost': '$1,000-$1,250', 'speed_bottleneck': 'FCE ablation requires sequential per-feature evaluation (mitigated by r_pb pre-screening to ~2K features); sequential editing experiments per model-benchmark pair; CLM-Bench evaluation involves Chinese cultural knowledge judgment requiring human spot-checking'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T18:48:53.177Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:48:53.177Z",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f"
}
```

---

## Round 1

50 recorded events

### User

_source line 3 · 2026-05-19T18:48:53.196Z_

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
  "promptId": "337860c3-19bc-47e7-8a4b-15fad24e9187",
  "type": "user",
  "uuid": "a31c5d64-c92e-4ef9-8715-fc48827f8a0b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:48:53.194Z_

```json
{
  "parentUuid": "a31c5d64-c92e-4ef9-8715-fc48827f8a0b",
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
  "uuid": "da075fda-f165-414f-8e3e-4294a5d5503d",
  "timestamp": "2026-05-19T18:48:53.194Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:48:53.194Z_

```json
{
  "parentUuid": "da075fda-f165-414f-8e3e-4294a5d5503d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "56f21b18-faaa-4439-86f9-688aae93a906",
  "timestamp": "2026-05-19T18:48:53.194Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
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
  "leafUuid": "56f21b18-faaa-4439-86f9-688aae93a906",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE features for cross-lingual knowledge editing",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:49:07.825Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate this proposal for CoRL 2026 submission. Let me first carefully read the proposal, then conduct web searches to understand the field landscape before making my assessment.

Wait - the user says CoRL 2026. CoRL is the Conference on Robot Learning. But this proposal is about cross-lingual knowledge editing in LLMs, which is an NLP/CL topic. This seems like a mismatch - this proposal would be more suited for ACL, EMNLP, NAACL, or COLING, not CoRL. Let me re-read...

Actually, looking at the system prompt again, it says "评估其投稿 CoRL 2026 主会的中稿潜力". 

There's definitely a venue mismatch here - CoRL focuses on robot learning while this work is purely about cross-lingual knowledge editing in language models using sparse autoencoders. The evaluation rubric itself references NLP/CL impact, which suggests there may be some confusion about the target conference. I should evaluate the proposal on its merits while noting this discrepancy.

Before scoring, I need to search for recent work in this space to understand the current landscape - specifically cross-lingual knowledge editing approaches, sparse autoencoder-based editing methods, the portability challenges in existing work, and the skepticism around SAE interventions in the literature.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56f21b18-faaa-4439-86f9-688aae93a906",
  "isSidechain": false,
  "requestId": "req_011CbCRmRdtPBNHEwANGTBdr",
  "type": "assistant",
  "uuid": "4d78c49f-b5f4-433c-9c8e-2d0dcaa57286",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKyoxo2ihHMpaa6H1jWSaP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8887,
      "cache_read_input_tokens": 13985,
      "output_tokens": 612,
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
          "output_tokens": 612,
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

_source line 9 · 2026-05-19T18:49:07.836Z_

I need to conduct thorough field research before evaluating this proposal. Let me first load the WebSearch tool and then perform multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d78c49f-b5f4-433c-9c8e-2d0dcaa57286",
  "isSidechain": false,
  "requestId": "req_011CbCRmRdtPBNHEwANGTBdr",
  "type": "assistant",
  "uuid": "27d9d2c2-103f-49ea-9f23-e7ffee67017b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKyoxo2ihHMpaa6H1jWSaP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8887,
      "cache_read_input_tokens": 13985,
      "output_tokens": 612,
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
          "output_tokens": 612,
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

_source line 10 · 2026-05-19T18:49:07.852Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ApE6KBACS5q4SDgxUn41hk`</summary>

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
  "parentUuid": "27d9d2c2-103f-49ea-9f23-e7ffee67017b",
  "isSidechain": false,
  "requestId": "req_011CbCRmRdtPBNHEwANGTBdr",
  "type": "assistant",
  "uuid": "bd12884b-19c1-46e0-95cd-ab40c8eb0772",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKyoxo2ihHMpaa6H1jWSaP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8887,
      "cache_read_input_tokens": 13985,
      "output_tokens": 612,
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
          "output_tokens": 612,
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

_source line 11 · 2026-05-19T18:49:07.859Z_

<details><summary>↩ Tool result · `toolu_01ApE6KBACS5q4SDgxUn41hk`</summary>

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
  "parentUuid": "bd12884b-19c1-46e0-95cd-ab40c8eb0772",
  "isSidechain": false,
  "promptId": "337860c3-19bc-47e7-8a4b-15fad24e9187",
  "type": "user",
  "uuid": "0f848fed-7de9-4d57-8ec6-47e8e8066f72",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "bd12884b-19c1-46e0-95cd-ab40c8eb0772",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T18:49:13.400Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me perform multiple targeted searches to understand the field landscape. I'll search for:
1. Cross-lingual knowledge editing recent work 2025-2026
2. SAE feature editing / FeatureEdit ACL 2025
3. LU-LAFNs cross-lingual portability bottleneck
4. SAE interventions skepticism and rebuttals
5. SAE language steering / Chou et al.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f848fed-7de9-4d57-8ec6-47e8e8066f72",
  "isSidechain": false,
  "requestId": "req_011CbCRnWYLqWmtqDpPtXYc6",
  "type": "assistant",
  "uuid": "c8995d1c-2411-48e1-afb5-62a74538fac7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdiV8g232p7R4A6VfRqtNR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 22872,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1139,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 448,
          "cache_read_input_tokens": 22872,
          "cache_creation_input_tokens": 1139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1139
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

_source line 13 · 2026-05-19T18:49:13.402Z_

Let me now perform several targeted searches in parallel to understand the field landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8995d1c-2411-48e1-afb5-62a74538fac7",
  "isSidechain": false,
  "requestId": "req_011CbCRnWYLqWmtqDpPtXYc6",
  "type": "assistant",
  "uuid": "04990c0e-4781-4287-9c12-5d822406b5e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdiV8g232p7R4A6VfRqtNR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 22872,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1139,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 448,
          "cache_read_input_tokens": 22872,
          "cache_creation_input_tokens": 1139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1139
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

_source line 14 · 2026-05-19T18:49:13.845Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H5eDiiHBCHtt5qUVRXGnVv`</summary>

```json
{
  "query": "cross-lingual knowledge editing LLMs 2025 2026 survey portability bottleneck"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04990c0e-4781-4287-9c12-5d822406b5e7",
  "isSidechain": false,
  "requestId": "req_011CbCRnWYLqWmtqDpPtXYc6",
  "type": "assistant",
  "uuid": "0a194b66-e9a2-4a27-8be8-d1d0e7988841",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdiV8g232p7R4A6VfRqtNR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 22872,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1139,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 448,
          "cache_read_input_tokens": 22872,
          "cache_creation_input_tokens": 1139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1139
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

_source line 15 · 2026-05-19T18:49:14.852Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QRYs5SyvATxybAoMeLbfw9`</summary>

```json
{
  "query": "FeatureEdit SAE sparse autoencoder knowledge editing ACL 2025 arXiv:2502.12483"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a194b66-e9a2-4a27-8be8-d1d0e7988841",
  "isSidechain": false,
  "requestId": "req_011CbCRnWYLqWmtqDpPtXYc6",
  "type": "assistant",
  "uuid": "160d731b-247e-4594-bced-4fca44fc6956",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdiV8g232p7R4A6VfRqtNR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 22872,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1139,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 448,
          "cache_read_input_tokens": 22872,
          "cache_creation_input_tokens": 1139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1139
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

_source line 16 · 2026-05-19T18:49:15.327Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KiMpWNd5JnT5Z9SiaQTCeT`</summary>

```json
{
  "query": "LU-LAFNs language-agnostic factual neurons COLING 2025 cross-lingual portability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "160d731b-247e-4594-bced-4fca44fc6956",
  "isSidechain": false,
  "requestId": "req_011CbCRnWYLqWmtqDpPtXYc6",
  "type": "assistant",
  "uuid": "27f57f2b-0daa-4bb6-99ec-503c1b9b40f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdiV8g232p7R4A6VfRqtNR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 22872,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1139,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 448,
          "cache_read_input_tokens": 22872,
          "cache_creation_input_tokens": 1139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1139
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

_source line 17 · 2026-05-19T18:49:16.264Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015zMzwvJqisdfZ8NF5q2GmK`</summary>

```json
{
  "query": "sparse autoencoder intervention skepticism Peng et al 2025 Arad et al SAE steering feature selection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27f57f2b-0daa-4bb6-99ec-503c1b9b40f5",
  "isSidechain": false,
  "requestId": "req_011CbCRnWYLqWmtqDpPtXYc6",
  "type": "assistant",
  "uuid": "5f2509a3-6620-43ed-ac29-1c35fac1f6ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdiV8g232p7R4A6VfRqtNR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 22872,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1139,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 448,
          "cache_read_input_tokens": 22872,
          "cache_creation_input_tokens": 1139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1139
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

_source line 18 · 2026-05-19T18:49:16.748Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BT7o8XC29xN6WzHYzcm6QE`</summary>

```json
{
  "query": "Chou et al SAE language steering multilingual transformers sparse feature 2025 arXiv:2507.13410"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f2509a3-6620-43ed-ac29-1c35fac1f6ca",
  "isSidechain": false,
  "requestId": "req_011CbCRnWYLqWmtqDpPtXYc6",
  "type": "assistant",
  "uuid": "06b36fd6-395e-4c66-80a6-49d868b7cf8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdiV8g232p7R4A6VfRqtNR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 22872,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1139,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 448,
          "cache_read_input_tokens": 22872,
          "cache_creation_input_tokens": 1139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1139
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

_source line 19 · 2026-05-19T18:49:22.479Z_

<details><summary>↩ Tool result · `toolu_01H5eDiiHBCHtt5qUVRXGnVv`</summary>

```text
Web search results for query: "cross-lingual knowledge editing LLMs 2025 2026 survey portability bottleneck"

Links: [{"title":"Cross-Lingual Knowledge Editing in Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/384207128_Cross-Lingual_Knowledge_Editing_in_Large_Language_Models"},{"title":"Cross-Lingual Knowledge Editing in Large Language Models","url":"https://arxiv.org/html/2309.08952v2"},{"title":"InstructEdit: Instruction-Based Knowledge Editing for Large Language Models","url":"https://www.ijcai.org/proceedings/2024/0733.pdf"},{"title":"Cross-Lingual Knowledge Editing in Large Language Models","url":"https://arxiv.org/pdf/2309.08952"},{"title":"(PDF) Cross-Lingual Knowledge Editing in Large Language Models","url":"https://www.researchgate.net/publication/373953974_Cross-Lingual_Knowledge_Editing_in_Large_Language_Models"},{"title":"CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing","url":"https://arxiv.org/pdf/2601.17397"},{"title":"Editing Across Languages: A Survey of Multilingual Knowledge Editing","url":"https://arxiv.org/html/2505.14393"},{"title":"Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs","url":"https://arxiv.org/pdf/2502.14645"}]

I found several relevant sources on cross-lingual knowledge editing in LLMs. Here's what the research shows:

## Overview of Cross-Lingual Knowledge Editing

Recent surveys summarize key findings on method effectiveness and transfer patterns, identify challenges in cross-lingual propagation, and highlight open problems related to language anisotropy, evaluation coverage, and edit scalability.

## Core Challenges

A major bottleneck is the **limited cross-lingual transfer of edits**. Research indicates that it remains challenging for multi-lingual LLMs to generalize the edited knowledge to other languages. More specifically, language modeling gaps across different languages influence the efficiency of knowledge editing, and it is still hard for existing knowledge editing methods to transfer the edited knowledge from one language to another in a multi-lingual LLM.

## Portability Issues

The underlying mechanism of cross-lingual misalignment remains unexplained, and while previous work observes that editing one language often fails to transfer to another, the geometric relationship between language-specific representations has not been rigorously analyzed.

## Recent Methodological Approaches

Recent advancements include parameter editing methods, memory-based methods, fine-tuning methods, and hypernetwork-based methods, alongside benchmark datasets designed to evaluate multilingual knowledge editing effectiveness.

## Emerging Solutions

Recent work has proposed X-KDE as a state-of-the-art solution for cross-lingual knowledge editing, demonstrating significant improvements in performance while preserving original knowledge and enhancing the portability of updates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a194b66-e9a2-4a27-8be8-d1d0e7988841",
  "isSidechain": false,
  "promptId": "337860c3-19bc-47e7-8a4b-15fad24e9187",
  "type": "user",
  "uuid": "66c2bd61-0688-46aa-b798-dac07505b7cf",
  "toolUseResult": {
    "query": "cross-lingual knowledge editing LLMs 2025 2026 survey portability bottleneck",
    "results": [
      {
        "tool_use_id": "srvtoolu_015KSLoA19DFF2aAWUBaX9Qo",
        "content": [
          {
            "title": "Cross-Lingual Knowledge Editing in Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/384207128_Cross-Lingual_Knowledge_Editing_in_Large_Language_Models"
          },
          {
            "title": "Cross-Lingual Knowledge Editing in Large Language Models",
            "url": "https://arxiv.org/html/2309.08952v2"
          },
          {
            "title": "InstructEdit: Instruction-Based Knowledge Editing for Large Language Models",
            "url": "https://www.ijcai.org/proceedings/2024/0733.pdf"
          },
          {
            "title": "Cross-Lingual Knowledge Editing in Large Language Models",
            "url": "https://arxiv.org/pdf/2309.08952"
          },
          {
            "title": "(PDF) Cross-Lingual Knowledge Editing in Large Language Models",
            "url": "https://www.researchgate.net/publication/373953974_Cross-Lingual_Knowledge_Editing_in_Large_Language_Models"
          },
          {
            "title": "CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing",
            "url": "https://arxiv.org/pdf/2601.17397"
          },
          {
            "title": "Editing Across Languages: A Survey of Multilingual Knowledge Editing",
            "url": "https://arxiv.org/html/2505.14393"
          },
          {
            "title": "Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs",
            "url": "https://arxiv.org/pdf/2502.14645"
          }
        ]
      },
      "I found several relevant sources on cross-lingual knowledge editing in LLMs. Here's what the research shows:\n\n## Overview of Cross-Lingual Knowledge Editing\n\nRecent surveys summarize key findings on method effectiveness and transfer patterns, identify challenges in cross-lingual propagation, and highlight open problems related to language anisotropy, evaluation coverage, and edit scalability.\n\n## Core Challenges\n\nA major bottleneck is the **limited cross-lingual transfer of edits**. Research indicates that it remains challenging for multi-lingual LLMs to generalize the edited knowledge to other languages. More specifically, language modeling gaps across different languages influence the efficiency of knowledge editing, and it is still hard for existing knowledge editing methods to transfer the edited knowledge from one language to another in a multi-lingual LLM.\n\n## Portability Issues\n\nThe underlying mechanism of cross-lingual misalignment remains unexplained, and while previous work observes that editing one language often fails to transfer to another, the geometric relationship between language-specific representations has not been rigorously analyzed.\n\n## Recent Methodological Approaches\n\nRecent advancements include parameter editing methods, memory-based methods, fine-tuning methods, and hypernetwork-based methods, alongside benchmark datasets designed to evaluate multilingual knowledge editing effectiveness.\n\n## Emerging Solutions\n\nRecent work has proposed X-KDE as a state-of-the-art solution for cross-lingual knowledge editing, demonstrating significant improvements in performance while preserving original knowledge and enhancing the portability of updates."
    ],
    "durationSeconds": 8.629428201,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0a194b66-e9a2-4a27-8be8-d1d0e7988841",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T18:49:24.368Z_

<details><summary>↩ Tool result · `toolu_01BT7o8XC29xN6WzHYzcm6QE`</summary>

```text
Web search results for query: "Chou et al SAE language steering multilingual transformers sparse feature 2025 arXiv:2507.13410"

Links: [{"title":"[2507.13410] Causal Language Control in Multilingual Transformers via Sparse Feature Steering","url":"https://arxiv.org/abs/2507.13410"},{"title":"Causal Language Control in Multilingual Transformers via Sparse Feature Steering","url":"https://arxiv.org/html/2507.13410v1"},{"title":"Causal Language Control in Multilingual Transformers via Sparse Feature","url":"https://arxiv.org/pdf/2507.13410"},{"title":"Language steering in latent space to mitigate unintended code-switching","url":"https://arxiv.org/pdf/2510.13849"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326v1"},{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/html/2505.12584v2"},{"title":"LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering","url":"https://arxiv.org/pdf/2604.03532"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/pdf/2602.02326"}]

I found the paper you're looking for! Here's what the search revealed:

The paper is titled "Causal Language Control in Multilingual Transformers via Sparse Feature Steering" by Cheng-Ting Chou and 6 other authors.

**Overview:**
The paper addresses the challenge of deterministically controlling the target generation language of large multilingual language models, particularly in zero-shot settings where neither explicit language prompts nor fine-tuning are available.

**Key Approach:**
The work investigates whether sparse autoencoder (SAE) features can be leveraged to steer the generated language of LLMs during inference. Using pretrained SAEs on the residual streams of Gemma-2B and Gemma-9B, the authors identify features whose activations differ most significantly between English and four target languages: Chinese, Japanese, Spanish, and French.

**Results:**
By modifying just a single SAE feature at one transformer layer, they achieve controlled language shifts with up to 90% success, while preserving semantic fidelity according to LaBSE similarity. The analysis reveals that language steering is most effective in mid-to-late transformer layers and is amplified by specific attention heads disproportionately associated with language-sensitive SAE features.

The paper was uploaded to arXiv on July 17, 2025 (with a revision on October 15, 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06b36fd6-395e-4c66-80a6-49d868b7cf8c",
  "isSidechain": false,
  "promptId": "337860c3-19bc-47e7-8a4b-15fad24e9187",
  "type": "user",
  "uuid": "4d382487-3745-410b-b907-3692e341187d",
  "toolUseResult": {
    "query": "Chou et al SAE language steering multilingual transformers sparse feature 2025 arXiv:2507.13410",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MESVS3cnRugSNsMaJwbgPW",
        "content": [
          {
            "title": "[2507.13410] Causal Language Control in Multilingual Transformers via Sparse Feature Steering",
            "url": "https://arxiv.org/abs/2507.13410"
          },
          {
            "title": "Causal Language Control in Multilingual Transformers via Sparse Feature Steering",
            "url": "https://arxiv.org/html/2507.13410v1"
          },
          {
            "title": "Causal Language Control in Multilingual Transformers via Sparse Feature",
            "url": "https://arxiv.org/pdf/2507.13410"
          },
          {
            "title": "Language steering in latent space to mitigate unintended code-switching",
            "url": "https://arxiv.org/pdf/2510.13849"
          },
          {
            "title": "Language Steering for Multilingual In-Context Learning",
            "url": "https://arxiv.org/html/2602.02326v1"
          },
          {
            "title": "Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://arxiv.org/html/2505.12584v2"
          },
          {
            "title": "LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering",
            "url": "https://arxiv.org/pdf/2604.03532"
          },
          {
            "title": "Language Steering for Multilingual In-Context Learning",
            "url": "https://arxiv.org/pdf/2602.02326"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search revealed:\n\nThe paper is titled \"Causal Language Control in Multilingual Transformers via Sparse Feature Steering\" by Cheng-Ting Chou and 6 other authors.\n\n**Overview:**\nThe paper addresses the challenge of deterministically controlling the target generation language of large multilingual language models, particularly in zero-shot settings where neither explicit language prompts nor fine-tuning are available.\n\n**Key Approach:**\nThe work investigates whether sparse autoencoder (SAE) features can be leveraged to steer the generated language of LLMs during inference. Using pretrained SAEs on the residual streams of Gemma-2B and Gemma-9B, the authors identify features whose activations differ most significantly between English and four target languages: Chinese, Japanese, Spanish, and French.\n\n**Results:**\nBy modifying just a single SAE feature at one transformer layer, they achieve controlled language shifts with up to 90% success, while preserving semantic fidelity according to LaBSE similarity. The analysis reveals that language steering is most effective in mid-to-late transformer layers and is amplified by specific attention heads disproportionately associated with language-sensitive SAE features.\n\nThe paper was uploaded to arXiv on July 17, 2025 (with a revision on October 15, 2025)."
    ],
    "durationSeconds": 7.614380569999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "06b36fd6-395e-4c66-80a6-49d868b7cf8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T18:49:24.602Z_

<details><summary>↩ Tool result · `toolu_01KiMpWNd5JnT5Z9SiaQTCeT`</summary>

```text
Web search results for query: "LU-LAFNs language-agnostic factual neurons COLING 2025 cross-lingual portability"

Links: [{"title":"Multilingual Knowledge Editing with Language-Agnostic Factual Neurons - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.385/"},{"title":"Multilingual Knowledge Editing with Language-Agnostic Factual Neurons","url":"https://arxiv.org/pdf/2406.16416"},{"title":"Multilingual Knowledge Editing with Language-Agnostic Factual Neurons","url":"https://arxiv.org/html/2406.16416"},{"title":"[2406.16416] Multilingual Knowledge Editing with Language-Agnostic Factual Neurons","url":"https://arxiv.org/abs/2406.16416"},{"title":"Multilingual Knowledge Editing with Language-Agnostic ...","url":"https://aclanthology.org/2025.coling-main.385.pdf"},{"title":"Multilingual Knowledge Editing with Language-Agnostic Factual Neurons - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240616416Z/abstract"},{"title":"Language-Specific Neurons Do Not Facilitate Cross-Lingual Transfer - ACL Anthology","url":"https://aclanthology.org/2025.insights-1.6/"},{"title":"Converging to a Lingua Franca: Evolution of Linguistic Regions and Semantics Alignment in Multilingual Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.707/"}]

Based on the search results, I found comprehensive information about LU-LAFNs and the related research:

## Overview

LU-LAFNs (Locating and Updating Language-Agnostic Factual Neurons) is a method for multilingual knowledge editing that aims to edit multilingual knowledge simultaneously while avoiding knowledge conflicts and improving edit performance.

## Key Discovery

The research discovered that the same factual knowledge in different languages generally activates a shared set of neurons, called language-agnostic factual neurons (LAFNs). These neurons represent the same factual knowledge shared across languages and imply the semantic connections among multilingual knowledge.

## How It Works

The LU-LAFNs architecture first locates the corresponding language-agnostic factual neurons, then optimizes update values for modifying them, and stores them in cache.

## Publication

The paper "Multilingual Knowledge Editing with Language-Agnostic Factual Neurons" by Zhang, Liang, Meng, and others was published in the Proceedings of the 31st International Conference on Computational Linguistics (COLING 2025) in Abu Dhabi, UAE in January 2025.

The research demonstrates the cross-lingual portability of factual knowledge by showing that editing knowledge in one language can simultaneously update related representations across multiple languages through these shared language-agnostic neurons.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27f57f2b-0daa-4bb6-99ec-503c1b9b40f5",
  "isSidechain": false,
  "promptId": "337860c3-19bc-47e7-8a4b-15fad24e9187",
  "type": "user",
  "uuid": "c31b88f2-ba9b-4a81-865b-1cd0b5d4371b",
  "toolUseResult": {
    "query": "LU-LAFNs language-agnostic factual neurons COLING 2025 cross-lingual portability",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RuAtGyigi3snvUmEVyjPX6",
        "content": [
          {
            "title": "Multilingual Knowledge Editing with Language-Agnostic Factual Neurons - ACL Anthology",
            "url": "https://aclanthology.org/2025.coling-main.385/"
          },
          {
            "title": "Multilingual Knowledge Editing with Language-Agnostic Factual Neurons",
            "url": "https://arxiv.org/pdf/2406.16416"
          },
          {
            "title": "Multilingual Knowledge Editing with Language-Agnostic Factual Neurons",
            "url": "https://arxiv.org/html/2406.16416"
          },
          {
            "title": "[2406.16416] Multilingual Knowledge Editing with Language-Agnostic Factual Neurons",
            "url": "https://arxiv.org/abs/2406.16416"
          },
          {
            "title": "Multilingual Knowledge Editing with Language-Agnostic ...",
            "url": "https://aclanthology.org/2025.coling-main.385.pdf"
          },
          {
            "title": "Multilingual Knowledge Editing with Language-Agnostic Factual Neurons - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240616416Z/abstract"
          },
          {
            "title": "Language-Specific Neurons Do Not Facilitate Cross-Lingual Transfer - ACL Anthology",
            "url": "https://aclanthology.org/2025.insights-1.6/"
          },
          {
            "title": "Converging to a Lingua Franca: Evolution of Linguistic Regions and Semantics Alignment in Multilingual Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2025.coling-main.707/"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about LU-LAFNs and the related research:\n\n## Overview\n\nLU-LAFNs (Locating and Updating Language-Agnostic Factual Neurons) is a method for multilingual knowledge editing that aims to edit multilingual knowledge simultaneously while avoiding knowledge conflicts and improving edit performance.\n\n## Key Discovery\n\nThe research discovered that the same factual knowledge in different languages generally activates a shared set of neurons, called language-agnostic factual neurons (LAFNs). These neurons represent the same factual knowledge shared across languages and imply the semantic connections among multilingual knowledge.\n\n## How It Works\n\nThe LU-LAFNs architecture first locates the corresponding language-agnostic factual neurons, then optimizes update values for modifying them, and stores them in cache.\n\n## Publication\n\nThe paper \"Multilingual Knowledge Editing with Language-Agnostic Factual Neurons\" by Zhang, Liang, Meng, and others was published in the Proceedings of the 31st International Conference on Computational Linguistics (COLING 2025) in Abu Dhabi, UAE in January 2025.\n\nThe research demonstrates the cross-lingual portability of factual knowledge by showing that editing knowledge in one language can simultaneously update related representations across multiple languages through these shared language-agnostic neurons."
    ],
    "durationSeconds": 9.272300661000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "27f57f2b-0daa-4bb6-99ec-503c1b9b40f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T18:49:24.629Z_

<details><summary>↩ Tool result · `toolu_01QRYs5SyvATxybAoMeLbfw9`</summary>

```text
Web search results for query: "FeatureEdit SAE sparse autoencoder knowledge editing ACL 2025 arXiv:2502.12483"

Links: [{"title":"Sparse Autoencoder Features for Classifications and Transferability - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1521/"},{"title":"Unveiling Language-Specific Features in Large Language Models via Sparse Autoencoders - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.229/"},{"title":"Model Unlearning via Sparse Autoencoder Subspace Guided Projections - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1348/"},{"title":"Sparse Autoencoder Features for Classifications and Transferability","url":"https://aclanthology.org/2025.emnlp-main.1521.pdf"},{"title":"Beyond Activation Patterns: A Weight-Based Out-of-Context Explanation of Sparse Autoencoder Features","url":"https://arxiv.org/pdf/2601.22447"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based   Representation Engineering","url":"https://arxiv.org/pdf/2410.15999"}]

Let me search more specifically for FeatureEdit and the arXiv paper you mentioned:

Links: [{"title":"[2502.12483] The Knowledge Microscope: Features as Better Analytical Lenses than Neurons","url":"https://arxiv.org/abs/2502.12483"},{"title":"The Knowledge Microscope: Features as Better Analytical Lenses than Neurons","url":"https://arxiv.org/html/2502.12483"},{"title":"The Knowledge Microscope: Features as Better Analytical Lenses than   Neurons","url":"https://arxiv.org/pdf/2502.12483"},{"title":"Analysis of feature influence on Covid-19 Death Rate Per Country Using a Novel Orthogonalization Technique","url":"https://www.medrxiv.org/content/10.1101/2021.07.02.21259929.full.pdf"},{"title":"Canonical time-series features for characterizing biologically informative dynamical patterns in fMRI","url":"https://www.biorxiv.org/content/10.1101/2024.07.14.603477.full.pdf"},{"title":"Leveraging Feature Transfer to Predict Medication Resistance and Secondary-Clinical Outcomes in Psychotic Disorders in Forensic Settings","url":"https://www.medrxiv.org/content/10.1101/2025.03.06.25321797.full.pdf"}]

Perfect! I found the paper. Based on the search results, here's what I found about FeatureEdit and the arXiv paper:

## FeatureEdit: SAE-Based Knowledge Editing

FeatureEdit is the first feature-based model editing method, presented in the paper "The Knowledge Microscope: Features as Better Analytical Lenses than Neurons" (arXiv:2502.12483).

### Key Findings

The paper validates that Sparse Autoencoders (SAE) can effectively decompose neurons into features, which serve as alternative analytical units for understanding language models. The research demonstrates three key advantages of features over neurons:

1. **Stronger Influence and Interpretability**: Features exhibit stronger influence on knowledge expression and superior interpretability

2. **Enhanced Monosemanticity**: Features demonstrate enhanced monosemanticity, showing distinct activation patterns between related and unrelated facts

3. **Better Privacy Protection**: Features achieve better privacy protection than neurons, demonstrated through the proposed FeatureEdit method, which significantly outperforms existing neuron-based approaches in erasing privacy-sensitive information from LMs

### Performance

Compared to neuron-based approaches, FeatureEdit achieves higher success rates in erasing privacy-sensitive knowledge from LMs while maintaining better generalization across semantically equivalent rephrase queries, and causes less damage to the model's general capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "160d731b-247e-4594-bced-4fca44fc6956",
  "isSidechain": false,
  "promptId": "337860c3-19bc-47e7-8a4b-15fad24e9187",
  "type": "user",
  "uuid": "ef39cd18-bf34-4373-b6cf-c2e6643534fd",
  "toolUseResult": {
    "query": "FeatureEdit SAE sparse autoencoder knowledge editing ACL 2025 arXiv:2502.12483",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Exn7nXRNRB2PNqDTmzMq6N",
        "content": [
          {
            "title": "Sparse Autoencoder Features for Classifications and Transferability - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.1521/"
          },
          {
            "title": "Unveiling Language-Specific Features in Large Language Models via Sparse Autoencoders - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.229/"
          },
          {
            "title": "Model Unlearning via Sparse Autoencoder Subspace Guided Projections - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.1348/"
          },
          {
            "title": "Sparse Autoencoder Features for Classifications and Transferability",
            "url": "https://aclanthology.org/2025.emnlp-main.1521.pdf"
          },
          {
            "title": "Beyond Activation Patterns: A Weight-Based Out-of-Context Explanation of Sparse Autoencoder Features",
            "url": "https://arxiv.org/pdf/2601.22447"
          },
          {
            "title": "Steering Knowledge Selection Behaviours in LLMs via SAE-Based   Representation Engineering",
            "url": "https://arxiv.org/pdf/2410.15999"
          }
        ]
      },
      "Let me search more specifically for FeatureEdit and the arXiv paper you mentioned:",
      {
        "tool_use_id": "srvtoolu_01QcdMoTsqYfvFgdavWuY6u8",
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
            "title": "Analysis of feature influence on Covid-19 Death Rate Per Country Using a Novel Orthogonalization Technique",
            "url": "https://www.medrxiv.org/content/10.1101/2021.07.02.21259929.full.pdf"
          },
          {
            "title": "Canonical time-series features for characterizing biologically informative dynamical patterns in fMRI",
            "url": "https://www.biorxiv.org/content/10.1101/2024.07.14.603477.full.pdf"
          },
          {
            "title": "Leveraging Feature Transfer to Predict Medication Resistance and Secondary-Clinical Outcomes in Psychotic Disorders in Forensic Settings",
            "url": "https://www.medrxiv.org/content/10.1101/2025.03.06.25321797.full.pdf"
          }
        ]
      },
      "Perfect! I found the paper. Based on the search results, here's what I found about FeatureEdit and the arXiv paper:\n\n## FeatureEdit: SAE-Based Knowledge Editing\n\nFeatureEdit is the first feature-based model editing method, presented in the paper \"The Knowledge Microscope: Features as Better Analytical Lenses than Neurons\" (arXiv:2502.12483).\n\n### Key Findings\n\nThe paper validates that Sparse Autoencoders (SAE) can effectively decompose neurons into features, which serve as alternative analytical units for understanding language models. The research demonstrates three key advantages of features over neurons:\n\n1. **Stronger Influence and Interpretability**: Features exhibit stronger influence on knowledge expression and superior interpretability\n\n2. **Enhanced Monosemanticity**: Features demonstrate enhanced monosemanticity, showing distinct activation patterns between related and unrelated facts\n\n3. **Better Privacy Protection**: Features achieve better privacy protection than neurons, demonstrated through the proposed FeatureEdit method, which significantly outperforms existing neuron-based approaches in erasing privacy-sensitive information from LMs\n\n### Performance\n\nCompared to neuron-based approaches, FeatureEdit achieves higher success rates in erasing privacy-sensitive knowledge from LMs while maintaining better generalization across semantically equivalent rephrase queries, and causes less damage to the model's general capabilities."
    ],
    "durationSeconds": 9.773435678000002,
    "searchCount": 2
  },
  "sourceToolAssistantUUID": "160d731b-247e-4594-bced-4fca44fc6956",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation  ## Description Current c…",
  "leafUuid": "ef39cd18-bf34-4373-b6cf-c2e6643534fd",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE features for cross-lingual knowledge editing",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f"
}
```

---

### Tool result

_source line 25 · 2026-05-19T18:49:26.326Z_

<details><summary>↩ Tool result · `toolu_015zMzwvJqisdfZ8NF5q2GmK`</summary>

```text
Web search results for query: "sparse autoencoder intervention skepticism Peng et al 2025 Arad et al SAE steering feature selection"

Links: [{"title":"Sparse Autoencoder Steering","url":"https://www.emergentmind.com/topics/sparse-autoencoder-steering"},{"title":"Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts","url":"https://arxiv.org/html/2506.23845v1"},{"title":"(PDF) Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts","url":"https://www.researchgate.net/publication/393183364_Use_Sparse_Autoencoders_to_Discover_Unknown_Concepts_Not_to_Act_on_Known_Concepts"},{"title":"Steering Language Model Refusal with Sparse Autoencoders","url":"https://arxiv.org/pdf/2411.11296"},{"title":"Does higher interpretability imply better utility? A Pairwise Analysis on Sparse Autoencoders","url":"https://arxiv.org/pdf/2510.03659"},{"title":"Denoising Concept Vectors with Sparse Autoencoders for Improved Language Model Steering","url":"https://arxiv.org/pdf/2505.15038"},{"title":"Improving Steering Vectors by Targeting Sparse Autoencoder Features","url":"https://arxiv.org/pdf/2411.02193"},{"title":"Sparse Autoencoders as a Steering Basis for Phase Synchronization in Graph-Based CFD Surrogates","url":"https://arxiv.org/pdf/2604.04946"}]

Based on my search results, I found relevant information about your query regarding sparse autoencoders (SAEs), intervention skepticism, and the work of Peng et al. and Arad et al.:

## Key Findings

**On Intervention Skepticism:**

While sparse autoencoders (SAEs) have generated significant excitement, a series of negative results have added to skepticism about their usefulness. However, a conceptual distinction reconciles competing narratives surrounding SAEs: while SAEs may be less effective for acting on known concepts, SAEs are powerful tools for discovering unknown concepts.

**Peng et al. 2025 Research:**

The paper "Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts" is by Kenny Peng (Cornell Tech), Rajiv Movva (UC Berkeley), Jon Kleinberg (Cornell University), Emma Pierson (UC Berkeley), and Nikhil Garg (Cornell Tech). The paper outlines use cases for SAEs in ML interpretability, explainability, fairness, auditing, and safety, and in social and health sciences.

**Feature Selection and Steering Effectiveness:**

Research shows that when benchmarked against existing output score-based methods from Arad et al. (2025), improved feature selection approaches yield substantial improvements in steering score and underscore the critical role of feature selection in characterizing and enhancing the steering utility of SAEs.

**Optimal Steering Layers:**

Ablations show that steering is most effective at mid-to-deep layers, with optimal injection strengths rising deeper in the model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f2509a3-6620-43ed-ac29-1c35fac1f6ca",
  "isSidechain": false,
  "promptId": "337860c3-19bc-47e7-8a4b-15fad24e9187",
  "type": "user",
  "uuid": "2f774994-5b88-43b4-b08f-1a5342c062aa",
  "toolUseResult": {
    "query": "sparse autoencoder intervention skepticism Peng et al 2025 Arad et al SAE steering feature selection",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V96gbrPQFKDCrkrD1BHwpK",
        "content": [
          {
            "title": "Sparse Autoencoder Steering",
            "url": "https://www.emergentmind.com/topics/sparse-autoencoder-steering"
          },
          {
            "title": "Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts",
            "url": "https://arxiv.org/html/2506.23845v1"
          },
          {
            "title": "(PDF) Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts",
            "url": "https://www.researchgate.net/publication/393183364_Use_Sparse_Autoencoders_to_Discover_Unknown_Concepts_Not_to_Act_on_Known_Concepts"
          },
          {
            "title": "Steering Language Model Refusal with Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2411.11296"
          },
          {
            "title": "Does higher interpretability imply better utility? A Pairwise Analysis on Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2510.03659"
          },
          {
            "title": "Denoising Concept Vectors with Sparse Autoencoders for Improved Language Model Steering",
            "url": "https://arxiv.org/pdf/2505.15038"
          },
          {
            "title": "Improving Steering Vectors by Targeting Sparse Autoencoder Features",
            "url": "https://arxiv.org/pdf/2411.02193"
          },
          {
            "title": "Sparse Autoencoders as a Steering Basis for Phase Synchronization in Graph-Based CFD Surrogates",
            "url": "https://arxiv.org/pdf/2604.04946"
          }
        ]
      },
      "Based on my search results, I found relevant information about your query regarding sparse autoencoders (SAEs), intervention skepticism, and the work of Peng et al. and Arad et al.:\n\n## Key Findings\n\n**On Intervention Skepticism:**\n\nWhile sparse autoencoders (SAEs) have generated significant excitement, a series of negative results have added to skepticism about their usefulness. However, a conceptual distinction reconciles competing narratives surrounding SAEs: while SAEs may be less effective for acting on known concepts, SAEs are powerful tools for discovering unknown concepts.\n\n**Peng et al. 2025 Research:**\n\nThe paper \"Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts\" is by Kenny Peng (Cornell Tech), Rajiv Movva (UC Berkeley), Jon Kleinberg (Cornell University), Emma Pierson (UC Berkeley), and Nikhil Garg (Cornell Tech). The paper outlines use cases for SAEs in ML interpretability, explainability, fairness, auditing, and safety, and in social and health sciences.\n\n**Feature Selection and Steering Effectiveness:**\n\nResearch shows that when benchmarked against existing output score-based methods from Arad et al. (2025), improved feature selection approaches yield substantial improvements in steering score and underscore the critical role of feature selection in characterizing and enhancing the steering utility of SAEs.\n\n**Optimal Steering Layers:**\n\nAblations show that steering is most effective at mid-to-deep layers, with optimal injection strengths rising deeper in the model."
    ],
    "durationSeconds": 10.059676797000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5f2509a3-6620-43ed-ac29-1c35fac1f6ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T18:49:31.316Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've found initial information. Now let me do a few more targeted searches to understand:
1. LangSAE and its cross-lingual retrieval results
2. Leask et al. on SAE feature non-canonicality (ICLR 2025)
3. Whether anyone has already combined SAE features with cross-lingual knowledge editing (the claimed gap)
4. Mondal et al. NAACL 2025 on neuron-level language-specific interventions
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f774994-5b88-43b4-b08f-1a5342c062aa",
  "isSidechain": false,
  "requestId": "req_011CbCRos78JBMc4ZCf38qo5",
  "type": "assistant",
  "uuid": "04311223-2cd7-407a-adc4-b2e03870bf43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TL9gbisFnBTq6HASJcHeG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 716,
      "cache_creation_input_tokens": 3805,
      "cache_read_input_tokens": 24011,
      "output_tokens": 412,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 716,
          "output_tokens": 412,
          "cache_read_input_tokens": 24011,
          "cache_creation_input_tokens": 3805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3805
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

_source line 27 · 2026-05-19T18:49:31.810Z_

Good initial results. Let me do a few more targeted searches to verify the claimed gap and check for any competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04311223-2cd7-407a-adc4-b2e03870bf43",
  "isSidechain": false,
  "requestId": "req_011CbCRos78JBMc4ZCf38qo5",
  "type": "assistant",
  "uuid": "669f31ea-ab5a-40db-9aca-eabb1355eb80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TL9gbisFnBTq6HASJcHeG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 716,
      "cache_creation_input_tokens": 3805,
      "cache_read_input_tokens": 24011,
      "output_tokens": 412,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 716,
          "output_tokens": 412,
          "cache_read_input_tokens": 24011,
          "cache_creation_input_tokens": 3805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3805
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

_source line 28 · 2026-05-19T18:49:32.770Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AXUkiJcxCGAQmAgpcB25Xp`</summary>

```json
{
  "query": "SAE sparse autoencoder cross-lingual knowledge editing 2025 2026 combining features multilingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "669f31ea-ab5a-40db-9aca-eabb1355eb80",
  "isSidechain": false,
  "requestId": "req_011CbCRos78JBMc4ZCf38qo5",
  "type": "assistant",
  "uuid": "00c5d8f5-63cf-46b6-8ffb-f6abef00baf2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TL9gbisFnBTq6HASJcHeG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 716,
      "cache_creation_input_tokens": 3805,
      "cache_read_input_tokens": 24011,
      "output_tokens": 412,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 716,
          "output_tokens": 412,
          "cache_read_input_tokens": 24011,
          "cache_creation_input_tokens": 3805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3805
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

_source line 29 · 2026-05-19T18:49:33.254Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011v7p952akGYByjrxWTSR8H`</summary>

```json
{
  "query": "Leask et al \"sparse autoencoders do not find canonical units\" ICLR 2025 meta-SAE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00c5d8f5-63cf-46b6-8ffb-f6abef00baf2",
  "isSidechain": false,
  "requestId": "req_011CbCRos78JBMc4ZCf38qo5",
  "type": "assistant",
  "uuid": "4ed43239-5b59-4404-9354-95193aaa5167",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TL9gbisFnBTq6HASJcHeG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 716,
      "cache_creation_input_tokens": 3805,
      "cache_read_input_tokens": 24011,
      "output_tokens": 412,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 716,
          "output_tokens": 412,
          "cache_read_input_tokens": 24011,
          "cache_creation_input_tokens": 3805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3805
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

_source line 30 · 2026-05-19T18:49:33.718Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017Y2hh3KN2RVP3LBkURKxD4`</summary>

```json
{
  "query": "Mondal et al \"language-specific neurons do not facilitate cross-lingual transfer\" NAACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ed43239-5b59-4404-9354-95193aaa5167",
  "isSidechain": false,
  "requestId": "req_011CbCRos78JBMc4ZCf38qo5",
  "type": "assistant",
  "uuid": "144e1444-2d72-4168-abb5-997fd85474af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TL9gbisFnBTq6HASJcHeG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 716,
      "cache_creation_input_tokens": 3805,
      "cache_read_input_tokens": 24011,
      "output_tokens": 412,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 716,
          "output_tokens": 412,
          "cache_read_input_tokens": 24011,
          "cache_creation_input_tokens": 3805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3805
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

_source line 31 · 2026-05-19T18:49:34.945Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AU5EcxECVqwiyfm5gdQTVn`</summary>

```json
{
  "query": "SCAN sparse circuit anchor lifelong editing Qwen Llama 2026 arXiv:2603.15226"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "144e1444-2d72-4168-abb5-997fd85474af",
  "isSidechain": false,
  "requestId": "req_011CbCRos78JBMc4ZCf38qo5",
  "type": "assistant",
  "uuid": "2e1379da-ee81-4b48-92ae-d642a71a3d59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TL9gbisFnBTq6HASJcHeG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 716,
      "cache_creation_input_tokens": 3805,
      "cache_read_input_tokens": 24011,
      "output_tokens": 412,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 716,
          "output_tokens": 412,
          "cache_read_input_tokens": 24011,
          "cache_creation_input_tokens": 3805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3805
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

_source line 32 · 2026-05-19T18:49:39.033Z_

<details><summary>↩ Tool result · `toolu_017Y2hh3KN2RVP3LBkURKxD4`</summary>

```text
Web search results for query: "Mondal et al "language-specific neurons do not facilitate cross-lingual transfer" NAACL 2025"

Links: [{"title":"Language-Specific Neurons Do Not Facilitate Cross-Lingual Transfer - ACL Anthology","url":"https://aclanthology.org/2025.insights-1.6/"},{"title":"Tracing Multilingual Knowledge Acquisition Dynamics in Domain Adaptation: A Case Study of English-Japanese Biomedical Adaptation","url":"https://arxiv.org/html/2510.12115v1"},{"title":"Linguistic Neuron Overlap Patterns to Facilitate Cross-lingual Transfer on Low-resource Languages","url":"https://arxiv.org/html/2508.17078v2"},{"title":"[2503.17456] Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer","url":"https://arxiv.org/abs/2503.17456"},{"title":"Language Arithmetics: Towards Systematic Language Neuron Identification and Manipulation","url":"https://arxiv.org/html/2507.22608v1"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/html/2601.16390v1"},{"title":"Unveiling the Influence of Amplifying Language-Specific Neurons","url":"https://arxiv.org/html/2507.22581v3"},{"title":"Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer - Paper Detail","url":"https://deeplearn.org/arxiv/590221/language-specific-neurons-do-not-facilitate-cross-lingual-transfer"},{"title":"Language-specific Neurons Do Not Facilitate Cross- ...","url":"https://aclanthology.org/2025.insights-1.6.pdf"},{"title":"Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer","url":"https://arxiv.org/pdf/2503.17456"}]

I found the paper you're looking for! The paper "Language-Specific Neurons Do Not Facilitate Cross-Lingual Transfer" by Mondal et al. was published in The Sixth Workshop on Insights from Negative Results in NLP in May 2025.

The research explores whether existing techniques to identify language-specific neurons can be leveraged to enhance cross-lingual task performance of low-resource languages in multilingual large language models.

The paper appears to be available through multiple sources:
- It was also published in Findings of the Association for Computational Linguistics: NAACL 2025
- The ACL Anthology page: https://aclanthology.org/2025.insights-1.6/
- arXiv: https://arxiv.org/abs/2503.17456

The work has already generated follow-up research, with other scholars building on or responding to its findings regarding the role of language-specific neurons in cross-lingual transfer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "144e1444-2d72-4168-abb5-997fd85474af",
  "isSidechain": false,
  "promptId": "337860c3-19bc-47e7-8a4b-15fad24e9187",
  "type": "user",
  "uuid": "70699df9-422a-4919-b7c2-6f131bccf05b",
  "toolUseResult": {
    "query": "Mondal et al \"language-specific neurons do not facilitate cross-lingual transfer\" NAACL 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CqaQWDVYHMQmom87Q2UxoW",
        "content": [
          {
            "title": "Language-Specific Neurons Do Not Facilitate Cross-Lingual Transfer - ACL Anthology",
            "url": "https://aclanthology.org/2025.insights-1.6/"
          },
          {
            "title": "Tracing Multilingual Knowledge Acquisition Dynamics in Domain Adaptation: A Case Study of English-Japanese Biomedical Adaptation",
            "url": "https://arxiv.org/html/2510.12115v1"
          },
          {
            "title": "Linguistic Neuron Overlap Patterns to Facilitate Cross-lingual Transfer on Low-resource Languages",
            "url": "https://arxiv.org/html/2508.17078v2"
          },
          {
            "title": "[2503.17456] Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer",
            "url": "https://arxiv.org/abs/2503.17456"
          },
          {
            "title": "Language Arithmetics: Towards Systematic Language Neuron Identification and Manipulation",
            "url": "https://arxiv.org/html/2507.22608v1"
          },
          {
            "title": "Cross-Lingual Activation Steering for Multilingual Language Models",
            "url": "https://arxiv.org/html/2601.16390v1"
          },
          {
            "title": "Unveiling the Influence of Amplifying Language-Specific Neurons",
            "url": "https://arxiv.org/html/2507.22581v3"
          },
          {
            "title": "Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer - Paper Detail",
            "url": "https://deeplearn.org/arxiv/590221/language-specific-neurons-do-not-facilitate-cross-lingual-transfer"
          },
          {
            "title": "Language-specific Neurons Do Not Facilitate Cross- ...",
            "url": "https://aclanthology.org/2025.insights-1.6.pdf"
          },
          {
            "title": "Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer",
            "url": "https://arxiv.org/pdf/2503.17456"
          }
        ]
      },
      "I found the paper you're looking for! The paper \"Language-Specific Neurons Do Not Facilitate Cross-Lingual Transfer\" by Mondal et al. was published in The Sixth Workshop on Insights from Negative Results in NLP in May 2025.\n\nThe research explores whether existing techniques to identify language-specific neurons can be leveraged to enhance cross-lingual task performance of low-resource languages in multilingual large language models.\n\nThe paper appears to be available through multiple sources:\n- It was also published in Findings of the Association for Computational Linguistics: NAACL 2025\n- The ACL Anthology page: https://aclanthology.org/2025.insights-1.6/\n- arXiv: https://arxiv.org/abs/2503.17456\n\nThe work has already generated follow-up research, with other scholars building on or responding to its findings regarding the role of language-specific neurons in cross-lingual transfer."
    ],
    "durationSeconds": 5.3114240159999975,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "144e1444-2d72-4168-abb5-997fd85474af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T18:49:40.164Z_

<details><summary>↩ Tool result · `toolu_01AXUkiJcxCGAQmAgpcB25Xp`</summary>

```text
Web search results for query: "SAE sparse autoencoder cross-lingual knowledge editing 2025 2026 combining features multilingual"

Links: [{"title":"[2507.11230] Sparse Autoencoders Can Capture Language-Specific Concepts Across Diverse Languages","url":"https://arxiv.org/abs/2507.11230"},{"title":"Sparse Autoencoder Features for Classifications and Transferability","url":"https://arxiv.org/html/2502.11367v1"},{"title":"Sparse Autoencoders Can Capture Language-Specific Concepts Across Diverse Languages","url":"https://arxiv.org/pdf/2507.11230"},{"title":"Sparse Autoencoder Features for Classifications and Transferability - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1521/"},{"title":"Sparse Autoencoder Features for Classifications and Transferability","url":"https://aclanthology.org/2025.emnlp-main.1521.pdf"},{"title":"Applying sparse autoencoders to unlearn knowledge in language models","url":"https://arxiv.org/pdf/2410.19278"},{"title":"Causal Language Control in Multilingual Transformers via Sparse Feature Steering","url":"https://arxiv.org/pdf/2507.13410"},{"title":"Cross-Lingual Knowledge Editing in Large Language Models","url":"https://arxiv.org/pdf/2309.08952"}]

Based on the search results, here are the key findings on SAE (sparse autoencoder) applications in cross-lingual and multilingual contexts:

## Language-Specific Features in SAEs

SAE-LAPE is a method based on feature activation probability to identify language-specific features within the feed-forward network. Sparse autoencoders (SAEs) have the ability to learn monosemantic features that represent concrete and abstract concepts across languages in LLMs.

## Recent Research (2025-2026)

A paper submitted on July 15, 2025 and revised on February 23, 2026 investigates how sparse autoencoders can capture language-specific concepts across diverse languages. The SAE-LAPE method identifies language-specific features within the feed-forward network, with many such features predominantly appearing in the middle to final layers of the model and being interpretable.

## Multilingual Control and Steering

Recent work on sparse autoencoders has shown that transformer residual streams can be decomposed into interpretable, behavior-aligned directions, and methods such as Feature-Guided Activation Additions (FGAA) and SAE-Targeted Steering (SAE-TS) demonstrate that selectively activating SAE features can causally steer LLM behavior.

## Cross-Lingual Knowledge Editing

Research has evaluated cross-lingual knowledge editing on multilingual LLMs using seven knowledge editing methods covering memory-based, meta-learning, and locate-then-edit paradigms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00c5d8f5-63cf-46b6-8ffb-f6abef00baf2",
  "isSidechain": false,
  "promptId": "337860c3-19bc-47e7-8a4b-15fad24e9187",
  "type": "user",
  "uuid": "d3bc7a30-ccef-4710-bb83-5ddf0f018073",
  "toolUseResult": {
    "query": "SAE sparse autoencoder cross-lingual knowledge editing 2025 2026 combining features multilingual",
    "results": [
      {
        "tool_use_id": "srvtoolu_015AAqpu5s6st5VAWVH92HFA",
        "content": [
          {
            "title": "[2507.11230] Sparse Autoencoders Can Capture Language-Specific Concepts Across Diverse Languages",
            "url": "https://arxiv.org/abs/2507.11230"
          },
          {
            "title": "Sparse Autoencoder Features for Classifications and Transferability",
            "url": "https://arxiv.org/html/2502.11367v1"
          },
          {
            "title": "Sparse Autoencoders Can Capture Language-Specific Concepts Across Diverse Languages",
            "url": "https://arxiv.org/pdf/2507.11230"
          },
          {
            "title": "Sparse Autoencoder Features for Classifications and Transferability - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.1521/"
          },
          {
            "title": "Sparse Autoencoder Features for Classifications and Transferability",
            "url": "https://aclanthology.org/2025.emnlp-main.1521.pdf"
          },
          {
            "title": "Applying sparse autoencoders to unlearn knowledge in language models",
            "url": "https://arxiv.org/pdf/2410.19278"
          },
          {
            "title": "Causal Language Control in Multilingual Transformers via Sparse Feature Steering",
            "url": "https://arxiv.org/pdf/2507.13410"
          },
          {
            "title": "Cross-Lingual Knowledge Editing in Large Language Models",
            "url": "https://arxiv.org/pdf/2309.08952"
          }
        ]
      },
      "Based on the search results, here are the key findings on SAE (sparse autoencoder) applications in cross-lingual and multilingual contexts:\n\n## Language-Specific Features in SAEs\n\nSAE-LAPE is a method based on feature activation probability to identify language-specific features within the feed-forward network. Sparse autoencoders (SAEs) have the ability to learn monosemantic features that represent concrete and abstract concepts across languages in LLMs.\n\n## Recent Research (2025-2026)\n\nA paper submitted on July 15, 2025 and revised on February 23, 2026 investigates how sparse autoencoders can capture language-specific concepts across diverse languages. The SAE-LAPE method identifies language-specific features within the feed-forward network, with many such features predominantly appearing in the middle to final layers of the model and being interpretable.\n\n## Multilingual Control and Steering\n\nRecent work on sparse autoencoders has shown that transformer residual streams can be decomposed into interpretable, behavior-aligned directions, and methods such as Feature-Guided Activation Additions (FGAA) and SAE-Targeted Steering (SAE-TS) demonstrate that selectively activating SAE features can causally steer LLM behavior.\n\n## Cross-Lingual Knowledge Editing\n\nResearch has evaluated cross-lingual knowledge editing on multilingual LLMs using seven knowledge editing methods covering memory-based, meta-learning, and locate-then-edit paradigms."
    ],
    "durationSeconds": 7.390138897000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "00c5d8f5-63cf-46b6-8ffb-f6abef00baf2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T18:49:40.569Z_

<details><summary>↩ Tool result · `toolu_011v7p952akGYByjrxWTSR8H`</summary>

```text
Web search results for query: "Leask et al "sparse autoencoders do not find canonical units" ICLR 2025 meta-SAE"

Links: [{"title":"Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/84ca3f2d9d9bfca13f69b48ea63eb4a5-Abstract-Conference.html"},{"title":"(PDF) Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://www.researchgate.net/publication/388847461_Sparse_Autoencoders_Do_Not_Find_Canonical_Units_of_Analysis"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2502.04878"},{"title":"ICLR Poster Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://iclr.cc/virtual/2025/poster/30676"},{"title":"[2502.04878] Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://arxiv.org/abs/2502.04878"},{"title":"[Literature Review] Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://www.themoonlight.io/en/review/sparse-autoencoders-do-not-find-canonical-units-of-analysis"},{"title":"Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://arxiv.org/html/2502.04878v1"},{"title":"SPARSE AUTOENCODERS DO NOT FIND CANONICAL ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/84ca3f2d9d9bfca13f69b48ea63eb4a5-Paper-Conference.pdf"},{"title":"MetaSAEs: Joint Training with a Decomposability Penalty Produces More Atomic Sparse Autoencoder Latents","url":"https://arxiv.org/pdf/2604.03436"}]

Based on the search results, here's what I found about the paper:

The paper "Sparse Autoencoders Do Not Find Canonical Units of Analysis" was published at ICLR 2025 by Patrick Leask, Bart Bussmann, Michael Pearce, Joseph Bloom, Curt Tigges, Noura Al Moubayed, Lee Sharkey, and Neel Nanda.

**Main Contributions:**

The authors cast doubt on the belief that SAEs can find canonical units using two novel techniques: SAE stitching to show they are incomplete, and meta-SAEs to show they are not atomic.

**Key Techniques:**

1. **SAE Stitching**: SAE stitching involves inserting or swapping latents from a larger SAE into a smaller one. Latents from the larger SAE can be divided into categories including novel latents, which improve performance when added to the smaller SAE, indicating they capture novel information.

2. **Meta-SAEs**: Using meta-SAEs -- SAEs trained on the decoder matrix of another SAE -- the authors find that latents in SAEs often decompose into combinations of latents from a smaller SAE, showing that larger SAE latents are not atomic.

**Example Finding**: The resulting decompositions are often interpretable; for example, a latent representing "Einstein" decomposes into "scientist", "Germany", and "famous person".

The authors suggest that future research should either pursue different approaches for identifying such units, or pragmatically choose the SAE size suited to their task.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ed43239-5b59-4404-9354-95193aaa5167",
  "isSidechain": false,
  "promptId": "337860c3-19bc-47e7-8a4b-15fad24e9187",
  "type": "user",
  "uuid": "2e7eef5e-8eea-47c9-a342-e01022867543",
  "toolUseResult": {
    "query": "Leask et al \"sparse autoencoders do not find canonical units\" ICLR 2025 meta-SAE",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TyTZbFRKocDdGLVU9BHTnT",
        "content": [
          {
            "title": "Sparse Autoencoders Do Not Find Canonical Units of Analysis",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/84ca3f2d9d9bfca13f69b48ea63eb4a5-Abstract-Conference.html"
          },
          {
            "title": "(PDF) Sparse Autoencoders Do Not Find Canonical Units of Analysis",
            "url": "https://www.researchgate.net/publication/388847461_Sparse_Autoencoders_Do_Not_Find_Canonical_Units_of_Analysis"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://arxiv.org/pdf/2502.04878"
          },
          {
            "title": "ICLR Poster Sparse Autoencoders Do Not Find Canonical Units of Analysis",
            "url": "https://iclr.cc/virtual/2025/poster/30676"
          },
          {
            "title": "[2502.04878] Sparse Autoencoders Do Not Find Canonical Units of Analysis",
            "url": "https://arxiv.org/abs/2502.04878"
          },
          {
            "title": "[Literature Review] Sparse Autoencoders Do Not Find Canonical Units of Analysis",
            "url": "https://www.themoonlight.io/en/review/sparse-autoencoders-do-not-find-canonical-units-of-analysis"
          },
          {
            "title": "Sparse Autoencoders Do Not Find Canonical Units of Analysis",
            "url": "https://arxiv.org/html/2502.04878v1"
          },
          {
            "title": "SPARSE AUTOENCODERS DO NOT FIND CANONICAL ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/84ca3f2d9d9bfca13f69b48ea63eb4a5-Paper-Conference.pdf"
          },
          {
            "title": "MetaSAEs: Joint Training with a Decomposability Penalty Produces More Atomic Sparse Autoencoder Latents",
            "url": "https://arxiv.org/pdf/2604.03436"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper:\n\nThe paper \"Sparse Autoencoders Do Not Find Canonical Units of Analysis\" was published at ICLR 2025 by Patrick Leask, Bart Bussmann, Michael Pearce, Joseph Bloom, Curt Tigges, Noura Al Moubayed, Lee Sharkey, and Neel Nanda.\n\n**Main Contributions:**\n\nThe authors cast doubt on the belief that SAEs can find canonical units using two novel techniques: SAE stitching to show they are incomplete, and meta-SAEs to show they are not atomic.\n\n**Key Techniques:**\n\n1. **SAE Stitching**: SAE stitching involves inserting or swapping latents from a larger SAE into a smaller one. Latents from the larger SAE can be divided into categories including novel latents, which improve performance when added to the smaller SAE, indicating they capture novel information.\n\n2. **Meta-SAEs**: Using meta-SAEs -- SAEs trained on the decoder matrix of another SAE -- the authors find that latents in SAEs often decompose into combinations of latents from a smaller SAE, showing that larger SAE latents are not atomic.\n\n**Example Finding**: The resulting decompositions are often interpretable; for example, a latent representing \"Einstein\" decomposes into \"scientist\", \"Germany\", and \"famous person\".\n\nThe authors suggest that future research should either pursue different approaches for identifying such units, or pragmatically choose the SAE size suited to their task."
    ],
    "durationSeconds": 7.312456287000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4ed43239-5b59-4404-9354-95193aaa5167",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation  ## Description Current c…",
  "leafUuid": "2e7eef5e-8eea-47c9-a342-e01022867543",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE features for cross-lingual knowledge editing",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f"
}
```

---

### Tool result

_source line 37 · 2026-05-19T18:49:41.957Z_

<details><summary>↩ Tool result · `toolu_01AU5EcxECVqwiyfm5gdQTVn`</summary>

```text
Web search results for query: "SCAN sparse circuit anchor lifelong editing Qwen Llama 2026 arXiv:2603.15226"

Links: [{"title":"SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing","url":"https://arxiv.org/pdf/2603.15226"},{"title":"Representation Interventions Enable Lifelong Unstructured Knowledge Control","url":"https://arxiv.org/pdf/2511.20892"},{"title":"Beyond Hard Writes and Rigid Preservation: Soft Recursive Least-Squares for Lifelong LLM Editing","url":"https://arxiv.org/pdf/2601.15686"},{"title":"MEMOIR: Lifelong Model Editing with Minimal Overwrite and Informed Retention for LLMs","url":"https://arxiv.org/pdf/2506.07899"},{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/html/2504.17768v2"},{"title":"[2403.19647] Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models","url":"https://arxiv.org/abs/2403.19647"}]

I found the paper! Here are the search results:

**SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing**

The paper addresses how Large Language Models often suffer from catastrophic forgetting and collapse during sequential knowledge editing. The vulnerability stems from the prevailing dense editing paradigm, which treats models as black boxes and relies on coarse-grained parameter interventions that inevitably disrupt preserved knowledge.

SCAN (Sparse Circuit Anchored Neuron) transforms editing into a mechanism-aware manipulation by constructing a knowledge circuit via Sparse Transcoders. Experiments on Gemma2, Qwen3, and Llama3.1 across CounterFact, ZsRE and WikiFactDiff demonstrate that SCAN achieves superior performance, maintaining model integrity on benchmarks like MMLU and GSM8K even after 3,000 sequential edits, whereas other existing methods deteriorate progressively.

The paper was published on **March 17, 2026** as indicated by the preprint date. You can access the full paper directly at: https://arxiv.org/pdf/2603.15226


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e1379da-ee81-4b48-92ae-d642a71a3d59",
  "isSidechain": false,
  "promptId": "337860c3-19bc-47e7-8a4b-15fad24e9187",
  "type": "user",
  "uuid": "43dcbf97-a6d1-4d04-9240-3c445712f5a1",
  "toolUseResult": {
    "query": "SCAN sparse circuit anchor lifelong editing Qwen Llama 2026 arXiv:2603.15226",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HxFjAgkZahoVk7YZC6w5Ga",
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
            "title": "Beyond Hard Writes and Rigid Preservation: Soft Recursive Least-Squares for Lifelong LLM Editing",
            "url": "https://arxiv.org/pdf/2601.15686"
          },
          {
            "title": "MEMOIR: Lifelong Model Editing with Minimal Overwrite and Informed Retention for LLMs",
            "url": "https://arxiv.org/pdf/2506.07899"
          },
          {
            "title": "The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs",
            "url": "https://arxiv.org/html/2504.17768v2"
          },
          {
            "title": "[2403.19647] Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models",
            "url": "https://arxiv.org/abs/2403.19647"
          }
        ]
      },
      "I found the paper! Here are the search results:\n\n**SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing**\n\nThe paper addresses how Large Language Models often suffer from catastrophic forgetting and collapse during sequential knowledge editing. The vulnerability stems from the prevailing dense editing paradigm, which treats models as black boxes and relies on coarse-grained parameter interventions that inevitably disrupt preserved knowledge.\n\nSCAN (Sparse Circuit Anchored Neuron) transforms editing into a mechanism-aware manipulation by constructing a knowledge circuit via Sparse Transcoders. Experiments on Gemma2, Qwen3, and Llama3.1 across CounterFact, ZsRE and WikiFactDiff demonstrate that SCAN achieves superior performance, maintaining model integrity on benchmarks like MMLU and GSM8K even after 3,000 sequential edits, whereas other existing methods deteriorate progressively.\n\nThe paper was published on **March 17, 2026** as indicated by the preprint date. You can access the full paper directly at: https://arxiv.org/pdf/2603.15226"
    ],
    "durationSeconds": 7.009086907999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2e1379da-ee81-4b48-92ae-d642a71a3d59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-19T18:49:41.961Z_

```json
{
  "parentUuid": "43dcbf97-a6d1-4d04-9240-3c445712f5a1",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2d3ebd7e-56c2-4262-ae0d-1c92b71cecb9",
  "timestamp": "2026-05-19T18:49:41.961Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 39 · 2026-05-19T18:49:44.671Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do one more round of searches to verify the key gap claim - that no one has combined SAE features with cross-lingual knowledge editing - and to check for very recent (2026) work that might have addressed this.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d3ebd7e-56c2-4262-ae0d-1c92b71cecb9",
  "isSidechain": false,
  "requestId": "req_011CbCRq1yx5rX8g1E4y6hjP",
  "type": "assistant",
  "uuid": "4583bdb5-cb0f-4796-81c4-874655f9ec9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTCGCTdminn2DMwbM2Bkoq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4237,
      "cache_read_input_tokens": 27816,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4237,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 280,
          "cache_read_input_tokens": 27816,
          "cache_creation_input_tokens": 4237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4237
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

_source line 40 · 2026-05-19T18:49:45.616Z_

Let me do one final round of searches to check for very recent competing work and verify the gap claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4583bdb5-cb0f-4796-81c4-874655f9ec9a",
  "isSidechain": false,
  "requestId": "req_011CbCRq1yx5rX8g1E4y6hjP",
  "type": "assistant",
  "uuid": "87464695-2de2-430b-8939-0006f65181dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTCGCTdminn2DMwbM2Bkoq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4237,
      "cache_read_input_tokens": 27816,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4237,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 280,
          "cache_read_input_tokens": 27816,
          "cache_creation_input_tokens": 4237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4237
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

_source line 41 · 2026-05-19T18:49:46.094Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CCosL364dHRqiE4p5eeoPt`</summary>

```json
{
  "query": "\"SAE\" \"cross-lingual\" \"knowledge editing\" OR \"model editing\" 2026 features multilingual propagation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87464695-2de2-430b-8939-0006f65181dd",
  "isSidechain": false,
  "requestId": "req_011CbCRq1yx5rX8g1E4y6hjP",
  "type": "assistant",
  "uuid": "bce48fa3-4f4c-410f-8a61-ed90ab395483",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTCGCTdminn2DMwbM2Bkoq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4237,
      "cache_read_input_tokens": 27816,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4237,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 280,
          "cache_read_input_tokens": 27816,
          "cache_creation_input_tokens": 4237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4237
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

_source line 42 · 2026-05-19T18:49:47.034Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GdcQaZV1nyiFimEEjPCs4m`</summary>

```json
{
  "query": "LangSAE language identity removal SAE multilingual retrieval arXiv:2601.04768 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bce48fa3-4f4c-410f-8a61-ed90ab395483",
  "isSidechain": false,
  "requestId": "req_011CbCRq1yx5rX8g1E4y6hjP",
  "type": "assistant",
  "uuid": "56e06a0c-737a-47cc-9bd7-3ac0dc6c35a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTCGCTdminn2DMwbM2Bkoq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4237,
      "cache_read_input_tokens": 27816,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4237,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 280,
          "cache_read_input_tokens": 27816,
          "cache_creation_input_tokens": 4237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4237
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

_source line 43 · 2026-05-19T18:49:47.952Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019oue1z74pm36q4pwBMoADk`</summary>

```json
{
  "query": "Bi-ZsRE portability EM cross-lingual knowledge editing all methods near zero"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56e06a0c-737a-47cc-9bd7-3ac0dc6c35a4",
  "isSidechain": false,
  "requestId": "req_011CbCRq1yx5rX8g1E4y6hjP",
  "type": "assistant",
  "uuid": "ee0f2296-7ad6-45ce-9a12-8035ccd87272",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTCGCTdminn2DMwbM2Bkoq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4237,
      "cache_read_input_tokens": 27816,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4237,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 280,
          "cache_read_input_tokens": 27816,
          "cache_creation_input_tokens": 4237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4237
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

_source line 44 · 2026-05-19T18:49:51.763Z_

<details><summary>↩ Tool result · `toolu_01GdcQaZV1nyiFimEEjPCs4m`</summary>

```text
Web search results for query: "LangSAE language identity removal SAE multilingual retrieval arXiv:2601.04768 2026"

Links: [{"title":"[2601.04768] LANGSAE EDITING: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal","url":"https://arxiv.org/abs/2601.04768"},{"title":"LANGSAE EDITING: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal","url":"https://arxiv.org/pdf/2601.04768"},{"title":"LangSAE Editing: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal","url":"https://arxiv.org/html/2601.04768v1"},{"title":"LANGSAE EDITING: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2601.04768"},{"title":"LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering","url":"https://arxiv.org/pdf/2604.03532"}]

I found the paper you're looking for! Here's what the search revealed:

LangSAE Editing is a post-hoc sparse autoencoder trained on pooled embeddings that enables controllable removal of language-identity signal directly in vector space. 

The research addresses how multilingual embeddings encode language identity alongside semantics, where this language signal can inflate similarity for same-language pairs and crowd out relevant evidence written in other languages in dense retrieval scenarios.

The method identifies language-associated latent units using cross-language activation statistics, suppresses these units at inference time, and reconstructs embeddings in the original dimensionality, making it compatible with existing vector databases without retraining the base encoder or re-encoding raw text.

Experiments across multiple languages show consistent improvements in ranking quality and cross-language coverage, with especially strong gains for script-distinct languages.

The paper (arXiv:2601.04768) was submitted on January 8, 2026, and is authored by Dongjun Kim, Jeongho Yoon, Chanjun Park, and Heuiseok Lim from Korea University and Soongsil University.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56e06a0c-737a-47cc-9bd7-3ac0dc6c35a4",
  "isSidechain": false,
  "promptId": "337860c3-19bc-47e7-8a4b-15fad24e9187",
  "type": "user",
  "uuid": "828da204-0eb1-458a-b355-e0254ead3665",
  "toolUseResult": {
    "query": "LangSAE language identity removal SAE multilingual retrieval arXiv:2601.04768 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QMbRS42UmErHjiHKKtHA5o",
        "content": [
          {
            "title": "[2601.04768] LANGSAE EDITING: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal",
            "url": "https://arxiv.org/abs/2601.04768"
          },
          {
            "title": "LANGSAE EDITING: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal",
            "url": "https://arxiv.org/pdf/2601.04768"
          },
          {
            "title": "LangSAE Editing: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal",
            "url": "https://arxiv.org/html/2601.04768v1"
          },
          {
            "title": "LANGSAE EDITING: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2601.04768"
          },
          {
            "title": "LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering",
            "url": "https://arxiv.org/pdf/2604.03532"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search revealed:\n\nLangSAE Editing is a post-hoc sparse autoencoder trained on pooled embeddings that enables controllable removal of language-identity signal directly in vector space. \n\nThe research addresses how multilingual embeddings encode language identity alongside semantics, where this language signal can inflate similarity for same-language pairs and crowd out relevant evidence written in other languages in dense retrieval scenarios.\n\nThe method identifies language-associated latent units using cross-language activation statistics, suppresses these units at inference time, and reconstructs embeddings in the original dimensionality, making it compatible with existing vector databases without retraining the base encoder or re-encoding raw text.\n\nExperiments across multiple languages show consistent improvements in ranking quality and cross-language coverage, with especially strong gains for script-distinct languages.\n\nThe paper (arXiv:2601.04768) was submitted on January 8, 2026, and is authored by Dongjun Kim, Jeongho Yoon, Chanjun Park, and Heuiseok Lim from Korea University and Soongsil University."
    ],
    "durationSeconds": 4.724938634999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "56e06a0c-737a-47cc-9bd7-3ac0dc6c35a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-19T18:49:53.521Z_

<details><summary>↩ Tool result · `toolu_01CCosL364dHRqiE4p5eeoPt`</summary>

```text
Web search results for query: ""SAE" "cross-lingual" "knowledge editing" OR "model editing" 2026 features multilingual propagation"

Links: [{"title":"Cross-Lingual Knowledge Editing in Large Language Models","url":"https://arxiv.org/pdf/2309.08952"},{"title":"MKE-PLLM: A benchmark for multilingual knowledge editing on pretrained large language model - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231225016510"},{"title":"Cross-Lingual Knowledge Editing in Large Language Models","url":"https://arxiv.org/html/2309.08952v2"},{"title":"Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs","url":"https://arxiv.org/pdf/2502.14645"},{"title":"Breaking Boundaries: Investigating the Effects of Model Editing on   Cross-linguistic Performance","url":"https://arxiv.org/pdf/2406.11139"},{"title":"MPN: Leveraging Multilingual Patch Neuron for Cross-lingual Model   Editing","url":"https://arxiv.org/pdf/2401.03190"}]

I found relevant research on cross-lingual knowledge editing and model editing. Here are the key findings:

## Cross-Lingual Knowledge Editing Research

Research conducts English editing on various knowledge editing methods and evaluates their performance in Chinese and vice versa, including evaluation across reliability, generality, locality and portability aspects.

Experimental results show that language modeling gaps across different languages influence knowledge editing efficiency, existing methods struggle to transfer edited knowledge from one language to another in multilingual LLMs, and editing in one language affects model performance on unrelated examples in other languages, resulting in low locality.

## Recent Advances in Multilingual Propagation

When editing responses like "the Conservative Party" to "the Labor Party" in English, this update does not propagate to the Chinese version, making cross-lingual knowledge synchronization crucial to ensure changes made in the source language are correctly applied to target languages.

Research revealed that there is minimal correlation between pre-training language resources and edit success, cross-lingual transference of edits among genealogically proximate languages, and the pivotal role of knowledge types in multilingual editing outcomes.

## 2026 Research

A benchmark study on multilingual knowledge editing for pretrained large language models appeared in Information Processing & Management in 2026.

The search results show active research into enabling knowledge edits to propagate across languages in multilingual language models, addressing a key challenge in maintaining consistency across linguistic variants.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bce48fa3-4f4c-410f-8a61-ed90ab395483",
  "isSidechain": false,
  "promptId": "337860c3-19bc-47e7-8a4b-15fad24e9187",
  "type": "user",
  "uuid": "1a41c267-7a58-4a39-aa00-c60ef43c0206",
  "toolUseResult": {
    "query": "\"SAE\" \"cross-lingual\" \"knowledge editing\" OR \"model editing\" 2026 features multilingual propagation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Bv2Bx3zhK2y914xNVp6kKC",
        "content": [
          {
            "title": "Cross-Lingual Knowledge Editing in Large Language Models",
            "url": "https://arxiv.org/pdf/2309.08952"
          },
          {
            "title": "MKE-PLLM: A benchmark for multilingual knowledge editing on pretrained large language model - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0925231225016510"
          },
          {
            "title": "Cross-Lingual Knowledge Editing in Large Language Models",
            "url": "https://arxiv.org/html/2309.08952v2"
          },
          {
            "title": "Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs",
            "url": "https://arxiv.org/pdf/2502.14645"
          },
          {
            "title": "Breaking Boundaries: Investigating the Effects of Model Editing on   Cross-linguistic Performance",
            "url": "https://arxiv.org/pdf/2406.11139"
          },
          {
            "title": "MPN: Leveraging Multilingual Patch Neuron for Cross-lingual Model   Editing",
            "url": "https://arxiv.org/pdf/2401.03190"
          }
        ]
      },
      "I found relevant research on cross-lingual knowledge editing and model editing. Here are the key findings:\n\n## Cross-Lingual Knowledge Editing Research\n\nResearch conducts English editing on various knowledge editing methods and evaluates their performance in Chinese and vice versa, including evaluation across reliability, generality, locality and portability aspects.\n\nExperimental results show that language modeling gaps across different languages influence knowledge editing efficiency, existing methods struggle to transfer edited knowledge from one language to another in multilingual LLMs, and editing in one language affects model performance on unrelated examples in other languages, resulting in low locality.\n\n## Recent Advances in Multilingual Propagation\n\nWhen editing responses like \"the Conservative Party\" to \"the Labor Party\" in English, this update does not propagate to the Chinese version, making cross-lingual knowledge synchronization crucial to ensure changes made in the source language are correctly applied to target languages.\n\nResearch revealed that there is minimal correlation between pre-training language resources and edit success, cross-lingual transference of edits among genealogically proximate languages, and the pivotal role of knowledge types in multilingual editing outcomes.\n\n## 2026 Research\n\nA benchmark study on multilingual knowledge editing for pretrained large language models appeared in Information Processing & Management in 2026.\n\nThe search results show active research into enabling knowledge edits to propagate across languages in multilingual language models, addressing a key challenge in maintaining consistency across linguistic variants."
    ],
    "durationSeconds": 7.423033404999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bce48fa3-4f4c-410f-8a61-ed90ab395483",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T18:49:57.266Z_

<details><summary>↩ Tool result · `toolu_019oue1z74pm36q4pwBMoADk`</summary>

```text
Web search results for query: "Bi-ZsRE portability EM cross-lingual knowledge editing all methods near zero"

Links: [{"title":"[Literature Review] Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs","url":"https://www.themoonlight.io/en/review/edit-once-update-everywhere-a-simple-framework-for-cross-lingual-knowledge-synchronization-in-llms"},{"title":"Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs","url":"https://arxiv.org/html/2502.14645"},{"title":"Cross-Lingual Knowledge Editing in Large Language Models","url":"https://arxiv.org/html/2309.08952v2"},{"title":"Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs","url":"https://arxiv.org/pdf/2502.14645"},{"title":"GitHub - krystalan/Bi_ZsRE: ACL 2024 main: Cross-Lingual Knowledge Editing in Large Language Models · GitHub","url":"https://github.com/krystalan/Bi_ZsRE"},{"title":"(PDF) Cross-Lingual Knowledge Editing in Large Language Models","url":"https://www.researchgate.net/publication/373953974_Cross-Lingual_Knowledge_Editing_in_Large_Language_Models"},{"title":"Cross-Lingual Knowledge Editing in Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/384207128_Cross-Lingual_Knowledge_Editing_in_Large_Language_Models"},{"title":"Multilingual Knowledge Editing with Language-Agnostic Factual Neurons","url":"https://arxiv.org/html/2406.16416"},{"title":"BMIKE-53: Investigating Cross-Lingual Knowledge Editing with In-Context Learning","url":"https://arxiv.org/html/2406.17764v1"}]

Based on the search results, I found information related to your query about Bi-ZsRE portability, EM, and cross-lingual knowledge editing methods:

Bi-ZsRE is a large-scale cross-lingual synthetic dataset created by translating ZsRE from English to Chinese, where English editing is conducted on various knowledge editing methods covering different paradigms and their performance is evaluated in Chinese, and vice versa.

The evaluation of cross-lingual knowledge editing includes four aspects: reliability, generality, locality, and portability.

Regarding cross-lingual portability performance, the state-of-the-art method IKE demonstrated significant limitations on the Bi-ZsRE benchmark, achieving merely a 73.33 average score when editing in English. This suggests that many existing methods struggle with portability in cross-lingual scenarios.

Parameter-based methods struggle with cross-lingual generalization, while instruction-tuned methods perform more robustly. This indicates that the portability of knowledge editing methods varies significantly depending on the method type used.

The search results show that X-KDE (Cross-Lingual Knowledge Democracy Edit) significantly enhances cross-lingual performance, achieving an average improvement of +8.19%. This suggests that while some newer methods show improvements, the baseline performance on cross-lingual portability remains challenging for most existing methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee0f2296-7ad6-45ce-9a12-8035ccd87272",
  "isSidechain": false,
  "promptId": "337860c3-19bc-47e7-8a4b-15fad24e9187",
  "type": "user",
  "uuid": "873069c7-2e33-44de-8383-4003f0e36658",
  "toolUseResult": {
    "query": "Bi-ZsRE portability EM cross-lingual knowledge editing all methods near zero",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BScd9BcZnxaNAf9ap4jofS",
        "content": [
          {
            "title": "[Literature Review] Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs",
            "url": "https://www.themoonlight.io/en/review/edit-once-update-everywhere-a-simple-framework-for-cross-lingual-knowledge-synchronization-in-llms"
          },
          {
            "title": "Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs",
            "url": "https://arxiv.org/html/2502.14645"
          },
          {
            "title": "Cross-Lingual Knowledge Editing in Large Language Models",
            "url": "https://arxiv.org/html/2309.08952v2"
          },
          {
            "title": "Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs",
            "url": "https://arxiv.org/pdf/2502.14645"
          },
          {
            "title": "GitHub - krystalan/Bi_ZsRE: ACL 2024 main: Cross-Lingual Knowledge Editing in Large Language Models · GitHub",
            "url": "https://github.com/krystalan/Bi_ZsRE"
          },
          {
            "title": "(PDF) Cross-Lingual Knowledge Editing in Large Language Models",
            "url": "https://www.researchgate.net/publication/373953974_Cross-Lingual_Knowledge_Editing_in_Large_Language_Models"
          },
          {
            "title": "Cross-Lingual Knowledge Editing in Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/384207128_Cross-Lingual_Knowledge_Editing_in_Large_Language_Models"
          },
          {
            "title": "Multilingual Knowledge Editing with Language-Agnostic Factual Neurons",
            "url": "https://arxiv.org/html/2406.16416"
          },
          {
            "title": "BMIKE-53: Investigating Cross-Lingual Knowledge Editing with In-Context Learning",
            "url": "https://arxiv.org/html/2406.17764v1"
          }
        ]
      },
      "Based on the search results, I found information related to your query about Bi-ZsRE portability, EM, and cross-lingual knowledge editing methods:\n\nBi-ZsRE is a large-scale cross-lingual synthetic dataset created by translating ZsRE from English to Chinese, where English editing is conducted on various knowledge editing methods covering different paradigms and their performance is evaluated in Chinese, and vice versa.\n\nThe evaluation of cross-lingual knowledge editing includes four aspects: reliability, generality, locality, and portability.\n\nRegarding cross-lingual portability performance, the state-of-the-art method IKE demonstrated significant limitations on the Bi-ZsRE benchmark, achieving merely a 73.33 average score when editing in English. This suggests that many existing methods struggle with portability in cross-lingual scenarios.\n\nParameter-based methods struggle with cross-lingual generalization, while instruction-tuned methods perform more robustly. This indicates that the portability of knowledge editing methods varies significantly depending on the method type used.\n\nThe search results show that X-KDE (Cross-Lingual Knowledge Democracy Edit) significantly enhances cross-lingual performance, achieving an average improvement of +8.19%. This suggests that while some newer methods show improvements, the baseline performance on cross-lingual portability remains challenging for most existing methods."
    ],
    "durationSeconds": 9.308829698000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ee0f2296-7ad6-45ce-9a12-8035ccd87272",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-19T18:51:14.238Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the field. Let me synthesize my findings and produce the evaluation.

Let me organize what I've found:

### Key Verified Facts:
1. **LU-LAFNs (COLING 2025)**: Real paper, identifies language-agnostic factual neurons, achieves 77.87 avg on Bi-ZsRE with bloomz-7b1-mt. The universal portability bottleneck (all methods EM < 10) is a real finding.

2. **FeatureEdit / The Knowledge Microscope (ACL 2025, arXiv:2502.12483)**: Real paper, demonstrates SAE features outperform neurons for knowledge erasure on PrivacyParaRel. 

3. **Mondal et al. (NAACL 2025 InsightsNLP)**: Real paper, shows neuron-level language-specific interventions don't facilitate cross-lingual transfer.

4. **LangSAE (arXiv:2601.04768, Jan 2026)**: Real paper, removes language identity from embeddings using SAE feature suppression, improves multilingual retrieval.

5. **Chou et al. (arXiv:2507.13410)**: Real paper, 90% language steering with single SAE feature.

The pattern emerging is that while SAE features excel at privacy-focused knowledge erasure, they're not necessarily the solution for factual editing or enabling cross-lingual knowledge propagation—those remain distinct challenges with their own constraints.

Looking at more recent work, there's a growing debate about whether SAEs are primarily useful for discovery versus actual intervention. Some papers argue output-score filtering can significantly amplify steering effectiveness, while others question whether SAE features are truly atomic units or just artifacts of the decomposition method. The latest approaches are exploring sparse transcoders for continuous model editing across different architectures, and there's emerging work on benchmarking these capabilities systematically.

What's striking is that despite all this activity around SAEs and knowledge editing, I haven't found anything that actually combines SAE feature decomposition with cross-lingual editing. The existing work either stays within one language, focuses on removing language identity rather than editing knowledge, or uses different architectural approaches entirely. So this gap does seem like a genuine opportunity.

Now I'm thinking through whether this idea is actually non-trivial—could you just apply the same edit vector across languages separately, or use something simpler like PCA-based projection instead of SAE features? based or linear probe-based language component removal) instead of the full SAE decomposition? If language-specific subspaces are linearly separable, a simple orthogonal projection might work without needing SAEs at all.
- LangEdit already uses null-space projection for multilingual editing. AlphaEdit uses null-space constraints. These are simpler approaches to the same problem of separating language and factual components.

The key question is: does the SAE approach provide something fundamentally different from simpler linear projection methods? The proposal argues that neuron-level decomposition is too coarse, but the alternative isn't just SAE features vs. neurons — it's also SAE features vs. simpler subspace methods.

**Premise Assumption Check:**
1. **Core assumption: polysemantic neurons entangle factual structure with language identity, causing the portability bottleneck.** This is plausible but unverified. The LU-LAFNs paper's observation that all methods achieve near-zero portability EM could have other explanations — maybe the portability metric itself is measuring reasoning chains that editing can't improve, as the LU-LAFNs authors themselves suggest.

2. **Assumption: SAE features are sufficiently monosemantic to cleanly separate language-specific and factual components.** Leask et al. (ICLR 2025) directly challenges this — features aren't atomic. The proposal acknowledges this but the response (continuous weighting) doesn't fully address whether the decomposition is clean enough to help.

3. **Assumption: the FCE metric can reliably identify which features matter for factual recall.** This is a novel metric proposed in the paper, and whether point-biserial correlation actually maps to the right features through the full ablation pipeline is untested.

4. **Assumption: the portability bottleneck is addressable at the representation level at all.** It could stem from something deeper — maybe the issue isn't in how facts are encoded but in how the model reasons across languages fundamentally.

The novelty here is applying SAE feature decomposition to cross-lingual knowledge editing, which hasn't been done before. But it's largely combining two well-studied areas rather than introducing fundamentally new techniques — the adaptive soft projection with FCE is incremental, the output-score filtering comes from prior work, and the activation-probability contrasts are from existing SAE methods. The real contribution is in the specific combination rather than individual components.

Cross-lingual portability is definitely a recognized problem worth solving, and if this approach works it could be valuable for maintaining multilingual models. But there's substantial uncertainty about whether it actually will.

The core hypothesis that polysemantic entanglement causes portability failures might be incorrect, and even if it's right, the improvements could be modest — moving from around 5% to maybe 15-20% EM wouldn't be transformative. The related work section is genuinely strong though, covering all the relevant tiers, adversarial approaches, rebuttals, and proper caveats about domain differences.

This is a solid "combine two emerging threads" proposal with a real gap and solid motivation, but the novelty sits at the level of thoughtful combination rather than fundamental breakthrough.

The main question is whether SAE decomposition actually provides meaningful advantages over simpler subspace projection methods — the proposal doesn't make a convincing case for why a linear subspace approach applied to language components wouldn't achieve similar results. The ablation design (comparing SAE features directly against neurons) is genuinely valuable and adds credibility to the experimental plan.

I should be careful not to mistake a well-written proposal with solid experimental design for a fundamentally strong idea. Using SAE features instead of neurons for cross-lingual editing is the natural next step given the existing literature — most researchers familiar with FeatureEdit and LU-LAFNs would probably identify this as the obvious direction to explore.

Wait, I'm noticing the venue is CoRL 2026, which is the Conference on Robot Learning. This is a purely NLP/interpretability paper about cross-lingual knowledge editing, which has essentially zero fit for a robotics venue. The rubric asks about CoRL acceptance probability, and that's a fundamental mismatch regardless of paper quality. Let me reconsider whether CoRL was actually the intended venue or if this is a placeholder. There's a clear mismatch here—the evaluation framework is entirely focused on NLP/CL impact, but the stated venue is CoRL 2026, which typically refers to Conference on Robot Learning. I should evaluate the paper's merit for an appropriate NLP venue and flag this inconsistency, then provide a probability estimate based on that context rather than the stated venue.

Looking at the proposal itself: the novelty is moderate since it combines existing techniques in a natural progression, though the specific components like the FCE metric and adaptive projection show some incremental innovation. The significance is also moderate—it tackles a real problem in cross-lingual knowledge editing, but the actual impact hinges on whether the core hypothesis holds and whether improvements are meaningful enough for the field.

The related work section is particularly strong, with comprehensive coverage across multiple research tiers and thoughtful engagement with competing approaches. Given all this, I'd estimate the probability of acceptance around 25-35%, with 30% as the midpoint. The work is solid and well-positioned, but it's essentially the obvious next step rather than a surprising leap forward, and there's real uncertainty about whether the hypothesis is correct or if simpler alternatives might work just as well.

Now I'm reconsidering the venue — if this is actually targeting CoRL 2026, the probability drops to nearly zero since it's completely out of scope. But the rubric mentions NLP/CL, so I suspect there's a venue mismatch. For an appropriate NLP venue like ACL or EMNLP, I'd estimate 25-35%, around 28-30%. The novelty is the real constraint here — it's a natural combination with some genuine gaps and thoughtful design choices, but the significance remains uncertain since we don't know if the approach actually works or if the gains would be meaningful.

The core limitation is that the central idea — using SAE features instead of neurons for cross-lingual editing — while untested, feels like the obvious next step rather than a surprising insight. That caps how exciting this can be, so I'm settling on 25-32%, with a midpoint around 28%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "873069c7-2e33-44de-8383-4003f0e36658",
  "isSidechain": false,
  "requestId": "req_011CbCRr9RCuXEqauaFQahv9",
  "type": "assistant",
  "uuid": "45bfb9ba-b12e-4a05-b497-db9e57dc6a29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxNXLtFzWv4dY3oz66tdCy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 32053,
      "output_tokens": 8096,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8096,
          "cache_read_input_tokens": 32053,
          "cache_creation_input_tokens": 2373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2373
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

_source line 48 · 2026-05-19T18:52:53.577Z_

Now I have comprehensive field understanding. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- LU-LAFNs (COLING 2025, arXiv:2406.16416): 最直接的 prior work。通过跨语言激活频率交集识别 language-agnostic factual neurons (LAFNs)，在 Bi-ZsRE 上 bloomz-7b1-mt 达到 77.87 avg。关键发现：67.9% 的 neurons 被标记为 LAFNs（极粗粒度），且**所有方法**在 portability EM 上均 < 10。作者自己承认这是普遍难题而非方法特定失败。
- FeatureEdit / The Knowledge Microscope (ACL 2025, arXiv:2502.12483): 首个基于 SAE feature 的模型编辑方法。在 PrivacyParaRel 隐私知识擦除任务上证明 features 优于 neurons（reliability ~0.80 vs ~0.65, generalization ~0.70 vs ~0.25）。但任务是隐私擦除而非事实编辑，模型是 Gemma-2，非跨语言场景。
- CLM-Bench (arXiv:2601.17397, Jan 2026): 提供了中英编辑向量近乎正交的几何证据，解释了 ROME/MEMIT 跨语言失败（~20% reliability）。
- Mondal et al. (NAACL 2025 InsightsNLP, arXiv:2503.17456): 独立证据表明 neuron-level language-specific interventions 对跨语言迁移无效（XNLI/XQuAD），支持"neuron 粒度不够"的论点。
- LangSAE Editing (arXiv:2601.04768, Jan 2026): 用 SAE feature suppression 移除 language identity，在多语言检索上 +21.9% nDCG@20。但目标是检索而非知识编辑。
- Chou et al. (arXiv:2507.13410, Jul 2025): 通过修改单个 SAE feature 在 Gemma-2B/9B 上实现高达 90% 的语言转向成功率，证明 SAE-based language manipulation 的可行性。
- Peng et al. (arXiv:2506.23845): 论证 SAE 适合 concept discovery 而非 acting on known concepts，SAE steering 不如 prompting/fine-tuning。
- Arad et al. (EMNLP 2025, arXiv:2505.20063): 反驳 Peng et al.，通过 output-score filtering 实现 SAE steering 2-3× 提升，匹配 supervised methods。
- Leask et al. (ICLR 2025, arXiv:2502.04878): 证明 SAE features 非 atomic/canonical units，大 SAE 的 latents 可分解为小 SAE latents 的组合。建议按任务需要选择 dictionary size。
- SCAN (arXiv:2603.15226, Mar 2026): 用 sparse transcoders 做 lifelong editing（Qwen3/Llama3.1），但目标是 sequential stability 而非跨语言迁移。
- X-KDE (ACL 2025 Findings, arXiv:2502.14645): 用 instruction tuning + preference optimization 做跨语言知识同步，+8.19% avg improvement。
- LangEdit (ACL 2025 Findings, arXiv:2506.10800): 用 null-space projection 做多语言 sequential editing。
- AlphaEdit (ICLR 2025): 用 null-space constraints 做知识编辑。
- Merging Methods for MKE (arXiv:2605.13919, May 2026): 用 vector merging + shared covariance 做 12 语言编辑，但没有 representation-level decomposition。
- SAE-LAPE/LangFIR (arXiv:2604.03532, ACL 2025 arXiv:2505.05111): 用 activation probability contrasts 发现 sparse language-specific features。

- **调研总结**: 跨语言知识编辑是一个活跃的研究方向，2025-2026 年密集出现了多种方法（LU-LAFNs、X-KDE、LangEdit、AlphaEdit、Merging Methods）。与此并行，SAE-based 方法在知识擦除 (FeatureEdit)、语言转向 (Chou et al.)、语言 identity 移除 (LangSAE) 等任务上已证明有效。但**确实没有工作将 SAE feature decomposition 直接应用于跨语言知识编辑**——这个 gap 是真实存在的。Proposal 处于两条成熟研究线（跨语言编辑 + SAE intervention）的交汇点，是一个"natural next step"型组合创新。

【Trivial Alternative 检验】:
存在至少两个更简单的 alternative 需要考虑：

1. **线性子空间投影（非 SAE）**: LangEdit 已经使用 null-space projection 处理多语言编辑，AlphaEdit 也用了 null-space constraints。如果语言特定分量和事实分量在 residual stream 中是线性可分的（这本身是一个合理的假设，CLM-Bench 的正交性发现暗示了这一点），那么一个简单的 PCA-based 或 linear probe-based 语言分量移除（不需要 SAE）可能就够了。Proposal 没有解释为什么 SAE 提供的非线性稀疏分解比线性投影本质上更好。

2. **多语言并行编辑**: 直接在每种目标语言中独立执行编辑（即对每种语言分别生成 edit vector 并应用），虽然 compute 成本更高但避免了跨语言迁移问题。X-KDE 的 instruction tuning 方法本质上也是绕过了 representation-level 分解。

**增量价值所在**: Proposal 的增量价值在于：(a) 如果 polysemantic entanglement 假说正确，线性方法确实无法处理非线性的 factual-language 纠缠；(b) SAE 的 ~64K monosemantic features 提供了 neurons (~14K) 无法达到的粒度。但这两个前提都未经验证——(a) 是核心假设本身，(b) 在 Leask et al. 的 non-atomicity 发现下有所减弱。

【前提假设检验】:
核心 claim 的逻辑链条中，有以下未验证的关键假设：

1. **"Portability 瓶颈是由 polysemantic entanglement 造成的"** —— 这是整个工作的核心假设，但完全未经验证。LU-LAFNs 作者自己将低 portability 归因于"the difficulty of measuring reasoning without a reasoning process"，即 portability metric 本身可能测量的是推理能力而非事实迁移。如果瓶颈不是 representation-level 的（而是 decoding/reasoning-level 的），那么无论多精细的 representation 分解都无法解决。

2. **"SAE features 能对 factual 和 language-specific 分量做比 neurons 更干净的分离"** —— Leask et al. (ICLR 2025) 已证明 SAE features 不是 atomic canonical units。虽然 proposal 用 continuous weighting 来 accommodate，但这本质上是在承认分离不干净的前提下做 soft mitigation，削弱了"finer granularity = cleaner separation"的核心论点。

3. **"FCE metric 能可靠识别 factual-language 纠缠程度"** —— FCE 是 ablation-based 的（去掉 feature → 测 factual recall 变化），但 ablation 只测量 necessary condition（feature 是否 necessary for recall），不测量 sufficiency。一个 feature 可能对 factual recall 不是 necessary（因为有冗余编码）但仍然 encode factual information。这可能导致高估"safe to remove"的 language-specific features 的数量。

4. **"FeatureEdit 在知识擦除上的优势能迁移到跨语言事实编辑"** —— Proposal 自己承认了这个 gap，但整个工作的 motivation 部分仍然大量依赖 FeatureEdit 的结果作为"features > neurons"的证据。擦除和编辑是不同操作（一个是移除信息，一个是替换信息 + 保持结构），迁移性未知。

其中第 1 点是最关键的——如果 portability bottleneck 的原因不是 representation entanglement 而是更深层的 reasoning limitation，整个技术路线就失去了根基。

【3 维度打分】:

1. **Novelty: 中** — 
   Gap 确实存在：搜索确认无工作将 SAE feature decomposition 应用于跨语言知识编辑。但这本质上是一个 "combine A (SAE features, well-studied) with B (cross-lingual editing, well-studied)" 型创新。对熟悉 FeatureEdit (ACL 2025) + LU-LAFNs (COLING 2025) + LangSAE (2026) 的研究者来说，"用 SAE features 代替 neurons 做跨语言编辑"是相当自然的 next step——不是"为什么没人想到"，而是"时间问题"。
   
   具体技术贡献上：activation-probability contrasts 来自 SAE-LAPE；output-score filtering 来自 Arad et al.；soft projection 而非 binary zeroing 的 insight 来自 Farrell et al.。Proposal 自己发明的核心技术只有 FCE metric 和 adaptive λ-projection 机制，这些是 solid 但 incremental 的方法贡献。
   
   如果核心发现是 positive（SAE features 确实提升了 portability），审稿人的反应更可能是 "makes sense, this is what I'd expect given FeatureEdit + LangSAE results" 而非 "surprising"。如果是 negative（SAE features 也无法提升 portability），这会更 surprising 也更有诊断价值——但 proposal 将此定位为 fallback 而非主打结论。

2. **Significance: 中** — 
   正面：跨语言知识编辑的 portability bottleneck 是一个被社区广泛认可的真实问题（survey arXiv:2505.14393 将其列为 key challenge）。如果能突破 EM < 10 的 universal ceiling，影响力确实显著。
   
   限制因素：(a) 即使 SAE decomposition 有帮助，从 EM ~5 提升到 EM ~15-20 仍然是相当 modest 的绝对改进，可能不足以让人感到"paradigm shift"；(b) 依赖 pre-trained SAEs（Qwen-Scope, Llama Scope），方法的通用性受限于 SAE 的可用性；(c) 目前的 SOTA 模型越来越强大，knowledge editing 这个范式本身面临来自 RAG、continual pretraining 等替代方案的竞争——如果 editing 范式本身在实践中被弱化，这条线的长期价值有限。
   
   此外，结果的可推广性取决于 polysemantic entanglement 假说的正确性，如果假说错误，方法就缺乏 principled 的理论基础。

3. **Related Work: 强** — 
   这是 proposal 最强的维度。四层分类（direct multilingual editing → neuron-level → SAE-based → SAE skepticism/counter-evidence）结构清晰。对每篇关键工作的描述经我搜索验证均准确——包括 FeatureEdit 的任务域限制（privacy erasure not factual editing）、Peng et al. vs Arad et al. 的论辩、Leask et al. 的 non-canonicality 挑战及其 pragmatic recommendation、Farrell et al. 的 binary zeroing 失败。
   
   特别值得肯定的是：(a) 对 adversarial work 的诚实对待和 principled engagement（多数 proposal 会回避 Peng et al. 和 Leask et al.）；(b) 对 FeatureEdit 结果的审慎引用（明确标注 domain mismatch）；(c) 对 Mondal et al. 的引用作为独立支持证据。References 经搜索验证均真实存在且描述准确。
   
   唯一的小缺口是未讨论 null-space projection methods (AlphaEdit, LangEdit) 作为更简单的 language component removal baseline——这正是 Trivial Alternative 检验中暴露的问题。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
Novelty（中）是主要的上界限制因素——这是一个"自然的下一步"组合创新，核心 insight（用 SAE features 代替 neurons）对领域内研究者来说不 surprising。Related Work（强）抬高了下限——proposal 对领域的理解和定位是出色的，降低了"审稿人发现致命遗漏"的风险。Significance（中）居中——问题真实但改进空间的绝对值可能有限。

核心假设（polysemantic entanglement 是 portability 瓶颈的原因）未经验证且存在 plausible alternative explanation（portability 测的是 reasoning 而非 representation），这构成了 idea 层面的实质风险——如果这个假设错误，即使实验执行完美，审稿人也会认为整个 framing 有问题。Trivial alternative（线性子空间投影）的威胁也降低了估值——如果一个简单的 PCA-based 语言分量移除达到类似效果，SAE 的复杂度就难以 justify。

Dual-outcome 设计（negative result 也有诊断价值）是合理的 hedge，但在竞争激烈的 top venue 中，以 negative result 为主的 paper 中稿概率会显著低于 positive result paper。

**注意**: Proposal 目标投稿 CoRL 2026（Conference on Robot Learning）。这是一个纯 NLP/mechanistic interpretability 工作，与 CoRL 的 robotics scope 完全不匹配。如果确实投稿 CoRL，中稿概率实际上接近 0%。上述 22-33% 的估计是假设投稿至合适的 NLP 会议（如 ACL/EMNLP/NAACL 2026）。

【主要风险】: 
1. **核心假设可能为假**: Portability bottleneck 的真正原因可能不是 polysemantic entanglement，而是 portability metric 测量的是 reasoning ability（LU-LAFNs 作者自己的解释）。如果如此，任何 representation-level decomposition（无论多精细）都无法改善 portability，整个技术路线的 framing 将被审稿人质疑。
2. **Trivial alternative 未被排除**: Proposal 没有论证为什么 SAE-based decomposition 比更简单的线性子空间投影（类似 AlphaEdit/LangEdit 的 null-space approach 但针对 language component）本质上更优。审稿人可能要求一个"linear projection baseline"并发现 SAE 的增量收益不 justify 其复杂度。
```

Sources:
- [LU-LAFNs: Multilingual Knowledge Editing with Language-Agnostic Factual Neurons](https://aclanthology.org/2025.coling-main.385/)
- [The Knowledge Microscope: Features as Better Analytical Lenses than Neurons](https://arxiv.org/abs/2502.12483)
- [CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment](https://arxiv.org/pdf/2601.17397)
- [Language-Specific Neurons Do Not Facilitate Cross-Lingual Transfer](https://aclanthology.org/2025.insights-1.6/)
- [LangSAE Editing: Improving Multilingual Information Retrieval](https://arxiv.org/abs/2601.04768)
- [Chou et al.: Causal Language Control via Sparse Feature Steering](https://arxiv.org/abs/2507.13410)
- [Peng et al.: Use SAEs to Discover Unknown Concepts](https://arxiv.org/html/2506.23845v1)
- [Arad et al.: SAEs Are Good for Steering — If You Select the Right Features](https://arxiv.org/abs/2505.20063)
- [Leask et al.: Sparse Autoencoders Do Not Find Canonical Units](https://arxiv.org/abs/2502.04878)
- [SCAN: Sparse Circuit Anchor for Lifelong Editing](https://arxiv.org/pdf/2603.15226)
- [X-KDE: Edit Once, Update Everywhere](https://arxiv.org/pdf/2502.14645)
- [Editing Across Languages: A Survey](https://arxiv.org/html/2505.14393)
- [Emergent Mind: SAE Steering Topic](https://www.emergentmind.com/topics/sparse-autoencoder-steering)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45bfb9ba-b12e-4a05-b497-db9e57dc6a29",
  "isSidechain": false,
  "requestId": "req_011CbCRr9RCuXEqauaFQahv9",
  "type": "assistant",
  "uuid": "a59634a3-71df-4aee-a678-7695f853951a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxNXLtFzWv4dY3oz66tdCy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 32053,
      "output_tokens": 8096,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8096,
          "cache_read_input_tokens": 32053,
          "cache_creation_input_tokens": 2373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2373
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

_source line 49_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation  ## Description Current c…",
  "leafUuid": "a59634a3-71df-4aee-a678-7695f853951a",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE features for cross-lingual knowledge editing",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation  ## Description Current c…",
  "leafUuid": "a59634a3-71df-4aee-a678-7695f853951a",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE features for cross-lingual knowledge editing",
  "sessionId": "eb252af3-dc52-43cd-8394-fe1b586a4d8f"
}
```

---
