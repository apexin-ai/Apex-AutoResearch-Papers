# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Repo-level CLS显著优于CWM，DeepSeek复现确认架构无关性，formulation advantage story完整成立 核心假设

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/caf3dc6a-df31-4098-9ba6-e664e5fc658f.jsonl`
- **Structured JSON:** [`6d6c4d99f3386c5c62ef.json`](../../sessions/6d/6d6c4d99f3386c5c62ef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T07:38:38.430Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T07:38:38.430Z",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Repo-level CLS显著优于CWM，DeepSeek复现确认架构无关性，formulation advantage story完整成立\n核心假设：['Repo-level CLS多seed稳定≥85% accuracy，fail_f1≥75%（当前单seed: 84.79%/81.18%）', 'CWM repo-level unparseable rate ≥80%被接受为formulation固有缺陷而非调参不足', 'DeepSeek function-level复现CLS≈CWM pattern，确认结论非Qwen-specific', '8B scaling gap (2.43pp) + repo-level gap共同构成complexity-dependent advantage的完整证据链']\n关键指标范围：{'repo_cls_accuracy_multiseed': [84, 88], 'repo_cls_fail_f1': [72, 82], 'repo_cwm_unparseable_rate': [0.8, 0.95], 'func_8b_cls_vs_cwm_gap_pp': [2.0, 3.5], 'deepseek_func_cls_cwm_gap_pp': [-1.0, 1.5], 'oracle_ensemble_accuracy': [90, 93]}\n叙事方向：Classification reformulation提供complexity-dependent scaling advantage: function-level equivalence → 8B divergence → repo-level CWM彻底崩溃。三级证据链完整，original claims无需调整。Complementary errors + oracle ensemble作为bonus contribution。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: exec-sim-repair-verifier\n\n## paper_framing.md\n\n# Paper Framing — exec-sim-repair-verifier\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Extended fallback: ICSE 2027 (Jun 23 abstract, Jun 30 paper)\n- Deadline: ARR May 25, 2026 (14 days from project start)\n\n## Core Claims (3 conditions)\n\n1. **Complexity-Dependent Reformulation Advantage**: Binary pass/fail classification and execution output generation (CWM-style) achieve equivalent accuracy on simple function-level code (4B: F1 diff 0.9pp), but classification scales better with model size (8B 3-seed mean accuracy gap=2.43pp; seed42: 2.81pp, cls 90.48% vs cwm 87.67%) and to repo-level complexity where CWM failure modes—token-budget exhaustion and string-value prediction errors—dominate. Zero-shot LLM-as-judge baselines (8B: 64.4%, 32B NF4: 71.7%) are far below fine-tuned 4B (88.4%), confirming fine-tuning necessity. (Validated function-level near-null + 8B scaling evidence; repo-level SWE-bench experiments in progress. Fallback: if repo-level also null, reframe to efficiency-equivalent accuracy—same F1 with 1-token vs N-token inference.)\n\n2. **Diagnostic Granularity At Equivalent Accuracy**: Per-test classification achieves equivalent variant-level accuracy to trajectory-level scoring (TOST equivalence test p=0.007, ±2pp margin; 5-seed pooled gap -0.40pp, 95% CI [-1.32, +0.52]) while providing actionable diagnostic information (which specific tests a patch fails). The per-test formulation gains diagnostic granularity without sacrificing accuracy—potentially enabling targeted re-repair and oracle-based test selection. (Evidence: 5-paired clustered bootstrap CI, 114 clusters, 10000 resamples. Paper must justify ±2pp margin: in code verification, 2pp variant-level difference is negligible given ICC=0.191/DEFF=3.97. Seeds 789/0 used 4-bit quantization — note in paper. Downstream re-repair experiment still needed for practical impact claim.)\n\n3. **Accuracy-Utility Frontier Characterization**: The effectiveness of per-test verification depends critically on test distribution characteristics. We empirically show: (a) per-test advantage concentrates in instances with multiple FAIL_TO_PASS tests (31% of SWE-bench Verified); (b) PASS_TO_PASS regression detection provides signal only when regression rate exceeds ~10%; (c) block-correlated prediction errors amplify per-test advantage through reduced effective degrees of freedom. These findings provide a practical decision framework for when per-test simulation is worth deploying.\n\n## Story Spine\n\n**Problem**: Test-time scaling for code repair requires ranking candidate patches, but verification paradigms face a granularity-cost tradeoff. Full execution costs ~$1-3 and minutes per candidate. Execution-free alternatives like SWE-RM predict trajectory-level binary correctness at low cost but provide only coarse signals that cannot distinguish between candidates failing on different test subsets.\n\n**Existing approaches & gaps**: Code World Models (Self-Execution Simulation, CWM) predict execution outputs but suffer from token-budget exhaustion and string-value prediction failures. SWE-RM achieves strong trajectory-level scoring but loses per-test diagnostic information. No work studies per-test binary classification as a dedicated verification formulation, or compares classification vs generation formulations for code execution simulation at controlled model sizes.\n\n**Our framing**: We reformulate execution simulation from an open-ended generation task (predict execution trace/output) to a closed-form classification task (predict binary pass/fail per test). On simple function-level code, both formulations achieve equivalent accuracy (~87% F1), because short execution outputs do not trigger CWM failure modes. However, on repo-level code with long execution traces and complex outputs, classification sidesteps token-budget exhaustion and string-value prediction errors, yielding a complexity-dependent advantage. We empirically ground this through (1) controlled function-level experiments establishing equivalence, (2) repo-level experiments demonstrating the complexity threshold, (3) oracle accuracy-utility frontier analysis revealing when per-test granularity helps, and (4) error complementarity analysis showing CLS/CWM have systematically opposite failure modes (CLS: miss bugs 75.5%, CWM: false alarms 83.1%), with oracle ensemble reaching 90.63%. (Downstream re-repair experiment is stretch goal; if not completed, frame as future work.)\n\n**Headline result template**: \"On function-level benchmarks, classification and generation verifiers achieve equivalent F1 (~87%), but classification scales better with model size (8B: +2.43pp accuracy) and on repo-level SWE-bench tasks outperforms by [Z] percentage points as CWM failure modes emerge. CLS and CWM exhibit complementary error patterns (oracle ensemble: 90.63%), suggesting formulation diversity as a verification strategy.\"\n\n## Venue Fit Risks\n\n1. **EMNLP vs SE venue**: Core concern is code repair verification, which may be perceived as SE rather than NLP. Mitigation: frame as (a) probing LLM code semantic reasoning capabilities through per-test prediction, and (b) a general NLP methodology insight about classification vs generation formulations applicable beyond code.\n\n2. **Negative P2P finding**: P2P regression rate ~1% means per-test is not universally better. Must present honestly as a characterization finding, not bury it. This actually strengthens the paper by showing nuanced understanding rather than overclaiming.\n\n3. **Function-level to repo-level gap**: Function-level results show classification ≈ generation. Repo-level extension is now CRITICAL (not optional) to demonstrate the complexity-dependent advantage. Requires SWE-bench Docker infrastructure. If repo-level also shows no advantage, paper pivots to efficiency framing (same accuracy, lower inference cost) + oracle characterization.\n\n## Anticipated Reviewer Concerns & Mitigations\n\n| Concern | Mitigation Experiment |\n|---------|----------------------|\n| \"Classification is trivially easier than generation -- not interesting\" | Function-level null result proves classification is NOT trivially easier; advantage is complexity-dependent, demonstrated by repo-level gap |\n| \"Per-test is just trajectory-level with extra steps when T=1\" | Oracle frontier analysis shows T distribution sensitivity; honest reporting of T=1 equivalence |\n| \"No practical downstream impact\" | Diagnostic re-repair experiment shows resolve rate improvement |\n| \"Small-scale function-level results don't generalize\" | Repo-level SWE-bench extension (if resources allow) |\n| \"CWM comparison is unfair (different output format)\" | Matched model, data, compute; discuss target asymmetry limitation |\n\n\n## experiment_plan (with registry status)\n\n- id: cwm-baseline\n  claim: 1\n  description: Train CWM generation baseline (Qwen3-4B LoRA, same data/config as MVP-B)\n    to predict execution output instead of pass/fail. Compare per-class F1 against\n    classification model (87.1/87.9%).\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - mvp-b-train\n  status: DONE\n  registry_id: cwm-baseline\n  conclusion: negative\n  metrics:\n    overall_accuracy: 87.51\n    pass_f1: 87.31\n    fail_f1: 87.71\n    pass_precision: 92.06\n    pass_recall: 83.03\n    fail_precision: 83.53\n    fail_recall: 92.32\n    exact_match_rate: 84.02\n    train_loss: 0.2534\n    eval_loss: 0.0644\n    train_runtime_sec: 3439\n    test_set_size: 1890\n    unparseable_predictions: 0\n- id: multi-seed-core\n  claim: 1\n  description: 'Multi-seed validation for core comparison: run classification (mvp-b-train)\n    and CWM baseline each with seeds {0, 1, 42}. Report mean +/- std F1. Statistical\n    significance via paired t-test or bootstrap CI. Required for any claim of ''significantly\n    better''.'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - cwm-baseline\n  registry_id: traj-level-seed0\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 85.66\n    unresolved_f1: 87.37\n    resolved_f1: 83.41\n    unresolved_precision: 82.71\n    unresolved_recall: 92.59\n    resolved_precision: 90.07\n    resolved_recall: 77.66\n    consistency_rate: 79.55\n    train_loss: 0.225\n    eval_loss_epoch1: 0.0949\n    eval_loss_epoch2: 0.0885\n    eval_loss_epoch3: 0.1011\n    train_runtime_sec: 4071.3\n- id: trace-then-judge\n  claim: 1\n  description: 'Trace-then-Judge ablation (chain-of-thought, NOT pipeline): single\n    Qwen3-4B model trained to first generate a brief execution reasoning trace (~50\n    tokens describing expected behavior), then output pass/fail. Same LoRA config/data.\n    Tests whether explicit execution reasoning helps or hurts compared to direct classification.\n    If trace-then-judge >= direct classification, the advantage is from task simplicity,\n    not from skipping reasoning.'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - cwm-baseline\n  registry_id: trace-then-judge\n  status: DONE\n  conclusion: failed\n- id: traj-level-finetuned\n  claim: 1\n  description: 'Same-size fine-tuned trajectory-level baseline: Qwen3-4B LoRA trained\n    to predict resolved/unresolved. Data construction: for each problem_id, aggregate\n    all (code, test) pairs into (code, all_tests_concatenated) -> resolved (original\n    code passes all tests) / unresolved (mutated code fails any test). Same train/val/test\n    split by problem_id. Isolates granularity effect.'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - mvp-b-data-prep\n  registry_id: traj-level-finetuned\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.66\n    unresolved_f1: 87.5\n    resolved_f1: 83.18\n    per_test_consistency: 79.94\n- id: model-size-scaling\n  claim: 1\n  description: Scale classification model from 4B to 8B. Measure accuracy improvement\n    and compare with CWM at 8B. Determine if classification advantage holds across\n    scales.\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - cwm-baseline\n  registry_id: model-size-scaling-cls8b\n  sub_experiments:\n  - registry_id: model-size-scaling-cls8b\n    gpu: seetacloud cuda:0\n    description: Qwen3-8B LoRA classification\n  - registry_id: model-size-scaling-cwm8b\n    gpu: seetacloud cuda:1\n    description: Qwen3-8B LoRA CWM generation\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 90.48\n    pass_f1: 90.86\n    fail_f1: 90.06\n    pass_precision: 90.22\n    pass_recall: 91.51\n    fail_precision: 90.76\n    fail_recall: 89.36\n    train_loss: 0.3125\n    eval_loss_epoch1: 0.0723\n    eval_loss_epoch2: 0.0741\n    eval_loss_epoch3: 0.0783\n    train_runtime_sec: 5614\n    unparseable: 0\n- id: diagnostic-rerepair\n  claim: 2\n  description: 'Downstream proof-of-concept: give repair agent per-test failure predictions\n    vs no per-test info, compare resolve rate on 200 instances. Uses SWE-agent or\n    similar repair framework.'\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - cwm-baseline\n  - traj-level-finetuned\n  status: planned\n- id: per-test-precision-recall\n  claim: 2\n  description: Measure per-test failure prediction precision/recall against ground-truth\n    failing tests on full test set. Evaluate diagnostic signal quality without downstream\n    execution.\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-b-train\n  registry_id: per-test-precision-recall\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.51\n    fail_precision: 82.75\n    fail_recall: 93.64\n    fail_f1: 87.86\n    pass_precision: 93.24\n    pass_recall: 81.8\n    pass_f1: 87.15\n    FP_count: 58\n    FN_count: 178\n    best_mutation: return_value (97.26%)\n    worst_mutation: off_by_one (82.56%)\n    bucket_6_10_acc: 96.3\n    bucket_11plus_acc: 87.12\n- id: oracle-f2p-stratified\n  claim: 3\n  description: Stratified oracle analysis by F2P test count (T=1, T=2, T=3+). Report\n    per-test advantage breakdown showing advantage concentrates in multi-test instances.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - mvp-a-oracle-sim\n  registry_id: oracle-f2p-stratified\n  status: DONE\n  conclusion: success\n  metrics:\n    T1_pct: 68.7\n    T1_block_adv: -0.09\n    T2_pct: 19.1\n    T2_block_adv: 31.69\n    T3_5_pct: 7.1\n    T3_5_block_adv: 40.74\n    T6plus_pct: 5.1\n    T6plus_block_adv: 40.06\n    overall_block_adv: 10.93\n    T2_contribution_pct: 55.3\n- id: oracle-total-validated\n  claim: 3\n  description: Oracle study with Total (F2P+P2P) distribution at empirically measured\n    regression rates. Validate when P2P tests help vs hurt.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - p2p-regression-rate\n  status: DONE\n  registry_id: mvp-a-oracle-sim\n  conclusion: success\n  metrics:\n    original_T12:\n      iid_adv_70_85: 0.1849\n      block_adv_70_85: 0.3618\n    sensitivity_T3:\n      iid_adv_70_85: 0.0761\n      block_adv_70_85: 0.3839\n    sensitivity_T7:\n      iid_adv_70_85: 0.1351\n      block_adv_70_85: 0.3833\n    sensitivity_T11:\n      iid_adv_70_85: 0.1863\n      block_adv_70_85: 0.3639\n    real_f2p_T1:\n      iid_adv_70_85: 0.0198\n      block_adv_70_85: 0.1088\n      pct_T1: 0.687\n      T_median: 1\n      T_mean: 2.3\n    swebench_f2p_stats:\n      median: 1\n      mean: 3\n      P75: 2\n      P90: 3\n    total_reg5pct:\n      iid_adv_70_85: -0.01\n      block_adv_70_85: -0.005\n      pass: false\n    total_reg10pct:\n      iid_adv_70_85: 0.132\n      block_adv_70_85: 0.083\n      pass: true\n    total_reg20pct:\n      iid_adv_70_85: 0.357\n      block_adv_70_85: 0.278\n      pass: true\n- id: block-corr-empirical\n  claim: 3\n  description: 'Empirically validate block-correlation assumption: measure actual\n    prediction error correlation structure from trained model''s test-level predictions,\n    compare with i.i.d. and block-correlated simulation models.'\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - mvp-b-train\n  registry_id: block-corr-empirical\n  status: DONE\n  conclusion: success\n  metrics:\n    icc: 0.1909\n    icc_p_value: 0\n    design_effect: 3.9676\n    overall_error_rate: 0.1249\n    all_correct_observed: 46\n    all_correct_expected_iid: 16.35\n    all_correct_ratio: 2.81\n    error_std_observed: 0.1531\n    error_std_expected_iid: 0.0811\n    error_std_ratio: 1.89\n    n_samples: 1890\n    n_problems: 114\n    inference_precision: bfloat16\n    version: v2_corrected\n- id: swebench-pertest-data\n  claim:\n  - 1\n  - 2\n  - 3\n  description: Docker re-evaluation of SWE-bench Verified patches to extract per-test\n    labels. Build SWE-bench-PerTest dataset (500 instances x 16 candidates). Resource\n    contribution.\n  priority: P1\n  gpu_budget_hours: 0\n  compute_note: CPU/Docker only, ~16-24h with 16 parallel containers. Start early\n    to parallelize with GPU experiments.\n  deps: []\n  status: planned\n- id: repo-level-training\n  claim:\n  - 1\n  - 2\n  description: Fine-tune Qwen3-4B/8B on repo-level (patched_code, test_code) -> pass/fail\n    using SWE-bench-PerTest data. Evaluate on held-out instances.\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - swebench-pertest-data\n  registry_id: repo-level-cwm-v3\n  status: DONE\n  conclusion: failed\n- id: llm-judge-baseline\n  claim:\n  - 1\n  - 3\n  description: Qwen3-8B/32B zero-shot LLM-as-judge baselines (trajectory-level and\n    per-test). Reference points for Pareto frontier.\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: llm-judge-8b-zeroshot\n  sub_experiments:\n  - registry_id: llm-judge-8b-zeroshot\n    gpu: seetacloud cuda:2\n    description: Qwen3-8B zero-shot per-test + trajectory-level\n  - registry_id: llm-judge-32b-zeroshot\n    gpu: seetacloud cuda:3\n    description: Qwen3-32B 4-bit quantized zero-shot\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 64.4\n    fail_precision: 57.9\n    fail_recall: 95.8\n    fail_f1: 72.2\n    pass_precision: 90\n    pass_recall: 35.1\n    pass_f1: 50.5\n    majority_baseline: 51.7\n    accuracy_vs_baseline_gap: 12.6\n    traj_accuracy: 99.1\n    traj_problems: 114\n    traj_true_resolved: 1\n    traj_pred_resolved: 0\n    confusion:\n      TP_fail: 874\n      FN_fail: 38\n      FP_fail: 635\n      TN_fail: 343\n- id: per-test-majority-voting\n  claim: 1\n  description: Per-test majority voting (K=3) with classification model. Test if self-consistency\n    improves per-test accuracy.\n  priority: P2\n  gpu_budget_hours: 3\n  deps:\n  - mvp-b-train\n  registry_id: per-test-majority-voting\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy_greedy: 87.51\n    accuracy_majority_vote_K3: 86.83\n    delta_accuracy: -0.69\n    fail_f1_greedy: 87.86\n    fail_f1_mv: 87.29\n    pass_f1_greedy: 87.15\n    pass_f1_mv: 86.33\n    unanimous_rate: 93.3\n    split_samples: 127\n    flipped_correct_to_wrong: 28\n    flipped_wrong_to_correct: 15\n    net_flips: -13\n    per_pass_accuracy:\n    - 86.72\n    - 86.83\n    - 87.62\n    wall_time_greedy_sec: 30\n    wall_time_mv_sec: 120\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-a-oracle-sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    original_T12:\n      iid_adv_70_85: 0.1849\n      block_adv_70_85: 0.3618\n    sensitivity_T3:\n      iid_adv_70_85: 0.0761\n      block_adv_70_85: 0.3839\n    sensitivity_T7:\n      iid_adv_70_85: 0.1351\n      block_adv_70_85: 0.3833\n    sensitivity_T11:\n      iid_adv_70_85: 0.1863\n      block_adv_70_85: 0.3639\n    real_f2p_T1:\n      iid_adv_70_85: 0.0198\n      block_adv_70_85: 0.1088\n      pct_T1: 0.687\n      T_median: 1\n      T_mean: 2.3\n    swebench_f2p_stats:\n      median: 1\n      mean: 3\n      P75: 2\n      P90: 3\n    total_reg5pct:\n      iid_adv_70_85: -0.01\n      block_adv_70_85: -0.005\n      pass: false\n    total_reg10pct:\n      iid_adv_70_85: 0.132\n      block_adv_70_85: 0.083\n      pass: true\n    total_reg20pct:\n      iid_adv_70_85: 0.357\n      block_adv_70_85: 0.278\n      pass: true\n- exp_id: mvp-b-data-prep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp-b-train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 0.875\n    pass_f1: 0.871\n    fail_f1: 0.879\n    pass_precision: 0.9324\n    pass_recall: 0.818\n    fail_precision: 0.8275\n    fail_recall: 0.9364\n    majority_baseline: 0.52\n    accuracy_vs_majority_gap: 0.355\n- exp_id: p2p-regression-rate\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: cwm-baseline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_accuracy: 87.51\n    pass_f1: 87.31\n    fail_f1: 87.71\n    pass_precision: 92.06\n    pass_recall: 83.03\n    fail_precision: 83.53\n    fail_recall: 92.32\n    exact_match_rate: 84.02\n    train_loss: 0.2534\n    eval_loss: 0.0644\n    train_runtime_sec: 3439\n    test_set_size: 1890\n    unparseable_predictions: 0\n- exp_id: multi-seed-core\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seed42:\n      accuracy: 87.83\n      pass_f1: 88.06\n      fail_f1: 87.59\n      pass_precision: 89.45\n      pass_recall: 86.71\n      fail_precision: 86.2\n      fail_recall: 89.04\n    seed123:\n      accuracy: 89.52\n      pass_f1: 89.64\n      fail_f1: 89.4\n      pass_precision: 91.76\n      pass_recall: 87.63\n      fail_precision: 87.34\n      fail_recall: 91.56\n    seed456:\n      accuracy: 87.88\n      pass_f1: 87.53\n      fail_f1: 88.21\n      pass_precision: 93.6\n      pass_recall: 82.21\n      fail_precision: 83.12\n      fail_recall: 93.97\n    mean:\n      accuracy: 88.41\n      pass_f1: 88.41\n      fail_f1: 88.4\n    std:\n      accuracy: 0.96\n      pass_f1: 1.1\n      fail_f1: 0.92\n- exp_id: trace-then-judge\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: traj-level-finetuned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.66\n    unresolved_f1: 87.5\n    resolved_f1: 83.18\n    per_test_consistency: 79.94\n- exp_id: model-size-scaling-cls8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 90.48\n    pass_f1: 90.86\n    fail_f1: 90.06\n    pass_precision: 90.22\n    pass_recall: 91.51\n    fail_precision: 90.76\n    fail_recall: 89.36\n    train_loss: 0.3125\n    eval_loss_epoch1: 0.0723\n    eval_loss_epoch2: 0.0741\n    eval_loss_epoch3: 0.0783\n    train_runtime_sec: 5614\n    unparseable: 0\n- exp_id: model-size-scaling-cwm8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.67\n    pass_f1: 87.57\n    fail_f1: 87.77\n    pass_precision: 91.53\n    pass_recall: 83.95\n    fail_precision: 84.19\n    fail_recall: 91.67\n    exact_match_rate: 84.39\n    train_loss: 0.229\n    eval_loss_epoch1: 0.0554\n    eval_loss_epoch2: 0.0512\n    eval_loss_epoch3: 0.0564\n    train_runtime_sec: 5570\n    unparseable: 0\n- exp_id: llm-judge-8b-zeroshot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 64.4\n    fail_precision: 57.9\n    fail_recall: 95.8\n    fail_f1: 72.2\n    pass_precision: 90\n    pass_recall: 35.1\n    pass_f1: 50.5\n    majority_baseline: 51.7\n    accuracy_vs_baseline_gap: 12.6\n    traj_accuracy: 99.1\n    traj_problems: 114\n    traj_true_resolved: 1\n    traj_pred_resolved: 0\n    confusion:\n      TP_fail: 874\n      FN_fail: 38\n      FP_fail: 635\n      TN_fail: 343\n- exp_id: llm-judge-32b-zeroshot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 71.69\n    majority_baseline: 51.75\n    accuracy_vs_baseline_gap: 19.95\n    fail_precision: 64.4\n    fail_recall: 92.43\n    fail_f1: 75.91\n    pass_precision: 88.12\n    pass_recall: 52.35\n    pass_f1: 65.68\n    unparseable_predictions: 0\n    trajectory_accuracy: 99.12\n    trajectory_total_problems: 114\n    trajectory_correct: 113\n    trajectory_true_resolved: 1\n    trajectory_pred_resolved: 0\n- exp_id: per-test-precision-recall\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.51\n    fail_precision: 82.75\n    fail_recall: 93.64\n    fail_f1: 87.86\n    pass_precision: 93.24\n    pass_recall: 81.8\n    pass_f1: 87.15\n    FP_count: 58\n    FN_count: 178\n    best_mutation: return_value (97.26%)\n    worst_mutation: off_by_one (82.56%)\n    bucket_6_10_acc: 96.3\n    bucket_11plus_acc: 87.12\n- exp_id: oracle-f2p-stratified\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    T1_pct: 68.7\n    T1_block_adv: -0.09\n    T2_pct: 19.1\n    T2_block_adv: 31.69\n    T3_5_pct: 7.1\n    T3_5_block_adv: 40.74\n    T6plus_pct: 5.1\n    T6plus_block_adv: 40.06\n    overall_block_adv: 10.93\n    T2_contribution_pct: 55.3\n- exp_id: traj-level-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 85.47\n    unresolved_f1: 87\n    resolved_f1: 83.52\n    unresolved_precision: 83.53\n    unresolved_recall: 90.78\n    resolved_precision: 88.17\n    resolved_recall: 79.33\n    consistency_rate: 78.59\n- exp_id: traj-level-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.4\n    unresolved_f1: 88.7\n    resolved_f1: 85.8\n    unresolved_precision: 85.7\n    unresolved_recall: 91.9\n    resolved_precision: 89.7\n    resolved_recall: 82.3\n    consistency_rate: 78.8\n- exp_id: per-test-majority-voting\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy_greedy: 87.51\n    accuracy_majority_vote_K3: 86.83\n    delta_accuracy: -0.69\n    fail_f1_greedy: 87.86\n    fail_f1_mv: 87.29\n    pass_f1_greedy: 87.15\n    pass_f1_mv: 86.33\n    unanimous_rate: 93.3\n    split_samples: 127\n    flipped_correct_to_wrong: 28\n    flipped_wrong_to_correct: 15\n    net_flips: -13\n    per_pass_accuracy:\n    - 86.72\n    - 86.83\n    - 87.62\n    wall_time_greedy_sec: 30\n    wall_time_mv_sec: 120\n- exp_id: block-corr-empirical\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    icc: 0.1909\n    icc_p_value: 0\n    design_effect: 3.9676\n    overall_error_rate: 0.1249\n    all_correct_observed: 46\n    all_correct_expected_iid: 16.35\n    all_correct_ratio: 2.81\n    error_std_observed: 0.1531\n    error_std_expected_iid: 0.0811\n    error_std_ratio: 1.89\n    n_samples: 1890\n    n_problems: 114\n    inference_precision: bfloat16\n    version: v2_corrected\n- exp_id: traj-level-seed789\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.31\n    unresolved_f1: 88.27\n    resolved_f1: 86.17\n    unresolved_precision: 87.41\n    unresolved_recall: 89.15\n    resolved_precision: 87.18\n    resolved_recall: 85.18\n    consistency_rate: 76.74\n    eval_loss: 0.1115\n    train_loss: 0.2255\n    train_runtime_sec: 2055.9\n- exp_id: traj-level-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 85.66\n    unresolved_f1: 87.37\n    resolved_f1: 83.41\n    unresolved_precision: 82.71\n    unresolved_recall: 92.59\n    resolved_precision: 90.07\n    resolved_recall: 77.66\n    consistency_rate: 79.55\n    train_loss: 0.225\n    eval_loss_epoch1: 0.0949\n    eval_loss_epoch2: 0.0885\n    eval_loss_epoch3: 0.1011\n    train_runtime_sec: 4071.3\n- exp_id: cls8b-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 89.4\n    pass_f1: 89.5\n    fail_f1: 89.2\n    pass_precision: 91.2\n    pass_recall: 87.9\n    fail_precision: 87.5\n    fail_recall: 90.9\n    train_loss: 0.3087\n    eval_loss: 0.0848\n    train_runtime_sec: 5666\n    unparseable: 0\n- exp_id: cwm8b-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 86.98\n    pass_f1: 86.83\n    fail_f1: 87.13\n    pass_precision: 91.12\n    pass_recall: 82.92\n    fail_precision: 83.3\n    fail_recall: 91.34\n    exact_match_rate: 84.13\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: cls-seed789\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89\n    pass_f1: 88.9\n    fail_f1: 89.1\n    pass_precision: 93.3\n    pass_recall: 84.9\n    fail_precision: 85.2\n    fail_recall: 93.4\n- exp_id: cls-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.94\n    pass_f1: 87.79\n    fail_f1: 88.08\n    pass_precision: 92.13\n    pass_recall: 83.84\n    fail_precision: 84.2\n    fail_recall: 92.32\n    train_loss: 0.2347\n    eval_loss: 0.0963\n    train_runtime_sec: 4976.75\n    unparseable: 0\n- exp_id: repo-level-cls\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.2\n    pass_f1: 86.95\n    fail_f1: 87.44\n    exact_match_rate: 84.44\n    majority_baseline_accuracy: 51.75\n    accuracy_vs_baseline_gap_pp: 35.45\n    test_set_size: 1890\n    unparseable_predictions: 0\n- exp_id: cwm-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 86.98\n    pass_f1: 86.66\n    fail_f1: 87.29\n    pass_precision: 92.26\n    pass_recall: 81.7\n    fail_precision: 82.52\n    fail_recall: 92.65\n    exact_match_rate: 84.02\n    train_loss: 0.2525\n    eval_loss_best: 0.0551\n    eval_loss_final: 0.0635\n    train_runtime_sec: 3440\n    unparseable: 0\n- exp_id: cwm-seed789\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 86.67\n    pass_f1: 86.74\n    fail_f1: 86.6\n    exact_match_rate: 83.97\n    baseline_gap_pp: 34.92\n    test_set_size: 1890\n    unparseable_predictions: 0\n    per_class:\n      fail:\n        precision: 84.09\n        recall: 89.25\n        f1: 86.6\n      pass:\n        precision: 89.37\n        recall: 84.25\n        f1: 86.74\n- exp_id: cwm-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.57\n    fail_f1: 87.93\n    fail_precision: 82.71\n    fail_recall: 93.86\n    pass_f1: 87.18\n    pass_precision: 93.45\n    pass_recall: 81.7\n    exact_match_rate: 84.29\n    eval_loss: 0.0665\n    train_loss: 0.2554\n    train_runtime_sec: 3586\n- exp_id: 5-paired-clustered-bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pooled_gap_pp: -0.45\n    pooled_ci_lower: -1.71\n    pooled_ci_upper: 0.84\n    pooled_p_value: 0.499\n    tost_p_value: 0.0071\n    tost_margin_pp: 2\n    seed_level_paired_t_p: 0.425\n    seed_level_mean_gap: -0.48\n    n_variants_pooled: 523\n    n_clusters: 114\n    per_seed_gaps:\n      seed42: -0.97\n      seed123: 1.45\n      seed456: -1.84\n      seed789: -0.78\n      seed0: -0.29\n- exp_id: cwm8b-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 86.24\n    pass_f1: 85.96\n    fail_f1: 86.51\n    pass_precision: 91.08\n    pass_recall: 81.39\n    fail_precision: 82.09\n    fail_recall: 91.45\n    exact_match_rate: 82.8\n    train_loss: 0.2279\n    eval_loss: 0.0583\n    unparseable: 0\n    test_set_size: 1890\n    majority_baseline_accuracy: 51.75\n    accuracy_vs_baseline_gap_pp: 34.5\n- exp_id: cls8b-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 88.31\n    pass_f1: 88.2\n    fail_f1: 88.41\n    pass_precision: 92.29\n    pass_recall: 84.46\n    fail_precision: 84.72\n    fail_recall: 92.43\n    train_loss: 0.3105\n    eval_loss: 0.0928\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: repo-level-cls-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-home\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6611\n    f1_macro: 0.5661\n    f1_pass: 0.769\n    f1_fail: 0.363\n    precision_pass: 0.765\n    recall_pass: 0.774\n    precision_fail: 0.369\n    recall_fail: 0.357\n    majority_baseline: 0.7296\n    n_unparseable: 132\n    best_checkpoint: checkpoint-200\n    early_stop: D045\n- exp_id: cls8b-eval-seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 90.48\n    pass_f1: 90.86\n    fail_f1: 90.06\n    pass_precision: 90.22\n    pass_recall: 91.51\n    fail_precision: 90.76\n    fail_recall: 89.36\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: cls8b-eval-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 89.37\n    pass_f1: 89.54\n    fail_f1: 89.19\n    pass_precision: 91.2\n    pass_recall: 87.93\n    fail_precision: 87.54\n    fail_recall: 90.9\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: matched-seed-8b-predictions\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: repo-level-cwm-v4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cwm-v5\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v6\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v7\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v8\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v9\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-seed123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cwm-seed123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cwm-v10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6991\n    f1_macro: 0.4671\n    f1_pass: 0.8187\n    f1_fail: 0.1154\n    precision_pass: 0.7304\n    recall_pass: 0.9314\n    precision_fail: 0.2815\n    recall_fail: 0.0726\n    majority_baseline: 0.7296\n    n_unparseable: 9102\n    n_unparseable_pct: 0.93\n    n_truncated: 478\n    n_truncated_pct: 0.0489\n    truncated_accuracy: 0.2176\n    best_checkpoint: checkpoint-400\n    early_stop: D045\n    eval_invalid: max_new_tokens=64 caused 93% unparseable (D047)\n- exp_id: repo-level-cls-v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_sweep:\n      ckpt_600:\n        accuracy: 76.74\n        f1_macro: 73.74\n        fail_f1: 64.88\n        pass_f1: 82.61\n      ckpt_4000:\n        accuracy: 81.51\n        f1_macro: 72.56\n        fail_f1: 56.9\n        pass_f1: 88.23\n      ckpt_4200:\n        accuracy: 80.64\n        f1_macro: 72.1\n        fail_f1: 56.66\n        pass_f1: 87.54\n      ckpt_4400:\n        accuracy: 82.11\n        f1_macro: 73.94\n        fail_f1: 59.34\n        fail_precision: 77.02\n        fail_recall: 48.26\n      ckpt_4600:\n        accuracy: 82.35\n        f1_macro: 74.74\n        fail_f1: 60.87\n        pass_f1: 88.6\n        fail_precision: 76\n        fail_recall: 50.76\n    best_checkpoint_accuracy: checkpoint-4600\n    best_checkpoint_f1: checkpoint-4600\n    eval_samples: 9784\n    accuracy: 82.35\n    f1_macro: 74.74\n    unparseable: 132\n    unparseable_pct: 1.3\n    majority_baseline: 72.96\n    gap_vs_baseline: 9.39\n    eval_server: home-1x5090\n    eval_env: transformers 4.57.6\n    note: Test set sweep complete. ckpt-4600 best on both accuracy (82.35%) and f1_macro\n      (74.74%).\n    val_2048:\n      ckpt_600:\n        accuracy: 77.25\n        f1_macro: 70.81\n        fail_f1: 57.11\n        pass_f1: 84.52\n      ckpt_4000:\n        accuracy: 83.32\n        f1_macro: 70.26\n        fail_f1: 50.56\n        pass_f1: 89.97\n      ckpt_4200:\n        accuracy: 82.82\n        f1_macro: 69.54\n        fail_f1: 49.43\n        pass_f1: 89.65\n      ckpt_4400:\n        accuracy: 83.49\n        f1_macro: 71.63\n        fail_f1: 53.29\n        pass_f1: 89.97\n      ckpt_4600:\n        accuracy: 83.63\n        f1_macro: 71.72\n        fail_f1: 53.36\n        pass_f1: 90.07\n      eval_samples: 9335\n      unparseable: 1883\n      unparseable_pct: 20.2\n      val_best_f1: ckpt-4600\n      val_best_acc: ckpt-4600\n      note: 'val-test 一致: 都是 ckpt-4600'\n- exp_id: repo-level-cwm-v11\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_checkpoint: checkpoint-600\n    eval_samples: 500\n    eval_type: subset500_tok1024\n    accuracy: 66.6\n    fail_f1: 27.7\n    pass_f1: 78.3\n    f1_macro: 52.99\n    fail_precision: 33.3\n    fail_recall: 23.7\n    pass_precision: 74.5\n    pass_recall: 82.5\n    unparseable: 376\n    unparseable_pct: 75.2\n    majority_baseline: 73\n    gap_vs_baseline: -6.4\n    gen_length_mean: 3398.1\n    gen_length_median: 3307.5\n    gen_length_max: 7582\n    confusion:\n      TP: 301\n      TN: 32\n      FP: 103\n      FN: 64\n- exp_id: repo-level-cls-8b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_checkpoint: checkpoint-200\n    eval_samples: 9784\n    accuracy: 71.37\n    fail_f1: 60.57\n    pass_f1: 77.53\n    f1_macro: 69.05\n    fail_precision: 48.26\n    fail_recall: 81.29\n    pass_precision: 90.71\n    pass_recall: 67.69\n    unparseable: 136\n    unparseable_pct: 1.39\n    majority_baseline: 73\n    gap_vs_baseline: -1.63\n    confusion:\n      TP: 4832\n      TN: 2151\n      FP: 495\n      FN: 2306\n    eval_server: westd-48478\n    eval_env: transformers 5.8.0\n- exp_id: repo-level-cls-seed123-home\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    val_2048:\n      n: 9335\n      unparseable: 1883\n      ckpt_200:\n        accuracy: 62.51\n        f1_macro: 55.54\n        f1_pass: 73.14\n        f1_fail: 37.94\n      ckpt_400:\n        accuracy: 80.72\n        f1_macro: 67.03\n        f1_pass: 88.27\n        f1_fail: 45.78\n      ckpt_600:\n        accuracy: 76.78\n        f1_macro: 66.81\n        f1_pass: 85\n        f1_fail: 48.63\n      ckpt_800:\n        accuracy: 81.81\n        f1_macro: 69.14\n        f1_pass: 88.91\n        f1_fail: 49.37\n      ckpt_1000:\n        accuracy: 82.3\n        f1_macro: 67.63\n        f1_pass: 89.42\n        f1_fail: 45.84\n      best_f1: ckpt_800\n      best_acc: ckpt_1000\n    val_4096:\n      n: 9335\n      unparseable: 1406\n      ckpt_400:\n        accuracy: 82.57\n        f1_macro: 71.24\n        f1_pass: 89.29\n        f1_fail: 53.18\n      ckpt_600:\n        accuracy: 79.18\n        f1_macro: 70.73\n        f1_pass: 86.45\n        f1_fail: 55\n      ckpt_800:\n        accuracy: 83.7\n        f1_macro: 73.31\n        f1_pass: 90\n        f1_fail: 56.7\n      best_f1: ckpt_800\n      best_acc: ckpt_800\n    val_5120:\n      n: 9335\n      unparseable: 0\n      truncated: 234\n      ckpt_400:\n        accuracy: 86.01\n        f1_macro: 79.66\n        f1_pass: 91.02\n        f1_fail: 68.3\n      ckpt_600:\n        accuracy: 81.89\n        f1_macro: 77.01\n        f1_pass: 87.6\n        f1_fail: 66.43\n      ckpt_800:\n        accuracy: 87.92\n        f1_macro: 81.95\n        f1_pass: 92.33\n        f1_fail: 71.57\n      best_f1: ckpt_800\n      best_acc: ckpt_800\n- exp_id: repo-level-cwm-v12\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_test_accuracy: 58.04\n    eval_test_f1_macro: 51.67\n    eval_test_f1_fail: 34.12\n    eval_test_f1_pass: 69.22\n    eval_test_unparseable: 5255\n    eval_test_total: 9784\n    eval_test_unparseable_rate: 53.7\n    eval_checkpoint: checkpoint-500\n- exp_id: repo-level-cwm-seed123-conda\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_test_accuracy: 59.09\n    eval_test_f1_macro: 43.43\n    eval_test_f1_fail: 13.67\n    eval_test_f1_pass: 73.19\n    eval_test_unparseable: 6574\n    eval_test_total: 9784\n    eval_test_unparseable_rate: 67.2\n    eval_checkpoint: checkpoint-500\n- exp_id: repo-level-cls-8b-conda\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    val_8192:\n      ckpt_200:\n        accuracy: 63.52\n        f1_macro: 61.17\n        f1_fail: 51.6\n        f1_pass: 70.7\n        unparseable: 9\n      ckpt_400:\n        accuracy: 80.96\n      ckpt_600:\n        accuracy: 85\n      best_acc: ckpt_600\n    val_5120:\n      ckpt_400:\n        accuracy: 80.47\n        f1_macro: 75.84\n    test_2048:\n      ckpt_400:\n        accuracy: 84.52\n        f1_macro: 80.89\n      ckpt_600:\n        accuracy: 78.51\n    test_8192:\n      ckpt_400:\n        accuracy: 84.79\n        f1_macro: 81.18\n        f1_fail: 72.93\n        f1_pass: 89.43\n        unparseable: 0\n        total: 9784\n      ckpt_600:\n        accuracy: 79.05\n        f1_macro: 75.12\n        f1_fail: 65.24\n        f1_pass: 85\n        unparseable: 0\n        total: 9784\n- exp_id: repo-level-cls-v5-conda\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_sweep:\n      ckpt_200:\n        accuracy: 52.96\n        f1_macro: 52.89\n        fail_f1: 51.02\n        pass_f1: 54.76\n      ckpt_400:\n        accuracy: 78.43\n        f1_macro: 68.41\n        fail_f1: 50.61\n        pass_f1: 86.21\n        fail_precision: 66.48\n        fail_recall: 40.85\n        pass_precision: 80.82\n        pass_recall: 92.36\n      ckpt_600:\n        accuracy: 76.37\n        f1_macro: 71.17\n        fail_f1: 58.93\n        pass_f1: 83.41\n        fail_precision: 55.6\n        fail_recall: 62.7\n        pass_precision: 85.49\n        pass_recall: 81.44\n    best_checkpoint_accuracy: checkpoint-400\n    best_checkpoint_f1: checkpoint-600\n    eval_samples: 9784\n    accuracy: 78.43\n    f1_macro: 71.17\n    unparseable: 132\n    unparseable_pct: 1.35\n    majority_baseline: 72.96\n    eval_server: westd-48478\n    eval_env: conda, transformers 4.57.6\n- exp_id: repo-level-cwm-8b-conda\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-8b-seed123-conda\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-8b-seed123-conda-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-8b-seed123-conda-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-ckpt3000-test-eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-ckpt3000-test-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt3000-val-eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cls-8b-s42-ckpt200-val\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt3000-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 88.69\n    f1_macro: 81.73\n    f1_fail: 70.5\n    f1_pass: 93\n    precision_fail: 95.2\n    precision_pass: 87.6\n    recall_fail: 55.9\n    recall_pass: 99.1\n    majority_baseline: 75.9\n    gap_vs_majority_pp: 12.8\n    unparseable: 9\n    total: 9335\n- exp_id: cls8b-s42-ckpt400-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.79\n    f1_macro: 81.18\n    f1_fail: 72.93\n    f1_pass: 89.43\n    precision_fail: 70.32\n    precision_pass: 90.74\n    recall_fail: 75.74\n    recall_pass: 88.15\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 11.84\n    unparseable: 0\n    total: 9784\n- exp_id: cls4b-seed123-ckpt800-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.92\n    f1_macro: 81.95\n    f1_pass: 92.33\n    f1_fail: 71.57\n    unparseable: 0\n    truncated: 234\n    total: 9335\n- exp_id: cls8b-s42-ckpt600-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 79.05\n    f1_macro: 75.12\n    f1_fail: 65.24\n    f1_pass: 85\n    precision_fail: 59.16\n    precision_pass: 88.95\n    recall_fail: 72.71\n    recall_pass: 81.4\n    unparseable: 0\n    total: 9784\n    majority_baseline: 73\n    gap_vs_majority_pp: 6.09\n- exp_id: repo-level-cls-8b-s42-resume\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_steps: 6633\n    epochs: 3\n    train_time_sec: 74425\n    final_train_loss: 0.4284\n    final_eval_loss: 0.4768\n    best_eval_loss_resume: 0.2516\n    best_eval_loss_resume_step: 4200\n    best_eval_loss_overall: 0.0796\n    best_eval_loss_overall_step: 200\n    checkpoints_saved: 32\n    overfitting: true\n    note: Severe overfitting after epoch 2. Resume-best=ckpt-4200. Val sweep running\n      on cuda:0.\n- exp_id: cls8b-s42-ckpt200-val8192-eval-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 63.52\n    f1_macro: 61.17\n    f1_fail: 51.6\n    f1_pass: 70.7\n    unparseable: 9\n    total: 9335\n- exp_id: cls4b-v5-val5120-sweep-home\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-v5-ckpt600-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 82.82\n    f1_macro: 79.81\n    f1_fail: 72.03\n    f1_pass: 87.6\n    precision_fail: 59.3\n    recall_fail: 91.7\n    unparseable: 0\n    total: 9335\n- exp_id: cls8b-s42-ckpt800-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.5\n    f1_macro: 79.2\n- exp_id: cls4b-v5-ckpt4000-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89.84\n    f1_macro: 84.25\n    f1_fail: 74.85\n    f1_pass: 93.64\n    precision_fail: 92.95\n    recall_fail: 62.66\n    precision_pass: 89.24\n    recall_pass: 98.49\n    unparseable: 0\n    truncated: 234\n    total: 9335\n- exp_id: cls8b-s42-ckpt1000-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 88.23\n    f1_macro: 82.72\n    f1_fail: 73\n    f1_pass: 92.5\n    precision_fail: 81.8\n    recall_fail: 65.8\n    precision_pass: 89.8\n    recall_pass: 95.3\n    unparseable: 9\n    total_instances: 9335\n- exp_id: cls4b-v5-ckpt4400-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    accuracy_partial_70pct: 89.69\n    f1_macro_partial_70pct: 84.61\n    samples_completed: 6544\n    samples_total: 9335\n- exp_id: cls8b-s42-ckpt1000-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.52\n    f1_macro: 77.5\n    f1_fail: 65.85\n    f1_pass: 89.14\n    precision_fail: 74.93\n    recall_fail: 58.73\n    precision_pass: 85.84\n    recall_pass: 92.72\n    majority_baseline: 72.96\n    gap_vs_majority: 10.56\n    unparseable_count: 0\n    unparseable_rate: 0\n    total_samples: 9784\n    tp: 6618\n    fp: 1092\n    fn: 520\n    tn: 1554\n- exp_id: cls4b-v5-ckpt4400-val5120-eval-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1200-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1400-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.97\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 10.09\n    f1_macro: 77.15\n    f1_fail: 62.95\n    f1_pass: 91.34\n    precision_fail: 86.68\n    precision_pass: 85.85\n    recall_fail: 49.42\n    recall_pass: 97.59\n    n_instances: 9335\n    n_unparseable: 9\n    confusion_matrix:\n      tn: 1113\n      fp: 1139\n      fn: 171\n      tp: 6912\n- exp_id: cls8b-s42-ckpt1600-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-v5-val-sweep-ckpt4600\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 90.07\n    f1_macro: 85.04\n    f1_fail: 76.37\n    f1_pass: 93.71\n    precision_fail: 89.65\n    recall_fail: 66.52\n    precision_pass: 90.16\n    recall_pass: 97.56\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 14.19\n    unparseable_count: 0\n    total_samples: 9335\n    n_truncated: 234\n- exp_id: cls4b-v5-val-sweep-ckpt4200\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89.06\n    f1_macro: 83.07\n    f1_fail: 73\n    f1_pass: 93.1\n    precision_fail: 90.3\n    recall_fail: 61.3\n    precision_pass: 88.8\n    recall_pass: 97.9\n- exp_id: cls4b-v5-val-sweep-ckpt4400\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1200-val8192\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-v5-val-sweep-ckpt4400-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89.96\n    f1_macro: 84.94\n    f1_fail: 76.25\n    f1_pass: 93.64\n    precision_fail: 88.84\n    precision_pass: 90.21\n    recall_fail: 66.79\n    recall_pass: 97.33\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 14.09\n    n_instances: 9335\n    n_truncated: 234\n    n_unparseable: 0\n- exp_id: cls8b-s42-ckpt1200-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.84\n    f1_macro: 77.47\n    f1_fail: 65.49\n    f1_pass: 89.45\n    precision_fail: 77.52\n    recall_fail: 56.69\n    precision_pass: 85.4\n    recall_pass: 93.91\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.89\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-s42-ckpt1400-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.47\n    f1_macro: 78.9\n    f1_fail: 67.13\n    f1_pass: 90.67\n    precision_fail: 86.43\n    recall_fail: 54.88\n    precision_pass: 85.27\n    recall_pass: 96.81\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 12.51\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-s42-ckpt1600-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.99\n    f1_macro: 78.94\n    f1_fail: 67.65\n    f1_pass: 90.22\n    precision_fail: 81.06\n    recall_fail: 58.05\n    precision_pass: 85.93\n    recall_pass: 94.97\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 12.03\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-s42-ckpt1200-val8192-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1200-val8192-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.76\n    f1_macro: 81.25\n    f1_fail: 70.2\n    f1_pass: 92.3\n    precision_fail: 85\n    recall_fail: 59.8\n    precision_pass: 88.3\n    recall_pass: 96.7\n    majority_baseline: 75.9\n    gap_vs_majority: 11.9\n    unparseable: 9\n- exp_id: cls8b-s42-ckpt1600-val8192-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 86.75\n    f1_macro: 78.94\n    f1_fail: 66.12\n    f1_pass: 91.76\n    precision_fail: 86.28\n    precision_pass: 86.83\n    recall_fail: 53.6\n    recall_pass: 97.29\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 10.87\n    unparseable: 9\n    total: 9335\n- exp_id: cls8b-s42-ckpt800-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.53\n    f1_macro: 78.97\n    f1_fail: 69.17\n    f1_pass: 88.77\n    precision_fail: 70.07\n    recall_fail: 68.29\n    precision_pass: 88.36\n    recall_pass: 89.18\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.58\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6600-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.23\n    f1_macro: 79.02\n    f1_fail: 65.9\n    f1_pass: 92.14\n    precision_fail: 92.6\n    recall_fail: 51.15\n    precision_pass: 86.4\n    recall_pass: 98.7\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.36\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls4b-v5-ckpt4600-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.63\n    f1_macro: 75.63\n    f1_fail: 61.67\n    f1_pass: 89.59\n    precision_fail: 84.03\n    recall_fail: 48.72\n    precision_pass: 83.55\n    recall_pass: 96.57\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.67\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6400-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.48\n    f1_macro: 79.66\n    f1_fail: 67.04\n    f1_pass: 92.27\n    precision_fail: 91.81\n    recall_fail: 52.8\n    precision_pass: 86.78\n    recall_pass: 98.5\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.6\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls8b-seed123-ckpt6200-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.52\n    f1_macro: 79.26\n    f1_fail: 66.16\n    f1_pass: 92.35\n    precision_fail: 95.63\n    recall_fail: 50.58\n    precision_pass: 86.33\n    recall_pass: 99.27\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.64\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls4b-v5-ckpt4400-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.24\n    f1_macro: 74.44\n    f1_fail: 59.45\n    f1_pass: 89.44\n    precision_fail: 85.98\n    recall_fail: 45.43\n    precision_pass: 82.78\n    recall_pass: 97.25\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.28\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt3000-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.6\n    f1_macro: 78.38\n    f1_fail: 65.89\n    f1_pass: 90.87\n    precision_fail: 91.65\n    recall_fail: 51.44\n    precision_pass: 84.52\n    recall_pass: 98.26\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 12.64\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6633-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.1\n    f1_macro: 78.79\n    f1_fail: 65.52\n    f1_pass: 92.07\n    precision_fail: 92.26\n    recall_fail: 50.8\n    precision_pass: 86.31\n    recall_pass: 98.64\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.23\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls8b-seed123-ckpt3000-test8192-eval-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-seed123-ckpt800-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-seed123-ckpt800-test5120-eval-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 75.33\n    f1_macro: 67.03\n    f1_fail: 50.5\n    f1_pass: 83.6\n    precision_fail: 55.2\n    recall_fail: 46.5\n    precision_pass: 81.3\n    recall_pass: 86\n    majority_baseline: 73\n    gap_vs_majority_pp: 2.4\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6200-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt6400-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt200-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt6200-test-eval-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.7\n    f1_fail: 63.71\n    f1_pass: 90.31\n    f1_macro: 77.01\n    precision_fail: 88.84\n    precision_pass: 83.96\n    recall_fail: 49.66\n    recall_pass: 97.69\n    n_instances: 9784\n    n_cls_unparseable: 0\n- exp_id: cls8b-seed123-ckpt6400-test-eval-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.08\n    f1_fail: 65.32\n    f1_pass: 90.49\n    f1_macro: 77.91\n    precision_fail: 87.92\n    precision_pass: 84.54\n    recall_fail: 51.97\n    recall_pass: 97.35\n    n_instances: 9784\n    n_cls_unparseable: 0\n- exp_id: cls4b-v5-ckpt600-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 77.74\n    f1_macro: 74.74\n    f1_fail: 66.03\n    f1_pass: 83.44\n    precision_fail: 56.21\n    recall_fail: 80.01\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 4.78\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6600-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.9\n    f1_macro: 77.58\n    pass_f1: 90.4\n    fail_f1: 64.8\n    pass_precision: 84.3\n    pass_recall: 97.4\n    fail_precision: 87.8\n    fail_recall: 51.3\n    n_samples: 9784\n    n_pass: 7138\n    n_fail: 2646\n    majority_baseline: 73\n    unparseable: 0\n    confusion_matrix:\n      fail_as_fail: 1357\n      fail_as_pass: 1289\n      pass_as_fail: 188\n      pass_as_pass: 6950\n- exp_id: cls8b-s42-ckpt200-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 70.07\n    f1_macro: 68.18\n    pass_f1: 75.9\n    fail_f1: 60.4\n    pass_precision: 91.8\n    pass_recall: 64.7\n    fail_precision: 47\n    fail_recall: 84.5\n    n_samples: 9784\n    n_pass: 7138\n    n_fail: 2646\n    majority_baseline: 73\n    unparseable: 0\n    confusion_matrix:\n      fail_as_fail: 2235\n      fail_as_pass: 411\n      pass_as_fail: 2517\n      pass_as_pass: 4621\n- exp_id: cls8b-s42-ckpt1000-test-seq2048-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 82.83\n    f1_macro: 76.88\n    fail_precision: 72.2\n    fail_recall: 59.3\n    fail_f1: 65.2\n    pass_precision: 85.9\n    pass_recall: 91.5\n    pass_f1: 88.6\n    unparseable: 136\n- exp_id: cls4b-v5-ckpt4000-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt6633-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.89\n    f1_macro: 77.56\n    f1_fail: 64.7\n    f1_pass: 90.4\n    precision_fail: 87.8\n    recall_fail: 51.2\n    precision_pass: 84.3\n    recall_pass: 97.4\n    majority_baseline: 73\n    gap_vs_majority_pp: 11.9\n    total_samples: 9784\n    unparseable_count: 0\n- exp_id: cls8b-seed123-ckpt200-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 72.55\n    f1_macro: 70.18\n    pass_f1: 78.58\n    fail_f1: 61.78\n    pass_precision: 91.21\n    pass_recall: 69.02\n    fail_precision: 49.54\n    fail_recall: 82.05\n    n_samples: 9784\n    n_pass: 7138\n    n_fail: 2646\n    majority_baseline: 72.96\n    unparseable: 0\n    confusion_matrix:\n      tn: 2171\n      fp: 475\n      fn: 2211\n      tp: 4927\n- exp_id: cwm8b-ckpt400-test-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm-rank32-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm-4b-rank32-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm-rank32-ablation-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87\n    exact_match_rate: 83.4\n    fail_f1: 87.1\n    pass_f1: 86.9\n    train_loss_final: 0.0152\n    train_loss_avg: 0.2536\n    eval_loss: 0.0688\n    train_runtime_sec: 5003\n    test_set_size: 1890\n    vs_rank16_baseline: -0.51\n    rank16_baseline_accuracy: 87.51\n- exp_id: cwm-rank64-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm-4b-rank64-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: s42-extended-val-sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm-rank32-alpha64-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.04\n    pass_f1: 86.79\n    fail_f1: 87.27\n    f1_macro: 87.03\n    pass_precision: 91.8\n    pass_recall: 82.3\n    fail_precision: 82.9\n    fail_recall: 92.1\n    exact_match_rate: 84.55\n    train_loss: 0.2069\n    eval_loss: 0.0606\n    n_instances: 1890\n    vs_rank16_baseline: -0.47\n    rank16_baseline_accuracy: 87.51\n- exp_id: cls8b-s42-extended-val-sweep\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: s42-extended-val-sweep-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-seq8192\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-seq4096\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-seq8192-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-gpu1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt1000-test-mutation\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1000-test-mutation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt3600-test\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt3600-mutation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 84.4849\n    overall_correct: 8266\n    overall_total: 9784\n    gold_accuracy: 96.2443\n    gold_correct: 4459\n    gold_total: 4633\n    mutation_operator_swap_accuracy: 81.3822\n    mutation_operator_swap_correct: 2732\n    mutation_operator_swap_total: 3357\n    mutation_off_by_one_accuracy: 86.8852\n    mutation_off_by_one_correct: 159\n    mutation_off_by_one_total: 183\n    mutation_return_value_accuracy: 75.4448\n    mutation_return_value_correct: 424\n    mutation_return_value_total: 562\n    mutation_boundary_removal_accuracy: 46.9018\n    mutation_boundary_removal_correct: 492\n    mutation_boundary_removal_total: 1049\n- exp_id: cls8b-s42-ckpt3600-seq2048-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.04\n    f1_macro: 76.8\n    unparseable: 136\n    n_samples: 9784\n    seq_length: 2048\n- exp_id: repo-level-cwm-8b-conda-v6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm8b-ckpt400-test-eval-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm8b-ckpt400-test-eval-v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt3600-test-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.48\n    f1_macro: 78.17\n    fail_recall: 56.8\n    pass_recall: 94.8\n    n_samples: 9784\n    note: reproduces v1 exactly\n- exp_id: cls8b-seed123-ckpt3000-mutation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.6\n    boundary_removal: 44.9\n    operator_swap: 82.6\n    return_value: 66.4\n    off_by_one: 79.2\n    gold: 99.6\n    n_samples: 9784\n- exp_id: cwm8b-ckpt400-test-eval-shard2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: cls4b-ckpt4600-test-mutation-pr\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.63\n    gold_acc: 98.25\n    operator_swap_acc: 78.91\n    return_value_acc: 67.97\n    off_by_one_acc: 58.47\n    boundary_removal_acc: 46.9\n    n_instances: 9784\n    note: off_by_one recall_fail=0 (all predicted pass); boundary_removal identical\n      to 8B\n- exp_id: cwm4b-s42-mutation-breakdown\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 58.04\n    parseable_rate: 46.3\n    parseable_only_accuracy: 42.9\n    gold_parse_rate: 43.5\n    gold_parseable_acc: 23.5\n    operator_swap_parse_rate: 56.9\n    operator_swap_parseable_acc: 63.1\n    off_by_one_parse_rate: 4.4\n    off_by_one_parseable_acc: 0\n    return_value_parse_rate: 48.8\n    return_value_parseable_acc: 27\n    boundary_removal_parse_rate: 30.6\n    boundary_removal_parseable_acc: 59.2\n    n_instances: 9784\n- exp_id: cwm8b-ckpt400-test-eval-shard3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm8b-ckpt400-test-eval-shard4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: deepseek-cls-repo\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: deepseek-cwm-func\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: deepseek-cls-func\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: deepseek-cwm-func-s123\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T07:38:38.433Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T07:38:38.433Z",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-16T07:38:38.454Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Repo-level CLS显著优于CWM，DeepSeek复现确认架构无关性，formulation advantage story完整成立
核心假设：['Repo-level CLS多seed稳定≥85% accuracy，fail_f1≥75%（当前单seed: 84.79%/81.18%）', 'CWM repo-level unparseable rate ≥80%被接受为formulation固有缺陷而非调参不足', 'DeepSeek function-level复现CLS≈CWM pattern，确认结论非Qwen-specific', '8B scaling gap (2.43pp) + repo-level gap共同构成complexity-dependent advantage的完整证据链']
关键指标范围：{'repo_cls_accuracy_multiseed': [84, 88], 'repo_cls_fail_f1': [72, 82], 'repo_cwm_unparseable_rate': [0.8, 0.95], 'func_8b_cls_vs_cwm_gap_pp': [2.0, 3.5], 'deepseek_func_cls_cwm_gap_pp': [-1.0, 1.5], 'oracle_ensemble_accuracy': [90, 93]}
叙事方向：Classification reformulation提供complexity-dependent scaling advantage: function-level equivalence → 8B divergence → repo-level CWM彻底崩溃。三级证据链完整，original claims无需调整。Complementary errors + oracle ensemble作为bonus contribution。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: exec-sim-repair-verifier

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
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: deepseek-cls-func
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: deepseek-cwm-func-s123
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}

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
  "promptId": "a7f03308-ef13-4d36-8d05-7c5b8556cf68",
  "type": "user",
  "uuid": "0225322d-611a-49e7-9e4b-719758d33fed",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T07:38:38.452Z_

```json
{
  "parentUuid": "0225322d-611a-49e7-9e4b-719758d33fed",
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
  "uuid": "1e0cd442-1e2c-42a5-9092-a0cd0a4ae95a",
  "timestamp": "2026-05-16T07:38:38.452Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T07:38:38.452Z_

```json
{
  "parentUuid": "1e0cd442-1e2c-42a5-9092-a0cd0a4ae95a",
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
  "uuid": "dabd01b2-4c83-48de-897e-70cc636aed54",
  "timestamp": "2026-05-16T07:38:38.452Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T07:38:38.452Z_

```json
{
  "parentUuid": "dabd01b2-4c83-48de-897e-70cc636aed54",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1c5600f4-c587-4baf-bf8f-73e09b09f9bf",
  "timestamp": "2026-05-16T07:38:38.452Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Repo-level CLS显著优于CWM，DeepSeek复现确认架构无关性，formulation advantage story完整成立 核心假设：['Repo-level CLS多seed稳定≥85% accuracy，fail_f1≥75%（当前单seed: 84.79%/81.18%）', 'CW…",
  "leafUuid": "1c5600f4-c587-4baf-bf8f-73e09b09f9bf",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Define best-tier results for repo-level verification via three-level evidence chain",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f"
}
```

---

### Assistant

_source line 9 · 2026-05-16T07:38:42.033Z_

Let me first review the current experiment plan and registry to understand which experiments are still "planned" and need predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c5600f4-c587-4baf-bf8f-73e09b09f9bf",
  "isSidechain": false,
  "requestId": "req_011Cb5sEGxdkRi7PQRdrvx8W",
  "type": "assistant",
  "uuid": "90bcc0b7-18f9-4d14-9f1f-6d88f56838d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NreXgTX48VA2iF6k6VCAbH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 30569,
      "cache_read_input_tokens": 11447,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 244,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 30569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30569
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

_source line 10 · 2026-05-16T07:38:47.531Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MYuQAL6jRk9bFN4GGrA14N`</summary>

```json
{
  "description": "Find planned experiments",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_16, search for files related to experiment planning. I need to find:\n1. The experiment_plan file (likely YAML) to identify all experiments with status \"planned\"\n2. Any files describing the \"best\" tier definition\n3. Any files with DeepSeek experiment configs or repo-level experiment details\n\nSearch broadly — check for .yaml, .yml, .md, .json files in the project root and subdirectories. Report the full content of any experiment plan files and tier definition files.",
  "subagent_type": "Explore"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90bcc0b7-18f9-4d14-9f1f-6d88f56838d4",
  "isSidechain": false,
  "requestId": "req_011Cb5sEGxdkRi7PQRdrvx8W",
  "type": "assistant",
  "uuid": "a7789b1b-89d6-45ed-a4d7-11c42565fbc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NreXgTX48VA2iF6k6VCAbH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 30569,
      "cache_read_input_tokens": 11447,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 244,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 30569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30569
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

_source line 11 · 2026-05-16T07:39:42.318Z_

<details><summary>↩ Tool result · `toolu_01MYuQAL6jRk9bFN4GGrA14N`</summary>

```text
Perfect! Now I have comprehensive information. Let me compile the final report:

## Summary of Experiment Planning Files Found

I've successfully located and analyzed the experiment planning files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/`. Here are my findings:

### 1. **Main Experiment Plan File**
**Path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/experiment_plan.yaml`

This YAML file contains 13 main experiments with the following structure:

**Experiments with Status "PREPARING":**
- **cwm-baseline** (Claim 1): Train CWM generation baseline to predict execution output vs pass/fail classification. Depends on mvp-b-train.

**Experiments without explicit "planned" status (implicitly planned/pending):**
- multi-seed-core (Claim 1): Multi-seed validation with seeds {0, 1, 42}, statistical significance testing
- trace-then-judge (Claim 1): Chain-of-thought ablation with ~50 token execution reasoning traces
- traj-level-finetuned (Claim 1): Trajectory-level resolved/unresolved prediction baseline
- model-size-scaling (Claim 1): Scale from 4B to 8B, with sub_experiments on cuda:0 and cuda:1
- per-test-precision-recall (Claim 2): Diagnostic signal quality measurement
- oracle-f2p-stratified (Claim 3): Stratified oracle analysis by F2P test count
- block-corr-empirical (Claim 3): Empirical validation of block-correlation assumption
- swebench-pertest-data (Claims 1,2,3): Docker re-evaluation for SWE-bench-PerTest dataset (500 instances × 16 candidates)
- repo-level-training (Claims 1,2): Fine-tune Qwen3-4B/8B on repo-level data using SWE-bench-PerTest
- llm-judge-baseline (Claims 1,3): Qwen3-8B/32B zero-shot baselines with sub_experiments
- per-test-majority-voting (Claim 1): K=3 majority voting for self-consistency
- diagnostic-rerepair (Claim 2): Proof-of-concept downstream experiment
- oracle-total-validated (Claim 3): Status DONE

---

### 2. **Tier Definition File**
**Path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/meta.yaml`

This file defines three tiers (best/median/worst) with detailed assumptions and number ranges:

**BEST TIER:**
- Repo-level CLS F1: 78-85%
- Repo-level CWM F1: 65-75%
- Repo-level gap: 5-15pp
- CWM unparseable/truncated: 15-35%
- Diagnostic re-repair resolve rate gain: 3-8pp
- Narrative: Full 3-claim story holds; complexity-dependent reformulation advantage confirmed
- Target venue: EMNLP Main

**MEDIAN TIER:**
- Repo-level CLS F1: 72-80%
- Repo-level CWM F1: 68-77%
- Repo-level gap: 2-5pp
- CWM unparseable/truncated: 5-14%
- Diagnostic re-repair resolve rate gain: 0.5-3pp
- Narrative: Reframe Claims 1+3; Claim 2 as hypothesis
- Target venue: EMNLP Findings

**WORST TIER:**
- Repo-level gap: <2pp, potentially 0.6pp
- CWM unparseable/truncated: ~5% or lower
- Diagnostic re-repair gain: ~0.5pp or less (not significant)
- Narrative: Pivot to analysis paper showing classification ≈ generation equivalence; per-test doesn't help in practice despite theoretical appeal
- Target venue: EMNLP Findings or ICSE 2027

---

### 3. **Dream Report Files (Three Tier Scenarios)**
**Paths:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/best/imagined_experiments.yaml`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/median/imagined_experiments.yaml`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/worst/imagined_experiments.yaml`

These files contain detailed imagined experiment results for each tier, including:
- **Multi-Seed Core Validation** with expected F1 scores and bootstrap CIs
- **Trace-then-Judge Ablation** results
- **Trajectory-Level Fine-tuned Baseline** comparisons
- **Model Size Scaling (4B→8B)** behavior
- **Per-test Precision/Recall Analysis**
- **Oracle F2P-Stratified Analysis** showing T=1 (68.7%), T=2 (16.2%), T≥3 (15.1%)
- **Block-Correlation Empirical Validation**
- **SWE-bench-PerTest Dataset Construction** (478-500 successful instances)
- **Repo-Level Training and Evaluation**
- **LLM-as-Judge Baselines** (Qwen3-8B/32B zero-shot)
- **Per-Test Majority Voting** results

---

### 4. **DeepSeek Experiment Configs**
**Paths with DeepSeek references:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_code_adapt-eval-deepseek_20260516T052154_result.json`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_train_deepseek-all-gpus_20260516T061139_result.json`

**Key DeepSeek Training Details:**
- Model: `deepseek-ai/deepseek-coder-6.7b-instruct` (located at `/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct/`)
- Three training tasks submitted:
  - **cuda:0**: `deepseek-cls-repo` - Classification on repo-level (70,748 samples)
  - **cuda:1**: `deepseek-cwm-func` - CWM on function-level (15,290 samples)
  - **cuda:2**: `deepseek-cls-func` - Classification on function-level (15,290 samples)
- Eval scripts adapted with:
  - Model family detection (qwen/deepseek/auto)
  - Chat template kwargs handling (no thinking mode for DeepSeek)
  - Custom stop token IDs for DeepSeek (`<|EOT|>` and `<｜end▁of▁sentence｜>`)
  - Safe chat template application for unsupported system roles

---

### 5. **Registry and Additional Config Files**
**Paths:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/registry.yaml`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/dream_registry.yaml`

These contain experiment metadata with status tracking, metrics, completion timestamps, and detailed notes.

---

### Summary Statistics:
- **Total experiments in plan:** 13 main experiments
- **Experiments with "PREPARING" status:** 1 (cwm-baseline)
- **Experiments with "DONE" status:** 1 (oracle-total-validated)
- **Planned but status not yet specified:** 11 experiments
- **Three experimental tiers defined:** best, median, worst with different narrative directions
- **Repo-level focus:** SWE-bench-PerTest dataset construction with 478-500 instances × 16 candidates
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7789b1b-89d6-45ed-a4d7-11c42565fbc4",
  "isSidechain": false,
  "promptId": "a7f03308-ef13-4d36-8d05-7c5b8556cf68",
  "type": "user",
  "uuid": "2ba75b26-6d39-4f2b-9cc4-234a1fecd1d5",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_16, search for files related to experiment planning. I need to find:\n1. The experiment_plan file (likely YAML) to identify all experiments with status \"planned\"\n2. Any files describing the \"best\" tier definition\n3. Any files with DeepSeek experiment configs or repo-level experiment details\n\nSearch broadly — check for .yaml, .yml, .md, .json files in the project root and subdirectories. Report the full content of any experiment plan files and tier definition files.",
    "agentId": "a9f0bac6f7f476666",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive information. Let me compile the final report:\n\n## Summary of Experiment Planning Files Found\n\nI've successfully located and analyzed the experiment planning files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/`. Here are my findings:\n\n### 1. **Main Experiment Plan File**\n**Path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/experiment_plan.yaml`\n\nThis YAML file contains 13 main experiments with the following structure:\n\n**Experiments with Status \"PREPARING\":**\n- **cwm-baseline** (Claim 1): Train CWM generation baseline to predict execution output vs pass/fail classification. Depends on mvp-b-train.\n\n**Experiments without explicit \"planned\" status (implicitly planned/pending):**\n- multi-seed-core (Claim 1): Multi-seed validation with seeds {0, 1, 42}, statistical significance testing\n- trace-then-judge (Claim 1): Chain-of-thought ablation with ~50 token execution reasoning traces\n- traj-level-finetuned (Claim 1): Trajectory-level resolved/unresolved prediction baseline\n- model-size-scaling (Claim 1): Scale from 4B to 8B, with sub_experiments on cuda:0 and cuda:1\n- per-test-precision-recall (Claim 2): Diagnostic signal quality measurement\n- oracle-f2p-stratified (Claim 3): Stratified oracle analysis by F2P test count\n- block-corr-empirical (Claim 3): Empirical validation of block-correlation assumption\n- swebench-pertest-data (Claims 1,2,3): Docker re-evaluation for SWE-bench-PerTest dataset (500 instances × 16 candidates)\n- repo-level-training (Claims 1,2): Fine-tune Qwen3-4B/8B on repo-level data using SWE-bench-PerTest\n- llm-judge-baseline (Claims 1,3): Qwen3-8B/32B zero-shot baselines with sub_experiments\n- per-test-majority-voting (Claim 1): K=3 majority voting for self-consistency\n- diagnostic-rerepair (Claim 2): Proof-of-concept downstream experiment\n- oracle-total-validated (Claim 3): Status DONE\n\n---\n\n### 2. **Tier Definition File**\n**Path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/meta.yaml`\n\nThis file defines three tiers (best/median/worst) with detailed assumptions and number ranges:\n\n**BEST TIER:**\n- Repo-level CLS F1: 78-85%\n- Repo-level CWM F1: 65-75%\n- Repo-level gap: 5-15pp\n- CWM unparseable/truncated: 15-35%\n- Diagnostic re-repair resolve rate gain: 3-8pp\n- Narrative: Full 3-claim story holds; complexity-dependent reformulation advantage confirmed\n- Target venue: EMNLP Main\n\n**MEDIAN TIER:**\n- Repo-level CLS F1: 72-80%\n- Repo-level CWM F1: 68-77%\n- Repo-level gap: 2-5pp\n- CWM unparseable/truncated: 5-14%\n- Diagnostic re-repair resolve rate gain: 0.5-3pp\n- Narrative: Reframe Claims 1+3; Claim 2 as hypothesis\n- Target venue: EMNLP Findings\n\n**WORST TIER:**\n- Repo-level gap: <2pp, potentially 0.6pp\n- CWM unparseable/truncated: ~5% or lower\n- Diagnostic re-repair gain: ~0.5pp or less (not significant)\n- Narrative: Pivot to analysis paper showing classification ≈ generation equivalence; per-test doesn't help in practice despite theoretical appeal\n- Target venue: EMNLP Findings or ICSE 2027\n\n---\n\n### 3. **Dream Report Files (Three Tier Scenarios)**\n**Paths:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/best/imagined_experiments.yaml`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/median/imagined_experiments.yaml`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/worst/imagined_experiments.yaml`\n\nThese files contain detailed imagined experiment results for each tier, including:\n- **Multi-Seed Core Validation** with expected F1 scores and bootstrap CIs\n- **Trace-then-Judge Ablation** results\n- **Trajectory-Level Fine-tuned Baseline** comparisons\n- **Model Size Scaling (4B→8B)** behavior\n- **Per-test Precision/Recall Analysis**\n- **Oracle F2P-Stratified Analysis** showing T=1 (68.7%), T=2 (16.2%), T≥3 (15.1%)\n- **Block-Correlation Empirical Validation**\n- **SWE-bench-PerTest Dataset Construction** (478-500 successful instances)\n- **Repo-Level Training and Evaluation**\n- **LLM-as-Judge Baselines** (Qwen3-8B/32B zero-shot)\n- **Per-Test Majority Voting** results\n\n---\n\n### 4. **DeepSeek Experiment Configs**\n**Paths with DeepSeek references:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_code_adapt-eval-deepseek_20260516T052154_result.json`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_train_deepseek-all-gpus_20260516T061139_result.json`\n\n**Key DeepSeek Training Details:**\n- Model: `deepseek-ai/deepseek-coder-6.7b-instruct` (located at `/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct/`)\n- Three training tasks submitted:\n  - **cuda:0**: `deepseek-cls-repo` - Classification on repo-level (70,748 samples)\n  - **cuda:1**: `deepseek-cwm-func` - CWM on function-level (15,290 samples)\n  - **cuda:2**: `deepseek-cls-func` - Classification on function-level (15,290 samples)\n- Eval scripts adapted with:\n  - Model family detection (qwen/deepseek/auto)\n  - Chat template kwargs handling (no thinking mode for DeepSeek)\n  - Custom stop token IDs for DeepSeek (`<|EOT|>` and `<｜end▁of▁sentence｜>`)\n  - Safe chat template application for unsupported system roles\n\n---\n\n### 5. **Registry and Additional Config Files**\n**Paths:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/registry.yaml`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/dream_registry.yaml`\n\nThese contain experiment metadata with status tracking, metrics, completion timestamps, and detailed notes.\n\n---\n\n### Summary Statistics:\n- **Total experiments in plan:** 13 main experiments\n- **Experiments with \"PREPARING\" status:** 1 (cwm-baseline)\n- **Experiments with \"DONE\" status:** 1 (oracle-total-validated)\n- **Planned but status not yet specified:** 11 experiments\n- **Three experimental tiers defined:** best, median, worst with different narrative directions\n- **Repo-level focus:** SWE-bench-PerTest dataset construction with 478-500 instances × 16 candidates"
      }
    ],
    "totalDurationMs": 54781,
    "totalTokens": 88173,
    "totalToolUseCount": 28,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 84652,
      "output_tokens": 2100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1416
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 2100,
          "cache_read_input_tokens": 84652,
          "cache_creation_input_tokens": 1416,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1416,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 12,
      "searchCount": 2,
      "bashCount": 14,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "a7789b1b-89d6-45ed-a4d7-11c42565fbc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-16T07:40:30.872Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now look at the experiment plan more carefully to identify which experiments are still "planned" (not DONE). From the context provided in the user's message, I can see the experiment_plan entries and their statuses. Let me identify the "planned" ones:

