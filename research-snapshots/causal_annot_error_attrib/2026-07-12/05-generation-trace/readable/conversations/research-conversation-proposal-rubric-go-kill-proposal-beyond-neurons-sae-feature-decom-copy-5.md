# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Beyond Neurons: SAE Feature Decom

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-1/a4ca4dc5-0609-48fb-b362-0d3efdc3eccd.jsonl`
- **Structured JSON:** [`924da72fdceeec05e038.json`](../../sessions/92/924da72fdceeec05e038.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T21:01:40.100Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T21:01:40.100Z",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation\n\n## Description\nCurrent cross-lingual knowledge editing faces a universal portability bottleneck: not just LU-LAFNs (COLING 2025) but ALL current methods achieve near-zero portability EM (< 10) on Bi-ZsRE, with the LU-LAFNs authors themselves noting 'all methods underperform on this metric without significant difference.' We hypothesize that this bottleneck has a specific causal mechanism: polysemantic neurons entangle factual relational structure with language identity, so any neuron-level editing that removes language components inevitably corrupts relational knowledge needed for portability. This hypothesis is independently supported by Mondal et al. (NAACL 2025 InsightsNLP), who showed that neuron-level language-specific interventions are insufficient for cross-lingual transfer even outside the editing setting.\n\nWe propose SAE-Projected Editing: using pre-trained Qwen-Scope SAEs (64K features on Qwen3-8B) and Llama Scope SAEs (128K features on Llama-3.1-8B) to decompose edit vectors into finer-grained sparse features, classify each as language-specific or language-agnostic via cross-lingual activation-probability contrasts, then apply adaptive soft projection that suppresses language-specific components proportionally to their Factual Causal Effect (FCE) — a per-feature ablation-based metric measuring how much factual recall degrades when the feature is removed. Unlike binary feature zeroing — which Farrell et al. (2024) showed is ineffective — our adaptive λ-projection preserves factual content encoded in partially-entangled features while removing pure language-identity signal.\n\n**Engagement with SAE intervention skepticism:** Peng et al. (arXiv:2506.23845) argue SAEs are better for discovery than intervention; however, Arad et al. (EMNLP 2025) directly rebut this by showing that output-score-based feature selection yields 2–3× improvement in SAE steering, matching supervised methods. The critique applies to naive feature selection, not SAE interventions as a paradigm. We incorporate output-score filtering into our pipeline. Chou et al. (arXiv:2507.13410) provide further feasibility evidence: modifying a single SAE feature achieves up to 90% language steering success on Gemma-2B/9B. Leask et al. (ICLR 2025) show SAE features are not atomic canonical units — larger latents decompose into sub-components. We accommodate this by: (a) treating features as a continuous weighted basis rather than binary switches, (b) using adaptive λ coefficients that handle partial feature overlap, and (c) ablating across SAE widths (16K/64K/128K) to identify task-appropriate granularity per Leask et al.'s recommendation.\n\n**FeatureEdit context note:** The +23% reliability and 2.8× generalization gains from FeatureEdit (ACL 2025) are for knowledge erasure on the PrivacyParaRel privacy dataset using Gemma-2 models, not factual knowledge editing or cross-lingual propagation. We cite these as evidence that features outperform neurons as representation-level intervention units, but do not assume these specific gains transfer to the editing setting.\n\n**FCE metric protocol:** For each of ~64K SAE features, we first compute point-biserial correlation r_pb between feature activation magnitude and binary factual recall success across ≥5,000 multilingual facts (computational cost: ~4 GPU-hours for forward passes). The top ~2K features by |r_pb| undergo full causal ablation: each feature is individually zeroed, and the change in factual recall probability is measured (FCE). This two-stage approach reduces the 64K × 5K evaluation matrix to a tractable 2K × 5K, requiring ~40 GPU-hours. Bootstrap confidence intervals (1000 resamples) provide uncertainty estimates for FCE values. As a validation check, we compute Spearman rank correlation between r_pb and FCE on the 2K features to verify the proxy quality.\n\nKey contributions: (1) First application of SAE feature decomposition to cross-lingual knowledge editing, providing ~5-10× finer granularity than neuron-level LAFN identification; (2) Adaptive soft projection mechanism that explicitly accounts for factual-language feature entanglement via a concrete, causal FCE metric with a two-stage efficient computation protocol; (3) Principled engagement with SAE intervention skepticism (Peng et al., Leask et al.) through output-score filtering, continuous-basis treatment, and multi-width ablation; (4) Testable portability hypothesis: if SAE features do NOT improve portability EM over neuron-level approaches (ablation A3), this falsifies the polysemanticity-entanglement explanation and has standalone diagnostic value; (5) Reconstruction fidelity validation protocol establishing whether SAE round-trip preserves edit vector quality across dictionary sizes.\n\nWe evaluate on CLM-Bench (zh-en), Bi-ZsRE, and MzsRE across 12 languages, targeting improvements over LU-LAFNs (77.87 Bi-ZsRE avg on bloomz-7b1-mt; MzsRE results reported as per-language heatmaps rather than a single average) particularly on portability metrics. Primary baselines: LU-LAFNs, FeatureEdit (adapted cross-lingual), MEMIT, AlphaEdit, M-MEMIT, X-KDE, LangEdit.\n\n**Risk mitigation:** The core risk is that the portability bottleneck is NOT caused by polysemantic entanglement but by a more fundamental limitation (e.g., the portability metric itself measuring reasoning ability that editing cannot improve). We address this through: (a) explicit FCE measurement before editing to quantify the entanglement ceiling, (b) adaptive λ-projection that preserves high-FCE features, (c) reconstruction fidelity go/no-go gate, (d) ablation A3 as a direct falsification test, and (e) relational follow-up evaluation (A2) that provides a complementary portability measure independent of the Bi-ZsRE metric. If SAE features fail to improve portability, the negative result still contributes a rigorous decomposition analysis of what fraction of factual information resides in language-specific vs. language-agnostic features — valuable for the multilingual interpretability community. Fallback: hybrid approach combining SAE-projected editing for low-entanglement facts with LU-LAFNs for high-entanglement cases.\n\n## Core Problem\nCross-lingual knowledge editing methods face two linked failures: (1) raw edit vectors reside in nearly orthogonal, language-specific subspaces (CLM-Bench), and (2) neuron-level approaches like LU-LAFNs that identify language-agnostic neurons achieve high monolingual reliability but suffer catastrophically low portability (26.43% F1, EM < 5) — a failure shared by ALL current methods (all EM < 10 on Bi-ZsRE portability), suggesting a fundamental representation-level bottleneck. We hypothesize that this bottleneck stems from polysemantic neurons entangling factual relational structure with language identity: edits that operate at neuron granularity cannot cleanly separate these components, corrupting relational knowledge during cross-lingual transfer. Can sparse autoencoder feature decomposition — which yields finer-grained, more monosemantic units — provide a cleaner separation that better preserves relational structure, and is this hypothesis even testable given recent challenges to SAE feature canonicality (Leask et al., ICLR 2025)?\n\n## Opportunity\nCLM-Bench (arXiv:2601.17397, Jan 2026) provided geometric evidence that Chinese and English edit vectors are nearly orthogonal, explaining why ROME/MEMIT fail cross-lingually (~20% reliability). LU-LAFNs (COLING 2025) achieved 77.87 avg on Bi-ZsRE by targeting language-agnostic neurons, but its neuron-level approach identifies 67.9% of neurons as LAFNs — an extremely coarse decomposition reflecting neuron polysemanticity — and ALL methods achieve near-zero portability EM (< 10 across the board), which the authors attribute to the difficulty of measuring reasoning without a reasoning process. Crucially, Mondal et al. (NAACL 2025 InsightsNLP) independently showed that neuron-level language-specific interventions are insufficient for cross-lingual transfer on XNLI/XQuAD, reinforcing the case that neuron-level decomposition is fundamentally too coarse.\n\nMeanwhile, FeatureEdit (ACL 2025) demonstrated that SAE features outperform neurons for knowledge erasure on PrivacyParaRel (~0.80 vs ~0.65 reliability, ~0.70 vs ~0.25 generalization on Gemma-2 2B/9B) — though notably this was for privacy-knowledge erasure, not factual editing or cross-lingual propagation, so these gains may not directly transfer. LangSAE (arXiv:2601.04768) proved SAE-based language identity removal improves cross-lingual retrieval by +21.9% nDCG@20. Chou et al. (arXiv:2507.13410) achieved up to 90% language steering success by modifying a single SAE feature on Gemma-2B/9B, demonstrating that SAE-based language manipulation is feasible and precise.\n\nHowever, recent work challenges SAE interventions: Peng et al. (arXiv:2506.23845) argue SAEs are better for concept discovery than acting on known concepts, finding SAE-based steering underperforms prompting/fine-tuning. Critically, Arad et al. (EMNLP 2025) rebut this: proper feature selection via output-score filtering yields 2–3× improvement in SAE steering, matching supervised methods — the issue was feature selection, not SAE interventions per se. Leask et al. (ICLR 2025) show SAE features aren't canonical atomic units — larger latents decompose into combinations — but recommend pragmatic choice of dictionary size suited to task, and our adaptive soft projection naturally accommodates non-atomicity by treating features as a continuous basis rather than binary switches.\n\nThe missing link: no work has combined SAE feature-level decomposition with cross-lingual knowledge editing. SAE features offer ~64K monosemantic units (vs. ~14K polysemantic neurons), enabling more precisely targeted language-component manipulation that may better preserve relational/factual structure — a hypothesis we propose to test directly.\n\n## Related Work / Landscape\nCross-lingual knowledge editing is a recognized open problem: the survey (arXiv:2505.14393) identifies language anisotropy and edit scalability as key challenges. The field is structured in three tiers:\n\n**Tier 1 — Direct multilingual editing baselines:** MEMIT/M-MEMIT apply locate-then-edit across languages (74.86 avg on Bi-ZsRE but ~20% cross-lingual reliability). AlphaEdit (ICLR 2025) uses null-space constraints. Merging Methods for MKE (arXiv:2605.13919, May 2026) explores vector merging with shared covariance for 12-language editing but without representation-level decomposition.\n\n**Tier 2 — Neuron/representation-level multilingual editing:** LU-LAFNs (COLING 2025, arXiv:2406.16416) is the closest prior work — identifies language-agnostic factual neurons via activation frequency intersection across languages, achieving 77.87 avg on Bi-ZsRE (bloomz-7b1-mt). However, it identifies 67.9% of neurons as LAFNs (extremely coarse), and ALL methods achieve near-zero portability (EM < 10, F1 ~26-36%), which the authors acknowledge as a universal challenge rather than a method-specific failure. Mondal et al. (NAACL 2025 InsightsNLP, arXiv:2503.17456) provide independent evidence that neuron-level language-specific interventions are insufficient for cross-lingual transfer. MEMLA (arXiv:2406.11566) uses neuron masking with LoRA but doesn't leverage monosemantic features. X-KDE (ACL 2025 Findings, arXiv:2502.14645) uses instruction tuning + preference optimization (+8.19% avg improvement). LangEdit (ACL 2025 Findings, arXiv:2506.10800) applies null-space projection for multilingual sequential editing across 6 languages.\n\n**Tier 3 — SAE-based editing and language feature work (our building blocks):** FeatureEdit from 'The Knowledge Microscope' (ACL 2025, arXiv:2502.12483) is the first SAE-feature-based model editing method — uses Gemma Scope JumpReLU SAEs to identify knowledge features and zero out specific weight positions. On the PrivacyParaRel knowledge-erasure benchmark (not factual editing), features achieve ~0.80 reliability (vs. ~0.65 for neurons) and ~0.70 generalization (vs. ~0.25), demonstrating features' advantage for representation-level interventions. However, it is monolingual English-only, targets knowledge erasure rather than cross-lingual propagation, and these gains may not directly transfer to the editing setting. SSPU (EMNLP 2025, arXiv:2505.24428) shows SAE-guided subspace projection via QR decomposition can unlearn knowledge while preserving non-target capabilities. LangSAE (arXiv:2601.04768) removes language identity from embeddings using SAE feature suppression (+21.9% nDCG@20). SAE-LAPE/LangFIR (arXiv:2604.03532) discover sparse language-specific features using activation probability contrasts. SASFT (ICLR 2026) shows SAE-guided fine-tuning preserves targeted knowledge. SpARE (NAACL 2025, arXiv:2410.15999) uses SAE-based representation engineering for knowledge selection steering but not cross-lingually. SCAN (arXiv:2603.15226, Mar 2026) uses sparse transcoders for lifelong editing on Qwen3/Llama3.1 but addresses sequential stability, not cross-lingual transfer. Farrell et al. (arXiv:2410.19278) found that zero ablation of SAE features is ineffective for knowledge unlearning — negative scaling is necessary. Chou et al. (arXiv:2507.13410) achieved up to 90% language steering success by modifying single SAE features on Gemma-2B/9B, providing direct feasibility evidence for SAE-based language manipulation.\n\n**Tier 4 — SAE intervention skepticism and counter-evidence (critical context):** Peng et al. (arXiv:2506.23845) argue SAEs are better for discovering unknown concepts than acting on known ones, finding SAE-based steering underperforms prompting/fine-tuning. However, Arad et al. (EMNLP 2025, arXiv:2505.20063) directly rebut this: by distinguishing 'input features' (capture input patterns) from 'output features' (causally affect model behavior) and filtering by output scores, SAE steering achieves 2–3× improvement, matching supervised methods. The issue was naive feature selection, not SAE interventions as a paradigm. Zhao et al. (arXiv:2505.15038) further show denoising concept vectors via SAE improves steering 4–16%. SAE-SSV (EMNLP 2025, arXiv:2505.16188) achieves high steering success rates using supervised feature selection in sparse spaces. Leask et al. (ICLR 2025, arXiv:2502.04878) demonstrate SAE features are neither atomic nor canonical — meta-SAEs decompose latents into sub-components (e.g., 'Einstein' → 'scientist' + 'Germany' + 'famous person'), and smaller SAEs miss information captured by larger ones. They recommend pragmatic dictionary size selection rather than assuming canonicality. Our approach accommodates this by treating SAE features as a practical continuous basis with adaptive coefficients, not as binary canonical units.\n\n**The gap:** No work combines SAE feature decomposition with cross-lingual knowledge editing. Specifically, no one has (a) used monosemantic SAE features instead of polysemantic neurons to decompose cross-lingual edit vectors, (b) tested whether finer-grained decomposition causally improves portability by preserving relational structure, or (c) engaged with the feature-selection insights from Arad et al. to ensure intervention-effective features are targeted.\n\n## Approach\n**Phase 1: Feature Classification with Output-Score Filtering (Weeks 1-2).** Leverage pre-trained SAEs — Qwen-Scope (64K features, 16× expansion) on Qwen3-8B and Llama Scope (128K features, 32× expansion) on Llama-3.1-8B — to decompose residual-stream activations at editing-critical layers (layers 12-25 for Qwen3-8B based on LU-LAFNs' LAFN distribution peaks). Classify each feature as language-specific, language-agnostic, or factual using activation-probability contrasts across Chinese, English, and 4+ additional languages (following SAE-LAPE/LangFIR methodology). Critically, following Arad et al.'s (EMNLP 2025) insight that input-pattern features and output-causal features rarely co-occur, compute output scores for all features to ensure we target features that causally affect model behavior, not merely correlational activations — this addresses the core criticism of Peng et al. For each language-specific feature f_i, compute its Factual Causal Effect (FCE): ablate f_i and measure the change in correct factual recall probability across a multilingual fact corpus of ≥5,000 facts (drawn from Bi-ZsRE + MzsRE test sets, held out from editing evaluation). FCE(f_i) = |P(correct | f_i active) - P(correct | f_i ablated)|. This produces a per-feature entanglement map. FCE is preferred over mutual information because: (a) it is causal rather than correlational, (b) it avoids the curse-of-dimensionality problems that plague MI estimation with 64K+ features (KSG estimators break down beyond ~10 dimensions), and (c) it is directly interpretable as the factual cost of removing a feature. As a computationally efficient proxy during initial screening, we also compute point-biserial correlation r_pb between feature activation magnitude and binary factual recall success, filtering to the top ~2K candidate features for full FCE ablation (reducing 64K × 5K evaluations to ~2K × 5K).\n\n**Phase 2: SAE-Projected Editing with Adaptive Soft Projection (Weeks 3-5).** For a given ROME/MEMIT edit vector e, decompose it into the SAE feature basis: e ≈ Σ_j α_j d_j (where d_j are SAE decoder directions and α_j are coefficients from the encoder). Following Farrell et al.'s finding that binary zeroing is ineffective and Leask et al.'s evidence that features are not atomic canonical units, we apply adaptive soft projection that treats features as a continuous basis: e_proj = e - Σ_{i ∈ L_spec} λ_i · α_i · d_i, where λ_i ∈ [0, 1] is inversely proportional to FCE(f_i) — features with high factual causal effect are preserved more, pure language-identity features (low FCE, high language specificity) are fully suppressed. This formulation naturally handles Leask et al.'s non-atomicity concern: since features are weighted continuously rather than treated as binary switches, partial overlap between sub-features is accommodated through the λ gradient. The projected vector e_proj is then applied via the standard locate-then-edit pipeline.\n\n**Phase 3: Reconstruction Fidelity Validation (Weeks 3-4, parallel).** Before full-scale editing, validate that SAE round-trip reconstruction preserves edit vector fidelity. Measure: (a) cosine similarity between original and reconstructed edit vectors, (b) monolingual edit success rate with SAE-reconstructed vectors (no language feature removal) vs. original ROME/MEMIT — this isolates reconstruction error from projection effects. If reconstruction degrades edit quality by >5%, investigate top-k sparsity adjustments or layer-specific SAE selection. Following Leask et al.'s recommendation, test multiple SAE widths (16K, 64K, 128K where available) to identify task-appropriate granularity rather than assuming larger is better. Establish a reconstruction quality threshold as a go/no-go gate.\n\n**Phase 4: Evaluation and Ablation (Weeks 5-8).** Evaluate on CLM-Bench (1,010 zh-en pairs), Bi-ZsRE, and MzsRE (12 languages) using Qwen3-8B and Llama-3.1-8B. Primary baselines: LU-LAFNs (77.87/Bi-ZsRE on bloomz-7b1-mt — the SOTA to beat), FeatureEdit (adapted to cross-lingual setting), MEMIT, AlphaEdit, M-MEMIT, X-KDE, LangEdit. Secondary baselines: SCAN, MEMLA. Key ablations: (A1) Full zeroing vs. soft projection — measuring factual content loss, directly testing Farrell et al.'s finding in the cross-lingual setting. (A2) Relational structure preservation: for edited facts, measure whether the model correctly answers relational follow-up questions (e.g., after editing 'capital of X', test 'X is in which continent?') — this directly tests the portability hypothesis. (A3) Feature granularity: SAE features (64K/128K) vs. neuron-level LAFNs (~10K) vs. random subspace projection — if SAE features do not improve portability over neurons, this falsifies our core hypothesis. (A4) λ scheduling: fixed λ vs. FCE-adaptive λ vs. oracle λ (per-fact optimal). (A5) Layer selection: which layers' SAEs are most critical for cross-lingual transfer. (A6) SAE width: 16K vs. 64K vs. 128K features, testing Leask et al.'s prediction that task-appropriate granularity matters more than raw dictionary size. (A7) Output-score filtering (per Arad et al.): restrict projection to high-output-score features vs. all language-classified features.\n\n## Inspiration\nLU-LAFNs' universal portability failure (all methods EM < 10) revealing a fundamental representation-level bottleneck + Mondal et al.'s independent evidence that neuron-level language interventions are insufficient + FeatureEdit's demonstration that SAE features outperform neurons for knowledge erasure + LangSAE proving language features can be surgically suppressed + Chou et al.'s 90% language steering with single SAE features + CLM-Bench's geometric evidence of language-specific subspaces + SSPU's QR-decomposition subspace methodology + Arad et al.'s insight that output-score feature selection rescues SAE interventions + Farrell et al.'s finding that soft scaling outperforms zero ablation\n\n## Key References\n- LU-LAFNs: Multilingual Knowledge Editing with Language-Agnostic Factual Neurons (COLING 2025, arXiv:2406.16416) — PRIMARY BASELINE\n- FeatureEdit / The Knowledge Microscope: Features as Better Analytical Lenses than Neurons (ACL 2025, arXiv:2502.12483) — METHODOLOGICAL PREDECESSOR (knowledge erasure, not editing)\n- CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing (arXiv 2026, arXiv:2601.17397)\n- LangSAE Editing: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal (arXiv 2026, arXiv:2601.04768)\n- LangEdit: Mitigating Negative Interference in Multilingual Sequential Knowledge Editing through Null-Space Constraints (ACL 2025 Findings, arXiv:2506.10800)\n- SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing (arXiv 2026, arXiv:2603.15226)\n- SSPU: Model Unlearning via Sparse Autoencoder Subspace Guided Projections (EMNLP 2025, arXiv:2505.24428)\n- Applying Sparse Autoencoders to Unlearn Knowledge in Language Models (arXiv 2024, arXiv:2410.19278)\n- X-KDE: Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs (ACL 2025 Findings, arXiv:2502.14645)\n- MEMLA: Enhancing Multilingual Knowledge Editing with Neuron-Masked Low-Rank Adaptation (arXiv 2024, arXiv:2406.11566)\n- Editing Across Languages: A Survey of Multilingual Knowledge Editing (arXiv 2025, arXiv:2505.14393)\n- SAE-LAPE: Unveiling Language-Specific Features in Large Language Models via Sparse Autoencoders (ACL 2025, arXiv:2505.05111)\n- LinguaLens: Towards Interpreting Linguistic Mechanisms of Large Language Models via Sparse Auto-Encoder (EMNLP 2025)\n- SASFT: Sparse Autoencoder-guided Supervised Finetuning to Mitigate Unexpected Code-Switching in LLMs (ICLR 2026)\n- AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models (ICLR 2025)\n- SpARE: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering (NAACL 2025, arXiv:2410.15999)\n- LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering (arXiv 2026, arXiv:2604.03532)\n- Merging Methods for Multilingual Knowledge Editing for Large Language Models: An Empirical Odyssey (arXiv 2026, arXiv:2605.13919)\n- SALVE: Sparse Autoencoder-Latent Vector Editing for Mechanistic Control of Neural Networks (arXiv 2025, arXiv:2512.15938)\n- Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models (arXiv 2026, arXiv:2605.11887)\n- Llama Scope: Extracting Millions of Features from Llama-3.1-8B with Sparse Autoencoders (arXiv 2024, arXiv:2410.20526)\n- Language-Specific Neurons: The Key to Multilingual Capabilities in Large Language Models (ACL 2024, arXiv:2402.16438)\n- Peng et al.: Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts (arXiv 2025, arXiv:2506.23845) — ADVERSARIAL: argues SAEs underperform for interventions\n- Leask et al.: Sparse Autoencoders Do Not Find Canonical Units of Analysis (ICLR 2025, arXiv:2502.04878) — ADVERSARIAL: shows features are not atomic/canonical\n- Arad et al.: SAEs Are Good for Steering — If You Select the Right Features (EMNLP 2025, arXiv:2505.20063) — REBUTTAL to Peng et al.: output-score filtering yields 2-3× improvement\n- Mondal et al.: Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer (NAACL 2025 InsightsNLP, arXiv:2503.17456) — SUPPORTS motivation: neuron-level is insufficient\n- Chou et al.: Causal Language Control in Multilingual Transformers via Sparse Feature Steering (arXiv 2025, arXiv:2507.13410) — FEASIBILITY: 90% language steering with single SAE feature\n- Zhao et al.: Denoising Concept Vectors with Sparse Autoencoders for Improved Language Model Steering (arXiv 2025, arXiv:2505.15038) — SAE steering improves 4-16% with denoising\n- SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models (EMNLP 2025, arXiv:2505.16188)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '450-550 (SAE feature classification + FCE ablation analysis ~120h on 1×A100 — increased due to per-feature ablation; reconstruction fidelity validation across SAE widths ~40h; editing experiments across 2 models × 3 benchmarks × 8+ baselines ~250h; ablation studies A1-A7 ~120h; analysis ~40h)', 'timeline': '10-12 weeks', 'estimated_gpu_cost': '$1,125-$1,375 (A100 at ~$2.50/hr; major savings from pre-trained Qwen-Scope and Llama Scope SAEs)'}\n- **human_in_loop**: {'gpu_hours': '400-500', 'timeline': '7-9 weeks', 'claude_api_cost': '$150-$250 (code generation for SAE analysis pipeline, FCE computation, experiment orchestration)', 'estimated_gpu_cost': '$1,000-$1,250'}\n- **auto_research**: {'gpu_hours': '400-500', 'timeline': '5-7 weeks', 'claude_api_cost': '$400-$550 (end-to-end experiment management, hyperparameter sweeps for λ, paper drafting)', 'estimated_gpu_cost': '$1,000-$1,250', 'speed_bottleneck': 'FCE ablation requires sequential per-feature evaluation (mitigated by r_pb pre-screening to ~2K features); sequential editing experiments per model-benchmark pair; CLM-Bench evaluation involves Chinese cultural knowledge judgment requiring human spot-checking'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T21:01:40.110Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T21:01:40.110Z",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd"
}
```

