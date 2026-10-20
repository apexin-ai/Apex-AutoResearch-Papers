# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/edfe3f73-b51a-48bc-bb8c-8e30abc59c32.jsonl`
- **Structured JSON:** [`28425fec5c2225d20d47.json`](../../sessions/28/28425fec5c2225d20d47.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T18:56:48.066Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T18:56:48.066Z",
  "sessionId": "edfe3f73-b51a-48bc-bb8c-8e30abc59c32",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: xling_calib_direction\nfocus: Core submission for EACL 2027 ARR: 2 models (Qwen3-235B + Llama 4 Scout) × 20 languages. Key risks: (1) CaCLR may not outperform simple linear projection; (2) difficulty-shared vs capability-specific decomposition may not cleanly separate; (3) orthogonality claim 4 may be seen as incremental. MVP showed mean-shift completely fails, Pareto tradeoff directly observed at L24 vs L27.\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) shifts the Pareto frontier by jointly optimizing calibration and cross-lingual invariance, enabling effective probe transfer at deeper, better-calibrated layers without target-language correctness labels.\n- MVP evidence: Mean-shift fails entirely (0/5 languages improved) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, and propose CaCLR to shift the frontier. This is both a field-level viability test and a practical method contribution.\n- **Headline template**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak\"** → 5 transfer conditions tested. Mean-shift failure (MVP-confirmed) motivates CaCLR. Mean-shift works for Xiao et al.'s knowledge boundary but fails for correctness — important finding.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR).\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request.\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    INT8 weight quantization.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: Needs 2× RTX 6000 PRO 96GB at INT8.\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency. Train CaCLR probes using English labels + unlabeled\n    parallel activations. Compare vs zero-shot, mean-shift, linear projection, few-shot\n    (25/100) across full Pareto frontier for both models × 20 languages. Hyperparameter\n    tuning (α, β) on held-out English + 5-language validation.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021.\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: Need IRT difficulty scores from GlobalMMLU or external source.\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'INT8 validation ablation: compare INT8 vs FP16 probing results at\n    5 representative layers for Llama 4 Scout on 5% random subset. Validates that\n    INT8 quantization doesn''t distort correctness signals.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 31B Dense (60 layers, dense, FP16): third architecture for\n    camera-ready. Full Pareto frontier, 20+ languages. Provides dense vs MoE architectural\n    contrast.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: failed\n  metrics:\n    bug: layer_config_mismatch\n    detail: extract_activations.py used --layers 2,6,10,14,18,22,26 but train_probe.py\n      and transfer_eval.py used default layers 0,4,8,12,16,20,24,28,31. Probe training\n      skipped all layers (activation files not found). Activations (42 files) are\n      valid and reusable.\n    fix: Add --layers 2,6,10,14,18,22,26 to train_probe.py and transfer_eval.py in\n      run_mvp_002.sh\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: RUNNING\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    bug: layer_config_mismatch\n    detail: extract_activations.py used --layers 2,6,10,14,18,22,26 but train_probe.py\n      and transfer_eval.py used default layers 0,4,8,12,16,20,24,28,31. Probe training\n      skipped all layers (activation files not found). Activations (42 files) are\n      valid and reusable.\n    fix: Add --layers 2,6,10,14,18,22,26 to train_probe.py and transfer_eval.py in\n      run_mvp_002.sh\n- exp_id: mvp_003\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T18:56:48.069Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T18:56:48.069Z",
  "sessionId": "edfe3f73-b51a-48bc-bb8c-8e30abc59c32"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T18:56:48.097Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

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

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b0812c6f-98d1-4cc5-8eb0-047426a6395d",
  "type": "user",
  "uuid": "a455776d-c2a1-403f-aeee-a1cfd553bbc2",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "edfe3f73-b51a-48bc-bb8c-8e30abc59c32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T18:56:48.095Z_

