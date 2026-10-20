# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：SVA marginal PASS（统计上弱），Qwen ACDC 技术可行但结果 mixed；Jaccard-utility 趋势可见但数据点不足

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/9fa4408e-fc3a-466c-8bb9-049ddeee63fb.jsonl`
- **Structured JSON:** [`d743c44761deb97f5f28.json`](../../sessions/d7/d743c44761deb97f5f28.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T08:30:10.898Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T08:30:10.898Z",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：SVA marginal PASS（统计上弱），Qwen ACDC 技术可行但结果 mixed；Jaccard-utility 趋势可见但数据点不足以达到统计显著\n核心假设：['SVA css_1.00 Δ(CPR) ∈ [0.005, 0.03]，condition④ technically PASS 但无统计置信度', 'Qwen ACDC 与 EAP-IG/EP Jaccard 中等（0.3-0.55），CSS 结果 1 PASS 1 FAIL 或全部 marginal', '总共 3-4 个有效数据点，Jaccard-utility 趋势方向正确但 p > 0.1', '低 Jaccard tasks 的 CSS PASS 率 ~50%（含 marginal）']\n关键指标范围：{'sva_cond4_delta': [0.005, 0.03], 'gpt2_pass_rate': ['1.5/3', '2/3'], 'qwen_ioi_css10_cpr_vs_best': [-0.02, 0.03], 'qwen_max_pairwise_jaccard': [0.3, 0.55], 'jaccard_utility_spearman_rho': [0.5, 0.8], 'total_task_model_points': [3, 4], 'low_jaccard_css_pass_fraction': [0.4, 0.65]}\n叙事方向：需要 reframe。降级 Claim 1 为 conditional result，升级 Claim 2 和 Claim 3 为主线。 叙事变为：\"CSS 的有效性取决于方法多样性，我们提供诊断框架（Jaccard 作为先验预测指标）帮助从业者判断何时值得做 consensus。\" Arithmetic 高 Jaccard → CSS 失败 成为核心 supporting evidence 而非 negative result。 SVA 描述为 \"borderline case consistent with moderate Jaccard\" 而非 strong positive。 论文从 \"CSS always works\" 变为 \"CSS works iff methods are diverse, and we can predict when\"。 仍可投 EMNLP，但需要诚实的 limitation section 承认数据点有限。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: structfuse-context\nfocus: 关键更新（相比上次 Dream 尝试）：\n1. SVA 条件④用 css_1.00 重新评估后可能从 negative 翻转为 marginal PASS（Δ=0.0127）\n2. D029 已决定用 ACDC top-k 替代 IFR（IFR 在 Qwen 上 Jaccard=0.000，完全不兼容）\n3. 当前真实成绩：IOI 明确 PASS，Arithmetic FAIL，SVA 待定（marginal），Qwen IFR FAIL（已弃用）\n4. css_0.67 评估 bug 影响所有历史 CSS≥0.67 数据\n5. 核心 tension：CSS faithfulness 优势高度 task-dependent，1/3 明确 PASS 的成功率能否支撑 EMNLP 投稿？\n6. 三条路：A) reframed \"CSS utility predicted by Jaccard\" 投 EMNLP，B) 加更多任务补数据点，C) pivot 方向\n\n审稿人请重点评估：reframed claim 在当前证据（可能 1.5/3 GPT-2 tasks + pending Qwen ACDC）下的说服力，以及 experiment_plan.yaml 剩余实验能否在 12 天内补足。\n\n## paper_framing.md\n\n# Paper Framing — structfuse-context\n\n> 最后更新: 2026-05-13 | 更新原因: MVP 结果出齐，基于 D027 reframe\n\n## Target Venue\nEMNLP 2026 Main (ARR deadline 2026-05-25)\n\n## Core Insight\nCross-method binary consensus (CSS) identifies faithful and edge-efficient circuit subsets **when discovery methods genuinely disagree** (low pairwise Jaccard). When methods are highly correlated (high Jaccard), CSS degenerates and provides no additional value over any single method. Inter-method correlation is a predictive signal for consensus utility.\n\n## Narrative Arc\n1. Circuit discovery methods (EAP-IG, Edge Pruning, ACDC) find different circuits for the same task — but which edges are \"real\"?\n2. We propose CSS: binary consensus scoring across K≥3 methods from different algorithmic families\n3. CSS=1.0 (full consensus) circuits are dramatically smaller yet comparably or more faithful — but only when methods provide independent evidence\n4. When methods are correlated (same algorithmic family, or task structure forces agreement), CSS degenerates to the most selective method\n5. This reveals a fundamental property: consensus value ∝ method diversity, measurable via pairwise Jaccard\n\n## Core Claims\n\n### Claim 1: CSS identifies edge-efficient consensus circuits (PRIMARY)\n- **Evidence needed**: CSS=1.0 CPR ≥ best single-method CPR on tasks with low inter-method Jaccard\n- **Current status**: IOI PASS (CSS=1.0 14 edges, CPR=0.109 > all 50-edge single methods)\n- **Strength**: Strong on IOI; needs 2+ more localized-circuit tasks\n\n### Claim 2: CSS utility is predicted by inter-method correlation (PRIMARY)\n- **Evidence needed**: Positive correlation between method diversity (1 - max pairwise Jaccard) and CSS faithfulness advantage\n- **Current status**: IOI Jaccard=0.31 → CSS works; Arithmetic Jaccard=0.695 → CSS fails. Two data points.\n- **Strength**: Mechanistically motivated, needs 3+ tasks to establish pattern\n\n### Claim 3: ACDC isinf binarization causes CSS degeneration (METHODOLOGICAL)\n- **Evidence needed**: Show CSS=1.0 ≡ ACDC under isinf; top-k breaks degeneration\n- **Current status**: Fully demonstrated on both IOI and Arithmetic\n- **Strength**: Strong, fully supported\n\n### Claim 4: CSS as diagnostic taxonomy (SECONDARY)\n- **Evidence needed**: CSS distribution (1/3, 2/3, 3/3 proportions) reveals task structure\n- **Current status**: IOI has dispersed CSS distribution (low 3/3 ratio); Arithmetic has concentrated distribution (high 3/3 ratio when k normalized)\n- **Strength**: Needs more tasks and mechanistic analysis\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Only 2 tasks, generalization unclear\"\n- **Mitigation**: Add SVA (localized), DocQA or similar (distributed) to establish pattern\n- **Phase 2 models with IFR** naturally increase method diversity → should help\n\n### R2: \"CSS=1.0 edge efficiency could be just circuit size effect\"\n- **Mitigation**: Size-normalized CPR comparison; show CSS=1.0 achieves same CPR as 3-5x larger single-method circuits\n\n### R3: \"EAP-IG and EP are gradient-adjacent, K=3 effectively K≈2\"\n- **Mitigation**: Phase 2 adds IFR (similarity-based, different family); Jaccard analysis shows exactly when this matters\n\n### R4: \"Why not use score averaging instead of binary consensus?\"\n- **Mitigation**: Binary consensus is threshold-free (no score calibration needed across methods); compare with Mondorf et al. score averaging\n\n### R5: \"ACDC binarization sensitivity undermines robustness\"\n- **Mitigation**: Top-k normalization as standard preprocessing; show results stable across k=50-150\n\n## Competitors\n- **CIRCUS** (Parekh 2026): Threshold diversity within single method; we tried it, it failed (D021 negative ablation)\n- **Mondorf et al.** (2510.06811): Cross-method score averaging (gradient family only); we use binary consensus across diverse families\n- **PIE** (2604.16889): Iterative pruning ensemble; single paradigm\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_pilot_gpt2_ioi\n  name: ''\n  status: DEPLOYED\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pilot_gpt2_ioi_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_pilot_gpt2_ioi_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    off_diagonal_pct: 13.3\n    off_diagonal_ci: '[1.7%, 40.5%]'\n    circus_core_edges: 15\n    css_core_edges_2of3: 52\n    css_core_edges_3of3: 7\n    gate: PASS_MAIN\n    d002_triggered: true\n    pairwise_jaccard:\n      eapig_x_ep: 0.3072\n      eapig_x_acdc: 0.0962\n      ep_x_acdc: 0.0857\n    three_way_ratio: 0.0452\n    circuit_sizes:\n      eapig: 100\n      ep: 100\n      acdc: 14\n    acdc_binarization: isinf (14 Infinity edges out of 32491)\n    faithfulness_vs_ioi_ref:\n      css_2of3_recall: 1\n      css_2of3_precision: 0.231\n      css_3of3_recall: 0.583\n      css_3of3_precision: 1\n      acdc_recall: 0.833\n      acdc_precision: 0.714\n    phase_d_faithfulness:\n      css_1.00:\n        edges: 7\n        CPR: 0.1095\n        CMD: 0.911\n      css_0.67:\n        edges: 52\n        CPR: 0.0634\n        CMD: 0.9582\n      acdc:\n        edges: 14\n        CPR: 0.0286\n        CMD: 0.9937\n      circus_core:\n        edges: 15\n        CPR: -0.1081\n        CMD: 1.1337\n      eap_ig:\n        edges: 100\n        CPR: -0.1092\n        CMD: 1.1348\n      ep:\n        edges: 100\n        CPR: -0.2413\n        CMD: 1.2699\n    phase_d_note: CPR偏低, node-level zero ablation破坏性大, CSS-1.0表现最好(CPR=0.11)\n- exp_id: mvp_arithmetic_gpt2_k3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    off_diagonal_pct: 92.9\n    off_diagonal_ci: '[91.0%, 94.5%]'\n    gate_verdict_code: PASS_MAIN (D002, unreliable)\n    gate_verdict_d025: FAIL (condition④)\n    css_distribution:\n      1/3: 36\n      2/3: 65\n      3/3: 17\n    pairwise_jaccard:\n      eapig_x_ep: 0.6949\n      eapig_x_acdc: 0.17\n      ep_x_acdc: 0.17\n    three_way_ratio: 0.144\n    circuit_sizes:\n      eapig: 100\n      ep: 100\n      acdc: 17\n    acdc_binarization: isinf (17 edges)\n    faithfulness_zero:\n      css_1.00:\n        edges: 17\n        CPR: -0.184\n        CMD: 5.197\n      eap_ig:\n        edges: 100\n        CPR: -0.131\n        CMD: 4.966\n      ep:\n        edges: 100\n        CPR: -0.163\n        CMD: 5.106\n    faithfulness_mean:\n      css_1.00_isinf:\n        edges: 17\n        CPR: 0.985\n        CMD: 0.068\n      css_1.00_k50:\n        edges: 44\n        CPR: 0.919\n        CMD: 0.357\n      css_1.00_k75:\n        edges: 54\n        CPR: 0.919\n        CMD: 0.357\n      eapig_k50:\n        edges: 50\n        CPR: 0.985\n        CMD: 0.064\n      eapig_k75:\n        edges: 75\n        CPR: 0.996\n        CMD: 0.018\n      ep_k50:\n        edges: 50\n        CPR: 0.962\n        CMD: 0.167\n      acdc_k50:\n        edges: 50\n        CPR: 0.907\n        CMD: 0.407\n    d025_conditions:\n      c1_jaccard_lt_070: PASS (0.695, marginal)\n      c2_css_2of3_gte_10: PASS (65)\n      c3_css_1of3_gte_3: PASS (17)\n      c4_css_gt_single: FAIL (CSS=1.0 mean CPR=0.919 < EAP-IG=0.985)\n    ioi_cpr_inconsistency: 'RESOLVED: different tasks compared, not data reliability\n      issue'\n- exp_id: mvp_sva_gpt2_k3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    binarization: top-100\n    edge_counts:\n      eap_ig: 100\n      edge_pruning: 100\n      acdc: 100\n    pairwise_jaccard:\n      acdc_x_eap_ig: 0.3699\n      acdc_x_edge_pruning: 0.4286\n      eap_ig_x_edge_pruning: 0.6529\n    three_way_jaccard: 0.3007\n    css_distribution:\n      '0.33': 52\n      '0.67': 55\n      '1.00': 46\n    cross_table:\n      stable_core: 80\n      method_specific: 895\n      cross_unstable: 21\n      noise: 31495\n      off_diagonal_pct: 0.918\n    mean_cpr:\n      eap_ig: 1.1676\n      edge_pruning: 1.1681\n      acdc: 1.1619\n      css_0.67: 1.1738\n      css_1.00: 1.1738\n      stable_core: 1.1765\n      circus_core: 0.9944\n    zero_cpr:\n      eap_ig: -0.3477\n      edge_pruning: -0.6535\n      acdc: -1.1959\n      css_0.67: -0.7401\n      css_1.00: -0.7401\n      stable_core: -1.0772\n      circus_core: 0.7438\n    gate_verdict: PASS_MAIN\n    d025_conditions:\n      cond1_jaccard_lt070: true\n      cond2_css_ge23_ge10: true\n      cond3_css_10_ge3: true\n      cond4_css10_cpr_gt_single: true\n    note: 实际运行 top-100 binarization（非预期的 isinf）\n- exp_id: phase2_qwen05b_ioi_k3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_edges: 179388\n    eapig_edges: 179388\n    ep_edges: 179388\n    ifr_edges: 141384\n    binarization: top-100\n    css_distribution:\n      1/3: 200\n      2/3: 100\n      3/3: 0\n    css_core_3of3: 0\n    off_diagonal_pct: 100\n    pairwise_jaccard:\n      eapig_x_ep: 0.54\n      eapig_x_ifr: 0\n      ep_x_ifr: 0\n    baseline_io_s_diff: 7.0764\n    wall_clock_seconds: 83\n    timing:\n      eapig: 5.3\n      ep: 70.7\n      ifr: 1.3\n    cpr_all_approx_zero: true\n    note: IFR focuses early layers (m2→a3), EAP-IG/EP focus deep layers (a20.h9).\n      Top-100 too sparse for 179k-edge model. TransformerLens does not support Qwen2.5,\n      all HF-native.\n- exp_id: mvp_sva_gpt2_k3_topk\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    css_distribution:\n      '0.33': 60\n      '0.67': 54\n      '1.00': 44\n    pairwise_jaccard:\n      acdc_x_eap_ig: 0.3158\n      acdc_x_edge_pruning: 0.4184\n      eap_ig_x_edge_pruning: 0.6529\n    three_way_jaccard: 0.2785\n    core_off_diagonal_pct: 0.921\n    gate_verdict: PASS_MAIN\n    evaluation_zero:\n      css_0.67_cpr: -1.0279\n      css_0.67_cmd: 5.9185\n      css_0.67_edges: 98\n      css_1.00_cpr: -0.8166\n      css_1.00_cmd: 5.3017\n      css_1.00_edges: 44\n      eap_ig_cpr: -0.3705\n      edge_pruning_cpr: -0.6879\n      acdc_cpr: -1.2574\n    evaluation_mean:\n      css_0.67_cpr: 1.1724\n      css_0.67_cmd: 0.5031\n      css_0.67_edges: 98\n      css_1.00_cpr: 1.1873\n      css_1.00_cmd: 0.5465\n      css_1.00_edges: 44\n      eap_ig_cpr: 1.1703\n      edge_pruning_cpr: 1.1703\n      acdc_cpr: 1.1746\n    d025_conditions:\n      cond1_jaccard: PASS\n      cond2_css_geq_2_3: PASS\n      cond3_css_1_count: PASS\n      cond4_cpr_dominance: 'FAIL (mean: css_0.67=1.1724 < acdc=1.1746; zero: all negative)'\n    css_067_bug_fix:\n      bug: threshold_css used 1e-9 tolerance, 2/3=0.6667 < 0.67, excluded majority-vote\n        edges\n      before: css_0.67 = 44 edges (same as css_1.00)\n      after: css_0.67 = 98 edges (54 majority + 44 consensus)\n      impact: css_0.67 FIXED still worse than css_1.00 and single methods\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-13T08:30:10.901Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T08:30:10.901Z",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb"
}
```

---

## Round 1

40 recorded events

### User

_source line 3 · 2026-05-13T08:30:10.922Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：SVA marginal PASS（统计上弱），Qwen ACDC 技术可行但结果 mixed；Jaccard-utility 趋势可见但数据点不足以达到统计显著
核心假设：['SVA css_1.00 Δ(CPR) ∈ [0.005, 0.03]，condition④ technically PASS 但无统计置信度', 'Qwen ACDC 与 EAP-IG/EP Jaccard 中等（0.3-0.55），CSS 结果 1 PASS 1 FAIL 或全部 marginal', '总共 3-4 个有效数据点，Jaccard-utility 趋势方向正确但 p > 0.1', '低 Jaccard tasks 的 CSS PASS 率 ~50%（含 marginal）']
关键指标范围：{'sva_cond4_delta': [0.005, 0.03], 'gpt2_pass_rate': ['1.5/3', '2/3'], 'qwen_ioi_css10_cpr_vs_best': [-0.02, 0.03], 'qwen_max_pairwise_jaccard': [0.3, 0.55], 'jaccard_utility_spearman_rho': [0.5, 0.8], 'total_task_model_points': [3, 4], 'low_jaccard_css_pass_fraction': [0.4, 0.65]}
叙事方向：需要 reframe。降级 Claim 1 为 conditional result，升级 Claim 2 和 Claim 3 为主线。 叙事变为："CSS 的有效性取决于方法多样性，我们提供诊断框架（Jaccard 作为先验预测指标）帮助从业者判断何时值得做 consensus。" Arithmetic 高 Jaccard → CSS 失败 成为核心 supporting evidence 而非 negative result。 SVA 描述为 "borderline case consistent with moderate Jaccard" 而非 strong positive。 论文从 "CSS always works" 变为 "CSS works iff methods are diverse, and we can predict when"。 仍可投 EMNLP，但需要诚实的 limitation section 承认数据点有限。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: structfuse-context
focus: 关键更新（相比上次 Dream 尝试）：
1. SVA 条件④用 css_1.00 重新评估后可能从 negative 翻转为 marginal PASS（Δ=0.0127）
2. D029 已决定用 ACDC top-k 替代 IFR（IFR 在 Qwen 上 Jaccard=0.000，完全不兼容）
3. 当前真实成绩：IOI 明确 PASS，Arithmetic FAIL，SVA 待定（marginal），Qwen IFR FAIL（已弃用）
4. css_0.67 评估 bug 影响所有历史 CSS≥0.67 数据
5. 核心 tension：CSS faithfulness 优势高度 task-dependent，1/3 明确 PASS 的成功率能否支撑 EMNLP 投稿？
6. 三条路：A) reframed "CSS utility predicted by Jaccard" 投 EMNLP，B) 加更多任务补数据点，C) pivot 方向

审稿人请重点评估：reframed claim 在当前证据（可能 1.5/3 GPT-2 tasks + pending Qwen ACDC）下的说服力，以及 experiment_plan.yaml 剩余实验能否在 12 天内补足。

## paper_framing.md

# Paper Framing — structfuse-context

> 最后更新: 2026-05-13 | 更新原因: MVP 结果出齐，基于 D027 reframe

## Target Venue
EMNLP 2026 Main (ARR deadline 2026-05-25)

## Core Insight
Cross-method binary consensus (CSS) identifies faithful and edge-efficient circuit subsets **when discovery methods genuinely disagree** (low pairwise Jaccard). When methods are highly correlated (high Jaccard), CSS degenerates and provides no additional value over any single method. Inter-method correlation is a predictive signal for consensus utility.

## Narrative Arc
1. Circuit discovery methods (EAP-IG, Edge Pruning, ACDC) find different circuits for the same task — but which edges are "real"?
2. We propose CSS: binary consensus scoring across K≥3 methods from different algorithmic families
3. CSS=1.0 (full consensus) circuits are dramatically smaller yet comparably or more faithful — but only when methods provide independent evidence
4. When methods are correlated (same algorithmic family, or task structure forces agreement), CSS degenerates to the most selective method
5. This reveals a fundamental property: consensus value ∝ method diversity, measurable via pairwise Jaccard

## Core Claims

### Claim 1: CSS identifies edge-efficient consensus circuits (PRIMARY)
- **Evidence needed**: CSS=1.0 CPR ≥ best single-method CPR on tasks with low inter-method Jaccard
- **Current status**: IOI PASS (CSS=1.0 14 edges, CPR=0.109 > all 50-edge single methods)
- **Strength**: Strong on IOI; needs 2+ more localized-circuit tasks

### Claim 2: CSS utility is predicted by inter-method correlation (PRIMARY)
- **Evidence needed**: Positive correlation between method diversity (1 - max pairwise Jaccard) and CSS faithfulness advantage
- **Current status**: IOI Jaccard=0.31 → CSS works; Arithmetic Jaccard=0.695 → CSS fails. Two data points.
- **Strength**: Mechanistically motivated, needs 3+ tasks to establish pattern

### Claim 3: ACDC isinf binarization causes CSS degeneration (METHODOLOGICAL)
- **Evidence needed**: Show CSS=1.0 ≡ ACDC under isinf; top-k breaks degeneration
- **Current status**: Fully demonstrated on both IOI and Arithmetic
- **Strength**: Strong, fully supported

### Claim 4: CSS as diagnostic taxonomy (SECONDARY)
- **Evidence needed**: CSS distribution (1/3, 2/3, 3/3 proportions) reveals task structure
- **Current status**: IOI has dispersed CSS distribution (low 3/3 ratio); Arithmetic has concentrated distribution (high 3/3 ratio when k normalized)
- **Strength**: Needs more tasks and mechanistic analysis

## Anticipated Reviewer Concerns

### R1: "Only 2 tasks, generalization unclear"
- **Mitigation**: Add SVA (localized), DocQA or similar (distributed) to establish pattern
- **Phase 2 models with IFR** naturally increase method diversity → should help

### R2: "CSS=1.0 edge efficiency could be just circuit size effect"
- **Mitigation**: Size-normalized CPR comparison; show CSS=1.0 achieves same CPR as 3-5x larger single-method circuits

### R3: "EAP-IG and EP are gradient-adjacent, K=3 effectively K≈2"
- **Mitigation**: Phase 2 adds IFR (similarity-based, different family); Jaccard analysis shows exactly when this matters

### R4: "Why not use score averaging instead of binary consensus?"
- **Mitigation**: Binary consensus is threshold-free (no score calibration needed across methods); compare with Mondorf et al. score averaging

### R5: "ACDC binarization sensitivity undermines robustness"
- **Mitigation**: Top-k normalization as standard preprocessing; show results stable across k=50-150

## Competitors
- **CIRCUS** (Parekh 2026): Threshold diversity within single method; we tried it, it failed (D021 negative ablation)
- **Mondorf et al.** (2510.06811): Cross-method score averaging (gradient family only); we use binary consensus across diverse families
- **PIE** (2604.16889): Iterative pruning ensemble; single paradigm


## registry (completed experiments)

- exp_id: mvp_pilot_gpt2_ioi
  name: ''
  status: DEPLOYED
  conclusion: killed
  metrics: {}
- exp_id: mvp_pilot_gpt2_ioi_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_pilot_gpt2_ioi_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    off_diagonal_pct: 13.3
    off_diagonal_ci: '[1.7%, 40.5%]'
    circus_core_edges: 15
    css_core_edges_2of3: 52
    css_core_edges_3of3: 7
    gate: PASS_MAIN
    d002_triggered: true
    pairwise_jaccard:
      eapig_x_ep: 0.3072
      eapig_x_acdc: 0.0962
      ep_x_acdc: 0.0857
    three_way_ratio: 0.0452
    circuit_sizes:
      eapig: 100
      ep: 100
      acdc: 14
    acdc_binarization: isinf (14 Infinity edges out of 32491)
    faithfulness_vs_ioi_ref:
      css_2of3_recall: 1
      css_2of3_precision: 0.231
      css_3of3_recall: 0.583
      css_3of3_precision: 1
      acdc_recall: 0.833
      acdc_precision: 0.714
    phase_d_faithfulness:
      css_1.00:
        edges: 7
        CPR: 0.1095
        CMD: 0.911
      css_0.67:
        edges: 52
        CPR: 0.0634
        CMD: 0.9582
      acdc:
        edges: 14
        CPR: 0.0286
        CMD: 0.9937
      circus_core:
        edges: 15
        CPR: -0.1081
        CMD: 1.1337
      eap_ig:
        edges: 100
        CPR: -0.1092
        CMD: 1.1348
      ep:
        edges: 100
        CPR: -0.2413
        CMD: 1.2699
    phase_d_note: CPR偏低, node-level zero ablation破坏性大, CSS-1.0表现最好(CPR=0.11)
- exp_id: mvp_arithmetic_gpt2_k3
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    off_diagonal_pct: 92.9
    off_diagonal_ci: '[91.0%, 94.5%]'
    gate_verdict_code: PASS_MAIN (D002, unreliable)
    gate_verdict_d025: FAIL (condition④)
    css_distribution:
      1/3: 36
      2/3: 65
      3/3: 17
    pairwise_jaccard:
      eapig_x_ep: 0.6949
      eapig_x_acdc: 0.17
      ep_x_acdc: 0.17
    three_way_ratio: 0.144
    circuit_sizes:
      eapig: 100
      ep: 100
      acdc: 17
    acdc_binarization: isinf (17 edges)
    faithfulness_zero:
      css_1.00:
        edges: 17
        CPR: -0.184
        CMD: 5.197
      eap_ig:
        edges: 100
        CPR: -0.131
        CMD: 4.966
      ep:
        edges: 100
        CPR: -0.163
        CMD: 5.106
    faithfulness_mean:
      css_1.00_isinf:
        edges: 17
        CPR: 0.985
        CMD: 0.068
      css_1.00_k50:
        edges: 44
        CPR: 0.919
        CMD: 0.357
      css_1.00_k75:
        edges: 54
        CPR: 0.919
        CMD: 0.357
      eapig_k50:
        edges: 50
        CPR: 0.985
        CMD: 0.064
      eapig_k75:
        edges: 75
        CPR: 0.996
        CMD: 0.018
      ep_k50:
        edges: 50
        CPR: 0.962
        CMD: 0.167
      acdc_k50:
        edges: 50
        CPR: 0.907
        CMD: 0.407
    d025_conditions:
      c1_jaccard_lt_070: PASS (0.695, marginal)
      c2_css_2of3_gte_10: PASS (65)
      c3_css_1of3_gte_3: PASS (17)
      c4_css_gt_single: FAIL (CSS=1.0 mean CPR=0.919 < EAP-IG=0.985)
    ioi_cpr_inconsistency: 'RESOLVED: different tasks compared, not data reliability
      issue'
- exp_id: mvp_sva_gpt2_k3
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    binarization: top-100
    edge_counts:
      eap_ig: 100
      edge_pruning: 100
      acdc: 100
    pairwise_jaccard:
      acdc_x_eap_ig: 0.3699
      acdc_x_edge_pruning: 0.4286
      eap_ig_x_edge_pruning: 0.6529
    three_way_jaccard: 0.3007
    css_distribution:
      '0.33': 52
      '0.67': 55
      '1.00': 46
    cross_table:
      stable_core: 80
      method_specific: 895
      cross_unstable: 21
      noise: 31495
      off_diagonal_pct: 0.918
    mean_cpr:
      eap_ig: 1.1676
      edge_pruning: 1.1681
      acdc: 1.1619
      css_0.67: 1.1738
      css_1.00: 1.1738
      stable_core: 1.1765
      circus_core: 0.9944
    zero_cpr:
      eap_ig: -0.3477
      edge_pruning: -0.6535
      acdc: -1.1959
      css_0.67: -0.7401
      css_1.00: -0.7401
      stable_core: -1.0772
      circus_core: 0.7438
    gate_verdict: PASS_MAIN
    d025_conditions:
      cond1_jaccard_lt070: true
      cond2_css_ge23_ge10: true
      cond3_css_10_ge3: true
      cond4_css10_cpr_gt_single: true
    note: 实际运行 top-100 binarization（非预期的 isinf）
- exp_id: phase2_qwen05b_ioi_k3
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    total_edges: 179388
    eapig_edges: 179388
    ep_edges: 179388
    ifr_edges: 141384
    binarization: top-100
    css_distribution:
      1/3: 200
      2/3: 100
      3/3: 0
    css_core_3of3: 0
    off_diagonal_pct: 100
    pairwise_jaccard:
      eapig_x_ep: 0.54
      eapig_x_ifr: 0
      ep_x_ifr: 0
    baseline_io_s_diff: 7.0764
    wall_clock_seconds: 83
    timing:
      eapig: 5.3
      ep: 70.7
      ifr: 1.3
    cpr_all_approx_zero: true
    note: IFR focuses early layers (m2→a3), EAP-IG/EP focus deep layers (a20.h9).
      Top-100 too sparse for 179k-edge model. TransformerLens does not support Qwen2.5,
      all HF-native.
- exp_id: mvp_sva_gpt2_k3_topk
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    css_distribution:
      '0.33': 60
      '0.67': 54
      '1.00': 44
    pairwise_jaccard:
      acdc_x_eap_ig: 0.3158
      acdc_x_edge_pruning: 0.4184
      eap_ig_x_edge_pruning: 0.6529
    three_way_jaccard: 0.2785
    core_off_diagonal_pct: 0.921
    gate_verdict: PASS_MAIN
    evaluation_zero:
      css_0.67_cpr: -1.0279
      css_0.67_cmd: 5.9185
      css_0.67_edges: 98
      css_1.00_cpr: -0.8166
      css_1.00_cmd: 5.3017
      css_1.00_edges: 44
      eap_ig_cpr: -0.3705
      edge_pruning_cpr: -0.6879
      acdc_cpr: -1.2574
    evaluation_mean:
      css_0.67_cpr: 1.1724
      css_0.67_cmd: 0.5031
      css_0.67_edges: 98
      css_1.00_cpr: 1.1873
      css_1.00_cmd: 0.5465
      css_1.00_edges: 44
      eap_ig_cpr: 1.1703
      edge_pruning_cpr: 1.1703
      acdc_cpr: 1.1746
    d025_conditions:
      cond1_jaccard: PASS
      cond2_css_geq_2_3: PASS
      cond3_css_1_count: PASS
      cond4_cpr_dominance: 'FAIL (mean: css_0.67=1.1724 < acdc=1.1746; zero: all negative)'
    css_067_bug_fix:
      bug: threshold_css used 1e-9 tolerance, 2/3=0.6667 < 0.67, excluded majority-vote
        edges
      before: css_0.67 = 44 edges (same as css_1.00)
      after: css_0.67 = 98 edges (54 majority + 44 consensus)
      impact: css_0.67 FIXED still worse than css_1.00 and single methods

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
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "type": "user",
  "uuid": "64311715-38a6-463b-ab1f-8bf890527894",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T08:30:10.921Z_

```json
{
  "parentUuid": "64311715-38a6-463b-ab1f-8bf890527894",
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
  "uuid": "809293c2-4080-4c52-9ba6-22cf5724eea0",
  "timestamp": "2026-05-13T08:30:10.921Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T08:30:10.921Z_

```json
{
  "parentUuid": "809293c2-4080-4c52-9ba6-22cf5724eea0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e29e8441-ceb9-4c7e-97fe-f5d060506df5",
  "timestamp": "2026-05-13T08:30:10.921Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframed CSS paper: Jaccard-predicted utility",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb"
}
```

---

### Assistant

_source line 7 · 2026-05-13T08:30:15.568Z_

Let me first review the experiment plan to understand what planned experiments need predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e29e8441-ceb9-4c7e-97fe-f5d060506df5",
  "isSidechain": false,
  "requestId": "req_011CazFjVFAQ21efZ6FQCdNd",
  "type": "assistant",
  "uuid": "204775a7-b237-4d31-b691-535c4c1f6445",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WvXHoTDta3CQtjMtkETHiS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10568,
      "cache_read_input_tokens": 11841,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10568,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 193,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10568
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

_source line 8 · 2026-05-13T08:30:19.411Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0138GWP7831rTTZtKoGYoxo4`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan files",
  "prompt": "Search for experiment_plan files in /home/ubuntu/.agent-ml-research-idea_gen_0509_3/. Look for YAML, markdown, or any file containing \"experiment_plan\" or \"planned\" experiments. Also look for any files with \"plan\" in the name. Search broadly — try patterns like **/*plan*, **/*experiment*, **/*.yaml, **/*.yml."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "204775a7-b237-4d31-b691-535c4c1f6445",
  "isSidechain": false,
  "requestId": "req_011CazFjVFAQ21efZ6FQCdNd",
  "type": "assistant",
  "uuid": "3eab1b05-c929-495f-acb4-eace526b7df0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WvXHoTDta3CQtjMtkETHiS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10568,
      "cache_read_input_tokens": 11841,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10568,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 193,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10568
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

_source line 9_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：SVA marginal PASS（统计上弱），Qwen ACDC 技术可行但结果 mixed；Jaccard-utility 趋势可见但数据点不足以达到统计显著 核心假设：['SVA css_1.00 Δ(CPR) ∈ [0.005, 0.03]，condition④ technically PASS…",
  "leafUuid": "3eab1b05-c929-495f-acb4-eace526b7df0",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb"
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframed CSS paper: Jaccard-predicted utility",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb"
}
```

---

### Tool result

_source line 11 · 2026-05-13T08:30:45.004Z_

<details><summary>↩ Tool result · `toolu_0138GWP7831rTTZtKoGYoxo4`</summary>

```text
Perfect! Now let me create a comprehensive summary of the experiment plan files I found.

## Summary: Experiment Plan Files Found

I've successfully located and analyzed the experiment planning files in the `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/` directory. Here are the key findings:

### Main Experiment Plan File

**`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/experiment_plan.yaml`**

This is the primary experiment planning document containing a comprehensive research roadmap with 14 planned experiments (plan_001 through plan_014). The structure includes:

**Completed MVP Phase (3 experiments):**
- plan_001: GPT-2 IOI K=3 CSS — PASS (CSS=1.0, CPR=0.109)
- plan_002: GPT-2 Arithmetic K=3 CSS — FAIL (CPR=0.919 < expected)
- plan_003: ACDC top-k binarization sweep — Confirmed isinf degeneration

**Research Phase (11 planned experiments):**
- Task Coverage (plans 004-005): SVA, DocQA/Factual Recall on GPT-2
- Model Scaling (plans 006-009): Qwen-2.5 0.5B, Gemma-2 2B, Llama-3.1 8B
- Ablations (plans 010-012): Binarization sensitivity, ablation method comparison, CIRCUS negative ablation
- Jaccard Prediction (plan 013): CSS utility correlation analysis
- Discussion (plan 014): IFR method divergence analysis

### Related Experiment Imagining Files

**`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/best/imagined_experiments.yaml`**

This file contains detailed imagined experiments with expected results and rationale for:
- SVA (Subject-Verb Agreement) on GPT-2 — plan_004
- Factual Recall on GPT-2 — plan_005
- Qwen-2.5 0.5B IOI with IFR — plan_006
- Qwen-2.5 0.5B Arithmetic — plan_007
- Gemma-2 2B IOI — plan_008
- Llama-3.1 8B IOI — plan_009
- Top-k Binarization Sensitivity — plan_010
- Ablation Methods Comparison — plan_011
- CIRCUS vs CSS Negative Ablation — plan_012
- Jaccard-CSS Correlation Analysis — plan_013

### Research Roadmap & Status

**`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ROADMAP.md`**

Provides research dashboard showing:
- Current phase: MVP verification stage
- Core hypothesis: CSS off-diagonal ≥5%
- Method configuration across models (GPT-2, Qwen, Gemma, Llama)
- MVP gate rules and decision criteria
- 4-phase schedule with GPU budget
- Key decision log (D001-D033) tracking project evolution

### Dream Registry Metadata

**`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/dream_registry.yaml`**

Contains metadata for three recent dream sessions:
- dream_20260513T044816: Failed (orchestrator crash)
- dream_20260513T054654: Completed (best tier)
- dream_20260513T081242: In progress (imagining stage)

### Additional Experiment Data Files

The directory also contains generated experiment data:
- `/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/{best,median,worst}/imagined_experiments.yaml`
- `/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/best/experiment_data.json`
- Phase 2 configuration files and run scripts

### Key Metrics & Thresholds

The experiment plan tracks:
- **CSS utility prediction**: Jaccard threshold ≈ 0.53 (threshold below which CSS=1.0 consensus shows consistent faithfulness advantage)
- **Spearman correlation**: ρ=0.94 (p=0.005) between method diversity and CSS utility
- **Task coverage**: 4 tasks (IOI, SVA, Factual Recall, Arithmetic) spanning localized→distributed spectrum
- **Model scaling**: From 125M (GPT-2) to 8B (Llama) parameters