---

## Round 1

52 recorded events

### User

_source line 3 · 2026-05-19T21:01:40.128Z_

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
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "9b12fef4-6694-45d3-a8e8-eea0c3e71768",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T21:01:40.127Z_

```json
{
  "parentUuid": "9b12fef4-6694-45d3-a8e8-eea0c3e71768",
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
  "uuid": "338df71f-268b-4790-b1a0-0b1a4b26bf22",
  "timestamp": "2026-05-19T21:01:40.127Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T21:01:40.127Z_

```json
{
  "parentUuid": "338df71f-268b-4790-b1a0-0b1a4b26bf22",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9fc56dd5-3b9e-47c3-8792-48d25beade74",
  "timestamp": "2026-05-19T21:01:40.127Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
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
  "leafUuid": "9fc56dd5-3b9e-47c3-8792-48d25beade74",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE feature decomposition for cross-lingual knowledge editing",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd"
}
```

---

### Assistant

_source line 8 · 2026-05-19T21:01:56.332Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 submission. Let me first carefully read the proposal, then conduct web searches to understand the current landscape before making my assessment.

Wait - the user says CoRL 2026, but the proposal is about cross-lingual knowledge editing in LLMs, which is more of an NLP/CL topic. CoRL is Conference on Robot Learning. Let me re-read... The system prompt says "CoRL 2026 主会" but the proposal is clearly about NLP/computational linguistics. This might be a mistake in the prompt, or the user might have intended a different venue. 

I'll evaluate the proposal on its merits regardless, but I should note this venue mismatch - the topic is fundamentally about NLP and language models rather than robotics, which is a significant disconnect from CoRL's scope.

Let me set aside the venue question for now and focus on assessing the idea itself. I need to search for recent work in cross-lingual knowledge editing, SAE-based interventions, and the specific papers referenced to understand where this proposal sits in the current landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fc56dd5-3b9e-47c3-8792-48d25beade74",
  "isSidechain": false,
  "requestId": "req_011CbCbtheAKRSnsJPLwTQXF",
  "type": "assistant",
  "uuid": "9f553ddb-d9bf-438f-a32f-61df6fe0e396",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9KXJJmj1DnscZJSrefeKm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8887,
      "cache_read_input_tokens": 13985,
      "output_tokens": 545,
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
          "output_tokens": 545,
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

_source line 9 · 2026-05-19T21:01:56.349Z_

I'll start by conducting the required literature searches to ground my assessment. Let me search for the key topics in this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f553ddb-d9bf-438f-a32f-61df6fe0e396",
  "isSidechain": false,
  "requestId": "req_011CbCbtheAKRSnsJPLwTQXF",
  "type": "assistant",
  "uuid": "0b6b1600-a346-4d40-81e4-f4c4bbe9c7e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9KXJJmj1DnscZJSrefeKm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8887,
      "cache_read_input_tokens": 13985,
      "output_tokens": 545,
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
          "output_tokens": 545,
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

_source line 10 · 2026-05-19T21:01:56.600Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HsZ9Z1TtnvzsfM1BARcU7X`</summary>

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
  "parentUuid": "0b6b1600-a346-4d40-81e4-f4c4bbe9c7e3",
  "isSidechain": false,
  "requestId": "req_011CbCbtheAKRSnsJPLwTQXF",
  "type": "assistant",
  "uuid": "e4ecae21-bb0c-42dd-9638-9079b7160eaa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9KXJJmj1DnscZJSrefeKm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8887,
      "cache_read_input_tokens": 13985,
      "output_tokens": 545,
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
          "output_tokens": 545,
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

_source line 11 · 2026-05-19T21:01:56.607Z_

<details><summary>↩ Tool result · `toolu_01HsZ9Z1TtnvzsfM1BARcU7X`</summary>

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
  "parentUuid": "e4ecae21-bb0c-42dd-9638-9079b7160eaa",
  "isSidechain": false,
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "dcce8db9-1d5c-40e6-9980-8d311b29a308",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "e4ecae21-bb0c-42dd-9638-9079b7160eaa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T21:01:59.120Z_

Now let me conduct the required searches in parallel to understand the landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcce8db9-1d5c-40e6-9980-8d311b29a308",
  "isSidechain": false,
  "requestId": "req_011CbCbuvUcHoNs5uUfuWVpn",
  "type": "assistant",
  "uuid": "6b877ce8-048d-4633-97e7-ba6b86333806",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01392kiLP7vRLxKmf3a82CnA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 22872,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 86,
          "cache_read_input_tokens": 22872,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1071
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

_source line 13 · 2026-05-19T21:01:59.692Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018mZkNN6QS4XwsYe53XU6aD`</summary>

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
  "parentUuid": "6b877ce8-048d-4633-97e7-ba6b86333806",
  "isSidechain": false,
  "requestId": "req_011CbCbuvUcHoNs5uUfuWVpn",
  "type": "assistant",
  "uuid": "e1b9cb19-c29e-4bd6-a22a-7640eea2ff80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01392kiLP7vRLxKmf3a82CnA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 22872,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 86,
          "cache_read_input_tokens": 22872,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1071
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

_source line 14 · 2026-05-19T21:02:05.809Z_

<details><summary>↩ Tool result · `toolu_018mZkNN6QS4XwsYe53XU6aD`</summary>

```text
Web search results for query: "cross-lingual knowledge editing LLMs 2025 2026 survey portability"

Links: [{"title":"(PDF) Cross-Lingual Knowledge Editing in Large Language Models","url":"https://www.researchgate.net/publication/373953974_Cross-Lingual_Knowledge_Editing_in_Large_Language_Models"},{"title":"Cross-Lingual Knowledge Editing in Large Language Models","url":"https://arxiv.org/pdf/2309.08952"},{"title":"Cross-Lingual Knowledge Editing in Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/384207128_Cross-Lingual_Knowledge_Editing_in_Large_Language_Models"},{"title":"Editing Across Languages: A Survey of Multilingual Knowledge Editing","url":"https://arxiv.org/html/2505.14393"},{"title":"Cross-Lingual Knowledge Editing in Large Language Models","url":"https://arxiv.org/html/2309.08952v2"},{"title":"Cross-Lingual Knowledge Editing in Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.627/"},{"title":"Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs","url":"https://arxiv.org/pdf/2502.14645"}]

Based on the search results, here's what I found on cross-lingual knowledge editing in LLMs:

## Recent Survey and Research

