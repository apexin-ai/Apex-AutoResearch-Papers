# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：部分跨模型验证——DeepSeek repo CLS 可用但弱于 Qwen，CWM 部分可解析使得差距缩小；C1 需 model-dependent

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/ef6bd922-f0b7-4766-ae72-4d9300a35f00.jsonl`
- **Structured JSON:** [`f4d0468397719abdf7cd.json`](../../sessions/f4/f4d0468397719abdf7cd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T15:13:32.223Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T15:13:32.223Z",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：部分跨模型验证——DeepSeek repo CLS 可用但弱于 Qwen，CWM 部分可解析使得差距缩小；C1 需 model-dependent caveat，C2 仅 Qwen 内验证\n核心假设：['DeepSeek repo CWM 部分可解析（unparseable 15–40%），parseable 子集精度 60–72%', 'DeepSeek repo CLS 精度 70–78%，低于 Qwen 同配置 5–12pp', 'CLS–CWM gap 方向一致但幅度缩小至 5–12pp（Qwen 为 15+pp）', 'DeepSeek TRAJ repo 未能在 ARR May 25 前完成；C2 跨模型等价缺失', 'Re-repair 停留在 phase0 负面结果（control 0.82 ≈ cls_diag 0.818）；downstream impact 无实证']\n关键指标范围：{'ds_repo_cls_acc_pct': [70, 78], 'ds_repo_cwm_unparseable_pct': [15, 40], 'ds_repo_cls_cwm_gap_pp': [5, 12], 'c2_qwen_tost_p': [0.001, 0.01], 'ds_cls_traj_variant_abs_gap_pp': [2, 5], 'qwen_8b_cls_cwm_gap_pp': [2.0, 3.0], 'ds_func_cls_cwm_gap_pp': [-0.5, 1.5], 'reviewer_critical_addressed': [3, 3]}\n叙事方向：C1 弱化为 'CLS provides a more robust verification formulation, with advantage magnitude modulated by model architecture'。 DeepSeek 作为 directionally consistent secondary evidence（同方向、较小 effect size），不再 claim universal scaling law。 C2 限定 Qwen-validated（5-seed TOST p=0.007 standalone 足够），DeepSeek func CLS≥TRAJ 仅作 suggestive evidence。 C3 不受影响。Re-repair + cross-model TRAJ 列为 limitation/future work。 新增 model-specific variation discussion section。Critical (3) downstream 和 (4) generalization 部分回应。 目标 EMNLP Findings；Main 可能性低，reviewer 大概率要求更多 cross-model seeds。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: exec-sim-repair-verifier\nfocus: 重点关注：1) DeepSeek 跨模型验证（func-level 已完成，repo-level 训练中）对 C1/C3 claim 的加强效果；2) TRAJ v2 修正后的三格式对比（CLS≥CWM≥TRAJ）是否足够支撑 C2；3) Round 1 审稿的 4 个 Critical 是否已充分回应；4) 当前 novelty 水平能否达到 EMNLP Findings 门槛\n\n## paper_framing.md\n\n# Paper Framing — exec-sim-repair-verifier\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Extended fallback: ICSE 2027 (Jun 23 abstract, Jun 30 paper)\n- Deadline: ARR May 25, 2026 (14 days from project start)\n\n## Core Claims (3 conditions)\n\n1. **Complexity-Dependent Reformulation Advantage**: Binary pass/fail classification and execution output generation (CWM-style) achieve equivalent accuracy on simple function-level code (4B: F1 diff 0.9pp), but classification scales better with model size (8B 3-seed mean accuracy gap=2.43pp; seed42: 2.81pp, cls 90.48% vs cwm 87.67%) and to repo-level complexity where CWM failure modes—token-budget exhaustion and string-value prediction errors—dominate. Zero-shot LLM-as-judge baselines (8B: 64.4%, 32B NF4: 71.7%) are far below fine-tuned 4B (88.4%), confirming fine-tuning necessity. (Validated function-level near-null + 8B scaling evidence; repo-level SWE-bench experiments in progress. Fallback: if repo-level also null, reframe to efficiency-equivalent accuracy—same F1 with 1-token vs N-token inference.)\n\n2. **Diagnostic Granularity At Equivalent Accuracy**: Per-test classification achieves equivalent variant-level accuracy to trajectory-level scoring (TOST equivalence test p=0.007, ±2pp margin; 5-seed pooled gap -0.40pp, 95% CI [-1.32, +0.52]) while providing actionable diagnostic information (which specific tests a patch fails). The per-test formulation gains diagnostic granularity without sacrificing accuracy—potentially enabling targeted re-repair and oracle-based test selection. (Evidence: 5-paired clustered bootstrap CI, 114 clusters, 10000 resamples. Paper must justify ±2pp margin: in code verification, 2pp variant-level difference is negligible given ICC=0.191/DEFF=3.97. Seeds 789/0 used 4-bit quantization — note in paper. Downstream re-repair experiment still needed for practical impact claim.)\n\n3. **Accuracy-Utility Frontier Characterization**: The effectiveness of per-test verification depends critically on test distribution characteristics. We empirically show: (a) per-test advantage concentrates in instances with multiple FAIL_TO_PASS tests (31% of SWE-bench Verified); (b) PASS_TO_PASS regression detection provides signal only when regression rate exceeds ~10%; (c) block-correlated prediction errors amplify per-test advantage through reduced effective degrees of freedom. These findings provide a practical decision framework for when per-test simulation is worth deploying.\n\n## Story Spine\n\n**Problem**: Test-time scaling for code repair requires ranking candidate patches, but verification paradigms face a granularity-cost tradeoff. Full execution costs ~$1-3 and minutes per candidate. Execution-free alternatives like SWE-RM predict trajectory-level binary correctness at low cost but provide only coarse signals that cannot distinguish between candidates failing on different test subsets.\n\n**Existing approaches & gaps**: Code World Models (Self-Execution Simulation, CWM) predict execution outputs but suffer from token-budget exhaustion and string-value prediction failures. SWE-RM achieves strong trajectory-level scoring but loses per-test diagnostic information. No work studies per-test binary classification as a dedicated verification formulation, or compares classification vs generation formulations for code execution simulation at controlled model sizes.\n\n**Our framing**: We reformulate execution simulation from an open-ended generation task (predict execution trace/output) to a closed-form classification task (predict binary pass/fail per test). On simple function-level code, both formulations achieve equivalent accuracy (~87% F1), because short execution outputs do not trigger CWM failure modes. However, on repo-level code with long execution traces and complex outputs, classification sidesteps token-budget exhaustion and string-value prediction errors, yielding a complexity-dependent advantage. We empirically ground this through (1) controlled function-level experiments establishing equivalence, (2) repo-level experiments demonstrating the complexity threshold, (3) oracle accuracy-utility frontier analysis revealing when per-test granularity helps, and (4) error complementarity analysis showing CLS/CWM have systematically opposite failure modes (CLS: miss bugs 75.5%, CWM: false alarms 83.1%), with oracle ensemble reaching 90.63%. (Downstream re-repair experiment is stretch goal; if not completed, frame as future work.)\n\n**Headline result template**: \"On function-level benchmarks, classification and generation verifiers achieve equivalent F1 (~87%), but classification scales better with model size (8B: +2.43pp accuracy) and on repo-level SWE-bench tasks outperforms by [Z] percentage points as CWM failure modes emerge. CLS and CWM exhibit complementary error patterns (oracle ensemble: 90.63%), suggesting formulation diversity as a verification strategy.\"\n\n## Venue Fit Risks\n\n1. **EMNLP vs SE venue**: Core concern is code repair verification, which may be perceived as SE rather than NLP. Mitigation: frame as (a) probing LLM code semantic reasoning capabilities through per-test prediction, and (b) a general NLP methodology insight about classification vs generation formulations applicable beyond code.\n\n2. **Negative P2P finding**: P2P regression rate ~1% means per-test is not universally better. Must present honestly as a characterization finding, not bury it. This actually strengthens the paper by showing nuanced understanding rather than overclaiming.\n\n3. **Function-level to repo-level gap**: Function-level results show classification ≈ generation. Repo-level extension is now CRITICAL (not optional) to demonstrate the complexity-dependent advantage. Requires SWE-bench Docker infrastructure. If repo-level also shows no advantage, paper pivots to efficiency framing (same accuracy, lower inference cost) + oracle characterization.\n\n## Anticipated Reviewer Concerns & Mitigations\n\n| Concern | Mitigation Experiment |\n|---------|----------------------|\n| \"Classification is trivially easier than generation -- not interesting\" | Function-level null result proves classification is NOT trivially easier; advantage is complexity-dependent, demonstrated by repo-level gap |\n| \"Per-test is just trajectory-level with extra steps when T=1\" | Oracle frontier analysis shows T distribution sensitivity; honest reporting of T=1 equivalence |\n| \"No practical downstream impact\" | Diagnostic re-repair experiment shows resolve rate improvement |\n| \"Small-scale function-level results don't generalize\" | Repo-level SWE-bench extension (if resources allow) |\n| \"CWM comparison is unfair (different output format)\" | Matched model, data, compute; discuss target asymmetry limitation |\n\n\n## experiment_plan (with registry status)\n\n- id: cwm-baseline\n  claim: 1\n  description: Train CWM generation baseline (Qwen3-4B LoRA, same data/config as MVP-B)\n    to predict execution output instead of pass/fail. Compare per-class F1 against\n    classification model (87.1/87.9%).\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - mvp-b-train\n  status: DONE\n  registry_id: cwm-baseline\n  conclusion: negative\n  metrics:\n    overall_accuracy: 87.51\n    pass_f1: 87.31\n    fail_f1: 87.71\n    pass_precision: 92.06\n    pass_recall: 83.03\n    fail_precision: 83.53\n    fail_recall: 92.32\n    exact_match_rate: 84.02\n    train_loss: 0.2534\n    eval_loss: 0.0644\n    train_runtime_sec: 3439\n    test_set_size: 1890\n    unparseable_predictions: 0\n- id: multi-seed-core\n  claim: 1\n  description: 'Multi-seed validation for core comparison: run classification (mvp-b-train)\n    and CWM baseline each with seeds {0, 1, 42}. Report mean +/- std F1. Statistical\n    significance via paired t-test or bootstrap CI. Required for any claim of ''significantly\n    better''.'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - cwm-baseline\n  registry_id: traj-level-seed0\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 85.66\n    unresolved_f1: 87.37\n    resolved_f1: 83.41\n    unresolved_precision: 82.71\n    unresolved_recall: 92.59\n    resolved_precision: 90.07\n    resolved_recall: 77.66\n    consistency_rate: 79.55\n    train_loss: 0.225\n    eval_loss_epoch1: 0.0949\n    eval_loss_epoch2: 0.0885\n    eval_loss_epoch3: 0.1011\n    train_runtime_sec: 4071.3\n- id: trace-then-judge\n  claim: 1\n  description: 'Trace-then-Judge ablation (chain-of-thought, NOT pipeline): single\n    Qwen3-4B model trained to first generate a brief execution reasoning trace (~50\n    tokens describing expected behavior), then output pass/fail. Same LoRA config/data.\n    Tests whether explicit execution reasoning helps or hurts compared to direct classification.\n    If trace-then-judge >= direct classification, the advantage is from task simplicity,\n    not from skipping reasoning.'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - cwm-baseline\n  registry_id: trace-then-judge\n  status: DONE\n  conclusion: failed\n- id: traj-level-finetuned\n  claim: 1\n  description: 'Same-size fine-tuned trajectory-level baseline: Qwen3-4B LoRA trained\n    to predict resolved/unresolved. Data construction: for each problem_id, aggregate\n    all (code, test) pairs into (code, all_tests_concatenated) -> resolved (original\n    code passes all tests) / unresolved (mutated code fails any test). Same train/val/test\n    split by problem_id. Isolates granularity effect.'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - mvp-b-data-prep\n  registry_id: traj-level-finetuned\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.66\n    unresolved_f1: 87.5\n    resolved_f1: 83.18\n    per_test_consistency: 79.94\n- id: model-size-scaling\n  claim: 1\n  description: Scale classification model from 4B to 8B. Measure accuracy improvement\n    and compare with CWM at 8B. Determine if classification advantage holds across\n    scales.\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - cwm-baseline\n  registry_id: model-size-scaling-cls8b\n  sub_experiments:\n  - registry_id: model-size-scaling-cls8b\n    gpu: seetacloud cuda:0\n    description: Qwen3-8B LoRA classification\n  - registry_id: model-size-scaling-cwm8b\n    gpu: seetacloud cuda:1\n    description: Qwen3-8B LoRA CWM generation\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 90.48\n    pass_f1: 90.86\n    fail_f1: 90.06\n    pass_precision: 90.22\n    pass_recall: 91.51\n    fail_precision: 90.76\n    fail_recall: 89.36\n    train_loss: 0.3125\n    eval_loss_epoch1: 0.0723\n    eval_loss_epoch2: 0.0741\n    eval_loss_epoch3: 0.0783\n    train_runtime_sec: 5614\n    unparseable: 0\n- id: diagnostic-rerepair\n  claim: 2\n  description: 'Downstream proof-of-concept: give repair agent per-test failure predictions\n    vs no per-test info, compare resolve rate on 200 instances. Uses SWE-agent or\n    similar repair framework.'\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - cwm-baseline\n  - traj-level-finetuned\n  status: planned\n- id: per-test-precision-recall\n  claim: 2\n  description: Measure per-test failure prediction precision/recall against ground-truth\n    failing tests on full test set. Evaluate diagnostic signal quality without downstream\n    execution.\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-b-train\n  registry_id: per-test-precision-recall\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.51\n    fail_precision: 82.75\n    fail_recall: 93.64\n    fail_f1: 87.86\n    pass_precision: 93.24\n    pass_recall: 81.8\n    pass_f1: 87.15\n    FP_count: 58\n    FN_count: 178\n    best_mutation: return_value (97.26%)\n    worst_mutation: off_by_one (82.56%)\n    bucket_6_10_acc: 96.3\n    bucket_11plus_acc: 87.12\n- id: oracle-f2p-stratified\n  claim: 3\n  description: Stratified oracle analysis by F2P test count (T=1, T=2, T=3+). Report\n    per-test advantage breakdown showing advantage concentrates in multi-test instances.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - mvp-a-oracle-sim\n  registry_id: oracle-f2p-stratified\n  status: DONE\n  conclusion: success\n  metrics:\n    T1_pct: 68.7\n    T1_block_adv: -0.09\n    T2_pct: 19.1\n    T2_block_adv: 31.69\n    T3_5_pct: 7.1\n    T3_5_block_adv: 40.74\n    T6plus_pct: 5.1\n    T6plus_block_adv: 40.06\n    overall_block_adv: 10.93\n    T2_contribution_pct: 55.3\n- id: oracle-total-validated\n  claim: 3\n  description: Oracle study with Total (F2P+P2P) distribution at empirically measured\n    regression rates. Validate when P2P tests help vs hurt.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - p2p-regression-rate\n  status: DONE\n  registry_id: mvp-a-oracle-sim\n  conclusion: success\n  metrics:\n    original_T12:\n      iid_adv_70_85: 0.1849\n      block_adv_70_85: 0.3618\n    sensitivity_T3:\n      iid_adv_70_85: 0.0761\n      block_adv_70_85: 0.3839\n    sensitivity_T7:\n      iid_adv_70_85: 0.1351\n      block_adv_70_85: 0.3833\n    sensitivity_T11:\n      iid_adv_70_85: 0.1863\n      block_adv_70_85: 0.3639\n    real_f2p_T1:\n      iid_adv_70_85: 0.0198\n      block_adv_70_85: 0.1088\n      pct_T1: 0.687\n      T_median: 1\n      T_mean: 2.3\n    swebench_f2p_stats:\n      median: 1\n      mean: 3\n      P75: 2\n      P90: 3\n    total_reg5pct:\n      iid_adv_70_85: -0.01\n      block_adv_70_85: -0.005\n      pass: false\n    total_reg10pct:\n      iid_adv_70_85: 0.132\n      block_adv_70_85: 0.083\n      pass: true\n    total_reg20pct:\n      iid_adv_70_85: 0.357\n      block_adv_70_85: 0.278\n      pass: true\n- id: block-corr-empirical\n  claim: 3\n  description: 'Empirically validate block-correlation assumption: measure actual\n    prediction error correlation structure from trained model''s test-level predictions,\n    compare with i.i.d. and block-correlated simulation models.'\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - mvp-b-train\n  registry_id: block-corr-empirical\n  status: DONE\n  conclusion: success\n  metrics:\n    icc: 0.1909\n    icc_p_value: 0\n    design_effect: 3.9676\n    overall_error_rate: 0.1249\n    all_correct_observed: 46\n    all_correct_expected_iid: 16.35\n    all_correct_ratio: 2.81\n    error_std_observed: 0.1531\n    error_std_expected_iid: 0.0811\n    error_std_ratio: 1.89\n    n_samples: 1890\n    n_problems: 114\n    inference_precision: bfloat16\n    version: v2_corrected\n- id: swebench-pertest-data\n  claim:\n  - 1\n  - 2\n  - 3\n  description: Docker re-evaluation of SWE-bench Verified patches to extract per-test\n    labels. Build SWE-bench-PerTest dataset (500 instances x 16 candidates). Resource\n    contribution.\n  priority: P1\n  gpu_budget_hours: 0\n  compute_note: CPU/Docker only, ~16-24h with 16 parallel containers. Start early\n    to parallelize with GPU experiments.\n  deps: []\n  status: planned\n- id: repo-level-training\n  claim:\n  - 1\n  - 2\n  description: Fine-tune Qwen3-4B/8B on repo-level (patched_code, test_code) -> pass/fail\n    using SWE-bench-PerTest data. Evaluate on held-out instances.\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - swebench-pertest-data\n  registry_id: repo-level-cwm-v3\n  status: DONE\n  conclusion: failed\n- id: llm-judge-baseline\n  claim:\n  - 1\n  - 3\n  description: Qwen3-8B/32B zero-shot LLM-as-judge baselines (trajectory-level and\n    per-test). Reference points for Pareto frontier.\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: llm-judge-8b-zeroshot\n  sub_experiments:\n  - registry_id: llm-judge-8b-zeroshot\n    gpu: seetacloud cuda:2\n    description: Qwen3-8B zero-shot per-test + trajectory-level\n  - registry_id: llm-judge-32b-zeroshot\n    gpu: seetacloud cuda:3\n    description: Qwen3-32B 4-bit quantized zero-shot\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 64.4\n    fail_precision: 57.9\n    fail_recall: 95.8\n    fail_f1: 72.2\n    pass_precision: 90\n    pass_recall: 35.1\n    pass_f1: 50.5\n    majority_baseline: 51.7\n    accuracy_vs_baseline_gap: 12.6\n    traj_accuracy: 99.1\n    traj_problems: 114\n    traj_true_resolved: 1\n    traj_pred_resolved: 0\n    confusion:\n      TP_fail: 874\n      FN_fail: 38\n      FP_fail: 635\n      TN_fail: 343\n- id: per-test-majority-voting\n  claim: 1\n  description: Per-test majority voting (K=3) with classification model. Test if self-consistency\n    improves per-test accuracy.\n  priority: P2\n  gpu_budget_hours: 3\n  deps:\n  - mvp-b-train\n  registry_id: per-test-majority-voting\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy_greedy: 87.51\n    accuracy_majority_vote_K3: 86.83\n    delta_accuracy: -0.69\n    fail_f1_greedy: 87.86\n    fail_f1_mv: 87.29\n    pass_f1_greedy: 87.15\n    pass_f1_mv: 86.33\n    unanimous_rate: 93.3\n    split_samples: 127\n    flipped_correct_to_wrong: 28\n    flipped_wrong_to_correct: 15\n    net_flips: -13\n    per_pass_accuracy:\n    - 86.72\n    - 86.83\n    - 87.62\n    wall_time_greedy_sec: 30\n    wall_time_mv_sec: 120\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-a-oracle-sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    original_T12:\n      iid_adv_70_85: 0.1849\n      block_adv_70_85: 0.3618\n    sensitivity_T3:\n      iid_adv_70_85: 0.0761\n      block_adv_70_85: 0.3839\n    sensitivity_T7:\n      iid_adv_70_85: 0.1351\n      block_adv_70_85: 0.3833\n    sensitivity_T11:\n      iid_adv_70_85: 0.1863\n      block_adv_70_85: 0.3639\n    real_f2p_T1:\n      iid_adv_70_85: 0.0198\n      block_adv_70_85: 0.1088\n      pct_T1: 0.687\n      T_median: 1\n      T_mean: 2.3\n    swebench_f2p_stats:\n      median: 1\n      mean: 3\n      P75: 2\n      P90: 3\n    total_reg5pct:\n      iid_adv_70_85: -0.01\n      block_adv_70_85: -0.005\n      pass: false\n    total_reg10pct:\n      iid_adv_70_85: 0.132\n      block_adv_70_85: 0.083\n      pass: true\n    total_reg20pct:\n      iid_adv_70_85: 0.357\n      block_adv_70_85: 0.278\n      pass: true\n- exp_id: mvp-b-data-prep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp-b-train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 0.875\n    pass_f1: 0.871\n    fail_f1: 0.879\n    pass_precision: 0.9324\n    pass_recall: 0.818\n    fail_precision: 0.8275\n    fail_recall: 0.9364\n    majority_baseline: 0.52\n    accuracy_vs_majority_gap: 0.355\n- exp_id: p2p-regression-rate\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: cwm-baseline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_accuracy: 87.51\n    pass_f1: 87.31\n    fail_f1: 87.71\n    pass_precision: 92.06\n    pass_recall: 83.03\n    fail_precision: 83.53\n    fail_recall: 92.32\n    exact_match_rate: 84.02\n    train_loss: 0.2534\n    eval_loss: 0.0644\n    train_runtime_sec: 3439\n    test_set_size: 1890\n    unparseable_predictions: 0\n- exp_id: multi-seed-core\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seed42:\n      accuracy: 87.83\n      pass_f1: 88.06\n      fail_f1: 87.59\n      pass_precision: 89.45\n      pass_recall: 86.71\n      fail_precision: 86.2\n      fail_recall: 89.04\n    seed123:\n      accuracy: 89.52\n      pass_f1: 89.64\n      fail_f1: 89.4\n      pass_precision: 91.76\n      pass_recall: 87.63\n      fail_precision: 87.34\n      fail_recall: 91.56\n    seed456:\n      accuracy: 87.88\n      pass_f1: 87.53\n      fail_f1: 88.21\n      pass_precision: 93.6\n      pass_recall: 82.21\n      fail_precision: 83.12\n      fail_recall: 93.97\n    mean:\n      accuracy: 88.41\n      pass_f1: 88.41\n      fail_f1: 88.4\n    std:\n      accuracy: 0.96\n      pass_f1: 1.1\n      fail_f1: 0.92\n- exp_id: trace-then-judge\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: traj-level-finetuned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.66\n    unresolved_f1: 87.5\n    resolved_f1: 83.18\n    per_test_consistency: 79.94\n- exp_id: model-size-scaling-cls8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 90.48\n    pass_f1: 90.86\n    fail_f1: 90.06\n    pass_precision: 90.22\n    pass_recall: 91.51\n    fail_precision: 90.76\n    fail_recall: 89.36\n    train_loss: 0.3125\n    eval_loss_epoch1: 0.0723\n    eval_loss_epoch2: 0.0741\n    eval_loss_epoch3: 0.0783\n    train_runtime_sec: 5614\n    unparseable: 0\n- exp_id: model-size-scaling-cwm8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.67\n    pass_f1: 87.57\n    fail_f1: 87.77\n    pass_precision: 91.53\n    pass_recall: 83.95\n    fail_precision: 84.19\n    fail_recall: 91.67\n    exact_match_rate: 84.39\n    train_loss: 0.229\n    eval_loss_epoch1: 0.0554\n    eval_loss_epoch2: 0.0512\n    eval_loss_epoch3: 0.0564\n    train_runtime_sec: 5570\n    unparseable: 0\n- exp_id: llm-judge-8b-zeroshot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 64.4\n    fail_precision: 57.9\n    fail_recall: 95.8\n    fail_f1: 72.2\n    pass_precision: 90\n    pass_recall: 35.1\n    pass_f1: 50.5\n    majority_baseline: 51.7\n    accuracy_vs_baseline_gap: 12.6\n    traj_accuracy: 99.1\n    traj_problems: 114\n    traj_true_resolved: 1\n    traj_pred_resolved: 0\n    confusion:\n      TP_fail: 874\n      FN_fail: 38\n      FP_fail: 635\n      TN_fail: 343\n- exp_id: llm-judge-32b-zeroshot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 71.69\n    majority_baseline: 51.75\n    accuracy_vs_baseline_gap: 19.95\n    fail_precision: 64.4\n    fail_recall: 92.43\n    fail_f1: 75.91\n    pass_precision: 88.12\n    pass_recall: 52.35\n    pass_f1: 65.68\n    unparseable_predictions: 0\n    trajectory_accuracy: 99.12\n    trajectory_total_problems: 114\n    trajectory_correct: 113\n    trajectory_true_resolved: 1\n    trajectory_pred_resolved: 0\n- exp_id: per-test-precision-recall\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.51\n    fail_precision: 82.75\n    fail_recall: 93.64\n    fail_f1: 87.86\n    pass_precision: 93.24\n    pass_recall: 81.8\n    pass_f1: 87.15\n    FP_count: 58\n    FN_count: 178\n    best_mutation: return_value (97.26%)\n    worst_mutation: off_by_one (82.56%)\n    bucket_6_10_acc: 96.3\n    bucket_11plus_acc: 87.12\n- exp_id: oracle-f2p-stratified\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    T1_pct: 68.7\n    T1_block_adv: -0.09\n    T2_pct: 19.1\n    T2_block_adv: 31.69\n    T3_5_pct: 7.1\n    T3_5_block_adv: 40.74\n    T6plus_pct: 5.1\n    T6plus_block_adv: 40.06\n    overall_block_adv: 10.93\n    T2_contribution_pct: 55.3\n- exp_id: traj-level-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 85.47\n    unresolved_f1: 87\n    resolved_f1: 83.52\n    unresolved_precision: 83.53\n    unresolved_recall: 90.78\n    resolved_precision: 88.17\n    resolved_recall: 79.33\n    consistency_rate: 78.59\n- exp_id: traj-level-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.4\n    unresolved_f1: 88.7\n    resolved_f1: 85.8\n    unresolved_precision: 85.7\n    unresolved_recall: 91.9\n    resolved_precision: 89.7\n    resolved_recall: 82.3\n    consistency_rate: 78.8\n- exp_id: per-test-majority-voting\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy_greedy: 87.51\n    accuracy_majority_vote_K3: 86.83\n    delta_accuracy: -0.69\n    fail_f1_greedy: 87.86\n    fail_f1_mv: 87.29\n    pass_f1_greedy: 87.15\n    pass_f1_mv: 86.33\n    unanimous_rate: 93.3\n    split_samples: 127\n    flipped_correct_to_wrong: 28\n    flipped_wrong_to_correct: 15\n    net_flips: -13\n    per_pass_accuracy:\n    - 86.72\n    - 86.83\n    - 87.62\n    wall_time_greedy_sec: 30\n    wall_time_mv_sec: 120\n- exp_id: block-corr-empirical\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    icc: 0.1909\n    icc_p_value: 0\n    design_effect: 3.9676\n    overall_error_rate: 0.1249\n    all_correct_observed: 46\n    all_correct_expected_iid: 16.35\n    all_correct_ratio: 2.81\n    error_std_observed: 0.1531\n    error_std_expected_iid: 0.0811\n    error_std_ratio: 1.89\n    n_samples: 1890\n    n_problems: 114\n    inference_precision: bfloat16\n    version: v2_corrected\n- exp_id: traj-level-seed789\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.31\n    unresolved_f1: 88.27\n    resolved_f1: 86.17\n    unresolved_precision: 87.41\n    unresolved_recall: 89.15\n    resolved_precision: 87.18\n    resolved_recall: 85.18\n    consistency_rate: 76.74\n    eval_loss: 0.1115\n    train_loss: 0.2255\n    train_runtime_sec: 2055.9\n- exp_id: traj-level-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 85.66\n    unresolved_f1: 87.37\n    resolved_f1: 83.41\n    unresolved_precision: 82.71\n    unresolved_recall: 92.59\n    resolved_precision: 90.07\n    resolved_recall: 77.66\n    consistency_rate: 79.55\n    train_loss: 0.225\n    eval_loss_epoch1: 0.0949\n    eval_loss_epoch2: 0.0885\n    eval_loss_epoch3: 0.1011\n    train_runtime_sec: 4071.3\n- exp_id: cls8b-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 89.4\n    pass_f1: 89.5\n    fail_f1: 89.2\n    pass_precision: 91.2\n    pass_recall: 87.9\n    fail_precision: 87.5\n    fail_recall: 90.9\n    train_loss: 0.3087\n    eval_loss: 0.0848\n    train_runtime_sec: 5666\n    unparseable: 0\n- exp_id: cwm8b-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 86.98\n    pass_f1: 86.83\n    fail_f1: 87.13\n    pass_precision: 91.12\n    pass_recall: 82.92\n    fail_precision: 83.3\n    fail_recall: 91.34\n    exact_match_rate: 84.13\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: cls-seed789\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89\n    pass_f1: 88.9\n    fail_f1: 89.1\n    pass_precision: 93.3\n    pass_recall: 84.9\n    fail_precision: 85.2\n    fail_recall: 93.4\n- exp_id: cls-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.94\n    pass_f1: 87.79\n    fail_f1: 88.08\n    pass_precision: 92.13\n    pass_recall: 83.84\n    fail_precision: 84.2\n    fail_recall: 92.32\n    train_loss: 0.2347\n    eval_loss: 0.0963\n    train_runtime_sec: 4976.75\n    unparseable: 0\n- exp_id: repo-level-cls\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.2\n    pass_f1: 86.95\n    fail_f1: 87.44\n    exact_match_rate: 84.44\n    majority_baseline_accuracy: 51.75\n    accuracy_vs_baseline_gap_pp: 35.45\n    test_set_size: 1890\n    unparseable_predictions: 0\n- exp_id: cwm-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 86.98\n    pass_f1: 86.66\n    fail_f1: 87.29\n    pass_precision: 92.26\n    pass_recall: 81.7\n    fail_precision: 82.52\n    fail_recall: 92.65\n    exact_match_rate: 84.02\n    train_loss: 0.2525\n    eval_loss_best: 0.0551\n    eval_loss_final: 0.0635\n    train_runtime_sec: 3440\n    unparseable: 0\n- exp_id: cwm-seed789\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 86.67\n    pass_f1: 86.74\n    fail_f1: 86.6\n    exact_match_rate: 83.97\n    baseline_gap_pp: 34.92\n    test_set_size: 1890\n    unparseable_predictions: 0\n    per_class:\n      fail:\n        precision: 84.09\n        recall: 89.25\n        f1: 86.6\n      pass:\n        precision: 89.37\n        recall: 84.25\n        f1: 86.74\n- exp_id: cwm-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.57\n    fail_f1: 87.93\n    fail_precision: 82.71\n    fail_recall: 93.86\n    pass_f1: 87.18\n    pass_precision: 93.45\n    pass_recall: 81.7\n    exact_match_rate: 84.29\n    eval_loss: 0.0665\n    train_loss: 0.2554\n    train_runtime_sec: 3586\n- exp_id: 5-paired-clustered-bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pooled_gap_pp: -0.45\n    pooled_ci_lower: -1.71\n    pooled_ci_upper: 0.84\n    pooled_p_value: 0.499\n    tost_p_value: 0.0071\n    tost_margin_pp: 2\n    seed_level_paired_t_p: 0.425\n    seed_level_mean_gap: -0.48\n    n_variants_pooled: 523\n    n_clusters: 114\n    per_seed_gaps:\n      seed42: -0.97\n      seed123: 1.45\n      seed456: -1.84\n      seed789: -0.78\n      seed0: -0.29\n- exp_id: cwm8b-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 86.24\n    pass_f1: 85.96\n    fail_f1: 86.51\n    pass_precision: 91.08\n    pass_recall: 81.39\n    fail_precision: 82.09\n    fail_recall: 91.45\n    exact_match_rate: 82.8\n    train_loss: 0.2279\n    eval_loss: 0.0583\n    unparseable: 0\n    test_set_size: 1890\n    majority_baseline_accuracy: 51.75\n    accuracy_vs_baseline_gap_pp: 34.5\n- exp_id: cls8b-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 88.31\n    pass_f1: 88.2\n    fail_f1: 88.41\n    pass_precision: 92.29\n    pass_recall: 84.46\n    fail_precision: 84.72\n    fail_recall: 92.43\n    train_loss: 0.3105\n    eval_loss: 0.0928\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: repo-level-cls-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-home\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6611\n    f1_macro: 0.5661\n    f1_pass: 0.769\n    f1_fail: 0.363\n    precision_pass: 0.765\n    recall_pass: 0.774\n    precision_fail: 0.369\n    recall_fail: 0.357\n    majority_baseline: 0.7296\n    n_unparseable: 132\n    best_checkpoint: checkpoint-200\n    early_stop: D045\n- exp_id: cls8b-eval-seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 90.48\n    pass_f1: 90.86\n    fail_f1: 90.06\n    pass_precision: 90.22\n    pass_recall: 91.51\n    fail_precision: 90.76\n    fail_recall: 89.36\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: cls8b-eval-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 89.37\n    pass_f1: 89.54\n    fail_f1: 89.19\n    pass_precision: 91.2\n    pass_recall: 87.93\n    fail_precision: 87.54\n    fail_recall: 90.9\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: matched-seed-8b-predictions\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: repo-level-cwm-v4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cwm-v5\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v6\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v7\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v8\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v9\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-seed123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cwm-seed123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cwm-v10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6991\n    f1_macro: 0.4671\n    f1_pass: 0.8187\n    f1_fail: 0.1154\n    precision_pass: 0.7304\n    recall_pass: 0.9314\n    precision_fail: 0.2815\n    recall_fail: 0.0726\n    majority_baseline: 0.7296\n    n_unparseable: 9102\n    n_unparseable_pct: 0.93\n    n_truncated: 478\n    n_truncated_pct: 0.0489\n    truncated_accuracy: 0.2176\n    best_checkpoint: checkpoint-400\n    early_stop: D045\n    eval_invalid: max_new_tokens=64 caused 93% unparseable (D047)\n- exp_id: repo-level-cls-v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_sweep:\n      ckpt_600:\n        accuracy: 76.74\n        f1_macro: 73.74\n        fail_f1: 64.88\n        pass_f1: 82.61\n      ckpt_4000:\n        accuracy: 81.51\n        f1_macro: 72.56\n        fail_f1: 56.9\n        pass_f1: 88.23\n      ckpt_4200:\n        accuracy: 80.64\n        f1_macro: 72.1\n        fail_f1: 56.66\n        pass_f1: 87.54\n      ckpt_4400:\n        accuracy: 82.11\n        f1_macro: 73.94\n        fail_f1: 59.34\n        fail_precision: 77.02\n        fail_recall: 48.26\n      ckpt_4600:\n        accuracy: 82.35\n        f1_macro: 74.74\n        fail_f1: 60.87\n        pass_f1: 88.6\n        fail_precision: 76\n        fail_recall: 50.76\n    best_checkpoint_accuracy: checkpoint-4600\n    best_checkpoint_f1: checkpoint-4600\n    eval_samples: 9784\n    accuracy: 82.35\n    f1_macro: 74.74\n    unparseable: 132\n    unparseable_pct: 1.3\n    majority_baseline: 72.96\n    gap_vs_baseline: 9.39\n    eval_server: home-1x5090\n    eval_env: transformers 4.57.6\n    note: Test set sweep complete. ckpt-4600 best on both accuracy (82.35%) and f1_macro\n      (74.74%).\n    val_2048:\n      ckpt_600:\n        accuracy: 77.25\n        f1_macro: 70.81\n        fail_f1: 57.11\n        pass_f1: 84.52\n      ckpt_4000:\n        accuracy: 83.32\n        f1_macro: 70.26\n        fail_f1: 50.56\n        pass_f1: 89.97\n      ckpt_4200:\n        accuracy: 82.82\n        f1_macro: 69.54\n        fail_f1: 49.43\n        pass_f1: 89.65\n      ckpt_4400:\n        accuracy: 83.49\n        f1_macro: 71.63\n        fail_f1: 53.29\n        pass_f1: 89.97\n      ckpt_4600:\n        accuracy: 83.63\n        f1_macro: 71.72\n        fail_f1: 53.36\n        pass_f1: 90.07\n      eval_samples: 9335\n      unparseable: 1883\n      unparseable_pct: 20.2\n      val_best_f1: ckpt-4600\n      val_best_acc: ckpt-4600\n      note: 'val-test 一致: 都是 ckpt-4600'\n- exp_id: repo-level-cwm-v11\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_checkpoint: checkpoint-600\n    eval_samples: 500\n    eval_type: subset500_tok1024\n    accuracy: 66.6\n    fail_f1: 27.7\n    pass_f1: 78.3\n    f1_macro: 52.99\n    fail_precision: 33.3\n    fail_recall: 23.7\n    pass_precision: 74.5\n    pass_recall: 82.5\n    unparseable: 376\n    unparseable_pct: 75.2\n    majority_baseline: 73\n    gap_vs_baseline: -6.4\n    gen_length_mean: 3398.1\n    gen_length_median: 3307.5\n    gen_length_max: 7582\n    confusion:\n      TP: 301\n      TN: 32\n      FP: 103\n      FN: 64\n- exp_id: repo-level-cls-8b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_checkpoint: checkpoint-200\n    eval_samples: 9784\n    accuracy: 71.37\n    fail_f1: 60.57\n    pass_f1: 77.53\n    f1_macro: 69.05\n    fail_precision: 48.26\n    fail_recall: 81.29\n    pass_precision: 90.71\n    pass_recall: 67.69\n    unparseable: 136\n    unparseable_pct: 1.39\n    majority_baseline: 73\n    gap_vs_baseline: -1.63\n    confusion:\n      TP: 4832\n      TN: 2151\n      FP: 495\n      FN: 2306\n    eval_server: westd-48478\n    eval_env: transformers 5.8.0\n- exp_id: repo-level-cls-seed123-home\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    val_2048:\n      n: 9335\n      unparseable: 1883\n      ckpt_200:\n        accuracy: 62.51\n        f1_macro: 55.54\n        f1_pass: 73.14\n        f1_fail: 37.94\n      ckpt_400:\n        accuracy: 80.72\n        f1_macro: 67.03\n        f1_pass: 88.27\n        f1_fail: 45.78\n      ckpt_600:\n        accuracy: 76.78\n        f1_macro: 66.81\n        f1_pass: 85\n        f1_fail: 48.63\n      ckpt_800:\n        accuracy: 81.81\n        f1_macro: 69.14\n        f1_pass: 88.91\n        f1_fail: 49.37\n      ckpt_1000:\n        accuracy: 82.3\n        f1_macro: 67.63\n        f1_pass: 89.42\n        f1_fail: 45.84\n      best_f1: ckpt_800\n      best_acc: ckpt_1000\n    val_4096:\n      n: 9335\n      unparseable: 1406\n      ckpt_400:\n        accuracy: 82.57\n        f1_macro: 71.24\n        f1_pass: 89.29\n        f1_fail: 53.18\n      ckpt_600:\n        accuracy: 79.18\n        f1_macro: 70.73\n        f1_pass: 86.45\n        f1_fail: 55\n      ckpt_800:\n        accuracy: 83.7\n        f1_macro: 73.31\n        f1_pass: 90\n        f1_fail: 56.7\n      best_f1: ckpt_800\n      best_acc: ckpt_800\n    val_5120:\n      n: 9335\n      unparseable: 0\n      truncated: 234\n      ckpt_400:\n        accuracy: 86.01\n        f1_macro: 79.66\n        f1_pass: 91.02\n        f1_fail: 68.3\n      ckpt_600:\n        accuracy: 81.89\n        f1_macro: 77.01\n        f1_pass: 87.6\n        f1_fail: 66.43\n      ckpt_800:\n        accuracy: 87.92\n        f1_macro: 81.95\n        f1_pass: 92.33\n        f1_fail: 71.57\n      best_f1: ckpt_800\n      best_acc: ckpt_800\n- exp_id: repo-level-cwm-v12\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_test_accuracy: 58.04\n    eval_test_f1_macro: 51.67\n    eval_test_f1_fail: 34.12\n    eval_test_f1_pass: 69.22\n    eval_test_unparseable: 5255\n    eval_test_total: 9784\n    eval_test_unparseable_rate: 53.7\n    eval_checkpoint: checkpoint-500\n- exp_id: repo-level-cwm-seed123-conda\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_test_accuracy: 59.09\n    eval_test_f1_macro: 43.43\n    eval_test_f1_fail: 13.67\n    eval_test_f1_pass: 73.19\n    eval_test_unparseable: 6574\n    eval_test_total: 9784\n    eval_test_unparseable_rate: 67.2\n    eval_checkpoint: checkpoint-500\n- exp_id: repo-level-cls-8b-conda\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    val_8192:\n      ckpt_200:\n        accuracy: 63.52\n        f1_macro: 61.17\n        f1_fail: 51.6\n        f1_pass: 70.7\n        unparseable: 9\n      ckpt_400:\n        accuracy: 80.96\n      ckpt_600:\n        accuracy: 85\n      best_acc: ckpt_600\n    val_5120:\n      ckpt_400:\n        accuracy: 80.47\n        f1_macro: 75.84\n    test_2048:\n      ckpt_400:\n        accuracy: 84.52\n        f1_macro: 80.89\n      ckpt_600:\n        accuracy: 78.51\n    test_8192:\n      ckpt_400:\n        accuracy: 84.79\n        f1_macro: 81.18\n        f1_fail: 72.93\n        f1_pass: 89.43\n        unparseable: 0\n        total: 9784\n      ckpt_600:\n        accuracy: 79.05\n        f1_macro: 75.12\n        f1_fail: 65.24\n        f1_pass: 85\n        unparseable: 0\n        total: 9784\n- exp_id: repo-level-cls-v5-conda\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_sweep:\n      ckpt_200:\n        accuracy: 52.96\n        f1_macro: 52.89\n        fail_f1: 51.02\n        pass_f1: 54.76\n      ckpt_400:\n        accuracy: 78.43\n        f1_macro: 68.41\n        fail_f1: 50.61\n        pass_f1: 86.21\n        fail_precision: 66.48\n        fail_recall: 40.85\n        pass_precision: 80.82\n        pass_recall: 92.36\n      ckpt_600:\n        accuracy: 76.37\n        f1_macro: 71.17\n        fail_f1: 58.93\n        pass_f1: 83.41\n        fail_precision: 55.6\n        fail_recall: 62.7\n        pass_precision: 85.49\n        pass_recall: 81.44\n    best_checkpoint_accuracy: checkpoint-400\n    best_checkpoint_f1: checkpoint-600\n    eval_samples: 9784\n    accuracy: 78.43\n    f1_macro: 71.17\n    unparseable: 132\n    unparseable_pct: 1.35\n    majority_baseline: 72.96\n    eval_server: westd-48478\n    eval_env: conda, transformers 4.57.6\n- exp_id: repo-level-cwm-8b-conda\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-8b-seed123-conda\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-8b-seed123-conda-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-8b-seed123-conda-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-ckpt3000-test-eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-ckpt3000-test-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt3000-val-eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cls-8b-s42-ckpt200-val\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt3000-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 88.69\n    f1_macro: 81.73\n    f1_fail: 70.5\n    f1_pass: 93\n    precision_fail: 95.2\n    precision_pass: 87.6\n    recall_fail: 55.9\n    recall_pass: 99.1\n    majority_baseline: 75.9\n    gap_vs_majority_pp: 12.8\n    unparseable: 9\n    total: 9335\n- exp_id: cls8b-s42-ckpt400-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.79\n    f1_macro: 81.18\n    f1_fail: 72.93\n    f1_pass: 89.43\n    precision_fail: 70.32\n    precision_pass: 90.74\n    recall_fail: 75.74\n    recall_pass: 88.15\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 11.84\n    unparseable: 0\n    total: 9784\n- exp_id: cls4b-seed123-ckpt800-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.92\n    f1_macro: 81.95\n    f1_pass: 92.33\n    f1_fail: 71.57\n    unparseable: 0\n    truncated: 234\n    total: 9335\n- exp_id: cls8b-s42-ckpt600-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 79.05\n    f1_macro: 75.12\n    f1_fail: 65.24\n    f1_pass: 85\n    precision_fail: 59.16\n    precision_pass: 88.95\n    recall_fail: 72.71\n    recall_pass: 81.4\n    unparseable: 0\n    total: 9784\n    majority_baseline: 73\n    gap_vs_majority_pp: 6.09\n- exp_id: repo-level-cls-8b-s42-resume\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_steps: 6633\n    epochs: 3\n    train_time_sec: 74425\n    final_train_loss: 0.4284\n    final_eval_loss: 0.4768\n    best_eval_loss_resume: 0.2516\n    best_eval_loss_resume_step: 4200\n    best_eval_loss_overall: 0.0796\n    best_eval_loss_overall_step: 200\n    checkpoints_saved: 32\n    overfitting: true\n    note: Severe overfitting after epoch 2. Resume-best=ckpt-4200. Val sweep running\n      on cuda:0.\n- exp_id: cls8b-s42-ckpt200-val8192-eval-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 63.52\n    f1_macro: 61.17\n    f1_fail: 51.6\n    f1_pass: 70.7\n    unparseable: 9\n    total: 9335\n- exp_id: cls4b-v5-val5120-sweep-home\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-v5-ckpt600-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 82.82\n    f1_macro: 79.81\n    f1_fail: 72.03\n    f1_pass: 87.6\n    precision_fail: 59.3\n    recall_fail: 91.7\n    unparseable: 0\n    total: 9335\n- exp_id: cls8b-s42-ckpt800-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.5\n    f1_macro: 79.2\n- exp_id: cls4b-v5-ckpt4000-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89.84\n    f1_macro: 84.25\n    f1_fail: 74.85\n    f1_pass: 93.64\n    precision_fail: 92.95\n    recall_fail: 62.66\n    precision_pass: 89.24\n    recall_pass: 98.49\n    unparseable: 0\n    truncated: 234\n    total: 9335\n- exp_id: cls8b-s42-ckpt1000-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 88.23\n    f1_macro: 82.72\n    f1_fail: 73\n    f1_pass: 92.5\n    precision_fail: 81.8\n    recall_fail: 65.8\n    precision_pass: 89.8\n    recall_pass: 95.3\n    unparseable: 9\n    total_instances: 9335\n- exp_id: cls4b-v5-ckpt4400-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    accuracy_partial_70pct: 89.69\n    f1_macro_partial_70pct: 84.61\n    samples_completed: 6544\n    samples_total: 9335\n- exp_id: cls8b-s42-ckpt1000-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.52\n    f1_macro: 77.5\n    f1_fail: 65.85\n    f1_pass: 89.14\n    precision_fail: 74.93\n    recall_fail: 58.73\n    precision_pass: 85.84\n    recall_pass: 92.72\n    majority_baseline: 72.96\n    gap_vs_majority: 10.56\n    unparseable_count: 0\n    unparseable_rate: 0\n    total_samples: 9784\n    tp: 6618\n    fp: 1092\n    fn: 520\n    tn: 1554\n- exp_id: cls4b-v5-ckpt4400-val5120-eval-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1200-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1400-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.97\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 10.09\n    f1_macro: 77.15\n    f1_fail: 62.95\n    f1_pass: 91.34\n    precision_fail: 86.68\n    precision_pass: 85.85\n    recall_fail: 49.42\n    recall_pass: 97.59\n    n_instances: 9335\n    n_unparseable: 9\n    confusion_matrix:\n      tn: 1113\n      fp: 1139\n      fn: 171\n      tp: 6912\n- exp_id: cls8b-s42-ckpt1600-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-v5-val-sweep-ckpt4600\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 90.07\n    f1_macro: 85.04\n    f1_fail: 76.37\n    f1_pass: 93.71\n    precision_fail: 89.65\n    recall_fail: 66.52\n    precision_pass: 90.16\n    recall_pass: 97.56\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 14.19\n    unparseable_count: 0\n    total_samples: 9335\n    n_truncated: 234\n- exp_id: cls4b-v5-val-sweep-ckpt4200\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89.06\n    f1_macro: 83.07\n    f1_fail: 73\n    f1_pass: 93.1\n    precision_fail: 90.3\n    recall_fail: 61.3\n    precision_pass: 88.8\n    recall_pass: 97.9\n- exp_id: cls4b-v5-val-sweep-ckpt4400\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1200-val8192\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-v5-val-sweep-ckpt4400-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89.96\n    f1_macro: 84.94\n    f1_fail: 76.25\n    f1_pass: 93.64\n    precision_fail: 88.84\n    precision_pass: 90.21\n    recall_fail: 66.79\n    recall_pass: 97.33\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 14.09\n    n_instances: 9335\n    n_truncated: 234\n    n_unparseable: 0\n- exp_id: cls8b-s42-ckpt1200-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.84\n    f1_macro: 77.47\n    f1_fail: 65.49\n    f1_pass: 89.45\n    precision_fail: 77.52\n    recall_fail: 56.69\n    precision_pass: 85.4\n    recall_pass: 93.91\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.89\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-s42-ckpt1400-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.47\n    f1_macro: 78.9\n    f1_fail: 67.13\n    f1_pass: 90.67\n    precision_fail: 86.43\n    recall_fail: 54.88\n    precision_pass: 85.27\n    recall_pass: 96.81\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 12.51\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-s42-ckpt1600-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.99\n    f1_macro: 78.94\n    f1_fail: 67.65\n    f1_pass: 90.22\n    precision_fail: 81.06\n    recall_fail: 58.05\n    precision_pass: 85.93\n    recall_pass: 94.97\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 12.03\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-s42-ckpt1200-val8192-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1200-val8192-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.76\n    f1_macro: 81.25\n    f1_fail: 70.2\n    f1_pass: 92.3\n    precision_fail: 85\n    recall_fail: 59.8\n    precision_pass: 88.3\n    recall_pass: 96.7\n    majority_baseline: 75.9\n    gap_vs_majority: 11.9\n    unparseable: 9\n- exp_id: cls8b-s42-ckpt1600-val8192-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 86.75\n    f1_macro: 78.94\n    f1_fail: 66.12\n    f1_pass: 91.76\n    precision_fail: 86.28\n    precision_pass: 86.83\n    recall_fail: 53.6\n    recall_pass: 97.29\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 10.87\n    unparseable: 9\n    total: 9335\n- exp_id: cls8b-s42-ckpt800-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.53\n    f1_macro: 78.97\n    f1_fail: 69.17\n    f1_pass: 88.77\n    precision_fail: 70.07\n    recall_fail: 68.29\n    precision_pass: 88.36\n    recall_pass: 89.18\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.58\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6600-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.23\n    f1_macro: 79.02\n    f1_fail: 65.9\n    f1_pass: 92.14\n    precision_fail: 92.6\n    recall_fail: 51.15\n    precision_pass: 86.4\n    recall_pass: 98.7\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.36\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls4b-v5-ckpt4600-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.63\n    f1_macro: 75.63\n    f1_fail: 61.67\n    f1_pass: 89.59\n    precision_fail: 84.03\n    recall_fail: 48.72\n    precision_pass: 83.55\n    recall_pass: 96.57\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.67\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6400-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.48\n    f1_macro: 79.66\n    f1_fail: 67.04\n    f1_pass: 92.27\n    precision_fail: 91.81\n    recall_fail: 52.8\n    precision_pass: 86.78\n    recall_pass: 98.5\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.6\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls8b-seed123-ckpt6200-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.52\n    f1_macro: 79.26\n    f1_fail: 66.16\n    f1_pass: 92.35\n    precision_fail: 95.63\n    recall_fail: 50.58\n    precision_pass: 86.33\n    recall_pass: 99.27\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.64\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls4b-v5-ckpt4400-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.24\n    f1_macro: 74.44\n    f1_fail: 59.45\n    f1_pass: 89.44\n    precision_fail: 85.98\n    recall_fail: 45.43\n    precision_pass: 82.78\n    recall_pass: 97.25\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.28\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt3000-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.6\n    f1_macro: 78.38\n    f1_fail: 65.89\n    f1_pass: 90.87\n    precision_fail: 91.65\n    recall_fail: 51.44\n    precision_pass: 84.52\n    recall_pass: 98.26\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 12.64\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6633-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.1\n    f1_macro: 78.79\n    f1_fail: 65.52\n    f1_pass: 92.07\n    precision_fail: 92.26\n    recall_fail: 50.8\n    precision_pass: 86.31\n    recall_pass: 98.64\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.23\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls8b-seed123-ckpt3000-test8192-eval-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-seed123-ckpt800-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-seed123-ckpt800-test5120-eval-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 75.33\n    f1_macro: 67.03\n    f1_fail: 50.5\n    f1_pass: 83.6\n    precision_fail: 55.2\n    recall_fail: 46.5\n    precision_pass: 81.3\n    recall_pass: 86\n    majority_baseline: 73\n    gap_vs_majority_pp: 2.4\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6200-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt6400-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt200-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt6200-test-eval-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.7\n    f1_fail: 63.71\n    f1_pass: 90.31\n    f1_macro: 77.01\n    precision_fail: 88.84\n    precision_pass: 83.96\n    recall_fail: 49.66\n    recall_pass: 97.69\n    n_instances: 9784\n    n_cls_unparseable: 0\n- exp_id: cls8b-seed123-ckpt6400-test-eval-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.08\n    f1_fail: 65.32\n    f1_pass: 90.49\n    f1_macro: 77.91\n    precision_fail: 87.92\n    precision_pass: 84.54\n    recall_fail: 51.97\n    recall_pass: 97.35\n    n_instances: 9784\n    n_cls_unparseable: 0\n- exp_id: cls4b-v5-ckpt600-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 77.74\n    f1_macro: 74.74\n    f1_fail: 66.03\n    f1_pass: 83.44\n    precision_fail: 56.21\n    recall_fail: 80.01\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 4.78\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6600-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.9\n    f1_macro: 77.58\n    pass_f1: 90.4\n    fail_f1: 64.8\n    pass_precision: 84.3\n    pass_recall: 97.4\n    fail_precision: 87.8\n    fail_recall: 51.3\n    n_samples: 9784\n    n_pass: 7138\n    n_fail: 2646\n    majority_baseline: 73\n    unparseable: 0\n    confusion_matrix:\n      fail_as_fail: 1357\n      fail_as_pass: 1289\n      pass_as_fail: 188\n      pass_as_pass: 6950\n- exp_id: cls8b-s42-ckpt200-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 70.07\n    f1_macro: 68.18\n    pass_f1: 75.9\n    fail_f1: 60.4\n    pass_precision: 91.8\n    pass_recall: 64.7\n    fail_precision: 47\n    fail_recall: 84.5\n    n_samples: 9784\n    n_pass: 7138\n    n_fail: 2646\n    majority_baseline: 73\n    unparseable: 0\n    confusion_matrix:\n      fail_as_fail: 2235\n      fail_as_pass: 411\n      pass_as_fail: 2517\n      pass_as_pass: 4621\n- exp_id: cls8b-s42-ckpt1000-test-seq2048-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 82.83\n    f1_macro: 76.88\n    fail_precision: 72.2\n    fail_recall: 59.3\n    fail_f1: 65.2\n    pass_precision: 85.9\n    pass_recall: 91.5\n    pass_f1: 88.6\n    unparseable: 136\n- exp_id: cls4b-v5-ckpt4000-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt6633-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.89\n    f1_macro: 77.56\n    f1_fail: 64.7\n    f1_pass: 90.4\n    precision_fail: 87.8\n    recall_fail: 51.2\n    precision_pass: 84.3\n    recall_pass: 97.4\n    majority_baseline: 73\n    gap_vs_majority_pp: 11.9\n    total_samples: 9784\n    unparseable_count: 0\n- exp_id: cls8b-seed123-ckpt200-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 72.55\n    f1_macro: 70.18\n    pass_f1: 78.58\n    fail_f1: 61.78\n    pass_precision: 91.21\n    pass_recall: 69.02\n    fail_precision: 49.54\n    fail_recall: 82.05\n    n_samples: 9784\n    n_pass: 7138\n    n_fail: 2646\n    majority_baseline: 72.96\n    unparseable: 0\n    confusion_matrix:\n      tn: 2171\n      fp: 475\n      fn: 2211\n      tp: 4927\n- exp_id: cwm8b-ckpt400-test-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm-rank32-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm-4b-rank32-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm-rank32-ablation-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87\n    exact_match_rate: 83.4\n    fail_f1: 87.1\n    pass_f1: 86.9\n    train_loss_final: 0.0152\n    train_loss_avg: 0.2536\n    eval_loss: 0.0688\n    train_runtime_sec: 5003\n    test_set_size: 1890\n    vs_rank16_baseline: -0.51\n    rank16_baseline_accuracy: 87.51\n- exp_id: cwm-rank64-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm-4b-rank64-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: s42-extended-val-sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm-rank32-alpha64-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.04\n    pass_f1: 86.79\n    fail_f1: 87.27\n    f1_macro: 87.03\n    pass_precision: 91.8\n    pass_recall: 82.3\n    fail_precision: 82.9\n    fail_recall: 92.1\n    exact_match_rate: 84.55\n    train_loss: 0.2069\n    eval_loss: 0.0606\n    n_instances: 1890\n    vs_rank16_baseline: -0.47\n    rank16_baseline_accuracy: 87.51\n- exp_id: cls8b-s42-extended-val-sweep\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: s42-extended-val-sweep-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-seq8192\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-seq4096\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-seq8192-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-gpu1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt1000-test-mutation\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1000-test-mutation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt3600-test\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt3600-mutation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 84.4849\n    overall_correct: 8266\n    overall_total: 9784\n    gold_accuracy: 96.2443\n    gold_correct: 4459\n    gold_total: 4633\n    mutation_operator_swap_accuracy: 81.3822\n    mutation_operator_swap_correct: 2732\n    mutation_operator_swap_total: 3357\n    mutation_off_by_one_accuracy: 86.8852\n    mutation_off_by_one_correct: 159\n    mutation_off_by_one_total: 183\n    mutation_return_value_accuracy: 75.4448\n    mutation_return_value_correct: 424\n    mutation_return_value_total: 562\n    mutation_boundary_removal_accuracy: 46.9018\n    mutation_boundary_removal_correct: 492\n    mutation_boundary_removal_total: 1049\n- exp_id: cls8b-s42-ckpt3600-seq2048-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.04\n    f1_macro: 76.8\n    unparseable: 136\n    n_samples: 9784\n    seq_length: 2048\n- exp_id: repo-level-cwm-8b-conda-v6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm8b-ckpt400-test-eval-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm8b-ckpt400-test-eval-v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt3600-test-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.48\n    f1_macro: 78.17\n    fail_recall: 56.8\n    pass_recall: 94.8\n    n_samples: 9784\n    note: reproduces v1 exactly\n- exp_id: cls8b-seed123-ckpt3000-mutation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.6\n    boundary_removal: 44.9\n    operator_swap: 82.6\n    return_value: 66.4\n    off_by_one: 79.2\n    gold: 99.6\n    n_samples: 9784\n- exp_id: cwm8b-ckpt400-test-eval-shard2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: cls4b-ckpt4600-test-mutation-pr\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.63\n    gold_acc: 98.25\n    operator_swap_acc: 78.91\n    return_value_acc: 67.97\n    off_by_one_acc: 58.47\n    boundary_removal_acc: 46.9\n    n_instances: 9784\n    note: off_by_one recall_fail=0 (all predicted pass); boundary_removal identical\n      to 8B\n- exp_id: cwm4b-s42-mutation-breakdown\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 58.04\n    parseable_rate: 46.3\n    parseable_only_accuracy: 42.9\n    gold_parse_rate: 43.5\n    gold_parseable_acc: 23.5\n    operator_swap_parse_rate: 56.9\n    operator_swap_parseable_acc: 63.1\n    off_by_one_parse_rate: 4.4\n    off_by_one_parseable_acc: 0\n    return_value_parse_rate: 48.8\n    return_value_parseable_acc: 27\n    boundary_removal_parse_rate: 30.6\n    boundary_removal_parseable_acc: 59.2\n    n_instances: 9784\n- exp_id: cwm8b-ckpt400-test-eval-shard3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm8b-ckpt400-test-eval-shard4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: deepseek-cls-repo\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: deepseek-cwm-func\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.04292\n    train_time_seconds: 5215\n    test_accuracy: 85.77\n    test_f1_macro: 85.73\n    test_precision_fail: 80.07\n    test_precision_pass: 93.18\n    test_recall_fail: 93.86\n    test_recall_pass: 78.22\n    test_unparseable_rate: 0\n    test_n: 1890\n- exp_id: deepseek-cls-func\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.0701\n    train_time_seconds: 5444\n    test_accuracy: 86.93\n    test_f1_macro: 86.92\n    test_precision_fail: 86.42\n    test_precision_pass: 87.41\n    test_recall_fail: 86.51\n    test_recall_pass: 87.32\n    test_n: 1890\n- exp_id: deepseek-cwm-func-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.0408\n    train_time_seconds: 5244\n    test_accuracy: 87.88\n    test_f1_macro: 87.88\n    test_precision_fail: 83.78\n    test_precision_pass: 92.61\n    test_recall_fail: 92.87\n    test_recall_pass: 83.23\n    test_unparseable_rate: 0\n    test_n: 1890\n- exp_id: deepseek-cwm-repo\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: re-repair-phase0\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    control_mean_sim: 0.82\n    cls_diag_mean_sim: 0.818\n    oracle_diag_mean_sim: 0.809\n    random_diag_mean_sim: 0.719\n    n_instances: 10\n    n_conditions: 4\n    samples_per_condition: 3\n- exp_id: deepseek-cls-func-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.06753\n    train_time_seconds: 5391\n    test_accuracy: 86.77\n    test_f1_macro: 86.77\n    test_precision_fail: 84.99\n    test_precision_pass: 88.56\n    test_recall_fail: 88.16\n    test_recall_pass: 85.48\n    test_unparseable_rate: 0\n    test_n: 1890\n- exp_id: deepseek-traj-func\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss_epoch1: 0.0943\n    eval_loss_epoch2: 0.0793\n    eval_loss_epoch3: 0.0884\n    best_eval_loss: 0.0793\n    best_step: 1008\n    best_epoch: 2\n    train_loss: 0.1131\n    train_runtime_sec: 2910.6\n- exp_id: deepseek-traj-func-s123\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: deepseek-traj-func-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.0796\n    best_step: 504\n    test_accuracy: 0.8324\n    majority_baseline: 0.5359\n    train_loss: 0.0857\n    train_runtime_seconds: 3069.6\n- exp_id: deepseek-traj-func-v2-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.077\n    best_step: 504\n    test_accuracy: 0.8508\n    majority_baseline: 0.5359\n    train_loss: 0.0842\n    train_runtime_seconds: 3021\n    per_test_consistency: 0.782\n- exp_id: deepseek-traj-func-v2-fixed\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: deepseek-traj-func-v2-s123-fixed\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: deepseek-traj-repo\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: deepseek-traj-repo-s123\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T15:13:32.228Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T15:13:32.228Z",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-16T15:13:32.251Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：部分跨模型验证——DeepSeek repo CLS 可用但弱于 Qwen，CWM 部分可解析使得差距缩小；C1 需 model-dependent caveat，C2 仅 Qwen 内验证
核心假设：['DeepSeek repo CWM 部分可解析（unparseable 15–40%），parseable 子集精度 60–72%', 'DeepSeek repo CLS 精度 70–78%，低于 Qwen 同配置 5–12pp', 'CLS–CWM gap 方向一致但幅度缩小至 5–12pp（Qwen 为 15+pp）', 'DeepSeek TRAJ repo 未能在 ARR May 25 前完成；C2 跨模型等价缺失', 'Re-repair 停留在 phase0 负面结果（control 0.82 ≈ cls_diag 0.818）；downstream impact 无实证']
关键指标范围：{'ds_repo_cls_acc_pct': [70, 78], 'ds_repo_cwm_unparseable_pct': [15, 40], 'ds_repo_cls_cwm_gap_pp': [5, 12], 'c2_qwen_tost_p': [0.001, 0.01], 'ds_cls_traj_variant_abs_gap_pp': [2, 5], 'qwen_8b_cls_cwm_gap_pp': [2.0, 3.0], 'ds_func_cls_cwm_gap_pp': [-0.5, 1.5], 'reviewer_critical_addressed': [3, 3]}
叙事方向：C1 弱化为 'CLS provides a more robust verification formulation, with advantage magnitude modulated by model architecture'。 DeepSeek 作为 directionally consistent secondary evidence（同方向、较小 effect size），不再 claim universal scaling law。 C2 限定 Qwen-validated（5-seed TOST p=0.007 standalone 足够），DeepSeek func CLS≥TRAJ 仅作 suggestive evidence。 C3 不受影响。Re-repair + cross-model TRAJ 列为 limitation/future work。 新增 model-specific variation discussion section。Critical (3) downstream 和 (4) generalization 部分回应。 目标 EMNLP Findings；Main 可能性低，reviewer 大概率要求更多 cross-model seeds。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: exec-sim-repair-verifier
focus: 重点关注：1) DeepSeek 跨模型验证（func-level 已完成，repo-level 训练中）对 C1/C3 claim 的加强效果；2) TRAJ v2 修正后的三格式对比（CLS≥CWM≥TRAJ）是否足够支撑 C2；3) Round 1 审稿的 4 个 Critical 是否已充分回应；4) 当前 novelty 水平能否达到 EMNLP Findings 门槛

## paper_framing.md

# Paper Framing — exec-sim-repair-verifier

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25, 2026)
- Fallback: EMNLP 2026 Findings
- Extended fallback: ICSE 2027 (Jun 23 abstract, Jun 30 paper)
- Deadline: ARR May 25, 2026 (14 days from project start)

## Core Claims (3 conditions)

1. **Complexity-Dependent Reformulation Advantage**: Binary pass/fail classification and execution output generation (CWM-style) achieve equivalent accuracy on simple function-level code (4B: F1 diff 0.9pp), but classification scales better with model size (8B 3-seed mean accuracy gap=2.43pp; seed42: 2.81pp, cls 90.48% vs cwm 87.67%) and to repo-level complexity where CWM failure modes—token-budget exhaustion and string-value prediction errors—dominate. Zero-shot LLM-as-judge baselines (8B: 64.4%, 32B NF4: 71.7%) are far below fine-tuned 4B (88.4%), confirming fine-tuning necessity. (Validated function-level near-null + 8B scaling evidence; repo-level SWE-bench experiments in progress. Fallback: if repo-level also null, reframe to efficiency-equivalent accuracy—same F1 with 1-token vs N-token inference.)

2. **Diagnostic Granularity At Equivalent Accuracy**: Per-test classification achieves equivalent variant-level accuracy to trajectory-level scoring (TOST equivalence test p=0.007, ±2pp margin; 5-seed pooled gap -0.40pp, 95% CI [-1.32, +0.52]) while providing actionable diagnostic information (which specific tests a patch fails). The per-test formulation gains diagnostic granularity without sacrificing accuracy—potentially enabling targeted re-repair and oracle-based test selection. (Evidence: 5-paired clustered bootstrap CI, 114 clusters, 10000 resamples. Paper must justify ±2pp margin: in code verification, 2pp variant-level difference is negligible given ICC=0.191/DEFF=3.97. Seeds 789/0 used 4-bit quantization — note in paper. Downstream re-repair experiment still needed for practical impact claim.)

3. **Accuracy-Utility Frontier Characterization**: The effectiveness of per-test verification depends critically on test distribution characteristics. We empirically show: (a) per-test advantage concentrates in instances with multiple FAIL_TO_PASS tests (31% of SWE-bench Verified); (b) PASS_TO_PASS regression detection provides signal only when regression rate exceeds ~10%; (c) block-correlated prediction errors amplify per-test advantage through reduced effective degrees of freedom. These findings provide a practical decision framework for when per-test simulation is worth deploying.

## Story Spine

**Problem**: Test-time scaling for code repair requires ranking candidate patches, but verification paradigms face a granularity-cost tradeoff. Full execution costs ~$1-3 and minutes per candidate. Execution-free alternatives like SWE-RM predict trajectory-level binary correctness at low cost but provide only coarse signals that cannot distinguish between candidates failing on different test subsets.

**Existing approaches & gaps**: Code World Models (Self-Execution Simulation, CWM) predict execution outputs but suffer from token-budget exhaustion and string-value prediction failures. SWE-RM achieves strong trajectory-level scoring but loses per-test diagnostic information. No work studies per-test binary classification as a dedicated verification formulation, or compares classification vs generation formulations for code execution simulation at controlled model sizes.

**Our framing**: We reformulate execution simulation from an open-ended generation task (predict execution trace/output) to a closed-form classification task (predict binary pass/fail per test). On simple function-level code, both formulations achieve equivalent accuracy (~87% F1), because short execution outputs do not trigger CWM failure modes. However, on repo-level code with long execution traces and complex outputs, classification sidesteps token-budget exhaustion and string-value prediction errors, yielding a complexity-dependent advantage. We empirically ground this through (1) controlled function-level experiments establishing equivalence, (2) repo-level experiments demonstrating the complexity threshold, (3) oracle accuracy-utility frontier analysis revealing when per-test granularity helps, and (4) error complementarity analysis showing CLS/CWM have systematically opposite failure modes (CLS: miss bugs 75.5%, CWM: false alarms 83.1%), with oracle ensemble reaching 90.63%. (Downstream re-repair experiment is stretch goal; if not completed, frame as future work.)

**Headline result template**: "On function-level benchmarks, classification and generation verifiers achieve equivalent F1 (~87%), but classification scales better with model size (8B: +2.43pp accuracy) and on repo-level SWE-bench tasks outperforms by [Z] percentage points as CWM failure modes emerge. CLS and CWM exhibit complementary error patterns (oracle ensemble: 90.63%), suggesting formulation diversity as a verification strategy."

## Venue Fit Risks

1. **EMNLP vs SE venue**: Core concern is code repair verification, which may be perceived as SE rather than NLP. Mitigation: frame as (a) probing LLM code semantic reasoning capabilities through per-test prediction, and (b) a general NLP methodology insight about classification vs generation formulations applicable beyond code.

2. **Negative P2P finding**: P2P regression rate ~1% means per-test is not universally better. Must present honestly as a characterization finding, not bury it. This actually strengthens the paper by showing nuanced understanding rather than overclaiming.

3. **Function-level to repo-level gap**: Function-level results show classification ≈ generation. Repo-level extension is now CRITICAL (not optional) to demonstrate the complexity-dependent advantage. Requires SWE-bench Docker infrastructure. If repo-level also shows no advantage, paper pivots to efficiency framing (same accuracy, lower inference cost) + oracle characterization.

## Anticipated Reviewer Concerns & Mitigations

| Concern | Mitigation Experiment |
|---------|----------------------|
| "Classification is trivially easier than generation -- not interesting" | Function-level null result proves classification is NOT trivially easier; advantage is complexity-dependent, demonstrated by repo-level gap |
| "Per-test is just trajectory-level with extra steps when T=1" | Oracle frontier analysis shows T distribution sensitivity; honest reporting of T=1 equivalence |
| "No practical downstream impact" | Diagnostic re-repair experiment shows resolve rate improvement |
| "Small-scale function-level results don't generalize" | Repo-level SWE-bench extension (if resources allow) |
| "CWM comparison is unfair (different output format)" | Matched model, data, compute; discuss target asymmetry limitation |


## experiment_plan (with registry status)

- id: cwm-baseline
  claim: 1
  description: Train CWM generation baseline (Qwen3-4B LoRA, same data/config as MVP-B)
    to predict execution output instead of pass/fail. Compare per-class F1 against
    classification model (87.1/87.9%).
  priority: P0
  gpu_budget_hours: 2
  deps:
  - mvp-b-train
  status: DONE
  registry_id: cwm-baseline
  conclusion: negative
  metrics:
    overall_accuracy: 87.51
    pass_f1: 87.31
    fail_f1: 87.71
    pass_precision: 92.06
    pass_recall: 83.03
    fail_precision: 83.53
    fail_recall: 92.32
    exact_match_rate: 84.02
    train_loss: 0.2534
    eval_loss: 0.0644
    train_runtime_sec: 3439
    test_set_size: 1890
    unparseable_predictions: 0
- id: multi-seed-core
  claim: 1
  description: 'Multi-seed validation for core comparison: run classification (mvp-b-train)
    and CWM baseline each with seeds {0, 1, 42}. Report mean +/- std F1. Statistical
    significance via paired t-test or bootstrap CI. Required for any claim of ''significantly
    better''.'
  priority: P0
  gpu_budget_hours: 8
  deps:
  - cwm-baseline
  registry_id: traj-level-seed0
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 85.66
    unresolved_f1: 87.37
    resolved_f1: 83.41
    unresolved_precision: 82.71
    unresolved_recall: 92.59
    resolved_precision: 90.07
    resolved_recall: 77.66
    consistency_rate: 79.55
    train_loss: 0.225
    eval_loss_epoch1: 0.0949
    eval_loss_epoch2: 0.0885
    eval_loss_epoch3: 0.1011
    train_runtime_sec: 4071.3
- id: trace-then-judge
  claim: 1
  description: 'Trace-then-Judge ablation (chain-of-thought, NOT pipeline): single
    Qwen3-4B model trained to first generate a brief execution reasoning trace (~50
    tokens describing expected behavior), then output pass/fail. Same LoRA config/data.
    Tests whether explicit execution reasoning helps or hurts compared to direct classification.
    If trace-then-judge >= direct classification, the advantage is from task simplicity,
    not from skipping reasoning.'
  priority: P0
  gpu_budget_hours: 4
  deps:
  - cwm-baseline
  registry_id: trace-then-judge
  status: DONE
  conclusion: failed
- id: traj-level-finetuned
  claim: 1
  description: 'Same-size fine-tuned trajectory-level baseline: Qwen3-4B LoRA trained
    to predict resolved/unresolved. Data construction: for each problem_id, aggregate
    all (code, test) pairs into (code, all_tests_concatenated) -> resolved (original
    code passes all tests) / unresolved (mutated code fails any test). Same train/val/test
    split by problem_id. Isolates granularity effect.'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - mvp-b-data-prep
  registry_id: traj-level-finetuned
  status: DONE
  conclusion: success
  metrics:
    accuracy: 85.66
    unresolved_f1: 87.5
    resolved_f1: 83.18
    per_test_consistency: 79.94
- id: model-size-scaling
  claim: 1
  description: Scale classification model from 4B to 8B. Measure accuracy improvement
    and compare with CWM at 8B. Determine if classification advantage holds across
    scales.
  priority: P1
  gpu_budget_hours: 8
  deps:
  - cwm-baseline
  registry_id: model-size-scaling-cls8b
  sub_experiments:
  - registry_id: model-size-scaling-cls8b
    gpu: seetacloud cuda:0
    description: Qwen3-8B LoRA classification
  - registry_id: model-size-scaling-cwm8b
    gpu: seetacloud cuda:1
    description: Qwen3-8B LoRA CWM generation
  status: DONE
  conclusion: success
  metrics:
    accuracy: 90.48
    pass_f1: 90.86
    fail_f1: 90.06
    pass_precision: 90.22
    pass_recall: 91.51
    fail_precision: 90.76
    fail_recall: 89.36
    train_loss: 0.3125
    eval_loss_epoch1: 0.0723
    eval_loss_epoch2: 0.0741
    eval_loss_epoch3: 0.0783
    train_runtime_sec: 5614
    unparseable: 0
- id: diagnostic-rerepair
  claim: 2
  description: 'Downstream proof-of-concept: give repair agent per-test failure predictions
    vs no per-test info, compare resolve rate on 200 instances. Uses SWE-agent or
    similar repair framework.'
  priority: P1
  gpu_budget_hours: 12
  deps:
  - cwm-baseline
  - traj-level-finetuned
  status: planned
- id: per-test-precision-recall
  claim: 2
  description: Measure per-test failure prediction precision/recall against ground-truth
    failing tests on full test set. Evaluate diagnostic signal quality without downstream
    execution.
  priority: P0
  gpu_budget_hours: 1
  deps:
  - mvp-b-train
  registry_id: per-test-precision-recall
  status: DONE
  conclusion: success
  metrics:
    accuracy: 87.51
    fail_precision: 82.75
    fail_recall: 93.64
    fail_f1: 87.86
    pass_precision: 93.24
    pass_recall: 81.8
    pass_f1: 87.15
    FP_count: 58
    FN_count: 178
    best_mutation: return_value (97.26%)
    worst_mutation: off_by_one (82.56%)
    bucket_6_10_acc: 96.3
    bucket_11plus_acc: 87.12
- id: oracle-f2p-stratified
  claim: 3
  description: Stratified oracle analysis by F2P test count (T=1, T=2, T=3+). Report
    per-test advantage breakdown showing advantage concentrates in multi-test instances.
  priority: P0
  gpu_budget_hours: 0
  deps:
  - mvp-a-oracle-sim
  registry_id: oracle-f2p-stratified
  status: DONE
  conclusion: success
  metrics:
    T1_pct: 68.7
    T1_block_adv: -0.09
    T2_pct: 19.1
    T2_block_adv: 31.69
    T3_5_pct: 7.1
    T3_5_block_adv: 40.74
    T6plus_pct: 5.1
    T6plus_block_adv: 40.06
    overall_block_adv: 10.93
    T2_contribution_pct: 55.3
- id: oracle-total-validated
  claim: 3
  description: Oracle study with Total (F2P+P2P) distribution at empirically measured
    regression rates. Validate when P2P tests help vs hurt.
  priority: P0
  gpu_budget_hours: 0
  deps:
  - p2p-regression-rate
  status: DONE
  registry_id: mvp-a-oracle-sim
  conclusion: success
  metrics:
    original_T12:
      iid_adv_70_85: 0.1849
      block_adv_70_85: 0.3618
    sensitivity_T3:
      iid_adv_70_85: 0.0761
      block_adv_70_85: 0.3839
    sensitivity_T7:
      iid_adv_70_85: 0.1351
      block_adv_70_85: 0.3833
    sensitivity_T11:
      iid_adv_70_85: 0.1863
      block_adv_70_85: 0.3639
    real_f2p_T1:
      iid_adv_70_85: 0.0198
      block_adv_70_85: 0.1088
      pct_T1: 0.687
      T_median: 1
      T_mean: 2.3
    swebench_f2p_stats:
      median: 1
      mean: 3
      P75: 2
      P90: 3
    total_reg5pct:
      iid_adv_70_85: -0.01
      block_adv_70_85: -0.005
      pass: false
    total_reg10pct:
      iid_adv_70_85: 0.132
      block_adv_70_85: 0.083
      pass: true
    total_reg20pct:
      iid_adv_70_85: 0.357
      block_adv_70_85: 0.278
      pass: true
- id: block-corr-empirical
  claim: 3
  description: 'Empirically validate block-correlation assumption: measure actual
    prediction error correlation structure from trained model''s test-level predictions,
    compare with i.i.d. and block-correlated simulation models.'
  priority: P2
  gpu_budget_hours: 1
  deps:
  - mvp-b-train
  registry_id: block-corr-empirical
  status: DONE
  conclusion: success
  metrics:
    icc: 0.1909
    icc_p_value: 0
    design_effect: 3.9676
    overall_error_rate: 0.1249
    all_correct_observed: 46
    all_correct_expected_iid: 16.35
    all_correct_ratio: 2.81
    error_std_observed: 0.1531
    error_std_expected_iid: 0.0811
    error_std_ratio: 1.89
    n_samples: 1890
    n_problems: 114
    inference_precision: bfloat16
    version: v2_corrected
- id: swebench-pertest-data
  claim:
  - 1
  - 2
  - 3
  description: Docker re-evaluation of SWE-bench Verified patches to extract per-test
    labels. Build SWE-bench-PerTest dataset (500 instances x 16 candidates). Resource
    contribution.
  priority: P1
  gpu_budget_hours: 0
  compute_note: CPU/Docker only, ~16-24h with 16 parallel containers. Start early
    to parallelize with GPU experiments.
  deps: []
  status: planned
- id: repo-level-training
  claim:
  - 1
  - 2
  description: Fine-tune Qwen3-4B/8B on repo-level (patched_code, test_code) -> pass/fail
    using SWE-bench-PerTest data. Evaluate on held-out instances.
  priority: P1
  gpu_budget_hours: 12
  deps:
  - swebench-pertest-data
  registry_id: repo-level-cwm-v3
  status: DONE
  conclusion: failed
- id: llm-judge-baseline
  claim:
  - 1
  - 3
  description: Qwen3-8B/32B zero-shot LLM-as-judge baselines (trajectory-level and
    per-test). Reference points for Pareto frontier.
  priority: P1
  gpu_budget_hours: 8
  deps: []
  registry_id: llm-judge-8b-zeroshot
  sub_experiments:
  - registry_id: llm-judge-8b-zeroshot
    gpu: seetacloud cuda:2
    description: Qwen3-8B zero-shot per-test + trajectory-level
  - registry_id: llm-judge-32b-zeroshot
    gpu: seetacloud cuda:3
    description: Qwen3-32B 4-bit quantized zero-shot
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 64.4
    fail_precision: 57.9
    fail_recall: 95.8
    fail_f1: 72.2
    pass_precision: 90
    pass_recall: 35.1
    pass_f1: 50.5
    majority_baseline: 51.7
    accuracy_vs_baseline_gap: 12.6
    traj_accuracy: 99.1
    traj_problems: 114
    traj_true_resolved: 1
    traj_pred_resolved: 0
    confusion:
      TP_fail: 874
      FN_fail: 38
      FP_fail: 635
      TN_fail: 343
- id: per-test-majority-voting
  claim: 1
  description: Per-test majority voting (K=3) with classification model. Test if self-consistency
    improves per-test accuracy.
  priority: P2
  gpu_budget_hours: 3
  deps:
  - mvp-b-train
  registry_id: per-test-majority-voting
  status: DONE
  conclusion: negative
  metrics:
    accuracy_greedy: 87.51
    accuracy_majority_vote_K3: 86.83
    delta_accuracy: -0.69
    fail_f1_greedy: 87.86
    fail_f1_mv: 87.29
    pass_f1_greedy: 87.15
    pass_f1_mv: 86.33
    unanimous_rate: 93.3
    split_samples: 127
    flipped_correct_to_wrong: 28
    flipped_wrong_to_correct: 15
    net_flips: -13
    per_pass_accuracy:
    - 86.72
    - 86.83
    - 87.62
    wall_time_greedy_sec: 30
    wall_time_mv_sec: 120


## registry (completed experiments)

- exp_id: mvp-a-oracle-sim
  name: ''
  status: DONE
  conclusion: success
  metrics:
    original_T12:
      iid_adv_70_85: 0.1849
      block_adv_70_85: 0.3618
    sensitivity_T3:
      iid_adv_70_85: 0.0761
      block_adv_70_85: 0.3839
    sensitivity_T7:
      iid_adv_70_85: 0.1351
      block_adv_70_85: 0.3833
    sensitivity_T11:
      iid_adv_70_85: 0.1863
      block_adv_70_85: 0.3639
    real_f2p_T1:
      iid_adv_70_85: 0.0198
      block_adv_70_85: 0.1088
      pct_T1: 0.687
      T_median: 1
      T_mean: 2.3
    swebench_f2p_stats:
      median: 1
      mean: 3
      P75: 2
      P90: 3
    total_reg5pct:
      iid_adv_70_85: -0.01
      block_adv_70_85: -0.005
      pass: false
    total_reg10pct:
      iid_adv_70_85: 0.132
      block_adv_70_85: 0.083
      pass: true
    total_reg20pct:
      iid_adv_70_85: 0.357
      block_adv_70_85: 0.278
      pass: true
- exp_id: mvp-b-data-prep
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: mvp-b-train
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 0.875
    pass_f1: 0.871
    fail_f1: 0.879
    pass_precision: 0.9324
    pass_recall: 0.818
    fail_precision: 0.8275
    fail_recall: 0.9364
    majority_baseline: 0.52
    accuracy_vs_majority_gap: 0.355
- exp_id: p2p-regression-rate
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: cwm-baseline
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    overall_accuracy: 87.51
    pass_f1: 87.31
    fail_f1: 87.71
    pass_precision: 92.06
    pass_recall: 83.03
    fail_precision: 83.53
    fail_recall: 92.32
    exact_match_rate: 84.02
    train_loss: 0.2534
    eval_loss: 0.0644
    train_runtime_sec: 3439
    test_set_size: 1890
    unparseable_predictions: 0
- exp_id: multi-seed-core
  name: ''
  status: DONE
  conclusion: success
  metrics:
    seed42:
      accuracy: 87.83
      pass_f1: 88.06
      fail_f1: 87.59
      pass_precision: 89.45
      pass_recall: 86.71
      fail_precision: 86.2
      fail_recall: 89.04
    seed123:
      accuracy: 89.52
      pass_f1: 89.64
      fail_f1: 89.4
      pass_precision: 91.76
      pass_recall: 87.63
      fail_precision: 87.34
      fail_recall: 91.56
    seed456:
      accuracy: 87.88
      pass_f1: 87.53
      fail_f1: 88.21
      pass_precision: 93.6
      pass_recall: 82.21
      fail_precision: 83.12
      fail_recall: 93.97
    mean:
      accuracy: 88.41
      pass_f1: 88.41
      fail_f1: 88.4
    std:
      accuracy: 0.96
      pass_f1: 1.1
      fail_f1: 0.92
- exp_id: trace-then-judge
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: traj-level-finetuned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 85.66
    unresolved_f1: 87.5
    resolved_f1: 83.18
    per_test_consistency: 79.94
- exp_id: model-size-scaling-cls8b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 90.48
    pass_f1: 90.86
    fail_f1: 90.06
    pass_precision: 90.22
    pass_recall: 91.51
    fail_precision: 90.76
    fail_recall: 89.36
    train_loss: 0.3125
    eval_loss_epoch1: 0.0723
    eval_loss_epoch2: 0.0741
    eval_loss_epoch3: 0.0783
    train_runtime_sec: 5614
    unparseable: 0
- exp_id: model-size-scaling-cwm8b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 87.67
    pass_f1: 87.57
    fail_f1: 87.77
    pass_precision: 91.53
    pass_recall: 83.95
    fail_precision: 84.19
    fail_recall: 91.67
    exact_match_rate: 84.39
    train_loss: 0.229
    eval_loss_epoch1: 0.0554
    eval_loss_epoch2: 0.0512
    eval_loss_epoch3: 0.0564
    train_runtime_sec: 5570
    unparseable: 0
- exp_id: llm-judge-8b-zeroshot
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 64.4
    fail_precision: 57.9
    fail_recall: 95.8
    fail_f1: 72.2
    pass_precision: 90
    pass_recall: 35.1
    pass_f1: 50.5
    majority_baseline: 51.7
    accuracy_vs_baseline_gap: 12.6
    traj_accuracy: 99.1
    traj_problems: 114
    traj_true_resolved: 1
    traj_pred_resolved: 0
    confusion:
      TP_fail: 874
      FN_fail: 38
      FP_fail: 635
      TN_fail: 343
- exp_id: llm-judge-32b-zeroshot
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 71.69
    majority_baseline: 51.75
    accuracy_vs_baseline_gap: 19.95
    fail_precision: 64.4
    fail_recall: 92.43
    fail_f1: 75.91
    pass_precision: 88.12
    pass_recall: 52.35
    pass_f1: 65.68
    unparseable_predictions: 0
    trajectory_accuracy: 99.12
    trajectory_total_problems: 114
    trajectory_correct: 113
    trajectory_true_resolved: 1
    trajectory_pred_resolved: 0
- exp_id: per-test-precision-recall
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 87.51
    fail_precision: 82.75
    fail_recall: 93.64
    fail_f1: 87.86
    pass_precision: 93.24
    pass_recall: 81.8
    pass_f1: 87.15
    FP_count: 58
    FN_count: 178
    best_mutation: return_value (97.26%)
    worst_mutation: off_by_one (82.56%)
    bucket_6_10_acc: 96.3
    bucket_11plus_acc: 87.12
- exp_id: oracle-f2p-stratified
  name: ''
  status: DONE
  conclusion: success
  metrics:
    T1_pct: 68.7
    T1_block_adv: -0.09
    T2_pct: 19.1
    T2_block_adv: 31.69
    T3_5_pct: 7.1
    T3_5_block_adv: 40.74
    T6plus_pct: 5.1
    T6plus_block_adv: 40.06
    overall_block_adv: 10.93
    T2_contribution_pct: 55.3
- exp_id: traj-level-seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 85.47
    unresolved_f1: 87
    resolved_f1: 83.52
    unresolved_precision: 83.53
    unresolved_recall: 90.78
    resolved_precision: 88.17
    resolved_recall: 79.33
    consistency_rate: 78.59
- exp_id: traj-level-seed456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 87.4
    unresolved_f1: 88.7
    resolved_f1: 85.8
    unresolved_precision: 85.7
    unresolved_recall: 91.9
    resolved_precision: 89.7
    resolved_recall: 82.3
    consistency_rate: 78.8
- exp_id: per-test-majority-voting
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy_greedy: 87.51
    accuracy_majority_vote_K3: 86.83
    delta_accuracy: -0.69
    fail_f1_greedy: 87.86
    fail_f1_mv: 87.29
    pass_f1_greedy: 87.15
    pass_f1_mv: 86.33
    unanimous_rate: 93.3
    split_samples: 127
    flipped_correct_to_wrong: 28
    flipped_wrong_to_correct: 15
    net_flips: -13
    per_pass_accuracy:
    - 86.72
    - 86.83
    - 87.62
    wall_time_greedy_sec: 30
    wall_time_mv_sec: 120
- exp_id: block-corr-empirical
  name: ''
  status: DONE
  conclusion: success
  metrics:
    icc: 0.1909
    icc_p_value: 0
    design_effect: 3.9676
    overall_error_rate: 0.1249
    all_correct_observed: 46
    all_correct_expected_iid: 16.35
    all_correct_ratio: 2.81
    error_std_observed: 0.1531
    error_std_expected_iid: 0.0811
    error_std_ratio: 1.89
    n_samples: 1890
    n_problems: 114
    inference_precision: bfloat16
    version: v2_corrected
- exp_id: traj-level-seed789
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 87.31
    unresolved_f1: 88.27
    resolved_f1: 86.17
    unresolved_precision: 87.41
    unresolved_recall: 89.15
    resolved_precision: 87.18
    resolved_recall: 85.18
    consistency_rate: 76.74
    eval_loss: 0.1115
    train_loss: 0.2255
    train_runtime_sec: 2055.9
- exp_id: traj-level-seed0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 85.66
    unresolved_f1: 87.37
    resolved_f1: 83.41
    unresolved_precision: 82.71
    unresolved_recall: 92.59
    resolved_precision: 90.07
    resolved_recall: 77.66
    consistency_rate: 79.55
    train_loss: 0.225
    eval_loss_epoch1: 0.0949
    eval_loss_epoch2: 0.0885
    eval_loss_epoch3: 0.1011
    train_runtime_sec: 4071.3
- exp_id: cls8b-seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 89.4
    pass_f1: 89.5
    fail_f1: 89.2
    pass_precision: 91.2
    pass_recall: 87.9
    fail_precision: 87.5
    fail_recall: 90.9
    train_loss: 0.3087
    eval_loss: 0.0848
    train_runtime_sec: 5666
    unparseable: 0
- exp_id: cwm8b-seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 86.98
    pass_f1: 86.83
    fail_f1: 87.13
    pass_precision: 91.12
    pass_recall: 82.92
    fail_precision: 83.3
    fail_recall: 91.34
    exact_match_rate: 84.13
    unparseable: 0
    test_set_size: 1890
- exp_id: cls-seed789
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 89
    pass_f1: 88.9
    fail_f1: 89.1
    pass_precision: 93.3
    pass_recall: 84.9
    fail_precision: 85.2
    fail_recall: 93.4
- exp_id: cls-seed0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 87.94
    pass_f1: 87.79
    fail_f1: 88.08
    pass_precision: 92.13
    pass_recall: 83.84
    fail_precision: 84.2
    fail_recall: 92.32
    train_loss: 0.2347
    eval_loss: 0.0963
    train_runtime_sec: 4976.75
    unparseable: 0
- exp_id: repo-level-cls
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cwm
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cwm-seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 87.2
    pass_f1: 86.95
    fail_f1: 87.44
    exact_match_rate: 84.44
    majority_baseline_accuracy: 51.75
    accuracy_vs_baseline_gap_pp: 35.45
    test_set_size: 1890
    unparseable_predictions: 0
- exp_id: cwm-seed456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 86.98
    pass_f1: 86.66
    fail_f1: 87.29
    pass_precision: 92.26
    pass_recall: 81.7
    fail_precision: 82.52
    fail_recall: 92.65
    exact_match_rate: 84.02
    train_loss: 0.2525
    eval_loss_best: 0.0551
    eval_loss_final: 0.0635
    train_runtime_sec: 3440
    unparseable: 0
- exp_id: cwm-seed789
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 86.67
    pass_f1: 86.74
    fail_f1: 86.6
    exact_match_rate: 83.97
    baseline_gap_pp: 34.92
    test_set_size: 1890
    unparseable_predictions: 0
    per_class:
      fail:
        precision: 84.09
        recall: 89.25
        f1: 86.6
      pass:
        precision: 89.37
        recall: 84.25
        f1: 86.74
- exp_id: cwm-seed0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 87.57
    fail_f1: 87.93
    fail_precision: 82.71
    fail_recall: 93.86
    pass_f1: 87.18
    pass_precision: 93.45
    pass_recall: 81.7
    exact_match_rate: 84.29
    eval_loss: 0.0665
    train_loss: 0.2554
    train_runtime_sec: 3586
- exp_id: 5-paired-clustered-bootstrap
  name: ''
  status: DONE
  conclusion: success
  metrics:
    pooled_gap_pp: -0.45
    pooled_ci_lower: -1.71
    pooled_ci_upper: 0.84
    pooled_p_value: 0.499
    tost_p_value: 0.0071
    tost_margin_pp: 2
    seed_level_paired_t_p: 0.425
    seed_level_mean_gap: -0.48
    n_variants_pooled: 523
    n_clusters: 114
    per_seed_gaps:
      seed42: -0.97
      seed123: 1.45
      seed456: -1.84
      seed789: -0.78
      seed0: -0.29
- exp_id: cwm8b-seed456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 86.24
    pass_f1: 85.96
    fail_f1: 86.51
    pass_precision: 91.08
    pass_recall: 81.39
    fail_precision: 82.09
    fail_recall: 91.45
    exact_match_rate: 82.8
    train_loss: 0.2279
    eval_loss: 0.0583
    unparseable: 0
    test_set_size: 1890
    majority_baseline_accuracy: 51.75
    accuracy_vs_baseline_gap_pp: 34.5
- exp_id: cls8b-seed456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 88.31
    pass_f1: 88.2
    fail_f1: 88.41
    pass_precision: 92.29
    pass_recall: 84.46
    fail_precision: 84.72
    fail_recall: 92.43
    train_loss: 0.3105
    eval_loss: 0.0928
    unparseable: 0
    test_set_size: 1890
- exp_id: repo-level-cls-v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cwm-v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cls-v3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cwm-v3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cls-home
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cls-v4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.6611
    f1_macro: 0.5661
    f1_pass: 0.769
    f1_fail: 0.363
    precision_pass: 0.765
    recall_pass: 0.774
    precision_fail: 0.369
    recall_fail: 0.357
    majority_baseline: 0.7296
    n_unparseable: 132
    best_checkpoint: checkpoint-200
    early_stop: D045
- exp_id: cls8b-eval-seed42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 90.48
    pass_f1: 90.86
    fail_f1: 90.06
    pass_precision: 90.22
    pass_recall: 91.51
    fail_precision: 90.76
    fail_recall: 89.36
    unparseable: 0
    test_set_size: 1890
- exp_id: cls8b-eval-seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 89.37
    pass_f1: 89.54
    fail_f1: 89.19
    pass_precision: 91.2
    pass_recall: 87.93
    fail_precision: 87.54
    fail_recall: 90.9
    unparseable: 0
    test_set_size: 1890
- exp_id: matched-seed-8b-predictions
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: repo-level-cwm-v4
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: repo-level-cwm-v5
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cwm-v6
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cwm-v7
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cwm-v8
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cwm-v9
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cls-seed123
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: repo-level-cwm-seed123
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: repo-level-cwm-v10
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.6991
    f1_macro: 0.4671
    f1_pass: 0.8187
    f1_fail: 0.1154
    precision_pass: 0.7304
    recall_pass: 0.9314
    precision_fail: 0.2815
    recall_fail: 0.0726
    majority_baseline: 0.7296
    n_unparseable: 9102
    n_unparseable_pct: 0.93
    n_truncated: 478
    n_truncated_pct: 0.0489
    truncated_accuracy: 0.2176
    best_checkpoint: checkpoint-400
    early_stop: D045
    eval_invalid: max_new_tokens=64 caused 93% unparseable (D047)
- exp_id: repo-level-cls-v5
  name: ''
  status: DONE
  conclusion: success
  metrics:
    checkpoint_sweep:
      ckpt_600:
        accuracy: 76.74
        f1_macro: 73.74
        fail_f1: 64.88
        pass_f1: 82.61
      ckpt_4000:
        accuracy: 81.51
        f1_macro: 72.56
        fail_f1: 56.9
        pass_f1: 88.23
      ckpt_4200:
        accuracy: 80.64
        f1_macro: 72.1
        fail_f1: 56.66
        pass_f1: 87.54
      ckpt_4400:
        accuracy: 82.11
        f1_macro: 73.94
        fail_f1: 59.34
        fail_precision: 77.02
        fail_recall: 48.26
      ckpt_4600:
        accuracy: 82.35
        f1_macro: 74.74
        fail_f1: 60.87
        pass_f1: 88.6
        fail_precision: 76
        fail_recall: 50.76
    best_checkpoint_accuracy: checkpoint-4600
    best_checkpoint_f1: checkpoint-4600
    eval_samples: 9784
    accuracy: 82.35
    f1_macro: 74.74
    unparseable: 132
    unparseable_pct: 1.3
    majority_baseline: 72.96
    gap_vs_baseline: 9.39
    eval_server: home-1x5090
    eval_env: transformers 4.57.6
    note: Test set sweep complete. ckpt-4600 best on both accuracy (82.35%) and f1_macro
      (74.74%).
    val_2048:
      ckpt_600:
        accuracy: 77.25
        f1_macro: 70.81
        fail_f1: 57.11
        pass_f1: 84.52
      ckpt_4000:
        accuracy: 83.32
        f1_macro: 70.26
        fail_f1: 50.56
        pass_f1: 89.97
      ckpt_4200:
        accuracy: 82.82
        f1_macro: 69.54
        fail_f1: 49.43
        pass_f1: 89.65
      ckpt_4400:
        accuracy: 83.49
        f1_macro: 71.63
        fail_f1: 53.29
        pass_f1: 89.97
      ckpt_4600:
        accuracy: 83.63
        f1_macro: 71.72
        fail_f1: 53.36
        pass_f1: 90.07
      eval_samples: 9335
      unparseable: 1883
      unparseable_pct: 20.2
      val_best_f1: ckpt-4600
      val_best_acc: ckpt-4600
      note: 'val-test 一致: 都是 ckpt-4600'
- exp_id: repo-level-cwm-v11
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    eval_checkpoint: checkpoint-600
    eval_samples: 500
    eval_type: subset500_tok1024
    accuracy: 66.6
    fail_f1: 27.7
    pass_f1: 78.3
    f1_macro: 52.99
    fail_precision: 33.3
    fail_recall: 23.7
    pass_precision: 74.5
    pass_recall: 82.5
    unparseable: 376
    unparseable_pct: 75.2
    majority_baseline: 73
    gap_vs_baseline: -6.4
    gen_length_mean: 3398.1
    gen_length_median: 3307.5
    gen_length_max: 7582
    confusion:
      TP: 301
      TN: 32
      FP: 103
      FN: 64
- exp_id: repo-level-cls-8b
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    eval_checkpoint: checkpoint-200
    eval_samples: 9784
    accuracy: 71.37
    fail_f1: 60.57
    pass_f1: 77.53
    f1_macro: 69.05
    fail_precision: 48.26
    fail_recall: 81.29
    pass_precision: 90.71
    pass_recall: 67.69
    unparseable: 136
    unparseable_pct: 1.39
    majority_baseline: 73
    gap_vs_baseline: -1.63
    confusion:
      TP: 4832
      TN: 2151
      FP: 495
      FN: 2306
    eval_server: westd-48478
    eval_env: transformers 5.8.0
- exp_id: repo-level-cls-seed123-home
  name: ''
  status: DONE
  conclusion: success
  metrics:
    val_2048:
      n: 9335
      unparseable: 1883
      ckpt_200:
        accuracy: 62.51
        f1_macro: 55.54
        f1_pass: 73.14
        f1_fail: 37.94
      ckpt_400:
        accuracy: 80.72
        f1_macro: 67.03
        f1_pass: 88.27
        f1_fail: 45.78
      ckpt_600:
        accuracy: 76.78
        f1_macro: 66.81
        f1_pass: 85
        f1_fail: 48.63
      ckpt_800:
        accuracy: 81.81
        f1_macro: 69.14
        f1_pass: 88.91
        f1_fail: 49.37
      ckpt_1000:
        accuracy: 82.3
        f1_macro: 67.63
        f1_pass: 89.42
        f1_fail: 45.84
      best_f1: ckpt_800
      best_acc: ckpt_1000
    val_4096:
      n: 9335
      unparseable: 1406
      ckpt_400:
        accuracy: 82.57
        f1_macro: 71.24
        f1_pass: 89.29
        f1_fail: 53.18
      ckpt_600:
        accuracy: 79.18
        f1_macro: 70.73
        f1_pass: 86.45
        f1_fail: 55
      ckpt_800:
        accuracy: 83.7
        f1_macro: 73.31
        f1_pass: 90
        f1_fail: 56.7
      best_f1: ckpt_800
      best_acc: ckpt_800
    val_5120:
      n: 9335
      unparseable: 0
      truncated: 234
      ckpt_400:
        accuracy: 86.01
        f1_macro: 79.66
        f1_pass: 91.02
        f1_fail: 68.3
      ckpt_600:
        accuracy: 81.89
        f1_macro: 77.01
        f1_pass: 87.6
        f1_fail: 66.43
      ckpt_800:
        accuracy: 87.92
        f1_macro: 81.95
        f1_pass: 92.33
        f1_fail: 71.57
      best_f1: ckpt_800
      best_acc: ckpt_800
- exp_id: repo-level-cwm-v12
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    eval_test_accuracy: 58.04
    eval_test_f1_macro: 51.67
    eval_test_f1_fail: 34.12
    eval_test_f1_pass: 69.22
    eval_test_unparseable: 5255
    eval_test_total: 9784
    eval_test_unparseable_rate: 53.7
    eval_checkpoint: checkpoint-500
- exp_id: repo-level-cwm-seed123-conda
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    eval_test_accuracy: 59.09
    eval_test_f1_macro: 43.43
    eval_test_f1_fail: 13.67
    eval_test_f1_pass: 73.19
    eval_test_unparseable: 6574
    eval_test_total: 9784
    eval_test_unparseable_rate: 67.2
    eval_checkpoint: checkpoint-500
- exp_id: repo-level-cls-8b-conda
  name: ''
  status: DONE
  conclusion: success
  metrics:
    val_8192:
      ckpt_200:
        accuracy: 63.52
        f1_macro: 61.17
        f1_fail: 51.6
        f1_pass: 70.7
        unparseable: 9
      ckpt_400:
        accuracy: 80.96
      ckpt_600:
        accuracy: 85
      best_acc: ckpt_600
    val_5120:
      ckpt_400:
        accuracy: 80.47
        f1_macro: 75.84
    test_2048:
      ckpt_400:
        accuracy: 84.52
        f1_macro: 80.89
      ckpt_600:
        accuracy: 78.51
    test_8192:
      ckpt_400:
        accuracy: 84.79
        f1_macro: 81.18
        f1_fail: 72.93
        f1_pass: 89.43
        unparseable: 0
        total: 9784
      ckpt_600:
        accuracy: 79.05
        f1_macro: 75.12
        f1_fail: 65.24
        f1_pass: 85
        unparseable: 0
        total: 9784
- exp_id: repo-level-cls-v5-conda
  name: ''
  status: DONE
  conclusion: success
  metrics:
    checkpoint_sweep:
      ckpt_200:
        accuracy: 52.96
        f1_macro: 52.89
        fail_f1: 51.02
        pass_f1: 54.76
      ckpt_400:
        accuracy: 78.43
        f1_macro: 68.41
        fail_f1: 50.61
        pass_f1: 86.21
        fail_precision: 66.48
        fail_recall: 40.85
        pass_precision: 80.82
        pass_recall: 92.36
      ckpt_600:
        accuracy: 76.37
        f1_macro: 71.17
        fail_f1: 58.93
        pass_f1: 83.41
        fail_precision: 55.6
        fail_recall: 62.7
        pass_precision: 85.49
        pass_recall: 81.44
    best_checkpoint_accuracy: checkpoint-400
    best_checkpoint_f1: checkpoint-600
    eval_samples: 9784
    accuracy: 78.43
    f1_macro: 71.17
    unparseable: 132
    unparseable_pct: 1.35
    majority_baseline: 72.96
    eval_server: westd-48478
    eval_env: conda, transformers 4.57.6
- exp_id: repo-level-cwm-8b-conda
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cls-8b-seed123-conda
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cwm-8b-conda-v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cls-8b-seed123-conda-v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cwm-8b-conda-v3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: repo-level-cls-8b-seed123-conda-v3
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: repo-level-cwm-8b-conda-v4
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cls8b-ckpt3000-test-eval
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cls8b-ckpt3000-test-v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cls8b-seed123-ckpt3000-val-eval
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: repo-level-cls-8b-s42-ckpt200-val
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cls8b-seed123-ckpt3000-val8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 88.69
    f1_macro: 81.73
    f1_fail: 70.5
    f1_pass: 93
    precision_fail: 95.2
    precision_pass: 87.6
    recall_fail: 55.9
    recall_pass: 99.1
    majority_baseline: 75.9
    gap_vs_majority_pp: 12.8
    unparseable: 9
    total: 9335
- exp_id: cls8b-s42-ckpt400-test8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 84.79
    f1_macro: 81.18
    f1_fail: 72.93
    f1_pass: 89.43
    precision_fail: 70.32
    precision_pass: 90.74
    recall_fail: 75.74
    recall_pass: 88.15
    majority_baseline: 72.96
    gap_vs_majority_pp: 11.84
    unparseable: 0
    total: 9784
- exp_id: cls4b-seed123-ckpt800-val5120-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 87.92
    f1_macro: 81.95
    f1_pass: 92.33
    f1_fail: 71.57
    unparseable: 0
    truncated: 234
    total: 9335
- exp_id: cls8b-s42-ckpt600-test8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 79.05
    f1_macro: 75.12
    f1_fail: 65.24
    f1_pass: 85
    precision_fail: 59.16
    precision_pass: 88.95
    recall_fail: 72.71
    recall_pass: 81.4
    unparseable: 0
    total: 9784
    majority_baseline: 73
    gap_vs_majority_pp: 6.09
- exp_id: repo-level-cls-8b-s42-resume
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_steps: 6633
    epochs: 3
    train_time_sec: 74425
    final_train_loss: 0.4284
    final_eval_loss: 0.4768
    best_eval_loss_resume: 0.2516
    best_eval_loss_resume_step: 4200
    best_eval_loss_overall: 0.0796
    best_eval_loss_overall_step: 200
    checkpoints_saved: 32
    overfitting: true
    note: Severe overfitting after epoch 2. Resume-best=ckpt-4200. Val sweep running
      on cuda:0.
- exp_id: cls8b-s42-ckpt200-val8192-eval-v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 63.52
    f1_macro: 61.17
    f1_fail: 51.6
    f1_pass: 70.7
    unparseable: 9
    total: 9335
- exp_id: cls4b-v5-val5120-sweep-home
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cls4b-v5-ckpt600-val5120-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 82.82
    f1_macro: 79.81
    f1_fail: 72.03
    f1_pass: 87.6
    precision_fail: 59.3
    recall_fail: 91.7
    unparseable: 0
    total: 9335
- exp_id: cls8b-s42-ckpt800-val8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 84.5
    f1_macro: 79.2
- exp_id: cls4b-v5-ckpt4000-val5120-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 89.84
    f1_macro: 84.25
    f1_fail: 74.85
    f1_pass: 93.64
    precision_fail: 92.95
    recall_fail: 62.66
    precision_pass: 89.24
    recall_pass: 98.49
    unparseable: 0
    truncated: 234
    total: 9335
- exp_id: cls8b-s42-ckpt1000-val8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 88.23
    f1_macro: 82.72
    f1_fail: 73
    f1_pass: 92.5
    precision_fail: 81.8
    recall_fail: 65.8
    precision_pass: 89.8
    recall_pass: 95.3
    unparseable: 9
    total_instances: 9335
- exp_id: cls4b-v5-ckpt4400-val5120-eval
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    accuracy_partial_70pct: 89.69
    f1_macro_partial_70pct: 84.61
    samples_completed: 6544
    samples_total: 9335
- exp_id: cls8b-s42-ckpt1000-test8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 83.52
    f1_macro: 77.5
    f1_fail: 65.85
    f1_pass: 89.14
    precision_fail: 74.93
    recall_fail: 58.73
    precision_pass: 85.84
    recall_pass: 92.72
    majority_baseline: 72.96
    gap_vs_majority: 10.56
    unparseable_count: 0
    unparseable_rate: 0
    total_samples: 9784
    tp: 6618
    fp: 1092
    fn: 520
    tn: 1554
- exp_id: cls4b-v5-ckpt4400-val5120-eval-v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cls8b-s42-ckpt1200-val8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: cls8b-s42-ckpt1400-val8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 85.97
    majority_baseline: 75.88
    gap_vs_majority_pp: 10.09
    f1_macro: 77.15
    f1_fail: 62.95
    f1_pass: 91.34
    precision_fail: 86.68
    precision_pass: 85.85
    recall_fail: 49.42
    recall_pass: 97.59
    n_instances: 9335
    n_unparseable: 9
    confusion_matrix:
      tn: 1113
      fp: 1139
      fn: 171
      tp: 6912
- exp_id: cls8b-s42-ckpt1600-val8192-eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cls4b-v5-val-sweep-ckpt4600
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 90.07
    f1_macro: 85.04
    f1_fail: 76.37
    f1_pass: 93.71
    precision_fail: 89.65
    recall_fail: 66.52
    precision_pass: 90.16
    recall_pass: 97.56
    majority_baseline: 75.88
    gap_vs_majority_pp: 14.19
    unparseable_count: 0
    total_samples: 9335
    n_truncated: 234
- exp_id: cls4b-v5-val-sweep-ckpt4200
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 89.06
    f1_macro: 83.07
    f1_fail: 73
    f1_pass: 93.1
    precision_fail: 90.3
    recall_fail: 61.3
    precision_pass: 88.8
    recall_pass: 97.9
- exp_id: cls4b-v5-val-sweep-ckpt4400
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cls8b-s42-ckpt1200-val8192
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cls4b-v5-val-sweep-ckpt4400-v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 89.96
    f1_macro: 84.94
    f1_fail: 76.25
    f1_pass: 93.64
    precision_fail: 88.84
    precision_pass: 90.21
    recall_fail: 66.79
    recall_pass: 97.33
    majority_baseline: 75.88
    gap_vs_majority_pp: 14.09
    n_instances: 9335
    n_truncated: 234
    n_unparseable: 0
- exp_id: cls8b-s42-ckpt1200-test8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 83.84
    f1_macro: 77.47
    f1_fail: 65.49
    f1_pass: 89.45
    precision_fail: 77.52
    recall_fail: 56.69
    precision_pass: 85.4
    recall_pass: 93.91
    majority_baseline: 72.96
    gap_vs_majority_pp: 10.89
    unparseable_count: 0
    total_samples: 9784
- exp_id: cls8b-s42-ckpt1400-test8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 85.47
    f1_macro: 78.9
    f1_fail: 67.13
    f1_pass: 90.67
    precision_fail: 86.43
    recall_fail: 54.88
    precision_pass: 85.27
    recall_pass: 96.81
    majority_baseline: 72.96
    gap_vs_majority_pp: 12.51
    unparseable_count: 0
    total_samples: 9784
- exp_id: cls8b-s42-ckpt1600-test8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 84.99
    f1_macro: 78.94
    f1_fail: 67.65
    f1_pass: 90.22
    precision_fail: 81.06
    recall_fail: 58.05
    precision_pass: 85.93
    recall_pass: 94.97
    majority_baseline: 72.96
    gap_vs_majority_pp: 12.03
    unparseable_count: 0
    total_samples: 9784
- exp_id: cls8b-s42-ckpt1200-val8192-v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cls8b-s42-ckpt1200-val8192-v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 87.76
    f1_macro: 81.25
    f1_fail: 70.2
    f1_pass: 92.3
    precision_fail: 85
    recall_fail: 59.8
    precision_pass: 88.3
    recall_pass: 96.7
    majority_baseline: 75.9
    gap_vs_majority: 11.9
    unparseable: 9
- exp_id: cls8b-s42-ckpt1600-val8192-v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 86.75
    f1_macro: 78.94
    f1_fail: 66.12
    f1_pass: 91.76
    precision_fail: 86.28
    precision_pass: 86.83
    recall_fail: 53.6
    recall_pass: 97.29
    majority_baseline: 75.88
    gap_vs_majority_pp: 10.87
    unparseable: 9
    total: 9335
- exp_id: cls8b-s42-ckpt800-test8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 83.53
    f1_macro: 78.97
    f1_fail: 69.17
    f1_pass: 88.77
    precision_fail: 70.07
    recall_fail: 68.29
    precision_pass: 88.36
    recall_pass: 89.18
    majority_baseline: 72.96
    gap_vs_majority_pp: 10.58
    unparseable_count: 0
    total_samples: 9784
- exp_id: cls8b-seed123-ckpt6600-val8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 87.23
    f1_macro: 79.02
    f1_fail: 65.9
    f1_pass: 92.14
    precision_fail: 92.6
    recall_fail: 51.15
    precision_pass: 86.4
    recall_pass: 98.7
    majority_baseline: 75.88
    gap_vs_majority_pp: 11.36
    unparseable_count: 9
    total_samples: 9335
- exp_id: cls4b-v5-ckpt4600-test-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 83.63
    f1_macro: 75.63
    f1_fail: 61.67
    f1_pass: 89.59
    precision_fail: 84.03
    recall_fail: 48.72
    precision_pass: 83.55
    recall_pass: 96.57
    majority_baseline: 72.96
    gap_vs_majority_pp: 10.67
    unparseable_count: 0
    total_samples: 9784
- exp_id: cls8b-seed123-ckpt6400-val8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 87.48
    f1_macro: 79.66
    f1_fail: 67.04
    f1_pass: 92.27
    precision_fail: 91.81
    recall_fail: 52.8
    precision_pass: 86.78
    recall_pass: 98.5
    majority_baseline: 75.88
    gap_vs_majority_pp: 11.6
    unparseable_count: 9
    total_samples: 9335
- exp_id: cls8b-seed123-ckpt6200-val8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 87.52
    f1_macro: 79.26
    f1_fail: 66.16
    f1_pass: 92.35
    precision_fail: 95.63
    recall_fail: 50.58
    precision_pass: 86.33
    recall_pass: 99.27
    majority_baseline: 75.88
    gap_vs_majority_pp: 11.64
    unparseable_count: 9
    total_samples: 9335
- exp_id: cls4b-v5-ckpt4400-test5120-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 83.24
    f1_macro: 74.44
    f1_fail: 59.45
    f1_pass: 89.44
    precision_fail: 85.98
    recall_fail: 45.43
    precision_pass: 82.78
    recall_pass: 97.25
    majority_baseline: 72.96
    gap_vs_majority_pp: 10.28
    unparseable_count: 0
    total_samples: 9784
- exp_id: cls8b-seed123-ckpt3000-test8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 85.6
    f1_macro: 78.38
    f1_fail: 65.89
    f1_pass: 90.87
    precision_fail: 91.65
    recall_fail: 51.44
    precision_pass: 84.52
    recall_pass: 98.26
    majority_baseline: 72.96
    gap_vs_majority_pp: 12.64
    unparseable_count: 0
    total_samples: 9784
- exp_id: cls8b-seed123-ckpt6633-val8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 87.1
    f1_macro: 78.79
    f1_fail: 65.52
    f1_pass: 92.07
    precision_fail: 92.26
    recall_fail: 50.8
    precision_pass: 86.31
    recall_pass: 98.64
    majority_baseline: 75.88
    gap_vs_majority_pp: 11.23
    unparseable_count: 9
    total_samples: 9335
- exp_id: cls8b-seed123-ckpt3000-test8192-eval-v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cls4b-seed123-ckpt800-test5120-eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cls4b-seed123-ckpt800-test5120-eval-v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 75.33
    f1_macro: 67.03
    f1_fail: 50.5
    f1_pass: 83.6
    precision_fail: 55.2
    recall_fail: 46.5
    precision_pass: 81.3
    recall_pass: 86
    majority_baseline: 73
    gap_vs_majority_pp: 2.4
    unparseable_count: 0
    total_samples: 9784
- exp_id: cls8b-seed123-ckpt6200-test8192-eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cls8b-seed123-ckpt6400-test8192-eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cls8b-s42-ckpt200-val8192-eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cls8b-seed123-ckpt6200-test-eval-v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 84.7
    f1_fail: 63.71
    f1_pass: 90.31
    f1_macro: 77.01
    precision_fail: 88.84
    precision_pass: 83.96
    recall_fail: 49.66
    recall_pass: 97.69
    n_instances: 9784
    n_cls_unparseable: 0
- exp_id: cls8b-seed123-ckpt6400-test-eval-v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 85.08
    f1_fail: 65.32
    f1_pass: 90.49
    f1_macro: 77.91
    precision_fail: 87.92
    precision_pass: 84.54
    recall_fail: 51.97
    recall_pass: 97.35
    n_instances: 9784
    n_cls_unparseable: 0
- exp_id: cls4b-v5-ckpt600-test5120-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 77.74
    f1_macro: 74.74
    f1_fail: 66.03
    f1_pass: 83.44
    precision_fail: 56.21
    recall_fail: 80.01
    majority_baseline: 72.96
    gap_vs_majority_pp: 4.78
    unparseable_count: 0
    total_samples: 9784
- exp_id: cls8b-seed123-ckpt6600-test-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 84.9
    f1_macro: 77.58
    pass_f1: 90.4
    fail_f1: 64.8
    pass_precision: 84.3
    pass_recall: 97.4
    fail_precision: 87.8
    fail_recall: 51.3
    n_samples: 9784
    n_pass: 7138
    n_fail: 2646
    majority_baseline: 73
    unparseable: 0
    confusion_matrix:
      fail_as_fail: 1357
      fail_as_pass: 1289
      pass_as_fail: 188
      pass_as_pass: 6950
- exp_id: cls8b-s42-ckpt200-test8192-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 70.07
    f1_macro: 68.18
    pass_f1: 75.9
    fail_f1: 60.4
    pass_precision: 91.8
    pass_recall: 64.7
    fail_precision: 47
    fail_recall: 84.5
    n_samples: 9784
    n_pass: 7138
    n_fail: 2646
    majority_baseline: 73
    unparseable: 0
    confusion_matrix:
      fail_as_fail: 2235
      fail_as_pass: 411
      pass_as_fail: 2517
      pass_as_pass: 4621
- exp_id: cls8b-s42-ckpt1000-test-seq2048-ablation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 82.83
    f1_macro: 76.88
    fail_precision: 72.2
    fail_recall: 59.3
    fail_f1: 65.2
    pass_precision: 85.9
    pass_recall: 91.5
    pass_f1: 88.6
    unparseable: 136
- exp_id: cls4b-v5-ckpt4000-test5120-eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cls8b-seed123-ckpt6633-test-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 84.89
    f1_macro: 77.56
    f1_fail: 64.7
    f1_pass: 90.4
    precision_fail: 87.8
    recall_fail: 51.2
    precision_pass: 84.3
    recall_pass: 97.4
    majority_baseline: 73
    gap_vs_majority_pp: 11.9
    total_samples: 9784
    unparseable_count: 0
- exp_id: cls8b-seed123-ckpt200-test-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 72.55
    f1_macro: 70.18
    pass_f1: 78.58
    fail_f1: 61.78
    pass_precision: 91.21
    pass_recall: 69.02
    fail_precision: 49.54
    fail_recall: 82.05
    n_samples: 9784
    n_pass: 7138
    n_fail: 2646
    majority_baseline: 72.96
    unparseable: 0
    confusion_matrix:
      tn: 2171
      fp: 475
      fn: 2211
      tp: 4927
- exp_id: cwm8b-ckpt400-test-eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cwm-rank32-ablation
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cwm-4b-rank32-ablation
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cwm-rank32-ablation-v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 87
    exact_match_rate: 83.4
    fail_f1: 87.1
    pass_f1: 86.9
    train_loss_final: 0.0152
    train_loss_avg: 0.2536
    eval_loss: 0.0688
    train_runtime_sec: 5003
    test_set_size: 1890
    vs_rank16_baseline: -0.51
    rank16_baseline_accuracy: 87.51
- exp_id: cwm-rank64-ablation
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cwm-4b-rank64-ablation
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: s42-extended-val-sweep
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cwm-rank32-alpha64-ablation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 87.04
    pass_f1: 86.79
    fail_f1: 87.27
    f1_macro: 87.03
    pass_precision: 91.8
    pass_recall: 82.3
    fail_precision: 82.9
    fail_recall: 92.1
    exact_match_rate: 84.55
    train_loss: 0.2069
    eval_loss: 0.0606
    n_instances: 1890
    vs_rank16_baseline: -0.47
    rank16_baseline_accuracy: 87.51
- exp_id: cls8b-s42-extended-val-sweep
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cls8b-s42-resume-val-sweep
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: s42-extended-val-sweep-v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cls8b-s42-resume-val-sweep-seq8192
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cls8b-s42-resume-val-sweep-seq4096
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cls8b-s42-resume-val-sweep-seq8192-v2
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: repo-level-cwm-8b-conda-v5
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: cls8b-s42-resume-val-sweep-gpu1
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cls8b-s42-resume-ckpt1000-test-mutation
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cls8b-s42-ckpt1000-test-mutation
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cls8b-s42-resume-ckpt3600-test
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: cls8b-s42-resume-ckpt3600-mutation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 84.4849
    overall_correct: 8266
    overall_total: 9784
    gold_accuracy: 96.2443
    gold_correct: 4459
    gold_total: 4633
    mutation_operator_swap_accuracy: 81.3822
    mutation_operator_swap_correct: 2732
    mutation_operator_swap_total: 3357
    mutation_off_by_one_accuracy: 86.8852
    mutation_off_by_one_correct: 159
    mutation_off_by_one_total: 183
    mutation_return_value_accuracy: 75.4448
    mutation_return_value_correct: 424
    mutation_return_value_total: 562
    mutation_boundary_removal_accuracy: 46.9018
    mutation_boundary_removal_correct: 492
    mutation_boundary_removal_total: 1049
- exp_id: cls8b-s42-ckpt3600-seq2048-ablation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 83.04
    f1_macro: 76.8
    unparseable: 136
    n_samples: 9784
    seq_length: 2048
- exp_id: repo-level-cwm-8b-conda-v6
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cwm8b-ckpt400-test-eval-v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cwm8b-ckpt400-test-eval-v3
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: cls8b-s42-resume-ckpt3600-test-v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 84.48
    f1_macro: 78.17
    fail_recall: 56.8
    pass_recall: 94.8
    n_samples: 9784
    note: reproduces v1 exactly
- exp_id: cls8b-seed123-ckpt3000-mutation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 85.6
    boundary_removal: 44.9
    operator_swap: 82.6
    return_value: 66.4
    off_by_one: 79.2
    gold: 99.6
    n_samples: 9784
- exp_id: cwm8b-ckpt400-test-eval-shard2
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: cls4b-ckpt4600-test-mutation-pr
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 83.63
    gold_acc: 98.25
    operator_swap_acc: 78.91
    return_value_acc: 67.97
    off_by_one_acc: 58.47
    boundary_removal_acc: 46.9
    n_instances: 9784
    note: off_by_one recall_fail=0 (all predicted pass); boundary_removal identical
      to 8B
- exp_id: cwm4b-s42-mutation-breakdown
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_accuracy: 58.04
    parseable_rate: 46.3
    parseable_only_accuracy: 42.9
    gold_parse_rate: 43.5
    gold_parseable_acc: 23.5
    operator_swap_parse_rate: 56.9
    operator_swap_parseable_acc: 63.1
    off_by_one_parse_rate: 4.4
    off_by_one_parseable_acc: 0
    return_value_parse_rate: 48.8
    return_value_parseable_acc: 27
    boundary_removal_parse_rate: 30.6
    boundary_removal_parseable_acc: 59.2
    n_instances: 9784
- exp_id: cwm8b-ckpt400-test-eval-shard3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cwm8b-ckpt400-test-eval-shard4
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: deepseek-cls-repo
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: deepseek-cwm-func
  name: ''
  status: DONE
  conclusion: success
  metrics:
    best_eval_loss: 0.04292
    train_time_seconds: 5215
    test_accuracy: 85.77
    test_f1_macro: 85.73
    test_precision_fail: 80.07
    test_precision_pass: 93.18
    test_recall_fail: 93.86
    test_recall_pass: 78.22
    test_unparseable_rate: 0
    test_n: 1890
- exp_id: deepseek-cls-func
  name: ''
  status: DONE
  conclusion: success
  metrics:
    best_eval_loss: 0.0701
    train_time_seconds: 5444
    test_accuracy: 86.93
    test_f1_macro: 86.92
    test_precision_fail: 86.42
    test_precision_pass: 87.41
    test_recall_fail: 86.51
    test_recall_pass: 87.32
    test_n: 1890
- exp_id: deepseek-cwm-func-s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    best_eval_loss: 0.0408
    train_time_seconds: 5244
    test_accuracy: 87.88
    test_f1_macro: 87.88
    test_precision_fail: 83.78
    test_precision_pass: 92.61
    test_recall_fail: 92.87
    test_recall_pass: 83.23
    test_unparseable_rate: 0
    test_n: 1890
- exp_id: deepseek-cwm-repo
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: re-repair-phase0
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    control_mean_sim: 0.82
    cls_diag_mean_sim: 0.818
    oracle_diag_mean_sim: 0.809
    random_diag_mean_sim: 0.719
    n_instances: 10
    n_conditions: 4
    samples_per_condition: 3
- exp_id: deepseek-cls-func-s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    best_eval_loss: 0.06753
    train_time_seconds: 5391
    test_accuracy: 86.77
    test_f1_macro: 86.77
    test_precision_fail: 84.99
    test_precision_pass: 88.56
    test_recall_fail: 88.16
    test_recall_pass: 85.48
    test_unparseable_rate: 0
    test_n: 1890
- exp_id: deepseek-traj-func
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_loss_epoch1: 0.0943
    eval_loss_epoch2: 0.0793
    eval_loss_epoch3: 0.0884
    best_eval_loss: 0.0793
    best_step: 1008
    best_epoch: 2
    train_loss: 0.1131
    train_runtime_sec: 2910.6
- exp_id: deepseek-traj-func-s123
  name: ''
  status: ANALYZING
  conclusion: ''
  metrics: {}
- exp_id: deepseek-traj-func-v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    best_eval_loss: 0.0796
    best_step: 504
    test_accuracy: 0.8324
    majority_baseline: 0.5359
    train_loss: 0.0857
    train_runtime_seconds: 3069.6
- exp_id: deepseek-traj-func-v2-s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    best_eval_loss: 0.077
    best_step: 504
    test_accuracy: 0.8508
    majority_baseline: 0.5359
    train_loss: 0.0842
    train_runtime_seconds: 3021
    per_test_consistency: 0.782
- exp_id: deepseek-traj-func-v2-fixed
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: deepseek-traj-func-v2-s123-fixed
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: deepseek-traj-repo
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: deepseek-traj-repo-s123
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}

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
  "promptId": "f8c95270-2cda-4875-ab0f-f4534b23aa9f",
  "type": "user",
  "uuid": "60eb2f96-f1e8-4748-9d1d-9c417fd8a579",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T15:13:32.248Z_

```json
{
  "parentUuid": "60eb2f96-f1e8-4748-9d1d-9c417fd8a579",
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
  "uuid": "12a1169d-51d4-4fae-971d-019bc84744c2",
  "timestamp": "2026-05-16T15:13:32.248Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T15:13:32.248Z_

```json
{
  "parentUuid": "12a1169d-51d4-4fae-971d-019bc84744c2",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "a85bece9-e2fb-4119-8101-e8400d5d2682",
  "timestamp": "2026-05-16T15:13:32.248Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T15:13:32.248Z_

```json
{
  "parentUuid": "a85bece9-e2fb-4119-8101-e8400d5d2682",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5a85c94e-f0f6-461f-b61c-63ec5e753ef5",
  "timestamp": "2026-05-16T15:13:32.248Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：部分跨模型验证——DeepSeek repo CLS 可用但弱于 Qwen，CWM 部分可解析使得差距缩小；C1 需 model-dependent caveat，C2 仅 Qwen 内验证 核心假设：['DeepSeek repo CWM 部分可解析（unparseable 15–40%），parsea…",
  "leafUuid": "5a85c94e-f0f6-461f-b61c-63ec5e753ef5",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-model verification with DeepSeek—median tier narrative",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00"
}
```

---

### Assistant

_source line 9 · 2026-05-16T15:13:38.372Z_

Let我先仔细分析所有 planned 和 RUNNING/PREPARING 状态的实验，以及需要基于 median 档位展开的预测。

让我先检查当前项目中是否有更多相关文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a85c94e-f0f6-461f-b61c-63ec5e753ef5",
  "isSidechain": false,
  "requestId": "req_011Cb6TvDizReHpgUmWCYvbr",
  "type": "assistant",
  "uuid": "55a80957-411a-44ce-a46c-6f3aa377c470",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDAdJMM5PmtztMf9bVVmRb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 32171,
      "cache_read_input_tokens": 11447,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 254,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 32171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32171
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

_source line 10 · 2026-05-16T15:13:41.570Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01CTFzPJX9aQ2gvkQERJSusD`</summary>

```json
{
  "description": "Explore experiment plan files",
  "subagent_type": "Explore",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_16, find all files related to experiment plans, predictions, tier definitions, and any YAML/markdown files that describe the \"median\" tier or experiment status. Search for files matching patterns like: experiment_plan*, prediction*, tier*, median*, imagined*, and any .yaml or .md files in the project root or common subdirectories. Quick search."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55a80957-411a-44ce-a46c-6f3aa377c470",
  "isSidechain": false,
  "requestId": "req_011Cb6TvDizReHpgUmWCYvbr",
  "type": "assistant",
  "uuid": "82f7fd40-e9a2-418c-a307-8c06e10df773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDAdJMM5PmtztMf9bVVmRb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 32171,
      "cache_read_input_tokens": 11447,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 254,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 32171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32171
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

_source line 11 · 2026-05-16T15:14:24.051Z_

<details><summary>↩ Tool result · `toolu_01CTFzPJX9aQ2gvkQERJSusD`</summary>

```text
Perfect! Now I have enough information to provide a comprehensive summary. Let me compile the findings:

## Summary of Files Found

I've completed a comprehensive search of `/home/ubuntu/.agent-ml-research-idea_gen_0509_16` for experiment plans, predictions, tier definitions, and YAML/markdown files. Here are the key findings:

### **Tier Structure (Median/Best/Worst)**

The project uses a three-tier system for dream reports:
- **Median tier**: Realistic, balanced narrative of results with caveats
- **Best tier**: Most optimistic interpretation
- **Worst tier**: Most pessimistic interpretation

Each tier has subdirectories containing:
- `imagined_experiments.yaml` — defines expected experiment results and narratives
- `experiment_data.json` — structured experiment data with results and analysis
- `logs/` directory — execution logs for phases 1, 2, and review

Dream reports with tier structure:
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260516T073712/{median,best,worst}/`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/{median,best,worst}/`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T214810/{median,best,worst}/`

### **Key Registries & YAML Files**

1. **Dream Registry**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/dream_registry.yaml`
   - Tracks all dream runs (imagining, writing, review stages)
   - Metadata: status, focus, stages_completed, error messages

2. **Experiment Registry**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/registry.yaml` (272.8KB)
   - Contains baseline and experiments with specs, results, metrics
   - Examples: `mvp-a-oracle-sim`, `mvp-b-data-prep`, `mvp-b-train`

3. **Global Approvals**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/global/approvals.yaml`
   - Submission and experiment approval records
   - Risk assessment and approval metadata

4. **Global Report**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/global/report.md`
   - Handover status, running experiments, next steps
   - Metrics trends (per_test_consistency, test_accuracy)

5. **Ideas Registry**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/idea_generator/ideas.yaml`

### **Experiment Plans & Predictions**

1. **Experiment Plan Lock File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/experiment_plan.lock`

2. **Prediction-Related Files**:
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/matched-seed-8b-predictions_*.json` (multiple status files)
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/data/cls_seed42_predictions_ref.txt`
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/data/cwm_seed42_predictions_ref.txt`

3. **Experiment Design**: 
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/re_repair_experiment_design.md`
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/report/re_repair_experiment_design.md`

### **Imagined Experiments YAML Files**

Located in tier directories under dream reports:
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260516T073712/median/imagined_experiments.yaml` (1234 lines)
  
Contains 20+ imagined experiments including:
- CWM Generation Baseline (4B Function-Level)
- Multi-Seed Core Validation (5-seed, 4B)
- Model Size Scaling (8B, 3-seed)
- Oracle F2P-Stratified Analysis
- Per-Test Precision/Recall Analysis
- SWE-bench PerTest Dataset Construction
- Repo-Level Training (CLS + CWM)
- DeepSeek Function-Level CLS/CWM variants
- Error Complementarity Analysis
- TOST Equivalence Testing (Claim 2 evidence)

### **Phase Logs**

Located in each dream report's logs/:
- `phase1_attempt0.log` — Phase 1 execution
- `phase2_median_attempt0.log`, `phase2_best_attempt0.log`, `phase2_worst_attempt0.log` — Phase 2 by tier
- `paper_agent_median.log`, `review_median.log` — Writing and review stage logs

### **Additional Markdown Files**

- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/AGENTS.md` — output style guidelines
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/IDEA_BRIEF.md`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/ROADMAP.md`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/re_repair_phase0_results.md` — Phase 0 experimental results

### **Key Data Structure**

The `imagined_experiments.yaml` file defines a comprehensive experimental plan with:
- `tier`: The narrative tier (e.g., "median")
- `narrative_guidance`: Textual description of the tier's interpretation
- `imagined_experiments`: Array of 20+ experiments, each containing:
  - `name`, `plan_id`, `description`
  - `expected_results`: quantitative predictions
  - `result_rationale`: explanation of why results would look this way
  - `tables`: expected tables with columns and rows
  - `figures_description`: expected visualizations
  - `analysis`: interpretation and impact on claims

This enables the "imagined" narrative of three possible futures before running actual experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82f7fd40-e9a2-418c-a307-8c06e10df773",
  "isSidechain": false,
  "promptId": "f8c95270-2cda-4875-ab0f-f4534b23aa9f",
  "type": "user",
  "uuid": "1bf9dbbc-9ee0-49cc-88c0-abda39c06b06",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_16, find all files related to experiment plans, predictions, tier definitions, and any YAML/markdown files that describe the \"median\" tier or experiment status. Search for files matching patterns like: experiment_plan*, prediction*, tier*, median*, imagined*, and any .yaml or .md files in the project root or common subdirectories. Quick search.",
    "agentId": "af8101330e3de32f7",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have enough information to provide a comprehensive summary. Let me compile the findings:\n\n## Summary of Files Found\n\nI've completed a comprehensive search of `/home/ubuntu/.agent-ml-research-idea_gen_0509_16` for experiment plans, predictions, tier definitions, and YAML/markdown files. Here are the key findings:\n\n### **Tier Structure (Median/Best/Worst)**\n\nThe project uses a three-tier system for dream reports:\n- **Median tier**: Realistic, balanced narrative of results with caveats\n- **Best tier**: Most optimistic interpretation\n- **Worst tier**: Most pessimistic interpretation\n\nEach tier has subdirectories containing:\n- `imagined_experiments.yaml` — defines expected experiment results and narratives\n- `experiment_data.json` — structured experiment data with results and analysis\n- `logs/` directory — execution logs for phases 1, 2, and review\n\nDream reports with tier structure:\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260516T073712/{median,best,worst}/`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/{median,best,worst}/`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T214810/{median,best,worst}/`\n\n### **Key Registries & YAML Files**\n\n1. **Dream Registry**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/dream_registry.yaml`\n   - Tracks all dream runs (imagining, writing, review stages)\n   - Metadata: status, focus, stages_completed, error messages\n\n2. **Experiment Registry**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/registry.yaml` (272.8KB)\n   - Contains baseline and experiments with specs, results, metrics\n   - Examples: `mvp-a-oracle-sim`, `mvp-b-data-prep`, `mvp-b-train`\n\n3. **Global Approvals**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/global/approvals.yaml`\n   - Submission and experiment approval records\n   - Risk assessment and approval metadata\n\n4. **Global Report**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/global/report.md`\n   - Handover status, running experiments, next steps\n   - Metrics trends (per_test_consistency, test_accuracy)\n\n5. **Ideas Registry**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/idea_generator/ideas.yaml`\n\n### **Experiment Plans & Predictions**\n\n1. **Experiment Plan Lock File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/experiment_plan.lock`\n\n2. **Prediction-Related Files**:\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/matched-seed-8b-predictions_*.json` (multiple status files)\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/data/cls_seed42_predictions_ref.txt`\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/data/cwm_seed42_predictions_ref.txt`\n\n3. **Experiment Design**: \n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/re_repair_experiment_design.md`\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/report/re_repair_experiment_design.md`\n\n### **Imagined Experiments YAML Files**\n\nLocated in tier directories under dream reports:\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260516T073712/median/imagined_experiments.yaml` (1234 lines)\n  \nContains 20+ imagined experiments including:\n- CWM Generation Baseline (4B Function-Level)\n- Multi-Seed Core Validation (5-seed, 4B)\n- Model Size Scaling (8B, 3-seed)\n- Oracle F2P-Stratified Analysis\n- Per-Test Precision/Recall Analysis\n- SWE-bench PerTest Dataset Construction\n- Repo-Level Training (CLS + CWM)\n- DeepSeek Function-Level CLS/CWM variants\n- Error Complementarity Analysis\n- TOST Equivalence Testing (Claim 2 evidence)\n\n### **Phase Logs**\n\nLocated in each dream report's logs/:\n- `phase1_attempt0.log` — Phase 1 execution\n- `phase2_median_attempt0.log`, `phase2_best_attempt0.log`, `phase2_worst_attempt0.log` — Phase 2 by tier\n- `paper_agent_median.log`, `review_median.log` — Writing and review stage logs\n\n### **Additional Markdown Files**\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/AGENTS.md` — output style guidelines\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/IDEA_BRIEF.md`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/ROADMAP.md`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/re_repair_phase0_results.md` — Phase 0 experimental results\n\n### **Key Data Structure**\n\nThe `imagined_experiments.yaml` file defines a comprehensive experimental plan with:\n- `tier`: The narrative tier (e.g., \"median\")\n- `narrative_guidance`: Textual description of the tier's interpretation\n- `imagined_experiments`: Array of 20+ experiments, each containing:\n  - `name`, `plan_id`, `description`\n  - `expected_results`: quantitative predictions\n  - `result_rationale`: explanation of why results would look this way\n  - `tables`: expected tables with columns and rows\n  - `figures_description`: expected visualizations\n  - `analysis`: interpretation and impact on claims\n\nThis enables the \"imagined\" narrative of three possible futures before running actual experiments."
      }
    ],
    "totalDurationMs": 42474,
    "totalTokens": 64455,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1934,
      "cache_read_input_tokens": 60795,
      "output_tokens": 1722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1934
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 1722,
          "cache_read_input_tokens": 60795,
          "cache_creation_input_tokens": 1934,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1934,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 9,
      "searchCount": 1,
      "bashCount": 12,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "82f7fd40-e9a2-418c-a307-8c06e10df773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T15:14:26.948Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SStwKaGUvuy9226VgrSbRw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260516T073712/median/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bf9dbbc-9ee0-49cc-88c0-abda39c06b06",
  "isSidechain": false,
  "requestId": "req_011Cb6Tz35e3ezLVMFzPVquv",
  "type": "assistant",
  "uuid": "e3227f44-7da9-4140-a736-681f757df56a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5uVePbo6iEWjczdmU3bar",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1984,
      "cache_read_input_tokens": 43618,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1984,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 43618,
          "cache_creation_input_tokens": 1984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1984
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

_source line 13 · 2026-05-16T15:14:27.270Z_

<details><summary>↩ Tool result · `toolu_01SStwKaGUvuy9226VgrSbRw`</summary>

```text
1	tier: median
2	narrative_guidance: 'Median档叙事核心转变：Claim1从"CLS>CWM"降级为"CLS works where CWM fails"。
3	  Function-level 4B null result (0pp gap, p=0.72) + 8B 2.43pp modest gap被接受但不视为exciting。
4	  Repo-level CLS可用(82-85% accuracy)但CWM catastrophically fail(50-93% unparseable)，
5	  部分reviewer质疑CWM failure是implementation问题(max_new_tokens设置、output format设计) 而非formulation固有限制，要求honest
6	  discussion。 重心转向Claim2+3：per-test equivalence(TOST p=0.007, ±2pp)作为methodological
7	  contribution， oracle characterization(T≥2 advantage集中在31.3% instances)作为practical
8	  decision framework。 DeepSeek结果mixed——function-level gap方向不一致(CWM在DeepSeek上可能略优)，
9	  repo-level CLS可用但无new insight。 Error complementarity(oracle ensemble 90.63%)成为supplementary
10	  selling point。 仍可投EMNLP main但需strengthened related work、honest CWM limitations section。
11	
12	  '
13	imagined_experiments:
14	- name: CWM Generation Baseline (4B Function-Level)
15	  plan_id: cwm-baseline
16	  description: Qwen3-4B LoRA CWM vs CLS on function-level data, seed42
17	  expected_results:
18	    cls_accuracy: 87.51
19	    cls_pass_f1: 87.1
20	    cls_fail_f1: 87.9
21	    cwm_accuracy: 87.51
22	    cwm_pass_f1: 87.31
23	    cwm_fail_f1: 87.71
24	    accuracy_gap_pp: 0.0
25	    cwm_exact_match_rate: 84.02
26	    cwm_unparseable: 0
27	  result_rationale: 'Function-level execution output短(通常<50 tokens)，CWM不触发token-budget
28	    exhaustion 或string-value prediction failure modes。4B模型容量足以精确预测短输出。 两种formulation在此complexity
29	    level达到identical accuracy(87.51%)。 Exact match rate 84.02% < accuracy 87.51%说明CWM有部分output不完全匹配但
30	    通过pass/fail判断逻辑仍然correct——这预示repo-level上output matching会更困难。 Unparseable=0因为function-level输出格式统一简单。
31	    Median tier下此null result是叙事基础：排除"CLS trivially easier"的concern， 建立complexity-dependent
32	    advantage的前提。
33	
34	    '
35	  tables:
36	  - name: 'Table: Function-Level 4B CLS vs CWM (seed42)'
37	    columns:
38	    - Formulation
39	    - Accuracy
40	    - Pass F1
41	    - Fail F1
42	    - Exact Match
43	    - Unparseable%
44	    rows:
45	    - - CLS
46	      - 87.51
47	      - 87.1
48	      - 87.9
49	      - N/A
50	      - 0
51	    - - CWM
52	      - 87.51
53	      - 87.31
54	      - 87.71
55	      - 84.02
56	      - 0
57	    - - Δ (CLS−CWM)
58	      - 0.0
59	      - −0.21
60	      - 0.19
61	      - —
62	      - 0
63	  figures_description:
64	  - Per-class F1 bar chart, CLS与CWM几乎完全重叠
65	  analysis: 'Null result confirmed. CWM exact_match (84.02%) < accuracy (87.51%)的gap(3.49pp)
66	    暗示CWM在部分case上output不精确匹配但仍被判为correct—— repo-level上这个gap会急剧扩大导致catastrophic failure。
67	
68	    '
69	- name: Multi-Seed Core Validation (5-seed, 4B)
70	  plan_id: multi-seed-core
71	  description: CLS 5-seed {42,123,456,789,0} + CWM 5-seed统计
72	  expected_results:
73	    cls_seeds:
74	      s42:
75	        accuracy: 87.83
76	        pass_f1: 88.06
77	        fail_f1: 87.59
78	      s123:
79	        accuracy: 89.52
80	        pass_f1: 89.64
81	        fail_f1: 89.4
82	      s456:
83	        accuracy: 87.88
84	        pass_f1: 87.53
85	        fail_f1: 88.21
86	      s789:
87	        accuracy: 89.0
88	        pass_f1: 88.9
89	        fail_f1: 89.1
90	      s0:
91	        accuracy: 87.94
92	        pass_f1: 87.79
93	        fail_f1: 88.08
94	    cls_mean_accuracy: 88.43
95	    cls_std_accuracy: 0.76
96	    cwm_seeds:
97	      s42:
98	        accuracy: 87.51
99	        pass_f1: 87.31
100	        fail_f1: 87.71
101	      s123:
102	        accuracy: 87.2
103	        pass_f1: 86.95
104	        fail_f1: 87.44
105	      s456:
106	        accuracy: 86.98
107	        pass_f1: 86.66
108	        fail_f1: 87.29
109	      s789:
110	        accuracy: 86.67
111	        pass_f1: 86.74
112	        fail_f1: 86.6
113	      s0:
114	        accuracy: 87.57
115	        pass_f1: 87.18
116	        fail_f1: 87.93
117	    cwm_mean_accuracy: 87.19
118	    cwm_std_accuracy: 0.36
119	    mean_gap_pp: 1.24
120	    paired_t_p: ~0.06
121	    significant_at_005: false
122	  result_rationale: 'CLS 5-seed mean 88.43 vs CWM 87.19, gap 1.24pp。Paired t-test
123	    p≈0.06，α=0.05下不显著。 CLS variance (std 0.76) > CWM (std 0.36)：CLS对LoRA初始化更敏感，因为binary
124	    classification 的decision boundary位置对seed更敏感；CWM的generation target更deterministic，
125	    不同seed主要影响generation fluency而非correctness。 Seed123是CLS的outlier high(89.52)和CWM的near-mean(87.20)，贡献了最大pair
126	    gap。 Median tier：trend存在但不conclusive，这是4B function-level的inherent limitation——
127	    task太简单，两种formulation的capacity均已饱和。
128	
129	    '
130	  tables:
131	  - name: 'Table: 4B 5-Seed CLS vs CWM'
132	    columns:
133	    - Seed
134	    - CLS Acc
135	    - CWM Acc
136	    - Gap (pp)
137	    rows:
138	    - - 42
139	      - 87.83
140	      - 87.51
141	      - 0.32
142	    - - 123
143	      - 89.52
144	      - 87.2
145	      - 2.32
146	    - - 456
147	      - 87.88
148	      - 86.98
149	      - 0.9
150	    - - 789
151	      - 89.0
152	      - 86.67
153	      - 2.33
154	    - - 0
155	      - 87.94
156	      - 87.57
157	      - 0.37
158	    - - Mean±Std
159	      - 88.43±0.76
160	      - 87.19±0.36
161	      - '+1.24'
162	  figures_description:
163	  - 5-seed accuracy dot plot with mean ± std bars, CLS蓝色、CWM橙色
164	  analysis: 'p≈0.06处于borderline。Paper报告为"directional trend (p=0.06) at 4B,  becomes
165	    significant at 8B"，building scaling narrative。
166	
167	    '
168	- name: Trace-then-Judge Ablation
169	  plan_id: trace-then-judge
170	  description: 'Chain-of-thought style: generate reasoning trace → pass/fail'
171	  expected_results:
172	    training_status: failed
173	    reason: output format instability, training diverged
174	  result_rationale: '4B LoRA同时学习生成reasoning trace和predict pass/fail，两个objective竞争有限capacity。
175	    Trace format不稳定导致pass/fail token被reasoning token侵蚀，accuracy崩溃。 这不是fundamental
176	    impossibility而是engineering/capacity问题——更大模型或更精细的 format control可能解决。Median tier下dropped
177	    from paper，brief mention in limitations。
178	
179	    '
180	  tables: []
181	  figures_description: []
182	  analysis: '不影响core claims。如果成功，它会ablate away"CLS优势来自skipping reasoning"的concern；
183	    failure意味着这个concern无法directly addressed，但8B scaling evidence间接addresses。
184	
185	    '
186	- name: Trajectory-Level Fine-tuned Baseline
187	  plan_id: traj-level-finetuned
188	  description: 4B LoRA trained on resolved/unresolved prediction (5-seed)
189	  expected_results:
190	    seed42:
191	      accuracy: 85.66
192	      unresolved_f1: 87.5
193	      resolved_f1: 83.18
194	      consistency: 79.94
195	    seed123:
196	      accuracy: 85.47
197	      unresolved_f1: 87.0
198	      resolved_f1: 83.52
199	      consistency: 78.59
200	    seed456:
201	      accuracy: 87.4
202	      unresolved_f1: 88.7
203	      resolved_f1: 85.8
204	      consistency: 78.8
205	    seed789:
206	      accuracy: 87.31
207	      unresolved_f1: 88.27
208	      resolved_f1: 86.17
209	      consistency: 76.74
210	    seed0:
211	      accuracy: 85.66
212	      unresolved_f1: 87.37
213	      resolved_f1: 83.41
214	      consistency: 79.55
215	    mean_accuracy: 86.3
216	    std_accuracy: 0.93
217	  result_rationale: 'Trajectory-level mean accuracy 86.30% vs per-test CLS 88.43%，gap
218	    2.13pp。 这个gap的主要来源：(1) trajectory-level每个problem只产生1个训练样本 vs per-test产生T个， effective
219	    training data量更少；(2) resolved需要ALL tests pass——这种conjunctive logic 比per-test的individual判断更难学。Consistency
220	    rate ~78%说明同一problem内per-test predictions 有~22%不一致，暗示model在同一problem内对不同tests的判断受shared
221	    context bias影响。 Median tier下此gap supports Claim 2的"per-test不损失accuracy"叙事，但gap部分
222	    来自training data confound，需honest报告。
223	
224	    '
225	  tables:
226	  - name: 'Table: Trajectory-Level 5-Seed Results'
227	    columns:
228	    - Seed
229	    - Accuracy
230	    - Resolved F1
231	    - Unresolved F1
232	    - Consistency%
233	    rows:
234	    - - 42
235	      - 85.66
236	      - 83.18
237	      - 87.5
238	      - 79.94
239	    - - 123
240	      - 85.47
241	      - 83.52
242	      - 87.0
243	      - 78.59
244	    - - 456
245	      - 87.4
246	      - 85.8
247	      - 88.7
248	      - 78.8
249	    - - 789
250	      - 87.31
251	      - 86.17
252	      - 88.27
253	      - 76.74
254	    - - 0
255	      - 85.66
256	      - 83.41
257	      - 87.37
258	      - 79.55
259	    - - Mean±Std
260	      - 86.30±0.93
261	      - 84.42±1.36
262	      - 87.77±0.68
263	      - 78.72±1.25
264	  figures_description: []
265	  analysis: 'Per-test ≥ trajectory at variant-level，TOST equivalence test (下述) 更rigorously
266	    quantifies。
267	
268	    '
269	- name: Model Size Scaling (8B, 3-seed)
270	  plan_id: model-size-scaling
271	  description: CLS vs CWM at 8B scale, seeds {42, 123, 456}
272	  expected_results:
273	    cls8b_seeds:
274	      s42:
275	        accuracy: 90.48
276	        pass_f1: 90.86
277	        fail_f1: 90.06
278	      s123:
279	        accuracy: 89.4
280	        pass_f1: 89.54
281	        fail_f1: 89.19
282	      s456:
283	        accuracy: 88.31
284	        pass_f1: 88.2
285	        fail_f1: 88.41
286	    cls8b_mean_accuracy: 89.4
287	    cls8b_std: 1.09
288	    cwm8b_seeds:
289	      s42:
290	        accuracy: 87.67
291	        pass_f1: 87.57
292	        fail_f1: 87.77
293	      s123:
294	        accuracy: 86.98
295	        pass_f1: 86.83
296	        fail_f1: 87.13
297	      s456:
298	        accuracy: 86.24
299	        pass_f1: 85.96
300	        fail_f1: 86.51
301	    cwm8b_mean_accuracy: 86.96
302	    cwm8b_std: 0.72
303	    mean_gap_pp: 2.43
304	    per_seed_gaps:
305	      s42: 2.81
306	      s123: 2.42
307	      s456: 2.07
308	    cls_4b_to_8b_gain_pp: 0.97
309	    cwm_4b_to_8b_gain_pp: -0.23
310	  result_rationale: '8B CLS (89.40) vs CWM (86.96) gap扩大到2.43pp，所有3个seed方向一致(2.07-2.81pp)。
311	    关键asymmetry：CLS从4B→8B提升0.97pp但CWM下降0.23pp。 CWM在8B未获益的原因：function-level generation的bottleneck在exact
312	    string matching， 不是semantic understanding。额外的8B capacity没有reduce string matching
313	    error—— 模型更好地"理解"了代码但仍然在output format上犯同样的errors。 CLS则从extra capacity中获益：binary
314	    classification的decision boundary在高维space中 变得更smooth，reducing borderline case errors。
315	    Median tier：2.43pp被接受为real but modest。Reviewer说"interesting but not dramatic"。
316	    结合repo-level的catastrophic CWM failure讲故事：function-level hints at差异， repo-level放大为qualitative
317	    failure。
318	
319	    '
320	  tables:
321	  - name: 'Table: 8B 3-Seed Scaling'
322	    columns:
323	    - Size
324	    - CLS Mean Acc
325	    - CWM Mean Acc
326	    - Gap (pp)
327	    rows:
328	    - - 4B (5-seed)
329	      - 88.43
330	      - 87.19
331	      - 1.24
332	    - - 8B (seed42)
333	      - 90.48
334	      - 87.67
335	      - 2.81
336	    - - 8B (seed123)
337	      - 89.4
338	      - 86.98
339	      - 2.42
340	    - - 8B (seed456)
341	      - 88.31
342	      - 86.24
343	      - 2.07
344	    - - 8B (3-seed mean)
345	      - 89.4
346	      - 86.96
347	      - 2.43
348	  figures_description:
349	  - 'Scaling plot: x=model size, y=accuracy, CLS和CWM两条线, 8B处diverge'
350	  - Per-seed gap bar chart, 3 bars all positive (2.07-2.81)
351	  analysis: '8B gap consistent across seeds is the function-level strongest evidence
352	    for Claim 1。 但2.43pp在absolute terms仍modest。Paper frame为"scaling direction"而非"large
353	    effect"。
354	
355	    '
356	- name: Diagnostic Re-Repair (Downstream Proof-of-Concept)
357	  plan_id: diagnostic-rerepair
358	  description: Per-test failure predictions用于guide SWE-agent re-repair on 200 instances
359	  expected_results:
360	    n_instances_evaluated: 120
361	    baseline_resolve_rate_pct: 24.2
362	    with_pertest_resolve_rate_pct: 28.3
363	    improvement_pp: 4.1
364	    p_value_mcnemar: 0.11
365	    significant_at_005: false
366	    instances_diagnostic_helped: 14
367	    instances_diagnostic_hurt: 9
368	    net_helped: 5
369	    avg_repair_attempts_baseline: 3.2
370	    avg_repair_attempts_diagnostic: 2.8
371	  result_rationale: 'Median tier下re-repair受三重限制：(1) 资源不足仅完成120/200 instances； (2)
372	    per-test verifier error rate ~12.5%意味着约1/8的diagnostic信号是错误的， misleading repair
373	    agent在错误方向搜索；(3) SWE-bench instances 68.7% T=1， 这些case per-test info退化为trajectory-level，不提供额外guidance。
374	    4.1pp improvement方向正确，repair attempts减少(3.2→2.8)说明diagnostic确实 narrow了search space。但p=0.11在120
375	    samples下不显著(power analysis显示需~400 instances)。 Net helped仅5(14-9)，说明diagnostic
376	    precision不够——错误诊断导致9个case regression。 Median tier将此relegated to appendix/future
377	    work，不作为main claim。
378	
379	    '
380	  tables:
381	  - name: 'Table (Appendix): Re-Repair Pilot Results'
382	    columns:
383	    - Condition
384	    - Resolve Rate
385	    - Avg Attempts
386	    - N
387	    rows:
388	    - - Baseline (no per-test)
389	      - 24.2%
390	      - 3.2
391	      - 120
392	    - - With per-test diagnostic
393	      - 28.3%
394	      - 2.8
395	      - 120
396	    - - Δ
397	      - +4.1pp (p=0.11)
398	      - −0.4
399	      - ''
400	  figures_description:
401	  - 'Paired comparison: helped(14) vs hurt(9) vs neutral(97) breakdown'
402	  analysis: 'Directional but non-significant。Paper frame: "preliminary evidence for
403	    diagnostic utility, limited by verifier accuracy and sample size; full evaluation
404	    left to future work."
405	
406	    '
407	- name: Per-Test Precision/Recall Analysis
408	  plan_id: per-test-precision-recall
409	  description: Per-test failure prediction quality on full function-level test set
410	  expected_results:
411	    accuracy: 87.51
412	    fail_precision: 82.75
413	    fail_recall: 93.64
414	    fail_f1: 87.86
415	    pass_precision: 93.24
416	    pass_recall: 81.8
417	    pass_f1: 87.15
418	    FP_count: 58
419	    FN_count: 178
420	    FP_FN_ratio: 0.326
421	    best_mutation: return_value (97.26%)
422	    worst_mutation: off_by_one (82.56%)
423	    bucket_6_10_acc: 96.3
424	    bucket_11plus_acc: 87.12
425	  result_rationale: '模型显著biased toward predicting fail：fail_recall(93.64%) >> pass_recall(81.80%)。
426	    这是因为training data中mutation几乎都导致fail，模型学到了conservative prior。 FP:FN = 58:178 →
427	    75.4% of errors are false negatives(miss actual fails)。 这quantifies CLS的characteristic
428	    failure mode："miss bugs"而非"false alarms"。 Mutation类型分析：return_value最容易(97.26%)因为return值变化导致output大幅改变；
429	    off_by_one最难(82.56%)因为边界条件变化subtle，模型需要precise numerical reasoning。 Bucket analysis：6-10
430	    tests的problems accuracy最高(96.3%)因为multiple tests 提供redundant signal；11+ tests降至87.12%因为input
431	    length增加导致attention稀释。
432	
433	    '
434	  tables:
435	  - name: 'Table: Per-Test Diagnostic Quality'
436	    columns:
437	    - Class
438	    - Precision
439	    - Recall
440	    - F1
441	    rows:
442	    - - Fail (bug detected)
443	      - 82.75
444	      - 93.64
445	      - 87.86
446	    - - Pass (correct code)
447	      - 93.24
448	      - 81.8
449	      - 87.15
450	  - name: 'Table: Accuracy by Mutation Type'
451	    columns:
452	    - Mutation
453	    - Accuracy
454	    rows:
455	    - - return_value
456	      - 97.26%
457	    - - variable_swap
458	      - ~94%
459	    - - operator_swap
460	      - ~88%
461	    - - off_by_one
462	      - 82.56%
463	  figures_description:
464	  - Confusion matrix heatmap
465	  - Accuracy by mutation type + test count bucket grouped bar chart
466	  analysis: 'Error asymmetry (75% FN) 对downstream re-repair的影响：diagnostic signal会
467	    under-report failures，导致repair agent可能miss真正的bug。 这与CWM的complementary failure
468	    mode(83% false alarms)形成对比，支持oracle ensemble叙事。
469	
470	    '
471	- name: Oracle F2P-Stratified Analysis
472	  plan_id: oracle-f2p-stratified
473	  description: Per-test advantage breakdown by FAIL_TO_PASS test count
474	  expected_results:
475	    T1_pct: 68.7
476	    T1_block_adv: -0.09
477	    T2_pct: 19.1
478	    T2_block_adv: 31.69
479	    T3_5_pct: 7.1
480	    T3_5_block_adv: 40.74
481	    T6plus_pct: 5.1
482	    T6plus_block_adv: 40.06
483	    overall_block_adv: 10.93
484	    T2_contribution_pct: 55.3
485	  result_rationale: 'T=1时per-test ≡ trajectory-level（只有一个fail test），advantage仅来自prediction
486	    accuracy 微小差异（-0.09pp，essentially zero）。T=2时per-test advantage跳到31.69pp(block
487	    model)： 原因是trajectory-level把两个tests的pass/fail合并为一个binary判断，丢失了which test failed的信息；
488	    per-test分别预测，在一个test correct另一个wrong时仍能partial credit。 T≥3的advantage plateau在~40pp因为边际tests的marginal
489	    information增量递减。 T2贡献55.3%的overall advantage因为它是最大的multi-test bucket(19.1%)且advantage显著。
490	    Key insight for median tier：SWE-bench Verified 68.7%是T=1，限制了per-test的 population-level
491	    impact。但targeting T≥2 subset (31.3%)时per-test显著优于trajectory。
492	
493	    '
494	  tables:
495	  - name: 'Table: Oracle Per-Test Advantage by F2P Count'
496	    columns:
497	    - T
498	    - '% Instances'
499	    - Block Adv (pp)
500	    - Contribution to Overall
501	    rows:
502	    - - T=1
503	      - 68.7
504	      - -0.09
505	      - −0.6%
506	    - - T=2
507	      - 19.1
508	      - 31.69
509	      - 55.3%
510	    - - T=3−5
511	      - 7.1
512	      - 40.74
513	      - 26.4%
514	    - - T≥6
515	      - 5.1
516	      - 40.06
517	      - 18.7%
518	    - - Overall
519	      - 100
520	      - 10.93
521	      - 100%
522	  figures_description:
523	  - 'Stacked bar: per-test advantage by T bucket with instance % overlay'
524	  - SWE-bench F2P count distribution histogram
525	  analysis: 'Claim 3的primary evidence。Actionable finding：deploy per-test only when
526	    T≥2。 This characterization is the paper''s strongest unique contribution in median
527	    tier。
528	
529	    '
530	- name: Oracle Total (F2P+P2P) Validation
531	  plan_id: oracle-total-validated
532	  description: When P2P regression detection adds value vs hurts
533	  expected_results:
534	    total_reg5pct:
535	      iid_adv: -0.01
536	      block_adv: -0.005
537	      beneficial: false
538	    total_reg10pct:
539	      iid_adv: 0.132
540	      block_adv: 0.083
541	      beneficial: true
542	    total_reg20pct:
543	      iid_adv: 0.357
544	      block_adv: 0.278
545	      beneficial: true
546	    empirical_p2p_regression_rate: ~0.01
547	  result_rationale: 'Empirical P2P regression rate仅~1%，远低于10%的breakeven threshold。
548	    5% regression下per-test P2P monitoring实际HURTS(-0.01pp)：false positive P2P predictions
549	    导致correct patches被wrongly rejected。只有当regression rate≥10%时， true positive detection才outweigh
550	    false positive cost。 这是negative但highly informative finding。当前SWE-bench patch质量高，
551	    几乎不break passing tests——但real-world场景中regression rate可能更高。
552	
553	    '
554	  tables:
555	  - name: 'Table: P2P Regression Threshold'
556	    columns:
557	    - Regression Rate
558	    - Per-Test Adv (IID)
559	    - Beneficial?
560	    rows:
561	    - - 1% (empirical)
562	      - ≈0
563	      - 'No'
564	    - - 5%
565	      - -0.01
566	      - 'No'
567	    - - 10%
568	      - 0.132
569	      - 'Yes'
570	    - - 20%
571	      - 0.357
572	      - 'Yes'
573	  figures_description:
574	  - Regression rate vs per-test advantage curve with breakeven point marked
575	  analysis: 'Honest negative finding。Strengthens paper credibility by showing nuanced
576	    analysis rather than overclaiming P2P utility。
577	
578	    '
579	- name: Block Correlation Empirical Validation
580	  plan_id: block-corr-empirical
581	  description: Measured ICC and design effect from trained model predictions
582	  expected_results:
583	    icc: 0.1909
584	    icc_p_value: 0.0
585	    design_effect: 3.9676
586	    all_correct_observed: 46
587	    all_correct_expected_iid: 16.35
588	    all_correct_ratio: 2.81
589	    error_std_observed: 0.1531
590	    error_std_expected_iid: 0.0811
591	    error_std_ratio: 1.89
592	    n_samples: 1890
593	    n_problems: 114
594	  result_rationale: 'ICC=0.191说明19.1%的prediction error variance is between-problem(problem-level
595	    effect)。 这显著高于iid的0%(p<0.001)但远低于full block correlation(ICC=1.0)。 Design effect
596	    3.97意味着effective sample size = nominal/3.97， justifies ±2pp TOST margin：在effective
597	    N更小时，2pp是practical equivalence。 All-correct ratio 2.81x：观测到46个全对problem vs iid预期16.35个。
598	    模型对某些problems consistently correct(可能这些code patterns简单)， 对另一些consistently wrong(可能涉及complex
599	    logic)——errors不是random per-test。 Median tier下ICC=0.19是moderate，supports block
600	    model但effect size温和。 Oracle analysis中的block curve是upper bound，iid curve是lower
601	    bound， reality在两者之间但closer to iid端。
602	
603	    '
604	  tables:
605	  - name: 'Table: Error Correlation Validation'
606	    columns:
607	    - Metric
608	    - Observed
609	    - IID Expected
610	    - Ratio
611	    rows:
612	    - - All-correct problems
613	      - 46
614	      - 16.35
615	      - 2.81×
616	    - - Error rate std
617	      - 0.153
618	      - 0.081
619	      - 1.89×
620	    - - ICC
621	      - 0.191
622	      - 0
623	      - —
624	    - - Design Effect
625	      - 3.97
626	      - 1.0
627	      - 3.97×
628	  figures_description:
629	  - 'Per-problem error rate distribution: observed vs IID-expected histogram overlay'
630	  analysis: 'Validates block correlation assumption partially. The realistic per-test
631	    advantage is between IID and block curves. Paper should present both bounds with
632	    empirical ICC as the arbitrator rather than claiming only the optimistic block
633	    estimate.
634	
635	    '
636	- name: SWE-bench PerTest Dataset Construction
637	  plan_id: swebench-pertest-data
638	  description: Docker re-evaluation of 500 SWE-bench Verified instances × 16 candidates
639	  expected_results:
640	    target_instances: 500
641	    successful_instances: 435
642	    failed_instances: 65
643	    success_rate_pct: 87.0
644	    total_candidate_evaluations: 6960
645	    total_pertest_labels: ~68000
646	    avg_tests_per_instance: 156
647	    avg_f2p_tests: 2.8
648	    avg_p2p_tests: 153
649	    p2p_regression_rate: 0.013
650	    avg_code_tokens: 2800
651	    construction_time_hours: 22
652	  result_rationale: '65/500 Docker failures(13%)主要因为legacy Python packages unavailable
653	    in 2026、 特定版本pinning broken、Docker image build timeouts for large repos。 435 instances足以support
654	    repo-level training(350 train/85 test split approx)。 F2P stats与SWE-bench metadata一致(median
655	    T=1, mean T=2.8)。 P2P regression rate ~1.3%再次confirms低regression率——P2P维度信号弱。 Code
656	    tokens ~2800远超function-level的~200，这是repo-level generalization challenge的根源： 模型必须在10x更长的input上做judgment，attention
657	    dilution显著。 Median tier下data collection是infrastructure contribution，paper brief
658	    mention， detailed stats in appendix。
659	
660	    '
661	  tables:
662	  - name: 'Table (Appendix): SWE-bench-PerTest Stats'
663	    columns:
664	    - Statistic
665	    - Value
666	    rows:
667	    - - Instances (successful)
668	      - 435
669	    - - Candidates/instance
670	      - 16
671	    - - Per-test labels
672	      - ~68K
673	    - - Avg F2P tests
674	      - 2.8
675	    - - Avg code tokens
676	      - 2800
677	    - - P2P regression rate
678	      - 1.3%
679	  figures_description:
680	  - Test count distribution (F2P vs P2P)
681	  analysis: 'Sufficient data for repo-level experiments. Docker failure rate acceptable.
682	    P2P regression rate confirms prior negative finding.
683	
684	    '
685	- name: Repo-Level Training (CLS + CWM, multi-attempt)
686	  plan_id: repo-level-training
687	  description: Repo-level CLS at 4B/8B + CWM attempts, checkpoint sweeps
688	  expected_results:
689	    cls_4b_best:
690	      accuracy: 82.35
691	      f1_macro: 74.74
692	      fail_f1: 60.87
693	      pass_f1: 88.6
694	      fail_precision: 76.0
695	      fail_recall: 50.76
696	      unparseable_pct: 1.3
697	    cls_4b_seed123_test:
698	      accuracy: 75.33
699	      fail_f1: 50.5
700	    cls_8b_best:
701	      accuracy: 84.79
702	      f1_macro: 81.18
703	      fail_f1: 72.93
704	      pass_f1: 89.43
705	      unparseable_pct: 0
706	    cls_8b_seed123:
707	      accuracy: 85.6
708	      fail_f1: 65.89
709	    cls_8b_multiseed_mean_accuracy: 85.2
710	    cls_8b_multiseed_fail_f1_mean: 69.41
711	    cwm_v10:
712	      accuracy: 69.91
713	      unparseable_pct: 93.0
714	      fail_f1: 11.54
715	    cwm_v12:
716	      accuracy: 58.04
717	      unparseable_pct: 53.7
718	      fail_f1: 34.12
719	    cwm_seed123:
720	      accuracy: 59.09
721	      unparseable_pct: 67.2
722	    cwm_8b_attempts: all failed (training/eval infrastructure issues)
723	  result_rationale: 'Repo-level CLS在median range内：8B multi-seed mean ~85%在[80,85]上缘，
724	    fail_f1 ~69%在[60,72]内。Minority class(fail)预测弱的原因： repo-level code长(2800+ tokens)使模型难以精确定位failure
725	    cause， fail recall低(50-56%)说明模型对大量fail case预测为pass——conservative model under-diagnoses
726	    failures。Fail precision较好(76-92%)说明当模型predict fail时通常correct。
727	
728	    CWM catastrophic failure：93%(v10)或53.7%(v12)或67.2%(seed123) unparseable。 原因是repo-level
729	    execution output极长(tracebacks、assertion details、log messages)， generation model无法produce
730	    matching output。Max_new_tokens限制(64 in v10)导致 几乎所有output被truncated。即使放宽到1024 tokens(v11)，仍有75.2%
731	    unparseable。
732	
733	    Median tier核心tension：CWM failure是formulation limitation还是implementation issue？
734	    Reviewer会argue：(1) max_new_tokens太短是implementation choice；(2) better output format
735	    (structured JSON vs raw string)可能reduce unparseable。Paper需要honest discussion：
736	    "even with generous token budget, CWM unparseable rate remains >50%, suggesting
737	    formulation-level difficulty in predicting complex execution outputs."
738	
739	    4B seed variance高(82.35 vs 75.33)是concern——对checkpoint selection敏感。 8B更稳定(84.79
740	    vs 85.60)因为更大model对hyperparameter less sensitive。
741	
742	    '
743	  tables:
744	  - name: 'Table: Repo-Level CLS vs CWM'
745	    columns:
746	    - Model
747	    - Formulation
748	    - Best Acc
749	    - Fail F1
750	    - Unparseable%
751	    rows:
752	    - - 4B
753	      - CLS (seed42)
754	      - 82.35
755	      - 60.87
756	      - 1.3
757	    - - 4B
758	      - CLS (seed123)
759	      - 75.33
760	      - 50.5
761	      - 0
762	    - - 8B
763	      - CLS (seed42)
764	      - 84.79
765	      - 72.93
766	      - 0
767	    - - 8B
768	      - CLS (seed123)
769	      - 85.6
770	      - 65.89
771	      - 0
772	    - - 4B
773	      - CWM (v10)
774	      - 69.91
775	      - 11.54
776	      - 93.0
777	    - - 4B
778	      - CWM (v12)
779	      - 58.04
780	      - 34.12
781	      - 53.7
782	    - - 4B
783	      - CWM (seed123)
784	      - 59.09
785	      - —
786	      - 67.2
787	  - name: 'Table: Complexity-Dependent Formulation Gap'
788	    columns:
789	    - Level
790	    - CLS Best Acc
791	    - CWM Best Acc
792	    - CWM Unparseable%
793	    rows:
794	    - - Function (4B)
795	      - 87.51
796	      - 87.51
797	      - 0
798	    - - Function (8B)
799	      - 90.48
800	      - 87.67
801	      - 0
802	    - - Repo (4B)
803	      - 82.35
804	      - 69.91
805	      - 93.0
806	    - - Repo (8B)
807	      - 84.79
808	      - failed
809	      - —
810	  figures_description:
811	  - CLS checkpoint accuracy curve (4B and 8B, test set)
812	  - CWM unparseable rate across 10+ training attempts timeline
813	  - Function vs Repo level CLS/CWM gap visualization
814	  analysis: 'Repo-level是paper最contentious evidence。Framing必须是"CLS works where CWM
815	    fails" 而非"CLS beats CWM"——因为CWM没有fair comparison point（它根本无法produce valid output）。
816	    Reviewer concern mitigation：show multiple CWM attempts with different configs，
817	    demonstrate that unparseable rate persists despite engineering effort。
818	
819	    '
820	- name: LLM-as-Judge Zero-Shot Baselines
821	  plan_id: llm-judge-baseline
822	  description: Qwen3-8B and 32B NF4 zero-shot judge baselines
823	  expected_results:
824	    judge_8b:
825	      accuracy: 64.4
826	      fail_f1: 72.2
827	      fail_recall: 95.8
828	      pass_recall: 35.1
829	      traj_accuracy: 99.1
830	    judge_32b:
831	      accuracy: 71.69
832	      fail_f1: 75.91
833	      fail_recall: 92.43
834	      pass_recall: 52.35
835	    finetuned_4b:
836	      accuracy: 87.51
837	    finetuned_vs_judge_32b_gap_pp: 15.82
838	    majority_baseline: 51.7
839	  result_rationale: 'Zero-shot judges极端biased toward "fail"：8B fail_recall 95.8% but
840	    pass_recall仅35.1%。 模型的zero-shot heuristic是"mutated code = broken"，几乎不考虑mutation是否actually
841	    affects test outcome。32B稍好(pass_recall 52.35%)但仍heavily biased。 Fine-tuned 4B
842	    (87.51%) >> 32B zero-shot (71.69%)，gap 15.82pp： task-specific fine-tuning的value
843	    massive。8x更大的零训练模型仍不如4x更小的微调模型。 Traj-level accuracy 99.1%是trivial：数据中仅1个resolved
844	    instance， judge只需default to "unresolved"即可达99%。这highlights traj-level accuracy的
845	    deceptive nature——per-test accuracy是更honest的metric。
846	
847	    '
848	  tables:
849	  - name: 'Table: Fine-Tuned vs Zero-Shot'
850	    columns:
851	    - Model
852	    - Method
853	    - Per-Test Acc
854	    - Fail F1
855	    - Pass F1
856	    rows:
857	    - - Qwen3-4B
858	      - Fine-tuned CLS
859	      - 87.51
860	      - 87.86
861	      - 87.15
862	    - - Qwen3-8B
863	      - Zero-shot
864	      - 64.4
865	      - 72.2
866	      - 50.5
867	    - - Qwen3-32B NF4
868	      - Zero-shot
869	      - 71.69
870	      - 75.91
871	      - 65.68
872	    - - Majority
873	      - Baseline
874	      - 51.7
875	      - —
876	      - —
877	  figures_description:
878	  - 'Accuracy-compute Pareto frontier: fine-tuned CLS dominates'
879	  analysis: 'Uncontroversial finding。Confirms fine-tuning necessity for code verification。
880	    Reviewer可能ask for few-shot or chain-of-thought baselines as additional reference。
881	
882	    '
883	- name: Per-Test Majority Voting (K=3)
884	  plan_id: per-test-majority-voting
885	  description: Self-consistency K=3 on per-test classification
886	  expected_results:
887	    accuracy_greedy: 87.51
888	    accuracy_mv_k3: 86.83
889	    delta_pp: -0.69
890	    unanimous_rate: 93.3
891	    split_samples: 127
892	    flipped_correct_to_wrong: 28
893	    flipped_wrong_to_correct: 15
894	    net_flips: -13
895	    wall_time_greedy_sec: 30
896	    wall_time_mv_sec: 120
897	  result_rationale: 'Majority voting hurt accuracy by 0.69pp。93.3% of predictions
898	    are unanimous—— model is highly confident, disagreement occurs only on 127/1890
899	    = 6.7% of samples。 These are the hardest borderline cases where model is genuinely
900	    uncertain。 Voting on uncertain cases flips 28 correct→wrong vs 15 wrong→correct
901	    (net -13)： the model''s first-pass greedy prediction is better than random among
902	    its own alternatives。 This is unlike LLM reasoning tasks where self-consistency
903	    helps——per-test classification is a discrimination task where greedy decoding
904	    already captures the optimal decision boundary。 4x compute cost for worse accuracy
905	    makes MV strictly dominated。
906	
907	    '
908	  tables:
909	  - name: 'Table (Appendix): Majority Voting'
910	    columns:
911	    - Method
912	    - Accuracy
913	    - Time(s)
914	    - Net Flips
915	    rows:
916	    - - Greedy (K=1)
917	      - 87.51
918	      - 30
919	      - —
920	    - - Majority (K=3)
921	      - 86.83
922	      - 120
923	      - −13
924	  figures_description: []
925	  analysis: 'Negative result in appendix。Self-consistency不适用于well-calibrated binary
926	    classifiers。
927	
928	    '
929	- name: 5-Seed Paired Clustered Bootstrap (TOST Equivalence)
930	  plan_id: 5-paired-clustered-bootstrap
931	  description: Per-test vs trajectory-level TOST equivalence with clustered bootstrap
932	  expected_results:
933	    pooled_gap_pp: -0.45
934	    pooled_ci_lower: -1.71
935	    pooled_ci_upper: 0.84
936	    ci_width_pp: 2.55
937	    tost_p_value: 0.0071
938	    tost_margin_pp: 2.0
939	    equivalence_confirmed: true
940	    per_seed_gaps:
941	      s42: -0.97
942	      s123: 1.45
943	      s456: -1.84
944	      s789: -0.78
945	      s0: -0.29
946	    seed_level_paired_t_p: 0.425
947	    n_variants_pooled: 523
948	    n_clusters: 114
949	    n_resamples: 10000
950	  result_rationale: 'TOST p=0.007 << 0.05 confirms per-test ≈ trajectory within ±2pp
951	    margin。 CI [-1.71, +0.84] width = 2.55pp在median range [1.5, 3.0]——sufficiently
952	    narrow to confirm equivalence but not extremely tight。 Per-seed gaps from -1.84
953	    to +1.45：方向不一致，3 seeds per-test worse,  1 seed per-test better, 1 seed near-zero。This
954	    inconsistency IS the equivalence signal—— if one formulation were systematically
955	    better, gaps would be consistently one-sided。 ±2pp margin justification: with
956	    ICC=0.191 and DEFF=3.97, 2pp is practical significance threshold given the reduced
957	    effective sample size。 Clustered bootstrap (114 clusters, 10000 resamples) accounts
958	    for within-problem correlation that would bias naive CI estimates。
959	
960	    '
961	  tables:
962	  - name: 'Table: Per-Test vs Trajectory Equivalence'
963	    columns:
964	    - Seed
965	    - Gap (per-test − traj, pp)
966	    - Direction
967	    rows:
968	    - - 42
969	      - -0.97
970	      - Traj better
971	    - - 123
972	      - 1.45
973	      - Per-test better
974	    - - 456
975	      - -1.84
976	      - Traj better
977	    - - 789
978	      - -0.78
979	      - Traj better
980	    - - 0
981	      - -0.29
982	      - Traj better
983	    - - Pooled
984	      - −0.45 [−1.71, +0.84]
985	      - TOST p=0.007
986	  figures_description:
987	  - 'Forest plot: per-seed gaps with pooled CI, ±2pp TOST bounds as dotted verticals'
988	  analysis: 'Claim 2的methodological cornerstone。TOST at p=0.007 is strong evidence。
989	    Median tier下这是paper最rigorous statistical result和primary contribution。
990	
991	    '
992	- name: CLS/CWM Error Complementarity Analysis
993	  plan_id: error-overlap
994	  description: CLS vs CWM error overlap on function-level (seed42, n=1890)
995	  expected_results:
996	    both_correct:
997	      count: 1601
998	      pct: 84.71
999	    cls_only_correct:
1000	      count: 59
1001	      pct: 3.12
1002	    cwm_only_correct:
1003	      count: 53
1004	      pct: 2.8
1005	    both_wrong:
1006	      count: 177
1007	      pct: 9.37
1008	    oracle_ensemble_accuracy: 90.63
1009	    cls_error_mode: miss bugs (FN dominant, 75.4% of CLS errors)
1010	    cwm_error_mode: false alarms (FP dominant, 83.1% of CWM errors)
1011	    cohens_kappa_predictions: 0.88
1012	    cohens_kappa_correctness: 0.73
1013	  result_rationale: 'CLS-only correct (3.12%) ≈ CWM-only correct (2.80%)说明两种formulation有近乎equal
1014	    but different错误区域。Oracle ensemble 90.63%远高于either alone(87.51%)。 Error mode complementarity：CLS倾向miss
1015	    bugs(conservative, FN dominant)， CWM倾向false alarm(overgenerate error outputs)。这不是random
1016	    complementarity 而是structural：CLS的binary decision boundary和CWM的string matching
1017	    在不同case types上fail。 Off_by_one最complementary(CWM-only 4.8%, both wrong 14.9%)：
1018	    CLS难以detect subtle boundary changes but CWM sometimes captures output differences。
1019	    Return_value最不complementary(96.8% both correct)：both formulations handle this
1020	    easily。 Kappa(correctness)=0.73 < Kappa(predictions)=0.88说明agreement on what''s
1021	    correct is lower than agreement on predictions——there''s a meaningful disagreement
1022	    zone。
1023	
1024	    '
1025	  tables:
1026	  - name: 'Table: Error Overlap (4B, seed42)'
1027	    columns:
1028	    - Category
1029	    - Count
1030	    - '%'
1031	    rows:
1032	    - - Both correct
1033	      - 1601
1034	      - 84.71%
1035	    - - CLS-only correct
1036	      - 59
1037	      - 3.12%
1038	    - - CWM-only correct
1039	      - 53
1040	      - 2.80%
1041	    - - Both wrong
1042	      - 177
1043	      - 9.37%
1044	    - - Oracle ensemble
1045	      - —
1046	      - 90.63%
1047	  figures_description:
1048	  - 'Venn diagram: CLS vs CWM error overlap'
1049	  - Per-mutation complementarity breakdown
1050	  analysis: 'Oracle ensemble 90.63%是paper的supplementary selling point。 Framing: "formulation
1051	    diversity as a verification strategy" —  even if neither CLS nor CWM individually
1052	    dominates, combining them yields 3.12pp lift。
1053	
1054	    '
1055	- name: DeepSeek Function-Level CLS (seed42)
1056	  plan_id: deepseek-cls-func
1057	  description: DeepSeek-Coder-6.7B-Instruct LoRA CLS on function-level
1058	  expected_results:
1059	    accuracy: 86.8
1060	    pass_f1: 86.5
1061	    fail_f1: 87.1
1062	    unparseable: 0
1063	    vs_qwen_4b_cls_gap_pp: -0.71
1064	  result_rationale: 'DeepSeek-Coder-6.7B是code-specialized model，parameter count略大于Qwen3-4B但
1065	    architecture不同(MoE-style vs dense)。在function-level CLS上达到~86.8%， 略低于Qwen 4B(87.51%)的0.71pp。差距可能来自：(1)
1066	    LoRA hyperparameters为Qwen优化过， DeepSeek可能需要不同rank/lr；(2) tokenizer差异影响code representation
1067	    quality； (3) instruction format差异(DeepSeek用自己的chat template)。 这说明CLS formulation对architecture
1068	    robust(差异<1pp)但不是完全invariant。 Median tier下DeepSeek CLS function-level confirms
1069	    CLS generalizability但无exciting finding。
1070	
1071	    '
1072	  tables: []
1073	  figures_description: []
1074	  analysis: 'Cross-architecture CLS works. Small performance gap likely attributable
1075	    to hyperparameter tuning.
1076	
1077	    '
1078	- name: DeepSeek Function-Level CWM (seed42)
1079	  plan_id: deepseek-cwm-func
1080	  description: DeepSeek-Coder-6.7B-Instruct LoRA CWM on function-level
1081	  expected_results:
1082	    accuracy: 87.5
1083	    pass_f1: 87.3
1084	    fail_f1: 87.7
1085	    exact_match_rate: 85.1
1086	    unparseable: 0
1087	    vs_deepseek_cls_gap_pp: 0.7
1088	  result_rationale: 'DeepSeek CWM (87.5%) > DeepSeek CLS (86.8%)：gap = +0.7pp FAVORING
1089	    CWM。 这与Qwen finding(CLS略优)方向相反。原因推测：DeepSeek-Coder在code generation pretraining上更强，其generation
1090	    capability转移到execution output prediction上 比classification更efficiently。CWM在DeepSeek上exact_match
1091	    85.1% > Qwen的84.02%， suggesting DeepSeek生成output更precise。 This is the key median
1092	    tier prediction："mixed DeepSeek results"—— CLS-CWM gap方向在DeepSeek上flipped，undermining"CLS
1093	    universally better"narrative。 deepseek_func_cls_cwm_gap_pp = -0.7，在[-2.0, 2.0]
1094	    range内。
1095	
1096	    '
1097	  tables: []
1098	  figures_description: []
1099	  analysis: 'Direction flip on DeepSeek is the defining "mixed" result。Paper must
1100	    acknowledge that CLS advantage may be architecture-specific rather than formulation-universal。
1101	
1102	    '
1103	- name: DeepSeek Function-Level CWM (seed123)
1104	  plan_id: deepseek-cwm-func-s123
1105	  description: Second seed for DeepSeek CWM stability check
1106	  expected_results:
1107	    accuracy: 86.9
1108	    pass_f1: 86.7
1109	    fail_f1: 87.1
1110	    exact_match_rate: 84.3
1111	    vs_seed42_gap_pp: -0.6
1112	  result_rationale: 'Seed123 CWM (86.9%) 低于 seed42 (87.5%) 0.6pp——正常seed variance
1113	    range。 如果DeepSeek CLS也跑seed123(假设~86.5%)，CLS-CWM gap ≈ -0.4pp(CWM slightly better)。
1114	    两个seeds下gap = {seed42: -0.7, seed123: ~-0.4}，方向一致(CWM better on DeepSeek) 但effect
1115	    size小。Cross-seed一致性比Qwen好(Qwen的CLS-CWM gap从+0.32到+2.33 across seeds)。
1116	
1117	    '
1118	  tables:
1119	  - name: 'Table: DeepSeek Function-Level Summary'
1120	    columns:
1121	    - Seed
1122	    - DeepSeek CLS
1123	    - DeepSeek CWM
1124	    - Gap (CLS−CWM)
1125	    rows:
1126	    - - 42
1127	      - ~86.8
1128	      - 87.5
1129	      - −0.7
1130	    - - 123
1131	      - —
1132	      - 86.9
1133	      - —
1134	  figures_description: []
1135	  analysis: 'DeepSeek CWM ≥ CLS consistently across seeds. Combined with Qwen (CLS
1136	    > CWM), the cross-architecture story is: formulation advantage is model-dependent,
1137	    not universal.
1138	
1139	    '
1140	- name: DeepSeek Repo-Level CLS
1141	  plan_id: deepseek-cls-repo
1142	  description: DeepSeek-Coder-6.7B fine-tuned CLS on repo-level SWE-bench data
1143	  expected_results:
1144	    accuracy: 80.5
1145	    f1_macro: 71.8
1146	    fail_f1: 61.2
1147	    pass_f1: 82.4
1148	    unparseable_pct: 2.1
1149	    majority_baseline: 73.0
1150	    gap_vs_baseline_pp: 7.5
1151	  result_rationale: 'DeepSeek repo-level CLS (80.5%) 在Qwen 4B(82.35%) 和 8B(84.79%)之间，
1152	    符合其~6.7B parameter count。Fail_f1 61.2%在median range [60,72]。 Unparseable 2.1%略高于Qwen(0-1.3%)——DeepSeek
1153	    tokenizer对repo-level formatting edge cases处理稍差。Gap vs majority baseline (7.5pp)说明model
1154	    learned meaningful signal 但比Qwen的9-12pp gap小，可能因为hyperparameter没有充分tune for repo-level。
1155	    Median tier意义：partial confirmation that CLS works on repo-level across architectures，
1156	    但performance水平无new insight(comparable to Qwen within normal variance)。
1157	
1158	    '
1159	  tables:
1160	  - name: 'Table: Cross-Architecture Repo-Level CLS'
1161	    columns:
1162	    - Model
1163	    - Accuracy
1164	    - Fail F1
1165	    - Unparseable%
1166	    rows:
1167	    - - Qwen3-4B (best seed)
1168	      - 82.35
1169	      - 60.87
1170	      - 1.3
1171	    - - Qwen3-8B (best seed)
1172	      - 84.79
1173	      - 72.93
1174	      - 0
1175	    - - DeepSeek-6.7B
1176	      - ~80.5
1177	      - ~61.2
1178	      - ~2.1
1179	  figures_description:
1180	  - Cross-architecture repo-level CLS accuracy comparison
1181	  analysis: 'Confirms CLS repo-level viability across architectures but adds no dramatic
1182	    new evidence。 In paper: single line in results table, brief mention in text。
1183	
1184	    '
1185	- name: Repo-Level CLS Mutation-Type Analysis
1186	  plan_id: repo-mutation-analysis
1187	  description: Per-mutation-type accuracy breakdown for repo-level CLS 8B
1188	  expected_results:
1189	    overall_accuracy: 84.48
1190	    gold_accuracy: 96.24
1191	    operator_swap: 81.38
1192	    off_by_one: 86.89
1193	    return_value: 75.44
1194	    boundary_removal: 46.9
1195	    seed123_overall: 85.6
1196	    seed123_boundary_removal: 44.9
1197	    seed123_gold: 99.6
1198	  result_rationale: 'Boundary_removal极低(46.9%)——接近random guessing。这类mutation移除了if/while条件判断，
1199	    导致代码行为大幅改变但模型难以仅从code+test text判断影响。 Return_value也低(75.4%)：返回值变化在repo-level context中更难捕获因为
1200	    函数调用链更长，影响propagation更complex。 Gold accuracy高(96-99%)说明模型对未mutated code的判断reliable。
1201	    Off_by_one在repo-level(86.9%)比function-level(82.56%)还高——可能因为 repo-level tests更explicitly
1202	    test boundary conditions。 Median tier下此breakdown explains为什么repo-level fail_f1
1203	    only 60-73%： boundary_removal(占test set 10.7%)严重拖低整体fail detection。
1204	
1205	    '
1206	  tables:
1207	  - name: 'Table: Repo-Level CLS 8B Mutation Breakdown'
1208	    columns:
1209	    - Mutation Type
1210	    - Accuracy (s42)
1211	    - Accuracy (s123)
1212	    rows:
1213	    - - Gold (no mutation)
1214	      - 96.24%
1215	      - 99.60%
1216	    - - operator_swap
1217	      - 81.38%
1218	      - 82.60%
1219	    - - off_by_one
1220	      - 86.89%
1221	      - 79.20%
1222	    - - return_value
1223	      - 75.44%
1224	      - 66.40%
1225	    - - boundary_removal
1226	      - 46.90%
1227	      - 44.90%
1228	  figures_description:
1229	  - 'Radar chart: mutation-type accuracy across models (func 4B, repo 4B, repo 8B)'
1230	  analysis: Boundary_removal is the Achilles heel. Represents instances where CLS
1231	    cannot determine test outcome from static code analysis alone — would need execution-like
1232	    reasoning。 This partially validates CWM's approach (predicting execution) for
1233	    specific mutation types。
1234	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3227f44-7da9-4140-a736-681f757df56a",
  "isSidechain": false,
  "promptId": "f8c95270-2cda-4875-ab0f-f4534b23aa9f",
  "type": "user",
  "uuid": "c8ea5c0d-5f69-42dc-a366-c435638326cd",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260516T073712/median/imagined_experiments.yaml",
      "content": "tier: median\nnarrative_guidance: 'Median档叙事核心转变：Claim1从\"CLS>CWM\"降级为\"CLS works where CWM fails\"。\n  Function-level 4B null result (0pp gap, p=0.72) + 8B 2.43pp modest gap被接受但不视为exciting。\n  Repo-level CLS可用(82-85% accuracy)但CWM catastrophically fail(50-93% unparseable)，\n  部分reviewer质疑CWM failure是implementation问题(max_new_tokens设置、output format设计) 而非formulation固有限制，要求honest\n  discussion。 重心转向Claim2+3：per-test equivalence(TOST p=0.007, ±2pp)作为methodological\n  contribution， oracle characterization(T≥2 advantage集中在31.3% instances)作为practical\n  decision framework。 DeepSeek结果mixed——function-level gap方向不一致(CWM在DeepSeek上可能略优)，\n  repo-level CLS可用但无new insight。 Error complementarity(oracle ensemble 90.63%)成为supplementary\n  selling point。 仍可投EMNLP main但需strengthened related work、honest CWM limitations section。\n\n  '\nimagined_experiments:\n- name: CWM Generation Baseline (4B Function-Level)\n  plan_id: cwm-baseline\n  description: Qwen3-4B LoRA CWM vs CLS on function-level data, seed42\n  expected_results:\n    cls_accuracy: 87.51\n    cls_pass_f1: 87.1\n    cls_fail_f1: 87.9\n    cwm_accuracy: 87.51\n    cwm_pass_f1: 87.31\n    cwm_fail_f1: 87.71\n    accuracy_gap_pp: 0.0\n    cwm_exact_match_rate: 84.02\n    cwm_unparseable: 0\n  result_rationale: 'Function-level execution output短(通常<50 tokens)，CWM不触发token-budget\n    exhaustion 或string-value prediction failure modes。4B模型容量足以精确预测短输出。 两种formulation在此complexity\n    level达到identical accuracy(87.51%)。 Exact match rate 84.02% < accuracy 87.51%说明CWM有部分output不完全匹配但\n    通过pass/fail判断逻辑仍然correct——这预示repo-level上output matching会更困难。 Unparseable=0因为function-level输出格式统一简单。\n    Median tier下此null result是叙事基础：排除\"CLS trivially easier\"的concern， 建立complexity-dependent\n    advantage的前提。\n\n    '\n  tables:\n  - name: 'Table: Function-Level 4B CLS vs CWM (seed42)'\n    columns:\n    - Formulation\n    - Accuracy\n    - Pass F1\n    - Fail F1\n    - Exact Match\n    - Unparseable%\n    rows:\n    - - CLS\n      - 87.51\n      - 87.1\n      - 87.9\n      - N/A\n      - 0\n    - - CWM\n      - 87.51\n      - 87.31\n      - 87.71\n      - 84.02\n      - 0\n    - - Δ (CLS−CWM)\n      - 0.0\n      - −0.21\n      - 0.19\n      - —\n      - 0\n  figures_description:\n  - Per-class F1 bar chart, CLS与CWM几乎完全重叠\n  analysis: 'Null result confirmed. CWM exact_match (84.02%) < accuracy (87.51%)的gap(3.49pp)\n    暗示CWM在部分case上output不精确匹配但仍被判为correct—— repo-level上这个gap会急剧扩大导致catastrophic failure。\n\n    '\n- name: Multi-Seed Core Validation (5-seed, 4B)\n  plan_id: multi-seed-core\n  description: CLS 5-seed {42,123,456,789,0} + CWM 5-seed统计\n  expected_results:\n    cls_seeds:\n      s42:\n        accuracy: 87.83\n        pass_f1: 88.06\n        fail_f1: 87.59\n      s123:\n        accuracy: 89.52\n        pass_f1: 89.64\n        fail_f1: 89.4\n      s456:\n        accuracy: 87.88\n        pass_f1: 87.53\n        fail_f1: 88.21\n      s789:\n        accuracy: 89.0\n        pass_f1: 88.9\n        fail_f1: 89.1\n      s0:\n        accuracy: 87.94\n        pass_f1: 87.79\n        fail_f1: 88.08\n    cls_mean_accuracy: 88.43\n    cls_std_accuracy: 0.76\n    cwm_seeds:\n      s42:\n        accuracy: 87.51\n        pass_f1: 87.31\n        fail_f1: 87.71\n      s123:\n        accuracy: 87.2\n        pass_f1: 86.95\n        fail_f1: 87.44\n      s456:\n        accuracy: 86.98\n        pass_f1: 86.66\n        fail_f1: 87.29\n      s789:\n        accuracy: 86.67\n        pass_f1: 86.74\n        fail_f1: 86.6\n      s0:\n        accuracy: 87.57\n        pass_f1: 87.18\n        fail_f1: 87.93\n    cwm_mean_accuracy: 87.19\n    cwm_std_accuracy: 0.36\n    mean_gap_pp: 1.24\n    paired_t_p: ~0.06\n    significant_at_005: false\n  result_rationale: 'CLS 5-seed mean 88.43 vs CWM 87.19, gap 1.24pp。Paired t-test\n    p≈0.06，α=0.05下不显著。 CLS variance (std 0.76) > CWM (std 0.36)：CLS对LoRA初始化更敏感，因为binary\n    classification 的decision boundary位置对seed更敏感；CWM的generation target更deterministic，\n    不同seed主要影响generation fluency而非correctness。 Seed123是CLS的outlier high(89.52)和CWM的near-mean(87.20)，贡献了最大pair\n    gap。 Median tier：trend存在但不conclusive，这是4B function-level的inherent limitation——\n    task太简单，两种formulation的capacity均已饱和。\n\n    '\n  tables:\n  - name: 'Table: 4B 5-Seed CLS vs CWM'\n    columns:\n    - Seed\n    - CLS Acc\n    - CWM Acc\n    - Gap (pp)\n    rows:\n    - - 42\n      - 87.83\n      - 87.51\n      - 0.32\n    - - 123\n      - 89.52\n      - 87.2\n      - 2.32\n    - - 456\n      - 87.88\n      - 86.98\n      - 0.9\n    - - 789\n      - 89.0\n      - 86.67\n      - 2.33\n    - - 0\n      - 87.94\n      - 87.57\n      - 0.37\n    - - Mean±Std\n      - 88.43±0.76\n      - 87.19±0.36\n      - '+1.24'\n  figures_description:\n  - 5-seed accuracy dot plot with mean ± std bars, CLS蓝色、CWM橙色\n  analysis: 'p≈0.06处于borderline。Paper报告为\"directional trend (p=0.06) at 4B,  becomes\n    significant at 8B\"，building scaling narrative。\n\n    '\n- name: Trace-then-Judge Ablation\n  plan_id: trace-then-judge\n  description: 'Chain-of-thought style: generate reasoning trace → pass/fail'\n  expected_results:\n    training_status: failed\n    reason: output format instability, training diverged\n  result_rationale: '4B LoRA同时学习生成reasoning trace和predict pass/fail，两个objective竞争有限capacity。\n    Trace format不稳定导致pass/fail token被reasoning token侵蚀，accuracy崩溃。 这不是fundamental\n    impossibility而是engineering/capacity问题——更大模型或更精细的 format control可能解决。Median tier下dropped\n    from paper，brief mention in limitations。\n\n    '\n  tables: []\n  figures_description: []\n  analysis: '不影响core claims。如果成功，它会ablate away\"CLS优势来自skipping reasoning\"的concern；\n    failure意味着这个concern无法directly addressed，但8B scaling evidence间接addresses。\n\n    '\n- name: Trajectory-Level Fine-tuned Baseline\n  plan_id: traj-level-finetuned\n  description: 4B LoRA trained on resolved/unresolved prediction (5-seed)\n  expected_results:\n    seed42:\n      accuracy: 85.66\n      unresolved_f1: 87.5\n      resolved_f1: 83.18\n      consistency: 79.94\n    seed123:\n      accuracy: 85.47\n      unresolved_f1: 87.0\n      resolved_f1: 83.52\n      consistency: 78.59\n    seed456:\n      accuracy: 87.4\n      unresolved_f1: 88.7\n      resolved_f1: 85.8\n      consistency: 78.8\n    seed789:\n      accuracy: 87.31\n      unresolved_f1: 88.27\n      resolved_f1: 86.17\n      consistency: 76.74\n    seed0:\n      accuracy: 85.66\n      unresolved_f1: 87.37\n      resolved_f1: 83.41\n      consistency: 79.55\n    mean_accuracy: 86.3\n    std_accuracy: 0.93\n  result_rationale: 'Trajectory-level mean accuracy 86.30% vs per-test CLS 88.43%，gap\n    2.13pp。 这个gap的主要来源：(1) trajectory-level每个problem只产生1个训练样本 vs per-test产生T个， effective\n    training data量更少；(2) resolved需要ALL tests pass——这种conjunctive logic 比per-test的individual判断更难学。Consistency\n    rate ~78%说明同一problem内per-test predictions 有~22%不一致，暗示model在同一problem内对不同tests的判断受shared\n    context bias影响。 Median tier下此gap supports Claim 2的\"per-test不损失accuracy\"叙事，但gap部分\n    来自training data confound，需honest报告。\n\n    '\n  tables:\n  - name: 'Table: Trajectory-Level 5-Seed Results'\n    columns:\n    - Seed\n    - Accuracy\n    - Resolved F1\n    - Unresolved F1\n    - Consistency%\n    rows:\n    - - 42\n      - 85.66\n      - 83.18\n      - 87.5\n      - 79.94\n    - - 123\n      - 85.47\n      - 83.52\n      - 87.0\n      - 78.59\n    - - 456\n      - 87.4\n      - 85.8\n      - 88.7\n      - 78.8\n    - - 789\n      - 87.31\n      - 86.17\n      - 88.27\n      - 76.74\n    - - 0\n      - 85.66\n      - 83.41\n      - 87.37\n      - 79.55\n    - - Mean±Std\n      - 86.30±0.93\n      - 84.42±1.36\n      - 87.77±0.68\n      - 78.72±1.25\n  figures_description: []\n  analysis: 'Per-test ≥ trajectory at variant-level，TOST equivalence test (下述) 更rigorously\n    quantifies。\n\n    '\n- name: Model Size Scaling (8B, 3-seed)\n  plan_id: model-size-scaling\n  description: CLS vs CWM at 8B scale, seeds {42, 123, 456}\n  expected_results:\n    cls8b_seeds:\n      s42:\n        accuracy: 90.48\n        pass_f1: 90.86\n        fail_f1: 90.06\n      s123:\n        accuracy: 89.4\n        pass_f1: 89.54\n        fail_f1: 89.19\n      s456:\n        accuracy: 88.31\n        pass_f1: 88.2\n        fail_f1: 88.41\n    cls8b_mean_accuracy: 89.4\n    cls8b_std: 1.09\n    cwm8b_seeds:\n      s42:\n        accuracy: 87.67\n        pass_f1: 87.57\n        fail_f1: 87.77\n      s123:\n        accuracy: 86.98\n        pass_f1: 86.83\n        fail_f1: 87.13\n      s456:\n        accuracy: 86.24\n        pass_f1: 85.96\n        fail_f1: 86.51\n    cwm8b_mean_accuracy: 86.96\n    cwm8b_std: 0.72\n    mean_gap_pp: 2.43\n    per_seed_gaps:\n      s42: 2.81\n      s123: 2.42\n      s456: 2.07\n    cls_4b_to_8b_gain_pp: 0.97\n    cwm_4b_to_8b_gain_pp: -0.23\n  result_rationale: '8B CLS (89.40) vs CWM (86.96) gap扩大到2.43pp，所有3个seed方向一致(2.07-2.81pp)。\n    关键asymmetry：CLS从4B→8B提升0.97pp但CWM下降0.23pp。 CWM在8B未获益的原因：function-level generation的bottleneck在exact\n    string matching， 不是semantic understanding。额外的8B capacity没有reduce string matching\n    error—— 模型更好地\"理解\"了代码但仍然在output format上犯同样的errors。 CLS则从extra capacity中获益：binary\n    classification的decision boundary在高维space中 变得更smooth，reducing borderline case errors。\n    Median tier：2.43pp被接受为real but modest。Reviewer说\"interesting but not dramatic\"。\n    结合repo-level的catastrophic CWM failure讲故事：function-level hints at差异， repo-level放大为qualitative\n    failure。\n\n    '\n  tables:\n  - name: 'Table: 8B 3-Seed Scaling'\n    columns:\n    - Size\n    - CLS Mean Acc\n    - CWM Mean Acc\n    - Gap (pp)\n    rows:\n    - - 4B (5-seed)\n      - 88.43\n      - 87.19\n      - 1.24\n    - - 8B (seed42)\n      - 90.48\n      - 87.67\n      - 2.81\n    - - 8B (seed123)\n      - 89.4\n      - 86.98\n      - 2.42\n    - - 8B (seed456)\n      - 88.31\n      - 86.24\n      - 2.07\n    - - 8B (3-seed mean)\n      - 89.4\n      - 86.96\n      - 2.43\n  figures_description:\n  - 'Scaling plot: x=model size, y=accuracy, CLS和CWM两条线, 8B处diverge'\n  - Per-seed gap bar chart, 3 bars all positive (2.07-2.81)\n  analysis: '8B gap consistent across seeds is the function-level strongest evidence\n    for Claim 1。 但2.43pp在absolute terms仍modest。Paper frame为\"scaling direction\"而非\"large\n    effect\"。\n\n    '\n- name: Diagnostic Re-Repair (Downstream Proof-of-Concept)\n  plan_id: diagnostic-rerepair\n  description: Per-test failure predictions用于guide SWE-agent re-repair on 200 instances\n  expected_results:\n    n_instances_evaluated: 120\n    baseline_resolve_rate_pct: 24.2\n    with_pertest_resolve_rate_pct: 28.3\n    improvement_pp: 4.1\n    p_value_mcnemar: 0.11\n    significant_at_005: false\n    instances_diagnostic_helped: 14\n    instances_diagnostic_hurt: 9\n    net_helped: 5\n    avg_repair_attempts_baseline: 3.2\n    avg_repair_attempts_diagnostic: 2.8\n  result_rationale: 'Median tier下re-repair受三重限制：(1) 资源不足仅完成120/200 instances； (2)\n    per-test verifier error rate ~12.5%意味着约1/8的diagnostic信号是错误的， misleading repair\n    agent在错误方向搜索；(3) SWE-bench instances 68.7% T=1， 这些case per-test info退化为trajectory-level，不提供额外guidance。\n    4.1pp improvement方向正确，repair attempts减少(3.2→2.8)说明diagnostic确实 narrow了search space。但p=0.11在120\n    samples下不显著(power analysis显示需~400 instances)。 Net helped仅5(14-9)，说明diagnostic\n    precision不够——错误诊断导致9个case regression。 Median tier将此relegated to appendix/future\n    work，不作为main claim。\n\n    '\n  tables:\n  - name: 'Table (Appendix): Re-Repair Pilot Results'\n    columns:\n    - Condition\n    - Resolve Rate\n    - Avg Attempts\n    - N\n    rows:\n    - - Baseline (no per-test)\n      - 24.2%\n      - 3.2\n      - 120\n    - - With per-test diagnostic\n      - 28.3%\n      - 2.8\n      - 120\n    - - Δ\n      - +4.1pp (p=0.11)\n      - −0.4\n      - ''\n  figures_description:\n  - 'Paired comparison: helped(14) vs hurt(9) vs neutral(97) breakdown'\n  analysis: 'Directional but non-significant。Paper frame: \"preliminary evidence for\n    diagnostic utility, limited by verifier accuracy and sample size; full evaluation\n    left to future work.\"\n\n    '\n- name: Per-Test Precision/Recall Analysis\n  plan_id: per-test-precision-recall\n  description: Per-test failure prediction quality on full function-level test set\n  expected_results:\n    accuracy: 87.51\n    fail_precision: 82.75\n    fail_recall: 93.64\n    fail_f1: 87.86\n    pass_precision: 93.24\n    pass_recall: 81.8\n    pass_f1: 87.15\n    FP_count: 58\n    FN_count: 178\n    FP_FN_ratio: 0.326\n    best_mutation: return_value (97.26%)\n    worst_mutation: off_by_one (82.56%)\n    bucket_6_10_acc: 96.3\n    bucket_11plus_acc: 87.12\n  result_rationale: '模型显著biased toward predicting fail：fail_recall(93.64%) >> pass_recall(81.80%)。\n    这是因为training data中mutation几乎都导致fail，模型学到了conservative prior。 FP:FN = 58:178 →\n    75.4% of errors are false negatives(miss actual fails)。 这quantifies CLS的characteristic\n    failure mode：\"miss bugs\"而非\"false alarms\"。 Mutation类型分析：return_value最容易(97.26%)因为return值变化导致output大幅改变；\n    off_by_one最难(82.56%)因为边界条件变化subtle，模型需要precise numerical reasoning。 Bucket analysis：6-10\n    tests的problems accuracy最高(96.3%)因为multiple tests 提供redundant signal；11+ tests降至87.12%因为input\n    length增加导致attention稀释。\n\n    '\n  tables:\n  - name: 'Table: Per-Test Diagnostic Quality'\n    columns:\n    - Class\n    - Precision\n    - Recall\n    - F1\n    rows:\n    - - Fail (bug detected)\n      - 82.75\n      - 93.64\n      - 87.86\n    - - Pass (correct code)\n      - 93.24\n      - 81.8\n      - 87.15\n  - name: 'Table: Accuracy by Mutation Type'\n    columns:\n    - Mutation\n    - Accuracy\n    rows:\n    - - return_value\n      - 97.26%\n    - - variable_swap\n      - ~94%\n    - - operator_swap\n      - ~88%\n    - - off_by_one\n      - 82.56%\n  figures_description:\n  - Confusion matrix heatmap\n  - Accuracy by mutation type + test count bucket grouped bar chart\n  analysis: 'Error asymmetry (75% FN) 对downstream re-repair的影响：diagnostic signal会\n    under-report failures，导致repair agent可能miss真正的bug。 这与CWM的complementary failure\n    mode(83% false alarms)形成对比，支持oracle ensemble叙事。\n\n    '\n- name: Oracle F2P-Stratified Analysis\n  plan_id: oracle-f2p-stratified\n  description: Per-test advantage breakdown by FAIL_TO_PASS test count\n  expected_results:\n    T1_pct: 68.7\n    T1_block_adv: -0.09\n    T2_pct: 19.1\n    T2_block_adv: 31.69\n    T3_5_pct: 7.1\n    T3_5_block_adv: 40.74\n    T6plus_pct: 5.1\n    T6plus_block_adv: 40.06\n    overall_block_adv: 10.93\n    T2_contribution_pct: 55.3\n  result_rationale: 'T=1时per-test ≡ trajectory-level（只有一个fail test），advantage仅来自prediction\n    accuracy 微小差异（-0.09pp，essentially zero）。T=2时per-test advantage跳到31.69pp(block\n    model)： 原因是trajectory-level把两个tests的pass/fail合并为一个binary判断，丢失了which test failed的信息；\n    per-test分别预测，在一个test correct另一个wrong时仍能partial credit。 T≥3的advantage plateau在~40pp因为边际tests的marginal\n    information增量递减。 T2贡献55.3%的overall advantage因为它是最大的multi-test bucket(19.1%)且advantage显著。\n    Key insight for median tier：SWE-bench Verified 68.7%是T=1，限制了per-test的 population-level\n    impact。但targeting T≥2 subset (31.3%)时per-test显著优于trajectory。\n\n    '\n  tables:\n  - name: 'Table: Oracle Per-Test Advantage by F2P Count'\n    columns:\n    - T\n    - '% Instances'\n    - Block Adv (pp)\n    - Contribution to Overall\n    rows:\n    - - T=1\n      - 68.7\n      - -0.09\n      - −0.6%\n    - - T=2\n      - 19.1\n      - 31.69\n      - 55.3%\n    - - T=3−5\n      - 7.1\n      - 40.74\n      - 26.4%\n    - - T≥6\n      - 5.1\n      - 40.06\n      - 18.7%\n    - - Overall\n      - 100\n      - 10.93\n      - 100%\n  figures_description:\n  - 'Stacked bar: per-test advantage by T bucket with instance % overlay'\n  - SWE-bench F2P count distribution histogram\n  analysis: 'Claim 3的primary evidence。Actionable finding：deploy per-test only when\n    T≥2。 This characterization is the paper''s strongest unique contribution in median\n    tier。\n\n    '\n- name: Oracle Total (F2P+P2P) Validation\n  plan_id: oracle-total-validated\n  description: When P2P regression detection adds value vs hurts\n  expected_results:\n    total_reg5pct:\n      iid_adv: -0.01\n      block_adv: -0.005\n      beneficial: false\n    total_reg10pct:\n      iid_adv: 0.132\n      block_adv: 0.083\n      beneficial: true\n    total_reg20pct:\n      iid_adv: 0.357\n      block_adv: 0.278\n      beneficial: true\n    empirical_p2p_regression_rate: ~0.01\n  result_rationale: 'Empirical P2P regression rate仅~1%，远低于10%的breakeven threshold。\n    5% regression下per-test P2P monitoring实际HURTS(-0.01pp)：false positive P2P predictions\n    导致correct patches被wrongly rejected。只有当regression rate≥10%时， true positive detection才outweigh\n    false positive cost。 这是negative但highly informative finding。当前SWE-bench patch质量高，\n    几乎不break passing tests——但real-world场景中regression rate可能更高。\n\n    '\n  tables:\n  - name: 'Table: P2P Regression Threshold'\n    columns:\n    - Regression Rate\n    - Per-Test Adv (IID)\n    - Beneficial?\n    rows:\n    - - 1% (empirical)\n      - ≈0\n      - 'No'\n    - - 5%\n      - -0.01\n      - 'No'\n    - - 10%\n      - 0.132\n      - 'Yes'\n    - - 20%\n      - 0.357\n      - 'Yes'\n  figures_description:\n  - Regression rate vs per-test advantage curve with breakeven point marked\n  analysis: 'Honest negative finding。Strengthens paper credibility by showing nuanced\n    analysis rather than overclaiming P2P utility。\n\n    '\n- name: Block Correlation Empirical Validation\n  plan_id: block-corr-empirical\n  description: Measured ICC and design effect from trained model predictions\n  expected_results:\n    icc: 0.1909\n    icc_p_value: 0.0\n    design_effect: 3.9676\n    all_correct_observed: 46\n    all_correct_expected_iid: 16.35\n    all_correct_ratio: 2.81\n    error_std_observed: 0.1531\n    error_std_expected_iid: 0.0811\n    error_std_ratio: 1.89\n    n_samples: 1890\n    n_problems: 114\n  result_rationale: 'ICC=0.191说明19.1%的prediction error variance is between-problem(problem-level\n    effect)。 这显著高于iid的0%(p<0.001)但远低于full block correlation(ICC=1.0)。 Design effect\n    3.97意味着effective sample size = nominal/3.97， justifies ±2pp TOST margin：在effective\n    N更小时，2pp是practical equivalence。 All-correct ratio 2.81x：观测到46个全对problem vs iid预期16.35个。\n    模型对某些problems consistently correct(可能这些code patterns简单)， 对另一些consistently wrong(可能涉及complex\n    logic)——errors不是random per-test。 Median tier下ICC=0.19是moderate，supports block\n    model但effect size温和。 Oracle analysis中的block curve是upper bound，iid curve是lower\n    bound， reality在两者之间但closer to iid端。\n\n    '\n  tables:\n  - name: 'Table: Error Correlation Validation'\n    columns:\n    - Metric\n    - Observed\n    - IID Expected\n    - Ratio\n    rows:\n    - - All-correct problems\n      - 46\n      - 16.35\n      - 2.81×\n    - - Error rate std\n      - 0.153\n      - 0.081\n      - 1.89×\n    - - ICC\n      - 0.191\n      - 0\n      - —\n    - - Design Effect\n      - 3.97\n      - 1.0\n      - 3.97×\n  figures_description:\n  - 'Per-problem error rate distribution: observed vs IID-expected histogram overlay'\n  analysis: 'Validates block correlation assumption partially. The realistic per-test\n    advantage is between IID and block curves. Paper should present both bounds with\n    empirical ICC as the arbitrator rather than claiming only the optimistic block\n    estimate.\n\n    '\n- name: SWE-bench PerTest Dataset Construction\n  plan_id: swebench-pertest-data\n  description: Docker re-evaluation of 500 SWE-bench Verified instances × 16 candidates\n  expected_results:\n    target_instances: 500\n    successful_instances: 435\n    failed_instances: 65\n    success_rate_pct: 87.0\n    total_candidate_evaluations: 6960\n    total_pertest_labels: ~68000\n    avg_tests_per_instance: 156\n    avg_f2p_tests: 2.8\n    avg_p2p_tests: 153\n    p2p_regression_rate: 0.013\n    avg_code_tokens: 2800\n    construction_time_hours: 22\n  result_rationale: '65/500 Docker failures(13%)主要因为legacy Python packages unavailable\n    in 2026、 特定版本pinning broken、Docker image build timeouts for large repos。 435 instances足以support\n    repo-level training(350 train/85 test split approx)。 F2P stats与SWE-bench metadata一致(median\n    T=1, mean T=2.8)。 P2P regression rate ~1.3%再次confirms低regression率——P2P维度信号弱。 Code\n    tokens ~2800远超function-level的~200，这是repo-level generalization challenge的根源： 模型必须在10x更长的input上做judgment，attention\n    dilution显著。 Median tier下data collection是infrastructure contribution，paper brief\n    mention， detailed stats in appendix。\n\n    '\n  tables:\n  - name: 'Table (Appendix): SWE-bench-PerTest Stats'\n    columns:\n    - Statistic\n    - Value\n    rows:\n    - - Instances (successful)\n      - 435\n    - - Candidates/instance\n      - 16\n    - - Per-test labels\n      - ~68K\n    - - Avg F2P tests\n      - 2.8\n    - - Avg code tokens\n      - 2800\n    - - P2P regression rate\n      - 1.3%\n  figures_description:\n  - Test count distribution (F2P vs P2P)\n  analysis: 'Sufficient data for repo-level experiments. Docker failure rate acceptable.\n    P2P regression rate confirms prior negative finding.\n\n    '\n- name: Repo-Level Training (CLS + CWM, multi-attempt)\n  plan_id: repo-level-training\n  description: Repo-level CLS at 4B/8B + CWM attempts, checkpoint sweeps\n  expected_results:\n    cls_4b_best:\n      accuracy: 82.35\n      f1_macro: 74.74\n      fail_f1: 60.87\n      pass_f1: 88.6\n      fail_precision: 76.0\n      fail_recall: 50.76\n      unparseable_pct: 1.3\n    cls_4b_seed123_test:\n      accuracy: 75.33\n      fail_f1: 50.5\n    cls_8b_best:\n      accuracy: 84.79\n      f1_macro: 81.18\n      fail_f1: 72.93\n      pass_f1: 89.43\n      unparseable_pct: 0\n    cls_8b_seed123:\n      accuracy: 85.6\n      fail_f1: 65.89\n    cls_8b_multiseed_mean_accuracy: 85.2\n    cls_8b_multiseed_fail_f1_mean: 69.41\n    cwm_v10:\n      accuracy: 69.91\n      unparseable_pct: 93.0\n      fail_f1: 11.54\n    cwm_v12:\n      accuracy: 58.04\n      unparseable_pct: 53.7\n      fail_f1: 34.12\n    cwm_seed123:\n      accuracy: 59.09\n      unparseable_pct: 67.2\n    cwm_8b_attempts: all failed (training/eval infrastructure issues)\n  result_rationale: 'Repo-level CLS在median range内：8B multi-seed mean ~85%在[80,85]上缘，\n    fail_f1 ~69%在[60,72]内。Minority class(fail)预测弱的原因： repo-level code长(2800+ tokens)使模型难以精确定位failure\n    cause， fail recall低(50-56%)说明模型对大量fail case预测为pass——conservative model under-diagnoses\n    failures。Fail precision较好(76-92%)说明当模型predict fail时通常correct。\n\n    CWM catastrophic failure：93%(v10)或53.7%(v12)或67.2%(seed123) unparseable。 原因是repo-level\n    execution output极长(tracebacks、assertion details、log messages)， generation model无法produce\n    matching output。Max_new_tokens限制(64 in v10)导致 几乎所有output被truncated。即使放宽到1024 tokens(v11)，仍有75.2%\n    unparseable。\n\n    Median tier核心tension：CWM failure是formulation limitation还是implementation issue？\n    Reviewer会argue：(1) max_new_tokens太短是implementation choice；(2) better output format\n    (structured JSON vs raw string)可能reduce unparseable。Paper需要honest discussion：\n    \"even with generous token budget, CWM unparseable rate remains >50%, suggesting\n    formulation-level difficulty in predicting complex execution outputs.\"\n\n    4B seed variance高(82.35 vs 75.33)是concern——对checkpoint selection敏感。 8B更稳定(84.79\n    vs 85.60)因为更大model对hyperparameter less sensitive。\n\n    '\n  tables:\n  - name: 'Table: Repo-Level CLS vs CWM'\n    columns:\n    - Model\n    - Formulation\n    - Best Acc\n    - Fail F1\n    - Unparseable%\n    rows:\n    - - 4B\n      - CLS (seed42)\n      - 82.35\n      - 60.87\n      - 1.3\n    - - 4B\n      - CLS (seed123)\n      - 75.33\n      - 50.5\n      - 0\n    - - 8B\n      - CLS (seed42)\n      - 84.79\n      - 72.93\n      - 0\n    - - 8B\n      - CLS (seed123)\n      - 85.6\n      - 65.89\n      - 0\n    - - 4B\n      - CWM (v10)\n      - 69.91\n      - 11.54\n      - 93.0\n    - - 4B\n      - CWM (v12)\n      - 58.04\n      - 34.12\n      - 53.7\n    - - 4B\n      - CWM (seed123)\n      - 59.09\n      - —\n      - 67.2\n  - name: 'Table: Complexity-Dependent Formulation Gap'\n    columns:\n    - Level\n    - CLS Best Acc\n    - CWM Best Acc\n    - CWM Unparseable%\n    rows:\n    - - Function (4B)\n      - 87.51\n      - 87.51\n      - 0\n    - - Function (8B)\n      - 90.48\n      - 87.67\n      - 0\n    - - Repo (4B)\n      - 82.35\n      - 69.91\n      - 93.0\n    - - Repo (8B)\n      - 84.79\n      - failed\n      - —\n  figures_description:\n  - CLS checkpoint accuracy curve (4B and 8B, test set)\n  - CWM unparseable rate across 10+ training attempts timeline\n  - Function vs Repo level CLS/CWM gap visualization\n  analysis: 'Repo-level是paper最contentious evidence。Framing必须是\"CLS works where CWM\n    fails\" 而非\"CLS beats CWM\"——因为CWM没有fair comparison point（它根本无法produce valid output）。\n    Reviewer concern mitigation：show multiple CWM attempts with different configs，\n    demonstrate that unparseable rate persists despite engineering effort。\n\n    '\n- name: LLM-as-Judge Zero-Shot Baselines\n  plan_id: llm-judge-baseline\n  description: Qwen3-8B and 32B NF4 zero-shot judge baselines\n  expected_results:\n    judge_8b:\n      accuracy: 64.4\n      fail_f1: 72.2\n      fail_recall: 95.8\n      pass_recall: 35.1\n      traj_accuracy: 99.1\n    judge_32b:\n      accuracy: 71.69\n      fail_f1: 75.91\n      fail_recall: 92.43\n      pass_recall: 52.35\n    finetuned_4b:\n      accuracy: 87.51\n    finetuned_vs_judge_32b_gap_pp: 15.82\n    majority_baseline: 51.7\n  result_rationale: 'Zero-shot judges极端biased toward \"fail\"：8B fail_recall 95.8% but\n    pass_recall仅35.1%。 模型的zero-shot heuristic是\"mutated code = broken\"，几乎不考虑mutation是否actually\n    affects test outcome。32B稍好(pass_recall 52.35%)但仍heavily biased。 Fine-tuned 4B\n    (87.51%) >> 32B zero-shot (71.69%)，gap 15.82pp： task-specific fine-tuning的value\n    massive。8x更大的零训练模型仍不如4x更小的微调模型。 Traj-level accuracy 99.1%是trivial：数据中仅1个resolved\n    instance， judge只需default to \"unresolved\"即可达99%。这highlights traj-level accuracy的\n    deceptive nature——per-test accuracy是更honest的metric。\n\n    '\n  tables:\n  - name: 'Table: Fine-Tuned vs Zero-Shot'\n    columns:\n    - Model\n    - Method\n    - Per-Test Acc\n    - Fail F1\n    - Pass F1\n    rows:\n    - - Qwen3-4B\n      - Fine-tuned CLS\n      - 87.51\n      - 87.86\n      - 87.15\n    - - Qwen3-8B\n      - Zero-shot\n      - 64.4\n      - 72.2\n      - 50.5\n    - - Qwen3-32B NF4\n      - Zero-shot\n      - 71.69\n      - 75.91\n      - 65.68\n    - - Majority\n      - Baseline\n      - 51.7\n      - —\n      - —\n  figures_description:\n  - 'Accuracy-compute Pareto frontier: fine-tuned CLS dominates'\n  analysis: 'Uncontroversial finding。Confirms fine-tuning necessity for code verification。\n    Reviewer可能ask for few-shot or chain-of-thought baselines as additional reference。\n\n    '\n- name: Per-Test Majority Voting (K=3)\n  plan_id: per-test-majority-voting\n  description: Self-consistency K=3 on per-test classification\n  expected_results:\n    accuracy_greedy: 87.51\n    accuracy_mv_k3: 86.83\n    delta_pp: -0.69\n    unanimous_rate: 93.3\n    split_samples: 127\n    flipped_correct_to_wrong: 28\n    flipped_wrong_to_correct: 15\n    net_flips: -13\n    wall_time_greedy_sec: 30\n    wall_time_mv_sec: 120\n  result_rationale: 'Majority voting hurt accuracy by 0.69pp。93.3% of predictions\n    are unanimous—— model is highly confident, disagreement occurs only on 127/1890\n    = 6.7% of samples。 These are the hardest borderline cases where model is genuinely\n    uncertain。 Voting on uncertain cases flips 28 correct→wrong vs 15 wrong→correct\n    (net -13)： the model''s first-pass greedy prediction is better than random among\n    its own alternatives。 This is unlike LLM reasoning tasks where self-consistency\n    helps——per-test classification is a discrimination task where greedy decoding\n    already captures the optimal decision boundary。 4x compute cost for worse accuracy\n    makes MV strictly dominated。\n\n    '\n  tables:\n  - name: 'Table (Appendix): Majority Voting'\n    columns:\n    - Method\n    - Accuracy\n    - Time(s)\n    - Net Flips\n    rows:\n    - - Greedy (K=1)\n      - 87.51\n      - 30\n      - —\n    - - Majority (K=3)\n      - 86.83\n      - 120\n      - −13\n  figures_description: []\n  analysis: 'Negative result in appendix。Self-consistency不适用于well-calibrated binary\n    classifiers。\n\n    '\n- name: 5-Seed Paired Clustered Bootstrap (TOST Equivalence)\n  plan_id: 5-paired-clustered-bootstrap\n  description: Per-test vs trajectory-level TOST equivalence with clustered bootstrap\n  expected_results:\n    pooled_gap_pp: -0.45\n    pooled_ci_lower: -1.71\n    pooled_ci_upper: 0.84\n    ci_width_pp: 2.55\n    tost_p_value: 0.0071\n    tost_margin_pp: 2.0\n    equivalence_confirmed: true\n    per_seed_gaps:\n      s42: -0.97\n      s123: 1.45\n      s456: -1.84\n      s789: -0.78\n      s0: -0.29\n    seed_level_paired_t_p: 0.425\n    n_variants_pooled: 523\n    n_clusters: 114\n    n_resamples: 10000\n  result_rationale: 'TOST p=0.007 << 0.05 confirms per-test ≈ trajectory within ±2pp\n    margin。 CI [-1.71, +0.84] width = 2.55pp在median range [1.5, 3.0]——sufficiently\n    narrow to confirm equivalence but not extremely tight。 Per-seed gaps from -1.84\n    to +1.45：方向不一致，3 seeds per-test worse,  1 seed per-test better, 1 seed near-zero。This\n    inconsistency IS the equivalence signal—— if one formulation were systematically\n    better, gaps would be consistently one-sided。 ±2pp margin justification: with\n    ICC=0.191 and DEFF=3.97, 2pp is practical significance threshold given the reduced\n    effective sample size。 Clustered bootstrap (114 clusters, 10000 resamples) accounts\n    for within-problem correlation that would bias naive CI estimates。\n\n    '\n  tables:\n  - name: 'Table: Per-Test vs Trajectory Equivalence'\n    columns:\n    - Seed\n    - Gap (per-test − traj, pp)\n    - Direction\n    rows:\n    - - 42\n      - -0.97\n      - Traj better\n    - - 123\n      - 1.45\n      - Per-test better\n    - - 456\n      - -1.84\n      - Traj better\n    - - 789\n      - -0.78\n      - Traj better\n    - - 0\n      - -0.29\n      - Traj better\n    - - Pooled\n      - −0.45 [−1.71, +0.84]\n      - TOST p=0.007\n  figures_description:\n  - 'Forest plot: per-seed gaps with pooled CI, ±2pp TOST bounds as dotted verticals'\n  analysis: 'Claim 2的methodological cornerstone。TOST at p=0.007 is strong evidence。\n    Median tier下这是paper最rigorous statistical result和primary contribution。\n\n    '\n- name: CLS/CWM Error Complementarity Analysis\n  plan_id: error-overlap\n  description: CLS vs CWM error overlap on function-level (seed42, n=1890)\n  expected_results:\n    both_correct:\n      count: 1601\n      pct: 84.71\n    cls_only_correct:\n      count: 59\n      pct: 3.12\n    cwm_only_correct:\n      count: 53\n      pct: 2.8\n    both_wrong:\n      count: 177\n      pct: 9.37\n    oracle_ensemble_accuracy: 90.63\n    cls_error_mode: miss bugs (FN dominant, 75.4% of CLS errors)\n    cwm_error_mode: false alarms (FP dominant, 83.1% of CWM errors)\n    cohens_kappa_predictions: 0.88\n    cohens_kappa_correctness: 0.73\n  result_rationale: 'CLS-only correct (3.12%) ≈ CWM-only correct (2.80%)说明两种formulation有近乎equal\n    but different错误区域。Oracle ensemble 90.63%远高于either alone(87.51%)。 Error mode complementarity：CLS倾向miss\n    bugs(conservative, FN dominant)， CWM倾向false alarm(overgenerate error outputs)。这不是random\n    complementarity 而是structural：CLS的binary decision boundary和CWM的string matching\n    在不同case types上fail。 Off_by_one最complementary(CWM-only 4.8%, both wrong 14.9%)：\n    CLS难以detect subtle boundary changes but CWM sometimes captures output differences。\n    Return_value最不complementary(96.8% both correct)：both formulations handle this\n    easily。 Kappa(correctness)=0.73 < Kappa(predictions)=0.88说明agreement on what''s\n    correct is lower than agreement on predictions——there''s a meaningful disagreement\n    zone。\n\n    '\n  tables:\n  - name: 'Table: Error Overlap (4B, seed42)'\n    columns:\n    - Category\n    - Count\n    - '%'\n    rows:\n    - - Both correct\n      - 1601\n      - 84.71%\n    - - CLS-only correct\n      - 59\n      - 3.12%\n    - - CWM-only correct\n      - 53\n      - 2.80%\n    - - Both wrong\n      - 177\n      - 9.37%\n    - - Oracle ensemble\n      - —\n      - 90.63%\n  figures_description:\n  - 'Venn diagram: CLS vs CWM error overlap'\n  - Per-mutation complementarity breakdown\n  analysis: 'Oracle ensemble 90.63%是paper的supplementary selling point。 Framing: \"formulation\n    diversity as a verification strategy\" —  even if neither CLS nor CWM individually\n    dominates, combining them yields 3.12pp lift。\n\n    '\n- name: DeepSeek Function-Level CLS (seed42)\n  plan_id: deepseek-cls-func\n  description: DeepSeek-Coder-6.7B-Instruct LoRA CLS on function-level\n  expected_results:\n    accuracy: 86.8\n    pass_f1: 86.5\n    fail_f1: 87.1\n    unparseable: 0\n    vs_qwen_4b_cls_gap_pp: -0.71\n  result_rationale: 'DeepSeek-Coder-6.7B是code-specialized model，parameter count略大于Qwen3-4B但\n    architecture不同(MoE-style vs dense)。在function-level CLS上达到~86.8%， 略低于Qwen 4B(87.51%)的0.71pp。差距可能来自：(1)\n    LoRA hyperparameters为Qwen优化过， DeepSeek可能需要不同rank/lr；(2) tokenizer差异影响code representation\n    quality； (3) instruction format差异(DeepSeek用自己的chat template)。 这说明CLS formulation对architecture\n    robust(差异<1pp)但不是完全invariant。 Median tier下DeepSeek CLS function-level confirms\n    CLS generalizability但无exciting finding。\n\n    '\n  tables: []\n  figures_description: []\n  analysis: 'Cross-architecture CLS works. Small performance gap likely attributable\n    to hyperparameter tuning.\n\n    '\n- name: DeepSeek Function-Level CWM (seed42)\n  plan_id: deepseek-cwm-func\n  description: DeepSeek-Coder-6.7B-Instruct LoRA CWM on function-level\n  expected_results:\n    accuracy: 87.5\n    pass_f1: 87.3\n    fail_f1: 87.7\n    exact_match_rate: 85.1\n    unparseable: 0\n    vs_deepseek_cls_gap_pp: 0.7\n  result_rationale: 'DeepSeek CWM (87.5%) > DeepSeek CLS (86.8%)：gap = +0.7pp FAVORING\n    CWM。 这与Qwen finding(CLS略优)方向相反。原因推测：DeepSeek-Coder在code generation pretraining上更强，其generation\n    capability转移到execution output prediction上 比classification更efficiently。CWM在DeepSeek上exact_match\n    85.1% > Qwen的84.02%， suggesting DeepSeek生成output更precise。 This is the key median\n    tier prediction：\"mixed DeepSeek results\"—— CLS-CWM gap方向在DeepSeek上flipped，undermining\"CLS\n    universally better\"narrative。 deepseek_func_cls_cwm_gap_pp = -0.7，在[-2.0, 2.0]\n    range内。\n\n    '\n  tables: []\n  figures_description: []\n  analysis: 'Direction flip on DeepSeek is the defining \"mixed\" result。Paper must\n    acknowledge that CLS advantage may be architecture-specific rather than formulation-universal。\n\n    '\n- name: DeepSeek Function-Level CWM (seed123)\n  plan_id: deepseek-cwm-func-s123\n  description: Second seed for DeepSeek CWM stability check\n  expected_results:\n    accuracy: 86.9\n    pass_f1: 86.7\n    fail_f1: 87.1\n    exact_match_rate: 84.3\n    vs_seed42_gap_pp: -0.6\n  result_rationale: 'Seed123 CWM (86.9%) 低于 seed42 (87.5%) 0.6pp——正常seed variance\n    range。 如果DeepSeek CLS也跑seed123(假设~86.5%)，CLS-CWM gap ≈ -0.4pp(CWM slightly better)。\n    两个seeds下gap = {seed42: -0.7, seed123: ~-0.4}，方向一致(CWM better on DeepSeek) 但effect\n    size小。Cross-seed一致性比Qwen好(Qwen的CLS-CWM gap从+0.32到+2.33 across seeds)。\n\n    '\n  tables:\n  - name: 'Table: DeepSeek Function-Level Summary'\n    columns:\n    - Seed\n    - DeepSeek CLS\n    - DeepSeek CWM\n    - Gap (CLS−CWM)\n    rows:\n    - - 42\n      - ~86.8\n      - 87.5\n      - −0.7\n    - - 123\n      - —\n      - 86.9\n      - —\n  figures_description: []\n  analysis: 'DeepSeek CWM ≥ CLS consistently across seeds. Combined with Qwen (CLS\n    > CWM), the cross-architecture story is: formulation advantage is model-dependent,\n    not universal.\n\n    '\n- name: DeepSeek Repo-Level CLS\n  plan_id: deepseek-cls-repo\n  description: DeepSeek-Coder-6.7B fine-tuned CLS on repo-level SWE-bench data\n  expected_results:\n    accuracy: 80.5\n    f1_macro: 71.8\n    fail_f1: 61.2\n    pass_f1: 82.4\n    unparseable_pct: 2.1\n    majority_baseline: 73.0\n    gap_vs_baseline_pp: 7.5\n  result_rationale: 'DeepSeek repo-level CLS (80.5%) 在Qwen 4B(82.35%) 和 8B(84.79%)之间，\n    符合其~6.7B parameter count。Fail_f1 61.2%在median range [60,72]。 Unparseable 2.1%略高于Qwen(0-1.3%)——DeepSeek\n    tokenizer对repo-level formatting edge cases处理稍差。Gap vs majority baseline (7.5pp)说明model\n    learned meaningful signal 但比Qwen的9-12pp gap小，可能因为hyperparameter没有充分tune for repo-level。\n    Median tier意义：partial confirmation that CLS works on repo-level across architectures，\n    但performance水平无new insight(comparable to Qwen within normal variance)。\n\n    '\n  tables:\n  - name: 'Table: Cross-Architecture Repo-Level CLS'\n    columns:\n    - Model\n    - Accuracy\n    - Fail F1\n    - Unparseable%\n    rows:\n    - - Qwen3-4B (best seed)\n      - 82.35\n      - 60.87\n      - 1.3\n    - - Qwen3-8B (best seed)\n      - 84.79\n      - 72.93\n      - 0\n    - - DeepSeek-6.7B\n      - ~80.5\n      - ~61.2\n      - ~2.1\n  figures_description:\n  - Cross-architecture repo-level CLS accuracy comparison\n  analysis: 'Confirms CLS repo-level viability across architectures but adds no dramatic\n    new evidence。 In paper: single line in results table, brief mention in text。\n\n    '\n- name: Repo-Level CLS Mutation-Type Analysis\n  plan_id: repo-mutation-analysis\n  description: Per-mutation-type accuracy breakdown for repo-level CLS 8B\n  expected_results:\n    overall_accuracy: 84.48\n    gold_accuracy: 96.24\n    operator_swap: 81.38\n    off_by_one: 86.89\n    return_value: 75.44\n    boundary_removal: 46.9\n    seed123_overall: 85.6\n    seed123_boundary_removal: 44.9\n    seed123_gold: 99.6\n  result_rationale: 'Boundary_removal极低(46.9%)——接近random guessing。这类mutation移除了if/while条件判断，\n    导致代码行为大幅改变但模型难以仅从code+test text判断影响。 Return_value也低(75.4%)：返回值变化在repo-level context中更难捕获因为\n    函数调用链更长，影响propagation更complex。 Gold accuracy高(96-99%)说明模型对未mutated code的判断reliable。\n    Off_by_one在repo-level(86.9%)比function-level(82.56%)还高——可能因为 repo-level tests更explicitly\n    test boundary conditions。 Median tier下此breakdown explains为什么repo-level fail_f1\n    only 60-73%： boundary_removal(占test set 10.7%)严重拖低整体fail detection。\n\n    '\n  tables:\n  - name: 'Table: Repo-Level CLS 8B Mutation Breakdown'\n    columns:\n    - Mutation Type\n    - Accuracy (s42)\n    - Accuracy (s123)\n    rows:\n    - - Gold (no mutation)\n      - 96.24%\n      - 99.60%\n    - - operator_swap\n      - 81.38%\n      - 82.60%\n    - - off_by_one\n      - 86.89%\n      - 79.20%\n    - - return_value\n      - 75.44%\n      - 66.40%\n    - - boundary_removal\n      - 46.90%\n      - 44.90%\n  figures_description:\n  - 'Radar chart: mutation-type accuracy across models (func 4B, repo 4B, repo 8B)'\n  analysis: Boundary_removal is the Achilles heel. Represents instances where CLS\n    cannot determine test outcome from static code analysis alone — would need execution-like\n    reasoning。 This partially validates CWM's approach (predicting execution) for\n    specific mutation types。\n",
      "numLines": 1234,
      "startLine": 1,
      "totalLines": 1234
    }
  },
  "sourceToolAssistantUUID": "e3227f44-7da9-4140-a736-681f757df56a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14 · 2026-05-16T15:14:27.299Z_

````json
{
  "parentUuid": "c8ea5c0d-5f69-42dc-a366-c435638326cd",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**exec-sim-repair-verifier**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"exec-sim-repair-verifier\")` 或 `load_project_config(\"exec-sim-repair-verifier\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/exec-sim-repair-verifier/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "125273d7-49a0-4bad-aebb-2e48d5f92197",
  "timestamp": "2026-05-16T15:14:27.299Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：部分跨模型验证——DeepSeek repo CLS 可用但弱于 Qwen，CWM 部分可解析使得差距缩小；C1 需 model-dependent caveat，C2 仅 Qwen 内验证 核心假设：['DeepSeek repo CWM 部分可解析（unparseable 15–40%），parsea…",
  "leafUuid": "125273d7-49a0-4bad-aebb-2e48d5f92197",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-model verification with DeepSeek—median tier narrative",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00"
}
```

---

### Assistant

_source line 17 · 2026-05-16T15:17:09.806Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. The user wants me to generate the median tier imagined experiments YAML for ALL planned experiments in the experiment_plan. Let me identify which experiments are still "planned" (not DONE) and which are RUNNING/PREPARING:

From the experiment_plan:
1. **diagnostic-rerepair** (plan_id) - status: planned
2. **swebench-pertest-data** (plan_id) - status: planned

From the registry (RUNNING/PREPARING status):
3. **deepseek-cls-repo** - RUNNING


4. **deepseek-cwm-repo** - RUNNING
5. **deepseek-traj-func-s123** - ANALYZING
6. **deepseek-traj-func-v2-fixed** - PREPARING, failed
7. **deepseek-traj-func-v2-s123-fixed** - PREPARING, failed
8. **deepseek-traj-repo** - PREPARING
9. **deepseek-traj-repo-s123** - PREPARING

Actually, I need to reconsider what the user is asking for. They want detailed data expansion for each planned experiment in the experiment_plan, which means I should focus on the two planned experiments from the plan itself, not all the running ones from the registry. Looking at the full list, I can see that diagnostic-rerepair and swebench-pertest-data are the only two experiments marked as "planned" in the experiment_plan. The rest are either completed or failed, though there are some registry experiments still in progress that might correspond to plan items.

But I notice the existing imagined_experiments.yaml already has predictions for completed experiments too, using their actual results as the expected outcomes. So the user probably wants me to generate predictions for all the planned experiments, treating the ones that are already done as reference points for what the predictions should look like. I'm noticing there are experiments in the registry that aren't listed in the experiment_plan—like the DeepSeek repo variants and trajectory experiments that are currently running or preparing. The existing imagined_experiments.yaml already has predictions for the planned experiments (diagnostic-rerepair and swebench-pertest-data) plus many completed ones, and it covers some of these in-progress experiments too. But I need to check which experiments the user actually wants me to generate predictions for, since the median tier definition they provided specifically mentions DeepSeek repo CLS/CWM and trajectory predictions. I need to regenerate the full median tier imagined_experiments YAML with current knowledge, since the existing file might be outdated. Looking at what's already covered, I see fourteen experiments listed, but I should verify this matches the latest status of running and planned items to ensure nothing's missing or needs updating. Looking at the performance metrics across these DeepSeek configurations, I'm seeing a pattern where the repo-level CLS accuracy sits at 70-78%, underperforming Qwen by 5-12 percentage points, while the CWM-CLS gap is narrower than expected. The trajectory experiments didn't finish in time, and the re-repair attempts haven't shown meaningful improvements over the baseline control results, so I need to establish median predictions for the running experiments based on these observed performance characteristics. Looking at the actual results across all the deepseek variants, I can see the function-level models are performing well (85-87% accuracy range), while the trajectory models show more variation. Now I need to figure out which experiments are still missing from the YAML and what predictions to add for the ones that haven't completed yet. I'm realizing the user wants predictions for all experiments that still need results—not just the two explicitly listed as "planned" in the experiment_plan, but also the DeepSeek variants currently running in the registry. Let me identify which experiments actually need median tier predictions: diagnostic-rerepair and swebench-pertest-data from the plan, plus the DeepSeek experiments that are actively running or preparing.

Now I'm working through the median tier thresholds to apply predictions across these experiments based on the defined ranges for accuracy, error rates, and performance gaps.

I need to clarify what the user is asking for—whether they want me to expand only the experiments marked as "planned" or provide a comprehensive YAML that includes both completed and planned experiments with detailed predictions for each one. Let me re-examine the request to understand if I should focus on just the planned entries or generate a full dataset covering all 21 experiments with their median-tier projections and rationales. just 2 experiments
2. All experiments in the plan → ~15 experiments

Given the context and the output format, I think they want ALL experiments (including done ones, since the YAML format includes all). But they emphasize "每条预测都必须给出 result_rationale" which suggests they want rationales for predictions.

OK here's my interpretation: The user wants me to produce the full median tier YAML with ALL experiments from the experiment_plan + the additional DeepSeek experiments, with median-tier predictions and rationales. The existing YAML is a reference, but I should produce a new comprehensive version that incorporates:

1. Actual results for completed experiments (used as "expected_results" since the median tier should reflect what actually happened where known)
2. Predicted results for planned/running/preparing experiments under the median tier assumptions

Looking at the experiment_plan, I see about 14 experiments total: the baseline and multi-seed work are done, trace-then-judge failed, trajectory-level finetuning is complete, model scaling is done, diagnostic repair is planned, per-test metrics are done, oracle variants are done, block correlation is done, swebench data prep is planned, repo-level training failed, judge baseline is done, and majority voting is done. Plus there are additional experiments from the registry that should be included in this comprehensive median tier version.

I'm now looking at the additional DeepSeek experiments that were listed: the paired bootstrap, error complementarity analysis, and various DeepSeek model variants across function-level and repo-level settings with different seeds, plus the trajectory-based DeepSeek experiments and the re-repair phase 0 which came back negative.

I need to synthesize all of this into a coherent median tier YAML that shows the progression and relationships between experiments while maintaining realistic predictions based on what we know about the actual results. I'm realizing the user specifically asked for "planned" experiments in the experiment_plan, which narrows it down to diagnostic-rerepair and swebench-pertest-data. But given the extensive DeepSeek registry data they provided and the median-tier narrative context, I think they'd find it more useful if I included all the incomplete experiments plus the key ones driving the research story. Let me build a comprehensive YAML that covers everything meaningfully. I need to distinguish between the DONE experiments where I should use actual registry results and the RUNNING/PREPARING ones where I'll generate median-tier predictions. Let me work through which experiments need new predictions versus which ones I can pull real data for. I see the diagnostic-rerepair experiment won't actually proceed as a full experiment since the re-repair-phase0 results are negative and stuck at phase0, so I should update that prediction accordingly. For swebench-pertest-data, the status remains planned with the existing YAML prediction. Now I'm compiling the final output focusing on the planned experiments with updated predictions, the running/preparing/analyzing experiments from the registry that need predictions, and the completed deepseek experiments not yet in the YAML with their actual results. I'm realizing the user's request in Chinese is asking for detailed data expansion on each planned experiment in the experiment_plan. Looking at the context, I have a comprehensive YAML with 21 experiments already documented, and I need to decide whether to expand all of them or just the ones marked as "planned" status. Given the request for detailed data with rationale and the existing comprehensive file, I think the user wants the full treatment across all experiments, using actual metrics for completed ones and reasonable predictions for those still in progress or planned. The user is probably asking me to UPDATE this YAML with:
1. The newly completed DeepSeek experiments (cls-func-s123, traj-func-v2, etc.)
2. Predictions for still-running experiments (deepseek-cls-repo, deepseek-cwm-repo)
3. Predictions for experiments that won't complete (deepseek-traj-repo, etc.)

Let me produce the full updated YAML. That's going to be extremely long though, so I need to think about what the most useful output is.

Looking at the median tier definition more carefully, my core assumptions are: DeepSeek repo CWM has 15–40% unparseable content with 60–72% accuracy on parseable subsets, repo CLS reaches 70–78% accuracy, the CLS–CWM gap narrows to 5–12pp compared to Qwen's 15+pp spread, the TRAJ repo won't finish by the deadline, and re-repair stays stuck in phase 0. These predictions mainly affect the repo-level experiments for cls, cwm, and traj, plus the re-repair downstream work and function-level trajectory comparisons needed for cross-model equivalence. Now I'm going through the remaining experiments to include in the YAML—per-test precision-recall, oracle variants, block correlation analysis, and the SWEBench data experiment, most of which are complete with actual results, though a couple are still planned with median predictions as placeholders. I'm also tracking the repo-level training results which had mixed outcomes, the majority voting approach, and several DeepSeek-specific experiments including the function-level variants and error complementarity analysis.

Looking at the full scope here, I realize the YAML output is going to be quite extensive, so I need to think about how to structure this efficiently rather than just listing everything verbatim. The user's request about expanding planned experiments with detailed data suggests they want substantive information, but I should reconsider whether that's actually what they're asking for or if I'm overcomplicating this.

Let me focus on what makes sense: the experiments marked as planned in the experiment_plan, plus the registry experiments that are part of the median narrative since those don't have final results yet. For the median-tier predictions, I'll need to estimate reasonable ranges based on what I know about the models and benchmarks involved.

For deepseek-cls-repo, I'm looking at the median range of 70-78% accuracy and settling around 74% as a reasonable midpoint, with fail_f1 probably in the 55-62% range and unparseable rates staying low around 1-3%. For deepseek-cwm-repo, the median suggests around 27% unparseable with parseable accuracy in the 60-72% range, which would be a significant improvement over the Qwen CWM results.

The CLS-CWM gap for DeepSeek narrows to about 8.5 percentage points. I've already got the actual results for both deepseek-traj-func-v2 variants (83.24% and 85.08%), while deepseek-traj-repo won't complete in time and diagnostic-rerepair is staying at phase 0 with control and classification diagnostic similarities both around 0.82.

Now looking at the function-level DeepSeek comparisons, the actual results show CLS at 86.93% outperforming CWM at 85.77% by 1.16 percentage points, which contradicts the earlier YAML predictions that had CWM slightly ahead.

However, checking the median tier bounds of [-0.5, 1.5] for this gap, the actual 1.16pp difference falls within the acceptable range. Across the two seeds tested, seed 42 favors CLS by 1.16pp while seed 123 favors CWM by 1.11pp, so the results are fairly balanced.

Now looking at the trajectory variant comparison, CLS consistently outperforms the trajectory approach—by 3.69pp on seed 42 and 1.69pp on seed 123, averaging around 2.69pp, which appears to fit within the expected bounds.

This cross-model evidence from DeepSeek aligns with what I'm seeing in Qwen, reinforcing the claim that CLS is the superior approach. I need to now compile the complete YAML output covering all the planned experiments with their detailed results and rationales.

Looking at the experiment_plan, I can see that most experiments are already marked as DONE, but there are only two that are actually planned: diagnostic-rerepair and swebench-pertest-data. I should focus on expanding those two with comprehensive data rather than repeating the experiments that are already complete.

However, the median tier definition references DeepSeek experiments and other work that isn't formally listed in the experiment_plan but exists in the registry. Since the user is asking for imagined_experiments in plural and wants predictions for what's still needed, I should create a YAML output that covers both the planned experiments from the formal plan and the in-progress or pending experiments from the registry, like the DeepSeek repo variants and the re-repair analysis.

The existing imagined_experiments.yaml was generated back in May, so some of these experiments have likely progressed. I'll compile a comprehensive YAML that includes all experiments—both completed ones where I can use actual results and incomplete ones where I'll apply median tier predictions—to give a complete picture of where things stand now.

Generating the comprehensive YAML... I'm realizing the existing YAML already captures the 14 planned experiments plus some extras, so I just need to fill in the missing DeepSeek variants and the re-repair baseline that aren't yet included.

Now I'm going to compile the complete updated YAML with all experiments organized by claim group, making sure to include actual results where they differ from predictions and keeping the structure clear and thorough.

Generating complete YAML...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "125273d7-49a0-4bad-aebb-2e48d5f92197",
  "isSidechain": false,
  "requestId": "req_011Cb6TzGxpREx5wRoM2uGaM",
  "type": "assistant",
  "uuid": "b5424f23-e12f-4336-baba-930ef1380735",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sKho75fvzUjuTJ66N5Tnb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22976,
      "cache_read_input_tokens": 45602,
      "output_tokens": 9935,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9935,
          "cache_read_input_tokens": 45602,
          "cache_creation_input_tokens": 22976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22976
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

_source line 18 · 2026-05-16T15:17:09.808Z_

I'll check what DeepSeek experiments are currently running and their latest status, then produce the comprehensive YAML.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5424f23-e12f-4336-baba-930ef1380735",
  "isSidechain": false,
  "requestId": "req_011Cb6TzGxpREx5wRoM2uGaM",
  "type": "assistant",
  "uuid": "a55f7ab1-4f30-4ce9-b6c2-ac78c7833c0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sKho75fvzUjuTJ66N5Tnb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22976,
      "cache_read_input_tokens": 45602,
      "output_tokens": 9935,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9935,
          "cache_read_input_tokens": 45602,
          "cache_creation_input_tokens": 22976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22976
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

_source line 19 · 2026-05-16T15:17:10.858Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XzcbRC6APwQe59W3m5wxQ6`</summary>

```json
{
  "pattern": "**/deepseek*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a55f7ab1-4f30-4ce9-b6c2-ac78c7833c0a",
  "isSidechain": false,
  "requestId": "req_011Cb6TzGxpREx5wRoM2uGaM",
  "type": "assistant",
  "uuid": "c66a3b2e-ab7d-4669-b7ad-6e07dd150406",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sKho75fvzUjuTJ66N5Tnb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22976,
      "cache_read_input_tokens": 45602,
      "output_tokens": 9935,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9935,
          "cache_read_input_tokens": 45602,
          "cache_creation_input_tokens": 22976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22976
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

_source line 20 · 2026-05-16T15:17:10.887Z_

<details><summary>↩ Tool result · `toolu_01XzcbRC6APwQe59W3m5wxQ6`</summary>

```text
projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-func_ANALYZING_20260516T075642.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func_ANALYZING_20260516T080020.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-func-s123_ANALYZING_20260516T080029.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-func_ANALYZING_20260516T080057.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-func_DONE_20260516T080116.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-repo_QUEUED_20260516T080507.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func_ANALYZING_20260516T080510.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-func-s123_ANALYZING_20260516T080510.json
projects/exec-sim-repair-verifier/artifacts/deepseek_training_analysis.md
projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func_DONE_20260516T080523.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-repo_RUNNING_20260516T080524.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-func-s123_DONE_20260516T080525.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func-s123_PREPARING_20260516T111140.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func-s123_PENDING_20260516T111202.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func-s123_QUEUED_20260516T111207.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func-s123_RUNNING_20260516T111213.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func-s123_DONE_20260516T111218.json
projects/exec-sim-repair-verifier/artifacts/deepseek-traj-func/intermediate/deepseek_traj_func_launch.md
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func_QUEUED_20260516T120915.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func_RUNNING_20260516T120921.json
projects/exec-sim-repair-verifier/artifacts/deepseek_func_summary.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-s123_QUEUED_20260516T122703.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-s123_RUNNING_20260516T122710.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-s123_ANALYZING_20260516T122747.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func_RUNNING_20260516T125812.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func_DONE_20260516T125816.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2_PREPARING_20260516T134639.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_PREPARING_20260516T134705.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_PENDING_20260516T141616.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_QUEUED_20260516T141623.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_ALLOCATED_20260516T141635.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_RUNNING_20260516T141643.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2_PENDING_20260516T141703.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2_QUEUED_20260516T141708.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2_ALLOCATED_20260516T141712.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2_RUNNING_20260516T141721.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-fixed_PREPARING_20260516T141843.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2_DONE_20260516T142039.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2_DONE_20260516T142041.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_ANALYZING_20260516T143519.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_ANALYZING_20260516T143526.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_DONE_20260516T143544.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123-fixed_PREPARING_20260516T143742.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-repo_PREPARING_20260516T144202.json
projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-repo-s123_PREPARING_20260516T144203.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c66a3b2e-ab7d-4669-b7ad-6e07dd150406",
  "isSidechain": false,
  "promptId": "f8c95270-2cda-4875-ab0f-f4534b23aa9f",
  "type": "user",
  "uuid": "6eb6c74f-8970-4798-a75f-89ae34890278",
  "toolUseResult": {
    "filenames": [
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-func_ANALYZING_20260516T075642.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func_ANALYZING_20260516T080020.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-func-s123_ANALYZING_20260516T080029.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-func_ANALYZING_20260516T080057.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-func_DONE_20260516T080116.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-repo_QUEUED_20260516T080507.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func_ANALYZING_20260516T080510.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-func-s123_ANALYZING_20260516T080510.json",
      "projects/exec-sim-repair-verifier/artifacts/deepseek_training_analysis.md",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func_DONE_20260516T080523.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-repo_RUNNING_20260516T080524.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-func-s123_DONE_20260516T080525.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func-s123_PREPARING_20260516T111140.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func-s123_PENDING_20260516T111202.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func-s123_QUEUED_20260516T111207.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func-s123_RUNNING_20260516T111213.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-cls-func-s123_DONE_20260516T111218.json",
      "projects/exec-sim-repair-verifier/artifacts/deepseek-traj-func/intermediate/deepseek_traj_func_launch.md",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func_QUEUED_20260516T120915.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func_RUNNING_20260516T120921.json",
      "projects/exec-sim-repair-verifier/artifacts/deepseek_func_summary.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-s123_QUEUED_20260516T122703.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-s123_RUNNING_20260516T122710.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-s123_ANALYZING_20260516T122747.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func_RUNNING_20260516T125812.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func_DONE_20260516T125816.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2_PREPARING_20260516T134639.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_PREPARING_20260516T134705.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_PENDING_20260516T141616.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_QUEUED_20260516T141623.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_ALLOCATED_20260516T141635.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_RUNNING_20260516T141643.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2_PENDING_20260516T141703.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2_QUEUED_20260516T141708.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2_ALLOCATED_20260516T141712.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2_RUNNING_20260516T141721.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-fixed_PREPARING_20260516T141843.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2_DONE_20260516T142039.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2_DONE_20260516T142041.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_ANALYZING_20260516T143519.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_ANALYZING_20260516T143526.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123_DONE_20260516T143544.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-func-v2-s123-fixed_PREPARING_20260516T143742.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-repo_PREPARING_20260516T144202.json",
      "projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-repo-s123_PREPARING_20260516T144203.json"
    ],
    "durationMs": 23,
    "numFiles": 45,
    "truncated": false
  },
  "sourceToolAssistantUUID": "c66a3b2e-ab7d-4669-b7ad-6e07dd150406",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：部分跨模型验证——DeepSeek repo CLS 可用但弱于 Qwen，CWM 部分可解析使得差距缩小；C1 需 model-dependent caveat，C2 仅 Qwen 内验证 核心假设：['DeepSeek repo CWM 部分可解析（unparseable 15–40%），parsea…",
  "leafUuid": "6eb6c74f-8970-4798-a75f-89ae34890278",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-model verification with DeepSeek—median tier narrative",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00"
}
```

---

### Tool call

_source line 23 · 2026-05-16T15:17:14.038Z_

<details open><summary>🔧 Tool call — Read · `toolu_01838qxWJeizRUuoJ1X8YFzW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/deepseek_func_summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6eb6c74f-8970-4798-a75f-89ae34890278",
  "isSidechain": false,
  "requestId": "req_011Cb6UCLisPA33NeXGbsni5",
  "type": "assistant",
  "uuid": "81f6b091-798c-4e9b-aae8-d59509faae75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4UUChi6xdwo9hzAtjYTAw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11591,
      "cache_read_input_tokens": 68578,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11591,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 272,
          "cache_read_input_tokens": 68578,
          "cache_creation_input_tokens": 11591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11591
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

_source line 24 · 2026-05-16T15:17:14.043Z_

<details><summary>↩ Tool result · `toolu_01838qxWJeizRUuoJ1X8YFzW`</summary>

```text
1	{
2	  "model": "DeepSeek-Coder-6.7B-Instruct",
3	  "level": "func",
4	  "test_set": {
5	    "n_instances": 1890,
6	    "label_distribution": {"pass": 978, "fail": 912},
7	    "majority_baseline_pct": 51.75
8	  },
9	  "experiments": {
10	    "CLS": {
11	      "seed42": {
12	        "accuracy": 86.93,
13	        "f1_macro": 86.92,
14	        "precision_fail": 86.42,
15	        "recall_fail": 86.51,
16	        "f1_fail": 86.47,
17	        "precision_pass": 87.41,
18	        "recall_pass": 87.32,
19	        "f1_pass": 87.37,
20	        "unparseable_rate": 0.0,
21	        "best_checkpoint_step": 478,
22	        "best_epoch": 1,
23	        "total_steps": 1434,
24	        "total_epochs": 3,
25	        "train_batch_size": 2,
26	        "training_time_min_approx": 90,
27	        "confusion_matrix": {"tn": 789, "fp": 123, "fn": 124, "tp": 854}
28	      },
29	      "seed123": {
30	        "accuracy": 86.77,
31	        "f1_macro": 86.77,
32	        "precision_fail": 84.99,
33	        "recall_fail": 88.16,
34	        "f1_fail": 86.54,
35	        "precision_pass": 88.56,
36	        "recall_pass": 85.48,
37	        "f1_pass": 86.99,
38	        "unparseable_rate": 0.0,
39	        "best_checkpoint_step": 956,
40	        "best_epoch": 1,
41	        "total_steps": 2868,
42	        "total_epochs": 3,
43	        "train_batch_size": 2,
44	        "training_time_min_approx": 90,
45	        "confusion_matrix": {"tn": 804, "fp": 108, "fn": 142, "tp": 836}
46	      },
47	      "mean_accuracy": 86.85,
48	      "mean_f1_macro": 86.845,
49	      "std_accuracy": 0.11,
50	      "std_f1_macro": 0.11
51	    },
52	    "CWM": {
53	      "seed42": {
54	        "accuracy": 85.77,
55	        "f1_macro": 85.73,
56	        "precision_fail": 80.07,
57	        "recall_fail": 93.86,
58	        "f1_fail": 86.42,
59	        "precision_pass": 93.18,
60	        "recall_pass": 78.22,
61	        "f1_pass": 85.05,
62	        "unparseable_rate": 0.0,
63	        "best_checkpoint_step": 956,
64	        "best_epoch": 2,
65	        "total_steps": 1434,
66	        "total_epochs": 3,
67	        "train_batch_size": 2,
68	        "training_time_min_approx": 87,
69	        "generation_stats": {"mean": 28.1, "median": 33.0, "max": 103, "min": 20},
70	        "confusion_matrix": {"tn": 856, "fp": 56, "fn": 213, "tp": 765}
71	      },
72	      "seed123": {
73	        "accuracy": 87.88,
74	        "f1_macro": 87.88,
75	        "precision_fail": 83.78,
76	        "recall_fail": 92.87,
77	        "f1_fail": 88.09,
78	        "precision_pass": 92.61,
79	        "recall_pass": 83.23,
80	        "f1_pass": 87.67,
81	        "unparseable_rate": 0.0,
82	        "best_checkpoint_step": 956,
83	        "best_epoch": 2,
84	        "total_steps": 1434,
85	        "total_epochs": 3,
86	        "train_batch_size": 2,
87	        "training_time_min_approx": 87,
88	        "generation_stats": {"mean": 28.1, "median": 33.0, "max": 103, "min": 20},
89	        "confusion_matrix": {"tn": 847, "fp": 65, "fn": 164, "tp": 814}
90	      },
91	      "mean_accuracy": 86.83,
92	      "mean_f1_macro": 86.81,
93	      "std_accuracy": 1.49,
94	      "std_f1_macro": 1.52
95	    }
96	  },
97	  "roadmap_verification": {
98	    "claimed_cls": "86.85±0.11%",
99	    "actual_cls": "86.85±0.11%",
100	    "cls_correct": true,
101	    "claimed_cwm": "86.83±1.49%",
102	    "actual_cwm": "86.83±1.49%",
103	    "cwm_correct": true
104	  },
105	  "registry_discrepancy": {
106	    "issue": "Registry claims deepseek-cls-func-s123 acc=87.88, actual is 86.77. The 87.88 belongs to deepseek-cwm-func-s123.",
107	    "corrected_cls_s123_accuracy": 86.77,
108	    "corrected_cwm_s123_accuracy": 87.88
109	  },
110	  "paper_table_data": {
111	    "DeepSeek-6.7B_CLS_func": {
112	      "accuracy_mean": 86.85,
113	      "accuracy_std": 0.11,
114	      "f1_mean": 86.85,
115	      "f1_std": 0.11,
116	      "unparseable_pct": 0.0
117	    },
118	    "DeepSeek-6.7B_CWM_func": {
119	      "accuracy_mean": 86.83,
120	      "accuracy_std": 1.49,
121	      "f1_mean": 86.81,
122	      "f1_std": 1.52,
123	      "unparseable_pct": 0.0
124	    }
125	  },
126	  "notes": [
127	    "All experiments run on 4×RTX5090 (single GPU used per experiment)",
128	    "CLS best checkpoints converge at epoch 1; CWM at epoch 2",
129	    "CWM shows higher variance across seeds (std 1.49 vs 0.11)",
130	    "CWM has asymmetric precision/recall: high precision_pass + high recall_fail pattern",
131	    "Zero unparseable for all DeepSeek func-level experiments"
132	  ]
133	}
134	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81f6b091-798c-4e9b-aae8-d59509faae75",
  "isSidechain": false,
  "promptId": "f8c95270-2cda-4875-ab0f-f4534b23aa9f",
  "type": "user",
  "uuid": "1de50cde-cdbb-466a-ba9f-9f128b334d36",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/deepseek_func_summary.json",
      "content": "{\n  \"model\": \"DeepSeek-Coder-6.7B-Instruct\",\n  \"level\": \"func\",\n  \"test_set\": {\n    \"n_instances\": 1890,\n    \"label_distribution\": {\"pass\": 978, \"fail\": 912},\n    \"majority_baseline_pct\": 51.75\n  },\n  \"experiments\": {\n    \"CLS\": {\n      \"seed42\": {\n        \"accuracy\": 86.93,\n        \"f1_macro\": 86.92,\n        \"precision_fail\": 86.42,\n        \"recall_fail\": 86.51,\n        \"f1_fail\": 86.47,\n        \"precision_pass\": 87.41,\n        \"recall_pass\": 87.32,\n        \"f1_pass\": 87.37,\n        \"unparseable_rate\": 0.0,\n        \"best_checkpoint_step\": 478,\n        \"best_epoch\": 1,\n        \"total_steps\": 1434,\n        \"total_epochs\": 3,\n        \"train_batch_size\": 2,\n        \"training_time_min_approx\": 90,\n        \"confusion_matrix\": {\"tn\": 789, \"fp\": 123, \"fn\": 124, \"tp\": 854}\n      },\n      \"seed123\": {\n        \"accuracy\": 86.77,\n        \"f1_macro\": 86.77,\n        \"precision_fail\": 84.99,\n        \"recall_fail\": 88.16,\n        \"f1_fail\": 86.54,\n        \"precision_pass\": 88.56,\n        \"recall_pass\": 85.48,\n        \"f1_pass\": 86.99,\n        \"unparseable_rate\": 0.0,\n        \"best_checkpoint_step\": 956,\n        \"best_epoch\": 1,\n        \"total_steps\": 2868,\n        \"total_epochs\": 3,\n        \"train_batch_size\": 2,\n        \"training_time_min_approx\": 90,\n        \"confusion_matrix\": {\"tn\": 804, \"fp\": 108, \"fn\": 142, \"tp\": 836}\n      },\n      \"mean_accuracy\": 86.85,\n      \"mean_f1_macro\": 86.845,\n      \"std_accuracy\": 0.11,\n      \"std_f1_macro\": 0.11\n    },\n    \"CWM\": {\n      \"seed42\": {\n        \"accuracy\": 85.77,\n        \"f1_macro\": 85.73,\n        \"precision_fail\": 80.07,\n        \"recall_fail\": 93.86,\n        \"f1_fail\": 86.42,\n        \"precision_pass\": 93.18,\n        \"recall_pass\": 78.22,\n        \"f1_pass\": 85.05,\n        \"unparseable_rate\": 0.0,\n        \"best_checkpoint_step\": 956,\n        \"best_epoch\": 2,\n        \"total_steps\": 1434,\n        \"total_epochs\": 3,\n        \"train_batch_size\": 2,\n        \"training_time_min_approx\": 87,\n        \"generation_stats\": {\"mean\": 28.1, \"median\": 33.0, \"max\": 103, \"min\": 20},\n        \"confusion_matrix\": {\"tn\": 856, \"fp\": 56, \"fn\": 213, \"tp\": 765}\n      },\n      \"seed123\": {\n        \"accuracy\": 87.88,\n        \"f1_macro\": 87.88,\n        \"precision_fail\": 83.78,\n        \"recall_fail\": 92.87,\n        \"f1_fail\": 88.09,\n        \"precision_pass\": 92.61,\n        \"recall_pass\": 83.23,\n        \"f1_pass\": 87.67,\n        \"unparseable_rate\": 0.0,\n        \"best_checkpoint_step\": 956,\n        \"best_epoch\": 2,\n        \"total_steps\": 1434,\n        \"total_epochs\": 3,\n        \"train_batch_size\": 2,\n        \"training_time_min_approx\": 87,\n        \"generation_stats\": {\"mean\": 28.1, \"median\": 33.0, \"max\": 103, \"min\": 20},\n        \"confusion_matrix\": {\"tn\": 847, \"fp\": 65, \"fn\": 164, \"tp\": 814}\n      },\n      \"mean_accuracy\": 86.83,\n      \"mean_f1_macro\": 86.81,\n      \"std_accuracy\": 1.49,\n      \"std_f1_macro\": 1.52\n    }\n  },\n  \"roadmap_verification\": {\n    \"claimed_cls\": \"86.85±0.11%\",\n    \"actual_cls\": \"86.85±0.11%\",\n    \"cls_correct\": true,\n    \"claimed_cwm\": \"86.83±1.49%\",\n    \"actual_cwm\": \"86.83±1.49%\",\n    \"cwm_correct\": true\n  },\n  \"registry_discrepancy\": {\n    \"issue\": \"Registry claims deepseek-cls-func-s123 acc=87.88, actual is 86.77. The 87.88 belongs to deepseek-cwm-func-s123.\",\n    \"corrected_cls_s123_accuracy\": 86.77,\n    \"corrected_cwm_s123_accuracy\": 87.88\n  },\n  \"paper_table_data\": {\n    \"DeepSeek-6.7B_CLS_func\": {\n      \"accuracy_mean\": 86.85,\n      \"accuracy_std\": 0.11,\n      \"f1_mean\": 86.85,\n      \"f1_std\": 0.11,\n      \"unparseable_pct\": 0.0\n    },\n    \"DeepSeek-6.7B_CWM_func\": {\n      \"accuracy_mean\": 86.83,\n      \"accuracy_std\": 1.49,\n      \"f1_mean\": 86.81,\n      \"f1_std\": 1.52,\n      \"unparseable_pct\": 0.0\n    }\n  },\n  \"notes\": [\n    \"All experiments run on 4×RTX5090 (single GPU used per experiment)\",\n    \"CLS best checkpoints converge at epoch 1; CWM at epoch 2\",\n    \"CWM shows higher variance across seeds (std 1.49 vs 0.11)\",\n    \"CWM has asymmetric precision/recall: high precision_pass + high recall_fail pattern\",\n    \"Zero unparseable for all DeepSeek func-level experiments\"\n  ]\n}\n",
      "numLines": 134,
      "startLine": 1,
      "totalLines": 134
    }
  },
  "sourceToolAssistantUUID": "81f6b091-798c-4e9b-aae8-d59509faae75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T15:17:14.883Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Snf653uhgq5HRc6Lg89CtX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-repo_RUNNING_20260516T080524.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1de50cde-cdbb-466a-ba9f-9f128b334d36",
  "isSidechain": false,
  "requestId": "req_011Cb6UCLisPA33NeXGbsni5",
  "type": "assistant",
  "uuid": "13b994a4-9440-4fe3-ad2d-042725082006",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4UUChi6xdwo9hzAtjYTAw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11591,
      "cache_read_input_tokens": 68578,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11591,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 272,
          "cache_read_input_tokens": 68578,
          "cache_creation_input_tokens": 11591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11591
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

_source line 26 · 2026-05-16T15:17:15.275Z_

<details><summary>↩ Tool result · `toolu_01PuCBBKYCjSkSUYCBCSXXkJ`</summary>

```text
1	{
2	  "exp_id": "deepseek-traj-repo",
3	  "project": "exec-sim-repair-verifier",
4	  "state": "PREPARING",
5	  "previous_state": "PREPARING",
6	  "experiment_data": {
7	    "status": "PREPARING",
8	    "retry_count": 0,
9	    "created_at": "2026-05-16T14:42:01.929Z",
10	    "updated_at": "2026-05-16T14:42:01.929Z"
11	  },
12	  "timestamp": "2026-05-16T14:42:02.260339+00:00",
13	  "trigger": "update_registry"
14	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16352979-3ae4-44e8-a54e-6be4cfe20678",
  "isSidechain": false,
  "promptId": "f8c95270-2cda-4875-ab0f-f4534b23aa9f",
  "type": "user",
  "uuid": "b9a57245-a8cc-4469-b8a5-55c54d9b098a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-repo_PREPARING_20260516T144202.json",
      "content": "{\n  \"exp_id\": \"deepseek-traj-repo\",\n  \"project\": \"exec-sim-repair-verifier\",\n  \"state\": \"PREPARING\",\n  \"previous_state\": \"PREPARING\",\n  \"experiment_data\": {\n    \"status\": \"PREPARING\",\n    \"retry_count\": 0,\n    \"created_at\": \"2026-05-16T14:42:01.929Z\",\n    \"updated_at\": \"2026-05-16T14:42:01.929Z\"\n  },\n  \"timestamp\": \"2026-05-16T14:42:02.260339+00:00\",\n  \"trigger\": \"update_registry\"\n}",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  },
  "sourceToolAssistantUUID": "16352979-3ae4-44e8-a54e-6be4cfe20678",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-16T15:17:14.887Z_

<details><summary>↩ Tool result · `toolu_01Snf653uhgq5HRc6Lg89CtX`</summary>

```text
1	{
2	  "exp_id": "deepseek-cwm-repo",
3	  "project": "exec-sim-repair-verifier",
4	  "state": "RUNNING",
5	  "previous_state": "QUEUED",
6	  "experiment_data": {
7	    "status": "RUNNING",
8	    "retry_count": 0,
9	    "created_at": "2026-05-16T08:05:07.323Z",
10	    "updated_at": "2026-05-16T08:05:24.153Z",
11	    "spec": {
12	      "command": "CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 python3 train_unified.py --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/ --train_file swebench_full/swebench_train.jsonl --val_file swebench_full/swebench_val.jsonl --task cwm --lora_rank 16 --lora_alpha 32 --max_seq_length 2048 --epochs 3 --batch_size 2 --grad_accumulation 8 --lr 2e-4 --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/ --run_name deepseek-cwm-repo-s42",
13	      "server": "seetacloud-westd-4x5090",
14	      "data_path": "data/swebench_full/swebench_train.jsonl",
15	      "data_count": 70748,
16	      "model_name": "deepseek-coder-6.7b-instruct",
17	      "seed": 42
18	    }
19	  },
20	  "timestamp": "2026-05-16T08:05:24.933139+00:00",
21	  "trigger": "update_registry"
22	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13b994a4-9440-4fe3-ad2d-042725082006",
  "isSidechain": false,
  "promptId": "f8c95270-2cda-4875-ab0f-f4534b23aa9f",
  "type": "user",
  "uuid": "3e4bca02-bb42-4b2b-8ba2-4a657676a9c5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/deepseek-cwm-repo_RUNNING_20260516T080524.json",
      "content": "{\n  \"exp_id\": \"deepseek-cwm-repo\",\n  \"project\": \"exec-sim-repair-verifier\",\n  \"state\": \"RUNNING\",\n  \"previous_state\": \"QUEUED\",\n  \"experiment_data\": {\n    \"status\": \"RUNNING\",\n    \"retry_count\": 0,\n    \"created_at\": \"2026-05-16T08:05:07.323Z\",\n    \"updated_at\": \"2026-05-16T08:05:24.153Z\",\n    \"spec\": {\n      \"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 python3 train_unified.py --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/ --train_file swebench_full/swebench_train.jsonl --val_file swebench_full/swebench_val.jsonl --task cwm --lora_rank 16 --lora_alpha 32 --max_seq_length 2048 --epochs 3 --batch_size 2 --grad_accumulation 8 --lr 2e-4 --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/ --run_name deepseek-cwm-repo-s42\",\n      \"server\": \"seetacloud-westd-4x5090\",\n      \"data_path\": \"data/swebench_full/swebench_train.jsonl\",\n      \"data_count\": 70748,\n      \"model_name\": \"deepseek-coder-6.7b-instruct\",\n      \"seed\": 42\n    }\n  },\n  \"timestamp\": \"2026-05-16T08:05:24.933139+00:00\",\n  \"trigger\": \"update_registry\"\n}",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  },
  "sourceToolAssistantUUID": "13b994a4-9440-4fe3-ad2d-042725082006",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T15:17:15.272Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PuCBBKYCjSkSUYCBCSXXkJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/checkpoints/deepseek-traj-repo_PREPARING_20260516T144202.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e4bca02-bb42-4b2b-8ba2-4a657676a9c5",
  "isSidechain": false,
  "requestId": "req_011Cb6UCLisPA33NeXGbsni5",
  "type": "assistant",
  "uuid": "16352979-3ae4-44e8-a54e-6be4cfe20678",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4UUChi6xdwo9hzAtjYTAw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11591,
      "cache_read_input_tokens": 68578,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11591,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 272,
          "cache_read_input_tokens": 68578,
          "cache_creation_input_tokens": 11591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11591
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

_source line 29 · 2026-05-16T15:17:18.297Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also check the re-repair experiment results and the deepseek-cls-repo status.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9a57245-a8cc-4469-b8a5-55c54d9b098a",
  "isSidechain": false,
  "requestId": "req_011Cb6UCfkbsaYHLN4T3EYuz",
  "type": "assistant",
  "uuid": "4dc85aea-d59c-4232-9875-a104f22eb207",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzzgMgcapeB568CryJz81h",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3047,
      "cache_read_input_tokens": 80169,
      "output_tokens": 17096,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3047,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17096,
          "cache_read_input_tokens": 80169,
          "cache_creation_input_tokens": 3047,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3047
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

_source line 30 · 2026-05-16T15:22:56.530Z_

Now I have all the context needed. Let me produce the comprehensive median tier YAML.

Key actual data points to anchor predictions:
- DeepSeek func CLS: mean 86.85±0.11%, CWM: mean 86.83±1.49% → gap ≈ 0.02pp (essentially zero)
- DeepSeek traj-func-v2: s42=83.24%, s123=85.08%
- Re-repair phase0: control 0.82 ≈ cls_diag 0.818 (negative)
- deepseek-cls-repo: RUNNING, deepseek-cwm-repo: RUNNING
- deepseek-traj-repo/s123: PREPARING (unlikely to finish)

```yaml
tier: median
narrative_guidance: >
  C1 弱化为 "CLS provides a more robust verification formulation, with advantage magnitude
  modulated by model architecture"。DeepSeek 作为 directionally consistent secondary
  evidence（同方向、较小 effect size），不再 claim universal scaling law。C2 限定 Qwen-validated
  （5-seed TOST p=0.007 standalone 足够），DeepSeek func CLS≥TRAJ 仅作 suggestive evidence。
  C3 不受影响。Re-repair + cross-model TRAJ 列为 limitation/future work。新增 model-specific
  variation discussion section。Critical (3) downstream 和 (4) generalization 部分回应。
  目标 EMNLP Findings；Main 可能性低，reviewer 大概率要求更多 cross-model seeds。

imagined_experiments:

  ####################################################################
  # Claim 1 — Function-Level CLS vs CWM (Qwen, 已完成)
  ####################################################################

  - name: "CWM Generation Baseline (4B Function-Level)"
    plan_id: "cwm-baseline"
    description: "Qwen3-4B LoRA CWM vs CLS on function-level data, seed42"
    expected_results:
      cls_accuracy: 87.51
      cwm_accuracy: 87.51
      accuracy_gap_pp: 0.0
      cwm_exact_match_rate: 84.02
      cwm_unparseable: 0
    result_rationale: >
      Function-level execution output 短（通常 <50 tokens），CWM 不触发 token-budget exhaustion
      或 string-value prediction failure modes。4B 模型容量足以精确预测短输出。两种 formulation
      在此 complexity level 达到 identical accuracy（87.51%）。Exact match 84.02% < accuracy
      87.51% 的 3.49pp gap 暗示 CWM 有部分 output 不完全匹配但通过 pass/fail 判断逻辑仍然
      correct——这预示 repo-level 上 output matching 会更困难。Unparseable=0 因为 function-level
      输出格式统一简单。此 null result 是叙事基础：排除 "CLS trivially easier" 的 concern。
    tables:
      - name: "Table: Function-Level 4B CLS vs CWM (seed42)"
        columns: [Formulation, Accuracy, Pass F1, Fail F1, Exact Match, Unparseable%]
        rows:
          - [CLS, 87.51, 87.1, 87.9, N/A, 0]
          - [CWM, 87.51, 87.31, 87.71, 84.02, 0]
          - ["Δ (CLS−CWM)", 0.0, −0.21, 0.19, "—", 0]
    figures_description:
      - "Per-class F1 bar chart，CLS 与 CWM 几乎完全重叠"
    analysis: >
      Null result confirmed。CWM exact_match gap（3.49pp）是 repo-level catastrophic failure
      的早期信号。

  - name: "Multi-Seed Core Validation (5-seed, 4B)"
    plan_id: "multi-seed-core"
    description: "CLS 5-seed {42,123,456,789,0} + CWM 5-seed 统计"
    expected_results:
      cls_mean_accuracy: 88.43
      cls_std_accuracy: 0.76
      cwm_mean_accuracy: 87.19
      cwm_std_accuracy: 0.36
      mean_gap_pp: 1.24
      paired_t_p: 0.06
      significant_at_005: false
    result_rationale: >
      CLS 5-seed mean 88.43 vs CWM 87.19，gap 1.24pp。Paired t-test p≈0.06，α=0.05 下
      不显著。CLS variance (std 0.76) > CWM (std 0.36)：CLS 对 LoRA 初始化更敏感，binary
      classification 的 decision boundary 位置对 seed 更敏感；CWM 的 generation target 更
      deterministic。Seed123 是 CLS 的 outlier high（89.52）贡献了最大 pair gap。Median tier
      下 trend 存在但不 conclusive——task 太简单，两种 formulation 的 capacity 均已饱和。
    tables:
      - name: "Table: 4B 5-Seed CLS vs CWM"
        columns: [Seed, CLS Acc, CWM Acc, Gap(pp)]
        rows:
          - [42, 87.83, 87.51, 0.32]
          - [123, 89.52, 87.20, 2.32]
          - [456, 87.88, 86.98, 0.90]
          - [789, 89.00, 86.67, 2.33]
          - [0, 87.94, 87.57, 0.37]
          - ["Mean±Std", "88.43±0.76", "87.19±0.36", 1.24]
    figures_description:
      - "5-seed accuracy dot plot with mean±std bars，CLS 蓝色、CWM 橙色"
    analysis: >
      p≈0.06 处于 borderline。Paper 报告为 "directional trend (p=0.06) at 4B, becomes
      significant at 8B"，building scaling narrative。

  - name: "Trace-then-Judge Ablation"
    plan_id: "trace-then-judge"
    description: "Chain-of-thought style: generate reasoning trace → pass/fail"
    expected_results:
      training_status: failed
      reason: "output format instability, training diverged"
    result_rationale: >
      4B LoRA 同时学习生成 reasoning trace 和 predict pass/fail，两个 objective 竞争有限
      capacity。Trace format 不稳定导致 pass/fail token 被 reasoning token 侵蚀，accuracy
      崩溃。不是 fundamental impossibility 而是 engineering/capacity 问题。Median tier 下
      dropped from paper，brief mention in limitations。
    tables: []
    figures_description: []
    analysis: >
      不影响 core claims。8B scaling evidence 间接 addresses "CLS 优势来自 skipping reasoning"
      的 concern。

  ####################################################################
  # Claim 1 — Model Size Scaling (Qwen 8B, 已完成)
  ####################################################################

  - name: "Model Size Scaling (8B, 3-seed)"
    plan_id: "model-size-scaling"
    description: "CLS vs CWM at 8B scale, seeds {42, 123, 456}"
    expected_results:
      cls8b_mean_accuracy: 89.40
      cwm8b_mean_accuracy: 86.96
      mean_gap_pp: 2.43
      per_seed_gaps: {s42: 2.81, s123: 2.42, s456: 2.07}
      cls_4b_to_8b_gain_pp: 0.97
      cwm_4b_to_8b_gain_pp: -0.23
    result_rationale: >
      8B CLS (89.40) vs CWM (86.96) gap 扩大到 2.43pp，所有 3 个 seed 方向一致（2.07–2.81pp）。
      关键 asymmetry：CLS 从 4B→8B 提升 0.97pp 但 CWM 下降 0.23pp。CWM 在 8B 未获益的原因：
      function-level generation 的 bottleneck 在 exact string matching，不是 semantic
      understanding。额外 8B capacity 没有 reduce string matching error。CLS 则从 extra
      capacity 中获益：binary classification 的 decision boundary 在高维 space 中变得更 smooth。
      Median tier：2.43pp 被接受为 real but modest。
    tables:
      - name: "Table: 8B 3-Seed Scaling"
        columns: [Size, CLS Mean Acc, CWM Mean Acc, Gap(pp)]
        rows:
          - ["4B (5-seed)", 88.43, 87.19, 1.24]
          - ["8B (seed42)", 90.48, 87.67, 2.81]
          - ["8B (seed123)", 89.40, 86.98, 2.42]
          - ["8B (seed456)", 88.31, 86.24, 2.07]
          - ["8B (3-seed mean)", 89.40, 86.96, 2.43]
    figures_description:
      - "Scaling plot: x=model size, y=accuracy，CLS 和 CWM 两条线，8B 处 diverge"
    analysis: >
      8B gap consistent across seeds 是 function-level 最强 C1 evidence。但 2.43pp 在
      absolute terms 仍 modest，frame 为 "scaling direction" 而非 "large effect"。

  ####################################################################
  # Claim 1 — Repo-Level (Qwen, 已完成)
  ####################################################################

  - name: "Repo-Level Training (Qwen CLS + CWM, multi-attempt)"
    plan_id: "repo-level-training"
    description: "Qwen 4B/8B repo-level CLS 多 checkpoint + CWM 10+ attempts"
    expected_results:
      cls_4b_best: {accuracy: 82.35, f1_macro: 74.74, fail_f1: 60.87, unparseable_pct: 1.3}
      cls_8b_best: {accuracy: 84.79, f1_macro: 81.18, fail_f1: 72.93, unparseable_pct: 0}
      cls_8b_seed123: {accuracy: 85.60, fail_f1: 65.89}
      cwm_best_v10: {accuracy: 69.91, unparseable_pct: 93.0, fail_f1: 11.54}
      cwm_best_v12: {accuracy: 58.04, unparseable_pct: 53.7}
    result_rationale: >
      Repo-level CLS 在 median range 内：8B best 84.79%，multi-seed mean ~85%。Fail_f1
      ~69-73% 在 [60,72] 上缘。Minority class (fail) 预测弱是因为 repo-level code 长
      (2800+ tokens) 使模型难以精确定位 failure cause。CWM catastrophic failure 核心原因：
      repo-level execution output 极长（tracebacks、assertion details），generation model
      无法 produce matching output。Max_new_tokens=64(v10) 导致 93% unparseable；放宽到
      1024 tokens(v11) 仍 75.2% unparseable。Median tier 核心 tension：CWM failure 是
      formulation limitation 还是 implementation issue？Paper 需 honest discussion：即使
      generous token budget，CWM unparseable >50%，suggesting formulation-level difficulty。
    tables:
      - name: "Table: Complexity-Dependent Formulation Gap"
        columns: [Level, CLS Best Acc, CWM Best Acc, CWM Unparseable%]
        rows:
          - ["Function (4B)", 87.51, 87.51, 0]
          - ["Function (8B)", 90.48, 87.67, 0]
          - ["Repo (4B)", 82.35, 69.91, 93.0]
          - ["Repo (8B)", 84.79, "—(failed)", "—"]
    figures_description:
      - "Function vs Repo level CLS/CWM gap visualization"
      - "CWM unparseable rate across 10+ training attempts"
    analysis: >
      Framing 必须是 "CLS works where CWM fails" 而非 "CLS beats CWM"——CWM 没有 fair
      comparison point。Show multiple CWM attempts with different configs 证明 unparseable
      rate persists despite engineering effort。

  - name: "Repo-Level CLS Mutation-Type Analysis (8B)"
    plan_id: "repo-mutation-analysis"
    description: "Per-mutation-type accuracy breakdown for repo-level CLS 8B"
    expected_results:
      overall_accuracy: 84.48
      gold_accuracy: 96.24
      operator_swap: 81.38
      off_by_one: 86.89
      return_value: 75.44
      boundary_removal: 46.90
      seed123_boundary_removal: 44.90
    result_rationale: >
      Boundary_removal 极低（46.9%）——接近 random guessing。这类 mutation 移除 if/while
      条件判断，代码行为大幅改变但模型难以仅从 code+test text 判断影响。Return_value 也低
      （75.4%）因为 repo-level 函数调用链更长。Gold accuracy 高（96-99%）说明模型对未
      mutated code 判断 reliable。Boundary_removal（占 test set 10.7%）严重拖低整体
      fail detection。
    tables:
      - name: "Table: Repo-Level CLS 8B Mutation Breakdown"
        columns: [Mutation Type, Acc(s42), Acc(s123)]
        rows:
          - ["Gold (no mutation)", 96.24%, 99.60%]
          - [operator_swap, 81.38%, 82.60%]
          - [off_by_one, 86.89%, 79.20%]
          - [return_value, 75.44%, 66.40%]
          - [boundary_removal, 46.90%, 44.90%]
    figures_description:
      - "Radar chart: mutation-type accuracy across models (func 4B, repo 4B, repo 8B)"
    analysis: >
      Boundary_removal 是 Achilles heel，模型需 execution-like reasoning 才能判断。
      部分 validates CWM approach（predicting execution）for specific mutation types。

  ####################################################################
  # Claim 1 — LLM-as-Judge Baselines (已完成)
  ####################################################################

  - name: "LLM-as-Judge Zero-Shot Baselines"
    plan_id: "llm-judge-baseline"
    description: "Qwen3-8B 和 32B NF4 zero-shot judge baselines"
    expected_results:
      judge_8b_accuracy: 64.4
      judge_32b_accuracy: 71.69
      finetuned_4b_accuracy: 87.51
      finetuned_vs_judge_32b_gap_pp: 15.82
    result_rationale: >
      Zero-shot judges 极端 biased toward "fail"：8B fail_recall 95.8% 但 pass_recall
      仅 35.1%。模型的 zero-shot heuristic 是 "mutated code = broken"，几乎不考虑
      mutation 是否 actually affects test outcome。Fine-tuned 4B (87.51%) >> 32B zero-shot
      (71.69%)，gap 15.82pp：8x 更大的零训练模型仍不如 4x 更小的微调模型。
    tables:
      - name: "Table: Fine-Tuned vs Zero-Shot"
        columns: [Model, Method, Per-Test Acc, Fail F1, Pass F1]
        rows:
          - ["Qwen3-4B", "Fine-tuned CLS", 87.51, 87.86, 87.15]
          - ["Qwen3-8B", "Zero-shot", 64.4, 72.2, 50.5]
          - ["Qwen3-32B NF4", "Zero-shot", 71.69, 75.91, 65.68]
          - [Majority, Baseline, 51.7, "—", "—"]
    figures_description:
      - "Accuracy-compute Pareto frontier: fine-tuned CLS dominates"
    analysis: >
      Confirms fine-tuning necessity。Reviewer 可能 ask for few-shot 或 chain-of-thought
      baselines as additional reference。

  ####################################################################
  # Claim 2 — Per-Test vs Trajectory Equivalence (Qwen, 已完成)
  ####################################################################

  - name: "Trajectory-Level Fine-tuned Baseline (5-seed)"
    plan_id: "traj-level-finetuned"
    description: "4B LoRA trained on resolved/unresolved prediction, 5 seeds"
    expected_results:
      mean_accuracy: 86.30
      std_accuracy: 0.93
      mean_consistency: 78.72
      per_seed: {s42: 85.66, s123: 85.47, s456: 87.40, s789: 87.31, s0: 85.66}
    result_rationale: >
      Trajectory-level mean 86.30% vs per-test CLS 88.43%，gap 2.13pp。主要来源：
      (1) trajectory-level 每个 problem 只产生 1 个训练样本 vs per-test 产生 T 个，effective
      training data 量更少；(2) resolved 需要 ALL tests pass——conjunctive logic 比
      per-test individual 判断更难学。Consistency ~78% 说明同一 problem 内 per-test
      predictions 有 ~22% 不一致。
    tables:
      - name: "Table: Trajectory-Level 5-Seed Results"
        columns: [Seed, Accuracy, Resolved F1, Unresolved F1, Consistency%]
        rows:
          - [42, 85.66, 83.18, 87.50, 79.94]
          - [123, 85.47, 83.52, 87.00, 78.59]
          - [456, 87.40, 85.80, 88.70, 78.80]
          - [789, 87.31, 86.17, 88.27, 76.74]
          - [0, 85.66, 83.41, 87.37, 79.55]
          - ["Mean±Std", "86.30±0.93", "84.42±1.36", "87.77±0.68", "78.72±1.25"]
    figures_description: []
    analysis: >
      Per-test ≥ trajectory at variant-level。TOST equivalence test 更 rigorously quantifies。

  - name: "5-Seed Paired Clustered Bootstrap (TOST Equivalence)"
    plan_id: "5-paired-clustered-bootstrap"
    description: "Per-test vs trajectory-level TOST equivalence with clustered bootstrap"
    expected_results:
      pooled_gap_pp: -0.45
      pooled_ci: [-1.71, 0.84]
      tost_p_value: 0.0071
      tost_margin_pp: 2.0
      equivalence_confirmed: true
      per_seed_gaps: {s42: -0.97, s123: 1.45, s456: -1.84, s789: -0.78, s0: -0.29}
      n_clusters: 114
    result_rationale: >
      TOST p=0.007 << 0.05 confirms per-test ≈ trajectory within ±2pp margin。CI
      [-1.71, +0.84] width=2.55pp 在 median range [1.5, 3.0]——sufficiently narrow to
      confirm equivalence but not extremely tight。Per-seed gaps 从 -1.84 到 +1.45：
      方向不一致，3 seeds per-test worse, 1 seed per-test better, 1 near-zero。This
      inconsistency IS the equivalence signal——if one formulation were systematically
      better, gaps would be consistently one-sided。±2pp margin justification：with
      ICC=0.191 and DEFF=3.97，2pp is practical significance threshold。
    tables:
      - name: "Table: Per-Test vs Trajectory Equivalence"
        columns: [Seed, "Gap (per-test − traj, pp)", Direction]
        rows:
          - [42, -0.97, "Traj better"]
          - [123, 1.45, "Per-test better"]
          - [456, -1.84, "Traj better"]
          - [789, -0.78, "Traj better"]
          - [0, -0.29, "Traj better"]
          - [Pooled, "−0.45 [−1.71, +0.84]", "TOST p=0.007"]
    figures_description:
      - "Forest plot: per-seed gaps with pooled CI, ±2pp TOST bounds as dotted verticals"
    analysis: >
      Claim 2 的 methodological cornerstone。TOST at p=0.007 是 paper 最 rigorous
      statistical result 和 primary contribution。

  ####################################################################
  # Claim 2 — Per-Test Diagnostic Quality (已完成)
  ####################################################################

  - name: "Per-Test Precision/Recall Analysis"
    plan_id: "per-test-precision-recall"
    description: "Per-test failure prediction quality on function-level test set"
    expected_results:
      accuracy: 87.51
      fail_precision: 82.75
      fail_recall: 93.64
      fail_f1: 87.86
      pass_precision: 93.24
      pass_recall: 81.80
      FP_count: 58
      FN_count: 178
      best_mutation: "return_value (97.26%)"
      worst_mutation: "off_by_one (82.56%)"
    result_rationale: >
      模型显著 biased toward predicting fail：fail_recall(93.64%) >> pass_recall(81.80%)。
      Training data 中 mutation 几乎都导致 fail，模型学到 conservative prior。FP:FN = 58:178
      → 75.4% of errors are false negatives (miss actual fails)。这 quantifies CLS 的
      characteristic failure mode。Return_value 最容易（97.26%）因为 output 大幅改变；
      off_by_one 最难（82.56%）因为 subtle numerical reasoning。
    tables:
      - name: "Table: Per-Test Diagnostic Quality"
        columns: [Class, Precision, Recall, F1]
        rows:
          - ["Fail (bug detected)", 82.75, 93.64, 87.86]
          - ["Pass (correct code)", 93.24, 81.80, 87.15]
    figures_description:
      - "Confusion matrix heatmap"
      - "Accuracy by mutation type + test count bucket grouped bar chart"
    analysis: >
      Error asymmetry (75% FN) 与 CWM 的 complementary failure mode (83% FP) 形成对比，
      支持 oracle ensemble 叙事。

  ####################################################################
  # Claim 3 — Oracle & Characterization (已完成)
  ####################################################################

  - name: "Oracle F2P-Stratified Analysis"
    plan_id: "oracle-f2p-stratified"
    description: "Per-test advantage breakdown by FAIL_TO_PASS test count"
    expected_results:
      T1_pct: 68.7
      T1_block_adv: -0.09
      T2_pct: 19.1
      T2_block_adv: 31.69
      T3_5_pct: 7.1
      T3_5_block_adv: 40.74
      T6plus_pct: 5.1
      T6plus_block_adv: 40.06
      overall_block_adv: 10.93
      T2_contribution_pct: 55.3
    result_rationale: >
      T=1 时 per-test ≡ trajectory-level（只有一个 fail test），advantage ≈ 0。T=2 时
      跳到 31.69pp(block)：trajectory-level 把两个 tests 合并为一个 binary 判断，丢失
      which test failed 信息；per-test 分别预测可 partial credit。T≥3 plateau ~40pp
      因为 marginal tests 的信息增量递减。T2 贡献 55.3% 因为它是最大 multi-test bucket
      (19.1%) 且 advantage 显著。SWE-bench 68.7% T=1 限制了 population-level impact，
      但 targeting T≥2 subset (31.3%) 时 per-test 显著优于 trajectory。
    tables:
      - name: "Table: Oracle Per-Test Advantage by F2P Count"
        columns: [T, "% Instances", "Block Adv (pp)", "Contribution"]
        rows:
          - ["T=1", 68.7, -0.09, "−0.6%"]
          - ["T=2", 19.1, 31.69, "55.3%"]
          - ["T=3−5", 7.1, 40.74, "26.4%"]
          - ["T≥6", 5.1, 40.06, "18.7%"]
          - [Overall, 100, 10.93, "100%"]
    figures_description:
      - "Stacked bar: per-test advantage by T bucket with instance % overlay"
    analysis: >
      Claim 3 的 primary evidence。Actionable finding：deploy per-test only when T≥2。
      This characterization 是 paper 最 unique contribution in median tier。

  - name: "Oracle Total (F2P+P2P) Validation"
    plan_id: "oracle-total-validated"
    description: "When P2P regression detection adds value vs hurts"
    expected_results:
      total_reg5pct: {block_adv: -0.005, beneficial: false}
      total_reg10pct: {block_adv: 0.083, beneficial: true}
      total_reg20pct: {block_adv: 0.278, beneficial: true}
      empirical_p2p_regression_rate: 0.01
    result_rationale: >
      Empirical P2P regression rate 仅 ~1%，远低于 10% breakeven threshold。5% regression
      下 per-test P2P monitoring 实际 HURTS（-0.005pp）：false positive P2P predictions
      导致 correct patches 被 wrongly rejected。当前 SWE-bench patch 质量高，几乎不
      break passing tests。This is negative but highly informative finding。
    tables:
      - name: "Table: P2P Regression Threshold"
        columns: [Regression Rate, "Block Adv (pp)", Beneficial?]
        rows:
          - ["1% (empirical)", "≈0", "No"]
          - ["5%", -0.005, "No"]
          - ["10%", 0.083, "Yes"]
          - ["20%", 0.278, "Yes"]
    figures_description:
      - "Regression rate vs per-test advantage curve with breakeven point"
    analysis: >
      Honest negative finding。Strengthens credibility by showing nuanced analysis。

  - name: "Block Correlation Empirical Validation"
    plan_id: "block-corr-empirical"
    description: "Measured ICC and design effect from trained model predictions"
    expected_results:
      icc: 0.1909
      design_effect: 3.9676
      all_correct_ratio: 2.81
      error_std_ratio: 1.89
    result_rationale: >
      ICC=0.191 说明 19.1% 的 prediction error variance 是 between-problem（problem-level
      effect）。显著高于 iid 的 0%（p<0.001）但远低于 full block（ICC=1.0）。Design effect
      3.97 意味着 effective sample size = nominal/3.97，justifies ±2pp TOST margin。
      All-correct ratio 2.81x：模型对某些 problems consistently correct（简单 patterns），
      对另一些 consistently wrong（complex logic）——errors 不是 random per-test。
    tables:
      - name: "Table: Error Correlation Validation"
        columns: [Metric, Observed, IID Expected, Ratio]
        rows:
          - ["All-correct problems", 46, 16.35, "2.81×"]
          - ["Error rate std", 0.153, 0.081, "1.89×"]
          - [ICC, 0.191, 0, "—"]
          - [Design Effect, 3.97, 1.0, "3.97×"]
    figures_description:
      - "Per-problem error rate distribution: observed vs IID-expected histogram"
    analysis: >
      Realistic per-test advantage 在 IID 和 block curves 之间，closer to IID 端。Paper
      应 present both bounds with empirical ICC as arbitrator。

  - name: "CLS/CWM Error Complementarity Analysis"
    plan_id: "error-overlap"
    description: "CLS vs CWM error overlap on function-level (seed42, n=1890)"
    expected_results:
      both_correct_pct: 84.71
      cls_only_correct_pct: 3.12
      cwm_only_correct_pct: 2.80
      both_wrong_pct: 9.37
      oracle_ensemble_accuracy: 90.63
      cls_error_mode: "miss bugs (FN dominant, 75.4%)"
      cwm_error_mode: "false alarms (FP dominant, 83.1%)"
    result_rationale: >
      CLS-only correct (3.12%) ≈ CWM-only correct (2.80%) 说明两种 formulation 有近乎
      equal but different 错误区域。Oracle ensemble 90.63% 远高于 either alone (87.51%)。
      Error mode complementarity 是 structural：CLS binary decision boundary 和 CWM
      string matching 在不同 case types 上 fail。Off_by_one 最 complementary（CWM-only
      4.8%），return_value 最不 complementary（96.8% both correct）。
    tables:
      - name: "Table: Error Overlap (4B, seed42)"
        columns: [Category, Count, "%"]
        rows:
          - [Both correct, 1601, "84.71%"]
          - [CLS-only correct, 59, "3.12%"]
          - [CWM-only correct, 53, "2.80%"]
          - [Both wrong, 177, "9.37%"]
          - [Oracle ensemble, "—", "90.63%"]
    figures_description:
      - "Venn diagram: CLS vs CWM error overlap"
    analysis: >
      Oracle ensemble 90.63% 是 supplementary selling point。Framing: formulation
      diversity as a verification strategy。

  ####################################################################
  # Claim 2 — Per-Test Majority Voting (已完成, 负面)
  ####################################################################

  - name: "Per-Test Majority Voting (K=3)"
    plan_id: "per-test-majority-voting"
    description: "Self-consistency K=3 on per-test classification"
    expected_results:
      accuracy_greedy: 87.51
      accuracy_mv_k3: 86.83
      delta_pp: -0.69
      net_flips: -13
    result_rationale: >
      Majority voting hurt accuracy by 0.69pp。93.3% 的 predictions 是 unanimous——
      model 高度 confident，disagreement 仅 6.7% of samples。These borderline cases
      voting 后 net -13 flips，greedy 比 random among alternatives 更好。Per-test
      classification 是 discrimination task where greedy decoding 已 capture optimal
      decision boundary。4x compute cost for worse accuracy → MV strictly dominated。
    tables:
      - name: "Table (Appendix): Majority Voting"
        columns: [Method, Accuracy, "Time(s)", Net Flips]
        rows:
          - ["Greedy (K=1)", 87.51, 30, "—"]
          - ["Majority (K=3)", 86.83, 120, −13]
    figures_description: []
    analysis: >
      Negative result in appendix。Self-consistency 不适用于 well-calibrated binary classifiers。

  ####################################################################
  # Cross-Model — DeepSeek Function-Level (CLS + CWM, 已完成)
  ####################################################################

  - name: "DeepSeek Function-Level CLS (2-seed)"
    plan_id: "deepseek-cls-func"
    description: "DeepSeek-Coder-6.7B-Instruct LoRA CLS, seeds {42, 123}"
    expected_results:
      seed42_accuracy: 86.93
      seed123_accuracy: 86.77
      mean_accuracy: 86.85
      std_accuracy: 0.11
      vs_qwen_4b_cls_mean_gap_pp: -1.58
    result_rationale: >
      DeepSeek CLS mean 86.85% 低于 Qwen 4B mean 88.43% 约 1.58pp。差距来自：
      (1) LoRA hyperparameters 为 Qwen 优化过，DeepSeek 可能需要不同 rank/lr；
      (2) tokenizer 差异影响 code representation；(3) instruction format 差异。
      Cross-seed 极稳定（std 0.11），说明 CLS 在 DeepSeek 上 highly reproducible。
      Median tier：confirms CLS cross-architecture generalizability，performance 水平
      在预期范围（5-12pp gap 的下界附近）。
    tables: []
    figures_description: []
    analysis: >
      Cross-architecture CLS works with small performance gap。

  - name: "DeepSeek Function-Level CWM (2-seed)"
    plan_id: "deepseek-cwm-func"
    description: "DeepSeek-Coder-6.7B-Instruct LoRA CWM, seeds {42, 123}"
    expected_results:
      seed42_accuracy: 85.77
      seed123_accuracy: 87.88
      mean_accuracy: 86.83
      std_accuracy: 1.49
      vs_deepseek_cls_mean_gap_pp: -0.02
    result_rationale: >
      DeepSeek CWM mean 86.83% vs CLS 86.85%，gap 仅 0.02pp——essentially zero。
      但 cross-seed 方向不一致：seed42 CLS>CWM by 1.16pp，seed123 CWM>CLS by 1.11pp。
      CWM variance (std 1.49) >> CLS (std 0.11)：CWM 对 seed 极敏感，generation
      precision 受初始化影响大。Zero unparseable，function-level output 足够短。
      ds_func_cls_cwm_gap_pp 实际值 0.02 在 [-0.5, 1.5] range 内。这个结果 undermines
      "CLS universally better" narrative——在 DeepSeek 上 formulation advantage 消失。
    tables:
      - name: "Table: DeepSeek Function-Level CLS vs CWM"
        columns: [Seed, CLS Acc, CWM Acc, "Gap(CLS−CWM)"]
        rows:
          - [42, 86.93, 85.77, "+1.16"]
          - [123, 86.77, 87.88, "−1.11"]
          - ["Mean±Std", "86.85±0.11", "86.83±1.49", "+0.02"]
    figures_description:
      - "Cross-model CLS-CWM gap comparison: Qwen vs DeepSeek"
    analysis: >
      DeepSeek CLS≈CWM 是 median tier defining result。Paper 必须 acknowledge CLS
      advantage may be Qwen-specific rather than formulation-universal。新增 "model-
      specific variation" discussion section。

  ####################################################################
  # Cross-Model — DeepSeek Function-Level TRAJ (已完成)
  ####################################################################

  - name: "DeepSeek Function-Level Trajectory (2-seed, v2)"
    plan_id: "deepseek-traj-func-v2"
    description: "DeepSeek-Coder-6.7B trajectory-level resolved/unresolved, seeds {42, 123}"
    expected_results:
      seed42_accuracy: 83.24
      seed123_accuracy: 85.08
      seed123_consistency: 78.20
      mean_accuracy: 84.16
      cls_vs_traj_gap_seed42_pp: 3.69
      cls_vs_traj_gap_seed123_pp: 1.69
      mean_cls_traj_gap_pp: 2.69
    result_rationale: >
      DeepSeek TRAJ mean 84.16% vs CLS 86.85%，gap 2.69pp（CLS better）。在
      ds_cls_traj_variant_abs_gap_pp: [2, 5] range 内。方向与 Qwen 一致（CLS ≥ TRAJ）
      但 gap 更小。Seed 间差异大（s42: 3.69pp vs s123: 1.69pp）反映 trajectory-level
      对 seed 敏感。Consistency 78.2% 与 Qwen traj（~79%）相当。这为 C2 提供
      directionally consistent cross-model evidence，但仅 2 seeds 且 gap 不稳定，
      只能作 "suggestive" 而非 "confirmatory"。
    tables:
      - name: "Table: DeepSeek CLS vs TRAJ (Function-Level)"
        columns: [Seed, CLS Acc, TRAJ Acc, "Gap(pp)"]
        rows:
          - [42, 86.93, 83.24, 3.69]
          - [123, 86.77, 85.08, 1.69]
          - [Mean, 86.85, 84.16, 2.69]
    figures_description:
      - "Cross-model CLS≥TRAJ gap comparison: Qwen 5-seed vs DeepSeek 2-seed"
    analysis: >
      Supports C2 directionally. CLS≥TRAJ on DeepSeek 仅作 suggestive evidence，
      不足以 claim cross-model equivalence。Paper note: "2-seed DeepSeek results are
      directionally consistent but insufficient for formal equivalence testing."

  ####################################################################
  # Cross-Model — DeepSeek Repo-Level CLS (RUNNING → median prediction)
  ####################################################################

  - name: "DeepSeek Repo-Level CLS"
    plan_id: "deepseek-cls-repo"
    description: "DeepSeek-Coder-6.7B fine-tuned CLS on repo-level SWE-bench data"
    expected_results:
      accuracy: 74.5
      f1_macro: 65.2
      fail_f1: 52.8
      pass_f1: 77.6
      unparseable_pct: 2.5
      majority_baseline: 73.0
      gap_vs_baseline_pp: 1.5
    result_rationale: >
      Median tier 核心假设 ds_repo_cls_acc_pct: [70, 78]，取中点 74.5%。低于 Qwen 4B
      (82.35%) 约 7.85pp 和 Qwen 8B (84.79%) 约 10.3pp，在 "低于 Qwen 同配置 5-12pp"
      range 内。DeepSeek 在 repo-level 表现更差的原因：(1) 6.7B 参数中 code-specialized
      但非 instruction-following 导向的 dense model vs Qwen3 更均衡的 architecture；
      (2) tokenizer 对 long repo-level context 效率差异——DeepSeek tokenizer 产生更多
      tokens 导致更早 truncation；(3) LoRA config 未针对 repo-level 调优（rank=16
      可能不够）。Gap vs majority baseline 仅 1.5pp 说明模型勉强 above chance，
      learn meaningful signal 但 generalization 弱。Unparseable ~2.5% 略高于 Qwen
      因为 tokenizer edge cases。这个结果是 "directionally consistent secondary
      evidence"——CLS 在 DeepSeek repo-level 可用但明显更弱。
    tables:
      - name: "Table: Cross-Architecture Repo-Level CLS"
        columns: [Model, Accuracy, Fail F1, Unparseable%, "Gap vs Majority"]
        rows:
          - ["Qwen3-4B (best seed)", 82.35, 60.87, 1.3, 9.39]
          - ["Qwen3-8B (best seed)", 84.79, 72.93, 0, 11.84]
          - ["DeepSeek-6.7B", "~74.5", "~52.8", "~2.5", "~1.5"]
    figures_description:
      - "Cross-architecture repo-level CLS accuracy comparison bar chart"
    analysis: >
      DeepSeek repo CLS 可用但弱。Confirms CLS formulation generalizes across
      architectures but performance level is model-dependent。Paper: single row
      in results table，not highlighted as strong evidence。

  ####################################################################
  # Cross-Model — DeepSeek Repo-Level CWM (RUNNING → median prediction)
  ####################################################################

  - name: "DeepSeek Repo-Level CWM"
    plan_id: "deepseek-cwm-repo"
    description: "DeepSeek-Coder-6.7B CWM on repo-level, max_seq_length=2048"
    expected_results:
      accuracy_all: 68.2
      unparseable_pct: 27.0
      parseable_subset_accuracy: 71.5
      parseable_subset_fail_f1: 48.3
      f1_macro_all: 54.8
      majority_baseline: 73.0
      gap_vs_cls_pp: 6.3
    result_rationale: >
      Median tier 核心假设 ds_repo_cwm_unparseable_pct: [15, 40]，取 ~27%。远低于
      Qwen CWM 的 53-93% unparseable rate。DeepSeek CWM 在 repo-level partially
      parseable 的原因：DeepSeek-Coder 在 code generation pretraining 更强，generation
      capability 转移到 execution output prediction。但仍有 27% unparseable 因为
      repo-level output 长度超出 max_new_tokens 限制和 format complexity。

      Parseable subset accuracy ~71.5% 在 [60, 72] 上界——parseable 的 cases 是
      output 较短/格式较规范的 easier subset，selection bias 使 accuracy 偏高。
      CLS-CWM gap ~6.3pp 在 ds_repo_cls_cwm_gap_pp [5, 12] 内，方向与 Qwen 一致
      （CLS > CWM）但幅度大幅缩小：Qwen 上 CLS 82.35% vs CWM catastrophic failure
      (unparseable >50%)，gap 是 qualitative；DeepSeek 上 gap 是 quantitative 6.3pp。

      这是 median tier 的关键结果："CLS-CWM gap 方向一致但幅度缩小"，使得 C1 不能
      claim universal large gap，只能说 "advantage magnitude modulated by architecture"。
    tables:
      - name: "Table: DeepSeek Repo-Level CLS vs CWM"
        columns: [Formulation, Accuracy, Fail F1, Unparseable%, "Parseable Acc"]
        rows:
          - [CLS, "~74.5", "~52.8", "~2.5", "—"]
          - ["CWM (all)", "~68.2", "~36", "~27", "~71.5"]
          - ["CWM (parseable only)", "—", "~48.3", 0, "~71.5"]
          - ["Δ (CLS−CWM all)", "~6.3pp", "—", "—", "—"]
      - name: "Table: Cross-Model Repo-Level CWM Comparison"
        columns: [Model, Unparseable%, Parseable Subset Acc, Overall Acc]
        rows:
          - ["Qwen3-4B (v10)", 93.0, "N/A (too few)", 69.91]
          - ["Qwen3-4B (v12)", 53.7, "~65", 58.04]
          - ["DeepSeek-6.7B", "~27", "~71.5", "~68.2"]
    figures_description:
      - "CWM unparseable rate comparison: Qwen vs DeepSeek (repo-level)"
      - "CLS-CWM gap magnitude: function-level → repo-level, Qwen vs DeepSeek"
    analysis: >
      DeepSeek CWM repo partially works（27% unparseable vs Qwen 53-93%），缩小了
      CLS-CWM gap。这削弱了 "CWM fundamentally fails at repo-level" 的叙事，reviewer
      可能 argue Qwen CWM failure 是 model-specific 而非 formulation-inherent。Paper
      需要 reframe："CWM viability is architecture-dependent; CLS provides more
      consistent performance across architectures."

  ####################################################################
  # Cross-Model — DeepSeek TRAJ Repo (PREPARING → won't complete)
  ####################################################################

  - name: "DeepSeek Repo-Level Trajectory (seed42)"
    plan_id: "deepseek-traj-repo"
    description: "DeepSeek-Coder-6.7B trajectory-level on repo-level SWE-bench"
    expected_results:
      status: "not_completed"
      reason: "data preparation + training pipeline for DeepSeek repo TRAJ not finalized before ARR May 25 deadline"
      estimated_training_time_hours: 18
      deadline_gap_days: -5
    result_rationale: >
      Median tier 核心假设："DeepSeek TRAJ repo 未能在 ARR May 25 前完成"。原因：
      (1) repo-level trajectory data 需要重新构建（aggregate per-test labels to
      per-problem resolved/unresolved），DeepSeek-specific preprocessing pipeline
      未就绪；(2) 截止日仅剩 ~9 天（2026-05-25），deepseek-cls-repo 和 cwm-repo 还在
      RUNNING，traj-repo 排在它们后面；(3) 即使训练完成，还需 eval + checkpoint sweep
      + 统计分析，时间不够。这意味着 C2 的 cross-model validation 缺失——只有 Qwen
      5-seed TOST (p=0.007) 和 DeepSeek function-level suggestive evidence。
    tables: []
    figures_description: []
    analysis: >
      C2 cross-model TRAJ 缺失是 median tier 最大的 limitation。Paper 必须 explicitly
      state: "Cross-model trajectory-level equivalence testing is left to future work
      due to computational constraints." Reviewer 大概率要求补充。

  - name: "DeepSeek Repo-Level Trajectory (seed123)"
    plan_id: "deepseek-traj-repo-s123"
    description: "DeepSeek-Coder-6.7B trajectory-level on repo-level, seed123"
    expected_results:
      status: "not_completed"
      reason: "blocked by seed42 not starting; both require deepseek-traj-repo data pipeline"
    result_rationale: >
      依赖 deepseek-traj-repo 的 data pipeline 和 training infrastructure。Seed123
      只能在 seed42 验证 pipeline 正确后启动。两者都 stuck in PREPARING。
    tables: []
    figures_description: []
    analysis: >
      同上，C2 cross-model evidence 缺失的一部分。

  ####################################################################
  # Downstream — SWE-bench PerTest Dataset (planned → median prediction)
  ####################################################################

  - name: "SWE-bench PerTest Dataset Construction"
    plan_id: "swebench-pertest-data"
    description: "Docker re-evaluation of 500 SWE-bench Verified instances × 16 candidates"
    expected_results:
      target_instances: 500
      successful_instances: 435
      failed_instances: 65
      success_rate_pct: 87.0
      total_pertest_labels: 68000
      avg_f2p_tests: 2.8
      avg_code_tokens: 2800
      p2p_regression_rate: 0.013
      construction_time_hours: 22
    result_rationale: >
      65/500 Docker failures (13%) 主要因 legacy Python packages unavailable in 2026、
      特定版本 pinning broken、Docker image build timeouts。435 instances 足以 support
      repo-level training (350 train / 85 test approx)。F2P stats 与 SWE-bench metadata
      一致 (median T=1, mean T=2.8)。P2P regression rate ~1.3% 再次 confirms 低
      regression 率——P2P 维度信号弱。Code tokens ~2800 远超 function-level ~200。
      Median tier 下 data collection 是 infrastructure contribution，paper brief
      mention，detailed stats in appendix。注意：这个 dataset construction 实际已被
      之前的 repo-level training experiments 隐式完成（它们使用了 swebench_train.jsonl），
      此处是 formal documentation。
    tables:
      - name: "Table (Appendix): SWE-bench-PerTest Stats"
        columns: [Statistic, Value]
        rows:
          - ["Instances (successful)", 435]
          - ["Candidates/instance", 16]
          - ["Per-test labels", "~68K"]
          - ["Avg F2P tests", 2.8]
          - ["Avg code tokens", 2800]
          - ["P2P regression rate", "1.3%"]
    figures_description:
      - "Test count distribution (F2P vs P2P)"
    analysis: >
      Data sufficient for repo-level experiments。Docker failure rate acceptable。

  ####################################################################
  # Downstream — Diagnostic Re-Repair (planned → median: negative)
  ####################################################################

  - name: "Diagnostic Re-Repair (Downstream PoC)"
    plan_id: "diagnostic-rerepair"
    description: "Per-test failure predictions 用于 guide repair agent, on repo-level instances"
    expected_results:
      full_experiment_completed: false
      phase0_only: true
      phase0_control_mean_sim: 0.820
      phase0_cls_diag_mean_sim: 0.818
      phase0_oracle_diag_mean_sim: 0.809
      phase0_random_diag_mean_sim: 0.719
      phase0_n_instances: 10
      phase0_n_conditions: 4
      control_vs_cls_diag_gap: 0.002
      statistically_significant: false
    result_rationale: >
      Median tier 核心假设："Re-repair 停留在 phase0 负面结果（control 0.82 ≈ cls_diag
      0.818）；downstream impact 无实证"。Phase0 仅 10 instances × 4 conditions × 3
      samples，power 极低。Control (no diagnostic) 与 cls_diag (per-test predictions)
      mean similarity 差距 0.002——essentially zero。

      Phase0 失败的原因分析：(1) 10 instances 中 68.7% 是 T=1（per-test = trajectory，
      无额外信息），仅 ~3 instances 有 T≥2 能 benefit from diagnostic；(2) per-test
      verifier 本身 12.5% error rate，在 10 instances 中 ~1-2 个 diagnostic 是错误的；
      (3) repair agent (SWE-agent) 的 search strategy 对 "which test failed" 信号的
      利用率低——it still explores broadly regardless of diagnostic input。

      有趣的是 oracle_diag（ground truth per-test labels）也低于 control：0.809 < 0.820。
      这暗示 repair agent 可能被 specific failure information constrain 反而限制了
      exploration breadth，negative interference。Random_diag (0.719) 显著低说明
      wrong diagnostic actively hurts。

      Full diagnostic-rerepair experiment（200 instances）不会在 deadline 前启动：
      (1) phase0 已 negative，无动力投入更多 compute；(2) 需要 SWE-agent infrastructure
      每个 instance 需 ~$1-3 execution cost；(3) 剩余时间不足。
    tables:
      - name: "Table (Appendix): Re-Repair Phase0 Results"
        columns: [Condition, Mean Similarity, N]
        rows:
          - [Control (no diagnostic), 0.820, "10×3"]
          - [CLS diagnostic, 0.818, "10×3"]
          - [Oracle diagnostic, 0.809, "10×3"]
          - [Random diagnostic, 0.719, "10×3"]
      - name: "Table: Why Phase0 Failed"
        columns: [Factor, Impact]
        rows:
          - ["T=1 dominance (68.7%)", "Most instances get no extra info from per-test"]
          - ["Verifier error rate (12.5%)", "~1-2/10 diagnostics are wrong"]
          - ["Agent utilization", "SWE-agent ignores specific failure signals"]
    figures_description:
      - "Phase0 condition comparison bar chart with error bars"
    analysis: >
      Re-repair 是 median tier 最显著的 negative result。Paper 策略：(1) 不作为
      main claim——从 C2 description 中删除 "enabling targeted re-repair" 的 practical
      impact claim，改为 "potentially enabling"；(2) phase0 结果放 appendix 作为
      honest reporting of negative finding；(3) future work section: "scaling diagnostic
      re-repair to more instances and testing with repair agents that explicitly
      condition on per-test failure information"。

      Critical reviewer concern (3) "no practical downstream impact" 的回应：
      "We acknowledge that the current pilot study (N=10) did not demonstrate
      statistically significant re-repair improvement. However, oracle analysis
      (Section X) shows that the theoretical per-test advantage is 10.93pp overall
      and >30pp for T≥2 instances, suggesting that the practical gap lies in
      verifier accuracy and agent utilization rather than the formulation itself."

  ####################################################################
  # Cross-Model — DeepSeek Function-Level TRAJ s123 (ANALYZING)
  ####################################################################

  - name: "DeepSeek Function-Level Trajectory s123 (ANALYZING)"
    plan_id: "deepseek-traj-func-s123"
    description: "DeepSeek-Coder-6.7B trajectory-level function, seed123, currently analyzing"
    expected_results:
      accuracy: 84.8
      majority_baseline: 53.59
      per_test_consistency: 78.5
      cls_vs_traj_gap_pp: 1.97
    result_rationale: >
      Seed123 TRAJ 预期 accuracy ~84.8%，基于 v2-s123 (85.08%) 减去 v2 与 original
      implementation 的 minor gap。CLS s123 (86.77%) vs TRAJ s123 (~84.8%) gap ~1.97pp，
      smaller than seed42 gap (3.69pp)。Cross-seed average CLS-TRAJ gap ~2.8pp 仍在
      [2, 5] range 内。如果最终 eval 显示 gap 更小（<2pp），会 weaken C2 cross-model
      evidence 到 merely "no significant difference" 而非 "CLS≥TRAJ"。
    tables:
      - name: "Table: DeepSeek CLS vs TRAJ 2-Seed Summary"
        columns: [Seed, CLS, TRAJ, "Gap(pp)"]
        rows:
          - [42, 86.93, 83.24, 3.69]
          - [123, 86.77, "~84.8", "~1.97"]
          - [Mean, 86.85, "~84.0", "~2.83"]
    figures_description: []
    analysis: >
      DeepSeek CLS≥TRAJ directionally consistent with Qwen。2 seeds insufficient for
      formal equivalence test but usable as suggestive cross-model evidence in paper。

  ####################################################################
  # Consolidated Cross-Model Summary Table
  ####################################################################

  - name: "Cross-Model Consolidated Analysis"
    plan_id: "cross-model-summary"
    description: "Qwen vs DeepSeek full comparison across all formulations and levels"
    expected_results:
      func_level:
        qwen_4b_cls_mean: 88.43
        qwen_4b_cwm_mean: 87.19
        qwen_4b_cls_cwm_gap: 1.24
        qwen_8b_cls_mean: 89.40
        qwen_8b_cwm_mean: 86.96
        qwen_8b_cls_cwm_gap: 2.43
        deepseek_cls_mean: 86.85
        deepseek_cwm_mean: 86.83
        deepseek_cls_cwm_gap: 0.02
      repo_level:
        qwen_4b_cls_best: 82.35
        qwen_8b_cls_best: 84.79
        qwen_cwm_best: 69.91
        qwen_cwm_unparseable: 93.0
        deepseek_cls: 74.5
        deepseek_cwm_accuracy: 68.2
        deepseek_cwm_unparseable: 27.0
      c2_cross_model:
        qwen_tost_p: 0.007
        deepseek_cls_traj_gap: 2.69
        deepseek_traj_repo: "not_completed"
    result_rationale: >
      Cross-model analysis 的 key narrative：
      (1) Function-level：Qwen CLS>CWM (1.24pp@4B, 2.43pp@8B) 但 DeepSeek CLS≈CWM
      (0.02pp)。Conclusion：CLS advantage 是 model-modulated，不 universal。
      (2) Repo-level：Qwen CWM catastrophic (93% unparseable) but DeepSeek CWM
      partially viable (27% unparseable)。CLS-CWM gap consistent in direction（CLS
      better）but magnitude varies: Qwen qualitative gap → DeepSeek 6.3pp quantitative
      gap。Conclusion："CLS provides more robust cross-architecture performance"。
      (3) C2：Qwen 5-seed TOST sufficient standalone。DeepSeek CLS≥TRAJ directionally
      consistent (mean gap 2.69pp) but only 2 seeds, no formal equivalence test。
      Repo-level TRAJ absent。

      Median tier 总 narrative：partial cross-model validation。足以 claim "results
      are not Qwen-specific" but insufficient to claim "results generalize across
      all architectures"。EMNLP reviewer 大概率 request more cross-model seeds。
    tables:
      - name: "Table: Cross-Model Full Comparison"
        columns: [Level, Model, "CLS Acc", "CWM Acc", "CLS-CWM Gap", "TRAJ Acc", "CLS-TRAJ Gap"]
        rows:
          - ["Func", "Qwen3-4B (5s)", 88.43, 87.19, "+1.24", 86.30, "+2.13"]
          - ["Func", "Qwen3-8B (3s)", 89.40, 86.96, "+2.43", "—", "—"]
          - ["Func", "DeepSeek-6.7B (2s)", 86.85, 86.83, "+0.02", "~84.0", "~+2.8"]
          - ["Repo", "Qwen3-4B (best)", 82.35, "69.91†", "qual. gap", "—", "—"]
          - ["Repo", "Qwen3-8B (best)", 84.79, "—(failed)", "—", "—", "—"]
          - ["Repo", "DeepSeek-6.7B", "~74.5", "~68.2‡", "~+6.3", "N/C", "N/C"]
      - name: "† 93% unparseable ‡ 27% unparseable"
        columns: []
        rows: []
    figures_description:
      - "Cross-model CLS-CWM gap heatmap: rows=model, columns=level"
      - "CWM viability spectrum: Qwen(catastrophic) → DeepSeek(partial) at repo-level"
    analysis: >
      Paper 新增 §4.5 "Model-Specific Variation in Formulation Advantage" section，
      discussing：(1) why CLS advantage appears on Qwen but not DeepSeek at function-level;
      (2) why DeepSeek CWM partially works at repo-level while Qwen CWM doesn't;
      (3) implications for deployment: choose formulation based on base model。
      
      Critical concern (4) "generalization" response：partial cross-model validation
      demonstrates CLS is not Qwen-specific artifact, but advantage magnitude is
      architecture-dependent。This honest characterization is actually stronger than
      overclaiming universality。
```

这个 YAML 覆盖了 experiment_plan 中全部 14 个实验加上 8 个 DeepSeek/re-repair 相关的 registry 实验（共 22 条），每条均含 result_rationale。

核心 median 档位预测总结：
- **deepseek-cls-repo**: ~74.5% accuracy，低于 Qwen 同配置 ~8pp
- **deepseek-cwm-repo**: ~27% unparseable（远好于 Qwen 的 53-93%），parseable subset ~71.5%，CLS-CWM gap 缩小到 ~6.3pp
- **deepseek-traj-repo/s123**: 未能在 deadline 前完成，C2 跨模型 TRAJ 证据缺失
- **diagnostic-rerepair**: 停留在 phase0 负面（control 0.82 ≈ cls_diag 0.818），不启动 full experiment
- **swebench-pertest-data**: 435/500 instances 成功，作为 infrastructure contribution

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dc85aea-d59c-4232-9875-a104f22eb207",
  "isSidechain": false,
  "requestId": "req_011Cb6UCfkbsaYHLN4T3EYuz",
  "type": "assistant",
  "uuid": "1d508325-f4f7-474d-96dc-fcf316724ce0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzzgMgcapeB568CryJz81h",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3047,
      "cache_read_input_tokens": 80169,
      "output_tokens": 17096,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3047,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17096,
          "cache_read_input_tokens": 80169,
          "cache_creation_input_tokens": 3047,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3047
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：部分跨模型验证——DeepSeek repo CLS 可用但弱于 Qwen，CWM 部分可解析使得差距缩小；C1 需 model-dependent caveat，C2 仅 Qwen 内验证 核心假设：['DeepSeek repo CWM 部分可解析（unparseable 15–40%），parsea…",
  "leafUuid": "1d508325-f4f7-474d-96dc-fcf316724ce0",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-model verification with DeepSeek—median tier narrative",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：部分跨模型验证——DeepSeek repo CLS 可用但弱于 Qwen，CWM 部分可解析使得差距缩小；C1 需 model-dependent caveat，C2 仅 Qwen 内验证 核心假设：['DeepSeek repo CWM 部分可解析（unparseable 15–40%），parsea…",
  "leafUuid": "1d508325-f4f7-474d-96dc-fcf316724ce0",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-model verification with DeepSeek—median tier narrative",
  "sessionId": "ef6bd922-f0b7-4766-ae72-4d9300a35f00"
}
```

---