All files are YAML/Markdown formatted and contain detailed methodology, expected results, and analytical frameworks for validating the CSS (Cross-method Structural Consensus) approach for robust circuit editing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3eab1b05-c929-495f-acb4-eace526b7df0",
  "isSidechain": false,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "type": "user",
  "uuid": "4e51404f-b220-4247-bed8-ae3177f70c7f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for experiment_plan files in /home/ubuntu/.agent-ml-research-idea_gen_0509_3/. Look for YAML, markdown, or any file containing \"experiment_plan\" or \"planned\" experiments. Also look for any files with \"plan\" in the name. Search broadly — try patterns like **/*plan*, **/*experiment*, **/*.yaml, **/*.yml.",
    "agentId": "ae43efe12dea425d5",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me create a comprehensive summary of the experiment plan files I found.\n\n## Summary: Experiment Plan Files Found\n\nI've successfully located and analyzed the experiment planning files in the `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/` directory. Here are the key findings:\n\n### Main Experiment Plan File\n\n**`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/experiment_plan.yaml`**\n\nThis is the primary experiment planning document containing a comprehensive research roadmap with 14 planned experiments (plan_001 through plan_014). The structure includes:\n\n**Completed MVP Phase (3 experiments):**\n- plan_001: GPT-2 IOI K=3 CSS — PASS (CSS=1.0, CPR=0.109)\n- plan_002: GPT-2 Arithmetic K=3 CSS — FAIL (CPR=0.919 < expected)\n- plan_003: ACDC top-k binarization sweep — Confirmed isinf degeneration\n\n**Research Phase (11 planned experiments):**\n- Task Coverage (plans 004-005): SVA, DocQA/Factual Recall on GPT-2\n- Model Scaling (plans 006-009): Qwen-2.5 0.5B, Gemma-2 2B, Llama-3.1 8B\n- Ablations (plans 010-012): Binarization sensitivity, ablation method comparison, CIRCUS negative ablation\n- Jaccard Prediction (plan 013): CSS utility correlation analysis\n- Discussion (plan 014): IFR method divergence analysis\n\n### Related Experiment Imagining Files\n\n**`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/best/imagined_experiments.yaml`**\n\nThis file contains detailed imagined experiments with expected results and rationale for:\n- SVA (Subject-Verb Agreement) on GPT-2 — plan_004\n- Factual Recall on GPT-2 — plan_005\n- Qwen-2.5 0.5B IOI with IFR — plan_006\n- Qwen-2.5 0.5B Arithmetic — plan_007\n- Gemma-2 2B IOI — plan_008\n- Llama-3.1 8B IOI — plan_009\n- Top-k Binarization Sensitivity — plan_010\n- Ablation Methods Comparison — plan_011\n- CIRCUS vs CSS Negative Ablation — plan_012\n- Jaccard-CSS Correlation Analysis — plan_013\n\n### Research Roadmap & Status\n\n**`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ROADMAP.md`**\n\nProvides research dashboard showing:\n- Current phase: MVP verification stage\n- Core hypothesis: CSS off-diagonal ≥5%\n- Method configuration across models (GPT-2, Qwen, Gemma, Llama)\n- MVP gate rules and decision criteria\n- 4-phase schedule with GPU budget\n- Key decision log (D001-D033) tracking project evolution\n\n### Dream Registry Metadata\n\n**`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/dream_registry.yaml`**\n\nContains metadata for three recent dream sessions:\n- dream_20260513T044816: Failed (orchestrator crash)\n- dream_20260513T054654: Completed (best tier)\n- dream_20260513T081242: In progress (imagining stage)\n\n### Additional Experiment Data Files\n\nThe directory also contains generated experiment data:\n- `/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/{best,median,worst}/imagined_experiments.yaml`\n- `/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/best/experiment_data.json`\n- Phase 2 configuration files and run scripts\n\n### Key Metrics & Thresholds\n\nThe experiment plan tracks:\n- **CSS utility prediction**: Jaccard threshold ≈ 0.53 (threshold below which CSS=1.0 consensus shows consistent faithfulness advantage)\n- **Spearman correlation**: ρ=0.94 (p=0.005) between method diversity and CSS utility\n- **Task coverage**: 4 tasks (IOI, SVA, Factual Recall, Arithmetic) spanning localized→distributed spectrum\n- **Model scaling**: From 125M (GPT-2) to 8B (Llama) parameters\n\nAll files are YAML/Markdown formatted and contain detailed methodology, expected results, and analytical frameworks for validating the CSS (Cross-method Structural Consensus) approach for robust circuit editing."
      }
    ],
    "totalDurationMs": 25586,
    "totalTokens": 42466,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1709,
      "cache_creation_input_tokens": 276,
      "cache_read_input_tokens": 39313,
      "output_tokens": 1168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 276
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1709,
          "output_tokens": 1168,
          "cache_read_input_tokens": 39313,
          "cache_creation_input_tokens": 276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 276,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 5,
      "searchCount": 5,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "3eab1b05-c929-495f-acb4-eace526b7df0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T08:30:47.678Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VDJ1QMnz2EKdtFHxpmRdjx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e51404f-b220-4247-bed8-ae3177f70c7f",
  "isSidechain": false,
  "requestId": "req_011CazFmzsS6e3pCC9gupgQN",
  "type": "assistant",
  "uuid": "df5b9568-912a-4e6e-808a-7153f7e228b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017JtEGcu3QFh6g8qgSoi831",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1369,
      "cache_read_input_tokens": 22409,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1369,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 22409,
          "cache_creation_input_tokens": 1369,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1369
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

_source line 13 · 2026-05-13T08:30:47.686Z_

<details><summary>↩ Tool result · `toolu_01VDJ1QMnz2EKdtFHxpmRdjx`</summary>

```text
1	experiments: []
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df5b9568-912a-4e6e-808a-7153f7e228b0",
  "isSidechain": false,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "type": "user",
  "uuid": "c5903e9e-06a3-42c0-a91a-102e6c7ea1ca",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/experiment_plan.yaml",
      "content": "experiments: []\n",
      "numLines": 2,
      "startLine": 1,
      "totalLines": 2
    }
  },
  "sourceToolAssistantUUID": "df5b9568-912a-4e6e-808a-7153f7e228b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14 · 2026-05-13T08:30:47.711Z_

````json
{
  "parentUuid": "c5903e9e-06a3-42c0-a91a-102e6c7ea1ca",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**structfuse-context**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"structfuse-context\")` 或 `load_project_config(\"structfuse-context\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/structfuse-context/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "83c62dd6-3bd3-47ed-9b49-d850adfe71ae",
  "timestamp": "2026-05-13T08:30:47.711Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Assistant

_source line 15 · 2026-05-13T08:30:51.069Z_

<details><summary>Logged reasoning block</summary>

```text
The experiment_plan.yaml is empty (just `experiments: []`). Let me look for the actual experiment plan data elsewhere - probably in the ROADMAP or other files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83c62dd6-3bd3-47ed-9b49-d850adfe71ae",
  "isSidechain": false,
  "requestId": "req_011CazFnCSTEUouf4bUPocrh",
  "type": "assistant",
  "uuid": "1415cd52-2766-4d86-a32a-bbe403a82e6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019V2Vk2SesDc7JdurzhsNFZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 23778,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 354,
          "cache_read_input_tokens": 23778,
          "cache_creation_input_tokens": 5067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5067
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

_source line 16 · 2026-05-13T08:30:52.168Z_

experiment_plan.yaml 是空的。让我找到实际的实验计划定义。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1415cd52-2766-4d86-a32a-bbe403a82e6b",
  "isSidechain": false,
  "requestId": "req_011CazFnCSTEUouf4bUPocrh",
  "type": "assistant",
  "uuid": "8736c05e-8467-4b88-a073-ecad5cb15d52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019V2Vk2SesDc7JdurzhsNFZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 23778,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 354,
          "cache_read_input_tokens": 23778,
          "cache_creation_input_tokens": 5067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5067
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

_source line 17 · 2026-05-13T08:30:58.532Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01E4ZCovNCTShPnTko3pe12K`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find planned experiments details",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/, I need to find where the planned experiments are defined. The experiment_plan.yaml is empty. Look for:\n1. ROADMAP.md - read it fully for experiment plan details\n2. Any files with \"plan_004\", \"plan_005\", \"plan_006\" etc.\n3. Any YAML/MD files that define what experiments are planned (not completed)\n4. The dream report files in artifacts/dream_reports/ - especially any imagined_experiments.yaml files\n5. Any file mentioning \"Qwen ACDC\" or \"phase2\" plans\n\nRead the full contents of the most relevant files. I need to know what experiments are PLANNED (not yet done) and their plan_ids."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8736c05e-8467-4b88-a073-ecad5cb15d52",
  "isSidechain": false,
  "requestId": "req_011CazFnCSTEUouf4bUPocrh",
  "type": "assistant",
  "uuid": "0fc429fa-2f73-4616-ab74-8811f253d2a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019V2Vk2SesDc7JdurzhsNFZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 23778,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 354,
          "cache_read_input_tokens": 23778,
          "cache_creation_input_tokens": 5067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5067
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

_source line 18 · 2026-05-13T08:31:34.775Z_

<details><summary>↩ Tool result · `toolu_01E4ZCovNCTShPnTko3pe12K`</summary>

```text
Perfect! Now I have all the information I need. Let me compile a comprehensive summary of the planned experiments.

## Summary: Planned Experiments in structfuse-context

Based on my thorough review of the project files, I found that **experiment_plan.yaml is indeed empty**, but the planned experiments are comprehensively defined in the **imagined_experiments.yaml files** from the dream reports (best/median/worst tiers dated 2026-05-13).

### **Key Finding: Three Experiment Plan Tiers**

The project uses a "dream" simulation approach with three narrative tiers (best/median/worst), each containing detailed imagined experiments with plan_ids. Here are the **PLANNED (not yet done) experiments**:

---

## **BEST TIER** — Most Optimistic Scenario
Plan IDs: **plan_004 through plan_013**

### Core Planned Experiments:
1. **plan_004** — GPT-2 Small Subject-Verb Agreement (SVA) K=3 CSS
   - Methods: EAP-IG + EP + ACDC
   - Expected result: CSS 优势（low Jaccard 0.22 → CSS CPR=0.12）

2. **plan_005** — GPT-2 Small Factual Recall K=3 CSS
   - Methods: EAP-IG + EP + ACDC
   - Expected: Distributed task, medium Jaccard (0.48) → CSS margin (CPR advantage=0.018)

3. **plan_006** — Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + IFR)
   - **IFR as third method** (similarity-based, different from gradient methods)
   - Expected: Lower Jaccard (0.28) → stronger CSS CPR (0.14)

4. **plan_007** — Qwen-2.5 0.5B Arithmetic K=3 (EAP-IG + EP + IFR)
   - Testing if IFR breaks high-correlation arithmetic pattern
   - Expected: max_Jaccard 0.58 (still high), CSS negative

5. **plan_008** — Gemma-2 2B IOI K=3 (EAP-IG + EP + IFR)
   - Scale validation to 2B model
   - Expected: CSS=1.0 CPR=0.13, advantage 0.09

6. **plan_009** — Llama-3.1 8B IOI K=3 (EAP-IG + EP + IFR)
   - Stretch goal: 8B model validation
   - Expected: CSS CPR=0.12, similar to smaller models

7. **plan_010** — Top-k Binarization Sensitivity Sweep
   - Systematic k sweep (50/75/100/150) on all completed tasks
   - Response to R5 (k robustness)
   - Expected: CSS=1.0 CPR stable, k-robust

8. **plan_011** — Ablation Method Comparison (Zero vs Mean vs Resample)
   - Compare evaluation methods on IOI and SVA
   - Expected: CSS advantage stable across ablations

9. **plan_012** — CIRCUS vs CSS Negative Ablation
   - Compare CIRCUS (threshold diversity) vs CSS (cross-method consensus)
   - Expected: CIRCUS fails (CPR=-0.108), CSS wins on IOI

10. **plan_013** — Jaccard-CSS Utility Correlation Analysis (KEY ANALYSIS)
    - Core data: 6 model×task pairs (IOI/SVA/Factual/Arithmetic × GPT-2/Qwen/Gemma)
    - Spearman ρ=0.94 (p=0.005) — **threshold ≈0.53**
    - **This is the crown jewel figure** showing (1-max_Jaccard) vs CSS advantage correlation

---

## **MEDIAN TIER** — Realistic Scenario
Plan IDs: **plan_004 through plan_013** (partial completion)

### Status of Plans:
- **plan_004** (SVA) — DONE, but partial support (CSS marginal, not superior)
- **plan_005** (Factual) — ABANDONED (GPT-2 Small factual recall too weak, ACDC failed)
- **plan_006** (Qwen IOI) — DONE, mixed results (IFR×EP Jaccard=0.55, higher than expected)
- **plan_007** (Qwen Arithmetic) — DONE, negative (CSS-1.0 CPR=0.932 < EAP-IG=0.971)
- **plan_008** (Gemma-2) — NOT ATTEMPTED (P2 priority, time constraints)
- **plan_009** (Llama-3.1 8B) — NOT ATTEMPTED (P3 priority, A100 80GB required)
- **plan_010** (k-sweep) — DONE, stable (k=75-150 range recommended)
- **plan_011** (ablation methods) — PARTIAL (IOI only, plan_013 listed as "not completed")
- **plan_012** (CIRCUS ablation) — DONE (CIRCUS cores CPR negative)
- **plan_013** (Jaccard correlation) — DONE (5 data points, Spearman ρ=-0.9 p=0.037)

---

## **WORST TIER** — Pessimistic Scenario
Plan IDs: **plan_004 through plan_013**

### Key findings:
- **Method correlation is systematic** — gradient methods (EAP-IG, EP) high correlation even on different tasks (Jaccard 0.48-0.62)
- **IFR doesn't provide independence** — similarity-based scoring correlates with gradient in transformer (Jaccard 0.45-0.52)
- **K_eff ≈ 1.5-1.8** (not true K=3 independence)
- **Only IOI positive** — likely artifact of ACDC isinf extreme sparsity (14 edges) + zero ablation bias
- **Jaccard-CSS correlation is confounded** — remove IOI/GPT-2 and ρ collapses to -0.30 (p=0.62)

---

## **Phase 2 Configuration (Already Defined)**

From `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/phase2_configs.yaml`:

**GPT-2 Small experiments:**
- gpt2_ioi (Priority 1 — MVP baseline)
- gpt2_greater_than (Priority 2)
- gpt2_docstring (Priority 2)

**Qwen-2.5 0.5B experiments (4 tasks):**
- qwen05_ioi (Priority 2)
- qwen05_greater_than (Priority 2)
- qwen05_docstring (Priority 2)
- qwen05_ioi_variant (Priority 3)

**Gemma-2 2B experiments (4 tasks, Priority 3):**
- gemma2_ioi, gemma2_greater_than, gemma2_docstring, gemma2_ioi_variant

**Llama-3.1 8B experiments (4 tasks, Priority 3):**
- llama31_ioi, llama31_greater_than, llama31_docstring, llama31_ioi_variant

---

## **What "Qwen ACDC" or "Phase 2" means:**

- **Phase 2** = After MVP completion, running full K=3 CSS computations across all 4 models × 4 tasks
- Currently in **Phase 1 (MVP pilot)**: Just validating CSS concept on GPT-2 Small with IOI and Arithmetic
- **Large model strategy (D006)**: Use IFR (Iterative Feature Removal) as 3rd method for large models (Qwen, Gemma, Llama), not ACDC
- **Qwen ACDC decision**: Actually **D029 reversed this** — switched from IFR back to ACDC top-k after discovering IFR zero-overlap issue

---

## **Critical Status Notes (from ROADMAP.md):**

- **Current blocker**: Awaiting mvp_arithmetic_gpt2_k3 completion → gate judgment
- **MVP gate rule**: If off-diagonal ≥5%, proceed to Phase 2; if 2-5%, confirm with Arithmetic; if <2%, kill
- **ARR deadline**: 2026-05-25 (12 days from 2026-05-13)
- **Next immediate task**: Write paper_framing.md + populate experiment_plan.yaml (currently empty!)

---

**In summary**: You have comprehensive planned experiment definitions in the dream reports (best/median/worst tiers), with plan_ids ranging from **plan_004 to plan_013**. The BEST tier shows the most ambitious 10-experiment plan for a strong paper; MEDIAN is more realistic with partial completions; WORST assumes method correlation defeats CSS. The empty experiment_plan.yaml should be populated from these imagined_experiments.yaml files once the Director makes tier selection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fc429fa-2f73-4616-ab74-8811f253d2a0",
  "isSidechain": false,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "type": "user",
  "uuid": "f7ded1ac-0f61-4e63-b40c-bd68c5a04221",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/, I need to find where the planned experiments are defined. The experiment_plan.yaml is empty. Look for:\n1. ROADMAP.md - read it fully for experiment plan details\n2. Any files with \"plan_004\", \"plan_005\", \"plan_006\" etc.\n3. Any YAML/MD files that define what experiments are planned (not completed)\n4. The dream report files in artifacts/dream_reports/ - especially any imagined_experiments.yaml files\n5. Any file mentioning \"Qwen ACDC\" or \"phase2\" plans\n\nRead the full contents of the most relevant files. I need to know what experiments are PLANNED (not yet done) and their plan_ids.",
    "agentId": "a35a40d5f6dfb18b5",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information I need. Let me compile a comprehensive summary of the planned experiments.\n\n## Summary: Planned Experiments in structfuse-context\n\nBased on my thorough review of the project files, I found that **experiment_plan.yaml is indeed empty**, but the planned experiments are comprehensively defined in the **imagined_experiments.yaml files** from the dream reports (best/median/worst tiers dated 2026-05-13).\n\n### **Key Finding: Three Experiment Plan Tiers**\n\nThe project uses a \"dream\" simulation approach with three narrative tiers (best/median/worst), each containing detailed imagined experiments with plan_ids. Here are the **PLANNED (not yet done) experiments**:\n\n---\n\n## **BEST TIER** — Most Optimistic Scenario\nPlan IDs: **plan_004 through plan_013**\n\n### Core Planned Experiments:\n1. **plan_004** — GPT-2 Small Subject-Verb Agreement (SVA) K=3 CSS\n   - Methods: EAP-IG + EP + ACDC\n   - Expected result: CSS 优势（low Jaccard 0.22 → CSS CPR=0.12）\n\n2. **plan_005** — GPT-2 Small Factual Recall K=3 CSS\n   - Methods: EAP-IG + EP + ACDC\n   - Expected: Distributed task, medium Jaccard (0.48) → CSS margin (CPR advantage=0.018)\n\n3. **plan_006** — Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + IFR)\n   - **IFR as third method** (similarity-based, different from gradient methods)\n   - Expected: Lower Jaccard (0.28) → stronger CSS CPR (0.14)\n\n4. **plan_007** — Qwen-2.5 0.5B Arithmetic K=3 (EAP-IG + EP + IFR)\n   - Testing if IFR breaks high-correlation arithmetic pattern\n   - Expected: max_Jaccard 0.58 (still high), CSS negative\n\n5. **plan_008** — Gemma-2 2B IOI K=3 (EAP-IG + EP + IFR)\n   - Scale validation to 2B model\n   - Expected: CSS=1.0 CPR=0.13, advantage 0.09\n\n6. **plan_009** — Llama-3.1 8B IOI K=3 (EAP-IG + EP + IFR)\n   - Stretch goal: 8B model validation\n   - Expected: CSS CPR=0.12, similar to smaller models\n\n7. **plan_010** — Top-k Binarization Sensitivity Sweep\n   - Systematic k sweep (50/75/100/150) on all completed tasks\n   - Response to R5 (k robustness)\n   - Expected: CSS=1.0 CPR stable, k-robust\n\n8. **plan_011** — Ablation Method Comparison (Zero vs Mean vs Resample)\n   - Compare evaluation methods on IOI and SVA\n   - Expected: CSS advantage stable across ablations\n\n9. **plan_012** — CIRCUS vs CSS Negative Ablation\n   - Compare CIRCUS (threshold diversity) vs CSS (cross-method consensus)\n   - Expected: CIRCUS fails (CPR=-0.108), CSS wins on IOI\n\n10. **plan_013** — Jaccard-CSS Utility Correlation Analysis (KEY ANALYSIS)\n    - Core data: 6 model×task pairs (IOI/SVA/Factual/Arithmetic × GPT-2/Qwen/Gemma)\n    - Spearman ρ=0.94 (p=0.005) — **threshold ≈0.53**\n    - **This is the crown jewel figure** showing (1-max_Jaccard) vs CSS advantage correlation\n\n---\n\n## **MEDIAN TIER** — Realistic Scenario\nPlan IDs: **plan_004 through plan_013** (partial completion)\n\n### Status of Plans:\n- **plan_004** (SVA) — DONE, but partial support (CSS marginal, not superior)\n- **plan_005** (Factual) — ABANDONED (GPT-2 Small factual recall too weak, ACDC failed)\n- **plan_006** (Qwen IOI) — DONE, mixed results (IFR×EP Jaccard=0.55, higher than expected)\n- **plan_007** (Qwen Arithmetic) — DONE, negative (CSS-1.0 CPR=0.932 < EAP-IG=0.971)\n- **plan_008** (Gemma-2) — NOT ATTEMPTED (P2 priority, time constraints)\n- **plan_009** (Llama-3.1 8B) — NOT ATTEMPTED (P3 priority, A100 80GB required)\n- **plan_010** (k-sweep) — DONE, stable (k=75-150 range recommended)\n- **plan_011** (ablation methods) — PARTIAL (IOI only, plan_013 listed as \"not completed\")\n- **plan_012** (CIRCUS ablation) — DONE (CIRCUS cores CPR negative)\n- **plan_013** (Jaccard correlation) — DONE (5 data points, Spearman ρ=-0.9 p=0.037)\n\n---\n\n## **WORST TIER** — Pessimistic Scenario\nPlan IDs: **plan_004 through plan_013**\n\n### Key findings:\n- **Method correlation is systematic** — gradient methods (EAP-IG, EP) high correlation even on different tasks (Jaccard 0.48-0.62)\n- **IFR doesn't provide independence** — similarity-based scoring correlates with gradient in transformer (Jaccard 0.45-0.52)\n- **K_eff ≈ 1.5-1.8** (not true K=3 independence)\n- **Only IOI positive** — likely artifact of ACDC isinf extreme sparsity (14 edges) + zero ablation bias\n- **Jaccard-CSS correlation is confounded** — remove IOI/GPT-2 and ρ collapses to -0.30 (p=0.62)\n\n---\n\n## **Phase 2 Configuration (Already Defined)**\n\nFrom `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/phase2_configs.yaml`:\n\n**GPT-2 Small experiments:**\n- gpt2_ioi (Priority 1 — MVP baseline)\n- gpt2_greater_than (Priority 2)\n- gpt2_docstring (Priority 2)\n\n**Qwen-2.5 0.5B experiments (4 tasks):**\n- qwen05_ioi (Priority 2)\n- qwen05_greater_than (Priority 2)\n- qwen05_docstring (Priority 2)\n- qwen05_ioi_variant (Priority 3)\n\n**Gemma-2 2B experiments (4 tasks, Priority 3):**\n- gemma2_ioi, gemma2_greater_than, gemma2_docstring, gemma2_ioi_variant\n\n**Llama-3.1 8B experiments (4 tasks, Priority 3):**\n- llama31_ioi, llama31_greater_than, llama31_docstring, llama31_ioi_variant\n\n---\n\n## **What \"Qwen ACDC\" or \"Phase 2\" means:**\n\n- **Phase 2** = After MVP completion, running full K=3 CSS computations across all 4 models × 4 tasks\n- Currently in **Phase 1 (MVP pilot)**: Just validating CSS concept on GPT-2 Small with IOI and Arithmetic\n- **Large model strategy (D006)**: Use IFR (Iterative Feature Removal) as 3rd method for large models (Qwen, Gemma, Llama), not ACDC\n- **Qwen ACDC decision**: Actually **D029 reversed this** — switched from IFR back to ACDC top-k after discovering IFR zero-overlap issue\n\n---\n\n## **Critical Status Notes (from ROADMAP.md):**\n\n- **Current blocker**: Awaiting mvp_arithmetic_gpt2_k3 completion → gate judgment\n- **MVP gate rule**: If off-diagonal ≥5%, proceed to Phase 2; if 2-5%, confirm with Arithmetic; if <2%, kill\n- **ARR deadline**: 2026-05-25 (12 days from 2026-05-13)\n- **Next immediate task**: Write paper_framing.md + populate experiment_plan.yaml (currently empty!)\n\n---\n\n**In summary**: You have comprehensive planned experiment definitions in the dream reports (best/median/worst tiers), with plan_ids ranging from **plan_004 to plan_013**. The BEST tier shows the most ambitious 10-experiment plan for a strong paper; MEDIAN is more realistic with partial completions; WORST assumes method correlation defeats CSS. The empty experiment_plan.yaml should be populated from these imagined_experiments.yaml files once the Director makes tier selection."
      }
    ],
    "totalDurationMs": 36237,
    "totalTokens": 72930,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1742,
      "cache_read_input_tokens": 68942,
      "output_tokens": 2240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1742
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2240,
          "cache_read_input_tokens": 68942,
          "cache_creation_input_tokens": 1742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1742,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 0,
      "bashCount": 3,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "0fc429fa-2f73-4616-ab74-8811f253d2a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：SVA marginal PASS（统计上弱），Qwen ACDC 技术可行但结果 mixed；Jaccard-utility 趋势可见但数据点不足以达到统计显著 核心假设：['SVA css_1.00 Δ(CPR) ∈ [0.005, 0.03]，condition④ technically PASS…",
  "leafUuid": "f7ded1ac-0f61-4e63-b40c-bd68c5a04221",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframed CSS paper: Jaccard-predicted utility",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb"
}
```

---

### Tool call

_source line 21 · 2026-05-13T08:31:37.729Z_

<details open><summary>🔧 Tool call — Read · `toolu_013w2AGwSJe5FS45RTrwFcJW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7ded1ac-0f61-4e63-b40c-bd68c5a04221",
  "isSidechain": false,
  "requestId": "req_011CazFqfkMMGvFTXweC6sDh",
  "type": "assistant",
  "uuid": "39105855-045e-49c3-9f6c-c3636f328fd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016kszi5xdNdW7hnrZuVSkBW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2602,
      "cache_read_input_tokens": 28845,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2602,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 28845,
          "cache_creation_input_tokens": 2602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2602
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

_source line 22 · 2026-05-13T08:31:37.742Z_

<details><summary>↩ Tool result · `toolu_013w2AGwSJe5FS45RTrwFcJW`</summary>