Multilingual Knowledge Editing (MKE) is a growing subdomain of model editing focused on ensuring factual edits generalize reliably across languages. Knowledge Editing has been extensively studied in monolingual settings, but remains underexplored in multilingual contexts.

## Comprehensive 2025 Survey

A comprehensive survey was recently published that presents a taxonomy of MKE methods covering parameter-based, memory-based, fine-tuning, and hypernetwork approaches, and identifies persistent challenges such as cross-lingual propagation, language anisotropy, and limited evaluation for low-resource and culturally specific languages.

## Key Findings and Challenges

Results indicate that it remains challenging for multi-lingual LLMs to generalize edited knowledge to other languages. Evaluation of cross-lingual knowledge editing includes four aspects: reliability, generality, locality and portability.

## Recent Methods

A 2026 paper introduces a new approach: Prior methods typically focus on single-language or basic multilingual editing, failing to achieve true cross-linguistic knowledge synchronization, and a state-of-the-art recipe called Cross-Lingual Knowledge Democracy Edit (X-KDE) is designed to propagate knowledge from a dominant language to other languages effectively.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1b9cb19-c29e-4bd6-a22a-7640eea2ff80",
  "isSidechain": false,
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "6ce3c3f2-afff-4de0-a35a-175403066af7",
  "toolUseResult": {
    "query": "cross-lingual knowledge editing LLMs 2025 2026 survey portability",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KDfwfhdw4V3dsYkjdWFaMM",
        "content": [
          {
            "title": "(PDF) Cross-Lingual Knowledge Editing in Large Language Models",
            "url": "https://www.researchgate.net/publication/373953974_Cross-Lingual_Knowledge_Editing_in_Large_Language_Models"
          },
          {
            "title": "Cross-Lingual Knowledge Editing in Large Language Models",
            "url": "https://arxiv.org/pdf/2309.08952"
          },
          {
            "title": "Cross-Lingual Knowledge Editing in Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/384207128_Cross-Lingual_Knowledge_Editing_in_Large_Language_Models"
          },
          {
            "title": "Editing Across Languages: A Survey of Multilingual Knowledge Editing",
            "url": "https://arxiv.org/html/2505.14393"
          },
          {
            "title": "Cross-Lingual Knowledge Editing in Large Language Models",
            "url": "https://arxiv.org/html/2309.08952v2"
          },
          {
            "title": "Cross-Lingual Knowledge Editing in Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.acl-long.627/"
          },
          {
            "title": "Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs",
            "url": "https://arxiv.org/pdf/2502.14645"
          }
        ]
      },
      "Based on the search results, here's what I found on cross-lingual knowledge editing in LLMs:\n\n## Recent Survey and Research\n\nMultilingual Knowledge Editing (MKE) is a growing subdomain of model editing focused on ensuring factual edits generalize reliably across languages. Knowledge Editing has been extensively studied in monolingual settings, but remains underexplored in multilingual contexts.\n\n## Comprehensive 2025 Survey\n\nA comprehensive survey was recently published that presents a taxonomy of MKE methods covering parameter-based, memory-based, fine-tuning, and hypernetwork approaches, and identifies persistent challenges such as cross-lingual propagation, language anisotropy, and limited evaluation for low-resource and culturally specific languages.\n\n## Key Findings and Challenges\n\nResults indicate that it remains challenging for multi-lingual LLMs to generalize edited knowledge to other languages. Evaluation of cross-lingual knowledge editing includes four aspects: reliability, generality, locality and portability.\n\n## Recent Methods\n\nA 2026 paper introduces a new approach: Prior methods typically focus on single-language or basic multilingual editing, failing to achieve true cross-linguistic knowledge synchronization, and a state-of-the-art recipe called Cross-Lingual Knowledge Democracy Edit (X-KDE) is designed to propagate knowledge from a dominant language to other languages effectively."
    ],
    "durationSeconds": 6.111053239999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e1b9cb19-c29e-4bd6-a22a-7640eea2ff80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T21:02:08.516Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CjJBeZCvzFSihNSKj5UST9`</summary>

```json
{
  "query": "LU-LAFNs language-agnostic factual neurons COLING 2025 cross-lingual editing portability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ce3c3f2-afff-4de0-a35a-175403066af7",
  "isSidechain": false,
  "requestId": "req_011CbCbvbKxhTcqHacYEE9yv",
  "type": "assistant",
  "uuid": "6fd908ab-e10a-48f9-8f52-ddbe9ce828cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZRD2ab2sMFoUGuTBMx89n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 23943,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 757,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 23943,
          "cache_creation_input_tokens": 757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 757
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

_source line 16 · 2026-05-19T21:02:14.668Z_

<details><summary>↩ Tool result · `toolu_01CjJBeZCvzFSihNSKj5UST9`</summary>

```text
Web search results for query: "LU-LAFNs language-agnostic factual neurons COLING 2025 cross-lingual editing portability"

Links: [{"title":"Multilingual Knowledge Editing with Language-Agnostic Factual Neurons - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.385/"},{"title":"[2406.16416] Multilingual Knowledge Editing with Language-Agnostic Factual Neurons","url":"https://arxiv.org/abs/2406.16416"},{"title":"Multilingual Knowledge Editing with Language-Agnostic Factual Neurons - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240616416Z/abstract"},{"title":"Multilingual Knowledge Editing with Language-Agnostic Factual Neurons","url":"https://arxiv.org/pdf/2406.16416"},{"title":"Multilingual Knowledge Editing with Language-Agnostic ...","url":"https://aclanthology.org/2025.coling-main.385.pdf"},{"title":"MPN: Leveraging Multilingual Patch Neuron for Cross-lingual Model   Editing","url":"https://arxiv.org/pdf/2401.03190"},{"title":"Language-Specific Neurons Do Not Facilitate Cross-Lingual Transfer - ACL Anthology","url":"https://aclanthology.org/2025.insights-1.6/"},{"title":"Converging to a Lingua Franca: Evolution of Linguistic Regions and Semantics Alignment in Multilingual Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.707/"}]

Based on the search results, I found information about the LU-LAFNs paper. Here's what the research is about:

LU-LAFNs is a method for Locating and Updating Language-Agnostic Factual Neurons to edit multilingual knowledge simultaneously, which avoids knowledge conflicts and improves edit performance.

The key discovery behind this approach is that the same factual knowledge in different languages generally activates a shared set of neurons, which are called language-agnostic factual neurons (LAFNs). These neurons represent the same factual knowledge shared across languages and imply the semantic connections among multilingual knowledge.

Experimental results on Bi-ZsRE and MzsRE benchmarks demonstrate that the method achieves the best edit performance, indicating the effectiveness and importance of modeling the semantic connections among multilingual knowledge.

The paper was published at COLING 2025 (as indicated by the ACL Anthology citation) and addresses the problem of multilingual knowledge editing with a focus on cross-lingual portability through the identification and manipulation of language-agnostic neural structures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fd908ab-e10a-48f9-8f52-ddbe9ce828cd",
  "isSidechain": false,
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "2b20351f-5bb3-4941-a52c-b1eee6f26a8b",
  "toolUseResult": {
    "query": "LU-LAFNs language-agnostic factual neurons COLING 2025 cross-lingual editing portability",
    "results": [
      {
        "tool_use_id": "srvtoolu_019chaXsHbx4XX6XXbzKBUrW",
        "content": [
          {
            "title": "Multilingual Knowledge Editing with Language-Agnostic Factual Neurons - ACL Anthology",
            "url": "https://aclanthology.org/2025.coling-main.385/"
          },
          {
            "title": "[2406.16416] Multilingual Knowledge Editing with Language-Agnostic Factual Neurons",
            "url": "https://arxiv.org/abs/2406.16416"
          },
          {
            "title": "Multilingual Knowledge Editing with Language-Agnostic Factual Neurons - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240616416Z/abstract"
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
            "title": "MPN: Leveraging Multilingual Patch Neuron for Cross-lingual Model   Editing",
            "url": "https://arxiv.org/pdf/2401.03190"
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
      "Based on the search results, I found information about the LU-LAFNs paper. Here's what the research is about:\n\nLU-LAFNs is a method for Locating and Updating Language-Agnostic Factual Neurons to edit multilingual knowledge simultaneously, which avoids knowledge conflicts and improves edit performance.\n\nThe key discovery behind this approach is that the same factual knowledge in different languages generally activates a shared set of neurons, which are called language-agnostic factual neurons (LAFNs). These neurons represent the same factual knowledge shared across languages and imply the semantic connections among multilingual knowledge.\n\nExperimental results on Bi-ZsRE and MzsRE benchmarks demonstrate that the method achieves the best edit performance, indicating the effectiveness and importance of modeling the semantic connections among multilingual knowledge.\n\nThe paper was published at COLING 2025 (as indicated by the ACL Anthology citation) and addresses the problem of multilingual knowledge editing with a focus on cross-lingual portability through the identification and manipulation of language-agnostic neural structures."
    ],
    "durationSeconds": 6.145824885999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6fd908ab-e10a-48f9-8f52-ddbe9ce828cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T21:02:17.477Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BPiG1HchAtWQBkaf1LNGNF`</summary>

```json
{
  "query": "FeatureEdit SAE sparse autoencoder knowledge editing ACL 2025 \"knowledge microscope\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b20351f-5bb3-4941-a52c-b1eee6f26a8b",
  "isSidechain": false,
  "requestId": "req_011CbCbwFEkauxGvZZjJyryf",
  "type": "assistant",
  "uuid": "bac5b8e6-34ae-4316-b620-955f4456d145",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUnQxSf9yuQsAYCkjVMajB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 24700,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 24700,
          "cache_creation_input_tokens": 777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 777
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

_source line 18 · 2026-05-19T21:02:24.565Z_

<details><summary>↩ Tool result · `toolu_01BPiG1HchAtWQBkaf1LNGNF`</summary>

```text
Web search results for query: "FeatureEdit SAE sparse autoencoder knowledge editing ACL 2025 "knowledge microscope""

Links: [{"title":"MicroEdit: Neuron-level Knowledge Disentanglement and Localization in Lifelong Model Editing - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1719/"},{"title":"The Knowledge Microscope: Features as Better Analytical Lenses than   Neurons","url":"https://arxiv.org/pdf/2502.12483"},{"title":"Sparse Autoencoder Features for Classifications and Transferability - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1521/"},{"title":"Unveiling Language-Specific Features in Large Language Models via Sparse Autoencoders - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.229/"},{"title":"Sparse Autoencoder Features for Classifications and Transferability","url":"https://arxiv.org/pdf/2502.11367"},{"title":"Sparse Autoencoder Features for Classifications and Transferability","url":"https://aclanthology.org/2025.emnlp-main.1521.pdf"}]

Based on the search results, I found information related to your query about SAE (Sparse Autoencoder) and knowledge editing, though the specific "FeatureEdit" paper wasn't found. However, I did find highly relevant work:

## The Knowledge Microscope

The paper "The Knowledge Microscope" argues that previous studies primarily utilize MLP neurons as units of analysis for understanding factual knowledge in Language Models, but neurons suffer from polysemanticity. The authors validate that Sparse Autoencoders (SAE) can effectively decompose neurons into features, which serve as alternative analytical units.

SAE transforms a "low-dimensional" neuronal space into a "high-dimensional" feature space, making previously inseparable problems separable.

## Related ACL 2025 Work on SAEs

The search also returned other ACL 2025 papers on sparse autoencoders:

- One paper introduces Sparse Autoencoders as offering a more nuanced analysis by decomposing the activations of LLMs into a sparse linear combination of SAE features, with a novel metric to assess the monolinguality of features obtained from SAEs.

- Another work called "MicroEdit" leverages a sparse autoencoder (SAE) to disentangle knowledge representations and activate only a minimal set of necessary neurons for precise parameter updates.

The "Knowledge Microscope" paper appears to be directly related to your query, focusing on SAEs as better analytical tools than neurons for understanding knowledge in language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bac5b8e6-34ae-4316-b620-955f4456d145",
  "isSidechain": false,
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "939ad1a6-1002-42a9-90ad-a27276cfbf3e",
  "toolUseResult": {
    "query": "FeatureEdit SAE sparse autoencoder knowledge editing ACL 2025 \"knowledge microscope\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XwfbcDfR6F4XNsgGU12mg2",
        "content": [
          {
            "title": "MicroEdit: Neuron-level Knowledge Disentanglement and Localization in Lifelong Model Editing - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.1719/"
          },
          {
            "title": "The Knowledge Microscope: Features as Better Analytical Lenses than   Neurons",
            "url": "https://arxiv.org/pdf/2502.12483"
          },
          {
            "title": "Sparse Autoencoder Features for Classifications and Transferability - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.1521/"
          },
          {
            "title": "Unveiling Language-Specific Features in Large Language Models via Sparse Autoencoders - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.229/"
          },
          {
            "title": "Sparse Autoencoder Features for Classifications and Transferability",
            "url": "https://arxiv.org/pdf/2502.11367"
          },
          {
            "title": "Sparse Autoencoder Features for Classifications and Transferability",
            "url": "https://aclanthology.org/2025.emnlp-main.1521.pdf"
          }
        ]
      },
      "Based on the search results, I found information related to your query about SAE (Sparse Autoencoder) and knowledge editing, though the specific \"FeatureEdit\" paper wasn't found. However, I did find highly relevant work:\n\n## The Knowledge Microscope\n\nThe paper \"The Knowledge Microscope\" argues that previous studies primarily utilize MLP neurons as units of analysis for understanding factual knowledge in Language Models, but neurons suffer from polysemanticity. The authors validate that Sparse Autoencoders (SAE) can effectively decompose neurons into features, which serve as alternative analytical units.\n\nSAE transforms a \"low-dimensional\" neuronal space into a \"high-dimensional\" feature space, making previously inseparable problems separable.\n\n## Related ACL 2025 Work on SAEs\n\nThe search also returned other ACL 2025 papers on sparse autoencoders:\n\n- One paper introduces Sparse Autoencoders as offering a more nuanced analysis by decomposing the activations of LLMs into a sparse linear combination of SAE features, with a novel metric to assess the monolinguality of features obtained from SAEs.\n\n- Another work called \"MicroEdit\" leverages a sparse autoencoder (SAE) to disentangle knowledge representations and activate only a minimal set of necessary neurons for precise parameter updates.\n\nThe \"Knowledge Microscope\" paper appears to be directly related to your query, focusing on SAEs as better analytical tools than neurons for understanding knowledge in language models."
    ],
    "durationSeconds": 7.085240361000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bac5b8e6-34ae-4316-b620-955f4456d145",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T21:02:29.156Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PN575XG2eyZijTT8SrJkYT`</summary>

```json
{
  "query": "SAE sparse autoencoder intervention steering skepticism Peng 2025 Arad EMNLP 2025 output score feature selection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "939ad1a6-1002-42a9-90ad-a27276cfbf3e",
  "isSidechain": false,
  "requestId": "req_011CbCbwybSJe9pFKSV17QTk",
  "type": "assistant",
  "uuid": "eda3e698-1c9d-4422-8f34-5c58c76dd26d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SHz2QiVFubKkchjyADqfeE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 25477,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 25477,
          "cache_creation_input_tokens": 746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 746
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

_source line 20 · 2026-05-19T21:02:38.619Z_

<details><summary>↩ Tool result · `toolu_01PN575XG2eyZijTT8SrJkYT`</summary>

```text
Web search results for query: "SAE sparse autoencoder intervention steering skepticism Peng 2025 Arad EMNLP 2025 output score feature selection"

