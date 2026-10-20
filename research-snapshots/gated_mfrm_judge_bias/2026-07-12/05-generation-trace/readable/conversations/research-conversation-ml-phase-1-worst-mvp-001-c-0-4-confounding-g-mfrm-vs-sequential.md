# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：真实污染量级接近 mvp_001（c̄ < 0.4），confounding 在真实数据上不可区分于噪声，G-MFRM vs sequential 无

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/791573df-b046-4c58-adaa-08eaeb0c70c3.jsonl`
- **Structured JSON:** [`e6f8d80b0530770f192c.json`](../../sessions/e6/e6f8d80b0530770f192c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T20:58:12.852Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T20:58:12.852Z",
  "sessionId": "791573df-b046-4c58-adaa-08eaeb0c70c3",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：真实污染量级接近 mvp_001（c̄ < 0.4），confounding 在真实数据上不可区分于噪声，G-MFRM vs sequential 无统计显著差异\n核心假设：['真实 c_n 分布均值 < 0.4，多数模型污染信号微弱（主流 LLM 的 benchmark 污染已被缓解）', 'ConStat e_i 在真实数据上噪声大（rank correlation < 0.65），exposure 信号不可靠', 'd_j 与 c_n·e_i 近似正交（|ρ| < 0.1），confounding 实际不发生', 'G-MFRM 和 sequential 在 Kendall-τ 上差异不显著（p > 0.1）', '收敛可能有问题（c_n 先验主导后验，数据信息量不足）']\n关键指标范围：{'real_c_n_mean': [0.05, 0.4], 'kendall_tau_gmfrm': [0.82, 0.86], 'kendall_tau_best_baseline': [0.82, 0.86], 'delta_tau_vs_best_baseline': [-0.01, 0.01], 'rmse_reduction_vs_sequential_pct': [-2, 8], 'confounding_theta_rmse_degradation_pct': [0, 5], 'scatter_pearson_r_seq_bias': [0.0, 0.25], 'convergence_max_rhat': [1.0, 1.1], 'convergence_min_ess': [50, 300], 'wilcoxon_p_joint_vs_seq': [0.05, 0.8]}\n叙事方向：核心 confounding claim 在真实数据上不成立——污染量级不足以产生可观测 confounding。 需要彻底 reframe，但不降级 venue。三个可选 pivot angle（按可行性排序）： (1) \"Diagnostic Framework\" 角度——G-MFRM 本身是一个统计检验工具：当 c_n 后验 集中在零附近时，恰恰是 G-MFRM 给出的 \"当前主流 benchmark 污染已不严重\"  的实证结论，这本身有发表价值（negative result + methodology）。论文 reframe 为 \"我们提出 G-MFRM 作为联合诊断框架，在合成数据上验证其检测力（mvp_003）， 在真实数据上发现当前污染已被缓解——但框架为未来监测提供了现成工具\"。 (2) \"Judge Bias as Main Story\" 角度——放弃污染联合估计为核心卖点， 转而强调 multi-facet judge bias 建模本身：G-MFRM 的 MFRM 部分（d_j 估计） 已经比 raw average 和部分 baseline 更好，论文重新聚焦于 judge severity  的细粒度建模和公平评分。(3) \"Controlled Contamination Injection\" 角度—— 在真实数据上人工注入已知量级的污染（fine-tune 部分模型在 benchmark 上）， 验证 G-MFRM 在受控设定下的检测和校正能力。这增加实验成本但保住原始 framing。 无论哪个 angle，exp-009 的 formal proposition 仍然成立（理论贡献不依赖实证量级）， 可作为论文的方法论贡献保留。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gated_mfrm_judge_bias\nvenue: emnlp-2026\nfocus: 核心关注：(1) confounding claim 的实证强度是否足够支撑 AAAI 投稿 (2) 真实数据 contamination 量级若接近 mvp_001 (弱) 而非 mvp_002 (强) 时论文 story 是否仍站得住 (3) DG-IRT 迁移的 novelty 是否被 reviewer 认可 (4) 7 个 baselines 的覆盖是否充分\n\n## paper_framing.md\n\n# Paper Framing — gated_mfrm_judge_bias\n\n## Target Venue\n- Primary: AAAI 2027 (full paper, deadline July 28, 2026)\n- Backup: ACL 2027 via ARR (submission August 3, 2026)\n- Timeline: ~68 days from today (2026-05-21)\n\n## Core Insight\nSequential approaches to judge bias correction and contamination adjustment produce biased model ability estimates due to omitted variable confounding. Joint estimation within a single psychometric calibration framework is methodologically necessary, not merely convenient.\n\n## Core Claims (3 条，均可证伪)\n\n1. **Confounding Claim**: When judge severity (d_j) and contamination susceptibility (c_n·e_i) are both present but only one is modeled, the unmodeled facet's effect is absorbed into other parameter estimates, producing systematic bias in model ability rankings. Sequential pipelines (bias-first or contamination-first) do not resolve this confounding.\n\n2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — jointly estimates model ability, item difficulty, judge severity, and contamination susceptibility in a single calibration, yielding bias-and-contamination-corrected \"fair scores.\"\n\n3. **Empirical Claim**: G-MFRM fair scores achieve higher agreement with human rankings (Chatbot Arena votes, Kendall-τ) than all baselines: raw multi-judge averages, bias-only correction (CyclicJudge, UDA), contamination-only adjustment (DCR), and naive sequential pipelines.\n\n## Story Spine\n\n- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.\n\n- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. No existing work (0/12 surveyed papers, through May 2026) jointly models both within a single calibration framework.\n\n- **Our framing**: Joint estimation is methodologically necessary. We formalize this as an omitted variable bias problem: under non-orthogonality of d_j and c_n·e_i, sequential estimators are asymptotically biased (direction determined by covariance sign). G-MFRM resolves this by estimating all facets simultaneously, with a three-stage procedure ensuring identifiability: (1) standard MFRM for initial estimates, (2) external exposure anchoring via ConStat + temporal signals, (3) joint gated model with c_n as latent parameters.\n\n- **Headline result template**: \"On MT-Bench/Arena-Hard with 8 LLM judges, G-MFRM fair scores achieve X% higher Kendall-τ with Chatbot Arena human votes than the best sequential baseline, while simultaneously producing interpretable per-model contamination estimates and per-judge severity profiles.\"\n\n## Narrative Strategy (from distilled writing)\n\n- **Type**: \"突破局限\" (sequential has structural flaw) + \"统一框架\" (G-MFRM unifies both corrections)\n- **Opening hook**: Quantitative shock — lead with confounding's θ-RMSE degradation (43.8% in synthetic, to be validated on real data)\n- **Section 2**: Toy example / formal proposition demonstrating confounding before introducing G-MFRM method\n- **Figure 1**: Left = sequential pipeline with confounding annotation, Right = joint G-MFRM with gating mechanism highlighted\n- **Main result table**: rows = methods (7 baselines + G-MFRM), cols = benchmarks × metrics\n- **Ablation**: Full numbers (not checkmark grid), rows = components on/off\n\n## Venue Fit Risks\n\n- **AAAI**: Good fit for psychometric methodology applied to AI evaluation. Risk: reviewers may lack MFRM/IRT background — need clear, self-contained exposition with toy examples. Strength: AAAI values formal modeling + practical impact.\n- **ACL/ARR**: Good fit for LLM evaluation methodology. Risk: may demand stronger NLP-specific contributions beyond the measurement framework. Strength: directly relevant to LLM evaluation community.\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"Why not CyclicJudge + discard contaminated items?\"** — Item discard wastes information; CyclicJudge doesn't capture item-specific judge effects; neither produces c_n for auditing; G-MFRM degrades gracefully to standard MFRM when contamination ≈ 0.\n\n2. **\"Is confounding large enough in practice?\"** — MVP synthetic: 43.8% RMSE degradation. Real-data calibration (P0 experiment) will establish realistic contamination magnitude. Bias scatter (r=0.65) shows the mechanism exists regardless of magnitude.\n\n3. **\"Rank-1 assumption (c_n·e_i) too strong\"** — Rank-1 is LLTM tradition, good approximation when contamination comes from dominant data source. Person-fit diagnostics (infit/outfit) detect violations. Rank-k extension is future work.\n\n4. **\"DG-IRT transfer is trivial\"** — Three structural differences require non-trivial adaptation: binary→continuous exposure, single-rater→multi-facet, known→unknown exposure status. Stage 2 external anchoring solves a fundamental obstacle (exposure unknown to administrator) absent in educational testing.\n\n5. **\"Contamination signal realistic?\"** — ConStat validated r²=0.94 with true contamination effects. LogProber provides per-item memorization indicators. Multiple indicators combined via weighted composite. P0 experiment calibrates against real benchmarks.\n\n## MVP Evidence Summary\n\n- mvp_003: Joint RMSE −43.8% vs Sequential (p=1e-6), Kendall-τ +6.3pp, R̂=1.03, ESS=224\n- Bias scatter: Pearson r=0.65 (sequential systematically overestimates high-c_n models)\n- Robustness: method effective even under model misspecification (DGP with s_j, model without)\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: multi_judge_data_collection\n  claim: 3\n  description: 'Collect multi-judge evaluation data on MT-Bench and Arena-Hard using\n    8+ judges: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B,\n    Qwen3.6-27B, Llama 4 Maverick, + 1 additional. Evaluate 20+ target models. Position\n    swap for pairwise.'\n  priority: P0\n  gpu_budget_hours: 130\n  deps: []\n  notes: Open-source judges via vLLM on RTX 6000. Proprietary judges via API (~$900\n    budget). Position swap doubles evaluation count.\n  status: planned\n- id: exp-002\n  name: constat_exposure_estimation\n  claim: 2\n  description: 'Estimate per-item exposure e_i via ConStat: generate reference benchmark\n    variants (rephrased by GPT-5.5/Claude), validate human equivalence, compute ConStat\n    delta scores. Combine with temporal signals where available.'\n  priority: P0\n  gpu_budget_hours: 30\n  deps:\n  - exp-001\n  notes: ConStat is black-box, validated r²=0.94. Reference variant quality is critical\n    — need human equivalence check on sample.\n  status: planned\n- id: exp-003\n  name: gmfrm_real_data_fit\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Fit G-MFRM three-stage pipeline on real data from exp-001/002. Stage\n    1: MFRM (θ,b,d). Stage 2: e_i from exp-002. Stage 3: Joint gated model. Compare\n    fair scores θ̂ with Chatbot Arena human votes (Kendall-τ).'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - exp-001\n  - exp-002\n  notes: NumPyro MCMC. Use MVP MCMC settings (warmup=2000, samples=4000, chains=4,\n    NCP, target_accept=0.95).\n  status: planned\n- id: exp-004\n  name: baseline_comparison\n  claim: 3\n  description: 'Compare G-MFRM against 7 baselines on same data: (1) raw multi-judge\n    average, (2) MFRM-only, (3) sequential pipeline, (4) CyclicJudge, (5) DCR Factor,\n    (6) UDA, (7) Preference Leakage calibration. Metrics: Kendall-τ, Spearman-ρ with\n    Chatbot Arena.'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-003\n  notes: CyclicJudge and UDA need reimplementation or adaptation from public code.\n    DCR requires their inference pipeline.\n  status: planned\n- id: exp-005\n  name: contamination_magnitude_calibration\n  claim: 1\n  description: 'Estimate real contamination magnitude: compare fitted c_n from exp-003\n    with synthetic MVP assumptions. Determine if real contamination is closer to mvp_001\n    (c~0.5, weak) or mvp_002 (c~1.5, strong). Critical for claim strength.'\n  priority: P0\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  notes: 'Reviewer flagged: if real c ≈ mvp_001 level, paper impact weakens. This\n    experiment determines claim calibration.'\n  status: planned\n- id: exp-006\n  name: judge_count_sensitivity\n  claim: 2\n  description: 'Sensitivity analysis: vary number of judges (2, 4, 6, 8+) and measure\n    G-MFRM performance degradation. At what minimum judge count does G-MFRM still\n    outperform sequential?'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - exp-003\n  status: planned\n- id: exp-007\n  name: exposure_indicator_ablation\n  claim: 2\n  description: 'Ablation: contribution of each exposure indicator (ConStat delta,\n    temporal signal, LogProber Safe Score) to e_i estimation quality. Leave-one-out\n    analysis.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - exp-002\n  - exp-003\n  status: planned\n- id: exp-008\n  name: facet_fit_diagnostics\n  claim: 2\n  description: 'Measurement quality validation: report infit/outfit MNSQ for all facets\n    (θ, b, d, c). Flag misfitting elements. Compare Stage 1 person-fit (lz, EMRi)\n    vs Stage 3 c_n as construct coherence validation.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  name: confounding_formal_proposition\n  claim: 1\n  description: 'Formal bias analysis: derive first-order bias approximation for sequential\n    estimator under d_j/c_n·e_i non-orthogonality. Validate via Monte Carlo simulation\n    across realistic parameter ranges. For paper Section 2.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps: []\n  notes: Can run in parallel with data collection. Extends MVP synthetic analysis\n    to formal proposition.\n  status: planned\n- id: exp-010\n  name: wildbench_replication\n  claim: 3\n  description: Replicate G-MFRM pipeline on WildBench as third benchmark. Cross-benchmark\n    generalization.\n  priority: P2\n  gpu_budget_hours: 40\n  deps:\n  - exp-003\n  status: planned\n- id: exp-011\n  name: adversarial_robustness\n  claim: 2\n  description: Test G-MFRM robustness against adversarial contamination following\n    Wang et al. (ICLR 2026) fragility findings.\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - exp-003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    convergence: PASS\n    rho_0.0:\n      joint_gmfrm:\n        RMSE: 0.1540±0.0269\n        tau: 0.9042±0.0445\n      sequential:\n        RMSE: 0.1540±0.0242\n        tau: 0.9016±0.0467\n      p_value: 0.4782\n    rho_0.3:\n      joint_gmfrm:\n        RMSE: 0.1521±0.0283\n        tau: 0.9068±0.0419\n      sequential:\n        RMSE: 0.1527±0.0236\n        tau: 0.9011±0.0452\n      p_value: 0.3506\n    rho_0.6:\n      joint_gmfrm:\n        RMSE: 0.1529±0.0285\n        tau: 0.9047±0.0418\n      sequential:\n        RMSE: 0.1537±0.0237\n        tau: 0.9037±0.0419\n      p_value: 0.3921\n    rho_0.0_no_degradation_p: 0.9563\n    runtime_seconds: 1675.6\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL (convergence)\n    convergence:\n      max_rhat: 1.05\n      min_ess: 47\n      pass: false\n    wilcoxon_joint_vs_seq:\n      p_value: 1.0e-06\n      pass: true\n    rmse_reduction: 32.8%\n    raw_average:\n      RMSE: 0.8063±0.0841\n      tau: 0.8401±0.0347\n    mfrm_only:\n      RMSE: 0.2539±0.0449\n      tau: 0.8390±0.0351\n    sequential:\n      RMSE: 0.2211±0.0376\n      tau: 0.8596±0.0291\n    joint_gmfrm:\n      RMSE: 0.1486±0.0199\n      tau: 0.9028±0.0181\n    runtime_seconds: 1935.4\n    scatter_pearson_r: 0.6534\n    scatter_p: 0\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    convergence:\n      max_rhat: 1.03\n      min_ess: 224\n      pass: true\n    wilcoxon_joint_vs_seq:\n      p_value: 1.0e-06\n      pass: true\n    rmse_reduction: 43.8%\n    raw_average:\n      RMSE: 0.8063±0.0841\n      tau: 0.8401±0.0347\n    mfrm_only:\n      RMSE: 0.2539±0.0448\n      tau: 0.8388±0.0345\n    sequential:\n      RMSE: 0.2211±0.0376\n      tau: 0.8593±0.0293\n    joint_gmfrm:\n      RMSE: 0.1243±0.0164\n      tau: 0.9223±0.0098\n    runtime_seconds: 4385.5\n    kendall_tau_joint: 0.9223\n    kendall_tau_seq: 0.8593\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T20:58:12.855Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T20:58:12.855Z",
  "sessionId": "791573df-b046-4c58-adaa-08eaeb0c70c3"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T20:58:12.873Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：真实污染量级接近 mvp_001（c̄ < 0.4），confounding 在真实数据上不可区分于噪声，G-MFRM vs sequential 无统计显著差异
核心假设：['真实 c_n 分布均值 < 0.4，多数模型污染信号微弱（主流 LLM 的 benchmark 污染已被缓解）', 'ConStat e_i 在真实数据上噪声大（rank correlation < 0.65），exposure 信号不可靠', 'd_j 与 c_n·e_i 近似正交（|ρ| < 0.1），confounding 实际不发生', 'G-MFRM 和 sequential 在 Kendall-τ 上差异不显著（p > 0.1）', '收敛可能有问题（c_n 先验主导后验，数据信息量不足）']
关键指标范围：{'real_c_n_mean': [0.05, 0.4], 'kendall_tau_gmfrm': [0.82, 0.86], 'kendall_tau_best_baseline': [0.82, 0.86], 'delta_tau_vs_best_baseline': [-0.01, 0.01], 'rmse_reduction_vs_sequential_pct': [-2, 8], 'confounding_theta_rmse_degradation_pct': [0, 5], 'scatter_pearson_r_seq_bias': [0.0, 0.25], 'convergence_max_rhat': [1.0, 1.1], 'convergence_min_ess': [50, 300], 'wilcoxon_p_joint_vs_seq': [0.05, 0.8]}
叙事方向：核心 confounding claim 在真实数据上不成立——污染量级不足以产生可观测 confounding。 需要彻底 reframe，但不降级 venue。三个可选 pivot angle（按可行性排序）： (1) "Diagnostic Framework" 角度——G-MFRM 本身是一个统计检验工具：当 c_n 后验 集中在零附近时，恰恰是 G-MFRM 给出的 "当前主流 benchmark 污染已不严重"  的实证结论，这本身有发表价值（negative result + methodology）。论文 reframe 为 "我们提出 G-MFRM 作为联合诊断框架，在合成数据上验证其检测力（mvp_003）， 在真实数据上发现当前污染已被缓解——但框架为未来监测提供了现成工具"。 (2) "Judge Bias as Main Story" 角度——放弃污染联合估计为核心卖点， 转而强调 multi-facet judge bias 建模本身：G-MFRM 的 MFRM 部分（d_j 估计） 已经比 raw average 和部分 baseline 更好，论文重新聚焦于 judge severity  的细粒度建模和公平评分。(3) "Controlled Contamination Injection" 角度—— 在真实数据上人工注入已知量级的污染（fine-tune 部分模型在 benchmark 上）， 验证 G-MFRM 在受控设定下的检测和校正能力。这增加实验成本但保住原始 framing。 无论哪个 angle，exp-009 的 formal proposition 仍然成立（理论贡献不依赖实证量级）， 可作为论文的方法论贡献保留。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: gated_mfrm_judge_bias
venue: emnlp-2026
focus: 核心关注：(1) confounding claim 的实证强度是否足够支撑 AAAI 投稿 (2) 真实数据 contamination 量级若接近 mvp_001 (弱) 而非 mvp_002 (强) 时论文 story 是否仍站得住 (3) DG-IRT 迁移的 novelty 是否被 reviewer 认可 (4) 7 个 baselines 的覆盖是否充分

## paper_framing.md

# Paper Framing — gated_mfrm_judge_bias

## Target Venue
- Primary: AAAI 2027 (full paper, deadline July 28, 2026)
- Backup: ACL 2027 via ARR (submission August 3, 2026)
- Timeline: ~68 days from today (2026-05-21)

## Core Insight
Sequential approaches to judge bias correction and contamination adjustment produce biased model ability estimates due to omitted variable confounding. Joint estimation within a single psychometric calibration framework is methodologically necessary, not merely convenient.

## Core Claims (3 条，均可证伪)

1. **Confounding Claim**: When judge severity (d_j) and contamination susceptibility (c_n·e_i) are both present but only one is modeled, the unmodeled facet's effect is absorbed into other parameter estimates, producing systematic bias in model ability rankings. Sequential pipelines (bias-first or contamination-first) do not resolve this confounding.

2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — jointly estimates model ability, item difficulty, judge severity, and contamination susceptibility in a single calibration, yielding bias-and-contamination-corrected "fair scores."

3. **Empirical Claim**: G-MFRM fair scores achieve higher agreement with human rankings (Chatbot Arena votes, Kendall-τ) than all baselines: raw multi-judge averages, bias-only correction (CyclicJudge, UDA), contamination-only adjustment (DCR), and naive sequential pipelines.

## Story Spine

- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.

- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. No existing work (0/12 surveyed papers, through May 2026) jointly models both within a single calibration framework.

- **Our framing**: Joint estimation is methodologically necessary. We formalize this as an omitted variable bias problem: under non-orthogonality of d_j and c_n·e_i, sequential estimators are asymptotically biased (direction determined by covariance sign). G-MFRM resolves this by estimating all facets simultaneously, with a three-stage procedure ensuring identifiability: (1) standard MFRM for initial estimates, (2) external exposure anchoring via ConStat + temporal signals, (3) joint gated model with c_n as latent parameters.

- **Headline result template**: "On MT-Bench/Arena-Hard with 8 LLM judges, G-MFRM fair scores achieve X% higher Kendall-τ with Chatbot Arena human votes than the best sequential baseline, while simultaneously producing interpretable per-model contamination estimates and per-judge severity profiles."

## Narrative Strategy (from distilled writing)

- **Type**: "突破局限" (sequential has structural flaw) + "统一框架" (G-MFRM unifies both corrections)
- **Opening hook**: Quantitative shock — lead with confounding's θ-RMSE degradation (43.8% in synthetic, to be validated on real data)
- **Section 2**: Toy example / formal proposition demonstrating confounding before introducing G-MFRM method
- **Figure 1**: Left = sequential pipeline with confounding annotation, Right = joint G-MFRM with gating mechanism highlighted
- **Main result table**: rows = methods (7 baselines + G-MFRM), cols = benchmarks × metrics
- **Ablation**: Full numbers (not checkmark grid), rows = components on/off

## Venue Fit Risks

- **AAAI**: Good fit for psychometric methodology applied to AI evaluation. Risk: reviewers may lack MFRM/IRT background — need clear, self-contained exposition with toy examples. Strength: AAAI values formal modeling + practical impact.
- **ACL/ARR**: Good fit for LLM evaluation methodology. Risk: may demand stronger NLP-specific contributions beyond the measurement framework. Strength: directly relevant to LLM evaluation community.

## Anticipated Reviewer Concerns & Responses

1. **"Why not CyclicJudge + discard contaminated items?"** — Item discard wastes information; CyclicJudge doesn't capture item-specific judge effects; neither produces c_n for auditing; G-MFRM degrades gracefully to standard MFRM when contamination ≈ 0.

2. **"Is confounding large enough in practice?"** — MVP synthetic: 43.8% RMSE degradation. Real-data calibration (P0 experiment) will establish realistic contamination magnitude. Bias scatter (r=0.65) shows the mechanism exists regardless of magnitude.

3. **"Rank-1 assumption (c_n·e_i) too strong"** — Rank-1 is LLTM tradition, good approximation when contamination comes from dominant data source. Person-fit diagnostics (infit/outfit) detect violations. Rank-k extension is future work.

4. **"DG-IRT transfer is trivial"** — Three structural differences require non-trivial adaptation: binary→continuous exposure, single-rater→multi-facet, known→unknown exposure status. Stage 2 external anchoring solves a fundamental obstacle (exposure unknown to administrator) absent in educational testing.

5. **"Contamination signal realistic?"** — ConStat validated r²=0.94 with true contamination effects. LogProber provides per-item memorization indicators. Multiple indicators combined via weighted composite. P0 experiment calibrates against real benchmarks.

## MVP Evidence Summary

- mvp_003: Joint RMSE −43.8% vs Sequential (p=1e-6), Kendall-τ +6.3pp, R̂=1.03, ESS=224
- Bias scatter: Pearson r=0.65 (sequential systematically overestimates high-c_n models)
- Robustness: method effective even under model misspecification (DGP with s_j, model without)


## experiment_plan (with registry status)

- id: exp-001
  name: multi_judge_data_collection
  claim: 3
  description: 'Collect multi-judge evaluation data on MT-Bench and Arena-Hard using
    8+ judges: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B,
    Qwen3.6-27B, Llama 4 Maverick, + 1 additional. Evaluate 20+ target models. Position
    swap for pairwise.'
  priority: P0
  gpu_budget_hours: 130
  deps: []
  notes: Open-source judges via vLLM on RTX 6000. Proprietary judges via API (~$900
    budget). Position swap doubles evaluation count.
  status: planned
- id: exp-002
  name: constat_exposure_estimation
  claim: 2
  description: 'Estimate per-item exposure e_i via ConStat: generate reference benchmark
    variants (rephrased by GPT-5.5/Claude), validate human equivalence, compute ConStat
    delta scores. Combine with temporal signals where available.'
  priority: P0
  gpu_budget_hours: 30
  deps:
  - exp-001
  notes: ConStat is black-box, validated r²=0.94. Reference variant quality is critical
    — need human equivalence check on sample.
  status: planned
- id: exp-003
  name: gmfrm_real_data_fit
  claim:
  - 1
  - 2
  - 3
  description: 'Fit G-MFRM three-stage pipeline on real data from exp-001/002. Stage
    1: MFRM (θ,b,d). Stage 2: e_i from exp-002. Stage 3: Joint gated model. Compare
    fair scores θ̂ with Chatbot Arena human votes (Kendall-τ).'
  priority: P0
  gpu_budget_hours: 15
  deps:
  - exp-001
  - exp-002
  notes: NumPyro MCMC. Use MVP MCMC settings (warmup=2000, samples=4000, chains=4,
    NCP, target_accept=0.95).
  status: planned
- id: exp-004
  name: baseline_comparison
  claim: 3
  description: 'Compare G-MFRM against 7 baselines on same data: (1) raw multi-judge
    average, (2) MFRM-only, (3) sequential pipeline, (4) CyclicJudge, (5) DCR Factor,
    (6) UDA, (7) Preference Leakage calibration. Metrics: Kendall-τ, Spearman-ρ with
    Chatbot Arena.'
  priority: P0
  gpu_budget_hours: 20
  deps:
  - exp-003
  notes: CyclicJudge and UDA need reimplementation or adaptation from public code.
    DCR requires their inference pipeline.
  status: planned
- id: exp-005
  name: contamination_magnitude_calibration
  claim: 1
  description: 'Estimate real contamination magnitude: compare fitted c_n from exp-003
    with synthetic MVP assumptions. Determine if real contamination is closer to mvp_001
    (c~0.5, weak) or mvp_002 (c~1.5, strong). Critical for claim strength.'
  priority: P0
  gpu_budget_hours: 5
  deps:
  - exp-003
  notes: 'Reviewer flagged: if real c ≈ mvp_001 level, paper impact weakens. This
    experiment determines claim calibration.'
  status: planned
- id: exp-006
  name: judge_count_sensitivity
  claim: 2
  description: 'Sensitivity analysis: vary number of judges (2, 4, 6, 8+) and measure
    G-MFRM performance degradation. At what minimum judge count does G-MFRM still
    outperform sequential?'
  priority: P1
  gpu_budget_hours: 10
  deps:
  - exp-003
  status: planned
- id: exp-007
  name: exposure_indicator_ablation
  claim: 2
  description: 'Ablation: contribution of each exposure indicator (ConStat delta,
    temporal signal, LogProber Safe Score) to e_i estimation quality. Leave-one-out
    analysis.'
  priority: P1
  gpu_budget_hours: 10
  deps:
  - exp-002
  - exp-003
  status: planned
- id: exp-008
  name: facet_fit_diagnostics
  claim: 2
  description: 'Measurement quality validation: report infit/outfit MNSQ for all facets
    (θ, b, d, c). Flag misfitting elements. Compare Stage 1 person-fit (lz, EMRi)
    vs Stage 3 c_n as construct coherence validation.'
  priority: P1
  gpu_budget_hours: 5
  deps:
  - exp-003
  status: planned
- id: exp-009
  name: confounding_formal_proposition
  claim: 1
  description: 'Formal bias analysis: derive first-order bias approximation for sequential
    estimator under d_j/c_n·e_i non-orthogonality. Validate via Monte Carlo simulation
    across realistic parameter ranges. For paper Section 2.'
  priority: P1
  gpu_budget_hours: 10
  deps: []
  notes: Can run in parallel with data collection. Extends MVP synthetic analysis
    to formal proposition.
  status: planned
- id: exp-010
  name: wildbench_replication
  claim: 3
  description: Replicate G-MFRM pipeline on WildBench as third benchmark. Cross-benchmark
    generalization.
  priority: P2
  gpu_budget_hours: 40
  deps:
  - exp-003
  status: planned
- id: exp-011
  name: adversarial_robustness
  claim: 2
  description: Test G-MFRM robustness against adversarial contamination following
    Wang et al. (ICLR 2026) fragility findings.
  priority: P2
  gpu_budget_hours: 15
  deps:
  - exp-003
  status: planned


## registry (completed experiments)

- exp_id: mvp_001
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    verdict: FAIL
    convergence: PASS
    rho_0.0:
      joint_gmfrm:
        RMSE: 0.1540±0.0269
        tau: 0.9042±0.0445
      sequential:
        RMSE: 0.1540±0.0242
        tau: 0.9016±0.0467
      p_value: 0.4782
    rho_0.3:
      joint_gmfrm:
        RMSE: 0.1521±0.0283
        tau: 0.9068±0.0419
      sequential:
        RMSE: 0.1527±0.0236
        tau: 0.9011±0.0452
      p_value: 0.3506
    rho_0.6:
      joint_gmfrm:
        RMSE: 0.1529±0.0285
        tau: 0.9047±0.0418
      sequential:
        RMSE: 0.1537±0.0237
        tau: 0.9037±0.0419
      p_value: 0.3921
    rho_0.0_no_degradation_p: 0.9563
    runtime_seconds: 1675.6
- exp_id: mvp_002
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    verdict: FAIL (convergence)
    convergence:
      max_rhat: 1.05
      min_ess: 47
      pass: false
    wilcoxon_joint_vs_seq:
      p_value: 1.0e-06
      pass: true
    rmse_reduction: 32.8%
    raw_average:
      RMSE: 0.8063±0.0841
      tau: 0.8401±0.0347
    mfrm_only:
      RMSE: 0.2539±0.0449
      tau: 0.8390±0.0351
    sequential:
      RMSE: 0.2211±0.0376
      tau: 0.8596±0.0291
    joint_gmfrm:
      RMSE: 0.1486±0.0199
      tau: 0.9028±0.0181
    runtime_seconds: 1935.4
    scatter_pearson_r: 0.6534
    scatter_p: 0
- exp_id: mvp_003
  name: ''
  status: DONE
  conclusion: success
  metrics:
    verdict: PASS
    convergence:
      max_rhat: 1.03
      min_ess: 224
      pass: true
    wilcoxon_joint_vs_seq:
      p_value: 1.0e-06
      pass: true
    rmse_reduction: 43.8%
    raw_average:
      RMSE: 0.8063±0.0841
      tau: 0.8401±0.0347
    mfrm_only:
      RMSE: 0.2539±0.0448
      tau: 0.8388±0.0345
    sequential:
      RMSE: 0.2211±0.0376
      tau: 0.8593±0.0293
    joint_gmfrm:
      RMSE: 0.1243±0.0164
      tau: 0.9223±0.0098
    runtime_seconds: 4385.5
    kendall_tau_joint: 0.9223
    kendall_tau_seq: 0.8593

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: worst
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
  "promptId": "e3a948f0-24fc-4f8f-8c6c-68f08590afe7",
  "type": "user",
  "uuid": "633b9e94-5ee3-47e0-b6ab-5f5f18daff30",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "791573df-b046-4c58-adaa-08eaeb0c70c3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T20:58:12.872Z_

```json
{
  "parentUuid": "633b9e94-5ee3-47e0-b6ab-5f5f18daff30",
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
  "uuid": "86165160-f0ec-4b9b-b2b8-7732f3e7f359",
  "timestamp": "2026-05-21T20:58:12.872Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "791573df-b046-4c58-adaa-08eaeb0c70c3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T20:58:12.872Z_

```json
{
  "parentUuid": "86165160-f0ec-4b9b-b2b8-7732f3e7f359",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "94968067-c980-432e-b50a-fd33632d1b31",
  "timestamp": "2026-05-21T20:58:12.872Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "791573df-b046-4c58-adaa-08eaeb0c70c3",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：真实污染量级接近 mvp_001（c̄ < 0.4），confounding 在真实数据上不可区分于噪声，G-MFRM vs sequential 无统计显著差异 核心假设：['真实 c_n 分布均值 < 0.4，多数模型污染信号微弱（主流 LLM 的 benchmark 污染已被缓解）', 'ConSta…",
  "leafUuid": "94968067-c980-432e-b50a-fd33632d1b31",
  "sessionId": "791573df-b046-4c58-adaa-08eaeb0c70c3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Real data contamination magnitude calibration for G-MFRM",
  "sessionId": "791573df-b046-4c58-adaa-08eaeb0c70c3"
}
```

---

### Assistant

_source line 8 · 2026-05-21T20:58:41.809Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment_plan, under the "worst" tier scenario. Let me carefully go through each experiment and predict what would happen if the worst-case scenario is true (real contamination is weak, confounding is negligible, G-MFRM doesn't outperform sequential).

Let me map out the worst tier assumptions:
- Real c_n mean < 0.4 (weak contamination)
- ConStat exposure signals noisy (rank correlation < 0.65)
- d_j and c_n·e_i approximately orthogonal (|ρ| < 0.1)


- G-MFRM and sequential Kendall-τ difference not significant (p > 0.1)
- Convergence issues possible (prior dominates posterior)

Now I'm looking at the expected metric ranges for this worst-case scenario, where both methods perform similarly with Kendall-τ values hovering around 0.82-0.86, minimal differences between G-MFRM and the best baseline, and negligible or slightly negative improvements from the sequential approach.

Looking at the specific experiments, in the multi-judge data collection scenario, contamination remains weak enough that the data collection process itself succeeds, though the underlying signal is compromised. For the ConStat exposure estimation case, the worst outcome means the exposure estimates become noisy with poor signal-to-noise ratios in the e_i values.

Moving through the remaining experiments: G-MFRM will fit the real data but with posteriors clustering near zero under the prior, showing borderline convergence and correlation metrics similar to baselines. The baseline comparison reveals no significant performance advantage for G-MFRM when contamination is minimal. The contamination magnitude calibration experiment would confirm that real c_n values match the weak scenario. Finally, the judge count sensitivity analysis shows G-MFRM failing to demonstrate clear advantages across different judge counts since the contamination correction provides minimal benefit.

The exposure indicator ablation confirms all indicators contribute negligibly without a strong contamination signal. MFRM facets fit well overall but c_n shows poor fit and limited information. The formal proposition holds mathematically and validates under strong contamination in simulation, but lacks practical relevance for weak real-world contamination. The WildBench replication follows the same pattern with no significant G-MFRM advantage. Interestingly, G-MFRM might show some advantage under artificial adversarial contamination, but this doesn't strengthen the natural contamination narrative.

Now I'm formatting these findings into the YAML structure with detailed rationales...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94968067-c980-432e-b50a-fd33632d1b31",
  "isSidechain": false,
  "requestId": "req_011CbGPFFuSdsigkyg8XUheS",
  "type": "assistant",
  "uuid": "4cefb25b-59f9-4ed3-9017-0fdedc420915",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "791573df-b046-4c58-adaa-08eaeb0c70c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CVWPKNpgYXCUgbtXcqXHSg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10923,
      "cache_read_input_tokens": 11841,
      "output_tokens": 13392,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10923,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 13392,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10923
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

_source line 9 · 2026-05-21T21:02:27.849Z_

```yaml
tier: worst
narrative_guidance: >
  核心 confounding claim 在真实数据上不成立——污染量级不足以产生可观测 confounding。
  c_n 后验集中在零附近，先验主导后验，G-MFRM 退化为标准 MFRM。Sequential 与 joint
  无统计显著差异，因为被建模的 confounding 通道在真实数据上近乎关闭。
  需要彻底 reframe：推荐 pivot (1) "Diagnostic Framework" 角度——G-MFRM 作为联合
  诊断框架，在合成数据上验证检测力，在真实数据上给出"当前污染已被缓解"的实证结论，
  框架为未来监测提供现成工具。exp-009 的 formal proposition 作为方法论贡献保留，
  不依赖实证量级。论文核心贡献从 "correction" 转向 "detection + monitoring readiness"。

imagined_experiments:
  - name: multi_judge_data_collection
    plan_id: exp-001
    description: >
      收集 8 judge × 20+ target models 在 MT-Bench 和 Arena-Hard 上的多评委评分数据。
      Position swap 后总评估量约 8×20×2×(80+500)=185,600 次。
    expected_results:
      num_judges: 8
      num_target_models: 22
      num_benchmarks: 2
      total_evaluations: ~186000
      api_cost_usd: 870
      gpu_hours_used: 118
      missing_rate_pct: 1.2
      inter_judge_agreement_fleiss_kappa: 0.38
      position_bias_swap_disagreement_pct: 14.5
    result_rationale: >
      数据收集本身不受 contamination 量级影响，预期正常完成。
      inter-judge agreement 中等偏低（κ~0.38）反映 LLM judge 间固有差异——
      这本身支持 MFRM 建模 judge severity 的必要性。Position swap disagreement
      ~14.5% 是 MT-Bench/Arena-Hard 上的典型值。数据质量足以支撑下游分析，
      但不会改变"真实污染弱"的底层事实。
    tables:
      - name: "Table A1: Data Collection Summary"
        columns: [benchmark, num_items, num_judges, num_models, total_evals, missing_pct]
        rows:
          - [MT-Bench, 80, 8, 22, 28160, 0.8]
          - [Arena-Hard, 500, 8, 22, 176000, 1.3]
    figures_description:
      - "Figure S1: Judge agreement heatmap (8×8 pairwise Cohen's κ)，展示 judge 间系统性差异模式"
    analysis: >
      数据收集是中性步骤。关键观察：judge severity 的变异足够大（κ~0.38），
      说明 MFRM 对 d_j 的建模有实质价值——这为 pivot (2) "Judge Bias as Main Story"
      保留了空间。数据完整性和规模满足后续所有实验需求。

  - name: constat_exposure_estimation
    plan_id: exp-002
    description: >
      通过 ConStat 方法估计每个 benchmark item 的 exposure 指标 e_i：
      生成参考变体（rephrased），计算 delta scores，结合 temporal signals。
    expected_results:
      num_items_mtbench: 80
      num_items_arenahard: 500
      num_reference_variants_per_item: 3
      constat_delta_mean: 0.08
      constat_delta_std: 0.12
      constat_delta_median: 0.04
      items_with_significant_delta_pct: 12.0
      rank_correlation_constat_vs_temporal: 0.31
      human_equivalence_check_pass_rate_pct: 89
      e_i_distribution_skewness: 2.1
      effective_signal_items_pct: 15
    result_rationale: >
      worst 档下，真实污染量级弱（c̄ < 0.4），大多数 item 的 ConStat delta
      接近零（均值 0.08），因为模型在原题和变体上的表现差异主要来自噪声而非记忆。
      仅约 12% 的 item 有统计显著的 delta——这些可能对应少数确实被泄露的题目，
      但整体 exposure 信号微弱。e_i 分布高度右偏（skewness=2.1）：绝大多数
      item 的 e_i 接近零，少数 item 有中等信号。ConStat 与 temporal signal
      的 rank correlation 仅 0.31，说明两个 indicator 捕捉的是不同维度的噪声
      而非一致的污染信号。参考变体的人工等价性检查通过率 89% 是可接受的，
      说明变体质量不是瓶颈——问题在于污染本身就弱。
    tables:
      - name: "Table S2: Exposure Indicator Statistics"
        columns: [indicator, mean, std, median, pct_significant]
        rows:
          - [ConStat_delta, 0.08, 0.12, 0.04, 12.0]
          - [temporal_signal, 0.05, 0.09, 0.02, 8.5]
          - [composite_e_i, 0.07, 0.10, 0.03, 11.0]
    figures_description:
      - "Figure S2: e_i 分布直方图，展示高度右偏的 near-zero 集中模式，少量 item 有中等 exposure"
      - "Figure S3: ConStat delta vs temporal signal 散点图，r=0.31，两个 indicator 基本不相关"
    analysis: >
      exposure 信号的整体微弱是 worst 档的核心特征之一。这并非方法论失败——
      ConStat 在合成数据上 r²=0.94 是已验证的——而是反映真实数据中主流 LLM
      的 benchmark 污染确实已被缓解（训练数据清洗、instruction tuning 策略改进）。
      对 pivot (1) 有利：e_i 接近零本身就是 G-MFRM 框架产出的有价值诊断结论。
      但对原始 framing 致命：没有足够的 exposure 变异来驱动 c_n 估计。

  - name: gmfrm_real_data_fit
    plan_id: exp-003
    description: >
      在 exp-001/002 的真实数据上拟合 G-MFRM 三阶段流程。
      Stage 1: MFRM 估计 θ,b,d。Stage 2: 使用 exp-002 的 e_i。
      Stage 3: Joint gated model。与 Chatbot Arena 人类投票比较。
    expected_results:
      # Stage 1 MFRM
      stage1_convergence_max_rhat: 1.01
      stage1_convergence_min_ess: 820
      stage1_kendall_tau_arena: 0.843
      stage1_d_j_range: [-0.62, 0.71]
      stage1_d_j_std: 0.35
      # Stage 3 Joint
      stage3_convergence_max_rhat: 1.06
      stage3_convergence_min_ess: 112
      stage3_kendall_tau_arena: 0.851
      # c_n estimates
      c_n_posterior_mean: 0.14
      c_n_posterior_std: 0.11
      c_n_95ci_covers_zero_pct: 78
      c_n_prior_posterior_kl_divergence: 0.08
      # Comparison
      delta_tau_stage3_vs_stage1: 0.008
      wilcoxon_p_stage3_vs_stage1: 0.34
      runtime_seconds: 5200
    result_rationale: >
      Stage 1 MFRM 收敛良好（R̂=1.01, ESS=820），因为 MFRM 是成熟模型，
      judge severity d_j 有充足数据支撑。Stage 1 的 τ=0.843 反映 MFRM
      对 judge bias 的有效校正。Stage 3 joint model 收敛变差（R̂=1.06,
      ESS=112）——c_n 参数数据信息量不足时，MCMC 在先验附近 random walk，
      链间混合慢。c_n 后验均值仅 0.14，78% 的模型 c_n 的 95% 可信区间
      覆盖零，说明先验主导后验——数据中没有足够信号将 c_n 从先验拉开。
      prior-posterior KL 仅 0.08 进一步确认这一点。Stage 3 的 τ=0.851
      比 Stage 1 仅高 0.008，Wilcoxon p=0.34 远不显著。本质上 joint model
      退化为一个带噪声 c_n 项的 MFRM——gating 机制因 e_i 信号弱而几乎
      不激活，c_n 被先验钉在零附近，θ 估计基本等于 Stage 1 的 MFRM 估计。
    tables:
      - name: "Table 2: G-MFRM Real Data Fit Summary"
        columns: [stage, model, max_rhat, min_ess, tau_arena, num_params]
        rows:
          - [Stage 1, MFRM, 1.01, 820, 0.843, 110]
          - [Stage 3, G-MFRM Joint, 1.06, 112, 0.851, 132]
      - name: "Table S3: c_n Posterior Summary (Top 10 Models by c_n)"
        columns: [model, c_n_mean, c_n_std, "95%CI_lower", "95%CI_upper", covers_zero]
        rows:
          - [model_A, 0.38, 0.15, 0.09, 0.67, false]
          - [model_B, 0.31, 0.17, -0.02, 0.64, true]
          - [model_C, 0.27, 0.14, 0.00, 0.54, true]
          - ["...(remaining 19 models)", "0.02–0.22", "0.10–0.18", "—", "—", "mostly true"]
    figures_description:
      - "Figure 3: c_n posterior density plots (all 22 models)——绝大多数紧贴零，仅 1-2 个模型的后验偏离先验"
      - "Figure S4: Prior vs posterior comparison for c_n——overlay 展示先验主导后验的模式"
      - "Figure S5: θ Stage1 vs θ Stage3 散点图——几乎完美对角线（r=0.99），证实 joint 未实质改变 ability 估计"
    analysis: >
      这是 worst 档的决定性实验。c_n 先验主导后验是最核心的 red flag——
      说明真实数据中缺乏足够的污染信号来支撑 contamination 参数的估计。
      G-MFRM 有效退化为 MFRM。但注意 Stage 1 MFRM 本身表现良好（τ=0.843），
      d_j 估计有实质意义——这为 pivot (2) "Judge Bias as Main Story" 提供支撑。
      收敛不佳但未完全失败（R̂=1.06 在边界内），可解释为"模型参数化过度"
      而非"模型错误"。

  - name: baseline_comparison
    plan_id: exp-004
    description: >
      在相同数据上比较 G-MFRM 与 7 个 baselines。
    expected_results:
      raw_average_tau: 0.812
      raw_average_spearman: 0.847
      mfrm_only_tau: 0.843
      mfrm_only_spearman: 0.871
      sequential_tau: 0.845
      sequential_spearman: 0.873
      cyclicjudge_tau: 0.838
      cyclicjudge_spearman: 0.866
      dcr_factor_tau: 0.819
      dcr_factor_spearman: 0.853
      uda_tau: 0.841
      uda_spearman: 0.869
      pref_leakage_tau: 0.824
      pref_leakage_spearman: 0.858
      gmfrm_joint_tau: 0.851
      gmfrm_joint_spearman: 0.878
      delta_tau_gmfrm_vs_best_baseline: 0.006
      delta_tau_gmfrm_vs_sequential: 0.006
      wilcoxon_p_gmfrm_vs_sequential: 0.28
      wilcoxon_p_gmfrm_vs_mfrm: 0.31
      bootstrap_95ci_delta_tau: [-0.008, 0.021]
    result_rationale: >
      worst 档下所有方法的 τ 集中在 [0.81, 0.86] 的窄带内。G-MFRM（τ=0.851）
      名义上最高，但与 sequential（0.845）和 MFRM-only（0.843）的差异不显著
      （p=0.28, 0.31）。Bootstrap 95% CI 跨零（[-0.008, 0.021]）。
      关键观察：(a) raw average → MFRM-only 的提升（0.812→0.843, +0.031）
      是所有比较中最大且显著的，说明 judge bias 校正有真实价值；
      (b) MFRM-only → sequential → G-MFRM 的增量极小（0.843→0.845→0.851），
      说明 contamination 校正层在真实数据上几乎不贡献；
      (c) CyclicJudge（0.838）略低于 MFRM，因为 round-robin 丢弃了非循环数据；
      (d) DCR/Pref Leakage 仅做 contamination 调整，对 judge bias 无帮助，
      表现接近 raw average；(e) UDA（0.841）接近 MFRM，其神经 K-factor
      调整在实质上也是做 judge severity 校正。
      整体格局：judge bias 校正是真实有效的改进来源，contamination 校正
      在当前数据上不贡献增量。
    tables:
      - name: "Table 3: Main Results — Kendall-τ with Chatbot Arena"
        columns: [method, "MT-Bench τ", "Arena-Hard τ", "Average τ", "Spearman ρ", "p vs G-MFRM"]
        rows:
          - [Raw Average, 0.801, 0.823, 0.812, 0.847, 0.003]
          - [MFRM-only, 0.836, 0.850, 0.843, 0.871, 0.31]
          - [Sequential (bias→contam), 0.839, 0.851, 0.845, 0.873, 0.28]
          - [CyclicJudge, 0.831, 0.845, 0.838, 0.866, 0.14]
          - [DCR Factor, 0.810, 0.828, 0.819, 0.853, 0.008]
          - [UDA, 0.834, 0.848, 0.841, 0.869, 0.22]
          - [Pref Leakage, 0.815, 0.833, 0.824, 0.858, 0.012]
          - ["**G-MFRM (ours)**", "**0.845**", "**0.857**", "**0.851**", "**0.878**", "—"]
    figures_description:
      - "Figure 2: Bar chart of Kendall-τ with 95% bootstrap CI——所有 bias-aware 方法（MFRM, Sequential, CyclicJudge, UDA, G-MFRM）的 CI 大面积重叠"
      - "Figure S6: Pairwise Δτ heatmap with significance markers——仅 Raw Average 和 DCR/PrefLeakage 与 G-MFRM 的差异显著"
    analysis: >
      主结果表无法支撑 Empirical Claim (claim 3) 的原始表述（"higher agreement
      than all baselines"）。G-MFRM 名义最优但不显著优于 MFRM-only 和 sequential。
      但 MFRM 部分（judge bias 校正）相对 raw average 的改进是显著的（+0.031 τ），
      这支持 pivot (2)。对 pivot (1)，可 reframe 为"G-MFRM 在污染弱的环境下
      gracefully degrades 到 MFRM 水平而不损害性能——这正是框架的设计特性"。

  - name: contamination_magnitude_calibration
    plan_id: exp-005
    description: >
      将 exp-003 拟合的 c_n 与 MVP 合成假设对比，确定真实污染量级。
    expected_results:
      real_c_n_mean: 0.14
      real_c_n_median: 0.09
      real_c_n_std: 0.11
      real_c_n_max: 0.38
      real_c_n_interquartile_range: [0.04, 0.22]
      closest_mvp_scenario: mvp_001
      ratio_real_vs_mvp001_c_mean: 0.28
      ratio_real_vs_mvp002_c_mean: 0.09
      num_models_c_gt_0.3: 2
      num_models_c_gt_0.5: 0
      confounding_theta_rmse_degradation_pct: 2.1
      scatter_pearson_r_seq_bias: 0.11
    result_rationale: >
      c̄=0.14 远低于 mvp_001 的 c̄~0.5，甚至比 mvp_001 的最弱设定还低。
      仅 2/22 模型的 c_n > 0.3，没有模型达到 0.5。这意味着即使在 mvp_001
      那个已被判定为 FAIL 的合成场景中，污染信号也比真实数据强约 3.5 倍。
      confounding 导致的 θ-RMSE degradation 仅 2.1%（mvp_003 中为 43.8%），
      说明 confounding 通道在真实数据上近乎关闭。Sequential bias scatter
      的 Pearson r=0.11（mvp_003 中为 0.65），说明 sequential 估计器的系统性
      偏差在真实数据上不可观测——d_j 和 c_n·e_i 在真实数据上近似正交
      （因为 c_n 和 e_i 都太小，乘积项的方差可忽略）。
      结论明确：真实数据远在 mvp_001 以下，原始 confounding claim 在实证上不成立。
    tables:
      - name: "Table 4: Contamination Magnitude Calibration"
        columns: [scenario, c_mean, c_std, "θ-RMSE degradation %", "bias scatter r", "Wilcoxon p"]
        rows:
          - [Real Data, 0.14, 0.11, 2.1, 0.11, 0.34]
          - [mvp_001 (synthetic weak), 0.50, 0.25, 0.0, 0.05, 0.48]
          - [mvp_002 (synthetic strong, pre-fix), 1.50, 0.50, "—", 0.65, 1e-6]
          - [mvp_003 (synthetic strong, fixed), 1.50, 0.50, 43.8, 0.65, 1e-6]
    figures_description:
      - "Figure 4: c_n 分布对比——Real data vs mvp_001 vs mvp_003 的 violin plot，真实数据分布紧贴零"
      - "Figure 5: Confounding magnitude landscape——x=c_mean, y=θ-RMSE degradation %，标注三个 MVP 和 real data 的位置，展示 confounding 仅在 c_mean > 0.8 时变得显著"
    analysis: >
      这是论文 framing 的决定性实验。结果明确否定了原始 confounding claim 的
      实证基础。但这个"negative result"本身有价值：它是 G-MFRM 框架给出的
      实证诊断结论——"截至 2026 年中，主流 LLM 的 benchmark 污染已被缓解到
      不足以产生可观测 confounding 的水平"。Figure 5 的 landscape 图特别有用：
      它展示了 confounding 何时会成为问题（c_mean > 0.8），以及当前数据距离
      该阈值有多远。这支持 pivot (1) "Diagnostic Framework" 角度。

  - name: judge_count_sensitivity
    plan_id: exp-006
    description: >
      变化 judge 数量（2, 4, 6, 8），测量 G-MFRM 相对于 sequential 的性能变化。
    expected_results:
      tau_gmfrm_2judges: 0.803
      tau_gmfrm_4judges: 0.831
      tau_gmfrm_6judges: 0.844
      tau_gmfrm_8judges: 0.851
      tau_sequential_2judges: 0.798
      tau_sequential_4judges: 0.828
      tau_sequential_6judges: 0.841
      tau_sequential_8judges: 0.845
      delta_tau_2judges: 0.005
      delta_tau_4judges: 0.003
      delta_tau_6judges: 0.003
      delta_tau_8judges: 0.006
      p_significant_at_any_count: false
      tau_mfrm_only_2judges: 0.801
      tau_mfrm_only_4judges: 0.829
      tau_mfrm_only_6judges: 0.842
      tau_mfrm_only_8judges: 0.843
      min_judges_for_mfrm_benefit: 3
    result_rationale: >
      在 worst 档下，G-MFRM 在所有 judge 数量上都与 sequential 和 MFRM-only
      无显著差异——因为 contamination 校正层始终不贡献。judge 数量的主要效应
      是对 MFRM 部分（d_j 估计精度）的：2 judges 时 d_j 估计不稳定，τ 下降；
      4+ judges 时 MFRM 已接近饱和。G-MFRM 和 MFRM-only 在每个 judge count
      水平上几乎相同（差异 < 0.01），再次确认 contamination 通道无贡献。
      G-MFRM 在 2 judges 时的 R̂ 可能升至 1.08-1.10（c_n 更难识别），
      但因为 c_n 估计本就不影响输出，这不改变结论。
    tables:
      - name: "Table S5: Judge Count Sensitivity"
        columns: [num_judges, "τ Raw Avg", "τ MFRM", "τ Sequential", "τ G-MFRM", "Δτ G-MFRM vs Seq", "p-value"]
        rows:
          - [2, 0.778, 0.801, 0.798, 0.803, 0.005, 0.61]
          - [4, 0.802, 0.829, 0.828, 0.831, 0.003, 0.72]
          - [6, 0.810, 0.842, 0.841, 0.844, 0.003, 0.68]
          - [8, 0.812, 0.843, 0.845, 0.851, 0.006, 0.28]
    figures_description:
      - "Figure S7: τ vs judge count 折线图，四条线（Raw, MFRM, Sequential, G-MFRM）几乎重合（MFRM/Seq/G-MFRM），仅 Raw Average 明显低于其他"
    analysis: >
      结果展示 MFRM 的 judge bias 校正是性能提升的唯一来源，且 4+ judges 时
      已接近饱和。G-MFRM 的 contamination 通道在任何 judge count 下都不贡献。
      对论文有用的正面发现：MFRM 在仅 3-4 judges 时就有显著提升，这对实际
      评估场景（judge 资源有限）是实用性结论。可纳入 pivot (2) 的实用性讨论。

  - name: exposure_indicator_ablation
    plan_id: exp-007
    description: >
      Leave-one-out 消融：逐一移除 exposure indicator（ConStat, temporal, LogProber），
      评估对 e_i 估计和最终 G-MFRM 性能的影响。
    expected_results:
      full_composite_tau: 0.851
      drop_constat_tau: 0.849
      drop_temporal_tau: 0.850
      drop_logprober_tau: 0.851
      constat_only_tau: 0.850
      temporal_only_tau: 0.848
      logprober_only_tau: 0.849
      no_exposure_tau: 0.843  # equivalent to MFRM-only
      max_tau_drop_any_indicator: 0.003
      e_i_rank_correlation_full_vs_drop_constat: 0.72
      e_i_rank_correlation_full_vs_drop_temporal: 0.88
      e_i_rank_correlation_full_vs_drop_logprober: 0.91
    result_rationale: >
      worst 档下 exposure indicator 消融几乎不影响最终 τ——因为 e_i 信号
      本身就弱，c_n 先验主导后验，gating 通道近乎关闭。移除任何单个
      indicator 导致的 τ 变化 ≤ 0.003，远在噪声范围内。不同 indicator
      之间的 rank correlation 也不高（full vs drop-ConStat = 0.72），
      说明各 indicator 在弱信号下捕捉的是不同的噪声分量而非一致的污染信号。
      唯一显著的 drop 是移除全部 exposure（no_exposure_tau=0.843，即
      MFRM-only），这恰好是因为移除了整个 Stage 3——但这只是回退到
      Stage 1 MFRM，不是因为 exposure 信息有价值。
    tables:
      - name: "Table S6: Exposure Indicator Ablation"
        columns: [configuration, "e_i rank corr with full", "τ Arena", "Δτ vs full"]
        rows:
          - [Full composite, 1.00, 0.851, 0.000]
          - [Drop ConStat, 0.72, 0.849, -0.002]
          - [Drop temporal, 0.88, 0.850, -0.001]
          - [Drop LogProber, 0.91, 0.851, 0.000]
          - [ConStat only, "—", 0.850, -0.001]
          - [Temporal only, "—", 0.848, -0.003]
          - [LogProber only, "—", 0.849, -0.002]
          - [No exposure (MFRM-only), "—", 0.843, -0.008]
    figures_description:
      - "Figure S8: Ablation bar chart with error bars——所有包含任何 exposure 的配置 CI 完全重叠"
    analysis: >
      消融结果进一步确认 exposure 通道在真实数据上信息量不足。
      但对 pivot (1) 可 reframe 为：消融展示了 G-MFRM 的鲁棒性——
      当 exposure indicator 质量不同时，框架不依赖于任何单一 indicator，
      且当污染信号弱时自动退化为 MFRM 而不引入噪声。

  - name: facet_fit_diagnostics
    plan_id: exp-008
    description: >
      报告所有 facet（θ, b, d, c）的 infit/outfit MNSQ，标记 misfit 元素，
      比较 Stage 1 person-fit 指标与 Stage 3 c_n。
    expected_results:
      theta_infit_mean: 1.02
      theta_infit_range: [0.78, 1.31]
      theta_misfit_count: 1
      b_infit_mean: 1.00
      b_infit_range: [0.72, 1.45]
      b_misfit_count: 28
      d_infit_mean: 0.98
      d_infit_range: [0.85, 1.12]
      d_misfit_count: 0
      c_n_infit_mean: 1.05
      c_n_infit_range: [0.60, 1.82]
      c_n_misfit_count: 5
      lz_vs_c_n_correlation: 0.18
      emri_vs_c_n_correlation: 0.12
      stage1_person_fit_flagged_models: 3
      stage3_c_n_flagged_models: 2
      overlap_flagged: 1
    result_rationale: >
      θ 和 d 的 fit 良好（infit MNSQ 在 [0.7, 1.3] 的可接受范围内），
      说明 MFRM 对 ability 和 judge severity 的建模是充分的。b（item difficulty）
      有 28 个 misfit items（约 5%），这在 580 个 items 中是正常水平——
      部分 items 可能有多维性或猜测行为。c_n 的 infit 分布更宽（range
      达到 [0.60, 1.82]），5 个模型 misfit——但因为 c_n 先验主导后验，
      infit 的解释力有限（计算 infit 需要的 expected response 依赖于
      c_n 估计，而 c_n 本身不可靠）。lz 和 EMRi 与 c_n 的 correlation
      极低（0.18, 0.12），说明 Stage 1 的 person misfit 信号与 Stage 3
      的 contamination 估计基本不相关——进一步确认 c_n 不携带有意义的信息。
    tables:
      - name: "Table S7: Facet Fit Summary"
        columns: [facet, n_elements, infit_mean, infit_range, outfit_mean, outfit_range, misfit_count, misfit_pct]
        rows:
          - [θ (ability), 22, 1.02, "0.78–1.31", 1.04, "0.72–1.38", 1, 4.5]
          - [b (difficulty), 580, 1.00, "0.72–1.45", 1.02, "0.65–1.68", 28, 4.8]
          - [d (severity), 8, 0.98, "0.85–1.12", 0.99, "0.82–1.15", 0, 0.0]
          - [c (contamination), 22, 1.05, "0.60–1.82", 1.08, "0.55–2.01", 5, 22.7]
    figures_description:
      - "Figure S9: Infit/Outfit bubble chart per facet——d_j 紧凑聚集，c_n 散布最广"
      - "Figure S10: lz (Stage 1) vs c_n (Stage 3) 散点图，r=0.18，几乎无关联"
    analysis: >
      d_j 的优良 fit（0 misfit, 窄 range）是最有价值的发现——说明 MFRM
      对 judge severity 的建模在测量学意义上是可靠的。c_n 的高 misfit 率
      （22.7%）和宽 infit range 进一步表明 contamination facet 在数据中
      不是一个良定义的构念（construct）。对 pivot (2) 有力支持：d_j 是
      可靠的、有意义的测量维度，可作为论文核心贡献。

  - name: confounding_formal_proposition
    plan_id: exp-009
    description: >
      推导 sequential estimator 在 d_j/c_n·e_i 非正交条件下的一阶偏差近似。
      Monte Carlo 模拟验证理论预测。
    expected_results:
      proposition_holds: true
      bias_formula_validated: true
      monte_carlo_n_settings: 120
      bias_direction_correct_pct: 97.2
      bias_magnitude_relative_error_mean: 0.08
      bias_magnitude_relative_error_std: 0.05
      critical_rho_threshold: 0.15
      critical_c_mean_threshold: 0.6
      bias_negligible_below_c_mean: 0.4
      type1_error_rate: 0.048
    result_rationale: >
      形式命题是纯数学结果，不依赖真实数据量级——在 worst 档下仍然成立。
      Monte Carlo 验证覆盖 120 个参数设定（c_mean × ρ × N × J 的网格），
      偏差方向预测准确率 97.2%，量级相对误差 8%——理论近似在常规参数范围
      内有效。关键发现：偏差在 ρ > 0.15 且 c_mean > 0.6 时才变得实质性
      显著（> 5% RMSE degradation）。当 c_mean < 0.4（worst 档的真实数据范围），
      即使 ρ=0.6，偏差也可忽略——这恰好解释了为什么 exp-005 发现真实数据上
      confounding 不可观测。命题本身仍有价值：它精确描述了 confounding 何时
      会成为问题，为未来监测提供了定量阈值。
    tables:
      - name: "Table 1: Confounding Bias — Theoretical vs Monte Carlo"
        columns: [c_mean, rho, "bias_theory", "bias_MC_mean", "bias_MC_std", "θ-RMSE degradation %"]
        rows:
          - [0.2, 0.3, 0.003, 0.004, 0.002, 0.8]
          - [0.2, 0.6, 0.007, 0.008, 0.003, 1.9]
          - [0.5, 0.3, 0.019, 0.021, 0.006, 5.2]
          - [0.5, 0.6, 0.041, 0.044, 0.009, 12.7]
          - [1.0, 0.3, 0.078, 0.082, 0.015, 24.1]
          - [1.0, 0.6, 0.163, 0.171, 0.028, 43.5]
          - [1.5, 0.6, 0.245, 0.258, 0.041, 67.2]
    figures_description:
      - "Figure 1 (paper): Confounding bias heatmap——x=c_mean, y=ρ, color=θ-RMSE degradation %，标注 'current real data' 在左下角安全区域，'future risk zone' 在右上角"
      - "Figure S11: Theory vs MC scatter for all 120 settings——高度线性，slope≈1.05"
    analysis: >
      exp-009 是 worst 档下价值最高的实验。它将原始的"confounding 是现实问题"
      转化为"confounding 是条件性问题——我们精确刻画了何时会发生"。
      heatmap（Figure 1）成为论文最核心的可视化：当前真实数据落在安全区域，
      但随着未来模型训练策略变化（更多 benchmark 数据泄露），confounding
      可能重新激活。这完美支撑 pivot (1) "Diagnostic Framework"：
      G-MFRM 是一个"恒温器"——当温度低时显示安全，当温度升高时自动切换
      到校正模式。formal proposition + Monte Carlo validation 是不依赖
      实证量级的方法论贡献。

  - name: wildbench_replication
    plan_id: exp-010
    description: >
      在 WildBench 上复制 G-MFRM pipeline，检验跨 benchmark 泛化性。
    expected_results:
      wildbench_raw_avg_tau: 0.795
      wildbench_mfrm_tau: 0.826
      wildbench_sequential_tau: 0.828
      wildbench_gmfrm_tau: 0.832
      wildbench_delta_gmfrm_vs_seq: 0.004
      wildbench_wilcoxon_p: 0.42
      wildbench_c_n_mean: 0.11
      wildbench_c_n_covers_zero_pct: 82
      cross_benchmark_c_n_correlation: 0.35
      cross_benchmark_d_j_correlation: 0.78
    result_rationale: >
      WildBench 的污染量级预期更低（c̄=0.11 vs MT-Bench/Arena-Hard 的 0.14），
      因为 WildBench 是较新的 benchmark，训练数据泄露更少。G-MFRM 与
      sequential 的差异同样不显著（p=0.42）。跨 benchmark 的 c_n correlation
      仅 0.35——如果 c_n 反映真实污染，不同 benchmark 上同一模型的 c_n
      应正相关，0.35 说明 c_n 主要是噪声。但 d_j 跨 benchmark correlation
      达到 0.78——judge severity 是 judge 的稳定属性，跨 benchmark 一致——
      这进一步支持 d_j 作为有意义构念、c_n 作为噪声的解读。
    tables:
      - name: "Table S8: WildBench Replication Results"
        columns: [method, "WildBench τ", "MT-Bench τ", "Arena-Hard τ", "Average τ"]
        rows:
          - [Raw Average, 0.795, 0.801, 0.823, 0.806]
          - [MFRM-only, 0.826, 0.836, 0.850, 0.837]
          - [Sequential, 0.828, 0.839, 0.851, 0.839]
          - [G-MFRM, 0.832, 0.845, 0.857, 0.845]
    figures_description:
      - "Figure S12: Cross-benchmark c_n 散点图（MT-Bench vs WildBench），r=0.35——c_n 跨 benchmark 不稳定"
      - "Figure S13: Cross-benchmark d_j 散点图，r=0.78——judge severity 跨 benchmark 高度一致"
    analysis: >
      WildBench 复制完全符合 worst 档预期。c_n 跨 benchmark 不稳定（r=0.35）
      vs d_j 跨 benchmark 一致（r=0.78）是一个有力的对比——可论证 d_j
      是可靠的测量维度而 c_n 在当前数据上不是。这同时支持 pivot (1) 和 (2)。

  - name: adversarial_robustness
    plan_id: exp-011
    description: >
      测试 G-MFRM 对抗对抗性污染的鲁棒性（Wang et al. ICLR 2026 的 fragility attack）。
    expected_results:
      # Under adversarial injection (controlled c_n ≈ 1.0 for 5 models)
      adversarial_gmfrm_tau: 0.871
      adversarial_sequential_tau: 0.831
      adversarial_raw_avg_tau: 0.780
      adversarial_delta_gmfrm_vs_seq: 0.040
      adversarial_wilcoxon_p: 0.008
      adversarial_c_n_recovery_correlation: 0.82
      adversarial_c_n_mean_injected: 0.91
      adversarial_c_n_mean_clean: 0.10
      adversarial_convergence_max_rhat: 1.03
      adversarial_convergence_min_ess: 195
    result_rationale: >
      在人工注入强污染（c_n ≈ 1.0, 5 个模型 fine-tuned on benchmark）后，
      G-MFRM 重新获得显著优势：τ=0.871 vs sequential 的 0.831（p=0.008），
      RMSE reduction ~32%——接近 mvp_003 的合成结果。c_n recovery correlation
      达到 0.82（因为注入的污染足够强，c_n 后验能从先验中拉出）。
      收敛也改善（R̂=1.03, ESS=195）——数据中有足够信息驱动 c_n 估计。
      这证明 G-MFRM 的检测和校正机制在信号充分时确实有效——问题不是方法
      不工作，而是当前真实数据中信号不够强。adversarial experiment 同时
      验证了 exp-009 的理论预测：当 c_mean 提升到 ~1.0 时，confounding
      变得显著，G-MFRM 的联合估计优势重新显现。
    tables:
      - name: "Table S9: Adversarial Robustness — Clean vs Injected"
        columns: [setting, "τ Raw Avg", "τ MFRM", "τ Sequential", "τ G-MFRM", "Δτ G-MFRM vs Seq", "p-value"]
        rows:
          - [Clean (natural), 0.812, 0.843, 0.845, 0.851, 0.006, 0.28]
          - [Adversarial (5 models injected), 0.780, 0.821, 0.831, 0.871, 0.040, 0.008]
      - name: "Table S10: c_n Recovery Under Adversarial Injection"
        columns: [model_group, n_models, true_c_mean, estimated_c_mean, recovery_corr]
        rows:
          - [Injected, 5, 1.00, 0.91, 0.82]
          - [Clean, 17, 0.00, 0.10, "—"]
    figures_description:
      - "Figure S14: Clean vs Adversarial τ comparison bar chart——G-MFRM 在 adversarial setting 下优势明显"
      - "Figure S15: c_n true vs estimated scatter (adversarial)——injected models 被准确识别"
    analysis: >
      adversarial experiment 是 worst 档下的关键 "silver lining"。
      它证明 G-MFRM 方法论上是正确的——检测和校正机制在信号充分时有效——
      只是当前真实数据的信号不足。这完美支撑 pivot (1)：G-MFRM 是一个
      "备战"框架——当前安全但已验证可在威胁升级时启动。
      结合 pivot (3) "Controlled Contamination Injection"，adversarial
      experiment 可作为受控验证的自然延伸。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cefb25b-59f9-4ed3-9017-0fdedc420915",
  "isSidechain": false,
  "requestId": "req_011CbGPFFuSdsigkyg8XUheS",
  "type": "assistant",
  "uuid": "fd9b8ad7-486e-4410-87ae-0b8ae637c09a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "791573df-b046-4c58-adaa-08eaeb0c70c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CVWPKNpgYXCUgbtXcqXHSg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10923,
      "cache_read_input_tokens": 11841,
      "output_tokens": 13392,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10923,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 13392,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10923
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：真实污染量级接近 mvp_001（c̄ < 0.4），confounding 在真实数据上不可区分于噪声，G-MFRM vs sequential 无统计显著差异 核心假设：['真实 c_n 分布均值 < 0.4，多数模型污染信号微弱（主流 LLM 的 benchmark 污染已被缓解）', 'ConSta…",
  "leafUuid": "fd9b8ad7-486e-4410-87ae-0b8ae637c09a",
  "sessionId": "791573df-b046-4c58-adaa-08eaeb0c70c3"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Real data contamination magnitude calibration for G-MFRM",
  "sessionId": "791573df-b046-4c58-adaa-08eaeb0c70c3"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：真实污染量级接近 mvp_001（c̄ < 0.4），confounding 在真实数据上不可区分于噪声，G-MFRM vs sequential 无统计显著差异 核心假设：['真实 c_n 分布均值 < 0.4，多数模型污染信号微弱（主流 LLM 的 benchmark 污染已被缓解）', 'ConSta…",
  "leafUuid": "fd9b8ad7-486e-4410-87ae-0b8ae637c09a",
  "sessionId": "791573df-b046-4c58-adaa-08eaeb0c70c3"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Real data contamination magnitude calibration for G-MFRM",
  "sessionId": "791573df-b046-4c58-adaa-08eaeb0c70c3"
}
```

---
