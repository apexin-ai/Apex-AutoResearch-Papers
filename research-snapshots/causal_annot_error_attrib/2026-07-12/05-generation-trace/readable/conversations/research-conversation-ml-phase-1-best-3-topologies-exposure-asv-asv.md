# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：≥3 topologies (含 exposure) 出现方向反转；ASV 框架在所有优先拓扑上均具备单调性+紧性证明；经验数据清晰展示 ASV 的实用

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/e14e2c22-1d8d-4bf4-953a-e482c1a8d81f.jsonl`
- **Structured JSON:** [`3c0b5b4f82c200f866b7.json`](../../sessions/3c/3c0b5b4f82c200f866b7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T07:47:54.488Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T07:47:54.488Z",
  "sessionId": "e14e2c22-1d8d-4bf4-953a-e482c1a8d81f",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：≥3 topologies (含 exposure) 出现方向反转；ASV 框架在所有优先拓扑上均具备单调性+紧性证明；经验数据清晰展示 ASV 的实用价值\n核心假设：['mediation 和 collider DAG 在 non-differential K≥3 误分类下均出现方向反转（100k random C 搜索 violation rate ≥30%）', '至少 1 个额外拓扑（M-bias/instrument/front-door）也出现反转', 'ASV 单调性和紧性在 confounding/mediation/collider 三个优先拓扑上均有完整形式化证明', '经验混淆矩阵（3 LLM × 3 task）覆盖足够多样的 C 结构，ASV 排序与实际 bias 严重度一致', 'correction framework 在 ≥93% 场景中推荐最优方法']\n关键指标范围：{'reversal_topologies_count': [3, 5], 'mediation_violation_rate': [0.3, 0.85], 'collider_violation_rate': [0.3, 0.85], 'theory_mc_match_rate': [0.95, 1.0], 'asv_coverage_at_95_nominal': [0.93, 0.97], 'asv_sharpness_formal_proofs': [3, 3], 'binarization_max_delta': [0.15, 0.25], 'correction_framework_accuracy': [0.93, 0.98], 'empirical_asv_concordance': [8, 9]}\n叙事方向：Version A 完全成立。Lead finding: non-differential multi-class error 在多个 DAG 拓扑中打破经典 toward-null 保证，且反转模式是拓扑依赖的。Taxonomy 揭示了不可化约的 {C structure × topology} 交互效应。三条 claims 无需调整：taxonomy 覆盖广、ASV 有完整理论保证、correction guidance 在几乎所有场景有效。Headline: \"the same confusion matrix that is benign in confounding topology produces direction-reversing bias in mediation/collider.\"\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: causal_annot_error_attrib\nfocus: Key uncertainty: will mediator/collider DAGs show direction reversal under non-differential multi-class error? Confounding DAG was monotonic in MVP. Also: is ASV framework practically useful enough vs just reporting confusion matrices?\n\n## paper_framing.md\n\n# Paper Framing — causal_annot_error_attrib\n\n## Target Venue\n- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)\n- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)\n- Tertiary: ICWSM 2027 Round 2 (2026-09-15)\n\n## Title\nMulti-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies\n\n## Core Claims (3 条)\n\n1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 6 canonical social-science DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door).\n\n2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of differential annotation error needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Reported alongside estimates, analogous to E-values for unmeasured confounding. Formal proofs (monotonicity + sharpness) for 3 priority topologies; MC-validated conjectures for the remaining 3.\n\n3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI, MLA, naive plug-in), characterizing regimes where each applies and where no existing method suffices — including dependence-aware multi-LLM correction as an open problem.\n\n## Story Spine\n\n- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31% of downstream conclusions are already incorrect. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable.\n\n- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.\n\n- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.\n\n- **Headline result template**: \"Across 6 DAG topologies with K=3,5,7, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. On 3 CSS tasks annotated by 3 LLMs, ASVs provide calibrated robustness indicators, and our taxonomy identifies cases where commonly applied corrections would increase rather than decrease bias.\"\n\n## Core Insight (Lead Finding) — DUAL VERSION, gate on plan_001\n\n### Version A (≥1 topology shows direction reversal under K≥3 non-differential exposure misclassification)\nThe binary guarantee that \"non-differential exposure misclassification biases toward the null\" (Bross 1954) breaks in the multi-class case. For specific confusion matrix structures in specific DAG topologies, K≥3 non-differential error can amplify or reverse effect estimates. Brenner (1993) identified this possibility for polytomous confounder misclassification (\"bias can go in either direction\"); we provide the first systematic characterization across 6 DAG topologies with exact conditions for each {C structure × topology} cell. Furthermore, binarizing a K-class variable to \"escape\" into the binary regime is itself hazardous — collapsing introduces new, direction-unpredictable bias (MVP evidence: Δ up to 0.103).\n\n### Version B (no direction reversal found across topologies)\nMulti-class annotation error is structurally irreducible to the binary case: the downstream bias magnitude depends on the full K×K confusion matrix in ways that binary sensitivity/specificity cannot predict, and binarizing a K-class variable introduces new bias (MVP evidence: Δ up to 0.103). While non-differential error preserves bias direction across tested topologies (a useful practitioners' guarantee), the magnitude varies dramatically with confusion matrix structure (0.13–0.30 in confounding DAG alone), and this variation is topology-dependent. ASVs provide the missing robustness measure for this quantitative — not directional — uncertainty.\n\n**Gate**: plan_001 results determine which version. ≥2 topologies with reversal → A; 1 → A with that topology as lead; 0 → B. See D003.\n\n## MVP Evidence\n\n**Confounding DAG + K=3** (confounder misclassification):\n- Theoretical bias expressions match MC perfectly (6/6 structures within 95% CI) — framework validated\n- Binary collapse ≠ multi-class: Δ up to 0.103 (near-permutation C), proving K=3 retains more confounding control than binarization\n- 100k random C search: confounding DAG bias is monotonically toward OVB — this topology is \"well-behaved\" (predictable direction)\n- NOTE: Confounding DAG tests residual confounding, NOT bias-toward-null (Bross 1954). Criterion 2 (away-from-null bias) holds for binary too in this topology. See M001.\n\n**Exposure DAG K=3** (exposure misclassification — D002/D004 CONFIRMED):\n- 100k random C: 85% violate bias-toward-null, 83.4% sign reversal, 14.1% amplification\n- K=2 control: 6/6 toward null (binary guarantee holds)\n- Worst case: β=1.0 → estimate=-0.84 (sign reversal + 2.83x amplification)\n- Mechanism: near-permutation C causes label swap → effect direction flips (structurally impossible in K=2)\n- **Two-DAG contrast**: confounding (monotonic, predictable) vs exposure (unpredictable, topology-dependent) — validates core claim\n\n## Venue Fit Risks\n\n- **AAAI**: Broad AI audience — emphasize general methodology for \"automated annotation measurement error,\" not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.\n- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.\n- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n1. **\"Trivial extension of binary to multi-class\"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 6 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]\n\n2. **\"Lee & Wood-Doughty (2024) already did categorical\"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 6 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]\n\n3. **\"Why these 6 DAG topologies?\"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]\n\n4. **\"K≥5 expressions aren't actionable\"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]\n\n5. **\"ASV sharpness only proved for 3 topologies\"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]\n\n6. **\"Correlated multi-LLM errors?\"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]\n\n7. **\"Empirical validation scope\"** → 3 CSS tasks × 3 LLMs × 3 DAG-relevant scenarios. Tasks selected to cover K=2,3,5 annotation complexity. [Experiments: plan_003, plan_006]\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: Derive and MC-validate bias expressions for 6 DAG topologies with K=3\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n  details: 'For each topology (confounding, mediation, collider, M-bias, instrument,\n    front-door): derive closed-form K=3 bias expression, validate with MC (1000 reps\n    × N=10000, 6 confusion matrix structures including near-permutation extreme).\n    Key question: which topologies show direction reversal under non-differential\n    error? Confounding already validated in MVP (no reversal, monotonic toward OVB).\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  description: Extend bias expressions to K=5,7 — matrix notation + interpretability\n    tools\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'Matrix-form expressions for general K. Three interpretability tools: (a)\n    eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar\n    bounds collapsing matrix to conservative scalar, (c) diagnostic visualizations\n    mapping confusion matrix regions to bias magnitude. Validate on confounding +\n    mediation + collider DAGs with K=5,7.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 1\n  description: 'Empirical confusion matrices: 3 LLMs × 3 CSS tasks vs gold-standard'\n  priority: P0\n  gpu_budget_hours: 0\n  api_cost_estimate: $300-550\n  deps: []\n  details: 'Tasks: protest event coding (K=5, ACLED/GPT-RE), stance detection (K=3,\n    SemEval/VAST), toxicity (K=2, as special case / consistency check, Civil Comments).\n    Models: Llama 4 Maverick (Together.ai), Qwen 3.5 Plus (OpenRouter), DeepSeek V4\n    (DeepSeek API). ~30K annotations per model × 3 datasets × 3 prompt variants. Output:\n    empirical confusion matrices, inter-model correlation analysis, downstream regression\n    bias vs gold-standard baseline.\n\n    '\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Binarization collapse analysis: K→2 folding bias across all 6 topologies'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'For each of 6 topologies with K=3,5,7: collapse to binary, compare bias\n    from full multi-class expression vs binarized expression. Demonstrate that binarization\n    is not a safe shortcut — can amplify or reverse bias. MVP showed Δ up to 0.089\n    for confounding DAG K=3.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'ASV framework: formal proofs for confounding, mediation, collider'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'Derive ASV expressions for 3 priority topologies. Formal proofs of: (a)\n    monotonicity (ASV increases with δ amplification), (b) sharpness (bound is achievable\n    for some confusion matrix). MC validation: coverage at 90%, 95%, 99% levels across\n    1000 scenarios.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 2\n  description: ASV MC validation for M-bias, instrument, front-door topologies\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_004\n  details: 'ASV expressions + MC validation of monotonicity and coverage. Sharpness\n    stated as conjectures supported by numerical evidence. If any topology fails monotonicity\n    under MC, flag and investigate.\n\n    '\n  status: planned\n- id: plan_006\n  claim: 2\n  description: ASV calibration on empirical data (3 CSS tasks × 3 LLMs)\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  - plan_004\n  details: 'Apply ASVs to empirical confusion matrices from plan_003. Validate coverage\n    on held-out gold-standard splits. Report ASV alongside downstream effect estimates\n    for each task. Compare ASV interpretability with raw confusion matrix reporting.\n\n    '\n  status: planned\n- id: plan_007\n  claim: 3\n  description: 'Correction guidance framework: decision mapping + validation'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_004\n  - plan_003\n  details: 'Decision framework: {topology × error structure × ASV} → correction method\n    (DSL / PPI / MLA / naive plug-in / \"no existing method adequate\"). MC validation:\n    recommended method produces least bias in ≥90% of scenarios. Empirical validation\n    on plan_003 data. Characterize regimes where no existing method suffices (correlated\n    errors, differential multi-class, etc.) — identify as open problems.\n\n    '\n  status: planned\n- id: plan_009\n  claim: 1\n  description: Pathological confusion matrix analysis (near-permutation, rank-deficient)\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'Extreme C structures: near-permutation, rank-deficient, block-diagonal.\n    Characterize when bias becomes catastrophic across topologies. Identify structural\n    conditions (spectral gap, diagonal dominance ratio) that predict bias severity\n    — candidate features for practitioners.\n\n    '\n  status: planned\n- id: plan_010\n  claim:\n  - 1\n  - 2\n  - 3\n  description: annot-sensitivity Python toolkit (open-source release)\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_004\n  - plan_007\n  details: 'Package: user-specified DAG + confusion matrix(es) + downstream estimate\n    → bias expressions (scalar K≤3, matrix K>3 with interpretability) + ASV bounds\n    + sensitivity curves + correction recommendation + diagnostic plots. pip-installable,\n    with worked examples for each topology.\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_confounding_dag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    theory_mc_match: 6/6\n    pass_criteria: 3/3\n    max_binary_collapse_delta: 0.103\n    bias_range: 0.132-0.298\n    ovb_reference: 0.3\n    direction_reversal_found: false\n    random_search_100k_min_bias: 0.063\n- exp_id: mvp_exposure_dag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    theory_mc_match: 5/5\n    pass_criteria: 3/3\n    violation_rate: 0.85\n    sign_reversal_rate: 0.834\n    amplification_rate: 0.141\n    K2_toward_null: 6/6\n    worst_severity: 2.83\n    named_structures_with_violation: 3/6\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T07:47:54.492Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T07:47:54.492Z",
  "sessionId": "e14e2c22-1d8d-4bf4-953a-e482c1a8d81f"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T07:47:54.528Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：≥3 topologies (含 exposure) 出现方向反转；ASV 框架在所有优先拓扑上均具备单调性+紧性证明；经验数据清晰展示 ASV 的实用价值
核心假设：['mediation 和 collider DAG 在 non-differential K≥3 误分类下均出现方向反转（100k random C 搜索 violation rate ≥30%）', '至少 1 个额外拓扑（M-bias/instrument/front-door）也出现反转', 'ASV 单调性和紧性在 confounding/mediation/collider 三个优先拓扑上均有完整形式化证明', '经验混淆矩阵（3 LLM × 3 task）覆盖足够多样的 C 结构，ASV 排序与实际 bias 严重度一致', 'correction framework 在 ≥93% 场景中推荐最优方法']
关键指标范围：{'reversal_topologies_count': [3, 5], 'mediation_violation_rate': [0.3, 0.85], 'collider_violation_rate': [0.3, 0.85], 'theory_mc_match_rate': [0.95, 1.0], 'asv_coverage_at_95_nominal': [0.93, 0.97], 'asv_sharpness_formal_proofs': [3, 3], 'binarization_max_delta': [0.15, 0.25], 'correction_framework_accuracy': [0.93, 0.98], 'empirical_asv_concordance': [8, 9]}
叙事方向：Version A 完全成立。Lead finding: non-differential multi-class error 在多个 DAG 拓扑中打破经典 toward-null 保证，且反转模式是拓扑依赖的。Taxonomy 揭示了不可化约的 {C structure × topology} 交互效应。三条 claims 无需调整：taxonomy 覆盖广、ASV 有完整理论保证、correction guidance 在几乎所有场景有效。Headline: "the same confusion matrix that is benign in confounding topology produces direction-reversing bias in mediation/collider."


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: causal_annot_error_attrib
focus: Key uncertainty: will mediator/collider DAGs show direction reversal under non-differential multi-class error? Confounding DAG was monotonic in MVP. Also: is ASV framework practically useful enough vs just reporting confusion matrices?

## paper_framing.md

# Paper Framing — causal_annot_error_attrib

## Target Venue
- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)
- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)
- Tertiary: ICWSM 2027 Round 2 (2026-09-15)

## Title
Multi-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies

## Core Claims (3 条)

1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 6 canonical social-science DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door).

2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of differential annotation error needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Reported alongside estimates, analogous to E-values for unmeasured confounding. Formal proofs (monotonicity + sharpness) for 3 priority topologies; MC-validated conjectures for the remaining 3.

3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI, MLA, naive plug-in), characterizing regimes where each applies and where no existing method suffices — including dependence-aware multi-LLM correction as an open problem.

## Story Spine

- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31% of downstream conclusions are already incorrect. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable.

- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.

- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.

- **Headline result template**: "Across 6 DAG topologies with K=3,5,7, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. On 3 CSS tasks annotated by 3 LLMs, ASVs provide calibrated robustness indicators, and our taxonomy identifies cases where commonly applied corrections would increase rather than decrease bias."

## Core Insight (Lead Finding) — DUAL VERSION, gate on plan_001

### Version A (≥1 topology shows direction reversal under K≥3 non-differential exposure misclassification)
The binary guarantee that "non-differential exposure misclassification biases toward the null" (Bross 1954) breaks in the multi-class case. For specific confusion matrix structures in specific DAG topologies, K≥3 non-differential error can amplify or reverse effect estimates. Brenner (1993) identified this possibility for polytomous confounder misclassification ("bias can go in either direction"); we provide the first systematic characterization across 6 DAG topologies with exact conditions for each {C structure × topology} cell. Furthermore, binarizing a K-class variable to "escape" into the binary regime is itself hazardous — collapsing introduces new, direction-unpredictable bias (MVP evidence: Δ up to 0.103).

### Version B (no direction reversal found across topologies)
Multi-class annotation error is structurally irreducible to the binary case: the downstream bias magnitude depends on the full K×K confusion matrix in ways that binary sensitivity/specificity cannot predict, and binarizing a K-class variable introduces new bias (MVP evidence: Δ up to 0.103). While non-differential error preserves bias direction across tested topologies (a useful practitioners' guarantee), the magnitude varies dramatically with confusion matrix structure (0.13–0.30 in confounding DAG alone), and this variation is topology-dependent. ASVs provide the missing robustness measure for this quantitative — not directional — uncertainty.

**Gate**: plan_001 results determine which version. ≥2 topologies with reversal → A; 1 → A with that topology as lead; 0 → B. See D003.

## MVP Evidence

**Confounding DAG + K=3** (confounder misclassification):
- Theoretical bias expressions match MC perfectly (6/6 structures within 95% CI) — framework validated
- Binary collapse ≠ multi-class: Δ up to 0.103 (near-permutation C), proving K=3 retains more confounding control than binarization
- 100k random C search: confounding DAG bias is monotonically toward OVB — this topology is "well-behaved" (predictable direction)
- NOTE: Confounding DAG tests residual confounding, NOT bias-toward-null (Bross 1954). Criterion 2 (away-from-null bias) holds for binary too in this topology. See M001.

**Exposure DAG K=3** (exposure misclassification — D002/D004 CONFIRMED):
- 100k random C: 85% violate bias-toward-null, 83.4% sign reversal, 14.1% amplification
- K=2 control: 6/6 toward null (binary guarantee holds)
- Worst case: β=1.0 → estimate=-0.84 (sign reversal + 2.83x amplification)
- Mechanism: near-permutation C causes label swap → effect direction flips (structurally impossible in K=2)
- **Two-DAG contrast**: confounding (monotonic, predictable) vs exposure (unpredictable, topology-dependent) — validates core claim

## Venue Fit Risks

- **AAAI**: Broad AI audience — emphasize general methodology for "automated annotation measurement error," not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.
- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.
- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.

## Anticipated Reviewer Concerns & Planned Responses

1. **"Trivial extension of binary to multi-class"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 6 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]

2. **"Lee & Wood-Doughty (2024) already did categorical"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 6 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]

3. **"Why these 6 DAG topologies?"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]

4. **"K≥5 expressions aren't actionable"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]

5. **"ASV sharpness only proved for 3 topologies"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]

6. **"Correlated multi-LLM errors?"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]

7. **"Empirical validation scope"** → 3 CSS tasks × 3 LLMs × 3 DAG-relevant scenarios. Tasks selected to cover K=2,3,5 annotation complexity. [Experiments: plan_003, plan_006]


## experiment_plan (with registry status)

- id: plan_001
  claim: 1
  description: Derive and MC-validate bias expressions for 6 DAG topologies with K=3
  priority: P0
  gpu_budget_hours: 0
  deps: []
  registry_id: null
  details: 'For each topology (confounding, mediation, collider, M-bias, instrument,
    front-door): derive closed-form K=3 bias expression, validate with MC (1000 reps
    × N=10000, 6 confusion matrix structures including near-permutation extreme).
    Key question: which topologies show direction reversal under non-differential
    error? Confounding already validated in MVP (no reversal, monotonic toward OVB).

    '
  status: planned
- id: plan_002
  claim: 1
  description: Extend bias expressions to K=5,7 — matrix notation + interpretability
    tools
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  details: 'Matrix-form expressions for general K. Three interpretability tools: (a)
    eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar
    bounds collapsing matrix to conservative scalar, (c) diagnostic visualizations
    mapping confusion matrix regions to bias magnitude. Validate on confounding +
    mediation + collider DAGs with K=5,7.

    '
  status: planned
- id: plan_003
  claim: 1
  description: 'Empirical confusion matrices: 3 LLMs × 3 CSS tasks vs gold-standard'
  priority: P0
  gpu_budget_hours: 0
  api_cost_estimate: $300-550
  deps: []
  details: 'Tasks: protest event coding (K=5, ACLED/GPT-RE), stance detection (K=3,
    SemEval/VAST), toxicity (K=2, as special case / consistency check, Civil Comments).
    Models: Llama 4 Maverick (Together.ai), Qwen 3.5 Plus (OpenRouter), DeepSeek V4
    (DeepSeek API). ~30K annotations per model × 3 datasets × 3 prompt variants. Output:
    empirical confusion matrices, inter-model correlation analysis, downstream regression
    bias vs gold-standard baseline.

    '
  status: planned
- id: plan_008
  claim: 1
  description: 'Binarization collapse analysis: K→2 folding bias across all 6 topologies'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  details: 'For each of 6 topologies with K=3,5,7: collapse to binary, compare bias
    from full multi-class expression vs binarized expression. Demonstrate that binarization
    is not a safe shortcut — can amplify or reverse bias. MVP showed Δ up to 0.089
    for confounding DAG K=3.

    '
  status: planned
- id: plan_004
  claim: 2
  description: 'ASV framework: formal proofs for confounding, mediation, collider'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  details: 'Derive ASV expressions for 3 priority topologies. Formal proofs of: (a)
    monotonicity (ASV increases with δ amplification), (b) sharpness (bound is achievable
    for some confusion matrix). MC validation: coverage at 90%, 95%, 99% levels across
    1000 scenarios.

    '
  status: planned
- id: plan_005
  claim: 2
  description: ASV MC validation for M-bias, instrument, front-door topologies
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_004
  details: 'ASV expressions + MC validation of monotonicity and coverage. Sharpness
    stated as conjectures supported by numerical evidence. If any topology fails monotonicity
    under MC, flag and investigate.

    '
  status: planned
- id: plan_006
  claim: 2
  description: ASV calibration on empirical data (3 CSS tasks × 3 LLMs)
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_003
  - plan_004
  details: 'Apply ASVs to empirical confusion matrices from plan_003. Validate coverage
    on held-out gold-standard splits. Report ASV alongside downstream effect estimates
    for each task. Compare ASV interpretability with raw confusion matrix reporting.

    '
  status: planned
- id: plan_007
  claim: 3
  description: 'Correction guidance framework: decision mapping + validation'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  - plan_004
  - plan_003
  details: 'Decision framework: {topology × error structure × ASV} → correction method
    (DSL / PPI / MLA / naive plug-in / "no existing method adequate"). MC validation:
    recommended method produces least bias in ≥90% of scenarios. Empirical validation
    on plan_003 data. Characterize regimes where no existing method suffices (correlated
    errors, differential multi-class, etc.) — identify as open problems.

    '
  status: planned
- id: plan_009
  claim: 1
  description: Pathological confusion matrix analysis (near-permutation, rank-deficient)
  priority: P2
  gpu_budget_hours: 0
  deps:
  - plan_001
  details: 'Extreme C structures: near-permutation, rank-deficient, block-diagonal.
    Characterize when bias becomes catastrophic across topologies. Identify structural
    conditions (spectral gap, diagonal dominance ratio) that predict bias severity
    — candidate features for practitioners.

    '
  status: planned
- id: plan_010
  claim:
  - 1
  - 2
  - 3
  description: annot-sensitivity Python toolkit (open-source release)
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  - plan_004
  - plan_007
  details: 'Package: user-specified DAG + confusion matrix(es) + downstream estimate
    → bias expressions (scalar K≤3, matrix K>3 with interpretability) + ASV bounds
    + sensitivity curves + correction recommendation + diagnostic plots. pip-installable,
    with worked examples for each topology.

    '
  status: planned


## registry (completed experiments)

- exp_id: mvp_confounding_dag
  name: ''
  status: DONE
  conclusion: success
  metrics:
    theory_mc_match: 6/6
    pass_criteria: 3/3
    max_binary_collapse_delta: 0.103
    bias_range: 0.132-0.298
    ovb_reference: 0.3
    direction_reversal_found: false
    random_search_100k_min_bias: 0.063
- exp_id: mvp_exposure_dag
  name: ''
  status: DONE
  conclusion: success
  metrics:
    theory_mc_match: 5/5
    pass_criteria: 3/3
    violation_rate: 0.85
    sign_reversal_rate: 0.834
    amplification_rate: 0.141
    K2_toward_null: 6/6
    worst_severity: 2.83
    named_structures_with_violation: 3/6

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
  "promptId": "5754135b-cb0e-474d-aabe-01be4600dd6f",
  "type": "user",
  "uuid": "5ded975f-5e57-4a96-bda8-2a0bc466f6c1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e14e2c22-1d8d-4bf4-953a-e482c1a8d81f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T07:47:54.527Z_

```json
{
  "parentUuid": "5ded975f-5e57-4a96-bda8-2a0bc466f6c1",
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
  "uuid": "a4a50d93-1ecb-4809-8ed7-9e53789bf2ab",
  "timestamp": "2026-05-20T07:47:54.527Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e14e2c22-1d8d-4bf4-953a-e482c1a8d81f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T07:47:54.527Z_

```json
{
  "parentUuid": "a4a50d93-1ecb-4809-8ed7-9e53789bf2ab",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6d9169ab-f938-4956-af7e-09d59b162cca",
  "timestamp": "2026-05-20T07:47:54.527Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e14e2c22-1d8d-4bf4-953a-e482c1a8d81f",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：≥3 topologies (含 exposure) 出现方向反转；ASV 框架在所有优先拓扑上均具备单调性+紧性证明；经验数据清晰展示 ASV 的实用价值 核心假设：['mediation 和 collider DAG 在 non-differential K≥3 误分类下均出现方向反转（100k rand…",
  "leafUuid": "6d9169ab-f938-4956-af7e-09d59b162cca",
  "sessionId": "e14e2c22-1d8d-4bf4-953a-e482c1a8d81f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-class annotation error direction reversal across DAG topologies",
  "sessionId": "e14e2c22-1d8d-4bf4-953a-e482c1a8d81f"
}
```

---

### Assistant

_source line 8 · 2026-05-20T07:49:12.631Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment data for all planned experiments in the experiment plan, under the "best" tier definition. Each prediction must include a result_rationale explaining why this result occurs under the best tier.

Let me carefully go through each planned experiment and generate detailed predictions consistent with the best tier constraints:

**Best tier definition:**
- ≥3 topologies (including exposure) show direction reversal
- ASV framework has monotonicity + sharpness proofs on all priority topologies
- Empirical data clearly demonstrates ASV practical value
- Key metric ranges provided

Let me work through each experiment:


For plan_001, I need to ensure at least three topologies show reversal including exposure. Since the MVP already demonstrates exposure with 83.4% sign reversal, I need mediation and collider to both exhibit reversal as well, plus one additional topology from M-bias, instrument, or front-door. The violation rates for mediation and collider should fall in the [0.3, 0.85] range to show meaningful reversal patterns, while the theory-MC match rate needs to be very high at [0.95, 1.0] to validate the bias expressions.

For K=5 and K=7, I'm extending the matrix notation approach with eigendecomposition to capture the dominant bias modes and show the method scales effectively. Then I'll gather confusion matrices from three different LLMs across three CSS tasks to ensure diverse causal structures for validation. The formal proofs for confounding, mediation, and collider need to be complete, with ASV coverage at the 95% nominal level reaching [0.93, 0.97]. After validating the remaining three topologies through MC simulation, I'll calibrate the ASV method on empirical data, aiming for [8, 9] out of 9 concordance. Finally, I'm building a correction guidance framework that achieves [0.93, 0.98] accuracy, and the thinking cuts off mid-plan.

Now I'm continuing with the binarization collapse analysis where the maximum delta should fall between [0.15, 0.25], followed by pathological confusion matrix analysis and the Python toolkit. For the YAML output, I need to determine which topologies show reversal in the best tier—exposure is already confirmed with a violation rate of 0.85, and mediation, collider, front-door, and possibly M-bias should all demonstrate reversals since misclassification in these structures can distort indirect effects or create spurious associations.

Looking at the reversal topology count metrics, I'm aiming for 4 topologies to fall within the [3, 5] range for the best tier. For mediation, when the mediator gets misclassified with K≥3, the indirect effect gets distorted because the misclassified version no longer properly decomposes the total effect—near-permutation confusion can flip the M→Y gradient and reverse the indirect effect sign, which is structurally impossible with binary misclassification since that just attenuates toward null. For colliders, conditioning on a misclassified collider opens a spurious path, and with K≥3 the misclassification can reverse the sign of the spurious association, not just create it.

With front-door, the criterion requires correctly identifying the mediating pathway, so K≥3 misclassification distorts both adjustment steps and near-permutation confusion can flip the second-stage regression sign. Confounding remains monotonic toward bias with no reversal possible. For instruments, the exclusion restriction holds under non-differential error on Z, but the Wald ratio's numerator and denominator respond differently to misclassification with K≥3, potentially flipping the ratio's sign—though I should verify this holds for the best tier classification.

Actually, reconsidering the reversals: confounding definitely doesn't reverse, exposure and mediation both do, collider reversal is plausible since misclassification changes which spurious paths open, and M-bias also shows reversal. For the best tier, I'm settling on four topologies that reverse: exposure, mediation, collider, and M-bias, while keeping confounding and instrument as non-reversing cases to stay realistic. So I'm mapping out which topologies show sign reversals when variables get misclassified — exposure, mediation, collider, and front-door all demonstrate this, while confounding, M-bias, and instrument don't. The plan covers six canonical DAG topologies from the paper, with exposure handled separately in the MVP, and I'm tracking which misclassification scenarios (confounder, mediator, collider, exposure, etc.) produce reversals across this framework. Looking at the core assumption requirements, I need mediation and collider to both show reversals with violation rates ≥30%, plus at least one more topology from the M-bias/instrument/front-door group. Setting exposure, mediation, collider, and front-door as my four topologies with reversals keeps me within the target range.

Now I'm working through the detailed predictions for each of the six topologies in plan_001, starting with confounding which should show no reversal and monotonic movement toward the OVB direction based on theory.

For mediation, the key insight is that when the mediator M gets misclassified into M̃, the indirect pathway X→M→Y gets distorted. With K≥3 categories and near-permutation error matrices, adjacent categories can swap in ways that flip the sign of the M→Y relationship, reversing the indirect effect even though the total effect stays stable. This creates a violation rate around 0.52, well within the acceptable range.

For the collider scenario, conditioning on the misclassified collider C̃ opens up a spurious path between X and Y. With K≥3 misclassification, different category conflations produce different conditioning effects, changing the magnitude and nature of the spurious association—violation rate approximately 0.45.

The M-bias structure is trickier since misclassification could push the estimate in either direction, so I'm expecting significant magnitude variation without necessarily reversing the sign. For the instrumental variable case, both the numerator and denominator of the Wald estimator get attenuated when Z is misclassified.

To hit the reversal_topologies_count target of 3-5 with mediation and collider already selected, I need to add front-door adjustment as the third topology. Front-door misclassification distorts both adjustment stages asymmetrically, which can produce sign reversal. Now I'm working through the precise numerical values for each metric to construct the YAML output. Now I'm looking at the remaining validation plans. Plans 002 through 005 focus on eigendecomposition capturing most of the bias variance with just two eigenvalues, worst-case bounds staying within 15% of true values, LLM confusion matrices across three models and tasks, and formal ASV proofs for priority topologies with proper coverage calibration. Plans 006 through 008 show the framework applied to empirical data achieving 8/9 concordance, a correction approach reaching 0.95 accuracy, and binarization effects staying under 0.19 delta.

For the final plans, I'm analyzing pathological cases across all six topologies where spectral gap predicts bias severity, then releasing the complete toolkit. Before writing the YAML, I need to finalize the metric ranges—using 4 for reversal topologies and 0.52 for mediation violation rate—and carefully articulate the core narrative: Version A's non-differential multi-class errors break toward-null guarantees in topology-dependent ways.

Writing the comprehensive YAML block...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d9169ab-f938-4956-af7e-09d59b162cca",
  "isSidechain": false,
  "requestId": "req_011CbDTAvw1uNeUWBMu1VxK3",
  "type": "assistant",
  "uuid": "60d2c78c-068b-4885-8f81-7769c34d221a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e14e2c22-1d8d-4bf4-953a-e482c1a8d81f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Es5cUJmup5FaK1z32w3u2X",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10666,
      "cache_read_input_tokens": 11841,
      "output_tokens": 21825,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10666,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 21825,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10666
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

_source line 9 · 2026-05-20T07:57:20.114Z_

```yaml
tier: best
narrative_guidance: >
  Version A 完全成立。Lead finding: non-differential K≥3 误分类在 4 个 DAG 拓扑（exposure, mediation, collider, front-door）中打破经典 toward-null 保证，
  而 confounding 和 instrument 保持单调性。反转模式严格拓扑依赖——同一混淆矩阵在 confounding DAG 中仅引起可预测的残差偏倚，在 mediation/collider DAG 中却产生方向反转。
  Headline: "the same confusion matrix that is benign in confounding topology produces direction-reversing bias in mediation and collider topologies."
  ASV 框架在三个优先拓扑上均有完整单调性+紧性形式化证明，经验校准良好。Correction framework 在 95% 场景推荐最优方法。
  Binarization collapse 分析强化了核心论点：K→2 折叠最大额外偏倚达 Δ=0.19，证明 binarization 不是安全退路。

imagined_experiments:
  - name: "Multi-topology bias derivation and MC validation (K=3)"
    plan_id: "plan_001"
    description: >
      对 6 个 DAG 拓扑（confounding, mediation, collider, M-bias, instrument, front-door）推导 K=3 闭式偏倚表达式，
      每个拓扑用 6 种混淆矩阵结构 × 1000 MC reps × N=10000 验证。另对 mediation/collider/front-door/M-bias/instrument
      执行 100k random C 搜索，检测方向反转违背率。
    expected_results:
      theory_mc_match_rate: 0.972
      theory_mc_match_detail: "35/36 structure×topology 组合落入 95% MC CI；1 个边界 case（front-door + rank-deficient C）偏差 0.003 超 CI 上界，增加到 N=50000 后收敛"
      reversal_topologies_count: 4
      reversal_topologies: ["exposure (MVP)", "mediation", "collider", "front-door"]
      non_reversal_topologies: ["confounding", "instrument"]
      mediation_violation_rate: 0.52
      mediation_sign_reversal_rate: 0.47
      mediation_amplification_rate: 0.11
      collider_violation_rate: 0.41
      collider_sign_reversal_rate: 0.36
      collider_amplification_rate: 0.09
      frontdoor_violation_rate: 0.34
      frontdoor_sign_reversal_rate: 0.28
      frontdoor_amplification_rate: 0.12
      mbias_violation_rate: 0.0
      mbias_bias_range: [0.04, 0.18]
      instrument_violation_rate: 0.0
      instrument_bias_range: [0.02, 0.14]
      confounding_violation_rate: 0.0
      confounding_bias_range: [0.063, 0.298]
      mediation_worst_case: "β_indirect=0.5 → estimate=-0.31 (sign reversal, 1.62x amplification)"
      collider_worst_case: "β_XY=0.0 (null) → estimate=0.44 (spurious effect creation + direction assignment)"
      frontdoor_worst_case: "β_total=0.8 → estimate=-0.22 (sign reversal via second-stage distortion)"
    result_rationale: >
      Mediation (violation rate 0.52): 间接效应 = β_XM × β_MY|X。K≥3 非差异误分类扭曲 M→Y|X 回归系数——
      近置换矩阵 C 使相邻类别标签互换，导致 β_MY|X 符号翻转，从而间接效应反转。K=2 下非差异误分类只能将 β_MY|X 
      向零压缩（attenuation），结构上不可能越过零点。violation rate 0.52 而非更高（对比 exposure 的 0.85），
      因为间接效应经过两步回归（X→M 和 M→Y|X），仅当 C 同时严重扰动 M 的条件分布时才出现反转，
      而 exposure 误分类直接作用于处理变量，单步即可反转。

      Collider (violation rate 0.41): 对 collider C̃ 条件化打开伪路径 X←U→C←V→Y。K≥3 误分类改变条件化的
      有效权重——不同类别的合并创造不同的伪关联模式。violation rate 低于 mediation 因为反转需要 C 矩阵
      使 X-path 和 Y-path 的贡献权重同时满足特定比例条件，约束更强。

      Front-door (violation rate 0.34): 前门调整涉及两阶段估计（X→M 和 M→Y|do(X)）。K≥3 误分类不对称地
      扭曲两个阶段——第一阶段 attenuation 与第二阶段 distortion 的交互可使整体估计翻转。violation rate 
      最低因为反转需要两阶段同时被 C 严重扰动且扰动方向"配合"，是三个反转拓扑中约束最强的。

      Confounding (violation rate 0.0): 已由 MVP 确认。残差混淆始终朝向 OVB 方向，因为误分类只能减少
      confounder 的解释力（信息丢失），不能创造新的混淆结构。K≥3 增加了更多丢失信息的方式但不改变方向性。

      Instrument (violation rate 0.0): Wald estimator = Cov(Y,Z̃)/Cov(X,Z̃)。非差异误分类对 Z 的两个
      协方差施加相同方向的 attenuation（均乘以 C 的特征值相关因子），比值的符号不变。
      K≥3 下分子分母的 attenuation 系数不再相同（不同特征值），导致幅度偏倚但符号保持。

      M-bias (violation rate 0.0): M-bias（蝴蝶 DAG）中被误分类的变量本不应被条件化。
      误分类使条件化效应减弱（信息丢失方向），偏倚幅度变化但不反转。
    tables:
      - name: "Table 1: Topology × Reversal Summary"
        columns: ["Topology", "Role of Annotated Variable", "Violation Rate (100k)", "Sign Reversal Rate", "Amplification Rate", "Worst-Case Severity", "K=2 Control"]
        rows:
          - ["Confounding", "Confounder", "0.000", "0.000", "0.000", "0.298 (toward OVB)", "toward OVB ✓"]
          - ["Exposure (MVP)", "Treatment", "0.850", "0.834", "0.141", "2.83x amplification", "toward null ✓"]
          - ["Mediation", "Mediator", "0.520", "0.470", "0.110", "1.62x + sign reversal", "toward null ✓"]
          - ["Collider", "Collider", "0.410", "0.360", "0.090", "spurious 0.44 from null", "attenuated ✓"]
          - ["M-bias", "M-bias variable", "0.000", "0.000", "0.000", "0.18 (attenuated)", "attenuated ✓"]
          - ["Instrument", "Instrument", "0.000", "0.000", "0.000", "ratio distortion 0.14", "attenuated ✓"]
          - ["Front-door", "Front-door variable", "0.340", "0.280", "0.120", "sign reversal", "toward null ✓"]
      - name: "Table 2: Theory-MC Match per Topology × C Structure"
        columns: ["Topology", "Diagonal-dominant", "Moderate off-diag", "Uniform off-diag", "Block-diagonal", "Near-permutation", "Rank-deficient", "Match Rate"]
        rows:
          - ["Confounding", "✓", "✓", "✓", "✓", "✓", "✓", "6/6"]
          - ["Mediation", "✓", "✓", "✓", "✓", "✓", "✓", "6/6"]
          - ["Collider", "✓", "✓", "✓", "✓", "✓", "✓", "6/6"]
          - ["M-bias", "✓", "✓", "✓", "✓", "✓", "✓", "6/6"]
          - ["Instrument", "✓", "✓", "✓", "✓", "✓", "✓", "6/6"]
          - ["Front-door", "✓", "✓", "✓", "✓", "✓", "△*", "5/6"]
    figures_description:
      - "Fig 1: 6-panel heatmap (one per topology), x=true effect size, y=confusion matrix diagonal dominance ratio, color=bias magnitude with sign (blue=toward null, red=away/reversal). 清晰展示 mediation/collider/front-door 的红色反转区域 vs confounding/instrument/M-bias 的全蓝区域。"
      - "Fig 2: Violin plots of 100k random C bias distribution per topology. Mediation/collider/front-door 分布跨越零线；confounding/instrument/M-bias 分布完全在一侧。"
      - "Fig 3: K=2 vs K=3 对比散点图（per topology）。所有 K=2 点落在 toward-null 区域，K=3 点在 mediation/collider/front-door 中散布到反转区域。"
    analysis: >
      核心发现：非差异 K≥3 误分类的方向反转是拓扑依赖的。6 个拓扑分为两类：(1) 信息丢失型（confounding, instrument, M-bias）——
      误分类只能减少变量的信息量，偏倚方向可预测；(2) 结构扭曲型（exposure, mediation, collider, front-door）——
      误分类改变变量在 DAG 中的功能角色（如 mediator 的类别标签互换等价于改变 M→Y 的函数形式），
      导致不可预测的方向反转。这一二分法是论文的核心理论贡献。Confounding DAG 的"良性"行为不可推广到其他拓扑，
      这直接挑战了实践者"non-differential error is conservative"的默认假设。

  - name: "General K bias expressions with interpretability tools (K=5,7)"
    plan_id: "plan_002"
    description: >
      将偏倚表达式推广到矩阵形式（一般 K）。开发三种可解释性工具：(a) 特征分解摘要，(b) 最坏情况标量界，
      (c) 诊断可视化。在 confounding + mediation + collider DAG 上用 K=5,7 验证。
    expected_results:
      eigendecomposition_variance_captured_top2: 0.87
      eigendecomposition_variance_captured_top3: 0.96
      worstcase_bound_tightness: 0.88
      worstcase_bound_tightness_detail: "最坏情况标量界在 88% 的场景中与真实最坏情况偏差 <15%"
      K5_mediation_violation_rate: 0.61
      K5_collider_violation_rate: 0.49
      K7_mediation_violation_rate: 0.68
      K7_collider_violation_rate: 0.55
      K5_confounding_reversal: false
      K7_confounding_reversal: false
      theory_mc_match_K5: "17/18 within 95% CI"
      theory_mc_match_K7: "16/18 within 95% CI"
    result_rationale: >
      K 增大时 violation rate 单调上升（mediation: 0.52→0.61→0.68；collider: 0.41→0.49→0.55），
      因为混淆矩阵的自由参数从 K=3 的 6 个增长到 K=5 的 20 个、K=7 的 42 个。
      更高维度的 C 矩阵有更多"方向"可以扭曲类别映射，使得 random search 中遇到反转配置的概率增加。
      
      特征分解 top-2 捕获 87% 方差：偏倚矩阵 B = f(C) 的谱结构由 C 的谱结构决定。
      C 通常是行随机矩阵（行和为 1），其最大特征值为 1（对应"保真"模式），第二大特征值
      对应主要误分类模式。因此 B 的前 2 个特征值对应"无偏"基线和"主误分类方向"，
      合计解释大部分方差。top-3 达 96% 因为第三个模式捕获了次要误分类模式。
      
      最坏情况标量界紧度 88%：该界通过对 B 的谱范数取上界得到，对于高对角优势 C 
      这个界很紧（谱范数 ≈ 最大特征值），但对于结构化偏差（如 block-diagonal C）
      谱范数高估约 25-30%，拉低了整体紧度。
      
      Theory-MC match 在 K=7 时略降（16/18 vs K=3 的 35/36）：高维 MC 模拟的方差增大，
      需要更大 N 才能达到同样精度。2 个未匹配 case 均为 near-permutation extreme，
      增加到 N=50000 后收敛。
    tables:
      - name: "Table 3: Violation Rate Scaling with K"
        columns: ["Topology", "K=3", "K=5", "K=7", "Trend"]
        rows:
          - ["Confounding", "0.000", "0.000", "0.000", "Stable at 0 (monotonic toward OVB)"]
          - ["Mediation", "0.520", "0.610", "0.680", "Monotonically increasing"]
          - ["Collider", "0.410", "0.490", "0.550", "Monotonically increasing"]
      - name: "Table 4: Eigendecomposition Variance Explained"
        columns: ["Topology", "K", "Top-1 EV%", "Top-2 EV%", "Top-3 EV%"]
        rows:
          - ["Confounding", "5", "72%", "89%", "97%"]
          - ["Confounding", "7", "68%", "85%", "95%"]
          - ["Mediation", "5", "70%", "87%", "96%"]
          - ["Mediation", "7", "65%", "84%", "94%"]
          - ["Collider", "5", "71%", "88%", "96%"]
          - ["Collider", "7", "66%", "85%", "95%"]
    figures_description:
      - "Fig 4: Bias matrix eigenspectrum plots (K=5,7) per topology，展示前 3 个特征值占主导地位，剩余特征值快速衰减。"
      - "Fig 5: Worst-case bound vs true worst-case scatter plot，color by C structure type。Block-diagonal 点偏离对角线最远，diagonal-dominant 点最接近。"
      - "Fig 6: Diagnostic heatmap——K=5 confusion matrix region → bias magnitude，用户可直接定位其实证 C 落在哪个 bias regime。"
    analysis: >
      K 增大强化了核心论点：随着分类粒度增加，binary 近似的失效更严重，方向反转概率上升。
      可解释性工具使 K≥5 的矩阵偏倚表达式在实践中可用：研究者无需理解完整 K×K 偏倚矩阵，
      只需检查 top-2 特征模式即可判断偏倚的方向和严重程度。最坏情况标量界为风险厌恶型研究者
      提供保守但可操作的单一数字。

  - name: "Empirical confusion matrices: 3 LLMs × 3 CSS tasks"
    plan_id: "plan_003"
    description: >
      收集 3 个 LLM（Llama 4 Maverick, Qwen 3.5 Plus, DeepSeek V4）在 3 个 CSS 任务
      （protest event coding K=5, stance detection K=3, toxicity K=2）上的实证混淆矩阵。
      ~30K annotations per model × 3 datasets × 3 prompt variants。
    expected_results:
      total_annotations: "~270K (3 models × 3 tasks × ~30K)"
      protest_K5_avg_diagonal_dominance: 0.62
      protest_K5_inter_model_kappa: 0.71
      stance_K3_avg_diagonal_dominance: 0.74
      stance_K3_inter_model_kappa: 0.68
      toxicity_K2_avg_accuracy: 0.89
      toxicity_K2_inter_model_kappa: 0.76
      cross_model_error_correlation: 0.58
      cross_model_error_correlation_detail: "当两个模型均出错时，58% 的 case 错向同一类别（与 Kim et al. 的 60% 一致）"
      distinct_C_structures_observed: 9
      near_permutation_cases: 2
      block_diagonal_cases: 3
      prompt_variant_C_shift: "prompt 变体导致 C 结构在 Frobenius 距离上变化 0.04-0.12"
      downstream_bias_vs_gold_protest: [-0.08, 0.15]
      downstream_bias_vs_gold_stance: [-0.05, 0.09]
      downstream_bias_vs_gold_toxicity: [-0.02, 0.03]
    result_rationale: >
      Protest event coding (K=5) 对角优势最低（0.62）：5 类任务（peaceful protest, violent protest, 
      strategic development, government response, other）存在固有歧义——"strategic development"与 
      "peaceful protest"常被混淆，LLM 倾向于对 borderline case 系统性偏向高频类别。
      低对角优势意味着 C 矩阵偏离对角，更接近 random search 中产生反转的区域。
      
      Stance detection (K=3) 对角优势较高（0.74）：3 类（favor, against, neutral）语义距离较大，
      但 neutral 与 against 的边界模糊导致特定 off-diagonal 元素偏高，形成 block-diagonal 结构
      （favor 与 against/neutral 分离，但 against-neutral 互相混淆）。
      
      Toxicity (K=2) 准确率最高（0.89）：二分类任务较简单，且 toxicity 有较清晰的语言标记。
      作为 binary special case / consistency check——K=2 下所有模型的偏倚均 toward null，
      与理论预测一致。
      
      跨模型错误相关 0.58：Kim et al. (ICML 2025) 报告 60%，我们的 0.58 高度一致。
      这不是巧合——LLM 共享类似的预训练数据和推理模式，对同类歧义样本倾向于犯同类错误。
      这个发现强化了我们的论点：多模型集成无法消除系统性偏倚，必须分析 C 结构。
      
      9 种不同 C 结构（3 models × 3 tasks）为后续 ASV 校准提供了充分多样性。
      2 个 near-permutation cases 出现在 protest coding 的特定 prompt 变体下（过度指令化导致
      类别定义混乱），3 个 block-diagonal cases 出现在 stance detection 中（favor 孤立）。
    tables:
      - name: "Table 5: Empirical Confusion Matrix Summary"
        columns: ["Task", "K", "Model", "Accuracy", "Diagonal Dominance", "Largest Off-Diag", "C Structure Type"]
        rows:
          - ["Protest", "5", "Llama 4 Maverick", "0.64", "0.60", "0.18 (strat_dev→peaceful)", "Moderate off-diag"]
          - ["Protest", "5", "Qwen 3.5 Plus", "0.60", "0.57", "0.21 (strat_dev→peaceful)", "Near-permutation"]
          - ["Protest", "5", "DeepSeek V4", "0.67", "0.63", "0.15 (other→gov_resp)", "Block-diagonal"]
          - ["Stance", "3", "Llama 4 Maverick", "0.77", "0.76", "0.14 (neutral→against)", "Block-diagonal"]
          - ["Stance", "3", "Qwen 3.5 Plus", "0.73", "0.72", "0.16 (against→neutral)", "Block-diagonal"]
          - ["Stance", "3", "DeepSeek V4", "0.76", "0.75", "0.13 (neutral→against)", "Block-diagonal"]
          - ["Toxicity", "2", "Llama 4 Maverick", "0.91", "0.91", "0.09 (toxic→non-toxic)", "Diagonal-dominant"]
          - ["Toxicity", "2", "Qwen 3.5 Plus", "0.87", "0.87", "0.13 (non-toxic→toxic)", "Diagonal-dominant"]
          - ["Toxicity", "2", "DeepSeek V4", "0.90", "0.90", "0.10 (toxic→non-toxic)", "Diagonal-dominant"]
      - name: "Table 6: Inter-Model Error Agreement"
        columns: ["Task", "Model Pair", "Cohen's κ", "Error Agreement Rate", "Same-Direction Error %"]
        rows:
          - ["Protest", "Llama-Qwen", "0.69", "0.24", "0.61"]
          - ["Protest", "Llama-DeepSeek", "0.72", "0.21", "0.57"]
          - ["Protest", "Qwen-DeepSeek", "0.68", "0.25", "0.56"]
          - ["Stance", "Llama-Qwen", "0.67", "0.18", "0.59"]
          - ["Stance", "Llama-DeepSeek", "0.70", "0.16", "0.58"]
          - ["Stance", "Qwen-DeepSeek", "0.66", "0.19", "0.57"]
          - ["Toxicity", "All pairs avg", "0.76", "0.09", "0.62"]
    figures_description:
      - "Fig 7: 9 个实证混淆矩阵热力图（3×3 grid: rows=models, cols=tasks）。Protest 列明显更'散'（低对角优势），toxicity 列高度集中在对角。"
      - "Fig 8: PCA projection of 9 confusion matrices onto theoretical C structure space，标注每个矩阵落在 random search 偏倚分布的哪个区域。"
    analysis: >
      实证 C 矩阵覆盖了理论分析中的多种结构类型（diagonal-dominant, block-diagonal, near-permutation），
      为后续 ASV 校准和 correction framework 验证提供了现实基础。关键观察：
      (1) Protest coding 的 C 矩阵接近 plan_001 中产生反转的区域，预示该任务在 mediation/collider 
      拓扑下风险最高；(2) 跨模型错误高度相关，确认多 LLM 集成不是解决方案；
      (3) Prompt 变体可显著移动 C 结构（Frobenius Δ 达 0.12），暗示 prompt engineering 
      本身是一种（未被充分认识的）bias intervention。

  - name: "Binarization collapse analysis across all topologies"
    plan_id: "plan_008"
    description: >
      对 6 个拓扑 + exposure（共 7 个拓扑），K=3,5,7 条件下，将 K 类变量折叠为二分类，
      比较完整多类偏倚表达式 vs 二值化后偏倚表达式的差异 Δ。
    expected_results:
      binarization_max_delta: 0.19
      binarization_max_delta_topology: "mediation"
      binarization_max_delta_K: 7
      binarization_avg_delta_K3: 0.08
      binarization_avg_delta_K5: 0.13
      binarization_avg_delta_K7: 0.16
      binarization_direction_reversal_cases: "12% of K=5,7 scenarios show Δ that flips bias direction"
      binarization_delta_by_topology:
        confounding_K3: 0.06
        confounding_K5: 0.09
        confounding_K7: 0.11
        mediation_K3: 0.10
        mediation_K5: 0.15
        mediation_K7: 0.19
        collider_K3: 0.09
        collider_K5: 0.14
        collider_K7: 0.17
        exposure_K3: 0.08
        exposure_K5: 0.12
        exposure_K7: 0.15
        mbias_K3: 0.05
        mbias_K5: 0.08
        mbias_K7: 0.10
        instrument_K3: 0.04
        instrument_K5: 0.07
        instrument_K7: 0.09
        frontdoor_K3: 0.09
        frontdoor_K5: 0.13
        frontdoor_K7: 0.16
    result_rationale: >
      Binarization max Δ = 0.19（mediation, K=7）：折叠 7 类 mediator 为二分类丢弃了类别间的
      细粒度偏倚结构。Mediation DAG 中间接效应依赖 M 的分布形状——当 7 个类别被折叠为 2 个时，
      被合并的类别可能具有相反方向的 M→Y 效应，导致折叠后的间接效应与原始间接效应方向相反。
      K=7 比 K=3 更严重因为折叠时信息丢失更多（5 个类别被合并 vs 1 个类别被合并）。
      
      Δ 随 K 单调增大（avg: 0.08→0.13→0.16）：这是信息论上的必然——K→2 折叠的信息丢失
      量为 log(K)-log(2)，K 越大丢失越多。
      
      12% 的 K=5,7 场景中 Δ 本身导致方向翻转：这意味着研究者试图通过 binarization 
      "逃入"二分类安全区域的策略不仅无效（因为折叠引入新偏倚），而且在 12% 的场景中
      反而比保留多类更危险。这个发现直接回应了一个预期的 reviewer concern：
      "既然 binary case 有保证，为什么不直接 binarize？"
      
      Mediation > Collider > Front-door > Exposure > Confounding > M-bias > Instrument 的 Δ 排序：
      Mediation 最大因为间接效应的非线性依赖 M 的类别分布；Instrument 最小因为 IV 估计
      主要依赖 Z 的第一阶段 F-statistic，对类别合并方式的敏感度较低。
    tables:
      - name: "Table 7: Binarization Collapse Δ by Topology × K"
        columns: ["Topology", "K=3 Δ", "K=5 Δ", "K=7 Δ", "Max Δ", "Direction Reversal by Δ?"]
        rows:
          - ["Confounding", "0.06", "0.09", "0.11", "0.11", "No"]
          - ["Exposure", "0.08", "0.12", "0.15", "0.15", "Yes (3% of K=7)"]
          - ["Mediation", "0.10", "0.15", "0.19", "0.19", "Yes (18% of K=7)"]
          - ["Collider", "0.09", "0.14", "0.17", "0.17", "Yes (14% of K=7)"]
          - ["M-bias", "0.05", "0.08", "0.10", "0.10", "No"]
          - ["Instrument", "0.04", "0.07", "0.09", "0.09", "No"]
          - ["Front-door", "0.09", "0.13", "0.16", "0.16", "Yes (11% of K=7)"]
    figures_description:
      - "Fig 9: Δ vs K 折线图（7 条线 = 7 拓扑），清晰展示 Δ 随 K 单调增长且拓扑间差异系统性存在。"
      - "Fig 10: Scatter plot of multi-class bias vs binarized bias per topology，对角线 = 无折叠偏倚。偏离对角线的点即 Δ ≠ 0，红点 = 方向翻转 case。"
    analysis: >
      Binarization 不是安全退路。Max Δ = 0.19 在实际社会科学研究中足以改变实质性结论
      （典型效应量 0.1-0.3）。这一结果与 MVP 中 confounding DAG 的 Δ=0.103 一致且推广：
      更多拓扑、更高 K 值下 Δ 更大。结合 plan_001 的方向反转结果，完整论点是：
      (1) 保留多类可能导致方向反转，(2) 折叠为二类也不安全——研究者无处可逃，必须使用 ASV 框架
      诊断其具体 {C × topology} 组合的偏倚性质。

  - name: "ASV formal proofs for 3 priority topologies"
    plan_id: "plan_004"
    description: >
      推导 confounding, mediation, collider 三个优先拓扑的 ASV 表达式。
      形式化证明单调性（ASV 随 δ 增大而增大）和紧性（bound 可被某个 C 达到）。
      MC 验证：1000 scenarios × coverage at 90%, 95%, 99% levels。
    expected_results:
      asv_sharpness_formal_proofs: 3
      asv_monotonicity_proofs: 3
      proof_technique_confounding: "algebraic — closed-form ASV as function of spectral gap of C and δ"
      proof_technique_mediation: "algebraic + envelope theorem — indirect effect ASV via product-of-coefficients decomposition"
      proof_technique_collider: "algebraic + Lagrangian optimization — ASV as constrained optimization over C perturbation space"
      asv_coverage_90_nominal: 0.912
      asv_coverage_95_nominal: 0.952
      asv_coverage_99_nominal: 0.988
      asv_coverage_by_topology:
        confounding_95: 0.958
        mediation_95: 0.949
        collider_95: 0.948
      mc_scenarios: 1000
      mc_reps_per_scenario: 500
      sharpness_achieving_C_found: "100% of scenarios — constructive proof provides explicit C* achieving bound"
    result_rationale: >
      三个证明均成功（asv_sharpness_formal_proofs = 3）：这是 best tier 的硬性要求，但也是
      数学上可行的，因为三个拓扑的偏倚表达式在 K=3 时有足够简洁的闭式形式。
      
      Confounding ASV：残差混淆偏倚 = OVB × (1 - f(C))，其中 f(C) 是 C 的对角优势函数。
      ASV = min{δ : |OVB × (1-f(C·diag(1+δ)))| > threshold}。单调性：f 关于 δ 单调递减
      （扰动增大→C 偏离对角→更多残差混淆），因此 ASV 单调。紧性：构造 C* = 在 δ 约束下
      使 f(C*) 最小化的行随机矩阵（显式构造）。
      
      Mediation ASV：间接效应 = β_XM × β_MY|X，两者均是 C 的函数。ASV 通过乘积分解为
      两个单调函数的乘积——当两者符号一致时整体单调，当符号不一致时需要 envelope theorem
      处理极值切换，但最终仍可证明关于 δ 的单调性。紧性通过构造性 Lagrangian 求解
      使间接效应恰好等于 threshold 的 C*。
      
      Collider ASV：条件化打开伪路径的效应大小是 C 的非线性函数。通过 Lagrangian 优化
      在 {C : ||C - I|| ≤ g(δ)} 约束集上求解伪效应的极值，证明该极值关于 δ 单调。
      紧性：Lagrangian 的 KKT 条件给出显式 C*。
      
      Coverage at 95% nominal = 0.952（在 [0.93, 0.97] 范围内）：轻微过覆盖（0.952 > 0.950）
      是因为 ASV bound 使用了保守的 worst-case C 方向，而大多数实际 C 不在最坏方向上。
      这种过覆盖是良性的（保守偏倚）。Mediation (0.949) 和 collider (0.948) 的覆盖率
      略低于 confounding (0.958)，因为这两个拓扑的偏倚函数非线性更强，
      ASV 的线性化近似在极端 δ 值附近不够精确。
    tables:
      - name: "Table 8: ASV Formal Proof Summary"
        columns: ["Topology", "Monotonicity", "Sharpness", "Proof Technique", "Constructive C*?"]
        rows:
          - ["Confounding", "✓ Proved", "✓ Proved", "Algebraic (spectral gap)", "Yes — explicit"]
          - ["Mediation", "✓ Proved", "✓ Proved", "Algebraic + envelope theorem", "Yes — explicit"]
          - ["Collider", "✓ Proved", "✓ Proved", "Lagrangian optimization + KKT", "Yes — explicit"]
      - name: "Table 9: ASV Coverage Calibration (MC, 1000 scenarios)"
        columns: ["Topology", "Nominal 90%", "Actual 90%", "Nominal 95%", "Actual 95%", "Nominal 99%", "Actual 99%"]
        rows:
          - ["Confounding", "90%", "91.8%", "95%", "95.8%", "99%", "99.2%"]
          - ["Mediation", "90%", "90.9%", "95%", "94.9%", "99%", "98.7%"]
          - ["Collider", "90%", "90.8%", "95%", "94.8%", "99%", "98.5%"]
          - ["Average", "90%", "91.2%", "95%", "95.2%", "99%", "98.8%"]
    figures_description:
      - "Fig 11: ASV sensitivity curves per topology——x=δ, y=bias bound, with MC point estimates overlaid. 证明 bound 确实是上界且紧。"
      - "Fig 12: Coverage probability plot——nominal level (x) vs actual coverage (y)。理想情况为对角线。三个拓扑均紧贴对角线，confounding 略微过覆盖。"
    analysis: >
      三个完整形式化证明是本论文最重要的理论贡献之一。ASV 类比于因果推断中的 E-value：
      E-value 量化 "多大的未测量混淆才能推翻结论"，ASV 量化 "多大的标注误差才能推翻结论"。
      关键区别：E-value 只需一个标量参数（RR），ASV 需要参考混淆矩阵 + δ 方向，
      因此证明复杂度更高。构造性紧性证明（显式 C*）不仅有理论价值，还有实践价值——
      研究者可以检查 "使结论翻转的最近 C* 与我的实证 C 有多远"，获得直觉性理解。

  - name: "ASV MC validation for remaining 3 topologies"
    plan_id: "plan_005"
    description: >
      对 M-bias, instrument, front-door 三个拓扑推导 ASV 表达式，MC 验证单调性和覆盖率。
      紧性作为猜想，用数值证据支持。
    expected_results:
      asv_monotonicity_mc_validated: 3
      asv_monotonicity_violations: 0
      asv_coverage_95_mbias: 0.954
      asv_coverage_95_instrument: 0.961
      asv_coverage_95_frontdoor: 0.943
      sharpness_numerical_gap: "< 0.008 across all 3 topologies (bound within 0.8% of achievable)"
      sharpness_conjecture_status: "Supported by 1000 scenario numerical optimization — no counterexample found"
      frontdoor_asv_note: "Front-door ASV 涉及两阶段估计的联合扰动，闭式紧性证明需要解决双线性约束优化，identified as immediate future work"
    result_rationale: >
      单调性在所有 3 个拓扑的 MC 验证中均成立（0 violations）：单调性是一个"自然"性质——
      更大的标注误差（更大的 δ）只能增加偏倚的潜在范围，不能减少它。这在直觉上成立：
      δ 增大扩展了 C 的可行域，而偏倚 bound 是在可行域上的 supremum，
      可行域扩大 → supremum 不减。形式化证明的技术难点在于处理非凸可行域，
      但 MC 验证表明即使在解析证明困难的情况下，性质仍成立。
      
      紧性作为猜想而非证明：M-bias 的 DAG 结构（butterfly）使偏倚表达式涉及 4 个
      条件概率的乘积，优化问题是四次多项式约束优化，闭式解不可行。
      Instrument 的 Wald ratio 使约束优化涉及分式规划。
      Front-door 的两阶段结构使约束是双线性的。
      数值优化（sequential quadratic programming）在所有场景中找到的最优 C 
      与 ASV bound 的差距 < 0.008，强烈支持紧性但不构成证明。
      
      Front-door coverage 略低（0.943）：两阶段估计的非线性使 ASV 的线性化近似
      在 extreme δ 附近不够精确，但仍在 [0.93, 0.97] 范围内。
    tables:
      - name: "Table 10: ASV Validation for Remaining Topologies"
        columns: ["Topology", "Monotonicity", "Coverage @95%", "Sharpness Gap", "Formal Proof Status"]
        rows:
          - ["M-bias", "✓ MC-validated (0 violations/1000)", "95.4%", "0.006", "Conjecture (numerical)"]
          - ["Instrument", "✓ MC-validated (0 violations/1000)", "96.1%", "0.005", "Conjecture (numerical)"]
          - ["Front-door", "✓ MC-validated (0 violations/1000)", "94.3%", "0.008", "Conjecture (numerical)"]
    figures_description:
      - "Fig 13: Monotonicity verification——对每个拓扑展示 1000 个 scenario 的 ASV(δ) 曲线，全部单调递增，无一例外。"
      - "Fig 14: Sharpness gap histogram——gap 集中在 0.002-0.008 范围，远小于 ASV 值本身（通常 0.1-0.5），支持紧性猜想。"
    analysis: >
      诚实地将紧性限定为猜想（而非证明）是策略性选择：(1) 避免 reviewer 质疑证明严谨性，
      (2) 数值证据已经足够有说服力（gap < 0.008），(3) 完整证明作为 immediate future work 
      为后续论文提供了明确方向。六个拓扑的 ASV 框架完整性：3 个有完整证明 + 3 个有强数值支持，
      覆盖了实践者可能遇到的所有主要 DAG 设计。

  - name: "ASV calibration on empirical data"
    plan_id: "plan_006"
    description: >
      将 ASV 框架应用于 plan_003 的实证混淆矩阵。在 held-out gold-standard splits 上验证覆盖率。
      报告 ASV alongside downstream effect estimates。比较 ASV 可解释性与原始混淆矩阵报告。
    expected_results:
      empirical_asv_concordance: 8
      empirical_asv_concordance_detail: "9 个 scenario（3 tasks × 3 topological contexts）中 8 个 ASV 排序与实际 bias 严重度一致"
      discordant_case: "protest × instrument context: ASV 排序 DeepSeek > Qwen，实际 bias Qwen > DeepSeek（差异 0.02，在 noise margin 内）"
      asv_interpretability_rating: "研究者 pilot（N=5）中 4/5 偏好 ASV + sensitivity curve 而非原始 C 矩阵"
      held_out_coverage_95: 0.94
      asv_actionable_alerts: "3/9 scenarios ASV < 1.5（结论脆弱），6/9 ASV > 3.0（结论稳健）"
      asv_correctly_flags_reversal_risk: "2/2 scenarios where empirical C falls in reversal zone are flagged by ASV < 1.5"
    result_rationale: >
      Concordance 8/9：ASV 是基于 worst-case perturbation 的 bound，而非 point estimate。
      在大多数场景中，worst-case 方向与实际偏倚方向一致，因此排序一致。
      唯一 discordant case 出现在 instrument context，因为 Wald ratio 对 C 的微小差异
      极其敏感（分母接近零时），导致 ASV 排序与实际偏倚排序在 noise margin 内翻转。
      差异仅 0.02，在实际意义上可忽略。
      
      3/9 scenarios ASV < 1.5：这些对应 protest coding（K=5, 低对角优势 C）在 
      mediation 和 collider 拓扑下的应用。ASV < 1.5 意味着仅需 50% 的额外标注误差
      即可推翻结论——这是一个强警告信号。6/9 ASV > 3.0 对应较简单的 toxicity 任务
      和 confounding 拓扑，结论稳健。
      
      ASV 正确标记了 2 个落入反转区域的实证 C：这是 ASV 框架实用价值的最直接证据。
      研究者报告原始 C 矩阵时无法判断"这个 C 有多危险"——ASV 提供了这个判断。
      
      Held-out coverage 0.94（vs 理论 0.95）：轻微欠覆盖因为实证 C 的估计本身有
      sampling variance（~30K annotations），引入了理论分析未考虑的噪声。
      但 0.94 在可接受范围内。
    tables:
      - name: "Table 11: ASV Concordance with Empirical Bias Severity"
        columns: ["Task", "Topological Context", "Model Ranking by ASV", "Model Ranking by Actual Bias", "Concordant?"]
        rows:
          - ["Protest", "Mediation", "Qwen < Llama < DeepSeek", "Qwen < Llama < DeepSeek", "✓"]
          - ["Protest", "Collider", "Qwen < Llama < DeepSeek", "Qwen < Llama < DeepSeek", "✓"]
          - ["Protest", "Instrument", "DeepSeek < Qwen < Llama", "Qwen < DeepSeek < Llama", "✗ (margin 0.02)"]
          - ["Stance", "Mediation", "Qwen < Llama < DeepSeek", "Qwen < Llama < DeepSeek", "✓"]
          - ["Stance", "Collider", "Llama < Qwen < DeepSeek", "Llama < Qwen < DeepSeek", "✓"]
          - ["Stance", "Confounding", "Llama < Qwen < DeepSeek", "Llama < Qwen < DeepSeek", "✓"]
          - ["Toxicity", "Mediation", "Qwen < Llama < DeepSeek", "Qwen < Llama < DeepSeek", "✓"]
          - ["Toxicity", "Collider", "Qwen < DeepSeek < Llama", "Qwen < DeepSeek < Llama", "✓"]
          - ["Toxicity", "Confounding", "Qwen < Llama < DeepSeek", "Qwen < Llama < DeepSeek", "✓"]
      - name: "Table 12: ASV Robustness Classification"
        columns: ["Task", "Context", "Best Model ASV", "Worst Model ASV", "Classification"]
        rows:
          - ["Protest", "Mediation", "2.1 (DeepSeek)", "0.9 (Qwen)", "FRAGILE — reversal risk"]
          - ["Protest", "Collider", "1.8 (DeepSeek)", "1.1 (Qwen)", "FRAGILE — reversal risk"]
          - ["Protest", "Instrument", "3.2 (Llama)", "2.4 (DeepSeek)", "Moderate"]
          - ["Stance", "Mediation", "4.1 (DeepSeek)", "2.8 (Qwen)", "Robust"]
          - ["Stance", "Collider", "3.8 (DeepSeek)", "2.5 (Llama)", "Moderate"]
          - ["Stance", "Confounding", "5.2 (DeepSeek)", "3.9 (Llama)", "Robust"]
          - ["Toxicity", "Mediation", "7.3 (Llama)", "5.1 (Qwen)", "Robust"]
          - ["Toxicity", "Collider", "6.8 (Llama)", "4.9 (Qwen)", "Robust"]
          - ["Toxicity", "Confounding", "8.1 (DeepSeek)", "6.2 (Qwen)", "Robust"]
    figures_description:
      - "Fig 15: ASV sensitivity curves for 9 empirical scenarios，实证 C 的位置标注在曲线上。FRAGILE scenarios 的 C 落在曲线陡峭区域（小 δ 即翻转）。"
      - "Fig 16: Side-by-side comparison——左：原始 C 矩阵热力图（研究者通常报告的）；右：ASV robustness gauge（绿/黄/红）。直观展示 ASV 的信息增益。"
    analysis: >
      8/9 concordance 证明 ASV 在实践中是有效的偏倚严重度指标。唯一 discordance 出现在
      noise margin 内，且在 instrument context（本身就是高方差估计）。关键实用发现：
      protest event coding 在 mediation/collider context 下使用 Qwen 3.5 Plus 时 ASV < 1.0——
      这意味着研究者如果用 Qwen 做 protest 分类并将其作为 mediator/collider，其下游因果结论
      几乎肯定不可靠。这种 actionable alert 是单纯报告混淆矩阵无法提供的。

  - name: "Correction guidance framework validation"
    plan_id: "plan_007"
    description: >
      构建决策框架：{topology × error structure × ASV} → correction method（DSL / PPI / MLA / naive plug-in / "无现有方法适用"）。
      MC 验证推荐方法在各场景中是否产生最小偏倚。在 plan_003 数据上经验验证。
    expected_results:
      correction_framework_accuracy: 0.95
      correction_framework_accuracy_detail: "432 个 MC scenario 中 411 个推荐方法产生最小 bias"
      scenarios_tested: 432
      scenario_breakdown: "6 topologies × 6 C structures × 3 K values × 4 effect sizes = 432"
      method_recommendation_distribution:
        DSL: "18% of scenarios"
        PPI: "24% of scenarios"
        MLA: "31% of scenarios"
        naive_plugin: "12% of scenarios"
        no_adequate_method: "15% of scenarios"
      no_adequate_method_conditions: "primarily: correlated multi-LLM errors + differential K≥5 + collider/front-door topology"
      failure_cases: "21/432 — 14 cases where MLA and PPI are within 0.005 of each other (recommendation arbitrary), 7 cases where extreme C + small N makes all methods unstable"
      empirical_validation_plan003: "8/9 empirical scenarios — recommended method produces bias reduction ≥40% vs uncorrected"
      empirical_failure: "1/9 — protest × collider × Qwen: no method adequate (flagged correctly as 'no adequate method')"
    result_rationale: >
      95% accuracy（411/432）：决策框架基于理论偏倚表达式的 closed-form 分析，
      在每个 {topology × C structure} cell 中选择使残差偏倚最小化的方法。
      14 个"失败"case 实际上是 MLA 和 PPI 表现几乎相同（差异 < 0.005）的场景——
      框架推荐了其中一个，但另一个同样好。这不是真正的失败，只是不确定性。
      7 个真正失败的 case 出现在极端 C（near-permutation）+ 小样本（N=1000）下，
      所有方法都不稳定——这种场景下正确答案可能是"收集更多数据"而非选择方法。
      
      Method distribution：MLA（31%）最常被推荐因为它直接利用 C 矩阵做 deconvolution，
      在 C 已知时通常最优。PPI（24%）在 C 有不确定性时被推荐（利用少量 gold-standard 数据
      做 prediction-powered inference）。DSL（18%）在 confounding topology + 
      high diagonal dominance C 下被推荐（double sampling + likelihood correction）。
      Naive plug-in（12%）仅在 ASV > 5.0（结论非常稳健）时被推荐——此时 correction 
      的 variance cost 大于 bias reduction benefit。
      
      15% "no adequate method"：这些场景主要涉及 correlated multi-LLM errors + 
      differential K≥5 + collider/front-door topology。这是论文 Claim 3 的一部分——
      识别现有方法不足的区域并标记为 open problems。其中 dependence-aware multi-LLM 
      correction 是最重要的 open problem（回应 Kim et al. ICML 2025）。
      
      Empirical 8/9：1 个"failure"实际上是框架正确标记为"no adequate method"
      （protest × collider × Qwen，C 接近 near-permutation + 模型间误差高度相关）。
      这是一个 success case of honest scoping，而非真正失败。
    tables:
      - name: "Table 13: Correction Method Recommendation Distribution"
        columns: ["Method", "% Scenarios", "Typical Condition", "Avg Bias Reduction"]
        rows:
          - ["MLA", "31%", "C known, K≤5, non-differential", "72%"]
          - ["PPI", "24%", "C uncertain, gold-standard available", "65%"]
          - ["DSL", "18%", "Confounding topology, high diag. dominance", "58%"]
          - ["Naive plug-in", "12%", "ASV > 5.0 (robust conclusions)", "N/A (unnecessary)"]
          - ["No adequate method", "15%", "Correlated errors + differential + collider/front-door", "N/A"]
      - name: "Table 14: Framework Accuracy by Topology"
        columns: ["Topology", "Scenarios", "Correct", "Accuracy", "Most Common Failure Mode"]
        rows:
          - ["Confounding", "72", "71", "98.6%", "MLA ≈ PPI (indistinguishable)"]
          - ["Mediation", "72", "69", "95.8%", "Extreme C + small N"]
          - ["Collider", "72", "67", "93.1%", "MLA ≈ PPI + extreme C"]
          - ["M-bias", "72", "70", "97.2%", "Rare edge case"]
          - ["Instrument", "72", "69", "95.8%", "Wald ratio instability"]
          - ["Front-door", "72", "65", "90.3%", "Two-stage estimation complexity"]
    figures_description:
      - "Fig 17: Decision tree visualization——研究者输入 {topology, C estimate, ASV}，沿路径得到推荐方法 + 置信度。"
      - "Fig 18: Empirical bias before vs after correction，per scenario。9 个点，8 个在 'improvement' 区域，1 个在 'no method' 区域（correctly flagged）。"
    analysis: >
      95% 准确率表明基于理论的决策框架在实践中可靠。最重要的发现不是哪个方法最好，
      而是 "方法选择是拓扑依赖的"——在 confounding DAG 中最优的方法在 collider DAG 中
      可能增加偏倚。这直接回应了 Jerzak et al. (EMNLP 2025) 的 unconditional benchmarking 
      方法论：如果不考虑拓扑，benchmarking 本身就是误导性的。
      15% "no adequate method" 区域是诚实的 open problem identification，
      为后续方法论研究提供了明确方向。

  - name: "Pathological confusion matrix analysis"
    plan_id: "plan_009"
    description: >
      分析极端 C 结构（near-permutation, rank-deficient, block-diagonal）在所有拓扑中的
      偏倚行为。识别预测偏倚严重度的结构性指标（spectral gap, diagonal dominance ratio）。
    expected_results:
      spectral_gap_bias_correlation: 0.91
      diagonal_dominance_bias_correlation: 0.87
      best_predictor: "spectral gap (1 - λ₂/λ₁) explains 83% of bias magnitude variance"
      catastrophic_bias_threshold: "spectral gap < 0.15 → bias > 2x effect size in ≥80% of reversal-prone topologies"
      near_permutation_analysis: "all near-permutation C (spectral gap < 0.05) produce reversal in mediation/collider/front-door; severity 1.5-3x"
      rank_deficient_analysis: "rank-deficient C always produce catastrophic bias regardless of topology — information loss is complete for collapsed dimensions"
      block_diagonal_analysis: "bias depends on which classes are in same block — if classes with opposite effects are merged, reversal guaranteed"
      practitioner_diagnostic: "two-number summary: (spectral gap, diagonal dominance ratio) → risk category (low/medium/high/catastrophic)"
    result_rationale: >
      Spectral gap 与偏倚强相关（r=0.91）：混淆矩阵 C 的第二大特征值 λ₂ 控制了
      "主误分类模式"的强度。当 spectral gap = 1-λ₂/λ₁ 接近 0 时，C 接近非满秩，
      信息丢失严重，偏倚灾难性。这不是偶然——偏倚表达式中 C 的逆（或伪逆）出现在
      correction 中，spectral gap 控制了逆的条件数。
      
      Diagonal dominance 相关性略低（0.87 vs 0.91）因为 diagonal dominance 
      是一个粗糙的指标——它只看对角元素与行和的比值，不捕获 off-diagonal 的结构
      （如 block-diagonal 的特殊性）。Spectral gap 通过特征分解捕获了完整的 
      off-diagonal 结构信息。
      
      Near-permutation 全部产生反转（在反转敏感拓扑中）：near-permutation C 
      等价于类别标签几乎完全互换，这在 K≥3 时结构性地翻转效应方向（而 K=2 时
      近置换 = 高误分类率，仍然只 attenuate toward null）。
      
      Block-diagonal 的方向依赖于块结构：如果具有相反效应的类别被合并在同一块中，
      块内平均化可以翻转块的净效应方向。这与 binarization collapse 的机制相同，
      但发生在 C 矩阵内部而非研究者的显式折叠中。
    tables:
      - name: "Table 15: Structural Predictors of Bias Severity"
        columns: ["Predictor", "Correlation with |Bias|", "R² (univariate)", "Threshold for Catastrophic Bias"]
        rows:
          - ["Spectral gap (1-λ₂/λ₁)", "-0.91", "0.83", "< 0.15"]
          - ["Diagonal dominance ratio", "-0.87", "0.76", "< 0.55"]
          - ["Condition number of C", "0.89", "0.79", "> 12"]
          - ["Min diagonal element", "-0.84", "0.71", "< 0.3"]
          - ["Spectral gap + diag. dom. (joint)", "—", "0.89", "Combined threshold"]
    figures_description:
      - "Fig 19: Spectral gap vs bias magnitude scatter，color by topology。Reversal-prone topologies（mediation/collider/front-door）的红色点集中在低 spectral gap 区域。"
      - "Fig 20: Practitioner risk map——x=spectral gap, y=diagonal dominance, zones colored by risk level。研究者可将自己的 C 矩阵定位到此图上。"
    analysis: >
      为实践者提供了两个可操作的诊断数字：spectral gap 和 diagonal dominance ratio。
      研究者无需理解完整的偏倚理论，只需计算其实证 C 矩阵的这两个指标，
      即可判断偏倚风险等级。这补充了 ASV 框架——ASV 告诉你"结论多稳健"，
      而 spectral diagnostics 告诉你"为什么不稳健"和"C 的哪个方面最危险"。
      Catastrophic threshold（spectral gap < 0.15）在 plan_003 的实证数据中
      对应 Qwen 在 protest coding 某些 prompt 变体下的 C 矩阵——与 ASV < 1.0 
      的 fragile classification 完全一致。

  - name: "annot-sensitivity Python toolkit"
    plan_id: "plan_010"
    description: >
      开源 Python 包：用户输入 DAG + confusion matrix + downstream estimate →
      输出 bias expressions + ASV bounds + sensitivity curves + correction recommendation + diagnostic plots。
      pip-installable，含每个拓扑的 worked examples。
    expected_results:
      package_name: "annot-sensitivity"
      pip_installable: true
      supported_topologies: 6
      supported_K_range: "2-20"
      api_surface: "3 main functions: bias_expression(), asv_bound(), recommend_correction()"
      documentation: "6 topology-specific tutorials (Jupyter notebooks), API reference, quickstart guide"
      test_coverage: ">90%"
      benchmark: "bias_expression() < 0.1s for K≤7; asv_bound() < 1s for K≤7; recommend_correction() < 0.5s"
      dependencies: "numpy, scipy, matplotlib (minimal)"
      worked_examples: 6
    result_rationale: >
      Toolkit 是论文影响力的关键放大器。学术论文的理论贡献如果没有可用工具，
      很难被实践者采纳。三个主函数对应论文三个 claims：bias_expression() → Claim 1（taxonomy），
      asv_bound() → Claim 2（ASV），recommend_correction() → Claim 3（correction guidance）。
      
      K 支持范围 2-20：K=2 作为 consistency check（应恢复经典二分类结果），
      K>7 用矩阵表达式 + 特征分解可解释性工具。K>20 实际中极罕见且计算成本高
      （C 矩阵有 K(K-1) 自由参数），故限定上界。
      
      性能目标（< 1s for K≤7）：bias_expression 和 recommend_correction 是闭式计算，
      主要耗时在矩阵运算。asv_bound 涉及优化问题（构造性紧性需要求解约束优化），
      K≤7 时维度足够低，SQP 在 1s 内收敛。
      
      最小依赖（numpy, scipy, matplotlib）：降低安装门槛，compatible with 
      任何 Python 科学计算环境。不依赖 PyTorch/TensorFlow 因为所有计算是
      解析数学而非机器学习。
    tables: []
    figures_description:
      - "Fig 21 (不在论文中，在 toolkit README): 示例输出截图——bias sensitivity curve + ASV gauge + correction recommendation 的组合 dashboard。"
    analysis: >
      Toolkit 的设计哲学是"一个函数回答一个问题"。研究者的典型 workflow：
      (1) 收集 gold-standard 子集 → 估计 C；(2) 调用 bias_expression(dag, C, K) → 
      了解偏倚结构；(3) 调用 asv_bound(dag, C, estimate, threshold) → 了解结论稳健性；
      (4) 调用 recommend_correction(dag, C, asv, n_gold) → 选择校正方法。
      开源发布对 AAAI/ARR 审稿均加分——artifact evaluation 是近年趋势。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60d2c78c-068b-4885-8f81-7769c34d221a",
  "isSidechain": false,
  "requestId": "req_011CbDTAvw1uNeUWBMu1VxK3",
  "type": "assistant",
  "uuid": "2cc0c602-3f77-4de4-92fa-99fb22cea95f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e14e2c22-1d8d-4bf4-953a-e482c1a8d81f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Es5cUJmup5FaK1z32w3u2X",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10666,
      "cache_read_input_tokens": 11841,
      "output_tokens": 21825,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10666,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 21825,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10666
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：≥3 topologies (含 exposure) 出现方向反转；ASV 框架在所有优先拓扑上均具备单调性+紧性证明；经验数据清晰展示 ASV 的实用价值 核心假设：['mediation 和 collider DAG 在 non-differential K≥3 误分类下均出现方向反转（100k rand…",
  "leafUuid": "2cc0c602-3f77-4de4-92fa-99fb22cea95f",
  "sessionId": "e14e2c22-1d8d-4bf4-953a-e482c1a8d81f"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-class annotation error direction reversal across DAG topologies",
  "sessionId": "e14e2c22-1d8d-4bf4-953a-e482c1a8d81f"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：≥3 topologies (含 exposure) 出现方向反转；ASV 框架在所有优先拓扑上均具备单调性+紧性证明；经验数据清晰展示 ASV 的实用价值 核心假设：['mediation 和 collider DAG 在 non-differential K≥3 误分类下均出现方向反转（100k rand…",
  "leafUuid": "2cc0c602-3f77-4de4-92fa-99fb22cea95f",
  "sessionId": "e14e2c22-1d8d-4bf4-953a-e482c1a8d81f"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-class annotation error direction reversal across DAG topologies",
  "sessionId": "e14e2c22-1d8d-4bf4-953a-e482c1a8d81f"
}
```

---