1. `diagnostic-rerepair` - status: planned
2. `swebench-pertest-data` - status: planned

And there are RUNNING experiments:
- `deepseek-cls-repo`
- `deepseek-cwm-func`
- `deepseek-cls-func`
- `deepseek-cwm-func-s123`


- 
Actually, I need to clarify what the user is asking for. They want predicted data for the experiments with "planned" status, which are `diagnostic-rerepair` and `swebench-pertest-data`, but I should also consider the RUNNING experiments since they don't have results yet either. Looking at the experiment_plan more carefully, only two experiments are marked as "planned": diagnostic-rerepair and swebench-pertest-data. But the DeepSeek experiments are actively running in the registry and seem crucial for validating the architecture-agnostic assumptions in the Phase 1 best tier definition, so they're clearly part of the broader project even if not formally listed in the plan. I should focus on the officially planned experiments first, but keep in mind these running DeepSeek experiments are also important context.

Now I'm reviewing the Phase 1 best tier criteria more carefully. The core assumptions involve multi-seed repo-level CLS stability above 85%, CWM's unparseable rate as evidence of formulation limitations rather than tuning issues, DeepSeek function-level results confirming the pattern isn't Qwen-specific, and the 8B scaling gap combined with repo-level performance gaps forming a complete evidence chain for complexity-dependent advantages. The key metrics I'm tracking have specific ranges: repo CLS accuracy between 84-88%, fail F1 between 72-82%, CWM unparseable rate between 0.8-0.95%, and the 8B versus CWM gap in the 2+ percentage point range.

