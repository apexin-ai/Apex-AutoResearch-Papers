# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Claims 1 and 4 fully hold. Claim 2 partially holds (decomposition works bu

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/2ff52ae3-7621-49aa-af5a-5d93d8966c1d.jsonl`
- **Structured JSON:** [`0d1fafda4f3a2c7a75f0.json`](../../sessions/0d/0d1fafda4f3a2c7a75f0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:02:16.720Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:02:16.720Z",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Claims 1 and 4 fully hold. Claim 2 partially holds (decomposition works but is noisy). Claim 3 is mixed — CaCLR helps but only marginally beats linear projection on high/mid-resource languages and fails to separate on low-resource. Paper needs rebalancing: elevate discovery/analysis, moderate method claims.\n核心假设：['Pareto frontier replicates on both architectures but with different shapes — Qwen3 shows clear tradeoff, Llama4 is flatter or noisier', 'CaCLR outperforms zero-shot and mean-shift clearly, but only matches or marginally beats linear projection (within 1-2pp on most languages)', 'Difficulty projection removes some but not most transfer gap; capability-specific residual is noisy and confounded with language-family effects', 'Orthogonality generalizes but with higher variance in low-resource languages (cosine 0.05-0.20)', 'Low-resource languages show inconsistent zero-shot transfer; 2-3 of 5 low-resource langs fail AUROC 0.60 threshold']\n关键指标范围：{'en_auroc_best_layer': [0.77, 0.83], 'zs_transfer_auroc_mean_19lang': [0.64, 0.73], 'zs_transfer_drop_mean_pp': [8, 18], 'caclr_vs_linproj_auroc_delta_pp': [0.5, 2.5], 'caclr_ece_reduction_vs_tempcal_pct': [12, 28], 'pareto_depth_transfer_rank_corr': [0.5, 0.78], 'decomp_difficulty_var_explained_pct': [25, 50], 'orthogonality_cosine_mean': [0.04, 0.15], 'low_resource_zs_pass_rate': [0.4, 0.7], 'caclr_improvement_pass_rate': [0.6, 0.85], 'pareto_frontier_agreement_across_arch': [0.55, 0.8]}\n叙事方向：Rebalance toward discovery + analysis. Claim 1 (Pareto frontier) becomes the headline contribution — first systematic characterization of depth-transferability tradeoff across architectures and 20 languages. Claim 2 reframes decomposition as 'partial but prescriptive': difficulty component is clearly transferable, capability residual is noisy but the decomposition still predicts when simple baselines suffice vs when CaCLR helps. Claim 3 softens: CaCLR is presented as 'matching or exceeding the best simple baseline (linear projection) while requiring no target-language data at all' — emphasize the zero-label setting rather than raw metric superiority. Add ablation showing where CaCLR's consistency term specifically helps (likely mid-resource languages). Claim 4 presented with resource-tier analysis showing orthogonality is robust for well-represented languages. Headline shifts to: 'Cross-lingual calibration probes reveal architecture-dependent Pareto frontier; CaCLR matches supervised transfer without target labels.'\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: xling_calib_direction\nfocus: Core submission for EACL 2027 ARR: 2 models (Qwen3-235B + Llama 4 Scout) × 20 languages. Key risks: (1) CaCLR may not outperform simple linear projection; (2) difficulty-shared vs capability-specific decomposition may not cleanly separate; (3) orthogonality claim 4 may be seen as incremental. MVP showed mean-shift completely fails, Pareto tradeoff directly observed at L24 vs L27.\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) shifts the Pareto frontier by jointly optimizing calibration and cross-lingual invariance, enabling effective probe transfer at deeper, better-calibrated layers without target-language correctness labels.\n- MVP evidence: Mean-shift fails entirely (0/5 languages improved) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, and propose CaCLR to shift the frontier. This is both a field-level viability test and a practical method contribution.\n- **Headline template**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak\"** → 5 transfer conditions tested. Mean-shift failure (MVP-confirmed) motivates CaCLR. Mean-shift works for Xiao et al.'s knowledge boundary but fails for correctness — important finding.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR).\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request.\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    INT8 weight quantization.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: Needs 2× RTX 6000 PRO 96GB at INT8.\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency. Train CaCLR probes using English labels + unlabeled\n    parallel activations. Compare vs zero-shot, mean-shift, linear projection, few-shot\n    (25/100) across full Pareto frontier for both models × 20 languages. Hyperparameter\n    tuning (α, β) on held-out English + 5-language validation.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021.\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: Need IRT difficulty scores from GlobalMMLU or external source.\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'INT8 validation ablation: compare INT8 vs FP16 probing results at\n    5 representative layers for Llama 4 Scout on 5% random subset. Validates that\n    INT8 quantization doesn''t distort correctness signals.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 31B Dense (60 layers, dense, FP16): third architecture for\n    camera-ready. Full Pareto frontier, 20+ languages. Provides dense vs MoE architectural\n    contrast.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: failed\n  metrics:\n    bug: layer_config_mismatch\n    detail: extract_activations.py used --layers 2,6,10,14,18,22,26 but train_probe.py\n      and transfer_eval.py used default layers 0,4,8,12,16,20,24,28,31. Probe training\n      skipped all layers (activation files not found). Activations (42 files) are\n      valid and reusable.\n    fix: Add --layers 2,6,10,14,18,22,26 to train_probe.py and transfer_eval.py in\n      run_mvp_002.sh\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: RUNNING\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    bug: layer_config_mismatch\n    detail: extract_activations.py used --layers 2,6,10,14,18,22,26 but train_probe.py\n      and transfer_eval.py used default layers 0,4,8,12,16,20,24,28,31. Probe training\n      skipped all layers (activation files not found). Activations (42 files) are\n      valid and reusable.\n    fix: Add --layers 2,6,10,14,18,22,26 to train_probe.py and transfer_eval.py in\n      run_mvp_002.sh\n- exp_id: mvp_003\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T19:02:16.723Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:02:16.723Z",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-20T19:02:16.752Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Claims 1 and 4 fully hold. Claim 2 partially holds (decomposition works but is noisy). Claim 3 is mixed — CaCLR helps but only marginally beats linear projection on high/mid-resource languages and fails to separate on low-resource. Paper needs rebalancing: elevate discovery/analysis, moderate method claims.
核心假设：['Pareto frontier replicates on both architectures but with different shapes — Qwen3 shows clear tradeoff, Llama4 is flatter or noisier', 'CaCLR outperforms zero-shot and mean-shift clearly, but only matches or marginally beats linear projection (within 1-2pp on most languages)', 'Difficulty projection removes some but not most transfer gap; capability-specific residual is noisy and confounded with language-family effects', 'Orthogonality generalizes but with higher variance in low-resource languages (cosine 0.05-0.20)', 'Low-resource languages show inconsistent zero-shot transfer; 2-3 of 5 low-resource langs fail AUROC 0.60 threshold']
关键指标范围：{'en_auroc_best_layer': [0.77, 0.83], 'zs_transfer_auroc_mean_19lang': [0.64, 0.73], 'zs_transfer_drop_mean_pp': [8, 18], 'caclr_vs_linproj_auroc_delta_pp': [0.5, 2.5], 'caclr_ece_reduction_vs_tempcal_pct': [12, 28], 'pareto_depth_transfer_rank_corr': [0.5, 0.78], 'decomp_difficulty_var_explained_pct': [25, 50], 'orthogonality_cosine_mean': [0.04, 0.15], 'low_resource_zs_pass_rate': [0.4, 0.7], 'caclr_improvement_pass_rate': [0.6, 0.85], 'pareto_frontier_agreement_across_arch': [0.55, 0.8]}
叙事方向：Rebalance toward discovery + analysis. Claim 1 (Pareto frontier) becomes the headline contribution — first systematic characterization of depth-transferability tradeoff across architectures and 20 languages. Claim 2 reframes decomposition as 'partial but prescriptive': difficulty component is clearly transferable, capability residual is noisy but the decomposition still predicts when simple baselines suffice vs when CaCLR helps. Claim 3 softens: CaCLR is presented as 'matching or exceeding the best simple baseline (linear projection) while requiring no target-language data at all' — emphasize the zero-label setting rather than raw metric superiority. Add ablation showing where CaCLR's consistency term specifically helps (likely mid-resource languages). Claim 4 presented with resource-tier analysis showing orthogonality is robust for well-represented languages. Headline shifts to: 'Cross-lingual calibration probes reveal architecture-dependent Pareto frontier; CaCLR matches supervised transfer without target labels.'

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
tier: median
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
  "promptId": "961d2670-53c4-4e07-b82c-db2a80244bf8",
  "type": "user",
  "uuid": "2251a4a2-0883-47b6-aefc-92600ba9efea",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:02:16.751Z_

```json
{
  "parentUuid": "2251a4a2-0883-47b6-aefc-92600ba9efea",
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
  "uuid": "1d7d23e4-409d-46fd-859c-abc312a5e322",
  "timestamp": "2026-05-20T19:02:16.751Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:02:16.751Z_

```json
{
  "parentUuid": "1d7d23e4-409d-46fd-859c-abc312a5e322",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6da93e10-cfb7-4f29-a59b-fc256431ab6e",
  "timestamp": "2026-05-20T19:02:16.751Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Claims 1 and 4 fully hold. Claim 2 partially holds (decomposition works but is noisy). Claim 3 is mixed — CaCLR helps but only marginally beats linear pr…",
  "leafUuid": "6da93e10-cfb7-4f29-a59b-fc256431ab6e",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Multilingual correctness probe transfer pareto frontier",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d"
}
```

---

### Assistant

_source line 8 · 2026-05-20T19:05:50.290Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experimental data for each "planned" experiment in the experiment plan, under the "median" tier assumptions. I need to provide specific predicted results with rationales for each experiment, formatted as YAML.

Let me go through each planned experiment and generate detailed predictions consistent with the median tier definition.

The median tier says:
- Claims 1 and 4 fully hold
- Claim 2 partially holds (decomposition works but is noisy)
- Claim 3 is mixed — CaCLR helps but only marginally beats linear projection on high/mid-resource languages and fails to separate on low-resource


- The paper needs rebalancing to elevate discovery and analysis while moderating method claims

Now I'm establishing the key metric ranges that should anchor the predicted results: English AUROC peaks around 0.77-0.83, zero-shot transfer averages 0.64-0.73 across languages, performance drops 8-18 percentage points on transfer, CaCLR's advantage over linear projection is modest at 0.5-2.5 percentage points, and calibration improvements from CaCLR versus temperature scaling range from 12-28 percent.

I'm also tracking several other critical metrics including Pareto frontier correlation, variance explained by difficulty decomposition, orthogonality measures, and pass rates across low-resource and improved settings, then planning the five core experiments: full Pareto frontiers on two large models, CaCLR implementation with comparisons, difficulty-controlled ablations, and cross-lingual orthogonality analysis.

Now I'm laying out the detailed experimental data across all planned runs. For Qwen3-235B with its 94 layers, I expect the best English performance around layers 72-80, with a significant transfer drop from those deep layers, so the optimal transfer point would sit around 40-50% depth. For Llama 4 Scout's 48 layers, the best English layer should be around 36-40 with slightly flatter Pareto characteristics.

Writing YAML output... better on English, while MLPs show marginal gains. Looking at the additional benchmarks, I'm seeing consistent patterns across Belebele and MMLU-ProX with slightly different absolute values. The INT8 quantization validation shows negligible differences from FP16, so that's not a concern. Gemma 4 provides an interesting architectural contrast with its dense structure and different Pareto frontier shape. Expanding to more languages reveals similar trends overall, though low-resource languages exhibit higher variability. Now I'm organizing all these findings into a comprehensive YAML structure, making sure the language groupings and experimental parameters stay internally consistent across the different plans. Looking at the performance metrics for Qwen3-235B across its probed layers, the best English AUROC peaks at layer 76 with solid calibration, but there's a clear tension between optimizing for English performance versus zero-shot transfer capability—layer 48 offers the best transfer performance across 19 languages at 0.721 AUROC, while sticking with the English-optimal layer 76 drops transfer performance to 0.654, a notable 0.158 point gap.

The transfer performance shows a strong negative correlation with layer depth, and when I break down the 19 languages by resource level at the optimal transfer layer, high-resource languages cluster around 0.752 mean AUROC, mid-resource languages around 0.710, and low-resource languages significantly lower at 0.602. I'm working through the metrics for different language resource groups at layer L76, calculating means for high-resource, mid-resource, and low-resource languages to see if I can hit the target range of 0.68 by adjusting the individual scores. .666 overall, which is reasonable but on the lower end. I need to clarify whether the transfer AUROC is pooled across both models or computed at the Pareto-optimal layer, and I should report metrics per experiment to ensure internal consistency. Looking at the language setup more carefully—"20 typologically diverse languages" likely means 20 total including English, so transfer evaluation would be on 19 non-English languages.

The metric name `zs_transfer_auroc_mean_19lang` confirms this split. For the low-resource languages, a pass rate of 0.4-0.7 translates to 2-3 out of 5 languages succeeding, and the CaCLR improvement pass rate of 0.6-0.85 means the method improves performance on roughly 11-16 of the 19 transfer languages. Now I'll construct the full YAML output with these metrics organized by experiment.

I need to be careful here—the user specifically asked for details on planned experiments only. Scanning through the experiment plan, all ten plan_00X entries have status: planned, while the MVP experiments are either done or still running, so I'll focus on expanding just those ten planned experiments with comprehensive, internally consistent data.

Now I'm thinking through the performance characteristics across different model architectures. For Qwen3 with its 94 layers and MoE structure, I'd expect a clear tradeoff pattern where early layers show weaker English performance but better transfer capability, mid-layers hit the sweet spot with moderate English AUROC and optimal transfer, and deeper layers sacrifice transfer quality as English performance plateaus. For Llama 4 Scout with its 48 layers, I need to map out a similar but compressed curve that reflects its smaller architecture.

For the YAML output, I'm planning to organize the results by experiment type—layer-wise profiles and per-language transfer metrics for the main experiments, comparison tables for methods, decomposition and orthogonality measurements for the analysis experiments, and cross-benchmark validation. I'll keep the output focused and well-structured rather than exhaustive.

Now I'm defining the language set across 20 languages spanning high-resource (English, Chinese, German, French, Spanish, Japanese, Russian) and mid-resource categories (Arabic, Hindi, Korean, Portuguese, Vietnamese, Thai, Turkish, Polish, Swahili, and others).

Writing YAML structure... Writing YAML structure... Looking at the performance metrics for CaCLR, decomposition, orthogonality, and low-resource scenarios—all the values fall within their expected ranges. Now I need to generate the full YAML configuration, though I should verify one more detail about the pass rate threshold before proceeding. I'm reconsidering the pass rates for each language based on the stronger model performance. Swahili likely crosses the threshold at 0.63, Telugu at 0.64, and Malay at 0.61, while Amharic and Yoruba fall short—giving me 3 passes out of 5, which aligns with the 0.6 pass rate I was targeting. , te 0.61, my 0.57, am 0.55, yo 0.51) — so about 2.5 out of 5 languages pass on average, which falls within the expected range. Rather than overthinking the exact breakdown, I should just write out the YAML structure now and verify everything's internally consistent and within the right bounds. For the tables, I'll format them as a list of row objects in YAML, which keeps things readable while staying structured.

This is going to be quite lengthy, so I need to be strategic about what to include — I'll focus on summary statistics and a few representative detailed tables per experiment rather than exhaustive breakdowns. For per-language results, showing tier means and a handful of example languages instead of all 19 will keep it manageable.

Now I'm drafting the full YAML with a clear plan for each experiment: key summary metrics in the expected results, then selective tables like the English AUROC progression across layers, zero-shot transfer performance at critical checkpoints, and overall Pareto summaries, followed by the figures. Pareto frontier plot description with analysis interpretation. I'm outlining several experimental plans: Llama 4 Scout with a flatter frontier, CaCLR with comparison tables and shifted frontier visualization, decomposition analysis with variance and residual transfer, orthogonality metrics by language and architecture, probe complexity comparisons, cross-benchmark validation, INT8 versus FP16 deltas, Gemma 4 projections based on architecture expectations, and extended language trend projections. Now I'm selecting specific layer indices carefully—for Qwen3-235B's 94 layers I'll sample every fourth layer starting from L0 through L92 to get 24 representative layers, and for Llama 4 Scout's 48 layers I'll do the same sampling pattern.

Generating AUROC curve data... Looking at the zero-shot transfer scores continuing to decline through L88 and L92, I'm noticing the pattern more clearly now—there's a trade-off between English performance and cross-lingual transfer. At L76 where English peaks, the drop to transfer performance is about 17 percentage points, which fits the expected range. The real sweet spot appears to be L40, where transfer reaches its maximum at 0.724 despite English being slightly lower, suggesting a negative correlation between depth and transfer capability across layers. The correlation between depth and transfer performance is actually what I need to focus on here. Since transfer peaks around layer 40 and then steadily declines while depth keeps increasing, I should compute the Spearman rank correlation across all 24 layers to see how consistently deeper layers correspond to worse transfer performance. L40 has highest transfer (rank 1)
L36 rank 2
L32 rank 3
L44 rank 4
L28 rank 5
...
L0 has lowest (rank ~24)
L92 rank ~20

This isn't really a clean negative correlation. Let me reconsider what this metric means.

Looking at the metric name again: `pareto_depth_transfer_rank_corr: [0.5, 0.78]`. These are positive values! So it might be the correlation between depth and transfer quality, meaning deeper layers have higher transfer? That contradicts the Pareto story.

Or maybe it's the absolute value of the correlation? Or the rank correlation of the Pareto-optimal points? Or the correlation between optimal-English-depth rank and optimal-transfer-depth rank across languages?

I think the most natural interpretation is: for each language, compute the rank correlation between layer depth and transfer AUROC, then average across languages. A moderate positive correlation of 0.5-0.78 would suggest deeper layers generally perform better for transfer, though the relationship isn't perfectly linear due to the Pareto tradeoff at deeper layers. Alternatively, it could be the Spearman correlation between which depth gives the best English AUROC and which depth gives the best transfer performance across the 19 languages—essentially checking if the optimal layer depths align between English and cross-lingual transfer. The rankings diverge significantly at the top, which explains the moderate correlation—the layers that perform best on English aren't the same ones that transfer well across languages. Let me work through the Spearman correlation by assigning ranks to each layer in both orderings to quantify this disagreement. Hmm, these are quite different rankings. The Spearman correlation would be low or even negative. Let me reconsider.

Actually, maybe the transfer curve doesn't peak that early. If transfer peaks around L32-L40, while English peaks at L76, the curves mostly move together until mid-depth, then diverge. For 24 data points where the first 8-10 agree in ordering and the rest diverge, the overall Spearman might be around 0.3-0.5.

Actually wait, I think I'm computing this wrong. Both English and transfer AUROC increase from early layers and then for English they keep increasing, for transfer they eventually decrease. So both would have layers 0-36 ranked similarly at the bottom, and layers 40-92 would diverge. The correlation of these rankings would be positive because low layers are bad for both, mid layers are moderate-to-good for both, and deep layers are great for English but bad for transfer. With roughly 10 agreeing and 13 disagreeing, the correlation would be moderate negative, but actually the transfer isn't terrible in those deep layers, so the ranking is more nuanced. Let me try a simpler approach and pair each layer's English rank with its transfer rank.

Generating ranking table... Continuing to sum the squared differences, working through the remaining values to get the total.

Now I'm calculating the Spearman correlation coefficient using the formula with n=24 and the sum of squared differences, which gives me about -0.26. That's a stark contrast to the expected range of 0.5 to 0.78, so either I'm misinterpreting what this metric actually represents, or my calculations need rechecking. Let me think about whether this could be measuring something different—maybe the correlation between layer depth and the transfer performance drop rather than between the two ranking systems.

Given the expected range, the most plausible explanation is that this metric captures how consistently the transfer performance degrades with depth across different languages, or perhaps it's the Spearman correlation of the Pareto frontier points specifically rather than all layers. It could also be measuring agreement on which layers are optimal for transfer across language pairs, which would indicate consistency in the frontier shape.

Actually, I think I've got it—this is likely the absolute value of the Spearman correlation between English AUROC and zero-shot transfer AUROC measured across the layers on the Pareto frontier, where the tradeoff between the two metrics should be clean and negative. My current correlation of -0.26 suggests the transfer curve isn't steep enough relative to the performance gains, so I need to adjust the transfer penalty to make that tradeoff more pronounced.

The real issue is that early layers are pulling the correlation toward zero because both metrics improve together there, masking the negative relationship in the deeper layers. If I focus only on the middle-to-deep range where the actual tradeoff happens, the correlation becomes much more negative.

Generating ranking table... I'm overthinking the rank correlation metric—I should just report summary statistics within the given ranges and make sure the detailed tables are internally consistent, rather than trying to verify every derived number from raw data. Let me write out the YAML with a clear structure: summary metrics in range, detailed per-layer and per-language tables that align directionally, and solid rationales for the patterns I'm showing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6da93e10-cfb7-4f29-a59b-fc256431ab6e",
  "isSidechain": false,
  "requestId": "req_011CbELbaED2cK52HYhqD65U",
  "type": "assistant",
  "uuid": "18e0856b-31d2-471f-b37f-4843129ee002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbsuPNTrfp4WhPvhRAz6PS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10931,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10931,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10931,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10931
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

_source line 9 · 2026-05-20T19:05:50.292Z_

Let me first check the project structure for any existing files I should reference for consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18e0856b-31d2-471f-b37f-4843129ee002",
  "isSidechain": false,
  "requestId": "req_011CbELbaED2cK52HYhqD65U",
  "type": "assistant",
  "uuid": "edb11e87-2905-4d07-9372-809621a6abfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbsuPNTrfp4WhPvhRAz6PS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10931,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10931,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10931,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10931
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

_source line 10 · 2026-05-20T19:05:50.750Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01RPZDSSihQnJh8pMLXf6kaJ`</summary>

```json
{
  "pattern": "**/*.{md,yaml,yml,json}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edb11e87-2905-4d07-9372-809621a6abfb",
  "isSidechain": false,
  "requestId": "req_011CbELbaED2cK52HYhqD65U",
  "type": "assistant",
  "uuid": "76d145cc-52b6-44e4-a46d-c9f3da02ef57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbsuPNTrfp4WhPvhRAz6PS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10931,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10931,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10931,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10931
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

_source line 11 · 2026-05-20T19:05:50.821Z_

<details><summary>↩ Tool result · `toolu_01YCBHX7Bn2e4jMbVxSrE3wc`</summary>

```text
projects/xling_calib_direction/code/extract_activations.py
projects/xling_calib_direction/code/train_probe.py
projects/xling_calib_direction/code/transfer_eval.py
projects/xling_calib_direction/code/analyze_results.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bede181-8a34-4090-8cb2-e593ab1d3a8b",
  "isSidechain": false,
  "promptId": "961d2670-53c4-4e07-b82c-db2a80244bf8",
  "type": "user",
  "uuid": "a6007ae0-aebd-48bc-b10f-82f2bd4801cc",
  "toolUseResult": {
    "filenames": [
      "projects/xling_calib_direction/code/extract_activations.py",
      "projects/xling_calib_direction/code/train_probe.py",
      "projects/xling_calib_direction/code/transfer_eval.py",
      "projects/xling_calib_direction/code/analyze_results.py"
    ],
    "durationMs": 11,
    "numFiles": 4,
    "truncated": false
  },
  "sourceToolAssistantUUID": "1bede181-8a34-4090-8cb2-e593ab1d3a8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T19:05:50.777Z_

<details><summary>↩ Tool result · `toolu_01RPZDSSihQnJh8pMLXf6kaJ`</summary>

```text
config/approvals.yaml
config/mcp_config.json
config/backend.yaml
config/pool.json
config/feishu.yaml
config/mcp_config_director.json
config/mcp_config_reviewer.json
.claude/sessions/no_project_9d2a9208/CLAUDE.md
.claude/sessions/no_project_9d2a9208/AGENTS.md
config/mcp_config_no_project.json
config/mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json
workspace.yaml
config/venue_registry.yaml
config/venue_rules/corl-2026.yaml
config/venue_rules/emnlp-2026.yaml
idea_generator/ideas.yaml
config/session_state.json
projects/xling_calib_direction/literature_map.yaml
projects/xling_calib_direction/.claude/sessions/distiller_70eed89a/CLAUDE.md
projects/xling_calib_direction/.claude/sessions/distiller_70eed89a/AGENTS.md
config/mcp_config_distiller.json
config/claude_sessions.json
projects/xling_calib_direction/distill_tmp/karandikar2021sbece.yaml
projects/xling_calib_direction/distill_tmp/miao2026closing.yaml
projects/xling_calib_direction/distill_tmp/civelli2026shared.yaml
projects/xling_calib_direction/distill_tmp/confidence_manifold2026.yaml
projects/xling_calib_direction/distill_tmp/xiao2025knowledge.yaml
projects/xling_calib_direction/distill_tmp/joshi2025calibration.yaml
projects/xling_calib_direction/distill_tmp/khanmohammadi2025ccps.yaml
projects/xling_calib_direction/distill_tmp/liu2025middle.yaml
projects/xling_calib_direction/distill_tmp/ji2025calibrating.yaml
projects/xling_calib_direction/distill_tmp/ravisankar2026dali.yaml
projects/xling_calib_direction/distill_tmp/zhou2025lace.yaml
projects/xling_calib_direction/distill_tmp/miao2026coral.yaml
config/resources.yaml
skills/projects/xling_calib_direction/distilled-research.skill.md
skills/projects/xling_calib_direction/distilled-writing.skill.md
config/secrets/xling_calib_direction/manifest.yaml
projects/xling_calib_direction/checkpoints/mvp_001_PREPARING_20260520T141702.json
config/mcp_config_worker_69e382e805b6f185c49ecc4b6d1f2d44.json
projects/xling_calib_direction/checkpoints/mvp_001_QUEUED_20260520T142501.json
projects/xling_calib_direction/checkpoints/mvp_001_RUNNING_20260520T142506.json
projects/xling_calib_direction/logs/workers/worker_code_mvp_001_setup_and_run_20260520T141803_result.json
config/mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
projects/xling_calib_direction/logs/workers/worker_diag_mvp_001_download_check_20260520T143045_result.json
config/mcp_config_worker_8164f16cea05223301ec10d99f320a22.json
config/mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json
projects/xling_calib_direction/logs/workers/worker_prep_mvp_001_parallel_tasks_20260520T150620_result.json
projects/xling_calib_direction/checkpoints/mvp_002_PREPARING_20260520T162627.json
projects/xling_calib_direction/checkpoints/mvp_002_QUEUED_20260520T170009.json
projects/xling_calib_direction/checkpoints/mvp_002_RUNNING_20260520T170020.json
projects/xling_calib_direction/logs/workers/worker_run_mvp_002_submit_20260520T165936_result.json
projects/xling_calib_direction/checkpoints/mvp_001_RUNNING_20260520T182006.json
projects/xling_calab_direction/registry.yaml
projects/xling_calib_direction/checkpoints/mvp_001_DONE_20260520T182309.json
config/mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
projects/xling_calib_direction/logs/workers/worker_analysis_mvp_001_gate_recheck_20260520T182750_result.json
projects/xling_calib_direction/checkpoints/mvp_003_QUEUED_20260520T184756.json
projects/xling_calib_direction/checkpoints/mvp_003_RUNNING_20260520T184808.json
projects/xling_calib_direction/logs/workers/worker_analysis_mvp_001_layer27_supplement_20260520T184655_result.json
projects/xling_calib_direction/memory.md
projects/xling_calib_direction/decisions.yaml
projects/xling_calib_direction/docs/IDEA_BRIEF.md
config/projects/xling_calib_direction.yaml
config/keepalive.json
global/logs/pending_queue/dc357fb05060.json
projects/xling_calib_direction/.claude/sessions/agent_3e57a809/CLAUDE.md
projects/xling_calib_direction/.claude/sessions/agent_3e57a809/AGENTS.md
projects/xling_calib_direction/checkpoints/mvp_002_RUNNING_20260520T185540.json
projects/xling_calib_direction/paper_framing.md
projects/xling_calib_direction/registry.yaml
projects/xling_calib_direction/checkpoints/mvp_002_DONE_20260520T185550.json
projects/xling_calib_direction/report.md
projects/xling_calib_direction/logs/workers/worker_analysis_mvp_002_diagnose_20260520T185417_result.json
global/logs/pending_queue/65c5d438af6e.json
projects/xling_calib_direction/experiment_plan.yaml
projects/xling_calib_direction/dream_registry.yaml
projects/xling_calib_direction/mistakes.yaml
global/logs/pending_queue/a21a5745872e.json
projects/xling_calib_direction/.claude/sessions/director_a0a38807/CLAUDE.md
projects/xling_calib_direction/.claude/sessions/director_a0a38807/AGENTS.md
projects/xling_calib_direction/ROADMAP.md
projects/xling_calib_direction/logs/workers/worker_code_mvp_003_llama_20260520T182822_result.json
global/logs/workers/registry.json
global/logs/pending_queue/18e50b693ad5.json
global/logs/pending_queue/8ab42e5c78b6.json
.claude/CLAUDE.md
AGENTS.md
projects/xling_calib_direction/.claude/CLAUDE.md
projects/xling_calib_direction/AGENTS.md
projects/xling_calib_direction/.claude/sessions/reviewer_b0408cba/CLAUDE.md
projects/xling_calib_direction/.claude/sessions/reviewer_b0408cba/AGENTS.md
state/pool_state_last.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76d145cc-52b6-44e4-a46d-c9f3da02ef57",
  "isSidechain": false,
  "promptId": "961d2670-53c4-4e07-b82c-db2a80244bf8",
  "type": "user",
  "uuid": "c61c2833-da4c-49c9-a8a7-f9feecbbcc07",
  "toolUseResult": {
    "filenames": [
      "config/approvals.yaml",
      "config/mcp_config.json",
      "config/backend.yaml",
      "config/pool.json",
      "config/feishu.yaml",
      "config/mcp_config_director.json",
      "config/mcp_config_reviewer.json",
      ".claude/sessions/no_project_9d2a9208/CLAUDE.md",
      ".claude/sessions/no_project_9d2a9208/AGENTS.md",
      "config/mcp_config_no_project.json",
      "config/mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json",
      "workspace.yaml",
      "config/venue_registry.yaml",
      "config/venue_rules/corl-2026.yaml",
      "config/venue_rules/emnlp-2026.yaml",
      "idea_generator/ideas.yaml",
      "config/session_state.json",
      "projects/xling_calib_direction/literature_map.yaml",
      "projects/xling_calib_direction/.claude/sessions/distiller_70eed89a/CLAUDE.md",
      "projects/xling_calib_direction/.claude/sessions/distiller_70eed89a/AGENTS.md",
      "config/mcp_config_distiller.json",
      "config/claude_sessions.json",
      "projects/xling_calib_direction/distill_tmp/karandikar2021sbece.yaml",
      "projects/xling_calib_direction/distill_tmp/miao2026closing.yaml",
      "projects/xling_calib_direction/distill_tmp/civelli2026shared.yaml",
      "projects/xling_calib_direction/distill_tmp/confidence_manifold2026.yaml",
      "projects/xling_calib_direction/distill_tmp/xiao2025knowledge.yaml",
      "projects/xling_calib_direction/distill_tmp/joshi2025calibration.yaml",
      "projects/xling_calib_direction/distill_tmp/khanmohammadi2025ccps.yaml",
      "projects/xling_calib_direction/distill_tmp/liu2025middle.yaml",
      "projects/xling_calib_direction/distill_tmp/ji2025calibrating.yaml",
      "projects/xling_calib_direction/distill_tmp/ravisankar2026dali.yaml",
      "projects/xling_calib_direction/distill_tmp/zhou2025lace.yaml",
      "projects/xling_calib_direction/distill_tmp/miao2026coral.yaml",
      "config/resources.yaml",
      "skills/projects/xling_calib_direction/distilled-research.skill.md",
      "skills/projects/xling_calib_direction/distilled-writing.skill.md",
      "config/secrets/xling_calib_direction/manifest.yaml",
      "projects/xling_calib_direction/checkpoints/mvp_001_PREPARING_20260520T141702.json",
      "config/mcp_config_worker_69e382e805b6f185c49ecc4b6d1f2d44.json",
      "projects/xling_calib_direction/checkpoints/mvp_001_QUEUED_20260520T142501.json",
      "projects/xling_calib_direction/checkpoints/mvp_001_RUNNING_20260520T142506.json",
      "projects/xling_calib_direction/logs/workers/worker_code_mvp_001_setup_and_run_20260520T141803_result.json",
      "config/mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json",
      "projects/xling_calib_direction/logs/workers/worker_diag_mvp_001_download_check_20260520T143045_result.json",
      "config/mcp_config_worker_8164f16cea05223301ec10d99f320a22.json",
      "config/mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json",
      "projects/xling_calib_direction/logs/workers/worker_prep_mvp_001_parallel_tasks_20260520T150620_result.json",
      "projects/xling_calib_direction/checkpoints/mvp_002_PREPARING_20260520T162627.json",
      "projects/xling_calib_direction/checkpoints/mvp_002_QUEUED_20260520T170009.json",
      "projects/xling_calib_direction/checkpoints/mvp_002_RUNNING_20260520T170020.json",
      "projects/xling_calib_direction/logs/workers/worker_run_mvp_002_submit_20260520T165936_result.json",
      "projects/xling_calib_direction/checkpoints/mvp_001_RUNNING_20260520T182006.json",
      "projects/xling_calab_direction/registry.yaml",
      "projects/xling_calib_direction/checkpoints/mvp_001_DONE_20260520T182309.json",
      "config/mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json",
      "projects/xling_calib_direction/logs/workers/worker_analysis_mvp_001_gate_recheck_20260520T182750_result.json",
      "projects/xling_calib_direction/checkpoints/mvp_003_QUEUED_20260520T184756.json",
      "projects/xling_calib_direction/checkpoints/mvp_003_RUNNING_20260520T184808.json",
      "projects/xling_calib_direction/logs/workers/worker_analysis_mvp_001_layer27_supplement_20260520T184655_result.json",
      "projects/xling_calib_direction/memory.md",
      "projects/xling_calib_direction/decisions.yaml",
      "projects/xling_calib_direction/docs/IDEA_BRIEF.md",
      "config/projects/xling_calib_direction.yaml",
      "config/keepalive.json",
      "global/logs/pending_queue/dc357fb05060.json",
      "projects/xling_calib_direction/.claude/sessions/agent_3e57a809/CLAUDE.md",
      "projects/xling_calib_direction/.claude/sessions/agent_3e57a809/AGENTS.md",
      "projects/xling_calib_direction/checkpoints/mvp_002_RUNNING_20260520T185540.json",
      "projects/xling_calib_direction/paper_framing.md",
      "projects/xling_calib_direction/registry.yaml",
      "projects/xling_calib_direction/checkpoints/mvp_002_DONE_20260520T185550.json",
      "projects/xling_calib_direction/report.md",
      "projects/xling_calib_direction/logs/workers/worker_analysis_mvp_002_diagnose_20260520T185417_result.json",
      "global/logs/pending_queue/65c5d438af6e.json",
      "projects/xling_calib_direction/experiment_plan.yaml",
      "projects/xling_calib_direction/dream_registry.yaml",
      "projects/xling_calib_direction/mistakes.yaml",
      "global/logs/pending_queue/a21a5745872e.json",
      "projects/xling_calib_direction/.claude/sessions/director_a0a38807/CLAUDE.md",
      "projects/xling_calib_direction/.claude/sessions/director_a0a38807/AGENTS.md",
      "projects/xling_calib_direction/ROADMAP.md",
      "projects/xling_calib_direction/logs/workers/worker_code_mvp_003_llama_20260520T182822_result.json",
      "global/logs/workers/registry.json",
      "global/logs/pending_queue/18e50b693ad5.json",
      "global/logs/pending_queue/8ab42e5c78b6.json",
      ".claude/CLAUDE.md",
      "AGENTS.md",
      "projects/xling_calib_direction/.claude/CLAUDE.md",
      "projects/xling_calib_direction/AGENTS.md",
      "projects/xling_calib_direction/.claude/sessions/reviewer_b0408cba/CLAUDE.md",
      "projects/xling_calib_direction/.claude/sessions/reviewer_b0408cba/AGENTS.md",
      "state/pool_state_last.json"
    ],
    "durationMs": 16,
    "numFiles": 93,
    "truncated": false
  },
  "sourceToolAssistantUUID": "76d145cc-52b6-44e4-a46d-c9f3da02ef57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T19:05:50.808Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YCBHX7Bn2e4jMbVxSrE3wc`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c61c2833-da4c-49c9-a8a7-f9feecbbcc07",
  "isSidechain": false,
  "requestId": "req_011CbELbaED2cK52HYhqD65U",
  "type": "assistant",
  "uuid": "1bede181-8a34-4090-8cb2-e593ab1d3a8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbsuPNTrfp4WhPvhRAz6PS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10931,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10931,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10931,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10931
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

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Claims 1 and 4 fully hold. Claim 2 partially holds (decomposition works but is noisy). Claim 3 is mixed — CaCLR helps but only marginally beats linear pr…",
  "leafUuid": "a6007ae0-aebd-48bc-b10f-82f2bd4801cc",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Multilingual correctness probe transfer pareto frontier",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d"
}
```

---

### Tool call

_source line 16 · 2026-05-20T19:05:56.584Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WiR8y9QxYzagRLHbZnkSKB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6007ae0-aebd-48bc-b10f-82f2bd4801cc",
  "isSidechain": false,
  "requestId": "req_011CbELsMYfVv31kDJvdGBmV",
  "type": "assistant",
  "uuid": "b75ddb8e-8581-4d86-a834-a28ae500cd3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012cgbVJvr2VY8auxxjfoJHt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13292,
      "cache_read_input_tokens": 22772,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 22772,
          "cache_creation_input_tokens": 13292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13292
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

_source line 17 · 2026-05-20T19:05:56.590Z_

<details><summary>↩ Tool result · `toolu_01WiR8y9QxYzagRLHbZnkSKB`</summary>

```text
1	experiments:
2	  # === P0: Core submission (must complete for EACL 2027 ARR Aug 3) ===
3	
4	  - id: plan_001
5	    claim: 1
6	    description: >
7	      Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8):
8	      extract activations at every 4th layer (24 probed layers),
9	      20 typologically diverse languages, train English correctness probes
10	      (logistic regression + 2-layer MLP), evaluate 5 transfer conditions
11	      (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).
12	    priority: P0
13	    gpu_budget_hours: 80
14	    deps: []
15	    notes: "Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request."
16	
17	  - id: plan_002
18	    claim: 1
19	    description: >
20	      Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8):
21	      extract activations at every 4th layer (12 probed layers),
22	      20 languages, 5 transfer conditions. INT8 weight quantization.
23	    priority: P0
24	    gpu_budget_hours: 40
25	    deps: []
26	    notes: "Needs 2× RTX 6000 PRO 96GB at INT8."
27	
28	  - id: plan_003
29	    claim: 3
30	    description: >
31	      CaCLR implementation and comparative evaluation:
32	      L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency.
33	      Train CaCLR probes using English labels + unlabeled parallel activations.
34	      Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100)
35	      across full Pareto frontier for both models × 20 languages.
36	      Hyperparameter tuning (α, β) on held-out English + 5-language validation.
37	    priority: P0
38	    gpu_budget_hours: 20
39	    deps: [plan_001, plan_002]
40	    notes: "CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS 2021."
41	
42	  - id: plan_004
43	    claim: 2
44	    description: >
45	      Difficulty-controlled ablation: train IRT difficulty probes (Ridge regression
46	      on human difficulty scores per Civelli et al.), project out difficulty direction
47	      from activations, retrain correctness probes on residuals, evaluate transfer.
48	      10 representative languages × 8 representative layers per model (20-90% depth).
49	    priority: P0
50	    gpu_budget_hours: 15
51	    deps: [plan_001, plan_002]
52	    notes: "Need IRT difficulty scores from GlobalMMLU or external source."
53	
54	  # === P1: Important for strong submission ===
55	
56	  - id: plan_005
57	    claim: 4
58	    description: >
59	      Cross-lingual orthogonality analysis: extract verbalized confidence direction
60	      (prompt model for confidence score, fit probe), compute cosine similarity
61	      with correctness direction across 20 languages × 2 architectures.
62	      Analyze by resource tier (high/mid/low) and language family.
63	    priority: P1
64	    gpu_budget_hours: 10
65	    deps: [plan_001, plan_002]
66	
67	  - id: plan_006
68	    claim: 1
69	    description: >
70	      Probe complexity comparison: logistic regression vs 2-layer MLP
71	      at each probed layer for both models. Compare English accuracy,
72	      cross-lingual transfer degradation, and calibration quality.
73	      Test hypothesis: linear probes transfer better cross-lingually.
74	    priority: P1
75	    gpu_budget_hours: 5
76	    deps: [plan_001, plan_002]
77	    notes: "CPU-bound, uses cached activations."
78	
79	  - id: plan_007
80	    claim: 1
81	    description: >
82	      Additional benchmark evaluation: evaluate best probes + CaCLR
83	      on Belebele (20 languages) and MMLU-ProX (20 languages).
84	      Validates generalization beyond MMLU/GlobalMMLU.
85	    priority: P1
86	    gpu_budget_hours: 30
87	    deps: [plan_001, plan_002, plan_003]
88	
89	  - id: plan_010
90	    claim: 1
91	    description: >
92	      INT8 validation ablation: compare INT8 vs FP16 probing results
93	      at 5 representative layers for Llama 4 Scout on 5% random subset.
94	      Validates that INT8 quantization doesn't distort correctness signals.
95	    priority: P1
96	    gpu_budget_hours: 5
97	    deps: [plan_002]
98	
99	  # === P2: Camera-ready extension ===
100	
101	  - id: plan_008
102	    claim: 1
103	    description: >
104	      Gemma 4 31B Dense (60 layers, dense, FP16): third architecture
105	      for camera-ready. Full Pareto frontier, 20+ languages.
106	      Provides dense vs MoE architectural contrast.
107	    priority: P2
108	    gpu_budget_hours: 30
109	    deps: []
110	
111	  - id: plan_009
112	    claim: 1
113	    description: >
114	      Extended language coverage: expand from 20 to 50+ languages
115	      for camera-ready. Leverages GlobalMMLU/Belebele full language sets.
116	    priority: P2
117	    gpu_budget_hours: 50
118	    deps: [plan_001, plan_002]
119	
120	  # === MVP experiments (completed/running) ===
121	
122	  - id: mvp_validation
123	    claim: 1
124	    description: "MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift"
125	    priority: P0
126	    registry_id: mvp_001
127	    gpu_budget_hours: 2
128	    deps: []
129	
130	  - id: mvp_complementary
131	    claim: 1
132	    description: "MVP robustness: complementary layer set (2,6,10,14,18,22,26)"
133	    priority: P1
134	    registry_id: mvp_002
135	    gpu_budget_hours: 2
136	    deps: [mvp_validation]
137	
138	  - id: mvp_llama_control
139	    claim: 1
140	    description: "MVP cross-architecture: Llama-3.1-8B control experiment"
141	    priority: P1
142	    registry_id: mvp_003
143	    gpu_budget_hours: 3
144	    deps: [mvp_validation]
145	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b75ddb8e-8581-4d86-a834-a28ae500cd3a",
  "isSidechain": false,
  "promptId": "961d2670-53c4-4e07-b82c-db2a80244bf8",
  "type": "user",
  "uuid": "8c43efa4-6d5c-441a-8818-16f6a2658d50",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/experiment_plan.yaml",
      "content": "experiments:\n  # === P0: Core submission (must complete for EACL 2027 ARR Aug 3) ===\n\n  - id: plan_001\n    claim: 1\n    description: >\n      Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8):\n      extract activations at every 4th layer (24 probed layers),\n      20 typologically diverse languages, train English correctness probes\n      (logistic regression + 2-layer MLP), evaluate 5 transfer conditions\n      (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).\n    priority: P0\n    gpu_budget_hours: 80\n    deps: []\n    notes: \"Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request.\"\n\n  - id: plan_002\n    claim: 1\n    description: >\n      Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8):\n      extract activations at every 4th layer (12 probed layers),\n      20 languages, 5 transfer conditions. INT8 weight quantization.\n    priority: P0\n    gpu_budget_hours: 40\n    deps: []\n    notes: \"Needs 2× RTX 6000 PRO 96GB at INT8.\"\n\n  - id: plan_003\n    claim: 3\n    description: >\n      CaCLR implementation and comparative evaluation:\n      L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency.\n      Train CaCLR probes using English labels + unlabeled parallel activations.\n      Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100)\n      across full Pareto frontier for both models × 20 languages.\n      Hyperparameter tuning (α, β) on held-out English + 5-language validation.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [plan_001, plan_002]\n    notes: \"CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS 2021.\"\n\n  - id: plan_004\n    claim: 2\n    description: >\n      Difficulty-controlled ablation: train IRT difficulty probes (Ridge regression\n      on human difficulty scores per Civelli et al.), project out difficulty direction\n      from activations, retrain correctness probes on residuals, evaluate transfer.\n      10 representative languages × 8 representative layers per model (20-90% depth).\n    priority: P0\n    gpu_budget_hours: 15\n    deps: [plan_001, plan_002]\n    notes: \"Need IRT difficulty scores from GlobalMMLU or external source.\"\n\n  # === P1: Important for strong submission ===\n\n  - id: plan_005\n    claim: 4\n    description: >\n      Cross-lingual orthogonality analysis: extract verbalized confidence direction\n      (prompt model for confidence score, fit probe), compute cosine similarity\n      with correctness direction across 20 languages × 2 architectures.\n      Analyze by resource tier (high/mid/low) and language family.\n    priority: P1\n    gpu_budget_hours: 10\n    deps: [plan_001, plan_002]\n\n  - id: plan_006\n    claim: 1\n    description: >\n      Probe complexity comparison: logistic regression vs 2-layer MLP\n      at each probed layer for both models. Compare English accuracy,\n      cross-lingual transfer degradation, and calibration quality.\n      Test hypothesis: linear probes transfer better cross-lingually.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [plan_001, plan_002]\n    notes: \"CPU-bound, uses cached activations.\"\n\n  - id: plan_007\n    claim: 1\n    description: >\n      Additional benchmark evaluation: evaluate best probes + CaCLR\n      on Belebele (20 languages) and MMLU-ProX (20 languages).\n      Validates generalization beyond MMLU/GlobalMMLU.\n    priority: P1\n    gpu_budget_hours: 30\n    deps: [plan_001, plan_002, plan_003]\n\n  - id: plan_010\n    claim: 1\n    description: >\n      INT8 validation ablation: compare INT8 vs FP16 probing results\n      at 5 representative layers for Llama 4 Scout on 5% random subset.\n      Validates that INT8 quantization doesn't distort correctness signals.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [plan_002]\n\n  # === P2: Camera-ready extension ===\n\n  - id: plan_008\n    claim: 1\n    description: >\n      Gemma 4 31B Dense (60 layers, dense, FP16): third architecture\n      for camera-ready. Full Pareto frontier, 20+ languages.\n      Provides dense vs MoE architectural contrast.\n    priority: P2\n    gpu_budget_hours: 30\n    deps: []\n\n  - id: plan_009\n    claim: 1\n    description: >\n      Extended language coverage: expand from 20 to 50+ languages\n      for camera-ready. Leverages GlobalMMLU/Belebele full language sets.\n    priority: P2\n    gpu_budget_hours: 50\n    deps: [plan_001, plan_002]\n\n  # === MVP experiments (completed/running) ===\n\n  - id: mvp_validation\n    claim: 1\n    description: \"MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift\"\n    priority: P0\n    registry_id: mvp_001\n    gpu_budget_hours: 2\n    deps: []\n\n  - id: mvp_complementary\n    claim: 1\n    description: \"MVP robustness: complementary layer set (2,6,10,14,18,22,26)\"\n    priority: P1\n    registry_id: mvp_002\n    gpu_budget_hours: 2\n    deps: [mvp_validation]\n\n  - id: mvp_llama_control\n    claim: 1\n    description: \"MVP cross-architecture: Llama-3.1-8B control experiment\"\n    priority: P1\n    registry_id: mvp_003\n    gpu_budget_hours: 3\n    deps: [mvp_validation]\n",
      "numLines": 145,
      "startLine": 1,
      "totalLines": 145
    }
  },
  "sourceToolAssistantUUID": "b75ddb8e-8581-4d86-a834-a28ae500cd3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T19:05:56.972Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PDotp9RoqX8h2QNvogzy5R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c43efa4-6d5c-441a-8818-16f6a2658d50",
  "isSidechain": false,
  "requestId": "req_011CbELsMYfVv31kDJvdGBmV",
  "type": "assistant",
  "uuid": "491a3d9b-99a3-496d-804a-46b08045b292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012cgbVJvr2VY8auxxjfoJHt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13292,
      "cache_read_input_tokens": 22772,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 22772,
          "cache_creation_input_tokens": 13292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13292
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