```text
1	tier: best
2	narrative_guidance: '原始 reframed claim 完整成立。四个任务（IOI、SVA、Factual Recall、Arithmetic）覆盖
3	  localized→distributed 全谱，Jaccard 作为 CSS utility 的 meta-diagnostic 是 novel 且 quantitatively
4	  validated 的 contribution。SVA 清晰复现 IOI 模式（低 Jaccard、CSS 优势显著）， Factual Recall 提供关键
5	  interpolation 数据点（中等 Jaccard、CSS 优势边际正），Arithmetic 作为 principled negative case 完善图景。IFR
6	  第四方法族在 Qwen 上进一步降低 max Jaccard， CSS=1.0 CPR 不退化甚至提升，直接回应 R3（K≈2 质疑）。Spearman ρ=0.94
7	  跨 6 个 model×task 组合成立，p=0.005，统计上无争议。论文叙事可以自信地以 Jaccard threshold (~0.55) 作为 practitioner
8	  guideline 收尾。
9	
10	  '
11	imagined_experiments:
12	- name: GPT-2 Small Subject-Verb Agreement K=3 CSS
13	  plan_id: plan_004
14	  description: '在 GPT-2 Small 上对 Subject-Verb Agreement (SVA) 任务运行三种发现方法 （EAP-IG,
15	    EP, ACDC），计算 CSS 分布和 faithfulness。SVA 是经典的 localized circuit 任务，核心计算集中在 layer
16	    7-10 的 number-tracking attention heads，预期方法间 Jaccard 低、CSS 优势显著。
17	
18	    '
19	  expected_results:
20	    eapig_edges: 50
21	    ep_edges: 50
22	    acdc_edges_isinf: 12
23	    acdc_edges_k50: 50
24	    jaccard_eapig_ep: 0.22
25	    jaccard_eapig_acdc: 0.08
26	    jaccard_ep_acdc: 0.06
27	    max_pairwise_jaccard: 0.22
28	    three_way_ratio: 0.032
29	    css_3of3_edges: 8
30	    css_2of3_edges: 31
31	    css_1of3_edges: 73
32	    css_1.00_edges: 8
33	    css_1.00_CPR: 0.12
34	    css_1.00_CMD: 0.89
35	    css_0.67_edges: 31
36	    css_0.67_CPR: 0.065
37	    css_0.67_CMD: 0.945
38	    acdc_edges: 12
39	    acdc_CPR: 0.03
40	    acdc_CMD: 0.975
41	    eapig_k50_CPR: -0.04
42	    eapig_k50_CMD: 1.05
43	    ep_k50_CPR: -0.07
44	    ep_k50_CMD: 1.08
45	    css1_cpr_advantage: 0.09
46	    css1_edge_ratio: 0.071
47	  result_rationale: 'SVA 在 GPT-2 Small 中依赖 layer 7-10 中约 5-8 个专门追踪主语数特征的 attention
48	    head。这是一个高度 localized 的电路：关键计算集中在少量 head 的 Q-K 匹配上。三种方法各自从不同角度发现该电路的不同子集——EAP-IG
49	    沿梯度 路径优先选取高 ∂L/∂e 的边，EP 通过逐步剪枝保留移除后损失最大的边，ACDC 通过激活差异识别 clean vs corrupt 下变化最大的边。由于电路
50	    localized，每种 方法只需少量边即可捕获核心功能，导致三组 top-50 edge set 的交集稀疏（max Jaccard=0.22）。CSS=1.0
51	    恰好捕获了所有三种方法共同认定的 8 条核心边—— 这些边对应 number-agreement 的关键 attention pattern，移除它们会破坏
52	    subject→verb 的 number propagation，因此 CPR=0.12 显著高于任何单方法。 ACDC 的 12 条 isinf 边虽然也
53	    localized，但包含了 4 条 ACDC 特有的 method-specific 边（其他方法未选中），导致部分噪声稀释了 faithfulness。
54	
55	    '
56	  tables:
57	  - name: 'Table: SVA Circuit Discovery Summary'
58	    description: '行: EAP-IG(k=50), EP(k=50), ACDC(isinf), CSS≥2/3, CSS=1.0 列: Edges,
59	      CPR, CMD, vs-best-single-Δ 展示 CSS=1.0 在仅 8 条边下达到 CPR=0.12，是 ACDC(0.03) 的 4 倍
60	
61	      '
62	  - name: 'Table: SVA Pairwise Jaccard Matrix'
63	    description: '3×3 对称矩阵，对角线为 1.0。EAP-IG×EP=0.22, EAP-IG×ACDC=0.08, EP×ACDC=0.06。与
64	      IOI 的 Jaccard 矩阵并列展示，突出 SVA 更低的 inter-method correlation
65	
66	      '
67	  figures_description:
68	  - 'Bar chart: x 轴为方法（EAP-IG, EP, ACDC, CSS≥2/3, CSS=1.0）， y 轴为 CPR。CSS=1.0 bar 显著高于其他所有方法，上方标注
69	    edge count。 与 IOI 对应图并列为 subplot，视觉化 CSS 优势在 localized tasks 上的复现
70	
71	    '
72	  analysis: 'SVA 完美复现 IOI 的核心模式：localized circuit → low Jaccard → CSS=1.0 faithfulness
73	    优势。max Jaccard 0.22 甚至低于 IOI 的 0.31，反映 SVA 电路更 集中（fewer critical heads），使方法分歧更大。CSS
74	    CPR advantage 0.09 与 IOI 的 0.08 一致，支撑 Claim 1。此结果将 Claim 1 的支持从 1 个任务扩展到 2 个，
75	    直接削弱 R1 泛化性质疑。
76	
77	    '
78	- name: GPT-2 Small Factual Recall K=3 CSS
79	  plan_id: plan_005
80	  description: '在 GPT-2 Small 上对 Factual Recall 任务（country→capital, e.g. "The capital
81	    of France is"）运行三种发现方法。这是一个 distributed computation 任务， 知识检索涉及多层 MLP 和跨层 attention
82	    routing，预期方法 Jaccard 中等， CSS 优势边际。
83	
84	    '
85	  expected_results:
86	    eapig_edges: 50
87	    ep_edges: 50
88	    acdc_edges_isinf: 22
89	    acdc_edges_k50: 50
90	    jaccard_eapig_ep: 0.48
91	    jaccard_eapig_acdc: 0.18
92	    jaccard_ep_acdc: 0.15
93	    max_pairwise_jaccard: 0.48
94	    three_way_ratio: 0.092
95	    css_3of3_edges: 15
96	    css_2of3_edges: 38
97	    css_1of3_edges: 69
98	    css_1.00_edges: 15
99	    css_1.00_CPR: 0.055
100	    css_1.00_CMD: 0.95
101	    css_0.67_edges: 38
102	    css_0.67_CPR: 0.04
103	    css_0.67_CMD: 0.965
104	    acdc_edges: 22
105	    acdc_CPR: 0.037
106	    acdc_CMD: 0.97
107	    eapig_k50_CPR: 0.03
108	    eapig_k50_CMD: 0.975
109	    ep_k50_CPR: 0.01
110	    ep_k50_CMD: 0.99
111	    css1_cpr_advantage: 0.018
112	    css1_edge_ratio: 0.123
113	  result_rationale: 'Factual recall 是一个 distributed computation：知识存储在中层 MLP（layer
114	    5-9） 的 key-value 机制中，而检索依赖多层 attention head 将 subject token 的 representation 路由到
115	    last token position。三种方法在 MLP 存储层的边上有较高 共识（这些边是任何方法都无法忽略的关键瓶颈），但在 attention routing
116	    边上 存在分歧——EAP-IG 偏好早期 attention head（梯度信号强），EP 保留后期 head （剪枝敏感），ACDC 选中的 head 分散在多层。这导致
117	    max Jaccard=0.48：高于 localized tasks（方法在核心 MLP 边上被迫共识），但远低于 Arithmetic（0.695） 因为
118	    routing 部分仍有显著分歧。CSS=1.0 的 15 条边捕获了 MLP 存储核心 + 最关键的 2-3 个 routing head，CPR=0.055
119	    略优于 ACDC(0.037)，但优势仅 0.018。 这符合理论预期：中等 Jaccard → 中等 CSS utility，consensus 的过滤效果被
120	    方法间部分冗余所稀释。
121	
122	    '
123	  tables:
124	  - name: 'Table: Factual Recall Circuit Discovery Summary'
125	    description: '格式同 SVA/IOI 表。CSS=1.0 的 15 条边 CPR=0.055 略优于 ACDC 的 22 条 边 CPR=0.037，但优势远小于
126	      IOI/SVA
127	
128	      '
129	  figures_description:
130	  - '与 IOI、SVA 的 CPR bar chart 并列的第三个 subplot。CSS=1.0 bar 仅略高于 ACDC bar，视觉化 CSS 优势随
131	    Jaccard 增加而递减的趋势
132	
133	    '
134	  analysis: 'Factual Recall 是论文叙事的关键 interpolation 点。它证明 CSS utility 不是 binary（有/无），而是连续的、可由
135	    Jaccard 预测的量。max Jaccard 0.48 落在 IOI(0.31) 和 Arithmetic(0.695) 之间，CSS advantage
136	    0.018 也相应落在 0.08 和 -0.066 之间。这将 Claim 2 从"两点定义的趋势"升级为"有中间插值的 连续关系"，显著增强说服力。同时，CSS=1.0
137	    的优势虽小但仍为正，使 n_tasks_css_wins 达到 3（IOI + SVA + Factual），满足 reviewer 对 majority-win
138	    的期望。
139	
140	    '
141	- name: Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + IFR)
142	  plan_id: plan_006
143	  description: '在 Qwen-2.5 0.5B 上运行 IOI，用 IFR（Iterative Feature Removal， similarity-based）替代
144	    ACDC，构成 K=3 = {EAP-IG, EP, IFR}。 IFR 来自不同算法族，预期降低 max Jaccard、维持或提升 CSS CPR。 同时验证
145	    CSS 跨模型架构（GQA, SwiGLU）的泛化性。
146	
147	    '
148	  expected_results:
149	    eapig_edges: 50
150	    ep_edges: 50
151	    ifr_edges: 50
152	    jaccard_eapig_ep: 0.28
153	    jaccard_eapig_ifr: 0.14
154	    jaccard_ep_ifr: 0.11
155	    max_pairwise_jaccard: 0.28
156	    css_3of3_edges: 10
157	    css_2of3_edges: 30
158	    css_1of3_edges: 82
159	    css_1.00_edges: 10
160	    css_1.00_CPR: 0.14
161	    css_1.00_CMD: 0.87
162	    css_0.67_edges: 30
163	    css_0.67_CPR: 0.08
164	    css_0.67_CMD: 0.93
165	    eapig_k50_CPR: 0.04
166	    ep_k50_CPR: 0.02
167	    ifr_k50_CPR: 0.05
168	    css1_cpr_advantage: 0.09
169	    max_jaccard_vs_gpt2_ioi: 0.28 ≤ 0.31 (GPT-2)
170	  result_rationale: 'IFR 通过逐步移除 feature 并测量 representation similarity 变化来评分边， 其算法逻辑与
171	    gradient-based EAP-IG 和 pruning-based EP 正交。在 Qwen 的 IOI 电路中，EAP-IG 和 EP 的 Jaccard
172	    从 GPT-2 的 0.31 降至 0.28——Qwen 的 GQA（Grouped Query Attention）使得 head 内 key-value
173	    sharing 改变了 gradient 和 pruning 的敏感度分布，两方法在 induction head 选择上出现更大 分歧。IFR 与 gradient
174	    方法的 Jaccard 极低（0.14/0.11），因为 similarity-based scoring 完全不依赖 loss gradient，而是基于
175	    intermediate representation 的 余弦距离变化。CSS=1.0 的 10 条边是三种完全不同的算法视角共同认定的 IOI 核心——name
176	    mover heads 和 S-inhibition heads 的关键边——CPR=0.14 不仅 不退化，反而高于 GPT-2 IOI 的 0.109。这验证了核心理论：方法多样性越高
177	    （更低 Jaccard），consensus 过滤越有效，CSS utility 越大。
178	
179	    '
180	  tables:
181	  - name: 'Table: Cross-Model IOI Comparison (GPT-2 vs Qwen)'
182	    description: '行: GPT-2 K=3(EAP-IG,EP,ACDC), Qwen K=3(EAP-IG,EP,IFR) 列: Max Jaccard,
183	      CSS=1.0 Edges, CSS=1.0 CPR, Best-Single CPR, Δ 突出 IFR 带来的 Jaccard 下降和 CPR 提升
184	
185	      '
186	  figures_description:
187	  - 'Paired bar chart: GPT-2 IOI vs Qwen IOI，每组有 CSS=1.0 和 best-single 两个 bar。Qwen
188	    的 CSS=1.0 bar 更高且与 best-single 的 gap 更大， 视觉化 method diversity → CSS utility 的因果链
189	
190	    '
191	  analysis: '此实验同时服务三个目标：(1) 验证 CSS 跨模型泛化（Qwen ≠ GPT-2 架构）， (2) 验证 IFR 作为第三算法族的加入降低
192	    Jaccard 并提升 CSS utility（直接回应 R3 的 K≈2 质疑），(3) 为 plan_013 提供第 5 个 Jaccard-CSS 数据点。
193	    max Jaccard 0.28 ≤ GPT-2 的 0.31，CSS CPR 0.14 > 0.109，两个指标同时 改善，是 best tier 最有力的单一证据。
194	
195	    '
196	- name: Qwen-2.5 0.5B Arithmetic K=3 (EAP-IG + EP + IFR)
197	  plan_id: plan_007
198	  description: 'Qwen 上运行 Arithmetic (Greaterthan)，IFR 替代 ACDC。测试 IFR 能否 打破 EAP-IG×EP
199	    的高 Jaccard 相关性、使 CSS 部分恢复。
200	
201	    '
202	  expected_results:
203	    jaccard_eapig_ep: 0.58
204	    jaccard_eapig_ifr: 0.28
205	    jaccard_ep_ifr: 0.24
206	    max_pairwise_jaccard: 0.58
207	    css_3of3_edges: 18
208	    css_2of3_edges: 35
209	    css_1of3_edges: 69
210	    css_1.00_CPR: 0.935
211	    eapig_k50_CPR: 0.975
212	    ep_k50_CPR: 0.95
213	    ifr_k50_CPR: 0.88
214	    css1_cpr_advantage: -0.04
215	  result_rationale: 'Arithmetic (Greaterthan) 的计算结构天然导致方法收敛：比较操作依赖一组固定的 comparison
216	    heads 和 magnitude-encoding MLPs，任何基于性能的方法都会被迫 选中这些瓶颈边。EAP-IG×EP 的 Jaccard 从 GPT-2
217	    的 0.695 降至 Qwen 的 0.58 ——Qwen 的更大模型容量和 GQA 结构使得 comparison 计算略微分散到更多 head， 降低了
218	    gradient-adjacent 的冗余。但 0.58 仍然远高于 CSS utility threshold (~0.55)。IFR 虽然作为不同族方法引入了新视角（IFR×EAP-IG=0.28），但
219	    max pairwise Jaccard 仍由 EAP-IG×EP=0.58 主导——CSS=1.0 的 filtering 效果被 两个 gradient-adjacent
220	    方法的高度共识所支配。CSS=1.0 CPR=0.935 低于 EAP-IG 的 0.975，确认 Arithmetic 在 Qwen 上仍是 CSS-negative
221	    case。 但 Jaccard 从 0.695 降至 0.58 提供了一个重要的 near-threshold 数据点， 说明 IFR 的加入确实在正确方向上推动了
222	    method diversity。
223	
224	    '
225	  tables:
226	  - name: 'Table: Arithmetic Cross-Model Comparison'
227	    description: 'GPT-2 K=3 vs Qwen K=3(with IFR)。突出 max Jaccard 从 0.695→0.58 的下降以及
228	      CSS advantage 从 -0.066 到 -0.04 的改善（趋势正确但未翻转）
229	
230	      '
231	  figures_description:
232	  - '在 Jaccard-CSS scatter plot 中，Qwen Arithmetic 的数据点落在 GPT-2 Arithmetic 的右上方（更高
233	    1-Jaccard，更小 negative advantage）， 视觉化 IFR 的正向但不充分的贡献
234	
235	    '
236	  analysis: '此实验的 negative result 实际上是论文叙事的资产而非负担。它证明：(1) Jaccard threshold 是稳健的——即使
237	    IFR 降低了 max Jaccard，只要仍高于 ~0.55， CSS 依然无效；(2) CSS utility 的 bottleneck 是 max pairwise
238	    Jaccard， 不是 average Jaccard——只要有一对方法高度相关，consensus 就会退化； (3) 为 Claim 2 提供了又一个符合预测的数据点（Spearman
239	    correlation 更稳健）。
240	
241	    '
242	- name: Gemma-2 2B IOI K=3 (EAP-IG + EP + IFR)
243	  plan_id: plan_008
244	  description: '将 CSS 扩展到 2B 参数量级模型。验证 localized circuit 模式在更大模型上是否 保持，以及 CSS faithfulness
245	    优势是否随模型规模 scale。
246	
247	    '
248	  expected_results:
249	    jaccard_eapig_ep: 0.25
250	    jaccard_eapig_ifr: 0.12
251	    jaccard_ep_ifr: 0.1
252	    max_pairwise_jaccard: 0.25
253	    css_3of3_edges: 12
254	    css_1.00_CPR: 0.13
255	    best_single_CPR: 0.04
256	    css1_cpr_advantage: 0.09
257	  result_rationale: '2B 模型的 IOI 电路比 0.5B 更分散——更多候选 head 可以承担 name mover 和 induction
258	    功能。这增加了方法间的分歧（max Jaccard 进一步降至 0.25），因为 每种方法在候选 head 中做出不同的排序选择。CSS=1.0 过滤出三种方法共同认定的
259	    12 条核心边，CPR=0.13 与 Qwen 结果一致。这证明 CSS 的 utility 不依赖于 特定模型架构或规模，而是由 method diversity（Jaccard）决定。
260	
261	    '
262	  tables:
263	  - name: 'Table: Model Scaling Summary (GPT-2 → Qwen → Gemma)'
264	    description: '三行对应三个模型，列: Params, Max Jaccard, CSS=1.0 Edges, CSS CPR, Advantage。展示
265	      CSS utility 跨模型稳定
266	
267	      '
268	  figures_description:
269	  - '补充到 cross-model bar chart 中作为第三个 subplot
270	
271	    '
272	  analysis: 'P2 优先级实验，为 camera-ready 提供额外的泛化性证据。如果 deadline 紧张 可以推迟到 revision 阶段。但如果完成，三个不同架构（GPT-2
273	    Transformer, Qwen GQA+SwiGLU, Gemma-2 sliding window）的一致结果将使 R1 泛化性 质疑几乎不可攻击。
274	
275	    '
276	- name: Llama-3.1 8B IOI K=3 (EAP-IG + EP + IFR)
277	  plan_id: plan_009
278	  description: '最大规模验证（8B）。P3 优先级，需 A100 80GB。best tier 下可能不完成， 但如果资源允许则提供 impressive
279	    scaling evidence。
280	
281	    '
282	  expected_results:
283	    max_pairwise_jaccard: 0.23
284	    css_3of3_edges: 14
285	    css_1.00_CPR: 0.12
286	    css1_cpr_advantage: 0.08
287	  result_rationale: '8B 模型有大量冗余 head，IOI 电路更分散但核心 name mover 功能仍由少量 head 主导。方法分歧进一步增加（Jaccard→0.23），CSS=1.0
288	    的 14 条边 精准锁定 consensus core。CPR=0.12 与小模型一致，说明 CSS utility 是 scale-invariant 的。EP
289	    在 8B 模型上计算量大（需 edge-level pruning on 8B），可能需要近似——如果近似引入噪声，Jaccard 可能进一步降低。
290	
291	    '
292	  tables: []
293	  figures_description:
294	  - '如果完成，加入 model scaling 图：x=model params (log scale), y=CSS CPR advantage，展示 flat
295	    trend 证明 scale invariance
296	
297	    '
298	  analysis: 'Stretch goal。如果完成，论文可以 claim CSS 在 117M→8B (68x) 范围内 稳健有效。如果未完成，Gemma-2
299	    2B 已经提供了足够的 scaling evidence。
300	
301	    '
302	- name: Top-k Binarization Sensitivity Sweep
303	  plan_id: plan_010
304	  description: '在所有已完成的 model×task 组合上系统扫描 k=50/75/100/150， 验证 CSS=1.0 CPR 对 k 选择的鲁棒性。直接回应
305	    R5。
306	
307	    '
308	  expected_results:
309	    ioi_gpt2:
310	      k50_css_edges: 7
311	      k50_css_CPR: 0.109
312	      k75_css_edges: 12
313	      k75_css_CPR: 0.102
314	      k100_css_edges: 18
315	      k100_css_CPR: 0.098
316	      k150_css_edges: 24
317	      k150_css_CPR: 0.091
318	    sva_gpt2:
319	      k50_css_edges: 8
320	      k50_css_CPR: 0.12
321	      k75_css_edges: 14
322	      k75_css_CPR: 0.11
323	      k100_css_edges: 20
324	      k100_css_CPR: 0.105
325	      k150_css_edges: 28
326	      k150_css_CPR: 0.095
327	    css_advantage_positive_across_all_k: true
328	    max_cpr_variation: 0.025
329	  result_rationale: '随着 k 增加，每个方法保留更多边，pairwise overlap 增加，CSS=1.0 集合扩大。 扩大的 CSS=1.0
330	    包含了更多低置信度的 consensus 边（三种方法在 top-50 之外 的边上的共识更可能是偶然的），因此 CPR 微降。但关键是：(1) CPR 始终为正
331	    且高于 best single method，说明 consensus core 的信号不依赖于 k 的精确选择； (2) 边数与 k 近似线性增长，说明新增的
332	    consensus 边是渐进的而非跳跃的—— 没有 critical threshold artifact。k=50 是合理的 default 选择（CPR
333	    最高）， 但 k=75-150 都给出 qualitatively identical 的结论。
334	
335	    '
336	  tables:
337	  - name: 'Table: Binarization Sensitivity (IOI + SVA)'
338	    description: '行: k=50, 75, 100, 150 + isinf baseline 列: CSS=1.0 Edges, CSS=1.0
339	      CPR, Best-Single CPR, Δ, Max Jaccard 每个 task 一个 sub-table
340	
341	      '
342	  figures_description:
343	  - 'Line plot: x=k, y=CPR, 两条线（CSS=1.0 和 best single method）。 CSS 线始终在 best-single
344	    线上方，两线间 shaded area 表示 CSS advantage。 IOI 和 SVA 各一个 subplot
345	
346	    '
347	  analysis: '此 ablation 是 R5 的完整回应。结论：CSS=1.0 的 faithfulness advantage 是 k-robust
348	    的（max variation < 0.025），实践中 k=50 是 conservative 且 sufficient 的默认值。论文可以在 Method
349	    章节推荐 k=50 并在 appendix 放 完整 sensitivity 表。
350	
351	    '
352	- name: Ablation Method Comparison (Zero vs Mean vs Resample)
353	  plan_id: plan_011
354	  description: '在 IOI 和 SVA 上比较三种 faithfulness 评估方式下的 CSS 优势稳定性。
355	
356	    '
357	  expected_results:
358	    ioi_zero:
359	      css_1.00_CPR: 0.109
360	      best_single_CPR: 0.029
361	      advantage: 0.08
362	    ioi_mean:
363	      css_1.00_CPR: 0.145
364	      best_single_CPR: 0.065
365	      advantage: 0.08
366	    ioi_resample_mean:
367	      css_1.00_CPR: 0.125
368	      best_single_CPR: 0.045
369	      advantage: 0.08
370	    ioi_resample_std: 0.018
371	    sva_zero:
372	      css_1.00_CPR: 0.12
373	      best_single_CPR: 0.03
374	      advantage: 0.09
375	    sva_mean:
376	      css_1.00_CPR: 0.155
377	      best_single_CPR: 0.065
378	      advantage: 0.09
379	    sva_resample_mean:
380	      css_1.00_CPR: 0.135
381	      best_single_CPR: 0.04
382	      advantage: 0.095
383	    advantage_stable_across_methods: true
384	    max_advantage_variation: 0.015
385	  result_rationale: '三种 ablation baseline 改变的是绝对 CPR 水平，但不改变 CSS=1.0 与 single-method
386	    之间的相对差异。Mean ablation 最温和（baseline 更接近正常 activations），所有方法的 CPR 都偏高；zero ablation
387	    最激进，CPR 整体偏低； resample 介于两者之间。CSS=1.0 的优势在三种评估下保持 Δ≈0.08-0.09， 因为 consensus 捕获的是
388	    method-independent 的核心功能边——这些边在任何 ablation scheme 下都是 critical 的。这排除了"CSS 优势是
389	    evaluation artifact" 的质疑。
390	
391	    '
392	  tables:
393	  - name: 'Table: Ablation Method Robustness'
394	    description: '行: Zero, Mean, Resample(n=10) 列: CSS=1.0 CPR, Best-Single CPR, Δ,
395	      p-value (resample) IOI 和 SVA 各一个 panel
396	
397	      '
398	  figures_description: []
399	  analysis: 'P2 实验，主要用于 appendix。如果 reviewer 质疑 evaluation protocol， 此表是 decisive
400	    response。实际上 zero ablation 是最保守的（CSS 优势最难 显现的条件），所以主实验用 zero ablation 是 methodologically
401	    conservative。
402	
403	    '
404	- name: CIRCUS vs CSS Negative Ablation
405	  plan_id: plan_012
406	  description: '系统对比 CIRCUS（threshold diversity within single method）和 CSS （cross-method
407	    consensus），证明结构共识优于单方法内部的阈值稳定性筛选。
408	
409	    '
410	  expected_results:
411	    ioi:
412	      circus_core_edges: 15
413	      circus_CPR: -0.108
414	      css_1.00_edges: 7
415	      css_1.00_CPR: 0.109
416	    sva:
417	      circus_core_edges: 12
418	      circus_CPR: -0.025
419	      css_1.00_edges: 8
420	      css_1.00_CPR: 0.12
421	    factual:
422	      circus_core_edges: 18
423	      circus_CPR: -0.015
424	      css_1.00_edges: 15
425	      css_1.00_CPR: 0.055
426	    circus_negative_on_all_tasks: true
427	  result_rationale: 'CIRCUS 通过扫描 EAP-IG 的阈值范围，选取在不同阈值下始终存在的"核心"边。 这些边确实是 EAP-IG 得分最高且最稳定的边——但它们仍然是
428	    EAP-IG 的 method-specific 视角。当 EAP-IG 本身存在系统性偏差（如过度依赖 early layer attention head
429	    的 gradient signal），CIRCUS 只会放大这种偏差而非 纠正它。IOI 上 CIRCUS CPR=-0.108 说明 EAP-IG 的"最确定"边恰恰是
430	    破坏性最大的（这些边可能是 EAP-IG gradient 信号的 artifact，不对应 真正的功能电路）。CSS=1.0 通过要求多方法共识，天然过滤掉了任何单方法的
431	    系统性偏差。在所有三个 CSS-positive 的任务上，CIRCUS CPR 均为负值， 而 CSS CPR 均为正值——这是 cross-method
432	    consensus 优于 within-method robustness 的 decisive evidence。
433	
434	    '
435	  tables:
436	  - name: 'Table: CIRCUS vs CSS Head-to-Head'
437	    description: '行: IOI, SVA, Factual Recall 列: Method, Edges, CPR, CMD 每个任务两行：CIRCUS
438	      core 和 CSS=1.0
439	
440	      '
441	  figures_description:
442	  - 'Grouped bar chart: 三个任务，每组两个 bar（CIRCUS 灰色，CSS=1.0 蓝色）。 CIRCUS bar 全部在 y=0 以下，CSS
443	    bar 全部在 y=0 以上，视觉冲击力强
444	
445	    '
446	  analysis: '此 negative ablation 是对 competitor CIRCUS (Parekh 2026) 的直接回应， 也从理论上论证了
447	    cross-method consensus 的必要性。即使 CIRCUS 在 Parekh 的原始 setting 中有效，它的 single-method
448	    assumption 使其在 CSS 的 framing 下天然处于劣势。此结果可以放在 Related Work 中用一段话 + 一个表来展示。
449	
450	    '
451	- name: Jaccard-CSS Utility Correlation Analysis
452	  plan_id: plan_013
453	  description: '汇总所有 model×task 组合的 (max pairwise Jaccard) 和 (CSS CPR advantage)，
454	    计算 Spearman 相关系数，拟合 CSS utility threshold。这是 Claim 2 的 definitive evidence。
455	
456	    '
457	  expected_results:
458	    data_points:
459	    - task: SVA (GPT-2)
460	      max_jaccard: 0.22
461	      one_minus_jaccard: 0.78
462	      css_cpr_advantage: 0.09
463	    - task: IOI (Qwen+IFR)
464	      max_jaccard: 0.28
465	      one_minus_jaccard: 0.72
466	      css_cpr_advantage: 0.09
467	    - task: IOI (GPT-2)
468	      max_jaccard: 0.31
469	      one_minus_jaccard: 0.69
470	      css_cpr_advantage: 0.08
471	    - task: Factual (GPT-2)
472	      max_jaccard: 0.48
473	      one_minus_jaccard: 0.52
474	      css_cpr_advantage: 0.018
475	    - task: Arithmetic (Qwen+IFR)
476	      max_jaccard: 0.58
477	      one_minus_jaccard: 0.42
478	      css_cpr_advantage: -0.04
479	    - task: Arithmetic (GPT-2)
480	      max_jaccard: 0.695
481	      one_minus_jaccard: 0.305
482	      css_cpr_advantage: -0.066
483	    spearman_rho: 0.94
484	    spearman_p: 0.005
485	    n_data_points: 6
486	    fitted_threshold: 0.53
487	    threshold_ci_95:
488	    - 0.48
489	    - 0.58
490	    spearman_rho_4task: 1.0
491	    spearman_p_4task: 0.042
492	  result_rationale: '(1-max_Jaccard) 与 CSS_CPR_advantage 的 Spearman ρ=0.94 (p=0.005)
493	    证明 方法多样性是 CSS utility 的强预测因子。这不是偶然的——有清晰的机械解释： 当三种方法独立发现不同的边集（低 Jaccard），它们的交集代表被多种不同算法
494	    视角共同验证的功能核心，这些边大概率是 true circuit edges 而非 method artifacts。当方法高度相关（高 Jaccard），交集趋近于最
495	    selective 的单方法 结果，共识不再增加信息量。 fitted threshold ≈ 0.53 意味着：如果三种发现方法的 max pairwise
496	    Jaccard < 0.53，使用 CSS=1.0 consensus 可以预期 faithfulness 提升；如果 > 0.53， 应直接使用性能最好的单方法。这是一个可操作的
497	    meta-diagnostic guideline。 6 个数据点覆盖了 Jaccard 0.22-0.695 的完整区间，包括 2 个模型、4 个任务，
498	    关系的稳健性已足够说服 reviewer。
499	
500	    '
501	  tables:
502	  - name: 'Table: Jaccard-CSS Correlation Data'
503	    description: '行: 6 个 model×task 组合 列: Task, Model, Methods, Max Jaccard, CSS=1.0
504	      CPR, Best-Single CPR, Δ(advantage), CSS=1.0 Edges 底部: Spearman ρ=0.94, p=0.005
505	
506	      '
507	  figures_description:
508	  - '核心 Figure（可能是 Figure 3 或 4）：Scatter plot，x 轴 = 1-max_Jaccard (method diversity),
509	    y 轴 = CSS CPR advantage。6 个点，颜色区分模型 （GPT-2 蓝色, Qwen 橙色），形状区分任务类型（圆=localized,
510	    三角=distributed）。 灰色虚线 y=0 分隔 CSS-positive 和 CSS-negative 区域。拟合线斜率为正。 右上角标注 ρ=0.94,
511	    p=0.005。垂直虚线标注 Jaccard threshold ≈ 0.53。 这可能是全文最重要的图——将整个叙事浓缩为一张可视化
512	
513	    '
514	  analysis: '此分析是论文的 crown jewel。6 个数据点虽然不多，但覆盖了 localized→distributed spectrum 和两个模型架构，Spearman
515	    ρ=0.94 在 p=0.005 下显著。Jaccard threshold ≈ 0.53 提供了 actionable guideline——这是 reviewer
516	    最希望看到的 practical contribution。仅用 4 个 GPT-2 任务时 ρ=1.0 但 p=0.042（4 个点的 perfect rank
517	    correlation 仍然 marginal），加入 Qwen 数据使 p 降至 0.005， 大幅增强统计说服力。建议论文主文放 4-task 分析（因为更
518	    clean），appendix 放 6-point 分析（加入跨模型验证）。
519	
520	    对 reviewer R1（泛化性）的回应：4 个任务覆盖 localized (SVA, IOI) 和 distributed (Factual, Arithmetic)，2
521	    个模型覆盖不同架构——足以建立 pattern。 对 reviewer R3（K≈2）的回应：IFR 的引入使 Qwen 数据点落在 GPT-2 趋势线上，
522	    证明 method diversity（而非特定方法组合）是 CSS utility 的决定因素。'
523	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39105855-045e-49c3-9f6c-c3636f328fd9",
  "isSidechain": false,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "type": "user",
  "uuid": "1bdeca9f-493e-44f2-8edc-2916aa59df6c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/best/imagined_experiments.yaml",
      "content": "tier: best\nnarrative_guidance: '原始 reframed claim 完整成立。四个任务（IOI、SVA、Factual Recall、Arithmetic）覆盖\n  localized→distributed 全谱，Jaccard 作为 CSS utility 的 meta-diagnostic 是 novel 且 quantitatively\n  validated 的 contribution。SVA 清晰复现 IOI 模式（低 Jaccard、CSS 优势显著）， Factual Recall 提供关键\n  interpolation 数据点（中等 Jaccard、CSS 优势边际正），Arithmetic 作为 principled negative case 完善图景。IFR\n  第四方法族在 Qwen 上进一步降低 max Jaccard， CSS=1.0 CPR 不退化甚至提升，直接回应 R3（K≈2 质疑）。Spearman ρ=0.94\n  跨 6 个 model×task 组合成立，p=0.005，统计上无争议。论文叙事可以自信地以 Jaccard threshold (~0.55) 作为 practitioner\n  guideline 收尾。\n\n  '\nimagined_experiments:\n- name: GPT-2 Small Subject-Verb Agreement K=3 CSS\n  plan_id: plan_004\n  description: '在 GPT-2 Small 上对 Subject-Verb Agreement (SVA) 任务运行三种发现方法 （EAP-IG,\n    EP, ACDC），计算 CSS 分布和 faithfulness。SVA 是经典的 localized circuit 任务，核心计算集中在 layer\n    7-10 的 number-tracking attention heads，预期方法间 Jaccard 低、CSS 优势显著。\n\n    '\n  expected_results:\n    eapig_edges: 50\n    ep_edges: 50\n    acdc_edges_isinf: 12\n    acdc_edges_k50: 50\n    jaccard_eapig_ep: 0.22\n    jaccard_eapig_acdc: 0.08\n    jaccard_ep_acdc: 0.06\n    max_pairwise_jaccard: 0.22\n    three_way_ratio: 0.032\n    css_3of3_edges: 8\n    css_2of3_edges: 31\n    css_1of3_edges: 73\n    css_1.00_edges: 8\n    css_1.00_CPR: 0.12\n    css_1.00_CMD: 0.89\n    css_0.67_edges: 31\n    css_0.67_CPR: 0.065\n    css_0.67_CMD: 0.945\n    acdc_edges: 12\n    acdc_CPR: 0.03\n    acdc_CMD: 0.975\n    eapig_k50_CPR: -0.04\n    eapig_k50_CMD: 1.05\n    ep_k50_CPR: -0.07\n    ep_k50_CMD: 1.08\n    css1_cpr_advantage: 0.09\n    css1_edge_ratio: 0.071\n  result_rationale: 'SVA 在 GPT-2 Small 中依赖 layer 7-10 中约 5-8 个专门追踪主语数特征的 attention\n    head。这是一个高度 localized 的电路：关键计算集中在少量 head 的 Q-K 匹配上。三种方法各自从不同角度发现该电路的不同子集——EAP-IG\n    沿梯度 路径优先选取高 ∂L/∂e 的边，EP 通过逐步剪枝保留移除后损失最大的边，ACDC 通过激活差异识别 clean vs corrupt 下变化最大的边。由于电路\n    localized，每种 方法只需少量边即可捕获核心功能，导致三组 top-50 edge set 的交集稀疏（max Jaccard=0.22）。CSS=1.0\n    恰好捕获了所有三种方法共同认定的 8 条核心边—— 这些边对应 number-agreement 的关键 attention pattern，移除它们会破坏\n    subject→verb 的 number propagation，因此 CPR=0.12 显著高于任何单方法。 ACDC 的 12 条 isinf 边虽然也\n    localized，但包含了 4 条 ACDC 特有的 method-specific 边（其他方法未选中），导致部分噪声稀释了 faithfulness。\n\n    '\n  tables:\n  - name: 'Table: SVA Circuit Discovery Summary'\n    description: '行: EAP-IG(k=50), EP(k=50), ACDC(isinf), CSS≥2/3, CSS=1.0 列: Edges,\n      CPR, CMD, vs-best-single-Δ 展示 CSS=1.0 在仅 8 条边下达到 CPR=0.12，是 ACDC(0.03) 的 4 倍\n\n      '\n  - name: 'Table: SVA Pairwise Jaccard Matrix'\n    description: '3×3 对称矩阵，对角线为 1.0。EAP-IG×EP=0.22, EAP-IG×ACDC=0.08, EP×ACDC=0.06。与\n      IOI 的 Jaccard 矩阵并列展示，突出 SVA 更低的 inter-method correlation\n\n      '\n  figures_description:\n  - 'Bar chart: x 轴为方法（EAP-IG, EP, ACDC, CSS≥2/3, CSS=1.0）， y 轴为 CPR。CSS=1.0 bar 显著高于其他所有方法，上方标注\n    edge count。 与 IOI 对应图并列为 subplot，视觉化 CSS 优势在 localized tasks 上的复现\n\n    '\n  analysis: 'SVA 完美复现 IOI 的核心模式：localized circuit → low Jaccard → CSS=1.0 faithfulness\n    优势。max Jaccard 0.22 甚至低于 IOI 的 0.31，反映 SVA 电路更 集中（fewer critical heads），使方法分歧更大。CSS\n    CPR advantage 0.09 与 IOI 的 0.08 一致，支撑 Claim 1。此结果将 Claim 1 的支持从 1 个任务扩展到 2 个，\n    直接削弱 R1 泛化性质疑。\n\n    '\n- name: GPT-2 Small Factual Recall K=3 CSS\n  plan_id: plan_005\n  description: '在 GPT-2 Small 上对 Factual Recall 任务（country→capital, e.g. \"The capital\n    of France is\"）运行三种发现方法。这是一个 distributed computation 任务， 知识检索涉及多层 MLP 和跨层 attention\n    routing，预期方法 Jaccard 中等， CSS 优势边际。\n\n    '\n  expected_results:\n    eapig_edges: 50\n    ep_edges: 50\n    acdc_edges_isinf: 22\n    acdc_edges_k50: 50\n    jaccard_eapig_ep: 0.48\n    jaccard_eapig_acdc: 0.18\n    jaccard_ep_acdc: 0.15\n    max_pairwise_jaccard: 0.48\n    three_way_ratio: 0.092\n    css_3of3_edges: 15\n    css_2of3_edges: 38\n    css_1of3_edges: 69\n    css_1.00_edges: 15\n    css_1.00_CPR: 0.055\n    css_1.00_CMD: 0.95\n    css_0.67_edges: 38\n    css_0.67_CPR: 0.04\n    css_0.67_CMD: 0.965\n    acdc_edges: 22\n    acdc_CPR: 0.037\n    acdc_CMD: 0.97\n    eapig_k50_CPR: 0.03\n    eapig_k50_CMD: 0.975\n    ep_k50_CPR: 0.01\n    ep_k50_CMD: 0.99\n    css1_cpr_advantage: 0.018\n    css1_edge_ratio: 0.123\n  result_rationale: 'Factual recall 是一个 distributed computation：知识存储在中层 MLP（layer\n    5-9） 的 key-value 机制中，而检索依赖多层 attention head 将 subject token 的 representation 路由到\n    last token position。三种方法在 MLP 存储层的边上有较高 共识（这些边是任何方法都无法忽略的关键瓶颈），但在 attention routing\n    边上 存在分歧——EAP-IG 偏好早期 attention head（梯度信号强），EP 保留后期 head （剪枝敏感），ACDC 选中的 head 分散在多层。这导致\n    max Jaccard=0.48：高于 localized tasks（方法在核心 MLP 边上被迫共识），但远低于 Arithmetic（0.695） 因为\n    routing 部分仍有显著分歧。CSS=1.0 的 15 条边捕获了 MLP 存储核心 + 最关键的 2-3 个 routing head，CPR=0.055\n    略优于 ACDC(0.037)，但优势仅 0.018。 这符合理论预期：中等 Jaccard → 中等 CSS utility，consensus 的过滤效果被\n    方法间部分冗余所稀释。\n\n    '\n  tables:\n  - name: 'Table: Factual Recall Circuit Discovery Summary'\n    description: '格式同 SVA/IOI 表。CSS=1.0 的 15 条边 CPR=0.055 略优于 ACDC 的 22 条 边 CPR=0.037，但优势远小于\n      IOI/SVA\n\n      '\n  figures_description:\n  - '与 IOI、SVA 的 CPR bar chart 并列的第三个 subplot。CSS=1.0 bar 仅略高于 ACDC bar，视觉化 CSS 优势随\n    Jaccard 增加而递减的趋势\n\n    '\n  analysis: 'Factual Recall 是论文叙事的关键 interpolation 点。它证明 CSS utility 不是 binary（有/无），而是连续的、可由\n    Jaccard 预测的量。max Jaccard 0.48 落在 IOI(0.31) 和 Arithmetic(0.695) 之间，CSS advantage\n    0.018 也相应落在 0.08 和 -0.066 之间。这将 Claim 2 从\"两点定义的趋势\"升级为\"有中间插值的 连续关系\"，显著增强说服力。同时，CSS=1.0\n    的优势虽小但仍为正，使 n_tasks_css_wins 达到 3（IOI + SVA + Factual），满足 reviewer 对 majority-win\n    的期望。\n\n    '\n- name: Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + IFR)\n  plan_id: plan_006\n  description: '在 Qwen-2.5 0.5B 上运行 IOI，用 IFR（Iterative Feature Removal， similarity-based）替代\n    ACDC，构成 K=3 = {EAP-IG, EP, IFR}。 IFR 来自不同算法族，预期降低 max Jaccard、维持或提升 CSS CPR。 同时验证\n    CSS 跨模型架构（GQA, SwiGLU）的泛化性。\n\n    '\n  expected_results:\n    eapig_edges: 50\n    ep_edges: 50\n    ifr_edges: 50\n    jaccard_eapig_ep: 0.28\n    jaccard_eapig_ifr: 0.14\n    jaccard_ep_ifr: 0.11\n    max_pairwise_jaccard: 0.28\n    css_3of3_edges: 10\n    css_2of3_edges: 30\n    css_1of3_edges: 82\n    css_1.00_edges: 10\n    css_1.00_CPR: 0.14\n    css_1.00_CMD: 0.87\n    css_0.67_edges: 30\n    css_0.67_CPR: 0.08\n    css_0.67_CMD: 0.93\n    eapig_k50_CPR: 0.04\n    ep_k50_CPR: 0.02\n    ifr_k50_CPR: 0.05\n    css1_cpr_advantage: 0.09\n    max_jaccard_vs_gpt2_ioi: 0.28 ≤ 0.31 (GPT-2)\n  result_rationale: 'IFR 通过逐步移除 feature 并测量 representation similarity 变化来评分边， 其算法逻辑与\n    gradient-based EAP-IG 和 pruning-based EP 正交。在 Qwen 的 IOI 电路中，EAP-IG 和 EP 的 Jaccard\n    从 GPT-2 的 0.31 降至 0.28——Qwen 的 GQA（Grouped Query Attention）使得 head 内 key-value\n    sharing 改变了 gradient 和 pruning 的敏感度分布，两方法在 induction head 选择上出现更大 分歧。IFR 与 gradient\n    方法的 Jaccard 极低（0.14/0.11），因为 similarity-based scoring 完全不依赖 loss gradient，而是基于\n    intermediate representation 的 余弦距离变化。CSS=1.0 的 10 条边是三种完全不同的算法视角共同认定的 IOI 核心——name\n    mover heads 和 S-inhibition heads 的关键边——CPR=0.14 不仅 不退化，反而高于 GPT-2 IOI 的 0.109。这验证了核心理论：方法多样性越高\n    （更低 Jaccard），consensus 过滤越有效，CSS utility 越大。\n\n    '\n  tables:\n  - name: 'Table: Cross-Model IOI Comparison (GPT-2 vs Qwen)'\n    description: '行: GPT-2 K=3(EAP-IG,EP,ACDC), Qwen K=3(EAP-IG,EP,IFR) 列: Max Jaccard,\n      CSS=1.0 Edges, CSS=1.0 CPR, Best-Single CPR, Δ 突出 IFR 带来的 Jaccard 下降和 CPR 提升\n\n      '\n  figures_description:\n  - 'Paired bar chart: GPT-2 IOI vs Qwen IOI，每组有 CSS=1.0 和 best-single 两个 bar。Qwen\n    的 CSS=1.0 bar 更高且与 best-single 的 gap 更大， 视觉化 method diversity → CSS utility 的因果链\n\n    '\n  analysis: '此实验同时服务三个目标：(1) 验证 CSS 跨模型泛化（Qwen ≠ GPT-2 架构）， (2) 验证 IFR 作为第三算法族的加入降低\n    Jaccard 并提升 CSS utility（直接回应 R3 的 K≈2 质疑），(3) 为 plan_013 提供第 5 个 Jaccard-CSS 数据点。\n    max Jaccard 0.28 ≤ GPT-2 的 0.31，CSS CPR 0.14 > 0.109，两个指标同时 改善，是 best tier 最有力的单一证据。\n\n    '\n- name: Qwen-2.5 0.5B Arithmetic K=3 (EAP-IG + EP + IFR)\n  plan_id: plan_007\n  description: 'Qwen 上运行 Arithmetic (Greaterthan)，IFR 替代 ACDC。测试 IFR 能否 打破 EAP-IG×EP\n    的高 Jaccard 相关性、使 CSS 部分恢复。\n\n    '\n  expected_results:\n    jaccard_eapig_ep: 0.58\n    jaccard_eapig_ifr: 0.28\n    jaccard_ep_ifr: 0.24\n    max_pairwise_jaccard: 0.58\n    css_3of3_edges: 18\n    css_2of3_edges: 35\n    css_1of3_edges: 69\n    css_1.00_CPR: 0.935\n    eapig_k50_CPR: 0.975\n    ep_k50_CPR: 0.95\n    ifr_k50_CPR: 0.88\n    css1_cpr_advantage: -0.04\n  result_rationale: 'Arithmetic (Greaterthan) 的计算结构天然导致方法收敛：比较操作依赖一组固定的 comparison\n    heads 和 magnitude-encoding MLPs，任何基于性能的方法都会被迫 选中这些瓶颈边。EAP-IG×EP 的 Jaccard 从 GPT-2\n    的 0.695 降至 Qwen 的 0.58 ——Qwen 的更大模型容量和 GQA 结构使得 comparison 计算略微分散到更多 head， 降低了\n    gradient-adjacent 的冗余。但 0.58 仍然远高于 CSS utility threshold (~0.55)。IFR 虽然作为不同族方法引入了新视角（IFR×EAP-IG=0.28），但\n    max pairwise Jaccard 仍由 EAP-IG×EP=0.58 主导——CSS=1.0 的 filtering 效果被 两个 gradient-adjacent\n    方法的高度共识所支配。CSS=1.0 CPR=0.935 低于 EAP-IG 的 0.975，确认 Arithmetic 在 Qwen 上仍是 CSS-negative\n    case。 但 Jaccard 从 0.695 降至 0.58 提供了一个重要的 near-threshold 数据点， 说明 IFR 的加入确实在正确方向上推动了\n    method diversity。\n\n    '\n  tables:\n  - name: 'Table: Arithmetic Cross-Model Comparison'\n    description: 'GPT-2 K=3 vs Qwen K=3(with IFR)。突出 max Jaccard 从 0.695→0.58 的下降以及\n      CSS advantage 从 -0.066 到 -0.04 的改善（趋势正确但未翻转）\n\n      '\n  figures_description:\n  - '在 Jaccard-CSS scatter plot 中，Qwen Arithmetic 的数据点落在 GPT-2 Arithmetic 的右上方（更高\n    1-Jaccard，更小 negative advantage）， 视觉化 IFR 的正向但不充分的贡献\n\n    '\n  analysis: '此实验的 negative result 实际上是论文叙事的资产而非负担。它证明：(1) Jaccard threshold 是稳健的——即使\n    IFR 降低了 max Jaccard，只要仍高于 ~0.55， CSS 依然无效；(2) CSS utility 的 bottleneck 是 max pairwise\n    Jaccard， 不是 average Jaccard——只要有一对方法高度相关，consensus 就会退化； (3) 为 Claim 2 提供了又一个符合预测的数据点（Spearman\n    correlation 更稳健）。\n\n    '\n- name: Gemma-2 2B IOI K=3 (EAP-IG + EP + IFR)\n  plan_id: plan_008\n  description: '将 CSS 扩展到 2B 参数量级模型。验证 localized circuit 模式在更大模型上是否 保持，以及 CSS faithfulness\n    优势是否随模型规模 scale。\n\n    '\n  expected_results:\n    jaccard_eapig_ep: 0.25\n    jaccard_eapig_ifr: 0.12\n    jaccard_ep_ifr: 0.1\n    max_pairwise_jaccard: 0.25\n    css_3of3_edges: 12\n    css_1.00_CPR: 0.13\n    best_single_CPR: 0.04\n    css1_cpr_advantage: 0.09\n  result_rationale: '2B 模型的 IOI 电路比 0.5B 更分散——更多候选 head 可以承担 name mover 和 induction\n    功能。这增加了方法间的分歧（max Jaccard 进一步降至 0.25），因为 每种方法在候选 head 中做出不同的排序选择。CSS=1.0 过滤出三种方法共同认定的\n    12 条核心边，CPR=0.13 与 Qwen 结果一致。这证明 CSS 的 utility 不依赖于 特定模型架构或规模，而是由 method diversity（Jaccard）决定。\n\n    '\n  tables:\n  - name: 'Table: Model Scaling Summary (GPT-2 → Qwen → Gemma)'\n    description: '三行对应三个模型，列: Params, Max Jaccard, CSS=1.0 Edges, CSS CPR, Advantage。展示\n      CSS utility 跨模型稳定\n\n      '\n  figures_description:\n  - '补充到 cross-model bar chart 中作为第三个 subplot\n\n    '\n  analysis: 'P2 优先级实验，为 camera-ready 提供额外的泛化性证据。如果 deadline 紧张 可以推迟到 revision 阶段。但如果完成，三个不同架构（GPT-2\n    Transformer, Qwen GQA+SwiGLU, Gemma-2 sliding window）的一致结果将使 R1 泛化性 质疑几乎不可攻击。\n\n    '\n- name: Llama-3.1 8B IOI K=3 (EAP-IG + EP + IFR)\n  plan_id: plan_009\n  description: '最大规模验证（8B）。P3 优先级，需 A100 80GB。best tier 下可能不完成， 但如果资源允许则提供 impressive\n    scaling evidence。\n\n    '\n  expected_results:\n    max_pairwise_jaccard: 0.23\n    css_3of3_edges: 14\n    css_1.00_CPR: 0.12\n    css1_cpr_advantage: 0.08\n  result_rationale: '8B 模型有大量冗余 head，IOI 电路更分散但核心 name mover 功能仍由少量 head 主导。方法分歧进一步增加（Jaccard→0.23），CSS=1.0\n    的 14 条边 精准锁定 consensus core。CPR=0.12 与小模型一致，说明 CSS utility 是 scale-invariant 的。EP\n    在 8B 模型上计算量大（需 edge-level pruning on 8B），可能需要近似——如果近似引入噪声，Jaccard 可能进一步降低。\n\n    '\n  tables: []\n  figures_description:\n  - '如果完成，加入 model scaling 图：x=model params (log scale), y=CSS CPR advantage，展示 flat\n    trend 证明 scale invariance\n\n    '\n  analysis: 'Stretch goal。如果完成，论文可以 claim CSS 在 117M→8B (68x) 范围内 稳健有效。如果未完成，Gemma-2\n    2B 已经提供了足够的 scaling evidence。\n\n    '\n- name: Top-k Binarization Sensitivity Sweep\n  plan_id: plan_010\n  description: '在所有已完成的 model×task 组合上系统扫描 k=50/75/100/150， 验证 CSS=1.0 CPR 对 k 选择的鲁棒性。直接回应\n    R5。\n\n    '\n  expected_results:\n    ioi_gpt2:\n      k50_css_edges: 7\n      k50_css_CPR: 0.109\n      k75_css_edges: 12\n      k75_css_CPR: 0.102\n      k100_css_edges: 18\n      k100_css_CPR: 0.098\n      k150_css_edges: 24\n      k150_css_CPR: 0.091\n    sva_gpt2:\n      k50_css_edges: 8\n      k50_css_CPR: 0.12\n      k75_css_edges: 14\n      k75_css_CPR: 0.11\n      k100_css_edges: 20\n      k100_css_CPR: 0.105\n      k150_css_edges: 28\n      k150_css_CPR: 0.095\n    css_advantage_positive_across_all_k: true\n    max_cpr_variation: 0.025\n  result_rationale: '随着 k 增加，每个方法保留更多边，pairwise overlap 增加，CSS=1.0 集合扩大。 扩大的 CSS=1.0\n    包含了更多低置信度的 consensus 边（三种方法在 top-50 之外 的边上的共识更可能是偶然的），因此 CPR 微降。但关键是：(1) CPR 始终为正\n    且高于 best single method，说明 consensus core 的信号不依赖于 k 的精确选择； (2) 边数与 k 近似线性增长，说明新增的\n    consensus 边是渐进的而非跳跃的—— 没有 critical threshold artifact。k=50 是合理的 default 选择（CPR\n    最高）， 但 k=75-150 都给出 qualitatively identical 的结论。\n\n    '\n  tables:\n  - name: 'Table: Binarization Sensitivity (IOI + SVA)'\n    description: '行: k=50, 75, 100, 150 + isinf baseline 列: CSS=1.0 Edges, CSS=1.0\n      CPR, Best-Single CPR, Δ, Max Jaccard 每个 task 一个 sub-table\n\n      '\n  figures_description:\n  - 'Line plot: x=k, y=CPR, 两条线（CSS=1.0 和 best single method）。 CSS 线始终在 best-single\n    线上方，两线间 shaded area 表示 CSS advantage。 IOI 和 SVA 各一个 subplot\n\n    '\n  analysis: '此 ablation 是 R5 的完整回应。结论：CSS=1.0 的 faithfulness advantage 是 k-robust\n    的（max variation < 0.025），实践中 k=50 是 conservative 且 sufficient 的默认值。论文可以在 Method\n    章节推荐 k=50 并在 appendix 放 完整 sensitivity 表。\n\n    '\n- name: Ablation Method Comparison (Zero vs Mean vs Resample)\n  plan_id: plan_011\n  description: '在 IOI 和 SVA 上比较三种 faithfulness 评估方式下的 CSS 优势稳定性。\n\n    '\n  expected_results:\n    ioi_zero:\n      css_1.00_CPR: 0.109\n      best_single_CPR: 0.029\n      advantage: 0.08\n    ioi_mean:\n      css_1.00_CPR: 0.145\n      best_single_CPR: 0.065\n      advantage: 0.08\n    ioi_resample_mean:\n      css_1.00_CPR: 0.125\n      best_single_CPR: 0.045\n      advantage: 0.08\n    ioi_resample_std: 0.018\n    sva_zero:\n      css_1.00_CPR: 0.12\n      best_single_CPR: 0.03\n      advantage: 0.09\n    sva_mean:\n      css_1.00_CPR: 0.155\n      best_single_CPR: 0.065\n      advantage: 0.09\n    sva_resample_mean:\n      css_1.00_CPR: 0.135\n      best_single_CPR: 0.04\n      advantage: 0.095\n    advantage_stable_across_methods: true\n    max_advantage_variation: 0.015\n  result_rationale: '三种 ablation baseline 改变的是绝对 CPR 水平，但不改变 CSS=1.0 与 single-method\n    之间的相对差异。Mean ablation 最温和（baseline 更接近正常 activations），所有方法的 CPR 都偏高；zero ablation\n    最激进，CPR 整体偏低； resample 介于两者之间。CSS=1.0 的优势在三种评估下保持 Δ≈0.08-0.09， 因为 consensus 捕获的是\n    method-independent 的核心功能边——这些边在任何 ablation scheme 下都是 critical 的。这排除了\"CSS 优势是\n    evaluation artifact\" 的质疑。\n\n    '\n  tables:\n  - name: 'Table: Ablation Method Robustness'\n    description: '行: Zero, Mean, Resample(n=10) 列: CSS=1.0 CPR, Best-Single CPR, Δ,\n      p-value (resample) IOI 和 SVA 各一个 panel\n\n      '\n  figures_description: []\n  analysis: 'P2 实验，主要用于 appendix。如果 reviewer 质疑 evaluation protocol， 此表是 decisive\n    response。实际上 zero ablation 是最保守的（CSS 优势最难 显现的条件），所以主实验用 zero ablation 是 methodologically\n    conservative。\n\n    '\n- name: CIRCUS vs CSS Negative Ablation\n  plan_id: plan_012\n  description: '系统对比 CIRCUS（threshold diversity within single method）和 CSS （cross-method\n    consensus），证明结构共识优于单方法内部的阈值稳定性筛选。\n\n    '\n  expected_results:\n    ioi:\n      circus_core_edges: 15\n      circus_CPR: -0.108\n      css_1.00_edges: 7\n      css_1.00_CPR: 0.109\n    sva:\n      circus_core_edges: 12\n      circus_CPR: -0.025\n      css_1.00_edges: 8\n      css_1.00_CPR: 0.12\n    factual:\n      circus_core_edges: 18\n      circus_CPR: -0.015\n      css_1.00_edges: 15\n      css_1.00_CPR: 0.055\n    circus_negative_on_all_tasks: true\n  result_rationale: 'CIRCUS 通过扫描 EAP-IG 的阈值范围，选取在不同阈值下始终存在的\"核心\"边。 这些边确实是 EAP-IG 得分最高且最稳定的边——但它们仍然是\n    EAP-IG 的 method-specific 视角。当 EAP-IG 本身存在系统性偏差（如过度依赖 early layer attention head\n    的 gradient signal），CIRCUS 只会放大这种偏差而非 纠正它。IOI 上 CIRCUS CPR=-0.108 说明 EAP-IG 的\"最确定\"边恰恰是\n    破坏性最大的（这些边可能是 EAP-IG gradient 信号的 artifact，不对应 真正的功能电路）。CSS=1.0 通过要求多方法共识，天然过滤掉了任何单方法的\n    系统性偏差。在所有三个 CSS-positive 的任务上，CIRCUS CPR 均为负值， 而 CSS CPR 均为正值——这是 cross-method\n    consensus 优于 within-method robustness 的 decisive evidence。\n\n    '\n  tables:\n  - name: 'Table: CIRCUS vs CSS Head-to-Head'\n    description: '行: IOI, SVA, Factual Recall 列: Method, Edges, CPR, CMD 每个任务两行：CIRCUS\n      core 和 CSS=1.0\n\n      '\n  figures_description:\n  - 'Grouped bar chart: 三个任务，每组两个 bar（CIRCUS 灰色，CSS=1.0 蓝色）。 CIRCUS bar 全部在 y=0 以下，CSS\n    bar 全部在 y=0 以上，视觉冲击力强\n\n    '\n  analysis: '此 negative ablation 是对 competitor CIRCUS (Parekh 2026) 的直接回应， 也从理论上论证了\n    cross-method consensus 的必要性。即使 CIRCUS 在 Parekh 的原始 setting 中有效，它的 single-method\n    assumption 使其在 CSS 的 framing 下天然处于劣势。此结果可以放在 Related Work 中用一段话 + 一个表来展示。\n\n    '\n- name: Jaccard-CSS Utility Correlation Analysis\n  plan_id: plan_013\n  description: '汇总所有 model×task 组合的 (max pairwise Jaccard) 和 (CSS CPR advantage)，\n    计算 Spearman 相关系数，拟合 CSS utility threshold。这是 Claim 2 的 definitive evidence。\n\n    '\n  expected_results:\n    data_points:\n    - task: SVA (GPT-2)\n      max_jaccard: 0.22\n      one_minus_jaccard: 0.78\n      css_cpr_advantage: 0.09\n    - task: IOI (Qwen+IFR)\n      max_jaccard: 0.28\n      one_minus_jaccard: 0.72\n      css_cpr_advantage: 0.09\n    - task: IOI (GPT-2)\n      max_jaccard: 0.31\n      one_minus_jaccard: 0.69\n      css_cpr_advantage: 0.08\n    - task: Factual (GPT-2)\n      max_jaccard: 0.48\n      one_minus_jaccard: 0.52\n      css_cpr_advantage: 0.018\n    - task: Arithmetic (Qwen+IFR)\n      max_jaccard: 0.58\n      one_minus_jaccard: 0.42\n      css_cpr_advantage: -0.04\n    - task: Arithmetic (GPT-2)\n      max_jaccard: 0.695\n      one_minus_jaccard: 0.305\n      css_cpr_advantage: -0.066\n    spearman_rho: 0.94\n    spearman_p: 0.005\n    n_data_points: 6\n    fitted_threshold: 0.53\n    threshold_ci_95:\n    - 0.48\n    - 0.58\n    spearman_rho_4task: 1.0\n    spearman_p_4task: 0.042\n  result_rationale: '(1-max_Jaccard) 与 CSS_CPR_advantage 的 Spearman ρ=0.94 (p=0.005)\n    证明 方法多样性是 CSS utility 的强预测因子。这不是偶然的——有清晰的机械解释： 当三种方法独立发现不同的边集（低 Jaccard），它们的交集代表被多种不同算法\n    视角共同验证的功能核心，这些边大概率是 true circuit edges 而非 method artifacts。当方法高度相关（高 Jaccard），交集趋近于最\n    selective 的单方法 结果，共识不再增加信息量。 fitted threshold ≈ 0.53 意味着：如果三种发现方法的 max pairwise\n    Jaccard < 0.53，使用 CSS=1.0 consensus 可以预期 faithfulness 提升；如果 > 0.53， 应直接使用性能最好的单方法。这是一个可操作的\n    meta-diagnostic guideline。 6 个数据点覆盖了 Jaccard 0.22-0.695 的完整区间，包括 2 个模型、4 个任务，\n    关系的稳健性已足够说服 reviewer。\n\n    '\n  tables:\n  - name: 'Table: Jaccard-CSS Correlation Data'\n    description: '行: 6 个 model×task 组合 列: Task, Model, Methods, Max Jaccard, CSS=1.0\n      CPR, Best-Single CPR, Δ(advantage), CSS=1.0 Edges 底部: Spearman ρ=0.94, p=0.005\n\n      '\n  figures_description:\n  - '核心 Figure（可能是 Figure 3 或 4）：Scatter plot，x 轴 = 1-max_Jaccard (method diversity),\n    y 轴 = CSS CPR advantage。6 个点，颜色区分模型 （GPT-2 蓝色, Qwen 橙色），形状区分任务类型（圆=localized,\n    三角=distributed）。 灰色虚线 y=0 分隔 CSS-positive 和 CSS-negative 区域。拟合线斜率为正。 右上角标注 ρ=0.94,\n    p=0.005。垂直虚线标注 Jaccard threshold ≈ 0.53。 这可能是全文最重要的图——将整个叙事浓缩为一张可视化\n\n    '\n  analysis: '此分析是论文的 crown jewel。6 个数据点虽然不多，但覆盖了 localized→distributed spectrum 和两个模型架构，Spearman\n    ρ=0.94 在 p=0.005 下显著。Jaccard threshold ≈ 0.53 提供了 actionable guideline——这是 reviewer\n    最希望看到的 practical contribution。仅用 4 个 GPT-2 任务时 ρ=1.0 但 p=0.042（4 个点的 perfect rank\n    correlation 仍然 marginal），加入 Qwen 数据使 p 降至 0.005， 大幅增强统计说服力。建议论文主文放 4-task 分析（因为更\n    clean），appendix 放 6-point 分析（加入跨模型验证）。\n\n    对 reviewer R1（泛化性）的回应：4 个任务覆盖 localized (SVA, IOI) 和 distributed (Factual, Arithmetic)，2\n    个模型覆盖不同架构——足以建立 pattern。 对 reviewer R3（K≈2）的回应：IFR 的引入使 Qwen 数据点落在 GPT-2 趋势线上，\n    证明 method diversity（而非特定方法组合）是 CSS utility 的决定因素。'\n",
      "numLines": 523,
      "startLine": 1,
      "totalLines": 523
    }
  },
  "sourceToolAssistantUUID": "39105855-045e-49c3-9f6c-c3636f328fd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：SVA marginal PASS（统计上弱），Qwen ACDC 技术可行但结果 mixed；Jaccard-utility 趋势可见但数据点不足以达到统计显著 核心假设：['SVA css_1.00 Δ(CPR) ∈ [0.005, 0.03]，condition④ technically PASS…",
  "leafUuid": "1bdeca9f-493e-44f2-8edc-2916aa59df6c",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframed CSS paper: Jaccard-predicted utility",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb"
}
```

