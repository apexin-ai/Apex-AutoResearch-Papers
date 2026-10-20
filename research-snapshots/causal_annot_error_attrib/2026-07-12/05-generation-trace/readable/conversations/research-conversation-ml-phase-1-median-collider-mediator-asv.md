# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：方向反转仅在 collider（或仅在窄条件下的 mediator）出现；ASV 单调性成立但紧致性部分依赖数值证据；实证异质性有限 核心假设：['

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/47795e28-b323-455e-bd89-9d1ed4fde7b0.jsonl`
- **Structured JSON:** [`3579a6608d6a3ee693d1.json`](../../sessions/35/3579a6608d6a3ee693d1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T07:35:57.870Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T07:35:57.870Z",
  "sessionId": "47795e28-b323-455e-bd89-9d1ed4fde7b0",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：方向反转仅在 collider（或仅在窄条件下的 mediator）出现；ASV 单调性成立但紧致性部分依赖数值证据；实证异质性有限\n核心假设：['方向反转存在但局限于特定拓扑或需要特定 C 结构条件（如对角优势比 < 阈值）', 'ASV 单调性在 3 个优先拓扑均成立，但紧致性仅 1-2 个有形式证明，其余为 MC 数值猜想', 'LLM 经验混淆矩阵结构较同质（对角优势型为主），taxonomy 的实证区分力主要来自合成数据', 'Binarization collapse 在部分拓扑显著，但 confounding 以外的效应量较 MVP 预期更小']\n关键指标范围：{'direction_reversal_topologies': [1, 2], 'mc_theory_match_rate': [0.85, 0.95], 'asv_coverage_deviation_95': [0.02, 0.05], 'asv_sharpness_formal_proofs': [1, 2], 'binarization_delta_max': [0.04, 0.09], 'empirical_asv_discriminates': [0.55, 0.8], 'taxonomy_cells_with_qualitative_difference': [0.35, 0.55]}\n叙事方向：Claims 需要调整强度。Claim 1 从 \"完整 taxonomy\" 调整为 \"系统性框架，揭示关键拓扑间的定性差异\"， 承认部分拓扑（如 instrument/front-door）行为与 confounding 类似而非产生新洞见。 Claim 2 诚实界定 ASV 的证明范围（\"3 个拓扑单调性 + 1-2 个紧致性证明，其余数值验证\"）， 强调 ASV 作为实用工具的校准性能而非纯理论优雅。 Claim 3 不变但补充实验：在 ASV 区分力有限的任务上，展示 correction guidance 仍提供正确建议。 Headline 聚焦于被确认反转的拓扑：\"在 collider DAG 下，非差异性多类误差可反转效应方向， 而现有二分类理论无法预测此行为。\" 补充 binarization 风险作为第二支撑。 可能需要增加 1 个补充实验（差异性误差条件下的扩展）以增厚贡献。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: causal_annot_error_attrib\nfocus: Key uncertainty: will mediator/collider DAGs show direction reversal under non-differential multi-class error? Confounding DAG was monotonic in MVP. Also: is ASV framework practically useful enough vs just reporting confusion matrices?\n\n## paper_framing.md\n\n# Paper Framing — causal_annot_error_attrib\n\n## Target Venue\n- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)\n- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)\n- Tertiary: ICWSM 2027 Round 2 (2026-09-15)\n\n## Title\nMulti-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies\n\n## Core Claims (3 条)\n\n1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 6 canonical social-science DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door).\n\n2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of differential annotation error needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Reported alongside estimates, analogous to E-values for unmeasured confounding. Formal proofs (monotonicity + sharpness) for 3 priority topologies; MC-validated conjectures for the remaining 3.\n\n3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI, MLA, naive plug-in), characterizing regimes where each applies and where no existing method suffices — including dependence-aware multi-LLM correction as an open problem.\n\n## Story Spine\n\n- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31% of downstream conclusions are already incorrect. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable.\n\n- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.\n\n- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.\n\n- **Headline result template**: \"Across 6 DAG topologies with K=3,5,7, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. On 3 CSS tasks annotated by 3 LLMs, ASVs provide calibrated robustness indicators, and our taxonomy identifies cases where commonly applied corrections would increase rather than decrease bias.\"\n\n## Core Insight (Lead Finding)\n\nThe binary guarantee that \"non-differential misclassification biases toward the null\" breaks in the multi-class case (Brenner 1993). But Brenner only identifies the danger without resolving the ambiguity. Our taxonomy resolves it: for each {confusion matrix structure × DAG topology} cell, we provide exact conditions determining when bias attenuates, amplifies, or reverses. Furthermore, the natural \"fix\" of binarizing a K-class variable is itself hazardous — collapsing categories introduces new, direction-unpredictable bias (demonstrated in MVP: Δ up to 0.089 between K=3 and binarized estimates).\n\n## MVP Evidence\n\nConfounding DAG + K=3 validated:\n- Theoretical bias expressions match MC perfectly (5/5 structures within 95% CI)\n- All non-differential C structures produce positive bias 0.20-0.30 (toward OVB)\n- Binary collapse produces different bias (max Δ=0.089)\n- 100k random C search: confounding DAG bias is monotonically toward OVB (no direction reversal in this topology)\n- Direction reversal expected in mediator/collider topologies — research phase priority\n\n## Venue Fit Risks\n\n- **AAAI**: Broad AI audience — emphasize general methodology for \"automated annotation measurement error,\" not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.\n- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.\n- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n1. **\"Trivial extension of binary to multi-class\"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 6 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]\n\n2. **\"Lee & Wood-Doughty (2024) already did categorical\"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 6 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]\n\n3. **\"Why these 6 DAG topologies?\"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]\n\n4. **\"K≥5 expressions aren't actionable\"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]\n\n5. **\"ASV sharpness only proved for 3 topologies\"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]\n\n6. **\"Correlated multi-LLM errors?\"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]\n\n7. **\"Empirical validation scope\"** → 3 CSS tasks × 3 LLMs × 3 DAG-relevant scenarios. Tasks selected to cover K=2,3,5 annotation complexity. [Experiments: plan_003, plan_006]\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: Derive and MC-validate bias expressions for 6 DAG topologies with K=3\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n  details: 'For each topology (confounding, mediation, collider, M-bias, instrument,\n    front-door): derive closed-form K=3 bias expression, validate with MC (1000 reps\n    × N=10000, 6 confusion matrix structures including near-permutation extreme).\n    Key question: which topologies show direction reversal under non-differential\n    error? Confounding already validated in MVP (no reversal, monotonic toward OVB).\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  description: Extend bias expressions to K=5,7 — matrix notation + interpretability\n    tools\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'Matrix-form expressions for general K. Three interpretability tools: (a)\n    eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar\n    bounds collapsing matrix to conservative scalar, (c) diagnostic visualizations\n    mapping confusion matrix regions to bias magnitude. Validate on confounding +\n    mediation + collider DAGs with K=5,7.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 1\n  description: 'Empirical confusion matrices: 3 LLMs × 3 CSS tasks vs gold-standard'\n  priority: P0\n  gpu_budget_hours: 0\n  api_cost_estimate: $300-550\n  deps: []\n  details: 'Tasks: protest event coding (K=5, ACLED/GPT-RE), stance detection (K=3,\n    SemEval/VAST), toxicity (K=2, as special case / consistency check, Civil Comments).\n    Models: Llama 4 Maverick (Together.ai), Qwen 3.5 Plus (OpenRouter), DeepSeek V4\n    (DeepSeek API). ~30K annotations per model × 3 datasets × 3 prompt variants. Output:\n    empirical confusion matrices, inter-model correlation analysis, downstream regression\n    bias vs gold-standard baseline.\n\n    '\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Binarization collapse analysis: K→2 folding bias across all 6 topologies'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'For each of 6 topologies with K=3,5,7: collapse to binary, compare bias\n    from full multi-class expression vs binarized expression. Demonstrate that binarization\n    is not a safe shortcut — can amplify or reverse bias. MVP showed Δ up to 0.089\n    for confounding DAG K=3.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'ASV framework: formal proofs for confounding, mediation, collider'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'Derive ASV expressions for 3 priority topologies. Formal proofs of: (a)\n    monotonicity (ASV increases with δ amplification), (b) sharpness (bound is achievable\n    for some confusion matrix). MC validation: coverage at 90%, 95%, 99% levels across\n    1000 scenarios.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 2\n  description: ASV MC validation for M-bias, instrument, front-door topologies\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_004\n  details: 'ASV expressions + MC validation of monotonicity and coverage. Sharpness\n    stated as conjectures supported by numerical evidence. If any topology fails monotonicity\n    under MC, flag and investigate.\n\n    '\n  status: planned\n- id: plan_006\n  claim: 2\n  description: ASV calibration on empirical data (3 CSS tasks × 3 LLMs)\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  - plan_004\n  details: 'Apply ASVs to empirical confusion matrices from plan_003. Validate coverage\n    on held-out gold-standard splits. Report ASV alongside downstream effect estimates\n    for each task. Compare ASV interpretability with raw confusion matrix reporting.\n\n    '\n  status: planned\n- id: plan_007\n  claim: 3\n  description: 'Correction guidance framework: decision mapping + validation'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_004\n  - plan_003\n  details: 'Decision framework: {topology × error structure × ASV} → correction method\n    (DSL / PPI / MLA / naive plug-in / \"no existing method adequate\"). MC validation:\n    recommended method produces least bias in ≥90% of scenarios. Empirical validation\n    on plan_003 data. Characterize regimes where no existing method suffices (correlated\n    errors, differential multi-class, etc.) — identify as open problems.\n\n    '\n  status: planned\n- id: plan_009\n  claim: 1\n  description: Pathological confusion matrix analysis (near-permutation, rank-deficient)\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'Extreme C structures: near-permutation, rank-deficient, block-diagonal.\n    Characterize when bias becomes catastrophic across topologies. Identify structural\n    conditions (spectral gap, diagonal dominance ratio) that predict bias severity\n    — candidate features for practitioners.\n\n    '\n  status: planned\n- id: plan_010\n  claim: all\n  description: annot-sensitivity Python toolkit (open-source release)\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_004\n  - plan_007\n  details: 'Package: user-specified DAG + confusion matrix(es) + downstream estimate\n    → bias expressions (scalar K≤3, matrix K>3 with interpretability) + ASV bounds\n    + sensitivity curves + correction recommendation + diagnostic plots. pip-installable,\n    with worked examples for each topology.\n\n    '\n  status: planned\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T07:35:57.876Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T07:35:57.876Z",
  "sessionId": "47795e28-b323-455e-bd89-9d1ed4fde7b0"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T07:35:57.963Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：方向反转仅在 collider（或仅在窄条件下的 mediator）出现；ASV 单调性成立但紧致性部分依赖数值证据；实证异质性有限
核心假设：['方向反转存在但局限于特定拓扑或需要特定 C 结构条件（如对角优势比 < 阈值）', 'ASV 单调性在 3 个优先拓扑均成立，但紧致性仅 1-2 个有形式证明，其余为 MC 数值猜想', 'LLM 经验混淆矩阵结构较同质（对角优势型为主），taxonomy 的实证区分力主要来自合成数据', 'Binarization collapse 在部分拓扑显著，但 confounding 以外的效应量较 MVP 预期更小']
关键指标范围：{'direction_reversal_topologies': [1, 2], 'mc_theory_match_rate': [0.85, 0.95], 'asv_coverage_deviation_95': [0.02, 0.05], 'asv_sharpness_formal_proofs': [1, 2], 'binarization_delta_max': [0.04, 0.09], 'empirical_asv_discriminates': [0.55, 0.8], 'taxonomy_cells_with_qualitative_difference': [0.35, 0.55]}
叙事方向：Claims 需要调整强度。Claim 1 从 "完整 taxonomy" 调整为 "系统性框架，揭示关键拓扑间的定性差异"， 承认部分拓扑（如 instrument/front-door）行为与 confounding 类似而非产生新洞见。 Claim 2 诚实界定 ASV 的证明范围（"3 个拓扑单调性 + 1-2 个紧致性证明，其余数值验证"）， 强调 ASV 作为实用工具的校准性能而非纯理论优雅。 Claim 3 不变但补充实验：在 ASV 区分力有限的任务上，展示 correction guidance 仍提供正确建议。 Headline 聚焦于被确认反转的拓扑："在 collider DAG 下，非差异性多类误差可反转效应方向， 而现有二分类理论无法预测此行为。" 补充 binarization 风险作为第二支撑。 可能需要增加 1 个补充实验（差异性误差条件下的扩展）以增厚贡献。


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

## Core Insight (Lead Finding)

The binary guarantee that "non-differential misclassification biases toward the null" breaks in the multi-class case (Brenner 1993). But Brenner only identifies the danger without resolving the ambiguity. Our taxonomy resolves it: for each {confusion matrix structure × DAG topology} cell, we provide exact conditions determining when bias attenuates, amplifies, or reverses. Furthermore, the natural "fix" of binarizing a K-class variable is itself hazardous — collapsing categories introduces new, direction-unpredictable bias (demonstrated in MVP: Δ up to 0.089 between K=3 and binarized estimates).

## MVP Evidence

Confounding DAG + K=3 validated:
- Theoretical bias expressions match MC perfectly (5/5 structures within 95% CI)
- All non-differential C structures produce positive bias 0.20-0.30 (toward OVB)
- Binary collapse produces different bias (max Δ=0.089)
- 100k random C search: confounding DAG bias is monotonically toward OVB (no direction reversal in this topology)
- Direction reversal expected in mediator/collider topologies — research phase priority

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
  claim: all
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
  "promptId": "6108d3d1-22c6-484b-9c83-c6acdf30de35",
  "type": "user",
  "uuid": "7a7e3f9c-d7ed-4442-a47e-e9f1aa2b4867",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "47795e28-b323-455e-bd89-9d1ed4fde7b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T07:35:57.961Z_

```json
{
  "parentUuid": "7a7e3f9c-d7ed-4442-a47e-e9f1aa2b4867",
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
  "uuid": "87f28849-835c-442c-a0b3-76e357d02715",
  "timestamp": "2026-05-20T07:35:57.961Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "47795e28-b323-455e-bd89-9d1ed4fde7b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T07:35:57.961Z_

```json
{
  "parentUuid": "87f28849-835c-442c-a0b3-76e357d02715",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4046db63-c79b-4d5b-8836-5d4a07b83110",
  "timestamp": "2026-05-20T07:35:57.961Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "47795e28-b323-455e-bd89-9d1ed4fde7b0",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：方向反转仅在 collider（或仅在窄条件下的 mediator）出现；ASV 单调性成立但紧致性部分依赖数值证据；实证异质性有限 核心假设：['方向反转存在但局限于特定拓扑或需要特定 C 结构条件（如对角优势比 < 阈值）', 'ASV 单调性在 3 个优先拓扑均成立，但紧致性仅 1-2 个有形式证明…",
  "leafUuid": "4046db63-c79b-4d5b-8836-5d4a07b83110",
  "sessionId": "47795e28-b323-455e-bd89-9d1ed4fde7b0"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-class annotation bias taxonomy and ASV framework",
  "sessionId": "47795e28-b323-455e-bd89-9d1ed4fde7b0"
}
```

---

### Assistant

_source line 8 · 2026-05-20T07:36:22.913Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment data for each planned experiment in the experiment_plan, based on the "median" tier definition. I need to produce YAML output with specific predicted results and rationales for each experiment.

Let me carefully go through each experiment and think about what median-tier results would look like, given the constraints defined:

**Median tier key characteristics:**
- Direction reversal only in collider (or only under narrow conditions in mediator)
- ASV monotonicity holds but sharpness partially relies on numerical evidence
- Limited empirical heterogeneity


- Direction reversals appearing in 1-2 topologies out of the full set
- Monte Carlo theory match rates between 85-95%, showing good but not perfect alignment
- ASV coverage deviations staying modest at 2-5%
- Formal proofs supporting 1-2 of the sharpness claims
- Binarization effects moderate, with max deltas between 4-9%
- Empirical ASV discrimination moderate at 55-80%
- Qualitative differences in taxonomy cells appearing in 35-55% of cases

Now I'm working through the first experiment plan with its 6 DAG topologies.

For plan_001, the median behavior shows direction reversal confirmed in the collider case while confounding remains stable without reversal, with instruments and front-door structures behaving similarly to confounding toward the null. M-bias shows some amplification but no reversal. The Monte Carlo match rate sits around 0.90, and five of the six topologies stay within the 95% confidence interval across all structures, though one topology might have a single structure slightly outside bounds.

Plan_002 extends to K=5 and K=7, where the matrix expressions work but the interpretability tools show mixed results—eigendecomposition captures the dominant mode well but higher K values introduce more noise. Plan_003 examines empirical confusion matrices from the LLM, finding them mostly diagonal-dominant with limited heterogeneity between models. Plan_004 focuses on formal ASV proofs for the three priority topologies, confirming monotonicity holds across all three.

Sharpness is proved for one or two topologies (likely confounding and possibly mediation), with coverage staying within 0.02-0.05 of nominal. Plan_005 applies ASV to the remaining three topologies, where Monte Carlo validation supports the numerical conjectures without any monotonicity failures. Plan_006 tests ASV calibration on empirical data, finding it discriminates in the 0.55-0.8 range—useful but not transformative. Plan_007 develops a correction guidance framework that works well for confounding and collider cases but is less clear for others, achieving at least 85% correct recommendation rates. Plan_008 examines binarization collapse with delta max values between 0.04 and 0.09, showing significant effects for collider and mediation but more modest effects elsewhere. Plan_009 investigates pathological confusion matrices and identifies the spectral gap as a key factor.

The spectral gap also reveals catastrophic bias in near-permutation cases. Plan_010 is a Python toolkit—more of a software deliverable than an experiment with quantifiable metrics. Now I'm moving on to write out the detailed YAML configuration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4046db63-c79b-4d5b-8836-5d4a07b83110",
  "isSidechain": false,
  "requestId": "req_011CbDSG7K88t3UVE92j4B7z",
  "type": "assistant",
  "uuid": "359ad4fd-3015-49c0-ac87-f867d223670c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "47795e28-b323-455e-bd89-9d1ed4fde7b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WzvpAoowrS8chKNd5v6fL2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10024,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10024,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11509,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10024
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

_source line 9 · 2026-05-20T07:39:52.963Z_

```yaml
tier: median
narrative_guidance: >
  Claims 需要调整强度。Claim 1 从 "完整 taxonomy" 调整为 "系统性框架，揭示关键拓扑间的定性差异"，
  承认 instrument/front-door 行为与 confounding 类似而非产生新洞见。
  Claim 2 诚实界定 ASV 证明范围（"3 个拓扑单调性 + 1-2 个紧致性证明，其余数值验证"），
  强调 ASV 作为实用校准工具。Claim 3 不变但补充实验：在 ASV 区分力有限的任务上，
  展示 correction guidance 仍提供正确建议。
  Headline 聚焦 collider DAG 方向反转 + binarization 风险。
  可能需增加差异性误差条件扩展实验以增厚贡献。

imagined_experiments:
  - name: "6-topology K=3 bias derivation and MC validation"
    plan_id: "plan_001"
    description: >
      对 6 个 DAG 拓扑（confounding, mediation, collider, M-bias, instrument, front-door）
      推导 K=3 闭式偏差表达式，每拓扑 6 种混淆矩阵结构 × 1000 MC reps × N=10000 验证。
    expected_results:
      direction_reversal_topologies: 1
      topologies_with_reversal: ["collider"]
      topologies_monotonic_toward_null: ["confounding", "instrument", "front-door"]
      mediation_reversal: "仅在 off-diagonal 质量集中于特定非对称结构时出现微弱反转（1/6 结构，幅度 < 0.02），不足以作为 robust claim"
      m_bias_behavior: "放大但不反转，偏差幅度 0.15-0.40，方向与 confounding 一致"
      mc_theory_match_rate_overall: 0.92
      mc_theory_match_by_topology:
        confounding: 1.0
        mediation: 0.83
        collider: 0.83
        m_bias: 1.0
        instrument: 1.0
        front_door: 0.83
      collider_reversal_magnitude: [-0.18, -0.08]
      confounding_bias_range: [0.20, 0.30]
      structures_within_95ci: "34/36 (94.4%)"
    result_rationale: >
      Confounding DAG 已在 MVP 中确认无反转（单调向 OVB）。Collider 拓扑因其"开门"效应——
      条件化 collider 引入虚假关联——在非差异性多类误差下最可能产生方向反转：
      误分类等效于对 collider 的软条件化，不同类别间的误分类率差异会引入不对称的虚假路径，
      导致净效应符号翻转。Mediation 拓扑在理论上可能反转（误分类改变间接效应的传递），
      但仅在 C 矩阵高度非对称且间接效应本身较弱时才出现，属于窄条件。
      Instrument 和 front-door 的误分类主要通过衰减 IV 强度或前门路径的传递效率起作用，
      效应方向由因果路径的符号结构决定而非误分类引入新路径，因此行为类似 confounding（单调衰减）。
      M-bias 因拓扑本身引入额外路径，误分类可放大偏差但不改变方向。
      MC 匹配率约 0.92 而非更高，因为 mediation/collider/front-door 的闭式表达式涉及
      间接效应乘积项，O(1/N) 近似在有限样本下引入轻微偏差，导致 2/36 结构点在
      near-permutation extreme 下略超 95% CI。
    tables:
      - name: "Table 1: Bias direction and magnitude by topology × C structure (K=3)"
        rows: ["confounding", "mediation", "collider", "M-bias", "instrument", "front-door"]
        columns: ["diagonal-dominant", "uniform-off-diag", "adjacent-leak", "block-confuse", "asymmetric-skew", "near-permutation"]
        content_description: >
          每格报告 (bias sign, bias magnitude, 95% MC CI)。
          Confounding 行全正 [+0.20, +0.30]；collider 行 4/6 为负 [-0.18, -0.03]，
          2/6 为正但幅度 < 0.05（diagonal-dominant 和 uniform-off-diag）；
          mediation 行 5/6 正，1/6 微负 (-0.015)；instrument/front-door 全正且幅度接近 confounding；
          M-bias 全正但幅度更大 [+0.15, +0.40]。
      - name: "Table 2: MC validation summary — theory vs simulation"
        rows: ["confounding", "mediation", "collider", "M-bias", "instrument", "front-door"]
        columns: ["structures_within_95CI (out of 6)", "max_absolute_deviation", "mean_absolute_deviation"]
        content_description: >
          Confounding 6/6, max dev 0.003；mediation 5/6, max dev 0.021；
          collider 5/6, max dev 0.018；M-bias 6/6, max dev 0.005；
          instrument 6/6, max dev 0.004；front-door 5/6, max dev 0.016。
    figures_description:
      - "Figure 1: Heatmap — bias magnitude × sign across 6 topologies × 6 C structures，颜色编码正/负/零，突出 collider 行的反转区域"
      - "Figure 2: MC scatter — 理论预测 vs MC 估计，36 个点，1:1 线 + 95% CI bands，标注超出 CI 的 2 个点"
    analysis: >
      核心发现：方向反转仅在 collider 拓扑下 robust 出现（4/6 C 结构），
      mediation 的反转过于微弱且条件苛刻，不宜作为独立 claim。
      Instrument/front-door 与 confounding 定性一致，这限制了 taxonomy 的实证区分力——
      6 拓扑中仅 3 组定性行为（confounding-like / collider / M-bias amplification）。
      Headline 应聚焦 collider 反转作为 lead finding。
      MC 匹配率 0.92 足够支撑理论可信度但需在论文中诚实报告 near-permutation 边界情况。

  - name: "General-K matrix expressions and interpretability tools"
    plan_id: "plan_002"
    description: >
      将偏差表达式推广至 K=5,7 矩阵形式，开发三种可解释性工具
      （特征分解、worst-case 标量界、诊断可视化），在 confounding/mediation/collider 上验证。
    expected_results:
      eigendecomp_dominant_mode_variance_explained:
        K5: 0.72
        K7: 0.61
      worst_case_bound_tightness:
        K5: 1.8
        K7: 2.4
      mc_validation_K5_match_rate: 0.89
      mc_validation_K7_match_rate: 0.86
      collider_reversal_persists_K5: true
      collider_reversal_persists_K7: true
      new_reversal_topologies_at_higher_K: 0
    result_rationale: >
      K 增大时偏差从标量变为矩阵值，特征分解的第一主成分解释方差随 K 下降是自然的——
      K=5 有 20 个自由参数，K=7 有 42 个，偏差的多模态结构更明显。
      Worst-case 标量界在高 K 下变松（tightness ratio 从 K=3 的 ~1.2 升至 K=7 的 ~2.4），
      因为将矩阵压缩为标量必然丢失结构信息，高维下损失更大。
      Collider 反转在 K=5,7 仍存在，因为其拓扑机制（误分类诱导虚假条件化）不依赖于 K，
      但不会出现新的反转拓扑——如果 K=3 下某拓扑不反转，增加类别只增加噪声维度而不改变因果路径结构。
      MC 匹配率下降至 0.86-0.89 因为高维闭式表达式涉及矩阵逆和 Kronecker 乘积，
      有限样本的矩阵估计误差在高 K 下更显著。
    tables:
      - name: "Table 3: Interpretability tool performance by K"
        rows: ["K=3", "K=5", "K=7"]
        columns: ["eigendecomp_R2", "worst_case_tightness", "mc_match_rate", "user_interpretability_score"]
        content_description: >
          展示三种工具随 K 的退化情况。K=3 仍推荐直接使用标量表达式；
          K=5 特征分解有效但 worst-case 界偏松；K=7 需组合使用三种工具。
    figures_description:
      - "Figure 3: 特征分解 biplot — K=5 collider 拓扑，前两个主成分，标注偏差方向和各类别贡献"
      - "Figure 4: 诊断热力图 — K=7 confounding，混淆矩阵区域 → 偏差幅度映射"
    analysis: >
      高 K 下可解释性工具有用但非完美——worst-case 界在 K≥5 时过松（2x+），
      需配合特征分解使用。这限制了 "actionable for practitioners" 的说服力，
      论文应诚实讨论 K≥5 的局限并推荐组合工具策略。
      关键正面发现：collider 反转在所有 K 下一致，strengthens Claim 1 的 headline。

  - name: "Empirical LLM confusion matrices on 3 CSS tasks"
    plan_id: "plan_003"
    description: >
      3 个 LLM（Llama 4 Maverick, Qwen 3.5 Plus, DeepSeek V4）× 3 个 CSS 任务
      （protest K=5, stance K=3, toxicity K=2）× 3 prompt variants，收集经验混淆矩阵。
    expected_results:
      total_annotations: "~270K (30K × 3 models × 3 tasks)"
      confusion_matrix_structure_dominant_type: "diagonal-dominant"
      diagonal_dominance_ratio_range: [0.55, 0.82]
      inter_model_error_correlation: 0.58
      models_with_qualitatively_different_C: 0
      prompt_variant_effect_on_C_structure: "quantitative shift only (diagonal ±0.05), no qualitative change"
      protest_K5_accuracy_range: [0.52, 0.68]
      stance_K3_accuracy_range: [0.65, 0.78]
      toxicity_K2_accuracy_range: [0.82, 0.91]
      downstream_bias_vs_gold:
        protest_confounding_proxy: [0.08, 0.22]
        stance_mediation_proxy: [0.05, 0.14]
        toxicity_binary_baseline: [0.02, 0.06]
    result_rationale: >
      当前 LLM（2026 年中）在 CSS 任务上普遍表现为对角优势型误差——模型倾向于
      在正确类别附近犯错而非系统性混淆远类别。Inter-model 相关 ~0.58 与 Kim et al. (2025)
      的 60% 一致，因为模型共享类似的预训练数据和 RLHF 模式，导致误差模式趋同。
      三个模型不会产生定性不同的 C 结构（如一个对角优势、另一个 block-confuse），
      因为底层语言理解能力的差异主要体现在精度而非误差拓扑。
      Prompt variant 仅改变对角线强度（±0.05），不改变 off-diagonal 结构，
      因为 prompt engineering 主要影响决策边界的置信度而非类别间的语义混淆模式。
      这意味着 taxonomy 的实证区分力主要来自合成数据而非真实 LLM——
      真实 LLM 占据 taxonomy 的一个有限子空间（对角优势型）。
      Protest K=5 精度最低因为类别数多且边界模糊（如 "riot" vs "protest" vs "demonstration"）。
    tables:
      - name: "Table 4: Empirical confusion matrices — 3 models × 3 tasks (best prompt variant)"
        rows: ["Llama 4 Maverick", "Qwen 3.5 Plus", "DeepSeek V4"]
        columns: ["protest (K=5) accuracy", "stance (K=3) accuracy", "toxicity (K=2) accuracy", "avg diagonal dominance ratio"]
        content_description: >
          Llama: 0.64/0.72/0.88/0.74；Qwen: 0.58/0.68/0.85/0.68；
          DeepSeek: 0.68/0.78/0.91/0.79。所有矩阵均为对角优势型。
      - name: "Table 5: Inter-model error correlation matrix"
        rows: ["Llama-Qwen", "Llama-DeepSeek", "Qwen-DeepSeek"]
        columns: ["protest", "stance", "toxicity", "average"]
        content_description: >
          相关系数范围 0.51-0.65，平均 0.58。Protest 任务相关最高（0.63）因为
          类别边界本身模糊导致模型在相同样本上犯错。
    figures_description:
      - "Figure 5: 混淆矩阵热力图 — 9 个子图（3 models × 3 tasks），颜色编码归一化行概率"
      - "Figure 6: 下游偏差 bar chart — gold vs 各 LLM 注释的效应估计，含 95% CI"
    analysis: >
      经验 C 矩阵的同质性（全部对角优势型）是 median 档的核心限制——
      taxonomy 的丰富区分力（如 near-permutation、block-confuse）无法在真实 LLM 数据上展示。
      论文需坦诚讨论这一点，并论证：(1) taxonomy 的价值在于预警未来可能出现的
      非典型误差结构（如领域特异性模型），(2) 即使在对角优势型区域内，
      下游偏差仍因拓扑不同而有定量差异（0.02-0.22）。

  - name: "ASV formal proofs for 3 priority topologies"
    plan_id: "plan_004"
    description: >
      对 confounding/mediation/collider 推导 ASV 表达式，证明单调性和紧致性，
      MC 验证覆盖率（90%/95%/99%）。
    expected_results:
      monotonicity_proved: ["confounding", "mediation", "collider"]
      sharpness_proved: ["confounding"]
      sharpness_numerical_only: ["mediation", "collider"]
      asv_coverage_90:
        confounding: 0.91
        mediation: 0.88
        collider: 0.87
      asv_coverage_95:
        confounding: 0.96
        mediation: 0.93
        collider: 0.92
      asv_coverage_99:
        confounding: 0.995
        mediation: 0.98
        collider: 0.97
      asv_coverage_deviation_95_max: 0.03
      mc_scenarios_validated: 1000
      sharpness_numerical_gap:
        mediation: 0.012
        collider: 0.018
    result_rationale: >
      单调性（ASV 随 δ 增大而增大）对三个拓扑均可证明，因为偏差表达式中
      δ 以乘性或仿射方式进入——增大误差放大因子单调增加偏差幅度，
      因此反转结论所需的最小误差量单调增加。这是一个相对温和的代数性质。
      紧致性（存在某 C 使界恰好达到）则困难得多：confounding 的偏差表达式是 C 的线性函数，
      极值在可行域顶点取到，可用线性规划对偶证明紧致。
      Mediation 涉及乘积项（直接效应 × 间接效应），collider 涉及条件化诱导的非线性——
      这些情况下极值可能在可行域内部取到，解析证明需要 KKT 条件的完整分析，
      代数复杂度在 median 档下仅能用数值方法逼近。
      数值紧致性间隙 0.012-0.018 表明界接近但非完全 tight。
      Coverage 在 95% 水平偏差 ≤0.03 是因为 ASV 基于闭式偏差表达式的保守上界，
      有限样本估计的 C 矩阵不确定性导致轻微欠覆盖，尤其在 mediation/collider
      因表达式含非线性项而更敏感。
    tables:
      - name: "Table 6: ASV proof status and coverage"
        rows: ["confounding", "mediation", "collider"]
        columns: ["monotonicity", "sharpness", "coverage_90", "coverage_95", "coverage_99", "numerical_sharpness_gap"]
        content_description: >
          Confounding: proved/proved/0.91/0.96/0.995/0.000；
          mediation: proved/conjecture/0.88/0.93/0.98/0.012；
          collider: proved/conjecture/0.87/0.92/0.97/0.018。
    figures_description:
      - "Figure 7: ASV sensitivity curves — 3 拓扑 × δ 从 1.0 到 3.0，展示 ASV 单调递增"
      - "Figure 8: Coverage calibration plot — 名义 vs 实际覆盖率，45 度线对比"
    analysis: >
      仅 confounding 的紧致性有形式证明，mediation/collider 依赖数值猜想。
      这需要在论文中诚实表述，但不影响 ASV 的实用价值——
      覆盖率偏差 ≤0.03 在实践中可接受（类似 E-value 的保守性）。
      Claim 2 应表述为 "单调性全证 + 紧致性部分证明 + 数值验证"，
      避免暗示完整的理论优雅性。

  - name: "ASV MC validation for secondary topologies"
    plan_id: "plan_005"
    description: >
      M-bias/instrument/front-door 的 ASV 表达式 + MC 验证单调性和覆盖率，
      紧致性作为数值猜想。
    expected_results:
      monotonicity_mc_confirmed: ["m_bias", "instrument", "front_door"]
      monotonicity_violations: 0
      coverage_95:
        m_bias: 0.93
        instrument: 0.95
        front_door: 0.94
      coverage_deviation_95_max: 0.02
      sharpness_numerical_gap:
        m_bias: 0.022
        instrument: 0.009
        front_door: 0.015
      mc_reps_per_scenario: 1000
      scenarios_tested: 500
    result_rationale: >
      这三个拓扑的 ASV 行为应与优先拓扑一致，因为 ASV 的单调性依赖的核心性质
      （偏差关于误差参数的单调性）是拓扑无关的一般性质。
      MC 单调性零违反是预期的——如果理论表达式正确且偏差确实随误差单调变化，
      1000 reps 足以确认。Instrument 的 coverage 最好（0.95 恰好）因为其偏差结构
      最简单（误分类仅衰减 IV 强度，类似测量误差衰减），ASV 界自然较紧。
      Sharpness gap 范围 0.009-0.022 与优先拓扑一致，
      M-bias 最大（0.022）因为其拓扑复杂度最高（4 条因果路径交互）。
    tables:
      - name: "Table 7: ASV validation for secondary topologies"
        rows: ["M-bias", "instrument", "front-door"]
        columns: ["monotonicity_confirmed", "coverage_95", "sharpness_gap", "scenarios"]
        content_description: >
          全部单调性确认，coverage 0.93-0.95，gap 0.009-0.022。
    figures_description:
      - "Figure 9: ASV sensitivity curves — 3 secondary topologies，格式同 Figure 7"
    analysis: >
      Secondary topologies 无意外，支持 ASV 框架的一般性。
      结合 plan_004，6 个拓扑均有单调性（3 形式证明 + 3 数值确认），
      紧致性 1 个形式证明 + 5 个数值猜想。
      这是 median 档的核心特征——理论完整但不全部形式化。

  - name: "ASV calibration on empirical CSS data"
    plan_id: "plan_006"
    description: >
      将 ASV 应用于 plan_003 的经验混淆矩阵，在 held-out gold splits 上验证覆盖率，
      报告 ASV alongside 下游效应估计。
    expected_results:
      empirical_asv_discriminates: 0.67
      tasks_where_asv_correctly_flags_risk:
        protest_confounding: true
        stance_mediation: true
        toxicity_binary: "trivially high ASV (no risk)"
      empirical_coverage_95: 0.93
      asv_vs_raw_confusion_matrix_interpretability_preference: "ASV preferred by construction but limited empirical gap"
      asv_range_protest: [1.2, 2.1]
      asv_range_stance: [1.8, 3.5]
      asv_range_toxicity: [4.5, 12.0]
      tasks_where_asv_changes_conclusion: 1
    result_rationale: >
      Empirical ASV 区分力 0.67 处于 median 范围 [0.55, 0.8]——
      因为经验 C 矩阵全部对角优势型，ASV 值分布的方差有限，区分不同风险水平的能力受限。
      Protest 任务 ASV 最低（1.2-2.1）因为 K=5 精度较低，离反转所需误差增幅近；
      toxicity 任务 ASV 极高（4.5-12.0）因为 K=2 高精度下结论极稳健。
      Stance 任务是 "sweet spot"——ASV 处于中等范围，能展示框架的诊断价值。
      仅 1 个 task-model 组合的 ASV 实际改变分析结论（protest + Qwen，ASV=1.2 提示
      结论不稳健），其余组合 ASV 提供的信息与直觉一致（高精度 → 高 ASV → 安全）。
      Empirical coverage 0.93 vs 名义 0.95 的偏差与 plan_004 的合成结果一致。
    tables:
      - name: "Table 8: ASV values by task × model"
        rows: ["Llama 4 Maverick", "Qwen 3.5 Plus", "DeepSeek V4"]
        columns: ["protest ASV", "stance ASV", "toxicity ASV", "conclusion_changed"]
        content_description: >
          仅 Qwen+protest 的 ASV=1.2 触发 "结论不稳健" 警告；
          其余 ASV ≥ 1.8，结论稳健。
      - name: "Table 9: ASV coverage validation on held-out splits"
        rows: ["protest", "stance", "toxicity"]
        columns: ["nominal_95_coverage", "empirical_coverage", "deviation"]
        content_description: >
          Protest 0.92, stance 0.93, toxicity 0.97。偏差范围 -0.03 到 +0.02。
    figures_description:
      - "Figure 10: ASV 仪表盘示例 — protest 任务 + Qwen，展示 ASV=1.2 的风险提示和建议"
      - "Figure 11: ASV 分布 violin plot — 3 tasks × 3 models，展示 ASV 的区分力"
    analysis: >
      ASV 在经验数据上的表现 "足够有用但不惊艳"——
      区分力 0.67 意味着约 1/3 的情况下 ASV 未能在已知风险和安全案例间提供清晰分离。
      这主要因为经验 C 矩阵同质性——如果未来 LLM 产生更多样化的误差结构，
      ASV 的区分力应提升。Claim 2 的经验支撑需要依赖 protest+Qwen 这个 "近边界" 案例
      作为 showcase，并补充合成数据的校准结果。

  - name: "Correction guidance framework validation"
    plan_id: "plan_007"
    description: >
      构建 {拓扑 × 误差结构 × ASV} → 校正方法映射，MC + 经验验证。
    expected_results:
      recommendation_accuracy_mc: 0.87
      recommendation_accuracy_empirical: 0.83
      methods_compared: ["DSL", "PPI", "MLA", "naive_plug_in"]
      regimes_no_method_adequate: 3
      no_method_regimes: ["correlated_multi_annotator", "differential_multiclass_collider", "near_permutation_any_topology"]
      correction_improves_vs_uncorrected: 0.78
      correction_guidance_useful_when_asv_low: true
    result_rationale: >
      推荐准确率 0.87（MC）而非更高，因为 mediation/collider 拓扑下最优校正方法
      取决于 C 矩阵的精细结构（不仅是类型），在边界区域多种方法表现相近，
      "最优" 的定义变得模糊。经验准确率 0.83 略低于 MC 因为经验 C 矩阵估计本身有噪声。
      3 个无充分方法的 regime 反映了现有校正文献的真实空白：
      (1) 相关多标注器误差缺乏联合模型，
      (2) 差异性多类误差在 collider 下的交互效应无现有方法处理，
      (3) near-permutation C 下所有方法均退化因为信号已被严重破坏。
      在 ASV 较低（结论不稳健）的案例上，correction guidance 仍能指向正确方法——
      这是 median 档下 Claim 3 的关键支撑：即使 ASV 区分力有限，guidance 仍 actionable。
    tables:
      - name: "Table 10: Correction method performance by topology × C structure"
        rows: ["confounding", "mediation", "collider", "M-bias", "instrument", "front-door"]
        columns: ["best_method", "best_bias_reduction_%", "framework_recommends_correctly", "no_method_adequate"]
        content_description: >
          Confounding: MLA best, 75% reduction, correct；
          mediation: PPI best, 60% reduction, correct；
          collider: DSL best, 55% reduction, correct but narrow margin over PPI；
          M-bias: MLA best, 68% reduction, correct；
          instrument: naive plug-in sufficient, 80% reduction, correct；
          front-door: PPI best, 65% reduction, correct。
    figures_description:
      - "Figure 12: Decision tree — {topology × C type × ASV} → recommended correction，可视化框架"
      - "Figure 13: Bias reduction bar chart — uncorrected vs framework-recommended vs oracle，3 tasks"
    analysis: >
      Correction guidance 的准确率 87% 足以作为 "principled starting point"，
      但 13% 的边界情况需要诚实讨论。关键卖点在 ASV-low 区域的有效性——
      即使 ASV 无法区分风险级别，guidance 仍指向偏差最小的校正方法。
      3 个 "无充分方法" regime 是 open problem 的自然位置，
      strengthens 论文的学术贡献（揭示空白而非假装已解决）。

  - name: "Binarization collapse analysis across 6 topologies"
    plan_id: "plan_008"
    description: >
      对 6 拓扑 × K=3,5,7 执行 K→2 折叠，比较多类偏差 vs 二值化偏差。
    expected_results:
      binarization_delta_max: 0.078
      binarization_delta_by_topology:
        confounding: 0.065
        mediation: 0.048
        collider: 0.078
        m_bias: 0.071
        instrument: 0.042
        front_door: 0.045
      delta_increases_with_K: true
      delta_K5_vs_K3_ratio: 1.35
      delta_K7_vs_K3_ratio: 1.62
      binarization_reverses_direction: 1
      reversal_topology: "collider (K=5, specific folding scheme)"
      taxonomy_cells_with_qualitative_difference: 0.44
    result_rationale: >
      Binarization delta max 0.078 处于 median 范围 [0.04, 0.09]。
      Collider delta 最大（0.078）因为二值化改变了条件化的有效类别结构——
      将 K=3 collider 折叠为 K=2 时，被合并类别的误分类模式发生质变而非仅量变。
      Delta 随 K 增大而增加（K=5 比 K=3 大 35%，K=7 比 K=3 大 62%），
      因为更多类别意味着更多折叠选择和更大的信息损失。
      方向反转仅在 collider K=5 的特定折叠方案下出现（1 个案例），
      因为只有当被合并的类别恰好包含反转效应的关键异质性时才会触发。
      Taxonomy 44% cells 有定性差异（median 范围 [0.35, 0.55]）——
      超过一半的 topology×structure 组合中二值化的偏差与多类偏差仅是量变。
      这限制了 binarization risk 作为 strong claim 的力度，
      但足以作为 "binarization is not a safe shortcut" 的支撑。
    tables:
      - name: "Table 11: Binarization Δ by topology × K"
        rows: ["confounding", "mediation", "collider", "M-bias", "instrument", "front-door"]
        columns: ["Δ_K3", "Δ_K5", "Δ_K7", "direction_change"]
        content_description: >
          Collider K=5 是唯一方向改变案例（Δ=0.078，从正变负）。
          其余全部为同方向的量变。
    figures_description:
      - "Figure 14: Binarization Δ heatmap — 6 topologies × 3 K values，标注方向反转 cell"
      - "Figure 15: Paired bar chart — 多类 vs 二值化偏差估计，6 topologies × K=5"
    analysis: >
      Binarization 风险作为第二支撑论据有效但非 dramatic。
      44% qualitative difference 意味着论文不能宣称 "binarization always dangerous"，
      而应说 "binarization introduces unpredictable bias in a substantial minority of scenarios,
      including one case of direction reversal"。
      MVP 的 Δ=0.089 属于偏高值；全面分析后平均水平为 0.058，headline 应调整预期。

  - name: "Pathological confusion matrix analysis"
    plan_id: "plan_009"
    description: >
      分析极端 C 结构（near-permutation, rank-deficient, block-diagonal）下的偏差行为，
      识别预测偏差严重性的结构条件。
    expected_results:
      catastrophic_bias_threshold_spectral_gap: 0.15
      diagonal_dominance_ratio_safe_threshold: 0.6
      near_permutation_max_bias: 0.85
      rank_deficient_identifiability_failure_rate: 0.35
      block_diagonal_bias_predictability: "high (R²=0.91 from block structure alone)"
      topologies_most_sensitive_to_pathological_C: ["collider", "m_bias"]
      practical_relevance: "low — current LLMs do not produce pathological C structures"
    result_rationale: >
      Near-permutation C（对角线 < 0.4）产生极大偏差（最高 0.85）因为误分类几乎是随机的，
      信号完全被噪声淹没。Spectral gap < 0.15 是 catastrophic 的阈值，因为这意味着
      C 矩阵的第一特征值与第二特征值之差过小，误分类不再保留类别间的任何序关系。
      Rank-deficient C 导致 35% 的情况下偏差不可识别（无法从观测数据推断真实效应方向），
      因为秩缺失意味着某些类别的区分信息完全丢失。
      Collider 和 M-bias 对 pathological C 最敏感，因为这两个拓扑本身引入额外的
      偏差路径（collider 开门，M-bias 多路径），极端误分类进一步放大这些路径。
      但实际相关性低——plan_003 显示当前 LLM 的对角优势比 0.55-0.82，远高于危险阈值。
    tables:
      - name: "Table 12: Pathological C regimes and bias consequences"
        rows: ["near-permutation", "rank-deficient", "block-diagonal", "extreme-asymmetric"]
        columns: ["max_bias", "identifiable", "topology_most_affected", "LLM_realistic"]
        content_description: >
          Near-permutation: bias 0.85, sometimes unidentifiable, collider, unrealistic；
          rank-deficient: bias varies, 35% unidentifiable, all, unrealistic；
          block-diagonal: bias 0.40, identifiable, M-bias, rare but possible；
          extreme-asymmetric: bias 0.55, identifiable, mediation, rare.
    figures_description:
      - "Figure 16: Phase diagram — spectral gap vs diagonal dominance → bias severity，6 topologies 叠加"
    analysis: >
      Pathological 分析主要服务于理论完整性和从业者的 "red flag" 工具开发。
      Phase diagram（Figure 16）可能是最有实用价值的输出——让使用者快速判断其 C 矩阵
      是否处于危险区域。但需在论文中明确说明当前 LLM 不产生此类 C 结构。

  - name: "annot-sensitivity Python toolkit"
    plan_id: "plan_010"
    description: >
      封装全部理论和计算工具为 pip-installable Python 包：
      DAG + C 矩阵 + 估计量 → 偏差表达式 + ASV + 校正建议 + 可视化。
    expected_results:
      api_coverage: "6 topologies × arbitrary K × 4 correction methods"
      computation_time_K3: "< 0.1s per scenario"
      computation_time_K7: "< 2s per scenario (MC-based)"
      test_coverage: 0.88
      documentation_examples: 6
      pypi_installable: true
      dependencies: ["numpy", "scipy", "matplotlib", "networkx"]
    result_rationale: >
      K=3 计算 < 0.1s 因为有闭式表达式可直接求值。
      K=7 需要 MC 辅助（矩阵逆数值不稳定性），因此 < 2s 包含 1000 reps MC。
      测试覆盖 88% 而非更高因为部分边界情况（pathological C 的数值稳定性处理）
      难以完全覆盖。6 个 worked examples 对应 6 个拓扑各一。
    tables: []
    figures_description:
      - "Figure 17: Toolkit workflow diagram — 输入 → 内部流程 → 输出的 schematic"
      - "Figure 18: Worked example output — protest 任务 confounding DAG 的完整诊断报告截图"
    analysis: >
      Toolkit 是 Claim 3 的实体化支撑和 reproducibility 保障。
      在 median 档下不是核心贡献但提升论文的实用价值和引用潜力。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "359ad4fd-3015-49c0-ac87-f867d223670c",
  "isSidechain": false,
  "requestId": "req_011CbDSG7K88t3UVE92j4B7z",
  "type": "assistant",
  "uuid": "a7ba68de-3a43-4cb1-861f-8f73bab99eba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "47795e28-b323-455e-bd89-9d1ed4fde7b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WzvpAoowrS8chKNd5v6fL2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10024,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10024,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11509,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10024
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：方向反转仅在 collider（或仅在窄条件下的 mediator）出现；ASV 单调性成立但紧致性部分依赖数值证据；实证异质性有限 核心假设：['方向反转存在但局限于特定拓扑或需要特定 C 结构条件（如对角优势比 < 阈值）', 'ASV 单调性在 3 个优先拓扑均成立，但紧致性仅 1-2 个有形式证明…",
  "leafUuid": "a7ba68de-3a43-4cb1-861f-8f73bab99eba",
  "sessionId": "47795e28-b323-455e-bd89-9d1ed4fde7b0"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-class annotation bias taxonomy and ASV framework",
  "sessionId": "47795e28-b323-455e-bd89-9d1ed4fde7b0"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：方向反转仅在 collider（或仅在窄条件下的 mediator）出现；ASV 单调性成立但紧致性部分依赖数值证据；实证异质性有限 核心假设：['方向反转存在但局限于特定拓扑或需要特定 C 结构条件（如对角优势比 < 阈值）', 'ASV 单调性在 3 个优先拓扑均成立，但紧致性仅 1-2 个有形式证明…",
  "leafUuid": "a7ba68de-3a43-4cb1-861f-8f73bab99eba",
  "sessionId": "47795e28-b323-455e-bd89-9d1ed4fde7b0"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-class annotation bias taxonomy and ASV framework",
  "sessionId": "47795e28-b323-455e-bd89-9d1ed4fde7b0"
}
```

---
