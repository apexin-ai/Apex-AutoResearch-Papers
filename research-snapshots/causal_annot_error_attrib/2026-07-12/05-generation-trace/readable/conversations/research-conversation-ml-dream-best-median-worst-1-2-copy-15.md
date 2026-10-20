# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 8
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/1006286d-c975-40d7-97b7-3d8681efc2df.jsonl`
- **Structured JSON:** [`eadf79c8386512908be5.json`](../../sessions/ea/eadf79c8386512908be5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T05:23:15.203Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T05:23:15.203Z",
  "sessionId": "1006286d-c975-40d7-97b7-3d8681efc2df",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: causal_annot_error_attrib\nvenue: emnlp-2026\nfocus: Re-dream after targeted fixes to all 5 cross-tier structural issues from previous Dream (best 4/6, median 4/6, worst 3.5/6). Key improvements: (1) Related work 31 refs (from ~11), (2) ASV vs PBA delineation, (3) Brenner reconciliation, (4) IV Dirichlet subspace appendix, (5) Non-differential stress test in progress. Paper: 6 figures, formal proofs, 16 pages (8+8), 31 citations.\n\n## paper_framing.md\n\n# Paper Framing — causal_annot_error_attrib\n\n## Target Venue\n- Primary: AAAI 2027 (abstract: 2026-07-21, paper: 2026-07-28)\n- Secondary: ARR October 2026 (~2026-10-15, commit to NAACL 2027 / ACL 2027)\n- Tertiary: ICWSM 2027 Round 2 (2026-09-15)\n\n## Title\nMulti-Class Annotation Errors Are Not Created Equal: Bias Taxonomy, Sensitivity Analysis, and Correction Guidance for LLM-Annotated Causal Studies\n\n## Core Claims (3 条)\n\n1. **Multi-class bias taxonomy**: For K≥3 annotation variables, the direction and magnitude of downstream bias depend on the interaction between the K×K confusion matrix structure and the DAG topology — breaking guarantees that hold in the binary case. We provide closed-form bias expressions for K=3 and matrix-form expressions with interpretability tools for general K, across 7 canonical social-science DAG topologies (confounding, exposure, mediation, collider, M-bias, instrument, front-door).\n\n2. **Annotation Sensitivity Values (ASVs)**: A sensitivity analysis framework for annotation-induced bias. ASVs quantify the minimum degree of annotation error amplification needed to overturn a downstream conclusion, parameterized by a reference confusion matrix and amplification factor δ. Three complementary ASV types — magnitude (E-value-style robustness reporting, all topologies), significance (hypothesis testing filter, effective for attenuating topologies), and sign-flip (direction reversal warning, primarily exposure DAG) — because no single sensitivity metric suffices across all causal designs. The choice of appropriate ASV type is itself topology-dependent, reinforcing Claim 1. ASVs reveal a striking sensitivity ranking: IV estimates are maximally fragile (any annotation error exceeds threshold), while M-bias is immune (misclassification actually reduces spurious associations). Unlike E-values, ASVs incorporate study precision (sample-dependent), providing actionable guidance: for a given τ and σ, the critical sample size N* is analytically computable. Formal proofs (envelope monotonicity + sharpness) for 3 priority topologies; MC-validated for all 7.\n\n3. **Correction guidance framework**: A principled decision framework mapping {DAG topology × error structure × ASV} to the appropriate correction method (DSL, PPI++, MLA, MC-SIMEX, naive plug-in). Key findings from 210-configuration MC validation (7 topo × 6 C × 5 methods × 1000 sims): (a) Frisch-Waugh theorem makes naive_plugin/MLA fundamentally ineffective for T-coefficient bias in 4/7 topologies (bias reduction = 0.0%, exact); (b) DSL is topology-limited — effective only for confounding (50%) and mediation (70%), catastrophically harmful elsewhere (mbias -768%, IV -187%); (c) PPI++ is the only universally reliable method (93.8% grand mean bias reduction, 96.8% coverage) but requires gold-standard labels; (d) correction method effectiveness is itself topology-dependent, reinforcing Claim 1. Dependence-aware multi-LLM correction remains an open problem.\n\n## Story Spine\n\n- **Problem**: LLMs are rapidly replacing human annotators in CSS, but Baumann et al. (2025) show 31–50% of downstream conclusions are already incorrect — critically, even annotators with F1 > 0.93 produce > 50% error risk in downstream causal estimates. Researchers lack diagnostic tools to answer: (a) which annotation error structures propagate bias under their causal design, and (b) how robust their conclusions are to annotation error. Kim et al. (ICML 2025) show cross-model errors are highly correlated (60% agreement when both err), meaning ensembles cannot escape systematic bias — researchers MUST analyze the error structure of their chosen annotator, which is exactly what our tools enable. The field's reliance on classification F1 as a proxy for downstream validity is fundamentally broken; our framework provides the missing link from annotation quality metrics to causal estimate reliability.\n\n- **Existing approaches & gaps**: Wood-Doughty et al. (2018) apply DAG reasoning to text classifier errors but produce no formal bias theorems (binary only). TeBlunthuis et al. (2024) provide the most complete binary treatment with MLA correction but are limited to K=2, single classifier. Lee & Wood-Doughty (2024) extend to categorical + LLM classifiers but cover only 1 DAG topology (unobserved confounding), with no systematic taxonomy or sensitivity analysis. VanderWeele & Li (2019) provide sensitivity bounds but only for binary risk ratios. Jerzak et al. (EMNLP 2025) benchmark correction methods but treat error as monolithic — if different confusion matrix structures produce qualitatively different bias in different DAG topologies, unconditional benchmarking is itself misleading.\n\n- **Our framing**: Multi-class annotation errors are not created equal. The same confusion matrix that produces innocuous residual bias in one DAG topology can produce direction-reversing toxic bias in another. We provide the first systematic characterization of this interaction (the taxonomy), a tool to quantify robustness (ASVs), and guidance for when/how to correct (the framework). This is not a new correction method — it is the missing diagnostic layer that tells researchers which correction is appropriate, or whether correction is needed at all.\n\n- **Headline result template**: \"Across 7 DAG topologies with K=3, our bias expressions correctly predict bias direction and magnitude within 95% MC confidence intervals. ASVs reveal a striking sensitivity spectrum: IV estimates are maximally fragile (any annotation error exceeds robustness thresholds), while M-bias associations are immune (misclassification reduces spurious bias). Empirical validation on 3 CSS tasks (K=2, 3, 10) annotated by 4 LLMs confirms the theoretical predictions: IV bias ranges from 30% at K=10 to 252% at K=3 across annotation settings, F1 does not predict downstream safety (F1=0.72 but IV bias>100%), and 55.4% of HumAID scenarios are ASV-unsafe, requiring correction or sensitivity reporting.\"\n\n## Core Insight (Lead Finding) — DUAL VERSION, gate on plan_001\n\n### Version A (≥1 topology shows direction reversal under K≥3 non-differential exposure misclassification)\nThe binary guarantee that \"non-differential exposure misclassification biases toward the null\" (Bross 1954) breaks in the multi-class case. For specific confusion matrix structures in specific DAG topologies, K≥3 non-differential error can amplify or reverse effect estimates. Brenner (1993) identified this possibility for polytomous confounder misclassification (\"bias can go in either direction\"); we provide the first systematic characterization across 7 DAG topologies with exact conditions for each {C structure × topology} cell. Furthermore, binarizing a K-class variable to \"escape\" into the binary regime is itself hazardous — collapsing introduces new, direction-unpredictable bias (MVP evidence: Δ up to 0.103).\n\n### Version B (no direction reversal found across topologies)\nMulti-class annotation error is structurally irreducible to the binary case: the downstream bias magnitude depends on the full K×K confusion matrix in ways that binary sensitivity/specificity cannot predict, and binarizing a K-class variable introduces new bias (MVP evidence: Δ up to 0.103). While non-differential error preserves bias direction across tested topologies (a useful practitioners' guarantee), the magnitude varies dramatically with confusion matrix structure (0.13–0.30 in confounding DAG alone), and this variation is topology-dependent. ASVs provide the missing robustness measure for this quantitative — not directional — uncertainty.\n\n**Gate**: RESOLVED → Version A. Two topologies show τ-specific direction reversal: exposure (~83-100% sign flip) and IV (~52% sign flip, Wald denominator mechanism). 5/7 topologies have structural guarantee τ_sign_flip=0% across K={3,5,7}. See D003, D004, D010.\n\n## MVP Evidence\n\n**Confounding DAG + K=3** (confounder misclassification):\n- Theoretical bias expressions match MC perfectly (6/6 structures within 95% CI) — framework validated\n- Binary collapse ≠ multi-class: Δ up to 0.103 (near-permutation C), proving K=3 retains more confounding control than binarization\n- 100k random C search: confounding DAG bias is monotonically toward OVB — this topology is \"well-behaved\" (predictable direction)\n- NOTE: Confounding DAG tests residual confounding, NOT bias-toward-null (Bross 1954). Criterion 2 (away-from-null bias) holds for binary too in this topology. See M001.\n\n**Exposure DAG K=3** (exposure misclassification — D002/D004 CONFIRMED):\n- 100k random C: 85% violate bias-toward-null, 83.4% sign reversal, 14.1% amplification\n- K=2 control: 6/6 toward null (binary guarantee holds)\n- Worst case: β₁=1.0 → γ̂₁=-0.84 (sign reversal, 0.84× magnitude); β₂=-0.5 → γ̂₂=-1.41 (2.83× amplification)\n- Mechanism: near-permutation C causes label swap → effect direction flips (structurally impossible in K=2)\n- **Two-DAG contrast**: confounding (monotonic, predictable) vs exposure (unpredictable, topology-dependent) — validates core claim\n\n**Dirichlet subspace analysis** (practical relevance validation):\n- diag≥0.5: 32.5% violation, 21.6% sign reversal, 11.3% amplification\n- diag≥0.7 (typical LLM accuracy): **13.7% violation**, 2.1% sign reversal, **11.7% amplification**\n- diag≥0.9 (high-accuracy LLM): **11.9% violation**, 0% sign reversal, **11.9% amplification**\n- Key pattern: sign reversal vanishes at high accuracy, but **amplification persists at ~12% regardless of accuracy**\n- Implication: even 90%+ accuracy LLMs face non-trivial effect amplification risk — no \"safe accuracy threshold\" exists\n\n**IV Dirichlet subspace analysis** (Dream feedback, 2026-05-21):\n- Full: 100% violation, 51.7% sign flip, 48.3% amplification\n- diag≥0.5: 100% violation, **0% sign flip**, 100% amplification, worst 28.6×\n- diag≥0.7: 100% violation, 0% sign flip, 100% amplification, worst 2.4×\n- diag≥0.9: 100% violation, 0% sign flip, 100% amplification, worst 1.2×\n- Key contrast with exposure: IV sign flip vanishes at diag≥0.5 (exposure persists at 2.1% at diag≥0.7), but IV amplification is **universal** (100% at all thresholds, vs exposure 11.7% at diag≥0.7)\n- Mechanism: Wald denominator monotonically contracts; diagonal dominance prevents zero-crossing (no sign flip) but not contraction (amplification)\n\n## Venue Fit Risks\n\n- **AAAI**: Broad AI audience — emphasize general methodology for \"automated annotation measurement error,\" not LLM-specific. Frame as extending classical measurement error theory to modern automated labeling.\n- **ARR/NAACL**: NLP audience — CSS track is natural fit. May want more empirical NLP experiments. Balance theory with practical LLM annotation scenarios.\n- **Cross-discipline bridge**: Epidemiology (measurement error theory) × NLP (annotation errors). Epi reviewers check proof rigor; NLP reviewers check empirical relevance. Must serve both.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n1. **\"Trivial extension of binary to multi-class\"** → Brenner (1993) proved direction reversal; our taxonomy provides the first systematic characterization across 7 topologies. Binarizing K-class introduces NEW unpredictable bias (MVP evidence). The complexity jump is structural: binary has 2 free parameters (sensitivity, specificity) → scalar bias; K=5 has 20 free parameters → matrix-valued bias requiring eigendecomposition for interpretation. [Experiments: plan_001, plan_008]\n\n2. **\"Lee & Wood-Doughty (2024) already did categorical\"** → They cover 1 topology (unobserved confounding) on 1 dataset (MIMIC). We cover 7 topologies with systematic taxonomy + ASVs + correction guidance. Their work is a stepping stone; ours is the full framework. [Experiments: plan_001]\n\n3. **\"Why these 7 DAG topologies?\"** → These are the canonical CSS causal designs used by Hernán & Cole (2009) and TeBlunthuis et al. (2024). They cover the major roles an annotated variable can play: exposure (treatment), confounder, mediator, collider, instrument, front-door criterion variable. [Experiments: plan_001]\n\n4. **\"K≥5 expressions aren't actionable\"** → Three interpretability tools: (a) eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar bounds, (c) diagnostic visualizations. [Experiments: plan_002]\n\n5. **\"ASV sharpness only proved for 3 topologies\"** → Honest scoping reflecting algebraic complexity. Remaining 3 validated via MC with numerical sharpness evidence. Full proofs identified as immediate future work. [Experiments: plan_004, plan_005]\n\n6. **\"Correlated multi-LLM errors?\"** → Kim et al. (ICML 2025) actually STRENGTHENS our case: if ensembles can't fix errors (60% agreement when both err), error structure analysis is the only viable approach. Multi-annotator correction with dependence is identified as an open problem. [Framework discussion]\n\n7. **\"Empirical validation scope\"** → 3 CSS tasks (HumAID K=10, VAST K=3, Civil Comments K=2) × 4 LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat, Qwen2.5-7B) × 7 topologies = 14 configs. D016 confirms: topology ranking matches theory across all K values; IV bias co-varies with annotation setting (K=3 IV bias 252% vs K=10 30%, confounded with dataset/model differences); 7B vs 235B bias ratio 1.24 (model scale not dominant). 0 sign flips across all 98 scenarios. Note: VAST/Civil Comments use 7B local model (API 402 blocker), creating a model-tier asymmetry acknowledged in Limitations. [Experiments: plan_003, plan_006]\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: Derive and MC-validate bias expressions for 6 DAG topologies with K=3\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: plan001_dag_taxonomy\n  details: 'For each topology (confounding, mediation, collider, M-bias, instrument,\n    front-door): derive closed-form K=3 bias expression, validate with MC (1000 reps\n    × N=10000, 6 confusion matrix structures including near-permutation extreme).\n    Key question: which topologies show direction reversal under non-differential\n    error? Confounding already validated in MVP (no reversal, monotonic toward OVB).\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    collider:\n      all_coef:\n        violation: 1\n        sign_flip: 0.688\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 0\n      small_tau_0.05:\n        tau_I: 0.015733\n        tau_violation: 0.96\n        tau_sign_flip: 0\n        tau_amplification: 0.992\n      small_tau_0.1:\n        tau_I: 0.06118\n        tau_violation: 0.974\n        tau_sign_flip: 0\n        tau_amplification: 0.995\n    mbias:\n      all_coef:\n        violation: 1\n        sign_flip: 0.651\n        amplification: 0.112\n      tau_specific:\n        violation: 0.532\n        sign_flip: 0\n        amplification: 0.104\n      misclass_amplifies_rate: 0.292\n      small_tau_0.05:\n        tau_I: 0.057669\n        tau_violation: 0.532\n        tau_sign_flip: 0\n        tau_amplification: 0.104\n      small_tau_0.1:\n        tau_I: 0.107669\n        tau_violation: 0.532\n        tau_sign_flip: 0\n        tau_amplification: 0.104\n    mediation_mixed:\n      all_coef:\n        violation: 1\n        sign_flip: 0.835\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    mediation_same:\n      all_coef:\n        violation: 1\n        sign_flip: 0.666\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    frontdoor_mixed:\n      all_coef:\n        violation: 1\n        sign_flip: 0.998\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_I: 0.050177\n        lambda_U: 0.1\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_I: 0.100169\n        lambda_U: 0.2\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    frontdoor_same:\n      all_coef:\n        violation: 1\n        sign_flip: 1\n        amplification: 1\n      tau_specific:\n        violation: 0.999\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 0.9997\n      small_tau_0.05:\n        tau_I: 0.050177\n        lambda_U: 0.1\n        tau_violation: 0.999\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_I: 0.100169\n        lambda_U: 0.2\n        tau_violation: 0.999\n        tau_sign_flip: 0\n        tau_amplification: 1\n    iv_note: 'IV metrics not computed in plan_001 (only 6 fixed C structures tested,\n      no dedicated IV tau_specific analysis). First measured in plan_002: 52% tau_specific_sign_flip\n      from 100k random C (Wald denominator sign reversal). See plan002_k57_extension\n      for full IV results.'\n- id: plan_002\n  claim: 1\n  description: Extend bias expressions to K=5,7 — matrix notation + interpretability\n    tools\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: plan002_k57_extension\n  details: 'Matrix-form expressions for general K. Three interpretability tools: (a)\n    eigendecomposition summaries identifying dominant bias modes, (b) worst-case scalar\n    bounds collapsing matrix to conservative scalar, (c) diagnostic visualizations\n    mapping confusion matrix regions to bias magnitude. Validate on confounding +\n    mediation + collider DAGs with K=5,7.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_k_comparison_7topo:\n      confounding:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.993\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1614\n          worst_case_diag70: 0.2744\n          worst_case_diag50: 0.2993\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1107\n          worst_case_diag70: 0.2156\n          worst_case_diag50: 0.2462\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0933\n          worst_case_diag70: 0.1859\n          worst_case_diag50: 0.2264\n      mediation:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.838\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1223\n          worst_case_diag70: 0.251\n          worst_case_diag50: 0.3032\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.966\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0867\n          worst_case_diag70: 0.1832\n          worst_case_diag50: 0.2396\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0607\n          worst_case_diag70: 0.1421\n          worst_case_diag50: 0.1879\n      collider:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.666\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0503\n          worst_case_diag70: 0.1064\n          worst_case_diag50: 0.1256\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.955\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0477\n          worst_case_diag70: 0.1087\n          worst_case_diag50: 0.1306\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.992\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0352\n          worst_case_diag70: 0.0826\n          worst_case_diag50: 0.1131\n      exposure:\n        K3:\n          tau_specific_sign_flip: N/A (all-coef fallback; MVP beta1 flip=83.4%)\n          all_coef_sign_flip: 0.99\n          violation: 1\n          amplification: 0.999\n          worst_case_diag90: 0.2726\n          worst_case_diag70: 0.7092\n          worst_case_diag50: 1.1438\n        K5:\n          tau_specific_sign_flip: N/A (all-coef fallback)\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 0.998\n          worst_case_diag90: 0.2097\n          worst_case_diag70: 0.5782\n          worst_case_diag50: 0.8784\n        K7:\n          tau_specific_sign_flip: N/A (all-coef fallback)\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 0.999\n          worst_case_diag90: 0.1853\n          worst_case_diag70: 0.4913\n          worst_case_diag50: 0.7441\n      mbias:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.667\n          violation: 0.584\n          amplification: 0.089\n          worst_case_diag90: 0.0106\n          worst_case_diag70: 0.0226\n          worst_case_diag50: 0.0287\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.954\n          violation: 1\n          amplification: 0\n          worst_case_diag90: 0.0154\n          worst_case_diag70: 0.0374\n          worst_case_diag50: 0.0487\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.992\n          violation: 1\n          amplification: 0\n          worst_case_diag90: 0.0133\n          worst_case_diag70: 0.0319\n          worst_case_diag50: 0.0449\n      iv:\n        K3:\n          tau_specific_sign_flip: 0.526\n          all_coef_sign_flip: 0.526\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.2993\n          worst_case_diag70: 1.6444\n          worst_case_diag50: 14.0463\n          note: Wald estimator extremely unstable at low accuracy\n        K5:\n          tau_specific_sign_flip: 0.514\n          all_coef_sign_flip: 0.514\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.4053\n          worst_case_diag70: 2.1036\n          worst_case_diag50: 9.6932\n        K7:\n          tau_specific_sign_flip: 0.523\n          all_coef_sign_flip: 0.523\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.3605\n          worst_case_diag70: 1.8132\n          worst_case_diag50: 8.2204\n      frontdoor:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.836\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1407\n          worst_case_diag70: 0.2604\n          worst_case_diag50: 0.2966\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.967\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1057\n          worst_case_diag70: 0.2066\n          worst_case_diag50: 0.2507\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.993\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0785\n          worst_case_diag70: 0.1646\n          worst_case_diag50: 0.2119\n    conclusion_summary:\n      structural_guarantee: tau_specific_sign_flip = 0% across ALL K for 5/7 topologies\n        (confounding/mediation/collider/mbias/frontdoor)\n      iv_new_finding: IV ~52% tau sign flip (K-invariant) — Wald denominator sign\n        reversal under random C\n      exposure_clarification: Exposure tau_spec_sflip column is all-coef fallback.\n        Actual beta1-specific flip rate = 83.4% (from MVP)\n      worst_case_trend: Decreasing with K for 5/7 topologies (K=3 most conservative).\n        IV catastrophic at low accuracy (WC_d50 up to 14x). Exposure decreasing.\n      mbias_special: Amplification drops to 0% at K>=5\n      rng_fix: Deterministic per-(topo,K,threshold) seeds via SHA-256. Previous values\n        had RNG ordering artifact.\n    runtime_seconds: 20\n    gpu: RTX 5090 cuda:0\n    script: /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py\n- id: plan_003\n  claim: 1\n  description: 'Empirical confusion matrices: 3 LLMs × 3 CSS tasks vs gold-standard'\n  priority: P0\n  gpu_budget_hours: 0\n  api_cost_estimate: $300-550\n  deps: []\n  registry_id: plan003_empirical_confusion_matrices\n  details: 'Tasks: crisis event classification (K=10, HumAID), stance detection (K=3,\n    VAST), toxicity (K=2, as special case / consistency check, Civil Comments). Models:\n    Llama 4 Maverick (Together.ai/OpenRouter), Qwen 3 235B (OpenRouter), DeepSeek\n    Chat V3 (DeepSeek API). ~30K annotations per model × 3 datasets × 3 prompt variants.\n    Output: empirical confusion matrices, inter-model correlation analysis, downstream\n    regression bias vs gold-standard baseline. Inter-model error correlation analysis:\n    for each of 3 model pairs, compute error agreement rate, conditional error correlation\n    (given true label), and Cohen''s kappa on errors. Quantify correlated-error structure\n    to inform whether independent-error assumptions in correction methods hold.\n\n    '\n  status: DONE\n  conclusion: failed\n  metrics:\n    status_detail: PAUSED - API 402 Payment Required (OPENROUTER_API_KEY)\n    api_endpoint: http://47.94.22.126/v1/chat/completions\n    data_dir: results/\n    humaid_recount_20260520T2312:\n      deepseek_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      deepseek_few-shot-3:\n        total: 1500\n        pred_valid: 1345\n        errors: 155\n        error_type: parsing\n        status: WARN\n      deepseek_few-shot-5:\n        total: 1500\n        pred_valid: 1237\n        errors: 263\n        error_type: parsing\n        status: WARN\n      llama4_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      llama4_few-shot-3:\n        total: 1500\n        pred_valid: 1498\n        errors: 2\n        status: OK\n      llama4_few-shot-5:\n        total: 1500\n        pred_valid: 1471\n        errors: 29\n        status: WARN\n      qwen3_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      qwen3_few-shot-3:\n        total: 1500\n        pred_valid: 1423\n        errors: 77\n        error_type: '402'\n        status: WARN\n      qwen3_few-shot-5:\n        total: 1500\n        pred_valid: 0\n        errors: 1500\n        error_type: '402'\n        status: FAIL\n    humaid_summary: 4 OK (≥1498) + 4 WARN (1237-1471) + 1 FAIL (qwen3_fs5 all 402)\n    humaid_usable: 8/9 files have valid data\n    data_fields:\n      true_label: gold_label\n      pred_label: pred_label\n    note: deepseek errors are parsing/format, NOT 402. Only qwen3 errors are 402.\n- id: plan_008\n  claim: 1\n  description: 'Binarization collapse analysis: K→2 folding bias across all 6 topologies'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan008_binarization_collapse\n  details: 'For each of 6 topologies with K=3,5,7: collapse to binary, compare bias\n    from full multi-class expression vs binarized expression. Demonstrate that binarization\n    is not a safe shortcut — can amplify or reverse bias. MVP showed Δ up to 0.089\n    for confounding DAG K=3.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    confounding:\n      D_mean: 0.0253\n      D_med: 0.0182\n      D_P95: 0.0733\n      D_max: 0.2213\n      frac_gt_001: 0.686\n      frac_gt_005: 0.138\n      sign_flip: 0\n    mediation:\n      D_mean: 0.0446\n      D_med: 0.0355\n      D_P95: 0.1179\n      D_max: 0.252\n      frac_gt_001: 0.835\n      frac_gt_005: 0.36\n      sign_flip: 0\n    collider:\n      D_mean: 0.0169\n      D_med: 0.0125\n      D_P95: 0.0472\n      D_max: 0.1069\n      frac_gt_001: 0.572\n      frac_gt_005: 0.039\n      sign_flip: 0\n    M-bias:\n      D_mean: 0.0063\n      D_med: 0.0054\n      D_P95: 0.0147\n      D_max: 0.0328\n      frac_gt_001: 0.181\n      frac_gt_005: 0\n      sign_flip: 0\n    exposure:\n      D_mean: 0.5164\n      D_med: 0.506\n      D_P95: 0.8453\n      D_max: 1.3876\n      frac_gt_001: 1\n      frac_gt_005: 0.999\n      sign_flip: 0.14\n    IV:\n      D_mean: 0.926\n      D_med: 0.9394\n      D_P95: 1.3426\n      D_max: 2.0809\n      frac_gt_001: 1\n      frac_gt_005: 1\n      sign_flip: 0.175\n- id: plan_004\n  claim: 2\n  description: 'ASV framework: formal proofs for confounding, mediation, collider'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan004_asv_framework\n  details: 'Derive ASV expressions for 3 priority topologies. Formal proofs of: (a)\n    monotonicity (ASV increases with δ amplification), (b) sharpness (bound is achievable\n    for some confusion matrix). MC validation: coverage at 90%, 95%, 99% levels across\n    1000 scenarios. Additionally report Type I/II error rates: rejection rate under\n    null (Type I) and power under alternative, before and after ASV-informed correction.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    v2_sign_flip_filter: ✅ effective (Type I=0%, power=100%)\n    v3_envelope_monotonicity: ✅ solved (0 violations)\n    v3_magnitude_reporting: ✅ informative values for all topologies\n    v3_magnitude_filter: ❌ rejected (scale-dependent, not viable as binary test)\n    v3_fixed_signif_filter: ✅ Type I=0% all topologies, power=100% for τ≥0.1\n    v3_significance_filter:\n      confounding_tau005:\n        type_i: 0\n        power: 1\n      confounding_tau010:\n        type_i: 0\n        power: 1\n      mediation_tau005:\n        type_i: 0\n        power: 0\n      mediation_tau010:\n        type_i: 0\n        power: 1\n      collider_tau005:\n        type_i: 0\n        power: 0\n      collider_tau010:\n        type_i: 0\n        power: 1\n      note: τ=0.05 mediation/collider power=0% is correct — attenuating topologies\n        are fragile at small effects\n    v3_fixed_status: complete — significance filter validated\n    v3_envelope_violations: 0\n    v3_magnitude_asv_tau0.5_range: 0.076-0.487\n    v3_magnitude_asv_tau0.05_range: 0.008-0.047\n    v3_magnitude_asv_tau0.1_range: 0.014-0.093\n    v3_coverage_tau0.05: 100.0%\n    v3_coverage_tau0.1: 100.0%\n    n_sensitivity_mediation_tau005:\n      topology: mediation\n      tau: 0.05\n      C0: sym_mild\n      mc_reps: 500\n      N_1000:\n        naive_power: 0.89\n        asv_power: 0\n        median_se: 0.070025\n        median_signif_asv: 0\n      N_2000:\n        naive_power: 0.998\n        asv_power: 0\n        median_se: 0.049649\n        median_signif_asv: 0\n      N_5000:\n        naive_power: 1\n        asv_power: 0\n        median_se: 0.031301\n        median_signif_asv: 0\n      N_10000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.022152\n        median_signif_asv: null\n      N_20000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.01566\n        median_signif_asv: null\n      N_50000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.009903\n        median_signif_asv: null\n      recovery_N: 10000\n      interpretation: 'Sharp phase transition at N~6000-10000. Below: 1.96*SE > tau=0.05\n        so signif_ASV=0 (ASV kills all rejections). Above: 1.96*SE < tau=0.05 so signif_ASV=None\n        (infinite robustness), ASV passes all.'\n- id: plan_005\n  claim: 2\n  description: ASV MC validation for M-bias, instrument, front-door topologies\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_004\n  registry_id: plan005_asv_extended\n  details: 'ASV expressions + MC validation of monotonicity and coverage. Sharpness\n    stated as conjectures supported by numerical evidence. If any topology fails monotonicity\n    under MC, flag and investigate.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    envelope_violations:\n      mbias: 0\n      iv: 0\n      frontdoor: 0\n    plim_at_identity:\n      mbias: 0.5128\n      iv: 0.6598\n      frontdoor: 0.4998\n    asv_tau05:\n      mbias:\n        sign_flip: null\n        magnitude_10pct: null\n      iv:\n        sign_flip_range: 1.1-6.7\n        magnitude_10pct_range: 0.101-0.607\n      frontdoor:\n        sign_flip: null\n        magnitude_10pct_range: 0.064-0.387\n    mc_coverage:\n      mbias_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      mbias_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n      iv_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      iv_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n      frontdoor_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      frontdoor_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n    v_fixed_signif_filter:\n      mbias:\n        type_i: 0\n        power_tau005: 95.8-99.2%\n        power_tau01: 100%\n      iv:\n        type_i: 0\n        power_tau005: 0%\n        power_tau01: 0%\n        note: correct — Wald estimator immediately fragile, signif_ASV≈0 blocks all\n          rejections\n      frontdoor:\n        type_i: 0\n        power_tau005: 100%\n        power_tau01: 100%\n    fixes_applied:\n    - 'C1: compute_signif_asv_fast added'\n    - 'C2: magnitude ASV tau≈0 returns 0.0'\n    - 'W1: IV tau_true=plim_iv(I)=0.6598'\n    - 'W2: M-bias tau_true=plim_mb(I)=0.5128'\n    fixed_script: /home/sonny/causal_annot_error_attrib/plan_005_asv_extended_fixed.py\n    runtime_seconds: 46.2\n- id: plan_006\n  claim: 2\n  description: ASV calibration on empirical data (3 CSS tasks × 3 LLMs)\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  - plan_004\n  details: 'Apply ASVs to empirical confusion matrices from plan_003. Validate coverage\n    on held-out gold-standard splits. Report ASV alongside downstream effect estimates\n    for each task. Compare ASV interpretability with raw confusion matrix reporting.\n    Report Type I/II error rates: rejection rate under null (Type I) and power under\n    alternative, before and after ASV-informed correction, across all task × model\n    combinations. F1 vs downstream causal bias analysis: for each model × task, compute\n    classification F1 and plot against |downstream bias|. Demonstrate that high F1\n    does not guarantee low downstream bias (Baumann 2025: F1>0.93 still >50% error\n    risk). This bridges the gap between annotation quality metrics and causal estimate\n    reliability.\n\n    '\n  status: planned\n- id: plan_007\n  claim: 3\n  description: 'Correction guidance framework: decision mapping + validation'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_004\n  - plan_003\n  details: 'Decision framework: {topology × error structure × ASV} → correction method\n    (DSL / PPI / MLA / MC-SIMEX / naive plug-in / \"no existing method adequate\").\n    MC validation: recommended method produces least bias in ≥90% of scenarios. Empirical\n    validation on plan_003 data. Characterize regimes where no existing method suffices\n    (correlated errors, differential multi-class, etc.) — identify as open problems.\n\n    '\n  status: planned\n- id: plan_009\n  claim: 1\n  description: Pathological confusion matrix analysis (near-permutation, rank-deficient)\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  registry_id: plan009_pathological_matrices\n  details: 'Extreme C structures: near-permutation, rank-deficient, block-diagonal.\n    Characterize when bias becomes catastrophic across topologies. Identify structural\n    conditions (spectral gap, diagonal dominance ratio) that predict bias severity\n    — candidate features for practitioners.\n\n    '\n  status: DONE\n  conclusion: success\n  metrics:\n    regression_dichotomy:\n      benign_topologies:\n        list:\n        - confounding\n        - mediation\n        - collider\n        - frontdoor\n        - mbias\n        R2_range: 0.61-0.77\n        primary_predictor: effective_rank\n        secondary_predictors:\n        - spectral_gap\n        - condition_number\n      dangerous_topologies:\n        list:\n        - exposure\n        - iv\n        exposure_R2: 0.11\n        iv_R2: ~0\n        iv_note: regression has no explanatory power — Wald denominator sign reversal\n          is discrete, not predicted by continuous matrix features\n        exposure_note: 'near_perm eps=0.01: 15% catastrophic bias above threshold'\n      global_R2: ~0 (cross-topology aggregation destroys predictive power — different\n        bias mechanisms)\n    risk_tiers:\n      low:\n        topologies:\n        - mbias\n        max_bias: <0.04\n        note: safe even under worst-case pathological C\n      medium:\n        topologies:\n        - confounding\n        - mediation\n        - collider\n        - frontdoor\n        bias_range: 0.1-0.31\n        catastrophic_fraction: 0%\n        R2: 0.70-0.77\n        note: bounded bias, matrix features predictive\n      high:\n        topologies:\n        - exposure\n        - iv\n        note: 'catastrophic regardless of C quality — exposure: structural identification\n          failure; IV: Wald estimator explosion (near_perm eps=0.01 cat=61-73%, rank-deficient\n          bias reaches millions)'\n    most_consistent_predictor: condition_number (significant in 5/5 medium-risk topologies)\n    hypothesis_assessment:\n      H1_predictable_catastrophic: partially — risk tier determined by topology, not\n        C features\n      H2_matrix_features_strong: topology-dependent — 5/7 R²>0.6, exposure/IV fail\n      H3_safety_threshold: not confirmed — boundary is topology-based, not C-feature\n        threshold\n      H4_diagnostic_features: partially — condition_number most consistent, but needs\n        topology-specific criteria\n    iv_filtering:\n      n_filtered: 3000\n      n_total: 28000\n      pct_infinite: 10.7\n      note: non-finite Wald values silently filtered from regression; must note in\n        paper\n    pathological_C_types:\n    - near_permutation (eps=0.01,0.05,0.1,0.2)\n    - rank_deficient\n    - block_diagonal\n    K_values:\n    - 3\n    - 5\n    - 7\n    M_per_config: 1000\n    N_per_sim: 5000000\n    runtime_seconds: 25\n    analysis_report: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md\n    output_files:\n      summary_json: /home/sonny/causal_annot_error_attrib/artifacts/plan009/pathological_bias_summary.json\n      regression_txt: /home/sonny/causal_annot_error_attrib/artifacts/plan009/regression_results.txt\n      analysis_md: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md\n- id: plan_010\n  claim: 1\n  description: annot-sensitivity Python toolkit (open-source release)\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_004\n  - plan_007\n  details: 'Package: user-specified DAG + confusion matrix(es) + downstream estimate\n    → bias expressions (scalar K≤3, matrix K>3 with interpretability) + ASV bounds\n    + sensitivity curves + correction recommendation + diagnostic plots. pip-installable,\n    with worked examples for each topology.\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_confounding_dag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    theory_mc_match: 6/6\n    pass_criteria: 3/3\n    max_binary_collapse_delta: 0.103\n    bias_range: 0.132-0.298\n    ovb_reference: 0.3\n    direction_reversal_found: false\n    random_search_100k_min_bias: 0.063\n- exp_id: mvp_exposure_dag\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    theory_mc_match: 5/5\n    pass_criteria: 3/3\n    violation_rate: 0.85\n    sign_reversal_rate: 0.834\n    amplification_rate: 0.141\n    K2_toward_null: 6/6\n    worst_severity: 2.83\n    named_structures_with_violation: 3/6\n- exp_id: mvp_exposure_dirichlet_subspace\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_space_violation: 0.849\n    full_space_sign_rev: 0.833\n    full_space_amplif: 0.275\n    diag50_violation: 0.325\n    diag50_sign_rev: 0.216\n    diag50_amplif: 0.113\n    diag70_violation: 0.137\n    diag70_sign_rev: 0.021\n    diag70_amplif: 0.117\n    diag90_violation: 0.119\n    diag90_sign_rev: 0\n    diag90_amplif: 0.119\n    samples_per_subspace: 50000\n    assessment: ALL subspaces STRONG (>10%)\n- exp_id: plan001_dag_taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    collider:\n      all_coef:\n        violation: 1\n        sign_flip: 0.688\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 0\n      small_tau_0.05:\n        tau_I: 0.015733\n        tau_violation: 0.96\n        tau_sign_flip: 0\n        tau_amplification: 0.992\n      small_tau_0.1:\n        tau_I: 0.06118\n        tau_violation: 0.974\n        tau_sign_flip: 0\n        tau_amplification: 0.995\n    mbias:\n      all_coef:\n        violation: 1\n        sign_flip: 0.651\n        amplification: 0.112\n      tau_specific:\n        violation: 0.532\n        sign_flip: 0\n        amplification: 0.104\n      misclass_amplifies_rate: 0.292\n      small_tau_0.05:\n        tau_I: 0.057669\n        tau_violation: 0.532\n        tau_sign_flip: 0\n        tau_amplification: 0.104\n      small_tau_0.1:\n        tau_I: 0.107669\n        tau_violation: 0.532\n        tau_sign_flip: 0\n        tau_amplification: 0.104\n    mediation_mixed:\n      all_coef:\n        violation: 1\n        sign_flip: 0.835\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    mediation_same:\n      all_coef:\n        violation: 1\n        sign_flip: 0.666\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    frontdoor_mixed:\n      all_coef:\n        violation: 1\n        sign_flip: 0.998\n        amplification: 1\n      tau_specific:\n        violation: 1\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 1\n      small_tau_0.05:\n        tau_I: 0.050177\n        lambda_U: 0.1\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_I: 0.100169\n        lambda_U: 0.2\n        tau_violation: 1\n        tau_sign_flip: 0\n        tau_amplification: 1\n    frontdoor_same:\n      all_coef:\n        violation: 1\n        sign_flip: 1\n        amplification: 1\n      tau_specific:\n        violation: 0.999\n        sign_flip: 0\n        amplification: 1\n      misclass_amplifies_rate: 0.9997\n      small_tau_0.05:\n        tau_I: 0.050177\n        lambda_U: 0.1\n        tau_violation: 0.999\n        tau_sign_flip: 0\n        tau_amplification: 1\n      small_tau_0.1:\n        tau_I: 0.100169\n        lambda_U: 0.2\n        tau_violation: 0.999\n        tau_sign_flip: 0\n        tau_amplification: 1\n    iv_note: 'IV metrics not computed in plan_001 (only 6 fixed C structures tested,\n      no dedicated IV tau_specific analysis). First measured in plan_002: 52% tau_specific_sign_flip\n      from 100k random C (Wald denominator sign reversal). See plan002_k57_extension\n      for full IV results.'\n- exp_id: plan003_empirical_confusion_matrices\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    status_detail: PAUSED - API 402 Payment Required (OPENROUTER_API_KEY)\n    api_endpoint: http://47.94.22.126/v1/chat/completions\n    data_dir: results/\n    humaid_recount_20260520T2312:\n      deepseek_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      deepseek_few-shot-3:\n        total: 1500\n        pred_valid: 1345\n        errors: 155\n        error_type: parsing\n        status: WARN\n      deepseek_few-shot-5:\n        total: 1500\n        pred_valid: 1237\n        errors: 263\n        error_type: parsing\n        status: WARN\n      llama4_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      llama4_few-shot-3:\n        total: 1500\n        pred_valid: 1498\n        errors: 2\n        status: OK\n      llama4_few-shot-5:\n        total: 1500\n        pred_valid: 1471\n        errors: 29\n        status: WARN\n      qwen3_zero-shot:\n        total: 1500\n        pred_valid: 1500\n        errors: 0\n        status: OK\n      qwen3_few-shot-3:\n        total: 1500\n        pred_valid: 1423\n        errors: 77\n        error_type: '402'\n        status: WARN\n      qwen3_few-shot-5:\n        total: 1500\n        pred_valid: 0\n        errors: 1500\n        error_type: '402'\n        status: FAIL\n    humaid_summary: 4 OK (≥1498) + 4 WARN (1237-1471) + 1 FAIL (qwen3_fs5 all 402)\n    humaid_usable: 8/9 files have valid data\n    data_fields:\n      true_label: gold_label\n      pred_label: pred_label\n    note: deepseek errors are parsing/format, NOT 402. Only qwen3 errors are 402.\n- exp_id: plan004_asv_framework\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    v2_sign_flip_filter: ✅ effective (Type I=0%, power=100%)\n    v3_envelope_monotonicity: ✅ solved (0 violations)\n    v3_magnitude_reporting: ✅ informative values for all topologies\n    v3_magnitude_filter: ❌ rejected (scale-dependent, not viable as binary test)\n    v3_fixed_signif_filter: ✅ Type I=0% all topologies, power=100% for τ≥0.1\n    v3_significance_filter:\n      confounding_tau005:\n        type_i: 0\n        power: 1\n      confounding_tau010:\n        type_i: 0\n        power: 1\n      mediation_tau005:\n        type_i: 0\n        power: 0\n      mediation_tau010:\n        type_i: 0\n        power: 1\n      collider_tau005:\n        type_i: 0\n        power: 0\n      collider_tau010:\n        type_i: 0\n        power: 1\n      note: τ=0.05 mediation/collider power=0% is correct — attenuating topologies\n        are fragile at small effects\n    v3_fixed_status: complete — significance filter validated\n    v3_envelope_violations: 0\n    v3_magnitude_asv_tau0.5_range: 0.076-0.487\n    v3_magnitude_asv_tau0.05_range: 0.008-0.047\n    v3_magnitude_asv_tau0.1_range: 0.014-0.093\n    v3_coverage_tau0.05: 100.0%\n    v3_coverage_tau0.1: 100.0%\n    n_sensitivity_mediation_tau005:\n      topology: mediation\n      tau: 0.05\n      C0: sym_mild\n      mc_reps: 500\n      N_1000:\n        naive_power: 0.89\n        asv_power: 0\n        median_se: 0.070025\n        median_signif_asv: 0\n      N_2000:\n        naive_power: 0.998\n        asv_power: 0\n        median_se: 0.049649\n        median_signif_asv: 0\n      N_5000:\n        naive_power: 1\n        asv_power: 0\n        median_se: 0.031301\n        median_signif_asv: 0\n      N_10000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.022152\n        median_signif_asv: null\n      N_20000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.01566\n        median_signif_asv: null\n      N_50000:\n        naive_power: 1\n        asv_power: 1\n        median_se: 0.009903\n        median_signif_asv: null\n      recovery_N: 10000\n      interpretation: 'Sharp phase transition at N~6000-10000. Below: 1.96*SE > tau=0.05\n        so signif_ASV=0 (ASV kills all rejections). Above: 1.96*SE < tau=0.05 so signif_ASV=None\n        (infinite robustness), ASV passes all.'\n- exp_id: plan008_binarization_collapse\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    confounding:\n      D_mean: 0.0253\n      D_med: 0.0182\n      D_P95: 0.0733\n      D_max: 0.2213\n      frac_gt_001: 0.686\n      frac_gt_005: 0.138\n      sign_flip: 0\n    mediation:\n      D_mean: 0.0446\n      D_med: 0.0355\n      D_P95: 0.1179\n      D_max: 0.252\n      frac_gt_001: 0.835\n      frac_gt_005: 0.36\n      sign_flip: 0\n    collider:\n      D_mean: 0.0169\n      D_med: 0.0125\n      D_P95: 0.0472\n      D_max: 0.1069\n      frac_gt_001: 0.572\n      frac_gt_005: 0.039\n      sign_flip: 0\n    M-bias:\n      D_mean: 0.0063\n      D_med: 0.0054\n      D_P95: 0.0147\n      D_max: 0.0328\n      frac_gt_001: 0.181\n      frac_gt_005: 0\n      sign_flip: 0\n    exposure:\n      D_mean: 0.5164\n      D_med: 0.506\n      D_P95: 0.8453\n      D_max: 1.3876\n      frac_gt_001: 1\n      frac_gt_005: 0.999\n      sign_flip: 0.14\n    IV:\n      D_mean: 0.926\n      D_med: 0.9394\n      D_P95: 1.3426\n      D_max: 2.0809\n      frac_gt_001: 1\n      frac_gt_005: 1\n      sign_flip: 0.175\n- exp_id: plan005_asv_extended\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    envelope_violations:\n      mbias: 0\n      iv: 0\n      frontdoor: 0\n    plim_at_identity:\n      mbias: 0.5128\n      iv: 0.6598\n      frontdoor: 0.4998\n    asv_tau05:\n      mbias:\n        sign_flip: null\n        magnitude_10pct: null\n      iv:\n        sign_flip_range: 1.1-6.7\n        magnitude_10pct_range: 0.101-0.607\n      frontdoor:\n        sign_flip: null\n        magnitude_10pct_range: 0.064-0.387\n    mc_coverage:\n      mbias_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      mbias_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n      iv_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      iv_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n      frontdoor_tau005:\n        plim_acc: 1\n        bias_bounded: 1\n      frontdoor_tau01:\n        plim_acc: 1\n        bias_bounded: 1\n    v_fixed_signif_filter:\n      mbias:\n        type_i: 0\n        power_tau005: 95.8-99.2%\n        power_tau01: 100%\n      iv:\n        type_i: 0\n        power_tau005: 0%\n        power_tau01: 0%\n        note: correct — Wald estimator immediately fragile, signif_ASV≈0 blocks all\n          rejections\n      frontdoor:\n        type_i: 0\n        power_tau005: 100%\n        power_tau01: 100%\n    fixes_applied:\n    - 'C1: compute_signif_asv_fast added'\n    - 'C2: magnitude ASV tau≈0 returns 0.0'\n    - 'W1: IV tau_true=plim_iv(I)=0.6598'\n    - 'W2: M-bias tau_true=plim_mb(I)=0.5128'\n    fixed_script: /home/sonny/causal_annot_error_attrib/plan_005_asv_extended_fixed.py\n    runtime_seconds: 46.2\n- exp_id: plan_004_asv_v3_fixed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan002_k57_extension\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_k_comparison_7topo:\n      confounding:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.993\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1614\n          worst_case_diag70: 0.2744\n          worst_case_diag50: 0.2993\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1107\n          worst_case_diag70: 0.2156\n          worst_case_diag50: 0.2462\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0933\n          worst_case_diag70: 0.1859\n          worst_case_diag50: 0.2264\n      mediation:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.838\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1223\n          worst_case_diag70: 0.251\n          worst_case_diag50: 0.3032\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.966\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0867\n          worst_case_diag70: 0.1832\n          worst_case_diag50: 0.2396\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0607\n          worst_case_diag70: 0.1421\n          worst_case_diag50: 0.1879\n      collider:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.666\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0503\n          worst_case_diag70: 0.1064\n          worst_case_diag50: 0.1256\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.955\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0477\n          worst_case_diag70: 0.1087\n          worst_case_diag50: 0.1306\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.992\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0352\n          worst_case_diag70: 0.0826\n          worst_case_diag50: 0.1131\n      exposure:\n        K3:\n          tau_specific_sign_flip: N/A (all-coef fallback; MVP beta1 flip=83.4%)\n          all_coef_sign_flip: 0.99\n          violation: 1\n          amplification: 0.999\n          worst_case_diag90: 0.2726\n          worst_case_diag70: 0.7092\n          worst_case_diag50: 1.1438\n        K5:\n          tau_specific_sign_flip: N/A (all-coef fallback)\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 0.998\n          worst_case_diag90: 0.2097\n          worst_case_diag70: 0.5782\n          worst_case_diag50: 0.8784\n        K7:\n          tau_specific_sign_flip: N/A (all-coef fallback)\n          all_coef_sign_flip: 1\n          violation: 1\n          amplification: 0.999\n          worst_case_diag90: 0.1853\n          worst_case_diag70: 0.4913\n          worst_case_diag50: 0.7441\n      mbias:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.667\n          violation: 0.584\n          amplification: 0.089\n          worst_case_diag90: 0.0106\n          worst_case_diag70: 0.0226\n          worst_case_diag50: 0.0287\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.954\n          violation: 1\n          amplification: 0\n          worst_case_diag90: 0.0154\n          worst_case_diag70: 0.0374\n          worst_case_diag50: 0.0487\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.992\n          violation: 1\n          amplification: 0\n          worst_case_diag90: 0.0133\n          worst_case_diag70: 0.0319\n          worst_case_diag50: 0.0449\n      iv:\n        K3:\n          tau_specific_sign_flip: 0.526\n          all_coef_sign_flip: 0.526\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.2993\n          worst_case_diag70: 1.6444\n          worst_case_diag50: 14.0463\n          note: Wald estimator extremely unstable at low accuracy\n        K5:\n          tau_specific_sign_flip: 0.514\n          all_coef_sign_flip: 0.514\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.4053\n          worst_case_diag70: 2.1036\n          worst_case_diag50: 9.6932\n        K7:\n          tau_specific_sign_flip: 0.523\n          all_coef_sign_flip: 0.523\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.3605\n          worst_case_diag70: 1.8132\n          worst_case_diag50: 8.2204\n      frontdoor:\n        K3:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.836\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1407\n          worst_case_diag70: 0.2604\n          worst_case_diag50: 0.2966\n        K5:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.967\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.1057\n          worst_case_diag70: 0.2066\n          worst_case_diag50: 0.2507\n        K7:\n          tau_specific_sign_flip: 0\n          all_coef_sign_flip: 0.993\n          violation: 1\n          amplification: 1\n          worst_case_diag90: 0.0785\n          worst_case_diag70: 0.1646\n          worst_case_diag50: 0.2119\n    conclusion_summary:\n      structural_guarantee: tau_specific_sign_flip = 0% across ALL K for 5/7 topologies\n        (confounding/mediation/collider/mbias/frontdoor)\n      iv_new_finding: IV ~52% tau sign flip (K-invariant) — Wald denominator sign\n        reversal under random C\n      exposure_clarification: Exposure tau_spec_sflip column is all-coef fallback.\n        Actual beta1-specific flip rate = 83.4% (from MVP)\n      worst_case_trend: Decreasing with K for 5/7 topologies (K=3 most conservative).\n        IV catastrophic at low accuracy (WC_d50 up to 14x). Exposure decreasing.\n      mbias_special: Amplification drops to 0% at K>=5\n      rng_fix: Deterministic per-(topo,K,threshold) seeds via SHA-256. Previous values\n        had RNG ordering artifact.\n    runtime_seconds: 20\n    gpu: RTX 5090 cuda:0\n    script: /home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py\n- exp_id: plan009_pathological_matrices\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    regression_dichotomy:\n      benign_topologies:\n        list:\n        - confounding\n        - mediation\n        - collider\n        - frontdoor\n        - mbias\n        R2_range: 0.61-0.77\n        primary_predictor: effective_rank\n        secondary_predictors:\n        - spectral_gap\n        - condition_number\n      dangerous_topologies:\n        list:\n        - exposure\n        - iv\n        exposure_R2: 0.11\n        iv_R2: ~0\n        iv_note: regression has no explanatory power — Wald denominator sign reversal\n          is discrete, not predicted by continuous matrix features\n        exposure_note: 'near_perm eps=0.01: 15% catastrophic bias above threshold'\n      global_R2: ~0 (cross-topology aggregation destroys predictive power — different\n        bias mechanisms)\n    risk_tiers:\n      low:\n        topologies:\n        - mbias\n        max_bias: <0.04\n        note: safe even under worst-case pathological C\n      medium:\n        topologies:\n        - confounding\n        - mediation\n        - collider\n        - frontdoor\n        bias_range: 0.1-0.31\n        catastrophic_fraction: 0%\n        R2: 0.70-0.77\n        note: bounded bias, matrix features predictive\n      high:\n        topologies:\n        - exposure\n        - iv\n        note: 'catastrophic regardless of C quality — exposure: structural identification\n          failure; IV: Wald estimator explosion (near_perm eps=0.01 cat=61-73%, rank-deficient\n          bias reaches millions)'\n    most_consistent_predictor: condition_number (significant in 5/5 medium-risk topologies)\n    hypothesis_assessment:\n      H1_predictable_catastrophic: partially — risk tier determined by topology, not\n        C features\n      H2_matrix_features_strong: topology-dependent — 5/7 R²>0.6, exposure/IV fail\n      H3_safety_threshold: not confirmed — boundary is topology-based, not C-feature\n        threshold\n      H4_diagnostic_features: partially — condition_number most consistent, but needs\n        topology-specific criteria\n    iv_filtering:\n      n_filtered: 3000\n      n_total: 28000\n      pct_infinite: 10.7\n      note: non-finite Wald values silently filtered from regression; must note in\n        paper\n    pathological_C_types:\n    - near_permutation (eps=0.01,0.05,0.1,0.2)\n    - rank_deficient\n    - block_diagonal\n    K_values:\n    - 3\n    - 5\n    - 7\n    M_per_config: 1000\n    N_per_sim: 5000000\n    runtime_seconds: 25\n    analysis_report: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md\n    output_files:\n      summary_json: /home/sonny/causal_annot_error_attrib/artifacts/plan009/pathological_bias_summary.json\n      regression_txt: /home/sonny/causal_annot_error_attrib/artifacts/plan009/regression_results.txt\n      analysis_md: /home/sonny/causal_annot_error_attrib/artifacts/plan009/plan009_analysis.md\n- exp_id: plan007_correction_guidance\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_combos: 210\n    runtime_sec: 2792\n    ppi_grand_mean_bias_red: 93.8%\n    ppi_grand_mean_coverage: 96.8%\n    ppi_win_rate: 95.2% (40/42)\n    mcsimex_grand_mean_bias_red: 20.9%\n    dsl_grand_mean_bias_red: -144.8%\n    naive_plugin_grand_mean_bias_red: -20.0%\n    mla_grand_mean_bias_red: -37.4%\n    fwl_invariance_verified: true\n    fwl_invariance_topologies: confounding, mediation, collider, mbias (0.0% bias_red\n      for naive/mla)\n    dsl_effective_topologies: confounding (49.8%), mediation (70.3%)\n    dsl_failure_topologies: mbias (-768%), iv (-187%), collider (-89%), exposure (-60%),\n      frontdoor (-29%)\n    ppi_weakness: 'mbias+realistic_llm: -25.1% bias_red (but 99% coverage)'\n- exp_id: plan010_annot_sensitivity_toolkit\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tests_passed: 35/35\n    modules: 7\n    topologies: 7\n    correction_methods: 5\n    lines_of_code:\n      __init__.py: 53\n      bias.py: 174\n      asv.py: 119\n      correction.py: 422\n      confusion.py: 129\n      dgp.py: 213\n      utils.py: 95\n      test_core.py: 35 tests\n    example_output:\n      confounding_k3_bias_pct: +10.20%\n      magnitude_asv: 0.967\n      sign_flip_asv: null\n      recommended_with_gold: ppi\n      recommended_without_gold: dsl\n- exp_id: plan006_asv_empirical\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_scenarios: 210\n    configs: 14\n    topologies: 7\n    k_values:\n    - 2\n    - 3\n    - 10\n    models:\n    - llama4\n    - deepseek\n    - qwen3\n    - qwen2.5-7b\n    sign_flips: 0\n    overall_asv_unsafe_pct: 43.8\n    k2_mean_bias_pct: 36.9\n    k3_mean_bias_pct: 65.3\n    k10_mean_bias_pct: 12.2\n    k2_iv_bias_pct: 116.5\n    k3_iv_bias_pct: 252.3\n    k10_iv_bias_pct: 30.3\n    f1_disconnect: civil_comments F1=0.72-0.75 but IV bias 101-131%\n    7b_vs_235b_bias_ratio: 1.24\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T05:23:15.208Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T05:23:15.208Z",
  "sessionId": "1006286d-c975-40d7-97b7-3d8681efc2df"
}
```