_source line 19 · 2026-05-20T19:05:57.108Z_

<details><summary>↩ Tool result · `toolu_01YRSeC6aVTfZMY4PTJc1DAt`</summary>

```text
1	_next_id: 5
2	decisions:
3	- id: D001
4	  date: 2026-05-20 13:49 UTC
5	  summary: MVP 用 7-8B 模型验证核心假设，不直接上 235B
6	  rationale: 核心假设（correctness probe 跨语言迁移 + layer-depth 效应）在 7-8B 模型上有充分先验（Miao &
7	    Ungar、Civelli 等均用 7-8B）。若 7B 无效应则整个方向不成立。7B 仅需 1 GPU × 2-4h，快速验证后再决定是否投入 235B
8	    的大资源。
9	  related_experiments: []
10	  depends_on: []
11	- id: D002
12	  date: 2026-05-20 13:53 UTC
13	  summary: MVP 模型固定为 Qwen2.5-7B-Instruct
14	  rationale: 与正式实验 Qwen3-235B 同属 Qwen 家族，架构连续性最好。Civelli et al. 报告 Qwen3-8B 最优迁移深度为
15	    24%，可为正式实验提供直接参考。Reviewer 建议明确选一个并记录理由。
16	  related_experiments: []
17	  depends_on: []
18	- id: D003
19	  date: 2026-05-20 18:25 UTC
20	  summary: P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/5 语言
21	  rationale: Mean-shift 是常数偏移，不改变 AUROC（rank-invariant）。Mean-shift 的设计目的是改善 calibration（概率准确性），应用
22	    ECE/Brier 衡量。同时 P1 ECE 阈值维持 0.15 但允许 temperature scaling 后重测。
23	  related_experiments:
24	  - exp_id: mvp_001
25	    role: trigger
26	    result: P4 ΔAUROC=0 暴露标准设计缺陷
27	  depends_on: []
28	- id: D004
29	  date: 2026-05-20 18:52 UTC
30	  summary: 'MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段'
31	  rationale: P1(AUROC=0.754+ECE=0.074 temp-scaled) / P2(4/5语言迁移) / P3(14.3pp depth
32	    effect) 全部 PASS。P4(mean-shift) FAIL 但属于 alignment baseline 方法失败，不否定核心假设。Mean-shift
33	    失败是有价值的 negative result：(1) 区分于 Xiao et al. 在 knowledge boundary 上 mean-shift
34	    成功；(2) motivate CaCLR 方法。额外发现：L27 英语最强但迁移退化 vs L24——直接观测到 Pareto tradeoff，是论文核心贡献的前兆。
35	  related_experiments:
36	  - exp_id: mvp_001
37	    role: primary
38	    result: P1✅P2✅P3✅P4❌, core hypothesis supported
39	  depends_on: []
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d06f7608-642e-4ecc-a28b-c8805cdb7f7c",
  "isSidechain": false,
  "promptId": "961d2670-53c4-4e07-b82c-db2a80244bf8",
  "type": "user",
  "uuid": "89608359-d471-4b0c-89c4-09c5fb38cb37",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/decisions.yaml",
      "content": "_next_id: 5\ndecisions:\n- id: D001\n  date: 2026-05-20 13:49 UTC\n  summary: MVP 用 7-8B 模型验证核心假设，不直接上 235B\n  rationale: 核心假设（correctness probe 跨语言迁移 + layer-depth 效应）在 7-8B 模型上有充分先验（Miao &\n    Ungar、Civelli 等均用 7-8B）。若 7B 无效应则整个方向不成立。7B 仅需 1 GPU × 2-4h，快速验证后再决定是否投入 235B\n    的大资源。\n  related_experiments: []\n  depends_on: []\n- id: D002\n  date: 2026-05-20 13:53 UTC\n  summary: MVP 模型固定为 Qwen2.5-7B-Instruct\n  rationale: 与正式实验 Qwen3-235B 同属 Qwen 家族，架构连续性最好。Civelli et al. 报告 Qwen3-8B 最优迁移深度为\n    24%，可为正式实验提供直接参考。Reviewer 建议明确选一个并记录理由。\n  related_experiments: []\n  depends_on: []\n- id: D003\n  date: 2026-05-20 18:25 UTC\n  summary: P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/5 语言\n  rationale: Mean-shift 是常数偏移，不改变 AUROC（rank-invariant）。Mean-shift 的设计目的是改善 calibration（概率准确性），应用\n    ECE/Brier 衡量。同时 P1 ECE 阈值维持 0.15 但允许 temperature scaling 后重测。\n  related_experiments:\n  - exp_id: mvp_001\n    role: trigger\n    result: P4 ΔAUROC=0 暴露标准设计缺陷\n  depends_on: []\n- id: D004\n  date: 2026-05-20 18:52 UTC\n  summary: 'MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段'\n  rationale: P1(AUROC=0.754+ECE=0.074 temp-scaled) / P2(4/5语言迁移) / P3(14.3pp depth\n    effect) 全部 PASS。P4(mean-shift) FAIL 但属于 alignment baseline 方法失败，不否定核心假设。Mean-shift\n    失败是有价值的 negative result：(1) 区分于 Xiao et al. 在 knowledge boundary 上 mean-shift\n    成功；(2) motivate CaCLR 方法。额外发现：L27 英语最强但迁移退化 vs L24——直接观测到 Pareto tradeoff，是论文核心贡献的前兆。\n  related_experiments:\n  - exp_id: mvp_001\n    role: primary\n    result: P1✅P2✅P3✅P4❌, core hypothesis supported\n  depends_on: []\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  },
  "sourceToolAssistantUUID": "d06f7608-642e-4ecc-a28b-c8805cdb7f7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T19:05:56.980Z_

<details><summary>↩ Tool result · `toolu_01PDotp9RoqX8h2QNvogzy5R`</summary>

```text
1	baseline: null
2	experiments:
3	  mvp_001:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-20T14:17:02.273Z'
7	    updated_at: '2026-05-20T18:53:43.847Z'
8	    hypothesis: 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性
9	      probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在
10	      layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp
11	      for ≥3/5 语言）。
12	    spec:
13	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
14	        base && cd /root/xling_calib_direction && bash run_mvp.sh"
15	      server: westd-13176
16	      gpu:
17	      - cuda:0
18	      pid: '9845'
19	      log_path: ~/runs/xling_calib_direction/mvp_001.log
20	      submitted_at: '2026-05-20T16:29:25.456Z'
21	      submitted_via: submit_training_job
22	      backend: tmux
23	      account: root
24	      wall_clock_seconds: 6824.1
25	      gpu_hours: 1.9
26	    conclusion: success
27	    metrics:
28	      en_best_auroc: 0.7541
29	      en_best_layer: 27
30	      en_best_ece_raw: 0.1951
31	      en_best_ece_tempcal: 0.0744
32	      temp_scaling_T: 6.21
33	      en_auroc_range:
34	      - 0.6113
35	      - 0.7541
36	      layer_depth_delta: 0.1428
37	      layers_tested:
38	      - 0
39	      - 4
40	      - 8
41	      - 12
42	      - 16
43	      - 20
44	      - 24
45	      - 27
46	      zs_pass_langs:
47	      - zh
48	      - ar
49	      - hi
50	      - ko
51	      zs_fail_langs:
52	      - sw
53	      best_zs_auroc:
54	        zh: 0.686
55	        ar: 0.651
56	        hi: 0.652
57	        ko: 0.648
58	        sw: 0.56
59	      mean_shift_delta_ece:
60	        zh: -0.36
61	        ar: -0.06
62	        hi: 2.22
63	        sw: 6.44
64	        ko: 0.01
65	      pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)
66	      p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)
67	      p2: PASS (4/5)
68	      p3: PASS (14.28pp)
69	      p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as
70	        naive baseline negative result)
71	    checkpoint_path: /root/xling_calib_direction/probes/
72	    log_path: /root/xling_calib_direction/results/summary.txt
73	    completed_at: '2026-05-20T18:23:09.593Z'
74	  mvp_002:
75	    status: DONE
76	    retry_count: 0
77	    created_at: '2026-05-20T16:26:27.143Z'
78	    updated_at: '2026-05-20T18:55:50.483Z'
79	    hypothesis: Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与
80	      mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际
81	      28 层，index 0-27）
82	    parent: mvp_001
83	    spec:
84	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
85	        base && cd /root/xling_calib_direction && bash run_mvp_002.sh"
86	      server: westd-13176
87	      gpu:
88	      - cuda:1
89	      pid: '11397'
90	      log_path: ~/runs/xling_calib_direction/mvp_002.log
91	      submitted_at: '2026-05-20T17:01:16.028Z'
92	      submitted_via: submit_training_job
93	      backend: tmux
94	      account: root
95	      wall_clock_seconds: 6874.5
96	      gpu_hours: 1.91
97	    conclusion: failed
98	    metrics:
99	      bug: layer_config_mismatch
100	      detail: extract_activations.py used --layers 2,6,10,14,18,22,26 but train_probe.py
101	        and transfer_eval.py used default layers 0,4,8,12,16,20,24,28,31. Probe training
102	        skipped all layers (activation files not found). Activations (42 files) are
103	        valid and reusable.
104	      fix: Add --layers 2,6,10,14,18,22,26 to train_probe.py and transfer_eval.py
105	        in run_mvp_002.sh
106	    log_path: /root/runs/xling_calib_direction/mvp_002.log
107	    checkpoint_path: /root/xling_calib_direction/activations_mvp002/
108	    completed_at: '2026-05-20T18:55:50.484Z'
109	  mvp_003:
110	    status: RUNNING
111	    retry_count: 0
112	    created_at: '2026-05-20T18:27:06.449Z'
113	    updated_at: '2026-05-20T18:48:08.053Z'
114	    hypothesis: 'Cross-lingual correctness direction is model-agnostic: an English-trained
115	      linear probe on Llama-3.1-8B-Instruct internal representations will transfer
116	      to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the
117	      pattern observed in Qwen2.5-7B-Instruct (mvp_001).'
118	    parent: mvp_001
119	    spec:
120	      command: CUDA_VISIBLE_DEVICES=2 bash /root/xling_calib_direction/run_mvp_003.sh
121	      server: westd-13176
122	      data_path: cais/mmlu + CohereForAI/Global-MMLU
123	      data_count: ~14K test samples per language
124	      model_name: LLM-Research/Meta-Llama-3.1-8B-Instruct (ModelScope)
125	      seed: 42
126	      gpu: cuda:2
127	      tmux_session: mvp_003
128	      log_path: /root/xling_calib_direction/mvp_003.log
129	      checkpoint_source: LLM-Research/Meta-Llama-3.1-8B-Instruct
130	      eval_data: cais/mmlu + CohereForAI/Global-MMLU
131	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "491a3d9b-99a3-496d-804a-46b08045b292",
  "isSidechain": false,
  "promptId": "961d2670-53c4-4e07-b82c-db2a80244bf8",
  "type": "user",
  "uuid": "285cb299-9cad-4442-b672-1677d246262d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/registry.yaml",
      "content": "baseline: null\nexperiments:\n  mvp_001:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-20T14:17:02.273Z'\n    updated_at: '2026-05-20T18:53:43.847Z'\n    hypothesis: 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性\n      probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在\n      layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp\n      for ≥3/5 语言）。\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && cd /root/xling_calib_direction && bash run_mvp.sh\"\n      server: westd-13176\n      gpu:\n      - cuda:0\n      pid: '9845'\n      log_path: ~/runs/xling_calib_direction/mvp_001.log\n      submitted_at: '2026-05-20T16:29:25.456Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n      wall_clock_seconds: 6824.1\n      gpu_hours: 1.9\n    conclusion: success\n    metrics:\n      en_best_auroc: 0.7541\n      en_best_layer: 27\n      en_best_ece_raw: 0.1951\n      en_best_ece_tempcal: 0.0744\n      temp_scaling_T: 6.21\n      en_auroc_range:\n      - 0.6113\n      - 0.7541\n      layer_depth_delta: 0.1428\n      layers_tested:\n      - 0\n      - 4\n      - 8\n      - 12\n      - 16\n      - 20\n      - 24\n      - 27\n      zs_pass_langs:\n      - zh\n      - ar\n      - hi\n      - ko\n      zs_fail_langs:\n      - sw\n      best_zs_auroc:\n        zh: 0.686\n        ar: 0.651\n        hi: 0.652\n        ko: 0.648\n        sw: 0.56\n      mean_shift_delta_ece:\n        zh: -0.36\n        ar: -0.06\n        hi: 2.22\n        sw: 6.44\n        ko: 0.01\n      pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n      p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n      p2: PASS (4/5)\n      p3: PASS (14.28pp)\n      p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n        naive baseline negative result)\n    checkpoint_path: /root/xling_calib_direction/probes/\n    log_path: /root/xling_calib_direction/results/summary.txt\n    completed_at: '2026-05-20T18:23:09.593Z'\n  mvp_002:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-20T16:26:27.143Z'\n    updated_at: '2026-05-20T18:55:50.483Z'\n    hypothesis: Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与\n      mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际\n      28 层，index 0-27）\n    parent: mvp_001\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && cd /root/xling_calib_direction && bash run_mvp_002.sh\"\n      server: westd-13176\n      gpu:\n      - cuda:1\n      pid: '11397'\n      log_path: ~/runs/xling_calib_direction/mvp_002.log\n      submitted_at: '2026-05-20T17:01:16.028Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n      wall_clock_seconds: 6874.5\n      gpu_hours: 1.91\n    conclusion: failed\n    metrics:\n      bug: layer_config_mismatch\n      detail: extract_activations.py used --layers 2,6,10,14,18,22,26 but train_probe.py\n        and transfer_eval.py used default layers 0,4,8,12,16,20,24,28,31. Probe training\n        skipped all layers (activation files not found). Activations (42 files) are\n        valid and reusable.\n      fix: Add --layers 2,6,10,14,18,22,26 to train_probe.py and transfer_eval.py\n        in run_mvp_002.sh\n    log_path: /root/runs/xling_calib_direction/mvp_002.log\n    checkpoint_path: /root/xling_calib_direction/activations_mvp002/\n    completed_at: '2026-05-20T18:55:50.484Z'\n  mvp_003:\n    status: RUNNING\n    retry_count: 0\n    created_at: '2026-05-20T18:27:06.449Z'\n    updated_at: '2026-05-20T18:48:08.053Z'\n    hypothesis: 'Cross-lingual correctness direction is model-agnostic: an English-trained\n      linear probe on Llama-3.1-8B-Instruct internal representations will transfer\n      to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the\n      pattern observed in Qwen2.5-7B-Instruct (mvp_001).'\n    parent: mvp_001\n    spec:\n      command: CUDA_VISIBLE_DEVICES=2 bash /root/xling_calib_direction/run_mvp_003.sh\n      server: westd-13176\n      data_path: cais/mmlu + CohereForAI/Global-MMLU\n      data_count: ~14K test samples per language\n      model_name: LLM-Research/Meta-Llama-3.1-8B-Instruct (ModelScope)\n      seed: 42\n      gpu: cuda:2\n      tmux_session: mvp_003\n      log_path: /root/xling_calib_direction/mvp_003.log\n      checkpoint_source: LLM-Research/Meta-Llama-3.1-8B-Instruct\n      eval_data: cais/mmlu + CohereForAI/Global-MMLU\n",
      "numLines": 131,
      "startLine": 1,
      "totalLines": 131
    }
  },
  "sourceToolAssistantUUID": "491a3d9b-99a3-496d-804a-46b08045b292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T19:05:57.099Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YRSeC6aVTfZMY4PTJc1DAt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "285cb299-9cad-4442-b672-1677d246262d",
  "isSidechain": false,
  "requestId": "req_011CbELsMYfVv31kDJvdGBmV",
  "type": "assistant",
  "uuid": "d06f7608-642e-4ecc-a28b-c8805cdb7f7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012cgbVJvr2VY8auxxjfoJHt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13292,
      "cache_read_input_tokens": 22772,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 22772,
          "cache_creation_input_tokens": 13292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13292
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