```json
{
  "parentUuid": "a455776d-c2a1-403f-aeee-a1cfd553bbc2",
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
  "uuid": "80f44697-d148-454d-a641-3503d4fc8247",
  "timestamp": "2026-05-20T18:56:48.095Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "edfe3f73-b51a-48bc-bb8c-8e30abc59c32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T18:56:48.095Z_

```json
{
  "parentUuid": "80f44697-d148-454d-a641-3503d4fc8247",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8c3c6d54-9790-416a-84dc-af784556a1f5",
  "timestamp": "2026-05-20T18:56:48.095Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "edfe3f73-b51a-48bc-bb8c-8e30abc59c32",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "8c3c6d54-9790-416a-84dc-af784556a1f5",
  "sessionId": "edfe3f73-b51a-48bc-bb8c-8e30abc59c32"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for xling_calib_direction",
  "sessionId": "edfe3f73-b51a-48bc-bb8c-8e30abc59c32"
}
```

---

### Assistant

_source line 8 · 2026-05-20T18:57:24.241Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to define three tiers (best/median/worst) for Dream simulation scenarios for their cross-lingual calibration direction research project targeting EACL 2027.

Let me analyze the existing data and project context carefully:

**MVP results (Qwen2.5-7B, 6 languages):**
- EN best AUROC: 0.7541 (L27)
- EN best ECE raw: 0.1951, after temp cal: 0.0744


- Zero-shot transfer shows mixed results across languages, with mean-shift approaches failing entirely and a clear Pareto tradeoff emerging between different layer configurations.

The main risks I'm seeing are whether CaCLR can actually beat simpler baselines, whether the difficulty-shared versus capability-specific decomposition will cleanly separate, and whether the orthogonality claims might come across as incremental rather than novel.

Now I'm mapping out the four core pillars of this work: the Pareto frontier discovery, the decomposition analysis, the CaCLR method itself, and the cross-lingual orthogonality findings. For each one, I need to think through what success actually looks like here—the best case would be CaCLR substantially outperforming all baselines with clean, consistent results across architectures and languages, while the median case is more modest improvements with noisier patterns that require softening some of the claims.

Looking at the worst-case scenario, if CaCLR doesn't consistently beat linear projection and the Pareto frontier doesn't hold up, I'd need to pivot the framing toward discovery and analysis rather than positioning it as a methodological breakthrough. Either way, the work is still viable for EACL. Now I'm thinking through the specific performance targets—for the full-scale experiments with the larger models and 20 languages, I'm expecting English AUROC in the 0.76-0.85 range depending on how things shake out, cross-lingual zero-shot performance around 0.64-0.80, and CaCLR results somewhere in that 0.68-0.83 band. Now I'm looking at how the Pareto frontier behaves across different scenarios—it's cleaner in the best case with consistent monotonic tradeoffs, but gets noisier and less generalizable as conditions degrade. For the decomposition analysis, the difficulty projection is doing meaningful work when it explains over 60% of the transfer gap, though in median cases it only accounts for 30-50% of the variance. I'm thinking through how to frame this: the core contribution is really the systematic analysis of the Pareto frontier itself, with CaCLR as a useful but not transformative improvement over simpler baselines. The narrative should emphasize the methodological insight rather than positioning CaCLR as a breakthrough solution.

In the worst-case framing, this becomes a diagnostic study showing that probe-based calibration fundamentally struggles with cross-lingual transfer—which is still publishable as a negative result with strong methodology, just reoriented around what the field learns about the limits of this approach. Now I'm considering how the larger Qwen model might shift these results—the English AUROC should improve from the 0.754 we saw on the 7B version, but the cross-lingual transfer behavior is where the real question lies.

Let me nail down the specific metrics I'll be tracking: English performance at the best layer, average zero-shot transfer across the 19 non-English languages, how much performance drops when moving from English to those languages, how much CaCLR improves over a simple linear projection baseline, ECE reduction gains compared to temperature scaling, how clearly the Pareto frontier emerges between layer depth and transfer degradation, what fraction of the transfer gap variance the difficulty-shared component explains, and how aligned the correctness and confidence directions are across languages.

Writing YAML config...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c3c6d54-9790-416a-84dc-af784556a1f5",
  "isSidechain": false,
  "requestId": "req_011CbELBMAESkzCWVjZCvew5",
  "type": "assistant",
  "uuid": "18cea41b-92c5-474e-986a-e5beb9515f9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "edfe3f73-b51a-48bc-bb8c-8e30abc59c32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReHdC3CFVWh4GqfRPc9AVJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10370,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3880,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10370
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

_source line 9 · 2026-05-20T18:58:08.014Z_

```yaml
tiers:
  best:
    meaning: "All 4 claims fully validated at scale. Pareto frontier is crisp and architecture-consistent, decomposition cleanly separates, CaCLR decisively outperforms linear projection, orthogonality generalizes. Paper runs original framing with no claim adjustments."
    key_assumptions:
      - "Pareto frontier (depth vs transferability tradeoff) replicates on both Qwen3-235B and Llama4 Scout with clear monotonic shape"
      - "CaCLR consistently outperforms linear projection — the consistency loss term provides genuine value beyond simple alignment"
      - "Difficulty-shared component accounts for majority of transferable signal; projecting it out isolates a clean capability-specific residual"
      - "Correctness-confidence orthogonality (cosine < 0.1) holds across all 20 languages and both architectures"
      - "Low-resource languages (sw, yo, ig) achieve usable zero-shot transfer (AUROC > 0.60)"
    number_ranges:
      en_auroc_best_layer: [0.80, 0.86]
      zs_transfer_auroc_mean_19lang: [0.71, 0.79]
      zs_transfer_drop_mean_pp: [5, 12]
      caclr_vs_linproj_auroc_delta_pp: [2.5, 5.0]
      caclr_ece_reduction_vs_tempcal_pct: [30, 50]
      pareto_depth_transfer_rank_corr: [0.75, 0.95]
      decomp_difficulty_var_explained_pct: [55, 80]
      orthogonality_cosine_mean: [0.02, 0.08]
      low_resource_zs_pass_rate: [0.80, 1.0]
      caclr_improvement_pass_rate: [0.85, 1.0]
      pareto_frontier_agreement_across_arch: [0.80, 1.0]
    narrative_direction: "Original framing stands: 'CaCLR shifts the cross-lingual calibration Pareto frontier.' All 4 claims form an unbroken causal chain — discovery → analysis → method → mechanism. Headline: CaCLR reduces non-EN ECE by 30-50% over temp scaling with zero target-language labels. Pareto frontier is the organizing principle, CaCLR is the actionable contribution, decomposition explains why it works, orthogonality explains why output-based methods can't."

  median:
    meaning: "Claims 1 and 4 fully hold. Claim 2 partially holds (decomposition works but is noisy). Claim 3 is mixed — CaCLR helps but only marginally beats linear projection on high/mid-resource languages and fails to separate on low-resource. Paper needs rebalancing: elevate discovery/analysis, moderate method claims."
    key_assumptions:
      - "Pareto frontier replicates on both architectures but with different shapes — Qwen3 shows clear tradeoff, Llama4 is flatter or noisier"
      - "CaCLR outperforms zero-shot and mean-shift clearly, but only matches or marginally beats linear projection (within 1-2pp on most languages)"
      - "Difficulty projection removes some but not most transfer gap; capability-specific residual is noisy and confounded with language-family effects"
      - "Orthogonality generalizes but with higher variance in low-resource languages (cosine 0.05-0.20)"
      - "Low-resource languages show inconsistent zero-shot transfer; 2-3 of 5 low-resource langs fail AUROC 0.60 threshold"
    number_ranges:
      en_auroc_best_layer: [0.77, 0.83]
      zs_transfer_auroc_mean_19lang: [0.64, 0.73]
      zs_transfer_drop_mean_pp: [8, 18]
      caclr_vs_linproj_auroc_delta_pp: [0.5, 2.5]
      caclr_ece_reduction_vs_tempcal_pct: [12, 28]
      pareto_depth_transfer_rank_corr: [0.50, 0.78]
      decomp_difficulty_var_explained_pct: [25, 50]
      orthogonality_cosine_mean: [0.04, 0.15]
      low_resource_zs_pass_rate: [0.40, 0.70]
      caclr_improvement_pass_rate: [0.60, 0.85]
      pareto_frontier_agreement_across_arch: [0.55, 0.80]
    narrative_direction: "Rebalance toward discovery + analysis. Claim 1 (Pareto frontier) becomes the headline contribution — first systematic characterization of depth-transferability tradeoff across architectures and 20 languages. Claim 2 reframes decomposition as 'partial but prescriptive': difficulty component is clearly transferable, capability residual is noisy but the decomposition still predicts when simple baselines suffice vs when CaCLR helps. Claim 3 softens: CaCLR is presented as 'matching or exceeding the best simple baseline (linear projection) while requiring no target-language data at all' — emphasize the zero-label setting rather than raw metric superiority. Add ablation showing where CaCLR's consistency term specifically helps (likely mid-resource languages). Claim 4 presented with resource-tier analysis showing orthogonality is robust for well-represented languages. Headline shifts to: 'Cross-lingual calibration probes reveal architecture-dependent Pareto frontier; CaCLR matches supervised transfer without target labels.'"

  worst:
    meaning: "Pareto frontier is real but weak/noisy. CaCLR fails to beat linear projection. Decomposition doesn't cleanly separate. Core method contribution collapses. But the large-scale empirical characterization (2 models × 20 languages × all layers) and the negative results on CaCLR/mean-shift are themselves publishable — reframe as a diagnostic/field-test paper."
    key_assumptions:
      - "Pareto frontier is flat or non-monotonic on one architecture (e.g., Llama4 shows no clear depth-transfer tradeoff), only partially replicates from MVP"
      - "CaCLR underperforms or matches linear projection across the board; consistency loss term adds no value or hurts"
      - "Difficulty-capability decomposition fails: projecting out difficulty doesn't meaningfully change transfer, or difficulty and capability directions are not separable"
      - "Orthogonality holds but reviewers may see it as a replication of Miao & Ungar extended to 20 langs — incremental"
      - "Zero-shot transfer fails for >40% of languages (AUROC < 0.60), suggesting probe-based calibration has a language barrier"
    number_ranges:
      en_auroc_best_layer: [0.73, 0.80]
      zs_transfer_auroc_mean_19lang: [0.57, 0.66]
      zs_transfer_drop_mean_pp: [14, 25]
      caclr_vs_linproj_auroc_delta_pp: [-1.5, 0.5]
      caclr_ece_reduction_vs_tempcal_pct: [0, 12]
      pareto_depth_transfer_rank_corr: [0.15, 0.50]
      decomp_difficulty_var_explained_pct: [5, 25]
      orthogonality_cosine_mean: [0.03, 0.12]
      low_resource_zs_pass_rate: [0.10, 0.40]
      caclr_improvement_pass_rate: [0.30, 0.55]
      pareto_frontier_agreement_across_arch: [0.20, 0.55]
    narrative_direction: "Full reframe to field-level diagnostic paper: 'Does probe-based calibration work beyond English? A systematic study across 2 architectures and 20 languages.' The value proposition shifts from 'here is a method' to 'here is the first large-scale answer to whether this research line generalizes.' Key findings become: (1) probe-based correctness signals exist multilingually but transfer is unreliable — architecture, language family, and resource tier all modulate success in unpredictable ways; (2) simple alignment methods (linear projection, few-shot) match or beat more principled approaches (CaCLR) — the signal is too noisy for sophisticated invariance objectives to help; (3) mean-shift completely fails (confirmed at scale beyond MVP); (4) difficulty and capability are entangled in cross-lingual representations, unlike the clean separation assumed by prior English-only work. Frame CaCLR ablation as a rigorous negative result that saves the community from pursuing consistency-based objectives for this problem. Lean into Claim 4 (orthogonality persists cross-lingually → output-based calibration is structurally limited everywhere, not just English) as the one mechanistic takeaway. Still targets EACL — negative/diagnostic results at this scale and rigor are valuable, especially when the field is actively expanding probe-based methods without multilingual validation."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18cea41b-92c5-474e-986a-e5beb9515f9e",
  "isSidechain": false,
  "requestId": "req_011CbELBMAESkzCWVjZCvew5",
  "type": "assistant",
  "uuid": "51be4852-ede3-44a6-8f2a-fba0f83daaa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "edfe3f73-b51a-48bc-bb8c-8e30abc59c32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReHdC3CFVWh4GqfRPc9AVJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10370,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3880,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10370
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "51be4852-ede3-44a6-8f2a-fba0f83daaa9",
  "sessionId": "edfe3f73-b51a-48bc-bb8c-8e30abc59c32"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for xling_calib_direction",
  "sessionId": "edfe3f73-b51a-48bc-bb8c-8e30abc59c32"
}
```

---
