# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：2 个拓扑出现方向反转（exposure + mediation 或 collider 之一）；ASV 紧性证明仅覆盖 2 个拓扑；经验验证可用但不

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/86f3ecd8-a732-4359-9b4e-e89c85b83a9f.jsonl`
- **Structured JSON:** [`3a1a76a52833a6acce37.json`](../../sessions/3a/3a1a76a52833a6acce37.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T07:57:22.652Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T07:57:22.652Z",
  "sessionId": "86f3ecd8-a732-4359-9b4e-e89c85b83a9f",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：2 个拓扑出现方向反转（exposure + mediation 或 collider 之一）；ASV 紧性证明仅覆盖 2 个拓扑；经验验证可用但不够 dramatic\n核心假设：['mediation 或 collider 中恰好 1 个出现方向反转（violation rate 15-40%），另 1 个单调', 'M-bias/instrument/front-door 均为单调（无反转），但 magnitude 变异显著', 'ASV 单调性对所有拓扑成立，但紧性仅对 2 个拓扑有形式化证明', '经验 ASV 排序大部分正确，但在低 bias 区间区分力不足', 'correction framework 整体有效，但 2-3 个边界场景中方法不可区分']\n关键指标范围：{'reversal_topologies_count': [2, 2], 'mediation_violation_rate': [0.0, 0.4], 'collider_violation_rate': [0.0, 0.4], 'theory_mc_match_rate': [0.85, 0.95], 'asv_coverage_at_95_nominal': [0.88, 0.93], 'asv_sharpness_formal_proofs': [2, 2], 'binarization_max_delta': [0.1, 0.15], 'correction_framework_accuracy': [0.85, 0.93], 'empirical_asv_concordance': [6, 8]}\n叙事方向：Version A 成立但需收窄 scope。Lead finding 聚焦于 exposure + 1 个拓扑的对比，而非 \"广泛打破经典保证\"。Claim 1 调整：taxonomy 仍然有效，但方向反转是 topology-specific 而非 universal，需强调 magnitude 不可预测性作为补充论据。Claim 2 调整：ASV 紧性降级为 \"2 个拓扑有证明 + 4 个有 MC 数值证据\"，增加一段讨论紧性证明的技术障碍。Claim 3 不变。 需补充实验：对反转拓扑做更细粒度的 C structure 条件分析（何时反转、何时不反转）， 以增强实用价值。可能需要额外 1-2 个经验任务来补偿理论覆盖面的缩窄。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: causal_annot_error_attrib\nfocus: Key uncertainty: will mediator/collider DAGs show direction reversal under non-differential multi-class error? Confounding DAG was monotonic in MVP. Also: is ASV framework practically useful enough vs just reporting confusion matrices?\n\n## paper_framing.md\n\n# Paper Framing — causal_annot_error_attrib\n\n## Target Venue\n- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)\n- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)\n- Tertiary: ICWSM 2027 Round 2 (2026-09-15)\n\n## Title\nMulti-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies\n\n## Core Claims (3 条)\n\n1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 6 canonical social-science DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door).\n\n2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of differential annotation error needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Reported alongside estimates, analogous to E-values for unmeasured confounding. Formal proofs (monotonicity + sharpness) for 3 priority topologies; MC-validated conjectures for the remaining 3.\n\n3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI, MLA, naive plug-in), characterizing regimes where each applies and where no existing method suffices — including dependence-aware multi-LLM correction as an open problem.\n\n## Story Spine\n\n- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31% of downstream conclusions are already incorrect. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable.\n\n- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.\n\n- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.\n\n- **Headline result template**: \"Across 6 DAG topologies with K=3,5,7, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. On 3 CSS tasks annotated by 3 LLMs, ASVs provide calibrated robustness indicators, and our taxonomy identifies cases where commonly applied corrections would increase rather than decrease bias.\"\n\n## Core Insight (Lead Finding) — DUAL VERSION, gate on plan_001\n\n### Version A (≥1 topology shows direction reversal under K≥3 non-differential exposure misclassification)\nThe binary guarantee that \"non-differential exposure misclassification biases toward the null\" (Bross 1954) breaks in the multi-class case. For specific confusion matrix structures in specific DAG topologies, K≥3 non-differential error can amplify or reverse effect estimates. Brenner (1993) identified this possibility for polytomous confounder misclassification (\"bias can go in either direction\"); we provide the first systematic characterization across 6 DAG topologies with exact conditions for each {C structure × topology} cell. Furthermore, binarizing a K-class variable to \"escape\" into the binary regime is itself hazardous — collapsing introduces new, direction-unpredictable bias (MVP evidence: Δ up to 0.103).\n\n### Version B (no direction reversal found across topologies)\nMulti-class annotation error is structurally irreducible to the binary case: the downstream bias magnitude depends on the full K×K confusion matrix in ways that binary sensitivity/specificity cannot predict, and binarizing a K-class variable introduces new bias (MVP evidence: Δ up to 0.103). While non-differential error preserves bias direction across tested topologies (a useful practitioners' guarantee), the magnitude varies dramatically with confusion matrix structure (0.13–0.30 in confounding DAG alone), and this variation is topology-dependent. ASVs provide the missing robustness measure for this quantitative — not directional — uncertainty.\n\n**Gate**: plan_001 results determine which version. ≥2 topologies with reversal → A; 1 → A with that topology as lead; 0 → B. See D003.\n\n## MVP Evidence\n\n**Confounding DAG + K=3** (confounder misclassification):\n- Theoretical bias expressions match MC perfectly (6/6 structures within 95% CI) — framework validated\n- Binary collapse ≠ multi-class: Δ up to 0.103 (near-permutation C), proving K=3 retains more confounding control than binarization\n- 100k random C search: confounding DAG bias is monotonically toward OVB — this topology is \"well-behaved\" (predictable direction)\n- NOTE: Confounding DAG tests residual confounding, NOT bias-toward-null (Bross 1954). Criterion 2 (away-from-null bias) holds for binary too in this topology. See M001.\n\n**Exposure DAG K=3** (exposure misclassification — D002/D004 CONFIRMED):\n- 100k random C: 85% violate bias-toward-null, 83.4% sign reversal, 14.1% amplification\n- K=2 control: 6/6 toward null (binary guarantee holds)\n- Worst case: β=1.0 → estimate=-0.84 (sign reversal + 2.83x amplification)\n- Mechanism: near-permutation C causes label swap → effect direction flips (structurally impossible in K=2)\n- **Two-DAG contrast**: confounding (monotonic, predictable) vs exposure (unpredictable, topology-dependent) — validates core claim\n\n## Venue Fit Risks\n\n- **AAAI**: Broad AI audience — emphasize general methodology for \"automated annotation measurement error,\" not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.\n- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.\n- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n1. **\"Trivial extension of binary to multi-class\"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 6 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]\n\n2. **\"Lee & Wood-Doughty (2024) already did categorical\"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 6 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]\n\n3. **\"Why these 6 DAG topologies?\"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]\n\n4. **\"K≥5 expressions aren't actionable\"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]\n\n5. **\"ASV sharpness only proved for 3 topologies\"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]\n\n6. **\"Correlated multi-LLM errors?\"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]\n\n7. **\"Empirical validation scope\"** → 3 CSS tasks × 3 LLMs × 3 DAG-relevant scenarios. Tasks selected to cover K=2,3,5 annotation complexity. [Experiments: plan_003, plan_006]\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: Derive and MC-validate bias expressions for 6 DAG topologies with K=3\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n  details: 'For each topology (confounding, mediation, collider, M-bias, instrument,\n    front-door): derive closed-form K=3 bias expression, validate with MC (1000 reps\n    × N=10000, 6 confusion matrix structures including near-permutation extreme).\n    Key question: which topologies show direction reversal under non-differential\n    error? Confounding already validated in MVP (no reversal, monotonic toward OVB).\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  description: Extend bias expressions to K=5,7 — matrix notation + interpretability\n    tools\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'Matrix-form expressions for general K. Three interpretability tools: (a)\n    eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar\n    bounds collapsing matrix to conservative scalar, (c) diagnostic visualizations\n    mapping confusion matrix regions to bias magnitude. Validate on confounding +\n    mediation + collider DAGs with K=5,7.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 1\n  description: 'Empirical confusion matrices: 3 LLMs × 3 CSS tasks vs gold-standard'\n  priority: P0\n  gpu_budget_hours: 0\n  api_cost_estimate: $300-550\n  deps: []\n  details: 'Tasks: protest event coding (K=5, ACLED/GPT-RE), stance detection (K=3,\n    SemEval/VAST), toxicity (K=2, as special case / consistency check, Civil Comments).\n    Models: Llama 4 Maverick (Together.ai), Qwen 3.5 Plus (OpenRouter), DeepSeek V4\n    (DeepSeek API). ~30K annotations per model × 3 datasets × 3 prompt variants. Output:\n    empirical confusion matrices, inter-model correlation analysis, downstream regression\n    bias vs gold-standard baseline.\n\n    '\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Binarization collapse analysis: K→2 folding bias across all 6 topologies'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'For each of 6 topologies with K=3,5,7: collapse to binary, compare bias\n    from full multi-class expression vs binarized expression. Demonstrate that binarization\n    is not a safe shortcut — can amplify or reverse bias. MVP showed Δ up to 0.089\n    for confounding DAG K=3.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'ASV framework: formal proofs for confounding, mediation, collider'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'Derive ASV expressions for 3 priority topologies. Formal proofs of: (a)\n    monotonicity (ASV increases with δ amplification), (b) sharpness (bound is achievable\n    for some confusion matrix). MC validation: coverage at 90%, 95%, 99% levels across\n    1000 scenarios.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 2\n  description: ASV MC validation for M-bias, instrument, front-door topologies\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_004\n  details: 'ASV expressions + MC validation of monotonicity and coverage. Sharpness\n    stated as conjectures supported by numerical evidence. If any topology fails monotonicity\n    under MC, flag and investigate.\n\n    '\n  status: planned\n- id: plan_006\n  claim: 2\n  description: ASV calibration on empirical data (3 CSS tasks × 3 LLMs)\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  - plan_004\n  details: 'Apply ASVs to empirical confusion matrices from plan_003. Validate coverage\n    on held-out gold-standard splits. Report ASV alongside downstream effect estimates\n    for each task. Compare ASV interpretability with raw confusion matrix reporting.\n\n    '\n  status: planned\n- id: plan_007\n  claim: 3\n  description: 'Correction guidance framework: decision mapping + validation'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_004\n  - plan_003\n  details: 'Decision framework: {topology × error structure × ASV} → correction method\n    (DSL / PPI / MLA / naive plug-in / \"no existing method adequate\"). MC validation:\n    recommended method produces least bias in ≥90% of scenarios. Empirical validation\n    on plan_003 data. Characterize regimes where no existing method suffices (correlated\n    errors, differential multi-class, etc.) — identify as open problems.\n\n    '\n  status: planned\n- id: plan_009\n  claim: 1\n  description: Pathological confusion matrix analysis (near-permutation, rank-deficient)\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'Extreme C structures: near-permutation, rank-deficient, block-diagonal.\n    Characterize when bias becomes catastrophic across topologies. Identify structural\n    conditions (spectral gap, diagonal dominance ratio) that predict bias severity\n    — candidate features for practitioners.\n\n    '\n  status: planned\n- id: plan_010\n  claim:\n  - 1\n  - 2\n  - 3\n  description: annot-sensitivity Python toolkit (open-source release)\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_004\n  - plan_007\n  details: 'Package: user-specified DAG + confusion matrix(es) + downstream estimate\n    → bias expressions (scalar K≤3, matrix K>3 with interpretability) + ASV bounds\n    + sensitivity curves + correction recommendation + diagnostic plots. pip-installable,\n    with worked examples for each topology.\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_confounding_dag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    theory_mc_match: 6/6\n    pass_criteria: 3/3\n    max_binary_collapse_delta: 0.103\n    bias_range: 0.132-0.298\n    ovb_reference: 0.3\n    direction_reversal_found: false\n    random_search_100k_min_bias: 0.063\n- exp_id: mvp_exposure_dag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    theory_mc_match: 5/5\n    pass_criteria: 3/3\n    violation_rate: 0.85\n    sign_reversal_rate: 0.834\n    amplification_rate: 0.141\n    K2_toward_null: 6/6\n    worst_severity: 2.83\n    named_structures_with_violation: 3/6\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T07:57:22.656Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T07:57:22.656Z",
  "sessionId": "86f3ecd8-a732-4359-9b4e-e89c85b83a9f"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T07:57:22.693Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：2 个拓扑出现方向反转（exposure + mediation 或 collider 之一）；ASV 紧性证明仅覆盖 2 个拓扑；经验验证可用但不够 dramatic
核心假设：['mediation 或 collider 中恰好 1 个出现方向反转（violation rate 15-40%），另 1 个单调', 'M-bias/instrument/front-door 均为单调（无反转），但 magnitude 变异显著', 'ASV 单调性对所有拓扑成立，但紧性仅对 2 个拓扑有形式化证明', '经验 ASV 排序大部分正确，但在低 bias 区间区分力不足', 'correction framework 整体有效，但 2-3 个边界场景中方法不可区分']
关键指标范围：{'reversal_topologies_count': [2, 2], 'mediation_violation_rate': [0.0, 0.4], 'collider_violation_rate': [0.0, 0.4], 'theory_mc_match_rate': [0.85, 0.95], 'asv_coverage_at_95_nominal': [0.88, 0.93], 'asv_sharpness_formal_proofs': [2, 2], 'binarization_max_delta': [0.1, 0.15], 'correction_framework_accuracy': [0.85, 0.93], 'empirical_asv_concordance': [6, 8]}
叙事方向：Version A 成立但需收窄 scope。Lead finding 聚焦于 exposure + 1 个拓扑的对比，而非 "广泛打破经典保证"。Claim 1 调整：taxonomy 仍然有效，但方向反转是 topology-specific 而非 universal，需强调 magnitude 不可预测性作为补充论据。Claim 2 调整：ASV 紧性降级为 "2 个拓扑有证明 + 4 个有 MC 数值证据"，增加一段讨论紧性证明的技术障碍。Claim 3 不变。 需补充实验：对反转拓扑做更细粒度的 C structure 条件分析（何时反转、何时不反转）， 以增强实用价值。可能需要额外 1-2 个经验任务来补偿理论覆盖面的缩窄。


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
  "promptId": "e8f77f9a-81e5-441f-8621-7de1077e969d",
  "type": "user",
  "uuid": "8a4fb488-c9e7-4c6d-a9c6-b068cb8e598c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "86f3ecd8-a732-4359-9b4e-e89c85b83a9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T07:57:22.692Z_

```json
{
  "parentUuid": "8a4fb488-c9e7-4c6d-a9c6-b068cb8e598c",
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
  "uuid": "640df67a-7346-4ffd-8321-be9a44bf0983",
  "timestamp": "2026-05-20T07:57:22.692Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "86f3ecd8-a732-4359-9b4e-e89c85b83a9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T07:57:22.692Z_

```json
{
  "parentUuid": "640df67a-7346-4ffd-8321-be9a44bf0983",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "daa3c9a8-083a-462a-9fda-f29477b454d9",
  "timestamp": "2026-05-20T07:57:22.692Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "86f3ecd8-a732-4359-9b4e-e89c85b83a9f",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：2 个拓扑出现方向反转（exposure + mediation 或 collider 之一）；ASV 紧性证明仅覆盖 2 个拓扑；经验验证可用但不够 dramatic 核心假设：['mediation 或 collider 中恰好 1 个出现方向反转（violation rate 15-40%），另 1…",
  "leafUuid": "daa3c9a8-083a-462a-9fda-f29477b454d9",
  "sessionId": "86f3ecd8-a732-4359-9b4e-e89c85b83a9f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze annotation errors across multi-class causal DAGs",
  "sessionId": "86f3ecd8-a732-4359-9b4e-e89c85b83a9f"
}
```

---

### Assistant

_source line 8 · 2026-05-20T08:10:04.495Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment results for each planned experiment in the experiment plan, calibrated to the "median" tier definition they've provided. Let me carefully go through each experiment and generate realistic predictions.

Let me analyze the median tier:
- 2 topologies show direction reversal (exposure + one of mediation/collider)
- ASV sharpness formal proofs cover only 2 topologies
- Empirical verification available but not dramatic
- Key metrics are well-defined

Let me go through each plan_id:


For plan_001, I'm deriving bias expressions across the 6 DAG topologies with K=3, where the exposure already shows reversal from the MVP. Based on the median tier, I expect one additional topology between mediation and collider to reverse, with violation rates staying in the 0-40% range for each. The theory-MC match rate should land around 0.85-0.95, while M-bias, instrument, and front-door topologies remain monotonic without reversal. Plan_002 extends this to K=5 and K=7 with matrix notation for better interpretability.

Now I'm moving through the remaining validation steps: empirical confusion matrices across 3 LLMs and CSS tasks, binarization collapse analysis with max deltas around 0.10-0.15, then formal ASV proofs for the 3 priority topologies—though the median suggests only 2 will achieve formal sharpness with coverage around 0.88-0.93. The remaining 3 topologies get MC validation with conjectures, followed by ASV calibration on empirical data targeting concordance of 6-8. I'm also building out the correction guidance framework with expected accuracy of 0.85-0.93, analyzing pathological confusion matrices, and implementing this in Python.

For the topology reversals, I'm deciding between mediation and collider as the one showing direction reversal under misclassification. Collider bias seems structurally more plausible—conditioning on a misclassified collider can induce spurious associations in unexpected directions. I'll set mediation as monotonic and collider as the one reversing with a violation rate around 25%.

Now I need to construct the detailed results for each plan, starting with confounding which is already established as monotonic toward omitted variable bias.

For the exposure pathway, I'm confirming the 85% violation rate, while mediation shows reversals in about 25% of cases concentrated in near-permutation C structures. Collider remains monotonic despite varying magnitudes, and the remaining pathways (M-bias, instrument, front-door) all show monotonic behavior. The theory-to-simulation match rate comes in around 92%, with minor discrepancies in the more complex topologies.

Moving to the higher-dimensional analysis, I'm deriving K=5 and K=7 expressions through matrix form and using eigendecomposition to identify the dominant modes—typically 2-3 of them. The computational scaling with K² stays manageable, and importantly, the reversal patterns I found at K=3 for exposure and mediation persist as K increases.

For the empirical validation, I'm collecting confusion matrices across models and analyzing their inter-model correlations, which reveal non-trivial but incomplete agreement patterns.

On the binarization front, the maximum delta sits around 0.12, within the expected 0.10-0.15 range, though some topologies do show direction reversals from the binarization process.

For the formal proofs, I'm finding that monotonicity holds across all three priority topologies, but sharpness proofs only come through for two of them—confounding and mediation get the formal treatment, while collider runs into technical obstacles.

The other topologies show promise too: M-bias, instrument, and front-door all validate through Monte Carlo simulation with monotonicity holding across the board, though sharpness there remains conjecture backed by numerical evidence. The empirical ASV concordance is tracking around 7 out of 9 cases.

Now I'm working through the concrete metrics for each plan. For plan_001, I'm looking at 36 total scenarios across 6 topologies and 6 causal structures, expecting theory-MC alignment around 0.917 with exposure violation rates near 0.85.

For the mediation and collider cases, I need to be precise about which one shows direction reversal—the reversing case should have violation rates between 15-40%, while the monotonic one stays at 0%. I'll set mediation to approximately 0.25 to capture that middle range.

Now I'm looking at the performance metrics across the different plans: ASV coverage is around 91%, which fits the expected range, and I've identified two sharpness proofs for confounding and mediation. For the other plans, max delta is roughly 0.13, concordance across scenarios is about 7 out of 9, and accuracy hovers near 0.89. I'm ready to compile this into the YAML documentation with relevant summary tables included.

For plan_003, I need to think through what the empirical results would show—confusion matrices from multiple LLMs on different tasks, inter-model correlations aligned with the literature, observable but not extreme downstream bias, and ASVs catching most risky scenarios. The key metrics to track are off-diagonal mass in the confusion matrices, how errors correlate across models, and the bias relative to a gold standard. I'm also considering plan_002 with different K values, where the eigendecomposition should reveal a few dominant modes accounting for most of the bias variance, and the reversal patterns from K=3 should hold up across K=5 and K=7.

Now I'm ready to write out the YAML structure. I need to make sure the narrative positioning reflects the median tier appropriately, and I should think carefully about which topologies actually reverse—exposure is confirmed, but for mediation I need to trace through what happens when the mediator gets misclassified with a near-permutation confusion matrix. Let me draft this carefully. swapped, which could reverse the apparent X→M or M→Y relationship, leading to reversal of the indirect effect. This is plausible.

Collider DAG: X → Z ← Y with Z misclassified and conditioned on. Conditioning on misclassified Z induces spurious association between X and Y. The direction of this spurious association depends on the misclassification structure. This is also plausible.

I'm leaning toward mediation as the reversing topology since it gives a cleaner narrative—both exposure and mediation involve variables on the causal pathway being misclassified, whereas collider and other structures are more about selection or auxiliary variables. Though collider is tempting because it's already counterintuitive, and adding misclassification to Berkson's paradox creates a compelling story. But mediation wins out because it's far more common in CSS research and the practical devastation of reversed indirect effects is more broadly relevant to the audience.

Now I need to finalize the YAML and select six topologies for plan_001. I need to pare this down to 6 topologies instead of 7, so I'm dropping exposure misclassification and focusing on confounding, mediation, collider, M-bias, instrument, and front-door. With 36 total scenarios across these topologies and their different C structures, I'm expecting a theory-MC match rate around 0.917 (33 out of 36), with the 3 mismatches likely concentrated in the more complex topologies like M-bias and front-door where the bias expressions are intricate and Monte Carlo variance tends to be higher.

Now I'm structuring the YAML output with fields for name, plan_id, description, expected results as metric-value pairs, result rationale, table descriptions, figure descriptions, and analysis. I should include actual table data where it's meaningful but keep complex tables as descriptions. Let me write out the full YAML block now, making sure it's the only output.

For plan_003, I'm setting up the median tier with three LLMs across three tasks: protest coding with K=5, stance detection with K=3, and toxicity with K=2. The empirical results should show confusion matrices with moderate off-diagonal spread, inter-model correlations around 0.5-0.65, and detectable but not extreme downstream bias. I'm targeting macro accuracy of 0.65-0.75 for protest coding with confusion between adjacent categories, 0.72-0.82 for stance detection with a neutral-as-default bias pattern, and 0.85-0.92 for toxicity classification.

Now I'm working through the calibration and correction frameworks. The ASV calibration across 9 scenarios should show concordance in 7 out of 9 cases, with the 2 failures likely occurring in the low-bias toxicity regime where ASV can't effectively discriminate. The correction framework achieves around 0.89 accuracy but has 2-3 boundary cases where methods become indistinguishable, particularly in low-bias regimes with near-diagonal confusion matrices. For binarization, I'm seeing a maximum delta of 0.13 across different topologies with varying K values, with the worst performance in exposure or mediation topologies. I'm also examining spectral gap and diagonal dominance as predictors for pathological cases.

Now I'm finalizing the toolkit and YAML configuration. The package is working and covers all 6 topologies with a solid API design. For the mediation violation rate, I'm setting it to 23% to create contrast with the exposure topology's 85% violation rate—mediation is conditionally broken only under specific causal structures, while exposure is dramatically broken. Permutation methods consistently underperform, and rank-deficiency depends on the topology being tested.

Writing the comprehensive YAML... the X→M and M→Y pathways. For near-permutation C, the M labels get swapped, which can reverse the apparent M→Y relationship. However, unlike exposure misclassification where the effect is direct and dramatic, mediation misclassification is attenuated because the indirect effect is a product of two coefficients — reversal only occurs when C is sufficiently far from diagonal AND the true indirect effect is moderate. This explains the lower violation rate (23% vs 85% for exposure).

For collider being monotonic: When Z is misclassified and conditioned on, the induced spurious association between X and Y is always in the same direction (toward the null, reducing the apparent independence). This is because misclassification of Z effectively reduces the strength of conditioning, making the collider bias smaller but not reversed. The mechanism: smoothing Z's distribution weakens the selection effect rather than changing its direction.

These mechanistic explanations hold up. Now looking at plan_002 with K=5 and K=7: I've successfully derived matrix expressions for all six topologies, with K=5 having 20 free parameters and K=7 having 42. The eigendecomposition reveals that just the top 2-3 modes capture 82-90% of the bias variance, though the worst-case bounds are conservative at 2-3x actual values. The reversal patterns I found for exposure and mediation persist at these higher K values, and interestingly, mediation's violation rate creeps up slightly at K=7 (around 30%) because the additional off-diagonal mass creates more opportunities for label swaps. For confounding at K=5, the first eigenmode alone explains 78% of bias variance and corresponds to diagonal dominance deviation, while exposure's top two modes account for 91% of the variance.

Writing YAML configuration... Now I'm mapping out the visualizations for each remaining experiment—eigenvalue spectra across different K values to show how topology affects the spectrum, bias scaling patterns, and diagnostic confusion matrices to pinpoint where the worst biases emerge. For plan_003, I'll use confusion matrix heatmaps across model-task pairs with correlation analysis and a summary of downstream bias severity. Plans 004 and 005 focus on ASV curves against δ, coverage calibration, and sharpness evidence from both formal proofs and numerical results. Finally, plan_006 will compare ASV predictions against actual sensitivity with case studies demonstrating where the method correctly identifies risky scenarios.

For the remaining plans, I'm creating a decision tree to guide method selection based on topology and error structure, a heatmap showing which approach works best for different configurations, and boundary case illustrations. Then I'll visualize the binarization gap across topologies and K values with examples of direction reversals, followed by a phase diagram showing the relationship between spectral gap and bias severity to identify when bias becomes catastrophic. I'll also include a summary table for plan_001 showing violation rates, sign reversal frequencies, maximum severity scores, and how well theory matches the Monte Carlo simulations across different topologies. Looking at the topology counts, I need to reconcile the differences between the MVP results and plan_001. The MVP had 5 exposure matches out of 5, but plan_001 extends to all 6 topologies with 6 causal structures each, so I should recalculate whether exposure maintains that perfect score or if there are mismatches I'm missing in the expanded framework.

Now I'm working through the match rate distribution across all 36 scenarios. With a median theory_mc_match_rate around 0.917, that translates to 33 correct matches out of 36. I'm allocating the 3 mismatches across the different identification strategies: collider bias has one failure case with near-permutation structures and high variance, M-bias has one mismatch from complex topology interactions, and front-door has one from the ratio-based formula creating higher Monte Carlo variance. The other four strategies—confounding, exposure, mediation, and instrumental variables—all achieve perfect matches.

For mediation specifically, I'm now looking at the violation and sign reversal rates of 0.23 and 0.18 respectively to understand where the method breaks down. I'm trying to work out what the severity metric actually represents—whether it's the ratio of absolute estimates to true values, the relative bias, or something else entirely. The 2.83 figure doesn't align with any of these straightforward calculations, so I need to reconsider how this severity measure is being defined.

I think worst_severity might be a separate aggregate metric across all scenarios rather than tied to a specific β value, so I'll treat it as a scalar multiplier without getting caught up in the exact derivation. For mediation effects in the median tier, a worst_severity around 1.6 seems plausible—less dramatic than the exposure-level amplification of 2.83.

I'm going to move forward with writing the YAML configuration now rather than continuing to parse this definition.

The narrative guidance also mentions a supplementary experiment about fine-grained C structure analysis for reversed topologies—specifically examining when reversals occur versus when they don't—to strengthen practical applicability. This might require one or two additional empirical tasks to compensate for narrowed theoretical coverage. I should incorporate this as a note within the existing plan structure or flag it as supplementary work alongside the main experiments.

Writing YAML configuration...

For plan_006, the ASV concordance metric of 7 indicates that out of approximately 9 task-model pairs, 7 show ASV rankings that correctly predict robustness differences between model-task combinations. The two failures occur in the low-bias regime where toxicity K=2 produces uniformly high ASV scores that can't discriminate between models. I'll use 7 as the concordance value without overspecifying the exact counting method—the description will make the meaning clear.

Now I'm mapping out the correction framework where different combinations of topology, error structure, and ASV level point to specific methods like DSL, PPI, MLA, or naive plug-in approaches. Across roughly 90 scenarios (6 topologies × 5 error structure bins × 3 ASV levels), the framework achieves about 89% accuracy in recommending the right method, with failures concentrated at boundaries where methods perform similarly or error structures fall between differential and non-differential patterns.

The indistinguishable cases cluster around three scenarios: near-diagonal confounding matrices where all methods converge on small bias, moderate off-diagonal structures with mediation where both DSL and MLA work equally well, and low-bias exposure settings where PPI and naive plug-in are both adequate. I'm about to write this up in YAML with concrete tables where they help, but first I need to clarify the sharpness evidence distribution—the narrative indicates 2 topologies have formal proofs while 4 have Monte Carlo numerical support, giving all 6 topologies some form of sharpness backing even if only 2 are formally proven.

Plan_004 covers confounding, mediation, and collider, yielding 2 formal proofs from that set, while plan_005 targets M-bias, instrument, and front-door with MC evidence only. So I'm deciding between confounding and mediation versus confounding and collider for the formal proofs—confounding is straightforward and well-studied, but mediation's reversal behavior complicates the sharpness proof since the bound might not stay tight when reversals occur. region that blocks the formal proof. So I'm settling on confounding and collider for formal sharpness proofs, while mediation and three other topologies get Monte Carlo evidence instead—that gives me two formal proofs and four MC validations across six total topologies, which aligns with the median tier definition. Now I need to write out the YAML configuration with appropriate detail levels, prioritizing the main experiments while keeping supporting ones concise.

Looking at how each plan contributes: plan_001 is the core with six topologies and K=3 bias expressions plus MC validation, showing reversals in exposure and mediation cases. plan_002 extends to K=5 and K=7 to confirm the patterns hold. plan_003 brings empirical confusion matrices across models and tasks, though the real-world results are moderate rather than dramatic—the downstream bias is detectable but not as striking as theoretical extremes would be. plan_004 delivers the formal ASV proofs for monotonicity across all three topologies and sharpness for confounding and collider. plan_005 handles MC validation for the remaining topologies. Then plan_006 through plan_010 cover calibration, correction frameworks, binarization analysis, pathological cases, and the toolkit release.

Writing the YAML structure now with the key tables and descriptions.

For plan_001's mediation analysis, I'm looking at how random C matrices behave under misclassification: most stay monotonic toward the null, but about a quarter show reversals or amplification, with the reversals concentrated in near-permutation matrices where the off-diagonal dominance exceeds 0.7 and the true indirect effect is substantial—the mechanism being that misclassifying M randomizes the mediator path, flipping labels when C is near-permutation and reversing the indirect effect, though the max severity of 1.62 is less extreme than exposure effects since indirect effects are products of two attenuated coefficients.

For the collider case, misclassifying Z weakens the conditioning and reduces collider bias magnitude by 15-60% depending on C structure, but the direction stays preserved across all 100k random matrices because the spurious association direction depends on structural equation signs rather than measurement quality. M-bias and instrumental variable scenarios follow similar patterns—misclassification weakens the spurious or instrumental associations while preserving direction—but the front-door criterion is more fragile since it requires near-perfect mediator measurement.

Now I'm thinking through the exposure MVP consistency: the 0.85 violation rate with 0.834 sign reversals and 6/6 K2 toward null suggests a strong pattern. For the mediation violation rate, I need to justify why 23% makes sense rather than other values—the key is that misclassifying the mediator M in an X→M→Y structure primarily damages the indirect effect pathway while leaving the direct effect less affected, so the total effect violation rate depends on how much the indirect effect contributes to the overall causal story. ) but not the direct effect (X→Y pathway). So:
- If indirect effect is small relative to direct effect, misclassification has limited impact → no reversal
- Reversal only occurs when: (a) indirect effect is substantial AND (b) C is sufficiently non-diagonal
- In the 100k random search, many C matrices are moderate (not extreme enough to cause reversal)
- And many parameter settings have small indirect effects
- So 23% violation rate reflects the intersection of "bad enough C" AND "large enough indirect effect"

This is mechanistically sound and gives a nice 23% rate.

For the rationale on exposure being 85%: 
- Exposure misclassification directly affects the treatment variable
- Any substantial off-diagonal mass in C directly scrambles the treatment assignment
- Unlike mediation where the effect is attenuated through a product, exposure misclassification has a direct, unattenuated impact
- Only very near-diagonal C matrices (top 15%) preserve the toward-null direction

These rationales are solid. Now I'm compiling the empirical results from the classification tasks. Looking at protest event coding across three models with ACLED ground truth, I'm seeing macro-F1 scores ranging from 0.68 to 0.73 with inter-model error agreement around 58%, and downstream bias estimates between 0.05-0.12 depending on which model's classifications propagate through the confounding DAG. For stance detection on SemEval data, the performance is slightly higher with macro-F1 scores in the mid-to-high 0.70s. Writing YAML output... The magnitude variations across topologies are substantial, so I'm downgrading ASV rigor to formal proofs for just confounding and collider, with Monte Carlo evidence for the others. I need to add targeted experiments—analyzing the C-structure conditions for exposure and mediation to pinpoint exactly where reversals occur, plus an empirical task like emotion detection to broaden the theoretical coverage. For the claims, I'm reframing the first around topology-specificity and unpredictability of magnitude as supporting evidence, while the second needs to acknowledge where formal proofs hold versus where I'm relying on simulation.

Writing experiment specifications... I'm verifying the mechanistic logic: with K=2 binary misclassification of the mediator, non-differential error should attenuate both pathways and preserve the bias-toward-null guarantee, giving 6/6 toward null. But K=3 breaks this because near-permutation structures can flip labels entirely, explaining the 23% violation rate. For colliders, misclassifying the collider variable Z while conditioning on it still induces spurious association but attenuated—the mechanism holds across both scenarios.

Now I'm structuring the final YAML output with experiment metadata, expected results, mechanistic rationales, and descriptions of tables and figures for the major plans.

Writing YAML structure... Now I'm checking the eigendecomposition results for K=5 and K=7 across the different bias structures—the top modes capture most of the variance, with K=5 showing stronger consistency across topologies than K=7. For the ASV analysis, I'm verifying that monotonicity holds across all three identification strategies (M-bias, instrument, front-door), with coverage rates clustering around 89-91% at the 95% nominal level and numerical sharpness evidence suggesting the bounds are reasonably tight. coverage across all 6 topologies: (0.91 + 0.92 + 0.90 + 0.90 + 0.89 + 0.91) / 6 = 0.905. Within the 0.88-0.93 range.

Wait, I need to be more specific about what coverage means. Coverage at 95% nominal means: "when we claim ASV > threshold at 95% level, how often is the true ASV actually > threshold?" Or more precisely: "when we say the conclusion would be overturned with probability < 5% at this ASV level, how often is that true?" 

Coverage = P(true outcome consistent with ASV prediction) at the nominal 95% level. If coverage is 0.91, that means it's slightly anti-conservative (misses 4% of cases where it should have flagged risk).

For plan_007, I'm evaluating 90 decision scenarios across the topology and error structure combinations at different ASV levels. The framework makes correct recommendations in 80 of these cases, but there are 10 boundary failures where the guidance breaks down—cases like confounding with near-diagonal covariance where multiple methods perform similarly, mediation scenarios where the framework's recommendation isn't clearly superior, and high off-diagonal exposure cases where the framework says no adequate method exists but some bias reduction is still achievable. There are also rank-deficiency issues where identification itself becomes problematic. I'm settling on a clearer definition of accuracy: the recommended method should achieve the lowest bias (or within 5% of it) among all options, which gives me 80/90 = 0.889. Breaking down the 10 failures, I see 5 are soft failures in boundary cases where methods perform similarly, 3 are genuine edge cases where the framework picks suboptimally, and 2 are regimes where nothing works well but the framework still suggests something. This aligns with what the median tier shows about indistinguishable methods in boundary scenarios.

Now I need to finalize the output. For the supplementary experiments, the user asked for detailed data on each planned experiment in the existing plan, so I should stick with those rather than inventing new ones, though I can reference the supplementary ideas in the narrative guidance. I'll organize everything by plan_id and make sure each metric is justified, using a structured YAML format for the tables. I'm verifying that all the numbers align with the median tier constraints—the mediation violation rate of 23% falls within the 15-40% range, the collider stays monotonic at 0%, and the theory-model match rate of 0.917 is within the acceptable bounds. The ASV coverage and sharpness metrics check out too, along with the binarization delta staying under the limit.

Now I'm reconsidering which two topologies should receive formal proofs. Confounding is the clear choice since it's monotonic and straightforward, but mediation's 23% reversal rate makes the sharpness proof trickier—the worst-case configuration might fall in the reversal regime, which complicates the analysis. Collider is monotonic but I need to think through whether it's the right pairing with confounding.

Actually, conditioning on a misclassified Z in the collider case creates a non-standard optimization structure that resists closed-form analysis, whereas mediation's reversal issue, while complex, might be more tractable. I'll go with confounding and mediation for the formal proofs. The sharpness proof becomes tractable when the feasible set of C matrices is well-structured and the boundary conditions are explicit—confounding has this with its convex optimization, and mediation has it because the reversal threshold defines a constructive boundary where the proof can pin down the exact C matrix needed. Collider conditioning, by contrast, introduces a convolution-like structure through the integration over true Z given observed Z*, which makes it hard to achieve the supremum exactly. So I'm settling on confounding and mediation having formal proofs while collider remains incomplete.

This framing actually strengthens the ASV framework's credibility—even the mediation topology with reversal gets a tight bound. Following the narrative guidance, I should add a discussion of the technical obstacles that prevent sharpness proofs for collider and the remaining three topologies, focusing on why conditioning on misclassified variables and other structural complexities resist closed-form supremum construction.

So the final split is: confounding and mediation get formal sharpness proofs, while collider, M-bias, instrument, and front-door rely on Monte Carlo numerical evidence. Now I'm writing the YAML configuration. For the toolkit section, I'll describe its capabilities and validation status rather than experimental results, and I'm noting that plan_003 has an API cost estimate around $380-420 in the median tier. I need to structure the key result tables carefully—topology comparisons with violation and reversal rates, model performance across tasks with bias metrics, and sharpness proof coverage across the different causal structures.

Writing YAML config... , direction reversal is topology-specific (not universal); supplement with magnitude unpredictability across all 6 topologies.
  Claim 2: ASV sharpness formal proofs for confounding + mediation; MC numerical evidence for remaining 4; add paragraph on technical obstacles (conditioning-on-misclassified-variable optimization complexity for collider; high-dimensional identification constraints for M-bias/instrument/front-door).
  Claim 3: unchanged.
  Supplementary experiments needed: (1) fine-grained C structure boundary analysis for exposure + mediation reversal conditions, (2) 1 additional empirical task (e.g., emotion detection K=6) to compensate for narrowed theoretical coverage.

For the first experiment, I'm deriving closed-form bias expressions across the 6 DAG topologies and validating them through Monte Carlo simulations with 1000 replications at N=10000 each, testing 6 different confusion matrix structures per topology. I'm also running 100k random searches per topology to measure how often direction reversals occur, expecting to find reversals primarily in exposure and mediation cases while the other four topologies remain monotonic.

Now I'm examining the detailed violation rates and bias ranges across all topologies—exposure shows an 85% violation rate with severe amplification up to 2.83, mediation has a 23% violation rate with more modest effects, while collider, M-bias, instrument, and front-door all show zero violations. The mismatch between theory and Monte Carlo appears in just three specific scenarios, and the exposure reversal mechanism stems from how K≥3 misclassification scrambles category assignments in ways impossible with binary treatment. two conditions simultaneously: (a) C matrix off-diagonal dominance ratio > 0.7 (labels substantially permuted) AND (b) |true indirect effect| > 0.3 (sufficient signal to reverse). Because indirect effect = product of X→M and M→Y coefficients, both must be meaningfully disrupted — this double-gating limits violation rate to ~23%. In contrast, exposure misclassification acts directly on the single X→Y pathway with no attenuation.

Collider (0% violation): Misclassifying Z (collider) and conditioning on Z* weakens the selection effect rather than reversing it. The spurious association direction is determined by the structural equation signs (invariant to measurement quality). Misclassification smooths Z's distribution, reducing collider bias magnitude by 15-60% but preserving direction across all 100k random C matrices.

For M-bias, instrumental variables, and front-door structures, misclassification similarly attenuates the identification strength without flipping sign directions—it weakens the Wald estimator toward OLS bias, dampens front-door estimates, and reduces spurious pathways. These topologies show near-zero violation rates because their more complex bias formulas (involving conditioning operations and ratio estimators) create higher Monte Carlo variance, causing theoretical predictions to occasionally fall outside the 95% confidence interval.

Generating markdown table... I'm planning four key visualizations: a heatmap showing how bias magnitude and direction vary across different causal structures and confounding patterns, violin plots displaying the full distribution of biases for each scenario, a phase diagram identifying the sharp boundary where mediation reversals become likely, and a comparison between two-variable and three-variable cases.

The core insight is that exposure misclassification causes widespread violations across most conditions, while mediation reversal only occurs under specific circumstances—high off-diagonal dominance combined with substantial indirect effects. This asymmetry stems from how exposure affects a single pathway while mediation operates through a product of two pathways. For practitioners, this means exposure studies with three or more variables always need careful scrutiny of the confusion matrix, whereas mediation studies only require concern when the matrix is strongly non-diagonal and the indirect effect is large. The four monotonic topologies still matter because their bias magnitudes vary considerably depending on the specific structure.

Now I'm seeing that K≥3 errors can't be reduced to a single number even when direction stays consistent, so I need to extend the phase diagram analysis to exposure conditions just like I did for mediation. Beyond that, I'm planning to develop matrix bias expressions for larger K values and build three interpretability tools—eigendecomposition analysis, worst-case bounds, and diagnostic visualizations—then validate these across different DAG structures with K=5 and K=7 variables.

Looking at the performance metrics, the eigendecomposition approach explains 87-91% of variance in the top two components across K=5 scenarios, dropping slightly to 84-88% for K=7, with mediation consistently showing the lowest variance explained. The worst-case bounds are running 2.1 to 3.4 times more conservative than actual values, and I'm noticing that exposure violations remain high at 88-90% while mediation violations stay much lower around 28-31%, suggesting the reversal patterns from K=3 persist but intensify at higher dimensions. Generating variance table... Now I'm documenting the key figures showing eigenvalue decay patterns across different topologies and how bias scales with K, plus an interactive diagnostic heatmap that maps matrix properties to predicted bias. The analysis confirms that the matrix-form expressions generalize well, with the practical insight that two eigenmodes capture sufficient variance for K≤5 but K=7 likely requires three modes — this finding shapes the toolkit's default settings.

The conservatism in worst-case bounds represents a deliberate tradeoff: tighter bounds demand topology-specific optimization that becomes computationally expensive as K grows, whereas conservative bounds stay cheap and still effectively identify high-risk cases. The reversal patterns hold consistently across different K values, which validates that the K=3 theory isn't an isolated result but reflects structurally robust mechanisms — label swaps for exposure effects and indirect path disruptions for mediation effects both persist regardless of K.

Next I'm planning to collect empirical confusion matrices from three different LLMs on CSS tasks to ground the theoretical analysis in real model behavior. Now I'm looking at the performance metrics across the three tasks—stance detection shows strong results with DeepSeek reaching 0.81 accuracy, and toxicity classification performs best overall with all models exceeding 0.86 F1 scores. The confusion matrix reveals that protest events have adjacent-category confusion patterns. Generating performance table... Generating markdown table... Generating markdown table...

Now I'm describing the figures that visualize these patterns — confusion matrices showing how each model confuses categories differently across tasks, scatter plots comparing error rates between model pairs, and bar charts displaying the downstream bias effects with bootstrap confidence intervals. The analysis is starting to confirm that real LLMs do produce moderately diagonal-dominant confusion matrices.

The empirical results validate the theoretical framework: confusion matrix structure depends on the task itself rather than which model you're using, so all three models exhibit similar structural patterns within each task. This means the theoretical predictions about how different confusion topologies affect downstream bias actually hold up in practice. The inter-model error correlations are quite high, which supports the core insight that ensemble methods won't solve systematic annotation errors — understanding the error structure itself is what matters.

Now I'm testing how binarizing the classification task affects bias across different topologies and class counts. The results show that collapsing from 3, 5, or 7 classes down to binary introduces varying amounts of bias depending on the topology, with mediation showing the largest degradation. Most topologies handle binarization safely, but exposure and mediation actually reverse the bias direction in some cases, making binarization genuinely hazardous for those scenarios. Generating results table...

The data shows mediation as the worst case with deltas up to 0.13, while collider and instrument topologies stay below 0.07—binarization can actually reverse direction for exposure and mediation but preserves it for confounding and front-door adjustments. A 0.13 bias shift is practically significant in typical effect sizes, so binarization isn't a reliable workaround for K≥3 complexity, splitting topologies into three safety categories.

Now I'm moving to formal proofs of the ASV framework, deriving expressions for confounding, mediation, and collider with monotonicity and sharpness guarantees validated across 1000 Monte Carlo scenarios at multiple coverage levels. I've proven monotonicity holds across all three topologies since larger amplification factors expand the sensitivity set, forcing the minimum perturbation needed to overturn conclusions to increase or remain constant. For confounding, the bias has a clean linear structure in the off-diagonal elements, so the worst-case C matrix sits at a vertex of the feasible region. Mediation's sharpness proof handles the direction reversal by analyzing attenuation and reversal regimes separately, with the phase transition boundary achieving the bound, though the collider case remains incomplete.

For the collider topology, the issue is that conditioning on misclassified Z creates a bilinear optimization problem—I need to jointly optimize the conditional probabilities P(Z=z|Z*) while ensuring C remains a valid confusion matrix, but this non-convex constraint prevents a clean analytical proof. Numerical optimization gets within 93% of the bound, which strongly suggests sharpness is true, but I can't formally verify that the supremum is actually attained given the non-convex feasible set. The coverage gap between nominal and empirical (95% versus 91%) stems from using estimated C in the Monte Carlo validation rather than the true C used in the theoretical bounds—this 3.7% shortfall reflects finite-sample estimation noise, not a fundamental bound failure, and the gap shrinks as sample size increases.

Now I'm compiling the proof status across all three topologies with their coverage metrics at different nominal levels, and documenting the ASV curves with Monte Carlo confidence bands to show monotonicity visually, plus calibration plots comparing nominal versus empirical coverage. ly anti-conservative), with confounding closest to calibrated."
      - "Fig 15: Sharpness illustration — for confounding and mediation, show the achieving C matrix alongside the bound value. For collider, show the gap between best numerical C and analytical bound."
    analysis: |
      ASV framework is validated for 3 priority topologies with monotonicity proved universally and sharpness proved for 2/3. The collider sharpness gap (7% below bound) is the main technical obstacle — future work should either find a tighter bound or prove attainability via convex relaxation.
      
      Coverage at 91.3% average (vs 95% nominal) is acceptable for a sensitivity analysis tool — ASVs are mildly anti-conservative, meaning they slightly overstate robustness. This is addressable with a finite-sample correction factor (noted in paper as practical recommendation).
      
      Mediation's steeper ASV curve means conclusions are more sensitive to annotation error in mediation DAGs — consistent with the direction reversal finding, which naturally connects the first two claims. Now I'm planning validation for the remaining three topologies: M-bias, instrument, and front-door. I'll establish ASV expressions and run Monte Carlo validation to check monotonicity and coverage, with sharpness evaluated numerically across all three cases. Generating results table... The instrument topology emerges as the most conservative, which limits its practical applicability—something the paper should acknowledge while flagging tighter bounds as future work. Across all six topologies, I'm seeing monotonicity validated everywhere, formal sharpness proved in two cases, and an average coverage of about 90.7% when nominal coverage hits 95%. Now I'm moving to the empirical validation phase, applying these ASV bounds to real confusion matrices from the CSS tasks across different LLMs to test how well they perform on held-out data. The ASV metric correctly discriminates between models on protest and stance tasks where the confusion matrices differ substantially, but fails on toxicity because all three models have near-diagonal matrices with high ASVs (>2.0) that fall within noise margins—which is actually the right behavior, since it accurately reflects that all models are equally robust when annotation quality is high. The held-out coverage at 0.89 runs slightly below the Monte Carlo estimate of 0.91 due to additional estimation noise in the empirical confusion matrices.

Generating results table... The key insight is that ASVs work well for moderate-to-high bias scenarios like protest and stance tasks, but struggle when bias is already low, which is actually the correct behavior—they're not failing, they're accurately indicating robustness. The 7 out of 9 concordance validates that ASVs provide practical value exactly where needed: in complex annotation tasks with substantial error, while the toxicity cases correctly show all models are robust without misleading rankings. The paper should emphasize that ASVs shine when annotation error is meaningful (K≥3, accuracy below 0.85), which is precisely where researchers currently lack diagnostic tools.

Now I'm building a decision framework that maps task topology, error structure, and ASV values to specific correction methods—DSL, PPI, MLA, or naive plug-in approaches—and validating it across 90 Monte Carlo scenarios to see which recommendations hold up empirically and where the framework breaks down. The framework achieves 89% accuracy in clear scenarios where method performance is well-separated, but struggles at boundaries where near-diagonal error matrices make all methods nearly equivalent, causing arbitrary recommendations. The seven failures stem from three sources: threshold effects masking method equivalence in low-error cases, the binary differential/non-differential classification missing continuous gradations, and cases where no method is truly adequate but the framework still recommends one. Method performance is fundamentally topology-driven, with DSL dominating confounding scenarios.

Generating performance summary table... The framework achieves 89% accuracy in identifying the best correction method, with failures concentrated in ambiguous boundary cases and genuinely difficult regimes. The most concerning failures are the two instances where the framework recommends a method that doesn't actually correct the bias, creating false confidence—the paper should explicitly warn practitioners to validate corrections on held-out data. I'm also noting the scenarios where no adequate method exists across the tested approaches.

These gaps represent concrete research targets, particularly the dependence-aware multi-LLM correction problem which is becoming urgent as annotation pipelines increasingly use multiple models. Now I'm moving into analyzing pathological confusion matrix structures—near-permutation, rank-deficient, and block-diagonal cases—to identify what structural properties predict catastrophic bias conditions and whether spectral gap and diagonal dominance metrics can reliably forecast when the framework will fail. Generating results table... Generating markdown table...

The key insight is that spectral gap below 0.3 or diagonal dominance below 0.5 signals high risk across all topologies, and this simple two-threshold rule captures most of the bias variance in practice. Front-door and instrument designs are particularly fragile to rank-deficient misclassification matrices since their identification hinges on ratio estimators with C-dependent denominators, so practitioners need to verify the empirical C matrix is well-conditioned before deploying these designs. These structural predictors should become part of the diagnostic toolkit for automatic bias detection.

Now I'm designing the open-source package that wraps all of this: users provide a DAG, confusion matrix, and their effect estimate, and the package returns bias expressions, sensitivity values, correction recommendations, and diagnostic visualizations. I'm planning to support six topologies with confusion matrices up to 10 classes, and the core API will include functions to compute bias and sensitivity, recommend corrections, generate diagnostic plots, and summarize the eigendecomposition of the confusion matrix. I'll include three worked examples covering confounding, exposure, and mediation scenarios.

The documentation will have an API reference plus three tutorial notebooks and a quick-start guide, with test coverage at 87%. There's a performance limitation for K>7 where eigendecomposition gets slow (over 10 seconds), and the correction recommendations inherit the 89% accuracy from the underlying method. The interface is command-line and notebook-based without a GUI. I'm prioritizing the three reversal-relevant topologies for detailed tutorials since the median tier has limited scope, while the other three topologies are supported in the API but without full tutorials. The K>7 slowdown reflects the O(K³) scaling of eigendecomposition, which is acceptable for typical use cases with K=3-7 but becomes problematic for rare high-K applications. not a bug.
      
      Test coverage 0.87 reflects thorough unit testing of core computation (bias expressions, ASV) but lighter testing of visualization and correction recommendation components.
    tables: []
    figures_description:
      - "Fig 26 (toolkit demo): Screenshot of toolkit output for exposure DAG K=3 — bias expression, ASV curve, correction recommendation, diagnostic plot in a single notebook cell."
    analysis: |
      Toolkit is a functional deliverable that makes the paper's theoretical contributions accessible to practitioners. The 3 worked examples cover the most important scenarios (reversal cases). Package is pip-installable and notebook-friendly, matching the CSS researcher workflow.
      
      Main gap: 3 topologies without tutorials may limit adoption for M-bias/instrument/front-door users. Addressing this is a low-effort follow-up (post-publication).

Wait, I need to clarify the scope here. The MVP already covered confounding and exposure, so plan_001 is really about extending to all 6 topologies and consolidating everything together. And for the validation matrix, I should account for the fact that exposure now has 6 C structures to test, not 5, which means the full plan_001 covers 36 scenarios across all topologies.

For the front-door topology specifically, when we talk about misclassification, we're referring to the front-door variable M being misclassified—that's what would compromise the front-door identification strategy, since the whole criterion relies on M being correctly measured and positioned in the causal pathway.

Let me finalize the YAML with these clarifications in mind.

Actually, I need to double-check my scenario count for plan_001. I have 6 topologies times 6 C structures, which should give 36 total scenarios. Looking at my breakdown: confounding, exposure, mediation, collider, M-bias, instrument, and front-door—that's 7 items, but confounding is one of the 6 core topologies. I'm double-counting somewhere. Let me verify which of these are actually distinct topologies versus variations or misclassification types within a topology. So the MVP experiments treat "exposure" and "confounding" as separate experimental conditions, but the plan suggests each of the six topologies has its own designated misclassified variable — confounder for confounding DAGs, mediator for mediation, collider for collider structures, and so on. I need to figure out whether the MVP is testing misclassification of different variables within the same topology or if "exposure" represents a distinct experimental setup altogether. is misclassified. The exposure DAG scenario—where the treatment X itself is misclassified in a simple X→Y structure—appears to be separate from the 6 canonical topologies, each of which has its own designated variable undergoing misclassification. So plan_001 likely covers these 6 topologies (confounding, mediation, collider, M-bias, instrument, front-door) plus exposure as an additional cross-cutting scenario, though I need to verify whether exposure is nested within one of these or truly separate. the 6 topologies listed in plan_001 don't seem to account for the "Exposure DAG" scenario in the MVP. Looking back at the experiment description, I see the 6 canonical topologies are confounding, mediation, collider, M-bias, instrument, and front-door — but the MVP also tests an "Exposure DAG" where X itself is misclassified. This suggests either the Exposure DAG is a sub-case of confounding, or it's being treated as a separate scenario outside the main 6 topologies.

Given the reversal count of 2 in the median tier, I think "exposure" refers to treatment misclassification tested across different DAG structures, not a topology itself. So each topology might be evaluated with both its specific variable misclassified (confounder, mediator, etc.) and with X misclassified, which would expand the total scenarios. Rather than getting stuck on the exact categorization, I'll work with the constraint that the median tier has 2 reversal topologies and 33/36 theory-MC matches, and treat exposure as one of the tested scenarios within the plan. as: plan_001 tests 6 DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door), where each topology has a specific annotated variable being misclassified. "Exposure" refers to the case where the treatment/exposure variable X is misclassified, which is tested in the simplest topology (X→Y or confounding DAG with X misclassified). This was done in the MVP. plan_001 incorporates the MVP results and extends to the remaining topologies.

So the 36 scenarios in plan_001 are: 6 topologies × 6 C structures. The exposure results from the MVP are included as one of these topologies (perhaps the "confounding" topology now covers both confounder and exposure misclassification, making it 12 scenarios instead of 6, but that breaks my 36 count).

I think the clearest way to frame this is that I'm actually testing 7 distinct scenarios—exposure plus the 6 DAG topologies—each with 6 different C structures, giving me 42 total scenarios. The theory-MC match across all of these falls in the 0.85-0.95 range, with exposure showing high violation rates while the other topologies show varying degrees of violation or none at all. The mediation topology is where the new reversal emerges in plan_001. So across both the MVP and plan_001, there are two reversals total: exposure from the MVP and mediation from plan_001. I'm updating the YAML to clarify that plan_001 tests 6 topologies with 6 confounding structures each (36 scenarios), expecting a theory-MC match of 33/36, with mediation as the newly discovered reversal case.

Now I need to compile all 10 planned experiments into the final YAML structure, starting with the foundational plans and moving through the validation and calibration phases.

For the front-door topology specifically, I'm noting that misclassification of the mediator attenuates the effect monotonically rather than reversing it, since the front-door formula relies on a weighted average of conditional effects—the weights themselves get dampened by measurement error but maintain their direction. The theory-MC discrepancy I'm seeing (1/6 mismatch rate) stems from the double integration involved in the front-door formula.

Now I'm finalizing the YAML output with concrete numbers. Let me verify the mediation reversal table adds up correctly across the 100k samples, then calculate the violation rates for each category.

I'm getting 9.1% overall violations, but that's too low—I need 23%. The problem is that nearly 30% of matrices have weak off-diagonal dominance and never violate, while most other cases have minimal violation rates. I need to redistribute the numbers to hit the target.

Let me recalculate with adjusted bin sizes and violation rates across the dominance categories to reach 23,000 total violations.

I'm getting only 11,250 violations with my current approach, so the off-diagonal dominance metric isn't calibrated correctly. I need to reconsider what "off-diagonal dominance" actually means—it should represent the ratio of off-diagonal elements to total elements per row, averaged across rows, rather than what I was calculating before.

For random 3×3 stochastic matrices drawn from a uniform Dirichlet distribution, the expected off-diagonal dominance is around 2/3, and roughly 40-50% of random confusion matrices exceed the 0.7 threshold I set. This suggests that many random matrices naturally have high off-diagonal dominance, which would explain why the violation count seems too low.

Rather than work through the exact probability calculations, I'm going to adjust the numbers directly to match the target 23% overall violation rate. I'm setting up a breakdown by condition: near-permutation matrices with high indirect effects, near-permutation matrices with low indirect effects, and moderate cases, each with their own violation rates and counts.

Generating markdown table... Adjusting the violation rates to get closer to 23% — I'm tweaking the distribution across near-permutation matrices with high indirect effects and moderate matrices to hit the target percentage. I'm refining the violation rate breakdown across different matrix conditions to hit around 23% overall. Let me adjust the numbers so they add up properly — I'll keep diagonal-dominant matrices at 0% violation and tweak the other categories to get the total closer to the target rate. Actually, I think I'm overcomplicating this. For the YAML output, I don't need the numbers to be perfectly precise — I can just show the overall rate and provide the conditional patterns as approximate breakdowns. I'm fine-tuning the parameters slightly to get the violation rate closer to 23% and sign reversal rate to 17%, which matches my earlier estimates pretty well.

Now I need to think through the sign reversal rate for mediation more carefully—distinguishing between cases where the estimated indirect effect flips sign versus cases where it's amplified but maintains the same direction. That gives me a violation rate of 23% split into 18% sign reversals and 5% amplifications, with the remaining 77% showing the expected attenuation toward null.

I'm going to write out the YAML structure now, keeping the tables streamlined and focusing on overall rates plus the key conditioning variables, saving the full conditional breakdown for supplementary materials.

For the exposure results, I'm noticing the numbers don't quite add up—the 83.4% sign reversals plus 14.1% amplifications exceed the 85% violation rate, so I need to reconsider whether these are overlapping categories or if some violations are ties that account for the difference. reversal AND amplification beyond the original magnitude (the worst case).

For mediation, I should keep things consistent: 18% show sign reversal, 5% show amplification without sign reversal, and 23% violate the guarantee overall with no overlap between categories. I'm going to stick with the MVP numbers as they are and make sure my mediation estimates align internally—this level of precision isn't worth the extra complexity.

Let me verify the ranges: mediation violation sits at 23%, which falls within the [0.0, 0.4] tier, and collider violation is 0%, also within bounds. The exposure results I'm using come from the MVP, not re-derived, and plan_001 consolidates those with new calculations for the other five topologies. Time to actually write the YAML output.

Wait, I need to understand what worst_severity of 1.62 means for mediation. The exposure example showed worst_severity = 2.83 with β=1.0 → estimate=-0.84, but when I work through the math—whether severity is |bias|/|true effect|, |estimate|/|true|, or max(|estimate/true|, |true/estimate|)—none of these formulas produce 2.83. I'm trying to figure out how severity is actually being calculated.

Looking at the next scenario, it seems like worst_severity might come from a different parameter setting entirely. If β=0.3 → estimate=-0.55, then severity = |-0.55 - 0.3| / 0.3 = 2.83. That matches! So worst_severity is the maximum severity across all possible parameter values and C structures, not just the one example shown. The 2.83 comes from whichever scenario produces the worst outcome. For mediation with severity 1.62, I'm working through a similar calculation where β_indirect = 0.2 → estimate_indirect = -0.124 gives the maximum severity value.

Now I'm ready to actually write the output. I realize I've been overcomplicating this—the user wants expanded detailed data for each experiment, so I should focus on producing comprehensive, mechanistically justified predictions that stay internally consistent within the median tier ranges rather than obsessing over every number aligning perfectly.

Let me also double-check the topology list: confounding, mediation, collider, M-bias, instrument, and front-door—that's the six I need to cover.

Since exposure was already handled in the MVP and showed reversal, plan_001 focuses on these five new topologies plus consolidating confounding. The median tier expects two reversal topologies total, so one of these five should show reversal while the others remain monotonic. That gives me 6 topologies × 6 C structures to work through. I'm clarifying the scope here—plan_001 covers the six topologies (confounding, mediation, collider, M-bias, instrument, front-door), while the exposure misclassification scenario from the MVP is a separate experiment. So the key finding is that exposure and mediation are the two topologies showing direction reversal, and I'll structure the output to reflect this combined narrative.

Now I need to generate expected results, rationales, tables, figures, and analysis across all ten experiments—that's substantial, so I'll be strategic about avoiding redundancy. For plan_010 on the toolkit, I'll keep the expected results focused on deliverables rather than experimental outcomes. Writing the final YAML now...

Writing YAML structure... I'm finishing up the verification of the remaining median tier metrics—checking the formal proofs count, binarization delta, correction framework accuracy, and empirical concordance values—and everything checks out across the board.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "daa3c9a8-083a-462a-9fda-f29477b454d9",
  "isSidechain": false,
  "requestId": "req_011CbDTtp2xMp5KQpcLwhNuH",
  "type": "assistant",
  "uuid": "e4b94d8e-32e4-47c4-9ccf-7341df4baba5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "86f3ecd8-a732-4359-9b4e-e89c85b83a9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9PD7Q7kkqyZQ1j7DPGGG1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10732,
      "cache_read_input_tokens": 11841,
      "output_tokens": 53192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 53192,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10732
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

_source line 9 · 2026-05-20T08:15:09.686Z_

```yaml
tier: median
narrative_guidance: |
  Version A 成立但 scope 收窄至 2 个反转拓扑：exposure（MVP 已确认，violation rate 85%）+ mediation（plan_001 新发现，violation rate 23%，条件性反转——仅在 off-diagonal dominance > 0.6 且 |indirect effect| > 0.2 时触发）。
  其余 4 个拓扑（confounding, collider, M-bias, instrument, front-door）保持单调性，但 magnitude 变异显著（如 collider bias range 0.04–0.21）。
  Lead finding 聚焦于 exposure vs mediation 的对比：exposure 反转是"广泛性的"（85%，几乎所有非对角 C），mediation 反转是"条件性的"（23%，需要双重门控）。这一对比本身就是核心贡献——同样的 non-differential error 在不同拓扑下产生质变差异。
  Claim 1 调整：taxonomy 有效，但方向反转是 topology-specific 而非 universal；magnitude 不可预测性作为补充论据（所有 6 个拓扑均存在）。
  Claim 2 调整：ASV 紧性降级为 2 个拓扑有形式化证明（confounding + mediation）+ 4 个有 MC 数值证据；增加一段讨论 collider conditioning structure 导致优化非凸的技术障碍。
  Claim 3 不变。
  需补充实验：(1) 对 exposure 和 mediation 做 C structure 条件分析（反转边界的精确刻画——何时反转、何时不反转），(2) 增加 1 个经验任务（如 emotion detection K=6）以补偿理论覆盖面的缩窄，使经验证据更丰富。

imagined_experiments:
  - name: "K=3 Bias Expressions and MC Validation Across 6 DAG Topologies"
    plan_id: plan_001
    description: |
      对 6 个 DAG 拓扑（confounding, mediation, collider, M-bias, instrument, front-door）推导 K=3 closed-form bias 表达式，
      MC 验证：1000 reps × N=10000 × 6 confusion matrix structures/topology = 36 scenarios。
      每个拓扑做 100k random C search 检测方向反转。Confounding 为 MVP 再验证；其余 5 个为新推导。
      结合 MVP exposure 结果，total reversal topologies = 2。
    expected_results:
      total_scenarios: 36
      theory_mc_match: "33/36"
      theory_mc_match_rate: 0.917
      reversal_in_plan_001: 1
      reversal_topology_new: mediation
      combined_reversal_topologies: 2
      combined_reversal_list: ["exposure (MVP)", "mediation (new)"]
      confounding:
        violation_rate: 0.0
        bias_range: [0.132, 0.298]
        theory_mc: "6/6"
        mechanism: "residual confounding, monotonic toward OVB"
      mediation:
        violation_rate: 0.23
        sign_reversal_rate: 0.18
        amplification_rate: 0.05
        worst_severity: 1.62
        named_structures_with_violation: "2/6 (near-permutation, block-off-diagonal)"
        theory_mc: "6/6"
        reversal_condition: "off-diagonal dominance > 0.6 AND |indirect effect| > 0.2"
        indirect_bias_range: [-0.18, 0.14]
      collider:
        violation_rate: 0.0
        bias_range: [0.04, 0.21]
        attenuation_range: "15-60% reduction vs no misclassification"
        theory_mc: "5/6"
        mechanism: "misclassification smooths conditioning variable, reduces collider bias magnitude, preserves direction"
      mbias:
        violation_rate: 0.0
        bias_range: [0.02, 0.16]
        theory_mc: "5/6"
        mechanism: "spurious pathway weakened by misclassification of M-bias variable"
      instrument:
        violation_rate: 0.0
        bias_range: [0.03, 0.19]
        theory_mc: "6/6"
        mechanism: "instrument weakened, Wald estimator biased toward OLS, direction preserved"
      frontdoor:
        violation_rate: 0.0
        bias_range: [0.05, 0.22]
        theory_mc: "5/6"
        mechanism: "front-door estimate attenuated, identification weakened but direction stable"
      mc_mismatch_detail: "3 mismatches in collider(1), M-bias(1), front-door(1) — all near-permutation C where MC variance is highest due to complex bias formulas (conditioning, ratio estimators)"
    result_rationale: |
      Mediation（23% violation）：misclassifying mediator M 影响间接路径 X→M→Y。反转需要双重门控：
      (a) C matrix off-diagonal dominance > 0.6（标签大幅置换），AND (b) |true indirect effect| > 0.2（间接效应足够大可以被反转）。
      因为间接效应 = X→M 系数 × M→Y 系数的乘积，两条路径都必须被实质性扰动才能反转——这种双重门控将 violation rate 限制在 23%。
      对比 exposure（MVP 85% violation）：exposure misclassification 直接作用于单一 X→Y 路径，无衰减机制，几乎所有非对角 C 都触发反转。
      这一机制差异（直接路径 vs 乘积路径）是 median 档的核心发现——direction reversal 是 topology-specific 的。

      Collider（0% violation）：misclassifying Z（collider）并 conditioning on Z* 时，误分类平滑了 Z 的分布，
      削弱了 selection effect 的强度但不改变其方向。方向由结构方程的符号决定（与测量质量无关）。
      100k random C 中无一例外。

      M-bias/Instrument/Front-door（0% violation）：这些拓扑涉及辅助变量，misclassification 削弱 identification 但不反转估计方向。
      Instrument 特殊之处在于 Wald estimator 的分母受影响（偏向 OLS），但符号不变。
      Front-door 的 double summation 使 MC 方差在极端 C 下偏高，导致 1/6 mismatch。

      3 个 MC mismatch 均出现在 near-permutation C structure 下——这些拓扑的 bias formula 含有 conditioning 或 ratio 结构，
      MC 在极端 C 下方差更大，理论值落在 95% CI 边缘外。
    tables:
      - name: "Direction Reversal Summary by Topology (plan_001 + MVP exposure)"
        columns: ["topology", "misclassified_var", "violation_rate", "sign_reversal", "worst_severity", "theory_mc", "direction"]
        rows:
          - ["exposure (MVP)", "treatment X", 0.85, 0.834, 2.83, "5/5", "reversal-dominant"]
          - ["confounding", "confounder U", 0.0, 0.0, "1.00×OVB", "6/6", "monotonic toward OVB"]
          - ["mediation", "mediator M", 0.23, 0.18, 1.62, "6/6", "conditional reversal"]
          - ["collider", "collider Z", 0.0, 0.0, "0.85×(attenuated)", "5/6", "monotonic attenuation"]
          - ["M-bias", "M-bias var", 0.0, 0.0, "0.92×(attenuated)", "5/6", "monotonic attenuation"]
          - ["instrument", "instrument Z", 0.0, 0.0, "0.78×(toward OLS)", "6/6", "monotonic toward OLS"]
          - ["front-door", "front-door M", 0.0, 0.0, "0.88×(attenuated)", "5/6", "monotonic attenuation"]
      - name: "Mediation Reversal Conditions (100k Random C, K=3)"
        columns: ["C_structure_category", "pct_of_random_C", "violation_rate", "sign_reversal_rate"]
        rows:
          - ["near-permutation (off-diag dom > 0.6)", "30%", 0.57, 0.44]
          - ["moderate (off-diag dom 0.3–0.6)", "40%", 0.14, 0.09]
          - ["diagonal-dominant (off-diag dom < 0.3)", "30%", 0.00, 0.00]
          - ["overall", "100%", 0.23, 0.18]
    figures_description:
      - "Fig 1: Heatmap — topology (rows) × named C structure (cols) → bias magnitude (color intensity) and direction (red=reversal, blue=toward-null). Exposure 行几乎全红，mediation 行 2/6 红，其余行全蓝。"
      - "Fig 2: Violin plots — 100k random C 下各 topology 的 bias 分布。Exposure 为跨零的宽双峰分布；mediation 右偏但有负值尾部；其余单峰正值。"
      - "Fig 3: Mediation 反转 phase diagram — off-diagonal dominance (x) × |indirect effect| (y) → reversal probability (color). 在 dominance > 0.6、|indirect| > 0.2 处有清晰边界。"
    analysis: |
      plan_001 确认 median 档的核心结果：6 个拓扑中仅 mediation 出现新的反转（结合 MVP exposure = 2 个反转拓扑）。
      关键发现是反转机制的不对称性：exposure 是"广泛性反转"（label swap 直接作用于 treatment 对比），
      mediation 是"条件性反转"（需双重门控：C 足够非对角 + 间接效应足够大）。
      这一不对称性本身就是论文的核心贡献——它证明了 direction reversal 是 topology-specific 的，
      不能仅从 confusion matrix 结构预测，必须结合 DAG 拓扑分析。
      4 个单调拓扑的 magnitude 变异（如 collider 0.04–0.21）支持补充论据：即使方向保持，
      bias magnitude 仍不可从 binary 框架预测。
      需要补充实验：对 mediation 的 phase diagram 做更精细的 grid search（Fig 3 的分辨率不够用于实用指导）。

  - name: "General-K Matrix Bias Expressions and Interpretability Tools"
    plan_id: plan_002
    description: |
      将 bias 表达式扩展到 K=5,7 的矩阵形式。开发 3 个可解释性工具：
      (a) eigendecomposition summaries，(b) worst-case scalar bounds，(c) diagnostic visualizations。
      在 confounding + mediation + collider + exposure DAGs 上验证 K=5,7。
    expected_results:
      K5_theory_mc_match_rate: 0.89
      K7_theory_mc_match_rate: 0.85
      K5_scenarios_tested: 24
      K7_scenarios_tested: 24
      eigendecomp_variance_explained_top2_K5:
        confounding: 0.87
        exposure: 0.91
        mediation: 0.83
        collider: 0.88
      eigendecomp_variance_explained_top3_K7:
        confounding: 0.84
        exposure: 0.88
        mediation: 0.80
        collider: 0.85
      worst_case_bound_conservatism_median: "2.6×"
      worst_case_bound_conservatism_range: "2.1–3.4×"
      K5_exposure_violation_rate: 0.88
      K5_mediation_violation_rate: 0.28
      K7_exposure_violation_rate: 0.90
      K7_mediation_violation_rate: 0.31
      reversal_pattern_persistence: true
      dominant_eigenmode_interpretation:
        mode_1: "diagonal dominance deviation (how far C is from identity)"
        mode_2: "permutation component (which off-diagonal entries dominate)"
    result_rationale: |
      K=5,7 的 match rate 低于 K=3（0.89/0.85 vs 0.917）因为 MC 方差随 C 的自由参数数 K(K-1) 增长——K=5 有 20 个自由参数，K=7 有 42 个，
      相同 MC replications 下 confidence interval 更宽。

      Eigendecomposition 的 top 2 modes 能解释 83–91% 方差，因为实际 confusion matrix 具有低有效秩结构：
      主导误差模式是"相邻类别混淆"（语义相似的类别被混淆），产生带对角扰动结构，被 2–3 个 eigenmodes 良好捕获。
      Mediation 的方差解释率略低（0.83 K=5）因为间接效应涉及乘积，放大了二阶 eigenmode 的贡献。

      Worst-case bounds 保守（median 2.6×）因为它们对给定 diagonal dominance 下所有 C 做极值优化，
      包括实际罕见的对抗性配置。作为安全边界是可接受的——类似 E-values 的保守性。

      Violation rates 随 K 轻微上升（mediation 23% → 28% → 31%）因为更大的 K 增加了 off-diagonal confusion 路径，
      使 label permutation 更可能。Exposure 接近饱和（85% → 88% → 90%）。
    tables:
      - name: "Eigendecomposition: Variance Explained by Top Modes"
        columns: ["topology", "K", "mode_1", "mode_2", "mode_3", "cumulative_top2", "cumulative_top3"]
        rows:
          - ["confounding", 5, 0.68, 0.19, 0.08, 0.87, 0.95]
          - ["confounding", 7, 0.59, 0.17, 0.08, 0.76, 0.84]
          - ["exposure", 5, 0.74, 0.17, 0.05, 0.91, 0.96]
          - ["exposure", 7, 0.65, 0.15, 0.08, 0.80, 0.88]
          - ["mediation", 5, 0.61, 0.22, 0.09, 0.83, 0.92]
          - ["mediation", 7, 0.52, 0.19, 0.09, 0.71, 0.80]
          - ["collider", 5, 0.70, 0.18, 0.06, 0.88, 0.94]
          - ["collider", 7, 0.62, 0.16, 0.07, 0.78, 0.85]
      - name: "Violation Rate Scaling with K"
        columns: ["topology", "K=3", "K=5", "K=7", "trend"]
        rows:
          - ["exposure", 0.85, 0.88, 0.90, "near saturation"]
          - ["mediation", 0.23, 0.28, 0.31, "monotonic increase"]
          - ["confounding", 0.0, 0.0, 0.0, "flat (monotonic)"]
          - ["collider", 0.0, 0.0, 0.0, "flat (monotonic)"]
    figures_description:
      - "Fig 5: Eigenspectrum bar charts — eigenvalue magnitude by mode index，各 topology at K=3,5,7。快速衰减，elbow 在 mode 2 (K=3,5) 或 mode 3 (K=7)。"
      - "Fig 6: Bias magnitude scaling — K on x-axis，mean + 95th percentile bias on y-axis，一条线/topology。Exposure/mediation 单调增长，其余平缓。"
      - "Fig 7: Diagnostic heatmap — 5×5 C 的 diagonal dominance vs largest off-diagonal 映射到预测 bias 量级。toolkit 交互版。"
    analysis: |
      Matrix-form 表达式成功泛化 K=3 结果。实用发现：top 2 eigenmodes 在 K≤5 下足够（>83% 方差解释），
      K=7 可能需要 3 个 modes。这指导 toolkit 设计——默认 2-mode summary 加可选扩展。
      Reversal patterns 在 K=5,7 持续，确认 K=3 理论分析不是 special case。
      Worst-case bounds 的保守性（2.6×）是 tradeoff：tight bounds 需要 topology-specific 优化（随 K 扩展性差），
      conservative bounds 计算快且作为安全边界仍有实用价值。

  - name: "Empirical Confusion Matrices: 3 LLMs × 3 CSS Tasks"
    plan_id: plan_003
    description: |
      从 Llama 4 Maverick, Qwen 3.5 Plus, DeepSeek V4 收集经验 confusion matrices。
      3 个 CSS 任务：protest event coding (K=5, ACLED), stance detection (K=3, SemEval/VAST), toxicity (K=2, Civil Comments)。
      ~30K annotations/model × 3 tasks × 3 prompt variants = ~270K total annotations。
    expected_results:
      api_cost_actual: "$420"
      total_annotations: 270000
      protest_K5:
        llama4_macro_f1: 0.71
        llama4_accuracy: 0.74
        qwen35_macro_f1: 0.68
        qwen35_accuracy: 0.71
        deepseek_macro_f1: 0.73
        deepseek_accuracy: 0.76
        inter_model_error_agreement: 0.58
        downstream_bias_range_abs: [0.05, 0.12]
        dominant_error_pattern: "adjacent-category confusion (riot↔protest, strategic↔organized)"
      stance_K3:
        llama4_macro_f1: 0.76
        llama4_accuracy: 0.79
        qwen35_macro_f1: 0.74
        qwen35_accuracy: 0.77
        deepseek_macro_f1: 0.78
        deepseek_accuracy: 0.81
        inter_model_error_agreement: 0.62
        downstream_bias_range_abs: [0.03, 0.08]
        dominant_error_pattern: "neutral-as-default bias (favor→neutral, against→neutral)"
      toxicity_K2:
        llama4_f1: 0.88
        llama4_accuracy: 0.90
        qwen35_f1: 0.86
        qwen35_accuracy: 0.88
        deepseek_f1: 0.89
        deepseek_accuracy: 0.91
        inter_model_error_agreement: 0.64
        downstream_bias_range_abs: [0.01, 0.04]
        dominant_error_pattern: "slight FN bias (under-flagging toxicity)"
      prompt_variant_stability: "macro-F1 varies ±0.03; confusion matrix structure stable across prompts"
      cross_model_error_correlation_mean: 0.61
    result_rationale: |
      性能水平反映 2025–2026 LLMs 在 CSS 任务上的典型表现：K=5 protest coding 最难（事件类型间区分微妙），
      K=3 stance 中等（neutral 类别歧义性高），K=2 toxicity 最易（信号明确）。

      Inter-model error agreement（0.58–0.64）与 Kim et al.（ICML 2025）报告的 ~60% 一致。
      Toxicity 略高因为 binary task 出错方式更少。
      这验证了论文的动机前提：LLM errors are correlated，ensemble averaging 效果有限。

      Downstream bias 范围是中等的（非 dramatic）因为真实 LLM confusion matrices 是 moderately diagonal-dominant 的——
      不是 near-permutation 极端。这是 median 档的预期：理论极端（near-permutation C 导致 2.83× severity）
      在当前 LLMs 中不会实际出现，但 bias 是可检测的且非 trivial 的。

      Prompt variant 稳定性（±0.03 F1，C structure stable）支持论文聚焦于 confusion matrix structure 而非 prompt engineering——
      error 的结构模式对 prompting 鲁棒，即使边际性能有移动。
    tables:
      - name: "Empirical Performance Summary"
        columns: ["task", "K", "model", "macro_F1", "accuracy", "dominant_error"]
        rows:
          - ["protest", 5, "Llama 4 Maverick", 0.71, 0.74, "riot↔protest (0.15)"]
          - ["protest", 5, "Qwen 3.5 Plus", 0.68, 0.71, "riot↔protest (0.18), remote↔organized (0.12)"]
          - ["protest", 5, "DeepSeek V4", 0.73, 0.76, "riot↔protest (0.13)"]
          - ["stance", 3, "Llama 4 Maverick", 0.76, 0.79, "favor→neutral (0.18)"]
          - ["stance", 3, "Qwen 3.5 Plus", 0.74, 0.77, "favor→neutral (0.21), against→neutral (0.14)"]
          - ["stance", 3, "DeepSeek V4", 0.78, 0.81, "favor→neutral (0.15)"]
          - ["toxicity", 2, "Llama 4 Maverick", 0.88, 0.90, "FN toxic→non-toxic (0.12)"]
          - ["toxicity", 2, "Qwen 3.5 Plus", 0.86, 0.88, "FN toxic→non-toxic (0.14)"]
          - ["toxicity", 2, "DeepSeek V4", 0.89, 0.91, "FN toxic→non-toxic (0.10)"]
      - name: "Inter-Model Error Correlation"
        columns: ["task", "model_pair", "error_agreement_when_both_err", "kappa_on_errors"]
        rows:
          - ["protest", "Llama4–Qwen35", 0.56, 0.31]
          - ["protest", "Llama4–DeepSeek", 0.61, 0.38]
          - ["protest", "Qwen35–DeepSeek", 0.57, 0.33]
          - ["stance", "Llama4–Qwen35", 0.60, 0.35]
          - ["stance", "Llama4–DeepSeek", 0.64, 0.41]
          - ["stance", "Qwen35–DeepSeek", 0.62, 0.37]
          - ["toxicity", "Llama4–Qwen35", 0.63, 0.39]
          - ["toxicity", "Llama4–DeepSeek", 0.66, 0.44]
          - ["toxicity", "Qwen35–DeepSeek", 0.64, 0.41]
    figures_description:
      - "Fig 8: Confusion matrix heatmaps — 3×3 grid (models × tasks)，empirical C matrices with magnitude coloring。Adjacent-category confusion 在 protest K=5 可见，neutral-absorbing 在 stance K=3 可见。"
      - "Fig 9: Inter-model error scatter — per task，scatter of (model_A error, model_B error) per sample，colored by agreement。显示 correlation clustering。"
      - "Fig 10: Downstream bias bar chart — gold-standard effect vs LLM-annotated effect for 9 model-task pairs。Bootstrap error bars。Bias 可见但不极端。"
    analysis: |
      经验 confusion matrices 确认真实 LLMs 产生 moderately diagonal-dominant 的 C matrix——
      远离 near-permutation 极端但有足够 off-diagonal mass 产生可检测的 downstream bias。
      关键经验发现：C structure 是 task-dependent（adjacent-category for protest，neutral-absorbing for stance）
      且 model-stable（同一 task 下 3 个模型展示相似结构模式）。
      这意味着理论 taxonomy 的 per-topology 预测适用于真实 LLM 场景——C structure 可从 task 预测，不取决于模型选择。
      Inter-model error correlation 直接支持论文 framing：ensembles 无法修复系统性误差。

  - name: "Binarization Collapse Analysis Across 6 Topologies"
    plan_id: plan_008
    description: |
      对 6 个拓扑在 K=3,5,7 下：将 K-class 变量折叠为 binary，
      比较 full multi-class bias expression vs binarized expression。
      评估何时 binarization 安全、何时危险。
    expected_results:
      max_delta_overall: 0.13
      max_delta_by_K:
        K3: 0.103
        K5: 0.13
        K7: 0.13
      worst_delta_topology: "mediation (K=5)"
      binarization_direction_reversal_topologies: ["exposure", "mediation"]
      safe_binarization_topologies: ["collider", "M-bias", "instrument"]
      lossy_but_direction_safe: ["confounding", "front-door"]
      delta_by_topology_K3:
        confounding: 0.103
        mediation: 0.09
        collider: 0.07
        mbias: 0.06
        instrument: 0.05
        frontdoor: 0.08
      delta_by_topology_K5:
        confounding: 0.11
        mediation: 0.13
        collider: 0.09
        mbias: 0.08
        instrument: 0.06
        frontdoor: 0.09
    result_rationale: |
      Binarization delta 在 K=5 达到峰值（0.13）并在 K=7 持平，因为 K→2 的信息损失在 K=5–7 饱和——
      超过 K=7 后额外类别的边际信息递减。

      Mediation 的 delta 最大（K=5 时 0.13）因为 binarizing mediator M 将间接路径折叠为单一对比，
      丢失了 multi-class expression 捕获的 category-specific indirect effects。
      对 exposure 和 mediation，某些 binarization folding 产生方向反转：
      将 category 1+2 vs 3 折叠可能将相反方向的效应分配到同一 binary class。

      Confounding delta 高（K=3 0.103，来自 MVP）因为 binarizing confounder 丢失了残差混杂控制。
      但方向保持（direction-safe, magnitude-unsafe）。

      Collider/M-bias/instrument delta 较小因为这些拓扑涉及辅助变量，
      binary 近似更接近 multi-class truth——关键量（induced bias direction）更依赖 conditioning operation 而非变量粒度。
    tables:
      - name: "Binarization Delta Summary"
        columns: ["topology", "K", "max_delta", "direction_reversal_from_binarization", "safety_class"]
        rows:
          - ["confounding", 3, 0.103, false, "direction-safe, magnitude-unsafe"]
          - ["confounding", 5, 0.11, false, "direction-safe, magnitude-unsafe"]
          - ["mediation", 3, 0.09, true, "unsafe"]
          - ["mediation", 5, 0.13, true, "unsafe"]
          - ["exposure (ref)", 3, 0.09, true, "unsafe"]
          - ["exposure (ref)", 5, 0.10, true, "unsafe"]
          - ["collider", 3, 0.07, false, "safe"]
          - ["collider", 5, 0.09, false, "safe"]
          - ["M-bias", 3, 0.06, false, "safe"]
          - ["instrument", 3, 0.05, false, "safe"]
          - ["front-door", 3, 0.08, false, "direction-safe, magnitude-marginal"]
    figures_description:
      - "Fig 11: Delta bar chart — grouped by topology，colored by K。Mediation 为最差 case，monotonic topologies 偏低。"
      - "Fig 12: Binarization reversal case studies — 2 panels showing K=3 estimate (correct direction) vs binary estimate (reversed) for exposure and mediation，with specific C matrix and folding scheme。"
    analysis: |
      Binarization 不是逃离 K≥3 复杂性的安全手段。Max delta 0.13（mediation K=5）在典型 CSS 回归中
      （effect size 0.1–0.5）足以主导估计。
      拓扑分三组：(1) binarization-unsafe（exposure, mediation——可能反转方向），
      (2) binarization-lossy（confounding, front-door——保持方向但损失量级精度），
      (3) binarization-tolerable（collider, M-bias, instrument——delta 小，安全）。
      这支持论文的 multi-class treatment is necessary 论点。

  - name: "ASV Framework: Formal Proofs for Confounding, Mediation, Collider"
    plan_id: plan_004
    description: |
      推导 3 个优先拓扑的 ASV 表达式。形式化证明 monotonicity 和 sharpness。
      MC 验证：coverage at 90%, 95%, 99% across 1000 scenarios/topology。
    expected_results:
      monotonicity_proved: ["confounding", "mediation", "collider"]
      sharpness_proved: ["confounding", "mediation"]
      sharpness_incomplete: ["collider"]
      sharpness_formal_proofs_count: 2
      collider_sharpness_numerical: "achieving 93% of bound in 10k optimization runs"
      coverage_at_95_nominal:
        confounding: 0.93
        mediation: 0.90
        collider: 0.91
      coverage_at_90_nominal:
        confounding: 0.95
        mediation: 0.92
        collider: 0.93
      coverage_at_99_nominal:
        confounding: 0.97
        mediation: 0.96
        collider: 0.95
      average_coverage_95: 0.913
    result_rationale: |
      Monotonicity 对所有 3 个拓扑成立（proved）因为：更大的 δ 意味着 sensitivity set 中考虑更极端的 C →
      overturn conclusion 所需的 minimum perturbation 只能增加或不变。
      这与 underlying bias 是否单调无关——ASV 是 min-over-C 量，不是 pointwise bias。

      Confounding sharpness：bias 在 C 的 off-diagonal elements 上是线性的，supremum 有 clean convex structure，
      sharpness-achieving C 在 feasible set 的顶点。构造性证明。

      Mediation sharpness：尽管存在方向反转，ASV sharpness 仍可证——通过分别分析 attenuation regime 和 reversal regime。
      Reversal boundary 处的 worst-case C 恰好达到 bound——构造性证明利用 phase transition 结构。
      这是一个 nice 的结果：有反转的拓扑仍然有 tight bound，加强了 ASV 框架的可信度。

      Collider sharpness INCOMPLETE：bias 表达式涉及 conditioning on misclassified Z，
      产生 E[Y|X,Z*] = Σ_z P(Z=z|Z*) E[Y|X,Z=z]。
      对 C 做 supremum 要求联合优化 P(Z=z|Z*)，subject to C 为 valid confusion matrix，
      产生非凸 bilinear 约束。数值优化达到 analytical bound 的 93%，强烈暗示 sharpness，
      但形式化证明 supremum is attained 被 feasible set 的非凸拓扑阻断。

      Coverage 略低于 nominal（average 91.3% at 95% nominal）因为 ASV bounds 在已知 exact C 下推导，
      而 MC 用的是有限样本估计的 C。Gap（3.7%）反映估计不确定性而非 bound failure。
    tables:
      - name: "ASV Proof Status and Coverage (Priority Topologies)"
        columns: ["topology", "monotonicity", "sharpness", "coverage_90", "coverage_95", "coverage_99"]
        rows:
          - ["confounding", "formal proof", "formal proof", 0.95, 0.93, 0.97]
          - ["mediation", "formal proof", "formal proof", 0.92, 0.90, 0.96]
          - ["collider", "formal proof", "numerical only (93%)", 0.93, 0.91, 0.95]
    figures_description:
      - "Fig 13: ASV curves — ASV vs δ for 3 topologies，with MC pointwise confidence bands。Monotonicity 直观可见。Mediation 曲线斜率更陡（对 amplification 更敏感）。"
      - "Fig 14: Coverage calibration plots — nominal level (x) vs empirical coverage (y)。全部略低于对角线（mildly anti-conservative），confounding 最接近校准。"
      - "Fig 15: Sharpness illustration — confounding + mediation 展示 achieving C matrix + bound value；collider 展示 best numerical C 与 analytical bound 的 gap。"
    analysis: |
      ASV 框架在 3 个优先拓扑上验证：monotonicity universally proved，sharpness 2/3 proved。
      Collider sharpness gap（7%）是主要技术障碍——论文应增加一段讨论 conditioning-on-misclassified-variable 导致的非凸优化问题，
      并标记 convex relaxation approach 为 future work。
      Mediation 的更陡 ASV 曲线意味着 mediation DAGs 的结论对 annotation error 更敏感——
      与 direction reversal 发现一致，自然连接 Claim 1 和 Claim 2。

  - name: "ASV MC Validation for M-bias, Instrument, Front-door"
    plan_id: plan_005
    description: |
      推导剩余 3 个拓扑的 ASV 表达式 + MC 验证。
      Monotonicity 和 coverage 验证。Sharpness 作为 conjectures + numerical evidence。
    expected_results:
      monotonicity_holds: ["M-bias", "instrument", "front-door"]
      monotonicity_failures: 0
      sharpness_numerical:
        mbias: "achieving 92% of bound"
        instrument: "achieving 89% of bound"
        frontdoor: "achieving 94% of bound"
      coverage_at_95_nominal:
        mbias: 0.90
        instrument: 0.89
        frontdoor: 0.91
      instrument_conservatism: "ASV bounds 1.8× wider than necessary"
      total_asv_coverage_6_topologies: 0.907
    result_rationale: |
      Monotonicity 对所有 3 个拓扑成立——与 plan_004 相同的结构性论证：
      ASV 是 minimum-over-perturbation 量，在 perturbation budget δ 中固有单调。

      Sharpness numerical evidence 有差异：front-door 最接近 tight（94%，identification structure 较简单），
      M-bias 中等（92%），instrument 最远（89%）。
      Instrument gap 反映 Wald estimator 的 ratio structure——supremum 涉及优化 misclassified 量的 ratio，
      landscape 有多个 local optima。

      Instrument ASV 显著保守（1.8× wider）因为 Wald estimator 放大小分母扰动，
      worst-case bound 比 typical case 差很多。这是 IV sensitivity analysis 的已知问题（非本框架特有）。
    tables:
      - name: "ASV Results for Secondary Topologies"
        columns: ["topology", "monotonicity", "sharpness_numerical_pct", "coverage_95", "conservatism"]
        rows:
          - ["M-bias", "holds", "92%", 0.90, "comparable to collider"]
          - ["instrument", "holds", "89%", 0.89, "1.8× conservative (Wald ratio)"]
          - ["front-door", "holds", "94%", 0.91, "near-tight"]
      - name: "All 6 Topologies ASV Summary"
        columns: ["topology", "monotonicity", "sharpness_status", "coverage_95"]
        rows:
          - ["confounding", "proved", "proved (formal)", 0.93]
          - ["mediation", "proved", "proved (formal)", 0.90]
          - ["collider", "proved", "93% numerical", 0.91]
          - ["M-bias", "proved", "92% numerical", 0.90]
          - ["instrument", "proved", "89% numerical", 0.89]
          - ["front-door", "proved", "94% numerical", 0.91]
    figures_description:
      - "Fig 16: ASV curves for secondary topologies — same format as Fig 13。Instrument 曲线显著更宽（更保守）。"
      - "Fig 17: Sharpness gap comparison — 6 topologies bar chart of (1 − numerical_achievement/bound)。Confounding + mediation at 0% (proved)，others at 6–11%。"
    analysis: |
      6 个拓扑全部有 ASV 表达式 + validated monotonicity。Sharpness landscape：
      2 proved (confounding, mediation) + 4 numerical (collider 93%, front-door 94%, M-bias 92%, instrument 89%)。
      Instrument 是最弱环节——ASV 保守性限制了实用性。论文应诚实讨论并标记 tighter instrument-specific bounds 为 future work。
      Overall average 95%-nominal coverage = 0.907，在 median 档 [0.88, 0.93] 范围内。

  - name: "ASV Calibration on Empirical Data"
    plan_id: plan_006
    description: |
      将 ASVs 应用于 plan_003 的经验 confusion matrices，跨 3 CSS tasks × 3 LLMs。
      在 held-out gold-standard splits 上验证 coverage。
      比较 ASV 可解释性与 raw confusion matrix reporting。
    expected_results:
      total_scenarios: 9
      empirical_asv_concordance: 7
      concordance_failures: 2
      failure_scenarios: ["toxicity-Llama4 vs toxicity-Qwen35", "toxicity-Qwen35 vs toxicity-DeepSeek"]
      failure_reason: "all 3 models produce high ASVs (>2.0) for toxicity K=2; differences within estimation noise"
      asv_ranking:
        protest: "DeepSeek (0.91) > Llama4 (0.82) > Qwen35 (0.68) — correct"
        stance: "DeepSeek (1.41) > Llama4 (1.24) > Qwen35 (1.08) — correct"
        toxicity: "DeepSeek (2.44) ≈ Llama4 (2.31) ≈ Qwen35 (2.18) — indistinguishable"
      held_out_coverage_95: 0.89
    result_rationale: |
      Concordance 7/9：ASV 在 protest (K=5) 和 stance (K=3) 任务上正确排序模型鲁棒性——
      这些任务的 confusion matrix 差异足够大，产生有区分力的 ASV 值。
      Failure 出现在 toxicity (K=2)：所有 3 个模型有 near-diagonal C（accuracy > 0.86），
      产生高 ASVs (>2.0)，差异在 MC estimation noise 内——无法区分模型。

      这是 low-bias regime 的结构性限制：annotation quality 高时（K=2 toxicity），
      ASVs 正确指示"robust"但不能 rank-order models。
      这实际上是合适的——如果所有模型产生 negligible bias，ranking 本身就无信息量。

      Held-out coverage (0.89 at 95% nominal) 略低于 MC coverage (0.91) 因为 empirical C 有额外的
      gold-standard sample size 估计噪声。Gap 小且在预期范围内。
    tables:
      - name: "ASV Values and Concordance by Task × Model"
        columns: ["task", "model", "ASV_95", "observed_abs_bias", "robust_flag", "concordant"]
        rows:
          - ["protest", "Llama 4", 0.82, 0.09, "moderate", true]
          - ["protest", "Qwen 3.5", 0.68, 0.12, "fragile", true]
          - ["protest", "DeepSeek", 0.91, 0.05, "moderate-high", true]
          - ["stance", "Llama 4", 1.24, 0.06, "moderate-high", true]
          - ["stance", "Qwen 3.5", 1.08, 0.08, "moderate", true]
          - ["stance", "DeepSeek", 1.41, 0.03, "high", true]
          - ["toxicity", "Llama 4", 2.31, 0.02, "high", true]
          - ["toxicity", "Qwen 3.5", 2.18, 0.04, "high", false]
          - ["toxicity", "DeepSeek", 2.44, 0.01, "high", false]
    figures_description:
      - "Fig 18: ASV vs observed absolute bias scatter — 9 scenarios。Protest + stance 展示 negative correlation；toxicity 聚集在右上角（high ASV, low bias, indistinguishable）。"
      - "Fig 19: ASV vs raw C matrix comparison — side-by-side 对比 2 个 example scenarios，展示 ASV 提供 single interpretable number vs 9–25 cell matrix。"
    analysis: |
      ASVs 在 moderate-to-high bias scenarios 中具有经验实用性（protest K=5, stance K=3），
      但在 low-bias regime 失去区分力（toxicity K=2）。这是诚实且预期的——
      类似 E-values 在 confounding 小时不 informative。
      论文应 frame 为："ASVs are most valuable when annotation error is non-trivial (K≥3, accuracy <0.85)——
      precisely the scenarios where researchers lack existing diagnostic tools。"
      7/9 concordance 支持 Claim 2 的实用价值。

  - name: "Correction Guidance Framework: Decision Mapping and Validation"
    plan_id: plan_007
    description: |
      Decision framework: {topology × error structure × ASV} → correction method
      (DSL / PPI / MLA / naive plug-in / "no existing method adequate")。
      MC validation: 90 scenarios + empirical validation on plan_003 data。
    expected_results:
      total_mc_scenarios: 90
      correction_framework_accuracy: 0.89
      correct_recommendations: 80
      boundary_indistinguishable_cases: 3
      hard_failure_cases: 7
      failure_breakdown:
        near_diagonal_all_methods_equivalent: 3
        differential_intermediate_mismatch: 2
        false_recommendation_in_hopeless_regime: 2
      method_dominance:
        DSL: "best in 28/90 (diagonal-dominant C, confounding/mediation)"
        PPI: "best in 22/90 (moderate C, exposure/front-door)"
        MLA: "best in 18/90 (high off-diagonal, confounding/collider)"
        naive_plugin: "best in 12/90 (near-diagonal, any topology)"
        no_method_adequate: "10/90 (near-permutation + reversal topologies)"
      empirical_validation_plan003:
        protest_correct: true
        stance_correct: true
        toxicity_correct: true
      open_problems:
        - "dependence-aware multi-LLM correction"
        - "differential K≥3 error correction"
        - "collider + near-permutation C (no method reduces bias below 50%)"
    result_rationale: |
      89% accuracy 反映框架在 clear-cut scenarios（方法性能明显分离）的优势和 boundary cases 的弱点。

      3 个 boundary cases 是结构性不可区分的：near-diagonal C（low error）下所有方法结果相近（within 5%），
      "best" recommendation 是任意的。这不是框架的失败而是问题本身的 degeneracy。

      7 个 hard failures：
      (a) 3 cases: near-diagonal C 使所有方法等效但框架因 threshold effects 选了次优方法；
      (b) 2 cases: intermediate differential error 处框架的 non-differential/differential 二分类
      无法捕获 differentiality 的连续性质；
      (c) 2 cases: 框架推荐了方法但正确答案是"no method adequate"（near-permutation C + reversal topology）。

      Method dominance 是 topology-driven 的：DSL 擅长 confounding（调整 misclassified confounder 是其 native use case），
      PPI 擅长 exposure（regression-calibration 处理 treatment misclassification），
      MLA 擅长 high off-diagonal error（maximum likelihood 直接建模 C）。

      10/90 "no method adequate" 集中在 reversal topologies（exposure, mediation）+ extreme C——
      这些是 current correction literature 的真实 gaps。
    tables:
      - name: "Correction Method Dominance Map"
        columns: ["method", "best_in_n", "primary_topology", "primary_error_regime"]
        rows:
          - ["DSL", 28, "confounding, mediation", "diagonal-dominant C"]
          - ["PPI", 22, "exposure, front-door", "moderate off-diagonal"]
          - ["MLA", 18, "confounding, collider", "high off-diagonal"]
          - ["naive plug-in", 12, "any", "near-diagonal"]
          - ["no method", 10, "exposure, mediation", "near-permutation"]
      - name: "Framework Failure Analysis"
        columns: ["failure_type", "count", "impact", "mitigation"]
        rows:
          - ["boundary (methods ≤5% apart)", 3, "low", "any recommendation acceptable"]
          - ["differential mismatch", 2, "moderate", "add continuous differentiality parameter"]
          - ["false recommendation in hopeless regime", 2, "high", "add safety check: if reversal topology + extreme C → flag"]
    figures_description:
      - "Fig 20: Decision tree / flowchart — {topology, error structure, ASV} → recommended method。Color-coded by method，boundary regions highlighted。"
      - "Fig 21: Method accuracy heatmap — topology (rows) × error structure bins (cols) → recommendation accuracy。Diagonal patterns showing topology-method alignment。"
      - "Fig 22: Open problems map — (off-diagonal mass, differentiality) 2D scatter colored by adequate method existence。Gap region in upper-right clearly visible。"
    analysis: |
      Correction framework 达到主要目标：89% 正确识别 best correction method。
      11% failure rate 集中在固有歧义的 boundary cases（3%）和真正困难的 regimes（8%）。
      2 个"false recommendation in hopeless regime"最令人担忧——框架提供了虚假信心。
      论文应明确讨论此风险并建议 practitioners 始终在 held-out data 上验证 corrections。
      10 个"no method adequate"scenarios 是论文对 open problems 的贡献——
      特别是 dependence-aware multi-LLM correction（结合 plan_003 的 correlation 发现）。

  - name: "Pathological Confusion Matrix Analysis"
    plan_id: plan_009
    description: |
      极端 C 结构分析：near-permutation, rank-deficient, block-diagonal。
      刻画 catastrophic bias 条件并识别结构性预测因子。
    expected_results:
      spectral_gap_predictive_R2: 0.78
      diagonal_dominance_predictive_R2: 0.71
      combined_predictor_R2: 0.84
      catastrophic_threshold_spectral_gap: 0.3
      catastrophic_threshold_diagonal_dominance: 0.5
      near_permutation_universally_catastrophic: true
      rank_deficient_topology_dependent: true
      rank_deficient_worst: ["front-door", "instrument"]
      block_diagonal_worst: "mediation (blocks indirect path)"
    result_rationale: |
      Spectral gap（C 的第一和第二 eigenvalue 之差）预测 bias severity（R²=0.78）
      因为它捕获了 C 距 permutation matrix 的距离——反转的结构性来源。
      R²=0.78 表示强但不完美的预测；剩余方差来自 topology-specific interactions。

      Diagonal dominance（minimum diagonal element）是更简单的 proxy，R² 略低（0.71）。
      Combined spectral gap + diagonal dominance 达到 R²=0.84——两个 features 捕获了大部分 bias-relevant C structure。

      Near-permutation 普遍 catastrophic 因为 label-swapping 搅乱所有拓扑。
      Rank-deficient C 是 topology-dependent：front-door 和 instrument 的 identification formula
      含有 C-dependent 分母——C rank-deficient 时分母趋零，bias unbounded。
      Confounding/mediation/collider 对 rank deficiency 处理更 graceful（无 ratio estimator）。

      Block-diagonal C 对 mediation 最 severe——block 结构可以创造 artifact category boundaries 上的 apparent indirect effects。
    tables:
      - name: "Structural Predictors of Bias Severity"
        columns: ["predictor", "R2_overall", "best_topology_R2", "worst_topology_R2"]
        rows:
          - ["spectral gap", 0.78, "exposure (0.85)", "M-bias (0.67)"]
          - ["diagonal dominance", 0.71, "confounding (0.82)", "front-door (0.58)"]
          - ["spectral gap + diag dom", 0.84, "exposure (0.91)", "instrument (0.74)"]
      - name: "Catastrophic Bias Conditions by Topology and C Structure"
        columns: ["topology", "near_permutation", "rank_deficient", "block_diagonal"]
        rows:
          - ["confounding", "severe (OVB > 2×)", "moderate", "moderate"]
          - ["exposure", "catastrophic (reversal)", "severe", "severe (block reversal)"]
          - ["mediation", "severe (reversal)", "moderate", "severe (block indirect effects)"]
          - ["collider", "severe (attenuation > 60%)", "moderate", "moderate"]
          - ["M-bias", "moderate", "moderate", "mild"]
          - ["instrument", "moderate", "catastrophic (Wald denom → 0)", "moderate"]
          - ["front-door", "moderate", "catastrophic (identification loss)", "moderate"]
    figures_description:
      - "Fig 23: Spectral gap vs bias severity scatter — one panel/topology，threshold at 0.3 where bias becomes catastrophic。"
      - "Fig 24: Phase diagram — spectral gap (x) × diagonal dominance (y) → bias regime (safe/moderate/catastrophic)。Sharp boundaries visible。"
      - "Fig 25: Rank deficiency impact — bias magnitude vs effective matrix rank for each topology。Front-door + instrument 在 rank 降低时 diverge。"
    analysis: |
      实用 takeaway：spectral gap < 0.3 OR diagonal dominance < 0.5 → 所有拓扑均高风险。
      这一双阈值规则足够简单可用且捕获 84% 的 bias variance。
      Front-door 和 instrument 对 rank-deficient C 特别脆弱（ratio estimator 分母问题）。
      这些 structural predictors 是 toolkit (plan_010) 的 automatic diagnostic features 候选。

  - name: "annot-sensitivity Python Toolkit"
    plan_id: plan_010
    description: |
      Open-source pip-installable package：user-specified DAG + confusion matrix + downstream estimate
      → bias expressions + ASV + sensitivity curves + correction recommendation + diagnostic plots。
    expected_results:
      package_name: "annot-sensitivity"
      supported_topologies: 6
      supported_K_range: "2–10"
      core_api:
        - "compute_bias(dag, C, estimate) → BiasResult"
        - "compute_asv(dag, C, estimate, delta_range) → ASVResult"
        - "recommend_correction(dag, C, asv) → CorrectionRecommendation"
        - "diagnostic_plot(result) → Figure"
        - "eigendecomp_summary(C, K) → EigenSummary"
        - "check_pathological(C) → PathologyReport (spectral gap + diag dom thresholds)"
      worked_examples: 3
      example_topologies: ["confounding (baseline)", "exposure (reversal)", "mediation (conditional reversal)"]
      test_coverage: 0.87
      documentation: "API reference + 3 tutorial notebooks + quick-start guide"
      known_limitations:
        - "K>7 eigendecomposition slow (>10s/computation)"
        - "correction accuracy inherits plan_007 limitations (89%)"
        - "CLI + notebook only, no GUI"
        - "3/6 topologies lack detailed tutorials (M-bias, instrument, front-door)"
    result_rationale: |
      3 个 worked examples（而非 6）因为 median 档 scope 有限——优先覆盖 3 个 reversal-relevant 拓扑
      （confounding 作为 baseline，exposure + mediation 作为反转案例）。剩余 3 个拓扑在 API 中支持但缺少详细 tutorial。

      K>7 性能限制反映 eigendecomposition 的 O(K³) 成本——对典型 CSS 使用（K=3–7）可接受，
      对罕见 high-K 应用偏慢。

      Test coverage 0.87 反映核心计算（bias expressions, ASV）的 thorough unit testing
      和 visualization/correction recommendation 组件的 lighter testing。

      check_pathological() 集成 plan_009 的 spectral gap + diagonal dominance 阈值，
      为 practitioner 提供自动 C matrix 质量诊断。
    tables: []
    figures_description:
      - "Fig 26 (toolkit demo): Notebook screenshot — exposure DAG K=3 的完整输出：bias expression, ASV curve, correction recommendation, diagnostic plot，in a single cell。"
    analysis: |
      Toolkit 是 functional deliverable，使论文的理论贡献对 practitioners 可及。
      3 个 worked examples 覆盖最重要的场景（reversal cases）。
      主要 gap：3 个拓扑缺少 tutorial，可能限制 M-bias/instrument/front-door 用户的采纳。
      Post-publication 低成本 follow-up。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4b94d8e-32e4-47c4-9ccf-7341df4baba5",
  "isSidechain": false,
  "requestId": "req_011CbDTtp2xMp5KQpcLwhNuH",
  "type": "assistant",
  "uuid": "087bcd25-0f2f-448f-ac93-b6d5a0f98ad4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "86f3ecd8-a732-4359-9b4e-e89c85b83a9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9PD7Q7kkqyZQ1j7DPGGG1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10732,
      "cache_read_input_tokens": 11841,
      "output_tokens": 53192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 53192,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10732
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：2 个拓扑出现方向反转（exposure + mediation 或 collider 之一）；ASV 紧性证明仅覆盖 2 个拓扑；经验验证可用但不够 dramatic 核心假设：['mediation 或 collider 中恰好 1 个出现方向反转（violation rate 15-40%），另 1…",
  "leafUuid": "087bcd25-0f2f-448f-ac93-b6d5a0f98ad4",
  "sessionId": "86f3ecd8-a732-4359-9b4e-e89c85b83a9f"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze annotation errors across multi-class causal DAGs",
  "sessionId": "86f3ecd8-a732-4359-9b4e-e89c85b83a9f"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：2 个拓扑出现方向反转（exposure + mediation 或 collider 之一）；ASV 紧性证明仅覆盖 2 个拓扑；经验验证可用但不够 dramatic 核心假设：['mediation 或 collider 中恰好 1 个出现方向反转（violation rate 15-40%），另 1…",
  "leafUuid": "087bcd25-0f2f-448f-ac93-b6d5a0f98ad4",
  "sessionId": "86f3ecd8-a732-4359-9b4e-e89c85b83a9f"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze annotation errors across multi-class causal DAGs",
  "sessionId": "86f3ecd8-a732-4359-9b4e-e89c85b83a9f"
}
```

---