_source line 22 · 2026-05-20T19:05:57.234Z_

````json
{
  "parentUuid": "89608359-d471-4b0c-89c4-09c5fb38cb37",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**xling_calib_direction**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"xling_calib_direction\")` 或 `load_project_config(\"xling_calib_direction\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n- **xling-calib-direction-research** — Research patterns from 12 papers on cross-lingual calibration and internal representations in LLMs  →  `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-research.skill.md`\n- **xling-calib-direction-writing** — Writing and visual presentation patterns from 8 papers on cross-lingual calibration and representations  →  `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-writing.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/xling_calib_direction/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "f1bab6a2-a050-4049-9839-28053d9aea83",
  "timestamp": "2026-05-20T19:05:57.234Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Claims 1 and 4 fully hold. Claim 2 partially holds (decomposition works but is noisy). Claim 3 is mixed — CaCLR helps but only marginally beats linear pr…",
  "leafUuid": "f1bab6a2-a050-4049-9839-28053d9aea83",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Multilingual correctness probe transfer pareto frontier",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d"
}
```

---

### Assistant

_source line 25 · 2026-05-20T19:06:01.435Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the project. Let me also check the dream_registry.yaml and the paper_framing.md for any additional context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1bab6a2-a050-4049-9839-28053d9aea83",
  "isSidechain": false,
  "requestId": "req_011CbELspsUCLEZoBo4zSca3",
  "type": "assistant",
  "uuid": "ef0733bb-3c92-4e24-a875-5a52a2121212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YMgvhAyT8Djoxmds2S3s2J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10605,
      "cache_read_input_tokens": 36064,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10605,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 36064,
          "cache_creation_input_tokens": 10605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10605
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

_source line 26 · 2026-05-20T19:06:01.680Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U2FaxKN63WSzdhixU7Zpwc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/dream_registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef0733bb-3c92-4e24-a875-5a52a2121212",
  "isSidechain": false,
  "requestId": "req_011CbELspsUCLEZoBo4zSca3",
  "type": "assistant",
  "uuid": "cb0cf694-c324-465b-a507-41e7e6786a50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YMgvhAyT8Djoxmds2S3s2J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10605,
      "cache_read_input_tokens": 36064,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10605,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 36064,
          "cache_creation_input_tokens": 10605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10605
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

_source line 27 · 2026-05-20T19:06:01.684Z_

<details><summary>↩ Tool result · `toolu_01U2FaxKN63WSzdhixU7Zpwc`</summary>

```text
1	dreams:
2	  dream_20260520T185641:
3	    dream_id: dream_20260520T185641
4	    project: xling_calib_direction
5	    status: imagining
6	    review_mode: full
7	    review_visible: true
8	    writing_visible: true
9	    venue: ''
10	    focus: 'Core submission for EACL 2027 ARR: 2 models (Qwen3-235B + Llama 4 Scout)
11	      × 20 languages. Key risks: (1) CaCLR may not outperform simple linear projection;
12	      (2) difficulty-shared vs capability-specific decomposition may not cleanly separate;
13	      (3) orthogonality claim 4 may be seen as incremental. MVP showed mean-shift
14	      completely fails, Pareto tradeoff directly observed at L24 vs L27.'
15	    what_if: []
16	    pid: 125082
17	    chat_id: oc_74ae31a7dc5ae9d419ba9a89bccc89c0
18	    card_message_id: om_x100b6fd47051f4a0b265b3fe5d1a636
19	    started_at: '2026-05-20T18:56:41+00:00'
20	    updated_at: '2026-05-20T18:56:45+00:00'
21	    stages_completed: []
22	    error: null
23	    context_hash: abe53e536c904420db4b681d2d0235b9002bdc7eb51dd196e066bb0ebb988b82
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb0cf694-c324-465b-a507-41e7e6786a50",
  "isSidechain": false,
  "promptId": "961d2670-53c4-4e07-b82c-db2a80244bf8",
  "type": "user",
  "uuid": "e4e5f7ca-642d-47e1-9c57-58a54b4d86a7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/dream_registry.yaml",
      "content": "dreams:\n  dream_20260520T185641:\n    dream_id: dream_20260520T185641\n    project: xling_calib_direction\n    status: imagining\n    review_mode: full\n    review_visible: true\n    writing_visible: true\n    venue: ''\n    focus: 'Core submission for EACL 2027 ARR: 2 models (Qwen3-235B + Llama 4 Scout)\n      × 20 languages. Key risks: (1) CaCLR may not outperform simple linear projection;\n      (2) difficulty-shared vs capability-specific decomposition may not cleanly separate;\n      (3) orthogonality claim 4 may be seen as incremental. MVP showed mean-shift\n      completely fails, Pareto tradeoff directly observed at L24 vs L27.'\n    what_if: []\n    pid: 125082\n    chat_id: oc_74ae31a7dc5ae9d419ba9a89bccc89c0\n    card_message_id: om_x100b6fd47051f4a0b265b3fe5d1a636\n    started_at: '2026-05-20T18:56:41+00:00'\n    updated_at: '2026-05-20T18:56:45+00:00'\n    stages_completed: []\n    error: null\n    context_hash: abe53e536c904420db4b681d2d0235b9002bdc7eb51dd196e066bb0ebb988b82\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  },
  "sourceToolAssistantUUID": "cb0cf694-c324-465b-a507-41e7e6786a50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-20T19:11:45.629Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me generate the detailed imagined experimental data for each planned experiment under the median tier.

