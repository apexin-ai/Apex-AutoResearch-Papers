# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/82f0607d-78c0-438f-b491-5c125e51ad8b.jsonl`
- **Structured JSON:** [`ef1742738c0fad6a5cb1.json`](../../sessions/ef/ef1742738c0fad6a5cb1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T05:45:38.893Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T05:45:38.893Z",
  "sessionId": "82f0607d-78c0-438f-b491-5c125e51ad8b",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: causal_annot_error_attrib\nvenue: emnlp-2026\nfocus: Post-fix re-dream: all 5 structural issues resolved. Related work +5 refs, ASV vs PBA, Brenner footnote, IV subspace appendix, nondiff stress test appendix+limitations.\n\n## paper_framing.md\n\n# Paper Framing — causal_annot_error_attrib\n\n## Target Venue\n- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)\n- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)\n- Tertiary: ICWSM 2027 Round 2 (2026-09-15)\n\n## Title\nMulti-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies\n\n## Core Claims (3 条)\n\n1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 7 canonical social-science DAG topologies (confounding, exposure, mediation, collider, M-bias, instrument, front-door).\n\n2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of annotation error amplification needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Three complementary ASV types — magnitude (E-value-style robustness reporting, all topologies), significance (hypothesis testing filter, effective for attenuating topologies), and sign-flip (direction reversal warning, primarily exposure DAG) — because no single sensitivity metric suffices across all causal designs. The choice of appropriate ASV type is itself topology-dependent, reinforcing Claim 1. ASVs reveal a striking sensitivity ranking: IV estimates are maximally fragile (any annotation error exceeds threshold), while M-bias is immune (misclassification actually reduces spurious associations). Unlike E-values, ASVs incorporate study precision (sample-dependent), providing actionable guidance: for a given τ and σ, the critical sample size N* is analytically computable. Formal proofs (envelope monotonicity + sharpness) for 3 priority topologies; MC-validated for all 7.\n\n3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI++, MLA, MC-SIMEX, naive plug-in). Key findings from 210-configuration MC validation (7 topo × 6 C × 5 methods × 1000 sims): (a) Frisch-Waugh theorem makes naive_plugin/MLA fundamentally ineffective for T-coefficient bias in 4/7 topologies (bias reduction = 0.0%, exact); (b) DSL is topology-limited — effective only for confounding (50%) and mediation (70%), catastrophically harmful elsewhere (mbias -768%, IV -187%); (c) PPI++ is the only universally reliable method (93.8% grand mean bias reduction, 96.8% coverage) but requires gold-standard labels; (d) correction method effectiveness is itself topology-dependent, reinforcing Claim 1. Dependence-aware multi-LLM correction remains an open problem.\n\n## Story Spine\n\n- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31–50% of downstream conclusions are already incorrect — critically, even annotators with F1 > 0.93 produce > 50% error risk in downstream causal estimates. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable. The field's reliance on classification F1 as a proxy for downstream validity is fundamentally broken; our framework provides the missing link from annotation quality metrics to causal estimate reliability.\n\n- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.\n\n- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.\n\n- **Headline result template**: \"Across 7 DAG topologies with K=3, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. ASVs reveal a striking sensitivity spectrum: IV estimates are maximally fragile (any annotation error exceeds robustness thresholds), while M-bias associations are immune (misclassification reduces spurious bias). Empirical validation on 3 CSS tasks (K=2, 3, 10) annotated by 4 LLMs confirms the theoretical predictions: IV bias ranges from 30% at K=10 to 252% at K=3 across annotation settings, F1 does not predict downstream safety (F1=0.72 but IV bias>100%), and 55.4% of HumAID scenarios are ASV-unsafe, requiring correction or sensitivity reporting.\"\n\n## Core Insight (Lead Finding) — DUAL VERSION, gate on plan_001\n\n### Version A (≥1 topology shows direction reversal under K≥3 non-differential exposure misclassification)\nThe binary guarantee that \"non-differential exposure misclassification biases toward the null\" (Bross 1954) breaks in the multi-class case. For specific confusion matrix structures in specific DAG topologies, K≥3 non-differential error can amplify or reverse effect estimates. Brenner (1993) identified this possibility for polytomous confounder misclassification (\"bias can go in either direction\"); we provide the first systematic characterization across 7 DAG topologies with exact conditions for each {C structure × topology} cell. Furthermore, binarizing a K-class variable to \"escape\" into the binary regime is itself hazardous — collapsing introduces new, direction-unpredictable bias (MVP evidence: Δ up to 0.103).\n\n### Version B (no direction reversal found across topologies)\nMulti-class annotation error is structurally irreducible to the binary case: the downstream bias magnitude depends on the full K×K confusion matrix in ways that binary sensitivity/specificity cannot predict, and binarizing a K-class variable introduces new bias (MVP evidence: Δ up to 0.103). While non-differential error preserves bias direction across tested topologies (a useful practitioners' guarantee), the magnitude varies dramatically with confusion matrix structure (0.13–0.30 in confounding DAG alone), and this variation is topology-dependent. ASVs provide the missing robustness measure for this quantitative — not directional — uncertainty.\n\n**Gate**: RESOLVED → Version A. Two topologies show τ-specific direction reversal: exposure (~83-100% sign flip) and IV (~52% sign flip, Wald denominator mechanism). 5/7 topologies have structural guarantee τ_sign_flip=0% across K={3,5,7}. See D003, D004, D010.\n\n## MVP Evidence\n\n**Confounding DAG + K=3** (confounder misclassification):\n- Theoretical bias expressions match MC perfectly (6/6 structures within 95% CI) — framework validated\n- Binary collapse ≠ multi-class: Δ up to 0.103 (near-permutation C), proving K=3 retains more confounding control than binarization\n- 100k random C search: confounding DAG bias is monotonically toward OVB — this topology is \"well-behaved\" (predictable direction)\n- NOTE: Confounding DAG tests residual confounding, NOT bias-toward-null (Bross 1954). Criterion 2 (away-from-null bias) holds for binary too in this topology. See M001.\n\n**Exposure DAG K=3** (exposure misclassification — D002/D004 CONFIRMED):\n- 100k random C: 85% violate bias-toward-null, 83.4% sign reversal, 14.1% amplification\n- K=2 control: 6/6 toward null (binary guarantee holds)\n- Worst case: β₁=1.0 → γ̂₁=-0.84 (sign reversal, 0.84× magnitude); β₂=-0.5 → γ̂₂=-1.41 (2.83× amplification)\n- Mechanism: near-permutation C causes label swap → effect direction flips (structurally impossible in K=2)\n- **Two-DAG contrast**: confounding (monotonic, predictable) vs exposure (unpredictable, topology-dependent) — validates core claim\n\n**Dirichlet subspace analysis** (practical relevance validation):\n- diag≥0.5: 32.5% violation, 21.6% sign reversal, 11.3% amplification\n- diag≥0.7 (typical LLM accuracy): **13.7% violation**, 2.1% sign reversal, **11.7% amplification**\n- diag≥0.9 (high-accuracy LLM): **11.9% violation**, 0% sign reversal, **11.9% amplification**\n- Key pattern: sign reversal vanishes at high accuracy, but **amplification persists at ~12% regardless of accuracy**\n- Implication: even 90%+ accuracy LLMs face non-trivial effect amplification risk — no \"safe accuracy threshold\" exists\n\n**IV Dirichlet subspace analysis** (Dream feedback, 2026-05-21):\n- Full: 100% violation, 51.7% sign flip, 48.3% amplification\n- diag≥0.5: 100% violation, **0% sign flip**, 100% amplification, worst 28.6×\n- diag≥0.7: 100% violation, 0% sign flip, 100% amplification, worst 2.4×\n- diag≥0.9: 100% violation, 0% sign flip, 100% amplification, worst 1.2×\n- Key contrast with exposure: IV sign flip vanishes at diag≥0.5 (exposure persists at 2.1% at diag≥0.7), but IV amplification is **universal** (100% at all thresholds, vs exposure 11.7% at diag≥0.7)\n- Mechanism: Wald denominator monotonically contracts; diagonal dominance prevents zero-crossing (no sign flip) but not contraction (amplification)\n\n## Venue Fit Risks\n\n- **AAAI**: Broad AI audience — emphasize general methodology for \"automated annotation measurement error,\" not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.\n- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.\n- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n1. **\"Trivial extension of binary to multi-class\"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 7 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]\n\n2. **\"Lee & Wood-Doughty (2024) already did categorical\"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 7 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]\n\n3. **\"Why these 7 DAG topologies?\"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: exposure (treatment), confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]\n\n4. **\"K≥5 expressions aren't actionable\"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]\n\n5. **\"ASV sharpness only proved for 3 topologies\"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]\n\n6. **\"Correlated multi-LLM errors?\"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]\n\n7. **\"Empirical validation scope\"** → 3 CSS tasks (HumAID K=10, VAST K=3, Civil Comments K=2) × 4 LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat, Qwen2.5-7B) × 7 topologies = 14 configs. D016 confirms: topology ranking matches theory across all K values; IV bias co-varies with annotation setting (K=3 IV bias 252% vs K=10 30%, confounded with dataset/model differences); 7B vs 235B bias ratio 1.24 (model scale not dominant). 0 sign flips across all 98 scenarios. Note: VAST/Civil Comments use 7B local model (API 402 blocker), creating a model-tier asymmetry acknowledged in Limitations. [Experiments: plan_003, plan_006]\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: Derive and MC-validate bias expressions for 6 DAG topologies with K=3\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: plan001_dag_taxonomy\n  details: 'For each topology (confounding, mediation, collider, M-bias, instrument,\n    front-door): derive closed-form K=3 bias expression, validate with MC (1000 reps\n    × N=10000, 6 confusion matrix structures including near-permutation extreme).\n    Key question: which topologies show direction reversal under non-differential\n    error? Confounding already validated in MVP (no reversal, monotonic toward OVB).\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    collider:\n      all_coef:\n        violation: 1\n        sign_flip: 0.688\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 0\n      small_tau_0.05:\n        tau_I: 0.015733\n        tau_violation: 0.96\n        tau_sign_flip: 0\n        tau_amplification: 0.992\n      small_tau_0.1:\n        tau_I: 0.06118\n        tau_violation: 0.974\n        tau_sign_flip: 0\n        tau_amplification: 0.995\n    mbias:\n      all_coef:\n        violation: 1\n        sign_flip: 0.651\n        amplification: 0.112\n      tau_specific:\n        violation: 0.532\n        sign_flip: 0\n        amplification: 0.104\n      misclass_amplifies_rate: 0.292\n      small_tau_0.05:\n        tau_I: 0.057669\n        tau_violation: 0.532\n        tau_sign_flip: 0\n        tau_amplification: 0.104\n      small_tau_0.1:\n        tau_I: 0.107669\n        tau_violation: 0.532\n        tau_sign_flip: 0\n        tau_amplification: 0.104\n    mediation_mixed:\n      all_coef:\n        violation: 1\n        sign_flip: 0.835\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    mediation_same:\n      all_coef:\n        violation: 1\n        sign_flip: 0.666\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    frontdoor_mixed:\n      all_coef:\n        violation: 1\n        sign_flip: 0.998\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_I: 0.050177\n        lambda_U: 0.1\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_I: 0.100169\n        lambda_U: 0.2\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    frontdoor_same:\n      all_coef:\n        violation: 1\n        sign_flip: 1\n        amplification: 1\n      tau_specific:\n        violation: 0.999\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 0.9997\n      small_tau_0.05:\n        tau_I: 0.050177\n        lambda_U: 0.1\n        tau_violation: 0.999\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_I: 0.100169\n        lambda_U: 0.2\n        tau_violation: 0.999\n        tau_sign_flip: 0\n        tau_amplification: 1\n    iv_note: 'IV metrics not computed in plan_001 (only 6 fixed C structures tested,\n      no dedicated IV tau_specific analysis). First measured in plan_002: 52% tau_specific_sign_flip\n      from 100k random C (Wald denominator sign reversal). See plan002_k57_extension\n      for full IV results.'\n- id: plan_002\n  claim: 1\n  description: Extend bias expressions to K=5,7 — matrix notation + interpretability\n    tools\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: plan002_k57_extension\n  details: 'Matrix-form expressions for general K. Three interpretability tools: (a)\n    eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar\n    bounds collapsing matrix to conservative scalar, (c) diagnostic visualizations\n    mapping confusion matrix regions to bias magnitude. Validate on confounding +\n    mediation + collider DAGs with K=5,7.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_k_comparison_7topo:\n      confounding:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.993\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1614\n          worst_case_diag70: 0.2744\n          worst_case_diag50: 0.2993\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1107\n          worst_case_diag70: 0.2156\n          worst_case_diag50: 0.2462\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0933\n          worst_case_diag70: 0.1859\n          worst_case_diag50: 0.2264\n      mediation:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.838\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1223\n          worst_case_diag70: 0.251\n          worst_case_diag50: 0.3032\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.966\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0867\n          worst_case_diag70: 0.1832\n          worst_case_diag50: 0.2396\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0607\n          worst_case_diag70: 0.1421\n          worst_case_diag50: 0.1879\n      collider:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.666\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0503\n          worst_case_diag70: 0.1064\n          worst_case_diag50: 0.1256\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.955\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0477\n          worst_case_diag70: 0.1087\n          worst_case_diag50: 0.1306\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.992\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0352\n          worst_case_diag70: 0.0826\n          worst_case_diag50: 0.1131\n      exposure:\n        K3:\n          tau_specific_sign_flip: N/A (all-coef fallback; MVP beta1 flip=83.4%)\n          all_coef_sign_flip: 0.99\n          violation: 1\n          amplification: 0.999\n          worst_case_diag90: 0.2726\n          worst_case_diag70: 0.7092\n          worst_case_diag50: 1.1438\n        K5:\n          tau_specific_sign_flip: N/A (all-coef fallback)\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 0.998\n          worst_case_diag90: 0.2097\n          worst_case_diag70: 0.5782\n          worst_case_diag50: 0.8784\n        K7:\n          tau_specific_sign_flip: N/A (all-coef fallback)\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 0.999\n          worst_case_diag90: 0.1853\n          worst_case_diag70: 0.4913\n          worst_case_diag50: 0.7441\n      mbias:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.667\n          violation: 0.584\n          amplification: 0.089\n          worst_case_diag90: 0.0106\n          worst_case_diag70: 0.0226\n          worst_case_diag50: 0.0287\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.954\n          violation: 1\n          amplification: 0\n          worst_case_diag90: 0.0154\n          worst_case_diag70: 0.0374\n          worst_case_diag50: 0.0487\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.992\n          violation: 1\n          amplification: 0\n          worst_case_diag90: 0.0133\n          worst_case_diag70: 0.0319\n          worst_case_diag50: 0.0449\n      iv:\n        K3:\n          tau_specific_sign_flip: 0.526\n          all_coef_sign_flip: 0.526\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.2993\n          worst_case_diag70: 1.6444\n          worst_case_diag50: 14.0463\n          note: Wald estimator extremely unstable at low accuracy\n        K5:\n          tau_specific_sign_flip: 0.514\n          all_coef_sign_flip: 0.514\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.4053\n          worst_case_diag70: 2.1036\n          worst_case_diag50: 9.6932\n        K7:\n          tau_specific_sign_flip: 0.523\n          all_coef_sign_flip: 0.523\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.3605\n          worst_case_diag70: 1.8132\n          worst_case_diag50: 8.2204\n      frontdoor:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.836\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1407\n          worst_case_diag70: 0.2604\n          worst_case_diag50: 0.2966\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.967\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1057\n          worst_case_diag70: 0.2066\n          worst_case_diag50: 0.2507\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.993\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0785\n          worst_case_diag70: 0.1646\n          worst_case_diag50: 0.2119\n    conclusion_summary:\n      structural_guarantee: tau_specific_sign_flip = 0% across ALL K for 5/7 topologies\n        (confounding/mediation/collider/mbias/frontdoor)\n      iv_new_finding: IV ~52% tau sign flip (K-invariant) — Wald denominator sign\n        reversal under random C\n      exposure_clarification: Exposure tau_spec_sflip column is all-coef fallback.\n        Actual beta1-specific flip rate = 83.4% (from MVP)\n      worst_case_trend: Decreasing with K for 5/7 topologies (K=3 most conservative).\n        IV catastrophic at low accuracy (WC_d50 up to 14x). Exposure decreasing.\n      mbias_special: Amplification drops to 0% at K>=5\n      rng_fix: Deterministic per-(topo,K,threshold) seeds via SHA-256. Previous values\n        had RNG ordering artifact.\n    runtime_seconds: 20\n    gpu: RTX 5090 cuda:0\n    script: /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py\n- id: plan_003\n  claim: 1\n  description: 'Empirical confusion matrices: 3 LLMs × 3 CSS tasks vs gold-standard'\n  priority: P0\n  gpu_budget_hours: 0\n  api_cost_estimate: $300-550\n  deps: []\n  registry_id: plan003_empirical_confusion_matrices\n  details: 'Tasks: crisis event classification (K=10, HumAID), stance detection (K=3,\n    VAST), toxicity (K=2, as special case / consistency check, Civil Comments). Models:\n    Llama 4 Maverick (Together.ai/OpenRouter), Qwen 3 235B (OpenRouter), DeepSeek\n    Chat V3 (DeepSeek API). ~30K annotations per model × 3 datasets × 3 prompt variants.\n    Output: empirical confusion matrices, inter-model correlation analysis, downstream\n    regression bias vs gold-standard baseline. Inter-model error correlation analysis:\n    for each of 3 model pairs, compute error agreement rate, conditional error correlation\n    (given true label), and Cohen''s kappa on errors. Quantify correlated-error structure\n    to inform whether independent-error assumptions in correction methods hold.\n\n    '\n  status: DONE\n  conclusion: failed\n  metrics:\n    status_detail: PAUSED - API 402 Payment Required (OPENROUTER_API_KEY)\n    api_endpoint: http://47.94.22.126/v1/chat/completions\n    data_dir: results/\n    humaid_recount_20260520T2312:\n      deepseek_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      deepseek_few-shot-3:\n        total: 1500\n        pred_valid: 1345\n        errors: 155\n        error_type: parsing\n        status: WARN\n      deepseek_few-shot-5:\n        total: 1500\n        pred_valid: 1237\n        errors: 263\n        error_type: parsing\n        status: WARN\n      llama4_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      llama4_few-shot-3:\n        total: 1500\n        pred_valid: 1498\n        errors: 2\n        status: OK\n      llama4_few-shot-5:\n        total: 1500\n        pred_valid: 1471\n        errors: 29\n        status: WARN\n      qwen3_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      qwen3_few-shot-3:\n        total: 1500\n        pred_valid: 1423\n        errors: 77\n        error_type: '402'\n        status: WARN\n      qwen3_few-shot-5:\n        total: 1500\n        pred_valid: 0\n        errors: 1500\n        error_type: '402'\n        status: FAIL\n    humaid_summary: 4 OK (≥1498) + 4 WARN (1237-1471) + 1 FAIL (qwen3_fs5 all 402)\n    humaid_usable: 8/9 files have valid data\n    data_fields:\n      true_label: gold_label\n      pred_label: pred_label\n    note: deepseek errors are parsing/format, NOT 402. Only qwen3 errors are 402.\n- id: plan_008\n  claim: 1\n  description: 'Binarization collapse analysis: K→2 folding bias across all 6 topologies'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan008_binarization_collapse\n  details: 'For each of 6 topologies with K=3,5,7: collapse to binary, compare bias\n    from full multi-class expression vs binarized expression. Demonstrate that binarization\n    is not a safe shortcut — can amplify or reverse bias. MVP showed Δ up to 0.089\n    for confounding DAG K=3.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    confounding:\n      D_mean: 0.0253\n      D_med: 0.0182\n      D_P95: 0.0733\n      D_max: 0.2213\n      frac_gt_001: 0.686\n      frac_gt_005: 0.138\n      sign_flip: 0\n    mediation:\n      D_mean: 0.0446\n      D_med: 0.0355\n      D_P95: 0.1179\n      D_max: 0.252\n      frac_gt_001: 0.835\n      frac_gt_005: 0.36\n      sign_flip: 0\n    collider:\n      D_mean: 0.0169\n      D_med: 0.0125\n      D_P95: 0.0472\n      D_max: 0.1069\n      frac_gt_001: 0.572\n      frac_gt_005: 0.039\n      sign_flip: 0\n    M-bias:\n      D_mean: 0.0063\n      D_med: 0.0054\n      D_P95: 0.0147\n      D_max: 0.0328\n      frac_gt_001: 0.181\n      frac_gt_005: 0\n      sign_flip: 0\n    exposure:\n      D_mean: 0.5164\n      D_med: 0.506\n      D_P95: 0.8453\n      D_max: 1.3876\n      frac_gt_001: 1\n      frac_gt_005: 0.999\n      sign_flip: 0.14\n    IV:\n      D_mean: 0.926\n      D_med: 0.9394\n      D_P95: 1.3426\n      D_max: 2.0809\n      frac_gt_001: 1\n      frac_gt_005: 1\n      sign_flip: 0.175\n- id: plan_004\n  claim: 2\n  description: 'ASV framework: formal proofs for confounding, mediation, collider'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan004_asv_framework\n  details: 'Derive ASV expressions for 3 priority topologies. Formal proofs of: (a)\n    monotonicity (ASV increases with δ amplification), (b) sharpness (bound is achievable\n    for some confusion matrix). MC validation: coverage at 90%, 95%, 99% levels across\n    1000 scenarios. Additionally report Type I/II error rates: rejection rate under\n    null (Type I) and power under alternative, before and after ASV-informed correction.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    v2_sign_flip_filter: ✅ effective (Type I=0%, power=100%)\n    v3_envelope_monotonicity: ✅ solved (0 violations)\n    v3_magnitude_reporting: ✅ informative values for all topologies\n    v3_magnitude_filter: ❌ rejected (scale-dependent, not viable as binary test)\n    v3_fixed_signif_filter: ✅ Type I=0% all topologies, power=100% for τ≥0.1\n    v3_significance_filter:\n      confounding_tau005:\n        type_i: 0\n        power: 1\n      confounding_tau010:\n        type_i: 0\n        power: 1\n      mediation_tau005:\n        type_i: 0\n        power: 0\n      mediation_tau010:\n        type_i: 0\n        power: 1\n      collider_tau005:\n        type_i: 0\n        power: 0\n      collider_tau010:\n        type_i: 0\n        power: 1\n      note: τ=0.05 mediation/collider power=0% is correct — attenuating topologies\n        are fragile at small effects\n    v3_fixed_status: complete — significance filter validated\n    v3_envelope_violations: 0\n    v3_magnitude_asv_tau0.5_range: 0.076-0.487\n    v3_magnitude_asv_tau0.05_range: 0.008-0.047\n    v3_magnitude_asv_tau0.1_range: 0.014-0.093\n    v3_coverage_tau0.05: 100.0%\n    v3_coverage_tau0.1: 100.0%\n    n_sensitivity_mediation_tau005:\n      topology: mediation\n      tau: 0.05\n      C0: sym_mild\n      mc_reps: 500\n      N_1000:\n        naive_power: 0.89\n        asv_power: 0\n        median_se: 0.070025\n        median_signif_asv: 0\n      N_2000:\n        naive_power: 0.998\n        asv_power: 0\n        median_se: 0.049649\n        median_signif_asv: 0\n      N_5000:\n        naive_power: 1\n        asv_power: 0\n        median_se: 0.031301\n        median_signif_asv: 0\n      N_10000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.022152\n        median_signif_asv: null\n      N_20000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.01566\n        median_signif_asv: null\n      N_50000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.009903\n        median_signif_asv: null\n      recovery_N: 10000\n      interpretation: 'Sharp phase transition at N~6000-10000. Below: 1.96*SE > tau=0.05\n        so signif_ASV=0 (ASV kills all rejections). Above: 1.96*SE < tau=0.05 so signif_ASV=None\n        (infinite robustness), ASV passes all.'\n- id: plan_005\n  claim: 2\n  description: ASV MC validation for M-bias, instrument, front-door topologies\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_004\n  registry_id: plan005_asv_extended\n  details: 'ASV expressions + MC validation of monotonicity and coverage. Sharpness\n    stated as conjectures supported by numerical evidence. If any topology fails monotonicity\n    under MC, flag and investigate.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    envelope_violations:\n      mbias: 0\n      iv: 0\n      frontdoor: 0\n    plim_at_identity:\n      mbias: 0.5128\n      iv: 0.6598\n      frontdoor: 0.4998\n    asv_tau05:\n      mbias:\n        sign_flip: null\n        magnitude_10pct: null\n      iv:\n        sign_flip_range: 1.1-6.7\n        magnitude_10pct_range: 0.101-0.607\n      frontdoor:\n        sign_flip: null\n        magnitude_10pct_range: 0.064-0.387\n    mc_coverage:\n      mbias_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      mbias_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n      iv_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      iv_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n      frontdoor_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      frontdoor_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n    v_fixed_signif_filter:\n      mbias:\n        type_i: 0\n        power_tau005: 95.8-99.2%\n        power_tau01: 100%\n      iv:\n        type_i: 0\n        power_tau005: 0%\n        power_tau01: 0%\n        note: correct — Wald estimator immediately fragile, signif_ASV≈0 blocks all\n          rejections\n      frontdoor:\n        type_i: 0\n        power_tau005: 100%\n        power_tau01: 100%\n    fixes_applied:\n    - 'C1: compute_signif_asv_fast added'\n    - 'C2: magnitude ASV tau≈0 returns 0.0'\n    - 'W1: IV tau_true=plim_iv(I)=0.6598'\n    - 'W2: M-bias tau_true=plim_mb(I)=0.5128'\n    fixed_script: /home/sonny/causal_annot_error_attrib/plan_005_asv_extended_fixed.py\n    runtime_seconds: 46.2\n- id: plan_006\n  claim: 2\n  description: ASV calibration on empirical data (3 CSS tasks × 3 LLMs)\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  - plan_004\n  details: 'Apply ASVs to empirical confusion matrices from plan_003. Validate coverage\n    on held-out gold-standard splits. Report ASV alongside downstream effect estimates\n    for each task. Compare ASV interpretability with raw confusion matrix reporting.\n    Report Type I/II error rates: rejection rate under null (Type I) and power under\n    alternative, before and after ASV-informed correction, across all task × model\n    combinations. F1 vs downstream causal bias analysis: for each model × task, compute\n    classification F1 and plot against |downstream bias|. Demonstrate that high F1\n    does not guarantee low downstream bias (Baumann 2025: F1>0.93 still >50% error\n    risk). This bridges the gap between annotation quality metrics and causal estimate\n    reliability.\n\n    '\n  status: planned\n- id: plan_007\n  claim: 3\n  description: 'Correction guidance framework: decision mapping + validation'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_004\n  - plan_003\n  details: 'Decision framework: {topology × error structure × ASV} → correction method\n    (DSL / PPI / MLA / MC-SIMEX / naive plug-in / \"no existing method adequate\").\n    MC validation: recommended method produces least bias in ≥90% of scenarios. Empirical\n    validation on plan_003 data. Characterize regimes where no existing method suffices\n    (correlated errors, differential multi-class, etc.) — identify as open problems.\n\n    '\n  status: planned\n- id: plan_009\n  claim: 1\n  description: Pathological confusion matrix analysis (near-permutation, rank-deficient)\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  registry_id: plan009_pathological_matrices\n  details: 'Extreme C structures: near-permutation, rank-deficient, block-diagonal.\n    Characterize when bias becomes catastrophic across topologies. Identify structural\n    conditions (spectral gap, diagonal dominance ratio) that predict bias severity\n    — candidate features for practitioners.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    regression_dichotomy:\n      benign_topologies:\n        list:\n        - confounding\n        - mediation\n        - collider\n        - frontdoor\n        - mbias\n        R2_range: 0.61-0.77\n        primary_predictor: effective_rank\n        secondary_predictors:\n        - spectral_gap\n        - condition_number\n      dangerous_topologies:\n        list:\n        - exposure\n        - iv\n        exposure_R2: 0.11\n        iv_R2: ~0\n        iv_note: regression has no explanatory power — Wald denominator sign reversal\n          is discrete, not predicted by continuous matrix features\n        exposure_note: 'near_perm eps=0.01: 15% catastrophic bias above threshold'\n      global_R2: ~0 (cross-topology aggregation destroys predictive power — different\n        bias mechanisms)\n    risk_tiers:\n      low:\n        topologies:\n        - mbias\n        max_bias: <0.04\n        note: safe even under worst-case pathological C\n      medium:\n        topologies:\n        - confounding\n        - mediation\n        - collider\n        - frontdoor\n        bias_range: 0.1-0.31\n        catastrophic_fraction: 0%\n        R2: 0.70-0.77\n        note: bounded bias, matrix features predictive\n      high:\n        topologies:\n        - exposure\n        - iv\n        note: 'catastrophic regardless of C quality — exposure: structural identification\n          failure; IV: Wald estimator explosion (near_perm eps=0.01 cat=61-73%, rank-deficient\n          bias reaches millions)'\n    most_consistent_predictor: condition_number (significant in 5/5 medium-risk topologies)\n    hypothesis_assessment:\n      H1_predictable_catastrophic: partially — risk tier determined by topology, not\n        C features\n      H2_matrix_features_strong: topology-dependent — 5/7 R²>0.6, exposure/IV fail\n      H3_safety_threshold: not confirmed — boundary is topology-based, not C-feature\n        threshold\n      H4_diagnostic_features: partially — condition_number most consistent, but needs\n        topology-specific criteria\n    iv_filtering:\n      n_filtered: 3000\n      n_total: 28000\n      pct_infinite: 10.7\n      note: non-finite Wald values silently filtered from regression; must note in\n        paper\n    pathological_C_types:\n    - near_permutation (eps=0.01,0.05,0.1,0.2)\n    - rank_deficient\n    - block_diagonal\n    K_values:\n    - 3\n    - 5\n    - 7\n    M_per_config: 1000\n    N_per_sim: 5000000\n    runtime_seconds: 25\n    analysis_report: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md\n    output_files:\n      summary_json: /home/sonny/causal_annot_error_attrib/artifacts/plan009/pathological_bias_summary.json\n      regression_txt: /home/sonny/causal_annot_error_attrib/artifacts/plan009/regression_results.txt\n      analysis_md: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md\n- id: plan_010\n  claim: 1\n  description: annot-sensitivity Python toolkit (open-source release)\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_004\n  - plan_007\n  details: 'Package: user-specified DAG + confusion matrix(es) + downstream estimate\n    → bias expressions (scalar K≤3, matrix K>3 with interpretability) + ASV bounds\n    + sensitivity curves + correction recommendation + diagnostic plots. pip-installable,\n    with worked examples for each topology.\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_confounding_dag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    theory_mc_match: 6/6\n    pass_criteria: 3/3\n    max_binary_collapse_delta: 0.103\n    bias_range: 0.132-0.298\n    ovb_reference: 0.3\n    direction_reversal_found: false\n    random_search_100k_min_bias: 0.063\n- exp_id: mvp_exposure_dag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    theory_mc_match: 5/5\n    pass_criteria: 3/3\n    violation_rate: 0.85\n    sign_reversal_rate: 0.834\n    amplification_rate: 0.141\n    K2_toward_null: 6/6\n    worst_severity: 2.83\n    named_structures_with_violation: 3/6\n- exp_id: mvp_exposure_dirichlet_subspace\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_space_violation: 0.849\n    full_space_sign_rev: 0.833\n    full_space_amplif: 0.275\n    diag50_violation: 0.325\n    diag50_sign_rev: 0.216\n    diag50_amplif: 0.113\n    diag70_violation: 0.137\n    diag70_sign_rev: 0.021\n    diag70_amplif: 0.117\n    diag90_violation: 0.119\n    diag90_sign_rev: 0\n    diag90_amplif: 0.119\n    samples_per_subspace: 50000\n    assessment: ALL subspaces STRONG (>10%)\n- exp_id: plan001_dag_taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    collider:\n      all_coef:\n        violation: 1\n        sign_flip: 0.688\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 0\n      small_tau_0.05:\n        tau_I: 0.015733\n        tau_violation: 0.96\n        tau_sign_flip: 0\n        tau_amplification: 0.992\n      small_tau_0.1:\n        tau_I: 0.06118\n        tau_violation: 0.974\n        tau_sign_flip: 0\n        tau_amplification: 0.995\n    mbias:\n      all_coef:\n        violation: 1\n        sign_flip: 0.651\n        amplification: 0.112\n      tau_specific:\n        violation: 0.532\n        sign_flip: 0\n        amplification: 0.104\n      misclass_amplifies_rate: 0.292\n      small_tau_0.05:\n        tau_I: 0.057669\n        tau_violation: 0.532\n        tau_sign_flip: 0\n        tau_amplification: 0.104\n      small_tau_0.1:\n        tau_I: 0.107669\n        tau_violation: 0.532\n        tau_sign_flip: 0\n        tau_amplification: 0.104\n    mediation_mixed:\n      all_coef:\n        violation: 1\n        sign_flip: 0.835\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    mediation_same:\n      all_coef:\n        violation: 1\n        sign_flip: 0.666\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    frontdoor_mixed:\n      all_coef:\n        violation: 1\n        sign_flip: 0.998\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_I: 0.050177\n        lambda_U: 0.1\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_I: 0.100169\n        lambda_U: 0.2\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    frontdoor_same:\n      all_coef:\n        violation: 1\n        sign_flip: 1\n        amplification: 1\n      tau_specific:\n        violation: 0.999\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 0.9997\n      small_tau_0.05:\n        tau_I: 0.050177\n        lambda_U: 0.1\n        tau_violation: 0.999\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_I: 0.100169\n        lambda_U: 0.2\n        tau_violation: 0.999\n        tau_sign_flip: 0\n        tau_amplification: 1\n    iv_note: 'IV metrics not computed in plan_001 (only 6 fixed C structures tested,\n      no dedicated IV tau_specific analysis). First measured in plan_002: 52% tau_specific_sign_flip\n      from 100k random C (Wald denominator sign reversal). See plan002_k57_extension\n      for full IV results.'\n- exp_id: plan003_empirical_confusion_matrices\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    status_detail: PAUSED - API 402 Payment Required (OPENROUTER_API_KEY)\n    api_endpoint: http://47.94.22.126/v1/chat/completions\n    data_dir: results/\n    humaid_recount_20260520T2312:\n      deepseek_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      deepseek_few-shot-3:\n        total: 1500\n        pred_valid: 1345\n        errors: 155\n        error_type: parsing\n        status: WARN\n      deepseek_few-shot-5:\n        total: 1500\n        pred_valid: 1237\n        errors: 263\n        error_type: parsing\n        status: WARN\n      llama4_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      llama4_few-shot-3:\n        total: 1500\n        pred_valid: 1498\n        errors: 2\n        status: OK\n      llama4_few-shot-5:\n        total: 1500\n        pred_valid: 1471\n        errors: 29\n        status: WARN\n      qwen3_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      qwen3_few-shot-3:\n        total: 1500\n        pred_valid: 1423\n        errors: 77\n        error_type: '402'\n        status: WARN\n      qwen3_few-shot-5:\n        total: 1500\n        pred_valid: 0\n        errors: 1500\n        error_type: '402'\n        status: FAIL\n    humaid_summary: 4 OK (≥1498) + 4 WARN (1237-1471) + 1 FAIL (qwen3_fs5 all 402)\n    humaid_usable: 8/9 files have valid data\n    data_fields:\n      true_label: gold_label\n      pred_label: pred_label\n    note: deepseek errors are parsing/format, NOT 402. Only qwen3 errors are 402.\n- exp_id: plan004_asv_framework\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    v2_sign_flip_filter: ✅ effective (Type I=0%, power=100%)\n    v3_envelope_monotonicity: ✅ solved (0 violations)\n    v3_magnitude_reporting: ✅ informative values for all topologies\n    v3_magnitude_filter: ❌ rejected (scale-dependent, not viable as binary test)\n    v3_fixed_signif_filter: ✅ Type I=0% all topologies, power=100% for τ≥0.1\n    v3_significance_filter:\n      confounding_tau005:\n        type_i: 0\n        power: 1\n      confounding_tau010:\n        type_i: 0\n        power: 1\n      mediation_tau005:\n        type_i: 0\n        power: 0\n      mediation_tau010:\n        type_i: 0\n        power: 1\n      collider_tau005:\n        type_i: 0\n        power: 0\n      collider_tau010:\n        type_i: 0\n        power: 1\n      note: τ=0.05 mediation/collider power=0% is correct — attenuating topologies\n        are fragile at small effects\n    v3_fixed_status: complete — significance filter validated\n    v3_envelope_violations: 0\n    v3_magnitude_asv_tau0.5_range: 0.076-0.487\n    v3_magnitude_asv_tau0.05_range: 0.008-0.047\n    v3_magnitude_asv_tau0.1_range: 0.014-0.093\n    v3_coverage_tau0.05: 100.0%\n    v3_coverage_tau0.1: 100.0%\n    n_sensitivity_mediation_tau005:\n      topology: mediation\n      tau: 0.05\n      C0: sym_mild\n      mc_reps: 500\n      N_1000:\n        naive_power: 0.89\n        asv_power: 0\n        median_se: 0.070025\n        median_signif_asv: 0\n      N_2000:\n        naive_power: 0.998\n        asv_power: 0\n        median_se: 0.049649\n        median_signif_asv: 0\n      N_5000:\n        naive_power: 1\n        asv_power: 0\n        median_se: 0.031301\n        median_signif_asv: 0\n      N_10000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.022152\n        median_signif_asv: null\n      N_20000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.01566\n        median_signif_asv: null\n      N_50000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.009903\n        median_signif_asv: null\n      recovery_N: 10000\n      interpretation: 'Sharp phase transition at N~6000-10000. Below: 1.96*SE > tau=0.05\n        so signif_ASV=0 (ASV kills all rejections). Above: 1.96*SE < tau=0.05 so signif_ASV=None\n        (infinite robustness), ASV passes all.'\n- exp_id: plan008_binarization_collapse\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    confounding:\n      D_mean: 0.0253\n      D_med: 0.0182\n      D_P95: 0.0733\n      D_max: 0.2213\n      frac_gt_001: 0.686\n      frac_gt_005: 0.138\n      sign_flip: 0\n    mediation:\n      D_mean: 0.0446\n      D_med: 0.0355\n      D_P95: 0.1179\n      D_max: 0.252\n      frac_gt_001: 0.835\n      frac_gt_005: 0.36\n      sign_flip: 0\n    collider:\n      D_mean: 0.0169\n      D_med: 0.0125\n      D_P95: 0.0472\n      D_max: 0.1069\n      frac_gt_001: 0.572\n      frac_gt_005: 0.039\n      sign_flip: 0\n    M-bias:\n      D_mean: 0.0063\n      D_med: 0.0054\n      D_P95: 0.0147\n      D_max: 0.0328\n      frac_gt_001: 0.181\n      frac_gt_005: 0\n      sign_flip: 0\n    exposure:\n      D_mean: 0.5164\n      D_med: 0.506\n      D_P95: 0.8453\n      D_max: 1.3876\n      frac_gt_001: 1\n      frac_gt_005: 0.999\n      sign_flip: 0.14\n    IV:\n      D_mean: 0.926\n      D_med: 0.9394\n      D_P95: 1.3426\n      D_max: 2.0809\n      frac_gt_001: 1\n      frac_gt_005: 1\n      sign_flip: 0.175\n- exp_id: plan005_asv_extended\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    envelope_violations:\n      mbias: 0\n      iv: 0\n      frontdoor: 0\n    plim_at_identity:\n      mbias: 0.5128\n      iv: 0.6598\n      frontdoor: 0.4998\n    asv_tau05:\n      mbias:\n        sign_flip: null\n        magnitude_10pct: null\n      iv:\n        sign_flip_range: 1.1-6.7\n        magnitude_10pct_range: 0.101-0.607\n      frontdoor:\n        sign_flip: null\n        magnitude_10pct_range: 0.064-0.387\n    mc_coverage:\n      mbias_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      mbias_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n      iv_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      iv_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n      frontdoor_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      frontdoor_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n    v_fixed_signif_filter:\n      mbias:\n        type_i: 0\n        power_tau005: 95.8-99.2%\n        power_tau01: 100%\n      iv:\n        type_i: 0\n        power_tau005: 0%\n        power_tau01: 0%\n        note: correct — Wald estimator immediately fragile, signif_ASV≈0 blocks all\n          rejections\n      frontdoor:\n        type_i: 0\n        power_tau005: 100%\n        power_tau01: 100%\n    fixes_applied:\n    - 'C1: compute_signif_asv_fast added'\n    - 'C2: magnitude ASV tau≈0 returns 0.0'\n    - 'W1: IV tau_true=plim_iv(I)=0.6598'\n    - 'W2: M-bias tau_true=plim_mb(I)=0.5128'\n    fixed_script: /home/sonny/causal_annot_error_attrib/plan_005_asv_extended_fixed.py\n    runtime_seconds: 46.2\n- exp_id: plan_004_asv_v3_fixed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan002_k57_extension\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_k_comparison_7topo:\n      confounding:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.993\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1614\n          worst_case_diag70: 0.2744\n          worst_case_diag50: 0.2993\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1107\n          worst_case_diag70: 0.2156\n          worst_case_diag50: 0.2462\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0933\n          worst_case_diag70: 0.1859\n          worst_case_diag50: 0.2264\n      mediation:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.838\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1223\n          worst_case_diag70: 0.251\n          worst_case_diag50: 0.3032\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.966\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0867\n          worst_case_diag70: 0.1832\n          worst_case_diag50: 0.2396\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0607\n          worst_case_diag70: 0.1421\n          worst_case_diag50: 0.1879\n      collider:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.666\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0503\n          worst_case_diag70: 0.1064\n          worst_case_diag50: 0.1256\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.955\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0477\n          worst_case_diag70: 0.1087\n          worst_case_diag50: 0.1306\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.992\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0352\n          worst_case_diag70: 0.0826\n          worst_case_diag50: 0.1131\n      exposure:\n        K3:\n          tau_specific_sign_flip: N/A (all-coef fallback; MVP beta1 flip=83.4%)\n          all_coef_sign_flip: 0.99\n          violation: 1\n          amplification: 0.999\n          worst_case_diag90: 0.2726\n          worst_case_diag70: 0.7092\n          worst_case_diag50: 1.1438\n        K5:\n          tau_specific_sign_flip: N/A (all-coef fallback)\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 0.998\n          worst_case_diag90: 0.2097\n          worst_case_diag70: 0.5782\n          worst_case_diag50: 0.8784\n        K7:\n          tau_specific_sign_flip: N/A (all-coef fallback)\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 0.999\n          worst_case_diag90: 0.1853\n          worst_case_diag70: 0.4913\n          worst_case_diag50: 0.7441\n      mbias:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.667\n          violation: 0.584\n          amplification: 0.089\n          worst_case_diag90: 0.0106\n          worst_case_diag70: 0.0226\n          worst_case_diag50: 0.0287\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.954\n          violation: 1\n          amplification: 0\n          worst_case_diag90: 0.0154\n          worst_case_diag70: 0.0374\n          worst_case_diag50: 0.0487\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.992\n          violation: 1\n          amplification: 0\n          worst_case_diag90: 0.0133\n          worst_case_diag70: 0.0319\n          worst_case_diag50: 0.0449\n      iv:\n        K3:\n          tau_specific_sign_flip: 0.526\n          all_coef_sign_flip: 0.526\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.2993\n          worst_case_diag70: 1.6444\n          worst_case_diag50: 14.0463\n          note: Wald estimator extremely unstable at low accuracy\n        K5:\n          tau_specific_sign_flip: 0.514\n          all_coef_sign_flip: 0.514\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.4053\n          worst_case_diag70: 2.1036\n          worst_case_diag50: 9.6932\n        K7:\n          tau_specific_sign_flip: 0.523\n          all_coef_sign_flip: 0.523\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.3605\n          worst_case_diag70: 1.8132\n          worst_case_diag50: 8.2204\n      frontdoor:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.836\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1407\n          worst_case_diag70: 0.2604\n          worst_case_diag50: 0.2966\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.967\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1057\n          worst_case_diag70: 0.2066\n          worst_case_diag50: 0.2507\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.993\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0785\n          worst_case_diag70: 0.1646\n          worst_case_diag50: 0.2119\n    conclusion_summary:\n      structural_guarantee: tau_specific_sign_flip = 0% across ALL K for 5/7 topologies\n        (confounding/mediation/collider/mbias/frontdoor)\n      iv_new_finding: IV ~52% tau sign flip (K-invariant) — Wald denominator sign\n        reversal under random C\n      exposure_clarification: Exposure tau_spec_sflip column is all-coef fallback.\n        Actual beta1-specific flip rate = 83.4% (from MVP)\n      worst_case_trend: Decreasing with K for 5/7 topologies (K=3 most conservative).\n        IV catastrophic at low accuracy (WC_d50 up to 14x). Exposure decreasing.\n      mbias_special: Amplification drops to 0% at K>=5\n      rng_fix: Deterministic per-(topo,K,threshold) seeds via SHA-256. Previous values\n        had RNG ordering artifact.\n    runtime_seconds: 20\n    gpu: RTX 5090 cuda:0\n    script: /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py\n- exp_id: plan009_pathological_matrices\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    regression_dichotomy:\n      benign_topologies:\n        list:\n        - confounding\n        - mediation\n        - collider\n        - frontdoor\n        - mbias\n        R2_range: 0.61-0.77\n        primary_predictor: effective_rank\n        secondary_predictors:\n        - spectral_gap\n        - condition_number\n      dangerous_topologies:\n        list:\n        - exposure\n        - iv\n        exposure_R2: 0.11\n        iv_R2: ~0\n        iv_note: regression has no explanatory power — Wald denominator sign reversal\n          is discrete, not predicted by continuous matrix features\n        exposure_note: 'near_perm eps=0.01: 15% catastrophic bias above threshold'\n      global_R2: ~0 (cross-topology aggregation destroys predictive power — different\n        bias mechanisms)\n    risk_tiers:\n      low:\n        topologies:\n        - mbias\n        max_bias: <0.04\n        note: safe even under worst-case pathological C\n      medium:\n        topologies:\n        - confounding\n        - mediation\n        - collider\n        - frontdoor\n        bias_range: 0.1-0.31\n        catastrophic_fraction: 0%\n        R2: 0.70-0.77\n        note: bounded bias, matrix features predictive\n      high:\n        topologies:\n        - exposure\n        - iv\n        note: 'catastrophic regardless of C quality — exposure: structural identification\n          failure; IV: Wald estimator explosion (near_perm eps=0.01 cat=61-73%, rank-deficient\n          bias reaches millions)'\n    most_consistent_predictor: condition_number (significant in 5/5 medium-risk topologies)\n    hypothesis_assessment:\n      H1_predictable_catastrophic: partially — risk tier determined by topology, not\n        C features\n      H2_matrix_features_strong: topology-dependent — 5/7 R²>0.6, exposure/IV fail\n      H3_safety_threshold: not confirmed — boundary is topology-based, not C-feature\n        threshold\n      H4_diagnostic_features: partially — condition_number most consistent, but needs\n        topology-specific criteria\n    iv_filtering:\n      n_filtered: 3000\n      n_total: 28000\n      pct_infinite: 10.7\n      note: non-finite Wald values silently filtered from regression; must note in\n        paper\n    pathological_C_types:\n    - near_permutation (eps=0.01,0.05,0.1,0.2)\n    - rank_deficient\n    - block_diagonal\n    K_values:\n    - 3\n    - 5\n    - 7\n    M_per_config: 1000\n    N_per_sim: 5000000\n    runtime_seconds: 25\n    analysis_report: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md\n    output_files:\n      summary_json: /home/sonny/causal_annot_error_attrib/artifacts/plan009/pathological_bias_summary.json\n      regression_txt: /home/sonny/causal_annot_error_attrib/artifacts/plan009/regression_results.txt\n      analysis_md: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md\n- exp_id: plan007_correction_guidance\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_combos: 210\n    runtime_sec: 2792\n    ppi_grand_mean_bias_red: 93.8%\n    ppi_grand_mean_coverage: 96.8%\n    ppi_win_rate: 95.2% (40/42)\n    mcsimex_grand_mean_bias_red: 20.9%\n    dsl_grand_mean_bias_red: -144.8%\n    naive_plugin_grand_mean_bias_red: -20.0%\n    mla_grand_mean_bias_red: -37.4%\n    fwl_invariance_verified: true\n    fwl_invariance_topologies: confounding, mediation, collider, mbias (0.0% bias_red\n      for naive/mla)\n    dsl_effective_topologies: confounding (49.8%), mediation (70.3%)\n    dsl_failure_topologies: mbias (-768%), iv (-187%), collider (-89%), exposure (-60%),\n      frontdoor (-29%)\n    ppi_weakness: 'mbias+realistic_llm: -25.1% bias_red (but 99% coverage)'\n- exp_id: plan010_annot_sensitivity_toolkit\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tests_passed: 35/35\n    modules: 7\n    topologies: 7\n    correction_methods: 5\n    lines_of_code:\n      __init__.py: 53\n      bias.py: 174\n      asv.py: 119\n      correction.py: 422\n      confusion.py: 129\n      dgp.py: 213\n      utils.py: 95\n      test_core.py: 35 tests\n    example_output:\n      confounding_k3_bias_pct: +10.20%\n      magnitude_asv: 0.967\n      sign_flip_asv: null\n      recommended_with_gold: ppi\n      recommended_without_gold: dsl\n- exp_id: plan006_asv_empirical\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_scenarios: 210\n    configs: 14\n    topologies: 7\n    k_values:\n    - 2\n    - 3\n    - 10\n    models:\n    - llama4\n    - deepseek\n    - qwen3\n    - qwen2.5-7b\n    sign_flips: 0\n    overall_asv_unsafe_pct: 43.8\n    k2_mean_bias_pct: 36.9\n    k3_mean_bias_pct: 65.3\n    k10_mean_bias_pct: 12.2\n    k2_iv_bias_pct: 116.5\n    k3_iv_bias_pct: 252.3\n    k10_iv_bias_pct: 30.3\n    f1_disconnect: civil_comments F1=0.72-0.75 but IV bias 101-131%\n    7b_vs_235b_bias_ratio: 1.24\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T05:45:38.897Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T05:45:38.897Z",
  "sessionId": "82f0607d-78c0-438f-b491-5c125e51ad8b"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T05:45:38.921Z_

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
  "promptId": "7f0e1c4f-b898-4ad3-9788-ff8ecf9c0d05",
  "type": "user",
  "uuid": "18953cea-a404-4bab-b838-c56cd312700e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "82f0607d-78c0-438f-b491-5c125e51ad8b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T05:45:38.919Z_

```json
{
  "parentUuid": "18953cea-a404-4bab-b838-c56cd312700e",
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
  "uuid": "e994845f-a979-46c2-a666-9e4774b92b0c",
  "timestamp": "2026-05-21T05:45:38.919Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "82f0607d-78c0-438f-b491-5c125e51ad8b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T05:45:38.919Z_

```json
{
  "parentUuid": "e994845f-a979-46c2-a666-9e4774b92b0c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e2f8b486-4a5f-4c6a-9ef1-f8406d5f3e67",
  "timestamp": "2026-05-21T05:45:38.919Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "82f0607d-78c0-438f-b491-5c125e51ad8b",
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
  "leafUuid": "e2f8b486-4a5f-4c6a-9ef1-f8406d5f3e67",
  "sessionId": "82f0607d-78c0-438f-b491-5c125e51ad8b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define best/median/worst scenarios for annotation error bias research",
  "sessionId": "82f0607d-78c0-438f-b491-5c125e51ad8b"
}
```

---

### Assistant

_source line 8 · 2026-05-21T05:49:33.182Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to define three tiers (best/median/worst) for a Dream simulation of this causal annotation error attribution research project. I need to analyze the current state of the research — what's done, what's pending, what the key risks are — and define scenarios that are internally consistent.

Let me analyze the current state:

**Completed experiments:**
- plan_001 (DAG taxonomy K=3): DONE, success
- plan_002 (K=5,7 extension): DONE, success
- plan_003 (empirical confusion matrices): DONE, **failed** (API 402 issues, only HumAID partial data)


- plan_004 through plan_010: All completed successfully, including the ASV framework variants, correction guidance, binarization collapse analysis, pathological matrices, and toolkit development

So most of the experimental pipeline is actually finished — plan_003 is the main failure point with the API issues limiting the confusion matrix collection. Everything else from the ASV framework through the toolkit has succeeded. , let me re-read. In the experiment_plan section, plan_006 and plan_007 show status: planned, but in the registry section, they show as DONE. The registry is the ground truth. So all experiments are actually done.

Key findings so far:
1. Core taxonomy validated: 5/7 topologies have structural guarantee (no sign flip), exposure and IV are dangerous
2. ASV framework works: Type I=0%, good power, coverage 100%
3. Correction guidance: PPI++ dominates (93.8% bias reduction), DSL limited, naive/MLA ineffective for 4/7 topologies
4. Empirical validation done on HumAID (K=10) with partial data (API 402 blocker for some models), plus VAST (K=3) and Civil Comments (K=2) - plan_006 reports 210 scenarios completed across all datasets
5. Binarization collapse confirmed
6. Pathological matrices analyzed

With AAAI 2027 deadline about two months away, the main concerns are whether reviewers will accept the empirical scope given the API failures on some models, and whether the four remaining topologies without formal proofs will be seen as incomplete despite Monte Carlo validation across all seven.

Now I'm thinking through the remaining gaps: correction guidance shows PPI++ works well but requires gold labels, which limits practical applicability. I also need to position this work clearly against prior work like Lee & Wood-Doughty and Wood-Doughty et al. to establish novelty. The core assumptions I'm gating on are whether the empirical validation feels sufficiently rigorous despite the model-tier asymmetry, whether the taxonomy plus sensitivity plus correction framing reads as a coherent contribution, whether the theory-empirical gap is acceptable, and whether ASV genuinely advances beyond E-values or just repackages them.

Looking at the key metrics I'd use to forecast success: empirical bias prediction accuracy, how often ASV flags unsafe scenarios, PPI++ bias reduction in practice, how many topologies have both clean theory and empirical support, and the strength of the F1-bias disconnect since that's central to the practical impact story. The best-case scenario is all three claims fully validated with enough empirical coverage that the direction reversal finding becomes the headline, ASV clearly differentiates from E-values, and reviewers see this as a comprehensive framework. The median case has the core taxonomy and ASV working but empirical gaps that require hedging and scope concerns.

Since plan_006 is already complete with the 210 scenarios and 43.8% ASV-unsafe rate in hand, I'm really forecasting how reviewers will respond once the paper is written and submitted—whether the empirical results sufficiently bridge the theory-practice gap or whether they'll see the taxonomy as just enumeration and the correction guidance as negative results. flips vanish when diagonal dominance exceeds 0.5, and empirical LLMs show diagonal dominance around 0.7 or higher — so zero sign flips actually validates the theory rather than contradicting it. The real concern is the 252% IV bias and the disconnect between F1 scores and bias metrics, which suggests the empirical results are strong but need careful framing in the paper.

Now I'm identifying the key risks: data quality issues from API failures in plan_003 mean only HumAID has complete 3-model coverage while VAST and Civil Comments might be limited to the 7B model, creating potential asymmetries. The bigger challenge is whether I can write this paper clearly given the complexity of 7 topologies across K classes and 3 ASV types without losing reviewers, and whether the contribution feels substantial enough.

To evaluate this, I need to track several metrics: how often theoretical predictions match the Monte Carlo simulations within confidence intervals, whether empirical observations align with theory, how well ASV bounds cover real scenarios, and crucially whether PPI++ actually reduces bias on real data beyond the 93.8% shown on synthetic data. I also want to measure what fraction of cases are flagged as ASV-unsafe and whether F1 scores correlate with downstream bias—if they don't, that strengthens my argument that F1 is an unreliable proxy.

Now I'm laying out three scenarios based on how well the evidence holds up. In the best case, all three claims are solid, the empirical data gap gets resolved, direction reversal is confirmed in at least one real scenario, ASV coverage is complete, and the F1-bias disconnect is stark. The median case has the first two claims holding well but the correction claim needing caveats since PPI++ requires gold labels.  The worst case assumes empirical validation is too thin to be convincing, the taxonomy reads as just listing things without real insight, and the PPI++ result isn't novel enough.

Now I'm looking at the actual Dream simulation results — 210 scenarios with no sign flips, 43.8% of cases flagged as ASV-unsafe, and some stark differences in IV bias across model sizes. The key finding here is that exposure and instrumental variable dangers are real and measurable, so I should center the narrative around that core insight rather than treating it as secondary.

I'm realizing there's some ambiguity in the experiment registry — plan_006 and plan_007 show as completed but the experiment plan lists them as pending, which suggests either partial runs that need extending or preliminary results that should be re-run. What matters for the Dream simulation tiers is how the remaining empirical work plays out: whether I can resolve the API issues, get the frontier model results on VAST and Civil Comments, and how well the theory predictions actually match what I observe. The reviewer reception will depend on how convincingly I can tie those pieces together.

I'm tracking several key metrics to define the tier boundaries: how often the empirical bias matches my theoretical predictions, whether the ASV bounds hold up on real data, how much PPI++ actually reduces bias in practice, whether I find any sign flips in the empirical scenarios, what fraction get flagged as ASV-unsafe, how broken F1 is as a bias predictor, and whether my recommended correction methods actually work best. Now I'm working through the specific tier definitions with precise assumption sets and number ranges for each outcome. In the median scenario, ASV coverage drops to at least 90% with bias reduction between 60-80%, and the theory-empirical match weakens to 75-90%, so I'm tempering the claims to describe the taxonomy as characterizing rather than predicting bias structure, positioning ASV as a useful diagnostic tool, and framing correction guidance as preliminary. For the worst case, I'm facing thin empirical validation with only one usable dataset, a 50-75% theory-empirical match rate hampered by model confounders, and the practical limitation that PPI++ requires gold labels that aren't available in real workflows.

Looking at the next scenario, F1-bias R² climbs to 0.30-0.50, which actually weakens the core narrative that F1 is fundamentally broken. I should reframe the paper around the exposure and instrumental variable findings as the main contribution, position ASV as a practical diagnostic tool, and drop correction guidance from the core claims—essentially repositioning this as a cautionary analysis rather than a prescriptive one. I'm still aiming for the same venues but with a narrower, more defensible scope.

Wait, I need to check whether these metrics are already measured in the existing plan or if the Dream simulation is about running new analyses on the current data or projecting what the final experiments might show.

The next part mentions defining three tiers for the Dream simulation—this is a pre-mortem exercise to establish what best, median, and worst outcomes look like so I can immediately categorize results when they arrive and decide how to respond. Since most experiments are done but a few are still pending, the tiers should focus on how clean the final empirical results are, how well the theory-empirical bridge holds, and how the narrative strength plays out.

I'm going to define actionable gating metrics: the fraction of scenarios where predicted bias direction matches what we observe empirically, and the mean absolute percentage error between predicted and observed magnitudes.

Writing the tier definitions... Looking at the key blockers: the API issue preventing full dataset coverage across all models, whether theoretical predictions actually match empirical bias patterns on real data, and whether PPI++ can be validated with our gold labels. I'm mapping out three scenarios—best case where everything resolves cleanly with strong theory-empirical alignment and a dramatic F1 disconnect, median case where I work with partial data (HumAID's usable files plus smaller models on VAST/CC) and get good but imperfect matches, and worst case where systematic model-specific errors create gaps in the narrative.

Now I'm anchoring these scenarios to concrete numbers from the existing results: the 43.8% ASV-unsafe rate, zero observed sign flips, the extreme IV bias ranging from 30% to 252% depending on the configuration, and the F1 disconnect where the model achieves 0.72 F1 despite over 100% IV bias. These measurements are locked in and will form the empirical backbone of whichever scenario plays out.

The real variation comes from how the remaining experiments land—specifically how many of the HumAID, VAST, and CC datasets yield usable quality data, how closely the theory's bias predictions match what we actually observe across these datasets, whether PPI++ can deliver meaningful bias reduction on real LLM annotations beyond the 93.8% we see in simulation, and ultimately what fraction of empirical scenarios require correction. These are the levers that will determine whether the paper lands as a strong contribution or needs significant reframing. Now I'm defining the median performance tier with two usable datasets, moderate bias reduction around 60-80%, and decision accuracy in the 65-85% range, then setting the worst-case scenario with just HumAID available, higher bias error, and weaker F1 correlation that starts to undermine the narrative.

Actually, I realize some of these metrics are already concrete from the 210 completed scenarios—the unsafe fraction and bias numbers are fixed measurements, not projections. What I should really be thinking about is how the paper's strength evolves between now and the AAAI deadline: resolving remaining API issues to gather more empirical data, completing any outstanding experiments, and ensuring the theoretical framework and writing quality are solid.

Let me step back and focus on what actually matters for the tiers—the best case has everything working cleanly with strong empirical validation and a solid theory-empirical connection leading to acceptance, the median case has mostly working results but with some gaps and caveats that make it borderline for AAAI but likely for ARR, and the worst case has thinner empirical support that requires reframing the core insight but still targets the same venue tier.

Writing the YAML now with specific metrics grounded in the data I have.

Actually, the user is saying I shouldn't preset what best/median/worst mean—I need to define them based on this specific project's framing and current state. Looking at where things stand: the theory is solid across most plans, but empirical validation is the bottleneck, especially around how well the real LLM data matches the theoretical predictions. The correction guidance works well in controlled settings but hasn't been tested on actual data yet. So the tiers should really hinge on how strong the empirical-theoretical correspondence is and whether I have complete enough data to support the claims.

For the actual metrics, I'm settling on measures that directly capture these gaps: how often predicted bias directions match what I observe, the magnitude error between theory and practice, whether the correction method actually reduces bias in real scenarios, and whether the ASV framework identifies unsafe cases correctly. I'm also tracking whether F1 scores correlate with actual bias—that disconnect would be a key finding.

Looking at what plan_006 already locked in, I've got the sign flip count and the ASV-unsafe percentage, so those aren't moving. The real uncertainty centers on three things: whether I can get the full dataset through the API, how well PPI++ generalizes from simulation to real data, and how precisely the theory predicts empirical bias magnitudes. I'm realizing the 55.4% figure is specific to HumAID while the overall average across all 210 scenarios is 43.8%, so both numbers are correct depending on context. Now I need to set up the YAML metrics carefully, making sure I'm consistent about which direction is favorable—some metrics improve when higher (like theory-empirical alignment and correction effectiveness), while others improve when lower (like magnitude error and F1 bias).

Writing YAML structure... Looking at the performance ranges across different metrics—theory-empirical direction matching stays consistently high around 95-100%, magnitude error stays tight within 5-15% MAPE, and the bias reduction from PPI shows 80-95% effectiveness. The ASV unsafe rate empirically sits around 45-60%, while F1 score barely correlates with downstream bias at 0.05-0.20 Pearson correlation, confirming it's not a useful predictor. Correction recommendations achieve 85-95% accuracy, and the instrumental variable analysis shows empirical bias percentages in the 200-300% range for K=3.

The narrative holds up completely—all three core claims stand at full strength. The taxonomy captures the full picture of direction reversals and structural guarantees across different DAG topologies, the ASV framework covers the necessary design variations with actionable guidance through the N* formula, and PPI++ emerges as the only universally reliable method. The headline emphasizes that even high-performing LLMs above 0.9 F1 still generate massive bias under instrumental variable DAGs, with 12% of scenarios showing effect amplification and no safety accuracy threshold to rely on. The paper doesn't need to walk back any of its claims.

But looking at the empirical evidence more carefully, there's a gap between the theoretical framework and what the data actually shows. Claims one and two hold up, but claim three about PPI++ needs to be positioned as preliminary guidance rather than a definitive conclusion. The issue is that we only have frontier model data from HumAID plus one additional dataset, while VAST and CC are limited to 7B models. More fundamentally, PPI++ shows lower bias reduction on real data compared to the Monte Carlo simulations—around 60-80% rather than what the theory predicts—because the actual confusion matrix structure doesn't match the simulation assumptions perfectly. The theory-empirical alignment looks solid for benign topologies, but the exposure and instrumental variable cases show larger discrepancies, partly because the Wald test becomes unstable there. I need to adjust how I frame the main claims: shifting the taxonomy language from "predicts" to "characterizes" to emphasize the structural guarantees and risk classification rather than exact magnitude forecasting, repositioning ASV as a practical diagnostic tool that captures phase transition behavior in attenuating topologies rather than a theoretical breakthrough in sensitivity analysis, and downgrading correction guidance from a core claim to a practical recommendation with explicit caveats about gold label requirements and multi-LLM dependencies. I'm also planning supplementary experiments to strengthen the empirical support.

Now I'm adding a Dirichlet subspace visualization to demonstrate that sign flip regions genuinely don't contain real LLM data points, and I need to give more prominent treatment to model-tier asymmetry in the limitations section. The core issue is that the empirical validation is too weak to support the three-claim structure as currently framed—I should reorient toward a more cautionary, diagnostic approach with narrower focus on just the taxonomy and a single ASV type. The constraints are significant: API issues remain unresolved, data quality problems from parsing errors are accumulating, only one HumAID dataset is usable with some prompt variants missing, and the theory-empirical magnitude match is weak with over 30% discrepancy between the IV/exposure bias and theoretical predictions.

Beyond that, PPI++ performance drops sharply on real data below 60% due to differential error components in the empirical confusion matrix that violate the nondifferential assumption, reviewers see the taxonomy as mere enumeration rather than genuine insight—just a systematic grid of 7 topologies by 6 configurations—and ASV itself lacks novelty as a straightforward multi-class extension of E-value methodology. The correction guidance depends entirely on Monte Carlo simulation with no real data validation, which reviewers identify as a fatal methodological gap for what should be an empirically grounded paper.

Looking at the performance ranges across different metrics—from dataset-model configurations to bias reduction percentages and F1-Pearson correlations—I'm reconsidering the entire framing. Instead of defending the three-claim structure, I should pivot toward positioning this as a cautionary analysis that reveals the topology-dependent dangers of annotation errors, with exposure and instrumental variables emerging as the high-risk tier based on the regression patterns I've observed.

For the safer topologies, condition number consistently predicts bounded bias, so I'll keep that signal. I'm stripping ASV down to just the significance measure where Type I error is cleanest, dropping the magnitude and sign-flip variants entirely. The correction guidance moves to future work—I'll only note that PPI++ shows promise but needs gold-standard data.

The reframed headline emphasizes that exposure and IV DAG structures are fundamentally fragile under annotation error with no safe precision threshold, while condition number predicts bias severity across most topologies except exposure and IV where bias becomes essentially unpredictable. This risk-tier narrative is cleaner and more honest about what the evidence actually shows.

Now I'm shifting away from the taxonomy framing to reduce the surface area for reviewer criticism about exhaustive enumeration. The submission targets AAAI 2027 or ARR October, but I'm narrowing the scope from a comprehensive framework down to focused danger analysis and diagnostic tools.

Checking the metric ordering across performance tiers...

the ranges show realistic overlap at boundaries, with each metric properly calibrated so that best, median, and worst tiers align with what strengthens the narrative—higher unsafe detection rates and lower bias metrics indicate more compelling findings.

Now I'm checking whether the three scenarios logically track with the metrics and story arc: the best case flows from full API resolution through strong config matching to all claims holding, the median case shows partial progress with claims 1-2 supported but claim 3 needing adjustment, and the worst case still requires a reframe but should remain publishable for a top venue. I should also reconcile the existing plan_006 measurements against these ranges to see how additional data collection would push the results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2f8b486-4a5f-4c6a-9ef1-f8406d5f3e67",
  "isSidechain": false,
  "requestId": "req_011CbFBf77sDrWBhH3TffTP4",
  "type": "assistant",
  "uuid": "3b9f2167-c2bb-4a45-a9e6-731a7d1ea336",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "82f0607d-78c0-438f-b491-5c125e51ad8b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TdJ4PFfk6Qk6SK4wtXEfP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26744,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12630,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12630,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26744
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

_source line 9 · 2026-05-21T05:50:07.563Z_

```yaml
tiers:
  best:
    meaning: "理论-实证桥梁完全闭合：3 claims 均以完整强度呈现，实证数据覆盖充分且 theory-empirical match 紧凑"
    key_assumptions:
      - "API 402 解决，VAST/Civil Comments 获得 frontier 模型(≥235B)标注，消除 model-tier asymmetry"
      - "PPI++ 在真实 LLM 标注上 bias reduction 与 MC 一致(≥80%)，nondiff assumption 近似成立"
      - "theory-empirical bias magnitude match 紧凑(MAPE ≤ 15%)，topology ranking 在 K=2,3,10 全部复现"
      - "Dirichlet subspace 可视化成功说服 reviewer：empirical 0 sign flip 是因 LLM accuracy 落在 diag≥0.7 安全区，理论预测的 sign flip 区域与实际 LLM 数据点无交集"
      - "ASV 的 sample-dependent N* 和三类型设计(magnitude/significance/sign-flip)被接受为对 E-value 的实质性扩展"
    number_ranges:
      usable_dataset_model_configs: [12, 14]
      theory_empirical_direction_match_pct: [95, 100]
      theory_empirical_magnitude_MAPE_pct: [5, 15]
      ppi_empirical_bias_reduction_pct: [80, 95]
      asv_unsafe_empirical_pct: [45, 60]
      f1_bias_pearson_r: [0.05, 0.20]
      correction_recommendation_accuracy_pct: [85, 95]
      iv_empirical_bias_pct_k3: [200, 300]
    narrative_direction: >
      原始 framing 完全成立，三条 claim 均以 full strength 呈现：
      (1) taxonomy 捕获 K≥3 方向反转(exposure 83%/IV 52% sign flip)和结构保证(5/7 topologies sign_flip=0%)的完整图景；
      (2) ASV 三类型覆盖不同 DAG，significance_ASV 的 N* phase transition 是核心 actionable 贡献；
      (3) PPI++ universally reliable(93.8% MC + ≥80% empirical)，DSL topology-limited，naive/MLA Frisch-Waugh 失效。
      Headline 无需修改："F1>0.9 的 LLM 在 IV 下仍 >200% bias，12% 场景效应放大无安全阈值。"

  median:
    meaning: "理论框架坚实，实证桥梁有缺口：Claims 1-2 完整但 claims 强度需微调，Claim 3 降级为 preliminary guidance"
    key_assumptions:
      - "API 402 部分解决：HumAID 完整 + 1 额外 dataset 有 frontier 模型，第 3 dataset 仅 7B 模型，model-tier asymmetry 存在但已控制"
      - "PPI++ 真实数据 bias reduction 低于 MC(60-80%)——empirical C 含轻微 differential 成分"
      - "theory-empirical match 在 benign topologies 良好但 IV/exposure MAPE 偏高(Wald 不稳定 + 有限样本方差)"
      - "0 empirical sign flip 与 Dirichlet diag≥0.7 预测一致，但部分 reviewer 仍要求直接 sign flip 实证"
      - "ASV 被部分 reviewer 视为 E-value 自然扩展——需在 rebuttal 中强调 sample-dependent 和 topology-specific ASV type selection 两个维度的差异化"
    number_ranges:
      usable_dataset_model_configs: [8, 11]
      theory_empirical_direction_match_pct: [85, 95]
      theory_empirical_magnitude_MAPE_pct: [15, 35]
      ppi_empirical_bias_reduction_pct: [60, 80]
      asv_unsafe_empirical_pct: [35, 50]
      f1_bias_pearson_r: [0.20, 0.40]
      correction_recommendation_accuracy_pct: [65, 85]
      iv_empirical_bias_pct_k3: [150, 250]
    narrative_direction: >
      Claims 调整措辞但不砍 claim 条数：
      (1) taxonomy "characterizes" 而非 "predicts"——强调 structural guarantee(5/7 sign_flip=0)和 risk tier
      三分(low/medium/high)，弱化对 exact magnitude 的承诺；
      (2) ASV 定位为 "practical diagnostic framework"，强调 significance_ASV 的 N* phase transition
      和 Type I=0% 的干净属性，magnitude_ASV 降级为 "reporting tool"；
      (3) correction guidance 从 core claim 降为 "practical recommendation section"——
      PPI++ dominance 呈现为 empirical finding + known limitation(gold labels required)，
      明确 multi-LLM dependence-aware correction 为 open problem。
      补充：Dirichlet subspace 可视化叠加 empirical LLM confusion matrices 位置，
      证明 sign flip 不在现实操作区域但 amplification 持续存在(12% at diag≥0.9)。
      Model-tier asymmetry 在 limitations 显著讨论。仍可接受于 AAAI/ARR。

  worst:
    meaning: "实证验证无法支撑三 claim 框架：需 reframe 为 cautionary/diagnostic paper，scope 收窄至 danger finding + 单一 ASV 类型"
    key_assumptions:
      - "API 402 持续未解决 + parsing errors 累积，仅 HumAID(K=10)可用且部分 prompt variant 缺失；VAST/CC 仅 7B 单模型"
      - "theory-empirical magnitude match 弱：IV/exposure MAPE >35%，reviewer 质疑 closed-form 在有限 N 下的实用性"
      - "PPI++ 真实数据效果显著下降(<60%)：empirical confusion matrix 含 differential + label-dependent 成分，violated nondiff assumption"
      - "Reviewer 将 7 topologies × 6 C 的 taxonomy 视为 mechanical enumeration，要求 higher-level insight"
      - "ASV 被归为 E-value 的 multi-class 推广，novelty 判定不足"
      - "correction guidance 完全依赖 MC 无真实验证——被视为 methodology paper 的致命伤"
    number_ranges:
      usable_dataset_model_configs: [4, 8]
      theory_empirical_direction_match_pct: [70, 85]
      theory_empirical_magnitude_MAPE_pct: [35, 55]
      ppi_empirical_bias_reduction_pct: [35, 60]
      asv_unsafe_empirical_pct: [25, 40]
      f1_bias_pearson_r: [0.35, 0.55]
      correction_recommendation_accuracy_pct: [40, 65]
      iv_empirical_bias_pct_k3: [100, 200]
    narrative_direction: >
      放弃三 claim 结构，reframe 为 "danger analysis + diagnostic tool"：
      核心 angle 转向 plan_009 的 regression dichotomy 发现——
      (a) exposure/IV 构成 high-risk tier：bias 不可用连续 matrix features 预测(R²≈0)，
      condition_number 在 5/7 topologies 是最一致预测因子但对 exposure/IV 无效；
      (b) 没有安全精度阈值——diag≥0.9 仍有 12% amplification(exposure)和 100% amplification(IV)。
      ASV 仅保留 significance_ASV(Type I=0%，最干净)，砍掉 magnitude 和 sign-flip 两类型以减少攻击面。
      Correction guidance 完全移至 future work，仅保留 "PPI++ promising but gold-dependent" 讨论段。
      用 risk tier(low/medium/high) 叙事替代 taxonomy 枚举，
      headline 改为："exposure 和 IV DAG 对标注误差 fundamentally fragile 且不可诊断——
      5/7 topologies 的 bias 可通过 condition_number 预测(R²=0.61-0.77)，
      但 exposure/IV 的 catastrophic bias 是离散的、不可预测的。"
      仍冲 AAAI 2027 / ARR October，scope 从 comprehensive framework 收窄为 focused danger analysis。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b9f2167-c2bb-4a45-a9e6-731a7d1ea336",
  "isSidechain": false,
  "requestId": "req_011CbFBf77sDrWBhH3TffTP4",
  "type": "assistant",
  "uuid": "e34526ac-4a61-45ab-834d-3bee5e0d87c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "82f0607d-78c0-438f-b491-5c125e51ad8b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TdJ4PFfk6Qk6SK4wtXEfP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26744,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12630,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12630,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26744
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
  "leafUuid": "e34526ac-4a61-45ab-834d-3bee5e0d87c1",
  "sessionId": "82f0607d-78c0-438f-b491-5c125e51ad8b"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define best/median/worst scenarios for annotation error bias research",
  "sessionId": "82f0607d-78c0-438f-b491-5c125e51ad8b"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "e34526ac-4a61-45ab-834d-3bee5e0d87c1",
  "sessionId": "82f0607d-78c0-438f-b491-5c125e51ad8b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Define best/median/worst scenarios for annotation error bias research",
  "sessionId": "82f0607d-78c0-438f-b491-5c125e51ad8b"
}
```

---