---

## Round 1

6 recorded events

### User

_source line 3 · 2026-05-21T05:23:15.241Z_

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
focus: Re-dream after targeted fixes to all 5 cross-tier structural issues from previous Dream (best 4/6, median 4/6, worst 3.5/6). Key improvements: (1) Related work 31 refs (from ~11), (2) ASV vs PBA delineation, (3) Brenner reconciliation, (4) IV Dirichlet subspace appendix, (5) Non-differential stress test in progress. Paper: 6 figures, formal proofs, 16 pages (8+8), 31 citations.

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
  "promptId": "8548fc34-12cf-4176-8b87-7028de2774b2",
  "type": "user",
  "uuid": "5860bcc1-8332-4775-9ce7-5efbb44ba80c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "1006286d-c975-40d7-97b7-3d8681efc2df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T05:23:15.238Z_

```json
{
  "parentUuid": "5860bcc1-8332-4775-9ce7-5efbb44ba80c",
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
  "uuid": "d834857b-c602-4a12-ac8e-097951cf86b2",
  "timestamp": "2026-05-21T05:23:15.238Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "1006286d-c975-40d7-97b7-3d8681efc2df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T05:23:15.238Z_

```json
{
  "parentUuid": "d834857b-c602-4a12-ac8e-097951cf86b2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8c4e909f-2d70-4631-87fa-313a81a5a996",
  "timestamp": "2026-05-21T05:23:15.238Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "1006286d-c975-40d7-97b7-3d8681efc2df",
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
  "leafUuid": "8c4e909f-2d70-4631-87fa-313a81a5a996",
  "sessionId": "1006286d-c975-40d7-97b7-3d8681efc2df"
}
```

---

### Assistant

_source line 7 · 2026-05-21T05:23:15.583Z_

You've hit your limit · resets 2am (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c4e909f-2d70-4631-87fa-313a81a5a996",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "1503bcf9-3723-4732-bcd8-9c40a4c7567e",
  "error": "rate_limit",
  "isApiErrorMessage": true,
  "apiErrorStatus": 429,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510",
  "sessionId": "1006286d-c975-40d7-97b7-3d8681efc2df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "1a69b7e9-6c88-495b-b67c-201cac76489a",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

### Runtime record

_source line 8_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "1503bcf9-3723-4732-bcd8-9c40a4c7567e",
  "sessionId": "1006286d-c975-40d7-97b7-3d8681efc2df"
}
```

---
