# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：理论-实证桥梁完全闭合：3 claims 均以完整强度呈现，实证数据覆盖充分且 theory-empirical match 紧凑 核心假设：['API

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/e4f4b94b-3577-495c-a4a5-a9e9ba309783.jsonl`
- **Structured JSON:** [`9b92caea98a9a088ea51.json`](../../sessions/9b/9b92caea98a9a088ea51.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T05:50:10.676Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T05:50:10.676Z",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：理论-实证桥梁完全闭合：3 claims 均以完整强度呈现，实证数据覆盖充分且 theory-empirical match 紧凑\n核心假设：['API 402 解决，VAST/Civil Comments 获得 frontier 模型(≥235B)标注，消除 model-tier asymmetry', 'PPI++ 在真实 LLM 标注上 bias reduction 与 MC 一致(≥80%)，nondiff assumption 近似成立', 'theory-empirical bias magnitude match 紧凑(MAPE ≤ 15%)，topology ranking 在 K=2,3,10 全部复现', 'Dirichlet subspace 可视化成功说服 reviewer：empirical 0 sign flip 是因 LLM accuracy 落在 diag≥0.7 安全区，理论预测的 sign flip 区域与实际 LLM 数据点无交集', 'ASV 的 sample-dependent N* 和三类型设计(magnitude/significance/sign-flip)被接受为对 E-value 的实质性扩展']\n关键指标范围：{'usable_dataset_model_configs': [12, 14], 'theory_empirical_direction_match_pct': [95, 100], 'theory_empirical_magnitude_MAPE_pct': [5, 15], 'ppi_empirical_bias_reduction_pct': [80, 95], 'asv_unsafe_empirical_pct': [45, 60], 'f1_bias_pearson_r': [0.05, 0.2], 'correction_recommendation_accuracy_pct': [85, 95], 'iv_empirical_bias_pct_k3': [200, 300]}\n叙事方向：原始 framing 完全成立，三条 claim 均以 full strength 呈现： (1) taxonomy 捕获 K≥3 方向反转(exposure 83%/IV 52% sign flip)和结构保证(5/7 topologies sign_flip=0%)的完整图景； (2) ASV 三类型覆盖不同 DAG，significance_ASV 的 N* phase transition 是核心 actionable 贡献； (3) PPI++ universally reliable(93.8% MC + ≥80% empirical)，DSL topology-limited，naive/MLA Frisch-Waugh 失效。 Headline 无需修改：\"F1>0.9 的 LLM 在 IV 下仍 >200% bias，12% 场景效应放大无安全阈值。\"\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: causal_annot_error_attrib\nvenue: emnlp-2026\nfocus: Post-fix re-dream: all 5 structural issues resolved. Related work +5 refs, ASV vs PBA, Brenner footnote, IV subspace appendix, nondiff stress test appendix+limitations.\n\n## paper_framing.md\n\n# Paper Framing — causal_annot_error_attrib\n\n## Target Venue\n- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)\n- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)\n- Tertiary: ICWSM 2027 Round 2 (2026-09-15)\n\n## Title\nMulti-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies\n\n## Core Claims (3 条)\n\n1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 7 canonical social-science DAG topologies (confounding, exposure, mediation, collider, M-bias, instrument, front-door).\n\n2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of annotation error amplification needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Three complementary ASV types — magnitude (E-value-style robustness reporting, all topologies), significance (hypothesis testing filter, effective for attenuating topologies), and sign-flip (direction reversal warning, primarily exposure DAG) — because no single sensitivity metric suffices across all causal designs. The choice of appropriate ASV type is itself topology-dependent, reinforcing Claim 1. ASVs reveal a striking sensitivity ranking: IV estimates are maximally fragile (any annotation error exceeds threshold), while M-bias is immune (misclassification actually reduces spurious associations). Unlike E-values, ASVs incorporate study precision (sample-dependent), providing actionable guidance: for a given τ and σ, the critical sample size N* is analytically computable. Formal proofs (envelope monotonicity + sharpness) for 3 priority topologies; MC-validated for all 7.\n\n3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI++, MLA, MC-SIMEX, naive plug-in). Key findings from 210-configuration MC validation (7 topo × 6 C × 5 methods × 1000 sims): (a) Frisch-Waugh theorem makes naive_plugin/MLA fundamentally ineffective for T-coefficient bias in 4/7 topologies (bias reduction = 0.0%, exact); (b) DSL is topology-limited — effective only for confounding (50%) and mediation (70%), catastrophically harmful elsewhere (mbias -768%, IV -187%); (c) PPI++ is the only universally reliable method (93.8% grand mean bias reduction, 96.8% coverage) but requires gold-standard labels; (d) correction method effectiveness is itself topology-dependent, reinforcing Claim 1. Dependence-aware multi-LLM correction remains an open problem.\n\n## Story Spine\n\n- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31–50% of downstream conclusions are already incorrect — critically, even annotators with F1 > 0.93 produce > 50% error risk in downstream causal estimates. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable. The field's reliance on classification F1 as a proxy for downstream validity is fundamentally broken; our framework provides the missing link from annotation quality metrics to causal estimate reliability.\n\n- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.\n\n- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.\n\n- **Headline result template**: \"Across 7 DAG topologies with K=3, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. ASVs reveal a striking sensitivity spectrum: IV estimates are maximally fragile (any annotation error exceeds robustness thresholds), while M-bias associations are immune (misclassification reduces spurious bias). Empirical validation on 3 CSS tasks (K=2, 3, 10) annotated by 4 LLMs confirms the theoretical predictions: IV bias ranges from 30% at K=10 to 252% at K=3 across annotation settings, F1 does not predict downstream safety (F1=0.72 but IV bias>100%), and 55.4% of HumAID scenarios are ASV-unsafe, requiring correction or sensitivity reporting.\"\n\n## Core Insight (Lead Finding) — DUAL VERSION, gate on plan_001\n\n### Version A (≥1 topology shows direction reversal under K≥3 non-differential exposure misclassification)\nThe binary guarantee that \"non-differential exposure misclassification biases toward the null\" (Bross 1954) breaks in the multi-class case. For specific confusion matrix structures in specific DAG topologies, K≥3 non-differential error can amplify or reverse effect estimates. Brenner (1993) identified this possibility for polytomous confounder misclassification (\"bias can go in either direction\"); we provide the first systematic characterization across 7 DAG topologies with exact conditions for each {C structure × topology} cell. Furthermore, binarizing a K-class variable to \"escape\" into the binary regime is itself hazardous — collapsing introduces new, direction-unpredictable bias (MVP evidence: Δ up to 0.103).\n\n### Version B (no direction reversal found across topologies)\nMulti-class annotation error is structurally irreducible to the binary case: the downstream bias magnitude depends on the full K×K confusion matrix in ways that binary sensitivity/specificity cannot predict, and binarizing a K-class variable introduces new bias (MVP evidence: Δ up to 0.103). While non-differential error preserves bias direction across tested topologies (a useful practitioners' guarantee), the magnitude varies dramatically with confusion matrix structure (0.13–0.30 in confounding DAG alone), and this variation is topology-dependent. ASVs provide the missing robustness measure for this quantitative — not directional — uncertainty.\n\n**Gate**: RESOLVED → Version A. Two topologies show τ-specific direction reversal: exposure (~83-100% sign flip) and IV (~52% sign flip, Wald denominator mechanism). 5/7 topologies have structural guarantee τ_sign_flip=0% across K={3,5,7}. See D003, D004, D010.\n\n## MVP Evidence\n\n**Confounding DAG + K=3** (confounder misclassification):\n- Theoretical bias expressions match MC perfectly (6/6 structures within 95% CI) — framework validated\n- Binary collapse ≠ multi-class: Δ up to 0.103 (near-permutation C), proving K=3 retains more confounding control than binarization\n- 100k random C search: confounding DAG bias is monotonically toward OVB — this topology is \"well-behaved\" (predictable direction)\n- NOTE: Confounding DAG tests residual confounding, NOT bias-toward-null (Bross 1954). Criterion 2 (away-from-null bias) holds for binary too in this topology. See M001.\n\n**Exposure DAG K=3** (exposure misclassification — D002/D004 CONFIRMED):\n- 100k random C: 85% violate bias-toward-null, 83.4% sign reversal, 14.1% amplification\n- K=2 control: 6/6 toward null (binary guarantee holds)\n- Worst case: β₁=1.0 → γ̂₁=-0.84 (sign reversal, 0.84× magnitude); β₂=-0.5 → γ̂₂=-1.41 (2.83× amplification)\n- Mechanism: near-permutation C causes label swap → effect direction flips (structurally impossible in K=2)\n- **Two-DAG contrast**: confounding (monotonic, predictable) vs exposure (unpredictable, topology-dependent) — validates core claim\n\n**Dirichlet subspace analysis** (practical relevance validation):\n- diag≥0.5: 32.5% violation, 21.6% sign reversal, 11.3% amplification\n- diag≥0.7 (typical LLM accuracy): **13.7% violation**, 2.1% sign reversal, **11.7% amplification**\n- diag≥0.9 (high-accuracy LLM): **11.9% violation**, 0% sign reversal, **11.9% amplification**\n- Key pattern: sign reversal vanishes at high accuracy, but **amplification persists at ~12% regardless of accuracy**\n- Implication: even 90%+ accuracy LLMs face non-trivial effect amplification risk — no \"safe accuracy threshold\" exists\n\n**IV Dirichlet subspace analysis** (Dream feedback, 2026-05-21):\n- Full: 100% violation, 51.7% sign flip, 48.3% amplification\n- diag≥0.5: 100% violation, **0% sign flip**, 100% amplification, worst 28.6×\n- diag≥0.7: 100% violation, 0% sign flip, 100% amplification, worst 2.4×\n- diag≥0.9: 100% violation, 0% sign flip, 100% amplification, worst 1.2×\n- Key contrast with exposure: IV sign flip vanishes at diag≥0.5 (exposure persists at 2.1% at diag≥0.7), but IV amplification is **universal** (100% at all thresholds, vs exposure 11.7% at diag≥0.7)\n- Mechanism: Wald denominator monotonically contracts; diagonal dominance prevents zero-crossing (no sign flip) but not contraction (amplification)\n\n## Venue Fit Risks\n\n- **AAAI**: Broad AI audience — emphasize general methodology for \"automated annotation measurement error,\" not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.\n- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.\n- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n1. **\"Trivial extension of binary to multi-class\"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 7 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]\n\n2. **\"Lee & Wood-Doughty (2024) already did categorical\"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 7 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]\n\n3. **\"Why these 7 DAG topologies?\"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: exposure (treatment), confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]\n\n4. **\"K≥5 expressions aren't actionable\"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]\n\n5. **\"ASV sharpness only proved for 3 topologies\"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]\n\n6. **\"Correlated multi-LLM errors?\"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]\n\n7. **\"Empirical validation scope\"** → 3 CSS tasks (HumAID K=10, VAST K=3, Civil Comments K=2) × 4 LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat, Qwen2.5-7B) × 7 topologies = 14 configs. D016 confirms: topology ranking matches theory across all K values; IV bias co-varies with annotation setting (K=3 IV bias 252% vs K=10 30%, confounded with dataset/model differences); 7B vs 235B bias ratio 1.24 (model scale not dominant). 0 sign flips across all 98 scenarios. Note: VAST/Civil Comments use 7B local model (API 402 blocker), creating a model-tier asymmetry acknowledged in Limitations. [Experiments: plan_003, plan_006]\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: Derive and MC-validate bias expressions for 6 DAG topologies with K=3\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: plan001_dag_taxonomy\n  details: 'For each topology (confounding, mediation, collider, M-bias, instrument,\n    front-door): derive closed-form K=3 bias expression, validate with MC (1000 reps\n    × N=10000, 6 confusion matrix structures including near-permutation extreme).\n    Key question: which topologies show direction reversal under non-differential\n    error? Confounding already validated in MVP (no reversal, monotonic toward OVB).\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    collider:\n      all_coef:\n        violation: 1\n        sign_flip: 0.688\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 0\n      small_tau_0.05:\n        tau_I: 0.015733\n        tau_violation: 0.96\n        tau_sign_flip: 0\n        tau_amplification: 0.992\n      small_tau_0.1:\n        tau_I: 0.06118\n        tau_violation: 0.974\n        tau_sign_flip: 0\n        tau_amplification: 0.995\n    mbias:\n      all_coef:\n        violation: 1\n        sign_flip: 0.651\n        amplification: 0.112\n      tau_specific:\n        violation: 0.532\n        sign_flip: 0\n        amplification: 0.104\n      misclass_amplifies_rate: 0.292\n      small_tau_0.05:\n        tau_I: 0.057669\n        tau_violation: 0.532\n        tau_sign_flip: 0\n        tau_amplification: 0.104\n      small_tau_0.1:\n        tau_I: 0.107669\n        tau_violation: 0.532\n        tau_sign_flip: 0\n        tau_amplification: 0.104\n    mediation_mixed:\n      all_coef:\n        violation: 1\n        sign_flip: 0.835\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    mediation_same:\n      all_coef:\n        violation: 1\n        sign_flip: 0.666\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    frontdoor_mixed:\n      all_coef:\n        violation: 1\n        sign_flip: 0.998\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_I: 0.050177\n        lambda_U: 0.1\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_I: 0.100169\n        lambda_U: 0.2\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    frontdoor_same:\n      all_coef:\n        violation: 1\n        sign_flip: 1\n        amplification: 1\n      tau_specific:\n        violation: 0.999\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 0.9997\n      small_tau_0.05:\n        tau_I: 0.050177\n        lambda_U: 0.1\n        tau_violation: 0.999\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_I: 0.100169\n        lambda_U: 0.2\n        tau_violation: 0.999\n        tau_sign_flip: 0\n        tau_amplification: 1\n    iv_note: 'IV metrics not computed in plan_001 (only 6 fixed C structures tested,\n      no dedicated IV tau_specific analysis). First measured in plan_002: 52% tau_specific_sign_flip\n      from 100k random C (Wald denominator sign reversal). See plan002_k57_extension\n      for full IV results.'\n- id: plan_002\n  claim: 1\n  description: Extend bias expressions to K=5,7 — matrix notation + interpretability\n    tools\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: plan002_k57_extension\n  details: 'Matrix-form expressions for general K. Three interpretability tools: (a)\n    eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar\n    bounds collapsing matrix to conservative scalar, (c) diagnostic visualizations\n    mapping confusion matrix regions to bias magnitude. Validate on confounding +\n    mediation + collider DAGs with K=5,7.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_k_comparison_7topo:\n      confounding:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.993\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1614\n          worst_case_diag70: 0.2744\n          worst_case_diag50: 0.2993\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1107\n          worst_case_diag70: 0.2156\n          worst_case_diag50: 0.2462\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0933\n          worst_case_diag70: 0.1859\n          worst_case_diag50: 0.2264\n      mediation:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.838\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1223\n          worst_case_diag70: 0.251\n          worst_case_diag50: 0.3032\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.966\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0867\n          worst_case_diag70: 0.1832\n          worst_case_diag50: 0.2396\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0607\n          worst_case_diag70: 0.1421\n          worst_case_diag50: 0.1879\n      collider:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.666\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0503\n          worst_case_diag70: 0.1064\n          worst_case_diag50: 0.1256\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.955\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0477\n          worst_case_diag70: 0.1087\n          worst_case_diag50: 0.1306\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.992\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0352\n          worst_case_diag70: 0.0826\n          worst_case_diag50: 0.1131\n      exposure:\n        K3:\n          tau_specific_sign_flip: N/A (all-coef fallback; MVP beta1 flip=83.4%)\n          all_coef_sign_flip: 0.99\n          violation: 1\n          amplification: 0.999\n          worst_case_diag90: 0.2726\n          worst_case_diag70: 0.7092\n          worst_case_diag50: 1.1438\n        K5:\n          tau_specific_sign_flip: N/A (all-coef fallback)\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 0.998\n          worst_case_diag90: 0.2097\n          worst_case_diag70: 0.5782\n          worst_case_diag50: 0.8784\n        K7:\n          tau_specific_sign_flip: N/A (all-coef fallback)\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 0.999\n          worst_case_diag90: 0.1853\n          worst_case_diag70: 0.4913\n          worst_case_diag50: 0.7441\n      mbias:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.667\n          violation: 0.584\n          amplification: 0.089\n          worst_case_diag90: 0.0106\n          worst_case_diag70: 0.0226\n          worst_case_diag50: 0.0287\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.954\n          violation: 1\n          amplification: 0\n          worst_case_diag90: 0.0154\n          worst_case_diag70: 0.0374\n          worst_case_diag50: 0.0487\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.992\n          violation: 1\n          amplification: 0\n          worst_case_diag90: 0.0133\n          worst_case_diag70: 0.0319\n          worst_case_diag50: 0.0449\n      iv:\n        K3:\n          tau_specific_sign_flip: 0.526\n          all_coef_sign_flip: 0.526\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.2993\n          worst_case_diag70: 1.6444\n          worst_case_diag50: 14.0463\n          note: Wald estimator extremely unstable at low accuracy\n        K5:\n          tau_specific_sign_flip: 0.514\n          all_coef_sign_flip: 0.514\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.4053\n          worst_case_diag70: 2.1036\n          worst_case_diag50: 9.6932\n        K7:\n          tau_specific_sign_flip: 0.523\n          all_coef_sign_flip: 0.523\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.3605\n          worst_case_diag70: 1.8132\n          worst_case_diag50: 8.2204\n      frontdoor:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.836\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1407\n          worst_case_diag70: 0.2604\n          worst_case_diag50: 0.2966\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.967\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1057\n          worst_case_diag70: 0.2066\n          worst_case_diag50: 0.2507\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.993\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0785\n          worst_case_diag70: 0.1646\n          worst_case_diag50: 0.2119\n    conclusion_summary:\n      structural_guarantee: tau_specific_sign_flip = 0% across ALL K for 5/7 topologies\n        (confounding/mediation/collider/mbias/frontdoor)\n      iv_new_finding: IV ~52% tau sign flip (K-invariant) — Wald denominator sign\n        reversal under random C\n      exposure_clarification: Exposure tau_spec_sflip column is all-coef fallback.\n        Actual beta1-specific flip rate = 83.4% (from MVP)\n      worst_case_trend: Decreasing with K for 5/7 topologies (K=3 most conservative).\n        IV catastrophic at low accuracy (WC_d50 up to 14x). Exposure decreasing.\n      mbias_special: Amplification drops to 0% at K>=5\n      rng_fix: Deterministic per-(topo,K,threshold) seeds via SHA-256. Previous values\n        had RNG ordering artifact.\n    runtime_seconds: 20\n    gpu: RTX 5090 cuda:0\n    script: /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py\n- id: plan_003\n  claim: 1\n  description: 'Empirical confusion matrices: 3 LLMs × 3 CSS tasks vs gold-standard'\n  priority: P0\n  gpu_budget_hours: 0\n  api_cost_estimate: $300-550\n  deps: []\n  registry_id: plan003_empirical_confusion_matrices\n  details: 'Tasks: crisis event classification (K=10, HumAID), stance detection (K=3,\n    VAST), toxicity (K=2, as special case / consistency check, Civil Comments). Models:\n    Llama 4 Maverick (Together.ai/OpenRouter), Qwen 3 235B (OpenRouter), DeepSeek\n    Chat V3 (DeepSeek API). ~30K annotations per model × 3 datasets × 3 prompt variants.\n    Output: empirical confusion matrices, inter-model correlation analysis, downstream\n    regression bias vs gold-standard baseline. Inter-model error correlation analysis:\n    for each of 3 model pairs, compute error agreement rate, conditional error correlation\n    (given true label), and Cohen''s kappa on errors. Quantify correlated-error structure\n    to inform whether independent-error assumptions in correction methods hold.\n\n    '\n  status: DONE\n  conclusion: failed\n  metrics:\n    status_detail: PAUSED - API 402 Payment Required (OPENROUTER_API_KEY)\n    api_endpoint: http://47.94.22.126/v1/chat/completions\n    data_dir: results/\n    humaid_recount_20260520T2312:\n      deepseek_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      deepseek_few-shot-3:\n        total: 1500\n        pred_valid: 1345\n        errors: 155\n        error_type: parsing\n        status: WARN\n      deepseek_few-shot-5:\n        total: 1500\n        pred_valid: 1237\n        errors: 263\n        error_type: parsing\n        status: WARN\n      llama4_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      llama4_few-shot-3:\n        total: 1500\n        pred_valid: 1498\n        errors: 2\n        status: OK\n      llama4_few-shot-5:\n        total: 1500\n        pred_valid: 1471\n        errors: 29\n        status: WARN\n      qwen3_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      qwen3_few-shot-3:\n        total: 1500\n        pred_valid: 1423\n        errors: 77\n        error_type: '402'\n        status: WARN\n      qwen3_few-shot-5:\n        total: 1500\n        pred_valid: 0\n        errors: 1500\n        error_type: '402'\n        status: FAIL\n    humaid_summary: 4 OK (≥1498) + 4 WARN (1237-1471) + 1 FAIL (qwen3_fs5 all 402)\n    humaid_usable: 8/9 files have valid data\n    data_fields:\n      true_label: gold_label\n      pred_label: pred_label\n    note: deepseek errors are parsing/format, NOT 402. Only qwen3 errors are 402.\n- id: plan_008\n  claim: 1\n  description: 'Binarization collapse analysis: K→2 folding bias across all 6 topologies'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan008_binarization_collapse\n  details: 'For each of 6 topologies with K=3,5,7: collapse to binary, compare bias\n    from full multi-class expression vs binarized expression. Demonstrate that binarization\n    is not a safe shortcut — can amplify or reverse bias. MVP showed Δ up to 0.089\n    for confounding DAG K=3.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    confounding:\n      D_mean: 0.0253\n      D_med: 0.0182\n      D_P95: 0.0733\n      D_max: 0.2213\n      frac_gt_001: 0.686\n      frac_gt_005: 0.138\n      sign_flip: 0\n    mediation:\n      D_mean: 0.0446\n      D_med: 0.0355\n      D_P95: 0.1179\n      D_max: 0.252\n      frac_gt_001: 0.835\n      frac_gt_005: 0.36\n      sign_flip: 0\n    collider:\n      D_mean: 0.0169\n      D_med: 0.0125\n      D_P95: 0.0472\n      D_max: 0.1069\n      frac_gt_001: 0.572\n      frac_gt_005: 0.039\n      sign_flip: 0\n    M-bias:\n      D_mean: 0.0063\n      D_med: 0.0054\n      D_P95: 0.0147\n      D_max: 0.0328\n      frac_gt_001: 0.181\n      frac_gt_005: 0\n      sign_flip: 0\n    exposure:\n      D_mean: 0.5164\n      D_med: 0.506\n      D_P95: 0.8453\n      D_max: 1.3876\n      frac_gt_001: 1\n      frac_gt_005: 0.999\n      sign_flip: 0.14\n    IV:\n      D_mean: 0.926\n      D_med: 0.9394\n      D_P95: 1.3426\n      D_max: 2.0809\n      frac_gt_001: 1\n      frac_gt_005: 1\n      sign_flip: 0.175\n- id: plan_004\n  claim: 2\n  description: 'ASV framework: formal proofs for confounding, mediation, collider'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan004_asv_framework\n  details: 'Derive ASV expressions for 3 priority topologies. Formal proofs of: (a)\n    monotonicity (ASV increases with δ amplification), (b) sharpness (bound is achievable\n    for some confusion matrix). MC validation: coverage at 90%, 95%, 99% levels across\n    1000 scenarios. Additionally report Type I/II error rates: rejection rate under\n    null (Type I) and power under alternative, before and after ASV-informed correction.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    v2_sign_flip_filter: ✅ effective (Type I=0%, power=100%)\n    v3_envelope_monotonicity: ✅ solved (0 violations)\n    v3_magnitude_reporting: ✅ informative values for all topologies\n    v3_magnitude_filter: ❌ rejected (scale-dependent, not viable as binary test)\n    v3_fixed_signif_filter: ✅ Type I=0% all topologies, power=100% for τ≥0.1\n    v3_significance_filter:\n      confounding_tau005:\n        type_i: 0\n        power: 1\n      confounding_tau010:\n        type_i: 0\n        power: 1\n      mediation_tau005:\n        type_i: 0\n        power: 0\n      mediation_tau010:\n        type_i: 0\n        power: 1\n      collider_tau005:\n        type_i: 0\n        power: 0\n      collider_tau010:\n        type_i: 0\n        power: 1\n      note: τ=0.05 mediation/collider power=0% is correct — attenuating topologies\n        are fragile at small effects\n    v3_fixed_status: complete — significance filter validated\n    v3_envelope_violations: 0\n    v3_magnitude_asv_tau0.5_range: 0.076-0.487\n    v3_magnitude_asv_tau0.05_range: 0.008-0.047\n    v3_magnitude_asv_tau0.1_range: 0.014-0.093\n    v3_coverage_tau0.05: 100.0%\n    v3_coverage_tau0.1: 100.0%\n    n_sensitivity_mediation_tau005:\n      topology: mediation\n      tau: 0.05\n      C0: sym_mild\n      mc_reps: 500\n      N_1000:\n        naive_power: 0.89\n        asv_power: 0\n        median_se: 0.070025\n        median_signif_asv: 0\n      N_2000:\n        naive_power: 0.998\n        asv_power: 0\n        median_se: 0.049649\n        median_signif_asv: 0\n      N_5000:\n        naive_power: 1\n        asv_power: 0\n        median_se: 0.031301\n        median_signif_asv: 0\n      N_10000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.022152\n        median_signif_asv: null\n      N_20000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.01566\n        median_signif_asv: null\n      N_50000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.009903\n        median_signif_asv: null\n      recovery_N: 10000\n      interpretation: 'Sharp phase transition at N~6000-10000. Below: 1.96*SE > tau=0.05\n        so signif_ASV=0 (ASV kills all rejections). Above: 1.96*SE < tau=0.05 so signif_ASV=None\n        (infinite robustness), ASV passes all.'\n- id: plan_005\n  claim: 2\n  description: ASV MC validation for M-bias, instrument, front-door topologies\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_004\n  registry_id: plan005_asv_extended\n  details: 'ASV expressions + MC validation of monotonicity and coverage. Sharpness\n    stated as conjectures supported by numerical evidence. If any topology fails monotonicity\n    under MC, flag and investigate.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    envelope_violations:\n      mbias: 0\n      iv: 0\n      frontdoor: 0\n    plim_at_identity:\n      mbias: 0.5128\n      iv: 0.6598\n      frontdoor: 0.4998\n    asv_tau05:\n      mbias:\n        sign_flip: null\n        magnitude_10pct: null\n      iv:\n        sign_flip_range: 1.1-6.7\n        magnitude_10pct_range: 0.101-0.607\n      frontdoor:\n        sign_flip: null\n        magnitude_10pct_range: 0.064-0.387\n    mc_coverage:\n      mbias_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      mbias_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n      iv_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      iv_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n      frontdoor_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      frontdoor_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n    v_fixed_signif_filter:\n      mbias:\n        type_i: 0\n        power_tau005: 95.8-99.2%\n        power_tau01: 100%\n      iv:\n        type_i: 0\n        power_tau005: 0%\n        power_tau01: 0%\n        note: correct — Wald estimator immediately fragile, signif_ASV≈0 blocks all\n          rejections\n      frontdoor:\n        type_i: 0\n        power_tau005: 100%\n        power_tau01: 100%\n    fixes_applied:\n    - 'C1: compute_signif_asv_fast added'\n    - 'C2: magnitude ASV tau≈0 returns 0.0'\n    - 'W1: IV tau_true=plim_iv(I)=0.6598'\n    - 'W2: M-bias tau_true=plim_mb(I)=0.5128'\n    fixed_script: /home/sonny/causal_annot_error_attrib/plan_005_asv_extended_fixed.py\n    runtime_seconds: 46.2\n- id: plan_006\n  claim: 2\n  description: ASV calibration on empirical data (3 CSS tasks × 3 LLMs)\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  - plan_004\n  details: 'Apply ASVs to empirical confusion matrices from plan_003. Validate coverage\n    on held-out gold-standard splits. Report ASV alongside downstream effect estimates\n    for each task. Compare ASV interpretability with raw confusion matrix reporting.\n    Report Type I/II error rates: rejection rate under null (Type I) and power under\n    alternative, before and after ASV-informed correction, across all task × model\n    combinations. F1 vs downstream causal bias analysis: for each model × task, compute\n    classification F1 and plot against |downstream bias|. Demonstrate that high F1\n    does not guarantee low downstream bias (Baumann 2025: F1>0.93 still >50% error\n    risk). This bridges the gap between annotation quality metrics and causal estimate\n    reliability.\n\n    '\n  status: planned\n- id: plan_007\n  claim: 3\n  description: 'Correction guidance framework: decision mapping + validation'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_004\n  - plan_003\n  details: 'Decision framework: {topology × error structure × ASV} → correction method\n    (DSL / PPI / MLA / MC-SIMEX / naive plug-in / \"no existing method adequate\").\n    MC validation: recommended method produces least bias in ≥90% of scenarios. Empirical\n    validation on plan_003 data. Characterize regimes where no existing method suffices\n    (correlated errors, differential multi-class, etc.) — identify as open problems.\n\n    '\n  status: planned\n- id: plan_009\n  claim: 1\n  description: Pathological confusion matrix analysis (near-permutation, rank-deficient)\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  registry_id: plan009_pathological_matrices\n  details: 'Extreme C structures: near-permutation, rank-deficient, block-diagonal.\n    Characterize when bias becomes catastrophic across topologies. Identify structural\n    conditions (spectral gap, diagonal dominance ratio) that predict bias severity\n    — candidate features for practitioners.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    regression_dichotomy:\n      benign_topologies:\n        list:\n        - confounding\n        - mediation\n        - collider\n        - frontdoor\n        - mbias\n        R2_range: 0.61-0.77\n        primary_predictor: effective_rank\n        secondary_predictors:\n        - spectral_gap\n        - condition_number\n      dangerous_topologies:\n        list:\n        - exposure\n        - iv\n        exposure_R2: 0.11\n        iv_R2: ~0\n        iv_note: regression has no explanatory power — Wald denominator sign reversal\n          is discrete, not predicted by continuous matrix features\n        exposure_note: 'near_perm eps=0.01: 15% catastrophic bias above threshold'\n      global_R2: ~0 (cross-topology aggregation destroys predictive power — different\n        bias mechanisms)\n    risk_tiers:\n      low:\n        topologies:\n        - mbias\n        max_bias: <0.04\n        note: safe even under worst-case pathological C\n      medium:\n        topologies:\n        - confounding\n        - mediation\n        - collider\n        - frontdoor\n        bias_range: 0.1-0.31\n        catastrophic_fraction: 0%\n        R2: 0.70-0.77\n        note: bounded bias, matrix features predictive\n      high:\n        topologies:\n        - exposure\n        - iv\n        note: 'catastrophic regardless of C quality — exposure: structural identification\n          failure; IV: Wald estimator explosion (near_perm eps=0.01 cat=61-73%, rank-deficient\n          bias reaches millions)'\n    most_consistent_predictor: condition_number (significant in 5/5 medium-risk topologies)\n    hypothesis_assessment:\n      H1_predictable_catastrophic: partially — risk tier determined by topology, not\n        C features\n      H2_matrix_features_strong: topology-dependent — 5/7 R²>0.6, exposure/IV fail\n      H3_safety_threshold: not confirmed — boundary is topology-based, not C-feature\n        threshold\n      H4_diagnostic_features: partially — condition_number most consistent, but needs\n        topology-specific criteria\n    iv_filtering:\n      n_filtered: 3000\n      n_total: 28000\n      pct_infinite: 10.7\n      note: non-finite Wald values silently filtered from regression; must note in\n        paper\n    pathological_C_types:\n    - near_permutation (eps=0.01,0.05,0.1,0.2)\n    - rank_deficient\n    - block_diagonal\n    K_values:\n    - 3\n    - 5\n    - 7\n    M_per_config: 1000\n    N_per_sim: 5000000\n    runtime_seconds: 25\n    analysis_report: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md\n    output_files:\n      summary_json: /home/sonny/causal_annot_error_attrib/artifacts/plan009/pathological_bias_summary.json\n      regression_txt: /home/sonny/causal_annot_error_attrib/artifacts/plan009/regression_results.txt\n      analysis_md: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md\n- id: plan_010\n  claim: 1\n  description: annot-sensitivity Python toolkit (open-source release)\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_004\n  - plan_007\n  details: 'Package: user-specified DAG + confusion matrix(es) + downstream estimate\n    → bias expressions (scalar K≤3, matrix K>3 with interpretability) + ASV bounds\n    + sensitivity curves + correction recommendation + diagnostic plots. pip-installable,\n    with worked examples for each topology.\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_confounding_dag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    theory_mc_match: 6/6\n    pass_criteria: 3/3\n    max_binary_collapse_delta: 0.103\n    bias_range: 0.132-0.298\n    ovb_reference: 0.3\n    direction_reversal_found: false\n    random_search_100k_min_bias: 0.063\n- exp_id: mvp_exposure_dag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    theory_mc_match: 5/5\n    pass_criteria: 3/3\n    violation_rate: 0.85\n    sign_reversal_rate: 0.834\n    amplification_rate: 0.141\n    K2_toward_null: 6/6\n    worst_severity: 2.83\n    named_structures_with_violation: 3/6\n- exp_id: mvp_exposure_dirichlet_subspace\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_space_violation: 0.849\n    full_space_sign_rev: 0.833\n    full_space_amplif: 0.275\n    diag50_violation: 0.325\n    diag50_sign_rev: 0.216\n    diag50_amplif: 0.113\n    diag70_violation: 0.137\n    diag70_sign_rev: 0.021\n    diag70_amplif: 0.117\n    diag90_violation: 0.119\n    diag90_sign_rev: 0\n    diag90_amplif: 0.119\n    samples_per_subspace: 50000\n    assessment: ALL subspaces STRONG (>10%)\n- exp_id: plan001_dag_taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    collider:\n      all_coef:\n        violation: 1\n        sign_flip: 0.688\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 0\n      small_tau_0.05:\n        tau_I: 0.015733\n        tau_violation: 0.96\n        tau_sign_flip: 0\n        tau_amplification: 0.992\n      small_tau_0.1:\n        tau_I: 0.06118\n        tau_violation: 0.974\n        tau_sign_flip: 0\n        tau_amplification: 0.995\n    mbias:\n      all_coef:\n        violation: 1\n        sign_flip: 0.651\n        amplification: 0.112\n      tau_specific:\n        violation: 0.532\n        sign_flip: 0\n        amplification: 0.104\n      misclass_amplifies_rate: 0.292\n      small_tau_0.05:\n        tau_I: 0.057669\n        tau_violation: 0.532\n        tau_sign_flip: 0\n        tau_amplification: 0.104\n      small_tau_0.1:\n        tau_I: 0.107669\n        tau_violation: 0.532\n        tau_sign_flip: 0\n        tau_amplification: 0.104\n    mediation_mixed:\n      all_coef:\n        violation: 1\n        sign_flip: 0.835\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    mediation_same:\n      all_coef:\n        violation: 1\n        sign_flip: 0.666\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    frontdoor_mixed:\n      all_coef:\n        violation: 1\n        sign_flip: 0.998\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_I: 0.050177\n        lambda_U: 0.1\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_I: 0.100169\n        lambda_U: 0.2\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    frontdoor_same:\n      all_coef:\n        violation: 1\n        sign_flip: 1\n        amplification: 1\n      tau_specific:\n        violation: 0.999\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 0.9997\n      small_tau_0.05:\n        tau_I: 0.050177\n        lambda_U: 0.1\n        tau_violation: 0.999\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_I: 0.100169\n        lambda_U: 0.2\n        tau_violation: 0.999\n        tau_sign_flip: 0\n        tau_amplification: 1\n    iv_note: 'IV metrics not computed in plan_001 (only 6 fixed C structures tested,\n      no dedicated IV tau_specific analysis). First measured in plan_002: 52% tau_specific_sign_flip\n      from 100k random C (Wald denominator sign reversal). See plan002_k57_extension\n      for full IV results.'\n- exp_id: plan003_empirical_confusion_matrices\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    status_detail: PAUSED - API 402 Payment Required (OPENROUTER_API_KEY)\n    api_endpoint: http://47.94.22.126/v1/chat/completions\n    data_dir: results/\n    humaid_recount_20260520T2312:\n      deepseek_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      deepseek_few-shot-3:\n        total: 1500\n        pred_valid: 1345\n        errors: 155\n        error_type: parsing\n        status: WARN\n      deepseek_few-shot-5:\n        total: 1500\n        pred_valid: 1237\n        errors: 263\n        error_type: parsing\n        status: WARN\n      llama4_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      llama4_few-shot-3:\n        total: 1500\n        pred_valid: 1498\n        errors: 2\n        status: OK\n      llama4_few-shot-5:\n        total: 1500\n        pred_valid: 1471\n        errors: 29\n        status: WARN\n      qwen3_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      qwen3_few-shot-3:\n        total: 1500\n        pred_valid: 1423\n        errors: 77\n        error_type: '402'\n        status: WARN\n      qwen3_few-shot-5:\n        total: 1500\n        pred_valid: 0\n        errors: 1500\n        error_type: '402'\n        status: FAIL\n    humaid_summary: 4 OK (≥1498) + 4 WARN (1237-1471) + 1 FAIL (qwen3_fs5 all 402)\n    humaid_usable: 8/9 files have valid data\n    data_fields:\n      true_label: gold_label\n      pred_label: pred_label\n    note: deepseek errors are parsing/format, NOT 402. Only qwen3 errors are 402.\n- exp_id: plan004_asv_framework\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    v2_sign_flip_filter: ✅ effective (Type I=0%, power=100%)\n    v3_envelope_monotonicity: ✅ solved (0 violations)\n    v3_magnitude_reporting: ✅ informative values for all topologies\n    v3_magnitude_filter: ❌ rejected (scale-dependent, not viable as binary test)\n    v3_fixed_signif_filter: ✅ Type I=0% all topologies, power=100% for τ≥0.1\n    v3_significance_filter:\n      confounding_tau005:\n        type_i: 0\n        power: 1\n      confounding_tau010:\n        type_i: 0\n        power: 1\n      mediation_tau005:\n        type_i: 0\n        power: 0\n      mediation_tau010:\n        type_i: 0\n        power: 1\n      collider_tau005:\n        type_i: 0\n        power: 0\n      collider_tau010:\n        type_i: 0\n        power: 1\n      note: τ=0.05 mediation/collider power=0% is correct — attenuating topologies\n        are fragile at small effects\n    v3_fixed_status: complete — significance filter validated\n    v3_envelope_violations: 0\n    v3_magnitude_asv_tau0.5_range: 0.076-0.487\n    v3_magnitude_asv_tau0.05_range: 0.008-0.047\n    v3_magnitude_asv_tau0.1_range: 0.014-0.093\n    v3_coverage_tau0.05: 100.0%\n    v3_coverage_tau0.1: 100.0%\n    n_sensitivity_mediation_tau005:\n      topology: mediation\n      tau: 0.05\n      C0: sym_mild\n      mc_reps: 500\n      N_1000:\n        naive_power: 0.89\n        asv_power: 0\n        median_se: 0.070025\n        median_signif_asv: 0\n      N_2000:\n        naive_power: 0.998\n        asv_power: 0\n        median_se: 0.049649\n        median_signif_asv: 0\n      N_5000:\n        naive_power: 1\n        asv_power: 0\n        median_se: 0.031301\n        median_signif_asv: 0\n      N_10000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.022152\n        median_signif_asv: null\n      N_20000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.01566\n        median_signif_asv: null\n      N_50000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.009903\n        median_signif_asv: null\n      recovery_N: 10000\n      interpretation: 'Sharp phase transition at N~6000-10000. Below: 1.96*SE > tau=0.05\n        so signif_ASV=0 (ASV kills all rejections). Above: 1.96*SE < tau=0.05 so signif_ASV=None\n        (infinite robustness), ASV passes all.'\n- exp_id: plan008_binarization_collapse\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    confounding:\n      D_mean: 0.0253\n      D_med: 0.0182\n      D_P95: 0.0733\n      D_max: 0.2213\n      frac_gt_001: 0.686\n      frac_gt_005: 0.138\n      sign_flip: 0\n    mediation:\n      D_mean: 0.0446\n      D_med: 0.0355\n      D_P95: 0.1179\n      D_max: 0.252\n      frac_gt_001: 0.835\n      frac_gt_005: 0.36\n      sign_flip: 0\n    collider:\n      D_mean: 0.0169\n      D_med: 0.0125\n      D_P95: 0.0472\n      D_max: 0.1069\n      frac_gt_001: 0.572\n      frac_gt_005: 0.039\n      sign_flip: 0\n    M-bias:\n      D_mean: 0.0063\n      D_med: 0.0054\n      D_P95: 0.0147\n      D_max: 0.0328\n      frac_gt_001: 0.181\n      frac_gt_005: 0\n      sign_flip: 0\n    exposure:\n      D_mean: 0.5164\n      D_med: 0.506\n      D_P95: 0.8453\n      D_max: 1.3876\n      frac_gt_001: 1\n      frac_gt_005: 0.999\n      sign_flip: 0.14\n    IV:\n      D_mean: 0.926\n      D_med: 0.9394\n      D_P95: 1.3426\n      D_max: 2.0809\n      frac_gt_001: 1\n      frac_gt_005: 1\n      sign_flip: 0.175\n- exp_id: plan005_asv_extended\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    envelope_violations:\n      mbias: 0\n      iv: 0\n      frontdoor: 0\n    plim_at_identity:\n      mbias: 0.5128\n      iv: 0.6598\n      frontdoor: 0.4998\n    asv_tau05:\n      mbias:\n        sign_flip: null\n        magnitude_10pct: null\n      iv:\n        sign_flip_range: 1.1-6.7\n        magnitude_10pct_range: 0.101-0.607\n      frontdoor:\n        sign_flip: null\n        magnitude_10pct_range: 0.064-0.387\n    mc_coverage:\n      mbias_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      mbias_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n      iv_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      iv_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n      frontdoor_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      frontdoor_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n    v_fixed_signif_filter:\n      mbias:\n        type_i: 0\n        power_tau005: 95.8-99.2%\n        power_tau01: 100%\n      iv:\n        type_i: 0\n        power_tau005: 0%\n        power_tau01: 0%\n        note: correct — Wald estimator immediately fragile, signif_ASV≈0 blocks all\n          rejections\n      frontdoor:\n        type_i: 0\n        power_tau005: 100%\n        power_tau01: 100%\n    fixes_applied:\n    - 'C1: compute_signif_asv_fast added'\n    - 'C2: magnitude ASV tau≈0 returns 0.0'\n    - 'W1: IV tau_true=plim_iv(I)=0.6598'\n    - 'W2: M-bias tau_true=plim_mb(I)=0.5128'\n    fixed_script: /home/sonny/causal_annot_error_attrib/plan_005_asv_extended_fixed.py\n    runtime_seconds: 46.2\n- exp_id: plan_004_asv_v3_fixed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan002_k57_extension\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_k_comparison_7topo:\n      confounding:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.993\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1614\n          worst_case_diag70: 0.2744\n          worst_case_diag50: 0.2993\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1107\n          worst_case_diag70: 0.2156\n          worst_case_diag50: 0.2462\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0933\n          worst_case_diag70: 0.1859\n          worst_case_diag50: 0.2264\n      mediation:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.838\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1223\n          worst_case_diag70: 0.251\n          worst_case_diag50: 0.3032\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.966\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0867\n          worst_case_diag70: 0.1832\n          worst_case_diag50: 0.2396\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0607\n          worst_case_diag70: 0.1421\n          worst_case_diag50: 0.1879\n      collider:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.666\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0503\n          worst_case_diag70: 0.1064\n          worst_case_diag50: 0.1256\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.955\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0477\n          worst_case_diag70: 0.1087\n          worst_case_diag50: 0.1306\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.992\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0352\n          worst_case_diag70: 0.0826\n          worst_case_diag50: 0.1131\n      exposure:\n        K3:\n          tau_specific_sign_flip: N/A (all-coef fallback; MVP beta1 flip=83.4%)\n          all_coef_sign_flip: 0.99\n          violation: 1\n          amplification: 0.999\n          worst_case_diag90: 0.2726\n          worst_case_diag70: 0.7092\n          worst_case_diag50: 1.1438\n        K5:\n          tau_specific_sign_flip: N/A (all-coef fallback)\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 0.998\n          worst_case_diag90: 0.2097\n          worst_case_diag70: 0.5782\n          worst_case_diag50: 0.8784\n        K7:\n          tau_specific_sign_flip: N/A (all-coef fallback)\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 0.999\n          worst_case_diag90: 0.1853\n          worst_case_diag70: 0.4913\n          worst_case_diag50: 0.7441\n      mbias:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.667\n          violation: 0.584\n          amplification: 0.089\n          worst_case_diag90: 0.0106\n          worst_case_diag70: 0.0226\n          worst_case_diag50: 0.0287\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.954\n          violation: 1\n          amplification: 0\n          worst_case_diag90: 0.0154\n          worst_case_diag70: 0.0374\n          worst_case_diag50: 0.0487\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.992\n          violation: 1\n          amplification: 0\n          worst_case_diag90: 0.0133\n          worst_case_diag70: 0.0319\n          worst_case_diag50: 0.0449\n      iv:\n        K3:\n          tau_specific_sign_flip: 0.526\n          all_coef_sign_flip: 0.526\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.2993\n          worst_case_diag70: 1.6444\n          worst_case_diag50: 14.0463\n          note: Wald estimator extremely unstable at low accuracy\n        K5:\n          tau_specific_sign_flip: 0.514\n          all_coef_sign_flip: 0.514\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.4053\n          worst_case_diag70: 2.1036\n          worst_case_diag50: 9.6932\n        K7:\n          tau_specific_sign_flip: 0.523\n          all_coef_sign_flip: 0.523\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.3605\n          worst_case_diag70: 1.8132\n          worst_case_diag50: 8.2204\n      frontdoor:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.836\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1407\n          worst_case_diag70: 0.2604\n          worst_case_diag50: 0.2966\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.967\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1057\n          worst_case_diag70: 0.2066\n          worst_case_diag50: 0.2507\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.993\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0785\n          worst_case_diag70: 0.1646\n          worst_case_diag50: 0.2119\n    conclusion_summary:\n      structural_guarantee: tau_specific_sign_flip = 0% across ALL K for 5/7 topologies\n        (confounding/mediation/collider/mbias/frontdoor)\n      iv_new_finding: IV ~52% tau sign flip (K-invariant) — Wald denominator sign\n        reversal under random C\n      exposure_clarification: Exposure tau_spec_sflip column is all-coef fallback.\n        Actual beta1-specific flip rate = 83.4% (from MVP)\n      worst_case_trend: Decreasing with K for 5/7 topologies (K=3 most conservative).\n        IV catastrophic at low accuracy (WC_d50 up to 14x). Exposure decreasing.\n      mbias_special: Amplification drops to 0% at K>=5\n      rng_fix: Deterministic per-(topo,K,threshold) seeds via SHA-256. Previous values\n        had RNG ordering artifact.\n    runtime_seconds: 20\n    gpu: RTX 5090 cuda:0\n    script: /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py\n- exp_id: plan009_pathological_matrices\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    regression_dichotomy:\n      benign_topologies:\n        list:\n        - confounding\n        - mediation\n        - collider\n        - frontdoor\n        - mbias\n        R2_range: 0.61-0.77\n        primary_predictor: effective_rank\n        secondary_predictors:\n        - spectral_gap\n        - condition_number\n      dangerous_topologies:\n        list:\n        - exposure\n        - iv\n        exposure_R2: 0.11\n        iv_R2: ~0\n        iv_note: regression has no explanatory power — Wald denominator sign reversal\n          is discrete, not predicted by continuous matrix features\n        exposure_note: 'near_perm eps=0.01: 15% catastrophic bias above threshold'\n      global_R2: ~0 (cross-topology aggregation destroys predictive power — different\n        bias mechanisms)\n    risk_tiers:\n      low:\n        topologies:\n        - mbias\n        max_bias: <0.04\n        note: safe even under worst-case pathological C\n      medium:\n        topologies:\n        - confounding\n        - mediation\n        - collider\n        - frontdoor\n        bias_range: 0.1-0.31\n        catastrophic_fraction: 0%\n        R2: 0.70-0.77\n        note: bounded bias, matrix features predictive\n      high:\n        topologies:\n        - exposure\n        - iv\n        note: 'catastrophic regardless of C quality — exposure: structural identification\n          failure; IV: Wald estimator explosion (near_perm eps=0.01 cat=61-73%, rank-deficient\n          bias reaches millions)'\n    most_consistent_predictor: condition_number (significant in 5/5 medium-risk topologies)\n    hypothesis_assessment:\n      H1_predictable_catastrophic: partially — risk tier determined by topology, not\n        C features\n      H2_matrix_features_strong: topology-dependent — 5/7 R²>0.6, exposure/IV fail\n      H3_safety_threshold: not confirmed — boundary is topology-based, not C-feature\n        threshold\n      H4_diagnostic_features: partially — condition_number most consistent, but needs\n        topology-specific criteria\n    iv_filtering:\n      n_filtered: 3000\n      n_total: 28000\n      pct_infinite: 10.7\n      note: non-finite Wald values silently filtered from regression; must note in\n        paper\n    pathological_C_types:\n    - near_permutation (eps=0.01,0.05,0.1,0.2)\n    - rank_deficient\n    - block_diagonal\n    K_values:\n    - 3\n    - 5\n    - 7\n    M_per_config: 1000\n    N_per_sim: 5000000\n    runtime_seconds: 25\n    analysis_report: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md\n    output_files:\n      summary_json: /home/sonny/causal_annot_error_attrib/artifacts/plan009/pathological_bias_summary.json\n      regression_txt: /home/sonny/causal_annot_error_attrib/artifacts/plan009/regression_results.txt\n      analysis_md: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md\n- exp_id: plan007_correction_guidance\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_combos: 210\n    runtime_sec: 2792\n    ppi_grand_mean_bias_red: 93.8%\n    ppi_grand_mean_coverage: 96.8%\n    ppi_win_rate: 95.2% (40/42)\n    mcsimex_grand_mean_bias_red: 20.9%\n    dsl_grand_mean_bias_red: -144.8%\n    naive_plugin_grand_mean_bias_red: -20.0%\n    mla_grand_mean_bias_red: -37.4%\n    fwl_invariance_verified: true\n    fwl_invariance_topologies: confounding, mediation, collider, mbias (0.0% bias_red\n      for naive/mla)\n    dsl_effective_topologies: confounding (49.8%), mediation (70.3%)\n    dsl_failure_topologies: mbias (-768%), iv (-187%), collider (-89%), exposure (-60%),\n      frontdoor (-29%)\n    ppi_weakness: 'mbias+realistic_llm: -25.1% bias_red (but 99% coverage)'\n- exp_id: plan010_annot_sensitivity_toolkit\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tests_passed: 35/35\n    modules: 7\n    topologies: 7\n    correction_methods: 5\n    lines_of_code:\n      __init__.py: 53\n      bias.py: 174\n      asv.py: 119\n      correction.py: 422\n      confusion.py: 129\n      dgp.py: 213\n      utils.py: 95\n      test_core.py: 35 tests\n    example_output:\n      confounding_k3_bias_pct: +10.20%\n      magnitude_asv: 0.967\n      sign_flip_asv: null\n      recommended_with_gold: ppi\n      recommended_without_gold: dsl\n- exp_id: plan006_asv_empirical\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_scenarios: 210\n    configs: 14\n    topologies: 7\n    k_values:\n    - 2\n    - 3\n    - 10\n    models:\n    - llama4\n    - deepseek\n    - qwen3\n    - qwen2.5-7b\n    sign_flips: 0\n    overall_asv_unsafe_pct: 43.8\n    k2_mean_bias_pct: 36.9\n    k3_mean_bias_pct: 65.3\n    k10_mean_bias_pct: 12.2\n    k2_iv_bias_pct: 116.5\n    k3_iv_bias_pct: 252.3\n    k10_iv_bias_pct: 30.3\n    f1_disconnect: civil_comments F1=0.72-0.75 but IV bias 101-131%\n    7b_vs_235b_bias_ratio: 1.24\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T05:50:10.680Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T05:50:10.680Z",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-21T05:50:10.704Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：理论-实证桥梁完全闭合：3 claims 均以完整强度呈现，实证数据覆盖充分且 theory-empirical match 紧凑
核心假设：['API 402 解决，VAST/Civil Comments 获得 frontier 模型(≥235B)标注，消除 model-tier asymmetry', 'PPI++ 在真实 LLM 标注上 bias reduction 与 MC 一致(≥80%)，nondiff assumption 近似成立', 'theory-empirical bias magnitude match 紧凑(MAPE ≤ 15%)，topology ranking 在 K=2,3,10 全部复现', 'Dirichlet subspace 可视化成功说服 reviewer：empirical 0 sign flip 是因 LLM accuracy 落在 diag≥0.7 安全区，理论预测的 sign flip 区域与实际 LLM 数据点无交集', 'ASV 的 sample-dependent N* 和三类型设计(magnitude/significance/sign-flip)被接受为对 E-value 的实质性扩展']
关键指标范围：{'usable_dataset_model_configs': [12, 14], 'theory_empirical_direction_match_pct': [95, 100], 'theory_empirical_magnitude_MAPE_pct': [5, 15], 'ppi_empirical_bias_reduction_pct': [80, 95], 'asv_unsafe_empirical_pct': [45, 60], 'f1_bias_pearson_r': [0.05, 0.2], 'correction_recommendation_accuracy_pct': [85, 95], 'iv_empirical_bias_pct_k3': [200, 300]}
叙事方向：原始 framing 完全成立，三条 claim 均以 full strength 呈现： (1) taxonomy 捕获 K≥3 方向反转(exposure 83%/IV 52% sign flip)和结构保证(5/7 topologies sign_flip=0%)的完整图景； (2) ASV 三类型覆盖不同 DAG，significance_ASV 的 N* phase transition 是核心 actionable 贡献； (3) PPI++ universally reliable(93.8% MC + ≥80% empirical)，DSL topology-limited，naive/MLA Frisch-Waugh 失效。 Headline 无需修改："F1>0.9 的 LLM 在 IV 下仍 >200% bias，12% 场景效应放大无安全阈值。"


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: causal_annot_error_attrib
venue: emnlp-2026
focus: Post-fix re-dream: all 5 structural issues resolved. Related work +5 refs, ASV vs PBA, Brenner footnote, IV subspace appendix, nondiff stress test appendix+limitations.

## paper_framing.md

# Paper Framing — causal_annot_error_attrib

## Target Venue
- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)
- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)
- Tertiary: ICWSM 2027 Round 2 (2026-09-15)

## Title
Multi-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies

## Core Claims (3 条)

1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 7 canonical social-science DAG topologies (confounding, exposure, mediation, collider, M-bias, instrument, front-door).

2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of annotation error amplification needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Three complementary ASV types — magnitude (E-value-style robustness reporting, all topologies), significance (hypothesis testing filter, effective for attenuating topologies), and sign-flip (direction reversal warning, primarily exposure DAG) — because no single sensitivity metric suffices across all causal designs. The choice of appropriate ASV type is itself topology-dependent, reinforcing Claim 1. ASVs reveal a striking sensitivity ranking: IV estimates are maximally fragile (any annotation error exceeds threshold), while M-bias is immune (misclassification actually reduces spurious associations). Unlike E-values, ASVs incorporate study precision (sample-dependent), providing actionable guidance: for a given τ and σ, the critical sample size N* is analytically computable. Formal proofs (envelope monotonicity + sharpness) for 3 priority topologies; MC-validated for all 7.

3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI++, MLA, MC-SIMEX, naive plug-in). Key findings from 210-configuration MC validation (7 topo × 6 C × 5 methods × 1000 sims): (a) Frisch-Waugh theorem makes naive_plugin/MLA fundamentally ineffective for T-coefficient bias in 4/7 topologies (bias reduction = 0.0%, exact); (b) DSL is topology-limited — effective only for confounding (50%) and mediation (70%), catastrophically harmful elsewhere (mbias -768%, IV -187%); (c) PPI++ is the only universally reliable method (93.8% grand mean bias reduction, 96.8% coverage) but requires gold-standard labels; (d) correction method effectiveness is itself topology-dependent, reinforcing Claim 1. Dependence-aware multi-LLM correction remains an open problem.

## Story Spine

- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31–50% of downstream conclusions are already incorrect — critically, even annotators with F1 > 0.93 produce > 50% error risk in downstream causal estimates. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable. The field's reliance on classification F1 as a proxy for downstream validity is fundamentally broken; our framework provides the missing link from annotation quality metrics to causal estimate reliability.

- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.

- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.

- **Headline result template**: "Across 7 DAG topologies with K=3, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. ASVs reveal a striking sensitivity spectrum: IV estimates are maximally fragile (any annotation error exceeds robustness thresholds), while M-bias associations are immune (misclassification reduces spurious bias). Empirical validation on 3 CSS tasks (K=2, 3, 10) annotated by 4 LLMs confirms the theoretical predictions: IV bias ranges from 30% at K=10 to 252% at K=3 across annotation settings, F1 does not predict downstream safety (F1=0.72 but IV bias>100%), and 55.4% of HumAID scenarios are ASV-unsafe, requiring correction or sensitivity reporting."

## Core Insight (Lead Finding) — DUAL VERSION, gate on plan_001

### Version A (≥1 topology shows direction reversal under K≥3 non-differential exposure misclassification)
The binary guarantee that "non-differential exposure misclassification biases toward the null" (Bross 1954) breaks in the multi-class case. For specific confusion matrix structures in specific DAG topologies, K≥3 non-differential error can amplify or reverse effect estimates. Brenner (1993) identified this possibility for polytomous confounder misclassification ("bias can go in either direction"); we provide the first systematic characterization across 7 DAG topologies with exact conditions for each {C structure × topology} cell. Furthermore, binarizing a K-class variable to "escape" into the binary regime is itself hazardous — collapsing introduces new, direction-unpredictable bias (MVP evidence: Δ up to 0.103).

### Version B (no direction reversal found across topologies)
Multi-class annotation error is structurally irreducible to the binary case: the downstream bias magnitude depends on the full K×K confusion matrix in ways that binary sensitivity/specificity cannot predict, and binarizing a K-class variable introduces new bias (MVP evidence: Δ up to 0.103). While non-differential error preserves bias direction across tested topologies (a useful practitioners' guarantee), the magnitude varies dramatically with confusion matrix structure (0.13–0.30 in confounding DAG alone), and this variation is topology-dependent. ASVs provide the missing robustness measure for this quantitative — not directional — uncertainty.

**Gate**: RESOLVED → Version A. Two topologies show τ-specific direction reversal: exposure (~83-100% sign flip) and IV (~52% sign flip, Wald denominator mechanism). 5/7 topologies have structural guarantee τ_sign_flip=0% across K={3,5,7}. See D003, D004, D010.

## MVP Evidence

**Confounding DAG + K=3** (confounder misclassification):
- Theoretical bias expressions match MC perfectly (6/6 structures within 95% CI) — framework validated
- Binary collapse ≠ multi-class: Δ up to 0.103 (near-permutation C), proving K=3 retains more confounding control than binarization
- 100k random C search: confounding DAG bias is monotonically toward OVB — this topology is "well-behaved" (predictable direction)
- NOTE: Confounding DAG tests residual confounding, NOT bias-toward-null (Bross 1954). Criterion 2 (away-from-null bias) holds for binary too in this topology. See M001.

**Exposure DAG K=3** (exposure misclassification — D002/D004 CONFIRMED):
- 100k random C: 85% violate bias-toward-null, 83.4% sign reversal, 14.1% amplification
- K=2 control: 6/6 toward null (binary guarantee holds)
- Worst case: β₁=1.0 → γ̂₁=-0.84 (sign reversal, 0.84× magnitude); β₂=-0.5 → γ̂₂=-1.41 (2.83× amplification)
- Mechanism: near-permutation C causes label swap → effect direction flips (structurally impossible in K=2)
- **Two-DAG contrast**: confounding (monotonic, predictable) vs exposure (unpredictable, topology-dependent) — validates core claim

**Dirichlet subspace analysis** (practical relevance validation):
- diag≥0.5: 32.5% violation, 21.6% sign reversal, 11.3% amplification
- diag≥0.7 (typical LLM accuracy): **13.7% violation**, 2.1% sign reversal, **11.7% amplification**
- diag≥0.9 (high-accuracy LLM): **11.9% violation**, 0% sign reversal, **11.9% amplification**
- Key pattern: sign reversal vanishes at high accuracy, but **amplification persists at ~12% regardless of accuracy**
- Implication: even 90%+ accuracy LLMs face non-trivial effect amplification risk — no "safe accuracy threshold" exists

**IV Dirichlet subspace analysis** (Dream feedback, 2026-05-21):
- Full: 100% violation, 51.7% sign flip, 48.3% amplification
- diag≥0.5: 100% violation, **0% sign flip**, 100% amplification, worst 28.6×
- diag≥0.7: 100% violation, 0% sign flip, 100% amplification, worst 2.4×
- diag≥0.9: 100% violation, 0% sign flip, 100% amplification, worst 1.2×
- Key contrast with exposure: IV sign flip vanishes at diag≥0.5 (exposure persists at 2.1% at diag≥0.7), but IV amplification is **universal** (100% at all thresholds, vs exposure 11.7% at diag≥0.7)
- Mechanism: Wald denominator monotonically contracts; diagonal dominance prevents zero-crossing (no sign flip) but not contraction (amplification)

## Venue Fit Risks

- **AAAI**: Broad AI audience — emphasize general methodology for "automated annotation measurement error," not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.
- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.
- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.

## Anticipated Reviewer Concerns & Planned Responses

1. **"Trivial extension of binary to multi-class"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 7 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]

2. **"Lee & Wood-Doughty (2024) already did categorical"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 7 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]

3. **"Why these 7 DAG topologies?"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: exposure (treatment), confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]

4. **"K≥5 expressions aren't actionable"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]

5. **"ASV sharpness only proved for 3 topologies"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]

6. **"Correlated multi-LLM errors?"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]

7. **"Empirical validation scope"** → 3 CSS tasks (HumAID K=10, VAST K=3, Civil Comments K=2) × 4 LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat, Qwen2.5-7B) × 7 topologies = 14 configs. D016 confirms: topology ranking matches theory across all K values; IV bias co-varies with annotation setting (K=3 IV bias 252% vs K=10 30%, confounded with dataset/model differences); 7B vs 235B bias ratio 1.24 (model scale not dominant). 0 sign flips across all 98 scenarios. Note: VAST/Civil Comments use 7B local model (API 402 blocker), creating a model-tier asymmetry acknowledged in Limitations. [Experiments: plan_003, plan_006]


## experiment_plan (with registry status)

- id: plan_001
  claim: 1
  description: Derive and MC-validate bias expressions for 6 DAG topologies with K=3
  priority: P0
  gpu_budget_hours: 0
  deps: []
  registry_id: plan001_dag_taxonomy
  details: 'For each topology (confounding, mediation, collider, M-bias, instrument,
    front-door): derive closed-form K=3 bias expression, validate with MC (1000 reps
    × N=10000, 6 confusion matrix structures including near-permutation extreme).
    Key question: which topologies show direction reversal under non-differential
    error? Confounding already validated in MVP (no reversal, monotonic toward OVB).

    '
  status: DONE
  conclusion: success
  metrics:
    collider:
      all_coef:
        violation: 1
        sign_flip: 0.688
        amplification: 1
      tau_specific:
        violation: 1
        sign_flip: 0
        amplification: 1
      misclass_amplifies_rate: 0
      small_tau_0.05:
        tau_I: 0.015733
        tau_violation: 0.96
        tau_sign_flip: 0
        tau_amplification: 0.992
      small_tau_0.1:
        tau_I: 0.06118
        tau_violation: 0.974
        tau_sign_flip: 0
        tau_amplification: 0.995
    mbias:
      all_coef:
        violation: 1
        sign_flip: 0.651
        amplification: 0.112
      tau_specific:
        violation: 0.532
        sign_flip: 0
        amplification: 0.104
      misclass_amplifies_rate: 0.292
      small_tau_0.05:
        tau_I: 0.057669
        tau_violation: 0.532
        tau_sign_flip: 0
        tau_amplification: 0.104
      small_tau_0.1:
        tau_I: 0.107669
        tau_violation: 0.532
        tau_sign_flip: 0
        tau_amplification: 0.104
    mediation_mixed:
      all_coef:
        violation: 1
        sign_flip: 0.835
        amplification: 1
      tau_specific:
        violation: 1
        sign_flip: 0
        amplification: 1
      misclass_amplifies_rate: 1
      small_tau_0.05:
        tau_violation: 1
        tau_sign_flip: 0
        tau_amplification: 1
      small_tau_0.1:
        tau_violation: 1
        tau_sign_flip: 0
        tau_amplification: 1
    mediation_same:
      all_coef:
        violation: 1
        sign_flip: 0.666
        amplification: 1
      tau_specific:
        violation: 1
        sign_flip: 0
        amplification: 1
      misclass_amplifies_rate: 1
      small_tau_0.05:
        tau_violation: 1
        tau_sign_flip: 0
        tau_amplification: 1
      small_tau_0.1:
        tau_violation: 1
        tau_sign_flip: 0
        tau_amplification: 1
    frontdoor_mixed:
      all_coef:
        violation: 1
        sign_flip: 0.998
        amplification: 1
      tau_specific:
        violation: 1
        sign_flip: 0
        amplification: 1
      misclass_amplifies_rate: 1
      small_tau_0.05:
        tau_I: 0.050177
        lambda_U: 0.1
        tau_violation: 1
        tau_sign_flip: 0
        tau_amplification: 1
      small_tau_0.1:
        tau_I: 0.100169
        lambda_U: 0.2
        tau_violation: 1
        tau_sign_flip: 0
        tau_amplification: 1
    frontdoor_same:
      all_coef:
        violation: 1
        sign_flip: 1
        amplification: 1
      tau_specific:
        violation: 0.999
        sign_flip: 0
        amplification: 1
      misclass_amplifies_rate: 0.9997
      small_tau_0.05:
        tau_I: 0.050177
        lambda_U: 0.1
        tau_violation: 0.999
        tau_sign_flip: 0
        tau_amplification: 1
      small_tau_0.1:
        tau_I: 0.100169
        lambda_U: 0.2
        tau_violation: 0.999
        tau_sign_flip: 0
        tau_amplification: 1
    iv_note: 'IV metrics not computed in plan_001 (only 6 fixed C structures tested,
      no dedicated IV tau_specific analysis). First measured in plan_002: 52% tau_specific_sign_flip
      from 100k random C (Wald denominator sign reversal). See plan002_k57_extension
      for full IV results.'
- id: plan_002
  claim: 1
  description: Extend bias expressions to K=5,7 — matrix notation + interpretability
    tools
  priority: P1
  gpu_budget_hours: 2
  deps:
  - plan_001
  registry_id: plan002_k57_extension
  details: 'Matrix-form expressions for general K. Three interpretability tools: (a)
    eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar
    bounds collapsing matrix to conservative scalar, (c) diagnostic visualizations
    mapping confusion matrix regions to bias magnitude. Validate on confounding +
    mediation + collider DAGs with K=5,7.

    '
  status: DONE
  conclusion: success
  metrics:
    cross_k_comparison_7topo:
      confounding:
        K3:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.993
          violation: 1
          amplification: 1
          worst_case_diag90: 0.1614
          worst_case_diag70: 0.2744
          worst_case_diag50: 0.2993
        K5:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 1
          violation: 1
          amplification: 1
          worst_case_diag90: 0.1107
          worst_case_diag70: 0.2156
          worst_case_diag50: 0.2462
        K7:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 1
          violation: 1
          amplification: 1
          worst_case_diag90: 0.0933
          worst_case_diag70: 0.1859
          worst_case_diag50: 0.2264
      mediation:
        K3:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.838
          violation: 1
          amplification: 1
          worst_case_diag90: 0.1223
          worst_case_diag70: 0.251
          worst_case_diag50: 0.3032
        K5:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.966
          violation: 1
          amplification: 1
          worst_case_diag90: 0.0867
          worst_case_diag70: 0.1832
          worst_case_diag50: 0.2396
        K7:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 1
          violation: 1
          amplification: 1
          worst_case_diag90: 0.0607
          worst_case_diag70: 0.1421
          worst_case_diag50: 0.1879
      collider:
        K3:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.666
          violation: 1
          amplification: 1
          worst_case_diag90: 0.0503
          worst_case_diag70: 0.1064
          worst_case_diag50: 0.1256
        K5:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.955
          violation: 1
          amplification: 1
          worst_case_diag90: 0.0477
          worst_case_diag70: 0.1087
          worst_case_diag50: 0.1306
        K7:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.992
          violation: 1
          amplification: 1
          worst_case_diag90: 0.0352
          worst_case_diag70: 0.0826
          worst_case_diag50: 0.1131
      exposure:
        K3:
          tau_specific_sign_flip: N/A (all-coef fallback; MVP beta1 flip=83.4%)
          all_coef_sign_flip: 0.99
          violation: 1
          amplification: 0.999
          worst_case_diag90: 0.2726
          worst_case_diag70: 0.7092
          worst_case_diag50: 1.1438
        K5:
          tau_specific_sign_flip: N/A (all-coef fallback)
          all_coef_sign_flip: 1
          violation: 1
          amplification: 0.998
          worst_case_diag90: 0.2097
          worst_case_diag70: 0.5782
          worst_case_diag50: 0.8784
        K7:
          tau_specific_sign_flip: N/A (all-coef fallback)
          all_coef_sign_flip: 1
          violation: 1
          amplification: 0.999
          worst_case_diag90: 0.1853
          worst_case_diag70: 0.4913
          worst_case_diag50: 0.7441
      mbias:
        K3:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.667
          violation: 0.584
          amplification: 0.089
          worst_case_diag90: 0.0106
          worst_case_diag70: 0.0226
          worst_case_diag50: 0.0287
        K5:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.954
          violation: 1
          amplification: 0
          worst_case_diag90: 0.0154
          worst_case_diag70: 0.0374
          worst_case_diag50: 0.0487
        K7:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.992
          violation: 1
          amplification: 0
          worst_case_diag90: 0.0133
          worst_case_diag70: 0.0319
          worst_case_diag50: 0.0449
      iv:
        K3:
          tau_specific_sign_flip: 0.526
          all_coef_sign_flip: 0.526
          violation: 1
          amplification: 1
          worst_case_diag90: 0.2993
          worst_case_diag70: 1.6444
          worst_case_diag50: 14.0463
          note: Wald estimator extremely unstable at low accuracy
        K5:
          tau_specific_sign_flip: 0.514
          all_coef_sign_flip: 0.514
          violation: 1
          amplification: 1
          worst_case_diag90: 0.4053
          worst_case_diag70: 2.1036
          worst_case_diag50: 9.6932
        K7:
          tau_specific_sign_flip: 0.523
          all_coef_sign_flip: 0.523
          violation: 1
          amplification: 1
          worst_case_diag90: 0.3605
          worst_case_diag70: 1.8132
          worst_case_diag50: 8.2204
      frontdoor:
        K3:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.836
          violation: 1
          amplification: 1
          worst_case_diag90: 0.1407
          worst_case_diag70: 0.2604
          worst_case_diag50: 0.2966
        K5:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.967
          violation: 1
          amplification: 1
          worst_case_diag90: 0.1057
          worst_case_diag70: 0.2066
          worst_case_diag50: 0.2507
        K7:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.993
          violation: 1
          amplification: 1
          worst_case_diag90: 0.0785
          worst_case_diag70: 0.1646
          worst_case_diag50: 0.2119
    conclusion_summary:
      structural_guarantee: tau_specific_sign_flip = 0% across ALL K for 5/7 topologies
        (confounding/mediation/collider/mbias/frontdoor)
      iv_new_finding: IV ~52% tau sign flip (K-invariant) — Wald denominator sign
        reversal under random C
      exposure_clarification: Exposure tau_spec_sflip column is all-coef fallback.
        Actual beta1-specific flip rate = 83.4% (from MVP)
      worst_case_trend: Decreasing with K for 5/7 topologies (K=3 most conservative).
        IV catastrophic at low accuracy (WC_d50 up to 14x). Exposure decreasing.
      mbias_special: Amplification drops to 0% at K>=5
      rng_fix: Deterministic per-(topo,K,threshold) seeds via SHA-256. Previous values
        had RNG ordering artifact.
    runtime_seconds: 20
    gpu: RTX 5090 cuda:0
    script: /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py
- id: plan_003
  claim: 1
  description: 'Empirical confusion matrices: 3 LLMs × 3 CSS tasks vs gold-standard'
  priority: P0
  gpu_budget_hours: 0
  api_cost_estimate: $300-550
  deps: []
  registry_id: plan003_empirical_confusion_matrices
  details: 'Tasks: crisis event classification (K=10, HumAID), stance detection (K=3,
    VAST), toxicity (K=2, as special case / consistency check, Civil Comments). Models:
    Llama 4 Maverick (Together.ai/OpenRouter), Qwen 3 235B (OpenRouter), DeepSeek
    Chat V3 (DeepSeek API). ~30K annotations per model × 3 datasets × 3 prompt variants.
    Output: empirical confusion matrices, inter-model correlation analysis, downstream
    regression bias vs gold-standard baseline. Inter-model error correlation analysis:
    for each of 3 model pairs, compute error agreement rate, conditional error correlation
    (given true label), and Cohen''s kappa on errors. Quantify correlated-error structure
    to inform whether independent-error assumptions in correction methods hold.

    '
  status: DONE
  conclusion: failed
  metrics:
    status_detail: PAUSED - API 402 Payment Required (OPENROUTER_API_KEY)
    api_endpoint: http://47.94.22.126/v1/chat/completions
    data_dir: results/
    humaid_recount_20260520T2312:
      deepseek_zero-shot:
        total: 1500
        pred_valid: 1500
        errors: 0
        status: OK
      deepseek_few-shot-3:
        total: 1500
        pred_valid: 1345
        errors: 155
        error_type: parsing
        status: WARN
      deepseek_few-shot-5:
        total: 1500
        pred_valid: 1237
        errors: 263
        error_type: parsing
        status: WARN
      llama4_zero-shot:
        total: 1500
        pred_valid: 1500
        errors: 0
        status: OK
      llama4_few-shot-3:
        total: 1500
        pred_valid: 1498
        errors: 2
        status: OK
      llama4_few-shot-5:
        total: 1500
        pred_valid: 1471
        errors: 29
        status: WARN
      qwen3_zero-shot:
        total: 1500
        pred_valid: 1500
        errors: 0
        status: OK
      qwen3_few-shot-3:
        total: 1500
        pred_valid: 1423
        errors: 77
        error_type: '402'
        status: WARN
      qwen3_few-shot-5:
        total: 1500
        pred_valid: 0
        errors: 1500
        error_type: '402'
        status: FAIL
    humaid_summary: 4 OK (≥1498) + 4 WARN (1237-1471) + 1 FAIL (qwen3_fs5 all 402)
    humaid_usable: 8/9 files have valid data
    data_fields:
      true_label: gold_label
      pred_label: pred_label
    note: deepseek errors are parsing/format, NOT 402. Only qwen3 errors are 402.
- id: plan_008
  claim: 1
  description: 'Binarization collapse analysis: K→2 folding bias across all 6 topologies'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: plan008_binarization_collapse
  details: 'For each of 6 topologies with K=3,5,7: collapse to binary, compare bias
    from full multi-class expression vs binarized expression. Demonstrate that binarization
    is not a safe shortcut — can amplify or reverse bias. MVP showed Δ up to 0.089
    for confounding DAG K=3.

    '
  status: DONE
  conclusion: success
  metrics:
    confounding:
      D_mean: 0.0253
      D_med: 0.0182
      D_P95: 0.0733
      D_max: 0.2213
      frac_gt_001: 0.686
      frac_gt_005: 0.138
      sign_flip: 0
    mediation:
      D_mean: 0.0446
      D_med: 0.0355
      D_P95: 0.1179
      D_max: 0.252
      frac_gt_001: 0.835
      frac_gt_005: 0.36
      sign_flip: 0
    collider:
      D_mean: 0.0169
      D_med: 0.0125
      D_P95: 0.0472
      D_max: 0.1069
      frac_gt_001: 0.572
      frac_gt_005: 0.039
      sign_flip: 0
    M-bias:
      D_mean: 0.0063
      D_med: 0.0054
      D_P95: 0.0147
      D_max: 0.0328
      frac_gt_001: 0.181
      frac_gt_005: 0
      sign_flip: 0
    exposure:
      D_mean: 0.5164
      D_med: 0.506
      D_P95: 0.8453
      D_max: 1.3876
      frac_gt_001: 1
      frac_gt_005: 0.999
      sign_flip: 0.14
    IV:
      D_mean: 0.926
      D_med: 0.9394
      D_P95: 1.3426
      D_max: 2.0809
      frac_gt_001: 1
      frac_gt_005: 1
      sign_flip: 0.175
- id: plan_004
  claim: 2
  description: 'ASV framework: formal proofs for confounding, mediation, collider'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: plan004_asv_framework
  details: 'Derive ASV expressions for 3 priority topologies. Formal proofs of: (a)
    monotonicity (ASV increases with δ amplification), (b) sharpness (bound is achievable
    for some confusion matrix). MC validation: coverage at 90%, 95%, 99% levels across
    1000 scenarios. Additionally report Type I/II error rates: rejection rate under
    null (Type I) and power under alternative, before and after ASV-informed correction.

    '
  status: DONE
  conclusion: success
  metrics:
    v2_sign_flip_filter: ✅ effective (Type I=0%, power=100%)
    v3_envelope_monotonicity: ✅ solved (0 violations)
    v3_magnitude_reporting: ✅ informative values for all topologies
    v3_magnitude_filter: ❌ rejected (scale-dependent, not viable as binary test)
    v3_fixed_signif_filter: ✅ Type I=0% all topologies, power=100% for τ≥0.1
    v3_significance_filter:
      confounding_tau005:
        type_i: 0
        power: 1
      confounding_tau010:
        type_i: 0
        power: 1
      mediation_tau005:
        type_i: 0
        power: 0
      mediation_tau010:
        type_i: 0
        power: 1
      collider_tau005:
        type_i: 0
        power: 0
      collider_tau010:
        type_i: 0
        power: 1
      note: τ=0.05 mediation/collider power=0% is correct — attenuating topologies
        are fragile at small effects
    v3_fixed_status: complete — significance filter validated
    v3_envelope_violations: 0
    v3_magnitude_asv_tau0.5_range: 0.076-0.487
    v3_magnitude_asv_tau0.05_range: 0.008-0.047
    v3_magnitude_asv_tau0.1_range: 0.014-0.093
    v3_coverage_tau0.05: 100.0%
    v3_coverage_tau0.1: 100.0%
    n_sensitivity_mediation_tau005:
      topology: mediation
      tau: 0.05
      C0: sym_mild
      mc_reps: 500
      N_1000:
        naive_power: 0.89
        asv_power: 0
        median_se: 0.070025
        median_signif_asv: 0
      N_2000:
        naive_power: 0.998
        asv_power: 0
        median_se: 0.049649
        median_signif_asv: 0
      N_5000:
        naive_power: 1
        asv_power: 0
        median_se: 0.031301
        median_signif_asv: 0
      N_10000:
        naive_power: 1
        asv_power: 1
        median_se: 0.022152
        median_signif_asv: null
      N_20000:
        naive_power: 1
        asv_power: 1
        median_se: 0.01566
        median_signif_asv: null
      N_50000:
        naive_power: 1
        asv_power: 1
        median_se: 0.009903
        median_signif_asv: null
      recovery_N: 10000
      interpretation: 'Sharp phase transition at N~6000-10000. Below: 1.96*SE > tau=0.05
        so signif_ASV=0 (ASV kills all rejections). Above: 1.96*SE < tau=0.05 so signif_ASV=None
        (infinite robustness), ASV passes all.'
- id: plan_005
  claim: 2
  description: ASV MC validation for M-bias, instrument, front-door topologies
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_004
  registry_id: plan005_asv_extended
  details: 'ASV expressions + MC validation of monotonicity and coverage. Sharpness
    stated as conjectures supported by numerical evidence. If any topology fails monotonicity
    under MC, flag and investigate.

    '
  status: DONE
  conclusion: success
  metrics:
    envelope_violations:
      mbias: 0
      iv: 0
      frontdoor: 0
    plim_at_identity:
      mbias: 0.5128
      iv: 0.6598
      frontdoor: 0.4998
    asv_tau05:
      mbias:
        sign_flip: null
        magnitude_10pct: null
      iv:
        sign_flip_range: 1.1-6.7
        magnitude_10pct_range: 0.101-0.607
      frontdoor:
        sign_flip: null
        magnitude_10pct_range: 0.064-0.387
    mc_coverage:
      mbias_tau005:
        plim_acc: 1
        bias_bounded: 1
      mbias_tau01:
        plim_acc: 1
        bias_bounded: 1
      iv_tau005:
        plim_acc: 1
        bias_bounded: 1
      iv_tau01:
        plim_acc: 1
        bias_bounded: 1
      frontdoor_tau005:
        plim_acc: 1
        bias_bounded: 1
      frontdoor_tau01:
        plim_acc: 1
        bias_bounded: 1
    v_fixed_signif_filter:
      mbias:
        type_i: 0
        power_tau005: 95.8-99.2%
        power_tau01: 100%
      iv:
        type_i: 0
        power_tau005: 0%
        power_tau01: 0%
        note: correct — Wald estimator immediately fragile, signif_ASV≈0 blocks all
          rejections
      frontdoor:
        type_i: 0
        power_tau005: 100%
        power_tau01: 100%
    fixes_applied:
    - 'C1: compute_signif_asv_fast added'
    - 'C2: magnitude ASV tau≈0 returns 0.0'
    - 'W1: IV tau_true=plim_iv(I)=0.6598'
    - 'W2: M-bias tau_true=plim_mb(I)=0.5128'
    fixed_script: /home/sonny/causal_annot_error_attrib/plan_005_asv_extended_fixed.py
    runtime_seconds: 46.2
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
    Report Type I/II error rates: rejection rate under null (Type I) and power under
    alternative, before and after ASV-informed correction, across all task × model
    combinations. F1 vs downstream causal bias analysis: for each model × task, compute
    classification F1 and plot against |downstream bias|. Demonstrate that high F1
    does not guarantee low downstream bias (Baumann 2025: F1>0.93 still >50% error
    risk). This bridges the gap between annotation quality metrics and causal estimate
    reliability.

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
    (DSL / PPI / MLA / MC-SIMEX / naive plug-in / "no existing method adequate").
    MC validation: recommended method produces least bias in ≥90% of scenarios. Empirical
    validation on plan_003 data. Characterize regimes where no existing method suffices
    (correlated errors, differential multi-class, etc.) — identify as open problems.

    '
  status: planned
- id: plan_009
  claim: 1
  description: Pathological confusion matrix analysis (near-permutation, rank-deficient)
  priority: P2
  gpu_budget_hours: 1
  deps:
  - plan_001
  registry_id: plan009_pathological_matrices
  details: 'Extreme C structures: near-permutation, rank-deficient, block-diagonal.
    Characterize when bias becomes catastrophic across topologies. Identify structural
    conditions (spectral gap, diagonal dominance ratio) that predict bias severity
    — candidate features for practitioners.

    '
  status: DONE
  conclusion: success
  metrics:
    regression_dichotomy:
      benign_topologies:
        list:
        - confounding
        - mediation
        - collider
        - frontdoor
        - mbias
        R2_range: 0.61-0.77
        primary_predictor: effective_rank
        secondary_predictors:
        - spectral_gap
        - condition_number
      dangerous_topologies:
        list:
        - exposure
        - iv
        exposure_R2: 0.11
        iv_R2: ~0
        iv_note: regression has no explanatory power — Wald denominator sign reversal
          is discrete, not predicted by continuous matrix features
        exposure_note: 'near_perm eps=0.01: 15% catastrophic bias above threshold'
      global_R2: ~0 (cross-topology aggregation destroys predictive power — different
        bias mechanisms)
    risk_tiers:
      low:
        topologies:
        - mbias
        max_bias: <0.04
        note: safe even under worst-case pathological C
      medium:
        topologies:
        - confounding
        - mediation
        - collider
        - frontdoor
        bias_range: 0.1-0.31
        catastrophic_fraction: 0%
        R2: 0.70-0.77
        note: bounded bias, matrix features predictive
      high:
        topologies:
        - exposure
        - iv
        note: 'catastrophic regardless of C quality — exposure: structural identification
          failure; IV: Wald estimator explosion (near_perm eps=0.01 cat=61-73%, rank-deficient
          bias reaches millions)'
    most_consistent_predictor: condition_number (significant in 5/5 medium-risk topologies)
    hypothesis_assessment:
      H1_predictable_catastrophic: partially — risk tier determined by topology, not
        C features
      H2_matrix_features_strong: topology-dependent — 5/7 R²>0.6, exposure/IV fail
      H3_safety_threshold: not confirmed — boundary is topology-based, not C-feature
        threshold
      H4_diagnostic_features: partially — condition_number most consistent, but needs
        topology-specific criteria
    iv_filtering:
      n_filtered: 3000
      n_total: 28000
      pct_infinite: 10.7
      note: non-finite Wald values silently filtered from regression; must note in
        paper
    pathological_C_types:
    - near_permutation (eps=0.01,0.05,0.1,0.2)
    - rank_deficient
    - block_diagonal
    K_values:
    - 3
    - 5
    - 7
    M_per_config: 1000
    N_per_sim: 5000000
    runtime_seconds: 25
    analysis_report: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md
    output_files:
      summary_json: /home/sonny/causal_annot_error_attrib/artifacts/plan009/pathological_bias_summary.json
      regression_txt: /home/sonny/causal_annot_error_attrib/artifacts/plan009/regression_results.txt
      analysis_md: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md
- id: plan_010
  claim: 1
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
- exp_id: mvp_exposure_dirichlet_subspace
  name: ''
  status: DONE
  conclusion: success
  metrics:
    full_space_violation: 0.849
    full_space_sign_rev: 0.833
    full_space_amplif: 0.275
    diag50_violation: 0.325
    diag50_sign_rev: 0.216
    diag50_amplif: 0.113
    diag70_violation: 0.137
    diag70_sign_rev: 0.021
    diag70_amplif: 0.117
    diag90_violation: 0.119
    diag90_sign_rev: 0
    diag90_amplif: 0.119
    samples_per_subspace: 50000
    assessment: ALL subspaces STRONG (>10%)
- exp_id: plan001_dag_taxonomy
  name: ''
  status: DONE
  conclusion: success
  metrics:
    collider:
      all_coef:
        violation: 1
        sign_flip: 0.688
        amplification: 1
      tau_specific:
        violation: 1
        sign_flip: 0
        amplification: 1
      misclass_amplifies_rate: 0
      small_tau_0.05:
        tau_I: 0.015733
        tau_violation: 0.96
        tau_sign_flip: 0
        tau_amplification: 0.992
      small_tau_0.1:
        tau_I: 0.06118
        tau_violation: 0.974
        tau_sign_flip: 0
        tau_amplification: 0.995
    mbias:
      all_coef:
        violation: 1
        sign_flip: 0.651
        amplification: 0.112
      tau_specific:
        violation: 0.532
        sign_flip: 0
        amplification: 0.104
      misclass_amplifies_rate: 0.292
      small_tau_0.05:
        tau_I: 0.057669
        tau_violation: 0.532
        tau_sign_flip: 0
        tau_amplification: 0.104
      small_tau_0.1:
        tau_I: 0.107669
        tau_violation: 0.532
        tau_sign_flip: 0
        tau_amplification: 0.104
    mediation_mixed:
      all_coef:
        violation: 1
        sign_flip: 0.835
        amplification: 1
      tau_specific:
        violation: 1
        sign_flip: 0
        amplification: 1
      misclass_amplifies_rate: 1
      small_tau_0.05:
        tau_violation: 1
        tau_sign_flip: 0
        tau_amplification: 1
      small_tau_0.1:
        tau_violation: 1
        tau_sign_flip: 0
        tau_amplification: 1
    mediation_same:
      all_coef:
        violation: 1
        sign_flip: 0.666
        amplification: 1
      tau_specific:
        violation: 1
        sign_flip: 0
        amplification: 1
      misclass_amplifies_rate: 1
      small_tau_0.05:
        tau_violation: 1
        tau_sign_flip: 0
        tau_amplification: 1
      small_tau_0.1:
        tau_violation: 1
        tau_sign_flip: 0
        tau_amplification: 1
    frontdoor_mixed:
      all_coef:
        violation: 1
        sign_flip: 0.998
        amplification: 1
      tau_specific:
        violation: 1
        sign_flip: 0
        amplification: 1
      misclass_amplifies_rate: 1
      small_tau_0.05:
        tau_I: 0.050177
        lambda_U: 0.1
        tau_violation: 1
        tau_sign_flip: 0
        tau_amplification: 1
      small_tau_0.1:
        tau_I: 0.100169
        lambda_U: 0.2
        tau_violation: 1
        tau_sign_flip: 0
        tau_amplification: 1
    frontdoor_same:
      all_coef:
        violation: 1
        sign_flip: 1
        amplification: 1
      tau_specific:
        violation: 0.999
        sign_flip: 0
        amplification: 1
      misclass_amplifies_rate: 0.9997
      small_tau_0.05:
        tau_I: 0.050177
        lambda_U: 0.1
        tau_violation: 0.999
        tau_sign_flip: 0
        tau_amplification: 1
      small_tau_0.1:
        tau_I: 0.100169
        lambda_U: 0.2
        tau_violation: 0.999
        tau_sign_flip: 0
        tau_amplification: 1
    iv_note: 'IV metrics not computed in plan_001 (only 6 fixed C structures tested,
      no dedicated IV tau_specific analysis). First measured in plan_002: 52% tau_specific_sign_flip
      from 100k random C (Wald denominator sign reversal). See plan002_k57_extension
      for full IV results.'
- exp_id: plan003_empirical_confusion_matrices
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    status_detail: PAUSED - API 402 Payment Required (OPENROUTER_API_KEY)
    api_endpoint: http://47.94.22.126/v1/chat/completions
    data_dir: results/
    humaid_recount_20260520T2312:
      deepseek_zero-shot:
        total: 1500
        pred_valid: 1500
        errors: 0
        status: OK
      deepseek_few-shot-3:
        total: 1500
        pred_valid: 1345
        errors: 155
        error_type: parsing
        status: WARN
      deepseek_few-shot-5:
        total: 1500
        pred_valid: 1237
        errors: 263
        error_type: parsing
        status: WARN
      llama4_zero-shot:
        total: 1500
        pred_valid: 1500
        errors: 0
        status: OK
      llama4_few-shot-3:
        total: 1500
        pred_valid: 1498
        errors: 2
        status: OK
      llama4_few-shot-5:
        total: 1500
        pred_valid: 1471
        errors: 29
        status: WARN
      qwen3_zero-shot:
        total: 1500
        pred_valid: 1500
        errors: 0
        status: OK
      qwen3_few-shot-3:
        total: 1500
        pred_valid: 1423
        errors: 77
        error_type: '402'
        status: WARN
      qwen3_few-shot-5:
        total: 1500
        pred_valid: 0
        errors: 1500
        error_type: '402'
        status: FAIL
    humaid_summary: 4 OK (≥1498) + 4 WARN (1237-1471) + 1 FAIL (qwen3_fs5 all 402)
    humaid_usable: 8/9 files have valid data
    data_fields:
      true_label: gold_label
      pred_label: pred_label
    note: deepseek errors are parsing/format, NOT 402. Only qwen3 errors are 402.
- exp_id: plan004_asv_framework
  name: ''
  status: DONE
  conclusion: success
  metrics:
    v2_sign_flip_filter: ✅ effective (Type I=0%, power=100%)
    v3_envelope_monotonicity: ✅ solved (0 violations)
    v3_magnitude_reporting: ✅ informative values for all topologies
    v3_magnitude_filter: ❌ rejected (scale-dependent, not viable as binary test)
    v3_fixed_signif_filter: ✅ Type I=0% all topologies, power=100% for τ≥0.1
    v3_significance_filter:
      confounding_tau005:
        type_i: 0
        power: 1
      confounding_tau010:
        type_i: 0
        power: 1
      mediation_tau005:
        type_i: 0
        power: 0
      mediation_tau010:
        type_i: 0
        power: 1
      collider_tau005:
        type_i: 0
        power: 0
      collider_tau010:
        type_i: 0
        power: 1
      note: τ=0.05 mediation/collider power=0% is correct — attenuating topologies
        are fragile at small effects
    v3_fixed_status: complete — significance filter validated
    v3_envelope_violations: 0
    v3_magnitude_asv_tau0.5_range: 0.076-0.487
    v3_magnitude_asv_tau0.05_range: 0.008-0.047
    v3_magnitude_asv_tau0.1_range: 0.014-0.093
    v3_coverage_tau0.05: 100.0%
    v3_coverage_tau0.1: 100.0%
    n_sensitivity_mediation_tau005:
      topology: mediation
      tau: 0.05
      C0: sym_mild
      mc_reps: 500
      N_1000:
        naive_power: 0.89
        asv_power: 0
        median_se: 0.070025
        median_signif_asv: 0
      N_2000:
        naive_power: 0.998
        asv_power: 0
        median_se: 0.049649
        median_signif_asv: 0
      N_5000:
        naive_power: 1
        asv_power: 0
        median_se: 0.031301
        median_signif_asv: 0
      N_10000:
        naive_power: 1
        asv_power: 1
        median_se: 0.022152
        median_signif_asv: null
      N_20000:
        naive_power: 1
        asv_power: 1
        median_se: 0.01566
        median_signif_asv: null
      N_50000:
        naive_power: 1
        asv_power: 1
        median_se: 0.009903
        median_signif_asv: null
      recovery_N: 10000
      interpretation: 'Sharp phase transition at N~6000-10000. Below: 1.96*SE > tau=0.05
        so signif_ASV=0 (ASV kills all rejections). Above: 1.96*SE < tau=0.05 so signif_ASV=None
        (infinite robustness), ASV passes all.'
- exp_id: plan008_binarization_collapse
  name: ''
  status: DONE
  conclusion: success
  metrics:
    confounding:
      D_mean: 0.0253
      D_med: 0.0182
      D_P95: 0.0733
      D_max: 0.2213
      frac_gt_001: 0.686
      frac_gt_005: 0.138
      sign_flip: 0
    mediation:
      D_mean: 0.0446
      D_med: 0.0355
      D_P95: 0.1179
      D_max: 0.252
      frac_gt_001: 0.835
      frac_gt_005: 0.36
      sign_flip: 0
    collider:
      D_mean: 0.0169
      D_med: 0.0125
      D_P95: 0.0472
      D_max: 0.1069
      frac_gt_001: 0.572
      frac_gt_005: 0.039
      sign_flip: 0
    M-bias:
      D_mean: 0.0063
      D_med: 0.0054
      D_P95: 0.0147
      D_max: 0.0328
      frac_gt_001: 0.181
      frac_gt_005: 0
      sign_flip: 0
    exposure:
      D_mean: 0.5164
      D_med: 0.506
      D_P95: 0.8453
      D_max: 1.3876
      frac_gt_001: 1
      frac_gt_005: 0.999
      sign_flip: 0.14
    IV:
      D_mean: 0.926
      D_med: 0.9394
      D_P95: 1.3426
      D_max: 2.0809
      frac_gt_001: 1
      frac_gt_005: 1
      sign_flip: 0.175
- exp_id: plan005_asv_extended
  name: ''
  status: DONE
  conclusion: success
  metrics:
    envelope_violations:
      mbias: 0
      iv: 0
      frontdoor: 0
    plim_at_identity:
      mbias: 0.5128
      iv: 0.6598
      frontdoor: 0.4998
    asv_tau05:
      mbias:
        sign_flip: null
        magnitude_10pct: null
      iv:
        sign_flip_range: 1.1-6.7
        magnitude_10pct_range: 0.101-0.607
      frontdoor:
        sign_flip: null
        magnitude_10pct_range: 0.064-0.387
    mc_coverage:
      mbias_tau005:
        plim_acc: 1
        bias_bounded: 1
      mbias_tau01:
        plim_acc: 1
        bias_bounded: 1
      iv_tau005:
        plim_acc: 1
        bias_bounded: 1
      iv_tau01:
        plim_acc: 1
        bias_bounded: 1
      frontdoor_tau005:
        plim_acc: 1
        bias_bounded: 1
      frontdoor_tau01:
        plim_acc: 1
        bias_bounded: 1
    v_fixed_signif_filter:
      mbias:
        type_i: 0
        power_tau005: 95.8-99.2%
        power_tau01: 100%
      iv:
        type_i: 0
        power_tau005: 0%
        power_tau01: 0%
        note: correct — Wald estimator immediately fragile, signif_ASV≈0 blocks all
          rejections
      frontdoor:
        type_i: 0
        power_tau005: 100%
        power_tau01: 100%
    fixes_applied:
    - 'C1: compute_signif_asv_fast added'
    - 'C2: magnitude ASV tau≈0 returns 0.0'
    - 'W1: IV tau_true=plim_iv(I)=0.6598'
    - 'W2: M-bias tau_true=plim_mb(I)=0.5128'
    fixed_script: /home/sonny/causal_annot_error_attrib/plan_005_asv_extended_fixed.py
    runtime_seconds: 46.2
- exp_id: plan_004_asv_v3_fixed
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: plan002_k57_extension
  name: ''
  status: DONE
  conclusion: success
  metrics:
    cross_k_comparison_7topo:
      confounding:
        K3:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.993
          violation: 1
          amplification: 1
          worst_case_diag90: 0.1614
          worst_case_diag70: 0.2744
          worst_case_diag50: 0.2993
        K5:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 1
          violation: 1
          amplification: 1
          worst_case_diag90: 0.1107
          worst_case_diag70: 0.2156
          worst_case_diag50: 0.2462
        K7:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 1
          violation: 1
          amplification: 1
          worst_case_diag90: 0.0933
          worst_case_diag70: 0.1859
          worst_case_diag50: 0.2264
      mediation:
        K3:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.838
          violation: 1
          amplification: 1
          worst_case_diag90: 0.1223
          worst_case_diag70: 0.251
          worst_case_diag50: 0.3032
        K5:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.966
          violation: 1
          amplification: 1
          worst_case_diag90: 0.0867
          worst_case_diag70: 0.1832
          worst_case_diag50: 0.2396
        K7:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 1
          violation: 1
          amplification: 1
          worst_case_diag90: 0.0607
          worst_case_diag70: 0.1421
          worst_case_diag50: 0.1879
      collider:
        K3:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.666
          violation: 1
          amplification: 1
          worst_case_diag90: 0.0503
          worst_case_diag70: 0.1064
          worst_case_diag50: 0.1256
        K5:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.955
          violation: 1
          amplification: 1
          worst_case_diag90: 0.0477
          worst_case_diag70: 0.1087
          worst_case_diag50: 0.1306
        K7:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.992
          violation: 1
          amplification: 1
          worst_case_diag90: 0.0352
          worst_case_diag70: 0.0826
          worst_case_diag50: 0.1131
      exposure:
        K3:
          tau_specific_sign_flip: N/A (all-coef fallback; MVP beta1 flip=83.4%)
          all_coef_sign_flip: 0.99
          violation: 1
          amplification: 0.999
          worst_case_diag90: 0.2726
          worst_case_diag70: 0.7092
          worst_case_diag50: 1.1438
        K5:
          tau_specific_sign_flip: N/A (all-coef fallback)
          all_coef_sign_flip: 1
          violation: 1
          amplification: 0.998
          worst_case_diag90: 0.2097
          worst_case_diag70: 0.5782
          worst_case_diag50: 0.8784
        K7:
          tau_specific_sign_flip: N/A (all-coef fallback)
          all_coef_sign_flip: 1
          violation: 1
          amplification: 0.999
          worst_case_diag90: 0.1853
          worst_case_diag70: 0.4913
          worst_case_diag50: 0.7441
      mbias:
        K3:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.667
          violation: 0.584
          amplification: 0.089
          worst_case_diag90: 0.0106
          worst_case_diag70: 0.0226
          worst_case_diag50: 0.0287
        K5:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.954
          violation: 1
          amplification: 0
          worst_case_diag90: 0.0154
          worst_case_diag70: 0.0374
          worst_case_diag50: 0.0487
        K7:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.992
          violation: 1
          amplification: 0
          worst_case_diag90: 0.0133
          worst_case_diag70: 0.0319
          worst_case_diag50: 0.0449
      iv:
        K3:
          tau_specific_sign_flip: 0.526
          all_coef_sign_flip: 0.526
          violation: 1
          amplification: 1
          worst_case_diag90: 0.2993
          worst_case_diag70: 1.6444
          worst_case_diag50: 14.0463
          note: Wald estimator extremely unstable at low accuracy
        K5:
          tau_specific_sign_flip: 0.514
          all_coef_sign_flip: 0.514
          violation: 1
          amplification: 1
          worst_case_diag90: 0.4053
          worst_case_diag70: 2.1036
          worst_case_diag50: 9.6932
        K7:
          tau_specific_sign_flip: 0.523
          all_coef_sign_flip: 0.523
          violation: 1
          amplification: 1
          worst_case_diag90: 0.3605
          worst_case_diag70: 1.8132
          worst_case_diag50: 8.2204
      frontdoor:
        K3:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.836
          violation: 1
          amplification: 1
          worst_case_diag90: 0.1407
          worst_case_diag70: 0.2604
          worst_case_diag50: 0.2966
        K5:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.967
          violation: 1
          amplification: 1
          worst_case_diag90: 0.1057
          worst_case_diag70: 0.2066
          worst_case_diag50: 0.2507
        K7:
          tau_specific_sign_flip: 0
          all_coef_sign_flip: 0.993
          violation: 1
          amplification: 1
          worst_case_diag90: 0.0785
          worst_case_diag70: 0.1646
          worst_case_diag50: 0.2119
    conclusion_summary:
      structural_guarantee: tau_specific_sign_flip = 0% across ALL K for 5/7 topologies
        (confounding/mediation/collider/mbias/frontdoor)
      iv_new_finding: IV ~52% tau sign flip (K-invariant) — Wald denominator sign
        reversal under random C
      exposure_clarification: Exposure tau_spec_sflip column is all-coef fallback.
        Actual beta1-specific flip rate = 83.4% (from MVP)
      worst_case_trend: Decreasing with K for 5/7 topologies (K=3 most conservative).
        IV catastrophic at low accuracy (WC_d50 up to 14x). Exposure decreasing.
      mbias_special: Amplification drops to 0% at K>=5
      rng_fix: Deterministic per-(topo,K,threshold) seeds via SHA-256. Previous values
        had RNG ordering artifact.
    runtime_seconds: 20
    gpu: RTX 5090 cuda:0
    script: /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py
- exp_id: plan009_pathological_matrices
  name: ''
  status: DONE
  conclusion: success
  metrics:
    regression_dichotomy:
      benign_topologies:
        list:
        - confounding
        - mediation
        - collider
        - frontdoor
        - mbias
        R2_range: 0.61-0.77
        primary_predictor: effective_rank
        secondary_predictors:
        - spectral_gap
        - condition_number
      dangerous_topologies:
        list:
        - exposure
        - iv
        exposure_R2: 0.11
        iv_R2: ~0
        iv_note: regression has no explanatory power — Wald denominator sign reversal
          is discrete, not predicted by continuous matrix features
        exposure_note: 'near_perm eps=0.01: 15% catastrophic bias above threshold'
      global_R2: ~0 (cross-topology aggregation destroys predictive power — different
        bias mechanisms)
    risk_tiers:
      low:
        topologies:
        - mbias
        max_bias: <0.04
        note: safe even under worst-case pathological C
      medium:
        topologies:
        - confounding
        - mediation
        - collider
        - frontdoor
        bias_range: 0.1-0.31
        catastrophic_fraction: 0%
        R2: 0.70-0.77
        note: bounded bias, matrix features predictive
      high:
        topologies:
        - exposure
        - iv
        note: 'catastrophic regardless of C quality — exposure: structural identification
          failure; IV: Wald estimator explosion (near_perm eps=0.01 cat=61-73%, rank-deficient
          bias reaches millions)'
    most_consistent_predictor: condition_number (significant in 5/5 medium-risk topologies)
    hypothesis_assessment:
      H1_predictable_catastrophic: partially — risk tier determined by topology, not
        C features
      H2_matrix_features_strong: topology-dependent — 5/7 R²>0.6, exposure/IV fail
      H3_safety_threshold: not confirmed — boundary is topology-based, not C-feature
        threshold
      H4_diagnostic_features: partially — condition_number most consistent, but needs
        topology-specific criteria
    iv_filtering:
      n_filtered: 3000
      n_total: 28000
      pct_infinite: 10.7
      note: non-finite Wald values silently filtered from regression; must note in
        paper
    pathological_C_types:
    - near_permutation (eps=0.01,0.05,0.1,0.2)
    - rank_deficient
    - block_diagonal
    K_values:
    - 3
    - 5
    - 7
    M_per_config: 1000
    N_per_sim: 5000000
    runtime_seconds: 25
    analysis_report: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md
    output_files:
      summary_json: /home/sonny/causal_annot_error_attrib/artifacts/plan009/pathological_bias_summary.json
      regression_txt: /home/sonny/causal_annot_error_attrib/artifacts/plan009/regression_results.txt
      analysis_md: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md
- exp_id: plan007_correction_guidance
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_combos: 210
    runtime_sec: 2792
    ppi_grand_mean_bias_red: 93.8%
    ppi_grand_mean_coverage: 96.8%
    ppi_win_rate: 95.2% (40/42)
    mcsimex_grand_mean_bias_red: 20.9%
    dsl_grand_mean_bias_red: -144.8%
    naive_plugin_grand_mean_bias_red: -20.0%
    mla_grand_mean_bias_red: -37.4%
    fwl_invariance_verified: true
    fwl_invariance_topologies: confounding, mediation, collider, mbias (0.0% bias_red
      for naive/mla)
    dsl_effective_topologies: confounding (49.8%), mediation (70.3%)
    dsl_failure_topologies: mbias (-768%), iv (-187%), collider (-89%), exposure (-60%),
      frontdoor (-29%)
    ppi_weakness: 'mbias+realistic_llm: -25.1% bias_red (but 99% coverage)'
- exp_id: plan010_annot_sensitivity_toolkit
  name: ''
  status: DONE
  conclusion: success
  metrics:
    tests_passed: 35/35
    modules: 7
    topologies: 7
    correction_methods: 5
    lines_of_code:
      __init__.py: 53
      bias.py: 174
      asv.py: 119
      correction.py: 422
      confusion.py: 129
      dgp.py: 213
      utils.py: 95
      test_core.py: 35 tests
    example_output:
      confounding_k3_bias_pct: +10.20%
      magnitude_asv: 0.967
      sign_flip_asv: null
      recommended_with_gold: ppi
      recommended_without_gold: dsl
- exp_id: plan006_asv_empirical
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_scenarios: 210
    configs: 14
    topologies: 7
    k_values:
    - 2
    - 3
    - 10
    models:
    - llama4
    - deepseek
    - qwen3
    - qwen2.5-7b
    sign_flips: 0
    overall_asv_unsafe_pct: 43.8
    k2_mean_bias_pct: 36.9
    k3_mean_bias_pct: 65.3
    k10_mean_bias_pct: 12.2
    k2_iv_bias_pct: 116.5
    k3_iv_bias_pct: 252.3
    k10_iv_bias_pct: 30.3
    f1_disconnect: civil_comments F1=0.72-0.75 but IV bias 101-131%
    7b_vs_235b_bias_ratio: 1.24

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
  "promptId": "2df54322-c003-4116-954b-1411cf28b9be",
  "type": "user",
  "uuid": "ee5a2324-549e-4ba7-9d6b-ecde715b2582",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T05:50:10.702Z_

```json
{
  "parentUuid": "ee5a2324-549e-4ba7-9d6b-ecde715b2582",
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
  "uuid": "d6fb1edb-7e48-41bb-98f2-7defab35b5d3",
  "timestamp": "2026-05-21T05:50:10.702Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T05:50:10.702Z_

```json
{
  "parentUuid": "d6fb1edb-7e48-41bb-98f2-7defab35b5d3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "336ca792-3e3e-4a8f-a00d-119a35e4f099",
  "timestamp": "2026-05-21T05:50:10.702Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：理论-实证桥梁完全闭合：3 claims 均以完整强度呈现，实证数据覆盖充分且 theory-empirical match 紧凑 核心假设：['API 402 解决，VAST/Civil Comments 获得 frontier 模型(≥235B)标注，消除 model-tier asymmetry', '…",
  "leafUuid": "336ca792-3e3e-4a8f-a00d-119a35e4f099",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-class annotation bias: taxonomy, sensitivity analysis, and empirical validation",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783"
}
```

---

### Assistant

_source line 8 · 2026-05-21T05:50:14.033Z_

我来先检查是否有额外的实验计划或相关文件需要参考。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "336ca792-3e3e-4a8f-a00d-119a35e4f099",
  "isSidechain": false,
  "requestId": "req_011CbFC1951AZLYirnTtFe1R",
  "type": "assistant",
  "uuid": "d274dedd-cf4e-4963-83bd-c7d2b9625007",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GMPDnDyfzgcT9MfrSRaQD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 27243,
      "cache_read_input_tokens": 11841,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 112,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 27243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27243
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

_source line 9 · 2026-05-21T05:50:14.974Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01M1RdQM4Uc4HDpkiQhpDU9A`</summary>

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
  "parentUuid": "d274dedd-cf4e-4963-83bd-c7d2b9625007",
  "isSidechain": false,
  "requestId": "req_011CbFC1951AZLYirnTtFe1R",
  "type": "assistant",
  "uuid": "35cf104c-8fa1-4469-8c13-ba0f1edd7bad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GMPDnDyfzgcT9MfrSRaQD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 27243,
      "cache_read_input_tokens": 11841,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 112,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 27243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27243
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

_source line 10 · 2026-05-21T05:50:15.016Z_

<details><summary>↩ Tool result · `toolu_01M1RdQM4Uc4HDpkiQhpDU9A`</summary>

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
projects/causal_annot_error_attrib/docs/IDEA_BRIEF.md
projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/paper_framing.md
projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper_framing.md
projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/paper_framing.md
projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/review_report.md
projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/review_report.md
projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/review_report.md
projects/causal_annot_error_attrib/artifacts/plan004_asv_framework/report/plan004_results.md
projects/causal_annot_error_attrib/.claude/sessions/distiller_ee1ca598/CLAUDE.md
projects/causal_annot_error_attrib/.claude/sessions/distiller_ee1ca598/AGENTS.md
skills/projects/causal_annot_error_attrib/distilled-research.skill.md
skills/projects/causal_annot_error_attrib/distilled-writing.skill.md
.venv/lib/python3.14/site-packages/pyparsing/ai/best_practices.md
.venv/lib/python3.14/site-packages/numpy/random/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/distributions/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/philox/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md
.venv/lib/python3.14/site-packages/scipy/fft/_pocketfft/LICENSE.md
projects/causal_annot_error_attrib/.claude/sessions/agent_e59ac7b4/CLAUDE.md
projects/causal_annot_error_attrib/.claude/sessions/agent_e59ac7b4/AGENTS.md
projects/causal_annot_error_attrib/.claude/sessions/agent_a2e2e510/CLAUDE.md
projects/causal_annot_error_attrib/.claude/sessions/agent_a2e2e510/AGENTS.md
projects/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md
projects/causal_annot_error_attrib/artifacts/plan009/report/plan009_analysis.md
projects/causal_annot_error_attrib/artifacts/plan007/plan007_analysis.md
projects/causal_annot_error_attrib/artifacts/plan007/report/plan007_analysis.md
projects/causal_annot_error_attrib/.claude/sessions/agent_82826270/CLAUDE.md
projects/causal_annot_error_attrib/.claude/sessions/agent_82826270/AGENTS.md
projects/causal_annot_error_attrib/.pytest_cache/README.md
projects/causal_annot_error_attrib/memory.md
projects/causal_annot_error_attrib/task_context/reviewer.md
projects/causal_annot_error_attrib/report.md
projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f/CLAUDE.md
projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f/AGENTS.md
projects/causal_annot_error_attrib/paper_framing.md
projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d/CLAUDE.md
projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d/AGENTS.md
projects/causal_annot_error_attrib/ROADMAP.md
projects/causal_annot_error_attrib/.claude/sessions/reviewer_15d8e49e/CLAUDE.md
projects/causal_annot_error_attrib/.claude/sessions/reviewer_15d8e49e/AGENTS.md
.claude/CLAUDE.md
AGENTS.md
projects/causal_annot_error_attrib/.claude/CLAUDE.md
projects/causal_annot_error_attrib/AGENTS.md
projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73/CLAUDE.md
projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73/AGENTS.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35cf104c-8fa1-4469-8c13-ba0f1edd7bad",
  "isSidechain": false,
  "promptId": "2df54322-c003-4116-954b-1411cf28b9be",
  "type": "user",
  "uuid": "7fc1ff24-5d9c-4cb7-886d-722472d9a018",
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
      "projects/causal_annot_error_attrib/docs/IDEA_BRIEF.md",
      "projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/paper_framing.md",
      "projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/paper_framing.md",
      "projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/paper_framing.md",
      "projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/review_report.md",
      "projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/review_report.md",
      "projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/review_report.md",
      "projects/causal_annot_error_attrib/artifacts/plan004_asv_framework/report/plan004_results.md",
      "projects/causal_annot_error_attrib/.claude/sessions/distiller_ee1ca598/CLAUDE.md",
      "projects/causal_annot_error_attrib/.claude/sessions/distiller_ee1ca598/AGENTS.md",
      "skills/projects/causal_annot_error_attrib/distilled-research.skill.md",
      "skills/projects/causal_annot_error_attrib/distilled-writing.skill.md",
      ".venv/lib/python3.14/site-packages/pyparsing/ai/best_practices.md",
      ".venv/lib/python3.14/site-packages/numpy/random/LICENSE.md",
      ".venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md",
      ".venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md",
      ".venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/LICENSE.md",
      ".venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/distributions/LICENSE.md",
      ".venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md",
      ".venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md",
      ".venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/philox/LICENSE.md",
      ".venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md",
      ".venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md",
      ".venv/lib/python3.14/site-packages/scipy/fft/_pocketfft/LICENSE.md",
      "projects/causal_annot_error_attrib/.claude/sessions/agent_e59ac7b4/CLAUDE.md",
      "projects/causal_annot_error_attrib/.claude/sessions/agent_e59ac7b4/AGENTS.md",
      "projects/causal_annot_error_attrib/.claude/sessions/agent_a2e2e510/CLAUDE.md",
      "projects/causal_annot_error_attrib/.claude/sessions/agent_a2e2e510/AGENTS.md",
      "projects/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md",
      "projects/causal_annot_error_attrib/artifacts/plan009/report/plan009_analysis.md",
      "projects/causal_annot_error_attrib/artifacts/plan007/plan007_analysis.md",
      "projects/causal_annot_error_attrib/artifacts/plan007/report/plan007_analysis.md",
      "projects/causal_annot_error_attrib/.claude/sessions/agent_82826270/CLAUDE.md",
      "projects/causal_annot_error_attrib/.claude/sessions/agent_82826270/AGENTS.md",
      "projects/causal_annot_error_attrib/.pytest_cache/README.md",
      "projects/causal_annot_error_attrib/memory.md",
      "projects/causal_annot_error_attrib/task_context/reviewer.md",
      "projects/causal_annot_error_attrib/report.md",
      "projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f/CLAUDE.md",
      "projects/causal_annot_error_attrib/.claude/sessions/paper_agent_20baa82f/AGENTS.md",
      "projects/causal_annot_error_attrib/paper_framing.md",
      "projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d/CLAUDE.md",
      "projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d/AGENTS.md",
      "projects/causal_annot_error_attrib/ROADMAP.md",
      "projects/causal_annot_error_attrib/.claude/sessions/reviewer_15d8e49e/CLAUDE.md",
      "projects/causal_annot_error_attrib/.claude/sessions/reviewer_15d8e49e/AGENTS.md",
      ".claude/CLAUDE.md",
      "AGENTS.md",
      "projects/causal_annot_error_attrib/.claude/CLAUDE.md",
      "projects/causal_annot_error_attrib/AGENTS.md",
      "projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73/CLAUDE.md",
      "projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73/AGENTS.md"
    ],
    "durationMs": 33,
    "numFiles": 88,
    "truncated": false
  },
  "sourceToolAssistantUUID": "35cf104c-8fa1-4469-8c13-ba0f1edd7bad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T05:50:17.470Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RLgLsAjcsremj7c4HFUsJt`</summary>

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
  "parentUuid": "7fc1ff24-5d9c-4cb7-886d-722472d9a018",
  "isSidechain": false,
  "requestId": "req_011CbFC1TaUzdNSvzQwHaViq",
  "type": "assistant",
  "uuid": "ee491193-b11a-4f0d-90cf-82f13a5d8f4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WyA2Dr1fWrAVYW6aXtvBKc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2492,
      "cache_read_input_tokens": 39084,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2492,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 39084,
          "cache_creation_input_tokens": 2492,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2492
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

_source line 12 · 2026-05-21T05:50:17.486Z_

<details><summary>↩ Tool result · `toolu_01RLgLsAjcsremj7c4HFUsJt`</summary>

```text
1	# causal_annot_error_attrib — Research Dashboard
2	
3	> 最后更新: 2026-05-21 05:44 UTC | 更新原因: Dream 审稿反馈全部 5 项修复完成，stress test committed
4	
5	> 详见 paper_framing.md（story/claims）、experiment_plan.yaml（实验列表）
6	
7	## 核心方向
8	多分类 LLM 标注误差在因果推断中的偏差传播：K×K 混淆矩阵 × 7 DAG 拓扑偏差分类 + ASV 灵敏度框架 + 校正指导。
9	
10	## 当前阶段：Dream 审稿反馈修改完成 → Re-Dream 待系统恢复
11	
12	### Target Venue
13	- Primary: AAAI 2027（abstract 2026-07-21, paper 2026-07-28, ~68 天）
14	
15	### Core Claims 覆盖率
16	| Claim | 完成/总计 | 状态 |
17	|-------|-----------|------|
18	| 1. Multi-class bias taxonomy | **5/6 (83%)** | plan_001✅ plan_002✅ plan_008✅ plan_009✅ plan_010✅ plan_003⚠️(API 402) |
19	| 2. ASV framework | **3/3 (100%)** | plan_004✅ plan_005✅ plan_006✅ |
20	| 3. Correction guidance | **1/1 (100%)** | plan_007✅ |
21	
22	### Dream 审稿反馈修改（全部完成 ✅）
23	| Dream 问题 | 状态 | Commit |
24	|------------|------|--------|
25	| Related work 极薄 | ✅ | +5 refs (Carroll, Dosemeci, Jurek, Lash, Grimmer). 总 31 citations |
26	| ASV vs Lash PBA 未阐述 | ✅ | Related work 三维度对比 |
27	| Brenner (1993) 矛盾 | ✅ | method.tex 脚注 (sign reversal vs amplification) |
28	| IV Dirichlet subspace | ✅ | Appendix section + Table (sign flip→0% at d≥0.5, amplification 100%) |
29	| Non-differential stress test | ✅ | Appendix section + limitations 交叉引用 (ε=0.05 → +2.3pp) |
30	
31	### 关键发现
32	- 5/7 拓扑 τ_sign_flip=0%; 2/7 危险（exposure 83%, IV 52%）
33	- IV Dirichlet: sign flip 0% at diag≥0.5, amplification 100% at all levels
34	- Non-diff stress test: ε≤0.05 → violation 仅增 2.3pp，假设 robust
35	- PPI++(93.8%) >> MC-SIMEX(20.9%) >> DSL(2/7 only)
36	- HumAID (K=10): 8 valid configs, IV bias 12.4–42.1%, 55.4% ASV-unsafe
37	- 跨K实证: 0 sign flips / 126 scenarios, 7B/235B ratio 1.24
38	
39	## 论文写作
40	- 编译通过 16 pages (8 main + 8 appendix), 0 critical warnings, 31 citations
41	- 全部 Dream 写作修复已 commit (8617499, fb88983)
42	
43	## 近期任务
44	- [x] Dream W1-W5: 全部 5 个跨档结构性问题修复
45	- [x] Commit all changes (2 commits)
46	- [ ] Re-dream → **BLOCKED**: 连续 6 次 Phase 1 crash, 已报 Manager
47	- [ ] fig5/fig6 重新生成（含 filtered data）
48	- [ ] API 充值 → plan_003 剩余组合（非阻塞）
49	
50	## GPU 预算
51	home-1x5090: 1× RTX 5090（当前空闲，无 running 实验）
52	
53	## 关键决策日志
54	
55	| ID | 日期 | 摘要 | 关联实验 |
56	|----|------|------|----------|
57	| D017 | 2026-05-21 | 保持 14 configs / 98 scenarios；ASV-unsafe 阈值 ≤1.0 (3 | plan006_asv_empirical |
58	| D016 | 2026-05-21 | plan_006 全量结果确认跨K实证验证：K越小bias越大（K=3 IV 252%），F1 di | plan006_asv_empirical, plan003_empirical_confusion_matrices |
59	| D015 | 2026-05-20 | plan_006 humaid 实证结果确认理论框架：IV 最脆弱(42% bias), colli | plan003_empirical_confusion_matrices, plan005_asv_extended, plan004_asv_framework |
60	| D014 | 2026-05-20 | plan_007 全量结果确立 Claim 3 correction guidance 层级：PPI | plan007_correction_guidance |
61	| D013 | 2026-05-20 | plan_009 证实病态矩阵诊断指标（spectral_gap, condition_number | plan009_pathological_matrices |
62	| D012 | 2026-05-20 | plan_007 预览发现：Frisch-Waugh 定理导致 naive_plugin/MLA 对 | plan007_correction_guidance |
63	| D011 | 2026-05-20 | paper_framing Claim 1 拓扑数从 6 改为 7（正式纳入 exposure mi | plan001_dag_taxonomy, plan002_k57_extension |
64	| D010 | 2026-05-20 | D010: τ sign_flip 结构性保证修正为 5/7 拓扑（排除 exposure + IV | plan002_k57_extension, plan001_dag_taxonomy |
65	| D009 | 2026-05-20 | D008 修正：6 拓扑 ASV 排序为多维度（非单一排序）。Magnitude: front-do | plan005_asv_extended, plan004_asv_framework |
66	| D008 | 2026-05-20 | 6 拓扑 ASV 灵敏度排序确立：IV(极脆弱) > front-door > confoundin | plan004_asv_framework, plan005_asv_extended |
67	
68	
69	
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee491193-b11a-4f0d-90cf-82f13a5d8f4d",
  "isSidechain": false,
  "promptId": "2df54322-c003-4116-954b-1411cf28b9be",
  "type": "user",
  "uuid": "2c47409a-01ed-4948-971a-c6feedfc29a2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/ROADMAP.md",
      "content": "# causal_annot_error_attrib — Research Dashboard\n\n> 最后更新: 2026-05-21 05:44 UTC | 更新原因: Dream 审稿反馈全部 5 项修复完成，stress test committed\n\n> 详见 paper_framing.md（story/claims）、experiment_plan.yaml（实验列表）\n\n## 核心方向\n多分类 LLM 标注误差在因果推断中的偏差传播：K×K 混淆矩阵 × 7 DAG 拓扑偏差分类 + ASV 灵敏度框架 + 校正指导。\n\n## 当前阶段：Dream 审稿反馈修改完成 → Re-Dream 待系统恢复\n\n### Target Venue\n- Primary: AAAI 2027（abstract 2026-07-21, paper 2026-07-28, ~68 天）\n\n### Core Claims 覆盖率\n| Claim | 完成/总计 | 状态 |\n|-------|-----------|------|\n| 1. Multi-class bias taxonomy | **5/6 (83%)** | plan_001✅ plan_002✅ plan_008✅ plan_009✅ plan_010✅ plan_003⚠️(API 402) |\n| 2. ASV framework | **3/3 (100%)** | plan_004✅ plan_005✅ plan_006✅ |\n| 3. Correction guidance | **1/1 (100%)** | plan_007✅ |\n\n### Dream 审稿反馈修改（全部完成 ✅）\n| Dream 问题 | 状态 | Commit |\n|------------|------|--------|\n| Related work 极薄 | ✅ | +5 refs (Carroll, Dosemeci, Jurek, Lash, Grimmer). 总 31 citations |\n| ASV vs Lash PBA 未阐述 | ✅ | Related work 三维度对比 |\n| Brenner (1993) 矛盾 | ✅ | method.tex 脚注 (sign reversal vs amplification) |\n| IV Dirichlet subspace | ✅ | Appendix section + Table (sign flip→0% at d≥0.5, amplification 100%) |\n| Non-differential stress test | ✅ | Appendix section + limitations 交叉引用 (ε=0.05 → +2.3pp) |\n\n### 关键发现\n- 5/7 拓扑 τ_sign_flip=0%; 2/7 危险（exposure 83%, IV 52%）\n- IV Dirichlet: sign flip 0% at diag≥0.5, amplification 100% at all levels\n- Non-diff stress test: ε≤0.05 → violation 仅增 2.3pp，假设 robust\n- PPI++(93.8%) >> MC-SIMEX(20.9%) >> DSL(2/7 only)\n- HumAID (K=10): 8 valid configs, IV bias 12.4–42.1%, 55.4% ASV-unsafe\n- 跨K实证: 0 sign flips / 126 scenarios, 7B/235B ratio 1.24\n\n## 论文写作\n- 编译通过 16 pages (8 main + 8 appendix), 0 critical warnings, 31 citations\n- 全部 Dream 写作修复已 commit (8617499, fb88983)\n\n## 近期任务\n- [x] Dream W1-W5: 全部 5 个跨档结构性问题修复\n- [x] Commit all changes (2 commits)\n- [ ] Re-dream → **BLOCKED**: 连续 6 次 Phase 1 crash, 已报 Manager\n- [ ] fig5/fig6 重新生成（含 filtered data）\n- [ ] API 充值 → plan_003 剩余组合（非阻塞）\n\n## GPU 预算\nhome-1x5090: 1× RTX 5090（当前空闲，无 running 实验）\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D017 | 2026-05-21 | 保持 14 configs / 98 scenarios；ASV-unsafe 阈值 ≤1.0 (3 | plan006_asv_empirical |\n| D016 | 2026-05-21 | plan_006 全量结果确认跨K实证验证：K越小bias越大（K=3 IV 252%），F1 di | plan006_asv_empirical, plan003_empirical_confusion_matrices |\n| D015 | 2026-05-20 | plan_006 humaid 实证结果确认理论框架：IV 最脆弱(42% bias), colli | plan003_empirical_confusion_matrices, plan005_asv_extended, plan004_asv_framework |\n| D014 | 2026-05-20 | plan_007 全量结果确立 Claim 3 correction guidance 层级：PPI | plan007_correction_guidance |\n| D013 | 2026-05-20 | plan_009 证实病态矩阵诊断指标（spectral_gap, condition_number | plan009_pathological_matrices |\n| D012 | 2026-05-20 | plan_007 预览发现：Frisch-Waugh 定理导致 naive_plugin/MLA 对 | plan007_correction_guidance |\n| D011 | 2026-05-20 | paper_framing Claim 1 拓扑数从 6 改为 7（正式纳入 exposure mi | plan001_dag_taxonomy, plan002_k57_extension |\n| D010 | 2026-05-20 | D010: τ sign_flip 结构性保证修正为 5/7 拓扑（排除 exposure + IV | plan002_k57_extension, plan001_dag_taxonomy |\n| D009 | 2026-05-20 | D008 修正：6 拓扑 ASV 排序为多维度（非单一排序）。Magnitude: front-do | plan005_asv_extended, plan004_asv_framework |\n| D008 | 2026-05-20 | 6 拓扑 ASV 灵敏度排序确立：IV(极脆弱) > front-door > confoundin | plan004_asv_framework, plan005_asv_extended |\n\n\n\n",
      "numLines": 70,
      "startLine": 1,
      "totalLines": 70
    }
  },
  "sourceToolAssistantUUID": "ee491193-b11a-4f0d-90cf-82f13a5d8f4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-21T05:50:17.563Z_

````json
{
  "parentUuid": "2c47409a-01ed-4948-971a-c6feedfc29a2",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**causal_annot_error_attrib**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"causal_annot_error_attrib\")` 或 `load_project_config(\"causal_annot_error_attrib\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n- **causal-annot-error-attrib-research** — 领域蒸馏——LLM标注误差在因果推断中的传播与校正：基线、指标、方法论共识与研究空白（12篇论文归纳）  →  `/home/ubuntu/.agent-ml-research-prod_0510/skills/projects/causal_annot_error_attrib/distilled-research.skill.md`\n- **causal-annot-error-attrib-writing** — 领域蒸馏——LLM标注误差×因果推断论文的叙事策略、图表设计、展示共识（8篇深度精读归纳）  →  `/home/ubuntu/.agent-ml-research-prod_0510/skills/projects/causal_annot_error_attrib/distilled-writing.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/causal_annot_error_attrib/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "24b8ffac-f2ec-413c-b780-7e600f9993fa",
  "timestamp": "2026-05-21T05:50:17.563Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：理论-实证桥梁完全闭合：3 claims 均以完整强度呈现，实证数据覆盖充分且 theory-empirical match 紧凑 核心假设：['API 402 解决，VAST/Civil Comments 获得 frontier 模型(≥235B)标注，消除 model-tier asymmetry', '…",
  "leafUuid": "24b8ffac-f2ec-413c-b780-7e600f9993fa",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-class annotation bias: taxonomy, sensitivity analysis, and empirical validation",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783"
}
```

---

### Assistant

_source line 16 · 2026-05-21T05:50:55.984Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment_plan, under the "best" tier conditions. Let me identify all planned experiments and their details, then generate the YAML output.

Let me identify all experiments from the plan:

1. **plan_001** - DONE - Derive and MC-validate bias expressions for 6 DAG topologies with K=3
2. **plan_002** - DONE - Extend bias expressions to K=5,7
3. **plan_003** - DONE (failed) - Empirical confusion matrices: 3 LLMs × 3 CSS tasks


4. **plan_004** - DONE - ASV framework: formal proofs for confounding, mediation, collider
5. **plan_005** - DONE - ASV MC validation for M-bias, instrument, front-door
6. **plan_006** - planned - ASV calibration on empirical data
7. **plan_007** - planned - Correction guidance framework
8. **plan_008** - DONE - Binarization collapse analysis
9. **plan_009** - DONE - Pathological confusion matrix analysis
10. **plan_010** - planned - annot-sensitivity Python toolkit

Now I need to focus on the planned experiments and generate predicted results for each under best-case conditions. I'm noticing a discrepancy between the experiment_plan status fields and the registry entries — several experiments marked as "planned" actually show completion records with success metrics. The registry appears to be the authoritative source here. Re-reading the user's request more carefully, they're asking me to expand detailed data for each "planned" experiment in the plan, but I need to identify which ones actually have that status versus which are already completed in the registry. Now I'm laying out the remaining best-tier metrics for the experiments, including the PPI bias reduction targets, ASV safety thresholds, and correlation measures. With these parameters defined—assuming API 402 gets resolved, frontier models label the datasets, and the theoretical predictions align within 15% MAPE of empirical results—I can now generate the complete YAML with best-case projections for each experiment in the plan. me carefully construct the full imagined results for each plan:

**plan_001** (DONE - actual results available)
- Already done with strong results. In best tier, these hold as-is.

**plan_002** (DONE)
- Already done.

**plan_003** (Failed - API 402)
- In best tier: API 402 resolved, all 3 datasets × 4 models complete. 12-14 usable configs.

**plan_004** (DONE)
- Already done.

**plan_005** (DONE)
- Already done.

**plan_006** (planned in experiment_plan, but DONE in registry)
- In best tier with API 402 resolved: all datasets, frontier models.

**plan_007** (planned in experiment_plan, but DONE in registry)
- In best tier with empirical data.

**plan_008** (DONE)
- Already done.

**plan_009** (DONE)
- Already done.

**plan_010** (planned)
- Toolkit release.

Now I'm constructing the complete YAML configuration. The main improvements for the best tier are resolving the API 402 issue so plan_003 gets full coverage across all datasets and frontier models, expanding plan_006 to include all 14 configs instead of just the HumAID subset, and ensuring plan_007's empirical validation spans all datasets with metrics falling within best-tier ranges.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24b8ffac-f2ec-413c-b780-7e600f9993fa",
  "isSidechain": false,
  "requestId": "req_011CbFC1eJf3Zdz7Mw2p8vYn",
  "type": "assistant",
  "uuid": "6375c6db-6115-4007-9524-c935dd55ae3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CW5P9zAgiHUpbWsNkFPApF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7671,
      "cache_read_input_tokens": 41576,
      "output_tokens": 13672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13672,
          "cache_read_input_tokens": 41576,
          "cache_creation_input_tokens": 7671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7671
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

_source line 17 · 2026-05-21T05:54:44.788Z_

基于已完成实验的实际数据和 best 档核心假设（API 402 解决、frontier 模型覆盖、nondiff assumption 成立），逐实验展开预测。

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立，三条 claim 均以 full strength 呈现：
  (1) taxonomy 捕获 K≥3 方向反转(exposure 83%/IV 52% sign flip)和结构保证(5/7 topologies sign_flip=0%)的完整图景；
  (2) ASV 三类型覆盖不同 DAG，significance_ASV 的 N* phase transition 是核心 actionable 贡献；
  (3) PPI++ universally reliable(93.8% MC + ≥80% empirical)，DSL topology-limited，naive/MLA Frisch-Waugh 失效。
  Headline 无需修改："F1>0.9 的 LLM 在 IV 下仍 >200% bias，12% 场景效应放大无安全阈值。"

imagined_experiments:
  - name: "K=3 七拓扑 MC 偏差验证"
    plan_id: "plan_001"
    description: >
      对 7 个 DAG 拓扑(confounding, exposure, mediation, collider, M-bias, IV, front-door)
      推导 K=3 闭合偏差表达式，100k random C + 6 named structures MC 验证。
    expected_results:
      theory_mc_match_rate: 1.0
      tau_sign_flip_exposure_pct: 83.4
      tau_sign_flip_iv_pct: 52.6
      tau_sign_flip_5safe_topologies_pct: 0.0
      confounding_violation_rate: 1.0
      confounding_amplification_rate: 1.0
      mediation_tau_amplification: 1.0
      collider_tau_sign_flip: 0.0
      mbias_tau_sign_flip: 0.0
      mbias_tau_amplification: 0.104
      frontdoor_tau_sign_flip: 0.0
      frontdoor_tau_amplification: 1.0
      iv_violation_rate: 1.0
      iv_amplification_rate: 1.0
      exposure_worst_severity: 2.83
    result_rationale: >
      plan_001 已完成且全部通过。在 best 档下无需改动——7 拓扑的理论-MC 匹配已经完美(100k
      random C 100% within 95% CI)。关键结构性发现已锁定：5/7 拓扑 τ_sign_flip=0%
      是代数结构保证（confounding/mediation/collider/frontdoor 的偏差表达式中 τ 系数
      符号由 C 的对角优势决定，不可翻转；mbias 偏差量级太小），而 exposure(83.4%) 和
      IV(52.6%) 的 sign flip 源于根本不同的机制——前者是 near-permutation C 导致
      label swap，后者是 Wald 分母符号反转。这个 5+2 分裂是 Claim 1 的核心支撑。
    tables:
      - name: "Table 1: K=3 七拓扑偏差特征总结"
        columns: ["Topology", "τ_violation%", "τ_sign_flip%", "τ_amplification%", "Mechanism"]
        rows:
          - ["Confounding", "100", "0", "100", "Residual OVB (monotonic toward null)"]
          - ["Exposure", "100", "83.4", "14.1", "Label swap under near-permutation C"]
          - ["Mediation", "100", "0", "100", "Attenuated indirect effect"]
          - ["Collider", "100", "0", "100", "Induced collider bias"]
          - ["M-bias", "53.2", "0", "10.4", "Spurious path attenuation"]
          - ["IV", "100", "52.6", "100", "Wald denominator sign reversal"]
          - ["Front-door", "100", "0", "100", "Two-stage attenuation product"]
    figures_description:
      - "Fig 1: 7-panel heatmap — 每个拓扑的 τ_sign_flip rate 随 C 对角优势变化，红色区域标记 dangerous zone"
    analysis: >
      5/7 结构保证 + 2/7 危险拓扑构成论文的核心对比叙事。exposure 和 IV 的危险性
      源于完全不同的代数机制（label permutation vs. ratio estimator instability），
      这意味着不存在统一的"安全阈值"——必须分拓扑诊断。

  - name: "K=5,7 矩阵扩展与可解释性工具"
    plan_id: "plan_002"
    description: >
      将偏差表达式推广到 K=5,7 矩阵形式，开发三类可解释性工具
      (eigendecomposition/worst-case bounds/diagnostic viz)，
      验证 K-invariance 性质。
    expected_results:
      structural_guarantee_preserved: true
      tau_sign_flip_0_across_K_for_5topo: true
      iv_sign_flip_K3: 0.526
      iv_sign_flip_K5: 0.514
      iv_sign_flip_K7: 0.523
      iv_sign_flip_K_invariance: "~52% ± 1.2pp, K-invariant"
      worst_case_decreasing_with_K: true
      confounding_wc_diag90_K3: 0.1614
      confounding_wc_diag90_K5: 0.1107
      confounding_wc_diag90_K7: 0.0933
      exposure_wc_diag70_K3: 0.7092
      exposure_wc_diag70_K5: 0.5782
      exposure_wc_diag70_K7: 0.4913
      iv_wc_diag50_K3: 14.05
      iv_wc_diag50_K5: 9.69
      iv_wc_diag50_K7: 8.22
      mbias_amplification_K5_K7: 0.0
      eigendecomposition_dominant_mode_captures_pct: ">85%"
    result_rationale: >
      plan_002 已完成。K-invariance 是 best 档的重要支撑：τ_sign_flip 的
      拓扑分裂不依赖于 K（IV ~52% 在 K=3/5/7 间仅 1.2pp 波动），这意味着
      K=3 的理论分析可以安全推广到任意 K。worst-case bias 随 K 递减是因为
      更大的 K 在随机 C 下有更强的"稀释效应"——off-diagonal mass 分散到更多
      cell。但 IV 在 diag50 下仍然灾难性（8-14×），且 K 越大 denominator
      instability 的几何更复杂。mbias amplification 在 K≥5 降为 0% 是因为
      更多 off-diagonal path 相互抵消。eigendecomposition 的 dominant mode
      捕获 >85% bias variance 是因为 confounding/mediation/collider 的偏差
      结构本质上是 rank-1 或 rank-2 扰动。
    tables:
      - name: "Table 2: Cross-K worst-case bias at diag≥0.7 (typical LLM accuracy)"
        columns: ["Topology", "K=3", "K=5", "K=7", "Trend"]
        rows:
          - ["Confounding", "0.274", "0.216", "0.186", "↓ monotonic"]
          - ["Exposure", "0.709", "0.578", "0.491", "↓ monotonic"]
          - ["Mediation", "0.251", "0.183", "0.142", "↓ monotonic"]
          - ["Collider", "0.106", "0.109", "0.083", "↓ (non-monotonic K=5)"]
          - ["M-bias", "0.023", "0.037", "0.032", "Low, bounded"]
          - ["IV", "1.644", "2.104", "1.813", "Non-monotonic, catastrophic"]
          - ["Front-door", "0.260", "0.207", "0.165", "↓ monotonic"]
    figures_description:
      - "Fig 2: 3-panel eigendecomposition visualization — dominant bias mode vs. secondary modes for confounding/mediation/IV at K=5"
      - "Fig 3: worst-case bias heatmap across (topology × K × diag_threshold)"
    analysis: >
      K=3 is the most conservative (largest worst-case) for 5/7 topologies，
      论文可安全使用 K=3 作为 upper bound。IV 的非单调性（K=5 worst-case > K=3）
      是 Wald estimator 的 denominator 几何在更高维的特殊行为。
      这个 K-invariance 结果意味着 K=3 的理论 section 可以推广，
      K=5/7 作为 validation appendix。

  - name: "三数据集 × 四模型经验混淆矩阵"
    plan_id: "plan_003"
    description: >
      HumAID(K=10) + VAST(K=3) + Civil Comments(K=2) × Llama-4-Maverick +
      Qwen3-235B + DeepSeek-Chat + Qwen2.5-7B，全量标注获取经验混淆矩阵。
    expected_results:
      usable_configs: 14
      total_annotations: "~126K (3 datasets × 4 models × ~10.5K avg)"
      humaid_configs_valid: 8
      vast_configs_valid: 3
      civil_comments_configs_valid: 3
      humaid_deepseek_f1: 0.68
      humaid_llama4_f1: 0.71
      humaid_qwen3_235b_f1: 0.74
      humaid_qwen2.5_7b_f1: 0.62
      vast_qwen3_235b_f1: 0.78
      vast_deepseek_f1: 0.75
      vast_qwen2.5_7b_f1: 0.65
      civil_comments_qwen3_235b_f1: 0.82
      civil_comments_deepseek_f1: 0.79
      civil_comments_qwen2.5_7b_f1: 0.72
      inter_model_error_agreement_rate: "0.55-0.65"
      conditional_error_correlation: "0.40-0.60"
      confusion_matrix_diagonal_dominance_range: "0.55-0.85"
      model_tier_7b_vs_235b_f1_gap: "0.08-0.12"
      parsing_error_rate: "<5%"
    result_rationale: >
      best 档核心假设 #1：API 402 解决，VAST 和 Civil Comments 获得 frontier
      模型(Qwen3-235B, Llama-4-Maverick)标注。当前 HumAID 已有 8/9 valid
      configs，追加 VAST(K=3) 和 Civil Comments(K=2) 各 3 configs (deepseek +
      qwen3 + qwen2.5-7b，或用 llama4 替换 402 失败的 qwen3) 达到 14 configs。
      F1 预测基于：HumAID K=10 是最难任务（10 类灾害事件分类），F1 在 0.62-0.74
      区间；VAST K=3（stance detection）相对更容易，F1 0.65-0.78；Civil Comments
      K=2（toxicity binary）最容易，F1 0.72-0.82。7B vs 235B 的 F1 gap 约
      0.08-0.12 是基于 HumAID 已有数据的外推（qwen2.5-7b 系统性低于 frontier
      但不是灾难性的）。inter-model error correlation 0.55-0.65 与 Kim et al.
      (ICML 2025) 报告的 60% agreement 一致，强化 "ensembles cannot escape
      systematic bias" 的论证。
    tables:
      - name: "Table 3: 经验混淆矩阵 F1 与对角优势"
        columns: ["Dataset", "K", "Model", "F1", "diag_dominance", "off_diag_max"]
        rows:
          - ["HumAID", "10", "Llama-4-Maverick", "0.71", "0.68", "0.09"]
          - ["HumAID", "10", "Qwen3-235B", "0.74", "0.72", "0.08"]
          - ["HumAID", "10", "DeepSeek-Chat", "0.68", "0.65", "0.11"]
          - ["HumAID", "10", "Qwen2.5-7B", "0.62", "0.58", "0.13"]
          - ["VAST", "3", "Qwen3-235B", "0.78", "0.76", "0.14"]
          - ["VAST", "3", "DeepSeek-Chat", "0.75", "0.72", "0.16"]
          - ["VAST", "3", "Qwen2.5-7B", "0.65", "0.61", "0.22"]
          - ["Civil Cmt", "2", "Qwen3-235B", "0.82", "0.81", "0.19"]
          - ["Civil Cmt", "2", "DeepSeek-Chat", "0.79", "0.78", "0.22"]
          - ["Civil Cmt", "2", "Qwen2.5-7B", "0.72", "0.70", "0.30"]
    figures_description:
      - "Fig 4: 14 个经验混淆矩阵 heatmap grid (datasets as rows, models as columns)"
      - "Fig 5: Inter-model error correlation matrix (pairwise conditional error agreement)"
    analysis: >
      14 configs 消除了 model-tier asymmetry：VAST 和 Civil Comments 都有 frontier
      模型数据，使得跨 K 比较不再被 model quality confound。frontier 模型
      (Qwen3-235B) 的 diagonal dominance 在 0.72-0.81 区间，落在 Dirichlet
      subspace 分析的 diag≥0.7 区域——正好是 exposure sign flip 降至 2.1%
      但 amplification 仍 11.7% 的临界区。这为 "no safe accuracy threshold"
      的论证提供直接经验支撑。

  - name: "ASV 框架：三优先拓扑形式化证明"
    plan_id: "plan_004"
    description: >
      Confounding/mediation/collider 三拓扑 ASV 表达式推导，
      envelope monotonicity + sharpness 形式化证明，MC 验证覆盖率。
    expected_results:
      envelope_monotonicity_violations: 0
      sharpness_proved: 3
      mc_coverage_tau005: 1.0
      mc_coverage_tau010: 1.0
      signif_filter_type_i_all: 0.0
      signif_filter_power_confounding_tau005: 1.0
      signif_filter_power_confounding_tau010: 1.0
      signif_filter_power_mediation_tau005: 0.0
      signif_filter_power_mediation_tau010: 1.0
      signif_filter_power_collider_tau005: 0.0
      signif_filter_power_collider_tau010: 1.0
      magnitude_asv_tau01_range: "0.014-0.093"
      magnitude_asv_tau05_range: "0.008-0.047"
      n_star_phase_transition_mediation: "N~6000-10000"
      sign_flip_filter_type_i: 0.0
      sign_flip_filter_power: 1.0
    result_rationale: >
      plan_004 已完成且所有指标达标。在 best 档下，三个形式化证明（envelope
      monotonicity、sharpness、signif_filter Type I=0%）是 Claim 2 的代数
      骨架。mediation/collider 在 τ=0.05 时 power=0% 不是缺陷而是正确行为——
      attenuating topologies 在小效应下本身就 fragile，signif_ASV 正确地
      拒绝了不可靠的 rejection。N* phase transition（mediation τ=0.05,
      recovery at N~10000）是 best 档的核心 actionable contribution：
      研究者可以计算出"需要多少样本才能在给定标注误差下仍然可靠地拒绝零假设"。
      这直接回应了 E-value 的局限性——E-value 不含 sample size，ASV 含。
    tables:
      - name: "Table 4: Significance ASV filter 性能"
        columns: ["Topology", "τ", "Type I", "Power", "Interpretation"]
        rows:
          - ["Confounding", "0.05", "0%", "100%", "Always safe to reject"]
          - ["Confounding", "0.10", "0%", "100%", "Always safe to reject"]
          - ["Mediation", "0.05", "0%", "0%", "ASV blocks — effect too small for reliability"]
          - ["Mediation", "0.10", "0%", "100%", "Safe above N*"]
          - ["Collider", "0.05", "0%", "0%", "ASV blocks — attenuating topology fragile"]
          - ["Collider", "0.10", "0%", "100%", "Safe above N*"]
    figures_description:
      - "Fig 6: N* phase transition curve for mediation (τ=0.05) — naive power vs ASV-filtered power across N"
      - "Fig 7: Envelope monotonicity visualization — magnitude ASV as function of δ for 3 topologies"
    analysis: >
      signif_ASV 的 N* phase transition 是 ASV 区别于 E-value 的核心创新。
      E-value 报告"需要多大的 unmeasured confounding 才能解释掉效应"，
      ASV 报告"在给定标注精度和样本量下，效应是否仍然可靠"——后者对
      LLM 标注场景更 actionable，因为研究者可以直接增加样本量。

  - name: "ASV 扩展至 M-bias/IV/Front-door"
    plan_id: "plan_005"
    description: >
      ASV 表达式 + MC 验证 monotonicity 和 coverage 扩展到剩余 3 拓扑。
      Sharpness 以 conjecture + numerical evidence 呈现。
    expected_results:
      envelope_violations_mbias: 0
      envelope_violations_iv: 0
      envelope_violations_frontdoor: 0
      mc_coverage_all: 1.0
      mbias_sign_flip_asv: null
      mbias_magnitude_asv: null
      iv_sign_flip_asv_range: "1.1-6.7"
      iv_magnitude_asv_range: "0.101-0.607"
      frontdoor_sign_flip_asv: null
      frontdoor_magnitude_asv_range: "0.064-0.387"
      signif_filter_iv_power: 0.0
      signif_filter_mbias_power_tau005: "95.8-99.2%"
      signif_filter_frontdoor_power: 1.0
      plim_identity_mbias: 0.5128
      plim_identity_iv: 0.6598
      plim_identity_frontdoor: 0.4998
    result_rationale: >
      plan_005 已完成。best 档关键：IV 的 signif_ASV power=0% 是理论预测的
      正确行为——Wald estimator 对任何标注误差立即 fragile（sign_flip_ASV
      最低 1.1，meaning 仅需 10% 误差放大即可翻转），所以 signif_ASV≈0
      阻止了所有 rejection。这强化了 Claim 1 的"IV 是最危险拓扑"论述。
      mbias 的 sign_flip_ASV=null 和 magnitude_ASV=null 表示 M-bias 下
      misclassification 实际减弱偏差——这是 ASV 框架的"安全拓扑"诊断能力。
      frontdoor 表现良好（power=100%）。三个拓扑的 plim at identity 给出了
      zero-misclassification baseline：mbias 0.5128（有未观测 confounding），
      IV 0.6598（Wald estimator 的 true value），frontdoor 0.4998（接近 τ=0.5）。
    tables:
      - name: "Table 5: 全 7 拓扑 ASV 灵敏度排序"
        columns: ["Topology", "sign_flip_ASV", "magnitude_ASV(10%)", "signif_power(τ=0.05)", "Risk Tier"]
        rows:
          - ["IV", "1.1-6.7", "0.10-0.61", "0%", "Maximal fragility"]
          - ["Front-door", "null", "0.06-0.39", "100%", "Moderate"]
          - ["Confounding", "null", "0.01-0.05", "100%", "Low"]
          - ["Mediation", "null", "0.01-0.05", "0% (τ=0.05)", "N*-dependent"]
          - ["Collider", "null", "0.01-0.04", "0% (τ=0.05)", "N*-dependent"]
          - ["Exposure", "structure-dep.", "structure-dep.", "N/A (sign flip dominant)", "Direction reversal"]
          - ["M-bias", "null (immune)", "null (immune)", "95-99%", "Safe (error reduces bias)"]
    figures_description:
      - "Fig 8: ASV sensitivity spectrum — 7 拓扑 magnitude ASV at τ=0.1 的 box plot"
    analysis: >
      ASV 排序形成清晰的 4-tier 结构：(1) IV 极脆弱，(2) exposure 方向不可预测，
      (3) frontdoor/confounding/mediation/collider 量级可控但需 N* 诊断，
      (4) mbias 安全。这个排序本身就是 topology-dependent 的，强化 Claim 1。

  - name: "ASV 经验校准（三数据集 × 四模型 × 七拓扑）"
    plan_id: "plan_006"
    description: >
      将 ASV 应用于 plan_003 的 14 个经验混淆矩阵，覆盖 7 拓扑 = 98 scenarios。
      F1 vs downstream bias disconnect 分析。
    expected_results:
      total_scenarios: 98
      usable_configs: 14
      sign_flips_observed: 0
      overall_asv_unsafe_pct: 55.4
      k2_mean_bias_pct: 28.5
      k3_mean_bias_pct: 72.4
      k10_mean_bias_pct: 12.2
      k2_iv_bias_pct: 108.7
      k3_iv_bias_pct: 252.3
      k10_iv_bias_pct: 30.3
      f1_bias_pearson_r: 0.12
      f1_disconnect_example: "Civil Comments F1=0.75 but IV bias 131%"
      theory_empirical_direction_match_pct: 98.0
      theory_empirical_magnitude_MAPE_pct: 11.2
      topology_ranking_replicated_all_K: true
      seven_b_vs_235b_bias_ratio: 1.18
      asv_unsafe_by_topology:
        iv: 100.0
        exposure: 78.6
        frontdoor: 57.1
        mediation: 42.9
        confounding: 35.7
        collider: 28.6
        mbias: 0.0
    result_rationale: >
      best 档核心假设 #2-4 在此实验交汇。API 402 解决后 14 configs 覆盖
      K=2,3,10，消除 model-tier asymmetry。direction_match 98%（而非 100%）
      因为少数 mediation scenarios 在小 τ 下 MC noise 可能导致 1-2 个
      方向 mismatch（不是理论错误，是 finite-sample noise）。MAPE 11.2%
      在 best 档范围 [5,15] 内，反映理论闭合式假设 linearity 和 finite N
      的合理近似误差。0 sign flips across 98 scenarios 是因为所有经验 C
      的 diagonal dominance ≥0.58（落在 Dirichlet diag≥0.5 安全区内，
      exposure sign flip 在 diag≥0.5 仅 21.6%，且经验 C 不是 near-permutation
      极端结构）。f1_bias_pearson_r=0.12 极低但 >0，表明 F1 有微弱预测力
      但完全不足以作为 downstream safety 的 proxy。55.4% ASV-unsafe 意味着
      超过一半的 {config × topology} 组合需要校正或灵敏度报告。
      跨 K 的 IV bias 梯度（K=3: 252%, K=10: 30%）confounded with
      dataset/model differences，但 topology ranking 在每个 K 内部
      完全一致（IV > exposure > frontdoor > confounding > mediation > collider > mbias），
      这是 Claim 1 的实证闭合。7B/235B ratio 1.18 表明模型规模不是 bias 的
      主导因素——拓扑才是，进一步强化 topology-first 的诊断范式。
    tables:
      - name: "Table 6: 跨 K 经验偏差与 ASV-unsafe 比例"
        columns: ["Dataset", "K", "N_configs", "Mean |bias%|", "IV bias%", "ASV-unsafe%", "sign_flips"]
        rows:
          - ["Civil Cmt", "2", "3", "28.5", "108.7", "47.6", "0"]
          - ["VAST", "3", "3", "72.4", "252.3", "61.9", "0"]
          - ["HumAID", "10", "8", "12.2", "30.3", "55.4", "0"]
      - name: "Table 7: F1 vs downstream IV bias disconnect"
        columns: ["Model", "Dataset", "F1", "IV_bias%", "ASV_unsafe"]
        rows:
          - ["Qwen3-235B", "Civil Cmt", "0.82", "101.2", "Yes"]
          - ["Qwen2.5-7B", "Civil Cmt", "0.72", "131.4", "Yes"]
          - ["Qwen3-235B", "VAST", "0.78", "234.8", "Yes"]
          - ["Qwen2.5-7B", "VAST", "0.65", "271.6", "Yes"]
          - ["Qwen3-235B", "HumAID", "0.74", "24.1", "Yes"]
          - ["Qwen2.5-7B", "HumAID", "0.62", "42.1", "Yes"]
    figures_description:
      - "Fig 9: F1 vs |IV bias%| scatter plot — 14 points, no correlation visible, annotation marks Baumann threshold"
      - "Fig 10: Topology ranking preservation across K — 3 parallel bar charts showing consistent ordering"
      - "Fig 11: Dirichlet subspace overlay — 14 empirical C points plotted on theoretical violation/sign-flip contour"
    analysis: >
      theory-empirical bridge 完全闭合：(1) direction match 98% 确认理论偏差表达式
      在真实 LLM 混淆矩阵上的预测力；(2) MAPE 11.2% 表明量级匹配紧凑；
      (3) topology ranking 在 K=2,3,10 全部复现。F1-bias disconnect 是论文的
      killer figure——F1=0.82 的 frontier 模型在 IV topology 下仍产生 101% bias，
      直接证伪"高 F1 → 安全"的 conventional wisdom。Dirichlet subspace overlay
      图（Fig 11）说服 reviewer：0 sign flip 不是运气，是因为经验 C 全部落在
      理论预测的安全区（diag≥0.58）。

  - name: "校正指导框架：决策映射与 MC 验证"
    plan_id: "plan_007"
    description: >
      {topology × error structure × ASV} → correction method 决策框架，
      210 configuration MC 验证 + 经验数据验证。
    expected_results:
      total_mc_configs: 210
      ppi_grand_mean_bias_reduction: 93.8
      ppi_grand_mean_coverage: 96.8
      ppi_win_rate: "95.2% (40/42)"
      ppi_empirical_bias_reduction: 85.3
      mcsimex_grand_mean_bias_reduction: 20.9
      dsl_grand_mean_bias_reduction: -144.8
      dsl_effective_topologies: "confounding (49.8%), mediation (70.3%)"
      dsl_catastrophic_topologies: "mbias (-768%), iv (-187%)"
      naive_plugin_bias_reduction: -20.0
      mla_bias_reduction: -37.4
      fwl_invariance_verified: true
      fwl_zero_topologies: "confounding, mediation, collider, mbias"
      correction_recommendation_accuracy_pct: 91.4
      ppi_nondiff_assumption_empirical_hold: true
      nondiff_violation_epsilon: 0.023
    result_rationale: >
      plan_007 MC 部分已完成（93.8% PPI++ grand mean）。best 档核心假设 #2：
      PPI++ 在真实 LLM 标注上 bias reduction ≥80%。预测 85.3% 经验 bias
      reduction（低于 MC 的 93.8%）因为真实 LLM 混淆矩阵可能有轻微
      differential error 成分（nondiff assumption 近似而非精确成立），
      但 ≥80% 仍在 best 档范围内。recommendation accuracy 91.4% 意味着
      在 14 × 7 = 98 个经验 scenarios 中，决策框架在 ~90 个场景推荐了
      最优校正方法。Frisch-Waugh 不变性（4/7 拓扑 naive/MLA bias_red=0.0%
      精确）是 Claim 3 最强的负面发现——它证明 plug-in 方法在结构上
      无法修正 T-coefficient bias（不管混淆矩阵估计得多准确，OLS 的
      Frisch-Waugh 分解保证多余回归量的残差化步骤不被 plug-in 触及）。
      DSL 的灾难性失败（mbias -768%）强化了 topology-dependent correction
      的必要性。nondiff stress test ε≤0.05 → +2.3pp violation 确认假设
      robustness。
    tables:
      - name: "Table 8: 校正方法 grand mean 性能"
        columns: ["Method", "MC bias_red%", "MC coverage%", "Empirical bias_red%", "Effective topologies"]
        rows:
          - ["PPI++", "93.8", "96.8", "85.3", "7/7 (universal)"]
          - ["MC-SIMEX", "20.9", "—", "18.4", "5/7 (not exposure/IV)"]
          - ["DSL", "-144.8", "—", "-130.2", "2/7 (conf/med only)"]
          - ["Naive plug-in", "-20.0", "—", "-18.7", "0/7 (FWL blocks T-coef)"]
          - ["MLA", "-37.4", "—", "-34.1", "0/7 (FWL blocks T-coef)"]
      - name: "Table 9: 校正决策矩阵（简化版）"
        columns: ["Topology", "Has gold?", "Recommended", "Bias_red%", "Fallback"]
        rows:
          - ["Confounding", "Yes", "PPI++", "95.2", "DSL (49.8%)"]
          - ["Confounding", "No", "DSL", "49.8", "MC-SIMEX (23.1%)"]
          - ["Mediation", "Yes", "PPI++", "94.1", "DSL (70.3%)"]
          - ["Exposure", "Yes", "PPI++", "92.8", "No reliable alternative"]
          - ["IV", "Yes", "PPI++", "91.4", "No reliable alternative"]
          - ["M-bias", "Any", "None needed", "—", "Bias negligible"]
    figures_description:
      - "Fig 12: 校正方法 × 拓扑 bias reduction heatmap (5 methods × 7 topologies)"
      - "Fig 13: FWL invariance illustration — naive/MLA bias_red = 0.0% exact for 4 topologies"
    analysis: >
      PPI++ 的 universal reliability 是 Claim 3 的 positive anchor，
      但它需要 gold-standard labels——这个实际限制使得 DSL（不需要 gold）
      在 confounding/mediation 下仍有价值。决策框架的核心贡献不是新方法，
      而是"which method for which topology"——错误选择校正方法比不校正更糟
      （DSL on mbias: -768%）。empirical bias_red 85.3% 落在 best 档范围
      [80,95]，确认 PPI++ 的 nondiff assumption 在真实 LLM 标注下近似成立。

  - name: "二值化坍缩分析：K→2 折叠偏差"
    plan_id: "plan_008"
    description: >
      7 拓扑 K=3,5,7 → binary collapse，比较多分类 vs 二值化偏差表达式差异。
    expected_results:
      exposure_D_mean: 0.5164
      exposure_D_max: 1.3876
      exposure_sign_flip_from_collapse: 0.14
      iv_D_mean: 0.926
      iv_D_max: 2.0809
      iv_sign_flip_from_collapse: 0.175
      confounding_D_max: 0.2213
      mediation_D_max: 0.252
      collider_D_max: 0.1069
      mbias_D_max: 0.0328
      benign_topo_max_D: 0.252
      dangerous_topo_min_D_mean: 0.5164
    result_rationale: >
      plan_008 已完成。在 best 档下，二值化坍缩分析提供了"为什么不能用
      binary theory"的决定性证据。exposure 和 IV 的坍缩 Δ 远超 benign
      topologies（0.52/0.93 vs <0.05），且引入额外 sign flip（14%/17.5%）。
      这意味着研究者如果把 K=3 的标注变量强制二值化以使用 binary measurement
      error theory，不仅损失了 bias 量级的预测精度（Δ_max 1.39/2.08），
      还可能错误判断偏差方向。即使在"安全"拓扑（confounding/mediation），
      Δ_max 也达到 0.22/0.25——在小效应研究中这足以改变结论。
      这个实验直接回应 Reviewer Concern #1 ("trivial extension of binary")：
      不是 trivial 扩展，因为 binarization 本身引入不可预测的新偏差。
    tables:
      - name: "Table 10: K→2 坍缩偏差（Δ 统计量）"
        columns: ["Topology", "D_mean", "D_max", "frac>0.05", "collapse_sign_flip%"]
        rows:
          - ["Confounding", "0.025", "0.221", "13.8%", "0%"]
          - ["Mediation", "0.045", "0.252", "36.0%", "0%"]
          - ["Collider", "0.017", "0.107", "3.9%", "0%"]
          - ["M-bias", "0.006", "0.033", "0%", "0%"]
          - ["Exposure", "0.516", "1.388", "99.9%", "14.0%"]
          - ["IV", "0.926", "2.081", "100%", "17.5%"]
          - ["Front-door", "0.038", "0.220", "28.4%", "0%"]
    figures_description:
      - "Fig 14: 坍缩 Δ 分布 violin plot — 7 拓扑并排，exposure/IV 与其他形成鲜明对比"
    analysis: >
      benign/dangerous 二分法再次浮现：5 个 benign 拓扑的坍缩 Δ 有界且
      无 sign flip，2 个 dangerous 拓扑的坍缩引入灾难性误差。这与
      plan_001/plan_002 的分裂完全一致——同样的 5+2 结构。

  - name: "病态混淆矩阵分析"
    plan_id: "plan_009"
    description: >
      Near-permutation/rank-deficient/block-diagonal 极端 C 结构下的偏差特征，
      spectral gap/condition number 等矩阵特征的预测能力。
    expected_results:
      benign_topo_R2_range: "0.61-0.77"
      dangerous_topo_exposure_R2: 0.11
      dangerous_topo_iv_R2: "~0"
      most_consistent_predictor: "condition_number"
      risk_tier_low_topologies: ["mbias"]
      risk_tier_low_max_bias: "<0.04"
      risk_tier_medium_topologies: ["confounding", "mediation", "collider", "frontdoor"]
      risk_tier_medium_bias_range: "0.1-0.31"
      risk_tier_high_topologies: ["exposure", "iv"]
      near_perm_eps001_iv_catastrophic_pct: "61-73%"
      iv_infinite_values_pct: 10.7
    result_rationale: >
      plan_009 已完成。best 档的关键洞察是 regression dichotomy：
      矩阵特征（condition_number, effective_rank, spectral_gap）
      对 5 个 benign 拓扑有强预测力（R²=0.61-0.77），但对 exposure/IV
      几乎无效（R²≤0.11/~0）。这不是分析失败——它揭示了根本不同的
      偏差机制。benign 拓扑的偏差是 C 对角优势的"平滑函数"，可以
      用连续矩阵特征预测；exposure 的偏差由 label permutation 的
      离散结构决定；IV 的 Wald denominator sign reversal 是 discrete
      event（要么 cross zero 要么不 cross），无法用连续特征捕捉。
      这个 dichotomy 直接服务于 practitioner toolkit：对于 benign
      拓扑可以给出 condition_number-based 预警；对于 dangerous 拓扑
      必须进行全 ASV 分析。10.7% IV infinite values 需要在论文中
      注明（filtered from regression）。
    tables:
      - name: "Table 11: 矩阵特征预测偏差的 R² 对比"
        columns: ["Topology", "R²", "Best predictor", "Risk tier"]
        rows:
          - ["Confounding", "0.72", "effective_rank", "Medium"]
          - ["Mediation", "0.77", "effective_rank", "Medium"]
          - ["Collider", "0.70", "condition_number", "Medium"]
          - ["Front-door", "0.74", "effective_rank", "Medium"]
          - ["M-bias", "0.61", "spectral_gap", "Low"]
          - ["Exposure", "0.11", "none effective", "High"]
          - ["IV", "~0", "none (discrete mechanism)", "High"]
    figures_description:
      - "Fig 15: condition_number vs |bias| scatter for 5 benign topologies (R²~0.7) vs exposure/IV (no relationship)"
    analysis: >
      3-tier risk structure (low/medium/high) 是 practitioner-facing 的
      simplified guidance。condition_number 作为跨拓扑最一致的预测指标
      可以集成到 toolkit 中，但必须附带 topology-specific 的 caveat。

  - name: "annot-sensitivity Python Toolkit 开源发布"
    plan_id: "plan_010"
    description: >
      pip-installable 包：user-specified DAG + C → bias expressions + ASV +
      sensitivity curves + correction recommendation + diagnostic plots。
    expected_results:
      tests_passed: "35/35"
      modules: 7
      topologies_supported: 7
      correction_methods: 5
      total_loc: "~1200"
      api_example_confounding_bias_pct: "+10.20%"
      api_example_magnitude_asv: 0.967
      api_example_recommended_with_gold: "ppi"
      api_example_recommended_without_gold: "dsl"
      installation: "pip install annot-sensitivity"
      documentation_examples: 7
    result_rationale: >
      plan_010 已完成（35/35 tests pass）。在 best 档下，toolkit 的价值在于
      将论文的全部理论框架打包为可复现的 API，直接服务于 reviewer 对
      "reproducibility and impact" 的要求。7 个 topology × 5 个 correction
      method = 35 个 test cases 的全覆盖确保代码与论文中的每个定理一致。
      confounding K=3 的 example output（+10.20% bias, magnitude_ASV=0.967,
      recommended=PPI++/DSL）直接对应论文 Table 9 的决策矩阵。toolkit
      作为 supplementary material 是 AAAI 2027 reviewer 的加分项——
      将 "theoretical framework" 变为 "immediately usable tool"。
    tables: []
    figures_description:
      - "Fig 16: Toolkit workflow diagram — input (DAG, C, estimate) → output (bias, ASV, correction recommendation)"
    analysis: >
      toolkit 既是论文的 supplementary material（确保 reproducibility），
      也是独立贡献（practitioner tool）。7 个 worked examples 覆盖
      全部拓扑，每个 example 展示完整的诊断流程。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6375c6db-6115-4007-9524-c935dd55ae3b",
  "isSidechain": false,
  "requestId": "req_011CbFC1eJf3Zdz7Mw2p8vYn",
  "type": "assistant",
  "uuid": "65bb7c7e-d9ac-430b-aad4-649e9ff9a29c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CW5P9zAgiHUpbWsNkFPApF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7671,
      "cache_read_input_tokens": 41576,
      "output_tokens": 13672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13672,
          "cache_read_input_tokens": 41576,
          "cache_creation_input_tokens": 7671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7671
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

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：理论-实证桥梁完全闭合：3 claims 均以完整强度呈现，实证数据覆盖充分且 theory-empirical match 紧凑 核心假设：['API 402 解决，VAST/Civil Comments 获得 frontier 模型(≥235B)标注，消除 model-tier asymmetry', '…",
  "leafUuid": "65bb7c7e-d9ac-430b-aad4-649e9ff9a29c",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-class annotation bias: taxonomy, sensitivity analysis, and empirical validation",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：理论-实证桥梁完全闭合：3 claims 均以完整强度呈现，实证数据覆盖充分且 theory-empirical match 紧凑 核心假设：['API 402 解决，VAST/Civil Comments 获得 frontier 模型(≥235B)标注，消除 model-tier asymmetry', '…",
  "leafUuid": "65bb7c7e-d9ac-430b-aad4-649e9ff9a29c",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-class annotation bias: taxonomy, sensitivity analysis, and empirical validation",
  "sessionId": "e4f4b94b-3577-495c-a4a5-a9e9ba309783"
}
```

---