Links: [{"title":"Does higher interpretability imply better utility? A Pairwise Analysis on Sparse Autoencoders","url":"https://arxiv.org/pdf/2510.03659"},{"title":"Improving Steering Vectors by Targeting Sparse Autoencoder Features","url":"https://arxiv.org/pdf/2411.02193"},{"title":"Toward Efficient Sparse Autoencoder-Guided Steering for Improved In-Context Learning in Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1474/"},{"title":"SAEs Are Good for Steering – If You Select the Right Features","url":"https://arxiv.org/html/2505.20063v1"},{"title":"Toward Efficient Sparse Autoencoder-Guided Steering for ...","url":"https://aclanthology.org/2025.emnlp-main.1474.pdf"},{"title":"Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts","url":"https://arxiv.org/html/2506.23845v1"},{"title":"A Comparative Analysis of Sparse Autoencoder and Activation Difference in Language Model Steering","url":"https://arxiv.org/pdf/2510.01246"}]

Based on the search results, I found several relevant papers and findings related to your query about SAE sparse autoencoders, intervention steering, and feature selection:

## Key Research Areas

**Recent Skepticism About SAE Steering:** As identified in Arad et al. [2025] and Wu et al. [2025], not all interpretable features in SAE are equally effective for steering. This appears to be a central concern in the field.

**Feature Selection Methods:** One innovative selection criterion for SAE features is Δ Token Confidence, which measures the degree to which amplifying a single feature shifts the model's next-token distribution. This has been benchmarked against the best existing output score methods.

**EMNLP 2025 Work:** A paper by Cho & Hockenmaier at EMNLP 2025 is titled "Toward Efficient Sparse Autoencoder-Guided Steering for Improved In-Context Learning in Large Language Models."

**Steering Effectiveness Challenges:** Existing SAE steering methods often introduce noise and redundancy by selecting top-activated features without verifying their relevance.

