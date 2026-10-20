# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：All 4 claims fully validated at scale. Pareto frontier is crisp and architec

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/8c3e7e33-f999-45e6-9b77-c8618fc951cb.jsonl`
- **Structured JSON:** [`8ec294d15012d96eae90.json`](../../sessions/8e/8ec294d15012d96eae90.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T18:58:10.761Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T18:58:10.761Z",
  "sessionId": "8c3e7e33-f999-45e6-9b77-c8618fc951cb",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：All 4 claims fully validated at scale. Pareto frontier is crisp and architecture-consistent, decomposition cleanly separates, CaCLR decisively outperforms linear projection, orthogonality generalizes. Paper runs original framing with no claim adjustments.\n核心假设：['Pareto frontier (depth vs transferability tradeoff) replicates on both Qwen3-235B and Llama4 Scout with clear monotonic shape', 'CaCLR consistently outperforms linear projection — the consistency loss term provides genuine value beyond simple alignment', 'Difficulty-shared component accounts for majority of transferable signal; projecting it out isolates a clean capability-specific residual', 'Correctness-confidence orthogonality (cosine < 0.1) holds across all 20 languages and both architectures', 'Low-resource languages (sw, yo, ig) achieve usable zero-shot transfer (AUROC > 0.60)']\n关键指标范围：{'en_auroc_best_layer': [0.8, 0.86], 'zs_transfer_auroc_mean_19lang': [0.71, 0.79], 'zs_transfer_drop_mean_pp': [5, 12], 'caclr_vs_linproj_auroc_delta_pp': [2.5, 5.0], 'caclr_ece_reduction_vs_tempcal_pct': [30, 50], 'pareto_depth_transfer_rank_corr': [0.75, 0.95], 'decomp_difficulty_var_explained_pct': [55, 80], 'orthogonality_cosine_mean': [0.02, 0.08], 'low_resource_zs_pass_rate': [0.8, 1.0], 'caclr_improvement_pass_rate': [0.85, 1.0], 'pareto_frontier_agreement_across_arch': [0.8, 1.0]}\n叙事方向：Original framing stands: 'CaCLR shifts the cross-lingual calibration Pareto frontier.' All 4 claims form an unbroken causal chain — discovery → analysis → method → mechanism. Headline: CaCLR reduces non-EN ECE by 30-50% over temp scaling with zero target-language labels. Pareto frontier is the organizing principle, CaCLR is the actionable contribution, decomposition explains why it works, orthogonality explains why output-based methods can't.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: xling_calib_direction\nfocus: Core submission for EACL 2027 ARR: 2 models (Qwen3-235B + Llama 4 Scout) × 20 languages. Key risks: (1) CaCLR may not outperform simple linear projection; (2) difficulty-shared vs capability-specific decomposition may not cleanly separate; (3) orthogonality claim 4 may be seen as incremental. MVP showed mean-shift completely fails, Pareto tradeoff directly observed at L24 vs L27.\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) shifts the Pareto frontier by jointly optimizing calibration and cross-lingual invariance, enabling effective probe transfer at deeper, better-calibrated layers without target-language correctness labels.\n- MVP evidence: Mean-shift fails entirely (0/5 languages improved) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, and propose CaCLR to shift the frontier. This is both a field-level viability test and a practical method contribution.\n- **Headline template**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak\"** → 5 transfer conditions tested. Mean-shift failure (MVP-confirmed) motivates CaCLR. Mean-shift works for Xiao et al.'s knowledge boundary but fails for correctness — important finding.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR).\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request.\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    INT8 weight quantization.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: Needs 2× RTX 6000 PRO 96GB at INT8.\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency. Train CaCLR probes using English labels + unlabeled\n    parallel activations. Compare vs zero-shot, mean-shift, linear projection, few-shot\n    (25/100) across full Pareto frontier for both models × 20 languages. Hyperparameter\n    tuning (α, β) on held-out English + 5-language validation.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021.\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: Need IRT difficulty scores from GlobalMMLU or external source.\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'INT8 validation ablation: compare INT8 vs FP16 probing results at\n    5 representative layers for Llama 4 Scout on 5% random subset. Validates that\n    INT8 quantization doesn''t distort correctness signals.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 31B Dense (60 layers, dense, FP16): third architecture for\n    camera-ready. Full Pareto frontier, 20+ languages. Provides dense vs MoE architectural\n    contrast.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: failed\n  metrics:\n    bug: layer_config_mismatch\n    detail: extract_activations.py used --layers 2,6,10,14,18,22,26 but train_probe.py\n      and transfer_eval.py used default layers 0,4,8,12,16,20,24,28,31. Probe training\n      skipped all layers (activation files not found). Activations (42 files) are\n      valid and reusable.\n    fix: Add --layers 2,6,10,14,18,22,26 to train_probe.py and transfer_eval.py in\n      run_mvp_002.sh\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: RUNNING\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    bug: layer_config_mismatch\n    detail: extract_activations.py used --layers 2,6,10,14,18,22,26 but train_probe.py\n      and transfer_eval.py used default layers 0,4,8,12,16,20,24,28,31. Probe training\n      skipped all layers (activation files not found). Activations (42 files) are\n      valid and reusable.\n    fix: Add --layers 2,6,10,14,18,22,26 to train_probe.py and transfer_eval.py in\n      run_mvp_002.sh\n- exp_id: mvp_003\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T18:58:10.765Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T18:58:10.765Z",
  "sessionId": "8c3e7e33-f999-45e6-9b77-c8618fc951cb"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T18:58:10.798Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：All 4 claims fully validated at scale. Pareto frontier is crisp and architecture-consistent, decomposition cleanly separates, CaCLR decisively outperforms linear projection, orthogonality generalizes. Paper runs original framing with no claim adjustments.
核心假设：['Pareto frontier (depth vs transferability tradeoff) replicates on both Qwen3-235B and Llama4 Scout with clear monotonic shape', 'CaCLR consistently outperforms linear projection — the consistency loss term provides genuine value beyond simple alignment', 'Difficulty-shared component accounts for majority of transferable signal; projecting it out isolates a clean capability-specific residual', 'Correctness-confidence orthogonality (cosine < 0.1) holds across all 20 languages and both architectures', 'Low-resource languages (sw, yo, ig) achieve usable zero-shot transfer (AUROC > 0.60)']
关键指标范围：{'en_auroc_best_layer': [0.8, 0.86], 'zs_transfer_auroc_mean_19lang': [0.71, 0.79], 'zs_transfer_drop_mean_pp': [5, 12], 'caclr_vs_linproj_auroc_delta_pp': [2.5, 5.0], 'caclr_ece_reduction_vs_tempcal_pct': [30, 50], 'pareto_depth_transfer_rank_corr': [0.75, 0.95], 'decomp_difficulty_var_explained_pct': [55, 80], 'orthogonality_cosine_mean': [0.02, 0.08], 'low_resource_zs_pass_rate': [0.8, 1.0], 'caclr_improvement_pass_rate': [0.85, 1.0], 'pareto_frontier_agreement_across_arch': [0.8, 1.0]}
叙事方向：Original framing stands: 'CaCLR shifts the cross-lingual calibration Pareto frontier.' All 4 claims form an unbroken causal chain — discovery → analysis → method → mechanism. Headline: CaCLR reduces non-EN ECE by 30-50% over temp scaling with zero target-language labels. Pareto frontier is the organizing principle, CaCLR is the actionable contribution, decomposition explains why it works, orthogonality explains why output-based methods can't.

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
tier: best
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
  "promptId": "dc67e84b-5cac-4b94-be37-5b628b771e0d",
  "type": "user",
  "uuid": "bd8ecc7b-b05e-45af-965c-f348e8e4e461",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8c3e7e33-f999-45e6-9b77-c8618fc951cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T18:58:10.797Z_

```json
{
  "parentUuid": "bd8ecc7b-b05e-45af-965c-f348e8e4e461",
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
  "uuid": "1919c65a-ceae-4616-a98c-a36dd0c59f29",
  "timestamp": "2026-05-20T18:58:10.797Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8c3e7e33-f999-45e6-9b77-c8618fc951cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T18:58:10.797Z_

```json
{
  "parentUuid": "1919c65a-ceae-4616-a98c-a36dd0c59f29",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f9ce3056-ff4d-4b0d-b384-97da37c48adc",
  "timestamp": "2026-05-20T18:58:10.797Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8c3e7e33-f999-45e6-9b77-c8618fc951cb",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：All 4 claims fully validated at scale. Pareto frontier is crisp and architecture-consistent, decomposition cleanly separates, CaCLR decisively outperforms…",
  "leafUuid": "f9ce3056-ff4d-4b0d-b384-97da37c48adc",
  "sessionId": "8c3e7e33-f999-45e6-9b77-c8618fc951cb"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "CaCLR cross-lingual calibration phase 1 full validation",
  "sessionId": "8c3e7e33-f999-45e6-9b77-c8618fc951cb"
}
```

---

### Assistant

_source line 8 · 2026-05-20T18:58:25.645Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined/predicted experimental results for all "planned" experiments in the experiment plan, under the "best" tier definition. Each prediction needs a result_rationale explaining why this tier would produce these results.

Let me carefully go through each planned experiment and generate realistic, detailed predictions consistent with the "best" tier metrics.

The key metrics ranges for "best" tier:
- en_auroc_best_layer: [0.8, 0.86]
- zs_transfer_auroc_mean_19lang: [0.71, 0.79]


- zs_transfer_drop_mean_pp: [5, 12]
- caclr_vs_linproj_auroc_delta_pp: [2.5, 5.0]
- caclr_ece_reduction_vs_tempcal_pct: [30, 50]
- pareto_depth_transfer_rank_corr: [0.75, 0.95]
- decomp_difficulty_var_explained_pct: [55, 80]
- orthogonality_cosine_mean: [0.02, 0.08]
- low_resource_zs_pass

_rate: [0.8, 1.0]
- caclr_improvement_pass_rate: [0.85, 1.0]
- pareto_frontier_agreement_across_arch: [0.8, 1.0]

Now I'm looking at the planned experiments spanning Pareto frontier analysis across different model architectures, CaCLR implementation and evaluation, difficulty-controlled ablations, cross-lingual orthogonality studies, and extended benchmark coverage including INT8 validation and camera-ready results.

I need to generate detailed predictions for each experiment, grounding them in the MVP baseline where Qwen2.5-7B achieved an en_best_auroc of 0.7541. Scaling up to much larger models like Qwen3-235B and Llama4 Scout should yield substantially better probing accuracy, pushing toward the 0.8-0.86 range I'm targeting.

Writing the full YAML predictions...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9ce3056-ff4d-4b0d-b384-97da37c48adc",
  "isSidechain": false,
  "requestId": "req_011CbELHSfYb91id8ucpnrR5",
  "type": "assistant",
  "uuid": "31f92f31-e2fc-4b8d-9031-f9e8a43b0351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8c3e7e33-f999-45e6-9b77-c8618fc951cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCAUFNtiY1KaJsZMXGrw6m",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10771,
      "cache_read_input_tokens": 11841,
      "output_tokens": 13831,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10771,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 13831,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10771
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

_source line 9 · 2026-05-20T19:02:13.992Z_

```yaml
tier: best
narrative_guidance: >
  Original framing stands: "CaCLR shifts the cross-lingual calibration Pareto frontier."
  All 4 claims form an unbroken causal chain — discovery → analysis → method → mechanism.
  Headline: CaCLR reduces non-EN ECE by 30-50% over temp scaling with zero target-language labels.
  Pareto frontier is the organizing principle, CaCLR is the actionable contribution,
  decomposition explains why it works, orthogonality explains why output-based methods can't.

imagined_experiments:
  - name: "Full Pareto Frontier — Qwen3-235B-A22B"
    plan_id: "plan_001"
    description: >
      Extract activations at every 4th layer (24 probed layers out of 94), 20 languages,
      train English correctness probes (logistic regression + 2-layer MLP), evaluate
      5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).
    expected_results:
      en_auroc_best_layer: 0.843
      en_best_layer_idx: 72  # ~77% depth
      en_auroc_range: [0.621, 0.843]
      en_ece_raw_best: 0.162
      en_ece_tempcal_best: 0.054
      temp_scaling_T: 4.87
      zs_transfer_auroc_mean_19lang_best_transfer_layer: 0.762
      zs_best_transfer_layer_idx: 56  # ~60% depth, shallower than EN-optimal
      zs_transfer_drop_from_en_mean_pp: 8.1
      zs_auroc_by_tier:
        high_resource_mean: 0.791  # zh, de, fr, es, ja, ru, pt, it
        mid_resource_mean: 0.754   # ar, hi, ko, vi, th, bn, tr, nl
        low_resource_mean: 0.683   # sw, yo, ig
      zs_auroc_by_lang:
        en: 0.843
        zh: 0.802
        de: 0.796
        fr: 0.793
        es: 0.789
        ja: 0.785
        ru: 0.782
        pt: 0.788
        it: 0.786
        ar: 0.768
        hi: 0.761
        ko: 0.755
        vi: 0.749
        th: 0.743
        bn: 0.738
        tr: 0.756
        nl: 0.790
        sw: 0.695
        yo: 0.672
        ig: 0.681
      mean_shift_improvement_count: 2  # out of 19; mean-shift still mostly fails
      mean_shift_delta_ece_mean: 1.41  # slightly positive = slightly hurts
      linproj_auroc_mean_19lang: 0.724
      fewshot_25_auroc_mean_19lang: 0.748
      fewshot_100_auroc_mean_19lang: 0.771
      pareto_depth_transfer_rank_corr: 0.88
      pareto_frontier_layers: [40, 44, 48, 52, 56, 60]  # 6 layers on Pareto front
      layers_above_0p5_auroc_count: 22  # nearly all probed layers informative
    result_rationale: >
      Qwen3-235B-A22B is a 94-layer MoE with massive representation capacity. The jump
      from MVP's 7B (en AUROC 0.754) to 235B is expected to yield ~9pp AUROC gain,
      consistent with prior probing literature showing log-linear scaling of linear probe
      accuracy with model parameters (Burns et al., Marks et al.). The MoE architecture
      concentrates expert representations, producing cleaner correctness signals in
      intermediate layers. The Pareto frontier emerges because deeper layers (L72+)
      specialize for English-dominant pretraining data distribution — the model's
      language-specific processing intensifies past ~75% depth, degrading cross-lingual
      invariance. The best transfer layer (L56, ~60% depth) sits in the "universal
      reasoning" zone before language-specific heads activate. Low-resource languages
      (sw, yo, ig) still transfer above 0.65 AUROC because GlobalMMLU questions share
      structural patterns that even underrepresented languages partially align with in
      middle layers. Mean-shift continues to mostly fail because correctness directions
      are not simply mean-offset between languages — they require rotation, not translation,
      which linear projection and CaCLR address.
    tables:
      - name: "Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by Layer"
        columns: [layer_idx, layer_depth_pct, en_auroc, zs_mean_auroc_19, zs_drop_pp, on_pareto]
        rows:
          - [4, 4, 0.621, 0.608, 1.3, false]
          - [8, 9, 0.648, 0.637, 1.1, false]
          - [12, 13, 0.689, 0.671, 1.8, false]
          - [16, 17, 0.712, 0.698, 1.4, false]
          - [20, 21, 0.738, 0.724, 1.4, false]
          - [24, 26, 0.756, 0.742, 1.4, false]
          - [28, 30, 0.771, 0.755, 1.6, false]
          - [32, 34, 0.784, 0.764, 2.0, false]
          - [36, 38, 0.795, 0.771, 2.4, false]
          - [40, 43, 0.803, 0.776, 2.7, true]
          - [44, 47, 0.810, 0.774, 3.6, true]
          - [48, 51, 0.816, 0.770, 4.6, true]
          - [52, 55, 0.822, 0.765, 5.7, true]
          - [56, 60, 0.827, 0.762, 6.5, true]
          - [60, 64, 0.831, 0.753, 7.8, true]
          - [64, 68, 0.835, 0.741, 9.4, false]
          - [68, 72, 0.839, 0.728, 11.1, false]
          - [72, 77, 0.843, 0.712, 13.1, false]
          - [76, 81, 0.841, 0.694, 14.7, false]
          - [80, 85, 0.838, 0.671, 16.7, false]
          - [84, 89, 0.832, 0.643, 18.9, false]
          - [88, 94, 0.819, 0.611, 20.8, false]
          - [92, 98, 0.791, 0.574, 21.7, false]
          - [94, 100, 0.762, 0.541, 22.1, false]
      - name: "Table 2: Transfer Condition Comparison (at best-transfer layer L56)"
        columns: [condition, auroc_mean_19, ece_mean_19, ece_reduction_vs_tempcal_pct]
        rows:
          - [zero-shot, 0.762, 0.098, 0]
          - [mean-shift, 0.758, 0.101, -3.1]
          - [linear_projection, 0.781, 0.082, 16.3]
          - [few-shot-25, 0.748, 0.089, 9.2]
          - [few-shot-100, 0.771, 0.079, 19.4]
          - [CaCLR, 0.814, 0.058, 40.8]
    figures_description:
      - "Figure 1a: Pareto frontier scatter plot (EN AUROC x-axis vs ZS mean AUROC y-axis), each point a layer, Pareto-optimal layers highlighted in red. Clear convex frontier shape from L40-L60."
      - "Figure 1b: Heatmap of ZS AUROC by language (y-axis, ordered by resource tier) × layer depth (x-axis). Shows warm band in mid-layers, cooling at extremes, with low-resource langs cooling earlier."
    analysis: >
      The Pareto frontier is crisp and monotonic: 6 layers form the efficient frontier
      between L40-L60. The rank correlation (Spearman) between layer depth and transfer
      degradation is ρ=0.88 (p<0.001). The frontier's shape confirms that the depth-
      transferability tradeoff is not an artifact of small models — it amplifies at scale.
      The 16pp gap between best-EN layer (L72) and best-transfer layer (L56) is larger
      than MVP's ~3-layer gap, consistent with deeper models having more room for
      language-specific specialization. All high-resource languages pass AUROC > 0.75
      at the best-transfer layer; all low-resource languages exceed 0.65.

  - name: "Full Pareto Frontier — Llama 4 Scout"
    plan_id: "plan_002"
    description: >
      Extract activations at every 4th layer (12 probed layers out of 48), 20 languages,
      5 transfer conditions. INT8 weight quantization.
    expected_results:
      en_auroc_best_layer: 0.821
      en_best_layer_idx: 36  # 75% depth
      en_auroc_range: [0.634, 0.821]
      en_ece_raw_best: 0.174
      en_ece_tempcal_best: 0.061
      temp_scaling_T: 5.34
      zs_transfer_auroc_mean_19lang_best_transfer_layer: 0.741
      zs_best_transfer_layer_idx: 28  # ~58% depth
      zs_transfer_drop_from_en_mean_pp: 8.0
      zs_auroc_by_tier:
        high_resource_mean: 0.771
        mid_resource_mean: 0.733
        low_resource_mean: 0.661
      zs_auroc_by_lang:
        en: 0.821
        zh: 0.784
        de: 0.778
        fr: 0.775
        es: 0.771
        ja: 0.766
        ru: 0.762
        pt: 0.770
        it: 0.768
        ar: 0.748
        hi: 0.741
        ko: 0.735
        vi: 0.729
        th: 0.722
        bn: 0.718
        tr: 0.737
        nl: 0.772
        sw: 0.674
        yo: 0.641
        ig: 0.667
      mean_shift_improvement_count: 1
      linproj_auroc_mean_19lang: 0.706
      fewshot_25_auroc_mean_19lang: 0.728
      fewshot_100_auroc_mean_19lang: 0.752
      pareto_depth_transfer_rank_corr: 0.82
      pareto_frontier_layers: [20, 24, 28, 32]
    result_rationale: >
      Llama 4 Scout has 48 layers (fewer than Qwen3's 94) and a different MoE routing
      strategy (16 experts, top-2). With roughly 109B total / ~17B active params, its
      active compute is smaller than Qwen3-235B's ~22B active. This yields ~2pp lower
      EN AUROC and ~2pp lower transfer AUROC. The Pareto frontier has fewer points (4
      vs 6) due to coarser layer sampling (every 4th of 48 = 12 points), but the
      monotonic depth-transfer tradeoff still holds clearly. Llama 4 Scout's best
      transfer layer sits at ~58% depth (L28), remarkably close to Qwen3's 60%, suggesting
      a universal "mid-depth transfer zone" across architectures. The rank correlation is
      slightly lower (0.82 vs 0.88) due to fewer data points but still highly significant.
      Low-resource languages are slightly weaker because Meta's multilingual pretraining
      mix underrepresents African languages compared to Qwen3.
    tables:
      - name: "Table 3: Llama 4 Scout Pareto Frontier"
        columns: [layer_idx, layer_depth_pct, en_auroc, zs_mean_auroc_19, zs_drop_pp, on_pareto]
        rows:
          - [4, 8, 0.634, 0.624, 1.0, false]
          - [8, 17, 0.672, 0.659, 1.3, false]
          - [12, 25, 0.714, 0.699, 1.5, false]
          - [16, 33, 0.745, 0.729, 1.6, false]
          - [20, 42, 0.768, 0.748, 2.0, true]
          - [24, 50, 0.786, 0.745, 4.1, true]
          - [28, 58, 0.798, 0.741, 5.7, true]
          - [32, 67, 0.810, 0.732, 7.8, true]
          - [36, 75, 0.821, 0.714, 10.7, false]
          - [40, 83, 0.818, 0.689, 12.9, false]
          - [44, 92, 0.804, 0.651, 15.3, false]
          - [48, 100, 0.771, 0.608, 16.3, false]
      - name: "Table 4: Cross-Architecture Pareto Frontier Agreement"
        columns: [metric, qwen3_235b, llama4_scout, agreement]
        rows:
          - [best_en_layer_depth_pct, 77, 75, "within 2pp"]
          - [best_transfer_layer_depth_pct, 60, 58, "within 2pp"]
          - [pareto_zone_depth_range_pct, "43-64", "42-67", "overlapping"]
          - [depth_transfer_rank_corr, 0.88, 0.82, "both >0.75"]
          - [frontier_shape, "convex monotonic", "convex monotonic", "consistent"]
    figures_description:
      - "Figure 2: Overlaid Pareto frontiers for both architectures (normalized depth %). Shows near-identical frontier shapes with Qwen3 shifted up-right (better overall) but same curvature."
    analysis: >
      Cross-architecture agreement is high: both models show best transfer at ~59% depth,
      the Pareto frontier occupies the 42-67% depth band, and the rank correlation between
      depth and transfer degradation exceeds 0.75 in both. The frontier shape is
      architecture-invariant — it's the depth-normalized position, not absolute layer
      count, that determines the tradeoff. This validates Claim 1 at scale.

  - name: "CaCLR Implementation and Comparative Evaluation"
    plan_id: "plan_003"
    description: >
      CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) implementation. Train on English
      labels + unlabeled parallel activations. Compare vs all 5 conditions across full
      Pareto frontier, both models × 20 languages. Hyperparameter tuning (α, β).
    expected_results:
      best_alpha: 0.15
      best_beta: 0.08
      # Qwen3-235B results
      qwen3_caclr_auroc_mean_19lang: 0.814
      qwen3_caclr_ece_mean_19lang: 0.058
      qwen3_caclr_vs_linproj_auroc_delta_pp: 3.3
      qwen3_caclr_vs_zeroshot_auroc_delta_pp: 5.2
      qwen3_caclr_ece_reduction_vs_tempcal_pct: 40.8
      qwen3_caclr_best_operating_layer: 64  # deeper than ZS-best (56), closer to EN-best (72)
      # Llama 4 Scout results
      llama4_caclr_auroc_mean_19lang: 0.793
      llama4_caclr_ece_mean_19lang: 0.064
      llama4_caclr_vs_linproj_auroc_delta_pp: 3.1
      llama4_caclr_vs_zeroshot_auroc_delta_pp: 5.2
      llama4_caclr_ece_reduction_vs_tempcal_pct: 38.5
      llama4_caclr_best_operating_layer: 32
      # Aggregate
      caclr_vs_linproj_auroc_delta_pp_mean: 3.2
      caclr_ece_reduction_vs_tempcal_pct_mean: 39.7
      caclr_improvement_pass_rate: 0.92  # 35/38 model-lang pairs improved vs linproj
      caclr_pareto_shift_layers: 2  # CaCLR-optimal layer is ~2 layers deeper than ZS-optimal
      low_resource_caclr_auroc:
        sw_qwen3: 0.731
        yo_qwen3: 0.709
        ig_qwen3: 0.718
        sw_llama4: 0.712
        yo_llama4: 0.681
        ig_llama4: 0.698
      low_resource_zs_pass_rate: 1.0  # all 6 low-resource × model pairs > 0.60 AUROC
    result_rationale: >
      CaCLR's consistency loss (β·L_consistency) directly penalizes divergence between
      EN and non-EN probe outputs on parallel/comparable activations, forcing the probe
      to learn language-invariant features. This is strictly more informative than linear
      projection (which only aligns means and covariances post-hoc) because it shapes
      the learned representation during training. The 3.2pp AUROC gain over linear
      projection reflects the value of end-to-end optimization: linear projection
      corrects first-order distributional mismatch but not the nonlinear feature
      interactions that L_consistency captures. The SB-ECE term (α·L_SB-ECE) provides
      calibration-aware training that temperature scaling cannot — it directly optimizes
      the calibration objective rather than post-hoc rescaling. The 40% ECE reduction
      over temperature scaling arises because CaCLR addresses the root cause (representation
      misalignment) rather than the symptom (miscalibrated probabilities). The Pareto
      frontier shift is the key result: CaCLR allows operating 2 layers deeper than the
      ZS-optimal point while maintaining equivalent or better transfer — it literally
      pushes the Pareto frontier outward. Low-resource languages benefit most from
      L_consistency because their activation distributions are most misaligned from EN;
      the consistency term provides the strongest gradient signal precisely where the
      gap is largest.
    tables:
      - name: "Table 5: CaCLR vs Baselines — Full Comparison (averaged across both architectures)"
        columns: [method, auroc_mean_19, ece_mean_19, requires_target_labels, params_overhead]
        rows:
          - [zero-shot, 0.752, 0.098, "no", "0"]
          - [mean-shift, 0.747, 0.102, "no", "0"]
          - [linear_projection, 0.770, 0.082, "no", "d×d matrix"]
          - [few-shot-25, 0.738, 0.089, "yes (25)", "0"]
          - [few-shot-100, 0.762, 0.079, "yes (100)", "0"]
          - [CaCLR, 0.804, 0.061, "no", "~1% probe params"]
      - name: "Table 6: CaCLR Ablation — Loss Component Contributions"
        columns: [configuration, auroc_mean_19, ece_mean_19, delta_vs_full_auroc_pp]
        rows:
          - [L_BCE_only (= zero-shot probe), 0.752, 0.098, -5.2]
          - [L_BCE + L_SB-ECE, 0.768, 0.072, -3.6]
          - [L_BCE + L_consistency, 0.793, 0.078, -1.1]
          - [L_BCE + L_SB-ECE + L_consistency (full CaCLR), 0.804, 0.061, 0.0]
      - name: "Table 7: CaCLR Pareto Frontier Shift (Qwen3-235B)"
        columns: [layer_idx, zs_auroc_19, caclr_auroc_19, shift_pp, on_shifted_pareto]
        rows:
          - [40, 0.776, 0.798, 2.2, false]
          - [44, 0.774, 0.800, 2.6, false]
          - [48, 0.770, 0.803, 3.3, true]
          - [52, 0.765, 0.806, 4.1, true]
          - [56, 0.762, 0.810, 4.8, true]
          - [60, 0.753, 0.814, 6.1, true]
          - [64, 0.741, 0.814, 7.3, true]
          - [68, 0.728, 0.808, 8.0, true]
          - [72, 0.712, 0.796, 8.4, false]
    figures_description:
      - "Figure 3: Pareto frontier before/after CaCLR. ZS frontier (blue) vs CaCLR frontier (red), showing outward shift. CaCLR's optimal operating point is 2 layers deeper with +5pp transfer AUROC."
      - "Figure 4: Per-language AUROC improvement from CaCLR over linear projection, grouped by resource tier. Low-resource languages show largest gains (4-6pp), high-resource 2-3pp."
      - "Figure 5: Loss component ablation bar chart — stacked contributions of L_SB-ECE and L_consistency to final AUROC and ECE improvements."
    analysis: >
      CaCLR decisively outperforms all baselines. The ablation shows both loss terms
      contribute: L_consistency provides the bulk of AUROC improvement (+4.1pp alone),
      while L_SB-ECE provides calibration refinement (ECE drops from 0.078 to 0.061
      when added). The interaction is synergistic — joint optimization yields better
      results than either term alone. The Pareto shift is the headline result: at the
      same EN calibration quality (L64, AUROC 0.835), CaCLR achieves 0.814 transfer
      vs 0.741 zero-shot — a 7.3pp improvement. This shifts the practical recommendation
      from "use shallower layers for transfer" to "use CaCLR and operate at deeper,
      better-calibrated layers." The improvement pass rate of 92% (35/38 model-lang
      pairs) demonstrates consistency. The 3 non-improving pairs are high-resource
      languages (fr, nl, de on Llama 4 Scout) where zero-shot transfer is already
      excellent and the consistency loss has minimal signal to exploit.

  - name: "Difficulty-Controlled Ablation"
    plan_id: "plan_004"
    description: >
      IRT difficulty probes (Ridge regression), project out difficulty direction, retrain
      correctness probes on residuals, evaluate transfer. 10 languages × 8 layers per model.
    expected_results:
      difficulty_probe_r2_mean: 0.72
      difficulty_var_explained_pct_mean: 68.4
      difficulty_var_explained_pct_range: [58.2, 79.1]
      # After projecting out difficulty
      residual_en_auroc_drop_pp: 4.2  # EN probe loses some predictive power
      residual_zs_transfer_drop_pp: 1.1  # but transfer barely changes
      capability_specific_var_pct: 31.6
      capability_specific_transfer_degradation_pct: 87  # most of the transfer drop is here
      difficulty_component_transfer_degradation_pct: 13
      decomp_prescriptive_accuracy: 0.81  # predicts correct alignment strategy 81% of time
      # By depth
      difficulty_var_by_depth:
        shallow_20pct: 0.74
        mid_50pct: 0.69
        deep_80pct: 0.62
      capability_transfer_drop_by_depth:
        shallow_20pct: 0.8  # pp drop
        mid_50pct: 3.4
        deep_80pct: 9.7
    result_rationale: >
      IRT difficulty is a strong, language-agnostic property — harder questions are harder
      everywhere. Ridge regression captures this cleanly (R²=0.72) because difficulty
      is linearly encoded in intermediate representations (Civelli et al. confirmed this).
      The difficulty component accounts for 68% of explained variance because GlobalMMLU
      correctness is heavily driven by item difficulty: a model gets easy questions right
      in all languages and hard questions wrong in all languages. After projecting out
      difficulty, the residual correctness signal is "capability-specific" — it captures
      language-dependent competence differences. This residual transfers poorly at deep
      layers (9.7pp drop at 80% depth vs 0.8pp at 20% depth) because deep layers encode
      language-specific processing that makes capability assessments non-transferable.
      The difficulty component transfers well at all depths (only 13% of total transfer
      degradation) because it's language-invariant by construction. This decomposition
      is prescriptive: when difficulty explains most of a language's correctness variance,
      simple zero-shot transfer suffices; when the capability residual is large, CaCLR
      is needed. The 81% prescriptive accuracy validates the decomposition as more than
      descriptive.
    tables:
      - name: "Table 8: Decomposition Results — Difficulty vs Capability Components"
        columns: [component, var_explained_pct, transfer_auroc_mean, transfer_drop_from_en_pp, share_of_total_transfer_drop_pct]
        rows:
          - [full_correctness, 100, 0.752, 8.1, 100]
          - [difficulty_shared, 68.4, 0.738, 1.1, 13]
          - [capability_specific, 31.6, 0.614, 14.2, 87]
      - name: "Table 9: Capability-Specific Transfer Drop by Depth"
        columns: [depth_band, difficulty_transfer_drop_pp, capability_transfer_drop_pp, ratio]
        rows:
          - ["0-30%", 0.3, 0.8, "2.7×"]
          - ["30-60%", 0.8, 3.4, "4.3×"]
          - ["60-90%", 1.6, 9.7, "6.1×"]
    figures_description:
      - "Figure 6: Stacked area chart showing difficulty vs capability variance across depth. Difficulty dominates at all depths but capability grows at deeper layers."
      - "Figure 7: Transfer degradation decomposed into difficulty (flat, near-zero) and capability (exponentially increasing with depth) components."
    analysis: >
      The decomposition cleanly separates: difficulty-shared signal is the majority (68%)
      of correctness variance and transfers near-perfectly across languages and depths.
      The capability-specific residual (32%) drives nearly all transfer degradation (87%),
      and this degradation accelerates exponentially with depth. This explains the Pareto
      frontier mechanistically: deeper layers have stronger capability-specific signals
      that improve EN calibration but impede transfer. CaCLR works because its consistency
      loss specifically targets the capability-specific component — forcing alignment of
      the non-difficulty residual across languages. The prescriptive value (81% accuracy
      in predicting when CaCLR is needed) confirms this is a load-bearing decomposition,
      not a post-hoc narrative.

  - name: "Cross-Lingual Orthogonality Analysis"
    plan_id: "plan_005"
    description: >
      Extract verbalized confidence direction via prompted confidence scores, compute
      cosine similarity with correctness direction across 20 languages × 2 architectures.
      Analyze by resource tier and language family.
    expected_results:
      orthogonality_cosine_mean_overall: 0.052
      orthogonality_cosine_range: [0.018, 0.094]
      orthogonality_cosine_en: 0.034
      # By architecture
      qwen3_cosine_mean: 0.048
      llama4_cosine_mean: 0.057
      # By resource tier
      high_resource_cosine_mean: 0.041
      mid_resource_cosine_mean: 0.054
      low_resource_cosine_mean: 0.074
      # Notable individual languages
      cosine_by_lang:
        en: 0.034
        zh: 0.038
        de: 0.036
        fr: 0.039
        es: 0.041
        ja: 0.044
        ru: 0.043
        pt: 0.040
        it: 0.042
        ar: 0.051
        hi: 0.055
        ko: 0.049
        vi: 0.058
        th: 0.061
        bn: 0.056
        tr: 0.052
        nl: 0.037
        sw: 0.078
        yo: 0.094
        ig: 0.082
      all_langs_below_0p1: true
      cosine_resource_tier_correlation: -0.68  # lower resource = higher cosine
    result_rationale: >
      Miao & Ungar (2026) established correctness-confidence orthogonality (cosine < 0.04)
      for English on 7-8B models. We extend to 20 languages on larger models. The
      orthogonality persists universally (all < 0.1) because it reflects a fundamental
      architectural property: verbalized confidence is generated by the language modeling
      head from surface-level token probabilities, while correctness is encoded in
      intermediate representation geometry. These are structurally decoupled in
      transformer architectures. The slight increase in cosine for low-resource languages
      (0.074 mean vs 0.041 for high-resource) occurs because low-resource languages have
      noisier confidence elicitation — the model's verbalized confidence in Yoruba is
      less well-calibrated and leaks some correctness signal, producing weak correlation.
      The resource-tier gradient (ρ=-0.68) suggests that better multilingual training
      data produces cleaner separation between correctness and confidence representations.
      The cross-architecture consistency (Qwen3: 0.048, Llama4: 0.057) confirms this is
      not architecture-specific. Llama 4's slightly higher cosines may reflect its
      less aggressive multilingual pretraining compared to Qwen3.
    tables:
      - name: "Table 10: Correctness-Confidence Cosine Similarity by Language and Architecture"
        columns: [language, resource_tier, qwen3_cosine, llama4_cosine, mean_cosine]
        rows:
          - [en, high, 0.031, 0.037, 0.034]
          - [zh, high, 0.035, 0.041, 0.038]
          - [de, high, 0.033, 0.039, 0.036]
          - [fr, high, 0.036, 0.042, 0.039]
          - [es, high, 0.038, 0.044, 0.041]
          - [ja, high, 0.041, 0.047, 0.044]
          - [ru, high, 0.040, 0.046, 0.043]
          - [pt, high, 0.037, 0.043, 0.040]
          - [it, high, 0.039, 0.045, 0.042]
          - [nl, high, 0.034, 0.040, 0.037]
          - [ar, mid, 0.047, 0.055, 0.051]
          - [hi, mid, 0.051, 0.059, 0.055]
          - [ko, mid, 0.045, 0.053, 0.049]
          - [vi, mid, 0.054, 0.062, 0.058]
          - [th, mid, 0.057, 0.065, 0.061]
          - [bn, mid, 0.052, 0.060, 0.056]
          - [tr, mid, 0.048, 0.056, 0.052]
          - [sw, low, 0.073, 0.083, 0.078]
          - [yo, low, 0.089, 0.099, 0.094]
          - [ig, low, 0.077, 0.087, 0.082]
      - name: "Table 11: Orthogonality Summary Statistics"
        columns: [statistic, qwen3_235b, llama4_scout, both_models]
        rows:
          - [cosine_mean, 0.048, 0.057, 0.052]
          - [cosine_std, 0.015, 0.017, 0.016]
          - [cosine_max, 0.089, 0.099, 0.094]
          - [cosine_min, 0.031, 0.037, 0.018]
          - [all_below_0.1, "yes (20/20)", "yes (19/20)", "39/40"]
          - [resource_tier_corr, -0.71, -0.65, -0.68]
    figures_description:
      - "Figure 8: Cosine similarity violin plots by resource tier, showing clear gradient from high (tight around 0.04) to low (spread around 0.08). All below 0.1 threshold."
      - "Figure 9: Scatter plot of cosine similarity vs language resource level (log wiki size), colored by architecture. Strong negative trend."
    analysis: >
      Orthogonality generalizes comprehensively. The mean cosine of 0.052 across all 40
      language-architecture pairs is well within the "near-orthogonal" regime (< 0.1).
      The resource-tier gradient is the novel finding: it suggests that output-based
      calibration methods are not just structurally limited but are *more* limited for
      well-resourced languages where the orthogonality is strongest. This strengthens
      the motivation for probe-based approaches universally and for CaCLR specifically
      in multilingual settings. Yoruba's 0.094 is the only value approaching the 0.1
      threshold (on Llama4 it hits 0.099), which is worth noting but does not break the
      claim.

  - name: "Probe Complexity Comparison"
    plan_id: "plan_006"
    description: >
      Logistic regression vs 2-layer MLP at each probed layer, both models. Compare
      English accuracy, cross-lingual transfer degradation, calibration quality.
    expected_results:
      # English AUROC
      logreg_en_auroc_best: 0.843  # Qwen3 best
      mlp_en_auroc_best: 0.856
      mlp_en_auroc_gain_pp: 1.3
      # Transfer
      logreg_zs_transfer_drop_mean_pp: 8.1
      mlp_zs_transfer_drop_mean_pp: 12.4
      transfer_degradation_ratio: 1.53  # MLP transfers 53% worse
      # Calibration
      logreg_ece_mean: 0.054
      mlp_ece_mean: 0.068
      # Interaction with depth
      logreg_transfer_advantage_shallow_pp: 2.1
      logreg_transfer_advantage_deep_pp: 6.8
    result_rationale: >
      Linear probes transfer better because they learn a single hyperplane in activation
      space — the hyperplane generalizes across languages when the underlying geometry is
      approximately shared (as it is in mid-depth layers). MLPs learn nonlinear decision
      boundaries that fit English-specific feature interactions, gaining ~1.3pp EN AUROC
      but losing ~4.3pp in transfer. The transfer gap widens at deeper layers (6.8pp
      advantage for logreg) because deep layers have more language-specific nonlinear
      structure that MLPs exploit but logreg ignores. This justifies our choice of linear
      probes for the main results and supports the geometric interpretation of the Pareto
      frontier: it's about linear subspace alignment, not complex feature interactions.
    tables:
      - name: "Table 12: Probe Complexity Comparison"
        columns: [probe_type, en_auroc_best, zs_auroc_mean_19, zs_drop_pp, ece_mean_19]
        rows:
          - [logistic_regression, 0.843, 0.762, 8.1, 0.054]
          - [mlp_2layer, 0.856, 0.733, 12.4, 0.068]
    figures_description:
      - "Figure S1 (supplementary): Transfer drop (pp) vs layer depth for both probe types. MLP line diverges sharply from logreg at deep layers."
    analysis: >
      Linear probes are the correct choice for cross-lingual transfer: they sacrifice 1.3pp
      EN AUROC but gain 4.3pp average transfer. The depth interaction effect is notable —
      the logreg advantage grows from 2.1pp at shallow layers to 6.8pp at deep layers,
      confirming that deep-layer transfer degradation is driven by nonlinear, language-
      specific features. CaCLR + logreg is thus the optimal configuration.

  - name: "Additional Benchmark Evaluation (Belebele + MMLU-ProX)"
    plan_id: "plan_007"
    description: >
      Evaluate best probes + CaCLR on Belebele (20 languages) and MMLU-ProX (20 languages).
    expected_results:
      # Belebele (reading comprehension MCQA)
      belebele_zs_auroc_mean_19: 0.738
      belebele_caclr_auroc_mean_19: 0.789
      belebele_caclr_vs_zs_pp: 5.1
      belebele_ece_reduction_vs_tempcal_pct: 36.2
      # MMLU-ProX (harder questions)
      mmlupx_zs_auroc_mean_19: 0.722
      mmlupx_caclr_auroc_mean_19: 0.774
      mmlupx_caclr_vs_zs_pp: 5.2
      mmlupx_ece_reduction_vs_tempcal_pct: 33.8
      # Cross-benchmark consistency
      caclr_benefit_cross_benchmark_cv: 0.08  # low coefficient of variation
    result_rationale: >
      Belebele tests reading comprehension (vs GlobalMMLU's factual knowledge), providing
      domain generalization evidence. Transfer AUROC is slightly lower (0.738 vs 0.762)
      because Belebele's passage-dependent questions have weaker difficulty-shared signal —
      comprehension difficulty is more language-dependent than factual difficulty. CaCLR
      still provides ~5pp improvement, confirming the consistency loss generalizes beyond
      factual MCQA. MMLU-ProX has harder questions that compress the AUROC distribution
      (lower base rate of correctness), yielding slightly lower absolute numbers but
      comparable CaCLR benefit. The cross-benchmark CV of 0.08 for CaCLR improvement
      confirms the method is robust to evaluation domain.
    tables:
      - name: "Table 13: Cross-Benchmark Generalization"
        columns: [benchmark, zs_auroc_mean_19, caclr_auroc_mean_19, caclr_gain_pp, ece_reduction_pct]
        rows:
          - [GlobalMMLU, 0.752, 0.804, 5.2, 39.7]
          - [Belebele, 0.738, 0.789, 5.1, 36.2]
          - [MMLU-ProX, 0.722, 0.774, 5.2, 33.8]
    figures_description:
      - "Figure S2: CaCLR improvement (pp) by benchmark × language, showing consistent gains across domains."
    analysis: >
      CaCLR generalizes cleanly across benchmarks. The improvement magnitude is remarkably
      stable (5.1-5.2pp AUROC, 33-40% ECE reduction), suggesting the method addresses
      a fundamental representation alignment issue rather than overfitting to GlobalMMLU-
      specific patterns. This is critical for reviewer confidence.

  - name: "INT8 Validation Ablation"
    plan_id: "plan_010"
    description: >
      Compare INT8 vs FP16 probing results at 5 representative layers for Llama 4 Scout
      on 5% random subset.
    expected_results:
      int8_fp16_auroc_diff_mean_pp: 0.3
      int8_fp16_auroc_diff_max_pp: 0.7
      int8_fp16_ece_diff_mean_pp: 0.2
      int8_fp16_transfer_drop_diff_pp: 0.4
      int8_fp16_rank_correlation: 0.997
      conclusion: "INT8 quantization introduces negligible distortion"
    result_rationale: >
      INT8 weight-only quantization preserves the 8 most significant bits of each weight,
      introducing per-channel quantization noise of ~0.4% relative magnitude. Correctness
      probing relies on the geometry of activation space (direction of correctness signal),
      not absolute magnitudes. The quantization noise is approximately isotropic and
      thus preserves angular relationships between directions. The 0.3pp mean AUROC
      difference is within random seed variance, and the rank correlation of 0.997
      between INT8 and FP16 layer rankings confirms that the Pareto frontier shape is
      unaffected. This result is expected given prior work showing that probing results
      are robust to quantization down to INT4 (Gao et al., 2024).
    tables:
      - name: "Table S1: INT8 vs FP16 Comparison (Llama 4 Scout, 5% subset)"
        columns: [layer_idx, fp16_auroc, int8_auroc, diff_pp, fp16_zs_auroc_5lang, int8_zs_auroc_5lang, transfer_diff_pp]
        rows:
          - [8, 0.674, 0.672, 0.2, 0.661, 0.658, 0.3]
          - [16, 0.747, 0.745, 0.2, 0.731, 0.728, 0.3]
          - [24, 0.788, 0.786, 0.2, 0.747, 0.744, 0.3]
          - [32, 0.812, 0.810, 0.2, 0.734, 0.731, 0.3]
          - [40, 0.820, 0.817, 0.3, 0.691, 0.687, 0.4]
    figures_description:
      - "Figure S3: INT8 vs FP16 AUROC scatter plot at all tested layer-language combinations. Points fall tightly along y=x diagonal."
    analysis: >
      INT8 quantization is validated as safe for our experimental setup. The maximum
      observed difference (0.7pp at a single layer-language combination) is well within
      the noise floor of probing experiments. The Pareto frontier ordering is perfectly
      preserved (rank correlation 0.997). This ablation preempts reviewer concern #5.

  - name: "Gemma 4 31B Dense — Third Architecture (Camera-Ready)"
    plan_id: "plan_008"
    description: >
      Full Pareto frontier on Gemma 4 31B Dense (60 layers), 20+ languages. Provides
      dense vs MoE architectural contrast.
    expected_results:
      en_auroc_best_layer: 0.812
      en_best_layer_idx: 45  # 75% depth
      zs_transfer_auroc_mean_19lang: 0.734
      zs_best_transfer_layer_idx: 36  # 60% depth
      zs_transfer_drop_mean_pp: 7.8
      pareto_depth_transfer_rank_corr: 0.86
      caclr_auroc_mean_19lang: 0.786
      caclr_vs_linproj_auroc_delta_pp: 2.9
      dense_vs_moe_transfer_comparison: "comparable within 2pp"
      pareto_shape: "convex monotonic, consistent with MoE models"
    result_rationale: >
      Gemma 4 31B Dense has fewer total parameters than the MoE models but all are
      active, yielding comparable per-token compute. As a dense model, its representations
      are more uniformly distributed across layers (no expert routing), producing slightly
      smoother Pareto frontiers. The best-transfer depth (~60%) matches both MoE models,
      confirming this is a universal property of transformer depth, not MoE-specific.
      EN AUROC is slightly lower (0.812 vs 0.843/0.821) because 31B active params < 22B
      active with MoE routing benefits. CaCLR improvement is slightly lower (2.9pp) on
      the dense model because the absence of expert routing means less language-specific
      feature fragmentation to correct. This is the ideal third data point: different
      architecture family, consistent findings.
    tables:
      - name: "Table 14: Three-Architecture Summary"
        columns: [model, type, layers, en_auroc_best, zs_auroc_mean_19, best_transfer_depth_pct, pareto_rank_corr, caclr_gain_pp]
        rows:
          - [Qwen3-235B-A22B, MoE, 94, 0.843, 0.762, 60, 0.88, 3.3]
          - [Llama 4 Scout, MoE, 48, 0.821, 0.741, 58, 0.82, 3.1]
          - [Gemma 4 31B Dense, Dense, 60, 0.812, 0.734, 60, 0.86, 2.9]
    figures_description:
      - "Figure 10: Three-architecture Pareto frontiers overlaid (normalized depth). Remarkably similar shapes despite architectural differences."
    analysis: >
      The three-architecture comparison is the strongest evidence for the universality of
      the depth-transferability tradeoff. The best-transfer depth converges to 58-60%
      across dense and MoE architectures with 48-94 layers, CaCLR provides consistent
      2.9-3.3pp improvement, and the Pareto rank correlation is 0.82-0.88 in all cases.
      Dense vs MoE makes minimal difference — the phenomenon is a property of transformer
      depth, not routing architecture.

  - name: "Extended Language Coverage (Camera-Ready)"
    plan_id: "plan_009"
    description: >
      Expand from 20 to 50+ languages for camera-ready, leveraging GlobalMMLU/Belebele
      full language sets.
    expected_results:
      total_languages: 52
      new_languages_added: 32
      zs_auroc_above_0p60_count: 48  # out of 51 non-EN
      zs_auroc_below_0p55_count: 2   # extremely low-resource
      caclr_improvement_positive_count: 49  # out of 51
      mean_zs_auroc_51lang: 0.72
      mean_caclr_auroc_51lang: 0.77
      pareto_frontier_holds_all_langs: true
      new_language_families_covered: ["Austronesian", "Dravidian", "Niger-Congo B", "Uralic", "Kartvelian"]
    result_rationale: >
      Expanding to 50+ languages primarily adds mid-resource languages (Indonesian, Malay,
      Finnish, Georgian, Tamil, Telugu, etc.) where the model has moderate pretraining
      exposure. Most new languages fall in the 0.65-0.78 AUROC range, consistent with
      the mid-resource tier from the 20-language set. A handful of extremely low-resource
      languages (e.g., Amharic script languages with minimal pretraining data) may fall
      below 0.55, but these represent edge cases rather than systematic failures. CaCLR
      continues to improve 96% of languages because the consistency loss mechanism is
      language-agnostic — it aligns activation distributions without requiring any
      language-specific knowledge. The Pareto frontier structure is preserved across all
      52 languages, confirming it's a depth property, not a language-set artifact.
    tables:
      - name: "Table 15: Extended Language Coverage Summary by Resource Tier"
        columns: [tier, n_langs, zs_auroc_mean, caclr_auroc_mean, caclr_gain_pp, pct_above_0p60]
        rows:
          - [high, 12, 0.782, 0.812, 3.0, 100]
          - [mid, 25, 0.738, 0.784, 4.6, 100]
          - [low, 10, 0.661, 0.712, 5.1, 90]
          - [very_low, 4, 0.582, 0.638, 5.6, 50]
    figures_description:
      - "Figure 11: World map with per-language CaCLR AUROC, colored by performance tier. Demonstrates broad geographic and typological coverage."
    analysis: >
      The extension to 52 languages confirms all findings at broader scale. The resource-tier
      gradient is smooth and predictable — no language family shows anomalous behavior.
      CaCLR's benefit is inversely correlated with resource level (3.0pp for high-resource
      to 5.6pp for very-low-resource), confirming that the consistency loss provides most
      value where representation misalignment is worst. The 48/51 pass rate (>0.60 AUROC)
      for zero-shot CaCLR transfer with no target-language labels is the practical headline
      for camera-ready: usable cross-lingual calibration for the vast majority of languages.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31f92f31-e2fc-4b8d-9031-f9e8a43b0351",
  "isSidechain": false,
  "requestId": "req_011CbELHSfYb91id8ucpnrR5",
  "type": "assistant",
  "uuid": "fc21a0af-1e70-48a4-938d-4de7a2f5bef3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "8c3e7e33-f999-45e6-9b77-c8618fc951cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCAUFNtiY1KaJsZMXGrw6m",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10771,
      "cache_read_input_tokens": 11841,
      "output_tokens": 13831,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10771,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 13831,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10771
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：All 4 claims fully validated at scale. Pareto frontier is crisp and architecture-consistent, decomposition cleanly separates, CaCLR decisively outperforms…",
  "leafUuid": "fc21a0af-1e70-48a4-938d-4de7a2f5bef3",
  "sessionId": "8c3e7e33-f999-45e6-9b77-c8618fc951cb"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "CaCLR cross-lingual calibration phase 1 full validation",
  "sessionId": "8c3e7e33-f999-45e6-9b77-c8618fc951cb"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：All 4 claims fully validated at scale. Pareto frontier is crisp and architecture-consistent, decomposition cleanly separates, CaCLR decisively outperforms…",
  "leafUuid": "fc21a0af-1e70-48a4-938d-4de7a2f5bef3",
  "sessionId": "8c3e7e33-f999-45e6-9b77-c8618fc951cb"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "CaCLR cross-lingual calibration phase 1 full validation",
  "sessionId": "8c3e7e33-f999-45e6-9b77-c8618fc951cb"
}
```

---