Let me structure this carefully. I need to define:
- 20 languages with resource tiers
- Per-experiment detailed predictions
- Tables with specific numbers
- Rationales grounded in the median tier assumptions

Language list (consistent with MVP which used en, zh, ar, hi, sw, ko):
High-resource (6 non-en): zh, de, fr, es, ja, ru
Mid-resource (8): ar, hi, ko, pt, vi, th, tr, pl


Low-resource (5): sw, te, my, am, yo

Now I'm anchoring my predictions to the median tier constraints. For English performance, I'll use 0.812 for Qwen3 and 0.793 for Llama4. The zero-shot transfer performance across 19 languages should average around 0.685 for Qwen3 and 0.672 for Llama4, with a performance drop of roughly 13 percentage points for Qwen3 and 12 for Llama4 compared to English.

Looking at the remaining metrics: the CACLR advantage over linear projection should be about 1.4 percentage points, ECE reduction from calibration around 21%, and the Pareto depth correlation at 0.71 for Qwen3 versus 0.56 for Llama4. Decomposition difficulty explains roughly 37% of variance, orthogonality averages near 0.08, and I'm expecting the low-resource zero-shot pass rate to hit about 60% across those five languages.

Finishing up the metrics—CACLR improvement on the pass rate should reach around 74%, and the Pareto frontier agreement across architectures looks to be hovering near 0.67.

Now I'm thinking through what pareto_depth_transfer_rank_corr actually represents. It's probably measuring the Spearman rank correlation between layer depth and transfer quality, though the positive range [0.5, 0.78] suggests deeper layers aren't necessarily worse. Or maybe it's tracking how consistently the Pareto frontier ranks across different languages—comparing the ordering of layers by transfer AUROC between language pairs using Kendall's tau or similar.

That second interpretation makes more sense: it's really about whether all languages agree on which layers transfer best. A value around 0.65 means moderate consistency—most languages align on the good transfer layers, but there's noise especially in low-resource settings. Qwen3 shows clearer patterns at 0.71 while Llama4 is messier at 0.56.

This framing works. Now I'm ready to write out the full YAML with all the layer-level details for both models.

Writing YAML output... Now I'm looking at the zero-shot transfer performance across 19 languages by layer, and there's a notable pattern—the AUROC peaks around layer 76 at 0.644, then drops off significantly in the deeper layers, which is quite different from the English-only performance that continues improving through layer 76. So I need to decide how to interpret the metrics—whether to measure at the best English layer or the best transfer layer. Using the best-English-layer interpretation gives me the 16.8pp drop for Qwen3, and if I take the optimal transfer performance across both models (L40 for Qwen3 at 0.719 and around 0.691 for Llama4), the average comes to roughly 0.705, which fits within the target range.

Rather than getting caught up in the exact interpretation, I should just assign consistent numbers for each experiment that align with the ranges I've defined. For Llama 4 Scout with its 48 layers, I'm mapping out the English AUROC progression across the probed layers to establish a baseline before looking at cross-lingual transfer. Looking at the per-language performance, the high-resource languages cluster around 0.754 mean accuracy at the best-transfer layer, while mid-resource languages start lower at 0.718 for Arabic and Hindi.

Let me verify the overall mean calculation across all language groups—I'm getting 0.696 when I sum the weighted averages, but that doesn't match the stated 0.719 mean, so I need to recheck my arithmetic on the individual language scores. I'm going to restructure this to keep things cleaner—I'll separate the layer profiles for English from the per-language breakdowns at key layers, rather than trying to force every number into perfect alignment. For the best English layer, I'm looking at the high-resource language means around 0.703 and mid-resource languages averaging 0.657.

Now I'm calculating the overall cross-language average at that layer, which comes out to about 0.643, giving me a drop from English of roughly 17 percentage points—that fits within the expected range. Looking at the low-resource languages, none of them actually reach the 0.60 AUROC threshold at this layer, so they all fail that particular benchmark.

But wait, I need to reconsider—the pass rate metric is supposed to measure across the full experiment, not just at the worst point. At the best transfer layer, I'm seeing 2 out of 5 languages pass the threshold, which gives me a 0.4 pass rate. That's right at the lower bound of my target range of 0.4 to 0.7. Let me see if I can nudge one more language over the line by adjusting the values slightly—if I can get one more to pass, that brings me to 3 out of 5, or 0.6, which sits more comfortably in the middle of my target range. I'll update those per-language scores at this layer.

Now I'm reconsidering how to define the pass rate itself. Rather than measuring at a single layer, it makes more sense to check whether each low-resource language can achieve the 0.60 threshold at *any* layer. So I'm going through each language and finding its best zero-shot performance across all layers—if that best performance hits 0.60 or above, it passes. Looking at the numbers, that gives me three languages clearing the bar and two falling just short.

For Llama 4 Scout, the best-layer performance is notably weaker across the board, with only two languages reaching the threshold. Combining both models, I'm getting a 50% pass rate overall, which sits comfortably within the expected range. Now I need to evaluate how CaCLR should perform—it ought to outperform the linear projection baseline, so let me work through the five transfer conditions.

Looking at the results across 19 languages at Qwen3's optimal layer, I'm seeing that mean-shift actually hurts performance slightly compared to zero-shot, which aligns with what we saw before. Linear projection gets us to 0.724, few-shot with 25 examples reaches 0.708, and with 100 examples climbs to 0.741. CaCLR lands at 0.738, which is close to the few-shot 100 result but falls just short of the linear projection baseline—that's unexpected since CaCLR should be pulling ahead by a small margin.

Let me recalibrate those numbers: if linear projection is actually 0.722 and CaCLR is 0.736, that gives us the +1.4 percentage point improvement we'd expect. The real test though is whether CaCLR maintains this advantage across the entire layer spectrum, especially at deeper layers where zero-shot performance typically degrades. At Qwen3's layer 76, zero-shot drops to 0.643, but CaCLR holds at 0.691 compared to linear projection's 0.676—that's a +1.5 percentage point gain, which suggests CaCLR is genuinely shifting the Pareto frontier rather than just winning at one particular layer.

The pattern becomes clearer when I look at the cross-lingual results: CaCLR improves over zero-shot in about 14 out of 19 languages, which is solidly in the expected range. The languages that don't improve are mostly low-resource ones like Amharic and Yoruba, plus a few mid-resource languages where the consistency regularization seems to introduce more noise than signal. On the calibration side, I'm comparing CaCLR's expected calibration error against temperature scaling to see if the method provides genuine uncertainty improvements beyond just better accuracy.

For the non-English languages specifically, temperature scaling gets the ECE down to 0.142, while CaCLR achieves 0.112—that's about a 21% reduction, which fits nicely within the expected bounds. Now I'm moving into the decomposition analysis to understand how much of the cross-lingual transfer gap is actually explained by task difficulty versus other factors like language-specific capabilities or confounding variables. The difficulty variance accounts for roughly 37% of the gap, which means projecting it out reduces the transfer gap from about 13 percentage points down to 8.2 percentage points, leaving a substantial portion that's driven by other mechanisms.

Looking at the orthogonality checks across all 20 languages, the cosine similarity between correctness and verbalized confidence is quite low at 0.08 on average—confirming they're nearly independent. The pattern shifts by resource tier though: high-resource languages cluster tightly around 0.06, while low-resource languages show much higher variance at 0.13, which validates the assumption that median-tier languages behave differently. For the probe complexity comparison, the logistic regression model underperforms the MLP slightly on English (0.812 versus 0.827 AUROC), but it generalizes better across languages.

The linear probe approach holds up across additional benchmarks—Belebele shows a similar Pareto pattern with slightly higher scores since reading comprehension is more straightforward, while MMLU-ProX dips lower due to harder questions, and the qualitative patterns remain consistent. INT8 quantization introduces negligible differences compared to FP16, staying under 0.5 percentage points across all layers with no systematic bias, so it's safe for the main experiments. Gemma's dense architecture produces a different Pareto curve than the MoE models—the English AUROC rises more monotonically and transfer degradation is smoother without the routing discontinuities, reaching around 0.805 at best.

Expanding to 50+ languages reveals that many fall below the 0.60 threshold in low-resource settings, making the Pareto frontier noisier as language scarcity increases. Now I'm ready to structure the YAML with comprehensive tables—I'll include per-layer English AUROC breakdowns for the main plans, per-language transfer results at key layers, method comparisons, decomposition analysis, and orthogonality metrics. For the figures, I'm planning Pareto frontier scatter plots showing English AUROC against zero-shot transfer performance, along with visualizations for the other key findings.

Writing YAML with per-language zero-shot AUROC values... Now I'm adding the remaining mid-resource languages and recalculating the mean across all nineteen languages, which drops to 0.644—a significant 16.8 percentage point decline from the best English result. Moving on to evaluate Llama 4 Scout at layer 32. Now I'm calculating the mean transfer performance at the L44 checkpoint across all language groups, summing up the scores and dividing by the total number of languages to get an average of around 0.668.

The performance drop from the best English result is about 13.65 percentage points, which falls within the expected range and aligns with the pattern I'm seeing—Qwen3 shows a steeper drop at 16.8pp while Llama4 is flatter at 13.7pp, which makes sense given their architectural differences.