Looking at what's actually running versus what's still planned, I see the DeepSeek function-level experiments are currently executing, while diagnostic-rerepair and swebench-pertest-data remain in the planned queue. I need to focus on predicting outcomes for the pending experiments rather than getting caught up in the full registry. explicitly "planned" in the experiment_plan AND the running DeepSeek experiments AND the repo-level multi-seed experiments that support the best tier narrative.

Let me look at the full experiment list more carefully. The plan shows diagnostic-rerepair and swebench-pertest-data as the only two marked "planned", with repo-level-training having failed initially but succeeding in later versions. But the user specifically asked for details on each "planned" experiment in the experiment_plan, which would be just those two—though that feels too narrow given the best tier's core assumptions about repo-level multi-seed CLS, DeepSeek function-level reproduction, and the CWM repo-level unparseable rate threshold.

I need to identify which experiments are still missing results but are critical for supporting the best tier: diagnostic-rerepair and swebench-pertest-data from the plan, plus the running DeepSeek experiments and any repo-level multi-seed CLS work that hasn't completed yet. I need to check what format was used in previous dream reports to understand what the user expects. Looking at the best tier definition, I see there are several experiments beyond the two explicitly planned ones—repo-level multi-seed runs, DeepSeek results, and oracle ensemble metrics—and some of these are already running or partially complete, so I should compose an answer that covers both the planned experiments and the additional ones implied by the best tier narrative.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ba75b26-6d39-4f2b-9cc4-234a1fecd1d5",
  "isSidechain": false,
  "requestId": "req_011Cb5sJyxKzpTwcPzq2cLp9",
  "type": "assistant",
  "uuid": "af153d1c-c9ec-4093-99dd-81cd2e004873",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mj8Qf82DGsdvDhTdvy14PD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2353,
      "cache_read_input_tokens": 42016,
      "output_tokens": 2461,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2353,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2461,
          "cache_read_input_tokens": 42016,
          "cache_creation_input_tokens": 2353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2353
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

_source line 13 · 2026-05-16T07:40:30.890Z_

Let me check the existing dream report format and the current state of running experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af153d1c-c9ec-4093-99dd-81cd2e004873",
  "isSidechain": false,
  "requestId": "req_011Cb5sJyxKzpTwcPzq2cLp9",
  "type": "assistant",
  "uuid": "0a9827c2-e52a-4503-a6cd-3ab480860e6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mj8Qf82DGsdvDhTdvy14PD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2353,
      "cache_read_input_tokens": 42016,
      "output_tokens": 2461,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2353,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2461,
          "cache_read_input_tokens": 42016,
          "cache_creation_input_tokens": 2353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2353
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

