# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：方向反转在 mediator 和 collider 拓扑均被确认；ASV 框架理论性质完整证明；实证数据展示 taxonomy 的实用区分力 核心假设：

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/898815c0-f847-4638-9e6c-fec5f265ed2f.jsonl`
- **Structured JSON:** [`5c3bdef46a71c0b486cc.json`](../../sessions/5c/5c3bdef46a71c0b486cc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T07:30:44.056Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T07:30:44.056Z",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：方向反转在 mediator 和 collider 拓扑均被确认；ASV 框架理论性质完整证明；实证数据展示 taxonomy 的实用区分力\n核心假设：['非差异性多类误分类在 mediator/collider DAG 下产生方向反转（打破二分类保证）', 'ASV 单调性 + 紧致性在 3 个优先拓扑上均可形式化证明', '3 个 LLM 的经验混淆矩阵在结构上有足够异质性，落入 taxonomy 的不同 cell', 'K→2 折叠偏差在多数拓扑上显著（Δ > 0.05），证明二值化不安全']\n关键指标范围：{'direction_reversal_topologies': [2, 3], 'mc_theory_match_rate': [0.93, 1.0], 'asv_coverage_deviation_95': [0.0, 0.02], 'asv_sharpness_formal_proofs': [3, 3], 'binarization_delta_max': [0.08, 0.15], 'empirical_asv_discriminates': [0.8, 1.0], 'taxonomy_cells_with_qualitative_difference': [0.6, 0.8]}\n叙事方向：原始 framing 完全成立。标题主张 \"Multi-class errors are not created equal\" 有跨拓扑方向反转的硬证据支撑。 三条 claim 均可以最强形式陈述：完整 taxonomy（含反转条件）、ASV 有形式保证、correction guidance 有 MC 验证。 Headline result: \"非差异性多类误差在 confounding DAG 偏向零但在 mediator/collider DAG 反转方向—— 同一混淆矩阵在不同因果设计下产生定性相反的偏差，二值化无法规避。\"\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: causal_annot_error_attrib\nfocus: Key uncertainty: will mediator/collider DAGs show direction reversal under non-differential multi-class error? Confounding DAG was monotonic in MVP. Also: is ASV framework practically useful enough vs just reporting confusion matrices?\n\n## paper_framing.md\n\n# Paper Framing — causal_annot_error_attrib\n\n## Target Venue\n- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)\n- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)\n- Tertiary: ICWSM 2027 Round 2 (2026-09-15)\n\n## Title\nMulti-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies\n\n## Core Claims (3 条)\n\n1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 6 canonical social-science DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door).\n\n2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of differential annotation error needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Reported alongside estimates, analogous to E-values for unmeasured confounding. Formal proofs (monotonicity + sharpness) for 3 priority topologies; MC-validated conjectures for the remaining 3.\n\n3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI, MLA, naive plug-in), characterizing regimes where each applies and where no existing method suffices — including dependence-aware multi-LLM correction as an open problem.\n\n## Story Spine\n\n- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31% of downstream conclusions are already incorrect. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable.\n\n- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.\n\n- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.\n\n- **Headline result template**: \"Across 6 DAG topologies with K=3,5,7, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. On 3 CSS tasks annotated by 3 LLMs, ASVs provide calibrated robustness indicators, and our taxonomy identifies cases where commonly applied corrections would increase rather than decrease bias.\"\n\n## Core Insight (Lead Finding)\n\nThe binary guarantee that \"non-differential misclassification biases toward the null\" breaks in the multi-class case (Brenner 1993). But Brenner only identifies the danger without resolving the ambiguity. Our taxonomy resolves it: for each {confusion matrix structure × DAG topology} cell, we provide exact conditions determining when bias attenuates, amplifies, or reverses. Furthermore, the natural \"fix\" of binarizing a K-class variable is itself hazardous — collapsing categories introduces new, direction-unpredictable bias (demonstrated in MVP: Δ up to 0.089 between K=3 and binarized estimates).\n\n## MVP Evidence\n\nConfounding DAG + K=3 validated:\n- Theoretical bias expressions match MC perfectly (5/5 structures within 95% CI)\n- All non-differential C structures produce positive bias 0.20-0.30 (toward OVB)\n- Binary collapse produces different bias (max Δ=0.089)\n- 100k random C search: confounding DAG bias is monotonically toward OVB (no direction reversal in this topology)\n- Direction reversal expected in mediator/collider topologies — research phase priority\n\n## Venue Fit Risks\n\n- **AAAI**: Broad AI audience — emphasize general methodology for \"automated annotation measurement error,\" not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.\n- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.\n- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n1. **\"Trivial extension of binary to multi-class\"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 6 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]\n\n2. **\"Lee & Wood-Doughty (2024) already did categorical\"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 6 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]\n\n3. **\"Why these 6 DAG topologies?\"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]\n\n4. **\"K≥5 expressions aren't actionable\"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]\n\n5. **\"ASV sharpness only proved for 3 topologies\"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]\n\n6. **\"Correlated multi-LLM errors?\"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]\n\n7. **\"Empirical validation scope\"** → 3 CSS tasks × 3 LLMs × 3 DAG-relevant scenarios. Tasks selected to cover K=2,3,5 annotation complexity. [Experiments: plan_003, plan_006]\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: Derive and MC-validate bias expressions for 6 DAG topologies with K=3\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n  details: 'For each topology (confounding, mediation, collider, M-bias, instrument,\n    front-door): derive closed-form K=3 bias expression, validate with MC (1000 reps\n    × N=10000, 6 confusion matrix structures including near-permutation extreme).\n    Key question: which topologies show direction reversal under non-differential\n    error? Confounding already validated in MVP (no reversal, monotonic toward OVB).\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  description: Extend bias expressions to K=5,7 — matrix notation + interpretability\n    tools\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'Matrix-form expressions for general K. Three interpretability tools: (a)\n    eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar\n    bounds collapsing matrix to conservative scalar, (c) diagnostic visualizations\n    mapping confusion matrix regions to bias magnitude. Validate on confounding +\n    mediation + collider DAGs with K=5,7.\n\n    '\n  status: planned\n- id: plan_003\n  claim: 1\n  description: 'Empirical confusion matrices: 3 LLMs × 3 CSS tasks vs gold-standard'\n  priority: P0\n  gpu_budget_hours: 0\n  api_cost_estimate: $300-550\n  deps: []\n  details: 'Tasks: protest event coding (K=5, ACLED/GPT-RE), stance detection (K=3,\n    SemEval/VAST), toxicity (K=2, as special case / consistency check, Civil Comments).\n    Models: Llama 4 Maverick (Together.ai), Qwen 3.5 Plus (OpenRouter), DeepSeek V4\n    (DeepSeek API). ~30K annotations per model × 3 datasets × 3 prompt variants. Output:\n    empirical confusion matrices, inter-model correlation analysis, downstream regression\n    bias vs gold-standard baseline.\n\n    '\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Binarization collapse analysis: K→2 folding bias across all 6 topologies'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'For each of 6 topologies with K=3,5,7: collapse to binary, compare bias\n    from full multi-class expression vs binarized expression. Demonstrate that binarization\n    is not a safe shortcut — can amplify or reverse bias. MVP showed Δ up to 0.089\n    for confounding DAG K=3.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'ASV framework: formal proofs for confounding, mediation, collider'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'Derive ASV expressions for 3 priority topologies. Formal proofs of: (a)\n    monotonicity (ASV increases with δ amplification), (b) sharpness (bound is achievable\n    for some confusion matrix). MC validation: coverage at 90%, 95%, 99% levels across\n    1000 scenarios.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 2\n  description: ASV MC validation for M-bias, instrument, front-door topologies\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_004\n  details: 'ASV expressions + MC validation of monotonicity and coverage. Sharpness\n    stated as conjectures supported by numerical evidence. If any topology fails monotonicity\n    under MC, flag and investigate.\n\n    '\n  status: planned\n- id: plan_006\n  claim: 2\n  description: ASV calibration on empirical data (3 CSS tasks × 3 LLMs)\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  - plan_004\n  details: 'Apply ASVs to empirical confusion matrices from plan_003. Validate coverage\n    on held-out gold-standard splits. Report ASV alongside downstream effect estimates\n    for each task. Compare ASV interpretability with raw confusion matrix reporting.\n\n    '\n  status: planned\n- id: plan_007\n  claim: 3\n  description: 'Correction guidance framework: decision mapping + validation'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_004\n  - plan_003\n  details: 'Decision framework: {topology × error structure × ASV} → correction method\n    (DSL / PPI / MLA / naive plug-in / \"no existing method adequate\"). MC validation:\n    recommended method produces least bias in ≥90% of scenarios. Empirical validation\n    on plan_003 data. Characterize regimes where no existing method suffices (correlated\n    errors, differential multi-class, etc.) — identify as open problems.\n\n    '\n  status: planned\n- id: plan_009\n  claim: 1\n  description: Pathological confusion matrix analysis (near-permutation, rank-deficient)\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  details: 'Extreme C structures: near-permutation, rank-deficient, block-diagonal.\n    Characterize when bias becomes catastrophic across topologies. Identify structural\n    conditions (spectral gap, diagonal dominance ratio) that predict bias severity\n    — candidate features for practitioners.\n\n    '\n  status: planned\n- id: plan_010\n  claim: all\n  description: annot-sensitivity Python toolkit (open-source release)\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_004\n  - plan_007\n  details: 'Package: user-specified DAG + confusion matrix(es) + downstream estimate\n    → bias expressions (scalar K≤3, matrix K>3 with interpretability) + ASV bounds\n    + sensitivity curves + correction recommendation + diagnostic plots. pip-installable,\n    with worked examples for each topology.\n\n    '\n  status: planned\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T07:30:44.060Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T07:30:44.060Z",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-20T07:30:44.100Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：方向反转在 mediator 和 collider 拓扑均被确认；ASV 框架理论性质完整证明；实证数据展示 taxonomy 的实用区分力
核心假设：['非差异性多类误分类在 mediator/collider DAG 下产生方向反转（打破二分类保证）', 'ASV 单调性 + 紧致性在 3 个优先拓扑上均可形式化证明', '3 个 LLM 的经验混淆矩阵在结构上有足够异质性，落入 taxonomy 的不同 cell', 'K→2 折叠偏差在多数拓扑上显著（Δ > 0.05），证明二值化不安全']
关键指标范围：{'direction_reversal_topologies': [2, 3], 'mc_theory_match_rate': [0.93, 1.0], 'asv_coverage_deviation_95': [0.0, 0.02], 'asv_sharpness_formal_proofs': [3, 3], 'binarization_delta_max': [0.08, 0.15], 'empirical_asv_discriminates': [0.8, 1.0], 'taxonomy_cells_with_qualitative_difference': [0.6, 0.8]}
叙事方向：原始 framing 完全成立。标题主张 "Multi-class errors are not created equal" 有跨拓扑方向反转的硬证据支撑。 三条 claim 均可以最强形式陈述：完整 taxonomy（含反转条件）、ASV 有形式保证、correction guidance 有 MC 验证。 Headline result: "非差异性多类误差在 confounding DAG 偏向零但在 mediator/collider DAG 反转方向—— 同一混淆矩阵在不同因果设计下产生定性相反的偏差，二值化无法规避。"


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
  "promptId": "30f22a65-d3f1-4c77-944b-50b488040b24",
  "type": "user",
  "uuid": "e65e097d-3702-4c71-97e7-43ac49af92d0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T07:30:44.099Z_

```json
{
  "parentUuid": "e65e097d-3702-4c71-97e7-43ac49af92d0",
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
  "uuid": "b0478465-d589-48c9-aede-be30b36e9d9b",
  "timestamp": "2026-05-20T07:30:44.099Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T07:30:44.099Z_

```json
{
  "parentUuid": "b0478465-d589-48c9-aede-be30b36e9d9b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1d19d4fb-8215-4dfd-8885-510b680ec2b7",
  "timestamp": "2026-05-20T07:30:44.099Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：方向反转在 mediator 和 collider 拓扑均被确认；ASV 框架理论性质完整证明；实证数据展示 taxonomy 的实用区分力 核心假设：['非差异性多类误分类在 mediator/collider DAG 下产生方向反转（打破二分类保证）', 'ASV 单调性 + 紧致性在 3 个优先拓扑上均…",
  "leafUuid": "1d19d4fb-8215-4dfd-8885-510b680ec2b7",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-class annotation errors and causal DAG bias",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f"
}
```

---

### Tool call

_source line 8 · 2026-05-20T07:30:48.931Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G6qmwTzkNEVF9Xmw7esUz3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/.claude/CLAUDE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d19d4fb-8215-4dfd-8885-510b680ec2b7",
  "isSidechain": false,
  "requestId": "req_011CbDRryNzbLH6knR5hTrnM",
  "type": "assistant",
  "uuid": "8e3932b2-00ae-4587-b72a-dc2d2b9c7684",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmavNtzdNwZJpPVDv1qDum",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9832,
      "cache_read_input_tokens": 11841,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 143,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9832
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

_source line 9 · 2026-05-20T07:30:48.947Z_

<details><summary>↩ Tool result · `toolu_01G6qmwTzkNEVF9Xmw7esUz3`</summary>

```text
1	
2	## 输出风格
3	
4	- 回复简洁直接，不说废话
5	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
6	- 不要复述用户的问题
7	- 不要给未被要求的建议或补充说明
8	- 推理要彻底，但输出只保留结论和必要信息
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e3932b2-00ae-4587-b72a-dc2d2b9c7684",
  "isSidechain": false,
  "promptId": "30f22a65-d3f1-4c77-944b-50b488040b24",
  "type": "user",
  "uuid": "20b9e6a7-f537-407e-9d09-a47cbc9cff9c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "8e3932b2-00ae-4587-b72a-dc2d2b9c7684",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T07:30:49.334Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DZVJDTtvgxoeUDrXabqATA`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20b9e6a7-f537-407e-9d09-a47cbc9cff9c",
  "isSidechain": false,
  "requestId": "req_011CbDRryNzbLH6knR5hTrnM",
  "type": "assistant",
  "uuid": "ff2722b7-aaac-4fd3-9aaf-a45e3dd579b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmavNtzdNwZJpPVDv1qDum",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9832,
      "cache_read_input_tokens": 11841,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 143,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9832
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

_source line 11 · 2026-05-20T07:30:49.359Z_

<details><summary>↩ Tool result · `toolu_01DZVJDTtvgxoeUDrXabqATA`</summary>

```text
.claude/sessions/no_project_44c41a86/CLAUDE.md
.claude/sessions/no_project_44c41a86/AGENTS.md
projects/crosscoder-behavioral-circuit-transplant/report.md
projects/crosscoder-behavioral-circuit-transplant/.claude/sessions/agent_5372568e/CLAUDE.md
projects/crosscoder-behavioral-circuit-transplant/.claude/sessions/agent_5372568e/AGENTS.md
projects/crosscoder-behavioral-circuit-transplant/ROADMAP.md
projects/crosscoder-behavioral-circuit-transplant/.claude/sessions/reviewer_36afb175/CLAUDE.md
projects/crosscoder-behavioral-circuit-transplant/.claude/sessions/reviewer_36afb175/AGENTS.md
projects/crosscoder-behavioral-circuit-transplant/memory.md
projects/crosscoder-behavioral-circuit-transplant/.claude/CLAUDE.md
projects/crosscoder-behavioral-circuit-transplant/AGENTS.md
projects/crosscoder-behavioral-circuit-transplant/.claude/sessions/director_ba797b8e/CLAUDE.md
projects/crosscoder-behavioral-circuit-transplant/.claude/sessions/director_ba797b8e/AGENTS.md
projects/diagprm-stage-reasoning/.claude/sessions/agent_b15d9aa0/CLAUDE.md
projects/diagprm-stage-reasoning/.claude/sessions/agent_b15d9aa0/AGENTS.md
projects/diagprm-stage-reasoning/docs/IDEA_BRIEF.md
projects/diagprm-stage-reasoning/.claude/sessions/reviewer_c27eb032/memory/project_initial_state.md
projects/diagprm-stage-reasoning/.claude/sessions/reviewer_c27eb032/memory/MEMORY.md
projects/diagprm-stage-reasoning/ROADMAP.md
projects/diagprm-stage-reasoning/artifacts/swe-smith-trajectory-research.md
projects/diagprm-stage-reasoning/.claude/sessions/reviewer_c27eb032/CLAUDE.md
projects/diagprm-stage-reasoning/.claude/sessions/reviewer_c27eb032/AGENTS.md
projects/diagprm-stage-reasoning/.claude/sessions/agent_d93749be/CLAUDE.md
projects/diagprm-stage-reasoning/.claude/sessions/agent_d93749be/AGENTS.md
.claude/sessions/no_project_13c29b16/CLAUDE.md
.claude/sessions/no_project_13c29b16/AGENTS.md
.claude/sessions/no_project_98c20cb1/CLAUDE.md
.claude/sessions/no_project_98c20cb1/AGENTS.md
.claude/sessions/idea_reviewer_9575c084/CLAUDE.md
.claude/sessions/idea_reviewer_9575c084/AGENTS.md
projects/diagprm-stage-reasoning/.claude/CLAUDE.md
projects/diagprm-stage-reasoning/AGENTS.md
projects/diagprm-stage-reasoning/.claude/sessions/director_18874762/CLAUDE.md
projects/diagprm-stage-reasoning/.claude/sessions/director_18874762/AGENTS.md
.claude/sessions/no_project_18960d1d/CLAUDE.md
.claude/sessions/no_project_18960d1d/AGENTS.md
projects/causal_annot_error_attrib/memory.md
projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d/CLAUDE.md
projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d/AGENTS.md
projects/causal_annot_error_attrib/docs/IDEA_BRIEF.md
projects/causal_annot_error_attrib/paper_framing.md
projects/causal_annot_error_attrib/.claude/sessions/reviewer_15d8e49e/CLAUDE.md
projects/causal_annot_error_attrib/.claude/sessions/reviewer_15d8e49e/AGENTS.md
.claude/CLAUDE.md
AGENTS.md
projects/causal_annot_error_attrib/.claude/CLAUDE.md
projects/causal_annot_error_attrib/AGENTS.md
projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73/CLAUDE.md
projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73/AGENTS.md
projects/causal_annot_error_attrib/ROADMAP.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff2722b7-aaac-4fd3-9aaf-a45e3dd579b3",
  "isSidechain": false,
  "promptId": "30f22a65-d3f1-4c77-944b-50b488040b24",
  "type": "user",
  "uuid": "4272e1d2-ffff-42d1-b5c6-7df1c94d514c",
  "toolUseResult": {
    "filenames": [
      ".claude/sessions/no_project_44c41a86/CLAUDE.md",
      ".claude/sessions/no_project_44c41a86/AGENTS.md",
      "projects/crosscoder-behavioral-circuit-transplant/report.md",
      "projects/crosscoder-behavioral-circuit-transplant/.claude/sessions/agent_5372568e/CLAUDE.md",
      "projects/crosscoder-behavioral-circuit-transplant/.claude/sessions/agent_5372568e/AGENTS.md",
      "projects/crosscoder-behavioral-circuit-transplant/ROADMAP.md",
      "projects/crosscoder-behavioral-circuit-transplant/.claude/sessions/reviewer_36afb175/CLAUDE.md",
      "projects/crosscoder-behavioral-circuit-transplant/.claude/sessions/reviewer_36afb175/AGENTS.md",
      "projects/crosscoder-behavioral-circuit-transplant/memory.md",
      "projects/crosscoder-behavioral-circuit-transplant/.claude/CLAUDE.md",
      "projects/crosscoder-behavioral-circuit-transplant/AGENTS.md",
      "projects/crosscoder-behavioral-circuit-transplant/.claude/sessions/director_ba797b8e/CLAUDE.md",
      "projects/crosscoder-behavioral-circuit-transplant/.claude/sessions/director_ba797b8e/AGENTS.md",
      "projects/diagprm-stage-reasoning/.claude/sessions/agent_b15d9aa0/CLAUDE.md",
      "projects/diagprm-stage-reasoning/.claude/sessions/agent_b15d9aa0/AGENTS.md",
      "projects/diagprm-stage-reasoning/docs/IDEA_BRIEF.md",
      "projects/diagprm-stage-reasoning/.claude/sessions/reviewer_c27eb032/memory/project_initial_state.md",
      "projects/diagprm-stage-reasoning/.claude/sessions/reviewer_c27eb032/memory/MEMORY.md",
      "projects/diagprm-stage-reasoning/ROADMAP.md",
      "projects/diagprm-stage-reasoning/artifacts/swe-smith-trajectory-research.md",
      "projects/diagprm-stage-reasoning/.claude/sessions/reviewer_c27eb032/CLAUDE.md",
      "projects/diagprm-stage-reasoning/.claude/sessions/reviewer_c27eb032/AGENTS.md",
      "projects/diagprm-stage-reasoning/.claude/sessions/agent_d93749be/CLAUDE.md",
      "projects/diagprm-stage-reasoning/.claude/sessions/agent_d93749be/AGENTS.md",
      ".claude/sessions/no_project_13c29b16/CLAUDE.md",
      ".claude/sessions/no_project_13c29b16/AGENTS.md",
      ".claude/sessions/no_project_98c20cb1/CLAUDE.md",
      ".claude/sessions/no_project_98c20cb1/AGENTS.md",
      ".claude/sessions/idea_reviewer_9575c084/CLAUDE.md",
      ".claude/sessions/idea_reviewer_9575c084/AGENTS.md",
      "projects/diagprm-stage-reasoning/.claude/CLAUDE.md",
      "projects/diagprm-stage-reasoning/AGENTS.md",
      "projects/diagprm-stage-reasoning/.claude/sessions/director_18874762/CLAUDE.md",
      "projects/diagprm-stage-reasoning/.claude/sessions/director_18874762/AGENTS.md",
      ".claude/sessions/no_project_18960d1d/CLAUDE.md",
      ".claude/sessions/no_project_18960d1d/AGENTS.md",
      "projects/causal_annot_error_attrib/memory.md",
      "projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d/CLAUDE.md",
      "projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d/AGENTS.md",
      "projects/causal_annot_error_attrib/docs/IDEA_BRIEF.md",
      "projects/causal_annot_error_attrib/paper_framing.md",
      "projects/causal_annot_error_attrib/.claude/sessions/reviewer_15d8e49e/CLAUDE.md",
      "projects/causal_annot_error_attrib/.claude/sessions/reviewer_15d8e49e/AGENTS.md",
      ".claude/CLAUDE.md",
      "AGENTS.md",
      "projects/causal_annot_error_attrib/.claude/CLAUDE.md",
      "projects/causal_annot_error_attrib/AGENTS.md",
      "projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73/CLAUDE.md",
      "projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73/AGENTS.md",
      "projects/causal_annot_error_attrib/ROADMAP.md"
    ],
    "durationMs": 19,
    "numFiles": 50,
    "truncated": false
  },
  "sourceToolAssistantUUID": "ff2722b7-aaac-4fd3-9aaf-a45e3dd579b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T07:30:52.918Z_

<details open><summary>🔧 Tool call — Read · `toolu_014tsLZYHqtQaEbNnZTpsCGj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4272e1d2-ffff-42d1-b5c6-7df1c94d514c",
  "isSidechain": false,
  "requestId": "req_011CbDRsMqrLzcvci3jgy9oA",
  "type": "assistant",
  "uuid": "e9e74ec9-5adf-4f93-ad39-b4aa6afa7a9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVqEQsSKdyuQ3a9eGDGJPK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1499,
      "cache_read_input_tokens": 21673,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1499,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 226,
          "cache_read_input_tokens": 21673,
          "cache_creation_input_tokens": 1499,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1499
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

_source line 13 · 2026-05-20T07:30:52.923Z_

<details><summary>↩ Tool result · `toolu_014tsLZYHqtQaEbNnZTpsCGj`</summary>

```text
1	# Project Memory
2	
3	## MVP 验证发现 (2026-05-20)
4	
5	### Confounding DAG 偏差方向性质
6	100k 随机列随机 C 矩阵搜索（两组 DGP 参数）均未发现负偏差。Confounding DAG (A→T, A→Y, T→Y) 中，K=3 多分类误分类偏差始终与 OVB 同向。**方向反转（偏差符号翻转）可能需要其他 DAG 拓扑**（mediator, collider, M-bias 等）来实现。
7	
8	这意味着项目核心假设"偏差方向取决于 C 结构与 DAG 拓扑的交互"在 confounding DAG 下只体现为**量级差异**（K=3 vs binary collapse），而非方向差异。若要证明多分类的本质区别，需要跨 DAG 对比。
9	
10	### DGP 参数选择
11	MVP 使用 P(A)=[0.4, 0.35, 0.25], alpha=[1.5, -1.0], beta_T=2.0, beta_A=[1.0, -0.5], sigma_T=sigma_Y=1.0。类别效应方向：A=1 对 T 和 Y 均正向，A=2 对 T 负向、对 Y 也负向。OVB=+0.30。
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9e74ec9-5adf-4f93-ad39-b4aa6afa7a9e",
  "isSidechain": false,
  "promptId": "30f22a65-d3f1-4c77-944b-50b488040b24",
  "type": "user",
  "uuid": "e83cdd50-6297-4d1d-889b-70aab29cf666",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/memory.md",
      "content": "# Project Memory\n\n## MVP 验证发现 (2026-05-20)\n\n### Confounding DAG 偏差方向性质\n100k 随机列随机 C 矩阵搜索（两组 DGP 参数）均未发现负偏差。Confounding DAG (A→T, A→Y, T→Y) 中，K=3 多分类误分类偏差始终与 OVB 同向。**方向反转（偏差符号翻转）可能需要其他 DAG 拓扑**（mediator, collider, M-bias 等）来实现。\n\n这意味着项目核心假设\"偏差方向取决于 C 结构与 DAG 拓扑的交互\"在 confounding DAG 下只体现为**量级差异**（K=3 vs binary collapse），而非方向差异。若要证明多分类的本质区别，需要跨 DAG 对比。\n\n### DGP 参数选择\nMVP 使用 P(A)=[0.4, 0.35, 0.25], alpha=[1.5, -1.0], beta_T=2.0, beta_A=[1.0, -0.5], sigma_T=sigma_Y=1.0。类别效应方向：A=1 对 T 和 Y 均正向，A=2 对 T 负向、对 Y 也负向。OVB=+0.30。\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  },
  "sourceToolAssistantUUID": "e9e74ec9-5adf-4f93-ad39-b4aa6afa7a9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T07:30:53.421Z_

<details open><summary>🔧 Tool call — Read · `toolu_017NmDmyjBFxw3S3kT5GBdLg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e83cdd50-6297-4d1d-889b-70aab29cf666",
  "isSidechain": false,
  "requestId": "req_011CbDRsMqrLzcvci3jgy9oA",
  "type": "assistant",
  "uuid": "17656846-0a51-440c-b05f-7c1be00c3a0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVqEQsSKdyuQ3a9eGDGJPK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1499,
      "cache_read_input_tokens": 21673,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1499,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 226,
          "cache_read_input_tokens": 21673,
          "cache_creation_input_tokens": 1499,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1499
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

_source line 15 · 2026-05-20T07:30:53.426Z_

<details><summary>↩ Tool result · `toolu_017NmDmyjBFxw3S3kT5GBdLg`</summary>

```text
1	# causal_annot_error_attrib — Research Dashboard
2	
3	> 最后更新: 2026-05-20 07:29 UTC | 更新原因: MVP 通过，进入 research 阶段，写完 framing + plan + 提交 dream
4	
5	## 核心方向
6	多分类 LLM 标注误差在因果推断中的偏差传播：推导 K×K 混淆矩阵在 6 种 DAG 拓扑下的偏差表达式，构建 Annotation Sensitivity Values (ASVs) 灵敏度分析框架。详见 paper_framing.md。
7	
8	## 当前阶段：Research（MVP 2026-05-20 通过）
9	
10	### MVP 结论
11	Confounding DAG + K=3 验证通过。理论框架正确（5/5 MC 匹配），多分类≠二分类已量化（Δ≤0.089）。Confounding DAG 偏差单调向 OVB（100k 随机 C 无方向反转）。方向反转需在其他拓扑验证。
12	
13	### Target Venue
14	- Primary: AAAI 2027（abstract 2026-07-21, paper 2026-07-28）
15	- Secondary: ARR October 2026（→ NAACL/ACL 2027）
16	
17	### Core Claims（详见 paper_framing.md）
18	1. Multi-class bias taxonomy — 6 DAG 拓扑 × K×K 混淆矩阵结构交互
19	2. Annotation Sensitivity Values (ASVs) — 标注误差灵敏度分析
20	3. Correction guidance framework — 诊断驱动的纠偏方法选择
21	
22	### 实验覆盖（详见 experiment_plan.yaml，compute_coverage_matrix 派生）
23	- P0 (必跑): plan_001(6 DAG K=3), plan_003(3 LLM实证), plan_004(ASV证明), plan_006(ASV实证), plan_008(二分类折叠)
24	- P1 (重要): plan_002(K=5,7), plan_005(ASV扩展), plan_007(纠偏框架), plan_010(工具包)
25	- P2 (加分): plan_009(病态C分析)
26	
27	## 当前进展
28	- ✅ MVP 通过（D001）
29	- ✅ paper_framing.md 已写
30	- ✅ experiment_plan.yaml 已写
31	- ⏳ Dream 模拟已提交（full review），等待回调
32	- ⏳ Reviewer 验证 MVP 结果中
33	
34	## 近期任务
35	- [ ] 等 Dream 回调，评估 framing/plan 是否需调整
36	- [ ] 等 Reviewer MVP 验证结果
37	- [ ] Dream 通过后：派 Agent 启动 plan_001（6 DAG 拓扑推导 + MC）
38	- [ ] 并行：plan_003 需要 API key（Llama 4 / Qwen 3.5 / DeepSeek V4）+ 金标数据集
39	
40	## GPU 预算
41	本项目 GPU 需求极低（总计 15-30h，后期 LLM API 实证用）。当前 0 GPU 分配。
42	服务器：home-1x5090（sonny），已绑定。
43	
44	## 关键风险
45	1. 方向反转是否出现——confounding 单调，mediator/collider 是否也单调？若 6 拓扑全部单调，Claim 1 最强形式需降级
46	2. Lee & Wood-Doughty (2024) 重叠——已区分 observed vs unobserved confounding
47	3. AAAI DDL 2 个月——紧但 AI 团队速度可行
48	
49	## 关键决策日志
50	
51	| ID | 日期 | 摘要 | 关联实验 |
52	|----|------|------|----------|
53	| D002 | 2026-05-20 | Research 阶段第一优先级：exposure misclassification DAG K= | — |
54	| D001 | 2026-05-20 | MVP PASS — Confounding DAG K=3 理论框架验证通过，进入 researc | — |
55	
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17656846-0a51-440c-b05f-7c1be00c3a0b",
  "isSidechain": false,
  "promptId": "30f22a65-d3f1-4c77-944b-50b488040b24",
  "type": "user",
  "uuid": "2c98c053-8632-4840-83ad-9067b9be58ff",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/ROADMAP.md",
      "content": "# causal_annot_error_attrib — Research Dashboard\n\n> 最后更新: 2026-05-20 07:29 UTC | 更新原因: MVP 通过，进入 research 阶段，写完 framing + plan + 提交 dream\n\n## 核心方向\n多分类 LLM 标注误差在因果推断中的偏差传播：推导 K×K 混淆矩阵在 6 种 DAG 拓扑下的偏差表达式，构建 Annotation Sensitivity Values (ASVs) 灵敏度分析框架。详见 paper_framing.md。\n\n## 当前阶段：Research（MVP 2026-05-20 通过）\n\n### MVP 结论\nConfounding DAG + K=3 验证通过。理论框架正确（5/5 MC 匹配），多分类≠二分类已量化（Δ≤0.089）。Confounding DAG 偏差单调向 OVB（100k 随机 C 无方向反转）。方向反转需在其他拓扑验证。\n\n### Target Venue\n- Primary: AAAI 2027（abstract 2026-07-21, paper 2026-07-28）\n- Secondary: ARR October 2026（→ NAACL/ACL 2027）\n\n### Core Claims（详见 paper_framing.md）\n1. Multi-class bias taxonomy — 6 DAG 拓扑 × K×K 混淆矩阵结构交互\n2. Annotation Sensitivity Values (ASVs) — 标注误差灵敏度分析\n3. Correction guidance framework — 诊断驱动的纠偏方法选择\n\n### 实验覆盖（详见 experiment_plan.yaml，compute_coverage_matrix 派生）\n- P0 (必跑): plan_001(6 DAG K=3), plan_003(3 LLM实证), plan_004(ASV证明), plan_006(ASV实证), plan_008(二分类折叠)\n- P1 (重要): plan_002(K=5,7), plan_005(ASV扩展), plan_007(纠偏框架), plan_010(工具包)\n- P2 (加分): plan_009(病态C分析)\n\n## 当前进展\n- ✅ MVP 通过（D001）\n- ✅ paper_framing.md 已写\n- ✅ experiment_plan.yaml 已写\n- ⏳ Dream 模拟已提交（full review），等待回调\n- ⏳ Reviewer 验证 MVP 结果中\n\n## 近期任务\n- [ ] 等 Dream 回调，评估 framing/plan 是否需调整\n- [ ] 等 Reviewer MVP 验证结果\n- [ ] Dream 通过后：派 Agent 启动 plan_001（6 DAG 拓扑推导 + MC）\n- [ ] 并行：plan_003 需要 API key（Llama 4 / Qwen 3.5 / DeepSeek V4）+ 金标数据集\n\n## GPU 预算\n本项目 GPU 需求极低（总计 15-30h，后期 LLM API 实证用）。当前 0 GPU 分配。\n服务器：home-1x5090（sonny），已绑定。\n\n## 关键风险\n1. 方向反转是否出现——confounding 单调，mediator/collider 是否也单调？若 6 拓扑全部单调，Claim 1 最强形式需降级\n2. Lee & Wood-Doughty (2024) 重叠——已区分 observed vs unobserved confounding\n3. AAAI DDL 2 个月——紧但 AI 团队速度可行\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D002 | 2026-05-20 | Research 阶段第一优先级：exposure misclassification DAG K= | — |\n| D001 | 2026-05-20 | MVP PASS — Confounding DAG K=3 理论框架验证通过，进入 researc | — |\n\n",
      "numLines": 56,
      "startLine": 1,
      "totalLines": 56
    }
  },
  "sourceToolAssistantUUID": "17656846-0a51-440c-b05f-7c1be00c3a0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T07:30:53.677Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KqV26gXJUW7NeF8wUdudx6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c98c053-8632-4840-83ad-9067b9be58ff",
  "isSidechain": false,
  "requestId": "req_011CbDRsMqrLzcvci3jgy9oA",
  "type": "assistant",
  "uuid": "f2e6a151-07c4-4c33-91c2-2dcf20108039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVqEQsSKdyuQ3a9eGDGJPK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1499,
      "cache_read_input_tokens": 21673,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1499,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 226,
          "cache_read_input_tokens": 21673,
          "cache_creation_input_tokens": 1499,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1499
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

_source line 17 · 2026-05-20T07:30:53.965Z_

<details><summary>↩ Tool result · `toolu_01KqV26gXJUW7NeF8wUdudx6`</summary>

```text
1	# Idea Brief: When Do LLM Annotation Errors Matter? Multi-Class Bias Expressions and Annotation Sensitivity Values for Downstream Social Science Inference
2	
3	
4	- **Idea ID**: `idea_027`
5	- **Created**: 2026-05-20
6	- **Approved**: 2026-05-20
7	- **Source**: foreign:be-idea-gen-0515-4
8	- **Level**: solid
9	- **Target Venues**: ARR October 2026 (deadline: ~2026-10-15; commit to NAACL 2027 or later *ACL venues), AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28), ICWSM 2027 Round 2 (deadline: 2026-09-15)
10	
11	## Seed Topic
12	
13	web_research
14	
15	## Generation Journey
16	
17	1. **Start** — 开始生成，seed: '## Seed 4: Open-Vocabulary Affordance Zero-Shot VLA\n\nObjective: CoRL 2026 submission.\n\nDirection: Traditional affordance methods and VLAs rely on fixed category annotations and struggle with open-world unknown objects and free-form interaction instructions. CoA-VLA (arXiv 2412.20451, December 2024) integrates affordance chain-of-reasoning into VLA, but uses 4 predefined structured affordance types (object, grasp, spatial, motion) — not truly open-vocabulary — and cannot handle free-form interaction descriptions like "use this thing to wipe off the dust over there." GeneralVLA (arXiv 2602.04315, February 2026) achieves zero-shot affordance perception and manipulation trajectory generation through VLM+SAM, but is a modular three-stage pipeline (affordance perception → trajectory planning → low-level control), not a unified end-to-end VLA — with information loss between modules and inability to jointly optimize. OVAL-Prompt (ICRA 2024 VLMNM Workshop, arXiv 2404.11000) achieves truly open-vocabulary affordance localization, but only performs detection/localization without generating actions. AffordDP (CVPR 2025, arXiv 2412.03142) achieves affordance cross-category transfer through 3D contact points and trajectories, but completely lacks language conditioning. Core gap: No work unifies open-vocabulary affordance reasoning into an end-to-end VLA for zero-shot manipulation — existing work either has fixed affordance types (CoA-VLA), or is a modular pipeline (GeneralVLA), or only does detection without actions (OVAL-Prompt), or lacks language (AffordDP).\n\nSeed Papers:\n- "OpenVLA: An Open-Source Vision-Language-Action Model" (Kim et al., CoRL 2024, arXiv 2406.09246)\n  — 7B parameter open-source VLA, trained on 970K real robot demonstrations, establishing the VLA open-source paradigm. The base architecture for this work — integrating open-vocabulary affordance reasoning on top.\n- "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance" (Li et al., arXiv 2412.20451, December 2024)\n  — Integrates affordance chain-of-reasoning into VLA: model sequentially reasons about object affordance, grasp affordance, spatial affordance, and motion affordance before predicting actions. Uses visual-language collaborative injection module. Surpasses OpenVLA and Octo. Key limitation: 4 affordance types are predefined/structured, not open-vocabulary — cannot handle arbitrary natural language descriptions of novel interactions.\n- "GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning" (Ma et al., arXiv 2602.04315, February 2026)\n  — Hierarchical three-module pipeline: (1) VLM+SAM affordance perception for keypoint detection, (2) mid-level planning agent for trajectory generation, (3) low-level control policy. Achieves zero-shot manipulation across 14 tasks without real-world data. Key limitation: Modular pipeline, not end-to-end — affordance module, trajectory planner, and controller are separated, with information bottlenecks between modules.\n- "OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot Manipulation through LLM Affordance-Grounding" (Tong et al., ICRA 2024 VLMNM Workshop, arXiv 2404.11000)\n  — Prompt-based method combining VLM for object part segmentation and LLM for part-affordance grounding mapping, achieving open-vocabulary affordance localization without prior training. Competitive with supervised methods on localization benchmarks. Key limitation: Only performs affordance detection/localization, does not generate robot actions — a perception module, not a complete manipulation system.\n- "AffordDP: Generalizable Diffusion Policy with Transferable Affordance" (Wu et al., CVPR 2025, arXiv 2412.03142)\n  — Models manipulation priors through 3D contact points and post-contact trajectories, achieving affordance cross-category transfer using visual models + point cloud registration. Affordance-guided diffusion policy generates actions. Key limitation: No language conditioning — affordances are geometric/contact-based, not language-driven, cannot handle open-vocabulary instructions.\n\nKnown Gap:\n- CoA-VLA integrates affordance into VLA but uses predefined structured types, does not support open vocabulary\n- GeneralVLA does zero-shot affordance manipulation but is a modular pipeline, not end-to-end\n- OVAL-Prompt does open-vocabulary affordance but only detection, no action generation\n- AffordDP does affordance cross-category transfer but no language conditioning\n- VoxPoser (CoRL 2023, arXiv 2307.05973) uses LLM to generate 3D affordance/constraint maps but is modular, no end-to-end learning\n- No work unifies open-vocabulary affordance reasoning into end-to-end VLA\n\nIn Scope: Methods unifying open-vocabulary affordance reasoning into end-to-end VLA architecture. Specifically includes: text prompt-driven open-vocabulary affordance feature activation mechanism, universal shape-function-interaction attribute association learning, end-to-end joint training of affordance reasoning and action generation, zero-shot generalization to unseen object categories and novel language interaction instructions. The core contribution should be a unified architecture, not a modular concatenation of affordance detection + action generation.\n\nOut of Scope: Predefined fixed affordance types (CoA-VLA already done). Modular affordance pipelines (GeneralVLA/VoxPoser already done). Affordance detection only without actions (OVAL-Prompt already done). Affordance transfer without language conditioning (AffordDP already done). Pure affordance benchmarking/analysis.\n\nContribution Type: Method contribution. Output must include (1) unified architecture design for open-vocabulary affordance and VLA, (2) end-to-end training strategy for affordance reasoning and action generation, (3) experimental validation of zero-shot generalization on unseen objects and novel interaction instructions, demonstrating advantages over structured affordance VLA and modular methods.\n\nEvaluation Protocol:\nTraining: Based on OpenVLA architecture, integrating open-vocabulary affordance module. Training data uses LIBERO + affordance annotation data (e.g., AGD20K/UMD Affordance).\nEvaluation Metrics:\n- Primary metric: Zero-shot manipulation success rate on unseen object categories\n- Novel interaction instruction generalization: Language interaction descriptions unseen during training (e.g., train on "pick up," test on "scoop out")\n- Affordance localization precision: Compare with detection methods like OVAL-Prompt (ensure affordance understanding itself does not degrade)\n- Manipulation success rate: Compare with standard VLA baselines (ensure adding affordance does not degrade known task performance)\n- Baseline comparisons:\n  1. Affordance-free VLA (OpenVLA direct fine-tuning)\n  2. Structured affordance VLA (CoA-VLA reproduction)\n  3. Modular affordance pipeline (GeneralVLA approach)\n  4. Affordance detection + independent policy (OVAL-Prompt + policy learning)\n  5. LLM affordance map + planning (VoxPoser approach)\n- Ablation studies: Open-vocabulary affordance vs. fixed-type affordance, end-to-end vs. staged training, text-driven affordance vs. vision-driven affordance\n- Cross-object transfer tests: Shape-function association generalization (e.g., if trained on shovel\'s "scooping" affordance, can the model activate the same interaction for novel shovel-like tools?)\n- Free-form instruction tests: Non-templated natural language instruction understanding\n\nBuilding Blocks: OpenVLA codebase (VLA base architecture); CoA-VLA codebase (affordance VLA baseline); OVAL-Prompt codebase (open-vocabulary affordance detection reference); AGD20K/UMD Affordance datasets (affordance annotations); LIBERO benchmark (manipulation task evaluation); DINOv2/SigLIP visual encoders; SAM2 (segmentation); HuggingFace transformers + accelerate; CLIP/SigLIP (open-vocabulary semantic alignment).\n\nHard Constraints:\nCompute: ≤200 H100-hours. Strategy: Fine-tune based on 7B VLA, affordance module leveraging pre-trained VLM features (e.g., CLIP/SigLIP) to reduce training requirements. Training ~80 H100-hours, baseline reproduction ~50 H100-hours, ablation ~40 H100-hours, generalization testing ~30 H100-hours.\nEvaluation: Must validate zero-shot generalization on unseen object categories. Must include free-form language instruction tests. Must include ≥4 baselines. Must report both affordance precision and manipulation success rate. Must include ablation studies and cross-object transfer tests.\n\nExploration Directions: (1) End-to-end activation of VLM internal affordance features: Rather than adding an external affordance detection module to VLA, activate interaction-relevant visual features within VLA\'s VLM backbone network directly through language instructions. Key insight: Large-scale VLMs (e.g., PaliGemma, SigLIP) have already learned extensive shape-function associations during pre-training ("knives can cut," "bowls can hold"), only requiring suitable activation mechanisms to release this implicit knowledge. (2) Affordance as intermediate reasoning tokens: Rather than explicitly outputting affordance heatmaps, have VLA generate a set of "affordance reasoning tokens" before generating action token sequences (similar to CoA-VLA\'s chain reasoning but open-vocabulary). These tokens encode interaction possibilities of objects in the current scene, then condition subsequent action generation. Differs from CoA-VLA: not limited to 4 predefined types; reasoning content is dynamically determined by language instructions. (3) Contrastive learning for universal shape-function-interaction mapping: Add contrastive objective during VLA training to pull together different-shaped objects with similar functions (various "tools that can scoop things") in affordance feature space, and push apart similar-shaped objects with different functions (decorative bowl vs. functional bowl). More flexible than CoA-VLA\'s structured types — any natural language-described interaction can participate in contrasting. (4) Knowledge distillation for zero-shot affordance reasoning: Use large VLMs\' (e.g., GPT-4V level) zero-shot affordance reasoning capability ("how can this object be interacted with?") as teacher signals, distilling into small VLA. Large models have rich commonsense knowledge and can generate affordance descriptions for virtually any object, but are too large to deploy directly on robots. (5) Affordance consistency self-supervision: The same object under different language descriptions should have consistent affordance responses ("grab the handle" vs. "pick it up by the stick part" describe the same interaction). Use this consistency as self-supervision signals, reducing dependency on fine-grained affordance annotations.\n\nAvoid:\n- Using predefined fixed affordance types — duplicates CoA-VLA\n- Modular pipeline (affordance detection → planning → control) — duplicates GeneralVLA/VoxPoser, and prevents end-to-end optimization\n- Only doing affordance detection without actions — duplicates OVAL-Prompt\n- Ignoring CoA-VLA baseline — it is the most recent affordance + VLA work; must directly compare\n- Ignoring GeneralVLA — it is the most recent zero-shot affordance manipulation work; must clarify advantages of end-to-end vs. modular\n- Reporting results only on within-training-distribution objects — the core value of open vocabulary is on out-of-distribution objects\n- Over-relying on affordance annotation data — should design methods to reduce annotation requirements\n\nIdea Generation Quality Constraints (Hard rules based on historical cases):\n\n1. No strawman problems: Any claim of "existing methods assume X" or "existing methods fail on Y" must cite specific paragraphs from specific papers as evidence.\n\n2. No pure observation ideas: Output must include a complete method, not merely analysis/benchmark/empirical study.\n\n3. No mediocre methods: Methods must answer:\n   - Core insight: Large-scale VLMs have already implicitly learned rich shape-function association knowledge during pre-training; CoA-VLA released part of it through structured reasoning chains, but is limited by predefined types. We directly activate corresponding affordance features within VLA through open-vocabulary language instructions, fully releasing VLM\'s implicit shape-function knowledge into action generation.\n   - Why non-obvious: (1) CoA-VLA (December 2024) is the first work integrating affordance chain reasoning into VLA; affordance + VLA itself is a new paradigm; (2) open-vocabulary requires solving the infinite-dimensional affordance space problem — unlike 4 fixed types that can be directly classified; (3) end-to-end training of open-vocabulary affordance requires affordance annotation data, but such data is scarce — needs training strategies that reduce annotation dependency.\n   - What information is exploited: Implicit shape-function association knowledge from VLM pre-training — which neither 2D visual VLAs nor fixed-type affordance methods fully utilize.\n   - Mechanistic argument: When given a free-form language instruction (e.g., "scoop the rice"), the VLM internally already encodes knowledge that "scooping requires a concave container-shaped tool." Through suitable activation mechanisms, this knowledge can be transformed into affordance attention in visual feature space — focusing on regions in the scene with corresponding geometric functional properties, then conditioning action generation. More flexible than CoA-VLA\'s fixed 4-type reasoning because affordance is dynamically defined by language.\n\n4. No duplicating existing work: Each core technical component must be confirmed with at least 3 different search queries to have no directly related work.\n\n5. No padding experiments:\n   - "Delete experiment test": Keep only the method description — does it teach the reader something non-trivial? Yes — VLM implicit shape-function knowledge can drive VLA action generation through open-vocabulary activation.\n   - "Baseline fear test": If CoA-VLA\'s 4 structured types already cover most scenarios, is the paper still valuable? Must prove open-vocabulary methods\' advantages on free-form instructions and novel interactions.\n   - "Citation test": Will people cite the numbers or the insight 5 years later? The insight — open-vocabulary affordance in end-to-end VLA paradigm.\n\n6. The following method patterns are rejected (unless with extremely strong structural reasons):\n   - "Add module X" — Why this specific structure?\n   - "Train on data Y" — Is data construction itself a contribution?\n   - "Transfer Z from domain A to domain B" — What is the structural analogy?\n   - "Combine P and Q" — Where is the synergy? Combining open-vocabulary detection (OVAL-Prompt) with VLA — must prove end-to-end joint training outperforms simple concatenation.\n   - "Use more/larger/stronger X" — Scale is not a method contribution.\n\nCompetition Warning: CoA-VLA (December 2024) is the most recent affordance + VLA — uses structured reasoning chains but not open-vocabulary. GeneralVLA (February 2026) does zero-shot affordance manipulation but is a modular pipeline. OVAL-Prompt (ICRA 2024 Workshop) does open-vocabulary affordance detection but no actions. AffordDP (CVPR 2025) does affordance cross-category transfer but no language. VoxPoser (CoRL 2023) uses LLM to generate 3D affordance maps but is modular. π0 (Physical Intelligence) and RT-2 and other large VLAs may implicitly contain partial affordance knowledge but do not explicitly leverage it. Differentiation core: The only work integrating open-vocabulary affordance reasoning end-to-end into a unified VLA architecture. Highest risk: CoA-VLA is closest in space; if its author team quickly extends to open-vocabulary, differentiation shrinks. Monitor: CoA-VLA author team, GeneralVLA author team, Physical Intelligence (whether π0 follow-ups will integrate affordance).\n\nTags: direction=open_vocab_affordance_zero_shot_vla, contribution_type=method, sub_direction=unified_affordance_vla_end_to_end, target_venues=["CoRL 2026"].'
18	2. **Problem Discovery** (492s) — 发现 4 个研究方向
19	   - Open-Vocabulary Affordance Chain-of-Reasoning for End-to-End VLA
20	   - Activating Implicit VLM Affordance Knowledge for Manipulation
21	   - Affordance-Conditioned Flow Matching for Open-Vocabulary VLA
22	   - Functional Correspondence Learning for Zero-Shot Affordance Transfer
23	3. **Method Synthesis** (626s) — 完成: "Open-Vocabulary Affordance Chain-of-Reasoning for End-to-End VLA" [top-tier] → ICLR 2027 (abstract Sep 19, paper Sep 24, 2026) — top-tier ML venue, best fit for method contribution, AAAI 2027 (abstract Jul 21, paper Jul 28, 2026) — top-tier AI venue, earlier deadline, CoRL 2026 (abstract May 26, paper May 29, 2026) — top-tier robotics venue, tight but feasible with auto-research, CVPR 2027 (abstract Nov 7, paper Nov 13, 2026) — top-tier vision venue, fallback if earlier submissions need revision
24	3. **Method Synthesis** (813s) — 完成: "Activating Implicit VLM Affordance Knowledge for Manipulation" [top-tier] → ICLR 2027 (abstract Sep 19, paper Sep 24, 2026 — highest-tier ML venue, ideal for the VLM interpretability + VLA generalization contribution), CoRL 2026 (abstract May 26, paper May 29, 2026 — premier robotics learning venue, tight deadline but perfect topical fit), AAAI 2027 (abstract Jul 21, paper Jul 28, 2026 — broad top-tier AI venue, comfortable timeline)
25	3. **Method Synthesis** (4s) — 完成: "Affordance-Conditioned Flow Matching for Open-Vocabulary VLA"
26	3. **Method Synthesis** (4s) — 完成: "Functional Correspondence Learning for Zero-Shot Affordance Transfer"
27	
28	## Core Problem
29	
30	LLM annotation errors can bias downstream social science conclusions, but researchers currently lack tools to answer two critical questions: (1) which specific annotation error structures actually propagate bias under my study's causal design, and (2) how severe must differential annotation error be to overturn my conclusion? This is not a hypothetical concern: Baumann, Röttger et al. (2025) demonstrate empirically across 37 tasks from 21 studies that approximately 31% of downstream conclusions are incorrect when using SOTA LLM annotations, rising to 50% for smaller models. Existing causal frameworks for text classifier measurement error (Wood-Doughty et al. 2018; TeBlunthuis et al. 2024) address the first question only for binary classification in limited DAG topologies, while sensitivity analysis tools analogous to E-values (VanderWeele & Ding 2017) or measurement error bounds (VanderWeele & Li 2019) do not exist for annotation-induced bias. The correction methods available (DSL, PPI, MLA) each assume specific error structures, but without diagnostic tools to characterize error structure, researchers cannot determine which correction is appropriate — or whether correction is needed at all. Meanwhile, the epidemiological measurement-error literature (Hernán & Cole 2009; VanderWeele & Hernán 2012) provides the causal foundations but has not been applied to the multi-class LLM annotation setting where confusion matrices replace simple misclassification rates.
31	
32	## Opportunity / Why Now
33	
34	Two converging gaps create a focused opportunity. First, the diagnostic gap: Wood-Doughty et al. (2018) produce no formal bias theorems and defer identifiability conditions, and TeBlunthuis et al. (2024) provide correction only for binary outcomes with a single classifier — yet most social science annotation tasks involve multi-class labels (protest type, stance category, topic), and bias propagation in the multi-class case is qualitatively different because directional bias depends on which categories are confused, not just overall error rates. The epidemiological literature confirms this complexity: Brenner (1993) shows that non-differential misclassification of polytomous confounders can bias in either direction, and Veierød & Laake (2001) prove that multi-category exposure misclassification produces bias that depends on all true category-specific coefficients weighted by the full misclassification probability matrix. No systematic treatment exists for how K-class confusion matrix structures map to downstream bias across different causal designs in the text annotation context. Second, the sensitivity gap: no sensitivity analysis framework exists for annotation-induced bias — researchers cannot report 'how differential must annotation error be to overturn my conclusion?' VanderWeele & Li (2019) provide sensitivity bounds for differential measurement error, but only for binary exposure/outcome settings using risk ratios, and explicitly do not address polytomous extensions or confusion-matrix parameterizations. Bridging these two gaps — extending bias expressions to multi-class annotation and providing annotation-specific sensitivity analysis — would give social science researchers actionable diagnostic tools to evaluate the robustness of LLM-annotated studies, complementing existing correction methods rather than replacing them. The urgency is underscored by Baumann et al. (2025), who show that 31% of downstream conclusions from LLM annotations are already incorrect — researchers need diagnostic tools now.
35	
36	## Landscape (SOTA & Limitations)
37	
38	The causal treatment of measurement error in DAGs is well-established in epidemiology: Hernán & Cole (2009) formalize starred-node DAGs with differential/non-differential and independent/dependent error taxonomy; VanderWeele & Hernán (2012) prove bias-direction results using signed DAGs; Li et al. (2020) connect causal structure between true variables to the type of measurement error that arises; VanderWeele & Li (2019) provide sensitivity bounds for differential measurement error of binary exposure/outcome using risk ratios; Schuessler & Selb (SMR 2025) apply DAGs to survey measurement error. For polytomous variables specifically, Brenner (1993) analyzes non-differential misclassification of polytomous confounders showing bias can go in either direction, and Veierød & Laake (2001) derive bias expressions for multi-category exposure misclassification in Poisson regression, showing bias in each category depends on all true coefficients weighted by misclassification probabilities — but neither connects to DAG-based causal reasoning or sensitivity analysis. In NLP, Wood-Doughty, Shpitser & Dredze (EMNLP 2018) apply DAG reasoning to text classifier errors with matrix adjustment correction but produce no formal bias theorems, no identifiability conditions, and note severe instability in corrections. TeBlunthuis, Hase & Chan (CMM 2024) provide the most complete treatment: four DAG scenarios (differential/non-differential × IV/DV), testable conditions via likelihood ratio tests, and a Maximum Likelihood Adjustment (MLA) method — but only for binary classification with a single classifier, and without LLM-specific considerations. On the LLM annotation side, Baumann, Röttger et al. (2025, arXiv:2509.08825) provide the strongest empirical motivation for diagnostic tools: across 37 annotation tasks from 21 published social science studies and 13 million labels from 18 models, they find approximately 31% of hypotheses yield incorrect conclusions with SOTA LLMs, rising to 50% for smaller models, coining the term 'LLM hacking' to describe how configuration choices can make 'virtually anything statistically significant.' Messing (April 2026, arXiv:2604.11581) decomposes LLM pipeline variance via linear mixed models, finding item-judge interaction dominates at 44%, but explicitly excludes causal identification. Gligorić et al. (NAACL 2025) note correlated errors bias estimates and propose DSL/PPI corrections. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic. Halterman & Keith (arXiv 2025) show conceptualization-induced bias cannot be fixed by accuracy improvements alone. Chew et al. (arXiv 2026, 2604.07591) decompose human labeling variance but provide no causal-propagation framework. Cheng, Mayya & Sedoc (arXiv 2024, 2412.14461) decompose LLM annotation error into guideline-, baseline-, prompt-, and model-induced components via their SILICON framework but do not connect to causal propagation. Crucially, recent work on correlated LLM errors reveals that the assumption of independent errors across LLMs is violated in practice: Kim, Garg, Peng & Garg (ICML 2025, arXiv:2506.07962) show models agree 60% of the time when both err, with larger models having highly correlated errors even across architectures; Balasubramanian, Podkopaev & Kasiviswanathan (arXiv 2026, 2601.22336) formalize dependence-aware aggregation via Ising models, proving conditional-independence methods are strictly suboptimal; CARE (Zhao et al., arXiv 2026, 2603.00039) demonstrates confounder-aware aggregation with identifiability guarantees under shared confounders. Mehrotra, Visokay & Gligorić (arXiv 2026, 2603.21404) introduce perspective-driven inference for subjective annotation tasks. No existing work provides: (a) multi-class extension of bias expressions across canonical social-science DAG topologies, or (b) sensitivity analysis values for annotation-induced bias parameterized by confusion matrices.
39	
40	## Proposed Approach
41	
42	We extend the causal measurement-error framework for text annotation in two directions, building explicitly on Wood-Doughty et al. (2018), TeBlunthuis et al. (2024), and the epidemiological sensitivity analysis tradition (VanderWeele & Li 2019), with connections to the polytomous misclassification literature (Brenner 1993; Veierød & Laake 2001). (1) MULTI-CLASS BIAS EXPRESSIONS IN MATRIX FORM: Model the LLM annotation process as a noisy measurement node A* within a structural causal model connecting true multi-class label A to covariates X, treatment T, and outcome Y, parameterizing the error mechanism via the full K×K confusion matrix C where C_{ji} = P(A*=j|A=i,X,T). Derive bias expressions for six canonical social-science DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door), proving formally which confusion matrix structures produce downstream-innocuous vs. downstream-toxic error for each topology. IMPORTANT QUALIFICATION ON TRACTABILITY: For K=2 (binary), our expressions reduce to the scalar formulas of TeBlunthuis et al. (2024), providing a consistency check. For K=3, we provide fully worked scalar closed-form expressions that practitioners can directly compute and interpret — this is the 'sweet spot' covering common annotation tasks like stance detection (pro/neutral/anti) and sentiment (positive/neutral/negative). For K≥5, bias expressions are necessarily in matrix notation involving confusion matrix algebra (products, inversions, spectral decompositions) rather than scalar closed-form, because a K=7 confusion matrix has 42 free parameters that cannot be meaningfully collapsed into a single scalar. For these higher-K settings, we provide three interpretability tools: (a) eigendecomposition summaries that identify which modes of category confusion drive downstream bias (e.g., 'the dominant bias mode is confusion between categories 2 and 5'), (b) worst-case scalar bounds that reduce the matrix expression to a conservative scalar threshold, and (c) diagnostic visualizations mapping confusion matrix regions to bias magnitude. This approach extends Veierød & Laake's (2001) insight that multi-category bias depends on all coefficients weighted by the full misclassification matrix, from their regression-only setting to the full DAG-based causal framework. We provide a complete taxonomy: for each topology, which confusion matrix structural properties (symmetry, diagonal dominance, spectral gap, off-diagonal concentration) preserve vs. distort downstream estimates, with explicit algebraic conditions at K=3 and matrix conditions for general K. (2) ANNOTATION SENSITIVITY VALUES (ASVs): Develop a sensitivity analysis framework, extending VanderWeele & Li's (2019) measurement-error sensitivity bounds from binary risk ratios to multi-class confusion matrices. For a given DAG topology, observed confusion matrix from a validation sample, and downstream effect estimate, an ASV computes the minimum degree of differential annotation error needed to change the sign or significance of the estimate. ASVs are parameterized by a reference confusion matrix (estimated from the validation subsample) and a differential-error amplification factor δ: 'annotation error would need to be δ times more differential than observed in the validation sample to overturn this conclusion.' SCOPED PROOF STRATEGY: We provide full formal proofs of ASV monotonicity and sharpness for three priority topologies (confounding, mediation, collider) — these are the most common in CSS research and have the most tractable algebra. For the remaining three topologies (M-bias, instrument, front-door), we provide the ASV expressions and validate monotonicity and coverage properties via Monte Carlo simulation, stating sharpness as conjectures supported by numerical evidence. This honest scoping reflects the substantial algebraic complexity: each topology requires separate treatment, and the multi-class case introduces matrix inequalities that do not trivially generalize from VanderWeele & Li's scalar bounds. Full proofs for the remaining topologies are identified as immediate future work. ASVs are reported alongside downstream estimates, analogous to E-values for unmeasured confounding — giving reviewers and readers an interpretable robustness metric. (3) CORRECTION GUIDANCE FRAMEWORK: Rather than proposing a new correction method, we provide a principled decision framework for selecting among existing methods (DSL, PPI, MLA, naive plug-in) based on the diagnosed DAG topology, error structure, and ASV. When ASV > threshold (conclusion is robust), naive plug-in may suffice. When error is non-differential and binary, MLA is recommended. When error is differential but a validation sample exists, DSL provides design-based guarantees. We characterize the regimes where each method applies and where no existing method is adequate — identifying open problems for future work, including dependence-aware multi-LLM correction that properly handles correlated errors across annotators (Balasubramanian et al. 2026; CARE, Zhao et al. 2026). VALIDATION: Monte Carlo simulations across six DAG topologies with calibrated error parameters from empirical LLM confusion matrices (varying symmetry, differential error degree, and number of categories K=3,5,7), validating ASV coverage properties and bias expression accuracy. Empirical experiments on three CSS tasks — protest event coding (multi-class, K=5), political stance detection (ordinal, K=3), and toxicity annotation (binary, K=2 as special case) — using Llama 4 Maverick, Qwen 3.5, and DeepSeek V4 via API inference against expert gold-standard labels. We demonstrate that (a) multi-class bias expressions correctly predict the direction and approximate magnitude of bias in empirical settings, (b) ASVs provide calibrated robustness indicators with verified coverage for the three fully-proved topologies, and (c) the correction guidance framework selects the appropriate method for each DAG scenario. Release an open-source Python toolkit ('annot-sensitivity') that takes a user-specified DAG, one or more LLM confusion matrices, and a downstream estimate as input and outputs bias expressions (scalar for K≤3, matrix-form with interpretability summaries for K>3), ASV bounds, sensitivity curves, correction recommendations, and diagnostic visualizations.
43	
44	## Resource Estimate
45	
46	- **auto_research**: {'api_annotation_cost': '$300-$550', 'claude_api_cost': '$200-$400', 'estimated_total_cost': '$545-$1030', 'gpu_hours': '15-30', 'speed_bottleneck': 'Expert review of ASV sharpness proofs for three priority topologies and bias expression derivations; acquiring gold-standard multi-class human-annotated datasets for empirical validation', 'timeline': '4-6 weeks'}
47	- **cost_notes**: API inference costs based on verified May 2026 pricing: Llama 4 Maverick $0.27/$0.85 per Mtok (Together.ai), DeepSeek V4-Flash $0.14/$0.28 per Mtok (DeepSeek API), Qwen 3.5 Plus $0.30/$1.80 per Mtok (OpenRouter). Prices verified against provider pricing pages as of May 2026; note pricing varies across providers (e.g., Fireworks charges $0.22/$0.88 for Maverick). Self-hosting on H100s is unnecessary for annotation-scale workloads. Estimates assume ~30K annotations per model across 3 datasets with 3 prompt variants. Timeline extended by 2 weeks vs. Round 2 to accommodate formal ASV sharpness proofs for confounding, mediation, and collider topologies.
48	- **human_in_loop**: {'api_annotation_cost': '$300-$550', 'claude_api_cost': '$100-$200', 'estimated_total_cost': '$445-$830', 'gpu_hours': '15-30', 'timeline': '8-10 weeks'}
49	- **manual**: {'api_annotation_cost': '$300-$550 (3 LLMs × 3 datasets × multiple prompt variants via Together.ai/Fireworks/DeepSeek API)', 'estimated_total_cost': '$360-$670', 'gpu_hours': '20-40 (simulations only; annotation via API)', 'timeline': '10-12 weeks'}
50	
51	## Key References
52	
53	- Challenges of Using Text Classifiers for Causal Inference (Wood-Doughty, Shpitser & Dredze, EMNLP 2018)
54	- Misclassification in Automated Content Analysis Causes Bias in Regression. Can We Fix It? Yes We Can! (TeBlunthuis, Hase & Chan, Communication Methods & Measures 2024)
55	- Causal Diagrams and Measurement Bias (Hernán & Cole, American Journal of Epidemiology 2009)
56	- Results on Differential and Dependent Measurement Error of the Exposure Using Signed DAGs (VanderWeele & Hernán, American Journal of Epidemiology 2012)
57	- Simple Sensitivity Analysis for Differential Measurement Error (VanderWeele & Li, American Journal of Epidemiology 2019)
58	- Sensitivity Analysis without Assumptions / E-values (VanderWeele & Ding, Epidemiology 2016; Annals of Internal Medicine 2017)
59	- Measurement Bias: A Structural Perspective (Li, Fan, Zhang, Liu, Bao & Zheng, arXiv 2020)
60	- Bias due to non-differential misclassification of polytomous confounders (Brenner, Journal of Clinical Epidemiology 1993)
61	- Exposure misclassification: bias in category specific Poisson regression coefficients (Veierød & Laake, Statistics in Medicine 2001)
62	- Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation (Baumann, Röttger, Urman, Wendsjö, Plaza-del-Arco, Gruber & Hovy, arXiv 2025, 2509.08825)
63	- Hidden Measurement Error in LLM Pipelines (Messing, arXiv 2026, 2604.11581)
64	- Can Unconfident LLM Annotations Be Used for Confident Conclusions? (Gligorić et al., NAACL 2025)
65	- Benchmarking Debiasing Methods for LLM-based Parameter Estimates (Jerzak et al., EMNLP 2025)
66	- Using Imperfect Surrogates for Downstream Inference: Design-Based Supervised Learning (Egami et al., NeurIPS 2023)
67	- Prediction-Powered Inference (Angelopoulos et al., Science 2023)
68	- Correlated Errors in Large Language Models (Kim, Garg, Peng & Garg, ICML 2025, arXiv:2506.07962)
69	- Dependence-Aware Label Aggregation for LLM-as-a-Judge via Ising Models (Balasubramanian, Podkopaev & Kasiviswanathan, arXiv 2026, 2601.22336)
70	- CARE: Confounder-Aware Aggregation for Reliable LLM Evaluation (Zhao, Shin, Huang, Namburi & Sala, arXiv 2026, 2603.00039)
71	- Identifiability of Parameters in Latent Structure Models with Many Observed Variables (Allman, Matias & Rhodes, Annals of Statistics 2009)
72	- What is a protest anyway? Codebook conceptualization is still a first-order concern in LLM-era classification (Halterman & Keith, arXiv 2025)
73	- From Ground Truth to Measurement: A Statistical Framework for Human Labeling (Chew, Eckman, Kern & Kreuter, arXiv 2026, 2604.07591)
74	- To Err Is Human; To Annotate, SILICON? Reducing Measurement Error in LLM Annotation (Cheng, Mayya & Sedoc, arXiv 2024, 2412.14461)
75	- Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks (Mehrotra, Visokay & Gligorić, arXiv 2026, 2603.21404)
76	- Graphical Causal Models for Survey Inference (Schuessler & Selb, SMR 2025)
77	- Using Large Language Models for Qualitative Analysis can Introduce Serious Bias (Ashwin, Chhabra & Rao, SMR 2025)
78	
79	## Reviewer Evaluation
80	
81	**Scores**:
82	  - entry_triage_x: **33.0**/5
83	  - exit_triage_z: **40.0**/5
84	
85	## Human Review Note
86	
87	## External Review — Verdict: PASS
88	
89	- X (entry triage): 33.0%
90	- Y (terminal self-eval): 43.0%
91	- Z (exit triage): 40.0%
92	- Z interval: [34.0%, 46.0%]
93	- Real improvement (Z-X): +7.0 pp
94	
95	### Optimization Suggestions
96	【优化方案】
97	
98	**一、标题与核心定位（命中 Novelty + Significance）**
99	
100	1. **[标题]** — 建议修改为 "Multi-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies"，突出 "not created equal" 的 taxonomy 核心思想，比原始技术性标题更有 punch — **命中 Novelty 第一印象**
101	
102	2. **[Introduction 第 1 段 / Motivation]** — 新增 "ensemble failure → error structure is irreplaceable" 论证链：Kim et al. (ICML 2025, arXiv:2506.07962) 证明 LLM 跨模型错误高度相关（60% agreement when both err），ensemble 无法逃避系统性偏差 → 研究者必须面对并分析所用模型的具体 confusion matrix 结构 → 这正是 taxonomy 的功能。将 Kim et al. 从 limitation 翻转为 proposal 不可替代性的正面论据 — **命中 Significance（从 "error structure matters" 升级为 "error structure is the ONLY thing you can work with"）**
103	
104	3. **[Introduction 第 3-4 段 / Core problem framing]** — 重构核心论点为"对现有 correction literature 的结构性批判"：Jerzak et al. (EMNLP 2025) 将 error 视为 monolithic 进行 benchmarking → 如果不同 confusion matrix structure 在不同 DAG topology 下产生质的不同 bias → unconditional benchmarking 本身就是 misleading → 本 proposal 的 taxonomy 是缺失的 conditioning variable。这比原始的"帮研究者选工具"定位更有力，因为它指向了现有文献的结构性缺陷 — **命中 Significance + Novelty**
105	
106	**二、Key Insight 章节（命中 Novelty）**
107	
108	4. **[Key Insight / Lead Finding]** — 将 "binary safety net breaks in multi-class" 提升为 paper 的核心 surprising result，在 Introduction 中以 lead finding 呈现。精确化 Brenner (1993) 引用：原文说 "in most cases the bias is in the same direction as the confounding"，guarantee 并非完全消失而是不再可靠。将 nuance 转化为 proposal 的价值点——"Brenner identifies the danger but cannot tell you when it strikes; our taxonomy resolves this ambiguity with exact conditions for each confusion matrix structure × DAG topology cell" — **命中 Novelty（防止 overselling 攻击的同时锐化差异化）**
109	
110	5. **[Key Insight / 质变论证]** — 新增 binarization collapse 不可行论证：审稿人最自然的 trivial alternative 是"把 K-class 折叠为 binary 再用成熟工具"。Brenner (1993) 直接回答：binarizing polytomous variable 本身引入方向不可预测的新 bias。补充技术支撑：binary confusion matrix 2 个自由度 → scalar bias；K=5 confusion matrix 20 个自由度 → matrix-valued bias，这是结构性的复杂度跃升而非仅是参数增加 — **命中 Novelty（消除 trivial alternative 质疑）**
111	
112	**三、Related Work 章节（命中 Related Work）**
113	
114	6. **[Related Work / 致命遗漏修复]** — 新增 Lee & Wood-Doughty (arXiv:2411.03004, 2024) 引用并明确 differentiate。原始 proposal 未引用此高度相关工作。该论文将 Wood-Doughty (EMNLP 2018) 扩展至 categorical + LLM classifiers（MIMIC 临床数据），但仅覆盖 1 个 DAG topology（unobserved confounding），无 bias taxonomy，无 sensitivity analysis。将其定位为 stepping stone，修正原 proposal 中 "Wood-Doughty and TeBlunthuis are limited to binary" 的叙事——binary limitation 已被部分突破，但系统性多 topology 处理仍缺失 — **命中 Related Work（消除审稿人发现未引用高相关论文后直接 reject 的风险）**
115	
116	7. **[Related Work / 近期文献补全]** — 新增以下 2024-2026 文献（若原始 proposal 未引用）：Cheng, Mayya & Sedoc (arXiv:2412.14461) SILICON error decomposition; Dependence-Aware Label Aggregation via Ising Models (arXiv:2601.22336, AAAI 2027); CARE (arXiv:2603.00039, AAAI 2027); Multi-Perspective LLM Annotations (arXiv:2603.21404, NAACL 2027); Chew et al. (arXiv:2604.07591) annotation-as-measurement; PPI++ (Angelopoulos et al., 2023) / multiPPI++ (COLM 2024); CrossPPI
117	
118	_Reviewed by external pipeline (batch7), 2026-05-20_
119	
120	
121	## MVP Validation Results
122	
123	- **Date**: 2026-05-20
124	- **Hypothesis Supported**: Yes
125	
126	### Key Metrics
127	
128	理论vs MC一致: 5/5 (全部在95%CI内) | 非差异性C偏差范围: 0.204-0.298 (OVB=0.300) | 二分类折叠差异: Δ=0.001-0.089 | 100k随机C方向反转: 0/100000
129	
130	### Summary
131	
132	Confounding DAG + K=3 三分类标注偏差验证。推导了 OLS 中 β_T 的理论偏差闭式表达式，在 5 种混淆矩阵结构（对称高精度/非对称/结构性混淆/近随机/差异性）× 1000 MC 重复 × N=10,000 下全部验证通过。附加 100k 随机 C 矩阵搜索发现 confounding DAG 下偏差方向始终与 OVB 同向（单调），方向反转需要在 mediator/collider 等其他拓扑验证。二分类折叠对照证实多分类控制保留更多混杂信息（最大 Δ=0.089）。
133	
134	### Recommendation
135	
136	GO — 理论框架验证通过，多分类≠二分类已量化证实。方向反转（核心 claim 最强形式）需 research 阶段在 mediator/collider DAG 上验证，confounding DAG 的单调性本身是有价值的 characterization result。建议立即进入 research 阶段，优先扩展到 6 种 DAG 拓扑。
137	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2e6a151-07c4-4c33-91c2-2dcf20108039",
  "isSidechain": false,
  "promptId": "30f22a65-d3f1-4c77-944b-50b488040b24",
  "type": "user",
  "uuid": "cb75689a-c3dc-477d-9bdc-ee1731c48cbc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/IDEA_BRIEF.md",
      "content": "# Idea Brief: When Do LLM Annotation Errors Matter? Multi-Class Bias Expressions and Annotation Sensitivity Values for Downstream Social Science Inference\n\n\n- **Idea ID**: `idea_027`\n- **Created**: 2026-05-20\n- **Approved**: 2026-05-20\n- **Source**: foreign:be-idea-gen-0515-4\n- **Level**: solid\n- **Target Venues**: ARR October 2026 (deadline: ~2026-10-15; commit to NAACL 2027 or later *ACL venues), AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28), ICWSM 2027 Round 2 (deadline: 2026-09-15)\n\n## Seed Topic\n\nweb_research\n\n## Generation Journey\n\n1. **Start** — 开始生成，seed: '## Seed 4: Open-Vocabulary Affordance Zero-Shot VLA\\n\\nObjective: CoRL 2026 submission.\\n\\nDirection: Traditional affordance methods and VLAs rely on fixed category annotations and struggle with open-world unknown objects and free-form interaction instructions. CoA-VLA (arXiv 2412.20451, December 2024) integrates affordance chain-of-reasoning into VLA, but uses 4 predefined structured affordance types (object, grasp, spatial, motion) — not truly open-vocabulary — and cannot handle free-form interaction descriptions like \"use this thing to wipe off the dust over there.\" GeneralVLA (arXiv 2602.04315, February 2026) achieves zero-shot affordance perception and manipulation trajectory generation through VLM+SAM, but is a modular three-stage pipeline (affordance perception → trajectory planning → low-level control), not a unified end-to-end VLA — with information loss between modules and inability to jointly optimize. OVAL-Prompt (ICRA 2024 VLMNM Workshop, arXiv 2404.11000) achieves truly open-vocabulary affordance localization, but only performs detection/localization without generating actions. AffordDP (CVPR 2025, arXiv 2412.03142) achieves affordance cross-category transfer through 3D contact points and trajectories, but completely lacks language conditioning. Core gap: No work unifies open-vocabulary affordance reasoning into an end-to-end VLA for zero-shot manipulation — existing work either has fixed affordance types (CoA-VLA), or is a modular pipeline (GeneralVLA), or only does detection without actions (OVAL-Prompt), or lacks language (AffordDP).\\n\\nSeed Papers:\\n- \"OpenVLA: An Open-Source Vision-Language-Action Model\" (Kim et al., CoRL 2024, arXiv 2406.09246)\\n  — 7B parameter open-source VLA, trained on 970K real robot demonstrations, establishing the VLA open-source paradigm. The base architecture for this work — integrating open-vocabulary affordance reasoning on top.\\n- \"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance\" (Li et al., arXiv 2412.20451, December 2024)\\n  — Integrates affordance chain-of-reasoning into VLA: model sequentially reasons about object affordance, grasp affordance, spatial affordance, and motion affordance before predicting actions. Uses visual-language collaborative injection module. Surpasses OpenVLA and Octo. Key limitation: 4 affordance types are predefined/structured, not open-vocabulary — cannot handle arbitrary natural language descriptions of novel interactions.\\n- \"GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning\" (Ma et al., arXiv 2602.04315, February 2026)\\n  — Hierarchical three-module pipeline: (1) VLM+SAM affordance perception for keypoint detection, (2) mid-level planning agent for trajectory generation, (3) low-level control policy. Achieves zero-shot manipulation across 14 tasks without real-world data. Key limitation: Modular pipeline, not end-to-end — affordance module, trajectory planner, and controller are separated, with information bottlenecks between modules.\\n- \"OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot Manipulation through LLM Affordance-Grounding\" (Tong et al., ICRA 2024 VLMNM Workshop, arXiv 2404.11000)\\n  — Prompt-based method combining VLM for object part segmentation and LLM for part-affordance grounding mapping, achieving open-vocabulary affordance localization without prior training. Competitive with supervised methods on localization benchmarks. Key limitation: Only performs affordance detection/localization, does not generate robot actions — a perception module, not a complete manipulation system.\\n- \"AffordDP: Generalizable Diffusion Policy with Transferable Affordance\" (Wu et al., CVPR 2025, arXiv 2412.03142)\\n  — Models manipulation priors through 3D contact points and post-contact trajectories, achieving affordance cross-category transfer using visual models + point cloud registration. Affordance-guided diffusion policy generates actions. Key limitation: No language conditioning — affordances are geometric/contact-based, not language-driven, cannot handle open-vocabulary instructions.\\n\\nKnown Gap:\\n- CoA-VLA integrates affordance into VLA but uses predefined structured types, does not support open vocabulary\\n- GeneralVLA does zero-shot affordance manipulation but is a modular pipeline, not end-to-end\\n- OVAL-Prompt does open-vocabulary affordance but only detection, no action generation\\n- AffordDP does affordance cross-category transfer but no language conditioning\\n- VoxPoser (CoRL 2023, arXiv 2307.05973) uses LLM to generate 3D affordance/constraint maps but is modular, no end-to-end learning\\n- No work unifies open-vocabulary affordance reasoning into end-to-end VLA\\n\\nIn Scope: Methods unifying open-vocabulary affordance reasoning into end-to-end VLA architecture. Specifically includes: text prompt-driven open-vocabulary affordance feature activation mechanism, universal shape-function-interaction attribute association learning, end-to-end joint training of affordance reasoning and action generation, zero-shot generalization to unseen object categories and novel language interaction instructions. The core contribution should be a unified architecture, not a modular concatenation of affordance detection + action generation.\\n\\nOut of Scope: Predefined fixed affordance types (CoA-VLA already done). Modular affordance pipelines (GeneralVLA/VoxPoser already done). Affordance detection only without actions (OVAL-Prompt already done). Affordance transfer without language conditioning (AffordDP already done). Pure affordance benchmarking/analysis.\\n\\nContribution Type: Method contribution. Output must include (1) unified architecture design for open-vocabulary affordance and VLA, (2) end-to-end training strategy for affordance reasoning and action generation, (3) experimental validation of zero-shot generalization on unseen objects and novel interaction instructions, demonstrating advantages over structured affordance VLA and modular methods.\\n\\nEvaluation Protocol:\\nTraining: Based on OpenVLA architecture, integrating open-vocabulary affordance module. Training data uses LIBERO + affordance annotation data (e.g., AGD20K/UMD Affordance).\\nEvaluation Metrics:\\n- Primary metric: Zero-shot manipulation success rate on unseen object categories\\n- Novel interaction instruction generalization: Language interaction descriptions unseen during training (e.g., train on \"pick up,\" test on \"scoop out\")\\n- Affordance localization precision: Compare with detection methods like OVAL-Prompt (ensure affordance understanding itself does not degrade)\\n- Manipulation success rate: Compare with standard VLA baselines (ensure adding affordance does not degrade known task performance)\\n- Baseline comparisons:\\n  1. Affordance-free VLA (OpenVLA direct fine-tuning)\\n  2. Structured affordance VLA (CoA-VLA reproduction)\\n  3. Modular affordance pipeline (GeneralVLA approach)\\n  4. Affordance detection + independent policy (OVAL-Prompt + policy learning)\\n  5. LLM affordance map + planning (VoxPoser approach)\\n- Ablation studies: Open-vocabulary affordance vs. fixed-type affordance, end-to-end vs. staged training, text-driven affordance vs. vision-driven affordance\\n- Cross-object transfer tests: Shape-function association generalization (e.g., if trained on shovel\\'s \"scooping\" affordance, can the model activate the same interaction for novel shovel-like tools?)\\n- Free-form instruction tests: Non-templated natural language instruction understanding\\n\\nBuilding Blocks: OpenVLA codebase (VLA base architecture); CoA-VLA codebase (affordance VLA baseline); OVAL-Prompt codebase (open-vocabulary affordance detection reference); AGD20K/UMD Affordance datasets (affordance annotations); LIBERO benchmark (manipulation task evaluation); DINOv2/SigLIP visual encoders; SAM2 (segmentation); HuggingFace transformers + accelerate; CLIP/SigLIP (open-vocabulary semantic alignment).\\n\\nHard Constraints:\\nCompute: ≤200 H100-hours. Strategy: Fine-tune based on 7B VLA, affordance module leveraging pre-trained VLM features (e.g., CLIP/SigLIP) to reduce training requirements. Training ~80 H100-hours, baseline reproduction ~50 H100-hours, ablation ~40 H100-hours, generalization testing ~30 H100-hours.\\nEvaluation: Must validate zero-shot generalization on unseen object categories. Must include free-form language instruction tests. Must include ≥4 baselines. Must report both affordance precision and manipulation success rate. Must include ablation studies and cross-object transfer tests.\\n\\nExploration Directions: (1) End-to-end activation of VLM internal affordance features: Rather than adding an external affordance detection module to VLA, activate interaction-relevant visual features within VLA\\'s VLM backbone network directly through language instructions. Key insight: Large-scale VLMs (e.g., PaliGemma, SigLIP) have already learned extensive shape-function associations during pre-training (\"knives can cut,\" \"bowls can hold\"), only requiring suitable activation mechanisms to release this implicit knowledge. (2) Affordance as intermediate reasoning tokens: Rather than explicitly outputting affordance heatmaps, have VLA generate a set of \"affordance reasoning tokens\" before generating action token sequences (similar to CoA-VLA\\'s chain reasoning but open-vocabulary). These tokens encode interaction possibilities of objects in the current scene, then condition subsequent action generation. Differs from CoA-VLA: not limited to 4 predefined types; reasoning content is dynamically determined by language instructions. (3) Contrastive learning for universal shape-function-interaction mapping: Add contrastive objective during VLA training to pull together different-shaped objects with similar functions (various \"tools that can scoop things\") in affordance feature space, and push apart similar-shaped objects with different functions (decorative bowl vs. functional bowl). More flexible than CoA-VLA\\'s structured types — any natural language-described interaction can participate in contrasting. (4) Knowledge distillation for zero-shot affordance reasoning: Use large VLMs\\' (e.g., GPT-4V level) zero-shot affordance reasoning capability (\"how can this object be interacted with?\") as teacher signals, distilling into small VLA. Large models have rich commonsense knowledge and can generate affordance descriptions for virtually any object, but are too large to deploy directly on robots. (5) Affordance consistency self-supervision: The same object under different language descriptions should have consistent affordance responses (\"grab the handle\" vs. \"pick it up by the stick part\" describe the same interaction). Use this consistency as self-supervision signals, reducing dependency on fine-grained affordance annotations.\\n\\nAvoid:\\n- Using predefined fixed affordance types — duplicates CoA-VLA\\n- Modular pipeline (affordance detection → planning → control) — duplicates GeneralVLA/VoxPoser, and prevents end-to-end optimization\\n- Only doing affordance detection without actions — duplicates OVAL-Prompt\\n- Ignoring CoA-VLA baseline — it is the most recent affordance + VLA work; must directly compare\\n- Ignoring GeneralVLA — it is the most recent zero-shot affordance manipulation work; must clarify advantages of end-to-end vs. modular\\n- Reporting results only on within-training-distribution objects — the core value of open vocabulary is on out-of-distribution objects\\n- Over-relying on affordance annotation data — should design methods to reduce annotation requirements\\n\\nIdea Generation Quality Constraints (Hard rules based on historical cases):\\n\\n1. No strawman problems: Any claim of \"existing methods assume X\" or \"existing methods fail on Y\" must cite specific paragraphs from specific papers as evidence.\\n\\n2. No pure observation ideas: Output must include a complete method, not merely analysis/benchmark/empirical study.\\n\\n3. No mediocre methods: Methods must answer:\\n   - Core insight: Large-scale VLMs have already implicitly learned rich shape-function association knowledge during pre-training; CoA-VLA released part of it through structured reasoning chains, but is limited by predefined types. We directly activate corresponding affordance features within VLA through open-vocabulary language instructions, fully releasing VLM\\'s implicit shape-function knowledge into action generation.\\n   - Why non-obvious: (1) CoA-VLA (December 2024) is the first work integrating affordance chain reasoning into VLA; affordance + VLA itself is a new paradigm; (2) open-vocabulary requires solving the infinite-dimensional affordance space problem — unlike 4 fixed types that can be directly classified; (3) end-to-end training of open-vocabulary affordance requires affordance annotation data, but such data is scarce — needs training strategies that reduce annotation dependency.\\n   - What information is exploited: Implicit shape-function association knowledge from VLM pre-training — which neither 2D visual VLAs nor fixed-type affordance methods fully utilize.\\n   - Mechanistic argument: When given a free-form language instruction (e.g., \"scoop the rice\"), the VLM internally already encodes knowledge that \"scooping requires a concave container-shaped tool.\" Through suitable activation mechanisms, this knowledge can be transformed into affordance attention in visual feature space — focusing on regions in the scene with corresponding geometric functional properties, then conditioning action generation. More flexible than CoA-VLA\\'s fixed 4-type reasoning because affordance is dynamically defined by language.\\n\\n4. No duplicating existing work: Each core technical component must be confirmed with at least 3 different search queries to have no directly related work.\\n\\n5. No padding experiments:\\n   - \"Delete experiment test\": Keep only the method description — does it teach the reader something non-trivial? Yes — VLM implicit shape-function knowledge can drive VLA action generation through open-vocabulary activation.\\n   - \"Baseline fear test\": If CoA-VLA\\'s 4 structured types already cover most scenarios, is the paper still valuable? Must prove open-vocabulary methods\\' advantages on free-form instructions and novel interactions.\\n   - \"Citation test\": Will people cite the numbers or the insight 5 years later? The insight — open-vocabulary affordance in end-to-end VLA paradigm.\\n\\n6. The following method patterns are rejected (unless with extremely strong structural reasons):\\n   - \"Add module X\" — Why this specific structure?\\n   - \"Train on data Y\" — Is data construction itself a contribution?\\n   - \"Transfer Z from domain A to domain B\" — What is the structural analogy?\\n   - \"Combine P and Q\" — Where is the synergy? Combining open-vocabulary detection (OVAL-Prompt) with VLA — must prove end-to-end joint training outperforms simple concatenation.\\n   - \"Use more/larger/stronger X\" — Scale is not a method contribution.\\n\\nCompetition Warning: CoA-VLA (December 2024) is the most recent affordance + VLA — uses structured reasoning chains but not open-vocabulary. GeneralVLA (February 2026) does zero-shot affordance manipulation but is a modular pipeline. OVAL-Prompt (ICRA 2024 Workshop) does open-vocabulary affordance detection but no actions. AffordDP (CVPR 2025) does affordance cross-category transfer but no language. VoxPoser (CoRL 2023) uses LLM to generate 3D affordance maps but is modular. π0 (Physical Intelligence) and RT-2 and other large VLAs may implicitly contain partial affordance knowledge but do not explicitly leverage it. Differentiation core: The only work integrating open-vocabulary affordance reasoning end-to-end into a unified VLA architecture. Highest risk: CoA-VLA is closest in space; if its author team quickly extends to open-vocabulary, differentiation shrinks. Monitor: CoA-VLA author team, GeneralVLA author team, Physical Intelligence (whether π0 follow-ups will integrate affordance).\\n\\nTags: direction=open_vocab_affordance_zero_shot_vla, contribution_type=method, sub_direction=unified_affordance_vla_end_to_end, target_venues=[\"CoRL 2026\"].'\n2. **Problem Discovery** (492s) — 发现 4 个研究方向\n   - Open-Vocabulary Affordance Chain-of-Reasoning for End-to-End VLA\n   - Activating Implicit VLM Affordance Knowledge for Manipulation\n   - Affordance-Conditioned Flow Matching for Open-Vocabulary VLA\n   - Functional Correspondence Learning for Zero-Shot Affordance Transfer\n3. **Method Synthesis** (626s) — 完成: \"Open-Vocabulary Affordance Chain-of-Reasoning for End-to-End VLA\" [top-tier] → ICLR 2027 (abstract Sep 19, paper Sep 24, 2026) — top-tier ML venue, best fit for method contribution, AAAI 2027 (abstract Jul 21, paper Jul 28, 2026) — top-tier AI venue, earlier deadline, CoRL 2026 (abstract May 26, paper May 29, 2026) — top-tier robotics venue, tight but feasible with auto-research, CVPR 2027 (abstract Nov 7, paper Nov 13, 2026) — top-tier vision venue, fallback if earlier submissions need revision\n3. **Method Synthesis** (813s) — 完成: \"Activating Implicit VLM Affordance Knowledge for Manipulation\" [top-tier] → ICLR 2027 (abstract Sep 19, paper Sep 24, 2026 — highest-tier ML venue, ideal for the VLM interpretability + VLA generalization contribution), CoRL 2026 (abstract May 26, paper May 29, 2026 — premier robotics learning venue, tight deadline but perfect topical fit), AAAI 2027 (abstract Jul 21, paper Jul 28, 2026 — broad top-tier AI venue, comfortable timeline)\n3. **Method Synthesis** (4s) — 完成: \"Affordance-Conditioned Flow Matching for Open-Vocabulary VLA\"\n3. **Method Synthesis** (4s) — 完成: \"Functional Correspondence Learning for Zero-Shot Affordance Transfer\"\n\n## Core Problem\n\nLLM annotation errors can bias downstream social science conclusions, but researchers currently lack tools to answer two critical questions: (1) which specific annotation error structures actually propagate bias under my study's causal design, and (2) how severe must differential annotation error be to overturn my conclusion? This is not a hypothetical concern: Baumann, Röttger et al. (2025) demonstrate empirically across 37 tasks from 21 studies that approximately 31% of downstream conclusions are incorrect when using SOTA LLM annotations, rising to 50% for smaller models. Existing causal frameworks for text classifier measurement error (Wood-Doughty et al. 2018; TeBlunthuis et al. 2024) address the first question only for binary classification in limited DAG topologies, while sensitivity analysis tools analogous to E-values (VanderWeele & Ding 2017) or measurement error bounds (VanderWeele & Li 2019) do not exist for annotation-induced bias. The correction methods available (DSL, PPI, MLA) each assume specific error structures, but without diagnostic tools to characterize error structure, researchers cannot determine which correction is appropriate — or whether correction is needed at all. Meanwhile, the epidemiological measurement-error literature (Hernán & Cole 2009; VanderWeele & Hernán 2012) provides the causal foundations but has not been applied to the multi-class LLM annotation setting where confusion matrices replace simple misclassification rates.\n\n## Opportunity / Why Now\n\nTwo converging gaps create a focused opportunity. First, the diagnostic gap: Wood-Doughty et al. (2018) produce no formal bias theorems and defer identifiability conditions, and TeBlunthuis et al. (2024) provide correction only for binary outcomes with a single classifier — yet most social science annotation tasks involve multi-class labels (protest type, stance category, topic), and bias propagation in the multi-class case is qualitatively different because directional bias depends on which categories are confused, not just overall error rates. The epidemiological literature confirms this complexity: Brenner (1993) shows that non-differential misclassification of polytomous confounders can bias in either direction, and Veierød & Laake (2001) prove that multi-category exposure misclassification produces bias that depends on all true category-specific coefficients weighted by the full misclassification probability matrix. No systematic treatment exists for how K-class confusion matrix structures map to downstream bias across different causal designs in the text annotation context. Second, the sensitivity gap: no sensitivity analysis framework exists for annotation-induced bias — researchers cannot report 'how differential must annotation error be to overturn my conclusion?' VanderWeele & Li (2019) provide sensitivity bounds for differential measurement error, but only for binary exposure/outcome settings using risk ratios, and explicitly do not address polytomous extensions or confusion-matrix parameterizations. Bridging these two gaps — extending bias expressions to multi-class annotation and providing annotation-specific sensitivity analysis — would give social science researchers actionable diagnostic tools to evaluate the robustness of LLM-annotated studies, complementing existing correction methods rather than replacing them. The urgency is underscored by Baumann et al. (2025), who show that 31% of downstream conclusions from LLM annotations are already incorrect — researchers need diagnostic tools now.\n\n## Landscape (SOTA & Limitations)\n\nThe causal treatment of measurement error in DAGs is well-established in epidemiology: Hernán & Cole (2009) formalize starred-node DAGs with differential/non-differential and independent/dependent error taxonomy; VanderWeele & Hernán (2012) prove bias-direction results using signed DAGs; Li et al. (2020) connect causal structure between true variables to the type of measurement error that arises; VanderWeele & Li (2019) provide sensitivity bounds for differential measurement error of binary exposure/outcome using risk ratios; Schuessler & Selb (SMR 2025) apply DAGs to survey measurement error. For polytomous variables specifically, Brenner (1993) analyzes non-differential misclassification of polytomous confounders showing bias can go in either direction, and Veierød & Laake (2001) derive bias expressions for multi-category exposure misclassification in Poisson regression, showing bias in each category depends on all true coefficients weighted by misclassification probabilities — but neither connects to DAG-based causal reasoning or sensitivity analysis. In NLP, Wood-Doughty, Shpitser & Dredze (EMNLP 2018) apply DAG reasoning to text classifier errors with matrix adjustment correction but produce no formal bias theorems, no identifiability conditions, and note severe instability in corrections. TeBlunthuis, Hase & Chan (CMM 2024) provide the most complete treatment: four DAG scenarios (differential/non-differential × IV/DV), testable conditions via likelihood ratio tests, and a Maximum Likelihood Adjustment (MLA) method — but only for binary classification with a single classifier, and without LLM-specific considerations. On the LLM annotation side, Baumann, Röttger et al. (2025, arXiv:2509.08825) provide the strongest empirical motivation for diagnostic tools: across 37 annotation tasks from 21 published social science studies and 13 million labels from 18 models, they find approximately 31% of hypotheses yield incorrect conclusions with SOTA LLMs, rising to 50% for smaller models, coining the term 'LLM hacking' to describe how configuration choices can make 'virtually anything statistically significant.' Messing (April 2026, arXiv:2604.11581) decomposes LLM pipeline variance via linear mixed models, finding item-judge interaction dominates at 44%, but explicitly excludes causal identification. Gligorić et al. (NAACL 2025) note correlated errors bias estimates and propose DSL/PPI corrections. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic. Halterman & Keith (arXiv 2025) show conceptualization-induced bias cannot be fixed by accuracy improvements alone. Chew et al. (arXiv 2026, 2604.07591) decompose human labeling variance but provide no causal-propagation framework. Cheng, Mayya & Sedoc (arXiv 2024, 2412.14461) decompose LLM annotation error into guideline-, baseline-, prompt-, and model-induced components via their SILICON framework but do not connect to causal propagation. Crucially, recent work on correlated LLM errors reveals that the assumption of independent errors across LLMs is violated in practice: Kim, Garg, Peng & Garg (ICML 2025, arXiv:2506.07962) show models agree 60% of the time when both err, with larger models having highly correlated errors even across architectures; Balasubramanian, Podkopaev & Kasiviswanathan (arXiv 2026, 2601.22336) formalize dependence-aware aggregation via Ising models, proving conditional-independence methods are strictly suboptimal; CARE (Zhao et al., arXiv 2026, 2603.00039) demonstrates confounder-aware aggregation with identifiability guarantees under shared confounders. Mehrotra, Visokay & Gligorić (arXiv 2026, 2603.21404) introduce perspective-driven inference for subjective annotation tasks. No existing work provides: (a) multi-class extension of bias expressions across canonical social-science DAG topologies, or (b) sensitivity analysis values for annotation-induced bias parameterized by confusion matrices.\n\n## Proposed Approach\n\nWe extend the causal measurement-error framework for text annotation in two directions, building explicitly on Wood-Doughty et al. (2018), TeBlunthuis et al. (2024), and the epidemiological sensitivity analysis tradition (VanderWeele & Li 2019), with connections to the polytomous misclassification literature (Brenner 1993; Veierød & Laake 2001). (1) MULTI-CLASS BIAS EXPRESSIONS IN MATRIX FORM: Model the LLM annotation process as a noisy measurement node A* within a structural causal model connecting true multi-class label A to covariates X, treatment T, and outcome Y, parameterizing the error mechanism via the full K×K confusion matrix C where C_{ji} = P(A*=j|A=i,X,T). Derive bias expressions for six canonical social-science DAG topologies (confounding, mediation, collider, M-bias, instrument, front-door), proving formally which confusion matrix structures produce downstream-innocuous vs. downstream-toxic error for each topology. IMPORTANT QUALIFICATION ON TRACTABILITY: For K=2 (binary), our expressions reduce to the scalar formulas of TeBlunthuis et al. (2024), providing a consistency check. For K=3, we provide fully worked scalar closed-form expressions that practitioners can directly compute and interpret — this is the 'sweet spot' covering common annotation tasks like stance detection (pro/neutral/anti) and sentiment (positive/neutral/negative). For K≥5, bias expressions are necessarily in matrix notation involving confusion matrix algebra (products, inversions, spectral decompositions) rather than scalar closed-form, because a K=7 confusion matrix has 42 free parameters that cannot be meaningfully collapsed into a single scalar. For these higher-K settings, we provide three interpretability tools: (a) eigendecomposition summaries that identify which modes of category confusion drive downstream bias (e.g., 'the dominant bias mode is confusion between categories 2 and 5'), (b) worst-case scalar bounds that reduce the matrix expression to a conservative scalar threshold, and (c) diagnostic visualizations mapping confusion matrix regions to bias magnitude. This approach extends Veierød & Laake's (2001) insight that multi-category bias depends on all coefficients weighted by the full misclassification matrix, from their regression-only setting to the full DAG-based causal framework. We provide a complete taxonomy: for each topology, which confusion matrix structural properties (symmetry, diagonal dominance, spectral gap, off-diagonal concentration) preserve vs. distort downstream estimates, with explicit algebraic conditions at K=3 and matrix conditions for general K. (2) ANNOTATION SENSITIVITY VALUES (ASVs): Develop a sensitivity analysis framework, extending VanderWeele & Li's (2019) measurement-error sensitivity bounds from binary risk ratios to multi-class confusion matrices. For a given DAG topology, observed confusion matrix from a validation sample, and downstream effect estimate, an ASV computes the minimum degree of differential annotation error needed to change the sign or significance of the estimate. ASVs are parameterized by a reference confusion matrix (estimated from the validation subsample) and a differential-error amplification factor δ: 'annotation error would need to be δ times more differential than observed in the validation sample to overturn this conclusion.' SCOPED PROOF STRATEGY: We provide full formal proofs of ASV monotonicity and sharpness for three priority topologies (confounding, mediation, collider) — these are the most common in CSS research and have the most tractable algebra. For the remaining three topologies (M-bias, instrument, front-door), we provide the ASV expressions and validate monotonicity and coverage properties via Monte Carlo simulation, stating sharpness as conjectures supported by numerical evidence. This honest scoping reflects the substantial algebraic complexity: each topology requires separate treatment, and the multi-class case introduces matrix inequalities that do not trivially generalize from VanderWeele & Li's scalar bounds. Full proofs for the remaining topologies are identified as immediate future work. ASVs are reported alongside downstream estimates, analogous to E-values for unmeasured confounding — giving reviewers and readers an interpretable robustness metric. (3) CORRECTION GUIDANCE FRAMEWORK: Rather than proposing a new correction method, we provide a principled decision framework for selecting among existing methods (DSL, PPI, MLA, naive plug-in) based on the diagnosed DAG topology, error structure, and ASV. When ASV > threshold (conclusion is robust), naive plug-in may suffice. When error is non-differential and binary, MLA is recommended. When error is differential but a validation sample exists, DSL provides design-based guarantees. We characterize the regimes where each method applies and where no existing method is adequate — identifying open problems for future work, including dependence-aware multi-LLM correction that properly handles correlated errors across annotators (Balasubramanian et al. 2026; CARE, Zhao et al. 2026). VALIDATION: Monte Carlo simulations across six DAG topologies with calibrated error parameters from empirical LLM confusion matrices (varying symmetry, differential error degree, and number of categories K=3,5,7), validating ASV coverage properties and bias expression accuracy. Empirical experiments on three CSS tasks — protest event coding (multi-class, K=5), political stance detection (ordinal, K=3), and toxicity annotation (binary, K=2 as special case) — using Llama 4 Maverick, Qwen 3.5, and DeepSeek V4 via API inference against expert gold-standard labels. We demonstrate that (a) multi-class bias expressions correctly predict the direction and approximate magnitude of bias in empirical settings, (b) ASVs provide calibrated robustness indicators with verified coverage for the three fully-proved topologies, and (c) the correction guidance framework selects the appropriate method for each DAG scenario. Release an open-source Python toolkit ('annot-sensitivity') that takes a user-specified DAG, one or more LLM confusion matrices, and a downstream estimate as input and outputs bias expressions (scalar for K≤3, matrix-form with interpretability summaries for K>3), ASV bounds, sensitivity curves, correction recommendations, and diagnostic visualizations.\n\n## Resource Estimate\n\n- **auto_research**: {'api_annotation_cost': '$300-$550', 'claude_api_cost': '$200-$400', 'estimated_total_cost': '$545-$1030', 'gpu_hours': '15-30', 'speed_bottleneck': 'Expert review of ASV sharpness proofs for three priority topologies and bias expression derivations; acquiring gold-standard multi-class human-annotated datasets for empirical validation', 'timeline': '4-6 weeks'}\n- **cost_notes**: API inference costs based on verified May 2026 pricing: Llama 4 Maverick $0.27/$0.85 per Mtok (Together.ai), DeepSeek V4-Flash $0.14/$0.28 per Mtok (DeepSeek API), Qwen 3.5 Plus $0.30/$1.80 per Mtok (OpenRouter). Prices verified against provider pricing pages as of May 2026; note pricing varies across providers (e.g., Fireworks charges $0.22/$0.88 for Maverick). Self-hosting on H100s is unnecessary for annotation-scale workloads. Estimates assume ~30K annotations per model across 3 datasets with 3 prompt variants. Timeline extended by 2 weeks vs. Round 2 to accommodate formal ASV sharpness proofs for confounding, mediation, and collider topologies.\n- **human_in_loop**: {'api_annotation_cost': '$300-$550', 'claude_api_cost': '$100-$200', 'estimated_total_cost': '$445-$830', 'gpu_hours': '15-30', 'timeline': '8-10 weeks'}\n- **manual**: {'api_annotation_cost': '$300-$550 (3 LLMs × 3 datasets × multiple prompt variants via Together.ai/Fireworks/DeepSeek API)', 'estimated_total_cost': '$360-$670', 'gpu_hours': '20-40 (simulations only; annotation via API)', 'timeline': '10-12 weeks'}\n\n## Key References\n\n- Challenges of Using Text Classifiers for Causal Inference (Wood-Doughty, Shpitser & Dredze, EMNLP 2018)\n- Misclassification in Automated Content Analysis Causes Bias in Regression. Can We Fix It? Yes We Can! (TeBlunthuis, Hase & Chan, Communication Methods & Measures 2024)\n- Causal Diagrams and Measurement Bias (Hernán & Cole, American Journal of Epidemiology 2009)\n- Results on Differential and Dependent Measurement Error of the Exposure Using Signed DAGs (VanderWeele & Hernán, American Journal of Epidemiology 2012)\n- Simple Sensitivity Analysis for Differential Measurement Error (VanderWeele & Li, American Journal of Epidemiology 2019)\n- Sensitivity Analysis without Assumptions / E-values (VanderWeele & Ding, Epidemiology 2016; Annals of Internal Medicine 2017)\n- Measurement Bias: A Structural Perspective (Li, Fan, Zhang, Liu, Bao & Zheng, arXiv 2020)\n- Bias due to non-differential misclassification of polytomous confounders (Brenner, Journal of Clinical Epidemiology 1993)\n- Exposure misclassification: bias in category specific Poisson regression coefficients (Veierød & Laake, Statistics in Medicine 2001)\n- Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation (Baumann, Röttger, Urman, Wendsjö, Plaza-del-Arco, Gruber & Hovy, arXiv 2025, 2509.08825)\n- Hidden Measurement Error in LLM Pipelines (Messing, arXiv 2026, 2604.11581)\n- Can Unconfident LLM Annotations Be Used for Confident Conclusions? (Gligorić et al., NAACL 2025)\n- Benchmarking Debiasing Methods for LLM-based Parameter Estimates (Jerzak et al., EMNLP 2025)\n- Using Imperfect Surrogates for Downstream Inference: Design-Based Supervised Learning (Egami et al., NeurIPS 2023)\n- Prediction-Powered Inference (Angelopoulos et al., Science 2023)\n- Correlated Errors in Large Language Models (Kim, Garg, Peng & Garg, ICML 2025, arXiv:2506.07962)\n- Dependence-Aware Label Aggregation for LLM-as-a-Judge via Ising Models (Balasubramanian, Podkopaev & Kasiviswanathan, arXiv 2026, 2601.22336)\n- CARE: Confounder-Aware Aggregation for Reliable LLM Evaluation (Zhao, Shin, Huang, Namburi & Sala, arXiv 2026, 2603.00039)\n- Identifiability of Parameters in Latent Structure Models with Many Observed Variables (Allman, Matias & Rhodes, Annals of Statistics 2009)\n- What is a protest anyway? Codebook conceptualization is still a first-order concern in LLM-era classification (Halterman & Keith, arXiv 2025)\n- From Ground Truth to Measurement: A Statistical Framework for Human Labeling (Chew, Eckman, Kern & Kreuter, arXiv 2026, 2604.07591)\n- To Err Is Human; To Annotate, SILICON? Reducing Measurement Error in LLM Annotation (Cheng, Mayya & Sedoc, arXiv 2024, 2412.14461)\n- Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks (Mehrotra, Visokay & Gligorić, arXiv 2026, 2603.21404)\n- Graphical Causal Models for Survey Inference (Schuessler & Selb, SMR 2025)\n- Using Large Language Models for Qualitative Analysis can Introduce Serious Bias (Ashwin, Chhabra & Rao, SMR 2025)\n\n## Reviewer Evaluation\n\n**Scores**:\n  - entry_triage_x: **33.0**/5\n  - exit_triage_z: **40.0**/5\n\n## Human Review Note\n\n## External Review — Verdict: PASS\n\n- X (entry triage): 33.0%\n- Y (terminal self-eval): 43.0%\n- Z (exit triage): 40.0%\n- Z interval: [34.0%, 46.0%]\n- Real improvement (Z-X): +7.0 pp\n\n### Optimization Suggestions\n【优化方案】\n\n**一、标题与核心定位（命中 Novelty + Significance）**\n\n1. **[标题]** — 建议修改为 \"Multi-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies\"，突出 \"not created equal\" 的 taxonomy 核心思想，比原始技术性标题更有 punch — **命中 Novelty 第一印象**\n\n2. **[Introduction 第 1 段 / Motivation]** — 新增 \"ensemble failure → error structure is irreplaceable\" 论证链：Kim et al. (ICML 2025, arXiv:2506.07962) 证明 LLM 跨模型错误高度相关（60% agreement when both err），ensemble 无法逃避系统性偏差 → 研究者必须面对并分析所用模型的具体 confusion matrix 结构 → 这正是 taxonomy 的功能。将 Kim et al. 从 limitation 翻转为 proposal 不可替代性的正面论据 — **命中 Significance（从 \"error structure matters\" 升级为 \"error structure is the ONLY thing you can work with\"）**\n\n3. **[Introduction 第 3-4 段 / Core problem framing]** — 重构核心论点为\"对现有 correction literature 的结构性批判\"：Jerzak et al. (EMNLP 2025) 将 error 视为 monolithic 进行 benchmarking → 如果不同 confusion matrix structure 在不同 DAG topology 下产生质的不同 bias → unconditional benchmarking 本身就是 misleading → 本 proposal 的 taxonomy 是缺失的 conditioning variable。这比原始的\"帮研究者选工具\"定位更有力，因为它指向了现有文献的结构性缺陷 — **命中 Significance + Novelty**\n\n**二、Key Insight 章节（命中 Novelty）**\n\n4. **[Key Insight / Lead Finding]** — 将 \"binary safety net breaks in multi-class\" 提升为 paper 的核心 surprising result，在 Introduction 中以 lead finding 呈现。精确化 Brenner (1993) 引用：原文说 \"in most cases the bias is in the same direction as the confounding\"，guarantee 并非完全消失而是不再可靠。将 nuance 转化为 proposal 的价值点——\"Brenner identifies the danger but cannot tell you when it strikes; our taxonomy resolves this ambiguity with exact conditions for each confusion matrix structure × DAG topology cell\" — **命中 Novelty（防止 overselling 攻击的同时锐化差异化）**\n\n5. **[Key Insight / 质变论证]** — 新增 binarization collapse 不可行论证：审稿人最自然的 trivial alternative 是\"把 K-class 折叠为 binary 再用成熟工具\"。Brenner (1993) 直接回答：binarizing polytomous variable 本身引入方向不可预测的新 bias。补充技术支撑：binary confusion matrix 2 个自由度 → scalar bias；K=5 confusion matrix 20 个自由度 → matrix-valued bias，这是结构性的复杂度跃升而非仅是参数增加 — **命中 Novelty（消除 trivial alternative 质疑）**\n\n**三、Related Work 章节（命中 Related Work）**\n\n6. **[Related Work / 致命遗漏修复]** — 新增 Lee & Wood-Doughty (arXiv:2411.03004, 2024) 引用并明确 differentiate。原始 proposal 未引用此高度相关工作。该论文将 Wood-Doughty (EMNLP 2018) 扩展至 categorical + LLM classifiers（MIMIC 临床数据），但仅覆盖 1 个 DAG topology（unobserved confounding），无 bias taxonomy，无 sensitivity analysis。将其定位为 stepping stone，修正原 proposal 中 \"Wood-Doughty and TeBlunthuis are limited to binary\" 的叙事——binary limitation 已被部分突破，但系统性多 topology 处理仍缺失 — **命中 Related Work（消除审稿人发现未引用高相关论文后直接 reject 的风险）**\n\n7. **[Related Work / 近期文献补全]** — 新增以下 2024-2026 文献（若原始 proposal 未引用）：Cheng, Mayya & Sedoc (arXiv:2412.14461) SILICON error decomposition; Dependence-Aware Label Aggregation via Ising Models (arXiv:2601.22336, AAAI 2027); CARE (arXiv:2603.00039, AAAI 2027); Multi-Perspective LLM Annotations (arXiv:2603.21404, NAACL 2027); Chew et al. (arXiv:2604.07591) annotation-as-measurement; PPI++ (Angelopoulos et al., 2023) / multiPPI++ (COLM 2024); CrossPPI\n\n_Reviewed by external pipeline (batch7), 2026-05-20_\n\n\n## MVP Validation Results\n\n- **Date**: 2026-05-20\n- **Hypothesis Supported**: Yes\n\n### Key Metrics\n\n理论vs MC一致: 5/5 (全部在95%CI内) | 非差异性C偏差范围: 0.204-0.298 (OVB=0.300) | 二分类折叠差异: Δ=0.001-0.089 | 100k随机C方向反转: 0/100000\n\n### Summary\n\nConfounding DAG + K=3 三分类标注偏差验证。推导了 OLS 中 β_T 的理论偏差闭式表达式，在 5 种混淆矩阵结构（对称高精度/非对称/结构性混淆/近随机/差异性）× 1000 MC 重复 × N=10,000 下全部验证通过。附加 100k 随机 C 矩阵搜索发现 confounding DAG 下偏差方向始终与 OVB 同向（单调），方向反转需要在 mediator/collider 等其他拓扑验证。二分类折叠对照证实多分类控制保留更多混杂信息（最大 Δ=0.089）。\n\n### Recommendation\n\nGO — 理论框架验证通过，多分类≠二分类已量化证实。方向反转（核心 claim 最强形式）需 research 阶段在 mediator/collider DAG 上验证，confounding DAG 的单调性本身是有价值的 characterization result。建议立即进入 research 阶段，优先扩展到 6 种 DAG 拓扑。\n",
      "numLines": 137,
      "startLine": 1,
      "totalLines": 137
    }
  },
  "sourceToolAssistantUUID": "f2e6a151-07c4-4c33-91c2-2dcf20108039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：方向反转在 mediator 和 collider 拓扑均被确认；ASV 框架理论性质完整证明；实证数据展示 taxonomy 的实用区分力 核心假设：['非差异性多类误分类在 mediator/collider DAG 下产生方向反转（打破二分类保证）', 'ASV 单调性 + 紧致性在 3 个优先拓扑上均…",
  "leafUuid": "cb75689a-c3dc-477d-9bdc-ee1731c48cbc",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-class annotation errors and causal DAG bias",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f"
}
```

---

### Runtime record

_source line 20 · 2026-05-20T07:30:54.084Z_

````json
{
  "parentUuid": "cb75689a-c3dc-477d-9bdc-ee1731c48cbc",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**causal_annot_error_attrib**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"causal_annot_error_attrib\")` 或 `load_project_config(\"causal_annot_error_attrib\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/causal_annot_error_attrib/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "ccd7a5b1-eb2d-48eb-adf4-3f365a203a4f",
  "timestamp": "2026-05-20T07:30:54.084Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Assistant

_source line 21 · 2026-05-20T07:31:38.721Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the project context. Let me synthesize the "best" tier imagined experiments based on the experiment plan and the tier definition.

The "best" tier means:
- Direction reversal confirmed in mediator AND collider topologies
- ASV framework theoretical properties fully proven
- Empirical data shows taxonomy's practical discriminative power

Core assumptions:
1. Non-differential multi-class misclassification under mediator/collider DAGs produces direction reversal (breaking binary guarantees)
2. ASV monotonicity + sharpness formally provable for 3 priority topologies
3. 3 LLMs' empirical confusion matrices are structurally heterogeneous enough to fall into different taxonomy cells


4. The folding bias from K→2 reduction is substantial across most topologies, demonstrating that binarization introduces meaningful distortion

Looking at the expected metric ranges, I'm seeing direction reversals in 2-3 topologies, theory-empirical alignment around 93-100%, tight ASV coverage deviations under 2%, all three priority topologies with formal proofs, binarization deltas between 8-15%, and empirical discriminative power from 80-100%.

The qualitative differences in taxonomy cells span 60-80% of cases, which reinforces the core narrative—the original framing holds up. The title claim about multi-class errors not being equivalent has solid cross-topology evidence of direction reversals.

Now I'm mapping out the experimental plan: validating bias expressions across the six DAG topologies with K=3, extending those expressions to K=5 and K=7 with matrix notation, collecting empirical confusion matrices from three LLMs on three CSS tasks, analyzing the binarization collapse across all topologies, formalizing the ASV framework with proofs for confounding and collider structures, and running Monte Carlo validation on the ASV results.

For the remaining experiments, I'm planning ASV calibration on the empirical CSS data, building a correction guidance framework with decision mappings, analyzing pathological confusion matrices with near-permutation and rank-deficient cases, and developing an open-source Python toolkit for annotation sensitivity.

For plan_001 specifically, I'm expecting all six topologies to be fully derived and validated, with direction reversals appearing in two to three of them—particularly the mediator and collider cases, possibly M-bias as well. The Monte Carlo theory match rate should land between 0.93 and 1.0. say 36/36 = 1.0 for 6 topologies × 6 C structures)
- Confounding: already known to be monotonic toward OVB
- Mediator: direction reversal expected because misclassification of mediator attenuates indirect effect but can amplify direct effect, causing net sign change
- Collider: direction reversal because conditioning on a misclassified collider opens a spurious path whose sign depends on C structure
- M-bias: could go either way
- Instrument: misclassified instrument weakens IV, but direction should be stable
- Front-door: misclassification of front-door mediator can reverse

For best tier, let's say 2-3 topologies show reversal. I'll say mediator and collider confirmed, with M-bias showing partial reversal under extreme C.

MC validation: 36/36 within 95% CI (6 topologies × 6 C structures)

For the K=5,7 extension, I'm deriving matrix-form expressions and using eigendecomposition to identify the dominant bias modes for each topology. The worst-case bounds stay tight within 15% of the Monte Carlo results, and the patterns from K=3 hold up but with amplified effects at larger K values.

On the empirical side, I'm checking confusion matrices across three different LLMs and finding they have structurally different patterns—enough variation that they fall into different cells of my taxonomy. Some LLM-task pairs land in toxic regions while others stay innocuous.

For the ASV proofs, I'm completing formal derivations for three topologies, verifying monotonicity and sharpness, and checking that coverage at the 95% level stays within 0.02 of nominal. The ASV expressions are computationally tractable.

Now I'm validating the ASV framework on empirical data to confirm it discriminates between robust and fragile conclusions, checking coverage on held-out splits, and confirming it adds real interpretive value beyond just looking at raw confusion matrices.

The correction guidance framework selects the least-biased method in at least 93% of Monte Carlo scenarios and identifies regimes where standard corrections would actually increase bias rather than reduce it. I'm validating these recommendations against the empirical confusion matrix data from the three LLMs.

For binarization collapse, I'm seeing maximum differences up to 0.08–0.15 across topologies, with some cases showing direction reversals that weren't present in the original K-way classification.

Near-permutation confusion matrices produce severe bias across all topologies, and I'm finding that spectral gap and diagonal dominance ratio are strong predictors of bias severity with R² > 0.85. Finally, I'm packaging everything as a pip-installable toolkit with worked examples for all six topologies, keeping computation under 1 second for K≤7 and reproducing all paper results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccd7a5b1-eb2d-48eb-adf4-3f365a203a4f",
  "isSidechain": false,
  "requestId": "req_011CbDRshvM2UiTAgRMoEpzL",
  "type": "assistant",
  "uuid": "20519930-a1af-4518-9a5a-ce7b0a0775ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PgdfZF8YquX9kmQtRvLBCi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18923,
      "cache_read_input_tokens": 23172,
      "output_tokens": 14349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18923,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14349,
          "cache_read_input_tokens": 23172,
          "cache_creation_input_tokens": 18923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18923
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

_source line 22 · 2026-05-20T07:35:55.184Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。标题主张 "Multi-class errors are not created equal" 有跨拓扑方向反转的硬证据支撑。
  三条 claim 均可以最强形式陈述：完整 taxonomy（含反转条件）、ASV 有形式保证、correction guidance 有 MC 验证。
  Headline result: "非差异性多类误差在 confounding DAG 偏向零但在 mediator/collider DAG 反转方向——
  同一混淆矩阵在不同因果设计下产生定性相反的偏差，二值化无法规避。"

imagined_experiments:
  - name: "6 DAG topologies K=3 bias derivation + MC validation"
    plan_id: "plan_001"
    description: >
      对 6 种 DAG 拓扑（confounding, mediation, collider, M-bias, instrument, front-door）推导 K=3 闭式偏差表达式，
      每种拓扑 × 6 种混淆矩阵结构（对称高精度、非对称、结构性混淆、近随机、差异性、近置换极端）× 1000 MC 重复 × N=10000 验证。
    expected_results:
      topologies_derived: 6
      topologies_mc_validated: 6
      confusion_structures_tested: 6
      mc_reps_per_cell: 1000
      N_per_rep: 10000
      theory_mc_match_rate: 0.97
      cells_within_95ci: "35/36 或 36/36"
      direction_reversal_topologies: 3
      direction_reversal_topologies_list: "mediator, collider, M-bias (partial)"
      confounding_bias_range: [0.20, 0.30]
      confounding_direction: "单调正向（OVB 同向），与 MVP 一致"
      mediator_bias_range: [-0.18, 0.12]
      mediator_reversal_c_structures: 3
      collider_bias_range: [-0.25, 0.15]
      collider_reversal_c_structures: 4
      mbias_partial_reversal: true
      instrument_bias_direction: "向零衰减（无反转）"
      frontdoor_bias_direction: "向零衰减为主，1 种 C 下弱反转"
      random_c_search_size: 100000
      random_c_reversal_rate_mediator: 0.34
      random_c_reversal_rate_collider: 0.41
    result_rationale: >
      Confounding DAG 已在 MVP 验证单调性——误分类的混杂变量使 OVB 不完全消除，偏差始终与遗漏方向同向。
      Mediator DAG 出现反转的机理：误分类的中介变量同时衰减间接效应并引入新的残差相关。当 C 矩阵的
      off-diagonal 集中在特定类别对时（如类别 1↔2 互混但类别 3 精确），被衰减的间接路径与被引入的
      残差路径符号相反，净效应翻转。具体而言，K=3 mediator 的偏差表达式包含 C 的逆矩阵与类别特定
      效应的乘积——当 C^{-1} 的负对角元素乘以正类别效应时，总偏差可变负。
      Collider DAG 反转更强：条件于被误分类的 collider 打开了本应封闭的 T→A←Y 路径，
      引入的伪相关方向取决于 C 的 off-diagonal 结构与真实类别分布的交互——非对称 C 在不均匀
      类别分布下容易产生负向伪相关，压过正向选择偏差。随机 C 搜索中约 34-41% 的 C 矩阵在
      mediator/collider 下产生反转，证明反转不是边界现象而是常态。
      M-bias 拓扑在极端 C 下出现弱反转（约 5% 的随机 C），因其结构天然对误分类更鲁棒。
      Instrument 和 front-door 拓扑偏差以向零衰减为主——instrument 误分类削弱工具变量强度但不改变 Wald 估计量方向；
      front-door 误分类主要衰减前门中介路径。
    tables:
      - name: "Table 1: Bias direction and magnitude across 6 topologies × 6 C structures"
        rows: "6 topologies"
        columns: "6 C structures + OVB/true effect baseline"
        key_pattern: >
          Confounding 行全正（0.20-0.30）；Mediator 行有 3 个负值（-0.18 至 -0.05）；
          Collider 行有 4 个负值（-0.25 至 -0.03）；其余拓扑以正/接近零为主
      - name: "Table 2: MC validation — theory vs simulation (36 cells)"
        rows: "36 cells (6×6)"
        columns: "theoretical bias, MC mean, MC 95% CI, within CI (Y/N)"
        key_pattern: "35-36/36 标记 Y，0-1 标记 N（边界情况）"
    figures_description:
      - "Fig 1: 6-panel heatmap，每 panel 一个拓扑，x 轴=C 结构，y 轴=偏差值，颜色编码方向（红=正，蓝=负），直观展示 mediator/collider 的蓝色区块"
      - "Fig 2: 100k 随机 C 偏差分布直方图，6 拓扑对比。Confounding 分布完全在正半轴，mediator/collider 跨零分布，instrument/frontdoor 集中在零附近"
    analysis: >
      核心发现：同一非差异性 C 矩阵在 confounding DAG 产生 +0.25 正偏差，在 mediator DAG 产生 -0.12 负偏差，
      在 collider DAG 产生 -0.20 负偏差——定性相反。这直接支撑标题主张和 Claim 1 最强形式。
      36 个 cell 中 35-36 个在 MC 95% CI 内（match rate ≥ 0.97），理论框架可靠。
      反转出现在 2-3 个拓扑（mediator, collider 确认，M-bias 部分），满足 best 档 direction_reversal_topologies ∈ [2,3]。

  - name: "K=5,7 matrix-form bias expressions + interpretability"
    plan_id: "plan_002"
    description: >
      将偏差表达式推广到 K=5,7，以矩阵代数形式给出。开发三种可解释性工具：
      (a) 特征分解识别主导偏差模式，(b) worst-case 标量界，(c) 诊断可视化。
      在 confounding + mediator + collider 三个核心拓扑上验证。
    expected_results:
      K_values_tested: [5, 7]
      topologies_validated: 3
      eigendecomposition_dominant_modes: "1-2 个主模式解释 ≥ 80% 偏差方差"
      worst_case_bound_tightness: "MC 实际偏差 / worst-case bound ∈ [0.55, 0.85]"
      K5_direction_reversal_preserved: true
      K7_direction_reversal_preserved: true
      K5_bias_amplification_vs_K3: 1.3
      K7_bias_amplification_vs_K3: 1.6
      mc_match_rate_K5: 0.95
      mc_match_rate_K7: 0.93
    result_rationale: >
      K=5 的 C 矩阵有 20 个自由度（vs K=3 的 6 个），偏差从标量变为矩阵值——但矩阵的特征结构
      通常由 1-2 个主模式主导，因为真实标注误差不是均匀分布在所有类别对之间，而是集中在语义相近的
      类别对（如 protest coding 中 "demonstration" 与 "riot" 互混远多于与 "petition" 互混）。
      特征分解捕获这种结构：第一主成分通常是"相邻类别互混"模式，第二主成分是"极端类别混入中间"模式，
      二者合计解释 ≥80% 的偏差方差。Worst-case bound 在 55-85% 之间的紧致度是合理的——bound
      取所有特征值的最坏情况，而实际 C 矩阵不会同时在所有模式上达到极端。
      K 增大时反转现象保留且放大（K=5 偏差 ×1.3, K=7 ×1.6），因为更多类别提供了更多
      off-diagonal 路径可以累积成反向偏差。MC match rate 略降（K=7 约 0.93）是因为高维
      矩阵代数近似在极端 C 结构下精度略减。
    tables:
      - name: "Table 3: Eigendecomposition summary for K=5 across 3 topologies"
        rows: "3 topologies × 6 C structures"
        columns: "λ1 贡献率, λ2 贡献率, cumulative, dominant mode 描述"
        key_pattern: "cumulative ≥ 0.80 在 16/18 个 cell"
      - name: "Table 4: Worst-case scalar bound vs MC actual (K=5,7)"
        rows: "3 topologies × 2 K values"
        columns: "worst-case bound, MC max |bias|, tightness ratio"
        key_pattern: "tightness ratio 0.55-0.85，说明 bound 保守但不过度保守"
    figures_description:
      - "Fig 3: 特征值谱图（K=3,5,7 对比），展示随 K 增长偏差的维度结构——K=3 退化为标量，K=5,7 呈现明显的主成分主导结构"
      - "Fig 4: Heatmap 可视化 K=5 confusion matrix 区域到偏差量级的映射，标注'毒性区域'和'良性区域'"
    analysis: >
      K=5,7 的结果验证了两个关键论点：(1) K 增大不是简单的参数增加而是结构性复杂度跃升——
      需要矩阵工具而非标量公式；(2) 尽管如此，特征分解使高维偏差可解释——practitioner 不需要
      理解 42 个参数，只需关注 1-2 个主导模式。Worst-case bound 提供了当 practitioner
      无法做特征分解时的保守替代。三种工具互补：快速诊断用 bound，深度分析用特征分解，沟通用可视化。

  - name: "3 LLMs × 3 CSS tasks empirical confusion matrices"
    plan_id: "plan_003"
    description: >
      Protest event coding (K=5, ACLED/GPT-RE), stance detection (K=3, SemEval/VAST),
      toxicity (K=2, Civil Comments)。3 个 LLM (Llama 4 Maverick, Qwen 3.5 Plus, DeepSeek V4)
      各约 30K 标注 × 3 prompt variant。输出经验混淆矩阵 + 模型间相关分析。
    expected_results:
      total_annotations: "~270K (3 models × 3 datasets × ~30K)"
      prompt_variants: 3
      llama4_maverick_accuracy_stance: 0.78
      llama4_maverick_accuracy_protest: 0.62
      llama4_maverick_accuracy_toxicity: 0.91
      qwen35_plus_accuracy_stance: 0.73
      qwen35_plus_accuracy_protest: 0.58
      qwen35_plus_accuracy_toxicity: 0.88
      deepseek_v4_accuracy_stance: 0.76
      deepseek_v4_accuracy_protest: 0.55
      deepseek_v4_accuracy_toxicity: 0.90
      inter_model_error_correlation: 0.52
      confusion_matrix_structural_heterogeneity: >
        3 个 LLM 的 C 矩阵在 protest K=5 任务上结构差异最大——
        Maverick 集中混淆 demonstration↔riot，Qwen 集中混淆 strike↔boycott，
        DeepSeek 整体准确度最低但 off-diagonal 更均匀
      taxonomy_cells_occupied: "3 个 LLM × 3 任务 = 9 个 C 矩阵落入 taxonomy 的不同区域"
      qualitative_difference_rate: 0.78
    result_rationale: >
      LLM 标注准确度的预期范围基于 Baumann et al. (2025) 的大规模实证：SOTA 模型在复杂多分类任务
      （如 protest coding K=5）上准确度 55-65%，简单二分类（toxicity）上 88-92%，中等复杂度
      （stance K=3）上 73-80%。三个 LLM 架构差异（Llama 4 MoE vs Qwen dense vs DeepSeek MoE）
      导致系统性不同的误差模式：Maverick 作为 MoE 模型在 protest coding 中对 fine-grained
      区分（demonstration vs riot）有独特弱点（路由机制倾向于合并语义相近类别）；
      Qwen 作为 dense 模型在 ordinal 类别上混淆不同（strike↔boycott 语义距离感知不同）；
      DeepSeek 整体准确度略低但误差更均匀分布。
      模型间误差相关约 0.52（Kim et al. 2025 报告 0.60），略低是因为我们选择了架构差异较大的模型组合。
      关键是结构异质性：9 个经验 C 矩阵中约 78% 在 taxonomy 中产生定性不同的偏差预测
      （如同一 C 在 mediator DAG 预测反转但在 confounding DAG 预测衰减），
      直接证明 taxonomy 的实用区分力。
    tables:
      - name: "Table 5: Accuracy and macro-F1 for 3 LLMs × 3 tasks × 3 prompt variants"
        rows: "9 model-task combinations"
        columns: "accuracy (mean±sd across prompts), macro-F1, per-class F1"
        key_pattern: "protest 任务方差最大（prompt 敏感），toxicity 最稳定"
      - name: "Table 6: Inter-model error correlation matrix (per task)"
        rows: "3 tasks"
        columns: "Mav-Qwen ρ, Mav-DS ρ, Qwen-DS ρ, mean ρ"
        key_pattern: "protest ρ ∈ [0.42, 0.58]，stance ρ ∈ [0.48, 0.62]，toxicity ρ ∈ [0.55, 0.68]"
    figures_description:
      - "Fig 5: 3×3 网格混淆矩阵热力图（行=LLM，列=task），直观展示三个 LLM 在 protest K=5 上的结构差异"
      - "Fig 6: PCA 降维将 9 个 C 矩阵映射到 2D 空间，着色按 taxonomy 预测的偏差类型（innocuous/toxic/reversal），展示 LLM 的结构差异足以落入不同 taxonomy cell"
    analysis: >
      经验数据的核心价值：证明 taxonomy 不是理论玩具而是实际有区分力的诊断工具。
      9 个 C 矩阵中 78% 产生定性不同的偏差预测（满足 best 档 taxonomy_cells_with_qualitative_difference ∈ [0.6, 0.8]），
      意味着研究者选择不同 LLM + 不同因果设计会面临质的不同的偏差问题——不能一刀切。
      模型间误差相关的实证数据直接支撑 Kim et al. 的发现并强化我们的动机：ensemble 不能解决问题，
      必须分析具体 error structure。

  - name: "Binarization collapse analysis across 6 topologies"
    plan_id: "plan_008"
    description: >
      对 6 种拓扑 × K=3,5,7，将多分类变量折叠为二分类，比较完整多分类偏差表达式 vs 二值化偏差表达式。
      量化 Δ = |bias_multiclass - bias_binary|，证明二值化不是安全捷径。
    expected_results:
      topologies_tested: 6
      K_values: [3, 5, 7]
      total_comparisons: 108
      delta_max_K3: 0.089
      delta_max_K5: 0.12
      delta_max_K7: 0.15
      delta_mean_across_all: 0.062
      binarization_introduces_reversal_cases: 4
      delta_gt_005_fraction: 0.72
      confounding_delta_range: [0.01, 0.089]
      mediator_delta_range: [0.03, 0.13]
      collider_delta_range: [0.04, 0.15]
    result_rationale: >
      二值化将 K-class 变量折叠为 2-class，不可避免地丢弃类别间的异质效应信息。
      MVP 已在 confounding DAG K=3 下观察到 Δ_max=0.089。随 K 增大，被折叠掉的信息量增加：
      K=3→2 丢失 1 个类别的独立效应，K=5→2 丢失 3 个，K=7→2 丢失 5 个——折叠偏差近似
      线性增长于被折叠的类别数。Δ_max 在 collider 拓扑最大（0.15）是因为 collider conditioning
      对类别粒度最敏感：粗粒度的二值 collider 打开的伪相关路径与细粒度多分类 collider 的不同。
      更关键的是 4 个案例中二值化引入了多分类下不存在的方向反转——原本在多分类下偏差为正的
      估计量，二值化后变为负偏差。这发生在折叠方案将效应方向相反的类别合并到同一组时
      （如 protest coding 中将 pro-government rally 和 anti-government demonstration 合为 "collective action"）。
      72% 的比较中 Δ > 0.05，远超统计噪声——二值化系统性地不安全。
    tables:
      - name: "Table 7: Binarization gap Δ across 6 topologies × K=3,5,7"
        rows: "6 topologies"
        columns: "K=3 Δ_max, K=5 Δ_max, K=7 Δ_max, 是否引入新反转"
        key_pattern: "collider 行的 Δ 值最大，confounding 行最小；mediator 和 collider 行标记'新反转'"
      - name: "Table 8: Δ > 0.05 的比例统计"
        rows: "按拓扑分组"
        columns: "K=3 %, K=5 %, K=7 %, 总计 %"
        key_pattern: "总计 72%，K=7 行接近 85%"
    figures_description:
      - "Fig 7: 配对散点图 (bias_multiclass vs bias_binary)，6 拓扑用不同颜色/marker，对角线=完美一致，偏离对角线=折叠偏差。Mediator/collider 点散布最广"
      - "Fig 8: Δ 随 K 增长的趋势图（6 拓扑各一条线），展示折叠偏差近似线性增长"
    analysis: >
      二值化分析直接回应审稿人最自然的 trivial alternative 质疑（"为什么不直接折叠成 binary 用成熟工具？"）。
      答案：Δ_max 高达 0.15（best 档范围 [0.08, 0.15]），且在 4 个案例中引入原本不存在的方向反转。
      这不是边际改善——是定性错误。72% 的比较 Δ > 0.05 证明这是系统性问题而非边界案例。
      Brenner (1993) 的理论预警在此得到跨拓扑的量化确认。

  - name: "ASV formal proofs: confounding, mediation, collider"
    plan_id: "plan_004"
    description: >
      推导 3 个优先拓扑的 ASV 表达式，形式化证明 (a) 单调性（ASV 随 δ 放大因子递增）和
      (b) 紧致性（bound 可达，存在 C 矩阵恰好达到 bound）。MC 验证覆盖率：90%, 95%, 99% 水平 × 1000 场景。
    expected_results:
      topologies_proved: 3
      monotonicity_proofs: 3
      sharpness_proofs: 3
      asv_coverage_90_deviation: 0.008
      asv_coverage_95_deviation: 0.012
      asv_coverage_99_deviation: 0.015
      mc_scenarios: 1000
      mc_reps_per_scenario: 1000
      coverage_95_actual: 0.938
      coverage_99_actual: 0.985
      asv_median_confounding: 2.8
      asv_median_mediator: 1.4
      asv_median_collider: 1.1
    result_rationale: >
      单调性证明的核心思路：ASV 定义为使下游估计符号翻转所需的最小差异性误差放大因子 δ。
      对 confounding DAG，偏差表达式是 C 矩阵元素的连续单调函数（MVP 已验证），
      因此 δ 增大时偏差单调增大，ASV 阈值随之单调递增——证明结构清晰。
      Mediator 和 collider 的单调性更精妙：因为偏差可能反转，需要证明的是 |bias| 关于 δ 单调——
      即差异性误差越大，偏差绝对值越大（不论方向）。这在 K=3 闭式表达式下可以通过对 δ 求导
      并验证导数符号来完成。
      紧致性证明构造性地给出达到 bound 的 C 矩阵——对每个拓扑，存在一个"最坏情况"C 使得
      恰好在 ASV 阈值处翻转。证明难度中等：confounding 最简单（标量优化），mediator 和 collider
      需要矩阵约束优化但 K=3 时退化为 6 维约束问题，可解析求解。
      Coverage 偏差在 95% 水平约 0.012（实际覆盖 93.8% vs 名义 95%），轻微欠覆盖因为
      ASV bound 依赖验证子样本估计的 C 而非真实 C——有限样本噪声导致 bound 略窄。
      ASV 中位数的拓扑差异有实质意义：confounding 的 ASV=2.8 意味着差异性误差需要比观测值
      大 2.8 倍才能翻转结论（相对鲁棒），而 collider 的 ASV=1.1 意味着只需 10% 额外的
      差异性误差就能翻转（非常脆弱）——这种差异直接体现 taxonomy 的诊断价值。
    tables:
      - name: "Table 9: ASV coverage calibration (3 topologies × 3 levels)"
        rows: "3 topologies"
        columns: "nominal 90% / actual, nominal 95% / actual, nominal 99% / actual"
        key_pattern: "所有偏差 ≤ 0.02，satisfying best 档 asv_coverage_deviation_95 ∈ [0.0, 0.02]"
      - name: "Table 10: ASV distribution summaries across 1000 MC scenarios"
        rows: "3 topologies"
        columns: "ASV median, Q25, Q75, min, max"
        key_pattern: "confounding ASV 最高（最鲁棒），collider 最低（最脆弱）"
    figures_description:
      - "Fig 9: ASV 灵敏度曲线（x=δ 放大因子，y=bias 绝对值），3 拓扑各一条曲线 + 95% CI band。直观展示 mediator/collider 在低 δ 即翻转"
      - "Fig 10: Coverage QQ-plot（实际覆盖率 vs 名义覆盖率），3 拓扑三条线应紧贴对角线"
    analysis: >
      ASV 形式保证的完成（3/3 单调性 + 3/3 紧致性）是 best 档的硬性要求（asv_sharpness_formal_proofs=3）。
      覆盖偏差 ≤ 0.02 证明 ASV 是校准良好的诊断工具——不是松散的上界，而是可信赖的灵敏度指标。
      拓扑间 ASV 的 2.5 倍差异（confounding 2.8 vs collider 1.1）是论文的关键 insight 之一：
      同一 LLM 的同一标注质量，在不同因果设计下的鲁棒性可以从"非常安全"到"极度脆弱"——
      这是 "not created equal" 的灵敏度版本表述。

  - name: "ASV MC validation for M-bias, instrument, front-door"
    plan_id: "plan_005"
    description: >
      推导剩余 3 种拓扑的 ASV 表达式，MC 验证单调性和覆盖率。紧致性以数值证据支持的猜想形式陈述。
    expected_results:
      topologies_validated: 3
      monotonicity_mc_confirmed: 3
      monotonicity_violation_rate: 0.0
      coverage_95_mbias: 0.942
      coverage_95_instrument: 0.948
      coverage_95_frontdoor: 0.939
      sharpness_numerical_evidence: "1000 场景中最坏情况 C 达到 bound 的 ≥ 97%"
      asv_median_mbias: 2.1
      asv_median_instrument: 3.5
      asv_median_frontdoor: 1.8
    result_rationale: >
      M-bias、instrument、front-door 的代数复杂度使完整形式证明不可行（M-bias 有 5 个节点的
      DAG，偏差表达式涉及 3 个 C 矩阵的嵌套乘积；instrument 的 Wald 估计量比值结构使
      单调性证明需要分子分母同时分析）。但 MC 验证可以高置信度确认性质：1000 场景 × 1000 重复
      无一违反单调性（violation rate = 0.0），覆盖率偏差 ≤ 0.02。
      Instrument 的 ASV 最高（3.5）是因为误分类的工具变量削弱 IV 强度但不改变
      估计方向——需要非常大的差异性误差才能翻转。Front-door 相对脆弱（1.8）因为
      前门准则需要两步条件期望，每步的误分类偏差会复合。
      紧致性猜想由数值证据支持：在 1000 个随机场景中，最坏情况 C 达到理论 bound 的 ≥ 97%，
      剩余 3% 的微小差距 (<0.005) 可能是数值优化未完全收敛。
    tables:
      - name: "Table 11: ASV coverage and monotonicity MC validation (3 additional topologies)"
        rows: "3 topologies"
        columns: "monotonicity violations / total, coverage 90%, coverage 95%, coverage 99%"
        key_pattern: "violations = 0/1000 for all; coverage 偏差 ≤ 0.02"
    figures_description:
      - "Fig 11: 6 拓扑 ASV 中位数柱状图（confounding 到 front-door），条件于同一参考 C。直观展示拓扑对鲁棒性的影响"
    analysis: >
      6 个拓扑的 ASV 完整图景：instrument 最鲁棒（ASV=3.5），collider 最脆弱（ASV=1.1），
      差异超过 3 倍。这给 practitioner 的消息很明确：如果你的研究设计涉及 collider conditioning
      且使用 LLM 标注，ASV 分析是必须的；如果是 IV 设计，标注误差的影响相对温和。
      3 个追加拓扑的形式证明留作 future work 是 honest scoping——论文已对最重要的 3 个拓扑
      给出完整保证，对全部 6 个给出 MC 验证。

  - name: "ASV calibration on empirical data"
    plan_id: "plan_006"
    description: >
      将 ASV 应用于 plan_003 的经验混淆矩阵。在 held-out 金标分割上验证覆盖率。
      对每个 task × LLM 报告 ASV + 下游效应估计。比较 ASV 与原始混淆矩阵报告的可解释性。
    expected_results:
      task_llm_combinations: 9
      asv_reported: 9
      coverage_verified_on_holdout: true
      holdout_coverage_95: 0.93
      asv_discriminates_fraction: 0.89
      asv_range_protest: [0.8, 2.5]
      asv_range_stance: [1.2, 3.0]
      asv_range_toxicity: [2.5, 5.0]
      downstream_conclusion_fragile_cases: 3
      downstream_conclusion_robust_cases: 6
      asv_vs_raw_confusion_interpretability_preference: "14/18 评估者偏好 ASV 报告"
    result_rationale: >
      经验 ASV 的范围反映任务复杂度与标注质量的交互：toxicity（K=2）的 ASV 最高（2.5-5.0）
      因为二分类误差结构简单且 LLM 准确度高（~90%），结论很鲁棒；
      protest（K=5）的 ASV 最低（0.8-2.5）因为多分类准确度低（~55-62%）且 C 结构复杂，
      结论相对脆弱；stance（K=3）居中。
      9 个组合中 3 个被标记为 fragile（ASV < 1.5），意味着适度的差异性误差即可翻转结论——
      这些恰好是 protest coding 任务 × 准确度较低的 LLM 组合，符合直觉。
      ASV 的区分力（89% 的组合中 ASV 提供了 C 矩阵本身不能直接提供的诊断信息）
      满足 best 档 empirical_asv_discriminates ∈ [0.8, 1.0]。
      Held-out 覆盖率 0.93（vs 名义 0.95）与 MC 验证结果一致，确认 ASV 在真实数据上校准良好。
    tables:
      - name: "Table 12: ASV report for 9 task × LLM combinations"
        rows: "9 combinations (3 tasks × 3 LLMs)"
        columns: "下游效应估计, 95% CI, ASV, 鲁棒性判定 (robust/fragile)"
        key_pattern: "3 个 fragile 标记集中在 protest × {Qwen, DeepSeek}"
      - name: "Table 13: Held-out coverage validation"
        rows: "9 combinations"
        columns: "训练集 ASV, 测试集实际覆盖, 偏差"
        key_pattern: "平均偏差 0.012, 最大偏差 0.025"
    figures_description:
      - "Fig 12: ASV 仪表盘示例——对一个 protest + Maverick 组合，展示 ASV 灵敏度曲线 + 当前估计位置 + 阈值标注。作为 toolkit 输出的示例"
      - "Fig 13: 9 个组合的 ASV vs downstream bias scatterplot，fragile 案例标红，robust 标绿"
    analysis: >
      经验验证将理论框架落地为 practitioner 工具。关键发现：即使同一 LLM（如 Maverick），
      在 stance 任务上 ASV=2.8（robust）而在 protest 任务上 ASV=1.2（fragile）——
      同一标注工具的可信度取决于任务复杂度和因果设计的交互，不能一概而论。
      这直接为 paper 的 pitch 提供了 "show, don't tell" 的经验支撑。

  - name: "Correction guidance framework validation"
    plan_id: "plan_007"
    description: >
      构建决策框架：{拓扑 × 误差结构 × ASV} → 纠偏方法推荐（DSL / PPI / MLA / naive plug-in / 无现有方法适用）。
      MC 验证推荐方法在 ≥90% 场景中产生最小偏差。在 plan_003 数据上做经验验证。
    expected_results:
      framework_cells: 72
      mc_validation_correct_recommendation_rate: 0.93
      correction_methods_tested: 4
      regimes_no_method_adequate: 8
      empirical_validation_correct_rate: 0.89
      correction_increases_bias_cases: 5
      correction_increases_bias_detected_by_framework: 5
    result_rationale: >
      决策框架的 72 个 cell（6 拓扑 × 4 误差结构类型 × 3 ASV 范围段）每个映射到一个推荐方法。
      MC 验证中 93% 正确推荐率（vs 要求 ≥90%）的来源：
      - DSL 在有验证子样本 + 差异性误差时最优（design-based 保证），框架正确识别这些场景
      - PPI 在大验证样本 + 非差异性误差时最优，框架正确识别
      - MLA 在二分类非差异性场景中最优（TeBlunthuis et al. 的核心场景），框架正确识别
      - Naive plug-in 在 ASV 很高时足够（结论鲁棒无需纠偏），框架正确识别
      7% 的错误推荐主要发生在边界区域（ASV 接近阈值，两种方法表现相当）。
      8 个"无现有方法适用"的 regime 集中在：(1) 差异性多分类误差 + 无验证样本（DSL 不可用，
      MLA 假设不满足），(2) 相关多 LLM 误差（所有现有方法假设独立误差）——
      这些被明确标记为 open problems。
      5 个"纠偏反而增加偏差"的案例全部被框架正确检测——这些发生在误用 MLA 于差异性误差场景，
      或误用 naive plug-in 于低 ASV 场景。这是论文的强力 selling point：
      没有诊断就做纠偏，可能适得其反。
    tables:
      - name: "Table 14: Decision framework mapping (condensed)"
        rows: "6 topologies"
        columns: "非差异/高ASV, 非差异/低ASV, 差异/有验证, 差异/无验证"
        key_pattern: "对角线区域是 straightforward 推荐，off-diagonal 有'无方法'或'谨慎使用'标记"
      - name: "Table 15: MC validation — recommended vs best-performing method"
        rows: "72 cells"
        columns: "推荐方法, 实际最优方法, bias 差异, 匹配 (Y/N)"
        key_pattern: "67/72 匹配 (93%)"
      - name: "Table 16: Cases where correction increases bias"
        rows: "5 cases"
        columns: "拓扑, 误差结构, 误用方法, 原始 bias, 纠偏后 bias, 增幅"
        key_pattern: "增幅最大案例：collider + 差异性误差 + 误用 MLA，bias 从 0.08 升至 0.22"
    figures_description:
      - "Fig 14: 决策流程图——从 DAG 拓扑 → 误差结构判断 → ASV 检查 → 推荐方法/标记 open problem"
      - "Fig 15: 4 种纠偏方法在 72 个场景中的偏差热力图，按框架推荐高亮最优选择"
    analysis: >
      Correction guidance 框架的核心贡献不是新的纠偏方法，而是"什么时候用什么"的诊断层。
      93% 正确推荐率 + 100% 误用检测率（5/5 适得其反案例被捕获）证明框架有实际价值。
      8 个 open problem regime 的明确标记是 honest scoping——论文不假装解决所有问题，
      而是给出目前能解决什么、不能解决什么的清晰边界。

  - name: "Pathological confusion matrix analysis"
    plan_id: "plan_009"
    description: >
      极端 C 结构（近置换、秩亏、块对角）在 6 种拓扑下的灾难性偏差分析。
      识别预测偏差严重度的结构性条件（谱隙、对角优势比）。
    expected_results:
      extreme_c_types_tested: 3
      topologies_tested: 6
      catastrophic_bias_threshold: 0.5
      catastrophic_cases_fraction: 0.28
      spectral_gap_bias_correlation: 0.88
      diagonal_dominance_bias_correlation: -0.91
      predictive_feature_R2: 0.87
      near_permutation_max_bias: 1.2
      rank_deficient_identifiability_failure_rate: 0.15
    result_rationale: >
      近置换 C 矩阵（对角线接近 0，off-diagonal 接近 1/K-1）代表"系统性误标"——
      LLM 几乎总是标错。在 mediator/collider 拓扑下，这产生的偏差可超过 1.0（远超真实效应量级），
      因为误分类不仅引入噪声还系统性地反转类别含义。
      秩亏 C（某些行线性相关，即两类别完全不可区分）导致 C^{-1} 不存在，偏差表达式
      diverge——这是理论上的 identifiability failure，约 15% 的秩亏情况下无法恢复无偏估计。
      谱隙（C 的最大与次大特征值之比）与偏差量级的相关高达 0.88——谱隙越小，
      C 越接近秩亏，偏差越大。对角优势比（对角线之和 / off-diagonal 之和）与偏差负相关 -0.91——
      对角优势越大，C 越接近单位矩阵，偏差越小。
      这两个特征的 joint R² = 0.87，意味着 practitioner 只需计算两个标量指标即可预估
      偏差严重度——无需完整的偏差表达式推导。
    tables:
      - name: "Table 17: Pathological C bias summary across topologies"
        rows: "3 extreme C types × 6 topologies"
        columns: "bias mean, bias max, |bias|>0.5 标记"
        key_pattern: "近置换 × collider 的 bias max = 1.2（灾难性）"
      - name: "Table 18: Diagnostic feature predictive power"
        rows: "候选特征 (spectral gap, diagonal dominance, condition number, Frobenius distance to I)"
        columns: "Pearson r, R², p-value"
        key_pattern: "spectral gap 和 diagonal dominance 是 top-2 特征，joint R²=0.87"
    figures_description:
      - "Fig 16: Spectral gap vs |bias| 散点图，6 拓扑着色，拟合线 + R² 标注"
    analysis: >
      病态分析为 practitioner 提供了"红线指标"：如果验证子样本显示 C 的谱隙 < 0.3 或
      对角优势比 < 1.5，应当对下游结论持极端怀疑态度。这些简单可计算的标量指标
      让非专家也能做初步诊断——是 toolkit 的核心功能之一。

  - name: "annot-sensitivity Python toolkit"
    plan_id: "plan_010"
    description: >
      开源 pip-installable 工具包。输入：用户指定 DAG + 混淆矩阵 + 下游估计。
      输出：偏差表达式 + ASV + 灵敏度曲线 + 纠偏推荐 + 诊断图。
    expected_results:
      package_name: "annot-sensitivity"
      pip_installable: true
      topologies_supported: 6
      K_range_supported: "2-20"
      computation_time_K3: "<0.1s"
      computation_time_K7: "<0.5s"
      computation_time_K20: "<5s"
      worked_examples: 6
      test_coverage: 0.92
      reproduces_all_paper_results: true
      api_functions: ["bias_expression", "asv_compute", "sensitivity_curve", "correction_recommend", "diagnostic_plot", "taxonomy_classify"]
    result_rationale: >
      工具包的价值在于将整篇论文的理论贡献转化为"一行代码"的 practitioner 体验。
      K=3 计算 <0.1s 因为闭式表达式只需矩阵乘法和求逆；K=7 <0.5s 因为需要特征分解但
      矩阵维度仍然很小；K=20 <5s 因为 MC-based ASV 需要少量模拟。6 个 worked examples
      （每种拓扑一个）确保 practitioner 有即拿即用的模板。
      92% 测试覆盖率覆盖所有拓扑 × K 值组合 + 边界情况（秩亏 C、K=2 退化等）。
      完全复现论文所有结果是开源可信度的基本要求。
    tables: []
    figures_description:
      - "Fig 17: Toolkit 架构图——输入/输出流，展示 6 个核心 API 函数的关系"
      - "Fig 18: Toolkit 输出示例截图——一个完整的诊断报告页面（bias expression + ASV + sensitivity curve + recommendation）"
    analysis: >
      工具包是 paper 被引用和实际使用的关键杠杆——纯理论 paper 引用衰减快，
      有配套工具的方法论 paper 被 cite 的周期长得多（参考 E-value 工具包对 VanderWeele & Ding 引用量的贡献）。
      在 AAAI/NeurIPS 审稿中，开源工具包也是 reproducibility + impact 的加分项。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20519930-a1af-4518-9a5a-ce7b0a0775ea",
  "isSidechain": false,
  "requestId": "req_011CbDRshvM2UiTAgRMoEpzL",
  "type": "assistant",
  "uuid": "fa0c6ae0-808b-4b24-99b4-a9c6d0e85c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PgdfZF8YquX9kmQtRvLBCi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18923,
      "cache_read_input_tokens": 23172,
      "output_tokens": 14349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18923,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14349,
          "cache_read_input_tokens": 23172,
          "cache_creation_input_tokens": 18923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18923
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

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：方向反转在 mediator 和 collider 拓扑均被确认；ASV 框架理论性质完整证明；实证数据展示 taxonomy 的实用区分力 核心假设：['非差异性多类误分类在 mediator/collider DAG 下产生方向反转（打破二分类保证）', 'ASV 单调性 + 紧致性在 3 个优先拓扑上均…",
  "leafUuid": "fa0c6ae0-808b-4b24-99b4-a9c6d0e85c44",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-class annotation errors and causal DAG bias",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：方向反转在 mediator 和 collider 拓扑均被确认；ASV 框架理论性质完整证明；实证数据展示 taxonomy 的实用区分力 核心假设：['非差异性多类误分类在 mediator/collider DAG 下产生方向反转（打破二分类保证）', 'ASV 单调性 + 紧致性在 3 个优先拓扑上均…",
  "leafUuid": "fa0c6ae0-808b-4b24-99b4-a9c6d0e85c44",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-class annotation errors and causal DAG bias",
  "sessionId": "898815c0-f847-4638-9e6c-fec5f265ed2f"
}
```

---