Moving on to examine the CaCLR results next. Generating comparison tables... CaCLR shows a 1.4 percentage point improvement over linear projection at layer 44, with hyperparameters tuned on held-out English and five validation languages. Looking at the best-performing layer for CaCLR, I'm checking how many of the 19 languages actually benefit from it—14 languages show AUROC improvements while 5 don't, giving a 74% pass rate across the multilingual evaluation. about right, with failures in low-resource languages. So I'm setting the improvement rate at 14 out of 19 languages where CaCLR's AUROC exceeds zero-shot at the best English layer—failures being Amharic, Yoruba, Thai, and Burmese, which are either too low-resource or have script/noise issues. For ECE reduction, CaCLR achieves 19.4% improvement over temperature scaling, which fits within the expected range. Now I need to clarify whether temperature scaling uses per-language calibration or a single English-derived temperature.

Temperature scaling is calibrated on English validation data and applied uniformly across all languages, giving an English temperature of 5.8 that brings non-English ECE down to 0.139. CaCLR improves this further to 0.112. For the difficulty-controlled ablation, I'm training IRT difficulty probes, projecting out that direction, and retraining correctness probes on what remains. The difficulty probes transfer well cross-lingually as expected, and after removing the difficulty signal, English AUROC drops modestly from 0.812 to 0.771 while the transfer gap shrinks from 16.8 percentage points to 10.6—meaning difficulty explains about 37% of the gap.

The residual capability-specific component is noisier though, with high variance across languages and clear language-family clustering in Indo-European languages. Variance decomposition shows difficulty accounts for 37% of the shared variance, while the remaining 63% of capability-specific variance splits roughly in half—about 32% shows language-family structure and 31% appears to be noise or language-specific artifacts. I'm now examining 10 representative languages across specific layers in both Qwen3 and Llama4 to trace where these patterns emerge.

Looking at the transfer AUROC results after difficulty projection, I'm seeing meaningful improvements—at Qwen3 L76 the mean AUROC jumped from 0.644 to 0.700, closing about a third of the cross-lingual gap. But I need to reconsider what's actually happening here: when I remove the difficulty component and retrain on the residual, the correctness probe should show lower English performance since some signal got removed, yet better cross-lingual transfer if difficulty is indeed the transferable component and capability is what doesn't transfer.

The experiment validates this decomposition—difficulty probes transfer strongly with mean zero-shot AUROC above 0.72, while the residual correctness probe shows degraded transfer, confirming that difficulty was carrying the transferable signal. However, the separation isn't perfectly clean in the median tier; the residual still contains some transferable signal and the difficulty projection captures some capability information, so the decomposition works but with noise rather than a clean split. signal too
- Variance explained by difficulty: 37% (not majority, hence "partial")

Let me structure this properly:

Original correctness probe at L76:
- English AUROC: 0.812
- ZS transfer mean: 0.644
- Transfer gap: 16.8pp

Difficulty probe at L76:
- English difficulty prediction R²: 0.68
- ZS transfer R²: 0.61 (transfers well)

Residual correctness probe at L76 (after removing difficulty):
- English AUROC: 0.758 (lower, because some correctness signal removed)
- ZS transfer mean: 0.585 (much lower — the remaining signal transfers poorly)
- Transfer gap: 17.3pp (slightly wider, confirming capability component transfers poorly)

The difficulty component accounted for the transferable part:
- Original transfer gap: 16.8pp
- Residual transfer gap: 17.3pp (even worse)
- If difficulty fully explained transfer, residual transfer should be near chance; it's not, so it's partial

So I need to be precise about variance explained: the difficulty direction accounts for 37% of the variance in the correctness direction, meaning 63% of the remaining signal is capability-specific and drives the transfer gap at deeper layers. The decomposition also suggests when simple baselines work—specifically for languages where difficulty alone predicts performance well.

Now I'm looking at orthogonality metrics across models and languages, examining cosine similarity between correctness and confidence directions.

For Qwen3-235B, the pattern shows increasing divergence as resource availability decreases: high-resource languages cluster around 0.05, mid-resource around 0.08, and low-resource languages spike to 0.17 on average. Computing the weighted mean across all twenty languages gives 0.092, which fits the target range. Moving on to check Llama's numbers... So that gives me 0.102 as the overall average for Scout. But looking at the guidance that low-resource languages should have higher cosine similarity, my initial values seem off—I'm getting 0.14-0.22 when they should probably be lower. Let me recalibrate the low-resource scores down to 0.12-0.19 and recalculate the means for both Qwen3 and Llama4 to see if that brings the overall averages more in line.

Now I'm computing the cross-model mean and confirming it falls within the expected range of 0.05-0.20 for low-resource settings. Next I need to look at probe complexity by comparing logistic regression versus MLP performance across key layers in the models.

Comparing performance metrics across layers...

The key insight is that MLPs outperform linear probes on English tasks by 1.5-2.0 percentage points, but this comes at a cost—they lose 2.5-3.7 percentage points on cross-lingual transfer. Linear probes maintain better generalization across languages, which validates the core hypothesis.

Looking at the additional benchmarks, both Belebele and MMLU-ProX show similar patterns: the Pareto frontier replicates across datasets, with English performance slightly varying (0.798 for Belebele versus 0.824 for MMLU-ProX), while zero-shot transfer hovers around 0.68-0.71. CaCLR provides a modest improvement of about 1.1 percentage points over the baseline linear projection approach.

For the INT8 quantization validation across representative layers, the precision loss is minimal and consistent—dropping by just 0.2-0.3 percentage points across all tested layers with no systematic bias toward either direction.

Moving to the Gemma 4 31B dense model, I'm seeing a smoother Pareto frontier compared to the MoE variants, with the best English AUROC of 0.805 at layer 48 and zero-shot transfer peaking at 0.709 at layer 32. The 10.2pp drop between these is smaller than what I observed in MoE models, which makes sense given the more gradual feature evolution in dense architectures. For the extended language evaluation across 50+ languages, the pattern holds but becomes noisier—very low-resource languages like Quechua and Hausa completely fail to transfer with AUROC below 0.55, though the overall frontier shape remains consistent.

Now I have the data I need to construct the full YAML specification. I'm thinking through the narrative framing one more time: the median-tier story should pivot toward discovery and analysis, making the Pareto frontier the headline contribution while repositioning the other claims as supporting evidence. The core message is that cross-lingual calibration probes reveal architecture-dependent boundaries, and CaCLR achieves supervised-level transfer without needing target labels. Before I write this out, I want to make sure I'm capturing the Pareto frontier agreement across architectures—that's a key finding I need to highlight.

I'm measuring this as the correlation of optimal transfer depths across languages between Qwen3 and Llama4, where for each language I identify which layer depth yields the best transfer performance, then correlate those depths across the two models. The data shows this agreement ranges from 0.55 to 0.8 depending on how I calculate it, and I'm seeing consistent patterns where both architectures favor similar layer regions for different languages. I'm noticing the depth percentages are perfectly monotonic across both models—the same language ordering appears in both—which would give a Spearman correlation too close to 1.0 for the target range. I need to introduce some variation to bring it down to the 0.55 to 0.8 range.

Let me just set the correlation value to 0.67 as a summary statistic rather than trying to derive it from individual data points, and move forward with writing the YAML output.

Actually, I'm reconsidering the layer depth analysis. For Llama 4 Scout with 48 layers, the peak at L44 represents 93.6% depth, while for Qwen3-235B with 94 layers, the EN AUROC peaks at L76 which is 81.7% depth. These different relative depths make sense given that the optimal transfer layer varies by architecture.

Looking back at the MVP results, Qwen2.5-7B also peaked near the end at L27/28 (96.4% depth), so this pattern of English probing peaking toward the later layers is consistent across models.

Now I'm ready to write out the comprehensive YAML structure. I'll keep the tables compact by using arrays and focusing on key layers rather than listing every single one. For the English AUROC data, I'll include all 24 layers since that's crucial for the Pareto frontier analysis, but I'll condense the per-resource-tier and per-language zero-shot results to just the most important layers.

For the CaCLR approach, the key innovation is the consistency loss term that encourages similar predictions across parallel activations in different languages. The hyperparameters α and β control the balance between the SB-ECE loss and this cross-lingual consistency signal. This consistency term is particularly effective for mid-resource languages where there's enough data to leverage the signal, though it doesn't help as much with low-resource languages where the activations are too noisy.

Writing YAML output... I need to clarify what temperature scaling is being applied to—if it's calibrating the zero-shot probe output, then the ECE improves from 0.183 to 0.139, and CaCLR achieves 0.112, which represents a 19.4% reduction compared to the temperature-scaled baseline. Let me make sure I'm comparing the right methods consistently.

The key insight is that all methods can have temperature scaling applied post-hoc, so the fairest comparison should pit CaCLR's raw ECE (0.112) against the best temperature-scaled baseline, which might be linear projection rather than zero-shot. I need to check what that baseline ECE actually is before finalizing the reduction metric. Writing YAML config... Generating YAML structure with detailed metrics... Looking at the remaining metrics and they all fall within acceptable ranges. Now I need to format everything as YAML output — the user wants a single block with rationales for each experiment, so I'll structure that and save it as an artifact rather than flooding the conversation.

For plan_004, I'm mapping out the layer sampling strategy across both models: Qwen3's 96 layers get probed at roughly 8 evenly-spaced depths from 20-90%, while Llama4's 48 layers need adjustment to hit similar depth percentages, sampling every 4th layer to keep the probe count manageable. For Llama4 with 48 layers, I need to find the 8 representative layers across the 20-90% depth range. Looking at the nearest probed layers available, I'll go with L8, L12, L20, L24, L28, L32, L40, L44 to get good coverage. Now I'm writing out the final YAML configuration with the key tables and layer profiles.

For the experimental plans, I need to make sure the expected results are clear: plan_006 should show LogReg transfers better than MLP despite MLP's stronger English performance, plan_007 should validate the Pareto patterns generalize to Belebele and MMLU-ProX, plan_010 should confirm INT8 quantization has negligible impact, and I'll project numbers for plan_008 and plan_009 covering Gemma 4 and extended language coverage.

Writing YAML structure... Now I'm structuring the main experimental results carefully, choosing realistic numbers that feel consistent with actual research findings. I'll present layer-by-layer AUROC scores for English and cross-lingual transfer, highlighting the Pareto frontier where CaCLR's key innovation shows—pushing the optimal operating point deeper into the network while maintaining or improving English performance by a couple percentage points compared to zero-shot baselines. I'll also weave in calibration metrics and method comparisons across different difficulty tiers to support the core claims.

Writing the results YAML... Continuing through the remaining plans—Llama4 shows similar performance with a zero-shot transfer of 0.679 and a 13.6 percentage point drop, while CaCLR demonstrates a 1.3 percentage point improvement over linear projection and achieves a 21% ECE reduction. The decomposition and orthogonality metrics are also checking out within expected ranges.

All the validation results are coming together—the probe complexity analysis shows logistic regression transfers better than MLP, the patterns hold across Belebele and MMLU-ProX, INT8 quantization has minimal impact, and the extended language evaluation across 50+ languages shows expected degradation in very low-resource settings. Now I need to document the hyperparameter tuning results for CaCLR, particularly the α and β sweep across the held-out English validation set.

The sweep tested α from 0.1 to 1.0 and β from 0.05 to 0.3, with α=0.30 and β=0.15 emerging as optimal. Lower α values fail to strengthen calibration enough, while higher values let the BCE loss dominate and hurt AUROC. Similarly, β needs to be high enough to meaningfully enforce consistency across languages but not so high that it tanks English performance. The balance at 0.30 and 0.15 handles all three objectives well. Time to write out the complete YAML configuration.

Now I'm thinking through the structure for each experiment entry. Each one needs a name, plan reference, description, expected metrics, rationale for those results, tables with data, figure descriptions, and analysis. I'll keep the tables compact by nesting objects where it makes sense rather than fully expanding everything into lists.

Writing YAML output... Writing the YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4e5f7ca-642d-47e1-9c57-58a54b4d86a7",
  "isSidechain": false,
  "requestId": "req_011CbELtA4PQEQbpETwhLaKb",
  "type": "assistant",
  "uuid": "010a8be7-2cc3-4a95-a2ee-4eb66e799e96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFmWAh8esqYDyQrbFzaDxW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 46669,
      "output_tokens": 40432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 577,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 40432,
          "cache_read_input_tokens": 46669,
          "cache_creation_input_tokens": 577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 577
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

_source line 29 · 2026-05-20T19:17:52.712Z_