---

### Assistant

_source line 25 · 2026-05-13T08:31:43.838Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the best tier. Let me also read the ROADMAP for any additional context on what experiments are planned, and check what the median tier dream already looks like for reference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bdeca9f-493e-44f2-8edc-2916aa59df6c",
  "isSidechain": false,
  "requestId": "req_011CazFqtezGkRjU5DuXNCvi",
  "type": "assistant",
  "uuid": "c41bbabc-b4e1-4d95-ba7b-fcc897331cf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185pW3pYFnuJTFWnYZLFcQD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 31447,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12121,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 31447,
          "cache_creation_input_tokens": 12121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12121
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

_source line 26 · 2026-05-13T08:31:44.359Z_

Now let me check the existing median tier dream report and the ROADMAP for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c41bbabc-b4e1-4d95-ba7b-fcc897331cf8",
  "isSidechain": false,
  "requestId": "req_011CazFqtezGkRjU5DuXNCvi",
  "type": "assistant",
  "uuid": "e2d8bf86-4138-40ed-817c-54fb11d0cca0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185pW3pYFnuJTFWnYZLFcQD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 31447,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12121,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 31447,
          "cache_creation_input_tokens": 12121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12121
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

_source line 27 · 2026-05-13T08:31:47.198Z_

<details open><summary>🔧 Tool call — Read · `toolu_014LncPKZ7u1VHaXvv76Dx2F`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2d8bf86-4138-40ed-817c-54fb11d0cca0",
  "isSidechain": false,
  "requestId": "req_011CazFqtezGkRjU5DuXNCvi",
  "type": "assistant",
  "uuid": "52f702b3-46e9-41b9-865c-abd86d9d9ff0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185pW3pYFnuJTFWnYZLFcQD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 31447,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12121,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 31447,
          "cache_creation_input_tokens": 12121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12121
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

_source line 28 · 2026-05-13T08:31:47.597Z_

<details><summary>↩ Tool result · `toolu_01Vqg7FyvH1XuGAq19AeyDUw`</summary>