_source line 14 · 2026-05-16T07:40:30.915Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01P9YJJAYPjv8TsGfUD5J14n`</summary>

```json
{
  "pattern": "**/dream_reports/**/best/imagined_experiments.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a9827c2-e52a-4503-a6cd-3ab480860e6a",
  "isSidechain": false,
  "requestId": "req_011Cb5sJyxKzpTwcPzq2cLp9",
  "type": "assistant",
  "uuid": "5d688381-a4ee-4ae9-8ad4-6aae07679ce5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mj8Qf82DGsdvDhTdvy14PD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2353,
      "cache_read_input_tokens": 42016,
      "output_tokens": 2461,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2353,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2461,
          "cache_read_input_tokens": 42016,
          "cache_creation_input_tokens": 2353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2353
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

_source line 15 · 2026-05-16T07:40:30.945Z_

<details><summary>↩ Tool result · `toolu_01P9YJJAYPjv8TsGfUD5J14n`</summary>

```text
projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T214810/best/imagined_experiments.yaml
projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/best/imagined_experiments.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d688381-a4ee-4ae9-8ad4-6aae07679ce5",
  "isSidechain": false,
  "promptId": "a7f03308-ef13-4d36-8d05-7c5b8556cf68",
  "type": "user",
  "uuid": "fda73a64-23f2-4429-95bf-8879aa685897",
  "toolUseResult": {
    "filenames": [
      "projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T214810/best/imagined_experiments.yaml",
      "projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/best/imagined_experiments.yaml"
    ],
    "durationMs": 23,
    "numFiles": 2,
    "truncated": false
  },
  "sourceToolAssistantUUID": "5d688381-a4ee-4ae9-8ad4-6aae07679ce5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Repo-level CLS显著优于CWM，DeepSeek复现确认架构无关性，formulation advantage story完整成立 核心假设：['Repo-level CLS多seed稳定≥85% accuracy，fail_f1≥75%（当前单seed: 84.79%/81.18%）', 'CW…",
  "leafUuid": "fda73a64-23f2-4429-95bf-8879aa685897",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Define best-tier results for repo-level verification via three-level evidence chain",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f"
}
```

---

### Tool call

_source line 18 · 2026-05-16T07:40:34.158Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LV2QxmdukrA6VoPB8kYrZg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fda73a64-23f2-4429-95bf-8879aa685897",
  "isSidechain": false,
  "requestId": "req_011Cb5sNZv54K2EGqSQBYkWg",
  "type": "assistant",
  "uuid": "0ffaea46-f380-4a15-a760-e072a4493b13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFfm2NmFoUXdj2ZRsdnDH3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2537,
      "cache_read_input_tokens": 44369,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2537,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 44369,
          "cache_creation_input_tokens": 2537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2537
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

_source line 19 · 2026-05-16T07:40:34.454Z_

<details><summary>↩ Tool result · `toolu_01LV2QxmdukrA6VoPB8kYrZg`</summary>

```text
1	tier: best
2	narrative_guidance: 'Full 3-claim story holds. Function-level CLS ≈ CWM null result
3	  is the setup（classification 不是 trivially easier）;
4	
5	  repo-level gap ~12pp 是 punchline（CWM failure modes 仅在复杂 trace 下显现）。
6	
7	  Diagnostic re-repair 以 5.5pp resolve rate gain 验证 Claim 2 的实用价值。
8	
9	  Oracle frontier 提供部署决策框架：per-test 优势集中在 multi-F2P 实例（T≥2 = 31.3%）。
10	
11	  Block-correlated errors（ρ≈0.43）放大 per-test 优势，验证 oracle 模拟假设。
12	
13	  Title: Complexity-Dependent Reformulation Advantage. Target: EMNLP Main, 三个 claim
14	  完整成立。
15	
16	  '
17	imagined_experiments:
18	- name: Multi-Seed Core Validation
19	  plan_id: multi-seed-core
20	  description: Classification 和 CWM 各跑 seeds {0,1,42}，报告 mean±std F1，paired bootstrap
21	    CI 检验差异是否显著。
22	  expected_results:
23	    cls_seed0_macro_f1: 87.2
24	    cls_seed1_macro_f1: 87.7
25	    cls_seed42_macro_f1: 87.5
26	    cls_mean_macro_f1: 87.47
27	    cls_std_macro_f1: 0.25
28	    cwm_seed0_macro_f1: 87.0
29	    cwm_seed1_macro_f1: 87.9
30	    cwm_seed42_macro_f1: 87.5
31	    cwm_mean_macro_f1: 87.47
32	    cwm_std_macro_f1: 0.45
33	    paired_diff_mean_pp: 0.0
34	    paired_diff_95ci_lower: -0.85
35	    paired_diff_95ci_upper: 0.85
36	    paired_ttest_pvalue: 0.98
37	    null_result_confirmed: true
38	  result_rationale: '函数级代码（HumanEval/MBPP）execution output 短（通常 <50 tokens），错误类型可预测（AssertionError
39	    占主导），
40	
41	    CWM 的两大 failure modes（token-budget exhaustion 和 string-value prediction errors）在此复杂度下不触发。
42	
43	    三个 seed 的 std 在 0.2-0.5 范围内，反映 LoRA 初始化和 data shuffling 的正常随机性。
44	
45	    CWM std 略高于 classification（0.45 vs 0.25）因为 generation 目标更高维，对初始化更敏感，
46	
47	    但差异不改变结论。95% CI [-0.85, 0.85] 包含 0，p=0.98 远超 0.05 阈值，
48	
49	    cleanly 确认 function-level null result。这为 Claim 1 "complexity-dependent" 叙事提供干净的
50	    baseline：
51	
52	    两种 formulation 在简单代码上无差异，差异仅在复杂度升高时出现。
53	
54	    '
55	  tables:
56	  - name: 'Table 2: Multi-Seed Function-Level Comparison (Macro F1)'
57	    columns:
58	    - Model
59	    - Seed 0
60	    - Seed 1
61	    - Seed 42
62	    - Mean
63	    - Std
64	    rows:
65	    - - Qwen3-4B-Cls
66	      - 87.2
67	      - 87.7
68	      - 87.5
69	      - 87.47
70	      - 0.25
71	    - - Qwen3-4B-CWM
72	      - 87.0
73	      - 87.9
74	      - 87.5
75	      - 87.47
76	      - 0.45
77	    - - Δ (Cls − CWM)
78	      - '+0.2'
79	      - −0.2
80	      - '0.0'
81	      - '0.00'
82	      - —
83	  figures_description:
84	  - 'Figure 2: 三 seed 的 per-class F1 box plot（classification vs CWM），CI 完全重叠，视觉化 null
85	    result'
86	  analysis: "Multi-seed 验证是 Claim 1 的统计基础。CI 完全包含 0 证明函数级等价不是单次实验的偶然。\n论文中应强调：classification\
87	    \ 在函数级「不比 generation 更容易」——这反驳 reviewer \n\"classification is trivially easier\"\
88	    \ 的质疑。真正的优势是 complexity-dependent 的。\n"
89	- name: Trace-then-Judge Ablation
90	  plan_id: trace-then-judge
91	  description: 单模型 chain-of-thought：先生成 ~50 token 执行推理 trace，再输出 pass/fail。检验显式推理在函数级是否有帮助。
92	  expected_results:
93	    ttj_pass_f1: 86.5
94	    ttj_fail_f1: 87.1
95	    ttj_macro_f1: 86.8
96	    ttj_accuracy: 86.9
97	    direct_cls_macro_f1: 87.5
98	    diff_from_direct_cls_pp: -0.7
99	    train_loss: 0.283
100	    eval_loss: 0.071
101	    avg_trace_length_tokens: 38.2
102	    trace_quality_exact_match: 82.5
103	  result_rationale: '在函数级代码上，trace-then-judge 与 direct classification 差异仅 -0.7pp（在
104	    best tier 范围 [-1.5, 1.5] 内）。
105	
106	    原因：函数级 execution 语义简单，模型无需显式推理就能直接判断 pass/fail——
107	
108	    trace 是冗余的中间步骤，略微分散了模型容量（4B 参数需同时学 trace generation + classification），
109	
110	    但因为 trace 很短（平均 38 tokens），overhead 很小。Trace exact match 82.5%（高于 CWM 的 84%
111	
112	    是因为 trace 只需覆盖关键推理步骤，不需精确复现完整 output）。
113	
114	    关键结论：在函数级，显式推理既不帮助也不伤害。这支持 "formulation advantage is about
115	
116	    skipping the generation bottleneck, not about reasoning quality" 的论点。
117	
118	    在 repo-level（未测），trace-then-judge 预期会因 trace 质量下降而退化。
119	
120	    '
121	  tables:
122	  - name: 'Table 3: Formulation Ablation — Function-Level'
123	    columns:
124	    - Method
125	    - Pass F1
126	    - Fail F1
127	    - Macro F1
128	    - Δ vs Direct Cls
129	    rows:
130	    - - Direct Classification
131	      - 87.1
132	      - 87.9
133	      - 87.5
134	      - —
135	    - - Trace-then-Judge (CoT)
136	      - 86.5
137	      - 87.1
138	      - 86.8
139	      - −0.7
140	    - - CWM Generation
141	      - 87.3
142	      - 87.7
143	      - 87.5
144	      - '0.0'
145	  figures_description:
146	  - 'Figure 3: 三种 formulation 的 per-class F1 bar chart，error bars 来自 bootstrap，三者
147	    CI 重叠'
148	  analysis: 'Trace-then-judge 接近 direct classification 证明函数级上显式执行推理是中性的。
149	
150	    三种方法（direct cls, TtJ, CWM）在函数级都 ~87%，共同构成 null result。
151	
152	    这为 repo-level 实验设置了对比：如果 repo-level TtJ 显著低于 direct cls，
153	
154	    则证明 trace generation 在高复杂度下成为瓶颈——而 classification 通过跳过 trace 避开了这个瓶颈。
155	
156	    '
157	- name: Trajectory-Level Finetuned Baseline
158	  plan_id: traj-level-finetuned
159	  description: Qwen3-4B LoRA 训练预测 resolved/unresolved（聚合所有 test）。隔离 granularity 效应。
160	  expected_results:
161	    traj_accuracy: 83.2
162	    traj_resolved_f1: 80.5
163	    traj_unresolved_f1: 84.8
164	    traj_macro_f1: 82.7
165	    traj_auc_roc: 0.882
166	    per_test_cls_derived_traj_acc: 85.3
167	    granularity_effect_pp: 2.1
168	    formulation_effect_pp: 0.0
169	    combined_effect_pp: 2.1
170	    class_balance_resolved_pct: 38.5
171	    class_balance_unresolved_pct: 61.5
172	  result_rationale: 'Trajectory-level 在函数级仍表现合理（83.2% acc）因为 test suites 小（通常 3-8
173	    test cases per problem）。
174	
175	    但比 per-test classification 的 derived trajectory accuracy（85.3%）低 2.1pp——
176	
177	    这是 granularity 效应：trajectory model 必须一次性从所有 test 的 concatenation 做出判断，
178	
179	    而 per-test model 逐个 test 判断后 AND 聚合，降低了每次推理的认知负担。
180	
181	    关键发现：formulation effect = 0pp（因为函数级 CLS ≈ CWM），granularity effect = 2.1pp。
182	
183	    这完成了 2×2 因子分析（formulation × granularity），显示在函数级只有 granularity 轴有微弱效应。
184	
185	    类别不平衡（61.5% unresolved）出现是因为多数 mutation 至少破坏一个 test，
186	
187	    导致 unresolved 成为多数类，unresolved_f1 高于 resolved_f1。
188	
189	    '
190	  tables:
191	  - name: 'Table 4: 2×2 Factorial Decomposition — Function-Level'
192	    columns:
193	    - Formulation
194	    - Granularity
195	    - Traj Acc
196	    - Macro F1
197	    rows:
198	    - - Generation (CWM)
199	      - Per-test
200	      - 85.0%*
201	      - 87.5
202	    - - Classification
203	      - Per-test
204	      - 85.3%*
205	      - 87.5
206	    - - Classification
207	      - Trajectory
208	      - 83.2%
209	      - 82.7
210	    footnotes:
211	    - '*Trajectory accuracy derived from per-test predictions via AND-aggregation'
212	  - name: Effect Decomposition
213	    columns:
214	    - Effect
215	    - Δ Traj Accuracy (pp)
216	    rows:
217	    - - Formulation (Gen→Cls)
218	      - 0.0 — null at function-level
219	    - - Granularity (Traj→Per-test)
220	      - '+2.1'
221	    - - Combined
222	      - '+2.1'
223	  figures_description:
224	  - 'Figure 4: 2×2 factorial heatmap，formulation axis 无差异，granularity axis 有 ~2pp
225	    效应'
226	  analysis: '在函数级，formulation 效应为零（CLS ≈ CWM），只有 granularity 贡献 2.1pp。
227	
228	    这是 best tier 叙事的关键一环：函数级的 2×2 分析为 repo-level 实验提供了 baseline。
229	
230	    如果 repo-level 实验显示 formulation 效应从 0 跳到 12+pp，则证明优势是 complexity-dependent 的。
231	
232	    '
233	- name: Model Size Scaling (4B → 8B)
234	  plan_id: model-size-scaling
235	  description: Classification 和 CWM 各扩展到 8B，验证函数级等价性是否随模型规模保持。
236	  expected_results:
237	    cls_8b_pass_f1: 89.8
238	    cls_8b_fail_f1: 90.4
239	    cls_8b_macro_f1: 90.1
240	    cls_8b_accuracy: 90.2
241	    cwm_8b_pass_f1: 89.5
242	    cwm_8b_fail_f1: 90.1
243	    cwm_8b_macro_f1: 89.8
244	    cwm_8b_accuracy: 89.9
245	    gap_8b_macro_f1_pp: 0.3
246	    gap_4b_macro_f1_pp: 0.0
247	    cls_scaling_gain_pp: 2.6
248	    cwm_scaling_gain_pp: 2.3
249	    cwm_8b_exact_match: 87.5
250	    cwm_8b_unparseable: 0
251	  result_rationale: '函数级 CWM 在 4B 已经不触发 failure modes（unparseable=0, exact_match=84%），
252	
253	    8B 进一步改善 exact match 到 87.5% 但 pass/fail 准确率提升与 classification 相当。
254	
255	    两者在 8B 仍然等价（gap 0.3pp，统计噪声范围内），因为函数级 execution output 短到
256	
257	    即使 4B 也能完整生成——增加参数只改善边际 case 的处理。
258	
259	    Scaling gain 略有差异（Cls +2.6 vs CWM +2.3）但不显著。
260	
261	    这强化了 complexity-dependent 叙事：不是模型太小导致 CWM 差，
262	
263	    而是函数级复杂度太低让 CWM 也能 work。gap 只在 repo-level 复杂度下出现。
264	
265	    '
266	  tables:
267	  - name: 'Table 5: Scaling Behavior — Function-Level'
268	    columns:
269	    - Scale
270	    - Cls Macro F1
271	    - CWM Macro F1
272	    - Gap (pp)
273	    rows:
274	    - - 4B
275	      - 87.5
276	      - 87.5
277	      - 0.0
278	    - - 8B
279	      - 90.1
280	      - 89.8
281	      - 0.3
282	    - - Scaling gain
283	      - '+2.6'
284	      - '+2.3'
285	      - '+0.3'
286	  figures_description:
287	  - 'Figure 5: 4B vs 8B scaling curve，两条线几乎平行，gap 保持在噪声水平'
288	  analysis: '函数级 scaling 实验排除了 "CWM 在更大模型上会超越 classification" 的 reviewer 质疑（至少在函数级）。
289	
290	    两种 formulation 的 scaling rate 相似，说明在此复杂度下两者的 learning dynamics 等价。
291	
292	    论文应指出：真正的 scaling 差异预期出现在 repo-level——CWM 需要更多参数来处理长 trace，
293	
294	    而 classification 因 1-token output 效率更高。
295	
296	    '
297	- name: Per-test Precision/Recall Analysis
298	  plan_id: per-test-precision-recall
299	  description: 在完整测试集上测量 per-test failure prediction 的 precision/recall，评估诊断信号质量。
300	  expected_results:
301	    fail_precision: 87.6
302	    fail_recall: 88.2
303	    fail_f1: 87.9
304	    pass_precision: 87.4
305	    pass_recall: 86.8
306	    pass_f1: 87.1
307	    false_positive_rate_pct: 8.3
308	    false_negative_rate_pct: 11.8
309	    failure_localization_exact_match_pct: 78.2
310	    precision_at_k1: 89.3
311	    precision_at_k3: 85.1
312	  result_rationale: "Fail precision 87.6% 和 recall 88.2% 直接来源于 mvp-b-train 的已有指标。\n\
313	    新增指标 failure_localization_exact_match（78.2%）衡量每个 problem 是否完整识别了所有 failing tests——\n\
314	    低于 per-test F1（87.9%）因为需要所有 test 都判对。但 78% 意味着约 4/5 的 problem \n能获得完全正确的 diagnostic\
315	    \ 信息。FPR 8.3% 足够低（12 次预测 fail 中约 1 次是误报），\n对 downstream re-repair agent 来说是可接受的误报率。\n\
316	    Precision@1（89.3%）表明 top-ranked failing test 几乎总是真实的失败——\n这对 repair agent 的 \"\
317	    先修最可能的 failure\" 策略非常有价值。\n"
318	  tables:
319	  - name: 'Table 6: Diagnostic Signal Quality — Function-Level'
320	    columns:
321	    - Metric
322	    - Fail Class
323	    - Pass Class
324	    - Macro
325	    rows:
326	    - - Precision
327	      - 87.6%
328	      - 87.4%
329	      - 87.5%
330	    - - Recall
331	      - 88.2%
332	      - 86.8%
333	      - 87.5%
334	    - - F1
335	      - 87.9%
336	      - 87.1%
337	      - 87.5%
338	  - name: Failure Localization
339	    columns:
340	    - Metric
341	    - Value
342	    rows:
343	    - - Exact match (all tests correct)
344	      - 78.2%
345	    - - Precision@1
346	      - 89.3%
347	    - - False positive rate
348	      - 8.3%
349	  figures_description:
350	  - 'Figure 6: Precision-Recall curve for fail class，AUC 标注，与 random baseline 对比'
351	  analysis: 'Per-test prediction 质量支撑 Claim 2：diagnostic signal 足够准确以产生实际价值。
352	
353	    78% exact match 意味着大多数情况下 repair agent 获得完全正确的 failing test list。
354	
355	    即使不完全正确，部分 diagnostic 信息仍优于无信息（re-repair 实验将验证这一点）。
356	
357	    '
358	- name: Oracle F2P-Stratified Analysis
359	  plan_id: oracle-f2p-stratified
360	  description: 按 F2P test count (T=1, T=2, T≥3) 分层 oracle 分析，展示 per-test advantage
361	    集中在 multi-test 实例。
362	  expected_results:
363	    T1_pct_instances: 68.7
364	    T1_iid_adv_70_85_pct: 2.0
365	    T1_block_adv_70_85_pct: 10.9
366	    T2_pct_instances: 16.2
367	    T2_iid_adv_70_85_pct: 17.5
368	    T2_block_adv_70_85_pct: 38.0
369	    T3plus_pct_instances: 15.1
370	    T3plus_iid_adv_70_85_pct: 26.5
371	    T3plus_block_adv_70_85_pct: 45.2
372	    weighted_iid_adv_pct: 7.6
373	    weighted_block_adv_pct: 19.5
374	  result_rationale: 'T=1 时 per-test 和 trajectory 对 F2P 部分数学上等价（只有一个 failing test，
375	
376	    per-test 预测和 trajectory 预测携带相同信息）——advantage 仅来自 tie-breaking（iid 2%）
377	
378	    或 block correlation 效应（10.9%）。
379	
380	    T=2 时 advantage 跳升至 17.5%/38.0%：per-test 能区分 "fails test A only" vs "fails both
381	    A and B"，
382	
383	    而 trajectory 将两者都折叠为 "unresolved"。这种信息增益在 candidate ranking 中产生显著差异。
384	
385	    T≥3 时 advantage 最大（26.5%/45.2%）因为 failure pattern 的组合空间增长，
386	
387	    per-test 捕获的信息量远超 trajectory-level。
388	
389	    Block-correlated advantage 始终显著高于 iid（~2-3×）因为 block 错误结构
390	
391	    减少了有效自由度，放大了 per-test 的信息优势。
392	
393	    Population-weighted advantage（7.6% iid / 19.5% block）因 T=1 占 68.7% 而被稀释——
394	
395	    这是诚实的报告，但也说明：如果 deployment 能 filter 出 multi-F2P instances，
396	
397	    per-test 的 ROI 大幅提升。
398	
399	    '
400	  tables:
401	  - name: 'Table 7: Per-test Advantage Stratified by F2P Count (Oracle, acc ∈ [70%,
402	      85%])'
403	    columns:
404	    - F2P Count (T)
405	    - '% Instances'
406	    - Adv (i.i.d.)
407	    - Adv (Block-corr)
408	    rows:
409	    - - T=1
410	      - 68.7%
411	      - 2.0%
412	      - 10.9%
413	    - - T=2
414	      - 16.2%
415	      - 17.5%
416	      - 38.0%
417	    - - T≥3
418	      - 15.1%
419	      - 26.5%
420	      - 45.2%
421	    - - Weighted
422	      - 100%
423	      - 7.6%
424	      - 19.5%
425	  figures_description:
426	  - 'Figure 7: Stacked bar chart 按 T 分层的 per-test advantage，iid vs block 双柱对比'
427	  - 'Figure 8: Advantage vs T 的 scatter plot with fitted curve，展示 advantage 随 T 单调递增'
428	  analysis: '分层分析是 Claim 3 的核心结果。它提供了实用决策框架：
429	
430	    当 instance 预期有 T≥2 个 failing tests（SWE-bench 中 31.3% 的情况），
431	
432	    per-test verification 的 expected advantage 为 20-42%。
433	
434	    对于 T=1 instances，per-test 与 trajectory 几乎等价（可以省略 per-test 分解以节省成本）。
435	
436	    这个 characterization 比 "per-test is always better" 的 overclaim 更有说服力。
437	
438	    '
439	- name: Block-Correlation Empirical Validation
440	  plan_id: block-corr-empirical
441	  description: 从训练好的 classification model 的 per-test 预测中测量实际 error correlation 结构。
442	  expected_results:
443	    within_instance_spearman_rho: 0.43
444	    within_instance_pearson_r: 0.41
445	    between_instance_spearman_rho: 0.028
446	    iid_model_rho: 0.0
447	    block_model_rho: 1.0
448	    n_instances_analyzed: 487
449	    avg_tests_per_instance: 4.7
450	    correlation_by_T2: 0.49
451	    correlation_by_T3: 0.44
452	    correlation_by_T4plus: 0.38
453	  result_rationale: 'Within-instance ρ=0.43 表明预测误差显著正相关：当模型对某个 (code, test_A) 判错时，
454	
455	    同一 code 的 test_B 也大概率被判错。这是因为同一 patch 的所有 test 共享相同的代码语义——
456	
457	    如果模型误解了 patch 的行为，相关的 test 都会受影响。
458	
459	    Between-instance ρ≈0.03 接近零，说明错误是 instance-specific 的（模型没有系统性偏差）。
460	
461	    ρ=0.43 处于 iid（ρ=0）和 full block（ρ=1）之间偏向 block 一侧，
462	
463	    验证了 oracle 分析中 block-correlation 假设的合理性：
464	
465	    block-corr 结果（36-45%）是上界，iid 结果（2-27%）是下界，真实值在两者之间偏上。
466	
467	    T=2 时 ρ 最高（0.49）因为只有两个 test 时共享的代码推理几乎完全相同；
468	
469	    T≥4 时 ρ 下降到 0.38 因为 test 多样性增加，部分 test 覆盖不同代码路径。
470	
471	    '
472	  tables:
473	  - name: 'Table 8: Empirical Error Correlation Structure'
474	    columns:
475	    - Scope
476	    - Spearman ρ
477	    - Interpretation
478	    rows:
479	    - - Within-instance
480	      - 0.43
481	      - Substantial positive correlation
482	    - - Between-instance
483	      - 0.028
484	      - Near-zero (instance-specific)
485	    - - i.i.d. model
486	      - 0.0
487	      - Lower bound
488	    - - Block-corr model
489	      - 1.0
490	      - Upper bound
491	  - name: Correlation by F2P Count
492	    columns:
493	    - T
494	    - ρ
495	    - N instances
496	    rows:
497	    - - T=2
498	      - 0.49
499	      - 79
500	    - - T=3
501	      - 0.44
502	      - 42
503	    - - T≥4
504	      - 0.38
505	      - 31
506	  figures_description:
507	  - 'Figure 9: ρ vs T scatter plot with 95% CI bands，叠加 iid (ρ=0) 和 block (ρ=1) reference
508	    lines'
509	  analysis: 'Block-correlation 验证连接了 oracle 模拟（Claim 3）和训练模型（Claim 1）。
510	
511	    ρ≈0.43 意味着 oracle 分析的 block 估计偏乐观但方向正确，iid 估计偏保守。
512	
513	    真实的 per-test advantage 落在两个 bound 之间，约 60% 权重偏 block。
514	
515	    这一发现独立验证了为什么 per-test 在 multi-F2P instances 上优势如此大：
516	
517	    block 错误意味着 trajectory-level 更容易「全错」或「全对」，per-test 则能部分纠正。
518	
519	    '
520	- name: SWE-bench-PerTest Dataset Construction
521	  plan_id: swebench-pertest-data
522	  description: Docker 重新执行 SWE-bench Verified patches，提取 per-test pass/fail labels。500
523	    instances × 16 candidates。
524	  expected_results:
525	    n_instances_target: 500
526	    n_instances_successful: 478
527	    n_instances_docker_fail: 22
528	    n_candidates_per_instance: 16
529	    total_test_executions: 391168
530	    avg_total_tests_per_instance: 51.2
531	    avg_f2p_tests: 3.0
532	    median_f2p_tests: 2
533	    avg_p2p_tests: 48.2
534	    docker_wall_clock_hours: 19.3
535	    n_parallel_containers: 16
536	    label_agreement_with_original_pct: 98.5
537	    flaky_test_rate_pct: 1.2
538	  result_rationale: '478/500 成功率（95.6%）与 SWE-bench Docker 基础设施的已知可靠性一致——
539	
540	    22 个失败主要来自 Python 版本不兼容（legacy repos 需要 Python 3.7/3.8）和
541	
542	    系统级依赖缺失（C extensions, CUDA）。
543	
544	    Average F2P=3.0, median=2 与 SWE-bench Verified 的已知分布一致（mean=3, P75=2, P90=3）。
545	
546	    98.5% label agreement 验证了 Docker re-evaluation 的方法论——
547	
548	    1.5% 不一致主要来自 flaky tests（1.2%）和环境敏感 assertions（0.3%）。
549	
550	    19.3h wall-clock 在 16 并行 container 下合理（每个 instance ~0.65h 包括环境搭建 + 测试执行）。
551	
552	    数据集本身是独立于论文 claims 的 resource contribution——
553	
554	    它使任何 future work on SWE-bench per-test verification 成为可能。
555	
556	    '
557	  tables:
558	  - name: 'Table 9: SWE-bench-PerTest Dataset Statistics'
559	    columns:
560	    - Statistic
561	    - Value
562	    rows:
563	    - - Instances (successful)
564	      - 478
565	    - - Candidates per instance
566	      - 16
567	    - - Total (instance, candidate, test) triples
568	      - 391,168
569	    - - Avg F2P tests per instance
570	      - 3.0
571	    - - Median F2P tests
572	      - 2
573	    - - Avg P2P tests per instance
574	      - 48.2
575	    - - Label agreement with SWE-bench
576	      - 98.5%
577	  figures_description:
578	  - 'Figure 10: F2P test count 的 histogram（T=1 到 T=15+），展示长尾分布'
579	  analysis: '数据集构建是 repo-level 实验的先决条件。F2P 分布（median=2, mean=3）
580	
581	    意味着约 31% 的 instances 有 T≥2，为 per-test advantage 提供足够的 multi-F2P 样本。
582	
583	    P2P 测试很多（avg 48.2）但由于 regression rate ~1%（已知），
584	
585	    P2P 对 per-test advantage 贡献极小，论文中应明确说明这一限制。
586	
587	    '
588	- name: Repo-Level Classification vs CWM Training
589	  plan_id: repo-level-training
590	  description: 在 SWE-bench-PerTest 上 fine-tune Qwen3-4B/8B 做 repo-level per-test classification
591	    和 CWM，评估 complexity-dependent gap。
592	  expected_results:
593	    repo_cls_4b_pass_f1: 80.8
594	    repo_cls_4b_fail_f1: 83.2
595	    repo_cls_4b_macro_f1: 82.0
596	    repo_cls_4b_accuracy: 82.3
597	    repo_cls_8b_pass_f1: 83.5
598	    repo_cls_8b_fail_f1: 85.5
599	    repo_cls_8b_macro_f1: 84.5
600	    repo_cls_8b_accuracy: 84.8
601	    repo_cwm_4b_macro_f1: 70.5
602	    repo_cwm_4b_accuracy: 71.2
603	    repo_cwm_4b_unparseable_pct: 15.2
604	    repo_cwm_4b_truncated_pct: 7.8
605	    repo_cwm_4b_unparseable_or_truncated_pct: 23.0
606	    repo_cwm_4b_string_mismatch_pct: 18.5
607	    repo_cwm_8b_macro_f1: 73.0
608	    repo_cwm_8b_unparseable_or_truncated_pct: 18.5
609	    gap_4b_pp: 11.5
610	    gap_8b_pp: 11.5
611	    func_to_repo_cls_f1_drop_pp: 5.5
612	    func_to_repo_cwm_f1_drop_pp: 17.0
613	    context_length_median_tokens: 6842
614	    context_length_p90_tokens: 14207
615	    context_truncation_rate_pct: 8.3
616	  result_rationale: "这是论文的 headline result。Classification 从函数级 87.5 下降到 repo 级 82.0（-5.5pp），\n\
617	    CWM 从 87.5 暴跌到 70.5（-17.0pp）——gap 从 0pp 扩大到 11.5pp。\nClassification 的温和下降来自三个因素：(1)\
618	    \ repo-level context 更长（median 6.8K tokens vs ~500），\nattention 稀释降低了对关键代码区域的聚焦；(2)\
619	    \ cross-file 依赖增加了推理复杂度；\n(3) 8.3% 的 cases 因 context 超长被截断。但 classification 只需输出\
620	    \ 1 token，\n这些因素只影响理解，不影响生成。\nCWM 的剧烈下降（-17pp）有明确的机械解释：\n- Token-budget exhaustion（15.2%）：repo-level\
621	    \ execution traces 动辄数百到数千 tokens，\n  4B 模型的 generation window 不够，trace 被截断导致\
622	    \ systematic false-fail。\n- String-value prediction errors（18.5%）：repo-level output\
623	    \ 包含文件路径、版本号、\n  复杂 stack traces、dict/list 格式化——这些不是语义推理而是 lexical memorization\
624	    \ 问题。\n- 两者合计影响 23% 的预测（unparseable + truncated），在 best tier 范围 [15%, 35%] 内。\n\
625	    Classification 完全绕过了这些 failure modes——它从不需要生成 execution output tokens。\n8B 模型的\
626	    \ gap 仍然 11.5pp（CWM 73.0 vs Cls 84.5），说明 scaling 缓解但不解决 CWM 的结构性缺陷。\n"
627	  tables:
628	  - name: 'Table 10: Repo-Level — Classification vs CWM (SWE-bench-PerTest)'
629	    columns:
630	    - Model
631	    - Formulation
632	    - Pass F1
633	    - Fail F1
634	    - Macro F1
635	    rows:
636	    - - Qwen3-4B
637	      - Classification
638	      - 80.8
639	      - 83.2
640	      - 82.0
641	    - - Qwen3-4B
642	      - CWM Generation
643	      - —
644	      - —
645	      - 70.5
646	    - - Δ (Cls − CWM)
647	      - —
648	      - —
649	      - —
650	      - '+11.5'
651	    - - Qwen3-8B
652	      - Classification
653	      - 83.5
654	      - 85.5
655	      - 84.5
656	    - - Qwen3-8B
657	      - CWM Generation
658	      - —
659	      - —
660	      - 73.0
661	    - - Δ (Cls − CWM)
662	      - —
663	      - —
664	      - —
665	      - '+11.5'
666	  - name: 'Table 11: Complexity-Dependent Gap — Function vs Repo Level'
667	    columns:
668	    - Level
669	    - Cls F1 (4B)
670	    - CWM F1 (4B)
671	    - Gap (pp)
672	    rows:
673	    - - Function-level
674	      - 87.5
675	      - 87.5
676	      - 0.0
677	    - - Repo-level
678	      - 82.0
679	      - 70.5
680	      - 11.5
681	    - - Drop
682	      - −5.5
683	      - −17.0
684	      - '+11.5'
685	  - name: 'Table 12: CWM Failure Mode Breakdown — Repo-Level'
686	    columns:
687	    - Failure Mode
688	    - '% of Predictions'
689	    - Explanation
690	    rows:
691	    - - Token-budget exhaustion
692	      - 15.2%
693	      - Trace exceeds generation window
694	    - - String-value mismatch
695	      - 18.5%
696	      - Correct semantics, wrong surface form
697	    - - Unparseable output
698	      - 7.8%
699	      - Cannot extract pass/fail from generation
700	    - - Clean predictions (none)
701	      - 58.5%
702	      - CWM works correctly
703	  figures_description:
704	  - 'Figure 11: Complexity-dependent gap visualization: 函数级 bar pair (gap≈0) vs repo
705	    级 bar pair (gap=11.5pp)'
706	  - 'Figure 12: CWM failure mode pie chart at repo-level，展示 41.5% 的预测受 failure modes
707	    影响'
708	  - 'Figure 13: F1 vs context length scatter/binned plot，classification 平缓下降，CWM 急剧下降'
709	  analysis: '这是论文的核心实验。Complexity-dependent gap 的 narrative 完全成立：
710	
711	    函数级 gap=0（null result），repo-level gap=11.5pp（显著差异）。
712	
713	    CWM failure mode breakdown 提供了机械解释——不只是报告数字，而是解释为什么。
714	
715	    Table 11 是论文的 headline table，应该出现在 abstract 和 introduction 中。
716	
717	    Reviewer concern "classification is trivially easier" 被函数级 null result 直接反驳：
718	
719	    如果 classification 本质上更简单，函数级也应该有 gap。gap=0 证明差异来自复杂度，不来自任务难度。
720	
721	    '
722	- name: Diagnostic Re-repair Experiment
723	  plan_id: diagnostic-rerepair
724	  description: 给 repair agent per-test failure predictions vs 无 per-test info，在 200
725	    instances 上比较 resolve rate。
726	  expected_results:
727	    n_instances: 200
728	    baseline_resolve_rate_pct: 26.5
729	    rerepair_without_diagnostics_resolve_rate_pct: 29.0
730	    rerepair_with_diagnostics_resolve_rate_pct: 34.5
731	    diagnostic_lift_pp: 5.5
732	    blind_rerepair_lift_pp: 2.5
733	    n_rerepair_triggered: 89
734	    rerepair_success_rate_with_diag_pct: 27.0
735	    rerepair_success_rate_without_diag_pct: 14.6
736	    p_value_mcnemar: 0.016
737	    multi_f2p_diagnostic_lift_pp: 10.8
738	    single_f2p_diagnostic_lift_pp: 2.3
739	  result_rationale: 'Diagnostic lift 5.5pp（在 best tier 范围 [3, 8] 内）来自 per-test predictions
740	    为 repair agent
741	
742	    提供了 actionable 的失败定位信息。当 agent 知道 "test_parse_edge_case fails but test_parse_basic
743	    passes" 时，
744	
745	    它可以将修复集中在 edge case 处理逻辑上，而不是盲目重试。
746	
747	    Blind re-repair（知道 "有 test 失败" 但不知道哪个）仍有 2.5pp 提升，因为重试本身就有价值——
748	
749	    但 diagnostic-specific lift（5.5 - 2.5 = 3.0pp 增量，或相对于 blind 的 +5.5pp）
750	
751	    证明了 per-test 信息的独特贡献。
752	
753	    优势集中在 multi-F2P instances（lift 10.8pp vs single-F2P 2.3pp），
754	
755	    与 oracle 分析的预测一致：当有多个 failing tests 时，知道哪些 fail 的信息增益最大。
756	
757	    McNemar p=0.016 在 200 样本下达到显著性，虽然样本量有限但足以支撑 proof-of-concept。
758	
759	    '
760	  tables:
761	  - name: 'Table 13: Diagnostic Re-repair Results'
762	    columns:
763	    - Condition
764	    - Resolve Rate
765	    - Δ vs Baseline
766	    rows:
767	    - - No re-repair (baseline)
768	      - 26.5%
769	      - —
770	    - - Re-repair without diagnostics
771	      - 29.0%
772	      - +2.5 pp
773	    - - Re-repair with per-test diagnostics
774	      - 34.5%
775	      - +8.0 pp
776	    - - Diagnostic-specific lift
777	      - —
778	      - +5.5 pp (p=0.016)
779	  - name: 'Table 14: Diagnostic Lift by F2P Count'
780	    columns:
781	    - F2P Count
782	    - '% Instances'
783	    - Diag Lift
784	    - Blind Lift
785	    rows:
786	    - - T=1
787	      - 69%
788	      - +2.3 pp
789	      - +1.8 pp
790	    - - T=2
791	      - 16%
792	      - +8.2 pp
793	      - +2.5 pp
794	    - - T≥3
795	      - 15%
796	      - +10.8 pp
797	      - +3.6 pp
798	  figures_description:
799	  - 'Figure 14: Grouped bar chart — three conditions (baseline / blind / diagnostic)
800	    × stratified by T'
801	  analysis: 'Re-repair 实验是 Claim 2 的锚点。5.5pp lift 在统计上显著且实际有意义。
802	
803	    Stratification 连接了 Claim 2 和 Claim 3：diagnostic 优势集中在 multi-F2P instances，
804	
805	    正是 oracle 分析预测的 "sweet spot"。
806	
807	    论文应定位为 proof-of-concept（不是 SOTA repair），目标是展示机制而非最优数字。
808	
809	    '
810	- name: LLM-as-Judge Baselines
811	  plan_id: llm-judge-baseline
812	  description: Qwen3-8B/32B zero-shot LLM-as-judge，trajectory 和 per-test 两种模式。作为 Pareto
813	    frontier 参考点。
814	  expected_results:
815	    qwen_8b_zs_traj_f1: 67.5
816	    qwen_8b_zs_traj_accuracy: 68.3
817	    qwen_8b_zs_pertest_macro_f1: 63.8
818	    qwen_32b_zs_traj_f1: 73.2
819	    qwen_32b_zs_traj_accuracy: 74.1
820	    qwen_32b_zs_pertest_macro_f1: 70.5
821	    finetuned_4b_cls_macro_f1: 87.5
822	    finetuned_4b_cost_per_instance: 0.001
823	    qwen_8b_cost_per_instance: 0.003
824	    qwen_32b_cost_per_instance: 0.012
825	  result_rationale: 'Zero-shot LLM judges 大幅低于 fine-tuned classifiers，原因：
826	
827	    (1) Execution simulation 在 pretraining 数据中代表性不足——模型能推理代码语义
828	
829	    但没有学过系统性地预测 pass/fail outcomes；
830	
831	    (2) Zero-shot 缺乏 calibration——模型倾向于过度自信或过度保守，没有训练信号来校准阈值；
832	
833	    (3) Per-test zero-shot 更差（63.8% vs 67.5% trajectory）因为需要逐个 test 推理，
834	
835	    而没有训练数据教模型如何处理单个 test 的判断。
836	
837	    Qwen3-8B zero-shot（67.5%）甚至低于 4B fine-tuned CWM（87.5%），
838	
839	    说明 fine-tuning 在此任务上比 8× 参数量更有价值。
840	
841	    Qwen3-32B zero-shot（73.2%）仍然远低于 4B fine-tuned classification（87.5%），
842	
843	    说明即使 32B 规模的 zero-shot prompting 也无法替代 task-specific fine-tuning。
844	
845	    这占据 Pareto frontier 的低效区域：高成本（$0.012）低 accuracy。
846	
847	    '
848	  tables:
849	  - name: 'Table 15: Pareto Frontier — Accuracy vs Cost'
850	    columns:
851	    - Method
852	    - Params
853	    - Fine-tuned
854	    - Macro F1
855	    - Cost/Instance
856	    rows:
857	    - - LLM-Judge ZS
858	      - 8B
859	      - 'No'
860	      - 67.5%
861	      - $0.003
862	    - - LLM-Judge ZS
863	      - 32B
864	      - 'No'
865	      - 73.2%
866	      - $0.012
867	    - - CWM Gen (func)
868	      - 4B
869	      - 'Yes'
870	      - 87.5%
871	      - $0.002
872	    - - Cls (func)
873	      - 4B
874	      - 'Yes'
875	      - 87.5%
876	      - $0.001
877	    - - Cls (func)
878	      - 8B
879	      - 'Yes'
880	      - 90.1%
881	      - $0.002
882	    - - Cls (repo)
883	      - 4B
884	      - 'Yes'
885	      - 82.0%
886	      - $0.001
887	  figures_description:
888	  - 'Figure 15: Pareto frontier scatter plot (F1 vs cost-per-instance)，fine-tuned
889	    classification 占据 optimal 角'
890	  analysis: 'LLM-judge baselines 回应两个 reviewer concern：
891	
892	    (1) "Why not just prompt a large model?" — 因为 32B zero-shot 仍比 4B fine-tuned 差
893	    14pp。
894	
895	    (2) "Is fine-tuning necessary?" — 是的，task-specific training signal 在结构化预测任务上不可替代。
896	
897	    Pareto frontier figure 是论文中最直观的可视化之一。
898	
899	    '
900	- name: Per-test Majority Voting (K=3)
901	  plan_id: per-test-majority-voting
902	  description: Classification model 温度采样 K=3 次取多数票，测试 self-consistency 是否提升 per-test
903	    accuracy。
904	  expected_results:
905	    k3_pass_f1: 88.5
906	    k3_fail_f1: 89.2
907	    k3_macro_f1: 88.9
908	    k3_accuracy: 89.0
909	    single_pass_macro_f1: 87.5
910	    improvement_from_voting_pp: 1.4
911	    cost_multiplier: 3.0
912	    disagreement_rate_pct: 13.5
913	    disagreement_accuracy: 62.3
914	  result_rationale: 'Majority voting 提供 1.4pp 边际改善（87.5→88.9），但代价是 3× 推理成本。
915	
916	    改善小的原因：base classifier 在 87.5% 已经是 well-calibrated 的——
917	
918	    大多数预测高置信度（86.5% 的 cases 三次投票一致），self-consistency 只在 13.5% 的
919	
920	    边界 cases 上有机会纠正错误，且其中也只有 62.3% 被正确纠正。
921	
922	    对比：直接用 8B 模型（+2.6pp, ~2× cost）比 4B majority voting（+1.4pp, 3× cost）更高效。
923	
924	    结论：majority voting 是 diminishing returns，model scaling 是更好的 accuracy 提升路径。
925	
926	    这是 appendix 级别的 P2 结果。
927	
928	    '
929	  tables:
930	  - name: 'Table S1 (Appendix): Majority Voting Results'
931	    columns:
932	    - Method
933	    - Macro F1
934	    - Relative Cost
935	    rows:
936	    - - Single-pass (4B)
937	      - 87.5%
938	      - 1×
939	    - - Majority K=3 (4B)
940	      - 88.9%
941	      - 3×
942	    - - Single-pass (8B)
943	      - 90.1%
944	      - ~2×
945	  figures_description: []
946	  analysis: 'Appendix 级结果。主要贡献是确认 self-consistency 在此任务上 ROI 低，
947	
948	    应优先考虑 model scaling。Disagreement rate 可以作为 confidence proxy 用于 selective abstention。'
949	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ffaea46-f380-4a15-a760-e072a4493b13",
  "isSidechain": false,
  "promptId": "a7f03308-ef13-4d36-8d05-7c5b8556cf68",
  "type": "user",
  "uuid": "988e3c11-211c-47c1-ad77-6878d937bbf3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/dream_reports/dream_20260511T231719/best/imagined_experiments.yaml",
      "content": "tier: best\nnarrative_guidance: 'Full 3-claim story holds. Function-level CLS ≈ CWM null result\n  is the setup（classification 不是 trivially easier）;\n\n  repo-level gap ~12pp 是 punchline（CWM failure modes 仅在复杂 trace 下显现）。\n\n  Diagnostic re-repair 以 5.5pp resolve rate gain 验证 Claim 2 的实用价值。\n\n  Oracle frontier 提供部署决策框架：per-test 优势集中在 multi-F2P 实例（T≥2 = 31.3%）。\n\n  Block-correlated errors（ρ≈0.43）放大 per-test 优势，验证 oracle 模拟假设。\n\n  Title: Complexity-Dependent Reformulation Advantage. Target: EMNLP Main, 三个 claim\n  完整成立。\n\n  '\nimagined_experiments:\n- name: Multi-Seed Core Validation\n  plan_id: multi-seed-core\n  description: Classification 和 CWM 各跑 seeds {0,1,42}，报告 mean±std F1，paired bootstrap\n    CI 检验差异是否显著。\n  expected_results:\n    cls_seed0_macro_f1: 87.2\n    cls_seed1_macro_f1: 87.7\n    cls_seed42_macro_f1: 87.5\n    cls_mean_macro_f1: 87.47\n    cls_std_macro_f1: 0.25\n    cwm_seed0_macro_f1: 87.0\n    cwm_seed1_macro_f1: 87.9\n    cwm_seed42_macro_f1: 87.5\n    cwm_mean_macro_f1: 87.47\n    cwm_std_macro_f1: 0.45\n    paired_diff_mean_pp: 0.0\n    paired_diff_95ci_lower: -0.85\n    paired_diff_95ci_upper: 0.85\n    paired_ttest_pvalue: 0.98\n    null_result_confirmed: true\n  result_rationale: '函数级代码（HumanEval/MBPP）execution output 短（通常 <50 tokens），错误类型可预测（AssertionError\n    占主导），\n\n    CWM 的两大 failure modes（token-budget exhaustion 和 string-value prediction errors）在此复杂度下不触发。\n\n    三个 seed 的 std 在 0.2-0.5 范围内，反映 LoRA 初始化和 data shuffling 的正常随机性。\n\n    CWM std 略高于 classification（0.45 vs 0.25）因为 generation 目标更高维，对初始化更敏感，\n\n    但差异不改变结论。95% CI [-0.85, 0.85] 包含 0，p=0.98 远超 0.05 阈值，\n\n    cleanly 确认 function-level null result。这为 Claim 1 \"complexity-dependent\" 叙事提供干净的\n    baseline：\n\n    两种 formulation 在简单代码上无差异，差异仅在复杂度升高时出现。\n\n    '\n  tables:\n  - name: 'Table 2: Multi-Seed Function-Level Comparison (Macro F1)'\n    columns:\n    - Model\n    - Seed 0\n    - Seed 1\n    - Seed 42\n    - Mean\n    - Std\n    rows:\n    - - Qwen3-4B-Cls\n      - 87.2\n      - 87.7\n      - 87.5\n      - 87.47\n      - 0.25\n    - - Qwen3-4B-CWM\n      - 87.0\n      - 87.9\n      - 87.5\n      - 87.47\n      - 0.45\n    - - Δ (Cls − CWM)\n      - '+0.2'\n      - −0.2\n      - '0.0'\n      - '0.00'\n      - —\n  figures_description:\n  - 'Figure 2: 三 seed 的 per-class F1 box plot（classification vs CWM），CI 完全重叠，视觉化 null\n    result'\n  analysis: \"Multi-seed 验证是 Claim 1 的统计基础。CI 完全包含 0 证明函数级等价不是单次实验的偶然。\\n论文中应强调：classification\\\n    \\ 在函数级「不比 generation 更容易」——这反驳 reviewer \\n\\\"classification is trivially easier\\\"\\\n    \\ 的质疑。真正的优势是 complexity-dependent 的。\\n\"\n- name: Trace-then-Judge Ablation\n  plan_id: trace-then-judge\n  description: 单模型 chain-of-thought：先生成 ~50 token 执行推理 trace，再输出 pass/fail。检验显式推理在函数级是否有帮助。\n  expected_results:\n    ttj_pass_f1: 86.5\n    ttj_fail_f1: 87.1\n    ttj_macro_f1: 86.8\n    ttj_accuracy: 86.9\n    direct_cls_macro_f1: 87.5\n    diff_from_direct_cls_pp: -0.7\n    train_loss: 0.283\n    eval_loss: 0.071\n    avg_trace_length_tokens: 38.2\n    trace_quality_exact_match: 82.5\n  result_rationale: '在函数级代码上，trace-then-judge 与 direct classification 差异仅 -0.7pp（在\n    best tier 范围 [-1.5, 1.5] 内）。\n\n    原因：函数级 execution 语义简单，模型无需显式推理就能直接判断 pass/fail——\n\n    trace 是冗余的中间步骤，略微分散了模型容量（4B 参数需同时学 trace generation + classification），\n\n    但因为 trace 很短（平均 38 tokens），overhead 很小。Trace exact match 82.5%（高于 CWM 的 84%\n\n    是因为 trace 只需覆盖关键推理步骤，不需精确复现完整 output）。\n\n    关键结论：在函数级，显式推理既不帮助也不伤害。这支持 \"formulation advantage is about\n\n    skipping the generation bottleneck, not about reasoning quality\" 的论点。\n\n    在 repo-level（未测），trace-then-judge 预期会因 trace 质量下降而退化。\n\n    '\n  tables:\n  - name: 'Table 3: Formulation Ablation — Function-Level'\n    columns:\n    - Method\n    - Pass F1\n    - Fail F1\n    - Macro F1\n    - Δ vs Direct Cls\n    rows:\n    - - Direct Classification\n      - 87.1\n      - 87.9\n      - 87.5\n      - —\n    - - Trace-then-Judge (CoT)\n      - 86.5\n      - 87.1\n      - 86.8\n      - −0.7\n    - - CWM Generation\n      - 87.3\n      - 87.7\n      - 87.5\n      - '0.0'\n  figures_description:\n  - 'Figure 3: 三种 formulation 的 per-class F1 bar chart，error bars 来自 bootstrap，三者\n    CI 重叠'\n  analysis: 'Trace-then-judge 接近 direct classification 证明函数级上显式执行推理是中性的。\n\n    三种方法（direct cls, TtJ, CWM）在函数级都 ~87%，共同构成 null result。\n\n    这为 repo-level 实验设置了对比：如果 repo-level TtJ 显著低于 direct cls，\n\n    则证明 trace generation 在高复杂度下成为瓶颈——而 classification 通过跳过 trace 避开了这个瓶颈。\n\n    '\n- name: Trajectory-Level Finetuned Baseline\n  plan_id: traj-level-finetuned\n  description: Qwen3-4B LoRA 训练预测 resolved/unresolved（聚合所有 test）。隔离 granularity 效应。\n  expected_results:\n    traj_accuracy: 83.2\n    traj_resolved_f1: 80.5\n    traj_unresolved_f1: 84.8\n    traj_macro_f1: 82.7\n    traj_auc_roc: 0.882\n    per_test_cls_derived_traj_acc: 85.3\n    granularity_effect_pp: 2.1\n    formulation_effect_pp: 0.0\n    combined_effect_pp: 2.1\n    class_balance_resolved_pct: 38.5\n    class_balance_unresolved_pct: 61.5\n  result_rationale: 'Trajectory-level 在函数级仍表现合理（83.2% acc）因为 test suites 小（通常 3-8\n    test cases per problem）。\n\n    但比 per-test classification 的 derived trajectory accuracy（85.3%）低 2.1pp——\n\n    这是 granularity 效应：trajectory model 必须一次性从所有 test 的 concatenation 做出判断，\n\n    而 per-test model 逐个 test 判断后 AND 聚合，降低了每次推理的认知负担。\n\n    关键发现：formulation effect = 0pp（因为函数级 CLS ≈ CWM），granularity effect = 2.1pp。\n\n    这完成了 2×2 因子分析（formulation × granularity），显示在函数级只有 granularity 轴有微弱效应。\n\n    类别不平衡（61.5% unresolved）出现是因为多数 mutation 至少破坏一个 test，\n\n    导致 unresolved 成为多数类，unresolved_f1 高于 resolved_f1。\n\n    '\n  tables:\n  - name: 'Table 4: 2×2 Factorial Decomposition — Function-Level'\n    columns:\n    - Formulation\n    - Granularity\n    - Traj Acc\n    - Macro F1\n    rows:\n    - - Generation (CWM)\n      - Per-test\n      - 85.0%*\n      - 87.5\n    - - Classification\n      - Per-test\n      - 85.3%*\n      - 87.5\n    - - Classification\n      - Trajectory\n      - 83.2%\n      - 82.7\n    footnotes:\n    - '*Trajectory accuracy derived from per-test predictions via AND-aggregation'\n  - name: Effect Decomposition\n    columns:\n    - Effect\n    - Δ Traj Accuracy (pp)\n    rows:\n    - - Formulation (Gen→Cls)\n      - 0.0 — null at function-level\n    - - Granularity (Traj→Per-test)\n      - '+2.1'\n    - - Combined\n      - '+2.1'\n  figures_description:\n  - 'Figure 4: 2×2 factorial heatmap，formulation axis 无差异，granularity axis 有 ~2pp\n    效应'\n  analysis: '在函数级，formulation 效应为零（CLS ≈ CWM），只有 granularity 贡献 2.1pp。\n\n    这是 best tier 叙事的关键一环：函数级的 2×2 分析为 repo-level 实验提供了 baseline。\n\n    如果 repo-level 实验显示 formulation 效应从 0 跳到 12+pp，则证明优势是 complexity-dependent 的。\n\n    '\n- name: Model Size Scaling (4B → 8B)\n  plan_id: model-size-scaling\n  description: Classification 和 CWM 各扩展到 8B，验证函数级等价性是否随模型规模保持。\n  expected_results:\n    cls_8b_pass_f1: 89.8\n    cls_8b_fail_f1: 90.4\n    cls_8b_macro_f1: 90.1\n    cls_8b_accuracy: 90.2\n    cwm_8b_pass_f1: 89.5\n    cwm_8b_fail_f1: 90.1\n    cwm_8b_macro_f1: 89.8\n    cwm_8b_accuracy: 89.9\n    gap_8b_macro_f1_pp: 0.3\n    gap_4b_macro_f1_pp: 0.0\n    cls_scaling_gain_pp: 2.6\n    cwm_scaling_gain_pp: 2.3\n    cwm_8b_exact_match: 87.5\n    cwm_8b_unparseable: 0\n  result_rationale: '函数级 CWM 在 4B 已经不触发 failure modes（unparseable=0, exact_match=84%），\n\n    8B 进一步改善 exact match 到 87.5% 但 pass/fail 准确率提升与 classification 相当。\n\n    两者在 8B 仍然等价（gap 0.3pp，统计噪声范围内），因为函数级 execution output 短到\n\n    即使 4B 也能完整生成——增加参数只改善边际 case 的处理。\n\n    Scaling gain 略有差异（Cls +2.6 vs CWM +2.3）但不显著。\n\n    这强化了 complexity-dependent 叙事：不是模型太小导致 CWM 差，\n\n    而是函数级复杂度太低让 CWM 也能 work。gap 只在 repo-level 复杂度下出现。\n\n    '\n  tables:\n  - name: 'Table 5: Scaling Behavior — Function-Level'\n    columns:\n    - Scale\n    - Cls Macro F1\n    - CWM Macro F1\n    - Gap (pp)\n    rows:\n    - - 4B\n      - 87.5\n      - 87.5\n      - 0.0\n    - - 8B\n      - 90.1\n      - 89.8\n      - 0.3\n    - - Scaling gain\n      - '+2.6'\n      - '+2.3'\n      - '+0.3'\n  figures_description:\n  - 'Figure 5: 4B vs 8B scaling curve，两条线几乎平行，gap 保持在噪声水平'\n  analysis: '函数级 scaling 实验排除了 \"CWM 在更大模型上会超越 classification\" 的 reviewer 质疑（至少在函数级）。\n\n    两种 formulation 的 scaling rate 相似，说明在此复杂度下两者的 learning dynamics 等价。\n\n    论文应指出：真正的 scaling 差异预期出现在 repo-level——CWM 需要更多参数来处理长 trace，\n\n    而 classification 因 1-token output 效率更高。\n\n    '\n- name: Per-test Precision/Recall Analysis\n  plan_id: per-test-precision-recall\n  description: 在完整测试集上测量 per-test failure prediction 的 precision/recall，评估诊断信号质量。\n  expected_results:\n    fail_precision: 87.6\n    fail_recall: 88.2\n    fail_f1: 87.9\n    pass_precision: 87.4\n    pass_recall: 86.8\n    pass_f1: 87.1\n    false_positive_rate_pct: 8.3\n    false_negative_rate_pct: 11.8\n    failure_localization_exact_match_pct: 78.2\n    precision_at_k1: 89.3\n    precision_at_k3: 85.1\n  result_rationale: \"Fail precision 87.6% 和 recall 88.2% 直接来源于 mvp-b-train 的已有指标。\\n\\\n    新增指标 failure_localization_exact_match（78.2%）衡量每个 problem 是否完整识别了所有 failing tests——\\n\\\n    低于 per-test F1（87.9%）因为需要所有 test 都判对。但 78% 意味着约 4/5 的 problem \\n能获得完全正确的 diagnostic\\\n    \\ 信息。FPR 8.3% 足够低（12 次预测 fail 中约 1 次是误报），\\n对 downstream re-repair agent 来说是可接受的误报率。\\n\\\n    Precision@1（89.3%）表明 top-ranked failing test 几乎总是真实的失败——\\n这对 repair agent 的 \\\"\\\n    先修最可能的 failure\\\" 策略非常有价值。\\n\"\n  tables:\n  - name: 'Table 6: Diagnostic Signal Quality — Function-Level'\n    columns:\n    - Metric\n    - Fail Class\n    - Pass Class\n    - Macro\n    rows:\n    - - Precision\n      - 87.6%\n      - 87.4%\n      - 87.5%\n    - - Recall\n      - 88.2%\n      - 86.8%\n      - 87.5%\n    - - F1\n      - 87.9%\n      - 87.1%\n      - 87.5%\n  - name: Failure Localization\n    columns:\n    - Metric\n    - Value\n    rows:\n    - - Exact match (all tests correct)\n      - 78.2%\n    - - Precision@1\n      - 89.3%\n    - - False positive rate\n      - 8.3%\n  figures_description:\n  - 'Figure 6: Precision-Recall curve for fail class，AUC 标注，与 random baseline 对比'\n  analysis: 'Per-test prediction 质量支撑 Claim 2：diagnostic signal 足够准确以产生实际价值。\n\n    78% exact match 意味着大多数情况下 repair agent 获得完全正确的 failing test list。\n\n    即使不完全正确，部分 diagnostic 信息仍优于无信息（re-repair 实验将验证这一点）。\n\n    '\n- name: Oracle F2P-Stratified Analysis\n  plan_id: oracle-f2p-stratified\n  description: 按 F2P test count (T=1, T=2, T≥3) 分层 oracle 分析，展示 per-test advantage\n    集中在 multi-test 实例。\n  expected_results:\n    T1_pct_instances: 68.7\n    T1_iid_adv_70_85_pct: 2.0\n    T1_block_adv_70_85_pct: 10.9\n    T2_pct_instances: 16.2\n    T2_iid_adv_70_85_pct: 17.5\n    T2_block_adv_70_85_pct: 38.0\n    T3plus_pct_instances: 15.1\n    T3plus_iid_adv_70_85_pct: 26.5\n    T3plus_block_adv_70_85_pct: 45.2\n    weighted_iid_adv_pct: 7.6\n    weighted_block_adv_pct: 19.5\n  result_rationale: 'T=1 时 per-test 和 trajectory 对 F2P 部分数学上等价（只有一个 failing test，\n\n    per-test 预测和 trajectory 预测携带相同信息）——advantage 仅来自 tie-breaking（iid 2%）\n\n    或 block correlation 效应（10.9%）。\n\n    T=2 时 advantage 跳升至 17.5%/38.0%：per-test 能区分 \"fails test A only\" vs \"fails both\n    A and B\"，\n\n    而 trajectory 将两者都折叠为 \"unresolved\"。这种信息增益在 candidate ranking 中产生显著差异。\n\n    T≥3 时 advantage 最大（26.5%/45.2%）因为 failure pattern 的组合空间增长，\n\n    per-test 捕获的信息量远超 trajectory-level。\n\n    Block-correlated advantage 始终显著高于 iid（~2-3×）因为 block 错误结构\n\n    减少了有效自由度，放大了 per-test 的信息优势。\n\n    Population-weighted advantage（7.6% iid / 19.5% block）因 T=1 占 68.7% 而被稀释——\n\n    这是诚实的报告，但也说明：如果 deployment 能 filter 出 multi-F2P instances，\n\n    per-test 的 ROI 大幅提升。\n\n    '\n  tables:\n  - name: 'Table 7: Per-test Advantage Stratified by F2P Count (Oracle, acc ∈ [70%,\n      85%])'\n    columns:\n    - F2P Count (T)\n    - '% Instances'\n    - Adv (i.i.d.)\n    - Adv (Block-corr)\n    rows:\n    - - T=1\n      - 68.7%\n      - 2.0%\n      - 10.9%\n    - - T=2\n      - 16.2%\n      - 17.5%\n      - 38.0%\n    - - T≥3\n      - 15.1%\n      - 26.5%\n      - 45.2%\n    - - Weighted\n      - 100%\n      - 7.6%\n      - 19.5%\n  figures_description:\n  - 'Figure 7: Stacked bar chart 按 T 分层的 per-test advantage，iid vs block 双柱对比'\n  - 'Figure 8: Advantage vs T 的 scatter plot with fitted curve，展示 advantage 随 T 单调递增'\n  analysis: '分层分析是 Claim 3 的核心结果。它提供了实用决策框架：\n\n    当 instance 预期有 T≥2 个 failing tests（SWE-bench 中 31.3% 的情况），\n\n    per-test verification 的 expected advantage 为 20-42%。\n\n    对于 T=1 instances，per-test 与 trajectory 几乎等价（可以省略 per-test 分解以节省成本）。\n\n    这个 characterization 比 \"per-test is always better\" 的 overclaim 更有说服力。\n\n    '\n- name: Block-Correlation Empirical Validation\n  plan_id: block-corr-empirical\n  description: 从训练好的 classification model 的 per-test 预测中测量实际 error correlation 结构。\n  expected_results:\n    within_instance_spearman_rho: 0.43\n    within_instance_pearson_r: 0.41\n    between_instance_spearman_rho: 0.028\n    iid_model_rho: 0.0\n    block_model_rho: 1.0\n    n_instances_analyzed: 487\n    avg_tests_per_instance: 4.7\n    correlation_by_T2: 0.49\n    correlation_by_T3: 0.44\n    correlation_by_T4plus: 0.38\n  result_rationale: 'Within-instance ρ=0.43 表明预测误差显著正相关：当模型对某个 (code, test_A) 判错时，\n\n    同一 code 的 test_B 也大概率被判错。这是因为同一 patch 的所有 test 共享相同的代码语义——\n\n    如果模型误解了 patch 的行为，相关的 test 都会受影响。\n\n    Between-instance ρ≈0.03 接近零，说明错误是 instance-specific 的（模型没有系统性偏差）。\n\n    ρ=0.43 处于 iid（ρ=0）和 full block（ρ=1）之间偏向 block 一侧，\n\n    验证了 oracle 分析中 block-correlation 假设的合理性：\n\n    block-corr 结果（36-45%）是上界，iid 结果（2-27%）是下界，真实值在两者之间偏上。\n\n    T=2 时 ρ 最高（0.49）因为只有两个 test 时共享的代码推理几乎完全相同；\n\n    T≥4 时 ρ 下降到 0.38 因为 test 多样性增加，部分 test 覆盖不同代码路径。\n\n    '\n  tables:\n  - name: 'Table 8: Empirical Error Correlation Structure'\n    columns:\n    - Scope\n    - Spearman ρ\n    - Interpretation\n    rows:\n    - - Within-instance\n      - 0.43\n      - Substantial positive correlation\n    - - Between-instance\n      - 0.028\n      - Near-zero (instance-specific)\n    - - i.i.d. model\n      - 0.0\n      - Lower bound\n    - - Block-corr model\n      - 1.0\n      - Upper bound\n  - name: Correlation by F2P Count\n    columns:\n    - T\n    - ρ\n    - N instances\n    rows:\n    - - T=2\n      - 0.49\n      - 79\n    - - T=3\n      - 0.44\n      - 42\n    - - T≥4\n      - 0.38\n      - 31\n  figures_description:\n  - 'Figure 9: ρ vs T scatter plot with 95% CI bands，叠加 iid (ρ=0) 和 block (ρ=1) reference\n    lines'\n  analysis: 'Block-correlation 验证连接了 oracle 模拟（Claim 3）和训练模型（Claim 1）。\n\n    ρ≈0.43 意味着 oracle 分析的 block 估计偏乐观但方向正确，iid 估计偏保守。\n\n    真实的 per-test advantage 落在两个 bound 之间，约 60% 权重偏 block。\n\n    这一发现独立验证了为什么 per-test 在 multi-F2P instances 上优势如此大：\n\n    block 错误意味着 trajectory-level 更容易「全错」或「全对」，per-test 则能部分纠正。\n\n    '\n- name: SWE-bench-PerTest Dataset Construction\n  plan_id: swebench-pertest-data\n  description: Docker 重新执行 SWE-bench Verified patches，提取 per-test pass/fail labels。500\n    instances × 16 candidates。\n  expected_results:\n    n_instances_target: 500\n    n_instances_successful: 478\n    n_instances_docker_fail: 22\n    n_candidates_per_instance: 16\n    total_test_executions: 391168\n    avg_total_tests_per_instance: 51.2\n    avg_f2p_tests: 3.0\n    median_f2p_tests: 2\n    avg_p2p_tests: 48.2\n    docker_wall_clock_hours: 19.3\n    n_parallel_containers: 16\n    label_agreement_with_original_pct: 98.5\n    flaky_test_rate_pct: 1.2\n  result_rationale: '478/500 成功率（95.6%）与 SWE-bench Docker 基础设施的已知可靠性一致——\n\n    22 个失败主要来自 Python 版本不兼容（legacy repos 需要 Python 3.7/3.8）和\n\n    系统级依赖缺失（C extensions, CUDA）。\n\n    Average F2P=3.0, median=2 与 SWE-bench Verified 的已知分布一致（mean=3, P75=2, P90=3）。\n\n    98.5% label agreement 验证了 Docker re-evaluation 的方法论——\n\n    1.5% 不一致主要来自 flaky tests（1.2%）和环境敏感 assertions（0.3%）。\n\n    19.3h wall-clock 在 16 并行 container 下合理（每个 instance ~0.65h 包括环境搭建 + 测试执行）。\n\n    数据集本身是独立于论文 claims 的 resource contribution——\n\n    它使任何 future work on SWE-bench per-test verification 成为可能。\n\n    '\n  tables:\n  - name: 'Table 9: SWE-bench-PerTest Dataset Statistics'\n    columns:\n    - Statistic\n    - Value\n    rows:\n    - - Instances (successful)\n      - 478\n    - - Candidates per instance\n      - 16\n    - - Total (instance, candidate, test) triples\n      - 391,168\n    - - Avg F2P tests per instance\n      - 3.0\n    - - Median F2P tests\n      - 2\n    - - Avg P2P tests per instance\n      - 48.2\n    - - Label agreement with SWE-bench\n      - 98.5%\n  figures_description:\n  - 'Figure 10: F2P test count 的 histogram（T=1 到 T=15+），展示长尾分布'\n  analysis: '数据集构建是 repo-level 实验的先决条件。F2P 分布（median=2, mean=3）\n\n    意味着约 31% 的 instances 有 T≥2，为 per-test advantage 提供足够的 multi-F2P 样本。\n\n    P2P 测试很多（avg 48.2）但由于 regression rate ~1%（已知），\n\n    P2P 对 per-test advantage 贡献极小，论文中应明确说明这一限制。\n\n    '\n- name: Repo-Level Classification vs CWM Training\n  plan_id: repo-level-training\n  description: 在 SWE-bench-PerTest 上 fine-tune Qwen3-4B/8B 做 repo-level per-test classification\n    和 CWM，评估 complexity-dependent gap。\n  expected_results:\n    repo_cls_4b_pass_f1: 80.8\n    repo_cls_4b_fail_f1: 83.2\n    repo_cls_4b_macro_f1: 82.0\n    repo_cls_4b_accuracy: 82.3\n    repo_cls_8b_pass_f1: 83.5\n    repo_cls_8b_fail_f1: 85.5\n    repo_cls_8b_macro_f1: 84.5\n    repo_cls_8b_accuracy: 84.8\n    repo_cwm_4b_macro_f1: 70.5\n    repo_cwm_4b_accuracy: 71.2\n    repo_cwm_4b_unparseable_pct: 15.2\n    repo_cwm_4b_truncated_pct: 7.8\n    repo_cwm_4b_unparseable_or_truncated_pct: 23.0\n    repo_cwm_4b_string_mismatch_pct: 18.5\n    repo_cwm_8b_macro_f1: 73.0\n    repo_cwm_8b_unparseable_or_truncated_pct: 18.5\n    gap_4b_pp: 11.5\n    gap_8b_pp: 11.5\n    func_to_repo_cls_f1_drop_pp: 5.5\n    func_to_repo_cwm_f1_drop_pp: 17.0\n    context_length_median_tokens: 6842\n    context_length_p90_tokens: 14207\n    context_truncation_rate_pct: 8.3\n  result_rationale: \"这是论文的 headline result。Classification 从函数级 87.5 下降到 repo 级 82.0（-5.5pp），\\n\\\n    CWM 从 87.5 暴跌到 70.5（-17.0pp）——gap 从 0pp 扩大到 11.5pp。\\nClassification 的温和下降来自三个因素：(1)\\\n    \\ repo-level context 更长（median 6.8K tokens vs ~500），\\nattention 稀释降低了对关键代码区域的聚焦；(2)\\\n    \\ cross-file 依赖增加了推理复杂度；\\n(3) 8.3% 的 cases 因 context 超长被截断。但 classification 只需输出\\\n    \\ 1 token，\\n这些因素只影响理解，不影响生成。\\nCWM 的剧烈下降（-17pp）有明确的机械解释：\\n- Token-budget exhaustion（15.2%）：repo-level\\\n    \\ execution traces 动辄数百到数千 tokens，\\n  4B 模型的 generation window 不够，trace 被截断导致\\\n    \\ systematic false-fail。\\n- String-value prediction errors（18.5%）：repo-level output\\\n    \\ 包含文件路径、版本号、\\n  复杂 stack traces、dict/list 格式化——这些不是语义推理而是 lexical memorization\\\n    \\ 问题。\\n- 两者合计影响 23% 的预测（unparseable + truncated），在 best tier 范围 [15%, 35%] 内。\\n\\\n    Classification 完全绕过了这些 failure modes——它从不需要生成 execution output tokens。\\n8B 模型的\\\n    \\ gap 仍然 11.5pp（CWM 73.0 vs Cls 84.5），说明 scaling 缓解但不解决 CWM 的结构性缺陷。\\n\"\n  tables:\n  - name: 'Table 10: Repo-Level — Classification vs CWM (SWE-bench-PerTest)'\n    columns:\n    - Model\n    - Formulation\n    - Pass F1\n    - Fail F1\n    - Macro F1\n    rows:\n    - - Qwen3-4B\n      - Classification\n      - 80.8\n      - 83.2\n      - 82.0\n    - - Qwen3-4B\n      - CWM Generation\n      - —\n      - —\n      - 70.5\n    - - Δ (Cls − CWM)\n      - —\n      - —\n      - —\n      - '+11.5'\n    - - Qwen3-8B\n      - Classification\n      - 83.5\n      - 85.5\n      - 84.5\n    - - Qwen3-8B\n      - CWM Generation\n      - —\n      - —\n      - 73.0\n    - - Δ (Cls − CWM)\n      - —\n      - —\n      - —\n      - '+11.5'\n  - name: 'Table 11: Complexity-Dependent Gap — Function vs Repo Level'\n    columns:\n    - Level\n    - Cls F1 (4B)\n    - CWM F1 (4B)\n    - Gap (pp)\n    rows:\n    - - Function-level\n      - 87.5\n      - 87.5\n      - 0.0\n    - - Repo-level\n      - 82.0\n      - 70.5\n      - 11.5\n    - - Drop\n      - −5.5\n      - −17.0\n      - '+11.5'\n  - name: 'Table 12: CWM Failure Mode Breakdown — Repo-Level'\n    columns:\n    - Failure Mode\n    - '% of Predictions'\n    - Explanation\n    rows:\n    - - Token-budget exhaustion\n      - 15.2%\n      - Trace exceeds generation window\n    - - String-value mismatch\n      - 18.5%\n      - Correct semantics, wrong surface form\n    - - Unparseable output\n      - 7.8%\n      - Cannot extract pass/fail from generation\n    - - Clean predictions (none)\n      - 58.5%\n      - CWM works correctly\n  figures_description:\n  - 'Figure 11: Complexity-dependent gap visualization: 函数级 bar pair (gap≈0) vs repo\n    级 bar pair (gap=11.5pp)'\n  - 'Figure 12: CWM failure mode pie chart at repo-level，展示 41.5% 的预测受 failure modes\n    影响'\n  - 'Figure 13: F1 vs context length scatter/binned plot，classification 平缓下降，CWM 急剧下降'\n  analysis: '这是论文的核心实验。Complexity-dependent gap 的 narrative 完全成立：\n\n    函数级 gap=0（null result），repo-level gap=11.5pp（显著差异）。\n\n    CWM failure mode breakdown 提供了机械解释——不只是报告数字，而是解释为什么。\n\n    Table 11 是论文的 headline table，应该出现在 abstract 和 introduction 中。\n\n    Reviewer concern \"classification is trivially easier\" 被函数级 null result 直接反驳：\n\n    如果 classification 本质上更简单，函数级也应该有 gap。gap=0 证明差异来自复杂度，不来自任务难度。\n\n    '\n- name: Diagnostic Re-repair Experiment\n  plan_id: diagnostic-rerepair\n  description: 给 repair agent per-test failure predictions vs 无 per-test info，在 200\n    instances 上比较 resolve rate。\n  expected_results:\n    n_instances: 200\n    baseline_resolve_rate_pct: 26.5\n    rerepair_without_diagnostics_resolve_rate_pct: 29.0\n    rerepair_with_diagnostics_resolve_rate_pct: 34.5\n    diagnostic_lift_pp: 5.5\n    blind_rerepair_lift_pp: 2.5\n    n_rerepair_triggered: 89\n    rerepair_success_rate_with_diag_pct: 27.0\n    rerepair_success_rate_without_diag_pct: 14.6\n    p_value_mcnemar: 0.016\n    multi_f2p_diagnostic_lift_pp: 10.8\n    single_f2p_diagnostic_lift_pp: 2.3\n  result_rationale: 'Diagnostic lift 5.5pp（在 best tier 范围 [3, 8] 内）来自 per-test predictions\n    为 repair agent\n\n    提供了 actionable 的失败定位信息。当 agent 知道 \"test_parse_edge_case fails but test_parse_basic\n    passes\" 时，\n\n    它可以将修复集中在 edge case 处理逻辑上，而不是盲目重试。\n\n    Blind re-repair（知道 \"有 test 失败\" 但不知道哪个）仍有 2.5pp 提升，因为重试本身就有价值——\n\n    但 diagnostic-specific lift（5.5 - 2.5 = 3.0pp 增量，或相对于 blind 的 +5.5pp）\n\n    证明了 per-test 信息的独特贡献。\n\n    优势集中在 multi-F2P instances（lift 10.8pp vs single-F2P 2.3pp），\n\n    与 oracle 分析的预测一致：当有多个 failing tests 时，知道哪些 fail 的信息增益最大。\n\n    McNemar p=0.016 在 200 样本下达到显著性，虽然样本量有限但足以支撑 proof-of-concept。\n\n    '\n  tables:\n  - name: 'Table 13: Diagnostic Re-repair Results'\n    columns:\n    - Condition\n    - Resolve Rate\n    - Δ vs Baseline\n    rows:\n    - - No re-repair (baseline)\n      - 26.5%\n      - —\n    - - Re-repair without diagnostics\n      - 29.0%\n      - +2.5 pp\n    - - Re-repair with per-test diagnostics\n      - 34.5%\n      - +8.0 pp\n    - - Diagnostic-specific lift\n      - —\n      - +5.5 pp (p=0.016)\n  - name: 'Table 14: Diagnostic Lift by F2P Count'\n    columns:\n    - F2P Count\n    - '% Instances'\n    - Diag Lift\n    - Blind Lift\n    rows:\n    - - T=1\n      - 69%\n      - +2.3 pp\n      - +1.8 pp\n    - - T=2\n      - 16%\n      - +8.2 pp\n      - +2.5 pp\n    - - T≥3\n      - 15%\n      - +10.8 pp\n      - +3.6 pp\n  figures_description:\n  - 'Figure 14: Grouped bar chart — three conditions (baseline / blind / diagnostic)\n    × stratified by T'\n  analysis: 'Re-repair 实验是 Claim 2 的锚点。5.5pp lift 在统计上显著且实际有意义。\n\n    Stratification 连接了 Claim 2 和 Claim 3：diagnostic 优势集中在 multi-F2P instances，\n\n    正是 oracle 分析预测的 \"sweet spot\"。\n\n    论文应定位为 proof-of-concept（不是 SOTA repair），目标是展示机制而非最优数字。\n\n    '\n- name: LLM-as-Judge Baselines\n  plan_id: llm-judge-baseline\n  description: Qwen3-8B/32B zero-shot LLM-as-judge，trajectory 和 per-test 两种模式。作为 Pareto\n    frontier 参考点。\n  expected_results:\n    qwen_8b_zs_traj_f1: 67.5\n    qwen_8b_zs_traj_accuracy: 68.3\n    qwen_8b_zs_pertest_macro_f1: 63.8\n    qwen_32b_zs_traj_f1: 73.2\n    qwen_32b_zs_traj_accuracy: 74.1\n    qwen_32b_zs_pertest_macro_f1: 70.5\n    finetuned_4b_cls_macro_f1: 87.5\n    finetuned_4b_cost_per_instance: 0.001\n    qwen_8b_cost_per_instance: 0.003\n    qwen_32b_cost_per_instance: 0.012\n  result_rationale: 'Zero-shot LLM judges 大幅低于 fine-tuned classifiers，原因：\n\n    (1) Execution simulation 在 pretraining 数据中代表性不足——模型能推理代码语义\n\n    但没有学过系统性地预测 pass/fail outcomes；\n\n    (2) Zero-shot 缺乏 calibration——模型倾向于过度自信或过度保守，没有训练信号来校准阈值；\n\n    (3) Per-test zero-shot 更差（63.8% vs 67.5% trajectory）因为需要逐个 test 推理，\n\n    而没有训练数据教模型如何处理单个 test 的判断。\n\n    Qwen3-8B zero-shot（67.5%）甚至低于 4B fine-tuned CWM（87.5%），\n\n    说明 fine-tuning 在此任务上比 8× 参数量更有价值。\n\n    Qwen3-32B zero-shot（73.2%）仍然远低于 4B fine-tuned classification（87.5%），\n\n    说明即使 32B 规模的 zero-shot prompting 也无法替代 task-specific fine-tuning。\n\n    这占据 Pareto frontier 的低效区域：高成本（$0.012）低 accuracy。\n\n    '\n  tables:\n  - name: 'Table 15: Pareto Frontier — Accuracy vs Cost'\n    columns:\n    - Method\n    - Params\n    - Fine-tuned\n    - Macro F1\n    - Cost/Instance\n    rows:\n    - - LLM-Judge ZS\n      - 8B\n      - 'No'\n      - 67.5%\n      - $0.003\n    - - LLM-Judge ZS\n      - 32B\n      - 'No'\n      - 73.2%\n      - $0.012\n    - - CWM Gen (func)\n      - 4B\n      - 'Yes'\n      - 87.5%\n      - $0.002\n    - - Cls (func)\n      - 4B\n      - 'Yes'\n      - 87.5%\n      - $0.001\n    - - Cls (func)\n      - 8B\n      - 'Yes'\n      - 90.1%\n      - $0.002\n    - - Cls (repo)\n      - 4B\n      - 'Yes'\n      - 82.0%\n      - $0.001\n  figures_description:\n  - 'Figure 15: Pareto frontier scatter plot (F1 vs cost-per-instance)，fine-tuned\n    classification 占据 optimal 角'\n  analysis: 'LLM-judge baselines 回应两个 reviewer concern：\n\n    (1) \"Why not just prompt a large model?\" — 因为 32B zero-shot 仍比 4B fine-tuned 差\n    14pp。\n\n    (2) \"Is fine-tuning necessary?\" — 是的，task-specific training signal 在结构化预测任务上不可替代。\n\n    Pareto frontier figure 是论文中最直观的可视化之一。\n\n    '\n- name: Per-test Majority Voting (K=3)\n  plan_id: per-test-majority-voting\n  description: Classification model 温度采样 K=3 次取多数票，测试 self-consistency 是否提升 per-test\n    accuracy。\n  expected_results:\n    k3_pass_f1: 88.5\n    k3_fail_f1: 89.2\n    k3_macro_f1: 88.9\n    k3_accuracy: 89.0\n    single_pass_macro_f1: 87.5\n    improvement_from_voting_pp: 1.4\n    cost_multiplier: 3.0\n    disagreement_rate_pct: 13.5\n    disagreement_accuracy: 62.3\n  result_rationale: 'Majority voting 提供 1.4pp 边际改善（87.5→88.9），但代价是 3× 推理成本。\n\n    改善小的原因：base classifier 在 87.5% 已经是 well-calibrated 的——\n\n    大多数预测高置信度（86.5% 的 cases 三次投票一致），self-consistency 只在 13.5% 的\n\n    边界 cases 上有机会纠正错误，且其中也只有 62.3% 被正确纠正。\n\n    对比：直接用 8B 模型（+2.6pp, ~2× cost）比 4B majority voting（+1.4pp, 3× cost）更高效。\n\n    结论：majority voting 是 diminishing returns，model scaling 是更好的 accuracy 提升路径。\n\n    这是 appendix 级别的 P2 结果。\n\n    '\n  tables:\n  - name: 'Table S1 (Appendix): Majority Voting Results'\n    columns:\n    - Method\n    - Macro F1\n    - Relative Cost\n    rows:\n    - - Single-pass (4B)\n      - 87.5%\n      - 1×\n    - - Majority K=3 (4B)\n      - 88.9%\n      - 3×\n    - - Single-pass (8B)\n      - 90.1%\n      - ~2×\n  figures_description: []\n  analysis: 'Appendix 级结果。主要贡献是确认 self-consistency 在此任务上 ROI 低，\n\n    应优先考虑 model scaling。Disagreement rate 可以作为 confidence proxy 用于 selective abstention。'\n",
      "numLines": 949,
      "startLine": 1,
      "totalLines": 949
    }
  },
  "sourceToolAssistantUUID": "0ffaea46-f380-4a15-a760-e072a4493b13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20 · 2026-05-16T07:40:34.486Z_

````json
{
  "parentUuid": "988e3c11-211c-47c1-ad77-6878d937bbf3",
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
  "uuid": "d0d22781-28ec-40aa-8c5d-3c07bdaae763",
  "timestamp": "2026-05-16T07:40:34.486Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Repo-level CLS显著优于CWM，DeepSeek复现确认架构无关性，formulation advantage story完整成立 核心假设：['Repo-level CLS多seed稳定≥85% accuracy，fail_f1≥75%（当前单seed: 84.79%/81.18%）', 'CW…",
  "leafUuid": "d0d22781-28ec-40aa-8c5d-3c07bdaae763",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Define best-tier results for repo-level verification via three-level evidence chain",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f"
}
```

---

### Assistant

_source line 23 · 2026-05-16T07:45:08.970Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view. Let me understand what's needed:

1. The user wants me to generate predictions for "planned" experiments in the experiment_plan under the "best" tier.

Looking at the experiment_plan, the experiments with status "planned" are:
- `diagnostic-rerepair` 
- `swebench-pertest-data`

But the best tier definition also requires:
- Repo-level CLS multi-seed stable ≥85% accuracy, fail_f1≥75%
- CWM repo-level unparseable rate ≥80%
- DeepSeek function-level reproducing CLS≈CWM pattern


- 8B scaling gap around 2.43pp at the repo level

The DeepSeek experiments are currently running, and while many repo-level experiments have already been completed, the key ones I need to predict for are diagnostic-rerepair and swebench-pertest-data, though the latter is implicitly done given the existing repo-level work. The repo-level CLS multi-seed is partially complete with single seed results at 84%.

79%/81.18%, while CWM attempts have mostly failed with high unparseable rates, with v10 being the best at 93% unparseable.

Looking back at the user's request, they're asking for detailed data specifically on experiments marked as "planned" in the experiment_plan—diagnostic-rerepair and swebench-pertest-data—but the best tier predictions also require accounting for repo-level multi-seed, CWM, and DeepSeek experiments that may not have "planned" status yet.

I think the user's intent is broader than just the formally planned experiments. They want predictions for all experiments needed to complete the best tier narrative, which includes swebench-pertest-data and diagnostic-rerepair as the planned ones, plus repo-level CLS multi-seed runs that are still needed.

But I also need to account for the DeepSeek experiments currently running at function and repo levels, the repo-level CWM work that's showing high unparseable rates, and the oracle ensemble approach at repo level. Looking back at the Phase 1 best tier requirements, the core assumptions are that repo-level CLS needs to hit ≥85% accuracy with fail_f1≥75% across multiple seeds (currently at 84.79%/81.18% for single seed), and CWM's unparseable rate needs to be ≥80% to be accepted as a formulation limitation rather than a tuning issue.

The key gaps I'm tracking are whether DeepSeek can replicate the CLS versus CWM pattern at function level to confirm this isn't Qwen-specific, and whether the 8B scaling gap combined with repo-level performance differences creates a complete evidence chain for complexity-dependent advantages. I'm monitoring specific metric ranges across all these experiments to validate the tier requirements.

Now I need to map out which experiments are actually running versus planned—the repo-level multi-seed CLS, CWM unparseable rates, DeepSeek function and repo-level results, and the oracle ensemble are all in flight or queued, while diagnostic-rerepair is still on the roadmap.

Looking at the existing repo-level CLS results to calibrate my predictions, I see the 8B models are consistently outperforming the 4B variants, with the seed123 checkpoint hitting 85.6% accuracy and the s42 checkpoint at 85.47%, while the 4B models trail around 83-87% depending on the checkpoint.

Now examining the CWM results, which show a much wider performance spread—the v10 variant achieves nearly 70% accuracy but struggles with parseability at 93%, while the later versions trade off accuracy for better parseability, with v12 dropping to 58% accuracy but improving unparseable rates to 53.7%.

Looking at the function-level comparisons, CLS consistently outperforms CWM across both model sizes, with the 8B models showing about a 2.8 percentage point gap in accuracy. I'm now working through the best-tier predictions by examining the ranges across successful runs and estimating where the next experiments should land—targeting around 85.5% for repo-level CLS accuracy and 74% for the fail F1 score.

I need to double-check which experiments are actually planned versus which ones I'm inferring are needed. The diagnostic-rerepair and swebench-pertest-data runs are confirmed, but repo-level CLS multi-seed results aren't explicitly scheduled yet, so I should verify that's covered before finalizing the YAML output. Looking at what's changed since the previous dream report, most of the original 11 experiments are now complete, leaving just two still in the planned stage: the SWE-bench per-test dataset work and diagnostic re-repair. On top of that, the updated best tier definition introduces several new experiments I need to account for—repo-level multi-seed validation with DeepSeek, function and repo-level variants, oracle ensemble approaches, and confirmation of the repo-level CWM unparseable rates.

Examining the current repo-level results more closely, the classification scores are actually quite solid across different seeds and checkpoints, clustering in that 84-88% accuracy range. But the CWM results are consistently problematic—hitting 93% unparseable rates and showing similar issues across different versions.

The unparseable rates are all over the place, from 53.7% down to 75.2%, but they all fall short of the ≥80% threshold needed for the best tier. DeepSeek experiments are still running and I need their predictions. Let me finalize the YAML output for the best tier, including both the planned experiments and these critical running ones.

Wait, I should double-check what the user actually asked for—they want detailed data for each planned experiment in the experiment_plan. The plan only lists 2 planned experiments, but the DeepSeek ones are currently running, not planned yet. Though looking at the registry more carefully...

Actually, I think the user is using "planned" more loosely to mean experiments that haven't finished yet and need predictions. So I should include the 2 explicitly planned ones plus all the running DeepSeek experiments and the repo-level variants implied by the best tier hypotheses. That gives me a complete picture of what's needed to validate the best tier.

For swebench-pertest-data, this is really the dataset construction step that's already been effectively completed through the existing repo-level experiments—they're already using the 9784 test samples. I'd expect around 478 successful instances with the standard distribution.

For diagnostic-rerepair, this is the downstream validation of the per-test repair approach. The key metric is resolve rate improvement, and based on previous predictions I'm expecting around a 5.5 percentage point lift.

Now looking at the repo-level CLS multi-seed results, I have the single seed baseline at 84.79% accuracy with 72.93% fail_f1. For the best tier I need to hit [84, 88] accuracy and [72, 82] fail_f1. With multiple seeds I'd expect the mean accuracy to land around 85-86% with roughly 1 percentage point variation, similar to what we saw at the function level. The seed123 checkpoint results are coming in lower on fail_f1 than the s42 baseline though—I'm checking which checkpoint actually performed best for that seed.

Looking at the actual numbers, seed123 gives me 85.6% accuracy but only 65.89% fail_f1, while s42 sits at 84.79% accuracy with 72.93% fail_f1. There's clearly a precision-recall tradeoff happening here. When I average these two seeds, I get around 85.2% accuracy but only 69.4% fail_f1—which falls short of the [72, 82] requirement for the best tier. This suggests seed123 needs a different checkpoint to bring that fail_f1 metric up to where it needs to be.

Let me also check what the 4B v5 model is doing. The validation results look promising at 90.07% accuracy and 76.37% fail_f1, but there's a significant drop on the test set to 83.63% accuracy and 61.67% fail_f1. The 4B seed123 checkpoint only reached 75.33% accuracy on test, which is concerning. For the 8B model, I'm seeing s42 ckpt400 at 84.79% accuracy and 72.93% fail_f1, but when I move to ckpt1000 the accuracy dips to 83.52% and fail_f1 drops further to 65.

85%. The later checkpoints and seed123 variants all cluster around 84-85% accuracy with fail_f1 in the 60s range. The s42 ckpt400 checkpoint stands out as the only one hitting that 72.93% fail_f1 threshold, so I'd need to run additional seeds to see if we can consistently reach that performance level across multiple runs.

Actually, I'm reconsidering the framing here. The user is asking for a prediction of what the best tier would look like if we achieved it, not whether we can achieve it. So I should work within the defined ranges—accuracy between 84-88% and fail_f1 between 72-82%—and justify why those numbers make sense given the hypothesis that multi-seed stability at ≥85% accuracy and ≥75% fail_f1 is possible. The current single-seed result shows 84.79% accuracy and 72.93% fail_f1, so the best tier prediction would be a modest improvement across multiple seeds to hit that ≥85% and ≥75% target.

For CWM, the unparseable rate varies significantly with generation settings—v10 with shorter tokens hit 93%, but v11 with longer generation dropped to 75.2%, and v12 with different config was 53.7%. So achieving the ≥80% threshold for best tier is plausible with the right configuration tuning. For DeepSeek, I'm starting to look at what the 6.7B model's performance characteristics might be.

Now I'm reconsidering the structure of what the user actually asked for. Looking back at the experiment_plan, there are only two experiments marked as "planned"—swebench-pertest-data and diagnostic-rerepair. But the best tier predictions require DeepSeek results that aren't in the plan yet, and repo-level multi-seed results that are already marked as done. Let me refocus on what's actually planned versus what's already completed.

For the best tier story, I need to identify which experiments are still missing. Looking at the repo-level CLS multi-seed results, I have checkpoints from two seeds so far, but I'm checking whether we have enough data or if a third seed is needed to make the story complete.

Examining the metrics more closely, seed123's test fail_f1 is significantly lower than its validation performance, which is concerning for the best tier threshold. I'm comparing this against s42's results to understand if the discrepancy is due to different checkpoint selections or training duration, and checking whether seed123 has an earlier checkpoint that might perform better.

Stepping back, I realize the user is asking me to predict what the best-case scenario would look like if everything aligned perfectly—not to validate existing results. In that ideal scenario, multi-seed experiments would show consistent high accuracy above 85% with fail_f1 stabilizing at 75% or higher, CWM would demonstrate elevated unparseable rates, and DeepSeek would confirm the architecture-independent nature of the findings.

Looking at the current data, repo-level CLS is already at 84.79%, which sits at the lower bound of the best tier range, so subsequent seeds would need to push above 85% to solidify that tier. I'm mapping the experiment plan IDs now—swebench-pertest-data and diagnostic-rerepair—and noting the DeepSeek variants (repo-level CLS, function-level CWM, and function-level CLS) as the additional experiments that would complete the evidence chain for the best tier prediction. Now I'm looking at the specific accuracy and F1 scores across the three seeds, with s42 already measured and s123, s456 as predictions. The mean repo-level performance would be around 85.6% accuracy with 0.73% standard deviation, though I'm realizing the actual s123 data shows lower failure F1 than expected, so I'd need to assume better checkpoint selection or training improvements for the best tier hypothesis to hold—essentially, if the s42 checkpoint happened to be well early-stopped, then sweeping checkpoints properly at 8192 sequence length for the other seeds should yield similar results.

Looking at the actual s123 test data though, the earlier checkpoint shows much worse accuracy, and there's no ckpt400 available for that seed since it was trained separately with different convergence behavior. Rather than getting caught up in what actually happened, I should frame this as a best-case scenario prediction—if the additional seeds converge similarly to s42, the performance would fall within the expected range, so I'll write out these predictions as the optimistic but grounded dream report.

Now I'm laying out the experiments to include in the YAML: the swebench pertest data, the repo-level multiseed and CWM variants implied by the best tier hypotheses, the running DeepSeek experiments across function and repo levels, the oracle ensemble, and the diagnostic rerepair. I'll start with predictions for the DeepSeek model, which is a specialized 6.7B parameter code model that should perform well at the function level.

For the function-level tasks, I'm expecting around 85-88% accuracy with CLS and CWM performing similarly, with a small gap between them. But when I look at the repo-level oracle ensemble, the numbers don't quite add up—if function-level CLS is around 85% and CWM drops to 50-60% due to parsing issues, the ensemble wouldn't reach the 90%+ range unless it's actually measuring function-level performance. Let me reconsider what the oracle ensemble metrics are actually referring to.

Looking back at the paper framing, the oracle ensemble reached 90.63% at the function level, and the registry shows several completed oracle experiments. So that 90-93% accuracy range in the best tier is already a confirmed measurement, not a prediction.

The experiments I actually need to forecast are the remaining ones: the SWE-bench per-test data collection, diagnostic re-repair validation, additional seeds for repo-level CLS, confirmation that repo-level CWM unparseable cases stay above 80%, and the three DeepSeek function-level runs that are currently in progress.

Let me work through predictions for each of these systematically, mapping them to their plan IDs where applicable.

For the SWE-bench per-test data, I've essentially already captured this through the repo-level experiments—the dataset itself with 9784 test and 9335 validation samples is ready. The repo-level CLS multiseed needs a third seed beyond the s42 checkpoint 400 (84.79%) and seed 123 checkpoint 3000 (85.6%) runs I already have, targeting a mean above 85% with fail F1 above 75%. The CWM unparseable confirmation is checking whether the v10 model's 93% unparseable rate stays above the 80% threshold for best tier. And I'm waiting on the DeepSeek function-level classification and CWM runs to complete.

For DeepSeek on repo-level classification, I'm expecting this to validate that the architecture works consistently across different model families, and then I'll have the downstream diagnostic experiment with 200 instances to round out the full picture. Now I need to structure all of this into the YAML output the user is expecting. I'm settling on including all the experiments needed for the best tier narrative, whether they were in the original plan or emerged as part of the updated definition. Let me structure the output with the tier, narrative guidance covering the three-level evidence chain from function-level equivalence through repo-level collapse, and DeepSeek's confirmation that the pattern holds across architectures.

Defining the imagined experiments...

Now I'm working through the expected metrics for the SWE-bench-PerTest dataset — we've essentially already constructed it with around 9784 test samples and 9335 validation samples across the repo-level experiments, though I should formally mark this as complete. I'm estimating roughly 489 successful instances out of the target, with about 11 docker failures.

For the repo-level CLS multi-seed validation, I'm looking at whether we can hit that best tier threshold of 85% accuracy and 75% fail_f1. The current checkpoints show promise — the 8B model at seed42 reaches 84.79% accuracy with 72.93% fail_f1, while seed123 gets slightly higher accuracy at 85.6% but drops to 65.89% fail_f1. The challenge is whether additional seeds can push the fail_f1 metric up to meet the tier requirement.

Looking at the 4B results for comparison, I notice the val5120 checkpoint performs better on fail_f1 (71.57%) than the test set, suggesting sequence length tuning matters. For the 8B multi-seed approach, I'm thinking checkpoint selection is critical — seed42 peaked at ckpt400, so seed123 might also benefit from an earlier checkpoint rather than ckpt3000, which could be overtraining.

Checking the available seed123 test results, I see ckpt200, ckpt3000, ckpt6200, ckpt6400, ckpt6600, and ckpt6633, but no ckpt400 evaluation exists for that seed. The best performance so far is ckpt3000 at 85.6% accuracy, though the later checkpoints cluster around 84.7-85.08%. For the ideal scenario, I'd estimate what a hypothetical earlier checkpoint might achieve.

Looking at the other seeds, s42 hits 84.79% accuracy with 72.93% fail_f1, while s456 reaches 85.5% accuracy with 75.5% fail_f1. If seed123 could match that trajectory with a better checkpoint selection—maybe something in the ckpt600 range that showed stronger fail_f1 on validation—it could potentially reach the best tier threshold of fail_f1≥75%, though the current 65.89% is a significant gap to close. So a third seed s456 would likely fall in that same performance range. Let me project what the results might look like if I apply the same early-stopping strategy across all three seeds: s42 at ckpt400 gives me 84.79% accuracy and 72.93% fail_f1, seed123 remeasured at an earlier checkpoint would probably hit around 85.2% accuracy and 75.8% fail_f1, and s456 following the same pattern would reach roughly 85.8% accuracy and 76.4% fail_f1. That would put the ensemble mean at about 85.3% accuracy and 75.0% fail_f1. The key insight is that s42's ckpt400 hit a sweet spot where precision and recall for failures were both well-balanced in the 70-76% range, and if I apply that same early-stopping logic based on validation fail_f1 to the other seeds, they should converge to similar performance levels rather than the overtrained state seed123 reached at ckpt3000.

For the repo-level CWM unparseable confirmation task, I'm looking at the gap between v10's 93% unparseable rate with just 64 tokens and v11's 75.2% with 1024 tokens. Since the best tier needs at least 80%, and 64 tokens was clearly insufficient, I'd estimate that with a middle ground of 256-512 tokens, the unparseable rate would land somewhere in the 82-88% range. My prediction is that with max_new_tokens=512, I'd see about 84% unparseable, roughly 68% accuracy on the predictions that do parse, which translates to around 45% overall accuracy when treating unparseable outputs as failures. The issue is that repo-level execution outputs are inherently long—often hundreds to thousands of tokens—so even 512 tokens isn't always enough for the model to complete its reasoning and produce a clear pass/fail judgment.

Wait, I need to reconsider the relationship here. If 64 tokens gives 93% unparseable and 1024 tokens gives 75%, then more tokens actually *lowers* the unparseable rate. That means at 512 tokens I'd expect something closer to 85%, not 84%. Looking at the data points again: 64 tokens is 93%, 1024 tokens is 75%, so interpolating around 256-512 tokens would put me in the 85-88% range. But the best tier requirement is ≥80% unparseable, which seems backwards—I need to clarify whether the tier is actually asking for a *lower* unparseable rate or if there's a misunderstanding about what "best tier" means here.

Actually, the argument being made is that CWM has inherent limitations causing high unparseable rates, not just parameter tuning issues. Looking at the v11 metrics, the model generates outputs averaging 3,300+ tokens, yet even at 1024 max tokens, 75% are still unparseable—meaning the outputs get truncated. So if I use a fair generation length matching typical output sizes (around 200-500 tokens), the unparseable rate would be roughly 85%, which still demonstrates CWM's fundamental problems.

For the dream scenario with max_new_tokens=2048, I'm predicting an unparseable rate around 82% with 65% accuracy on the parseable outputs, giving an overall accuracy of roughly 11-12%.

The core issue is that repo-level execution outputs have complex structures—stack traces, file paths, formatted data—and even with a generous token budget, CWM struggles with string prediction errors and format-sensitive outputs like JSON or XML.

Now looking at DeepSeek-Coder-6.7B for function-level classification, it's a code-specialized model that should fall between the Qwen3-4B and Qwen3-8B performance levels, so I'd expect accuracy around 87-89%. The model is from an older generation though, which might affect how it compares to more recent alternatives.

Given the architecture differences and training data gap, I'm predicting DeepSeek will hit around 86.5% on CLS and 86% on CWM at the function level, with a gap of about 0.5 percentage points—suggesting the null result holds across different architectures. The same reasoning applies to the CWM predictions, and I'm starting to work through the multi-seed scenarios.

For repo-level performance, I'm estimating DeepSeek will land in the 78-82% range, slightly lower than Qwen3-8B given its older training. On the diagnostic repair side, I'm predicting the baseline resolve rate around 27%, improving to 33% with diagnostics for a 6 percentage point lift, with multi-F2P showing an 11pp improvement and single-F2P around 2.5pp.

Now I have enough detail to structure the complete YAML output, making sure it's comprehensive while matching the format from the previous report.

The user emphasized that each prediction needs a result_rationale explaining mechanistically why these results occur in the best tier. I need to ground the predictions in existing data and connect the numbers back to the theoretical framework. I'm also keeping in mind the core assumptions for the best tier: repo-level CLS multi-seed stability ≥85% accuracy with fail_f1≥75%, CWM repo-level unparseable ≥80% accepted as formulation-inherent, and DeepSeek function-level reproducibility constraints.

Now I'm selecting specific values within the defined metric ranges for each experiment—starting with repo_cls_accuracy_multiseed at 85.5%, which sits at the lower end of the [84, 88] range to reflect realistic multi-seed stability while maintaining the best tier threshold.

Generating YAML structure...

I'm organizing the experiments by hypothesis and then reconsidering the oracle ensemble approach—at the repo level, the very high unparseable rate for CWM makes an ensemble less practical since we wouldn't have reliable predictions across both methods on the same test set.

Since the function-level oracle ensemble is already measured at 90.63%, which falls within the expected range, I can skip that experiment and focus on the seven core ones: the SWE-bench-PerTest dataset, repo-level variants of CLS and CWM, DeepSeek function-level experiments, and diagnostic re-repair analysis.

Now I'm wondering if I should also dig into repo-level failure modes—specifically breaking down CWM's issues between token exhaustion and string mismatches, plus analyzing how context length affects performance across different repository complexities.

Let me verify the 4B and 8B repo-level checkpoints I'm working with: the 4B model peaked at 90.07% validation accuracy with checkpoint 4600, while test performance was 83.63%, and the 8B variant achieved 85.6% test accuracy with seed 123 at checkpoint 3000.

The 8B model shows a modest accuracy gain over 4B at the repo level (84.79% vs 83.63%), but the real win is in fail_f1 where it jumps from 61.67 to 72.93—that's a meaningful improvement in catching actual failures. Now I need to structure the final YAML output with all the experiments, results, and analysis tied together into a coherent narrative about model scaling.

I'm thinking about scope here—the previous dream report had 12 experiments across roughly 1000 lines, so I should aim for similar depth without bloating it. Some experiments are already validated (like the func-level multi-seed and 8B scaling), but I need to focus predictions on what's still open: the SWE-bench-PerTest dataset, repo-level multi-seed runs beyond seed 42, the repo-level CWM attempts, the DeepSeek experiments currently running across func and repo levels, and the diagnostic re-repair work. That's seven key experiments that fill the gaps in the best tier story.

Composing the YAML now...

I'm reconsidering DeepSeek's positioning—it's a 2023 model with 6.7B parameters versus Qwen3-4B from 2025, so despite the parameter advantage, the generation gap might make them closer in capability than raw numbers suggest. For function-level tasks, I'd expect DeepSeek to land slightly below Qwen3-4B's multi-seed mean of 88.41% but still well above baseline, around 85-86% for CLS and 85% for CWM with roughly a 0.5-1.0 percentage point gap between them. At the repo level, DeepSeek CLS should hit 80-83%, which is lower than Qwen3-8B's 84.79%.

Now I'm looking at the SWE-bench-PerTest results and the multi-seed repo CLS performance across different random seeds. The dataset has 489 successful instances with an average of 3.0 attempts per problem, and I'm cross-checking the fail_f1 scores across seeds to ensure they meet the quality threshold—the mean fail_f1 is coming in around 75.3%, which sits at the lower end of the acceptable range.

Moving through the other model evaluations: the Repo CWM approach shows significant parsing challenges with 85% unparseable instances and only 51% overall accuracy. DeepSeek's function-level models perform much stronger, with the CLS variant hitting 86.3% accuracy and balanced F1 scores around 86%, while the repo-level CLS drops to 81.5% with weaker fail_f1 at 69.8%. The diagnostic re-repair approach shows promise with a 6 percentage point lift over the baseline when incorporating diagnostic information.

Writing the YAML configuration...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0d22781-28ec-40aa-8c5d-3c07bdaae763",
  "isSidechain": false,
  "requestId": "req_011Cb5sNpxhAB8RycrCjL4FE",
  "type": "assistant",
  "uuid": "165f2549-4a7a-4ddc-840b-8b82279dfd79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2dRc2F42eefdfC6a9Rtwa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20078,
      "cache_read_input_tokens": 46906,
      "output_tokens": 23055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20078,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 23055,
          "cache_read_input_tokens": 46906,
          "cache_creation_input_tokens": 20078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20078
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

_source line 24 · 2026-05-16T07:48:14.435Z_

Now I have the full context. Let me synthesize the predictions grounded in existing data for each experiment needed to complete the best tier story.

```yaml
tier: best
narrative_guidance: >
  Classification reformulation提供complexity-dependent scaling advantage：
  function-level CLS≈CWM null result（三级证据：Qwen3-4B null → 8B diverge 2.43pp → repo-level CWM崩溃）。
  DeepSeek-Coder-6.7B复现function-level null result确认结论非Qwen-specific。
  Repo-level CLS 3-seed稳定≥85% accuracy，CWM因unparseable≥80%彻底失败。
  Complementary errors + oracle ensemble（90.63%）作为bonus contribution。
  Diagnostic re-repair以~6pp resolve rate gain验证per-test granularity的实用价值。
  Original claims无需调整，三个claim完整成立。Target: EMNLP Main。

imagined_experiments:
  - name: "SWE-bench-PerTest Dataset Construction"
    plan_id: "swebench-pertest-data"
    description: >
      Docker重新执行SWE-bench Verified patches提取per-test labels。
      已通过repo-level实验系列隐式完成（test set 9784 samples, val set 9335 samples）。
    expected_results:
      n_instances_target: 500
      n_instances_successful: 489
      n_instances_docker_fail: 11
      total_test_samples: 9784
      total_val_samples: 9335
      avg_f2p_tests_per_instance: 3.0
      median_f2p_tests: 2
      avg_p2p_tests_per_instance: 47.8
      f2p_T1_pct: 68.7
      f2p_T2_pct: 19.1
      f2p_T3plus_pct: 12.2
      docker_wall_clock_hours: 18.5
      n_parallel_containers: 16
      label_agreement_with_original_pct: 98.7
      flaky_test_rate_pct: 1.0
      class_balance_pass_pct: 72.96
      class_balance_fail_pct: 27.04
    result_rationale: >
      489/500成功率（97.8%）略高于前次预测，因为SWE-bench Verified本身经过质量筛选，
      Docker环境兼容性好于完整SWE-bench。11个失败主要来自极老repo的Python 3.7依赖
      和少量C extension编译失败。F2P分布与SWE-bench Verified已知统计一致（median=2, mean=3）。
      类别不平衡72.96% pass / 27.04% fail与repo-level-cls-v5实验的majority baseline吻合。
      98.7% label agreement验证Docker re-evaluation的方法论可靠性——
      1.3%不一致来自flaky tests（1.0%）和时间敏感assertions（0.3%）。
      数据集本身是独立resource contribution，使任何future work on SWE-bench per-test verification成为可能。
    tables:
      - name: "SWE-bench-PerTest Dataset Statistics"
        columns: [Statistic, Value]
        rows:
          - [Instances (successful), 489]
          - [Candidates per instance, 16]
          - [Total test-level samples, 9784]
          - [Avg F2P tests/instance, 3.0]
          - [Median F2P tests, 2]
          - [Avg P2P tests/instance, 47.8]
          - [Class balance (pass%), 72.96%]
          - [Label agreement, 98.7%]
    figures_description:
      - "F2P test count histogram (T=1 to T=10+)，展示T=1占68.7%的长尾分布"
      - "Per-instance total test count distribution，展示repo-level测试规模"
    analysis: >
      数据集已通过repo-level实验系列隐式构建并验证。F2P分布确认31.3%的instances有T≥2，
      为per-test advantage提供足够的multi-F2P样本。P2P测试数量大（avg 47.8）但regression rate ~1%
      意味着P2P对per-test advantage贡献极小。数据集的主要价值是enable repo-level CLS vs CWM对比。

  - name: "Repo-Level CLS Multi-Seed Validation (8B)"
    plan_id: "repo-level-training"
    description: >
      Qwen3-8B LoRA classification在repo-level SWE-bench-PerTest上的3-seed验证。
      当前有s42 (ckpt400, 84.79%)和seed123 (ckpt3000, 85.6%)，需第3个seed并统一checkpoint selection策略。
      Best tier要求mean accuracy≥85%, fail_f1≥75%。
    expected_results:
      seed42_accuracy: 84.79
      seed42_fail_f1: 72.93
      seed42_pass_f1: 89.43
      seed42_checkpoint: ckpt-400
      seed123_accuracy: 85.8
      seed123_fail_f1: 76.2
      seed123_pass_f1: 90.1
      seed123_checkpoint: ckpt-500
      seed456_accuracy: 85.9
      seed456_fail_f1: 76.8
      seed456_pass_f1: 90.5
      seed456_checkpoint: ckpt-450
      mean_accuracy: 85.5
      std_accuracy: 0.61
      mean_fail_f1: 75.3
      std_fail_f1: 2.1
      mean_pass_f1: 90.0
      mean_f1_macro: 82.7
      unparseable_all_seeds: 0
      bootstrap_ci_accuracy_95: [84.6, 86.4]
    result_rationale: >
      当前s42 ckpt400的72.93% fail_f1是所有8B repo-level实验中最高的——
      原因是ckpt400处于early-stopping sweet spot，fail precision(70.32%)和recall(75.74%)相对平衡。
      seed123的ckpt3000训练过长导致严重的precision-recall偏移：precision_fail高达91.65%但recall_fail仅51.44%，
      模型过度保守地预测fail（宁可漏报不误报），导致fail_f1=65.89%。
      Best tier假设统一checkpoint selection策略（按val fail_f1选最佳ckpt而非按accuracy），
      seed123在ckpt500附近可以恢复fail recall到~68%，将fail_f1提升至76.2%。
      seed456作为新seed，在相同selection策略下预期表现与seed123相近。
      3-seed mean accuracy 85.5%稳定在[84,88]范围中部，std=0.61pp反映正常的LoRA初始化随机性。
      fail_f1 mean 75.3%在[72,82]范围下部但≥75%，验证CLS在repo-level的稳定性。
      关键洞察：repo-level CLS从function-level 88.41%下降到85.5%（-2.9pp），
      下降幅度远小于CWM（从87.4%崩溃到<55%）——这是complexity-dependent advantage的核心证据。
    tables:
      - name: "Repo-Level CLS 8B Multi-Seed Results"
        columns: [Seed, Checkpoint, Accuracy, Fail F1, Pass F1, F1 Macro]
        rows:
          - [42, ckpt-400, 84.79%, 72.93%, 89.43%, 81.18%]
          - [123, ckpt-500, 85.8%, 76.2%, 90.1%, 83.2%]
          - [456, ckpt-450, 85.9%, 76.8%, 90.5%, 83.7%]
          - [Mean±Std, —, "85.5±0.61", "75.3±2.1", "90.0±0.5", "82.7±1.3"]
      - name: "Function-Level → Repo-Level Drop (CLS vs CWM)"
        columns: [Level, CLS Accuracy (3-seed), CWM Accuracy, Gap (pp)]
        rows:
          - [Function (4B), 88.41%, 87.4%, "+1.0"]
          - [Function (8B), 89.75%, 87.3%, "+2.43"]
          - [Repo (8B), 85.5%, "<55%*", ">30"]
        footnotes:
          - "*CWM repo accuracy estimated from parseable predictions only; overall accuracy <55% due to ≥85% unparseable rate"
    figures_description:
      - "3-seed accuracy + fail_f1 box plot with CI，展示跨seed稳定性"
      - "Function-to-Repo drop comparison bar chart：CLS -2.9pp vs CWM -32+pp"
    analysis: >
      Multi-seed验证是best tier的核心数据基础。3-seed std=0.61pp证明repo-level CLS结果不是单次实验的偶然。
      与function-level的std=0.96pp相比，repo-level variance更小，
      可能因为repo-level数据集更大（9784 vs 1890 samples），averaging效应更强。
      fail_f1的std=2.1pp较大，反映checkpoint selection对precision-recall tradeoff敏感——
      但mean 75.3%稳定≥75%，证明CLS可以在repo-level可靠地检测failing tests。

  - name: "Repo-Level CWM Unparseable Rate Confirmation"
    plan_id: "repo-level-training"
    description: >
      确认CWM在repo-level的unparseable rate≥80%是formulation固有缺陷。
      整合现有cwm-v10(93%), v11(75.2%), v12(53.7%), cwm-seed123-conda(67.2%)的数据。
      用标准化generation config（max_new_tokens=512, 匹配典型test output长度）重新评估。
    expected_results:
      cwm_8b_unparseable_rate: 0.85
      cwm_8b_accuracy_overall: 0.52
      cwm_8b_accuracy_parseable_only: 0.64
      cwm_8b_fail_f1: 0.18
      cwm_8b_pass_f1: 0.67
      cwm_8b_f1_macro: 0.42
      cwm_8b_truncated_pct: 0.38
      cwm_8b_string_mismatch_pct: 0.22
      cwm_8b_clean_correct_pct: 0.10
      cwm_4b_unparseable_rate: 0.88
      cwm_4b_accuracy_overall: 0.48
      majority_baseline: 0.7296
      cwm_vs_majority_gap_pp: -21.0
      generation_length_mean_tokens: 487
      generation_length_median_tokens: 512
    result_rationale: >
      现有数据已强烈支持unparseable≥80%：cwm-v10在max_new_tokens=64时93%，
      cwm-v11在1024时75.2%（但该实验用了subset500且可能有config差异）。
      标准化config（max_new_tokens=512）下预期85%，原因：
      (1) Repo-level test execution output通常包含完整stack trace（200-2000 tokens）、
      文件路径、版本号、格式化数据结构——CWM需要精确复现这些才能推导pass/fail，
      但4B/8B模型无法忠实生成如此复杂的结构化文本；
      (2) 即使生成了看似合理的output，string-level exact match极低（v10: exact_match约10%），
      因为一个字符的差异（路径分隔符、空格、换行）就导致mismatch；
      (3) Token budget exhaustion在512 tokens时仍影响38%的predictions——
      许多test output超过512 tokens，truncation导致判断信息丢失。
      关键论点：CWM的85% unparseable不是调参不足（已尝试10+版本，不同rank/alpha/generation length），
      而是generation formulation在repo-level complexity下的结构性失败——
      要求模型精确生成数百token的结构化文本是一个远难于binary classification的任务。
      Overall accuracy 52%低于majority baseline（72.96%），证明CWM在repo-level不仅无优势，
      实际上worse than trivial baseline。
    tables:
      - name: "Repo-Level CWM Failure Mode Breakdown"
        columns: [Category, "% of Predictions", Description]
        rows:
          - [Unparseable (total), 85%, "Cannot extract pass/fail from generation"]
          - ["— Token exhaustion", 38%, "Output truncated at max_new_tokens"]
          - ["— Format failure", 28%, "Output structurally invalid"]
          - ["— String mismatch", 19%, "Parseable but wrong surface form"]
          - [Parseable & correct, 10%, "CWM produces correct output"]
          - [Parseable & wrong, 5%, "Clean but incorrect prediction"]
      - name: "CWM Evolution Across Versions"
        columns: [Version, max_new_tokens, Unparseable%, Accuracy%]
        rows:
          - [v10, 64, 93%, 69.9%*]
          - [v11, 1024, 75.2%, 66.6%]
          - [v12, 512, 53.7%**, 58.0%]
          - [seed123-conda, 512, 67.2%, 59.1%]
          - ["Best-tier (standardized)", 512, 85%, 52%]
        footnotes:
          - "*v10 accuracy inflated: unparseable treated as majority-class prediction"
          - "**v12 used different training config (longer training, lower LR)"
    figures_description:
      - "Unparseable rate vs max_new_tokens curve，展示generation length与parsability的tradeoff"
      - "CWM failure mode stacked bar：token exhaustion + format failure + string mismatch = 85% total"
    analysis: >
      CWM的repo-level失败是formulation-level的必然结果，不是工程问题。
      10+版本的迭代（v1到v12，不同seed，不同LoRA配置）consistently产生50-93% unparseable rate，
      说明问题出在task formulation而非model/training细节。
      这为Claim 1提供了最强的对比：CLS在相同数据上85.5% accuracy vs CWM 52%——
      gap超过30pp，远超function-level的0-2.43pp。
      Complexity-dependent advantage的narrative完整成立。

  - name: "DeepSeek Function-Level Classification"
    plan_id: "deepseek-cls-func"
    description: >
      DeepSeek-Coder-6.7B-Instruct LoRA fine-tune做function-level per-test binary classification。
      与Qwen3-4B CLS对比，验证CLS formulation advantage不是Qwen-specific。
    expected_results:
      accuracy: 86.3
      pass_f1: 86.0
      fail_f1: 86.5
      f1_macro: 86.3
      pass_precision: 90.8
      pass_recall: 81.5
      fail_precision: 82.2
      fail_recall: 91.2
      train_loss: 0.265
      eval_loss: 0.078
      unparseable: 0
      test_set_size: 1890
    result_rationale: >
      DeepSeek-Coder-6.7B（2023年12月）比Qwen3-4B（2025年5月）多~1.7x参数，
      但属于旧generation，code understanding能力与Qwen3-4B大致equivalent。
      预期accuracy 86.3%略低于Qwen3-4B multi-seed mean（88.41%），
      因为DeepSeek的pretraining data cutoff更早，对newer coding patterns覆盖不足。
      但86.3%仍然远高于majority baseline（51.75%）和zero-shot LLM-judge（64.4%），
      证明fine-tuned classification在不同架构上consistently有效。
      关键发现：DeepSeek CLS accuracy（86.3%）与DeepSeek CWM accuracy（85.7%）的gap仅0.6pp——
      这复现了Qwen3-4B上的null result（gap 1.0pp at 4B），
      确认function-level CLS≈CWM equivalence是architecture-independent的。
    tables: []
    figures_description: []
    analysis: >
      DeepSeek CLS结果是hypothesis 3的关键支撑。
      如果gap仅在Qwen上存在，reviewer可以质疑这是Qwen-specific artifact。
      DeepSeek复现消除了这个concern。

  - name: "DeepSeek Function-Level CWM + Multi-Seed"
    plan_id: "deepseek-cwm-func"
    description: >
      DeepSeek-Coder-6.7B LoRA CWM generation baseline + seed123多seed验证。
      与DeepSeek CLS对比确认function-level null result的architecture independence。
    expected_results:
      seed42_cwm_accuracy: 85.7
      seed42_cwm_pass_f1: 85.4
      seed42_cwm_fail_f1: 86.0
      seed42_cwm_exact_match: 80.5
      seed42_cwm_unparseable: 0
      seed123_cwm_accuracy: 86.1
      seed123_cwm_pass_f1: 85.8
      seed123_cwm_fail_f1: 86.3
      seed42_cls_accuracy: 86.3
      cls_cwm_gap_seed42_pp: 0.6
      cls_cwm_gap_seed123_pp: 0.2
      cls_cwm_gap_mean_pp: 0.4
      cls_cwm_gap_95ci_lower: -0.9
      cls_cwm_gap_95ci_upper: 1.7
      paired_ttest_pvalue: 0.68
    result_rationale: >
      DeepSeek CWM在function-level预期accuracy 85.7%，与CLS的86.3%差距仅0.6pp。
      这复现了Qwen3-4B上的pattern：CWM 87.4% vs CLS 88.41%（gap ~1.0pp）。
      DeepSeek的exact match rate（80.5%）低于Qwen3-4B（84.02%），
      因为DeepSeek对function-level output format的生成精度略低——
      但由于function-level output短（<50 tokens），这些format差异不影响pass/fail判断。
      seed123 CWM（86.1%）与seed42（85.7%）的差异（0.4pp）在正常随机性范围内。
      两seed的CLS-CWM gap（0.6pp和0.2pp）mean=0.4pp，95% CI [-0.9, 1.7]包含0，
      p=0.68远超0.05，cleanly确认function-level null result。
      关键指标：deepseek_func_cls_cwm_gap_pp = 0.4pp，在best tier范围[-1.0, 1.5]内。
    tables:
      - name: "DeepSeek vs Qwen Function-Level Comparison"
        columns: [Architecture, Size, CLS Acc, CWM Acc, "Gap (pp)"]
        rows:
          - [Qwen3, 4B, 88.41%, 87.4%, "+1.0"]
          - [Qwen3, 8B, 89.75%, 87.3%, "+2.43"]
          - [DeepSeek-Coder, 6.7B, 86.3%, 85.7%, "+0.6"]
      - name: "DeepSeek Multi-Seed CWM"
        columns: [Seed, CWM Acc, CLS Acc, "Gap (pp)"]
        rows:
          - [42, 85.7%, 86.3%, "+0.6"]
          - [123, 86.1%, 86.3%*, "+0.2"]
          - [Mean, 85.9%, 86.3%, "+0.4"]
        footnotes:
          - "*CLS只训练了seed42，此处复用同一CLS模型"
    figures_description:
      - "Architecture-independent null result visualization：Qwen3-4B, Qwen3-8B, DeepSeek-6.7B三组bar pairs，function-level gap均在噪声范围内"
      - "DeepSeek CLS vs CWM per-class F1 comparison，CI完全重叠"
    analysis: >
      DeepSeek复现是best tier叙事的关键一环。三个architecture×size配置的function-level gap：
      Qwen3-4B: +1.0pp, Qwen3-8B: +2.43pp, DeepSeek-6.7B: +0.6pp。
      function-level gap始终在0-2.5pp范围内，与repo-level >30pp形成鲜明对比。
      这排除了"CLS advantage是Qwen architecture artifact"的reviewer concern。
      注意Qwen3-8B的2.43pp gap已经开始diverge——这preview了repo-level的趋势，
      更大模型+更复杂任务下CWM failure modes逐渐显现。
      DeepSeek作为完全不同的architecture（不同tokenizer、不同attention实现、不同pretraining data）
      仍然reproduce null result，说明这是task-level property而非model-level artifact。

  - name: "DeepSeek Repo-Level Classification"
    plan_id: "deepseek-cls-repo"
    description: >
      DeepSeek-Coder-6.7B LoRA classification在repo-level SWE-bench-PerTest数据上。
      验证classification formulation的repo-level advantage在不同architecture下是否保持。
    expected_results:
      accuracy: 81.5
      f1_macro: 76.8
      fail_f1: 65.2
      pass_f1: 88.4
      fail_precision: 68.5
      fail_recall: 62.1
      pass_precision: 85.3
      pass_recall: 91.7
      unparseable: 0
      majority_baseline: 72.96
      gap_vs_majority_pp: 8.5
      qwen8b_repo_accuracy: 85.5
      deepseek_vs_qwen_gap_pp: -4.0
      deepseek_func_to_repo_drop_pp: -4.8
    result_rationale: >
      DeepSeek repo-level CLS预期81.5% accuracy，低于Qwen3-8B的85.5%（-4.0pp），原因：
      (1) DeepSeek-Coder-6.7B的context window限制（16K vs Qwen3-8B的32K），
      repo-level input平均6.8K tokens，更多cases需要truncation；
      (2) DeepSeek的code understanding在repo-level cross-file dependencies上弱于newer Qwen3，
      pretraining data中repo-level code comprehension的覆盖不足；
      (3) 6.7B vs 8B的参数差距虽小，但Qwen3架构效率更高（GQA + sliding window attention）。
      从function-level 86.3%到repo-level 81.5%的drop（-4.8pp）与Qwen3-8B的drop（-4.3pp）相近，
      说明classification formulation在不同architecture上有consistent的degradation pattern。
      关键发现：DeepSeek repo-level CLS（81.5%）仍然远高于majority baseline（72.96%），
      证明classification formulation即使在非SOTA architecture上也能provide reliable verification。
      如果DeepSeek CWM repo-level也像Qwen CWM一样unparseable≥80%，
      则完全确认advantage是formulation-driven而非architecture-driven。
    tables:
      - name: "Cross-Architecture Repo-Level CLS Comparison"
        columns: [Architecture, Size, Func CLS Acc, Repo CLS Acc, "Drop (pp)"]
        rows:
          - [Qwen3, 4B, 88.41%, "~83.6%*", -4.8]
          - [Qwen3, 8B, 89.75%, 85.5%, -4.3]
          - [DeepSeek-Coder, 6.7B, 86.3%, 81.5%, -4.8]
        footnotes:
          - "*4B repo results from cls4b-v5-ckpt4600 test eval"
    figures_description:
      - "Function → Repo accuracy drop comparison across architectures，三组paired bars展示consistent ~4-5pp drop"
    analysis: >
      DeepSeek repo-level CLS是supplementary evidence，不是核心result。
      其价值在于展示classification formulation的robustness across architectures：
      即使换一个完全不同的model family，repo-level CLS仍然work（>>majority baseline），
      而CWM仍然fail（unparseable dominant）。
      这是architecture independence claim在repo-level的延伸验证。

  - name: "Repo-Level Error Complementarity & Oracle Ensemble"
    plan_id: "repo-level-training"
    description: >
      分析repo-level CLS和CWM（parseable subset）的error complementarity。
      计算oracle ensemble accuracy——如果两个模型的错误不重叠，ensemble ceiling多高。
      扩展function-level的complementarity finding（oracle=90.63%）到repo-level。
    expected_results:
      cls_repo_accuracy: 85.5
      cwm_repo_accuracy_parseable: 64.0
      cwm_repo_parseable_pct: 15.0
      oracle_accuracy_parseable_subset: 91.2
      cls_error_type_dominant: "miss_bug (false_negative)"
      cwm_error_type_dominant: "false_alarm + unparseable"
      complementarity_rate: 0.68
      cls_only_correct_pct: 34.5
      cwm_only_correct_pct: 8.2
      both_correct_pct: 48.8
      both_wrong_pct: 8.5
      n_parseable_samples: 1468
    result_rationale: >
      Repo-level complementarity analysis限于CWM parseable subset（~15% of total，~1468 samples）。
      在这个subset上，CLS accuracy ~85.5%，CWM accuracy ~64%——
      但两者的error pattern高度complementary（complementarity rate 0.68）。
      CLS的dominant error是miss bugs（false negative）：模型对长context中的subtle bugs不敏感，
      倾向于predict pass。CWM的dominant error是false alarms：
      生成的output与gold不完全match被判为fail，即使语义上patch是correct的。
      Oracle ensemble在parseable subset上达91.2%，证明两种formulation捕获不同的code semantics。
      但CWM的85% unparseable严重限制了ensemble的实际应用——
      只有15%的predictions可以ensemble，对overall accuracy的提升有限。
      这为paper提供了nuanced finding：complementarity存在但CWM的formulation bottleneck
      使其无法被充分利用。Future work可以探索更好的generation formulation来保留complementarity
      同时降低unparseable rate。
    tables:
      - name: "Repo-Level Error Complementarity (Parseable Subset)"
        columns: [Category, "%"]
        rows:
          - [Both correct, 48.8%]
          - [CLS only correct, 34.5%]
          - [CWM only correct, 8.2%]
          - [Both wrong, 8.5%]
          - [Oracle accuracy, 91.2%]
      - name: "Function vs Repo Error Complementarity"
        columns: [Level, CLS Acc, CWM Acc, Oracle Acc, Complementarity]
        rows:
          - [Function (4B), 87.5%, 87.5%, 90.63%, 0.72]
          - ["Repo (8B, parseable)", 85.5%, 64.0%, 91.2%, 0.68]
    figures_description:
      - "Venn diagram of error overlap at repo-level，展示CLS和CWM的error union structure"
    analysis: >
      Repo-level complementarity结果有两面性：
      (1) 好消息：在parseable subset上oracle达91.2%，与function-level的90.63%相近，
      说明CLS和CWM在能work的cases上仍然是complementary的。
      (2) 坏消息：85% unparseable意味着ensemble只覆盖15%的predictions。
      论文中应frame为：complementarity是formulation-level property（与complexity无关），
      但CWM的generation bottleneck在高complexity下限制了其utility。
      这motivates future work on improved generation formulations that maintain complementarity
      while achieving better parsability。

  - name: "Diagnostic Re-repair Experiment"
    plan_id: "diagnostic-rerepair"
    description: >
      200-instance downstream proof-of-concept：repair agent在per-test failure predictions
      指导下vs无per-test信息，比较resolve rate。使用SWE-agent framework。
    expected_results:
      n_instances: 200
      baseline_resolve_rate_pct: 27.0
      rerepair_blind_resolve_rate_pct: 29.5
      rerepair_with_diagnostics_resolve_rate_pct: 33.0
      diagnostic_lift_pp: 6.0
      blind_lift_pp: 2.5
      diagnostic_specific_lift_pp: 3.5
      n_initially_unresolved: 146
      n_rerepair_triggered: 92
      rerepair_success_with_diag_pct: 25.0
      rerepair_success_without_diag_pct: 13.0
      mcnemar_pvalue: 0.022
      multi_f2p_diagnostic_lift_pp: 11.5
      single_f2p_diagnostic_lift_pp: 2.0
      multi_f2p_n_instances: 62
      single_f2p_n_instances: 138
      avg_rerepair_attempts: 1.8
      per_test_prediction_accuracy_on_tested: 84.2
    result_rationale: >
      Diagnostic lift 6.0pp（best tier范围[3,8]）的机制：
      (1) Per-test predictions为repair agent提供failure localization——
      当agent知道"test_parse_edge_case fails but test_basic passes"时，
      修复集中在edge case logic而非盲目重试entire solution；
      (2) Blind re-repair（知道unresolved但不知哪个test fail）仍有2.5pp lift，
      因为SWE-agent的retry本身就有correction概率——
      但diagnostic-specific增量3.5pp证明per-test信息的独特贡献；
      (3) 优势严重集中于multi-F2P instances：
      T≥2时lift 11.5pp vs T=1时仅2.0pp，与oracle analysis预测完全一致。
      原因：T=1时per-test info等价于trajectory info（只有一个fail test，
      知道"有test fail"和知道"test_X fail"信息量相同）；
      T≥2时per-test info区分了不同failure patterns，
      repair agent可以逐个target failing tests而非guess which test fails。
      McNemar p=0.022在200样本下达到显著性（<0.05）——
      虽然样本量有限但足以支撑proof-of-concept级别的claim。
      92/146 re-repair triggered表明63%的unresolved instances至少尝试了re-repair；
      with diagnostics的25% success rate vs without的13%证明信息质量差异。
      Per-test prediction accuracy on re-repair测试的84.2%与overall 85.5%接近，
      说明re-repair并未选择性地作用于easy/hard cases。
    tables:
      - name: "Diagnostic Re-repair Results"
        columns: [Condition, Resolve Rate, "Δ vs Baseline"]
        rows:
          - [No re-repair (baseline), 27.0%, —]
          - [Re-repair without diagnostics, 29.5%, "+2.5 pp"]
          - [Re-repair with per-test diagnostics, 33.0%, "+6.0 pp"]
          - [Diagnostic-specific lift, —, "+3.5 pp (p=0.022)"]
      - name: "Diagnostic Lift Stratified by F2P Count"
        columns: ["F2P Count", "N Instances", "Diag Lift", "Blind Lift"]
        rows:
          - ["T=1", 138, "+2.0 pp", "+1.5 pp"]
          - ["T≥2", 62, "+11.5 pp", "+3.8 pp"]
          - ["Overall", 200, "+6.0 pp", "+2.5 pp"]
    figures_description:
      - "Grouped bar chart: three conditions × T=1 vs T≥2 stratification"
      - "Per-instance resolve rate improvement scatter: x=N failing tests, y=resolve rate delta"
    analysis: >
      Re-repair实验完成了Claim 2的实证闭环：per-test classification不仅在accuracy上等价于trajectory
      （TOST p=0.007），还提供了actionable的diagnostic信息带来6pp resolve rate improvement。
      Stratification连接Claim 2和Claim 3：advantage集中在multi-F2P instances（与oracle预测一致），
      为部署决策提供了清晰框架——在multi-F2P场景下per-test verification的ROI最高。
      论文应定位为proof-of-concept，目标是展示mechanism而非claim SOTA repair performance。
      200 instances是moderate sample size，sufficient for significance但reviewer可能要求larger scale——
      frame为future work方向。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "165f2549-4a7a-4ddc-840b-8b82279dfd79",
  "isSidechain": false,
  "requestId": "req_011Cb5sNpxhAB8RycrCjL4FE",
  "type": "assistant",
  "uuid": "ee63c1fa-e91f-4896-817d-14aa2b9ca184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2dRc2F42eefdfC6a9Rtwa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20078,
      "cache_read_input_tokens": 46906,
      "output_tokens": 23055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20078,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 23055,
          "cache_read_input_tokens": 46906,
          "cache_creation_input_tokens": 20078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20078
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Repo-level CLS显著优于CWM，DeepSeek复现确认架构无关性，formulation advantage story完整成立 核心假设：['Repo-level CLS多seed稳定≥85% accuracy，fail_f1≥75%（当前单seed: 84.79%/81.18%）', 'CW…",
  "leafUuid": "ee63c1fa-e91f-4896-817d-14aa2b9ca184",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Define best-tier results for repo-level verification via three-level evidence chain",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Repo-level CLS显著优于CWM，DeepSeek复现确认架构无关性，formulation advantage story完整成立 核心假设：['Repo-level CLS多seed稳定≥85% accuracy，fail_f1≥75%（当前单seed: 84.79%/81.18%）', 'CW…",
  "leafUuid": "ee63c1fa-e91f-4896-817d-14aa2b9ca184",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Define best-tier results for repo-level verification via three-level evidence chain",
  "sessionId": "caf3dc6a-df31-4098-9ba6-e664e5fc658f"
}
```

---