```yaml
tier: median
narrative_guidance: >
  Rebalance toward discovery + analysis. Claim 1 (Pareto frontier) becomes the headline contribution —
  first systematic characterization of depth-transferability tradeoff across architectures and 20 languages.
  Claim 2 reframes decomposition as 'partial but prescriptive': difficulty component is clearly transferable,
  capability residual is noisy but the decomposition still predicts when simple baselines suffice vs when
  CaCLR helps. Claim 3 softens: CaCLR is presented as 'matching or exceeding the best simple baseline
  (linear projection) while requiring no target-language data at all' — emphasize the zero-label setting
  rather than raw metric superiority. Add ablation showing where CaCLR's consistency term specifically
  helps (mid-resource languages). Claim 4 presented with resource-tier analysis showing orthogonality
  is robust for well-represented languages but noisier for low-resource.
  Headline: 'Cross-lingual calibration probes reveal architecture-dependent Pareto frontier;
  CaCLR matches supervised transfer without target labels.'

imagined_experiments:

  ##############################################################################
  # plan_001 — Full Pareto Frontier on Qwen3-235B-A22B
  ##############################################################################
  - name: "Full Pareto Frontier — Qwen3-235B-A22B"
    plan_id: plan_001
    description: >
      94-layer MoE model, INT8 quantization. 24 probed layers (every 4th: L0–L92).
      20 languages (7 high / 8 mid / 5 low resource). English logistic-regression
      correctness probes trained per layer, evaluated on 5 transfer conditions
      (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR placeholder).
      Core Pareto frontier data for Claim 1.
    expected_results:
      en_auroc_best: 0.812
      en_best_layer: L76
      en_auroc_range: [0.531, 0.812]
      en_ece_raw_at_best: 0.168
      en_ece_tempcal_at_best: 0.057
      temp_scaling_T: 5.83
      zs_transfer_auroc_mean_19lang_at_best_en: 0.644
      zs_transfer_drop_at_best_en_pp: 16.8
      best_transfer_layer: L40
      zs_transfer_auroc_mean_at_best_transfer: 0.696
      en_auroc_at_best_transfer: 0.776
      pareto_depth_transfer_rank_corr: 0.71
      low_resource_zs_pass_rate: 0.6  # 3/5 pass AUROC≥0.60 at best-per-lang layer
      mean_shift_improvement_rate: 0.05  # 1/19 languages marginally improved
      linproj_auroc_mean_at_best_transfer: 0.724
      fewshot25_auroc_mean_at_best_transfer: 0.711
      fewshot100_auroc_mean_at_best_transfer: 0.743
    result_rationale: >
      Qwen3-235B-A22B 的 94 层深度提供了充分的层级分辨率来观测 Pareto tradeoff。
      深层（L76）英语 AUROC 达 0.812，因为更深层积累了更多 task-specific correctness 信号；
      但这些深层 representation 也更 language-specific（MoE routing 在深层更分化），
      导致 zero-shot 迁移退化至 0.644（drop 16.8pp）。最佳迁移层 L40 处于模型 ~42%
      深度，此处 representation 仍保留足够的 language-agnostic 结构。跨语言层序一致性
      Spearman ρ=0.71 表明各语言对最优迁移深度的偏好高度一致，Pareto 结构是 robust 的。
      Mean-shift 继承 MVP 的失败模式（correctness ≠ knowledge-boundary），仅 1/19
      语言微弱改善。Linear projection 利用无标注目标语激活做线性对齐，在 L40 处比
      zero-shot 高 2.8pp，确立为 CaCLR 需要超越的 strong baseline。
      低资源语言（sw/te/my 通过，am/yo 失败）符合预期：GlobalMMLU 低资源子集样本量小且
      翻译质量不稳定，但 3/5 通过证明 correctness direction 跨语言性在大模型上比 7B 更强。
    tables:
      - title: "English AUROC by Layer (Logistic Regression)"
        columns: [layer, depth_pct, en_auroc, en_ece_raw]
        data:
          - {layer: L0,  depth_pct: 0,   en_auroc: 0.531, en_ece_raw: 0.341}
          - {layer: L4,  depth_pct: 4,   en_auroc: 0.557, en_ece_raw: 0.328}
          - {layer: L8,  depth_pct: 9,   en_auroc: 0.589, en_ece_raw: 0.312}
          - {layer: L12, depth_pct: 13,  en_auroc: 0.621, en_ece_raw: 0.293}
          - {layer: L16, depth_pct: 17,  en_auroc: 0.653, en_ece_raw: 0.274}
          - {layer: L20, depth_pct: 21,  en_auroc: 0.684, en_ece_raw: 0.255}
          - {layer: L24, depth_pct: 26,  en_auroc: 0.711, en_ece_raw: 0.237}
          - {layer: L28, depth_pct: 30,  en_auroc: 0.735, en_ece_raw: 0.221}
          - {layer: L32, depth_pct: 34,  en_auroc: 0.752, en_ece_raw: 0.210}
          - {layer: L36, depth_pct: 38,  en_auroc: 0.766, en_ece_raw: 0.199}
          - {layer: L40, depth_pct: 43,  en_auroc: 0.776, en_ece_raw: 0.192}
          - {layer: L44, depth_pct: 47,  en_auroc: 0.784, en_ece_raw: 0.186}
          - {layer: L48, depth_pct: 51,  en_auroc: 0.790, en_ece_raw: 0.182}
          - {layer: L52, depth_pct: 55,  en_auroc: 0.796, en_ece_raw: 0.178}
          - {layer: L56, depth_pct: 60,  en_auroc: 0.800, en_ece_raw: 0.175}
          - {layer: L60, depth_pct: 64,  en_auroc: 0.804, en_ece_raw: 0.173}
          - {layer: L64, depth_pct: 68,  en_auroc: 0.807, en_ece_raw: 0.171}
          - {layer: L68, depth_pct: 72,  en_auroc: 0.810, en_ece_raw: 0.170}
          - {layer: L72, depth_pct: 77,  en_auroc: 0.811, en_ece_raw: 0.169}
          - {layer: L76, depth_pct: 81,  en_auroc: 0.812, en_ece_raw: 0.168}
          - {layer: L80, depth_pct: 85,  en_auroc: 0.809, en_ece_raw: 0.170}
          - {layer: L84, depth_pct: 89,  en_auroc: 0.804, en_ece_raw: 0.174}
          - {layer: L88, depth_pct: 94,  en_auroc: 0.796, en_ece_raw: 0.179}
          - {layer: L92, depth_pct: 98,  en_auroc: 0.782, en_ece_raw: 0.188}

      - title: "Zero-Shot Transfer AUROC by Resource Tier (key layers)"
        note: "19 non-English languages; tier means ± std"
        columns: [layer, high_6_mean, high_6_std, mid_8_mean, mid_8_std, low_5_mean, low_5_std, all_19_mean]
        data:
          - {layer: L24, high_6_mean: 0.731, high_6_std: 0.011, mid_8_mean: 0.692, mid_8_std: 0.014, low_5_mean: 0.590, low_5_std: 0.031, all_19_mean: 0.679}
          - {layer: L32, high_6_mean: 0.747, high_6_std: 0.010, mid_8_mean: 0.706, mid_8_std: 0.013, low_5_mean: 0.601, low_5_std: 0.029, all_19_mean: 0.691}
          - {layer: L40, high_6_mean: 0.753, high_6_std: 0.010, mid_8_mean: 0.711, mid_8_std: 0.013, low_5_mean: 0.607, low_5_std: 0.032, all_19_mean: 0.696}
          - {layer: L52, high_6_mean: 0.741, high_6_std: 0.011, mid_8_mean: 0.697, mid_8_std: 0.015, low_5_mean: 0.586, low_5_std: 0.035, all_19_mean: 0.682}
          - {layer: L64, high_6_mean: 0.721, high_6_std: 0.013, mid_8_mean: 0.673, mid_8_std: 0.017, low_5_mean: 0.558, low_5_std: 0.039, all_19_mean: 0.661}
          - {layer: L76, high_6_mean: 0.705, high_6_std: 0.010, mid_8_mean: 0.657, mid_8_std: 0.016, low_5_mean: 0.540, low_5_std: 0.033, all_19_mean: 0.644}
          - {layer: L92, high_6_mean: 0.672, high_6_std: 0.015, mid_8_mean: 0.621, mid_8_std: 0.020, low_5_mean: 0.497, low_5_std: 0.042, all_19_mean: 0.607}

      - title: "Per-Language Zero-Shot AUROC at L40 (Best Transfer) and L76 (Best English)"
        columns: [lang, tier, L40_auroc, L76_auroc, delta_pp]
        data:
          - {lang: zh, tier: high, L40_auroc: 0.762, L76_auroc: 0.712, delta_pp: -5.0}
          - {lang: de, tier: high, L40_auroc: 0.753, L76_auroc: 0.703, delta_pp: -5.0}
          - {lang: fr, tier: high, L40_auroc: 0.757, L76_auroc: 0.708, delta_pp: -4.9}
          - {lang: es, tier: high, L40_auroc: 0.764, L76_auroc: 0.715, delta_pp: -4.9}
          - {lang: ja, tier: high, L40_auroc: 0.737, L76_auroc: 0.688, delta_pp: -4.9}
          - {lang: ru, tier: high, L40_auroc: 0.744, L76_auroc: 0.697, delta_pp: -4.7}
          - {lang: ar, tier: mid, L40_auroc: 0.717, L76_auroc: 0.667, delta_pp: -5.0}
          - {lang: hi, tier: mid, L40_auroc: 0.710, L76_auroc: 0.659, delta_pp: -5.1}
          - {lang: ko, tier: mid, L40_auroc: 0.703, L76_auroc: 0.652, delta_pp: -5.1}
          - {lang: pt, tier: mid, L40_auroc: 0.731, L76_auroc: 0.681, delta_pp: -5.0}
          - {lang: vi, tier: mid, L40_auroc: 0.696, L76_auroc: 0.644, delta_pp: -5.2}
          - {lang: th, tier: mid, L40_auroc: 0.688, L76_auroc: 0.633, delta_pp: -5.5}
          - {lang: tr, tier: mid, L40_auroc: 0.706, L76_auroc: 0.655, delta_pp: -5.1}
          - {lang: pl, tier: mid, L40_auroc: 0.723, L76_auroc: 0.673, delta_pp: -5.0}
          - {lang: sw, tier: low, L40_auroc: 0.638, L76_auroc: 0.579, delta_pp: -5.9}
          - {lang: te, tier: low, L40_auroc: 0.644, L76_auroc: 0.590, delta_pp: -5.4}
          - {lang: my, tier: low, L40_auroc: 0.607, L76_auroc: 0.543, delta_pp: -6.4}
          - {lang: am, tier: low, L40_auroc: 0.583, L76_auroc: 0.532, delta_pp: -5.1}
          - {lang: yo, tier: low, L40_auroc: 0.561, L76_auroc: 0.510, delta_pp: -5.1}

    figures_description:
      - >
        Figure 1a: Pareto frontier scatter — x-axis: English AUROC, y-axis: zero-shot
        transfer mean AUROC (19 langs). Each point is one probed layer (L0–L92), color-coded
        by depth percentage. Clear upward-then-left curve: shallow layers cluster at bottom-left
        (both low), mid layers at upper-right of transfer axis (L40 peak), deep layers drift
        right on English axis but downward on transfer. Pareto-efficient frontier connects
        L40→L48→L56→L64→L76. Annotate L40 ("best transfer") and L76 ("best English").
      - >
        Figure 1b: Layer-depth profile — dual y-axis plot. Left axis: English AUROC (blue,
        rising then plateau). Right axis: ZS transfer mean (orange, rising then falling).
        Crossover region around L44–L52 clearly visible. Shaded band shows ±1σ across 19 languages
        on the transfer curve — band widens at deeper layers.
      - >
        Figure 1c: Heatmap — rows: 19 languages (grouped by resource tier), columns: 24 layers.
        Cell color: zero-shot AUROC. Clear gradient: high-resource rows are warm (0.65–0.76)
        across most layers; low-resource rows are cool (0.50–0.64) with the warm zone concentrated
        at mid-depth layers. Visual pattern immediately shows depth-transferability × resource
        interaction.
    analysis: >
      Qwen3-235B exhibits a textbook Pareto frontier for Claim 1. The depth-transferability
      tradeoff is sharp: 36 layers separate the best-EN (L76) and best-transfer (L40) operating
      points, with 16.8pp transfer degradation at L76. The layer ranking consistency ρ=0.71
      means 19 languages broadly agree on which depths transfer best, supporting the claim that
      this is a structural property of the model rather than a language-specific artifact.
      Low-resource languages show the expected fragility: 3/5 pass but am and yo fall below
      the 0.60 AUROC threshold even at the optimal transfer layer. This will be framed as a
      resource-tier modulation of the Pareto frontier rather than a failure of the phenomenon.
      Mean-shift's continued failure (replicating MVP) cleanly motivates CaCLR.

  ##############################################################################
  # plan_002 — Full Pareto Frontier on Llama 4 Scout
  ##############################################################################
  - name: "Full Pareto Frontier — Llama 4 Scout"
    plan_id: plan_002
    description: >
      48-layer MoE model, INT8 quantization. 12 probed layers (every 4th: L0–L44).
      20 languages, 5 transfer conditions. Second architecture for cross-model
      Pareto frontier comparison (Claim 1).
    expected_results:
      en_auroc_best: 0.793
      en_best_layer: L44
      en_auroc_range: [0.538, 0.793]
      en_ece_raw_at_best: 0.178
      en_ece_tempcal_at_best: 0.063
      temp_scaling_T: 5.41
      zs_transfer_auroc_mean_19lang_at_best_en: 0.657
      zs_transfer_drop_at_best_en_pp: 13.6
      best_transfer_layer: L32
      zs_transfer_auroc_mean_at_best_transfer: 0.679
      en_auroc_at_best_transfer: 0.771
      pareto_depth_transfer_rank_corr: 0.56
      low_resource_zs_pass_rate: 0.4  # 2/5
      mean_shift_improvement_rate: 0.05
      linproj_auroc_mean_at_best_transfer: 0.705
      pareto_frontier_agreement_with_qwen3: 0.67
    result_rationale: >
      Llama 4 Scout 仅 48 层（vs Qwen3 的 94 层），Pareto 前沿更 flat/noisy。
      英语 AUROC 峰值 0.793 低于 Qwen3 的 0.812，原因是 Scout 作为 MoE 的 active
      参数量（~17B）小于 Qwen3-A22B，correctness 信号的 linear accessibility 稍弱。
      最佳迁移层 L32（67% 深度）vs 最佳英语层 L44（92% 深度）仅相隔 12 层，前沿
      更紧凑。Transfer drop 13.6pp 低于 Qwen3 的 16.8pp，说明 Llama4 的深层 representation
      language-specificity 增长更平缓——可能与 Llama4 的训练数据分布有关（更多多语言
      数据在预训练中）。跨语言层序一致性 ρ=0.56 明显低于 Qwen3 的 0.71，表明不同
      语言在 Llama4 上对最优迁移层的偏好更分散，Pareto 结构存在但更 noisy。
      与 Qwen3 的 frontier agreement 0.67 说明两个架构共享定性趋势（"中层比深层
      迁移更好"）但定量最优点不同——这正是 "architecture-dependent" claim 的证据。
      低资源仅 2/5 通过，sw 和 te 勉强过线，my/am/yo 失败。
    tables:
      - title: "English AUROC by Layer (Logistic Regression)"
        columns: [layer, depth_pct, en_auroc, en_ece_raw]
        data:
          - {layer: L0,  depth_pct: 0,   en_auroc: 0.538, en_ece_raw: 0.336}
          - {layer: L4,  depth_pct: 8,   en_auroc: 0.571, en_ece_raw: 0.318}
          - {layer: L8,  depth_pct: 17,  en_auroc: 0.613, en_ece_raw: 0.296}
          - {layer: L12, depth_pct: 25,  en_auroc: 0.651, en_ece_raw: 0.272}
          - {layer: L16, depth_pct: 33,  en_auroc: 0.688, en_ece_raw: 0.248}
          - {layer: L20, depth_pct: 42,  en_auroc: 0.718, en_ece_raw: 0.228}
          - {layer: L24, depth_pct: 50,  en_auroc: 0.741, en_ece_raw: 0.212}
          - {layer: L28, depth_pct: 58,  en_auroc: 0.759, en_ece_raw: 0.199}
          - {layer: L32, depth_pct: 67,  en_auroc: 0.771, en_ece_raw: 0.190}
          - {layer: L36, depth_pct: 75,  en_auroc: 0.782, en_ece_raw: 0.183}
          - {layer: L40, depth_pct: 83,  en_auroc: 0.790, en_ece_raw: 0.179}
          - {layer: L44, depth_pct: 92,  en_auroc: 0.793, en_ece_raw: 0.178}

      - title: "Zero-Shot Transfer AUROC by Resource Tier"
        columns: [layer, high_6_mean, mid_8_mean, low_5_mean, all_19_mean]
        data:
          - {layer: L16, high_6_mean: 0.713, mid_8_mean: 0.670, low_5_mean: 0.571, all_19_mean: 0.659}
          - {layer: L24, high_6_mean: 0.731, mid_8_mean: 0.691, low_5_mean: 0.587, all_19_mean: 0.677}
          - {layer: L28, high_6_mean: 0.737, mid_8_mean: 0.697, low_5_mean: 0.591, all_19_mean: 0.683}
          - {layer: L32, high_6_mean: 0.738, mid_8_mean: 0.694, low_5_mean: 0.585, all_19_mean: 0.679}
          - {layer: L36, high_6_mean: 0.733, mid_8_mean: 0.688, low_5_mean: 0.574, all_19_mean: 0.673}
          - {layer: L40, high_6_mean: 0.724, mid_8_mean: 0.678, low_5_mean: 0.561, all_19_mean: 0.663}
          - {layer: L44, high_6_mean: 0.714, mid_8_mean: 0.669, low_5_mean: 0.548, all_19_mean: 0.657}

      - title: "Cross-Architecture Pareto Comparison"
        columns: [metric, qwen3_235b, llama4_scout, interpretation]
        data:
          - {metric: en_auroc_best, qwen3_235b: 0.812, llama4_scout: 0.793, interpretation: "Qwen3 higher, more layers for correctness to accumulate"}
          - {metric: best_transfer_depth_pct, qwen3_235b: 43, llama4_scout: 67, interpretation: "Llama4 optimal transfer much deeper (flatter frontier)"}
          - {metric: zs_drop_at_best_en_pp, qwen3_235b: 16.8, llama4_scout: 13.6, interpretation: "Qwen3 sharper tradeoff, Llama4 flatter"}
          - {metric: layer_rank_consistency, qwen3_235b: 0.71, llama4_scout: 0.56, interpretation: "Qwen3 more consistent across languages"}
          - {metric: frontier_gap_layers, qwen3_235b: 36, llama4_scout: 12, interpretation: "Qwen3 has wider Pareto gap"}
          - {metric: frontier_agreement, qwen3_235b: null, llama4_scout: null, interpretation: "Spearman ρ=0.67 across 19 langs"}

    figures_description:
      - >
        Figure 2: Overlaid Pareto frontiers for Qwen3 (circles) and Llama4 (triangles) on
        same axes (EN AUROC × ZS transfer mean). Qwen3 frontier is wider and steeper; Llama4
        is more compact and flatter. Annotated inset: depth percentage labels show Qwen3's optimal
        transfer at 43% depth vs Llama4 at 67% depth — architecture-dependent optimal operating
        point. This is the main Figure 1 of the paper.
    analysis: >
      Llama 4 Scout 确认 Pareto frontier 的跨架构泛化性，但 frontier shape 明显不同：
      更 flat、更 compact、更 noisy。这支持 Claim 1 的 "architecture-dependent" 修饰语。
      关键对比：Qwen3 的最优迁移在 43% 深度，Llama4 在 67% 深度——practitioners 不能
      假设一个固定的 "最优层百分比"。Llama4 较低的层序一致性（0.56 vs 0.71）暗示
      其内部 multilingual representation 的组织方式更分散，可能与 Scout 的 MoE routing
      策略有关。两架构的 frontier agreement 0.67 说明定性趋势共享但定量不可直接迁移。

  ##############################################################################
  # plan_003 — CaCLR Implementation and Comparative Evaluation
  ##############################################################################
  - name: "CaCLR Implementation and Comparative Evaluation"
    plan_id: plan_003
    description: >
      L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency. Trained using English correctness
      labels + unlabeled parallel activations from 19 target languages.
      Hyperparameter sweep: α∈{0.1,0.2,0.3,0.5,1.0}, β∈{0.05,0.1,0.15,0.2,0.3}.
      Compared against 4 baselines across full Pareto frontier for both models × 20 languages.
    expected_results:
      best_alpha: 0.30
      best_beta: 0.15
      # At Pareto-optimal transfer layer (Qwen3 L40)
      qwen3_L40_caclr_auroc_mean: 0.738
      qwen3_L40_caclr_ece_mean: 0.112
      qwen3_L40_linproj_auroc_mean: 0.724
      qwen3_L40_zeroshot_auroc_mean: 0.696
      qwen3_L40_caclr_vs_linproj_pp: 1.4
      # At best-English layer (Qwen3 L76)
      qwen3_L76_caclr_auroc_mean: 0.695
      qwen3_L76_linproj_auroc_mean: 0.678
      qwen3_L76_caclr_vs_linproj_pp: 1.7
      # At Pareto-optimal transfer layer (Llama4 L32)
      llama4_L32_caclr_auroc_mean: 0.717
      llama4_L32_linproj_auroc_mean: 0.705
      llama4_L32_caclr_vs_linproj_pp: 1.2
      # Cross-model summary
      caclr_vs_linproj_auroc_delta_mean_pp: 1.3
      caclr_ece_reduction_vs_tempcal_pct: 21.1
      caclr_improvement_over_zs_pass_rate: 0.89  # 17/19
      caclr_improvement_over_linproj_pass_rate: 0.74  # 14/19
      # Pareto frontier shift
      qwen3_caclr_optimal_layer: L52
      qwen3_zs_optimal_layer: L40
      qwen3_frontier_shift_layers: 12
      llama4_caclr_optimal_layer: L36
      llama4_zs_optimal_layer: L32
      llama4_frontier_shift_layers: 4
      # Failures
      caclr_fails_vs_linproj_langs: [th, my, am, yo, te]
      mean_shift_any_improvement: 1  # out of 19
    result_rationale: >
      CaCLR 在 median 档位下表现为 "matches or marginally exceeds linear projection"。
      核心原因：consistency term（L_consistency）对齐的是 unlabeled parallel activations
      的 probe output distribution，在中-高资源语言中有效（parallel corpus 质量好，
      激活空间足够对齐），但在低资源语言中由于 (a) GlobalMMLU 翻译噪声 (b) tokenizer
      覆盖率低导致 activation 本身质量差，consistency 信号变成噪声。因此 CaCLR 比
      zero-shot 有显著改善（+4.2pp at L40），但比 linear projection 仅高 1.3pp 平均——
      因为 linear projection 已经利用了 target-language activations 做对齐。CaCLR 的
      真正优势在 Pareto shift：它把最优工作层从 L40 推到 L52（Qwen3），在更深层维持
      迁移质量，同时获得 +2.0pp 英语 AUROC。SB-ECE loss 使 CaCLR probe 自带 calibration，
      ECE 比 temperature-scaled zero-shot 低 21.1%——这是方法论层面的 practical benefit。
      Hyperparameter 敏感度中等：α=0.3 在 0.2-0.5 范围内差异小于 0.5pp，β 更敏感——
      β>0.2 时 consistency 过强导致英语 AUROC 下降。5 个失败语言（th/my/am/yo/te）
      中 4 个是低资源或 activation 质量低的语言，th 是 mid-resource 但独特的声调语言
      导致 alignment 困难。
    tables:
      - title: "5-Method Comparison at Qwen3-235B Pareto-Optimal Layer (L40)"
        columns: [method, auroc_mean, auroc_high, auroc_mid, auroc_low, ece_mean, brier_mean]
        data:
          - {method: zero-shot, auroc_mean: 0.696, auroc_high: 0.753, auroc_mid: 0.711, auroc_low: 0.607, ece_mean: 0.148, brier_mean: 0.286}
          - {method: mean-shift, auroc_mean: 0.683, auroc_high: 0.742, auroc_mid: 0.698, auroc_low: 0.591, ece_mean: 0.155, brier_mean: 0.294}
          - {method: linear-proj, auroc_mean: 0.724, auroc_high: 0.775, auroc_mid: 0.738, auroc_low: 0.633, ece_mean: 0.121, brier_mean: 0.261}
          - {method: few-shot-25, auroc_mean: 0.711, auroc_high: 0.766, auroc_mid: 0.725, auroc_low: 0.618, ece_mean: 0.132, brier_mean: 0.270}
          - {method: few-shot-100, auroc_mean: 0.743, auroc_high: 0.791, auroc_mid: 0.756, auroc_low: 0.655, ece_mean: 0.108, brier_mean: 0.247}
          - {method: CaCLR, auroc_mean: 0.738, auroc_high: 0.786, auroc_mid: 0.754, auroc_low: 0.636, ece_mean: 0.112, brier_mean: 0.251}

      - title: "5-Method Comparison at Llama 4 Scout L32"
        columns: [method, auroc_mean, auroc_high, auroc_mid, auroc_low, ece_mean]
        data:
          - {method: zero-shot, auroc_mean: 0.679, auroc_high: 0.738, auroc_mid: 0.694, auroc_low: 0.585, ece_mean: 0.153}
          - {method: mean-shift, auroc_mean: 0.668, auroc_high: 0.726, auroc_mid: 0.682, auroc_low: 0.577, ece_mean: 0.161}
          - {method: linear-proj, auroc_mean: 0.705, auroc_high: 0.758, auroc_mid: 0.720, auroc_low: 0.610, ece_mean: 0.129}
          - {method: few-shot-25, auroc_mean: 0.694, auroc_high: 0.749, auroc_mid: 0.708, auroc_low: 0.602, ece_mean: 0.138}
          - {method: few-shot-100, auroc_mean: 0.728, auroc_high: 0.776, auroc_mid: 0.741, auroc_low: 0.640, ece_mean: 0.113}
          - {method: CaCLR, auroc_mean: 0.717, auroc_high: 0.769, auroc_mid: 0.733, auroc_low: 0.618, ece_mean: 0.122}

      - title: "CaCLR vs Linear Projection per Resource Tier (Qwen3, averaged across Pareto layers)"
        columns: [tier, n_langs, caclr_auroc, linproj_auroc, delta_pp, caclr_wins]
        data:
          - {tier: high, n_langs: 6, caclr_auroc: 0.786, linproj_auroc: 0.775, delta_pp: 1.1, caclr_wins: "6/6"}
          - {tier: mid, n_langs: 8, caclr_auroc: 0.754, linproj_auroc: 0.738, delta_pp: 1.6, caclr_wins: "7/8"}
          - {tier: low, n_langs: 5, caclr_auroc: 0.636, linproj_auroc: 0.633, delta_pp: 0.3, caclr_wins: "1/5"}

      - title: "CaCLR Consistency Term Ablation (Qwen3 L52)"
        note: "α=0.30 fixed; β=0 is calibrated-only probe"
        columns: [config, auroc_mean, ece_mean, high_delta_vs_linproj, mid_delta_vs_linproj, low_delta_vs_linproj]
        data:
          - {config: "α=0.3 β=0 (no consistency)", auroc_mean: 0.716, ece_mean: 0.119, high_delta_vs_linproj: 0.3, mid_delta_vs_linproj: -0.2, low_delta_vs_linproj: -0.5}
          - {config: "α=0.3 β=0.15 (full CaCLR)", auroc_mean: 0.733, ece_mean: 0.112, high_delta_vs_linproj: 0.8, mid_delta_vs_linproj: 1.4, low_delta_vs_linproj: -0.2}
          - {config: "α=0 β=0.15 (consistency only)", auroc_mean: 0.708, ece_mean: 0.136, high_delta_vs_linproj: -0.4, mid_delta_vs_linproj: 0.6, low_delta_vs_linproj: -0.8}

      - title: "Hyperparameter Sensitivity (Qwen3, validation set mean AUROC across 5 langs)"
        columns: [alpha, beta_0.05, beta_0.10, beta_0.15, beta_0.20, beta_0.30]
        data:
          - {alpha: 0.10, beta_0.05: 0.704, beta_0.10: 0.709, beta_0.15: 0.711, beta_0.20: 0.708, beta_0.30: 0.699}
          - {alpha: 0.20, beta_0.05: 0.711, beta_0.10: 0.718, beta_0.15: 0.724, beta_0.20: 0.720, beta_0.30: 0.708}
          - {alpha: 0.30, beta_0.05: 0.715, beta_0.10: 0.723, beta_0.15: 0.731, beta_0.20: 0.726, beta_0.30: 0.712}
          - {alpha: 0.50, beta_0.05: 0.712, beta_0.10: 0.719, beta_0.15: 0.725, beta_0.20: 0.718, beta_0.30: 0.701}
          - {alpha: 1.00, beta_0.05: 0.698, beta_0.10: 0.703, beta_0.15: 0.706, beta_0.20: 0.695, beta_0.30: 0.674}

    figures_description:
      - >
        Figure 3a: Pareto frontier shift — overlaid zero-shot frontier (grey) and CaCLR frontier
        (blue) for Qwen3. CaCLR frontier is shifted up-and-right: at the same English AUROC,
        CaCLR achieves higher transfer; at the same transfer quality, CaCLR operates at deeper
        layers. Annotated: zero-shot optimal (L40) vs CaCLR optimal (L52), with arrows showing
        +2.0pp English gain and +1.2pp transfer gain.
      - >
        Figure 3b: Bar chart — CaCLR AUROC improvement over linear projection, grouped by
        resource tier. High-resource bars around +1.1pp (all positive). Mid-resource bars around
        +1.6pp (7/8 positive, th near zero). Low-resource bars around +0.3pp (mostly near zero
        or negative). Clear visual: CaCLR's consistency term primarily benefits mid-resource languages.
      - >
        Figure 3c: ECE comparison — grouped bar chart with 5 methods × 3 resource tiers.
        CaCLR ECE bars consistently among the lowest, comparable to few-shot-100 for high/mid
        resource but without requiring any target-language labels.
    analysis: >
      CaCLR 的 median-tier 表现支持 "zero-label alternative that matches supervised transfer"
      的 framing，而非 "大幅超越" 的 framing。核心发现：(1) CaCLR 在 zero-label 设定下
      接近 few-shot-100 的性能（差 0.5pp AUROC，差 0.4pp ECE），这是 practical value 的
      来源；(2) vs linear projection 仅 +1.3pp，但 CaCLR 不需要任何 target-language 数据
      结构假设（linear projection 假设线性可分对齐），是更 principled 的方案；(3)
      consistency term 的 ablation 清晰显示其主要贡献在 mid-resource 语言（+1.6pp），
      这些语言有足够好的 parallel activation 质量让 consistency loss 有效，但又不像
      high-resource 那样 zero-shot 已经很好。Paper 应将 CaCLR 定位为 "practical tool
      for the mid-resource sweet spot" 而非 universal improvement。

  ##############################################################################
  # plan_004 — Difficulty-Controlled Ablation
  ##############################################################################
  - name: "Difficulty-Controlled Ablation"
    plan_id: plan_004
    description: >
      IRT difficulty probes (Ridge regression on human difficulty scores per Civelli et al.)
      trained per layer, difficulty direction projected out of activations, correctness probes
      retrained on residuals, transfer evaluated. 10 languages × 8 layers per model.
    expected_results:
      difficulty_probe_en_R2_mean: 0.68
      difficulty_probe_zs_R2_mean: 0.61
      decomp_difficulty_var_explained_pct: 37
      original_transfer_gap_pp: 15.2   # averaged across both models
      residual_transfer_gap_pp: 11.4
      gap_reduction_pp: 3.8
      gap_reduction_pct: 25   # 3.8/15.2 — lower than var_explained because nonlinear
      residual_en_auroc_drop: 0.038  # English AUROC drops after removing difficulty
      language_family_cluster_effect: "IE languages (de/fr/es/pl/ru) cluster; others scattered"
      capability_residual_noisy: true
      prescriptive_accuracy: 0.72  # decomposition correctly predicts method choice 72% of cases
    result_rationale: >
      Difficulty 是已知的跨语言可迁移特征（Civelli et al. 直接证明了 IRT difficulty probe
      的跨语言迁移性）。在 median 档，difficulty 解释了 correctness direction 37% 的方差，
      因为 "题目难不难" 确实是 correctness 的一个强组成部分（简单题各语言都对，难题各
      语言都错）。但 correctness 还包含 "模型在该语言上是否具备回答这道题的 capability"
      这一 language-dependent 成分。投影掉 difficulty 后，transfer gap 从 15.2pp 缩小到
      11.4pp（减少 25%），比 variance-explained 的 37% 低是因为 projection 是线性的而
      difficulty-correctness 的关系有非线性成分。残差中的 capability-specific 信号是 noisy
      的：高资源语言表现出清晰的 language-family clustering（IE 语言的 capability profiles
      相似），但低资源语言的 capability residual 被 tokenization 和数据质量 confound，
      无法干净分离。Prescriptive accuracy 72% 意味着：当 decomposition 预测 "这个
      language-layer 对简单 baseline 就够了" 时，72% 的情况下确实如此——有用但不完美。
      Paper 应将此 framing 为 "partial decomposition that explains the transferable component
      and predicts method choice, but capability residual remains confounded"。
    tables:
      - title: "Difficulty Probe Quality by Language (Qwen3 L48)"
        columns: [lang, tier, difficulty_R2, zs_transfer_R2, delta]
        data:
          - {lang: en, tier: high, difficulty_R2: 0.71, zs_transfer_R2: null, delta: null}
          - {lang: zh, tier: high, difficulty_R2: null, zs_transfer_R2: 0.67, delta: -0.04}
          - {lang: de, tier: high, difficulty_R2: null, zs_transfer_R2: 0.68, delta: -0.03}
          - {lang: es, tier: high, difficulty_R2: null, zs_transfer_R2: 0.69, delta: -0.02}
          - {lang: ar, tier: mid, difficulty_R2: null, zs_transfer_R2: 0.63, delta: -0.08}
          - {lang: hi, tier: mid, difficulty_R2: null, zs_transfer_R2: 0.61, delta: -0.10}
          - {lang: ko, tier: mid, difficulty_R2: null, zs_transfer_R2: 0.60, delta: -0.11}
          - {lang: vi, tier: mid, difficulty_R2: null, zs_transfer_R2: 0.58, delta: -0.13}
          - {lang: sw, tier: low, difficulty_R2: null, zs_transfer_R2: 0.49, delta: -0.22}
          - {lang: te, tier: low, difficulty_R2: null, zs_transfer_R2: 0.51, delta: -0.20}

      - title: "Decomposition Effect on Transfer Gap (Qwen3, 8 layers averaged)"
        columns: [component, en_auroc, zs_transfer_mean_9lang, gap_pp]
        data:
          - {component: "original correctness probe", en_auroc: 0.796, zs_transfer_mean_9lang: 0.674, gap_pp: 12.2}
          - {component: "difficulty probe only", en_auroc: 0.714, zs_transfer_mean_9lang: 0.670, gap_pp: 4.4}
          - {component: "residual (capability) probe", en_auroc: 0.758, zs_transfer_mean_9lang: 0.653, gap_pp: 10.5}
          - {component: "difficulty + residual reconstructed", en_auroc: 0.791, zs_transfer_mean_9lang: 0.671, gap_pp: 12.0}

      - title: "Variance Decomposition by Layer Depth (Qwen3)"
        columns: [layer, difficulty_var_pct, capability_var_pct, reconstruction_loss_pct]
        data:
          - {layer: L20, difficulty_var_pct: 44, capability_var_pct: 51, reconstruction_loss_pct: 5}
          - {layer: L28, difficulty_var_pct: 42, capability_var_pct: 53, reconstruction_loss_pct: 5}
          - {layer: L36, difficulty_var_pct: 40, capability_var_pct: 54, reconstruction_loss_pct: 6}
          - {layer: L48, difficulty_var_pct: 37, capability_var_pct: 56, reconstruction_loss_pct: 7}
          - {layer: L56, difficulty_var_pct: 34, capability_var_pct: 58, reconstruction_loss_pct: 8}
          - {layer: L64, difficulty_var_pct: 31, capability_var_pct: 60, reconstruction_loss_pct: 9}
          - {layer: L76, difficulty_var_pct: 28, capability_var_pct: 62, reconstruction_loss_pct: 10}
          - {layer: L84, difficulty_var_pct: 26, capability_var_pct: 63, reconstruction_loss_pct: 11}

      - title: "Prescriptive Accuracy: Does Decomposition Predict Method Choice?"
        note: "For each lang-layer pair, decomposition predicts 'zero-shot suffices' if difficulty component dominates (>50%), else 'CaCLR needed'. Ground truth from plan_003."
        columns: [tier, n_pairs, correct_predictions, accuracy]
        data:
          - {tier: high, n_pairs: 48, correct_predictions: 38, accuracy: 0.79}
          - {tier: mid, n_pairs: 64, correct_predictions: 47, accuracy: 0.73}
          - {tier: low, n_pairs: 40, correct_predictions: 25, accuracy: 0.63}
          - {tier: all, n_pairs: 152, correct_predictions: 110, accuracy: 0.72}

    figures_description:
      - >
        Figure 4a: Stacked bar chart — per layer, the proportion of correctness direction
        variance attributed to difficulty (blue), capability (orange), reconstruction loss (grey).
        Difficulty share monotonically decreases from 44% at L20 to 26% at L84; capability
        share correspondingly increases. Visual narrative: deeper layers have more capability-specific
        information, which is why they transfer worse.
      - >
        Figure 4b: Scatter — x-axis: difficulty variance share (%), y-axis: zero-shot transfer
        AUROC for each language-layer pair. Positive correlation (r≈0.55): higher difficulty share
        predicts better zero-shot transfer. But substantial scatter, especially for low-resource
        languages (marked with different symbol). Regression line shown with confidence band.
    analysis: >
      Decomposition 部分成功：difficulty component 确实是 transferable part，其 share 随
      depth 递减完美解释了 Pareto tradeoff 的机制——deeper layers 积累更多 capability-specific
      信息，这些信息是 language-dependent 的。但 "partial" 体现在两方面：(1) difficulty
      仅解释 37% 的 variance，多数 correctness signal 在 capability residual 中；(2)
      capability residual 本身不是干净的 language-specific signal，而是与 language-family
      effects confounded（IE 语言 cluster 说明 capability 共享有 phylogenetic 结构）。
      Prescriptive accuracy 72% 是一个有用但不完美的 practical tool。Paper 应将此 framed
      为 "first decomposition of cross-lingual correctness transfer that identifies the
      transferable component and partially predicts method choice, with the capability
      residual as a target for future work."

  ##############################################################################
  # plan_005 — Cross-Lingual Orthogonality Analysis
  ##############################################################################
  - name: "Cross-Lingual Orthogonality Analysis"
    plan_id: plan_005
    description: >
      Extract verbalized confidence direction (prompt for P(correct) score, fit linear probe),
      compute cosine similarity with correctness direction across 20 languages × 2 architectures.
      Resource-tier and language-family analysis.
    expected_results:
      cosine_mean_all: 0.091
      cosine_mean_qwen3: 0.086
      cosine_mean_llama4: 0.096
      cosine_high_mean: 0.059
      cosine_mid_mean: 0.084
      cosine_low_mean: 0.147
      cosine_low_std: 0.032
      cosine_range: [0.04, 0.21]
      en_cosine_qwen3: 0.04
      en_cosine_llama4: 0.05
      cross_arch_cosine_corr: 0.78  # per-language cosine values correlate across architectures
      orthogonality_holds_all_20: true  # all < 0.25 threshold
    result_rationale: >
      Miao & Ungar (2026) 在英语 7-8B 模型上发现 correctness-confidence cosine < 0.04。
      在 median 档，该 orthogonality 跨语言泛化但有 resource-tier 梯度。High-resource
      语言（cosine ~0.06）接近英语水平，因为模型在这些语言上有充足的训练数据，
      verbalized confidence 和 internal correctness 的分离是 well-learned 的。
      Mid-resource 语言（cosine ~0.08）稍高，模型的 confidence 表达在这些语言上
      不那么 calibrated。Low-resource 语言（cosine ~0.15, std 0.032）明显更高且 variance
      更大——模型在低资源语言上的 verbalized confidence 方向本身就不稳定（probe 拟合
      noisy），导致与 correctness 的 cosine 更大也更不可靠。但即使最高的 yo (0.21)
      也远低于 "parallel" 的 0.7+，orthogonality 的定性结论在所有 20 语言上成立。
      Cross-architecture correlation 0.78 表明 per-language cosine 值在两个模型上高度
      一致——这是 structural property，不是 model-specific artifact。
    tables:
      - title: "Correctness-Confidence Cosine Similarity by Language"
        columns: [lang, tier, qwen3_cosine, llama4_cosine, mean]
        data:
          - {lang: en, tier: high, qwen3_cosine: 0.04, llama4_cosine: 0.05, mean: 0.045}
          - {lang: zh, tier: high, qwen3_cosine: 0.05, llama4_cosine: 0.06, mean: 0.055}
          - {lang: de, tier: high, qwen3_cosine: 0.06, llama4_cosine: 0.07, mean: 0.065}
          - {lang: fr, tier: high, qwen3_cosine: 0.05, llama4_cosine: 0.06, mean: 0.055}
          - {lang: es, tier: high, qwen3_cosine: 0.05, llama4_cosine: 0.06, mean: 0.055}
          - {lang: ja, tier: high, qwen3_cosine: 0.07, llama4_cosine: 0.08, mean: 0.075}
          - {lang: ru, tier: high, qwen3_cosine: 0.06, llama4_cosine: 0.07, mean: 0.065}
          - {lang: ar, tier: mid, qwen3_cosine: 0.08, llama4_cosine: 0.09, mean: 0.085}
          - {lang: hi, tier: mid, qwen3_cosine: 0.07, llama4_cosine: 0.08, mean: 0.075}
          - {lang: ko, tier: mid, qwen3_cosine: 0.08, llama4_cosine: 0.09, mean: 0.085}
          - {lang: pt, tier: mid, qwen3_cosine: 0.06, llama4_cosine: 0.07, mean: 0.065}
          - {lang: vi, tier: mid, qwen3_cosine: 0.09, llama4_cosine: 0.10, mean: 0.095}
          - {lang: th, tier: mid, qwen3_cosine: 0.10, llama4_cosine: 0.11, mean: 0.105}
          - {lang: tr, tier: mid, qwen3_cosine: 0.08, llama4_cosine: 0.09, mean: 0.085}
          - {lang: pl, tier: mid, qwen3_cosine: 0.07, llama4_cosine: 0.08, mean: 0.075}
          - {lang: sw, tier: low, qwen3_cosine: 0.12, llama4_cosine: 0.13, mean: 0.125}
          - {lang: te, tier: low, qwen3_cosine: 0.10, llama4_cosine: 0.11, mean: 0.105}
          - {lang: my, tier: low, qwen3_cosine: 0.15, llama4_cosine: 0.16, mean: 0.155}
          - {lang: am, tier: low, qwen3_cosine: 0.16, llama4_cosine: 0.17, mean: 0.165}
          - {lang: yo, tier: low, qwen3_cosine: 0.18, llama4_cosine: 0.19, mean: 0.185}

      - title: "Orthogonality Summary by Resource Tier"
        columns: [tier, n_langs, cosine_mean, cosine_std, cosine_min, cosine_max]
        data:
          - {tier: high, n_langs: 7, cosine_mean: 0.059, cosine_std: 0.010, cosine_min: 0.04, cosine_max: 0.08}
          - {tier: mid, n_langs: 8, cosine_mean: 0.084, cosine_std: 0.013, cosine_min: 0.06, cosine_max: 0.11}
          - {tier: low, n_langs: 5, cosine_mean: 0.147, cosine_std: 0.032, cosine_min: 0.10, cosine_max: 0.19}
          - {tier: all, n_langs: 20, cosine_mean: 0.091, cosine_std: 0.040, cosine_min: 0.04, cosine_max: 0.19}

    figures_description:
      - >
        Figure 5: Dot plot — x-axis: cosine similarity, y-axis: languages (sorted by resource
        tier, then by cosine). Two markers per language (circle=Qwen3, triangle=Llama4). Vertical
        dashed line at cosine=0.25 ("orthogonality threshold"). All points to the left. Clear
        visual gradient from high-resource (clustered near 0.05) to low-resource (spread between
        0.10-0.19). Error bars show bootstrap 95% CI. Annotation: "Miao & Ungar EN baseline:
        cos < 0.04" with arrow pointing to English dots.
    analysis: >
      Claim 4 在 median 档下获得 strong support for high/mid-resource languages, qualified
      support for low-resource。核心结论：correctness-confidence orthogonality 是一个跨语言
      的 structural property，不是英语特有的。但 resource-tier gradient（high 0.06 → low 0.15）
      表明该 property 在低资源语言上更弱——这可能是因为模型在低资源语言上的 confidence
      calibration 本身就差，confidence direction 拟合不稳定。Cross-architecture 一致性 0.78
      进一步强化了 structural claim。Paper 应呈现为 "orthogonality universally holds (all
      cos < 0.25) but varies in degree, with implications for why output-based calibration is
      structurally limited across all languages — but especially limited for high-resource
      languages where the orthogonality is strongest."

  ##############################################################################
  # plan_006 — Probe Complexity Comparison
  ##############################################################################
  - name: "Probe Complexity Comparison"
    plan_id: plan_006
    description: >
      Logistic regression vs 2-layer MLP (hidden dim 256, ReLU) at each probed layer
      for both models. Compare English accuracy, cross-lingual transfer degradation,
      and calibration quality. Test hypothesis: linear probes transfer better.
    expected_results:
      # Qwen3 at best-EN layer L76
      qwen3_L76_logreg_en_auroc: 0.812
      qwen3_L76_mlp_en_auroc: 0.827
      qwen3_L76_logreg_transfer_mean: 0.644
      qwen3_L76_mlp_transfer_mean: 0.607
      qwen3_L76_logreg_transfer_drop_pp: 16.8
      qwen3_L76_mlp_transfer_drop_pp: 22.0
      # Llama4 at best-EN layer L44
      llama4_L44_logreg_en_auroc: 0.793
      llama4_L44_mlp_en_auroc: 0.812
      llama4_L44_logreg_transfer_mean: 0.657
      llama4_L44_mlp_transfer_mean: 0.625
      llama4_L44_logreg_transfer_drop_pp: 13.6
      llama4_L44_mlp_transfer_drop_pp: 18.7
      # Summary
      mlp_en_advantage_pp_mean: 1.7
      logreg_transfer_advantage_pp_mean: 3.5
      hypothesis_confirmed: true
    result_rationale: >
      MLP 在英语上多 ~1.7pp AUROC，因为非线性层可以捕获 correctness 与 activation 之间
      的非线性关系。但 MLP 在跨语言迁移上劣 ~3.5pp，因为非线性决策边界更容易 overfit
      英语 activation 的分布特征，这些特征在其他语言中不保持。Linear probe 的决策
      超平面在 high-dimensional space 中更 "blunt"，因此更 robust to distribution shift。
      这个结果与 Civelli et al. 的发现一致（linear > nonlinear for cross-lingual difficulty
      transfer），也回应了 reviewer 可能提出的 "为什么不用更复杂的 probe" 的质疑。
      Paper 据此使用 logistic regression 作为 primary probe，MLP 仅作为 ablation 报告。
    tables:
      - title: "LogReg vs MLP at Key Layers (Qwen3-235B)"
        columns: [layer, logreg_en, mlp_en, en_delta, logreg_transfer, mlp_transfer, transfer_delta]
        data:
          - {layer: L40, logreg_en: 0.776, mlp_en: 0.794, en_delta: 1.8, logreg_transfer: 0.696, mlp_transfer: 0.672, transfer_delta: -2.4}
          - {layer: L52, logreg_en: 0.796, mlp_en: 0.813, en_delta: 1.7, logreg_transfer: 0.682, mlp_transfer: 0.651, transfer_delta: -3.1}
          - {layer: L64, logreg_en: 0.807, mlp_en: 0.824, en_delta: 1.7, logreg_transfer: 0.661, mlp_transfer: 0.626, transfer_delta: -3.5}
          - {layer: L76, logreg_en: 0.812, mlp_en: 0.827, en_delta: 1.5, logreg_transfer: 0.644, mlp_transfer: 0.607, transfer_delta: -3.7}

      - title: "LogReg vs MLP at Key Layers (Llama 4 Scout)"
        columns: [layer, logreg_en, mlp_en, en_delta, logreg_transfer, mlp_transfer, transfer_delta]
        data:
          - {layer: L24, logreg_en: 0.741, mlp_en: 0.758, en_delta: 1.7, logreg_transfer: 0.677, mlp_transfer: 0.654, transfer_delta: -2.3}
          - {layer: L32, logreg_en: 0.771, mlp_en: 0.789, en_delta: 1.8, logreg_transfer: 0.679, mlp_transfer: 0.651, transfer_delta: -2.8}
          - {layer: L40, logreg_en: 0.790, mlp_en: 0.808, en_delta: 1.8, logreg_transfer: 0.663, mlp_transfer: 0.631, transfer_delta: -3.2}
          - {layer: L44, logreg_en: 0.793, mlp_en: 0.812, en_delta: 1.9, logreg_transfer: 0.657, mlp_transfer: 0.625, transfer_delta: -3.2}

    figures_description:
      - >
        Figure S1 (Appendix): Dual-line plot per model — x-axis: layer depth, y-axis: AUROC.
        Solid lines = LogReg (blue = English, orange = transfer mean). Dashed lines = MLP
        (blue = English, orange = transfer mean). The "scissors" pattern: MLP blue line is
        above LogReg blue line (better English), but MLP orange line is below LogReg orange
        line (worse transfer). Gap widens at deeper layers.
    analysis: >
      Hypothesis confirmed: linear probes transfer significantly better cross-lingually than
      MLP probes (+3.5pp average), while sacrificing only 1.7pp English accuracy. The transfer
      advantage of linear probes is larger at deeper layers (where distribution shift is worst),
      which is consistent with the Pareto tradeoff mechanism — nonlinear probes amplify the
      depth-dependent distribution shift. This result justifies the methodological choice of
      logistic regression as the primary probe throughout the paper.

  ##############################################################################
  # plan_007 — Additional Benchmark Evaluation
  ##############################################################################
  - name: "Additional Benchmark Evaluation"
    plan_id: plan_007
    description: >
      Evaluate best probes + CaCLR on Belebele (20 languages, reading comprehension)
      and MMLU-ProX (20 languages, harder STEM questions). Tests generalization of
      Pareto frontier and CaCLR beyond GlobalMMLU.
    expected_results:
      # Belebele — reading comprehension, generally easier
      belebele_en_auroc_best: 0.798
      belebele_zs_transfer_mean_at_best_transfer: 0.708
      belebele_pareto_replicates: true
      belebele_caclr_vs_linproj_pp: 1.1
      belebele_best_transfer_layer_qwen3: L44  # slightly deeper than GlobalMMLU's L40
      # MMLU-ProX — harder questions, clearer correctness signal
      mmlupx_en_auroc_best: 0.824
      mmlupx_zs_transfer_mean_at_best_transfer: 0.681
      mmlupx_pareto_replicates: true
      mmlupx_caclr_vs_linproj_pp: 1.6
      mmlupx_best_transfer_layer_qwen3: L40
      # Low-resource robustness
      belebele_low_resource_pass_rate: 0.6  # 3/5
      mmlupx_low_resource_pass_rate: 0.4   # 2/5 — harder questions amplify low-resource failures
    result_rationale: >
      Pareto frontier 作为 representation structure 的 property，不应依赖特定 benchmark。
      Belebele（阅读理解）和 MMLU-ProX（更难 STEM 题）提供了两个不同难度和认知类型的
      测试。Belebele 稍简单，英语 AUROC 稍低（0.798 vs 0.812）因为 reading comprehension
      的 correctness 比 knowledge QA 更依赖 surface patterns，linear probe 的 ceiling 更低。
      但迁移质量稍高（0.708 vs 0.696）因为阅读理解的跨语言 pattern 更相似。MMLU-ProX
      更难，英语 AUROC 更高（0.824）因为难题的 correctness signal 更 salient（模型更
      "确定" 自己是否知道），但迁移稍差（0.681）因为 STEM 知识的跨语言 variation 更大。
      CaCLR 在 MMLU-ProX 上优势稍大（+1.6pp vs +1.1pp）因为更难的题目有更多 distribution
      shift 可以被 consistency term 修正。两个 benchmark 都复现了 Pareto 结构，确认其
      generalizability。低资源在 MMLU-ProX 上更差（2/5 vs 3/5）因为难题放大了数据不足的问题。
    tables:
      - title: "Cross-Benchmark Comparison (Qwen3-235B, LogReg)"
        columns: [metric, GlobalMMLU, Belebele, MMLU_ProX]
        data:
          - {metric: en_auroc_best, GlobalMMLU: 0.812, Belebele: 0.798, MMLU_ProX: 0.824}
          - {metric: best_en_layer, GlobalMMLU: L76, Belebele: L72, MMLU_ProX: L76}
          - {metric: best_transfer_layer, GlobalMMLU: L40, Belebele: L44, MMLU_ProX: L40}
          - {metric: zs_transfer_mean, GlobalMMLU: 0.696, Belebele: 0.708, MMLU_ProX: 0.681}
          - {metric: transfer_drop_pp, GlobalMMLU: 16.8, Belebele: 13.1, MMLU_ProX: 18.4}
          - {metric: caclr_vs_linproj_pp, GlobalMMLU: 1.4, Belebele: 1.1, MMLU_ProX: 1.6}
          - {metric: low_resource_pass_rate, GlobalMMLU: 0.6, Belebele: 0.6, MMLU_ProX: 0.4}

    figures_description:
      - >
        Figure S2 (Appendix): Three-panel Pareto frontier plots (GlobalMMLU / Belebele /
        MMLU-ProX) with identical axis scales. Visual pattern clearly replicates across all
        three: upward-then-left curve in all panels, with MMLU-ProX showing the steepest
        tradeoff and Belebele the mildest.
    analysis: >
      Cross-benchmark replication is the key result: Pareto frontier structure is benchmark-
      agnostic, confirming it reflects model representation properties rather than dataset
      artifacts. The quantitative differences (Belebele flatter, MMLU-ProX steeper) are
      interpretable and strengthen the paper's analysis. CaCLR's benchmark-robust improvement
      (+1.1 to +1.6pp) confirms its general utility.

  ##############################################################################
  # plan_010 — INT8 Validation Ablation
  ##############################################################################
  - name: "INT8 Validation Ablation"
    plan_id: plan_010
    description: >
      Compare INT8 vs FP16 probing results at 5 representative layers for Llama 4 Scout
      on 5% random subset (~700 samples). Validates that INT8 quantization doesn't distort
      correctness signals in the activation space.
    expected_results:
      max_auroc_delta_pp: 0.3
      mean_auroc_delta_pp: 0.24
      direction_bias: "negligible (INT8 marginally lower at all layers)"
      cosine_sim_directions: 0.997  # INT8 and FP16 correctness directions nearly identical
      conclusion: "INT8 validated — no meaningful distortion of correctness signal"
    result_rationale: >
      INT8 weight-only quantization 保留了 activation space 的大部分结构（weight quantization
      引入的 perturbation 在 high-dimensional space 中被分摊，对线性 probe 的影响极小）。
      AUROC delta < 0.3pp 远低于实验中观测到的其他 effect sizes（transfer drop 13-17pp,
      CaCLR improvement 1-4pp）。Correctness direction 的 cosine similarity 0.997 说明
      quantization 几乎不改变 direction，只是 slightly perturb magnitude。这是 expected
      result，但对 reviewer 来说是必要的 due diligence——没有这个 ablation，reviewer
      可能质疑 INT8 是否引入 systematic bias。
    tables:
      - title: "INT8 vs FP16 Probing Results (Llama 4 Scout, 5% subset)"
        columns: [layer, int8_auroc, fp16_auroc, delta_pp, direction_cosine]
        data:
          - {layer: L4,  int8_auroc: 0.568, fp16_auroc: 0.571, delta_pp: -0.3, direction_cosine: 0.998}
          - {layer: L12, int8_auroc: 0.648, fp16_auroc: 0.651, delta_pp: -0.3, direction_cosine: 0.997}
          - {layer: L24, int8_auroc: 0.738, fp16_auroc: 0.740, delta_pp: -0.2, direction_cosine: 0.998}
          - {layer: L36, int8_auroc: 0.780, fp16_auroc: 0.782, delta_pp: -0.2, direction_cosine: 0.997}
          - {layer: L44, int8_auroc: 0.791, fp16_auroc: 0.794, delta_pp: -0.3, direction_cosine: 0.996}

    figures_description:
      - >
        Figure S3 (Appendix): Paired bar chart — 5 layers, INT8 (blue) vs FP16 (orange) bars.
        Bars nearly identical height at every layer. Annotation: "max Δ = 0.3pp". Simple,
        clean validation figure.
    analysis: >
      INT8 quantization is validated for correctness probing. The <0.3pp AUROC difference
      is well within noise levels and has no systematic direction. This ablation can be
      reported in 2-3 sentences in the Appendix with the table — no need for extended discussion.

  ##############################################################################
  # plan_008 — Gemma 4 31B Dense (P2, Camera-Ready)
  ##############################################################################
  - name: "Gemma 4 31B Dense — Camera-Ready Extension"
    plan_id: plan_008
    description: >
      Third architecture (60 layers, dense, FP16) for camera-ready version.
      Dense vs MoE architectural contrast. Full Pareto frontier, 20+ languages.
    expected_results:
      en_auroc_best: 0.805
      en_best_layer: L48
      best_transfer_layer: L32
      zs_transfer_mean_at_best_transfer: 0.709
      zs_transfer_drop_at_best_en_pp: 10.2
      pareto_frontier_shape: "smoother than MoE models, more gradual transfer decline"
      low_resource_pass_rate: 0.6  # 3/5
      caclr_vs_linproj_pp: 1.0
      frontier_agreement_with_qwen3: 0.62
      frontier_agreement_with_llama4: 0.71
    result_rationale: >
      Dense architecture 与 MoE 的关键差异：没有 routing 机制导致的 discrete layer-wise
      变化，representation 的 language-specificity 随 depth 更连续地增长。因此 Pareto
      frontier 更 smooth（transfer decline 更 gradual），transfer drop 仅 10.2pp（vs
      Qwen3 16.8pp, Llama4 13.6pp）。English AUROC 略低于 Qwen3（0.805 vs 0.812）因为
      31B dense 的 total compute 少于 235B MoE。Best transfer 在 53% 深度（L32/60），
      介于 Qwen3(43%) 和 Llama4(67%) 之间。CaCLR 优势更小（+1.0pp）因为 dense model
      的 representation shift across languages 本身更 gradual，simple baselines 已经
      表现不错。与 Llama4 的 frontier agreement (0.71) 高于与 Qwen3 (0.62)，可能因为
      Llama4 和 Gemma4 的训练数据组成更相似。
    tables:
      - title: "Three-Architecture Pareto Summary"
        columns: [metric, Qwen3_235B_MoE, Llama4_Scout_MoE, Gemma4_31B_Dense]
        data:
          - {metric: total_layers, Qwen3_235B_MoE: 94, Llama4_Scout_MoE: 48, Gemma4_31B_Dense: 60}
          - {metric: architecture, Qwen3_235B_MoE: MoE, Llama4_Scout_MoE: MoE, Gemma4_31B_Dense: Dense}
          - {metric: en_auroc_best, Qwen3_235B_MoE: 0.812, Llama4_Scout_MoE: 0.793, Gemma4_31B_Dense: 0.805}
          - {metric: best_transfer_depth_pct, Qwen3_235B_MoE: 43, Llama4_Scout_MoE: 67, Gemma4_31B_Dense: 53}
          - {metric: transfer_drop_pp, Qwen3_235B_MoE: 16.8, Llama4_Scout_MoE: 13.6, Gemma4_31B_Dense: 10.2}
          - {metric: frontier_smoothness, Qwen3_235B_MoE: "sharp", Llama4_Scout_MoE: "flat/noisy", Gemma4_31B_Dense: "smooth"}
          - {metric: caclr_benefit_pp, Qwen3_235B_MoE: 1.4, Llama4_Scout_MoE: 1.2, Gemma4_31B_Dense: 1.0}

    figures_description:
      - >
        Figure 6 (Camera-Ready): Three-model overlaid Pareto frontiers. Qwen3 (circles) shows
        widest, steepest frontier. Llama4 (triangles) shows compact, flat frontier. Gemma4
        (squares) shows smooth, intermediate frontier. Visual immediately communicates
        architecture-dependent Pareto structure. Inset table shows optimal transfer depth %.
    analysis: >
      Dense vs MoE 对比是 camera-ready 的最有价值的扩展。Dense 架构的 smoother frontier
      提供了 mechanistic insight：MoE routing 在深层的 language-specific expert selection
      可能是 Qwen3 sharp Pareto tradeoff 的原因，而 dense model 的 continuous feature
      evolution 产生更 gradual 的 language specificity 增长。三架构的 frontier 定性一致
      但定量不同，强化了 "Pareto frontier is universal but architecture-dependent" 的 headline claim。

  ##############################################################################
  # plan_009 — Extended Language Coverage (P2, Camera-Ready)
  ##############################################################################
  - name: "Extended Language Coverage — Camera-Ready Extension"
    plan_id: plan_009
    description: >
      Expand from 20 to 50+ languages using GlobalMMLU/Belebele full language sets.
      Tests how Pareto frontier patterns scale to long-tail languages.
    expected_results:
      total_languages: 53
      high_resource_count: 12
      mid_resource_count: 18
      low_resource_count: 23
      zs_transfer_mean_all_52: 0.651
      low_resource_pass_rate_23: 0.35  # 8/23
      very_low_resource_auroc_range: [0.50, 0.58]
      pareto_replicates_qualitatively: true
      new_failure_languages: ["qu", "ha", "gn", "lg", "ny", "sn", "xh", "zu", "ig", "mg", "rw", "so", "tn", "ts", "ve"]
      caclr_improvement_rate_52: 0.67  # 35/52, lower due to more low-resource langs
      layer_rank_consistency_52: 0.58  # lower with more diverse languages
    result_rationale: >
      扩展到 53 语言后，低资源尾部显著增长（23 个 low-resource vs 原来 5 个），整体
      指标下降是 expected 的。ZS transfer mean 从 0.696（20 langs）降至 0.651（52 non-en
      langs）因为新增语言大部分是低资源的非洲/大洋洲/美洲原住民语言，GlobalMMLU 翻译
      质量参差不齐。低资源 pass rate 从 0.6（3/5）降至 0.35（8/23）说明 "correctness
      direction universally transfers" 的说法在尾部语言不成立——但 Pareto 结构本身
      仍然定性存在。CaCLR 的 improvement rate 也从 0.74 降至 0.67，但仍是多数语言
      受益。Layer ranking consistency 从 0.71 降至 0.58，因为低资源语言的最优迁移层
      更分散。Paper 应将此 framing 为 "Pareto frontier scales to 50+ languages but with
      diminishing returns for very low-resource languages, motivating future work on
      low-resource-specific transfer methods."
    tables:
      - title: "Extended Coverage Summary by Tier"
        columns: [tier, n_langs_20, n_langs_53, mean_auroc_20, mean_auroc_53, pass_rate_20, pass_rate_53]
        data:
          - {tier: high, n_langs_20: 6, n_langs_53: 11, mean_auroc_20: 0.753, mean_auroc_53: 0.745, pass_rate_20: 1.0, pass_rate_53: 1.0}
          - {tier: mid, n_langs_20: 8, n_langs_53: 18, mean_auroc_20: 0.711, mean_auroc_53: 0.698, pass_rate_20: 1.0, pass_rate_53: 0.94}
          - {tier: low, n_langs_20: 5, n_langs_53: 23, mean_auroc_20: 0.607, mean_auroc_53: 0.571, pass_rate_20: 0.6, pass_rate_53: 0.35}
          - {tier: all, n_langs_20: 19, n_langs_53: 52, mean_auroc_20: 0.696, mean_auroc_53: 0.651, pass_rate_20: 0.89, pass_rate_53: 0.69}

    figures_description:
      - >
        Figure 7 (Camera-Ready): Language-level scatter — x-axis: log(pretraining data size
        estimate, tokens), y-axis: best zero-shot transfer AUROC. Clear positive correlation
        (r≈0.72). Horizontal dashed line at AUROC=0.60. Labels for notable languages.
        Below the line: cluster of 15 very-low-resource languages. Color by language family.
        Shows that transfer success is primarily a function of pretraining representation quality.
    analysis: >
      Extended coverage confirms the fundamental insight: Pareto frontier is a structural
      property that scales to 50+ languages, but the practical utility of zero-shot correctness
      probe transfer is bounded by pretraining data quantity. The 15 languages below the 0.60
      threshold are all in the lowest quintile of pretraining data, suggesting a minimum
      representation quality floor for this approach. This limitation should be acknowledged
      transparently in the Discussion section, not hidden — it's a valuable finding about the
      scope of probe-based calibration methods.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "010a8be7-2cc3-4a95-a2ee-4eb66e799e96",
  "isSidechain": false,
  "requestId": "req_011CbELtA4PQEQbpETwhLaKb",
  "type": "assistant",
  "uuid": "0a05eb9c-ac98-4426-a21f-cf1544ff5356",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFmWAh8esqYDyQrbFzaDxW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 46669,
      "output_tokens": 40432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 577,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 40432,
          "cache_read_input_tokens": 46669,
          "cache_creation_input_tokens": 577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 577
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Claims 1 and 4 fully hold. Claim 2 partially holds (decomposition works but is noisy). Claim 3 is mixed — CaCLR helps but only marginally beats linear pr…",
  "leafUuid": "0a05eb9c-ac98-4426-a21f-cf1544ff5356",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Multilingual correctness probe transfer pareto frontier",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Claims 1 and 4 fully hold. Claim 2 partially holds (decomposition works but is noisy). Claim 3 is mixed — CaCLR helps but only marginally beats linear pr…",
  "leafUuid": "0a05eb9c-ac98-4426-a21f-cf1544ff5356",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Multilingual correctness probe transfer pareto frontier",
  "sessionId": "2ff52ae3-7621-49aa-af5a-5d93d8966c1d"
}
```

---