The search results indicate active research on improving SAE-based steering through better feature selection mechanisms, with growing recognition that interpretability alone doesn't guarantee effective steering utility.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eda3e698-1c9d-4422-8f34-5c58c76dd26d",
  "isSidechain": false,
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "28f18a03-3a58-4686-9de8-00b12005034d",
  "toolUseResult": {
    "query": "SAE sparse autoencoder intervention steering skepticism Peng 2025 Arad EMNLP 2025 output score feature selection",
    "results": [
      {
        "tool_use_id": "srvtoolu_01B3YnbRdau4D6kxzCqdmMPS",
        "content": [
          {
            "title": "Does higher interpretability imply better utility? A Pairwise Analysis on Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2510.03659"
          },
          {
            "title": "Improving Steering Vectors by Targeting Sparse Autoencoder Features",
            "url": "https://arxiv.org/pdf/2411.02193"
          },
          {
            "title": "Toward Efficient Sparse Autoencoder-Guided Steering for Improved In-Context Learning in Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.1474/"
          },
          {
            "title": "SAEs Are Good for Steering – If You Select the Right Features",
            "url": "https://arxiv.org/html/2505.20063v1"
          },
          {
            "title": "Toward Efficient Sparse Autoencoder-Guided Steering for ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1474.pdf"
          },
          {
            "title": "Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts",
            "url": "https://arxiv.org/html/2506.23845v1"
          },
          {
            "title": "A Comparative Analysis of Sparse Autoencoder and Activation Difference in Language Model Steering",
            "url": "https://arxiv.org/pdf/2510.01246"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and findings related to your query about SAE sparse autoencoders, intervention steering, and feature selection:\n\n## Key Research Areas\n\n**Recent Skepticism About SAE Steering:** As identified in Arad et al. [2025] and Wu et al. [2025], not all interpretable features in SAE are equally effective for steering. This appears to be a central concern in the field.\n\n**Feature Selection Methods:** One innovative selection criterion for SAE features is Δ Token Confidence, which measures the degree to which amplifying a single feature shifts the model's next-token distribution. This has been benchmarked against the best existing output score methods.\n\n**EMNLP 2025 Work:** A paper by Cho & Hockenmaier at EMNLP 2025 is titled \"Toward Efficient Sparse Autoencoder-Guided Steering for Improved In-Context Learning in Large Language Models.\"\n\n**Steering Effectiveness Challenges:** Existing SAE steering methods often introduce noise and redundancy by selecting top-activated features without verifying their relevance.\n\nThe search results indicate active research on improving SAE-based steering through better feature selection mechanisms, with growing recognition that interpretability alone doesn't guarantee effective steering utility."
    ],
    "durationSeconds": 9.458771137000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "eda3e698-1c9d-4422-8f34-5c58c76dd26d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation  ## Description Current c…",
  "leafUuid": "28f18a03-3a58-4686-9de8-00b12005034d",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE feature decomposition for cross-lingual knowledge editing",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd"
}
```

---

### Tool call

_source line 23 · 2026-05-19T21:02:41.842Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0199QmM2yNnedEy4owdHXct1`</summary>

```json
{
  "query": "Chou et al 2025 \"causal language control\" multilingual transformers sparse feature steering SAE language steering 90%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28f18a03-3a58-4686-9de8-00b12005034d",
  "isSidechain": false,
  "requestId": "req_011CbCby1xbRXyC1eQ8ksH6d",
  "type": "assistant",
  "uuid": "5a31b9d7-340c-43eb-a06f-0d891e7ee36d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019DfqxgxiE6FFSmLL3LnN7S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 26223,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 26223,
          "cache_creation_input_tokens": 762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 762
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

_source line 24 · 2026-05-19T21:02:49.401Z_

<details><summary>↩ Tool result · `toolu_0199QmM2yNnedEy4owdHXct1`</summary>

```text
Web search results for query: "Chou et al 2025 "causal language control" multilingual transformers sparse feature steering SAE language steering 90%"

Links: [{"title":"[2507.13410] Causal Language Control in Multilingual Transformers via Sparse Feature Steering","url":"https://arxiv.org/abs/2507.13410"},{"title":"Causal Language Control in Multilingual Transformers via Sparse Feature Steering","url":"https://arxiv.org/html/2507.13410v1"},{"title":"Causal Language Control in Multilingual Transformers via Sparse Feature Steering | Algoverse | Algoverse AI Research","url":"https://algoverseairesearch.org/news/causal-language-control"},{"title":"Causal Language Control in Multilingual Transformers via Sparse Feature","url":"https://arxiv.org/pdf/2507.13410"},{"title":"Computation and Language Jul 2025","url":"https://www.arxiv.org/list/cs.CL/2025-07?skip=650&show=25"},{"title":"Tense Localization and Control in a Multilingual LLM","url":"https://aclanthology.org/2025.mrl-main.17.pdf"},{"title":"LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering","url":"https://arxiv.org/pdf/2604.03532"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** Causal Language Control in Multilingual Transformers via Sparse Feature Steering

**Authors:** Cheng-Ting Chou, George Liu, Jessica Sun, Cole Blondin, Kevin Zhu, Vasu Sharma, Sean O'Brien

**Key Findings:**
- The research investigates whether sparse autoencoder (SAE) features can be leveraged to steer the generated language of LLMs during inference.
- Using pretrained SAEs on the residual streams of Gemma-2B and Gemma-9B, they identify features whose activations differ most significantly between English and four target languages: Chinese, Japanese, Spanish, and French.
- By modifying just a single SAE feature at one transformer layer, they achieve controlled language shifts with up to 90% success, as measured by FastText language classification, while preserving semantic fidelity according to LaBSE (Language-Agnostic BERT Sentence Embedding) similarity.
- Language steering is most effective in mid-to-late transformer layers and is amplified by specific attention heads disproportionately associated with language-sensitive SAE features.

**Publication Status:** Accepted to ACL SRW 2025

The paper is available on arXiv at: https://arxiv.org/abs/2507.13410


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a31b9d7-340c-43eb-a06f-0d891e7ee36d",
  "isSidechain": false,
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "aa2de011-d14f-4812-80ea-907e5da997c5",
  "toolUseResult": {
    "query": "Chou et al 2025 \"causal language control\" multilingual transformers sparse feature steering SAE language steering 90%",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A3zNns7zexiYNexk67rTid",
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
            "title": "Causal Language Control in Multilingual Transformers via Sparse Feature Steering | Algoverse | Algoverse AI Research",
            "url": "https://algoverseairesearch.org/news/causal-language-control"
          },
          {
            "title": "Causal Language Control in Multilingual Transformers via Sparse Feature",
            "url": "https://arxiv.org/pdf/2507.13410"
          },
          {
            "title": "Computation and Language Jul 2025",
            "url": "https://www.arxiv.org/list/cs.CL/2025-07?skip=650&show=25"
          },
          {
            "title": "Tense Localization and Control in a Multilingual LLM",
            "url": "https://aclanthology.org/2025.mrl-main.17.pdf"
          },
          {
            "title": "LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering",
            "url": "https://arxiv.org/pdf/2604.03532"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n**Paper Title:** Causal Language Control in Multilingual Transformers via Sparse Feature Steering\n\n**Authors:** Cheng-Ting Chou, George Liu, Jessica Sun, Cole Blondin, Kevin Zhu, Vasu Sharma, Sean O'Brien\n\n**Key Findings:**\n- The research investigates whether sparse autoencoder (SAE) features can be leveraged to steer the generated language of LLMs during inference.\n- Using pretrained SAEs on the residual streams of Gemma-2B and Gemma-9B, they identify features whose activations differ most significantly between English and four target languages: Chinese, Japanese, Spanish, and French.\n- By modifying just a single SAE feature at one transformer layer, they achieve controlled language shifts with up to 90% success, as measured by FastText language classification, while preserving semantic fidelity according to LaBSE (Language-Agnostic BERT Sentence Embedding) similarity.\n- Language steering is most effective in mid-to-late transformer layers and is amplified by specific attention heads disproportionately associated with language-sensitive SAE features.\n\n**Publication Status:** Accepted to ACL SRW 2025\n\nThe paper is available on arXiv at: https://arxiv.org/abs/2507.13410"
    ],
    "durationSeconds": 7.553921715000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5a31b9d7-340c-43eb-a06f-0d891e7ee36d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T21:02:52.316Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RVuHWTj8fY3xisvvMVzXtz`</summary>

```json
{
  "query": "SCAN sparse circuit anchor neuron lifelong knowledge editing 2026 SAE transcoder cross-lingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa2de011-d14f-4812-80ea-907e5da997c5",
  "isSidechain": false,
  "requestId": "req_011CbCbyoivNLtndp67ACZeE",
  "type": "assistant",
  "uuid": "ad4e050e-0989-4179-8944-9554d7a330d8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018evqcAw7gQYUh8ygGuY8mh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 783,
      "cache_read_input_tokens": 26985,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 783,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 26985,
          "cache_creation_input_tokens": 783,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 783
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

_source line 26 · 2026-05-19T21:02:58.646Z_

<details><summary>↩ Tool result · `toolu_01RVuHWTj8fY3xisvvMVzXtz`</summary>

```text
Web search results for query: "SCAN sparse circuit anchor neuron lifelong knowledge editing 2026 SAE transcoder cross-lingual"

Links: [{"title":"SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing","url":"https://arxiv.org/pdf/2603.15226"},{"title":"[2510.22139] Edit Less, Achieve More: Dynamic Sparse Neuron Masking for Lifelong Knowledge Editing in LLMs","url":"https://arxiv.org/abs/2510.22139"},{"title":"Edit Less, Achieve More: Dynamic Sparse Neuron Masking for Lifelong Knowledge Editing in LLMs","url":"https://arxiv.org/html/2510.22139"},{"title":"MPN: Leveraging Multilingual Patch Neuron for Cross-lingual Model   Editing","url":"https://arxiv.org/pdf/2401.03190"},{"title":"Language Model Circuits Are Sparse in the Neuron Basis","url":"https://arxiv.org/pdf/2601.22594"}]

Based on the web search results, I found relevant information about your query:

SCAN (Sparse Circuit Anchor Interpretable Neuron) is a framework for lifelong knowledge editing that transforms editing into mechanism-aware manipulation by constructing knowledge circuits via Sparse Transcoders.

The framework addresses the vulnerability that stems from the prevailing dense editing paradigm, which treats models as black boxes and relies on coarse-grained parameter interventions that disrupt preserved knowledge.

SCAN was tested on Gemma2, Qwen3, and Llama3.1 across multiple benchmarks and achieved superior performance, maintaining model integrity even after 3,000 sequential edits, whereas other existing methods deteriorate progressively and eventually result in model collapse.

The search results also show related work in this area:
- Lifelong knowledge editing enables continuous, precise updates to outdated knowledge in LLMs without computationally expensive full retraining
- Cross-lingual model editing addresses the issue of cross-lingual knowledge synchronization in multilingual models by training multilingual patch neurons to store cross-lingual knowledge
- Sparse autoencoders (SAEs) and transcoders are approaches that learn to express language model computations in higher-dimensional sparse spaces


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad4e050e-0989-4179-8944-9554d7a330d8",
  "isSidechain": false,
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "dff2d655-5a5e-407e-802f-3c57e1afd377",
  "toolUseResult": {
    "query": "SCAN sparse circuit anchor neuron lifelong knowledge editing 2026 SAE transcoder cross-lingual",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U2MYrnUkYwJx9ncLuP5bqY",
        "content": [
          {
            "title": "SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing",
            "url": "https://arxiv.org/pdf/2603.15226"
          },
          {
            "title": "[2510.22139] Edit Less, Achieve More: Dynamic Sparse Neuron Masking for Lifelong Knowledge Editing in LLMs",
            "url": "https://arxiv.org/abs/2510.22139"
          },
          {
            "title": "Edit Less, Achieve More: Dynamic Sparse Neuron Masking for Lifelong Knowledge Editing in LLMs",
            "url": "https://arxiv.org/html/2510.22139"
          },
          {
            "title": "MPN: Leveraging Multilingual Patch Neuron for Cross-lingual Model   Editing",
            "url": "https://arxiv.org/pdf/2401.03190"
          },
          {
            "title": "Language Model Circuits Are Sparse in the Neuron Basis",
            "url": "https://arxiv.org/pdf/2601.22594"
          }
        ]
      },
      "Based on the web search results, I found relevant information about your query:\n\nSCAN (Sparse Circuit Anchor Interpretable Neuron) is a framework for lifelong knowledge editing that transforms editing into mechanism-aware manipulation by constructing knowledge circuits via Sparse Transcoders.\n\nThe framework addresses the vulnerability that stems from the prevailing dense editing paradigm, which treats models as black boxes and relies on coarse-grained parameter interventions that disrupt preserved knowledge.\n\nSCAN was tested on Gemma2, Qwen3, and Llama3.1 across multiple benchmarks and achieved superior performance, maintaining model integrity even after 3,000 sequential edits, whereas other existing methods deteriorate progressively and eventually result in model collapse.\n\nThe search results also show related work in this area:\n- Lifelong knowledge editing enables continuous, precise updates to outdated knowledge in LLMs without computationally expensive full retraining\n- Cross-lingual model editing addresses the issue of cross-lingual knowledge synchronization in multilingual models by training multilingual patch neurons to store cross-lingual knowledge\n- Sparse autoencoders (SAEs) and transcoders are approaches that learn to express language model computations in higher-dimensional sparse spaces"
    ],
    "durationSeconds": 6.3258004650000075,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ad4e050e-0989-4179-8944-9554d7a330d8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T21:03:01.779Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JcWfHmhCecEoT3J4Nnvgqt`</summary>

```json
{
  "query": "LangSAE language identity removal SAE multilingual retrieval 2026 arXiv:2601.04768"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dff2d655-5a5e-407e-802f-3c57e1afd377",
  "isSidechain": false,
  "requestId": "req_011CbCbzVGSmqUHyTrF1Z8iJ",
  "type": "assistant",
  "uuid": "5a19a053-c93f-4906-9e99-d18793c1aff6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014gaBNHdsmCsZKSP5ikQHhM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 27768,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 639,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 27768,
          "cache_creation_input_tokens": 639,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 639
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

_source line 28 · 2026-05-19T21:03:06.044Z_

<details><summary>↩ Tool result · `toolu_01JcWfHmhCecEoT3J4Nnvgqt`</summary>

```text
Web search results for query: "LangSAE language identity removal SAE multilingual retrieval 2026 arXiv:2601.04768"

Links: [{"title":"[2601.04768] LANGSAE EDITING: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal","url":"https://arxiv.org/abs/2601.04768"},{"title":"LANGSAE EDITING: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal","url":"https://arxiv.org/pdf/2601.04768"},{"title":"LangSAE Editing: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal","url":"https://arxiv.org/html/2601.04768v1"},{"title":"LANGSAE EDITING: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2601.04768"},{"title":"LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering","url":"https://arxiv.org/pdf/2604.03532"}]

Based on the search results, I found the paper you're looking for:

LangSAE Editing is a post-hoc sparse autoencoder trained on pooled embeddings that enables controllable removal of language-identity signal directly in vector space. In multilingual settings, dense retrieval often searches over mixed-language collections, yet multilingual embeddings encode language identity alongside semantics, which can inflate similarity for same-language pairs and crowd out relevant evidence written in other languages.

The method identifies language-associated latent units using cross-language activation statistics, suppresses these units at inference time, and reconstructs embeddings in the original dimensionality, making it compatible with existing vector databases without retraining the base encoder or re-encoding raw text. Experiments across multiple languages show consistent improvements in ranking quality and cross-language coverage, with especially strong gains for script-distinct languages.

The paper was submitted on January 8, 2026, and is authored by Dongjun Kim, Jeongho Yoon, Chanjun Park, and Heuiseok Lim. You can find the full paper on arXiv at https://arxiv.org/abs/2601.04768.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a19a053-c93f-4906-9e99-d18793c1aff6",
  "isSidechain": false,
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "72896f45-8bae-41c8-9123-dc0b24ffc2b1",
  "toolUseResult": {
    "query": "LangSAE language identity removal SAE multilingual retrieval 2026 arXiv:2601.04768",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XVh9BVytjcN17NBwSfXjhE",
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
      "Based on the search results, I found the paper you're looking for:\n\nLangSAE Editing is a post-hoc sparse autoencoder trained on pooled embeddings that enables controllable removal of language-identity signal directly in vector space. In multilingual settings, dense retrieval often searches over mixed-language collections, yet multilingual embeddings encode language identity alongside semantics, which can inflate similarity for same-language pairs and crowd out relevant evidence written in other languages.\n\nThe method identifies language-associated latent units using cross-language activation statistics, suppresses these units at inference time, and reconstructs embeddings in the original dimensionality, making it compatible with existing vector databases without retraining the base encoder or re-encoding raw text. Experiments across multiple languages show consistent improvements in ranking quality and cross-language coverage, with especially strong gains for script-distinct languages.\n\nThe paper was submitted on January 8, 2026, and is authored by Dongjun Kim, Jeongho Yoon, Chanjun Park, and Heuiseok Lim. You can find the full paper on arXiv at https://arxiv.org/abs/2601.04768."
    ],
    "durationSeconds": 4.262021179999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5a19a053-c93f-4906-9e99-d18793c1aff6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-19T21:03:06.056Z_

```json
{
  "parentUuid": "72896f45-8bae-41c8-9123-dc0b24ffc2b1",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "75daf980-df47-4735-8194-8e5dbc2d4e84",
  "timestamp": "2026-05-19T21:03:06.056Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-19T21:03:09.326Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VcKxySFp53JSS4GmUBsTVQ`</summary>

```json
{
  "query": "Leask et al \"sparse autoencoders do not find canonical units\" ICLR 2025 meta-SAE feature atomicity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75daf980-df47-4735-8194-8e5dbc2d4e84",
  "isSidechain": false,
  "requestId": "req_011CbCc12txY96YvfU2hYexB",
  "type": "assistant",
  "uuid": "4fcfbb92-2865-47b3-a405-fa98d9040dfb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gavg5Viuwig19KxHyv1af",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 761,
      "cache_read_input_tokens": 28407,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 761,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 28407,
          "cache_creation_input_tokens": 761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 761
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

_source line 31 · 2026-05-19T21:03:15.785Z_

<details><summary>↩ Tool result · `toolu_01VcKxySFp53JSS4GmUBsTVQ`</summary>

```text
Web search results for query: "Leask et al "sparse autoencoders do not find canonical units" ICLR 2025 meta-SAE feature atomicity"

Links: [{"title":"Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/84ca3f2d9d9bfca13f69b48ea63eb4a5-Abstract-Conference.html"},{"title":"(PDF) Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://www.researchgate.net/publication/388847461_Sparse_Autoencoders_Do_Not_Find_Canonical_Units_of_Analysis"},{"title":"ActivationReasoning: Logical Reasoning in Latent Activation Spaces","url":"https://arxiv.org/html/2510.18184v1"},{"title":"ICLR Poster Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://iclr.cc/virtual/2025/poster/30676"},{"title":"[2502.04878] Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://arxiv.org/abs/2502.04878"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2502.04878"},{"title":"SPARSE AUTOENCODERS DO NOT FIND CANONICAL ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/84ca3f2d9d9bfca13f69b48ea63eb4a5-Paper-Conference.pdf"},{"title":"Sparse Autoencoders Do Not Find Canonical Units of Analysis","url":"https://arxiv.org/html/2502.04878v1"},{"title":"Sparse Autoencoders Do Not Find Canonical Units of Analysis | OpenReview","url":"https://openreview.net/forum?id=9ca9eHNrdH"}]

I found the paper! Here's what the search revealed:

The paper is by Patrick Leask, Bart Bussmann, Michael Pearce, Joseph Bloom, Curt Tigges, Noura Al Moubayed, Lee Sharkey, and Neel Nanda, and it was published as a conference paper at ICLR 2025.

**Main Findings:**

The paper uses two novel techniques: SAE stitching to show sparse autoencoders are incomplete, and meta-SAEs to show they are not atomic.

**Methodology:**

SAE stitching involves inserting or swapping latents from a larger SAE into a smaller one. Latents from the larger SAE can be divided into two categories: novel latents, which improve performance when added to the smaller SAE, indicating they capture novel information, and reconstruction latents, which can replace corresponding latents in the smaller SAE that have similar behavior.

**Key Conclusion:**

The paper concludes that SAE practitioners should embrace a pragmatic approach towards choosing dictionary size when using SAEs on interpretability tasks such as probing, unlearning and steering.

The paper directly challenges the assumption that sparse autoencoders can discover a canonical, complete, and atomic set of features, which has important implications for mechanistic interpretability research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fcfbb92-2865-47b3-a405-fa98d9040dfb",
  "isSidechain": false,
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "abd4c9f4-52a0-413a-b8c3-73bb8461c3ce",
  "toolUseResult": {
    "query": "Leask et al \"sparse autoencoders do not find canonical units\" ICLR 2025 meta-SAE feature atomicity",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YEZV7AjawKex3J9KMnoty4",
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
            "title": "ActivationReasoning: Logical Reasoning in Latent Activation Spaces",
            "url": "https://arxiv.org/html/2510.18184v1"
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
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://arxiv.org/pdf/2502.04878"
          },
          {
            "title": "SPARSE AUTOENCODERS DO NOT FIND CANONICAL ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/84ca3f2d9d9bfca13f69b48ea63eb4a5-Paper-Conference.pdf"
          },
          {
            "title": "Sparse Autoencoders Do Not Find Canonical Units of Analysis",
            "url": "https://arxiv.org/html/2502.04878v1"
          },
          {
            "title": "Sparse Autoencoders Do Not Find Canonical Units of Analysis | OpenReview",
            "url": "https://openreview.net/forum?id=9ca9eHNrdH"
          }
        ]
      },
      "I found the paper! Here's what the search revealed:\n\nThe paper is by Patrick Leask, Bart Bussmann, Michael Pearce, Joseph Bloom, Curt Tigges, Noura Al Moubayed, Lee Sharkey, and Neel Nanda, and it was published as a conference paper at ICLR 2025.\n\n**Main Findings:**\n\nThe paper uses two novel techniques: SAE stitching to show sparse autoencoders are incomplete, and meta-SAEs to show they are not atomic.\n\n**Methodology:**\n\nSAE stitching involves inserting or swapping latents from a larger SAE into a smaller one. Latents from the larger SAE can be divided into two categories: novel latents, which improve performance when added to the smaller SAE, indicating they capture novel information, and reconstruction latents, which can replace corresponding latents in the smaller SAE that have similar behavior.\n\n**Key Conclusion:**\n\nThe paper concludes that SAE practitioners should embrace a pragmatic approach towards choosing dictionary size when using SAEs on interpretability tasks such as probing, unlearning and steering.\n\nThe paper directly challenges the assumption that sparse autoencoders can discover a canonical, complete, and atomic set of features, which has important implications for mechanistic interpretability research."
    ],
    "durationSeconds": 6.455367751999991,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4fcfbb92-2865-47b3-a405-fa98d9040dfb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-19T21:03:18.999Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013mbHVFQaCxsEtU4pxwkgb6`</summary>

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
  "parentUuid": "abd4c9f4-52a0-413a-b8c3-73bb8461c3ce",
  "isSidechain": false,
  "requestId": "req_011CbCc1kYEWwZxTg7pErDqe",
  "type": "assistant",
  "uuid": "7fda9a2a-32f2-46e8-865c-12e330f3cbbd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014z2WPB4qtwgJBkNiKWajS5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 909,
      "cache_read_input_tokens": 29168,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 29168,
          "cache_creation_input_tokens": 909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 909
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

_source line 33 · 2026-05-19T21:03:24.096Z_

<details><summary>↩ Tool result · `toolu_013mbHVFQaCxsEtU4pxwkgb6`</summary>

```text
Web search results for query: "Mondal et al "language-specific neurons do not facilitate cross-lingual transfer" NAACL 2025"

Links: [{"title":"Language-Specific Neurons Do Not Facilitate Cross-Lingual Transfer - ACL Anthology","url":"https://aclanthology.org/2025.insights-1.6/"},{"title":"Tracing Multilingual Knowledge Acquisition Dynamics in Domain Adaptation: A Case Study of English-Japanese Biomedical Adaptation","url":"https://arxiv.org/html/2510.12115v1"},{"title":"[2503.17456] Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer","url":"https://arxiv.org/abs/2503.17456"},{"title":"Language Arithmetics: Towards Systematic Language Neuron Identification and Manipulation","url":"https://arxiv.org/html/2507.22608v1"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/html/2601.16390v1"},{"title":"Linguistic Neuron Overlap Patterns to Facilitate Cross-lingual Transfer on Low-resource Languages","url":"https://arxiv.org/html/2508.17078v1"},{"title":"Unveiling the Influence of Amplifying Language-Specific Neurons","url":"https://arxiv.org/html/2507.22581v3"},{"title":"Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer - Paper Detail","url":"https://deeplearn.org/arxiv/590221/language-specific-neurons-do-not-facilitate-cross-lingual-transfer"},{"title":"Language-specific Neurons Do Not Facilitate Cross- ...","url":"https://aclanthology.org/2025.insights-1.6.pdf"},{"title":"Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer","url":"https://arxiv.org/pdf/2503.17456"}]

I found the paper you're looking for. Here are the key details:

The paper "Language-Specific Neurons Do Not Facilitate Cross-Lingual Transfer" is by Soumen Kumar Mondal, Sayambhu Sen, Abhishek Singhania, and Preethi Jyothi.

However, I should note that the paper was published in The Sixth Workshop on Insights from Negative Results in NLP, pages 46–62, Albuquerque, New Mexico, not directly at NAACL 2025. The paper is available through the ACL Anthology.

The work explores whether existing techniques to identify language-specific neurons can be leveraged to enhance cross-lingual task performance of low-resource languages.

The paper has been cited and discussed in several subsequent works on multilingual language models and neuron-level interventions. You can access the full paper at the ACL Anthology link: https://aclanthology.org/2025.insights-1.6/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fda9a2a-32f2-46e8-865c-12e330f3cbbd",
  "isSidechain": false,
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "aa34da78-3e44-4c8f-aef8-eb76af03a82f",
  "toolUseResult": {
    "query": "Mondal et al \"language-specific neurons do not facilitate cross-lingual transfer\" NAACL 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UdKSpqNba77ZxYcmdajUFY",
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
            "title": "Linguistic Neuron Overlap Patterns to Facilitate Cross-lingual Transfer on Low-resource Languages",
            "url": "https://arxiv.org/html/2508.17078v1"
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
      "I found the paper you're looking for. Here are the key details:\n\nThe paper \"Language-Specific Neurons Do Not Facilitate Cross-Lingual Transfer\" is by Soumen Kumar Mondal, Sayambhu Sen, Abhishek Singhania, and Preethi Jyothi.\n\nHowever, I should note that the paper was published in The Sixth Workshop on Insights from Negative Results in NLP, pages 46–62, Albuquerque, New Mexico, not directly at NAACL 2025. The paper is available through the ACL Anthology.\n\nThe work explores whether existing techniques to identify language-specific neurons can be leveraged to enhance cross-lingual task performance of low-resource languages.\n\nThe paper has been cited and discussed in several subsequent works on multilingual language models and neuron-level interventions. You can access the full paper at the ACL Anthology link: https://aclanthology.org/2025.insights-1.6/"
    ],
    "durationSeconds": 5.092245582000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7fda9a2a-32f2-46e8-865c-12e330f3cbbd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation  ## Description Current c…",
  "leafUuid": "aa34da78-3e44-4c8f-aef8-eb76af03a82f",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE feature decomposition for cross-lingual knowledge editing",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd"
}
```

---

### Tool call

_source line 36 · 2026-05-19T21:03:27.111Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011GMBPu2J4bGir6SipGJqdp`</summary>

```json
{
  "query": "\"merging methods\" multilingual knowledge editing 2026 arXiv:2605.13919 cross-lingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa34da78-3e44-4c8f-aef8-eb76af03a82f",
  "isSidechain": false,
  "requestId": "req_011CbCc2N3RTzReb2cezPFcJ",
  "type": "assistant",
  "uuid": "4ed12464-9f45-460f-bde0-a4dd62d584fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUxSGgLubLdcxid6PHw9Xv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 30077,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 30077,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 37 · 2026-05-19T21:03:34.472Z_

<details><summary>↩ Tool result · `toolu_011GMBPu2J4bGir6SipGJqdp`</summary>

```text
Web search results for query: ""merging methods" multilingual knowledge editing 2026 arXiv:2605.13919 cross-lingual"

Links: [{"title":"[2605.13919] Merging Methods for Multilingual Knowledge Editing for Large Language Models: An Empirical Odyssey","url":"https://arxiv.org/abs/2605.13919"},{"title":"Merging Methods for Multilingual Knowledge Editing for Large Language Models: An Empirical Odyssey","url":"https://arxiv.org/html/2605.13919"},{"title":"Multilingual Knowledge Editing with Language-Agnostic Factual Neurons","url":"https://arxiv.org/pdf/2406.16416"},{"title":"Model Merging for Knowledge Editing","url":"https://arxiv.org/html/2506.12384v1"},{"title":"MEMLA: Enhancing Multilingual Knowledge Editing with Neuron-Masked   Low-Rank Adaptation","url":"https://arxiv.org/pdf/2406.11566"},{"title":"Retrieval-augmented Multilingual Knowledge Editing","url":"https://arxiv.org/pdf/2312.13040"},{"title":"Model Merging for Knowledge Editing","url":"https://arxiv.org/pdf/2506.12384"},{"title":"[2603.28263] Merge and Conquer: Instructing Multilingual Models by Adding Target Language Weights","url":"https://arxiv.org/abs/2603.28263"},{"title":"Merge and Conquer: Instructing Multilingual Models by Adding Target Language Weights","url":"https://arxiv.org/pdf/2603.28263"}]

I found the paper you're looking for! Here are the key findings from arXiv:2605.13919 on "Merging Methods for Multilingual Knowledge Editing for Large Language Models: An Empirical Odyssey".

Multilingual knowledge editing (MKE) remains challenging because language-specific edits interfere with one another, even when locate-then-edit methods work well in monolingual settings.

The paper addresses three main research questions: the effectiveness of vector merging methods for MKE, the extent to which Task Singular Vectors for Merging (TSVM) can reduce multilingual interference, and the influence of the weight scaling factor and rank compression ratio on performance.

**Key Findings:**

- Vector summation with shared covariance is the most reliable overall strategy, whereas simple summation without shared covariance performs poorly.
- TSVM improves performance in some settings, but its ability to mitigate multilingual interference is limited.

**Methodology:**

The researchers evaluate six merging variants with two popular backbone large language models, two base knowledge editing methods, and 12 languages on the MzsRE benchmark under a large-scale batch-editing setting.

The paper was submitted on May 13, 2026, and provides an empirical investigation into how vector merging methods can be applied to address cross-lingual challenges in knowledge editing for multilingual LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ed12464-9f45-460f-bde0-a4dd62d584fa",
  "isSidechain": false,
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "2af8d22b-4566-4adf-aa8c-2f2d4a6b027e",
  "toolUseResult": {
    "query": "\"merging methods\" multilingual knowledge editing 2026 arXiv:2605.13919 cross-lingual",
    "results": [
      {
        "tool_use_id": "srvtoolu_016wf52ozDjR7b3R3T3AeqXq",
        "content": [
          {
            "title": "[2605.13919] Merging Methods for Multilingual Knowledge Editing for Large Language Models: An Empirical Odyssey",
            "url": "https://arxiv.org/abs/2605.13919"
          },
          {
            "title": "Merging Methods for Multilingual Knowledge Editing for Large Language Models: An Empirical Odyssey",
            "url": "https://arxiv.org/html/2605.13919"
          },
          {
            "title": "Multilingual Knowledge Editing with Language-Agnostic Factual Neurons",
            "url": "https://arxiv.org/pdf/2406.16416"
          },
          {
            "title": "Model Merging for Knowledge Editing",
            "url": "https://arxiv.org/html/2506.12384v1"
          },
          {
            "title": "MEMLA: Enhancing Multilingual Knowledge Editing with Neuron-Masked   Low-Rank Adaptation",
            "url": "https://arxiv.org/pdf/2406.11566"
          },
          {
            "title": "Retrieval-augmented Multilingual Knowledge Editing",
            "url": "https://arxiv.org/pdf/2312.13040"
          },
          {
            "title": "Model Merging for Knowledge Editing",
            "url": "https://arxiv.org/pdf/2506.12384"
          },
          {
            "title": "[2603.28263] Merge and Conquer: Instructing Multilingual Models by Adding Target Language Weights",
            "url": "https://arxiv.org/abs/2603.28263"
          },
          {
            "title": "Merge and Conquer: Instructing Multilingual Models by Adding Target Language Weights",
            "url": "https://arxiv.org/pdf/2603.28263"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key findings from arXiv:2605.13919 on \"Merging Methods for Multilingual Knowledge Editing for Large Language Models: An Empirical Odyssey\".\n\nMultilingual knowledge editing (MKE) remains challenging because language-specific edits interfere with one another, even when locate-then-edit methods work well in monolingual settings.\n\nThe paper addresses three main research questions: the effectiveness of vector merging methods for MKE, the extent to which Task Singular Vectors for Merging (TSVM) can reduce multilingual interference, and the influence of the weight scaling factor and rank compression ratio on performance.\n\n**Key Findings:**\n\n- Vector summation with shared covariance is the most reliable overall strategy, whereas simple summation without shared covariance performs poorly.\n- TSVM improves performance in some settings, but its ability to mitigate multilingual interference is limited.\n\n**Methodology:**\n\nThe researchers evaluate six merging variants with two popular backbone large language models, two base knowledge editing methods, and 12 languages on the MzsRE benchmark under a large-scale batch-editing setting.\n\nThe paper was submitted on May 13, 2026, and provides an empirical investigation into how vector merging methods can be applied to address cross-lingual challenges in knowledge editing for multilingual LLMs."
    ],
    "durationSeconds": 7.357642116999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4ed12464-9f45-460f-bde0-a4dd62d584fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-19T21:03:37.197Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012jRpVMGYUcwn8GmPvcLGGT`</summary>

```json
{
  "query": "CLM-Bench cross-lingual misalignment knowledge editing 2026 Chinese English orthogonal edit vectors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2af8d22b-4566-4adf-aa8c-2f2d4a6b027e",
  "isSidechain": false,
  "requestId": "req_011CbCc38QAEAUPQ1t6m3Ax9",
  "type": "assistant",
  "uuid": "c480f259-2af5-4757-9737-e5b4d51e5085",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUbur2bFrEDp4Srda53bA2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 30885,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 30885,
          "cache_creation_input_tokens": 822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 822
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

_source line 39 · 2026-05-19T21:03:44.860Z_

<details><summary>↩ Tool result · `toolu_012jRpVMGYUcwn8GmPvcLGGT`</summary>

```text
Web search results for query: "CLM-Bench cross-lingual misalignment knowledge editing 2026 Chinese English orthogonal edit vectors"

Links: [{"title":"CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing","url":"https://arxiv.org/html/2601.17397v1"},{"title":"CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing","url":"https://arxiv.org/pdf/2601.17397"},{"title":"[2601.17397] CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing","url":"https://arxiv.org/abs/2601.17397"},{"title":"Cross-lingual Misalignment in Neural Models","url":"https://www.emergentmind.com/topics/cross-lingual-misalignment"},{"title":"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/html/2601.08331v1"}]

I found relevant information about CLM-Bench and the orthogonal edit vectors you're asking about.

CLM-Bench is a culture-aware benchmark constructed using a native Chinese-first methodology, with 1,010 high-quality CounterFact pairs rooted in Chinese cultural contexts (covering domains like history and literature) aligned with English counterparts.

The research reveals a significant Cross-lingual Misalignment: edits in one language function independently and fail to propagate to the other.

Regarding the orthogonal edit vectors, the edit vectors for Chinese and English representations are nearly orthogonal, which explains why cross-lingual transfer fails—the optimization direction for one language has almost no projection onto the other. When mixed-language editing is performed, the resulting vector is an almost perfect linear sum of the individual language vectors.

This insight suggests that multilingual knowledge in current LLMs is stored in disjoint subspaces that do not naturally interact during gradient-based or locate-and-edit updates. The research was published in January 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c480f259-2af5-4757-9737-e5b4d51e5085",
  "isSidechain": false,
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "527eec1e-bef7-4b16-913f-106c4e360fd2",
  "toolUseResult": {
    "query": "CLM-Bench cross-lingual misalignment knowledge editing 2026 Chinese English orthogonal edit vectors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WUwizXrmeCMgmhE1em1Dnj",
        "content": [
          {
            "title": "CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing",
            "url": "https://arxiv.org/html/2601.17397v1"
          },
          {
            "title": "CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing",
            "url": "https://arxiv.org/pdf/2601.17397"
          },
          {
            "title": "[2601.17397] CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing",
            "url": "https://arxiv.org/abs/2601.17397"
          },
          {
            "title": "Cross-lingual Misalignment in Neural Models",
            "url": "https://www.emergentmind.com/topics/cross-lingual-misalignment"
          },
          {
            "title": "CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark",
            "url": "https://arxiv.org/html/2601.08331v1"
          }
        ]
      },
      "I found relevant information about CLM-Bench and the orthogonal edit vectors you're asking about.\n\nCLM-Bench is a culture-aware benchmark constructed using a native Chinese-first methodology, with 1,010 high-quality CounterFact pairs rooted in Chinese cultural contexts (covering domains like history and literature) aligned with English counterparts.\n\nThe research reveals a significant Cross-lingual Misalignment: edits in one language function independently and fail to propagate to the other.\n\nRegarding the orthogonal edit vectors, the edit vectors for Chinese and English representations are nearly orthogonal, which explains why cross-lingual transfer fails—the optimization direction for one language has almost no projection onto the other. When mixed-language editing is performed, the resulting vector is an almost perfect linear sum of the individual language vectors.\n\nThis insight suggests that multilingual knowledge in current LLMs is stored in disjoint subspaces that do not naturally interact during gradient-based or locate-and-edit updates. The research was published in January 2026."
    ],
    "durationSeconds": 7.659122709999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c480f259-2af5-4757-9737-e5b4d51e5085",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-19T21:03:48.258Z_

Now I have sufficient information to make my assessment. Let me compile the evaluation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "527eec1e-bef7-4b16-913f-106c4e360fd2",
  "isSidechain": false,
  "requestId": "req_011CbCc3to8NtuSdq9r3CrbG",
  "type": "assistant",
  "uuid": "dcc9a1a6-94bc-4fe8-bb32-a43ea30ea0d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLDuDvtyVBZDeXS4ZqheT9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 31707,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 617,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 97,
          "cache_read_input_tokens": 31707,
          "cache_creation_input_tokens": 617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 617
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

_source line 41 · 2026-05-19T21:03:48.889Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KS11d8VRgFRr35fcLkSf8A`</summary>

```json
{
  "query": "Qwen-Scope SAE sparse autoencoder Qwen3 2026 arXiv:2605.11887"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcc9a1a6-94bc-4fe8-bb32-a43ea30ea0d0",
  "isSidechain": false,
  "requestId": "req_011CbCc3to8NtuSdq9r3CrbG",
  "type": "assistant",
  "uuid": "11cf4204-914a-4e47-b383-2008a8a52ca0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLDuDvtyVBZDeXS4ZqheT9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 31707,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 617,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 97,
          "cache_read_input_tokens": 31707,
          "cache_creation_input_tokens": 617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 617
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

_source line 42 · 2026-05-19T21:03:56.249Z_

<details><summary>↩ Tool result · `toolu_01KS11d8VRgFRr35fcLkSf8A`</summary>

```text
Web search results for query: "Qwen-Scope SAE sparse autoencoder Qwen3 2026 arXiv:2605.11887"

Links: [{"title":"Qwen-Scope: Open-Source Sparse AutoEncoders for LLM Interpretability and Steering • Dev|Journal","url":"https://earezki.com/ai-news/2026-05-01-qwen-ai-releases-qwen-scope-an-open-source-sparse-autoencoders-sae-suite-that-turns-llm-internal-features-into-practical-development-tools/"},{"title":"Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models","url":"https://arxiv.org/html/2605.11887"},{"title":"Qwen AI Releases Qwen-Scope: An Open-Source Sparse AutoEncoders (SAE) Suite That Turns LLM Internal Features into Practical Development Tools - MarkTechPost","url":"https://www.marktechpost.com/2026/05/01/qwen-ai-releases-qwen-scope-an-open-source-sparse-autoencoders-sae-suite-that-turns-llm-internal-features-into-practical-development-tools/"},{"title":"[2605.11887] Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models","url":"https://arxiv.org/abs/2605.11887"},{"title":"Qwen Releases Qwen-Scope Sparse Autoencoder Suite for Qwen Models","url":"https://www.therift.ai/news-feed/qwen-releases-qwen-scope-sparse-autoencoder-suite-for-qwen-models"},{"title":"Pairwise matrices for sparse autoencoders: single-feature inspection mislabels causal axes","url":"https://arxiv.org/html/2605.03160v1"},{"title":"ModelScope on X: \"Introducing Qwen-Scope! Sparse Autoencoders trained on Qwen3 and Qwen3.5 models, turning hidden representations into interpretable features. 🚀 14 SAE weight sets across 7 models: Qwen3-1.7B, 8B, 30B-A3B and Qwen3.5-2B, 9B, 27B, 35B-A3B. Trained on 0.5B tokens sampled from https://t.co/mRPmR2Yvpn\" / X","url":"https://x.com/ModelScope2022/status/2052009415000076568"},{"title":"Aihola","url":"https://aihola.com/article/alibaba-qwen-scope-release"}]

I found comprehensive information about Qwen-Scope. Here's what the search results reveal:

## Overview

Qwen-Scope is an open-source suite of SAEs built on the Qwen model family, comprising 14 groups of SAEs across 7 model variants from the Qwen3 and Qwen3.5 series, covering both dense and mixture-of-expert architectures.

## Key Features

SAEs trained on Qwen3/3.5 serve as a common interface for four practical directions: interpretable steering at inference time, capability-aware benchmark analysis, feature-guided data workflows, and targeted post-training for model improvement.

Sparse latent features represent specific concepts like style or language, activated using a Top-k rule with k=50 or 100.

## Practical Applications

**Inference-time Steering:** By adding or subtracting a feature direction from the residual stream at inference time using the formula h' = h + αd, where h is the hidden state, d is the SAE feature direction, and α controls strength, engineers can push the model toward or away from specific behaviors.

**Model Improvement:** Sparse Autoencoder-guided Supervised Fine-Tuning (SASFT) reduced code-switching by over 50% across multiple model families.

## Coverage

Qwen-Scope ships sparse-autoencoder weights for Qwen3 and Qwen3.5 base models from 1.7B up to the 35B-A3B variant. The collection covers sizes from 1.7B parameters up through the 35B-A3B mixture-of-experts variant, with multiple width and sparsity configurations.

The paper (arXiv:2605.11887) represents a significant contribution to open-source mechanistic interpretability research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11cf4204-914a-4e47-b383-2008a8a52ca0",
  "isSidechain": false,
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "16933d41-323b-4b3d-8fb0-3b90760283a6",
  "toolUseResult": {
    "query": "Qwen-Scope SAE sparse autoencoder Qwen3 2026 arXiv:2605.11887",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EEgUz9Gv35SbSJvkrA8zLT",
        "content": [
          {
            "title": "Qwen-Scope: Open-Source Sparse AutoEncoders for LLM Interpretability and Steering • Dev|Journal",
            "url": "https://earezki.com/ai-news/2026-05-01-qwen-ai-releases-qwen-scope-an-open-source-sparse-autoencoders-sae-suite-that-turns-llm-internal-features-into-practical-development-tools/"
          },
          {
            "title": "Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models",
            "url": "https://arxiv.org/html/2605.11887"
          },
          {
            "title": "Qwen AI Releases Qwen-Scope: An Open-Source Sparse AutoEncoders (SAE) Suite That Turns LLM Internal Features into Practical Development Tools - MarkTechPost",
            "url": "https://www.marktechpost.com/2026/05/01/qwen-ai-releases-qwen-scope-an-open-source-sparse-autoencoders-sae-suite-that-turns-llm-internal-features-into-practical-development-tools/"
          },
          {
            "title": "[2605.11887] Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models",
            "url": "https://arxiv.org/abs/2605.11887"
          },
          {
            "title": "Qwen Releases Qwen-Scope Sparse Autoencoder Suite for Qwen Models",
            "url": "https://www.therift.ai/news-feed/qwen-releases-qwen-scope-sparse-autoencoder-suite-for-qwen-models"
          },
          {
            "title": "Pairwise matrices for sparse autoencoders: single-feature inspection mislabels causal axes",
            "url": "https://arxiv.org/html/2605.03160v1"
          },
          {
            "title": "ModelScope on X: \"Introducing Qwen-Scope! Sparse Autoencoders trained on Qwen3 and Qwen3.5 models, turning hidden representations into interpretable features. 🚀 14 SAE weight sets across 7 models: Qwen3-1.7B, 8B, 30B-A3B and Qwen3.5-2B, 9B, 27B, 35B-A3B. Trained on 0.5B tokens sampled from https://t.co/mRPmR2Yvpn\" / X",
            "url": "https://x.com/ModelScope2022/status/2052009415000076568"
          },
          {
            "title": "Aihola",
            "url": "https://aihola.com/article/alibaba-qwen-scope-release"
          }
        ]
      },
      "I found comprehensive information about Qwen-Scope. Here's what the search results reveal:\n\n## Overview\n\nQwen-Scope is an open-source suite of SAEs built on the Qwen model family, comprising 14 groups of SAEs across 7 model variants from the Qwen3 and Qwen3.5 series, covering both dense and mixture-of-expert architectures.\n\n## Key Features\n\nSAEs trained on Qwen3/3.5 serve as a common interface for four practical directions: interpretable steering at inference time, capability-aware benchmark analysis, feature-guided data workflows, and targeted post-training for model improvement.\n\nSparse latent features represent specific concepts like style or language, activated using a Top-k rule with k=50 or 100.\n\n## Practical Applications\n\n**Inference-time Steering:** By adding or subtracting a feature direction from the residual stream at inference time using the formula h' = h + αd, where h is the hidden state, d is the SAE feature direction, and α controls strength, engineers can push the model toward or away from specific behaviors.\n\n**Model Improvement:** Sparse Autoencoder-guided Supervised Fine-Tuning (SASFT) reduced code-switching by over 50% across multiple model families.\n\n## Coverage\n\nQwen-Scope ships sparse-autoencoder weights for Qwen3 and Qwen3.5 base models from 1.7B up to the 35B-A3B variant. The collection covers sizes from 1.7B parameters up through the 35B-A3B mixture-of-experts variant, with multiple width and sparsity configurations.\n\nThe paper (arXiv:2605.11887) represents a significant contribution to open-source mechanistic interpretability research."
    ],
    "durationSeconds": 7.353916680000009,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "11cf4204-914a-4e47-b383-2008a8a52ca0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T21:03:59.581Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EcNrcGdL5K6uAMgThC4mXh`</summary>

```json
{
  "query": "Farrell et al 2024 \"zero ablation\" SAE features knowledge unlearning negative scaling arXiv:2410.19278"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16933d41-323b-4b3d-8fb0-3b90760283a6",
  "isSidechain": false,
  "requestId": "req_011CbCc4jWobrML4V81j54wu",
  "type": "assistant",
  "uuid": "dac4adf2-3dce-411d-8056-2fc807f05035",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167Ds3GRRCYyRnvQWKNKar9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 32324,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 32324,
          "cache_creation_input_tokens": 1207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1207
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

_source line 44 · 2026-05-19T21:04:06.138Z_

<details><summary>↩ Tool result · `toolu_01EcNrcGdL5K6uAMgThC4mXh`</summary>

```text
Web search results for query: "Farrell et al 2024 "zero ablation" SAE features knowledge unlearning negative scaling arXiv:2410.19278"

Links: [{"title":"[2410.19278] Applying sparse autoencoders to unlearn knowledge in language models","url":"https://arxiv.org/abs/2410.19278"},{"title":"SAEs Can Improve Unlearning: Dynamic Sparse Autoencoder Guardrails for Precision Unlearning in LLMs","url":"https://arxiv.org/html/2504.08192v1"},{"title":"SAeUron: Interpretable Concept Unlearning in Diffusion Models with Sparse Autoencoders","url":"https://arxiv.org/html/2501.18052v2"},{"title":"Applying sparse autoencoders to unlearn knowledge in language models","url":"https://arxiv.org/html/2410.19278"},{"title":"Applying sparse autoencoders to unlearn knowledge in language models","url":"https://arxiv.org/pdf/2410.19278"},{"title":"Preprint. Under review. SAEs Can Improve Unlearning: Dynamic Sparse Autoencoder","url":"https://arxiv.org/pdf/2504.08192"},{"title":"Model Unlearning via Sparse Autoencoder Subspace Guided Projections","url":"https://arxiv.org/pdf/2505.24428"},{"title":"Don't Forget It! Conditional Sparse Autoencoder Clamping Works for   Unlearning","url":"https://arxiv.org/pdf/2503.11127"}]

I found the paper! Here's information about the Farrell et al. 2024 research:

## Paper Overview

The paper investigates whether sparse autoencoders (SAEs) can be used to remove knowledge from language models. The authors use the biology subset of the Weapons of Mass Destruction Proxy dataset and test on the gemma-2b-it and gemma-2-2b-it language models.

## Key Findings on Zero Ablation and Negative Scaling

Your query specifically mentions zero ablation and negative scaling findings. The results suggest that negative scaling of feature activations is necessary and that zero ablating features is ineffective.

## Results

The researchers demonstrate that individual interpretable biology-related SAE features can be used to unlearn a subset of WMDP-Bio questions with minimal side-effects in domains other than biology. However, intervening using multiple SAE features simultaneously can unlearn multiple different topics, but with similar or larger unwanted side-effects than the existing Representation Misdirection for Unlearning technique. Current SAE quality or intervention techniques would need to improve to make SAE-based unlearning comparable to the existing fine-tuning based techniques.

The paper was published in November 2024 and presented at the NeurIPS 2024 Safe Generative AI Workshop.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dac4adf2-3dce-411d-8056-2fc807f05035",
  "isSidechain": false,
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "1b95a777-ed8d-464e-8a72-63ad11ef5c00",
  "toolUseResult": {
    "query": "Farrell et al 2024 \"zero ablation\" SAE features knowledge unlearning negative scaling arXiv:2410.19278",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RuwwYfX1uLy4x9ecPmeAdS",
        "content": [
          {
            "title": "[2410.19278] Applying sparse autoencoders to unlearn knowledge in language models",
            "url": "https://arxiv.org/abs/2410.19278"
          },
          {
            "title": "SAEs Can Improve Unlearning: Dynamic Sparse Autoencoder Guardrails for Precision Unlearning in LLMs",
            "url": "https://arxiv.org/html/2504.08192v1"
          },
          {
            "title": "SAeUron: Interpretable Concept Unlearning in Diffusion Models with Sparse Autoencoders",
            "url": "https://arxiv.org/html/2501.18052v2"
          },
          {
            "title": "Applying sparse autoencoders to unlearn knowledge in language models",
            "url": "https://arxiv.org/html/2410.19278"
          },
          {
            "title": "Applying sparse autoencoders to unlearn knowledge in language models",
            "url": "https://arxiv.org/pdf/2410.19278"
          },
          {
            "title": "Preprint. Under review. SAEs Can Improve Unlearning: Dynamic Sparse Autoencoder",
            "url": "https://arxiv.org/pdf/2504.08192"
          },
          {
            "title": "Model Unlearning via Sparse Autoencoder Subspace Guided Projections",
            "url": "https://arxiv.org/pdf/2505.24428"
          },
          {
            "title": "Don't Forget It! Conditional Sparse Autoencoder Clamping Works for   Unlearning",
            "url": "https://arxiv.org/pdf/2503.11127"
          }
        ]
      },
      "I found the paper! Here's information about the Farrell et al. 2024 research:\n\n## Paper Overview\n\nThe paper investigates whether sparse autoencoders (SAEs) can be used to remove knowledge from language models. The authors use the biology subset of the Weapons of Mass Destruction Proxy dataset and test on the gemma-2b-it and gemma-2-2b-it language models.\n\n## Key Findings on Zero Ablation and Negative Scaling\n\nYour query specifically mentions zero ablation and negative scaling findings. The results suggest that negative scaling of feature activations is necessary and that zero ablating features is ineffective.\n\n## Results\n\nThe researchers demonstrate that individual interpretable biology-related SAE features can be used to unlearn a subset of WMDP-Bio questions with minimal side-effects in domains other than biology. However, intervening using multiple SAE features simultaneously can unlearn multiple different topics, but with similar or larger unwanted side-effects than the existing Representation Misdirection for Unlearning technique. Current SAE quality or intervention techniques would need to improve to make SAE-based unlearning comparable to the existing fine-tuning based techniques.\n\nThe paper was published in November 2024 and presented at the NeurIPS 2024 Safe Generative AI Workshop."
    ],
    "durationSeconds": 6.552513768999983,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dac4adf2-3dce-411d-8056-2fc807f05035",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T21:04:08.975Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JQTgTCA4EPvw72gDkd5As1`</summary>

```json
{
  "query": "CoRL 2026 conference robot learning submission topics call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b95a777-ed8d-464e-8a72-63ad11ef5c00",
  "isSidechain": false,
  "requestId": "req_011CbCc5To2mYxV8EhP5w9WG",
  "type": "assistant",
  "uuid": "4289a151-18c3-4ff6-b16e-6c3f6b8186d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbLK9yG1FXh9vbePyAyHdS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 33531,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 33531,
          "cache_creation_input_tokens": 801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 801
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

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation  ## Description Current c…",
  "leafUuid": "4289a151-18c3-4ff6-b16e-6c3f6b8186d9",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE feature decomposition for cross-lingual knowledge editing",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd"
}
```

---

### Tool result

_source line 48 · 2026-05-19T21:04:14.882Z_

<details><summary>↩ Tool result · `toolu_01JQTgTCA4EPvw72gDkd5As1`</summary>

```text
Web search results for query: "CoRL 2026 conference robot learning submission topics call for papers"

Links: [{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models","url":"https://arxiv.org/pdf/2512.11908"}]

Based on the search results, here's what I found about CoRL 2026:

## Conference Details

CoRL (Conference on Robot Learning) is an annual international conference focusing on the intersection of robotics and machine learning. CoRL 2026 will be held in Austin, Texas, US. More specifically, workshops and tutorials will be held in-person at the JW Marriott Austin on November 9th, 2026, with the main conference running November 10–12, 2026.

## Submission Deadlines

Abstract submission deadline is May 26, 2026 at 11:59 UTC and paper submission deadline is May 29, 2026 at 11:59 UTC.

## Paper Submission Topics and Requirements

Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.

Topics include video models and latent world models for robot learning. Additionally, all submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments.

Papers may be submitted through OpenReview.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4289a151-18c3-4ff6-b16e-6c3f6b8186d9",
  "isSidechain": false,
  "promptId": "850f203e-7bdd-4d15-889c-90b3e4a978a0",
  "type": "user",
  "uuid": "60da5885-4c19-4410-be89-3db56cb1b1cf",
  "toolUseResult": {
    "query": "CoRL 2026 conference robot learning submission topics call for papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_017XhUKewTEfAcomLeohyu93",
        "content": [
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf?lang=en"
          },
          {
            "title": "CoRL 2026 - Call for Workshops",
            "url": "https://www.corl.org/contributions/call-for-workshops"
          },
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
          },
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models",
            "url": "https://arxiv.org/pdf/2512.11908"
          }
        ]
      },
      "Based on the search results, here's what I found about CoRL 2026:\n\n## Conference Details\n\nCoRL (Conference on Robot Learning) is an annual international conference focusing on the intersection of robotics and machine learning. CoRL 2026 will be held in Austin, Texas, US. More specifically, workshops and tutorials will be held in-person at the JW Marriott Austin on November 9th, 2026, with the main conference running November 10–12, 2026.\n\n## Submission Deadlines\n\nAbstract submission deadline is May 26, 2026 at 11:59 UTC and paper submission deadline is May 29, 2026 at 11:59 UTC.\n\n## Paper Submission Topics and Requirements\n\nSubmissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\n\nTopics include video models and latent world models for robot learning. Additionally, all submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments.\n\nPapers may be submitted through OpenReview."
    ],
    "durationSeconds": 5.904032093999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4289a151-18c3-4ff6-b16e-6c3f6b8186d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-19T21:05:02.512Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a critical piece of information: **CoRL 2026 is the Conference on Robot Learning**, and this proposal is about cross-lingual knowledge editing using SAEs — a purely NLP/computational linguistics topic. This is a **fundamental venue mismatch**. CoRL explicitly requires "submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics." This proposal has absolutely nothing to do with robotics.

This is a fatal issue that needs to be flagged immediately. The proposal would be desk-rejected at CoRL regardless of its quality.
 
Wait, let me reconsider. The user's instructions specifically ask for evaluation at CoRL 2026, and the evaluation rubric includes dimensions like "NLP/CL领域的影响力" — impact in the NLP/CL field. This suggests either the template is generic or there's a mismatch in what the user is asking for. But they were explicit about CoRL. I suspect this is likely a user error — they may have meant to submit to an NLP conference instead, or they're confused about what CoRL actually is.

I should flag this venue mismatch clearly as a primary concern, then proceed to evaluate the proposal's quality assuming it would be submitted to an appropriate NLP venue like ACL, EMNLP, or NAACL. Looking at the actual proposal now, the field of cross-lingual knowledge editing is quite active with recent work in this space, and I'm starting to review the key contributions and related research to assess its merit. The novelty here is really in the combination—while SAE features for editing, language-specific feature classification, and adaptive scaling all exist independently in recent work, putting them together to handle cross-lingual knowledge editing is the new contribution. Each individual component draws from established papers, but the integrated approach hasn't been explored yet.

That said, there are simpler alternatives that might work just as well: I could apply LangSAE's language removal directly to edit vectors, or adapt FeatureEdit's existing cross-lingual approach without the full FCE pipeline. The core innovation—using activation contrasts to classify features and then adaptively scale them—is methodologically sound but fairly straightforward given what's already out there.

The deeper issue is whether the premise actually holds up. The hypothesis assumes polysemantic entanglement is the bottleneck, but there's competing evidence that portability failures might stem from reasoning ability rather than knowledge representation. Even if SAE features do separate language identity from relational structure better than neurons, prior work suggests SAE features themselves aren't truly atomic or canonical—so the continuous basis and adaptive λ workaround feels like it's papering over a fundamental limitation. And if the real bottleneck is in the model's reasoning process rather than its representations, then no amount of representation-level manipulation will solve it.

On the empirical side, positive results would be somewhat expected—moving from coarse neurons to finer SAE features for cross-lingual editing is the natural next step to try, so the surprise factor is moderate. Negative results would require exceptionally deep analysis to be publishable at a top venue. There's also a venue mismatch: this is a pure NLP paper being proposed for CoRL, which focuses on robot learning, so it would likely face desk rejection.

The proposal is intellectually mature and addresses known objections thoroughly, but that rigor doesn't increase the novelty of the core idea. The real risk is whether the portability bottleneck actually stems from polysemantic entanglement—if not, the entire approach falls apart. For an NLP venue like ACL or EMNLP, I'd estimate the acceptance probability at 25-35%, with novelty and significance both moderate, though the related work coverage is strong. For CoRL, it's essentially zero due to the fundamental venue mismatch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60da5885-4c19-4410-be89-3db56cb1b1cf",
  "isSidechain": false,
  "requestId": "req_011CbCc67DYrdXiH8AzpAYoe",
  "type": "assistant",
  "uuid": "06be8e58-c9c4-4a69-89b2-d70b47868e71",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01938ncZ2AV2hwqRvTdpiHmA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 34332,
      "output_tokens": 7680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7680,
          "cache_read_input_tokens": 34332,
          "cache_creation_input_tokens": 701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 701
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

_source line 50 · 2026-05-19T21:07:02.587Z_

Now I have comprehensive search results. Let me compile the full evaluation.

---

```
【阶段】: Triage
```

## ⚠️ 致命前置问题：venue 完全不匹配

**CoRL (Conference on Robot Learning) 2026 明确要求 "Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics."** 本 proposal 是纯 NLP/interpretability 工作（跨语言知识编辑 + SAE 特征分解），与 robotics 零关联。投 CoRL **会被直接 desk reject**，中稿概率实质为 0%。

以下评估假设投稿目标为 **NLP/CL 主会**（如 ACL/EMNLP/NAACL），以客观评价 idea 本身的质量。

---

```
【领域调研】:
```

- **LU-LAFNs** (COLING 2025, arXiv:2406.16416): 最直接的先驱。通过激活频率交集识别 language-agnostic factual neurons，在 Bi-ZsRE 上达到 77.87 avg (bloomz-7b1-mt)。但 67.9% 的 neurons 被标记为 LAFNs（极粗粒度），且**所有方法** portability EM < 10，作者自己承认这是 universal failure。
  - [ACL Anthology](https://aclanthology.org/2025.coling-main.385/)

- **FeatureEdit / The Knowledge Microscope** (ACL 2025, arXiv:2502.12483): 首个用 SAE feature 做 model editing 的工作。在 PrivacyParaRel 隐私擦除任务上，feature 优于 neuron (~0.80 vs ~0.65 reliability, ~0.70 vs ~0.25 generalization)。但仅限单语英文的知识擦除，非 factual editing 或 cross-lingual。
  - [arXiv PDF](https://arxiv.org/pdf/2502.12483)

- **CLM-Bench** (arXiv 2026, arXiv:2601.17397): 提供了中英编辑向量近乎正交的几何证据，解释了 ROME/MEMIT 跨语言失效（~20% reliability）。1,010 对中文文化知识-英文对照。
  - [arXiv](https://arxiv.org/abs/2601.17397)

- **LangSAE Editing** (arXiv 2026, arXiv:2601.04768): 用 SAE 特征抑制移除嵌入中的语言身份信号，跨语言检索 +21.9% nDCG@20。方法论上与本 proposal 的"SAE 移除语言特征"高度相关，但应用于 retrieval 而非 editing。
  - [arXiv](https://arxiv.org/abs/2601.04768)

- **SAE-LAPE / LangFIR** (ACL 2025 / arXiv 2026, arXiv:2604.03532): 用 activation-probability contrasts 发现语言特定 SAE 特征。**proposal 的 feature classification 方法直接沿用此方法论。**
  - [arXiv](https://arxiv.org/abs/2604.03532)

- **Chou et al.** (ACL SRW 2025, arXiv:2507.13410): 修改 Gemma-2B/9B 的单个 SAE 特征即可达到 90% 语言 steering 成功率，是 SAE 语言操控可行性的直接证据。
  - [arXiv](https://arxiv.org/abs/2507.13410)

- **Mondal et al.** (NAACL 2025 Insights Workshop, arXiv:2503.17456): 独立证明 neuron-level 语言特定干预不足以实现 cross-lingual transfer（在 XNLI/XQuAD 上测试）。
  - [ACL Anthology](https://aclanthology.org/2025.insights-1.6/)

- **SCAN** (arXiv 2026, arXiv:2603.15226): 用 sparse transcoders 做 lifelong editing，在 Qwen3/Llama3.1 上 3000 次连续编辑后仍保持模型完整性。但解决的是 sequential stability，非 cross-lingual。
  - [arXiv PDF](https://arxiv.org/pdf/2603.15226)

- **Merging Methods for MKE** (arXiv 2026, arXiv:2605.13919): 2026年5月最新工作。探索向量 merging + shared covariance 在12语言上做 batch editing，但无 representation-level decomposition。
  - [arXiv](https://arxiv.org/abs/2605.13919)

- **Peng et al.** (arXiv 2025, arXiv:2506.23845): 对 SAE 干预的核心质疑——SAEs 适合发现概念，不适合对已知概念做干预，steering 不如 prompting/fine-tuning。
  - [arXiv](https://arxiv.org/html/2506.23845v1)

- **Arad et al.** (EMNLP 2025, arXiv:2505.20063): 对 Peng et al. 的直接反驳——output-score filtering 使 SAE steering 提升 2-3×，匹配 supervised 方法。
  - [arXiv](https://arxiv.org/html/2505.20063v1)

- **Leask et al.** (ICLR 2025, arXiv:2502.04878): SAE features 既不 atomic 也不 canonical——meta-SAE 可将 latent 分解为子成分。建议按任务选择 dictionary size。
  - [ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/84ca3f2d9d9bfca13f69b48ea63eb4a5-Abstract-Conference.html)

- **Farrell et al.** (NeurIPS 2024 SafeGenAI, arXiv:2410.19278): SAE feature 的 zero ablation 对知识遗忘无效，需要 negative scaling。
  - [arXiv](https://arxiv.org/abs/2410.19278)

- **Qwen-Scope** (arXiv 2026, arXiv:2605.11887): Qwen3/3.5 上的预训练 SAE 套件，14 组 SAE 权重。Proposal 计划直接使用。
  - [arXiv](https://arxiv.org/abs/2605.11887)

- **SSPU** (EMNLP 2025, arXiv:2505.24428): SAE-guided subspace projection + QR 分解做知识遗忘。方法论与本 proposal 的 projection 思路有相似之处。

**调研总结**: 跨语言知识编辑是一个活跃且公认未解的问题，portability 是所有方法的共同瓶颈（EM < 10）。SAE 在语言特征操控（LangSAE, Chou et al., SAE-LAPE）和知识编辑（FeatureEdit, SCAN）上分别有了初步成功，但**尚无工作将 SAE feature 分解应用于跨语言知识编辑**。本 proposal 填的是一个"自然组合"的空白——各组件（SAE feature classification, language feature suppression, adaptive scaling）均已独立存在，proposal 的核心贡献是将它们组合并针对 cross-lingual editing portability 问题进行工程化。

---

```
【Trivial Alternative 检验】:
```

**存在明显的 trivial alternative 威胁。** 

最简单的竞争方案：直接将 LangSAE 的语言身份移除方法（已在 retrieval 上验证有效）应用于 edit vectors——用 activation-probability contrasts（SAE-LAPE 现成方法）分类特征，然后按 Farrell et al. 的发现做 negative scaling 而非 zero ablation。这个方案的成本远低于本 proposal 的完整 FCE pipeline，且可能达到类似效果。

本 proposal 相对于这个 trivial alternative 的增量价值在于 **FCE-based adaptive λ-projection**：声称通过度量每个 language-specific feature 的 factual causal effect，可以更精确地保留高 factual content 的 features。但这个增量价值有两个不确定性：
1. FCE 和简单 thresholding 之间的性能差距可能很小（如果大多数 language-specific features 的 FCE 本身就很低，即 factual 和 language 本身就是比较分离的，那 adaptive λ 就退化为 binary removal）
2. 整个 pipeline 的复杂度（两阶段 screening + per-feature ablation + bootstrap CI）是否值得相对于 simple suppression 的边际增益

**增量价值存在但有限，且未经验证。**

---

```
【前提假设检验】:
```

核心 claim 的逻辑链条如下，标注每个环节的假设强度：

1. **"Portability 瓶颈源于 polysemantic neurons 将 factual 和 language 信息纠缠"** — ⚠️ **这是最关键的未验证假设**。LU-LAFNs 作者自己给出了**替代解释**："portability 指标可能测量的是推理能力，而非知识迁移"。如果 portability 低是因为模型缺乏跨语言推理链（而非表征层面的纠缠），那么任何 representation-level 的操控都无法改善它。本 proposal 承认了这个风险（Risk mitigation 部分），但它仍然是整个工作成败的前提。

2. **"SAE features 能比 neurons 更干净地分离 factual vs. language 成分"** — 部分有据。FeatureEdit 在知识擦除上验证了 features > neurons，LangSAE/SAE-LAPE 验证了 SAE 可以分离语言特征。但 **从"更好的分离"到"更好的 portability"** 的推理环节缺少证据——这正是 proposal 要验证的，但也意味着如果 portability 瓶颈不在表征分离上，这步推理就断裂。

3. **"FCE-based adaptive projection 优于 simple binary removal"** — 合理但未验证。Farrell et al. 的 finding（negative scaling > zero ablation）支持非二值操作的方向，但 proposal 的 adaptive λ 方案与 Farrell et al. 的 negative scaling 在机制上并不相同。

4. **"Pre-trained SAEs（Qwen-Scope, Llama Scope）的重建质量足以保留 edit vector 的有效性"** — 实证假设，proposal 安排了 Phase 3 验证，是合理的风控设计。但如果重建质量不足（这是有可能的——edit vectors 是高精度方向向量，SAE 的 reconstruction error 可能对此敏感），整个方法就不可行。

**总结：逻辑链的最弱环节是假设 1——portability 瓶颈的归因。如果瓶颈不在 polysemantic entanglement 而在 reasoning capability，整个 idea 的理论基础就不成立。**

---

```
【3 维度打分】:
```

### 1. Novelty: 中偏弱 (Moderate-Weak)

**理由：**

本工作的核心贡献是"首次将 SAE feature 分解应用于跨语言知识编辑"——这是一个**组合性 novelty**，各组件均已独立存在：

- SAE features → knowledge editing：FeatureEdit (ACL 2025) 已开此先河（虽然是 erasure 而非 cross-lingual editing）
- SAE → 语言特征分离：SAE-LAPE (ACL 2025), LangSAE (2026), LangFIR (2026) 已有成熟方法
- SAE → 语言 steering：Chou et al. (2025) 已验证可行性
- Soft/adaptive scaling vs binary：Farrell et al. (2024) 已指出方向
- Output-score feature selection：Arad et al. (EMNLP 2025) 已提出

Proposal 的主要方法论增量是 **FCE metric + adaptive λ-projection**，这是一个合理的工程设计，但并非深刻的方法论创新。它本质上是：先用 ablation study 估算每个 feature 的 factual importance，然后按 importance 加权做 projection。这个思路在 representation engineering 中是相当标准的。

**"如果这个组合是 obvious next step，为什么没人做"** 的反问有一定说服力——确实没人做过。但这也可能是因为：(a) timing（各组件在 2025-2026 才成熟），(b) community 规模小（跨语言 editing 本身是 niche 方向），(c) 领域内的人可能在并行探索类似方向（如 Merging Methods for MKE 在2026年5月刚出，说明这个领域非常活跃）。

### 2. Significance: 中 (Moderate)

**理由：**

**问题本身是重要的**：cross-lingual knowledge editing 的 portability 瓶颈是领域内公认的 open problem（所有方法 EM < 10，LU-LAFNs 论文和 survey arXiv:2505.14393 均确认）。如果能突破这个瓶颈，对多语言 LLM 的事实更新有实际价值。

**但影响力受限于**：
- 跨语言知识编辑本身是 niche 方向（相比于通用 model editing 或多语言 NLP）
- 如果 positive result 出来，审稿人可能会说 **"this is the natural thing to try — moving from neurons to features is an obvious granularity upgrade"**。它不会是 "surprising, not what I expected"，而更可能是 "well, this confirms what we would have predicted"。
- 即使 portability 有所提升，如果提升幅度有限（比如 EM 从 <10 提升到 15-20），审稿人可能认为 bottleneck 仍未真正突破
- 作为 negative result 发表（falsification of polysemanticity hypothesis）的价值取决于分析深度，但 negative results 在主会的接受门槛更高

### 3. Related Work: 强 (Strong)

**理由：**

这是 proposal 最强的维度。Related work 覆盖极为全面：
- 覆盖了3个层面的现有工作（direct editing baselines, neuron-level approaches, SAE-based methods）
- **主动对抗了 SAE intervention skepticism**（Peng et al., Leask et al.），并引用了具体的 rebuttal 工作（Arad et al., Zhao et al.）
- 准确区分了 FeatureEdit 的适用范围（privacy erasure ≠ factual editing ≠ cross-lingual）
- 引用的论文经调研验证**均真实存在、描述准确**（LU-LAFNs → COLING 2025 确认，Mondal et al. → NAACL 2025 Insights 确认，Leask et al. → ICLR 2025 确认，Qwen-Scope → arXiv 2026 确认，Chou et al. → ACL SRW 2025 确认）
- 差异化定位清晰（明确说明了与 FeatureEdit、LangSAE、SCAN 等工作的区别）

---

```
【概率估计】: 20% - 30%，中位 25%
```

（注意：此概率假设投稿至 NLP 主会如 ACL/EMNLP。若投 CoRL 2026，概率为 ~0%，因 venue 完全不匹配。）

```
【估计理由】:
```

**从 3 维度到概率的推理：**

- **Related Work（强）** 保障了项目的下限——审稿人不会因为 "miss important related work" 或 "overstate novelty" 而直接拒。这使概率不会跌到 15% 以下。

- **Novelty（中偏弱）** 是限制上限的核心因素。作为一个 "natural combination" 工作，审稿人最可能的评价是："well-executed but incremental — the individual pieces all exist, and the combination is the expected next step." 这类工作在 ACL/EMNLP 主会的接受率通常在 25% 左右，取决于实验结果的说服力。

- **Significance（中）** 居中，不加分也不扣分。问题确实重要但方向不是 surprising 的。如果 positive result 是 "SAE features improve portability from EM 5 → EM 25"，那 significance 会上升到"中偏强"。但这取决于实验结果，入口评估不能预期。

**上界受限于 Novelty**：即使实验完美执行，idea 的组合性质使其很难获得 "strong accept"。预期最好的 reviewer 评分分布是 2个 borderline accept + 1个 weak reject，这对应 ~30% 的 acceptance probability。

**下界由 Related Work 和问题的合理性保障**：proposal 的 intellectual rigor 明显高于平均，dual-outcome design 和 risk mitigation 设计成熟。即使 novelty 偏弱，至少不会被认为是 sloppy work。

```
【主要风险】:
```

1. **核心假设风险**（idea 层面）：Portability 瓶颈可能并非源于 polysemantic entanglement，而是源于模型缺乏跨语言推理能力——如果是后者，任何 representation-level manipulation（包括 SAE-based）都无法改善 portability，整个 idea 的理论基础就不成立。LU-LAFNs 作者自己提出了这个替代解释，审稿人很可能也会抓住这一点。

2. **"Natural next step" 质疑**（novelty 层面）：审稿人可能会认为 "从 neurons 升级到 SAE features 做跨语言编辑" 是一个显而易见的下一步，尤其在 FeatureEdit、LangSAE、SAE-LAPE 等工作都已存在的情况下。如果实验结果只是 moderate improvement，reviewer 会判定 "contribution insufficient for a top venue."

---

Sources:
- [LU-LAFNs (COLING 2025)](https://aclanthology.org/2025.coling-main.385/)
- [FeatureEdit / Knowledge Microscope (ACL 2025)](https://arxiv.org/pdf/2502.12483)
- [CLM-Bench (arXiv 2026)](https://arxiv.org/abs/2601.17397)
- [LangSAE Editing (arXiv 2026)](https://arxiv.org/abs/2601.04768)
- [SAE-LAPE (ACL 2025)](https://aclanthology.org/2025.acl-long.229/)
- [Mondal et al. (NAACL 2025 Insights)](https://aclanthology.org/2025.insights-1.6/)
- [Chou et al. (ACL SRW 2025)](https://arxiv.org/abs/2507.13410)
- [Peng et al. (arXiv 2025)](https://arxiv.org/html/2506.23845v1)
- [Arad et al. (EMNLP 2025)](https://arxiv.org/html/2505.20063v1)
- [Leask et al. (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/hash/84ca3f2d9d9bfca13f69b48ea63eb4a5-Abstract-Conference.html)
- [Farrell et al. (NeurIPS 2024 SafeGenAI)](https://arxiv.org/abs/2410.19278)
- [SCAN (arXiv 2026)](https://arxiv.org/pdf/2603.15226)
- [Merging Methods for MKE (arXiv 2026)](https://arxiv.org/abs/2605.13919)
- [Qwen-Scope (arXiv 2026)](https://arxiv.org/abs/2605.11887)
- [Editing Across Languages Survey (arXiv 2025)](https://arxiv.org/html/2505.14393)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06be8e58-c9c4-4a69-89b2-d70b47868e71",
  "isSidechain": false,
  "requestId": "req_011CbCc67DYrdXiH8AzpAYoe",
  "type": "assistant",
  "uuid": "2c22231d-9dbe-409c-92f2-91997c7e760f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01938ncZ2AV2hwqRvTdpiHmA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 34332,
      "output_tokens": 7680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7680,
          "cache_read_input_tokens": 34332,
          "cache_creation_input_tokens": 701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 701
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

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation  ## Description Current c…",
  "leafUuid": "2c22231d-9dbe-409c-92f2-91997c7e760f",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE feature decomposition for cross-lingual knowledge editing",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation  ## Description Current c…",
  "leafUuid": "2c22231d-9dbe-409c-92f2-91997c7e760f",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "SAE feature decomposition for cross-lingual knowledge editing",
  "sessionId": "a4ca4dc5-0609-48fb-b362-0d3efdc3eccd"
}
```

---
