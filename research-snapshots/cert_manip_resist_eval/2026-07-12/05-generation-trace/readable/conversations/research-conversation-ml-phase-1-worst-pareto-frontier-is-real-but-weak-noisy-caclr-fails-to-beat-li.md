# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Pareto frontier is real but weak/noisy. CaCLR fails to beat linear projecti

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/f77c5807-10e5-4eae-ab8e-381ef798b6e6.jsonl`
- **Structured JSON:** [`9d30c595f1dd1c1856e8.json`](../../sessions/9d/9d30c595f1dd1c1856e8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:17:54.877Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:17:54.877Z",
  "sessionId": "f77c5807-10e5-4eae-ab8e-381ef798b6e6",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Pareto frontier is real but weak/noisy. CaCLR fails to beat linear projection. Decomposition doesn't cleanly separate. Core method contribution collapses. But the large-scale empirical characterization (2 models × 20 languages × all layers) and the negative results on CaCLR/mean-shift are themselves publishable — reframe as a diagnostic/field-test paper.\n核心假设：['Pareto frontier is flat or non-monotonic on one architecture (e.g., Llama4 shows no clear depth-transfer tradeoff), only partially replicates from MVP', 'CaCLR underperforms or matches linear projection across the board; consistency loss term adds no value or hurts', \"Difficulty-capability decomposition fails: projecting out difficulty doesn't meaningfully change transfer, or difficulty and capability directions are not separable\", 'Orthogonality holds but reviewers may see it as a replication of Miao & Ungar extended to 20 langs — incremental', 'Zero-shot transfer fails for >40% of languages (AUROC < 0.60), suggesting probe-based calibration has a language barrier']\n关键指标范围：{'en_auroc_best_layer': [0.73, 0.8], 'zs_transfer_auroc_mean_19lang': [0.57, 0.66], 'zs_transfer_drop_mean_pp': [14, 25], 'caclr_vs_linproj_auroc_delta_pp': [-1.5, 0.5], 'caclr_ece_reduction_vs_tempcal_pct': [0, 12], 'pareto_depth_transfer_rank_corr': [0.15, 0.5], 'decomp_difficulty_var_explained_pct': [5, 25], 'orthogonality_cosine_mean': [0.03, 0.12], 'low_resource_zs_pass_rate': [0.1, 0.4], 'caclr_improvement_pass_rate': [0.3, 0.55], 'pareto_frontier_agreement_across_arch': [0.2, 0.55]}\n叙事方向：Full reframe to field-level diagnostic paper: 'Does probe-based calibration work beyond English? A systematic study across 2 architectures and 20 languages.' The value proposition shifts from 'here is a method' to 'here is the first large-scale answer to whether this research line generalizes.' Key findings become: (1) probe-based correctness signals exist multilingually but transfer is unreliable — architecture, language family, and resource tier all modulate success in unpredictable ways; (2) simple alignment methods (linear projection, few-shot) match or beat more principled approaches (CaCLR) — the signal is too noisy for sophisticated invariance objectives to help; (3) mean-shift completely fails (confirmed at scale beyond MVP); (4) difficulty and capability are entangled in cross-lingual representations, unlike the clean separation assumed by prior English-only work. Frame CaCLR ablation as a rigorous negative result that saves the community from pursuing consistency-based objectives for this problem. Lean into Claim 4 (orthogonality persists cross-lingually → output-based calibration is structurally limited everywhere, not just English) as the one mechanistic takeaway. Still targets EACL — negative/diagnostic results at this scale and rigor are valuable, especially when the field is actively expanding probe-based methods without multilingual validation.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: xling_calib_direction\nfocus: Core submission for EACL 2027 ARR: 2 models (Qwen3-235B + Llama 4 Scout) × 20 languages. Key risks: (1) CaCLR may not outperform simple linear projection; (2) difficulty-shared vs capability-specific decomposition may not cleanly separate; (3) orthogonality claim 4 may be seen as incremental. MVP showed mean-shift completely fails, Pareto tradeoff directly observed at L24 vs L27.\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) shifts the Pareto frontier by jointly optimizing calibration and cross-lingual invariance, enabling effective probe transfer at deeper, better-calibrated layers without target-language correctness labels.\n- MVP evidence: Mean-shift fails entirely (0/5 languages improved) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, and propose CaCLR to shift the frontier. This is both a field-level viability test and a practical method contribution.\n- **Headline template**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak\"** → 5 transfer conditions tested. Mean-shift failure (MVP-confirmed) motivates CaCLR. Mean-shift works for Xiao et al.'s knowledge boundary but fails for correctness — important finding.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR).\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request.\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    INT8 weight quantization.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: Needs 2× RTX 6000 PRO 96GB at INT8.\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency. Train CaCLR probes using English labels + unlabeled\n    parallel activations. Compare vs zero-shot, mean-shift, linear projection, few-shot\n    (25/100) across full Pareto frontier for both models × 20 languages. Hyperparameter\n    tuning (α, β) on held-out English + 5-language validation.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021.\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: Need IRT difficulty scores from GlobalMMLU or external source.\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'INT8 validation ablation: compare INT8 vs FP16 probing results at\n    5 representative layers for Llama 4 Scout on 5% random subset. Validates that\n    INT8 quantization doesn''t distort correctness signals.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 31B Dense (60 layers, dense, FP16): third architecture for\n    camera-ready. Full Pareto frontier, 20+ languages. Provides dense vs MoE architectural\n    contrast.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: failed\n  metrics:\n    bug: layer_config_mismatch\n    detail: extract_activations.py used --layers 2,6,10,14,18,22,26 but train_probe.py\n      and transfer_eval.py used default layers 0,4,8,12,16,20,24,28,31. Probe training\n      skipped all layers (activation files not found). Activations (42 files) are\n      valid and reusable.\n    fix: Add --layers 2,6,10,14,18,22,26 to train_probe.py and transfer_eval.py in\n      run_mvp_002.sh\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: RUNNING\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    bug: layer_config_mismatch\n    detail: extract_activations.py used --layers 2,6,10,14,18,22,26 but train_probe.py\n      and transfer_eval.py used default layers 0,4,8,12,16,20,24,28,31. Probe training\n      skipped all layers (activation files not found). Activations (42 files) are\n      valid and reusable.\n    fix: Add --layers 2,6,10,14,18,22,26 to train_probe.py and transfer_eval.py in\n      run_mvp_002.sh\n- exp_id: mvp_003\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T19:17:54.880Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:17:54.880Z",
  "sessionId": "f77c5807-10e5-4eae-ab8e-381ef798b6e6"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T19:17:54.914Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Pareto frontier is real but weak/noisy. CaCLR fails to beat linear projection. Decomposition doesn't cleanly separate. Core method contribution collapses. But the large-scale empirical characterization (2 models × 20 languages × all layers) and the negative results on CaCLR/mean-shift are themselves publishable — reframe as a diagnostic/field-test paper.
核心假设：['Pareto frontier is flat or non-monotonic on one architecture (e.g., Llama4 shows no clear depth-transfer tradeoff), only partially replicates from MVP', 'CaCLR underperforms or matches linear projection across the board; consistency loss term adds no value or hurts', "Difficulty-capability decomposition fails: projecting out difficulty doesn't meaningfully change transfer, or difficulty and capability directions are not separable", 'Orthogonality holds but reviewers may see it as a replication of Miao & Ungar extended to 20 langs — incremental', 'Zero-shot transfer fails for >40% of languages (AUROC < 0.60), suggesting probe-based calibration has a language barrier']
关键指标范围：{'en_auroc_best_layer': [0.73, 0.8], 'zs_transfer_auroc_mean_19lang': [0.57, 0.66], 'zs_transfer_drop_mean_pp': [14, 25], 'caclr_vs_linproj_auroc_delta_pp': [-1.5, 0.5], 'caclr_ece_reduction_vs_tempcal_pct': [0, 12], 'pareto_depth_transfer_rank_corr': [0.15, 0.5], 'decomp_difficulty_var_explained_pct': [5, 25], 'orthogonality_cosine_mean': [0.03, 0.12], 'low_resource_zs_pass_rate': [0.1, 0.4], 'caclr_improvement_pass_rate': [0.3, 0.55], 'pareto_frontier_agreement_across_arch': [0.2, 0.55]}
叙事方向：Full reframe to field-level diagnostic paper: 'Does probe-based calibration work beyond English? A systematic study across 2 architectures and 20 languages.' The value proposition shifts from 'here is a method' to 'here is the first large-scale answer to whether this research line generalizes.' Key findings become: (1) probe-based correctness signals exist multilingually but transfer is unreliable — architecture, language family, and resource tier all modulate success in unpredictable ways; (2) simple alignment methods (linear projection, few-shot) match or beat more principled approaches (CaCLR) — the signal is too noisy for sophisticated invariance objectives to help; (3) mean-shift completely fails (confirmed at scale beyond MVP); (4) difficulty and capability are entangled in cross-lingual representations, unlike the clean separation assumed by prior English-only work. Frame CaCLR ablation as a rigorous negative result that saves the community from pursuing consistency-based objectives for this problem. Lean into Claim 4 (orthogonality persists cross-lingually → output-based calibration is structurally limited everywhere, not just English) as the one mechanistic takeaway. Still targets EACL — negative/diagnostic results at this scale and rigor are valuable, especially when the field is actively expanding probe-based methods without multilingual validation.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: xling_calib_direction
focus: Core submission for EACL 2027 ARR: 2 models (Qwen3-235B + Llama 4 Scout) × 20 languages. Key risks: (1) CaCLR may not outperform simple linear projection; (2) difficulty-shared vs capability-specific decomposition may not cleanly separate; (3) orthogonality claim 4 may be seen as incremental. MVP showed mean-shift completely fails, Pareto tradeoff directly observed at L24 vs L27.

## paper_framing.md

# Paper Framing — xling_calib_direction

## Target Venue
- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
- Core submission: 2 models × 20 languages × all contributions
- Camera-ready extension: Gemma 4 31B Dense + 30+ languages

## Core Insight
The model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.

## Core Claims (4, causal chain)

### Claim 1 — Pareto Frontier (Discovery)
Cross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.
- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.
- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.

### Claim 2 — Decomposition (Analysis)
Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
- Evidence: IRT difficulty probes → project out → retrain → compare transfer.

### Claim 3 — CaCLR (Method)
CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) shifts the Pareto frontier by jointly optimizing calibration and cross-lingual invariance, enabling effective probe transfer at deeper, better-calibrated layers without target-language correctness labels.
- MVP evidence: Mean-shift fails entirely (0/5 languages improved) — motivates principled approach.
- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier.

### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)
The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.
- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.

## Story Spine
- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, and propose CaCLR to shift the frontier. This is both a field-level viability test and a practical method contribution.
- **Headline template**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."

## Field-Level Significance
This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.

## Anticipated Reviewer Concerns & Responses
1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier.
2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
3. **"Mean-shift too weak"** → 5 transfer conditions tested. Mean-shift failure (MVP-confirmed) motivates CaCLR. Mean-shift works for Xiao et al.'s knowledge boundary but fails for correctness — important finding.
4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.

## Differentiation from Closest Prior Work
| Paper | Their Focus | Our Difference |
|-------|-------------|----------------|
| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier |
| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |


## experiment_plan (with registry status)

- id: plan_001
  claim: 1
  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): extract
    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,
    train English correctness probes (logistic regression + 2-layer MLP), evaluate
    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,
    CaCLR).

    '
  priority: P0
  gpu_budget_hours: 80
  deps: []
  notes: Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request.
  status: planned
- id: plan_002
  claim: 1
  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): extract
    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.
    INT8 weight quantization.

    '
  priority: P0
  gpu_budget_hours: 40
  deps: []
  notes: Needs 2× RTX 6000 PRO 96GB at INT8.
  status: planned
- id: plan_003
  claim: 3
  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +
    α·L_SB-ECE + β·L_consistency. Train CaCLR probes using English labels + unlabeled
    parallel activations. Compare vs zero-shot, mean-shift, linear projection, few-shot
    (25/100) across full Pareto frontier for both models × 20 languages. Hyperparameter
    tuning (α, β) on held-out English + 5-language validation.

    '
  priority: P0
  gpu_budget_hours: 20
  deps:
  - plan_001
  - plan_002
  notes: CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS
    2021.
  status: planned
- id: plan_004
  claim: 2
  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge
    regression on human difficulty scores per Civelli et al.), project out difficulty
    direction from activations, retrain correctness probes on residuals, evaluate
    transfer. 10 representative languages × 8 representative layers per model (20-90%
    depth).

    '
  priority: P0
  gpu_budget_hours: 15
  deps:
  - plan_001
  - plan_002
  notes: Need IRT difficulty scores from GlobalMMLU or external source.
  status: planned
- id: plan_005
  claim: 4
  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence
    direction (prompt model for confidence score, fit probe), compute cosine similarity
    with correctness direction across 20 languages × 2 architectures. Analyze by resource
    tier (high/mid/low) and language family.

    '
  priority: P1
  gpu_budget_hours: 10
  deps:
  - plan_001
  - plan_002
  status: planned
- id: plan_006
  claim: 1
  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at
    each probed layer for both models. Compare English accuracy, cross-lingual transfer
    degradation, and calibration quality. Test hypothesis: linear probes transfer
    better cross-lingually.

    '
  priority: P1
  gpu_budget_hours: 5
  deps:
  - plan_001
  - plan_002
  notes: CPU-bound, uses cached activations.
  status: planned
- id: plan_007
  claim: 1
  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele
    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.

    '
  priority: P1
  gpu_budget_hours: 30
  deps:
  - plan_001
  - plan_002
  - plan_003
  status: planned
- id: plan_010
  claim: 1
  description: 'INT8 validation ablation: compare INT8 vs FP16 probing results at
    5 representative layers for Llama 4 Scout on 5% random subset. Validates that
    INT8 quantization doesn''t distort correctness signals.

    '
  priority: P1
  gpu_budget_hours: 5
  deps:
  - plan_002
  status: planned
- id: plan_008
  claim: 1
  description: 'Gemma 4 31B Dense (60 layers, dense, FP16): third architecture for
    camera-ready. Full Pareto frontier, 20+ languages. Provides dense vs MoE architectural
    contrast.

    '
  priority: P2
  gpu_budget_hours: 30
  deps: []
  status: planned
- id: plan_009
  claim: 1
  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.
    Leverages GlobalMMLU/Belebele full language sets.

    '
  priority: P2
  gpu_budget_hours: 50
  deps:
  - plan_001
  - plan_002
  status: planned
- id: mvp_validation
  claim: 1
  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'
  priority: P0
  registry_id: mvp_001
  gpu_budget_hours: 2
  deps: []
  status: DONE
  conclusion: success
  metrics:
    en_best_auroc: 0.7541
    en_best_layer: 27
    en_best_ece_raw: 0.1951
    en_best_ece_tempcal: 0.0744
    temp_scaling_T: 6.21
    en_auroc_range:
    - 0.6113
    - 0.7541
    layer_depth_delta: 0.1428
    layers_tested:
    - 0
    - 4
    - 8
    - 12
    - 16
    - 20
    - 24
    - 27
    zs_pass_langs:
    - zh
    - ar
    - hi
    - ko
    zs_fail_langs:
    - sw
    best_zs_auroc:
      zh: 0.686
      ar: 0.651
      hi: 0.652
      ko: 0.648
      sw: 0.56
    mean_shift_delta_ece:
      zh: -0.36
      ar: -0.06
      hi: 2.22
      sw: 6.44
      ko: 0.01
    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)
    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)
    p2: PASS (4/5)
    p3: PASS (14.28pp)
    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as
      naive baseline negative result)
- id: mvp_complementary
  claim: 1
  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'
  priority: P1
  registry_id: mvp_002
  gpu_budget_hours: 2
  deps:
  - mvp_validation
  status: DONE
  conclusion: failed
  metrics:
    bug: layer_config_mismatch
    detail: extract_activations.py used --layers 2,6,10,14,18,22,26 but train_probe.py
      and transfer_eval.py used default layers 0,4,8,12,16,20,24,28,31. Probe training
      skipped all layers (activation files not found). Activations (42 files) are
      valid and reusable.
    fix: Add --layers 2,6,10,14,18,22,26 to train_probe.py and transfer_eval.py in
      run_mvp_002.sh
- id: mvp_llama_control
  claim: 1
  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'
  priority: P1
  registry_id: mvp_003
  gpu_budget_hours: 3
  deps:
  - mvp_validation
  status: RUNNING


## registry (completed experiments)

- exp_id: mvp_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    en_best_auroc: 0.7541
    en_best_layer: 27
    en_best_ece_raw: 0.1951
    en_best_ece_tempcal: 0.0744
    temp_scaling_T: 6.21
    en_auroc_range:
    - 0.6113
    - 0.7541
    layer_depth_delta: 0.1428
    layers_tested:
    - 0
    - 4
    - 8
    - 12
    - 16
    - 20
    - 24
    - 27
    zs_pass_langs:
    - zh
    - ar
    - hi
    - ko
    zs_fail_langs:
    - sw
    best_zs_auroc:
      zh: 0.686
      ar: 0.651
      hi: 0.652
      ko: 0.648
      sw: 0.56
    mean_shift_delta_ece:
      zh: -0.36
      ar: -0.06
      hi: 2.22
      sw: 6.44
      ko: 0.01
    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)
    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)
    p2: PASS (4/5)
    p3: PASS (14.28pp)
    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as
      naive baseline negative result)
- exp_id: mvp_002
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    bug: layer_config_mismatch
    detail: extract_activations.py used --layers 2,6,10,14,18,22,26 but train_probe.py
      and transfer_eval.py used default layers 0,4,8,12,16,20,24,28,31. Probe training
      skipped all layers (activation files not found). Activations (42 files) are
      valid and reusable.
    fix: Add --layers 2,6,10,14,18,22,26 to train_probe.py and transfer_eval.py in
      run_mvp_002.sh
- exp_id: mvp_003
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: worst
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b2ce485f-a794-407b-bb74-9fe9b9f04c48",
  "type": "user",
  "uuid": "98168012-6d5a-483f-8533-7cbe6d848007",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f77c5807-10e5-4eae-ab8e-381ef798b6e6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:17:54.913Z_

```json
{
  "parentUuid": "98168012-6d5a-483f-8533-7cbe6d848007",
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
  "uuid": "9a5ca509-f0de-4a2b-93cf-04c00eacf1a1",
  "timestamp": "2026-05-20T19:17:54.913Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f77c5807-10e5-4eae-ab8e-381ef798b6e6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:17:54.913Z_

```json
{
  "parentUuid": "9a5ca509-f0de-4a2b-93cf-04c00eacf1a1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ba2c11b5-be33-49a6-b440-c54a3db9954f",
  "timestamp": "2026-05-20T19:17:54.913Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f77c5807-10e5-4eae-ab8e-381ef798b6e6",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Pareto frontier is real but weak/noisy. CaCLR fails to beat linear projection. Decomposition doesn't cleanly separate. Core method contribution collapses.…",
  "leafUuid": "ba2c11b5-be33-49a6-b440-c54a3db9954f",
  "sessionId": "f77c5807-10e5-4eae-ab8e-381ef798b6e6"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Multilingual probe calibration field diagnostic",
  "sessionId": "f77c5807-10e5-4eae-ab8e-381ef798b6e6"
}
```

---

### Assistant

_source line 8 · 2026-05-20T19:18:28.907Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for the "worst" tier scenario for each planned experiment in their experiment plan. I need to produce a single YAML block with all the predicted data, rationales, and analysis for each experiment.

Let me carefully go through each planned experiment and generate worst-tier predictions consistent with the defined worst-tier parameters.

Key worst-tier constraints:
- en_auroc_best_layer: [0.73, 0.8]
- zs_transfer_auroc_mean_19lang: [0.57, 0.66]
- zs_transfer_drop_mean_pp: [14, 25]


- caclr_vs_linproj_auroc_delta_pp: [-1.5, 0.5]
- caclr_ece_reduction_vs_tempcal_pct: [0, 12]
- pareto_depth_transfer_rank_corr: [0.15, 0.5]
- decomp_difficulty_var_explained_pct: [5, 25]
- orthogonality_cosine_mean: [0.03, 0.12]
- low_resource_zs_pass_rate: [0.1, 0.4]
- caclr_improvement_pass_rate: [0.3, 0.55]
- pareto_frontier

Now I'm working through the remaining worst-tier parameter ranges to ensure all experiments have consistent predictions within these bounds. _agreement_across_arch: [0.2, 0.55]

Narrative: Reframe as diagnostic/field-test paper. CaCLR fails to beat linear projection. Decomposition doesn't cleanly separate. Pareto frontier is weak/noisy. But large-scale characterization and negative results are publishable.

Looking at the experimental plans, most hit fundamental issues. The Pareto frontiers across both Qwen3 and Llama 4 are noisy or flat with poor agreement between architectures. CaCLR doesn't outperform simpler baselines, and the difficulty-capability decomposition doesn't hold up cleanly. Cross-lingual orthogonality is incremental, probe complexity gives mixed results, and generalization beyond GlobalMMLU is weak. The INT8 validation should at least pass as a sanity check.

For the remaining plans, I'm adding predictions for Gemma 4 31B and extended language coverage as secondary contributions. Now I need to work out realistic numbers for each experiment—thinking through what the actual results might look like given the model scales and transfer patterns I'm seeing.

For Qwen3-235B, I expect English AUROC around 0.78 since it's larger than the MVP baseline, but the worst-tier frontier will be noisy. Transfer drops significantly to a mean of 0.62 across languages, with only about a third passing the 0.65 threshold. Mean-shift fails as confirmed, linear projection helps modestly, and CaCLR doesn't improve much beyond that—the Pareto frontier exists but shows weak rank correlation around 0.35.

Llama 4 Scout presents a different challenge with its MoE architecture, likely producing a flatter or non-monotonic frontier. English performance sits lower at 0.75, transfer is worse than Qwen3, and architectural agreement on the frontier is poor. For CaCLR specifically, I'm seeing it underperform linear projection by about half a percentage point, though it does help pass rates reach 0.40—but consistency losses hurt certain languages, which complicates the overall picture.

Decomposing difficulty explains only 12% of variance and doesn't meaningfully shift transfer patterns, suggesting difficulty and capability aren't cleanly separable. Orthogonality across languages averages 0.07 cosine similarity with substantial noise, and resource tier modulation exists but inconsistently. Probe complexity shows minimal differences—MLPs edge out linear in English but transfer worse overall. Results partially hold on Belebele but degrade further on MMLU-ProX, and INT8 quantization appears equivalent to FP16 so that should validate cleanly.

Writing comprehensive YAML...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba2c11b5-be33-49a6-b440-c54a3db9954f",
  "isSidechain": false,
  "requestId": "req_011CbEMnjEcmpHfRArKSy91B",
  "type": "assistant",
  "uuid": "0e0c97fe-375b-49e2-842b-dbb3789c7000",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f77c5807-10e5-4eae-ab8e-381ef798b6e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BN4tHuPgfkEsHSVZLMJ181",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11006,
      "cache_read_input_tokens": 11841,
      "output_tokens": 18255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11006,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18255,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11006
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

_source line 9 · 2026-05-20T19:23:17.931Z_

```yaml
tier: worst
narrative_guidance: >
  Full reframe to field-level diagnostic paper: 'Does probe-based calibration work beyond English?
  A systematic study across 2 architectures and 20 languages.' Value proposition shifts from method
  contribution to first large-scale answer on whether this research line generalizes. CaCLR is
  reported as a rigorous negative result — consistency-based objectives do not help when the
  cross-lingual correctness signal is this noisy. Decomposition is reported as evidence that
  difficulty and capability are entangled in multilingual representations, contradicting the clean
  separation assumed by English-only prior work. Pareto frontier is real on Qwen3 but fails to
  replicate cleanly on Llama 4 Scout — reported as architecture-dependence finding rather than
  universal law. Orthogonality (Claim 4) survives as the one mechanistic takeaway: output-based
  calibration is structurally limited everywhere, not just English. Target EACL with framing that
  negative/diagnostic results at this scale (2 models × 20 languages × all layers) are
  community-valuable when the field is actively expanding probe-based methods without multilingual
  validation.

imagined_experiments:

  # ============================================================
  # plan_001 — Full Pareto Frontier, Qwen3-235B-A22B
  # ============================================================
  - name: "Full Pareto Frontier — Qwen3-235B-A22B (94 layers, MoE, INT8)"
    plan_id: plan_001
    description: >
      Extract activations at 24 probed layers (every 4th of 94), 20 languages on GlobalMMLU.
      Train English logistic regression + 2-layer MLP correctness probes. Evaluate 5 transfer
      conditions: zero-shot, mean-shift, linear projection, few-shot (25/100), CaCLR.
    expected_results:
      # English probing
      en_auroc_best_layer: 0.776
      en_best_layer_idx: 72  # ~77% depth in 94-layer model
      en_auroc_range: [0.612, 0.776]
      en_ece_raw_best: 0.172
      en_ece_tempcal_best: 0.068
      temp_scaling_T: 5.83
      # Zero-shot transfer
      zs_transfer_auroc_mean_19lang: 0.621
      zs_transfer_auroc_median_19lang: 0.633
      zs_transfer_auroc_std_19lang: 0.054
      zs_transfer_drop_mean_pp: 15.5
      zs_pass_rate_19lang: 0.368  # 7/19 above 0.65 threshold
      zs_pass_langs: [zh, fr, de, es, ja, ru, ko]
      zs_fail_langs: [ar, hi, sw, yo, te, bn, ta, th, vi, uk, id, pl]
      # Mean-shift
      mean_shift_improves_count: 0  # 0/19 languages
      mean_shift_mean_delta_ece_pp: 3.14  # hurts calibration on average
      # Linear projection
      linproj_auroc_mean_19lang: 0.648
      linproj_improves_over_zs_count: 13  # 13/19
      linproj_mean_delta_auroc_vs_zs_pp: 2.7
      # Few-shot 25
      fewshot25_auroc_mean_19lang: 0.654
      fewshot25_improves_over_zs_count: 14
      # Few-shot 100
      fewshot100_auroc_mean_19lang: 0.671
      fewshot100_improves_over_zs_count: 16
      # Pareto frontier shape
      pareto_depth_transfer_rank_corr: 0.41  # positive but moderate
      pareto_frontier_monotonic: false  # noisy, local reversals at layers 48-56
      pareto_n_dominated_layers: 6  # only 6 of 24 layers are Pareto-optimal
      # Per-language-family transfer AUROC (zero-shot, best layer per lang)
      transfer_by_family:
        indo_european_germanic: {mean: 0.672, langs: [de, en]}
        indo_european_romance: {mean: 0.661, langs: [fr, es]}
        indo_european_slavic: {mean: 0.629, langs: [ru, uk, pl]}
        indo_european_indic: {mean: 0.598, langs: [hi, bn, te, ta]}
        sino_tibetan: {mean: 0.668, langs: [zh]}
        japonic: {mean: 0.651, langs: [ja]}
        koreanic: {mean: 0.648, langs: [ko]}
        afroasiatic: {mean: 0.612, langs: [ar]}
        niger_congo: {mean: 0.543, langs: [sw, yo]}
        tai_kadai: {mean: 0.591, langs: [th]}
        austronesian: {mean: 0.618, langs: [id]}
        austroasiatic: {mean: 0.607, langs: [vi]}
    result_rationale: >
      Qwen3-235B is a much larger MoE model than the MVP's Qwen2.5-7B. English AUROC at 0.776
      improves modestly over MVP's 0.754 because the model is more capable and the correctness
      signal is more linearly accessible in larger models, but gains are sublinear — the larger
      model also has more complex, distributed representations that resist simple linear probing.
      Zero-shot transfer mean of 0.621 reflects the worst-tier prediction that transfer is
      unreliable: high-resource Indo-European languages (fr, de, es) and CJK (zh, ja, ko) transfer
      adequately because their representations share more subspace structure with English at
      intermediate layers, but low-resource languages (sw, yo, te, bn) and languages with very
      different morphology (th, ta) fail because the MoE routing creates language-specific expert
      patterns that are opaque to an English-trained linear probe. Mean-shift fails entirely (0/19)
      because the mean activation difference between languages conflates content, style, and script
      differences — subtracting it removes useful signal. The Pareto frontier rank correlation of
      0.41 is real but moderate: the general trend (deeper = better English, worse transfer) holds,
      but MoE routing introduces non-monotonic noise at mid-depth layers where expert activation
      patterns shift. The 7/19 pass rate reflects that only typologically close or high-resource
      languages have enough representational overlap with English for zero-shot transfer to work.
    tables:
      - name: "Table 1: Qwen3-235B English Probe Performance by Layer (Selected Layers)"
        columns: [layer, depth_pct, logreg_auroc, mlp_auroc, ece_raw, ece_tempcal]
        rows:
          - [4,   4,  0.612, 0.618, 0.298, 0.192]
          - [16, 17,  0.653, 0.661, 0.251, 0.148]
          - [28, 30,  0.694, 0.708, 0.224, 0.121]
          - [40, 43,  0.721, 0.737, 0.203, 0.098]
          - [52, 55,  0.742, 0.755, 0.191, 0.082]
          - [60, 64,  0.758, 0.769, 0.183, 0.075]
          - [72, 77,  0.776, 0.783, 0.172, 0.068]
          - [80, 85,  0.771, 0.779, 0.176, 0.071]
          - [88, 94,  0.753, 0.762, 0.185, 0.079]
          - [92, 98,  0.728, 0.739, 0.198, 0.091]
      - name: "Table 2: Qwen3-235B Zero-Shot Transfer AUROC by Language (Best Transfer Layer)"
        columns: [language, family, resource_tier, best_zs_layer, best_zs_auroc, en_auroc_at_same_layer, drop_pp]
        rows:
          - [zh, sino_tibetan, high, 52, 0.668, 0.742, 7.4]
          - [fr, romance, high, 52, 0.672, 0.742, 7.0]
          - [de, germanic, high, 52, 0.671, 0.742, 7.1]
          - [es, romance, high, 52, 0.661, 0.742, 8.1]
          - [ja, japonic, high, 48, 0.651, 0.735, 8.4]
          - [ru, slavic, high, 48, 0.644, 0.735, 9.1]
          - [ko, koreanic, high, 48, 0.648, 0.735, 8.7]
          - [ar, afroasiatic, mid, 40, 0.612, 0.721, 10.9]
          - [hi, indic, mid, 40, 0.618, 0.721, 10.3]
          - [vi, austroasiatic, mid, 40, 0.607, 0.721, 11.4]
          - [id, austronesian, mid, 40, 0.618, 0.721, 10.3]
          - [th, tai_kadai, mid, 40, 0.591, 0.721, 13.0]
          - [pl, slavic, mid, 40, 0.621, 0.721, 10.0]
          - [uk, slavic, mid, 40, 0.614, 0.721, 10.7]
          - [bn, indic, low, 28, 0.583, 0.694, 11.1]
          - [te, indic, low, 28, 0.571, 0.694, 12.3]
          - [ta, indic, low, 28, 0.568, 0.694, 12.6]
          - [sw, niger_congo, low, 28, 0.557, 0.694, 13.7]
          - [yo, niger_congo, low, 28, 0.529, 0.694, 16.5]
      - name: "Table 3: Qwen3-235B Transfer Method Comparison (AUROC, 19-Language Mean)"
        columns: [method, auroc_mean, auroc_std, pass_rate, ece_mean, delta_vs_zs_pp]
        rows:
          - [zero_shot,         0.621, 0.054, 0.368, 0.194, 0.0]
          - [mean_shift,        0.604, 0.067, 0.263, 0.225, -1.7]
          - [linear_projection, 0.648, 0.048, 0.526, 0.171, 2.7]
          - [few_shot_25,       0.654, 0.045, 0.526, 0.166, 3.3]
          - [few_shot_100,      0.671, 0.041, 0.632, 0.152, 5.0]
    figures_description:
      - "Figure 1a: Heatmap of zero-shot transfer AUROC (y-axis: 24 probed layers sorted by depth, x-axis: 20 languages sorted by resource tier). Shows a gradient where upper-left (deep layers × high-resource langs) has moderate AUROC (~0.65-0.67) and lower-right (shallow layers × low-resource langs) is near chance (~0.52-0.57). But the pattern is noisy — no crisp diagonal boundary. Several mid-depth layers show unexpected dips (layers 48-56) breaking monotonicity."
      - "Figure 1b: Pareto frontier scatter plot (x-axis: mean 19-lang zero-shot AUROC, y-axis: English AUROC at same layer). Each point is a layer. The Pareto front connects 6 non-dominated layers but the remaining 18 points scatter widely around it. Convex hull is thin — the tradeoff is real but the frontier offers limited choice. Error bars (bootstrap 95% CI) overlap substantially between adjacent Pareto-optimal points."
      - "Figure 1c: Line plot of zero-shot transfer drop (EN AUROC minus target-lang AUROC) vs layer depth, one line per language, colored by resource tier. High-resource languages (blue) show a gentle upward slope (deeper = worse transfer). Low-resource languages (red) show a steep upward slope. The spread between lines increases with depth, illustrating that the Pareto tradeoff is more severe for low-resource languages."
    analysis: >
      The Pareto frontier is real on Qwen3-235B but weak: rank correlation of 0.41 means the
      depth-transfer tradeoff explains only ~17% of variance. MoE routing creates non-monotonic
      perturbations at mid-depth. The practical implication is limited — the frontier provides
      modest guidance for layer selection but is not a reliable engineering tool. Zero-shot transfer
      fails for 12/19 languages (AUROC < 0.65), with a clear resource-tier gradient. The field
      should not assume English-trained correctness probes transfer to low-resource languages.
      Mean-shift is confirmed dead at scale. Linear projection and few-shot are the only viable
      transfer methods, with few-shot-100 achieving the best results — but requiring 100 labeled
      examples per language partially negates the zero-label promise.

  # ============================================================
  # plan_002 — Full Pareto Frontier, Llama 4 Scout
  # ============================================================
  - name: "Full Pareto Frontier — Llama 4 Scout (48 layers, MoE, INT8)"
    plan_id: plan_002
    description: >
      Extract activations at 12 probed layers (every 4th of 48), 20 languages on GlobalMMLU.
      Train English correctness probes, evaluate 5 transfer conditions.
    expected_results:
      en_auroc_best_layer: 0.749
      en_best_layer_idx: 36  # 75% depth
      en_auroc_range: [0.598, 0.749]
      en_ece_raw_best: 0.188
      en_ece_tempcal_best: 0.074
      temp_scaling_T: 5.47
      zs_transfer_auroc_mean_19lang: 0.594
      zs_transfer_auroc_median_19lang: 0.601
      zs_transfer_auroc_std_19lang: 0.061
      zs_transfer_drop_mean_pp: 18.2
      zs_pass_rate_19lang: 0.211  # 4/19
      zs_pass_langs: [zh, fr, de, es]
      zs_fail_langs: [ja, ru, ko, ar, hi, sw, yo, te, bn, ta, th, vi, uk, id, pl]
      mean_shift_improves_count: 0
      mean_shift_mean_delta_ece_pp: 4.21
      linproj_auroc_mean_19lang: 0.623
      linproj_improves_over_zs_count: 11
      fewshot25_auroc_mean_19lang: 0.631
      fewshot100_auroc_mean_19lang: 0.652
      pareto_depth_transfer_rank_corr: 0.22  # weak, near-flat frontier
      pareto_frontier_monotonic: false  # non-monotonic, no clear tradeoff
      pareto_n_dominated_layers: 3  # only 3 of 12 layers non-dominated
      pareto_frontier_agreement_with_qwen3: 0.33  # low agreement
      # Non-monotonicity detail
      nonmonotonic_layers: [20, 24, 28]  # transfer improves then drops then improves again
    result_rationale: >
      Llama 4 Scout is the worst-tier's key failure point. Its Pareto frontier is flat/non-monotonic
      (rank correlation 0.22) because Llama 4 Scout's MoE architecture uses a different routing
      strategy than Qwen3-235B: its experts are more language-specialized at intermediate layers,
      meaning the English correctness direction at layers 20-28 is entangled with English-specific
      expert activations in ways that neither degrade nor improve monotonically with depth. English
      AUROC peaks at 0.749 (lower than Qwen3's 0.776) because Llama 4 Scout's 48 layers compress
      the representational hierarchy — the same functional stages are packed into fewer layers,
      leaving less room for a clean correctness signal to emerge. Zero-shot transfer is worse
      overall (mean 0.594 vs Qwen3's 0.621) because Llama 4 Scout's training data distribution
      is more English-centric, and its MoE routing assigns non-English tokens to a sparser expert
      set that shares less structure with the English experts. Only 4/19 languages pass the 0.65
      threshold. The 0.33 cross-architecture Pareto agreement means the optimal layer for a given
      language on Qwen3 does not predict the optimal layer on Llama 4 — the tradeoff is
      architecture-specific, not a universal property of transformer depth.
    tables:
      - name: "Table 4: Llama 4 Scout English Probe Performance by Layer"
        columns: [layer, depth_pct, logreg_auroc, mlp_auroc, ece_raw, ece_tempcal]
        rows:
          - [4,   8,  0.598, 0.604, 0.312, 0.201]
          - [8,  17,  0.631, 0.641, 0.274, 0.168]
          - [12, 25,  0.668, 0.679, 0.241, 0.137]
          - [16, 33,  0.694, 0.706, 0.218, 0.112]
          - [20, 42,  0.712, 0.722, 0.205, 0.098]
          - [24, 50,  0.726, 0.735, 0.196, 0.088]
          - [28, 58,  0.734, 0.743, 0.192, 0.083]
          - [32, 67,  0.741, 0.749, 0.189, 0.078]
          - [36, 75,  0.749, 0.755, 0.188, 0.074]
          - [40, 83,  0.744, 0.751, 0.190, 0.077]
          - [44, 92,  0.731, 0.738, 0.195, 0.084]
          - [48, 100, 0.708, 0.718, 0.209, 0.097]
      - name: "Table 5: Llama 4 Scout Zero-Shot Transfer AUROC by Language (Best Transfer Layer)"
        columns: [language, best_zs_layer, best_zs_auroc, drop_vs_en_pp]
        rows:
          - [zh, 24, 0.658, 6.8]
          - [fr, 24, 0.662, 6.4]
          - [de, 24, 0.655, 7.1]
          - [es, 24, 0.651, 7.5]
          - [ja, 20, 0.631, 8.1]
          - [ru, 20, 0.622, 9.0]
          - [ko, 20, 0.627, 8.5]
          - [ar, 16, 0.589, 10.5]
          - [hi, 16, 0.594, 10.0]
          - [vi, 16, 0.581, 11.3]
          - [id, 16, 0.591, 10.3]
          - [th, 16, 0.568, 12.6]
          - [pl, 20, 0.608, 10.4]
          - [uk, 16, 0.592, 10.2]
          - [bn, 12, 0.556, 11.2]
          - [te, 12, 0.541, 12.7]
          - [ta, 12, 0.538, 13.0]
          - [sw, 12, 0.524, 14.4]
          - [yo, 12, 0.498, 17.0]
      - name: "Table 6: Cross-Architecture Pareto Frontier Agreement"
        columns: [metric, qwen3_235b, llama4_scout, agreement]
        rows:
          - [rank_corr_depth_vs_transfer, 0.41, 0.22, "—"]
          - [pareto_optimal_layer_count, "6/24", "3/12", "—"]
          - [best_transfer_layer_pct_depth, "55%", "50%", "—"]
          - [zs_mean_auroc, 0.621, 0.594, "—"]
          - [optimal_layer_rank_agreement_tau, "—", "—", 0.33]
          - [pass_lang_overlap_jaccard, "—", "—", 0.44]
    figures_description:
      - "Figure 2a: Side-by-side Pareto frontier scatter plots for Qwen3-235B (left) and Llama 4 Scout (right). Qwen3 shows a discernible convex Pareto front with 6 non-dominated points forming a curve from upper-left (high EN, low transfer) to lower-right (low EN, high transfer). Llama 4 shows a near-flat cloud with only 3 weakly non-dominated points — no meaningful tradeoff curve. The contrast is the paper's key Figure 2 evidence that the Pareto frontier is architecture-dependent."
      - "Figure 2b: Llama 4 Scout non-monotonicity detail: line plot of transfer AUROC vs layer depth for zh, fr, ar, sw. The zh/fr lines show a bump at layer 20, dip at 24, recover at 28 — violating the monotonic depth-transfer assumption. This is attributed to MoE expert routing transitions at these layers."
    analysis: >
      Llama 4 Scout is the worst-tier's smoking gun for the diagnostic reframe. The Pareto frontier
      essentially doesn't exist on this architecture (rank corr 0.22, only 3 non-dominated layers).
      This is the strongest evidence for the diagnostic paper's thesis: the depth-transfer tradeoff
      from Claim 1 is not a universal property of transformers but an architecture-dependent
      phenomenon that cannot be assumed to generalize. The 0.33 cross-architecture agreement means
      practitioners cannot use findings from one model to guide layer selection on another. For the
      paper, this transforms from a weakness into a key finding: the field cannot assume probe-based
      calibration will behave consistently across architectures.

  # ============================================================
  # plan_003 — CaCLR Implementation and Comparative Evaluation
  # ============================================================
  - name: "CaCLR Implementation and Comparative Evaluation"
    plan_id: plan_003
    description: >
      Implement CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency). Train CaCLR probes using English
      labels + unlabeled parallel activations. Compare vs all 5 transfer conditions across full
      Pareto frontier for both models × 20 languages.
    expected_results:
      # CaCLR vs baselines (19-language means)
      caclr_auroc_mean_qwen3: 0.645
      caclr_auroc_mean_llama4: 0.618
      caclr_vs_linproj_auroc_delta_pp_qwen3: -0.3  # CaCLR slightly worse than linproj
      caclr_vs_linproj_auroc_delta_pp_llama4: -0.5
      caclr_vs_zs_auroc_delta_pp_qwen3: 2.4  # better than zero-shot
      caclr_vs_zs_auroc_delta_pp_llama4: 2.4
      caclr_vs_fewshot100_auroc_delta_pp_qwen3: -2.6  # worse than few-shot 100
      caclr_vs_fewshot100_auroc_delta_pp_llama4: -3.4
      caclr_improvement_pass_rate_qwen3: 0.47  # 9/19 languages improve over zero-shot
      caclr_improvement_pass_rate_llama4: 0.37  # 7/19
      caclr_ece_mean_qwen3: 0.174
      caclr_ece_mean_llama4: 0.189
      caclr_ece_reduction_vs_tempcal_pct_qwen3: 7.2
      caclr_ece_reduction_vs_tempcal_pct_llama4: 3.8
      # Hyperparameter sensitivity
      best_alpha: 0.3
      best_beta: 0.05  # consistency term shrunk to near-zero by tuning
      alpha_sensitivity: "moderate — ±0.1 changes AUROC by ~0.5pp"
      beta_sensitivity: "flat — β from 0.01 to 0.5 changes AUROC by <0.3pp, indicating consistency loss is inert"
      # Ablation: CaCLR components
      caclr_no_consistency_auroc_mean: 0.647  # removing consistency term slightly improves
      caclr_no_sbece_auroc_mean: 0.629  # SB-ECE helps modestly
      caclr_bce_only_auroc_mean: 0.621  # equivalent to zero-shot
      # Per-language CaCLR results (Qwen3, best layer per lang)
      caclr_per_lang_qwen3:
        zh: {auroc: 0.671, delta_vs_zs: 0.3, delta_vs_linproj: -0.8}
        fr: {auroc: 0.668, delta_vs_zs: -0.4, delta_vs_linproj: -1.2}
        de: {auroc: 0.665, delta_vs_zs: -0.6, delta_vs_linproj: -0.9}
        es: {auroc: 0.658, delta_vs_zs: -0.3, delta_vs_linproj: -0.7}
        ja: {auroc: 0.649, delta_vs_zs: -0.2, delta_vs_linproj: -0.4}
        ru: {auroc: 0.641, delta_vs_zs: -0.3, delta_vs_linproj: -0.6}
        ko: {auroc: 0.647, delta_vs_zs: -0.1, delta_vs_linproj: -0.3}
        ar: {auroc: 0.628, delta_vs_zs: 1.6, delta_vs_linproj: 0.2}
        hi: {auroc: 0.635, delta_vs_zs: 1.7, delta_vs_linproj: 0.1}
        vi: {auroc: 0.621, delta_vs_zs: 1.4, delta_vs_linproj: -0.3}
        id: {auroc: 0.633, delta_vs_zs: 1.5, delta_vs_linproj: -0.1}
        th: {auroc: 0.607, delta_vs_zs: 1.6, delta_vs_linproj: 0.3}
        pl: {auroc: 0.638, delta_vs_zs: 1.7, delta_vs_linproj: 0.1}
        uk: {auroc: 0.631, delta_vs_zs: 1.7, delta_vs_linproj: 0.2}
        bn: {auroc: 0.601, delta_vs_zs: 1.8, delta_vs_linproj: 0.5}
        te: {auroc: 0.589, delta_vs_zs: 1.8, delta_vs_linproj: 0.4}
        ta: {auroc: 0.587, delta_vs_zs: 1.9, delta_vs_linproj: 0.6}
        sw: {auroc: 0.578, delta_vs_zs: 2.1, delta_vs_linproj: 0.9}
        yo: {auroc: 0.551, delta_vs_zs: 2.2, delta_vs_linproj: 0.7}
    result_rationale: >
      CaCLR's consistency loss (L_consistency) is designed to align cross-lingual probe activations
      so that the English probe generalizes. In the worst tier, this fails because the
      cross-lingual correctness signal is too noisy for the consistency objective to find meaningful
      invariances. The unlabeled parallel activations contain language-specific variance (script,
      morphology, tokenization artifacts) that dominates the correctness signal, so minimizing
      distributional distance between languages collapses both signal and noise. The hyperparameter
      search confirms this: β (consistency weight) is driven to near-zero (0.05), and removing
      the consistency term entirely slightly improves performance (+0.2pp). The SB-ECE term helps
      modestly because it acts as a calibration regularizer on the English side, but this benefit
      doesn't compound with consistency. CaCLR ends up being essentially "zero-shot + SB-ECE
      regularization" — functionally a slightly calibration-aware version of the base probe. Linear
      projection beats CaCLR because projection directly estimates and applies the affine
      transformation between language representation subspaces, which is a more efficient use of
      the few available parallel datapoints than trying to learn an invariant representation. The
      key insight: simple alignment (linproj) outperforms principled invariance (CaCLR) when the
      signal-to-noise ratio of the target signal is low. For high-resource languages that already
      transfer well, CaCLR's overhead yields no benefit; for low-resource languages where help is
      needed, the consistency signal is too noisy to learn from.
    tables:
      - name: "Table 7: Transfer Method Comparison Summary (19-Language Mean, Both Architectures)"
        columns: [method, qwen3_auroc, qwen3_ece, llama4_auroc, llama4_ece, labels_needed]
        rows:
          - [zero_shot,         0.621, 0.194, 0.594, 0.212, "0 target"]
          - [mean_shift,        0.604, 0.225, 0.571, 0.248, "0 target (fails)"]
          - [linear_projection, 0.648, 0.171, 0.623, 0.189, "~50 parallel"]
          - [CaCLR,             0.645, 0.174, 0.618, 0.193, "0 target + parallel"]
          - [few_shot_25,       0.654, 0.166, 0.631, 0.182, "25 target"]
          - [few_shot_100,      0.671, 0.152, 0.652, 0.168, "100 target"]
      - name: "Table 8: CaCLR Ablation (Qwen3-235B, 19-Language Mean)"
        columns: [variant, auroc_mean, ece_mean, delta_vs_full_pp]
        rows:
          - ["Full CaCLR (BCE+SB-ECE+Consistency)", 0.645, 0.174, 0.0]
          - ["CaCLR − Consistency (BCE+SB-ECE)",    0.647, 0.172, +0.2]
          - ["CaCLR − SB-ECE (BCE+Consistency)",     0.629, 0.188, -1.6]
          - ["BCE Only (= zero-shot probe)",          0.621, 0.194, -2.4]
          - ["Linear Projection",                     0.648, 0.171, +0.3]
    figures_description:
      - "Figure 3a: Grouped bar chart comparing 6 transfer methods across 20 languages (Qwen3-235B), sorted by language resource tier. Shows that few-shot-100 > few-shot-25 ≈ linear projection ≈ CaCLR > zero-shot >> mean-shift. CaCLR and linear projection bars are nearly identical in height across all languages. The visual message is clear: CaCLR adds complexity without benefit."
      - "Figure 3b: Hyperparameter sensitivity plot for CaCLR. Left panel: AUROC vs α (SB-ECE weight), showing a gentle inverted-U peaking at α=0.3. Right panel: AUROC vs β (consistency weight), showing a flat line — β has no effect. This is the key visual evidence that the consistency objective is inert."
      - "Figure 3c: Scatter plot of per-language CaCLR improvement (y-axis) vs zero-shot baseline AUROC (x-axis). Shows that CaCLR helps low-resource languages modestly (+1-2pp) but slightly hurts high-resource languages that already transfer well (-0.3 to -1.2pp). Linear projection shows the same pattern but with uniformly better outcomes. Net: CaCLR's mechanism doesn't add value over simple geometric alignment."
    analysis: >
      CaCLR is a rigorous negative result. The consistency loss term — the core methodological
      novelty — is inert. This is not a hyperparameter tuning failure; β is swept over 3 orders
      of magnitude and the landscape is flat. The SB-ECE term provides modest calibration
      regularization, but this benefit is available without any cross-lingual machinery. Linear
      projection achieves the same or better results with a simpler mechanism. For the paper, this
      is framed as: "consistency-based cross-lingual alignment objectives do not help when the
      underlying correctness signal has low cross-lingual SNR. This negative result saves the
      community from pursuing distributional-matching approaches (adversarial, MMD, consistency)
      for this problem class."

  # ============================================================
  # plan_004 — Difficulty-Controlled Ablation (Decomposition)
  # ============================================================
  - name: "Difficulty-Controlled Ablation (Decomposition)"
    plan_id: plan_004
    description: >
      Train IRT difficulty probes, project out difficulty direction from activations, retrain
      correctness probes on residuals, evaluate transfer. 10 representative languages × 8
      representative layers per model.
    expected_results:
      # Difficulty probe quality
      difficulty_probe_r2_en_qwen3: 0.52
      difficulty_probe_r2_en_llama4: 0.47
      difficulty_probe_transfer_r2_mean_9lang: 0.41  # difficulty transfers better than correctness
      # Decomposition results
      decomp_difficulty_var_explained_pct_qwen3: 14.3
      decomp_difficulty_var_explained_pct_llama4: 11.8
      # After projecting out difficulty
      correctness_residual_auroc_en_qwen3: 0.738  # drops from 0.776
      correctness_residual_auroc_en_llama4: 0.711  # drops from 0.749
      correctness_residual_transfer_auroc_mean_qwen3: 0.607  # drops from 0.621
      correctness_residual_transfer_auroc_mean_llama4: 0.581  # drops from 0.594
      # Key test: does projecting out difficulty improve transfer?
      transfer_improvement_after_projection: false
      transfer_delta_after_projection_pp_qwen3: -1.4  # slightly WORSE
      transfer_delta_after_projection_pp_llama4: -1.3
      # Cosine similarity between difficulty and correctness directions
      difficulty_correctness_cosine_mean_qwen3: 0.34
      difficulty_correctness_cosine_mean_llama4: 0.38
      difficulty_correctness_cosine_std: 0.11
      # Subspace overlap (principal angles)
      subspace_overlap_mean_angle_deg: 58  # neither orthogonal (90°) nor aligned (0°)
    result_rationale: >
      In the worst tier, difficulty and capability are entangled in cross-lingual representations.
      The difficulty direction explains only 14% (Qwen3) / 12% (Llama4) of correctness probe
      variance — real but modest. Critically, projecting out difficulty makes transfer WORSE
      (-1.3 to -1.4pp), not better. This is because the difficulty-shared component actually
      carries useful cross-lingual signal: questions that are hard in English tend to be hard
      everywhere due to shared conceptual complexity, and this shared difficulty signal is one of
      the few reliable cross-lingual bridges for the correctness probe. Removing it strips away
      a genuine cross-lingual invariance. The residual "capability-specific" component is more
      language-dependent, not less — it contains the idiosyncratic ways each language's tokens
      encode competence, which are precisely the non-transferable signals. The cosine similarity
      of 0.34-0.38 between difficulty and correctness directions confirms they are neither
      orthogonal nor aligned — they share a moderate subspace that cannot be cleanly separated.
      This contradicts the paper's original Claim 2 hypothesis that decomposition would be
      prescriptive. The decomposition is real but useless: it describes variance structure without
      enabling better transfer.
    tables:
      - name: "Table 9: Difficulty Probe Quality (Ridge Regression, R² on Held-Out)"
        columns: [language, qwen3_r2, llama4_r2, is_transfer]
        rows:
          - [en, 0.52, 0.47, false]
          - [zh, 0.48, 0.43, true]
          - [fr, 0.47, 0.42, true]
          - [de, 0.46, 0.41, true]
          - [ar, 0.42, 0.37, true]
          - [hi, 0.41, 0.36, true]
          - [ja, 0.44, 0.39, true]
          - [ko, 0.43, 0.38, true]
          - [sw, 0.33, 0.28, true]
          - [yo, 0.29, 0.24, true]
      - name: "Table 10: Decomposition Transfer Ablation (9-Language Mean)"
        columns: [condition, qwen3_auroc, qwen3_delta_pp, llama4_auroc, llama4_delta_pp]
        rows:
          - ["Full activations (baseline)",           0.621, 0.0,   0.594, 0.0]
          - ["Residual (difficulty projected out)",    0.607, -1.4,  0.581, -1.3]
          - ["Difficulty component only",              0.568, -5.3,  0.551, -4.3]
          - ["Random direction projected out (ctrl)",  0.618, -0.3,  0.591, -0.3]
    figures_description:
      - "Figure 4a: Scatter plot of correctness AUROC vs difficulty R² across 10 languages × 8 layers, colored by model. Shows moderate positive correlation (r=0.41) — layers where difficulty is well-encoded also support better correctness probing. This contradicts the expectation that difficulty is a confound to be removed."
      - "Figure 4b: Principal angle distribution between difficulty and correctness subspaces across layers. Histogram peaks at ~55-60° — far from both 0° (fully shared) and 90° (fully orthogonal). The wide spread (std ~11°) across layers and languages shows the relationship is inconsistent, preventing clean decomposition."
    analysis: >
      Decomposition fails as a prescriptive tool. The difficulty-shared component, far from being
      a confound, is actually one of the more reliable cross-lingual bridges — removing it hurts.
      The capability-specific residual is more language-dependent, not less, because it captures
      idiosyncratic encoding patterns. For the diagnostic paper, this finding is reframed as:
      "difficulty and capability are entangled in multilingual representations, unlike the clean
      separation reported in English-only work. This entanglement may be fundamental to how
      multilingual models represent knowledge — the shared difficulty structure is load-bearing
      for cross-lingual transfer, not a confound to be controlled for."

  # ============================================================
  # plan_005 — Cross-Lingual Orthogonality Analysis
  # ============================================================
  - name: "Cross-Lingual Orthogonality Analysis"
    plan_id: plan_005
    description: >
      Extract verbalized confidence direction, compute cosine similarity with correctness direction
      across 20 languages × 2 architectures. Analyze by resource tier and language family.
    expected_results:
      orthogonality_cosine_mean_overall: 0.072
      orthogonality_cosine_std_overall: 0.038
      orthogonality_cosine_mean_qwen3: 0.068
      orthogonality_cosine_mean_llama4: 0.076
      orthogonality_cosine_range: [0.018, 0.148]
      # By resource tier
      orthogonality_cosine_high_resource: 0.054  # more orthogonal
      orthogonality_cosine_mid_resource: 0.071
      orthogonality_cosine_low_resource: 0.098  # less orthogonal
      # Significance
      pct_langs_cosine_below_0_1: 0.75  # 15/20 languages have cosine < 0.1
      pct_langs_cosine_below_0_05: 0.35  # 7/20 match Miao & Ungar's < 0.04 threshold
      # Confidence probe quality
      confidence_probe_r2_mean: 0.68
      confidence_probe_transfer_drops: true  # confidence direction also language-dependent
    result_rationale: >
      Orthogonality persists cross-lingually (mean cosine 0.072, all languages below 0.15) because
      it is a structural property of how LLMs represent confidence vs correctness — the model's
      verbalized confidence is calibrated to appear confident regardless of actual correctness,
      and this dissociation is encoded geometrically at the representation level. However, the
      worst-tier variance is higher than Miao & Ungar's English-only finding (std 0.038 vs their
      ~0.01): low-resource languages show less orthogonality (cosine ~0.098) because the model has
      less capacity to maintain the confidence-correctness dissociation for languages with limited
      training data — when the model is uncertain due to lack of language-specific knowledge, both
      its correctness and confidence signals degrade in correlated ways, slightly breaking
      orthogonality. Reviewers may see this as incremental: Miao & Ungar showed orthogonality for
      English, we extend to 20 languages, but the finding is qualitatively the same. The resource-
      tier modulation is the one novel angle but the effect size is modest (0.054 vs 0.098).
    tables:
      - name: "Table 11: Correctness-Confidence Cosine Similarity by Language"
        columns: [language, resource_tier, qwen3_cosine, llama4_cosine, mean_cosine]
        rows:
          - [en, high, 0.038, 0.041, 0.040]
          - [zh, high, 0.042, 0.049, 0.046]
          - [fr, high, 0.045, 0.051, 0.048]
          - [de, high, 0.047, 0.054, 0.051]
          - [es, high, 0.049, 0.056, 0.053]
          - [ja, high, 0.055, 0.062, 0.059]
          - [ru, high, 0.058, 0.064, 0.061]
          - [ko, high, 0.061, 0.068, 0.065]
          - [ar, mid,  0.063, 0.072, 0.068]
          - [hi, mid,  0.065, 0.075, 0.070]
          - [vi, mid,  0.068, 0.077, 0.073]
          - [id, mid,  0.064, 0.073, 0.069]
          - [th, mid,  0.072, 0.082, 0.077]
          - [pl, mid,  0.059, 0.067, 0.063]
          - [uk, mid,  0.062, 0.071, 0.067]
          - [bn, low,  0.081, 0.092, 0.087]
          - [te, low,  0.088, 0.098, 0.093]
          - [ta, low,  0.091, 0.103, 0.097]
          - [sw, low,  0.098, 0.112, 0.105]
          - [yo, low,  0.112, 0.148, 0.130]
      - name: "Table 12: Orthogonality by Resource Tier (Mean Cosine ± Std)"
        columns: [resource_tier, n_langs, qwen3_mean, llama4_mean, overall_mean, std]
        rows:
          - [high, 8, 0.049, 0.056, 0.054, 0.009]
          - [mid,  7, 0.065, 0.074, 0.071, 0.005]
          - [low,  5, 0.094, 0.111, 0.098, 0.016]
          - [all, 20, 0.066, 0.076, 0.072, 0.022]
    figures_description:
      - "Figure 5a: Bar chart of cosine similarity (correctness vs confidence direction) for 20 languages, sorted by resource tier, with Miao & Ungar's English-only threshold (0.04) marked as a horizontal dashed line. Most high-resource languages cluster near the line; low-resource languages are 2-3× higher but still below 0.15. The visual confirms orthogonality persists everywhere but the quantitative story is noisier than prior work suggested."
      - "Figure 5b: Scatter plot of orthogonality cosine (y-axis) vs zero-shot transfer AUROC (x-axis), per language. Moderate negative correlation (r ≈ -0.62): languages where orthogonality is stronger (lower cosine) also transfer better. This connects Claims 1 and 4 — representation quality covaries with both metrics — but the causal direction is ambiguous."
    analysis: >
      Claim 4 survives in the worst tier but its contribution is incremental. Orthogonality
      persists (mean 0.072, all < 0.15) — output-based calibration is indeed structurally limited
      everywhere. The resource-tier gradient (high: 0.054, mid: 0.071, low: 0.098) is novel but
      the effect size is modest. The correlation between orthogonality and transfer success is
      intriguing but not causal. For the diagnostic paper, this is framed as the one mechanistic
      takeaway: "the correctness-confidence dissociation is a multilingual phenomenon, confirming
      that output-based calibration methods face a structural ceiling regardless of language.
      However, this ceiling is slightly lower for low-resource languages, suggesting that the
      dissociation partly reflects representation quality rather than a pure architectural invariant."

  # ============================================================
  # plan_006 — Probe Complexity Comparison
  # ============================================================
  - name: "Probe Complexity Comparison"
    plan_id: plan_006
    description: >
      Compare logistic regression vs 2-layer MLP at each probed layer for both models. Test
      hypothesis that linear probes transfer better cross-lingually.
    expected_results:
      # English performance
      mlp_vs_logreg_en_auroc_delta_mean_pp_qwen3: 1.1  # MLP ~1pp better in English
      mlp_vs_logreg_en_auroc_delta_mean_pp_llama4: 0.9
      # Transfer performance
      mlp_vs_logreg_transfer_auroc_delta_mean_pp_qwen3: -0.4  # logreg transfers slightly better
      mlp_vs_logreg_transfer_auroc_delta_mean_pp_llama4: -0.2  # inconsistent
      # Net: effect is small and inconsistent
      hypothesis_linear_transfers_better: "weak support"
      effect_size_cohens_d: 0.18  # negligible
      # Interaction with depth
      mlp_advantage_shallow_layers_pp: 0.6
      mlp_advantage_deep_layers_pp: 1.4
      logreg_transfer_advantage_shallow_pp: 0.1
      logreg_transfer_advantage_deep_pp: 0.7
    result_rationale: >
      The hypothesis that linear probes transfer better receives only weak support. MLP probes
      are ~1pp better in English because the 2-layer MLP captures mild nonlinearities in the
      correctness signal (interaction effects between representation dimensions). But the
      cross-lingual transfer difference is tiny (-0.2 to -0.4pp favoring logistic regression)
      and inconsistent across languages and layers — Cohen's d of 0.18 means the effect would
      be invisible without large sample sizes. The interaction with depth is the most interesting
      signal: at deep layers, MLP probes overfit to English-specific patterns more (1.4pp English
      advantage) and consequently transfer worse (0.7pp transfer penalty). But even this effect
      is too small to be practically actionable. For the paper, this confirms logistic regression
      as the appropriate probe choice (simpler, nearly as good) but doesn't generate a standalone
      finding.
    tables:
      - name: "Table 13: Probe Complexity Comparison (Mean Across All Layers)"
        columns: [model, probe, en_auroc_mean, transfer_auroc_mean, en_ece_mean, transfer_ece_mean]
        rows:
          - [qwen3, logreg, 0.714, 0.621, 0.206, 0.194]
          - [qwen3, mlp,    0.725, 0.617, 0.198, 0.197]
          - [llama4, logreg, 0.697, 0.594, 0.219, 0.212]
          - [llama4, mlp,    0.706, 0.592, 0.212, 0.214]
    figures_description:
      - "Figure S1 (supplementary): Paired difference plot (MLP AUROC − LogReg AUROC) vs layer depth, one panel for English (positive differences, increasing with depth) and one for transfer mean (negative but near-zero differences, slightly increasing magnitude with depth). The confidence bands overlap zero at most layers for the transfer panel."
    analysis: >
      Probe complexity is a non-finding. The effect is real but negligible (Cohen's d 0.18).
      Logistic regression is the correct default choice: nearly identical performance with
      fewer hyperparameters and better interpretability. This goes into the supplementary
      as a methods validation, not a main finding.

  # ============================================================
  # plan_007 — Additional Benchmark Evaluation
  # ============================================================
  - name: "Additional Benchmark Evaluation (Belebele + MMLU-ProX)"
    plan_id: plan_007
    description: >
      Evaluate best probes + CaCLR on Belebele (reading comprehension, 20 languages) and
      MMLU-ProX (translated MMLU, 20 languages).
    expected_results:
      # Belebele
      belebele_en_auroc_qwen3: 0.741
      belebele_en_auroc_llama4: 0.718
      belebele_zs_transfer_mean_qwen3: 0.598
      belebele_zs_transfer_mean_llama4: 0.572
      belebele_drop_vs_globalmmlu_pp: 2.3  # slightly worse than GlobalMMLU
      belebele_caclr_delta_vs_linproj_pp: -0.6
      # MMLU-ProX
      mmlupx_en_auroc_qwen3: 0.762
      mmlupx_en_auroc_llama4: 0.738
      mmlupx_zs_transfer_mean_qwen3: 0.583
      mmlupx_zs_transfer_mean_llama4: 0.557
      mmlupx_drop_vs_globalmmlu_pp: 3.8  # noticeably worse — translation artifacts
      mmlupx_caclr_delta_vs_linproj_pp: -0.9
      # Cross-benchmark consistency
      lang_rank_correlation_globalmmlu_vs_belebele: 0.82  # languages rank similarly
      lang_rank_correlation_globalmmlu_vs_mmlupx: 0.71  # MMLU-ProX is noisier
    result_rationale: >
      Belebele partially replicates GlobalMMLU findings because it is also a high-quality,
      natively multilingual benchmark where translation artifacts are minimal. The 2.3pp drop
      reflects the domain shift (reading comprehension vs knowledge questions) but the relative
      ranking of languages is preserved (rank corr 0.82). MMLU-ProX shows worse transfer (3.8pp
      drop) because it is machine-translated from English MMLU — translation artifacts create
      systematic distributional shifts that the English-trained correctness probe cannot handle.
      The translation introduces new failure modes: ambiguous translations for domain-specific
      terms, cultural references that don't transfer, and occasional errors in low-resource
      translations. CaCLR is again no better than linear projection on either benchmark,
      confirming the negative result generalizes beyond the training benchmark.
    tables:
      - name: "Table 14: Cross-Benchmark Generalization (19-Language Mean)"
        columns: [benchmark, metric, qwen3, llama4]
        rows:
          - [GlobalMMLU, zs_transfer_auroc, 0.621, 0.594]
          - [Belebele,   zs_transfer_auroc, 0.598, 0.572]
          - [MMLU-ProX,  zs_transfer_auroc, 0.583, 0.557]
          - [GlobalMMLU, caclr_vs_linproj_pp, -0.3, -0.5]
          - [Belebele,   caclr_vs_linproj_pp, -0.6, -0.8]
          - [MMLU-ProX,  caclr_vs_linproj_pp, -0.9, -1.2]
    figures_description:
      - "Figure S2 (supplementary): Three-panel scatter plot showing per-language transfer AUROC correlation across benchmark pairs (GlobalMMLU vs Belebele, GlobalMMLU vs MMLU-ProX, Belebele vs MMLU-ProX). High correlation for the first pair, moderate for others. Low-resource languages (marked in red) are consistent outliers on MMLU-ProX due to translation quality."
    analysis: >
      Results partially generalize: Belebele confirms the main findings, MMLU-ProX is noisier due
      to translation artifacts. The language ranking is stable across benchmarks (which languages
      transfer well vs poorly is consistent), but absolute performance degrades with benchmark
      domain shift. CaCLR's negative result is robust across all three benchmarks — it never beats
      linear projection. For the paper, include Belebele in the main results and MMLU-ProX in
      supplementary with a note about translation artifacts.

  # ============================================================
  # plan_010 — INT8 Validation Ablation
  # ============================================================
  - name: "INT8 Validation Ablation"
    plan_id: plan_010
    description: >
      Compare INT8 vs FP16 probing results at 5 representative layers for Llama 4 Scout on 5%
      random subset. Validate that INT8 quantization doesn't distort correctness signals.
    expected_results:
      int8_vs_fp16_auroc_delta_mean_pp: -0.3
      int8_vs_fp16_auroc_delta_max_pp: -0.7
      int8_vs_fp16_ece_delta_mean_pp: 0.2
      int8_vs_fp16_activation_cosine_sim_mean: 0.994
      int8_vs_fp16_rank_correlation_layers: 0.98
      validation_passes: true
    result_rationale: >
      INT8 quantization introduces minimal distortion to correctness signals. The 0.3pp mean
      AUROC difference is within noise — INT8 preserves the relative ordering of activations
      that linear probes rely on, even though absolute magnitudes shift slightly. The 0.994
      cosine similarity between INT8 and FP16 activations confirms near-perfect directional
      alignment. This is expected because correctness is encoded in the direction of activations,
      not their magnitude, and INT8 preserves directions well. The layer ranking is identical
      (rank corr 0.98). This ablation passes cleanly even in the worst tier — quantization
      artifacts are not the source of any failures observed elsewhere.
    tables:
      - name: "Table S1 (supplementary): INT8 vs FP16 Probing Comparison"
        columns: [layer, fp16_auroc, int8_auroc, delta_pp, activation_cosine]
        rows:
          - [8,  0.637, 0.633, -0.4, 0.993]
          - [16, 0.700, 0.697, -0.3, 0.994]
          - [24, 0.731, 0.729, -0.2, 0.995]
          - [32, 0.746, 0.743, -0.3, 0.994]
          - [40, 0.748, 0.741, -0.7, 0.992]
    figures_description:
      - "Figure S3 (supplementary): Paired scatter plot of FP16 vs INT8 AUROC at each layer × language combination. Points lie tightly along the y=x diagonal with slight downward bias. Inset shows histogram of deltas, centered near -0.3pp with tight spread."
    analysis: >
      INT8 validation passes. Quantization is not a confound for any findings in this paper.
      Include in supplementary appendix as one paragraph + Table S1.

  # ============================================================
  # plan_008 — Gemma 4 31B Dense (Camera-Ready, P2)
  # ============================================================
  - name: "Gemma 4 31B Dense — Third Architecture (Camera-Ready)"
    plan_id: plan_008
    description: >
      Full Pareto frontier on Gemma 4 31B Dense (60 layers, dense architecture, FP16).
      Provides dense-vs-MoE architectural contrast for camera-ready extension.
    expected_results:
      en_auroc_best_layer: 0.761
      en_best_layer_idx: 45  # 75% depth
      zs_transfer_auroc_mean_19lang: 0.608
      zs_transfer_drop_mean_pp: 16.8
      pareto_depth_transfer_rank_corr: 0.48  # cleaner than MoE models
      pareto_frontier_agreement_with_qwen3: 0.42
      pareto_frontier_agreement_with_llama4: 0.29
      caclr_vs_linproj_pp: -0.2
      dense_vs_moe_finding: "Dense architecture shows cleaner Pareto frontier (rank corr 0.48 vs 0.41/0.22 for MoE models) — MoE routing is a source of non-monotonic noise in the depth-transfer relationship"
    result_rationale: >
      Gemma 4 31B Dense shows a cleaner (but still moderate) Pareto frontier because dense
      architectures have more homogeneous layer-to-layer representation transformations — no
      expert routing to create non-monotonic jumps. The rank correlation of 0.48 is the highest
      of the three architectures but still in the worst tier range. English AUROC of 0.761 is
      between Qwen3 (0.776) and Llama4 (0.749), consistent with its intermediate model size.
      Transfer is intermediate too (0.608). Cross-architecture agreement remains low (0.42 with
      Qwen3, 0.29 with Llama4), confirming architecture-dependence. The dense-vs-MoE contrast
      is the main value-add for camera-ready: it demonstrates that MoE routing is a specific
      source of frontier noise, not just model variation.
    tables:
      - name: "Table 15: Three-Architecture Comparison Summary"
        columns: [model, type, layers, en_auroc, transfer_auroc, pareto_rank_corr, pareto_agreement_mean]
        rows:
          - [Qwen3-235B, MoE, 94, 0.776, 0.621, 0.41, 0.38]
          - [Llama4-Scout, MoE, 48, 0.749, 0.594, 0.22, 0.31]
          - [Gemma4-31B, Dense, 60, 0.761, 0.608, 0.48, 0.36]
    figures_description:
      - "Figure 6 (camera-ready): Three-panel Pareto frontier comparison (Qwen3, Llama4, Gemma4). The dense model's frontier is the most visually coherent, with points forming a recognizable curve. MoE models show increasing scatter. Annotated with rank correlation values."
    analysis: >
      Gemma4 confirms the diagnostic paper's thesis from a new angle: the Pareto frontier is
      more coherent in dense architectures, implicating MoE routing as a specific source of
      cross-lingual transfer noise. For camera-ready, this strengthens the "architecture matters"
      message without changing the core worst-tier narrative.

  # ============================================================
  # plan_009 — Extended Language Coverage (Camera-Ready, P2)
  # ============================================================
  - name: "Extended Language Coverage (50+ Languages, Camera-Ready)"
    plan_id: plan_009
    description: >
      Expand from 20 to 50+ languages using full GlobalMMLU/Belebele language sets.
    expected_results:
      total_languages: 52
      zs_transfer_auroc_mean_51lang: 0.587  # worse with more low-resource languages
      zs_pass_rate_51lang: 0.235  # 12/51 above 0.65
      new_lang_families_added: 5  # Turkic, Uralic, Dravidian (extended), Kartvelian, Mongolic
      low_resource_auroc_mean_new_langs: 0.548
      worst_language_auroc: 0.491  # near chance for some extremely low-resource languages
      resource_tier_gradient_steeper: true  # the more languages, the steeper the drop-off
    result_rationale: >
      Expanding to 50+ languages worsens the aggregate picture because the additional languages
      are predominantly low- and very-low-resource. Many of these languages (e.g., Amharic,
      Lao, Mongolian, Georgian) have minimal representation in the models' training data, so
      their internal representations share even less structure with English. The pass rate drops
      from ~37% (7/19) to ~24% (12/51), and some languages approach chance (AUROC ~0.49).
      For the paper, this strengthens the diagnostic message: "probe-based calibration has a
      severe language barrier that scales with the number of languages you try to cover."
    tables:
      - name: "Table 16: Transfer Success by Resource Tier (Expanded 52-Language Set, Qwen3)"
        columns: [resource_tier, n_langs, zs_auroc_mean, zs_auroc_std, pass_rate]
        rows:
          - [high, 10, 0.653, 0.018, 0.70]
          - [mid, 18, 0.603, 0.024, 0.28]
          - [low, 14, 0.558, 0.031, 0.07]
          - [very_low, 10, 0.521, 0.022, 0.00]
    figures_description:
      - "Figure 7 (camera-ready): World map heatmap with 52 languages colored by zero-shot transfer AUROC. Europe and East Asia are green/yellow (adequate transfer). South/Southeast Asia is orange. Sub-Saharan Africa and Central Asia are red (near-chance). Visual reinforces the 'language barrier' framing."
    analysis: >
      Extended coverage is the nail in the coffin for universal probe-based calibration. With
      52 languages, the majority fail to transfer. The resource-tier gradient is steep and
      monotonic. This is the strongest evidence for the diagnostic paper's conclusion: "this
      research line does not generalize beyond a small set of high-resource languages without
      fundamental methodological advances."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e0c97fe-375b-49e2-842b-dbb3789c7000",
  "isSidechain": false,
  "requestId": "req_011CbEMnjEcmpHfRArKSy91B",
  "type": "assistant",
  "uuid": "a350538f-450e-48ba-8b6a-80c45f4e54ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f77c5807-10e5-4eae-ab8e-381ef798b6e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BN4tHuPgfkEsHSVZLMJ181",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11006,
      "cache_read_input_tokens": 11841,
      "output_tokens": 18255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11006,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18255,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11006
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Pareto frontier is real but weak/noisy. CaCLR fails to beat linear projection. Decomposition doesn't cleanly separate. Core method contribution collapses.…",
  "leafUuid": "a350538f-450e-48ba-8b6a-80c45f4e54ee",
  "sessionId": "f77c5807-10e5-4eae-ab8e-381ef798b6e6"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Multilingual probe calibration field diagnostic",
  "sessionId": "f77c5807-10e5-4eae-ab8e-381ef798b6e6"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Pareto frontier is real but weak/noisy. CaCLR fails to beat linear projection. Decomposition doesn't cleanly separate. Core method contribution collapses.…",
  "leafUuid": "a350538f-450e-48ba-8b6a-80c45f4e54ee",
  "sessionId": "f77c5807-10e5-4eae-ab8e-381ef798b6e6"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Multilingual probe calibration field diagnostic",
  "sessionId": "f77c5807-10e5-4eae-ab8e-381ef798b6e6"
}
```

---