```text
1	# structfuse-context — Research Dashboard
2	
3	> 最后更新: 2026-05-13 UTC | 更新原因: 更新当前进展与近期任务（IOI PASS_MAIN, Arithmetic 运行中）
4	
5	## 核心方向
6	跨方法二值共识（CSS）用于鲁棒电路编辑：证明 binary stability scoring + family-agreement constraint 在分布偏移下优于 score averaging 和单方法电路。
7	
8	## 当前进展
9	- **阶段**: MVP 验证 — IOI 已 PASS_MAIN（off-diagonal 13.3%），Arithmetic 确认实验运行中
10	- **核心假设**: CSS off-diagonal ≥5%（D021 CSS-only gate，D024 覆盖 D002）
11	- **基础设施**: cqa1-21977 (cuda:5, RTX 4090D) 已配置
12	- **大模型方案已定 (D006)**: IFR 作为第三方法，triangulation 框架定位
13	- **目标**: EMNLP 2026 Main（ARR deadline 2026-05-25，剩余 12 天）
14	
15	## 方法配置
16	| 模型 | K | 方法 | 算法族 |
17	|------|---|------|--------|
18	| GPT-2 Small | 3 | EAP-IG + Edge Pruning + ACDC | gradient / mask / greedy causal |
19	| Qwen-2.5 0.5B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |
20	| Gemma-2 2B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |
21	| Llama-3.1 8B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |
22	
23	论文需披露：GPT-2 Small CSS = 3 因果方法共识；大模型 CSS = 2 因果 + 1 相似度方法共识（triangulation）。
24	
25	## MVP Gate 规则（D001-D003）
26	| off-diagonal % | 决策 |
27	|---|---|
28	| ≥10% | → Main track |
29	| 5-10% | → Findings + 追加 Arithmetic 验证 |
30	| 2-5% | → Findings 确认 |
31	| <2% (两组) + ΔF 无差异 | → Kill |
32	
33	## 阶段规划
34	
35	### Phase 1: MVP pilot（当前）
36	- GPT-2 Small / IOI，K=3（3 因果族），~2h → off-diagonal 判定
37	
38	### Phase 2: K=3 checkpoint + 全量 CSS（MVP 后 ~3天）
39	- Qwen-2.5 0.5B / IOI K=3（含 IFR）快速检查
40	- 全 4 模型 × 4 任务 CSS 计算
41	- 确认 Edge Pruning 实现：princeton-nlp/edge-pruning（非 auto-circuit mask gradient）
42	
43	### Phase 3: OOD editing（~4天）
44	### Phase 4: 分析 + 写作（~3天，最迟 5月22日）
45	
46	## 近期任务
47	- [ ] 等待 mvp_arithmetic_gpt2_k3 完成 → gate 判定
48	- [ ] Gate PASS 后 complete_mvp → 进入 research
49	- [ ] 写 paper_framing.md + experiment_plan.yaml
50	- [ ] 部署 IFR + Phase 2 实验脚本到服务器
51	- [ ] 下载目标模型（Qwen-2.5 0.5B 优先）
52	
53	## GPU 预算
54	- 已分配: 1× RTX 4090D (cuda:5@cqa1-21977)
55	- MVP: ~2h | 全量: ~290h A100（需后续扩卡）
56	
57	## 关键决策日志
58	
59	| ID | 日期 | 摘要 | 关联实验 |
60	|----|------|------|----------|
61	| D033 | 2026-05-13 | D033: SVA 判定降级为 inconclusive——单 seed Δ=0.013 不具鲁棒性 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |
62	| D032 | 2026-05-13 | D032: 条件④评估指标修正——必须用 css_1.00 而非 css_0.67 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |
63	| D031 | 2026-05-13 | 统一 D025 条件④标准：zero PASS 或 mean Δ≥0.01，SVA 两次均判 neg | mvp_sva_gpt2_k3, mvp_sva_gpt2_k3_topk |
64	| D030 | 2026-05-13 | SVA D025 gate FAIL（zero FAIL / mean 边际 Δ=0.008）；发现 | mvp_sva_gpt2_k3_topk |
65	| D029 | 2026-05-13 | Phase 2 第三方法：放弃 IFR，改用 ACDC top-k。IFR 跨族分歧作为 Discu | phase2_qwen05b_ioi_k3 |
66	| D028 | 2026-05-13 | Phase 2 IFR 零重叠问题：暂停 Qwen/Gemma 新实验，先修 IFR per-hea | phase2_qwen05b_ioi_k3 |
67	| D027 | 2026-05-13 | MVP 最终判定：CSS faithfulness 优势 task-dependent（IOI PA | mvp_arithmetic_gpt2_k3, mvp_pilot_gpt2_ioi_v3 |
68	| D026 | 2026-05-13 | Arithmetic D025 gate FAIL（条件④），暂不判 MVP 结果，先做 ACDC  | mvp_arithmetic_gpt2_k3 |
69	| D025 | 2026-05-13 | 更新 Arithmetic gate 为 CSS-only 四条件标准（替代 D024 的单一 5% | mvp_arithmetic_gpt2_k3 |
70	| D024 | 2026-05-13 | D021 覆盖 D002 灰区定义：arithmetic CSS off-diagonal ≥5%  | — |
71	
72	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b407f6d-42cc-40ae-89a7-1198eb14f687",
  "isSidechain": false,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "type": "user",
  "uuid": "fbb5ef92-7f72-423f-baad-a4b202a88471",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ROADMAP.md",
      "content": "# structfuse-context — Research Dashboard\n\n> 最后更新: 2026-05-13 UTC | 更新原因: 更新当前进展与近期任务（IOI PASS_MAIN, Arithmetic 运行中）\n\n## 核心方向\n跨方法二值共识（CSS）用于鲁棒电路编辑：证明 binary stability scoring + family-agreement constraint 在分布偏移下优于 score averaging 和单方法电路。\n\n## 当前进展\n- **阶段**: MVP 验证 — IOI 已 PASS_MAIN（off-diagonal 13.3%），Arithmetic 确认实验运行中\n- **核心假设**: CSS off-diagonal ≥5%（D021 CSS-only gate，D024 覆盖 D002）\n- **基础设施**: cqa1-21977 (cuda:5, RTX 4090D) 已配置\n- **大模型方案已定 (D006)**: IFR 作为第三方法，triangulation 框架定位\n- **目标**: EMNLP 2026 Main（ARR deadline 2026-05-25，剩余 12 天）\n\n## 方法配置\n| 模型 | K | 方法 | 算法族 |\n|------|---|------|--------|\n| GPT-2 Small | 3 | EAP-IG + Edge Pruning + ACDC | gradient / mask / greedy causal |\n| Qwen-2.5 0.5B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |\n| Gemma-2 2B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |\n| Llama-3.1 8B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |\n\n论文需披露：GPT-2 Small CSS = 3 因果方法共识；大模型 CSS = 2 因果 + 1 相似度方法共识（triangulation）。\n\n## MVP Gate 规则（D001-D003）\n| off-diagonal % | 决策 |\n|---|---|\n| ≥10% | → Main track |\n| 5-10% | → Findings + 追加 Arithmetic 验证 |\n| 2-5% | → Findings 确认 |\n| <2% (两组) + ΔF 无差异 | → Kill |\n\n## 阶段规划\n\n### Phase 1: MVP pilot（当前）\n- GPT-2 Small / IOI，K=3（3 因果族），~2h → off-diagonal 判定\n\n### Phase 2: K=3 checkpoint + 全量 CSS（MVP 后 ~3天）\n- Qwen-2.5 0.5B / IOI K=3（含 IFR）快速检查\n- 全 4 模型 × 4 任务 CSS 计算\n- 确认 Edge Pruning 实现：princeton-nlp/edge-pruning（非 auto-circuit mask gradient）\n\n### Phase 3: OOD editing（~4天）\n### Phase 4: 分析 + 写作（~3天，最迟 5月22日）\n\n## 近期任务\n- [ ] 等待 mvp_arithmetic_gpt2_k3 完成 → gate 判定\n- [ ] Gate PASS 后 complete_mvp → 进入 research\n- [ ] 写 paper_framing.md + experiment_plan.yaml\n- [ ] 部署 IFR + Phase 2 实验脚本到服务器\n- [ ] 下载目标模型（Qwen-2.5 0.5B 优先）\n\n## GPU 预算\n- 已分配: 1× RTX 4090D (cuda:5@cqa1-21977)\n- MVP: ~2h | 全量: ~290h A100（需后续扩卡）\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D033 | 2026-05-13 | D033: SVA 判定降级为 inconclusive——单 seed Δ=0.013 不具鲁棒性 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |\n| D032 | 2026-05-13 | D032: 条件④评估指标修正——必须用 css_1.00 而非 css_0.67 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |\n| D031 | 2026-05-13 | 统一 D025 条件④标准：zero PASS 或 mean Δ≥0.01，SVA 两次均判 neg | mvp_sva_gpt2_k3, mvp_sva_gpt2_k3_topk |\n| D030 | 2026-05-13 | SVA D025 gate FAIL（zero FAIL / mean 边际 Δ=0.008）；发现 | mvp_sva_gpt2_k3_topk |\n| D029 | 2026-05-13 | Phase 2 第三方法：放弃 IFR，改用 ACDC top-k。IFR 跨族分歧作为 Discu | phase2_qwen05b_ioi_k3 |\n| D028 | 2026-05-13 | Phase 2 IFR 零重叠问题：暂停 Qwen/Gemma 新实验，先修 IFR per-hea | phase2_qwen05b_ioi_k3 |\n| D027 | 2026-05-13 | MVP 最终判定：CSS faithfulness 优势 task-dependent（IOI PA | mvp_arithmetic_gpt2_k3, mvp_pilot_gpt2_ioi_v3 |\n| D026 | 2026-05-13 | Arithmetic D025 gate FAIL（条件④），暂不判 MVP 结果，先做 ACDC  | mvp_arithmetic_gpt2_k3 |\n| D025 | 2026-05-13 | 更新 Arithmetic gate 为 CSS-only 四条件标准（替代 D024 的单一 5% | mvp_arithmetic_gpt2_k3 |\n| D024 | 2026-05-13 | D021 覆盖 D002 灰区定义：arithmetic CSS off-diagonal ≥5%  | — |\n\n",
      "numLines": 72,
      "startLine": 1,
      "totalLines": 72
    }
  },
  "sourceToolAssistantUUID": "8b407f6d-42cc-40ae-89a7-1198eb14f687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-13T08:31:47.204Z_

<details><summary>↩ Tool result · `toolu_014LncPKZ7u1VHaXvv76Dx2F`</summary>

```text
1	tier: median
2	narrative_guidance: '论文重心从 "CSS empirically superior" 转向 "CSS as analytical framework
3	  + binarization pathology"。 SVA 提供第三个数据点但 CSS 优势不明显（CPR 差距 < 0.02），仅能 claim "comparable
4	  faithfulness at fraction of edges"。Jaccard-utility 趋势方向正确（3 点 Spearman ≈ 0.87）但无法做统计检验（p
5	  > 0.3）， 降级为 "observed trend"。DocQA 第四任务因 GPT-2 Small 能力不足未产出 clean circuit，被砍掉。
6	  IFR 加入 Qwen IOI 后某些 pair Jaccard 降低但 IFR×EP 高度相关（~0.55），CSS 优势被稀释。 Claim 3（binarization
7	  pathology）和 Claim 4（CSS taxonomy）成为最坚实的 methodological contribution。 仍可投 EMNLP main，framing
8	  为 analytical/diagnostic framework，reviewer 主攻点在 n=3 泛化性 和 ACDC top-k 的 degree of
9	  freedom。
10	
11	  '
12	imagined_experiments:
13	- name: GPT-2 SVA K=3 CSS
14	  plan_id: plan_004
15	  description: 'Subject-Verb Agreement on GPT-2 Small, K=3 (EAP-IG + EP + ACDC with
16	    top-k=75). SVA 是相对 localized 的语法任务，预期方法间有中等分歧。
17	
18	    '
19	  expected_results:
20	    status: done
21	    conclusion: partial_support
22	    pairwise_jaccard:
23	      eapig_x_ep: 0.38
24	      eapig_x_acdc_k75: 0.18
25	      ep_x_acdc_k75: 0.15
26	    max_jaccard: 0.38
27	    three_way_ratio: 0.067
28	    circuit_sizes:
29	      eapig_k75: 75
30	      ep_k75: 75
31	      acdc_k75: 75
32	      acdc_isinf: 22
33	    css_distribution:
34	      1/3: 148
35	      2/3: 54
36	      3/3: 23
37	    faithfulness_mean:
38	      css_1.00_k75:
39	        edges: 23
40	        CPR: 0.941
41	        CMD: 0.263
42	      css_0.67_k75:
43	        edges: 54
44	        CPR: 0.958
45	        CMD: 0.189
46	      eapig_k75:
47	        edges: 75
48	        CPR: 0.953
49	        CMD: 0.211
50	      ep_k75:
51	        edges: 75
52	        CPR: 0.937
53	        CMD: 0.284
54	      acdc_k75:
55	        edges: 75
56	        CPR: 0.922
57	        CMD: 0.347
58	    faithfulness_isinf_degeneration:
59	      css_1.00_isinf:
60	        edges: 22
61	        CPR: 0.918
62	        CMD: 0.368
63	      acdc_isinf:
64	        edges: 22
65	        CPR: 0.918
66	        CMD: 0.368
67	      degeneration_confirmed: true
68	    css1_cpr_advantage_over_best: -0.012
69	    css1_edge_ratio: 0.307
70	    sva_gate_verdict: MARGINAL — CSS=1.0 CPR comparable but not superior; edge efficiency
71	      3.3x
72	  result_rationale: 'SVA 在 GPT-2 Small 上的电路比 IOI 更 localized（主要涉及 subject token 到
73	    verb position 的 attention + 少量 MLP），但不如 IOI 那样有清晰的 "备份名字" 结构驱动方法分歧。EAP-IG 和 EP
74	    作为 gradient-adjacent 方法在 SVA 上 Jaccard=0.38（高于 IOI 的 0.31），因为 SVA 的 gradient landscape
75	    比 IOI 更平滑——主谓一致主要依赖几个 key attention head，gradient 方法容易收敛到 类似子集。ACDC top-k=75 normalization
76	    打破了 isinf 退化（isinf 只有 22 条 edge），但引入了 k 的选择作为额外自由度。CSS=1.0 包含 23 条边，CPR=0.941
77	    略低于 EAP-IG 的 0.953（差距 0.012）， 说明全共识子集在去除了各方法的 "独特发现" 后损失了少量信息。这符合 median 档预期：CSS
78	    部分支持 但不完美，edge efficiency 优势（3.3x fewer edges）是实在的，但 faithfulness 并无优势。
79	
80	    '
81	  tables:
82	  - name: 'Table: SVA Faithfulness Comparison (mean ablation, top-k=75)'
83	    columns:
84	    - Circuit
85	    - Edges
86	    - CPR ↑
87	    - CMD ↓
88	    - Edge Ratio
89	    rows:
90	    - - CSS=1.0 (k=75)
91	      - 23
92	      - 0.941
93	      - 0.263
94	      - 0.31x
95	    - - CSS≥0.67 (k=75)
96	      - 54
97	      - 0.958
98	      - 0.189
99	      - 0.72x
100	    - - EAP-IG (k=75)
101	      - 75
102	      - 0.953
103	      - 0.211
104	      - 1.00x
105	    - - EP (k=75)
106	      - 75
107	      - 0.937
108	      - 0.284
109	      - 1.00x
110	    - - ACDC (k=75)
111	      - 75
112	      - 0.922
113	      - 0.347
114	      - 1.00x
115	    - - ACDC (isinf)
116	      - 22
117	      - 0.918
118	      - 0.368
119	      - 0.29x
120	  - name: 'Table: SVA Pairwise Jaccard (top-k=75)'
121	    columns:
122	    - ''
123	    - EAP-IG
124	    - EP
125	    - ACDC
126	    rows:
127	    - - EAP-IG
128	      - —
129	      - 0.38
130	      - 0.18
131	    - - EP
132	      - 0.38
133	      - —
134	      - 0.15
135	    - - ACDC
136	      - 0.18
137	      - 0.15
138	      - —
139	  figures_description:
140	  - 'Fig: SVA CSS distribution histogram (1/3, 2/3, 3/3) — 与 IOI 对比显示更集中的分布'
141	  - 'Fig: SVA edge overlap Venn diagram (3 methods, top-k=75)'
142	  analysis: 'SVA 结果处于 IOI（CSS clear win）和 Arithmetic（CSS clear loss）之间的灰色地带。 CSS=1.0
143	    用 23 条边达到了 75 条边 EAP-IG 的 98.7% faithfulness (0.941/0.953)， edge efficiency 论点成立但
144	    CPR 没有优势。关键问题：top-k=75 是 SVA 上的最优 k， k=50 时 CSS=1.0 只有 15 条边且 CPR 降到 0.89，k=100
145	    时 CSS=1.0 有 31 条边但 CPR 不再提升——这个 k-sensitivity 是 reviewer 可攻击的 degree of freedom。
146	    对 Claim 1 的贡献：降级为 "comparable faithfulness at fraction of edges"。 对 Claim 2 的贡献：Jaccard=0.38
147	    + CSS marginal → 第三个数据点，位于 IOI 和 Arithmetic 之间，方向一致。
148	
149	    '
150	- name: GPT-2 DocQA/Factual K=3 CSS
151	  plan_id: plan_005
152	  description: 'Distributed computation task on GPT-2 Small. 预期高 Jaccard → CSS 应该失败（确认模式）。
153	
154	    '
155	  expected_results:
156	    status: abandoned
157	    conclusion: data_not_clean
158	    partial_metrics:
159	      eapig_completed: true
160	      ep_completed: true
161	      acdc_completed: false
162	      acdc_failure_reason: GPT-2 Small factual recall 太弱，ACDC 收敛到近空电路（< 5 edges）
163	    note: ACDC 无法产出有意义的电路，实验被终止。不纳入论文分析。
164	  result_rationale: 'GPT-2 Small (117M) 的 factual knowledge 极为有限，DocQA/Factual recall
165	    任务上 模型本身准确率不稳定（~55-65% vs random 25%）。EAP-IG 和 EP 可以强行产出 top-k 电路，但 ACDC 的 patching-based
166	    搜索在 clean performance 不稳定时无法收敛—— 阈值过高则电路为空，过低则几乎保留全图。尝试调低阈值后得到 3-5 条 isinf 边，
167	    top-k normalization 后虽能凑出 50-75 条边但其 faithfulness 接近随机（CPR ≈ 0）。 这不是 CSS 方法的失败而是
168	    task-model 匹配问题。在 deadline 压力下（ARR 5/25） 决定放弃第四任务，论文保持 3 个任务（IOI + Arithmetic
169	    + SVA）。
170	
171	    '
172	  tables: []
173	  figures_description: []
174	  analysis: '第四任务失败是 median 档的核心限制。论文需要在 Limitations 中说明 GPT-2 Small 对 factual recall
175	    的能力不足以支撑 circuit discovery，并将 broader task coverage 列为 future work。这会成为 reviewer
176	    攻击的主要靶点（"only 3 tasks on one model"）。 应对策略：强调 3 个任务已覆盖 localized（IOI）、distributed（Arithmetic）、
177	    intermediate（SVA）三种电路结构类型，以及 Qwen 上的 cross-model validation。
178	
179	    '
180	- name: Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + IFR)
181	  plan_id: plan_006
182	  description: '首次 larger model + IFR 作为第三方法（替换 ACDC）。IFR 是 similarity-based 方法， 与
183	    gradient 方法家族不同，预期降低 Jaccard。
184	
185	    '
186	  expected_results:
187	    status: done
188	    conclusion: mixed
189	    pairwise_jaccard:
190	      eapig_x_ep: 0.42
191	      eapig_x_ifr: 0.19
192	      ep_x_ifr: 0.55
193	    max_jaccard: 0.55
194	    three_way_ratio: 0.082
195	    circuit_sizes:
196	      eapig_k75: 75
197	      ep_k75: 75
198	      ifr_k75: 75
199	    css_distribution:
200	      1/3: 143
201	      2/3: 63
202	      3/3: 19
203	    faithfulness_mean:
204	      css_1.00:
205	        edges: 19
206	        CPR: 0.103
207	        CMD: 0.921
208	      css_0.67:
209	        edges: 63
210	        CPR: 0.087
211	        CMD: 0.944
212	      eapig_k75:
213	        edges: 75
214	        CPR: 0.091
215	        CMD: 0.938
216	      ep_k75:
217	        edges: 75
218	        CPR: 0.078
219	        CMD: 0.952
220	      ifr_k75:
221	        edges: 75
222	        CPR: 0.064
223	        CMD: 0.967
224	    css1_cpr: 0.103
225	    css1_vs_best_single: 0.012
226	    ifr_ep_correlation_note: 'IFR×EP Jaccard=0.55 远高于预期。IFR 虽然是 similarity-based，但在
227	      IOI 上 EP 的 edge importance 与 IFR 的 representation similarity 高度一致—— 可能因为 IOI
228	      的 backup name 机制使得 "重要的边" 在两种度量下都突出。 这削弱了 K≈3 independent methods 的假设，实际独立证据更接近
229	      K≈2.3。
230	
231	      '
232	  result_rationale: 'Qwen-2.5 0.5B 上 IOI 的电路结构与 GPT-2 类似（名字 mover head + backup 机制），
233	    但模型更大导致电路更分散。EAP-IG×EP 的 Jaccard 从 GPT-2 的 0.31 升至 0.42， 因为 Qwen 的 gradient landscape
234	    更平滑（more parameters → gradient 更 concentrated on true signal）。IFR 作为 similarity-based
235	    方法确实与 EAP-IG 差异大（Jaccard=0.19）， 但与 EP 的 Jaccard 意外达到 0.55——这是因为 EP 的 edge pruning
236	    和 IFR 的 representation similarity 都偏好 "移除后 representation 变化大" 的边，两者在 measurement
237	    层面有隐含重叠。CSS=1.0 的 19 条边 CPR=0.103 略好于 GPT-2 IOI 的 0.109 （量级一致），表明 CSS 在 larger
238	    model 上仍然能提取 faithful 子集。但 max_jaccard=0.55 使得这个数据点在 Jaccard-utility 图上落在不太理想的位置——CSS
239	    优势有限（+0.012 over EAP-IG）且 Jaccard 不够低。IFR 混入了与 EP 相关的信号，有效独立方法数 < 3。
240	
241	    '
242	  tables:
243	  - name: 'Table: Qwen-0.5B IOI Faithfulness (mean ablation, k=75)'
244	    columns:
245	    - Circuit
246	    - Edges
247	    - CPR ↑
248	    - CMD ↓
249	    rows:
250	    - - CSS=1.0
251	      - 19
252	      - 0.103
253	      - 0.921
254	    - - CSS≥0.67
255	      - 63
256	      - 0.087
257	      - 0.944
258	    - - EAP-IG
259	      - 75
260	      - 0.091
261	      - 0.938
262	    - - EP
263	      - 75
264	      - 0.078
265	      - 0.952
266	    - - IFR
267	      - 75
268	      - 0.064
269	      - 0.967
270	  - name: 'Table: Qwen-0.5B IOI Pairwise Jaccard'
271	    columns:
272	    - ''
273	    - EAP-IG
274	    - EP
275	    - IFR
276	    rows:
277	    - - EAP-IG
278	      - —
279	      - 0.42
280	      - 0.19
281	    - - EP
282	      - 0.42
283	      - —
284	      - 0.55
285	    - - IFR
286	      - 0.19
287	      - 0.55
288	      - —
289	  figures_description:
290	  - 'Fig: Qwen IOI CSS distribution vs GPT-2 IOI — 对比两个 model scale 下的 CSS 分布形态'
291	  - 'Fig: IFR vs EP edge importance scatter plot — 显示 Jaccard=0.55 的来源'
292	  analysis: 'Qwen IOI 结果是 "mixed" 的典型案例。好消息：CSS=1.0 在 larger model 上仍然 work， CPR 略优于
293	    best single method，证明 CSS 框架可跨模型。坏消息：IFR×EP Jaccard=0.55 说明 "不同算法家族 → 低相关" 的假设不总成立——算法差异不等于
294	    measurement independence。 这对 Claim 2 有双重影响：(1) max_jaccard=0.55 + CSS marginal
295	    win 支持 "中等 Jaccard → 中等 CSS 收益" 的连续关系假设；(2) 但也说明 Jaccard 可能需要分 pair 解读而非只看 max。
296	    论文中应在 Discussion 讨论 IFR-EP 相关性的 mechanistic 原因。
297	
298	    '
299	- name: Qwen-2.5 0.5B Arithmetic K=3
300	  plan_id: plan_007
301	  description: 'Qwen 上的 Arithmetic (Greaterthan) task，IFR 替换 ACDC。 验证 IFR 是否能降低 Arithmetic
302	    的 Jaccard 使 CSS recover。
303	
304	    '
305	  expected_results:
306	    status: done
307	    conclusion: negative
308	    pairwise_jaccard:
309	      eapig_x_ep: 0.61
310	      eapig_x_ifr: 0.38
311	      ep_x_ifr: 0.48
312	    max_jaccard: 0.61
313	    three_way_ratio: 0.195
314	    css_distribution:
315	      1/3: 98
316	      2/3: 73
317	      3/3: 54
318	    faithfulness_mean:
319	      css_1.00:
320	        edges: 54
321	        CPR: 0.932
322	        CMD: 0.302
323	      eapig_k75:
324	        edges: 75
325	        CPR: 0.971
326	        CMD: 0.128
327	      ep_k75:
328	        edges: 75
329	        CPR: 0.955
330	        CMD: 0.199
331	      ifr_k75:
332	        edges: 75
333	        CPR: 0.891
334	        CMD: 0.487
335	    css1_cpr_advantage_over_best: -0.039
336	    note: 'IFR 将 max_jaccard 从 GPT-2 的 0.695 降至 0.61，但仍不够低。 CSS=1.0 CPR=0.932 < EAP-IG=0.971。CSS
337	      未 recover。
338	
339	      '
340	  result_rationale: 'Arithmetic/Greaterthan 任务的电路结构本质上是 distributed 的——多个 MLP layer
341	    协同完成数值比较，gradient-based 方法容易收敛到相似的关键路径。IFR 替换 ACDC 后 确实降低了 max_jaccard（0.695 →
342	    0.61），但降幅不够大。原因：Arithmetic 的 "重要边" 集中在少数 MLP 到 final position 的连接上，无论用 gradient
343	    (EAP-IG/EP) 还是 similarity (IFR)，这些边都会被 rank 到顶部。IFR 本身表现较弱（CPR=0.891）， 拖累了 CSS=1.0
344	    的质量——共识要求三方都同意的边包含了 IFR 的一些 false positive。 这个结果实际上支持 Claim 2：Jaccard 仍然偏高（0.61）→
345	    CSS 仍然不优—— 趋势一致，但不是正面结果。
346	
347	    '
348	  tables:
349	  - name: 'Table: Qwen-0.5B Arithmetic Faithfulness (mean ablation)'
350	    columns:
351	    - Circuit
352	    - Edges
353	    - CPR ↑
354	    - CMD ↓
355	    rows:
356	    - - CSS=1.0
357	      - 54
358	      - 0.932
359	      - 0.302
360	    - - EAP-IG (k=75)
361	      - 75
362	      - 0.971
363	      - 0.128
364	    - - EP (k=75)
365	      - 75
366	      - 0.955
367	      - 0.199
368	    - - IFR (k=75)
369	      - 75
370	      - 0.891
371	      - 0.487
372	  figures_description:
373	  - 'Fig: Qwen Arithmetic CSS distribution — 与 GPT-2 Arithmetic 对比'
374	  analysis: 'IFR "部分修复" 了 Arithmetic 的 Jaccard 问题但不够彻底。从 Claim 2 角度看 这其实是一个有价值的 intermediate
375	    data point：Jaccard 从 0.695 降到 0.61， CSS 优势从 -0.066 改善到 -0.039，方向正确但仍为负。如果画 Jaccard
376	    vs CSS_advantage 的图，这个点和 GPT-2 Arithmetic 几乎在同一条趋势线上。 问题在于 IFR 本身在 Arithmetic
377	    上的 faithfulness 较差（CPR=0.891 远低于 EAP-IG 的 0.971），说明 similarity-based method 对
378	    distributed computation 的识别 能力有限——这是一个独立的 finding，可在 Discussion 中报告。
379	
380	    '
381	- name: Gemma-2 2B IOI K=3
382	  plan_id: plan_008
383	  description: Scale to 2B model (Gemma-2). P2 优先级。
384	  expected_results:
385	    status: not_attempted
386	    conclusion: null
387	    reason: 时间和 GPU 资源不足，P1 任务已消耗大部分 budget。列入 Future Work。
388	  result_rationale: 'Median 档的时间约束（ARR 5/25 deadline）下，plan_004 (SVA) + plan_006 (Qwen
389	    IOI) + plan_007 (Qwen Arith) 已消耗约 20 GPU-hours。Gemma-2 2B 需要 16 GPU-hours 且 依赖
390	    plan_006 结果（IFR pipeline 验证）。即使 plan_006 顺利完成，剩余时间不足 以完成 Gemma-2 实验 + 分析 + 论文写作。P2
391	    优先级下被合理推迟。
392	
393	    '
394	  tables: []
395	  figures_description: []
396	  analysis: Not attempted. 在 Limitations 中列为 model scale generalization future work。
397	- name: Llama-3.1 8B IOI K=3
398	  plan_id: plan_009
399	  description: Scale to 8B model. P3 优先级。Needs A100 80GB。
400	  expected_results:
401	    status: not_attempted
402	    conclusion: null
403	    reason: P3 优先级，且 plan_008 未完成作为前置。远超 deadline 范围。
404	  result_rationale: '8B 模型实验需要 A100 80GB（当前设备可能不支持 EP 的内存需求），且依赖 plan_008。 在 median
405	    档下属于完全不现实的目标。
406	
407	    '
408	  tables: []
409	  figures_description: []
410	  analysis: Not attempted. Future work 中的 stretch goal。
411	- name: Binarization sensitivity ablation
412	  plan_id: plan_010
413	  description: 'Systematic k sweep (k=50/75/100/150) on all completed model×task pairs.
414	    验证 CSS 在不同 k 下的稳定性。
415	
416	    '
417	  expected_results:
418	    status: done
419	    conclusion: partially_stable
420	    ioi_gpt2_k_sweep:
421	      k50:
422	        css_1.0_edges: 12
423	        css_1.0_cpr: 0.098
424	      k75:
425	        css_1.0_edges: 18
426	        css_1.0_cpr: 0.112
427	      k100:
428	        css_1.0_edges: 24
429	        css_1.0_cpr: 0.109
430	      k150:
431	        css_1.0_edges: 31
432	        css_1.0_cpr: 0.108
433	      verdict: stable (CPR range 0.098-0.112, Δ=0.014)
434	    arithmetic_gpt2_k_sweep:
435	      k50:
436	        css_1.0_edges: 44
437	        css_1.0_cpr: 0.919
438	      k75:
439	        css_1.0_edges: 54
440	        css_1.0_cpr: 0.919
441	      k100:
442	        css_1.0_edges: 62
443	        css_1.0_cpr: 0.926
444	      k150:
445	        css_1.0_edges: 71
446	        css_1.0_cpr: 0.933
447	      verdict: stable (CPR range 0.919-0.933, Δ=0.014)
448	    sva_gpt2_k_sweep:
449	      k50:
450	        css_1.0_edges: 15
451	        css_1.0_cpr: 0.891
452	      k75:
453	        css_1.0_edges: 23
454	        css_1.0_cpr: 0.941
455	      k100:
456	        css_1.0_edges: 29
457	        css_1.0_cpr: 0.944
458	      k150:
459	        css_1.0_edges: 38
460	        css_1.0_cpr: 0.94
461	      verdict: sensitive at k=50 (CPR drop 0.05), stable k=75-150
462	    qwen_ioi_k_sweep:
463	      k50:
464	        css_1.0_edges: 11
465	        css_1.0_cpr: 0.082
466	      k75:
467	        css_1.0_edges: 19
468	        css_1.0_cpr: 0.103
469	      k100:
470	        css_1.0_edges: 26
471	        css_1.0_cpr: 0.099
472	      k150:
473	        css_1.0_edges: 35
474	        css_1.0_cpr: 0.097
475	      verdict: stable k=75-150, drop at k=50
476	    overall_verdict: 'CSS=1.0 CPR 在 k=75-150 范围内对所有 task 稳定（max Δ < 0.015）。 k=50 在
477	      SVA 和 Qwen IOI 上 CPR 下降 ~0.04-0.05，因为 k=50 过小导致方法 重叠不足、CSS=1.0 边数太少。推荐 k=75
478	      作为默认值，但需要在论文中报告这个选择。
479	
480	      '
481	  result_rationale: 'Top-k normalization 的核心逻辑是让 ACDC 和其他方法在同一 edge budget 下比较。 k=75-150
482	    范围内，三种方法各自选择的 top edges 有足够的 overlap base 使 CSS=1.0 稳定。k=50 时边太少，方法间 overlap 降到
483	    noise level，CSS=1.0 变得不可靠。 SVA 比 IOI 更敏感于 k 的原因：SVA 电路更 concentrated（少数 critical
484	    edges 占比更大），k=50 可能恰好切掉了某些方法的 borderline critical edge。 这个 sensitivity 是 median
485	    档的典型问题——结果 "基本稳定但有 caveat"， reviewer 可以攻击 k=75 的选择是 cherry-picked（虽然实际不是）。
486	
487	    '
488	  tables:
489	  - name: 'Table: CSS=1.0 CPR across k values (all tasks)'
490	    columns:
491	    - Task
492	    - k=50
493	    - k=75
494	    - k=100
495	    - k=150
496	    - Max Δ
497	    rows:
498	    - - IOI (GPT-2)
499	      - 0.098
500	      - 0.112
501	      - 0.109
502	      - 0.108
503	      - 0.014
504	    - - Arith (GPT-2)
505	      - 0.919
506	      - 0.919
507	      - 0.926
508	      - 0.933
509	      - 0.014
510	    - - SVA (GPT-2)
511	      - 0.891
512	      - 0.941
513	      - 0.944
514	      - 0.94
515	      - 0.053
516	    - - IOI (Qwen)
517	      - 0.082
518	      - 0.103
519	      - 0.099
520	      - 0.097
521	      - 0.021
522	  figures_description:
523	  - 'Fig: Line plot of CSS=1.0 CPR vs k for all 4 model×task configs — 灰色 band 标记
524	    k=75-150 稳定区间'
525	  analysis: 'Binarization ablation 的结论可以支撑 Claim 3（top-k 修复 isinf 退化）， 但 SVA k=50
526	    的 sensitivity 会被 reviewer 追问。应对：(1) 论文推荐 k=75 并展示 full sweep 数据，(2) argue k=50
527	    本身就低于合理下界（只保留 0.15% edges for GPT-2 的 32k+ edge graph），(3) 指出 k=75-150 的 CPR 标准差
528	    < 0.01。
529	
530	    '
531	- name: Ablation method comparison (zero vs mean vs resample)
532	  plan_id: plan_011
533	  description: 'Compare ablation methods on all tasks. P2 优先级。 验证 CSS advantage 不依赖特定
534	    evaluation ablation。
535	
536	    '
537	  expected_results:
538	    status: partial
539	    conclusion: inconclusive
540	    completed_tasks:
541	    - IOI (GPT-2)
542	    ioi_gpt2:
543	      zero_ablation:
544	        css_1.0_cpr: 0.109
545	        best_single_cpr: 0.029
546	        css_advantage: 0.08
547	      mean_ablation:
548	        css_1.0_cpr: 0.112
549	        best_single_cpr: 0.091
550	        css_advantage: 0.021
551	      resample_ablation:
552	        css_1.0_cpr: 0.095
553	        best_single_cpr: 0.082
554	        css_advantage: 0.013
555	    note: '仅完成 IOI 一个 task 的三种 ablation 对比。CSS advantage 在三种 ablation 下 方向一致（正），但绝对值差异大（0.013-0.080）。SVA
556	      和 Arithmetic 未完成。
557	
558	      '
559	  result_rationale: '这是 P2 优先级实验，在 SVA (plan_004) 和 Qwen (plan_006/007) 完成后 时间已所剩不多。仅对
560	    IOI 跑了 zero/mean/resample 三种 ablation， 因为 IOI 是唯一 CSS clearly wins 的 task。结果显示
561	    CSS 优势在三种 ablation 下都为正但量级不同：zero ablation 下优势最大（因为 zero ablation 对电路外 edge 的破坏最大，小电路受益最多），resample
562	    下优势最小。这表明 CSS advantage 不是 ablation method artifact，但缺少 SVA 和 Arithmetic 的对比数据使结论不完整。
563	
564	    '
565	  tables:
566	  - name: 'Table: IOI CSS advantage under different ablation methods'
567	    columns:
568	    - Ablation
569	    - CSS=1.0 CPR
570	    - Best Single CPR
571	    - Advantage
572	    rows:
573	    - - Zero
574	      - 0.109
575	      - 0.029
576	      - '+0.080'
577	    - - Mean
578	      - 0.112
579	      - 0.091
580	      - '+0.021'
581	    - - Resample
582	      - 0.095
583	      - 0.082
584	      - '+0.013'
585	  figures_description: []
586	  analysis: '部分完成的 ablation 对比。IOI 结果可以放在 Appendix 中作为 robustness check。 关键 takeaway：CSS
587	    advantage 在 mean ablation（最常用）下为 +0.021，在 resample （最严格）下为 +0.013，都是正的。但仅一个 task
588	    不足以 claim robustness。 论文中可以 footnote 提及 IOI 上的一致性，full multi-task ablation 列为
589	    future work。
590	
591	    '
592	- name: CIRCUS as negative ablation
593	  plan_id: plan_012
594	  description: '使用 D021 中 CIRCUS 的已有失败结果作为 negative ablation。 0 GPU hours，仅需分析和写作。
595	
596	    '
597	  expected_results:
598	    status: done
599	    conclusion: negative_ablation_confirmed
600	    circus_vs_css:
601	      ioi_circus_core_cpr: -0.108
602	      ioi_css_1.0_cpr: 0.109
603	      ioi_circus_core_edges: 15
604	      ioi_css_1.0_edges: 7
605	    circus_failure_modes:
606	    - CIRCUS 基于 single-method faithfulness scoring 选 core edges，但 scoring 本身依赖 ablation
607	      noise
608	    - 'CIRCUS D021 三次运行结果不一致（edges: 12, 15, 18），说明 threshold sensitivity 严重'
609	    - CSS 的 binary consensus 不需要 score calibration，避免了 CIRCUS 的核心缺陷
610	  result_rationale: 'CIRCUS (Parekh 2026) 在 IOI 上的 D021 结果已有：core edges CPR=-0.108（负值，
611	    说明 CIRCUS core 实际上破坏了模型行为）。相比 CSS=1.0 的 CPR=0.109，差距极大。 CIRCUS 失败的根本原因是它在 single
612	    method 内部做 faithfulness scoring 来选 core， 但这个 scoring 对 threshold 和 ablation method
613	    极其敏感。CSS 通过 cross-method binary agreement 绕过了 score calibration 问题。这个对比自然成为论文中
614	    Claim 4 的关键证据：structural consensus (CSS) > faithfulness scoring (CIRCUS)。
615	
616	    '
617	  tables:
618	  - name: 'Table: CSS vs CIRCUS on IOI (negative ablation)'
619	    columns:
620	    - Method
621	    - Edges
622	    - CPR ↑
623	    - CMD ↓
624	    - Stable?
625	    rows:
626	    - - CSS=1.0
627	      - 7
628	      - 0.109
629	      - 0.911
630	      - Yes (3/3 runs identical)
631	    - - CIRCUS core
632	      - 15
633	      - -0.108
634	      - 1.134
635	      - No (12-18 edges across runs)
636	  figures_description:
637	  - 'Fig: CSS vs CIRCUS edge selection comparison — 显示两种方法选择的 edge 集合差异'
638	  analysis: 'CIRCUS negative ablation 是 Claim 4 最有力的证据，也是论文中最 "clean" 的结果之一。 CSS=1.0
639	    用更少的边（7 vs 15）达到正的 CPR，而 CIRCUS core 的 CPR 为负。 关键论点：binary consensus across methods
640	    比 within-method score selection 更稳定， 因为前者不需要 score calibration，后者严重依赖 ablation
641	    method 和 threshold。 这是 methodological contribution 的核心，reviewer 较难攻击（结果清晰、对比公平）。
642	
643	    '
644	- name: Jaccard-CSS correlation analysis
645	  plan_id: plan_013
646	  description: 'Across all model×task pairs, plot max pairwise Jaccard vs CSS faithfulness
647	    advantage. 3 个 task data points + Qwen cross-validation。
648	
649	    '
650	  expected_results:
651	    status: done
652	    conclusion: trend_observed_no_statistical_power
653	    data_points:
654	    - task: IOI (GPT-2)
655	      max_jaccard: 0.31
656	      css_advantage: 0.021
657	      css_wins: true
658	    - task: Arithmetic (GPT-2)
659	      max_jaccard: 0.695
660	      css_advantage: -0.066
661	      css_wins: false
662	    - task: SVA (GPT-2)
663	      max_jaccard: 0.38
664	      css_advantage: -0.012
665	      css_wins: false
666	    - task: IOI (Qwen)
667	      max_jaccard: 0.55
668	      css_advantage: 0.012
669	      css_wins: true
670	    - task: Arithmetic (Qwen)
671	      max_jaccard: 0.61
672	      css_advantage: -0.039
673	      css_wins: false
674	    spearman_rho: -0.9
675	    spearman_p: 0.037
676	    pearson_r: -0.82
677	    pearson_p: 0.089
678	    threshold_estimate: max_jaccard ≈ 0.45 (CSS advantage crosses zero)
679	    note: 'Spearman p=0.037 因为 5 个 data points 刚过 significance threshold， 但 Pearson
680	      p=0.089 不显著。Reviewer 会质疑 n=5 的统计力。 如果只看 3 个 GPT-2 tasks，Spearman 无法计算 meaningful
681	      p-value。
682	
683	      '
684	  result_rationale: '5 个 model×task 数据点显示清晰的负相关趋势：max_jaccard 越高，CSS advantage 越低。Spearman
685	    rho=-0.90 方向非常一致（只有 SVA 和 Qwen IOI 的排序有微小扰动）。 但 n=5 的统计检验力极弱——Spearman p=0.037
686	    刚好显著，Pearson 不显著。这是 因为 5 个点中有 3 个 "extremes"（IOI GPT-2 clearly positive，两个 Arithmetic
687	    clearly negative），中间的 SVA 和 Qwen IOI 决定了趋势的精确斜率但不足以 firm up p-value。如果只看 3 个 GPT-2
688	    任务（plan 最初设计），完全无法做统计检验； 加入 Qwen 的 2 个数据点后勉强可以报告 Spearman。 论文中应 claim "observed
689	    negative correlation consistent with hypothesis" 而非 "established significant correlation"。threshold
690	    ≈ 0.45 只是 visual estimate from 5 points，不具预测力。
691	
692	    '
693	  tables:
694	  - name: 'Table: Jaccard vs CSS Advantage (all model×task)'
695	    columns:
696	    - Task
697	    - Model
698	    - Max Jaccard
699	    - CSS Adv (CPR)
700	    - CSS Wins?
701	    rows:
702	    - - IOI
703	      - GPT-2
704	      - 0.31
705	      - '+0.021'
706	      - ✓
707	    - - SVA
708	      - GPT-2
709	      - 0.38
710	      - −0.012
711	      - ✗ (marginal)
712	    - - IOI
713	      - Qwen-0.5B
714	      - 0.55
715	      - '+0.012'
716	      - ✓ (marginal)
717	    - - Arithmetic
718	      - Qwen-0.5B
719	      - 0.61
720	      - −0.039
721	      - ✗
722	    - - Arithmetic
723	      - GPT-2
724	      - 0.695
725	      - −0.066
726	      - ✗
727	  figures_description:
728	  - 'Fig (KEY FIGURE): Scatter plot — x: max pairwise Jaccard, y: CSS CPR advantage.
729	    5 points with linear fit and 95% CI band. Vertical dashed line at Jaccard≈0.45.
730	    Points colored by task type (shape) and model (color).'
731	  - 'Fig: Heatmap — rows=tasks, cols=method pairs, cells=Jaccard values. Annotated
732	    with CSS outcome per task.'
733	  analysis: 这是 Claim 2 的核心 figure，也是论文能否从 "anecdotal 2-task observation" 升级为 "systematic
734	    pattern" 的关键。5 个数据点的 Spearman rho=-0.90 (p=0.037) 在 技术上可以 claim significance，但
735	    reviewer 很可能指出：(1) n=5 统计力不足， (2) IOI 和 Arithmetic 是 "designed" 对比（一个 localized
736	    一个 distributed）， 不是 random sample，(3) SVA 和 Qwen IOI 的 "marginal" 结果可以翻转。 应对策略：(1)
737	    不 over-claim，用 "observed trend" 而非 "significant correlation"； (2) 强调 mechanistic
738	    motivation（Jaccard 度量 method independence → independence 是 consensus 有价值的前提条件）比纯统计论证更重要；(3)
739	    提供 threshold 的 practical guidance（"practitioners should check Jaccard before applying
740	    CSS"）作为 actionable takeaway。
741	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52f702b3-46e9-41b9-865c-abd86d9d9ff0",
  "isSidechain": false,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "type": "user",
  "uuid": "5bb2718f-04c9-45aa-986e-912e463c2635",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/imagined_experiments.yaml",
      "content": "tier: median\nnarrative_guidance: '论文重心从 \"CSS empirically superior\" 转向 \"CSS as analytical framework\n  + binarization pathology\"。 SVA 提供第三个数据点但 CSS 优势不明显（CPR 差距 < 0.02），仅能 claim \"comparable\n  faithfulness at fraction of edges\"。Jaccard-utility 趋势方向正确（3 点 Spearman ≈ 0.87）但无法做统计检验（p\n  > 0.3）， 降级为 \"observed trend\"。DocQA 第四任务因 GPT-2 Small 能力不足未产出 clean circuit，被砍掉。\n  IFR 加入 Qwen IOI 后某些 pair Jaccard 降低但 IFR×EP 高度相关（~0.55），CSS 优势被稀释。 Claim 3（binarization\n  pathology）和 Claim 4（CSS taxonomy）成为最坚实的 methodological contribution。 仍可投 EMNLP main，framing\n  为 analytical/diagnostic framework，reviewer 主攻点在 n=3 泛化性 和 ACDC top-k 的 degree of\n  freedom。\n\n  '\nimagined_experiments:\n- name: GPT-2 SVA K=3 CSS\n  plan_id: plan_004\n  description: 'Subject-Verb Agreement on GPT-2 Small, K=3 (EAP-IG + EP + ACDC with\n    top-k=75). SVA 是相对 localized 的语法任务，预期方法间有中等分歧。\n\n    '\n  expected_results:\n    status: done\n    conclusion: partial_support\n    pairwise_jaccard:\n      eapig_x_ep: 0.38\n      eapig_x_acdc_k75: 0.18\n      ep_x_acdc_k75: 0.15\n    max_jaccard: 0.38\n    three_way_ratio: 0.067\n    circuit_sizes:\n      eapig_k75: 75\n      ep_k75: 75\n      acdc_k75: 75\n      acdc_isinf: 22\n    css_distribution:\n      1/3: 148\n      2/3: 54\n      3/3: 23\n    faithfulness_mean:\n      css_1.00_k75:\n        edges: 23\n        CPR: 0.941\n        CMD: 0.263\n      css_0.67_k75:\n        edges: 54\n        CPR: 0.958\n        CMD: 0.189\n      eapig_k75:\n        edges: 75\n        CPR: 0.953\n        CMD: 0.211\n      ep_k75:\n        edges: 75\n        CPR: 0.937\n        CMD: 0.284\n      acdc_k75:\n        edges: 75\n        CPR: 0.922\n        CMD: 0.347\n    faithfulness_isinf_degeneration:\n      css_1.00_isinf:\n        edges: 22\n        CPR: 0.918\n        CMD: 0.368\n      acdc_isinf:\n        edges: 22\n        CPR: 0.918\n        CMD: 0.368\n      degeneration_confirmed: true\n    css1_cpr_advantage_over_best: -0.012\n    css1_edge_ratio: 0.307\n    sva_gate_verdict: MARGINAL — CSS=1.0 CPR comparable but not superior; edge efficiency\n      3.3x\n  result_rationale: 'SVA 在 GPT-2 Small 上的电路比 IOI 更 localized（主要涉及 subject token 到\n    verb position 的 attention + 少量 MLP），但不如 IOI 那样有清晰的 \"备份名字\" 结构驱动方法分歧。EAP-IG 和 EP\n    作为 gradient-adjacent 方法在 SVA 上 Jaccard=0.38（高于 IOI 的 0.31），因为 SVA 的 gradient landscape\n    比 IOI 更平滑——主谓一致主要依赖几个 key attention head，gradient 方法容易收敛到 类似子集。ACDC top-k=75 normalization\n    打破了 isinf 退化（isinf 只有 22 条 edge），但引入了 k 的选择作为额外自由度。CSS=1.0 包含 23 条边，CPR=0.941\n    略低于 EAP-IG 的 0.953（差距 0.012）， 说明全共识子集在去除了各方法的 \"独特发现\" 后损失了少量信息。这符合 median 档预期：CSS\n    部分支持 但不完美，edge efficiency 优势（3.3x fewer edges）是实在的，但 faithfulness 并无优势。\n\n    '\n  tables:\n  - name: 'Table: SVA Faithfulness Comparison (mean ablation, top-k=75)'\n    columns:\n    - Circuit\n    - Edges\n    - CPR ↑\n    - CMD ↓\n    - Edge Ratio\n    rows:\n    - - CSS=1.0 (k=75)\n      - 23\n      - 0.941\n      - 0.263\n      - 0.31x\n    - - CSS≥0.67 (k=75)\n      - 54\n      - 0.958\n      - 0.189\n      - 0.72x\n    - - EAP-IG (k=75)\n      - 75\n      - 0.953\n      - 0.211\n      - 1.00x\n    - - EP (k=75)\n      - 75\n      - 0.937\n      - 0.284\n      - 1.00x\n    - - ACDC (k=75)\n      - 75\n      - 0.922\n      - 0.347\n      - 1.00x\n    - - ACDC (isinf)\n      - 22\n      - 0.918\n      - 0.368\n      - 0.29x\n  - name: 'Table: SVA Pairwise Jaccard (top-k=75)'\n    columns:\n    - ''\n    - EAP-IG\n    - EP\n    - ACDC\n    rows:\n    - - EAP-IG\n      - —\n      - 0.38\n      - 0.18\n    - - EP\n      - 0.38\n      - —\n      - 0.15\n    - - ACDC\n      - 0.18\n      - 0.15\n      - —\n  figures_description:\n  - 'Fig: SVA CSS distribution histogram (1/3, 2/3, 3/3) — 与 IOI 对比显示更集中的分布'\n  - 'Fig: SVA edge overlap Venn diagram (3 methods, top-k=75)'\n  analysis: 'SVA 结果处于 IOI（CSS clear win）和 Arithmetic（CSS clear loss）之间的灰色地带。 CSS=1.0\n    用 23 条边达到了 75 条边 EAP-IG 的 98.7% faithfulness (0.941/0.953)， edge efficiency 论点成立但\n    CPR 没有优势。关键问题：top-k=75 是 SVA 上的最优 k， k=50 时 CSS=1.0 只有 15 条边且 CPR 降到 0.89，k=100\n    时 CSS=1.0 有 31 条边但 CPR 不再提升——这个 k-sensitivity 是 reviewer 可攻击的 degree of freedom。\n    对 Claim 1 的贡献：降级为 \"comparable faithfulness at fraction of edges\"。 对 Claim 2 的贡献：Jaccard=0.38\n    + CSS marginal → 第三个数据点，位于 IOI 和 Arithmetic 之间，方向一致。\n\n    '\n- name: GPT-2 DocQA/Factual K=3 CSS\n  plan_id: plan_005\n  description: 'Distributed computation task on GPT-2 Small. 预期高 Jaccard → CSS 应该失败（确认模式）。\n\n    '\n  expected_results:\n    status: abandoned\n    conclusion: data_not_clean\n    partial_metrics:\n      eapig_completed: true\n      ep_completed: true\n      acdc_completed: false\n      acdc_failure_reason: GPT-2 Small factual recall 太弱，ACDC 收敛到近空电路（< 5 edges）\n    note: ACDC 无法产出有意义的电路，实验被终止。不纳入论文分析。\n  result_rationale: 'GPT-2 Small (117M) 的 factual knowledge 极为有限，DocQA/Factual recall\n    任务上 模型本身准确率不稳定（~55-65% vs random 25%）。EAP-IG 和 EP 可以强行产出 top-k 电路，但 ACDC 的 patching-based\n    搜索在 clean performance 不稳定时无法收敛—— 阈值过高则电路为空，过低则几乎保留全图。尝试调低阈值后得到 3-5 条 isinf 边，\n    top-k normalization 后虽能凑出 50-75 条边但其 faithfulness 接近随机（CPR ≈ 0）。 这不是 CSS 方法的失败而是\n    task-model 匹配问题。在 deadline 压力下（ARR 5/25） 决定放弃第四任务，论文保持 3 个任务（IOI + Arithmetic\n    + SVA）。\n\n    '\n  tables: []\n  figures_description: []\n  analysis: '第四任务失败是 median 档的核心限制。论文需要在 Limitations 中说明 GPT-2 Small 对 factual recall\n    的能力不足以支撑 circuit discovery，并将 broader task coverage 列为 future work。这会成为 reviewer\n    攻击的主要靶点（\"only 3 tasks on one model\"）。 应对策略：强调 3 个任务已覆盖 localized（IOI）、distributed（Arithmetic）、\n    intermediate（SVA）三种电路结构类型，以及 Qwen 上的 cross-model validation。\n\n    '\n- name: Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + IFR)\n  plan_id: plan_006\n  description: '首次 larger model + IFR 作为第三方法（替换 ACDC）。IFR 是 similarity-based 方法， 与\n    gradient 方法家族不同，预期降低 Jaccard。\n\n    '\n  expected_results:\n    status: done\n    conclusion: mixed\n    pairwise_jaccard:\n      eapig_x_ep: 0.42\n      eapig_x_ifr: 0.19\n      ep_x_ifr: 0.55\n    max_jaccard: 0.55\n    three_way_ratio: 0.082\n    circuit_sizes:\n      eapig_k75: 75\n      ep_k75: 75\n      ifr_k75: 75\n    css_distribution:\n      1/3: 143\n      2/3: 63\n      3/3: 19\n    faithfulness_mean:\n      css_1.00:\n        edges: 19\n        CPR: 0.103\n        CMD: 0.921\n      css_0.67:\n        edges: 63\n        CPR: 0.087\n        CMD: 0.944\n      eapig_k75:\n        edges: 75\n        CPR: 0.091\n        CMD: 0.938\n      ep_k75:\n        edges: 75\n        CPR: 0.078\n        CMD: 0.952\n      ifr_k75:\n        edges: 75\n        CPR: 0.064\n        CMD: 0.967\n    css1_cpr: 0.103\n    css1_vs_best_single: 0.012\n    ifr_ep_correlation_note: 'IFR×EP Jaccard=0.55 远高于预期。IFR 虽然是 similarity-based，但在\n      IOI 上 EP 的 edge importance 与 IFR 的 representation similarity 高度一致—— 可能因为 IOI\n      的 backup name 机制使得 \"重要的边\" 在两种度量下都突出。 这削弱了 K≈3 independent methods 的假设，实际独立证据更接近\n      K≈2.3。\n\n      '\n  result_rationale: 'Qwen-2.5 0.5B 上 IOI 的电路结构与 GPT-2 类似（名字 mover head + backup 机制），\n    但模型更大导致电路更分散。EAP-IG×EP 的 Jaccard 从 GPT-2 的 0.31 升至 0.42， 因为 Qwen 的 gradient landscape\n    更平滑（more parameters → gradient 更 concentrated on true signal）。IFR 作为 similarity-based\n    方法确实与 EAP-IG 差异大（Jaccard=0.19）， 但与 EP 的 Jaccard 意外达到 0.55——这是因为 EP 的 edge pruning\n    和 IFR 的 representation similarity 都偏好 \"移除后 representation 变化大\" 的边，两者在 measurement\n    层面有隐含重叠。CSS=1.0 的 19 条边 CPR=0.103 略好于 GPT-2 IOI 的 0.109 （量级一致），表明 CSS 在 larger\n    model 上仍然能提取 faithful 子集。但 max_jaccard=0.55 使得这个数据点在 Jaccard-utility 图上落在不太理想的位置——CSS\n    优势有限（+0.012 over EAP-IG）且 Jaccard 不够低。IFR 混入了与 EP 相关的信号，有效独立方法数 < 3。\n\n    '\n  tables:\n  - name: 'Table: Qwen-0.5B IOI Faithfulness (mean ablation, k=75)'\n    columns:\n    - Circuit\n    - Edges\n    - CPR ↑\n    - CMD ↓\n    rows:\n    - - CSS=1.0\n      - 19\n      - 0.103\n      - 0.921\n    - - CSS≥0.67\n      - 63\n      - 0.087\n      - 0.944\n    - - EAP-IG\n      - 75\n      - 0.091\n      - 0.938\n    - - EP\n      - 75\n      - 0.078\n      - 0.952\n    - - IFR\n      - 75\n      - 0.064\n      - 0.967\n  - name: 'Table: Qwen-0.5B IOI Pairwise Jaccard'\n    columns:\n    - ''\n    - EAP-IG\n    - EP\n    - IFR\n    rows:\n    - - EAP-IG\n      - —\n      - 0.42\n      - 0.19\n    - - EP\n      - 0.42\n      - —\n      - 0.55\n    - - IFR\n      - 0.19\n      - 0.55\n      - —\n  figures_description:\n  - 'Fig: Qwen IOI CSS distribution vs GPT-2 IOI — 对比两个 model scale 下的 CSS 分布形态'\n  - 'Fig: IFR vs EP edge importance scatter plot — 显示 Jaccard=0.55 的来源'\n  analysis: 'Qwen IOI 结果是 \"mixed\" 的典型案例。好消息：CSS=1.0 在 larger model 上仍然 work， CPR 略优于\n    best single method，证明 CSS 框架可跨模型。坏消息：IFR×EP Jaccard=0.55 说明 \"不同算法家族 → 低相关\" 的假设不总成立——算法差异不等于\n    measurement independence。 这对 Claim 2 有双重影响：(1) max_jaccard=0.55 + CSS marginal\n    win 支持 \"中等 Jaccard → 中等 CSS 收益\" 的连续关系假设；(2) 但也说明 Jaccard 可能需要分 pair 解读而非只看 max。\n    论文中应在 Discussion 讨论 IFR-EP 相关性的 mechanistic 原因。\n\n    '\n- name: Qwen-2.5 0.5B Arithmetic K=3\n  plan_id: plan_007\n  description: 'Qwen 上的 Arithmetic (Greaterthan) task，IFR 替换 ACDC。 验证 IFR 是否能降低 Arithmetic\n    的 Jaccard 使 CSS recover。\n\n    '\n  expected_results:\n    status: done\n    conclusion: negative\n    pairwise_jaccard:\n      eapig_x_ep: 0.61\n      eapig_x_ifr: 0.38\n      ep_x_ifr: 0.48\n    max_jaccard: 0.61\n    three_way_ratio: 0.195\n    css_distribution:\n      1/3: 98\n      2/3: 73\n      3/3: 54\n    faithfulness_mean:\n      css_1.00:\n        edges: 54\n        CPR: 0.932\n        CMD: 0.302\n      eapig_k75:\n        edges: 75\n        CPR: 0.971\n        CMD: 0.128\n      ep_k75:\n        edges: 75\n        CPR: 0.955\n        CMD: 0.199\n      ifr_k75:\n        edges: 75\n        CPR: 0.891\n        CMD: 0.487\n    css1_cpr_advantage_over_best: -0.039\n    note: 'IFR 将 max_jaccard 从 GPT-2 的 0.695 降至 0.61，但仍不够低。 CSS=1.0 CPR=0.932 < EAP-IG=0.971。CSS\n      未 recover。\n\n      '\n  result_rationale: 'Arithmetic/Greaterthan 任务的电路结构本质上是 distributed 的——多个 MLP layer\n    协同完成数值比较，gradient-based 方法容易收敛到相似的关键路径。IFR 替换 ACDC 后 确实降低了 max_jaccard（0.695 →\n    0.61），但降幅不够大。原因：Arithmetic 的 \"重要边\" 集中在少数 MLP 到 final position 的连接上，无论用 gradient\n    (EAP-IG/EP) 还是 similarity (IFR)，这些边都会被 rank 到顶部。IFR 本身表现较弱（CPR=0.891）， 拖累了 CSS=1.0\n    的质量——共识要求三方都同意的边包含了 IFR 的一些 false positive。 这个结果实际上支持 Claim 2：Jaccard 仍然偏高（0.61）→\n    CSS 仍然不优—— 趋势一致，但不是正面结果。\n\n    '\n  tables:\n  - name: 'Table: Qwen-0.5B Arithmetic Faithfulness (mean ablation)'\n    columns:\n    - Circuit\n    - Edges\n    - CPR ↑\n    - CMD ↓\n    rows:\n    - - CSS=1.0\n      - 54\n      - 0.932\n      - 0.302\n    - - EAP-IG (k=75)\n      - 75\n      - 0.971\n      - 0.128\n    - - EP (k=75)\n      - 75\n      - 0.955\n      - 0.199\n    - - IFR (k=75)\n      - 75\n      - 0.891\n      - 0.487\n  figures_description:\n  - 'Fig: Qwen Arithmetic CSS distribution — 与 GPT-2 Arithmetic 对比'\n  analysis: 'IFR \"部分修复\" 了 Arithmetic 的 Jaccard 问题但不够彻底。从 Claim 2 角度看 这其实是一个有价值的 intermediate\n    data point：Jaccard 从 0.695 降到 0.61， CSS 优势从 -0.066 改善到 -0.039，方向正确但仍为负。如果画 Jaccard\n    vs CSS_advantage 的图，这个点和 GPT-2 Arithmetic 几乎在同一条趋势线上。 问题在于 IFR 本身在 Arithmetic\n    上的 faithfulness 较差（CPR=0.891 远低于 EAP-IG 的 0.971），说明 similarity-based method 对\n    distributed computation 的识别 能力有限——这是一个独立的 finding，可在 Discussion 中报告。\n\n    '\n- name: Gemma-2 2B IOI K=3\n  plan_id: plan_008\n  description: Scale to 2B model (Gemma-2). P2 优先级。\n  expected_results:\n    status: not_attempted\n    conclusion: null\n    reason: 时间和 GPU 资源不足，P1 任务已消耗大部分 budget。列入 Future Work。\n  result_rationale: 'Median 档的时间约束（ARR 5/25 deadline）下，plan_004 (SVA) + plan_006 (Qwen\n    IOI) + plan_007 (Qwen Arith) 已消耗约 20 GPU-hours。Gemma-2 2B 需要 16 GPU-hours 且 依赖\n    plan_006 结果（IFR pipeline 验证）。即使 plan_006 顺利完成，剩余时间不足 以完成 Gemma-2 实验 + 分析 + 论文写作。P2\n    优先级下被合理推迟。\n\n    '\n  tables: []\n  figures_description: []\n  analysis: Not attempted. 在 Limitations 中列为 model scale generalization future work。\n- name: Llama-3.1 8B IOI K=3\n  plan_id: plan_009\n  description: Scale to 8B model. P3 优先级。Needs A100 80GB。\n  expected_results:\n    status: not_attempted\n    conclusion: null\n    reason: P3 优先级，且 plan_008 未完成作为前置。远超 deadline 范围。\n  result_rationale: '8B 模型实验需要 A100 80GB（当前设备可能不支持 EP 的内存需求），且依赖 plan_008。 在 median\n    档下属于完全不现实的目标。\n\n    '\n  tables: []\n  figures_description: []\n  analysis: Not attempted. Future work 中的 stretch goal。\n- name: Binarization sensitivity ablation\n  plan_id: plan_010\n  description: 'Systematic k sweep (k=50/75/100/150) on all completed model×task pairs.\n    验证 CSS 在不同 k 下的稳定性。\n\n    '\n  expected_results:\n    status: done\n    conclusion: partially_stable\n    ioi_gpt2_k_sweep:\n      k50:\n        css_1.0_edges: 12\n        css_1.0_cpr: 0.098\n      k75:\n        css_1.0_edges: 18\n        css_1.0_cpr: 0.112\n      k100:\n        css_1.0_edges: 24\n        css_1.0_cpr: 0.109\n      k150:\n        css_1.0_edges: 31\n        css_1.0_cpr: 0.108\n      verdict: stable (CPR range 0.098-0.112, Δ=0.014)\n    arithmetic_gpt2_k_sweep:\n      k50:\n        css_1.0_edges: 44\n        css_1.0_cpr: 0.919\n      k75:\n        css_1.0_edges: 54\n        css_1.0_cpr: 0.919\n      k100:\n        css_1.0_edges: 62\n        css_1.0_cpr: 0.926\n      k150:\n        css_1.0_edges: 71\n        css_1.0_cpr: 0.933\n      verdict: stable (CPR range 0.919-0.933, Δ=0.014)\n    sva_gpt2_k_sweep:\n      k50:\n        css_1.0_edges: 15\n        css_1.0_cpr: 0.891\n      k75:\n        css_1.0_edges: 23\n        css_1.0_cpr: 0.941\n      k100:\n        css_1.0_edges: 29\n        css_1.0_cpr: 0.944\n      k150:\n        css_1.0_edges: 38\n        css_1.0_cpr: 0.94\n      verdict: sensitive at k=50 (CPR drop 0.05), stable k=75-150\n    qwen_ioi_k_sweep:\n      k50:\n        css_1.0_edges: 11\n        css_1.0_cpr: 0.082\n      k75:\n        css_1.0_edges: 19\n        css_1.0_cpr: 0.103\n      k100:\n        css_1.0_edges: 26\n        css_1.0_cpr: 0.099\n      k150:\n        css_1.0_edges: 35\n        css_1.0_cpr: 0.097\n      verdict: stable k=75-150, drop at k=50\n    overall_verdict: 'CSS=1.0 CPR 在 k=75-150 范围内对所有 task 稳定（max Δ < 0.015）。 k=50 在\n      SVA 和 Qwen IOI 上 CPR 下降 ~0.04-0.05，因为 k=50 过小导致方法 重叠不足、CSS=1.0 边数太少。推荐 k=75\n      作为默认值，但需要在论文中报告这个选择。\n\n      '\n  result_rationale: 'Top-k normalization 的核心逻辑是让 ACDC 和其他方法在同一 edge budget 下比较。 k=75-150\n    范围内，三种方法各自选择的 top edges 有足够的 overlap base 使 CSS=1.0 稳定。k=50 时边太少，方法间 overlap 降到\n    noise level，CSS=1.0 变得不可靠。 SVA 比 IOI 更敏感于 k 的原因：SVA 电路更 concentrated（少数 critical\n    edges 占比更大），k=50 可能恰好切掉了某些方法的 borderline critical edge。 这个 sensitivity 是 median\n    档的典型问题——结果 \"基本稳定但有 caveat\"， reviewer 可以攻击 k=75 的选择是 cherry-picked（虽然实际不是）。\n\n    '\n  tables:\n  - name: 'Table: CSS=1.0 CPR across k values (all tasks)'\n    columns:\n    - Task\n    - k=50\n    - k=75\n    - k=100\n    - k=150\n    - Max Δ\n    rows:\n    - - IOI (GPT-2)\n      - 0.098\n      - 0.112\n      - 0.109\n      - 0.108\n      - 0.014\n    - - Arith (GPT-2)\n      - 0.919\n      - 0.919\n      - 0.926\n      - 0.933\n      - 0.014\n    - - SVA (GPT-2)\n      - 0.891\n      - 0.941\n      - 0.944\n      - 0.94\n      - 0.053\n    - - IOI (Qwen)\n      - 0.082\n      - 0.103\n      - 0.099\n      - 0.097\n      - 0.021\n  figures_description:\n  - 'Fig: Line plot of CSS=1.0 CPR vs k for all 4 model×task configs — 灰色 band 标记\n    k=75-150 稳定区间'\n  analysis: 'Binarization ablation 的结论可以支撑 Claim 3（top-k 修复 isinf 退化）， 但 SVA k=50\n    的 sensitivity 会被 reviewer 追问。应对：(1) 论文推荐 k=75 并展示 full sweep 数据，(2) argue k=50\n    本身就低于合理下界（只保留 0.15% edges for GPT-2 的 32k+ edge graph），(3) 指出 k=75-150 的 CPR 标准差\n    < 0.01。\n\n    '\n- name: Ablation method comparison (zero vs mean vs resample)\n  plan_id: plan_011\n  description: 'Compare ablation methods on all tasks. P2 优先级。 验证 CSS advantage 不依赖特定\n    evaluation ablation。\n\n    '\n  expected_results:\n    status: partial\n    conclusion: inconclusive\n    completed_tasks:\n    - IOI (GPT-2)\n    ioi_gpt2:\n      zero_ablation:\n        css_1.0_cpr: 0.109\n        best_single_cpr: 0.029\n        css_advantage: 0.08\n      mean_ablation:\n        css_1.0_cpr: 0.112\n        best_single_cpr: 0.091\n        css_advantage: 0.021\n      resample_ablation:\n        css_1.0_cpr: 0.095\n        best_single_cpr: 0.082\n        css_advantage: 0.013\n    note: '仅完成 IOI 一个 task 的三种 ablation 对比。CSS advantage 在三种 ablation 下 方向一致（正），但绝对值差异大（0.013-0.080）。SVA\n      和 Arithmetic 未完成。\n\n      '\n  result_rationale: '这是 P2 优先级实验，在 SVA (plan_004) 和 Qwen (plan_006/007) 完成后 时间已所剩不多。仅对\n    IOI 跑了 zero/mean/resample 三种 ablation， 因为 IOI 是唯一 CSS clearly wins 的 task。结果显示\n    CSS 优势在三种 ablation 下都为正但量级不同：zero ablation 下优势最大（因为 zero ablation 对电路外 edge 的破坏最大，小电路受益最多），resample\n    下优势最小。这表明 CSS advantage 不是 ablation method artifact，但缺少 SVA 和 Arithmetic 的对比数据使结论不完整。\n\n    '\n  tables:\n  - name: 'Table: IOI CSS advantage under different ablation methods'\n    columns:\n    - Ablation\n    - CSS=1.0 CPR\n    - Best Single CPR\n    - Advantage\n    rows:\n    - - Zero\n      - 0.109\n      - 0.029\n      - '+0.080'\n    - - Mean\n      - 0.112\n      - 0.091\n      - '+0.021'\n    - - Resample\n      - 0.095\n      - 0.082\n      - '+0.013'\n  figures_description: []\n  analysis: '部分完成的 ablation 对比。IOI 结果可以放在 Appendix 中作为 robustness check。 关键 takeaway：CSS\n    advantage 在 mean ablation（最常用）下为 +0.021，在 resample （最严格）下为 +0.013，都是正的。但仅一个 task\n    不足以 claim robustness。 论文中可以 footnote 提及 IOI 上的一致性，full multi-task ablation 列为\n    future work。\n\n    '\n- name: CIRCUS as negative ablation\n  plan_id: plan_012\n  description: '使用 D021 中 CIRCUS 的已有失败结果作为 negative ablation。 0 GPU hours，仅需分析和写作。\n\n    '\n  expected_results:\n    status: done\n    conclusion: negative_ablation_confirmed\n    circus_vs_css:\n      ioi_circus_core_cpr: -0.108\n      ioi_css_1.0_cpr: 0.109\n      ioi_circus_core_edges: 15\n      ioi_css_1.0_edges: 7\n    circus_failure_modes:\n    - CIRCUS 基于 single-method faithfulness scoring 选 core edges，但 scoring 本身依赖 ablation\n      noise\n    - 'CIRCUS D021 三次运行结果不一致（edges: 12, 15, 18），说明 threshold sensitivity 严重'\n    - CSS 的 binary consensus 不需要 score calibration，避免了 CIRCUS 的核心缺陷\n  result_rationale: 'CIRCUS (Parekh 2026) 在 IOI 上的 D021 结果已有：core edges CPR=-0.108（负值，\n    说明 CIRCUS core 实际上破坏了模型行为）。相比 CSS=1.0 的 CPR=0.109，差距极大。 CIRCUS 失败的根本原因是它在 single\n    method 内部做 faithfulness scoring 来选 core， 但这个 scoring 对 threshold 和 ablation method\n    极其敏感。CSS 通过 cross-method binary agreement 绕过了 score calibration 问题。这个对比自然成为论文中\n    Claim 4 的关键证据：structural consensus (CSS) > faithfulness scoring (CIRCUS)。\n\n    '\n  tables:\n  - name: 'Table: CSS vs CIRCUS on IOI (negative ablation)'\n    columns:\n    - Method\n    - Edges\n    - CPR ↑\n    - CMD ↓\n    - Stable?\n    rows:\n    - - CSS=1.0\n      - 7\n      - 0.109\n      - 0.911\n      - Yes (3/3 runs identical)\n    - - CIRCUS core\n      - 15\n      - -0.108\n      - 1.134\n      - No (12-18 edges across runs)\n  figures_description:\n  - 'Fig: CSS vs CIRCUS edge selection comparison — 显示两种方法选择的 edge 集合差异'\n  analysis: 'CIRCUS negative ablation 是 Claim 4 最有力的证据，也是论文中最 \"clean\" 的结果之一。 CSS=1.0\n    用更少的边（7 vs 15）达到正的 CPR，而 CIRCUS core 的 CPR 为负。 关键论点：binary consensus across methods\n    比 within-method score selection 更稳定， 因为前者不需要 score calibration，后者严重依赖 ablation\n    method 和 threshold。 这是 methodological contribution 的核心，reviewer 较难攻击（结果清晰、对比公平）。\n\n    '\n- name: Jaccard-CSS correlation analysis\n  plan_id: plan_013\n  description: 'Across all model×task pairs, plot max pairwise Jaccard vs CSS faithfulness\n    advantage. 3 个 task data points + Qwen cross-validation。\n\n    '\n  expected_results:\n    status: done\n    conclusion: trend_observed_no_statistical_power\n    data_points:\n    - task: IOI (GPT-2)\n      max_jaccard: 0.31\n      css_advantage: 0.021\n      css_wins: true\n    - task: Arithmetic (GPT-2)\n      max_jaccard: 0.695\n      css_advantage: -0.066\n      css_wins: false\n    - task: SVA (GPT-2)\n      max_jaccard: 0.38\n      css_advantage: -0.012\n      css_wins: false\n    - task: IOI (Qwen)\n      max_jaccard: 0.55\n      css_advantage: 0.012\n      css_wins: true\n    - task: Arithmetic (Qwen)\n      max_jaccard: 0.61\n      css_advantage: -0.039\n      css_wins: false\n    spearman_rho: -0.9\n    spearman_p: 0.037\n    pearson_r: -0.82\n    pearson_p: 0.089\n    threshold_estimate: max_jaccard ≈ 0.45 (CSS advantage crosses zero)\n    note: 'Spearman p=0.037 因为 5 个 data points 刚过 significance threshold， 但 Pearson\n      p=0.089 不显著。Reviewer 会质疑 n=5 的统计力。 如果只看 3 个 GPT-2 tasks，Spearman 无法计算 meaningful\n      p-value。\n\n      '\n  result_rationale: '5 个 model×task 数据点显示清晰的负相关趋势：max_jaccard 越高，CSS advantage 越低。Spearman\n    rho=-0.90 方向非常一致（只有 SVA 和 Qwen IOI 的排序有微小扰动）。 但 n=5 的统计检验力极弱——Spearman p=0.037\n    刚好显著，Pearson 不显著。这是 因为 5 个点中有 3 个 \"extremes\"（IOI GPT-2 clearly positive，两个 Arithmetic\n    clearly negative），中间的 SVA 和 Qwen IOI 决定了趋势的精确斜率但不足以 firm up p-value。如果只看 3 个 GPT-2\n    任务（plan 最初设计），完全无法做统计检验； 加入 Qwen 的 2 个数据点后勉强可以报告 Spearman。 论文中应 claim \"observed\n    negative correlation consistent with hypothesis\" 而非 \"established significant correlation\"。threshold\n    ≈ 0.45 只是 visual estimate from 5 points，不具预测力。\n\n    '\n  tables:\n  - name: 'Table: Jaccard vs CSS Advantage (all model×task)'\n    columns:\n    - Task\n    - Model\n    - Max Jaccard\n    - CSS Adv (CPR)\n    - CSS Wins?\n    rows:\n    - - IOI\n      - GPT-2\n      - 0.31\n      - '+0.021'\n      - ✓\n    - - SVA\n      - GPT-2\n      - 0.38\n      - −0.012\n      - ✗ (marginal)\n    - - IOI\n      - Qwen-0.5B\n      - 0.55\n      - '+0.012'\n      - ✓ (marginal)\n    - - Arithmetic\n      - Qwen-0.5B\n      - 0.61\n      - −0.039\n      - ✗\n    - - Arithmetic\n      - GPT-2\n      - 0.695\n      - −0.066\n      - ✗\n  figures_description:\n  - 'Fig (KEY FIGURE): Scatter plot — x: max pairwise Jaccard, y: CSS CPR advantage.\n    5 points with linear fit and 95% CI band. Vertical dashed line at Jaccard≈0.45.\n    Points colored by task type (shape) and model (color).'\n  - 'Fig: Heatmap — rows=tasks, cols=method pairs, cells=Jaccard values. Annotated\n    with CSS outcome per task.'\n  analysis: 这是 Claim 2 的核心 figure，也是论文能否从 \"anecdotal 2-task observation\" 升级为 \"systematic\n    pattern\" 的关键。5 个数据点的 Spearman rho=-0.90 (p=0.037) 在 技术上可以 claim significance，但\n    reviewer 很可能指出：(1) n=5 统计力不足， (2) IOI 和 Arithmetic 是 \"designed\" 对比（一个 localized\n    一个 distributed）， 不是 random sample，(3) SVA 和 Qwen IOI 的 \"marginal\" 结果可以翻转。 应对策略：(1)\n    不 over-claim，用 \"observed trend\" 而非 \"significant correlation\"； (2) 强调 mechanistic\n    motivation（Jaccard 度量 method independence → independence 是 consensus 有价值的前提条件）比纯统计论证更重要；(3)\n    提供 threshold 的 practical guidance（\"practitioners should check Jaccard before applying\n    CSS\"）作为 actionable takeaway。\n",
      "numLines": 741,
      "startLine": 1,
      "totalLines": 741
    }
  },
  "sourceToolAssistantUUID": "52f702b3-46e9-41b9-865c-abd86d9d9ff0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-13T08:31:47.594Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Vqg7FyvH1XuGAq19AeyDUw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bb2718f-04c9-45aa-986e-912e463c2635",
  "isSidechain": false,
  "requestId": "req_011CazFqtezGkRjU5DuXNCvi",
  "type": "assistant",
  "uuid": "8b407f6d-42cc-40ae-89a7-1198eb14f687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185pW3pYFnuJTFWnYZLFcQD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 31447,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12121,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 31447,
          "cache_creation_input_tokens": 12121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12121
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：SVA marginal PASS（统计上弱），Qwen ACDC 技术可行但结果 mixed；Jaccard-utility 趋势可见但数据点不足以达到统计显著 核心假设：['SVA css_1.00 Δ(CPR) ∈ [0.005, 0.03]，condition④ technically PASS…",
  "leafUuid": "fbb5ef92-7f72-423f-baad-a4b202a88471",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframed CSS paper: Jaccard-predicted utility",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb"
}
```

---

### Assistant

_source line 33 · 2026-05-13T08:32:18.086Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view. Let me also check: the user mentioned that the Phase 1 has defined the median tier's meaning, and now they want me to generate median-tier predictions for each planned experiment. Let me also check if there's a current dream session in progress and see the project context more carefully.

The key context updates for median tier:
1. SVA css_1.00 re-evaluated: possibly marginal PASS (Δ=0.0127)
2. D029: ACDC top-k replaces IFR (IFR Jaccard=0.000 on Qwen, incompatible)


3. Current results show IOI clearly passing, Arithmetic failing, SVA in marginal territory, and Qwen IFR deprecated, with only a 1/3 success rate across clear passes.

For the median tier predictions, I'm working with SVA as a marginal PASS with modest CPR improvements, Qwen ACDC as technically viable but showing mixed performance around 0.3-0.55 Jaccard, and reconsidering the remaining experiments.

I've got 4 valid data points showing the Jaccard-utility trend in the right direction but falling short of statistical significance. The CSS PASS rate for low Jaccard tasks sits around 50% when including marginal results. The key shift from the best tier is that SVA doesn't reach strong PASS status, Qwen switched to ACDC top-k instead of IFR, Factual Recall appears abandoned, and Gemma and Llama weren't attempted. The narrative needs reframing around this weaker but still directionally correct trend.

I'm checking the existing plan IDs—they run from plan_004 through plan_013 in the current median tier. Since the context changed with D029 replacing IFR with ACDC for Qwen, I need to reconstruct the median predictions with this new information. Now I'm stepping through each experiment starting with plan_004 for GPT-2 SV.

For the K=3 CSS variant, this work already exists in the registry as mvp_sva_gpt2_k3 and mvp_sva_gpt2_k3_topk. The median tier prediction shows SVA achieving css_1.00 with a CPR improvement between 0.005 and 0.03, technically passing condition④ but without strong statistical backing. Looking at the actual data, the SVA css_1.00 version gives a mean CPR of 1.1738 versus the best single model at 1.1676, yielding a delta of 0.0062. The topk variant shows 1.1873 versus 1.1703, giving 0.017. So the median prediction needs to align with this observed range.

GPT-2 on factual and document QA tasks is likely abandoned since the model lacks sufficient capacity for reliable factual recall. For Qwen-2.5 0.5B on IOI with K=3, I'm now using ACDC top-k instead of IFR, though the results are mixed with Jaccard scores between 0.3 and 0.55, and CSS results showing one pass, one fail, or mostly marginal outcomes. The arithmetic variant also switches to ACDC top-k but is expected to underperform given the high Jaccard difficulty. Gemma-2 2B on IOI hasn't been attempted yet, and Llama-3 is the next in the queue.

I've completed the binarization sensitivity sweep with partial stability, partially worked through ablation method comparisons, finished the CIRCUS negative ablation, and analyzed the Jaccard-CSS correlation with a few data points showing a visible trend but not statistically significant. Now I'm writing out the full YAML configuration, making sure the numbers align precisely with the defined ranges.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbb5ef92-7f72-423f-baad-a4b202a88471",
  "isSidechain": false,
  "requestId": "req_011CazFrcuE6AC584kuvuMA7",
  "type": "assistant",
  "uuid": "e74c755c-127c-48a6-93ee-0f4c26a5314e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPcQmLKUFVtbyh8EqdcwKw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14866,
      "cache_read_input_tokens": 43568,
      "output_tokens": 14989,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14989,
          "cache_read_input_tokens": 43568,
          "cache_creation_input_tokens": 14866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14866
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

_source line 34 · 2026-05-13T08:32:18.231Z_

Now I have all the context. Let me construct the median tier imagined experiments based on the updated project state (D029: ACDC top-k replaces IFR, SVA marginal, css_0.67 bug, etc.).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e74c755c-127c-48a6-93ee-0f4c26a5314e",
  "isSidechain": false,
  "requestId": "req_011CazFrcuE6AC584kuvuMA7",
  "type": "assistant",
  "uuid": "8d8d91eb-e26c-46f5-aff8-67a9bac611fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPcQmLKUFVtbyh8EqdcwKw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14866,
      "cache_read_input_tokens": 43568,
      "output_tokens": 14989,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14989,
          "cache_read_input_tokens": 43568,
          "cache_creation_input_tokens": 14866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14866
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

_source line 35 · 2026-05-13T08:37:01.127Z_

<details open><summary>🔧 Tool call — Write · `toolu_01GHGiMQYcyVkc1WqwLk8nox`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/median/imagined_experiments.yaml",
  "content": "tier: median\nnarrative_guidance: >\n  需要 reframe。降级 Claim 1 为 conditional result，升级 Claim 2 和 Claim 3 为主线。\n  叙事变为：\"CSS 的有效性取决于方法多样性，我们提供诊断框架（Jaccard 作为先验预测指标）帮助从业者判断何时值得做 consensus。\"\n  Arithmetic 高 Jaccard → CSS 失败成为核心 supporting evidence 而非 negative result。\n  SVA 描述为 \"borderline case consistent with moderate Jaccard\" 而非 strong positive。\n  论文从 \"CSS always works\" 变为 \"CSS works iff methods are diverse, and we can predict when\"。\n  仍可投 EMNLP，但需要诚实的 limitation section 承认数据点有限。\n  关键更新：D029 用 ACDC top-k 替代 IFR（IFR 在 Qwen 上 Jaccard=0.000，完全不兼容），\n  css_0.67 评估 bug 已修复但历史数据受影响，SVA 用 css_1.00 重新评估后 marginal PASS（Δ≈0.013）。\n\nimagined_experiments:\n\n- name: GPT-2 SVA K=3 CSS（css_1.00 重新评估）\n  plan_id: plan_004\n  description: >\n    Subject-Verb Agreement on GPT-2 Small, K=3 (EAP-IG + EP + ACDC top-k)。\n    已有两次运行（mvp_sva_gpt2_k3 top-100, mvp_sva_gpt2_k3_topk top-k=50/75/100）。\n    Median 档下用 css_1.00 重新评估条件④，结果为 marginal PASS——Δ(CPR) 在统计噪声范围内。\n  expected_results:\n    status: done\n    conclusion: marginal_pass\n    pairwise_jaccard:\n      eapig_x_ep: 0.6529\n      eapig_x_acdc: 0.3158\n      ep_x_acdc: 0.4184\n    max_jaccard: 0.6529\n    three_way_ratio: 0.2785\n    circuit_sizes:\n      eapig_k75: 75\n      ep_k75: 75\n      acdc_k75: 75\n      acdc_isinf: ~22\n    css_distribution:\n      \"0.33\": 60\n      \"0.67\": 54\n      \"1.00\": 44\n    faithfulness_mean:\n      css_1.00:\n        edges: 44\n        CPR: 1.1873\n        CMD: 0.5465\n      css_0.67:\n        edges: 98\n        CPR: 1.1724\n        CMD: 0.5031\n      eapig_k75:\n        edges: 75\n        CPR: 1.1703\n        CMD: ~0.53\n      ep_k75:\n        edges: 75\n        CPR: 1.1703\n        CMD: ~0.53\n      acdc_k75:\n        edges: 75\n        CPR: 1.1746\n        CMD: ~0.52\n    css_1.00_delta_cpr: 0.0127\n    d025_cond4_verdict: \"technically PASS (css_1.00 CPR=1.1873 > acdc=1.1746) but Δ=0.013 within noise\"\n    d033_verdict: \"inconclusive — single seed Δ=0.013 不具鲁棒性\"\n    isinf_degeneration:\n      css_1.00_isinf_edges: ~22\n      css_1.00_isinf_cpr: ~1.174\n      acdc_isinf_cpr: ~1.174\n      degeneration_confirmed: true\n    sva_gate_verdict: \"MARGINAL — condition④ technically PASS but no statistical confidence; D033 降级为 inconclusive\"\n  result_rationale: >\n    SVA 在 GPT-2 Small 上的 EAP-IG×EP Jaccard=0.6529 远高于 IOI 的 0.31——这是因为\n    SVA 的语法一致性计算主要依赖 layer 7-10 的 number-tracking attention heads，gradient\n    方法（EAP-IG）和 pruning 方法（EP）在这些 dominant heads 上高度一致。ACDC top-k 引入了\n    部分分歧（ACDC×EAP-IG=0.32, ACDC×EP=0.42），但 max pairwise Jaccard 仍由 EAP-IG×EP\n    主导。css_1.00 的 44 条 consensus 边 CPR=1.1873 略高于 ACDC 的 1.1746（Δ=0.0127），\n    方向正确但在单 seed 条件下无法排除随机波动。D033 明确判定此 Δ 不具鲁棒性——需要至少\n    3-5 个 seed 的 bootstrap CI 才能确认方向性，而当前只有 1 个 seed。\n    这正是 median 档的标志性结果：技术上 PASS 但缺乏统计说服力，放在论文里只能描述为\n    \"borderline case where CSS shows marginal improvement consistent with moderate Jaccard\"。\n    max_jaccard=0.6529 接近 Arithmetic 的 0.695，预示 CSS 在高相关方法对下的过滤效果有限。\n  tables:\n    - name: \"Table: SVA Faithfulness (mean ablation, top-k=75)\"\n      columns: [Circuit, Edges, CPR ↑, CMD ↓, Δ vs best single]\n      rows:\n        - [CSS=1.0 (k=75), 44, 1.187, 0.547, \"+0.013\"]\n        - [CSS≥0.67 (k=75), 98, 1.172, 0.503, \"−0.003\"]\n        - [EAP-IG (k=75), 75, 1.170, ~0.53, \"—\"]\n        - [EP (k=75), 75, 1.170, ~0.53, \"−0.000\"]\n        - [ACDC (k=75), 75, 1.175, ~0.52, \"+0.005\"]\n    - name: \"Table: SVA Pairwise Jaccard (top-k)\"\n      columns: [\"\", EAP-IG, EP, ACDC]\n      rows:\n        - [EAP-IG, \"—\", 0.653, 0.316]\n        - [EP, 0.653, \"—\", 0.418]\n        - [ACDC, 0.316, 0.418, \"—\"]\n  figures_description:\n    - >\n      Bar chart: SVA faithfulness comparison (CSS=1.0 vs single methods)。\n      CSS=1.0 bar 仅微微高于 ACDC bar（Δ=0.013 几乎不可见），与 IOI 的清晰差距形成鲜明对比。\n      旁注标注 \"Δ not statistically significant (single seed)\"。\n    - >\n      SVA CSS distribution histogram (0.33/0.67/1.00) vs IOI — SVA 分布更均匀（44/54/60），\n      IOI 更偏向 1/3（3of3 仅 7 edges vs SVA 的 44），反映 SVA top-k normalization\n      后方法 overlap 更大。\n  analysis: >\n    SVA 在 median 档下是一个 borderline data point。max_jaccard=0.653 → CSS utility\n    预测为低（接近 Arithmetic 的 0.695），实际 Δ=0.013 符合这个预期。\n    对 Claim 1 的贡献：不能 claim CSS faithfulness 优势，只能 claim \"comparable faithfulness\n    at 59% edges\" (44/75)——edge efficiency 论点弱于 IOI（IOI 是 7/100=7%）。\n    对 Claim 2 的贡献：提供了一个 mid-range Jaccard 数据点，方向一致但 CSS advantage 为\n    marginal positive，需要标注 uncertainty。\n    关键风险：reviewer 会问 \"if Δ=0.013 is within noise, how do you distinguish SVA\n    from a CSS-neutral case?\"——需要在论文中诚实承认这一点。\n\n- name: GPT-2 Factual Recall K=3 CSS\n  plan_id: plan_005\n  description: >\n    Distributed computation task on GPT-2 Small。预期高 Jaccard 或 ACDC 收敛困难。\n    GPT-2 Small 的 factual knowledge 有限，ACDC 可能无法产出 clean circuit。\n  expected_results:\n    status: abandoned\n    conclusion: data_not_clean\n    partial_metrics:\n      eapig_completed: true\n      ep_completed: true\n      acdc_completed: false\n      acdc_failure_reason: >\n        GPT-2 Small factual recall accuracy ~55-65% (vs random 25%)，baseline 不稳定。\n        ACDC patching-based search 在 clean performance 波动大时无法收敛——阈值过高电路为空，\n        过低保留近全图。isinf 仅得 3-5 条边，top-k 后 faithfulness 接近随机 (CPR ≈ 0)。\n    note: >\n      实验被终止。不纳入论文分析。在 Limitations 中说明 GPT-2 Small 对 factual recall\n      能力不足以支撑 circuit discovery。\n  result_rationale: >\n    GPT-2 Small (117M) 的 parametric knowledge 极为稀疏——factual recall (\"The capital\n    of France is\") 的准确率在 55-65% 之间波动，意味着模型本身对 clean input 的行为就不一致。\n    EAP-IG 和 EP 可以通过 top-k 强行选出 50-75 条边，但这些边的 faithfulness 接近 baseline\n    （CPR ≈ 0 即移除后模型行为无明显变化），说明 GPT-2 Small 没有形成 dedicated factual\n    retrieval circuit——信息分散在整个 residual stream 中，没有可 localize 的子结构。\n    ACDC 对这种 diffuse computation 最敏感：patching 单条边几乎不改变输出，所有边的\n    importance score 都在噪声水平，无法区分 signal 和 noise。\n    这不是 CSS 方法论的失败，而是 task-model 匹配问题。在 ARR 5/25 deadline 下，\n    合理决策是放弃第四任务，保留 3 个 GPT-2 tasks（IOI + Arithmetic + SVA）。\n  tables: []\n  figures_description: []\n  analysis: >\n    第四任务失败是 median 档的核心限制之一。论文保持 3 个 GPT-2 tasks +\n    Qwen cross-validation。Reviewer 会攻击 \"only 3 tasks on one small model\"——\n    应对：强调 3 个任务覆盖 localized (IOI)、distributed (Arithmetic)、\n    intermediate (SVA) 三种电路结构，加上 Qwen 提供跨模型验证。\n\n- name: Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + ACDC top-k)\n  plan_id: plan_006\n  description: >\n    D029 后用 ACDC top-k 替代 IFR 作为第三方法（IFR 在 Qwen 上 Jaccard=0.000，\n    完全不兼容——IFR 聚焦 early layers m2→a3，EAP-IG/EP 聚焦 deep layers a20.h9，\n    零重叠导致 CSS=1.0 为空集）。ACDC top-k 在 Qwen 上技术可行但需要调参。\n    验证 CSS 跨模型架构（GQA, SwiGLU）的泛化性。\n  expected_results:\n    status: done\n    conclusion: mixed\n    total_edges: 179388\n    binarization: top-k (k=75)\n    pairwise_jaccard:\n      eapig_x_ep: 0.38\n      eapig_x_acdc: 0.22\n      ep_x_acdc: 0.19\n    max_jaccard: 0.38\n    three_way_ratio: 0.09\n    circuit_sizes:\n      eapig_k75: 75\n      ep_k75: 75\n      acdc_k75: 75\n    css_distribution:\n      \"1/3\": 148\n      \"2/3\": 58\n      \"3/3\": 19\n    faithfulness_mean:\n      css_1.00:\n        edges: 19\n        CPR: 0.095\n        CMD: 0.932\n      css_0.67:\n        edges: 58\n        CPR: 0.078\n        CMD: 0.951\n      eapig_k75:\n        edges: 75\n        CPR: 0.082\n        CMD: 0.946\n      ep_k75:\n        edges: 75\n        CPR: 0.071\n        CMD: 0.958\n      acdc_k75:\n        edges: 75\n        CPR: 0.068\n        CMD: 0.962\n    css1_cpr: 0.095\n    css1_vs_best_single: 0.013\n    qwen_acdc_technical_notes: >\n      ACDC 在 179k-edge Qwen graph 上运行时间显著增加（~45min vs GPT-2 的 ~5min）。\n      isinf 产出极少边（< 10），top-k=75 normalization 后产出合理但 faithfulness\n      指标波动较大（不同 random seed 间 CPR 变化 ±0.02）。\n      TransformerLens 不支持 Qwen2.5，全部用 HF-native 实现，与 GPT-2 pipeline\n      不完全对齐——这是潜在的 confound。\n  result_rationale: >\n    Qwen-2.5 0.5B 上 ACDC top-k 替代 IFR 后，三种方法都来自不同算法族但全部\n    基于 performance/loss 信号（gradient、pruning、greedy causal），这意味着\n    方法间的分歧主要来源于搜索策略差异而非 measurement paradigm 差异。\n    EAP-IG×EP Jaccard=0.38 低于 SVA 的 0.653 但高于 IOI GPT-2 的 0.31——\n    Qwen 的 GQA 结构使得 head 内 key-value sharing 改变了 gradient 和 pruning\n    的敏感度分布，但 IOI 的 name mover / S-inhibition 机制在 Qwen 上仍然相对\n    localized，给方法分歧留出空间。ACDC×EAP-IG 和 ACDC×EP 的 Jaccard 较低\n    （0.22/0.19）因为 ACDC 的 greedy search 在大 graph 上的搜索路径与 gradient\n    方法显著不同。\n    CSS=1.0 的 19 条边 CPR=0.095 略优于 EAP-IG 的 0.082（Δ=0.013），方向正确\n    但与 SVA 类似处于 marginal 区间。这是 median 档的特征：CSS 在 low-to-moderate\n    Jaccard 条件下 consistently shows small positive advantage，但没有一个\n    结果足够强到单独 claim significance。\n    核心限制：HF-native pipeline 与 GPT-2 的 TransformerLens pipeline 不完全\n    对齐，跨模型 CPR 比较需要 caveat。\n  tables:\n    - name: \"Table: Qwen-0.5B IOI Faithfulness (mean ablation, k=75)\"\n      columns: [Circuit, Edges, CPR ↑, CMD ↓]\n      rows:\n        - [CSS=1.0, 19, 0.095, 0.932]\n        - [CSS≥0.67, 58, 0.078, 0.951]\n        - [EAP-IG, 75, 0.082, 0.946]\n        - [EP, 75, 0.071, 0.958]\n        - [ACDC, 75, 0.068, 0.962]\n    - name: \"Table: Qwen-0.5B IOI Pairwise Jaccard (top-k=75)\"\n      columns: [\"\", EAP-IG, EP, ACDC]\n      rows:\n        - [EAP-IG, \"—\", 0.38, 0.22]\n        - [EP, 0.38, \"—\", 0.19]\n        - [ACDC, 0.22, 0.19, \"—\"]\n  figures_description:\n    - >\n      Cross-model IOI comparison (GPT-2 vs Qwen): paired bar chart 显示两个模型的\n      CSS=1.0 vs best-single CPR。GPT-2 gap 更大（0.109 vs 0.029, Δ=0.08），\n      Qwen gap 较小（0.095 vs 0.082, Δ=0.013）。Qwen 的 smaller gap 反映了\n      ACDC top-k 与 gradient 方法的 Jaccard 比 GPT-2 ACDC isinf 的更高。\n    - >\n      Jaccard heatmap: 3×3 matrix for Qwen IOI, 与 GPT-2 IOI 并列。\n      Qwen 的整体 Jaccard 更均匀（0.19-0.38），GPT-2 更极端（0.086-0.307）。\n  analysis: >\n    Qwen IOI 是 median 档中最有价值的新增数据点。max_jaccard=0.38 + CSS Δ=+0.013\n    落在 Jaccard-utility 趋势线的预期位置（IOI GPT-2: 0.31/+0.08, SVA: 0.653/+0.013,\n    Arithmetic: 0.695/−0.066 之间）。\n    关键意义：(1) 证明 CSS 跨模型可行（Qwen ≠ GPT-2 架构），(2) ACDC top-k\n    在大模型上作为第三方法的可行性验证，(3) 为 Jaccard-utility 分析提供第 4 个数据点。\n    但 Δ=+0.013 的 marginal nature 意味着 Qwen IOI 不能单独支撑 Claim 1——\n    它只是趋势中的一个 intermediate point。\n\n- name: Qwen-2.5 0.5B Arithmetic K=3 (EAP-IG + EP + ACDC top-k)\n  plan_id: plan_007\n  description: >\n    Qwen 上 Arithmetic/Greaterthan，ACDC top-k 作为第三方法。\n    预期 Jaccard 较高（distributed computation → method convergence），CSS 应失败。\n    验证 Arithmetic 的 CSS-negative 模式跨模型复现。\n  expected_results:\n    status: done\n    conclusion: negative\n    pairwise_jaccard:\n      eapig_x_ep: 0.52\n      eapig_x_acdc: 0.31\n      ep_x_acdc: 0.28\n    max_jaccard: 0.52\n    three_way_ratio: 0.17\n    css_distribution:\n      \"1/3\": 112\n      \"2/3\": 71\n      \"3/3\": 42\n    faithfulness_mean:\n      css_1.00:\n        edges: 42\n        CPR: 0.921\n        CMD: 0.345\n      eapig_k75:\n        edges: 75\n        CPR: 0.968\n        CMD: 0.142\n      ep_k75:\n        edges: 75\n        CPR: 0.951\n        CMD: 0.218\n      acdc_k75:\n        edges: 75\n        CPR: 0.938\n        CMD: 0.274\n    css1_cpr_advantage: -0.047\n    css1_vs_eapig_delta: -0.047\n    note: >\n      CSS=1.0 CPR=0.921 < EAP-IG=0.968。Qwen Arithmetic 确认 CSS-negative。\n      但 max_jaccard=0.52 比 GPT-2 的 0.695 显著降低（Qwen 的 GQA + 更大容量\n      使 comparison computation 更分散），CSS advantage 也从 −0.066 改善到 −0.047。\n  result_rationale: >\n    Arithmetic/Greaterthan 的数值比较计算在 Qwen 上比 GPT-2 更分散——0.5B 参数\n    提供了更多 redundant heads 可以承担 comparison 功能，降低了方法间在 top-k\n    边集上的重合度。EAP-IG×EP Jaccard 从 GPT-2 的 0.695 降至 Qwen 的 0.52，\n    反映了这种分散效应。ACDC 在 Qwen Arithmetic 上的行为也更 diverse（ACDC×EAP-IG=0.31），\n    因为 greedy search 在更大 graph 中有更多备选路径。\n    然而 max_jaccard=0.52 仍然意味着 EAP-IG 和 EP 在超过一半的 top-75 边上达成共识——\n    这些共识边覆盖了 Arithmetic 的核心 comparison pathway，任何 performance-based\n    方法都难以忽略它们。CSS=1.0 的 42 条边要求三方法全部同意，这过滤掉了 ACDC 独特发现的\n    一些 low-importance edges，但也丢失了 EAP-IG×EP 共识中 ACDC 未选中的 important edges。\n    净效果是 CSS=1.0 CPR=0.921 低于 EAP-IG 单方法的 0.968。\n    关键观察：max_jaccard=0.52 落在 Jaccard-utility threshold 的 borderline 区域\n    （定义为 ~0.45-0.55）。如果 threshold 在 0.50 以下，这个点确认 \"above threshold\n    → CSS fails\"；如果 threshold 在 0.55 以上，这个点是一个 near-miss。这种 ambiguity\n    是 median 档的核心特征——趋势清晰但 boundary 模糊。\n  tables:\n    - name: \"Table: Qwen-0.5B Arithmetic Faithfulness (mean ablation, k=75)\"\n      columns: [Circuit, Edges, CPR ↑, CMD ↓]\n      rows:\n        - [CSS=1.0, 42, 0.921, 0.345]\n        - [EAP-IG (k=75), 75, 0.968, 0.142]\n        - [EP (k=75), 75, 0.951, 0.218]\n        - [ACDC (k=75), 75, 0.938, 0.274]\n    - name: \"Table: Arithmetic Cross-Model Comparison\"\n      columns: [Model, Max Jaccard, CSS=1.0 CPR, Best Single CPR, Δ]\n      rows:\n        - [GPT-2, 0.695, 0.919, 0.985, \"−0.066\"]\n        - [Qwen-0.5B, 0.52, 0.921, 0.968, \"−0.047\"]\n  figures_description:\n    - >\n      在 Jaccard-utility scatter plot 中，Qwen Arithmetic 的数据点 (0.52, −0.047)\n      落在 GPT-2 Arithmetic (0.695, −0.066) 的左上方（更低 Jaccard，更小 negative\n      advantage），方向一致、趋势线延伸自然。\n  analysis: >\n    Qwen Arithmetic 的 negative result 在 reframed narrative 下是资产：\n    (1) 确认 high-Jaccard → CSS fails 的模式跨模型稳定，\n    (2) max_jaccard 从 0.695 降至 0.52 伴随 CSS disadvantage 从 0.066 缩小至 0.047，\n        精确地落在 Jaccard-utility 趋势线上，\n    (3) 提供了第 4 个（或第 3 个，取决于 SVA 是否计入）有效数据点。\n    但 max_jaccard=0.52 接近 putative threshold（~0.5），使 threshold 估计更不确定——\n    如果这个点被归为 \"near-threshold ambiguous\"，有效的 clear positive 和 clear negative\n    数据点各减少一个。\n\n- name: Gemma-2 2B IOI K=3\n  plan_id: plan_008\n  description: >\n    Scale to 2B model (Gemma-2). P2 优先级。需要 ~16 GPU-hours 和经过验证的\n    ACDC top-k pipeline for larger models。\n  expected_results:\n    status: not_attempted\n    conclusion: null\n    reason: >\n      时间和 GPU 资源不足。plan_004 (SVA 重新评估) + plan_006 (Qwen IOI ACDC) +\n      plan_007 (Qwen Arith) 已消耗大部分 12 天 budget。Gemma-2 2B 需要额外的\n      EP 内存优化（2B model edge-level pruning 在 RTX 4090D 24GB 上 borderline），\n      且 ACDC 在 2B graph 上可能需要 gradient checkpointing。在 ARR 5/25 前\n      无法完成实验 + 分析 + 论文写作。\n  result_rationale: >\n    Median 档的时间约束下，优先完成 Qwen 两个任务（验证跨模型 + ACDC top-k pipeline）\n    已消耗大部分 Phase 2 budget。Gemma-2 实验依赖 plan_006 的 pipeline 验证结果，\n    且需要额外的工程工作（EP 内存、ACDC 长运行时间、模型下载 ~5GB）。\n    即使勉强跑完 Gemma-2 IOI，结果只增加一个数据点——在 deadline 压力下，\n    投入产出比不如把时间用在论文写作和现有数据的 robust 分析上。\n  tables: []\n  figures_description: []\n  analysis: >\n    Not attempted。在 Limitations 中列为 model scale generalization future work。\n    论文 claim \"GPT-2 (117M) + Qwen (500M)\" 两个 scale，reviewer 会追问更大模型，\n    但可以 argue 核心 finding (Jaccard predicts CSS utility) 是 method-level\n    property 不 fundamentally depend on model scale。\n\n- name: Llama-3.1 8B IOI K=3\n  plan_id: plan_009\n  description: >\n    Scale to 8B model. P3 优先级。需要 A100 80GB（RTX 4090D 24GB 不够 EP）。\n  expected_results:\n    status: not_attempted\n    conclusion: null\n    reason: >\n      P3 优先级 + 硬件不足（需要 A100 80GB）+ plan_008 未完成作为前置。\n      远超 deadline 范围。\n  result_rationale: >\n    8B 模型需要 A100 80GB 级 GPU 来运行 EP（edge-level pruning 的内存需求\n    随 model size 超线性增长），当前 RTX 4090D 24GB 完全不够。即使有硬件，\n    单次 ACDC 运行可能需要数小时，3 方法 × 调参 → 不现实。\n  tables: []\n  figures_description: []\n  analysis: >\n    Not attempted。Future work stretch goal。有 Qwen 0.5B 已经够 claim\n    \"beyond GPT-2 Small\"。\n\n- name: Top-k Binarization Sensitivity Sweep\n  plan_id: plan_010\n  description: >\n    在已完成的 model×task pairs 上系统扫描 k=50/75/100/150。\n    验证 CSS=1.0 CPR 在不同 k 下的稳定性，回应 R5。\n  expected_results:\n    status: done\n    conclusion: partially_stable\n    ioi_gpt2:\n      k50: {css_1.0_edges: 7, css_1.0_cpr: 0.109}\n      k75: {css_1.0_edges: 12, css_1.0_cpr: 0.105}\n      k100: {css_1.0_edges: 18, css_1.0_cpr: 0.098}\n      k150: {css_1.0_edges: 24, css_1.0_cpr: 0.093}\n      verdict: \"stable (CPR range 0.093-0.109, Δ=0.016)\"\n    arithmetic_gpt2:\n      k50: {css_1.0_edges: 44, css_1.0_cpr: 0.919}\n      k75: {css_1.0_edges: 54, css_1.0_cpr: 0.919}\n      k100: {css_1.0_edges: 62, css_1.0_cpr: 0.926}\n      k150: {css_1.0_edges: 71, css_1.0_cpr: 0.933}\n      verdict: \"stable (CPR range 0.919-0.933, Δ=0.014)\"\n    sva_gpt2:\n      k50: {css_1.0_edges: 15, css_1.0_cpr: 0.891}\n      k75: {css_1.0_edges: 23, css_1.0_cpr: 0.941}\n      k100: {css_1.0_edges: 29, css_1.0_cpr: 0.944}\n      k150: {css_1.0_edges: 38, css_1.0_cpr: 0.940}\n      verdict: \"sensitive at k=50 (CPR drop 0.05), stable k=75-150\"\n    qwen_ioi:\n      k50: {css_1.0_edges: 11, css_1.0_cpr: 0.074}\n      k75: {css_1.0_edges: 19, css_1.0_cpr: 0.095}\n      k100: {css_1.0_edges: 26, css_1.0_cpr: 0.091}\n      k150: {css_1.0_edges: 35, css_1.0_cpr: 0.088}\n      verdict: \"sensitive at k=50 (CPR drop 0.021), stable k=75-150\"\n    overall_verdict: >\n      CSS=1.0 CPR 在 k=75-150 范围内基本稳定（max Δ < 0.016 for IOI/Arith,\n      < 0.004 for SVA k≥75）。k=50 在 SVA 和 Qwen IOI 上 CPR 下降 0.02-0.05，\n      因为 k=50 过小导致方法重叠不足、CSS=1.0 边数太少。\n      推荐 k=75 作为默认值。但 SVA k=50 的 sensitivity 是可被攻击的 degree of freedom。\n  result_rationale: >\n    Top-k normalization 将 ACDC 的 arbitrary isinf binarization 替换为固定 edge budget，\n    使三种方法在 comparable scale 下比较。k 越大，每个方法保留更多边，pairwise overlap\n    概率增加，CSS=1.0 集合扩大——新增的 consensus 边包含更多低置信度的偶然共识，CPR 微降。\n    k=75-150 范围内这个效应很温和（IOI CPR 变化 0.016），因为核心 consensus edges\n    在这个 k 范围内始终被选中。\n    k=50 的 sensitivity 来源不同：SVA 和 Qwen IOI 的电路较 concentrated，k=50 时\n    可能恰好切掉了某方法 borderline 但 functionally important 的边，导致 CSS=1.0\n    丢失关键 consensus 成员。这不是 CSS 方法论的缺陷，而是 k 需要大于某个 minimum\n    （约 60-70）才能让方法有足够的 overlap base。\n    IOI GPT-2 的 k=50 不受影响是因为 GPT-2 IOI 的 ACDC isinf 只有 14 条边，\n    top-k=50 已远超 isinf 集合，CSS=1.0 的 7 条核心边全在 k=50 range 内。\n  tables:\n    - name: \"Table: CSS=1.0 CPR across k values\"\n      columns: [Task/Model, k=50, k=75, k=100, k=150, Max Δ, Verdict]\n      rows:\n        - [IOI/GPT-2, 0.109, 0.105, 0.098, 0.093, 0.016, stable]\n        - [Arith/GPT-2, 0.919, 0.919, 0.926, 0.933, 0.014, stable]\n        - [SVA/GPT-2, 0.891, 0.941, 0.944, 0.940, 0.053, \"k=50 sensitive\"]\n        - [IOI/Qwen, 0.074, 0.095, 0.091, 0.088, 0.021, \"k=50 sensitive\"]\n  figures_description:\n    - >\n      Line plot: x=k, y=CSS=1.0 CPR, four lines (one per task×model).\n      灰色 band 标记 k=75-150 稳定区间。k=50 处 SVA 和 Qwen IOI 有明显 dip。\n  analysis: >\n    Binarization ablation 支撑 Claim 3（top-k 修复 isinf 退化）且 k=75-150 稳定。\n    SVA/Qwen k=50 的 sensitivity 是 reviewer 攻击点但可防守：k=50 对 32k+ edge\n    graph 仅保留 0.15% edges，低于合理下界。推荐 k=75 作为 default 并在 appendix\n    放完整 sweep 数据。\n\n- name: Ablation Method Comparison (Zero vs Mean)\n  plan_id: plan_011\n  description: >\n    在 IOI 上比较 zero 和 mean ablation 下的 CSS 优势。P2 优先级。\n    Resample ablation 和 SVA/Arithmetic 的 ablation 对比因时间不足未完成。\n  expected_results:\n    status: partial\n    conclusion: directionally_consistent\n    completed_tasks: [IOI (GPT-2)]\n    ioi_gpt2:\n      zero_ablation:\n        css_1.0_cpr: 0.109\n        best_single_cpr: 0.029\n        css_advantage: 0.080\n      mean_ablation:\n        css_1.0_cpr: 0.118\n        best_single_cpr: 0.095\n        css_advantage: 0.023\n    note: >\n      仅完成 IOI 一个 task 的 zero vs mean 对比。CSS advantage 方向一致（正），\n      但绝对值差异大——zero ablation 下 Δ=0.080，mean ablation 下 Δ=0.023。\n      Resample ablation 未完成。SVA 和 Arithmetic 未完成。\n  result_rationale: >\n    Zero ablation 将电路外所有边的 activation 清零，这对电路外的破坏最大，使得\n    \"真正重要的电路\" 和 \"不重要的电路\" 之间的 CPR 差距放大。CSS=1.0 作为最精简的\n    consensus 子集，在 zero ablation 下受益最大（保留的 7 条边全是 critical path，\n    丢失少量非 critical 边的惩罚小）。\n    Mean ablation 更温和——baseline 是均值而非零，电路外的 \"noise\" 被部分保留，\n    所有方法的 CPR 都偏高，CSS=1.0 与 single method 的差距被压缩。\n    关键 insight：CSS advantage 在两种 ablation 下都为正，说明 consensus 的\n    信号不是 evaluation artifact。但 Δ=0.023 (mean) vs Δ=0.080 (zero) 意味着\n    论文主实验使用的 evaluation method 会显著影响 reported advantage 的量级——\n    reviewer 会追问这一点。\n    仅有 IOI 一个 task 的数据不足以 claim robustness across tasks。\n  tables:\n    - name: \"Table: IOI CSS advantage under different ablation methods\"\n      columns: [Ablation, CSS=1.0 CPR, Best Single CPR, Δ]\n      rows:\n        - [Zero, 0.109, 0.029, \"+0.080\"]\n        - [Mean, 0.118, 0.095, \"+0.023\"]\n  figures_description: []\n  analysis: >\n    部分完成。IOI 上 CSS advantage 在 zero 和 mean 下方向一致。\n    可在 Appendix 放 IOI 的 ablation robustness table。\n    Reviewer 追问时可 footnote \"CSS advantage directionally stable across\n    evaluation methods; magnitude varies with ablation aggressiveness, as expected.\"\n    Full multi-task ablation 列为 future work。\n\n- name: CIRCUS vs CSS Negative Ablation\n  plan_id: plan_012\n  description: >\n    使用 D021 中 CIRCUS 的已有失败结果作为 negative ablation。\n    0 GPU hours，仅需分析和写作。直接对比 CIRCUS core vs CSS=1.0 on IOI。\n  expected_results:\n    status: done\n    conclusion: negative_ablation_confirmed\n    circus_vs_css:\n      ioi:\n        circus_core_edges: 15\n        circus_core_cpr: -0.108\n        css_1.0_edges: 7\n        css_1.0_cpr: 0.109\n    circus_failure_modes:\n      - \"CIRCUS 基于 single-method (EAP-IG) faithfulness scoring 选 core edges\"\n      - \"scoring 依赖 ablation method 和 threshold，三次运行结果不一致 (edges: 12, 15, 18)\"\n      - \"CSS binary consensus 不需要 score calibration，避免了 CIRCUS 的核心缺陷\"\n    note: >\n      仅在 IOI 上有 CIRCUS 数据。SVA 和 Arithmetic 上未跑 CIRCUS（无额外 GPU 预算）。\n      单 task negative ablation 说服力有限但结果清晰。\n  result_rationale: >\n    CIRCUS (Parekh 2026) 在 IOI 上的 D021 结果：core edges CPR=−0.108（负值），\n    说明 CIRCUS 的 \"most stable\" edges 实际上破坏了模型行为。这是因为 CIRCUS\n    在 EAP-IG 内部做 threshold sweep 选 core——EAP-IG 的系统性偏差（过度依赖\n    early-layer attention gradient）被 CIRCUS 放大而非纠正。\n    CSS=1.0 通过 cross-method agreement 过滤了单方法偏差：即使 EAP-IG 对某些\n    early-layer edges 评分过高，如果 EP 和 ACDC 不同意，这些边被排除。\n    CIRCUS CPR=−0.108 vs CSS CPR=+0.109 的反差是论文中最 \"clean\" 的结果之一。\n    但仅有 IOI 一个 task 的数据意味着 reviewer 可以质疑 CIRCUS 在其他 task/setting\n    下是否同样差——Parekh 的原始结果可能在更大模型或不同任务上表现不同。\n    论文应 hedge：\"on the tasks we evaluated, structural consensus outperforms\n    within-method stability selection.\"\n  tables:\n    - name: \"Table: CSS vs CIRCUS on IOI\"\n      columns: [Method, Edges, CPR ↑, CMD ↓, Reproducible?]\n      rows:\n        - [CSS=1.0, 7, 0.109, 0.911, \"Yes (deterministic)\"]\n        - [CIRCUS core, 15, −0.108, 1.134, \"No (12-18 edges across runs)\"]\n  figures_description:\n    - >\n      Two-bar comparison: CSS=1.0 (blue, positive) vs CIRCUS (grey, negative) on IOI.\n      简洁有力的 visual contrast。\n  analysis: >\n    CIRCUS negative ablation 是 Claim 3 (binarization pathology → top-k fix)\n    和 Claim 4 (CSS taxonomy) 的有力 supporting evidence。结果清晰、对比公平、\n    计算成本为零。但仅 IOI 一个 task 限制了 generalizability claim。\n    在 Related Work 中用一段 + 一个 table 展示。\n\n- name: Jaccard-CSS Utility Correlation Analysis\n  plan_id: plan_013\n  description: >\n    汇总所有 model×task 组合的 (max pairwise Jaccard, CSS CPR advantage)，\n    计算 Spearman 相关系数。这是 reframed Claim 2 的核心证据。\n    Median 档下有 3-4 个有效数据点（取决于 SVA 是否计入为 \"marginal positive\"）。\n  expected_results:\n    status: done\n    conclusion: trend_visible_not_significant\n    data_points:\n      - task: IOI (GPT-2)\n        max_jaccard: 0.31\n        css_advantage: 0.080\n        css_wins: true\n        quality: clear_positive\n      - task: SVA (GPT-2)\n        max_jaccard: 0.653\n        css_advantage: 0.013\n        css_wins: marginal\n        quality: borderline\n      - task: Arithmetic (GPT-2)\n        max_jaccard: 0.695\n        css_advantage: -0.066\n        css_wins: false\n        quality: clear_negative\n      - task: IOI (Qwen)\n        max_jaccard: 0.38\n        css_advantage: 0.013\n        css_wins: marginal\n        quality: borderline\n    spearman_rho: -0.80\n    spearman_p: 0.20\n    n_data_points: 4\n    threshold_estimate: \"~0.50 (visual estimate, large uncertainty)\"\n    low_jaccard_css_pass_fraction: 0.50\n    note: >\n      4 个数据点：1 个 clear positive (IOI GPT-2)，2 个 marginal (SVA, Qwen IOI)，\n      1 个 clear negative (Arithmetic GPT-2)。\n      如果加入 Qwen Arithmetic (max_jaccard=0.52, css_advantage=−0.047)\n      作为第 5 个点，Spearman rho 改善至 −0.90, p=0.037——但这依赖于\n      Qwen Arithmetic 实验是否在 deadline 前完成。\n      趋势方向正确（higher Jaccard → lower CSS utility）但 p > 0.1 at n=4。\n  result_rationale: >\n    4 个 model×task 数据点的 Spearman rho=−0.80 方向清晰但统计力不足（p=0.20，\n    因为 n=4 下 even perfect rank correlation 的 p 也只有 0.042）。\n    趋势的 mechanistic 解释仍然成立：低 Jaccard 意味着方法独立发现不同 edge sets，\n    交集代表 multi-perspective validated core → higher faithfulness。\n    高 Jaccard 意味着方法收敛，consensus 退化为最 selective 的单方法。\n    但 4 个数据点中有 2 个 \"extremes\"（IOI clearly positive, Arithmetic clearly\n    negative）和 2 个 \"borderlines\"（SVA Δ=+0.013, Qwen IOI Δ=+0.013），\n    趋势的 robustness 高度依赖 borderline points 的归类。\n    如果把 SVA 和 Qwen IOI 都视为 \"CSS neutral\"（Δ < 0.02 ≈ noise），\n    那么只有 IOI GPT-2 是 CSS positive，success rate = 1/3 for GPT-2 tasks。\n    这就是 median 档的核心 tension：趋势可见，但无法区分 \"weak but real pattern\"\n    和 \"IOI 是唯一 positive case + noise\"。\n\n    加入 Qwen Arithmetic（如果完成）将 n 提升到 5，rho 改善到 −0.90 (p=0.037)，\n    勉强过 significance threshold。这使得 Qwen Arithmetic 成为 median 档中\n    最关键的 \"swing experiment\"。\n\n    threshold estimate ~0.50 基于 4 个点的 visual interpolation，置信区间极宽\n    （可能 [0.35, 0.65]），不具 predictive power。论文中应报告为 \"preliminary\n    estimate\" 而非 actionable guideline。\n  tables:\n    - name: \"Table: Jaccard vs CSS Advantage (all experiments)\"\n      columns: [Task, Model, Methods, Max Jaccard, CSS=1.0 CPR, Best Single CPR, Δ, Verdict]\n      rows:\n        - [IOI, GPT-2, \"EAP-IG/EP/ACDC\", 0.31, 0.109, 0.029, \"+0.080\", \"✓ PASS\"]\n        - [SVA, GPT-2, \"EAP-IG/EP/ACDC\", 0.653, 1.187, 1.175, \"+0.013\", \"~ marginal\"]\n        - [IOI, Qwen-0.5B, \"EAP-IG/EP/ACDC\", 0.38, 0.095, 0.082, \"+0.013\", \"~ marginal\"]\n        - [Arithmetic, GPT-2, \"EAP-IG/EP/ACDC\", 0.695, 0.919, 0.985, \"−0.066\", \"✗ FAIL\"]\n    - name: \"Table: Jaccard-Utility Correlation Statistics\"\n      columns: [Metric, Value]\n      rows:\n        - [N data points, 4]\n        - [Spearman ρ, −0.80]\n        - [Spearman p, 0.20]\n        - [\"Threshold estimate\", \"~0.50 (±0.15)\"]\n        - [\"Low-Jaccard (<0.50) CSS PASS fraction\", \"1/2 clear + 1/2 marginal\"]\n  figures_description:\n    - >\n      KEY FIGURE: Scatter plot — x: max pairwise Jaccard, y: CSS CPR advantage。\n      4 个点，颜色区分模型（GPT-2 蓝色, Qwen 橙色），形状区分任务。\n      灰色虚线 y=0。拟合线斜率为负但 95% CI band 很宽（几乎覆盖全图）。\n      右上角标注 ρ=−0.80, p=0.20, n=4。\n      与 best tier 的 6-point tight fit (ρ=0.94, p=0.005) 形成鲜明对比——\n      这里的 pattern 是 \"suggestive\" 而非 \"conclusive\"。\n    - >\n      Heatmap: rows=tasks, cols=method pairs, cells=Jaccard values。\n      Annotated with CSS outcome per task。帮助 reader 直观理解\n      \"which method pair drives max_jaccard\"。\n  analysis: >\n    Jaccard-utility 分析是 reframed narrative 的 crown jewel，但在 median 档下\n    它更像一个 \"hypothesis-generating observation\" 而非 \"validated finding\"。\n    4 个数据点 + p=0.20 意味着论文必须非常谨慎地措辞：\n    \"We observe a negative trend between max pairwise Jaccard and CSS faithfulness\n    advantage (ρ=−0.80, n=4), consistent with the hypothesis that CSS utility\n    depends on method diversity. While the trend does not reach statistical\n    significance at conventional thresholds (p=0.20), the direction is mechanistically\n    motivated and consistent across both models tested.\"\n\n    如果 Qwen Arithmetic（plan_007）在 deadline 前完成并纳入，n=5 + ρ≈−0.90 + p≈0.037\n    将显著改善说服力。这使 plan_007 成为 median 档中最 high-leverage 的实验——\n    应优先保证它的完成。\n\n    Low-Jaccard (<0.50) CSS PASS fraction = 1 clear + 1 marginal out of 2 cases = 50%-100%\n    取决于 \"marginal\" 是否算 PASS。这个 pass rate 远低于 best tier 的 100%，\n    但 reframed claim 不需要 CSS always wins——只需要 \"Jaccard predicts when CSS wins\"。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d8d91eb-e26c-46f5-aff8-67a9bac611fb",
  "isSidechain": false,
  "requestId": "req_011CazFrcuE6AC584kuvuMA7",
  "type": "assistant",
  "uuid": "70026870-1453-4c76-a242-1415b4692a0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPcQmLKUFVtbyh8EqdcwKw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14866,
      "cache_read_input_tokens": 43568,
      "output_tokens": 14989,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14989,
          "cache_read_input_tokens": 43568,
          "cache_creation_input_tokens": 14866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14866
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

_source line 36 · 2026-05-13T08:37:01.151Z_

<details><summary>↩ Tool result · `toolu_01GHGiMQYcyVkc1WqwLk8nox`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/median/imagined_experiments.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70026870-1453-4c76-a242-1415b4692a0f",
  "isSidechain": false,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "type": "user",
  "uuid": "da60ce81-7513-4615-813a-5cda062d4c04",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/median/imagined_experiments.yaml",
    "content": "tier: median\nnarrative_guidance: >\n  需要 reframe。降级 Claim 1 为 conditional result，升级 Claim 2 和 Claim 3 为主线。\n  叙事变为：\"CSS 的有效性取决于方法多样性，我们提供诊断框架（Jaccard 作为先验预测指标）帮助从业者判断何时值得做 consensus。\"\n  Arithmetic 高 Jaccard → CSS 失败成为核心 supporting evidence 而非 negative result。\n  SVA 描述为 \"borderline case consistent with moderate Jaccard\" 而非 strong positive。\n  论文从 \"CSS always works\" 变为 \"CSS works iff methods are diverse, and we can predict when\"。\n  仍可投 EMNLP，但需要诚实的 limitation section 承认数据点有限。\n  关键更新：D029 用 ACDC top-k 替代 IFR（IFR 在 Qwen 上 Jaccard=0.000，完全不兼容），\n  css_0.67 评估 bug 已修复但历史数据受影响，SVA 用 css_1.00 重新评估后 marginal PASS（Δ≈0.013）。\n\nimagined_experiments:\n\n- name: GPT-2 SVA K=3 CSS（css_1.00 重新评估）\n  plan_id: plan_004\n  description: >\n    Subject-Verb Agreement on GPT-2 Small, K=3 (EAP-IG + EP + ACDC top-k)。\n    已有两次运行（mvp_sva_gpt2_k3 top-100, mvp_sva_gpt2_k3_topk top-k=50/75/100）。\n    Median 档下用 css_1.00 重新评估条件④，结果为 marginal PASS——Δ(CPR) 在统计噪声范围内。\n  expected_results:\n    status: done\n    conclusion: marginal_pass\n    pairwise_jaccard:\n      eapig_x_ep: 0.6529\n      eapig_x_acdc: 0.3158\n      ep_x_acdc: 0.4184\n    max_jaccard: 0.6529\n    three_way_ratio: 0.2785\n    circuit_sizes:\n      eapig_k75: 75\n      ep_k75: 75\n      acdc_k75: 75\n      acdc_isinf: ~22\n    css_distribution:\n      \"0.33\": 60\n      \"0.67\": 54\n      \"1.00\": 44\n    faithfulness_mean:\n      css_1.00:\n        edges: 44\n        CPR: 1.1873\n        CMD: 0.5465\n      css_0.67:\n        edges: 98\n        CPR: 1.1724\n        CMD: 0.5031\n      eapig_k75:\n        edges: 75\n        CPR: 1.1703\n        CMD: ~0.53\n      ep_k75:\n        edges: 75\n        CPR: 1.1703\n        CMD: ~0.53\n      acdc_k75:\n        edges: 75\n        CPR: 1.1746\n        CMD: ~0.52\n    css_1.00_delta_cpr: 0.0127\n    d025_cond4_verdict: \"technically PASS (css_1.00 CPR=1.1873 > acdc=1.1746) but Δ=0.013 within noise\"\n    d033_verdict: \"inconclusive — single seed Δ=0.013 不具鲁棒性\"\n    isinf_degeneration:\n      css_1.00_isinf_edges: ~22\n      css_1.00_isinf_cpr: ~1.174\n      acdc_isinf_cpr: ~1.174\n      degeneration_confirmed: true\n    sva_gate_verdict: \"MARGINAL — condition④ technically PASS but no statistical confidence; D033 降级为 inconclusive\"\n  result_rationale: >\n    SVA 在 GPT-2 Small 上的 EAP-IG×EP Jaccard=0.6529 远高于 IOI 的 0.31——这是因为\n    SVA 的语法一致性计算主要依赖 layer 7-10 的 number-tracking attention heads，gradient\n    方法（EAP-IG）和 pruning 方法（EP）在这些 dominant heads 上高度一致。ACDC top-k 引入了\n    部分分歧（ACDC×EAP-IG=0.32, ACDC×EP=0.42），但 max pairwise Jaccard 仍由 EAP-IG×EP\n    主导。css_1.00 的 44 条 consensus 边 CPR=1.1873 略高于 ACDC 的 1.1746（Δ=0.0127），\n    方向正确但在单 seed 条件下无法排除随机波动。D033 明确判定此 Δ 不具鲁棒性——需要至少\n    3-5 个 seed 的 bootstrap CI 才能确认方向性，而当前只有 1 个 seed。\n    这正是 median 档的标志性结果：技术上 PASS 但缺乏统计说服力，放在论文里只能描述为\n    \"borderline case where CSS shows marginal improvement consistent with moderate Jaccard\"。\n    max_jaccard=0.6529 接近 Arithmetic 的 0.695，预示 CSS 在高相关方法对下的过滤效果有限。\n  tables:\n    - name: \"Table: SVA Faithfulness (mean ablation, top-k=75)\"\n      columns: [Circuit, Edges, CPR ↑, CMD ↓, Δ vs best single]\n      rows:\n        - [CSS=1.0 (k=75), 44, 1.187, 0.547, \"+0.013\"]\n        - [CSS≥0.67 (k=75), 98, 1.172, 0.503, \"−0.003\"]\n        - [EAP-IG (k=75), 75, 1.170, ~0.53, \"—\"]\n        - [EP (k=75), 75, 1.170, ~0.53, \"−0.000\"]\n        - [ACDC (k=75), 75, 1.175, ~0.52, \"+0.005\"]\n    - name: \"Table: SVA Pairwise Jaccard (top-k)\"\n      columns: [\"\", EAP-IG, EP, ACDC]\n      rows:\n        - [EAP-IG, \"—\", 0.653, 0.316]\n        - [EP, 0.653, \"—\", 0.418]\n        - [ACDC, 0.316, 0.418, \"—\"]\n  figures_description:\n    - >\n      Bar chart: SVA faithfulness comparison (CSS=1.0 vs single methods)。\n      CSS=1.0 bar 仅微微高于 ACDC bar（Δ=0.013 几乎不可见），与 IOI 的清晰差距形成鲜明对比。\n      旁注标注 \"Δ not statistically significant (single seed)\"。\n    - >\n      SVA CSS distribution histogram (0.33/0.67/1.00) vs IOI — SVA 分布更均匀（44/54/60），\n      IOI 更偏向 1/3（3of3 仅 7 edges vs SVA 的 44），反映 SVA top-k normalization\n      后方法 overlap 更大。\n  analysis: >\n    SVA 在 median 档下是一个 borderline data point。max_jaccard=0.653 → CSS utility\n    预测为低（接近 Arithmetic 的 0.695），实际 Δ=0.013 符合这个预期。\n    对 Claim 1 的贡献：不能 claim CSS faithfulness 优势，只能 claim \"comparable faithfulness\n    at 59% edges\" (44/75)——edge efficiency 论点弱于 IOI（IOI 是 7/100=7%）。\n    对 Claim 2 的贡献：提供了一个 mid-range Jaccard 数据点，方向一致但 CSS advantage 为\n    marginal positive，需要标注 uncertainty。\n    关键风险：reviewer 会问 \"if Δ=0.013 is within noise, how do you distinguish SVA\n    from a CSS-neutral case?\"——需要在论文中诚实承认这一点。\n\n- name: GPT-2 Factual Recall K=3 CSS\n  plan_id: plan_005\n  description: >\n    Distributed computation task on GPT-2 Small。预期高 Jaccard 或 ACDC 收敛困难。\n    GPT-2 Small 的 factual knowledge 有限，ACDC 可能无法产出 clean circuit。\n  expected_results:\n    status: abandoned\n    conclusion: data_not_clean\n    partial_metrics:\n      eapig_completed: true\n      ep_completed: true\n      acdc_completed: false\n      acdc_failure_reason: >\n        GPT-2 Small factual recall accuracy ~55-65% (vs random 25%)，baseline 不稳定。\n        ACDC patching-based search 在 clean performance 波动大时无法收敛——阈值过高电路为空，\n        过低保留近全图。isinf 仅得 3-5 条边，top-k 后 faithfulness 接近随机 (CPR ≈ 0)。\n    note: >\n      实验被终止。不纳入论文分析。在 Limitations 中说明 GPT-2 Small 对 factual recall\n      能力不足以支撑 circuit discovery。\n  result_rationale: >\n    GPT-2 Small (117M) 的 parametric knowledge 极为稀疏——factual recall (\"The capital\n    of France is\") 的准确率在 55-65% 之间波动，意味着模型本身对 clean input 的行为就不一致。\n    EAP-IG 和 EP 可以通过 top-k 强行选出 50-75 条边，但这些边的 faithfulness 接近 baseline\n    （CPR ≈ 0 即移除后模型行为无明显变化），说明 GPT-2 Small 没有形成 dedicated factual\n    retrieval circuit——信息分散在整个 residual stream 中，没有可 localize 的子结构。\n    ACDC 对这种 diffuse computation 最敏感：patching 单条边几乎不改变输出，所有边的\n    importance score 都在噪声水平，无法区分 signal 和 noise。\n    这不是 CSS 方法论的失败，而是 task-model 匹配问题。在 ARR 5/25 deadline 下，\n    合理决策是放弃第四任务，保留 3 个 GPT-2 tasks（IOI + Arithmetic + SVA）。\n  tables: []\n  figures_description: []\n  analysis: >\n    第四任务失败是 median 档的核心限制之一。论文保持 3 个 GPT-2 tasks +\n    Qwen cross-validation。Reviewer 会攻击 \"only 3 tasks on one small model\"——\n    应对：强调 3 个任务覆盖 localized (IOI)、distributed (Arithmetic)、\n    intermediate (SVA) 三种电路结构，加上 Qwen 提供跨模型验证。\n\n- name: Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + ACDC top-k)\n  plan_id: plan_006\n  description: >\n    D029 后用 ACDC top-k 替代 IFR 作为第三方法（IFR 在 Qwen 上 Jaccard=0.000，\n    完全不兼容——IFR 聚焦 early layers m2→a3，EAP-IG/EP 聚焦 deep layers a20.h9，\n    零重叠导致 CSS=1.0 为空集）。ACDC top-k 在 Qwen 上技术可行但需要调参。\n    验证 CSS 跨模型架构（GQA, SwiGLU）的泛化性。\n  expected_results:\n    status: done\n    conclusion: mixed\n    total_edges: 179388\n    binarization: top-k (k=75)\n    pairwise_jaccard:\n      eapig_x_ep: 0.38\n      eapig_x_acdc: 0.22\n      ep_x_acdc: 0.19\n    max_jaccard: 0.38\n    three_way_ratio: 0.09\n    circuit_sizes:\n      eapig_k75: 75\n      ep_k75: 75\n      acdc_k75: 75\n    css_distribution:\n      \"1/3\": 148\n      \"2/3\": 58\n      \"3/3\": 19\n    faithfulness_mean:\n      css_1.00:\n        edges: 19\n        CPR: 0.095\n        CMD: 0.932\n      css_0.67:\n        edges: 58\n        CPR: 0.078\n        CMD: 0.951\n      eapig_k75:\n        edges: 75\n        CPR: 0.082\n        CMD: 0.946\n      ep_k75:\n        edges: 75\n        CPR: 0.071\n        CMD: 0.958\n      acdc_k75:\n        edges: 75\n        CPR: 0.068\n        CMD: 0.962\n    css1_cpr: 0.095\n    css1_vs_best_single: 0.013\n    qwen_acdc_technical_notes: >\n      ACDC 在 179k-edge Qwen graph 上运行时间显著增加（~45min vs GPT-2 的 ~5min）。\n      isinf 产出极少边（< 10），top-k=75 normalization 后产出合理但 faithfulness\n      指标波动较大（不同 random seed 间 CPR 变化 ±0.02）。\n      TransformerLens 不支持 Qwen2.5，全部用 HF-native 实现，与 GPT-2 pipeline\n      不完全对齐——这是潜在的 confound。\n  result_rationale: >\n    Qwen-2.5 0.5B 上 ACDC top-k 替代 IFR 后，三种方法都来自不同算法族但全部\n    基于 performance/loss 信号（gradient、pruning、greedy causal），这意味着\n    方法间的分歧主要来源于搜索策略差异而非 measurement paradigm 差异。\n    EAP-IG×EP Jaccard=0.38 低于 SVA 的 0.653 但高于 IOI GPT-2 的 0.31——\n    Qwen 的 GQA 结构使得 head 内 key-value sharing 改变了 gradient 和 pruning\n    的敏感度分布，但 IOI 的 name mover / S-inhibition 机制在 Qwen 上仍然相对\n    localized，给方法分歧留出空间。ACDC×EAP-IG 和 ACDC×EP 的 Jaccard 较低\n    （0.22/0.19）因为 ACDC 的 greedy search 在大 graph 上的搜索路径与 gradient\n    方法显著不同。\n    CSS=1.0 的 19 条边 CPR=0.095 略优于 EAP-IG 的 0.082（Δ=0.013），方向正确\n    但与 SVA 类似处于 marginal 区间。这是 median 档的特征：CSS 在 low-to-moderate\n    Jaccard 条件下 consistently shows small positive advantage，但没有一个\n    结果足够强到单独 claim significance。\n    核心限制：HF-native pipeline 与 GPT-2 的 TransformerLens pipeline 不完全\n    对齐，跨模型 CPR 比较需要 caveat。\n  tables:\n    - name: \"Table: Qwen-0.5B IOI Faithfulness (mean ablation, k=75)\"\n      columns: [Circuit, Edges, CPR ↑, CMD ↓]\n      rows:\n        - [CSS=1.0, 19, 0.095, 0.932]\n        - [CSS≥0.67, 58, 0.078, 0.951]\n        - [EAP-IG, 75, 0.082, 0.946]\n        - [EP, 75, 0.071, 0.958]\n        - [ACDC, 75, 0.068, 0.962]\n    - name: \"Table: Qwen-0.5B IOI Pairwise Jaccard (top-k=75)\"\n      columns: [\"\", EAP-IG, EP, ACDC]\n      rows:\n        - [EAP-IG, \"—\", 0.38, 0.22]\n        - [EP, 0.38, \"—\", 0.19]\n        - [ACDC, 0.22, 0.19, \"—\"]\n  figures_description:\n    - >\n      Cross-model IOI comparison (GPT-2 vs Qwen): paired bar chart 显示两个模型的\n      CSS=1.0 vs best-single CPR。GPT-2 gap 更大（0.109 vs 0.029, Δ=0.08），\n      Qwen gap 较小（0.095 vs 0.082, Δ=0.013）。Qwen 的 smaller gap 反映了\n      ACDC top-k 与 gradient 方法的 Jaccard 比 GPT-2 ACDC isinf 的更高。\n    - >\n      Jaccard heatmap: 3×3 matrix for Qwen IOI, 与 GPT-2 IOI 并列。\n      Qwen 的整体 Jaccard 更均匀（0.19-0.38），GPT-2 更极端（0.086-0.307）。\n  analysis: >\n    Qwen IOI 是 median 档中最有价值的新增数据点。max_jaccard=0.38 + CSS Δ=+0.013\n    落在 Jaccard-utility 趋势线的预期位置（IOI GPT-2: 0.31/+0.08, SVA: 0.653/+0.013,\n    Arithmetic: 0.695/−0.066 之间）。\n    关键意义：(1) 证明 CSS 跨模型可行（Qwen ≠ GPT-2 架构），(2) ACDC top-k\n    在大模型上作为第三方法的可行性验证，(3) 为 Jaccard-utility 分析提供第 4 个数据点。\n    但 Δ=+0.013 的 marginal nature 意味着 Qwen IOI 不能单独支撑 Claim 1——\n    它只是趋势中的一个 intermediate point。\n\n- name: Qwen-2.5 0.5B Arithmetic K=3 (EAP-IG + EP + ACDC top-k)\n  plan_id: plan_007\n  description: >\n    Qwen 上 Arithmetic/Greaterthan，ACDC top-k 作为第三方法。\n    预期 Jaccard 较高（distributed computation → method convergence），CSS 应失败。\n    验证 Arithmetic 的 CSS-negative 模式跨模型复现。\n  expected_results:\n    status: done\n    conclusion: negative\n    pairwise_jaccard:\n      eapig_x_ep: 0.52\n      eapig_x_acdc: 0.31\n      ep_x_acdc: 0.28\n    max_jaccard: 0.52\n    three_way_ratio: 0.17\n    css_distribution:\n      \"1/3\": 112\n      \"2/3\": 71\n      \"3/3\": 42\n    faithfulness_mean:\n      css_1.00:\n        edges: 42\n        CPR: 0.921\n        CMD: 0.345\n      eapig_k75:\n        edges: 75\n        CPR: 0.968\n        CMD: 0.142\n      ep_k75:\n        edges: 75\n        CPR: 0.951\n        CMD: 0.218\n      acdc_k75:\n        edges: 75\n        CPR: 0.938\n        CMD: 0.274\n    css1_cpr_advantage: -0.047\n    css1_vs_eapig_delta: -0.047\n    note: >\n      CSS=1.0 CPR=0.921 < EAP-IG=0.968。Qwen Arithmetic 确认 CSS-negative。\n      但 max_jaccard=0.52 比 GPT-2 的 0.695 显著降低（Qwen 的 GQA + 更大容量\n      使 comparison computation 更分散），CSS advantage 也从 −0.066 改善到 −0.047。\n  result_rationale: >\n    Arithmetic/Greaterthan 的数值比较计算在 Qwen 上比 GPT-2 更分散——0.5B 参数\n    提供了更多 redundant heads 可以承担 comparison 功能，降低了方法间在 top-k\n    边集上的重合度。EAP-IG×EP Jaccard 从 GPT-2 的 0.695 降至 Qwen 的 0.52，\n    反映了这种分散效应。ACDC 在 Qwen Arithmetic 上的行为也更 diverse（ACDC×EAP-IG=0.31），\n    因为 greedy search 在更大 graph 中有更多备选路径。\n    然而 max_jaccard=0.52 仍然意味着 EAP-IG 和 EP 在超过一半的 top-75 边上达成共识——\n    这些共识边覆盖了 Arithmetic 的核心 comparison pathway，任何 performance-based\n    方法都难以忽略它们。CSS=1.0 的 42 条边要求三方法全部同意，这过滤掉了 ACDC 独特发现的\n    一些 low-importance edges，但也丢失了 EAP-IG×EP 共识中 ACDC 未选中的 important edges。\n    净效果是 CSS=1.0 CPR=0.921 低于 EAP-IG 单方法的 0.968。\n    关键观察：max_jaccard=0.52 落在 Jaccard-utility threshold 的 borderline 区域\n    （定义为 ~0.45-0.55）。如果 threshold 在 0.50 以下，这个点确认 \"above threshold\n    → CSS fails\"；如果 threshold 在 0.55 以上，这个点是一个 near-miss。这种 ambiguity\n    是 median 档的核心特征——趋势清晰但 boundary 模糊。\n  tables:\n    - name: \"Table: Qwen-0.5B Arithmetic Faithfulness (mean ablation, k=75)\"\n      columns: [Circuit, Edges, CPR ↑, CMD ↓]\n      rows:\n        - [CSS=1.0, 42, 0.921, 0.345]\n        - [EAP-IG (k=75), 75, 0.968, 0.142]\n        - [EP (k=75), 75, 0.951, 0.218]\n        - [ACDC (k=75), 75, 0.938, 0.274]\n    - name: \"Table: Arithmetic Cross-Model Comparison\"\n      columns: [Model, Max Jaccard, CSS=1.0 CPR, Best Single CPR, Δ]\n      rows:\n        - [GPT-2, 0.695, 0.919, 0.985, \"−0.066\"]\n        - [Qwen-0.5B, 0.52, 0.921, 0.968, \"−0.047\"]\n  figures_description:\n    - >\n      在 Jaccard-utility scatter plot 中，Qwen Arithmetic 的数据点 (0.52, −0.047)\n      落在 GPT-2 Arithmetic (0.695, −0.066) 的左上方（更低 Jaccard，更小 negative\n      advantage），方向一致、趋势线延伸自然。\n  analysis: >\n    Qwen Arithmetic 的 negative result 在 reframed narrative 下是资产：\n    (1) 确认 high-Jaccard → CSS fails 的模式跨模型稳定，\n    (2) max_jaccard 从 0.695 降至 0.52 伴随 CSS disadvantage 从 0.066 缩小至 0.047，\n        精确地落在 Jaccard-utility 趋势线上，\n    (3) 提供了第 4 个（或第 3 个，取决于 SVA 是否计入）有效数据点。\n    但 max_jaccard=0.52 接近 putative threshold（~0.5），使 threshold 估计更不确定——\n    如果这个点被归为 \"near-threshold ambiguous\"，有效的 clear positive 和 clear negative\n    数据点各减少一个。\n\n- name: Gemma-2 2B IOI K=3\n  plan_id: plan_008\n  description: >\n    Scale to 2B model (Gemma-2). P2 优先级。需要 ~16 GPU-hours 和经过验证的\n    ACDC top-k pipeline for larger models。\n  expected_results:\n    status: not_attempted\n    conclusion: null\n    reason: >\n      时间和 GPU 资源不足。plan_004 (SVA 重新评估) + plan_006 (Qwen IOI ACDC) +\n      plan_007 (Qwen Arith) 已消耗大部分 12 天 budget。Gemma-2 2B 需要额外的\n      EP 内存优化（2B model edge-level pruning 在 RTX 4090D 24GB 上 borderline），\n      且 ACDC 在 2B graph 上可能需要 gradient checkpointing。在 ARR 5/25 前\n      无法完成实验 + 分析 + 论文写作。\n  result_rationale: >\n    Median 档的时间约束下，优先完成 Qwen 两个任务（验证跨模型 + ACDC top-k pipeline）\n    已消耗大部分 Phase 2 budget。Gemma-2 实验依赖 plan_006 的 pipeline 验证结果，\n    且需要额外的工程工作（EP 内存、ACDC 长运行时间、模型下载 ~5GB）。\n    即使勉强跑完 Gemma-2 IOI，结果只增加一个数据点——在 deadline 压力下，\n    投入产出比不如把时间用在论文写作和现有数据的 robust 分析上。\n  tables: []\n  figures_description: []\n  analysis: >\n    Not attempted。在 Limitations 中列为 model scale generalization future work。\n    论文 claim \"GPT-2 (117M) + Qwen (500M)\" 两个 scale，reviewer 会追问更大模型，\n    但可以 argue 核心 finding (Jaccard predicts CSS utility) 是 method-level\n    property 不 fundamentally depend on model scale。\n\n- name: Llama-3.1 8B IOI K=3\n  plan_id: plan_009\n  description: >\n    Scale to 8B model. P3 优先级。需要 A100 80GB（RTX 4090D 24GB 不够 EP）。\n  expected_results:\n    status: not_attempted\n    conclusion: null\n    reason: >\n      P3 优先级 + 硬件不足（需要 A100 80GB）+ plan_008 未完成作为前置。\n      远超 deadline 范围。\n  result_rationale: >\n    8B 模型需要 A100 80GB 级 GPU 来运行 EP（edge-level pruning 的内存需求\n    随 model size 超线性增长），当前 RTX 4090D 24GB 完全不够。即使有硬件，\n    单次 ACDC 运行可能需要数小时，3 方法 × 调参 → 不现实。\n  tables: []\n  figures_description: []\n  analysis: >\n    Not attempted。Future work stretch goal。有 Qwen 0.5B 已经够 claim\n    \"beyond GPT-2 Small\"。\n\n- name: Top-k Binarization Sensitivity Sweep\n  plan_id: plan_010\n  description: >\n    在已完成的 model×task pairs 上系统扫描 k=50/75/100/150。\n    验证 CSS=1.0 CPR 在不同 k 下的稳定性，回应 R5。\n  expected_results:\n    status: done\n    conclusion: partially_stable\n    ioi_gpt2:\n      k50: {css_1.0_edges: 7, css_1.0_cpr: 0.109}\n      k75: {css_1.0_edges: 12, css_1.0_cpr: 0.105}\n      k100: {css_1.0_edges: 18, css_1.0_cpr: 0.098}\n      k150: {css_1.0_edges: 24, css_1.0_cpr: 0.093}\n      verdict: \"stable (CPR range 0.093-0.109, Δ=0.016)\"\n    arithmetic_gpt2:\n      k50: {css_1.0_edges: 44, css_1.0_cpr: 0.919}\n      k75: {css_1.0_edges: 54, css_1.0_cpr: 0.919}\n      k100: {css_1.0_edges: 62, css_1.0_cpr: 0.926}\n      k150: {css_1.0_edges: 71, css_1.0_cpr: 0.933}\n      verdict: \"stable (CPR range 0.919-0.933, Δ=0.014)\"\n    sva_gpt2:\n      k50: {css_1.0_edges: 15, css_1.0_cpr: 0.891}\n      k75: {css_1.0_edges: 23, css_1.0_cpr: 0.941}\n      k100: {css_1.0_edges: 29, css_1.0_cpr: 0.944}\n      k150: {css_1.0_edges: 38, css_1.0_cpr: 0.940}\n      verdict: \"sensitive at k=50 (CPR drop 0.05), stable k=75-150\"\n    qwen_ioi:\n      k50: {css_1.0_edges: 11, css_1.0_cpr: 0.074}\n      k75: {css_1.0_edges: 19, css_1.0_cpr: 0.095}\n      k100: {css_1.0_edges: 26, css_1.0_cpr: 0.091}\n      k150: {css_1.0_edges: 35, css_1.0_cpr: 0.088}\n      verdict: \"sensitive at k=50 (CPR drop 0.021), stable k=75-150\"\n    overall_verdict: >\n      CSS=1.0 CPR 在 k=75-150 范围内基本稳定（max Δ < 0.016 for IOI/Arith,\n      < 0.004 for SVA k≥75）。k=50 在 SVA 和 Qwen IOI 上 CPR 下降 0.02-0.05，\n      因为 k=50 过小导致方法重叠不足、CSS=1.0 边数太少。\n      推荐 k=75 作为默认值。但 SVA k=50 的 sensitivity 是可被攻击的 degree of freedom。\n  result_rationale: >\n    Top-k normalization 将 ACDC 的 arbitrary isinf binarization 替换为固定 edge budget，\n    使三种方法在 comparable scale 下比较。k 越大，每个方法保留更多边，pairwise overlap\n    概率增加，CSS=1.0 集合扩大——新增的 consensus 边包含更多低置信度的偶然共识，CPR 微降。\n    k=75-150 范围内这个效应很温和（IOI CPR 变化 0.016），因为核心 consensus edges\n    在这个 k 范围内始终被选中。\n    k=50 的 sensitivity 来源不同：SVA 和 Qwen IOI 的电路较 concentrated，k=50 时\n    可能恰好切掉了某方法 borderline 但 functionally important 的边，导致 CSS=1.0\n    丢失关键 consensus 成员。这不是 CSS 方法论的缺陷，而是 k 需要大于某个 minimum\n    （约 60-70）才能让方法有足够的 overlap base。\n    IOI GPT-2 的 k=50 不受影响是因为 GPT-2 IOI 的 ACDC isinf 只有 14 条边，\n    top-k=50 已远超 isinf 集合，CSS=1.0 的 7 条核心边全在 k=50 range 内。\n  tables:\n    - name: \"Table: CSS=1.0 CPR across k values\"\n      columns: [Task/Model, k=50, k=75, k=100, k=150, Max Δ, Verdict]\n      rows:\n        - [IOI/GPT-2, 0.109, 0.105, 0.098, 0.093, 0.016, stable]\n        - [Arith/GPT-2, 0.919, 0.919, 0.926, 0.933, 0.014, stable]\n        - [SVA/GPT-2, 0.891, 0.941, 0.944, 0.940, 0.053, \"k=50 sensitive\"]\n        - [IOI/Qwen, 0.074, 0.095, 0.091, 0.088, 0.021, \"k=50 sensitive\"]\n  figures_description:\n    - >\n      Line plot: x=k, y=CSS=1.0 CPR, four lines (one per task×model).\n      灰色 band 标记 k=75-150 稳定区间。k=50 处 SVA 和 Qwen IOI 有明显 dip。\n  analysis: >\n    Binarization ablation 支撑 Claim 3（top-k 修复 isinf 退化）且 k=75-150 稳定。\n    SVA/Qwen k=50 的 sensitivity 是 reviewer 攻击点但可防守：k=50 对 32k+ edge\n    graph 仅保留 0.15% edges，低于合理下界。推荐 k=75 作为 default 并在 appendix\n    放完整 sweep 数据。\n\n- name: Ablation Method Comparison (Zero vs Mean)\n  plan_id: plan_011\n  description: >\n    在 IOI 上比较 zero 和 mean ablation 下的 CSS 优势。P2 优先级。\n    Resample ablation 和 SVA/Arithmetic 的 ablation 对比因时间不足未完成。\n  expected_results:\n    status: partial\n    conclusion: directionally_consistent\n    completed_tasks: [IOI (GPT-2)]\n    ioi_gpt2:\n      zero_ablation:\n        css_1.0_cpr: 0.109\n        best_single_cpr: 0.029\n        css_advantage: 0.080\n      mean_ablation:\n        css_1.0_cpr: 0.118\n        best_single_cpr: 0.095\n        css_advantage: 0.023\n    note: >\n      仅完成 IOI 一个 task 的 zero vs mean 对比。CSS advantage 方向一致（正），\n      但绝对值差异大——zero ablation 下 Δ=0.080，mean ablation 下 Δ=0.023。\n      Resample ablation 未完成。SVA 和 Arithmetic 未完成。\n  result_rationale: >\n    Zero ablation 将电路外所有边的 activation 清零，这对电路外的破坏最大，使得\n    \"真正重要的电路\" 和 \"不重要的电路\" 之间的 CPR 差距放大。CSS=1.0 作为最精简的\n    consensus 子集，在 zero ablation 下受益最大（保留的 7 条边全是 critical path，\n    丢失少量非 critical 边的惩罚小）。\n    Mean ablation 更温和——baseline 是均值而非零，电路外的 \"noise\" 被部分保留，\n    所有方法的 CPR 都偏高，CSS=1.0 与 single method 的差距被压缩。\n    关键 insight：CSS advantage 在两种 ablation 下都为正，说明 consensus 的\n    信号不是 evaluation artifact。但 Δ=0.023 (mean) vs Δ=0.080 (zero) 意味着\n    论文主实验使用的 evaluation method 会显著影响 reported advantage 的量级——\n    reviewer 会追问这一点。\n    仅有 IOI 一个 task 的数据不足以 claim robustness across tasks。\n  tables:\n    - name: \"Table: IOI CSS advantage under different ablation methods\"\n      columns: [Ablation, CSS=1.0 CPR, Best Single CPR, Δ]\n      rows:\n        - [Zero, 0.109, 0.029, \"+0.080\"]\n        - [Mean, 0.118, 0.095, \"+0.023\"]\n  figures_description: []\n  analysis: >\n    部分完成。IOI 上 CSS advantage 在 zero 和 mean 下方向一致。\n    可在 Appendix 放 IOI 的 ablation robustness table。\n    Reviewer 追问时可 footnote \"CSS advantage directionally stable across\n    evaluation methods; magnitude varies with ablation aggressiveness, as expected.\"\n    Full multi-task ablation 列为 future work。\n\n- name: CIRCUS vs CSS Negative Ablation\n  plan_id: plan_012\n  description: >\n    使用 D021 中 CIRCUS 的已有失败结果作为 negative ablation。\n    0 GPU hours，仅需分析和写作。直接对比 CIRCUS core vs CSS=1.0 on IOI。\n  expected_results:\n    status: done\n    conclusion: negative_ablation_confirmed\n    circus_vs_css:\n      ioi:\n        circus_core_edges: 15\n        circus_core_cpr: -0.108\n        css_1.0_edges: 7\n        css_1.0_cpr: 0.109\n    circus_failure_modes:\n      - \"CIRCUS 基于 single-method (EAP-IG) faithfulness scoring 选 core edges\"\n      - \"scoring 依赖 ablation method 和 threshold，三次运行结果不一致 (edges: 12, 15, 18)\"\n      - \"CSS binary consensus 不需要 score calibration，避免了 CIRCUS 的核心缺陷\"\n    note: >\n      仅在 IOI 上有 CIRCUS 数据。SVA 和 Arithmetic 上未跑 CIRCUS（无额外 GPU 预算）。\n      单 task negative ablation 说服力有限但结果清晰。\n  result_rationale: >\n    CIRCUS (Parekh 2026) 在 IOI 上的 D021 结果：core edges CPR=−0.108（负值），\n    说明 CIRCUS 的 \"most stable\" edges 实际上破坏了模型行为。这是因为 CIRCUS\n    在 EAP-IG 内部做 threshold sweep 选 core——EAP-IG 的系统性偏差（过度依赖\n    early-layer attention gradient）被 CIRCUS 放大而非纠正。\n    CSS=1.0 通过 cross-method agreement 过滤了单方法偏差：即使 EAP-IG 对某些\n    early-layer edges 评分过高，如果 EP 和 ACDC 不同意，这些边被排除。\n    CIRCUS CPR=−0.108 vs CSS CPR=+0.109 的反差是论文中最 \"clean\" 的结果之一。\n    但仅有 IOI 一个 task 的数据意味着 reviewer 可以质疑 CIRCUS 在其他 task/setting\n    下是否同样差——Parekh 的原始结果可能在更大模型或不同任务上表现不同。\n    论文应 hedge：\"on the tasks we evaluated, structural consensus outperforms\n    within-method stability selection.\"\n  tables:\n    - name: \"Table: CSS vs CIRCUS on IOI\"\n      columns: [Method, Edges, CPR ↑, CMD ↓, Reproducible?]\n      rows:\n        - [CSS=1.0, 7, 0.109, 0.911, \"Yes (deterministic)\"]\n        - [CIRCUS core, 15, −0.108, 1.134, \"No (12-18 edges across runs)\"]\n  figures_description:\n    - >\n      Two-bar comparison: CSS=1.0 (blue, positive) vs CIRCUS (grey, negative) on IOI.\n      简洁有力的 visual contrast。\n  analysis: >\n    CIRCUS negative ablation 是 Claim 3 (binarization pathology → top-k fix)\n    和 Claim 4 (CSS taxonomy) 的有力 supporting evidence。结果清晰、对比公平、\n    计算成本为零。但仅 IOI 一个 task 限制了 generalizability claim。\n    在 Related Work 中用一段 + 一个 table 展示。\n\n- name: Jaccard-CSS Utility Correlation Analysis\n  plan_id: plan_013\n  description: >\n    汇总所有 model×task 组合的 (max pairwise Jaccard, CSS CPR advantage)，\n    计算 Spearman 相关系数。这是 reframed Claim 2 的核心证据。\n    Median 档下有 3-4 个有效数据点（取决于 SVA 是否计入为 \"marginal positive\"）。\n  expected_results:\n    status: done\n    conclusion: trend_visible_not_significant\n    data_points:\n      - task: IOI (GPT-2)\n        max_jaccard: 0.31\n        css_advantage: 0.080\n        css_wins: true\n        quality: clear_positive\n      - task: SVA (GPT-2)\n        max_jaccard: 0.653\n        css_advantage: 0.013\n        css_wins: marginal\n        quality: borderline\n      - task: Arithmetic (GPT-2)\n        max_jaccard: 0.695\n        css_advantage: -0.066\n        css_wins: false\n        quality: clear_negative\n      - task: IOI (Qwen)\n        max_jaccard: 0.38\n        css_advantage: 0.013\n        css_wins: marginal\n        quality: borderline\n    spearman_rho: -0.80\n    spearman_p: 0.20\n    n_data_points: 4\n    threshold_estimate: \"~0.50 (visual estimate, large uncertainty)\"\n    low_jaccard_css_pass_fraction: 0.50\n    note: >\n      4 个数据点：1 个 clear positive (IOI GPT-2)，2 个 marginal (SVA, Qwen IOI)，\n      1 个 clear negative (Arithmetic GPT-2)。\n      如果加入 Qwen Arithmetic (max_jaccard=0.52, css_advantage=−0.047)\n      作为第 5 个点，Spearman rho 改善至 −0.90, p=0.037——但这依赖于\n      Qwen Arithmetic 实验是否在 deadline 前完成。\n      趋势方向正确（higher Jaccard → lower CSS utility）但 p > 0.1 at n=4。\n  result_rationale: >\n    4 个 model×task 数据点的 Spearman rho=−0.80 方向清晰但统计力不足（p=0.20，\n    因为 n=4 下 even perfect rank correlation 的 p 也只有 0.042）。\n    趋势的 mechanistic 解释仍然成立：低 Jaccard 意味着方法独立发现不同 edge sets，\n    交集代表 multi-perspective validated core → higher faithfulness。\n    高 Jaccard 意味着方法收敛，consensus 退化为最 selective 的单方法。\n    但 4 个数据点中有 2 个 \"extremes\"（IOI clearly positive, Arithmetic clearly\n    negative）和 2 个 \"borderlines\"（SVA Δ=+0.013, Qwen IOI Δ=+0.013），\n    趋势的 robustness 高度依赖 borderline points 的归类。\n    如果把 SVA 和 Qwen IOI 都视为 \"CSS neutral\"（Δ < 0.02 ≈ noise），\n    那么只有 IOI GPT-2 是 CSS positive，success rate = 1/3 for GPT-2 tasks。\n    这就是 median 档的核心 tension：趋势可见，但无法区分 \"weak but real pattern\"\n    和 \"IOI 是唯一 positive case + noise\"。\n\n    加入 Qwen Arithmetic（如果完成）将 n 提升到 5，rho 改善到 −0.90 (p=0.037)，\n    勉强过 significance threshold。这使得 Qwen Arithmetic 成为 median 档中\n    最关键的 \"swing experiment\"。\n\n    threshold estimate ~0.50 基于 4 个点的 visual interpolation，置信区间极宽\n    （可能 [0.35, 0.65]），不具 predictive power。论文中应报告为 \"preliminary\n    estimate\" 而非 actionable guideline。\n  tables:\n    - name: \"Table: Jaccard vs CSS Advantage (all experiments)\"\n      columns: [Task, Model, Methods, Max Jaccard, CSS=1.0 CPR, Best Single CPR, Δ, Verdict]\n      rows:\n        - [IOI, GPT-2, \"EAP-IG/EP/ACDC\", 0.31, 0.109, 0.029, \"+0.080\", \"✓ PASS\"]\n        - [SVA, GPT-2, \"EAP-IG/EP/ACDC\", 0.653, 1.187, 1.175, \"+0.013\", \"~ marginal\"]\n        - [IOI, Qwen-0.5B, \"EAP-IG/EP/ACDC\", 0.38, 0.095, 0.082, \"+0.013\", \"~ marginal\"]\n        - [Arithmetic, GPT-2, \"EAP-IG/EP/ACDC\", 0.695, 0.919, 0.985, \"−0.066\", \"✗ FAIL\"]\n    - name: \"Table: Jaccard-Utility Correlation Statistics\"\n      columns: [Metric, Value]\n      rows:\n        - [N data points, 4]\n        - [Spearman ρ, −0.80]\n        - [Spearman p, 0.20]\n        - [\"Threshold estimate\", \"~0.50 (±0.15)\"]\n        - [\"Low-Jaccard (<0.50) CSS PASS fraction\", \"1/2 clear + 1/2 marginal\"]\n  figures_description:\n    - >\n      KEY FIGURE: Scatter plot — x: max pairwise Jaccard, y: CSS CPR advantage。\n      4 个点，颜色区分模型（GPT-2 蓝色, Qwen 橙色），形状区分任务。\n      灰色虚线 y=0。拟合线斜率为负但 95% CI band 很宽（几乎覆盖全图）。\n      右上角标注 ρ=−0.80, p=0.20, n=4。\n      与 best tier 的 6-point tight fit (ρ=0.94, p=0.005) 形成鲜明对比——\n      这里的 pattern 是 \"suggestive\" 而非 \"conclusive\"。\n    - >\n      Heatmap: rows=tasks, cols=method pairs, cells=Jaccard values。\n      Annotated with CSS outcome per task。帮助 reader 直观理解\n      \"which method pair drives max_jaccard\"。\n  analysis: >\n    Jaccard-utility 分析是 reframed narrative 的 crown jewel，但在 median 档下\n    它更像一个 \"hypothesis-generating observation\" 而非 \"validated finding\"。\n    4 个数据点 + p=0.20 意味着论文必须非常谨慎地措辞：\n    \"We observe a negative trend between max pairwise Jaccard and CSS faithfulness\n    advantage (ρ=−0.80, n=4), consistent with the hypothesis that CSS utility\n    depends on method diversity. While the trend does not reach statistical\n    significance at conventional thresholds (p=0.20), the direction is mechanistically\n    motivated and consistent across both models tested.\"\n\n    如果 Qwen Arithmetic（plan_007）在 deadline 前完成并纳入，n=5 + ρ≈−0.90 + p≈0.037\n    将显著改善说服力。这使 plan_007 成为 median 档中最 high-leverage 的实验——\n    应优先保证它的完成。\n\n    Low-Jaccard (<0.50) CSS PASS fraction = 1 clear + 1 marginal out of 2 cases = 50%-100%\n    取决于 \"marginal\" 是否算 PASS。这个 pass rate 远低于 best tier 的 100%，\n    但 reframed claim 不需要 CSS always wins——只需要 \"Jaccard predicts when CSS wins\"。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "70026870-1453-4c76-a242-1415b4692a0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-13T08:37:01.185Z_

```json
{
  "parentUuid": "da60ce81-7513-4615-813a-5cda062d4c04",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6a7daa7b-9e4c-4ed9-bc42-d679f1dcbf41",
  "timestamp": "2026-05-13T08:37:01.185Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：SVA marginal PASS（统计上弱），Qwen ACDC 技术可行但结果 mixed；Jaccard-utility 趋势可见但数据点不足以达到统计显著 核心假设：['SVA css_1.00 Δ(CPR) ∈ [0.005, 0.03]，condition④ technically PASS…",
  "leafUuid": "6a7daa7b-9e4c-4ed9-bc42-d679f1dcbf41",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframed CSS paper: Jaccard-predicted utility",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb"
}
```

---

### Assistant

_source line 40 · 2026-05-13T08:37:13.986Z_

已生成 median 档 imagined_experiments.yaml，覆盖 plan_004 到 plan_013 共 10 个实验。

核心差异 vs best tier：
- **plan_004 SVA**: marginal PASS (Δ=0.013)，非 strong positive，max_jaccard=0.653 接近 Arithmetic
- **plan_005 Factual**: abandoned（GPT-2 Small 能力不足）
- **plan_006 Qwen IOI**: 改用 ACDC top-k（非 IFR），CSS Δ=+0.013 marginal，max_jaccard=0.38
- **plan_007 Qwen Arith**: CSS negative（Δ=−0.047），但 Jaccard 从 0.695 降至 0.52，趋势一致
- **plan_008/009**: not attempted
- **plan_010**: k=75-150 稳定，k=50 SVA/Qwen 敏感
- **plan_011**: 仅 IOI zero vs mean，方向一致但量级差异大
- **plan_012**: CIRCUS negative ablation 确认（仅 IOI）
- **plan_013**: 4 个数据点 ρ=−0.80 p=0.20，趋势可见但不显著；加入 Qwen Arith 后 n=5 可改善到 p≈0.037

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a7daa7b-9e4c-4ed9-bc42-d679f1dcbf41",
  "isSidechain": false,
  "requestId": "req_011CazGFjE86kTpQpwYN2TjN",
  "type": "assistant",
  "uuid": "3789a98f-e589-492a-9633-4dfc7e7156e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjHzkCvDCC1AWdewuakGnU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15153,
      "cache_read_input_tokens": 58434,
      "output_tokens": 378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 378,
          "cache_read_input_tokens": 58434,
          "cache_creation_input_tokens": 15153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15153
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

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：SVA marginal PASS（统计上弱），Qwen ACDC 技术可行但结果 mixed；Jaccard-utility 趋势可见但数据点不足以达到统计显著 核心假设：['SVA css_1.00 Δ(CPR) ∈ [0.005, 0.03]，condition④ technically PASS…",
  "leafUuid": "3789a98f-e589-492a-9633-4dfc7e7156e1",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframed CSS paper: Jaccard-predicted utility",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb"
}
```

---
